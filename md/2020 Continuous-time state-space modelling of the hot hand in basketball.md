<!-- source: 2020 Continuous-time state-space modelling of the hot hand in basketball.pdf -->

# Continuous-time state-space modelling of the hot hand in basketball 

Sina Mews<sup>1</sup><sup>_,_∗</sup> and Marius Otting<sup>¨1</sup> 

> 1Bielefeld University, Germany 

#### **Abstract** 

We investigate the hot hand phenomenon using data on 110,513 free throws taken in the National Basketball Association (NBA). As free throws occur at unevenly spaced time points within a game, we consider a state-space model formulated in continuous time to investigate serial dependence in players’ success probabilities. In particular, the underlying state process can be interpreted as a player’s (latent) varying form and is modelled using the Ornstein-Uhlenbeck process. Our results support the existence of the hot hand, but the magnitude of the estimated effect is rather small. 

**Keywords:** free throws, hot hand, irregularly sampled data, Ornstein-Uhlenbeck process, sports analytics, state-space model 

## **1 Introduction** 

In several areas of society, it remains an open question whether a “hot hand” effect exists, according to which humans may temporarily enter a state during which they perform 

> ∗ Corresponding author; email: `sina.mews@uni-bielefeld.de` . 

1 

better than on average. While this concept may occur in different fields, such as among hedge fund managers and artists (Jagannathan et al., 2010; Liu et al., 2018), it is most — — prominent in sports. Sports commentators and fans especially in basketball often refer to players as having a “hot hand”, and being “on fire” or “in the zone” when they show a (successful) streak in performance. In the academic literature, the hot hand has gained great interest since the seminal paper by Gilovich et al. (1985), who investigated a potential hot hand effect in basketball. They found no evidence for its existence and attributed the hot hand to a cognitive illusion, much to the disapproval of many athletes and fans. Still, the results provided by Gilovich et al. (1985) have often been used as a primary example for showing that humans over-interpret patterns of success and failure in random sequences (see, e.g., Thaler and Sunstein, 2009; Kahneman, 2011). 

During the last decades, many studies have attempted to replicate or refute the results of Gilovich et al. (1985), analysing sports such as, for example, volleyball, baseball, golf, and especially basketball. Bar-Eli et al. (2006) provide an overview of 24 studies on the hot hand, 11 of which were in favour of the hot hand phenomenon. Several more recent studies, often based on large data sets, also provide evidence for the existence of the hot hand (see, e.g., Raab et al., 2012; Green and Zwiebel, 2017; Miller and Sanjurjo, 2018; Chang, 2019). Notably, Miller and Sanjurjo (2018) show that the original study from Gilovich et al. (1985) suffers from a selection bias. Using the same data as in the original study by Gilovich et al. (1985), Miller and Sanjurjo (2018) account for that bias, and their results do reveal a hot hand effect. However, there are also recent studies which provide mixed results (see, e.g., Wetzels et al., 2016) or which do not find evidence for the hot hand, such as Morgulev et al. (2020). Thus, more than 30 years after the study of Gilovich et al. (1985), the existence of the hot hand remains highly disputed. 

Moreover, the literature does not provide a universally accepted definition of the hot hand effect. While some studies regard it as serial correlation in _outcomes_ (see, e.g., Gilovich et al., 1985; Dorsey-Palmateer and Smith, 2004; Miller and Sanjurjo, 2018), others 

2 

consider it as serial correlation in _success probabilities_ (see, e.g., Albert, 1993; Wetzels et al., 2016; Otting<sup>¨</sup> et al., 2020). The latter definition translates into a latent (state) — process underlying the observed performance intuitively speaking, a measure for a — player’s form which can be elevated without the player necessarily being successful in every attempt. In our analysis, we follow this approach and hence consider state-space models (SSMs) to investigate the hot hand effect in basketball. Specifically, we analyse free throws from more than 9,000 games played in the National Basketball Association (NBA), totalling in 110,513 observations. In contrast, Gilovich et al. (1985) use data on 2,600 attempts in their controlled shooting experiment. 

Free throws in basketball, or similar events in sports with game clocks, occur at unevenly spaced time points. These varying time lengths between consecutive attempts may affect inference on the hot hand effect if the model formulation does not account for the temporal irregularity of the observations. As an illustrative example, consider an irregular sequence of throws with intervals ranging from, say, two seconds to 15 minutes. For intervals between attempts that are fairly short (such as a few seconds), a player will most likely be able to retain his form from the last shot. On the other hand, if several minutes elapse before a player takes his next shot, it becomes less likely that he is able to retain his form from the last attempt. However, we found that existing studies on the hot hand do not account for different interval lengths between attempts. In particular, studies investigating serial correlation in success probabilities usually consider discrete-time models that require the data to follow a regular sampling scheme and thus, cannot (directly) be applied to irregularly sampled data. In our contribution, we overcome this limitation by formulating our model in continuous time to explicitly account for irregular time intervals between free throws in basketball. Specifically, we consider a stochastic differential equation (SDE) as latent state process, namely the Ornstein-Uhlenbeck (OU) process, which represents the underlying form of a player fluctuating continuously around his average performance. 

3 

In the following, Section 2 presents our data set and covers some descriptive statistics. Subsequently, in Section 3, the continuous-time state-space model (SSM) formulation for the analysis of the hot hand effect is introduced, while its results are presented in Section 4. We conclude our paper with a discussion in Section 5. 

## **2 Data** 

We extracted data on all basketball games played in the NBA between October 2012 and June 2019 from `https://www.basketball-reference.com/` , covering both regular seasons and playoff games. For our analysis, we consider data only on free throw attempts as these constitute a highly standardised setting without any interaction between players, which is usually hard to account for when modelling field goals in basketball. We further included all players who took at least 2,000 free throws in the period considered, totalling in 110,513 free throws from 44 players. For each player, we included only those games in which he attempted at least four free throws to ensure that throws did not only follow successively (as players receive up to three free throws if they are fouled). A single sequence of free throw attempts consists of all throws taken by one player in a given game, totalling in 15,075 throwing sequences with a median number of 6 free throws per game (min: 4; max: 39). 

As free throws occur irregularly within a basketball game, the information on whether an attempt was successful needs to be supplemented by its time point _tk, k_ = 1 _, . . . , T_ , where 0 _≤ t_ 1 _≤ t_ 2 _≤ . . . ≤ tT_ , corresponding to the time already played (in minutes) as indicated by the game clock. For each player _p_ in his _n_ -th game, we thus consider an irregular sequence of binary variables _Yt_<sup>_p,n_</sup> 1<sup>_, Y_</sup> _t_<sup>_p,n_</sup> 2<sup>_, . . . , Y_</sup> _t_<sup>_p,n_</sup> _Tp,n_<sup>,with</sup> 



4 

In our sample, the proportion of successful free throw attempts is obtained as 0.784. However, there is considerable heterogeneity in the players’ throwing success as the corresponding empirical proportions range from 0.451 (Andre Drummond) to 0.906 (Stephen Curry). Players can receive up to three free throws (depending on the foul) in the NBA, which are then thrown in quick succession, and the proportion of successful free throws differs substantially between the three attempts, with 0.769, 0.8, and 0.883 obtained for the first, second, and third free throw, respectively. To account for the position of the throw in a player’s set of (at most) three free throws, we hence include the dummy variables _ft2_ and _ft3_ in our analysis. In our sample, 54.5% of all free throws correspond to the first, 43.7% to the second, and only 1.8% to the third attempt in a set (cf. Table 1). Furthermore, as the outcome of a free throw is likely affected by intermediate informa— — tion on the game such as a close game leading to pressure situations we consider several further covariates, which were also used in previous studies (see, e.g., Toma, 2017; Morgulev et al., 2020). Specifically, we consider the current score difference ( _scorediff_ ), a home dummy ( _home_ ), and a dummy indicating whether the free throw occurred in the last 30 seconds of the quarter ( _last30_ ). Corresponding summary statistics are shown in Table 1. 

In Table 2, example throwing sequences used in our analysis are shown for free throws taken by LeBron James in five NBA games. These throwing sequences illustrate that free throw attempts often appear in clusters of two or three attempts at the same time 

**Table 1:** Descriptive statistics of the covariates. 

||mean|st. dev.|min.|max.|
|---|---|---|---|---|
|_scoredif_|0.576|9.860|_−_45|49|
|_home_|0.514|–|0|1|
|_last30_|0.093|–|0|1|
|_ft2_|0.437|–|0|1|
|_ft3_|0.018|–|0|1|



5 

**Table 2:** Throwing sequences of LeBron James. 

|||Mia|mi Heat|@ Hou|ston R|ockets, N|ovembe|r 12, 2012|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_y_<sup>James</sup><sup>_,_1</sup><br>_tk_|0|1|0|1|1|0|1|1<br>-|-|-|-|-|
|_tk_ (in min.)|11.01|11.01|23.48|23.48|46.68|46.68|47.09|47.09<br>-|-|-|-|-|
|||Miam|i Heat @|Los A|ngeles|Clippers,|Novem|ber 14, 2012|||||
|_y_<sup>James</sup><sup>_,_2</sup><br>_tk_|0|1|0|0|1|1|1|1<br>1|-|-|-|-|
|_tk_ (in min.)|9.47|23.08|23.08|24.73|36.95|36.95|41|41<br>42.77|-|-|-|-|
|||Mil|waukee B|ucks @|Miam|i Heat, N|ovembe|r 21, 2012|||||
|_y_<sup>James</sup><sup>_,_3</sup><br>_tk_|0|1|0|1|0|1|1|0<br>-|-|-|-|-|
|_tk_ (in min.)|7.5|7.5|10.02|10.02|35.62|35.62|42.68|42.68<br>-|-|-|-|-|
|<sup>James4</sup>||Cleve<br>|land Ca<br>|valiers <br>|@ Miam<br>|i Heat, <br>|Novemb<br>|er 24, 2012<br><br>|||||
|_y_<sup>_,_</sup><br>_tk_|1|1|1|0|1|1|1|1<br>1|-|-|-|-|
|_tk_ (in min.)|11.62|21.07|21.07|21.38|21.38|31.95|31.95|32.68<br>32.68|-|-|-|-|
|<sup>J5</sup>||Los <br>|Angeles <br>|Lakers <br>|@ Mia<br>|mi Heat,<br>|Januar<br>|y 23, 2014<br><br>|||||
|_y_<sup>ames</sup><sup>_,_</sup><br>_tk_<br>|0|1|0|1|1|0|0|1<br>1|0|1|0|1|
|_tk_ (in min.)|9.28|9.28|20.53|25.97|25.97|31.57|31.57|33.43<br>33.43|42.1|42.1|47.62|47.62|



(depending on the foul), followed by a time period without any free throws. Therefore, it is important to take into account the different lengths of the time intervals between consecutive attempts as the time elapsed between attempts affects a player’s underlying form. 

## **3 Continuous-time modelling of the hot hand** 

### **3.1 State-space model specification** 

Following the idea that the throwing success depends on a player’s current (latent) form (see, e.g., Albert, 1993; Wetzels et al., 2016; Otting<sup>¨</sup> et al., 2020), we model the observed free throw attempts using a state-space model formulation as represented in Figure 1. The observation process corresponds to the binary sequence of a player’s throwing success, while the state process can be interpreted as a player’s underlying form (or “hotness”). We further include the covariates introduced in Section 2 in the model, which possibly affect a player’s throwing success. In particular, we model the binary response of throwing success _Yt_<sup>_p,n_</sup> _k_ using a Bernoulli distribution with the associated success probability _πt_<sup>_p,n_</sup> _k_ being a function of the player’s current state _St_<sup>_p,n_</sup> _k_<sup>andthecovariates.Droppingthesuperscripts</sup><sup>_p_</sup> 

6 

and _n_ for notational simplicity from now on, we thus have 



where _β_ 0 _,p_ is a player-specific intercept to account for differences between players’ average throwing success. To address the temporal irregularity of the free throw attempts, we formulate the stochastic process _{St}t≥_ 0 in continuous time. Furthermore, we require the state process to be continuous-valued to allow for gradual changes in a player’s form, rather than assuming a finite number of discrete states (e.g. three states interpreted as cold vs. normal vs. hot; cf. Wetzels et al., 2016; Green and Zwiebel, 2017). In addition, the state process ought to be stationary such that in the long-run a player returns to his average form. A natural candidate for a corresponding stationary, continuous-valued and continuous-time process is the OU process, which is described by the following SDE: 



where _θ >_ 0 is the drift term indicating the strength of reversion to the long-term mean _µ ∈_ R, while _σ >_ 0 is the diffusion parameter controlling the strength of fluctuations, and _Bt_ denotes the Brownian motion. We further specify _µ_ = 0 such that the state process fluctuates around a player’s average form, given the current covariate values. Specifically, positive values of the state process indicate higher success probabilities, whereas negative values indicate decreased throwing success given the player’s average ability and the current game characteristics. 

As shown in Figure 1, we model the hot hand effect as serial correlation in success probabilities as induced by the state process: while the observed free throw attempts are conditionally independent, given the underlying states, the unobserved state process induces correlation in the observation process. Regarding the hot hand effect, the drift 

7 



<!-- Start of picture text -->
Yt 1 Yt 2 Yt 3 throwing success (observed)<br>St 1 St 2 St 3 ... player’s form (hidden)<br><!-- End of picture text -->

**Figure 1:** Dependence structure of our SSM: the throwing success _Ytk_ is assumed to be driven by the underlying (latent) form of a player. To explicitly account for the irregular time intervals between observations, we formulate our model in continuous time. 

parameter _θ_ of the OU process is thus of main interest as it governs the speed of reversion (to the average form). The smaller _θ_ , the longer it takes for the OU process to return to its mean and hence the higher the serial correlation. To assess whether a model including serial dependence (i.e. an SSM) is actually needed to describe the structure in the data, we additionally fit a benchmark model without the underlying state variable _Stk_ in Equation (1). Consequently, the benchmark model corresponds to the absence of any hot hand effect, i.e. a standard logistic regression model. 

### **3.2 Statistical inference** 

The likelihood of the continuous-time SSM given by Equations (1) and (2) involves integration over all possible realisations of the continuous-valued state _Stk_ , at each observation time _t_ 1 _, t_ 2 _, . . . , tT_ . For simplicity of notation, let the integer _τ_ = 1 _,_ 2 _, . . . , T_ denote the _number_ of the observation in the time series, such that _Ytτ_ shortens to _Yτ_ and _Stτ_ shortens to _Sτ_ . Further, _tτ_ represents the _time_ at which the observation _τ_ was collected. Then the 

8 

likelihood of a single throwing sequence _y_ 1 _, . . . , yT_ is given by 



where we assume that each player starts a game in his stationary distribution _S_ 1 _∼ N_ 0 _,_<sup>_<u>σ</u>_</sup> 2 _θ_<sup>2</sup> , i.e. the stationary distribution of the OU process. Further, we assume _Yτ_ to be � � Bernoulli distributed with corresponding state-dependent probabilities Pr( _yτ |sτ_ ) additionally depending on the current covariate values (cf. Equation (1)), while the probabilities of transitioning between the states Pr( _sτ |sτ −_ 1) are normally distributed as determined by the conditional distribution of the OU process: 



where ∆ _τ_ = _tτ − tτ −_ 1 denotes the time difference between consecutive observations. 

Due to the _T_ integrals in Equation (3), the likelihood calculation is intractable. To render its evaluation feasible, we approximate the multiple integral by finely discretising the continuous-valued state space as first suggested by Kitagawa (1987). The discretisation of the state space can effectively be seen as a reframing of the model as a continuoustime hidden Markov model (HMM) with a large but finite number of states, enabling us to apply the corresponding efficient machinery. In particular, we use the forward algorithm to calculate the likelihood, defining the possible range of state values as [ _−_ 2 _,_ 2], which we divide into 100 intervals. For details on the approximation of the likelihood via state discretisation, see Otting<sup>¨</sup> et al. (2020) for discrete-time and Mews et al. (2020) for continuous-time SSMs. 

9 

Assuming single throwing sequences of players to be mutually independent, conditional on the model parameters, the likelihood over all games and players is simply calculated as the product of the individual likelihoods. The model parameters, i.e. the drift parameter and the diffusion coefficient of the OU process as well as the regression coefficients, are then estimated by numerically maximising the (approximate) joint likelihood. The resulting parameter estimators are unbiased and consistent — corresponding simulation experiments are shown in Mews et al. (2020). 

## **4 Results** 

According to the information criteria AIC and BIC, the continuous-time model formulation including a potential hot hand effect is clearly favoured over the benchmark model without any underlying state process (∆AIC = 61.20, ∆BIC = 41.97). The parameter estimates of the OU process, which represents the underlying form of a player, as well as the estimated regression coefficients are shown in Table 3. In particular, the estimate for the drift parameter _θ_ of the OU process is fairly small, thus indicating serial correlation in the state process over time. However, when assessing the magnitude of the hot hand effect, we also observe a fairly small estimate for the diffusion coefficient _σ_ . The corresponding stationary distribution is thus estimated as _N_ (0 _,_ 0 _._ 348<sup>2</sup> ), indicating a rather small range 

**Table 3:** Parameter estimates with 95% confidence intervals. 

|par|ameter|estimate|95% CI|
|---|---|---|---|
|_θ_|(drift)|0.042|[0.016; 0.109]|
|_σ_|(difusion)|0.101|[0.055; 0.185]|
|_β_1|(_home_)|0.023|[-0.009; 0.055]|
|_β_2|(_scoredif_)|0.030|[0.011; 0.048]|
|_β_3|(_last30_)|0.003|[-0.051; 0.058]|
|_β_4|(_ft2_)|0.223|[0.192; 0.254]|
|_β_5|(_ft3_)|0.421|[0.279; 0.563]|



10 



<!-- Start of picture text -->
0.8<br>0.90<br>0.4<br>0.85<br>0.0<br>0.80<br>−0.4 0.75<br>0.70<br>0 10 20 30 40 50<br>time<br>state<br>success prob.<br><!-- End of picture text -->

**Figure 2:** Simulation of possible state trajectories for the length of an NBA game based on the estimated parameters of the OU process. The red dashed line indicates the intercept (here: the median throwing success over all players), around which the processes fluctuate. The right y-axis shows the success probabilities resulting from the current state (left y-axis), given that the explanatory variables equal 0. The graphs were obtained by application of the Euler-Maruyama scheme with initial value 0 and step length 0.01. 

of the state process, which becomes apparent also when simulating state trajectories based on the parameter estimates of the OU process (cf. Figure 2). Still, the associated success probabilities, given that all covariate values are fixed to zero, vary considerably during the time of an NBA game (cf. right y-axis of Figure 2). While the state process and hence the resulting success probabilities slowly fluctuate around the average throwing success (given the covariates), the simulated state trajectories reflect the temporal persistence of the players’ underlying form. Thus, our results suggest that players can temporarily enter a state in which their success probability is considerably higher than their average performance, which provides evidence for a hot hand effect. 

Regarding the estimated regression coefficients, the player-specific intercepts _β_<sup>ˆ</sup> 0 _,p_ range from -0.311 to 2.192 (on the logit scale), reflecting the heterogeneity in players’ throwing success. The estimates for _β_ 1 to _β_ 5 are displayed in Table 3 together with their 95% 

11 

confidence intervals. The chance of making a free throw is slightly increased if the game is played at home ( _β_ 1) or if a free throw occurs in the last 30 seconds of a quarter ( _β_ 3), but both corresponding confidence intervals include the zero. In contrast, the confidence interval for the score difference ( _β_ 2) does not include the zero and its effect is positive but small, indicating that the higher the lead, the higher is, on average, the chance to make a free throw. The position of the throw, i.e. whether it is the first, second ( _β_ 4), or third ( _β_ 5) attempt in a row, has the largest effect of all covariates considered: compared to the first free throw, the chance of a hit is considerably increased if it is the second or, in particular, the third attempt, which was already indicated by the descriptive analysis presented in Section 2. However, this strong effect on the success probabilities is probably caused by the fact that three free throws in a row are only awarded if a player is fouled while shooting a three-point field goal, which, in turn, is more often attempted by players who regularly perform well at free throws. 

To further investigate how the hot hand may evolve during a game, we compute the most likely state sequences, corresponding to the underlying form of a player. Specifically, we seek 



where _s_<sup>_∗_</sup> 1<sup>_, . . . , s∗_</sup> _T_<sup>denotesthemostlikelystatesequencegiventheobservations.Aswe</sup> transferred our continuous-time SSM to an HMM framework by finely discretising the state space (cf. Section 3.2), we can use the Viterbi algorithm to calculate such sequences at low computational cost (Zucchini et al., 2016). Figure 3 shows the most likely states underlying the throwing sequences presented in Table 2. While the decoded state processes fluctuate around zero (i.e. a player’s average throwing success), the state values vary slightly over the time of an NBA game. Over all players, the decoded states range from -0.42 to 0.46, again indicating that the hot hand effect as modelled by the state process is rather small. 

The decoded state sequences in Figure 3 further allow to illustrate the advantages and the main idea of our continuous-time modelling approach. For example, consider the 

12 



<!-- Start of picture text -->
0.1<br>0.0<br>−0.1<br>−0.2<br>0.1<br>0.0<br>−0.1<br>−0.2<br>0.1<br>0.0<br>−0.1<br>−0.2<br>0.1<br>0.0<br>−0.1<br>−0.2<br>0.1<br>0.0<br>−0.1<br>−0.2<br>10 20 30 40<br>time<br>match  1<br>match  2<br>state match  3<br>match  4<br>match  5<br><!-- End of picture text -->

**Figure 3:** Decoded states underlying the throwing sequences of LeBron James shown in Table 2. Successful free throws are shown in yellow, missed shots in black. 

throwing sequence in the second match shown, where LeBron James only made a single free throw of his first four attempts. The decoded state at throw number 3 is -0.092 (cf. Figure 3) and the time passed between throw number 3 and 4 is 1.65 minutes (cf. Table 2). Thus, the value of the state process at throw number 4 is drawn from a normal distribution, given the decoded state of the previous attempt, with mean e<sup>_−_0</sup><sup>_._042</sup><sup>_·_1</sup><sup>_._65</sup> ( _−_ 0 _._ 092) = _−_ 0 _._ 086 <u>0</u> _<u>.</u>_ <u>101</u><sup>2</sup> and variance 2 _·_ 0 _._ 042<sup>(1</sup><sup>_−_e</sup><sup>_−_2</sup><sup>_·_0</sup><sup>_._042</sup><sup>_·_1</sup><sup>_._65)=0</sup><sup>_._016(cf.Equation(4)).Accordingly,thevalue</sup> of the state process for throw number 5 is drawn from a normal distribution with mean _−_ 0 _._ 050 and variance 0 _._ 078, conditional on the decoded state of -0.084 at throw number 4 and a relatively long time interval of 12.22 minutes. As highlighted by these example calculations, the conditional distribution of the state process takes into account the interval length between consecutive attempts: the more time elapses, the higher the variance in 

13 

the state process and hence, the less likely is a player to retain his form, with a tendency to return to his average performance. 

## **5 Discussion** 

In our analysis of the hot hand, we used SSMs formulated in continuous time to model throwing success in basketball. Focusing on free throws taken in the NBA, our results provide evidence for a hot hand effect as the underlying state process exhibits some persistence over time. In particular, the model including a hot hand effect is preferred over the benchmark model without any underlying state process by information criteria. Although we provide evidence for the existence of a hot hand, the magnitude of the hot hand effect is rather small as the underlying success probabilities are only elevated by a few percentage points (cf. Figures 2 and 3). 

A minor drawback of the analysis arises from the fact that there is no universally accepted definition of the hot hand. In our setting, we use the OU process to model players’ continuously varying form and it is thus not clear which values of the drift parameter _θ_ correspond to the existence of the hot hand. While lower values of _θ_ refer to a slower reversion of a player’s form to his average performance, a further quantification of the magnitude of the hot hand effect is not possible. In particular, a comparison of our results to other studies on the hot hand effect proves difficult as these studies apply different methods to investigate the hot hand. 

In general, the modelling framework considered provides great flexibility with regard to distributional assumptions. In particular, the response variable is not restricted to be Bernoulli distributed (or Gaussian, as is often the case when making inference on continuous-time SSMs), such that other types of response variables used in hot hand analyses (e.g. Poisson) can be implemented by changing just a few lines of code. Our continuous-time SSM can thus easily be applied to other sports, and the measure for 

14 

success does not have to be binary as considered here. For readers interested in adopting our code to fit their own hot hand model, the authors can provide the data and code used for the analysis. 

## **Acknowledgements** 

We thank Roland Langrock, Christian Deutscher, and Houda Yaqine for stimulating discussions and helpful comments. 

15 

## **References** 

- Albert, J. (1993). A statistical analysis of hitting streaks in baseball: Comment. _Journal of the American Statistical Association_ , 88(424):1184–1188. 

- Bar-Eli, M., Avugos, S., and Raab, M. (2006). Twenty years of “hot hand” research: review and critique. _Psychology of Sport and Exercise_ , 7(6):525–553. 

- Chang, J. C. (2019). Predictive Bayesian selection of multistep Markov chains, applied to the detection of the hot hand and other statistical dependencies in free throws. _Royal Society Open Science_ , 6(3):182174. 

- Dorsey-Palmateer, R. and Smith, G. (2004). Bowlers’ hot hands. _The American Statistician_ , 58(1):38–45. 

- Gilovich, T., Vallone, R., and Tversky, A. (1985). The hot hand in basketball: on the misperception of random sequences. _Cognitive Psychology_ , 17(3):295–314. 

- Green, B. and Zwiebel, J. (2017). The hot-hand fallacy: cognitive mistakes or equilibrium adjustments? Evidence from Major League Baseball. _Management Science_ , 64(11):4967–5460. 

- Jagannathan, R., Malakhov, A., and Novikov, D. (2010). Do hot hands exist among hedge fund managers? An empirical evaluation. _The Journal of Finance_ , 65(1):217–255. 

- Kahneman, D. (2011). _Thinking, Fast and Slow_ . New York: Farrar, Straus and Giroux. 

- Kitagawa, G. (1987). Non-gaussian state-space modeling of nonstationary time series. _Journal of the American Statistical Association_ , 82(400):1032–1041. 

- Liu, L., Wang, Y., Sinatra, R., Giles, C. L., Song, C., and Wang, D. (2018). Hot streaks in artistic, cultural, and scientific careers. _Nature_ , 559(7714):396–399. 

16 

- Mews, S., Langrock, R., Otting,<sup>¨</sup> M., Yaqine, H., and Reinecke, J. (2020). Maximum approximate likelihood estimation of general continuous-time state-space models. _arXiv preprint arXiv:2010.14883_ . 

- Miller, J. B. and Sanjurjo, A. (2018). Surprised by the hot hand fallacy? A truth in the law of small numbers. _Econometrica_ , 86(6):2019–2047. 

- Morgulev, E., Azar, O. H., and Bar-Eli, M. (2020). Searching for momentum in NBA triplets of free throws. _Journal of Sports Sciences_ , 38(4):390–398. 

- ¨Otting, M., Langrock, R., Deutscher, C., and Leos-Barajas, V. (2020). The hot hand in professional darts. _Journal of the Royal Statistical Society (Series A)_ , 183(2):565–580. 

- Raab, M., Gula, B., and Gigerenzer, G. (2012). The hot hand exists in volleyball and is used for allocation decisions. _Journal of Experimental Psychology: Applied_ , 18(1):81–94. 

- Thaler, R. H. and Sunstein, C. R. (2009). _Nudge: Improving Decisions about Health, Wealth, and Happiness_ . London: Penguin. 

- Toma, M. (2017). Missed shots at the free-throw line: analyzing the determinants of choking under pressure. _Journal of Sports Economics_ , 18(6):539–559. 

- Wetzels, R., Tutschkow, D., Dolan, C., van der Sluis, S., Dutilh, G., and Wagenmakers, E.-J. (2016). A Bayesian test for the hot hand phenomenon. _Journal of Mathematical Psychology_ , 72:200–209. 

- Zucchini, W., MacDonald, I. L., and Langrock, R. (2016). _Hidden Markov Models for Time Series: An Introduction Using R_ . Boca Raton: Chapman & Hall/CRC. 

17 


