# Sports Analytics Papers — Novelty / Practicality / Reproducibility Ranking

An interactive version of this report is published as an HTML artifact (`paper-ranking-report.html`). Full per-file scores are in `paper-ranking-scores.csv`.

## Method

All 266 curated PDFs (repo root + `Soccer/`, `Pythagorean Win Expectancy and Weibull/`, and the `randoms/` grab-bag) were text-extracted and read at the front-matter level (title, abstract, intro, data/method section). Each was scored 1–10 on three axes:

- **Novelty** — originality at time of publication.
- **Practicality** — actionable value to a working analyst / front office / public practitioner.
- **Reproducibility** — could a competent analyst rebuild the result today? Public data (play-by-play, Retrosheet, Big Data Bowl, nflfastR/sportsdataverse) and released code raise the score; proprietary optical tracking (SportVU, Second Spectrum, Noah), slides-only decks, and commercial black boxes lower it.

**Composite** = N + P + R (out of 30). This is a fast directional triage from front-matter reads, not peer review. 8 scanned/slide-only PDFs were scored from filename + known literature.

## Collection at a glance

| Metric | Value |
|---|---|
| Papers read & scored | 266 |
| Unique works (curated, after dedup) | 165 |
| Duplicate copies found | 22 (across 20 works) |
| Public-data papers / mean reproducibility | 93 / 6.6 |
| Proprietary-data papers / mean reproducibility | 44 / 2.9 |
| Sport mix | Basketball 85 · NFL 26 · Soccer 12 · MLB 9 · NHL 8 · CFB 7 · other 18 |


## Top 25 overall (by composite)

| # | Paper | Yr | Sport | N | P | R | Σ/30 |
|--:|---|--:|---|--:|--:|--:|--:|
| 1 | nflWAR: a reproducible method for offensive player evaluation in football | 2019 | NFL | 8 | 8 | 9 | **25** |
| 2 | Overconfidence vs. Market Efficiency in the National Football League | 2005 | NFL | 9 | 9 | 7 | **25** |
| 3 | A Starting Point for Analyzing Basketball Statistics | 2007 | NBA | 6 | 8 | 9 | **23** |
| 4 | Analytics, have some humility: a statistical view of fourth-down decision making | 2023 | NFL | 8 | 7 | 8 | **23** |
| 5 | Improved NBA Adjusted +/- Using Regularization and Out-of-Sample Testing | 2010 | NBA | 8 | 8 | 7 | **23** |
| 6 | Operations Research on Football | 1971 | NFL | 10 | 7 | 6 | **23** |
| 7 | Colley's Bias Free College Football Ranking Method: The Colley Matrix Explained | 2003 | CFB | 7 | 6 | 9 | **22** |
| 8 | A Regression-based Adjusted Plus-Minus Statistic for NHL Players | 2010 | NHL | 7 | 7 | 8 | **22** |
| 9 | CourtVision: New Visual and Spatial Analytics for the NBA | 2012 | NBA | 8 | 7 | 7 | **22** |
| 10 | Statistical Methods in Sports with a Focus on Win Probability and Performance Evaluation | 2016 | NFL | 7 | 8 | 7 | **22** |
| 11 | A No-Tanking Draft Allocation Policy | 2020 | NBA | 7 | 6 | 8 | **21** |
| 12 | Modified Kelly Criteria | 2018 | Betting | 6 | 7 | 8 | **21** |
| 13 | An Expected Goals Model for Evaluating NHL Teams and Players | 2012 | NHL | 7 | 7 | 7 | **21** |
| 14 | Meta-Analytics: Tools for Understanding the Statistical Properties of Sports Metrics | 2016 | Multi | 7 | 7 | 7 | **21** |
| 15 | Route Identification in the National Football League | 2019 | NFL | 7 | 7 | 7 | **21** |
| 16 | SEAM: Synthetic Estimated Average Matchup for Player Matchups | 2020 | MLB | 7 | 7 | 7 | **21** |
| 17 | Measuring Spatial Allocative Efficiency in Basketball | 2020 | NBA | 8 | 7 | 6 | **21** |
| 18 | A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes (EPV) | 2016 | NBA | 9 | 7 | 5 | **21** |
| 19 | Using Zone Entry Data To Separate Offensive, Neutral, And Defensive Zone Performance | 2013 | NHL | 8 | 8 | 5 | **21** |
| 20 | The Price of Anarchy in Basketball | 2011 | NBA | 8 | 4 | 8 | **20** |
| 21 | A Derivation of the Pythagorean Won-Loss Formula in Baseball | 2006 | MLB | 8 | 4 | 8 | **20** |
| 22 | Evaluating one-shot tournament predictions | 2021 | Soccer | 7 | 5 | 8 | **20** |
| 23 | Track Anything: Segment Anything Meets Videos | 2023 | Other | 7 | 5 | 8 | **20** |
| 24 | Estimating NBA Team Shot Selection Efficiency from Aggregations of True, Continuous Shot Charts: A GAM Approach | 2024 | NBA | 6 | 6 | 8 | **20** |
| 25 | An easily implemented and accurate model for predicting NCAA tournament at-large bids | 2016 | NBA | 5 | 7 | 8 | **20** |

## Most novel

| N | Paper | Yr | Sport |
|--:|---|--:|---|
| 10 | Operations Research on Football | 1971 | NFL |
| 9 | Overconfidence vs. Market Efficiency in the National Football League | 2005 | NFL |
| 9 | A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes (EPV) | 2016 | NBA |
| 9 | POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data | 2014 | NBA |
| 9 | POINTWISE: Predicting Points and Valuing Decisions | 2014 | NBA |
| 8 | nflWAR: a reproducible method for offensive player evaluation in football | 2019 | NFL |
| 8 | Improved NBA Adjusted +/- Using Regularization and Out-of-Sample Testing | 2010 | NBA |
| 8 | Analytics, have some humility: a statistical view of fourth-down decision making | 2023 | NFL |
| 8 | CourtVision: New Visual and Spatial Analytics for the NBA | 2012 | NBA |
| 8 | Using Zone Entry Data To Separate Offensive, Neutral, And Defensive Zone Performance | 2013 | NHL |
| 8 | Measuring Spatial Allocative Efficiency in Basketball | 2020 | NBA |
| 8 | The Price of Anarchy in Basketball | 2011 | NBA |

## Most practical

| P | Paper | Yr | Sport |
|--:|---|--:|---|
| 9 | Overconfidence vs. Market Efficiency in the National Football League | 2005 | NFL |
| 8 | nflWAR: a reproducible method for offensive player evaluation in football | 2019 | NFL |
| 8 | A Starting Point for Analyzing Basketball Statistics | 2007 | NBA |
| 8 | Improved NBA Adjusted +/- Using Regularization and Out-of-Sample Testing | 2010 | NBA |
| 8 | Statistical Methods in Sports with a Focus on Win Probability and Performance Evaluation | 2016 | NFL |
| 8 | Using Zone Entry Data To Separate Offensive, Neutral, And Defensive Zone Performance | 2013 | NHL |
| 8 | Machine learning for sports betting: should forecasting models be optimised for accuracy or calibration? | 2023 | NBA |
| 8 | Analytics for the Front Office: Valuing Protections on NBA Draft Picks | 2019 | NBA |
| 8 | Predicting NBA Talent from Enormous Amounts of College Basketball Tracking Data | 2021 | NCAAB |
| 8 | The Logic of Sports Betting | 2019 | Betting |
| 7 | Operations Research on Football | 1971 | NFL |
| 7 | Analytics, have some humility: a statistical view of fourth-down decision making | 2023 | NFL |

## Most reproducible

| R | Paper | Yr | Sport |
|--:|---|--:|---|
| 9 | nflWAR: a reproducible method for offensive player evaluation in football | 2019 | NFL |
| 9 | A Starting Point for Analyzing Basketball Statistics | 2007 | NBA |
| 9 | Colley's Bias Free College Football Ranking Method: The Colley Matrix Explained | 2003 | CFB |
| 9 | An improvement to the baseball statistic "Pythagorean Wins" | 2016 | MLB |
| 8 | Analytics, have some humility: a statistical view of fourth-down decision making | 2023 | NFL |
| 8 | A Regression-based Adjusted Plus-Minus Statistic for NHL Players | 2010 | NHL |
| 8 | A No-Tanking Draft Allocation Policy | 2020 | NBA |
| 8 | Modified Kelly Criteria | 2018 | Betting |
| 8 | The Price of Anarchy in Basketball | 2011 | NBA |
| 8 | An easily implemented and accurate model for predicting NCAA tournament at-large bids | 2016 | NBA |
| 8 | Evaluating one-shot tournament predictions | 2021 | Soccer |
| 8 | Estimating NBA Team Shot Selection Efficiency from Aggregations of True, Continuous Shot Charts: A GAM Approach | 2024 | NBA |

## The proprietary-data trap

High novelty (≥7) but low reproducibility (≤3) — strong ideas locked behind optical-tracking feeds you can't buy. This is the collection's dominant fault line, concentrated in the 2012–2019 NBA SportVU / Second Spectrum era.

| Paper | Yr | Sport | N | P | R |
|---|--:|---|--:|--:|--:|
| POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data | 2014 | NBA | 9 | 7 | 3 |
| POINTWISE: Predicting Points and Valuing Decisions | 2014 | NBA | 9 | 6 | 2 |
| Predicting NBA Talent from Enormous Amounts of College Basketball Tracking Data | 2021 | NCAAB | 8 | 8 | 2 |
| Approaching In-Venue Quality Tracking from Broadcast Video using Generative AI | 2024 | Soccer | 8 | 7 | 2 |
| Deconstructing the Rebound with Optical Tracking Data | 2012 | NBA | 8 | 6 | 3 |
| The Dwight Effect: A New Ensemble of Interior Defense Analytics for the NBA | 2013 | NBA | 8 | 6 | 3 |
| The Three Dimensions of Rebounding | 2014 | NBA | 8 | 6 | 3 |
| Counterpoints: Advanced Defensive Metrics for NBA Basketball | 2015 | NBA | 8 | 6 | 3 |
| Possession Sketches: Mapping NBA Strategies | 2017 | NBA | 8 | 6 | 3 |
| Data-Driven Ghosting using Deep Imitation Learning | 2017 | Soccer | 8 | 6 | 2 |
| The Hot Hand: A New Approach to an Old "Fallacy" | 2014 | NBA | 8 | 5 | 3 |
| To Crash or Not To Crash: Offensive Rebounding vs. Transition Defense in the NBA | 2013 | NBA | 7 | 7 | 3 |
| Quantifying Shot Quality in the NBA | 2014 | NBA | 7 | 7 | 2 |
| Recognizing and Analyzing Ball Screen Defense in the NBA | 2016 | NBA | 7 | 7 | 2 |

## Best of the `randoms/` folder

| Σ/30 | Paper | Yr | Sport | N | P | R |
|--:|---|--:|---|--:|--:|--:|
| 20 | Adjusted Plus-Minus for NHL Players using Ridge Regression | 2012 | NHL | 7 | 7 | 6 |
| 20 | An Improved Adjusted Plus-Minus Statistic for NHL Players | 2011 | NHL | 7 | 7 | 6 |
| 20 | Characterizing the Spatial Structure of Defensive Skill in Professional Basketball | 2015 | NBA | 9 | 7 | 4 |
| 20 | Evaluating NHL Goalies, Skaters, and Teams Using Weighted Shots | — | NHL | 7 | 7 | 6 |
| 19 | Large Data and Bayesian Modeling: Aging Curves of NBA Players | 2019 | NBA | 7 | 6 | 6 |
| 19 | Strategies for Pulling the Goalie in Hockey | — | NHL | 7 | 7 | 5 |
| 19 | The Harsh Rule of the Goals: Data-Driven Football Performance Indicators | — | Soccer | 7 | 6 | 6 |
| 18 | Basketball Teams as Strategic Networks | 2012 | NBA | 7 | 5 | 6 |
| 18 | Estimation of NBA Players' Offense/Defense Ratings through Shrinkage | 2014 | NBA | 6 | 6 | 6 |
| 17 | An Analysis of Factors Contributing to Wins in the NHL | 2014 | NHL | 5 | 6 | 6 |
| 17 | Archetypoid Analysis for Sports Analytics | — | Multi | 7 | 5 | 5 |
| 17 | Depth of Player Rotation on Game Performance in NCAA Men's Basketball | — | NBA | 5 | 6 | 6 |

## Duplicate / near-duplicate groups

Same work stored under different filenames (byte-identical copies or arXiv-vs-conference versions); scores held identical across copies:

- Three Dimensions of Rebounding (x3)
- Body Shots / Shooting Styles / Steph Curry (x3)
- Meta-Analytics (x2, + JQAS version)
- Graphical Model for Basketball Match Simulation (x2)
- Applying Deep Learning to Basketball Trajectories (x2)
- Possession Sketches: Mapping NBA Strategies (x2)
- Recognizing and Analyzing Ball Screen Defense (x2)
- Using In-Game Shot Trajectories / Defensive Impact (x2)
- Evaluating NFL Plays: EP Adjusted for Schedule (x2)
- Modeling Player and Team Performance in Basketball (x2)
- Estimating NBA Team Shot Selection Efficiency (x2)
- Miller Pythagorean Won-Loss derivation (x2)
- Testing Pythagorean on D-I CFB (x2)
- 2023 Estimating Positional Plus-Minus (.docx x2)
