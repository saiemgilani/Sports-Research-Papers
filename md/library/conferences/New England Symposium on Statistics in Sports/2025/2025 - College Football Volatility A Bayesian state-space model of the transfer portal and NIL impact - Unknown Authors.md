<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - College Football Volatility A Bayesian state-space model of the transfer portal and NIL impact - Unknown Authors.pdf -->



College Football Volatility: A Bayesian state-space model of the transfer portal and NIL impact 

Ron Yurko (joint work w/ Luke Benz) 

September 27, 2025 

Assistant Teaching Professor Director of Carnegie Mellon Sports Analytics Center (stat.cmu.edu/cmsac) Department of Statistics & Data Science, Carnegie Mellon University 

## Brief timeline of college football… 

- 2014 - College Football Playoff era begins 2018 - **Launch of NCAA transfer portal** _“student athlete database compliance tool”_ 

## Brief timeline of college football… 

- 2014 - College Football Playoff era begins 

- 2018 - **Launch of NCAA transfer portal** _“student athlete database compliance tool”_ 2020 - _Don’t need to remind you_ 2021 - **Student athletes allowed to transfer once without sitting out a year** 

   - Conference realignment madness announcements 

   - **NIL era begins!** Supreme Court ruling in NCAA vs Alston 

- 2024 - **Immediate eligibility no matter how many times athletes transferred** 

Welcome to the era of perpetual free-agency 



## Which schools have the fewest incoming transfers? 



## Which schools have the fewest incoming transfers? 

United States military academies! **Army, Navy, Air Force** 

## Which schools have the fewest incoming transfers? 

United States military academies! **Army, Navy, Air Force** 

_“Every player is technically a transfer. We just signed a whole class of guys transferring from high school…”_ 

- Clemson HC Dabo Swinney on **taking 0 transfers in 2024** 

## Which schools are leading in transfers??? (ignoring 2025) 



## Which schools are leading in transfers??? (ignoring 2025) 

**Prime Time!** Led by Deion Sanders: 

2022 W-L record: 1-11 

## Which schools are leading in transfers??? (ignoring 2025) 

**Prime Time!** Led by Deion Sanders: Colorado with 52 in 2023 and 38 in 2024 2022 W-L record: 1-11 **-> 2023: 4-8 -> 2024: 9-4** 

Which schools are leading in transfers??? (ignoring 2025) **Prime Time!** Led by Deion Sanders: Colorado with 52 in 2023 and 38 in 2024 

2022 W-L record: 1-11 **-> 2023: 4-8 -> 2024: 9-4** UNC Charlotte - Francis ‘Biff’ Poggi: 40 in 2023 and 31 in 2024 **Fired on Nov 18 2024** after 3-7 start to season, compiled 6-16 record overall 

Which schools are leading in transfers??? (ignoring 2025) **Prime Time!** Led by Deion Sanders: Colorado with 52 in 2023 and 38 in 2024 

2022 W-L record: 1-11 **-> 2023: 4-8 -> 2024: 9-4** UNC Charlotte - Francis ‘Biff’ Poggi: 40 in 2023 and 31 in 2024 **Fired on Nov 18 2024** after 3-7 start to season, compiled 6-16 record overall Texas State - GJ Kinne: 42 in 2023 and 36 in 2024 Finished 8-5 in both 2023 and 2024, signed 7-year contract in Nov 2024 

Which schools are leading in transfers??? (ignoring 2025) **Prime Time!** Led by Deion Sanders: Colorado with 52 in 2023 and 38 in 2024 2022 W-L record: 1-11 **-> 2023: 4-8 -> 2024: 9-4** UNC Charlotte - Francis ‘Biff’ Poggi: 40 in 2023 and 31 in 2024 **Fired on Nov 18 2024** after 3-7 start to season, compiled 6-16 record overall Texas State - GJ Kinne: 42 in 2023 and 36 in 2024 Finished 8-5 in both 2023 and 2024, signed 7-year contract in Nov 2024 Indiana - Curt Cignetti: 4th most transfers with 30 in 2024, made playoff! 

## More transfers leads to… different variance? 



Modeling team ratings - Glickman & Stern (1998, 2017) Let _Y_ be the score differential in a game between teams _i_ and _j_ during year _t_ : _ijt_ 



Modeling team ratings - Glickman & Stern (1998, 2017) Let _Y_ be the score differential in a game between teams _i_ and _j_ during year _t_ : _ijt_ Simple model for game means with constant home-field advantage (HA): 



Modeling team ratings - Glickman & Stern (1998, 2017) Let _Y_ be the score differential in a game between teams _i_ and _j_ during year _t_ : _ijt_ Simple model for game means with constant home-field advantage (HA): 





Autoregressive model for team ratings with constant innovation variance      : 





## Data - FBS games in playoff era (2014-2024) 

- Gathered all data using the cfbfastR package (College Football Data API) 

- Focus on 9003 regular season NCAA Division I Football Bowl Subdivision (FBS) games in playoff era (2014-2024) - highest level of college football 

- Did NOT include bowl games and playoffs due to players sitting out 

- Treated all NCAA Division I Football Championship Subdivision (FCS) teams as one ‘FCS team’ - second highest level of college football 

- Gathered roster information about each team, counting the number of incoming transfers entering a season (including for different position groups) 

## Classic model results across major conferences 



Stochastic Volatility Extension - Glickman (2001) Is the constant innovation variance assumption appropriate in this crazy era? Can consider a dynamic innovation variance instead: 







## Innovation variance over time, but constant for each team 



### Model innovation variance as function of transfers + NIL era 

Allow the innovation variance to vary between teams based on transfers and changes to transfer portal + NIL rule (beginning in 2021) 



Innovation variance entering season t is a function of: 

- Indicator denoting if season t is in the NIL era (ie since 2021) 

- ● Number of incoming transfers for team i entering season t ○ i.e., Counting number of new players transferring to team 

- ● For FCS: use average transfer counts across FCS teams 

### Lower variance in NIL era, but higher variance with transfers 



## Innovation variance leaderboard 



## Innovation variance leaderboard 



Understanding the impact of innovation variance 



## Understanding the impact of innovation variance 



## Understanding the impact of innovation variance 



## What about positional differences in transfers? 





### Pass defense transfers are associated with higher variance? 



## Variance leaderboard based on transfer positions 



## Variance leaderboard based on transfer positions 



How do these models compare to each other? Posterior predictive comparison for holdout performance in 2023 and 2024 e.g., train model on 2014-22, sample ’23 team rating from innovation distribution 

## How do these models compare to each other? 

Posterior predictive comparison for holdout performance in 2023 and 2024 

e.g., train model on 2014-22, sample ’23 team rating from innovation distribution 



Best game-level predictions (RMSE and ELPD) 

- **Glickman & Stern (1998) wins!** 

- Transfer model (w/o positions) is next best in performance, w/ comparable results in 2024 

- Stochastic volatility extension (2001) is by far the worst of the four 

Best in-sample fit during NIL era (WAIC): 

- **Transfer model (w/o positions)** 

## Discussion and Limitations 

**Evidence indicating that this is a new era of uncertainty in college football** 

- Overall NIL era between-season variance is lower, but transfers offset this! 

## Discussion and Limitations 

**Evidence indicating that this is a new era of uncertainty in college football** 

- Overall NIL era between-season variance is lower, but transfers offset this! 

#### Several limitations… 

- Obvious relationship between new coach and high number of transfers 

- What about the selection bias displayed by schools in transfers? 

   - e.g., does Ohio State get fewer but better transfers? 

- Completely ignored recruiting in this study, **and do not have access to NIL amounts** 

- **●** Only considered modeling the variance, but maybe there is a change in the autoregressive parameter instead? **We’re completely ignored the quality of the transferring players!** 

**Key point: we are working with very limited data in the NIL era!** Only started in 2021… 

## What about 2025??? 



## What about 2025??? 

Purdue 2024: 1-11 -> 2025: 2-2 

UNLV 11-3   ->           4-0 WVU 6-7   ->           2-2 UNC 6-7   ->           2-2 WKY 8-6   ->           3-1 Oklahoma State 3-9   -> 1-2 



## What about 2025??? 

Purdue 2024: 1-11 -> 2025: 2-2 

**Register now for CMSAC Oct 24-25!** https://www.cmsaconference.com/ 

UNLV 11-3   ->           4-0 WVU 6-7   ->           2-2 UNC 6-7   ->           2-2 WKY 8-6   ->           3-1 Oklahoma State 3-9   -> 1-2 **_Thanks to co-author Luke Benz, as well as Tom Bliss for expertise!_** 



# Appendix 

40 

## More transfers leads to… different variance? 



## Relationship between incoming and departing transfers 



<!-- Start of picture text -->
Correlation<br>of about 0.75<br><!-- End of picture text -->

## Transfer counts by position 



## Transfer counts by position over time 



## Change in ESPN FPI ratings by position 




