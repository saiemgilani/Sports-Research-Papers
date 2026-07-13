<!-- source: Predicting play calls in the National Football League using hidden Markov models.pdf -->

# Predicting play calls in the National Football League using hidden Markov models 

### Marius Otting<sup>¨</sup><sup>_∗_</sup> 

#### **Abstract** 

In recent years, data-driven approaches have become a popular tool in a variety of sports to gain an advantage by, e.g., analysing potential strategies of opponents. Whereas the availability of play-by-play or player tracking data in sports such as basketball and baseball has led to an increase of sports analytics studies, equivalent datasets for the National Football League (NFL) were not freely available for a long time. In this contribution, we consider a comprehensive play-by-play NFL dataset provided by `www.kaggle.com` , comprising 289,191 observations in total, to predict play calls in the NFL using hidden Markov models. The resulting out-of-sample prediction accuracy for the 2018 NFL season is 71.5%, which is substantially higher compared to similar studies on play call predictions in the NFL. 

## **1 Introduction** 

Unpredictability of play calls is widely accepted to be a key ingredient to success in the NFL. For example, according to several players of the 2017 Dallas Cowboys, being too predictable regarding their play calling may have been one reason for their elimination from the playoff contention of the 2017 NFL season. Being unpredictable hence is desirable, and, vice versa, it is clearly also of interest to be able to accurately predict the opponent’s next play call. In earlier studies, play call predictions were carried out 

> _∗_ Bielefeld University, Germany 

1 

by simple arithmetics, such as calculating the relative frequencies of runs and passes of previous matches (Heiny and Blevins, 2011). Driven by the availability of play-by-play NFL data, several studies considered statistical models for play call predictions. These studies can be divided in those where play-by-play data only is considered (see, Heiny and Blevins, 2011; Teich et al., 2016) and those who consider additional data on the players on the field, such as the number of offensive players for a certain position and player ratings (see Lee et al., 2017; Joash Fernandes et al., 2019). The former report prediction accuracy of about 0.67, whereas the latter provide prediction accuracy of about 0.75. 

However, most of these studies use basic statistical models, e.g. linear discriminant analysis, logistic regression, or decision trees, which do not account for the time series structure of the data at hand. This contribution considers HMMs for modelling and forecasting NFL play calls. In the recent past, HMMs have been applied in different areas of research for forecasting, including stock markets (see, e.g., De Angelis and Paas, 2013; Dias et al., 2015), environmental science (see, e.g., Chambers et al., 2012; Tseng et al., 2020) and political conflicts (Schrodt, 2006). Within HMMs, the observations are assumed to be driven by an underlying state variable. In the context of play calling, the underlying states serve as a proxy for the team’s current propensity to make a pass (as opposed to a run). The state sequence is modelled as a Markov chain, thereby inducing correlation in the observations and hence accounting for the time series structure of the data. HMMs are fitted to data from seasons 2009 to 2017 to predict the play calls for season 2018. In practice, these predictions are helpful for defense coordinators to make adjustments in real time on the field. Offense coordinators may also benefit from these models, since they allow them to check the predictability of their own play calls. 

This paper is organised as follows: Section 2 describes the the play-by-play data and provides exploratory data analysis. Section 3 explains HMMs in furhther detail, and section 4 presents the results. 

## **2 Data** 

The data for predicting play calls in the NFL were taken from `www.kaggle.com` , covering (almost) all plays of regular season matches between 2009 to 2018. In total, _m_ = 2 _,_ 526 

2 

matches are considered<sup>1</sup> , each of which is split up into two time series (one for each team’s offense), totalling in 5,052 time series containing 318,691 plays. The observed time series _{ym,p}p_ =1 _,...,Pm_ indicates whether a run or a pass play has been called in the _p_ -th play in match _m_ , with 



and _Pm_ denoting the total number of plays in match _m_ . For all matches considered, other plays such as field goals and kickoffs, which occur typically at the beginning or the end of drives, are ignored here. Since the main goal is to predict play calls, we divide the data into a training and a test data set. The data set for training the models covers all matches from seasons 2009 – 2017, comprising 2,302 matches and 289,191 plays. The test data covers 224 matches, totalling in 29,500 plays. For the full data set, about 58.4% of play calls were passes. 

Since the play of the offense is likely affected by intermediate information on the match (such as the current score), several covariates are considered, which have also been considered by previous studies on predicting play calls summarised above: a dummy indicating whether the match is played at home ( _home_ ), the yards to go for a first down ( _ydstogo_ ), the current down number ( _down1_ , _down2_ , _down3_ , and _down4_ ), a dummy indicating whether the formation is shotgun ( _shotgun_ ), a dummy indicating whether the play is a no-huddle play ( _no-huddle_ ), the difference in the intermediate score (own score minus the opponent’s score) ( _scorediff_ ), a dummy indicating whether the current play is a goal-to-go play ( _goaltogo_ ), and a dummy indicating whether the team is starting within 10 yards of their own end zone ( _yardline90_ ). Table 1 summarises the covariates and displays corresponding descriptive statistics (for the full data set). 

To investigate how the play calling varies with different downs and the shotgun formation, Figure 1 shows the empirical proportions for a pass found in the data, separated for the different downs and the shotgun formation. As indicated by the figure, a pass becomes more likely with increasing number of downs, and there is a substantial increase in passes observed if the team is in shotgun formation. However, 

> 1The data comprises 2,526 regular-season matches out of 2,560 matches which have taken place in the time period considered. 

3 

Table 1: Descriptive statistics of the covariates. 

||mean|st. dev.|min.|max.|
|---|---|---|---|---|
|_pass_ (response)|0.584|0.493|0|1|
|_home_|0.503|0.500|0|1|
|_ydstogo_|8.634|3.931|1|50|
|_down1_|0.443|0.497|0|1|
|_down2_|0.333|0.471|0|1|
|_down3_|0.209|0.407|0|1|
|_down4_|0.015|0.121|0|1|
|_shotgun_|0.525|0.499|0|1|
|_no-huddle_|0.087|0.282|0|1|
|_scoredif_|_−_1.458|10.84|_−_59|59|
|_goaltogo_|0.057|0.232|0|1|
|_yardline90_|0.033|0.178|0|1|



whether a run or a pass is called is also likely to depend on the yards to go for a first down, which is shown in Figure 2, indicating that a pass becomes more likely the more yards are needed for a first down. The colours in Figure 2 indicate the (categorised) score difference, suggesting that a pass becomes more likely if teams are trailing. 

In addition to the covariates potentially affecting the decision to call a pass or a run, one example time series from the data set, corresponding to the play calls observed for the New Orleans Saints in the match against the New York Giants played in November 2015 is shown in Figure 3. With 101 points scored in total, this match is one of the highest scoring NFL games. The plays shown in the figure underline that there are periods with a fairly high number of passing plays (e.g. around play 20), and those where more runs are called (e.g. around play 30). 

## **3 Modelling and forecasting play-calls** 

To account for the periods of passes and runs as indicated by Figure 3, HMMs are considered for modelling and forecasting play calls. The underlying states can be interpreted as the propensity to make a pass (as opposed to a run) of the team considered. A HMM involves two components, namely an observed state-dependent process and an unobserved Markov chain with _N_ states, assuming that the observations are generated by one of _N_ pre-specified state-dependent distributions. The dependence structure of the HMM considered is shown in Figure 4. Here, the observed time series are the 

4 



<!-- Start of picture text -->
0.75<br>0.50 Shotgun formation<br>no<br>yes<br>0.25<br>0.00<br>1 2 3 4<br>down<br>pass proportion<br><!-- End of picture text -->

Figure 1: Empirical proportions for a pass found in the data for different downs and the shotgun formation. 

Table 2: Descriptive statistics of the covariates considered. 

||mean|std. dev.|min|max|
|---|---|---|---|---|
|_pass_ (response)|0.584|0.493|0|1|
|_home_|0.503|0.500|0|1|
|_ydstogo_|8.634|3.931|1|50|
|_down1_|0.443|0.497|0|1|
|_down2_|0.333|0.471|0|1|
|_down3_|0.209|0.407|0|1|
|_down4_|0.015|0.121|0|1|
|_shotgun_|0.525|0.499|0|1|
|_no-huddle_|0.087|0.282|0|1|
|_scoredif_|_−_1.458|10.84|_−_59|59|
|_goaltogo_|0.057|0.232|0|1|
|_yardline90_|0.033|0.178|0|1|



5 



<!-- Start of picture text -->
G<br>G G G G G G G G G G G G<br>G<br>G<br>0.8 G G G G G G G G G G G G G<br>G G G G<br>G G G G G G G G G G G GG G<br>G G G G<br>G G G G G G G<br>G G G G G<br>G G<br>G G G G G G G G G G G Categorized<br>G G G G  score difference<br>0.6 G G G G<br>G G G < −7<br>G G G G ≥ −7 & ≤ 0<br>G G G<br>G G > 0 & ≤ 7<br>G > 7<br>G G<br>G<br>0.4 G<br>G<br>G<br>G<br>G<br>0.2<br>0 5 10 15 20 25<br>yards to go<br>pass proportion<br><!-- End of picture text -->

Figure 2: Empirical proportions for a pass found in the data for the different yards to go for a first down. Colours indicate the (categorised) score difference. The proportion for a pass for 10 yards to go is relatively low, since most of these observations correspond to a first down, where a run is more likely. Observations with more than 25 yards to go are excluded (the number of observations for each of these categories is less than 100). 

6 



<!-- Start of picture text -->
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG<br>1 10 20 30 40 50 60 70<br>G pass G run<br><!-- End of picture text -->

Figure 3: Example time series found in the data: the play calls of the New Orleans Saints observed for the match against the New York Giants played on November 1, 2015. 

play calls _{ym,p}p_ =1 _,...,Pm_ , which are denoted from now on by _yp_ for notational simplicity. The unobserved state process, modelled by a _N_ -state Markov chain, is denoted by _{sp}p_ =1 _,...,Pm_ . For the state transitions, a transition probability matrix (t.p.m.) **Γ** = ( _γij_ ) is defined, with _γij_ = Pr( _sp_ = _j|sp−_ 1 = _i_ ), i.e. the probability of switching from state _i_ at play _p −_ 1 to state _j_ in play _p_ . For the model formulation of an HMM to be completed, the number of states _N_ and the class of the state-dependent distribution have to be selected. Since the play calls are binary, the Bernoulli distribution is chosen here. The corresponding probabilities of the observation given state _i_ , i.e. _f_ ( _yp | sp_ = _i_ ) are comprised in the _i−_ th diagonal element of the _N × N_ diagonal matrix **P** ( _yp_ ). Since assuming a team to start in its stationary distribution at the beginning of an American football match is fairly unrealistic, we estimate the initial distribution **_δ_** = � Pr( _sp_ = 1) _, . . . ,_ Pr( _sp_ = _N_ )�. 

To include the covariates introduced above which may lead to state-switching, we allow the transition probabilities _γij_ to depend on covariates at play _p_ . This is done by linking _γij_<sup>(</sup><sup>_p_)</sup> to covariates (denoted by _x_<sup>(</sup> 1<sup>_p_)</sup><sup>_, . . . , x_(</sup> _k_<sup>_p_))usingthemultinomiallogitlink:</sup> 



with 

7 



Since the transition probabilities depend on covariates, the t.p.m. as introduced above is not constant across time, and hence denoted by **Γ**<sup>(</sup><sup>_p_)</sup> . To formulate the likelihood, we apply the forward algorithm, which allows to calculate the likelihood recursively at low computational cost (Zucchini et al., 2016). The likelihood for a single match _m_ is then given by: 



with column vector **1** = (1 _, . . . ,_ 1)<sup>_′_</sup> _∈_ R<sup>_N_</sup> (Zucchini et al., 2016). To obtain the likelihood for the full data set, we assume independence between the individual matches such that the likelihood is given by the product of likelihoods for the individual matches: 



where _M_ denotes the total number of matches. The model parameters are estimated by numerically maximising the likelihood using `nlm()` in R (R Core Team, 2018). Subsequently, we predict play calls for the test data using the fitted models. Specifically, to forecast play calls, the forecast distribution is considered, which is for a single match given as a ratio of likelihoods (dropping the subscript _m_ for notational simplicity): 



where **Γ**<sup>(</sup><sup>_y_)</sup> and **y**<sup>(</sup><sup>_P_)</sup> denote the t.p.m. as implied by the new covariates and the vector of all preceding observations of the match considered, respectively (Zucchini et al., 2016). The play which is most likely under the forecast distribution is then taken as the one-step-ahead forecast. To address heterogeneity between teams, the models are fitted to data of each team individually instead of pooling the data of all teams. The corresponding results are presented in the next section. 

8 



<!-- Start of picture text -->
yp− 1 yp yp +1<br>... sp− 1 sp sp +1 ...<br><!-- End of picture text -->

Figure 4: Dependence structure of the HMM considered. Each observation _yp_ is assumed to be generated by one of _N_ distributions according to the state process _sp_ , which serves for the team’s current propensity to make a pass (as opposed to a run). 

## **4 Results** 

Before presenting the results on the prediction of play calls, the number of states _N_ and the covariates have to be selected. As the number of parameters (due to the inclusion of covariates) increases considerably fast compared to the number of observations per team, we select _N_ = 2 states here to avoid numerical instability. We apply a forward selection of the covariates described in Section 2 based on the AIC. In addition, we also include several interactions between the covariates, such as an interaction between _ydstogo_ and _scorediff_ , which was already indicated by in Figure 2. Based on further explanatory data analysis, the following additional interaction terms are considered: interactions between the different downs and _ydstogo_ , between _shotgun_ and _ydstogo_ , between _nohudlle_ and _scorediff_ , and between _nohuddle_ and _shotgun_ . The AIC-based forward covariate selection is then applied for each team individually, with the covariates selected being slightly different between the teams. 

The play call forecasts are evaluated by the prediction accuracy (i.e. the proportion of correct predictions), the precision (i.e. the proportion of predicted runs/passes that were actually correct) and the recall (i.e. the proportion of actual runs/passes that were identified correctly). The weighted average of the prediction accuracy over all teams is obtained as 0.715. This is a substantial improvement compared to existing studies that were also based on play-by-play data only (i.e. without including information on the players on the field). Moreover, the prediction accuracy obtained here is only slightly lower than the ones reported by Lee et al. (2017) and Joash Fernandes et al. (2019) 

9 

(which are about 75%), notably _without_ taking into account information about the players on the field. 

The prediction accuracy for the individual teams is shown in Figure 5, indicating that the lowest and highest prediction accuracy are obtained for the Seattle Seahaws (0.602) and the New England Patriots (0.779), respectively. In addition, the precision rates for a run range from 0.532 (Green Bay Packers) to 0.763 (Houston Texans), which can be interpreted as follows: when our model predicts a run for the Houston Texans (Green Bay Packers), it is correct in about 76.3% (53.2%) of all predicted runs. The recall rates for a run range from 0.324 (Baltimore Ravens) to 0.886 (Los Angeles Rams) — in other words, our model correctly predicts 88.6% of all runs for the Los Angeles Rams. For passing plays, precision and recall range from 0.559 (Seattle Seahawks) to 0.9 (Los Angeles Rams), and from 0.664 (Los Angeles Rams) to 0.922 (Pittsburgh Steelers), respectively. These summary statistics on the predicted play calls reveal that there are substantial differences in the predictive power with regard to the individual teams. Section 5 discusses practical implications following from these summary statistics. It took us on avarage 7 hours to conduct the AIC-based forward selection for the covariates on a standard desktop computer. However, using the fitted models to predict play calls takes less than a second for a single match, thus rendering the approach considered suitable for application in practice. 

## **5 Discussion** 

The use of HMMs to predict play calls in the NFL indicates that the accuracy of the – – predictions is increased compared to similar previous studies by accounting for the time series structure of the data. We split the data into a training set (seasons 2009–2017) and a test set (season 2018), and fitted HMMs to the (training) data of all teams individually, which yields 71.5% correctly predicted out-of-sample play calls. The prediction accuracy for the individual teams range from 60.2% to 77.9%, with the highest prediction accuracy obtained for the New England Patriots (see Figure 5). 

Practitioners have to take into account the variation in the prediction accuracy across teams and plays. For example, if a pass is predicted for the Los Angeles Rams, it is fairly likely that the actual play will indeed be a pass (according to our model), since 

10 



<!-- Start of picture text -->
0.8 981 963 905<br>964 941 958 881 863 896 944 843 873<br>933 977 959 953 905 916 961 876 942 888 890 950 941<br>894 933 922 926 825<br>982<br>915<br>0.6<br>0.4<br>0.2<br>0.0<br>team<br>prediction accuracy<br>NE PIT NYG RAMS DET DAL MIN DEN NYJ NO ARI CHAR CLE TB IND ATL WAS OAK JAX CIN SF HOU TEN BUF PHI CAR GB KC CHI MIA BAL SEA<br><!-- End of picture text -->

Figure 5: Prediction accuracy for the individual teams. The number of out-of-sample observations (i.e. of predicted plays) is shown at the top of the bars. 

the corresponding precision is obtained as 90%. On the other hand, if a pass is predicted for the Seattle Seahawks, this forecast has to be treated with caution, as the precision is obtained as 55.9%. Additional aspects for practitioners are the costs of an incorrect decision. For example, if teams want to avoid that a pass is anticipated although the actual play of the opponent’s offense is a run, then coaches should carefully consider the corresponding precision rates. Since the models presented here provide probabilistic forecasts and not only binary classifications, coaches could consult the forecasts only if the predicted probability exceeds a chosen threshold. In any case, practitioners should not regard these models as a tool which delivers defense adjustments for each play automatically, but rather as an additional help to make better defense and offense plays, respectively. 

Further research could focus on including additional covariates to improve the pre- 

11 

dictive power, such as the personnel of the team, i.e. the information on how many running backs/fullbacks, tight ends and wide receiver are on the field. In addition, the current strength of the team is not captured yet. This could be quantified by, for instance, the player ratings provided by the video game Madden, which was also done by Lee et al. (2017) and Joash Fernandes et al. (2019). However, it is at least questionable whether information on players can indeed be used on the field in practice, since players are substituted fairly frequently during a match. Finally, updating the model throughout the 2018 season dynamically, rather than using the model fitted up to season 2018 in the out-of-sample prediction would further improve the predictive power. 

12 

## **References** 

- Chambers, D. W., Baglivo, J. A., Ebel, J. E., and Kafka, A. L. (2012). Earthquake forecasting using hidden Markov models. _Pure and applied geophysics_ , 169(4):625– 639. 

- De Angelis, L. and Paas, L. J. (2013). A dynamic analysis of stock markets using a hidden Markov model. _Journal of Applied Statistics_ , 40(8):1682–1700. 

- Dias, J. G., Vermunt, J. K., and Ramos, S. (2015). Clustering financial time series: New insights from an extended hidden Markov model. _European Journal of Operational Research_ , 243(3):852–864. 

- Heiny, E. L. and Blevins, D. (2011). Predicting the Atlanta Falcons play-calling using discriminant analysis. _Journal of Quantitative Analysis in Sports_ , 7(3). 

- Joash Fernandes, C., Yakubov, R., Li, Y., Prasad, A. K., and Chan, T. C. (2019). Predicting plays in the National Football League. _Journal of Sports Analytics_ , Prepress(Pre-press):1–9. 

- Lee, P., Chen, R., and Lakshman, V. (2017). Predicting offensive play types in the National Football League. https://tinyurl.com/ya3q4w6q. 

- R Core Team (2018). _R: A Language and Environment for Statistical Computing_ . R Foundation for Statistical Computing, Vienna, Austria. 

- Schrodt, P. A. (2006). Forecasting conflict in the balkans using hidden Markov models. In _Programming for Peace_ , pages 161–184. Springer. 

- Teich, B., Lutz, R., and Kassarnig, V. (2016). NFL play prediction. _arXiv preprint arXiv:1601.00574_ . 

- Tseng, Y.-T., Kawashima, S., Kobayashi, S., Takeuchi, S., and Nakamura, K. (2020). Forecasting the seasonal pollen index by using a hidden Markov model combining meteorological and biological factors. _Science of The Total Environment_ , 698. 

- Zucchini, W., MacDonald, I. L., and Langrock, R. (2016). _Hidden Markov Models for Time Series: An Introduction Using R_ . Boca Raton: Chapman & Hall/CRC. 

13 


