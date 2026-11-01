# Sports analytics weekly roundup — 2026-10-20

Window: 2026-10-13 to 2026-10-20 (180-day context where noted). Method: arXiv API queries (sports analytics, play-by-play, tracking, win probability, xG/xP, NBA/NFL/MLB/NHL, college, soccer tracking, LLMs), PyPI JSON, CRAN pages, Arrow blog, Polars releases page. General web search returned little dated content for the week, so coverage is best-effort and skews to sources with APIs.

## 1. Sports Analytics Literature & Research

Only two sports-relevant arXiv items were posted in the past 7 days; six more from the prior four weeks were added for context. All are saved in `library/preprints/arXiv/` and scored in `paper-ranking-scores.csv` / `paper-ranking-report.md`.

**New this week**
- [MoveBench: rubric-based benchmark for LLMs in sports and health coaching](https://arxiv.org/abs/2610.26185) (Oct 19) — 16/30. Code public.
- [Throwing4: phase-aware pose modeling for throw-distance prediction in elite athletics](https://arxiv.org/abs/2610.16383) (Oct 12) — not downloaded (biomechanics, outside scope).

**Prior four weeks (highest value first)**
- [Who Blocks Whom? Probabilistic pass-blocking assignments](https://arxiv.org/abs/2609.33664) (Sep 27, v2) — 23/30. NFL, Big Data Bowl 2021.
- [Concave processes for multi-task NBA career trajectories](https://arxiv.org/abs/2609.33752) (Sep 27, v2) — 21/30.
- [Credit attribution in soccer networks with multivariate Hawkes processes](https://arxiv.org/abs/2610.12775) (Oct 8) — 21/30. StatsBomb open data.
- [SambaGraph action-reaction soccer graphs](https://arxiv.org/abs/2609.25569) (Sep 22) — 19/30.
- [From metrics to decisions in NBA analytics (review)](https://arxiv.org/abs/2609.27245) (Sep 23) — 19/30.
- [Strategic multi-agent action valuation in football](https://arxiv.org/abs/2610.05961) (Oct 5) — 18/30.
- [Markov chain approach to modeling rugby union](https://arxiv.org/abs/2610.04813) (Oct 3) — 17/30.

Not covered: journal TOCs (JQAS 22(2), JSA) and the MLSA 2026 proceedings are paywalled or subscription previews; the repo's scheduled library workflow handles open PDFs from those. Industry blogs returned nothing dated this week.

## 2. Open-Source Packages & Ecosystem Updates

No confirmed new releases this week for the tracked R packages; GitHub release pages for repos outside this session's scope could not be read.

| Package | Latest found | Date | Source |
|---|---|---|---|
| sportsdataverse (PyPI) | 0.1.4 | 2026-09-01 | [PyPI](https://pypi.org/project/sportsdataverse/) |
| sportsdataverse-py docs index | `docs-index` release asset refreshed | 2026-10-06 | repo releases |
| hoopR (CRAN) | 3.1.0 | 2026-08-25 | [CRAN](https://cran.r-project.org/web/packages/hoopR/) |
| baseballr (CRAN) | 2.0.0 | 2026-08-26 | [CRAN](https://cran.r-project.org/web/packages/baseballr/) |
| nflreadr (CRAN) | 1.5.1 | 2026-04-13 | [CRAN](https://cran.r-project.org/web/packages/nflreadr/) |
| cfbfastR (CRAN) | 3.0.0 (CRAN checks 2026-08-24) | — | [CRAN](https://cran.r-project.org/web/packages/cfbfastR/) |
| nflreadpy (PyPI) | 0.1.5 | 2025-11-19 | [PyPI](https://pypi.org/project/nflreadpy/) |

Not checked (no access): wehoop, fastRhockey, nflfastR, other sportsdataverse repos' GitHub activity.

## 3. Data Engineering & Tooling

- **Polars 2.0.0 (Oct 6)** — [release](https://github.com/pola-rs/polars/releases). Out-of-core processing on by default (80% RAM threshold, 64 GB default disk budget), streaming out-of-core sort, large SQL expansion (window frames, GROUPING SETS/ROLLUP/CUBE, APPROX_QUANTILE), `scan_lance`, `scan_external_reader`, `collect` on `RemoteEngine`. Breaking: SQL window/QUALIFY semantics, exact SQL literals as Decimal, Parquet ENUM read as String, `cut`/`qcut` deprecated. sportsdataverse-py already constrains `polars>=1.0,<3` and documents 2.0 compatibility rules, so this is expected to be a no-op there; worth a CI confirmation run on the new release.
- **Apache Arrow 26.0.0 (Oct 8)** — [blog](https://arrow.apache.org/blog/); 337 resolved issues, 403 commits, 108 contributors. pyarrow 26.0.0 on PyPI Oct 9. Highlights were not readable from the page excerpt. sportsdataverse-py reads release parquet through pyarrow, so run its release-parquet tests against 26.
- **Arrow Rust 60.0.0 (Sep 29)** and Arrow Go 18.8.0 (Sep 8) — same blog.
- **dlt 1.31.0 (Oct 7)**, **Dagster 1.13.26 (Oct 9)**, **DuckDB 1.5.6 (Sep 28)**, **Airflow 3.3.2 (Sep 17)** — PyPI; point releases, no notes reviewed.

## Follow-ups worth considering
1. Run sportsdataverse-py CI against Polars 2.0.0 and pyarrow 26.0.0 (not done here).
2. Fold the NBA review's six decision-readiness gates into the Practicality axis of the paper rubric.
3. Reproduction notebooks for Who Blocks Whom (BDB 2021) and the Hawkes assist-credit model (StatsBomb open data).
