<!-- source: library/preprints/arXiv/2026/2026 - Context-adjusted Player Evaluation for Twenty20 Cricket - Bandyopadhyay.pdf -->
<!-- item: https://arxiv.org/abs/2608.18020 -->
<!-- authors: Rhitankar Bandyopadhyay -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-05; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Context-adjusted Player Evaluation for Twenty20 Cricket

                                               Context-adjusted Player Evaluation for Twenty20 Cricket

                                                                                     Rhitankar Bandyopadhyay
                                                      University of Florida, Gainesville, FL 32611, USA. Email: r.bandyopadhyay@ufl.edu




                                                                                               Abstract
                                                 I develop a reproducible framework for evaluating individual batting and bowling performances in
                                                 Twenty20 (T20) cricket on one interpretable scale of runs above expectation, built from two ball-level
arXiv:2608.18020v2 [stat.AP] 27 Aug 2026




                                                 primitives. The first, Runs Above Expected (RAE), is the residual between the runs scored on a delivery
                                                 and a contextual expectation of what an average performer would produce in the same situation. That
                                                 expectation is a multiplicative log-linear model of the cohort scoring rate, whose per-cell estimator is
                                                 shown to be a conditional Poisson maximum likelihood multiplier. It is fitted by iterated backfitting
                                                 and stabilised by empirical Bayes shrinkage, so that thinly sampled contexts are pooled towards the
                                                 population. A single opposition symmetry places run-scoring and run-prevention on the same footing.
                                                 The second primitive, Dismissal Adjusted Runs (DAR), prices a dismissal in that currency as the runs
                                                 it forgoes, read off a batting side value function solved by dynamic programming through a Bellman
                                                 expectation recursion, under observed play. Because dismissal is the expected end of every innings,
                                                 the realised wicket cost (realDAR) is centered against its expectation (xDAR) under a league dismissal
                                                 hazard rate. The centered quantity is a run-weighted mean zero martingale residual of the dismissal
                                                 process, so a player is charged only for departing from average behaviour. The two primitives sum to a
                                                 symmetric Impact, which makes batting and bowling comparable in centre as well as in unit. Estimated
                                                 on over 2.7 million legal deliveries of men’s T20 cricket, the framework recovers known contextual
                                                 structure, agrees with the conventional rates it refines while correcting their context-blindness, and
                                                 yields face-valid player, innings and season leaderboards for the Indian Premier League.

                                           Keywords: Bellman expectation, Dynamic programming, Impact metrics, Player evaluation, Run ex-
                                           pectancy, Sports analytics.




                                           1    Introduction
                                           Twenty20 (T20) is the shortest and most widely watched form of professional cricket. Each side bats for
                                           a single innings of twenty overs, i.e. at most 120 legal deliveries, so scoring is compressed and unforgiving.
                                           A handful of balls can decide a match, and every delivery carries a visible trade-off between runs and
                                           the risk of dismissal. Since its introduction, the format has grown into a global professional circuit of
                                           franchise leagues, the Indian Premier League (IPL) foremost among them, alongside the Big Bash League
                                           (BBL), the Caribbean Premier League (CPL), the SA20 to name a few, in which recruitment, selection
                                           and in-game tactics turn on large sums of money and on increasingly fine grained data. Every ball of
                                           professional T20 matches is now recorded, which makes the quantitative evaluation of individual batting
                                           and bowling both possible and consequential, and it is that evaluation this paper develops.
                                              The rest of this section sets the context: Section 1.1 discusses performance analysis in T20 and why raw
                                           statistics are inadequate for it, Section 1.2 reviews the relevant literature across cricket and other sports,
                                           and Section 1.3 states our contribution. The data are described in Section 2; Section 3 formulates the
                                           first primitive, Runs Above Expected; Section 4 constructs the second of them, Dismissal Adjusted Runs,
                                           through a batting-side value function; Section 5 combines them into a single Impact rating; Section 6
                                           reports the empirical properties and validation; and Section 7 concludes.
                                               This work is part of the development of an app Regulus. The Regulus platform and its constituent metrics are
                                           proprietary at this point; all methodology described herein is for documentation and scholarly communication only.
                                                                                                                      2

1.1     Performance analysis in T20 cricket
A T20 innings unfolds in three broadly recognised phases. Unless rain or some other interruption shortens
the match, the ‘powerplay’ of the first six overs restricts the fielding side and rewards aggression; the
‘middle overs’ usually see consolidation, often against spin, and the ‘death overs’ at the end of the innings
are played at maximum risk. Batting and bowling therefore mean very different things at different points
of an innings, and against different opponents and conditions, and this is what makes individual evaluation
difficult. The conventional measures, namely a batter’s average (runs per dismissal) and strike rate (runs
per hundred balls), a bowler’s average (runs per dismissal), economy rate (runs per 6 balls), and strike
rate (balls per dismissal), aggregate over this heterogeneity and are systematically confounded by it. A
strike rate of 150 is unremarkable at the death and exceptional in the middle overs, an economy around 8
is expensive in the middle overs and cheap at the death, a boundary off a good bowler is worth more than
the same boundary off a part-timer, and a dismissal early in an innings costs a side far more than the same
dismissal towards its end. None of these situational factors are visible in the raw numbers. Two further
problems compound it. Batting and bowling are reported on incommensurable scales, i.e. runs per ball (or
100 balls) against runs per over, so the two roles cannot be placed on a common footing, which matters
acutely for all-rounders and for squad-level decisions, and a raw average credits occupation of the crease
without asking what the runs were worth in context. Yet these are the distinctions performance analysis
exists to draw, since selection, auction valuation, match-ups and in-game strategy all turn on what a
player actually contributes, net of the situation he found himself in. A metric fit to inform such decisions
must adjust for context at the level of the individual ball, must reward run-scoring and run-prevention on
the same scale as the wickets that punctuate them, and must stay interpretable enough to be trusted and
reproducible enough to be checked.
1.2     Review of literature
Quantitative cricket analysis has long rested on the idea of a run expectancy, a function that assigns to
each state of an innings the runs a side can expect from it. Its best known instance is the Duckworth-
Lewis method for resetting targets in interrupted matches (Duckworth and Lewis, 1998), whose resource
table is exactly such a function of the overs and wickets a side has in hand. A parallel line used dynamic
programming to derive optimal play: Clarke (1988) computed optimal scoring rates in one-day cricket, and
Preston and Thomas (2000) formulated optimal batting strategy against a target. The same machinery
underlies the modern win-and-score predictor WASP, built by Brooker and Hogan (2011) on a dynamic
programming run expectancy estimated from historical limited-overs data, while later statistical models
describe how scoring and dismissal risk evolve within an innings rather than optimise them (Stevenson and
Brewer, 2021). The value function of the present paper belongs to this tradition, but is put to a different
use. I solve it under observed play, to price the runs a wicket forgoes, not to prescribe how a side should
bat.
   Turning from game states to players, early evaluation measures refined the batting average and strike
rate into single indices (Lemmer, 2004), but these inherit the context-blindness of their ingredients. The
closest antecedent of our work is the simulation approach of Davis et al. (2015a) and Davis et al. (2015b),
who built a ball-by-ball T20 simulator and, from it, an expected run differential: the runs a player adds
relative to a standard player in the same role, obtained by re-simulating innings with and without him.
This captures context and reports contributions in runs, but it depends on a full generative simulator
and a role-defined replacement, and it does not yield a transparent per-ball decomposition. Other work
rates players through Bayesian or machine-learning models and data-envelopment indices, or models player
valuation specifically for the IPL auction. These gain flexibility at the cost of interpretability, and typically
treat batting and bowling on separate scales.
   Alongside the academic literature, several proprietary systems target the same quantity we do: a
context-adjusted, unified measure of impact, but behind closed models. Cricinfo’s Smart Stats1 report
Smart Runs (runs re-weighted by match context) and Smart Wickets (a dismissal valued by the batter
removed, its timing, and the state of the game) and combine the two into a single ‘Player Impact’ on a
runs scale, the same design goal as ours. CricViz derives expected runs, expected wickets and expected
  1
      Read articles and illustrations on Cricinfo’s Smart Stats here: https://www.cricinfo.com/genre/superstats-706
                                                                                                            3

dismissals from ball-tracking data, and independent analysts have proposed replacement-level measures
such as Runs Above Average Replacement2 , a cricketing analogue of baseball’s value over replacement.
These efforts are influential, but their mechanisms are largely unpublished, they often rely on proprietary
or tracking data unavailable for most matches, and they are validated only informally, so they can be
neither reproduced nor audited by others.
   The underlying idea of valuing an event by its expected contribution to a scoring currency, above what
an average or replacement performer would have produced, is mature in several other sports. Baseball’s run
expectancy and win probability accounting descends from Lindsey (1963) and now underpins reproducible
wins-above-replacement systems (Baumer et al., 2015). In association football, expected goals grade a
chance by its scoring probability, and action value frameworks such as VAEP value every on-the-ball
action by the change it induces in the probabilities of scoring and conceding (Decroos et al., 2019). In
basketball, the expected possession value model prices the state of a possession by the points it is expected
to yield (Cervone et al., 2016). All of these share one logic: price events in the currency of the game,
relative to expectation, which the present framework brings to T20 cricket.
   The cricketing literature either optimises play rather than evaluating it, evaluates players through
simulators or opaque models that are hard to reproduce, or reports the two roles on scales that do not
meet, and the systems that come closest to a unified impact measure are proprietary. What is missing
is a transparent, likelihood based framework that adjusts for context at the level of the individual ball,
prices wickets in the same runs currency as the runs themselves, and places batting and bowling on one
comparable scale, reproducible in full from public data. This paper provides it.
1.3     Contribution of the work
I build the framework from two ball-level primitives, both expressed in runs above expectation and shared
symmetrically between the two roles. The first, Runs Above Expected (RAE), is the residual between the
runs scored on a delivery and a contextual expectation of what an average performer would have produced
in the same situation, specified through phase, innings, era, fall of wickets, bowler type, venue and the
specific opponent. That expectation is a multiplicative, log-linear model of the cohort scoring rate whose
per-cell estimator I show to be a conditional Poisson maximum likelihood multiplier, fitted by iterated
backfitting and stabilised by empirical Bayes shrinkage, so that thinly sampled contexts and players are
pooled towards the population rather than trusted blindly. A single opposition symmetry credits a batter
against the bowler he faced and a bowler against the batter he contained, which places run-scoring and
run-prevention on one scale. The second primitive, Dismissal Adjusted Runs (DAR), prices a dismissal in
that same currency. A batting-side value function, solved by dynamic programming under observed play,
gives the runs a wicket forgoes in a given state. But charging a batter the full cost of every dismissal would
penalise even an average player, since being dismissed is the expected end of an innings. I therefore centre
the realised wicket cost against its expectation under a corresponding league dismissal hazard rate, which
yields a quantity that is exactly a run-weighted martingale residual of the dismissal process, mean zero
under average behaviour, so a player is charged only for departing from it. Summed over a career, the two
primitives give a symmetric Impact, batting and bowling differing only in sign, on a single interpretable
runs scale.
   Three parts of this are new. The first is reproducibility. Every multiplier, hazard and shrinkage
strength is estimated from public ball-by-ball data, and there is no tuning constant left to set, whereas the
proprietary impact systems do not disclose their models at all. The second is the pricing of a wicket as a
centered martingale residual, which is to our knowledge new to cricket. It is what puts a batter’s and a
bowler’s Impact on a common centre and not only a common unit: an average performer of either role sits
near zero, and the long-standing difficulty of placing the two roles on one footing goes away with it. The
third is that both primitives are additive at the ball level, so the same construction reads coherently from
a single delivery to a long career without re-fitting anything. I fit the framework on more than 2.7 million
legal T20 deliveries and report the contextual structure it recovers, the agreement of each primitive with
the conventional rate it refines, and leaderboards and case studies for the IPL.
  2
      Read here: https://www.cricinfo.com/story/using-the-runs-above-average-replacement-metric-1226970
                                                                                                              4

2   Data
The analysis uses a ball-by-ball dataset across men’s T20 cricket spanning from February 2005 to June
2026 (data last updated as of June 05, 2026), drawn from 19 competitions including T20 Internationals
and several major domestic franchise and national leagues. Table 1 summarises the dataset. The unit of
analysis is the legal delivery (is_legal_ball = True, wides and no-balls excluded).

                 Table 1: Data summary and coverage. The dataset has two tiers: a baseline
                 record present for every delivery and a ball-tracking record available only for a
                 section of matches. Qualification thresholds count players by legal balls, ni .

                       Quantity                                                       Value
                       Entire dataset
                       Total deliveries                                          2,819,700
                       Legal deliveries                                          2,727,420
                       Matches                                                      12,492
                       Distinct competitions                                             19
                       Date range                                     Feb 2005 - May 2026
                       IPL deliveries / matches                             295,629 / 1,243
                       Coverage of the detailed (ball-tracking) tier
                       Matches with any stroke annotation        2,128 (17.0% of matches)
                       Deliveries with stroke annotation          448,751 (16.5% of legal)
                       Deliveries with line/length                924,134 (33.9% of legal)
                       Baseline-only (Cricsheet) matches       10,364 (83.0% of matches)
                       Qualifying players
                       Qualifying batters, ni ≥ 30/100/500              6,234 / 3,800 / 1,220
                       Qualifying bowlers, ni ≥ 60/200                          4,607 / 2,516



Two tiers of detail. The dataset is deliberately heterogeneous in granularity, so I state exactly what is
available where. Each of the 12,492 matches (2,727,420 legal deliveries) carries a baseline record derived
from public Cricsheet repositories: the batter and bowler identities, the key components of model (1)
(phase, innings, date, wickets_fallen, bowler_type_grp, ground), the outcome fields runs_off_bat,
is_boundary, is_dot, bowler-credited dismissal flag and the chase-state components (runs, balls, wickets
remaining, target at any point during 2nd innings) used by the second-innings value function of Section 4. A
smaller ball-tracking tier adds the delivery’s line and length, stroke type, stroke magnitude, stroke direction,
elevation etc. This richer information is present for only a minority of the data: stroke annotation covers
448,751 legal deliveries (16.5%) across 2,128 matches (17.0%) and line and length data covers 924,134
deliveries (33.9%), so the majority of matches (10,364 or 83%) carry the baseline record alone. Coverage
is also uneven within the tier: some matches are annotated ball for ball while others are only partially
tracked, which is why I report ball counts rather than treating any match as wholly tracked.
   This heterogeneity forces a design choice. Both primitives, RAE (Section 3) and Dismissal Adjusted
Runs (Section 4), use only baseline fields, so they are computed identically on every match irrespective
of ball-tracking availability. Restricting the covariates to those recorded for every delivery keeps the
sample pool as large as possible, lets a player be compared across eras, venues and match situations on
one consistent baseline, and keeps the framework reproducible from public data. The richer ball-tracking
covariates (line, length, stroke geometry etc.) are therefore not used by the metrics defined here. A fairer
batting evaluation would, however, credit run-scoring relative to the exact delivery faced. I accordingly
extend the expected runs model to incorporate the delivery’s line and length on the annotated subset, and
formulate a modified RAE in Section S2 of the supplementary materials. No metric silently degrades on
a baseline-only match; each is fully defined from fields recorded everywhere.

3   The ‘Runs Above Expected’ (RAE) model
RAE is the foundation of the framework, and every other metric is a functional of the ball-level RAE series.
The construction has three parts: a contextual expectation model (Section 3.1), its estimation by iter-
                                                                                                                                  5

ated, shrunk backfitting (Section 3.2-3.3) and the role-specific opposition overlay followed by aggregation
(Section 3.4).
3.1    The contextual expectation model
Let rb ∈ {0, 1, 2, 3, 4, 6} be the runs off the bat on legal delivery b and let xb denote its context. I model
the cohort expected runs, defined as what an average batter would score (for batting), and an average
bowler would concede (for bowling), in that situation, as a product of a global base rate and contextual
multipliers:
                                  µ(xb ) = µ0 γcscen  γ era γ wkt γ type γ ven γ opp ,
                                                 1 (b) c2 (b) c3 (b) c4 (b) c5 (b) c6 (b)
                                                                                                           (1)

where µ0 is the grand mean over all legal deliveries, each of γcscen
                                                                 1 (b)
                                                                       , γcera
                                                                            2 (b)
                                                                                  , γcwkt
                                                                                       3 (b)
                                                                                             , γctype
                                                                                                  4 (b)
                                                                                                        , γcven
                                                                                                             5 (b)
                                                                                                                   is a non-negative
                                                                                              opp
multiplier attached to a categorical cell of the corresponding factor, and γc6 (b) is the opposition factor,
defined as the opposition bowler’s multiplier for batter evaluation and the opposition batter’s multiplier
for bowler evaluation (Section 3.4). The five shared factors stated in (1) are:

                       Factor           Cell key cf (b)                     Captures
                       Scenario         (phase, innings)                    situational scoring level
                       Era              (year, phase)                       temporal scoring inflation
                       Wicket           (phase, wickets fallen)             fall-of-wickets pressure
                       Bowler type      (phase, pace/spin sub-type)         match-up difficulty by phase
                       Venue            (ground, 3-year bucket)             pitch, via temporal locality

The wicket factor is conditioned on the exact number of wickets fallen (0 to 10), so the fall-of-wickets
gradient is estimated at full resolution and the empirical Bayes shrinkage of Section 3.3 pools the sparse
deep-collapse cells automatically; the venue bucket groups consecutive 3-year windows at each ground.
Taking logs on both sides, (1) is a main-effects log-linear model,
                                                                                  (f )
                                             log µ(xb ) = log µ0 +          log γcf (b) ,                                       (2)
                                                                      X

                                                                        f

on crossed categorical keys; the crosses (e.g. phase×innings, year×phase etc.) admit a controlled set of
two-way interactions while keeping the parameter count tractable.
Remark 1 (Difficulty parameter lives in the expectation). Phase difficulty is captured inside µ(xb ),
                                    scen
principally by the scenario factor γ(phase,innings) (and refined by era, wicket and bowler-type factors, each
phase-conditioned). A run in a higher-scoring phase is therefore measured against a higher bar automati-
cally. No separate phase weight is applied to either role, RAE therefore acts as a pure residual on the run
scale.
   The factors of (1) are not chosen by convention alone; each of them carries strong, independent signal.
Table 2 reports an analysis of deviance for the fitted expected runs model: dropping any single factor
from the converged fit raises the Poisson deviance of Proposition 1 by the stated amount, on its degrees of
freedom. At this sample size, every factor is significant far beyond any conventional threshold (p < 10−300 ),
so the deviance each explains is read not as a test but as a measure of relative importance. The venue and
the fall of wickets state carry the most, the phase-innings scenario and opposition bowler identity follow,
and even the smallest, the pace or spin sub-type of a bowler, remains decisive. The symmetric opposition
batter factor of the bowler evaluation fit is significant to the same degree.
   Beyond the covariates in (1), the delivery’s line and length are the most informative additions the data
offer. On the annotated subset, length alone explains a deviance rivalling that of the venue factor and
line a smaller but still overwhelming amount (lower block of Table 2). I keep them out of the headline
model for the comparability reasons of Section 2, but develop the resulting extension, a modified RAE,
and quantify its effect in Section S2 of the Supplementary Materials.
   The case for line and length is cricketing as much as statistical. Two deliveries identical in every recorded
respect, i.e. the same phase, innings, bowler type, venue and match state, are still not equivalent if one
is a good length ball outside off and the other a half volley on the pads. A boundary off the former is
a finer stroke than off the latter and, for a fair evaluation, should be rewarded as such. Symmetrically,
                                                                                                                           6

                    Table 2: Analysis of deviance for the expected runs model. Each row gives the
                    rise in Poisson deviance (χ2 ) when the factor is dropped from the converged fit,
                    on its degrees of freedom; all factors are significant beyond any usual threshold.

                        Factor                                  d.f.   ∆Deviance (χ2 )             p
                        Always-available model (1)              (n = 2,727,420 legal deliveries)
                        Scenario (phase × innings)                7              21,686   < 10−300
                        Era (year × phase)                       68               8,611   < 10−300
                        Wicket (phase × wickets fallen)          32              27,972   < 10−300
                        Bowler type (phase × sub-type)           20               2,812   < 10−300
                        Venue (ground × 3-yr bucket)          1,267              41,767   < 10−300
                        Opposition bowler (identity)          7,281              27,545   < 10−300
                        Additional ball-tracking covariates    (annotated subset, n = 804,308)
                        Length (phase × length)                  20              41,924   < 10−300
                        Line (phase × line)                      20               3,409   < 10−300




                    Figure 1: Line×length structure for right-hand batters against right-arm pace,
                    by phase. Each cell reports the frequency (percentage of the phase’s deliveries
                    pitching there), strike rate and batting average in that cell.


being dismissed by a sharp yorker is not the lapse that missing a straight full toss is, and ideally the two
should be debited differently. These ‘line-and-length’ effects are large, and they shift with the phase and
the bowler. Figure 1 shows, for right-hand batters against right-arm pace, how sharply scoring depends
on where the ball lands. Against a good-length ball outside off, which is the single most common delivery
(27% of powerplay balls), the strike rate is only 97, less than half the 208 that a short ball on the same
line concedes, and the mix itself moves through the innings, fuller lengths growing far more frequent at
the death overs. Figure 2 tells the same story from the striker’s end, plotting where each delivery reaches
the batter. The cloud of impact points3 , and the wickets, fours and sixes within it, climbs and spreads
as the innings progresses. A model blind to line and length scores all of these deliveries against one bar;
   3
     Impact points, along with the detailed ball-tracking data for IPL 2026, have been obtained from the official IPL website
run by BCCI: https://www.iplt20.com/matches/results.
                                                                                                               7




                  Figure 2: Ball impact point (the ‘beehive’ stump view) for right-hand batters
                  against right-arm pace in IPL 2026, by phase. Each dot is a delivery, placed
                  by its width and height as it reaches the batter; wickets, fours and sixes are
                  highlighted. The cloud rises and widens from the powerplay to the death overs.


conditioning on them, where the data allow, is the refinement Section S2 takes up.
3.2   Estimation by iterated backfitting
The factors in (1) are correlated: deliveries early (and late) in an innings are simultaneously in the
Powerplay (and Death) phase, at low (and high) wicket counts, and often against pace, so fitting each
against the raw base rate would over-count shared variation. I therefore estimate them by sequential
residualisation (backfitting) in the fixed order: scenario → era → wicket → bowler type → venue →
opposition. Carry a running fitted value eb , initialised at eb = µ0 . At any stage, for the current factor f
with cells c, set                                       P
                                                              rb
                                             γ̂c = Pb∈c ,
                                               (f )
                                                                                                          (3)
                                                          b∈c eb
                          (f )
then update eb ← eb · γ̂cf (b) before moving to the next factor. Note that (3) is exactly the multiplica-
tive adjustment that equates each cell’s fitted total to its observed total and it has a precise likelihood
interpretation.
Proposition 1 (Cell ratio as a conditional Poisson MLE). Suppose rb | xb ∼ Poisson(µb ) independently,
with log µb = log eb + log γc(b) , i.e. log eb enters as a known offset. Then the maximum-likelihood estimator
of the multiplier γc for cell c is γ̂c =                   b∈c eb , which is (3).
                                             P         P       
                                               b∈c rb

Proof. The cell-c log-likelihood contribution is b∈c {rb (log eb + log γc ) − eb γc } + const. Differentiating
                                                    P

with respect to γc and equating it to zero gives b∈c rb /γc − b∈c eb = 0, hence the stated estimator. The
                                                P             P

second derivative − rb /γc2 < 0 confirms a maximum.
                    P


   Thus each update step given by (3) is one coordinate (block) step of Gauss-Seidel ascent on the Poisson
log-likelihood of (2), holding the other factors as offset. Since the log-likelihood is concave in the log-
multipliers, repeating the sweep drives the estimates to that peak, i.e. the one best-fitting set of multipliers.
On the first pass, each factor is fitted against the factors placed before it, and on every later pass, a factor
is re-fitted against all the others (I divide its current multiplier back out of eb before re-estimating, so
no factor counts itself twice). I iterate the sweep till convergence, stopping once the fitted values eb have
effectively stopped changing. The empirical Bayes shrinkage of Section 3.3 is re-applied each time a factor
is fitted.
Remark 2 (Order independence at convergence). The maximised log-likelihood is unique, so the fitted
expectation and hence the ball-level RAE does not depend on the order in which the factors are cycled.
The ordering (most to least populous) affects only the number of cycles to convergence. Up to the mild
                                                                                                              8

empirical-Bayes shrinkage, the fit satisfies the Poisson score identities b∈c rb = b∈c µ̂b for every cell of
                                                                                P           P

every factor, so the residual RAE is centered within each context cell and not merely in aggregate.
3.3   Empirical Bayes shrinkage of the multipliers
Thin cells with very few deliveries (a rare ground in a particular three-year window; a bowler or batter
with a short record) yield unstable ratios. Each raw multiplier is therefore shrunk towards the neutral
value 1 by a pseudo-count κf :
                                    (f )
                                nc γ̂c + κf                                               nc
                     γc(f ) =               = ωc γ̂c(f ) + (1 − ωc ) · 1,       ωc =            ,           (4)
                                  nc + κ f                                             nc + κ f

where nc is the cell’s delivery count. The shrinkage is a convex combination of the data ratio and unity,
with data weight ωc increasing in sample size; κf is the number of prior deliveries pulling a thin cell back
to neutral.
   Here 1 is the neutral no-adjustment value: a multiplier of 1 leaves the expectation unchanged. Shrinking
towards it simply treats a thin, poorly-estimated cell as average until it has enough data to prove otherwise.
I estimate one κf per factor from the data by empirical Bayes, so the degree of shrinkage is itself learned.
                         (f )
Model the raw ratios γ̂c as noisy estimates of true multipliers θc that scatter across cells around a cross-
sectional mean of 1 with variance τf2 . Two variances must be separated here. The between-cell variance
τf2 is the real spread of the true effects from one cell to the next; this is the signal I want to keep. The
within-cell variance is the sampling error in a single cell’s estimate, coming only from its finite number of
                                                              (f )
deliveries; this is the noise I want to discount. Because γ̂c =                    b∈c eb has a fixed offset in
                                                                     P         P        
                                                                        b∈c rb /
its denominator, this sampling variance is
                                                        Var(r) nc
                                                   vc = P        2 .                                       (5)
                                                          b∈c eb

I calibrate it to the empirical run variance Var(r) rather than to a Poisson assumption: runs off the bat
are lumpy (point masses concentrated mostly at 0, 1, 2, 4, 6 and few at 3, 5) and markedly over-dispersed,
with Var(r)/µ0 ≈ 2.08 in the dataset, so a Poisson variance would understate the noise and leave thin
cells over-trusted.
                                                                 (f )
   I do not observe τf2 directly, since the observed spread of γ̂c mixes signal and noise. I recover it by the
DerSimonian-Laird method of moments (DerSimonian and Laird, 1986), the standard method-of-moments
empirical Bayes estimator, which simply subtracts the average sampling variance from the total observed
spread, leaving the between-cell signal τf2 . The Bayes posterior mean for θc is then the precision-weighted
average of the cell’s own ratio and the neutral value 1, with weight

                                                    τf2          signal
                                           wc =            =                .                               (6)
                                                  τf2 + vc   signal + noise

So a cell is trusted in proportion to how much of its apparent effect is real rather than sampling noise.
Finally, because each delivery’s expectation is close to the base rate, b∈c eb ≈ nc µ0 and hence vc ≈
                                                                          P

(Var(r)/µ20 )/nc ; substituting this into (6) collapses the variance weight exactly onto the pseudo-count
form ωc = nc /(nc + κf ) of (4), with

                                           Var(r)   within-cell sampling noise
                                  κf =            =                            .                            (7)
                                            2  2
                                           µ0 τf       between-cell signal

Thus a single number κf (the noise-to-signal ratio for factor f ), read as an equivalent count of prior
deliveries, sets the shrinkage. A factor whose cells differ only weakly beyond noise (small τf2 ) gives a large
κf and is pulled hard towards 1, while a factor carrying strong, repeatable variation (large τf2 ) gives a small
κf and is left close to its raw ratios. A cell holding exactly κf deliveries sits halfway (ωc = 0.5) between
its own estimate and the neutral value. The fitted values (Table 3) recover the expected ordering without
it being imposed: the small pace/spin effect (bowler-type) is shrunk most heavily (κf ≈ 103 ), while venue,
opposition batter and scenario, which carry large heterogeneity, are shrunk the least (κf ≈ 1.5-1.9 × 102 ).
                                                                                                             9

Remark 3 (Relation to the conjugate Gamma-Poisson posterior). Under a Gamma(κ, κ) prior on γc
(prior mean 1, prior strength κ) with the Poisson likelihood of Proposition 1, the posterior mean is
( b∈c rb + κ)/( b∈c eb + κ). Estimator (4) replaces the exposure b∈c eb by the count nc ; since eb ≈
 P             P                                                        P

µ0 ≈ 1.24 runs per ball, b∈c eb ≈ 1.24 nc , so (4) is a close, slightly more conservative proxy for the exact
                        P

conjugate posterior mean. I therefore describe it as an empirical Bayes shrinkage estimator rather than
an exact Bayes rule.
3.4   The opposition overlay and aggregation
The single adjustment that specialises the cohort expectation to either role is the opposition factor γ opp ,
estimated symmetrically. For batters’ evaluation, a bowler multiplier γ(bowler
                                                                          bowl
                                                                                id) is co-fit with the context
factors in the joint backfitting of Section 3.2 and for bowlers’ evaluation, a batter multiplier γ(batter
                                                                                                      bat
                                                                                                            id)
is co-fit with the same context factors. The two role-specific fits share an identical context specification,
differing only in which opposition identity they carry, and each is applied one at a time.

  • Batter’s RAE multiplies the expectation by the opposition-bowler multiplier γ bowl , so out-scoring a
    strong bowler yields a larger residual.
  • Bowler’s RAE multiplies the expectation by the opposition-batter multiplier γ bat , so containing a
    strong batter yields a larger (more negative) residual.

A player’s own factor is never applied to his own residual since multiplying a bowler’s expectation by his
own multiplier would cancel the skill being measured, and likewise for a batter.
  The ball-level Runs Above Expected and its player aggregates are finally recorded as
                                                    1 X
                 RAEb = rb − µ̂(xb ),      RAEi =           RAEb ,     RAEtotal =          RAEb ,          (8)
                                                                                    X
                                                                          i
                                                    ni b: i                         b: i
                                      √
with standard error sei = sdb (RAEb )/ ni , where the expectation µ̂ carries the role-appropriate opposition
factor. For a batter, RAEi (denoting RAE/Ball) is the headline rate, centered so that a cohort-average
batter scores ≈ 0, with positive values denoting run production above contextual expectation. For a
bowler, RAEi is the excess runs conceded per ball, so lower (negative) is better: a negative RAE/Ball
means the bowler concedes fewer runs than an average bowler would concede in the same situation. The
per-ball value used by all downstream signals is vb = RAEb for batters and vb = −RAEb for bowlers.

Reading RAE at different scales. Because RAE is defined and additive at the ball level, the same
primitive reads coherently at every level of aggregation, with no re-fitting. The expectation is fixed, so a
delivery, a knock and a career are all just sums of the identical residual, and each scale answers a distinct
question.

  • Single ball-level event (RAEb ): the value of a single delivery, i.e. the unit for ball-by-ball diagnostics
    (determines which deliveries a batter punished, where a bowler was beaten etc.).
  • Per innings or spell ( b∈knock/spell RAEb ): the value of one performance. This is a context-adjusted
                            P

    innings/spell measure. For example, a fighting 40-run innings against quality pace during a collapse
    can outscore a 60-run innings on a flat deck, because the expectation bar it cleared was higher.
  • Per-ball average (RAEi or RAE/Ball): a player’s quality rate, the headline per-ball figure, compa-
    rable across players irrespective of sample size.
  • Cumulative (RAEtotal
                      i  ): the total value contributed by a player over a series, tournament, career or
    any span of time.

The rate and the total RAE outputs distinctly answer “how good per ball (or on average)” versus “how
much value in total” a player produces. A short-sample specialist can top the former while a durable
accumulator tops the latter (Tables 9 and 10). Run prevention, however, is only one of a bowler’s two
sources of value, and only one side of a dismissal’s ledger; the next section prices the second, Dismissal
Adjusted Runs.
                                                                                                             10

4     Dismissal Adjusted Runs (DAR)
RAE prices the runs on a delivery, but a delivery that takes a wicket carries value that a per-ball run
residual cannot capture: a wicket removes a batter from the remainder of the innings, and the runs he
would have gone on to score go with him. From the batting side’s view, the side loses whatever those
forgone runs exceed what the batters who followed him actually managed; from the bowling side’s, the
same runs are saved. I call this quantity Dismissal Adjusted Runs: the number of runs a dismissal costs the
batting side, and equivalently the number it saves the bowling side. It is the framework’s second primitive
and, like RAE, a currency shared by the two roles. I build it in two steps. Section 4.1 constructs a batting-
side value function and reads off, for every delivery, the wicket cost c(s) it would forgo were a dismissal
to occur there, a single non-negative number attached to the match state. Section 4.2 then aggregates
this cost twice: once over a player’s realised dismissals and once, as a hazard-weighted expectation, over
all the balls the batter is party to. The primitive that enters Impact is the difference of the two, which
centers the wicket ledger at zero in the same way RAE centers the run ledger.
   A wicket’s value is inherently counterfactual, in the sense of “how would the innings have continued had
the batter survived?”. It cannot be read directly off the scorecard, or off any record of events that actually
took place, and must instead be estimated against a model of the innings’ continuation. The natural
model for this estimation is a run-expectancy function or ‘value’ function. To every state of an innings
it assigns the runs the batting side can expect to add from that point onward. Given such a function,
a wicket needs no separate apparatus to price, rather it is simply the drop in expected remaining runs
when a set batter is replaced by the next one in. Valuing game states this way has a long lineage in sport,
from the run-expectancy tables of baseball (Lindsey, 1963) to the resource tables of Duckworth and Lewis
(1998), which are themselves a value function of the overs and wickets (together termed as ‘resources’ in
DL and DLS methods) a side has in hand.
   Such value functions are naturally recursive. The runs expected from a state equal what happens on the
next delivery plus the expected value of the state that delivery leads to, averaged over its possible outcomes.
This decomposition is a Bellman equation, the identity that organises dynamic programming by tying the
value of a state to the values of its successors, and it comes in two forms that must not be confused.
The Bellman optimality equation maximises over the actions available at each state and so describes how
a side should bat to score the most. It is the object of the dynamic programming studies of optimal
scoring rates and batting strategy in limited-overs cricket (Clarke, 1988; Preston and Thomas, 2000). The
Bellman expectation equation instead holds the policy fixed: it takes the way batters actually score and
are dismissed, estimated directly from the data, and returns the expected runs under that behaviour, in
the descriptive spirit of models of how scoring evolves through an innings (Stevenson and Brewer, 2021).
Pricing a wicket calls for the runs an innings would in fact have yielded, not the runs an optimal side
could have extracted, so I adopt the expectation form in this paper. Carrying no maximisation, it is a
linear recursion, and since the state advances one ball at a time, it is acyclic in terms of balls remaining.
So a single backward sweep from the end of the innings solves it exactly, with no optimiser and no fixed
point to iterate towards.
4.1    The batting team value function
Describe an innings by the state s = (m, w, i, j): m legal balls remain in the innings, the batting side has
w remaining wickets in hand, the striker is of quality tier i and the non-striker of tier j (tiers are defined
in Section 4.2), with e ∈ {1, 2} denoting the innings. Let

       Ve (m, w, i, j) = expected runs the batting side scores over the remaining m balls from state s,

under observed play. The phase of a delivery is a deterministic function of the balls already bowled, given
by φ = φ(M0 − m) with M0 = 120, so contextual scoring enters through the transition model without
enlarging the state.
  On the next delivery, the striker (tier i) is dismissed with hazard rate hi,φ,e , otherwise he scores r ∈
R = {0, 1, 2, 3, 4, 5, 6} runs with probability πr|i,φ,e , where r∈R πr|i,φ,e = 1 (probabilities are conditional
                                                                P

on survival of the batter). Odd runs and the end of an over rotate the strike; a dismissal brings in a fresh
batter of tier ι(w) (see details in Section 4.2). Writing σ(r, m) ∈ {0, 1} for whether the strike changes ends
                                                                                                                               11

after the ball (i.e. r is odd or the over ends), the value function satisfies the Bellman expectation recursion
                                                                                             h                         i
   Ve (m, w, i, j) = hi,φ,e Ve m − 1, w − 1, ι(w), j + (1 − hi,φ,e )                 πr|i,φ,e r + Ve m − 1, w, i′ , j ′ ,     (9)
                                                                              X

                                                                              r∈R

where (i′ , j ′ ) = (j, i) when σ(r, m) = 1 and (i, j) otherwise, and on a dismissal the incoming batter takes
strike (its position rotates under σ likewise). The recursion closes at the absorbing boundaries

           Ve (0, w, i, j) = 0   (balls exhausted),            Ve (m, 0, i, j) = 0    (batting team gets all out).           (10)

   Equation (9) is the expectation form introduced above: it evaluates the runs a team scores under its
observed scoring and dismissal behaviour, with no maximisation over batting actions. The state space is
finite and acyclic when ordered by m, so (9) has a unique solution, obtained by a single backward sweep
from m = 0 to m = M0 .
4.2    The transition model
The recursion needs, per (tier, phase, innings), a dismissal hazard rate h and a scoring distribution π, all
estimated from the same dataset with the empirical Bayes shrinkage of Section 3.3.
   Player rates and quality tiers. For each batter, I form empirical Bayes shrunk estimates of their scoring
rate µi and per-ball dismissal hazard ηi ,

                                             b: i rb + κµ µ0                  di + κη η0
                                            P
                                     µi =                        ,     ηi =              ,                                   (11)
                                                ni + κ µ                       ni + κ η

with di denoting the batter’s dismissals, µ0 and η0 the corresponding means based on the dataset, and κµ
and κη the corresponding pseudo-counts in the sense of the empirical Bayes shrinkage theory described in
Section 3.3. Batters are grouped into Q = 6 quality tiers by ball-weighted quantiles of µi , so a tier is a
homogeneous quality band and thin players are pulled to the population before being tiered.
   Scoring and hazard by state. Pooling deliveries by (tier, phase, innings), the scoring distribution π·|i,φ,e
and hazard rate hi,φ,e are the corresponding empirical frequencies, each shrunk toward its (phase, innings)
pooled distribution by a conjugate (Dirichlet, respectively Beta) pseudo-count so that sparse cells borrow
strength. Estimating π and h separately by innings lets the second-innings value function reflect chase-
state scoring; a finer conditioning on the required run rate is a natural refinement (see Section 7).
   Strike rotation and the incoming batter. Odd runs and end of an over rotate the strike through σ.
When a wicket falls, the incoming batter’s tier ι(w) is the empirical average tier of batters entering at
that position, so the value function unrolls the actual remaining batting order: every subsequent batter is
accounted for through the recursion, weighted by how much of the innings remains and how likely each of
them is to bat in it.
   Because the state is ordered by balls remaining in the innings, one backward pass fills the entire table
exactly (Algorithm 1).

Algorithm 1 Backward solve of the batting-side value function Ve (Bellman expectation)
 1: Ve (0, ·, ·, ·) ← 0; Ve (·, 0, ·, ·) ← 0
 2: for m = 1, . . . , M0 do
 3:    φ ← φ(M0 − m); overEnd ← 1[(M0 − m + 1) mod 6 = 0]
 4:    for w = 1, . . . , 10 and tiers i, j ∈ {1, . . . , Q} do
          A ← r∈R πr|i,φ,e r + Ve (m − 1, w, i′ , j ′ )                                 ▷ (i′ , j ′ ) per strike rotation σ(r, m)
                 P                                          
 5:
 6:       B ← Ve (m − 1, w − 1, ι(w), j)                                                                    ▷ 0 if w = 1 (all out)
 7:       Ve (m, w, i, j) ← hi,φ,e B + (1 − hi,φ,e ) A
 8:    end for
 9: end for
10: return Ve
                                                                                                                                12

Per-ball wicket cost. Consider a delivery in state s = (m, w, i, j, e): a tier-i striker with a tier-j partner,
m balls and w wickets remaining in innings e. Had the striker been dismissed here, the batting side would
trade its current continuation for the one that follows a wicket, the ball is consumed and a fresh batter of
tier ι(w) resumes, so the runs forgone are the drop in the value function,
                               h                                                                                   i
                      c(s) =          Ve (m, w, i, j)         − Ve (m − 1, w − 1, ι(w), j) + δfresh                        ,   (12)
                                      |      {z        }             |             {z               }                  +
                                   runs if batter survived               runs after the dismissal

where [ · ]+ = max{·, 0}. The quantity in brackets is non-negative by construction, since a set batter is
worth at least as much as the fresh one who replaces him, and the positive part only guards against rare
estimation noise. The correction δfresh ≥ 0 accounts for the incoming batter entering unset: a new batter
scores below his settled rate over his first few deliveries. Writing the empirical ‘set curve’ as f (·), with
f (k) ∈ (0, 1] the fraction of the settled rate realised over the first k balls, and E = {1 − (1 − ηi )si m }/ηi for
the geometric survival expectation of balls the dismissed batter would have faced (from his hazard ηi and
strike share si ),
                                       δfresh = (1 − f (E)) µ min(E, Emax ).                                   (13)
Note that c(s) is a function of the match state, defined on every delivery and not only on those that
happen to take a wicket. Every state is priced on its own terms: the quality of the striker and his partner,
the balls and wickets remaining, the phase and the innings, so no global ‘runs per wicket’ constant enters
anywhere. Dismissing a top-order batter in the powerplay forgoes many runs; removing a tail-ender in the
final over forgoes almost none, and the same expression returns both.

Realised and expected Dismissal Adjusted Runs. Let Wb ∈ {0, 1} mark whether the striker was
dismissed on delivery b, and let sb be its state. The realised Dismissal Adjusted Runs (realDAR) sums the
cost over a player’s actual dismissals, grouped by Di , the deliveries on which batter i was out and Wi , the
deliveries on which bowler i took the wicket,

                               realDARbat =                c(sb ),         realDARbowl =            c(sb ).                    (14)
                                                     X                                         X
                                      i                                           i
                                                    b∈Di                                       b∈Wi

Taken alone, this is a strictly non-negative accumulation, one term per wicket, and it is the naive quantity
one would debit the batter and credit the bowler. It is also what makes the two roles incomparable if
used directly: a mean-zero run ledger (RAE) combined with a one-signed wicket ledger (realDAR) drives
every batter’s total down and every bowler’s up, an artefact of mixing a centered and an uncentered
quantity rather than a fact about the players (Section 6.3 quantifies the resulting scale gap). The correct
comparison is not against zero but against what the same deliveries would have cost an average player.
Let h̄φ,e be the global dismissal rate per legal ball in phase φ, innings e (for evaluations confined to a
large enough league, tournament or era, the corresponding dismissal rate can be used instead for finer
accuracy). This is defined as a context-level baseline, conditioned on the situation and not on the player
being evaluated, exactly as the cohort expectation µ(xb ) is in RAE. Summing the cost over every delivery
a player takes part in, weighted by that hazard, gives the expected Dismissal Adjusted Runs (xDAR). For
Fi denoting the deliveries batter i faced and Bi those bowler i bowled,

                          xDARbat =               h̄φb ,eb c(sb ),         xDARbowl =           h̄φb ,eb c(sb ).               (15)
                                            X                                               X
                              i                                                i
                                           b∈Fi                                             b∈Bi

xDARbat
      i   reads as the wicket value an average batter would be expected to concede over the situations i
actually batted in, and xDARbowl
                              i    the value an average bowler would be expected to take over the balls i
actually bowled.

The centered Dismissal Adjusted Runs. The primitive that enters the final Impact of a player,
Dismissal Adjusted Runs (DAR), is the difference of the two aggregates, realised minus expected. Because
  b∈Fi Wb c(sb ) =  b∈Di c(sb ) = realDAR i , it collapses to a single sum over the balls faced,
P                  P                      bat


                      DARbat := realDARbat − xDARbat =                                     Wb − h̄φb ,eb c(sb ),               (16)
                                                                                    X                     
                         i             i         i
                                                                                    b∈Fi
                                                                                                                13

and symmetrically for the bowler over Bi . The factor b (Wb − h̄φb ,eb ) is the martingale residual of
                                                               P

the dismissal counting process, i.e. observed events minus their compensator, the accumulated hazard
(following Barlow and Prentice (1988) and Therneau et al. (1990)), so (16) is that residual weighted by
the run value of each potential wicket. The following makes the centering precise.
Proposition 2 (The centered Dismissal Adjusted Runs is a mean-zero martingale residual). If, condi-
tional on the state sb , a batter is dismissed at the league hazard, E[Wb | sb ] = h̄φb ,eb , then E DARbat     =
                                                                                                             
                                                                                                           i
E realDARbat     xDAR    bat 
                               = 0.
  
            i  −         i          Consequently  a batter is charged only for  departing    from  the global (or
league) dismissal rate: negative values (survival beyond expectation) raise Bat Impact, positive values (be-
ing dismissed more often, or in costlier states, than his situations warranted) lower it, and dismissal at
exactly the expected rate is free.

Proof. Taking expectations in (16), E[(Wb − h̄φb ,eb )c(sb ) | sb ] = c(sb ) E[Wb − h̄φb ,eb | sb ] = 0 under the
stated null; summing over Fi and applying the tower property gives the result. The same argument holds
for the bowler over Bi .

Remark 4 (A transfer of expected runs, conserved system-wide). The wicket cost c(sb ) enters the dis-
missed batter’s ledger with a negative sign and the bowler’s with a positive one, so a wicket remains a trans-
fer of expected runs between the sides. The centering is conserved in aggregate as well: the expected total
is the same whether summed over all batters or all bowlers, i xDARbat    i =    b h̄φb ,eb c(sb ) =   i xDAR i
                                                                                                             bowl
                                                                P             P                     P
                                                                                                                  ,
while i realDARbat    =      realDAR bowl
       P                P
                   i       i         i    is the realised total. The framework  therefore    stays  balanced glob-
ally while judging each player against the situations they personally faced, the same property RAE pos-
sesses.

5   Impact: batting and bowling on the same runs scale
With two primitives in hand, i.e. RAE for excess runs on every ball and the centered Dismissal Adjusted
Runs (DAR = realDAR − xDAR) for excess wicket value, a player’s Impact is his total contribution across
both channels. The construction is symmetric between the roles and differs only in sign: a batter and a
bowler each add value by scoring or saving runs, and transfer value at dismissals relative to what those
dismissals were expected to be worth.

Batting Impact. A batter adds runs above expectation ball by ball (+RAE) and carries the centered
wicket ledger:
                                 (Bat)
                               Ωi      =   RAEb − DARbat                                     (17)
                                         X
                                                           i .
                                                  b∈Fi

The first term rewards how he scored, a per-ball residual against a contextual par, so a below-par passage
accrues little or negative RAE however long it lasts. The second term, expanded as realDARbat i −xDAR i ,
                                                                                                         bat

credits the wicket value an average batter would have surrendered over his situations and debits what he
actually surrendered. A batter who outlasts the global (or league) dismissal rate is rewarded for it; one
who is dismissed early or cheaply, relative to the states he batted in, is charged the excess. This differs
from a raw wicket penalty in an important way. Getting out is the expected end of every innings, so the
metric does not tax a batter simply for being dismissed, rather it taxes only dismissals beyond expectation,
and pays a survival dividend below it. Occupation of the crease is close to neutral rather than free, since
the survival credit it earns is offset by the weak RAE that slow scoring produces, while sustained batting
at or above par is rewarded through both channels at once.

Bowling Impact. Symmetrically, a bowler saves runs ball by ball (−RAE) and carries the centered
wicket credit:
                              (Bowl)
                            Ωi       =−     RAEb + DARbowl                                 (18)
                                        X
                                                           i   .
                                                   b∈Bi

Here the wicket term credits a bowler for taking wickets beyond what his overs would ordinarily yield and
neither rewards nor penalises one who takes exactly the expected number. This is the correction that a
raw wicket count misses: a high-volume containment bowler accumulates wickets simply by bowling many
deliveries, and pricing those against the expected haul strips out the inflation while leaving the strike
                                                                                                          14

bowlers who beat expectation ahead. Run prevention and this net wicket credit are the two separate
sources of bowling value, and both are measured in runs, so they add directly. Their relative weight is not
a tuning parameter but a consequence of the value function and the hazard baseline.
Remark 5 (One centered scale, comparable across roles). Both (17) and (18) are sums of two mean-
zero residuals in runs above expectation. A batter’s Impact and a bowler’s Impact are therefore readily
comparable: a value of +300 denotes the same 300 runs of net contribution whichever role produced
it, and an average performer of either role sits near the common origin. Under the naive aggregate
   RAE ∓ realDAR, a one-signed wicket total added to a centered run total pushes the roles onto disjoint
P

ranges; subtracting the expectation xDAR restores a shared scale, as Section 6.3 documents. Impact may
be read as a career or tournament total, which is longevity-aware because both the run value and the
                                                               (Bat)
survival credit accumulate with volume, or as a per-ball rate Ωi     /ni ; the two answer peak-quality and
total-contribution questions respectively.
   Given the value table of Algorithm 1 and the hazard baseline h̄φ,e , both aggregates assemble in a single
linear pass over the deliveries (Algorithm 2): each ball adds its RAE to the striker and its negative to
the bowler, adds the hazard-weighted wicket cost h̄φb ,eb c(sb ) to both players’ expected ledgers, and, on a
dismissal, adds the realised cost c(sb ) as well.

Algorithm 2 Assembly of batting and bowling Impact in one pass over deliveries
 1: Rbat , Rbowl , realDARbat , realDARbowl , xDARbat , xDARbowl ← 0 for all players
 2: for each legal delivery b with striker p, bowler q, state sb do
 3:    Rpbat += RAEb ; Rqbowl −= RAEb
 4:    xDARbatp += h̄φb ,eb c(sb ); xDAR q
                                         bowl
                                               += h̄φb ,eb c(sb )
 5:    if a wicket falls (Wb = 1): realDARbat
                                            d(b) += c(sb ), realDAR q
                                                                      bowl
                                                                           += c(sb )
 6: end for
     (Bat)                                         (Bowl)
 7: Ωp     ← Rpbat − (realDARbatp − xDAR p ); Ωq
                                           bat
                                                            ← Rqbowl + (realDARbowl
                                                                                q    − xDARbowl
                                                                                           q    )
               (Bat)        (Bowl)
 8: return {Ωp         }, {Ωq        }


6     Results and discussions
This section documents the fitted framework on the entire dataset: the structure of the expected runs
model (Section 6.1), the distribution of RAE (Section 6.2), the state dependence of Dismissal Adjusted
Runs (Section 6.3), the correlation structure and convergent validity (Section 6.4), and the face-validity
leaderboards from an IPL case study (Section 6.5). All quantities are computed by the production esti-
mators of Sections 3-5.
6.1    Structure of the expected runs model
The grand mean is µ0 = 1.2425 runs per legal delivery. Table 3 summarises the seven fitted factors
and their shrinkage pseudo-counts; Table 4 reports the interpretable scenario, wicket and bowler-type
multipliers, and Figure 3 plots the era trend.
Finding 1 (Death overs premium, Powerplay discount). Conditional on all other factors, expected runs
in the Death overs run +18.8% (innings 1) and +13.2% (innings 2) above base, while the Powerplay sits
0-4% below base. The strike rate premium of the Powerplay visible in raw data is therefore largely a
phase artefact: because the scenario factor raises the Death overs bar, a run scored (or saved) there earns
proportionately less (or more) RAE than the same run in the lower-scoring Powerplay.

Finding 2 (Wicket pressure is phase-dependent). The wicket factor (Table 5) is sharp where deliveries are
plentiful and shrunk toward neutral where they are not. In the middle overs it declines almost monotonically
from 1.136 (0 down) to 0.657 (9 down), so each further wicket lowers cohort expected runs. The powerplay
shows the same early decline (1.047 → 0.716 across the first five wickets), while its deep-collapse cells (6
or more down inside the first six overs, a rare event) carry little information and are pulled back towards
1. The death overs invert the top of the gradient: one wicket down (1.164) scores above none (0.986),
                                                                                                                         15

                 Table 3: The fitted RAE factor model. Multiplier ranges for the low-
                 cardinality factors are over interpretable cell aggregates; for the high-cardinality
                 venue and opposition factors, they are raw shrunk-cell extrema. τf2 is the em-
                 pirical Bayes between-cell variance and κf = Var(r)/(µ20 τf2 ) the resulting data
                 estimated shrinkage pseudo-count (7). The batter and bowler factors are the
                 symmetric opposition multipliers of Section 3.4, applied one at a time.

               Factor (cell key)                       No. of cells    Multiplier range              τf2       κf
               Scenario (phase × innings)                          8       0.96 - 1.27         0.0093        180
               Era (year × phase)                                 69       0.96 - 1.14         0.0016      1,043
               Wicket (phase × wickets fallen)                    33       0.66 - 1.16         0.0034        485
               Bowler type (phase × sub-type)                     21       0.97 - 1.03         0.0013      1,249
               Venue (ground × 3-yr bucket)                    1,268       0.17 - 1.36         0.0054        311
               Opposition bowler (identity)                    7,282       0.77 - 1.18         0.0061        273
               Opposition batter (identity)                    9,740       0.50 - 1.87         0.0249         67
               Base rate µ0 = 1.2425 runs / legal ball; Var(r) = 2.578.


                 Table 4: Interpretable context multipliers. Values above 1 raise, and below 1
                 lower, the cohort expected runs relative to base.

                                    Scenario γ scen                        Bowler type γ type
                          Phase          Inns 1       Inns 2       Sub-type              Multiplier
                          Powerplay       0.959       0.999        Right-arm pace            1.028
                          Middle overs    0.968       0.975        Left-arm pace             0.998
                          Death overs     1.188       1.132        Leg-spin                  1.005
                                                                   Off-spin                  0.989
                                                                   Left-arm spin             0.968

                 Table 5: Wicket multiplier γ wkt by phase and number of wickets fallen. Values
                 above 1 raise, and below 1 lower, the cohort expected runs relative to base.

         Wickets fallen      0      1       2         3        4       5        6        7       8         9        10
         Powerplay         1.047 1.025 0.920 0.825 0.746 0.716 0.851 0.911 1.008 0.984   –
         Middle overs      1.136 1.081 1.036 0.988 0.938 0.889 0.840 0.770 0.735 0.657 0.977
         Death overs       0.986 1.164 1.150 1.117 1.083 1.028 0.975 0.895 0.824 0.692 0.751




                 Figure 3: The era multiplier γ era by year, shown separately for each match
                 phase together with the phase mean (dashed). Scoring conditions are broadly
                 stationary across the sample with a mild inflation in the most recent seasons.
                 The phase × innings scenario multipliers are listed exactly in Table 4.


consistent with a side that accelerates once a set batter falls, before the decline resumes. Banding the
counts averages this phase-dependent structure away, while conditioning on the exact count retains it, with
                                                                                                          16

the empirical Bayes shrinkage absorbing the sparse cells automatically.
Finding 3 (Pace is more expensive than spin). Averaged over phases, right-arm pacers concede the most
(1.028) and finger spinners the least (off-spin 0.989, left-arm spin 0.968), with left-arm pace (0.998) and
leg-spin (1.005) sitting near base: ≈ 6% expected runs gap between right-arm pace and left-arm finger spin,
absorbed by the bowler-type factor so that RAE neither rewards batters for merely facing more pace nor
penalises bowlers for bowling it.
6.2   Distribution of RAE
Figure 4 shows the ball-level and batter-level RAE distributions.




                 Figure 4: (a) Ball-level batter RAEb (truncated to [−3, 5] for display): a right-
                 skewed point-mass mixture centered at zero, the long right tail corresponding
                 to boundaries. (b) Batter-level RAEi for batters with ni ≥ 100; the dotted line
                 marks the cohort mean.

Remark 6 (The residual is centered). Across all 2,727,420 legal deliveries, the mean ball-level batter
residual is RAEb = −0.0001 runs, i.e. four orders of magnitude below the base rate µ0 = 1.2425, with
standard deviation 1.588 and right-skew 1.58; the bowler residual is likewise centered (−0.0005, s.d. 1.582).
This centering is a property of the converged fit, whose Poisson score identities (Remark 2) equate fitted
and observed totals within every context cell; the skew and excess mass at {−µ0 , 4, 6} reflect the discrete
run distribution rather than model misfit.
6.3   The wicket cost and restoration due to centering
Across all 147,797 bowler-credited dismissals in the dataset, the per-ball wicket cost c(s) evaluated at
the dismissal state averages 2.65 runs (median 2.56, 90th percentile 5.34). A dismissal, therefore, costs
a batting side, on average, only a couple of runs beyond the ball on which it falls, because most wickets
remove middling batters in the middle or late overs where the marginal cost of one more is small; the tail
of high-value dismissals (a set top-order batter removed early) reaches 15 runs. This spread is produced
entirely by the state: the value function assigns every wicket its own worth from the balls and wickets
remaining, the phase, the innings, and the quality of the batter dismissed and their partner.
   The cost is highest in the powerplay and roughly flat thereafter (Table 6). A powerplay dismissal costs
≈ 23% more than a death-overs dismissal does, because removing a batter early exposes the rest of the
order to more of the innings. The gradient is not monotone through the innings, however the middle overs
are the cheapest, and the death overs recover slightly because the few balls a late wicket forgoes are the
highest-scoring of the innings, an effect that partly offsets their small number.
Finding 4 (Wicket value is situational, not constant). No single ‘runs per wicket’ number describes the
data: the wicket cost ranges from near zero (a tail-ender removed on the last ball of a settled match) to
approximately 15.5 runs (a set top-order batter dismissed early), with a powerplay-to-death phase profile
of 3.10 → 2.52 runs (Table 6) and a further, orthogonal dependence on the quality of the batter dismissed.
This is the behaviour a run value of a wicket should have, and it is why the value function, rather than a
flat exchange rate, is required.
                                                                                                          17

                 Table 6: Mean wicket cost c(s) (runs) by over band, over all bowler-credited
                 dismissals. The cost is largest in the powerplay, dips through the middle overs,
                 and recovers marginally at the death, so it is not monotone in the balls remain-
                 ing.

           Over band           1-6 (Powerplay)     7-10 (Middle 1)    11-15 (Middle 2)    16-20 (Death)
           Mean c(s) (runs)          3.10                2.49               2.42               2.52


   The realised total of these costs is what a naive symmetric aggregate would debit each batter and
credit each bowler. Doing so is what breaks role comparability. Figure 5(a) shows the two Impact
distributions under the absolute construction RAE∓realDAR across qualifying IPL players (137 batters
                                               P

at ≥ 500 balls, 207 bowlers at ≥ 300 balls). On this subset of players, Batting Impact averages −193 runs
(median −159, maximum 210) while Bowling Impact averages +225 (median +123, maximum 1799). The
distributions barely overlap, and the ratio of the leading bowler to the leading batter is roughly 8.6 to 1.
   Subtracting the expected Dismissal Adjusted Runs (xDAR) removes the artefact. Panel (b) shows
the same players under the centered aggregate of (17)-(18): batting Impact now averages +144 (median
+87, maximum 1022) and bowling Impact −15 (median −34, maximum 924), so the two roles occupy a
common range around the origin and their leaders differ by less than 10%. The shift is not a rescaling but
a re-centering: an average bowler who takes the wickets his volume ordinarily yields, previously flattered
by a large positive wicket total, now sits near zero, while the strike bowlers who beat expectation stay
high.




                 Figure 5: Batting (blue) and bowling (red) ImpactP distributions over qualify-
                 ing IPL players. (a) The absolute construction      RAE ∓ realDAR places the
                 roles on disjoint ranges: a mean-zero run ledgerPcombined with a one-signed
                 wicket ledger. (b) The centered construction        RAE ∓ DAR returns both
                 roles to a shared, comparable scale about the origin. Densities; the vertical line
                 marks zero.

Finding 5 (Centering the wicket ledger restores role comparability). Pricing wickets in runs is necessary
but not sufficient for a comparable batting and bowling scale: realDAR is a one-signed accumulation,
and adding it to the mean-zero RAE leaves batters and bowlers on ranges that differ by nearly an order of
magnitude (Figure 5a). Subtracting each player’s xDAR, i.e. the martingale compensator of Proposition 2,
returns both roles to mean-zero residuals on one runs scale (Figure 5b), so that a batter’s and a bowler’s
Impact share a common centre as well as a common unit.
6.4   Correlation structure and convergent validity
Since the framework rests on two primitives, the natural validity checks are that (i) each primitive agrees
with the conventional statistic it is meant to context-adjust (convergent validity), and (ii) the two sources
of bowling value are distinct from each other (discriminant validity). Tables 7-8 report Pearson correlations
across qualifying IPL players (n = 137 batters at ≥ 500 balls, n = 207 bowlers at ≥ 300 balls).
                                                                                                                             18

                                                                         Table 8: Bowling Impact correlations
           Table 7: Batting Impact correlations
                                                                              Impact −RAE/Ball DAR/Ball Economy
                     Impact     RAE/Ball   Strike Rate
                                                              Impact            1.00
  Impact              1.00
                                                              −RAE/Ball         0.73       1.00
  RAE/Ball            0.65        1.00
                                                              DAR/Ball          0.13      0.09         1.00
  Strike Rate         0.54        0.82            1.00
                                                              Economy          −0.46      −0.68        −0.07          1.00


Finding 6 (RAE is essentially a context-adjusted run rate). RAE/Ball correlates 0.82 with the batter’s
raw strike rate and the bowler’s runs saved correlate −0.68 with economy. Each primitive tracks the
conventional rate it refines, confirming that RAE measures scoring rate or run-prevention rate. The
correlations are strong but far from one, and the gap is exactly the contextual adjustment (era, phase,
wicket pressure, venue, opposition) that any raw performance metric ignores. Batting Impact correlates
only 0.54 with strike rate, because it also carries the centered wicket ledger, through survival credit and
dismissal charge, which strike rate cannot see.
Finding 7 (Wicket-taking and run prevention are nearly orthogonal). On the bowling side, the two
value sources are almost uncorrelated. The net Dismissal Adjusted Runs per ball correlates only 0.09 with
runs saved per ball. Wicket-taking is therefore a separate dimension of bowling value, not a by-product
of containment: a miserly bowler need not be a strike bowler (e.g. Jasprit Bumrah), nor the reverse
(e.g. Arshdeep Singh). This justifies Bowling Impact carrying both terms in (18): economy alone (which
correlates −0.46 with Bowling Impact) would misjudge the wicket-hunters, and neither term subsumes the
other. The more modest correlation of net Dismissal Adjusted Runs with Bowling Impact itself (0.13) is a
direct consequence of centering. Once the expected haul is removed, most bowlers contribute little through
wickets, and the minority of strike bowlers does the separating.
6.5        Leaderboards based on the Indian Premier League
The framework’s rankings should recover cricketing consensus while remaining reproducible from the ball-
by-ball record. Among the 18 domestic and franchise leagues across Australia, Bangladesh, England, India,
Ireland, Nepal, New Zealand, Pakistan, South Africa, Sri Lanka and West Indies available in our dataset,
the Indian Premier League (IPL) records the largest sample size, with 295,629 deliveries (285,761 of them
legal) spanning 18 consecutive seasons (2008-2026), involving 769 batters and 603 bowlers.
   I report IPL leaderboards (2008-present) as the primary case study, both as per-ball rate and as cumu-
lative Impacts, and the two answer different questions (peak rate versus sustained contribution).

                      Table 9: Top batters in IPL sorted by (a) per-ball rate RAE/Ball; (b) cumu-
                      lative Bat Impact Ω(Bat) = RAE − DARbat (min 500 balls).
 (a) By RAE/Ball                                                            (b) By cumulative Bat Impact Ω(Bat)

 Rank       Batter              RAE/Ball   Runs          SR   Rank Batter               Ω(Bat) RAE realDAR xDAR Runs           SR
       1    Andre Russell          0.368   2651     175.5        1   AB de Villiers      1022   713     514     824   5162   151.9
       2    Virender Sehwag        0.341   2728     155.4        2   David Warner         911   540     762    1133   6565   139.6
       3    Sunil Narine           0.278   1820     165.2        3   Chris Gayle          891   684     568     775   4965   149.2
       4    Phil Salt              0.276   1258     175.7        4   KL Rahul             672   204     550    1017   5815   139.1
       5    Abhishek Sharma        0.271   2379     171.3        5   Andre Russell        667   543     333     457   2651   175.5
       6    Glenn Maxwell          0.257   2819     155.1        6   Suryakumar Yadav     619   424     460     655   4581   149.1
       7    Sanath Jayasuriya      0.238    768     144.4        7   MS Dhoni             601    68     535    1069   5439   137.5
       8    Travis Head            0.221   1556     170.1        8   Virat Kohli          601    11    1013    1604   9336   134.8
       9    Nicholas Pooran        0.215   2527     164.0        9   Suresh Raina         584   371     678     891   5528   136.7
      10    Tim David              0.210   1151     176.5       10   Jos Buttler          545   312     508     741   4646   149.7
      11    AB de Villiers         0.209   5162     151.9       11   Virender Sehwag      523   598     509     434   2728   155.4
      12    Chris Gayle            0.204   4965     149.2       12   Shane Watson         511   390     538     659   3874   138.0


   Reading Table 9(b) through its decomposition separates two distinct routes to a high Bat Impact. The
first is contextual run production. Virender Sehwag reaches 523 almost entirely through RAE (598, the
second largest in the table), and is the only batter in the table whose wicket ledger is a net charge: his
realised effect (realDAR = 509) exceeds its expectation (xDAR = 434), so being an attacking opener,
he was naturally dismissed more, and in higher-value states, than the league baseline predicts, a tax his
                                                                                                                           19

                    Table 10: Top bowlers in IPL sorted by (a) per-ball  run prevention
                    −RAE/Ball; (b) cumulative Bowl Impact Ω(Bowl) = − RAE+DARbowl (min
                                                                     P
                    300 balls).
             (a) By −RAE/Ball                                        (b) By cumulative Bowl Impact Ω(Bowl)

Rank Bowler                   −RAE/Ball Wkts Econ      Rank Bowler                  Ω(Bowl) −RAE realDAR xDAR Econ Wkts
    1   Matheesha Pathirana       0.292    47   7.73      1   Jasprit Bumrah           924   1049    750      875   7.07        187
    2   Jasprit Bumrah            0.286   187   7.07      2   Sunil Narine             802   1059    728      985   6.66        207
    3   Sunil Narine              0.227   207   6.66      3   Bhuvneshwar Kumar        621    858    878     1115   7.44        226
    4   Jofra Archer              0.217    84   7.78      4   Lasith Malinga           476    566    467      556   6.77        170
    5   Anil Kumble               0.200    45   6.38      5   Rashid Khan              430    520    701      790   7.17        179
    6   Lasith Malinga            0.199   170   6.77      6   Dale Steyn               307    395    296      384   6.61         97
    7   Glenn McGrath             0.192    12   6.52      7   Jofra Archer             296    345    371      419   7.78         84
    8   Bhuvneshwar Kumar         0.186   226   7.44      8   R. Ashwin                242    521    647      925   6.95        187
    9   Dale Steyn                0.180    97   6.61      9   M. Muralitharan          197    246    155      204   6.45         63
   10   M. Muralitharan           0.161    63   6.45     10   Varun Chakravarthy       176    180    454      458   7.39        111
   11   Lungi Ngidi               0.151    42   8.16     11   Matheesha Pathirana      175    208    154      188   7.73         47
   12   Rashid Khan               0.147   179   7.17     12   Anil Kumble              169    194    106      132   6.38         45



scoring more than repays. That a batter who last appeared in the IPL in 2015 still ranks this high follows
directly from the era factor γ era : his stroke-play is scored against the lower bar of his own pre-inflation
seasons rather than the high-scoring modern game, so he is neither flattered by a friendly era nor penalised
for having missed the recent run-glut. The second route is survival. Virat Kohli (RAE = 11) and MS
Dhoni (RAE = 68) add almost nothing above par per delivery, yet rank equal-seventh at 601, because
their wicket ledger is a large credit: the expected effect far exceeds the realised one (xDAR = 1604 against
realDAR = 1013 for Kohli, 1069 against 535 for Dhoni). Both figures are large because they scale with
deliveries faced, and Kohli has faced more than any batter in IPL history; their difference xDAR−realDAR
is the run value of the dismissals each avoided relative to an average batter over that volume, which a raw
wicket count cannot see. KL Rahul (672, credit 467) is the same anchor profile. AB de Villiers tops the
board by drawing on both routes at once, a large RAE (713) alongside a survival credit of 310.
   The bowling decomposition reads differently from a raw wicket count. Jasprit Bumrah and Sunil Narine
lead on elite containment, the two largest run-saved totals in the league (−RAE around 1050). Their
realised wicket hauls sit close to, but do not exceed, what their heavy volumes predict (realDAR = 750
against xDAR = 875 for Bumrah), so it is run prevention, not wicket-taking, that elevates them. One
thing the tables do not show directly: Yuzvendra Chahal took the most wickets of any bowler in IPL
(233, realDAR = 840), yet his expected haul over the same overs is almost identical (xDAR = 845), so he
nets nothing significant through wickets and ranks on his modest containment alone. R Ashwin shows the
sharper edge of the same mechanism: his realised wickets (647) fall well short of what his large volume
would ordinarily yield (925), so his standing rests on containment rather than strike. The pattern holds
across the table: once the expected haul is removed, the net wicket ledger is a modest, usually negative
adjustment, and it is run prevention that separates the leading bowlers, with the wicket channel penalising
those whose strike output lags their workload. Because Impact is a cumulative runs total, longevity still
contributes, but only through value added above expectation, not through the sheer number of balls
bowled.
   As a sharper face-validity test, I rank single innings by their batting Impact. Table 11 lists the top
knocks of IPL history sorted by their Batting Impacts. It recovers the canonical great innings, i.e. Chris
Gayle’s 175∗ (the highest score in T20 history till date) on top, followed by Brendon McCullum’s 158∗ in
the league opening match, and spans eras from 2008 to 2025 because RAE is measured against the scoring
conditions of each era.
   The innings ranking rewards contextual run value and survival rather than milestones, and this is
clearest among the knocks Table 11 leaves out. The most impactful sub-hundred score in IPL history
is Suresh Raina’s 87 from 25 balls against Kings XI Punjab in 2014 (Impact 56), almost at a level with
a few lower hundreds in and around the table, despite Raina facing barely a quarter of the deliveries.
Hardik Pandya’s 91 (34) and Rashid Khan’s 79∗ (32) reach the same Impact of 56. A twenty-five-ball
assault clears a far higher contextual bar than a measured hundred and the metric records it as such.
The costliest dismissals tell a different story: they are not the failures of tail-enders but the early falls
                                                                                                                                         20

                    Table 11: Most impactful individual IPL innings by batting Impact (innings
                    RAE − DARbat , in runs). Cost is the realised wicket value realDAR at the
                    dismissal, 0 for an unbeaten innings; Credit is the expected wicket value xDAR
                    accrued over the deliveries faced, the survival dividend.

     Rank       Batter               Opposition               Date     Runs      Balls     RAE       Cost      Credit       Impact
        1       Chris Gayle                 PWI        2013-04-23         175      66           76        0          15             91
        2       Brendon McCullum            RCB        2008-04-18         158      73           60        0          17             77
        3       Virender Sehwag              DC        2011-05-05         119      56           55        4          15             66
        4       AB de Villiers               GL        2016-05-14         129      52           53        0          11             64
        5       David Miller                RCB        2013-05-06         101      38           54        0           9             63
        6       Yusuf Pathan                 MI        2010-03-13         100      37           53        2          11             62
        7       David Warner                KKR        2017-04-30         126      59           52        3          13             62
        8       Priyansh Arya               CSK        2025-04-08         103      42           52        6          14             60
        9       AB de Villiers               MI        2015-05-10         133      59           46        0          13             59
       10       Andrew Symonds               RR        2008-04-24         117      53           45        0          13             58


of set or top-order batters in the powerplay, where the wicket value peaks. Travis Head’s 22 (12) cost
14 runs, the largest single-dismissal debit in the sample, and even the rare early failures of great players
surface here, with Chris Gayle’s 10 (10) and a sixteen-ball 16 from MS Dhoni each costing 12. The survival
dividend, finally, is largest for long unbeaten innings: Shikhar Dhawan’s 99∗ (66) earns a credit of 34 runs
and Dhoni’s 63∗ (45) earns a credit of 28, where the batters were repaid for carrying their wicket through
deliveries an average batter would not have survived.
   Aggregating Impact over an entire IPL season rather than a single innings gives a longer-run view of
contribution. Tables 12 and 13 list the most impactful batting and bowling seasons in IPL history, each
decomposed into its run and wicket components.

                    Table 12: Most impactful individual IPL batting seasons, by season Bat Im-
                    pact Ω(Bat) = RAE − (realDAR − xDAR) (minimum 150 balls faced).

            #   Batter               Team     Season    Runs         SR   RAE     RAE/B         realDAR       xDAR    Ω(Bat)
          1 Vaibhav Suryavanshi RR              2026      776    237.3     254       0.78            73         79         260
          2 Chris Gayle         RCB             2011      608    183.1     192       0.58            38         69         223
          3 Andre Russell       KKR             2019      511    204.4     170       0.68            32         82         220
          4 Chris Gayle         RCB             2012      733    160.7     158       0.35            49        109         218
          5 David Warner        SRH             2016      848    151.4     147       0.26            70        130         208
          6 Virat Kohli         RCB             2016      973    152.0     110       0.17            46        141         205
          7 AB de Villiers      RCB             2016      687    168.8     155       0.38            46         95         204
          8 Glenn Maxwell       KXIP            2014      552    187.8     194       0.66            63         65         196
          9 Rishabh Pant        DC              2018      684    173.6     157       0.40            54         89         192
         10 Chris Gayle         RCB             2013      720    156.9     112       0.24            57        107         163



                    Table 13: Most impactful individual IPL bowling seasons, by season Bowl
                    Impact Ω(Bowl) = −RAE + (realDAR − xDAR) (minimum 120 balls bowled).

        #   Bowler                 Team     Season   Wkts       Econ   −RAE      −RAE/B         realDAR       xDAR        Ω(Bowl)
        1 Jasprit Bumrah           MI        2024        20     6.08       159           0.51         86         83          162
        2 Sunil Narine             KKR       2013        25     5.42       152           0.40         61         66          148
        3 Jasprit Bumrah           MI        2025        19     6.57       141           0.50         76         71          146
        4 Sunil Narine             KKR       2012        26     5.37       130           0.37         67         53          144
        5 Jasprit Bumrah           MI        2019        20     6.48       158           0.42         66         85          139
        6 Bhuvneshwar Kumar        RCB       2026        29     7.73       106           0.28        151        119          138
        7 Rashid Khan              SRH       2020        20     5.27       138           0.36         73         79          132
        8 Mohammed Siraj           RCB       2023        19     6.81       114           0.38         88         80          123
        9 Sunil Narine             KKR       2026        16     6.60       138           0.45         61         76          123
       10 Lasith Malinga           MI        2011        29     5.61       107           0.28         83         71          119


  Season Impact rewards contextual efficiency over raw volume. The most impactful batting season in IPL
                                                                                                            21

history belongs not to the leading run-scorer but to Vaibhav Suryavanshi’s 776 runs at a strike rate of 237
in 2026 (Impact 260), whose per-ball value of 0.78 is much higher than that of Virat Kohli’s record 973-run
season in 2016 (Impact 205, per-ball value 0.17), which ranks only sixth. Several of the most impactful
seasons rest on modest aggregate returns, because what those runs were worth, ball for ball and situation
for situation, far outstripped a longer but flatter accumulation, for example, Andre Russell’s 511 runs in
2019 (Impact 220) and Glenn Maxwell’s 552 in 2014 (Impact 196). A few names recur, a sign of sustained
rather than one-off impact. Chris Gayle holds three of the 10 most impactful batting seasons (2011-2013)
and Jasprit Bumrah holds three of the top 10 bowling seasons, with Sunil Narine close behind. The two
routes to bowling value reappear at the season scale as well. Bumrah leads through elite containment at
an economy near 6, whereas Bhuvneshwar Kumar’s 2026 (29 wickets) is carried by a large wicket haul
despite a higher economy. Finally, the same players surface on both leaderboards: Narine ranks among
the most impactful bowling seasons and, as an opener, among the most valuable batting rates, and Pat
Cummins appears on both sides too, the mark of season-long all-round contribution.

7   Concluding remarks
The framework reduces T20 player evaluation to two ball-level primitives, both measured as runs above
expectation, and its strengths follow from that single design choice. RAE prices the runs on every delivery
against a contextual, likelihood-grounded expectation whose per-cell update is an exact conditional Poisson
maximum-likelihood multiplier (Proposition 1). The stratified, nonparametric baseline makes it robust to
playing conditions, phase and opposition without assuming any distribution for the lumpy, over-dispersed
run outcome, and a single opposition symmetry lets the same residual serve both batting and bowling.
Dismissal Adjusted Runs prices the runs at every dismissal through a batting-side value function and then
nets a player’s realised total against its hazard compensator, so the quantity that enters evaluation is
a run-weighted martingale residual, mean-zero by construction (Proposition 2). This centering is what
turns a shared unit into a shared scale. Both primitives become above-expectation residuals, so Bat
Impact = RAE − DARbat and Bowl Impact = − RAE + DARbowl are comparable in centre as well
           P                                           P

as in dimension (Finding 5), and a batter is charged for a dismissal only to the extent it exceeds what his
match situations warranted.
   Some further properties follow from the same construction. Empirical-Bayes shrinkage, applied both to
the factor multipliers of (4) and to the player rates feeding the value function, corrects the small-sample
bias that inflates naive averages, and the symmetric opposition factors remove any need for hand-set phase
weights, since difficulty is carried inside the expectation itself (Remark 1). Because Dismissal Adjusted
Runs is priced in the same unit as RAE, a bowler’s two separate sources of value (run prevention and
wicket-taking), near-orthogonal by Finding 7, combine additively with no weighting constant to defend,
and every wicket is valued on its own match state rather than by a flat exchange rate (Finding 4). Nothing
is tuned in the construction: the weight of a wicket relative to a run is a consequence of the value function
and the hazard baseline, not a parameter I set.
   The framework’s limitations point directly to its extensions. The expectation model treats delivery con-
text as exogenous to player identity, whereas in practice bowlers adjust line and length to specific batters;
a batter who forces bowlers into uncomfortable areas may carry a slightly deflated µ̂(xb ), and a structural
model of bowler strategy would address the resulting confounding. The second-innings value function con-
ditions on the innings alone, capturing average chase behaviour through innings-specific transition models
but not the live required run rate; a finer chase state, valuing runs and wickets against the current target
in the spirit of the Pressure Index of Bandyopadhyay and Bhattacharjee (2026), is a natural refinement.
The value function itself tracks batter quality by discrete tiers and treats every dismissal as the striker’s,
so run-outs of the non-striker, finer within-tier heterogeneity and a full ball-by-ball settling model are left
aside, though these are secondary to the state variables that dominate a wicket’s worth. On the input
side, RAE uses only always-available fields so that every match is scored identically; the line, length and
stroke-geometry data present for a minority of deliveries could sharpen the expected runs model on the
annotated subset, at the cost of comparability across the dataset. This extended RAE model, together
with the evidence for adopting line and length as the additional covariates and for confining the extension
to batting, is developed in Section S2 in the supplementary materials.
                                                                                                              22

   Two choices shape how the numbers should be read. The expected DAR uses a league dismissal hazard
h̄φ,e conditioned on phase and innings only; the coarseness is deliberate, since a context-level baseline lets
batting skill surface as survival above the league rate rather than being absorbed into a player-specific
expectation, but it leaves the survival credit indifferent to finer state such as the wicket count or the tier of
the batter at the crease. Conditioning h̄ on the richer state the value function already tracks would sharpen
the compensator, at the cost of moving the baseline closer to the player and diluting the skill signal it is
meant to expose; where to set that resolution is a modelling choice I leave open. A related consequence
is that cumulative Impact is longevity-aware by construction. Both the run value and the survival credit
accumulate with volume, so a durable accumulator can top the cumulative board on sustained competence
while the per-ball rate isolates peak quality, and the two are meant to be read together. Finally, because
both primitives are defined relative to the average player in the chosen data slice, cross-competition
comparisons inherit a system-wide competition-strength discrepancy, and a standard-adjusted baseline is
planned.

Data availability statement
The data used in this research have been obtained from three sources: baseline ball-by-ball data from
the Cricsheet website (link: https://cricsheet.org/matches/), granular ball-by-ball data from Dr. Hi-
manish Ganjoo’s collection of cricket data (link: https://himanishganjoo.com/cricket-data/) with his au-
thorization and assistance, and hawk-eye ball-tracking data for IPL 2026 from the IPL website (link:
https://www.iplt20.com/matches/results). The cleaned data, along with all relevant Python code and
other files, will be made publicly available in the author’s GitHub repository.

References
Bandyopadhyay, R. and Bhattacharjee, D. (2026). Applications of higher order markov models and pressure
  index to strategize controlled run chases in twenty20 cricket. International Journal of Sports Science &
  Coaching, page 17479541261430809.

Barlow, W. E. and Prentice, R. L. (1988). Residuals for relative risk regression. Biometrika, 75(1):65–74.

Baumer, B. S., Jensen, S. T., and Matthews, G. J. (2015). openWAR: An open source system for evalu-
  ating overall player performance in Major League Baseball. Journal of Quantitative Analysis in Sports,
  11(2):69–84.

Brooker, S. and Hogan, S. (2011). A method for inferring batting conditions in ODI cricket from historical
  data. Technical report, Department of Economics and Finance, University of Canterbury. Working
  paper; statistical basis of the WASP win-and-score predictor.

Cervone, D., D’Amour, A., Bornn, L., and Goldsberry, K. (2016). A multiresolution stochastic process
  model for predicting basketball possession outcomes. Journal of the American Statistical Association,
  111(514):585–599.

Clarke, S. R. (1988). Dynamic programming in one-day cricket—optimal scoring rates. Journal of the
  Operational Research Society, 39(4):331–337.

Davis, J., Perera, H., and Swartz, T. B. (2015a). Player evaluation in Twenty20 cricket. Journal of Sports
 Analytics, 1(1):19–31.

Davis, J., Perera, H., and Swartz, T. B. (2015b). A simulator for Twenty20 cricket. Australian & New
 Zealand Journal of Statistics, 57(1):55–71.

Decroos, T., Bransen, L., Van Haaren, J., and Davis, J. (2019). Actions speak louder than goals: Valu-
  ing player actions in soccer. In Proceedings of the 25th ACM SIGKDD International Conference on
  Knowledge Discovery and Data Mining, pages 1851–1861.

DerSimonian, R. and Laird, N. (1986). Meta-analysis in clinical trials. Controlled Clinical Trials, 7(3):177–
  188.
                                                                                                           23

Duckworth, F. C. and Lewis, A. J. (1998). A fair method for resetting the target in interrupted one-day
 cricket matches. Journal of the Operational Research Society, 49(3):220–227.

Lemmer, H. H. (2004). A measure for the batting performance of cricket players. South African Journal
  for Research in Sport, Physical Education and Recreation, 26(1):55–64.

Lindsey, G. R. (1963). An investigation of strategies in baseball. Operations Research, 11(4):477–501.

Preston, I. and Thomas, J. (2000). Batting strategy in limited overs cricket. Journal of the Royal Statistical
  Society, Series D, 49(1):95–106.

Stevenson, O. G. and Brewer, B. J. (2021). Modelling the evolution of batting strategies in Twenty20
  cricket. Journal of the Royal Statistical Society, Series C, 70(4):770–793.

Therneau, T. M., Grambsch, P. M., and Fleming, T. R. (1990). Martingale-based residuals for survival
 models. Biometrika, 77(1):147–160.
                                                                                                               24

                                    Supplementary materials


S1     Model specification for reproducibility
This section records the fitted values of every quantity the estimators of Sections 3–4 produce, so that
the numbers reported in the paper can be reproduced exactly. Unless stated otherwise, each quantity is
estimated on the full dataset of 2,727,420 legal deliveries of Section 2. The estimators themselves, i.e.
the shrunk backfitting for RAE and the tiering, transition model, and backward recursion for Dismissal
Adjusted Runs, are given in the main text and are not repeated. The three high-cardinality RAE factors
(venue and the two opposition identities, with 1,268, 7,282, and 9,740 cells) are too numerous to list; each
is estimated by the shrinkage rule (4) and its fitted extrema appear in Table 3.
S1.1    Global constants and fixed hyperparameters
Every tuning quantity in the framework is either estimated from the data or fixed at a value stated here;
there are no hand-set weights. Table S1 collects the fixed constants. The per-factor RAE shrinkage
strengths κf are themselves data-estimated by empirical Bayes and are reported with the factor model in
Table 3.
                             Table S1: Global constants and fixed hyperparameters.

        Symbol              Value              Meaning
        µ0                  1.2425             grand mean runs per legal ball
        Var(r)              2.578              run variance (overdispersion scale)
        Q                   6                  batter quality tiers
        M0                  120                legal balls in a T20 innings
        phases              3                  powerplay (≤ over 6), middle (7–15), death (16–20)
        Emax                6                  cap on the freshness horizon in (13)
        venue window        3 years            bucket width for the venue factor
        κµ                  60                 EB pseudo-count for the batter scoring rate µi (11)
        κη                  40                 EB pseudo-count for the hazard ηi and for hi,φ,e
        κπ                  200                Dirichlet pseudo-count pooling πr|i,φ,e toward its phase mean
        strike-share clip   [0.25, 0.75]       bounds on the crease-window strike share si
        κf                  data-estimated     per-factor RAE shrinkage (Table 3)


S1.2    Expected-runs factor estimates
The scenario and bowler-type multipliers appear in Table 4 and the wicket factor in Table 5. Two further
pieces complete the specification of the interpretable factors. The bowler-type factor is resolved by phase
in Table S2 (Table 4 reports its phase average). The era factor, plotted in Figure 3, is listed in full by year
and phase in Table S3.

                     Table S2: Bowler-type multiplier γ type by phase and bowling sub-type.

                                    Sub-type          Powerplay    Middle   Death
                                    Right-arm pace       1.016      1.025    1.033
                                    Left-arm pace        0.951      1.026    1.007
                                    Leg-spin             1.056      0.998    0.950
                                    Off-spin             1.005      0.988    0.961
                                    Left-arm spin        0.988      0.951    0.953
                                    Other                0.990      1.001    1.009
                                    Unknown              0.958      0.985    1.011
                                                                                                         25

                   Table S3: Era multiplier γ era by year and phase, with the phase means.

                                      Year     Powerplay     Middle      Death         Mean
                                      2005       1.015        1.007       1.014        1.012
                                      2006       0.994        0.985       0.995        0.991
                                      2007       1.016        1.050       1.020        1.029
                                      2008       0.988        0.991       1.005        0.995
                                      2009       1.027        0.962       1.003        0.997
                                      2010       0.995        1.002       1.030        1.009
                                      2011       0.981        0.993       0.972        0.982
                                      2012       0.992        1.005       1.007        1.001
                                      2013       0.981        0.994       1.030        1.002
                                      2014       1.023        1.020       1.022        1.022
                                      2015       0.969        0.983       1.008        0.987
                                      2016       0.963        0.991       0.995        0.983
                                      2017       1.039        1.004       0.997        1.013
                                      2018       1.034        1.027       1.003        1.021
                                      2019       0.995        1.006       0.993        0.998
                                      2020       0.984        1.005       1.012        1.000
                                      2021       0.979        0.993       1.014        0.995
                                      2022       0.969        0.998       1.004        0.990
                                      2023       1.004        1.026       1.021        1.017
                                      2024       1.016        1.019       1.023        1.019
                                      2025       1.060        1.066       1.042        1.056
                                      2026       1.137        1.068       1.028        1.078


S1.3   Value-function transition model
The batting-side value function Ve of Section 4.1 is fully determined by the quality tiers (Table S4), the
per-state dismissal hazard hi,φ,e (Table S5) and scoring distribution πr|i,φ,e (Tables S6–S7), the incoming-
batter tier ι(w) (the observed average batting order of Section 4.2), and the set curve f (k) (Table S8).
Given these inputs, a single backward sweep of the recursion (9) reproduces Ve exactly.

                 Table S4: Quality tiers. A batter is assigned to a tier by his empirical Bayes
                 shrunk scoring rate µi falling in the stated range; the tier’s ball-weighted mean
                 rate µ̄ and mean hazard η̄ index the transition tables below.

                               Tier    µi range (runs/ball)         µ̄          η̄       #batters
                               0            µi < 1.016          0.920         0.0268          1,373
                               1        1.016 ≤ µi < 1.103      1.062         0.0273          1,669
                               2        1.103 ≤ µi < 1.171      1.140         0.0250          2,011
                               3        1.171 ≤ µi < 1.241      1.208         0.0230          2,402
                               4        1.241 ≤ µi < 1.333      1.285         0.0218          1,342
                               5            µi ≥ 1.333          1.419         0.0244           943



                 Table S5: Per-state dismissal hazard rate hi,φ,e (probability of a dismissal on
                 a legal ball) by tier i, phase φ and innings e.

                                               Innings 1                        Innings 2
                           Tier        PP        Mid       Death         PP           Mid       Death
                           0          0.0527    0.0590     0.1105     0.0539         0.0625     0.1030
                           1          0.0503    0.0535     0.1028     0.0523         0.0565     0.1011
                           2          0.0473    0.0485     0.0978     0.0507         0.0538     0.0922
                           3          0.0435    0.0448     0.0910     0.0458         0.0488     0.0875
                           4          0.0421    0.0446     0.0861     0.0435         0.0462     0.0796
                           5          0.0443    0.0461     0.0823     0.0481         0.0489     0.0812
                                                                                                             26

                    Table S6: Scoring distribution πr|i,φ,e in first innings, by tier and phase.
                            Tier   Phase     0        1       2      3       4       6
                            0      PP       0.620   0.242   0.050   0.005   0.075   0.008
                            0      Mid      0.510   0.371   0.061   0.003   0.044   0.012
                            0      Death    0.448   0.383   0.085   0.005   0.057   0.021
                            1      PP       0.553   0.265   0.050   0.006   0.108   0.017
                            1      Mid      0.421   0.431   0.065   0.003   0.058   0.021
                            1      Death    0.384   0.404   0.091   0.005   0.078   0.037
                            2      PP       0.526   0.270   0.050   0.006   0.126   0.022
                            2      Mid      0.374   0.453   0.071   0.004   0.069   0.029
                            2      Death    0.348   0.403   0.098   0.004   0.095   0.051
                            3      PP       0.502   0.278   0.050   0.006   0.138   0.026
                            3      Mid      0.340   0.468   0.074   0.004   0.078   0.036
                            3      Death    0.304   0.410   0.105   0.004   0.109   0.067
                            4      PP       0.478   0.284   0.049   0.006   0.149   0.034
                            4      Mid      0.321   0.473   0.073   0.004   0.086   0.043
                            4      Death    0.283   0.401   0.108   0.004   0.120   0.083
                            5      PP       0.460   0.271   0.049   0.006   0.163   0.051
                            5      Mid      0.318   0.454   0.071   0.003   0.092   0.063
                            5      Death    0.282   0.374   0.105   0.003   0.126   0.110



                  Table S7: Scoring distribution πr|i,φ,e in second innings, by tier and phase.
                            Tier   Phase     0        1       2      3       4       6
                            0      PP       0.622   0.235   0.046   0.005   0.081   0.011
                            0      Mid      0.516   0.363   0.060   0.002   0.045   0.014
                            0      Death    0.501   0.354   0.066   0.003   0.055   0.020
                            1      PP       0.544   0.270   0.049   0.005   0.114   0.019
                            1      Mid      0.429   0.420   0.064   0.004   0.061   0.022
                            1      Death    0.419   0.392   0.075   0.004   0.076   0.034
                            2      PP       0.519   0.276   0.048   0.005   0.127   0.025
                            2      Mid      0.392   0.441   0.065   0.003   0.069   0.030
                            2      Death    0.380   0.391   0.084   0.005   0.094   0.045
                            3      PP       0.493   0.282   0.049   0.006   0.140   0.030
                            3      Mid      0.359   0.454   0.071   0.003   0.078   0.036
                            3      Death    0.338   0.405   0.092   0.003   0.104   0.058
                            4      PP       0.472   0.283   0.048   0.005   0.152   0.039
                            4      Mid      0.334   0.461   0.072   0.004   0.088   0.042
                            4      Death    0.312   0.395   0.098   0.003   0.119   0.072
                            5      PP       0.456   0.263   0.049   0.005   0.168   0.058
                            5      Mid      0.328   0.440   0.070   0.003   0.094   0.065
                            5      Death    0.309   0.373   0.092   0.003   0.122   0.101



                  Table S8: The set curve f (k): the fraction of the settled scoring rate realised
                  over a batter’s first k deliveries, used in the freshness term (13).

          k         1       2       3       4        5       6        8      10       15     20       30
          f (k)   0.623   0.688    0.734   0.771    0.802   0.830   0.876   0.912   0.970   1.003    1.042


   The centered Dismissal Adjusted Runs additionally uses the league dismissal hazard h̄φ,e . Table S9
gives it, and also reports how the hazard varies across the major T20 leagues. The assembly of Impact
then follows Algorithm 2.
                                                                                                         27

                 Table S9: Empirical dismissal hazard h̄φ,e (probability of a dismissal on a
                 legal ball) by phase and innings, within each of ten major T20 leagues and
                 pooled over the full dataset. The pooled values (final block) are the baseline
                 h̄φ,e that centers Dismissal Adjusted Runs (Section 4).

                     League                        Innings   Powerplay    Middle    Death
                                                   1           0.0386     0.0417   0.0844
                     Indian Premier League
                                                   2           0.0415     0.0446   0.0820
                                                   1           0.0414     0.0441   0.0904
                     Big Bash League
                                                   2           0.0451     0.0489   0.0871
                                                   1           0.0440     0.0444   0.0899
                     Caribbean Premier League
                                                   2           0.0457     0.0497   0.0833
                                                   1           0.0387     0.0465   0.0916
                     Pakistan Super League
                                                   2           0.0457     0.0487   0.0904
                                                   1           0.0474     0.0448   0.0837
                     SA20
                                                   2           0.0466     0.0547   0.0927
                                                   1           0.0513     0.0429   0.0860
                     Major League Cricket
                                                   2           0.0464     0.0562   0.0798
                                                   1           0.0454     0.0446   0.0911
                     Syed Mushtaq Ali Trophy
                                                   2           0.0425     0.0450   0.0820
                                                   1           0.0446     0.0483   0.0884
                     Super Smash
                                                   2           0.0519     0.0519   0.0868
                                                   1           0.0478     0.0486   0.0941
                     Lanka Premier League
                                                   2           0.0528     0.0512   0.0845
                                                   1           0.0445     0.0461   0.0886
                     T20 Blast
                                                   2           0.0470     0.0505   0.0886
                                                   1           0.0448     0.0471   0.0905
                     Full dataset
                                                   2           0.0475     0.0502   0.0876


S2     Extending RAE with ball-tracking covariates
The RAE model of Section 3 conditions only on covariates recorded for every delivery in our dataset,
so that it applies identically to every match and keeps players comparable across eras and conditions.
That choice is deliberate, but it leaves information unused: a boundary struck off a yorker is a finer piece
of batting than the same boundary off a half-volley, yet the baseline model, blind to the delivery’s line
and length, scores the two alike. Where ball-tracking data exist, we can refine the expectation to the
exact delivery faced, and so isolate a batter’s shot-production more sharply. This section develops that
refinement, measures how much it moves the evaluation, and says why we keep it out of the headline
metric and apply it to batting only.
   To keep the two metrics separate we name them distinctly. We write pRAE (primary RAE) for the metric
of the main paper and mRAE (modified RAE) for the extension. pRAE is the residual rb − µ(xb ) against
the expectation built from fields recorded for every delivery (Equation (1)), while mRAE is the residual
against an expectation that additionally conditions on the delivery’s line and length. The availability of
these two data tiers is described in Section 2. Because the two use different covariate sets and, since
tracking is partial, are defined on different samples, the distinct notation guards against conflating a
player’s pRAE (over all his deliveries) with his mRAE (over his tracked deliveries only).
S2.1    Ball-tracking data: covariates and coverage
The ball-tracking tier records two kinds of variable. Delivery variables describe the ball the bowler sent
down, before the batter played it: its length (Yorker, Full Toss, Half Volley, Good Length, Back of Length,
Short, Bouncer), its line (On Stumps, Outside Off, Down Leg and their wide variants), and the bowler’s
variation. Response variables describe what the batter then did: whether the shot was controlled, the
                                                                                                                 28

stroke played, its elevation, and the area to which the ball went. Only the delivery variables are candidates
for an expected-runs model, for the reason given in Section S2.2.
   Coverage is partial and uneven across competitions (Table S10). Line and length are present for about
one-third of all legal deliveries in men’s T20 matches and only a quarter of men’s T20 internationals, but
for a majority of the well-resourced franchise leagues: 57% of the IPL, 66% of the Big Bash and around
three quarters of the CPL and SA20 in our dataset carry ball-tracking data, while some competitions are
barely tracked. Coverage is also patchy within a competition: the T20 Blast carries length for one-third of
its deliveries but line for almost none. This heterogeneity is exactly why line and length cannot enter the
headline metric, at least until ball-tracking data become publicly available across the board. A residual
built on them would be defined on an unpredictable, competition-dependent subset and would not be
comparable across matches, so the extension below is a refinement available wherever tracking exists, and
it sits alongside pRAE rather than taking its place.

                 Table S10: Ball-tracking coverage: percentage of legal deliveries carrying each
                 covariate, overall, for men’s internationals, and for the major franchise leagues.

                Competition                    Legal balls      Length    Line    Control   Shot type
                Overall (all data)                 2,727,420      33.9    29.5     39.7           16.5
                Men’s internationals               1,213,059      25.2    24.2     25.4           12.4
                Indian Premier League               285,761       57.1    57.0     57.1           32.3
                Big Bash League                     147,955       65.5    65.5     65.4           49.6
                Caribbean Premier League             90,866       75.7    75.7     75.7           22.6
                Pakistan Super League                81,037       60.8    60.8     60.9            0.0
                SA20                                 28,048       75.5    75.5     75.4            0.0
                T20 Blast                           324,920       33.7     0.4     82.1           33.2
                Syed Mushtaq Ali Trophy             154,361        6.4     6.4      6.4            0.0
                Super Smash                          59,327       15.1    15.1     15.0            0.0


S2.2   Choosing the covariates
An expected runs model may condition only on what is known before the outcome of a ball, which rules
out the response variables at once. Conditioning expected runs on whether a shot was controlled, or on
where the ball was hit, would fold the outcome into its own expectation and explain away the run-scoring
the residual is meant to capture. The objection is not only a conceptual one. Table S11 fits each candidate
as a single phase-conditioned factor on top of the baseline expectation and reports its between-cell signal
τ 2 , its data-estimated shrinkage κ, and the fraction of residual sum of squares it removes (∆RSS). The
response variables carry by far the largest apparent signal. Shot area alone removes 20% of the residual
variance, with a multiplier range from 0.02 to 1.75, because they are proxies for the result: a ball hit to the
boundary explains its four runs tautologically. Admitting them would be circular, so they are excluded
despite, indeed because of, their apparent significance.

                 Table S11: Significance of candidate additional covariates, each fitted as a
                 single phase-conditioned factor on top of the baseline expectation. ∆RSS is the
                 percentage of residual sum of squares the factor removes on its own coverage
                 subset. Response variables are post-outcome and are excluded from the model
                 despite their large apparent signal (see text).

          Covariate    Role       Coverage (%)       Cells     Multiplier range       τ2     κ      ∆RSS (%)
          Length       delivery             33.9        21        0.51–1.44       0.0455     37           2.61
          Line         delivery             29.5        21        0.93–1.18       0.0038    437           0.20
          Variation    delivery             16.5        39        0.53–1.08       0.0061    272           0.32
          Control      response             39.7        15        0.01–1.17       0.1282    13            6.47
          Shot type    response             16.5        71        0.06–1.58       0.1646    10           10.24
          Shot area    response             16.1        48        0.02–1.75       0.3164     5           19.93


  Among the admissible delivery variables, length is by far the most informative: it removes 2.6% of
                                                                                                          29

the residual variance with a multiplier ranging from 0.49 on a yorker to 1.46 on a short ball. Line is
comparatively weak (0.2%, almost all of it in the wide categories), and the bowler’s variation weak too
(0.3%) and poorly covered. Adding line to length lifts the removed variance from 2.63% to 2.74%, and
adding variation to 2.86%. The marginal gains beyond length are small, and variation’s low coverage
would further shrink the tracked sample. We therefore adopt ‘line and length’ as the additional covariates
to formulate mRAE.
S2.3   The modified expected runs model
The extension is a strict addition to the multiplicative model (1), not a new mechanism. On the tracked
subset we append two factors,
                                      µ̃(xb ) = µ(xb ) γ(φ,
                                                        len        lin
                                                            ℓ(b)) γ(φ, λ(b)) ,                     (S1)
where ℓ(b) and λ(b) are the length and line of delivery b, each factor is phase-conditioned like the others,
and γ len , γ lin are estimated by the same iterated, empirical Bayes shrunk backfitting of Sections 3.2-3.3,
holding the baseline expectation µ(xb ) as the offset. The modified and primary residuals are then

                           mRAEb = rb − µ̃(xb ),           pRAEb = rb − µ(xb ).                         (S2)

The fitted multipliers (Table S12) line up with cricketing intuition. A yorker is worth about half an average
ball and a short ball about half again as much, while line matters only through width, down the leg side
or wide outside off. Because length dominates, mRAE is in effect a length adjustment, raising the bar on
deliveries that are easy to score off and lowering it on the hardest.

                       Table S12: Fitted length and line multipliers (phase-averaged).

                            Length           γ len      Line                 γ lin
                            Yorker           0.490      Off Stump           0.973
                            Bouncer          0.607      Leg Stump           0.982
                            Good Length      0.880      Outside Off         0.986
                            Back of Length   0.970      On Stumps           0.988
                            Half Volley      1.188      Down Leg            1.013
                            Full Toss        1.320      Wide Down Leg       1.042
                            Short            1.460      Wide Outside Off    1.118


   Line and length occupy opposite roles for the two sides of a delivery. For the batter, they provide
context: the ball he had to deal with and did not choose, so conditioning on them isolates his shot-making
given the delivery. For the bowler, they measure skill: bowling a yorker or hitting a hard length is the act
by which he suppresses scoring, so conditioning a bowler’s residual on his own line and length subtracts
out his main contribution, just as conditioning a batter’s residual on his own shot selection would. The
distinction mirrors the opposition factor asymmetry already in the model (Section 3.4), where a batter
is credited against the bowler he faced and a bowler against the batter he faced, never against his own
quality.
   Applied to batters, the extension leaves the ranking essentially intact: across the 107 qualifying IPL
batters (≥ 400 tracked balls) the pRAE and mRAE per-ball rates correlate 0.984, with Spearman rank cor-
relation 0.97. Applied to bowlers, conditioning on their own line and length degrades the ranking markedly
(Spearman 0.83) and moves it in the wrong direction. The bowlers who lose most are the ones whose value
is their length and line control: Rashid Khan (+0.170 → +0.118 runs saved per ball), Bhuvneshwar Kumar
(+0.178 → +0.117), Sunil Narine (+0.168 → +0.099) and Mitchell Santner (+0.139 → +0.078), since the
model now treats the ‘hard to score’ deliveries they bowl as the expected state of affairs rather than their
achievement. We therefore define mRAE for batters only.
S2.4   Primary RAE versus modified RAE
Ball tracking is available in the IPL only from the 2015 season onward, so every leaderboard in this
subsection is computed on the tracked deliveries of the 2015–2025 seasons, and each player’s runs, balls,
strike rate, wickets and economy are likewise measured over those tracked deliveries alone, so that pRAE
                                                                                                                   30

and mRAE are compared on exactly the same balls. Each table is ordered by the modified metric, and
we report two ranks: the ‘mRank’ is the player’s position under mRAE and the ‘pRank’ is the position he
would have held under pRAE on the same balls. The gap between the two is the clearest single summary
of what the tracking refinement changes.

                   Table S13: Top IPL batters by mRAE per ball on the tracked subset (2015–
                   2025, ≥ 400 tracked balls), with pRAE per ball on the same balls, the two
                   ranks, the change ∆ = mRAE − pRAE, and runs, balls and strike rate over the
                   tracked deliveries.
           mRank       Batter             mRAE/Ball      pRAE/Ball   pRank          ∆   Runs    Balls     SR
                   1   Andre Russell            0.321        0.375        1    −0.054   2,588   1,475   175.5
                   2   AB de Villiers           0.249        0.270        5    −0.021   3,102   1,919   161.6
                   3   Nicholas Pooran          0.220        0.272        4    −0.052   2,293   1,357   169.0
                   4   Phil Salt                0.215        0.272        3    −0.057   1,056     600   176.0
                   5   Heinrich Klaasen         0.204        0.235        7    −0.031   1,480     872   169.7
                   6   Pat Cummins              0.192        0.205       10    −0.013     612     402   152.2
                   7   Travis Head              0.186        0.245        6    −0.059   1,146     674   170.0
                   8   Sunil Narine             0.179        0.310        2    −0.131   1,733   1,028   168.6
                   9   Abhishek Sharma          0.176        0.218        8    −0.042   1,816   1,114   163.0
                  10   Liam Livingstone         0.165        0.209        9    −0.044   1,051     662   158.8
                  11   Glenn Maxwell            0.161        0.185       12    −0.024   2,223   1,482   150.0
                  12   Prithvi Shaw             0.146        0.161       14    −0.015   1,884   1,280   147.2
                  13   Suryakumar Yadav         0.132        0.152       16    −0.020   4,140   2,776   149.1
                  14   Shashank Singh           0.128        0.157       15    −0.029     773     490   157.8
                  15   Rajat Patidar            0.128        0.129       21    −0.001   1,111     720   154.3



                   Table S14: Top IPL bowlers by −mRAE per ball (runs saved) on the tracked
                   subset (2015–2025, ≥ 300 tracked balls), shown only to demonstrate the failure
                   of the extension on bowling (Section S2.3).
         mRank     Bowler                 −mRAE/Ball     −pRAE/Ball     pRank           ∆   Wkts   Econ    Balls
              1    Matheesha Pathirana           0.311          0.301          1   +0.010     49   7.66     682
              2    Jasprit Bumrah                0.293          0.298          2   −0.005    190   6.93   3,086
              3    Jofra Archer                  0.291          0.257          3   +0.034     60   7.49   1,228
              4    Chris Morris                  0.160          0.117         11   +0.043     86   7.69   1,420
              5    Harshal Patel                 0.150          0.080         19   +0.070    155   8.37   2,129
              6    Andrew Tye                    0.137          0.113         12   +0.024     48   8.25     684
              7    Nathan Ellis                  0.136          0.142          8   −0.006     20   8.44     381
              8    Prasidh Krishna               0.135          0.102         14   +0.033     79   8.32   1,516
              9    Mitchell Marsh                0.135          0.079         20   +0.056     21   8.10     300
             10    Nathan Coulter-Nile           0.131          0.079         21   +0.052     49   7.49     815
             11    Lasith Malinga                0.130          0.098         15   +0.032     53   8.08     904
             12    Morne Morkel                  0.121          0.058         28   +0.063     22   7.70     384
             13    Mohammed Siraj                0.120          0.105         13   +0.015    112   8.25   2,307
             14    Rashid Khan                   0.119          0.171          6   −0.052    166   6.96   3,156
             15    Bhuvneshwar Kumar             0.117          0.178          4   −0.061    165   7.71   3,260


Per-ball rates. Among batters (Table S13), the ordering holds broadly but reshuffles underneath. AB
de Villiers rises from pRank 5 to second under mRAE, while Sunil Narine falls from pRank 2 to mRank
8, the sharpest mover, because much of his scoring comes off short and wide balls the refined model now
expects runs from. The bowler table (Table S14) is the evidence, as mentioned in Section S2.3, that the
same refinement must not be applied to bowling. Conditioning a bowler’s residual on his own line and
length lifts almost every bowler’s apparent run prevention. Harshal Patel jumps from pRank 19 to mRank
5, and Chris Morris and Morne Morkel climb similarly, while the elite suppressors fall. Rashid Khan slides
from pRank 6 to mRank 14 and Bhuvneshwar Kumar from pRank 4 to mRank 15, because the hard
lengths that are their skill now count as par. The resulting order does not describe bowling quality.
                                                                                                         31

Cumulative and season totals. The cumulative and per-season orderings tell the same story on the
batting side, where they are meaningful. Over careers, (Table S15) de Villiers and Russell trade the top
two places and Narine slides from pRank 8 to mRank 12. By season, (Table S17) Russell’s 2019 and de
Villiers’s 2016 remain the most valuable tracked campaigns under either metric. The bowling cumulative
and season tables (Tables S16 and S18) are included for completeness and show the same distortion as
the rates: Bumrah, whose value is as much containment as length, is the one elite name to hold the top;
Bhuvneshwar and Rashid each shed about 200 runs of apparent value, and Bumrah alone accounts for
four of the ten most valuable bowling seasons.

                 Table S15: Top IPL batters by cumulative mRAE (tracked deliveries, 2015–
                 2025, ≥ 400 balls), with cumulative pRAE on the same balls.
                 mRank   Batter             mRAE      pRAE   pRank        ∆   Runs    Balls     SR
                       1 AB de Villiers        479     517       2  −38       3,102   1,919   161.6
                       2 Andre Russell         474     554       1  −80       2,588   1,475   175.5
                       3 Suryakumar Yadav      367     422       3  −55       4,140   2,776   149.1
                       4 Jos Buttler           311     331       7  −20       4,119   2,756   149.5
                       5 Rishabh Pant          299     357       5  −58       3,546   2,401   147.7
                       6 Nicholas Pooran       298     369       4  −71       2,293   1,357   169.0
                       7 Sanju Samson          260     257      10   +3       4,156   2,929   141.9
                       8 Glenn Maxwell         238     274       9  −36       2,223   1,482   150.0
                       9 David Warner          238     332       6  −94       4,597   3,243   141.8
                      10 Abhishek Sharma       196     243      11  −47       1,816   1,114   163.0
                      11 Prithvi Shaw          187     207      12  −19       1,884   1,280   147.2
                      12 Sunil Narine          185     318       8 −134       1,733   1,028   168.6



                 Table S16: Top IPL bowlers by cumulative −mRAE (runs saved; tracked
                 deliveries, 2015–2025, ≥ 300 balls), with −pRAE on the same balls. Included
                 for completeness only (Section S2.3). ∆ = (−mRAE) − (−pRAE).
              mRank    Bowler               −mRAE     −pRAE    pRank          ∆   Wkts   Econ    Balls
                   1 Jasprit Bumrah             903      920          1    −17     190   6.93   3,086
                   2 Bhuvneshwar Kumar          381      581          2   −200     165   7.71   3,260
                   3 Rashid Khan                374      539          4   −165     166   6.96   3,156
                   4 Jofra Archer               357      315          6    +42      60   7.49   1,228
                   5 Harshal Patel              319      169         11   +150     155   8.37   2,129
                   6 Sunil Narine               319      541          3   −222     135   6.98   3,224
                   7 Sandeep Sharma             315      346          5    −31     135   7.74   2,713
                   8 Mohammed Siraj             277      242          7    +35     112   8.25   2,307
                   9 Chris Morris               227      166         12    +62      86   7.69   1,420
                  10 Matheesha Pathirana        212      206          9     +6      49   7.66     682
                  11 Prasidh Krishna            205      154         13    +50      79   8.32   1,516
                  12 Pat Cummins                147       77         23    +70      80   8.51   1,595


   Not every player falls under mRAE and the direction of the change is itself informative. Among batters,
only eleven of the 107 qualifiers gain, and they are the orthodox accumulators who score against good balls
rather than by waiting for loose ones: Faf du Plessis (pRank 26 → mRank 15 on the cumulative list, +39
runs), Ruturaj Gaikwad, Shane Watson and Ajinkya Rahane, so the refinement redistributes credit from
those who feast on hittable deliveries towards those who milk good ones. On the bowling side, the pattern
reverses and is far larger. A majority of qualifying bowlers (73 of 132) rise, because conditioning away
line and length compresses the field, flattering the expensive bowler who at least bowled testing areas and
docking the miser who earned his economy through control. That the adjustment moves most bowlers in
the wrong direction is the quantitative case for confining mRAE to batting.
                                                                                                         32

                 Table S17: Most valuable IPL batter-seasons by mRAE (tracked deliveries,
                 2015–2025, ≥ 150 balls in the season), with pRAE on the same balls, the two
                 ranks, the per-ball change ∆/Ball, and tracked runs, balls and strike rate.
            mRank   Batter             Season   mRAE    pRAE    pRank    ∆/B     Runs    Balls     SR
                 1 Andre Russell       2019       154     170       1   −0.064    511     250    204.4
                 2 AB de Villiers      2016       151     156       3   −0.011    686     406    169.0
                 3 Rishabh Pant        2018       145     158       2   −0.032    679     390    174.1
                 4 David Warner        2016       130     149       4   −0.033    848     559    151.7
                 5 Abhishek Sharma     2024       128     140       6   −0.053    484     237    204.2
                 6 Travis Head         2024       127     141       5   −0.045    567     296    191.6
                 7 Suryakumar Yadav    2023       125     137       7   −0.034    605     334    181.1
                 8 AB de Villiers      2018       103     108       9   −0.017    478     273    175.1
                 9 Prithvi Shaw        2021       103      98      16   +0.016    479     301    159.1
                10 Priyansh Arya       2025       103     108      10   −0.017    545     299    182.3


                 Table S18: Most valuable IPL bowler-seasons by −mRAE (runs saved; tracked
                 deliveries, 2015–2025, ≥ 120 balls in the season), with −pRAE on the same
                 balls. Included for completeness only (Section S2.3).
           mRank    Bowler           Season   −mRAE     −pRAE   pRank     ∆/B    Balls   Wkts     Econ
                 1 Jasprit Bumrah    2019        149      158       2   −0.023    374       21    6.48
                 2 Jasprit Bumrah    2024        142      159       1   −0.056    315       21    6.08
                 3 Jasprit Bumrah    2025        139      141       4   −0.007    284       21    6.57
                 4 Lasith Malinga    2015        138      108      10   +0.081    362       24    7.08
                 5 Jofra Archer      2020        133      115       7   +0.053    336       20    6.29
                 6 Prasidh Krishna   2025        124      102      11   +0.061    354       26    8.08
                 7 Rashid Khan       2020        118      138       5   −0.053    384       20    5.27
                 8 Mohammed Siraj    2023        116      114       8   +0.005    302       20    6.81
                 9 Jasprit Bumrah    2018        115      117       6   −0.007    325       17    6.55
                10 Sunil Narine      2022        110      142       3   −0.095    336       10    5.45


   Two caveats temper even the batting refinement, and together they are why the main paper headlines
pRAE. First, it is available only on the tracked subset, large for some leagues and negligible for others
(Table S10), so mRAE cannot serve as a universal, reproducible cross-competition scale. Second, treating
the delivery as exogenous ignores the batter’s own hand in it: a fine player forces bowlers into the loose
lengths he then punishes, and mRAE, by adjusting them away, declines to credit him for it (the confounding
noted in Section 7). mRAE is thus best read as a sharper, tracking-aware companion to pRAE on the
matches that support it, not as its direct replacement.
