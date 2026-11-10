# Match forecasts in UEFA club competitions: Elo ratings versus Transfermarkt valuations

- arXiv: https://arxiv.org/abs/2609.21674
- Authors: Gergely Csurilla, László Csató
- Sport: Soccer; N/P/R 5/6/7 = 18/30

Elo and Transfermarkt values give near-identical out-of-sample accuracy on 2020/21-2024/25 UCL/UEL matches; combining helps modestly; Elo-based seeding is near-optimal.

---

                                                     Match forecasts in UEFA club competitions:
                                                     Elo ratings versus Transfermarkt valuations
                                                                  Gergely Csurilla∗                   László Csató†

                                                                               21st September 2026
arXiv:2609.21674v1 [econ.EM] 18 Sep 2026




                                           “Second, it would be interesting to check whether the reported results carry over to other
                                           settings in soccer. For example, can Transfermarkt values also generate accurate predictions
                                           for games between clubs?” (Peeters, 2018, p. 28)

                                                                                        Abstract
                                                  The pre-season strengths of European football clubs are usually measured by two
                                                  proxies in the literature. Football Club Elo Ratings provide strictly performance-
                                                  based Elo ratings from the early days of the European Cups, while Transfermarkt
                                                  valuations are crowd-based estimates of squad market values. This paper compares
                                                  them by evaluating their ability to forecast the results of matches played in the UEFA
                                                  Champions League and the UEFA Europa League between the seasons 2020/21 and
                                                  2024/25. The two indicators yield almost identical out-of-sample accuracy when
                                                  used separately. Combining the two measures leads to a modest improvement, but
                                                  the best aggregation procedure is sensitive to the forecast target. Our results suggest
                                                  that seeding based on Elo ratings would be (closely) optimal.

                                           Keywords: Elo rating; football; forecasting; market value; UEFA club competitions
                                           MSC class: 62F07, 62P20, 90B90
                                           JEL classification number: C53, Z20




                                              ∗
                                                E-mail: csurilla.gergely@krtk.elte.hu
                                           Institute of Economics, ELTE Centre for Economic and Regional Studies, Budapest, Hungary
                                           Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                           Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                           Decision Systems, Budapest, Hungary
                                           Hungarian University of Sports Science, Budapest, Hungary
                                              †
                                                Corresponding author
                                           E-mail: laszlo.csato@sztaki.hun-ren.hu
                                           Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                           Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                           Decision Systems, Budapest, Hungary
                                           Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of
                                           Operations Research and Actuarial Sciences, Budapest, Hungary
1     Introduction
Simulating tournament designs strongly relies on measures of team strength (Lasek and
Gagolewski, 2018; Sziklai et al., 2022; Devriesere et al., 2025). Elo ratings (Elo, 1978;
Aldous, 2017; Gomes de Pinho Zanco et al., 2024) have become a natural benchmark as
they summarise past results in a single dynamic, continuously updated value, and can be
used across competitions and countries (Hvattum and Arntzen, 2010; van Eetvelde and
Ley, 2019; Csató, 2024; Gerken et al., 2026). The market value of the squad provides a
different source of information. Transfermarkt values are crowd-based estimates of player
market values and have been shown to contain meaningful information about player quality
and transfer fees (Herm et al., 2014; Coates and Parshakov, 2022).
    Crucially, Peeters (2018) finds that Transfermarkt valuations outperform the previous
FIFA World Ranking (used until 2018) and the World Football Elo Ratings in forecasting
matches played by national football teams. We ask whether the same market value signal
is able to improve season-ahead predictions in the most prestigious European club football
competitions—as suggested in the last sentence of Peeters (2018), quoted above.
    This setting changes the forecasting problem in several ways. Club teams play signific-
antly more games than national teams, and compete in different domestic leagues and cups
in parallel to meeting in international competitions organised by the Union of European
Football Associations (UEFA). The higher number of matches played potentially makes
Elo ratings more informative, even though the set of matches forms a sparse, fragmented
network (Gerken et al., 2026). On the other hand, Elo ratings at the beginning of the
season are insensitive to squad changes, as they depend only on past performance observed
on the field. Since the squads of clubs change more frequently, Transfermarkt squad
values before the season provide potentially valuable orthogonal information that might
improve the accuracy of season-ahead forecasts. However, Transfermarkt values tend to
underestimate transfer fees, and this bias is quite heterogeneous, which can reduce their
predictive power (Coates and Parshakov, 2022).
    Besides focusing on club football, another crucial difference compared to Peeters (2018)
is that we deliberately use pre-season values: the Elo ratings observed on 1 September
and the lagged Transfermarkt squad value from the previous season. Our aim is not to
construct the most accurate prediction model, but to explore how tournament organisers
and researchers could predict the results of competitions based solely on the information
available before they start. This also explains why betting odds are ignored despite their
proven value in providing accurate forecasts (Wunderlich and Memmert, 2018; Wunderlich,
2025).
    We aim to explore whether pre-season Football Club Elo Ratings and Transfermarkt
values should be treated as substitutes or complements in predicting European club football
results. We therefore compare Elo-only, Transfermarkt-only, and joint models, and consider
combining model forecasts. This forecast-combination layer is important because a central
lesson in forecasting is that simple averages are often difficult to beat (Bates and Granger,
1969). Thus, our analysis also contributes to the question of whether pooling forecasts
from strongly correlated signals based on different information sources could improve
predictive accuracy when both signals are fixed at a common forecast origin.
    The comparison covers realised goal difference, expected goals difference, and ordered
match outcome. The expected goals target has been inspired by works that use shot quality
to separate underlying performance from variation in finishing (Brechot and Flepp, 2020;
Mead et al., 2023). For probability forecasts, Rank Probability Score (RPS) is our headline


                                             2
scoring rule because it respects the natural ordering of win, draw, loss (Constantinou
and Fenton, 2012; Ley et al., 2019). Nevertheless, Brier scores, log loss, and classification
success reported, too.
    According to the results, both indicators contain predictive information in the common
sample, and neither clearly dominates across all forecast targets. Combining their forecasts
yields small improvements in aggregate accuracy. Estimated stacking records the lowest
RMSE for the continuous targets, while equal-weight pooling implies the lowest RPS and
log loss under both statistical models (ordered probit and multinomial logit). The ranking
changes across evaluation seasons, and the probability-score advantage of pooling over
Transfermarkt alone remains uncertain.
    Our results could be useful especially for designing future competitions. Seeding,
the ordering of teams prior to the tournament, plays a crucial rule in determining the
outcome of any tournament except for round-robin leagues (where each team plays the
same number of matches against any other team) (Scarf and Yusof, 2011). Misaligned
seeding policies substantially bias both the FIFA Men’s (Lapré and Palazzolo, 2023)
and Women’s (Lapré and Palazzolo, 2022) World Cups, as well as the UEFA European
Championships (Lapré and Amato, 2025), by creating strongly imbalanced groups. Even
though the new incomplete round-robin format of UEFA club competitions, introduced in
the 2024/25 season, does not contain groups, seeding remains important as it determines
the set of opponents, which has a substantial impact on the final ranking (Csató et al.,
2026a,b; Guyon et al., 2026).
    The remainder of the paper is organised as follows. Section 2 gives an overview of
related studies. Section 3 describes our data and forecast samples. Section 4 presents the
empirical design, Section 5 reports the results, and Section 6 concludes.


2     Related literature
Football forecasts are obtained either from score models or from direct models of the
trichotomous win, draw, loss outcome. Poisson-type specifications provide the main score-
based benchmark (Maher, 1982; van Eetvelde and Ley, 2019). Goddard (2005) compares
score and result models, while Koopman and Lit (2019) develop dynamic specifications for
goals, goal difference, and the trichotomous categorical result. Another class of models
aggregates past performance in a team rating. Hvattum and Arntzen (2010) use Elo
differences as covariates in ordered logit models, Leitner et al. (2010) embed ratings in
tournament simulations, and Lasek and Gagolewski (2021) derive online rating updates
from likelihood-based models. Related time-varying paired comparison methods are
studied by Baker and McHale (2015), Baker and McHale (2018), and Ley et al. (2019).
Empirical evidence suggests that the leading score- and rating-based methods often have
similar predictive accuracy (Lasek et al., 2013; Hubáček et al., 2022). We therefore use
parsimonious models and focus on the information content of the strength measures, not
on developing a new prediction method.
    Team ratings based only on historical results incorporate the impact of player transfers
only after they affect observed performance. Player-level models address this issue more
directly. According to Arntzen and Hvattum (2021), Elo team ratings and plus-minus
player ratings show similar performance separately, but a model containing both improves
match forecasts. Analogously, Holmes and McHale (2024) model team strength from the
abilities of their players.
    Transfermarkt squad values provide an aggregate measure of a related source of

                                             3
information, squad composition and assessed player quality. Crowd valuations predict
realised transfer fees (Herm et al., 2014), even though they suffer from systematic bias and
substantial heterogeneity (Coates and Parshakov, 2022). Franceschi et al. (2024) survey
the determinants of player valuation in football.
    The current paper is also related to forecasting the results of UEFA club tournaments.
Corona et al. (2019) use a Bayesian match model, while Dagaev and Rudyak (2019),
Gyimesi (2024), and Devriesere et al. (2026) use Poisson models to evaluate alternative
Champions League formats and seeding rules. Csató (2024) compares the predictive power
of UEFA club coefficients and Football Club Elo Ratings in the UEFA Champions League.
    Combining forecasts is known to improve accuracy when the component models contain
different information (Bates and Granger, 1969; Wang et al., 2023). This motivates our
distinction between a joint Elo–Transfermarkt model and pools of forecasts produced by
separate models.


3     Data and empirical setting
The unit of observation is a match. The dataset covers the group stage, league phase, and
knockout stage matches played in the UEFA Champions League and the UEFA Europa
League in five recent seasons from 2020/21 to 2024/25. The group stage, used until
the 2023/24 season, has been replaced by a new incomplete round-robin league phase in
2024/25. Qualifying rounds are not considered. Three fixtures are excluded since they did
not take place: Villarreal vs. Qarabağ in 2020/21, which UEFA awarded as a 3-0 win for
Villarreal after being cancelled, and two RB Leipzig vs. Spartak Moscow fixtures in the
2021/22 Europa League Round of 16. The resulting panel contains 1,503 matches.
    The match-level data come from FotMob (https://www.fotmob.com/), and contain
match dates, home and away teams, final scores, and expected goals (xG). xG is the
likelihood that a shot is converted into a goal, based on the quality of the chance. We use
these match records to construct three forecast targets.
    Let ℎ and 𝑎 denote the home and away clubs, respectively, in match 𝑖 played in season
𝑡. The realised goal difference is

                                    GD 𝑖𝑡 = 𝐺ℎ𝑖𝑡 − 𝐺𝑎𝑖𝑡 ,                               (1)

where 𝐺ℎ𝑖𝑡 and 𝐺𝑎𝑖𝑡 are the number of goals scored by the home and away clubs, respectively.
   Analogously, the expected goals difference is

                                  xGD 𝑖𝑡 = 𝑥𝐺ℎ𝑖𝑡 − 𝑥𝐺𝑎𝑖𝑡 .                              (2)

    The third target is the ordered match outcome:
                                 ⎧
                                 ⎨0,  if the away team wins;
                                 ⎪
                                 ⎪
                           𝑅𝑖𝑡 = ⎪1, if the result is a draw;                           (3)
                                 ⎪
                                 ⎩
                                   2, if the home team wins.

   The match-level xG and final score on FotMob include potential extra time in the
second leg of knockout matches. The baseline retains these observations, while a robustness
sample excludes all matches where extra time is played.
   The explanatory variables are two season-ahead measures of relative club strength.
The first indicator is Football Club Elo Ratings (http://clubelo.com/), which provide

                                             4
                   Table 1: Coverage of pre-season strength indicators

            Competition                   𝑁               Elo         Transfermarkt
            Champions League             689              100%            98.3%
            Europa League                814              100%            88.1%
               Notes: Entries except 𝑁 are sample shares. Cancelled and administratively
               awarded fixtures are excluded. Elo is observed on 1 September of the
               corresponding season; Transfermarkt is the lagged previous season squad
               value. Coverage requires values for both clubs.


Elo ratings for European football clubs and is widely used in the academic literature as a
proxy of team strength (Bosker and Gürtler, 2024; Csató, 2022, 2024; Csató and Petróczy,
2026; Yildirim and Bilman, 2025a,b). We use ratings on 1 September of the corresponding
season for each club and define the home-away difference as:

                                      Elo𝑖𝑡 = Eloℎ𝑡 − Elo𝑎𝑡 .                              (4)

    The second indicator is the lagged Transfermarkt squad market value from the previous
season. Transfermarkt (https://www.transfermarkt.com/) publishes football transfers,
market values, and squad information; prior research interprets these values as crowd-
informed assessments of player and squad quality (Herm et al., 2014; Peeters, 2018; Coates
and Parshakov, 2022). For forecast season 𝑡, we use the club-level Transfermarkt value
assigned to season 𝑡 − 1. This value is fixed across all matches of a club in season 𝑡. The
regressor is the log market-value difference:
                                            (︁       )︁    (︁    )︁
                                            ℎ          𝑎
                               TM𝑖𝑡 = log 𝑉𝑡−1 − log 𝑉𝑡−1 ,                                (5)
         ℎ        𝑎
where 𝑉𝑡−1  and 𝑉𝑡−1 denote the lagged squad values of the home and away clubs, respectively.
Taking the difference in logarithms expresses relative squad strength, and limits the
influence of clubs with exceptionally high market values.
    For fixtures played on a neutral field, home and away correspond to the match record.
We retain this orientation for every difference, but set the home venue indicator to zero.
    The merge of data is performed in two steps. First, match-level FotMob records are
standardised by season, competition, phase, date, home club and away club. Second,
club-season indicator files are harmonised across naming conventions and joined separately
to the home and away clubs. The final panel contains the realised outcome, xG values,
pre-season Elo ratings, and lagged Transfermarkt squad values for each fixture.
    The main sample requires a played match with non-missing outcome, xG, Elo, and
Transfermarkt values. Table 1 reports coverage by competition. Outcome, xG, and Elo are
observed for every match. Transfermarkt coverage is above 98% in the Champions League
and 88% in the Europa League. Since Elo coverage is complete, the Transfermarkt-covered
matches form the common Elo–Transfermarkt sample of 1,394 observations. At the club-
season level, 17 observations lack a lagged Transfermarkt value. Their mean Elo rating is
1487.3 and their maximum Elo rating is 1603.1 (Maccabi Haifa in 2022/23), compared
with the mean of 1712.3 among the 336 covered club-season observations. Missing coverage
is therefore concentrated among lower-rated clubs.
    Table 2 summarises descriptive statistics for the sample. The positive means of
home-away goal difference and home-away xG difference indicate the well-documented
home advantage (Pollard, 2008). The means of Elo and log Transfermarkt differences

                                                 5
           Table 2: Descriptive statistics, common Elo–Transfermarkt sample

 Variable                                   𝑁          Mean     Std. dev.    Min               Max
 Goal difference                          1394         0.366        1.970 −6.000              7.000
 Expected goals difference                1394         0.327       1.387  −3.820              5.730
 Elo difference                           1394        −0.090     168.908 −613.805           499.658
 Log Transfermarkt difference             1394         0.001        1.353 −4.078              3.872
   Notes: Goal difference and expected goals difference are measured as home minus away. Elo difference
   is the 1 September home-away rating difference. Transfermarkt is the log difference of the lagged
   previous season squad values.

                    Table 3: Sample sizes under robustness restrictions

 Sample                                        Total 𝑁         Evaluation 𝑁       League-phase 𝑁
 Main                                           1394                600                272
 No extra time                                  1364                585                272
 No finals                                      1384                596                272
 No neutral matches                             1352                584                264
 No second leg                                  1203                522                272
 No last matchday                               1238                538                238
 No second leg + no last matchday               1047                460                238
 No 2024/25 league phase                        1122                328                  0
   Notes: The main sample contains played matches with non-missing outcome, xG, Elo, and Transfer-
   markt variables. The final restriction removes only the 2024/25 league phase and retains the 2024/25
   knockout stage.


are essentially zero, since most of the matches are home-away, except for the finals and
the league phase in the 2024/25 season. The correlation between the Elo and the log
Transfermarkt differences is 0.877, showing substantial but imperfect overlap between the
two indicators.
    Expanding-window forecasts are first generated for the 2022/23 season. This initial
held-out forecast is used to estimate the data-driven combination parameters. The headline
evaluation covers the 2023/24 and 2024/25 seasons, with 238 and 362 matches, respectively,
giving 600 evaluation observations.
    Table 3 presents the sample sizes for headline evaluation and seven restricted samples.
The first three address match duration and venue by excluding matches with extra time,
finals, and all fixtures classified as neutral or relocated. The next three remove knockout
second legs, last matchdays in the first phase of the competition, or both sets of these
matches. The final restriction excludes the 2024/25 league phase, but retains the knockout
stage from the same season. Section 4.4 will justify these restrictions.
    The COVID-affected seasons require special treatment due to weaker home advantage
(Bryson et al., 2021; Fischer and Haucap, 2021). Venue and attendance information are
used to construct two match-context controls, 𝐻𝑖𝑡 and 𝐶𝑖𝑡 , respectively. 𝐻𝑖𝑡 = 1 if the
designated home club plays at its usual home venue and zero otherwise. 𝐻𝑖𝑡 = 0 for finals
that are always played on a neutral field. Other potential relocations are identified when
the recorded venue is at least 150 kilometres from the home venue of the club. 𝐶𝑖𝑡 = 1 if
an attendance restriction is identified for match 𝑖. All matches in the 2020/21 season are
classified as restriction-affected because match-level attendance records are incomplete.

                                                  6
From 2021/22 onward, recorded zero attendance and manually verified cases determine
the classification; missing attendance alone does not trigger the indicator. Appendix A.2
describes how these variables enter the models and compares the match-level definition
with the earlier season-wide classification. The baseline restriction contains 308 matches in
the common sample: all (300) matches from the 2020/21 season and eight matches from
the 2021/22 season. The interaction 𝐻𝑖𝑡 𝐶𝑖𝑡 equals one for 293 matches.


4     Methodology
The methodology of our empirical analysis is presented in the following structure: model
specification (Section 4.1), out-of-sample forecast design and evaluation (Section 4.2),
forecast combination (Section 4.3), and sensitivity analysis by reasonable sample restrictions
(Section 4.4).

4.1    Baseline outcome models
For a continuous outcome 𝑌𝑖𝑡 ∈ {GD 𝑖𝑡 , xGD 𝑖𝑡 }, the linear in-sample specification, estimated
by ordinary least squares (OLS), is

                𝑌𝑖𝑡 = 𝛼 + 𝑋𝑖𝑡′ 𝛽 + 𝛾𝐻 𝐻𝑖𝑡 + 𝛾𝐶 𝐻𝑖𝑡 𝐶𝑖𝑡 + 𝛿𝑐(𝑖) + 𝜌𝑝(𝑖) + 𝜆𝑡 + 𝑢𝑖𝑡 .              (6)

𝑋𝑖𝑡 contains Elo, Transfermarkt, or both strength indicators. The coefficient 𝛾𝐻 measures
the home venue effect in matches without an identified attendance restriction, 𝛾𝐻 + 𝛾𝐶 is
the corresponding effect under restrictions. Competition, phase, and season fixed effects
are denoted by 𝛿𝑐(𝑖) , 𝜌𝑝(𝑖) , and 𝜆𝑡 , respectively. Phase fixed effects distinguish the group
or league phase from the knockout stage. The in-sample specifications use standardised
strength indicators to facilitate coefficient comparisons. Standard errors are clustered by
unordered team-pair-season.
    For the ordered match result, the baseline probability model is an ordered probit. The
latent home team performance index is

        𝑅𝑖𝑡* = 𝑋𝑖𝑡′ 𝛽 + 𝛾𝐻 𝐻𝑖𝑡 + 𝛾𝐶 𝐻𝑖𝑡 𝐶𝑖𝑡 + 𝛿𝑐(𝑖) + 𝜌𝑝(𝑖) + 𝜆𝑡 + 𝜀𝑖𝑡 ,       𝜀𝑖𝑡 ∼ 𝑁 (0, 1).   (7)

The observed result is generated by two estimated cutpoints:

                        𝑅𝑖𝑡 = 𝑗    if 𝜅𝑗−1 < 𝑅𝑖𝑡* ≤ 𝜅𝑗 ,        𝑗 = 0, 1, 2,                     (8)

with 𝜅−1 = −∞ and 𝜅2 = ∞. We estimate the two cutpoints freely. Ordered probit is
used because the three outcomes correspond to negative, zero, and positive goal differences
from the perspective of the designated home team. The category codes do not impose
equal spacing between outcomes. No separate intercept is included because the location
of the latent index is absorbed by the estimated cutpoints. Although raw Elo difference
enters the latent index linearly, the ordered probit link maps that index nonlinearly into
the three outcome probabilities.
    The ordered probit model uses a common coefficient vector for the two cumulative
probabilities, which bounds how the predictors affect the probability of draw. To check
the robustness of the forecasting conclusions, we also estimate multinomial logit models,
which do not impose this common-coefficient restriction. The comparison uses the same
predictors and the out-of-sample forecast design (see Section 4.2 and Table 5).

                                                 7
4.2    Forecast design and evaluation
Forecasts are generated recursively; for each forecast season 𝑡, model parameters are
estimated from all seasons 𝜏 < 𝑡. The Elo and Transfermarkt measures, together with
the estimated coefficients, are fixed throughout season 𝑡. Forecasts are conditional on the
fixtures and match contexts that subsequently occur. Competition, phase, venue, and
attendance-regime variables describe the match being forecast, but no outcome, xG, or
within-season performance information from season 𝑡 is used to re-estimate or update
the models. Season fixed effects are omitted because the effect for the forecast season is
unavailable at the forecast origin. Forecasts for the 2022/23 season provide the initial held-
out observations used to estimate the data-driven combination parameters; the headline
evaluation begins in 2023/24.
    We use a deliberately simple historical benchmark as a naïve reference forecast. For
continuous outcomes, it is the historical mean with an expanding window:
                                                 1 ∑︁
                                     𝑌^𝑖𝑡hist =            𝑌ℓ ,                           (9)
                                                |ℐ𝑡 | ℓ∈ℐ𝑡

where ℐ𝑡 is the set of training matches available before season 𝑡. For the ordered match
outcome, it uses expanding-window outcome frequencies with Laplace smoothing:
                                       𝑛𝑗𝑡 + 1
                              𝑝^hist
                                𝑗𝑡 =           ,        𝑗 = 0, 1, 2,                     (10)
                                       𝑛𝑡 + 3
where 𝑛𝑗𝑡 is the number of training matches with outcome 𝑗. Since it does not include the
match-context controls of the main strength models, the incremental comparison between
Elo and Transfermarkt is based primarily on specifications estimated with the same set of
controls.
    For the trichotomous ordered match outcome, the ordered-probit forecasts are comple-
mented by multinomial logit forecasts. With draw as the base outcome, the multinomial
logit probabilities are
                                            exp(𝜂𝑗𝑖𝑡 )
                    𝑃 (𝑅𝑖𝑡 = 𝑗 | 𝑋𝑖𝑡 ) = ∑︀2              ,        𝑗 = 0, 1, 2,          (11)
                                           𝑘=0 exp(𝜂𝑘𝑖𝑡 )

where 𝜂1𝑖𝑡 = 0 for the base outcome. This robustness check avoids imposing the single-index
structure of the ordinal model on the draw probability.
    Continuous forecasts are evaluated by the root mean squared error (RMSE) and the
out-of-sample 𝑅2 relative to the historical benchmark:

                                                (𝑌𝑖 − 𝑌^𝑖 )2
                                          ∑︀
                              𝑅𝑂𝑂𝑆 = 1 − ∑︀ 𝑖∈𝒯
                               2
                                                               ,                         (12)
                                                     ^ hist )2
                                           𝑖∈𝒯 (𝑌𝑖 − 𝑌𝑖

where 𝒯 is the forecast-evaluation sample.
   Probability forecasts are evaluated with proper scoring rules (Gneiting and Raftery,
2007). Our primary measure is the ranked probability score (Epstein, 1969):
                                             ⎛                         ⎞2
                                  𝑁 ∑︁1    𝑘
                               1 ∑︁       ∑︁
                        RPS =           ⎝    𝑝^𝑖𝑗 − 1{𝑅𝑖 ≤ 𝑘}⎠ .                         (13)
                              2𝑁 𝑖=1 𝑘=0 𝑗=0

RPS evaluates cumulative probabilities across away wins, draws, and home wins (Con-
stantinou and Fenton, 2012; Ley et al., 2019). Lower values indicate better forecasts. In

                                                 8
the following, all tables and the accompanying discussion report its value multiplied by
100. Pairwise RPS loss differentials and their standard errors are presented on the same
scale. Naturally, this rescaling has no effect on model rankings or statistical tests.
    Alongside RPS, we also report the Brier score (Brier, 1950):
                                      𝑁 ∑︁2
                                   1 ∑︁
                          BS =                𝑝𝑖𝑗 − 1{𝑅𝑖 = 𝑗})2 ;
                                             (^                                       (14)
                                  3𝑁 𝑖=1 𝑗=0

and the log loss:
                                                𝑁
                                             1 ∑︁
                                   LL = −          log(^
                                                       𝑝𝑖𝑅𝑖 ).                        (15)
                                             𝑁 𝑖=1
Finally, the success rate is the proportion of matches in which the most likely outcome is
realised. It is not a proper scoring rule and is interpreted as descriptive only.
    Pairwise forecast comparisons are based on match-level loss differentials. For models 𝐴
and 𝐵, we define
                                      Δ𝑖 = 𝐿𝑖,𝐴 − 𝐿𝑖,𝐵 ,                               (16)
so that negative values favour model 𝐴. The mean loss differential is estimated with
an intercept-only regression. Each cluster groups matches between the same unordered
team pair within a season and competition. Our two-sided 𝑡-tests and 95% confidence
intervals use the cluster-based standard errors and degrees of freedom. This follows the
loss-differential framework of Diebold and Mariano (1995) with a variance estimator for
the match panel. The intervals describe uncertainty in mean loss differences for the fitted
forecasts; they do not incorporate re-estimation of the outcome models or pooling weights.
For the continuous targets, the comparisons use squared error losses, not RMSE differences.
We also report forecast scores separately for the two evaluation seasons.
    Calibration is assessed for the probability of home win. We cluster the predicted
probabilities into bins and compare the mean predicted probability with the observed
frequency in each bin. Positive deviations of the observed frequency from the predicted
probability indicate underestimation of home wins in the given probability bin.

4.3    Forecast pooling
Joint estimation is distinguished from forecast pooling. The joint Elo–Transfermarkt model
includes both strength indicators in the same outcome equation. Forecast pools estimate
the Elo-only and Transfermarkt-only models separately and combine their predictions.
    For a continuous outcome, the equal-weight pool is

                               𝑌^𝑖𝑡𝑒𝑞 = 0.5 · 𝑌^𝑖𝑡Elo + 0.5 · 𝑌^𝑖𝑡TM .                (17)

For the outcome probabilities, pooling is applied outcome by outcome:

                       𝑝^𝑒𝑞          ^Elo
                         𝑖𝑗𝑡 = 0.5 · 𝑝            ^TM
                                      𝑖𝑗𝑡 + 0.5 · 𝑝 𝑖𝑗𝑡 ,        𝑗 = 0, 1, 2.         (18)

Equal weighting is specified in advance and does not require any estimation.
   We also construct data-driven combinations from earlier out-of-sample forecasts. For
continuous outcomes, the stacking specification is

                            𝑌^𝑖𝑡𝑠𝑡𝑎𝑐𝑘 = 𝑎𝑡 + 𝑏𝐸,𝑡 𝑌^𝑖𝑡Elo + 𝑏𝑇,𝑡 𝑌^𝑖𝑡TM .             (19)


                                                 9
The intercept and slope coefficients are unconstrained; the two slopes need not be positive
or sum to one. For the outcome probabilities, we select 𝜔𝑡 ∈ {0, 0.05, . . . , 1} to minimise
RPS over earlier out-of-sample forecasts:

                              𝑝^𝑟𝑝𝑠               ^Elo
                                𝑖𝑗𝑡 = (1 − 𝜔𝑡 ) · 𝑝           ^TM
                                                   𝑖𝑗𝑡 + 𝜔𝑡 · 𝑝𝑖𝑗𝑡 .                     (20)

All estimated parameters are based exclusively on forecasts and outcomes available before
the current forecast season.
    For the 2023/24 forecasts, we estimate combination parameters from the 238 out-of-
sample forecasts for 2022/23. For 2024/25, this sample expands to 476 forecasts from
2022/23 and 2023/24. Appendix Table A.1 reports the estimated parameters, including
the stacking intercepts.

4.4    Robustness checks
Our sensitivity analyses examine four features of the underlying data that may affect
forecast performance: match duration and venue, strategic match context, the replacement
of the group stage with the league phase, and selected modelling and measurement choices.
    First, the FotMob final score and match-level xG include extra time if it is played.
Hence, we repeat the forecast evaluation after excluding all matches with extra time. Venue
may also affect the interpretation of the home indicator. Finals remain in the baseline
sample but are treated as neutral (𝐻𝑖𝑡 = 0). We report separate results after excluding
finals and after removing all fixtures classified as neutral or relocated (see Section 3).
    Second, the incentives in some matches may be distorted by strategic considerations.
The second leg of a knockout tie is a prominent example: the relevant objective of any
club is advancement over the two matches, not the result of the second leg in isolation.
Therefore, a draw or even a small loss may be sufficient if it leads to qualification. The
last matchday in the group stage and the league phase could involve weak or asymmetric
incentives once qualification or elimination has already been determined (Csató et al., 2024;
Devriesere et al., 2026; Gyimesi, 2024); even deliberate losing may arise under particular
conditions (Rewilak, 2026). We consequently report RPS results after excluding knockout
second legs, after excluding the last matchday in the first phase, and after applying both
restrictions jointly.
    Third, the 2024/25 season introduced an incomplete round-robin league phase instead
of the previous group stage, which might affect the probability of a draw (Csató, 2025;
Winkelmann et al., 2026). Thus, one forecast exercise excludes the 2024/25 league-phase
matches but retains the knockout stage from the same season. In a separate analysis, we
add the 2024/25 league phase indicator and its interactions with both strength indicators
to the joint in-sample models. The baseline controls and fixed effects are retained, and
the two interaction coefficients are tested jointly and separately.
    Finally, two supplementary specifications are investigated in the Appendix. The raw
Elo difference is compared with the canonical Elo expected score, both without a home
adjustment and with a forecast-origin-specific adjustment estimated exclusively from
earlier unrestricted-attendance matches. This might be important since the update of
the Elo rating is not a linear function of Elo difference (Csató and Petróczy, 2025, 2026).
Second, as restrictions on the number of spectators influenced home advantage in European
football (Bryson et al., 2021; Fischer and Haucap, 2021), we compare the match-level
crowd-restriction indicator with the earlier season-wide classification.


                                               10
5       Results
Section 5.1 examines the in-sample associations between the strength indicators and match
outcomes. Section 5.2 compares out-of-sample accuracy, tests the significance of loss
differences, and assesses sensitivity to sample composition and the league-phase format.
Calibration of home wins is addressed in Appendix A.1, and additional specification tests
are conducted in Appendix A.2.

5.1     In-sample baseline estimates
The in-sample estimates for the common Elo–Transfermarkt sample are reported in Table 4.
Table 4.a shows that both standardised indicators are positively associated with realised
goal difference, and both estimates are statistically significant. The single-indicator
coefficients are similar in magnitude, 0.977 for Elo and 0.938 for Transfermarkt. When
both indicators are included, the coefficients decline to 0.662 and 0.358, respectively, but
remain statistically significant. The adjusted 𝑅2 increases from 0.254 in the Elo-only
model and 0.236 in the Transfermarkt-only model to 0.261 in the joint specification. The
two measures contain substantial common information about realised score differences,
with a limited additional contribution from their joint use.
    The expected goals difference results in Table 4.b provide stronger evidence of distinct
conditional information. The Elo-only and Transfermarkt-only coefficients are nearly
identical, at 0.746 and 0.742, and the two models have similar adjusted 𝑅2 values. In the
joint specification, the standardised coefficients remain comparable (0.409 for Elo and
0.384 for Transfermarkt), and both are significant. The adjusted 𝑅2 rises from 0.297 and
0.295 in the single-indicator models to 0.314 in the joint model. Thus, each indicator
contributes to explaining differences in chance creation after conditioning on the other.
The increase in model fit is larger than for realised goal difference, although it remains
moderate.
    Table 4.c shows a similar pattern for ordered match results. Both Elo and Trans-
fermarkt shift the latent index towards a more favourable outcome for the home club,
and both coefficients remain statistically significant in the joint ordered-probit model.
The conditional Elo coefficient is 0.402, compared with 0.223 for Transfermarkt. The
pseudo-𝑅2 , however, increases only marginally in the joint model.
    To conclude, the in-sample results therefore indicate that neither indicator is condi-
tionally redundant, but the gains in model fit are quite limited.

5.2     Out-of-sample forecasts
The out-of-sample analysis in Section 5.2.1 uncovers whether the conditional associations
in Table 4 translate into forecast improvements. The statistical differences between the
prediction models are tested in Section 5.2.2. Section 5.2.3 presents the sensitivity analyses
with various sample restrictions, and Section 5.2.4 investigates the effect of the novel
incomplete round-robin league phase on the estimated coefficients.

5.2.1    Forecast accuracy
According to Table 5, all of our strength models clearly outperform the unconditional
historical benchmark. Since the benchmark does not contain match-context controls, the



                                             11
         Table 4: In-sample explanatory models using Elo and Transfermarkt
                                       (a) Goal difference

                                    Elo              Transfermarkt       Joint Elo–TM
                                 0.977***                                   0.662***
          Elo                                             —
                                  (0.047)                                    (0.099)
                                                       0.938***             0.358***
          Transfermarkt              —
                                                        (0.047)              (0.095)
          𝑁                        1394                  1394                 1394
          Adjusted 𝑅2              0.254                 0.236                0.261

                                 (b) Expected goals difference

                                    Elo              Transfermarkt       Joint Elo–TM
                                 0.746***                                   0.409***
          Elo                                             —
                                  (0.032)                                    (0.066)
                                                       0.742***             0.384***
          Transfermarkt              —
                                                        (0.032)              (0.063)
          𝑁                        1394                  1394                 1394
          Adjusted 𝑅2              0.297                 0.295                0.314

                                    (c) Ordered match result

                                    Elo              Transfermarkt       Joint Elo–TM
                                 0.596***                                   0.402***
          Elo                                             —
                                  (0.036)                                    (0.070)
                                                       0.568***             0.223***
          Transfermarkt              —
                                                        (0.037)              (0.071)
          𝑁                        1394                  1394                 1394
          Pseudo 𝑅2                0.108                 0.100                0.112
            Notes: Coefficients are based on standardised season-fixed strength indicators.
            All specifications include the home venue indicator and its interaction with
            the baseline crowd-restriction indicator. All three outcome models include
            season, competition, and phase fixed effects and use standard errors clustered
            by unordered team-pair-season within competition. The ordered match result
            is estimated by ordered probit. Standard errors are in parentheses. Cells with –
            indicate that the indicator is not included in the specification. Significance: *
            𝑝 < 0.10, ** 𝑝 < 0.05, *** 𝑝 < 0.01.


substantive comparison concerns the Elo, Transfermarkt, joint, and pooled specifications,
which use a common set of controls.
   For goal difference (Table 5.a), the Elo-only and Transfermarkt-only models have
exactly the same RMSE at the reported precision. Both joint estimation and forecast
pooling reduce the error. The estimated combination records the lowest RMSE, followed
by the equal-weight pool and the joint model. Their out-of-sample 𝑅2 values are around
0.25. Thus, combining the two information sources improves goal difference forecasts,


                                                12
   Table 5: Out-of-sample forecast performance, common Elo–Transfermarkt sample
                                   (a) Goal difference forecasts

                     Model                             𝑁      RMSE         𝑅2
                     Historical                       600     1.958       0.000
                     Elo                              600     1.710       0.237
                     Transfermarkt                    600     1.710       0.237
                     Joint Elo–TM                     600     1.698       0.248
                     Equal-weight pool                600     1.695       0.251
                     Estimated combination            600     1.686       0.259

                             (b) Expected goals difference forecasts

                     Model                             𝑁      RMSE         𝑅2
                     Historical                       600     1.386       0.000
                     Elo                              600     1.183       0.272
                     Transfermarkt                    600     1.186       0.268
                     Joint Elo–TM                     600     1.173       0.284
                     Equal-weight pool                600     1.172       0.285
                     Estimated combination            600     1.168       0.290

                       (c) Ordered match result forecasts, ordered probit

 Model                             𝑁         100×RPS           Brier        Log loss       Success
 Historical                       600         23.068           0.207         1.029          0.510
 Elo                              600         19.729           0.183         0.932          0.558
 Transfermarkt                    600         19.533           0.182         0.928          0.577
 Joint Elo–TM                     600         19.539           0.182         0.926          0.560
 Equal-weight pool                600         19.431           0.182         0.923          0.568
 Estimated combination            600         19.480           0.182         0.925          0.563

                     (d) Ordered match result forecasts, multinomial logit

 Model                             𝑁         100×RPS           Brier        Log loss       Success
 Historical                       600         23.068           0.207         1.029          0.510
 Elo                              600         19.761           0.184         0.935          0.565
 Transfermarkt                    600         19.524           0.182         0.928          0.575
 Joint Elo–TM                     600         19.579           0.183         0.929          0.562
 Equal-weight pool                600         19.452           0.182         0.925          0.570
 Estimated combination            600         19.505           0.182         0.927          0.563
   Notes: Forecasts use an expanding window and are not updated within a forecast season. Lower RMSE,
   RPS, Brier score, and log loss are better, whereas higher 𝑅2 and success are better. Out-of-sample 𝑅2
   is measured relative to the expanding-window historical benchmark. All models use the same training
   and evaluation matches at each forecast origin. Success is the proportion of matches in which the
   most likely outcome occurs. Exact ties follow the code order: home win, draw, away win.


although the gain is small.


                                                 13
   Table 6: Pairwise comparison tests of ordered probit forecasts based on RPS, main sample

Comparison                             100×RPS Δ           100×Std.e.         95% CI               𝑝-value
Equal-weight vs. Elo                     −0.297               0.148       [−0.588, −0.007]         0.045**
Equal-weight vs. TM                      −0.102               0.150       [−0.397, +0.194]          0.499
Estimated vs. Equal-weight               +0.049               0.041       [−0.033, +0.130]          0.240
Estimated vs. Joint Elo–TM               −0.059               0.048       [−0.153, +0.035]          0.220
Joint Elo–TM vs. Elo                     −0.190               0.075       [−0.337, −0.042]         0.012**
Joint Elo–TM vs. Equal-weight            +0.108               0.083       [−0.056, +0.272]          0.198
Joint Elo–TM vs. TM                      +0.006               0.230       [−0.446, +0.458]          0.980
TM vs. Elo                               −0.195               0.297       [−0.778, +0.387]          0.510
  Notes: The number of observations is 600 in all cases. RPS Δ is the score of model A minus the score of
  model B; negative values favour model A. Differences, standard errors and confidence intervals report RPS
  multiplied by 100. Standard errors are clustered by unordered team-pair-season within competition. The 95%
  confidence intervals use the same 𝑡 distribution and degrees of freedom as the reported tests. Equal-weight and
  Estimated denote uniform and estimated forecast pools. The intervals condition on the fitted forecasts; they do
  not re-estimate models or pooling weights. Significance: * 𝑝 < 0.10, ** 𝑝 < 0.05, *** 𝑝 < 0.01.


      The expected goals difference results (Table 5.b) follow the same pattern. Elo performs
  slightly better than Transfermarkt when they are used separately. The joint model and
  both forecast-level combinations improve on the two single-indicator specifications. The
  estimated combination again records the lowest RMSE (1.168) and out-of-sample 𝑅2
  (0.290). The equal-weight pool is close, with an RMSE of 1.172 and an 𝑅2 of 0.285. The
  combination gain also appears for the balance of chance creation, but estimating the
  stacking parameters yields only a minor numerical improvement over equal weighting.
      For the outcome probabilities (Tables 5.c and 5.d), the equal-weight pool has the
  lowest RPS under both probability models, but all RPS values are close to each other
  except for the naïve approach. Log loss also favours equal weighting, while Brier score
  differences are negligible among the leading models. Classification success is the best for
  the Transfermarkt-only model under both links, illustrating that modal-outcome accuracy
  and probability-forecast quality do not always produce the same ranking. The estimated
  probability pools assign weights of 0.35–0.40 to Transfermarkt across the two forecast
  seasons (Table A.1), and have slightly worse aggregate RPS than the equal-weight pools.
      Across the full evaluation sample, estimated stacking records the lowest RMSE for
  both continuous targets, while equal-weight pooling records the lowest RPS and log loss
  under both probability models. These are rankings of observed losses, not evidence that
  one combination method dominates all alternatives. Table A.2 in the Appendix shows
  that the model ranking changes across evaluation seasons. The joint model records the
  lowest RPS in the 2023/24 season, while Transfermarkt alone has the lowest RPS in the
  2024/25 season under both probability specifications. Equal-weight pooling shows the best
  RPS over the full 600-match evaluation sample, but not in either season separately. The
  advantage of estimated stacking for the continuous targets also varies across seasons.

   5.2.2    Forecast comparison tests
   According to Table 6, both the equal-weight pool and the joint model achieve modest
   but statistically significant RPS gains over Elo. On the other hand, neither improves
   significantly on Transfermarkt, and the tests do not reject equal predictive accuracy for
   the two single-indicator models. Estimating the pool weights does not provide a significant

                                                      14
              Table 7: Robustness checks for outcome probability forecasts
                           (a) Match duration and venue restrictions

 Model                            Main         No extra time        No finals        No neutral
 Historical                      23.068           23.113             23.057           22.951
 Elo                             19.729           19.698             19.679           19.640
 Transfermarkt                   19.533           19.462             19.503           19.462
 Joint Elo–TM                    19.539           19.495             19.497           19.467
 Equal-weight pool               19.431           19.380             19.391           19.353
 Estimated combination           19.480           19.437             19.417           19.400
 Observations                      600                585              596               584

                         (b) Strategic-context and format restrictions

 Model                          Main        No second        No last         Both      No league
                                               leg          matchday                    phase
 Historical                    23.068        23.287          23.131        23.365       23.135
 Elo                           19.729        19.819          19.839        19.956       19.410
 Transfermarkt                 19.533        19.646          19.644        19.788       19.232
 Joint Elo–TM                  19.539        19.623          19.636        19.750       19.205
 Equal-weight pool             19.431        19.524          19.536        19.654       19.154
 Estimated combination         19.480        19.560          19.546        19.675       19.198
 Observations                    600            522           538            460           328
   Notes: Entries are the RPSs of ordered probit multiplied by 100; lower values are better. Finals
   are retained in the main sample but coded as neutral. The neutral or relocated restriction removes
   matches at venues at least 150 km from the venue of the home club. Column Both in panel (b)
   excludes knockout second legs and last first phase matchday in the first phase. The last column in
   panel (b) removes the 2024/25 league phase, but not the knockout stage. Each restriction applies
   to both training and evaluation matches. We re-estimate the component models and combination
   parameters at each forecast origin.


improvement over equal weighting.
    The comparison with Transfermarkt differs for expected goals forecasts, as equal-
weight pooling significantly reduces RMSE loss (Table A.3). Estimated stacking does not
significantly improve on equal weighting for either continuous target. The evidence for
pooling therefore depends on the forecast target and the loss function.

5.2.3    Robustness to sample composition
Table 7 shows that the ranking of prediction models with respect to their RPSs is stable
across all sample restrictions considered. The equal-weight pool performs the best after
excluding matches with extra time, finals, and all neutral or relocated fixtures (Table 7.a).
    The strategic-context restrictions lead to the same ranking again (Table 7.b). The
equal-weight pool continues to have the lowest RPS after excluding knockout second
legs, the last matchday in the first phase, or both sets of matches. The last restriction
removes the 2024/25 league phase. In the resulting evaluation sample of 328 matches, the
equal-weight pool again records the best RPS. Although the level of forecast loss varies
with sample composition, the comparison among the leading models remains stable.

                                                15
           Table 8: Structural break diagnostics for the 2024/25 league phase
                                      (a) Goal difference

                  Estimator Test                                   𝑝-value
                  OLS       Joint Elo–TM slopes                     0.709
                  OLS       Elo slope                               0.866
                  OLS       Transfermarkt slope                     0.591

                                (b) Expected goals difference

                  Estimator Test                                   𝑝-value
                  OLS       Joint Elo–TM slopes                     0.496
                  OLS       Elo slope                               0.238
                  OLS       Transfermarkt slope                     0.323

                                   (c) Ordered match result

                  Estimator            Test                           𝑝-value
                  Ordered probit       Joint Elo–TM slopes             0.389
                  Ordered probit       Elo slope                       0.337
                  Ordered probit       Transfermarkt slope             0.716
                     Notes: The number of observations is 1394 in all cases, with
                     272 league phase matches. The diagnostics test whether
                     Elo and Transfermarkt slopes (interaction coefficients) differ
                     in the 2024/25 league phase matches. Models include the
                     league-phase indicator, its interactions with both strength
                     indicators, and the baseline controls and fixed effects. Sig-
                     nificance: * 𝑝 < 0.10, ** 𝑝 < 0.05, *** 𝑝 < 0.01.


5.2.4    League-phase slope diagnostics
Table 8 tests whether the Elo and Transfermarkt slopes differ for the matches played in
the 2024/25 league phase. None of the individual or joint interaction tests rejects the
assumption of equal slope; even the smallest reported 𝑝-value exceeds 0.2. However, the
diagnostic is based on a single season and may have limited power to identify moderate
changes. Hence, the result should be read as an absence of evidence for a break, not
as proof that the relationship between the strength indicators and match outcomes is
invariant to the format change.


6       Conclusions
Our paper has compared the predictive power of pre-season Elo ratings and lagged
Transfermarkt values in recent seasons of UEFA club competitions. The two indicators
achieve similar aggregate accuracy when used separately. Estimated stacking records the
best RMSE for goal difference and expected goals difference, while equal-weight pooling
has the best RPS under both probability models. However, these gains are small, and no
combination dominates across all targets and evaluation seasons. Equal-weight pooling
retains the best RPS under every sample restriction. Its advantage in RPS over Elo

                                                16
is significant under the reported test, but the comparison with Transfermarkt remains
uncertain.
    According to Peeters (2018), Transfermarkt valuations robustly outperform Elo ratings
for matches played by national teams. We find no clear Transfermarkt advantage in UEFA
club competitions. The substantially higher number of club matches probably makes
Elo ratings more informative, but our methodology is not able to not capture this effect.
Differences in forecast horizon and the use of pre-season ratings and values also limit direct
comparisons between the two studies.
    To summarise, the objective, strictly performance-based Elo rating seems to be a
sufficiently good predictor in club football. Even though combining this measure with
market value could achieve a significant improvement in accuracy in certain settings,
seeding is expected to remain close to optimal if it is based on Elo ratings, which is worth
considering by tournament organisers.


Acknowledgements
We appreciate the help of András Gyimesi and the Social Science Computing Unit of the
Databank at the ELTE Centre for Economic and Regional Studies in data collection.
The research was supported by the National Research, Development and Innovation
Office under Grants Advanced 152220 and FK 145838, and by the János Bolyai Research
Scholarship of the Hungarian Academy of Sciences.


References
Aldous, D. (2017). Elo ratings and the sports model: A neglected topic in applied
  probability? Statistical Science, 32(4):616–629.
Arntzen, H. and Hvattum, L. M. (2021). Predicting match outcomes in association football
  using team ratings and player ratings. Statistical Modelling, 21(5):449–470.
Baker, R. D. and McHale, I. G. (2015). Time varying ratings in association football: the
  all-time greatest team is. . . . Journal of the Royal Statistical Society: Series A (Statistics
 in Society), 178(2):481–492.
Baker, R. D. and McHale, I. G. (2018). Time-varying ratings for international football
  teams. European Journal of Operational Research, 267(2):659–666.
Bates, J. M. and Granger, C. W. J. (1969). The combination of forecasts. Journal of the
 Operational Research Society, 20(4):451–468.
Bosker, J. and Gürtler, M. (2024). The impact of cultural differences on the success of elite
  labor migration—Evidence from professional soccer. Annals of Operations Research,
  341(2-3):781–824.
Brechot, M. and Flepp, R. (2020). Dealing with randomness in match outcomes: how to
  rethink performance evaluation in European club football using expected goals. Journal
  of Sports Economics, 21(4):335–362.
Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. Monthly
 Weather Review, 78(1):1–3.

                                               17
Bryson, A., Dolton, P., Reade, J. J., Schreyer, D., and Singleton, C. (2021). Causal
  effects of an absent crowd on performances and refereeing decisions during Covid-19.
  Economics Letters, 198:109664.

Coates, D. and Parshakov, P. (2022). The wisdom of crowds and transfer market values.
 European Journal of Operational Research, 301(2):523–534.

Constantinou, A. C. and Fenton, N. E. (2012). Solving the problem of inadequate scoring
  rules for assessing probabilistic football forecast models. Journal of Quantitative Analysis
 in Sports, 8(1):1.

Corona, F., Forrest, D., Tena Horrillo, J. de D., and Wiper, M. (2019). Bayesian forecasting
  of UEFA Champions League under alternative seeding regimes. International Journal
 of Forecasting, 35(2):722–732.

Csató, L. (2022). UEFA against the champions? An evaluation of the recent reform of the
  Champions League qualification. Journal of Sports Economics, 23(8):991–1016.

Csató, L. (2024). Club coefficients in the UEFA Champions League: Time for shift
  to an Elo-based formula. International Journal of Performance Analysis in Sport,
  24(2):119–134.

Csató, L. (2025). A hidden benefit of incomplete round-robin tournaments: Encouraging
  offensive play. Manuscript. DOI: 10.48550/arXiv.2509.13141.

Csató, L., Devriesere, K., Goossens, D., Gyimesi, A., Lambers, R., and Spieksma, F.
 (2026a). Ranking matters: Does the new format select the best teams for the knockout
  phase in the UEFA Champions League? International Journal of Sports Science &
 Coaching, 21(2):1123–1131.

Csató, L., Gyimesi, A., Goossens, D., Devriesere, K., Lambers, R., and Spieksma, F.
 (2026b). The uncertainty of a tournament draw: Insights from the Champions League.
  Manuscript. DOI: 10.48550/arXiv.2507.15320.

Csató, L., Molontay, R., and Pintér, J. (2024). Tournament schedules and incentives
  in a double round-robin tournament with four teams. International Transactions in
 Operational Research, 31(3):1486–1514.

Csató, L. and Petróczy, D. G. (2025). Competitive balance in the UEFA Champions
  League group stage: Novel measures show no evidence of decline. Annals of Operations
  Research, 352(1-2):105–120.

Csató, L. and Petróczy, D. G. (2026). Are penalty shootouts better than a coin toss?
  Evidence from international club football in Europe. Journal of Sports Economics,
  27(6):713–734.

Dagaev, D. and Rudyak, V. (2019). Seeding the UEFA Champions League participants:
 evaluation of the reforms. Journal of Quantitative Analysis in Sports, 15(2):129–140.

Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: A review from an
  operational research perspective. European Journal of Operational Research, 324(1):1–21.



                                             18
Devriesere, K., Goossens, D., and Spieksma, F. (2026). From groups to a single league:
 evaluating competitiveness in the UEFA Champions League. Journal of Quantitative
 Analysis in Sports, in press. DOI: 10.1515/jqas-2025-0128.
Diebold, F. X. and Mariano, R. S. (1995). Comparing predictive accuracy. Journal of
  Business and Economic Statistics, 13(3):253–263.
Elo, A. E. (1978). The Rating of Chessplayers: Past and Present. Arco, New York, New
  York, USA.
Epstein, E. S. (1969). A scoring system for probability forecasts of ranked categories.
 Journal of Applied Meteorology, 8(6):985–987.
Fischer, K. and Haucap, J. (2021). Does crowd support drive the home advantage
  in professional football? Evidence from German ghost games during the COVID-19
  pandemic. Journal of Sports Economics, 22(8):982–1008.
Franceschi, M., Brocard, J.-F., Follert, F., and Gouguet, J.-J. (2024). Determinants
  of football players’ valuation: A systematic review. Journal of Economic Surveys,
  38(3):577–600.
Gerken, J., Zhang, H., Garnica Caparrós, M., Gardeweg, L., Memmert, D., and Wunderlich,
  F. (2026). The issue of sparse networks in sports competitions: can Elo ratings efficiently
  compare football teams that never play a match? Journal of the Operational Research
 Society, in press. DOI: 10.1080/01605682.2025.2612140.
Gneiting, T. and Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and
 estimation. Journal of the American Statistical Association, 102(477):359–378.
Goddard, J. (2005). Regression models for forecasting goals and match results in association
 football. International Journal of Forecasting, 21(2):331–340.
Gomes de Pinho Zanco, D., Szczecinski, L., Kuhn, E. V., and Seara, R. (2024). Stochastic
 analysis of the Elo rating algorithm in round-robin tournaments. Digital Signal Processing,
 145:104313.
Guyon, J., Ben Salem, A., Buchholtzer, T., and Tanré, M. (2026). Drawing and scheduling
 incomplete tournaments with seeding constraints: the case of the UEFA Champions
 League. Manuscript. DOI: 10.2139/ssrn.5413142.
Gyimesi, A. (2024). Competitive balance in the post-2024 Champions League and the
 European Super League: A simulation study. Journal of Sports Economics, 25(6):707–
 734.
Herm, S., Callsen-Bracker, H.-M., and Kreis, H. (2014). When the crowd evaluates soccer
  players’ market values: Accuracy and evaluation attributes of an online community.
 Sport Management Review, 17(4):484–492.
Holmes, B. and McHale, I. G. (2024). Forecasting football match results using a player
 rating based model. International Journal of Forecasting, 40(1):302–312.
Hubáček, O., Šourek, G., and Železnỳ, F. (2022). Forty years of score-based soccer match
 outcome prediction: an experimental review. IMA Journal of Management Mathematics,
 33(1):1–18.

                                             19
Hvattum, L. M. and Arntzen, H. (2010). Using ELO ratings for match result prediction in
  association football. International Journal of Forecasting, 26(3):460–470.

Koopman, S. J. and Lit, R. (2019). Forecasting football match results in national league
 competitions using score-driven time series models. International Journal of Forecasting,
 35(2):797–809.

Lapré, M. A. and Amato, J. G. (2025). The impact of imbalanced groups in UEFA Euro
  1980–2024 and comparison with the FIFA World Cup. Journal of Quantitative Analysis
  in Sports, in press. DOI: 10.1515/jqas-2024-0151.

Lapré, M. A. and Palazzolo, E. M. (2022). Quantifying the impact of imbalanced groups
  in FIFA Women’s World Cup tournaments 1991–2019. Journal of Quantitative Analysis
  in Sports, 18(3):187–199.

Lapré, M. A. and Palazzolo, E. M. (2023). The evolution of seeding systems and the impact
  of imbalanced groups in FIFA Men’s World Cup tournaments 1954–2022. Journal of
  Quantitative Analysis in Sports, 19(4):317–332.

Lasek, J. and Gagolewski, M. (2018). The efficacy of league formats in ranking teams.
  Statistical Modelling, 18(5-6):411–435.

Lasek, J. and Gagolewski, M. (2021). Interpretable sports team rating models based on
  the gradient descent algorithm. International Journal of Forecasting, 37(3):1061–1071.

Lasek, J., Szlávik, Z., and Bhulai, S. (2013). The predictive power of ranking systems in
  association football. International Journal of Applied Pattern Recognition, 1(1):27–46.

Leitner, C., Zeileis, A., and Hornik, K. (2010). Forecasting sports tournaments by ratings of
  (prob)abilities: A comparison for the EURO 2008. International Journal of Forecasting,
  26(3):471–481.

Ley, C., van de Wiele, T., and van Eetvelde, H. (2019). Ranking soccer teams on the basis
  of their current strength: A comparison of maximum likelihood approaches. Statistical
  Modelling, 19(1):55–73.

Maher, M. J. (1982). Modelling association football scores. Statistica Neerlandica, 36(3):109–
 118.

Mead, J., O’Hare, A., and McMenemy, P. (2023). Expected goals in football: Improving
 model performance and demonstrating value. PLoS ONE, 18(4):e0282295.

Peeters, T. (2018). Testing the Wisdom of Crowds in the field: Transfermarkt valuations
  and international soccer results. International Journal of Forecasting, 34(1):17–29.

Pollard, R. (2008). Home advantage in football: A current review of an unsolved puzzle.
 The Open Sports Sciences Journal, 1(1).

Rewilak, J. (2026). The perversity of mild failure: Evidence from the UEFA Champions
  League. Sports Economics Review, 14:100072.

Scarf, P. A. and Yusof, M. M. (2011). A numerical study of tournament structure and
  seeding policy for the soccer World Cup Finals. Statistica Neerlandica, 65(1):43–57.

                                             20
Sziklai, B. R., Biró, P., and Csató, L. (2022). The efficacy of tournament designs. Computers
  & Operations Research, 144:105821.

van Eetvelde, H. and Ley, C. (2019). Ranking methods in soccer. In Kenett, R. S.,
  Longford, T. N., Piegorsch, W., and Ruggeri, F., editors, Wiley StatsRef: Statistics
  Reference Online, pages 1–9. Springer, Hoboken, New Jersey, USA.

Wang, X., Hyndman, R. J., Li, F., and Kang, Y. (2023). Forecast combinations: An over
 50-year review. International Journal of Forecasting, 39(4):1518–1547.

Winkelmann, D., Deutscher, C., and Michels, R. (2026). Predicting qualification thresholds
 in the UEFA Champions League and Europa League under the new league phase format.
 Manuscript. DOI: 10.48550/arXiv.2508.20075.

Wunderlich, F. (2025). Using the wisdom of crowds in sports: how performance analysis
 in football can benefit from the information enclosed in betting odds. International
 Journal of Performance Analysis in Sport, 25(4):687–706.

Wunderlich, F. and Memmert, D. (2018). The betting odds rating system: Using soccer
 forecasts to forecast soccer. PLoS ONE, 13(6):e0198668.

Yildirim, M. and Bilman, M. E. (2025a). New rules, new game? The effects of the away
  goals rule removal and video assistant referee adoption on game dynamics in UEFA
  Champions League ties. Journal of Policy Modeling, 47(1):78–96.

Yildirim, M. and Bilman, M. E. (2025b). Second-leg home advantage no more? The
  impact of Video Assistant Referee and no away goals rule in elite soccer. Journal of
  Policy Modeling, 47(5):1097–1112.




                                             21
Appendix
A.1     Calibration
Table A.4 presents binned calibration of home win probabilities for the combined ordered
probit forecasts. For each specification, the observed frequency of home win exceeds the
mean predicted probability in every bin. For the equal-weight pool, the gap is the smallest
in the central probability range and larger in the 0.2–0.4 and 0.8–1.0 bins, but the latter
contains only 31 matches.

A.2     Additional specification checks
For the Elo functional form check, we use the expected winning probability
                                                     1
                              𝑊𝑖𝑡 (ℎ) =                               ,                  (21)
                                          1 + 10−(Elo𝑖𝑡 +ℎ𝐻𝑖𝑡 )/400
where ℎ is the home advantage parameter (in Elo points) and 𝐻𝑖𝑡 is the home venue
indicator. Neutral fixtures receive no adjustment as 𝐻𝑖𝑡 = 0. At each forecast origin, we
       ̂︀ ∈ {−50, −49, . . . , 150} to minimise mean squared error against the home score
select ℎ 𝑡
(win = 1, draw = 0.5, loss = 0) on earlier matches with unrestricted attendance in the
common sample.
    The raw Elo and ℎ = 0 specifications include separate 𝐻𝑖𝑡 and 𝐻𝑖𝑡 𝐶𝑖𝑡 terms. With
estimated ℎ, the transformation contains the home adjustment, so we omit the separate
𝐻𝑖𝑡 term and retain 𝐻𝑖𝑡 𝐶𝑖𝑡 . All three specifications include competition and phase fixed
effects. The transformed score enters the outcome models as a predictor. According to
Table A.5, the raw Elo difference performs slightly better for all three forecast targets.
    Table A.6 compares the baseline crowd-restriction flag with a season-wide classification
of 2020/21 and 2021/22. Under the baseline definition, the entire 2020/21 season is treated
as restriction-affected and eight verified closed-door matches are added from the 2021/22
season. The estimated restricted home effect remains positive under both definitions, but
its magnitude and precision vary across outcomes. This exercise is therefore interpreted as
a check on the home-context controls, not as a separate estimate of the effect of restrictions
on attendance.




                                               22
            Table A.1: Estimated Elo–Transfermarkt combination parameters
                                 (a) Goal difference forecasts

Estimator     Forecast season       𝑁       Elo parameter          TM parameter          Intercept
Stacked           2023/24          238           0.608                   0.466             0.234
Stacked           2024/25          476           0.587                   0.454             0.268

                            (b) Expected goals difference forecasts

Estimator     Forecast season       𝑁       Elo parameter          TM parameter          Intercept
Stacked           2023/24          238           0.479                   0.541             0.082
Stacked           2024/25          476           0.507                   0.442             0.157

                              (c) Ordered match result forecasts

    Estimator             Forecast season 𝑁            Elo parameter        TM parameter
    Ordered probit           2023/24      238                0.6                 0.4
    Ordered probit           2024/25      476               0.65                0.35
    Multinomial logit        2023/24      238               0.65                0.35
    Multinomial logit        2024/25      476               0.65                0.35
      Notes: For continuous outcomes, entries are unconstrained stacking coefficients estimated
      from earlier out-of-sample forecasts and need not sum to one. Column Intercept reports the
      constant in each stacking regression; probability pools have no intercept. For the ordered
      match result probabilities, the parameters are convex Elo–Transfermarkt mixture weights
      selected by minimising previous out-of-sample RPS over a grid.




                                               23
                  Table A.2: Forecast performance by evaluation season
                               (a) One season forecast: 2023/24

Model                             Goal         xG difference         Ordered        Multinomial
                               difference                             probit           logit
Measure of loss                 RMSE                 RMSE           100×RPS          100×RPS
Historical                       1.830               1.329            22.997          22.997
Elo                              1.531               1.141            18.287          18.318
Transfermarkt                    1.537               1.140            18.509          18.518
Joint Elo–TM                     1.522               1.134            18.185          18.212
Equal-weight pool                1.519               1.129            18.246          18.273
Estimated combination            1.489               1.118            18.230          18.256
  Notes: The number of observations is 238 in all cases. Lower values are better.

                               (b) One season forecast: 2024/25

Model                             Goal         xG difference         Ordered        Multinomial
                               difference                             probit           logit
Measure of loss                 RMSE                 RMSE           100×RPS          100×RPS
Historical                       1.830               1.329            22.997          22.997
Elo                              1.531               1.141            18.287          18.318
Transfermarkt                    1.537               1.140            18.509          18.518
Joint Elo–TM                     1.522               1.134            18.185          18.212
Equal-weight pool                1.519               1.129            18.246          18.273
Estimated combination            1.489               1.118            18.230          18.256
  Notes: The number of observations is 238 in all cases. Lower values are better.




                                                24
               Table A.3: Selected pairwise comparison tests of forecasts
                             (a) Goal difference, squared error loss

Comparison                            Δ              Std.e.          95% CI              𝑝-value
Equal-weight vs. Elo                −0.052           0.032       [−0.115, +0.010]        0.099*
Equal-weight vs. TM                 −0.052           0.032       [−0.116, +0.011]         0.105
Estimated vs. Equal-weight          −0.031           0.039       [−0.107, +0.046]         0.431

                       (b) Expected goals difference, squared error loss

Comparison                            Δ              Std.e.          95% CI              𝑝-value
Equal-weight vs. Elo                −0.026           0.016       [−0.058, +0.006]         0.116
Equal-weight vs. TM                 −0.034           0.017       [−0.067, −0.001]        0.046**
Estimated vs. Equal-weight          −0.009           0.012       [−0.032, +0.015]         0.476

                                  (c) Ordered probit, log loss

Comparison                            Δ              Std.e.          95% CI              𝑝-value
Equal-weight vs. Elo                −0.009           0.005       [−0.018, +0.001]        0.080*
Equal-weight vs. TM                 −0.004           0.005       [−0.013, +0.005]         0.375
Estimated vs. Equal-weight          +0.001           0.001       [−0.001, +0.004]         0.316

                                (d) Multinomial logit, RPS loss

Comparison                         100 × Δ       100×Std.e.     95% CI                   𝑝-value
Equal-weight vs. Elo                −0.309          0.146   [−0.596, −0.021]             0.035**
Equal-weight vs. TM                 −0.072          0.148   [−0.364, +0.220]              0.627
Estimated vs. Equal-weight          +0.053          0.044   [−0.034, +0.139]              0.232
  Notes: The number of observations is 600 in all cases. Δ is the score of model A minus the score of
  model B; negative values favour model A. Standard errors are clustered by unordered team-pair-season
  within competition. The 95% confidence intervals use the same 𝑡 distribution and degrees of freedom
  as the reported tests. Equal-weight and Estimated denote uniform and estimated forecast pools.
  The intervals condition on the fitted forecasts; they do not re-estimate models or pooling weights.
  Significance: * 𝑝 < 0.10, ** 𝑝 < 0.05, *** 𝑝 < 0.01.




                                                25
     Table A.4: Home win probability calibration, main sample
                         (a) Joint Elo–Transfermarkt

Probability bin     𝑁         Mean predicted           Observed frequency
[0.0, 0.2)          72            0.133                      0.236
[0.2, 0.4)         167            0.306                      0.365
[0.4, 0.6)         188            0.493                      0.521
[0.6, 0.8)         131            0.700                      0.710
[0.8, 1.0]          42            0.864                      0.881

                            (b) Equal-weight pool

Probability bin     𝑁         Mean predicted           Observed frequency
[0.0, 0.2)          55            0.139                      0.200
[0.2, 0.4)         172            0.306                      0.384
[0.4, 0.6)         210            0.489                      0.500
[0.6, 0.8)         132            0.695                      0.720
[0.8, 1.0]          31            0.856                      0.935

                         (c) Joint Elo–Transfermarkt

Probability bin     𝑁         Mean predicted           Observed frequency
[0.0, 0.2)          55            0.134                      0.182
[0.2, 0.4)         175            0.303                      0.377
[0.4, 0.6)         205            0.491                      0.507
[0.6, 0.8)         134            0.698                      0.731
[0.8, 1.0]          31            0.861                      0.903
  Notes: Bins are based on predicted home win probabilities by the ordered probit
  model.




                                      26
                       Table A.5: Robustness to Elo functional form
                            (a) Out-of-sample forecast performance

Target                                  Goal difference        xG difference        Ordered result
Measure of loss                            RMSE                   RMSE                100×RPS
Raw Elo difference                          1.710                 1.183                19.729
Elo expected prob., ℎ = 0                   1.714                 1.189                19.806
Elo expected prob., estimated ℎ             1.721                 1.193                19.850
  Notes: The number of observation is 600. RPS is multiplied by 100.

                (b) Home advantage parameter estimated from prior seasons

         Forecast season       Calibration 𝑁          Estimated ℎ      Calibration MSE
         2022/23                    248                    40               0.15041
         2023/24                    486                    66               0.14897
         2024/25                    724                    73               0.14668
            Notes: The home adjustment parameter ℎ in Elo points is estimated at each
            forecast origin using only earlier unrestricted-attendance matches.




      Table A.6: Home advantage under alternative crowd-restriction definitions
                                        (a) Goal difference

Restriction definition            Unrestricted         Adjustment           Restricted        𝑝-value
Baseline crowd-restriction            0.416                0.281               0.697           0.052
2020/21–2021/22 seasons               0.488                0.064               0.552           0.119

                                  (b) Expected goals difference

Restriction definition            Unrestricted         Adjustment           Restricted        𝑝-value
Baseline crowd-restriction            0.508              −0.070                0.438           0.099
2020/21–2021/22 seasons               0.716              −0.587                0.129           0.619

                                 (c) Ordered result latent index

Restriction definition            Unrestricted         Adjustment           Restricted        𝑝-value
Baseline crowd-restriction            0.071                0.314               0.385           0.194
2020/21–2021/22 seasons               0.090                0.219               0.309           0.327
  Notes: The number of observations is 1394 in all cases. Column Unrestricted is the coefficient of
  the home venue indicator. Column Adjustment is its interaction with the stated crowd-restriction
  definition. Column Restricted is their sum. OLS coefficients are for goals or xG, while the ordered
  probit coefficient is for the latent outcome index. The 𝑝-values refer to tests whether the restricted
  home effect equals zero.




                                                 27
