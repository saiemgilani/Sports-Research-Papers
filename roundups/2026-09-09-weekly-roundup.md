# Sports Analytics Weekly Roundup — 2026-09-09

Coverage window: 2026-09-02 to 2026-09-09 (headline items), with additional context back to roughly 180 days where the last-week yield was thin. Compiled from web research across academic sources, arXiv, industry blogs, GitHub release activity, and data-engineering tooling news.

## 1. Sports Analytics Literature & Research

**Past 7 days** — three new arXiv preprints, all archived in full to this repo (see [Archived this week](#archived-this-week) below). No dated journal, conference, or industry-blog research posts were found in-window; JQAS's site blocks automated fetches, CMSAC 2026 (Oct 23–24) hasn't published papers yet, and the most recent StatsBomb/Hudl and Squared Statistics research posts predate this window.

- **[Unified Pitch Graphs for Diagnosing Pitching Strategy](https://arxiv.org/abs/2609.03810)** — Lee & Ko, arXiv:2609.03810 (Sept 3). A hierarchical graph representation that keeps every MLB pitch as an exact event with a reconstructed 3D trajectory instead of collapsing pitches to type/location bins. Tested on 3.94M Statcast pitches (2021–2026); a support-adaptive backoff mechanism lifts held-out path coverage from 18.9% to 94.9%. **Baseball · pitch sequencing · graph representation learning.**
- **[The profit-bias identity in sports betting](https://arxiv.org/abs/2609.06739)** — Dmochowski, arXiv:2609.06739 (Sept 6). Derives a closed-form identity generalizing Levitt (2004): bookmaker profit = hold + (price-shading × public lean) + bet-share/outcome covariance. On 1,139 MLB games, the pooled bias effect vanishes but reappears strongly game-by-game — a Simpson's-paradox result. **Betting markets · market efficiency.**
- **[A Statistical and ML Framework for Quantifying Offensive Impact in Professional Box Lacrosse](https://arxiv.org/abs/2609.06610)** — Jimerson Jr., arXiv:2609.06610 (Sept 6). First xG-style shot-quality and expected-assist/pick-value framework for box lacrosse; preliminary single-team case study (1,006 shots, 13 Rochester Knighthawks games). **Box lacrosse · expected goals · niche-sport analytics.**

**Additional recent context (8–180 days)**

- **[Beyond Expected Goals: A Probabilistic Framework for Shot Occurrences in Soccer (xG+)](https://arxiv.org/abs/2512.00203)** — Pipping-Gamón, Feng & Sabin, arXiv:2512.00203 (Jan 2026). Jointly models shot occurrence and shot quality at the possession level, fixing standard xG's selection bias (it only conditions on shots that happened). The most-discussed soccer-methods preprint of the last several months — archived this week as high-value context.
- **[The Historical RAPM Project](https://squared2020.com/2026/04/29/the-historical-rapm-project/)** — Squared Statistics (Apr 2026). Hand-reconstructed possession-level RAPM data back to the pre-play-by-play NBA era (1969–96); a major open-data effort still being expanded and cited.
- Other notable items from the last few months: a deep-learning live NBA win-probability model (Springer, Mar 2026), a state-dependent WNBA win-probability framework (Apr 2026), multimodal tennis injury-risk prediction (arXiv:2608.25126, Aug 2026), transformer-based pitch-sequence optimization for K/9 gains (arXiv:2606.17345, Jun 2026), two cricket win-probability/strategy papers (arXiv:2608.14696 and 2604.13861), and an NBA officiating-impact study using ESPN win-probability data (arXiv:2605.17845, May 2026).

### Archived this week

All four papers above are now stored as full open-access PDFs under `library/preprints/arXiv/2026/`, with `pypdf`-extracted markdown mirrors under `md/library/preprints/arXiv/2026/`, manifest entries in `library/manifest.jsonl`, and Novelty/Practicality/Reproducibility scores added to `paper-ranking-scores.csv`. Narrative analysis for each is in the new **"The weekly-roundup arXiv batch (added 2026-09-09)"** section of `paper-ranking-report.md`. Composite scores: profit-bias identity 22/30, xG+ 20/30, Unified Pitch Graphs 19/30, box lacrosse framework 15/30.

## 2. Open-Source Packages & Ecosystem Updates

**Past 7 days**

- **cfbfastR (R)** — very active dev-branch work following its Aug 24 CRAN 3.0.0 release: play-by-play catch-location parsing fixed (Sept 1), Expected Points model docs completed (Sept 3), XP/two-point scoring-era cutoffs fixed (Sept 7), and passing/rushing endpoints added, bringing CFBD API coverage to 84/84 endpoints (Sept 9). No new CRAN version yet.
- **nflverse-data** — routine weekly data drops continued as the 2026 NFL season opened: `nfldata` (Sept 9), `nflverse-rosters` (Sept 8), `nflverse-players` (Sept 5), `nflverse-data-archives` (Sept 3), `nflverse-pbp` (Sept 2).
- **nflreadr (R) / nflreadpy (Python)** — matching unreleased fixes on Sept 1/7/8: FTN charting-dictionary improvements, `clean_team_abbrs()` now maps "AZ"→"ARI", and `load_injuries()` no longer rejects the practice week before the season opener for an upcoming season. No new package version cut yet on either side.
- **sportsdataverse-py** — most recent tag (v0.1.4, Sept 1) falls just outside the 7-day window but is the newest release as of today.
- **worldfootballR (R)** — no activity; flagged as a standing gap since the repo was archived by its owner on 2025-09-18 and remains read-only.
- hoopR, wehoop, baseballr, and fastRhockey had no commits this week — quiet since their late-August CRAN pushes (below).

**Additional recent context (8–30 days)**

- **Coordinated CRAN release wave, Aug 24–26** across the sportsdataverse R family, timed just ahead of the CFB/NFL season openers: **cfbfastR 3.0.0**, **hoopR 3.1.0**, **wehoop 3.0.0**, **baseballr 2.0.0**, and **fastRhockey 1.0.0** — each adding dozens of new ESPN/Fox Sports/vendor endpoint wrappers and, for baseballr, a major Statcast column-handling refactor.
- **sportsdataverse-py** shipped six patch releases in six days (0.1.0 → 0.1.4, Aug 27–Sept 1): new ESPN roster datasets, refactored CFB loaders, and fixes for formation tags misparsed as player names.
- **statsbombpy** remains at v1.22.0 (Jul 30), the current stable.
- No activity found for nflfastR, nflplotR, nflseedR, kloppy, socceraction, gtExtras, gamezoneR, or espnscrapeR in this window. hockeyR remains maintained but has known-broken scrapers since the NHL's 2023–24 API migration.

**Headline takeaway**: the dominant story is the coordinated late-August CRAN wave across the R sportsdataverse family ahead of the football season, followed by cfbfastR's continued active bug-fixing through Week 1 of college football, plus matching nflverse "allow upcoming season" fixes landing in parallel on both the R and Python sides.

## 3. Data Engineering & Tooling

**Past 7 days**

- **Polars 2.0rc1** (Sept 2) — first release candidate for the 2.0 major version; `collect()` now defaults to the streaming engine (claimed ~5x speedup and lower memory for typical workloads), with stricter type coercion and breaking changes around casts and horizontal concat. Worth testing against existing pipelines before GA.
- **DuckDB v2.0-alpha** (Sept 2) — feature-frozen `v2.0-cyanoptera` branch; alpha builds available now, GA targeted for later in October. Headline features: DuckDB-as-a-server, triggers, a `VARIANT` type, async I/O, a new SQL parser, and a new storage format — the biggest architectural release since 1.0.
- **Dagster 1.13.21** and **Prefect 3.8.5** (Sept 3) — routine patch releases; the bigger context is Prefect's July 2026 agreement to acquire Dagster Labs, still shaping the orchestration landscape as both ship in parallel.
- **dbt platform** — several behavior-change flags defaulted on Sept 1; Fusion engine added beta Salesforce Data 360 support. Separately, a Snowflake string/binary column-sizing change rolling out this month is a breaking risk for dbt-snowflake < v1.10.6 incremental models.
- **BigQuery Graph** reached GA (Sept 1) — GQL queries ~2x faster and undirected traversal ~100x faster than the April preview; relevant to anyone doing network analysis (e.g. passing networks) without a separate graph database.

**Additional recent context (8–30 days)**

- Arrow ADBC hit v24 (Jul 28); driver governance for several connectors has moved to an independent ADBC Driver Foundry outside Apache Arrow proper.
- DuckLake v1.0 shipped in April; a v1.1 standard is expected this September alongside the DuckDB v2.0 timeline.
- Apache Iceberg 1.12.0 is an imminent RC (most recent stable: 1.11.0, May); Delta Lake's most recent release remains 4.1.0 (March).
- Polars published a pandas→Polars migration case-study post (Aug 6) citing a 25% cloud-cost reduction from migrating 100+ Airflow DAGs and a 48x speedup on nanosecond market-data workloads — relevant ammunition for teams considering the same move for large play-by-play/tracking datasets.

No new sports-specific vendor or team blog posts connecting these tools to sports analytics work surfaced this week. The most relevant standing link is that **SportsDataverse** returns data natively as Polars DataFrames, but its own tooling docs were last updated in July, outside this window.

---

*Compiled as part of the repository's recurring sports-analytics research routine. See `paper-ranking-report.md` and `paper-ranking-scores.csv` for the full paper collection and rubric, and `feeds/` for the standing conference/opportunity watch list.*
