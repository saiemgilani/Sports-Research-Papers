<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - Home Sweet Home Quantifying Home Court Advantages for NCAA Basketball Statistics - Unknown Authors.pdf -->

**Home Sweet Home: Quantifying Home Court Advantages For NCAA Basketball Statistics Matthew van Bommel, Luke Bornn, Peter Chow-White, Chuancong Gao / Simon Fraser University** The Crowd Effect: Attendance Impact on Statistics **Home vs Away vs Neutral Statistics Attendance Impact on Statistics Quantifying Home Court Advantage** Conclusions: ● Referee decisions appear to be affected by crowd size: both PF and FTA **Results: Results:** have significantly different home team advantages in high attendance ● ● Home teams outperformed away (and neutral location) teams in nearly Referee bias in favor of the home team increased in games with high The home court boosts for AST and BLK were equivalent to having 12 games compared to low attendance games in 5 of the 6 gender-division all statistics across every gender-division-season combination attendance (statistically significant for all but D2 Women) and 43 additional possessions in a game respectively combinations (all but D2 Women). ● ● ● AST and BLK (the most subjective statistics) had the greatest home Referee bias had a greater impact on point totals in D2 and D3, Referee bias appears to have a greater impact on point totals in D2 and Men received an additional home court boost for BLK while women advantages and much of the advantages remained when compared to compared to D1D3, compared to D1. received a lesser home court boost for OREB and FGA ● ● ● No evidence of aNo evidence of a **ttendanc** e impact on FT% was discovere impact on FT% was discov **e** redd. Team strength advantage coefficients were highly correlated (0.85) ● ● Home teams experienced a big boost in FG% and 3FG%, while away No evidence of attendance impact on scorekeepers was discoveredNo evidence of attendance impact on scorekeepers was discovered. with home advantage coefficients, thus scorekeepers may have been teams performed slightly worse than neutral location teams more biased in favor of stronger teams FT% was negatively impacted for away teams compared to neutral **Two-sample t-testsTwo-sample t-tests** location teams but home teams did not receive an additional boost **LASSO Poisson regression model** Scorekeepers tended to have greater home team biases when Controlling for home team strength Mean Mean Mean Controlling for home team strength Predicting statistic counts Mean advantage: _N_ observing men compared to women or higher divisions compared to advantage: _p_ while controlling for: (Home – Away) (Home – Away) (Home – Away) _x_ (Home – Away) β0+β _i_ −<sup>1</sup> _x_ e ● RPI` Statistic ValueStatistic Value Statistic ValueStatistic Value RPI' = Home RPI - Away RPI ^β= _argmin_ ( _yi_ (β0+β _i_ )− )+λ∑|<sup>β</sup> _j_ | _N_<sup>∑</sup> **vs** RPI' = Home RPI - Away RPI ^β0 _,_ β _i_ =1 _j_ =11 ● Possessions in games within games with in games with in games with ● RPI = (0.25 * Team Win %) + Gender / Division Using over 100,000 games between the 2011-2012 and 2015-2016 **Low Attendance High AttendanceHigh Attendance Low Attendance** RPI = (0.25 * Team Win %) + (0.50 * Opponents’ Win %) + seasons, we compared the difference in home, away, and neutral teams (Top 25%)(Top 25%) (Bottom 25%) (0.50 * Opponents’ Win %) + (Bottom 25%) (0.25 * Opponents’ Opponents’ Win %) 

**Home vs Away vs Neutral Statistics** 

**Results:** ● Home teams outperformed away (and neutral location) teams in nearly all statistics across every gender-division-season combination ● AST and BLK (the most subjective statistics) had the greatest home advantages and much of the advantages remained when compared to neutral location teams ● Home teams experienced a big boost in FG% and 3FG%, while away teams performed slightly worse than neutral location teams ● FT% was negatively impacted for away teams compared to neutral location teams but home teams did not receive an additional boost ● Scorekeepers tended to have greater home team biases when observing men compared to women or higher divisions compared to lower divisions Using over 100,000 games between the 2011-2012 and 2015-2016 seasons, we compared the difference in home, away, and neutral teams across a variety of box score statistics for both genders and all three divisions. The results are displayed in the following figure. 

**Results:** ● The home court boosts for AST and BLK were equivalent to having 12 and 43 additional possessions in a game respectively ● Men received an additional home court boost for BLK while women received a lesser home court boost for OREB and FGA ● Team strength advantage coefficients were highly correlated (0.85) with home advantage coefficients, thus scorekeepers may have been more biased in favor of stronger teams 

Predicting statistic counts _p_ while controlling for: ● RPI` ∑||<sup>β</sup> _j_ | _j_ =11 ● Possessions ● Gender / Division 

advantage: advantage: RPI' = Home RPI - Away RPI RPI' = Home RPI - Away RPI RPI = (0.25 * Team Win %) + RPI = (0.25 * Team Win %) + (0.50 * Opponents’ Win %) + (0.50 * Opponents’ Win %) + (0.25 * Opponents’ Opponents’ Win %) (0.25 * Opponents’ Opponents’ Win %) Statistical matching Statistical matching and bootstrap and bootstrap sampling used to sampling used to construct new high construct new high attendance (High*) attendance (High*) samples, with equal distributions, with RPI’ distributions to equal RPI’ low attendance. distributions to low attendance. 

After estimating the models, the percentage impact values are computed as e<sup>βj</sup> -1 and are presented in the following table. 







The matching algorithm has a random component, so we repeated the The matching algorithm has a random component, so we repeat the process 1000 times for each statistic, performing 1000 distinct tests. The process 1000 times for each statistic, performing 1000 distinct tests, and average p-value results are displayed in the following table. display the average p-value results in the following table: 

**Home** – increase in statistic frequency for home teams compared to away teams **Division** – baseline differences in gender-division combinations 



**Empty Cells –** variables not selected in models 

**To read the full paper visit: matthewvanbommel.com/nessis or arxiv.org/abs/1909.04817** 

**Contact:** 

**matthew.vbommel@gmail.com** 

**Low / High** – attendance cutoffs **Overall** – average p-values across all gender-division combinations – attendance cutoffs **Low / High Bold values Overall** – significant t-test results at α = 0.0006 (Bonferroni correction) – average p-values across all gender-division combinations **Negative values** – p-values multiplied by -1 when away teams had the advantage **Bold p-values** – significant home advantage at α = 0.0006 (Bonferroni correction) 

**(A)** – neutral teams’ advantage over away teams **(H)** – home teams’ advantage over neutral teams 


