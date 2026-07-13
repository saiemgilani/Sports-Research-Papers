<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Bayesian two-stage framework for lineup independent assessment of individual rebounding in the NBA - Unknown Authors.pdf -->

A Bayesian two-stage framework for lineup-independent assessment of individual rebounding ability in the NBA 

Nicholas Kiriazis<sup>1</sup> Christian Genest<sup>1</sup> Alexandre Leblanc<sup>2</sup> 

> 1McGill University 

> 2University of Manitoba 

23 September, 2023 

1 / 27 

# Existing measures for assessing rebounding 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) _→_ Doesn’t account for number of missed shots 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) _→_ Doesn’t account for number of missed shots 

Rebounding rates (proportion of misses) 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) _→_ Doesn’t account for number of missed shots 

Rebounding rates (proportion of misses) _→_ Conveys information about other players on court 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) _→_ Doesn’t account for number of missed shots 

Rebounding rates (proportion of misses) 

_→_ Conveys information about other players on court 

Both these metrics only credit players who collect rebounds themselves 

2 / 27 

# Existing measures for assessing rebounding 

Scaled rebounding counts (per game, per 100, ...) 

- _→_ Doesn’t account for number of missed shots 

Rebounding rates (proportion of misses) 

- _→_ Conveys information about other players on court 

Both these metrics only credit players who collect rebounds themselves 

- _→_ Engelmann (2016) suggests applying Rosenbaum (2004) APM framework to rebounding (more on this later!) 

2 / 27 

# High-level ideas: rebounding 

3 / 27 

# High-level ideas: rebounding 

- Each player has some intrinsic, constant rebounding ability 

3 / 27 

# High-level ideas: rebounding 

- Each player has some intrinsic, constant rebounding ability 

- Individual rebounding allocation is a function of all 10 abilities 

3 / 27 

# High-level ideas: rebounding 

- Each player has some intrinsic, constant rebounding ability 

- Individual rebounding allocation is a function of all 10 abilities 

We propose factorizing individual rebounding rates as follows: 

Pr(A collects rebound) = 

Pr(A collects rebound _∩_ A’s team collects rebound) = 

Pr(A collects rebound _|_ A’s team collects rebound) _×_ <u>�</u> �� <u>�</u> _γ−level_ 



3 / 27 

# High-level ideas: parameter reduction 



Figure: Distribution of possessions played by players in the 2020–21 NBA season. 

4 / 27 

# High-level ideas: parameter reduction 



Figure: Distribution of possessions played by players in the 2020–21 NBA season. 

1. Rosenbaum (2004) replaces all unusable players by a single parameter (the _Replacement Player_ ) 

4 / 27 

# High-level ideas: parameter reduction 



Figure: Distribution of possessions played by players in the 2020–21 NBA season. 

1. Rosenbaum (2004) replaces all unusable players by a single parameter (the _Replacement Player_ ) 

2. Sill (2010) instills an identical prior across all players 

4 / 27 

# High-level ideas: parameter reduction 



Figure: Distribution of possessions played by players in the 2020–21 NBA season. 

1. Rosenbaum (2004) replaces all unusable players by a single parameter (the _Replacement Player_ ) 

2. Sill (2010) instills an identical prior across all players 

We propose a middle ground approach: group players who are similar. (See thesis for details) 

4 / 27 

# Data 

- Rebounding models: play-by-play data 

- Technical note: not all rebounds are allocated to an individual player (referred to as _team rebounds_ ) 

The data were accessed using the NBA API (Patel, 2023), for which the repository can be found at https://github.com/swar/nba api 

5 / 27 

# _γ_ -level rebounding model 

6 / 27 

# _γ_ -level rebounding model 

We are conditioning on the team having the rebound 

6 / 27 

# _γ_ -level rebounding model 

We are conditioning on the team having the rebound 

- _⇒_ Treat each rebound as a multinomial random variable with 6 responses (5 possible players or the team) 

6 / 27 

# _γ_ -level rebounding model 

We are conditioning on the team having the rebound 

- _⇒_ Treat each rebound as a multinomial random variable with 6 responses (5 possible players or the team) 

   - Can’t use traditional multinomial regression 

6 / 27 

# _γ_ -level rebounding model 

We are conditioning on the team having the rebound 

- _⇒_ Treat each rebound as a multinomial random variable with 6 responses (5 possible players or the team) 

   - Can’t use traditional multinomial regression 

   - We have one common category across all lineups 

6 / 27 

# _γ_ -level rebounding model 

We are conditioning on the team having the rebound 

- _⇒_ Treat each rebound as a multinomial random variable with 6 responses (5 possible players or the team) 

   - Can’t use traditional multinomial regression 

   - We have one common category across all lineups 

      - _→_ Model log-odds ratio between individual rebound and team rebound 

6 / 27 

# _γ_ -level rebounding model _cont._ 

Therefore, for arbitrary player _i_ and arbitrary lineup _L_ 







7 / 27 

# _γ_ -level rebounding model _cont._ 

Therefore, for arbitrary player _i_ and arbitrary lineup _L_ 







We use MCMC with a flat prior instead of MLE 

7 / 27 

# Review of APM and RAPM 

8 / 27 

# Review of APM and RAPM 

## Rosenbaum’s APM formula: _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _W_<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ 

_X_ : sparse matrix of substitution-less stints 

_Y_ : vector of net ratings for the home team during each stint 

_W_ : weight matrix to account for irregular number of possessions 

8 / 27 

# Review of APM and RAPM 

## Rosenbaum’s APM formula: _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _W_<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ 

_X_ : sparse matrix of substitution-less stints 

_Y_ : vector of net ratings for the home team during each stint 

_W_ : weight matrix to account for irregular number of possessions 

## Positives: 

▶ Box-score independent (this is what we are looking for!) 

8 / 27 

# Review of APM and RAPM 

## Rosenbaum’s APM formula: _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _W_<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ 

_X_ : sparse matrix of substitution-less stints 

_Y_ : vector of net ratings for the home team during each stint 

_W_ : weight matrix to account for irregular number of possessions 

## Positives: 

- Box-score independent (this is what we are looking for!) 

## Negatives: 

- Assumes response contributions are linearly additive (probabilities?, diminishing returns?) 

- Standard errors are large 

- Doesn’t distinguish between offense and defense 

8 / 27 

# Review of APM and RAPM 

Rosenbaum’s APM formula: _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _W_<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ 

_X_ : sparse matrix of substitution-less stints 

_Y_ : vector of net ratings for the home team during each stint 

- _W_ : weight matrix to account for irregular number of possessions 

## Positives: 

- Box-score independent (this is what we are looking for!) 

- Negatives: 

- Assumes response contributions are linearly additive (probabilities?, diminishing returns?) 

- Standard errors are large 

- Doesn’t distinguish between offense and defense 

Sill’s RAPM formula: _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _W_<sup>_−_1</sup> _X_ + _λI_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ 

_λ_ : regularization parameter, 

_I_ : identity matrix. 

- _⇒_ Solves standard error issue problem by shrinking all players to 

   - common mean 

8 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 









9 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 





_βj_<sup>_O_:offensiveabilityofplayer</sup><sup>_j_,</sup> 



### _→_ Natural parameter space 

9 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 





_βj_<sup>_O_:offensiveabilityofplayer</sup><sup>_j_,</sup> 



_→_ Natural parameter space 

### _→_ Diminishing returns 

9 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 











### _→_ Diminishing returns 



9 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 











### _→_ Diminishing returns 



9 / 27 

# _β_ -level model: proposed mechanism 

Logistic regression allows us to naturally oppose defensive rebounds (success) and offensive rebounds (failure): 



_βi_<sup>_D_:defensiveabilityofplayer</sup><sup>_i_,</sup> 

_βj_<sup>_O_:offensiveabilityofplayer</sup><sup>_j_,</sup> 





_→_ Diminishing returns 

_→_ Separates offense and defense 

We have two severe estimation problems: multicollinearity and unidentifiability 

9 / 27 

# _β_ -level model: multicollinearity 

10 / 27 

# _β_ -level model: multicollinearity 

For rebounding, it doesn’t make sense to assume everyone is equal a priori 

10 / 27 

# _β_ -level model: multicollinearity 

For rebounding, it doesn’t make sense to assume everyone is equal a priori 

- _→_ Individual rebounding rates probably provide a rough idea of _β_ -ability 

10 / 27 

# _β_ -level model: multicollinearity 

For rebounding, it doesn’t make sense to assume everyone is equal a priori 

_→_ Individual rebounding rates probably provide a rough idea of _β_ -ability 

Individual rebounding rates should be reflected in choice of priors, but with appropriate variance 

10 / 27 

# _β_ -level model: multicollinearity 

For rebounding, it doesn’t make sense to assume everyone is equal a priori 

- _→_ Individual rebounding rates probably provide a rough idea of _β_ -ability 

Individual rebounding rates should be reflected in choice of priors, but with appropriate variance 

- _→_ We have an idea of the parameter ordering, but not of the scale 

10 / 27 

# _β_ -level model: unidentifiability 



11 / 27 

# _β_ -level model: unidentifiability 



_→_ We can add some constant _c_ to every parameter (this is okay!) 

11 / 27 

# _β_ -level model: unidentifiability 



_→_ We can add some constant _c_ to every parameter (this is okay!) More problematic case: assume we have equal defenders A and B, equal attackers C and D, but that we have only observed a subset of all possible match ups: 



11 / 27 

# _β_ -level model: unidentifiability 

Recall the proposed model: _p_<sup>_L_</sup> = _<u>e</u>_<sup>_β_</sup> 1<sup>_D_+</sup><sup>_···_+</sup><sup>_β_</sup> 5<sup>_D−β_</sup> 1<sup>_O−···−β_</sup> 5<sup>_O_</sup> 1+ _e_<sup>_β_</sup> 1<sup>_D_+</sup><sup>_···_+</sup><sup>_β_</sup> 5<sup>_D−β_</sup> 1<sup>_O−···−β_</sup> 5<sup>_O_</sup> 

_→_ We can add some constant _c_ to every parameter (this is okay!) More problematic case: assume we have equal defenders A and B, equal attackers C and D, but that we have only observed a subset of all possible match ups: 



_→_ We can play with constants to make any player the best! 

11 / 27 

# _β_ -level model: unidentifiability 

Recall the proposed model: _p_<sup>_L_</sup> = _<u>e</u>_<sup>_β_</sup> 1<sup>_D_+</sup><sup>_···_+</sup><sup>_β_</sup> 5<sup>_D−β_</sup> 1<sup>_O−···−β_</sup> 5<sup>_O_</sup> 1+ _e_<sup>_β_</sup> 1<sup>_D_+</sup><sup>_···_+</sup><sup>_β_</sup> 5<sup>_D−β_</sup> 1<sup>_O−···−β_</sup> 5<sup>_O_</sup> 

_→_ We can add some constant _c_ to every parameter (this is okay!) More problematic case: assume we have equal defenders A and B, equal attackers C and D, but that we have only observed a subset of all possible match ups: 



_→_ We can play with constants to make any player the best! If we restrict the parameter space, we can limit how extreme any re-ordering can be 

_→_ How can we do that? 

11 / 27 

# _β_ -level model: re-phrasing the question 



Figure: Equivalent parameterizations (1, 2, 3) to the true parameterization (*) 

12 / 27 

# _β_ -level model: re-phrasing the question 



Figure: Equivalent parameterizations (1, 2, 3) to the true parameterization (*) 

1. How wide do the offensive and defensive parameter ranges need to be to capture observed player variability? 

12 / 27 

# _β_ -level model: re-phrasing the question 



Figure: Equivalent parameterizations (1, 2, 3) to the true parameterization (*) 

1. How wide do the offensive and defensive parameter ranges need to be to capture observed player variability? 

2. How far apart do we need these clouds to be to express observed rebounding rates? 

12 / 27 

# Answering Question 1: a thought experiment 

13 / 27 

# Answering Question 1: a thought experiment 

_→_ Suppose we could clone the best and worst _β_ -level rebounders ( _βMax_<sup>_D_and</sup><sup>_β_</sup> _Min_<sup>_D_)</sup> 

13 / 27 

# Answering Question 1: a thought experiment 

_→_ Suppose we could clone the best and worst _β_ -level rebounders ( _βMax_<sup>_D_and</sup><sup>_β_</sup> _Min_<sup>_D_)</sup> 

_→_ Play them against an average offensive rebounding lineup 

13 / 27 

# Answering Question 1: a thought experiment 

_→_ Suppose we could clone the best and worst _β_ -level rebounders ( _βMax_<sup>_D_and</sup><sup>_β_</sup> _Min_<sup>_D_)</sup> 

_→_ Play them against an average offensive rebounding lineup 

- _→_ Team defensive rebounding rate is probably less than 90% for the strong lineup, and greater than 50% for the weak lineup 

13 / 27 

# Answering Question 1: a thought experiment 

_→_ Suppose we could clone the best and worst _β_ -level rebounders ( _βMax_<sup>_D_and</sup><sup>_β_</sup> _Min_<sup>_D_)</sup> 

_→_ Play them against an average offensive rebounding lineup 

- _→_ Team defensive rebounding rate is probably less than 90% for the strong lineup, and greater than 50% for the weak lineup 

- _→_ What is the “narrowest” support that allows for that to happen? 

13 / 27 

# Answering Question 1: a thought experiment 

_→_ Suppose we could clone the best and worst _β_ -level rebounders ( _βMax_<sup>_D_and</sup><sup>_β_</sup> _Min_<sup>_D_)</sup> 

_→_ Play them against an average offensive rebounding lineup 

- _→_ Team defensive rebounding rate is probably less than 90% for the strong lineup, and greater than 50% for the weak lineup 

- _→_ What is the “narrowest” support that allows for that to happen? 



13 / 27 

# Answering Question 1: a thought experiment _(cont.)_ 

We can easily solve this using the Lagrangian multiplier 

14 / 27 

# Answering Question 1: a thought experiment _(cont.)_ 

We can easily solve this using the Lagrangian multiplier _→_ We find that _βMax_<sup>_D−β_</sup> _Min_<sup>_D_= 0</sup><sup>_._340</sup> 

14 / 27 

# Answering Question 1: a thought experiment _(cont.)_ 

We can easily solve this using the Lagrangian multiplier _→_ We find that _βMax_<sup>_D−β_</sup> _Min_<sup>_D_= 0</sup><sup>_._340</sup> 

_→_ This is a very similar scale to individual rebounding rates! 

14 / 27 

# Answering Question 1: a thought experiment _(cont.)_ 

We can easily solve this using the Lagrangian multiplier _→_ We find that _βMax_<sup>_D−β_</sup> _Min_<sup>_D_= 0</sup><sup>_._340</sup> 

_→_ This is a very similar scale to individual rebounding rates! 

_→_ We similarly find that _βMax_<sup>_O−β_</sup> _Min_<sup>_O_= 0</sup><sup>_._292(weallowedfora</sup> difference of 35% since offensive rebounding shows less variation) 

14 / 27 

# Answering Question 1: a thought experiment _(cont.)_ 

We can easily solve this using the Lagrangian multiplier _→_ We find that _βMax_<sup>_D−β_</sup> _Min_<sup>_D_= 0</sup><sup>_._340</sup> 

_→_ This is a very similar scale to individual rebounding rates! 

_→_ We similarly find that _βMax_<sup>_O−β_</sup> _Min_<sup>_O_= 0</sup><sup>_._292(weallowedfora</sup> difference of 35% since offensive rebounding shows less variation) 

We have an (approximate) upper bound on the size of each cloud! 

14 / 27 

# Answering Question 2: re-defining the model 

We can re-write the true parameterization in terms of any other valid parameterization, along with some shift in the “clouds”: 



15 / 27 

# Answering Question 2: re-defining the model 

We can re-write the true parameterization in terms of any other valid parameterization, along with some shift in the “clouds”: 



_→_ Equivalent solution since it preserves ordering and has identical predictions 

15 / 27 

# Answering Question 2: re-defining the model 

We can re-write the true parameterization in terms of any other valid parameterization, along with some shift in the “clouds”: 



- _→_ Equivalent solution since it preserves ordering and has identical predictions 

- _→_ We can force the clouds anywhere, as long as we include the _α_ parameter to space them out accordingly 

15 / 27 

# Answering Question 2: re-defining the model 

We can re-write the true parameterization in terms of any other valid parameterization, along with some shift in the “clouds”: 



- _→_ Equivalent solution since it preserves ordering and has identical predictions 

_→_ We can force the clouds anywhere, as long as we include the _α_ parameter to space them out accordingly 

- _→_ We can (probably) learn the shift from the data 

15 / 27 

# Formal _β_ -level model formulation 

We propose using the following hierarchical Bayesian framework: 



## where 



16 / 27 



# A simulation study 

Details can be found in my thesis. The key points are: 

17 / 27 



# A simulation study 

Details can be found in my thesis. The key points are: 

_→_ Sample sizes are comparable to that of one NBA season 

17 / 27 



# A simulation study 

Details can be found in my thesis. The key points are: 

_→_ Sample sizes are comparable to that of one NBA season 

- _→_ We recover the original parameters by equally distributing the estimated shift amongst the ten players 

17 / 27 



# A simulation study 

Details can be found in my thesis. The key points are: 

_→_ Sample sizes are comparable to that of one NBA season 

- _→_ We recover the original parameters by equally distributing the estimated shift amongst the ten players 

- _→_ We repeat a high variance and low variance version of the simulation 

17 / 27 

# A simulation study 

## Details can be found in my thesis. The key points are: 

_→_ Sample sizes are comparable to that of one NBA season 

- _→_ We recover the original parameters by equally distributing the estimated shift amongst the ten players 

- _→_ We repeat a high variance and low variance version of the simulation 



17 / 27 

# Results - _β_ -level estimates 



Figure: Standard deviations ( _y_ -axis) of each posterior distribution against the posterior mean ( _x_ -axis). 

18 / 27 

# Results - Sanity check 



Figure: Posterior mean against prior mean. 

19 / 27 

# Results - _γ_ -level estimates 



Figure: Standard deviations ( _y_ -axis) of each posterior distribution against the posterior mean ( _x_ -axis) of the _γ_ -level parameters. Color represents the number of minutes of the player in question, and is a proxy for the number of multinomial observations used to estimate the parameter. 

20 / 27 

# Results - Binned predictions 



Figure: Predicted probabilities ( _y_ -axis) against observed probabilities ( _x_ -axis) for seen and unseen lineups during the 2021–22 NBA season. Note that the groups for the unseen lineups contain each about 1940 observations, and the seen lineup groups contain about 560 observations. 

21 / 27 

# Results - Individual predictions 



Figure: Two-stage predicted vs observed rebounding counts for individual players during the 2021–22 season. 

22 / 27 

# Results - Practical example 



23 / 27 

# Results - Trends 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

   - _→_ Forcing rotations and defense is out of position? 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

_→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

   - _→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

_→_ Forcing long close outs? 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

_→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

_→_ Forcing long close outs? 

- Ball-handlers are overrated defensive rebounders 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

_→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

_→_ Forcing long close outs? 

- Ball-handlers are overrated defensive rebounders 

_→_ No box-out responsibilities? 

_→_ Teams funnel rebounds to their guards? 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

_→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

_→_ Forcing long close outs? 

- Ball-handlers are overrated defensive rebounders 

_→_ No box-out responsibilities? 

_→_ Teams funnel rebounds to their guards? 

- Some traditional centers are overrated offensive rebounders 

24 / 27 

# Results - Trends 

- Ball-dominant offensive engines are underrated offensive rebounders 

_→_ Forcing rotations and defense is out of position? 

- Long-range threats are underrated offensive rebounders 

   - _→_ Forcing long close outs? 

- Ball-handlers are overrated defensive rebounders 

_→_ No box-out responsibilities? 

_→_ Teams funnel rebounds to their guards? 

- Some traditional centers are overrated offensive rebounders 

_→_ Guaranteed to collect rebounds because of proximity to basket? 

24 / 27 

# Limitations 

25 / 27 

# Limitations 

Need to carefully think about blocked shots. 

25 / 27 

# Limitations 

Need to carefully think about blocked shots. 

How important were the omitted covariates? 

25 / 27 

# Further details 

Thesis can (eventually) be found by searching by name here: https://escholarship.mcgill.ca/ 

Questions and comments can be sent to me by email: nicholas.kiriazis@mail.mcgill.ca 

26 / 27 

# References 









Engelmann, J. (2016). Possession-based player performance analysis in basketball (adjusted +/– and related concepts). In _Handbook of Statistical Methods and Analyses in Sports_ . Chapman; Hall/CRC. Patel, S. (2023). Nba api. Rosenbaum, D. T. (2004). Measuring how NBA players help their teams win. Retrieved January 18, 2023, from http://www.82games.com/comm30.htm# ~~f~~ tn1 Sill, J. (2010). Improved NBA adjusted +/- using regularization and out-of-sample testing. _Proceedings of the 2010 MIT Sloan Sports Analytics Conference_ . 

27 / 27 


