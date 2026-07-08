#!/usr/bin/env python3
"""Open a publisher page and export Playwright storage state.

Use this for publisher sites that require an interactive browser step, such as
institutional login or Cloudflare verification. The script does not read an
existing browser profile; it opens a fresh Playwright-controlled browser and
saves only the session state created in that browser.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path


PRESETS = {
    "jqas": {
        "url": "https://www.degruyterbrill.com/journal/key/jqas/html",
        "output": Path(".auth/storage_state.json"),
        "ready_text": "Journal of Quantitative Analysis in Sports",
        "test_pdf": "",
    },
    "jsa": {
        "url": "https://journals.sagepub.com/toc/sana/2/1",
        "output": Path(".auth/jsa_storage_state.json"),
        "ready_text": "Journal of Sports Analytics",
        "test_pdf": "https://journals.sagepub.com/doi/pdf/10.3233/JSA-150007",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publisher", choices=sorted(PRESETS), default="jsa")
    parser.add_argument("--url", help="Page to open before exporting cookies.")
    parser.add_argument("--output", type=Path, help="Storage-state JSON to write.")
    parser.add_argument("--ready-text", help="Text that indicates the target page is loaded.")
    parser.add_argument("--test-pdf-url", help="Optional PDF URL to test with browser cookies.")
    parser.add_argument("--wait-seconds", type=int, default=300)
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    return parser.parse_args()


def cloudflare_challenge_text(text: str) -> bool:
    lowered = text.lower()
    return (
        "performing security verification" in lowered
        or "just a moment" in lowered
        or "cloudflare" in lowered
        or "verify you are human" in lowered
    )


def page_ready(page, ready_text: str) -> bool:
    title = page.title()
    text = page.locator("body").inner_text(timeout=5000)
    if cloudflare_challenge_text(title) or cloudflare_challenge_text(text):
        return False
    return not ready_text or ready_text.lower() in text.lower() or ready_text.lower() in title.lower()


def pdf_test_passed(context, url: str) -> bool:
    if not url:
        return True
    response = context.request.get(url, timeout=60000)
    if not response.ok:
        print(f"PDF test returned HTTP {response.status}: {url}")
        return False
    body = response.body()
    if not body.startswith(b"%PDF"):
        print(f"PDF test did not return PDF bytes: {url}")
        return False
    print(f"PDF test passed: {url} ({len(body)} bytes)")
    return True


def main() -> int:
    args = parse_args()
    preset = PRESETS[args.publisher]
    url = args.url or preset["url"]
    output = args.output or preset["output"]
    ready_text = args.ready_text if args.ready_text is not None else preset["ready_text"]
    test_pdf_url = args.test_pdf_url if args.test_pdf_url is not None else preset["test_pdf"]

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed.")
        print("Install it with:")
        print("  python -m pip install playwright")
        print("  python -m playwright install chromium")
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        deadline = time.monotonic() + args.wait_seconds
        print()
        print(f"Opened {url}")
        print("Complete any browser verification or institutional login in the visible window.")
        print(f"Waiting up to {args.wait_seconds} seconds for the page to become usable...")

        ready = False
        while time.monotonic() < deadline:
            try:
                if page_ready(page, ready_text):
                    ready = True
                    break
            except Exception as exc:
                print(f"Still waiting: {exc}")
            time.sleep(args.poll_seconds)

        if not ready:
            print("Timed out before the page looked usable. Storage state was not written.")
            browser.close()
            return 2

        context.storage_state(path=str(output))
        print(f"Wrote {output}")

        if test_pdf_url and not pdf_test_passed(context, test_pdf_url):
            browser.close()
            return 3

        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
