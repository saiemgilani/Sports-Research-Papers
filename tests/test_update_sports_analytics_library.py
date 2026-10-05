from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_sports_analytics_library as library  # noqa: E402


WSAJ = "https://wsb.wharton.upenn.edu"
WSAJ_SOURCE = {
    "include_href_patterns": [f"{WSAJ}/"],
    "item_scope_pattern": '<h2 class="entry-title[^"]*">.*?</h2>',
    "issue_from_feed_url_pattern": "(?:spring|fall)-\\d{4}",
}

# Trimmed from the live WSAJ pages, 2026-10-04.
ALL_EDITIONS_PAGE = f"""
<a href="{WSAJ}/wharton-sports-analytics-journal/submission-guidelines/">Submit</a>
<a href="{WSAJ}/wharton-sports-analytics-journal/spring-2026/">10 articles &rarr;</a>
<a href="{WSAJ}/wharton-sports-analytics-journal/fall-2025/">16 articles &rarr;</a>
<a href="{WSAJ}/wharton-sports-analytics-journal/spring-2026/">Spring 2026</a>
<a href="{WSAJ}/wharton-sports-analytics-journal/all-editions/">All Editions</a>
"""

EDITION_PAGE = f"""
<a href="{WSAJ}/wharton-sports-analytics-journal/">Wharton Sports Analytics Journal</a>
<div class="content-blog listCatBlog"><article class="post"><header class="entry-header"><h2 class="entry-title"><a href="{WSAJ}/a-unified-server-quality-metric-for-tennis/">A Unified Server Quality Metric for Tennis</a></h2></header><div class="post-entry"><div class="entry-content"><p><span class="post_excerpt">A Unified Server Quality Metric for Tennis, authored by Aiwen Li, University of Pennsylvania. </span><a class="read-more" href=" {WSAJ}/a-unified-server-quality-metric-for-tennis/ ">Read&nbsp;More</a></p></div></div></article>
"""

ARTICLE_PAGE = """
<meta property="article:published_time" content="2026-05-01T21:43:29+00:00" />
<div class="wpb_wrapper"> <p><span style="color: #999999;"><strong>AUTHORS</strong></span></p> <p>Aiwen Li, <em>University of Pennsylvania </em><br /> Amrita Balajee, <em>University of Pennsylvania </em><br /> Harry Wieand, <em>Boston University Academy</em><br /> Jonathan Pipping-Gamon, <em>University of Pennsylvania </em></p> </div> </div> <div class="wpb_text_column wpb_content_element" > <div class="wpb_wrapper"> <p><span style="color: #999999;"><strong>ABSTRACT</strong></span></p>
<a href="https://wsb.wharton.upenn.edu/wp-content/uploads/2026/05/Unified_Server_Metric_for_Tennis.pdf" class="vc_btn">Read Full Paper (PDF)</a>
"""


def block(inner: str) -> str:
    return (
        '<p><span style="color: #999999;"><strong>AUTHORS</strong></span></p> '
        + inner
        + ' <p><span style="color: #999999;"><strong>ABSTRACT</strong></span></p>'
    )


class WsajSourceTests(unittest.TestCase):
    def test_index_discovers_edition_pages_only(self) -> None:
        urls = library.index_feed_urls(
            ALL_EDITIONS_PAGE,
            f"{WSAJ}/wharton-sports-analytics-journal/all-editions/",
            "/wharton-sports-analytics-journal(?:-og)?/(?:spring|fall)-\\d{4}/$",
        )
        self.assertEqual(
            urls,
            [
                f"{WSAJ}/wharton-sports-analytics-journal/spring-2026/",
                f"{WSAJ}/wharton-sports-analytics-journal/fall-2025/",
            ],
        )

    def test_edition_page_yields_article_items_with_issue(self) -> None:
        items = library.parse_html_index(
            EDITION_PAGE.encode(),
            f"{WSAJ}/wharton-sports-analytics-journal-og/spring-2026/",
            WSAJ_SOURCE,
        )
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "A Unified Server Quality Metric for Tennis")
        self.assertEqual(
            items[0].link, f"{WSAJ}/a-unified-server-quality-metric-for-tennis/"
        )
        self.assertEqual(items[0].issue, "Spring 2026")
        self.assertEqual(items[0].published, "2026")

    def test_article_page_gives_pdf_authors_and_affiliations(self) -> None:
        item = library.FeedItem(
            title="A Unified Server Quality Metric for Tennis", link="x"
        )
        enriched = library.enrich_from_page(item, ARTICLE_PAGE, wordpress_article=True)
        self.assertEqual(
            enriched.authors,
            ["Aiwen Li", "Amrita Balajee", "Harry Wieand", "Jonathan Pipping-Gamon"],
        )
        self.assertEqual(enriched.affiliations[2], "Boston University Academy")
        self.assertEqual(enriched.published[:4], "2026")
        self.assertEqual(
            library.find_pdf_candidates(
                ARTICLE_PAGE, f"{WSAJ}/a-unified-server-quality-metric-for-tennis/"
            ),
            [f"{WSAJ}/wp-content/uploads/2026/05/Unified_Server_Metric_for_Tennis.pdf"],
        )
        # Other sources keep their behaviour: no flag, no author-block parsing.
        self.assertIsNone(library.enrich_from_page(item, ARTICLE_PAGE).authors)

    def test_author_block_variants_from_live_pages(self) -> None:
        cases = {
            # Spring 2023: class years, an affiliation line, a faculty advisor.
            "<p>Allen Sha, W’23; Noah Hyman, W’23; Joshua Sewell, W’23; and Aron Ramsey, W’23<br /> "
            "The Wharton School, University of Pennsylvania, Philadelphia, PA, USA</p> "
            "<p>Faculty Advisor: Abraham Wyner, PhD<br /> The Wharton School</p>": (
                ["Allen Sha", "Noah Hyman", "Joshua Sewell", "Aron Ramsey"],
                "The Wharton School, University of Pennsylvania, Philadelphia, PA, USA",
            ),
            # Spring 2026 competition entry: inline label, <br> inside <em>, an advisor.
            "<p><strong>Authors</strong>: Zach Zaslow, Lucas Greenwald, Max Li, <em>The Pingry School, Basking Ridge, NJ<br /> "
            "</em><strong>Advisor</strong>: Mr. Bradford Poprik, <em>The Pingry School, Basking Ridge, NJ</em></p>": (
                ["Zach Zaslow", "Lucas Greenwald", "Max Li"],
                "The Pingry School, Basking Ridge, NJ",
            ),
            # Spring 2023: affiliation written before the <em>.
            "<p>Samantha Kostacos, Germantown Academy, PA, USA <em> (Moneyball Academy Training Camp FLEX)</em></p>": (
                ["Samantha Kostacos"],
                "Germantown Academy, PA, USA (Moneyball Academy Training Camp FLEX)",
            ),
            # Spring 2023: names only.
            "<p>Aaron Lim<br /> Harrison Goetz</p> <p>Advisor: Naomi Korn</p>": (
                ["Aaron Lim", "Harrison Goetz"],
                "",
            ),
        }
        for inner, (names, affiliation) in cases.items():
            authors, affiliations = library.author_block(block(inner))
            self.assertEqual(authors, names)
            self.assertEqual(set(affiliations), {affiliation})

    def test_fetch_percent_encodes_non_ascii_urls(self) -> None:
        # Spring 2024 links ".../SET_-Spatial-Edge-Technique-...-Edge-Setters¶.pdf".
        seen: list[str] = []

        class Response:
            headers = {"Content-Type": "application/pdf"}

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def read(self):
                return b"%PDF-1.7"

            def geturl(self):
                return seen[-1]

        def fake_urlopen(request, timeout):
            seen.append(request.full_url)
            return Response()

        with patch.object(library.urllib.request, "urlopen", fake_urlopen):
            library.fetch(
                f"{WSAJ}/wp-content/uploads/2024/05/Edge-Setters¶.pdf?a=1&b=%20"
            )
        self.assertEqual(
            seen,
            [f"{WSAJ}/wp-content/uploads/2024/05/Edge-Setters%C2%B6.pdf?a=1&b=%20"],
        )


if __name__ == "__main__":
    unittest.main()
