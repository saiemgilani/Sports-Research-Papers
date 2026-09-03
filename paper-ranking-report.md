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

## Additions since the 2026-07 ranking pass

Papers added to the collection after the original 266-PDF sweep. Same 1–10 rubric, same
composite; they are appended to `paper-ranking-scores.csv` with `folder = library` so the
original pass's counts above stay reproducible.

| Paper | Yr | Sport | N | P | R | Σ/30 |
|---|--:|---|--:|--:|--:|--:|
| **Nuthin' But A G League: Estimating league translation factors** | 2026 | NBA | 8 | 7 | 8 | **23** |
| Lineup Regularized Adjusted Plus-Minus (L-RAPM) | 2026 | NBA | 7 | 8 | 6 | **21** |
| A predictive metamodel for college football | 2025 | CFB | 6 | 8 | 7 | **21** |
| Lasso Multinomial Performance Indicators for in-play Basketball Data | 2024 | NBA | 6 | 8 | 7 | **21** |
| Hierarchical Bayesian Modeling of Cross-League Performance Translation in Elite Football | 2026 | Soccer | 6 | 6 | 8 | **20** |
| WINSCORE revisited: A model-based evaluation of player performance in the NBA and EuroLeague | 2026 | NBA | 5 | 8 | 7 | **20** |
| iWinRNFL: A Simple, Interpretable & Well-Calibrated In-Game WP Model for NFL | 2017 | NFL | 5 | 7 | 8 | **20** |
| A causal approach for detecting team-level momentum in NBA games | 2023 | NBA | 8 | 5 | 7 | **20** |
| mWAR: A Bayesian estimator of manager value | 2026 | MLB | 7 | 6 | 7 | **20** |
| Understanding team collapse via probabilistic graphical models | 2024 | NBA | 7 | 4 | 7 | **18** |
| Implicit Biases in Refereeing: Lessons from NBA Referees | 2022 | NBA | 5 | 5 | 8 | **18** |
| tHoops: A Multi-Aspect Analytical Framework for Spatio-Temporal Basketball Data | 2017 | NBA | 7 | 5 | 6 | **18** |
| The Anatomy of the Three-Point Shot | 2016 | NBA | 7 | 4 | 7 | **18** |
| Footballonomics: The Anatomy of American Football | 2016 | NFL | 5 | 5 | 8 | **18** |
| Predictions of european basketball match results with ML algorithms | 2023 | basketball | 5 | 6 | 7 | **18** |
| DeepHoops: Evaluating Micro-Actions in Basketball | 2019 | NBA | 8 | 5 | 4 | **17** |
| Big data analytics for scoring probability under high pressure *(abstract only)* | 2017 | basketball | 6 | 5 | 4 | **15** |
| Concurrent validity of computer-vision AI player tracking from broadcast footage | 2026 | Soccer | 5 | 7 | 3 | **15** |
| How to assess leader capabilities: AI algorithms to evaluate NBA head coaches | 2025 | NBA | 4 | 4 | 6 | **14** |
| The Anatomy of Corner 3s in the NBA | 2021 | NBA | 7 | 6 | 3 | **16** |

### Hierarchical Bayesian Modeling of Cross-League Performance Translation in Elite Football

Shaikh, *Journal of Sports Analytics* 12 (SAGE, Aug 2026), [10.1177/22150218261481583](https://doi.org/10.1177/22150218261481583), CC BY-NC.
Markdown: [`md/library/journals/Journal of Sports Analytics/2026/…`](md/library/journals/Journal%20of%20Sports%20Analytics/2026/2026%20-%20Hierarchical%20Bayesian%20Modeling%20of%20Cross-League%20Performance%20Translation%20in%20Elite%20Football%20-%20Shaikh.md).

**What it does.** Estimates the "league tax" — how a footballer's per-90 process metrics shift
when they move into the Premier League from La Liga, Bundesliga, Serie A or Ligue 1. The
response is a log-ratio of destination-to-source per-90 rate (with an ε = 0.05 offset); the mean
is decomposed into a source-league random effect, a destination-team random effect and a
quadratic age term, fit as a **joint multivariate Student-t (ν = 6)** with an **LKJ(η = 3) prior**
on the metric correlation matrix. Two separate bridges — attacking/midfield (KP, PrgP, PrgC,
SCA; n = 174 train / 45 test) and defensive (TklW, Int, Clr, Blocks; n = 106 / 35) — because
forcing one covariance structure across both metric families learns team style, not player talent.
PyMC + NUTS, 2 chains × 1500 draws, zero divergences, R̂ ≤ 1.005.

**The two ideas worth stealing.**

1. **Within-league transfers as an untreated control.** Intra-Premier-League moves are included
   in training with the league term pinned to τ = 0. They contribute nothing directional but they
   give the residual and team-level variance components an empirical anchor for the *universal*
   shock of changing clubs — new teammates, new system, new manager. Without that anchor, a
   cross-border-only bridge silently attributes ordinary transfer friction to the league. This is a
   general trick for any "translation factor" problem where the treatment and the move are
   confounded, and it is directly portable to NCAA→NBA, G League→NBA, and portal transfers.
2. **Calibration is the gate; MAE is a diagnostic.** The paper states up front that it does not
   claim to beat Ridge or a GBM on point error, and it doesn't — Ridge and GBM edge it on MAE
   on several metrics. What it delivers is empirical coverage of the nominal 90% HDI: 0.889–0.933
   on the attacking bridge. It then reports the one place calibration fails (interceptions, 0.657)
   and traces it to a real train/test variance shift (0.380 → 0.486) rather than burying it.

**Where it is weak.** Premier League destinations only, outfield players only, Year-1 only,
n = 174/106 training rows. The single credible empirical finding is one coefficient — La Liga SCA,
posterior mean +0.306, 90% HDI [+0.015, +0.578] — and the paper is explicit that transfer
selection is non-random, so even that is a conditional association and not a league effect. The
DEF bridge pools centre backs and full backs because position labels were unavailable, which
is the stated cause of its Clr/Int miscalibration. Novelty is 6 rather than higher because the
machinery (partial pooling, LKJ, Student-t) is standard and league-as-random-effect goes back to
McHale & Szczepański (2014); what is new is the control group and the evaluation posture.

**Why reproducibility scores 8** — the joint top mark among the soccer papers in this collection,
where the median is 3. Public FBref-derived Kaggle datasets named by URL; every prior written
out; likelihood, ν, η, the minutes-weighting function and its sensitivity range all specified;
the full stack pinned to patch version (PyMC 5.28.5, NumPyro 0.21.0, JAX 0.7.2, ArviZ 0.22.0,
scikit-learn 1.6.1); seed fixed at 42; sampler settings given; code public at
`github.com/mohammadarshan/football-league-translation` (reachable as of 2026-09-02). It loses
two points only because the bridge-construction judgment calls (the 5×90s inclusion floor, the
ε offset, the ATT/MID bucketing) are described but not independently verified here.

> **Provenance note.** The stored PDF is the author's open SocArXiv preprint
> ([10.31235/osf.io/59a7s](https://doi.org/10.31235/osf.io/59a7s)); SAGE's version of record is
> Cloudflare-blocked from datacenter IPs. Abstract, tables and reported numbers match the
> published record; final copy-editing may differ.

### Lineup Regularized Adjusted Plus-Minus (L-RAPM): Basketball Lineup Ratings with Informed Priors

Petridis & Pelechrinis, arXiv:[2601.15000](https://arxiv.org/abs/2601.15000) \[cs.LG], Jan 2026.
Markdown: [`md/2026 Lineup Regularized Adjusted Plus-Minus (L-RAPM)…`](md/2026%20Lineup%20Regularized%20Adjusted%20Plus-Minus%20(L-RAPM)%20-%20Petridis,%20Pelechrinis.md).

**What it does.** Rates *lineups*, not players. Two stages: fit Sill-style RAPM on the prior season to get player coefficients (λ<sub>off</sub> = 4000, λ<sub>def</sub> = 6000 by validation), then fit a second ridge on the current season where the covariates are the offensive and defensive **five-man units** rather than individuals — and shrink each lineup coefficient not toward zero but toward a prior equal to league points-per-possession plus the sum of its five players' RAPM. Evaluated on NBA 2022–23 → 2023–24 in an expanding weekly window, out-of-sample throughout, scored on RMSE.

**Why it matters more than its effect size suggests.** The headline gain is 1.5–5% RMSE over raw lineup ratings, which sounds negligible until the paper contextualises it: 1.5% over a game's possessions is ≈ 3.4 points, larger than the ~2-point home edge books carry. Two structural properties do the real work:

1. **It rates lineups that have never played.** Raw ratings cannot — the baseline falls back to league-average points per possession — and LinNet, the prior art, cannot either, because an unseen lineup is not in the training network. L-RAPM has a prior for every combination of five rostered players, so it answers "should I try this five?" That is the question a coach actually asks, and δ ≈ 5% on unseen lineups is the paper's largest gain.
2. **The gain is inversely proportional to sample size.** Above ~500 possessions raw ratings have converged and L-RAPM adds almost nothing; below ~50 it dominates. Since the average NBA lineup sees ~17 offensive and ~17 defensive possessions a season, the regime where it helps *is* the regime.

The motivating arithmetic is worth quoting: a lineup with 10 offensive possessions and 13 points has a raw offensive rating of 113.0; flip one made three to a miss — a 64% event — and it reads 100.0. **That single-shot swing spans the gap between the best and worst offence in the league.**

**Where it is weak.** Rookies and other players absent from the prior season get RAPM = −1 on both sides, a large arbitrary penalty on a points-per-possession scale; the authors flag it and propose in-season updating instead. One shared λ for offensive and defensive lineup coefficients, when their own player-level model uses two and the cited literature says offence stabilises faster. No code or data artifact, and the possession-level lineup panel has to be assembled from play-by-play — hence reproducibility 6 rather than higher, since the *method* is fully specified (both objective functions are written out) but nothing ships.

---

### WINSCORE revisited: A model-based evaluation of player performance in the NBA and EuroLeague

Carta & Favero, *Journal of Sports Analytics* 12 (SAGE, Jul 2026), [10.1177/22150218261468843](https://doi.org/10.1177/22150218261468843), CC BY-NC.
Markdown: [`md/library/journals/Journal of Sports Analytics/2026/…`](md/library/journals/Journal%20of%20Sports%20Analytics/2026/2026%20-%20WINSCORE%20revisited%20-%20A%20model-based%20evaluation%20of%20player%20performance%20in%20the%20NBA%20and%20EuroLeague%20-%20Carta,%20Favero.md).

**What it does.** Re-derives Berri et al. (2006) WINSCORE as a structural two-parameter regression: season wins on the difference between points per *employed* possession and opponent points per *acquired* possession. Because the box-score statistics enter through a nonlinear possession ratio rather than as separate regressors, the collinearity that wrecks an unrestricted wins-on-everything regression never arises — the model has exactly two free parameters. The per-statistic weights are then recovered **by simulation**, not estimation: perturb one statistic off its mean, re-predict wins, take the difference. That construction is what makes the weights internally consistent — a made three is worth its three points *net of the possession it consumed*.

**The three results worth keeping.**

1. **PIR is statistically retired.** In the encompassing regression of actual wins on both models' fitted values, the WINSCORE coefficient is never distinguishable from 1 and the PIR coefficient is never distinguishable from 0, in all three samples; the joint restriction δ₁ = 1, δ₂ = 0 is never rejected. The same holds against Four Factors, OBPM, DBPM, BPM and VORP. Team R² is 0.95/0.93/0.86 for WINSCORE versus 0.91/0.91/0.76 for PIR.
2. **Every possession-changing event carries the same weight** (+0.036 EuroLeague, +0.032 NBA): offensive rebound, defensive rebound, steal, forced turnover, team rebound. That is the model's central structural claim and precisely what PIR's unit weights get wrong. The weights are stable across a 1994–2005 NBA sample, a 2021–24 NBA sample, and the EuroLeague.
3. **The low-minute extrapolation trap — the part most directly applicable elsewhere.** Berri's player-level measure projects each player to full-season minutes before building the role benchmark. Since the projection factor is mechanically largest exactly where the sample is thinnest, a handful of bench players distort the benchmark for *everyone in that role*. The EuroLeague evidence is stark: a 5.3-minute guard projects to −38.6 wins, two players under 100 minutes out-project the best full-season player at their position, and the guard-role average **flips from −0.506 to +0.039** once the edge cases are dropped. The fix is a caliper rather than a cutoff — benchmark each player only against same-role players whose minutes fall within ±10% of his — and the diagnostic that proves it works is that summed player contributions should equal team wins: the uncorrected version turns Berlin's 5 real wins into 15.5, the caliper version into −1.6.

**Where it is weak.** The core model is twenty years old and re-estimated; novelty 5 reflects that the contributions are the caliper, the EuroLeague replication and the single-game opponent-matched variant, not the framework. Validation is cross-sample and cross-league by choice, with no held-out predictive test — defensible given the stated measurement (not forecasting) objective, but it means "R² = 0.93" is in-sample. Assists, blocks and fouls sit outside the possession structure and are folded back in through auxiliary regressions whose coefficients are insignificant. And the single-game case study is one game, explicitly labelled an illustration.

> **Provenance note.** **No PDF is held for this paper.** SAGE's version of record is Cloudflare-blocked from datacenter IPs and, unlike the Shaikh paper above, there is no preprint or repository copy anywhere (OpenAlex: `any_repository_has_fulltext = false`). The markdown was extracted from the SAGE HTML version of record through the `r.jina.ai` reader proxy on 2026-09-02: **prose is verbatim, tables are transcribed, but equations were reconstructed by hand from mangled MathJax and the figures and Appendices A–B are absent.** Verify any formula against the publisher PDF before implementing. A replication package with an R data-retrieval and estimation pipeline is referenced in footnote 2, but no URL for it appears in the extracted text — hence `code = referenced` rather than `yes`, and reproducibility 7 rather than 8.

---

## The Pelechrinis arXiv batch (added 2026-09-02)

Thirteen arXiv preprints, every one with Konstantinos Pelechrinis as an author — effectively his public corpus. **Four were already in the collection** under their published filenames and were *not* re-added as second copies; they are recorded in the duplicate list below with their arXiv identifiers so the link is captured without a redundant PDF. The other **nine are new** and scored above.

All nine markdown files in `md/` are **machine conversions** (`pdftotext` + scripted reflow, headed by an explicit provenance comment). Equations, tables and figures are not preserved — consult the PDF for those. This matches how the rest of the `md/` corpus was produced.

### The two that matter most for a public-data practitioner

**Lasso Multinomial Performance Indicators (2024) — 21/30, the highest of the batch.** Damoulaki, Ntzoufras & Pelechrinis run the RAPM bake-off nobody had published: ridge (the standard) versus lasso versus regularized binary and multinomial logistic, over **322,852 possessions** from every NBA game in 2021–22. The observation driving it is almost embarrassingly simple and correct — **points per possession is a discrete variable taking values 0 to 3, so fitting OLS or ridge to it is the wrong likelihood.** A regularized multinomial logit gets the response family right; their final indicator, **wEPTS**, takes expected points from that model and weights each player by his share of the team's possessions, and it beats every other RAPM variant they test. Lasso also beats ridge on their validation criteria. For anyone shipping a ridge-on-points RAPM — which is nearly everyone public — this is a directly comparable upgrade path with the comparison already done.

**iWinRNFL (2017) — 20/30.** A ten-variable logistic in-game win probability model on seven seasons of public play-by-play, 75% winner accuracy against a 63% pre-game baseline, and — the actual point — **well calibrated**. Its most useful contribution is a negative result stated plainly: *"we have also evaluated more complex, non-linear, models using the same set of features, without any significant improvement in performance."* The paper's framing is that the proprietary models under scrutiny after the 2016 comeback season could not be evaluated at all, and that an open, calibrated, boring model is worth more than a closed accurate one. That argument has aged well.

### The rest

- **Understanding team collapse (2024) — 18/30.** A probabilistic graphical model of team dynamics with learnable parameters, used to identify what causes a team to collapse and to state principles for resilient teams; validated in simulation and real-world experiments before the NBA application. Code is public. Novelty 7 — nothing else in this collection models collapse — but practicality 4, because the NBA half is diagnostic rather than a metric anyone ships.
- **Implicit Biases in Refereeing (2022) — 18/30.** Three bias types tested on the league's own **Last Two Minutes reports** (public, released for every game within 5 points in the final 2 minutes since 2015) plus play-by-play. Findings: home bias is real and playoff-amplified but shrank after the pandemic; specific players draw favourable calls beyond chance, though **no** negative bias toward individual players or teams; and no evidence of racial bias. Reproducibility 8 — the entire data set is public, which is rare for officiating work and makes this the most rebuildable referee paper in the collection.
- **tHoops (2017) — 18/30.** PARAFAC decomposition of an entity × court-location × time tensor into interpretable prototype spatio-temporal patterns, with a method for choosing the number of components; every team, player or possession is then a weighted mix of prototypes. The generalisation past shot-location-only comparison is the contribution. Runs on the public SportVU dump, hence 6 rather than 3.
- **The Anatomy of the Three-Point Shot (2016) — 18/30.** The tidiest result in the batch: shot attempts show a statistically significant **discontinuity** between the one-foot zones just inside and just outside the arc, while field goal percentage across those same zones is **statistically identical**. Shooters are behaving rationally; it is the line's placement that leaves the space just inside it unexploited. A fractal-inspired metric quantifies the unused dimensionality.
- **Footballonomics (2016) — 18/30.** The only peer-reviewed item in the batch (PLOS ONE, [10.1371/journal.pone.0168716](https://doi.org/10.1371/journal.pone.0168716)). Rejects the rational-coaching hypothesis on PAT and fourth-down decisions over 2009–2015, then shows a small logistic plus bootstrap reaches ~63% accuracy, comparable to far more complex systems and beating expert analysts 60% of the time. Reproducibility 8 (public `nflgame` pipeline, seasons named); novelty 5, since Romer had established fourth-down irrationality a decade earlier.
- **DeepHoops (2019) — 17/30.** The highest novelty in the batch (8): an end-to-end deep sequence model over tracking data emitting a running expected-points stream, framed as multi-class classification of the *terminal* action of a possession, with a parameterised downsampling scheme for the severe class imbalance. It values off-ball micro-actions — a screen, a backdoor cut — that no box score records. Reproducibility 4: the model is trained on proprietary NBA tracking, and only a realtime-application repo is public.
- **The Anatomy of Corner 3s (2021) — 16/30.** Lowest composite, best single fact: corner threes are efficient **because they are assisted over 90% of the time**, not because they are two feet shorter than an above-the-break three — explicitly contrary to the mass-media explanation. More than half involve a shooter anchored in the corner waiting for the kick-out. The offense/defense game they define has a Nash equilibrium of committing either to the corner shooter or to the drive, never splitting the difference — which is what the defenses in their data actually did. Reproducibility 3: Second Spectrum tracking throughout.

### Already in the collection — arXiv identifiers recorded, no second copy added

Scores held at their existing values; each was checked rather than assumed.

| Existing entry | arXiv | Existing score |
|---|---|---|
| LinNet: Probabilistic Lineup Evaluation Through Network Embedding | [1707.01855](https://arxiv.org/abs/1707.01855) | 6 / 5 / 6 = 17 |
| Going Deep: Continuous-Time Within-Play Valuation … American Football | [1906.01760](https://arxiv.org/abs/1906.01760) | 8 / 7 / 4 = 19 |
| A Naive Bayes Approach for NFL Passing Evaluation (= *next-gen-scraPy*) | [1906.03339](https://arxiv.org/abs/1906.03339) | 7 / 6 / 6 = 19 |
| The Hot Hand in Actual Game Situations | [2006.14609](https://arxiv.org/abs/2006.14609) | 5 / 3 / 4 = 12 |

The Hot Hand entry's `data = proprietary`, `R = 4` was re-checked against the arXiv text and is correct — SportVU and Second Spectrum optical tracking throughout.

**Note on reading this batch as a whole:** it is one researcher's output, so it is not a sample of the field. Its internal split is still informative — the papers built on **public data** (Last Two Minutes reports, `nflgame`, shot charts, the public SportVU dump) score 6–8 on reproducibility, and the two built on **contracted optical tracking** score 3 and 4, with no relationship to how good the underlying idea is. DeepHoops has the batch's highest novelty and its second-lowest composite for exactly this reason. That is the same pattern the collection-wide "proprietary-data trap" section documents, reproduced inside a single author's bibliography.

---

## The *Journal of Sports Analytics* batch (added 2026-09-02)

Nine SAGE-hosted links. **Seven are open access and were stored in full**; one is closed access and is held as a metadata stub only; one was already in the collection.

Every one of the seven carries the same provenance limitation as *WINSCORE revisited* above: **no PDF is held.** SAGE's version of record is Cloudflare-blocked from datacenter IPs and none of these has a preprint or repository copy, so the text came from the SAGE HTML version of record through the `r.jina.ai` reader proxy. Prose and tables are as published; **equations are lost** — MathJax does not survive text extraction — and figures and appendices are absent. Consult the publisher page before implementing any formula.

### Nuthin' But A G League: Estimating league translation factors — **23/30, the highest score of any 2026 addition**

Glazer, *JSA* 12 (Feb 2026), [10.1177/22150218261428808](https://doi.org/10.1177/22150218261428808), **CC BY**.

The causal counterpart to the hierarchical-Bayes translation paper above, and the first application of a causal-inference framework to league translation factors. The design in one line: **players who stayed in the G League for two consecutive seasons are the control group for players who went G League → NBA**, matched on age, position, usage rate and the prior-season value of the statistic being translated, then differenced twice.

- **Genetic matching** (`MatchIt`, `method = "genetic"`, `distance = "glm"`) with replacement, generalising propensity-score and Mahalanobis matching via an evolutionary search for balance. Balance is verified against the Rubin (2001) / Stuart (2010) criteria — standardised mean differences below 0.25, variance ratios below 2.
- **Rate statistics only, deliberately**, because the G League runs experimental rules (the Elam Ending, the one-free-throw rule) that would contaminate totals. Tip-Off Tournament games excluded for the same reason.
- The estimand is the **ATT** under parallel trends, and the paper is candid that with only one pre-treatment season a formal pre-trend test is infeasible; it substitutes covariate balance plus a check that pre-transition performance levels do not differ between treated and matched controls.

| Statistic | Same-season | Difference-in-differences |
|---|---:|---:|
| FG% | −3.6% (0.7%) | −2.9% (1.1%) |
| 3P% | −1.7% (1.1%) | −0.3% (2.1%) |
| eFG% | −3.0% (0.8%) | −2.0% (1.3%) |
| FT% | −2.3% (1.5%) | −1.2% (3.0%) |
| AST% | −5.1% (0.66%) | −3.3% (1.14%) |
| DRB% | −3.1% (0.43%) | −1.1% (0.96%) |
| TOV% | −1.5% (0.45%) | −1.3% (0.69%) |
| ORB% / STL% / BLK% | −0.3% / −0.4% / −0.3% | −0.2% / −0.3% / **+0.12%** |

Bootstrap standard errors in parentheses; 81–88 matched pairs, 2021–22 through 2023–24.

**The two findings that generalise beyond basketball.** First, **the DD estimates are consistently smaller in magnitude than the same-season estimates** — the naive comparison of players who appear in both leagues in one season overstates the league effect, because it absorbs within-season development and does not adjust for aging. Second, **the naive league-average and z-score approaches are not merely imprecise, they are directionally wrong**: NBA free-throw percentage exceeds the G League's because NBA players are better free-throw shooters, not because NBA rims are kinder, so a league-average adjustment gets the sign backwards. Glazer notes this differs from baseball, where some minor-league averages exceed the majors'.

The honest limitation is stated: the framework requires player overlap between the two leagues, and extending it to league pairs with little or no overlap "would require additional methodological development."

### A predictive metamodel for college football — 21/30

Coleman, *JSA* 11 (Jul 2025), [10.1177/22150218251365223](https://doi.org/10.1177/22150218251365223), CC BY-NC.

Only the third published attempt to identify the best *ensemble* of college football rating systems, after Fair & Oster (2007) and Coleman (2014). 29 systems, 5,925 games, 2016–24 with 2020 omitted; train/validate on 4,416 games (2016–22), test on 1,509 (2023–24).

Three methodological choices worth copying. **Predictors are projected victory margins, not rank differences** — which also folds in each system's own home-field treatment instead of a single global HFA dummy. **Selection is by cross-validated predicted SSE, not statistical significance**, via forward selection with six-fold season-wise holdout. And **coefficients are constrained non-negative**, sacrificing a little fit for a model that a non-specialist will trust.

The winning ensemble is five of the 29 — Dokter Entropy, Pi-Rate Bias, Keeper, ESPN FPI, Pigskin Index — with an in-sample R² of 0.451 and, notably, **none of the four systems that previous studies had selected**. Performance:

| | Validation (n=4,116) | Test (n=1,419) |
|---|---:|---:|
| Metamodel MAE | 12.6014 | **12.2572** |
| Opening line MAE | 12.5685 | 12.1663 |
| Closing line MAE | 12.4598 | 12.0550 |
| Metamodel accuracy | 74.59% | **74.14%** |
| Closing line accuracy | 74.78% | 73.93% |

So it does not beat the closing line on MAE, but it lands within a quarter-point of it and edges it on winner accuracy in the test years, and it is statistically significant in the presence of the opening line. **The opening-line comparison is the right one** and the paper argues why: ratings are built from information available immediately after the previous week, whereas the midweek and closing lines have absorbed everything since — including, plausibly, the published system predictions themselves.

### A causal approach for detecting team-level momentum in NBA games — 20/30

Weimer, Steinert-Threlkeld & Coltin, *JSA* 9 (2023), [10.3233/JSA-220592](https://doi.org/10.3233/JSA-220592), CC BY-NC.

A positive momentum result in a literature that mostly finds none, and it earns it with an identification strategy rather than a bigger model. **TV timeouts occur at fixed clock points, exogenous to the flow of play**, so they isolate the effect of a pause from the effect of a coach choosing to call one. Matched design, Poisson regression, dependent variable = points scored by the team on a run in the following three minutes.

| Run threshold | TV timeout coefficient | n |
|---|---:|---:|
| ≥ 6 points | −0.119\*\*\* (0.012) | 5,148 |
| ≥ 10 points | −0.123\*\*\* (0.036) | 576 |
| ≥ 15 points | −0.368\*\*\* (0.129) | **48** |

A TV timeout cuts the momentumed team's subsequent scoring by **11.2%**, roughly 50% more than an opposing substitution. Two controls do the interpretive work: the coefficient on run size is ~0 and insignificant, so **this is not mean reversion**; and the momentumed team substituting its own player costs ~16%, more than the timeout — which makes sense, since swapping a player means the team that had the momentum is no longer on the floor.

Read the ≥15 row with care: **n = 48**. The headline is the ≥6 row. The stated limitation is that timeouts permit non-substitution strategy changes (defensive assignments, a speech) that the design cannot observe, though the authors argue those should not be stronger during TV timeouts than during other stoppages, which form the control.

### mWAR: A Bayesian estimator of manager value — 20/30

Kahan, *JSA* 12 (May 2026), [10.1177/22150218261452597](https://doi.org/10.1177/22150218261452597), CC BY-NC. 80 references.

500+ managers across AL/NL seasons since 1901, with team performance measured against the record predicted by aggregate player WAR. The methodological discipline is the reason to read it, and it comes in two parts.

**A precondition test before any estimator is built.** Manager deviations from WAR-predicted records are compared against a *realistic simulated null* — how far teams would deviate with no manager decision-making at all. Only after clearing that does the paper proceed. The paper is explicit that this is the test Pythagorean-Expectation-based manager studies fail: they measure a residual and name it the manager without ever showing the residual is larger than chance.

**A decision rule instead of a point estimate.** A multilevel hierarchical model (team performance at level one, a manager-specific latent effect drawn from a population distribution at level two, MCMC) yields posteriors, and those are then read against a **region of practical equivalence** — here ±0.012 win probability, i.e. ±2 wins per 162 games. What gets reported per manager is the posterior mass outside the ROPE: the probability the manager's true value is practically consequential. Readers who prefer a different threshold can recompute it from the published posterior means and variances. The conclusion is that a substantial fraction of managers, current ones included, have moved winning percentage by ≥ ±0.012 over their careers.

### Predictions of european basketball match results with ML algorithms — 18/30

Lampis, Ntzoufras, Vassalos & Dimitriou, *JSA* 9 (2023), [10.3233/JSA-220639](https://doi.org/10.3233/JSA-220639), CC BY-NC.

A conventional bake-off — logistic regression, random forest, XGBoost, plus an ensemble — over 5,214 games from four European competitions (EuroLeague, EuroCup, Greek Basket League, Liga ACB), 2013–18, scored on Brier, accuracy and F1 across three scenarios (full season, mid-season, playoffs). The transferable part is not the algorithm ranking but the **feature construction**: Elo, PageRank and pi-rating features, with the rating-system parameters tuned per tournament on dedicated training data, and these lift the models materially over a team-name-only vanilla baseline.

The result worth remembering is where the lift *isn't*. The improvement is **smallest in the EuroLeague**, whose Brier-score gain is near zero, and **largest in the EuroCup**. The authors attribute this to competitive balance: the EuroLeague is uniformly top-class and therefore genuinely unpredictable, while the EuroCup mixes strong teams with teams not contesting the tournament seriously. Feature engineering buys the most in unbalanced leagues, which is a useful prior when deciding where to spend effort across a portfolio of competitions.

### Concurrent validity of computer-vision AI player tracking from broadcast footage — 15/30

Crang et al., *JSA* 12 (May 2026), [10.1177/22150218261445834](https://doi.org/10.1177/22150218261445834), **CC BY**.

Three commercial computer-vision providers measured against TRACAB Gen 5 multi-camera tracking on one match at the 2022 World Cup, across tactical, programme and camera-1 feeds at 720p and 1080p. Position RMSE **1.68 to 16.39 m**; speed RMSE **0.34 to 2.38 m·s⁻¹**; total distance mean bias **−1,745 m (−21.8%) to +1,945 m (+24.3%)**.

Low composite, high decision value. That distance-bias range spans 46 percentage points *between vendors on the same match*, which settles the question of whether broadcast-derived tracking is a commodity: it is not, and provider choice dominates. The practical guidance is concrete — **use a tactical feed**, which maximises player detection and therefore accuracy, and **resolution is not the constraint**: 720p and 1080p are both adequate given competent models. Reproducibility 3 because it is one match, the providers are anonymised, and the reference system is proprietary.

### How to assess leader capabilities: AI algorithms to evaluate NBA head coaches — 14/30, lowest of the batch

Kim & Lee, *JSA* 11 (Jul 2025), [10.1177/22150218251357538](https://doi.org/10.1177/22150218251357538), CC BY-NC.

24 seasons (1999–2023), 772 team-seasons. A model predicts each team's win differential from **prior-season** player statistics only, deliberately excluding coaching, and the gap between prediction and outcome is called the coach's marginal contribution. LightGBM is selected as the best of four learners.

The design is the standard coach-residual idea, and the problem is that **the residual is attributed to coaching by assumption**. Roster turnover, injuries, schedule, front-office moves and ordinary variance all live in the same gap, and the paper does not test the residual against a null. Put it directly beside mWAR above, which does exactly that test first and reports the null as a precondition — the two papers ask a near-identical question, and the difference in inferential care is the whole distance between 20/30 and 14/30. Two further notes: the reported margins run from −18 to +17 wins with a mean near zero, which is described as evidence of calibration but is equally consistent with a centred noise distribution; and **the abstract quotes LightGBM accuracy of 68.50% while Table 1 reports 67.25%** (with SVM tied at 67.25%), a discrepancy the extracted text does not reconcile.

### Closed access — metadata stub only

**Big data analytics for modeling scoring probability in basketball: The effect of shooting under high-pressure conditions.** Zuccolotto, Manisera & Sandri, *International Journal of Sports Science & Coaching* 13 (2017), [10.1177/1747954117737492](https://doi.org/10.1177/1747954117737492).

Alone in this batch, Crossref lists **no Creative Commons licence** for this paper. Per the repo's rule against committing licensed files, only the publisher abstract and bibliographic record are stored, at `md/library/journals/International Journal of Sports Science and Coaching/2017/…METADATA ONLY.md`. **Its 6/5/4 = 15 was assigned from the abstract alone** — the same lower-confidence class as the 8 scanned/slide-only PDFs noted in the Method section, and flagged as such in the CSV. The same group's *Measuring Sport Performances Under Pressure by Classification Trees* (composite 17) is already in the collection and covers the same programme without a subscription.

### Already in the collection

| Existing entry | DOI | Existing score |
|---|---|---|
| Beyond runs expectancy — Jim Albert | [10.3233/JSA-140001](https://doi.org/10.3233/JSA-140001) | 6 / 6 / 7 = 19 |

Also closed access (no CC licence), and already held as a PDF from before this batch.

### What the batch says as a set

Two pairs of papers in this batch ask the same question with different rigour, and the ranking gap between each pair is entirely about inferential discipline rather than data or technique. **Glazer (23) versus the naive league-average translation** she benchmarks against: same data, but a control group turns a directionally-wrong adjustment into a causal estimate. **mWAR (20) versus the NBA head-coach paper (14)**: both read a residual against a roster-based baseline, but one tests that residual against a simulated null before naming it, and one does not. If there is a single transferable lesson here, it is that in this literature **the control group and the null test are worth more than the model.**
