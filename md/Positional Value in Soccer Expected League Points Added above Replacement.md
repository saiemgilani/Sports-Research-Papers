<!-- source: Positional Value in Soccer Expected League Points Added above Replacement.pdf -->

# **Positional Value in Soccer: Expected League Points Added above Replacement** 

## Konstantinos Pelechrinis<sup>_∗_</sup> and Wayne Winston<sup>_†_</sup> 

**Abstract.** Soccer is undeniably the most popular sport world-wide, but at the same time it is one of the least quantified. While there are many reasons for this, one of the main is the difficulty to explicitly quantify the contribution of every player on the field to his team chances of winning. For example, successful advanced metrics such as the (adjusted) +/- that allows for division of credit among a basketball team’s players (and ultimately to obtain a view of the wins contributed by a player), fail to work in soccer due to severe co-linearities (i.e., the same players being on the field for the majority of the time). In this work, we take a first step towards developing metrics that can estimate the contribution of a soccer player to his team’s winning chances. In particular, using data from (i) approximately 20,000 games from 11 European leagues for 8 seasons, as well as, (ii) player ratings from FIFA, we estimate through a Skellam regression model the _importance_ of every line in winning a soccer game. We consequently translate the model to expected league points added (per game) above a replacement player eLPAR. This model can be used as a guide for contracts’ monetary value decisions. For example, using market value data for approximately 10,000 players we further identify that currently the market clearly under-values defensive line players relative to the goalkeepers. Finally, we discuss how this model can be significantly enhanced using optical tracking data, but also, how it can be used to obtain positional (and consequently player) value for American football (another sports where achieving division of credit has been proven to be hard to date). 

**1. Introduction.** Soccer is undoubtedly the _king of sports_ , with approximately 4 billion global following [28]. However, despite this huge global interest it still lags behind with respect to advanced quantitative analysis and metrics capturing teams’ and players’ performance as compared to other sports with much smaller fan base (e.g., baseball, basketball). Soccer epitomizes the notion of team sport, but contrary to other sports it is really a game of space and off-ball movement. Traditionally sports metrics quantify on-ball events. However, in soccer every player has the ball in his possession an average of only 3 minutes [8], and hence, metrics that quantify on-ball events are destined to fail to capture a player’s influence on the game. 

Expected goals (xG) [18, 7] is probably the most prominent, advanced metric used in soccer today. xG takes into account the context of a shot taken (e.g., location of the shot, number of defenders in the vicinity etc.) and provides us with the probability of a shot leading to a goal. xG allows us to statistically evaluate players. For example, if a player is over-performing his expected goals, it suggests that he is either lucky or an above-average finisher. If this over-performance persists year-after-year then the latter will be a very plausible hypothesis. Nevertheless, while expected goals represent a straightforward concept and has been already used by mainstream soccer broadcast media, its application on evaluating players is still limited to a specific aspect of the game (i.e., shot taking) and only to players that actually take the shots (and also potentially goalkeepers). A more inclusive version of expected goals, is the Expected Goal Chains (xGC) [21]. xGC considers all passing sequences that lead to a 

> _∗_ School of Computing and Information, University of Pittsburgh (kpele@pitt.edu 

> _†_ Kelly School of Business, Indiana University (wayne@indiana.edu) 

**1** 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**2** 

shot and credits each player involved with the expected goal value for the shot. Of course, not all passes are created equally [20] and hence, xGC can over/under estimate the contribution of a pass to the final shot. 

The last few years player tracking technology (optical and/or GPS-based) has started penetrating quickly the soccer industry. During the last world cup in Russia, teams obtained player tracking data in real time [6]! The availability of such fine-grained spatio-temporal data have allowed researchers to start looking into more detailed ways to evaluate soccer players through their movement in space. For example, Hoang _et al._ [16, 15] developed a deep imitation learning framework for identifying the _optimal_ locations - i.e., the ones that minimize the probability of conceding a goal - of the defenders in any given situation based on the locations of the attackers (and the other defensive players). Fernandez and Bornn [8] also analyzed player tracking data and developed a metric quantifying the contribution of players in space creation as well as, this space’s value, while a nice overview of the current status of advanced spatio-temporal soccer analytics is provided by Bornn _et al._ [4]. Player tracking data will undoubtedly provide managers, coaches and players with information that previously was considered to be _intangible_ , and revolutionize soccer analytics. However, to date all of the efforts have been focused on specific aspects of the game. While in the future we anticipate that a manager will have the ability to holistically evaluate the contribution of a player during a game over a number of dimensions (e.g., space generation, space coverage, expected goals etc.), currently this is not the case. Therefore, it has been hard to develop soccer metrics similar to Win Shares and/or Wins Above Replacement that exist for other sports (e.g., baseball, basketball etc.) [11, 25]. These - all-inclusive - metrics translate on field performance to what managers, coaches and players can understand and relate to, i.e., wins. 

In this work, we take a first step towards developing such metric(s) for soccer. The first step towards this - and the main focus of this study - is quantifying the positional values in soccer. For instance, how much more important are the middle-fielders compared to the goalkeeper when it comes to winning a game? In order to achieve this we use data from games from 11 European leagues as well as FIFA ratings for the players played in these games. These ratings have been shown to be able drive real-world soccer analytics studies [5] and they are easy to obtain<sup>1</sup> . Using these ratings we model the final goal differential of a game through a Skellam regression that allows us to estimate the impact of 1 unit of increase of the FIFA rating for a specific position on the probability of winning the game. To avoid the sparsity data problem, in this study, as we will elaborate on later, we use as independent variables in our model the difference on the average rating of the four team lines (attack, middle-field, defense and goalkeeping). Then using this model we can estimate the **expected** league points added above replacement (eLPAR) for every player. The emphasis is put on the fact that this is the expected points added from a player, since it is based on a fairly static, usually pre-season, player rating (FIFA ratings change only a few times over the course of a season), and hence, does not capture the exact performance of a player in the games he played. However, when we describe our model in detail it should become evident that if these data (i.e., game-level player ratings) are available the exact same framework can be used to evaluate the actual league points added above replacement. 

> 1 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**3** 

The contribution of our work is twofold: 

1. We develop a pre-game win probability model for soccer that is accurate and wellcalibrated. More importantly it is based on the starting lineups of the two teams and hence, it can account for personnel changes between games. 

2. We develop the expected league points added above replacement ( `eLPAR` ) metric that can be used to identify positional values and facilitate (monetary) player valuation. Section 2 describes the data we used as well as the regression model for the score differential. Section 3 further details how we use the above model to obtain our expected league points added above replacement. In this section we also discuss the implications for the players’ transfer market. Finally, Section 4 discusses the scope and limitations of our current study, as well as, future directions for research. 

**2. Data and Methods.** In this section we will present the data that we used for our analysis, as well as, the Skellam regression model for the goal differential in a soccer game. 

**2.1. Soccer Dataset.** In our study we made use of the Kaggle European Soccer Database [1]. This dataset includes all the games (21,374 in total) from 11 European leagues<sup>2</sup> between the seasons 2008-09 and 2015-16. For every game, information about the final result as well as the starting lineups are provided. There is also temporal information on the corresponding players’ ratings for the period covered by the data. A player’s _p_ rating takes values between 0 and 100 and includes an overall rating _rp_ , as well as _sub-ratings_ of different skills (e.g., tackling, dribbling etc.). There are 11,060 players in totals and an average of 2 rating readings per season for every player. One of the information that we need for our analysis and is not present in the original dataset, is the players’ position and his market value. We obtained this information through FIFA’s rating website (www.sofifa.com) for all the players in our dataset. 

The goals scored in a soccer game have traditionally been described through a Poisson distribution [17, 12], while a negative binomial distribution has also been proposed to account for possible over-dispersion in the data [19, 9]. However, the over-dispersion, whenever observed is fairly small and from a practical perspective does not justify the use of the negative binomial for modeling purposes considering the trade-off between complexity of estimating the models and improvement in accuracy [12]. In our data, we examined the presence of overdispersion through the Pearson chi-squared dispersion test. We performed the test separately for the goal scored from home and away teams and in both cases the dispersion statistic is very close to 1 (1.01 and 1.1 respectively), which allows us to conclude that a Poisson model fits better for our data. Figure 1 depicts the two distributions for the goals scored per game for the home and away teams in our dataset. 

Another important modeling question is the dependency between the two Poisson processes that capture the scoring for the two competing teams. In general, the empirical data exhibit a small correlation (usually with an absolute value for the correlation coefficient less than 0.05) between the goals scored by the two competing teams and the use of Bivariate Poisson models has been proposed to deal with this correlation [13]. Simple put, ( _X, Y_ ) _∼ BP_ ( _λ_ 1 _, λ_ 2 _, λ_ 3), where: 

> 2English Premier League, Bundesliga, Serie A, Scotish Premier League, La Liga, Swiss Super League, Jupiler League, Ligue 1, Eredivisie, Liga Zon Sagres, Ekstraklasa. 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**4** 





**Figure 1.** _The empirical distribution of the number of goals scored per game from the home (left) and way (right) teams. The data can be fitted by a Poisson with means λ_ = 1 _._ 56 _and λ_ = 1 _._ 18 _respectively._ 





The parameter _λ_ 3 captures the covariance between the two marginal Poisson distributions for _X_ and _Y_ , i.e., _λ_ 3 = _Cov_ ( _X, Y_ ). In our data, the correlation between the number of goals scored from the home and away team is also small and equal to -0.06. While this correlation is small, Karlis and Ntzoufras [13] showed that it can impact the estimation of the probability of a draw. However, a major drawback of the Bivariate Poisson model is that it can only model data with positive correlations [14]. Given that in our dataset the correlation is negative, and hence, a Bivariate Poisson model cannot be used, an alternative approach is to directly model the difference between the two Poisson processes that describe the goals scored for the two competing teams. With _Z_ , _X_ and _Y_ being the random variables describing the final score differential, the goals scored from the home team and the goals scored from the away team respectively, we clearly have _Z_ = _X − Y_ . With ( _X, Y_ ) _∼ BP_ ( _λ_ 1 _, λ_ 2 _, λ_ 3), _Z_ has the following probability mass function [22]: 



where _Ir_ ( _x_ ) is the modified Bessel function. Equation (2.2) describes a Skellam distribution and clearly shows that the distribution of _Z_ does not depend on the correlation between the two Poisson distributions _X_ and _Y_ . In fact, Equation (2.2) is exactly the same as the distribution of the difference of two independent Poisson variates [22]. Therefore, we can directly model the goal differential without having to explicitly model the covariance. Of course, the drawback of this approach is that the derived model is not able to provide estimates on the actual 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**5** 



**Figure 2.** _For our analysis we grouped the various player positions to four distinct groups, namely, goalkeeping, attack, middlefielders and defense._ 

game score, but rather only on the score differential. Nevertheless, in our study we are only interested for the win/lose/draw probability and hence, this does not pose any limitations for our purposes. 

**2.2. Skellam Regression Model.** Our objective in this work is quantifying the value of different positions in soccer. This problem translates to identifying how an one-unit increase in the rating of a player’s position impacts the probability of his team winning. For example, if we substitute our current striker who has a FIFA rating of 79, with a new striker with a FIFA rating of 80, how do our chances of winning alter? Once we have this information we can obtain for every player an expected league points added per game over a reference, i.e., replacement, player (Section 3.1). This can then be used to obtain a more objective market value for players based on their position and rating (Section 3.2). 

In order to achieve our goal we will model the goal differential _Z_ of a game using as our independent variables the player/position ratings of the two teams that compete. Hence, our model’s dependent variable is the goal differential (home - away) of game _i_ , _zi_ , while our independent variables are the positional rating differences of the two teams, _xi,π_ = _rp_ ( _h,π,i_ ) _− rp_ ( _a,π,i_ ) _, ∀π ∈_ Π, where _rp_ ( _h,π,i_ ) ( _rp_ ( _a,π,i_ )) is the rating of the home (away) team player that covers position _π_ during game _i_ and Π is the set of all soccer positions. One of the challenges with this setting is the fact that different teams will use different formations and hence, it can be very often the case that while one team might have 2 center backs and 2 wing backs, the other team might have 3 center backs only in its defensive line. This will lead to a situation where the independent variables _xi,π_ might not be well-defined. While this could potentially be solved by knowing the exact formation of a team (we will elaborate on this later), this is unfortunately a piece of information missing from our data. Nevertheless, even this could create data sparsity problems. Hence, we merge positions to four groups, 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**6** 

namely, attacking line, middle-fielders, defensive line and goalkeeping. Figure 2 depicts the grouping of the positions we used to the four lines Λ = _{λD, λM , λA, λGK}_ . Note that this grouping in the four lines has been used in the past when analyzing soccer players as well [10]. The independent variables are then the differences in the average rating of the corresponding lines. The interpretation of the model slightly changes now, since, as we will elaborate on later, the independent variable captures the rating of the whole line as compared to a single position/player. Under this setting we fit a Skellam regression for _Z_ through maximum likelihood estimation. In particular: 

## **Model 2.1: Final Goal** 

- We model the goal differential _Zi_ of game _i_ using the following four co-variates: 

   - The difference between the average player rating of the defensive line of the two teams _xD_ 

   - The difference between the average player rating of the middle-fielders of the two teams _xM_ 

   - The difference between the average player rating of the attacking line of the two teams _xA_ 

   - The difference between the goalkeeper’s rating of the two teams _xGK_ The random variable _Z_ follows a Skellam distribution, where its parameters depend on the model’s covariates **x** = ( _xD, xM , xA, xGK_ ): 

|(2.3)|_Z ∼Skellam_(_λ_1_, λ_2)|
|---|---|
|(2.4)|log(_λ_1) =**b**<sup>_T_</sup><br>1 <sup>_·_</sup><sup>**x**</sup>|
|(2.5)|log(_λ_2) =**b**<sup>_T_</sup><br>2 <sup>_·_</sup><sup>**x**</sup>|



Table 1 shows the regression coefficients. It is interesting to note that the coefficients for the two parameters are fairly symmetric. _λ_ 1 and _λ_ 2 can be thought of as the mean of the Poisson distributions describing the home and visiting team respectively and hence, a positive relationship between an independent variable and the score differential for one team corresponds - to an equally strong - negative relationship between the same variable and the score differential. An additional thing to note is that increase in the average rating of any line of a team contributed positively to its chances of winning (as one might have expected). 

Before using the model for estimating the expected league points added for each player, we examine how good the model is in terms of actually predicting the score differential and the win/draw/lose probabilities. We use an 80-20 split for training and testing of the model. We begin our evaluation by calculating the difference between the goal differential predicted by our model and the actual goal differential of the game [23]. Figure 3 (left) presents the distribution of this difference and as we can see it is center around 0, while the standard deviation is equal to 1.6 goals. Furthermore, a chi-squared goodness-of-fit test cannot reject the hypothesis that the distribution is normal with mean equal to 0 and standard deviation 1.6. 

However, apart from the score differential prediction error, more important for our pur- 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**7** 

|**Variable**|log(_λ_1)<br>log(_λ_2)|
|---|---|
|Intercept|0.41***<br>0.13***|
||(0.006)<br>(0.006)|
|_xD_|0.02***<br>-0.02***|
||(0.01)<br>(0.002)|
|_xM_|0.02***<br>-0.02***|
||(0.01)<br>(0.001)|
|_xA_|0.01***<br>-0.01***|
||(0.001)<br>(0.001)|
|_xGK_|0.001<br>-0.002**|
||(0.001)<br>(0.001)|
|N|21,374<br>21,374|
|***_p <_0_._01<br>_Skellam _|, **_p <_0_._05, *_p <_0_._1<br>**Table 1**<br> _regression coefcients_|



poses is the ability to obtain _true_ win/loss/draw probabilities for the games. As we will see in Section 3.1 we will use the changes in these probabilities to calculate an expected league points added for every player based on their position and rating. Hence, we need to evaluate how accurate these probabilities are and how well-calibrated they are. Figure 3 (right) presents the probability calibration curves. Given that we have 3 possible results (i.e., win, loss and draw), we present three curves from the perspective of the home team, that is, a home team win, loss or draw. As we can see for all 3 events the probability output of our model is very accurate, that is, all lines are practically on top of the _y_ = _x_ line. Given that the _x_ -axis is the predicted probability and the _y_ -axis is the observed probability, this means that these two are practically equal. It is interesting to note, that our model does not provide a draw probability higher than 30% for any of the games in the test set, possibly due to the fact that the base rate for draws in the whole dataset is about 25%. 

In the following section we show how we can use this model in order to estimate the expected league points added for a player and how we can get insights for his actual market value. 

**3. eLPAR and Market Value.** In this section we begin by defining the notion of a replacement player and how we can use the model from Section 2.2 to identify how many league points a player is expected to provide to his team above a replacement player. These values allow us to further identify the positional value of the different lines and explore the _efficiency_ of the player transfer market. 

**3.1. Replacement Player and Expected League Points Added.** The notion of replacement player was popularized by Keith Woolner [27] who developed the Value Over Replacement Player (VORP) metric for baseball. The high level idea is that player talent comes at different levels. For instance, there are superstar players, average players and subpar player 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**8** 





**Figure 3.** _Our model is able to predict the score differential as well as the win/loss/draw probabilities fairly accurate._ 

talent. These different levels come in different proportions within the pool of players, with superstars being a scarcity, while subpar players (what Woolner termed replacement players) being a commodity. This essentially means that a team needs to spend a lot of money if it wants to acquire a superstar, while technically a replacement player comes for free. Since a replacement player can be thought of as a _free_ player, a good way to evaluate (and consequently estimate a market value for) a player is to estimate the (expected) contribution in wins, points etc. that he/she offers above a replacement player. One of the main contributions of Woolner’s work is to show that average players have value [25]! If we were to use the average player as our reference for evaluating talent, we would fail to recognize the value of average playing time. However, replacement level, even though it is important for assigning economic value to a player, it is a less concrete mathematical concept. Identifying an exact replacement level is beyond the scope of our work but there are several ways that have been used to estimate this. For example, one can sort players (of a specific position) in decreasing order of their contract value and obtain as replacement level the talent at the bottom 20th percentile [24]. What we use for our study is a _rule-of-thumb_ suggested from Woolner [26]. In particular, the replacement level is set at the 80% of the positional average rating. 

Figure 4 presents the distribution of the player ratings for the different lines for the last season in our dataset - i.e., 2015-16. The vertical green lines represent the replacement level for every position/line, i.e., 80% of the average of each distribution. As we can see all replacement levels are very close to each other and around a rating of 56. So the question now becomes how are we going to estimate the expected league points added above replacement ( `eLPAR` ) given the model from Section 2.2 and the replacements levels calculated here. First let us define `eLPAR` more concretely: 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**9** 









**Figure 4.** _The replacement level rating (green vertical line) for each one of the positional lines in soccer is around 56._ 

## **Definition 3.1:** eLPAR 

Consider a game between teams with replacement players. Player _p_ substitutes a replacement player in the lineup. `eLPAR` _p_ describes how many league points (win=3 points, draw = 1 point, loss = 0 points) _p_ is expected to add for his team. 

Based on the above definition, `eLPAR` _p_ can be calculated by estimating the change in the win/draw/loss probability after substituting a replacement player with _p_ . However, the win probability model aforementioned does not consider individual players but rather lines. Therefore, in order to estimate the expected points to be added by inserting player _p_ in the lineup we have to consider the formation used by the team. For example, a defender substituting a replacement player in a 5-3-2 formation will add a different value of expected points as compared to a formation with only 3 center-backs in the defensive line. Therefore, in order to estimate `eLPAR` _p_ we need to specify the formation we are referring to. Had the formation been available in our dataset we could have built a multilevel model, where each 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**10** 

combination of position and formation would have had their own coefficients<sup>3</sup> . Nevertheless, since this is not available our model captures the formation-average value of each line. In particular, `eLPAR` _p_ for player _p_ with rating _rp_ can be calculated as following: 

Step.1 Calculate the increase in the average rating of the line _λ ∈_ Λ where _p_ substituted the replacement player based on _rp_ , formation _φ_ and the replacement player rating for the line _rreplacement,φ,λ_ 

Step.2 Calculate, using the win probability model above, the change in the win, loss and draw probability ( _δPw_ , _δPd_ and _δPl_ respectively) 

Step.3 Calculate `eLPAR` _p_ ( _φ_ ) as: 



It should be evident that by definition a replacement player has `eLPAR` = 0 - regardless of the formation - while if a player has rating better than a replacement, his `eLPAR` will be positive. However, the actual value and how it compares to players playing in different positions will depend on the formation. In Figure 5 we present the expected league points added per game for players with different ratings (ranging from 50 to 99) and for different formations. While there are several different formations that a team can use, we chose 4 of the most often used ones. 

One common pattern in all of the formations presented is the fact that for a given player rating goal keepers provide the smallest expected league points above replacement - which is in line with other studies/reports for the value of goal keepers in today’s soccer [3]. It is also evident that depending on the formation the different positions offer different _value_ . For example, a 4-5-1 system benefits more from an attacker with a rating of 90 as compared to a defender with the same rating, while in a 3-5-2 formation the opposite is true. It is also interesting to note that for a 4-4-2 formation, the value added above replacement for the different positions are very close to each other (the closest compared to the rest of the formations). This most probably is due to the fact that the 4-4-2 formation is the most balanced formation in soccer, and hence, all positions _contribute_ equally to the team. To reiterate this is an expected value added, i.e., it is not based on the actual performance of a player but rather on static ratings for a player. Given that teams play different formations over different games (or even during the same game after in-game adjustments), a more detailed calculation of `eLPAR` would include the fraction of total playing time spent by each player on a specific formation. With _T_ being the total number of minutes played by _p_ , and _tφ_ the total minutes he played in formation _φ_ , we have: 



The last row in Figure 5 presents the average `eLPAR` for each position and player rating across all the four possessions (assuming equal playing time for all formations). As we can see 

> 3And in this case we would also be able to analyze better the impact of positions within a line (e.g., value of RB/LB compared to CB). 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**11** 











**Figure 5.** _Expected league points added above replacement for different formations, player ratings and positions._ 

for the same player rating, a defender adds more expected league points above replacement, followed by an attacker with the same rating. A middlefielder with the same rating adds a little less expected league points, while a goal keeper (with the same rating) adds the least amount of expected league points. A team manager can use this information to identify more appropriate targets given the team style play (formations used) and the budget. In the following section we will explore the relation between the market value of a player and his 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**12** 







**Figure 6.** _Even though goalkeepers are among the lowest paid players in soccer, they still are overpaid in terms of expected league points contributions. Defenders are undervalued when it comes to contributions in winning._ 

## `eLPAR` . 

**3.2. Positional Value and Player Market Value.** In this section we will explore how we can utilize `eLPAR` to identify possible _inefficiencies_ in the player’s transfer market. In particular, we are interested in examining whether the transfer market overvalues specific positions based on the `eLPAR` value they provide. Splitting the players in the four lines Figure 6 (left) presents the differences between the average market value for each position. As we can see, on average, defenders are the lowest paid players! However, as aforementioned (Figure 5) for a given player rating, a defensive player provides the maximum `eLPAR` value. Nevertheless, this is not enough to declare the market inefficient. 

What we are really interested in is the monetary value that a team pays for 1 expected league point above replacement per player. Granted there is a different supply of players in different positions. For example, only 8.5% of the players are goal keepers, as compared to approximately 35% of defenders<sup>4</sup> , and hence, one might expect goalkeepers to be paid more than defenders. However, there is also smaller demand for these positions and hence, we expect these two to cancel out to a fairly great extend, at least to an extend that does not over-inflate the market values. Hence, we calculate the monetary cost the players market values imply that teams are willing to pay for 1 expected league points. Figure 6 (middle) presents the cost (in Euros) per 1 expected league points for different positions and as a function of the `eLPAR` they provide. An _efficient_ market would have four straight horizontal lines, one on top of the other, since the value of 1 expected league point should be the same regardless of where this point is expected. However, what we observe is that the market over-values significantly goal keepers (even though on average they are only the 3rd highest paid line), and this is mainly a result of their low `eLPAR` (the best goalkeeper in our dataset provides an `eLPAR` of just over 0.1 per 90 minutes). Furthermore, teams appear to be willing to pay a premium for expected league points generated by the offense as compared to points generated by the defense, and this premium increases with `eLPAR` . This becomes even more clear from the right plot in Figure 6, where teams are willing to pay multiples in premium for 1 expected league point coming from a goalkeeper with 88 FIFA rating as compared to 1 expected league point 

> 4There is another approximately 35% of middlefielders and 21% of attackers. 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**13** 

## (i.e., the same performance) coming from a defender with 86 FIFA rating. 

These results open up interesting questions for soccer clubs when it comes to budget decisions. Budget is spent for two reasons; (a) to win, as well as, (b) to maximize the monetary return (after all, sports franchises are businesses). The premium that clubs are willing to pay an attacker over a defender for the same amount of league points can be seen as an investment. These players bring fans in the stadium, sponsors, sell club merchandise, etc. For example, even though attackers are approximately only 20% of the players, 60% of the top-selling jerseys in England during 2018 belonged to attackers [2]. Therefore, when we discuss the money spent from a team for a transfer, winning is only on part of the equation. Nevertheless, similar analysis is helpful for clubs with limited budget that want to maximize their winning chances. A club with a fixed budget _B_ can distribute it in such a way that maximizes the expected league points _bought_ (even under positional constraints). For instance, with _B_ = 6 millions and with the need for an attacker and a goalkeeper, if we use the average market values for the two positions we should allocate 55% of the budget (i.e., 3.3 millions) for the goalkeeper and 45% of the budget for the defender. This will eventually get us about 0.028 expected league points per 90 minutes (a goalkeeper with a 74 FIFA rating and a defender with a 73 FIFA rating). However, if we allocate 500K for the goalkeeper and 5.5 millions for the defender this will get us around 0.033 expected league points (a goalkeeper with 68 FIFA rating and a defender with 78 FIFA rating), or simply put the team will have bought 1 expected league point at a 15% discount as compared to the rest of the market. 

## **Rule of Thumb 3.1: Positional Premiums** 

Buy bulk expected league points at a discount through defense and pay a smaller premium for an _average_ goalkeeper 

We further examine some real budgets from team. For example, let us consider FC Barcelona and Manchester United. We use the wages of the starting 11 players of the teams and considering the total budget constant, we redistribute the budget based on the `eLPAR` of each player. The reason for doing so is that there is no salary cap in European soccer and hence, we should make an assumption for the total budget of a team. Hence, this analysis will simply provide us with some insight on whether teams relatively spend their budget proportional to the positional and personal value of each player on field. Simply put we cannot really say whether a team over-spend on a player since as aforementioned there are several other factors (from a business perspective) to consider when making salary negotiations. Table 2 presents the starting 11 for Barcelona, their FIFA rating and their wage<sup>5</sup> , while Table 3 presents the same information for Manchester United<sup>6</sup> . We have also included the formation-agnostic (i.e., average of the four most frequent formations aforementioned) `eLPAR` and the corresponding redistribution of salaries, as well as the same figures for the default formation of each team (44-2 for Barcelona and 4-3-3 for Manchester United). The way we calculate the re-distribution is as following: 

Step.1 Calculate the fraction of total `eLPAR` , i.e., `eLPAR` _total_ =<sup>�11</sup> _p_ =1<sup>`eLPAR`</sup><sup>_p_,thatplayer</sup><sup>_p_</sup> 

- 5www.sofifa.com/team/241 

> 6www.sofifa.com/team/11 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**14** 

|||**FC **<br>|**Barcelona**||||
|---|---|---|---|---|---|---|
|Players|FIFA Rating|Wage (e)|`eLPAR`|`eLPAR`Wage<br>(e)|`eLPAR`<br>(4-4-2)|`eLPAR`Wage<br>(4-4-2) (e)|
|M. Stegen|87|185K|0.092|79K|0.093|83K|
|S. Roberto|82|150K|0.32|271.5K|0.30|266K|
|Pique|87|240K|0.38|324K|0.36|317K|
|S. Umtiti|84|175K|0.35|292.5K|0.32|286.5K|
|Jordi Alba|87|185K|0.38|324K|0.35|317.5K|
|O. Dembele|83|150K|0.28|239K|0.29|258K|
|I. Rakitic|86|275K|0.31|266K|0.32|287K|
|s. Busquets|87|250K|0.32|275K|0.33|298K|
|Coutinho|87|275K|0.32|275K|0.33|298K|
|L. Messi|94|565K|0.41|349K|0.35|317K|
|L. Suarez|92|510K|0.39|330K|0.33|300K|



**Table 2** 

_FC Barcelona wages and_ `eLPAR` _-based projected wages._ 

|||**Manch**<br>|**ester Uni**|**ted**<br>|||
|---|---|---|---|---|---|---|
|Players|FIFA Rating|Wage (e)|`eLPAR`|`eLPAR`Wage<br>(e)|`eLPAR`<br>(4-3-3)|`eLPAR`Wage<br>(4-3-3) (e)|
|De Gea|91|295K|0.1|65.5K|0.11|69K|
|A. Valencia|83|130K|0.33|208K|0.31|203K|
|C. Smalling|81|120K|0.31|193K|0.28|188K|
|V. Lindelof|78|86K|0.27|169K|0.25|165K|
|A. Young|79|120K|0.28|177K|0.26|172.5K|
|N. Matic|85|180K|0.3|189.5K|0.41|273K|
|A. Herrera|83|145K|0.28|176K|0.38|254K|
|P. Pogba|88|250K|0.34|209.5K|0.46|301.5K|
|J. Lingard|81|115K|0.27|168K|0.15|100K|
|R. Lukaku|86|210K|0.32|202.5K|0.18|121K|
|A. Sanchez|88|325K|0.35|216K|0.19|129K|



**Table 3** 

_Manchester United wages and_ `eLPAR` _-based projected wages._ 

## `eLPAR` _<u>p</u>_ 

contributes to his team, i.e., _fp_ = `eLPAR` _total_ Step.2 Calculate the `eLPAR` -based wage for player _p_ as _fp · B_ 

As we can see there are differences in the wages projected when using `eLPAR` . Both teams for example appear to overpay their goalkeepers based on what expected league points above replacement per 90 minutes they offer. Of course, some players are under-valued, and as we can see these players are mainly in the defensive line. The average average discrepancy between the actual wage and the projected wage from `eLPAR` is around 4% of the total budget 

_This manuscript is for review purposes only._ 

**POSITIONAL VALUE IN SOCCER: EXPECTED LEAGUE POINTS ADDED ABOVE REPLACEMENT** 

**15** 

for Manchester United and 3% for Barcelona. While teams with such large budgets like Manchester United and Barcelona might be able to pay all of their players to at least their value (while overvaluing specific positions), other teams in the middle-of-the-pack can achieve significant savings, without compromising their chances of winning. 

**4. Conclusions and Discussion.** In this work our objective is to understand positional values in soccer and relate them with the current transfer market. We start by developing a win probability model for soccer games based on the ratings of the four lines of the teams (attack, middlefield, defense and goalkeeper). We then translate this positional values to expected league points added above a replacement player considering a team’s formations. Our results indicate that specific positions are over-valued when only considering their contribution to winning the game. 

We believe that this study will trigger further research on the positional value in soccer. An immediate improvement over our current model is to consider the actual formation that the teams used (a piece of information missing in our current dataset). This will allow us to build a multilevel regression model where we will include covariates for more fine grained positions (e.g., center back, right back, center middlefielder etc.). We can also include information about substitutions during a game (another piece of information not available to us). Furthermore, our current study is based on static player ratings obtained from FIFA. This only allows us to estimate the **expected** league points added over a replacement player. While these ratings capture the overall performance of a player during past season(s) and hence, it is still appropriate for estimating his monetary value, actual game ratings for players will allow us to estimate the **actual** league points added over replacement by a player over the course of a season. These game ratings for example can be composed through appropriate analysis of optical tracking data, which at the least will provide us with information about how much time a combo-player (e.g., a left middlefielder who can also play left wing/forward) played at each line. We will explore these direction as part of our future research, while we will also explore the applicability of a similar approach towards quantifying positional value for American Football (NFL). In particular, using player ratings from Madden (in a similar way we use player ratings from FIFA), we can evaluate the contribution of 1 unit increase in the Madden rating of a player to the expected points added from a team’s play. This could be a significant step towards defining a metric similar to Wins Above replacement for NFL, and finally understanding the contribution of each position in winning. 

### **REFERENCES** 

> [1] _European soccer database_ , 2016, https://www.kaggle.com/hugomathien/soccer/. 

> [2] _Best selling premier league player jerseys revealed_ , 2018, https://soccer.nbcsports.com/2018/02/15/ top-20-premier-league-player-jerseys-revealed/. 

> [3] _Why footballs goalkeepers are cheap and unheralded_ . The Economist, Feb. 2018, https://www.economist. com/game-theory/2018/02/09/why-footballs-goalkeepers-are-cheap-and-unheralded (accessed 201807-15). [4] L. Bornn, D. Cervone, and J. Fernandez, _Soccer analytics: Unravelling the complexity of the beautiful game_ , Significance, 15, pp. 26–29. 

> [5] L. Cotta, P. de Melo, F. Benevenuto, and A. A. Loureiro, _Using fifa soccer video game data for soccer analytics_ , in Workshop on Large Scale Sports Analytics, 2016. 

_This manuscript is for review purposes only._ 

**KONSTANTINOS PELECHRINIS, WAYNE WINSTON** 

**16** 

- [6] Economist, _How gps tracking is changing football_ , 2018, https://www.1843magazine.com/technology/ how-gps-tracking-is-changing-football (accessed 2018-07-09). 

- [7] A. Fairchild, K. Pelechrinis, and M. Kokkodis, _Spatial analysis of shots in mls: A model for expected goals and fractal dimensionality_ , Journal of Sports Analytics, pp. 1–10. 

- [8] J. Fernandez and L. Bornn, _Wide open spaces: A statistical technique for measuring space creation in professional soccer_ , 2018. 

- [9] J. Greenhough, P. Birch, S. Chapman, and G. Rowlands, _Football goal distributions and extremal statistics_ , Physica A: Statistical Mechanics and its Applications, 316 (2002), pp. 615–624. 

- [10] M. He, R. Cachucho, and A. Knobbe, _Football players performance and market value_ , in Proceedings of the 2nd workshop of sports analytics, European Conference on Machine Learning and Principles and Practice of Knowledge Discov-ery in Databases (ECML PKDD), 2015. 

- [11] B. James and J. Henzler, _Win shares_ , STATS Pub., 2002. 

- [12] D. Karlis and I. Ntzoufras, _On modelling soccer data_ , Student, 3 (2000), pp. 229–244. 

- [13] D. Karlis and I. Ntzoufras, _Analysis of sports data by using bivariate poisson models_ , Journal of the Royal Statistical Society: Series D (The Statistician), 52 (2003), pp. 381–393. 

- [14] D. Karlis and I. Ntzoufras, _Bivariate poisson and diagonal inflated bivariate poisson regression models in r_ , Journal of Statistical Software, 14 (2005). 

- [15] H. M. Le, P. Carr, Y. Yue, and P. Lucey, _Data-driven ghosting using deep imitation learning_ , MIT Sloan Sports Analytics Conference, (2017). 

- [16] H. M. Le, Y. Yue, and P. Carr, _Coordinated multi-agent imitation learning_ , ICML, (2017). 

- [17] A. J. Lee, _Modeling scores in the premier league: is manchester united really the best?_ , Chance, 10 (1997), pp. 15–19. 

- [18] P. Lucey, A. Bialkowski, M. Monfort, P. Carr, and I. Matthews, _quality vs quantity: Improved shot prediction in soccer using strategic features from spatiotemporal data_ , 2015. 

- [19] R. Pollard, _69.9 goal-scoring and the negative binomial distribution_ , The Mathematical Gazette, 69 (1985), pp. 45–47. 

- [20] P. Power, H. Ruiz, X. Wei, and P. Lucey, _Not all passes are created equal: Objectively measuring the risk and reward of passes in soccer from tracking data_ , KDD ’17, 2017, pp. 1605–1613. 

- [21] K. Shank, _Expected goal chains: The link between passing sequences and shots_ , Oct. 2017, https://www.americansocceranalysis.com/home/2017/10/3/ expected-goal-chains-the-link-between-passing-sequences-and-shots (accessed 2018-07-09). 

- [22] J. G. Skellam, _The frequency distribution of the difference between two poisson variates belonging to different populations._ , Journal of the Royal Statistical Society. Series A (General), 109 (1946), pp. 296– 296. 

- [23] H. Stern, _On the probability of winning a football game_ , American Statistician, 45 (1991), pp. 179–183. 

- [24] W. L. Winston, _Mathletics: How gamblers, managers, and sports enthusiasts use mathematics in baseball, basketball, and football_ , Princeton University Press, 2012. 

- [25] K. Woolner, _Introduction to vorp: Value over replacement player_ , 2001, https://web.archive.org/web/ 20070928064958/http://www.stathead.com/bbeng/woolner/vorpdescnew.htm (accessed 2018-07-09). 

- [26] K. Woolner, _Vorp: Measuring the value of a baseball player’s performance_ , 2001, https://web.archive. org/web/20080926233543/http://www.stathead.com/articles/woolner/vorp.htm (accessed 2018-0714). 

- [27] K. Woolner, _Understanding and measuring replacement level_ , Baseball prospectus, (2002), pp. 55–66. 

- [28] WorldAtlas, _The most popular sports in the world_ , Apr. 2018, https://www.worldatlas.com/articles/ what-are-the-most-popular-sports-in-the-world.html (accessed 2018-07-09). 

_This manuscript is for review purposes only._ 


