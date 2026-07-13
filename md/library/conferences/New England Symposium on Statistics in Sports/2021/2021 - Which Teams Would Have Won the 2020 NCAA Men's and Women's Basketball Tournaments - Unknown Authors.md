<!-- source: library/conferences/New England Symposium on Statistics in Sports/2021/2021 - Which Teams Would Have Won the 2020 NCAA Men's and Women's Basketball Tournaments - Unknown Authors.pdf -->

Which Teams Would Have Won the 2020 NCAA Men’s and Women’s Basketball Tournaments? 

Chancellor Johnstone, Dan Nettleton 

October 24, 2021 

1 / 28 

# Background 



In 2020, the NCAA Division 1 Basketball tournaments (along with several conference tournaments) were cancelled due to COVID-19. 



We want to determine tournament win probabilities through the estimation of team strength. 

2 / 28 

# Question of Interest 

Given a collection of game-by-game win probabilities, can we generate tournament win probabilities for each team? 

3 / 28 

# Knockout Tournament Win Probability 



The probability for a team _i_ winning in round _J_ is, 







“the probability of team _i_ winning in round _J_ ” We can also determine the probability that a team makes the tournament based on their conference and estimated strength. 

[Edwards, 1991] 

4 / 28 

# 8-team Knockout Tournament Example 



<!-- Start of picture text -->
1<br>8<br>4<br>5<br>3<br>6<br>2<br>7<br><!-- End of picture text -->

Figure 1: Bracket for eight team single-elimination tournament. 

5 / 28 

# 8-team Knockout Tournament Example Probabilities 

Table 1: Example win probability matrix for eight team knockout tournament 

||1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|1||0.35|0.23|0.14|0.08|0.05|0.03|0.01|
|2|0.65||0.35|0.23|0.14|0.08|0.05|0.03|
|3|0.77|0.65||0.35|0.23|0.14|0.08|0.05|
|4|0.86|0.77|0.65||0.35|0.23|0.14|0.08|
|5|0.92|0.86|0.77|0.65||0.35|0.23|0.14|
|6|0.95|0.92|0.86|0.77|0.65||0.35|0.23|
|7|0.97|0.95|0.92|0.86|0.77|0.65||0.35|
|8|0.99|0.97|0.95|0.92|0.86|0.77|0.65||



6 / 28 

# 8-team Knockout Tournament Example 

Table 2: Probability of winning each round 

||Round 1|Round 2<br>Final|
|---|---|---|
|1|0.99|0.87<br>0.60|
|8|0.01|0.00<br>0.00|
|4|0.65|0.10<br>0.03|
|5|0.35|0.03<br>0.01|
|3|0.86|0.33<br>0.10|
|6|0.14|0.02<br>0.00|
|2|0.95|0.65<br>0.27|
|7|0.05|0.01<br>0.00|



7 / 28 

# Question of Interest 

Given the two teams playing, can we estimate margin of victory? 

8 / 28 

# The Harville Method 







_Mij_ = observed margin of victory (MOV) for team _i_ playing at _−_ home against team _j_ (home score away score). _H_ = home field advantage parameter. 







_Si, Sj_ = strengths of team _i_ and team _j_ , respectively. _eij_ = unobserved, random error associated with team _i_ playing at home against team _j_ . _H, Si, Sj_ estimated from game-outcome data. 

[Harville, 1977] 

9 / 28 

# Four Team Example 

|Week|Home Team|Away Team<br>Home Score|Away Score|MOV|
|---|---|---|---|---|
|1|3|1<br>11|16|5|
|1|4|2<br>14|7|-7|
|2|4|1<br>10|19|9|
|2|3|2<br>21|24|3|
|3|1|4<br>14|13|-7|
|3|2|3<br>3|28|25|
|||5_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_3_−_<sup>ˆ</sup>_S_1|||
|||_−_7_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_4_−_<sup>ˆ</sup>_S_2|||
|||9_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_4_−_<sup>ˆ</sup>_S_1|||
|||3_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_3_−_<sup>ˆ</sup>_S_2|||
|||_−_7_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_3_−_<sup>ˆ</sup>_S_4|||
|||25_≈_<sup>ˆ</sup>_H_+ <sup>ˆ</sup>_S_2_−_<sup>ˆ</sup>_S_1|||



10 / 28 

# Example Data Team Strengths 



Team strengths for example data are, 

ˆ ˆ ˆ ˆ ˆ _H_ = 5 _._ 75 _, S_ 1 = _−_ 6 _._ 125 _, S_ 2 = 9 _._ 375 _, S_ 3 = _−_ 3 _._ 375 _, S_ 4 = 0 _._ 125 _._ 

11 / 28 

# 2019-2020 Regular Season Team Strengths 

Table 3: Ranks for top 10 NCAA men’s teams in 2020 

Table 4: Ranks for top 10 NCAA women’s teams in 2020 

|Team|ˆ_θ_|Rank|AP|NET|KP|Team|ˆ_θ_|Rank|AP|RPI|CSM|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Kansas|25.25|1|1|2|1|Connecticut|27.35|1|5|4|3|
|Gonzaga|22.79|2|2|1|2|South Carolina|23.32|2|1|1|1|
|Duke|22.31|3|11|6|5|Stanford|22.54|3|7|6|7|
|Michigan State|20.54|4|9|7|7|Oregon|22.41|4|2|2|2|
|Baylor|20.44|5|5|5|3|Princeton|21.18|5|22|9|20|
|Arizona|19.39|6|-|14|19|Oregon State|20.95|6|14|20|17|
|San Diego State|18.65|7|6|4|6|Louisville|20.95|7|6|7|6|
|West Virginia|18.43|8|24|17|10|Baylor|20.64|8|3|4|4|
|Ohio State|18.22|9|19|16|8|Kentucky|20.13|9|16|24|-|
|Dayton|18.07|10|3|3|4|Arizona|18.44|10|12|28|16|



12 / 28 

# Question of Interest 

How do we go from estimating margin of victory to win probabilities? 

13 / 28 

# Win Probabilities Through Conformal Prediction 





_Conformal prediction_ is an inference methodology based on how well incoming observations conform to previously seen observations. 

The steps are as follows: 

1. For a new observation, specify a hypothesized response value, e.g., a MOV of -25. 

2. Retrain prediction model with observed training data as well as the new observation with hypothesized response. 

3. Calculate a _conformity score_ for each observation. 



4. Compare conformity score for new observation to conformity scores for all other observations; higher magnitude conformity scores correspond to hypothesized responses that are less likely. Useful for generating prediction intervals around a predicted response value. 

14 / 28 

# Win Probabilities Through Conformal Prediction 



<!-- Start of picture text -->
−40 −20 0 20 40 −40 −20 0 20 40<br>residual residual<br>−40 −20 0 20 40<br>residual<br>0.03 0.03<br>0.02 0.02<br>relative frequency 0.01 relative frequency 0.01<br>0.00 0.00<br>0.03<br>0.02<br>relative frequency 0.01<br>0.00<br><!-- End of picture text -->

15 / 28 

# Example with 2019-2020 Regular Season Data 



<!-- Start of picture text -->
Connecticut vs. South Carolina<br>Connecticut vs. Arizona<br>Connecticut vs. Dayton<br>−40 −20 0 20 40<br>1.0<br>0.8<br>) 0.6<br> m<br> ><br>M<br>P^( 0.4<br>0.2<br>0.0<br><!-- End of picture text -->

m 

16 / 28 

# Other Win Probability Methods 

We can generate win probability estimates in other ways Linear regression under normality assumptions 





## Logistic regression 



17 / 28 

# March Madness 2020 









Following cancellation, there were 20 unfinished men’s conference tournaments; 18 unfinished women’s conference tournaments. Each team falls into one of five different situations. We cannot calculate tournament win probabilities without generating probabilities for making the tournament. We simplify bracket generation to make the task of constructing probabilities of making the tournament tractable (S-curve). 

18 / 28 

# S-curve Bracket Simplification 

### Table 5: March Madness example bracket using S-curve method 

|||Reg<br>|ion<br>||
|---|---|---|---|---|
|Seed|1|2|3|4|
|1|1|2|3|4|
|2|8|7|6|5|
|3|9|10|11|12|
|4|16|15|14|13|
|5|17|18|19|20|
|6|24|23|22|21|
|7|25|26|27|28|
|8|32|31|30|29|
|9|33|34|35|36|
|10|40|39|38|37|
|11|41|42|43|44|
|12|48|47|46|45|
|13|49|50|51|52|
|14|56|55|54|53|
|15|57|58|59|60|
|16|64|63|62|61|



19 / 28 

# Situations for NCAA Teams 

1. A team has already made the tournament. 

2. A team must win their conference tournament or relies on a 

   - small number of teams ranked below them winning their respective conference tournament to make the tournament. 

3. A team relies on a small number of teams ranked below them winning their respective conference tournament to make the tournament. 

4. A team must win their conference tournament to make the 

   - tournament. 

5. A team cannot make the tournament. 

20 / 28 

# Probabilities of Making Tournament 

Table 7: Situation 4 tournament probabilities 

Table 6: Situation 3 tournament probabilities 

|Table 6: Situati|n 3 tournament p|robabilities|Team|Overall Rank|Probability|
|---|---|---|---|---|---|
|Team|Overall Rank|Probability|Old Dominion|48|0.239|
|Yale|40|0.995|Northern Iowa|49|0.173|
|Michigan|41|0.917|Oklahoma|52|0.011|
|North Carolina|42|0.618|Western Kentucky|54|0.199|
|Central Florida|43|0.232|West Virginia|57|0.038|
|St. John’s|44|0.031|Rice|58|0.248|
||||Middle Tennessee|63|0.226|



21 / 28 

# Tournament Win Probabilities 

Table 8: Win probabilities given example bracket for top ranked women’s teams 

|Team|Probability|
|---|---|
|Connecticut|0.289|
|South Carolina|0.127|
|Stanford|0.104|
|Oregon|0.094|
|Princeton|0.064|
|Oregon State|0.061|
|Louisville|0.058|
|Baylor|0.043|
|Kentucky|0.032|
|Arizona|0.021|



22 / 28 

# Win Probability Calibration 

|Men|Women|
|---|---|
|1.00||
|||
|0.50<br>.<br>Relative Frequency||
|0.25<br>||
|0.00||
|000<br>025<br>050<br>075<br>100|000<br>025<br>050<br>075<br>100|
|.<br>.<br>.<br>.<br>.|.<br>.<br>.<br>.<br>.|
|Binned Proba|bility Estimate|



Method Conformal Normal Logistic 

23 / 28 

# Win Probability Calibration by Season 

|||ECE|||MCE||
|---|---|---|---|---|---|---|
|Season|Conformal|Linear|Logistic|Conformal|Linear|Logistic|
|2014-2015|**0.077**|0.111|0.104|0.824|**0.412**|0.423|
|2015-2016|0.103|0.101|**0.082**|0.711|**0.392**|0.817|
|2016-2017|**0.071**|0.115|0.110|0.826|**0.817**|0.890|
|2017-2018|**0.072**|0.132|0.101|0.717|**0.465**|0.581|
|2018-2019|**0.067**|0.118|0.090|0.329|**0.245**|0.405|
|2019-2020|**0.121**|0.147|0.134|0.375|0.331|**0.325**|
|||ECE|||MCE||
|Season|Conformal|Linear|Logistic|Conformal|Linear|Logistic|
|2014-2015|**0.086**|0.097|0.088|0.920|**0.305**|0.672|
|2015-2016|0.083|0.094|**0.071**|0.314|0.276|**0.242**|
|2016-2017|**0.058**|0.079|0.105|**0.302**|0.325|0.434|
|2017-2018|0.064|0.071|**0.057**|0.819|**0.793**|0.828|
|2018-2019|**0.057**|0.061|0.068|**0.126**|0.142|0.195|
|2019-2020|**0.052**|0.098|0.114|**0.189**|0.247|0.289|



Table 9: Calibration comparison for all methods within each women’s season (top) and men’s season (bottom) 

24 / 28 

# Issues 



## Data 

- Inconsistencies with naming convention. 

- Women’s data is much more to obtain. 



## Model 

- Does not account for: momentum, injuries, match-ups, etc. 

- We (over)simplify the bracket generation process. 

- Double-dip on overall team strength. 

25 / 28 

# Future Work 





Utilize more complex modeling approaches to margin of victory prediction, e.g., fused lasso approach. Apply to betting scenarios. 



Incorporate more accurate portrayal of existing selection process. 



Extend to other professional and amateur leagues. 

26 / 28 

Questions? 

27 / 28 

# References 



Edwards, C. T. (1991). 

_The combinatorial theory of single-elimination tournaments_ . PhD thesis, Montana State University-Bozeman, College of Letters & Science. 



Harville, D. (1977). 

The use of linear-model methodology to rate high school or college football teams. 



_Journal of the American Statistical Association_ , 72(358):278–289. Vovk, V., Shen, J., Manokhin, V., and Min-ge, X. (2019). Nonparametric predictive distributions based on conformal prediction. _Machine Learning_ , 108(3):445–474. 

28 / 28 

# Conformal Predictive Distributions 

We formalize this using conformal predictive distributions to generate estimates of win probability for the home team in an upcoming match-up as, 



where _Ri_ ( _yc_ ) = _yi − y_ ˆ _i_ ( _yc_ ) and _Rn_ +1( _yc_ ) = _yc − y_ ˆ _n_ +1( _yc_ ), the index ( _i_ ) represents that _i_ -th order statistic of the collection of conformity scores and _τ_ is a _U_ (0 _,_ 1) random variable. 

[Vovk et al., 2019] 

29 / 28 

# CPD Four Team Example 

|<br>0.6<br>0.8<br>1.0<br>probability|<br>0.6<br>0.8<br>1.0<br>probability|
|---|---|
|0.4<br>mated|0.4<br>mated|
|0.2<br>esi|0.2<br>esi|
|0.0|0.0|
|−40<br>−20<br>0|20<br>40<br>−40<br>−20<br>0<br>20<br>40|
|MOV|MOV|



Figure 3: MOV conformal predictive distributions for team 1 vs. team 2 (left) and team 3 vs. team 4 (right). 

30 / 28 

# 2020 Conference Champions 

Table 10: Winners of completed conference tournaments for NCAA women’s basketball 

Table 11: Winners of completed conference tournaments for NCAA men’s basketball 

|Conference|Winner|men’s basketball||
|---|---|---|---|
|Atlantic-10|Dayton|Conference|Winner|
|ACC|North Carolina St.|ASUN|Liberty|
|American|Connecticut|Big South|Winthrop|
|Big East|DePaul|CAA|Hofstra|
|Big Ten|Maryland|Horizon League|Northern Kentucky|
|Horizon|IUPUI|Missouri Valley|Bradley|
|Ivy League|Princeton|Mountain West|Utah St.|
|Mountain West|Boise St.|Northeast|Robert Morris|
|Ohio Valley|Southeast Missouri St.|Ohio Valley|Belmont|
|Pac-12|Oregon|Patriot League|Boston|
|SEC|South Carolina|Southern|E. Tennessee St.|
|Southern|Samford|The Summit|North Dakota St.|
|Summit<br>WCC|South Dakota<br>Portland|WCC|Gonzaga|



Princeton was awarded the automatic bid to the tournament based on regular season performance, not by winning the Ivy League conference tournament. 

31 / 28 

# NCAA Men’s Situations 

Table 12: Situations for men’s teams ranked from thirty-three to sixty-four 

|Situation|Teams|
|---|---|
|1|Utah St., Florida, Auburn|
|2|Alabama, Providence, Syracuse, Mississippi St., Memphis, NC St., Arizona St., Rhode Island,<br>Virginia, USC, Oklahoma St., Tennessee, Notre Dame, Richmond, Yale, Clemson, Connecticut|
|3<br>4<br>5|Indiana, LSU, Arkansas, Oklahoma, Wichita St., Cincinnati<br>Stanford<br>all other teams|



32 / 28 

# Men’s Probabilities of Making Tournament 

Table 13: Probability of winning conference tournament 

|Team|Overall Rank|Probability|
|---|---|---|
|Alabama|45|0.055|
|Providence|46|0.078|
|Syracuse|47|0.063|
|Mississippi St.|48|0.101|
|Memphis|49|0.102|
|NC St.|50|0.046|
|Arizona St.|51|0.158|
|Rhode Island|52|0.157|
|Virginia|53|0.068|
|USC|56|0.069|
|Oklahoma St.|57|0.025|
|Tennessee|58|0.038|
|Notre Dame|60|0.058|
|Richmond|61|0.128|
|Yale|62|0.464|
|Clemson|63|0.040|
|Connecticut|64|0.070|



Table 14: Probability of making tournament for men’s teams in Situations 3 and 4 

|Team|Overall Rank|Probability|
|---|---|---|
|Indiana|36|0.999|
|LSU|37|0.994|
|Arkansas|38|0.956|
|Stanford*|39|0.801|
|Oklahoma|40|0.522|
|Wichita St.|41|0.350|
|Cincinnati|42|0.224|



33 / 28 

# Men’s Basketball Example Bracket 

Table 15: Bracket 1 for men’s tournament and respective seeding 

|Seed|Region 1|Region 2|Region 3|Region 4|
|---|---|---|---|---|
|1|Kansas|Gonzaga|Duke|Michigan St.|
|2|West Virginia|San Diego St.|Arizona|Baylor|
|3|Ohio St.|Dayton|Maryland|Michigan|
|4|Creighton|Texas Tech|Florida St.|Louisville|
|5|BYU|Oregon|Seton Hall|Villanova|
|6|Marquette|Iowa|Houston|Penn St.|
|7|Colorado|Purdue|Kentucky|Wisconsin|
|8|Butler|Rutgers|Minnesota|Illinois|
|9|Utah St.|Florida|Auburn|Indiana|
|10|Oklahoma|Stanford|Arkansas|LSU|
|11|Wichita St.|Cincinnati|Xavier/Providence|Saint Mary’s (CA)/Alabama|
|12|Liberty|North Texas|E. Tennessee St.|Yale|
|13|Vermont|Akron|No. Colorado|Belmont|
|14|Bradley|UC Irvine|Stephen F. Austin|Texas St.|
|15|New Mexico St.|Hofstra|Winthrop|North Dakota St.|
|16|Prairie View/Robert Morris|Siena/Norfolk St.|Boston|Northern Kentucky|



34 / 28 

# Men’s Basketball Tournament Win Probabilities 

Table 16: Win probabilities given exemplar brackets for top ranked men’s teams 

|Team|Probability|
|---|---|
|Kansas|0.269|
|Gonzaga|0.144|
|Duke|0.123|
|Michigan State|0.067|
|Baylor|0.063|
|Arizona|0.043|
|San Diego State|0.031|
|West Virginia|0.027|
|Ohio State|0.023|
|Dayton|0.023|



35 / 28 

# Probability of Being At-Large Bid 





For team ranked _i_ to make the tournament as an at large bid we have to look at every team below them and enumerate all possible combinations of conference outcomes Results in the following probability distribution, 



36 / 28 


