# On the fairness of single round-robin tournaments: Evidence from European football

- arXiv: https://arxiv.org/abs/2610.21296
- Published: 2026-10-15
- PDF: ../../library/preprints/arxiv/2026/2026 On the fairness of single round-robin tournaments Evidence from European football - arXiv 2610.21296.pdf

## Abstract

Single round-robin tournaments are widely regarded as unfair because of their home-away imbalance: some competitors play more home games than the others. Therefore, most sports leagues are played in a double round-robin format. However, some European football leagues contain a single round-robin (sub)tournament. To test whether empirical data can validate their unfairness, we construct a unique database and develop a strength of schedule metric based on Elo ratings with favourable theoretical properties. In contrast to the robust impact of relative team strength, the strength of schedule is found to have no significant effect on the number of points scored under the assumption of a league-specific home advantage. Consequently, the theoretical unfairness is not a serious issue in practice, or the standard approach of modelling home advantage in Elo ratings might need to be reconsidered.

## Full text (pdftotext)

                                                  On the fairness of single round-robin tournaments:
                                                          Evidence from European football
                                                  László Csatóa                  Diána Ivett Fűrészb                     Zsolt Havranc

                                                                                 16th October 2026
arXiv:2610.21296v1 [econ.EM] 15 Oct 2026




                                           “When accepting the presence of a home advantage in a single round robin context, where
                                           each team has a certain strength, the following is true: the particular set of teams played
                                           at home, and teams played away impacts the expected number of points or wins a team can
                                           collect. By that, the outcome of the tournament depends on which teams one plays home,
                                           and which teams one plays away.” (Wessel et al., 2026, p. 830)


                                                                                         Abstract
                                                   Single round-robin tournaments are widely regarded as unfair because of their home-
                                                   away imbalance: some competitors play more home games than the others. Therefore,
                                                   most sports leagues are played in a double round-robin format. However, some
                                                   European football leagues contain a single round-robin (sub)tournament. To test
                                                   whether empirical data can validate their unfairness, we construct a unique database
                                                   and develop a strength of schedule metric based on Elo ratings with favourable
                                                   theoretical properties. In contrast to the robust impact of relative team strength,
                                                   the strength of schedule is found to have no significant effect on the number of points
                                                   scored under the assumption of a league-specific home advantage. Consequently, the
                                                   theoretical unfairness is not a serious issue in practice, or the standard approach of
                                                   modelling home advantage in Elo ratings might need to be reconsidered.

                                           Keywords: Elo rating; fairness; home advantage; round-robin tournament; sports scheduling
                                           MSC class: 62F07, 62P20, 90B90
                                           JEL classification number: C44, C53, D71, Z20


                                              a
                                                Corresponding author
                                           E-mail: laszlo.csato@sztaki.hun-ren.hu
                                           Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                           Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                           Decision Systems, Budapest, Hungary
                                           Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of
                                           Operations Research and Actuarial Sciences, Budapest, Hungary
                                              b
                                                E-mail: furesz.diana@ktk.pte.hu
                                           University of Pécs, Faculty of Business and Economics, Pécs, Hungary
                                              c
                                                E-mail: zsolt.havran@uni-corvinus.hu
                                           Corvinus University of Budapest (BCE), Institute of Entrepreneurship and Innovation, Department of
                                           Business Economics, Budapest, Hungary
Motivation
The Hungarian first football division is organised in a triple round-robin format since the
2015/16 season: any given pair of teams 𝑖 and 𝑗 plays three times against each other such
that either team 𝑖 or team 𝑗 plays twice at home. Hence, all the 12 teams play 33 matches,
but six teams play 17 home matches, while the remaining six teams play only 16 home
matches.
    In the 2017/18 season, Balmazújváros and Diósgyőr contested to avoid relegation. Both
clubs finished with 36 points; Balmazújváros played fewer home games and had a superior
goal difference – but was relegated as the primary tie-breaking rule is the number of wins.
In the 2025/26 season, after seven consecutive triumphs for Ferencváros, Győr became the
champion ahead of Ferencváros with the minimal advantage of one point; the tie-breaking
rules favoured Ferencváros. However, Győr played twice at home against Ferencváros.
    One can argue that the structure of the league affected these outcomes, and might
have been responsible for the relegation of Balmazújváros and the disappointment of
Ferencváros. The current paper aims to empirically explore the impact of this inherent
bias in single round-robin tournaments, caused by the asymmetric allocation of home
advantages.


1     Introduction
Every professional sports league produces a ranking at the end of the season. Thus, one of
the most important responsibilities of decision-makers is guaranteeing that the rules of
the competition do not affect the ranking, which solely depends on performance on the
field. In particular, if the ranking aggregates the results of matches, all teams should meet
opponents of comparable strength. This explains the popularity of the round-robin format,
where each team plays the same number of games against any other team.
    Obviously, asymmetry in the games can be balanced only if every pair of teams plays an
even number of games against each other. Asymmetry arises in many sports. For instance,
playing with the white pieces is considered beneficial in chess (Henery, 1992; Fecker, 2024).
Analogously, if the match is played at the venue of one of the teams, the well-documented
home advantage (Pollard and Pollard, 2005) implies asymmetry. Unsurprisingly, most
European football leagues use a double round-robin format (Goossens and Spieksma,
2012b; Lasek and Gagolewski, 2018), since home advantage plays an important role in
determining the result of a game (Pollard, 1986, 2006, 2008).
    However, some leagues contain single round-robin (sub)tournaments as mentioned
above. A recent theoretical paper, Wessel et al. (2026), argues that each player should
face its opponents when ranked by strength in an alternating fashion with respect to home
advantage to prevent distorting the outcome and to guarantee equal treatment. First in
the literature, we check whether this claim of distortion is supported by empirical data.
    In particular, our paper aims to study the fairness of single round-robin competitions
by examining the following research question: Does the number of points scored depend
on the allocation of home and away games? In order to statistically test this issue, a
unique database is constructed from European football leagues (Section 3). We define
average winning probability based on Elo ratings and develop a strength of schedule
metric (Section 4). Our measure uses a constant home advantage parameter (which is the
standard used by Elo ratings in football), equals zero in the absence of home advantage,
and takes into account the relative strength of home and away opponents. The latter is a

                                             2
key feature because, for example, a strong team is severely disadvantaged if it plays against
the strongest half of its opponents away, and against the weakest half of its opponents at
home (Wessel et al., 2026). The statistical analysis applies the correlated random-effects
method based on the Mundlak specification.
   The results in Section 5 consistently show that, under the assumption of home advantage
enjoyed equally by all teams across the league, strength of schedule does not have any
statistically significant impact on the number of points. Thus, the allocation of home
games – including the imbalance in the number of home and away games – seems not to
make these tournaments unfair in practice, even though home advantage can be clearly
observed.


2     Related literature
As far as we know, no previous study has examined the fairness of single round-robin
tournaments empirically, in contrast to the impact of the schedule in double round-robin
tournaments and competitions played on a neutral field. If team A plays against team
B, and subsequently against team C, the performance of team A against team C may
depend on team B; hence, team C is said to receive a carryover effect from team B.
Goossens and Spieksma (2012a) develop a method to measure whether the carryover effect
influences the outcome of football matches, and apply it to the highest Belgian division.
No supporting evidence is found, implying that the carryover effect is not a major issue in
sports scheduling from the perspective of league organisers, even though it plays a central
role in the scheduling literature (Lambrechts et al., 2018; Goossens et al., 2020; Devriesere
et al., 2025). Krumer and Lechner (2017) study the fairness of sequential round-robin
tournaments with three and four contestants. According to their results based on Olympic
wrestling (three athletes per group), as well as FIFA World Cups and UEFA European
Championships (four teams per group), competing in the first and third matches provides
a significant advantage.
    Tűű-Szabó and Kóczy (2026) propose a Monte Carlo simulation framework to quantify
procedural fairness in league competitions by isolating biases caused by fixture schedules
from team strength and ranking rules. They show that unadjusted triple round-robin
tournaments, such as the Hungarian first football division, create substantially larger and
less evenly distributed fairness distortions, while balancing mechanisms, like those used in
Switzerland, can substantially reduce these effects.
    Wessel et al. (2026) introduce a novel fairness measure for a single round-robin tour-
nament where the contestants are ranked by their strength. In order to guarantee equal
treatment, each contestant should face its opponents when ranked by strength in an al-
ternating pattern with respect to home advantage. The existence of ranking-fair schedules
is proved if the number of contestants is a multiple of four, and an algorithm is given to
construct them.
    A potential problem of fairness, analogous to single round-robin competitions, arises
in Swiss-system tournaments with an odd number of rounds. Csató and Krumer (2026)
compare the number of points scored in Swiss-system chess tournaments by two groups
of players, who played one game more/less with the white pieces. Players with an extra
white game score significantly more points; the advantage exceeds the value of a draw in
the prestigious FIDE Grand Swiss tournaments played in 11 rounds.
    Unbalanced schedules have received serious attention in sports economics since they can
distort standard measures of competitive balance. Lenten (2008) suggests a log-probability

                                             3
rule to derive adjusted win ratios correcting for the bias. Lenten (2011) uses a modified
model and applies it to the Australian Football League (AFL) to create an adjusted league
ranking. Lenten (2015) extends this model to the conference and divisional design of the
National Football League (NFL). Lee et al. (2019) show that the winning percentage is
a biased estimator of the true win probability if schedules are unbalanced, and present
a mathematical statistical approach to compute an unbiased estimator of within-season
competitive balance. However, none of these studies test whether the implied bias can be
empirically detected in the league rankings, which will be done in the following for single
round-robin (sub)tournaments in European football.
    Finally, we know only one paper about scheduling real-world single round-robin tour-
naments. Rasmussen (2008) proposes a solution method based on a logic-based Benders
decomposition to find a schedule for the triple round-robin tournament played in Denmark.
The given algorithm works for practical applications, but struggles to prove optimality. It
was adopted by the Danish Football Association to schedule the 2006/07 season.


3    Data
While the top European football leagues have been organised in a double round-robin
format in recent decades, there exist some exceptions among second-tier leagues that can
be considered to explore the fairness of single round-robin competitions. In the absence of
any comprehensive database on the format of these leagues, we have managed to find the
following candidates to construct a database.
    Three countries have recently used a triple round-robin format with 12 teams such
that the schedule of the whole season was determined before the first round:

     • Denmark: between 1995/96 and 2015/16 (21 seasons);

     • Hungary: between 2015/16 and 2025/26 (11 seasons);

     • Scotland (before the split): between 2000/01 and 2025/26, except for the unfin-
       ished 2019/20 season (25 seasons).

Three West Balkan countries have recently used a triple round-robin with 12 teams such
that the schedule of the last 11 rounds was determined before the 23rd round, based on
the positions after the first 22 rounds:

     • Croatia: 1999/2000, between 2006/07 and 2008/09, 2012/13 (5 seasons);

     • Serbia: between 2007/08 and 2008/09 (2 seasons);

     • Slovenia: between 1998/99 and 2002/03 (5 seasons).

Finally, two nations have used a league system with 16 teams where a subset of teams
play an additional single round-robin tournament after a double round-robin:

     • Romania: the last ten teams since 2020/21 (6 seasons);

     • Serbia: the first eight teams (championship part) and the last eight teams
       (relegation part) since 2015/16, except for the unfinished 2019/20 and 2020/21
       seasons (9 seasons).


                                            4
Based on the list above, we have chosen the countries where a single round-robin tournament
is organised at least over 10 years: Denmark (1995/96–2015/16), Hungary (since 20215/16),
Scotland (since 2000/01), and Serbia (since 2015/16).
    In order to estimate the potential bias caused by the allocation of home games in a
single round-robin tournament, it is crucial to have a reliable measure of team strengths.
For this purpose, we use Football Club Elo Ratings (http://clubelo.com/), a well-
established measure in the academic literature (Bosker and Gürtler, 2024; Csató, 2022b,
2024; Csató and Petróczy, 2025, 2026; Yildirim and Bilman, 2025a,b). Even though the
triple round-robin format has been used recently in further leagues, such as the Faroe
Islands, Finland, Israel, Kosovo, and Slovakia, they have not been included in the sample
because even the top divisions of these countries are missing from the database of Football
Club Elo Ratings.
    The basic idea behind the Elo method is straightforward: the ratings of the two
opponents are updated based on the outcome of their match; the same result against a
stronger (weaker) opponent leads to a higher (smaller) gain, and the impact of a game
decreases after new games are played (Csató et al., 2025). In contrast to the official FIFA
World Ranking, which uses the Elo approach since 2018 (FIFA, 2018), Football Club Elo
Ratings take both home advantage and goal difference into account as recommended by
Szczecinski and Roatis (2022). Home advantage is a league-specific, dynamic parameter;
its value increases or decreases together with the Elo rating of the home team. Hence,
Football Club Elo Ratings are able to capture trends in home advantage. Unsurprisingly,
this parameter in the top European leagues reached its minimum in the seasons affected
by the Covid-19 pandemic when the matches were played behind closed doors.
    Elo rating is a strictly performance-based measure that does not reflect the effect
of injuries, managerial changes, or player transfers. Hence, Elo ratings are usually not
competitive with betting odds in forecasting accuracy (Wunderlich, 2025). Furthermore,
the database of Football Club Elo Ratings does not contain the second football divisions
of these countries. Thus, the ratings of the promoted teams are equal at the beginning of
a season and are an unreliable measure of strength.
    To conclude, it would be suboptimal using pre-season Elo ratings rather than Elo
ratings after the standard double round-robin part of the league is played. This does not
cause any problem in Hungary, Scotland, and Serbia except for some marginal corrections
detailed in the Appendix. However, the Danish league started with a single round-robin
of 11 rounds, followed by a double round-robin of 22 rounds (Rasmussen, 2008), which
excludes using the Danish data.
    Therefore, we construct club-level panel data from three European football leagues
(Hungary, Scotland, Serbia). Although observations for the Scottish league are available
from the 2000/01 season, analogous data for the Hungarian and Serbian leagues do not
exist before the 2015/16 season. To ensure temporal comparability, the primary sample is
restricted to the common observation period from 2015/16 to 2025/26. The exclusion of
Scottish data prior to the 2015/16 season is particularly important given the cross-country
focus, as retaining the earlier observations would make country membership partially
confounded with the observation period. Restricting the analysis to a common time window
ensures a consistent basis for estimating country effects and country-specific interaction
terms. Nonetheless, we consider all observations from Scotland in the secondary sample.
    The two samples are summarised in Table 1. Both constitute an unbalanced panel:
individual clubs may enter or leave the sample over time due to promotion and relegation.
The club is the cross-sectional unit and season is the time dimension.


                                            5
                                     Table 1: Sample coverage
                              (a) Primary sample (2025/16–2025/26)

      Country         Seasons         Teams per season       Observations                Clubs
      Hungary           11                  12                   132                      23
      Scotland          10                  12                   120                      17
      Serbia             9                 2×8                   144                      31
      Total              30                    —                     396                     71
        Notes: Hungary: All seasons from 2015/16 to 2025/26.
        Scotland: All seasons from 2015/16 to 2025/26, except for the unfinished 2019/20.
        Serbia: All seasons from 2015/16 to 2025/26, except for the unfinished 2019/20 and 2020/21.

                                (b) Secondary sample (Scotland)

      Country         Seasons         Teams per season       Observations                Clubs
      Scotland           25                    12                    300                     19
        Note: All seasons from 2000/01 to 2025/26, except for the unfinished 2019/20.


   We use Football Club Elo Ratings as of the first day of Round 23 in the Hungarian
and Scottish leagues, and as of the first day of Round 31 in the Serbian league. The exact
dates are provided in Table A.1 in the Appendix.


4     Methodology
The background of the estimation is described in two parts. Section 4.1 presents how
we control for the strength of opponents and the strength of schedule, while Section 4.2
discusses the selection of the statistical approach.

4.1     Variable and model construction
Let 𝑅𝑖 and 𝑅𝑗 denote the Elo ratings of teams 𝑖 and 𝑗, respectively. According to the
methodology of Football Club Elo Ratings, team 𝑖 wins against team 𝑗 at home with a
probability of
                                                    1
                               𝑝𝑖𝑗 (Δ) =                    ,                      (1)
                                         1 + 10 −𝑅𝑖 −Δ)/400
                                               (𝑅 𝑗


where Δ is the home advantage parameter (the Elo rating of the home team is increased
by Δ). Since the Elo method does not consider draws in the calculation of winning
probabilities, the probability that team 𝑗 wins against team 𝑖 away equals
                                               1                           1
                 1 − 𝑝𝑖𝑗 (Δ) = 1 −                           =                           .
                                     1 + 10(𝑅𝑗 −𝑅𝑖 −Δ)/400       1 + 10(𝑅𝑖 −𝑅𝑗 +Δ)/400
    The Elo ratings are updated after the match between teams 𝑖 and 𝑗 as follows:
      𝑅𝑖′ = 𝑅𝑖 + 𝑘 [𝑄𝑖𝑗 − 𝑝𝑖𝑗 (Δ)]       and        𝑅𝑗′ = 𝑅𝑗 + 𝑘 [(1 − 𝑄𝑖𝑗 ) − (1 − 𝑝𝑖𝑗 (Δ))] ,
where 𝑄𝑖𝑗 is the outcome of the match; 𝑄𝑖𝑗 = 1 if team 𝑖 wins, 𝑄𝑖𝑗 = 0 if team 𝑗 wins,
and 𝑄𝑖𝑗 = 0.5 if they play a draw. Consequently, 𝑅𝑖 + 𝑅𝑗 = 𝑅𝑖′ + 𝑅𝑗′ . Football Club Elo
Ratings assume 𝑘 = 20.

                                                    6
                  Table 2: League-specific home advantage parameters

              Country     End of sample           Minimum              Maximum
                               46.6               42.1                   156.5
              Hungary
                           (2026-06-30)       (2026-03-21)            (1980-03-01)
                               66.5               21.9                   113.5
              Scotland
                           (2026-06-30)       (2017-12-09)            (1953-10-31)
                               47.9               45.4                   101.5
              Serbia
                           (2026-06-30)       (2025-08-18)            (2007-05-30)
                 Source: Football Club Elo Ratings (http://clubelo.com/).


    Let 𝑁 be the set of teams and |𝑁 | = 𝑛 be the number of teams in a tournament. The
logic behind the Elo method suggests the following definition.

Definition 1. The average winning probability of team 𝑖 in a double round-robin tourna-
ment is
                                       ∑︁ 𝑝𝑖𝑗 (Δ) + 𝑝𝑗𝑖 (Δ)
                        AWP 𝑖 (Δ) =                          .                      (2)
                                     𝑗∈𝑁,𝑗̸=𝑖   2(𝑛 − 1)

AWP 𝑖 (Δ) is the mean of winning probabilities from equation (1), taken over the set of
matches played against all other teams, once at home and once away.
    AWP 𝑖 (Δ) = 0.5 for each team 𝑖 ∈ 𝑁 if they are of equal strength. In the case of
competitive imbalance, AWP 𝑖 (Δ) is influenced by the value of home advantage Δ due
to the non-linearity of 𝑝𝑖𝑗 as a function of 𝑅𝑗 − 𝑅𝑖 . However, the dependence is rather
marginal because the reduction in the probability of winning away is balanced by the
increase in the probability of winning at home to a great extent.
    Denote by 𝑂𝑖ℎ (𝑂𝑖𝑎 ) the opponents of team 𝑖 against whom it plays at home (away) in
a tournament.

Definition 2. The strength of schedule of team 𝑖 in a tournament is
                               ⎛ ∑︀                  ∑︀                              ⎞
                                   𝑗∈𝑂𝑖ℎ 𝑝𝑖𝑗 (Δ) +    𝑗∈𝑂𝑖𝑎 𝑝𝑗𝑖 (Δ)
            SoS 𝑖 (Δ) = 100 × ⎝            ⃒ ⃒
                                           ⃒ ℎ⃒                       − AWP 𝑖 (Δ)⎠ .     (3)
                                           ⃒𝑂𝑖 ⃒ + |𝑂𝑖𝑎 |

This metric, inspired by equation (2), is the difference between the average winning
probabilities in the tournament considered and a (fair) double round-robin tournament,
respectively, multiplied by 100. In a single round-robin tournament without home advantage
(Δ = 0), as well as in a double round-robin, SoS 𝑖 (Δ) = 0 for each team 𝑖 ∈ 𝑁 .
    Since we use ex-ante Elo ratings, both the average winning probability AWP and the
strength of schedule SoS are independent of the result of any match played in the single
round-robin (sub)tournament of the given season. On the other hand, both AWP and SoS
depend on the home advantage parameter Δ. Some league-specific home advantage values
of Football Club Elo Ratings are shown in Table 2. Δ = 50 is chosen as a benchmark,
while Δ = 25 and Δ = 75 are used for sensitivity analyses.
    Our empirical analysis examines whether schedule characteristics are associated with
sporting performance in single round-robin competitions. The unit of observation is the
club-season, resulting in an unbalanced panel of clubs from Hungary, Serbia, and Scotland
over the 2015/16–2025/26 period. The dependent variable is the number of points per


                                              7
                    Table 3: Summary statistics of the main variables
                           (a) Primary sample (2015/16–2025/26)

      Measure  𝑆 (points per match)            AWP(Δ = 50)              SoS (Δ = 50)
      Mean             1.38                       0.50                     +0.00
      St. dev.         0.56                       0.13                     +0.83
      Minimum            0                        0.25                     −2.15
      Median           1.29                       0.47                     +0.04
      Maximum            3                        0.90                     +2.15

                               (b) Secondary sample (Scotland)

      Measure  𝑆 (points per match)            AWP(Δ = 50)              SoS (Δ = 50)
      Mean             1.38                       0.50                     +0.00
      St. dev.         0.58                       0.15                     +0.63
      Minimum          0.27                       0.22                     −1.27
      Median           1.27                       0.46                     +0.01
      Maximum          2.82                       0.90                     +1.11

         Table 4: Model specification tests, primary sample (2015/16–2025/26)

      Test                                        Statistic               𝑝-value
      FE vs. pooled OLS F-test              𝐹 (70, 323) = 1.276            0.084
      RE vs. pooled OLS BP-LM test             𝜒2 (1) = 0.101              0.751
      Hausman test, FE vs. RE                 𝜒2 (2) = 13.930             < 0.001
        Notes: Baseline specification with home advantage parameter Δ = 50.
        BP-LM = Breusch–Pagan Lagrange multiplier; FE = fixed effects; RE = random effects.


match rather than accumulated points. This normalisation is important because the
number of matches underlying the scheduling measures differs across the countries.
   The baseline relationship is expressed as follows:

                 𝑆𝑖𝑡 = 𝛼 + 𝛽1 AWP 𝑖𝑡 + 𝛽2 SoS 𝑖𝑡 + 𝛾1 HUN 𝑖 + 𝛾2 SRB 𝑖 + 𝜀𝑖𝑡 ,

where 𝑖 denotes the clubs and 𝑡 denotes the seasons. The dependent variable 𝑆𝑖𝑡 is the
number of points collected per match. AWP 𝑖𝑡 is the average winning probability, SoS 𝑖𝑡
represents the strength of schedule. Scotland serves as the reference country; the dummy
variables HUN 𝑖 and SRB 𝑖 identify Hungarian and Serbian clubs, respectively.
    Table 3 reports the main descriptive statistics of the two variables constructed, together
with the number of points per match. The mean average winning probability is almost
exactly 0.5, and the mean strength of schedule is essentially zero. Average winning
probability varies roughly between 25% and 90%. Accounting for the allocation of home
matches biases this probability by no more than 2.5 percentage points in the baseline
model with home advantage Δ = 50.




                                               8
4.2    Selection of the estimation method
Since the dataset has a panel structure, we initially considered pooled ordinary least
squares (OLS), fixed-effects (FE), and random-effects (RE) specifications. As reported
in Table 4, the FE versus pooled OLS F-test does not reject the pooled specification.
Similarly, the Breusch–Pagan Lagrange Multiplier test provides no evidence in favour
of RE over pooled OLS. The Hausman test rejects the conventional RE orthogonality
assumption. Taken together, these tests do not justify selecting the conventional RE
estimator and do not reject pooled OLS in favour of a model with unit-specific effects at
the conventional 5% significance level.
    Nevertheless, distinguishing within-club from between-club variation is important
because schedule characteristics may vary both across seasons for the same club and
systematically across clubs. The pooled OLS specification was therefore augmented
with club-specific temporal means of the time-varying regressors following the Mundlak
approach (Mundlak, 1978; Wooldridge, 2002). This implementation is consistent with
the formulation by Wooldridge (2025) of Mundlak regressions, using pooled OLS with
unit-specific time averages as additional regressors.
    Thus, the estimated specification is

      𝑆𝑖𝑡 = 𝛽0 + 𝛽1 AWP 𝑖𝑡 + 𝛽2 SoS 𝑖𝑡 + 𝛾1 HUN 𝑖 + 𝛾2 SRB 𝑖 + 𝜃1 AWP 𝑖 + 𝜃2 SoS 𝑖 + 𝜀𝑖𝑡 ,

where the terms AWP 𝑖 and SoS 𝑖 are club-specific temporal means of the corresponding time-
varying regressors and constitute the Mundlak correction. Under this parameterisation, 𝜃1
and 𝜃2 capture the difference between the between-club and within-club slopes, such that
the implied between-club slope for a variable is given by 𝛽 + 𝜃.
    Repeated observations from the same club may exhibit heteroskedasticity and within-
club dependence; hence, statistical inference is based on HC1 robust standard errors
clustered at the club level. Club-specific temporal means are jointly significant in the
baseline and sensitivity specifications (see Section 5), supporting their inclusion in the
final models.
    The estimation is conducted in R using the plm (Linear Models for Panel Data) package
(https://cran.r-project.org/web/packages/plm/index.html).


5     Results
Section 5.1 offers some descriptive statistics for the three leagues in order to help under-
standing the main characteristics of the data. The results of the baseline statistical model
are presented in Section 5.2, and sensitivity analyses are given in Section 5.3.

5.1    Preliminary data analysis
Table 5 summarises the descriptive statistics of trichotomous match outcomes for the three
leagues. As expected, home teams consistently have a higher probability of winning than
away teams; their advantage is around 15 percentage points in Hungary and Scotland, but
exceeds 20 in Serbia. The reason is that the home-away patterns are fixed at the beginning
of the season in the former two countries, while the first half of the teams after 30 rounds
(ranked 1–4 in the championship part and 9–12 in the relegation part) are guaranteed
to play more (four) home games in the Serbian league. Consequently, more home games
are positively correlated with team strength in Serbia. The range of match outcomes

                                               9
         Table 5: Match outcomes in the single round-robin (sub)tournaments
                                (a) Hungary, 2015/16–2025/26

                        Home win          Draw         Away win       Home-away gap
          Average        44.21%          27.55%         28.24%           15.98%
          Minimum        36.36%          21.21%         21.21%           04.55%
          Maximum        57.58%          37.88%         34.85%           36.36%

                     (b) Scotland, 2015/16–2025/26 (2019/20 excluded)

                        Home win          Draw         Away win       Home-away gap
          Average        45.61%          22.88%         31.52%           14.09%
          Minimum        40.91%          12.12%         21.21%            4.55%
          Maximum        53.03%          31.82%         36.36%           31.82%

               (c) Serbia, 2015/16–2025/26 (2019/20 and 2020/21 excluded)

                        Home win          Draw         Away win       Home-away gap
          Average        49.21%          23.41%         27.38%           21.83%
          Minimum        32.14%          03.57%         14.29%           03.57%
          Maximum        75.00%          46.43%         35.71%           53.57%
            Note: The championship part, contested by the top eight teams after 30 rounds,
            and the relegation part, contested by the bottom eight teams after 30 rounds,
            are treated separately.

                     (d) Scotland, 2000/01–2025/26 (2019/20 excluded)

                        Home win          Draw         Away win       Home-away gap
          Average        45.52%          24.36%         30.12%          −15.39%
          Minimum        37.88%          12.12%         19.70%          0−1.52%
          Maximum        53.03%          40.91%         40.91%          −31.82%


across the seasons is also higher in Serbia, explained by the higher randomness of single
round-robin tournaments with eight teams compared to tournaments with 12 teams.
    The share of teams playing more home games from the total number of points collected
is presented in Table 6. In Hungary and Scotland, this varies roughly between 40% and
60%, with an average of almost exactly 50%. In contrast, the mean robustly exceeds 50%
in Serbia due to the scheduling policy that favours teams performing better in the first
30 rounds. The variance is also higher in Serbia, again because of the smaller number of
teams in the single round-robin (sub)tournaments.
    Figure 1 shows the relationship between our measure of relative team strength, the
average winning probability AWP, and the dependent variable, the number of points per
match 𝑆, in the estimated models, for the primary sample. A clear positive but, naturally,
imperfect correlation can be seen. Extreme values in 𝑆 are more frequent in the Serbian
league as its relevant (sub)tournament consists of seven rounds instead of 11.




                                               10
                                      Table 6: Share of points collected by the teams with more home games

                                                                        Hungary            Scotland        Serbia
                                                   Average              50.11%              50.90%         56.91%
                                                   Minimum              41.67%              42.93%         33.77%
                                                   Maximum              58.70%              61.75%         71.43%
                                                         Notes: Hungary: All seasons from 2015/16 to 2025/26.
                                                         Scotland: All seasons from 2000/01 to 2025/26, except for
                                                         the unfinished 2019/20. Serbia: All seasons from 2015/16
                                                         to 2025/26, except for the unfinished 2019/20 and 2020/21.

                                 3


                                2.5
 Number of points per match 𝑆




                                 2


                                1.5


                                 1


                                0.5


                                 0
                                      0.2   0.25   0.3     0.35   0.4    0.45   0.5   0.55   0.6   0.65   0.7   0.75   0.8   0.85   0.9   0.95
                                                                        Average winning probability AWP
                                                                  Hungary             Scotland        Serbia

                                        Figure 1: The connection between average winning probability and
                                       the number of points per match, primary sample (2015/16–2025/26)


5.2                                   The baseline Mundlak-augmented pooled OLS estimation
Table 7 presents the results of the baseline regression, which reveals a positive and
statistically significant within-club association between AWP and sporting performance.
In particular, a 10 percentage point increase in AWP for the same club is associated with
an increase of approximately 0.16 points per match, ceteris paribus. In contrast, SoS
exhibits no statistically significant within-club association with 𝑆. The coefficient of mean
AWP is also positive and statistically significant, whereas mean SoS remains insignificant.
The sum of the within-club AWP coefficient and the mean-AWP coefficient gives an
implied between-club slope of approximately 2.935. Thus, both within-club variation and
systematic differences across clubs contribute to the observed relationship between AWP
and sporting performance. Club-specific temporal means are jointly significant, supporting
their inclusion in the Mundlak-augmented pooled OLS specification.
    Neither country indicator is statistically significant. Consequently, when performance is


                                                                                      11
Table 7: Mundlak-augmented pooled OLS estimates, primary sample (2015/16–2025/26)

 Model                          Baseline                Sensitivity              Sensitivity
 Home advantage Δ                 50                        25                       75
                                 −0.082                   −0.069                   −0.103
 Constant
                                 (0.073)                  (0.072)                  (0.074)
                                1.597***                 1.575***                 1.628***
 AWP
                                 (0.318)                  (0.315)                  (0.323)
                                  0.006                    0.014                    0.004
 SoS
                                 (0.034)                  (0.068)                  (0.023)
                                 −0.023                   −0.023                   −0.023
 Hungary
                                 (0.045)                  (0.045)                  (0.045)
                                 −0.001                   −0.001                   −0.001
 Serbia
                                  (0.05)                   (0.05)                   (0.05)
                                1.338***                 1.334***                 1.350***
 AWP (Mean AWP)
                                 (0.345)                  (0.342)                   (0.35)
                                  0.034                    0.067                    0.023
 SoS (Mean SoS )
                                 (0.065)                   (0.13)                  (0.044)
 Mundlak test                  16.138***                16.306***                 15.963***
 𝑅2                               0.426                    0.426                    0.426
 Adjusted 𝑅2                      0.417                    0.417                    0.417
 AIC                             453.624                 453.583                   453.679
 BIC                            481.494                  481.453                   481.548
 RMSE                             0.422                    0.422                    0.422
 Observations                      396                      396                      396
   Notes: The dependent variable is points per match. Scotland is the reference category. Club-
   specific temporal means of AWP and SoS are included following a Mundlak-style within–between
   decomposition. Standard errors in parentheses are HC1 robust standard errors clustered at the club
   level. AIC = Akaike information criterion; BIC = Bayesian information criterion; RMSE = root mean
   square error. Significance: * 𝑝 < 5%; ** 𝑝 < 1%; *** 𝑝 < 0.1%.


normalised and the scheduling variables are controlled for, there is no detectable conditional
difference in points per match across Hungary, Scotland, and Serbia. This is reinforced
by the joint insignificance of AWP × HUN and AWP × SRB interactions (𝜒2 (2) = 0.012,
𝑝 = 0.994).

5.3    Robustness checks
Our baseline specification computes AWP and SoS with a home advantage of Δ = 50,
which might not hold as illustrated by Table 2. To assess whether the results depend
on this choice, the model is re-estimated with Δ = 25 and Δ = 75, see Table 7. The
estimated within-club AWP coefficients remain remarkably close to the baseline coefficient.
The conclusions for SoS are equally stable, its coefficient remains statistically insignificant
in all specifications. The country indicators are also insignificant, while mean AWP is
positive and significant. Therefore, the results are robust to the value of home advantage
in terms of Elo ratings, with negligible changes in the coefficients.
    Additional specification checks are conducted using the baseline model (Δ = 50).
First, year indicators are included to account for common season-specific shocks. They

                                                12
   Table 8: Mundlak-augmented pooled OLS estimates, secondary sample (Scotland)

 Model                          Baseline                 Sensitivity              Sensitivity
 Home advantage Δ                 50                         25                       75
                               −0.221***                 −0.208***                −0.243***
 Constant
                                 (0.052)                   (0.052)                 (0.053)
                                1.408***                  1.394***                1.430***
 AWP
                                 (0.276)                   (0.273)                  (0.28)
                                  0.048                     0.097                   0.032
 SoS
                                 (0.039)                   (0.077)                 (0.026)
                                1.790***                  1.778***                1.812***
 AWP (Mean AWP)
                                 (0.266)                   (0.263)                  (0.27)
                                  0.251                      0.51                   0.166
 SoS (Mean SoS )
                                 (0.172)                    (0.34)                 (0.115)
 Mundlak test                  51.852***                 52.652***                51.236***
 𝑅2                               0.615                     0.615                   0.615
 Adjusted 𝑅2                      0.609                     0.610                   0.609
 AIC                             248.016                  247.775                  248.110
 BIC                            266.535                   266.294                  266.629
 RMSE                             0.360                     0.360                   0.360
 Observations                      300                       300                     300
   Notes: The dependent variable is points per match. Club-specific temporal means of AWP and SoS
   are included following a Mundlak-style within–between decomposition. Standard errors in parentheses
   are HC1 robust standard errors clustered at the club level. AIC = Akaike information criterion;
   BIC = Bayesian information criterion; RMSE = root mean square error. Significance: * 𝑝 < 5%; **
   𝑝 < 1%; *** 𝑝 < 0.1%.


are jointly insignificant (𝜒2 (10) = 0.848, 𝑝 > 0.999), and their inclusion essentially does
not change the principal coefficients. Second, because the three country panels do not
have identical temporal coverage, the baseline model is re-estimated using only the nine
common seasons (2015/16–2018/19 and 2021/22–2025/26), with club-specific temporal
means recalculated for the restricted sample. The coefficient of AWP remains significant
(𝛽1 = 1.723, 𝑝 < 0.001), while SoS and the country indicators remain insignificant. Thus,
our results are not driven by differences in temporal coverage.
    The analysis was repeated for the secondary sample, the Scottish Premiership from
2000/01 to 2025/26, excluding the 2019/20 season. The extended sample comprises 300
club-season observations, compared with 120 observations in the corresponding Scottish
subsample of the primary sample. Both periods were estimated using the same Mundlak-
augmented pooled OLS specification with club-clustered robust standard errors.
    The results are consistent across the two observation periods. Both AWP and mean
AWP remain positive and statistically significant with a small difference in their coefficients,
whereas neither SoS nor club mean SoS is statistically significant. The joint Mundlak
tests reject the null hypothesis that the coefficients of club-specific means are jointly zero
(𝑝 < 0.001). The models explain approximately 61.5% of the variation in points per match
in contrast to about 42.6% for the primary sample, indicating that the results of the
Scottish Premiership are less uncertain than the Hungarian and Serbian leagues.
    To summarise, excluding the pre-2015 Scottish observations from the primary cross-
country analysis does not appear to alter the main findings. Even though the insignificant

                                                 13
SoS coefficient might be due to limited sample size, the impact of scheduling asymmetry
remains below 0.1 points per match as the absolute value of SoS never exceeds 1.5
(Table 3.b), which translates to less than one point (the value of a draw) in the single
round-robin (sub)tournament containing 11 rounds.


6     Discussion and conclusion
A tournament with an even number of contestants may be unfair if the matches are
asymmetric due to some reasons, such as playing with the white pieces in chess or playing
at home in most team sports. Therefore, our paper has empirically investigated the
fairness of single round-robin tournaments. To that end, we have constructed a unique
dataset from the first division of three European football leagues, where a standard double
round-robin tournament is continued with a single round-robin (sub)tournament. This
setting allows an accurate identification of team strengths, which is crucial to analyse
whether the allocation of home games provides a detectable (dis)advantage in the number
of points collected. We have also developed a strength of schedule metric using Elo ratings
that has favourable theoretical properties.
    The research question has been studied with a Mundlak-augmented pooled OLS
regression that bridges standard random-effects and fixed-effects panel models. The
statistical estimations show a consistent picture: while the average winning probability
has a clear and robust positive effect on the number of points per match, the strength of
schedule does not impact the points at all. In the primary sample, the coefficient is even
negative, suggesting that the insignificant result is not caused by limited sample size. In
the secondary sample of the Scottish league, the strength of schedule has a positive but
insignificant effect, with a negligible (if any) impact on the final ranking.
    This finding may be surprising at first sight. After all, home advantage is well-
documented in football, and can also be seen in the descriptive statistics of the sample.
Csató and Krumer (2026) have recently examined a similar problem: the fairness of
Swiss-system chess tournaments containing an odd number of rounds. There, players with
more white games enjoy a substantial, statistically significant advantage compared to their
peers with more black games. Due to the analogy between home advantage in team sports
and white advantage in chess (van Ours, 2024), one could anticipate a positive impact
in our sample, too – but the results presented above do not support the straightforward
expectation. Consequently, using the rather complex ranking-fair schedules proposed by
Wessel et al. (2026) seems to be unnecessary in the football leagues considered here.
    However, the lack of empirical evidence does not guarantee the fairness of these
tournaments. A possible reason is that home advantage is quantified by adding the same
constant to the Elo ratings of the home team in each match. Even though all widely
used Elo variants, such as FIFA Women’s World Ranking (van Eetvelde and Ley, 2019),
Football Club Elo ratings, and World Football Elo Ratings (https://eloratings.net/)
(Gásquez and Royuela, 2016; Csató, 2022a), account for home advantage in this way, home
advantage has a team-specific component (Peeters and van Ours, 2021), which cannot
be captured by this approach. Non-transitive patterns in long-term rivalries (van Ours,
2024), bogey team relationships (van Ours, 2025), and circular triads of overperformance
(van Ours, 2026) could also interact with the allocation of the field of the games, and
may lead to unfairness when some teams benefit from a given set of home opponents.
Hopefully, our study will inspire future research on single round-robin tournaments from
these perspectives.

                                            14
Acknowledgements
The research was supported by the National Research, Development and Innovation Office
under Grants Advanced 152220 and FK 145838, and the János Bolyai Research Scholarship
of the Hungarian Academy of Sciences.


References
Bosker, J. and Gürtler, M. (2024). The impact of cultural differences on the success of elite
  labor migration—Evidence from professional soccer. Annals of Operations Research,
  341(2-3):781–824.
Csató, L. (2022a). Quantifying incentive (in)compatibility: A case study from sports.
  European Journal of Operational Research, 302(2):717–726.
Csató, L. (2022b). UEFA against the champions? An evaluation of the recent reform of
  the Champions League qualification. Journal of Sports Economics, 23(8):991–1016.
Csató, L. (2024). Club coefficients in the UEFA Champions League: Time for shift
  to an Elo-based formula. International Journal of Performance Analysis in Sport,
  24(2):119–134.
Csató, L., Kiss, L. M., and Szádoczki, Zs. (2025). The allocation of FIFA World Cup slots
  based on the ranking of confederations. Annals of Operations Research, 344(1):153–173.
Csató, L. and Krumer, A. (2026). Swiss-system chess tournaments and unfairness. Annals
  of Operations Research, in press. DOI: 10.1007/s10479-026-07412-6.
Csató, L. and Petróczy, D. G. (2025). Competitive balance in the UEFA Champions
  League group stage: Novel measures show no evidence of decline. Annals of Operations
  Research, 352(1-2):105–120.
Csató, L. and Petróczy, D. G. (2026). Are penalty shootouts better than a coin toss?
  Evidence from international club football in Europe. Journal of Sports Economics,
  27(6):713–734.
Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: A review from an
  operational research perspective. European Journal of Operational Research, 324(1):1–21.
Fecker, N. (2024). Skewed expectations in the Elo rating system: Home advantage in
  football and white advantage in chess. Bachelor thesis, ETH Zürich.
FIFA (2018). Revision of the FIFA / Coca-Cola World Ranking. https://digitalhub.f
  ifa.com/m/f99da4f73212220/original/edbm045h0udbwkqew35a-pdf.pdf.
Gásquez, R. and Royuela, V. (2016). The determinants of international football success:
 A panel data analysis of the Elo rating. Social Science Quarterly, 97(2):125–141.
Goossens, D. and Spieksma, F. C. R. (2012a). The carryover effect does not influence
 football results. Journal of Sports Economics, 13(3):288–305.
Goossens, D. and Spieksma, F. C. R. (2012b). Soccer schedules in Europe: An overview.
 Journal of Scheduling, 15(5):641–651.

                                             15
Goossens, D., Yi, X., and Van Bulck, D. (2020). Fairness trade-offs in sports timetabling.
 In Ley, C. and Dominicy, Y., editors, Science Meets Sports: When Statistics Are More
 Than Numbers, pages 213–244. Cambridge Scholars Publishing, Newcastle upon Tyne,
 United Kingdom.

Henery, R. J. (1992). An extension to the Thurstone–Mosteller model for chess. Journal
 of the Royal Statistical Society Series D: The Statistician, 41(5):559–567.

Krumer, A. and Lechner, M. (2017). First in first win: Evidence on schedule effects in
  round-robin tournaments in mega-events. European Economic Review, 100:412–427.

Lambrechts, E., Ficker, A. M. C., Goossens, D. R., and Spieksma, F. C. R. (2018).
  Round-robin tournaments generated by the Circle Method have maximum carry-over.
  Mathematical Programming, 172:277–302.

Lasek, J. and Gagolewski, M. (2018). The efficacy of league formats in ranking teams.
  Statistical Modelling, 18(5-6):411–435.

Lee, Y. H., Kim, Y., and Kim, S. (2019). Competitive balance with unbalanced schedules.
  Journal of Quantitative Analysis in Sports, 15(3):239–260.

Lenten, L. J. A. (2008). Unbalanced schedules and the estimation of competitive balance
  in the Scottish Premier League. Scottish Journal of Political Economy, 55(4):488–508.

Lenten, L. J. A. (2011). The extent to which unbalanced schedules cause distortions in
  sports league tables. Economic Modelling, 28(1-2):451–458.

Lenten, L. J. A. (2015). Measurement of competitive balance in conference and divisional
  tournament design. Journal of Sports Economics, 16(1):3–25.

Mundlak, Y. (1978). On the pooling of time series and cross section data. Econometrica,
 46(1):69–85.

Peeters, T. and van Ours, J. C. (2021). Seasonal home advantage in English professional
  football; 1974–2018. De Economist, 169(1):107–126.

Pollard, R. (1986). Home advantage in soccer: A retrospective analysis. Journal of Sports
  Sciences, 4(3):237–248.

Pollard, R. (2006). Worldwide regional variations in home advantage in association football.
  Journal of Sports Sciences, 24(3):231–240.

Pollard, R. (2008). Home advantage in football: A current review of an unsolved puzzle.
 The Open Sports Sciences Journal, 1(1).

Pollard, R. and Pollard, G. (2005). Long-term trends in home advantage in professional
  team sports in North America and England (1876–2003). Journal of Sports Sciences,
  23(4):337–350.

Rasmussen, R. V. (2008). Scheduling a triple round robin tournament for the best Danish
  soccer league. European Journal of Operational Research, 185(2):795–810.

Szczecinski, L. and Roatis, I.-I. (2022). FIFA ranking: Evaluation and path forward.
  Journal of Sports Analytics, 8(4):231–250.

                                            16
Tűű-Szabó, B. and Kóczy, L. T. (2026). A Monte Carlo framework for procedural fixture
  fairness evaluation in league competitions. Annals of Operations Research, 364(3):3259–
 3285.

van Eetvelde, H. and Ley, C. (2019). Ranking methods in soccer. In Kenett, R. S.,
  Longford, T. N., Piegorsch, W., and Ruggeri, F., editors, Wiley StatsRef: Statistics
  Reference Online, pages 1–9. Springer, Hoboken, New Jersey, USA.

van Ours, J. C. (2024). Nontransitive patterns in long-term football rivalries. Journal of
  Sports Economics, 25(7):802–826.

van Ours, J. C. (2025). On bogey teams and circular triads: Psychological factors in team
  performance. Sports Economics Review, 10:100051.

van Ours, J. C. (2026). Circular triads of overperformance in top European football leagues.
  Sports Economics Review, 14:100070.

Wessel, S., Hurkens, C., and Spieksma, F. (2026). Fair schedules for single round robin
 tournaments with ranked participants. European Journal of Operational Research,
 335(3):829–838.

Wooldridge, J. M. (2002). Econometric Analysis of Cross Section and Panel Data. MIT
 Press, Cambridge, Massachusetts, USA.

Wooldridge, J. M. (2025). Two-way fixed effects, the two-way Mundlak regression, and
 difference-in-differences estimators. Empirical Economics, 69(5):2545–2587.

Wunderlich, F. (2025). Using the wisdom of crowds in sports: How performance analysis
 in football can benefit from the information enclosed in betting odds. International
 Journal of Performance Analysis in Sport, 25(4):687–706.

Yildirim, M. and Bilman, M. E. (2025a). New rules, new game? The effects of the away
  goals rule removal and video assistant referee adoption on game dynamics in UEFA
  Champions League ties. Journal of Policy Modeling, 47(1):78–96.

Yildirim, M. and Bilman, M. E. (2025b). Second-leg home advantage no more? The
  impact of Video Assistant Referee and no away goals rule in elite soccer. Journal of
  Policy Modeling, 47(5):1097–1112.




                                            17
Appendix

        Table A.1: First matchdays of the single round-robin (sub)tournaments

                                              Country
                   Season
                               Hungary        Scotland         Serbia
                   2000/01        —          2000-12-26          —
                   2001/02        —          2002-01-12          —
                   2002/03        —          2002-12-29          —
                   2003/04        —          2004-02-10          —
                   2004/05        —          2005-01-22          —
                   2005/06        —          2006-01-21          —
                   2006/07        —          2007-01-01          —
                   2007/08        —          2008-01-19          —
                   2008/09        —          2009-01-24          —
                   2009/10        —          2010-01-30          —
                   2010/11        —          2011-01-22          —
                   2011/12        —          2012-01-14          —
                   2012/13        —          2013-01-19          —
                   2013/14        —          2014-01-18          —
                   2014/15        —          2015-01-20          —
                   2015/16    2016-03-05     2016-01-15      2016-04-15
                   2016/17    2017-03-11     2017-01-31      2017-04-14
                   2017/18    2018-03-17     2018-01-23      2018-04-13
                   2018/19    2019-03-02     2019-01-26      2019-04-12
                   2019/20    2020-02-29         —               —
                   2020/21    2021-02-26     2021-01-09          —
                   2021/22    2022-03-04     2022-01-25      2022-04-15
                   2022/23    2023-03-11     2023-01-28      2023-04-21
                   2023/24    2024-03-02     2024-01-27      2024-04-20
                   2024/25    2025-03-07     2025-01-11      2025-04-12
                   2025/26    2026-02-21     2026-01-24      2026-04-18
                     Note: Football Club Elo Ratings can be downloaded from
                     api.clubelo.com/YEAR-MM-DD.

    Table A.1 presents the first day of Round 23 in the Hungarian and Scottish leagues, as
well as the first day of Round 31 in the Serbian league. Elo ratings on these days are used
in the statistical analysis.

A    Data corrections and remarks
Some adjustments have been necessary in the Elo ratings and match results.
    In Hungary, the league uses a mirrored schedule (Goossens and Spieksma, 2012b): the
second half of the double round-robin subtournament is identical to the first, except that
the venues are inverted, and the third part copies the first half of the double round-robin
subtournament. However, in the 2019/20 season, the two matches Kaposvár vs Újpest took
place in Rounds 11 and 22, while Újpest vs Kaposvár took place in Round 33. Hence, the
result of Kaposvár vs Újpest in Round 22 (0-1) was used to calculate the number of points

                                            18
collected in Rounds 23–33 instead of the result of Újpest vs Kaposvár, and the Elo ratings
of 22 February 2020 were used for Kaposvár and Újpest regarding this particular match in
the calculation of average winning probability and strength of schedule. Analogously, in
the 2020/21 season, the two matches Fehérvár vs Puskás Akadémia took place in Rounds
4 and 15, while Puskás Akadémia vs Fehérvár took place in Round 26. Hence, the result
of Fehérvár vs Puskás Akadémia in Round 15 (1-1) was used to calculate the number of
points collected in Rounds 23–33 instead of the result of Puskás Akadémia vs Fehérvár,
and the Elo ratings of 15 December 2020 were used for Fehérvár and Puskás Akadémia
regarding this particular match in the calculation of average winning probability and
strength of schedule.
    In the 2023/24 Scottish Premiership, the match Dundee vs Kilmarnock in Round 23
was played on 3 November 2024, even though Round 23 started only on 11 January 2025
as shown in Table A.1. Consequently, the Elo ratings of 3 November 2024 were used for
Dundee and Kilmarnock regarding this particular match in the calculation of average
winning probability and strength of schedule.
    The Serbian club Javor Ivanjica/Javor Matis played in the first division in five out
of the nine seasons in our sample. Between 2015/16 and 2017/18, it is called Loznica in
Football Club Elo Ratings; between 2022/23 and 2023/24, it is called Ivanjica in Football
Club Elo Ratings; thus, Football Club Elo Ratings consider it two separate teams.




                                           19

