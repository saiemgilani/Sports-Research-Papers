#!/usr/bin/env python3
"""Download sports analytics papers from configured feeds.

The script is deliberately conservative:
- it only writes files that are verified as PDF bytes;
- it only uses authentication cookies explicitly supplied by the user;
- it records each download in library/manifest.jsonl for deduplication.
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


USER_AGENT = (
    "Sports-Research-Papers feed updater "
    "(public PDFs only; https://github.com/)"
)
PDF_MAGIC = b"%PDF"
DEFAULT_CONFIG = Path("feeds/download-sources.json")
DEFAULT_MANIFEST = Path("library/manifest.jsonl")
DEFAULT_COOKIE_DOMAINS = {
    "degruyter.com",
    "www.degruyter.com",
    "degruyterbrill.com",
    "www.degruyterbrill.com",
}
AUTH_COOKIE_HEADER = ""
AUTH_COOKIE_DOMAINS: set[str] = set()


@dataclass
class FeedItem:
    title: str
    link: str
    published: str = ""
    authors: list[str] | None = None
    doi: str = ""


@dataclass
class DownloadResult:
    source_id: str
    source_name: str
    title: str
    authors: list[str]
    year: str
    item_url: str
    pdf_url: str
    path: str
    sha256: str
    bytes: int
    downloaded_at: str
    doi: str = ""


def cookie_domain_matches(host: str, domain: str) -> bool:
    domain = domain.lstrip(".").lower()
    host = host.lower()
    return host == domain or host.endswith(f".{domain}")


def auth_cookie_for_url(url: str) -> str:
    if not AUTH_COOKIE_HEADER:
        return ""
    host = urllib.parse.urlparse(url).hostname or ""
    if any(cookie_domain_matches(host, domain) for domain in AUTH_COOKIE_DOMAINS):
        return AUTH_COOKIE_HEADER
    return ""


def fetch(url: str, timeout: int = 30, accept: str = "*/*") -> tuple[bytes, str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": accept,
    }
    cookie_header = auth_cookie_for_url(url)
    if cookie_header:
        headers["Cookie"] = cookie_header
    request = urllib.request.Request(
        url,
        headers=headers,
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()
        return response.read(), content_type, final_url


def text_from_bytes(data: bytes) -> str:
    for encoding in ("utf-8", "utf-8-sig", "iso-8859-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, names: Iterable[str]) -> str:
    wanted = {name.lower() for name in names}
    for child in list(element):
        if local_name(child.tag) in wanted and child.text:
            return clean_text(child.text)
    return ""


def child_attr(element: ET.Element, child_name: str, attr_name: str) -> str:
    for child in list(element):
        if local_name(child.tag) == child_name.lower():
            return child.attrib.get(attr_name, "")
    return ""


def parse_feed(data: bytes) -> list[FeedItem]:
    root = ET.fromstring(data)
    items: list[FeedItem] = []

    # RSS 2.0 channel/item and RDF RSS item forms.
    feed_items = [
        element
        for element in root.iter()
        if local_name(element.tag) in {"item", "entry"}
    ]

    for element in feed_items:
        title = child_text(element, ["title"])
        link = child_text(element, ["link"])
        if not link:
            link = child_attr(element, "link", "href")
        published = child_text(element, ["pubDate", "date", "published", "updated"])
        doi = child_text(element, ["doi"])
        authors = parse_author_string(
            child_text(element, ["creator", "author", "description"])
        )
        if title and link:
            items.append(
                FeedItem(
                    title=title,
                    link=link,
                    published=published,
                    authors=authors,
                    doi=doi,
                )
            )
    return items


def parse_author_string(value: str) -> list[str]:
    value = clean_text(value)
    if not value:
        return []
    value = re.sub(r"\bAbstract\b.*$", "", value, flags=re.IGNORECASE).strip()
    parts = re.split(r"\s*;\s*|\s*,\s+(?=[A-Z][A-Za-z.' -]+(?:\s|$))", value)
    authors = [part.strip(" .") for part in parts if 2 < len(part.strip()) < 120]
    return authors[:12]


def meta_values(page: str, name: str) -> list[str]:
    pattern = re.compile(
        r"<meta\s+[^>]*(?:name|property)\s*=\s*['\"]"
        + re.escape(name)
        + r"['\"][^>]*content\s*=\s*['\"]([^'\"]+)['\"][^>]*>",
        re.IGNORECASE,
    )
    return [html.unescape(match.group(1)).strip() for match in pattern.finditer(page)]


def tag_text(page: str, tag_name: str, href: str) -> str:
    pattern = re.compile(
        r"<a\b[^>]*href\s*=\s*['\"]"
        + re.escape(href)
        + r"['\"][^>]*>(.*?)</a>",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(page)
    if not match:
        return ""
    return clean_text(match.group(1))


def href_values(page: str) -> list[str]:
    pattern = re.compile(r"href\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
    return [html.unescape(match.group(1)).strip() for match in pattern.finditer(page)]


def find_pdf_candidates(page: str, base_url: str) -> list[str]:
    candidates: list[str] = []
    candidates.extend(meta_values(page, "citation_pdf_url"))
    parsed_base = urllib.parse.urlparse(base_url)
    if "/document/doi/" in parsed_base.path and parsed_base.path.endswith("/html"):
        candidates.append(urllib.parse.urlunparse(parsed_base._replace(path=parsed_base.path[:-5] + "/pdf")))
    for href in href_values(page):
        lowered = href.lower()
        if ".pdf" in lowered or "doi/pdf" in lowered or "hfpdf.php" in lowered:
            candidates.append(href)

    absolute: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        url = urllib.parse.urljoin(base_url, candidate)
        if url not in seen:
            seen.add(url)
            absolute.append(url)
    return absolute


def doi_from_url(url: str) -> str:
    match = re.search(r"/document/doi/(10\.[^/]+/[^/]+)/", url)
    if match:
        return urllib.parse.unquote(match.group(1))
    return ""


def parse_html_index(data: bytes, base_url: str, source: dict) -> list[FeedItem]:
    page = text_from_bytes(data)
    include_patterns = source.get("include_href_patterns") or ["/document/doi/"]
    exclude_patterns = source.get("exclude_href_patterns") or []
    seen: set[str] = set()
    items: list[FeedItem] = []

    for href in href_values(page):
        if not any(pattern in href for pattern in include_patterns):
            continue
        if any(pattern in href for pattern in exclude_patterns):
            continue
        url = urllib.parse.urljoin(base_url, href)
        url = re.sub(r"/pdf(?:\?.*)?$", "/html", url)
        if url in seen:
            continue
        seen.add(url)
        title = tag_text(page, "a", href) or doi_from_url(url) or url
        items.append(
            FeedItem(
                title=title,
                link=url,
                doi=doi_from_url(url),
            )
        )

    return items


def enrich_from_page(item: FeedItem, page: str) -> FeedItem:
    titles = meta_values(page, "citation_title")
    author_values = meta_values(page, "citation_author")
    authors: list[str] = []
    for value in author_values:
        authors.extend(parse_author_string(value))
    dates = (
        meta_values(page, "citation_publication_date")
        or meta_values(page, "citation_online_date")
        or meta_values(page, "citation_date")
    )
    dois = meta_values(page, "citation_doi")
    return FeedItem(
        title=clean_text(titles[0]) if titles else item.title,
        link=item.link,
        published=dates[0] if dates else item.published,
        authors=authors if authors else item.authors,
        doi=dois[0] if dois else item.doi,
    )


def is_pdf(data: bytes, content_type: str) -> bool:
    return data.startswith(PDF_MAGIC) or "application/pdf" in content_type.lower()


def year_from_item(item: FeedItem) -> str:
    candidates = [item.published, item.title, item.link]
    for candidate in candidates:
        if not candidate:
            continue
        parsed = email.utils.parsedate_to_datetime(candidate) if "," in candidate else None
        if parsed:
            return f"{parsed.year:04d}"
        match = re.search(r"\b(19|20)\d{2}\b", candidate)
        if match:
            return match.group(0)
    return "undated"


def first_author_label(authors: list[str]) -> str:
    if not authors:
        return "Unknown Authors"
    first = authors[0]
    last = first.split()[-1].strip(",")
    if len(authors) == 1:
        return last
    return f"{last} et al"


def safe_component(value: str, max_length: int = 140) -> str:
    value = html.unescape(value)
    value = value.replace("&", " and ")
    value = re.sub(r"[^\w .,'()+-]+", " ", value, flags=re.ASCII)
    value = re.sub(r"\s+", " ", value).strip(" .")
    if not value:
        value = "untitled"
    return value[:max_length].rstrip(" .")


def destination_for(root: Path, source: dict, item: FeedItem) -> Path:
    year = year_from_item(item)
    category = [safe_component(part, 80) for part in source["category_path"]]
    title = safe_component(item.title)
    author = safe_component(first_author_label(item.authors or []), 60)
    filename = f"{year} - {title} - {author}.pdf"
    return root.joinpath(*category, year, filename)


def source_requires_auth(source: dict) -> bool:
    return bool(source.get("requires_auth"))


def load_manifest(path: Path) -> dict[str, dict]:
    records: dict[str, dict] = {}
    if not path.exists():
        return records
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = record.get("dedupe_key") or record.get("sha256") or record.get("item_url")
        if key:
            records[key] = record
    return records


def append_manifest(path: Path, record: DownloadResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "dedupe_key": record.doi or record.item_url,
        "source_id": record.source_id,
        "source_name": record.source_name,
        "title": record.title,
        "authors": record.authors,
        "year": record.year,
        "doi": record.doi,
        "item_url": record.item_url,
        "pdf_url": record.pdf_url,
        "path": record.path,
        "sha256": record.sha256,
        "bytes": record.bytes,
        "downloaded_at": record.downloaded_at,
    }
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(data, sort_keys=True) + "\n")


def process_item(
    source: dict,
    item: FeedItem,
    root: Path,
    manifest: dict[str, dict],
    dry_run: bool,
) -> DownloadResult | None:
    dedupe_key = item.doi or item.link
    if dedupe_key in manifest:
        print(f"skip existing: {item.title}")
        return None

    try:
        page_bytes, page_type, page_url = fetch(item.link, accept="text/html,application/xhtml+xml,*/*")
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"skip fetch failed: {item.link} ({exc})")
        return None

    pdf_candidates: list[str]
    enriched = item
    if is_pdf(page_bytes, page_type):
        pdf_candidates = [page_url]
        pdf_bytes = page_bytes
        pdf_url = page_url
    else:
        page = text_from_bytes(page_bytes)
        enriched = enrich_from_page(item, page)
        pdf_candidates = find_pdf_candidates(page, page_url)
        pdf_bytes = b""
        pdf_url = ""

    for candidate in pdf_candidates:
        try:
            if pdf_url != candidate:
                pdf_bytes, pdf_type, final_pdf_url = fetch(candidate, accept="application/pdf,*/*")
            else:
                pdf_type = page_type
                final_pdf_url = pdf_url
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"skip pdf fetch failed: {candidate} ({exc})")
            continue

        if not is_pdf(pdf_bytes, pdf_type):
            print(f"skip non-pdf response: {candidate}")
            continue

        destination = destination_for(root, source, enriched)
        sha256 = hashlib.sha256(pdf_bytes).hexdigest()
        if any(record.get("sha256") == sha256 for record in manifest.values()):
            print(f"skip duplicate hash: {enriched.title}")
            return None

        if dry_run:
            print(f"would download: {final_pdf_url} -> {destination}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists():
                stem = destination.stem
                destination = destination.with_name(f"{stem} - {sha256[:8]}.pdf")
            destination.write_bytes(pdf_bytes)
            print(f"downloaded: {destination}")

        return DownloadResult(
            source_id=source["id"],
            source_name=source["name"],
            title=enriched.title,
            authors=enriched.authors or [],
            year=year_from_item(enriched),
            doi=enriched.doi,
            item_url=enriched.link,
            pdf_url=final_pdf_url,
            path=str(destination).replace(os.sep, "/"),
            sha256=sha256,
            bytes=len(pdf_bytes),
            downloaded_at=datetime.now(timezone.utc).isoformat(),
        )

    print(f"skip no public pdf found: {item.title}")
    return None


def run(args: argparse.Namespace) -> int:
    configure_auth(args)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    root = Path(config.get("download_root", "library"))
    manifest_path = args.manifest
    manifest = load_manifest(manifest_path)
    source_filter = set(args.source or [])
    total_downloaded = 0

    for source in config["sources"]:
        if source_filter and source["id"] not in source_filter:
            continue
        print(f"source: {source['id']} - {source['name']}")
        if source_requires_auth(source) and not AUTH_COOKIE_HEADER:
            print(
                f"skip source requires auth cookies: {source['id']} "
                "(set JQAS_COOKIE, JQAS_COOKIE_FILE, or JQAS_STORAGE_STATE)"
            )
            continue
        try:
            feed_bytes, _, feed_url = fetch(
                source["feed_url"],
                accept="application/rss+xml,application/xml,text/xml,text/html,*/*",
            )
            if source.get("feed_type") == "html_index":
                items = parse_html_index(feed_bytes, feed_url, source)
            else:
                items = parse_feed(feed_bytes)
        except (ET.ParseError, urllib.error.URLError, TimeoutError) as exc:
            print(f"skip source failed: {source['id']} ({exc})")
            continue

        if args.max_items:
            items = items[: args.max_items]

        for item in items:
            result = process_item(source, item, root, manifest, args.dry_run)
            if result:
                total_downloaded += 1
                if not args.dry_run:
                    append_manifest(manifest_path, result)
                    manifest[result.doi or result.item_url] = {
                        "sha256": result.sha256,
                        "item_url": result.item_url,
                    }
            if args.sleep:
                time.sleep(args.sleep)

    print(f"downloaded_count={total_downloaded}")
    return 0


def cookie_header_from_netscape(path: Path, domains: set[str]) -> str:
    pairs: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 7:
            continue
        domain, _, _, _, _, name, value = parts[:7]
        if any(cookie_domain_matches(domain.lstrip("."), allowed) for allowed in domains):
            pairs[name] = value
    return "; ".join(f"{name}={value}" for name, value in sorted(pairs.items()))


def cookie_header_from_storage_state(path: Path, domains: set[str]) -> str:
    state = json.loads(path.read_text(encoding="utf-8"))
    pairs: dict[str, str] = {}
    for cookie in state.get("cookies", []):
        domain = str(cookie.get("domain", "")).lstrip(".")
        if any(cookie_domain_matches(domain, allowed) for allowed in domains):
            name = str(cookie.get("name", ""))
            value = str(cookie.get("value", ""))
            if name:
                pairs[name] = value
    return "; ".join(f"{name}={value}" for name, value in sorted(pairs.items()))


def configure_auth(args: argparse.Namespace) -> None:
    global AUTH_COOKIE_DOMAINS, AUTH_COOKIE_HEADER
    domains = set(DEFAULT_COOKIE_DOMAINS)
    env_domains = os.environ.get("JQAS_COOKIE_DOMAINS", "")
    domains.update(domain.strip() for domain in env_domains.split(",") if domain.strip())
    AUTH_COOKIE_DOMAINS = domains

    if args.cookie:
        AUTH_COOKIE_HEADER = args.cookie.strip()
    elif args.cookie_file:
        AUTH_COOKIE_HEADER = cookie_header_from_netscape(args.cookie_file, domains)
    elif args.storage_state:
        AUTH_COOKIE_HEADER = cookie_header_from_storage_state(args.storage_state, domains)
    elif os.environ.get("JQAS_COOKIE"):
        AUTH_COOKIE_HEADER = os.environ["JQAS_COOKIE"].strip()
    elif os.environ.get("JQAS_COOKIE_FILE"):
        AUTH_COOKIE_HEADER = cookie_header_from_netscape(Path(os.environ["JQAS_COOKIE_FILE"]), domains)
    elif os.environ.get("JQAS_STORAGE_STATE"):
        AUTH_COOKIE_HEADER = cookie_header_from_storage_state(Path(os.environ["JQAS_STORAGE_STATE"]), domains)

    if AUTH_COOKIE_HEADER:
        print(f"auth cookies enabled for domains: {', '.join(sorted(domains))}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--source", action="append", help="Only process this source id. May be repeated.")
    parser.add_argument("--max-items", type=int, default=0, help="Limit items per source.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Delay between item requests.")
    parser.add_argument("--cookie", help="Cookie header for authorized JQAS/De Gruyter access.")
    parser.add_argument("--cookie-file", type=Path, help="Netscape cookies.txt file for authorized access.")
    parser.add_argument("--storage-state", type=Path, help="Playwright storage_state.json file for authorized access.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
