<!-- source: library/conferences/New England Symposium on Statistics in Sports/2015/2015 - A Bayesian hierarchical model to estimate the framing ability of major league baseball catchers - Unknown Authors.pdf -->

**A Bayesian Hierarchical Model To Estimate the Framing Ability of Major League Baseball Catchers** 

Sameer K. Deshpande and Abraham J. Wyner Statistics Department, The Wharton School University of Pennsylvania 

26 September 2015 



Introduction 

- What exactly is framing? 

   - A catcher’s effect on the likelihood a taken pitch is called a strike. 

- Should we even care about framing? 

   - Lots of attention in popular presst 

   - Several articles on Baseball Prospectus and Hardball Times 

   - “Good framer” can save _∼_ 15 - 25 runs per season. 

   - Teams seem to care: Hank Conger, Russell Martin 

<mark>NESSIS 2015 2 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>Catcher Framing</mark> 

# Fundamental Question and Our Contribution 

For any given _taken_ pitch, what is the catcher’s effect on likelihood of pitch being called strike over and above factors like: 

   - Pitch Location 

   - Pitch Context: Count, base runners, score differential, etc. 

   - Pitch Participants: batter, pitcher, umpire 

- Our contributions: 

   - Hierarchical Bayesian logistic regression model of called strike 

      - probability 

   - Value of a called strike as function of count 

   - Uncertainty estimates of framing impact (runs saved on average) 

<mark>3 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

PITCHf/x Data 

## PITCHf/x data scraped from MLB Advanced Media: 

- Horizontal and vertical coordinate of pitch as it crosses plate 

- Approximate vertical boundaries for the strike zone 

- Umpire, pitcher, catcher, batter identities 

- Count 

Focus only on the 320,308 taken pitches within 1 ft. of the strike zone. 

<mark>4 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# Parameterizing Pitch Location 



- (a) Distance from strike zone, _R_ (b) Angles from horizontal and vertical 

Figure : _R, ϕ_ 1 _, ϕ_ 2 for RHB 

<mark>5 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# Bayesian Logistic Regression Model 

For umpire _u_ , log-odds of calling a strike is a linear function of: 

_R, ϕ_ 1 _, ϕ_ 2 _,_ and indicators for batter, catcher, pitcher, and count 

Let Θ<sup>(</sup><sup>_u_)</sup> be vector of covariate partial effects. Place common prior on Θ<sup>(</sup><sup>_u_)</sup> ’s (“borrow strength” between umpires)<sup>i.i.d</sup> Θ<sup>(1)</sup> _, . . . ,_ Θ<sup>(93)</sup> _∼_ � Cauchy(0 _, λj_ ) _. j_ 

- _λj_ = 2 _._ 5 as in [Gelman et. al (2008)]. 

- Gibbs sampling facilitated by Polya-Gamma data augmentation [Polson, Scott, and Windle (2013)] 

- Identifiability: designate one batter, catcher, and pitcher as baseline 

<mark>6 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

Differences between umpires’ probability of calling strikes 



Figure : Inside _−→_ Outside 

<mark>NESSIS 2015 7 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>Catcher Framing</mark> 

# Impact of Framing 

For each catcher, look at all of the called pitches he received: 

   - _p_ ˆ: fitted probability of strike 

   - _p_ ˆ<sup>0</sup> : fitted probability of strike with catcher replaced by baseline catcher 

   - _p_ ˆ _− p_ ˆ<sup>0</sup> : catcher’s “framing effect” 

   - Value of called strike, based on count, _ρ_ 

- Sum _ρ ×_ � _p_ ˆ _− p_ ˆ<sup>0�</sup> over all called pitches received 

- **Value of a called strike depends on the count!** 

<mark>8 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# – Value of a called strike on an 0 1 pitch 

## Between 2011 and 2014: 

- 182,405 0 – 1 pitches taken: 140,667 balls, 41,738 called strikes 

- Avg. # runs allowed in rest of inning after called ball: 0.322 

- Avg. # runs allowed in rest of inning after called strike: 0.265 

**Conditional on an 0 – 1 pitch being taken** : 

called strike saves _ρ_ = 0 _._ 057 runs, on average 

<mark>9 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# Expected Runs Saved Over All Pitches 

|Rank|Catcher|Runs Saved|95% Interval|Num. Pitches|
|---|---|---|---|---|
|1.|Hank Conger|13.95|[6.12, 22.38]|5515|
|2.|Miguel Montero|11.87|[3.51, 21.48]|9272|
|3.|Brian McCann|9.89|[1.90, 17.54]|7350|
|4.|Jose Molina|9.69|[1.90, 17.54]|5301|
|5.|Jonathan Lucroy|8.99|[0.95, 19.08]|9571|
|6.|Mike Zunino|8.97|[0.16, 18.34]|8822|
|7.|Rene Rivera|8.92|[1.34, 13.76]|5925|
|8.|Christian Vazquez|7.5|[1.44,13.76]|3770|
|9.|Russell Martin|7.37|[-0.24, 15.61]|7228|
|10.|Buster Posey|6.37|[-0.75, 14.69]|7441|



Table : _ρ ×_ � _p_ ˆ _− p_ ˆ<sup>0�</sup> summed over all of catcher’s called pitches 

<mark>10 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# Ongoing and Future Work: 

## _•_ Other ways to incorporate pitch location: 

- Alternative parameterizations of strike zone 

- Non-parametric approach: generalized additive models 

## _•_ Out-of-sample performance 

## _•_ Improved Runs saved calculation 

- Non-uniform distribution of framing opportunities 

- Integrate _ρ ×_ � _p_ ˆ _− p_ ˆ<sup>0�</sup> over batter, pitcher, umpire, count, and location. 

- Framing analog of SAFE [Jensen, Shirley, and Wyner (2008)] 

<mark>11 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# References 







Gelman, A., Jakulin, A., Pittau, M., and Su, Y. (2008) “A weakly informative default prior for logistic and other regression models.” _Annals of Applied Statistics_ , 2:4, 1360–1383. Polson, N.G., Scott, J.G., and Windle, J. (2013) “Bayesian inference for logistic models using Polya-Gamma latent variables.” _Annals of Statistics_ , 108:504, 1339-1349 Jensen, S.T., Shirley, K.E., Wyner, A.J. (2008) “Bayesball: A Bayesian hierarchical model for evaluating fielding in Major League Baseball.” _Annals of Applied Statistics_ , 3:2, 491–520. 

<mark>12 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

# Acknowledgements 

Special thanks to 

- Hugh MacMullan and Wharton High-Performance Computing team. 

- NESSIS Organizers 

- All of y’all 

_Please send any ideas or questions!_ 

Email: dsameer@wharton.upenn.edu Paper and code will be available soon: `www-stat.wharton.upenn.edu/~dsameer/pitchFraming/pitchFraming.html` 

<mark>13 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 

Estimated Strike Probabilities 



<mark>NESSIS 2015 14 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>Catcher Framing</mark> 

# Average # Runs Given Up and Value of Strike 

|Count|Ball|Strike|Value of strike, _ρ_|
|---|---|---|---|
|0-0|0.367 (0.002)|0.305 (0.002)|0.062 (0.002)|
|0-1|0.322 (0.002)|0.265 (0.004)|0.057 (0.004)|
|0-2|0.276 (0.003)|0.178 (0.007)|0.098 (0.008)|
|1-0|0.427 (0.003)|0.324 (0.003)|0.103 (0.005)|
|1-1|0.364 (0.003)|0.280 (0.004)|0.084 (0.005)|
|1-2|0.302 (0.003)|0.162 (0.006)|0.140 (0.006)|
|2-0|0.571 (0.007)|0.370 (0.006)|0.201 (0.009)|
|2-1|0.468 (0.005)|0.309 (0.006)|0.159 (0.008)|
|2-2|0.383 (0.004)|0.165 (0.006)|0.218 (0.007)|
|3-0|0.786 (0.013)|0.481 (0.008)|0.305 (0.015)|
|3-1|0.730 (0.010)|0.403 (0.009)|0.327 (0.014)|
|3-2|0.706 (0.008)|0.166 (0.008)|0.540 (0.011)|



### Table : Standard errors in parentheses 

<mark>15 / 15</mark> 

<mark>Deshpande & Wyner</mark> 

<mark>NESSIS 2015</mark> 

<mark>Catcher Framing</mark> 


