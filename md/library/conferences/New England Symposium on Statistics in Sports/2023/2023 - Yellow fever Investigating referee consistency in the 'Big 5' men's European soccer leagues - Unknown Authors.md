<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Yellow fever Investigating referee consistency in the 'Big 5' men's European soccer leagues - Unknown Authors.pdf -->

**Some background and exploratory data analysis Modelling the data Results** 

Yellow fever: investigating referee consistency in the ‘Big 5’ men’s European soccer leagues 

## Pete Philipson 

Newcastle University, UK 

NESSIS 2023 - Saturday 23rd September 

**Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Overview 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> **1** Some background and exploratory data analysis 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> **2** Modelling the data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

- **3** Results 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Some background and exploratory data analysis 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Background & motivation 



Interested in a different take on soccer, and working on small count data liable to underdispersion led me to think about yellow cards 



Yellow cards are issued for a moderate disciplinary infraction 



Previous work (using bivariate Poisson and negative binomial models) found evidence of refereeing bias in the English Premier League in the period 1996-2003 [ **?** ] 



It was subsequently found that the number of yellow and red cards received reduced the chance of victory in an ordered probit regression model using data from the Bundesliga [ **?** ] 

**Pete Philipson Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Some background and exploratory data analysis Modelling the data Results** 

# The role of the referee 



In soccer the referee has a somewhat thankless task . . . 

_”The trouble with referees is that they know the rules but they do not know the game.” - Bill Shankly_ 

_”Italian referees can be compared to sheriffs in the Wild West: trying to impose the increasingly flimsy authority of law and order in the face of mistrust, hostility and violence.” - From Calcio by John Foot._ 



‘Akkiappa!’ was a game created by the then-president (!) of Como, Enrico Preziosi - essentially whack-a-mole but with referees - so incensed was he by refereeing decisions against his team 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Application: Yellow cards in the ‘Big 5’ European leagues - (2018/19 2021/22) 



Consider data on the number of yellow cards shown by referees in the ‘Big 5’ European leagues between seasons 2018/19 and 2021/22 



This gives _≈_ 7 _._ 5 _K_ matches with two observations for each match, played between _k_ = 129 teams, overseen by _m_ = 171 referees. 



We also have data before, during, and after the impact of Covid-19 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Application: Yellow cards in the ‘Big 5’ European leagues - (2018/19 2021/22) 



The data on yellow cards (and referees in the case of the EPL) are publicly available at `https://www.football-data.co.uk/` 



Data on referees and crowds are publicly available at `https://fbref.com/en/` 



The two resources can be combined in a fun data-wrangling exercise 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Application: Exploratory data analysis 



Overall mean for yellow cards by league is 



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
3<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br><!-- End of picture text -->



<!-- Start of picture text -->
5<br><!-- End of picture text -->

1.60 with a variance of 1.21 in the Premier League (EPL); 1.91 with a variance of 1.28 in Ligue 1 (L1); 1.82 with a variance of 1.30 in the Bundesliga (BL); 2.36 with a variance of 1.37 in Serie A (SA); 2.49 with a variance of 1.50 in La Liga (LL). 



The mean exceeds the variance for each league = _⇒_ underdispersion 



This ignores the effects of covariates, but suggests underdispersion is a real phenomenon for these data 



Referees are expected to be alike, teams are expected to be different . . . 

**Pete Philipson Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Some background and exploratory data analysis Modelling the data Results** 

# Application: Exploratory data analysis 





How are the counts dispersed at the referee level? The data are made up of 171 (EPL - 27, L1 - 32, BL - 30, SA - 56, LL - 26) - likely heterogeneous - referees 



<!-- Start of picture text -->
0.5 1.0 1.5 2.0 2.5 3.0<br>Mean<br>3.0<br>Variance 2.0<br>1.0<br>0.0<br><!-- End of picture text -->

Figure 1: Variance against mean for yellow cards for each referee in the ‘Big 5’ leagues 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Application: Exploratory data analysis 



Are the number of yellow cards given to home and away teams independent? 



Initially explore this using Kendall’s _τb_ , which can be easily calculated in R; around a quarter of the paired observations are ties, and _τb_ adjusts for this 

Table 1: Values of _τb_ for home and away yellow cards 

|League|_τb_|_p_-value|
|---|---|---|
|EPL|0.15|_<_0_._001|
|L1|0.08|_<_0_._001|
|BL|0.18|_<_0_._001|
|SA|0.12|_<_0_._001|
|LL|0.17|_<_0_._001|



**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Application: Exploratory data analysis 

To explore possible dependency we can look at the ratio of the empirical joint bivariate probabilities to the empirical independent bivariate probabilities: 

|||||Away <br>|yellows<br>|||
|---|---|---|---|---|---|---|---|
|||0|1|2|3|4|_≥_5|
|ws|0|2.07|1.09|1.01|0.75|0.46|0.41|
|llo|1|1.10|1.15|1.05|0.87|0.81|0.70|
|ye|2|0.91|0.99|1.03|1.03|1.03|0.90|
|me|3|0.57|0.95|0.93|1.13|1.28|1.41|
|Ho|4|0.41|0.73|0.97|1.25|1.42|1.78|
||_≥_5|0.42|0.60|0.80|1.37|1.71|2.18|



**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Modelling the data 

**Pete Philipson** 

**Some background and exploratory data analysis** 

**Modelling the data Results** 

Application: Yellow cards in the ‘Big 5’ European leagues - (2018/19 2021/22) 



In order to conduct an analysis that properly accounts for the features of the data (i.e. potential dependence between home and away cards) we desire: 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

- A bivariate count data regression model capable of handling both over and underdispersion; 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- Standard inferences for the covariates; 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

- Routine implementation - preferably broadly comparable to bivariate Poisson, negative binomial models in terms of CPU time; 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

Application: Yellow cards in the ‘Big 5’ European leagues - (2018/19 2021/22) 





We can also think about the covariates for the model itself We would like to have individual (i.e. referee) level effects for the mean and possibly the dispersion 



Also may wish to consider 



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
3<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br><!-- End of picture text -->



<!-- Start of picture text -->
5<br><!-- End of picture text -->



<!-- Start of picture text -->
6<br><!-- End of picture text -->

the effect of being at home; 

whether the absence of fans due to the COVID-19 pandemic made a material difference to the number of cards shown; whether the effect of being behind closed doors differed for the nominal home and away teams; 

differences between teams; 

differences between leagues; 

changes over time (due to rule changes, game focus etc.) 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# The Conway-Maxwell-Poisson distribution 



Routinely adopted count distributions were developed to handle the more common overdispersion. 







The Conway-Maxwell-Poisson (CMP) distribution generalises the Poisson distribution, with an extra parameter to account for possible over- or underdispersion, or _both_ (bidispersion). First introduced in 1962 in the context of queueing [ **?** ]. Little footprint in the statistical literature prior to 2005, but has gained some traction recently. 

**Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Why does handling bidispersion matter? 



Commonly, the Poisson model is too liberal in the presence of overdispersion 



This is typically remedied by a negative binomial (NB) model, or some other Poisson mixture model (or through a zero-altered model) 



In the presence of both types of dispersion the Poisson model will be both conservative and liberal 



An NB model can only help with the overdispersion and is, at best, the same as the Poisson in cases of underdispersion 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# CMP definition 



The CMP distribution has probability mass function given by 

_λ_<sup>_x_</sup> 1 Pr( _X_ = _x | λ, ν_ ) = ( _x_ !)<sup>_ν_</sup> _G∞_ ( _λ, ν_ ) 

with _x_ = 0 _,_ 1 _,_ 2 _, . . . , λ >_ 0 and _ν ≥_ 0. 







_λ_ is the rate parameter and _ν_ models the dispersion. _G∞_ ( _λ, ν_ ) =<sup>�</sup><sup>_∞_</sup> _r_ =0<sup>_λr/_(</sup><sup>_r_!)</sup><sup>_ν_ensuresthattheCMPdistribution</sup> is proper. Several classic discrete distributions are special cases 



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
3<br><!-- End of picture text -->

Poisson ( _ν_ = 1) Geometric ( _ν_ = 0) Bernoulli ( _ν −→∞_ ) 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# The mean-parameterised CMP distribution 







CMP distribution does not provide ‘nice’ inferences. No mean parameter so can only talk about general trends. Can reparameterise in terms of the mean _µ_ 





Rearranging leads to 





Hence, _λ_ is an _n_<sup>_th_</sup> -order polynomial, depending on _µ_ and _ν_ , under this reparameterisation, known as a MPCMP distribution (or CMP _µ_ ). 

**Pete Philipson** 

**Some background and exploratory data analysis** 

**Modelling the data Results** 

# Fitting MPCMP models 



Huang [ **?** ] suggested a hybrid bisection and Newton-Raphson approach to find _λ_ . 



This was applied in small sample Bayesian settings [ **?** ] but is not scaleable. 



Ribeiro et al. [ **?** ] used an asymptotic approximation of _G∞_ ( _λ, ν_ ) to obtain a closed form estimate for _λ_ . 



This approximation is poor for small values of _µ_ and _ν_ (as are often encountered with underdispersion). 



By Descartes’ rule of signs there is one positive, real solution for _λ_ (when _r > µ_ ). 



This allows us to solve the high-order polynomial, but we have to do so many times at each iteration . . . 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# The MPCMP parameterisation in practice 



Can pre-compute look-up tables of values of _λ_ for combinations of _µ, ν_ and then look up _λ_ ( _µ, ν_ ) 



This is done in conjunction with bilinear interpolation and reduces computational times greatly 



Implemented using a step size of 0.01 for both _µ_ and _ν_ , with _µ ∈_ [0 _,_ 19]<sup>_∗_</sup> and _ν ∈_ [0 _,_ 10]. 



Using multiple cores the look-up table can be created in _≈_ 20 seconds 



This approach performs well in simulation studies [ **?** ] 

**Pete Philipson Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Some background and exploratory data analysis Modelling the data Results** 

# The model 

Denoting the yellow cards issued by referee _i_ to team _j_ at home ( _k_ = 1) or away ( _k_ = 2), the linear predictor is modelled by 

log( _µijk_ ) = _β_ League _i_ + _β_ 6 _I_ (Home _ijk_ = 1) + _β_ 7 _I_ (NoFans _ijk_ = 1) + _β_ 8 _I_ (Home _ijk_ = 1) _× I_ (NoFans _ijk_ = 1) + _θi_ + _γj_ 

## where 



**_β_** is the vector of parameters for the league effects, home advantage, no fans and the interaction of interest 



the individual referee effects are captured through _θi , i_ = 1 _, . . ._ 171 





the individual team effects are captured via _γj , j_ = 1 _, . . . ,_ 129 dispersion at the league level is modelled via _ψℓ_ = log( _νℓ_ ) _, ℓ_ = 1 _, . . . ,_ 5 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# The model (continued) 



The dependence between the number of home and away yellow cards is modelled via a copula 



A similar approach has been taken to model disciplinary points [ **?** ], international soccer matches [ **?** ], and English domestic soccer matches [ **?** ] 



A Frank copula was either the only, or preferred, copula in each case - the association is governed by parameter _κ_ 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# The model (continued) 



Suppose _Y_ 1 and _Y_ 2 are a pair of random variables. 



From Sklar [ **?** ], the joint distribution function _F_ may be written in the form 



where _C_ ( _·_ ) is a copula, of which there are many choices. 



Frank’s copula is adopted here, whereby 





We can also add zero (or other) inflation at the marginal level or the joint level 

**Pete Philipson** 

**Some background and exploratory data analysis** 

**Modelling the data Results** 

# The model (continued) 



The association is governed by _κ_ 





This association is also allowed to vary be league, in keeping with our earlier values of _τb_ , via parameters _κℓ, ℓ_ = 1 _, . . . ,_ 5 We adopt mean-parameterised CMP distributions for each marginal cumulative distribution function 



Happily, we can utilise our look-up table & bilinear interpolation approach once more - now just for the cumulative probabilities 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Choice of priors and computational details 



Semi-informative priors are adopted for the league and referee effects 



Vaguer priors are adopted for the dispersions and copula parameters 



Sum-to-zero constraints are placed on the referees and teams _within_ each league 



- 10K MCMC iterations takes _≈_ 20 minutes 

**Pete Philipson Yellow fever: investigating referee consistency in the ‘Big 5’** 

**Some background and exploratory data analysis Modelling the data Results** 

Results 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Results: home and pandemic effects 



The posterior mean effect for being at home is 0 _._ 90 (0 _._ 88 _,_ 0 _._ 94), i.e. a 10% reduction in the rate 



The posterior mean effect for playing behind closed doors is 0 _._ 87 (0 _._ 83 _,_ 0 _._ 92) = _⇒_ a 13% reduction in the rate 



The interaction has a posterior mean of 1 _._ 13 (1 _._ 03 _,_ 1 _._ 22), essentially removing the home effect completely 



The posterior HDIs for the dispersions, _νℓ_ , all lie above one = _⇒_ there is significant underdispersion at play within each league 



The posterior HDIs for _κℓ_ all lie above zero = _⇒_ positive dependence between the home and away yellow cards 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Posterior league effects 



<!-- Start of picture text -->
3.0<br>0.05<br>0.04<br>2.5<br>0.03<br>2.0<br>0.02<br>0.01<br>1.5<br>BL EPL LL L1 SA BL EPL LL L1 SA<br>League League<br>Number of yellow cards<br>Posterior variance of referees<br><!-- End of picture text -->

Figure 2: Boxplots of posterior distributions for the mean league effects (left) and for the variance of the referees (right) 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Posterior mean referee effects 



<!-- Start of picture text -->
120<br>150<br>80<br>100<br>50 40<br>0 0<br>0.8 1.0 1.2 1.4 0.6 0.8 1.0 1.2 1.4<br>Multiplicative effect Multiplicative effect<br>Referee Team<br><!-- End of picture text -->

Figure 3: Posterior HDIs of _θi_ for each referee (left) and team (right) 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Summary table of ‘top’ and ‘tail’ referees 

|Rank|Referee|Country|_E_(_e_<sup>_θ_</sup>)|_SD_(_e_<sup>_θ_</sup>)|
|---|---|---|---|---|
|1|Alejandro Hern´andez|LaLiga|1.27|0.07|
|2|M Dean|EPL|1.20|0.06|
|3|J Brooks|EPL|1.20|0.13|
|4|R East|EPL|1.20|0.11|
|5|Gianluca Rocchi|SerieA|1.19|0.06|
|6|S Attwell|EPL|1.19|0.07|
|7|Fabio Maresca|SerieA|1.19|0.05|
|8|Daniele Orsato|SerieA|1.19|0.05|
|9|C Pawson|EPL|1.18|0.07|
|10|Javier Estrada|LaLiga|1.17|0.07|
|..|..|..|..|..|
|.<br>162|.<br>Harm Osmers|.<br>Bundesliga|.<br>0.88|.<br>0.05|
|163|Florent Batta|Ligue1|0.88|0.05|
|164|G Scott|EPL|0.87|0.05|
|165|Jos´e Luis Munuera|LaLiga|0.86|0.05|
|166|Fabrizio Pasqua|SerieA|0.84|0.04|
|167|Olivier Thual|Ligue1|0.84|0.06|
|168|Tobias Reichel|Bundesliga|0.84|0.07|
|169|Alberola Rojas|LaLiga|0.79|0.04|
|170|Eric Wattellier|Ligue1|0.78|0.04|
|171|Manuel Gr¨afe|Bundesliga|0.77|0.05|



**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Summary table of ‘top’ and ‘tail’ teams 

|Rank|Team|Country|_E_(_e_<sup>_~~γ~~_</sup>)|_SD_(_e_<sup>_~~γ~~_</sup>)|
|---|---|---|---|---|
|1|Paderborn|Bundesliga|1.31|0.12|
|2|Leeds|EPL|1.31|0.09|
|3|Getafe|LaLiga|1.27|0.05|
|4|Leganes|LaLiga|1.22|0.06|
|5|Shefeld United|EPL|1.20|0.09|
|6|Chievo|SerieA|1.19|0.11|
|7|Venezia|SerieA|1.19|0.10|
|8|Metz|Ligue1|1.19|0.07|
|9|Fulham|EPL|1.18|0.09|
|10|Monaco|Ligue1|1.18|0.06|
|..|..|..|..|..|
|.<br>113|.<br>Juventus|.<br>SerieA|.<br>0.86|.<br>0.05|
|114|Inter|SerieA|0.85|0.04|
|115|Girona|LaLiga|0.85|0.09|
|116|Man City|EPL|0.82|0.07|
|117|Guingamp|Ligue1|0.81|0.08|
|118|Real Madrid|LaLiga|0.81|0.04|
|119|Dortmund|Bundesliga|0.81|0.06|
|120|Freiburg|Bundesliga|0.81|0.06|
|121|Atalanta|SerieA|0.79|0.05|
|122|Napoli|SerieA|0.78|0.05|
|123|Bayern Munich|Bundesliga|0.76|0.05|
|124|Liverpool|EPL|0.73|0.06|



**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Model checking: home yellow cards 



<!-- Start of picture text -->
0.10 0.12 0.14 0.16 0.18<br>0.26 0.27 0.28 0.29 0.30<br>0.080 0.085 0.090 0.095<br>0<br>Frequency<br>25<br>0<br>Frequency<br>20<br>0<br>Frequency<br><!-- End of picture text -->



<!-- Start of picture text -->
0.25 0.26 0.27 0.28 0.29<br>0.16 0.17 0.18 0.19 0.20<br>0.040 0.045 0.050 0.055<br>Yellow fever: investigating referee consistency in the ‘Big 5’ men’s European soccer leagues<br>30<br>0<br>Frequency<br>35<br>0<br>Frequency<br>0<br>Frequency<br><!-- End of picture text -->

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Model checking: away yellow cards 



<!-- Start of picture text -->
0.095 0.105 0.115 0.125 0.230 0.240 0.250 0.260<br>0.265 0.275 0.285 0.295 0.185 0.195 0.205 0.215<br>0.095 0.100 0.105 0.110 0.055 0.060 0.065 0.070<br>Pete Philipson Yellow fever: investigating referee consistency in the ‘Big 5’ men’s European soccer leagues<br>0 0<br>Frequency Frequency<br>0 0<br>Frequency Frequency<br>0 0<br>Frequency Frequency<br><!-- End of picture text -->

**Some background and exploratory data analysis Modelling the data Results** 

# Other potential applications of the CMP _µ_ distribution 



Ice-hockey goals at the team level (e.g. Boston Bruins 22/23 season) 

Goals scored 3.72 (2.35) 



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br><!-- End of picture text -->

Goals conceded 2.16 (2.09) 





Baseball at the player level (at bats, runs, hits, home runs) features a host of small counts, liable to underdispersion NFL touchdowns (team level, QB level, . . . ) 



Rushing yards per carry by NFL running backs 

**Pete Philipson** 

**Some background and exploratory data analysis Modelling the data Results** 

# Bibliography I 

**Pete Philipson** 


