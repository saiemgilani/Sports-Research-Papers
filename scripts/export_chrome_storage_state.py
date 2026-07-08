#!/usr/bin/env python3
"""Export storage state from a real Chrome/Edge session via CDP.

This is intended for sites that reject Playwright's bundled browser during bot
verification. It launches an installed Chrome or Edge binary with a temporary
profile and remote debugging enabled, lets the user clear the challenge in that
real browser, then writes Playwright-compatible storage state.
"""

from __future__ import annotations

import argparse
import json
import socket
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_URL = "https://journals.sagepub.com/toc/sana/2/1"
DEFAULT_OUTPUT = Path(".auth/jsa_storage_state.json")
DEFAULT_PROFILE = Path(".auth/jsa_chrome_profile")
DEFAULT_READY_TEXT = "Journal of Sports Analytics"
DEFAULT_TEST_PDF = "https://journals.sagepub.com/doi/pdf/10.3233/JSA-150007"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--browser-executable", type=Path)
    parser.add_argument("--ready-text", default=DEFAULT_READY_TEXT)
    parser.add_argument("--test-pdf-url", default=DEFAULT_TEST_PDF)
    parser.add_argument("--wait-seconds", type=int, default=300)
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--keep-open", action="store_true")
    parser.add_argument(
        "--manual-bootstrap",
        action="store_true",
        help="First open Chrome without CDP; close it after clearing verification, then export from the same profile.",
    )
    parser.add_argument(
        "--bootstrap-only",
        action="store_true",
        help="Open normal Chrome with the profile and exit immediately; rerun without this flag to export.",
    )
    return parser.parse_args()


def find_browser() -> Path:
    candidates = [
        Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
        Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
        Path("C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
        Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Could not find Chrome or Edge. Pass --browser-executable.")


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def wait_for_cdp(port: int, timeout: int = 30) -> None:
    deadline = time.monotonic() + timeout
    url = f"http://127.0.0.1:{port}/json/version"
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                json.loads(response.read().decode("utf-8"))
                return
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            time.sleep(0.5)
    raise TimeoutError(f"Timed out waiting for Chrome DevTools on port {port}")


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
    browser_executable = args.browser_executable or find_browser()
    port = free_port()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.profile_dir.mkdir(parents=True, exist_ok=True)

    if args.manual_bootstrap or args.bootstrap_only:
        bootstrap_command = [
            str(browser_executable),
            f"--user-data-dir={args.profile_dir.resolve()}",
            "--no-first-run",
            "--no-default-browser-check",
            args.url,
        ]
        print(f"Launched normal browser: {browser_executable}")
        print(f"Opened {args.url}")
        print("Complete Cloudflare verification in that browser.")
        if args.bootstrap_only:
            print("After verification, close the browser and rerun this script without --bootstrap-only.")
            subprocess.Popen(bootstrap_command)
            return 0
        print("Close the browser window after verification so this script can export the profile.")
        bootstrap = subprocess.Popen(bootstrap_command)
        try:
            bootstrap.wait(timeout=args.wait_seconds)
        except subprocess.TimeoutExpired:
            print("Timed out waiting for the normal browser to close.")
            print("Close the browser and rerun this command, or increase --wait-seconds.")
            return 4

    command = [
        str(browser_executable),
        f"--remote-debugging-port={port}",
        f"--user-data-dir={args.profile_dir.resolve()}",
        "--no-first-run",
        "--no-default-browser-check",
        args.url,
    ]
    process = subprocess.Popen(command)
    print(f"Launched {browser_executable}")
    print(f"Opened {args.url}")
    print("Complete any Cloudflare verification in the browser window.")

    try:
        wait_for_cdp(port)
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
            context = browser.contexts[0]
            page = context.pages[0] if context.pages else context.new_page()

            deadline = time.monotonic() + args.wait_seconds
            ready = False
            while time.monotonic() < deadline:
                try:
                    if page_ready(page, args.ready_text):
                        ready = True
                        break
                except Exception as exc:
                    print(f"Still waiting: {exc}")
                time.sleep(args.poll_seconds)

            if not ready:
                print("Timed out before the page looked usable. Storage state was not written.")
                browser.close()
                return 2

            context.storage_state(path=str(args.output))
            print(f"Wrote {args.output}")

            if args.test_pdf_url and not pdf_test_passed(context, args.test_pdf_url):
                browser.close()
                return 3

            browser.close()
    finally:
        if not args.keep_open and process.poll() is None:
            process.terminate()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
