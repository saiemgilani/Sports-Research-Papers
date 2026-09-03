<!-- source: NO PDF HELD. SAGE's version of record is Cloudflare-blocked from datacenter IPs and this paper has no preprint or repository copy (OpenAlex: any_repository_has_fulltext = false). -->
<!-- text source: the SAGE HTML version of record, retrieved 2026-09-02 through the r.jina.ai reader proxy. Prose is verbatim from the VoR; TABLES are transcribed and EQUATIONS are RECONSTRUCTED BY HAND from mangled MathJax — verify any formula against the publisher PDF before implementing. Figures 1-7 and Appendices A (data) and B.1-B.5 (robustness) are NOT included in the HTML extraction. -->
<!-- doi: 10.1177/22150218261468843 · Journal of Sports Analytics 12 (SAGE, Jul 2026) · CC BY-NC 4.0 -->

# WINSCORE revisited: A model-based evaluation of player performance in the NBA and EuroLeague

**Gabriele Carta** (ORCID 0009-0004-9781-3258) · **Carlo A. Favero** (ORCID 0000-0002-1668-9426)
Bocconi University

*Journal of Sports Analytics*, vol. 12 (2026). DOI [10.1177/22150218261468843](https://doi.org/10.1177/22150218261468843). Open access, CC BY-NC 4.0.

## Abstract

In professional basketball, despite progress in Sport Analytics, widely used methods of player evaluation still rely on box-score statistics aggregated without formal justification for the weights used. The popular Performance Index Rating (PIR) is a prominent example. This paper revisits WINSCORE, a possession-based player evaluation methodology, and reinterprets it within a structural, model-based framework that links individual statistics to team outcomes through the efficient management of possessions. In this framework, the weights assigned to player statistics are derived endogenously from the data, providing a coherent foundation for measuring performance. Using NBA and EuroLeague data, we evaluate the model at the team level through goodness-of-fit evidence, residual analysis, encompassing tests against PIR, and comparisons with alternative advanced measures, including Four Factors and adjusted box-score plus-minus indicators. The results show that the model accounts well for variation in team performance, displays no major residual patterns, and adds explanatory content beyond existing metrics. We then extend WINSCORE to construct player performance measures for season-level and single-game analysis. These measures incorporate opponent adjustments and address playing-time endogeneity. The resulting indicators provide transparent tools for player assessment, coaching, and tactical analysis, with a measurement-oriented rather than causal interpretation.

## 1. Introduction

The question "How good is this player, really?" is central to basketball and, more generally, to all sports. Despite the progress made in Sport Analytics, the most popular methods of player evaluation still rely on box-score statistics **aggregated without a formal justification for the weights used and without a clear theoretical link to team performance**. The Performance Index Rating (PIR), widely used in leagues such as the NBA and the EuroLeague, is a prominent example.

This paper revisits the WINSCORE methodology, originally proposed by Berri et al. (2006), and reinterprets it within a structural, model-based framework that explicitly links individual statistics to team outcomes through the efficient management of possessions. This reinterpretation allows the weights assigned to player statistics to be **derived endogenously from the data, rather than imposed a priori**.

**Scope, stated explicitly.** "The purpose of the paper is not to evaluate whether a box-score-based structural model can outperform modern deep-learning, player-tracking, or spatio-temporal analytics frameworks… Our objective is instead to ask whether the same information set used by widely adopted box-score indexes such as PIR can be organized within a transparent model-based framework that links individual statistics to team outcomes." Tracking and ML methods are treated as **complementary, not competitors**.

A model separates data into **structure** and **noise**. The structure captures the essential features of the data-generating process that are independent of the observed sample; noise reflects accidental features specific to a given sample and should not be fitted when the objective is prediction or out-of-sample analysis. The authors impose a common functional specification across leagues while allowing the parameters to vary, to capture league-specific features (NBA vs. EuroLeague).

Two main empirical findings are claimed. First, the model provides an excellent fit to team performance and, **through encompassing tests, dominates PIR** and other widely used advanced box-score metrics in explaining variation in wins. Second, a validation strategy exploiting variation across **both eras and leagues** — the historical NBA sample studied by Berri et al. (2006) versus a recent post-COVID NBA sample, and NBA versus EuroLeague — shows the estimated relationship and the simulated weights to be stable. "We interpret this evidence as a test of empirical robustness within the available data, **not as a claim of universal structural invariance.**"

## 2. Related Literature

The literature is divided into three strands:

1. **Aggregation-based metrics** — PIR being the most widely used. Simple and widely adopted, but lacking a theoretical foundation linking individual actions to team outcomes.
2. **Regression-based / plus-minus approaches** — Rosenbaum (2004) introduced adjusted plus-minus; Ilardi and Barzilai (2008) incorporated box-score information; Kubatko et al. (2007) provide a systematic regression framework; Sill (2010) proposes regularization. The most modern applications cited are Iatropoulos et al. (2025) and **Petridis and Pelechrinis (2026)**.
3. **Theory-based structural models** — Hollinger (2002) and Oliver (2004) established possessions as the fundamental unit; Berri and Eschker (2005) and Berri et al. (2006) developed WINSCORE. "This framework provides a more direct connection between individual actions and team success, but its interpretation has remained largely **operational rather than explicitly model-based**."

On **L-RAPM** specifically: "Petridis and Pelechrinis (2026) propose Lineup-Regularized Adjusted Plus-Minus (L-RAPM). L-RAPM estimates lineup quality, rather than individual player quality, by regressing points per possession on the offensive and defensive lineups involved in each possession. To address the sparsity and noise of lineup data, it regularizes lineup estimates toward informed priors built from individual player RAPM ratings."

**Why no ML benchmark.** "A different empirical exercise would be to benchmark WINSCORE against fully predictive machine-learning models trained on box-score statistics. Such a comparison would require specifying a prediction target, training-validation-test splits, tuning rules, and loss functions. We do not pursue this route because the purpose of the paper is not to optimize predictive accuracy with a flexible learner, but to construct a transparent and interpretable measurement framework."

## 3. Wins and Box-Score Statistics: Data Analysis Without a Theory

Available box-score statistics: FG, FGA, 3P, 3PA, FT, FTA, ORB, DRB, AST, STL, BLK, TOV, PF (and **FD, fouls drawn**, which the EuroLeague additionally publishes).

### 3.1 The PIR approach

$$\text{PIR} = \text{PTS} + \text{REB} + \text{AST} + \text{STL} + \text{BLK} + \text{FD} - \text{FGMISS} - \text{FTMISS} - \text{TOV} - \text{PF}$$

Developed by the Spanish ACB League in 1991 and adopted by the EuroLeague, where it determines weekly MVPs; agents refer to it in contract negotiations (Wen et al. 2023).

The stated objections: PIR assigns **unjustified equal weights** — "a missed free throw, which costs the team one point, and a missed field goal, which may cost the team either two or three points, are treated equally despite their different opportunity costs." Rebounds, assists, steals and blocks all enter with unitary weight. And PIR **does not account for opponent performance or for the outcome of the game.**

### 3.2 Can measurement without theory help?

Two problems with naive correlation between win percentage and box-score statistics:

- **Sign reversal from confounding.** "Offensive rebounds exhibit a **negative** correlation with the percentage of wins… This is because offensive rebounds are highly correlated with missed field goals, which are themselves negatively associated with winning. Thus, offensive rebounds may partly act as a proxy for poor shooting rather than being intrinsically detrimental."
- **Collinearity.** With strongly correlated regressors, coefficients "may become unstable, sample-dependent, and difficult to interpret as structural weights."

But the correlation patterns are strikingly **stable** across the 2021–25 NBA sample, the 1992–2005 NBA sample, and the 2022–25 EuroLeague sample (Figures 1–3), suggesting a stable underlying data-generating process.

The conclusion drawn is a fork: "high-dimensional and highly correlated box-score data cannot be weighted reliably by unrestricted regression alone: **either theory or regularization is needed** to discipline the parameterization."

## 4. Reinterpreting WINSCORE as a Model-Based Framework

The model-based approach unfolds as **specification → estimation/calibration → validation → simulation**.

### 4.1 Specification and estimation

A possession starts when one team gains control of the ball and ends when that team gives it up (an offensive rebound starts a new *play*, not a new possession). Possessions split into **Employed Possessions (EP)** and **Acquired Possessions (AP)**:

$$EP_{i,t} = FGA_{i,t} + 0.45 \cdot FTA_{i,t} + TOV_{i,t} - ORB_{i,t}$$
$$AP_{i,t} = OTOV_{i,t} + DRB_{i,t} + TEAMR_{i,t} + OFG_{i,t} + 0.45 \cdot OFT_{i,t}$$
$$EP_{i,t} \approx AP_{i,t}$$

The near-equality "**is not a behavioral assumption. It is a possession-accounting restriction implied by the rules of basketball**"; discrepancies come from end-of-period possessions and the conventional box-score reconstruction formula, and average out at the season level (Appendix B.1). Team rebounds `TEAMR` are not in the box score but **are reconstructed by exploiting EP ≈ AP**.

The stochastic equation (the only one of the seven with unknown parameters):

$$W_{i,t} = \beta_0 + \beta_1\left(\frac{PTS_{i,t}}{EP_{i,t}} - \frac{PTSA_{i,t}}{AP_{i,t}}\right) + u_{i,t}, \qquad u_{i,t}\sim N.I.D(0,\sigma^2) \tag{1}$$

with `PTS = 1·FT + 2·2PFG + 3·3PFG` and the opponent analogue. β₀ captures the average team's season performance (expected ≈ *n*/2) and β₁ the impact of the efficiency differential.

**Why this beats an unrestricted regression:** the statistics are combined through theoretically motivated **nonlinear** transformations into two efficiency ratios, reducing the problem to two parameters. "The contribution of a made three-point shot is not simply a fixed marginal coefficient on 3PFG. It depends on its joint effect on **both points scored and possessions employed**." Hence variance-inflation diagnostics are not the relevant check — the collinear statistics never get separate free coefficients.

**Table 1 — Wins and efficiency in the NBA and the EuroLeague**

| | NBA 1994–2005 | NBA 2021–2024 | EuroLeague 2022–25 |
|---|---:|---:|---:|
| *(a) Dependent variable: Wins* | | | |
| Intercept | 41.00\*\*\* (0.17) | 41.00\*\*\* (0.33) | 17.00\*\*\* (0.26) |
| Efficiency differential | 257.16\*\*\* (3.40) | 237.38\*\*\* (7.11) | 78.46\*\*\* (4.34) |
| *(b) Dependent variable: Win %* | | | |
| Intercept | 0.50\*\*\* (0.002) | 0.50\*\*\* (0.007) | 0.50\*\*\* (0.04) |
| Efficiency differential | 3.13\*\*\* (0.041) | 2.89\*\*\* (0.086) | 2.30\*\*\* (0.127) |
| Observations | 316 | 90 | 54 |
| R² / Adj. R² | 0.95 / 0.95 | 0.93 / 0.93 | 0.86 / 0.86 |
| F | 5718\*\*\* | 1115\*\*\* | 326.2\*\*\* |

\*\*\* *p* < 0.001. NBA seasons are 82 games, EuroLeague 34, hence both scalings.

The EuroLeague slope is significantly smaller (Chow-type test, Appendix B.2), explained by the **higher variance of the efficiency measure** in the EuroLeague — read as a signal of **higher competitive balance in the NBA** (Zimbalist 2002). "Interestingly, the average points scored per possession are higher in the EuroLeague than in the NBA, **debunking the myth that European basketball features better defenses**."

### 4.2 Validation

The strategy is **cross-sample and cross-league rather than algorithmic cross-validation** — deliberately, because the objective is not to optimize a forecasting algorithm over random folds.

**Table 2 — Wins on the PIR factor** (PIR<sub>it</sub> − OPIR<sub>it</sub>): intercepts 41.00/41.00/17.00; PIR-factor coefficients 0.016/0.014/0.011 (all \*\*\*); R² **0.91 / 0.91 / 0.76** — versus WINSCORE's 0.95 / 0.93 / 0.86.

**Table 3 — Residual diagnostics** (win-percentage regressions)

| Sample | Model | SD | RMSE | MAE | JB *p* |
|---|---|---:|---:|---:|---:|
| NBA 1994–2005 (excl. 1999) | Winscore | 0.0366 | 0.0365 | 0.0291 | 0.8157 |
| | PIR | 0.0478 | 0.0477 | 0.0390 | **0.0352** |
| NBA 2022–2025 | Winscore | 0.0366 | 0.0364 | 0.0287 | 0.6731 |
| | PIR | 0.0402 | 0.0400 | 0.0332 | 0.4865 |
| EuroLeague 2022–2025 | Winscore | 0.0546 | 0.0541 | 0.0443 | 0.5150 |
| | PIR | 0.0716 | 0.0710 | 0.0576 | 0.7972 |

Winscore residuals are lower-dispersion in all three samples, and Jarque–Bera does not reject normality for Winscore anywhere (it does reject for PIR on the 1994–2005 sample).

**Encompassing test** (Mizon and Richard 1986): regress actual wins on the two models' fitted values,

$$W_{i,t} = \delta_1 \hat{W}^{WS}_{i,t} + \delta_2 \hat{W}^{PIR}_{i,t} + \epsilon_{i,t} \tag{3}$$

**Table 4 — Encompassing regressions**

| | NBA (Berri) | NBA 2021–2024 | EuroLeague 2022–25 |
|---|---:|---:|---:|
| Pred. WINSCORE | 0.92\*\*\* (0.06) | 0.77\*\*\* (0.17) | 1.08\*\*\* (0.18) |
| Pred. PIR | 0.08 (0.06) | 0.23 (0.17) | −0.08 (0.18) |
| R² | 0.9952 | 0.9947 | 0.9892 |

"For all data-sets considered, the coefficient on the WINSCORE prediction is positive, statistically different from zero and **not statistically different from one**, whereas the coefficient associated with the PIR prediction is **always not statistically different from zero**. Moreover, the joint hypothesis δ₁ = 1, δ₂ = 0 is never rejected."

Appendix B.4 repeats the exercise against **Four Factors** (Oliver 2004) and **adjusted box-score plus-minus measures — OBPM, DBPM, BPM, VORP** — with the same pattern: WINSCORE fitted values stay significant, the alternatives "generally do not add explanatory power." Tracking-data, lineup-based and spatio-temporal models are excluded as complementary rather than competing.

### 4.3 Simulation → the weights

Weights are attributed by simulation, not estimated as coefficients: predict wins with all statistics at their averages (baseline), then predict again moving one statistic, and take the difference. "The model-based procedure takes **all feedbacks** into account: one more three-point shot made gives the team three points more **at the cost of employing a possession**." Point estimates come from deterministic simulation; the distribution of the impact is available via stochastic simulation drawing (β₀, β₁) from their asymptotic distribution.

**Table 5 — The value of statistics in terms of wins**

| Statistic | EuroLeague | NBA 2021–2024 | NBA (Berri et al. 2006) |
|---|---:|---:|---:|
| **Scoring** | | | |
| Three-point field goals made | +0.059 | +0.054 | +0.066 |
| Opponent's three-point field goals made | −0.059 | −0.054 | −0.066 |
| Two-point field goals made | +0.027 | +0.025 | +0.033 |
| Opponent's two-point field goals made | −0.027 | −0.025 | −0.033 |
| Free throws made | +0.016 | +0.015 | +0.018 |
| Opponent's free throws made | −0.016 | −0.014 | −0.018 |
| Missed field goals | −0.036 | −0.032 | −0.034 |
| Missed free throws | −0.016 | −0.014 | −0.015 |
| **Possession** | | | |
| Offensive rebounds | +0.036 | +0.032 | +0.034 |
| Turnovers | −0.036 | −0.032 | −0.034 |
| Defensive rebounds | +0.036 | +0.032 | +0.034 |
| Team rebounds | +0.036 | +0.032 | +0.034 |
| Opponent's turnovers | +0.036 | +0.032 | +0.034 |
| Steals | +0.036 | +0.032 | +0.034 |
| **Fouls, blocks, assists** | | | |
| Personal fouls | −0.016 | −0.014 | −0.018 |
| Blocked shots | +0.017 | +0.015 | +0.021 |
| Assists | +0.018 | +0.020 | +0.022 |

Every possession-changing event carries **the same weight** (+0.036 EuroLeague / +0.032 NBA) — that is the model's central structural claim, and it is exactly what PIR's unit weights get wrong.

**On the statistics the model does not contain.** Assists, personal fouls and blocked shots "do not directly create, consume, or transfer possessions" and so do not enter the structural model. Their implied values are recovered through auxiliary regressions; Appendix B.5 shows that augmenting the model with them yields coefficients **not statistically different from zero**, i.e. conditional on the WINSCORE variables they add nothing independent. "Their value is therefore not omitted from the model, but is already reflected in the included possession-based statistics."

### 4.4 The linearized interpretation

$$W^{WS}_{i,t} = \frac{n}{2} + WINSEFF_{i,t} - OWINSEFF_{i,t} \tag{4}$$
$$WINSEFF_{i,t} = SCSTAT_{i,t} + POSSTAT_{i,t} + PFBLKA_{i,t}$$
$$SCSTAT_{i,t} = 3PFG\cdot w_{3P} + 2PFG\cdot w_{2P} + FT\cdot w_{FT} + (FGA - 3PFG - 2PFG)\cdot w_{FGM} + (FTA - FT)\cdot w_{FTM}$$
$$POSSTAT_{i,t} = w_{POS}\,(ORB + DRB + STL - TOV)$$
$$PFBLKA_{i,t} = w_{BLK}\cdot BLK + w_{PF}\cdot(PF - FD) + w_{A}\cdot A$$

with the opponent analogues, and the *w*'s taken from Table 5.

## 5. From Team to Players: Season Data

The Berri-type player measure aggregates a player's WINSEFF, benchmarks it against an average player in the same role, and anchors it to the wins an average team produces over the same court time:

$$WINSCORE^{B}_{j} = WINSEFF_j - OWINSEFF^{adj,B}_{j} + \frac{MIN_j}{TOTMIN_j}\cdot\frac{0.5\cdot G}{5} \tag{5}$$
$$OWINSEFF^{adj,B}_{j} = \left(\frac{1}{N_{\text{role}(j)}}\sum_{k\in\text{role}(j)} WINSEFF_k \cdot \frac{TOTMIN_k}{MIN_k}\right)\cdot\frac{MIN_j}{TOTMIN_j} \tag{6}$$

and if internally consistent, Σ<sub>j</sub> WINSCORE<sup>B</sup><sub>j,i</sub> ≈ team wins<sub>i</sub>. (7)

### The playing-time problem — the paper's sharpest practical contribution

"Playing time is **not randomly assigned**. It is the outcome of coaching decisions, roster constraints, injuries, tactical choices, and assessments of player ability. As a result, players with very low minutes are typically a selected group, and projecting their observed performance to full-season minutes can generate extreme values."

"The problem is particularly severe because **the projection factor is mechanically large when MIN<sub>j</sub> is small.** For example, a player who plays only one minute and makes a three-point shot would be projected to an implausibly high full-game or full-season scoring rate… **This is not simply a problem of noisy observations. It is a selection problem** induced by the interaction between limited playing time and full-season extrapolation. Low-minute players are precisely those for whom observed statistics are least informative about season-long productivity, **yet the standard projection assigns them the largest scaling factors.** Consequently, a small number of edge cases can distort the role-level benchmark and, through it, the relative contribution assigned to **all other players in the same role**."

**Table 6 — Edge cases, 2024–25 EuroLeague projected WINSEFF**

*(a) Average projected WINSEFF by role*

| Role | With edge cases | Excluding edge cases |
|---|---:|---:|
| Guard | **−0.506** | **0.039** |
| Forward | 5.136 | 5.131 |
| Center | 8.744 | 8.951 |

*(b) Best full-season projected player by role*

| Role | Player | Team | Minutes | Projected WINSEFF |
|---|---|---|---:|---:|
| Guard | Weiler-Babb, Nick | MUN | 841.7 | 7.03 |
| Forward | Vezenkov, Sasha | OLY | 973.0 | 14.46 |
| Center | Tavares, Walter | MAD | 812.1 | 15.10 |

*(c) Low-minute projection edge cases (≤ 100 minutes)*

| Role | Player | Team | Minutes | Projected WINSEFF |
|---|---|---|---:|---:|
| Center | Koumadje, Khalifa | BER | 96.8 | 18.254 |
| Forward | Yilmaz, Erkan | IST | 20.0 | 17.665 |
| Center | Yebo, Kevin | MUN | 99.5 | 4.290 |
| Guard | Wong, Isaiah | ZAL | 85.9 | 2.708 |
| Guard | Laprovittola, Nicolas | BAR | 88.1 | 0.957 |
| Forward | Begarin, Juhann | MCO | 42.6 | −6.829 |
| Center | Pleiss, Tibor | PAN | 33.3 | −8.912 |
| Guard | Smith Jr, Dennis | MAD | 20.7 | −12.579 |
| Guard | Wallace, Tyrone | ZAL | 22.4 | −16.064 |
| Guard | Querejeta, Joseba | BAS | 5.3 | **−38.598** |

A 5.3-minute player projects to −38.6, and two ≤ 100-minute players out-project the best full-season player at their position. The **guard** average flips sign entirely once those cases are removed.

### The proposed correction: a playing-time caliper

Rejecting an arbitrary minimum-minutes threshold ("the choice of the threshold is arbitrary and may discard useful information"), the benchmark for player *j* is built **only from players in the same role whose minutes lie within a ±10% window around MIN<sub>j</sub>**:

$$WINSCORE^{M}_{j} = WINSEFF_j - OWINSEFF^{adj,M}_{j} + \frac{MIN_j}{TOTMIN_j}\cdot\frac{0.5\cdot G}{5} \tag{8}$$
$$OWINSEFF^{adj,M}_{j} = \frac{1}{N^{\Delta}_{j}}\sum_{\substack{k\in\text{role}(j)\\ MIN_k\in[0.9\,MIN_j,\ 1.1\,MIN_j]}} WINSEFF_k \tag{9}$$

"The correction can be interpreted as a **role-specific matching procedure based on a playing-time caliper**… analogous to a caliper-matching rule in which players are matched on the observable determinants of their opportunity to contribute, namely role and realized court time." The authors are careful: it "does not claim to fully eliminate the endogeneity of playing time, nor does it identify a causal effect."

**Table 7 — Model predictions vs. actual wins, 2024–25 EuroLeague**

| Team | Wins | WS | Lin. WS | Σ WINSCORE<sup>B</sup> | Σ WINSCORE<sup>M</sup> |
|---|---:|---:|---:|---:|---:|
| ASV | 13 | 12.5 | 13.5 | 18.2 | 13.0 |
| BAR | 20 | 21.2 | 20.1 | 27.2 | 22.8 |
| BAS | 14 | 15.0 | 20.1 | 19.7 | 20.5 |
| BER | 5 | 3.6 | 0.5 | 15.5 | −1.6 |
| IST | 20 | 22.5 | 27.0 | 32.7 | 24.7 |
| MAD | 20 | 19.6 | 27.6 | 20.1 | 18.7 |
| MCO | 21 | 21.1 | 15.3 | 25.5 | 18.4 |
| MIL | 17 | 16.2 | 18.3 | 30.5 | 19.8 |
| MUN | 19 | 15.8 | 16.0 | 25.6 | 18.6 |
| OLY | 24 | 22.0 | 22.4 | 30.3 | 24.6 |
| PAN | 22 | 22.7 | 25.4 | 34.3 | 23.3 |
| PAR | 16 | 18.5 | 12.5 | 22.0 | 20.2 |
| PRS | 19 | 17.5 | 9.6 | 24.4 | 19.7 |
| RED | 18 | 18.2 | 15.3 | 22.0 | 13.3 |
| TEL | 11 | 13.8 | 15.4 | 28.0 | 15.7 |
| ULK | 23 | 19.4 | 23.6 | 23.6 | 13.4 |
| VIR | 9 | 11.3 | 8.6 | 20.9 | 13.2 |
| ZAL | 15 | 14.7 | 14.8 | 17.0 | 9.1 |

The Berri-type aggregation **systematically over-predicts** — BER's 5 actual wins become 15.5, TEL's 11 become 28.0 — because the role benchmark is contaminated by extrapolated low-minute players. The caliper version tracks actual wins far more closely. **The aggregation identity (7) is the diagnostic that exposes the bias.**

## 6. From Team to Players: Single-Game Data

With single-game data, players can be matched **precisely** with opponents rather than compared to a role average. The procedure:

1. Group players by role — **Back-Court (BC) / Front-Court (FC)**, reclassified from the game itself rather than official position, because "in a single game, due to injuries or tactical adjustments, coaches may assign players to roles different from their official designation" (season-long misassignment averages out; single-game misassignment does not).
2. Rank players by time on court within role.
3. Match each player with the same-rank opponent in the same role, equalizing court time.
4. Compute the average player's contribution over that same court time.

$$WINSCORE^{r}_{j,1} = WINSEFF^{r}_{j,1} - WINSEFF^{r}_{j,2}\left(\frac{MIN^{r}_{j,1}}{MIN^{r}_{j,2}}\right) + \frac{MIN^{r}_{j,1}}{TOTMIN^{r}_{j,1}}\cdot\frac{0.5}{5} \tag{10}$$

**Table 8 — EuroLeague, April 2025: Barcelona 91 – Virtus Bologna 87**

*(a) Barcelona*

| Player | Seconds | Role | Opponent | Opp. sec | WINSCORE | PIR | Points |
|---|---:|---|---|---:|---:|---:|---:|
| SATORANSKY | 1756 | BC | CORDINIER | 1522 | 0.303 | 19 | 11 |
| PUNTER | 1744 | BC | CLYBURN | 1409 | 0.189 | 22 | 20 |
| ANDERSON | 1489 | BC | HOLIDAY | 1254 | −0.123 | 12 | 12 |
| BRIZUELA | 1278 | BC | MORGAN | 1228 | 0.268 | 10 | 10 |
| ABRINES | 358 | BC | HACKETT | 925 | 0.042 | 0 | 0 |
| ABRINES | 358 | BC | PAJOLA | 916 | 0.013 | 0 | 0 |
| PARKER | 1366 | FC | SHENGELIA | 1706 | 0.045 | 7 | 10 |
| PARRA | 1251 | FC | DIOUF | 909 | −0.143 | 13 | 10 |
| HERNANGOMEZ | 1114 | FC | ZIZIC | 894 | 0.072 | 12 | 9 |
| VESELY | 917 | FC | POLONARA | 755 | −0.052 | 13 | 9 |
| FALL | 369 | FC | AKELE | 482 | −0.072 | −2 | 0 |
| **Sum** | 12000 | | | 12000 | **0.541** | 106 | 91 |

*(b) Virtus Bologna*

| Player | Seconds | Role | Opponent | Opp. sec | WINSCORE | PIR | Points |
|---|---:|---|---|---:|---:|---:|---:|
| CORDINIER | 1522 | BC | SATORANSKY | 1756 | −0.136 | 10 | 11 |
| CLYBURN | 1409 | BC | PUNTER | 1744 | −0.035 | 13 | 15 |
| HOLIDAY | 1254 | BC | ANDERSON | 1489 | 0.208 | 16 | 16 |
| MORGAN | 1228 | BC | BRIZUELA | 1278 | −0.155 | −3 | 5 |
| HACKETT | 925 | BC | ABRINES | 358 | −0.032 | 0 | 0 |
| PAJOLA | 916 | BC | ABRINES | 358 | 0.044 | 3 | 0 |
| SHENGELIA | 1706 | FC | PARKER | 1366 | 0.086 | 12 | 17 |
| DIOUF | 909 | FC | PARRA | 1251 | 0.180 | 13 | 6 |
| ZIZIC | 894 | FC | HERNANGOMEZ | 1114 | 0.017 | 13 | 12 |
| POLONARA | 755 | FC | VESELY | 917 | 0.106 | 9 | 5 |
| AKELE | 482 | FC | FALL | 369 | 0.134 | 2 | 0 |
| **Sum** | 12000 | | | 12000 | **0.417** | 88 | 87 |

Barcelona had one fewer player than Virtus, so Abrines' 716 on-court seconds are **split into two half-Abrines of 358 seconds each**, with half his WINSCORE, to match both Hackett and Pajola.

The team totals — 0.541 vs 0.417 of an expected win — are read as the game's contribution to season wins; close values indicate a close game, and polarized values an unbalanced one.

"**Notably, PIR and WINSCORE are not correlated.** For instance, Parra has the lowest WINSCORE on Barcelona but the fourth-highest PIR. This is because Diouf outperformed Parra in their head-to-head comparison, and WINSCORE is computed relative to a relevant opponent and the average player. PIR, by contrast, is an absolute measure that does not account for opponent context." The analysis also shows Barcelona's back-court outperformed Virtus's while Virtus's front-court outperformed Barcelona's — a contrast PIR does not capture.

## 7. Conclusion

The encompassing tests show WINSCORE contains predictive information not fully summarized by PIR. Simulated weights are broadly stable across samples and leagues. The player-level extensions incorporate opponent adjustments and playing-time normalization; the **caliper-corrected aggregation is closer to team wins** than the standard adjustment, "suggesting that accounting for the selection of court time improves the descriptive reliability of individual efficiency estimates."

Explicit caveats: the findings "should not be read as evidence that the model captures all dimensions of player value," and the single-game case study "should be interpreted as an illustration rather than as definitive validation."

## 8. Stated Future Work

- **Scalability / real-time.** Extend the same logic to rolling game windows, **lineup stints, or possession-level updates**, to monitor contributions dynamically during a season or a game.
- **Causal inference.** The measures are descriptive. A causal extension would need plausibly exogenous variation in player availability or lineup composition — lineup-based panel models with player/team/opponent/game fixed effects, quasi-experimental variation from injuries, suspensions, staggered rest or substitution patterns, or possession/stint-level before-and-after comparisons controlling for score margin, opponent strength, lineup composition and game state.
- **External validity.** Other European leagues, domestic cups, international competitions, and **women's basketball** — "would provide further evidence on the stability of the estimated weights."

## Practical implications (author's framing)

The framework supports player comparison, roster construction, rotation analysis and contract evaluation **especially when richer tracking data are not available**. Players should be assessed relative to competitive context, since "the same statistical line may have different value depending on the opponent, role, minutes played, and team environment" — relevant for scouting and game preparation. The single-game implementation decomposes value across role groups for post-game analysis. It "should therefore be viewed not as a replacement for expert judgment or richer tactical analysis, but as an interpretable quantitative benchmark that can complement them."

## Data, code and declarations

- **Data sources (footnote 3):** EuroLeague statistics from <https://www.euroleaguebasketball.net/en/euroleague/> (real-time and historical, standard and advanced, for competitions, teams and players); NBA statistics from <https://www.basketball-reference.com/>. A Data appendix describes the data in detail.
- **Replication (footnote 2):** "The replication package nevertheless provides the full data-retrieval and estimation pipeline in **R**." *No URL for this package appears in the HTML version of record as extracted; check the publisher's supplementary material.*
- **Conflicting interest:** none declared. **Funding:** none received.

## Selected references

Berri DJ and Eschker E (2005) · Berri DJ, Schmidt MB and Brook SL (2006), *The Wages of Wins* · Cervone D et al. (2014) · Cooley T (1997) · Favero CA (2001) · Hollinger J (2002) · Iatropoulos et al. (2025) · Ilardi S and Barzilai A (2008) · James G et al. (2013) · Kubatko J et al. (2007) · Lakhloufi (2025) · Mizon GE and Richard J-F (1986) · Oliver D (2004), *Basketball on Paper* · Page SE (2018), *The Model Thinker* · **Petridis C and Pelechrinis K (2026), Lineup-Regularized Adjusted Plus-Minus (L-RAPM)** · Rosenbaum D (2004) · Sarlis (2024) · Sill J (2010) · Terner Z and Franks A (2021) · Wen et al. (2023) · Zhou and Li (2024) · Zimbalist A (2002)
