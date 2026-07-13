<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Estimating Shot Selection Efficiency in Basketball A Revealed Efficiency Approach - Unknown Authors.pdf -->



- Shot Selection Efficiency in Basketball: A Revealed Efficiency Approach Justin Ehrlich and Shane Sanders 

- Sport Analytics, Falk College, Syracuse University, Syracuse, NY 

- Results 

Background • We create a shot selection measure called _Shot Selection Efficiency_ that takes as input a team’s (player’s) expected points and expected proportional volume from each observed shooting bin of the half court and computes the team’s bin shot volume weighted correlation between binlevel proportional volume and bin-level expected points, from the field and free throw line, across all shooting bins for a season. Methods • Play-by-play data was subscribed from bigdataball.com for the 2016/17-2022/23 seasons. • Binned shots and computed expected true points: • _Shot Selection Efficiency_ was then calculated as the shot-volume weighted correlation between bin-level expected true points and bin-level shooting volume across all shooting bins for a season. 

# **Estimated Models *All models include team fixed effects.** 



|||**Pyth_W_pct**|||**W_pct**|||**Pyth_W_pct**|||
|---|---|---|---|---|---|---|---|---|---|---|
|**Predictors**|Estimates|std. Error|p|Estimates|std. Error|p|Estimates|std. Error|p||
|**(Intercept)**|-31.323|5.984|<0.001|-29.863|6.902|<0.001|-41.292|7.254|<0.001||
|**DRtg**|-0.031|0.002|<0.001|-0.031|0.002|<0.001|-0.031|0.002|<0.001||
|**true shooting**|0.350|0.118|0.003|0.295|0.136|0.032|0.333|0.148|0.025||
|**efficiency**|||||||||||
|**exogenous**<br>**shooting**<br>|1.050|0.127|<0.001|1.062|0.146|<0.001|1.095|0.150|<0.001||
|**ability**|||||||||||
|**season**|0.017|0.003|<0.001|0.016|0.004|<0.001|0.022|0.004|<0.001||
|**off TOV%**|-0.036|0.006|<0.001|-0.035|0.007|<0.001|||||
|**off ORB%**|0.016|0.002|<0.001|0.013|0.003|<0.001|||||
|**payroll normalized**|||||||1.095|0.619|0.079||
|**payroll**<br>**normalized^2**|||||||-0.674|0.388|0.084||
|**Observations**|210|||210|||210||||
|**R**<sup>**2**</sup>**/ R**<sup>**2**</sup>**adjusted**|0.827 / 0.792|||0.782 / 0.738|||0.739 / 0.687||||
|021-22|Milwa|ukee B|ucks|||||||Conclusion|





<!-- Start of picture text -->
-0.674 0.388 0.084<br>210 210<br>0.782 / 0.738 0.739 / 0.687<br><!-- End of picture text -->



<!-- Start of picture text -->
Observations 210 210<br>R 2  / R 2  adjusted 0.827 / 0.792 0.782 / 0.738<br><!-- End of picture text -->

2021-22 Milwaukee Bucks True Shot Chart 

A new shot selection measure, called _Shot Selection_ 

• 



_Efficiency_ , aggregates from team-season shot charts into a single efficiency measure that incorporates 

• _Exogenous Shooting Ability_ is obtained by finding a team’s average expected true points from each bin of its shot chart in a season. Then, we take an unweighted average of all bin-level expected true point values to obtain a measure of shooting ability that is exogenous of shot selection. • We first run 2 sets of 4 fixed effects regression models. On LHS, we specify either team-season _Pythagorean_ .. _expected win% or team-season actual win%_ • On the RHS, we essentially specify the four factors on each side of the ball, but at different levels of aggregation or disaggregation, toward highly controlled, highly-explanatory models that isolate the effect of shot selection efficiency on team success. • Explanatory team-season variables: _DRtg, exogenous shooting ability, shot selection efficiency, ORB%,_ and _season. TOV%, team fixed effects,_ • A third set of models consider the payroll-conditional effect of _Shot Selection Efficiency_ on team success. Is _Shot Selection Efficiency_ priced-in or Moneyball? 

shot-dependent FT scoring. The measure does not depend on overall shooting 

• 

ability. A separate measure of exogenous shooting ability is created that is exogenous of shot selection. 

In 2-way, 4-factor type models, _Shot Selection Eff._ and _team success_ have a positive, significant rel’n _._ If a team in a season can improve the weighted correlation between bin-level shot-volume and expected true points by 0.1 units, it gains an 

• 

• 

expected 0.035 units of win proportion or nearly 3 games.  Alternatively, a 1 s.d.  increase in the variable increases expected wins by 1.41 according to the full Pyth_W_pct model. 

A 1 s.d. increase in _Exogenous Shooting Ability_ has approximately a three-fold effect on expected wins, by comparison. 

• 





A third set of models suggests _Shot Selection Efficiency_ is a source of expected wins not fully explained by team payroll. 

• 

_Shot Selection Efficiency_ may not be fully priced into the player market, suggesting a potential Moneyball opportunity related to game/set management of shot selection. Future work will examine whether _Shot Selection Efficiency_ is a measure of team coaching efficiency via coaching tenure fixed effects. 

• 

|**Characteristic**|**N = 210**|
|---|---|
|Pyth_W_pct||
|Median(SD)Range|0.50(0.14)0.18 - 0.82|
|W_pct||
|Median(SD)Range|0.50(0.14)0.18 - 0.82|
|NRtg||
|Median(SD)Range|0.4(4.6)-10.5 - 11.6|
|true_shooting_efficiency||
|Median(SD)Range|0.51(0.05)0.40 - 0.61|
|exogenous_shooting_ability||
|Median(SD)Range|0.88(0.05)0.76 - 1.03|
|off_TOV%||
|Median(SD)Range|12.60(0.90)9.90 - 14.90|
|off_ORB%||
|Median(SD)Range|22.80(2.21)17.90 - 30.20|
|DRtg||
|Median(SD)Range|111.2(3.3)102.9 - 120.0|
|payroll_normalized||
|Median (SD) Range|0.78 (0.11) 0.46 - 1.00|



• 




