#!/usr/bin/env python3
"""Render _site/cv/standalone.html to a PDF using headless Chromium (Playwright).

Prefers the local file (_site/cv/standalone.html) so the script works offline as
long as Jekyll has built the site at least once. Falls back to localhost:8080 if
the file is absent.

Output: assets/pdf/cv_kami.pdf
"""

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

_REPO_ROOT = Path(__file__).resolve().parent.parent
_LOCAL_HTML = _REPO_ROOT / "_site" / "cv" / "standalone.html"
_LOCALHOST_URL = "http://localhost:8080/cv/standalone.html"
_OUTPUT = _REPO_ROOT / "assets" / "pdf" / "cv_kami.pdf"


def _pick_source() -> str:
    if _LOCAL_HTML.exists():
        return _LOCAL_HTML.as_uri()
    return _LOCALHOST_URL


def main() -> int:
    source = _pick_source()
    print(f"Source: {source}")

    _OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(source, wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(_OUTPUT),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True,
        )
        browser.close()

    print(f"Generated: {_OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
