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

### Conference Papers

Conference PDF sources are categorized under `library/conferences/`. The first
downloadable public archives are CMSAC, NESSIS, and a verified SSAC seed list:

```bash
python scripts/update_sports_analytics_library.py \
  --source cmsac-conference-papers \
  --source nessis-presentations-posters \
  --source mit-ssac-research-papers-seed \
  --dry-run
```

MIT Sloan SSAC's public website currently returns `403` to raw automation, so
`mit-ssac-research-papers-seed` stores verified official SSAC item pages and
their public Webflow CDN PDF URLs. The seed currently covers 41 public research
paper PDFs and should be expanded as more SSAC paper pages are verified.

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
python scripts/export_publisher_storage_state.py --publisher jqas
python scripts/update_sports_analytics_library.py \
  --source jqas-degruyter \
  --storage-state .auth/storage_state.json \
  --dry-run
```

For GitHub Actions, add a private repository secret named `JQAS_COOKIE`. A
self-hosted runner on the institutional network is usually more reliable than a
GitHub-hosted runner for publisher entitlement checks.

### Journal of Sports Analytics Backfill

The `jsa-crossref-2016` source enumerates Journal of Sports Analytics articles
from Volume 2 / 2016 onward using Crossref metadata, then tries the public SAGE
DOI PDF URL and legacy IOS Press download URLs.

SAGE and IOS Press may show Cloudflare verification to automated clients. To
create a browser storage state after clearing that challenge, prefer the real
Chrome/Edge bootstrap:

```bash
python -m pip install playwright
python scripts/export_chrome_storage_state.py --manual-bootstrap
python scripts/update_sports_analytics_library.py \
  --source jsa-crossref-2016 \
  --storage-state .auth/jsa_storage_state.json \
  --unpaywall-email you@example.edu \
  --browser-fallback \
  --dry-run
```

The bootstrap opens Chrome/Edge normally first. Complete the Cloudflare
verification, close the browser, then the script reopens that profile through
CDP only long enough to export cookies.

If the browser needs to stay open longer than the command timeout, use the
split form:

```bash
python scripts/export_chrome_storage_state.py --bootstrap-only
# complete verification, then close that Chrome/Edge window
python scripts/export_chrome_storage_state.py
```

If the site accepts Playwright's bundled browser, this simpler path also works:

```bash
python -m pip install playwright
python -m playwright install chromium
python scripts/export_publisher_storage_state.py --publisher jsa
python scripts/update_sports_analytics_library.py \
  --source jsa-crossref-2016 \
  --storage-state .auth/jsa_storage_state.json \
  --unpaywall-email you@example.edu \
  --browser-fallback \
  --dry-run
```

For scheduled runs, prefer a private self-hosted runner that can refresh
`JSA_COOKIE` or `JSA_STORAGE_STATE` without committing those secrets.

Do not use Sci-Hub, LibGen, Annas Archive, proxy bypasses, or similar download
routes in this repository. The downloader is limited to public/open PDFs,
Crossref and Unpaywall open-access locations, and browser sessions you are
authorized to use.
