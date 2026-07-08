#!/usr/bin/env python3
"""Open a browser for JQAS login and export Playwright storage state.

This helper does not read cookies from an existing browser profile. It opens a
fresh Playwright-controlled browser, lets you complete your institutional login,
then saves the resulting cookies/session state to .auth/storage_state.json.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_URL = "https://www.degruyterbrill.com/journal/key/jqas/html"
DEFAULT_OUTPUT = Path(".auth/storage_state.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed.")
        print("Install it with:")
        print("  python -m pip install playwright")
        print("  python -m playwright install chromium")
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(args.url, wait_until="domcontentloaded")
        print()
        print("Complete your institutional login in the browser window.")
        print("Navigate back to the JQAS page if needed.")
        input("Press Enter here after you can access JQAS PDFs...")
        context.storage_state(path=str(args.output))
        browser.close()

    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
