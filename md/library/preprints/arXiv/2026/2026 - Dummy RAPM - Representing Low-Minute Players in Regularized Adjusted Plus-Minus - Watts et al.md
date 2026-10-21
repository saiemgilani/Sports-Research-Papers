<!-- source: library/preprints/arXiv/2026/2026 - Dummy RAPM - Representing Low-Minute Players in Regularized Adjusted Plus-Minus - Watts et al.pdf -->
<!-- arXiv:2608.19454 · CC BY 4.0 · first submitted 2026-08-19 · retrieved 2026-10-21 -->

# Dummy RAPM: Representing Low-Minute Players in Regularized Adjusted Plus-Minus

**Kenny Watts, Jonathan Pipping-Gamón, Abraham J. Wyner**

arXiv:[2608.19454](https://arxiv.org/abs/2608.19454) · [PDF](https://arxiv.org/pdf/2608.19454)

## Triage (N/P/R = 5/7/9, composite 21/30)

Keeps stints of dropped low-minute players by adding five 'excluded-player count' dummy columns; cuts held-out game-margin RMSE 12.897→12.856 (13/16 seasons). Small but consistent; code on GitHub (whartonsabi/dummy-rapm); cites hoopR.

## Full text (extracted from the arXiv PDF)

                                             Dummy RAPM: Representing Low-Minute Players in
                                                    Regularized Adjusted Plus-Minus
                                                   Kenny Watts, Jonathan Pipping-Gamón, and Abraham J. Wyner
                                                                    The Wharton School, University of Pennsylvania
arXiv:2608.19454v2 [stat.AP] 21 Aug 2026

                                                                                       July 2026

                                                                                        Abstract
                                                     Regularized Adjusted Plus-Minus (RAPM) uses stint-level lineup indicators to
                                                 estimate player contributions to scoring margin. When low-minute player columns are
                                                 removed, their stints remain in the data, but the design matrix no longer represents the
                                                 complete lineup. Dummy RAPM restores this information using five indicators for the
                                                 number of excluded players on each lineup side. Across 16 NBA seasons, chronological
                                                 validation selects a 10-minute-per-appearance threshold and a dummy-to-player penalty
                                                 ratio of 2.2. On held-out March–April games, Dummy RAPM reduces mean season
                                                 game-margin RMSE from 12.897 to 12.856 and achieves lower RMSE in 13 of 16 seasons.
                                                 The average reduction is 0.042 points, or 0.30%. Although the improvement in game-level
                                                 predictive accuracy is small, it is consistent: RAPM performs better when it records
                                                 how many excluded players are on each side.

                                           1 Introduction
                                           Basic plus-minus measures a team’s score differential while a player is on the court but does
                                           not adjust for teammates or opponents. Adjusted Plus-Minus (APM), associated with the
                                           WINVAL work of Jeff Sagarin and Wayne Winston and described publicly by Rosenbaum
                                           (2004), addresses this limitation by regressing stint-level score differentials on player indicators.
                                           APM estimates are unstable when players repeatedly share the floor with the same teammates
                                           and opponents or appear in few stints. Ridge regression stabilizes correlated designs by
                                           shrinking coefficients (Hoerl and Kennard, 1970). Sill (2010) applied this approach to APM
                                           and emphasized evaluation on future games, yielding Regularized Adjusted Plus-Minus
                                           (RAPM). Box Plus/Minus represents a separate, complementary line of work based on box-
                                           score and role information (Myers, 2020). Bayesian partial-pooling approaches provide a
                                           related response to weak identification. Fearnhead and Taylor (2011) estimated offensive and
                                           defensive abilities while borrowing information across seasons, and Deshpande and Jensen
                                           (2016) modeled changes in win probability using Bayesian linear regression.
                                           Some RAPM implementations remove low-minute players before fitting. Removing these
                                           columns leaves their stints in the data but makes the lineup representation incomplete. The

                                                                                            1
model may then attribute omitted contributions to retained players whose indicators are
correlated with the missing lineup information.
Dummy RAPM addresses this omission without estimating a separate coefficient for every
low-minute player. It records how many excluded players appear on the home and away sides,
then pools those count coefficients with ridge regularization. The question is simple: does
restoring this small piece of lineup information improve prediction?

2 Model
2.1 Stint response and player design
A stint is an interval over which neither lineup changes. Let ∆i be the change in home-minus-
away score margin during stint i, and define exposure
                                               PH,i + PA,i
                                        qi =               ,
                                                    2
where PH,i and PA,i count home and away possession-ending events. The response is

                                                      ∆i
                                          yi = 100       ,
                                                      qi
the home-team margin per 100 team possessions. Observation i receives weight qi , so a longer
stint contributes more to estimation. Scaling before estimation makes coefficients directly
interpretable in points per 100 team possessions.
For retained player j, xij = 1 when the player is in the home lineup, xij = −1 when in the
away lineup, and xij = 0 otherwise. Filtered RAPM estimates
                                    ( n                               )
                                    X                     2
                                          qi yi − α − xTi β + λP ∥β∥22 .
                                                           
                   α̂, β̂ = arg min
                                  α,β
                                        i=1

The intercept is not penalized, and predictors are not standardized. Ridge solutions are
computed over a decreasing sequence of λP values using cyclic coordinate descent (Friedman
et al., 2010).

2.2 Lineup-side count indicators
For k = 1, . . . , 5, define
            (k)
           dH,i = 1{the home lineup in stint i contains exactly k excluded players},
             (k)
           dA,i = 1{the away lineup in stint i contains exactly k excluded players}.
Lineups with no excluded players form the reference category. The augmented model therefore
contains ten dummy regressors, five for each lineup side. Separate home and away coefficient

                                                  2
blocks allow the association for a given count to differ according to which side contains the
excluded players.
Let γ H and γ A denote the two five-element dummy blocks. Dummy RAPM estimates
                                       n
                                       X                                                 2
                  arg      min               qi yi − α − xTi β − dTH,i γ H − dTA,i γ A
                        α,β,γ H ,γ A
                                       i=1
                                       + λP ∥β∥22 + λD ∥γ H ∥22 + ∥γ A ∥22 .
                                                                          

The relative penalty ρ = λD /λP is tuned from the data. A common penalty for the dummy
coefficients allows them to be pooled more or less strongly than the player coefficients without
requiring ten separate hyperparameters.

3 Data Construction
We use publicly accessible ESPN play-by-play and player box-score records distributed
through the sportsdataverse project (Gilani, 2026). Starter flags identify each opening lineup,
and recorded substitutions divide the game into stints with unchanged lineups. We retain
a game only when both teams have five unique recorded starters and every modeled stint
contains five unique home players and five unique away players. This removes 33 games,
including 19 in 2019.
Stint scoring is reconstructed from changes in the reported home-minus-away scoreboard
margin. This captures technical and other free throws even when the corresponding event
is not marked as ending a possession. A scoring segment with no possession exposure is
merged with the next positive-exposure stint, or with the preceding stint at the end of a
game. We verify that the resulting stint margins sum to the official final margin. Within each
game, we retain the contiguous sequence of periods beginning with period 1, preserving valid
multi-overtime games while discarding disconnected records. Garbage-time and overtime
possessions remain in the sample so that stint predictions aggregate to the full-game margin.
Player playing time is summarized by mean minutes per appearance within the relevant
training window. This reflects a player’s role when active rather than the number of games
he happened to play. As in Rosenbaum (2004), low-minute players are pooled rather than
estimated individually, but we select the cutoff by chronological validation instead of fixing it
at 250 total minutes across two seasons.
Table 1 reports the season-level sample. The analysis contains 19,589 games and 496,575
positive-exposure stints. The “Out” column counts regular-season games in May–September,
outside the analysis windows; these games may also appear among the starter exclusions.

4 Selection and Evaluation
The sample contains 16 seasons: 2007–2011, 2013–2019, and 2022–2025. Seasons are labeled
by the calendar year in which they end. The series begins in 2007 because starter metadata

                                                       3
              Table 1: Season-level analysis sample and chronological windows
 Season    All Oct–Dec     Jan–Feb Oct–Feb         Mar–Apr     Out     Starter excl.   Stints   Players
   2007   1214       443        404         847          362       0              5 28,257         454
   2008   1217       448        411         859          358       0              0 27,243         451
   2009   1228       471        409         880          348       0              0 26,348         445
   2010   1225       470        409         879          346       0              0 26,835         441
   2011   1226       479        408         887          339       0              0 27,583         452
   2013   1226       453        402         855          366       0              5 23,607         469
   2014   1225       464        403         867          357       0              1 23,700         482
   2015   1226       477        393         870          356       0              0 25,134         492
   2016   1227       489        399         888          339       0              0 25,155         477
   2017   1230       506        387         893          336       0              1 25,032         484
   2018   1226       540        375         915          309       0              2 34,393         539
   2019   1230       532        376         908          303       0             19 34,502         537
   2022   1230       527        394         921          309       0              0 42,133         605
   2023   1230       546        385         931          299       0              0 42,531         539
   2024   1231       481        405         886          345       0              0 41,552         572
   2025   1231       485        403         888          343       0              0 42,570         569

are incomplete in earlier seasons. The lockout-shortened 2011–12 season, disrupted 2019–20
season, and COVID-shortened 2020–21 season are excluded because their schedules do not
support the common October–April chronological split.
Within each season, October–December games form the inner training period, January–
February games form the inner validation period, and March–April games form the outer test
period. Outer training is exactly the union of the October–December and January–February
windows. May–September games are in none of the four analysis sets. The windows are
disjoint and strictly chronological.
The initial inner search considers mean-minutes-per-appearance thresholds

                                      {0, 5, 10, 15, 20, 25, 30}

and dummy-to-player penalty ratios

                                      {0, 0.1, 0.25, 0.5, 1, 2}.

Threshold zero retains every training-observed player and serves as the unfiltered RAPM
benchmark. The cutoff determines which player columns are pooled and is chosen solely by
predictive performance.
In the first stage, we evaluate every threshold-ratio pair in the initial grid. For each pair, we
average the inner-validation RMSEs of Dummy RAPM and filtered RAPM, then average that
score across seasons. The minimizing pair selects a threshold of 10 minutes per appearance.
Holding that threshold fixed for both models, the second stage evaluates the dummy-to-player
penalty ratio over
                                     ρ ∈ {1.0, 1.1, . . . , 2.5}.

                                                  4
If the minimum occurs at a grid boundary, we extend the grid in increments of 0.1 until the
selected value is interior. The checked grid runs from 1 to 2.5 and selects ρ = 2.2. Both
stages minimize this model-averaged, season-averaged inner-validation RMSE. Exact ties
prefer the lower minute threshold and then the larger dummy penalty. March–April results
are not used for selection.
After selection, both models are refit using all games through February and evaluated once
on March–April games. Player eligibility is recomputed using only the corresponding training
period. For each season and training window, we construct one deterministic five-fold partition
at the game level and use it for every threshold, model, and penalty ratio. Within each fit,
λP minimizes cross-validated game-margin RMSE.
For game g, stint predictions are converted back to points and summed:
                                           X
                                     ∆
                                     bg =     ybi qi /100.
                                             i∈g

For season s, game-margin RMSE is
                                         s
                                              1 X            b g )2 .
                              RMSEs =                  (∆g − ∆
                                             |Ts | g∈T
                                                     s

Held-out predictive fit is summarized by
                                             P          b 2
                               2             g∈Ts (∆g − ∆g )
                              Roos,s = 1 − P                 2
                                                               ,
                                            g∈Ts (∆g − ∆Ts )

where Ts is the March–April test set for season s and ∆Ts is its mean observed game margin.
The denominator is the test-set total sum of squares. Mean season RMSE and mean season
 2
Roos are arithmetic averages of these season-specific quantities, giving each season equal
weight rather than pooling all test games.
The paired t-test on season-level RMSE differences is the primary inferential analysis. The
Wilcoxon signed-rank and sign tests are rank-based and direction-only robustness checks;
the unfiltered-benchmark and 2019-exclusion comparisons are secondary sensitivity analyses.
These nominal tests treat seasons as independent observational units. Because adjacent
seasons share players, coaches, and league conditions, their p-values are best interpreted as
approximate across-season summaries.
Because predictions condition on the realized lineups in the held-out games, the target is
lineup-conditioned final margin rather than a pregame forecast.

                                                5
Figure 1: Mean inner-validation game-margin RMSE over the dummy-to-player penalty grid.
The dashed line marks the selected ratio, 2.2.

5 Results
5.1 Held-out prediction

               Table 2: Outer-test predictive performance across 16 seasons
                                                           2
    Model             Mean season RMSE Mean season Roos         Lower-RMSE seasons
    Dummy RAPM                12.856                0.178                   13
    Filtered RAPM             12.897                0.173                    3

Dummy RAPM reduces mean season game-margin RMSE from 12.897 to 12.856. This
reduction of 0.042 points, equivalent to 0.30% of the filtered RAPM RMSE, occurs in 13 of
                           2
16 seasons. Mean season Roos  rises from 0.173 to 0.178. Thus, the count indicators produce a
small but consistent improvement in predictive accuracy across seasons.
The across-season 95% t-based confidence interval for the reduction in RMSE is 0.013 to
0.070 points. The paired t-test gives t(15) = 3.138 and p = 0.0068. As robustness checks,
the Wilcoxon signed-rank test gives W = 120.0 and p = 0.0077. The sign test records lower
RMSE in 13 of 16 seasons (p = 0.0213).
As a secondary sensitivity analysis, Dummy RAPM has lower RMSE in 9 of 12 seasons
through 2019 and in 4 of 4 seasons from 2022 onward. Excluding 2019, the season with the
most starter-data exclusions, leaves 15 seasons with an average RMSE reduction of 0.035
points (p = 0.0132).

                                             6
Figure 2: Outer-test game-margin RMSE difference by season. Positive values indicate lower
RMSE for Dummy RAPM.

5.2 Filtering and representation
The unfiltered benchmark provides a second sensitivity analysis. Filtering low-minute
players without adding count indicators does not improve RAPM. Relative to the unfiltered
benchmark, the selected filtered model has mean RMSE 0.015 points higher (p = 0.1129),
while Dummy RAPM has mean RMSE 0.026 points lower (p = 0.0626). The improvement
therefore appears to come from restoring information about lineup composition rather than
from excluding low-minute player coefficients.

5.3 Dummy coefficients
Table 3 reports how often each home and away count occurs in the selected outer-training
designs. Exposure is the sum of qi = (PH,i + PA,i )/2 over contributing stints. The season lists
distinguish structural zeros caused by an absent category from coefficients merely shrunk
close to zero.
The dominant coefficient pattern is straightforward. Conditional on the retained-player
indicators, a lineup with one excluded home player is associated with -1.59 home-margin
points per 100 possessions. One excluded away player is associated with 0.82 home-margin
points. Both signs are consistent with the same basketball interpretation: the side using a
low-minute player tends to be weaker. The home coefficient is negative in 16 seasons, and
the away coefficient is positive in 13.
These are lineup associations, not ratings of individual excluded players. Score state, injuries,
matchups, and schedule conditions all affect when low-minute lineups appear. Counts of four

                                               7
     Table 3: Selected outer-training dummy-category exposure across seasons
    Side      Count    Stints    Exposure       Seasons   Seasons present
    Home          0   341,583   1,256,501.5         16    2007–2011, 2013–2019, 2022–
                                                          2025
    Home          1    20,320     61,577.5          16    2007–2011, 2013–2019, 2022–
                                                          2025
    Home          2     2,476         7,957.5       16    2007–2011, 2013–2019, 2022–
                                                          2025
    Home          3       676       2,759.5         12    2007, 2013–2019, 2022–2025
    Home          4       255       1,081.5          6    2018, 2019, 2022–2025
    Home          5        45         202.0          4    2022–2025
    Away          0   339,479   1,251,045.0         16    2007–2011, 2013–2019, 2022–
                                                          2025
    Away          1    21,903     65,940.5          16    2007–2011, 2013–2019, 2022–
                                                          2025
    Away          2     2,899         9,120.5       16    2007–2011, 2013–2019, 2022–
                                                          2025
    Away          3      763          2,702.0       13    2007, 2010, 2013–2019, 2022–
                                                          2025
    Away          4      266          1,090.5        7    2016, 2018, 2019, 2022–2025
    Away          5       45            181.0        4    2022–2025

                 Table 4: Selected dummy coefficients across seasons
Lineup side    Low-minute players Mean coefficient               Directional seasons
Home                              1                 -1.59                    16 negative
Home                              2                 -0.59                    16 negative
Home                              3                 -0.35            12 negative, 4 zero
Home                              4                 -0.07 5 negative, 1 positive, 10 zero
Home                              5                 -0.04            4 negative, 12 zero
Away                              1                  0.82        3 negative, 13 positive
Away                              2                  0.24         7 negative, 9 positive
Away                              3                 -0.04 11 negative, 2 positive, 3 zero
Away                              4                 -0.07 4 negative, 3 positive, 9 zero
Away                              5                  0.03 1 negative, 3 positive, 12 zero

                                                8
and five occur in only a few seasons; when a category is absent, its coefficient is structurally
zero. The clearest recurring pattern is concentrated in the one- and two-player categories.
The intervals in Figure 3 summarize variation across seasons.

Figure 3: Mean selected home and away dummy coefficients with 95% cross-season t intervals.
Away coefficients retain the home-margin orientation.

6 Discussion
Why does this modest modification improve prediction so consistently? Most of the predictive
signal is already carried by the retained-player indicators. Dropping low-minute columns
discards only a limited amount of lineup information, so a large reduction in RMSE should
not be expected. Nevertheless, the omitted information is predictive. Ten count indicators
recover enough of it to improve prediction in 13 of 16 seasons.
The comparison with the unfiltered benchmark sharpens the point. Filtering players while
omitting their lineup counts makes the model slightly worse. Recording those counts makes
it slightly better. RAPM does not need a separate, noisy coefficient for every low-minute
player, but it benefits from knowing how many such players are on the floor.
The selected ratio, ρ = 2.2, places 2.2 times as much penalty weight on the squared count
coefficients as on the squared player coefficients. Because predictors are not standardized
and occur at different frequencies, ρ is not an effective shrinkage factor and should not be
read as the literal relative contraction of the fitted coefficients. Nearby ratios perform nearly
identically, so the precise value of 2.2 is less important than the broader result: the data favor
a distinct, relatively strong penalty for the count coefficients rather than their exclusion.
The remaining weaknesses come mostly from the data. Lineups are reconstructed from
play-by-play and starter records rather than an official shift chart. Starter-data exclusions
are concentrated in 2019, although the result survives without that season. Categories with
four or five low-minute players are rare, so they contribute little to the substantive pattern.

                                                9
7 Conclusion
When low-minute players are filtered out, they disappear from the design matrix but not
from the game. Five home and five away count indicators preserve that lineup information.
Across 16 seasons, this representation improves game-margin RMSE in 13 seasons. RAPM
can therefore pool low-minute players without discarding information about their presence
on the floor.

Reproducibility
Code and instructions for reproducing the data construction, model fitting, tables, figures,
and manuscript are available at https://github.com/whartonsabi/dummy-rapm.

Acknowledgments
We thank the participants in the Wharton Sports Research Seminar for helpful discussion
and feedback.

References
Deshpande, S. K. and Jensen, S. T. (2016). Estimating an NBA player’s impact on his team’s chances of
  winning. Journal of Quantitative Analysis in Sports, 12:51–72.
Fearnhead, P. and Taylor, B. M. (2011). On estimating the ability of NBA players. Journal of Quantitative
  Analysis in Sports, 7(3).
Friedman, J., Hastie, T., and Tibshirani, R. (2010). Regularization paths for generalized linear models via
   coordinate descent. Journal of Statistical Software, 33(1):1–22.
Gilani, S. (2026). hoopR: Access Men’s Basketball Play-by-Play Data. R package version 3.1.0.
Hoerl, A. E. and Kennard, R. W. (1970). Ridge regression: Biased estimation for nonorthogonal problems.
 Technometrics, 12(1):55–67.
Myers, D. (2020). Introducing Box Plus/Minus 2.0.
Rosenbaum, D. T. (2004). Measuring how NBA players help their teams win.
Sill, J. (2010). Improved NBA adjusted plus-minus using regularization and out-of-sample testing.

                                                    10
