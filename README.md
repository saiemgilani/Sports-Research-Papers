# Sports-Research-Papers

A selection of sports analytics research papers.

## Feeds

The curated sports analytics research and opportunity feed lives in:

- [feeds/sports-analytics-feed.md](feeds/sports-analytics-feed.md)
- [feeds/sports-analytics-sources.yml](feeds/sports-analytics-sources.yml)
- [feeds/sports-analytics-feeds.opml](feeds/sports-analytics-feeds.opml)

## Automated Updates

The scheduled workflow in `.github/workflows/update-sports-analytics-library.yml`
downloads public PDFs from configured feeds into `library/`, records metadata in
`library/manifest.jsonl`, and commits new files back to the repository.

Run it locally with:

```bash
python scripts/update_sports_analytics_library.py --dry-run --max-items 3
```
