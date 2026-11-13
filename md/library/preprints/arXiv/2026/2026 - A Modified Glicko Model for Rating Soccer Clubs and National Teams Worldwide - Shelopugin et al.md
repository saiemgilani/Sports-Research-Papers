<!-- source: library/preprints/arXiv/2026/2026 - A Modified Glicko Model for Rating Soccer Clubs and National Teams Worldwide - Shelopugin et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.15378 -->
<!-- authors: Andrei Shelopugin, Alexander Sirotkin -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-13; equations, tables and figures are NOT preserved - consult the PDF for those -->

# A Modified Glicko Model for Rating Soccer Clubs and National Teams Worldwide

                                             A Modified Glicko Model for Rating Soccer Clubs and National
                                                                  Teams Worldwide
                                                                       Andrei Shelopugin* 1 and Alexander Sirotkin†2
                                                                                      1 Independent Researcher
                                                                                           2 HSE University
arXiv:2611.15378v1 [cs.LG] 11 Nov 2026




                                                                                               Abstract
                                                      Comparing soccer teams that rarely or never meet is a fundamental challenge in sports analytics:
                                                  clubs play mostly within their national leagues, and national teams within their confederations.
                                                  We propose a rating framework that places clubs and national teams worldwide on a common
                                                  probabilistic scale. Building on a recent extension of Glicko with order effects and strength-
                                                  dependent draw probabilities, we adapt the model to soccer with goal-scoring adjustments, a
                                                  decomposition of home advantage, extra time, league-aware rating initialization and rules of
                                                  promotion and relegation that do not inflate the levels of leagues; national teams start from the
                                                  levels of their confederations. The models are evaluated on about 1.2 million club matches of
                                                  252 leagues from 166 countries (2000–2026) and 12.6 thousand national team matches (1998–
                                                  2026). On held-out seasons, the modified Glicko model is clearly more accurate than Elo and
                                                  as accurate as score-matrix models built on the goal expectations of a gradient boosting model,
                                                  including the Dixon–Coles and Markov chain models, while it is substantially more accurate in
                                                  international club matches. Averaging the predictions of the rating model and the Markov chain
                                                  model is more accurate than either model alone. For national teams, the model is significantly
                                                  more accurate than all baselines, especially in the final tournaments, where teams of different
                                                  confederations meet. The resulting ratings are interpretable and can be used for player evaluation,
                                                  transfer analysis and match forecasting. The match data, the ratings and the code are publicly
                                                  available at https://github.com/andreyshelopugin/SportsRatings.
                                                  Keywords: Glicko, rating systems, sports analytics, football analytics, soccer match outcome
                                                  prediction, national teams


                                         1       Introduction

                                         One of the key challenges for soccer (association football) managers, scouts, and analysts is accurately
                                         evaluating player abilities. This can be achieved through video analysis of player performance or
                                         by examining performance metrics[1]. In the latter case, it is crucial for analysts to understand the
                                         competitive level of different leagues in order to make informed decisions about player recruitment.
                                         For example, a player who is the top goal scorer in a lower-tier league may fail to replicate the same
                                         performance level after transferring to a more competitive league.
                                             Another important task in soccer analytics is predicting match outcomes [2]. To improve the
                                         accuracy of match outcome predictions, a ranking model needs to be developed. This model enables
                                         the simulation of future match results, helping soccer managers make strategic decisions, particularly
                                         regarding player transfers. Additionally, the ranking model can be used to set constraints in draw
                                         simulators for final tournaments, ensuring balanced groups and enhancing overall fan engagement.
                                             Some models already calculate ratings of soccer clubs and leagues, such as Club Elo1 and the UEFA
                                         coefficient system, but existing approaches suffer from serious drawbacks. The UEFA rating system2 is
                                             * Corresponding author: shelopuginandrey@gmail.com
                                             †
                                               avsirotkin@hse.ru
                                             1
                                               http://clubelo.com, accessed October 30, 2026.
                                             2
                                               https://www.uefa.com/nationalassociations/uefarankings/country, accessed October 30, 2026


                                                                                                   1
widely regarded in soccer, but it has several weaknesses. Firstly, it does not account for the strength of
opponents, treating victories over both top teams and weaker opponents equally. Secondly, it relies
heavily on past performances, which can distort a team’s current ranking and influence tournament
draw outcomes. If a team’s performance declines, they may still face stronger opponents, making it
difficult to accumulate points. Additionally, the system applies the same weight to matches regardless
of the season or year, failing to accurately reflect the current strength of teams.
    In addition to these major issues, the UEFA rating system has several minor limitations. For instance,
the rating points are not based on a solid mathematical foundation, making the system difficult to
interpret. Furthermore, it does not effectively assess the strength of a national league, as it primarily
focuses on the performance of top teams, which are typically the ones participating in international
competitions. This approach provides little to no information about the performance of weaker teams
in the first division or those in lower leagues.
    The same problem arises for national teams. The FIFA World Ranking3 has been computed since
2018 with an Elo-type formula [3], which accounts for the strength of the opponent. However, it
ignores the venue of a match, does not model draws explicitly, and weights matches by fixed importance
coefficients of the competitions rather than by coefficients estimated from data. Since most national
teams play most of their matches within their own confederation, the levels of the confederations are
anchored only by a small number of intercontinental matches, mainly at the World Cup.
    This paper aims to address these limitations. We propose a rating system for soccer clubs and
national teams based on the Glicko model, with several modifications. The main contributions are as
follows:

      • an adaptation of the Glicko model with strength-dependent draws and order effects of Glick-
        man [4] to soccer: the dependence of the outcome probabilities on the expected number of goals,
        a decomposition of home advantage into crowd and travel components, and extra time;

      • league-aware rating initialization and rating dynamics at promotion and relegation that do not
        inflate the levels of leagues, which makes clubs of different leagues and countries comparable;

      • an extension to national teams with confederation starting levels;

      • an evaluation on about 1.2 million matches against the Elo model and against score-matrix
        models built on the goal expectations of a gradient boosting model: the proposed model is as
        accurate as the score-matrix models overall and substantially more accurate in international
        matches, and an ablation attributes this advantage to the league-aware initialization; for national
        teams, it is significantly more accurate than all baselines, and the levels of the confederations
        play the same role; together with a comparison with the FIFA ranking;

      • public match data, code and ratings of clubs, leagues and national teams (https://github.com/
        andreyshelopugin/SportsRatings), which are planned to be updated regularly.

2       Experimental Setup

2.1      Data

The data were collected from Flashscore4 and consist of matches from the first and second divisions of
nearly all countries, as well as national cup competitions and international tournaments such as the
Champions League and Copa Libertadores. Matches involving teams from lower-ranked leagues (third
division and below) were deliberately excluded, including national cup matches featuring third-tier
teams. In addition, matches decided by forfeit were removed from the dataset.
    The club dataset contains matches played between January 2000 and September 2026 by 8,402
clubs from 252 leagues of 166 countries.
    3
        https://inside.fifa.com/fifa-rankings/world-ranking/men, accessed October 30, 2026
    4
        https://www.flashscore.com, accessed October 30, 2026




                                                         2
    The national team dataset contains matches of 220 national teams played between June 1998 and
July 2026: the World Cup and continental final tournaments, their qualifiers starting with the qualifiers
for Euro 2000 and the 2002 World Cup, and the Nations Leagues.
    The numbers of matches by type of competition are given in Table 1.
                            Table 1: Number of matches by type of competition

 Competition                                                                 Matches          Share, %
 Clubs, 2000–2026
 First divisions                                                                715,021            58.9
 Second divisions                                                               408,047            33.6
 Domestic cups                                                                   55,891             4.6
 Domestic super cups                                                              1,530             0.1
 Continental and intercontinental competitions                                   33,606             2.8
 Continental super cups                                                               97            0.0
 Total                                                                      1,214,192            100.0
 National teams, 1998–2026
 Qualifiers                                                                       9,272            73.5
 Continental final tournaments                                                    1,710            13.6
 World Cup final tournaments                                                          487           3.9
 Nations Leagues                                                                  1,149             9.1
 Total                                                                           12,618          100.0

    The score of a match includes extra time; for 6,491 of the 9,374 matches with extra time, the match
pages also give the score after 90 minutes and the goals of extra time separately. Penalty shootouts
are not included in the score, and forfeits, walkovers, annulled and abandoned matches are removed.
Neutral venues, matches played at the stadium of the visiting team and the hosts of final tournaments
are annotated. From the match notes of Flashscore, we also annotate the matches played without
spectators (21,549 club matches, mostly during the COVID-19 pandemic), with a limited number of
spectators (2,958) and at a different stadium of the home team (2,674); these annotations enter the
home advantage (Section 4).

2.2   Evaluation Protocol

All models are evaluated on the same held-out seasons. The parameters of all models are estimated on
the seasons that started before 2021, and the metrics are computed on the seasons that started in 2021
or later (Table 2).
                        Table 2: Number of matches in the training and test seasons

 Matches                                         Train (< 2021)       Test (≥ 2021)               Total
 Clubs, domestic                                         878,816            301,756          1,180,572
 Clubs, international                                     24,222              9,481             33,703
 National teams                                            8,721              3,897             12,618
 Total                                                   911,759            315,134          1,226,893

    For national teams, the split is by date: the rating models are estimated on the matches played
before 2021 and evaluated on the matches since 2021. A split by season would mix the chronology,
since a season of national teams spans several years (the qualifiers for the 2022 World Cup started in
2019, and Euro 2020 was played in 2021). During the test seasons, the parameters are fixed, and the
ratings are updated after every match in the order of the dates: the prediction of a match uses the
ratings after all earlier matches, as in the use of the model in practice. The predictions are therefore

                                                     3
out-of-sample with respect to both the parameters and the results of the matches being predicted. The
parameters are not re-estimated during the test seasons, which makes the reported metrics conservative
for all models. The national teams are evaluated separately (Section 5.8).
    The metrics are computed on the outcome after 90 minutes (win, draw or loss), which is defined
for every match. All matches are weighted equally in the test metrics, without the weights and the
discounting used in the estimation of the Glicko parameters (Section 4.4).
    The ratings published with this paper are computed with the parameters re-estimated on all seasons,
so that the most recent seasons, which matter most for the current strength of the teams, also contribute
to the parameters. The two sets of parameters are compared in Section 5.6.

2.3    Approaches

There are two effective approaches to predicting soccer match outcomes. The first approach is based
on predicting the number of goals each team will score and translating these goal expectations into
probabilities of a win, draw, or loss. The second approach relies on rating systems to quantify team
strength, in which the probabilistic nature is embedded in the model formulation. Consequently,
probabilities of a win, draw, or loss arise directly from the rating dynamics. We discuss both approaches
in sections 3 and 4, respectively.

3     Approach 1: Match Outcome Prediction via Goal Expectations

3.1    Idea

This approach leverages a widely recognized concept for forecasting soccer match results, focusing on
predicting the number of goals each team will score against its respective opponent. We assume that
the number of goals in soccer approximately follows a Poisson distribution [2]. We then translate these
goal expectations into outcome probabilities.

3.2    Implementation

Gradient boosting models have demonstrated impressive performance when applied to tabular data
[5]. Consequently, we constructed a machine learning model utilizing the LightGBM [6] framework
to predict the goal count for both competing teams. We also experimented with the CatBoost [7]
model; however, it yielded inferior results. Since the goals in soccer approximately follow a Poisson
distribution, we set the LightGBM parameter objective to poisson. We note, however, that empirical
goal distributions deviate from the strict Poisson assumption. This limitation is addressed later through
model refinements.
    The goal models (LightGBM and CatBoost, with the same features) predict the expected number of
goals of each team in a match. Each row of the training set corresponds to one participant of a match,
so every match gives two rows. The model uses 52 features listed in Table 3. The rolling statistics are
computed over the last 5, 10, 20 and 30 matches of the team (one feature per window) with at least 3,
5, 10 and 20 matches, respectively; otherwise the feature is missing.
    Matches with extra time last 120 minutes instead of 90. Where the score after 90 minutes is known,
the goal model is trained on it. For the other matches with extra time, the final score is used with an
offset: the model expects 1.38 times more goals than in 90 minutes. The ratio 0.38 of the goals of extra
time to the goals of a regular match is estimated from the data: 1.02 goals are scored in extra time
against 2.69 in an average match (12,898 matches with extra time and the scores by period, including
the lower divisions and cups that are not part of the dataset). Per minute, more goals are scored in
extra time than in an average match (3.05 against 2.69 per 90 minutes). The prediction for every
match is the expected number of goals in 90 minutes, and the expected number of goals in extra time
is 0.38 of it.




                                                   4
Table 3: Features of the gradient boosting models (LightGBM and CatBoost) that predict the expected number of
goals of a team in a match. Every row of the training set is a pair (match, team), so every match gives two rows.
Venue: in the last home matches for a home match and in the last away matches for an away match

 Group               Features
 Venue               venue (+1 home, 0 neutral, −1 away); no spectators; limited number of spectators; home
                     match at a different stadium; match during the COVID-19 pandemic
 Stage               extra time possible
 Schedule            days since the previous match; matches played in the season; both for the team and for
                     the opponent
 Competition         league of the team and of the opponent; tournament; tournament type (first league,
                     second league, cup, super cup, international cup, international super cup, national team
                     qualification, national team final tournament); league level difference (+1, 0, −1)

 Group               Rolling statistic                          Mean      Median      Max           Windows
 Form                goals scored                                  •                              5, 10, 20, 30
                     goals conceded                                •                              5, 10, 20, 30
                     goals scored by the opponent                  •                              5, 10, 20, 30
                     goals conceded by the opponent                •                              5, 10, 20, 30
                     goals scored, same tournament type            •                              5, 10, 20, 30
 Venue form          goals scored at the venue                     •         •          •        5, 10, 20, 30;
                                                                                                      max: 10
                     goals conceded at the venue                   •         •                    5, 10, 20, 30

3.3   Outcome Probabilities via the Skellam Distribution

The Poisson assumption, together with the assumption of independence between the goal-scoring
processes of the two teams, allows us to use the probability mass function associated with the Skellam
distribution:
                                                              µ k         √
                            p(k, µ1 , µ2 ) = exp(−(µ1 + µ2 ))( 1 ) 2 Ik (2 µ1 µ2 )                           (1)
                                                              µ2
    In equation (1), Ik is the modified Bessel function, and k represents the score difference in a soccer
match. If k > 0, the value of the probability mass function corresponds to the probability of the first
team winning; for k = 0, it gives the draw probability; and if k < 0, it provides the probability of the
second team winning. The parameters µ1 and µ2 are the means of two Poisson-distributed random
variables. In our case, µ1 and µ2 are the expected goals of the two teams predicted by the gradient
boosting model.

3.4   Score Matrix Models

While the Skellam distribution provides a direct way to compute win, draw, and loss probabilities from
goal expectations, it does not explicitly represent the full joint distribution of possible scorelines. To
obtain a more detailed description of match outcomes, we construct a score probability matrix.
    Let p(i, j) denote the probability that the home team scores i goals and the away team scores j
goals. The collection of probabilities {p(i, j)} forms a two-dimensional matrix representing the joint
distribution of match scores. In practice, the infinite support of goal counts must be truncated for
computational purposes. We approximate the joint distribution by constructing a 15 × 15 score matrix
corresponding to goal counts from 0 to 14 for each team. For typical goal expectations observed in
professional soccer, the probability of exceeding this range is negligible; the matrix is subsequently
renormalized so that the total probability mass equals one.
    Outcome probabilities are then computed by summing over appropriate regions of this matrix:



                                                       5
                                                     X
                                             pH =          p(i, j),
                                                     i>j
                                                     X
                                             pD =          p(i, j),
                                                                                                        (2)
                                                     i=j
                                                     X
                                              pA =         p(i, j).
                                                     i<j

    This matrix-based formulation offers several advantages. First, it provides the complete distribution
over scorelines rather than only the score difference. Second, it allows flexible modeling of dependence
structures between the two teams’ goal processes. Third, the outcome probabilities of all score-matrix
models below are computed in the same way, by Eq. (2), so the models differ only in how the matrix is
constructed.
    In the following subsections, we describe three alternative constructions of the score matrix.

3.5   Score Matrix under Independent Poisson Assumption

The simplest approach assumes that the number of goals scored by the home and away teams follows
independent Poisson distributions with means µ1 and µ2 , respectively.
    Let xi = p(Ghome = i) and yj = p(Gaway = j) denote the corresponding Poisson probabilities. Under
the independence assumption, the joint score probability is given by

                                               p(i, j) = xi yj .                                        (3)

3.6   Dixon–Coles Score Matrix

Although the independent Poisson model provides a convenient baseline, empirical soccer data reveal
dependence between the goal-scoring processes of the two teams, particularly in low-scoring matches.
The independent model tends to underestimate the probabilities of low-scoring draws such as (0, 0) and
(1, 1). To account for this, we adopt the Dixon–Coles adjustment [2]. Starting from the independent
Poisson construction given in Equation (3), the probabilities of specific low-score outcomes are modified.
    The Dixon–Coles model introduces a dependence parameter ρ that adjusts the probabilities as
follows:

                                     p(0, 0) ← p(0, 0) (1 − µ1 µ2 ρ),
                                     p(0, 1) ← p(0, 1) (1 + µ1 ρ),
                                                                                                        (4)
                                     p(1, 0) ← p(1, 0) (1 + µ2 ρ),
                                     p(1, 1) ← p(1, 1) (1 − ρ).
    All other scoreline probabilities remain unchanged. After applying the correction factors, the score
matrix is renormalized to ensure that the total probability sums to one.
    When ρ = 0, the model reduces to the independent Poisson formulation. The parameter is estimated
on the validation set of the goal model by a grid search with the step 0.001 (Section 5.2): ρ = −0.060.

3.7   Markov Score Matrix

The Poisson and Dixon–Coles matrices describe only the final score. In a real match, however, the
scoring rate of a team depends on the current score: a leading team tends to defend, and a trailing
team takes more risk. Following the birth process model of Dixon and Robinson [8], we describe a
match as a sequence of goals: the score starts at 0–0, and from every score each team scores at its own
rate, which depends on the goal difference. Unlike the original model, which estimates the strength of
the teams itself and is fitted on the times of the goals, we use it as a layer on top of the goal model: the
base rates of the two teams are the expected goals of LightGBM, and only the dependence on the score
is estimated, from the final outcomes.


                                                      6
   From a score (i, j) the home team scores with the rate λhome (i, j) and the away team with the rate
λaway (i, j):
                              λhome (i, j) = µhome mscore (d) mlow (i, j),
                                                                                                   (5)
                              λaway (i, j) = µaway mscore (−d) mlow (i, j),
where d = i − j is the goal difference, capped at ±3, mscore (d) is the multiplier of a team leading by d
goals (d < 0: trailing by |d| goals), mscore (0) = 1, and mlow (i, j) adjusts the low scores in the spirit of
Dixon–Coles, scaled by µhome µaway :

                                             mlow (0, 0) = 1 + a00 µhome µaway ,
                              mlow (1, 0) = mlow (0, 1) = 1 − a10 µhome µaway ,                              (6)
                                             mlow (1, 1) = 1 + a11 µhome µaway ,

mlow (i, j) = 1 for the other scores. The score matrix p(i, j) is the distribution of the state of the chain at
the end of the match, the matrix exponential of the generator (transition rate) matrix built from these
rates. With mscore ≡ 1 and mlow ≡ 1 the chain reduces to the independent Poisson matrix.
    The multipliers change not only the shape of the score distribution but also the total number of
goals. Since the expected goals are taken from LightGBM, we rescale the base rates so that the chain
produces the same expected goals as LightGBM, and the Markov layer changes only the shape of the
distribution.
    The nine parameters are estimated on the validation set of the goal model (Section 5.2) by
minimizing the outcome log loss; Table 4 shows the estimates. A one-goal lead makes the leading team
score less and the trailing team score more, a strong comeback effect, in agreement with Dixon and
Robinson [8]; with a three-goal lead the effect reverses (Table 4). Part of the reason is that the match
is effectively decided, but a three-goal lead is also a selected state: it often arises when something went
wrong for the trailing team, such as a red card or a collapse of the team, which is not in the expected
goals before the match and keeps acting until the end of the match.
    The estimates should be read as the direction and the approximate size of the effects rather than as
precise values. The loss changes very little with the parameters, since different combinations of them
give almost the same probabilities of a win, a draw and a loss, and large goal differences are rare. With
the minutes of the goals, as used by Dixon and Robinson [8], the time spent at every score and the
goals scored from it would be observed directly, and the multipliers would be identified much better.
Table 4: Fitted parameters of the Markov score matrix, Eq. (5): the scoring rates of the leading and the trailing
team relative to the base rates of the goal model, and the low-score adjustments

      Goal         Leading team               Trailing team
 difference    Multiplier     Change      Multiplier     Change     Interpretation
       1            0.800     −20.0%           1.205       +20.5%   leader defends, trailer attacks
       2            0.960       −4.0%          0.930       −7.0%    both teams score less
       3            1.230     +23.0%           0.855       −14.5%   match decided; red cards
 Low-score adjustments: a00 = 0.025, a10 = 0.085, a11 = 0.040



4     Approach 2: Match Outcome Prediction Using Modified Glicko

4.1    Rating Systems

Rating systems such as Elo [3], Glicko [9], and TrueSkill [10] have been widely applied to measure
competitor strength in head-to-head games and sports. These systems were originally designed for
competitions with binary outcomes (win or loss). Most implementations treat ties as equivalent to
half a win and half a loss, ignoring the fact that draw probabilities may depend not only on the
difference in competitor strengths. However, their direct application to team sports such as soccer
presents significant challenges, as standard rating models do not account for crucial sport-specific


                                                       7
factors, including home-field advantage, roster changes due to player transfers, and strength-dependent
draw probabilities.
    In soccer, the occurrence of draws introduces additional complexity that classical rating systems
cannot naturally accommodate. Empirical evidence suggests that draw probabilities depend not only
on the relative strength difference between teams, but also on their absolute strength levels and goal-
scoring tendencies. Recently, Glickman [4] extended paired comparison models to incorporate strength-
dependent tie probabilities in chess, recognizing that draws become more likely when competitors are
closely matched in skill, and that stronger players are more likely to draw than weaker players. This
development provides a principled foundation for adapting rating systems to soccer, where draws are
similarly common and influenced by both team strengths.
    In our previous work [11], we adapted the Glicko-2 model to soccer by incorporating draw
probabilities, home-field advantage, and rating adjustments for league transitions. Building on these
developments and Glickman’s recent advances, we now adopt the strength-dependent draw framework
from [4], extending it to account for goal-scoring tendencies—a soccer-specific factor where high-
scoring teams produce fewer draws than low-scoring teams (Fig. 1). This relationship is consistent with
the nature of goal-scoring in soccer: teams with lower expected goal rates are more likely to remain at
0-0, thereby increasing the overall probability of a draw, while high-scoring teams generate more total
goals, reducing the likelihood that both teams finish with identical scores.
                                           Away goals                                                                      Away goals
                    0           1          2         3          4            5                      0           1          2         3          4            5


             0    11.1        12.2        6.7       2.5        0.7          0.1                0   4.1         6.5        5.2       2.8        1.1          0.4



             1    12.2        13.4        7.4       2.7        0.7          0.2                1   6.5        10.4        8.3       4.5        1.8          0.6



             2     6.7         7.4        4.1       1.5        0.4          0.1                2   5.2         8.3        6.7       3.6        1.4          0.5
Home goals




                                                                                  Home goals




             3     2.5         2.7        1.5       0.5        0.1          0.0                3   2.8         4.5        3.6       1.9        0.8          0.2



             4     0.7         0.7        0.4       0.1        0.0          0.0                4   1.1         1.8        1.4       0.8        0.3          0.1



             5     0.1         0.2        0.1       0.0        0.0          0.0                5   0.4         0.6        0.5       0.2        0.1          0.0



                         (a) both teams expect 1.1 goals, P(draw) = 29.1%                                (b) both teams expect 1.6 goals, P(draw) = 23.4%
                                                                home win           draw                  away win



Figure 1: Score probabilities (%) for two equally strong teams under independent Poisson goals: (a) both teams
expect 1.1 goals, (b) both teams expect 1.6 goals. Home wins are shown in blue, draws (the diagonal) in orange
and away wins in purple, darker for more probable scores. The teams are equal in both cases, but the draw
probability falls from 29.1% to 23.4% as the expected number of goals grows.

    Furthermore, we incorporate league-specific characteristics and dynamic rating adjustments follow-
ing promotion or relegation. Our approach enables cross-league comparisons and provides interpretable
ratings that can be applied to player evaluation, transfer analysis, and match outcome prediction across
diverse competitive environments.

4.2              Glicko with Strength-Dependent Draws

The Glicko model represents competitor strength as a probability distribution. Each team is initially
associated with a normal prior distribution characterized by a mean rating µ and uncertainty (rating
deviation) ϕ. As match outcomes accumulate, ratings are updated via Bayesian inference toward a


                                                                                  8
posterior distribution. When a team wins, its rating increases; the magnitude of this increase is primarily
determined by two factors: the difference in ratings (larger upsets produce larger adjustments) and
rating uncertainty (teams with limited match history experience larger changes).
    Recent work by Glickman [4] extends paired comparison models to address two critical limitations
of classical rating systems. First, order effects such as home-field advantage (analogous to the white
piece advantage in chess) systematically favor one competitor. Second, the probability of a draw
depends not only on the strength difference between competitors, but also on their absolute strength
levels—stronger pairs are more likely to draw.
    The original formulas are given below:

                                                                       θ +θ
                                                                            
                                              exp θi + 14 xij α0 + α1 · i 2 j
                             P(Yij = 1) =                                                              (7)
                                                              Dij
                                                                       θ +θ
                                                                            
                                              exp θj − 14 xij α0 + α1 · i 2 j
                             P(Yij = 0) =                                                              (8)
                                                                 Dij
                                                                  θ +θ
                                                                        
                                              exp β0 + (1 + β1 ) · i 2 j
                             P(Yij = 21 ) =                                                            (9)
                                                           Dij

   where
– θi , θj are the ratings of team i (home) and team j (away);
– xij is the venue: 1 home, 0 neutral, −1 away for team i;
– α0 , α1 are the baseline and the strength-dependent home advantage;
– β0 , β1 are the baseline and the strength-dependent draw probability;
– Dij is the sum of the three numerators.
                θ +θ
    The term i 2 j represents the average strength of both teams. In Equations (7)–(8), this term
modulates the home-field advantage: the parameter α1 allows the advantage to vary with team quality.
In Equation (9), the coefficient (1 + β1 ) determines how draw probability changes with absolute team
strength.

4.3     Custom Extensions of Glicko-2

4.3.1    Modified Outcome Probability Function

We modify the original probability specification by (i) incorporating expected goals into both the order
effect and the draw component, and (ii) decomposing the baseline order effect into a crowd-related
term and a logistic (travel) term. Let gij denote the scoring intensity of the match: the sum of the
expected goals of the two teams from the goal model (Section 3), clipped at its 99.9% quantile for
numerical stability and centered at its mean over the club matches.
    The match outcome probabilities are defined as:

                                                                    θ +θ
                                                                                  
                                exp θi + xij αcrowd + αlogistic + α1 i 2 j + α2 gij
                   P(Yij = 1) =                                                        ,              (10)
                                                       Dij

                                                                    θ +θ
                                                                                  
                                exp θj − xij αcrowd + αlogistic + α1 i 2 j + α2 gij
                   P(Yij = 0) =                                                        ,              (11)
                                                       Dij

                                               θ +θ
                                                              
                                    exp β0 + β1 i 2 j + β2 gij
                   P(Yij = 12 ) =                                  .                                  (12)
                                                Dij

   Here, xij indicates venue, αcrowd and αlogistic jointly determine the baseline home advantage, α1
captures strength-dependent order effects, and α2 introduces a scoring-intensity adjustment. The draw

                                                       9
component is governed by β0 (baseline draw frequency), β1 (strength dependence), and β2 (scoring
dependence).
    The separation between αcrowd and αlogistic is identifiable due to the COVID-19 period, during which
matches were played without spectators. While the crowd-related component was effectively removed,
travel-related disadvantages remained, providing natural variation that allows the two effects to be
estimated separately. Beyond the pandemic period, match-level annotations from Flashscore—such
as “Limited number of spectators” or “Playing home matches at a different stadium”—enable further
fine-tuning of these parameters. Specifically, the crowd component is set to zero for matches without
spectators and halved for matches with a limited number of spectators; for a home match at a different
stadium, the crowd component is halved and the travel component is set to zero, since in this case both
teams usually travel to the venue (a simplification: the alternative stadium is sometimes close to the
home city). At a neutral venue, the home advantage is zero, and the draw component uses the average
of the parameters of the leagues of the two teams.

4.3.2   Rating Initialization

The Glicko model depends only on rating differences; adding a constant to all ratings does not affect
predicted match outcomes. To enable cross-league comparability, we introduce an additional parameter
referred to as the initial league rating, which represents the average strength level of a league. While
this parameter does not affect predictions within a single national championship, it plays a crucial role
when comparing teams across different leagues, particularly in international competitions.
    Every club starts with the initial rating of its league, µ = µinit , and the initial rating deviation
ϕ0 = 250. The initial league rating is used only when the league itself appears in the dataset (or the
club appears in its first season in the dataset). Later, the initial rating of a club that enters a league is
determined by the clubs it replaces, which keeps the level of the league stable (Section 4.3.4):
                 
                 µ + µlift or µ − µlift if the club was promoted or relegated (Eq. (16)),
                 
            µ = µleavers + µnew            if the club has no matches in the previous season,           (13)
                 
                   µinit                   in the first season of the league.
                 

A club without matches in the previous season is reinitialized even if earlier history exists: for example,
a club that played in the second division in 2013/2014, was relegated to the third division (not in the
dataset) and returned in 2015/2016 starts the 2015/2016 season from the anchor of Eq. (17), and its
rating deviation is reset to ϕ0 .
     For leagues that appear only after the training seasons, the parameters are the medians over the
fitted first or second divisions; for leagues of countries with fewer than 30 international matches,
the initial rating is additionally capped at 1400, below the mean rating of 1500: their level cannot
be identified from the data, and leagues with little international history are, as a rule, weaker than
average.

4.3.3   Mid-Season

As in Glicko, the matches are grouped into rating periods: the ratings and rating deviations are updated
once per period, using all matches of the period together. The rating periods are the calendar quarters,
which gives 107 periods between 2000 and 2026 and about ten matches of a team per period in a
typical league. The length of the period is a hyperparameter: shorter periods update the ratings more
often but with less information per update, longer periods react more slowly to changes of form. For
the predictions, the ratings within a period are updated after every match in the order of the dates
(Section 2.2), so the length of the period affects the official update of the ratings but not the timeliness
of the predictions.
    Team strength changes over time, gradually during a season and abruptly at the season transition,
when the rosters change in the transfer window. Both are modeled by the growth of the rating deviation.
Before every rating period (a quarter of a year), the rating deviation of a team grows as in Glicko,
                                                q
                                           ϕ ← ϕ2 + ϕ2period ,                                          (14)

                                                     10
as long as ϕ is below the threshold of 120. At the season transition, it additionally grows by ϕseason ,
and a team that changes its division also changes its rating by µlift :
                 (
                  r(µ ± µlift , ϕ + ϕseason ) if the team was promoted (+) or relegated (−),
      r(µ, ϕ) ←                                                                                   (15)
                  r(µ, ϕ + ϕseason )          otherwise.

The parameter µlift ≥ 0 is estimated for every country and captures the tendency of promoted clubs
to strengthen (the budget typically increases after promotion) and of relegated clubs to weaken. The
growth ϕseason has two global values, one for the first and one for the second divisions, since the rosters
of second-division clubs change more between seasons (per-league values did not improve the model,
Section 5.10); the estimates are given in Section 5.6.
    Another source of inflation is the change in the number of teams of a league, for example after
a reform of its format. It is handled by the same mechanism: the newcomers start from the ratings
of the clubs they replace, or, in an expansion of the league, from a low quantile of the ratings of the
continuing clubs (Section 4.3.4).

4.3.4   Preventing Rating Inflation at League Transitions

Matches within a league are almost zero-sum: the rating gained by one team is lost by its opponent.
The levels of the leagues are therefore determined by two sources: international matches and the rating
that enters or leaves a league at the season transitions. If the transitions systematically add rating to a
league, the league is inflated, and since most leagues play few international matches, the inflation is
not corrected by the data.
    In the earlier version of the model [12], promotion and relegation had separate parameters,
estimated independently for every league. Such parameters are poorly identified within a single league,
and the estimates of some leagues added more rating to promoted teams than was taken from relegated
teams. As a result, the total rating of these leagues grew from season to season, and their clubs were
overrated in international competitions. The imbalance of a single transition is small, but it is repeated
at every season transition, and over the 25 seasons of the dataset it accumulates into a noticeable drift
of the level of the league. The effect resembles exploding and vanishing gradients in deep and recurrent
neural networks, where a small deviation at every step is compounded over a long sequence of steps. A
similar imbalance exists in the FIFA ranking of national teams: matches decided by a penalty shoot-out
are scored as 0.75 for the winner and 0.5 for the loser, so such a match adds 1.25 instead of 1 to the
total score of the two teams, and the teams that often reach the knockout stages accumulate points in
excess of their results.
    In the proposed model, the transition between the first and the second division of a country is
governed by a single parameter µlift ≥ 0, estimated for the first division: a promoted team gains µlift ,
and a relegated team loses the same amount,

                       µ ← µ + µlift (promotion),        µ ← µ − µlift (relegation).                  (16)

When the numbers of promoted and relegated teams are equal, the transitions do not change the total
rating of the two divisions of the country.
    A team that enters a league without a match history in the previous season (for example, after a
few seasons in the third division, which is not in the dataset) starts from the mean current rating of the
teams that left the league at the same transition, plus a global offset µnew :

                                          µ = µleavers + µnew .                                       (17)

If the league has no leavers (e.g. an expansion of the league), the starting rating is the 10% quantile of
the ratings of the continuing teams, and in the first season of a league, the initial league rating µinit .
The offset is positive (µnew = 90): at the moment of leaving, the ratings of the leavers are too low
because of regression to the mean and the collapse of some clubs (financial problems, the departure of
key players, administrative relegation), so the newcomers start above them. Since a newcomer replaces
a leaver, the total rating of the league changes only by the offset. One value is used for all leagues
(Section 5.10).

                                                    11
    The offset slightly increases the total rating of a league at every transition. We also tested a stricter
version, in which the continuing teams of the league give up the same total amount, so the total rating
of the league is preserved exactly. This version made the predictions worse for the newcomers, the
relegated teams and the international matches (Section 5.5), so it is not used. The reason is that exact
conservation is only needed where nothing else anchors the level of a league. In leagues connected
to other leagues by international matches, the ratings of the continuing teams are already corrected
by these matches, and an additional downward shift only distorts them. The small inflation from the
newcomer offset matters only for isolated leagues with few international matches, whose level is in any
case less reliable (Section 4.5). The goal of the model is therefore not an exactly constant total rating,
but the absence of a systematic drift that the data cannot correct: the large imbalance of separate
promotion and relegation parameters is removed, while the small, justified offset of the newcomers is
kept.

4.3.5    Extra Time

In single-leg knockout matches and in the second legs of two-legged ties with a level aggregate score, a
draw after 90 minutes is often followed by extra time. Such matches are rare (9,122 club matches,
0.75% of the dataset, and 252 national team matches, 2.0%), but they are the playoffs of the most
important tournaments, where an accurate assessment of the strongest teams matters most. We treat
extra time as a second stage of the match with its own outcome (win, draw or loss in extra time), which
enters both the rating update and the loss function in the same way as the outcome of the regular
time. Penalty shootouts directly after 90 minutes, in competitions without extra time (2,142 matches,
identified by the scores by period), are draws of the regular time without the extra time stage.
    Extra time is described by the same outcome model as the regular time, applied to a shorter game,
rather than by a separate model. The only question is how the parameters of the outcome model
change when the game lasts 30 minutes instead of 90. A shorter game contains fewer goals, so the
outcome depends less on the difference in strength and more on chance. In the model, this corresponds
to a contraction of the rating scale by a factor κ: the ratings enter the outcome probabilities as κθ, and
κ = 1 recovers the regular time. Similarly, the home advantage of the league is scaled by a factor sET ,
and the draw component, which describes the probability that 30 minutes end without a decisive goal,
has its own parameters β0ET , β1ET , β2ET . All five parameters are common for all leagues, since extra time
is played in only a few matches per league, and they are estimated from the data together with the
other parameters of the model:
                                                                           θ +θ
                                                                                        
               P(YijET = 1) ∝ exp κθi + xij sET αcrowd + αlogistic + α1 i 2 j + α2 gET ij     ,         (18)
                                                                           θ +θ
                                                                                        
               P(YijET = 0) ∝ exp κθj − xij sET αcrowd + αlogistic + α1 i 2 j + α2 gET ij    ,          (19)
                                                     θ +θ
                                                                   
               P(YijET = 21 ) ∝ exp β0ET + β1ET κ i 2 j + β2ET gET
                                                                 ij   ,                                 (20)

where gET
        ij is the expected number of goals in extra time: the expected number of goals of 90 minutes
multiplied by 0.38 (Section 3). A match with extra time thus acts as two games: a draw of the regular
time, which updates the ratings as any other draw, and a short second game, whose result moves the
ratings κ times less than an equally surprising result of a regular match. The parameters of extra time
are estimated after the parameters of the leagues; the estimates are given in Table 5.
    With the estimated parameters (κ = 0.76, sET = 0.58), a draw is by far the most likely outcome of
extra time, and the difference in strength and the home advantage matter much less than in regular
time (Table 10).

4.4     Parameter Estimation

The parameters of the model are listed in Table 5. They are of two kinds: the parameters of a league
are estimated separately for every first and second division, and the global parameters are common
for all leagues. The transition parameter µlift is estimated for the first division of every country and
applies to both of its divisions. The offset of the newcomers is not estimated but set to µnew = 90:

                                                    12
newcomers play a small share of the matches, so the loss hardly changes with this value. Instead, the
value is checked by the calibration: in their first season in the league, the newcomers score as expected
by the model (+0.006 per match, Table 9). The table gives the estimates on all seasons, which are
used for the published ratings; the estimates on the training seasons, used for the evaluation, are close
to them (Section 5.6).
Table 5: Parameters of the model and their estimates on all seasons. League: estimated for every league (253
leagues: 165 first and 88 second divisions); country: for every country (165 countries); global: once for all
leagues; fixed: set without estimation by the model. For the league and country parameters, the mean over the
leagues and, in brackets, the standard deviation

 Parameter                 Estimate      Description
 League
 µinit                    1330 (253)     initial rating of the league
 αcrowd                0.101 (0.068)     home advantage: crowd
 αlogistic             0.119 (0.067)     home advantage: travel
 α1                    0.004 (0.009)     home advantage: strength of the teams
 α2                   −0.022 (0.019)     home advantage: expected goals
 β0                   −0.245 (0.069)     draws: baseline
 β1                    1.009 (0.012)     draws: strength of the teams
 β2                   −0.495 (0.023)     draws: expected goals
 Country
 µlift                    37.6 (12.9)    rating change at promotion and relegation
 Global
 ϕperiod                          14     growth of ϕ per rating period
 ϕseason                          16     growth of ϕ per season, first divisions
 ϕseason                          34     growth of ϕ per season, second divisions
 κ                               0.76    extra time: scale of the ratings
 sET                             0.58    extra time: scale of the home advantage
 β0ET                            1.01    extra time: draws, baseline
 β1ET                            1.00    extra time: draws, strength of the teams
 β2ET                          −1.63     extra time: draws, expected goals
 Fixed
 µnew                             90     rating offset of the newcomers
                                    4    rating periods per year (calendar quarters)
 γ                               0.95    discount of the loss per rating period
 w                                  4    loss weight: continental club competitions
 w                                10     loss weight: FIFA Club World Cup
                                 0.38    goals of extra time, share of a regular match (from the data)

    The parameters are constrained to the values that have a meaning: the crowd and travel components
of home advantage are non-negative, since playing at home is not expected to be a disadvantage, and
the two components are separated only by the matches without spectators, so without the constraint
one of them could become negative and be compensated by the other; promoted clubs do not become
weaker (µlift ≥ 0); and the uncertainty added at the season transition, with the changes of the rosters,
is not smaller than that of a rating period during the season (ϕseason ≥ ϕperiod ≥ 0). The constraints
mainly restrict the search to the meaningful region and speed up the estimation: the estimates of
almost all leagues lie inside this region anyway (Table 5).
    All parameters are estimated by minimizing the loss function described below with coordinate
descent. The parameters of a single league change the loss only slightly, so a direct per-league search is

                                                     13
slow and stops at plateaus. The estimation therefore goes from the most general parameters to the most
specific ones: the global parameters, shifts of each parameter shared by all leagues, the level of each
country (the initial ratings of its two divisions shifted together, since their gap is fixed by domestic cups
and only international matches decide the level), the parameters of each league, and the parameters
of extra time. The exact procedure is given in the code5 . Finally, all initial ratings are shifted by a
common constant so that the mean rating of the active clubs equals 1500, which does not change the
predictions.
    The choice of the loss function follows from the purpose of the ratings. The goal is not only to
predict individual matches well, but to estimate the current strength of clubs and leagues on a common
scale, which is what the applications require (player evaluation, transfers, comparison of leagues). A
model can predict domestic matches almost perfectly and still place the leagues at wrong levels relative
to each other, so the loss is designed to emphasize the matches that carry information about the levels
of leagues and the recent matches that carry information about the current strength.
    The loss function is a weighted sum of the log losses of individual matches. Each match is weighted
by the type of competition and by its age:
                                                        
                                                        1,
                                                               domestic match,
                          T−t
                   X           X
              L=        γ            wm ℓm ,     wm = 4,        continental club competition,            (21)
                   t>t0
                                                        
                              m∈Mt                      
                                                           10, FIFA Club World Cup,

where Mt is the set of matches of the rating period t, T is the last rating period, ℓm is the log loss of
match m (including the extra time stage), and γ is the discount factor.
    The weights of international matches compensate for their small number. International matches
make up less than 3% of the dataset, but they are the only source of information about the relative
levels of the countries: the levels of the leagues do not affect the predictions of domestic matches
(Section 4.3.4). Without the weights, the estimation is dominated by domestic matches, and a league
whose clubs are systematically over- or underrated in international competitions costs only a small
amount of the loss. The Club World Cup has the largest weight, since it is the main source of matches
between confederations. The weights are used only for the estimation of the parameters: all reported
test metrics are computed with equal weights, so that they are comparable with the metrics of the other
models.
    The discount factor gives more weight to recent seasons, since the goal of the ratings is the current
strength of the teams, and the parameters of the leagues change over time: home advantage, for
example, has decreased over the last two decades (Fig. 2). A season contains four rating periods, and
we use γ = 0.95 per rating period, which corresponds to a half-life of about 13.5 rating periods, or
about 3.4 seasons. The first t0 = 8 rating periods (two seasons) are excluded from the loss, since the
ratings are not yet established.
    Home advantage decreased from about 0.65 points per match in the early 2000s to about 0.49
in 2018, fell to 0.36 in the 2020 season, when most matches were played without spectators (in the
top 5 European leagues, where almost the whole season was played in empty stadiums, to 0.15), and
has recovered only partly since then (0.39 in 2025). Home advantage in soccer has been documented
for a long time [13], and part of it is attributed to the pressure of the crowd on the referees: referees
favour the home team less when the crowd noise is absent [14] or the stadium is empty [15], and the
decline in 2017–2019 coincides with the introduction of the video assistant referee (VAR) in the top
European leagues. However, the decline is visible in the second divisions as well, where VAR is mostly
not used, so we do not attribute it to VAR. Whatever the causes, home advantage is not constant over
time, which is another reason to discount older matches. A model with constant parameters estimated
on the whole history would therefore overestimate home advantage in the current seasons, which is
another reason to discount older matches.
    Although it may be theoretically appealing to assign team-specific parameters—incorporating factors
such as stadium capacity, geographic distance between cities, or other determinants of home advan-
tage—such an approach substantially increases model complexity and typically results in overfitting.
  5
   https://github.com/andreyshelopugin/SportsRatings/blob/main/soccer/club_ratings/train_glicko.py,
method TrainGlicko.fit.


                                                     14
Home minus away points per match
                                   0.7
                                   0.6
                                   0.5
                                   0.4
                                   0.3
                                   0.2        All leagues
                                              First divisions
                                   0.1        Second divisions
                                              Top 5 European leagues                 VAR in top leagues        COVID-19
                                   0.0
                                      2000            2005                 2010             2015                2020      2025
                                                                              Season (start year)
       Figure 2: Home advantage by season: the mean difference between the points of the home and the away team
       per match (3 for a win, 1 for a draw, after 90 minutes) in domestic league matches, with 95% intervals, and
       separately for the first divisions of England, Spain, Germany, Italy and France (top 5; about 1,800 matches
       per season, the interval of about ±0.12 is not shown). The darkness of the band of a season is the share of its
       matches played during the COVID-19 pandemic (13% in 2019, 93% in 2020, 9% in 2021). The dotted line marks
       the introduction of VAR in the top European leagues (2017/2018–2019/2020)

                                   The complete estimation pipeline of the clubs is shown in Figure 3 in Appendix A.

       4.5                          League Ratings

      The rating of a league is computed from the current ratings of its clubs as a weighted mean of the
      ratings of the eight strongest clubs:
                                                                      P8
                                                                       k=1 wk µ(k)
                                                          Rleague =    P8            ,     wk = 1.1 − 0.1 k,                (22)
                                                                           k=1 wk

      where µ(k) is the rating of the club ranked k-th in the league, so the weights decrease from 1 for the
      strongest club to 0.3 for the eighth. The number eight is the size of the smallest leagues in the dataset,
      so every league is measured by the same number of clubs. The decreasing weights reflect the fact that
      the level of a league is perceived mainly through its strongest clubs, which represent the league in the
      continental competitions. At the same time, unlike the UEFA coefficient, the rating takes into account
      the whole upper half of a typical league, not only the clubs that play in international competitions.
           The model places all leagues on one scale, but the precision of the level of a league depends on how
      strongly it is connected to the other leagues. A league that regularly plays in continental competitions
      is anchored by hundreds of matches, while the level of an isolated league is inferred mainly from
      its initialization and from a few matches of its clubs. Even a few matches against other leagues or a
      few promoted and relegated teams link a league to the common scale, which is the purpose of the
      model. A league without any of these links over the last three seasons, however, keeps the level of its
      initialization. Such leagues (6 of 250: the first divisions of Bermuda, Macao, Palestine, Sri Lanka and
      Yemen, and the second division of Mexico, which has no promotion to the first division) are rated by
      the model, but are not shown in Table 12. The same holds for a country as a whole: the two Russian
      divisions are linked to each other, but their clubs have played almost no international matches since
      2022, so the level of the country is not identified and the Russian leagues are not shown either. The
      weighted top-8 is not the only reasonable definition of the strength of a league, and the best definition
      depends on the task. For the assessment of a transfer from a top club, the rating of the strongest clubs
      is more relevant; for the evaluation of a typical player of the league, the mean or the median over all
      clubs may be more appropriate. Since the ratings of all clubs are available, any such aggregate can be


                                                                                    15
computed directly; the tables of the repository also include the means of the top 5, top 7 and top 10
clubs and the ratings of the clubs by position.
   The ratings of the leagues and clubs after the 2025/2026 season are given in Tables 12 and 13, with
the strongest club, the median club and the standard deviation (SD) over all clubs. The aggregates
can rank leagues differently. The Saudi Pro League is ahead of the Brazilian Serie A by the weighted
top 8 (2093 against 2067) and by the mean of the top 5 clubs (2141 against 2083), since its strongest
clubs are stronger. The Brazilian league, however, is much more even (standard deviation 89 against
189), and its median club is stronger by 120 points (1940 against 1820), so a typical match in Brazil is
played at a higher level.

5     Experimental Results

All results are computed on the held-out seasons according to the protocol of Section 2.2.

5.1    Metrics

Let pm,k be the predicted probability of the outcome k ∈ {H, D, A} of match m, and ym,k = 1 if the
outcome occurred and 0 otherwise. The main metric is the outcome log loss, the mean of the binary
log losses of the three outcomes:
                                 N
                              1 X X                                           
                    LL = −           ym,k log pm,k + (1 − ym,k ) log(1 − pm,k ) ,                  (23)
                             3N
                                m=1 k

which is also the loss used in the estimation of the Glicko parameters, so the values are directly
comparable across all models. We also report the multiclass Brier score
                                                 N
                                            1 XX
                                     BS =       (pm,k − ym,k )2                                    (24)
                                            N
                                              m=1 k

and the ranked probability score (RPS), which takes into account the order of the outcomes (a home
win is closer to a draw than to an away win) [16]:
                                             N       2     2
                                      1 X XX
                               RPS =         (pm,k − ym,k ) ,                                      (25)
                                     2N
                                            m=1 r=1       k≤r

where the outcomes are ordered as H, D, A. Lower values are better for all three metrics.

5.2    Comparison of Score Matrix Models

The score-matrix models serve as baselines that share the goal model and differ only in how the goal
expectations are converted into outcome probabilities. Since all of them use the same expected goals,
the comparison isolates this last step and can be viewed as an ablation of the structure of the score
distribution.
    The parameters of the score-matrix models (ρ of Dixon–Coles and the nine parameters of the Markov
model) are estimated with the expected goals of LightGBM as inputs. They are fitted on a held-out
10% of the training seasons (90,979 matches), on which LightGBM was not trained (these matches
were used only for early stopping). As in stacking, the second-level model is fitted on predictions for
new data, as it is used in practice, rather than on the training matches of the first-level model.
    We compare three such models: the Skellam probabilities (independent Poisson goals), the Dixon–
Coles matrix and the Markov score matrix (Table 6).
    The independent Poisson score matrix (Eq. (3)) gives the same probabilities as the Skellam distribu-
tion up to the truncation of the matrix, so it is not reported separately.
    The Dixon–Coles and Markov models achieve slightly lower loss than the independent Poisson
model on club matches: the Dixon–Coles correction reduces the loss by 0.00026 and the Markov model

                                                         16
Table 6: Score matrix models on the test seasons (90 minutes): outcome log loss of clubs (311,166 matches),
national teams (3,897) and all matches, Brier score and RPS of all matches. All models use the same goal
expectations of LightGBM. Bold: the best value in a column

 Model                                      Clubs        National          All        Brier         RPS
 Skellam (independent Poisson)           0.583899        0.518382   0.583089      0.596645      0.203256
 Dixon–Coles                             0.583638        0.518363   0.582831      0.596330      0.203203
 Markov                                  0.583569        0.517802   0.582756      0.596266      0.203189

by 0.00033. For national teams, the differences are of the same size or smaller than the noise of a
sample of 3,897 matches. Overall, the structure of the score distribution matters much less than the
goal expectations themselves.

5.3   Comparison with the Baselines

As a baseline rating model we use the classical Elo rating [3] with home advantage and the draw
probabilities of Davidson [17]:
                                           √
                  qi           qj         ν qi qj
         P(H) = , P(A) = , P(D) =                 ,     qi = 10(ri +hxij )/400 , qj = 10rj /400 , (26)
                  D            D             D
where D normalizes the probabilities, and the ratings are updated after every match by K times the
difference between the actual and the expected score. As usual for Elo, all clubs start from the same
rating. The parameters are estimated by a grid search on the training seasons (K from 10 to 50, h from
40 to 160 and ν from 0.6 to 1.1), which gives K = 35, h = 100 and ν = 0.8; none of the estimates lies
at the boundary of the grid.
    Table 7 compares all models on the club matches of the test seasons, separately for domestic and
international matches. For each model, the last column gives the difference in log loss between the
modified Glicko model and the model, with a 95% interval from a paired bootstrap over matches (1,000
resamples); a negative difference means that Glicko is better.
    The modified Glicko model is clearly better than Elo in all groups of matches. Over all matches and
over domestic matches, it is as accurate as the score-matrix models: the intervals of the differences in
log loss include zero, and by the Brier score and the RPS it is the best single model over all matches.
Both approaches are built on the same matches, so the comparable accuracy is expected. The difference
is in what else they give: the rating model also gives a single interpretable number for every club,
comparable across leagues and seasons, together with its uncertainty.
    In international matches, however, the modified Glicko model is substantially more accurate than
all baselines: its log loss is lower by about 0.009 than that of the score-matrix models and by 0.043
than that of Elo, with intervals far from zero. International matches are the matches in which the levels
of different leagues meet, and they are exactly the matches that the league-aware components of the
model are designed for. The goal model describes the scoring of a team by its recent matches, which
are mostly played within its own league, so it does not know how strong the league is; Elo, with the
same initial rating for all clubs, does not know it either. The ablation below attributes the advantage to
the league-aware initialization.
    The test metrics are computed without the weights of international matches and without the
discounting used in the estimation of the Glicko parameters (Section 4.4), so the Glicko model is
evaluated by a criterion it does not optimize, while the score-matrix models are fitted on the same
criterion they are evaluated by. The comparison is therefore conservative for the rating model.
    Finally, the average of the probabilities of the modified Glicko and the Markov models is the best
model in all groups, with a large and significant gain over each of them in domestic matches. The two
approaches use different information: the rating summarizes the whole history of results and the levels
of the leagues, while the goal model describes the recent scoring of the teams. In international matches,
the average is as accurate as Glicko alone, since the information about the levels of the leagues comes
from the rating.



                                                    17
Table 7: Club matches of the test seasons (90 minutes): outcome log loss, Brier score and RPS. ∆: log loss of the
modified Glicko model minus log loss of the model, with a 95% paired bootstrap interval (negative: Glicko is
better). Glicko + Markov is the average of the probabilities of the two models. Bold: the best model in a group;
in international matches, the modified Glicko model and Glicko + Markov do not differ significantly, and both
are bold

 Model                               Log loss            Brier           RPS                 ∆ [95% interval]
 All matches (311,152)
 Elo                                 0.591105       0.606114        0.207224      −0.0075 [−0.0079, −0.0070]
 Skellam                             0.583895       0.597624        0.203627       −0.0002 [−0.0007, 0.0002]
 Dixon–Coles                         0.583634       0.597304        0.203573         0.0000 [−0.0004, 0.0005]
 Markov                              0.583565       0.597245        0.203561         0.0001 [−0.0004, 0.0005]
 Modified Glicko                     0.583646       0.596989        0.203507                                  –
 Glicko + Markov                     0.580274       0.593186        0.201684          0.0034 [0.0031, 0.0036]
 Domestic matches (301,671)
 Elo                                 0.590887       0.605871        0.206943      −0.0063 [−0.0067, −0.0059]
 Skellam                             0.584536       0.598446        0.203853         0.0000 [−0.0004, 0.0004]
 Dixon–Coles                         0.584256       0.598101        0.203795         0.0003 [−0.0001, 0.0007]
 Markov                              0.584202       0.598058        0.203791         0.0003 [−0.0001, 0.0008]
 Modified Glicko                     0.584546       0.598129        0.203889                                  –
 Glicko + Markov                     0.581084       0.594223        0.202018          0.0035 [0.0032, 0.0037]
 International matches (9,481)
 Elo                                 0.598042       0.613843        0.216154      −0.0430 [−0.0469, −0.0392]
 Skellam                             0.563512       0.571475        0.196416      −0.0085 [−0.0114, −0.0056]
 Dixon–Coles                         0.563853       0.571947        0.196495      −0.0088 [−0.0119, −0.0060]
 Markov                              0.563290       0.571379        0.196254      −0.0083 [−0.0113, −0.0054]
 Modified Glicko                     0.555016       0.560713        0.191361                                  –
 Glicko + Markov                     0.554494       0.560188        0.191027         0.0005 [−0.0010, 0.0020]




                                                       18
5.4   Ablation

To measure the contribution of the components of the model, we switch them off one at a time
and compute the test loss (Table 8). In the version without refit, the other parameters are kept as
estimated; in the version with refit, the global parameters and the parameters shared by the leagues
are re-estimated on the training seasons without the component, so that the other parameters can
compensate for it; the parameters of the individual leagues are kept as estimated.
Table 8: Ablation: increase of the test log loss of the modified Glicko model (club matches, 90 minutes) when
one component is switched off. Without refit: the other parameters are fixed; with refit: the global and shared
parameters are re-estimated without the component

                                                Without refit                         With refit
 Switched off                             All    Domestic        Intern.        All   Domestic        Intern.
 Home advantage                       0.0097        0.0094       0.0189     0.0096       0.0094       0.0181
 League-aware initialization          0.0018        0.0005       0.0443     0.0019       0.0006       0.0433
 Scoring dependence (α2 , β2 )        0.0021        0.0021       0.0018     0.0019       0.0019       0.0018
 Season growth of ϕ                   0.0013        0.0014      −0.0008     0.0013       0.0014      −0.0010
 Newcomer offset µnew                 0.0003        0.0003       0.0001     0.0003       0.0003      −0.0002
 Promotion/relegation µlift           0.0000        0.0000       0.0000     0.0001       0.0001      −0.0001

    The league-aware initialization hardly matters for domestic matches, where the level of the league
cancels out, but without it the loss of international matches increases by 0.044, about the same as
the gap between Glicko and Elo in these matches. The advantage of the proposed model over Elo
in international matches is therefore due to the initialization of the clubs at the level of their league.
Home advantage is the most important component overall. The dependence of home advantage and of
draws on the expected goals reduces the loss by about 0.002 in all groups; since the strength of the
teams is already in the model, this is information that the ratings do not contain, which answers the
question whether the expected goals are redundant given the ratings (stronger teams also score more).
The season growth of the rating deviation helps in domestic matches and slightly hurts in international
ones. The newcomer offset and the promotion/relegation adjustment hardly change the loss: their
role is not the accuracy of individual matches but the stability of the levels of the leagues over time
(Section 4.3.4), which is checked by the calibration below. The refit changes the effects only slightly:
the other parameters compensate for a removed component only to a small extent, so the contributions
without refit are not exaggerated.

5.5   Calibration of League Levels

Log loss measures the quality of predictions over all matches, but it says little about whether the levels
of different leagues are consistent with each other. Most matches are played within a single league,
so a league that is rated too high or too low as a whole may cost only a small amount of log loss. We
therefore complement log loss with a calibration check.
    For every match, the expected score of a team is computed from the pre-match outcome probabilities
of the model,
                                    E[score] = P(win) + 12 P(draw),                                   (27)
and compared with the actual score (1, 0.5 or 0). The difference between the actual and the expected
score is averaged over groups of matches; if the model is calibrated for a group, the average difference
is close to zero. The standard deviation of the score in a single match is √ about 0.44, so for a group of n
matches the noise level of the average difference is approximately 0.44/ n, for example 0.044 for 100
matches.
     We consider two types of groups. The first are the teams in their first season after a league transition
(promoted, relegated, new in the league, or remaining in the same league), in domestic matches since
2010. These groups check the rules of Section 4.3.4. The second are the leagues in international club
matches: if a league is underrated, its clubs score more in international competitions than the model

                                                       19
expects. This is the most direct test of the levels of the leagues. Since international matches also enter
the loss function with large weights, we perform this test on the test seasons: the parameters are
estimated on the seasons before 2021, and the predictions are the sequential predictions of Section 2.2,
so the matches being checked were not used in any way.
    The results are given in Table 9. Teams that remain in their league, promoted teams and newcomers
are well calibrated. Relegated teams score slightly less than expected in their first season in the lower
league (−0.021 per match).
    In the international matches of the test seasons, the mean absolute difference over the 142 leagues
with at least 20 matches is 0.042, while the noise alone gives about 0.040 for a perfectly calibrated
model (the mean absolute value of a normal variable is 0.8 of its standard deviation). The difference
exceeds two noise levels in 4.2% of the leagues, as expected by chance. The leagues with the most
international matches are calibrated within about one noise level (Brazil +0.002, Argentina +0.018,
England +0.022, Spain −0.024, Germany +0.008). Some of the largest deviations follow from changes
of the level of a league. Gradual changes of the level of a league are followed by the ratings, but sudden
changes are followed with a delay, since the level of a league is corrected only by its international
matches. The Saudi Pro League (+0.051) has become much stronger since 2023, when its clubs started
to sign star players, and the Ukrainian league (−0.082) has become weaker since 2022, when many
players left the country and the clubs started to play their home matches abroad. The deviations of the
Asian leagues (Japan +0.111, about 3 noise levels, and Iran −0.050) are not related to such changes
and are left for future work (Section 6).
Table 9: Calibration of the modified Glicko model: actual minus expected score per match (win 1, draw 0.5, loss
0). Transitions: domestic matches since 2010. Leagues: international club matches of the test seasons, predicted
with the parameters estimated before 2021: the four leagues with the most matches and the leagues with the
largest deviations, and the
                         √ mean over all 143 leagues with at least 20 matches (the full table is in the repository).
The noise level is 0.44/ n. I: first division

 Group                                                        Matches       Actual − Expected              Noise
 First season after a transition
 Same league                                                 1,061,062                     0.001            0.000
 Promoted                                                       71,462                     0.000            0.002
 Relegated                                                      59,648                    −0.021            0.002
 New in the league                                             176,116                     0.006            0.001
 International matches of the test seasons, selected leagues
 Brazil I                                                          853                     0.002            0.015
 Argentina I                                                       603                     0.018            0.018
 England I                                                         450                     0.022            0.021
 Spain I                                                           411                    −0.024            0.022
 Japan I                                                           181                     0.111            0.033
 Saudi Arabia I                                                    196                     0.051            0.031
 Iran I                                                            120                    −0.050            0.040
 Ukraine I                                                         160                    −0.082            0.035
 Mean |difference|, 142 leagues                                                            0.042            0.040



5.6   Estimated Parameters

The estimates of all parameters are given in Table 5. They are stable: the estimates on the training
seasons and on all seasons are close (for example, the mean crowd component 0.119 and 0.101, the
draw baseline −0.265 and −0.245, µlift 29 and 38, and the initial ratings of the leagues differ by 12
points on average).
   The league parameters are interpretable. The median home advantage αcrowd + αlogistic is 0.22 in


                                                        20
the first divisions and 0.23 in the second divisions. Among the leagues with at least 1,000 matches,
it is the largest in Nigeria (1.00 in the first division and 0.87 in the second), followed by Bosnia and
Herzegovina, Algeria, Guatemala and Ghana (about 0.6). Draws are the most frequent, relative to the
strength and the expected goals of the teams, in El Salvador, the United Arab Emirates, Iran and the
Italian Serie B, and the least frequent in the second divisions of Bosnia and Herzegovina and Albania
and in Kazakhstan. The parameters of small leagues stay close to their starting values, since a single
league changes the loss only slightly, so they should not be interpreted.
     The extra time parameters show what changes in a short game after a level score. The difference in
strength matters less (κ = 0.76). This is partly a selection effect rather than a property of extra time:
extra time follows a draw, which is evidence that the teams were closer on the day than their ratings
suggest. The home advantage is about 60% of that in regular time (sET = 0.58), and the large draw
baseline reflects the fact that 40% of extra time periods end without a goal. The mechanism of draws
is the same as in regular time: per unit of the expected goals of 90 minutes, the effect of scoring on
draws is −1.63 · 0.38 = −0.62 in extra time and −0.50 on average in regular time, and the effect of
strength is the same (β1ET = 1.00 and β1 = 1.01).

5.7   Interpretation of Ratings

The ratings have a direct probabilistic interpretation: Table 10 gives the outcome probabilities for a
given rating difference.
Table 10: Outcome probabilities (%) by the rating difference between the stronger and the weaker team, at a
neutral venue and at the home stadium of the stronger team (parameters of the English Premier League, a match
with the average expected number of goals)

           Rating                  Neutral venue                        Home of the stronger team
       difference           Win           Draw            Loss           Win           Draw           Loss
 Regular time
                0           36.5           27.1           36.5           44.4           26.6           29.0
                10          37.5           27.1           35.4           45.5           26.5           28.0
                50          41.8           26.9           31.3           49.8           25.9           24.4
              100           47.2           26.3           26.5           55.0           24.8           20.2
              200           57.7           24.1           18.2           64.8           21.9           13.4
              300           67.1           21.0           11.9           73.0           18.5            8.5
              500           81.2           14.3            4.6           84.8           12.1            3.1
 Extra time
                0           21.1           57.9           21.1           23.7           57.7           18.6
                10          21.5           57.9           20.6           24.2           57.6           18.1
                50          23.4           57.7           18.8           26.3           57.2           16.5
              100           26.0           57.3           16.7           29.0           56.5           14.6
              200           31.4           55.6           13.0           34.6           54.2           11.2
              300           37.2           52.9           10.0           40.5           51.0            8.5
              500           49.3           45.2            5.5           52.7           42.7            4.6



5.8   National Teams

The national teams are rated by the same model as the clubs, with the confederations in place of the
leagues: a team enters with the initial rating of its confederation, and the levels of the confederations
are estimated from the matches between them, mainly at the World Cup. The host of a final tournament
is treated as the usual home team, and the other matches of a final tournament are played at a neutral
venue. The home advantage parameters are global (Section 5.10). In the loss, the matches of the


                                                     21
World Cup final tournaments have weight 3, the matches of the other final tournaments weight 2, and
the qualifiers and the Nations Leagues weight 1. As for the clubs, the rating periods are the calendar
quarters; since national teams do not play in every quarter, the rating deviation grows in proportion to
the time between two periods with matches, and there is no additional growth at season transitions.
Extra time is modelled as for the clubs (Section 4.3.5). The pipeline is shown in Figure 4.
    The parameters are estimated on the matches before 2021 and evaluated on the matches since 2021
(the qualifiers for the 2022 World Cup and later), with sequential predictions as for the clubs. Elo is
estimated in the same way as for the clubs (Section 5.3); the grid search gives K = 80, h = 100 and
ν = 0.7, so the ratings of national teams, which play only a few matches per year, change faster than
those of the clubs (K = 35). Table 11 compares the models on the 3,637 matches that are in the test
sets of all models. The goal model of the baselines is split by season, so its training data include a few
final tournaments played in 2021 (for example, Euro 2020), which, if anything, favours the baselines.
Table 11: National teams, test matches since 2021 (90 minutes): outcome log loss, Brier score and RPS. ∆: log
loss of the modified Glicko model minus log loss of the model, with a 95% paired bootstrap interval (negative:
Glicko is better). Final tournaments: the World Cup and the continental championships

 Model                              Log loss           Brier           RPS                ∆ [95% interval]
 All matches (3,637)
 Elo                                0.510621       0.509617       0.168752      −0.0106 [−0.0145, −0.0063]
 Skellam                            0.519458       0.519064       0.174164      −0.0194 [−0.0251, −0.0134]
 Dixon–Coles                        0.519460       0.519140       0.174176      −0.0194 [−0.0252, −0.0134]
 Markov                             0.518880       0.518611       0.173952      −0.0188 [−0.0248, −0.0127]
 Modified Glicko                    0.500060       0.496356       0.163617                                 –
 Glicko + Markov                    0.501617       0.497917       0.164305       −0.0016 [−0.0046, 0.0015]
 Final tournaments (592)
 Elo                                0.581951       0.594969       0.191977      −0.0373 [−0.0530, −0.0202]
 Skellam                            0.581367       0.595744       0.195374      −0.0367 [−0.0542, −0.0189]
 Dixon–Coles                        0.580276       0.594539       0.195173      −0.0356 [−0.0532, −0.0176]
 Markov                             0.580249       0.594666       0.195150      −0.0356 [−0.0534, −0.0173]
 Modified Glicko                    0.544675       0.547217       0.172870                                 –
 Glicko + Markov                    0.551509       0.556765       0.177274       −0.0068 [−0.0157, 0.0026]

    For national teams, the modified Glicko model is significantly more accurate than all baselines,
by about 0.019 in log loss than the score-matrix models and by 0.011 than Elo. Unlike for the clubs,
the score-matrix models are less accurate than Elo, and the average with the Markov model does not
improve on Glicko alone. The gap is the largest in the final tournaments (0.036), where teams of
different confederations meet; the ablation below attributes it to the levels of the confederations, as the
advantage in international club matches is attributed to the levels of the leagues.
    The ablation confirms this. Without the levels of the confederations (all teams start from the same
rating), the test loss increases by 0.007 over all matches and by 0.028 in the final tournaments; with
a refit of the other parameters, by 0.004 and 0.021, so the other parameters cannot compensate for
the levels. Without home advantage, the loss increases by 0.003 (0.003 with a refit), mostly in the
qualifiers, where every match has a host. The dependence on the expected goals adds 0.004 without a
refit but almost nothing with a refit (0.0004), since the draw parameters take over its role.
    The estimated initial levels of the confederations relative to Europe are +415 for South America,
−295 for Africa, −653 for Asia, −700 for North and Central America and −1153 for Oceania. The
ratings after the 2026 World Cup (Table 14) are led by Spain (2421), Argentina (2345), France (2321)
and England (2274), the same four teams as at the top of the FIFA ranking. The largest differences
from the FIFA ranking concern the hosts of the 2026 World Cup and the Asian teams, which are lower
in our ratings (Mexico 19th, Japan 27th, the USA 34th): for the hosts, one reason is that a large part of
their recent results was obtained at home, and the model, unlike the FIFA ranking, discounts the home


                                                     22
advantage. Another difference is that the FIFA ranking also counts friendly matches, which are not in
our data.

5.9    Application: League Ratings in Player Performance Prediction

Consider, for instance, our objective to predict various player metrics for the upcoming season, such
as the number of goals a specific player will score. To make accurate predictions, we can take into
account factors like player age, position, previous performance, and the number of goals scored in
the previous season, along with other relevant features. However, a significant challenge arises when
a player undergoes transfers, moving to a different club or league during their career. How can we
effectively inform the model about such transitions?
    One possible solution involves introducing a categorical feature, such as "player transfers from the
Denmark Superliga to France Ligue 1." Nonetheless, this approach encounters the curse of dimensional-
ity—there are relatively few transfers between these two leagues, making it challenging for the model
to train effectively. A more viable approach, which aligns with our method, is to generate numeric
features. For example, we can create a feature that quantifies the difference in ratings between the
Denmark Superliga and France Ligue 1. This enables the model to account for league transitions more
effectively. Features of this kind were used to forecast the impact of a transfer, with the strength of
the clubs and leagues measured by Elo ratings [18], and to predict the expected possession value of
players in the next season [19].
    The ratings can also be used to evaluate the difficulty of a schedule. The expected number of points
of a team over a sequence of matches, computed from the ratings of the opponents and the venues,
measures how demanding a period of the season is. Combined with the dates of the matches, this
allows clubs to plan the rotation of players (load management): for example, to rest key players in
matches against weaker opponents between two difficult matches, or to estimate the cost of a congested
period with several strong opponents in a row.
    Additionally, we can enhance the precision of player performance analysis, particularly within the
context of a single team. For instance, we can calculate the average rating of the opposing teams
faced by each player. This fine-grained analysis helps differentiate player performances, as several
players may exhibit similar statistics, but the strength of the opponent teams they encounter can vary
significantly.

5.10    Negative Results

Several variants of the model were tested and did not improve it, so they are not used:
– separate parameters of promotion and relegation for every league (as in the earlier version of the
  model [12]) inflated the levels of some leagues and were replaced by the single parameter µlift
  (Section 4.3.4);
– a stricter version of the newcomer rule, in which the continuing teams of a league pay the offset of
  the newcomers, made the calibration of the newcomers, the relegated teams and the international
  matches worse (Section 4.3.4);
– ϕseason estimated for every league: the loss was almost flat in this parameter, and the only systematic
  difference was between the first and the second divisions, so two global values are used;
– the offset of the newcomers µnew estimated for every league: a single league changes the loss by less
  than one unit, so the values are not identifiable;
– the volatility of Glicko-2, an individual speed of the rating of every team, changed the loss only
  marginally, for the clubs as well as for the national teams;
– for the national teams, rating periods that follow their calendar (every international window and
  every match day of a final tournament as a separate period) gave the same test loss as the calendar
  quarters;
– for the national teams, parameters for every country (home advantage and initial rating, as offsets to
  the global and confederation values) overfitted the training matches and did not reduce the test loss;
– for the national teams, a larger home advantage of the host of a final tournament (about 2.5 times
  the usual one) made the test loss worse, so the host is treated as a usual home team;


                                                   23
– for the national teams, weights of the rating update by the importance of the match (as the K-factor
  of the World Football Elo ratings) and a lower weight of the matches in which a team has already
  qualified (dead rubbers) did not reduce the test loss;
– for the national teams, scaling the rating change by the goal difference did not improve on a uniformly
  larger rating change.
    Some choices were not tuned and are left for future work. For the clubs, only the calendar quarters
were used as rating periods. The weights of international matches in the loss (4 for the continental
competitions and 10 for the Club World Cup) and the discount factor γ = 0.95 were set by judgement
rather than estimated (Table 5), and the parameters are estimated once rather than in an expanding
window (Section 6).

6   Discussion

The primary limitation of the proposed framework is its reliance exclusively on match outcomes. As
a result, the model implicitly assumes that team strength evolves smoothly over time. In practice,
however, roster composition can change substantially during the season, particularly in second-tier
leagues where transfers and financial instability are more common. Such structural breaks are only
partially captured through seasonal and mid-season adjustments.
    The dataset spans six confederations, providing broad global coverage. However, direct inter-
continental competition remains relatively rare. Until 2025, matches between clubs from different
confederations were limited to a few matches of the FIFA Club World Cup per year. The expanded Club
World Cup of 32 clubs (since 2025) and, within Europe, the Conference League (since 2021/2022)
substantially increase the number of matches that connect leagues of different levels and continents,
and we expect the cross-confederation levels to become more reliable as these tournaments accumulate.
At present, the sparse cross-confederation interaction still reduces the amount of information available
to anchor ratings across regions and introduces additional uncertainty when comparing clubs from
different continents; for national teams, the same role is played by the World Cup.
    At the same time, the reliance on match outcomes makes the model undemanding: it requires only
the results of matches and a small amount of metadata (the venue, the type of competition, the league
of each club), which are available for almost every professional league in the world. This is what makes
a worldwide coverage possible, since richer data such as expected goals or player-level data exist only
for a small number of top leagues. Where such data are available, the model is easy to extend. In
an earlier experiment, for example, we replaced the actual outcome of a match with the outcome by
expected goals (xG) [20], that is, the win was credited to a team whose xG exceeded the xG of the
opponent by more than 0.5, and the match was counted as a draw otherwise. More generally, any
signal that can be expressed as an outcome or as an adjustment of the scoring intensity can enter the
model without changing its structure.
    The framework is not specific to soccer. Its components (strength-dependent draws, home advantage,
a scoring intensity from a goal or points model, league-aware initialization and transitions between
divisions) apply to any team sport with a league structure, promotion and relegation or international
club competitions. Basketball, handball, volleyball and ice hockey have national leagues of very different
levels connected by continental competitions, and the same problem of cross-league comparison arises
there. Sports without draws (e.g. basketball) simplify the model, while sports with overtime or
shoot-outs (e.g. ice hockey) can reuse the extra time stage. Adapting the model to other sports is a
natural direction for future work, and the repository is designed to host ratings for other sports as well.
    The gain of the average of the Glicko and the Markov models suggests that the two approaches
capture different aspects of team strength. A natural next step is to analyze in which matches each of
them is more accurate (for example, by the history of the teams, the gap between their strengths, the
time since a transfer window, or the stage of the season) and to use these findings to build a single
model that combines the stable league-aware ratings with the short-term information of the goal model,
rather than averaging the predictions of two separate models.
    In the evaluation, the parameters are estimated once on the seasons before 2021 and are not
updated during the five test seasons. In practice, they would be re-estimated regularly, for example


                                                    24
before every season. An expanding-window evaluation, in which the parameters are re-estimated
before every test season on all earlier seasons, would show the accuracy of the model as it is used in
practice and how quickly the parameters become outdated.
    The collected data contain the scores by period for about two thirds of the matches with extra
time, but not the minutes of the goals. With the minutes, the scoring rates of the Markov model at
every score could be identified much better. Collecting the minutes of the goals is planned for the next
version of the dataset.
    The international matches of some leagues are not calibrated as well as those of the others: the
clubs of Japan win more often than the model predicts, and the clubs of Iran less often (Section 5.5).
Whether these deviations come from the data or from the model remains to be checked.
    Despite these constraints, the proposed framework remains computationally efficient and relies
solely on publicly available data. While alternative probabilistic score-distribution models yield only
marginal performance differences, the modified Glicko framework consistently improves predictive
accuracy and provides interpretable ratings that can be directly applied to downstream analytical tasks.




                                                  25
A   The Pipeline of the Rating Estimation



                                                     Match data
                                   results of first and second divisions, domestic cups
                                   and continental competitions, venue and spectators
                                   outcome after 90 minutes, extra time, venue status


                                                     Goal model
                         LightGBM on the recent goals of the teams, the venue and the competition
                                              expected goals of both teams


                                                 Scoring intensity
                              sum of the expected goals of both teams, clipped and centered
                                                            gij



                                             Parameter estimation
                               coordinate descent on the weighted log loss of the matches:
                               international matches weighted up, older periods discounted

                                                 Modified Glicko
                           rating updates: league-aware initialization, promotion and relegation,
                           newcomers, growth of the rating deviation per period and per season
                                                 ratings μi, deviations ϕi



                                             Outcome probabilities
                               home advantage (crowd, travel), strength-dependent draws,
                                     scoring intensity, extra time as a second stage
                                                 win, draw, loss; log loss

                                          global, country and league parameters



                                                    Club ratings
                                    ratings of the clubs with the estimated parameters
                                                club ratings and deviations


                                                  League ratings
                               weighted mean rating of the eight strongest clubs of a league
                                                      league ratings



                 Figure 3: The pipeline of the estimation of the club and league ratings




                                                            26
                                   Match data
                   World Cup and continental final tournaments,
                     their qualifiers and the Nations Leagues
              outcome after 90 minutes, extra time, host, neutral venue


                                   Goal model
        the same LightGBM model, trained on club and national team matches
                            expected goals of both teams


                              Scoring intensity
           sum of the expected goals of both teams, clipped and centered
                                          gij



                           Parameter estimation
             coordinate descent on the weighted log loss of the matches:
               final tournaments weighted up, older periods discounted

                               Modified Glicko
             rating updates: initialization at the level of the confederation,
          growth of the rating deviation with the time between rating periods
                                 ratings μi, deviations ϕi



                          Outcome probabilities
          home advantage of the host, neutral venues of final tournaments,
             strength-dependent draws, extra time as a second stage
                             win, draw, loss; log loss

                 global parameters and levels of the confederations



                           National team ratings
             ratings of the national teams with the estimated parameters
                     ratings and deviations of the national teams



Figure 4: The pipeline of the estimation of the national team ratings




                                          27
B       Ratings of Leagues, Clubs and National Teams

The ratings after the 2025/2026 season and the 2026 World Cup, computed with the parameters
estimated on all seasons. The full tables are available in the repository.

Table 12: Ratings of the first and second divisions after the 2025/2026 season: the weighted mean of the eight
strongest clubs, Eq. (22). The stripe: the confederation ( UEFA CONMEBOL AFC CAF CONCACAF OFC); SD:
the standard deviation of the club ratings (darker: less even); n: the number of clubs; Int: the matches of the
clubs of the league against foreign clubs in the last three seasons; the bar: from the median club to the strongest
one, the dot: the league rating; the history of the league rating since 2016, relative to the world mean of every
season; the strongest club and its world rank. Not shown: 6 leagues without matches against other leagues and
without promotion or relegation in the last three seasons (Section 4.5) and the Russian leagues

    # League                Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
    1    England I          2441     118   20 214                                            Arsenal (2)

    2    Spain I            2361     133   20 191                                            Barcelona (3)

    3    Germany I          2345     153   18 173                                            Bayern Munich (1)

    4    Italy I            2332     153   20 176                                            Inter (7)

    5    France I           2283     141   18 155                                            PSG (6)

    6    Portugal I         2183     185   18 131                                            Benfica (17)

    7    Turkey I           2103     137   18 106                                            Galatasaray (38)

    8    Belgium I          2100     137   16 108                                            Club Brugge KV (37)

    9    Saudi Arabia I     2093     189   18   97                                           Al Hilal (33)

 10      Netherlands I      2083     159   18 136                                            PSV (30)

 11      Brazil I           2067     89    20 352                                            Palmeiras (60)

 12      England II         2057     91    24    2                                           Ipswich (94)

 13      Greece I           2045     176   14 106                                            Olympiacos Piraeus (57)

 14      Spain II           2040     88    22    0                                           Racing Santander (104)

 15      Japan I            2033     71    17   94                                           Kashima Antlers (81)

 16      Denmark I          2007     121   12   80                                           Midtjylland (74)

 17      Mexico I           1992     122   18 165                                            Cruz Azul (124)

 18      Czech Republic I   1992     146   16 112                                            Slavia Prague (64)

 19      Italy II           1970     103   20    0                                           Venezia (121)

 20      Norway I           1969     120   16   92                                           Bodo/Glimt (75)

 21      Argentina I        1969     88    30 280                                            River Plate (165)

 22      Poland I           1966     74    18   96                                           Lech Poznan (155)

 23      Germany II         1956     81    18    0                                           Paderborn (185)

 24      Austria I          1954     105   12   91                                           Sturm Graz (145)

 25      Switzerland I      1952     96    12   88                                           Lugano (209)

 26      Israel I           1948     137   14   50                                           H. Beer Sheva (125)

 27      Morocco I          1943     115   16   82                                           FAR Rabat (135)

 28      USA I              1936     89    30 186                                            Inter Miami (189)

 29      Iran I             1933     108   16   57                                           Tractor (167)

 30      France II          1931     92    18    1                                           Le Mans (204)

 31      Sweden I           1928     104   16   92                                           Mjallby (164)

 32      Egypt I            1924     132   21   93                                           Pyramids (140)

 33      Romania I          1922     116   16   66                                           Univ. Craiova (184)

 34      Cyprus I           1918     193   14   92                                           Omonia (159)

 35      Ukraine I          1909     169   16   68                                           Shakhtar Donetsk (76)

 36      UAE I              1903     168   14   81                                           Shabab Al Ahli Dubai (158)

 37      Scotland I         1898     142   12   88                                           Celtic (103)



                                                               28
 # League              Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
38   South Korea I     1898     70    12   75                                           Jeonbuk (192)

39   Algeria I         1894     104   16   86                                           MC Alger (190)

40   Paraguay I        1878     98    12 118                                            Cerro Porteno (211)

41   Croatia I         1870     133   10   56                                           Din. Zagreb (101)

42   Ecuador I         1867     114   16 121                                            Ind. del Valle (175)

43   South Africa I    1851     139   16   79                                           Mamelodi Sundowns (122)

44   Colombia I        1850     102   20 115                                            Atl. Nacional (279)

45   Brazil II         1844     109   20    0                                           Sao Bernardo (348)

46   Bulgaria I        1833     157   16   62                                           Levski Sofia (270)

47   Turkey II         1831     119   20    0                                           Erzurumspor (352)

48   Tunisia I         1830     165   16   53                                           Esperance Tunis (160)

49   Hungary I         1824     127   12   64                                           Ferencvaros (153)

50   Chile I           1824     101   16 133                                            Coquimbo (350)

51   Qatar I           1813     119   12   74                                           Al Sadd (222)

52   Australia I       1811     82    12   38                                           Auckland FC (390)

53   Iraq I            1806     137   20   30                                           Al Shorta (322)

54   Slovenia I        1799     141   10   78                                           Celje (280)

55   Uruguay I         1790     89    16 118                                            Penarol (355)

56   Japan II          1787     100   20    0                                           V-Varen Nagasaki (399)

57   Serbia I          1782     157   16   58                                           Crvena zvezda (118)

58   Azerbaijan I      1776     177   12   56                                           Qarabag (234)

59   China I           1775     115   16   65                                           Chengdu Rongcheng (386)

60   Slovakia I        1774     116   12   52                                           Slovan Bratislava (295)

61   Saudi Arabia II   1767     156   18    0                                           Al Diriyah (427)

62   Thailand I        1763     147   16 114                                            Buriram (252)

63   Bahrain I         1763     177   14   23                                           Al Muharraq (306)

64   Belgium II        1760     151   17    0                                           Beveren (245)

65   Uzbekistan I      1753     142   16   30                                           Neftchi Fargona (432)

66   Algeria II        1748     154   32    0                                           El Biar (408)

67   Portugal II       1746     71    18    0                                           Torreense (592)

68   Poland II         1745     98    18    8                                           Wisla (466)

69   Argentina II      1744     77    36    0                                           Deportivo Moron (707)

70   Costa Rica I      1733     123   10   68                                           Saprissa (507)

71   Greece II         1729     187   20    0                                           Kalamata (351)

72   Zimbabwe I        1720     123   18    8                                           Scottland (450)

73   Peru I            1718     125   18 116                                            Alianza Lima (476)

74   Jordan I          1718     209   10   29                                           Al Hussein (318)

75   Ghana I           1716     77    18   14                                           Medeama (794)

76   Romania II        1714     154   22    6                                           Sepsi Sf. Gheorghe (618)

77   Kazakhstan I      1706     116   16   51                                           Kairat Almaty (601)

78   DR Congo I        1694     177   30   46                                           Mazembe (382)

79   Belarus I         1693     160   16   38                                           Din. Minsk (524)

80   South Korea II    1687     136   17    0                                           Suwon Bluewings (805)

81   Switzerland II    1686     129   10    6                                           Aarau (639)

82   Vietnam I         1680     113   14   47                                           Cong An Ha Noi (675)

83   Zambia I          1680     117   18   26                                           Power Dynamos (483)

84   Paraguay II       1680     125   16    0                                           Benjamin Aceval (765)



                                                          29
  # League                 Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
85    Bolivia I            1678     112   15 104                                            Bolivar (588)

86    Finland I            1678     126   12   48                                           KuPS (629)

87    Indonesia I          1673     117   18   41                                           Persib Bandung (631)

88    Bosnia and Herz. I   1672     176   10   52                                           Borac Banja Luka (405)

89    Libya I              1671     197   36   18                                           Al Ahly Tripoli (581)

90    Angola I             1671     168   16   46                                           Petro Atletico (326)

91    Lebanon I            1671     200   12   10                                           Al Ansar (457)

92    Syria I              1668     168   16    4                                           Al Ittihad Aleppo (660)

93    Oman I               1666     143   14   12                                           Al Seeb (419)

94    Senegal I            1666     88    16   16                                           Teungueth (946)

95    Kosovo I             1665     82    10   44                                           Drita (754)

96    Iran II              1662     132   18    0                                           Nassaji Mazandaran (883)

97    Tanzania I           1661     221   16   64                                           Young Africans (256)

98    Mali I               1660     137   14   36                                           Djoliba (623)

99    Uganda I             1659     156   16    8                                           Vipers (573)

100   Kuwait I             1658     220   10   22                                           Al (271)

101   Ivory Coast I        1658     83    16   46                                           ASEC Mimosas (680)

102   Ghana II             1656     121   48    0                                           Port City (695)

103   Honduras I           1652     145   11   40                                           Olimpia (511)

104   Netherlands II       1648     104   20    0                                           Den Haag (783)

105   Morocco II           1645     90    16    0                                           Widad Temara (841)

106   Cameroon I           1645     100   14    8                                           Colombe (745)

107   Denmark II           1638     126   12    0                                           Lyngby (915)

108   USA II               1637     112   25    0                                           Louisville City (911)

109   Panama I             1634     93    12   28                                           Plaza Amador (741)

110   Malaysia I           1634     232   13   59                                           Johor DT (130)

111   Venezuela I          1634     108   14   92                                           Carabobo (985)

112   Ireland I            1632     99    10   60                                           Shamrock Rovers (830)

113   Armenia I            1628     200   10   56                                           Noah (594)

114   Norway II            1628     102   16    0                                           Kongsvinger (926)
115   Australia II         1626     190   16    0                                           South Melbourne (541)

116   Guatemala I          1625     94    12   41                                           Municipal (732)

117   Israel II            1620     79    16    0                                           Maccabi Petah Tikva (977)

118   Albania I            1620     70    10   30                                           AF Elbasani (1027)

119   Sweden II            1619     93    16    0                                           Norrkoping (953)

120   Ecuador II           1612     80    12    0                                           Atletico FC (1006)

121   Georgia I            1606     108   10   26                                           Iberia 1999 (948)

122   Austria II           1605     90    16    0                                           Admira (1138)

123   Barbados I           1602     185   10    4                                           Weymouth Wales (415)

124   Iceland I            1601     131   12   54                                           Vikingur Reykjavik (498)

125   South Africa II      1595     97    16    0                                           Kruger United (1066)

126   North Macedonia I    1593     147   12   32                                           Shkendija (755)

127   Chile II             1591     63    16    0                                           Cobreloa (1287)

128   Nigeria I            1587     63    20   30                                           Rangers Int’l (1146)

129   Hungary II           1581     95    16    0                                           Vasas (1023)

130   Guinea I             1579     104   14   14                                           Horoya (891)

131   Burkina Faso I       1579     89    16   16                                           Rahimo (898)




                                                              30
  # League                  Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
132   Congo I               1573     160   22   16                                           Otoho d’Oyo (1004)

133   Sudan I               1570     186   24   17                                           Al-Hilal Omdurman II (869)

134   Egypt II              1570     103   18    0                                           Al Qanah (1118)

135   Ukraine II            1569     149   16    0                                           Bukovyna (844)

136   Colombia II           1562     140   16    0                                           Inter Palmira (1309)

137   Luxembourg I          1562     128   16   26                                           Differdange (1040)

138   Scotland II           1562     99    13    0                                           St Johnstone (1024)

139   Moldova I             1560     215   8    44                                           Sheriff Tiraspol (686)

140   Lithuania I           1552     107   10   30                                           Kauno Zalgiris (1222)

141   Gambia I              1552     74    16    2                                           Medina United (1295)

142   Niger I               1546     127   16    8                                           Nigelec (1311)

143   Slovenia II           1546     169   16    0                                           Grosuplje (981)

144   Togo I                1545     104   14   10                                           ASC Kara (876)

145   Czech Republic II     1532     91    16    0                                           Brno (962)

146   Uruguay II            1531     90    14    0                                           Huracan FC (1510)

147   Mozambique I          1531     155   14   14                                           UD Songo (860)

148   Latvia I              1531     243   10   44                                           Riga FC (544)

149   Faroe Islands I       1526     218   10   30                                           Klaksvik (558)

150   Indonesia II          1522     152   20    0                                           Garudayaksa (1532)

151   Botswana I            1520     176   16   18                                           Gaborone Utd (998)

152   Malta I               1518     140   12   34                                           Floriana (1220)

153   Ethiopia I            1516     64    20   10                                           Negele Arsi Ketema (1656)

154   Antigua & Barbuda I   1516     263   12    4                                           All Saints Utd. (723)

155   Benin I               1510     72    18   12                                           Coton FC (1386)

156   Cameroon II           1510     101   16    2                                           Union SA (1615)

157   Mauritania I          1506     132   14   10                                           Nouadhibou (913)

158   Rwanda I              1501     152   18   33                                           Al Hilal Omdurman (809)

159   El Salvador I         1501     152   12   23                                           Luis Angel Firpo (1414)

160   Jamaica I             1496     134   14   26                                           Mount Pleasant (1272)

161   Montenegro I          1495     83    10   28                                           Mornar Bar (1521)

162   Tunisia II            1495     121   28    0                                           PS Sakiet Eddaier (1475)

163   Canada I              1495     141   8    26                                           Forge (1141)

164   Costa Rica II         1492     114   16    0                                           Inter San Carlos (1237)

165   Haiti I               1490     158   13   18                                           Violette (1081)

166   Liberia I             1489     139   15   10                                           Fassell (1505)

167   India I               1487     112   14   15                                           Mohun Bagan (1538)

168   Bolivia II            1474     175   24    0                                           Ciudad Nueva SC (1649)

169   Dominican Rep. I      1468     196   10   32                                           Cibao (1152)

170   Burundi I             1467     190   16   12                                           Aigle Noir (1409)

171   Serbia II             1465     116   16    0                                           Zemun (1796)

172   Northern Ireland I    1465     147   12   36                                           Larne (1498)

173   Cyprus II             1464     151   16    0                                           Nea Salamis (1086)

174   Turkmenistan I        1463     315   8    31                                           Arkadag (198)

175   Eswatini I            1461     159   18   14                                           Nsingizini Hotspurs (1474)

176   Croatia II            1461     79    12    0                                           Cibalia (1809)

177   Singapore I           1458     231   8    54                                           Lion City (980)

178   Thailand II           1455     89    18    0                                           Rasisalai Utd (1466)



                                                               31
  # League                  Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
179   Hong Kong I           1439     203   10   24                                           Kitchee (1483)

180   Philippines I         1437     296   11   36                                           Manila Digger (1372)

181   Cambodia I            1430     224   11   28                                           Svay Rieng (1233)

182   Kenya I               1427     93    18   20                                           Gor Mahia (1775)

183   Mauritius I           1423     191   10    4                                           La Cure Waves (1487)
184   Kosovo II             1422     180   18    0                                           Vushtrria (1624)

185   Peru II               1422     93    18    0                                           Comerciantes (1891)

186   Nigeria II            1422     107   35    0                                           Inter Lagos (2133)

187   Estonia I             1418     174   10   34                                           Levadia (1265)

188   Albania II            1410     150   13    0                                           Laci (1435)

189   Bulgaria II           1410     111   17    0                                           Dunav Ruse (1987)

190   Wales I               1408     146   12   30                                           TNS (1167)

191   Nicaragua I           1400     175   10   32                                           Diriangen (1461)

192   Gabon I               1394     163   14    4                                           Mangasport (1325)

193   Lesotho I             1392     200   16    2                                           Matlama (2172)

194   Venezuela II          1387     106   17    0                                           Lara (2215)

195   Andorra I             1386     236   10   26                                           Inter Escaldes (1559)

196   Martinique I          1385     174   14    1                                           RC Saint Joseph (1496)

197   Slovakia II           1380     91    16    0                                           Banska Bystrica (1776)

198   UAE II                1377     169   15    0                                           United FC (2132)

199   Vietnam II            1375     157   12    0                                           Truong Tuoi Dong Nai (1754)

200   Uzbekistan II         1371     167   14    0                                           Aral (2134)

201   Georgia II            1369     97    10    2                                           FC Gareji Sagarejo (1959)

202   Azerbaijan II         1354     152   10    0                                           Safa Baku (1940)

203   India II              1346     87    10    0                                           Diamond Harbour (2130)

204   Iceland II            1336     100   12    0                                           Afturelding (2482)

205   Uganda II             1332     86    16    0                                           Blacks Power (2462)

206   China II              1331     85    16    0                                           Guangdong GZ-Power (2207)

207   Trinidad & Tobago I   1329     203   12   20                                           Defence Force Trinidad And Tobago (1451)

208   Mongolia I            1320     190   10    7                                           Falcons (1962)

209   Finland II            1319     111   10    0                                           Haka (2422)

210   Armenia II            1312     221   16    0                                           Sardarapat (1960)

211   Tajikistan I          1307     163   12   21                                           Istiqlol Dushanbe (1725)

212   New Zealand I         1298     152   11    7                                           Auckland City (2365)

213   Kazakhstan II         1286     164   14    0                                           Shakhter Karagandy (2381)

214   Bangladesh I          1276     187   10    8                                           Bashundara Kings (2036)

215   Bosnia and Herz. II   1276     91    14    0                                           Celik Zenica (2350)

216   Belarus II            1276     161   18    0                                           SKA-1938 (2419)

217   Kyrgyzstan I          1271     210   16   12                                           Muras United (2441)

218   Somalia I             1267     265   12   10                                           Heegan (2644)

219   Gibraltar I           1259     306   12   34                                           Lincoln Red Imps (1199)

220   North Macedonia II    1252     262   16    0                                           Bregalnica Stip (2555)

221   Taiwan I              1247     184   8     9                                           Taiwan Steel (2218)

222   Chad I                1243     149   14    4                                           Foullah Edifice (2413)

223   Qatar II              1243     96    8     0                                           Al Markhiya (2823)

224   Montenegro II         1228     112   10    0                                           Otrant (2704)
225   Suriname I            1224     227   10    6                                           Robinhood (1932)




                                                               32
  # League                  Rating   SD    n    Int   1500 1750 2000 2250 2500   2016–2025   Best club, rank
226   Kenya II              1212     117   20    0                                           Equity Bank (2950)

227   Ireland II            1192     122   10    0                                           Cork City (2386)

228   Malta II              1189     159   16    0                                           Balzan (2836)

229   Lithuania II          1183     159   16    0                                           Babrungas (2927)

230   Kuwait II             1182     217   8     0                                           Yarmouk (2873)

231   Seychelles I          1179     132   10    6                                           Cote d’Or (2974)

232   Moldova II            1177     120   12    0                                           Real Sireti (2770)

233   Myanmar I             1168     234   12   20                                           Shan Utd (2296)

234   Malawi I              1162     141   16    6                                           Silver Strikers (2931)

235   Bhutan I              1160     221   10    6                                           Paro (2280)

236   Sierra Leone I        1154     96    18    8                                           Bo Rangers (3007)

237   San Marino I          1146     225   16   20                                           Virtus (2804)

238   Latvia II             1113     183   14    0                                           Metta (3178)

239   Northern Ireland II   1082     130   12    0                                           Limavady (3239)

240   Wales II              1055     138   16    0                                           Cambrian United (3282)

241   Laos I                1046     235   10   10                                           Young Elephant (3063)

242   Estonia II            1017     121   10    0                                           Viimsi JK (3367)

243   Fiji I                1005     171   10    2                                           Rewa (3375)

244   Faroe Islands II       993     142   10    0                                           Sandur (3365)




                                                               33
Table 13: The 100 strongest clubs after the 2025/2026 season. RD: the rating deviation (darker: less certain);
the history since 2016, relative to the world mean of every season

 # Club                          Rating RD 2016–2025    # Club                                Rating RD 2016–2025
 1   Bayern Munich Germany I     2585   54             51    Freiburg Germany I               2215   51
 2   Arsenal England I           2560   51             52    Real Sociedad Spain I            2210   52
 3   Barcelona Spain I           2538   53             53    Ath Bilbao Spain I               2202   51
 4   Manchester City England I   2521   50             54    Celta Vigo Spain I               2200   51
 5   Real Madrid Spain I         2490   53             55    Al Nassr Saudi Arabia I          2195   56
 6   PSG France I                2482   52             56    Sunderland England I             2194   56
 7   Inter Italy I               2458   53             57    Olympiacos Piraeus Greece I      2194   55
 8   Liverpool England I         2425   51             58    West Ham England I               2193   53
 9   Aston Villa England I       2408   50             59    Hoffenheim Germany I             2191   56
10   Manchester Utd England I    2382   53             60    Palmeiras Brazil I               2183   58
11   Atl. Madrid Spain I         2380   50             61    Eintracht Frankfurt Germany I    2182   53
12   Bayer Leverkusen Germany I 2361    53             62    Rayo Vallecano Spain I           2181   51
13   Dortmund Germany I          2357   52             63    Braga Portugal I                 2177   51
14   Chelsea England I           2355   49             64    Slavia Prague Czech Republic I   2172   57
15   Napoli Italy I              2341   54             65    Strasbourg France I              2169   52
16   Newcastle England I         2334   49             66    Rennes France I                  2167   56
17   Benfica Portugal I          2329   54             67    Valencia Spain I                 2167   55
18   Sporting CP Portugal I      2329   55             68    Flamengo RJ Brazil I             2162   56
19   Brighton England I          2325   53             69    Al Ahli SC Saudi Arabia I        2146   52
20   Juventus Italy I            2325   52             70    AEK Athens Greece I              2145   54
21   Bournemouth England I       2315   54             71    Fiorentina Italy I               2145   50
22   FC Porto Portugal I         2304   55             72    Osasuna Spain I                  2141   55
23   AC Milan Italy I            2304   54             73    Mainz Germany I                  2140   53
24   AS Roma Italy I             2295   52             74    Midtjylland Denmark I            2134   51
25   RB Leipzig Germany I        2293   56             75    Bodo/Glimt Norway I              2130   63
26   Atalanta Italy I            2284   51             76    Shakhtar Donetsk Ukraine I       2130   57
27   Brentford England I         2280   53             77    Getafe Spain I                   2129   56
28   Lens France I               2279   56             78    Girona Spain I                   2126   55
29   Crystal Palace England I    2274   50             79    Alaves Spain I                   2118   55
30   PSV Netherlands I           2274   59             80    Burnley England I                2116   56
31   Betis Spain I               2270   50             81    Kashima Antlers Japan I          2115   59
32   Villarreal Spain I          2267   53             82    Espanyol Spain I                 2114   56
33   Al Hilal Saudi Arabia I     2267   58             83    Torino Italy I                   2113   55
34   Tottenham England I         2262   50             84    Mallorca Spain I                 2111   56
35   Stuttgart Germany I         2258   51             85    Feyenoord Netherlands I          2109   56
36   Fulham England I            2256   53             86    Sassuolo Italy I                 2107   57
37   Club Brugge KV Belgium I    2255   51             87    Augsburg Germany I               2107   57
38   Galatasaray Turkey I        2253   55             88    Wolves England I                 2106   54
39   Lyon France I               2253   53             89    Elche Spain I                    2106   56
40   Royale Union SG Belgium I   2247   52             90    B. Monchengladbach Germany I 2105       57
41   Nottingham England I        2243   50             91    Sevilla Spain I                  2104   55
42   Como Italy I                2243   54             92    Toulouse France I                2104   56
43   Everton England I           2239   54             93    Brest France I                   2104   56
44   Lazio Italy I               2238   53             94    Ipswich England II               2102   59
45   Leeds England I             2235   54             95    Union Berlin Germany I           2102   57
46   Lille France I              2234   53             96    Levante Spain I                  2101   57
47   Bologna Italy I             2234   50             97    Lorient France I                 2099   59
48   Marseille France I          2232   54             98    PAOK Greece I                    2098   51
49   Monaco France I             2227   53             99    Udinese Italy I                  2098   56
50   Fenerbahce Turkey I         2223   53             100   Southampton England II           2092   55

                                                       34
Table 14: Ratings of the 216 national teams after the 2026 World Cup. The stripe: the confederation; RD: the
rating deviation (darker: less certain); the history since 2010 at the end of every year, relative to the mean of all
teams
 # Team            Rating   RD   2010–2026        # Team                     Rating   RD   2010–2026
 1   Spain         2415     72                   37   Poland                 1902     77
 2   Argentina     2335     74                   38   Sweden                 1900     76
 3   France        2316     73                   39   Czech Republic         1886     75
 4   England       2270     73                   40   Peru                   1885     80
 5   Portugal      2216     76                   41   Iran                   1883     85
 6   Brazil        2212     80                   42   Australia              1878     81
 7   Netherlands   2187     75                   43   Venezuela              1874     81
 8   Germany       2182     79                   44   Chile                  1866     81
 9   Colombia      2147     75                   45   Mali                   1859     78
10   Italy         2139     79                   46   D.R. Congo             1856     72
11   Morocco       2128     76                   47   Tunisia                1851     77
12   Belgium       2108     75                   48   Canada                 1850     76
13   Croatia       2107     74                   49   South Africa           1849     76
14   Switzerland   2090     72                   50   Slovenia               1834     77
15   Senegal       2067     77                   51   Slovakia               1834     77
16   Uruguay       2065     77                   52   Romania                1833     81
17   Norway        2058     76                   53   Ireland                1828     80
18   Mexico        2036     75                   54   South Korea            1826     84
19   Denmark       2036     76                   55   Burkina Faso           1816     79
20   Ecuador       2017     77                   56   Ghana                  1812     79
21   Turkey        2013     75                   57   Panama                 1802     72
22   Ukraine       1989     79                   58   Cape Verde             1789     79
23   Egypt         1983     73                   59   Costa Rica             1778     76
24   Nigeria       1982     75                   60   Bolivia                1770     80
25   Paraguay      1973     75                   61   Kosovo                 1770     79
26   Ivory Coast   1967     77                   62   Israel                 1765     82
27   Japan         1952     86                   63   Bosnia & Herzegovina   1761     74
28   Scotland      1948     75                   64   Albania                1757     81
29   Serbia        1943     79                   65   North Macedonia        1749     81
30   Austria       1939     76                   66   Georgia                1740     78
31   Wales         1937     79                   67   Saudi Arabia           1730     80
32   Algeria       1931     76                   68   Gabon                  1720     81
33   USA           1931     74                   69   Uzbekistan             1718     86
34   Greece        1925     81                   70   Finland                1717     81
35   Hungary       1920     79                   71   Uganda                 1703     82
36   Cameroon      1911     79                   72   Zambia                 1702     83




                                                         35
  # Team                     Rating   RD    2010–2026        # Team                 Rating   RD    2010–2026
 73   Iceland                1693     79                 109    Rwanda              1534     86
 74   Guinea                 1690     80                 110    Liberia             1523     87
 75   Angola                 1688     80                 111    Malawi              1519     85
 76   Northern Ireland       1688     80                 112    Syria               1513     93
 77   Equatorial Guinea      1685     81                 113    Ethiopia            1511     82
 78   Qatar                  1676     78                 114    Burundi             1504     86
 79   Benin                  1673     81                 115    Oman                1493     85
 80   Mozambique             1651     80                 116    Trinidad & Tobago   1493     78
 81   Iraq                   1647     79                 117    Curacao             1486     81
 82   Jamaica                1642     73                 118    Eritrea             1484     151
 83   Honduras               1640     74                 119    Congo               1482     89
 84   Montenegro             1637     81                 120    Botswana            1473     85
 85   Jordan                 1622     85                 121    Faroe Islands       1465     83
 86   Comoros                1622     84                 122    Azerbaijan          1461     85
 87   Bulgaria               1621     81                 123    Bahrain             1461     90
 88   New Zealand            1606     115                124    Cyprus              1461     81
 89   Gambia                 1606     84                 125    China               1454     86
 90   Tanzania               1599     81                 126    Central Africa      1454     86
 91   Sierra Leone           1597     88                 127    Estonia             1453     83
 92   Haiti                  1582     80                 128    Suriname            1439     80
 93   Kenya                  1579     88                 129    El Salvador         1434     76
 94   Libya                  1577     86                 130    Latvia              1429     82
 95   Belarus                1576     82                 131    Lesotho             1429     88
 96   Madagascar             1571     83                 132    Palestine           1412     90
 97   Sudan                  1570     81                 133    Moldova             1409     84
 98   Guatemala              1562     79                 134    Guadeloupe          1407     89
 99   Niger                  1559     89                 135    Lithuania           1391     82
100   United Arab Emirates   1555     80                 136    Martinique          1373     88
101   Armenia                1553     80                 137    North Korea         1373     96
102   Zimbabwe               1550     83                 138    Nicaragua           1371     83
103   Mauritania             1547     83                 139    Thailand            1370     93
104   Luxembourg             1543     80                 140    Indonesia           1352     87
105   Togo                   1541     84                 141    Kyrgyzstan          1345     91
106   Kazakhstan             1540     82                 142    Tajikistan          1335     96
107   Guinea Bissau          1539     83                 143    Kuwait              1331     93
108   Namibia                1535     84                 144    Lebanon             1331     90




                                                        36
  # Team                        Rating   RD    2010–2026         # Team                    Rating   RD    2010–2026
145   Guyana                    1331     83                     181   Saint Martin         1064     94
146   Cuba                      1319     81                     182   Tahiti               1060     111
147   Malta                     1318     86                     183   Fiji                 1059     109
148   Chad                      1315     88                     184   Vanuatu              1042     130
149   Dominican Republic        1312     83                     185   Afghanistan          1039     95
150   South Sudan               1305     88                     186   Antigua & Barbuda    1031     85
151   Eswatini                  1300     87                     187   Papua New Guinea      981     114
152   Vietnam                   1299     92                     188   San Marino            981     97
153   Turkmenistan              1255     99                     189   Aruba                 976     91
154   Puerto Rico               1238     93                     190   Bangladesh            958     96
155   Malaysia                  1229     95                     191   Sri Lanka             956     105
156   French Guiana             1227     96                     192   Barbados              948     83
157   Sao Tome & Principe       1225     93                     193   Brunei                946     115
158   Yemen                     1210     92                     194   Cambodia              943     107
159   Philippines               1203     95                     195   Dominica              941     87
160   Bermuda                   1202     81                     196   Mongolia              941     116
161   Mauritius                 1199     100                    197   Bhutan                936     105
162   Singapore                 1196     92                     198   Cayman Islands        934     90
163   Grenada                   1194     91                     199   Maldives              927     100
164   Somalia                   1178     108                    200   Bonaire               913     100
165   Andorra                   1168     89                     201   Laos                  912     109
166   Djibouti                  1160     100                    202   Nepal                 886     98
167   St Kitts & Nevis          1139     86                     203   Pakistan              869     112
168   New Caledonia             1138     114                    204   Guam                  868     122
169   India                     1136     92                     205   Chinese Taipei        829     97
170   St Vincent & Grenadines   1134     82                     206   British Virgin Is.    809     91
171   Gibraltar                 1129     87                     207   Turks & Caicos        803     98
172   Saint Lucia               1126     89                     208   Bahamas               795     88
173   Hong Kong                 1119     92                     209   Macau                 792     130
174   Montserrat                1112     90                     210   Timor-Leste           756     107
175   Belize                    1109     84                     211   Samoa                 745     123
176   Seychelles                1106     109                    212   US Virgin Islands     727     96
177   Myanmar                   1088     97                     213   Anguilla              709     90
178   Liechtenstein             1079     89                     214   Tonga                 700     153
179   Sint Maarten              1079     93                     215   Cook Islands          650     159
180   Solomon Islands           1074     114                    216   American Samoa        628     186




                                                           37
Acknowledgements Andrei Shelopugin is thankful to Nikita Kozodoi and Viktoria Lokteva for their
contributions to the earlier stages of this research, and to Nikita Vasyukhin for consultations on soccer.

References

 [1] Bergkamp, T.L., Frencken, W.G., Niessen, A.S.M., Meijer, R.R., Hartigh, R.J.: How soccer scouts
     identify talented players. European Journal of Sport Science 22(7), 994–1004 (2022)

 [2] Dixon, M.J., Coles, S.G.: Modelling association football scores and inefficiencies in the football
     betting market. Journal of the Royal Statistical Society: Series C (Applied Statistics) 46(2),
     265–280 (1997)

 [3] Elo, A.E.: The proposed uscf rating system, its development, theory, and applications. Chess Life
     22(8), 242–247 (1967)

 [4] Glickman, M.E.: Paired comparison models with strength-dependent ties and order effects.
     Statistical Modelling 26(5), 476–499 (2026)

 [5] Grinsztajn, L., Oyallon, E., Varoquaux, G.: Why do tree-based models still outperform deep
     learning on typical tabular data? Advances in neural information processing systems 35, 507–520
     (2022)

 [6] Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.-Y.: Lightgbm: A highly
     efficient gradient boosting decision tree. Advances in neural information processing systems 30
     (2017)

 [7] Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A.V., Gulin, A.: Catboost: unbiased boosting
     with categorical features. Advances in neural information processing systems 31 (2018)

 [8] Dixon, M., Robinson, M.: A birth process model for association football matches. Journal of the
     Royal Statistical Society: Series D (The Statistician) 47(3), 523–538 (1998)

 [9] Glickman, M.E.: Example of the glicko-2 system. Boston University 28 (2012)

[10] Herbrich, R., Minka, T., Graepel, T.: Trueskill™: a bayesian skill rating system. Advances in neural
     information processing systems 19 (2006)

[11] Shelopugin, A., Sirotkin, A.: Ratings of european and south american football leagues based on
     glicko-2 with modifications. arXiv preprint arXiv:2310.11459 (2023)

[12] Shelopugin, A., Sirotkin, A.: Constructing football club ratings with league strength awareness
     using a modified glicko model. In: International Sports Analytics Conference and Exhibition, pp.
     38–61 (2026). Springer

[13] Pollard, R.: Home advantage in soccer: a retrospective analysis. Journal of Sports Sciences 4(3),
     237–248 (1986)

[14] Nevill, A.M., Balmer, N.J., Williams, A.M.: The influence of crowd noise and experience upon
     refereeing decisions in football. Psychology of Sport and Exercise 3(4), 261–272 (2002)

[15] Pettersson-Lidbom, P., Priks, M.: Behavior under social pressure: Empty italian stadiums and
     referee bias. Economics Letters 108(2), 212–214 (2010)

[16] Constantinou, A.C., Fenton, N.E.: Solving the problem of inadequate scoring rules for assessing
     probabilistic football forecast models. Journal of Quantitative Analysis in Sports 8(1) (2012)

[17] Davidson, R.R.: On extending the bradley-terry model to accommodate ties in paired comparison
     experiments. Journal of the American Statistical Association 65(329), 317–328 (1970)



                                                   38
[18] Dinsdale, D., Gallagher, J.: Transfer portal: Accurately forecasting the impact of a player transfer
     in soccer. arXiv preprint arXiv:2201.11533 (2022)

[19] Shelopugin, A.: Expected possession value of control and duel actions for soccer player skills
     estimation. In: International Sports Analytics Conference and Exhibition, pp. 292–314 (2026).
     Springer

[20] Pollard, R., Reep, C.: Measuring the effectiveness of playing strategies at soccer. Journal of the
     Royal Statistical Society Series D: The Statistician 46(4), 541–550 (1997)




                                                   39
