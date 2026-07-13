<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2021/2021 - A Bayesian marked spatial point processes model for basketball shot chart - Jiao et al.pdf -->

J. Quant. Anal. Sports 2021; 17(2): 77–90 

### Research article 

### Jieying Jiao*, Guanyu Hu and Jun Yan 

# A Bayesian marked spatial point processes model for basketball shot chart 

https://doi.org/10.1515/jqas-2019-0106 Received October 16, 2019; accepted November 29, 2020; published online December 24, 2020 

Abstract: The success rate of a basketball shot may be higher at locations where a player makes more shots. For a marked spatial point process, this means that the mark and the intensity are associated. We propose a Bayesian joint model for the mark and the intensity of marked point processes, where the intensity is incorporated in the mark model as a covariate. Inferences are done with a Markov chain Monte Carlo algorithm. Two Bayesian model comparison criteria, the Deviance Information Criterion and the Logarithm of the Pseudo-Marginal Likelihood, were used to assess the model. The performances of the proposed methods were examined in extensive simulation studies. The proposed methods were applied to the shot charts of four players (Curry, Harden, Durant, and James) in the 2017–2018 regular season of the National Basketball Association to analyze their shot intensity in the field and the field goal percentage in detail. Application to the top 50 most frequent shooters in the season suggests that the field goal percentage and the shot intensity are positively associated for a majority of the players. The fitted parameters were used as inputs in a secondary analysis to cluster the players into different groups. 

Keywords: MCMC; model selection; sports analytic. 

## 1 Introduction 

Shot charts are important summaries for basketball players. A shot chart is a spatial representation of the location and the result of each shot attempt by one player. 

*Corresponding author: Jieying Jiao, Department of Statistics, University of Connecticut, Storrs, CT, 06269, USA, E-mail: jieying.jiao@uconn.edu. https://orcid.org/0000-0001-85859938 

Guanyu Hu and Jun Yan, Department of Statistics, University of Connecticut, Storrs, CT, 06269, USA 

Good defense strategies depend on good understandings of the offense players’ tendencies to shoot and abilities to score. Reich et al. (2006) proposed hierarchical spatial models with spatially-varying covariates for shot attempt frequencies over a grid on the court and for shot success with shot locations fixed. Spatial point processes are commonly used to model random locations (e.g., Cressie 2015; Diggle 2013). Miller et al. (2014) used a low dimensional representation of related point processes to analyze shot attempt locations. Franks et al. (2015) combined spatial and spatio-temporal processes, matrix factorization techniques, and hierarchical regression models to analyze defensive skill. Many parametric models for spatial point process have been proposed in the literature, such as the Poisson process (Geyer 1999), the Gibbs process (Møller and Waagepetersen 2003), and the log Gaussian Cox process (LGCP) (Møller et al. 1998). When each point in a point process is companied with a random variable or vector known as mark, the resulting process is a marked point process (e.g., Banerjee, Carlin, and Gelfand 2014, Ch. 8). A shot chart can be modeled by a spatial marked point process with a binary mark showing the shot results. 

The frequency of successful shots may be higher at locations where a player makes more shot attempts. This positive association is expected from different angles. More frequent shots suggests higher competence level and, hence, higher shooting accuracy. Higher accuracy also encourages more shooting since it means higher reward. In behavioral science, the matching law states that individuals will allocate their behavior according to the relative rates of reinforcement available for each option (Baum 1974; Staddon 1978). It predicts higher proportion of three-point shots taken relative to all shots to be associated with higher proportion of three-point shots scored relative to all shots scored (Alferink et al. 2009; Vollmer and Bourret 2000). The association might be more obvious for players who get fewer minutes and may be more selective to “prove their worth”. It might be less so for players who have possession more often and may be less selective. Team strategies could affect the association in two opposite directions. Players with high three-point shot accuracy are more likely to be arranged in areas beyond the 

78 J. Jiao et al.: A Bayesian marked spatial point processes model 

three-point line. This is in favor of the positive association. On the other hand, optimal shot selection strategy requires all shot locations to have the same marginal shot efficiency for the whole team (Skinner and Goldman 2015), which may not be consistent with shot selections for individual players. A quantitative measure of the association for a player will be helpful for understanding the player’s performance and suggesting directions for improvement at both player level and team strategies level. 

We consider marked spatial point processes where the mark distributions depend on the point pattern. There are two approaches to model this dependence. Location dependent models (Mrkvička et al. 2011) are observation driven, where the observed point pattern is incorporated into characterizing the spatially varying distribution of the mark. Intensity dependent models (Ho and Stoyan 2008) are parameter driven, where the intensity instead of the observed point pattern characterizes the distribution of the mark at each point in the spatial domain. For basketball shot charts, no work has jointly modeled the intensity of the shot attempts and the results of the attempts. 

The contribution of this paper is twofold. First, we propose a Bayesian joint model for marked spatial point processes to study the association between shot intensity and shot accuracy. In particular, we use a nonhomogeneous Poisson point process to model the spatial pattern of the shot attempts and incorporate the shot intensity as a covariate in the model of shot accuracy. Inferences are made with Markov chain Monte Carlo (MCMC). The deviance information criterion (DIC) and the logarithm of the pseudo-marginal likelihood (LPML) are used to assess the fitness of our proposed model. Our second contribution is the analyses of four representative – players and the top 50 most frequent shooters in the 2017 2018 regular season of the National Basketball Association (NBA). The shot intensity of each player is captured by a set of intensity basis constructed from historical data which represents different shot types such as long two-pointers and corner threes, among others (Miller et al. 2014). For a majority (about 80%) of the these players, the results support a significant positive association between the shot accuracy and shot intensity. The fitted coefficients are then used as input for a clustering analysis to group the top 50 most frequent shooters in the season, which provides insights for game strategies and training management. 

The rest of the paper is organized as follows. In Section 2, the shot charts of selected players from the 2017–2018 NBA regular season, along with research questions that such data can help answer, are introduced. In Section 3, we develop the Bayesian joint model of marked point process. Details of the Bayesian computation are presented in 

Section 4, including the MCMC algorithm and the two model selection criteria. Extensive simulation studies are summarized in Section 5 to investigate empirical performance of the proposed methods. Applications of the proposed methods to four NBA players are reported in Section 6. Section 7 concludes with a discussion. 

## 2 Shot charts of NBA players 

We focus on the 2017–2018 regular NBA season here. The website NBAsavant.com provides a convenient tool to search for shot data of NBA players, and the original data are a consolidation between the NBA statistics (https:// stats.nba.com) and ESPN’s shot tracking (https:// shottracker.com). For each player, the available data contains information about each of his shots in this season including game date, opponent team, game period when the shot was made (four quarters and a fifth period representing extra time), minutes and seconds left to the end of that period, success indicator or mark (0 for missed and 1 for made), shot type (two-point or three-point shot), shot distance, and shot location coordinates, among others. Euclidean shot distances were rounded to foot. 

We chose four famous players with quite different styles: Stephen Curry, Kevin Durant, James Harden and LeBron James. Figure 1 shows Curry’s shot locations with the shot success indicators as a demonstration. The total number of shots was in the range of 740 (Curry) to 1409 (James). Curry has the highest proportion of three-point shots (57%) while James made the highest proportion of two-point shots (75%). The field goal percentage ranged from 45 (Harden) to 52% (James). As shown in Figure 1, most of the shots were made close to the rim or out of but close to the three-point line. This is expected since shorter distance should give higher shot accuracy for either twopoint or three-point shots. 

The shot chart of each player can be modeled by a marked point process that captures the dependence between the binary mark and the intensity of the shots. Through analyses of the selected NBA players, we address the following questions: How to characterize the shot pattern of individual players? What are the factors, such as shot location, time remaining, period of the game, and the level of the opponent, that may affect the shot accuracy? Is there a positive association between shot accuracy and shot intensity of some players? How often is the positive association seen among the most frequent shooters? Is this positive association different between two-point versus three-point shots? Can the players be grouped by their shooting styles? These questions may not be completely 

79 

J. Jiao et al.: A Bayesian marked spatial point processes model 

















































answered, but even partial answers would shed lights on understanding the game and the players for better game strategies and training management. 

## 3 Bayesian marked spatial point process model 

function of the process. The likelihood of the observed locations S is 



Covariates can be incorporated into the intensity by setting 



The observed shot chart of a player can be represented by (S, M), where S is the collection of the locations of shot attempts (x and y coordinates) and M is the vector of the corresponding marks (1 means success and 0 means failure). Assuming that N shots were observed, we have S = (s1, s2, …, sN ) and M = (m(s1), m(s2), …, m(sN )). 

### 3.1 Marked spatial point process 

We propose to model (S, M) by a marked spatial point process. The shot locations S are modeled by a nonhomogeneous Poisson point process (e.g., Diggle 2013). Let B ⊂ R<sup>2</sup> be a subset of the half basketball court on which we are interested in modeling the shot intensity. A Poisson point process is defined such that N(A) = ∑<sup>N</sup> i=1<sup>1(si ∈A)foranyA ⊂BfollowsaPoissondistribution</sup> with mean λ(A) = ∫Aλ(s)ds, where λ(⋅) defines an intensity 

where λ0 is a baseline intensity, X(si) is a p × 1 spatially varying covariate vector, and β is the corresponding coefficient vector. 

Next we consider modeling the success indicator (mark). It is natural to suspect that the success rate of shot attempts is higher at locations with higher shot intensity, suggesting an intensity dependent mark model. In particular, the success indicator is modeled by a logistic regression 



where λ(si) is the intensity defined in (1) with a scalar coefficient ξ, Z(si) is a q × 1 covariate vector evaluated at ith data point (Z does not need to be spatial, like period covariates), and α is a q × 1 vector of coefficient. 

With Θ = (λ0, β, ξ , α), the joint likelihood for the observed marked spatial point process (S, M) is 

80 

J. Jiao et al.: A Bayesian marked spatial point processes model 



### 3.2 Prior specification 

Vague priors are specified for model parameters. For λ0, the gamma distribution is conjugate prior (e.g., Leininger et al. 2017). For β, ξ, or α, there is no conjugate prior and we specify a vague, independent normal prior. In summary, we have 



where G(a, b) represents a Gamma distribution with shape a and rate b, respectively, MVN(0, Σ) is a multivariate normal distribution with mean vector 0 and variance matrix Σ, (a, b, σ<sup>2</sup> β<sup>, σ2</sup> ξ<sup>, σ</sup> α<sup>2) are hyper-parameters to be specified,</sup> and Ik is the k-dimensional identity matrix. 

## 4 Bayesian computation 

### 4.1 The MCMC sampling schemes 

The posterior distribution of Θ is 



where π(Θ) = π(λ0)π(β)π(ξ )π(α) is the joint prior density as specified in (4). In practice, we used vague priors with hyper-parameters σ<sup>2</sup> β<sup>= σ2</sup> ξ<sup>= σ2</sup> α<sup>= 100 and a = b = 0.01</sup> in (4). 

To sample from the posterior distribution of Θ in (5), an Metropolis–Hasting within Gibbs algorithm is facilitated by R package nimble (de Valpine et al. 2017). The loglikelihood function of the joint model used in the MCMC iteration is directly defined using the RW_llFunction() sampler. The integration in the likelihood function (3) does not have a closed-form. It needs to be computed with a Riemann approximation by partitioning B into a grid with a sufficiently fine resolution. Within each grid box, the integrand λ(s) is approximated by a constant. Then the integration of λ(s) becomes a summation over all of the grid boxes. 

### 4.2 Bayesian model comparison 

Toassess whether theintensity term isnecessary inthe mark model (2), model comparison criteria is needed. Within the Bayesian framework, DIC (Spiegelhalter et al. 2002) and LPML (LPML; Geisser and Eddy 1979; Gelfand and Dey 1994) are two well-known Bayesian criteriafor model comparison. Using the method of Zhang et al. (2017), each criterion for the proposed joint model can be decomposed into one for the intensity model and one for the mark model conditioning on the point pattern for more insight on the model comparison. 

The DIC for the joint model is 



where the deviance Dev is the negated loglikelihood function in Equation (3), Dev is the mean of the deviance evaluated at each posterior draw of the parameters, Θ is the posterior mean of Θ, and pD is known as the effective number of parameters. For the intensity model and the conditional mark model, the DIC can be computed with deviance, respectively, 



where λ = (λ(s1), λ(s2), …, λ(sN )), and f (m(si)|λ(si), α, ξ , Z(si)) is the conditional probability mass function of m(si) given (λ(si), α, ξ , Z(si)). Clearly, the DIC for joint model is the summation of the DIC for the intensity model and the DIC for the conditional mark model. Models with smaller DIC are better models. 

Calculation of the LPML for point process models is challenging because the usual conditional predictive ordinate (CPO) based on the leaving-one-out assessment is not applicable where the number of points N is random. Hu et al. (2019) recently suggested a Monte Carlo method to approximate the LPML for the intensity model as 

N LPMLintensity = ∑ logλ<sup>˜</sup> (si) − ∫λ(s)ds , (8) i=1 B −1 where λ<sup>˜</sup> (si) = (K1<sup>∑</sup> k<sup>K</sup> =1<sup>λ(k)(si)−1)</sup> , λ(s) = K1<sup>∑</sup> k<sup>K</sup> =1<sup>λ(k)(s),and</sup> {λ<sup>(k)</sup> (si) : k = 1, 2, …, K} is a posterior sample of size K of the parameters from the MCMC. The LPML for the conditional mark model can be calculated as usual (Chen, Shao, and Ibrahim 2000, Ch. 10). For the ith data point, define 

81 

J. Jiao et al.: A Bayesian marked spatial point processes model 



where {α<sup>(K)</sup> , ξ<sup>(K)</sup> : k = 1, 2, …, K} is a posterior sample of size K of the parameters from the MCMC. Then the LPML on mark model is 



The LPML for the joint model is then calculated as the sum of (8) and (9). Models with higher LPML are better models. 

## 5 Simulation studies 

To investigate the performance of the estimation, we generated data from a non-homogeneous Poisson point process defined on a square B = [ −1, 1] × [ −1, 1] with intensity λ(si) = 100λ0 exp(β1xi + β2yi), where si = (xi, yi) ∈ B is the location for every data point. For each si, i = 1, …, N, the mark m(si) follows a logistic model with two covariates in addition to λ and intercept: 



The parameters of the model were designed to give point counts that are comparable to the basketball shot chart data. We fixed (β1, β2) = (2, 1), ξ = 0.5, α0 = 0.5, and α2 = 1. Three levels of α1 were considered, α1 ∈ {0.8, 1, 2}, in order to compare the performance of the estimation procedure under different magnitudes of the coefficients in the mark model. Two levels of λ0 were considered, λ0 ∈ {0.5, 1}, which controls the mean of the number of points on B. It is easy to integrate in this case the intensity function over B to get the average number of points being 850 and 1700, respectively, for λ0 = 0.5 and 1. The numbers are approximately in the range of the NBA basketball shot charts in Section 2. In the mark model, covariate Z1 was generated from the standard normal distribution; two types of Z2 were considered, standard normal distribution or Bernoulli with rate 0.5. The resulting range of the Bernoulli rate of the marks was within (0.55, 0.78) for all the scenarios. 

For each setting, 200 data sets were generated. R package spatstat (Baddeley et al. 2005) was used to generate the Poisson point process data with the given intensity function. The priors for the model parameters were set to be (4) with the hyper-parameters σ<sup>2</sup> β<sup>= σ2</sup> ξ<sup>= σ</sup> α<sup>2=</sup> 100 and a = b = 0.01. The grid used to calculate the integration in likelihood function had resolution 100 × 100. For 

each data set, a MCMC was run for 20,000 iterations with the first 10,000 treated as burn-in period. For each parameter, the posterior mean was used as the point estimate and the 95% credible interval was constructed with the 2.5% lower and upper quantiles of the posterior sample. 

Tables 3 and 4 in Appendix summarize the simulation results for the scenarios of standard normal Z2 and Bernoulli Z2, respectively. The empirical bias for all the settings are close to zero. The average posterior standard deviation from the 200 replicates is very close to the empirical standard deviation of the 200 point estimates for all the parameters, suggesting that the uncertainty of the estimator are estimated well. Consequently, the empirical coverage rates of the credible intervals are close to the nominal level 0.95. As α1 increases, the variation increases in the mark parameter estimates but does not change in the intensity parameter estimates. As λ0 increases, the variations of the estimates for both intensity and mark parameters get lower. Between the continuous and binary cases of Z2, the variation in the estimates is higher in the latter case, especially for the coefficient of Z2. 

## 6 NBA players shot chart analysis 

### 6.1 Covariates construction 

To capture the shot styles of individual players in their shot intensity model, we follow Miller et al. (2014) to construct basis covariates that are interpreted as archetypal intensities or “shot types” used by the players. The focus is on the 35 ft by 50 ft rectangle on the side of the backboard in the offensive half court. The origin of the Cartesian coordinates (x, y) is replaced at the bottom left corner so that x ∈ [0, 50] and y ∈ [0, 35]. The rectangle was evenly partitioned into 50 × 35 grid boxes of 1 ft by 1 ft. Our bases construction is slightly different from that of Miller et al. (2014) in the preparation for the Nonnegative matrix factorization (NMF). First, we used a kernel estimation instead of an LGCP model to estimate the 50 × 35 intensity matrix of each individual players, which is easier to compute and more accurate in the sense of intensity fitting accuracy. Second, we used historical data instead of the current season data. In particular, a kernel estimate of the 50 × 35 intensity matrix for each of the 407 players in the – previous season (2016 2017) who had made over 50 shots was used as input for the NMF. As in Miller et al. (2014), we obtained 10 bases using R package NMF (Gaujoux and Seoighe 2010). 

Figure 2 displays the 10 nonnegative matrix bases that can be used as covariates for the intensity matrix fitting. 

82 

J. Jiao et al.: A Bayesian marked spatial point processes model 



Figure 2: Intensity matrix bases heat plots. 

They are similar to those in the literature (Franks et al. 2015; Miller et al. 2014). Each basis is nicely interpreted as a certain shot type. For example, basis 1 is long two-points, bases 2–3 are left/right wing threes, bases 4–5 are left/ right/center restricted area two-points, basis 7 is top of key threes, basis 8 is center threes, basis 9 is corner threes, and basis 10 is mid-range twos. When used as covariates in modeling individual shot intensity, their coefficients characterize the shooting style of each player. 

The influence of intensity on shot accuracy might be different for different shot type. Players’ shot selection may be biased towards three point shot for higher reward (Alferink et al. 2009; Skinner and Goldman 2015). This can result in higher intensity for three-point shot at locations with not high accuracy. To capture this tendency, an interaction term between the intensity and the shot type is introduced to the mark model. In addition to intensity and interaction term between intensity and shot type, other covariates in the mark model include distance to the basket 

and non-spatial covariates such as seconds left to the end of the period, dummy variables for five different periods with first period as reference, and the indicator of opponent made to the playoff in the last season. 

### 6.2 Model comparison 

– The joint model (1) (2) was fitted for each player with the hyper-parameters in (4) set as σ<sup>2</sup> β<sup>= σ2</sup> ξ<sup>= σ</sup> α<sup>2= 100and</sup> a = b = 0.01. The numerical integration in evaluating the joint log-likelihood (3) was based on the same 50 × 35 grid as that used in constructing the basis shot styles from NMF. To check the importance of intensity as covariate in the mark component, we also fitted the model with the restriction ξ = 0. For each model fitting, 60,000 MCMC iterations were run. The first 20,000 were discarded as the burn-in period and the rest were thinned by 10, which led to an MCMC sample of size 4000. The trace plots of the MCMC 

83 

J. Jiao et al.: A Bayesian marked spatial point processes model 

were checked and the convergence of all the parameters were confirmed. The reported results were obtained from a second run after insignificant covariates were removed to avoid possible collinearity among some variables; for example, basis 6 (restricted area two-points) appears to be well approximated by a combination of basis 4 (left restricted area two-points) and basis 5 (right restricted area two-points). 

Table 1 summarizes the DIC and LPML for the full joint model and its two components. The smallest absolute difference is 8.6 in DIC and 4.2 in LPML for Durant; the largest absolute difference is 41.2 in DIC and 20.4 in LPML for James. The DIC has a rule of thumb similar to AIC in decision making (Spiegelhalter et al. 2002, p. 613): a difference larger than 10 is substantial and a difference about 2–3 does not give an evidence to support one model over the other. For LPML, a difference less than 0.5 is “not worth more than to mention” and larger than 4.5 can be considered “very strong” (Kass and Raftery 1995). With these guidelines applied to DIC and LPML, the mark model with shot intensity included as a covariate has a clear advantage relative to the model without it for Durant, Harden, and James, but not for Curry, an interesting result which will be discussed in the next subsection. The difference in DIC and LPML between the models with and without ξ = 0 comes from the mark component. The two criteria for the intensity component are almost the same with and without ξ = 0. This is expected because the marks may contain little information about the intensities, and intensity fitting results are not influenced by the mark model significantly. 

In order to have a direct comparison of improvement of mark model by using the preferred model, we calculate the mean squared error (MSE) of fitted mark models with and without intensity as a covariate. The preferred models for 

all four players, which are intensity independent model for Curry and intensity dependent model for other three players, can reduce the MSE by 2.7, 1.3, 2.0, and 7.0%. 

### 6.3 Fitted results 

Table 2 summarizes the posterior mean, posterior standard deviation, and the 95% highest posterior density (HPD) credible intervals for the regression coefficients in the models for Curry, Durant, Harden, and James as selected by the DIC and LPML. Only significant covariates are displayed as determined by whether or not the 95% HPD credible intervals cover zero in the first run. The reported results were from the second run after insignificant covariates were removed. 

The coefficients of the 10 basis shot styles in the intensity model describe the composition of each individual player’s shot style. After being exponentiated, they represent a multiplicative effect on the baseline intensity. So they are comparable across players as a relative scale. The four players are quite different in the coefficients of a few well-interpreted bases. Curry’s rate of corner threes was the highest among the four. Durant has the least rate of corner threes and highest rate of long/mid-range two-pointers. Harden had the least rate of long two-pointers and highest rate of top of key threes. Curry and Harden had less two point shots but more three point shots than Durant and James. James seemed to prefer to shot on the left side of court for three point shots more than the other three players. All four had high rate of center threes. Figure 3 (upper) shows the fitted intensity surfaces of the four players. These results echo the findings in earlier works (Franks et al. 2015; Miller et al. 2014). 

Table : Summaries of DIC and LPML for the models for Curry, Durant, Harden, and James with and without ξ = . 

||||Curry|Durant|Harden|James|
|---|---|---|---|---|---|---|
|Joint model|DIC|ξ ≠|.|.|.|.|
|||ξ=|.|.|.|.|
||LPML|ξ ≠|−.|−.|−.|−.|
|||ξ=|−.|−.|−.|−.|
|Intensity|DIC|ξ ≠|.|.|.|−.|
|||ξ=|.|.|.|−.|
||LPML|ξ ≠|−.|−.|−.|.|
|||ξ=|−.|−.|−.|.|
|Mark|DIC|ξ ≠|.|.|.|.|
|||ξ=|.|.|.|.|
||LPML|ξ ≠|−.|−.|−.|−.|
|||ξ=|−.|−.|−.|−.|



84 

J. Jiao et al.: A Bayesian marked spatial point processes model 

Table : Estimated coefficients in the joint models for Curry, Durant, Harden, and James. 

|Player|Model|Covariates|Posterior mean|Posterior SD|% Credible Interval|
|---|---|---|---|---|---|
|Curry|Intensity|Baseline (λ)|.|.|(.,.)|
|||Basis(long two-pointers)|.|.|(.,.)|
|||Basis(right wing threes)|.|.|(.,.)|
|||Basis(left wing threes)|.|.|(.,.)|
|||Basis(left restricted area)<br>|.|.|(.,.)<br>|
|||Basis(top of key threes)<br>|.|.|(.,.)<br>|
|||Basis(center threes)|.|.|(.,.)|
|||Basis(corner threes)|.|.|(.,.)<br>|
||Mark|Intercept|−.|.|(−.,.)|
|||Distance|−.|.|(−.,−.)|
|Durant|Intensity|Baseline (λ)|.|.|(.,.)|
|||Basis(long two-pointers)|.|.|(.,.)|
|||Basis(right wing threes)|.|.|(.,.)|
|||Basis(left wing threes)|.|.|(.,.)|
|||Basis(left restricted area)|.|.|(.,.)|
|||Basis(restricted area)|−.|.|(−.,−.)|
|||Basis(top of key threes)|.|.|(.,.)|
|||Basis(center threes)|.|.|(.,.)|
|||Basis(corner threes)|−.|.|(−.,−.)|
|||Basis(mid-range twos)|.|.|(.,.)|
||Mark|Intercept|−.|.|(−.,−.)|
|||Intensity (λ)|.|.|(.,.)|
|||Distance|−.|.|(−.,−.)|
|Harden|Intensity|Baseline (λ)|.|.|(.,.)|
|||Basis(long two-pointers)|−.|.|(−.,−.)|
|||Basis(right wing threes)|.|.|(.,.)|
|||Basis(left wing threes)|.|.|(.,.)|
|||Basis(left restricted area)|.|.|(.,.)|
|||Basis(restricted area)|.|.|(.,.)|
|||Basis(top of key threes)|.|.|(.,.)|
|||Basis(center threes)|.|.|(.,.)|
|||Basis(mid-range twos)|.|.|(.,.)|
||Mark|Intercept|−.|.|(−.,−.)|
|||Intensity (λ)|.|.|(.,.)|
|James|Intensity|Baseline (λ)|.|.|(.,.)|
|||Basis(long two-pointers)|.|.|(.,.)|
|||Basis(left wing threes)|.|.|(.,.)|
|||Basis(left restricted area)|.|.|(.,.)|
|||Basis(restricted area)|.|.|(.,.)|
|||Basis(top of key threes)|.|.|(.,.)|
|||Basis(center threes)|.|.|(.,.)|
|||Basis(corner threes)|.|.|(.,.)|
|||Basis(mid-range twos)|.|.|(.,.)|
||Mark|Intercept|−.|.|(−.,−.)|
|||Intensity (λ)|.|.|(.,.)|
|||Distance|−.|.|(−.,−.)|



The results from the mark model conditioning on the intensity are the major contribution of this work. All nonspatial covariates were insignificant and were dropped from the model, except shot distance. The coefficient of the intensity was found to be significantly positive for Durant, Harden, and James, but not for Curry. That is, for the 

players excluding Curry, shot accuracy was higher where they shot more frequently. The interaction between the intensity of shot type (two- vs. three-point) was not significant for any player, suggesting that, for those whose shot frequency and shot accuracy were positively associated, the association was not influenced directly by shot 

85 

J. Jiao et al.: A Bayesian marked spatial point processes model 



Figure 3: Fitted shot intensity surfaces (upper) and expected score surfaces (lower) of Curry, Durant, Harden and James on the same scale. Redder means higher. 

rewards. The magnitude of coefficient of the intensity shows how strong this dependence is. The association is much weaker (about a half) for James compared to Durant and Harden. Shot distance was found to have a significantly negative effect on shot accuracy for Curry, Durant, and James, but not for Harden. The presence of both shot distance and intensity in the shot accuracy model means that among locations with the same accuracy but different rewards (two- vs. three-point), three-point locations tend to have higher intensities. This reflects the bias of shooting intensity to three-point shot due to higher rewards (Alferink et al. 2009). Since shot distance was not significant in 

Harden’s model, he could make more three-point shots for higher rewards. 

Curry’s mark model only included a single covariate shot distance with a significantly negative coefficient. At shot locations with the same shot distance, Curry’s shot accuracy was not affected by his shot frequency, which makes him hard to guard against for a defense team. From an alternative direction of reasoning, Curry’s results suggest that he did not shoot more often at locations where his shot accuracy was higher, which might not be optimal from the team strategy point of view. The might be due to his injury in that season and reduced time on court. He could 

86 

J. Jiao et al.: A Bayesian marked spatial point processes model 

make more shots where his accuracy is higher to improve scoring efficiency. 

The fitted mark model allows combining shot accuracy and shot frequency to construct an expected score map for each player; see Figure 3 (lower). This plot is more informative than a shooting accuracy plot because the latter would contain no value at locations where there were few or no shots. Curry had a more obvious scoring pattern of corner threes among the four. Durant and James had more two point scores and less three point scores than Curry and Harden. Curry and Harden’s two point scores were more concentrated in the restricted area than Durant and James. 

To get an idea about the intensity dependent effect on shot accuracy averaged over top players, we analyzed all shots attempted by the top 20 most frequent shooters, which cover Harden and James, but not Curry and Durant. The 20 players’ data were pooled and treated as one virtual player. Due to computational feasibility, we could not include more players in the pool. The fitted coefficient of the intensity divided by 20 gives an “elite average” of the intensity dependent effect, which is 1.023. Compared with the results in Table 2, Harden and Durant’s fitted coefficients were above the average, while James and Curry’s were below the average (Curry’s fitted coefficient can be treated as 0 since his result favors intensity independent model). The ranking relative to the elite average could be a measure in assessing the players’ efficiency in shot location selection. Players with a fitted coefficient below the elite average might have room to improve their score efficiency through shot selection. 

### 6.4 Application to top 50 most frequent shooters 

We further applied the same analysis to each of the top 50 most frequent shooters in the 2017–2018 regular season. The number of shots of the 50 players ranged from 813 (Andre Drummond) to 1,517 (Russell Westbrook). Among them, 40 players’ data favored the intensity dependent model (ξ ≠ 0) in terms of DIC and LPML. Their estimated coefficients of the intensity in the mark model were all positive; the interactions between the intensity and the shot type (two- vs. three-point) were all not significantly different from zero. That is, 80% of the most frequent shooters in that season had positive association between shot intensity and shot accuracy, and the association did not vary with shot rewards. For the 10 players who had intensity independent mark models similar to Curry, shot 

distance was found to be significantly negative in every model. 

The estimated coefficients in the joint model can be used as features to cluster the players into groups. With Curry added in, estimates from a total of 51 players were used as inputs to a cluster analysis. Both clustering for shot patterns based on the estimated coefficients in the intensity model and clustering for the accuracy–intensity relationship based on the mark model given intensity were considered. For the shot pattern clustering, only 10 coefficients of the basis styles, with the baseline intensity excluded, were used to focus on the distribution of the pattern instead of the total count of shots. The clustering of the accuracy–intensity relationship clustering only used the coefficients of intensity and shot distance in addition to the intercept because the other coefficients were found to be insignificant for most of the players. We used the hierarchical clustering method using the minimum variance criterion of Ward (1963) as implemented in R (Murtagh and Legendre 2014). 

Figure 4a displays the results of clustering the 51 players by their shot patterns into five groups. The first group only contains three players who made mostly twopoint shots. The second group includes, interestingly, Curry, Harden, and James. The closest players to Curry, Durant, and James were, respectively, Kyrie Irving, Kyle Lowry, and Damian Lillard. Players in this group had relative small coefficients for bases 1 and 10, and large coefficients for bases 3 and 8. That is, they had less long/ mid-range twos and more threes, especially left wing threes. Players in the third group, which includes Durant, had large coefficients for bases 1 and 10, showing that they had more long/mid-range two-pointers. The closest player to Durant was Kemba Walker. Group four includes players with small coefficient for basis 6 and large coefficient for basis 9, which means that they had less two-pointers from the restricted area and more corner threes. The last group contains to players with small coefficients for bases 3 and 9, and large coefficient for basis 10, indicating less left wing threes and corner threes, but more mid-range twos. 

The clustering results of the 51 players by the characteristics of their shot accuracy in relation to their shot intensity are shown in Figure 4b. Group two has Harden and other players whose mark model contained the shot intensity but not distance. Group four, which includes Curry, contains half of the players whose shot intensity was insignificant in their mark model. Group five is the largest group, which includes Durant and James. The players in this group had significant shot distance effect on their accuracy. Most of them had intensity in the mark model with a relatively small coefficients, and five of them had 

87 

J. Jiao et al.: A Bayesian marked spatial point processes model 



Figure 4: Hierarchical clustering of 51 NBA players into five groups based on fitted coefficients in the intensity model and the mark model. 

intensity insignificant. The first group includes players with intensity but not distance in the mark model, which is similar to Group two, but the magnitude of the coefficient for the intensity was the largest among all the players, suggesting the strongest dependence between shot intensity and shot accuracy. Players here were more likely to shoot at locations with higher accuracy rates. The third group has only two players, Simmons and Drummond, whose coefficients for shot distance were much larger than others’ in magnitude, which was expected because the two players shot mostly in the restricted area. 

## 7 Discussion 

We proposed a Bayesian marked spatial point process to model both the shot locations and shot outcomes in NBA players’ shot charts. Basis shot styles constructed from the NMF method (Miller et al. 2014) were included as covariates in the intensity for the Poisson point process model and the logistic model for shot outcomes. For a majority of the top players, a positive association between 

the shot intensity and shot accuracy was reported. The association did not vary significantly according to the shot rewards. Players whose shot intensity was not found to affect their shot accuracy (e.g., Curry) may be hard to defend against. From the offense perspective, these players could score more by making more shots where they shot more frequently. The cluster analyses based on the fitted coefficients characterizing the shot pattern and shot accuracy are quite unique. Unlike other cluster analyses, (e.g., Zhang et al. 2018), the data input here are not directly observed but estimated from fitting a model to the shot charts. Consequently, less obvious insights could be discovered. 

A few directions of further work are worth investigating. Our proposed model is univariate in the sense that each player is modeled separately. A full hierarchical model for pooled data from multiple players in one season may be useful with a random effect at the player level for certain parameters. The number of basis shot styles was set to 10 as suggested by Miller et al. (2014). It would be interesting to find an optimal number of basis through model comparison criteria like DIC and LPML. An important factor for shot accuracy is the shot clock time 

88 J. Jiao et al.: A Bayesian marked spatial point processes model 

remaining (Skinner 2012), but it is not available in the dataset we obtained. It should be added to the mark model if available. Our spatial Poisson process model formulates a linear relationship between the spatial covariates and the log intensity, which cannot capture more complicated spatial trend of the intensity of spatial point pattern. Including some Bayesian non-parametric methods like finite mixture model (Miller and Harrison 2018) may help increase the accuracy of the estimation of spatial point pattern. 

Author contribution: All the authors have accepted responsibility for the entire content of this submitted manuscript and approved submission. Research funding: None declared. 

Conflict of interest statement: The authors declare no conflicts of interest regarding this article. 

## Appendix 

This section shows the tables of simulation results. 

Table : Summaries of the bias, standard deviation (SD), average of the Bayesian SD estimate (SD), and coverage rate (CR) of % credible intervals when Z is continuous: ξ = α = ., α = , (β, β) = (, ) and Z ∼ N(, ). 

|||||||λ=.||||λ=|
|---|---|---|---|---|---|---|---|---|---|---|
||||||c||||c||
|α|Model|Para|Bias|SD|SD|CR|Bias|SD|SD|CR|
|.|Intensity|λ|.|.|.|.|.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
||Mark|ξ|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
||Intensity|λ|.|.|.|.|.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
||Mark|ξ|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|−.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
||Intensity|λ|.|.|.|.|.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
||Mark|ξ|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|−.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|



Table : Summaries of the bias, standard deviation (SD), average of the Bayesian SD estimate (SD), and coverage rate (CR) of % credible intervals when Z is binary: ξ = α = ., α = , (β, β) = (, ) and Z ∼ Bernoulli(.). 

|||||||λ=.||||λ=|
|---|---|---|---|---|---|---|---|---|---|---|
|α|Model|Para|Bias|SD|c<br>SD|CR|Bias|SD|c<br>SD|CR|
|.|Intensity|λ|.|.|.|.|.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
||Mark|ξ|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
|||α|.|.|.|.|.|.|.|.|
||Intensity|λ|.|.|.|.|.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
|||β|−.|.|.|.|−.|.|.|.|
||Mark|ξ|.|.|.|.|.|.|.|.|



89 

J. Jiao et al.: A Bayesian marked spatial point processes model 

Table : (continued) 

|||||c<br>|λ=.<br>|||c<br>|λ=<br>|
|---|---|---|---|---|---|---|---|---|---|
|α<br>Model|Para|Bias|SD|SD|CR|Bias|SD|SD|CR|
||α|.|.|.|.|−.|.|.|.|
||α|.|.|.|.|.|.|.|.|
||α|.|.|.|.|.|.|.|.|
|<br>Intensity|λ|.|.|.|.|.|.|.|.|
||β|−.|.|.|.|−.|.|.|.|
||β|−.|.|.|.|−.|.|.|.|
|Mark|ξ|.|.|.|.|.|.|.|.|
||α|.|.|.|.|−.|.|.|.|
||α|.|.|.|.|.|.|.|.|
||α|.|.|.|.|.|.|.|.|



## References 

- Alferink, L. A., T. S. Critchfield, J. L. Hitt, and W. J. Higgins. 2009. “Generality of the Matching Law as a Descriptor of Shot Selection in Basketball.” Journal of Applied Behavior Analysis 42 (3): 595–608. 

- Baddeley, A., and R. Turner. 2005. “Spatstat: An R Package for Analyzing Spatial Point Patterns.” Journal of Statistical Software 12 (6): 1–42. 

- Banerjee, S., B. P. Carlin, and A. E. Gelfand. 2014. Hierarchical Modeling and Analysis for Spatial Data. Boca Raton, Florida: Chapman and Hall/CRC. 

- Baum, W. M. 1974. “On Two Types of Deviation from the Matching Law: Bias and Undermatching.” Journal of the Experimental Analysis of Behavior 22 (1): 231–42. 

- Chen, M.-H., Q.-M. Shao, and J. G. Ibrahim. 2000. Monte Carlo Methods in Bayesian Computation. Berlin/Heidelberg, Germany: Springer Science & Business Media. 

- Cressie, N. 2015. Statistics for Spatial Data. Hoboken,New Jersey: John Wiley & Sons. 

- de Valpine, P., D. Turek, C. J. Paciorek, C. Anderson-Bergman, D. T. Lang, and R. Bodik. 2017. “Programming with Models: Writing Statistical Algorithms for General Model Structures with NIMBLE.” Journal of Computational and Graphical Statistics 26 (2): 403–13. 

- Diggle, P. J. 2013. Statistical Analysis of Spatial and Spatio-Temporal Point Patterns. Boca Raton, Florida: Chapman and Hall/CRC. 

- Franks, A., A. Miller, L. Bornn, K. Goldsberry. 2015. “Characterizing the Spatial Structure of Defensive Skill in Professional Basketball.” The Annals of Applied Statistics 9 (1): 94–121. 

- Gaujoux, R., and C. Seoighe. 2010. “A Flexible R Package for Nonnegative Matrix Factorization.” BMC Bioinformatics 11 (1): 367. 

- Geisser, S., and W. F. Eddy. 1979. “A Predictive Approach to Model Selection.” Journal of the American Statistical Association 74 (365): 153–60. 

- Gelfand, A. E., and D. K. Dey. 1994. “Bayesian Model Choice: Asymptotics and Exact Calculations.” Journal of the Royal Statistical Society. Series B (Methodological) 56 (3): 501–14. 

- Geyer, C. J. 1999. “Likelihood Inference for Spatial Point Processes.” In Stochastic Geometry: Likelihood and Computation, 80, edited by O. Barndorff-Nielsen, W. Kendall, and M. van Lieshout, 79–140. Boca Raton, Florida: CRC Press. 

- Ho, L. P., and D. Stoyan. 2008. “Modelling Marked Point Patterns by Intensity-Marked Cox Processes.” Statistics & Probability Letters 78 (10): 1194–9. 

- Hu, G., F. Huffer, and M.-H. Chen. 2019. “New Development of Bayesian Variable Selection Criteria for Spatial Point Process with Applications.” e-prints 1910.06870, arXiv. 

- Kass, R. E., and A. E. Raftery. 1995. “Bayes Factors.” Journal of the American Statistical Association 90 (430): 773–95. 

- Leininger, T. J., and A. E. Gelfand. 2017. “Bayesian Inference and Model Assessment for Spatial Point Patterns Using Posterior Predictive Samples.” Bayesian Analysis 12 (1): 1–30. 

- Miller, A., L. Bornn, R. Adams, and K. Goldsberry. 2014. “Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball.” In Proceedings of the 31st International Conference on Machine Learning — Volume 32, ICML’14, 235–43. 

- Miller, J. W., and M. T. Harrison. 2018. “Mixture Models with a Prior on the Number of Components.” Journal of the American Statistical Association 113 (521): 340–56. 

- Møller, J., A. R. Syversveen, and R. P. Waagepetersen. 1998. “Log Gaussian Cox Processes.” Scandinavian Journal of Statistics 25 (3): 451–82. 

- Møller, J., and R. P. Waagepetersen. 2003. Statistical Inference and Simulation for Spatial Point Processes. Boca Raton, Florida: Chapman and Hall/CRC. 

- Mrkvička, T., F. Goreaud, and J. Chadœuf. 2011. “Spatial Prediction of the Mark of a Location-Dependent Marked Point Process: How the Use of a Parametric Model May Improve Prediction.” Kybernetika 47 (5): 696–714. 

- Murtagh, F., and P. Legendre. 2014. “Wards Hierarchical Agglomerative Clustering Method: Which Algorithms Implement Wards Criterion?” Journal of Classification 31 (3): 274–95. 

- Reich, B. J., J. S. Hodges, B. P. Carlin, and A. M. Reich. 2006. “A Spatial Analysis of Basketball Shot Chart Data.” The American Statistician 60 (1): 3–12. 

- Skinner, B. 2012. “The Problem of Shot Selection in Basketball.” PLoS One 7 (1): e30776. 

- Skinner, B., and M. Goldman. 2015. “Optimal Strategy in Basketball.” e-prints 1512.05652, arXiv. 

- Spiegelhalter, D. J., N. G. Best, B. P. Carlin, and A. Van Der Linde. 2002. “Bayesian Measures of Model Complexity and Fit.” Journal of the Royal Statistical Society: Series B (Statistical Methodology) 64 (4): 583–639. 

90 J. Jiao et al.: A Bayesian marked spatial point processes model 

- Staddon, J. 1978. “Theory of Behavioral Power Functions.” Psychological Review 85 (4): 305–20. 

- Vollmer, T. R., and J. Bourret. 2000. “An Application of the Matching Law to Evaluate the Allocation of Two- and Three-point Shots by College Basketball Players.” Journal of Applied Behavior Analysis 33 (2): 137–50. 

- Ward, J. H., Jr. 1963. “Hierarchical Grouping to Optimize an Objective Function.” Journal of the American Statistical Association 58 (301): 236–44. 

- Zhang, D., M.-H. Chen, J. G. Ibrahim, M. E. Boye, and W. Shen. 2017. “Bayesian Model Assessment in Joint Modeling of Longitudinal and Survival Data with Applications to Cancer Clinical Trials.” Journal of Computational and Graphical Statistics 26 (1): 121–33. 

- Zhang, S., A. Lorenzo, M.-A. Gómez, N. Mateus, B. Gonçalves, and J. Sampaio. 2018. “Clustering Performances in the NBA According to Players Anthropometric Attributes and Playing Experience.” Journal of Sports Sciences 36 (22): 2511–20. 


