<!-- source: library/preprints/arXiv/2026/2026 - Concave Processes for Multi-Task Career Trajectories - Brahme & Franks (arXiv 2609.33752).pdf -->
<!-- item: https://arxiv.org/abs/2609.33752 -->
<!-- arXiv: 2609.33752, submitted 2026-09-27 -->
<!-- authors: Abhijit Brahme; Alexander Franks -->
<!-- machine conversion from the stored PDF via pdftotext -layout, 2026-10-28; equations, tables and figures are NOT preserved - consult the PDF for those -->

                                              Concave Processes for Multi-Task Career Trajectories: Evaluating
                                                   Aging Across Multiple Measures of NBA Performance
                                                                            Abhijit Brahme∗1 and Alexander Franks†1
                                          1
                                              Department of Statistics and Applied Probability, University of California, Santa Barbara, Santa Barbara,
                                                                                            CA 93106
arXiv:2609.33752v2 [stat.AP] 1 Oct 2026

                                                                                                Abstract
                                                         NBA athlete performance tends to increase through early career as athletes develop and ac-
                                                     climate to the league, followed by decline due to age-related deterioration in athleticism. While
                                                     this general pattern persists, the precise shape of this trajectory varies by athlete and across
                                                     different measures of performance. To model performance increase and decline, we introduce
                                                     the concave process prior, a novel nonparametric prior over concave functions. We then use a
                                                     latent variable model to characterize dependence in aging profiles across player-metrics, embed-
                                                     ding each player in a shared low-dimensional latent space so that players with similar profiles
                                                     learn similar trajectory shapes, peak ages, and peak values. Posterior analysis of the learned
                                                     embedding supports latent-space nearest-neighbor retrieval of career-comparable players and
                                                     informed projections of young players. We apply our model to data across over a dozen per-
                                                     formance metrics for over two thousand players in seasons ranging from 1997 to 2026. Our
                                                     results show that jointly modeling all metrics improves held-out predictive performance over
                                                     single-metric alternatives, and that the concavity constraint itself improves prediction. We find
                                                     that athleticism-driven metrics such as blocks and offensive rebounds peak in a player’s early
                                                     twenties, while skill-based shooting metrics peak in the mid-twenties or later.
                                                     Keywords: Bayesian nonparametrics; Gaussian process latent variable model; concavity con-
                                                     straints; production curves; sports analytics; survival analysis.

                                          1         Introduction
                                          Performance across all demanding human endeavors follow the same performance pattern. Early
                                          on, performance improves as skills are acquired: extended, structured practice produces large
                                          and reliably measured gains in domains ranging from music to chess to sport (Ericsson et al.,
                                          1993; Macnamara et al., 2014). Later, the physiological and cognitive capacities that support
                                          execution begin to erode. Physically, muscle mass, strength, speed, and aerobic power decline after
                                          forty years of age onward and accelerates with age (Tanaka and Seals, 2008). On the cognitive
                                          side, measurable decline in processing speed, reasoning, and memory begins well before mid-life
                                          (Salthouse, 2009). Together, the two processes yield a single-peaked aging profile documented for
                                          creative and professional achievement (Simonton, 1988).
                                              In athletic competition, such aging patterns are often particularly important since performance
                                          is measured over the course of athletes complete careers. Production curves have been estimated
                                               ∗
                                                   abhijitbrahme@ucsb.edu
                                               †
                                                   amfranks@ucsb.edu

                                                                                                    1
across multiple sports ranging from baseball to hockey to golf (Berry et al., 1999; Schulz et al., 1994;
Bradbury, 2009). In these studies, production is approximately unimodal in age. Within a sport,
the age of peak is fairly stable, although the timing of this peak, and the rate of performance decline,
vary by sports and are influenced by the physical and cognitive demands unique to the task (Schulz
and Curnow, 1988; Allen and Hopkins, 2015; Berry et al., 1999; Fair, 2007). This evidence sorts
abilities into two broad families that age in opposite ways: skill-based abilities, accumulated through
sustained, structured practice, that remain comparatively robust once acquired, and athleticism-
based abilities that atrophy earlier and fall away more steeply.
    Basketball is a sport where many observable skills fall into a blend of both regimes. A single
roster spot demands shooting accuracy, rebounding, playmaking, and defense at once, and these
draw on a combination of learned skill and raw athleticism; analyses of professional basketball
players find evidence of exactly this kind of trait compensation with age (Lailvaux et al., 2014).
General managers must project whether a player’s production will hold over the life of a proposed
contract. For example, the Brooklyn Nets’ 2013 trade for aging stars Paul Pierce and Kevin
Garnett (35 and 37 years old respectively) in exchange for future draft picks and younger prospects
illustrates the franchise-altering cost of misjudging career trajectories. Paul Pierce retired shortly
after the end of that season, Kevin Garnett was traded in middle of the subsequent season and
without draft capital or young talent the Nets quickly became one of the worst teams in the
league. From the athlete’s perspective, knowing which skills decline earliest can guide training
adjustments: players may shift toward shooting and decision-making, relying on developing skills
rather than athleticism to impact the game. Production curve analysis formalizes this challenge
as inferring smooth trajectories fp (t) from sparse longitudinal observations across players (Wakim
and Jin, 2014).
    The bulk of the production curve literature models focus on modeling the evolution of a scalar
summary of NBA performance (Page et al., 2007, 2013; Vaci et al., 2019; Wakim and Jin, 2014),
and ignore more nuanced multivariate nature of player performance across multiple aspects of
play like shooting, rebounding, and defensive ability. Rating systems such as RAPTOR (Robust
Algorithm using Player Tracking and On/Off Ratings; Silver and Fischer-Baum, 2015; Silver, 2019)
estimate a single summary score via nearest-neighbor averaging of similar historical players. They
impose similarity through fixed feature comparisons and are susceptible to selection bias at career
extremes. Vaci et al. (2019) improve upon naive averages by fitting piecewise parametric curves
with the peak location specified a priori, but the rigid functional form limits adaptability to diverse
career shapes. Methods that do incorporate player pooling either use categorical positional types
(Page et al., 2007) or pre-specified continuous similarity (Wakim and Jin, 2014; Vinué and Epifanio,
2019); in particular, Vinué and Epifanio (2019) represent each player as a convex combination of a
fixed set of archetypoids (Vinué et al., 2015), constraining the representation to the convex hull of
an a-priori determined archetype set.

1.1   Contributions
Our analysis is organized around three questions about how professional athletes age.

  1. How does production evolve over a career, and how does that evolution vary
     across athletes? A career is characterized not only by average performance but also by
     when players peak and how steeply they decline away afterwards. We therefore want the age
     of peak performance and the value attained at that peak to be explicit, estimable quantities
     carrying their own uncertainty, so that athletes may be compared on the shape of their careers
     rather than on a single career summary.

                                                   2
    2. Do different aspects of performance follow different aging trajectories? Shooting
       accuracy, rebounding, playmaking, and defense place different demands on learned skill and
       on physical capacity. These qualities do not necessarily peak together within a player or
       across the league. Answering this requires estimating a distinct trajectory for each metric
       while still pooling strength across metrics and players.

    3. Does multi-task inference improve forecasts of player skill? Decisions about con-
       tracts, playing time, and draft selections depend on accurate forecasts across a range of skills.
       Multi-task models have been shown to have improved predictive power compared to one-at-
       a-time predictive models (Bonilla et al., 2008), but to date such approaches have not been
       applied to forecasting basketball performance.

    Answering these questions requires a novel production curve model which must (i) treat the
metrics jointly rather than independently (ii) place a prior over trajectories flexible enough to
accommodate diverse career shapes yet constrained to a single peak, with the location of the
peak inferred rather than fixed a priori (cf. Vaci et al., 2019); (iii) respect the native sampling
distributions of count and proportion metrics (iv) learn player similarity from the data rather than
imposing it a priori through positional labels (Page et al., 2007) or a pre-specified archetype sets
(Vinué and Epifanio, 2019); and (v) account for survivorship bias which arises due to the earlier
retirement of less productive athletes.
    To this end, we propose a Bayesian multi-task Concave Process Latent Variable Model (CPLVM)
that jointly estimates concave production curves across over a dozen performance metrics and
thousands of NBA players across 30 seasons of data. The model accounts for player and metric
similarity by learning player-specific latent embeddings from the full metric profile; players with
similar embeddings have similar aging trajectories without relying on positional labels or hand-
specified archetypes. Concavity is enforced through a novel nonparametric prior which we call
a “concave process prior”. A survival model accounts for right-censored careers, correcting the
survivor bias that afflicts conditioning on observed seasons alone.
    We use the results of our latent variable representation to characterize how players age across
the suite of metrics. In doing so, we are able to generate posterior distributions of career trajec-
tories across a wide set of metrics for prospective athletes with limited data. Furthermore, we
generate a deeper understanding of when different metrics peak, characterizing which components
of performance crest early and which crest late in a career. Finally, we are able to examine how a
player moves through their aging profile, creating a characterization of athletes who take longer to
develop vs. those whose decline is rapid.
    The remainder of the paper is organized as follows. In Section 2 we describe the data and high-
light the structure which motivates our modeling choices. In Section 3 we develop the proposed
multi-task Bayesian model of performance, and in Section 4 we introduce the details of our infer-
ential approach. In Section 5 we report the results of our model fit, including comparisons with
alternative models and results which characterize variability in production curves across players
and metrics.

2     Data and Exploratory Analysis
In this work, we analyze data collected on approximately 2300 NBA players from years 1997 -
2026, from the ages of 18 - 38 scraped from basketball-reference.com at a yearly season-level
resolution. The data can be naturally viewed as a tensor of size P by T by K where P is the
number of players, T is the range of ages observed across players’ careers, and K is the number

                                                   3
of production metric curves. Values may be missing for a player at certain ages due to injury,
retirement (right censoring), or late entry into the league (left-censoring). On offense, we measure
free throw attempts (FTA), free throw percentage (FT%), two point shot attempts (FG2A) and
two point shot percentage (FG2%), three point shot attempts (FG3A) and percentage (FG3%),
offensive rebounds (OREB), turnovers (TOV), and assists (AST). On defense, we measure blocked
shots (BLK), defensive rebounds (DREB), and steals (STL). We also include composite metrics
like usage rate (USG) and box plus-minus (BPM), the latter of which is an estimate of points
contributed by the player above league average per 100 possessions played (Myers, 2020). Box
Plus Minus is divided into a measure of points added on offense (OBPM) and points added on
defense (DBPM). In addition, we measure the average minutes per game played (MPG) and total
fraction of games played in the season (GP%). More detailed description of these metrics and an
introduction to basketball analytics can be found in Terner and Franks (2021).
    Broadly, there are three sources of variation, which align with each of the modes of the data
tensor: variability over time for a given player-metric, covariability between players, and covari-
ability between metrics. In Figure 1a we plot LOESS smoothed curves of the evolution of OBPM
over time for five different players. We can see that for all five players they exhibit the expected
pattern of improvement and decline. However, the value at peak performance, the age at which
they peak, and the rate at which they improve and decline all vary by player. LeBron James,
widely regarded as one of the best players of all time, exhibits the largest peak value OBPM of
these five athletes and the slowest decline post-peak. Steve Nash, a famous "late bloomer", does
not peak until his early 30s and sustains that ability until nearly 35 before steeply declining. We
seek to model this temporal evolution of performance via a model that flexibly accounts for this
variation across players.
    However, the rise-then-fall pattern is not limited to OBPM. In Figure 1b we show the correlation
matrix of metrics over time, averaged over players with at least three seasons of data. The figure
shows modest positive correlation between most metrics, which is driven by a combination of what
the player can do athletically and what skills they have learned with experience (often referred to
as "basketball IQ") or repetition. For example, free throw attempt rate is correlated with two-point
field goal attempt rate, since players who attack the rim are more likely to get fouled; the ability
to get to the rim is largely driven by player athleticism. Similarly, metrics measuring shooting
skill tend to correlate, and players who rebound well on the offensive glass in a given season
tend to rebound well on the defensive end. With the metrics ordered via hierarchical clustering,
the heatmap shows a group of metrics related to shooting-skill and offensive performance, and a
distinct group corresponding to rebounding and blocked shot metrics. Composite metrics such
as DBPM, which aggregate contributions of both kinds, correlate modestly with each group. A
multi-task model of production should necessarily account for this metric-dependence.
    Finally, we note that performance varies by player, depending on their playing style and position.
In Figure S1 of the Supplementary Material we show the correlation in career average metrics
computed between players. This plot largely reflects differences in playing style, best understood
in terms by considering the three broad categories of basketball player: guard, forward, and center.
Guards tend to be better at shooting and have more three point shots and centers tend to accrue
more blocks and rebounds. This is apparent in the negative correlation between the group of
blocks/rebounding metrics and the shooting metrics, since being a specialist in one set of skills
tends to imply that they are worse at the other. Positional categories should be considered useful
heuristics, as playing style and ability exists on a spectrum (Chessa et al., 2023). A production
curve model should leverage the low dimensional structure inherent to player style and ability.

                                                  4
    (a) LOESS smoothing of OBPM over time                            (b) Within-player metric correlation

Figure 1: (a) LOESS-smoothed OBPM trajectories for five players: every career rises and then
declines, but peak age, peak value, and the rate of decline all differ by player. (b) Within-player
correlation of metrics across seasons of the same career: most metrics are positively correlated over
the course of a career. Rows and columns are ordered by hierarchical clustering.

3    Proposed Model
Let Y be the P × T × K tensor of metrics yptk be the measured outcome for player p at age t, in
metric k. We model data at a yearly resolution between the ages of 18 and 38 (t ∈ {18, ..., 38})
over the 17 metrics described in Section 2 (k ∈ {1, ..., 17}). yptk is missing for all k if player p does
not play age t, either due to injury or retirement.
    To account for the evolution of performance over time, we construct an aging function fk (Xp , t)
that is concave in t for all p and k. Although this assumption than unimodality, we find that
concavity provides a reasonable approximation to unimodality on a fixed domain. This aging
function enters additively into a latent natural parameter µptk (Xp ), which represents the expected
capability of player p at age t in metric k given a player-specific latent embedding Xp . This
parameter functions as a link-transformed conditional expectation across a number of distinct
likelihood families, allowing us to model non-Gaussian data. We extend this GLM-like construction
to a career duration survival model, which also models the natural parameters as a function of Xp .
In short, our model can be succinctly characterized via the following equations,

                                   µptk = fk (Xp , t) + rpk (t) + optk                                      (1)
                                                                              
                                    yptk ∼ Fk       gk−1 (µptk ) , ϕk , ωptk                                (2)

where fk (Xp , .) represents a concave aging profile given player embedding Xp for metric k and
captures aspects of performance that are predictable given the performance of similar players over
time. rpk (t) reflects aspects of the player’s true skill that deviate from concavity in ways that are
not predictable (e.g. due to injury, change of strategy or role). This source of variability is given an
AR(1) prior and is distinct from irreducible sampling variability due to finite observations which

                                                        5
comes from the sampling distribution in (2). optk is a fixed precomputed offset that we use to
adjust for seasonal league-average trends (see Appendix B.1 of the Supplementary Material for
details). Fk denotes the conditional distribution family corresponding to metric k and gk (·) is a
metric-specific link function mapping the conditional expectation to the linear predictor space. ϕk
represents optional metric-level dispersion or variance scale parameters and ωptk represents time-
varying, observation-specific exposure weights or trial totals, such as minutes played or total field
goal attempts.
   In Subsection 3.1, we describe the likelihood functions for each metric. In Subsection 3.2 we
describe how we model similarity in structural variations from a shared low-dimensional latent space
across players, which jointly maps each likelihood to a unified representation of career progression.
Finally, in Section 3.3 we describe how we construct the concave process for modeling changes in
production over time.

3.1    Likelihood
In this section, we describe the data models, which include a career trajectory model across multiple
metrics as well as a career duration survival model. Joint inference over the performance and
survival components proceeds by summing the log-densities from both models, so that the latent
embedding Xp is simultaneously informed by what a player did on the court and how long they
stayed in the league.
    We consider four classes of observation models based on the available metrics: Gaussian, Bi-
nomial / Beta-Binomial, Poisson / Negative-Binomial, and Beta (See Table 1). Metrics which are
inherently fractions (e.g. field goal percentage) are assumed to be conditionally Beta-Binomially or
Binomially distributed, where nptk is the number of trials, µptk is the logit success probability, and
B is the set of indices corresponding to made-shot metrics. Raw volume counts (BLK, STL, AST,
DREB, OREB, TOV) are modeled as conditionally Poisson, where C is the set of Poisson indices.

                             yptk ∼ Binomial(nptk , logit−1 (µptk )) if k ∈ B                           (3)

                               yptk ∼ Poisson(mpt · exp(µptk )) if k ∈ C                                (4)
   Attempt totals (FTA, FG2A, FG3A), which exhibit overdispersion beyond Poisson, are modeled
as Negative-Binomial,

                        yptk ∼ Negative-Binomial(mpt · exp(µptk ), τk2 ) if k ∈ R                       (5)

Table 1: Observation families by metric type: likelihood, link function, dispersion parameter, and
exposure weight entering Equation (2). For notational brevity in the Binomial and Poisson case,
we assume that the dispersion term from their overdispersed counterparts → ∞.

      Metric Type (k)        Likelihood (Fk )   Link (gk )   Dispersion (ϕk )    Exposure (ωptk )
      Made Shots (k ∈ B)     (Beta-)Binomial    Logit        Precision τk2       Total attempts nptk
      Attempts (k ∈ C, R)    Pois. / NB         Log          Concentration τk2   Minutes played mpt

      Composite (k ∈ G)      Normal             Identity     Variance σ 2        Precision weight mpt
      Proportions (k ∈ P)    Beta               Logit        Precision τk2       Mean-variance map

                                                    6
where τk2 is the overdispersion parameter and R is the set of Negative-Binomial attempt met-
rics. For continuous valued metrics (composite metrics such as OBPM and DBPM), we assume a
conditionally Gaussian model:

                                yptk ∼ Normal(µptk , σ 2 /mpt ) if k ∈ G                           (6)

where G corresponds to the indices of real-valued metrics. Proportion metrics bounded in (0, 1)
— specifically usage rate (USG) and percentage of available minutes played (PCT Minutes) — are
modeled as conditionally Beta distributed,

                               yptk ∼ Beta(logit−1 (µptk ), τk2 ) if k ∈ P                         (7)

where P is the set of indices corresponding to proportion metrics.
   In addition, we consider some special cases related to playing-time. Let gpt denote the total
number of games played and mpt denote the minutes per game played by player p at time t. We
assume that

                                 gpt ∼ Beta-Bin(82, logit−1 (µgpt ), τ12 )                         (8)
                                                        −1
                                mpt ∼ 48 · Beta(logit        (µm      2
                                                               pt ), τ2 /gpt )                     (9)

That is, games played follows a Beta-Binomial distribution with 82 trials (the maximum games
in a season) and minutes-per-game follows a scaled Beta distribution (scaled by 48, the maximum
minutes in a game). In both of the above, we use the mean-variance parameterization.
    Finally, not every player is observed for the full span of seasons covered by the data, and their
dropout is likely informative. For instance, some players retire voluntarily, whereas others are
forced out due to diminishing performance or injury; career lengths are heavily right-skewed, with
the modal career lasting a single season (Figure S2 of the Supplementary Material). Ignoring these
selection would bias estimates of the aging curve since players who exit early are systematically
different from those who persist. We therefore augment the trajectory likelihood with an explicit
model for career duration that accounts for right-censored observations.
    We model the exit age (e.g. retirement) of player p using a survival model. Let Tp be the exit
age and let αp denote their entrance age. We place a player-specific Gompertz proportional-hazards
model on the time at risk Tp | Tp > αp , with age-varying hazard
                                                                            
                                hp (a | Xp ) = ηp (Xp ) exp γp (Xp ) a ,                          (10)

where ηp (Xp ) > 0 is the baseline hazard and γp (Xp ) > 0 is the aging rate governing how quickly
exit risk accelerates with age. We adopt the Gompertz form because its log-hazard is linear in
age, log hp (a) = log ηp (Xp ) + γp (Xp ) a, encoding the notion that exit risk increases by a constant
proportional factor with each additional year of age. This exponential-in-age hazard is commonly
used to model human aging, making it a natural model of athletic decline. More details of this
formulation can be found in Appendix B.4 of the Supplementary Material.

3.2   Player Specific Latent Variables
A key goal is to accurately model dependence between both players and metrics in a data-informed
manner. To this end, we borrow heavily from the methodology of Gaussian Process Latent Variable
Models (GPLVMs), which treat the usual input to the Gaussian Process as an unobserved latent
variable (Lawrence, 2005). Specifically, we introduce a q-dimensional player-specific latent variable
Xp ∈ Rq , such that players that with similar values of xp are expected to have more similar career

                                                    7
production curves across metrics. We encode prior domain knowledge about player embeddings us-
ing a structured prior mean, by shrinking latent variables towards a linear combination of exogenous
player attributes:
                                                         q
                  Xp = Zp⊤ W + σX εp ,                                                  2
                                                                         
                                            εp ∼ t4 0,       1/2 Iq ,        W ∼ N (0, σW I)       (11)
Covariates, Z, include height, draft position, and nominal position (Center, Guard, Forward). The
residual is heavy-tailed, scaled to unit marginal variance so that it matches a standard normal
in width and differs only in the tails, which lets an outlying player sit away from the population
without widening the bulk of the embedding. A more detailed description of this prior can be found
in Appendix B.2 of the Supplementary Material. This prior helps identify more appropriate latent
representations for players with limited data, which in turn improves predictive performance. Next,
we describe how these variables factor into the expected production for players across all metrics.

3.3   A Non-Parametric Prior for Concave Functions
In this Section we describe our construction for the concave functions fk (Xp , t). Specifically, we
construct f by developing a novel nonparametric prior over concave functions which strikes an
ideal balance between flexibility over simpler parametric alternatives (e.g. quadratic models) while
appropriately constraining the functions to respect expected well-documented aging patterns. We
first describe this prior in general terms before describing how it’s applied specifically to model
basketball data.
     We call the prior the “concave process prior” which arises as a composition of continuous push-
forward maps applied to a Gaussian Process with a stationary kernel. Our approach is inspired
the strategy used by Andersen et al. (2018), who propose a non-parametric prior over the space of
monotonic functions.
Proposition 1 (Concave process prior). We say a random function f(t) has a concave process
(CP) prior iff
                                                           Z tZ s
                             f (t) = β0 + β1 (t − t0 ) −                [g(z)]2 dz ds,             (12)
                                                             t0    t0

where g ∼ GP(0, Kt ) is a mean-zero Gaussian process with stationary covariance kernel Kt (·, ·; Θ),
and β0 , β1 are random variables with prior support over all R. If f (t) ∼ CP , it is almost surely
concave. Moreover, let µ denote the law of g on C([t0 , t1 ]), the space of continuous functions on
the modeled interval, and let T : C([t0 , t1 ]) → C([t0 , t1 ]) denote the map defined by the right-hand
side of Equation (12),
                                                           Z tZ s
                             T (g) = β0 + β1 (t − t0 ) −                 g(z)2 dz ds.
                                                              t0    t0

Then f (t) puts positive mass on every uniform neighborhood of any continuous concave function.
Proof. See Appendix A.1 of the Supplementary Material

    The construction above requires only that Kt be stationary with a well-defined spectral den-
sity; throughout the remainder of the paper we take Kt to be the squared-exponential kernel. In
practice, the double integral in Equation (12) cannot be evaluated analytically, so we make a linear
approximation to the Gaussian process as in Andersen et al. (2018). Specifically, we use the Hilbert
Space GP basis function approximation (HSGP), which converges as the number of basis functions
goes to infinity, and leads to tractable analytic solutions (Solin and Särkkä, 2019). See Appendix C
of the Supplementary Material for details.

                                                    8
                                                                                        √
Proposition 2. In Equation (12) replace g(z) with the HSGP approximation Jl=1 S( λl )1/2 αl ψl (t),
                                                                                P
                                                         iid
where S(·) is the spectral density of the kernel Kt , αl ∼ N (0, 1) are basis weights, ψl (t) and λl are
the J eigenfunctions and eigenvalues of the HSGP approximation of Kt on the compact interval
[−L, L], If we let t0 = −L, then,

                                 f (t|Θ) = β0 + β1 (t + L) − αT Ψ(t)α                             (13)

where
                                       cos(ϵ+
                                                              2
                                               (t+L))−1
                                     
                                           lz
                                                 + 2
                                           2L(ϵlz )
                                                        + (t+L)
                                                            4L               if l = z
                         Ψlz (t) =     cos(ϵ+  (t+L))−1   cos(ϵ−  (t+L))−1
                                                                                                  (14)
                                     
                                           lz
                                                 + 2
                                           2L(ϵlz )
                                                        −      lz
                                                              2L(ϵ−    )2
                                                                             if l ̸= z
                                                                    lz

                                                   √                    √     √            √     √
Here, α is a J-vector with entries given by αl · S( λl )1/2 , and ϵ+
                                                                   lz =   λl + λz , ϵ −
                                                                                      lz =   λl − λz ,
respectively. Θ collects the hyperparameters of Kt (lengthscale and amplitude), which enter through
the spectral density S. The parameters β0 and β1 are the constants of integration carried over from
Equation (12).

Proof. see Appendix A.2 of the Supplementary Material.

    The the analytic approximation to concave process derived in Equation (13) can thus be incorpo-
rated into a fully Bayesian model that can be implemented in probabilistic programming language.
We further reparameterize this model into a form that more amenable to prior elicitation for NBA
production curve models. Specifically, note that β0 and β1 can be modeled as a-priori independent
parameters that control the shape of the concave function. For modeling NBA production, we are
most interesting in reasoning about both the value and age of peak performance. As such, define
f ∗ and t∗ the max and argmax of f (t) respectively, that is

                                          f ∗ = max f (t) = f (t∗ )                               (15)
                                                   t

In the following Theorem, we state the parameterization of the concave process in terms of f ∗ and
t∗ .

Theorem 1. Let f (t|Θ) be defined as in Equation (13). Then, if f (t|Θ) takes on the maximum
value of f ∗ at time t∗ ,

                                                                   dΨ(t∗ )
                        f (t|Θ) = f ∗ + AT [Ψ(t∗ ) − Ψ(t) +                (t − t∗ )]A            (16)
                                                                     dt
          ∗
where dΨ(t )
        dt , the time derivative of (14), can be computed analytically.

Proof. See Appendix A.4 of the Supplementary Material.

    Because all of the relevant link functions are strictly monotone increasing, the location of the
maximum is preserved under the inverse link: arg maxt g −1 (f (t)) = arg maxt f (t). Consequently,
the peak age t∗k and the rank ordering of peak values are exactly preserved in the observable space,
and the model’s ability to place a structured prior on peak age and peak value is maintained
regardless of the observation family.

                                                       9
3.3.1   Modeling Dependence Across Concave Processes
In this Section, we extend the univariate concave process to a process over multiple concave func-
tions. Here, we assume each process is associated with auxiliary time-invariant covariates, x, which
in our application corresponds to the player-embedding. We let f (x, t) denote a multivariate con-
cave process associated with covariate x which is concave in t and model the dependence between
h(x, t) and h(x′ , t) for x ̸= x′ . We extend the concave process to a multivariate processes by using
a multi-output Gaussian process.
    We can construct dependent multivariate concave functions, f (x, t), by extending (13) by inte-
grating the square of a multi-task Gaussian Process, g(x, t). Specifically, g(x, t) ∼ GP(0, Kx ⊗ Kt ),
where Kx and Kt are stationary covariance kernels acting on the x space, and time t, independently,
and by allowing the integration constants β0 and β1 to also depend on x. We wish to find all set
                                     2
of f (x, t) such that [g(x, t)]2 = ∂ f∂t(x,t)
                                         2    ≥ 0. As such, our desired function has the form
                                                               Z tZ s
                        h(x, t) = β0 (x) + β1 (x)(t − t0 ) −              [g(x, z)]2 dzds           (17)
                                                                t0   t0

where β0 (x), β1 (x) are constants of integration with respect to t.
                                                                               √ 1/2 i
Proposition 3. Assume (17) holds and let g(x, t) = M
                                                         P             PK                     
                                                            i=1 ϕi (x)   l=1 S( λl ) αl ψl (t) , where
ϕi (x) is a projection of x such that ϕ(x)T ϕ(x) ≈ K(x, x′ ) and ψl (t) are HSGP basis functions for
t. Then,

                f (x, t|Θ) = f ∗ (x)
                                                                     ∗
                                       h                                               i
                          + ϕ(x)T AT Ψ(t∗ (x)) − Ψ(t) + dΨ(tdt(x)) (t − t∗ (x)) A ϕ(x)              (18)
                                                                                      √
where Ψlz (t) is defined as in Equation 14, and A is a M by K matrix where Ail = S( λl )1/2 αli .
Our formulation f (x, t|Θ) converges uniformly to h(x, t) of Equation (17) as K, M −
                                                                                   → ∞.
Proof: see Appendix A.3 of the Supplementary Material.

    Much like the univariate case in Theorem 1, we place independent Gaussian process priors on
the peak value f ∗ and the peak age t∗ , both indexed by the player embedding, so that players with
similar latent coordinates are given similar peaks:
                                           
              fk∗ (Xp ) ∼ GP ck , σc2 K(·, ·) ,
                                                                                           
              t∗k (Xp ) = a tanh gk (Xp ) + tanh−1 (tk /a) ,             gk ∼ GP 0, σt2 K(·, ·) ,   (19)

where K is the same latent-space kernel that governs the curvature weights, and ck and tk are metric-
specific offsets. The peak value is therefore a Gaussian process on the embedding, and the peak
age is the same construction bounded such that the peak age falls within our observation window.
Each metric is realized as an independent draw from these processes, while the shared kernel K
ties them to a common notion of player similarity. Both processes, like the curvature weights, are
realized in practice through the random-feature approximation described in Appendix B.5 of the
Supplementary Material.
    Equations (1), (18) and (19) together specify the production model. For player p and metric
k, the aging curve fk (Xp , t) is the concave process of Equation (18) evaluated at x = Xp , its peak
located and scaled by the two processes of Equation (19), and its curvature determined by the
metric-specific weight matrix Ak , which couples the latent space to the M HSGP time bases.q √ We
give Ak independent normal entries scaled by the square root of the spectral density S( λl ),

                                                   10
so that the induced prior on the second derivative is a Gaussian process over age with per-metric
amplitude αk and lengthscale ℓk , indexed by the same embedding as the peak processes. The
remaining term in Equation (1), the idiosyncratic deviation rpk (t), is given an AR(1) prior with
                                                               k ∼ HalfNormal(0.3). The full set
autocorrelation ρk ∼ Uniform(−0.5, 0.5) and innovation scale σAR
of priors, including the dispersion and exposure parameters of each likelihood family in Table 1, is
given in Appendix B.6 of the Supplementary Material.

4    Inference and Hyperparameter Selection
We implement our model in the probabilistic programming language NumPyro (Phan et al., 2019).
Full MCMC inference in this model is challenging Bayesian factor models typically have rotational
identifiability issues with either the loadings or the factors themselves, yielding a multi-modal pos-
terior. In particular, we find that MCMC sampler gets stuck at suboptimal modes when randomly
initialized. As such, to start the the sampler near a well-identified mode by initializing the MCMC
chains from a maximum a posteriori (MAP) estimate. The MAP estimate is used to fix a small
set of kernel hyperparameters, specifically, the concave GP lengthscale and amplitude (α, lk , σt ,
σc ), the structured prior scales (σW , σX ), and the Gompertz global hazard offset parameters. All
remaining parameters are sampled.
     The model was implemented in the probabilistic programming language NumPyro (Phan et al.,
2019) and inference run on an NVIDIA RTX A5500 GPU (24 GB). The MAP estimate was obtained
by Stochastic Gradient Descent (SGD) and MCMC samples acquired using No U-Turn Sampling
(NUTS). Posterior samples were obtained from 4 chains, run in parallel across both GPUs after
2,000 warmup iterations, with every post-warmup draw retained. Convergence diagnostics are given
in Appendix E and Table S2 of the Supplementary Material. We select the dimension of the latent
player embedding, q, by conducting a holdout ablation study (Appendix H of the Supplementary
Material). A latent dimension of q = 10 was used for the player embedding space, along with
5 HSGP basis functions, to approximate the CPLVM. Analysis of the resultant rotationally non-
identifiable latent space X is conducted through a Procrustes alignment (Appendix B.3 of the
Supplementary Material).
     Finally, we describe our procedure for generating posterior predictive draws. This is non-trivial
as many metrics are conditional on each other through the exposure structure: count-based metrics
depend on minutes played, which in turn depends on games played all of which are part of the joint
forecast in our CPLVM model. To account for this, we generate posterior predictive curves in
systematic way. First, we sample games played (GP%) and minutes per game from the posterior
predictive distribution. The total-minutes in a season is generated as the product of these two
quantities and serves as the exposure for for all counting and rate metrics (FTA, AST, DREB,
etc.). Shooting percentages are then derived from binomial given the the sampled counts. This
cascade appropriately propagates uncertainty about playing time into the uncertainty for season
total production. All code for the analyses in this paper can be found in the github repository.

5    Results
In this Section, we highlight a select number of ways in which our model can be used. First, in
Section 5.1 we demonstrate the superior out of sample forecasting performance of our CPLVM
model compared to many reasonable alternatives. We show that multi-task inference, i.e. fitting
all metrics jointly, improves predictive performance over one-at-a-time models. Then, we show
that the concave process model outperforms both more flexible nonparametric models which are

                                                 11
not constrained to concavity as well as less flexible parametric alternatives. In Section 5.2, we
demonstrate the model fit across a number of players and show how it leads to useful forecasts
of future production as well as principled retrieval of historically comparable players. Finally, in
Section 5.3, we summarize aging patterns vary across metrics, focused on the timing of the peak
and how sensitive different performance metrics are to age-related change.

5.1   Model Comparison
A key advantage of the joint model is its ability to borrow information across metrics and across
similar players. Even for an established star with many seasons of data, the model in Equation (1)
fit to a single metric sees only that metric’s own history. The joint model instead exploits the
low-dimensional structure in how metrics co-evolve: the trajectories of a player’s other metrics
are informative about how OBPM should evolve, which should produce tighter and more coherent
posteriors.
    We test this pooling directly by refitting the model to OBPM alone and find that doing so
significantly degrades held-out predictive accuracy on OBPM itself (Appendix F and Table S3 of
the Supplementary Material).
    We further compare our concave process approach to three alternative models. First, we consider
an unconstrained Gaussian process (GP) prior on fk (Xp , t), built from the same RFF basis, which
imposes smoothness but no restriction on the shape of the trajectory. We also compare the CP
prior to parametric alternatives based on a simpler quadratic model. We consider two variants:
an asymmetric quadratic, in which curvature is constant on each side of the peak but allowed to
differ between the ascent and the decline, and a symmetric quadratic, in which a single constant
curvature governs both. These models all incorporate player-specific latent embeddings, Xp , the
random-Fourier-feature latent kernel, the per-player autoregressive term, and the position-year de-
trend as described in Equation (1). They differ only in what kind of constraints we impose on
fk (Xp , t) over time. Specifically, these models can be considered nested in the sense that each

                      GP
                      |{z}         ⊃ |concave
                                         {z } ⊃ asym. quadratic ⊃ sym. quadratic
                                                 |          {z        }    |          {z       }
                     df 2              df 2      df 2                          df 2
                            free            ≤0          piecewise const.              const.
                     dt2               dt2       dt2                           dt2

As such, the concave process prior used as the featured model represents a balance between non-
parametric flexibility and informed constraints.
   Differences between theseq  nested variants are quantified by the standard deviation of the paired
pointwise differences, se∆ = n vari (elpdA           B
                                            i − elpdi ), following Vehtari et al. (2017). Because the
chain is nested, we compare each variant against its immediate parent rather than against whichever
model scores best in a given scheme, so that every entry measures the cost of one specific restriction
against a reference that is fixed across schemes.
    Constraining the unconstrained GP to a single peak improves held-out predictive density on
every scheme. The parametric restrictions beyond it do not help, suggesting that the flexibility of
a non-parametric model is necessary.
    Table 2 reports holdout 95% HDI coverage together with this ladder: its columns run from least
to most restricted, and each ELPPD entry is the change in held-out density per observation from
imposing that column’s restriction on the model to its left, with † marking differences exceeding
1.96 se∆ . Coverage for the model sits two to four points below the 95% across schemes. One possible
source for this under-coverage include the fact that we fix a set of hyperparameters to their MAP
estimate (Section 4), which removes one layer of uncertainty from the predictive distribution.

                                                         12
Table 2: Predictive performance across holdout schemes for the nested model chain, ordered least
to most restricted. Coverage: holdout 95% HDI coverage, bold closest to nominal. ELPPD:
change in log predictive density per held-out observation from imposing that column’s restriction
on the model to its left; positive favours the restriction, and † marks |∆| > 1.96 se∆ . Performance
metrics only.

                Holdout Scheme        GP        CP      Asym Quadratic      Quadratic
                95% Coverage
                Hold-out Last k     86.6%     90.7%           90.4%            90.4%
                Hold-out First k    87.1%     91.8%           91.2%            91.2%
                Random Interior     84.5%     91.6%           91.5%            91.5%
                Hold-out Peak       87.6%     92.6%           92.3%            92.3%
                Stratified Next k   88.0%     91.7%           91.6%            91.4%
                ∆ELPPD
                Hold-out Last k       ref    +0.25†          -0.015†          -0.0038
                Hold-out First k      ref    +0.31†          -0.012†         +0.0028
                Random Interior       ref    +0.46†          -0.044†         +0.018†
                Hold-out Peak         ref    +0.32†          +0.0020         +0.014†
                Stratified Next k     ref    +0.25†          -0.016†         -0.0087†

5.2   Forecasting and player similarity
Forecasting player ability is a central goal for front offices, who are constantly looking to anticipate
how a player’s production will evolve before committing draft capital, roster spots, and multi-year
salary to that projection. Relatedly, identifying historically similar players helps contextualize a
young player’s early seasons: the completed careers of comparable predecessors provide a reference
for how such profiles have historically developed and declined. As a case study, we focus on the
recent breakout star, seven-foot-four-inch Victor Wembanyama. Wembanyama entered the league
in 2023 amid historic expectations, and his combination of size, rim protection, and perimeter skill
has few direct precedents.
    In Figure 2, we illustrate how our structured prior on the latent space adapts to new data. Be-
cause Wembanyama was the number one overall pick, the structured prior on the player embedding
(Equation 11) anchors Xp in sparsely populated region occupied by elite big men such like Tim
Duncan and Alonzo Mourning. After three seasons however, the data shift his posterior further
toward the edge of the population, into the neighborhood of Durant and James, indicating that
Wembanyama has more guard like qualities than is typical of a player of his size. In order to find
comparable players, we rank players with completed careers by the distance between their posterior
mean embedding and Wembanyama’s, computed after Procrustes alignment of the posterior draws
(Appendix B.3 of the Supplementary Material). His five nearest neighbors are David Robinson,
Alonzo Mourning, Patrick Ewing, Derrick Coleman and Hakeem Olajuwon. Four of the five are
rim-protecting centers; the fifth, Derrick Coleman, is a power forward.
    In Figure 3 we overlay the posterior mean production curves of Wembanyama and his five
nearest completed-career neighbors across AST, BLK, MPG and OBPM, illustrating how closely
the model places his projected career alongside theirs. Figure S3 of the Supplementary Material
shows a complementary view: the model forecast for Wembanyama across OBPM, FG2%, FG2A
and FTA given data from three recorded seasons of play (2023–2026), shown above the fits to career

                                                  13
data from David Robinson and Alonzo Mourning with observed data overlayed. From the model
projections, we expect Wembanyama’s offensive performance, as measured by OBPM, to peak at
around 25 years of age.
    Next, we extend our forecasts to all athletes that entered the league between 2020 and 2025.
We illustrate the forecasting capability of our model, focusing on OBPM as a high-signal measure
of overall offensive production. In Table 3 we report the top five projected players per entry cohort
ranked by the posterior mean of their peak OBPM. We also include 95% credible intervals for their
peak OBPM, the estimated age that they peak (and credible interval) and posterior probabilities
that their career peak OBPM exceeds 2, 3 and 4. These thresholds span the range from above-
average starter to All-Star caliber production: only 19 percent of NBA players in our dataset have
a measured value of OBPM greater than 2 by the end of their career. This drops to 12% for players
that ever exceed an OBPM of 3 and 7% for players that ever exceed an OBPM of 4. The 2020–
2021 entry cohorts show high mean peak OBPM for their top players (Zion Williamson, Tyrese
Haliburton, Anthony Edwards) with near-certain P (OBPM>2), while the 2025 cohort, with only
two seasons of data, yields more diffuse probabilities. Victor Wembanyama tops the 2024 entry
cohort, with an expected OBPM peak of 4.2. For reference, only about a third of number one
overall picks like Wembanyama ever exceed an OBPM of 4. Thus, while a priori we expect this
outcome to be somewhat unlikely, after observing three years of play, the model is more confident
that Wembanyama is likely to be an elite caliber player.

5.3   Characterizing Aging Patterns
In this Section, we explore variation in the timing of peak performance both across metrics and
players. In order to understand heterogeneity in the timing of peak performance across metrics, we
compute the posterior mean of each player’s age of peak performance across metrics. This is only
made possible by the reparameterization of the concave process to explicitly encode f ∗ and t∗ , which
allows us to explicitly sample the posterior of the peak value for a metric, as well as the peak age.
These posterior values act as smoothed estimates of an individual’s observed peak value and peak
age, allowing us to perform Principal Component Analysis (PCA) on the resultant matrix without
introducing noise from the observational data. We plot the loadings for each of the metrics for the
first two principal components, as well as the principal component scores in Figure 4. The first
principal component captures variation in timing of the peak for nearly all metrics, separating early
peakers (Jonny Flynn) from late (Steve Nash), while the second component contrasts the timing
of rebounding, shot-blocking, defensive impact and two-point efficiency with that of three-point
attempt volume.
     In Figure 5a we plot the population distribution of the age of peak performance, split by metric.
The vast majority of metrics peak between the ages of 20 and 25, with the exception of assists,
DBPM, and three point field goal attempts. We find that metrics that are more dependent on
athleticism tend to peak earlier. For example, blocking a shot requires vertical explosiveness and
the recovery speed to contest at the rim. Offensive and defensive rebounding reward second-jump
quickness and the ability to hold position in traffic. By contrast, FT%, FG3%, and AST are pri-
marily skill-driven since they largely reflect the result of a technique refined through repetition
(Ericsson et al., 1993). These metrics tend to peak later. Three-point attempt rate is the clear out-
lier, continuing to rise into a player’s early thirties as shooters add volume, perhaps to compensate
for their declining ability to generate two point field goals.
     In order to properly contextualize these values, we also compute measures of how much change
we can expect in a career, relative to between-player-variation in peak performance. Specifi-
cally, we compute the expected yearly improvement over the four years before the peak, Ep [(fp∗ −

                                                 14
Figure 2: Prior and posterior placement of Victor Wembanyama in the latent space. Background
points show all players at their posterior mean embeddings, projected onto the first two principal
components of that embedding and coloured by listed position. The horizontal axis separates elite
producers from fringe players, and the vertical axis separates guards from big men. The orange
density reflects the covariate-anchored prior density of X for Wembanyama (Equation 11). The
blue density depicts the posterior over Xp given three observed seasons of play. Diamonds mark the
prior and posterior means. Draft standing, height, and positional role alone place him at the thinly
populated big-man edge of the population near Tim Duncan and Alonzo Mourning; the observed
seasons move him further outward, toward Kevin Durant and LeBron James.

                                                15
Figure 3: Posterior mean trajectories of f k (xp , t) for Victor Wembanyama (solid line) and his five
nearest latent-space neighbors, across AST, BLK, MPG, and OBPM. Neighbors are restricted to
completed careers (at least ten observed seasons, with observations at age 34 or later). Curves are
on each metric’s natural scale: counts per 36 minutes, MPG in minutes per game, and OBPM in
points added per 100 possessions.

                                                 16
                                                        OBPM
 Rank    Player               Age   Pos.   Peak Value        Peak Age            P(>2)   P(>3)   P(>4)
 Entry 2025 (2 seasons)
     1   Jared McCain          21   G      1.8 [-1.0, 5.2]   23.6 [20.7, 27.0]    43%     21%      9%
     2   Zaccharie Risacher    20   F      1.4 [-1.6, 4.9]   23.4 [20.7, 25.6]    34%     16%      6%
     3   Ron Holland           20   F      0.8 [-2.4, 4.3]   23.7 [20.7, 26.3]    22%      9%      3%
     4   Stephon Castle        21   G      0.6 [-2.0, 3.7]   22.6 [20.5, 25.0]    17%      6%      2%
     5   Dalton Knecht         24   F      0.5 [-1.7, 2.9]   24.1 [21.4, 27.8]     9%      2%      0%
 Entry 2024 (3 seasons)
     1   Victor Wembanyama     22   C      4.2 [1.7, 7.3]    23.4 [21.1, 25.9]    95%     80%     54%
     2   Anthony Black         22   G      2.7 [-1.5, 6.3]   26.3 [22.5, 28.7]    65%     44%     24%
     3   Amen Thompson         23   F      2.0 [-0.2, 4.6]   23.9 [21.0, 27.2]    46%     19%      6%
     4   Brandon Miller        23   F      1.5 [-0.7, 4.1]   23.7 [21.3, 25.6]    34%     12%      3%
     5   Cam Whitmore          21   F      1.4 [-1.1, 4.2]   22.4 [20.2, 25.3]    30%     11%      3%
 Entry 2023 (4 seasons)
     1   Jalen Williams        24   G      5.3 [2.7, 7.9]    26.5 [24.6, 28.4]    99%     96%     84%
     2   Paolo Banchero        23   F      4.1 [2.0, 6.7]    23.5 [21.9, 25.2]    97%     84%     53%
     3   Dyson Daniels         22   G      2.7 [-0.3, 5.8]   25.9 [23.2, 28.3]    68%     42%     20%
     4   Christian Braun       24   G      2.6 [-0.5, 5.6]   27.5 [23.1, 30.3]    65%     40%     18%
     5   Shaedon Sharpe        22   G      2.4 [-0.3, 5.2]   24.4 [21.4, 26.5]    60%     32%     12%
 Entry 2022 (5 seasons)
     1   Cade Cunningham       24   G      4.0 [1.9, 6.5]    24.0 [22.5, 26.1]    97%     84%     45%
     2   Trey Murphy III       25   F      3.7 [1.6, 6.3]    26.2 [23.9, 28.9]    94%     71%     38%
     3   Franz Wagner          24   F      3.6 [1.5, 6.1]    24.7 [23.2, 26.6]    92%     68%     34%
     4   Cam Thomas            24   G      3.5 [0.7, 6.6]    25.8 [23.1, 28.5]    83%     60%     35%
     5   Evan Mobley           24   F      3.3 [1.1, 5.6]    23.9 [21.8, 25.9]    88%     61%     23%
 Entry 2021 (6 seasons)
     1   Tyrese Haliburton     25   G      6.4 [4.3, 8.7]    25.7 [23.7, 28.3]   100%    100%     99%
     2   Anthony Edwards       24   G      4.5 [2.6, 6.5]    24.0 [22.7, 25.4]   100%     95%     72%
     3   Tyrese Maxey          25   G      4.4 [2.2, 6.7]    26.1 [24.2, 28.1]    98%     89%     62%
     4   LaMelo Ball           24   G      4.2 [2.4, 6.4]    23.0 [20.8, 25.2]    99%     90%     55%
     5   Desmond Bane          27   G      3.8 [2.0, 6.1]    27.2 [25.1, 29.5]    97%     76%     37%
 Entry 2020 (7 seasons)
     1   Zion Williamson       25   F      5.2 [3.6, 7.2]    22.8 [20.9, 25.4]   100%    100%     93%
     2   Ja Morant             26   G      4.6 [2.7, 6.1]    23.3 [21.9, 25.1]   100%     96%     77%
     3   Tyler Herro           26   G      3.4 [1.3, 5.2]    25.4 [23.8, 27.6]    89%     69%     24%
     4   Darius Garland        26   G      3.3 [0.6, 5.7]    25.5 [23.2, 27.6]    83%     67%     30%
     5   Cameron Johnson       29   F      2.6 [1.1, 4.3]    27.1 [25.2, 29.1]    73%     29%      5%

Table 3: Top 5 players by posterior mean peak OBPM per entry cohort. Peak Value and Peak Age
are posterior means with 95% credible intervals in brackets. P(>2), P(>3), P(>4) are posterior
probabilities that peak OBPM exceeds the threshold; empirically, 19% of players peaked above
OBPM = 2, 12% above OBPM = 3, and 7% above OBPM = 4 (career peak per player).

                                               17
Figure 4: PCA on posterior mean peak ages by metric: player scores on the first two principal
components (left) and the corresponding metric loadings (right). In the left panel, two represen-
tative players are labelled per quadrant. The horizontal axis (PC1) captures overall peak timing.
All but four metrics load with the same sign (the exceptions are DBPM, STL, BLK, and OREB),
so players toward the left peak later across most of the board (e.g. Nash, Stockton) and those
toward the right peak earlier (e.g. Jonny Flynn, Landry Fields). The vertical axis (PC2) contrasts
the timing of rebounding, shot-blocking, defensive impact and two-point efficiency with that of
three-point attempt volume. Players near the top have their three-point volume peak earlier (e.g.
Arron Afflalo), while players near the bottom show the reverse (e.g. Nash, Stockton).

fp (a− ))/(t∗ − a− )]/sdp (fp∗ ), as well as the expected yearly decline over the four years after it,
Ep [(fp∗ − fp (a+ ))/(a+ − t∗ )]/sdp (fp∗ ), taken over all players for each specific metric, where a− =
max(t∗ − 4, 18) and a+ = min(t∗ + 4, 38) stop the window at the boundary of the modelled ages.
These values are depicted for all metrics in Figure 5. Metrics further from the origin change the
most over a career, whereas those that are closer to the origin tend to change relatively little. This
suggests that aging greatly affects metrics such as minutes per game, OBPM, games played while
leaving metrics such as blocks, defensive rebounds, and steals relatively intact.
    Blocks, for example, “peak” very early (even before most athlete’s enter the NBA) but do not
decline much over an athlete’s career, suggesting block rate is dependent more so on player style
rather than aging. On the other hand, OBPM, FG2% and minutes per game change more dramat-
ically over an athlete’s career. If we assume that shooting in isolation is a technique driven ability,
then we can attribute the aging derived change in two point field goals to a drop in athleticism
which prevents the shooter from generating clean physical separation from their defenders. This
in part can explain drops in OBPM and minutes per game, as a diminished ability to pressure
defenses can cause a drop in impact on the offensive end and meaningful minutes.
    We also identify metrics which decline faster than they rise (and vice versa) by examining
whether the metrics lie above the y=x line in Figure 5b. For most metrics, the rate of rise and
fall are roughly the same. However, minutes per game decay faster than they rise suggesting an
athlete quickly becomes less durable as their career progresses, either playing less due to injury,
capacity, or injury prevention protocols. Two-point shooting efficiency has the opposite asymmetry,
improving rapidly early in a career and decaying more slowly post-peak. Ultimately, these multi-
metric aging trends can help front offices and coaches understand and calibrate realistic performance
expectations.

                                                  18
                                                        (b) Expected pre-peak improvement vs. post-peak de-
               (a) Peak age by metric                   cline

Figure 5: (a) Distribution of posterior means for the age of peak, separated by metric and ordered by
population mean (dot), with 50% (thick) and 95% (thin) intervals. BLK and OREB peak earliest;
the shooting metrics FG3%, FT%, and FG3A sit at the late end of the ordering. (b) Expected
improvement per year over the four years before the peak against expected decline per year over
the four years after, one point per metric. The horizontal coordinate is Ep [(f ∗ − f (a− ))/(t∗ −
a− )]/sdp (f ∗ ) and the vertical coordinate is Ep [(f ∗ − f (a+ ))/(a+ − t∗ )]/sdp (f ∗ ), with a− = max(t∗ −
4, 18) and a+ = min(t∗ + 4, 38). A metric on the dashed line rises and falls at the same normalised
rate, one above it decays faster than it ascends. The largest asymmetry above the line belongs to
MPG, which decays faster than it rose. OREB and BLK sit just above it. GP% and FG2% lie
furthest below the line, rising faster than they decline.

                                                     19
6    Conclusion and Future Work
We introduced a joint Bayesian model for multi-metric NBA career trajectories that combines
two novel components 1) a Concave Process (CP) prior over production curves that encodes the
biological constraint of concave aging, and 2) a latent variable model (GPLVM) that embeds all 17
metrics into a shared low-dimensional player representation.
    Our results answer the three questions posed in Section 1.1. First, the model renders peak age
and peak value explicit posterior quantities, so a career is characterized not by a single summary
but by when a player peaks, how high, and with what uncertainty. Players with limited data inherit
credible trajectories from their nearest latent neighbors, allowing us to make multi-metric forecasts
for rookies and young players. Second, different aspects of performance are affected by aging in
different way: rebounding and shot-blocking peak in a player’s early twenties, shooting efficiency
peaks in the mid-twenties, and three-point attempt volume continues rising into the early thirties.
Third, multi-task inference improves performance forecasts, emphasizing the value of multivariate
predictive models in sports.
    Several limitations should be noted. First, the model is estimated on players who appeared in at
least one NBA game, introducing survivor bias. Players who failed to reach or sustain NBA careers
are unobserved, so the posteriors describe the distribution over NBA-caliber trajectories rather than
the full talent distribution. Second, the latent kernel is stationary, so similarity between players
depends only on the distance between their embeddings and not on where in the latent space they
sit. A non-stationary kernel could allow for more flexible modeling.
    There are also several interesting extensions and generalizations that may be considered. The
most immediate is to apply the framework to other professional sports leagues where longitudinal
performance data are available (e.g., soccer, hockey, baseball), testing whether CPLVM structure
generalize beyond basketball. In addition, our model could be used to estimate the impacts of
injury by comparing counterfactual career trajectories to observed post-injury performance. Finally,
integrating the trajectory model with contract-length and salary-cap data would allow front offices
to assess not just athletic performance but economic value over the duration of a proposed contract.

                                                 20
References
Sian V Allen and William G Hopkins. Age of peak competitive performance of elite athletes: A
  systematic review. Sports Medicine, 45(10):1431–1441, 2015.

Michael Riis Andersen, Eero Siivola, Gabriel Riutort-Mayol, and Aki Vehtari. A non-parametric
 probabilistic model for monotonic functions. All of Bayesian Nonparametrics Workshop
 (BNP@NeurIPS), 2018.

Christian Aßmann, Jens Boysen-Hogrefe, and Markus Pape. Bayesian analysis of static and dynamic
 factor models: An ex-post approach towards the rotation problem. Journal of Econometrics, 192
 (1):190–206, 2016. ISSN 0304-4076. doi: https://doi.org/10.1016/j.jeconom.2015.10.010. URL
 https://www.sciencedirect.com/science/article/pii/S0304407615002626.

Scott M Berry, C Shane Reese, and Patrick D Larkey. Bridging different eras in sports. Journal of
  the American Statistical Association, 94(447):661–676, 1999.

Edwin V Bonilla, Kian Chai, and Christopher Williams. Multi-task gaussian process prediction. In
  J. Platt, D. Koller, Y. Singer, and S. Roweis, editors, Advances in Neural Information Processing
  Systems, volume 20. Curran Associates, Inc., 2008. URL https://proceedings.neurips.cc/
  paper/2007/file/66368270ffd51418ec58bd793f2d9b1b-Paper.pdf.

John Charles Bradbury. Peak athletic performance and ageing: Evidence from baseball. Journal
  of Sports Sciences, 27(6):599–610, 2009.

Antonio Chessa, Pierpaolo D’Urso, Luigi De Giovanni, et al. Complex networks for community
 detection of basketball players. Annals of Operations Research, 325:363–389, 2023. doi: 10.1007/
 s10479-022-04647-x. URL https://doi.org/10.1007/s10479-022-04647-x.

K Anders Ericsson, Ralf T Krampe, and Clemens Tesch-Römer. The role of deliberate practice in
  the acquisition of expert performance. Psychological Review, 100(3):363–406, 1993.

Ray C Fair. Estimated age effects in athletic events and chess. Experimental Aging Research, 33
  (1):37–57, 2007.

Gregory W. Gundersen, Michael Minyi Zhang, and Barbara E. Engelhardt. Latent variable model-
  ing with random features. In Proceedings of the 24th International Conference on Artificial Intel-
  ligence and Statistics, volume 130 of Proceedings of Machine Learning Research, pages 1333–1341.
  PMLR, 2021. URL https://proceedings.mlr.press/v130/gundersen21a.html.

Simon P Lailvaux, Robbie Wilson, and Michael M Kasumovic. Trait compensation and sex-specific
  aging of performance in male and female professional basketball players. Evolution, 68(5):1523–
  1532, 2014.

Neil Lawrence. Probabilistic non-linear principal component analysis with gaussian process latent
  variable models. Journal of Machine Learning Research, 6(60):1783–1816, 2005. URL http:
  //jmlr.org/papers/v6/lawrence05a.html.

Brooke N Macnamara, David Z Hambrick, and Frederick L Oswald. Deliberate practice and per-
  formance in music, games, sports, education, and professions: A meta-analysis. Psychological
  Science, 25(8):1608–1618, 2014.

                                                21
Daniel Myers. About box plus/minus (bpm). Basketball-Reference.com, 2020. URL https://www.
 basketball-reference.com/about/bpm2.html. Accessed: 2026-08-26.

Garritt L Page, Gilbert W Fellingham, and C Shane Reese. Using box-scores to determine a
 position’s contribution to winning basketball games. Journal of Quantitative Analysis in Sports,
 3(4), 2007.

Garritt L Page, Bradley J Barney, and Aaron T McGuire. Effect of position, usage rate, and per
 game minutes played on NBA player production curves. Journal of Quantitative Analysis in
 Sports, 9(4):337–345, 2013.

Du Phan, Neeraj Pradhan, and Martin Jankowiak. Composable effects for flexible and accelerated
 probabilistic programming in numpyro. arXiv preprint arXiv:1912.11554, 2019.

Evan Poworoznek, Niccolo Anceschi, Federico Ferrari, and David Dunson. Efficiently resolving
  rotational ambiguity in bayesian matrix sampling with matching, 2024. URL https://arxiv.
  org/abs/2107.13783.

Ali Rahimi and Benjamin Recht. Random features for large-scale kernel machines. In J. Platt,
  D. Koller, Y. Singer, and S. Roweis, editors, Advances in Neural Information Processing Systems,
  volume 20. Curran Associates, Inc., 2007. URL https://proceedings.neurips.cc/paper_
  files/paper/2007/file/013a006f03dbc5392effeb8f18fda755-Paper.pdf.

Timothy A Salthouse. When does age-related cognitive decline begin? Neurobiology of Aging, 30
  (4):507–514, 2009.

Richard Schulz and Christine Curnow. Peak performance and age among superathletes: Track and
  field, swimming, baseball, tennis, and golf. Journal of Gerontology, 43(5):P113–P120, 1988.

Richard Schulz, Donald Musa, James Staszewski, and Robert S Siegler. The relationship between
  age and major league baseball performance: Implications for development. Psychology and Aging,
  9(2):274–286, 1994.

Nate Silver. How our RAPTOR metric works.            https://fivethirtyeight.com/features/
 how-our-raptor-metric-works/, Oct 2019.

Nate Silver and Reuben Fischer-Baum. We’re predicting the career of every NBA player. Here’s how.
 https://fivethirtyeight.com/features/how-were-predicting-NBA-player-career/, Oct
 2015.

Dean Keith Simonton. Age and outstanding achievement: What do we know after a century of
  research? Psychological Bulletin, 104(2):251–267, 1988.

Arno Solin and Simo Särkkä. Hilbert space methods for reduced-rank gaussian process re-
  gression. Statistics and Computing, 30(2):419–446, August 2019. ISSN 1573-1375. doi:
  10.1007/s11222-019-09886-w. URL http://dx.doi.org/10.1007/s11222-019-09886-w.

Hirofumi Tanaka and Douglas R Seals. Endurance exercise performance in masters athletes: Age-
  associated changes and underlying physiological mechanisms. The Journal of Physiology, 586(1):
  55–63, 2008.

Zachary Terner and Alexander Franks. Modeling player and team performance in basketball.
  Annual Review of Statistics and Its Application, 8:1–23, 2021.

                                               22
Nemanja Vaci, Dijana Cocić, Bartosz Gula, and Merim Bilalić. Large data and bayesian model-
  ing—aging curves of NBA players. Behavior Research Methods, pages 1–21, 2019.

Aki Vehtari, Andrew Gelman, and Jonah Gabry. Practical bayesian model evaluation using leave-
 one-out cross-validation and WAIC. Statistics and Computing, 27(5):1413–1432, 2017.

Aki Vehtari, Andrew Gelman, Daniel Simpson, Bob Carpenter, and Paul-Christian Bürkner. Rank-
 normalization, folding, and localization: An improved R b for assessing convergence of MCMC
 (with discussion). Bayesian Analysis, 16(2):667–718, 2021.

Guillermo Vinué and Irene Epifanio. Forecasting basketball players’ performance using sparse
 functional data. Statistical Analysis and Data Mining: The ASA Data Science Journal, 2019.

Guillermo Vinué, Irene Epifanio, and Sandra Alemany. Archetypoids: A new approach to define
 representative archetypal data. Computational Statistics & Data Analysis, 87:102–115, 2015.

Alexander Wakim and Jimmy Jin. Functional data analysis of aging curves in sports. arXiv preprint
  arXiv:1403.7548, 2014.

Michael Minyi Zhang, Gregory W. Gundersen, and Barbara E. Engelhardt. Bayesian non-linear
 latent variable modeling via random fourier features, 2023. URL https://arxiv.org/abs/2306.
 08352.

                                               23
Supplementary Material

A      Enforcing Concavity
A.1     Validity of Prior
Proof. The map Φ(a, b, g)(t) = a + b(t − t0 ) − tt0 ts0 g(z)2 dz ds is continuous since it composes the
                                                       R R

bounded, continuous operations (addition, squaring, integrating). A continuous transformation of
a distribution is a valid distribution over the image of the transformation. That image consists of
                                    ′′
concave functions, since Φ(a, b, g) = −g 2 ≤ 0.

A.2     Univariate Case
Considering we only wish our function f (t) to be concave in the t argument, we wish to find all set
                    2
of f (t) such that ∂ ∂tf 2(t) ≥ 0. As such, our desired function has the form
                                                               Z tZ s 2
                                                                     ∂ f (z)
                                f (t) = a + b(t − t0 ) −                             dzds            (S1)
                                                                  t0   t0    ∂z 2
where a, b are some constants of integration with respect to t. We show in the subsequent section
how these constants of integration can be defined to modulate the shape of f (t).
                                                                                       2
   Following the line of reasoning from Andersen et al. (2018), we assume that ∂ ∂tf 2(t) can be
modeled by [g(t)]2 , where g(t) ∼ GP(0, Kt ). In order to enforce concavity across the t dimension,
we use the Hilbert Space Gaussian Process
                                       √ 1/2(HSGP) approximation mentioned in Andersen et al.
(2018) to approximate g(t) ≈ K
                               P
                                 l=1 S( λl ) αl ψl (t).
   Consequently,
                                     K X
                                     X K
                           g(t)2 ≈             S( λz )1/2 S( λl )1/2 αl αz ψl (t)ψz (t)
                                                 p              p

                                     l=1 z=1
                                                                  K X
                                                                  X K
                                                              ≈               α̃l α˜z ψl (t)ψz (t)   (S2)
                                                                  l=1 z=1
                           √
     after letting α̃l = S( λl )1/2 αl . As such, substituting (S2) into (S1) gives
                                                   K X
                                                   X K                 Z tZ s
                       f (t) ≈ a + b(t − t0 ) −              α̃l α˜z              ψl (w)ψz (w)dwds   (S3)
                                                   l=1 z=1              t0   t0

     Rewriting the above in terms of matrix products, and setting t0 = −L, yields

                                       f (t) ≈ a + b(t + L) − α̃T Ψ(t)α̃                             (S4)

     Here, α̃ is a K vector with entries given by α̃l . The entries of the K × K matrix Ψ(t) are given
by
                                         cos(ϵ+
                                                                2
                                                 (t+L))−1
                                       
                                             lz
                                                   + 2
                                             2L(ϵlz )
                                                          + (t+L)
                                                              4L                       if l = z
                           Ψlz (t) =     cos(ϵ+  (t+L))−1   cos(ϵ−  (t+L))−1
                                                                                                     (S5)
                                       
                                             lz
                                             2L(ϵ+    )2
                                                          −      lz
                                                                2L(ϵ  − 2
                                                                         )
                                                                                       if l ̸= z
                                                   lz                 lz
                 √      √                √     √
    Here, ϵ+
           lz =    λl + λz , and ϵ− lz =   λl − λz . Note that since the eigen-functions ψl (t) are
sinusoidal, the integral in (S1) can be computed in closed form.

                                                         24
    The concavity prior is placed on the latent mean µptk in the linear predictor space; it does not,
in general, guarantee concavity of the observable response after applying the inverse link. However,
the scientifically relevant properties are fully preserved. All link functions used in the model are
strictly monotone increasing. For any strictly monotone g −1 ,

                                   arg max g −1 (µptk (t)) = arg max µptk (t),
                                        t                                          t

so the peak age t∗k is identical in the latent and observable spaces. The peak value in the observable
space, g −1 (µptk (t∗k )), is a monotone function of the latent peak, so the rank ordering of peak values
across players is also preserved.

A.3     Multivariate Case
Considering we only wish our function f (x, t) to be concave in the t argument, but still incorporate
information from another set of dimensions encoded by x, we wish to find all set of f (x, t) such
      2
that ∂ f∂t(x,t)
           2    ≥ 0. As such, our desired function has the form
                                                                             Z tZ s 2
                                                                                   ∂ f (x, z)
                         f (x, t) = β0 (x) + β1 (x)(t − t0 ) −                                        dzds   (S6)
                                                                              t0   t0        ∂z 2

where β0 (x), β1 (x) are constants of integration with respect to t. We show in the subsequent section
how these constants of integration can be defined to modulate the shape of f (x, t).
                                                                                                2
    Following the line of reasoning from Andersen et al. (2018), we assume that ∂ f∂t(x,t)         2  can be
modeled by [g(x, t)]2 , where g(x, t) ∼ GP(0, Kx ⊗ Kt ). Note that this assumes that the time
variable t is separate from our x variable .
    Using a Random Fourier Feature (Appendix B.5) projection ϕi (x) for the x dimension, we can
write g(x, t) ≈ M
                  P
                    i=1 βi (t)ϕi (x). Here, βi (t) are t-dependent coefficients of the basis expansion. In or-
der to enforce concavity across the t dimension, we use the Hilbert Space Gaussian Process     √ 1/2(HSGP)
approximation mentioned in Andersen et al. (2018) to approximate βi (t) ≈ K                     λl ) αli ψl (t).
                                                                                      P
                                                                                        l=1 S(
Note that this approximate representation preserves the separability of the covariance structure of
our desired g(x, t) (Appendix D).
                           √
    If we let α˜li = αli S( λl )1/2 , then g(x, t) ≈ M
                                                       P             PK ˜i
                                                          i=1 ϕi (x)( l=1 αl ψl (t)).
    Consequently,
                                                       M X
                                                       X M
                                         g(x, t)2 ≈                 ϕj (x)ϕi (x)βj (t)βi (t)
                                                       i=1 j=1
                                   M X
                                     M                       K                   X ˜   K
                                                                    α˜li ψl (t))( αlj ψl (t))
                                   X                         X
                              ≈               ϕj (x)ϕi (x)(
                                    i=1 j=1                   l=1                      l=1
                                     M X
                                       M                       K X
                                                                 K
                                                                             ˜
                                                                             αlj α˜zi ψl (t)ψz (t))
                                     X                         X
                               ≈               ϕj (x)ϕi (x)(                                                 (S7)
                                     i=1 j=1                   l=1 z=1

    As such, substituting (S7) into Equation (17) of the main text gives

                        f (x, t) ≈ β0 (x) + β1 (x)(t − t0 )−
                        M X
                          M                        K X
                                                     K                 Z tZ s
                                                       ˜j
                                                             αl α˜zi
                        X                          X
                                   ϕj (x)ϕi (x)(                                   ψl (w)ψz (w)dwds)         (S8)
                         i=1 j=1                   l=1 z=1              t0    t0

                                                              25
   Rewriting the above in terms of matrix products, and setting t0 = −L, yields

                        f (x, t) ≈ β0 (x) + β1 (x)(t + L) − ϕ(x)T ÃT Ψ(t)Ãϕ(x)                    (S9)

                                                     ˜
    Here, Ã is a M × K matrix with entries given by αlj . The entries of the K × K matrix Ψ(t) are
given by Equation (14) of the main text, from the univariate case.

A.4    Controlling the Peak Behavior
We may wish to place a prior on the location of the peak of our curve, as well as the value that
this peak takes. Thus, our formulation begins with the following constraints:

  1. f (x, tmax ) = fmax
     d
  2. dt f (x, t)|t=tmax = 0

    The first expectation illustrates that at our peak tmax , our function takes on the value c. The
second expectation requires that our first derivative with respect to t is 0 at tmax . Since our function
is concave by construction, we do not need to constrain the behavior of the second derivative. Note
here that tmax and fmax are specified apriori.
    Taking the partial derivative of the main text’s Equation (18) with respect to t, and setting it
equal to 0 yields the following requirement
                                                               ′
                                     β1 (x) = ϕ(x)T ÃT Ψ (tmax )Ãϕ(x)                            (S10)
        ′
Here, Ψ is the first derivative of the entries of the main text’s Equation (14) with respect to t.
Now, it remains to satisfy the peak value constraint. Formally,

                     β0 (x) = fmax − β1 (x)(tmax − t0 ) + ϕ(x)T ÃT Ψ(tmax )Ãϕ(x)                 (S11)

If we combine (S10) and (S11), and plug the resulting values for β0 (x) and β1 (x) into Equation (18)
of the main text, we are met with the following theorem.

                                                                     ′
              f (x, t) ≈ fmax + ϕ(x)T ÃT [Ψ(tmax ) − Ψ(t) + Ψ (tmax )(t − tmax )]Ãϕ(x)           (S12)

Note that when t = tmax , we recover fmax as desired.
   Subsequently, letting fmax (x), tmax (x) ∼ GP (0, Kx ) allows us to pool information across the x
dimension, allowing similar players to have similar peaks / peak-values.

A.5    Convergence of the Push-Forward HSGP Approximation
Proposition S1 (Convergence of the HSGP approximation). Let K be a stationary covariance
function with spectral density S(·), let g ∼ GP (0, K), and fix an interval of interest [0, T ]. For
a domain
     √    [−L, L] ⊃ [0, T ] let {ψi , λi }∞
                                          i=1 be the Dirichlet Laplacian eigenpairs on [−L, L], write
ωi = λi , and let
                                           M q
                                           X                             iid
                              gM,L (t) =         S(ωi ) αi ψi (t),   αi ∼ N (0, 1),
                                           i=1

                                                         26
be the HSGP approximation of Solin and Särkkä (2019). Define
                            Z tZ s                                Z tZ s
                                         2
                  f (t) =            g(z) dz ds,     fM,L (t) =            gM,L (z)2 dz ds.
                             0   0                                 0   0

Then, as L → ∞ with M/L → ∞,

                                 fM,L → f     in distribution on C([0, T ]).

Proof. By Theorem 1 of Solin and Särkkä (2019), KM,L → K uniformly. Since both processes are
centred Gaussian, this gives gM,L → g in distribution on L2 ([0, T ]). Squaring is continuous from L2
to L1 and double integration is bounded linear from L1 into C([0, T ]), so the continuous mapping
theorem gives fM,L → f in distribution.

                                                     27
B     Model Specifications
B.1    Accounting for Seasonal Trends Across Metrics
Three-point volume, pace, and positional usage have all changed substantially over the seasons
spanned by the data. Left unmodeled, this era variation is absorbed into the aging function, and
fk conflates how a player changes with how the league changed.
    Let cp ∈ {G, F, C} denote the position group of player p — guard, forward, or center — and spt
the calendar season in which player p is aged t. Writing ȳk (c, s) for the observed average of metric
k over all players of position group c in season s, the offset optk = gk (ȳk (c, s)) enters each metric’s
linear predictor through that metric’s own link. For ages projected beyond the observed seasons,
the offset is set to the nearest available season.
    The grouping is by position and season rather than season alone because league trends such
as three point shooting did not effect all positions equally. For example, big men saw a larger
proportionate increase in three point attempt rate than guards. The curve fk then represents
production relative to a player’s positional peers in the same season.

B.2    Latent Embedding Prior
Let                                                                      ⊤
                                                                              ∈ R4
                              
                        Zp = − log dp , hp , 1[posp = F ], 1[posp = G]
denote four player-level age agnostic covariates: negative log draft position − log dp (a proxy for
talent), height hp , and two indicator variables for positional group (Forward and Guard, with Center
as the baseline category). Players without a recorded draft position are assigned a rank of P +1,
where P is the total number of players in the cohort, so that − log dp defaults to the minimum value
after standardization. We introduce a learned projection W ∈ R4×q with scale σW and a residual
scale σX , and place the prior
                                                           q
                     Xp = Zp⊤ W + σX εp ,
                                                                         
                                              εp ∼ tν 0,    (ν − 2)/ν Iq ,    ν = 4,
                                 2
                      W ∼ N (0, σW I4×q ).                                                          (S13)

The residual is Student-t rather than Gaussian to account for the probability of outlier talent. Scales
are learned at the MAP and held fixed during posterior sampling (σX = 1.90, σW = 0.16). The
prior mean Zp⊤ W pulls a player’s latent position toward the subspace predicted by draft standing,
physical size, and positional role; the residual scale σX controls how tightly the data must pull Xp
away from that prior mean. When σW → 0 the prior reduces to the isotropic case σX εp . Finally,
W is shared across all players and learned from the data.

B.3    Procrustes Alignment of Posterior Draws
Because the latent embedding Xp ∈ Rq is only identified up to orthogonal rotation of its learned
coordinates, raw MCMC draws from different chains occupy different rotation frames and cannot be
directly compared or averaged. There are different approaches for dealing with nonidentifiability
of factors across multiple MCMC samples (Aßmann et al., 2016; Poworoznek et al., 2024). To
enable coherent posterior summaries, we apply Procrustes alignment to each (chain, draw) pair:
given the MAP estimate X̂ as a fixed reference, we find the orthogonal matrix R(s) minimising
∥X̂ − X (s) R(s) ∥F via singular value decomposition, and replace each sampled X (s) with the aligned
version X (s) R(s) before any downstream computation.

                                                   28
B.4    Career Duration Formulation
We model career exit with a player-specific Gompertz proportional-hazards model. We select the
Gompertz model since its hazard rises monotonically with age, and has historically been used to
model human aging. Because player p is only observed from entrance age αp onward, the exit-
time likelihood is left-truncated at αp (and right-censored for players still active at the end of the
observation window). The Gompertz hazard and cumulative hazard are
                                                                    ηp γp a
                                 hp (a) = ηp eγp a ,
                                                                            
                                                        Hp (a) =       e −1 ,                        (S14)
                                                                    γp
and the left-truncated log-likelihood contributions for exit age Tp are
                             (                                       
                                 log hp (Tp ) − Hp (Tp ) − Hp (αp )       (observed exit),
                      ℓp =                                                                         (S15)
                                 − Hp (Tp ) − Hp (αp )                    (right-censored),

where log hp (a) = log ηp + γp a and the truncated increment is Hp (Tp ) − Hp (αp ) = (ηp /γp ) eγp Tp −
eγp αp . Both parameters are linked to the latent embedding on the log scale, through the same
feature-map projection ϕ(Xp ) used by the performance likelihood. The latent embedding thereby
ties career longevity to the same low-dimensional representation that drives on-court performance:

                                      log ηp = ηglob + σexit ϕ(Xp )⊤ ψexit ,                         (S16)
                                      log γp = γglob + ϕ(Xp )⊤ ψrate ,                               (S17)

Here ηglob ∼ N (log 0.04, 0.5) and γglob ∼ N (log 0.15, 0.3) are global log baseline-hazard and log
aging-rate offsets, σexit ∼ HalfNormal(0.5) controls the player-specific spread in baseline hazard,
and ψexit ∼ N (0, I), ψrate ∼ N (0, 0.12 I), with dimension matching ϕ(Xp ). The exponential links
keep ηp , γp > 0, so every player’s exit hazard is increasing in age.

B.5    Random Fourier Feature Latent Projection
We model player-player correlation with a random Fourier feature (RFF) expansion (Rahimi
and Recht, 2007), which induces a stationary, automatic-relevance-determination (ARD) squared-
exponential kernel over the latent space. This is the random Fourier feature latent variable model
(RFLVM) of Gundersen et al. (2021), together with its fully Bayesian extension Zhang et al. (2023).
    Draw m spectral frequencies collected into Ω ∈ Rm×q with Ωij ∼ N (0, 1), together    √           with
                                                                                                      p 
                                                                                                          a
per-dimension lengthscale ℓ = (ℓ1 , . . . , ℓq ), ℓj ∼ HalfNormal(1). Writing Ω̃ = Ω diag ℓ1 , . . . , ℓq ,
define the unit-norm feature map
                           1 h                       i⊤
                 ϕ(Xp ) = √ cos(Ω̃Xp )⊤ , sin(Ω̃Xp )⊤ ∈ R2m ,                    ∥ϕ(Xp )∥2 = 1.      (S18)
                           m
By Bochner’s theorem the feature inner product is an unbiased Monte-Carlo estimator of the ARD
squared-exponential kernel (Rahimi and Recht, 2007),
                                                                         Pq                   
               ϕ(Xp )⊤ ϕ(Xp′ ) −−−−−→ k(Xp , Xp′ ) = exp − 21                                   2
                                                                           j=1 ℓj (Xpj − Xp′ j ) ,   (S19)
                                     m→∞

so ℓj is the relevance (inverse squared bandwidth) of latent dimension j. The peak-age and peak-
value weights become γ kage , γ kval ∈ R2m , the concave HSGP basis weights become Ak ∈ R2m×M ,
and the Gompertz links of Equations S16–S17 specialise to

                log ηp = ηglob + σexit ϕ(Xp )⊤ ψ exit ,       log γp = γglob + ϕ(Xp )⊤ ψ rate ,      (S20)

                                                        29
with ψ exit , ψ rate ∈ R2m .
    We keep the structured prior on Xp (Equation S13) unchanged. The projection remains shared
across all metrics and the survival model. The frequencies Ω are drawn once and are learned rather
than held at their random initialisation. We initialise Ω at its MAP estimate and continue to
sample it during MCMC, while the lengthscale ℓ is learned at the MAP estimate and plugged in as
a fixed value during posterior sampling. We use m = 50 random features (hence 2m = 100 feature
dimensions) over the q = 10 latent√ dimensions. We summarise the RFF embedding through the
ARD-rescaled coordinates Xp ⊙ ℓ, which place inter-player distances on the scale of the induced
kernel (S19).

B.6    Model Priors
Table S1 lists the prior on each parameter, its role in the model, and whether it is sampled during
MCMC or held at its MAP estimate.

                                                30
 Parameter     Prior                 Role                                                  In MCMC
 σW            HalfNormal(1)         Scale of the covariate projection W                   MAP
 W             N (0, 1)              Covariate projection to the latent mean Zp⊤ W         sampled
 σX            HalfNormal(0.5)       Latent residual scale                                 MAP
                                     Latent residual, Xp = Zp⊤ W + σX εp
                     p
 εp            t4 (0, 1/2)                                                                 sampled
 ℓj            HalfNormal(1)         Latent-kernel ARD lengthscale, per latent dimension   MAP
 Ω             N (0, 1)              Random Fourier frequencies                            sampled
 γ kval        N (0, 1)              Peak-value weights, fk∗ (Xp )                         sampled
 γ kage        N (0, 1)              Peak-age weights, t∗k (Xp )                           sampled
 σc            IG(2, 1)              Peak-value process scale                              MAP
 σt            HalfNormal(0.5)       Peak-age process scale                     q √        sampled
 Ak            N (0, 1)              HSGP curvature weights, entries scaled by S( λl )     sampled
 αk            HalfNormal(1)         Curvature amplitude                                   sampled
 ℓk            log N (log 3, 0.7)    Curvature-kernel lengthscale                          sampled
 ρk            Uniform(−0.5, 0.5)    AR(1) autocorrelation of rpk (t)                      sampled
   k
 σAR           HalfNormal(0.3)       AR(1) innovation scale                                sampled
 rpk (t)       N (0, 1)              AR(1) innovations (non-centred)                       sampled
 rpk (t0 )     N (0, 1)              AR(1) initial state (non-centred)                     sampled
 σ2            IG(5, 600)            Gaussian observation variance, k ∈ G                  sampled
 τk2 , k ∈ P   Uniform(0, 1)         Beta precision                                        sampled
 τk2 , k ∈ B   Exponential(1)        Beta-binomial precision                               sampled
 τk2 , k ∈ C   Exponential(1)        Negative-binomial concentration                       sampled
 ηglob         N (log 0.04, 0.52 )   Global log baseline hazard                            sampled
 γglob         N (log 0.15, 0.32 )   Global log aging rate                                 sampled
 σexit         HalfNormal(0.5)       Baseline-hazard latent spread                         MAP
 ψexit         N (0, 1)              Log baseline-hazard weights                           sampled
 ψrate         N (0, 0.12 )          Log aging-rate weights                                sampled

Table S1: IG(α, β) is an Inverse-Gamma with shape α and rate β; tν (0, s) is a Student-t with ν
degrees of freedom and scale s. Weight sites are resolved in the random-feature space, so the peak
weights are 2m = 100-dimensional per metric and the curvature weights Ak are 2m × M ; the latent
coordinates themselves are q = 10-dimensional. The final column records whether a site is sampled
during MCMC or held fixed at its MAP estimate.

                                                   31
C     Hilbert Space Gaussian Processes
Traditionally, sampling from a full Gaussian Process is a computationally expensive procedure,
involving inverting a typically large N × N covariance matrix K. Solin and Särkkä (2019) showed,
however, that a reduced rank approximation of traditional stationary covariance matrices can be
utilized instead, reducing
                     √ 1/2 computational burden. The resulting approximation represents the func-
             PK
tion f (x) ≈ l=1 S( λl ) αl ψl (x) as a finite, weighted, linear combination
                                                                     √         of eigenvectors, ψl (x),
of the Laplacian on the√domain of x, with the weights αl ∼ N (0, S(√ l λ  )), arising as a function of
the spectral density S( λl ) evaluated at the associated eigenvalue λl of the stationary covariance
                                                                  √           √             2
matrix K. If K is the standard squared exponential kernel, S( λl ) = s2 2πωexp( −ω2 λl ) is the
spectral density of the squared exponential with length-scale parameter ω and variance parameter
s. As we increase the number of dimensions, this approximation does not scale well, as eigenvalues
for each d-tuple are needed. As such, this approach is useful for one-dimensional cases, where the
domain Ω is bounded on [−L, L]. In the one dimensionalqDirichlet boundary condition case, the
                                         jπ 2                      √
eigenvalues and eigenvectors are λj = ( 2L  ) and ψl (x) = L1 sin( λl (L + x)) respectively. For a
full treatment of this approach, please refer to Solin and Särkkä (2019).

                                                  32
D       Approximating a Separable Kernel
We make the claim that g(x, t) ≈ M                 K    i
                                     P                         P
                                       i=1 ϕi (x)( l=1 αl ψl (t)) has a separable covariance structure in
                                  ′   ′                                                     ′        ′
x and t. That is, Cov(g(x, t), g(x , t )) √
                                          can be factored into a product of kernels K(t, t )K(x, x ).
   First, we assume that αli ∼ N (0, S( λl )). Furthermore,
                                                           (     √
                                                               S( λl ) if l = z, k = i
                               Cov(αli , αzk ) =                                                                           (S21)
                                                               0       o.w

These assumptions align with the formulation outlined in Solin and Särkkä (2019).
                                            ′
   First, we will evaluate Cov(βi (t), βi (t )), where βi (t) = K     i
                                                               P
                                                                 l=1 αl ψl (t).

                                                                      K                   K
                                               ′                      X                   X              ′
                          Cov(βi (t), βi (t )) = Cov(                       αli ψl (t),         αli ψl (t ))               (S22)
                                                                      l=1                 l=1

Using (S21), we reach that
                                                                   K
                                                       ′           X           ′                p
                               Cov(βi (t), βi (t )) =                    ψl (t )ψl (t)S( λl )                              (S23)
                                                                   l=1
                                  PK     ′        √             ′                     ′
From Solin and Särkkä (2019), l=1 ψl (t )ψl (t)S( λl ) = K̃(t, t ) converges to K(t, t ) uniformly in
the univariate case. Since we only consider the time dimension, this suffices for our purposes.
                                           ′ ′
   Now, we can evaluate Cov(g(x, t), g(x , t )).
                                                                   M                       M
                                       ′   ′                       X                       X             ′         ′
                     Cov(g(x, t), g(x , t )) = Cov(                      ϕi (x)βi (t),              ϕi (x )βi (t ))        (S24)
                                                                   i=1                     i=1

Note that from (S21),
                                                           (P
                                                             K            √
                                                                l=1 S(        λl )ψl (t)2           if j = i
                         Cov(βi (t), βj (t)) =                                                                             (S25)
                                                            0                                       o.w

Thus,
                                                                M
                                           ′       ′                               ′                           ′
                                                              X                                                 
                       Cov g(x, t), g(x , t ) =                       ϕ(x)ϕ(x )Cov βi (t), βi (t )
                                                                i=1
                                                                            M
                                                                                                ′
                                                           = K̃(t, t′ )
                                                                            X
                                                                                   ϕ(x)ϕ(x )                               (S26)
                                                                            i=1

                                                                                                                       ′      ′
In our implementation, ϕi (x) is a linear (identity) projection, so M
                                                                                                       P
                                                                         i=1 ϕ(x)ϕ(x ) = Klin (x, x )
                            ′           ′
exactly. The product K̃(t, t )Klin (x, x ) therefore gives an exact separable covariance structure in
                                                          ′                              ′
the x dimension, while the HSGP approximation K̃(t, t ) converges uniformly to K(t, t ) from Solin
and Särkkä (2019).
                                                                                                   ′
    For the random Fourier feature projection (Appendix B.5), the x-factor 2m
                                                                                 P
                                                                                    i=1 ϕi (x)ϕi (x ) =
          ′
ϕ(x)⊤ ϕ(x ) is instead a random-feature approximation of the ARD kernel that converges as the
number of features grows (Rahimi and Recht, 2007).

                                                                   33
E    MCMC Convergence Diagnostics
Table S2 summarizes split-R̂ and tail effective sample size for the peak ages, peak values, concave
curves and latent embeddings.

                     Quantity                    n     median R̂   median tail-ESS
                      ∗
                     t (peak age)            46,767        1.077              144
                     f ∗ (peak value)        46,767        1.029              983
                     µptk (concave curve)   982,107        1.040              421
                     ∥Xp ∥ (latent)           2,751        1.049              367

Table S2: Convergence diagnostics over 50,400 posterior draws (4 chains). n is the number of cells
summarised. Entries are medians over those n cells. R̂ is the rank-normalized split-R̂ of Vehtari
et al. (2021). Tail-ESS is the smaller of the effective sample sizes of the indicators for the 5% and
95% quantiles (Vehtari et al., 2021).

                                                  34
F     Predictive Model Comparison
F.1    The value of joint modelling
Restricting the model to only use OBPM for predictive performance worsens the model’s perfor-
mance when compared to OBPM predicted from using all metrics (Table S3).

                            Restriction imposed           Stratified Next k
                                        ′′
                            concavity (µ ≤ 0)               +226 ± 73†
                            constant curvature per side       −5 ± 16
                            symmetry (αu = αd )              −68 ± 18†
                            metric set: 17 → 1              −355 ± 108†

Table S3: Every entry is the change in held-out log predictive density on OBPM alone; † marks
|∆| > 1.96 se∆ with the paired standard error of Vehtari et al. (2017). Negative means the restriction
costs accuracy. The first three rows are the curve-shape ladder of Table 2 of the main text on OBPM
observations rather than pooled across metrics. The last row is the identical model, priors, de-trend
and holdout fit to OBPM alone. Results are for the Stratified Next k scheme.

                                                  35
G     Model Validation
The five holdout schemes are implemented by selecting a 20% subset of players and masking their
observations as follows.

Hold-out Last k (k=2, 727 obs). The final 2 observed seasons of each selected player are ex-
    cluded from the training likelihood. The model therefore sees the player’s career up to but
    not including their most recent 2 seasons, then is scored on those withheld seasons. This
    mimics the real task of forecasting a player’s next 1–2 seasons from their career to date.

Hold-out First k (k=2, 757 obs). The first 2 observed seasons of each selected player are with-
    held. The model sees seasons 3 onward and must recover the player’s rookie and sophomore
    output. This tests whether the concave prior and latent embedding generalise backward in
    time and whether the model is well-calibrated for players with sparse early-career histories.

Random Interior (413 obs). For each selected player, a random 20% of their interior seasons
    (all but the first and last) are withheld. Unlike the last-k and first-k schemes, the model has
    observations on both sides of every gap, so this tests interpolation rather than extrapolation.

Hold-out Peak (450 obs). The single season of peak observed production for each selected
    player is withheld. This directly evaluates whether the model’s explicit peak parameteri-
    sation (t∗ , f ∗ ) allows it to recover the peak even when it is unobserved.

Stratified Next k (k=2, 1,484 obs). A balanced forecasting scheme that controls for career
     stage. Players are first binned into six career-length cohorts by their maximum observed
     age, using the thresholds ≥ 25, 27, 29, 31, 33, 35 (each player assigned to the highest cohort
     it qualifies for), with corresponding hold-out start ages of 23, 25, 27, 29, 31, 33. For every se-
     lected player the entire career tail from its cohort’s start age onward is removed from the
     training likelihood and predictions are scored on the next k withheld seasons, i.e. the cohort’s
     two-year window (ages 23–24, 25–26, . . . , 33–34). Unlike Hold-out Last k, whose scored sea-
     sons cluster at each player’s individual career end, this scheme evaluates the next-two-season
     forecast evenly across the full 23–34 age range, isolating how forecast quality varies by career
     stage.

                                                  36
H    Latent Dimension Ablation
To select the latent dimension q we fit the model for q ∈ {5, 10, 15, 20}, holding all other hy-
perparameters fixed, and scored each fit on held-out data under four of the holdout schemes of
Appendix G (Hold-out Last k, Hold-out First k, Random Interior and Hold-out Peak). Table S4
reports holdout RMSE with bias for every metric and value of q, one block per scheme.
   The ablation was carried out with MAP fits of the model under each holdout scheme rather
than with full posterior sampling.

                                              37
  Metric           q=5                q = 10               q = 15               q = 20
              RMSE (bias)         RMSE (bias)          RMSE (bias)          RMSE (bias)
  GP%        0.348 (-0.327)      0.365 (-0.346)     0.324 (-0.284)         0.329 (-0.261)
  USG%       0.055 (-0.004)     0.052 (+0.008)     0.049 (+0.001)          0.055 (-0.011)
  MPG       0.172 (+0.053)    0.138 (+0.038)         0.138 (+0.040)       0.140 (+0.003)
  OBPM      2.722 (+1.073)    1.950 (+0.437)         2.299 (+0.931)       2.300 (+0.728)
  DBPM      1.206 (+0.121)      1.054 (+0.060)     0.992 (+0.152)         1.050 (+0.192)
  BLK       0.282 (+0.241)      0.280 (+0.232)       0.320 (+0.221)     0.224 (+0.173)
  STL       0.871 (+0.859)    0.768 (+0.763)         0.882 (+0.852)       0.855 (+0.797)
  AST       1.058 (+1.052)    0.999 (+0.919)         1.017 (+0.944)       1.603 (+1.414)
  DREB      1.017 (+0.087)    1.002 (+0.361)         1.315 (+0.376)       1.346 (+0.322)
  OREB      0.632 (+0.554)      0.616 (+0.558)     0.500 (+0.482)         0.769 (+0.718)
  TOV       0.675 (+0.096)    0.547 (+0.217)         0.626 (+0.188)       0.601 (+0.149)
  FTA       2.041 (+1.823)      1.996 (+1.904)       2.147 (+1.927)     1.829 (+1.661)
  FG2A      3.696 (+1.350)      2.637 (+1.008)     2.329 (+0.775)         2.443 (+0.654)
  FG3A      1.034 (+0.636)    0.803 (+0.446)         0.861 (+0.227)       1.563 (+0.596)
  FT%        0.367 (-0.117)      0.375 (-0.104)     0.354 (-0.092)         0.420 (-0.116)
  FG2%      0.365 (+0.364)    0.202 (+0.202)         0.406 (+0.406)       0.497 (+0.496)
  FG3%      0.326 (+0.243)      0.323 (+0.236)       0.328 (+0.235)     0.304 (+0.202)

Table S4: Holdout RMSE and bias (in parentheses) by metric and latent dimension q — Hold-out
Last k scheme. Best q per metric in bold.

                                            38
I   Additional Figures and Tables

                                39
                          Figure S1: Between-player metric correlation.

Figure S2: Number of observed NBA seasons per player in our data window. The distribution is
heavily right-skewed. The mode of career lengths lasts a single season, 37% of players are observed
for two seasons or fewer, and the median career is four seasons against a maximum of 23. Exit
from the sample is strongly concentrated among short, low-production careers.

                                                40
Figure S3: Posterior production curves for Victor Wembanyama (top row) and his two nearest
latent-space neighbors, David Robinson (middle row) and Alonzo Mourning (bottom row), with
the four representative metrics (OBPM, FG2%, FG2A, FTA) as columns. The dashed vertical line
in the top row marks Wembanyama’s last observed season; the curve beyond it is a forecast. The
posterior mean of the aging curve fk (Xp , t) is the green line, with its 95% credible band in gray;
the light-blue band is the 95% interval for the full latent trajectory fk (Xp , t) + rpk (t), which adds
the per-player AR(1) term. Observed values are black points.

                                                  41
