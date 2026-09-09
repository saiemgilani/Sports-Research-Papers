<!-- source: arXiv preprint 2512.00203, submitted 2026-01-26. Open access under arXiv's non-exclusive licence. -->
<!-- text source: PDF extracted with pypdf from https://arxiv.org/pdf/2512.00203 on 2026-09-09. Layout/columns are flattened to reading order; equations and figures may be imperfectly rendered. Consult the PDF for exact formatting. -->
<!-- arxiv: 2512.00203 · subjects: Applications (stat.AP); Machine Learning (cs.LG); Image and Video Processing (eess.IV) · Archived from the weekly sports-analytics roundup (2026-09-09) as high-value recent context (posted 2026-01-26, still widely discussed). -->

# Beyond Expected Goals: A Probabilistic Framework for Shot Occurrences in Soccer

**Pipping-Gamón, Jonathan; Feng, Tianshu; Sabin, R. Paul**

*arXiv:2512.00203* (Applications (stat.AP); Machine Learning (cs.LG); Image and Video Processing (eess.IV)), submitted 2026-01-26. [Abstract](https://arxiv.org/abs/2512.00203) · [PDF](https://arxiv.org/pdf/2512.00203). Open access.

## Abstract
Expected goals (xG) models estimate the probability that a shot results in a goal from its context (e.g., location, pressure), but they operate only on observed shots. We propose xG+, a possession-level framework that first estimates the probability that a shot occurs within the next second and its corresponding xG if it were to occur. We also introduce ways to aggregate this joint probability estimate over the course of a possession. By jointly modeling shot-taking behavior and shot quality, xG+ remedies the conditioning-on-shots limitation of standard xG. We show that this improves predictive accuracy at the team level and produces a more persistent player skill signal than standard xG models.

## Full text (extracted)

Beyond Expected Goals: A Probabilistic Framework for
Shot Occurrences in Soccer
Jonathan Pipping-Gamón1, Tianshu Feng2, and Paul Sabin 1
1Department of Statistics & Data Science, University of Pennsylvania
2Department of Computer & Information Science, University of Pennsylvania
January 27, 2026
Abstract
Expected goals (xG) models estimate the probability that a shot results in a goal
from its context (e.g., location, pressure), but they operate only on observed shots. We
propose xG+, a possession-level framework that first estimates the probability that a
shot occurs within the next second and its corresponding xG if it were to occur. We
also introduce ways to aggregate this joint probability estimate over the course of a
possession. By jointly modeling shot-taking behavior and shot quality, xG+ remedies
the conditioning-on-shots limitation of standard xG. We show that this improves pre-
dictive accuracy at the team level and produces a more persistent player skill signal
than standard xG models.
1 Introduction
1.1 Expected Goals
Expected Goals (xG) has become the most commonly used metric in modern soccer analytics
(Eggels et al., 2016). This statistic can now be seen on television broadcasts and is even
shown as part of the popular video game EA Sports FC (formerly FIFA).
xG quantifies the probability that a shot will result in a goal based on characteristics such as
shot location, angle to the goal, shot type, and defensive pressure (Spearman, 2018). Perhaps
the earliest use of expected goals was Ensum et al. (2004), which used a logistic regression
model to estimate the probability that a shot becomes a goal. Macdonald (2012) implements
an expected goals model in a different low-scoring sport, ice hockey, where expected goals
were used to estimate an adjusted plus-minus model for players in the NHL. Like this work
in the NHL, xG in soccer has been shown to be a more predictive metric of future goals
scored than actual goals scored (Heuer and Rubner (2012) & Mead et al. (2023)).
Lucey et al. (2015) introduced the use of spatio-temporal data to estimate expected goals
models. Fernández et al. (2019) uses an expected goals model (among others) to decompose
1
arXiv:2512.00203v2  [stat.AP]  26 Jan 2026

the game into a series of decisions and actions by each player.
1.2 Limitations of Expected Goals
Any limitations of xG are important to recognize as xG is not only used as a metric itself
but is a foundational piece to many important research papers in soccer analytics. Singh
(2018), Bransen and Van Haaren (2018), and Statsbomb (2021) use the xG value of actual
shots to value on-ball actions in the buildup. This is often referred to as expected threat
(xT) and sometimes as on-ball value (OBV).
Despite its widespread use, xG remains limited by its foundational assumption: it only
evaluates the quality of shots that areactually taken. As a result, the model ignores many
of the most dangerous moments in a match simply because they did not result in a shot.
There have been very few previous attempts to explicitly model the probabilistic nature of
shot taking. The work of Fernández et al. (2019) and Fernández et al. (2021) decomposes
actions into a sequence using spatio-temporal tracking data and models the probability of a
pass, balldrive, orshotattheendofapossession. Theauthorsspendlittletimetalkingabout
the expected goals part of their work, focusing on the passing and ball drive components,
but do report that they had some model for the probability a shot occurs.
Another work that incorporated some probabilistic component of shot taking is Poropudas
and Inkilä (2021), who incorporated a shot decision model into expected threat (xT).
A few attempts at adjusted plus-minus models in soccer using expected goals have also
been attempted, similar to Macdonald (2012) in hockey. Matano et al. (2018) attempted to
use expected goals in their FIFA rating augmented plus-minus but decided against it due
to data limitations. Kharrat et al. (2020) and Zhang (2022) use expected goals to derive
various extensions to the augmented plus-minus models proposed by Macdonald (2012).
xG is also typically used in predictive models either alongside or instead of the actual goals
in the match, as was the case with FiveThirtyEight’s Soccer Power Index (SPI) (FiveThir-
tyEight, 2020).
While “all models are wrong,” any shortcomings of expected goals models propagate to power
ratings models, adjusted plus-minus models, and expected threat models because of their
reliance on xG as an outcome variable.
Soccer matches are filled with sequences that nearly result in shots: crosses that are barely
intercepted, passes to open attackers that arrive just a moment too late, or dribbles into the
box that are stopped by a last-ditch tackle. These moments reflect true offensive danger,
yet go unrecorded in traditional xG models.
Soccer may also fall victim to the same selection bias that plagues expected points models
in American football. Brill et al. (2025) brought attention to this issue and showed that
among other issues, the fact that better offensive teams had more plays closer to the end
zone affected the certainty of machine learning-based expected points models and those that
relied on expected points (such as 4th down models).
2

Similarly in soccer, it is possible that players who are better at converting shots to goals
take more shots than those who are less skilled. In a similar vein, players who are better at
converting opportunities into shots are likely taking an outsized share of shots compared to
other players who play similar positions.
Since xG models are trained on recorded shots, any bias in shot takers will also propagate
to other models that rely on xG.
Another assumption of xG models is that they treat shots as independent events, so aggre-
gating the metric yields inflated cumulative values whenever a sequence includes multiple
rapid-fire rebound attempts, even though only one goal could possibly result per possession.
1.3 Our Contribution
To address several of these shortcomings, we propose a new framework that models not just
the quality of shots taken, but also the probability of a shot occurring in the first place.
This component of the goal-generating process yields the metricxS, which we define as the
probability that a shot occurs within the next second. Combining this with the existing xG
metric yieldsxG+, which reflects the probability of scoring in the next secondwhether or
not a shot actually occurs. We also present possession-adjusted xG+, which measures, at
each frame, the marginal increase in the probability of scoring by the end of the possession.
This adjustment of xG at the possession level recognizes the fundamental limitation that
only one goal can be scored per possession.
By accounting for both shot generation and goal scoring, xG+ represents a more complete
metric that better aligns with how fans, coaches, and analysts intuitively understand the
game, while improving prediction of future goal-scoring performance: for players as well as
teams.
2 Motivating Examples
To illustrate the shortcomings of traditional xG and further motivate our approach, we
examine a few concrete match scenarios.
On February 19, 2025, Real Madrid faced Manchester City in the second leg of a Champions
League knockout round match (Figure 1). Early in the second half, Real Madrid’s Rodrygo
attempted a speculative shot from 35 yards out, which generated a very low xG (approx-
imately 0.03 according to FBRef). Moments later, a cross into the six-yard box nearly
connected with a Real forward who was fighting with the defender to get a foot on the ball.
If the attacker beats the defender to the ball, it’s an almost-sure goal. If the defender gets
there first instead, no shot occurs at all. The City defender reached the ball just in time,
and no shot was recorded – resulting in a zero contribution to the team’s xG despite clearly
being the more dangerous moment.
This contrast illustrates a core flaw in traditional xG: the most threatening moments are
not always those that result in shots. Our framework captures this by assigning a nonzero
scoring probability to such near-opportunities by accounting for both the probability that a
3

shot occurs and the conditional probability of a goal if a shot occurs, based on features of
the tracking data.
(a) Rodrygo takes a shot from distance with a low probability of scoring.
(b) Three players were close to tapping this cross into a goal, but none got to the ball.
Figure 1: A comparison of a shot with low goal probability and a cross with a much higher
goal probability that never became a shot.
4

(a) Mbappé has an opportunity to shoot here with a defender bearing down on him.
(b)Aftermakinghisdefendermiss, Mbappénowhasamuchbetterchancetoscore(0.5xGaccording
to FBRef)
Figure 2: Kylian Mbappé demonstrates his ability to create high-quality shots by making his
man miss against Manchester City (Feb 19, 2025). Traditional xG metrics only consider the
probability of a goal once he shoots, which is why some elite goal-scorers fail to consistently
outperform their xG. Their xG is high because they created better chances!
We now present another motivating example that illustrates the need to account for the
sequential nature of possessions. In the 78th minute of the February 22, 2025 match between
Orlando City and Philadelphia Union, Orlando generated a chaotic attacking sequence that
included four shots in rapid succession (per FBRef). As shown in Table 1, the total xG
assigned to this sequence was 1.63, which contradicts the basic logic that an attack can score
no more than one goal. This sequence – featuring blocked shots, rebounds, and ultimately
a goal – highlights the compounding nature of xG in tightly-clustered shot events.
Properly aggregating goal scoring opportunities across a possession is essential to our meth-
ods because we evaluate the probability of a goal every second.
5

Table 1: Sequence of shots leading to one goal but totaling 1.63 xG.
Time Player Shot outcome (xG)
78:01 Brekalo Shot blocked (0.05)
78:02 Muriel Shot post (0.52)
78:04 Pasalic Shot post (0.68)
78:05 Pasalic Shot goal (0.38)
3 Methodology
3.1 Modeling Framework
To correct for these limitations, we definexG+as the product of two estimated probabilities:
the likelihood of a shot occurring (xS) and the likelihood of a goal given that a shot occurs
(xG) in the next second. Formally, at any framet:
xG+t =P t(Shot)×P t(Goal|Shot) =xS t·xG t
To compute the expected goal probability over an entire possession ofnframes, we use the
formula:
xG+poss = 1−
nY
t=1
(1−xG+ t)
This equation ensures that the total possession value is bounded by one and reflects both
latent and realized scoring threats. The focus of this work now turns to estimating the
probabilityofashotoccurringwithinthenextsecondusingthecamera-basedopticaltracking
data from Gradient Sports.
3.2 Data and Feature Engineering
We use video tracking, event, and team data provided by Gradient Sports for the 2022–
23, 2023–24, and 2024–25 English Premier League (EPL) seasons. Event data encodes
on-ball actions such as possession changes, shots, and goals, while tracking data includes
synchronized ball and player positions.
For each video frame (30 fps), the full dataset includes:
•Ball and player positions (x, y, z)
•Possession indicators and shot outcomes
•Player and team IDs
From these raw inputs, we filter our data for sequences where one team has clear possession
in the attacking third, then derive the following features:
•Ball distance to the goal, bearing (angle) to goal, speed, and height
6

•Relative positioning and Euclidean distances from the ball to the 5 nearest attackers
and non-goalkeeper defenders1
•Goalkeeper location andopenGoal, a proxy for how obstructed the path to the goal is.
A full description of engineered features is included in Appendix A.
3.3 Model Estimation
We train two separate XGBoost models on our engineered features:
1.xS: Predicts the probability that a shot will occur in the next second
2.xG: Predicts the probability that a shot taken in the current frame results in a goal.
Both models use 5-fold cross-validation within each season, with log loss as the primary
evaluation metric. Model results and diagnostics are included in the next section.
4 Results and Evaluation
4.1 Baseline Comparison
Webenchmarkourmodelsagainstlogisticregressionbaselinestrainedonfourfeaturesets: (i)
ball distance only, (ii) all ball features, (iii) ball + goalkeeper features, and (iv) all features.
Each model is evaluated with 5-fold cross-validation on identical splits, and we compare
mean out-of-sample log loss. As shown in Table 2, our XGBoost models outperform all
logistic baselines – especially on the xS task. Our xG model is conceptually similar to the
proprietary models described by Hudl (nd).
Table 2: Model comparison: mean out-of-sample log loss (±SD)
Model Features xG (log loss↓) xS (log loss↓)
Logistic Ball distance only0.356±0.0105 0.0260±0.00053
Logistic Ball (all)0.350±0.0087 0.0260±0.00053
Logistic Ball + GK0.340±0.0086 0.0258±0.00054
Logistic All features0.337±0.0086 0.0251±0.00060
XGBoost All features0.326±0.0074 0.0227±0.00089
Improvement vs best logistic (all features) 0.011 (3.3%) 0.0024 (9.5%)
4.2 Feature Importance and Partial Dependence
It is useful to understand which features are most important for predicting the probabilities
of taking (xS) and converting (xG) a shot. We plot feature importance by information gain
1Note that the ball should mostly overlap with the attacker closest to the ball since the cleaned dataset
is filtered on the condition where one team has clear possession in their attacking third. As a result, the
attacker closest to the ball is not counted.
7

for both models in Figures 3 and 4. As expected, the distance from the ball to the goal (r)
is the dominant predictor in both models. Additionally, ball speed ranks second for xS and
third for xG, while the unobstructed goalmouth percentage (openGoal) is the second most
influential feature for xG but contributes little to xS. This pattern is consistent with the idea
that obstruction affects finishing quality more than the decision to shoot.
Additionally, the partial dependence plots in Figures 5 and 6 demonstrate the partial rela-
tionships between key features and predicted shooting (xS) and scoring (xG) probabilities.
From these plots, it seems that both xS and xG decrease monotonically as the distance
from the goal increases: from 8-30m for xS and 8-20m for xG. Ball speed exhibits opposing
associations across tasks: higher speeds are linked to a greater likelihood of a shot in the
next second (xS) but to lower scoring probability conditional on shooting (xG), with the lat-
ter dropping off sharply from an idle ball. A plausible interpretation is that fast sequences
(e.g., through balls or crosses) often create chances, but from less controlled setups. For xG,
openGoalis positively associated with conversion, whereas ball height is negatively associ-
ated. Ball height can also be considered a correlated proxy for what body part was used.
These patterns align with soccer domain knowledge and suggest the models capture salient
aspects of shot creation and conversion.
Figure 3: xS feature importance based on information gain
8

Figure 4: xG feature importance based on information gain
(a) Distance from ball to goal
 (b) Ball speed
Figure 5: Partial dependence plots (PDPs) for key variables affecting xS.
9

(a) Distance from ball to goal
 (b) Ball speed
(c)openGoal
 (d) Ball height
Figure 6: Partial dependence plots (PDPs) for key variables affecting xG.
4.3 Cross Validation Study on Goal Prediction
To evaluate xG+ and xS against xG as predictive metrics, we use a rolling-origin cross-
validation over three full EPL seasons (114 matchdays). We create one xG+, xS, and xG
for each possession in a game and sum up those values across all possessions. The number
in each possession is aggregated by one of these two approaches.
1.At-least-one per possession:1− Q(1−xG+ t)
2.Max xG+ per possession:max(xG+ t)
For xG, we also included a naive “independent sum of all shots” to match what is currently
done with xG: aggregating values across an entire match.
A full list of metrics is shown in Table 3.
10

Table 3: Metrics adjusted to model future team scoring
Metric Aggregation method
1. xG At-least-one-per-possession
2. xG Max-per-possession
3. xG Sum-of-shots
4. xS At-least-one-per-possession
5. xS Max-per-possession
6. xG+ At-least-one-per-possession
7. xG+ Max-per-possession
For each metric listed in Table 3 we perform a cross-validation study to predict team scoring
on out-of-sample matches. We treat each matchday as a fold, train on the remaining 113
matchdays, and evaluate performance on the held-out one.
Within each training set, we fit a mixed-effects Poisson model to the chosen metric (Table
3) with random intercepts for season, the attacking team, and the defending team, along
with a fixed effect for home advantage. We specify our model in thelme4package in the R
programming language as follows:
metric∼(1|season) + (1|season:team) + (1|season:opp) +home
Thisspecificationyieldsseason-specificestimatesof(i)teamattackingstrength, (ii)opponent
defensive strength, (iii) season-level variation, and (iv) home advantage for each metric.
These adjusted team- and opponent-level metrics are then fed into a second-stage Poisson
model for goals, which we fit inRwith the following formula:
goals∼home+season+team_off+opp_def
This two-stage modeling approach mirrors common practices in sports analytics, where un-
derlying player and team skill estimates are used to forecast observable outcomes. We display
our average cross-validation errors for each metric and aggregation strategy in Tables 4 and
5.
Table 4: Mean squared error (MSE) by metric and aggregation method
Aggregation method xG+ xS xG
At-least-one-per-possession 2.84 2.90 2.94
Max-per-possession 2.84 2.87 2.91
Sum-of-shots — — 2.90
11

Table 5: Mean absolute error (MAE) by metric and aggregation method
Aggregation method xG+ xS xG
At-least-one-per-possession 1.86 1.87 1.89
Max-per-possession 1.86 1.86 1.89
Sum-of-shots — — 1.87
Across all specifications, xG+ yielded the lowest error, suggesting that combining shot prob-
ability (xS) with goal probability given a shot (xG) improves team-level forecasts relative to
either component alone. The fact that xS also outperforms xG implies that short-horizon
shot creation is a more stable team-level signal than shot quality, underscoring the value of
modeling latent chances and the sequential structure of possessions.
To complement the average errors in Tables 4 and 5, we also examine the variability in per-
formance of each specification across matchdays. For each metric and aggregation method,
we compute the empirical 90% interval of squared error over cross-validation folds. These
intervals are reported in Table 6.
Table 6: 90% squared error intervals by metric and aggregation method
Aggregation method xG+ xS xG
At-least-one-per-possession (0.800, 2.25) (0.823, 2.28) (0.819, 2.32)
Max-per-possession (0.792, 2.26) (0.817, 2.27) (0.802, 2.31)
Sum-of-shots — — (0.822, 2.30)
Across Tables 4, 5, and 6, the max-per-possession aggregation is either indistinguishable (to
two decimal places) from, or slightly better than, the at-least-one-per-possession approach.
While the at-least-one rule is more directly interpretable as a cumulative scoring probability
over the course of a possession, it also grows mechanically with possession length. By con-
trast, the max operator focuses on the single most dangerous moment in the possession and
appears to deliver equal or better predictive accuracy for all three metrics.
Although xG+ achieves the lowest mean error in Tables 4 and 5, the 90% intervals in Table
6 still overlap across methods. This is not surprising: some matchdays feature unusually
volatile or upset-heavy results, which limit the separation we can observe in aggregate error
summaries. To probe this further, we examine performance on a matchday-by-matchday
basis. For each aggregation method, we compute the fraction of matchdays on which its
mean squared error is lower than that of the traditional sum-of-xG benchmark (Table 7).
If two approaches are truly equivalent, we would expect each to outperform the baseline on
roughly 50% of matchdays.
Under the null hypothesis that each alternative method is equally likely to beat the sum-
of-xG baseline on any given matchday, the number of wins over 114 matchdays follows
a Binomial(114,0.5)distribution, assuming performance across matchdays is independent.
Observing 69 or more wins for the at-least-one xG+ specification has probability 0.015, and
12

Table 7: Number and fraction of matchdays on which each specification outperforms the
sum of xG
Aggregation method xG+ xS xG
At-least-one-per-possession 69 (0.605) 56 (0.491) 50 (0.439)
Max-per-possession 70 (0.614) 60 (0.526) 56 (0.491)
observing 70 or more wins for the max-per-possession xG+ specification has probability
0.009. Taken together, these results provide strong evidence that xG+ offers a genuinely
better predictor of future team scoring than the traditional xG sum-of-shots approach, and
thatitsapparentgainsareunlikelytobeexplainedbysamplingvariabilityalone. Wevalidate
this claim further with a training sample robustness analysis included in Appendix B.
4.4 Player Evaluation
Traditional xG-based metrics often suggest that few players consistently “outperform” their
expected goals over multiple seasons (Goodman, 2014; Kwiatkowski, 2017; Davis and Rob-
berechts, 2024). In other words, the extent to which a player scores above or below the
sum of their xG in one season is only weakly informative about whether they will over- or
under-perform in the future.
To formalize this, we define three player-season performance-over-expected quantities:
GOExG =Goals−xG,SOE=Shots−xS,GOE xG+ =Goals−xG+.
For xG and xG+, performance over expected is defined relative to goals; for xS it is defined
relative to shots. Table 8 reports the year-to-year correlations of these measures at the
player-season level. Consistent with prior work, goals over expected relative to xG exhibit
very low stability (correlation≈0.12). By contrast, shots over expected relative to xS
are highly persistent across seasons (correlation≈0.63), while performance over xG+ lies
between these extremes, reflecting the fact that xG+ combines information from both shot
creation and finishing.
Table 8: Year-to-year correlation (stability) of performance over expected
GOExG SOE GOE xG+
0.12 0.63 0.35
This contrast aligns with the motivating example in Figure 2, featuring Kylian Mbappé.
Traditional xG assigned his eventual shot a high value (0.5 at FBRef), a level that would
be difficult to consistently outperform in finishing alone. However, that valuation ignores
the skill required to create such a high-probability opportunity in the first place. By jointly
modeling the probability of creating a shot (xS) and converting it (xG), our framework
attributes value to both the buildup and the finish, ensuring that Mbappé and similar players
13

receive credit for repeatedly manufacturing high-quality chances, not just for converting
them.
To study this effect at scale, we focus first onshots over expected(SOE), as defined above,
and examine which players most strongly over- or under-perform this baseline. Table 9
reports the top 10 and bottom 10 player-seasons by SOE in our dataset (EPL 2022–2025).
Players with large positive SOE are consistently able to turn possession states into more
shots than expected, while those with large negative SOE tend to generate fewer shots than
their xS would predict.
Table 9: Top 10 and bottom 10 player-seasons by shots over expected (SOE)
Season Player name Shots xS SOE Matches
2022-23 Marcus Rashford 103 54.4 48.6 35
2023-24 Mohamed Salah 114 67.0 47.0 32
2024-25 Antoine Semenyo 105 60.0 45.0 36
2023-24 Erling Haaland 112 67.5 44.5 31
2023-24 Darwin Núñez 98 55.2 42.8 35
2024-25 Cole Palmer 114 71.8 42.2 37
2022-23 Harry Kane 116 74.3 41.7 38
2022-23 Erling Haaland 120 78.4 41.6 35
2024-25 Eberechi Eze 92 50.9 41.1 34
2024-25 Matheus Cunha 92 51.2 40.8 33
2024-25 Rico Lewis 11 22.7 -11.7 28
2024-25 Joško Gvardiol 35 46.9 -11.9 37
2024-25 Thomas Partey 26 38.2 -12.2 35
2023-24 Manuel Akanji 9 21.3 -12.3 29
2022-23 Ben White 9 23.2 -14.2 38
2022-23 Pascal Groß 36 50.8 -14.8 37
2024-25 İlkay Gündogan 28 42.8 -14.8 31
2023-24 Bernardo Silva 30 45.0 -15.0 33
2022-23 Bruno Guimarães 22 37.1 -15.1 32
2024-25 Bernardo Silva 27 43.1 -16.1 33
The pattern in Table 9 is consistent with the stability results in Table 8: players with large
positive SOE are, in general, widely regarded as among the Premier League’s most impactful
attackers. Their primary repeatable skill is not persistently finishing above xG, but rather
consistently creating more shots than we would expect given the state of play.
The joint behavior of shot creation and finishing is illustrated in Figure 7, which plots shots
over expected (SOE) against goals over expected relative to xG (GOExG). Erling Haaland’s
record-breaking 2022–23 season, in which he scored 36 Premier League goals, appears in
the upper-right region of this plot: he not only generates more shots than expected (high
SOE), but also benefits from substantially favorable finishing variance relative to his xG
(high GOExG).
14

Figure 7: Goals over expected relative to xG (GOExG) vs shots over expected (SOE) for
EPL player-seasons, 2022–2025.
Finally, we compare players by their over-performance relative to xG+ and xG on a per-
match basis. For each player-season, we scale the performance-over-expected quantities by
matches played (MP):
GOEpm
xG+ = GOExG+
MP and GOE pm
xG = GOExG
MP .
Table 10 lists the top ten player-seasons by GOEpm
xG+ and GOEpm
xG, respectively, among players
with at least 10 matches with a chance. The xG+ ranking places sustained shot creation
and chance generation at the top of the list (e.g., Haaland, Isak, Kane, Salah), aligning more
closely with long-run attacking impact, whereas the xG-only ranking is more sensitive to
shorter-run finishing streaks.
15

Table 10: Top 10 player-seasons ranked by GOEpm
xG+ and GOEpm
xG, EPL 2022–2025
Goals over expected relative to xG+
PlayerGOE pm
xG+ Goals Matches
22–23 Erling Haaland 0.52 36 35
23–24 Erling Haaland 0.44 30 31
24–25 Omar Marmoush 0.41 10 16
24–25 Yoane Wissa 0.35 22 35
24–25 Mohamed Salah 0.33 27 38
24–25 Chris Wood 0.31 23 36
23–24 Cole Palmer 0.30 19 34
24–25 Alexander Isak 0.30 25 34
23–24 Alexander Isak 0.30 19 28
22–23 Harry Kane 0.29 25 38
Goals over expected relative to xG
PlayerGOE pm
xG Goals Matches
24–25 Omar Marmoush 0.41 10 16
24–25 Chris Wood 0.31 23 36
24–25 Michael Keane 0.21 3 10
22–23 Erling Haaland 0.52 36 35
22–23 Roberto Firmino 0.25 10 21
22–23 Martin Ödegaard 0.22 15 37
23–24 Heung-min Son 0.28 20 35
22–23 Matias Viña 0.26 3 10
22–23 Alexander Isak 0.24 11 22
23–24 Taiwo Awoniyi 0.26 7 19
Note: Sample restricted to player-seasons with at least 10 matches with a shot opportunity.
5 Discussion
5.1 Conclusions
Our proposed xG+ metric addresses key limitations of existing expected goals models by
explicitly modeling the probability of a shot and incorporating this into a possession-based
framework, which allows us to account for rebounded chances, credit dangerous non-shot
moments, and more accurately evaluate team and player strength.
Our analysis shows that xG+ is more predictive of actual goals than traditional methods
like xG, and that shot creation ability is far more stable across seasons than finishing ability.
These insights can inform recruitment, tactical analysis, and performance forecasting.
5.2 Potential Limitations
Our study has several limitations that qualify the interpretation of our findings. First,
measurement noise in video tracking can introduce error in ball and player locations which
our models depend on. Furthermore, our models – trained exclusively on the 2022–2025 EPL
seasons – may not generalize well to other leagues or competitions without recalibration.
Additionally, the one-second horizon used to define xS also renders labels sensitive to small
timestamp misalignments, creating boundary effects near the decision window. On the data-
curation side, our requirement for “clear possession in the attacking third” depends on noisy
possession indicators and may inadvertently exclude genuine goal threats (e.g., dangerous
crosses or through balls with no attackers nearby). Feature construction introduces further
approximation:openGoaltreats players as identical 2D occluders and ignores differences in
reach, height, and jumping. Methodologically, the framework scores frames with snapshot
features and thus omits sequential dependence – such as recovery runs, second balls, and
pass–shoot chains – that may shape both shot taking and shot quality. At the aggregation
stage, possession-level summaries of xS can mechanically reward longer possessions even after
the optimal shooting moment has passed, so caution is warranted when applying the metric
to player evaluation. Finally, selection on opportunity persists: stronger teams and players
16

reach dangerous states more frequently, and this exposure is not explicitly modeled in the
present formulation.
5.3 Future Work
There are several natural extensions to this work. Methodologically, replacing snapshot
models with sequence models – such as temporal point processes or survival/hazard for-
mulations – may provide richer estimation of xS. Additionally, higher-fidelity tracking may
yield improved feature construction (e.g., exact player and ball positions, player orienta-
tion), yielding more reliable estimates. Adding hierarchical team and player effects would
also mitigate selection on opportunity. Decision-analytic extensions include estimating the
counterfactual value of actions (e.g., shooting now vs. continuing the possession), which
may enable policy-aware variants of xG+. On the defensive side, this framework could be
mirrored to quantify shot and goal suppression, with credit assignment for lane-closing and
goalkeeper positioning. Finally, external validation across other leagues and competitions,
together with real-time implementations ofopenGoal, xS, and xG+ would broaden applica-
bility for scouting, broadcasting, and in-match decision-making.
References
Bransen, L. and Van Haaren, J. (2018). Measuring football players’ on-the-ball contributions
from passes during games. InInternational Workshop on Machine Learning and Data
Mining for Sports Analytics, pages 3–15. Springer.
Brill, R. S., Yurko, R., and Wyner, A. J. (2025). Analytics, have some humility: A statistical
view of fourth-down decision making.The American Statistician, pages 1–17.
Davis, J. and Robberechts, P. (2024). Biases in expected goals models confound finishing
ability.arXiv preprint arXiv:2401.09940.
Eggels, H., van Elk, R., and Pechenizkiy, M. (2016). Expected goals in soccer: Explaining
match results using predictive analytics. InThe Machine Learning and Data Mining for
Sports Analytics Workshop, volume 16. Technische Universiteit Eindhoven.
Ensum, J., Pollard, R., and Taylor, S. (2004). Applications of logistic regression to shots at
goal in association football: Calculation of shot probabilities, quantification of factors and
player/team.Journal of Sports Sciences, 22(6):500–20.
Fernández, J., Bornn, L., and Cervone, D. (2019). Decomposing the immeasurable sport: A
deep learning expected possession value framework for soccer. In13th MIT Sloan Sports
Analytics Conference, volume 2.
Fernández, J., Bornn, L., and Cervone, D. (2021). A framework for the fine-grained eval-
uation of the instantaneous expected value of soccer possessions.Machine Learning,
110(6):1389–1427.
FiveThirtyEight (2020). How Our Club Soccer Predictions Work.https://
17

fivethirtyeight.com/methodology/how-our-club-soccer-predictions-work/. Last
edit July 2, 2020; accessed October 21, 2025.
Goodman, M. (2014). Thinking about finishing skill. StatsBomb Blog. Accessed via Stats-
Bomb blog archive.
Heuer, A. and Rubner, O. (2012). Towards the perfect prediction of soccer matches.arXiv
preprint arXiv:1207.4561.
Hudl (n.d.). What are expected goals (xG)?
Kharrat, T., McHale, I. G., and Peña, J. L. (2020). Plus–minus player ratings for soccer.
European Journal of Operational Research, 283(2):726–736.
Kwiatkowski, M. (2017). Quantifying finishing skill. StatsBomb Blog. Accessed via Stats-
Bomb blog archive.
Lucey, P., Bialkowski, A., Monfort, M., Carr, P., and Matthews, I. (2015). Quality vs
quantity: Improved shot prediction in soccer using strategic features from spatiotemporal
data. In9th MIT Sloan Sports Analytics Conference.
Macdonald, B. (2012). An expected goals model for evaluating NHL teams and players. In
Proceedings of the 2012 MIT Sloan Sports Analytics Conference.
Matano, F., Richardson, L. F., Pospisil, T., Eubanks, C., and Qin, J. (2018). Augmenting
adjusted plus-minus in soccer with FIFA ratings.arXiv preprint arXiv:1810.08032.
Mead, J., O’Hare, A., and McMenemy, P. (2023). Expected goals in football: Improving
model performance and demonstrating value.PLOS ONE, 18(4):e0282295.
Poropudas, J. and Inkilä, V. (2021). Extended model for expected threat in soccer. In
Proceedings of NESSIS 2021.
Singh, K. (2018). Introducing expected threat (xT).https://karun.in/blog/
expected-threat.html. Blog post; accessed October 7, 2025.
Spearman, W. (2018). Beyond expected goals.MIT Sloan Sports Analytics Conference.
Statsbomb, H. (2021). Introducing on-ball value (obv).https://blogarchive.statsbomb.
com/news/introducing-on-ball-value-obv/. Blog post; accessed October 8, 2025.
Zhang, B. (2022). A regularized adjusted plus-minus model in soccer with box score
prior. Presented at Carnegie Mellon Sports Analytics Conference (CMSAC), October
29, 2022. Slides and video available onlinehttps://gary-boyuan-zhang.github.io/
talks/2022-10-29-CMSAC.
18

A Description of Model Features
Table 11 includes a full description of the features used to train the xS and xG models in
Section 3.3. We computeopenGoalby modeling defenders (excluding the goalkeeper) as
uniform circles with 75cm diameters and computing the tangent line pairs from the ball to
everydefenderbetweentheballandgoal. Thesegmentsmadeupbytheintersectionsbetween
tangent line pairs and the goal line are considered “obstructed.”openGoalis computed as
the percentage of the goal not covered by the obstructed segments. An illustration of this is
presented in Figure 8; red dots correspond to defenders, yellow lines represent tangent line
pairs, yellow segments represent obstructed portions of the goal line, and the black segment
represents the "open" portion of the goalmouth.
Table 11: Data dictionary of features used to train xS and xG models
V ariable Units Description
Ball features
rm Distance from ball to center of goal.
thetarad Angle from ball to center of goal.
zm Ball height above pitch.
speedm/s Ball speed.
Goal features
openGoal[0,1] Unobstructed share of the goal mouth; see Fig. 8.
Goalkeeper features
GK_rm Distance from goalkeeper to center of goal.
GK_ thetarad Bearing from goalkeeper to center of goal.
Outfield player features
DefAngle_{0..4}rad Bearing from ball to thek+ 1-th nearest defender (non-
GK), wherek∈{0, . . . ,4}.
DefDist_{0..4}m Distance from ball to thek+1-th nearest defender (non-
GK), wherek∈{0, . . . ,4}.
OffAngle_{0..4}rad Bearing from ball to thek+ 1-th nearest attacker (ex-
cluding carrier),k∈{0, . . . ,4}.
OffDist_{0..4}m Distance from ball to thek+ 1-th nearest attacker (ex-
cluding carrier),k∈{0, . . . ,4}.
19

Figure 8: An illustration of howopenGoalis constructed. Red dots correspond to defenders,
yellow lines represent tangent line pairs, yellow segments represent obstructed portions of
the goal line, and the black segment represents the "open" portion of the goalmouth.
B Analysis of Downstream Variance
Because our modeling pipeline is multi-stage, estimation error in the xS and xG components
can propagate to downstream models. To assess how sensitive our conclusions are to the
particular training sample, we perform a training-sample robustness check based on repeated
subsampling at the matchday level.
We first designate 20% of matchdays as a fixed hold-out test set, which is excluded from
all model fitting. On the remaining 80% of matchdays, we construct ten distinct training
samples by randomly selecting 90% of available matchdays (without replacement) for each
replication. For each of these ten training samples, we repeat the full modeling pipeline
from Section 3.3 and the subsequent mixed-effects and goals models, and then generate goal
predictions for all clubs in all matches in the fixed test set for each metric and aggregation
strategy.
Table 12 summarizes these results. For each metric and aggregation rule, we report the
minimum and maximum difference in average mean squared error (MSE) relative to the
traditional xG game-sum benchmark across the ten replications. Negative values indicate
that a given method improves upon the sum-of-xG baseline on the held-out test matches.
For both aggregation strategies, all three possession-level specifications (xG+, xS, and xG)
exhibit uniformly negative differences, indicating lower test-set MSE than the traditional
xG game-sum in every training subsample. The additional sampling variability introduced
by this resampling scheme makes it difficult to cleanly rank the three alternatives against
20

one another, but it does clearly show that each possession-based approach improves on the
traditional independent sum-of-shots xG benchmark. Taken together with the main-sample
results, these findings suggest that the gains from xG+ are robust to variation in the training
sample and are unlikely to be an artifact of a single favorable split of the data.
Table 12: Min–max intervals for the difference in average mean squared error (MSE) relative
to the sum of xG
Aggregation method xG+ diff xS diff xG diff
At-least-one-per-possession (-0.112,-0.0612) (-0.122,-0.0722) (-0.146,-0.0957)
Max-per-possession (-0.0929,-0.0458) (-0.108,-0.0572) (-0.106,-0.0503)
21
