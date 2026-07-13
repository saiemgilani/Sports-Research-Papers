<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - An Examination of Timeout Value, Strategy, and Momentum in NCAA Division 1 Men's Basketball - Unknown Authors.pdf -->

**An Examination of Timeout Value, Strategy, and Momentum in NCAA Division 1 Men’s Basketball** Luke Benz Yale University Department of Applied Mathematics 



**Introduction** The sport of basketball is often described as “a game of runs“. A basketball have sev- typical game may eral stretches when one team scores the majority of points in a short portion of the game, only to be followed by the other team answering with a scoring run of its own. Coaches seem to take timeouts when their team is on a negative scoring run, feeling pressure to an of stop opponent’s quick flurry scoring. This work seeks to examine how timeouts are used in NCAA Division 1 men’s basketball and whether there is any truth to the notion that timeouts stop momentum the rate of opponent by decreasing opor the rate of in ponent scoring swinging scoring favor of the timeout-calling team. The data used in this project are 10,409 complete NCAA basketball play-by-play logs from the 2016-17 and 2017-18 seasons, scraped from ESPN.com using the `ncaahoopR` package for the R statistical computing language. [1] **A First Pass** 







Figure 1: Net Score Differential Distributions Before and After Called (Non-Media) Timeouts 

A first pass at trying to quantify momentum is to look at the net score differential, from the perspective of the timeout calling team, during equal length intervals before and after the timeout. For each 1-5 minute interval, the timeout calling team has a net score in higher average differential posttimeout intervals when compared to corresponding pre-timeout intervals, with the variance in posttimeout net score differential lower than the variance in pre-timeout net differentials for each equal length interval. 

**Points Above Expectation** To account for the fact that coaches are more likely to call timeouts when their team is on a negative this section outlines a framework for scoring run, modeling the number of points a team would expect to score in a certain time interval given a particular were the run of to continue as game situation, play normal. Taking the difference between the number of points a team scored following a timeout and the number of were to score points they expected given the particular game situation allows one to quantify the value of a timeout in terms of Points Above Expectation (PAE). 



More formally, let _S_ and _S_ denote the net _ijkB ijkA −_ score differential for a team in _i_ minute intervals before and after game state _j_ (time remaining, score differential, and pre-game point spread) of game _k_ . 



**_X_** is a vector of covariates encoding information _ijk_ about the particular game state. Specifically, the following covariates are considered: 





The training set for these models removed all game states where a timeout took place (both media and non-media) in order to adequately capture expected behavior without immediate stoppage of play. Predicting these models on game states that are timeouts allows for an estimate of how much better or worse a team performed as a result of the stoppage in play. Specifically points above expectation is given by the residual: ˆ _S S ijkA − ijkA_ 

# **Results** 





Figure 2: Distributions of PAE After Timeouts 

For each of the five intervals, non-media timeouts have median PAE > 0. That on teams is, average, calling a timeout perform better in up to five minute intervals the timeout than would be ex- following pected were no timeout to be called from an equivalent game state. This does not hold for media timeouts, suggesting that even after accounting for the fact that teams are more likely to take timeouts folthere to be lowing negative scoring runs, appears more in called timeouts with me- benefit compared dia timeouts. As the below figure shows, teams tend to out perform expectation after timeouts by larger margins earlier in the than later in the This is game game. likely due to the fact that more timeouts are taken later in the game than in the beginning of the game, and that there are more stoppages of continuous game play towards the end of games. Figure 3: Average PAE After Non-Media Timeouts Throughout the Course of a Game 



**Timeout Value** A decent for timeout value because it is the proxy average PAE in the five minute interval following a timeout (from Figure 3) multiplied by the value of increasing the score differential by 1 point in the team’s favor at that particular time of game, which comes from the the win probability model outlined in the full paper version of this work [2]. The resulting values reflect a team’s increase in the odds of winning a game by taking a timeout and experiencing the average 5 minute boost in PAE. Figure 4: Value of Taking a Timeout 



• On average, taking a timeout improves net score differential in intervals up to _≥_ 5 minutes following the timeout. 

- Coaches should be more aggressive with early half timeouts. 

• “Use it or Lose it“ timeouts right before halftime are least valuable, though are still better than not taking a timeout. **References** [1] L. Benz. ncaahoopR: An R package for working with NCAA Basketball Play-by-Play Data. 2019. `https://github.com/lbenz730/ncaahoopR` , [2] L. Benz. An Examination of Timeout Value, Strategy, and Momentum in NCAA Division 1 Men’s Basketball. `https://github.com/lbenz730/Senior-Thesis` , 2019. 




