# Efficient Frontier Optimization of NBA Shot Selection Using Markov Reward Processes

- arXiv: https://arxiv.org/abs/2607.02933
- Published: 2026-07-03
- PDF: ../../library/preprints/arxiv/2026/2026 Efficient Frontier Optimization of NBA Shot Selection Using Markov Reward Processes - arXiv 2607.02933.pdf

## Abstract

This paper asks whether modern NBA shot selection can be evaluated as a dynamic portfolio problem rather than as a collection of isolated shot attempts. We combine a possession-level Markov reward process with both a mean-variance shot allocation objective and a defense response cost. The model separates rim attempts, midrange attempts, corner threes, and noncorner threes, then values each candidate shot diet by immediate scoring, continuation after offensive rebounds, empirical game-level variance, and a timeout-response stability cost. Because fastbreak value depends on geometry that is not fully observed in standard play-by-play, we optimize the no-fastbreak sample first and then add back observed fastbreak shot selection as a fixed transition component. Our results indicate that the league aggregate operates near the efficient frontier, with marginal improvements to be made by slightly decreasing perimeter volume and mid range attempts while increasing rim attempts. Team-level analyses reflect this general trend. Ultimately, these findings suggest the three-point revolution has pushed volume slightly past its optimal boundary. By incorporating outcome variance and continuation effects, we show that optimizing solely for expected value mathematically overstates the benefit of perimeter shots.

## Full text (pdftotext)

                                               Efficient Frontier Optimization of NBA Shot Selection Using
                                                                  Markov Reward Processes
                                                                        Nirek Duma               Leo Benaharon


                                                                                         Abstract
arXiv:2607.02933v1 [stat.AP] 3 Jul 2026




                                                   This paper asks whether modern NBA shot selection can be evaluated as a dynamic portfolio
                                               problem rather than as a collection of isolated shot attempts. We combine a possession-level
                                               Markov reward process with both a mean-variance shot allocation objective and a defense re-
                                               sponse cost. The model separates rim attempts, midrange attempts, corner threes, and non-
                                               corner threes, then values each candidate shot diet by immediate scoring, continuation after
                                               offensive rebounds, empirical game-level variance, and a timeout-response stability cost. Be-
                                               cause fastbreak value depends on geometry that is not fully observed in standard play-by-play,
                                               we optimize the no-fastbreak sample first and then add back observed fastbreak shot selection
                                               as a fixed transition component. Our results indicate that the league aggregate operates near
                                               the efficient frontier, with marginal improvements to be made by slightly decreasing perimeter
                                               volume and mid range attempts while increasing rim attempts. Team-level analyses reflect this
                                               general trend. Ultimately, these findings suggest the three-point revolution has pushed volume
                                               slightly past its optimal boundary. By incorporating outcome variance and continuation ef-
                                               fects, we show that optimizing solely for expected value mathematically overstates the benefit
                                               of perimeter shots.


                                          1    Introduction
                                          Over the past two decades, the NBA has greatly increased both pace and three-point attempt share.
                                          The league did not only change where shots came from; it changed the rhythm of the game. More
                                          possessions and more threes created the conditions for extreme scoring outbursts, including teams
                                          scoring over 150 points in regulation environments, but they also created a version of basketball
                                          that can become difficult to watch when variance turns the wrong way. The clearest example is
                                          the 2018 Houston Rockets missing 27 straight threes in Game 7 of the Western Conference Finals.
                                              In the modern NBA, we have seen offensive philosophies based on analytics use a common ex-
                                          pected value argument to justify their shot selection. Executives like Daryl Morey have built teams
                                          with offensive philosophies centered almost entirely on the rim and the arc, popularizing the term
                                          ’Moreyball.’ Mathematically, this seems sound, as rim attempts and threes yield higher expected
                                          returns than midrange attempts. The question is whether expected value alone is sufficient. A
                                          shot diet also carries continuation value, game-to-game variance, and defensive response pressure.
                                          These factors determine whether a high-value diet is actually stable.




                                                                                             1
Figure 1: League shot-diet share by season. The three-point line shows the macro shift toward
threes, while the rim and middle-two lines show how the rest of the shot diet moved around it.

   The basic expected-value argument is simple:
                                            E[Vz ] = pz rz ,
where pz is make probability and rz is the point value of shot category z. But expected value alone
is incomplete. Three-point shots can have strong expected value while still producing higher game-
to-game variance. Over the finite sample size of a single game or playoff series, a high-variance shot
profile exposes a team to downside risk and cold streaks. It also treats a miss as the same kind of
event across shot types. In reality, misses create different transition opportunities: some misses are
more likely to become offensive rebounds, free throws, or another shot before the possession ends.
     The abrupt shift in three-point shooting trends, alongside its current analytical justification,
motivates the central question of this paper. Have NBA teams reached a point where they shoot
too many threes? To investigate this, we develop an optimization model to benchmark empirical
shot diets against the league-wide efficient frontier. Furthermore, we apply this framework to team-
specific transition matrices. This allows us to generate customized shot portfolio recommendations
for each franchise while validating directional consistency across unique offensive environments.




Figure 2: Shot probability and shot value move differently by category. Rim attempts have the
strongest make-rate profile, while threes gain value from the extra point. This is why raw expected
value is necessary but not sufficient.


                                                   2
   This paper fills the gap between the micro and macro domains. We model the possession as
an absorbing Markov reward process, use the transient possession value as the return term in a
portfolio objective, and penalize both shot-return variance and timeout-response instability. The
shot portfolio is
                                     π = (πR , πM , πC3 , πN C3 ),
where R is rim attempts, M is midrange attempts, C3 is corner threes, and N C3 is non-corner
threes. The components satisfy

                             πR + πM + πC3 + πN C3 = 1,         πi ≥ 0.

    We do not claim that one universal shot chart is correct. We will attempt to generalize the
league-wide shot diets of the 3-point revolution and compare them to constructed efficient frontiers
where continuation, variance, and response sensitivity are all included.


2    Background and Gap
Initial advancements in the basketball analytics revolution focused on the ”micro” problem of
offensive efficiency. Frameworks ranging from Skinner’s optimal stopping models [3] to the Markov
Decision Processes of Sandholtz and Bornn [5] quantified the cascading probabilities of a single 24-
second possession. Consequently, offenses were re-engineered to generate high-value spatial states,
such as rim attempts and corner threes, by using dribble penetrations to force defensive rotational
dilemmas [6].
    The 3-point revolution led to a new ”macro” problem in basketball analytics. The macroscopic
shift in league shot diets toward perimeter volume raised a systemic question: Is there a mathe-
matical limit to this logic? Optimizing a full-game offensive architecture solely around expected
value dangerously ignores outcome volatility. Because three-point shots inherently possess a lower
raw make probability, relying exclusively on a high-variance perimeter profile exposes a team to
severe downside risk over a finite sample. As demonstrated by Fichman and O’Brien’s application
of Modern Portfolio Theory to basketball [2], elite offensive design requires balancing expected
points against portfolio variance. They predicted that the three-point revolution would reach its
equilibrium at about 38% of field-goal attempts [1]. However, that number was reached in 2019,
with the three-point attempt share since pushing further past their predicted equilibrium to 41.5%.
    Fichman and O’Brien treated shot diets as non-transient, not taking account for rebound contin-
uations. To refine their framework, we account for the sequential continuations of live possessions.
Therefore, a drive to the rim captures both its immediate expected value and the subsequent
opportunities it generates.
    Our model bridges the “micro” and “macro” domains by fusing the stochastic modeling of in-
dividual possessions with the macroscopic Modern Portfolio approach to optimize a comprehensive
offensive profile. By defining the half-court offense as an absorbing Markov Reward Process, we
calculate transient-state continuation values that inherently capture spatial transition probabili-
ties. We then integrate this transient expected value into a centralized objective function alongside
empirical shot variance and timeout-response penalties. Extracting the efficient frontier from this
model mathematically balances the generation of high-value shots against the mitigation of sys-
temic volatility. Ultimately, this dynamic portfolio framework allows us to mathematically evaluate
whether the NBA shoots ”too many” threes.
    The contribution is therefore specific: this paper combines a possession-level Markov reward
process with a shot-diet portfolio objective, separates corner threes from non-corner threes, and


                                                 3
compares full-sample results with a no-fastbreak sample. Fastbreaks are analyzed separately be-
cause their value depends on geometry, who gets back on defense, and how the offense fills lanes.
Standard play-by-play does not fully observe that information.


3     Data and State Space
The analysis uses cached NBA live play-by-play data from regular-season games in the 2021–22
through 2025–26 seasons. Each possession is mapped into the state space

                   S = {P S, RM, RX, M M, M X, C3M, C3X, N C3M, N C3X,
                         F T 1, F T 2, F T 3, ORR , ORM , ORC3 , ORN C3 , OR, EP }.

Here P S is possession start and EP is the absorbing end-of-possession state. Made and missed
shots are split by location and result. Offensive rebounds are also split by the type of missed shot
that created them.
   In the no-fastbreak sample, after removing any modeled possession containing a live fastbreak
qualifier, the diet was
                             R/M/C3/N C3 = 0.313/0.277/0.105/0.305.
The no-fastbreak run removed 129,695 modeled fastbreak possessions and 302,262 modeled events.
This is not a claim that fastbreaks are unimportant. It is the opposite: fastbreak value depends
heavily on geometry and player recovery, which are not fully captured in standard play-by-play.
   The observed full-sample league shot diet was

                              R/M/C3/N C3 = 0.345/0.252/0.103/0.301.


4     Model
4.1   Transition Matrix
Let P be the empirical transition matrix:

                                    Pij = Pr(Xt+1 = j | Xt = i).

The end state is absorbing:
                                            PEP,EP = 1.
For transient analysis, remove EP and write the remaining transient block as Q ≡ Qtrans . The
fundamental matrix is
                            N = (I − Q)−1 = I + Q + Q2 + Q3 + · · · .
The entry Nij is the expected number of visits to transient state j before the possession ends when
starting in state i.
    For a candidate shot diet π, the transition matrix becomes P (π). P (π) reallocates shot-outcome
mass in the possession-start and offensive-rebound rows across the four shot categories while pre-
serving empirical non-shot mass, free-throw mass, end-of-possession mass, and category make rates.
If pz is the make rate of category z and ω is the row’s field-goal outcome mass, then the simplified
row logic is
                  Pr(row → zM | π) = ωπz pz ,     Pr(row → zX | π) = ωπz (1 − pz ).



                                                  4
This is why π changes the shot mix without pretending that turnovers, fouls, and possession-ending
events disappear.
    Figures 3 and 4 show the empirical transition structure. The full matrix P includes the absorbing
EP state, so it shows where possessions terminate. The transient block Qtrans removes EP and
isolates the continuation process before possession end. The important rows for this paper are the
missed-shot rows, because they determine whether a miss is truly a dead possession or a continuation
opportunity.




Figure 3: No-fastbreak empirical transition matrices. The left panel is the full transition matrix P
and the right panel is the transient block Qtrans after removing the absorbing end-possession state.




Figure 4: Full-sample empirical transition matrices. Adding fastbreaks increases the possession-
start mass into rim outcomes, while the transient block still shows the same continuation channels
through missed shots, free throws, and offensive rebounds.

   The miss-to-offensive-rebound rows show that rim misses create the most continuation. In the

                                                 5
no-fastbreak sample,

                        Pr(ORR | RX ) = 0.384,          Pr(ORM | MX ) = 0.270,
                    Pr(ORC3 | C3X ) = 0.258, Pr(ORN C3 | N C3X ) = 0.260.

In the full sample the same ordering holds:

                        Pr(ORR | RX ) = 0.391,          Pr(ORM | MX ) = 0.271,
                    Pr(ORC3 | C3X ) = 0.262, Pr(ORN C3 | N C3X ) = 0.260.

So, in this model, missed rim attempts have the highest offensive-rebound continuation opportunity.
Corner-three and non-corner-three misses are nearly tied, and both are slightly below midrange
misses.




Figure 5: Offensive-rebound continuation probability conditional on a missed shot. Rim misses are
the strongest continuation source in both samples.


4.2   Rewards, One-Step Value, and Transient Value
The reward vector r attaches immediate points to entering states:

                       rRM = 2,     rM M = 2,         rC3M = 3,      rN C3M = 3.

Free-throw states receive their empirical expected free-throw contribution, and miss/end states
receive zero immediate reward.
    The one-step value is
                                       V1 (π) = eTP S Q(π)r.
This is the expected value of the next transition from possession start. It is useful because it is
close to the traditional first-shot expected-value view.
    The transient value is

                             VT (π) = eTP S (I − Q(π))−1 r = eTP S N (π)r.

                                                  6
This is the expected value of the possession before absorption into EP . It is the main value object
because it includes continuation after offensive rebounds, free throws, and possession survival.
Comparing V1 and VT shows exactly where continuation changes the ranking of shot diets.

4.3    Variance
Let gt be the game-level vector of shot-category returns:
                                                                points from category z in game t
          gt = [gt,R , gt,M , gt,C3 , gt,N C3 ]T ,   gt,z =                                       .
                                                               attempts from category z in game t
The covariance matrix is
                                                      T
                                                 1 X
                                        Σ=           (gt − ḡ)(gt − ḡ)T .
                                               T −1
                                                     t=1
For a candidate diet, portfolio variance is
                                                               XX
                                        σ 2 (π) = π T Σπ =             πi Σij πj .
                                                               i   j

We use covariance rather than independent category variance because shot families can co-move.
A high-rim game and a high-corner-three game may not be independent events; covariance is the
part of the model that lets diversification matter.

4.4    Timeout Response Cost
Timeout intervals are split on team-attributed full timeouts. Each interval has a pressure vector

                             st = [EPR , EPM , EPC3 , EPN C3 , EPOR , EPF T ]T .

The first four components are interval scoring pressure by shot family:

                                          EPz,t = sharez,t · FG%z,t · rz .

The remaining components are
                                free-throw points in interval t
                       EPF T,t =                                ,
                                            F GAt
                                points after first offensive rebound in interval t
                       EPOR,t =                                                    .
                                                       F GAt
   The response matrix is fit by ridge regression:

                              ∆st = Bst + ϵt ,        B̂ T = (X T X + αI)−1 X T Y,

where each row of X is the current interval pressure vector and each row of Y is the next-interval
change st+1 − st .
   For a candidate diet, the model builds

                        s(π) = [sR (π), sM (π), sC3 (π), sN C3 (π), sOR (π), sF T (π)]T ,

with
                                           sz (π) = Pr(P S → zM | π)rz ,

                                                           7
                                                                        X
        sOR (π) = max{VT (π) − V1 (π), 0},        sF T (π) =                           Pr(P S → k | π)rk .
                                                               k∈{F T 1,F T 2,F T 3}

The response cost is
                                            E(π) = ∥Bs(π)∥2 .
We include B because a shot diet can be efficient but structurally unstable. This term functions
as an implicit coaching adjustment cost, penalizing shot profiles that empirically trigger signifi-
cant post-timeout movement. Practically, if an offense generates an unsustainably high volume of
uncontested three-pointers, the opposing defense will use the timeout to structurally regress that
specific advantage back toward the mean.

4.5   Optimization and Frontier Selection
The final objective is
                                                   f2 (π) − λ2 E(π),
                                   max Ve (π) − λ1 σ           e
                                    π
subject to                                                X
                                        0 ≤ πi ≤ 1,           πi = 1.
                                                          i
Each term is normalized on the candidate portfolio support before entering the objective:
                                                 A(π) − Amin
                                          A(π)
                                          e    =             .
                                                 Amax − Amin
This keeps value, variance, and response cost on comparable scales. Without this normalization, the
largest numerical term can dominate the objective for a mechanical reason rather than a basketball
reason. A grid search across λ1 and λ2 is used to trace the frontier and identify the risk-return
region where the knee rule is applied. The league selected portfolios with the respective λ1 and λ2
are then solved with constrained SLSQP over the continuous simplex.
    The main knee rule in this paper is the dx/dy-tail rule. Let the upper efficient envelope be
ordered as
                                   (xm , ym ) = σ 2 (πm ), V (πm ) .
                                                                  

The rule computes the local tail slope
                                           dx     xm+1 − xm
                                                ≈
                                           dy m   ym+1 − ym

and selects the high-value frontier point where this quantity is smallest. Intuitively, this is the part
of the frontier where the curve has entered its nearly vertical tail: more risk is being added faster
than useful value. We use it as the main rule because it is conservative and matches the question
of risk-controlled shot allocation.

4.6   Team-Level Matrices
League optimization is a benchmark, but team-specific optimization needs team-level transition
matrices. For the main team figures, we estimate each team’s transition matrix directly from
its observed transition counts. The five-season sample gives each team a reasonable number of
modeled transitions, including more than 60,000 no-fastbreak training transitions for every team,
so the main analysis does not need an added smoothing term. This keeps the team-specific results
tied to each team’s own observed possession structure.

                                                      8
4.7   Hybrid Fastbreak Recomposition
The main optimizer excludes fastbreak possessions because their value depends on geometry that
standard play-by-play does not observe. To still express a full-game recommendation, we add
fastbreaks back as an observed fixed component rather than optimizing them. Let N F B be the
number of modeled fastbreak possessions and N All be the total number of modeled possessions.
The fastbreak weight is
                                               NFB
                                          α = All .
                                               N
   For shot category z, let AFz B be attempts from that category inside the removed fastbreak
possessions only. The observed fastbreak shot distribution is

                                                   AF B
                                        ρFz B,L = P z F B ,
                                                   j Aj

The hybrid recommendation uses the no-fastbreak optimum and fastbreak distribution:

                                 πzHybrid = (1 − α)πzN F ∗ + αρFz B .

In the data, the league fastbreak-possession probability is αL = 0.105. The league fastbreak shot
distribution is
                            R/M/C3/N C3 = 0.571/0.070/0.090/0.269.
This is why adding the observed fastbreak component raises rim share and lowers midrange share
relative to the no-fastbreak optimum.


5     Results
5.1   Response Cost
Using timeout-separated pressure intervals, the response cost matrix B can be seen in Figure 6.
This response cost takes into account the ability for the defense to quickly adapt to the shooting
style of the opposing team. To figure out what type of offense minimizes ∥Bs(π)∥2 we want to find
a π where:

                                       ∥Bs(π) − s(π)∥2 ≈ 0
In Table 1, it can be seen that the π that minimizes ∥Bs(π)∥2 is approximately the actual league
shooting distribution. This means that the response cost yields approximately the same minimum
as a standard L2 penalty, an expected result given its derivation from aggregated empirical data.
However, matrix B ensures that our penalty behaves asymmetrically, accurately capturing the
cross-correlated cost of different spatial adjustments.




                                                  9
Figure 6: Estimated timeout response matrix B for the six pressure components. Negative diagonal
entries indicate mean reversion within the same pressure channel, while off-diagonal entries show
how one pressure source is associated with movement in another.


 Table 1: Response-cost-minimizing shot diet compared with the full-sample actual league diet.

                       Diet                           Rim         Mid       C3     NC3
                       Full actual                    0.345      0.252    0.103    0.301
                       Minimum response cost          0.342      0.253    0.108    0.297


5.2   League-Level Shot Diets
Table 2 reports the no-fastbreak league results under the normalized w-tail objective and the hybrid
full-game recomposition. It can be seen that λ1 and λ2 are similar across the one-step and transient
models.

                     Table 2: League optima under dx/dy-tail frontier selection.

            Sample            Model       λ1    λ2         Rim      Mid       C3     NC3    Value
            No fastbreak      One-step    5.8   0.7    0.404      0.230    0.100    0.266   0.945
            No fastbreak      Transient   5.7   0.7    0.415      0.233    0.095    0.257   1.099
            Full Sample       Transient   5.7   0.7    0.431      0.216    0.095    0.258       –



                                                      10
    Fastbreaks are valuable but structurally different from half-court possessions. Their expected
value depends on where players are on the floor, how many defenders get back, and how quickly
the offense fills lanes. The standard play-by-play API contains a fastbreak qualifier, but it does not
contain the full geometry. For this reason, the no-fastbreak version removes any modeled possession
containing a fastbreak-tagged event.
    The no-fastbreak actual diet has fewer rim attempts and more midrange attempts than the full
sample. Table 3 separates the half-court-heavy possessions from the removed fastbreak possessions.

                      Table 3: Actual league shot diets by possession sample.

                         Sample                 Rim      Mid       C3      NC3
                         No fastbreak actual   0.313    0.277    0.105    0.305
                         Fastbreak actual      0.571    0.070    0.090    0.269
                         Full sample actual    0.345    0.252    0.103    0.301

    Figure 7 and 8 show each teams actual shot diet compared to the league actual and optimum
respectfully. The no-fastbreak transient optimum moves meaningfully toward rim pressure while
staying diversified:

      Table 4: No-fastbreak actual diet compared with the no-fastbreak transient optimum.

                  Diet                                 Rim       Mid       C3     NC3
                  No fastbreak actual                  0.313    0.277    0.105    0.305
                  No fastbreak transient optimum       0.415    0.233    0.095    0.257

   The recommendation is more rim pressure and fewer non-corner threes than the observed diet,
but it is not a pure rim-and-three profile.




      Figure 7: No-fastbreak team diets compared with the no-fastbreak league actual diet.




                                                 11
   Figure 8: No-fastbreak team diets compared with the no-fastbreak league transient frontier.

   The hybrid full-game benchmark uses the no-fastbreak transient optimum for half-court-like
possessions and the observed fastbreak shot distribution for transition possessions:

           Table 5: Hybrid actual diet compared with the Hybrid transient optimum.

                    Diet                             Rim    Mid      C3    NC3
                    Hybrid actual                 0.340    0.255   0.103   0.301
                    Hybrid transient optimum      0.431    0.216   0.095   0.258

    This is directionally consistent with transition offense creating easier rim chances. The result
remains similar because only the non-fastbreak component is optimized; the fastbreak component
is held to the actual removed fastbreak shot distribution.




Figure 9: Full actual team diets compared with the hybrid league benchmark. The right-hand bar
is (1 − αL ) times the no-fastbreak league transient optimum plus αL times the league fastbreak
shot distribution.

    As a calibration check, Figure 10 shows the full-sample league transient frontier when fastbreak
and non-fastbreak possessions are pooled. The selected full-sample model value is 1.149 points per
possession (PPP), close to the empirical league PPP of about 1.15, so the Markov reward scale is
aligned with observed scoring.




                                                12
Figure 10: Actual teams plotted on the full-sample league transient frontier. The dx/dy-tail point
is the selected league frontier portfolio when all possessions, including fastbreaks, are optimized
together.

    In Figure 11, we see that the empirical shot diets of all NBA franchises live in close proximity
to the league-wide efficient frontier. This indicates that modern offensive distributions are already
highly optimized within our framework. In Figure 10, see that marginal improvements can be made
by slightly reducing their three-point and midrange attempt shares while proportionally increasing
rim volume.

5.3   Team-Specific Frontiers
In this section, we examine what the model recommends under teams’ own statistical environments.
Teams differ in shot efficiency, offensive rebounding paths, covariance structure, and transition
tendencies. The team-specific results support the main conceptual point: there is not one universal
shot diet.
    For the team-specific comparison figures, the selected team points use each team’s empirical
transition matrix. The resulting target distributions exhibit the identical structural trends observed
along the macro league-wide frontier. As illustrated in Figures 11 and 12, our model suggests that
the majority of teams should shoot more rim shots, a similar amount of corner threes, and fewer
non-corner threes and midrange shots.




                                                 13
Figure 11: No-fastbreak team shot diets compared with team-specific transient frontier portfolios.




Figure 12: Full actual team diets compared with team-specific hybrid benchmarks. The right-hand
bar uses each team’s own no-fastbreak optimum, fastbreak-possession probability, and observed
fastbreak shot distribution.

    We observe that Washington’s optimum represents an extreme anomaly, suggesting a portfolio
composed almost entirely of rim attempts. To address this, we detail an empirical shrinkage
approach in the appendix. While shrinkage successfully corrected Washington’s benchmark and
maintained stability across the majority of the league, it simultaneously introduced severe volatility
into Denver’s optimum. We hypothesize that this divergence highlights a fundamental limitation
of the shrinkage estimator: it correctly regresses Washington’s small-sample noise to the mean but
inappropriately penalizes Denver’s statistically extreme, yet highly efficient, structural reality.


6    Discussion
The main conclusion is that the three-point revolution should not be evaluated as a slogan. The
overarching problem is not whether a three-point attempt is inherently worth more than a two-
point jump shot. Rather, the question is what specific shot portfolio maximizes transient possession
value while simultaneously controlling for outcome volatility and strategic instability. Under our
model, NBA offenses are already operating very close to the efficient frontier, leaving only marginal
gains to be extracted. Specifically, the model’s directional optimum supports a slight reduction in
perimeter and midrange volume in favor of a corresponding increase in rim attempts.
    The no-fastbreak results are important because they keep the model honest. Transition offense
is generated by spacing, live-ball turnovers, rebound outlets, player speed, and defensive recov-
ery. Without tracking data, we cannot fully observe those geometric inputs. Removing fastbreak
possessions therefore gives a cleaner view of half-court shot allocation.


                                                 14
    Our results demonstrate that a single, universally optimal shot diet does not exist, as teams
have unique suggestions based on their statistical landscapes. However, the mathematical diver-
gence between these team-specific optimums is generally narrower than the stark stylistic contrasts
observed in the contemporary NBA. For instance, the Denver Nuggets and Boston Celtics main-
tain historically elite offensive efficiencies despite utilizing opposite perimeter-volume philosophies.
This indicates that while the underlying statistical landscape defines the structural boundaries
of a team’s efficiency, unique personnel constraints and overarching coaching philosophy dictate
its ultimate behavioral extreme. While our dx/dy stopping condition identifies a mathematical
equilibrium between risk and reward, individual franchises may weigh risk and reward differently
based on their personnel. A system built around high-volume perimeter creation and one built
around interior pressure can both be mathematically coherent. This does not mean all shot diets
are created equal; it proves that true offensive optimality is conditional on both a team’s statistical
ecosystem and its unique personnel and offensive philosophy.


7    Limitations and Future Work
The model holds the empirical make percentage constant when shot shares change. We deliberately
do this to avoid overfitting. A simple regression of shot attempts on shooting percentage would
be flawed because attempts are not randomly assigned: a team may shoot more from a category
because it is hot that day, because the defense is conceding that shot, or because personnel created
unusually good looks. Further work with optical tracking data is required to estimate how efficiency
changes when shot frequency changes.
     The framework functions most effectively as a macro-level prescription rather than a granular
optimization tool for individual franchises. On a localized, team-specific level, the model lacks criti-
cal personnel identification. We do not explicitly quantify the offensive gravity of distinct superstars,
specific lineup spacing, matchup pressure, or individual shot-maker identities. Because the model
smooths over these localized variables, the team-specific frontiers it generates naturally mirror the
macro league optimum. Therefore, while our overarching directional recommendation—increasing
rim pressure while reducing midrange and perimeter volume—serves as a highly robust baseline for
the average franchise, it should not be viewed as an absolute mandate. In reality, a team’s true
efficient frontier would dynamically shift based on its specific personnel advantages, meaning this
macro directional trend may not hold true for every individual roster.
     Fastbreaks are another limitation. We exclude them in the main no-fastbreak analysis because
transition offense depends on geometry: who gets back, who fills lanes, where the ball is, and how
the defense is matched. A stronger model would estimate fastbreak creation and fastbreak shot
diet as explicit optimizable terms rather than treating transition possessions separately.
     Finally, we do not explicitly model defense. The timeout response matrix is only an implicit
way to measure adaptability after pressure states. Proper defensive modeling would require more
advanced data: exact coverage responses, help positioning, matchup changes, substitutions, and
personnel-specific defensive choices.
     While this framework identifies the macro-level efficient frontier for expected possession value,
future research should map these portfolios directly to expected win probability. The central
question for subsequent models is whether shifting the objective function from expected points
to expected wins naturally bridges the slight gap between our theoretical optimum and observed
league averages. By optimizing the league-wide shot diet against game-state simulators, future work
can definitively determine if the modern NBA’s current, high-variance empirical shot distribution
is actually the mathematical requirement for win maximization.


                                                   15
A     Full-Sample Frontier Figures
The main text uses the no-fastbreak optimizer plus observed fastbreak recomposition. For compar-
ison, the original full-sample SLSQP figures are shown here. These figures optimize directly on the
full sample, so fastbreak and non-fastbreak possessions are pooled in a single transition matrix.




Figure 13: Actual teams plotted on the full-sample league one-step frontier. The one-step model
shows the first-transition value surface before full continuation is included.

    Figures 14 and 15 are therefore different from the hybrid figures in the main text. They do not
keep fastbreaks fixed as an observed component; they optimize over the entire possession sample,
including fastbreak possessions.




Figure 14: Full-sample team shot diets compared with the league transient frontier portfolio selected
by dx/dy tail. This is a full-sample optimization over all possessions, so fastbreaks are not held
fixed.



                                                 16
Figure 15: Full-sample team shot diets compared with team-specific transient frontier portfolios.
This is also a full-sample optimization over all possessions, not the hybrid fixed-fastbreak recom-
position.


B     Transition-Matrix Shrinkage Sensitivity
The main team figures use empirical team transition matrices. As a robustness check, we also
compared those team matrices with an empirical-Bayes version that shrinks each team row toward
the league transition matrix. For team a, the smoothed transition probability is
                                                  (a)
                                         (a,K)   nij + KPijleague
                                       Pij     =      (a)
                                                                  ,
                                                    Ni + K
          (a)                                                                             (a)       P  (a)
where nij is the team’s observed transition count from state i to state j, Ni                   =   j nij is the
team’s row total, and Pijleague is the league transition probability. The empirical matrix is the
special case K = 0:
                                                      (a)
                                             (a,0)  nij
                                           Pij     = (a) .
                                                    Ni
    The motivation for the smoothed version is row-level stability. Total team transition counts are
large, but some specific rows are still uncommon after splitting by shot family, result, offensive-
rebound source, and fastbreak status. A positive K acts like league pseudo-counts in those sparse
rows. We used K = 1000 as the comparison value because it was the largest candidate in the
validation grid and had the lowest validation mean-squared error in the no-fastbreak transition
validation. It is also small relative to each team’s total five-season transition count, so it is a
stability check rather than a replacement of team identity.

                        Table 6: K=0 versus K=1000 team-frontier comparison.

 Sample                 Teams   Same diets   Mean L1 diet dist.   Max L1 diet dist.   Mean |∆V |    Max |∆ gap|
 Hybrid recomposition      30           0               0.0525              0.8575        0.0080         0.1342
 No fastbreak              30           0               0.0587              0.9545        0.0080         0.1342


    Both the hybrid and no-fastbreak comparisons are usually close, but each has at least one team-
level result that is sensitive to smoothing. The hybrid comparison keeps observed fastbreak shot
selection fixed and changes only the no-fastbreak team frontier from K = 0 to K = 1000. This is
why the main text uses the empirical team matrices and keeps the shrinkage version as a sensitivity
check rather than as the main team result.

                                                      17
Figure 16: Full actual team diets compared with hybrid recompositions using the no-fastbreak
K = 0 and K = 1000 team-frontier diets. Fastbreak shot selection is held fixed from observed
removed fastbreak possessions.




      Figure 17: Hybrid team-frontier diets compared directly under K = 0 and K = 1000.




Figure 18: No-fastbreak team actual diets compared with empirical team-frontier diets and K =
1000 team-frontier diets.




                                             18
Figure 19: No-fastbreak empirical team-frontier diets compared directly with K = 1000 team-
frontier diets.




Figure 20: No-fastbreak frontier value gaps under empirical and K = 1000 team transition matrices.


References
[1] Fichman, M. and O’Brien, J. R. (2019). Optimal shot selection strategies for the NBA. Journal
    of Quantitative Analysis in Sports, 15(3), 203–211. doi:10.1515/jqas-2017-0113.
[2] Fichman, M. and O’Brien, J. (2018). Three point shooting and efficient mixed strategies: A

                                               19
   portfolio management approach. Journal of Sports Analytics, 4, 107–120. doi:10.3233/JSA-
   160154.

[3] Skinner, B. (2011). The problem of shot selection in basketball. Journal of Quantitative Analysis
    in Sports.

[4] Cervone, D., D’Amour, A., Bornn, L., and Goldsberry, K. (2016). A multiresolution stochastic
    process model for predicting basketball possession outcomes. Journal of the American Statistical
    Association.

[5] Sandholtz, N. and Bornn, L. (2020). Markov decision processes with dynamic transition prob-
    abilities: an analysis of shooting strategies in basketball. Annals of Applied Statistics.

[6] Pelechrinis, K. and Goldsberry, K. (2021). The anatomy of corner 3s in the NBA: What makes
    them efficient, how are they generated and how can defenses respond? arXiv:2105.12785.




                                                 20

