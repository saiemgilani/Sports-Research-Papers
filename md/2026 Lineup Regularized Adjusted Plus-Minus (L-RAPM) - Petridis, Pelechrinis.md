<!-- source: 2026 Lineup Regularized Adjusted Plus-Minus (L-RAPM) - Petridis, Pelechrinis.pdf -->
<!-- arXiv:2601.15000v1 [cs.LG], 21 Jan 2026 · text extracted from the arXiv PDF (open access) -->
<!-- cited as forthcoming ("Petridis and Pelechrinis, 2026") in Carta & Favero, J. Sports Analytics 12 -->

# Lineup Regularized Adjusted Plus-Minus (L-RAPM): Basketball Lineup Ratings with Informed Priors

**Christos Petridis** — Department of Computer and Information Sciences, Temple University, Philadelphia, United States · `christos.petridis@temple.edu`
**Konstantinos Pelechrinis** — Department of Informatics and Networked Systems, University of Pittsburgh, Pittsburgh, United States · `kpele@pitt.edu`

arXiv:[2601.15000v1](https://arxiv.org/abs/2601.15000) \[cs.LG], 21 January 2026.

## Abstract

Identifying combinations of players (that is, lineups) in basketball — and other sports — that perform well when they play together is one of the most important tasks in sports analytics. One of the main challenges associated with this task is the frequent substitutions that occur during a game, which results in highly sparse data. In particular, a National Basketball Association (NBA) team will use more than 600 lineups during a season, which translates to an average lineup having seen the court in approximately 25–30 possessions. Inevitably, any statistics that one collects for these lineups are going to be noisy, with low predictive value. Yet, there is no existing work (in the public at least) that addresses this problem. In this work, we propose a regression-based approach that controls for the opposition faced by each lineup, while it also utilizes information about the players making up the lineups. Our experiments show that L-RAPM provides improved predictive power than the currently used baseline, and this improvement increases as the sample size for the lineups gets smaller.

## 1. Introduction

Given an opponent's lineup λ<sub>O</sub> and a set Λ of possible lineups that our team can play, by how many points do we expect each lineup λ ∈ Λ to outperform λ<sub>O</sub>? This is the core question we are trying to answer in this study by developing L-RAPM, a regression-based model. Although this is one of the most important tasks for the coaches and analytics departments of teams, there is very little public work that allows someone to answer this question to a satisfactory degree.

A lineup is typically evaluated through its offensive, defensive and net rating — the number of points it scores per 100 possessions (offensive rating), the number of points allowed per 100 possessions (defensive rating), and the difference between these two (net rating). **These ratings are the only publicly available metrics for evaluating lineups and they are usually taken at face value when it comes to projecting future lineup performance.**

While these raw ratings capture how a lineup has performed so far, they suffer from small — sometimes tiny — sample sizes, thus limiting their predictive power. Using data from the 2023–24 NBA season, Figure 1 shows the distribution of the number of total possessions (both offense and defense) that each lineup played during the season, in log-log scale since the distribution is right-skewed: the vast majority of lineups are on the court for very few possessions, while a small number have played thousands. **An average lineup plays approximately 17 possessions on offense and 17 on defense, with a standard deviation of 56 possessions.**

The worked example the paper gives for why this matters:

> Consider lineup λ<sub>a</sub>, that has played 10 offensive possessions and has scored 13 points. Its raw offensive rating is 113.0. If, in one of the 10 possessions during which the lineup was on the court, a made three-point shot had instead resulted in a miss (which, on average, occurs 64% of the time), the raw offensive rating of λ<sub>a</sub> would have been 100.0. **The difference between offensive ratings of 113.0 and 100.0 is of the same magnitude as the difference between the offensive rating of the best and worst offensive teams in the league.**

An additional limitation of using these raw ratings is that they do not take into account the strength of opposition faced. Two lineups λ<sub>a</sub> and λ<sub>b</sub> with identical raw ratings are not of the same quality if λ<sub>a</sub> played all of its possessions against the best players of the opposing teams while λ<sub>b</sub> mainly played during the end of games that were already decided, against "end-of-bench" players.

L-RAPM addresses both challenges: it **controls for the opposition faced** by a lineup through the regression covariates, and **uses a prior for each lineup** — informed by individual player ratings and incorporated through regularization — to overcome the small-sample problem. For lineups that have played several hundred possessions, raw ratings do almost as well; **as the lineups get thinner — under 50 possessions, or never observed at all — the benefit from L-RAPM increases.**

## 2. Related Studies

While there is a significant volume of research on evaluating players and decomposing their impact from that of their teammates, there is little public work on the opposite direction: given a lineup, project its performance.

**Player ratings.** The current gold standard is a plethora of metrics based on adjusted plus-minus (APM) (Winston et al. 2022; Rosenbaum 2004). A player's APM is calculated through a regression model where each data point is a possession and the dependent variable is the points scored during the possession. Independent variables correspond to players, each associated with two binary variables — offense (x<sub>i,off</sub>) and defense (x<sub>i,def</sub>). Solving this regression divides credit among players for team performance, adjusting for who else was on the court.

One of the problems of early APM versions is that they were mainly **descriptive** metrics, capturing what has happened until that moment, with little predictive power. Sill (2010) introduced the regularized version (RAPM), which has more predictive power. While Sill shrank the coefficients **to 0**, other models (ESPN's RPM, 538's RAPTOR, etc.) use **a different prior value for each coefficient** to shrink to, based on box-score statistics and other factors (Winston et al. 2022; Deshpande and Jensen 2016). This study uses Sill (2010)'s RAPM for player ratings, **since most of the metrics that use some type of box-score prior are proprietary.**

**Lineup evaluation.** The most prevalent approach is the raw offensive, defensive, and net rating available from the league website. A basic adjustment exists (Winston et al. 2022): subtract the average player ratings of the opponents faced. For example, if λ<sub>a</sub> has a raw defensive rating of 113.2 and the average offensive rating of the players faced is +0.26 per 100 possessions, adjust to 113.2 − (5 × 0.26) = 111.9. While an improvement over raw ratings, it still suffers from small sample sizes and extreme outliers.

A network embedding approach was introduced by Pelechrinis (2018) (LinNet), where nodes are lineups and a directed edge runs from λ<sub>a</sub> to λ<sub>b</sub> if λ<sub>b</sub> outperformed λ<sub>a</sub>, weighted by net rating; node2vec then produces embeddings for downstream tasks such as predicting matchups. This approach is also susceptible to small sample sizes, and **cannot make predictions for previously unseen lineups**, as those lineups were not part of the training network.

## 3. Our Model

L-RAPM consists of two modeling components: (a) individual player ratings, and (b) lineup ratings.

### 3.1 Player ratings: Regularized Adjusted Plus-Minus

To build the priors for the lineup ratings, ratings for individual players are needed first, obtained via Sill (2010)'s RAPM. **The season prior to the one for which lineups are rated is used** — to rate lineups for 2023–24, player ratings come from 2022–23.

For each possession the model needs: (i) players on offense, (ii) players on defense, (iii) points scored. Every player *p* is associated with two dummy variables, x<sub>p,off</sub> and x<sub>p,def</sub>. For data point *i*, if player *p* is on offense x<sub>i,p,off</sub> = 1; if on defense x<sub>i,p,def</sub> = −1; otherwise both are 0. With *y<sub>i</sub>* the points scored during possession *i*:

$$\min_{\gamma} \sum_{i=1}^{n}\left(y_i - \Big(\gamma_0 + \sum_{j=1}^{m}\gamma_{j,\text{off}}\,x_{i,j,\text{off}} + \sum_{j=1}^{m}\gamma_{j,\text{def}}\,x_{i,j,\text{def}}\Big)\right)^{2} + \lambda_{\text{off}}\sum_{j=1}^{m}\gamma_{j,\text{off}}^{2} + \lambda_{\text{def}}\sum_{j=1}^{m}\gamma_{j,\text{def}}^{2}$$

**A different regularization constant is used for the offensive and defensive coefficients** to give the model more flexibility; λ<sub>off</sub> and λ<sub>def</sub> are identified through a validation set. γ<sub>0</sub> is the league-average points per possession; γ<sub>p,off</sub> is points per possession above league average that player *p* contributes on offense; γ<sub>p,def</sub> is points per possession below league average that *p* saves on defense (positive = better than average in both cases).

**Fitted values:** using 2022–23 NBA data, the values minimizing validation error are **λ<sub>off</sub> = 4000 and λ<sub>def</sub> = 6000.**

### 3.2 Regularized regression for lineup matchups

The second component is a regression for points scored per possession where the independent variables are the **offensive and defensive lineup units** rather than the individual players. This adjusts for the opposing lineups faced, but data sparsity limits predictive power — so regularization is used, and **unlike RAPM the lineup coefficients are shrunk not to 0 but to a value informed by the player ratings.**

**Prior values π.** For a lineup λ<sub>a</sub> made up of players p₁…p₅, absent any information about the players one would assume league-average performance. But the players' RAPM ratings are known, so the prior belief before seeing any data for λ<sub>a</sub> is:

$$\pi_{\lambda_a,\text{off}} = \text{league ppp} + \gamma_{1,\text{off}} + \gamma_{2,\text{off}} + \gamma_{3,\text{off}} + \gamma_{4,\text{off}} + \gamma_{5,\text{off}}$$
$$\pi_{\lambda_a,\text{def}} = \text{league ppp} + \gamma_{1,\text{def}} + \gamma_{2,\text{def}} + \gamma_{3,\text{def}} + \gamma_{4,\text{def}} + \gamma_{5,\text{def}}$$

With β the set of offensive and defensive lineup coefficients:

$$\min_{\beta} \sum_{i=1}^{n}\left(y_i - \Big(\beta_0 + \sum_{j=1}^{l}\beta_{j,\text{off}}\,x_{i,j,\text{off}} + \sum_{j=1}^{l}\beta_{j,\text{def}}\,x_{i,j,\text{def}}\Big)\right)^{2} + \lambda\sum_{j=1}^{l}(\beta_{j,\text{off}}-\pi_{j,\text{off}})^{2} + \lambda\sum_{j=1}^{l}(\beta_{j,\text{def}}-\pi_{j,\text{def}})^{2}$$

where *l* is the number of distinct lineups, *n* the number of data points, and x<sub>i,j</sub> indicates whether lineup λ<sub>j</sub> is on offense, defense, or not involved in data point *i*. The resulting β are the final lineup ratings: **adjusted for the opponents each lineup faced through the regression covariates, and informed by individual player ratings through the shrinkage target.**

## 4. Experimental Results

**Data.** Possession-level data covering the NBA seasons 2022–23 and 2023–24 (both regular seasons and playoffs). Each data point is a single possession:

`< p_i, offPl_{i,1..5}, defPl_{i,1..5} >`

where p<sub>i</sub> is points scored in possession *i*. The first season (2022–23) yields the players' RAPM ratings; the second (2023–24) evaluates predictive power.

**Rookie handling (a stated weakness):** players who appear in 2023–24 but not in the prior season — rookies from college or other professional leagues — have **their offensive and defensive RAPM set to −1 each.** Section 5 discusses alternatives.

**Experimental evaluation.** Expanding-window, out-of-sample, weekly. Start with the first 4 weeks of 2023–24 as observations, predict the possessions in week 5; thereafter use weeks 1 through (n−1) to predict week *n*. Evaluation metric is RMSE per week, with relative improvement:

$$\delta_{\text{L-RAPM}} = \frac{\text{RMSE}_{\text{L-RAPM}} - \text{RMSE}_{\text{baseline}}}{\text{RMSE}_{\text{baseline}}}$$

**Results.**

- **Over the season (Figure 2):** L-RAPM provides clear improvement over the baseline throughout, with some week-to-week variability but **no trend as the season progresses.** The reason is that later weeks still contain a mix of lineups with a few dozen possessions and lineups with several hundred.
- **By training-sample size (Figure 3):** the improvement is **larger for lineups with fewer observed possessions** — which is the majority of real cases. For lineups with more than 500 possessions the sample likely includes a good mix of opponent strength, so the raw rating has converged to (or near) its true value.
- **Previously unseen lineups (Figure 4):** these appear frequently — coaches experimenting, injuries, in-season acquisitions. L-RAPM has no fitted regression coefficient for them, **but can predict from the prior alone**; the baseline has no raw rating at all and must fall back to league-average points per possession. L-RAPM consistently outperforms, with **δ ≈ 5%.** (The last two weeks show outliers, but those are playoff weeks with very few games and very few newly seen lineups.)

**On effect size.** "These improvements might seem small, but even a **1.5% improvement adds up quickly over the possessions of a whole game to approximately 3.4 points**, which is not small. For comparison, this is higher than the home edge that betting markets incorporate in their handicap, which is about 2 points at the moment (Lopez et al. 2018)."

## 5. Discussion and Conclusions

L-RAPM addresses the major problem when rating lineups — small sample size. A typical lineup plays an average of 30 to 40 total possessions for a whole season and its observed performance is susceptible to variance. The benefits are higher when the observed sample is smaller, i.e. in exactly the settings of most interest.

Stated directions for improvement:

- **Continually updated player ratings.** Currently the priors use ratings from the previous season; updating them as the current season progresses would capture player form more accurately and would, at minimum, give better ratings for players not in the league the previous season **instead of setting them to −1.**
- **Separate regularization constants for the offensive and defensive lineup coefficients.** The player-level RAPM already does this; the lineup model uses a single λ. This should improve predictive power, **since the offensive performance of a lineup/team tends to stabilize faster than the defensive one (Partnow 2021).**

## References

- NBA Advanced Stats: Lineup Efficiency. <https://stats.nba.com/lineups/advanced/> (accessed 2025-02-18).
- Deshpande SK and Jensen ST (2016). Estimating an NBA player's impact on his team's chances of winning. *Journal of Quantitative Analysis in Sports* 12(2): 51–72.
- Lopez MJ, Matthews GJ and Baumer BS (2018). How often does the best team win? A unified approach to understanding randomness in North American sport. *The Annals of Applied Statistics* 12(4): 2483–2516.
- Partnow S (2021). *The Midrange Theory.* Triumph Books.
- Pelechrinis K (2018). LinNet: Probabilistic lineup evaluation through network embedding. *ECML PKDD*, pp. 20–36. Springer.
- Rosenbaum D (2004). Measuring how NBA players help their teams win. <http://www.82games.com/comm30.htm>
- Sill J (2010). Improved NBA adjusted +/- using regularization and out-of-sample testing. *MIT Sloan Sports Analytics Conference.*
- Winston WL, Nestler S and Pelechrinis K (2022). *Mathletics: How Gamblers, Managers, and Fans Use Mathematics in Sports.* Princeton University Press.
