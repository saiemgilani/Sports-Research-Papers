#!/usr/bin/env python3
"""Poll sports analytics opportunity pages and generate normalized feeds."""

from __future__ import annotations

import argparse
import base64
import email.utils
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, time as datetime_time, timezone, tzinfo
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_CONFIG = Path("feeds/opportunity-sources.json")
DEFAULT_STATE = Path("feeds/opportunity-source-state.json")
DEFAULT_JSON_OUTPUT = Path("feeds/sports-analytics-opportunities.json")
DEFAULT_RSS_OUTPUT = Path("feeds/sports-analytics-opportunities.xml")
DEFAULT_MARKDOWN_OUTPUT = Path("feeds/sports-analytics-opportunities.md")
USER_AGENT = (
    "Sports-Research-Papers opportunity monitor "
    "(https://github.com/saiemgilani/Sports-Research-Papers)"
)
BLOCK_MARKERS = (
    "attention required! | cloudflare",
    "sorry, you have been blocked",
    "cf-chl-",
    "captcha",
)
DATE_PATTERN = re.compile(
    r"\b(?:"
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,)?\s+\d{4}"
    r"|\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|"
    r"Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|"
    r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}"
    r"|\d{4}-\d{2}-\d{2}"
    r")\b",
    re.IGNORECASE,
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.ignored_depth:
            self.ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.ignored_depth:
            self.parts.append(data)


@dataclass
class PollResult:
    source_id: str
    status: str
    checked_at: str
    url: str
    final_url: str = ""
    http_status: int | None = None
    content_sha256: str = ""
    changed: bool = False
    missing_markers: list[str] | None = None
    date_mentions: list[str] | None = None
    error: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "status": self.status,
            "checked_at": self.checked_at,
            "url": self.url,
            "final_url": self.final_url,
            "http_status": self.http_status,
            "content_sha256": self.content_sha256,
            "changed": self.changed,
            "missing_markers": self.missing_markers or [],
            "date_mentions": self.date_mentions or [],
            "error": self.error,
        }


def utc_now(value: str = "") -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def clean_page_text(data: bytes) -> str:
    decoded = data.decode("utf-8", errors="replace")
    parser = TextExtractor()
    parser.feed(decoded)
    text = html.unescape(" ".join(parser.parts))
    return re.sub(r"\s+", " ", text).strip()


def extract_date_mentions(text: str, limit: int = 12) -> list[str]:
    mentions: list[str] = []
    seen: set[str] = set()
    for match in DATE_PATTERN.finditer(text):
        start = max(0, match.start() - 70)
        end = min(len(text), match.end() + 70)
        context = re.sub(r"\s+", " ", text[start:end]).strip(" -|,.;")
        key = match.group(0).casefold()
        if key in seen:
            continue
        seen.add(key)
        mentions.append(context)
        if len(mentions) >= limit:
            break
    return mentions


def safe_error(exc: BaseException) -> str:
    message = re.sub(r"\s+", " ", str(exc)).strip()
    return message[:240]


def request_headers(source: dict[str, Any]) -> tuple[dict[str, str], str]:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/json,*/*"}
    if source.get("auth") != "kaggle_optional":
        return headers, ""
    username = os.environ.get("KAGGLE_USERNAME", "").strip()
    key = os.environ.get("KAGGLE_KEY", "").strip()
    if not username or not key:
        return headers, "KAGGLE_USERNAME and KAGGLE_KEY are not configured"
    token = base64.b64encode(f"{username}:{key}".encode()).decode()
    headers["Authorization"] = f"Basic {token}"
    return headers, ""


def fetch_url(
    url: str,
    headers: dict[str, str],
    timeout: float,
    retries: int,
) -> tuple[bytes, str, int]:
    last_error: BaseException | None = None
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), response.geturl(), response.status
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(0.5 * (attempt + 1))
    assert last_error is not None
    raise last_error


def poll_source(
    source: dict[str, Any],
    previous: dict[str, Any],
    now: datetime,
    timeout: float,
    retries: int,
) -> tuple[PollResult, Any | None]:
    url = source.get("poll_url") or source["url"]
    checked_at = iso_utc(now)
    headers, auth_error = request_headers(source)
    if auth_error:
        return (
            PollResult(
                source_id=source["id"],
                status="auth_required",
                checked_at=checked_at,
                url=url,
                error=auth_error,
            ),
            None,
        )

    try:
        data, final_url, http_status = fetch_url(url, headers, timeout, retries)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").casefold()
        blocked = exc.code in {403, 429} or any(
            marker in body for marker in BLOCK_MARKERS
        )
        return (
            PollResult(
                source_id=source["id"],
                status="blocked" if blocked else "error",
                checked_at=checked_at,
                url=url,
                final_url=exc.geturl(),
                http_status=exc.code,
                error=f"HTTP {exc.code}",
            ),
            None,
        )
    except (urllib.error.URLError, TimeoutError) as exc:
        return (
            PollResult(
                source_id=source["id"],
                status="error",
                checked_at=checked_at,
                url=url,
                error=safe_error(exc),
            ),
            None,
        )

    if source.get("parser") == "kaggle_api":
        try:
            payload = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            return (
                PollResult(
                    source_id=source["id"],
                    status="error",
                    checked_at=checked_at,
                    url=url,
                    final_url=final_url,
                    http_status=http_status,
                    error=f"invalid Kaggle JSON: {safe_error(exc)}",
                ),
                None,
            )
        normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(normalized.encode()).hexdigest()
        return (
            PollResult(
                source_id=source["id"],
                status="ok",
                checked_at=checked_at,
                url=url,
                final_url=final_url,
                http_status=http_status,
                content_sha256=digest,
                changed=bool(previous.get("content_sha256"))
                and digest != previous.get("content_sha256"),
            ),
            payload,
        )

    text = clean_page_text(data)
    folded = text.casefold()
    if any(marker in folded for marker in BLOCK_MARKERS):
        status = "blocked"
    elif not text:
        status = "empty"
    else:
        status = "ok"
    missing = [
        marker
        for marker in source.get("required_markers", [])
        if marker.casefold() not in folded
    ]
    digest = hashlib.sha256(text.encode()).hexdigest() if text else ""
    if status == "ok" and missing:
        status = "markers_missing"
    return (
        PollResult(
            source_id=source["id"],
            status=status,
            checked_at=checked_at,
            url=url,
            final_url=final_url,
            http_status=http_status,
            content_sha256=digest,
            changed=bool(previous.get("content_sha256"))
            and digest != previous.get("content_sha256"),
            missing_markers=missing,
            date_mentions=extract_date_mentions(text),
        ),
        None,
    )


def timezone_for(name: str) -> tzinfo:
    if name == "UTC":
        return timezone.utc
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(f"unknown timezone: {name}") from exc


def parse_temporal(
    value: str, timezone_name: str, end_of_day: bool = False
) -> datetime:
    if not value:
        raise ValueError("empty date")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        parsed_date = date.fromisoformat(value)
        parsed = datetime.combine(
            parsed_date,
            datetime_time(23, 59, 59) if end_of_day else datetime_time.min,
        )
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone_for(timezone_name))
    return parsed


def normalized_temporal(
    value: str, timezone_name: str, end_of_day: bool = False
) -> str:
    return parse_temporal(value, timezone_name, end_of_day).isoformat()


def record_status(record: dict[str, Any], now: datetime) -> str:
    override = record.get("status_override", "")
    timezone_name = record.get("timezone", "UTC")
    event_end = record.get("event_end") or record.get("event_start")
    if override == "open" and event_end:
        if (
            parse_temporal(event_end, timezone_name, end_of_day=True).astimezone(
                timezone.utc
            )
            < now
        ):
            return "closed"
    if override:
        return override
    if record.get("deadline"):
        deadline = parse_temporal(
            record["deadline"], timezone_name, end_of_day="T" not in record["deadline"]
        ).astimezone(timezone.utc)
        return "open" if deadline >= now else "closed"
    if record.get("event_start"):
        start = parse_temporal(record["event_start"], timezone_name).astimezone(
            timezone.utc
        )
        end_value = record.get("event_end") or record["event_start"]
        end = parse_temporal(end_value, timezone_name, end_of_day=True).astimezone(
            timezone.utc
        )
        if now < start:
            return "upcoming"
        if now <= end:
            return "ongoing"
        return "completed"
    return "monitor"


def normalize_record(
    source: dict[str, Any], record: dict[str, Any], now: datetime
) -> dict[str, Any]:
    timezone_name = record.get("timezone", "UTC")
    normalized = {
        "id": record["id"],
        "title": record["title"],
        "source_id": source["id"],
        "source_name": source["name"],
        "organization": source.get("organization", ""),
        "source_type": source.get("type", ""),
        "priority": source.get("priority", "monitor"),
        "kind": record["kind"],
        "status": record_status(record, now),
        "url": record.get("url") or source["url"],
        "deadline": "",
        "timezone": timezone_name,
        "event_start": "",
        "event_end": "",
        "eligibility": record.get("eligibility", ""),
        "summary": record.get("summary", ""),
        "tags": list(dict.fromkeys(record.get("tags", []))),
    }
    if record.get("deadline"):
        normalized["deadline"] = normalized_temporal(
            record["deadline"], timezone_name, end_of_day="T" not in record["deadline"]
        )
    if record.get("event_start"):
        normalized["event_start"] = normalized_temporal(
            record["event_start"], timezone_name
        )
    if record.get("event_end"):
        normalized["event_end"] = normalized_temporal(
            record["event_end"], timezone_name, end_of_day=True
        )
    return normalized


def kaggle_records(
    payload: Any,
    source: dict[str, Any],
    now: datetime,
    limit: int,
) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        competitions = payload.get("competitions") or payload.get("items") or []
    elif isinstance(payload, list):
        competitions = payload
    else:
        competitions = []
    records: list[dict[str, Any]] = []
    for competition in competitions[:limit]:
        if not isinstance(competition, dict):
            continue
        ref = str(competition.get("ref") or competition.get("id") or "").strip()
        title = str(competition.get("title") or competition.get("name") or ref).strip()
        if not ref or not title:
            continue
        deadline = str(competition.get("deadline") or "").strip()
        summary_parts = [
            str(competition.get("description") or "").strip(),
            f"Reward: {competition.get('reward')}" if competition.get("reward") else "",
            f"Teams: {competition.get('teamCount')}"
            if competition.get("teamCount")
            else "",
        ]
        record = {
            "id": f"kaggle-{ref}",
            "title": title,
            "kind": "data_competition",
            "url": f"https://www.kaggle.com/competitions/{ref}",
            "timezone": "UTC",
            "summary": " ".join(part for part in summary_parts if part),
            "tags": ["competition", "kaggle", "sports", "machine-learning"],
        }
        if deadline:
            record["deadline"] = deadline
        normalized = normalize_record(source, record, now)
        if normalized["status"] not in {"closed", "completed"}:
            records.append(normalized)
    return records


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != 1:
        raise ValueError("unsupported opportunity config schema")
    source_ids: set[str] = set()
    record_ids: set[str] = set()
    for source in config.get("sources", []):
        source_id = source.get("id", "")
        if not source_id or source_id in source_ids:
            raise ValueError(f"duplicate or missing source id: {source_id!r}")
        source_ids.add(source_id)
        if not str(source.get("url", "")).startswith("https://"):
            raise ValueError(f"source URL must use HTTPS: {source_id}")
        for record in source.get("records", []):
            record_id = record.get("id", "")
            if not record_id or record_id in record_ids:
                raise ValueError(f"duplicate or missing record id: {record_id!r}")
            record_ids.add(record_id)
            normalize_record(source, record, datetime.now(timezone.utc))


def load_previous_state(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {
        item["source_id"]: item
        for item in payload.get("sources", [])
        if item.get("source_id")
    }


STATUS_ORDER = {
    "open": 0,
    "invitation_only": 1,
    "upcoming": 2,
    "ongoing": 3,
    "monitor": 4,
    "closed": 5,
    "completed": 6,
}


def record_sort_key(record: dict[str, Any]) -> tuple[int, str, str]:
    temporal = record.get("deadline") or record.get("event_start") or "9999"
    return (STATUS_ORDER.get(record["status"], 9), temporal, record["title"].casefold())


def content_text(record: dict[str, Any]) -> str:
    parts = [record["summary"], f"Status: {record['status']}"]
    if record.get("deadline"):
        parts.append(f"Deadline: {record['deadline']}")
    if record.get("event_start"):
        event = record["event_start"]
        if record.get("event_end"):
            event += f" through {record['event_end']}"
        parts.append(f"Event: {event}")
    if record.get("eligibility"):
        parts.append(f"Eligibility: {record['eligibility']}")
    return "\n".join(part for part in parts if part)


def render_json_feed(
    feed_config: dict[str, Any],
    records: list[dict[str, Any]],
    poll_results: list[PollResult],
    generated_at: str,
) -> str:
    source_status = {result.source_id: result.status for result in poll_results}
    payload = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": feed_config["title"],
        "home_page_url": feed_config["home_page_url"],
        "feed_url": feed_config["feed_url"],
        "description": feed_config.get("description", ""),
        "_date_modified": generated_at,
        "items": [
            {
                "id": record["id"],
                "url": record["url"],
                "title": record["title"],
                "content_text": content_text(record),
                "date_modified": generated_at,
                "tags": record["tags"],
                "_source_id": record["source_id"],
                "_source_name": record["source_name"],
                "_source_status": source_status.get(record["source_id"], "offline"),
                "_kind": record["kind"],
                "_status": record["status"],
                "_deadline": record["deadline"] or None,
                "_timezone": record["timezone"],
                "_event_start": record["event_start"] or None,
                "_event_end": record["event_end"] or None,
                "_eligibility": record["eligibility"] or None,
                "_priority": record["priority"],
            }
            for record in records
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def render_rss(
    feed_config: dict[str, Any], records: list[dict[str, Any]], generated_at: str
) -> str:
    ET.register_namespace("atom", "http://www.w3.org/2005/Atom")
    ET.register_namespace(
        "sports", "https://github.com/saiemgilani/Sports-Research-Papers/ns"
    )
    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = feed_config["title"]
    ET.SubElement(channel, "link").text = feed_config["home_page_url"]
    ET.SubElement(channel, "description").text = feed_config.get("description", "")
    ET.SubElement(channel, "lastBuildDate").text = email.utils.format_datetime(
        datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    )
    ET.SubElement(
        channel,
        "{http://www.w3.org/2005/Atom}link",
        {
            "href": feed_config["feed_url"].replace(".json", ".xml"),
            "rel": "self",
            "type": "application/rss+xml",
        },
    )
    for record in records:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = record["title"]
        ET.SubElement(item, "link").text = record["url"]
        ET.SubElement(item, "guid", {"isPermaLink": "false"}).text = record["id"]
        ET.SubElement(item, "description").text = content_text(record)
        ET.SubElement(item, "pubDate").text = email.utils.format_datetime(
            datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
        )
        for tag in record["tags"]:
            ET.SubElement(item, "category").text = tag
        namespace = "https://github.com/saiemgilani/Sports-Research-Papers/ns"
        ET.SubElement(item, f"{{{namespace}}}status").text = record["status"]
        ET.SubElement(item, f"{{{namespace}}}kind").text = record["kind"]
        if record["deadline"]:
            ET.SubElement(item, f"{{{namespace}}}deadline").text = record["deadline"]
    ET.indent(rss, space="  ")
    return ET.tostring(rss, encoding="unicode", xml_declaration=True) + "\n"


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_markdown(
    records: list[dict[str, Any]], poll_results: list[PollResult], generated_at: str
) -> str:
    lines = [
        "# Sports Analytics Opportunities",
        "",
        f"Generated: {generated_at}",
        "",
        "Deadlines are normalized to the timezone shown. Always confirm details on the official page before submitting.",
        "",
        "| Status | Opportunity | Kind | Deadline / event | Timezone | Source |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        temporal = record["deadline"] or record["event_start"] or "TBA"
        lines.append(
            "| {status} | [{title}]({url}) | {kind} | {temporal} | {timezone} | {source} |".format(
                status=record["status"],
                title=markdown_escape(record["title"]),
                url=record["url"],
                kind=record["kind"],
                temporal=temporal,
                timezone=record["timezone"],
                source=markdown_escape(record["source_name"]),
            )
        )
    lines.extend(
        [
            "",
            "## Source Health",
            "",
            "| Source | Fetch status | Changed | Missing markers |",
            "| --- | --- | --- | --- |",
        ]
    )
    for result in sorted(poll_results, key=lambda item: item.source_id):
        missing = ", ".join(result.missing_markers or []) or "-"
        lines.append(
            f"| {result.source_id} | {result.status} | {str(result.changed).lower()} | {markdown_escape(missing)} |"
        )
    return "\n".join(lines) + "\n"


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = path.read_text(encoding="utf-8") if path.exists() else None
    if previous == value:
        print(f"unchanged: {path}")
        return
    path.write_text(value, encoding="utf-8", newline="\n")
    print(f"updated: {path}")


def semantic_state(payload: dict[str, Any]) -> dict[str, Any]:
    stable = json.loads(json.dumps(payload))
    stable.pop("generated_at", None)
    for source in stable.get("sources", []):
        source.pop("checked_at", None)
        source.pop("changed", None)
    return stable


def semantic_feed(payload: dict[str, Any]) -> dict[str, Any]:
    stable = json.loads(json.dumps(payload))
    stable.pop("date_modified", None)
    stable.pop("_date_modified", None)
    for item in stable.get("items", []):
        item.pop("date_modified", None)
    return stable


def outputs_semantically_unchanged(
    state_path: Path,
    json_output_path: Path,
    state_payload: dict[str, Any],
    json_feed_payload: dict[str, Any],
) -> bool:
    if not state_path.exists() or not json_output_path.exists():
        return False
    try:
        previous_state = json.loads(state_path.read_text(encoding="utf-8"))
        previous_feed = json.loads(json_output_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return semantic_state(previous_state) == semantic_state(
        state_payload
    ) and semantic_feed(previous_feed) == semantic_feed(json_feed_payload)


def run(args: argparse.Namespace) -> int:
    config = json.loads(args.config.read_text(encoding="utf-8"))
    validate_config(config)
    now = utc_now(args.now)
    generated_at = iso_utc(now)
    previous = load_previous_state(args.state)
    selected = set(args.source or [])
    sources = [
        source
        for source in config["sources"]
        if not selected or source["id"] in selected
    ]
    if selected - {source["id"] for source in sources}:
        missing = ", ".join(sorted(selected - {source["id"] for source in sources}))
        raise ValueError(f"unknown source ids: {missing}")

    records: list[dict[str, Any]] = []
    poll_results: list[PollResult] = []
    for source in sources:
        for record in source.get("records", []):
            records.append(normalize_record(source, record, now))
        if args.offline:
            result = PollResult(
                source_id=source["id"],
                status="offline",
                checked_at=generated_at,
                url=source.get("poll_url") or source["url"],
            )
            dynamic_payload = None
        else:
            result, dynamic_payload = poll_source(
                source,
                previous.get(source["id"], {}),
                now,
                args.timeout,
                args.retries,
            )
        poll_results.append(result)
        print(f"source={source['id']} status={result.status} changed={result.changed}")
        if dynamic_payload is not None and source.get("parser") == "kaggle_api":
            records.extend(
                kaggle_records(dynamic_payload, source, now, args.max_dynamic_items)
            )

    records.sort(key=record_sort_key)
    state_payload = {
        "schema_version": 1,
        "generated_at": generated_at,
        "sources": [result.as_dict() for result in poll_results],
    }
    json_feed_text = render_json_feed(
        config["feed"], records, poll_results, generated_at
    )
    json_feed_payload = json.loads(json_feed_text)
    successes = sum(
        result.status in {"ok", "markers_missing"} for result in poll_results
    )
    print(
        f"source_count={len(poll_results)} success_count={successes} record_count={len(records)}"
    )
    if args.require_success and successes < args.require_success:
        print(
            f"error: only {successes} sources succeeded; required {args.require_success}",
            file=sys.stderr,
        )
        return 1
    if args.only_write_on_change and outputs_semantically_unchanged(
        args.state,
        args.json_output,
        state_payload,
        json_feed_payload,
    ):
        print("no semantic opportunity changes; generated files left untouched")
        return 0

    write_text(
        args.state, json.dumps(state_payload, indent=2, ensure_ascii=False) + "\n"
    )
    write_text(args.json_output, json_feed_text)
    write_text(args.rss_output, render_rss(config["feed"], records, generated_at))
    write_text(
        args.markdown_output, render_markdown(records, poll_results, generated_at)
    )
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON_OUTPUT)
    parser.add_argument("--rss-output", type=Path, default=DEFAULT_RSS_OUTPUT)
    parser.add_argument("--markdown-output", type=Path, default=DEFAULT_MARKDOWN_OUTPUT)
    parser.add_argument(
        "--source", action="append", help="Only poll this source id. May be repeated."
    )
    parser.add_argument(
        "--offline", action="store_true", help="Generate feeds without network polling."
    )
    parser.add_argument(
        "--now", default="", help="Override current time with an ISO-8601 timestamp."
    )
    parser.add_argument("--timeout", type=float, default=25.0)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--max-dynamic-items", type=int, default=50)
    parser.add_argument("--require-success", type=int, default=0)
    parser.add_argument(
        "--only-write-on-change",
        action="store_true",
        help="Keep generated files untouched when only polling timestamps changed.",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
