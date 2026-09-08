# Weekly Sports Analytics Roundup

A recurring digest across three areas: sports analytics literature/research, the
SportsDataverse open-source package ecosystem, and data engineering/tooling relevant to
building sports-data pipelines. Newest entry first. Companion to
[`sports-analytics-feed.md`](sports-analytics-feed.md) (conference/journal source catalog)
and [`sports-analytics-opportunities.md`](sports-analytics-opportunities.md) (CFP/deadline
feed) — this file is the editorial "what happened this week" layer those structured feeds
don't cover.

---

## 2026-09-08

*Window: last 180 days for context; items flagged "past 7 days" cover 2026-09-01 through
2026-09-08.*

### 1. Sports Analytics Literature & Research

**Past 7 days** (all via arXiv; all five below were pulled into this repository as full
PDFs with markdown analysis notes and ranking-rubric scores — see links):

- **[A Fairness Audit of the Duckworth–Lewis–Stern Method](https://arxiv.org/abs/2609.04754)** (Roy, 4 Sep) — first large-scale (8,150-match) empirical bias audit of cricket's rain-interruption target formula; finds a +6.13-run gender-differential miscalibration and ships a drop-in calibration layer plus a new "Win-Flip Rate" fairness metric, with code/data released. Highest-scored item this week (25/30). Repo: [PDF](<../2026 A Fairness Audit of the Duckworth-Lewis-Stern Method - Roy.pdf>) · [notes](<../md/2026 A Fairness Audit of the Duckworth-Lewis-Stern Method - Roy.md>).
- **[Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition](https://arxiv.org/abs/2609.03786)** (Lee & Ko, 3 Sep) — uses the KBO's 2024 ABS rollout as a natural experiment on umpire count-pressure bias; directly relevant to MLB's own ABS/Challenge System debate. Repo: [PDF](<../2026 Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition - Lee, Ko.pdf>) · [notes](<../md/2026 Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition - Lee, Ko.md>).
- **[Unified Pitch Graphs for Diagnosing Pitching Strategy](https://arxiv.org/abs/2609.03810)** (Lee & Ko, 3 Sep) — hierarchical trajectory-preserving graph over 3.94M MLB Statcast pitches; support-adaptive backoff lifts path coverage 18.9%→94.9%. Repo: [PDF](<../2026 Unified Pitch Graphs for Diagnosing Pitching Strategy - Lee, Ko.pdf>) · [notes](<../md/2026 Unified Pitch Graphs for Diagnosing Pitching Strategy - Lee, Ko.md>).
- **[The Traveling Tournament Problem: An Overview](https://arxiv.org/abs/2609.03612)** (Van Bulck, Yang, Goossens & Trick, 3 Sep) — 25-year survey of the canonical sports-scheduling optimization problem, doubling as the continuation of Michael Trick's RobinX benchmark repository. Dedicated to co-originator Kelly Easton (d. Feb 2026). Repo: [PDF](<../2026 The Traveling Tournament Problem An Overview - Van Bulck, Yang, Goossens, Trick.pdf>) · [notes](<../md/2026 The Traveling Tournament Problem An Overview - Van Bulck, Yang, Goossens, Trick.md>).
- **[Landmark-Based Discrimination of Injury-Associated Athlete-Sessions](https://arxiv.org/abs/2609.03790)** (Chatzidimitriou & Tserpes, 3 Sep) — tests fixed-timepoint features for injury prediction on the SoccerMon dataset (48 elite women players); results were weak (ROC-AUC 0.37–0.61), a useful negative result. Not added to the library (weak/negative result, lower priority for full ingestion) — flagged here for awareness.
- **[Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection](https://arxiv.org/abs/2609.04803)** (Wang, Li, Wang & Huang, 4 Sep) — graph + pointer network predicting soccer pass receivers from broadcast-style partial freeze-frame data. Repo: [PDF](<../2026 Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection - Wang, Li, Wang, Huang.pdf>) · [notes](<../md/2026 Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection - Wang, Li, Wang, Huang.md>).
- **[MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video](https://arxiv.org/abs/2609.02854)** (Bradshaw, Giordano, et al., 2 Sep) — phone-camera center-of-mass estimation; athlete-monitoring-relevant but not sport-specific, not added to the library.

**Notable gap this week:** no new JQAS or Journal of Sports Analytics issues, no Open
Source Football / StatsBomb / Squared Statistics posts, and no MLB/NFL/NHL win-probability
or betting-market papers in the past 7 days. MIT Sloan SSAC27's Research Paper Competition
opened (abstracts due 2026-10-01) — a process update, tracked separately in
[`sports-analytics-opportunities.md`](sports-analytics-opportunities.md).

**Older, for context (8–180 days):** ELASTIC event/tracking synchronization (arXiv:2608.30227);
HoopMind NBA possession planning (2608.29563); tennis "Big Three era" extremes analysis
(2608.27362); context-adjusted T20 player evaluation (2608.18020); Longitudinal Bayesian
Networks for NBA team performance (2608.09824); H-VAEP/H-xT handball action valuation
(2608.12926); NBA scoring-pattern network analysis (2606.27957); match-fixing detection via
in-play betting markets (2605.30209); NBA officiating impact metric (2605.17845); odds-to-
probability forecasting methods (2604.17194); broadcast-video soccer computer vision
(2604.08722); Bayesian NFL ball-carrier movement models (2603.17866); broadcast-video
pitching injury-risk screening (2603.04864); plus the Squared Statistics Historical RAPM
Project (pre-play-by-play NBA RAPM back to 1969) and recent JQAS Vol. 20 issues (Grid WAR
for starting pitchers; positional plus-minus in the NBA).

### 2. Open-Source Packages & Ecosystem Updates

**Past 7 days:**

- **sportsdataverse-py v0.1.4** (2026-09-01) — fixed CFB EP/WP inputs (mirrored end-yardlines, flipped win-probability calc), added penalty-analysis columns and air-yards metrics to box scores.
- **cfbfastR** — no new version tag, but active post-3.0.0 stabilization on `main`: fixed 2-pt/xpass scoring-era cuts, corrected vignette claims about the 2-pt model, raised the CFBD API retry budget, rewrote EP model docs (all merged 2026-09-01–07, maintainer saiemgilani).
- **nflverse-data** — weekly automated refresh for the new NFL season: `schedules` (Sep 8), `espn_data`/`weekly_rosters`/`players` (Sep 7), `ftn_charting` (Sep 1).

**Older, for context — a coordinated major-version wave (2026-08-24 to 09-01):**
cfbfastR 3.0.0 (39 new dataset loaders, 65 ESPN wrappers, CFB EP/WP/4th-down/QBR models),
hoopR 3.1.0 (CollegeBasketballData, Bart Torvik, Basketball-Reference wrappers), wehoop 3.0.0
(WNBA/WBB crosswalks, Her Hoop Stats), baseballr 2.0.0 (ESPN MLB/college-baseball, Fox
Sports Bifrost API), fastRhockey 1.0.0 (NHL/PWHL, migrated to httr2). nflplotR 1.5.0/1.6.0
added ggplot2 v4 compatibility (Sep–Nov 2025); nflreadpy (new Python nflreadr port) has
shipped v0.1.0→0.1.5 since Sep 2025.

**Quiet / effectively unmaintained:** worldfootballR (repo archived), nfl_data_py (repo
archived, superseded by nflreadpy), pybaseball (last release Sep 2023), ffscrapr (last
release Feb 2023), cfbplotR/cfb4th/sportypy/gamezoneR/puntr (no recent tagged releases).

*Full detail: this week's research pass covered GitHub releases, CRAN, and PyPI for the
full sportsdataverse/nflverse/ffverse family — see commit history for the complete agent
report if a deeper dive is needed.*

### 3. Data Engineering & Tooling

**Past 7 days — the big story is two breaking-change RCs landing the same day:**

- **Polars 2.0.0-rc1** (Sep 2) — `LazyFrame.collect(engine="auto")` now defaults to the
  streaming engine (~5x faster claimed); **breaking:** row order no longer guaranteed by
  default on joins/group-bys/unpivots — use `maintain_order=True` if sports box-score merges
  depend on row order.
- **dbt Core 2.0.0-rc1** (Sep 2) — Rust-based Fusion engine foundation; Parquet metadata
  artifacts (queryable instead of parsing the full manifest — matters for large dbt
  projects), stricter YAML spec, big parse-time improvements.
- **DuckDB v2.0-alpha** ("cyanoptera", Sep 2) — feature freeze cut, alpha builds open;
  stable v2.0 targeted for second half of October 2026.
- **AWS finalized the DuckLabs acquisition** (Sep 1) — DuckDB itself stays MIT-licensed and
  independently governed by the DuckDB Foundation; not an acquisition of DuckDB.
- Routine patches: Dagster 1.13.21, Prefect 3.8.5, dbt Core 1.12.4/1.11.15 (all Sep 3–8).
  Snowflake External Lineage reached GA (Sep 3); BigQuery shipped a Rust SDK preview and
  Conversational Analytics GA updates (Sep 1–3); Databricks GA'd Arrow support for Zerobus
  Ingest.

**Practical takeaway:** if a sports-data pipeline sits on Polars or dbt, test against the
2.0 release candidates before they go stable — both carry breaking changes that are easy to
miss (row-order semantics; artifact/parse behavior).

**Older, for context:** Apache Airflow 3.3 added Stateful Tasks/Asset State Store and a
Language Task SDK (Jul); Dagster 1.13 "Octopus's Garden" added AI-assisted dev skills and
20+ new components (Apr); pandas 3.0 shipped PyArrow-backed string dtype and copy-on-write
by default (Jan), quiet since; Iceberg is now genuinely multi-engine-interoperable across
BigQuery/Databricks/Snowflake/S3 Tables (May–Aug); R tidyverse/data.table quiet and stable.

---

## Scope note

GitHub access for the session that compiles this roundup is scoped to this repository only.
Cross-posting analysis into SportsDataverse or other sports-analytics community repositories
(issues, discussions, PRs) requires access this session does not have — any such follow-up
needs to happen from a session with that repository authorized, or manually by a maintainer.
