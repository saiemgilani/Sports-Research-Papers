<!-- source: library/preprints/arXiv/2026/2026 - The efficacy-competitiveness frontier in the Swiss system - Csato et al..pdf -->
<!-- arXiv:2610.01997 | https://arxiv.org/abs/2610.01997 | filed 2026-10-19 -->

# The efficacy-competitiveness frontier in the Swiss system

                                                                        The efficacy-competitiveness
                                                                        frontier in the Swiss system
                                                                       László Csató∗               Balázs R. Sziklai†

                                                                                      2nd October 2026
arXiv:2610.01997v1 [physics.soc-ph] 1 Oct 2026




                                                                                             Abstract
                                                       An ideal tournament is both efficacious and attractive: it selects the best player as
                                                       the winner, but only at the end of the tournament in order to maintain suspense
                                                       as long as possible. We identify and explore the trade-off between these criteria in
                                                       Swiss-system chess team tournaments via simulations. Organising more rounds is
                                                       shown to improve efficacy but increase the probability of a stakeless last round. The
                                                       2008 reform in the Chess Olympiad ranking is found to be a questionable move,
                                                       as the previous rule based on board points determines the efficacy-competitiveness
                                                       frontier, regardless of whether two or three points are awarded for winning a match.
                                                       Combining board points and match points is better than using match points only.
                                                       Our results can help optimise the design of the Swiss system, which, besides chess,
                                                       is also widely used in e-sports.

                                                 Keywords: attractiveness; efficacy; OR in sports; Swiss system; simulation
                                                 MSC class: 62F07, 68U20, 90-10, 90B90
                                                 JEL classification number: C44, C53, Z20




                                                   ∗
                                                      Corresponding author
                                                 E-mail: laszlo.csato@sztaki.hun-ren.hu
                                                 Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN),
                                                 Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and
                                                 Decision Systems, Budapest, Hungary
                                                 Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of
                                                 Operations Research and Actuarial Sciences, Budapest, Hungary
                                                    †
                                                      E-mail: sziklai.balazs@krtk.elte.hu
                                                 Institute of Economics, ELTE Centre for Economic and Regional Studies, Budapest, Hungary
                                                 Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of
                                                 Operations Research and Actuarial Sciences, Budapest, Hungary
1     Introduction
According to a recent survey of tournament design, efficacy and attractiveness are among
the most important design criteria (Devriesere et al., 2025). Efficacy is the ability of the
tournament to approxiamte the latent strength ranking of the players by the ranking based
on the results of matches. Indeed, a tournament is often considered a selection mechanism
used to identify the best team in a noisy environment (Ryvkin, 2010). While attractiveness
has several different interpretations, they are all connected to the entertainment generated
by the tournament. Here we adopt a straightforward definition called competitiveness:
the winner should not be decided before the last round of the tournament. This choice is
supported by empirical findings. For example, elevated interest is detected for football
matches that are potentially significant for end-of-season outcomes (Buraimo et al., 2022),
and search interest declines substantially in the Formula One World Drivers’ Championship
after the winner becomes known (Garcia-del Barrio and Reade, 2022). Avoiding a stakeless
match played by the final winner is also important from the perspective of fairness, since
its opponent can win more easily in the absence of incentives to win, as the favourite
probably does not exert full effort (Csató and Gyimesi, 2026a).
    Even though efficacy and competitiveness are both crucial characteristics of tourna-
ments, we do not know of any previous study that explores the trade-off between them.
We address this research gap by investigating the Swiss system. The Swiss system is a
non-eliminating tournament format, where the contestants play a given number of rounds
chosen by the decision-maker, which gives a crucial flexibility missing from knockout and
round-robin tournaments.
    Aside from the adaptable nature of the Swiss system, our focus on it is explained by
three reasons. First, according to an extensive simulation study by Sziklai et al. (2022), the
Swiss system provides the best trade-off between efficacy and the number of matches among
the most popular tournament formats. Second, the last round became uncompetitive in
some Swiss-system chess tournaments. For instance, in the 2015 Australian Open, the
Chinese Grandmaster Ni Hua scored 9.5 points in the first 10 rounds, but the runners-up
had only 7.5 points when one point was awarded for a win, making the last, 11th round
uninteresting to most viewers (see https://s2.chess-results.com/tnr157180.aspx).
Third, the Chess Olympiad, one of the most prestigious chess tournaments, uses the Swiss
system. Furthermore, its ranking rules were fundamentally changed in 2008: since then,
the ranking is based on the number of match points instead of the number of board points.
    The 2008 reform had two important consequences. First, it made the margin of victory
irrelevant, except for tie-breaking rules: a narrow match victory and a large-margin victory
have the same reward in the primary criterion of the ranking. Second, it introduced
an additional strategic consideration for the teams. Chess games, especially at higher
levels, often end in draws. Players can often steer a game towards a draw by simplifying
the position and avoiding unnecessary risks. Even in an advantageous position, it may
be rational to settle for a draw if this secures a favorable team result. The two most
obvious case is if three boards have already produced decisive results, and a draw on
the remaining board is sufficient either to secure a victory for the team or to guarantee
a drawn match. Indeed, this behaviour is frequently observed in team competitions.
For example, during the 2018 Chess Olympiad, the Armenian player Lilit Mkrtchian
was reportedly instructed by her captain to seek a draw against Irina Krush, despite
having winning chances (see https://www.chess.com/news/view/chess-olympiad-u-
s-joins-poland-azerbaijan-in-lead).


                                              2
    This mechanism may further increase the number of drawn games. One way to
counteract this tendency could be providing stronger incentives for taking risks. Therefore,
some team chess competitions, such as the Global Chess League, award three points
for winning a match. There is an ongoing debate about how effective this rule is in
competitions where each team acts as a single decision-making entity, such as in football
(Lenten and Kendall, 2022). It is even less clear whether it has the same effect in team
chess, where the incentives of the team may differ from those of its individual players.
    The decision to use match points was probably motivated by a desire to strengthen
the team-competition nature of the tournament, while awarding extra points for match
victories aims to encourage teams to play for a win. Both objectives are valid, but they
can also affect efficacy and competitiveness as we will see.
    The paper is organised as follows. Section 2 gives an overview of previous works on
similar problems. The simulation method is described in Section 3, and the results are
presented in Section 4. Finally, Section 5 summarises the key findings and discusses
directions for future research.


2     Related literature
The Swiss system has been developed to rank a large number of players who play a relatively
small number of rounds without elimination. The pairing is dynamic; it depends on the
results of the previous rounds: players generally play against opponents with (roughly)
equal running score, subject to various constraints. This format, proposed by the Swiss
teacher Dr. Julius Müller, was applied first in 1895 at the 5. Schweizerische Schachturnier,
but is now used in other games such as bridge and Go. E-sports competitions—including
Counter-Strike: Global Offensive (CS:GO), Dota 2, Hearthstone, and Rocket League—often
use a variant of the Swiss system (Dong et al., 2023).
    The two major design issues in the Swiss system are the choice of the pairing algorithm
and the ranking method. Pairing is traditionally done by hand, but today several software
are available for this purpose; see, for example, the pioneering study Ólafsson (1990)
and the program Swiss-Manager (https://swiss-manager.at/). There are alternative
pairing algorithms in the literature: Kujansuu et al. (1999) determine the pairs by solving
a stable roommates problem, Glickman and Jensen (2005) consider a Bayesian optimal
design framework for pairing, while Sauer et al. (2024) suggest a parametric method
based on finding maximum weight matchings in an appropriately constructed graph. The
main challenge of ranking resides in the uncertain trade-off between the number of points
scored and the strength of opponents (Chebotarev, 1994; Csató, 2013, 2017; Csató et al.,
2026; Leiva Bertrán, 2025). Tie-breaking rules also play an important role in the Swiss
system due to the low number of rounds compared to the number of players, especially in
the middle of the ranking. Freixas (2022) uncovers some weaknesses of the widely used
Buchholz method, the arithmetic mean of points scored by all opponents.
    Efficacy, the ability of a tournament to rank the players according to their (unknown)
strengths, is usually examined via Monte Carlo simulations as the observed set of match
results is only one realisation of the interaction of several random variables. If the match
outcomes are deterministic, ranking in the Swiss system with eight players and three
rounds is perfect for the first and the last positions, but not for the middle positions
(Dinh et al., 2020). Appleton (1995) computes the chance that the best player wins with
random tie-breaking, is the sole winner, or shares the first place without tie-breaking when
8 or 16 players compete in five rounds. Sziklai et al. (2022) determine the efficacy of the

                                             3
                          Table 1: Input data of the simulations

                                        Setup A                      Setup B
 Number of teams                           32                           16
 Players per team                           4                            4
 Elo rating of the best player            2750                         2750
 Within team Elo decrease          40 for each player                  None
 Across team Elo decrease          10 for each team       100 from 1st to 2nd; none after


Swiss system for 32 players under six different models of winning probabilities and several
metrics of ranking ability. Similar to the current study, the number of rounds is assumed
to be a decision variable.
    Our measure of competitiveness, the probability of a stakeless last round, has received
serious attention in (incomplete) round-robin tournaments. Chater et al. (2021) consider
stakeless matches in various round-robin formats of the FIFA World Cup group stage,
and Csató et al. (2024) in double round-robin groups of four teams. Csató and Gyimesi
(2026a) study indifferent teams in the last round of the 2026 FIFA World Cup group stage.
Gyimesi (2024), Csató and Gyimesi (2026b), and Devriesere et al. (2026) compare the
pre-2024 and post-2024 formats of the UEFA Champions League from this perspective.
Csató (2023) explores the effect of tie-breaking rules on the competitiveness of matches
played in the last round of the four groups in the 2022/23 UEFA Nations League A. Finally,
Feddersen et al. (2023) document that betting markets believe European football teams
adjust their effort level according to the incentives at the end of the season; thus, the
impact of incentives can actually be seen in historical data.


3     Methodology
Following the standard approach in tournament design (Devriesere et al., 2025), we use
Monte Carlo simulations to quantify efficacy and competitiveness. Section 3.1 explains the
choice of team strengths. Section 3.2 describes the pairing mechanism and the probabilistic
model of Milvang (2015) used to generate match results. The tournament metrics are
presented in Section 3.3, and the details of the computations are discussed in Section 3.4.

3.1    Input data
We examine two settings regarding the strengths of players based on Elo points (Elo, 1978).
While both setups are synthetic since the Elo ratings are assigned according to a linear
pattern, the first is realistic and mimics the distribution of team strengths in a real-world
chess tournament. The second is simplified to help measure ranking accuracy.
   Table 1 summarises the basic information about both setups. The 2025 European Team
Chess Championship Open tournament (https://s2.chess-results.com/tnr1263013.
aspx) has motivated Setup A. There were 40 participating teams. If the teams and the
players within each team are ordered by their Elo ratings, the average rating difference
between consecutive teams is approximately 13 points, while the average difference between
consecutive players within the same team is around 43 points. The highest-ranked team
was Germany with an average Elo rating of 2681, and the second highest-ranked team
was the Netherlands, with an average Elo rating of 2675; a difference of 6 points. For

                                             4
comparison, the average Elo of the fourth and fifth highest-ranked teams, Azerbaijan and
England, differed by 21 Elo points. For the individual players of the Dutch team, the
average difference between the consecutive players is 39 points. Again, these differences
vary. The Elo difference between the best and second-best players is 87 points, whereas
the difference between the second- and third-best players is only 25 points.
    The European Team Chess Championship is a fairly typical tournament, and Setup A
models it in a stylized manner by rounding both average differences to the nearest multiple
of ten and ignoring their variation. The advantage of using synthetic rather than real data
resides in the transparent structure of expected winning probabilities. The strongest team
has approximately the same (expected) advantage over the second strongest team as the
19th-ranked team has over the 20th-ranked team, and likewise for any pair of consecutively
ranked teams. Even though a 100-point rating difference implies the same expected score
in the Elo rating system, this does not hold for the estimated model of Milvang (2015)
used in the following (see Section 3.2). However, the differences are small.
    Besides the variation in Elo differences, Setup A differs from the real tournament in
two further aspects. First, the number of teams is fixed at 32. Second, the number of
players in any team is four, but most teams enter the tournament with five players. They
are listed in a fixed board order, which cannot be modified during the tournament, but
the reserve player is allowed to play as a substitute on any board.
    In Setup B, all players of the first team have an Elo rating of 2750, while all players
of the other teams have an Elo rating of 2650. Consequently, the strong team has a
71.5% chance of winning the match against any other team, an 18.4% chance of playing
a draw, and a 10.1% chance of losing. Thus, the first team is the clear favourite to win
the tournament in Setup B. As we will see in Section 4, if more rounds are played, then
the probability that the first team is the only one with consistently strong performance
increases, since in a match between two weak teams, they have roughly a 35% chance
of winning. In the simple Setup B, the ranking of the teams is irrelevant except for the
position of the first team, which simplifies the quantification of efficacy.

3.2    The pairing method and the game prediction model
For pairing the teams in each round of the tournament, we use an integer linear program
that takes into account the current standings and the previous matchups. The objective
is to pair teams with similar scores, subject to the constraint that no pair of teams can
meet more than once. Hence, the team with the highest score is paired with the team
with the second-highest score whenever possible. If this is infeasible, it is paired with
the third-highest scoring team, and so on. Once the first pair has been determined, the
procedure is repeated for the remaining teams. This pairing rule is implemented by
minimising the sum of squared score differences within pairs.
    Formally, let 𝐺 = (𝑉, 𝐸) be the tournament graph, where the nodes (edges) in set 𝑉
(𝐸) represent the teams (matches). Let 𝐹 denote the set of feasible edges, corresponding
to pairs of teams that have not played against each other in the earlier rounds. Denote by
𝑠𝑢 the current score of team 𝑢 ∈ 𝑉 . Then the optimal solution to the following integer




                                            5
program gives the pairing in the next round:

                  max               (𝑠𝑢 − 𝑠𝑣 )2 𝑥𝑢𝑣
                            ∑︁

                          (𝑢,𝑣)∈𝐹

                   s.t.             𝑥𝑢𝑣 = 1,
                            ∑︁
                                                                ∀𝑢 ∈ 𝑉,
                          (𝑢,𝑣)∈𝐹

                          𝑥𝑢𝑣 ∈ {0, 1},                         ∀(𝑢, 𝑣) ∈ 𝐹.

If multiple optimal solutions exist, we use the solution returned by the solver in order to
minimise running time. The LP was implemented in Python using the PuLP package,
with COIN-OR Branch and Cut (CBC) as the default solver.
    Pairing, including in the first round, is based exclusively on the current scores of the
teams, which may be measured by board points, match points, or a combination of the two.
Tie-breaking is not specified explicitly; the algorithm only checks whether the matching is
valid, meaning that no two teams are paired more than once during the tournament, and
whether the objective function is optimal. Seeding is ignored, although it may improve
tournament efficacy (Sziklai et al., 2022).
    For winning probabilities, we use the empirical distribution of Milvang (2015), similar
to Sauer et al. (2024). It estimates win, draw, and loss probabilities from historical data,
taking into account colour allocation since white advantage is well-documented in chess
(Henery, 1992; Fecker, 2024). The model fits piecewise quadratic functions based on both
the rating difference and the average rating of the two players. Consequently, unlike in the
standard Elo method, the predicted probabilities depend slightly on the absolute rating
levels, as well as on the rating difference. In particular, the probability of a draw increases
with the mean strength of the players.

3.3    Tournament metrics
Four alternative measures are used to quantify efficacy:

      • The average rank of the winner;

      • Sum of Ranking Differences (SRD) computed from the true ranking and the final
        ranking of the teams;

      • The probability that the strongest team wins;

      • The probability that the strongest team finishes in the top three.

Sum of Ranking Differences is a comparative statistical method; see, for example, West
(2018) and Gere et al. (2022). SRD measures the distance between two rankings in 𝐿1
norm. It ranges from 0 to 1; 0 indicates perfect agreement between two rankings, while 1
corresponds to complete disagreement, attained when one ranking is the reverse of the
other. The distribution is not centred on 0.5 since the mean distance between a given
ranking and a randomly generated ranking is approximately 0.66 (Sziklai et al., 2025).
    The average rank of the winner and SRD are only considered in Setup A because the
15 weak teams are identical in Setup B. In the case of the first two measures, a lower value
is preferred, but a higher value is better for the probabilities. Therefore, a reversed scale
will be used for the average rank of the winner and SRD in the following.


                                                      6
    Our competitiveness metric is the probability of a non-stakeless last round: the
advantage of the team with the highest score after the penultimate round does not exceed
the maximum number of points to be scored in one round. A higher value, ideally close to
1, is preferred.
    To determine the final ranking, we consider different scoring rules. The number of
board points was used in the Chess Olympiad until 2006: one point for a win, half points
for a draw, zero points for a loss, summed over the four boards. The maximum number
of board points for a team in one round is four. The number of match points has been
used for ranking in the Chess Olympiad since 2008: two points for a win (at least 2.5
board points), one point for a draw (2-2 board points for the two teams, respectively), zero
points for a loss (at most 1.5 board points). The maximum number of match points for a
team in one round is two. The 3-1-0 system, which is common in association football, is
used in some prestigious individual chess competitions, such as the Bilbao Chess Masters
Final and the London Chess Classic. We apply this rule to match points: three points for
a win, one point for a draw, zero points for a loss. Then the maximum number of points
for a team in one round is three.
    As a robustness check, we also investigate whether combining board and game points
can improve the trade-off between efficacy and competitiveness. For this purpose, the sum
of board and match points is used, both with the 2-1-0 and the 3-1-0 system regarding
match points. The maximum number of points for a team in one round is six and seven,
respectively.
    Ties in the number of scores are broken by the traditional Sonneborn–Berger method
without the lowest result: a team receives the match points of all teams it defeated and
half the match points of all drawn opponents, but the lowest of these values is omitted.

3.4    Implementation
The number of rounds is fixed for any tournament and varies between 3–12 in Setup A
(32 teams) and between 3–9 in Setup B (16 teams). A round starts by pairing the teams
according to their current match points, see Section 3.2. For each pair of teams, players
are matched together according to their rating. Colours on board one are decided by play
history. If the two lead players played with different colours in the previous round, their
colours are reversed in the current round. If they had the same colour in the previous
round, the player who had black more often is assigned white. Otherwise, the colour
assignment is determined randomly. The remaining players are assigned to the colours in
an alternating manner. Thus, two-two players of every team play with the black and the
white pieces, respectively, in each match.
    The simulation was performed on a laptop equipped with an AMD Ryzen 9 8940HX
processor and 32 GB of RAM, running Windows 11 Pro. For each tournament, 40
thousand simulation runs were performed to ensure convergence. Depending on the setup,
the simulation took approximately 3–4 days to complete.


4     Results
Figure 1 presents the relationship between efficacy (the average rank of the winner and
SRD) and a non-stakeless last round in the realistic Setup A under the three basic scoring
rules. As expected, efficacy improves when more rounds are played (Lasek and Gagolewski,
2018)—but this is parallel with a decline in competitiveness. The last round never becomes

                                             7
                                                             Setup A, Average rank of the winner

                                100
 Non-stakeless last round (%)




                                 95



                                 90



                                 85



                                 80



                                 75
                                      4.8    4.6   4.4       4.2     4             3.8          3.6      3.4    3.2    3     2.8
                                                          Average rank of the winner (inverted scale)
                                  Board points            Match points                   Match points with three points for a win


                                                          Setup A, Sum of Ranking Differences (SRD)

                                100
 Non-stakeless last round (%)




                                 95



                                 90



                                 85



                                 80



                                 75
                                  0.38      0.36   0.34       0.32       0.3             0.28         0.26     0.24   0.22    0.2
                                                   Sum of Ranking Differences (SRD) (inverted scale)
                                  Board points            Match points                   Match points with three points for a win

   Figure 1: The efficacy-competitiveness trade-off: average rank of the winner and SRD
Note: The number of rounds increases from 3 to 12 (9) in Setup A (B) along the lines from left to right.




                                                                               8
   Non-stakeless last round (%)                Setup A, Strongest team wins                                                          Setup B, Strongest team wins




                                                                                          Non-stakeless last round (%)
                                  100                                                                                    100


                                                                                                                          90
                                   90
                                                                                                                          80


                                   80                                                                                     70


                                          0.15          0.2          0.25       0.3                                            0.3      0.4         0.5     0.6          0.7
                                                  Probability of winning                                                                    Probability of winning

                                        Setup A, Strongest team in top three                                                   Setup B, Strongest team in top three
 Non-stakeless last round (%)




                                  100                                                   Non-stakeless last round (%)     100


                                                                                                                          90
                                  90
                                                                                                                          80

                                  80
                                                                                                                          70


                                         0.4     0.45   0.5   0.55     0.6   0.65                                           0.6      0.65     0.7   0.75   0.8    0.85     0.9
                                        Probability of finishing in top three                                                   Probability of finishing in top three
                                    Board points               Match points                                              Match points with three points for a win

                                           Figure 2: The efficacy-competitiveness trade-off: Strongest team
Note: The number of rounds increases from 3 to 12 (9) in Setup A (B) along the lines from left to right.


stakeless if the number of rounds is three or four. However, the probability of an exciting
last round drops rapidly when the ranking is based on match points, and the situation is
even worse with the 3-1-0 system.
    The efficacy-competitiveness frontier is fully determined by the rule based on board
points, when the chance of a stakeless last round remains below 3% with 32 teams and 12
rounds. Since we do not know of any Swiss-system chess tournament consisting of more
than 11 rounds, the threat to attractiveness remains limited with this ranking system.
However, if the ranking is based on match points, the probability of a stakeless last round
exceeds 6% even with seven rounds. Our findings are insensitive to the choice of the
efficacy measure; the trade-off curve is quite similar when using the average rank of the
winner and the Sum of Ranking Differences.
    As Figure 2 shows, the main patterns are not affected by focusing on the strongest team
or by considering a 16-team tournament with a clear favourite (Setup B). Ranking based
on board points determines the Pareto frontier, and awarding three points for winning a
match remains suboptimal. Setup B reveals that selecting the strong team as the winner is

                                                                                    9
   Non-stakeless last round (%)         Setup A, Average rank of the winner                                                  Setup A, Sum of Ranking Diff.




                                                                                     Non-stakeless last round (%)
                                  100                                                                               100



                                   90                                                                                90



                                   80                                                                                80


                                             4.5       4      3.5        3                                                   0.35          0.3      0.25        0.2
                                        Avg. rank of the winner (inv. scale)                                                          SRD (inv. scale)


                                           Setup A, Strongest team wins                                                   Setup A, Strongest team in top three
 Non-stakeless last round (%)




                                  100
                                                                                   Non-stakeless last round (%)     100



                                   90                                                                               90



                                   80                                                                               80


                                         0.15         0.2       0.25         0.3                                             0.4    0.45   0.5   0.55   0.6   0.65
                                                Probability of winning                                                    Probability of finishing in top three
                                                    Board points
                                                    Match points
                                                    Board points plus match points
                                                    Match points with three points for a win
                                                    Board points plus match points with three points for a win

                                        Figure 3: The efficacy-competitiveness trade-off: All ranking systems
Note: The number of rounds increases from 3 to 12 along the lines from left to right.


increasingly challenging if one wants to achieve a higher accuracy: for a mere improvement
of 4 percentage points from 67% to 71%, the chance of an uninteresting last round grows
from 3.3% to more than 5.6%. Organising a higher number of rounds has diminishing
returns in terms of ranking accuracy, while its price in attractiveness is worryingly high.
    Design choices such as using match points instead of board points or awarding extra
points for match victories may serve valid objectives, but, according to Figures 1 and 2,
they come at the cost of competitiveness if efficacy is to be maintained. In this respect,
hybrid scoring systems are worth exploring, as they preserve the incentives created by
these design choices to a great extent, while making it possible to move closer to the
Pareto frontier.
    Figure 3 examines scoring systems based on the sum of board points and match points.


                                                                               10
Combining the two improves performance compared to using only match points (where a
win is worth either two or three points); however, there remains a substantial gap from
the Pareto frontier.


5     Concluding remarks
The current paper explores a previously unaddressed issue in tournament design: the
trade-off between two key criteria, the accuracy of the final ranking and the competitiveness
of the last round. To that end, we have examined the Swiss system, which ensures the best
possible ranking for a given number of matches (Sziklai et al., 2022). The Swiss system
is also widely used in chess and esports, while the number of rounds provide a crucial
flexibility for decision-makers.
    Our results uncover the need to balance the quality of the ranking and suspense in
the last round: the former can be improved only by playing a higher number of rounds,
which increases the likelihood that the winner will be determined early. This trade-off also
depends on the scoring rule; according to the simulations, ranking is Swiss-system chess
team tournaments should be based on the number of board points rather than the number
of match points, while combining board and match points is preferred to using match
points. These findings are remarkably robust to the choice of efficacy measure (average
rank of the winner or SRD) and the assumed strength distribution (Setup A or B).
    Therefore, the decision to replace board points with match points from the 2008 Chess
Olympiad has been a questionable step. While the reform may have strengthened the
team-competition nature of the tournament, ranking based on the number of match points
seems to be suboptimal with respect to the crucial efficacy-competitiveness trade-off.
Tournament organisers are encouraged to reconsider the scoring rule in light of our results.
    A substantial scope remains for future research. The pairing mechanism is a key feature
of the Swiss system, and alternative pairing algorithms could enhance its performance. In
particular, pairing the leading players against each other helps win the competition early
by defeating the direct opponents. For the sake of attractiveness, however, it would be
better to see the match between the strongest players towards the end of the tournament.
The second promising direction is offered by the analysis of incomplete round-robin
tournaments. In contrast to the Swiss system, these competitions use a static schedule; the
set of matches to be played is determined before the tournament starts. This difference
might have a significant impact on the tournament metrics considered here. Finally, the
effect of awarding an extra point for team victory when teams consist of several players
playing separate games needs to be investigated by empirical studies.


Acknowledgements
The research was supported by the National Research, Development and Innovation Office
under Grants FK 145838, K 146320, Advanced 152220, and by the János Bolyai Research
Scholarship of the Hungarian Academy of Sciences.


References
Appleton, D. R. (1995). May the best man win? Journal of the Royal Statistical Society:
 Series D (The Statistician), 44(4):529–538.

                                             11
Buraimo, B., Forrest, D., McHale, I. G., and Tena, J. D. (2022). Armchair fans: Modelling
  audience size for televised football matches. European Journal of Operational Research,
  298(2):644–655.

Chater, M., Arrondel, L., Gayant, J.-P., and Laslier, J.-F. (2021). Fixing match-fixing: Op-
  timal schedules to promote competitiveness. European Journal of Operational Research,
 294(2):673–683.

Chebotarev, P. Yu. (1994). Aggregation of preferences by the generalized row sum method.
 Mathematical Social Sciences, 27(3):293–320.

Csató, L. (2013). Ranking by pairwise comparisons for Swiss-system tournaments. Central
  European Journal of Operations Research, 21(4):783–803.

Csató, L. (2017). On the ranking of a Swiss system chess team tournament. Annals of
 Operations Research, 254(1-2):17–36.

Csató, L. (2023). How to avoid uncompetitive games? The importance of tie-breaking
  rules. European Journal of Operational Research, 307(3):1260–1269.

Csató, L., Devriesere, K., Goossens, D., Gyimesi, A., Lambers, R., and Spieksma, F.
 (2026). Ranking matters: Does the new format select the best teams for the knockout
  phase in the UEFA Champions League? International Journal of Sports Science &
 Coaching, 21(2):1123–1131.

Csató, L. and Gyimesi, A. (2026a). Increasing competitiveness by imbalanced groups: The
  example of the 48-team FIFA World Cup. European Journal of Operational Research,
  332(3):868–879.

Csató, L. and Gyimesi, A. (2026b). A probabilistic match classification model for low-
  scoring sports. Manuscript. DOI: 10.48550/arXiv.2601.09673.

Csató, L., Molontay, R., and Pintér, J. (2024). Tournament schedules and incentives
  in a double round-robin tournament with four teams. International Transactions in
 Operational Research, 31(3):1486–1514.

Devriesere, K., Csató, L., and Goossens, D. (2025). Tournament design: A review from an
  operational research perspective. European Journal of Operational Research, 324(1):1–21.

Devriesere, K., Goossens, D., and Spieksma, F. (2026). From groups to a single league:
 evaluating competitiveness in the UEFA Champions League. Journal of Quantitative
 Analysis in Sports, in press. DOI: 10.1515/jqas-2025-0128.

Dinh, A. V. N., Bao, N. P. H., Khalid, M. N. A., and Iida, H. (2020). Simulating
  competitiveness and precision in a tournament structure: A reaper tournament system.
  International Journal of Information Technology, 12(1):1–18.

Dong, Z.-L., Ribeiro, C. C., Xu, F., Zamora, A., Ma, Y., and Jing, K. (2023). Dynamic
 scheduling of e-sports tournaments. Transportation Research Part E: Logistics and
 Transportation Review, 169:102988.

Elo, A. E. (1978). The Rating of Chessplayers: Past and Present. Arco, New York, New
  York, USA.

                                            12
Fecker, N. (2024). Skewed expectations in the Elo rating system: Home advantage in
  football and white advantage in chess. Bachelor thesis, ETH Zürich.

Feddersen, A., Humphreys, B. R., and Soebbing, B. P. (2023). Contest incentives, team
  effort, and betting market outcomes in European football. European Sport Management
  Quarterly, 23(3):605–621.

Freixas, J. (2022). The decline of the Buchholz tiebreaker system: A preferable alternat-
  ive. In Nguyen, N. T., Kowalczyk, R., Mercik, J., and Motylska-Kuźma, A., editors,
  Transactions on Computational Collective Intelligence XXXVII, pages 1–20. Springer,
  Berlin, Heidelberg, Germany.

Garcia-del Barrio, P. and Reade, J. J. (2022). Does certainty on the winner diminish
 the interest in sport competitions? The case of Formula One. Empirical Economics,
 63(2):1059–1079.

Gere, A., Szakál, D., and Héberger, K. (2022). Multiobject optimization of national
 football league drafts: comparison of teams and experts. Applied Sciences, 12(13):6303.

Glickman, M. E. and Jensen, S. T. (2005). Adaptive paired comparison design. Journal of
  Statistical Planning and Inference, 127(1-2):279–293.

Gyimesi, A. (2024). Competitive balance in the post-2024 Champions League and the
 European Super League: A simulation study. Journal of Sports Economics, 25(6):707–
 734.

Henery, R. J. (1992). An extension to the Thurstone–Mosteller model for chess. Journal
 of the Royal Statistical Society Series D: The Statistician, 41(5):559–567.

Kujansuu, E., Lindberg, T., and Mäkinen, E. (1999). The stable roommates problem and
 chess tournament pairings. Divulgaciones Matemáticas, 7(1):19–28.

Lasek, J. and Gagolewski, M. (2018). The efficacy of league formats in ranking teams.
  Statistical Modelling, 18(5-6):411–435.

Leiva Bertrán, F. (2025). Ranking in incomplete tournaments: The generalized win
  percentage method, efficiency, and NCAA football. Journal of Sports Economics,
  26(1):3–34.

Lenten, L. J. A. and Kendall, G. (2022). Scholarly sports: Influence of social science
  academe on sports rules and policy. Journal of the Operational Research Society,
  73(12):2591–2601.

Milvang, O. (2015). Probability for the outcome of a chess game based on rating. Manuscript.
 http://www.nordstrandsjakk.no/documents/spp/Probability.pdf.

Ólafsson, S. (1990). Weighted matching in chess tournaments. Journal of the Operational
   Research Society, 41(1):17–24.

Ryvkin, D. (2010). The selection efficiency of tournaments. European Journal of Operational
 Research, 206(3):667–675.



                                            13
Sauer, P., Cseh, Á., and Lenzner, P. (2024). Improving ranking quality and fairness in
  Swiss-system chess tournaments. Journal of Quantitative Analysis in Sports, 20(2):127–
  146.

Sziklai, B. R., Biró, P., and Csató, L. (2022). The efficacy of tournament designs. Computers
  & Operations Research, 144:105821.

Sziklai, B. R., Gere, A., Héberger, K., and Staudacher, J. (2025). rSRD: An R pack-
  age for the Sum of Ranking Differences statistical procedure. Manuscript. DOI:
  10.48550/arXiv.2502.03208.

West, C. (2018). Statistics for analysts who hate statistics, Part VII: Sum of Ranking
 Differences (SRD). LCGC North America, 36(12):882–885.




                                              14
