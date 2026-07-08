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
import subprocess
import sys
import time
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

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
    "content.iospress.com",
    "iospress.com",
    "journals.sagepub.com",
    "sagepub.com",
}
AUTH_COOKIE_HEADER = ""
AUTH_COOKIE_DOMAINS: set[str] = set()
BROWSER_STORAGE_STATE: Path | None = None
BROWSER_FALLBACK = False
UNPAYWALL_EMAIL = ""


@dataclass
class FeedItem:
    title: str
    link: str
    published: str = ""
    authors: list[str] | None = None
    doi: str = ""
    pdf_candidates: list[str] | None = None


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


def parse_crossref(data: bytes, source: dict) -> list[FeedItem]:
    payload = json.loads(text_from_bytes(data))
    records = payload.get("message", {}).get("items", [])
    items: list[FeedItem] = []
    for record in records:
        doi = str(record.get("DOI", "")).strip()
        title_values = record.get("title") or []
        title = clean_text(title_values[0]) if title_values else doi
        if not doi or not title:
            continue
        min_volume = source.get("min_volume")
        volume = str(record.get("volume", "")).strip()
        if min_volume is not None:
            try:
                if int(volume) < int(min_volume):
                    continue
            except ValueError:
                continue
        if any(pattern.lower() in title.lower() for pattern in source.get("exclude_title_patterns", [])):
            continue
        authors = [
            clean_text(" ".join(part for part in [author.get("given", ""), author.get("family", "")] if part))
            for author in record.get("author", [])
        ]
        authors = [author for author in authors if author]
        published = crossref_date(record)
        article_url = source.get("article_url_template", "https://doi.org/{doi}").format(
            doi=urllib.parse.quote(doi, safe="/")
        )
        items.append(
            FeedItem(
                title=title,
                link=article_url,
                published=published,
                authors=authors,
                doi=doi,
                pdf_candidates=crossref_pdf_candidates(record) + sage_pdf_candidates(doi),
            )
        )
    return items


def parse_static_items(source: dict) -> list[FeedItem]:
    items: list[FeedItem] = []
    for record in source.get("items", []):
        title = clean_text(str(record.get("title", "")))
        link = str(record.get("item_url") or record.get("url") or "").strip()
        pdf_url = str(record.get("pdf_url") or "").strip()
        if not title or not (link or pdf_url):
            continue
        items.append(
            FeedItem(
                title=title,
                link=link or pdf_url,
                published=str(record.get("year", "")).strip(),
                authors=[clean_text(str(author)) for author in record.get("authors", []) if clean_text(str(author))],
                doi=str(record.get("doi", "")).strip(),
                pdf_candidates=[pdf_url] if pdf_url else [],
            )
        )
    return items


def crossref_pdf_candidates(record: dict) -> list[str]:
    candidates: list[str] = []
    for link in record.get("link", []) or []:
        content_type = str(link.get("content-type", "")).lower()
        url = str(link.get("URL", "")).strip()
        if url and "pdf" in content_type:
            candidates.append(url)
    return unique_urls(candidates)


def crossref_date(record: dict) -> str:
    for key in ("published-print", "published-online", "published", "issued"):
        date_parts = record.get(key, {}).get("date-parts", [])
        if not date_parts or not date_parts[0]:
            continue
        parts = [int(part) for part in date_parts[0]]
        while len(parts) < 3:
            parts.append(1)
        return f"{parts[0]:04d}-{parts[1]:02d}-{parts[2]:02d}"
    return ""


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


def context_heading_after_href(page: str, href: str) -> str:
    pattern = re.compile(
        r"<a\b[^>]*href\s*=\s*['\"]"
        + re.escape(href)
        + r"['\"][^>]*>.*?</a>",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(page)
    if not match:
        return ""
    following = page[match.end() : match.end() + 2500]
    heading = re.search(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", following, re.IGNORECASE | re.DOTALL)
    if not heading:
        return ""
    title = clean_text(heading.group(1))
    if title.lower() in {"abstract", "biography"}:
        following = following[heading.end() :]
        heading = re.search(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", following, re.IGNORECASE | re.DOTALL)
        title = clean_text(heading.group(1)) if heading else ""
    return title


def title_from_href(href: str) -> str:
    parsed = urllib.parse.urlparse(href)
    name = Path(urllib.parse.unquote(parsed.path)).stem
    name = re.sub(r"[_-]+", " ", name)
    name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)
    return clean_text(name)


def generic_link_text(value: str) -> bool:
    normalized = clean_text(value).lower().strip("()[] ")
    return normalized in {
        "",
        "pdf",
        "paper",
        "view paper",
        "download",
        "download paper",
        "download pdf",
        "download the full paper here",
        "full conference program",
    }


def year_from_source_url(url: str) -> str:
    match = re.search(r"\b(19|20)\d{2}\b", url)
    if match:
        return match.group(0)
    match = re.search(r"nessis(\d{2})", url, flags=re.IGNORECASE)
    if match:
        year = int(match.group(1))
        return f"{2000 + year:04d}" if year < 70 else f"{1900 + year:04d}"
    return ""


def href_values(page: str) -> list[str]:
    pattern = re.compile(r"href\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
    return [html.unescape(match.group(1)).strip() for match in pattern.finditer(page)]


def unique_values(values: Iterable[str]) -> list[str]:
    unique: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        unique.append(value)
    return unique


def unique_urls(values: Iterable[str], base_url: str = "") -> list[str]:
    urls = [
        urllib.parse.urljoin(base_url, value.strip())
        for value in values
        if value and value.strip()
    ]
    return unique_values(urls)


def find_pdf_candidates(page: str, base_url: str) -> list[str]:
    candidates: list[str] = []
    candidates.extend(meta_values(page, "citation_pdf_url"))
    parsed_base = urllib.parse.urlparse(base_url)
    if "/document/doi/" in parsed_base.path and parsed_base.path.endswith("/html"):
        candidates.append(urllib.parse.urlunparse(parsed_base._replace(path=parsed_base.path[:-5] + "/pdf")))
    doi = doi_from_url(base_url)
    if doi:
        candidates.extend(sage_pdf_candidates(doi))
    for href in href_values(page):
        lowered = href.lower()
        if ".pdf" in lowered or "doi/pdf" in lowered or "hfpdf.php" in lowered:
            candidates.append(href)

    return unique_urls(candidates, base_url)


def doi_from_url(url: str) -> str:
    match = re.search(r"/document/doi/(10\.[^/]+/[^/]+)/", url)
    if match:
        return urllib.parse.unquote(match.group(1))
    match = re.search(r"/doi/(?:abs|full|pdf|epdf)?/?(10\.[^?#]+)", url)
    if match:
        return urllib.parse.unquote(match.group(1)).rstrip("/")
    return ""


def sage_pdf_candidates(doi: str) -> list[str]:
    if not doi:
        return []
    encoded_doi = urllib.parse.quote(doi, safe="/")
    candidates = [
        f"https://journals.sagepub.com/doi/pdf/{encoded_doi}",
        f"https://journals.sagepub.com/doi/epdf/{encoded_doi}",
    ]
    for ios_code in ios_press_jsa_codes(doi):
        candidates.append(
            "https://content.iospress.com/download/journal-of-sports-analytics/"
            f"{ios_code}?id=journal-of-sports-analytics%2F{ios_code}"
        )
    return candidates


def ios_press_jsa_codes(doi: str) -> list[str]:
    match = re.fullmatch(r"10\.3233/JSA-(\d+)", doi, flags=re.IGNORECASE)
    if not match:
        return []
    digits = match.group(1)
    candidates = [f"jsa{digits.lower()}"]
    if len(digits) == 6:
        candidates.append(f"jsa{int(digits[2:]):04d}")
        candidates.append(f"jsa{int(digits[2:])}")
    return unique_values(candidates)


def unpaywall_pdf_candidates(doi: str) -> list[str]:
    if not doi or not UNPAYWALL_EMAIL:
        return []
    url = (
        "https://api.unpaywall.org/v2/"
        + urllib.parse.quote(doi, safe="/")
        + "?email="
        + urllib.parse.quote(UNPAYWALL_EMAIL, safe="@")
    )
    try:
        data, _, _ = fetch(url, accept="application/json,*/*")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"skip Unpaywall lookup failed: {doi} ({exc})")
        return []
    try:
        payload = json.loads(text_from_bytes(data))
    except json.JSONDecodeError as exc:
        print(f"skip Unpaywall lookup failed: {doi} ({exc})")
        return []
    candidates: list[str] = []
    best = payload.get("best_oa_location") or {}
    candidates.extend(
        str(best.get(key, "")).strip()
        for key in ("url_for_pdf", "url")
        if best.get(key)
    )
    for location in payload.get("oa_locations") or []:
        candidates.extend(
            str(location.get(key, "")).strip()
            for key in ("url_for_pdf", "url")
            if location.get(key)
        )
    return unique_urls(candidates)


def legacy_issue_url_from_item(item_url: str, source_url: str = "") -> str:
    doi = doi_from_url(item_url)
    if not doi.startswith("10.1515/1559-0410."):
        return ""
    source_match = re.search(r"/journal/key/jqas/(\d+)/(\d+)/html", source_url)
    if not source_match:
        return ""
    volume = int(source_match.group(1))
    issue = int(source_match.group(2))
    year = volume + 2004
    article = doi.rsplit("/", 1)[-1]
    return (
        "https://www.degruyter.com/view/j/"
        f"jqas.{year}.{volume}.issue-{issue}/{article}/{article}.xml?format=INT"
    )


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
        link_title = tag_text(page, "a", href)
        title = link_title if not generic_link_text(link_title) else ""
        if not title:
            title = context_heading_after_href(page, href)
        if not title:
            title = doi_from_url(url) or title_from_href(url) or url
        items.append(
            FeedItem(
                title=title,
                link=legacy_issue_url_from_item(url, base_url) or url,
                published=year_from_source_url(base_url),
                doi=doi_from_url(url),
                pdf_candidates=legacy_pdf_candidates(url, base_url),
            )
        )

    return items


def legacy_pdf_candidates(item_url: str, source_url: str = "") -> list[str]:
    doi = doi_from_url(item_url)
    if not doi.startswith("10.1515/1559-0410."):
        return []
    source_match = re.search(r"/journal/key/jqas/(\d+)/(\d+)/html", source_url)
    if not source_match:
        return []
    volume = int(source_match.group(1))
    issue = int(source_match.group(2))
    year = volume + 2004
    article = doi.rsplit("/", 1)[-1]
    return [
        (
            "https://www.degruyter.com/downloadpdf/j/"
            f"jqas.{year}.{volume}.issue-{issue}/{article}/{article}.pdf"
        )
    ]


def direct_pdf_candidate(item_url: str) -> str:
    parsed = urllib.parse.urlparse(item_url)
    if "/document/doi/" in parsed.path and parsed.path.endswith("/html"):
        return urllib.parse.urlunparse(parsed._replace(path=parsed.path[:-5] + "/pdf"))
    return ""


def browser_download_pdf(url: str, article_url: str = "") -> tuple[bytes, str] | None:
    if not BROWSER_FALLBACK:
        return None
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            output_pdf = temp_path / "download.pdf"
            output_json = temp_path / "download.json"
            helper = Path(__file__).with_name("playwright_download_pdf.py")
            command = [
                sys.executable,
                str(helper),
                "--url",
                url,
                "--output-pdf",
                str(output_pdf),
                "--output-json",
                str(output_json),
            ]
            if article_url:
                command.extend(["--article-url", article_url])
            if BROWSER_STORAGE_STATE:
                command.extend(["--storage-state", str(BROWSER_STORAGE_STATE)])

            completed = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=90000,
            )
            if completed.returncode != 0:
                message = (completed.stderr or completed.stdout).strip()
                print(f"skip browser pdf fallback failed: {url} ({message})")
                return None
            metadata = json.loads(output_json.read_text(encoding="utf-8"))
            return output_pdf.read_bytes(), metadata.get("url", url)
    except Exception as exc:
        print(f"skip browser pdf fallback failed: {url} ({exc})")
        return None


def source_feed_urls(source: dict) -> list[str]:
    if "feed_urls" in source:
        return [str(url) for url in source["feed_urls"]]
    return [str(source["feed_url"])]


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
        try:
            parsed = email.utils.parsedate_to_datetime(candidate) if "," in candidate else None
        except (TypeError, ValueError):
            parsed = None
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

    item_pdf_candidates = list(item.pdf_candidates or [])
    for candidate in unpaywall_pdf_candidates(item.doi):
        if candidate not in item_pdf_candidates:
            item_pdf_candidates.append(candidate)

    try:
        page_bytes, page_type, page_url = fetch(item.link, accept="text/html,application/xhtml+xml,*/*")
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"skip fetch failed: {item.link} ({exc})")
        page_bytes = b""
        page_type = ""
        page_url = item.link

    pdf_candidates: list[str]
    enriched = item
    if page_bytes and is_pdf(page_bytes, page_type):
        pdf_candidates = [page_url]
        pdf_bytes = page_bytes
        pdf_url = page_url
    elif page_bytes:
        page = text_from_bytes(page_bytes)
        enriched = enrich_from_page(item, page)
        pdf_candidates = list(item_pdf_candidates)
        for candidate in find_pdf_candidates(page, page_url):
            if candidate not in pdf_candidates:
                pdf_candidates.append(candidate)
        pdf_bytes = b""
        pdf_url = ""
    else:
        pdf_candidates = list(item_pdf_candidates)
        direct_candidate = direct_pdf_candidate(item.link)
        if direct_candidate and direct_candidate not in pdf_candidates:
            pdf_candidates.append(direct_candidate)
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
            fallback = browser_download_pdf(candidate, enriched.link)
            if not fallback:
                continue
            pdf_bytes, final_pdf_url = fallback
            pdf_type = "application/pdf"

        if not is_pdf(pdf_bytes, pdf_type):
            fallback = browser_download_pdf(candidate, enriched.link)
            if not fallback:
                print(f"skip non-pdf response: {candidate}")
                continue
            pdf_bytes, final_pdf_url = fallback
            pdf_type = "application/pdf"

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
        items: list[FeedItem] = []
        seen_item_keys: set[str] = set()
        if source.get("feed_type") == "static_items":
            items = parse_static_items(source)
        feed_urls = [] if source.get("feed_type") == "static_items" else source_feed_urls(source)
        for configured_feed_url in feed_urls:
            try:
                feed_bytes, _, feed_url = fetch(
                    configured_feed_url,
                    accept="application/json,application/rss+xml,application/xml,text/xml,text/html,*/*",
                )
                if source.get("feed_type") == "crossref":
                    feed_items = parse_crossref(feed_bytes, source)
                elif source.get("feed_type") == "html_index":
                    feed_items = parse_html_index(feed_bytes, feed_url, source)
                else:
                    feed_items = parse_feed(feed_bytes)
            except (ET.ParseError, urllib.error.URLError, TimeoutError) as exc:
                print(f"skip feed failed: {configured_feed_url} ({exc})")
                continue

            for item in feed_items:
                item_key = item.doi or item.link
                if item_key in seen_item_keys:
                    continue
                seen_item_keys.add(item_key)
                items.append(item)

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
    global AUTH_COOKIE_DOMAINS, AUTH_COOKIE_HEADER, BROWSER_FALLBACK, BROWSER_STORAGE_STATE, UNPAYWALL_EMAIL
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
    elif os.environ.get("PUBLISHER_COOKIE"):
        AUTH_COOKIE_HEADER = os.environ["PUBLISHER_COOKIE"].strip()
    elif os.environ.get("JQAS_COOKIE"):
        AUTH_COOKIE_HEADER = os.environ["JQAS_COOKIE"].strip()
    elif os.environ.get("JSA_COOKIE"):
        AUTH_COOKIE_HEADER = os.environ["JSA_COOKIE"].strip()
    elif os.environ.get("JQAS_COOKIE_FILE"):
        AUTH_COOKIE_HEADER = cookie_header_from_netscape(Path(os.environ["JQAS_COOKIE_FILE"]), domains)
    elif os.environ.get("JSA_COOKIE_FILE"):
        AUTH_COOKIE_HEADER = cookie_header_from_netscape(Path(os.environ["JSA_COOKIE_FILE"]), domains)
    elif os.environ.get("JQAS_STORAGE_STATE"):
        AUTH_COOKIE_HEADER = cookie_header_from_storage_state(Path(os.environ["JQAS_STORAGE_STATE"]), domains)
    elif os.environ.get("JSA_STORAGE_STATE"):
        AUTH_COOKIE_HEADER = cookie_header_from_storage_state(Path(os.environ["JSA_STORAGE_STATE"]), domains)
    elif os.environ.get("PUBLISHER_STORAGE_STATE"):
        AUTH_COOKIE_HEADER = cookie_header_from_storage_state(Path(os.environ["PUBLISHER_STORAGE_STATE"]), domains)

    BROWSER_FALLBACK = bool(args.browser_fallback)
    BROWSER_STORAGE_STATE = args.storage_state
    UNPAYWALL_EMAIL = args.unpaywall_email or os.environ.get("UNPAYWALL_EMAIL", "")
    if not BROWSER_STORAGE_STATE and os.environ.get("JQAS_STORAGE_STATE"):
        BROWSER_STORAGE_STATE = Path(os.environ["JQAS_STORAGE_STATE"])
    if not BROWSER_STORAGE_STATE and os.environ.get("JSA_STORAGE_STATE"):
        BROWSER_STORAGE_STATE = Path(os.environ["JSA_STORAGE_STATE"])
    if not BROWSER_STORAGE_STATE and os.environ.get("PUBLISHER_STORAGE_STATE"):
        BROWSER_STORAGE_STATE = Path(os.environ["PUBLISHER_STORAGE_STATE"])

    if AUTH_COOKIE_HEADER:
        print(f"auth cookies enabled for domains: {', '.join(sorted(domains))}")
    if BROWSER_FALLBACK:
        print("browser PDF fallback enabled")
    if UNPAYWALL_EMAIL:
        print("Unpaywall OA lookup enabled")


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
    parser.add_argument("--browser-fallback", action="store_true", help="Use Playwright browser downloads when raw PDF requests fail.")
    parser.add_argument("--unpaywall-email", help="Email address for optional Unpaywall open-access PDF lookup.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
