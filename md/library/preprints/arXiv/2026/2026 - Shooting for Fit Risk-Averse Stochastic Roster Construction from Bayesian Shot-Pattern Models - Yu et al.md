<!-- source: library/preprints/arXiv/2026/2026 - Shooting for Fit Risk-Averse Stochastic Roster Construction from Bayesian Shot-Pattern Models - Yu et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.33820 -->
<!-- authors: Yue Yu, Cong Zhang, David Crandall, Guanyu Hu -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-26; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Shooting for Fit: Risk-Averse Stochastic Roster Construction from Bayesian Shot-Pattern Models

                                            Shooting for Fit: Risk-Averse Stochastic Roster Construction from
                                                              Bayesian Shot-Pattern Models
                                                           Yue Yu∗          Cong Zhang†            David Crandall‡            Guanyu Hu§
arXiv:2611.33820v1 [stat.AP] 25 Nov 2026




                                                                                               Abstract
                                                        Roster construction is a critical decision problem in professional basketball, requiring teams
                                                   to balance player quality, player complementarity, and financial constraints under uncertainty.
                                                   Existing roster optimization models primarily rely on individual player ratings and aggregate
                                                   performance statistics, which provide limited information about how players’ offensive contribu-
                                                   tions vary with their teammates. Recent advances in player-tracking technology have enabled
                                                   statistical analyses of spatial shooting patterns, but these insights have rarely informed roster
                                                   construction. We bridge this gap by developing a data-driven, risk-averse two-stage stochastic
                                                   optimization framework for NBA roster construction. We first develop a Bayesian modeling
                                                   framework that combines player statistics and spatial shot-chart data to identify player roles and
                                                   estimate how teammate composition influences shot selection, shooting frequency, and scoring
                                                   efficiency. The resulting model provides uncertainty-quantified offensive values for hypothetical
                                                   five-player lineups, including combinations that have never played together. We then formulate
                                                   roster construction as a two-stage stochastic mixed-integer program that optimizes player acquisi-
                                                   tions under NBA salary-cap regulations while allowing lineup playing-time allocations to adapt to
                                                   uncertain player roles. We evaluate the framework using 240 team-offseason decisions over eight
                                                   seasons and two additional held-out seasons. The results demonstrate that incorporating spatial
                                                   shooting compatibility substantially changes optimal roster decisions and improves predicted
                                                   offensive performance relative to approaches based on individual player values. We further find
                                                   that flexibility in allocating playing time across lineups absorbs much of the uncertainty about
                                                   player roles. Our findings highlight how detailed spatial shooting information can be translated
                                                   into actionable roster decisions through stochastic optimization.

                                           Keywords: OR in sports; stochastic programming; roster construction; shot selection; Bayesian
                                           modeling


                                           1       Introduction
                                           Constructing a competitive roster is one of the most consequential decisions in professional basketball.
                                           Each offseason, National Basketball Association (NBA) teams must determine which players to
                                           retain, acquire, or release while balancing individual player quality, team compatibility, and complex
                                           financial constraints. These decisions have motivated a substantial literature in operations research,
                                           where roster construction is typically formulated as a constrained optimization problem involving
                                               ∗
                                                 Department of Statistics, Indiana University; email: yyu3@iu.edu
                                               †
                                                 School of Economics, University of Nottingham Ningbo; email: cong.zhang@nottingham.edu.cn
                                               ‡
                                                 Department of Computer Science, Indiana University; email: djcran@iu.edu
                                               §
                                                 Department of Statistics and Probability, Michigan State University; email: huguanyu@msu.edu


                                                                                                   1
player selection, performance evaluation, and resource allocation (Boon and Sierksma, 2003; Pantuso,
2017; Muniz and Flamand, 2023). However, the success of a roster depends not only on the individual
abilities of its players but also on how players’ offensive contributions reinforce or constrain one
another. In July 2019, for example, the Los Angeles Clippers signed Kawhi Leonard, the most
valuable player of the previous NBA Finals, and traded a promising young guard, a starting forward,
and five first-round draft picks to acquire Paul George, who had finished third in MVP voting the
previous season. Although the pairing was widely expected to produce a championship contender,
it ultimately failed to deliver a title. This example illustrates a fundamental challenge in roster
construction: how to identify player combinations in which individual abilities reinforce one another
and translate into greater value for the team as a whole.
    A central difficulty is that basketball performance is inherently interactive. With only one ball
available, the offensive opportunities of one player depend on the tendencies and decisions of his
teammates. In this sense, players can act as substitutes or complements in offensive production.
Two players who favor similar shooting locations may compete for scoring opportunities, whereas a
perimeter shooter may create additional space for teammates who attack the basket. A playmaker
who attracts defensive attention may also improve the quality of shots available to others. Con-
sequently, a player’s marginal contribution to team performance depends on the composition of
the roster, and the same player may contribute substantially different value across different rosters.
Previous studies have recognized the importance of player interactions through lineup synergy,
adjusted player ratings, and passing networks (Maymin et al., 2013; Bu et al., 2019; Kalman and
Bosch, 2020; Grassetti et al., 2021; Yamada and Fujii, 2024). Nevertheless, anticipating how players
will perform together remains difficult, particularly when evaluating potential acquisitions who have
never played with the current roster. These decisions must also be made before the season begins
and under salary-cap regulations that restrict feasible player combinations. In a typical season,
players new to a team account for approximately one-third of its playing minutes, while a single
star contract can consume a substantial share of the team’s payroll. Effective roster construction
therefore requires a framework that accounts for player compatibility, financial feasibility, and
uncertainty about future lineup performance.
    A substantial body of operations research has developed optimization approaches to roster
construction and related player selection problems. Early models primarily relied on traditional
player information, including positions, individual ratings, and aggregate performance statistics.
For example, Boon and Sierksma (2003) match the quality required at each position with the
quality supplied by available players. In football, Pantuso (2017) formulate squad composition as a
stochastic optimization problem with uncertain player values, while Pantuso and Hvattum (2021)
incorporate chance constraints to maintain financial sustainability. More recently, Villafuerte and
Aros-Vera (2026) combine machine learning and optimization to construct financially sustainable
squads. In baseball, Chan and Fearing (2019) investigate the value of players who can cover
multiple positions, while Haugh and Singal (2021) formulate daily-fantasy lineup selection as a
portfolio optimization problem under uncertainty. Basketball-specific studies include Muniz and
Flamand (2023), who optimize draft selections, trades, and free-agent acquisitions while accounting
for synergy between player archetypes, and Zhang et al. (2026), who develop a multiseason franchise
management framework using distributionally robust optimization. Related research has examined
individual player valuation (Müller et al., 2017; McHale and Relton, 2018; Kharrat et al., 2020). More
broadly, roster construction shares important features with workforce planning under heterogeneous
skills (De Bruecker et al., 2015), where long-term personnel commitments must be coordinated


                                                  2
with flexible operational assignments (Malaki et al., 2023). Despite these developments, club-level
roster decisions have received comparatively less attention than league-level optimization problems
involving scheduling, tournament design, seeding, and ranking (Devriesere et al., 2025).
    Although existing optimization models provide useful tools for player selection, their evaluation
of candidate rosters is generally based on individual player values or relatively coarse measures of
compatibility. Player contributions are often represented by aggregate statistics, such as scoring
averages, shooting percentages, and player ratings, while interactions are captured through predefined
player types or pairwise synergy parameters. Such representations may overlook important differences
in offensive playing styles. For example, two players with similar scoring averages and shooting
percentages may have very different spatial shooting patterns. One may primarily attempt shots
near the basket, whereas another may rely heavily on perimeter jump shots. Differences in spatial
shooting patterns can substantially affect player compatibility, even when players have similar
aggregate statistics. Moreover, teammate composition may influence not only where a player shoots
but also how frequently he shoots and how efficiently he scores. Understanding these effects is
essential for evaluating hypothetical lineups, yet conventional player-level summary statistics provide
limited information about them.
    Recent developments in player-tracking technology and the availability of high-resolution basket-
ball data offer new opportunities to address these limitations. Modern tracking systems and detailed
play-by-play records provide increasingly rich information about shot locations, shooting outcomes,
player movements, and the identities of teammates and opponents on the court. In particular,
spatial shot-chart data characterize where players attempt shots and how successfully they score
across different court locations, providing a more detailed representation of offensive behavior than
traditional aggregate statistics. These advances have stimulated a growing statistical literature
on the spatial analysis of basketball performance. For example, Reich et al. (2006), Miller et al.
(2014), and Jiao et al. (2021) develop statistical models to characterize spatial shooting patterns,
while Hu et al. (2021), Wong-Toi et al. (2023), and Yin et al. (2023) investigate clustering methods
for identifying players with similar shot-selection behavior. Other studies develop spatial models
that borrow information across neighboring court locations (Yin et al., 2022) or evaluate player
contributions through expected points (Williams et al., 2025).
    The availability of player-tracking data has also enabled more detailed investigations of offensive
and defensive interactions. For instance, Franks et al. (2015) and Cervone et al. (2016) use
spatial tracking information to study defensive effects and possession values, while Sandholtz et al.
(2020) examine the offensive consequences of suboptimal shot allocation. These developments
demonstrate that high-resolution basketball data can reveal aspects of individual performance and
team interactions that are not apparent from conventional summary statistics. From a modeling
perspective, the composition of teammate roles can also be characterized using compositional data,
for which the effects of individual components are interpreted relative to the others (Li et al., 2023;
Meng et al., 2026; Deng et al., 2026). Recent developments in compositional regression further allow
components with similar effects to be identified and grouped (Xu and Hu, 2026).
    Despite substantial progress in statistical modeling of basketball shot charts and player-tracking
data, these developments have not been fully incorporated into roster construction decisions.
Existing shot-chart studies primarily focus on modeling spatial shooting behavior, clustering players,
evaluating individual performance, or understanding lineup interactions. In contrast, the roster
construction literature continues to rely largely on aggregate player characteristics and summary
performance measures. In particular, while previous approaches have considered compatibility


                                                  3
through player archetypes or observed lineup outcomes, they do not directly exploit spatial shooting
patterns to predict how a player’s shot selection, shot frequency, and shooting efficiency vary
with teammate combinations. This creates a gap between the information available from modern
basketball tracking systems and the information used in roster optimization. Bridging this gap
requires a framework that translates spatial shooting behavior into the offensive value of hypothetical
lineups and integrates those values into constrained roster decisions.
    In this paper, we address this gap by developing an integrated statistical and optimization
framework that uses spatial shot-chart data to guide NBA roster construction. To the best of our
knowledge, this is the first study to directly incorporate spatial shot-chart information into a roster
optimization framework for evaluating hypothetical player combinations and making acquisition
decisions. Our central idea is to estimate how each player’s offensive contribution varies with
teammate composition, rather than treating individual player values as fixed across potential
rosters. By linking spatial statistical modeling with stochastic optimization, the proposed framework
translates detailed player-level shooting information into actionable roster recommendations.
    The proposed approach follows the decision-making process of an NBA front office, as illustrated
in Figure 1. We first characterize players using offensive roles learned from traditional performance
statistics and spatial shot charts from the previous season. These roles provide transferable
representations of playing styles and enable the evaluation of potential acquisitions who have never
played with the current roster. We then develop a Bayesian shot-pattern model that estimates how the
roles of a player’s four teammates influence his shot locations, shot frequency, and shooting efficiency.
The estimated relationships are used to construct an offensive value function for any hypothetical
five-player lineup, expressed in expected points per 100 possessions, while also accounting for
posterior uncertainty about its performance.
    We subsequently incorporate these lineup values into a risk-averse two-stage stochastic mixed-
integer optimization model. In the first stage, the model determines which players to retain or acquire
subject to salary-cap regulations and transaction constraints. In the second stage, it allocates playing
time across feasible lineups under different realizations of uncertain player roles. This formulation
distinguishes long-term roster commitments from the operational flexibility available to coaches,
who can adjust lineup rotations after observing how players perform together. Consequently, the
framework jointly accounts for spatial shooting compatibility, uncertainty in player roles, and the
flexibility of playing-time allocation.
    We evaluate the proposed framework through a retrospective analysis of roster decisions for
all 30 NBA teams across eight offseasons from 2016 to 2023, yielding 240 team-offseason decision
problems. For each offseason, the model uses only information available at the time of the decision
and compares its recommended roster with the roster actually assembled through trades and
free-agent signings. To assess out-of-sample generalizability, we further evaluate the framework on
two additional seasons held out throughout model development, using a frozen implementation.
The empirical findings highlight the importance of accounting for teammate compatibility when
constructing competitive rosters. Compared with methods that primarily value players using
individual performance measures, our framework recommends substantially different rosters with
higher predicted offensive performance. The estimated improvements would move a league-average
offense to about sixth in the league. We also find that flexibility in allocating playing time across
lineups allows teams to accommodate much of the uncertainty associated with player roles. A case
study of the 2019 Los Angeles Clippers further illustrates how spatial shooting compatibility can
change the evaluation of high-profile roster decisions.


                                                   4
     Data, season t            Statistical model           Decision model                Evaluation
        Section 2                  Section 3.2             Sections 3.3 and 3.4        Sections 4 and 5


   Box scores, minutes           Roles: seven,             Contracts and the          Plans against the
      and positions           learned by Bayesian           salary rules of            real rosters of
     of every player               clustering                season t + 1              240 offseasons


   Every shot: where,             Shot model:              Stage 1, summer:
                                                                                     Plans against those
   how it was created,          teammates shift              keep, re-sign,
                                                                                      of simpler models
    made or missed            attempts and makes              sign, trade
                                                                     roster
                                                            Stage 2, season         Two held-out seasons
   Every stint: the ten       Lineup values Vℓd values
                                                           t + 1: minutes in         and three famous
   players on the floor       in each role draw d
                                                             each role draw              summers

Figure 1: The engine for one team-offseason, in four layers. Data from season t feed the statistical models,
whose lineup values enter the two-stage stochastic program; its plans are then compared with the rosters
teams built and with the plans of simpler models. The models are fitted on data up to season t, and the
posterior draws of the roles are the scenarios of the program.


    Our study makes three main contributions. First, we bridge the gap between statistical analysis
of spatial shot charts and roster optimization by developing a shot-chart-driven lineup valuation
framework. Unlike existing roster construction approaches that primarily rely on aggregate player
ratings or coarse synergy measures, our model explicitly characterizes how teammate composition
affects shot selection, shot frequency, and shooting efficiency. This provides a transferable framework
for evaluating hypothetical lineups, including combinations of players who have never played together,
while quantifying uncertainty in their offensive performance.
    Second, we develop a risk-averse two-stage stochastic mixed-integer optimization framework
that converts shot-based lineup values into roster construction decisions. The first stage optimizes
player acquisitions under the salary regulations of three collective bargaining agreements, while the
second stage adjusts playing-time allocations across uncertain scenarios. This formulation integrates
player compatibility, financial constraints, and adaptive lineup management within a unified decision
framework.
    Third, we provide a comprehensive empirical evaluation using 240 historical team-offseasons and
two additional held-out seasons. Through comparisons with actual front-office decisions, predictive
benchmarks, and component-level analyses, we quantify the decision value of spatial shooting
information, teammate compatibility, uncertainty modeling, and lineup flexibility. These results
illustrate how high-resolution sports data can improve not only statistical evaluation but also
downstream optimization decisions.
    From a methodological perspective, our framework builds on the predict-then-optimize paradigm
(Bertsimas and Kallus, 2020; Elmachtoub and Grigas, 2022) by integrating Bayesian predictions with
stochastic optimization. Rather than training the predictor directly for downstream optimization,
we investigate which components of a rich predictive model materially change the resulting decisions.
We quantify their decision value using established measures from stochastic programming (Birge and
Louveaux, 2011). Posterior draws of player roles generate scenarios for sample average approximation
(Kleywegt et al., 2002), while a tail-risk objective protects against unfavorable outcomes (Rockafellar
and Uryasev, 2000). We also examine the robustness of recommended rosters to defensive adjustments


                                                     5
through a budgeted uncertainty set (Bertsimas and Sim, 2004).
   The remainder of the paper is organized as follows. Section 2 describes the data and research
questions. Section 3 presents the shot-pattern model, lineup valuation, and stochastic optimization
framework. Section 4 evaluates the proposed approach using historical and held-out NBA seasons.
Section 5 examines three case studies involving major roster decisions. Section 6 discusses managerial
implications and concludes the paper. Appendices A–F detail the data, the role and shot models,
the salary-rule constants, the calibration of the stress test and the frozen evaluation protocol.


2     Data and research questions
2.1   Data
All data used in this study are public. Play-by-play logs, shot locations, box scores and rotation
records come from NBA.com/Stats, the league’s official statistics website (National Basketball
Association, 2026), accessed through the Python client nba_api (Patel, 2018), for eleven regular
seasons, 2015-16 to 2025-26, and the playoffs of 2015-16 to 2024-25; the nine seasons from 2015-16
to 2023-24 alone hold 1.88 million shots. On-court lineups are reconstructed from rotation and
play-by-play records, so that every shot is linked to the ten players on the floor. Salaries, players’
moves and contract status, team offensive ratings and playoff results come from Basketball-Reference
(Sports Reference LLC, 2026); the salaries of 2024-25 and 2025-26 come from its contracts page
as archived after each season’s opening night (Sports Reference LLC, 2025). The amounts of the
salary cap, the tax line and the exceptions of each league year come from the league’s press releases
(NBA Communications, 2024) and contemporary press reports (Hoops Rumors, 2025; Basketball
Insiders, 2016), and the salary rules from the collective bargaining agreements of 2011, 2017 and
2023 (National Basketball Association and National Basketball Players Association, 2011, 2017,
2023).
     To evaluate how teammates affect a player’s opportunities, we describe every shot by where
it is taken and how it is created. The court is divided into five zones (the restricted area at the
rim, the rest of the paint, mid-range, the corner three and the above-the-break three). Each shot is
categorized by its movement type: a drive to the basket, a cut, a pull-up jumper off the dribble, a
post-up or touch in the paint, or a spot-up shot off a pass. Crossing the five zones with the five
movement types yields 25 cells. Movement type separates the shots a player creates for himself
from the shots created by his teammates: a corner three off a pass and a pull-up three from that
spot depend on very different teammates. Zones are calculated from recorded shot coordinates, and
movement types come from play-by-play descriptions, which we checked season by season against
the league’s player-tracking data (National Basketball Association, 2026; Appendix A).
     The shot data show why offensive production cannot be evaluated by adding individual shot
charts together. Each movement type has its own geography (Figure 2(a)): drives and cuts end
near the basket, spot-ups fill the corners and the arc, and pull-ups spread across the half court.
Individual players differ even more (Figure 2(b)). Some take most of their shots off the dribble
across all zones, others wait for spot-ups in the corners, and others finish at the rim. Because five
players share one ball, these individual tendencies cannot simply be added up: how many shots a
player takes in any cell depends directly on whether his teammates want those same shots.
     The decision engine is evaluated over eight pairs of seasons. Models estimated on one season
make the decisions for the following summer, from 2015-16 → 2016-17 to 2022-23 → 2023-24. Two


                                                  6
All attempts                                  Drive · 28% of attempts                           Cut · 6% of attempts




Pull-up · 23% of attempts                     Post / paint · 12% of attempts                    Spot-up · 32% of attempts




                             0.01                  0.1                  1                              10
                                       Share of the panel's attempts per 1.5 ft hex (%)

(a) Where the league’s shots come from, for all attempts and for each movement type, in 2022-23.
Darker hexagons hold a larger share of the panel’s attempts.

Jayson Tatum                        Killian Hayes                      Malik Beasley                        Royce O'Neale
Primary creator                     Playmaker                          Shooter                              Spot-up connector




   36%         29%        26%        20%        48%          28%       15%       24%          58%            23%                61%
                  1,559 attempts                       815 attempts                          931 attempts                   593 attempts


Lauri Markkanen                     Joel Embiid                        Nic Claxton
Two-way forward                     Hub big                            Rim big                                Movement type
                                                                                                                  Drive
                                                                                                                  Cut
                                                                                                                  Pull-up
                                                                                                                  Post / paint
                                                                                                                  Spot-up
                                                                                                                  Made
 19%        16%        43%           22%        35%     14% 23%            26%         33%      41%               Missed
                  1,145 attempts                      1,328 attempts                         587 attempts

(b) One representative player of each role of Table 1 in 2022-23: every shot, by movement type, made
(filled) or missed (open). The bar under each court gives the player’s mix of movement types.

                                                 Figure 2: The shot data.




                                                                       7
later seasons, 2024-25 and 2025-26, were kept aside throughout model development: nothing from
them was opened until the entire method had been frozen, providing a clean final test (Section 4.4).

2.2   Research questions
The patterns in the shot data motivate the four research questions this paper addresses. Because
players differ sharply in where and how they shoot, and because five players share one ball, a
newcomer inevitably changes the shots of the teammates already on the roster. A front office must
therefore determine whether these mutual adjustments can be predicted for lineups that have never
played together, whether acting on those predictions leads to better rosters, and which components
of the model actually alter the resulting decisions. We investigate four questions in sequence:
 Q1. Can teammate fit be predicted? Do the roles of a player’s teammates shift his shots in ways
       that hold in the next season, carry over to players who change teams, and track how well
       teams score? (Section 4.1)
 Q2. Does planning for fit build better rosters? Given the same information, options and salary
       rules, does the engine’s plan improve on the roster each team actually assembled, and does
       the improvement hold in seasons kept aside? (Sections 4.2 and 4.4)
 Q3. Which parts of the model change the decision? How much does a front office lose if it ignores
       teammate effects, plans for each player’s average role instead of the uncertainty about roles,
       ignores how teammates crowd the same shots, or ignores playoff defenses, and how many
       rosters are nearly as good as the best? (Section 4.3)
 Q4. What does the engine say about decisions that shaped the league? How does it read Cleveland’s
       summer of 2017, the Clippers’ of 2019, Brooklyn’s of 2020 and the moves of 2023, and what
       lies outside its view? (Section 5)
    The first question evaluates the statistical shot model, while the remaining three address the
optimization decisions. Throughout, a richer model earns its place only if the plans it produces
differ from, and score better than, the plans of a simpler one.


3     The roster construction model
This section builds the decision model for one team-offseason. Section 3.1 describes the decision a
front office faces, Section 3.2 turns shot patterns into the value of any lineup, Section 3.3 formulates
the two-stage stochastic program, and Section 3.4 explains how we solve the program and evaluate
its plans.

3.1   Problem description
An NBA offseason forces a front office to make binding personnel commitments before the coaching
staff can observe the new players on the court. Every summer, once the playoffs end, each team
enters a transaction window. The front office holds the contracts of some players, decides whether
to re-sign its own free agents, and pursues outside signings or trades. Three practical questions
govern this summer planning: which incumbent free agents to retain, whether to spend cap space or
over-the-cap exceptions, and which trade packages satisfy the league’s salary-matching rules. Once
the season opens, the head coach distributes playing time across five-player lineups as he observes
which player combinations work well together.



                                                   8
    This operational calendar creates a natural two-stage decision structure separated by time and
information. During the summer offseason, the front office sets the roster for season t + 1 without
knowing how incoming and returning players will blend on the court. During the subsequent season,
the coach observes on-court chemistry and adjusts playing time across lineups. Our mathematical
formulation follows the same sequence. We estimate all components from data up to season t,
including player roles, the shot model, and candidate lineup values. The first stage selects the roster
for season t + 1 under the collective bargaining rules of the coming league year. The second stage
determines the playing time of each lineup across D = 20 posterior draws of player roles, where each
draw represents a plausible scenario of how the players will be used. In stochastic programming
terms, the roster represents the first-stage decision, lineup minutes provide the recourse, and the
posterior role draws serve as scenarios. We solve each team-offseason as a single program across all
scenarios simultaneously. Because these scenarios originate directly from the Bayesian role model,
they express the model’s own uncertainty about how players will be used; they are not noise added
for the optimization.
    To define the available personnel choices, we assemble the team’s candidate options after season
t into a pool P. This pool includes all players under contract for season t + 1, including players
returning from injury. It also includes any player the team traded away during the summer, since
the club could have chosen to keep him. The pool also contains the team’s own free agents, whom
the club can re-sign at their actual realized salaries. To evaluate external additions, the pool
incorporates a market of twelve outside free agents and trade targets. This market begins with the
players the team actually acquired that summer. We complete the market with outside movers who
logged the most minutes that year, provided the team could afford them by trade or free agency.
Using actual movers at their realized salaries keeps player availability realistic. The optimization
engine can always replicate the moves the front office executed, but it can also choose differently. A
typical pool contains about 24 players.

3.2   Lineup values from shot patterns
To compare potential rosters, a front office must evaluate what five players would produce together,
including combinations that have never shared the court. Historical lineup records cannot answer
this question, because prospective trades and signings create five-player combinations with zero
recorded minutes. We therefore construct the value of any five-player lineup in three steps using
data up to season t. We focus here on the practical implications for front-office decisions, and report
the full statistical specifications in Appendices B and C.

Roles. When evaluating an unfamiliar outside player, a front office cannot measure his chemistry
with existing teammates directly. The front office can, however, determine what kind of player he is,
because knowing how a player type alters teammate shots allows the team to value any newcomer
by his role. We describe each player-season by one of K = 7 roles using a Bayesian mixture model
that groups players with similar box-score statistics and shot charts, in the tradition of Bayesian
clustering of shot charts (Hu et al., 2021; Yin et al., 2023). We chose seven roles for their use to a
front office rather than for forecasting accuracy, because front offices need a small set of recognizable
archetypes: the statistical fit improves little after five or six roles, each role captures a substantial
share of league minutes, and the seventh role separates two distinct forward archetypes that front
offices treat differently. Table 1 defines the seven roles, and Figure 2(b) illustrates a representative
player for each role. Rather than assigning a fixed label, the model gives each player a probability

                                                   9
        Table 1: The seven roles and their share of league minutes (fit through 2022-23 season).

 Role                  Minutes     How the role plays                   Examples
 Primary creator       20%         pull-ups from every zone, high       Edwards, Tatum, LaVine
                                   usage, many assists
 Two-way forward       18%         balanced wings and forwards          Mikal Bridges, Scottie Barnes,
                                                                        Harrison Barnes
 Shooter               15%         spot-up and pull-up threes           Caldwell-Pope, Strus, Huerter
 Spot-up connector     12%         corner threes and cuts from          O’Neale, Finney-Smith
                                   low-usage forwards
 Rim big               12%         cuts and finishes at the rim,        Gobert, Jarrett Allen, Claxton
                                   rebounds, blocks
 Playmaker             12%         drives and assists from guards and   Smart, Lowry, Draymond Green
                                   point forwards
 Hub big               10%         post-ups, paint touches and          Jokić, Sabonis, Vučević
                                   passing from bigs


distribution across the seven roles. A player who split his playing time between creating his own shot
and spotting up retains probability mass on both roles, while a player with limited minutes retains
wide uncertainty. The optimization engine draws 20 samples from these posterior distributions as
scenarios. Each draw represents one plausible way player roles could unfold across the league next
season.

Shots. A front office must also account for how incoming players redistribute field-goal attempts
across the roster. Basketball is played with one ball, so adding a second creator takes shots away
from players who already create offense. The shot model predicts how frequently a player shoots
from each of the 25 court cells, and how often he scores, conditional on his on-court teammates. For
player q in a stint, defined as an unbroken stretch of play with the same ten players on the floor, his
attempts in cell c follow a Poisson distribution with rate per 100 possessions

                     Aqc = 100 exp µc + sqc + βc⊤ bq + (a⊤          ⊤
                                                         q ug(c) )(bq vg(c) ) + γ Oqc .                  (3.1)
                                    


The league baseline rate µc and the player’s profile sqc describe his baseline attempt frequency beside
average teammates. The vector bq averages the role probabilities of his four on-court teammates, so
βc⊤ bq captures how the surrounding mix of roles shifts his attempts in cell c. Because teammate
role probabilities sum to one, each coefficient represents a relative shift (Li et al., 2023), defined
as the change in his attempt rate when an average teammate is replaced by a teammate of a
specific role. The bilinear term (a⊤q ug(c) )(bq vg(c) ) allows this shift to depend on the shooter’s own
                                               ⊤

role aq through a low-rank interaction within cell group g. This interaction captures asymmetric
adjustments: adding a second creator takes shots from an existing creator, but can generate open
shots for a spot-up shooter. The spatial crowding term γ Oqc accounts for congestion that broad
roles miss. Here Oqc denotes how often his four teammates shoot from that same cell, so a negative
coefficient γ means that players who favor identical spots shoot less when sharing the court. A
logistic model with matching teammate covariates estimates whether each attempt is made. Court
cells that respond similarly to teammates share strength through the spatially constrained Bayesian
clustering of Meng et al. (2026), the precisions of the teammate effects are chosen by the marginal
likelihood on season t itself, and the model is fitted on every stint of the season (Appendix C). We

                                                    10
define two benchmark models for comparison: shooter-only rates, which retain individual profiles
without teammate effects, and additive roles, which keep teammate roles but drop both the shooter
interaction and the crowding term. We refer to formulation (3.1) as the full model.

Lineup values. To compare alternative rosters during summer negotiations, a front office needs a
single performance metric for each five-player lineup. For any candidate lineup ℓ and posterior role
draw d, the shot model supplies expected attempts and make probabilities for each player across all
25 cells. We multiply expected attempts by make probabilities and shot point values (ptsc , equal
to two or three points), and add expected points from free throws drawn by each player. This
calculation yields the lineup’s expected shot points, denoted Πℓd , over Nℓd total attempts per 100
possessions. The engine values each lineup by
                                              Πℓd
                                      Vℓd =       min{Nℓd , N̄ },                                (3.2)
                                              Nℓd
which multiplies points per shot by effective shot volume, capping total attempts at the league
average N̄ . The cap reflects how the game works. A lineup that cannot generate shots is charged for
the shots it does not take, which preserves the value of shot creators. Conversely, five high-volume
scorers cannot take more than a game’s worth of shots, so stacking them earns nothing extra.
Because the underlying model predicts how attempts shift with teammate composition, this value
function directly prices player fit. The same player contributes more to a lineup that needs his
shot creation than to a lineup that already possesses it. We apply two adjustments so that these
valuations travel to rosters that do not exist yet. We damp predicted shot adjustments for newly
acquired players by κ = 0.75, an empirical transfer factor estimated from players who changed teams
(Section 4.1). We also value any player who missed season t due to injury using his performance
from season t − 1. With lineup values Vℓd established for all candidate lineups and role draws, the
roster optimization problem is fully specified.

3.3   The two-stage stochastic program
We formulate the offseason decision of Section 3.1 as a risk-averse two-stage stochastic mixed-integer
program. Table 2 summarizes the mathematical notation. The candidate pool P combines players
under contract for season t + 1 (R), the team’s own free agents (O), and outside market candidates
from free agency (F) and trades (T ). The binary variable ki ∈ {0, 1} indicates whether player i ∈ P
is on the roster for season t + 1, while yi ∈ {0, 1} indicates whether he enters the active rotation.
The set L contains all feasible candidate lineups of five players from P that maintain positional
balance by including at least one guard, at most two bigs, and at most nin outside additions. In
the second stage, after role uncertainty resolves into scenario d ∈ D, the coach selects the recourse
variables mℓd ≥ 0, representing the share of team possessions played by lineup ℓ in draw d. The
team’s offensive performance under scenario d is the minutes-weighted value of its active lineups:

                                          Td =                                                   (3.3)
                                                 X
                                                       Vℓd mℓd .
                                                 ℓ∈L



Objective. A front office cannot rely on expected scoring alone. An NBA season provides only
one chance to compete, so a roster that scores well on average but fails when player roles conflict is


                                                  11
                                        Table 2: Notation of the two-stage program.

Sets
P =R∪O∪F ∪T                                          the team’s pool: players under contract for t + 1, its own free agents,
                                                     outside free agents and trade targets
F+ ⊆ F                                               outside free agents above the minimum salary
G, B ⊆ P                                             guards and bigs
A⊆R                                                  protected players: All-NBA in season t or t − 1 and under contract
L                                                    candidate lineups: five players of P, at least one guard, at most
                                                     two bigs, at most nin from F ∪ T
D                                                    posterior role draws, the scenarios, |D| = D = 20
C                                                    the 25 cells of the court (zone by movement type)
Parameters
Vℓd                                                  value of lineup ℓ in draw d, points per 100 possessions, from (3.2)
Si , S0                                              next season’s salary of player i; salaries of the rest of the roster
                                                     ($M)
P̄                                                   the owner’s payroll limit: the first apron, or the team’s actual
                                                     payroll if higher
nin , nout                                           market players brought in and players under contract let go, at
                                                     most
f , f , m̄                                           a rotation player’s minimum and maximum share of possessions,
                                                     and a lineup’s maximum (10%, 75%, 35%)
ρ, α                                                 weight on the tail term and the tail share (0.5 and 0.2)
Γ, ω                                                 cells an opposing defense may attack, and the weight on the stress
                                                     loss
λℓdc                                                 value lineup ℓ loses in draw d, per unit of its possession share, when
                                                     cell c is attacked
Cap, RE                                              the salary cap and the room exception
MLE, MLEtax , BAE                                    the mid-level, taxpayer mid-level and bi-annual exceptions
Apron1 , Apron2 , Line                               the first and second aprons; the line above which trades follow the
                                                     narrow rule (the tax line, or the first apron from 2023-24)
First-stage decisions
ki ∈ {0, 1}                            player i is on the roster for t + 1 (kept, re-signed or acquired)
yi ∈ {0, 1}                            player i is in the rotation
z room , z hard , z exc , z line , z band ∈ {0, 1}
                                       salary modes: the team uses cap room; is hard-capped at the first
                                       apron; uses an exception under the 2023 agreement; ends under the
                                       line; uses the third trade band
xi ∈ {0, 1}                            player i moves in the room phase: sent away to clear room (i ∈ R)
                                       or absorbed into room (i ∈ T )
Second-stage decisions and auxiliary variables
mℓd ≥ 0                                share of possessions played by lineup ℓ in draw d
η, ξd ≥ 0                              threshold and shortfalls of the tail term
πd , qdc ≥ 0                           dual variables of the playoff stress test




                                                                  12
a risky bet. To balance average performance against downside volatility, we optimize a weighted
combination of expected offensive value, conditional value at risk across unfavorable scenarios, and
expected losses from targeted playoff defenses:
               1 X              1 X       ω X
 max (1 − ρ)         Td + ρ η −        ξd −       SLd ,                            ξd ≥ η − Td , ξd ≥ 0 (d ∈ D). (3.4)
               D d∈D            αD d∈D      D d∈D

The second term models downside risk using the linear formulation of conditional value at risk
established by Rockafellar and Uryasev (2000). In this formulation, the auxiliary variable η represents
the value-at-risk threshold at quantile α, while ξd ≥ 0 measures the performance shortfall below
that threshold in scenario d. At optimality, the expression η − αD
                                                                 1 P
                                                                      d∈D ξd exactly equals the mean
offensive value across the worst α share of draws. This linear representation eliminates non-smooth
minimum operators and keeps the stochastic program computationally tractable as a mixed-integer
linear program. We place equal weight on expected performance and tail risk by setting ρ = 0.5,
and focus on the lowest quintile of outcomes by setting α = 0.2, which evaluates the four worst
scenarios among the twenty draws. The third term incorporates the stress loss SLd from defensive
countermeasures, which we define below; our primary roster optimizations set ω = 0.

Roster and rotation. A front office must respect strict structural rules governing roster size,
positional depth, transaction volume, and financial capacity. We capture these requirements through
the first-stage constraints (3.5)–(3.7):

                 yi ≤ ki (i ∈ P),             8≤           yi ≤ 10,             yi ≥ 3,          yi ≥ 2,          (3.5)
                                                     X                    X                X

                                                     i∈P                  i∈G              i∈B

                                                    (1 − ki ) ≤ nout ,      ki = 1 (i ∈ A),                       (3.6)
                     X                        X
                          ki ≤ nin ,
                 i∈F ∪T                       i∈R

                 S0 +                                                                                             (3.7)
                         X
                               Si ki ≤ P̄ .
                         i∈P

Constraints (3.5) define the active playing rotation. The first inequality ensures that a player can
enter the rotation only if he is signed to the roster (yi ≤ ki ). The remaining bounds require a
rotation of eight to ten players, containing at least three guards (i ∈ G) and at least two bigs (i ∈ B).
Constraints (3.6) regulate roster turnover. The first inequality caps outside acquisitions from free
agency and trades at nin , while the second inequality restricts departures of contracted players to
at most nout . Re-signing the team’s own free agents does not count against these turnover limits,
because the club already owns their rights. The equality ki = 1 protects All-NBA players under
contract (i ∈ A). Because our shot model evaluates offense, an engine that traded away a franchise
player on purely offensive metrics would lack credibility with front offices. Constraint (3.7) keeps
total team spending within the owner’s budget P̄ , summing the salaries of the rest of the roster S0
and the salaries Si of all retained and acquired players.

Minutes. During the regular season, coaches share the possessions among combinations of rotation
players. In the second stage, the model assigns possession shares to candidate lineups separately for
each posterior draw d ∈ D:

          mℓd = 1,                       mℓd ≤ f yi (i ∈ P),             0 ≤ mℓd ≤ m̄ (ℓ ∈ L)          (d ∈ D).   (3.8)
    X                              X
                         f yi ≤
    ℓ∈L                            ℓ∋i


                                                              13
Constraints (3.8) govern playing-time allocation across lineups. The first equality ensures that
lineup shares sum to all team possessions in each scenario. The second pair of inequalities links
the two decision stages: any player omitted from the rotation receives zero possessions, while each
active rotation player receives between f = 10% and f = 75% of team playing time. Because
constraints (3.5) require yi ≤ ki , unrostered players receive no minutes, ensuring that a lineup plays
only when all five of its members are on the roster. The final upper bound prevents any single
lineup from exceeding m̄ = 35% of total possessions, which keeps playing-time patterns realistic.
Because minutes adapt across draws, the coach can reallocate playing time toward effective lineups
under whichever scenario occurs.

Salary-cap rules. A front office cannot simply assemble any roster that satisfies its total budget,
because the league’s collective bargaining agreement dictates which contract mechanisms a team
can legally use. These financial mechanisms change across collective bargaining agreements, and
we encode the rules of the 2011, 2017, and 2023 agreements (National Basketball Association and
National Basketball Players Association, 2011, 2017, 2023). We model these rules using five binary
indicators of the team’s operating mode and binary variables xi ∈ {0, 1} for players involved in
cap-room transactions.
   An offseason operates in two phases. A team that uses cap space (z room = 1) first fits its
contracted players, incumbent free-agent holds, and absorbed trade targets under the salary cap,
and then signs outside free agents using remaining room and the room exception. To create cap
space, the front office may send contracted players away (xi = 1):

    xi ≤ 1 − ki , xi ≤ z room (i ∈ R);                    xj ≤ kj , xj ≤ z room (j ∈ T ),                         (3.9)
    S0 +         Si (1 − xi ) +         Sj kj +         Sj xj ≤ Cap + M1 (1 − z             ),                   (3.10)
           X                      X               X
                                                                                     room

           i∈R                    j∈O             j∈T

    S0 +         Si (1 − xi ) +         Sj kj +           Sj kj +         Sj xj ≤ Cap + RE + M2 (1 − z room ).   (3.11)
           X                      X               X                 X

           i∈R                    j∈O             j∈F +             j∈T

Constraints (3.9) govern the moves of the cap-room phase. They allow such moves only when the
team uses cap room (z room = 1): a player under contract (i ∈ R) can be sent away to clear room
only if he leaves the roster, and a trade target (j ∈ T ) can be absorbed into room only if he is
acquired. Constraint (3.10) ensures that the players under contract who are not sent away to clear
room, the re-signed free agents, the absorbed trade targets, and the salaries of the rest of the roster
S0 fit within the salary cap (Cap). Constraint (3.11) ensures that outside free agents signed above
the minimum salary (j ∈ F + ) fit within the room exception (RE) and remaining cap room.
     A team operating over the salary cap (z room = 0) can sign outside free agents above the minimum
only through salary-cap exceptions. Using the full mid-level exception or the bi-annual exception,
or acquiring a player through a sign-and-trade transaction, hard-caps the team at the first apron
(z hard = 1). Under the 2023 agreement, spending any exception hard-caps payroll at the second




                                                                14
apron (z exc = 1; constraints (3.14) apply to that agreement only):

           Sj kj ≤ MLEtax + (MLE − MLEtax + BAE) z hard + M3 z room ,                                            (3.12)
    X

   j∈F +

  S0 +           Si ki ≤ Apron1 + M4 (1 − z hard ),         kj ≤ z hard (j arriving by sign-and-trade),          (3.13)
           X

           i∈P

           Sj kj ≤ (MLE + BAE) z exc + M5 z room ,                 S0 +         Si ki ≤ Apron2 + M6 (1 − z exc ). (3.14)
    X                                                                     X

   j∈F +                                                                  i∈P

Constraints (3.12) ensure that an over-the-cap team restricts outside free-agent signings to the
taxpayer mid-level exception (MLEtax ) unless it accepts a hard cap at the first apron (z hard = 1).
Constraints (3.13) enforce the first apron hard cap. The first inequality ensures that payroll does not
exceed the first apron threshold (Apron1 ) when hard-capped, while the second inequality ensures
that any player arriving via sign-and-trade triggers this hard cap. Constraints (3.14) enforce the
second apron rules of the 2023 agreement. The first inequality restricts exception spending unless
the team accepts a second apron restriction (z exc = 1), and the second inequality ensures that total
payroll remains below the second apron (Apron2 ).
    Trades outside cap room must balance outgoing and incoming player salaries. Let I =
   j∈T Sj (kj − xj ) denote incoming trade salary and O =          i∈R Si (1 − ki − xi ) denote outgo-
P                                                                P

ing salary matched in the trade phase. Teams ending above the salary line must match trades
tightly, whereas teams finishing below the line (z line = 1) choose between two flexible trade bands
using binary selector z band :

                   S0 +         Si ki ≤ Line + M7 (1 − z line ),      I ≤ a0 O + b0 + M8 z line ,                (3.15)
                          X

                          i∈P
                   I ≤ a1 O + b1 + M9 (1 − z line ),         I ≤ O + b2 + M10 (1 − z line + z band ),
                   I ≤ a3 O + b3 + M11 (2 − z line − z band ).                                                   (3.16)

Constraints (3.15) define operating status relative to the salary line. The first inequality ensures
that a team counted as under the line (z line = 1) does finish below it, while the second inequality
ensures that a team ending above the line obeys the narrow trade-matching rule I ≤ a0 O + b0 .
Constraints (3.16) govern trades for teams finishing below the line (z line = 1). The first inequality
enforces a common upper bound I ≤ a1 O + b1 , while the remaining inequalities permit the team to
choose between the trade bands I ≤ O + b2 and I ≤ a3 O + b3 using binary variable z band .
    The big-M parameters M1 through M11 enable these logical conditions within a linear framework.
We calculate each constant Mj as the maximum amount by which the left side of its constraint
can exceed the right side under the owner’s payroll limit P̄ . Choosing the smallest valid constants
switches off the rules that do not apply in a mode while keeping the linear relaxation tight. We match
trades in aggregate across the summer on the team’s side only, and allow minimum-salary signings
and incumbent free agents without matching restrictions. Appendix D provides the numerical values
for parameters a0 , a1 , a3 and b0 , b1 , b2 , b3 , as well as the aggregation rules governing multi-player
trades from 2024-25.

Protection against playoff defenses. A front office that optimizes purely for regular-season
scoring can build a roster vulnerable to postseason game plans. Against the best playoff defenses,
teams lose a sizeable share of their cuts to the rim and their spot-up shots in the paint, and take

                                                             15
many more pull-up threes instead (Appendix E). A roster that relies on a few kinds of shot is
exposed to this. To guard against this vulnerability, our formulation provides an optional defensive
stress test that allows an opposing defense to remove part of the team’s attempts in up to Γ of the
25 court cells. The removed attempts are re-routed to alternative shots at the lower value they
keep in the playoffs. Under scenario d, the loss in cell c depends linearly on playing-time shares,
Ldc = ℓ λℓdc mℓd .
       P

    The opposing defense chooses an optimal attack by targeting the Γ cells that cause the largest
reduction in offensive value. This adversarial attack forms a budgeted uncertainty set (Bertsimas
and Sim, 2004). Because a maximization nested inside the program would make it nonlinear, we
replace the defensive subproblem by its linear programming dual:
                                                            n                                          o
       SLd =      max′                Ldc =     min         Γπd +          qdc : qdc + πd ≥ Ldc (c ∈ C) .   (3.17)
                              X                                      X
                ′
               C ⊆C, |C |≤Γ                   πd , qdc ≥0
                              c∈C ′                                  c∈C

In this dual representation, the variable πd ≥ 0 sets a baseline threshold on defensive damage, while
qdc ≥ 0 captures cell losses that exceed this threshold. Inserting this minimization into objective
(3.4) with ω = 1 keeps the overall program linear and computationally tractable. By varying Γ from
one to four cells, a front office can trace, for its own roster, the trade-off between regular-season
value and protection against a playoff defense. Historical playoff series through season t provide the
empirical estimates for shot reductions and re-routed scoring values.

Properties. The formulation possesses two attractive structural properties. All objective terms
and operational constraints are linear, so the model is a mixed-integer linear program. The
formulation is also exact for the underlying value model. Teammates influence individual scoring
only through the five-player lineup on the floor, and precomputing all candidate lineup values Vℓd
avoids inner approximations. To isolate what drives decision quality, we define two benchmark
formulations. The mean-roles program condenses the twenty draws into a single scenario where
each player receives his expected role probabilities. The single-stage program fixes playing time
before role uncertainty resolves, requiring mℓd = mℓ across all draws.

3.4   Solution method and evaluation
Solving the two-stage program requires an efficient solution strategy to handle the large number of
continuous recourse variables. A typical pool of about 24 players generates some 19,000 candidate
lineups, so the twenty-draw program contains several hundred thousand continuous playing-time
variables alongside fewer than one hundred binary roster variables. We precompute all lineup values
using JAX (Bradbury et al., 2018) on CPU or GPU, which takes under a minute per team-offseason
across all models and draws. We construct each problem instance as a sparse matrix and solve it
with HiGHS (Huangfu and Hall, 2018) to a relative optimality gap of 10−4 , setting a time limit of
one hour per program.
    When initialized without a starting solution, the solver can search for an hour without discovering
an effective roster. We resolve this difficulty with a sequential three-step procedure. We first solve
the smaller mean-roles program to optimality. We then fix that roster and optimize rotation and
playing-time variables across all twenty draws, which supplies an advanced feasible solution for the
full program. We initialize the twenty-draw program from this solution, disabling solver presolve
because presolve alone requires about twenty minutes on instances of this scale.


                                                                16
    Table 3: Problem sizes and solver statistics over the 240 team-offseasons (engine with the full model).

                                                            Median      90th percentile   Maximum
          Players in the pool                                  24             26               27
          Candidate lineups                                  18,650         32,900          49,390
          Relative gap of the recourse program             2.5 × 10−5     9.1 × 10−5      1.0 × 10−4
          All programs of one team-offseason (minutes)         24             62              187


    This solution procedure allows the engine to achieve a relative optimality gap of 10−4 in every
backtest case, guaranteeing an objective value that is never inferior to the mean-roles plan under
flexible minutes. Table 3 reports problem sizes and computation times. Solving all programs for
one team-offseason takes about 25 minutes on a standard server, and the backtest ran across five
servers sharing a common task queue.
    We verified the mathematical formulation through two independent checks. On 13 instances
small enough to permit complete roster enumeration, under the 2011, 2017, and 2023 agreements
and six of them signing free agents into cap room, the program matched the brute-force optimum in
every case. Every roster recommended by the engine in the backtest also satisfies an independent
audit of league salary rules. The actual rosters assembled by teams pass that same audit in 74% of
team-offseasons.

How the plans are judged. Beyond evaluating each recommended plan, a front office needs to
know which model components drive the suggested decisions. For any roster k, we denote by zb(k)
its value under objective (3.4) and the full model, with playing-time recourse variables re-optimized
in every draw. By evaluating all plans under zb, we judge plans produced by simpler models by
what they would deliver if the full model is right. We structure our evaluation around four primary
comparisons that directly address the research questions of Section 2.2:
• the gain over the real roster, zb(k ⋆ ) − zb(k real ), where k ⋆ is the engine’s plan and k real the roster
    the team fielded, with minutes optimized over its own lineups;
• the value of the stochastic solution (Birge and Louveaux, 2011), VSS = zb(k ⋆ ) − zb(k mean ), the
    gain from planning for the uncertainty about roles rather than for each player’s average role,
    where k mean is the roster of the mean-roles program;
• the value of modeling synergy, zb(k ⋆ ) − zb(k add ) and zb(k ⋆ ) − zb(k shoot ), where k add and k shoot are
    the plans the engine makes when lineup values come from additive roles or from shooter-only
    rates;
• the value of the crowding term, measured in the same way against the plan made without it, and
    the trade-off between regular-season value and playoff protection traced by the stress test.
We evaluate the value of flexible minutes by comparing the recourse program with its single-stage
counterpart. Each comparison evaluates decision quality rather than statistical forecasting. A richer
model earns its place only if the plans it produces differ from, and score better than, the plans of a
simpler one.


4      Results
This section answers the first three research questions raised in Section 2.2; Section 5 addresses the
fourth. We evaluate every decision model and statistical forecast by fitting the models on data up

                                                      17
Table 4: How each part of the shot model improves the forecast of the next season’s shots: gain in log score
per game over shooter-only rates, averaged over the eight season pairs, and the number of pairs in which the
step itself improves the forecast.

                 Model                                             Gain    Pairs improved
                 + teammates’ roles, each cell on its own         +2.05         8 of 8
                 + similar cells grouped (additive roles)         +2.06         5 of 8
                 + effects that depend on the player’s own role   +2.13         5 of 8
                 + crowding beyond roles (the full model)         +2.35         8 of 8


to season t and evaluating them on season t + 1 across the eight consecutive season pairs. Nothing
from the later season enters any estimate, so every evaluation is out of sample.

4.1    Teammate fit can be predicted
This subsection answers Question Q1 by establishing that teammate fit can be predicted from
micro-level shot data. The estimated shot model captures the concrete tactical trade-offs coaches
see on the court (Figure 3). When a primary creator joins a lineup in place of an average teammate,
a player’s above-the-break pull-ups fall by almost a third, because the new creator takes those shots
himself. When a playmaker joins, the player’s cuts to the rim rise by a quarter, because someone is
now there to find him. A rim big shifts the player’s shot distribution away from the basket, reducing
cuts and post-ups while increasing drives and pull-ups. These adjustments reflect the choices front
offices weigh when pairing scorers with creators, playmakers, or traditional centers, and the model
puts a number on each shift.
     Court geography and teammate roles exhibit stable structure that simplifies front-office decisions.
Cells that respond to teammates in the same way form groups that recur season after season:
self-created shots (pull-ups and drives away from the rim), finishes near the basket (cuts and
post-ups), and, usually, corner spot-ups (Appendix C). Within each group, some teammate roles
have the same effect. Following the collapsed relative-shift patterns of Xu and Hu (2026), a posterior
over the 877 groupings of the seven teammate roles within each cell cluster shows which roles have
equal effects (Figure 4). In most seasons, for corner spot-ups, the spacing roles (spot-up connector,
two-way forward, shooter) cut a player’s corner threes and the other four raise them. For self-created
shots, the primary creator, the rim big, and the spot-up connector each stand apart. Roles that act
alike on a kind of shot are interchangeable in their effect on it, which narrows the comparisons a
front office has to make.
     Out-of-sample evaluations confirm that these teammate effects predict shooting patterns in the
subsequent season. Table 4 measures forecasts of the next season’s attempts by their log score
(Gneiting and Raftery, 2007), against shooter-only rates. Knowing a player’s teammates improves
the forecast of his shots substantially, in every season, and teammates’ roles bring by far the largest
gain. Grouping similar cells preserves predictive accuracy while making the effects readable. Letting
effects depend on the player’s own role adds a modest improvement, and adding the crowding term
provides a clear further gain across all eight season pairs.
     The predicted teammate effects carry over when players change teams. Because the engine
values candidates on new rosters, the effects must hold when a player moves. For the 775 players
who played substantial minutes for one team and then for another, we compare the change in their
shot mix with the change the model attributes to their new teammates (Figure 5a,b). The predicted

                                                    18
                            Drive                    Cut                    Pull-up                Post / paint                Spot-up


               + creator




            + playmaker




               + shooter




             + connector




           + two-way fwd




               + hub big




                + rim big




                                                    −36       −24      −12         0       +12        +24       +36
                               Change in the player's attempt rate when one of four average teammates is replaced by the row's role (%)
                                                      hatched: 90% interval covers 0, widened for role uncertainty


Figure 3: How one teammate’s role changes a player’s shots (2022-23). Each row replaces one of a player’s
four average teammates by a teammate of that role; each panel is a movement type drawn over the five court
zones, and the color is the change in the player’s attempt rate. Hatched cells: the 90% interval includes zero
once the uncertainty about roles is taken into account.




                                                                      19
                                                                                                     (b) Probability of collapse, 8 pairs
                    (a) Self-created: most probable grouping (probability 0.40)                      outlined: (a)'s groups
          Rim big                                                                          Rim big
       Connector                                                                        Connector    .1
     Two-way fwd                                                                      Two-way fwd    .0 .0
       Playmaker                                                                        Playmaker    .0 .1 .6
          Shooter                                                                          Shooter   .1 .0 .5 .6
          Hub big                                                                          Hub big   .0 .0 .6 .5 .5
          Creator                                                                          Creator   .0 .0 .0 .0 .0 .1

                       −30    −20    −10      0      10     20     30        40

                    Interior finishes: most probable grouping (probability 0.39)                     Probability of collapse, 8 pairs
       Playmaker                                                                        Playmaker
          Creator                                                                          Creator   .4
          Shooter                                                                          Shooter   .4 .8
       Connector                                                                        Connector    .4 .6 .6
     Two-way fwd                                                                      Two-way fwd    .0 .4 .5 .5
          Hub big                                                                          Hub big   .0 .1 .0 .0 .1
          Rim big                                                                          Rim big   .0 .0 .1 .0 .2 .7

                       −30    −20    −10      0      10     20     30        40

                    Rim drives, spot-ups: most probable grouping (probability 0.33)                  Probability of collapse, 4 pairs
       Playmaker                                                                        Playmaker
       Connector                                                                        Connector    .6
          Rim big                                                                          Rim big   .8 .7
     Two-way fwd                                                                      Two-way fwd    .4 .2 .4
          Hub big                                                                          Hub big   .1 .0 .0 .5
          Shooter                                                                          Shooter   .3 .5 .2 .3 .2
          Creator                                                                          Creator   .0 .0 .0 .0 .0 .2

                       −30    −20    −10      0      10     20     30        40

                    Corner spot-ups: most probable grouping (probability 0.57)                       Probability of collapse, 7 pairs
          Creator                                                                          Creator
          Rim big                                                                          Rim big   .8
          Hub big                                                                          Hub big   .8 .9
       Playmaker                                                                        Playmaker    .7 .7 .7
       Connector                                                                        Connector    .0 .0 .0 .2
          Shooter                                                                          Shooter   .1 .1 .1 .1 .6
     Two-way fwd                                                                      Two-way fwd    .1 .1 .0 .1 .8 .7

                       −30    −20    −10      0      10     20     30        40
     Change in the shooter's attempts of these shots when a teammate of this role
                  replaces an average teammate (%, 90% interval)

Figure 4: Which teammate roles act alike, by kind of shot. (a) The role effects on the shots of each cell
cluster in the latest season pair (replacing an average teammate, with 90% intervals), with the roles ordered
and shaded by the most probable grouping. (b) The probability that two roles have equal effects, averaged
over the season pairs that have the cluster, with the groups of (a) outlined.


effects carry over at about three quarters of their size, with weaker transfer near the basket than
for threes. We therefore apply this transfer factor κ = 0.75 as a damping parameter whenever the
engine evaluates newcomers.
    Lineup values derived from shot patterns directly track realized team scoring on the court. For
each team, we value the lineups it played in two consecutive seasons, using only data up to the first
season. When the value of a team’s lineups rises, its offensive rating rises too (Figure 5c), and in
levels the value of the lineups a team uses closely tracks how well it scores (panel d). The lineup
values also carry predictive signal that past records omit: they forecast next season’s offense better
than last season’s offensive rating does, both in levels and in changes. Adding them to last season’s
rating raises the share of explained variation from 43% to 67%. A point of predicted change goes


                                                                        20
                                             (a) 775 movers, 8 season pairs                                                        (b) By zone, 95% intervals
                                                    Without crowding, κ = 0.72
                                         2          Additive roles, κ = 0.80                                   Above-break 3
           Realized change, net (pp)




                                         1                                                                           Corner 3


                                         0                                                                          Mid-range


                                       −1                                                                                 Paint


                                       −2                                                                     Restricted area


                                               −3        −2         −1        0   1      2         3                               0.0      0.2     0.4        0.6      0.8           1.0         1.2
                                               Predicted change from new teammates (pp)                                                                 κ (1 = full transfer)

                                             (c) Predicted and realized change, without crowding                                   (d) Four models of the same lineups
                                              r = 0.56 (0.44 to 0.65)
                                              slope 0.48, 240 team-offseasons                               Change vs change
                                                                                                             in offensive rating
Change in offensive rating




                                        10


                                         5                                                                  Change vs change
                                                                                                              in effective FG%
                                                    ATL 2017-18
                                         0
                                                                                                            Value vs offensive
                                                                                      Season t+1            rating, season t+1
                                       −5
                                                                                      16-17       20-21                                                                          Full model
                                                                                      17-18       21-22                                                                          Without crowding
                                       −10                                            18-19       22-23          Stress loss vs                                                  Additive roles
                                              GSW 2019-20                                                       playoff drop-off
                                                                                      19-20       23-24                                                                          Shooter-only

                                                −15           −10        −5       0           5        10                      −0.4      −0.2     0.0       0.2      0.4        0.6         0.8         1.0
                                                            Predicted change in value                                                             Pearson r (95% interval)
                                                          (points per 100 possessions)

Figure 5: The effects hold on the next season. (a) Players who change teams: the realized change in a
mover’s shot mix against the change the model predicts from his new teammates, in bins; the dashed line is
full transfer. (b) The transfer factor κ by zone, with 95% intervals. (c) Lineup values and team offense, 240
team-seasons: the predicted change in the value of the lineups a team played against the realized change in its
offensive rating, under the model without the crowding term; the solid line is the fitted line. (d) Correlations
with 95% intervals for four versions of the model.


with about half a point of realized change, so the values are best read as a ranking of rosters whose
differences are somewhat exaggerated; we use this calibration when we translate the engine’s gains
into offensive rating. The answer to Question Q1 is therefore yes: teammates’ roles shift where and
how often players shoot, these shifts carry over to players who change teams, and the resulting
lineup values track how well teams score.

4.2                                          Better rosters than the ones teams built
This subsection answers the first part of Question Q2: we test whether planning for teammate
fit builds better rosters than the ones front offices actually assembled across 240 historical team-
offseasons. We put the engine in the position of every front office in every summer from 2016 to 2023,
thirty teams over eight summers. Each problem instance uses only what the team could have known


                                                                                                             21
Table 5: The backtest by summer (30 teams each; points per 100 possessions). Gain: the engine’s plan over
the real roster. The last four columns give what a front office would lose by planning without each part of
the model.

            Engine against the real roster                Value of planning with the full model
 Summer     Gain        Engine better        Role uncertainty    vs additive   vs shooter-only    Crowding
 2016        8.04           100%                   0.18              0.41           1.70            0.01
 2017       10.54           100%                   0.16              0.77           1.99            0.03
 2018        5.77           100%                   0.19              0.35           1.26            0.04
 2019        4.07            97%                   0.14              0.66           1.01            0.03
 2020        4.04           100%                   0.27              0.53           1.84            0.02
 2021        4.65           100%                   0.45              0.48           0.96            0.09
 2022        4.46           100%                   0.10              0.75           1.15            0.04
 2023        3.67            97%                   0.17              0.43           1.11            0.05
 All 240     5.65            99%                   0.21              0.55           1.38            0.04


at the time: the models estimated on data up to season t, the team’s pool and market, the salary
rules of the coming league year, and the twenty posterior role draws. To keep the cases comparable,
every team may bring in two market players (nin = 2, more if it needs them to field a rotation)
and let three players under contract go (nout = 3). The engine then plans the offseason, and we
compare its plan with the roster the team actually assembled through its real trades, signings, and
departures. For the comparisons of Section 3.4, the engine also plans each case with the simpler
models, and every plan, including the real roster, is scored in the same way.
    The engine identifies rosters with substantially higher predicted offensive value than those
assembled by front offices in practice. In almost every case, 99% across the backtest, the engine
finds a roster that the model values more highly than the one assembled by the team, gaining about
five and a half points per 100 possessions on average (Table 5). The gap is widest in the summers
of 2016 and 2017 and settles around four points from 2019 on. Because a point of predicted gain
goes with about half a point of realized gain (Section 4.1), the average gap corresponds to about 2.8
points of offensive rating in real play. That improvement is large enough to lift a league-average
offense to about the sixth best in the league.
    The engine’s plans translate the optimization results into salary-compliant rosters through
feasible player transactions. They bring in two market players and send out two or three players on
average, and every plan satisfies the salary rules. Many of them create cap space by sending away
players under contract, which the market of a real summer would have to absorb. The engine is not
simply buying stars: since the market contains the players each team really acquired, the engine
could often have repeated the team’s moves, and it almost always found a better combination. In
answer to the historical part of Question Q2, planning for teammate fit within salary constraints
builds substantially better rosters than real NBA front offices constructed.

4.3     What drives the decision
This subsection answers Question Q3 by determining which components of the optimization model
drive roster choices and quantifying what a front office loses by omitting them. Figure 6(a) establishes
this by showing what a front office loses when it plans with less of the model. The clearest answer


                                                    22
concerns teammate synergy. A front office that valued each player by his own shooting, as if his
teammates did not matter, would choose the engine’s roster in only 7% of the cases, and its rosters
would score well over a point per 100 possessions less. The reason is the competition for shots of
Section 3.2. Judged one at a time, two scorers who take the same shots look as good together as
apart; once their competition is counted, they are worth less together than a scorer paired with a
playmaker or a shooter. A front office that thinks in roles but treats their effects as simply additive
gets part of the way, keeping the engine’s roster in about one case in five and losing about half a
point. Fit, in short, is not a refinement of player value: it changes which players a team should
pursue.
    Teammate effects also govern which trades make economic sense for both franchises. Holding
each team’s real roster for the next season, we screened every one-for-one and two-for-two trade of
rotation players within the salary rules of both teams and solved the most promising of them exactly,
up to 200 a season. Under the full model, between 0 and 28 trades a season raise both teams’ value
in all 20 role draws (94 over the eight seasons), against 53 to 193 under shooter-only rates. Without
teammate effects, a trade can help both sides only through the cap on a lineup’s attempts, while
the full model charges an incoming creator for the shots he takes from his new teammates.
    The remaining model components exert much smaller effects on roster selection. With the
crowding term, the engine picks a different roster in about half of the cases, but the rosters it would
otherwise have picked are almost as good: the term helps the engine choose among rosters that
are already close in value. Protection against a strong playoff defense is cheap. A roster built to
withstand an opponent who cuts into two of its favorite kinds of shot gives up only a few hundredths
of a point per 100 possessions in the regular season (Figure 6b), and larger attacks add almost
nothing.
    Uncertainty about player roles does not require elaborate hedging because in-season playing-time
adjustments absorb most risk. Front offices do not know in advance whether a newcomer will
create his own shots or spot up. In most cases, however, planning for every role draw yields little
gain over planning for each player’s average role and letting rotation minutes adapt. The value of
the stochastic solution averages 0.21 points (Table 5), and in more than a third of the cases both
formulations pick exactly the same roster. The second stage performs this heavy lifting: whatever
roles the season reveals, the coach moves minutes toward lineups that click, so a roster built for
average roles rarely leaves value behind.
    Stochastic planning pays off when an offseason roster carries high role volatility. Figure 6(c)
shows that the gain from stochastic modeling grows with the risk of the average-role plan, measured
by how far its value drops in its worst draws. For the safest quarter of rosters, the value of the
stochastic solution is close to zero; for the riskiest quarter, it averages about half a point per 100
possessions, and for a few teams it is well over a point. Most of this gain comes from the bad draws
(panel d): planning for uncertainty changes little in average outcomes, but protects the franchise
against seasons where new roles combine poorly. The cases where it matters most cluster in the
summer of 2021, perhaps because the shortened 2020-21 season left many players’ roles less settled
than usual.
    Front offices typically have multiple near-optimal rosters available at similar salaries. Table 6
repeats the backtest with the engine without the crowding term under three changes to its inputs.
When newcomers’ effects are damped more or less (κ = 0.5 or κ = 1), the plan changes in about
half of the cases while the value it reaches barely moves. When the free agents who re-signed with
their own teams are removed from the market, most plans change but the engine’s lead over the


                                                  23
                                                     (a) 240 team-offseasons (means above the boxes)                                                                                (b) Stress frontier
                                              17.5                                                                                                                           0.25




                                                                                                                                      Stress loss avoided at that budget
                                              15.0
Points per 100 possessions




                                                                                                                                                                             0.20
                                              12.5
                                                          +5.65
                                              10.0
                                                                                                                                                                             0.15
                                               7.5

                                               5.0                                                                                                                           0.10
                                                                                                                    +1.38
                                               2.5                                                    +0.55                                                                                                                                               Γ=1
                                                                       +0.21                                                                                                 0.05                                                                         Γ=2
                                                                                      +0.04
                                               0.0                                                                                                                                                                                                        Γ=3
                                                                                                                                                                                                                                                          Γ=4
                                          −2.5                                                                                                                               0.00
                                                      Engine's plan Value of the Crowding vs Synergy vs Synergy vs                                                                  0.00      0.05        0.10         0.15           0.20         0.25
                                                       minus the     stochastic plans made    additive  shooter-only
                                                       real roster    solution    without it   roles       rates                                                                                 Regular-season value given up

                                                     (c) 240 team-offseasons, r = 0.55                                                                                              (d) Where the gain comes from (104 cases above 0.1)
                                                          same roster as the average-role plan (88)
                                                                                                                                      Gain in the worst fifth of the draws



                                                                                                                                                                              2.5
           Value of the stochastic solution




                                                          different roster (152)
                                               2.0
                                                          mean by quarter of role risk
                                                                                          ATL 2021                UTA 2018                                                    2.0
                                                                                                              LAL 2023
                                               1.5                                      BOS 2021
                                                                                                                                                                              1.5
                                                                                              NYK 2021
                                                                                                                                                                              1.0
                                               1.0
                                                                                                                                                                              0.5

                                               0.5
                                                                                                                                                                              0.0
                                                                                                                                                                                                                           83% gain more in the worst fifth
                                                                                                                                                                             −0.5                                median share of the gain from the tail: 78%
                                               0.0
                                                      0           1             2             3               4              5                                                        −0.5     0.0        0.5        1.0        1.5          2.0      2.5
                                                               Role risk of the average-role plan                                                                                             Gain in the mean over the role draws
                                                            (mean minus worst fifth of the role draws)

Figure 6: What drives the decision, over 240 team-offseasons (points per 100 possessions). (a) The engine’s
plan against the real roster, and what is lost by planning with a simpler model: with each player’s average
role, without the crowding term, with additive roles, and with shooter-only rates. Every plan is scored by the
full model; means are printed above the boxes. (b) Protection against a playoff defense: plans made for an
attack on Γ cells give up regular-season value (horizontal) to avoid losses against that attack (vertical); thin
lines are teams, dots are means. (c) The value of the stochastic solution against the risk of the average-role
plan (its mean value minus the mean of its worst fifth of draws); light points are cases where both plans pick
the same roster, and the orange line follows the mean by quarter of risk. (d) For the cases with a gain above
0.1, the gain in the average over the draws against the gain in the worst fifth of the draws.




                                                                                                                                 24
Table 6: Robustness of the plans, 240 team-offseasons (239 without re-signers: one case has no feasible
roster), engine without the crowding term. Points per 100 possessions; mean (median). Change: the attainable
value minus the main run’s.

        Variant                          Change       Same plan    Engine minus real        VSS
        Main run (κ = 0.75)               —                —           5.66 (4.86)      0.29 (0.07)
        κ = 0.5                      +0.12 (+0.04)        50%          5.78 (4.89)      0.25 (0.07)
        κ=1                          +0.03 (+0.06)        58%          5.60 (4.98)      0.32 (0.11)
        No other teams’ re-signers   −0.32 (−0.00)        31%          5.36 (4.76)      0.36 (0.11)


real rosters stays almost the same. This version of the engine reaches the same conclusions as the
full one: its lead over the real roster is 5.66 points (median 4.86), the value of its stochastic solution
0.29, its values of modeling synergy 0.52 against additive plans and 1.69 against shooter-only plans,
and its stress frontier gives up 0.04 to save 0.05 at Γ = 2. Within salary constraints, a team’s
market usually offers several players who satisfy the same positional need at comparable cost. The
engine’s most useful output is therefore a short list of strong rosters, among which managers can
choose using attributes outside the model, such as defense, health, and character. In answer to
Question Q3, teammate fit is the primary driver of roster decisions: flexible minutes absorb most of
the uncertainty about roles, protection against playoff defenses costs little, and the engine offers
front offices a short list of near-optimal rosters rather than a single answer.

4.4    Two held-out seasons
This subsection answers the second part of Question Q2 by evaluating whether the gains from
planning for fit hold out of sample in two seasons kept aside during model development. All results
discussed so far derive from seasons studied while refining the methodology. To ensure that our
findings are not an artifact of model tuning, we held two complete seasons untouched. Nothing from
2024-25 was inspected, and data from 2025-26 were not even downloaded, until the code was frozen
at a single commit and ten claims were written down, each with the range it took over the eight
earlier seasons. Each untouched season was then processed and scored with the models estimated on
the season before it. Three data problems that surfaced during these runs were fixed by correcting
how the data are read, without changing any model, setting or claim, and every affected case was
solved again (Appendix F).
    The central claims held in both held-out seasons (Table 7). Teammates’ roles improved shot
forecasts by amounts comparable to the strongest historical results; the estimated shifts carried over
to players changing teams; lineup values tracked realized team offense; the engine constructed a
better roster than the real one for every team; and plans made without teammate effects sacrificed
value. The crowding term again improved forecast accuracy, while the interaction with a player’s
own role added no predictive power and degraded forecast accuracy in 2024-25. The answer to
Question Q2 therefore holds on seasons the method had never seen: planning for teammate fit
builds better rosters than the ones teams assembled.




                                                     25
Table 7: The claims on the two held-out seasons, beside their range over the eight earlier seasons. Claims
1–3: gain in log score per game; claim 4: the transfer factor κ; claims 5 and 6: correlations over 30 teams;
claims 7–10: points per 100 possessions.

      Claim                                                           Earlier seasons   2024-25   2025-26
 1    Teammates’ roles improve forecasts of players’ shots            +1.43 to +2.60     +2.51     +2.68
 2    The dependence on a player’s own role adds little               −0.09 to +0.26     −0.65     −0.02
 3    Players shoot less where their teammates shoot                  +0.13 to +0.35     +0.05     +0.07
 4    Teammate effects carry over to players who move                  0.44 to 1.21       0.50      0.93
 5    Lineup values track changes in team offense                      0.36 to 0.73       0.67     0.55
 6    Lineup values rank team offenses                                 0.54 to 0.84       0.79      0.69
 7    The engine improves on the real roster                           3.67 to 10.54      4.50     3.83
 8    Planning for role uncertainty adds a little                      0.10 to 0.45       0.07      0.14
 9    Teammate effects change the plan: vs additive roles              0.35 to 0.77       0.58      0.82
        vs shooter-only rates                                          0.96 to 1.99       0.91      1.49
 10   Crowding changes plans more than values                          0.01 to 0.09       0.10      0.07


5     Case studies: three famous summers
This section answers Question Q4: we examine how the engine evaluates high-profile front-office
decisions that shaped the league, following Cleveland in 2017, the Los Angeles Clippers in 2019,
Brooklyn in 2020, and Boston and Phoenix in 2023. While the broad backtest demonstrates
systematic gains across 240 team-offseasons, these case studies illuminate the concrete basketball
reasoning of the stochastic program. To inspect each decision in realistic operational detail, we let
each team make at most as many moves as the franchise made that summer, rather than applying
the uniform limits of the backtest. We also price individual transactions by re-solving the stochastic
program with specific players forced onto the roster or ruled out, using identical lineup values and
posterior draws (Figure 7 and Table 8); unchanged re-solves reproduce the original objective values.
These are the numbers a front office would want before it commits: what a star is worth to this
particular roster, what the best alternative would have been, and what a concession in a trade costs.

5.1    Cleveland, 2017: the price of a trade request
The 2017 Cleveland Cavaliers illustrate how the engine quantifies the hidden cost of an unexpected
trade request. In July 2017, Kyrie Irving asked to be traded, and Cleveland sent him to Boston for
Isaiah Thomas, Jae Crowder, and draft picks; it also signed Derrick Rose and, later in the offseason,
Dwyane Wade. Free to keep Irving, the engine does so. It acquires Thomas and Crowder by trading
away JR Smith’s salary, signs Rose, and builds a roster worth about 1.3 points per 100 possessions
more than Cleveland’s. Boston, however, gave up Thomas and Crowder only to receive Irving, which
the engine’s market cannot know. Once Irving has to leave, as he did, the engine’s best plan brings
in the four players at the heart of Cleveland’s summer: Thomas, Crowder, Rose, and Wade. In
that constrained re-solve, the engine’s plan matches the value of Cleveland’s realized roster. Given
the trade request, the model agrees with the front office’s choices, and quantifies the offensive cost
of accommodating the request at approximately 1.3 points per 100 possessions (Figure 7). Of the
players Cleveland received, Thomas was the one that mattered: without him the plan loses almost
four points, while Crowder is worth about half a point.


                                                    26
                                                    Cleveland, 2017
             Trade Kyrie Irving, as Cleveland did                                                             -1.31

                              No Isaiah Thomas                                   -3.84

                                No Jae Crowder                                                                                -0.48
                                                    LA Clippers, 2019
          Paul George instead of Kawhi Leonard                                                                        -0.89

        Leonard and George, without Bogdanović                                                       -2.00

                       Keep Gilgeous-Alexander                                                                                        -0.08
                                                    Brooklyn, 2020
            No Harden (Brandon Ingram instead)          -5.75

         Send Jarrett Allen away, as the Nets did                                                                     -0.93

                        Keep Spencer Dinwiddie                                                                                  -0.32


                                                         −6           −5           −4        −3          −2              −1                   0
                                                              Change in the engine's objective (points per 100 possessions)

Figure 7: What the key moves of three summers are worth for each team. Each bar is the change in the
engine’s objective when the program is solved again with one move imposed or ruled out (points per 100
possessions).



Table 8: Single-move re-solves of the three case studies (engine with the full model). Change: the objective
minus the case’s, points per 100 possessions. Re-signings of the team’s own free agents are omitted.

 Case                       Move                                  Change        Acquired                       Sent away
 Cleveland, 2017            engine’s plan (122.23)                  —           Thomas, Crowder, Rose          Smith
                            Irving sent away                       −1.31        Thomas, Crowder, Rose,         Irving
                                                                                Wade
                            Thomas ruled out                       −3.84        George, Crowder, Rose,         Love
                                                                                Wade
                            Crowder ruled out                      −0.48        Thomas, George                 Love
 LA Clippers, 2019          engine’s plan (126.70)                    —         Leonard,    Bogdanović,        Gilgeous-Alexander,
                                                                                Noah                           Robinson
                            George forced in                       −0.89        George,     Bogdanović,        Gilgeous-Alexander,
                                                                                Noah                           Robinson
                            Leonard ruled out                      −0.89        George,     Bogdanović,        Gilgeous-Alexander,
                                                                                Noah, Patterson                Robinson
                            Bogdanović ruled out                   −2.00        Leonard, George, Noah          L. Williams, Robinson
                            Gilgeous-Alexander kept                −0.08        Leonard,    Bogdanović,        Robinson
                                                                                Grant, Noah
 Brooklyn, 2020             engine’s plan (126.74)                    —         Harden, Green, Shamet          Dinwiddie, LeVert, Prince,
                                                                                                               Kurucs
                            Harden ruled out                       −5.75        Ingram, Green, Vonleh          Dinwiddie, LeVert, Prince,
                                                                                                               Jordan
                            Allen sent away                        −0.93        Harden, Green, Vonleh          Allen, LeVert, Prince, Ku-
                                                                                                               rucs
                            Dinwiddie kept                         −0.32        Harden, Green, Shamet,         LeVert, Prince, Jordan
                                                                                Vonleh




                                                                           27
                                                          (a) First stage: the roster under the 2019-20 salary rules
                                                    150
                                                                                                                                                                                                                                         First apron $138.9M
                                                                                                                                                                                                                                         Tax $132.6M
                                                    125                                                                                  Kawhi Leonard
                                                                                                                                        Bojan Bogdanović                                       Joakim Noah                               Cap + room exception $113.9M
                                                                                                                                                                                                                                         Cap $109.1M




                                     Payroll ($M)
                                                    100

                                                    75                                                      Garrett Temple
                                                                                    Jerome Robinson         Patrick Beverley
                                                                                 Shai Gilgeous-Alexander
                                                    50

                                                    25

                                                     0
                                                               Under contract         Sent away to         Own free agents                                      Free agents                        Minimum                 Payroll
                                                              after the season         clear room            re-signed                                           into room                         contracts




                                                                                                                               Lineup value (points per 100 possessions)
                                                          (b) Second stage: minutes, draw by draw                                                                                  (c) Value in each draw
                                                               Plan under role uncertainty                                                                                           worst fifth
                               Danilo Gallinari
                                                               Plan with mean roles                                                                                        128.0
                               Kawhi Leonard
                            Bojan Bogdanović
                                 Lou Williams
                                                                                                                                                                           127.5
                              Montrezl Harrell
                                                                                                                                                                           127.0
                                 Joakim Noah
                               Landry Shamet
                                                                                                                                                                           126.5
                              Patrick Beverley
                               Garrett Temple                                                                                                                              126.0
           Jerami Grant (mean-roles plan only)
                                                                                                                                                                                                          Objective: 126.70 against 126.50
Shai Gilgeous-Alexander (mean-roles plan only)                                                                                                                             125.5                       value of the stochastic solution 0.20

                                                          0             10             20             30                                                                    Role draws, ordered by the plan under uncertainty
                                                               Minutes per game in each role draw


Figure 8: The two-stage program on the Clippers’ summer of 2019. (a) First stage: the payroll through the
cap-room phase under the 2019-20 rules. (b) Second stage: each player’s minutes in each of the 20 role draws,
for the plan made under role uncertainty (filled) and the plan made with each player’s average role (open).
(c) Each plan’s value in each draw; the dashed lines are the two objectives.


5.2         The Clippers, 2019: a shooter beside Leonard
The 2019 Los Angeles Clippers reveal how pairing two high-usage creators can congest offensive shot
distribution. In July 2019, the Clippers signed Kawhi Leonard and traded Shai Gilgeous-Alexander,
Danilo Gallinari, and five first-round draft picks to Oklahoma City for Paul George. Given identical
market alternatives and salary-cap rules, the engine also signs Leonard, but it declines to trade for
George (Figure 8a). It clears cap space by sending away Gilgeous-Alexander and Jerome Robinson,
re-signs Patrick Beverley and Garrett Temple, signs Leonard and the shooter Bojan Bogdanović
into that space, adds Joakim Noah at the minimum salary, and retains Gallinari and Lou Williams.
The model values this roster about three and a half points per 100 possessions above the roster the
Clippers fielded.
    The engine rejects the George trade because adding another primary creator yields diminishing
returns on a roster already rich in shot creation. Leonard and George are both primary creators, and
the Clippers already had two more in Gallinari and Lou Williams. Because basketball possessions
are finite, creators take shots from one another, so a second star creator adds much less to this roster
than his own numbers suggest, while a shooter adds what the roster lacks. Marginal transaction
values highlight this trade-off (Figure 7). When Bogdanović is ruled out, the engine does pair
Leonard with George, sending Lou Williams away to afford him, and the plan loses two points;
George in place of Leonard loses almost one.
    The second stage matters as much as the first. Figure 8(b) tracks each player’s minutes across
the twenty posterior role draws: Landry Shamet and Patrick Beverley play anywhere from five


                                                                                                               28
to more than thirty minutes a game, depending on how the roles turn out. A rotation fixed in
advance for all draws, the single-stage program of Section 3.3, would lose 2.2 points, the largest
value of flexible minutes in the three summers. The plan made for each player’s average role keeps
Gilgeous-Alexander for a few minutes and adds Jerami Grant in place of Beverley and Temple; it is
worth a fifth of a point less and falls short in 15 of the 20 draws (panel c).
    One move in the engine’s plan is almost free to undo. Keeping Gilgeous-Alexander costs less
than a tenth of a point, because the engine sends him away only to make cap space. A front office
that valued his future, which a model of the coming season does not price, could have kept the
player who went on to become the league’s most valuable player at almost no cost to its offense.

5.3   Brooklyn, 2020: why Harden
The 2020 Brooklyn Nets demonstrate how micro-level shot charts distinguish stars who share
identical categorical roles. Kevin Durant joined Brooklyn in 2019 but missed the 2019-20 season
recovering from a torn Achilles tendon, so the engine values him on his 2018-19 season. In January
2021, the Nets traded Caris LeVert, Jarrett Allen, Taurean Prince, Rodions Kurucs, and draft picks
for James Harden. Offered Harden as a trade target in the summer, the engine makes the trade as
well, with one difference: it sends Spencer Dinwiddie instead of Allen and keeps Allen as its center.
It also adds Jeff Green and Landry Shamet, and its rotation gives Kyrie Irving 24 minutes a game
beside Harden and Durant.
    Spatial shot distribution explains why Harden complements Durant far better than other elite
scoring creators. Durant, Harden, Irving, and Brandon Ingram, the best alternative in Brooklyn’s
market, are all primary creators in the model, so categorical roles alone cannot separate them. Their
shot charts resolve the question (Figure 9a). Ingram’s and Irving’s charts resemble Durant’s, with
many shots from mid-range; Harden’s does not, because he scores at the rim and from beyond the
arc. Measured by the share of shots that two charts have in common, Harden overlaps Durant by
0.48, against 0.74 for Irving and 0.79 for Ingram. Players shoot less where their teammates shoot,
so Harden keeps more of his value beside Durant than the others would, and he had led the league
in scoring as well. Without him, the engine turns to Ingram and its plan loses almost six points, by
far the largest value of any single move in the three summers. Sending Allen away, as the Nets did,
costs almost a point and leaves a roster worth about the same as the one Brooklyn fielded. In the
engine’s reading, the Nets chose the right star (James Harden) but paid for him with the wrong
player (Jarrett Allen).

5.4   What the model does not see: Boston, 2023
The summer of 2023 shows both what a model of offense built from roles sees and what it does
not. Milwaukee traded Jrue Holiday for Damian Lillard, a move the engine’s plan for the Bucks
makes as well, and the Bucks’ offensive rating rose by 3.0 points, close to the calibrated forecast
of 3.4 points for the lineups they used. Boston traded Marcus Smart for Kristaps Porzin, gis‘
                                                                                                and
sent Malcolm Brogdon and Robert Williams III to Portland for Holiday; the following season it had
the league’s best offense and won the title. Its offensive rating rose by more than five points, yet
the model saw almost no gain in the lineups Boston used. Part of the difference lies outside the
model by design, since Holiday was prized above all for his defense. The rest is instructive. The
two newcomers took fewer pull-ups beside their new teammates, as predicted, but Jayson Tatum,
who stayed, took many more of his shots off the dribble, where the model expected him to defer to


                                                 29
                                          (a) Kevin Durant                           Brandon Ingram                            Kyrie Irving                            James Harden
                                          2018-19                                    2019-20 · overlap 0.79                    2019-20 · overlap 0.74                  2019-20 · overlap 0.48




                                           18%          41%             33%             25%         27%           39%             32%           45%            20%          38%             40%        17%
                                                                  1,378 attempts                              1,091 attempts                            410 attempts                           1,504 attempts


                                             Drive       Cut       Pull-up       Post / paint      Spot-up
                                                                                                                                                              0.1                    1                        10
                                                                                                                                                        Share of the player's attempts per 1.5 ft hex (%)

                                          (b) Full model                                                                       (c) Shooter-only rates

                                           changed teams: r = +0.59                                                              changed teams: r = -0.03
                                           stayed: r = -0.46       Tatum pull-ups                                                stayed: r = -0.23
Realized change in share (points)




                                                                             Gafford cuts
                                    +10
                                                                                            Beal spot-ups




                                      0



                                                                                                                                                                                         PHX 2023
                                                  Porziņģis
                                                   pull-ups                                                                                                                              BOS 2023
                                                                                                                                                                                         DAL, 2024 deadline
                                    −10                                                                                                                                                  Changed teams
                                                                                                                                                                                         Stayed

                                                 −10                         0                          +10                         −10                         0                        +10
                                                              Predicted change in share (points)                                              Predicted change in share (points)

Figure 9: The shot patterns behind the case studies. (a) Kevin Durant’s shots in 2018-19 beside those
of three creators Brooklyn could pair with him, in 2019-20. Color: the share of the player’s attempts in
each hexagon; bars: his mix of movement types. Overlap: the share of shots that the two players’ 25-cell
mixes have in common (1 for identical mixes). (b, c) Predicted against realized changes in the shot mixes
of eleven key players of three moves (Phoenix and Boston in 2023, Dallas at the 2024 trade deadline), by
movement type and zone, under the full model (b) and shooter-only rates (c), all scored with the model fitted
on 2022-23.


the newcomers. Phoenix, which traded Chris Paul, Landry Shamet, and draft picks that summer
for Bradley Beal to play beside Devin Booker and Kevin Durant, tells the same story. Beal and
Durant, who had played most of the previous season elsewhere, gave up as many pull-ups as the
model predicted and took more spot-ups, while Booker took more pull-ups than before. Across
the eleven key players of three such moves, Phoenix and Boston in 2023 and Dallas at the 2024
trade deadline, the predicted shifts track the realized ones for the six players who changed teams
(r = 0.59) and run against them for the five who stayed (r = −0.46; Figure 9b), while shooter-only
rates predict almost no shift at all (panel c). The asymmetry points to offensive hierarchy as an
additional determinant of how players adjust to a new roster, with newcomers adapting to their
teammates while established stars retain offensive priority. Roles describe how players play, but not
whose role adjusts when the roster changes, pointing to a natural extension of the model.


                                                                                                                      30
6    Conclusions
Roster construction in professional basketball is a decision about combinations. We have shown
that the way teammates shape each other’s shots can be estimated from public micro-level shot
data, turned into the value of any lineup, and built into a risk-averse two-stage stochastic program
that respects the league’s salary rules. Tested against every team’s offseason over eight seasons,
and on two seasons held out until the method was fixed, the engine finds rosters that are clearly
stronger than those the teams built.
     The engine is best read as a decision support tool, and its results carry five implications for how
such a tool should be used in practice. First, value players in context rather than by individual
box scores: a front office that ignores teammate effects would build a different roster in almost
every summer and give up more than a point per 100 possessions, because these interactions are
first-order effects on a roster’s offense. Second, plan for the average role but keep the minutes
flexible: in-season rotation changes absorb most of the uncertainty about how newcomers will be
used (for the 2019 Clippers, fixing the rotation in advance would have cost more than two points per
100 possessions), and explicit hedging pays only when a roster’s value depends on several players
whose roles are unsettled. Third, treat the optimal roster as a short list: the objective landscape
is flat near the optimum, the best plan that kept Gilgeous-Alexander cost less than a tenth of a
point per 100 possessions, and the decision maker adds most value by choosing among near-optimal
rosters on dimensions the model does not observe. Fourth, price the moves, not only the roster:
re-solving the program with a single move imposed or ruled out yields the decision value of each
option, turning sensitivity analysis into a negotiation tool. Fifth, protection against playoff defenses
is cheap: a roster built to withstand a strong playoff defense that cuts into two of its favorite shot
types gives up only a few hundredths of a point per 100 possessions in the regular season, and
the stress test can quantify each candidate roster’s exposure before the front office commits to its
acquisitions.
     Several limitations bound the scope of these implications. The engine values offense only; the
trade market is modeled generously; the reported gains are measured by the same model that found
them and are therefore subject to the optimizer’s curse (Smith and Winkler, 2006), mitigated but
not eliminated by out-of-sample validation; the stress test measures exposure within the model
rather than predicting actual playoff declines; and roles are forecast from the season just ended, so
the model foresees neither injuries nor the value of draft picks. Each limitation suggests a direct
extension: a defensive value function constructed in the same way from the shots a lineup’s opponents
take; explicit modeling of the other side of each trade; linking stress-test exposure to realized playoff
outcomes over a longer panel; and embedding the single-offseason model in a multi-season dynamic
program with injuries, aging, draft assets, and contract years as state variables. The same framework
also extends naturally to workforce planning and other team-assembly problems in which individual
productivity depends on colleagues and managers can adapt operational assignments after personnel
commitments are made.


References
Basketball Insiders. NBA minimum salary scale and 2016-17 cap figures.                    https://www.
  basketballinsiders.com, 2016. Accessed November 2026.



                                                   31
Dimitris Bertsimas and Nathan Kallus. From predictive to prescriptive analytics. Management
  Science, 66(3):1025–1044, 2020. doi: 10.1287/mnsc.2018.3253.

Dimitris Bertsimas and Melvyn Sim. The price of robustness. Operations Research, 52(1):35–53,
  2004. doi: 10.1287/opre.1030.0065.

John R. Birge and François Louveaux. Introduction to Stochastic Programming. Springer New York,
  2011. ISBN 9781461402374. doi: 10.1007/978-1-4614-0237-4.

Bart H. Boon and Gerard Sierksma. Team formation: Matching quality supply and quality demand.
  European Journal of Operational Research, 148(2):277–292, 2003. doi: 10.1016/s0377-2217(02)
  00684-7.

James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal
  Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and Qiao
  Zhang. JAX: Composable transformations of Python+NumPy programs. http://github.com/
  jax-ml/jax, 2018.

Fan Bu, Sonia Xu, Katherine Heller, and Alexander Volfovsky. SMOGS: Social network metrics of
  game success. In Proceedings of the 22nd International Conference on Artificial Intelligence and
  Statistics, volume 89 of Proceedings of Machine Learning Research, pages 2406–2414, 2019.

Daniel Cervone, Alex D’Amour, Luke Bornn, and Kirk Goldsberry. A multiresolution stochastic
 process model for predicting basketball possession outcomes. Journal of the American Statistical
 Association, 111(514):585–599, 2016. doi: 10.1080/01621459.2016.1141685.

Timothy C. Y. Chan and Douglas Fearing. Process flexibility in baseball: The value of positional
  flexibility. Management Science, 65(4):1642–1666, 2019. doi: 10.1287/mnsc.2017.3004.

David B. Dahl. Model-Based Clustering for Expression Data via a Dirichlet Process Mixture
 Model, page 201–218. Cambridge University Press, 2006. ISBN 9781107636989. doi: 10.1017/
 cbo9780511584589.011.

Philippe De Bruecker, Jorne Van den Bergh, Jeroen Beliën, and Erik Demeulemeester. Workforce
  planning incorporating skills: State of the art. European Journal of Operational Research, 243(1):
 1–16, 2015. doi: 10.1016/j.ejor.2014.10.038.

Jingwen Deng, Shujie Ma, Sergio J. Rey, and Guanyu Hu. Linking COPD prevalence with
  income distribution: A spatial heterogeneous compositional regression via geographically weighted
  penalized approach. Annals of the American Association of Geographers, 2026. doi: 10.1080/
  24694452.2026.2722318. Advance online publication.

Karel Devriesere, László Csató, and Dries Goossens. Tournament design: A review from an
 operational research perspective. European Journal of Operational Research, 324(1):1–21, 2025.
 doi: 10.1016/j.ejor.2024.10.044.

Adam N. Elmachtoub and Paul Grigas. Smart “predict, then optimize”. Management Science, 68
 (1):9–26, 2022. doi: 10.1287/mnsc.2020.3922.




                                                32
Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Characterizing the spatial
  structure of defensive skill in professional basketball. The Annals of Applied Statistics, 9(1):
  94–121, 2015. doi: 10.1214/14-aoas799.

Tilmann Gneiting and Adrian E Raftery. Strictly proper scoring rules, prediction, and es-
  timation. Journal of the American Statistical Association, 102(477):359–378, 2007. doi:
  10.1198/016214506000001437.

Luca Grassetti, Ruggero Bellio, Luca Di Gaspero, Giovanni Fonseca, and Paolo Vidoni. An extended
  regularized adjusted plus-minus analysis for lineup management in basketball using play-by-play
  data. IMA Journal of Management Mathematics, 32(4):385–409, 2021. doi: 10.1093/imaman/
  dpaa022.

Martin B. Haugh and Raghav Singal. How to play fantasy sports strategically (and win). Management
 Science, 67(1):72–92, 2021. doi: 10.1287/mnsc.2019.3528.

Matthew D. Hoffman and Andrew Gelman. The No-U-Turn sampler: Adaptively setting path
 lengths in Hamiltonian Monte Carlo. Journal of Machine Learning Research, 15(47):1593–1623,
 2014.

Hoops Rumors. Salary cap, tax line, exception and minimum-salary figures for the 2016-17 to
 2025-26 seasons. https://www.hoopsrumors.com, 2025. Accessed November 2026.

Guanyu Hu, Hou-Cheng Yang, and Yishu Xue. Bayesian group learning for shot selection of
 professional basketball players. Stat, 10(1):e324, 2021. doi: 10.1002/sta4.324.

Q. Huangfu and J. A. J. Hall. Parallelizing the dual revised simplex method. Mathematical
  Programming Computation, 10(1):119–142, 2018. doi: 10.1007/s12532-017-0130-5.

Jieying Jiao, Guanyu Hu, and Jun Yan. A Bayesian marked spatial point processes model for
  basketball shot chart. Journal of Quantitative Analysis in Sports, 17(2):77–90, 2021. doi:
  10.1515/jqas-2019-0106.

Samuel Kalman and Jonathan Bosch. NBA lineup analysis on clustered player tendencies. In MIT
  Sloan Sports Analytics Conference, 2020.

Tarak Kharrat, Ian G. McHale, and Javier López Peña. Plus–minus player ratings for soccer.
  European Journal of Operational Research, 283(2):726–736, 2020. doi: 10.1016/j.ejor.2019.11.026.

Anton J. Kleywegt, Alexander Shapiro, and Tito Homem-de Mello. The sample average approxima-
 tion method for stochastic discrete optimization. SIAM Journal on Optimization, 12(2):479–502,
 2002. doi: 10.1137/s1052623499363220.

Gen Li, Yan Li, and Kun Chen. It’s all relative: Regression analysis with compositional predictors.
 Biometrics, 79(2):1318–1329, 2023. doi: 10.1111/biom.13703.

Saha Malaki, Navid Izady, and Lilian M. de Menezes. A framework for optimal recruitment of
  temporary and permanent healthcare workers in highly uncertain environments. European Journal
  of Operational Research, 308(2):768–781, 2023. doi: 10.1016/j.ejor.2022.12.008.



                                                33
Allan Z. Maymin, Philip Z. Maymin, and Eugene Shen. NBA chemistry: Positive and negative
  synergies in basketball. International Journal of Computer Science in Sport, 12(2):4–23, 2013.

Ian G. McHale and Samuel D. Relton. Identifying key players in soccer teams using network
  analysis and pass difficulty. European Journal of Operational Research, 268(1):339–347, 2018. doi:
  10.1016/j.ejor.2018.01.018.

Jingcheng Meng, Yimeng Ren, Xuening Zhu, and Guanyu Hu. Spatially clustered compositional
  regression: A nonparametric Bayesian approach. Journal of Computational and Graphical
  Statistics, 35(1):51–62, 2026. doi: 10.1080/10618600.2025.2500978.

Andrew Miller, Luke Bornn, Ryan Adams, and Kirk Goldsberry. Factorized point process intensities:
 A spatial analysis of professional basketball. In Proceedings of the 31st International Conference
 on Machine Learning, volume 32 of Proceedings of Machine Learning Research, pages 235–243,
 2014.

Jeffrey W. Miller and David B. Dunson. Robust Bayesian inference via coarsening. Journal of the
  American Statistical Association, 114(527):1113–1125, 2019. doi: 10.1080/01621459.2018.1469995.

Jeffrey W. Miller and Matthew T. Harrison. Mixture models with a prior on the number of
  components. Journal of the American Statistical Association, 113(521):340–356, 2018. doi:
  10.1080/01621459.2016.1255636.

Megan Muniz and Tülay Flamand. Sports analytics for balanced team-building decisions. Journal
 of the Operational Research Society, 74(8):1892–1909, 2023. doi: 10.1080/01605682.2022.2118634.

Oliver Müller, Alexander Simons, and Markus Weinmann. Beyond crowd judgments: Data-driven
  estimation of market value in association football. European Journal of Operational Research, 263
 (2):611–624, 2017. doi: 10.1016/j.ejor.2017.05.005.

National Basketball Association. NBA.com/Stats. https://www.nba.com/stats, 2026. Accessed
 November 2026.

National Basketball Association and National Basketball Players Association. Collective bargaining
  agreement. Agreement in force for the 2011-12 to 2016-17 league years, 2011.

National Basketball Association and National Basketball Players Association. Collective bargaining
  agreement. Agreement in force for the 2017-18 to 2022-23 league years, 2017.

National Basketball Association and National Basketball Players Association. Collective bargaining
  agreement. Agreement in force from the 2023-24 league year, 2023.

NBA Communications. Salary cap announcements for the 2016-17 to 2024-25 seasons. https:
 //pr.nba.com, 2024. Accessed November 2026.

G. Pantuso and L. M. Hvattum. Maximizing performance with an eye on the finances: a chance-
  constrained model for football transfer market decisions. TOP, 29(2):583–611, 2021. doi: 10.1007/
  s11750-020-00584-9.

Giovanni Pantuso. The football team composition problem: a stochastic programming approach.
 Journal of Quantitative Analysis in Sports, 13(3):113–129, 2017. doi: 10.1515/jqas-2017-0030.

                                                34
Swar Patel. nba_api: An API client package to access the APIs for NBA.com. https://github.
  com/swar/nba_api, 2018.

Du Phan, Neeraj Pradhan, and Martin Jankowiak. Composable effects for flexible and accelerated
 probabilistic programming in NumPyro, 2019. arXiv:1912.11554.

Brian J. Reich, James S. Hodges, Bradley P. Carlin, and Adam M. Reich. A spatial analysis
  of basketball shot chart data. The American Statistician, 60(1):3–12, 2006. doi: 10.1198/
  000313006X90305.

R. Tyrrell Rockafellar and Stanislav Uryasev. Optimization of conditional value-at-risk. The Journal
  of Risk, 2(3):21–41, 2000. doi: 10.21314/jor.2000.038.

Nathan Sandholtz, Jacob Mortensen, and Luke Bornn. Measuring spatial allocative efficiency
 in basketball. Journal of Quantitative Analysis in Sports, 16(4):271–289, 2020. doi: 10.1515/
 jqas-2019-0126.

James E. Smith and Robert L. Winkler. The optimizer’s curse: Skepticism and postdecision surprise
  in decision analysis. Management Science, 52(3):311–322, 2006. doi: 10.1287/mnsc.1050.0451.

Sports Reference LLC. NBA player contracts. https://www.basketball-reference.com/
  contracts/players.html, 2025. Copies archived by the Internet Archive (https://web.
  archive.org) on 10 November 2024 and 23 October 2025. Accessed November 2026.

Sports Reference LLC. Basketball-Reference.com. https://www.basketball-reference.com, 2026.
  Accessed November 2026.

Enzo Villafuerte and Felipe Aros-Vera. Beyond the pitch: An integrated machine learning and
  operations research methodology for financially sustainable squad formation. European Journal
 of Operational Research, 2026. doi: 10.1016/j.ejor.2026.09.039.

Benjamin Williams, Erin M. Schliep, Bailey K. Fosdick, and Ryan Elmore. Expected points above
  average: A novel NBA player metric based on Bayesian hierarchical modeling. The Annals of
 Applied Statistics, 19(4):3492–3507, 2025. doi: 10.1214/25-AOAS2079.

Eliot Wong-Toi, Hou-Cheng Yang, Weining Shen, and Guanyu Hu. A joint analysis for field goal
  attempts and percentages of professional basketball players: Bayesian nonparametric resource.
  Journal of Data Science, 21(1):68–86, 2023. doi: 10.6339/22-jds1062.

Maoran Xu and Guanyu Hu. Learning collapsed patterns in compositional data: A Bayesian
 heterogeneous relative-shift approach, 2026. arXiv:2606.07373.

Kazuhiro Yamada and Keisuke Fujii. Offensive lineup analysis in basketball with clustering players
 based on shooting style and offensive role, 2024. arXiv:2403.13821.

Fan Yin, Jieying Jiao, Jun Yan, and Guanyu Hu. Bayesian nonparametric learning for point
  processes with spatial homogeneity: A spatial analysis of NBA shot locations. In Proceedings of
  the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine
  Learning Research, pages 25523–25551, 2022.



                                                35
Fan Yin, Guanyu Hu, and Weining Shen. Analysis of professional basketball field goal attempts via
  a Bayesian matrix clustering approach. Journal of Computational and Graphical Statistics, 32(1):
  49–60, 2023. doi: 10.1080/10618600.2022.2085727.

Siming Zhang, Zhehui Shen, Shijie Chen, and Jian Zhou. A rolling-horizon stochastic optimization
  framework for NBA franchise management with distributionally robust risk constraints, 2026.
  arXiv:2604.06548.




                                               36
                                                                             Appendix

A     Data
Shots and cells. Every regular-season field-goal attempt carries the scorer’s coordinates and
an action description. The zone follows from the coordinates (restricted area, paint outside it,
mid-range, corner three, above-the-break three); the movement type from the description, mapped
to drive, cut, pull-up, post-up or paint touch, and spot-up. Labels were checked against the league’s
tracking-based play-type classifications (National Basketball Association, 2026) season by season
(Figure 10); scorers in different arenas use the default labels at different rates, which is why the
shot model carries an arena-by-movement term. The same retention rule applies to every season.
Figure 11 shows how often each cell is used and how much players’ mixes vary within and between
players.

                                             (a) Catch-and-shoot (official tracking)             (b) Pull-up (official tracking)
                                      1.00                                               1.00
       Player-season r




                                      0.95                                               0.95


                                      0.90                                               0.90


                                      0.85     SportVU     Second Spectrum   Hawk-Eye    0.85


                                                                                          1.4
                                       1.4
             Label count ÷ official




                                                                                             1
                                        1
                                                                                          0.7

                                       0.7                                                0.5


                                       0.5
                                         16 6
                                         17 7
                                         18 8
                                         19 9
                                         20 0
                                         21 1
                                         22 2
                                         23 3
                                              4




                                                                                             16 6
                                                                                             17 7
                                                                                             18 8
                                                                                             19 9
                                                                                             20 0
                                                                                             21 1
                                                                                             22 2
                                                                                             23 3
                                                                                                  4
                                           -1
                                           -1
                                           -1
                                           -1
                                           -2
                                           -2
                                           -2
                                           -2
                                           -2




                                                                                               -1
                                                                                               -1
                                                                                               -1
                                                                                               -1
                                                                                               -2
                                                                                               -2
                                                                                               -2
                                                                                               -2
                                                                                               -2
                                         15




                                                                                             15




                                                           Season                                               Season

                                                           Label groups used in this paper             Other label groupings

                               Figure 10: Movement labels against the league’s tracking classifications, by season.



Lineups and exposures. The unit of the shot model is a stint: an interval with the same ten
players on the floor. Lineups come from the league’s rotation records or, where those are missing,
from a reconstruction of the substitutions in the play-by-play. Exposure is counted in offensive
possessions.


                                                                                    37
                                            (a) How often each cell is used                                     (b) How much players' shot mixes vary
                                           dots: seasons, 2015-16 (dark blue) to 2023-24 (pink); tick: median
                                 Drive
                                   Cut
        Restricted area
                           Post / paint
                              Spot-up

                                 Drive
                                   Cut
                 Paint         Pull-up
                           Post / paint
                              Spot-up

                                 Drive
                               Pull-up
             Mid-range
                           Post / paint
                              Spot-up

                                 Pull-up
              Corner 3
                                Spot-up

                                 Pull-up
        Above-break 3
                                Spot-up


                                                 10
                                                      2
                                                                      10
                                                                           3
                                                                                           10
                                                                                                4               0      2      4       6      8      10     12     14

                                                          Attempts per season (log scale)                           SD of a player's true share of attempts (pp)

                                                                               Between players           Within a player, between lineups        Sampling noise of a median lineup



       Figure 11: Attempts per cell, and the variation of shot mixes between and within players.


Salaries and the cap. Player salaries by season come from Basketball-Reference team pay-
rolls (Sports Reference LLC, 2026), and for 2024-25 and 2025-26 from its contracts page as archived
after opening night (Sports Reference LLC, 2025), matched to league identifiers by name, team and
season; a player who logged minutes without a salary row receives the season’s minimum salary
for zero years of service. A mover’s salary skips the row of the team he left when it records a
buyout. Table 9 gives the amounts of each league year, each checked against a league release (NBA
Communications, 2024) or contemporary press source (Hoops Rumors, 2025; Basketball Insiders,
2016).

Table 9: Salary-cap amounts by league year ($M), and the collective bargaining agreement in force (National
Basketball Association and National Basketball Players Association, 2011, 2017, 2023).

   League year            Cap              Tax              First apron               Second apron                  Mid-level             Taxpayer mid-level              Agreement
   2016-17             94.14          113.29                   117.29                          —                        5.63                       3.48                        2011
   2017-18             99.09          119.27                   125.27                          —                        8.41                       5.19                        2017
   2018-19            101.87          123.73                   129.82                          —                        8.64                       5.34                        2017
   2019-20            109.14          132.63                   138.93                          —                        9.26                       5.72                        2017
   2020-21            109.14          132.63                   138.93                          —                        9.26                       5.72                        2017
   2021-22            112.41          136.61                   143.00                          —                        9.54                       5.89                        2017
   2022-23            123.66          150.27                   156.98                          —                       10.49                       6.48                        2017
   2023-24            136.02          165.29                   172.35                        182.79                    12.41                       5.00                        2023
   2024-25            140.59          170.81                   178.13                        188.93                    12.82                       5.17                        2023
   2025-26            154.65          187.90                   195.95                        207.82                    14.10                       5.69                        2023



Movers and transactions. For each player who changed teams after season t, transaction
records (Sports Reference LLC, 2026) give how he left (traded in the summer, traded or waived
during t, free agent) and his contract status in t + 1. A summer trade leaves the player under his
contract; a team cannot re-sign a player it waived; a player gone during t is no longer his old team’s.



                                                                                                    38
Seasons. Only the first pair reads 2015-16’s play-by-play, shots and playoffs, and its role model
adds the box-score totals of 2014-15; every other pair’s role model reads 2015-16 through its box
score only. In 2024-25 one game with a defective feed is excluded. In 2025-26 the league’s traditional
box-score service returns empty tables for most games; those games take the next version of the
service, written in the same format, after checking that the two agree on the games both return.


B     The role model
Model. To value potential additions by player type, we define player roles through a Bayesian
mixture model that joins box scores with shot charts. For player-season i in season s(i) with minutes
Mi and role zi ,

        Xij | zi = k ∼ NegBin (Mi /36) ξs(i)j µkj , ϕj ,      j ∈ {box counts, total attempts},
                                                        

      Yi | ni , zi = k ∼ DirMult ni , κ softmax(log ψk + δs(i) ) ,
                                                                

                   zi ∼ Categorical(πgroup(i) ),

where ξ is a season-by-statistic multiplier for league-wide drift, Yi is the count of the player-season’s
attempts over the 25 cells, ψk represents role k’s cell shares, δs is a season shift per cell, and π
is the role mix of each position group. The box counts are points, attempts, free throws, assists,
turnovers, rebounds, steals and blocks. The Dirichlet-multinomial term enters the likelihood with
weight 0.1, so that shots refine roles defined by the whole box score instead of overriding them. We
sum out the discrete role assignments analytically and sample the remaining parameters with the
No-U-Turn sampler (Hoffman and Gelman, 2014) in NumPyro (Phan et al., 2019) on a GPU.

Choosing the number of roles. We choose seven roles for their use to a front office rather than
for forecasting accuracy. To select the number of roles, we fit a sparse mixture of ten components to
every season under the coarsened posterior of Miller and Dunson (2019), with robustness parameter
α ∈ {50, 100, 150, 200, 300, 500} across four chains each. This sweep yields 4, 5, 6, 6, 9 and 10
occupied roles. The fit gained per step falls from 1.47 to 0.33 by six roles, the smallest role holds
14.0% to 6.2% of minutes, and chain agreement is highest up to six or seven roles. Because no
value in the grid yields seven or eight roles, we fit seven roles directly. For each of the seven pairs
whose training season falls between 2016-17 and 2022-23, all four chains of the exact posterior
find seven roles, with role-rate R
                                 b at most 1.013. The seventh role splits the forwards into spot-up
connectors (corner spot-ups and rim cuts) and two-way wings, a distinction front offices use. At full
shot weight, the runner-up configuration with six roles costs 0.10 to 0.13 per game of held-out log
score. Figure 12 shows each role’s share of minutes by season.

Fold fits and draws. We fit the roles separately for each season pair and draw from the posterior
to represent uncertainty in how players will be used. Each season pair’s roles are fitted on the
seasons up to its training season. The engine’s roles and draws come from the coarsened posterior
(α = 200), whose spread captures a player’s role uncertainty; Figure 12 uses the exact posterior of
the pair trained on 2022-23. Under the coarsened posterior the seventh role occasionally empties in
a draw, which loosens the role rates of the kept chains. Players with fewer than 100 minutes in the
season before a decision draw their roles from their position group’s role mix with a prior weight
of three, so their uncertainty is wide. The same 20 draws are used by every program of a season.

                                                   39
Across the ten fits, one to three of the four chains share the reference chain’s roles (the others split
the same continuum of players differently), with no divergences and role-rate R     b between 1.03 and
3.21, the highest for the fit through 2018-19. The first pair’s fit, on 2015-16 and the box-score totals
of 2014-15, keeps three chains, with 8 of 50 draws leaving a role empty (R  b 1.11), and the fit through
2024-25 keeps one, with 13 of 50 (R 1.41). All fits were used as fitted.
                                     b


                                                                                                                    Primary creator
                                           25
       Share of the season's minutes (%)




                                           20

                                                                                                                    Two-way forward

                                           15                                                                       Shooter
                                                                                                                    Spot-up connector
                                                                                                                    Playmaker
                                           10                                                                       Rim big
                                                                                                                    Hub big


                                                2015-16 2016-17 2017-18 2018-19 2019-20 2020-21 2021-22 2022-23
                                                                             Season of the statistics

                                           Figure 12: The seven roles’ share of minutes by season, with 90% posterior bands.



C     The shot model
Attempts. To quantify how teammates influence where and how frequently a player shoots, we
model attempt counts across court cells with a penalized Poisson regression. For the player in lineup
slot u of a stint, the attempt count Yuc in cell c is Poisson with mean Eu exp(ηuc ), where Eu is the
stint’s offensive possessions and
                                            ηuc = µc + 12 h 1[home] + θarena(u),m(c) + sq(u),c + βc⊤ bu + (a⊤          ⊤
                                                                                                            u ug(c) )(bu vg(c) ),

with bu = H ⊤ w̄−u the four teammates’ mean role shares and au = H ⊤ wu the shooter’s own, both
in Helmert contrasts H of the seven roles. The arena term absorbs how each arena’s scorers record
movement types. Because the role shares sum to one, only contrasts of the slopes are identified, and
we report them as relative shifts against an average teammate (Li et al., 2023). We fit the model as
a ridge-penalized Poisson regression at its posterior mode under normal priors: players’ profiles are
pulled toward the league average so that a player with few shots is not given an extreme profile,
and the shooter profiles s and arena terms θ have their own ridge penalties. The precisions of the
teammate effects (the role slopes, their pull toward the cell cluster and the interaction terms) are
chosen by the marginal likelihood on season t; the profile penalty is the one that forecasts best on
the previous season pair (fitted on t − 1 and scored on t; for the first pair, on a split of its training
season’s games); and the arena penalty is fixed at 4. No data from season t + 1 enter any penalty.

                                                                                     40
Makes. To determine whether an attempt succeeds, we fit a logistic regression model with the
same teammate predictors:
                             logit pqc = µm
                                          c + sqc + βc bq .
                                               m     m⊤



Sharing across cells. We share statistical strength across court locations by clustering cells that
exhibit similar responses to teammates. At the fitted coefficients, the curvature of the log likelihood
in the role block, with the other blocks profiled out, gives a normal approximation bc ∼ N (βc , Λ−1  c )
of each cell’s six teammate-role slopes. The cells with at least 500 training attempts are clustered
by the MRF-constrained mixture of finite mixtures (Miller and Harrison, 2018) of Meng et al.
(2026), run on these approximations (neighbors within graph distance two on the zone-by-movement
grid; λ chosen by the log pseudo-marginal likelihood; Dahl’s estimate of the partition, Dahl, 2006);
the clustering favors grouping cells that are neighbors on the court. Each cell’s slopes are then
pulled toward its cluster mean, βc ∼ N (β̄g(c) , τ −1 I), with τ chosen by the marginal likelihood of the
approximations; the nine or ten cells with fewer attempts keep their own slopes. The partitions
recur across seasons: self-created shots (drives and pull-ups), interior finishes (cuts and post-ups)
and corner spot-ups form clusters in most pairs (Figure 13). Against independent cells whose ridge
is chosen the same way, the pulled slopes gain +0.00 per game (+0.00 to +0.01) and are better in
five of the eight pairs; fixing the independent cells’ ridge at 4 instead raises their gain from +2.05 to
+2.07.
                   (a) 2015-16, 3 clusters                   (b) 2016-17, 3 clusters                    (c) 2017-18, 3 clusters                   (d) 2018-19, 5 clusters
   Above-break 3

        Corner 3

       Mid-range

           Paint

            Rim



                   (e) 2019-20, 5 clusters                   (f) 2020-21, 2 clusters                    (g) 2021-22, 4 clusters                   (h) 2022-23, 4 clusters
   Above-break 3

        Corner 3

       Mid-range

           Paint

            Rim
                                                   Spot-up




                                                                                              Spot-up




                                                                                                                                        Spot-up




                                                                                                                                                                                  Spot-up
                    Pull-up

                              Drive

                                      Post

                                             Cut




                                                              Pull-up

                                                                        Drive

                                                                                Post

                                                                                       Cut




                                                                                                         Pull-up

                                                                                                                   Drive

                                                                                                                           Post

                                                                                                                                  Cut




                                                                                                                                                   Pull-up

                                                                                                                                                             Drive

                                                                                                                                                                     Post

                                                                                                                                                                            Cut




                                              Self-created: pull-ups, drives
                                              outside the restricted area                    Rim drives, spot-ups                 Above-break spot-ups
                                              Interior finishes: cuts,                       Corner spot-ups                      Under 500 attempts:
                                              post-ups                                                                            own slopes


Figure 13: Groups of cells that share their teammate effects, one panel per season. Each square is a zone
(rows) and a movement type (columns); cells with the same color share their effects, and white cells, with
fewer than 500 attempts, keep their own.




                                                                                        41
The interaction ladder. We test higher-order interactions to evaluate whether a player’s own role
changes how he responds to teammates. Over the additive model, the rank-one shooter-by-teammate
interaction gains +0.07 per game on average (95% interval +0.03 to +0.11; −0.09 to +0.26 across
pairs), a rank-two interaction and teammate-pair redundancy terms nothing more, and the full-rank
interaction +0.09; five pairs gain and three lose a little. The makes model carries teammates’ roles
as well; they add nothing to the held-out score, so the teammate effects work through where and
how often players shoot.

The overlap term. We incorporate a crowding term to account for direct competition when
teammates seek shots in the same court cell. With the interaction model as an offset, the term γ Oqc ,
where Oqc is the four teammates’ expected attempts in the player’s cell per 100 possessions, is fitted
on season t with cell intercepts and scored on t + 1. Its coefficient is negative in every pair (−0.0080
to −0.0188 per teammate attempt, standard errors about 0.001) and its held-out gain positive in all
eight (+0.13 to +0.35 per game); a term in the teammates’ total usage adds nothing once it is in.

Transportability. We verify that predicted teammate effects carry over to players who change
teams. Figure 5(a, b) gives the damping factor κ across the court and by zone. On the movers’
held-out shot mix, the additive model gains +0.0045 per attempt over shooter-only rates (+0.0028
to +0.0060) and the mover’s own season-t mix loses 0.022.


D     Salary-rule constants
We state the trade-matching constants and salary aggregation rules of the 2011, 2017 and 2023
collective bargaining agreements (National Basketball Association and National Basketball Players
Association, 2011, 2017, 2023) that complete the cap constraints of Section 3.3. The salary-cap
constraints (3.9)–(3.16) use the amounts of each league year in Table 9 and the trade-matching
constants below. The narrow rule I ≤ a0 O + b0 , which applies above the line, has (a0 , b0 ) =
(1.25, $0.1M ) under the 2011 and 2017 agreements, (1.10, 0) in 2023-24 and (1.00, 0) from 2024-25.
Under the line, the ceiling a1 O + b1 and the two bands O + b2 and a3 O + b3 have (a1 , b1 , b2 , a3 , b3 ) =
(1.75, 0.1, 5, 1.25, 0.1) under the 2017 agreement, (1.5, 0.1, 5, 1.25, 0.1) under the 2011 agreement
and (2.0, 0.25, 7.5, 1.25, 0.25) under the 2023 agreement, in $M. Starting in 2024-25, a team that
aggregates two or more outgoing salaries in a trade is capped at the second apron. One more binary
variable z agg records this, with S0 + i Si ki ≤ Apron2 + M (1 − z agg ) and, for every trade arrival j,
                                       P

                                                        1
                                                                 (ki + xi ),
                                                             X
                                 z agg ≥ kj − xj −
                                                     |R| − 1 i∈R

which forces z agg = 1 when a player arrives in the trade phase while two or more players under
contract leave in it.


E     Stress-test calibration
Strong defenses are each season’s playoff teams in the best quarter by regular-season field-goal points
allowed per 100 possessions. For each series against them, the offense’s expected attempts per cell
are its own regular-season rates times the series’ possessions; the cut in a cell is one minus playoff


                                                     42
over expected attempts, kept between 0 and 0.5. The removed attempts that reappear in other
cells, and the points they score there, give the value v rr of a removed attempt. Each decision season
uses the playoffs up to its training season only (Table 10). Over the 62 series of 2016-17 to 2022-23,
strong defenses cut rim cuts by 17%, rim post-ups by 21%, paint spot-ups by 23%, mid-range
spot-ups by 20% and above-the-break spot-ups by 10%; above-the-break pull-ups rise 34%, paint
drives 25% and mid-range pull-ups 10%. For the broader playoff shift, Figure 14 compares all playoff
games with the league’s regular-season rates over 2016-17 to 2023-24.

Table 10: Calibration by training season: series against strong defenses, mean cut, share of removed attempts
re-routed, and value of a removed attempt.

              Training season        Series         Mean cut    Re-routed           Value of a removed attempt
              2015-16                       6           0.20           1.00                       1.01
              2016-17                       10          0.08           0.96                       1.23
              2017-18                       19          0.14           0.93                       1.03
              2018-19                       27          0.13           0.88                       0.92
              2019-20                       38          0.12           0.82                       0.80
              2020-21                       44          0.12           0.85                       0.82
              2021-22                       57          0.09           0.83                       0.78
              2022-23                       62          0.09           0.87                       0.81
              2023-24                       69          0.09           0.85                       0.79


                        (a) Attempts per 100 possessions                      (b) Field-goal percentage, points

        Above-break 3    +43%                                   -8%             -0.6                              -0.6



             Corner 3    +36%                                   +6%             +0.2                              -0.7



            Mid-range    +16%       +20%         -29%           -22%            +0.0      +1.5     +0.6           +0.2



                Paint    +21%       +9%          -16%     +7%   -32%            +0.6      -0.3     -0.5   +2.1    +1.2



                 Rim     -14%       -1%          -21%     -5%   -25%            -0.7      -0.5     -0.8   +0.3    -5.6
                                                                                                                  Spot-up
                          Pull-up


                                    Drive


                                                 Post




                                                                 Spot-up
                                                          Cut




                                                                                Pull-up


                                                                                          Drive


                                                                                                   Post


                                                                                                           Cut




Figure 14: The playoff shift: playoff attempts per 100 possessions against the league’s regular-season rates,
by zone and movement type, 2016-17 to 2023-24.



F     The frozen protocol and its deviations
What was frozen. Before either untouched season was opened, the code was fixed at one commit;
the models (seven shot-informed roles, the 25-cell shot model with pulled cell clusters, the rank-one

                                                                43
interaction and the overlap term, the capped lineup value with κ = 0.75, the engine’s objective and
constraints, the stress calibration); the data rules; and the ten claims of Table 7, each with its range
over the eight open pairs. Each untouched season was then processed and scored once by a scripted
run in which every fit, penalty and tuning choice uses the seasons before it, and the season enters
only to be scored. The run was rehearsed beforehand on the 2022-23 → 2023-24 pair under another
name; it reproduced that pair’s quantities to within 0.01, except the value of modeling synergy
(0.48 against 0.44, and 1.07 against 1.16), because the engine chose differently among rosters of
equal value (the same roster for 17 of 30 teams, values within 0.007 for all).

Three deviations. Three data problems came to light during the runs. Each fix changes how
data are read, not a model, a setting or a claim, and each was tested before its results were used.
   (i) Minimum salaries for the untouched seasons. The salary table’s rule for players without a
       salary row had not run for 2024-25, whose box scores were sealed when the table was built, so
       27 of the 139 movers into 2024-25 had no salary and 24 of the 30 pools could not be built.
       The first run solved six offseasons (engine minus real roster 4.90, VSS 0.05, synergy 0.31 and
       0.77, value of overlap 0.12 on those six). With the rule applied (156 rows for 137 players), the
       re-run solved 29.
  (ii) 2025-26 box scores. The league’s traditional box-score service returned no rows for 1,199 of
       the 1,230 games; those games take the next version of the service, in the same format. On the
       31 games both return, the two agree except for one plus-minus value among 799 player rows.
 (iii) The order of games. A player’s last team in season t and first team in t + 1 were read from
       box scores sorted by game identifier, which is not chronological where games were rescheduled
       (2020-21, 2021-22) or added late (the in-season tournament, from 2023-24); some players
       acquired at the trade deadline fell out of their new team’s pool. Ordering by game date
       changes 13 of the 30 pools of 2025, 8 of 2024 (including Washington, which without its deadline
       acquisitions had no feasible roster) and 12 of the open pairs (5 in 2020, 4 in 2021, 3 in 2023).
       Every affected case was solved again in every version it had been run in. Table 11 gives claims
       7 to 10 before and after; of the open-pair ranges, two move at two decimals: claim 7’s lower
       end (3.68 to 3.67) and claim 8’s upper end (0.46 to 0.45).

   Table 11: Claims 7–10 before and after the game-order fix, for the offseasons whose pools changed.

   Offseason        Engine minus real      VSS         Synergy (additive / shooter-only)    Overlap
   2020                4.05 → 4.04      0.29 → 0.27        0.58 / 1.82 → 0.53 / 1.84       0.03 → 0.02
   2021                4.65 → 4.65      0.46 → 0.45        0.46 / 0.96 → 0.48 / 0.96       0.09 → 0.09
   2023                3.68 → 3.67      0.17 → 0.17        0.44 / 1.16 → 0.43 / 1.11       0.06 → 0.05
   2024 (2024-25)      4.49 → 4.50      0.05 → 0.07        0.47 / 0.93 → 0.58 / 0.91       0.09 → 0.10
   2025 (2025-26)      3.94 → 3.83      0.18 → 0.14        0.78 / 1.48 → 0.82 / 1.49       0.09 → 0.07



Role fits used as fitted. The role fit through 2024-25, which feeds the 2025-26 scores, kept one
of its four chains (the others found six roles); 13 of its 50 draws leave a role empty and the role
rates’ Rb reaches 1.41. It was used as fitted, as were the other fits (Appendix B).




                                                  44
