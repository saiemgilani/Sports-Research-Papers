<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - Evaluating NBA Player Consistency through GARCH Modeling - Unknown Authors.pdf -->



<!-- Start of picture text -->
,<br><!-- End of picture text -->



- **Evaluating NBA Player Consistency through GARCH Modeling Joshua Davila, Texas A&M University** 



# **INTRODUCTION** 

- “Basketball is a pretty simple game. What wins is consistency and competitiveness.” – Gregg Popovich 

- As teams continuously look to improve upon their previous seasons, both coaching staffs and front offices try to build out their teams featuring players that play their role at an exceptional level. Role players are often the backbone of the teams that hoist the Larry O’Brien Trophy at the end of the NBA Season. 

- However, many of the standard measures of consistency do not appropriately measure performance over a season. One potential solution is the use of Generalized Autoregressive Conditional Heteroskedasticity (GARCH) modeling to evaluate player consistency. 

# **METHOD** 

- Focusing on the consistency of performance, this study utilized the abilities of GARCH modeling (“fGarch” package in R) in order to gauge a player’s performance consistency. Using GARCH allowed for a measurement of their game-to-game consistency with a focus on the time series nature of a season. 

# **Generalized Autoregressive Conditional Heteroskedasticity (GARCH Modeling)** 

- Building on the Autoregressive Conditional Heteroskedasticity modeling (first introduced by Robert F. Engle), Tim Bollerslev introduced the GARCH model in 1986. The improvements made upon the original ARCH model allowed for a more flexible model to help capture the time varying variability. This was done by adding lagged conditional variances into the equation. 

- This dataset used was collected using the “hoopR” package in R. The dataset analyzed for this study featured over 26 thousand individual game performances for the 2023-24 NBA regular season. 

- Only players participating in an average at least 10 minutes a game for at least 65 games were included in the modeling. All players were then sorted into a ranking to determine their relative consistency compared to other players. 



||5 Most|Consistent|Players||
|---|---|---|---|---|
||Average<br>Game|Volatility|Average||
|Player Name|Score|Constant|Minutes per Game|Games Played|
|Drew Eubanks|6.08|1.82E-05|15.53|75|
|Joe Ingles|5.44|1.89E-05|17.15|68|
|Kris Dunn|7.05|2.02E-05|18.95|66|
|Amir Coffey|5.96|2.17E-05|20.83|70|
|David Roddy|5.23|2.34E-05|18.11|65|
||5 Least|Consistent|Players||
||Average<br>Game|Volatility|Average||
|Player Name|Score|Constant|Minutes per Game|Games Played|
|Tyrese Haliburton|21.77|65.92|32.23|71|
|Zion Williamson|19.30|58.03|31.57|70|
|Fred VanVleet|16.84|48.32|36.79|73|
|Jaren Jackson Jr.|14.88|47.59|32.18|66|
|Paolo Banchero|17.53|35.87|34.78|81|





<!-- Start of picture text -->
5 Most Consistent Players (Average of  > 32 minutes per game)<br>Average<br>Game Volatility  Average<br>Player Name Score Constant Minutes per Game Games Played<br>Max Strus 10.72 3.89E-05 32.01 70<br>Josh Hart 10.22 4.26E-05 33.41 81<br>Pascal Siakam 18.59 4.51E-05 33.25 80<br>Coby White 14.98 6.05E-05 36.47 79<br>De’Aaron Fox 20.28 6.92E-05 35.93 74<br>5 Least Consistent Players (Average of  > 32 minutes per game)<br>Average<br>Game Volatility  Average<br>Player Name Score Constant Minutes per Game Games Played<br>Tyrese Haliburton 21.77 65.92 32.23 71<br>Fred VanVleet 16.84 48.32 36.79 73<br>Jaren Jackson Jr. 14.88 47.59 32.18 66<br>Paolo Banchero 17.53 35.87 34.78 81<br>Devin Booker 20.79 34.87 35.71 69<br><!-- End of picture text -->

# **RESULTS** 

The player ranked the least consistent for the 2023-24 NBA season was Tyrese Haliburton of the Indiana Pacers (volatility constant = 65.9201), while the player ranked the most consistent was Drew Eubanks of the Phoenix Suns (volatility constant = 0.00002). 

• 

**FUTURE RESEARCH** GARCH modeling can be utilized in tandem with other models such as Vector Autoregression (VAR) and Generalized Autoregressive Score (GAS). This could allow for a more complete look at a player’s consistency. Future research could also utilize a bigger dataset with more observations. For example, utilizing a combination of GARCH and GAS could be used to help measure the consistency of shooting for an NBA player. They could also be used with other non normal distributions that occur in the data. 

- 

- 


