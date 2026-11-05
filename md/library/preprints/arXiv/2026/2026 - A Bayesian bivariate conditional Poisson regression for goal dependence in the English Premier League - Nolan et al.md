<!-- source: library/preprints/arXiv/2026/2026 - A Bayesian bivariate conditional Poisson regression for goal dependence in the English Premier League - Nolan et al.pdf -->
<!-- item: https://arxiv.org/abs/2608.07168 -->
<!-- authors: Marcus Nolan, Wagner Barreto-Souza, Luiza S. C. Piancastelli, Raanju R. Sundararajan -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-05; equations, tables and figures are NOT preserved - consult the PDF for those -->

# A Bayesian bivariate conditional Poisson regression for goal dependence in the English Premier League

                                          A Bayesian bivariate conditional Poisson regression
                                          for goal dependence in the English Premier League
                                                      Marcus Nolan⋆ * , Wagner Barreto-Souza⋆†, Luiza S.C. Piancastelli⋆‡
                                                                         and Raanju R. Sundararajan♯§
                                                  ⋆
                                                      School of Mathematics and Statistics, University College Dublin, Republic of Ireland
                                                       ♯
                                                         Department of Statistics and Data Science, Southern Methodist University, USA

                                                                                        August 10, 2026
arXiv:2608.07168v1 [stat.AP] 7 Aug 2026




                                                                                              Abstract
                                                          Understanding the relationship between home and away goal counts in football pro-
                                                      vides valuable insights into match-level dynamics. While the influence of home advantage
                                                      is well-established, with historical records indicating roughly 50% of matches are won by
                                                      home teams (versus about 30% by the away team), properly determining the joint goal
                                                      distribution while accounting for key match factors remains under-explored. In this paper,
                                                      we develop a Bayesian bivariate Conditional Poisson (BCP) regression model to explicitly
                                                      capture the dependence between home and away goal counts, addressing a core limitation
                                                      of traditional football scoring models that assume independence or only allow for positive
                                                      correlation. The BCP regression is applied to the English Premier League (EPL) data span-
                                                      ning three seasons, incorporating stadium attendance and committed fouls by both teams
                                                      as regressors. Inference is conducted within a Bayesian framework, enabling interpretable
                                                      uncertainty quantification and model validation through posterior predictive checks. Our
                                                      results reveal a negative correlation between home and away goal counts and highlight an
                                                      asymmetry in how match attendance influences home versus away scoring.

                                          Keywords: Bayesian inference, committed fouls, home advantage, posterior predictive checks,
                                          stadium attendance.


                                          1           Introduction
                                          Football scores are naturally represented by a pair of non-negative integer-valued outcomes: the
                                          goals scored by the home team and those scored by the away team. These counts determine the
                                          match result, but they also reflect a sequence of strategic interactions. A goal may alter the pace
                                          of play, the amount of risk taken by each team, and the balance between attacking and defensive
                                              * email: marcus.nolan1234@gmail.com
                                              †
                                                email: wagner.barreto-souza@ucd.ie
                                              ‡
                                                email: luiza.piancastelli@ucd.ie
                                              §
                                                e-mail: rsundararajan@mail.smu.edu


                                                                                                  1
effort. Consequently, home and away goals are not expected to be independent. Quantifying
their dependence while accounting for match-level factors is important both for understanding
match dynamics and for producing realistic probabilistic descriptions of football scores.
    Poisson models provide a standard starting point for this problem. The seminal formu-
lation of Maher (1982) expressed the scoring intensities of the two teams in terms of their
attacking and defensive strengths and a home-effect parameter. Subsequent work relaxed the
assumption that the two goal counts are independent. In particular, Dixon and Coles (1997)
introduced an adjustment for dependence in low-scoring matches, while Karlis and Ntzoufras
(2003) showed that bivariate Poisson models can improve the representation of draws and other
score-line probabilities. These contributions established that the association between home and
away goals is an intrinsic feature of football data. However, the conventional bivariate Poisson
construction generates dependence through a shared Poisson component and therefore permits
only non-negative correlation. This restriction may be inappropriate when in-match tactical
responses produce negative dependence, for example when a team protects a lead by “parking
the bus”, and suppresses its opponent’s scoring opportunities.
    The statistical relationship between home and away goals is also connected to the well-
documented phenomenon of home advantage. Using English football data, Clarke and Norman
(1995) demonstrated that home advantage should be assessed after accounting for differences in
team strength, rather than solely through the percentage of home wins. International evidence
further indicates substantial geographical variation in the magnitude of home advantage, con-
sistent with a combination of crowd support, travel, familiarity, and territorial factors (Pollard,
2006). Crowd support is of particular interest because it may affect both player performance
and match officials. Experimental evidence reported by Nevill et al. (2002) showed that crowd
noise can influence referees’ assessments of challenges, providing a plausible pathway through
which spectators may affect fouls, disciplinary decisions, and ultimately scoring opportunities.
    The attendance restrictions imposed during the COVID-19 pandemic created an unusual
setting in which the role of spectators could be examined more directly. Across 17 countries
and 23 leagues, Bryson et al. (2021) found that matches played without crowds were associated
with fewer disciplinary sanctions against away teams, thereby reducing one channel of home
advantage. Similarly, Scoppa (2021) reported that the home advantage in goals, points, and
other performance measures was substantially smaller in matches played behind closed doors,
while foul and card decisions became more balanced between home and away teams. Evi-
dence from Germany suggests that the effect was not uniform across competitions: Fischer and
Haucap (2021) found a reduction in home advantage in the top division but not in the second
and third divisions. A broad analysis of European leagues by McCarrick et al. (2021) likewise
documented an overall decline in home advantage without spectators, although the magnitude
varied across leagues and outcomes.
    More recent statistical developments have addressed the joint distribution of home and away
goals. Koopman and Lit (2015) introduced a dynamic bivariate Poisson model to analyze En-
glish Premier League (EPL) match outcomes from the 2010–2011 and 2011–2012 seasons.
Piancastelli et al. (2023a) developed a flexible multivariate COM-Poisson model for analyzing
EPL matches and found that the absence of crowds was associated primarily with a reduction
in home-team scoring, rather than a comparable change in away-team goals. This asymme-
try is especially relevant for the present study: if attendance affects the two scoring processes
differently, a model should permit separate covariate effects for home and away goals while
simultaneously representing their dependence. Foul measures may provide additional infor-


                                                2
mation because they capture aspects of defensive pressure, interruptions of attacking play, and
possible crowd-related differences in officiating. Other recent contributions on the analysis of
the number of goals scored by home and away teams based on the COM-Poisson distribution
are due to Florez et al. (2025) and Zhang et al. (2026). To extend the baseline bivariate Poisson
literature, Michels et al. (2025) framed the Dixon-Coles model as a special case of the Sar-
manov family and proposed flexible multiplicative extensions tailored to the distinct scoring
dynamics of women’s football. Extending multivariate count modeling beyond goal counts
to match discipline, Philipson (2026) proposed a bivariate mean-parameterized COM–Poisson
copula model to evaluate referee heterogeneity and yellow card distributions across major Eu-
ropean leagues.
     To overcome the limitations of standard football scoring models, which often assume inde-
pendence or restrict dependence to positive correlation, this paper proposes a flexible Bivariate
Conditional Poisson (BCP) regression framework to model match-level dynamics and goal de-
pendence. Following Berkhout and Plug (2004) and the reparameterization by Piancastelli et al.
(2023b), the BCP specification accommodates an extended range of joint dependence, allowing
for a comprehensive analysis of English Premier League match dynamics, stadium attendance,
and foul-committed measures across pre-, during-, and post-pandemic seasons. A full Bayesian
inferential framework is explicitly developed to estimate the model parameters via Hamiltonian
Monte Carlo sampling. This procedure yields complete posterior distributions for both struc-
tural dependence and covariate parameters while facilitating rigorous model validation through
posterior predictive checks. The main contributions are listed below.

    • The flexible BCP formulation specifies one goal count marginally and the other condi-
      tionally, introducing a dependence parameter ϕ that captures both positive and negative
      associations.

    • Stadium attendance and foul-related variables enter the marginal mean specifications as
      covariates, enabling separate estimation of their associations with home and away scoring
      while simultaneously modeling goal dependence.

    • Inference is conducted within an empirical Bayes framework, providing posterior distri-
      butions for parameter uncertainty quantification and a natural basis for model evaluation
      via posterior predictive checks.

    • The empirical analysis uses 1,140 matches from the 2018–19, 2020–21, and 2023–
      24 seasons, representing pre-pandemic, restricted-attendance, and post-pandemic con-
      ditions. The aims are (i) to determine whether goal counts retain structural dependence
      after accounting for attendance and foul variables, (ii) to assess whether attendance is
      associated differently with the two teams’ scoring rates, and (iii) to evaluate whether the
      flexible dependence structure of the BCP model provides an informative description of
      EPL match outcomes.

   In a closely related paper, Petretta et al. (2025) proposed a bivariate conditional Pois-
son specification to model goal dependence in football matches. Although also inspired by
Berkhout and Plug (2004), their formulation adopts a more complex conditional structure for
which key statistical properties, such as marginal expectation and variance of one component,
and the resulting correlation, cannot be obtained in closed form. In contrast, our approach relies


                                                3
on a tractable, well-established parameterization where these moments and dependence met-
rics are analytically well-defined. A detailed discussion of these methodological distinctions is
provided in Section 3.
     The remainder of this article is organized as follows. Section 2 details the dataset of
1,140 English Premier League matches across pre-pandemic, restricted-attendance, and post-
pandemic seasons, presenting descriptive statistics and preliminary correlation analyses. Sec-
tion 3 introduces the Bivariate Conditional Poisson (BCP) regression framework, details the
log-linear covariate specifications for scoring intensities, and outlines the Bayesian inferen-
tial setup using empirical Bayes priors and Hamiltonian Monte Carlo sampling in Stan. Sec-
tion 4 reports the empirical findings, evaluating directional specifications (Home Goals →
Away Goals versus Away Goals → Home Goals) via leave-one-out cross-validation, inter-
preting posterior parameter distributions, and validating model fit through posterior predictive
checks. Finally, Section 5 summarizes the main conclusions, addresses study limitations, and
highlights potential avenues for future research.


2     Data
This section describes the construction of the dataset and presents preliminary empirical pat-
terns that motivate the modelling strategy developed in Section 3.

2.1   Description and pre-processing
The dataset comprises match-level observations from three English Premier League (EPL) sea-
sons: 2018–19, 2020–21, and 2023–24. These seasons were selected to represent, respectively,
the pre-pandemic period, the period in which most matches were played behind closed doors
because of COVID-19 restrictions, and the post-pandemic period. Their inclusion therefore
provides useful variation in stadium attendance with which to examine the association between
crowd presence and match outcomes.
    Match results and statistics were obtained from Football-Data.co.uk, while match
attendance figures were collected from FBref.com. The two sources were combined using
the relevant match identifiers. Each season contains 380 matches, yielding a total sample of
1,140 observations. The observed variables are the numbers of home and away goals (HG and
AG), stadium attendance (SA), and the numbers of fouls committed by the home and away
teams (HF and AF).

2.2   Preliminary insights
Table 1 reports selected summary statistics by season. Average attendance fell from 38,181
in the 2018–19 season to only 462 in the COVID-stricken 2020–21 season, reflecting the re-
strictions imposed during the pandemic, before returning to 38,613 for the 2023–24 season.
Over the same pre-pandemic-to-pandemic comparison, mean home goals declined from 1.57
to 1.35, whereas mean away goals increased slightly from 1.25 to 1.34. Although these de-
scriptive differences do not by themselves establish a causal crowd effect, they are consistent
with a reduction in home advantage when spectators were largely absent. Scoring was higher
for both teams in the 2023–24 season, when mean home and away goals reached 1.80 and 1.48,
respectively.

                                               4
                   Table 1: Premier League Summary Statistics by Season
     Season      Matches    Mean Home Goals       Mean Away Goals     Mean Attendance
     2018–19         380                  1.57                 1.25               38181
     2020–21         380                  1.35                 1.34                 462
     2023–24         380                  1.80                 1.48               38613


    Across the full sample, home wins are the most frequent match outcome (approximately
500 matches), followed by away wins (approximately 400) and draws (approximately 240);
see Figure 1a. This pattern provides descriptive evidence of home advantage and motivates a
closer examination of the factors associated with home-team scoring.
    Figure 1b compares the empirical distributions of home and away goals. Both are right-
skewed, with most teams scoring zero, one, or two goals and comparatively few teams record-
ing high scores. This discrete, non-negative structure supports the use of a Poisson-based
framework. The home-goal distribution is shifted slightly to the right of the away-goal dis-
tribution, in line with the higher average number of goals scored by home teams.




                      (a)                                             (b)

      Figure 1: Distributions of match outcomes (left) and home and away goals (right).

   As an initial assessment of the relationship between crowd presence and on-field discipline,
Pearson correlations were computed between attendance and the foul measures. The following
observations are made.
    • Attendance and home fouls were weakly negatively correlated (r = −0.1097, p = 0.0002);
    • Attendance and away fouls exhibited little evidence of an association (r = 0.0336, p =
      0.2572); and

                                              5
    • Attendance and total fouls were also not significantly correlated at the 5% level (r =
      −0.0499, p = 0.0924).

These associations are small and should be interpreted descriptively. Nevertheless, they sug-
gest that crowd presence may be related to home-team behaviour while having little direct
association with away or total fouls. Together with the interpretation of fouls suffered as a pos-
sible proxy for attacking pressure, or for an opponent’s inability to halt an attack legally, these
patterns motivate the inclusion of foul-related covariates in the regression models.


3    Methodology
Let Y1 and Y2 denote the two discrete random variables representing the number of goals
scored by the two teams in a given football match. A standard starting point in football score
modeling is the Poisson distribution. In the simplest case of marginal (independent) Poisson
models, it is assumed that Y j are independent Poisson random variables with means µ j , i.e.,
Y j ∼ Poisson(µ j ), j = 1, 2. The mean parameters µ j are typically modeled as functions of
match-specific covariates or latent team effects. For example, in the well-known Dixon-Coles
model (Dixon and Coles, 1997), letting subscripts H and A denote home and away teams re-
spectively, one assumes

                         YH ∼ Poisson(µH ),      µH = exp(γ + αH + βA ),

                            YA ∼ Poisson(µA ),       µA = exp(αA − βH ),
where α and β represent attack and defence strength parameters, respectively, and γ captures
the home advantage effect. Or similarly, in the presence of covariates xi for match i, Yi, j ∼
Poisson(µi, j ), with µi, j = exp(xi⊤ β j ), where β j is a vector of regression coefficients.
     Note that the above formulation does not model dependence between home and away goals,
which is an anticipated feature. Building on this observation, a natural idea would be to con-
sider the bivariate Poisson (BP) distribution. The BP is constructed as follows. Let Z0 , Z1 , Z2
be independent Poisson random variables with parameters λ0 , λ1 , λ2 , respectively, and define
Y1 = Z1 + Z0 , Y2 = Z2 + Z0 . The pair (Y1 , Y2 ) follows a BP distribution with parameter vec-
tor (λ0 , λ1 , λ2 ), and marginal distributions that remain Poisson; see Holgate (1964); Kawamura
(1984); Karlis and Ntzoufras (2003) for some examples. Dependence between Y1 and Y2 is
induced through the shared component Z0 , yielding Cov(Y1 , Y2 ) = λ0 ≥ 0. Observe that this
particular model formulation can only accommodate non-negative dependence, which is not
realistic when modeling competing teams’ goal counts at the match level.
     To address this limitation, we develop a Bayesian regression model based on the bivari-
ate conditional Poisson (BCP) distribution of Berkhout and Plug (2004), adopting the pa-
rameterization of Piancastelli et al. (2023a) specified in terms of the marginal means and a
parameter governing dependence. A (reparameterized) BCP random vector (Y1 , Y2 ), denoted
(Y1 , Y2 ) ∼ BCP(λ1 , λ2 , ϕ), admits the representation

                                          Y2 | Y1 = y1 ∼ Poisson µ2 eϕy1 ,
                                                                        
                    Y1 ∼ Poisson(λ1 ),                                                         (1)

where µ2 = λ2 exp{−λ1 (eϕ − 1)}, λ1 , λ2 > 0 and ϕ ∈ R. We denote (Y1 , Y2 ) ∼ BCP(λ1 , λ2 , ϕ).
Notably, the BCP model introduces a directional structure because the distribution of Y2 is

                                                 6
conditional on Y1 . In our context, the assignment of home and away goals to Y1 or Y2 reflects a
modeling choice regarding which component is assumed to drive the other. Both specifications,
home-to-away and away-to-home, will be considered and compared in Section 4.
    The joint probability function of a BCP random pair (Y1 , Y2 ), denoted by f (y1 , y2 |λ1 , λ2 , ϕ) ≡
P(Y1 = y1 , Y2 = y2 ), is given by
                              λy11 λy22
                                        exp −λ1 1 + y2 (eϕ − 1) − λ2 exp{−λ1 (eϕ − 1) + ϕy1 } + ϕy1 y2 ,
                                           n                                                          o
   f (y1 , y2 |λ1 , λ2 , ϕ) =
                                                               
                              y1 !y2 !
for (y1 , y2 ) ∈ {0, 1, . . .}2 . Naturally, as Y1 ∼ Poisson(λ1 ), its marginal mean and variance are
E(Y1 ) = Var(Y1 ) = λ1 . As for Y2 , its (unconditional) distribution is a mixed Poisson with
E(Y2 ) = λ2 and Var(Y2 ) = λ2 + λ1 λ2 (eϕ − 1)2 . The BCP covariance and correlation are respec-
tively given by (Piancastelli et al., 2023a)
                                         Cov(Y1 , Y2 ) = λ1 λ2 eϕ − 1 ,
                                                                     

and                                                            s
                                                                            λ1 λ2
                               Corr(Y1 , Y2 ) = eϕ − 1                                       ,
                                                           
                                                                   1 + λ2 (eλ1 (eϕ −1)2 − 1)
which implies that the direction of dependence is determined by the sign of ϕ. Illustrations
pertaining to the role of the ϕ parameter in Corr(Y1 , Y2 ) can be found in Piancastelli et al.
(2023b) (Section 2). In particular, we note that the correlation structure as a function of ϕ is
nonlinear, with values of ϕ closer to zero corresponding to stronger dependence even though
ϕ = 0 is the independence case. Further, the model is able to account for an extended range
of positive or negative correlations. More properties of the BCP distribution, such as joint
moments, can be found in Berkhout and Plug (2004).
    We now propose the BCP to model football scoring outcomes. Let yi = (yi,1 , yi,2 )⊤ represent
the goals scored by each team in match i, and assume that yi ∼ BCP(λ1,i , λ2,i , ϕ). The specific
assignment of home-to-away (Y1 : Home, Y2 : Away) and away-to-home (Y1 : Away, Y2 : Home)
are explored in Section 4.
    The collection of results across n matches will be denoted by y = (y1 , . . . , yn )⊤ . To ac-
count for the match-specific covariates introduced in Section 2, log-linear specifications are
introduced for λ1,i , λi,2 . Specifically,
                                log λ1,i = β0,1 + β1,Att log(Atti + 1) + β1,F FS i,1 ,
                                log λ2,i = β0,2 + β2,Att log(Atti + 1) + β2,F FS i,2 ,
where FS i, j refers to the fouls suffered by team j in match i, and Atti the corresponding stadium
attendance covariate, with the β’s denoting the associate regression coefficients. The attendance
covariate is log-transformed to manage numerical scaling, and the unit shift (log(Atti + 1))
ensures the transformation is well-defined during periods of zero attendance, i.e. closed doors
matches that occurred during the 2020-21 season. In what follows, X will denote the design
matrix containing these three (FS 1 , FS 2 , log(Att + 1)) covariates.
    Assuming that the matches are independent, the likelihood function for the collection of
results y is the product
                     y       y
                  n
                  Y λ1,ii,1 λ2,ii,2       n
                                                           ϕ                                 ϕ
                                                                                                                o!
f (y|β, ϕ, X) =                        exp −λ1,i 1 + yi,2 (e − 1) − λ2,i exp{−λ1,i (e − 1) + ϕyi,1 } + ϕyi,1 yi,2 ,
                                                                     
                  i=1
                        yi,1 !yi,2 !
                                                                                                             (2)

                                                            7
where β = (β0,1 , β1,Att , β1,F , β0,2 , β2,Att , β2,F )⊤ denotes the vector coefficients corresponding to the
covariates, and θ = (β⊤ , ϕ)⊤ denotes the entire parameter vector of interest.
    Before presenting the Bayesian inferential framework for BCP regression in the next sub-
section, we highlight key differences between our methodology and the approach proposed by
Petretta et al. (2025). Their work also introduces a bivariate conditional Poisson regression in-
spired by Berkhout and Plug (2004), but assumes a baseline joint distribution with the following
reparameterized stochastic representation:

                                       Y2 | Y1 = y1 ∼ Poisson λ2 eϕ logit(F(y1 )) ,
                                                                                 
                  Y1 ∼ Poisson(λ1 ),                                                            (3)
                                          x 
where λ1 , λ2 > 0, ϕ ∈ R, logit(x) = log         for x ∈ (0, 1), and F(·) being the cumulative dis-
                                          1−x
tribution function of Y1 . The primary distinction between stochastic representations (1) and (3)
lies in their respective dependence components, eϕy1 and eϕ logit(F(y1 )) . Under the former, math-
ematical tractability is preserved: key theoretical properties, including marginal means, vari-
ances, and the attainable correlation range, are available in closed form and well documented
(Berkhout and Plug, 2004; Piancastelli et al., 2023a). Under the latter, Petretta et al. (2025)
additionally consider a mixture of bivariate conditional Poisson distributions by swapping the
roles of Y1 and Y2 . However, as those authors acknowledge, the resulting marginal distributions
lack finite moments, an unappealing theoretical property when modeling goal counts, which
naturally possess finite moments. Beyond these analytical differences, the two approaches also
diverge in implementation: while Petretta et al. (2025) adopt a frequentist estimation scheme
with a distinct set of covariates, our work employs a Bayesian inferential framework.

3.1    Bayesian Inference
We here develop a Bayesian inference for the BCP regression model. Key advantages of adopt-
ing a Bayesian approach include directly interpretable uncertainty quantification of model pa-
rameters and the capacity to formally incorporate expert knowledge through the prior.
    Given the BCP likelihood defined in (2), the target posterior distribution is given by

                                  π(β, ϕ|y, X) ∝ f (y|β, ϕ, X)π(β)p(ϕ),                                   (4)

where π(β) and p(ϕ) denote the prior distribution specifications for β and ϕ, respectively.
     A number of approaches exist for choosing the prior distributions, such as (i) subjective
priors - which encode expert belief about the model parameters, (ii) objective (or noninforma-
tive) priors - designed to have minimal influence on the posterior, and (iii) empirical Bayes -
wherein parameters of prior distributions are set to certain empirical estimates obtained from
the data. In this work, we adopt the empirical Bayes approach, more specifically, letting the fre-
quentist maximum likelihood estimates (MLEs) inform the π(·) distributional setup as follows;
see Carlin and Louis (2000).
     We start from the canonical prior choice for the real-valued parameters, a zero-mean Gaus-
sian distribution. Let θ ∈ Θ denote the model parameter vector, θ̂ its corresponding MLE, and
sbe(θ̂) the associated frequentist standard error. We specify the prior for θ as θ ∼ N(0, sbe(θ̂)2 ) in
an empirical Bayes fashion. Centering the distribution at zero allows the prior to remain weakly
informative in the sense of Gelman et al. (2013), allowing the data to dominate posterior infer-
ence. Meanwhile, scaling the prior standard deviation using empirical standard errors yields a


                                                      8
hybrid prior that is empirically guided. Finally, we apply this empirical approach under together
with the assumption of prior independence for θ = (β, ϕ), so π(θ) = π(ϕ) 2j=1 k∈{0,Att,F} π(β j,k ).
                                                                            Q Q
    As is common in most non-trivial Bayesian models, the form of the posterior in (4) is
not known analytically, nor is it available in closed-form. Specifically, its normalizing con-
stant, often
           R referred to as the marginal likelihood or evidence, is the high-dimensional integral
p(y|X) = Θ f (y|θ, X)π(θ)dθ, rendering the posterior density intractable.
    To circumvent this, we adopt computational simulation methods as done typically. Markov
Chain Monte Carlo (MCMC) algorithms are ubiquitous in Bayesian inference; indeed, their
advancement has been a crucial driver for the wider adoption of Bayesian methods. Rather
than seeking a closed-form analytical solution for the posterior, MCMC techniques generate
a sequence of samples from the parameter space. This is achieved by constructing a Markov
chain designed to have the target posterior π(θ|y, X) as its stationary distribution. Crucially, be-
cause MCMC algorithms typically rely on ratios of posterior densities, such as the Metropolis-
Hastings ratio, the normalizing constant p(y|X) is avoided. Once the chain has reached its
stationary region, the resulting samples can be treated as samples from the posterior and used
to approximate summaries of interest.
    We perform MCMC sampling using Stan (Carpenter et al., 2017), a software which imple-
ments a computationally efficient MCMC algorithm called Hamiltonian Monte Carlo (HMC).
A feature of HMC is that it uses gradient information to explore high-probability regions of the
posterior effectively. Details on this sampler are provided in Hoffman and Gelman (2014). Our
code for implementing the BCP model in Stan is provided by the authors upon request.

3.2    Posterior predictive assessment
Another advantage of Bayesian inference is the ability to generate samples from the posterior
predictive distribution. This represents the distribution of new simulated and replicated data
(yrep ) that could be expected given the observed data (y). It is formally defined by integrating
the likelihood over the entire posterior distribution of the parameters.
                                              Z
                                 p(yrep |y) =    p(yrep |θ)p(θ|y)dθ

This is accomplished by first drawing a parameter sample, θ(s) , from the MCMC generated
posterior, and then drawing a new dataset, y(s)
                                             rep , from the likelihood function conditional on that
parameter sample. This process is automated in Stan. This results in a collection of replicated
datasets that can be used for model checking. It also allows for generating predictions that
allow interpretation of parameter uncertainty. Gelman et al. (1996) outline in depth the theory
on Posterior Predictive assessment.
    Posterior Predictive Checks (PPCs) are used to assess the model’s ability to match the ob-
served data. This is achieved by comparing the distribution of the observed data with the
distributions of replicated datasets. Graphical comparisons are assessed. Density plots of repli-
cated data on the observed data and comparing summary statistics between the observed and
replicated datasets are analysed. A model that fits well will generate replicated data that looks
similar to the observed data.




                                                 9
3.3    Model selection
The relative predictive performance of Bayesian models is compared using information criteria
that estimate out-of-sample predictive accuracy while penalizing for model complexity. The
Widely Applicable Information Criterion (WAIC) and the Leave-One-Out Cross-Validation
(LOO-CV), implemented via the ‘loo‘ package, are calculated. Models with lower WAIC or
LOO-CV values are considered to have better predictive performance. Vehtari et al. (2017)
outline the relevant theory. The Expected Log-Predictive Density (ELPD) is also calculated for
model comparison of the Bayesian methods to quantify and compare the out-of-sample pre-
dictive power of the conditional vs the independent model. The larger difference favours the
model with the higher ELPD score.
    Beyond purely statistical measures, the final model selection is guided by the interpretabil-
ity and theoretical coherence of the parameter estimates. The primary focus is on how com-
peting models capture the influence of the covariates and the dependence parameter ϕ. The
main goal is to select a model that provides a statistically valid and contextually meaningful
explanation of the data.


4     Results
In this section, we analyze the English Premier League (EPL) data introduced in Section 2 with
the Bayesian conditional bivariate Poisson (BCP) regression specified in Section 3. We study
the two possible direction attributions for the BCP: one in which the away team goals influence
the home team goals (A→H), and the other in which the home team goals influence the away
team goals (H→A). Bayesian inference is conducted in R using the rstan interface to the
Stan probabilistic programming platform. Sampling was performed across four chains, each
running 2,000 iterations, with the first 1,000 iterations discarded as warm-up. Empirical Bayes
priors specified in Section 3.1 are employed, although results are robust to the prior choice as
investigated by the authors but not reported here to save space.
    The following three models are fitted: (i) BCP A→H, (ii) BCP H→A, and (iii) independent
Poisson, and first compared via their leave-one-out expected log predictive density (ELPD-
LOO) performance. ELPD-LOO is a fully Bayesian selection criterion that quantifies how well
a model predicts unseen data. Its computation involves evaluating the expected log posterior of
each sample point i, i.e., match i, under a model that is fit without data from match i. Formally,

                                ELPDi = Eθ∼p(θ|y−i ) log p(yi | θ) ,
                                                                 

where p(θ | y−i ) is the posterior distribution of the parameter vector θ obtained by fitting
the model without the observations from match i. The total ELPD-LOO is then ELPDLOO =
Pn
   i=1 ELPDi . In practice, exact leave-one-out computation is approximated using Pareto-smoothed
importance sampling (PSIS-LOO) to avoid n model refits. Higher ELPD-LOO values are in-
dicative of better out-of-sample predictive performance. The ELPD-LOO estimates were BCP
A→H: −3552.0, BCP H→A: −3552.1 and Poisson: −3565.0. These results point to similar
performance shown by the two BCP models, with some indication of improvement when com-
pared to the independent Poisson model.
     Next, we study the directionality choice with ELPD-LOO metric by considering the condi-
tional log-probability of the causal component, i.e., ELPD2 = ni=1 ELPDi,2 where ELPDi,2 =
                                                                  P


                                                10
Eθ∼p(θ|y2,−i ,y1 ) log p(yi,2 | yi,1 , θ) . The H→A attribution yields an ELPD2 estimate of −1721.8
                                        
and the A→H direction yields −1817.2. Hence, while both models achieve similar joint predic-
tive performance, conditional predictive evaluation shows that the H→A model provides better
predictive accuracy, supporting this specification.
    The posterior estimates from the BCP H→A model are summarized in Table 2. The validity
of posterior inference was assessed using trace plots, the Gelman–Rubin statistic (R̂; Gelman
et al. (2013)), and the effective sample size (neff ). The trace plots show no apparent trends
or drifts, indicating that all four chains adequately explored the target distribution; these plots
are omitted here to save space. In addition, R̂ values are close to 1.0 for all parameters, and
effective sample sizes are sufficiently large.
    As described in Section 3, the parameter ϕ captures the dependency between home and
away team goals, with its sign indicating the direction of correlation and ϕ = 0 representing
independence. The posterior for ϕ is centered at −0.107, with a 95% credible interval that
excludes zero, indicating a statistically significant negative relationship. This suggests a sup-
pressive effect in which goals scored by the home team are associated with a reduction in the
expected number of away team goals, consistent with theoretical expectations.
    A visualisation of the posterior intervals corresponding to the covariate effects is provided
in Figure 2. Thick bars represent 50% credible intervals, thin bars 90% credible intervals, and
points indicate the posterior medians. We observe that the effect of (log) match attendance on
home team goals, represented by β1,Att , is positive and significant, whereas the corresponding
effect on away team goals, β2,Att , is centered at zero. This result empirically confirms the well-
known influence of crowd support on the performance of the home team. The effect of fouls
is also not symmetric. While the results on the parameter β1,AF indicate that away team fouls
positively impact home team goals, the reverse is not decisive. Specifically, the 95% credible
bands for β2,HF include zero. These findings highlight the asymmetric impact of contextual and
behavioral factors on team performance during matches. Such asymmetry strongly supports
the home advantage phenomenon, whereby the home team benefits from both crowd support
and opposition disruptions.

               Mean (SD)             95% CI
     β01      0.146 (0.084)     [−0.022, 0.311]
     β1,Att   0.024 (0.005)      [0.013, 0.034]
     β1,AF    0.012 (0.007)     [−0.001, 0.025]
     β02      0.232 (0.096)      [0.041, 0.419]
     β2,Att   0.000 (0.006)     [−0.011, 0.011]
     β2,HF    0.007 (0.007)     [−0.008, 0.022]
     ϕ        −0.107 (0.020)    [−0.147, −0.066]

    Table 2: Posterior summaries of
                                                     Figure 2: Posterior intervals for covari-
    the BCP H→A model parameters.
                                                     ate effects. Thick bars represent 50%
    Means, standard deviations (SD), and
                                                     intervals, thin bars 90% intervals, and
    95% credible intervals (CI) are re-
                                                     points indicate medians.
    ported for all parameters.



                                                11
Figure 3: Posterior predictive densities for the marginal means and variances of goals. Teams
are represented as columns and statistics as rows. Vertical solid lines indicate the observed
value.


    The fit of the BCP H→A model to the data is further assessed using a posterior predic-
tive exercise. Posterior predictive checks (PPCs) are a standard Bayesian tool for evaluat-
ing model adequacy, based on comparing the observed data to data replicated from the fit-
ted model. Specifically, parameter values are sampled from the posterior distribution, and
replicated datasets are generated from the likelihood conditional on these sampled parameters.
These replicated datasets are compared to the observed data, typically through a set of infor-
mative summary statistics. The choice of summary statistics is context-dependent and aims to
assess how well the model captures key features of the data. We consider the marginal mean
and variance of home and away team goals, the sample correlation between goals, and the
proportion of matches lost by the home team.
    Posterior predictive checks are repeated for all three competing models, BCP H→A, BCP
A→H, and the independent Poisson model, as this comparison is expected to highlight im-
portant distinctions. Figures 3 and 4 illustrate the posterior predictive results with densities
constructed from 4,000 replications. Models are indicated by different colors and line types,
while the vertical solid line represents the observed value of each summary statistic in the data.
Figure 3 shows the marginal means and variances, with teams as columns and statistics as
rows. The observed values lie within high posterior predictive density regions for all models,
indicating that all adequately capture the marginal mean and variance structures. However,
this changes when assessing the goals correlation and the proportion of home losses, shown in
Figure 4. The observed dependency between goals is not captured by the independent Poisson
model, consistent with our previous observation on the significance of ϕ. Incorporating this
dependency leads to a more realistic representation of match outcomes, with the BCP models
producing home loss proportions closer to those observed in the data.




                                               12
Figure 4: Posterior predictive densities for the correlation between home and away goals (left)
and the proportion of matches lost by the home team (right).


4.1    Discussion
The model comparisons provide evidence that allowing for negative dependence between home
and away team goals improves the representation of match-level dynamics from the EPL. The
two BCP specifications achieved nearly identical joint ELPD-LOO values (−3552.0 for A→H
and −3552.1 for H→A), with both models seen doing better than the independent Poisson
model. Thus, this joint ELPD-LOO criterion supports the inclusion of a dependence structure
but does not distinguish meaningfully between the two directional factorizations. By contrast,
the conditional ELPD comparison favored H→A (−1721.8 versus −1817.2), motivating our
focus on that specification. This direction should be interpreted as a predictive factorization of
the joint distribution, however, rather than as evidence that home team goals causally determine
away team goals.
    The posterior estimate of the dependence parameter provides clear evidence of a negative
association between the two scoring processes. Under the H→A specification, the posterior
mean of ϕ is −0.107, and its 95% credible interval, [−0.147, −0.066], excludes zero. Because
the conditional mean of away team goals contains the factor exp(ϕy1 ), a one-goal increase in
the home score multiplies the conditional expected number of away goals by exp(−0.107) ≈
0.899, holding the modeled intensities and covariates fixed. This corresponds to an estimated
reduction of approximately 10% in the conditional mean, not a 10% reduction in the probability
of scoring. The negative dependence may reflect tactical and behavioral adjustments within a
match, such as a team protecting a lead or its opponent changing its level of attacking risk.
    The results highlight an important advantage of the conditional construction of Berkhout
and Plug (2004). Conventional shared-component bivariate Poisson models restrict the covari-
ance to be non-negative, whereas the BCP model accommodates both signs of association. The
posterior predictive checks reinforce the practical importance of this flexibility. Specifically,
although all three models reproduce the marginal means and variances reasonably well, the
independent Poisson model fails to reproduce the observed goal correlation and yields a less
accurate distribution for the proportion of home losses. The BCP models therefore provide a
more realistic joint description of the match outcomes considered here.
    The covariate results also indicate a pronounced asymmetry between home and away scor-


                                               13
ing. The coefficient of log attendance is positive for home team goals, with a posterior mean
of 0.024 and a 95% credible interval of [0.013, 0.034], whereas the corresponding interval for
away team goals, [−0.011, 0.011], is centered at zero. Because attendance enters as the term
log(Attendance + 1) in a log-linear mean model, the home goal coefficient can be interpreted
approximately as an elasticity at positive attendance levels. More precisely, a 1% increase in
attendance is associated with about a 0.024% increase in the expected number of home goals,
with the other modeled quantities held fixed. The home-specific pattern is consistent with pre-
vious evidence that the presence of crowds primarily affects home-team scoring (Piancastelli et
al., 2023a). Nevertheless, attendance, pandemic conditions, and season are closely intertwined
in these data, so the coefficient should be interpreted as an adjusted association rather than a
causal crowd effect.
     Evidence for the foul-related covariates is also asymmetric. The posterior mean for the
association between away team fouls and home team goals is positive (0.012), but its 95%
credible interval, [−0.001, 0.025], includes zero. Likewise, the interval for the association be-
tween home team fouls and away team goals, [−0.008, 0.022], includes zero. The data therefore
suggest, at most, a weak positive association between away fouls and home scoring; they do
not establish a decisive foul effect at the 95% credible level. More detailed measures of match
events and team strength may be needed to separate the roles of attacking pressure, defensive
disruption, and refereeing behavior.


5    Conclusion
This paper developed a Bayesian bivariate conditional Poisson model to analyse 1,140 English
Premier League matches from the 2018–19, 2020–21, and 2023–24 seasons. Extending the
established Poisson-based literature on football scores (Maher, 1982; Dixon and Coles, 1997;
Karlis and Ntzoufras, 2003), the BCP formulation allows the association between home and
away goals to be either positive or negative while retaining separate regression structures for the
two scoring intensities. Bayesian estimation in Stan provides direct uncertainty quantification
for both the dependence parameter and the covariate effects.
    The results support three main conclusions. First, the BCP models provide better joint pre-
dictive performance than the independent Poisson model and more accurately reproduce the
observed correlation between home and away goals. Second, the preferred H→A specification
yields a negative dependence estimate, with the credible interval for ϕ lying entirely below
zero. Third, attendance is positively associated with home-team scoring but shows no clear as-
sociation with away-team scoring, a pattern consistent with earlier research on crowd presence
and home advantage (Piancastelli et al., 2023a). The foul-related effects are comparatively
uncertain because both 95% credible intervals include zero.
    These findings should be interpreted in light of the study design. The three selected sea-
sons provide substantial variation in attendance, but they also differ in pandemic conditions,
team composition, and the broader scoring environment. Moreover, the current specification
does not explicitly account for team-specific attacking and defensive strengths. The estimated
attendance effect therefore describes an association conditional on the included covariates and
should not, by itself, be interpreted as a causal effect of crowd size.
    Several extensions would strengthen the analysis. Hierarchical team-level attack and de-
fense effects, together with season-specific or time-varying parameters, could account for changes


                                               14
in team quality and scoring conditions; related seasonal structures are considered by Egidi et al.
(2018). Additional match-level information, including expected goals, red cards, rest periods,
tactical formations, weather, and referee characteristics, could help explain the mechanisms
underlying the estimated dependence. Applying the model to more seasons and to leagues
in other countries would also show whether the negative association and attendance asymme-
try generalize across competitions and playing styles. Finally, designs that compare matches
within narrower time windows or exploit more localized changes in spectator restrictions would
permit a more credible assessment of causal crowd effects.

Software and data availability. The Stan implementation of the BCP model can be obtained
from the authors upon request. The original match statistics and attendance records were ob-
tained from the publicly accessible sources identified in Section 2; the data-construction steps
needed to reproduce the analytical dataset are described there.

Conflict of interest. None to be declared.


References
B ERKHOUT, P., AND P LUG , E. (2004). A bivariate Poisson count data model using conditional
  probabilities. Statistica Neerlandica 58, 349–364.

B RYSON , A., D OLTON , P., R EADE , J. J., S CHREYER , D., AND S INGLETON , C. (2021).
  Causal effects of an absent crowd on performances and refereeing decisions during COVID-
  19. Economics Letters 198, 109664.

C ARLIN , B. P., AND L OUIS , T. A. (2000). Empirical Bayes: Past, present and future. Journal
  of the American Statistical Association 95, 1286–1289.

C ARPENTER , B., G ELMAN , A., H OFFMAN , M. D., L EE , D., G OODRICH , B., B ETAN -
  COURT, M., B RUBAKER , M., G UO , J., L I , P., AND R IDDELL , A. (2017). Stan: A proba-
  bilistic programming language. Journal of Statistical Software 76, 1–32.

C LARKE , S. R., AND N ORMAN , J. M. (1995). Home ground advantage of individual clubs
  in English soccer. Journal of the Royal Statistical Society: Series D (The Statistician) 44,
  509–521.

D IXON , M. J., AND C OLES , S. G. (1997). Modelling association football scores and inef-
   ficiencies in the football betting market. Journal of the Royal Statistical Society: Series C
   (Applied Statistics) 46, 265–280.

E GIDI , L., PAULI , F., AND T ORELLI , N. (2018). Combining historical data and bookmakers’
  odds in modelling football scores. Statistical Modelling 18, 436–459.

F ISCHER , K., AND H AUCAP, J. (2021). Does crowd support drive the home advantage in
   professional football? Evidence from German ghost games during the COVID-19 pandemic.
   Journal of Sports Economics 22, 982–1008.



                                               15
F LOREZ , M., G UINDANI , M., AND VANNUCCI , M. (2025). Bayesian bivariate Conway–
   Maxwell–Poisson regression model for correlated count data in sports. Journal of Quantita-
   tive Analysis in Sports 21, 51–71.

G ELMAN , A., M ENG , X.-L., AND S TERN , H. S. (1996). Posterior predictive assessment of
  model fitness via realized discrepancies. Statistica Sinica 6, 733–760.

G ELMAN , A., C ARLIN , J. B., S TERN , H. S., D UNSON , D. B., V EHTARI , A., AND RUBIN ,
  D. B. (2013). Bayesian Data Analysis (3rd ed.). Chapman & Hall/CRC.

H OFFMAN , M. D., AND G ELMAN , A. (2014). The no-u-turn sampler: Adaptively setting path
  lengths in Hamiltonian Monte Carlo. Journal of Machine Learning Research 15, 1593–1623.

H OLGATE , P. (1964). Estimation for the bivariate Poisson distribution. Biometrika 51, 241–
  245.

K ARLIS , D., AND N TZOUFRAS , I. (2003). Analysis of sports data by using bivariate Poisson
  models. Journal of the Royal Statistical Society: Series D (The Statistician) 52, 381–393.

K AWAMURA , K. (1984). Direct calculation of maximum likelihood estimator for the bivariate
  Poisson distribution. Kodai Mathematical Journal 7, 211–221.

KOOPMAN , S.J., AND L IT, R. (2015). A dynamic bivariate Poisson model for analysing and
 forecasting match results in the English Premier League. Journal of the Royal Statistical
 Society: Series A (Statistics in Society) 178, 167–186.

M AHER , M. J. (1982). Modelling association football scores. Statistica Neerlandica 36, 109–
  118.

M C C ARRICK , D., B ILALI Ć , M., N EAVE , N., AND W OLFSON , S. (2021). Home advantage
  during the COVID-19 pandemic: Analyses of European football leagues. Psychology of
  Sport and Exercise 56, 102013.

M ICHELS , R., Ö TTING , M., AND K ARLIS , D. (2025). Extending the Dixon and Coles model:
  an application to women’s football data. Journal of the Royal Statistical Society: Series C
  (Applied Statistics) 74, 167–186.

N EVILL , A. M., BALMER , N. J., AND W ILLIAMS , A. M. (2002). The influence of crowd
  noise and experience upon refereeing decisions in football. Psychology of Sport and Exercise
  3, 261–272.

P ETRETTA , M., S CHIAVON , L., AND D IQUIGIOVANNI , J. (2025). Modelling dependence in
   football match outcomes: Traditional assumptions and an alternative proposal. Statistical
   Modelling 25, 255–269.

P HILIPSON , P. (2026).         Yellow fever: an investigation into referee consistency in
   the ‘Big 5’ leagues of European football using a bivariate mean-parameterized Con-
   way–Maxwell–Poisson copula model. Journal of the Royal Statistical Society Series A:
   Statistics in Society, 1–20 (in press).



                                             16
P IANCASTELLI , L., F RIEL , N., BARRETO -S OUZA , W., AND O MBAO , H. (2023). Mul-
   tivariate Conway-Maxwell-Poisson distribution: Sarmanov method and doubly-intractable
   Bayesian inference. Journal of Computational and Graphical Statistics 32, 483–500.

P IANCASTELLI , L., BARRETO -S OUZA , W., AND O MBAO , H. (2023). Flexible bivariate IN-
   GARCH process with a broad range of contemporaneous correlation. Journal of Time Series
   Analysis 44, 206–222.

P OLLARD , R. (2006). Worldwide regional variations in home advantage in association football.
   Journal of Sports Sciences 24, 231–240.

S COPPA , V. (2021). Social pressure in the stadiums: Do agents change behavior without crowd
   support? Journal of Economic Psychology 82, 102344.

V EHTARI , A., G ELMAN , A., AND G ABRY, J. (2017). Practical bayesian model evaluation
  using leave-one-out cross-validation and WAIC. Statistics and Computing 27, 1413–1432.

Z HANG , N., R ASTELLI , R., AND F RIEL , N. (2026). Bayesian Conway-Maxwell-Poisson
  model with spike-and-slab priors for dispersed count data with application to football scores.
  arXiv preprint arXiv:2607.18009v1.




                                              17
