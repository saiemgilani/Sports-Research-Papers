<!-- source: library/conferences/New England Symposium on Statistics in Sports/2015/2015 - Nearest-neighbor matchup effects Predicting March Madness - Unknown Authors.pdf -->

# Nearest-Neighbor Matchup Effects: Predicting March Madness 

Andrew Hoegh, Marcos Carzolio, Ian Crandell, Xinran Hu, Lucas Roberts, Yuhyun Song, Scotland Leman Department of Statistics, Virginia Tech 

September 26, 2015 

## Who is has out an NCAA bracket before? 



<mark>2 / 36</mark> 

<mark>Introduction</mark> 

<mark>Motivation</mark> 

## Who has won an NCAA bracket competition? 



<mark>3 / 36</mark> 

<mark>Introduction</mark> 

<mark>Motivation</mark> 

Who has lost a bracket competition to someone that does not know what a basketball looks like? 



<mark>4 / 36</mark> 

<mark>Introduction</mark> 

<mark>Motivation</mark> 

General modeling strategies for NCAA tournament competitions Matchup effects modeling framework Uncertainty inherent in NCAA tournament & competitions 

<mark>5 / 36</mark> 

<mark>Overview</mark> 

<mark>Introduction</mark> 





<mark>General Modeling Competition Types 6 / 36</mark> 

_L_ ( _y,_ ˆ _y_ ) = _cδ_ ( _y_ = ˆ _y_ ) _L_ ( _y,_ ˆ _y, r_ ) = _cr δ_ ( _y_ = ˆ _y_ ) 



<mark>7 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Decision Theory</mark> 

_L_ ( _y, p_ ) = _−y_ log( _p_ ) _−_ (1 _−y_ ) log(1 _−p_ ) 

This is a _proper_ scoring rule. 



<!-- Start of picture text -->
Kaggle loss function<br>0.0 0.2 0.4 0.6 0.8 1.0<br>P<br>7<br>6<br>5<br>4<br>3<br>L(y=1,p)<br>2<br>1<br>0<br><!-- End of picture text -->

<mark>8 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Decision Theory</mark> 

There are many important characteristics useful for modeling the strength of an NCAA basketball team: 

Winning percentage, Point differential, 

Strength of schedule, Conference affiliation, 

. . . 

Rebounding percentage, Adjusted offensive efficiency, and Adjusted defensive efficiency. 

<mark>9 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Rather than using team characteristics, there are many available rating and ranking systems: 

ESPN BPI, Sagarin, RPI, 

Pomeroy, and Logistic Regression/Markov Chain (LRMC). 

<mark>10 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Typically the model framework for predicting winner of games (or winning probabilities) can be formulated as a relative strength model. Formally this can be expressed as: 

_yij_ = _f_ ( **_θ_** _i,_ **_θ_** _j_ ) 

<mark>11 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Typically the model framework for predicting winner of games (or winning probabilities) can be formulated as a relative strength model. Formally this can be expressed as: 

_yij_ = _f_ ( **_θ_** _i,_ **_θ_** _j_ ) such as 

linear model: _yij_ = _βhome_ + ( _θi − θj_ ) _βD_ + _ϵij,_ where _ϵij ∼ N_ (0 _, σ_<sup>2</sup> ) 

<mark>11 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Typically the model framework for predicting winner of games (or winning probabilities) can be formulated as a relative strength model. Formally this can be expressed as: 

_yij_ = _f_ ( **_θ_** _i,_ **_θ_** _j_ ) such as 

linear model: _yij_ = _βhome_ + ( _θi − θj_ ) _βD_ + _ϵij,_ where _ϵij ∼ N_ (0 _, σ_<sup>2</sup> ) 

or 

logistic regression: _yij ∼ Bernoulli_ ( _pij_ ) where _logit_ ( _pij_ ) = _βhome_ + ( _θi − θj_ ) _βD_ 

<mark>11 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Note that relative strength models of this type are strictly transitive, where _PA>B_ denotes the probability that team A beats team B. Under transitive models, 

_{PA>B >_ 0 _._ 5 _∪ PB>C >_ 0 _._ 5 _} ⇒ PA>C >_ 0 _._ 5 _._ 

<mark>12 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Bayesian Linear Model Prior _β ∼ N_ ( _β_ ; _m, s_ ) Likelihood _β|Y , X ∝ N_ ( _β_ ; _β,_<sup>ˆ</sup> Σ) Posterior _β|Y , X ∼ N_ ( _β_ ; _µ,_ Σ _β_ ) 



<mark>13 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Bayesian Linear Model Prior _β ∼ N_ ( _β_ ; _m, s_ ) Likelihood _β|Y , X ∝ N_ ( _β_ ; _β,_<sup>ˆ</sup> Σ) Posterior _β|Y , X ∼ N_ ( _β_ ; _µ,_ Σ _β_ ) 



<mark>14 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Bayesian Linear Model Prior _β ∼ N_ ( _β_ ; _m, s_ ) Likelihood _β|Y , X ∝ N_ ( _β_ ; _β,_<sup>ˆ</sup> Σ) Posterior _β|Y , X ∼ N_ ( _β_ ; _µ,_ Σ _β_ ) 



<mark>15 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

Bayesian Linear Model 

Predictive: _p_ ( _Y_<sup>_∗_</sup> _|X_<sup>_∗_</sup> _, Y , X_ ) = _p_ ( _Y_<sup>_∗_</sup> _|X_<sup>_∗_</sup> _, β_ ) _p_ ( _β|Y , X_ ) _dβ_ � 0 _P_ ( _Y_<sup>_∗_</sup> _<_ 0) = _p_ ( _Y_<sup>_∗_</sup> _|X_<sup>_∗_</sup> _, Y , X_ ) _dY_<sup>_∗_</sup> � _−∞_ 



<mark>16 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 



<mark>General Modeling Data 17 / 36</mark> 

A substantial challenge in predictive modeling of sports competitions, and major discussion point, is predicting upsets. Consider ”predicting upsets” as a comparison of the probabilistic predictions for competitors. 

<mark>18 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

### **Distribution of Predictions** 

A substantial challenge in predictive modeling of sports competitions, and major discussion point, is predicting upsets. Consider ”predicting upsets” as a comparison of the probabilistic predictions for competitors. 



<!-- Start of picture text -->
Your<br> Prediction<br>0.0 0.1 0.2 0.3 0.4 0.5<br>P(Upset)<br><!-- End of picture text -->

<mark>18 / 36</mark> 

<mark>General Modeling</mark> 

<mark>Data</mark> 

“Well, it’s hard to predict a particular team. You have to look at the higher seed and see, do they overwhelm the smaller school or the lower seed? Can they overwhelm someone with their athleticism or length or size or quickness or speed? Do they play a particular style of the pressure defense? And I think I look at the lower seed then and say, can they counter the higher seed’s strengths? Do they shoot the three point shot well? Do they have athleticism at certain positions? Do they play a particular style that will give the higher seed trouble?” Andy Enfield 

<mark>19 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>motivation</mark> 



<!-- Start of picture text -->
5 10 15 20<br>Games<br>Neighbor Matchup Efectsects motivation 20 / 36<br>10<br>5<br>Observed Results 0<br><!-- End of picture text -->

<mark>Nearest Neighbor Matchup Efectsects</mark> 



<!-- Start of picture text -->
Estimated<br> Strength<br>5 10 15 20<br>Games<br>Neighbor Matchup Efectsects motivation 21 / 36<br>10<br>5<br>Observed Results 0<br><!-- End of picture text -->

<mark>Nearest Neighbor Matchup Efectsects</mark> 



<!-- Start of picture text -->
5 10 15 20<br>Games<br>Neighbor Matchup Efectsects motivation 22 / 36<br>10<br>5<br>Observed Results 0<br><!-- End of picture text -->

<mark>Nearest Neighbor Matchup Efectsects</mark> 



<!-- Start of picture text -->
5 10 15 20<br>Games<br>10<br>5<br>Observed Results 0<br><!-- End of picture text -->

<mark>23 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>motivation</mark> 

Estimation of the nearest-neighbor matchup effects has three components: 

1. Fit a relative strength model, 

2. Identify neighbors for the matchup, and 

3. Calibrate the matchup adjustment. 

<mark>24 / 36</mark> 

<mark>Outline</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

Consider the simple relative strength model using the Sagarin ratings and home court 

_Yij_ = _βhome_ + _DijβD_ + _ϵij, ϵij ∼ N_ (0 _, σ_<sup>2</sup> ) where _Dij_ = Sagarin _i −_ Sagarin _j_ 

<mark>25 / 36</mark> 

<mark>Relative Strength Model</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

Consider the simple relative strength model using the Sagarin ratings and home court 

_Yij_ = _βhome_ + _DijβD_ + _ϵij, ϵij ∼ N_ (0 _, σ_<sup>2</sup> ) where _Dij_ = Sagarin _i −_ Sagarin _j_ 

Note that relative strength models of this type are strictly transitive. 

<mark>25 / 36</mark> 

<mark>Relative Strength Model</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

Identifying neighbors first requires specifying team characteristics and a distance function between teams. We used a collection of data from Ken Pomeroy’s `www.kenpom.com` including: Effective Height Adjusted Tempo Effective Field Goal Percentage Defense Offensive Rebound Percentage Block Percentage Steal Rate 

Three Point Field Goal Contribution 

<mark>26 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Identifying Neighbors</mark> 



<mark>Nearest Neighbor Matchup Efects Identifying Neighbors 27 / 36</mark> 



<mark>Nearest Neighbor Matchup Efects Identifying Neighbors 28 / 36</mark> 



<mark>Nearest Neighbor Matchup Efects Identifying Neighbors 29 / 36</mark> 

For each particular matchup, say Dayton vs. Stanford, identify past opponents to see who is most like the current opponent. Teams Dayton played similar to Stanford Teams Stanford played similar to Dayton 

California George Mason Georgia Tech George Washington Gonzaga 

Cal Poly California Oregon Pittsburgh Utah 

<mark>30 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Identifying Neighbors</mark> 

Let _Rj_ ( _i_ ) = _K_<sup><u>1</u></sup> � _k∈Nj_<sup>(</sup><sup>_Yik−µik_),where</sup><sup>_Nj_aretheneighborsforteam</sup><sup>_i_</sup> with respect to team _j_ , _Yik_ is the observed point differential between team _i_ , and team _k_ and _µik_ is the expected point differential between team _i_ and team _k_ . 

Then _φij_ = _ρ_ ( _Ri_ ( _j_ ) _−Rj_ ( _i_ )), where _ρ_ controls how much information is passed from the neighbors. 

<mark>31 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Matchup Adjustment</mark> 

Then using the relative strength model previously described, the predictive distribution becomes: 

_Yij|Xij_ = _βhome_ + _DijβD_ + _φij_ + _ϵij_ 

Effectively _φij_ shifts the predictive distribution and results in a non-transitive model. 

<mark>32 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Matchup Adjustment</mark> 

Using data across NCAA tournaments from 2007 - 2013, the model parameters are estimated. 

||_βhome_|_βD_|_σ_<sup>2</sup>|_ρ_|
|---|---|---|---|---|
|Posterior mean|3.87|0.913|121.6|0.167|
|Credible interval|(3.83,3.91)|(0.909,0.916)|(120.0,123.2)|(0.012,0.454)|



The positive credible interval suggests a moderate, but meaningful result from the matchup effect. 

<mark>33 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Results</mark> 

## Largest shifts in expected point spread ( _φij_ ). 

|Team1|Team1|_R_1(2)|_R_2(1)|_φ_12|
|---|---|---|---|---|
|Cal Poly|Wichita St.|7.52|-0.44|1.59|
|UConn|St. Joes|0.70|-8.80|1.90|
|Dayton|Stanford|14.97|-0.55|3.10|
|Dayton|Syracuse|8.65|-2.83|2.30|
|Kentucky|Michigan|2.2|-5.87|1.62|
|UMass|Tennessee|-1.75|7.16|-1.78|
|Memphis|Virginia|-8.09|4.74|-2.57|
|Michigan|Tennessee|-2.85|6.55|-1.88|
|Michigan|Texas|-5.87|5.12|-2.20|
|Syracuse|W.Mich|6.27|-5.52|2.36|



<mark>34 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Demonstration</mark> 

|Team|Neighbor|Point Dif.|E[Point Dif]|Residual|
|---|---|---|---|---|
|Dayton|California|18|-0.9|18.9|
|Dayton|Gonzaga|5|-12.4|17.4|
|Dayton|George Mason|17|3.4|13.6|
|Dayton|Georgia Tech|10|-5.3|15.3|
|Dayton|George Washington|10|0.4|9.6|
|Stanford|California|-7|4.1|-11.1|
|Stanford|California|11|-2.3|13.3|
|Stanford|Oregon|2|-8.9|10.9|
|Stanford|Pittsburgh|-21|-5.3|-15.7|
|Stanford|Cal Poly|17|13.8|3.2|
|Stanford|Utah|1|4.9|-3.9|



<mark>35 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Demonstration</mark> 





1. Evaluated on small number of data points leads to very uncertain outcomes, even with quality predictions 

2. Does this contest actually have a proper scoring rule? 

3. Alternative strategies (maximizing expected return). 

<mark>36 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Demonstration</mark> 

1. Evaluated on small number of data points leads to very uncertain outcomes, even with quality predictions 

2. Does this contest actually have a proper scoring rule? 

3. Alternative strategies (maximizing expected return). 





<mark>36 / 36</mark> 

<mark>Nearest Neighbor Matchup Efects</mark> 

<mark>Demonstration</mark> 


