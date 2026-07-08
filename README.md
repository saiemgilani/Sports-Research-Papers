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

### Authorized JQAS Access

JQAS/De Gruyter automation is configured to run only when you provide an
authorized browser session cookie at runtime. Do not commit cookies or licensed
files to a public repository unless your license permits redistribution.

Supported cookie inputs:

```bash
# Direct Cookie header
JQAS_COOKIE="cookie_name=value; other_cookie=value" \
python scripts/update_sports_analytics_library.py --source jqas-degruyter --dry-run

# Netscape cookies.txt export
python scripts/update_sports_analytics_library.py \
  --source jqas-degruyter \
  --cookie-file .auth/cookies.txt \
  --dry-run

# Playwright storage_state.json
python scripts/update_sports_analytics_library.py \
  --source jqas-degruyter \
  --storage-state .auth/storage_state.json \
  --dry-run
```

To create `.auth/storage_state.json` interactively:

```bash
python -m pip install playwright
python -m playwright install chromium
python scripts/export_jqas_storage_state.py
python scripts/update_sports_analytics_library.py \
  --source jqas-degruyter \
  --storage-state .auth/storage_state.json \
  --dry-run
```

For GitHub Actions, add a private repository secret named `JQAS_COOKIE`. A
self-hosted runner on the institutional network is usually more reliable than a
GitHub-hosted runner for publisher entitlement checks.
