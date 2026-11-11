<!-- source: library/preprints/arXiv/2026/2026 - Modeling the Joint Distribution of Box Score Statistics A Gaussian Copula Approach - Watts.pdf -->
<!-- item: https://arxiv.org/abs/2611.10152 -->
<!-- authors: Kenny Watts -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-11; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Modeling the Joint Distribution of Box Score Statistics: A Gaussian Copula Approach

                                                   Modeling the Joint Distribution of Box Score Statistics:
                                                               A Gaussian Copula Approach
                                                                                       Kenny Watts
                                                                                   University of Virginia
                                                                                   xen5ek@virginia.edu
arXiv:2611.10152v1 [stat.AP] 6 Nov 2026




                                                                                        November 2026


                                                                                            Abstract
                                                    What is the probability that LeBron James records at least 27 points, 7 rebounds, and 7
                                                assists tonight? While an interesting statistical question by itself, the rise of sports betting and
                                                multi-leg parlays has made answering this question increasingly relevant. However, coming up
                                                with an estimated likelihood is tricky, since box score statistics aren’t independent.
                                                We estimate the joint probability that a player reaches a combination of thresholds in points,
                                                assists, and rebounds using a Gaussian copula, fit separately for each player using only their
                                                previous games. We compare it with two benchmarks: the product of the empirical marginal
                                                probabilities (i.e. assuming independence) and the empirical frequency of the joint event. Across
                                                ∼ 22, 000 player-observations, the Gaussian copula performs on par or better than either bench-
                                                mark at lower threshold levels, with large gains at high joint exceedance levels. Because it is
                                                generative, the model also allows for probabilistic calculations for combinations that a player
                                                has rarely or never produced.


                                          1    Introduction
                                          Same-game parlays allow bettors to combine several outcomes from a single game into one wager.
                                          In basketball these legs often involve player box score statistics; for example, a bettor may wager
                                          that a player records at least 20 points, 5 rebounds, and 5 assists. There is evidence that these
                                          multi-leg parlays are far more profitable for sports books (Whelan, 2026), likely due to the difficulty
                                          in estimating the probability of the joint event and the multiplicative way that sports books set
                                          their parlay odds (every line has a built in vig, so combining multiple bets multiplies the house’s
                                          take).
                                              Treating the three box score statistics as independent is a poor approximation: a player who
                                          scored a large number of points likely spent more time on the court, accumulating opportunities
                                          to record rebounds and assists. Modeling these joint probabilities therefore requires a framework
                                          that accounts for inter-variable dependencies, rather than treating each metric in isolation. Figure
                                          1 shows that our three box score statistics exhibit mild but positive correlation.




                                                                                                 1
                 Figure 1: Within player correlation between Box Score Statistics

     Copulas provide a natural framework for this problem, since they separate each variable’s
marginal distribution from the dependence structure that links them (Sklar, 1959). Once the
marginals and the copula are estimated, we can simulate from the fitted joint distribution and
estimate the probability of any combination of variable thresholds, including combinations with
little or no historical support. Gaussian copulas were popularized in finance for modeling default
correlation (Li, 2000), and copula methods have been applied to basketball data before; D’Urso
et al. (2023) used a copula-based Bayesian network to study the determinants of player perfor-
mance, and Liu and Yu (2026) used a copula-based Dirichlet process mixture to find subgroups of
similar players. Our objective is to model the joint distribution of points, rebounds, and assists at
the individual player level.

    In this paper, we model this joint distribution using a Gaussian copula, fitting the model in a
strictly out-of-sample setting by re-estimating it before every game. We evaluate joint exceedance
forecasts across 27 combinations of player-relative thresholds with Log Loss as our loss function,
comparing the Gaussian copula against independence and empirical-frequency benchmarks. The
results show that the benefits of modeling dependence are concentrated in combinations where all
three thresholds are high. The model uses only a player’s own game history and does not account
for opponents, minutes, or pace. It therefore provides a baseline for assessing the predictive value
of dependence modeling rather than a complete model pipeline.


2    Gaussian Copulas
A copula is a multivariate distribution function on the unit hypercube [0, 1]d whose univariate mar-
gins are uniform. Sklar’s theorem (Sklar, 1959) states that for any d-dimensional joint distribution
function F with marginals F1 , . . . , Fd , there exists a copula C such that
                                                                                  
                               F (x1 , . . . , xd ) = C F1 (x1 ), . . . , Fd (xd ) ,             (1)


                                                 2
and C is unique when the margins are continuous. The marginals describe each variable by itself,
and the copula carries the information about their joint behavior, meaning the two can be specified
and estimated separately. When the margins are discrete, as with box score counts, C is not unique;
we return to this in Section 4.
   Let Φ denote the standard normal distribution function and Φ−1 its quantile function. The
Gaussian copula is the dependence structure of a multivariate normal distribution,

                           CR (u1 , . . . , ud ) = ΦR Φ−1 (u1 ), . . . , Φ−1 (ud ) ,
                                                                                  
                                                                                                (2)

where ΦR is the d-variate standard normal distribution function with correlation matrix R. The
correlation matrix fully determines the dependence. The Gaussian copula captures dependence
through a single correlation matrix, allowing each pair of statistics its own strength of association
while retaining flexibility in the marginals.


3    Estimation
For each player we model X = (Xpts , Xreb , Xast ) with a Gaussian copula and empirical marginals.
To mimic a genuine forecasting setting, the model is re-estimated before every game using only
past games: for game t ≥ 21, the training set consists of the n = t − 1 preceding games x1 , . . . , xn .

Marginals. For j ∈ {pts, reb, ast}, the marginal F̂j is the empirical distribution function of the
player’s training games, with quantile function Q̂j = F̂j−1 given by the linearly interpolated sample
quantile.

Dependence. Each observation is mapped to the unit interval through its rank-based pseudo-
observation and then to the normal scale,
                                      rsj
                            ûsj =        ,     zsj = Φ−1 (ûsj ),       s = 1, . . . , n,                     (3)
                                     n+1
where rsj is the rank of xsj among the training games, with average ranks for ties. The copula’s
correlation matrix R̂ is estimated as the sample correlation matrix of the normal scores zs =
(zs,pts , zs,reb , zs,ast ). We use the ‘nearPD‘ procedure from the R package ‘Matrix‘ (Bates et al.,
2026) to obtain the nearest positive definite correlation matrix, enforcing a unit diagonal. The
fitted joint distribution is

                 F̂ (xpts , xreb , xast ) = ΦR̂ Φ−1 (F̂pts (xpts )), Φ−1 (F̂reb (xreb )), Φ−1 (F̂ast (xast )) .
                                                                                                             
                                                                                                                (4)

Simulation.      We estimate joint exceedance probabilities by Monte Carlo. For b = 1, . . . , B we
draw
                                                  (b)        (b)         (b)           (b) 
                         z(b) ∼ N (0, R̂),      uj = Φ zj            ,   xj = Q̂j uj            ,              (5)

giving simulated games x(b) with the player’s own marginals and the estimated dependence. We
use B = 5,000. Fitting and simulation used the copula package in R (Jun Yan, 2007).




                                                        3
4     Evaluation Design
4.1   Thresholds and events
For each player-game, we use the player’s training games (at least 20) to set player-specific thresh-
olds. For quartile levels α = (αpts , αreb , αast ) with each αj ∈ {0.25, 0.50, 0.75}, giving 33 = 27
combinations, the thresholds are τj = Q̂j (αj ) and the event of interest is

                            Aα = {Xpts ≥ τpts , Xreb ≥ τreb , Xast ≥ τast }.                         (6)

For example, the combination (PTS Q50, REB Q25, AST Q75) is the event that the player scores
at least his historical median in points, at least his 25th percentile in rebounds, and at least his 75th
percentile in assists. Because thresholds are computed from each player’s own history, a “high”
threshold is relative to that player and the events are comparable across players with different
statistical profiles. Thresholds are updated along with the model before every game. We score each
forecast against the realized outcome yt = 1{xt ∈ Aα }, where xt is the stat line of the game being
predicted, resulting in 27 binary outcomes for each player every game.
    Although the Gaussian copula can theoretically estimate the likelihood of any combination
of thresholds, we limit our analysis to quartiles (Q25, Q50, Q75) to limit the complexity of the
prediction space and retain explanatory clarity.
    Points, rebounds, and assists are integer-valued, so their marginal distributions are discrete with
frequent ties. Two consequences follow. First, the copula is not unique, so F̂ is one of many joint
distributions consistent with the marginals. Second, because the event uses ≥ and the thresholds
are interpolated quantiles, Pr(Xj ≥ τj ) can differ from 1−αj , typically being larger. Thresholds are
not rounded to the nearest integer; exceedance events are evaluated directly using the interpolated
thresholds. We use the same threshold definition for the copula and both benchmarks, ensuring a
like-for-like comparison.

4.2   Forecasts and benchmarks
The copula forecast of Pr(Aα ) is the Monte Carlo estimate
                                                    B
                                                  1 X  (b)
                                     p̂cop =          1 x ∈ Aα .                                     (7)
                                                  B
                                                    b=1

The empirical benchmark is the frequency of the event in the n training games,
                                                     n
                                           emp     1X 
                                      p̂         =     1 xs ∈ Aα .                                   (8)
                                                   n
                                                    s=1

The independence benchmark multiplies the empirical marginal exceedance frequencies,
                                      3
                                        " n                #
                               ind
                                     Y    1X 
                             p̂ =              1 xsj ≥ τj .                                          (9)
                                          n
                                             j=1     s=1

This captures the marginal distributions but assumes independence.




                                                          4
4.3   Loss and inference
Forecasts are scored with log loss:
                                                                     
                              ℓ(p, y) = − y log p + (1 − y) log(1 − p) ,                          (10)

With sample sizes as small as 20, the empirical joint exceedance probability can be exactly zero.
We therefore clip p to [10−6 , 1 − 10−6 ] so that forecasts of exactly zero or one have finite loss.

4.4   Data
We sampled one NBA starter from each team in the first game of each two season window, selecting
players who appeared in that game and had at least 20 total games across the two season win-
dow. All player-game observations were restricted to games in which the player recorded non-zero
minutes. Players were then followed across the two consecutive seasons, with forecasts estimated
before each game. Players who were traded or missed games due to injury remained in the sample,
provided they met the initial eligibility criteria. We used seven windows, each covering two con-
secutive seasons, and avoiding the 2020 COVID season. The windows include 2010–11, 2012–13,
2014–15, 2016–17, 2018–19, 2023–24, and 2025–26. This yielded 207 players and approximately
22,000 player-game binary outcomes.


5     Results
Figure 2 and 3 compare the copula with each benchmark on the same player-games. For each
threshold combination, it shows the relative improvement, 1 − ℓGaussian /ℓcomparison . Because both
models forecast the same events, this is a paired comparison: player-games that are hard to forecast
are hard for both models, and this shared difficulty largely cancels in the ratio. Confidence intervals
come from a cluster bootstrap that resamples player-runs and recomputes both losses on each
resampled set, so they respect dependence among games from the same player.




Figure 2: Relative log loss improvement of the Gaussian copula over the independence benchmark
by threshold combination. Points show estimates and bars show confidence intervals.



                                                  5
    We observe clear separation between the Gaussian copula and the independence model with
all but two thresholds showing statistically significant improvements. For thresholds with multiple
Q75s we see between 2% − 8% decreases in log loss, showing that the Gaussian copula is better at
capturing the correlations at the upper quartiles.




Figure 3: Relative log loss improvement of the Gaussian copula over the empirical benchmark by
threshold combination. Points show estimates and bars show confidence intervals.

    The log loss looks very similar for the Gaussian copula and empirical model for many of the
lower thresholds. Only at the upper thresholds do we see the Gaussian copula performing signif-
icantly better. We attach in the Appendix 8 examples of Log Loss for more extreme thresholds
which show even greater out performance.

   For some context of the magnitude of Log Loss in Table 1 we show the average Log Loss across
example thresholds.

              Table 1: Average Log Loss Across Selected Threshold Combinations

                     Thresholds        Gaussian        Empirical   Independence
                     Q25, Q25, Q25         0.658           0.659          0.660
                     Q50, Q50, Q50         0.571           0.573          0.585
                     Q75, Q75, Q75         0.245           0.266          0.264




                                                   6
5.1   Calibration




                         Figure 4: Calibration Plot for All Three Models

We observe that the empirical and Gaussian models are well calibrated, while the model assuming
marginal independence systematically under predicts the probabilities of joint exceedance.

5.2   Relative Density Plots
Figure 5a shows the ratio of the copula’s joint exceedance probability to the independence bench-
mark, fixing assists at the Q75 threshold and varying the points and rebounds quartile levels.
Figure 5b is the same graph but with assists fixed at Q25. We see in both cases the ratio of the
probabilities rising as the quartile level increases, with a more extreme increase when assists are
conditioned at Q75.




(a) Independence benchmark comparison - Assists       (b) Independence benchmark comparison - Assists
at Q75                                                at Q25

Figure 5: Ratio of the Gaussian copula’s joint exceedance probability relative to the independence
benchmark.


                                                  7
    Although the Gaussian distribution places relatively little probability mass in its tails, we
observe that this does not prevent the Gaussian copula from capturing dependence at high quantiles.
The copula separates the dependence structure from the marginal distributions, which in our case
are empirical and therefore retain the observed tail behavior of each statistic.


6    Conclusion
A Gaussian copula performs on par or better than the empirical joint frequency model at lower
threshold levels, while demonstrating clear out performance over both the independence benchmark
and the empirical model at higher quartiles. The result is a simple, a fully generative model that
can be used to calculate threshold probabilities of both observed and previously unobserved stat
lines. It represents a baseline that future models could extend with richer pre-game context.


7    Discussion and Future Directions
The results support modeling dependence: gains over independence are consistent across all 27
combinations, and gains over the empirical estimate are largest where joint events are rare and
the empirical frequency is noisiest. Several limitations remain. The Gaussian copula imposes
a symmetric dependence structure and exhibits zero asymptotic tail dependence. We explored
alternative dependence specifications, including the Gumbel copula, as well as approaches that did
not impose a parametric joint distribution and allowed the dependence structure to vary across
players. We didn’t find any clear improvement in predictive performance, so we retained the
Gaussian copula as our primary model specification.
    Applications using Gaussian copulas such as (Li, 2000) have been criticized for their lack of
sensitivity to rare events and tail risk. However, this isn’t particularly relevant in this situation
since we’re predicting binary outcomes, i.e. there aren’t extreme asymmetric gains/losses to an
incorrect prediction of an outlier.
    Our model uses only a player’s own history, so it ignores ex ante knowledge of opponents,
minutes, and pace. We suspect that conditioning on pre-game predicted possessions would improve
the joint estimates, since playing time is the main driver of the dependence we model. Finally, we
evaluate player-relative quartile thresholds rather than the absolute lines offered by sports books,
so we have not tested out performance against market implied odds.


8    Appendix
All code and plots are accessible on GitHub.




                                                 8
We attach graphs of relative Log Loss improvement for more extreme thresholds.




      (a) Gaussian vs Independence                      (b) Gaussian vs Empirical

              Figure 6: Relative Log Loss Improvement at High Thresholds




                                           9
   Table 2 and 3 show the mean paired differences between the Gaussian copula and alternative
method, alongside bootstrapped p-values.

                         Table 2: Independence vs. Gaussian Copula

                Combo                               Mean Difference     pboot
                PTS Q75 — REB Q75 — AST Q75                  0.01860   0.0001
                PTS Q75 — REB Q50 — AST Q75                  0.01670   0.0001
                PTS Q75 — REB Q75 — AST Q50                  0.01660   0.0001
                PTS Q50 — REB Q50 — AST Q75                  0.01650   0.0001
                PTS Q50 — REB Q75 — AST Q75                  0.01580   0.0001
                PTS Q50 — REB Q50 — AST Q50                  0.01450   0.0001
                PTS Q50 — REB Q75 — AST Q50                  0.01350   0.0001
                PTS Q75 — REB Q50 — AST Q50                  0.01350   0.0001
                PTS Q75 — REB Q75 — AST Q25                  0.01230   0.0001
                PTS Q50 — REB Q25 — AST Q75                  0.01020   0.0001
                PTS Q75 — REB Q25 — AST Q75                  0.01000   0.0001
                PTS Q25 — REB Q50 — AST Q75                  0.00977   0.0001
                PTS Q50 — REB Q50 — AST Q25                  0.00906   0.0001
                PTS Q25 — REB Q75 — AST Q75                  0.00893   0.0001
                PTS Q25 — REB Q50 — AST Q50                  0.00852   0.0001
                PTS Q75 — REB Q50 — AST Q25                  0.00847   0.0001
                PTS Q50 — REB Q75 — AST Q25                  0.00835   0.0001
                PTS Q50 — REB Q25 — AST Q50                  0.00798   0.0001
                PTS Q25 — REB Q75 — AST Q50                  0.00651   0.0001
                PTS Q75 — REB Q25 — AST Q50                  0.00639   0.0001
                PTS Q25 — REB Q25 — AST Q75                  0.00545   0.0001
                PTS Q25 — REB Q25 — AST Q50                  0.00509   0.0012
                PTS Q25 — REB Q50 — AST Q25                  0.00403   0.0032
                PTS Q50 — REB Q25 — AST Q25                  0.00345   0.0104
                PTS Q25 — REB Q75 — AST Q25                  0.00225   0.0248
                PTS Q25 — REB Q25 — AST Q25                  0.00217   0.0734
                PTS Q75 — REB Q25 — AST Q25                  0.00195   0.0480




                                             10
                            Table 3: Empirical vs. Gaussian Copula

                 Combo                                 Mean Difference     pboot
                 PTS Q75 — REB Q75 — AST Q75                   0.02100   0.0001
                 PTS Q75 — REB Q75 — AST Q50                   0.00989   0.0001
                 PTS Q75 — REB Q50 — AST Q75                   0.00872   0.0001
                 PTS Q50 — REB Q75 — AST Q75                   0.00839   0.0001
                 PTS Q25 — REB Q75 — AST Q75                   0.00371   0.0038
                 PTS Q75 — REB Q75 — AST Q25                   0.00298   0.0124
                 PTS Q75 — REB Q50 — AST Q50                   0.00253   0.0150
                 PTS Q50 — REB Q50 — AST Q75                   0.00202   0.1090
                 PTS Q50 — REB Q50 — AST Q50                   0.00196   0.0150
                 PTS Q25 — REB Q50 — AST Q50                   0.00194   0.0028
                 PTS Q75 — REB Q25 — AST Q75                   0.00187   0.1240
                 PTS Q50 — REB Q75 — AST Q50                   0.00184   0.0422
                 PTS Q25 — REB Q25 — AST Q50                   0.00178   0.0042
                 PTS Q50 — REB Q25 — AST Q50                   0.00174   0.0064
                 PTS Q50 — REB Q25 — AST Q75                   0.00156   0.0746
                 PTS Q50 — REB Q25 — AST Q25                   0.00145   0.0098
                 PTS Q25 — REB Q25 — AST Q75                   0.00128   0.0830
                 PTS Q25 — REB Q50 — AST Q25                   0.00122   0.0326
                 PTS Q25 — REB Q25 — AST Q25                   0.00115   0.0592
                 PTS Q25 — REB Q75 — AST Q50                   0.00112   0.0818
                 PTS Q50 — REB Q50 — AST Q25                  0.000845   0.2550
                 PTS Q25 — REB Q50 — AST Q75                  0.000704   0.4330
                 PTS Q50 — REB Q75 — AST Q25                  0.000664   0.5250
                 PTS Q75 — REB Q25 — AST Q50                  0.000507   0.5580
                 PTS Q25 — REB Q75 — AST Q25                  0.000015   0.9820
                 PTS Q75 — REB Q50 — AST Q25                 -0.000079   0.9140
                 PTS Q75 — REB Q25 — AST Q25                 -0.000705   0.2090


References
Bates, D., Maechler, M., and Jagan, M. (2026). Matrix: Sparse and Dense Matrix Classes and
  Methods. R package version 1.7-5.

D’Urso, P., De Giovanni, L., and Vitale, V. (2023). A Bayesian network to analyse basketball
  players’ performances: a multivariate copula-based approach. Annals of Operations Research,
  325:419–440.

Jun Yan (2007). Enjoy the joy of copulas: With a package copula. Journal of Statistical Software,
  21(4):1–21.

Li, D. X. (2000). On default correlation: A copula function approach. Technical Report 99-07, The
  RiskMetrics Group.

Liu, Y. and Yu, S. (2026). Bayesian Dirichlet process copula mixtures for heterogeneous multi-



                                               11
  cluster data: Methods and an NBA player stats application. Statistical Analysis and Data Mining:
  An ASA Data Science Journal, 19(3):e70074.

Sklar, A. (1959). Fonctions de répartition à n dimensions et leurs marges. Publications de l’Institut
  de Statistique de l’Université de Paris, 8:229–231. Distribution functions with n dimensions and
  their margins.

Whelan, K. (2026). The parlay puzzle: Expected utility and multi-leg betting. UCD Centre
 for Economic Research Working Paper Series WP2026/10, University College Dublin, School of
 Economics.




                                                  12
