from __future__ import annotations

import json
import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_sports_analytics_opportunities as opportunities  # noqa: E402


NOW = datetime(2026, 7, 12, 16, tzinfo=timezone.utc)


class OpportunityPollerTests(unittest.TestCase):
    def test_record_status_uses_deadline_and_event_dates(self) -> None:
        self.assertEqual(
            opportunities.record_status(
                {
                    "deadline": "2026-10-01T23:59:00-04:00",
                    "timezone": "America/New_York",
                },
                NOW,
            ),
            "open",
        )
        self.assertEqual(
            opportunities.record_status(
                {
                    "deadline": "2026-06-05T23:59:59+02:00",
                    "timezone": "Europe/Rome",
                },
                NOW,
            ),
            "closed",
        )
        self.assertEqual(
            opportunities.record_status(
                {
                    "event_start": "2026-09-07T00:00:00+02:00",
                    "timezone": "Europe/Rome",
                },
                NOW,
            ),
            "upcoming",
        )

    def test_open_override_closes_after_event(self) -> None:
        status = opportunities.record_status(
            {
                "status_override": "open",
                "event_start": "2026-01-01T00:00:00+00:00",
                "timezone": "UTC",
            },
            NOW,
        )
        self.assertEqual(status, "closed")

    def test_date_mentions_include_context(self) -> None:
        text = (
            "Paper submission is due June 5, 2026. "
            "The workshop takes place September 7, 2026 in Naples."
        )
        mentions = opportunities.extract_date_mentions(text)
        self.assertEqual(len(mentions), 2)
        self.assertIn("Paper submission", mentions[0])
        self.assertIn("workshop", mentions[1])

    def test_poll_source_detects_missing_markers_and_changes(self) -> None:
        source = {
            "id": "example",
            "url": "https://example.com/call",
            "required_markers": ["Call for Papers", "August 3, 2026"],
        }
        page = b"<html><body><h1>Call for Papers</h1></body></html>"
        previous = {"content_sha256": "old"}
        with patch.object(
            opportunities,
            "fetch_url",
            return_value=(page, source["url"], 200),
        ):
            result, payload = opportunities.poll_source(
                source, previous, NOW, timeout=1, retries=0
            )
        self.assertIsNone(payload)
        self.assertEqual(result.status, "markers_missing")
        self.assertEqual(result.missing_markers, ["August 3, 2026"])
        self.assertTrue(result.changed)

    def test_kaggle_payload_normalizes_dynamic_competition(self) -> None:
        source = {
            "id": "kaggle-sports",
            "name": "Kaggle Sports Competitions",
            "organization": "Kaggle",
            "type": "competition_index",
            "priority": "core",
            "url": "https://www.kaggle.com/competitions",
        }
        payload = [
            {
                "ref": "sample-sports-challenge",
                "title": "Sample Sports Challenge",
                "deadline": "2026-08-01T00:00:00Z",
                "reward": "$10,000",
                "teamCount": 42,
            }
        ]
        records = opportunities.kaggle_records(payload, source, NOW, limit=10)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["id"], "kaggle-sample-sports-challenge")
        self.assertEqual(records[0]["status"], "open")
        self.assertIn("Teams: 42", records[0]["summary"])

        payload.append(
            {
                "ref": "closed-sports-challenge",
                "title": "Closed Sports Challenge",
                "deadline": "2026-01-01T00:00:00Z",
            }
        )
        records = opportunities.kaggle_records(payload, source, NOW, limit=10)
        self.assertEqual(
            [record["id"] for record in records], ["kaggle-sample-sports-challenge"]
        )

    def test_generated_json_and_rss_are_parseable(self) -> None:
        source = {
            "id": "example",
            "name": "Example",
            "organization": "Example Org",
            "type": "conference",
            "priority": "core",
            "url": "https://example.com",
        }
        record = opportunities.normalize_record(
            source,
            {
                "id": "example-deadline",
                "title": "Example deadline",
                "kind": "abstract_submission",
                "deadline": "2026-08-01T23:59:59+00:00",
                "timezone": "UTC",
                "tags": ["abstract"],
            },
            NOW,
        )
        result = opportunities.PollResult(
            source_id="example",
            status="ok",
            checked_at=opportunities.iso_utc(NOW),
            url=source["url"],
        )
        feed = {
            "title": "Example Feed",
            "home_page_url": "https://example.com",
            "feed_url": "https://example.com/feed.json",
        }
        generated_at = opportunities.iso_utc(NOW)
        json_payload = json.loads(
            opportunities.render_json_feed(feed, [record], [result], generated_at)
        )
        self.assertEqual(json_payload["items"][0]["_source_status"], "ok")
        ET.fromstring(opportunities.render_rss(feed, [record], generated_at))

    def test_semantic_comparison_ignores_polling_timestamps(self) -> None:
        first_state = {
            "schema_version": 1,
            "generated_at": "2026-07-12T16:00:00Z",
            "sources": [
                {
                    "source_id": "example",
                    "status": "ok",
                    "checked_at": "2026-07-12T16:00:00Z",
                    "changed": False,
                    "content_sha256": "same",
                }
            ],
        }
        second_state = json.loads(json.dumps(first_state))
        second_state["generated_at"] = "2026-07-13T16:00:00Z"
        second_state["sources"][0]["checked_at"] = "2026-07-13T16:00:00Z"
        self.assertEqual(
            opportunities.semantic_state(first_state),
            opportunities.semantic_state(second_state),
        )

        first_feed = {
            "_date_modified": "2026-07-12T16:00:00Z",
            "items": [{"id": "example", "date_modified": "2026-07-12T16:00:00Z"}],
        }
        second_feed = {
            "_date_modified": "2026-07-13T16:00:00Z",
            "items": [{"id": "example", "date_modified": "2026-07-13T16:00:00Z"}],
        }
        self.assertEqual(
            opportunities.semantic_feed(first_feed),
            opportunities.semantic_feed(second_feed),
        )


if __name__ == "__main__":
    unittest.main()
