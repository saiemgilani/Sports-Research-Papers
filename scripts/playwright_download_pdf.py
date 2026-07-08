#!/usr/bin/env python3
"""Download one PDF through a Playwright browser session."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--article-url", default="")
    parser.add_argument("--storage-state", type=Path)
    parser.add_argument("--output-pdf", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    from playwright.sync_api import sync_playwright

    storage_state = str(args.storage_state) if args.storage_state else None
    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state=storage_state, accept_downloads=True)
        page = context.new_page()

        response = context.request.get(args.url, timeout=60000)
        body = response.body() if response.ok else b""
        if body.startswith(b"%PDF"):
            args.output_pdf.write_bytes(body)
            args.output_json.write_text(
                json.dumps(
                    {
                        "url": str(response.url),
                        "suggested_filename": Path(args.url).name or "download.pdf",
                    }
                ),
                encoding="utf-8",
            )
            browser.close()
            return 0

        if args.article_url:
            page.goto(args.article_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(1000)
            download_link = first_download_link(page)
            with page.expect_download(timeout=60000) as download_info:
                download_link.click(timeout=15000)
        else:
            with page.expect_download(timeout=60000) as download_info:
                page.goto(args.url, wait_until="domcontentloaded", timeout=60000)
        download = download_info.value
        downloaded_path = Path(download.path())
        args.output_pdf.write_bytes(downloaded_path.read_bytes())
        args.output_json.write_text(
            json.dumps(
                {
                    "url": download.url,
                    "suggested_filename": download.suggested_filename,
                }
            ),
            encoding="utf-8",
        )
        browser.close()

    return 0


def first_download_link(page):
    selectors = [
        "a[href*='/doi/pdf/']",
        "a[href*='/doi/epdf/']",
        "a[href*='/download/']",
    ]
    for selector in selectors:
        locator = page.locator(selector).first
        if locator.count():
            return locator
    labels = [
        "Download Article",
        "Download PDF",
        "View PDF/EPUB",
        "PDF/EPUB",
        "PDF / EPUB",
        "PDF",
    ]
    for label in labels:
        locator = page.get_by_text(label, exact=False).first
        if locator.count():
            return locator
    raise RuntimeError("No PDF download link found on article page")


if __name__ == "__main__":
    raise SystemExit(main())
