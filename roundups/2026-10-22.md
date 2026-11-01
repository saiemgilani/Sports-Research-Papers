# Sports analytics roundup — week ending 2026-10-22

Window: 2026-10-15 → 2026-10-22, with a 30-day look-back for papers. Sources: arXiv API, PyPI, CRAN (crandb), web search. Package dates are first-upload dates on those registries.

## 1. Sports Analytics Literature & Research

**Past 7 days:** nothing new in the arXiv sports-statistics space. The 15–22 Oct hits were robotics, vision and an unrelated clinical "win probability" paper. The substantive items are from the prior 3–4 weeks and are now in the library (PDF in repo root, text in `md/`, scores in `paper-ranking-scores.csv`).

| Paper | Date | Σ/30 | Why it matters |
|---|---|--:|---|
| [Who Blocks Whom? Probabilistic Pass-Blocking Assignments](https://arxiv.org/abs/2609.33664) — Brahme, Mehta, Matthews, Franks | 27 Sep | 24 | Big Data Bowl tracking, matchup HMM ported from basketball; frame-level blocker→rusher assignment feeding an APM. Public data, reproducible. |
| [Credit Attribution in Soccer Networks Using Multivariate Hawkes Processes](https://arxiv.org/abs/2610.12775) — Kornberg, Xu | 8 Oct | 22 | Shares credit for shots across the buildup; StatsBomb open data. |
| [Concave Processes for Multi-Task Career Trajectories](https://arxiv.org/abs/2609.33752) — Brahme, Franks | 27 Sep | 20 | Nonparametric aging curves across NBA metrics with a shared latent space. |
| [A Markov Chain Approach to Modeling Rugby Union](https://arxiv.org/abs/2610.04813) — Watts, Pipping-Gamón | 3 Oct | 18 | Score/time/field-position state space; WP and expected points. |
| [Strategic Multi-Agent Learning for Action Valuation of All Players in Football](https://arxiv.org/abs/2610.05961) — Ide et al. | 5 Oct | 17 | MPE-inspired valuation incl. off-ball players; code only "upon acceptance". |
| [SambaGraph](https://arxiv.org/abs/2609.25569) — Reyes-Angulo et al. | 22 Sep | 17 | Graph benchmark from World Cup 2022; PFF-derived data. |
| [From Metrics to Decisions in NBA Analytics](https://arxiv.org/abs/2609.27245) — Zhou, Guan | 23 Sep | 16 | Review with six "decision-readiness" gates. |

Seen, not archived (vision/robotics, out of scope for the rubric): SoccerNet-FoulRet (2610.09742), BMASH header spotting (2609.39300), Throwing4 (2610.16383), TTNet table-tennis (2610.07823).

Other: Springer published the ISACE 2026 (Vancouver) proceedings, 28 full papers — [link](https://link.springer.com/book/10.1007/978-3-032-27272-0). Springer pages are subscription previews, so nothing was downloaded. The repo's own automation also continues to add JSSM in-press papers (latest 19 Oct), which are mostly exercise physiology rather than analytics.

## 2. Open-Source Packages & Ecosystem Updates

Registry data only; GitHub release notes for the R packages were not reachable from this session.

- **sportsdataverse-py** — latest PyPI release 0.1.4 (1 Sep); a `docs-index` rolling release was refreshed 6 Oct. Nothing new in the past week.
- **R packages (CRAN)** — all had major releases in the last two months: cfbfastR 3.0.0 and wehoop 3.0.0 (24 Aug), hoopR 3.1.0 (25 Aug), baseballr 2.0.0 (26 Aug), fastRhockey 1.0.0 (25 Aug), nflfastR 6.0.0 (18 Sep). nflreadr is unchanged since 1.5.1 (Apr). **nflplotR 1.7.1 (20 Oct)** is the only one inside the window.
- **Python peers** — kloppy 3.19.1 (3 Oct); statsbombpy 1.22.0 (30 Jul); nflreadpy 0.1.5 (Nov 2025) and nfl-data-py 0.3.3 (2024) look dormant.

## 3. Data Engineering & Tooling

- **Polars 2.0.0** — released 6 Oct (PyPI). Per secondary sources, the lazy engine now defaults to streaming, so row order is no longer guaranteed for joins/group-bys/unpivots unless `maintain_order` or an explicit sort is used. Not verified against official notes. sportsdataverse-py already requires `polars>=2`, so any ordering assumptions there are worth auditing. [Upgrade guide (secondary)](https://www.kunalganglani.com/blog/polars-2-0-upgrade-guide)
- **DuckDB 2.0.0** — on PyPI 21 Oct. Preview coverage lists server mode (Quack extension), VARIANT type, new storage format and parser. [Preview](https://duckdb.org/2026/08/17/duckdb-20-highlights). The official release post was not found.
- **Apache Arrow / pyarrow 26.0.0** — on PyPI 9 Oct; no release notes found. R `arrow` is at 25.0.1.
- **Apache Airflow 3.4.0b2** — 20 Oct (b1 on 13 Oct). **Prefect 3.9.0** — 21 Oct. **Dagster 1.13.26** — 9 Oct. **dbt-core 1.12.6** and 2.0.0rc9 — 14 Oct. deltalake 1.6.6 (24 Sep); pyiceberg 0.12.0 (1 Sep).

## Analysis and links to existing work

- **Who Blocks Whom** is the best fit for the repo's focus: it reuses the 2015 Franks matchup HMM and the nflWAR/APM line already in the collection. If anyone builds OL evaluation on Big Data Bowl data, start here.
- **Hawkes credit attribution** is directly implementable against StatsBomb open data via kloppy/statsbombpy; a candidate for a sportsdataverse-py soccer example.
- **Rugby Markov model** parallels the EP/WP approach in the football stack; useful as a calibration-check template.
- **SambaGraph / PFF caveat:** the paper is archived, but it depends on PFF-derived data; per repo policy, don't pull or redistribute that data.
- **Polars 2.0** ordering change is the one item that may need action in downstream repos (sportsdataverse-py, game-on-paper-app's processor). I did not change those repos in this run.
- Scores are quick front-matter triage (same method as `paper-ranking-report.md`), not peer review.
