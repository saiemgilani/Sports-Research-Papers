<!-- source: randoms/Adjusted_Plus_Minus_for_NHL_Players_usin.pdf -->

# Adjusted Plus-Minus for NHL Players using Ridge Regression with Goals, Shots, Fenwick, and Corsi 

Brian Macdonald<sup>_∗_</sup> 

October 3, 2012 

#### **Abstract** 

Regression-based adjusted plus-minus statistics were developed in basketball and have recently come to hockey. The purpose of these statistics is to provide an estimate of each player’s contribution to his team, independent of the strength of his teammates, the strength of his opponents, and other variables that are out of his control. One of the main downsides of the ordinary least squares regression models is that the estimates have large error bounds. Since certain pairs of teammates play together frequently, collinearity is present in the data and is one reason for the large errors. In hockey, the relative lack of scoring compared to basketball is another reason. To deal with these issues, we use ridge regression, a method that is commonly used in lieu of ordinary least squares regression when collinearity is present in the data. We also create models that use not only goals, but also shots, Fenwick rating (shots plus missed shots), and Corsi rating (shots, missed shots, and blocked shots). One benefit of using these statistics is that there are roughly ten times as many shots as goals, so there is much more data when using these statistics and the resulting estimates have smaller error bounds. The results of our ridge regression models are estimates of the offensive and defensive contributions of forwards and defensemen during even strength, power play, and short handed situations, in terms of goals per 60 minutes. The estimates are independent of strength of teammates, strength of opponents, and the zone in which a player’s shift begins. 

**Keywords:** adjusted plus-minus, plus-minus, hockey, nhl, performance analysis 

> _∗_ email: `bmac@jhu.edu` 

1 

## **Contents** 

|**1**<br>**Intr**|**oduction**<br>**3**|
|---|---|
|1.1|Brief summary of the new models<br>. . . . . . . . . . . . . . . . .<br>4|
|1.2|Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>5|
|1.3|Example of the results<br>. . . . . . . . . . . . . . . . . . . . . . .<br>6|
|**2**<br>**Ridg**|**e Regression Model**<br>**8**|
|2.1|Differences in OLS and Ridge Estimates . . . . . . . . . . . . . .<br>10|
|2.2|Year-to-year correlations . . . . . . . . . . . . . . . . . . . . . .<br>11|
|**3**<br>**Resu**|**lts**<br>**12**|
|3.1|Four-year Selke Trophy fnalists for Best Defensive Forward . . .<br>13|
|3.2|Four-year Norris Trophy fnalists for Best Defensemen . . . . . .<br>14|
|3.3|Four-year Hart Trophy fnalists for Most Valuable Player . . . . .<br>15|
|**4**<br>**Con**|**clusions and Future Work**<br>**15**|
|**5**<br>**App**|**endix**<br>**19**|
|5.1|Ordinary Least Squares . . . . . . . . . . . . . . . . . . . . . . .<br>19|
|5.2|Ridge Regression . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
|5.3|Choosing_λ_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>21|
|5.4|Supplemental fgures . . . . . . . . . . . . . . . . . . . . . . . .<br>23|



## **List of Tables** 

|1|Summary of notation for_APM_results using goals. . . . . . . . . .<br>6<br>|
|---|---|
|2|The top 10 offensive players in the NHL according to_G_<sup>off</sup>. . . . .<br>7|
|3|Sidney Crosby’s_APM_statistics during 2007-11 using goals.<br>. . .<br>7|
|4<br>5|Alex Ovechkin’s EV offense statistics, with standard errors. . . . .<br>8<br>The top 5 defensive forwards according to_G_<sup>def</sup>. . . . . . . . . . .<br>13|
|6|The top 5 defensemen during the last 4 seasons, according to_G_.<br>.<br>14|
|7|The top 5 players according to_G_. . . . . . . . . . . . . . . . . . .<br>15|



## **List of Figures** 

|1|Estimates of_G_<sup>off</sup><br>_PP,_60 <sup>for some players, for different values of</sup><sup>_λ_. . .</sup><br>11|
|---|---|
|2|_G_<sup>off</sup><br>_PP,_60 <sup>vs</sup><sup>_λ_ for players whose estimates change the most . . . . .</sup><br>12|
|3|Year-to-year correlations of OLS and Ridge estimates . . . . . . .<br>13|
|4|Shift lengths for all PP shifts and PP shifts when a goal is scored .<br>23|
|5|Distribution of players’ ice time for EV and PP situations . . . . .<br>24|



2 

## **1 Introduction** 

Though the plus-minus statistic was first used in hockey, advanced versions of plus-minus have been developing more quickly in basketball. These new versions attempt to correct one or more of the problems associated with the traditional plusminus statistic, which depends heavily on the strength of a player’s teammates and opponents, and on other variables out of a player’s control. Regression-based versions of adjusted plus-minus ( _APM_ ) statistics for NBA players can be found in Winston (2009), Rosenbaum (2004), Lewin (2007), Witus (2008), Ilardi and Barzilai (2008), Sill (2010), and Fearnhead and Taylor (2011). 

In Macdonald (2011a) and Macdonald (2011b), the author developed similar models for hockey. In Macdonald (2011a), the author used weighted least squares models similar to those in Rosenbaum (2004) and Ilardi and Barzilai (2008) to find the estimates of each player’s offensive and defensive contribution during even strength situations, adjusted for the strength of his teammates and opponents. The contributions are given in terms of goals per 60 minutes and goals per season. Special teams situations are addressed in Macdonald (2011b). Information about the zone in which each shift begins was also used in Macdonald (2011b) in order to get estimates that are independent of the zone on the ice in which a player typically begins his shifts. 

In many of the basketball articles, and also in the hockey articles Macdonald (2011a) and Macdonald (2011b), it was noted that one downside of the ordinary least squares regression models is that the results can have large error bounds, which are measures of uncertainty in the estimates. Since two main uses of these estimates could be (1) deciding which players to trade for and (2) establishing parameters for salary negotiations, smaller errors, and hence more precise estimates, have significant value to NHL analysts and decision-makers. 

One reason for the large errors is the high collinearity in the data caused by teammates who play together frequently, a common occurrence in many sports. For example, Henrik and Daniel Sedin, twin brothers who play for the Vancouver Canucks, are almost always on the ice together. A regression model will have a difficult time telling them apart (both statistically and biologically) and their estimates tend to have large errors. In an extreme case where two players always play together, the ordinary least squares estimates will not even be unique. 

Another reason for the high errors in hockey is the relative lack of scoring when compared to a sport like basketball. A typical hockey team only scores two to four goals per game on average during a season. The low goal scoring rates, coupled with randomness and luck involved with goal scoring, makes it difficult to properly judge players using goals alone without using multiple seasons of data. Additionally, a player’s goals for and goals against while he is on the ice is dependent on the quality of goalies on the ice. Ideally, one would prefer to estimate a player’s abilities in a way that is independent of the quality of the 

3 

goalies he faces, and independent of the quality of goalies on his team. 

### **1.1 Brief summary of the new models** 

In light of these observations, we make two modifications to the models given in Macdonald (2011a) and Macdonald (2011b). First, in lieu of ordinary least squares regression models, we use ridge regression models (Hoerl (1962), Hoerl and Kennard (1970)), similar to the model used for basketball in Sill (2010). Ridge regression frequently reduces the error bounds in the estimates and improves the predictive performance of the model when collinearly exists in the data. Ridge regression introduces bias in the estimates, but the tradeoff is typically worthwhile. The model is discussed in detail in Section 2. 

The second change we make is to form additional models that use three other statistics, in addition to goals, as the dependent variable. These additional models use shots, Fenwick rating (shots plus missed shots), and Corsi rating (shots, missed shots, and blocked shots). These statistics were chosen because each of them has been shown to be very good indicators of performance at the team level (JLikens (2011), Ferrari (2009)). 

There are pros and cons to using these statistics, and that is one reason that we will use them _in addition to_ goals and not _instead of_ goals. For example, on one hand, shots, Fenwick rating, and Corsi rating ignore the shooting ability of players, although many hockey analysts would argue that a player’s shooting ability is not nearly as significant as his ability to generate shots. Also, some would argue that missed shots and blocked shots should not be included or should not be considered good, since they are attempted shots that never reached the goal. However, if a team has more shots, missed shots, and blocked shots than their opponents, it is most likely an indication of a territorial advantage and an advantage in terms of puck possession. In order to take a shot, a player must possess the puck, and typically that player is also in the offensive zone. 

The relationships among goals, shots, Fenwick rating, and Corsi rating are described well in JLikens (2011) and discussed further in Macdonald (2012). In both articles, the authors show that shots, Fenwick rating, and Corsi rating are better indicators than goals of a team’s future performance when one uses data from only half of a season. Based on this analysis, we believe the results based on shots, Fenwick rating and Corsi rating do have value, especially for our models that are based on only one season’s worth of data. The reader can decide for himor herself how much value those results have. 

One nice benefit of using of these additional statistics is that they are far more prevalent than goals. Typically, there are roughly 10 shots to every goal. The extra data goes a long way to producing estimates with much smaller error bounds. Also, for the most part, those statistics are independent of goalies, so the strength of the goalies on a player’s team will not have much of an affect on the estimates 

4 

of his contributions. When using goals, the estimate of a player’s defensive contribution, in particular, can be positively or negatively affected by the performance of the goalie playing behind him. 

In order to more easily compare the results based on these additional statistics with the results based on goals, the new results were rescaled using league average shooting percentages. By shooting percentages we mean goals per shot � _<u>GoalsShots</u>_ <u>�,</u> goals per Fenwick rating � _Shots_ + _<u>GoalsMissed Shots</u>_ �, and goals per Corsi rating � _Shots_ + _Missed ShotsGoals_ + _Blocked Shots_ �. League averages of these shooting percentages were computed for even strength, power play, and short handed situations separately, using data from the last four full NHL seasons. 

The results based on shots, Fenwick rating, and Corsi rating were then rescaled by multiplying by the league average goals per shot, goals per Fenwick rating, and goals per Corsi rating, respectively. These results are in the units of expected goals per 60 minutes based on shots, Fenwick, or Corsi. A player’s rescaled results based on shots can be thought of as his contribution to his team, in the units of expected goals per 60 minutes, based on shots for and shots against when he was on the ice. The results remain independent of the strength of his teammates, the strength of his opponents, and the zone in which his shifts begin. The rescaled results based on Fenwick rating and Corsi rating can be interpreted similarly. 

We use four separate ridge regression models for even strength situations using each of these four statistics (goals, shots, Fenwick rating, and Corsi rating) as the response variable. Each even strength model gives an even strength offensive and defensive component of _APM_ for each player in terms of goals per 60 minutes or expected goals per 60 minutes. These components can be added to give a player’s total contribution at even strength in terms of goals per 60 minutes. We also have four separate models for special teams situations, one for each of the four statistics. Each special teams model gives an offensive and defensive component on the power play, as well as an offensive and defensive component during short handed situations, in terms of goals per 60 minutes. In total, we get 36 estimates for each player in terms of goals per 60 minutes. If the results are expressed in terms of goals per season, then even strength, power play, and shorthanded results can be added to give estimates of offensive, defensive, and total contributions in all situations, in terms of goals per season. So, in this case, we get 48 different ratings for each player. This can be a bit of information overload, and when we present the results here, we will need to be selective regarding which components of _APM_ are listed. Notation will be important as well. 

### **1.2 Notation** 

Notation for the offensive, defensive, and total contribution of a player (forward or defensemen) during even strength, power play, and short handed situations, using 

5 

the model with goals as the response variable, is given in Table 1. The adjusted 

Table 1: Summary of notation for _APM_ results using goals. For each player (forward or defensemen), we have offensive, defensive, and total contributions during even strength, power play, and short handed situations, in terms of goals per season. 

|Strength<br>Offense Defense|Total|
|---|---|
|Even strength<br>_G_<sup>off</sup><br>_EV_<br>_G_<sup>def</sup><br>_EV_|_GEV_|
|Power play<br>_G_<sup>off</sup><br>_PP_<br>_G_<sup>def</sup><br>_PP_|_GPP_|
|Short handed<br>_G_<sup>off</sup><br>_SH_<br>_G_<sup>def</sup><br>_SH_|_GSH_|
|All situations<br>_G_<sup>off</sup><br>_G_<sup>def</sup>|_G_|



plus-minus results based on shots, Fenwick rating and Corsi rating are denoted similarly, except with “ _S_ ”, “ _F_ ”, and “ _C_ ”, respectively, instead of the “ _G_ ” that is used for goals. For example, the **ev** en strength **off** ensive component of _APM_ using **g** oals, **s** hots, **F** enwick rating, and **C** orsi rating are denoted _G_<sup>off</sup> _EV_<sup>_,S_</sup> _EV_<sup>off</sup><sup>_,F_</sup> _EV_<sup>offand</sup> _C_<sup>offThe per 60 minute versions of these statistics are denoted simi-</sup> _EV_<sup>, respectively.</sup> larly, but with a subscript of “60” included. For example, **ev** en strength **off** ensive component of adjusted plus-minus per **60** minutes using **g** oals is denoted _G_<sup>off</sup> _EV,_ 60<sup>.</sup> 

### **1.3 Example of the results** 

In Table 2, we give an example of the results. We list the top 10 players in offense during the 2007-08, 2008-09, 2009-10, and 2010-11 seasons according to _G_<sup>off</sup> , the offensive component of _APM_ in terms of goals per season. We also list the players’ offensive contributions according to the _APM_ models based on the other statistics. 

Recall that _S_<sup>off</sup> , _F_<sup>off</sup> , and _C_<sup>off</sup> have been rescaled by multiplying by the league average goals per shot, goals per Fenwick rating, and goals per Corsi rating, respectively. Note that these statistics are in the units of goals per season or expected goals per season based on shots, Fenwick, or Corsi, so they do depend on playing time. Sidney Crosby, for example, has missed significant time in two of the four seasons, and that has a big impact on his rating, although he still leads the league in _G_<sup>off</sup> by a sizeable margin. 

Some per 60 minute results, _G_<sup>off</sup> _EV,_ 60<sup>and</sup><sup>_S_</sup> _EV_<sup>off</sup> _,_ 60<sup>,alongwiththeirstandarder-</sup> rors, are given in the last four columns of that table. These statistics are independent of playing time, so they do not depend on how much their coaches play them. They also do not depend on how much time these players have spent on injured 

6 

Table 2: The top 10 offensive players in the NHL according to _G_<sup>off</sup> . 

|Player|Pos|Team|_G_<sup>off</sup>|_S_<sup>off</sup>|_F_<sup>off</sup>|_C_<sup>off</sup>|_G_<sup>off</sup><br>_EV,_60|Err|_S_<sup>off</sup><br>_EV,_60|Err|
|---|---|---|---|---|---|---|---|---|---|---|
|1 Sidney Crosby|C|PIT|23|12|13|14|0.83|0.20|0.42|0.07|
|2 Jonathan Toews|C|CHI|18|8|8|9|0.45|0.20|0.22|0.07|
|3 Alex Ovechkin|LW|WSH|17|17|20|24|0.46|0.18|0.45|0.07|
|4 Daniel Sedin|LW|VAN|16|13|13|15|0.47|0.18|0.44|0.08|
|5 Joe Thornton|C|S.J|16|11|11|15|0.34|0.18|0.26|0.06|
|6 Nicklas Backstrom|C|WSH|16|11|12|14|0.23|0.19|0.28|0.07|
|7 Evgeni Malkin|C|PIT|15|11|11|12|0.40|0.20|0.31|0.06|
|8 Ryan Getzlaf|C|ANA|15|6|8|9|0.31|0.19|0.07|0.07|
|9 Pavel Datsyuk|C|DET|15|10|11|12|0.53|0.19|0.27|0.07|
|10 Jason Spezza|C|OTT|13|7|8|9|0.37|0.21|0.25|0.07|



reserve. We believe that both the per season and per 60 minutes versions of these statistics have value, and we will continue to list both versions in our tables. 

In this paper, we will mostly give results based on models that contain data from four NHL seasons: 2007-08, 2008-09, 2009-10, and 2010-11. However, since we are now using ridge regression, single season results are stable enough to have value. One might prefer to see a player’s progression from season to season rather than seeing a single number for all four years. Also, one might prefer to make adjustments so that the statistics for a player are relative to a replacement player at the same position. An example of Sidney Crosby’s _APM_ statistics in each of the past four seasons, with adjustments for position and replacement players, is given in Table 3. We have also included his 4-year results for comparison. 

Table 3: Sidney Crosby’s _APM_ statistics over the past four seasons using <u>goals.</u> 

|Year|Age|GP|_G_<sup>off </sup>|G<sup>def</sup>|_G_|_G_<sup>off</sup><br>_EV _|<sup>_G_def</sup><br>_EV _|<sup>_G_</sup>_EV_|_G_<sup>off</sup><br>_PP _|<sup>_G_def</sup><br>_PP _|<sup>_G_</sup>_PP_|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2007|20|53|25|9|33|19|7|26|6|2|7|
|2008|21|77|30|3|33|21|2|23|9|1|10|
|2009|22|81|37|4|41|31|2|34|5|2|7|
|2010|23|41|17|1|18|13|0|13|3|1|5|
|4-yr|20-23|63|29|1|30|23|1|24|5|1|6|



We also note that the errors in our estimates are lower than those reported in Macdonald (2011a) and Macdonald (2011b), where the author used ordinary least squares (OLS) regression instead of ridge regression. As an example, we give Alex Ovechkin’s even strength offensive contributions per 60 minutes in Table 4, along with their standard errors. The errors in Ovechkin’s _G_<sup>off</sup> _EV,_ 60<sup>are smaller than</sup> those reported in Macdonald (2011a) and Macdonald (2011b). Also, the errors in 

7 

Ovechkin’s _SEV_<sup>off</sup> _,_ 60<sup>,</sup><sup>_F_</sup> _EV_<sup>off</sup> _,_ 60<sup>,and</sup><sup>_C_</sup> _EV_<sup>off</sup> _,_ 60<sup>are smaller than the errors in</sup><sup>_G_off</sup> _EV,_ 60<sup>.This</sup> trend can also be seen in Table 2. The standard errors in _S_<sup>offmuchlower</sup> _EV,_ 60<sup>are</sup> than the standard errors in _G_<sup>off</sup> _EV,_ 60<sup>for all of the players in that table.The errors are</sup> still not small enough to be ignored, as the confidence intervals of many of the estimates still overlap. Nevertheless, the _APM_ estimates with smaller error bounds, coupled with the additional _APM_ estimates based on shots, Fenwick rating, and Corsi rating, are useful metrics with which to analyze the performance of NHL players. 

Table 4: Alex Ovechkin’s EV offense statistics, with standard errors. 

|Player Pos|Team|_G_<sup>off</sup><br>_EV,_60|_Err_|_S_<sup>off</sup><br>_EV,_60|_Err_|_F_<sup>off</sup><br>_EV,_60|_Err_|_C_<sup>off</sup><br>_EV,_60|_Err_|
|---|---|---|---|---|---|---|---|---|---|
|Alex Ovechkin LW|WSH|0.46|0.18|0.45|0.07|0.53|0.06|0.63|0.05|



The rest of this paper is organized as follows. First, we describe the ridge regression models in detail in Section 2. In Section 3, we give the players that _APM_ determines as the Hart Trophy, Norris Trophy, and Selke Trophy finalists (most valuable player, best defensemen, and best defensive forward, respectively) during the 2007-08, 2008-09, 2009-10, and 2010-11 seasons combined. We finish with conclusions and future work in Section 4. In the Appendix, we give a brief comparison of ordinary least squares and ridge regression, and describe how we chose our ridge parameter in our ridge regression models. 

## **2 Ridge Regression Model** 

We now describe the setup of our model. We use information about the players on the ice during every shift of every game during the 2007-08, 2008-09, 200910, and 2010-11 seasons, as well as the outcome of each shift. We divide this data into even strength and special teams situations, and we remove empty net situations from both data sets. Each shift gives two lines of data: one line corresponding to the goals per 60 minutes scored by the home team, and one line corresponding to the goals per 60 minutes scored by the away team. Both of these observations are weighted by the duration of that shift. We denote the total number of observations by _N_ . For even strength, we have _N_ = 2 _,_ 324 _,_ 528 _,_ while for special teams situations, we have _N_ = 461 _,_ 022. We note that the average duration of a shift is 4.5 seconds longer for special teams than for even strength. Other observations about shift lengths and ice time for players, along with accompanying figures, can be found in Figures 4 and 5 the Appendix. 

Let _J_ denote the number of players in the league, let _y_ denote the goals (or shots, Fenwick rating, or Corsi rating) per 60 minutes during an observation, and 

8 

let _X j_ and _D j_ be indicator variables that are defined as follows: 



where 1 _≤ j ≤ J._ Note that by “skater” we mean a forward or a defensemen, but not a goalie. We also note that for the models which use goals, we included defensive variables for goalies. Let _Zo f f_ and _Zde f_ be indicator variables defined as follows: 





To clarify, we give an example. Suppose that in one shift, skaters 1-5 are on the ice for the home team, and skaters 6-10 are on the ice for the away team. Suppose that this is a shift of duration _t_ 1 seconds, and that the home team scores a goal during this shift. For this shift we would have two lines of data, one for goals per 60 minutes scored by the home team, and the second for goals per 60 minutes scored by the away team. These two rows of data would look like this: 



We note that<sup><u>1</u></sup> _t_ 1<sup>is in the units of goals per second, so we multiple by 3,600 to get</sup> goals per 60 minutes. For even strength situations, we start with the following linear model: 



The quantities of interest are the _β j_ s and _δ j_ s, which are player _j_ ’s offensive and defensive contributions, respectively, in terms of goals per 60 minutes. The coefficients _ζof f_ and _ζdef_ can be regarded as estimates of the value of starting a shift in the offensive or defensive zone, respectively, in terms of goals per 60 minutes. 

9 

For special teams situations, we start with a model that is similar to (3) and is described in Macdonald (2011b). In total, there are 8 models: an even strength model and a special teams model for each of the four statistics. 

A linear model like (3) can also be expressed as a system of linear equations in matrix form as 



where _y_ is an _N ×_ 1 vector of response variables, _X_ is an _N ×_ (2 _J_ + 3) matrix of the explanatory variables, and _β_ is an (2 _J_ + 3) _×_ 1 vector of coefficients, the quantities we are interested in. Typically, when the number of observations, _N_ , is much greater than the number of explanatory variables, 2 _J_ + 3, no solution to (4) exists, and one must find some sort of “best fit” solution. 

Instead of using OLS as in Macdonald (2011a) and Macdonald (2011b) to find the best fit, we use ridge regression. For the sake of those readers who are unfamiliar with ridge regression, we give a brief description of how to find the best fit estimates using OLS regression and ridge regression, and how the two methods are related, in the Appendix. We also discuss how we chose the ridge parameter _λ_ in that section. 

### **2.1 Differences in OLS and Ridge Estimates** 

The effect that this ridge parameter _λ_ has on the estimates can be seen in Figure 1. In this example, we plot the estimated coefficient for _G_<sup>off</sup> _PP,_ 60<sup>(offensive contri-</sup> bution on the power play in terms of goals per 60 minutes) of a few players in the league for different choices of _λ ._ Note that when _λ_ = 0, Pavel Datsyuk (solid red line) actually has a negative estimate, and Brandon Dubinsky (solid blue line) has a very high positive estimate in line with the league’s elite offensive players. Dubinsky is a valuable offensive player, but one would not expect his rating to be that much higher than Datsyuk’s rating or among the league’s elite. Also, we would not consider Datsyuk to be a below average player on the power play. We note that _λ_ = 0 corresponds to the ordinary least squares estimates, so these are the estimates we would have gotten for Dubinsky and Datsyuk if we had not used ridge regression. 

However, notice that for larger choices of _λ_ , the estimates begin to stabilize. Datsyuk’s estimate moves towards the estimates of the league’s elite players, while Dubinsky’s estimate returns to a more reasonable level. These estimates agree with most people’s intuition that Datysuk is an elite offensive player, while Dubinsky is an above average offensive player, but not an elite player as his ordinary least squares estimate suggested. 

For Dubinsky, the unexpected result for _λ_ = 0 is probably due to minimal playing time. For Datsyuk, it is probably due to the fact that he spent 90% of his 

10 



<!-- Start of picture text -->
Estimates of GoffPP vs λ<br>Pavel Datsyuk   C<br>Sidney Crosby   C<br>Alex Ovechkin   LW<br>Henrik Sedin   C<br>Daniel Sedin   LW<br>G Dubinsky's OLS estimate<br>Nicklas Lidstrom   D<br>Brandon Dubinsky   C<br>G Datsyuk's ridge estimate<br>G Dubinsky's ridge estimate<br>G Datsyuk's OLS estimate<br>0.0 0.5 1.0 1.5 2.0<br>λ<br>2.5<br>2.0<br>off PP 1.5<br>G<br>of<br>1.0<br>Estimate<br>0.5<br>0.0<br><!-- End of picture text -->

Figure 1: Estimates of _G_<sup>off</sup> _PP,_ 60<sup>for some players, for different values of</sup><sup>_λ_.</sup> 

power play time with one of his teammates, Nicklas Lidstrom. While Datsyuk’s estimate starts below zero for _λ_ = 0 and increases as _λ_ increases, Lidstrom’s estimate (dotted and dashed, light blue line) is off the figure near 4.0 for _λ_ = 0, and rapidly decreases as _λ_ increases. While we would expect Lidstrom to have a good offensive rating on the power play, 4.0 is unusually high, and the ridge regression seems to be tempering Lidstrom’s estimate while correcting Datsyuk’s. 

Datsyuk and Dubinsky are not the only players whose estimates exhibit this behavior. We give the tracecurves of the 25 players whose coefficients were the most positively (resp. negatively) affected by the ridge regression as the dotted (resp. solid) lines in Figure 2. In many cases, there are drastic changes in a player’s value relative the other players in the league. A player may be worth 1 goal per 60 minutes more than another player according to their OLS estimates ( _λ_ = 0) but worth 0.5 goals per 60 minutes _less_ according to their ridge estimates ( _λ_ = 0 _._ 5). 

### **2.2 Year-to-year correlations** 

We note that the ridge estimates tend to be more consistent from year to year than the OLS estimates. In Figure 3 we give three examples of year-to-year correlations for three of the components of _APM_ . In the left figure, we see that our ridge estimates for offense at even strength using goals tend to be more consistent 

11 



<!-- Start of picture text -->
Estimates of GoffPP vs λ<br>Risers<br>Fallers<br>1st percentile<br>99th percentile<br>0.0 0.1 0.2 0.3 0.4 0.5<br>λ<br>4<br>2<br>off PP<br>G<br>of<br>0<br>Estimate<br>−2<br><!-- End of picture text -->

Figure 2: Estimates of _G_<sup>off</sup> _PP,_ 60<sup>fordifferentvaluesof</sup><sup>_λ_forthe25playerswhose</sup> coefficients were the most positively (resp. negatively) affected by the ridge regression, plotted as dashed (resp. solid) lines. 

than the corresponding OLS estimates from Macdonald (2011a) (which also used goals). Also, the ridge estimates that use shots, Fenwick, and Corsi tend to be more consistent than the ridge estimates that use goals. 

In the middle figure, we see that these trends are true for power play offense as well. For short handed defense, the ridge estimates using goals are not more consistent than the OLS estimates, although the correlations for shots, Fenwick and Corsi are still higher. We note that, in general, the even strength estimates tend to have higher year-to-year correlations than the power play and short handed estimates. This trend is expected, since there is much less data for special teams situations than for even strength situations. 

## **3 Results** 

We now consider performance during the 2007-08, 2008-09, 2009-10, and 201011 seasons combined and determine the “four-year” Selke Trophy finalists (best defensive forwards), Norris Trophy finalists (best defensemen), and Hart Trophy finalists (most valuable players), according to _APM_ . Although the NHL typically announces three finalists for each trophy, we will give our top 5 finalists for each 

12 



<!-- Start of picture text -->
Year−to−year correlations of APM estimates Year−to−year correlations of APM estimates Year−to−year correlations of APM estimates<br> (EV offense)  (PP offense)  (SH defense)<br>0.63<br>0.56<br>0.47<br>0.44<br>0.36 0.39<br>0.34<br>0.28 0.26 0.26 0.29 0.3<br>0.22 0.21<br>0.18<br>OLS  Goals Shots Fenwick Corsi OLS  Goals Shots Fenwick Corsi OLS  Goals Shots Fenwick Corsi<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>Correlation Correlation Correlation<br>0.2 0.2 0.2<br>0.0 0.0 0.0<br><!-- End of picture text -->

Figure 3: A comparison of year-to-year correlations for OLS estimates (OLS) and our new ridge regression estimates (Goals, Shots, Fwick, Corsi). (Left) Even strength offense, minimum 500 minutes. (Middle) Power play offense, minimum 150 minutes. (Right) Short handed defense, minimum 150 minutes. To compute the correlations, the per 60 minutes versions of these statistics were used. 

award and discuss other notable players. 

### **3.1 Four-year Selke Trophy finalists for Best Defensive Forward** 

Each season, the Selke Trophy is awarded to the forward that “best excels at the defensive aspects of the game” NHL.com (2010). In practice, the award winner is typically a great defensive forward who contributes offensively as well. In Table 5, we give the top defensive forwards in the league during the 2007-08, 200809, 2009-10, and 2010-11 seasons according to _G_<sup>def</sup> . Recall that _S_<sup>off</sup> , _F_<sup>off</sup> , _C_<sup>off</sup> 

Table 5: The top 5 defensive forwards according to _G_<sup>def</sup> . 

|Player|Pos|Team|_G_<sup>def</sup>|_S_<sup>def</sup>|_F_<sup>def</sup>|_C_<sup>def</sup>|_G_<sup>def</sup><br>_EV,_60|Err|_S_<sup>def</sup><br>_EV,_60|Err|
|---|---|---|---|---|---|---|---|---|---|---|
|Pavel Datsyuk|C|DET|12|8|7|6|0.44|0.19|0.30|0.07|
|David Krejci|C|BOS|11|3|2|0|0.52|0.20|0.18|0.07|
|Chris Higgins|LW|VAN|10|0|_−_1|_−_2|0.33|0.21|0.03|0.07|
|Tomas Plekanec|C|MTL|10|_−_0|_−_1|_−_3|0.30|0.20|0.03|0.07|
|Mikko Koivu|C|MIN|9|3|3|3|0.53|0.21|0.20|0.08|



have been rescaled by multiplying by the league average goals per shot, goals per Fenwick rating, and goals per Corsi rating, respectively. Recall that these statistics are in the units of goals per season or expected goals per season based on shots, Fenwick, or Corsi. 

Pavel Datsyuk seems to be the clear choice as the best defensive forward in the NHL according to _APM_ . He is the league leader in all 4 flavors of defensive 

13 

contribution, and is also the best offensive player on the list. The voters seem to agree: Datsyuk was awarded the Selke Trophy in 2007-08, 2008-09, and 200910, and he was a finalist in 2010-11. Tomas Plekanec and Chris Higgins are on this list, but one might consider the next best candidates to be David Krejic and Mikko Koivu due to their superior ability to reduce the opposition’s shots, Fenwick rating and Corsi rating. Interestingly, multi-year finalist and 2010-11 winner Ryan Kesler is not on this list, although he did have very good numbers in 2010-11. We note that 5 other players were tied with Koivu for 5th in _G_<sup>def</sup> with 9 to round out the top 10 in that category. Daymond Langkow, who was 11th in _G_<sup>def</sup> with 8, missed the top 10 in _G_<sup>def</sup> , but was second in _S_<sup>def</sup> , and third in both _F_<sup>def</sup> and _C_<sup>def</sup> . In light of those rankings, Langkow could be considered one of the best defensive forwards in the game. 

### **3.2 Four-year Norris Trophy finalists for Best Defensemen** 

The James Norris Memorial Trophy is given each year to the defensemen who “demonstrates throughout the season the greatest all-round ability in the position” NHL.com (2010). In Table 6, we give the top defensemen in the league during the 2007-08, 2008-09, 2009-10, and 2010-11 seasons according to _G_ . It is not too 

Table 6: The top 5 defensemen during the last 4 seasons, according to _G_ . 

|Player|Pos|Team|_G_|_S_|_F_|_C _|_G_<sup>off</sup><br>_EV,_60|<sup>_S_off</sup><br>_EV,_60|<sup>_G_off</sup><br>_PP,_60|Err|_S_<sup>off</sup><br>_PP,_60|Err|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Zdeno Chara|D|BOS|19|9|9|10|0.10|0.21|0.43|0.33|0.58|0.07|
|Nicklas Lidstrom|D|DET|19|1|3|5|_−_0.06|0.07|1.37|0.26|0.71|0.05|
|Brian Campbell|D|CHI|14|7|7|8|0.12|0.16|0.23|0.36|0.32|0.08|
|Andrei Markov|D|MTL|13|_−_3|_−_1|1|0.20|0.13|1.75|0.37|0.59|0.08|
|Brian Rafalski|D|DET|13|9|8|11|_−_0.02|0.22|0.84|0.30|0.65|0.06|



surprising that Zdeno Chara and Nicklas Lidstrom were the best defenseman in the NHL during those seasons according to _G_ . Zdeno Chara’s _APM_ results based on shots, Fenwick rating, and Corsi rating are better than those of Lidstrom, so one might choose to select him as the best defenseman. Brian Campbell and Brian Rafalski are both strong across the board. Interestingly, Andrei Markov does not rate very well in the _APM_ estimates based on shots, Fenwick rating, and Corsi rating. One might prefer to include Chris Pronger, Dan Boyle, or Kris Letang instead of Markov on this list due to their ratings in _S, F_ and _C_ . Boyle, for example, led the league in _S_ , _F_ and _C_ . 

14 

### **3.3 Four-year Hart Trophy finalists for Most Valuable Player** 

The Hart Memorial Trophy is given each year to the player “judged to be the most valuable to his team” NHL.com (2010). Since _APM_ is not computed for goalies, we restrict our attention to only forwards and defensemen. Typically, the Hart Trophy winner is a forward, in part because defensemen and goalies already have a trophy dedicated to the best player at those positions. In Table 7, we list the top 5 players in the league according to _G_ . According to _G_ , Pavel Datsyuk was the 

Table 7: The top 5 players according to _G_ . 

|Player|Pos|Team|_G_|_S_|_F_|_C G_<sup>off</sup><br>_EV,_60|<sup>_S_off</sup><br>_EV,_60|<sup>_G_off</sup><br>_PP,_60|Err|_S_<sup>off</sup><br>_PP,_60|Err|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Pavel Datsyuk|C|DET|27|18|17|18<br>0.53|0.27|0.77|0.31|0.70|0.06|
|Jonathan Toews|C|CHI|24|11|10|11<br>0.45|0.22|1.67|0.34|0.79|0.07|
|Alex Ovechkin|LW|WSH|24|18|19|23<br>0.46|0.45|0.87|0.26|0.84|0.05|
|Daniel Sedin|LW|VAN|23|16|16|17<br>0.47|0.44|1.11|0.26|0.73|0.06|
|Sidney Crosby|C|PIT|22|11|12|12<br>0.83|0.42|0.98|0.29|0.58|0.06|



most valuable player in the league during the four seasons in question thanks to his excellent two-way play. Datsyuk is also tied for first in _S_ and is third in _F_ and _C_ . 

Given the number of shots that Ovechkin throws at the net, it is not surprising that he is the leader in _S, F,_ and _C_ , as well as the corresponding offensive components _S_<sup>off</sup> _, F_<sup>off</sup> _,_ and _C_<sup>off</sup> . Ovechkin and Daniel Sedin have each won the Hart Trophy during the past four years, while Jonathan Toews has been a consistently excellent two-way player. Toews has been a Selke finalist and a Conn Smythe trophy winner for the best player in the playoffs. Unfortunately, Crosby missed significant time because of injury in two of the seasons that are used in this model. Despite the injuries, Crosby still rates as the top offensive player in the league according to _G_<sup>off</sup> , as we saw earlier in Table 2. 

## **4 Conclusions and Future Work** 

The use of ridge regression, and the addition of adjusted plus-minus models based on shots, Fenwick rating, and Corsi rating, are two valuable modifications of the earlier _APM_ models in hockey. Other modifications could prove useful as well. Different estimation techniques, such as that in Thomas et al. (2012), could be used. Different outcome variables could also be used. 

For example, one could also consider using weighted shots as the response variable in an _APM_ model. By “weighted shots” we mean the following. We could estimate the probability that a shot on goal will be a goal using distance, 

15 

type of shot, and other details as explanatory variables. Such shot quality models have been developed by Ken Krzywicki in Krzywicki (2005), Krzywicki (2009), and Krzywicki (2010) and Michael Schuckers in Schuckers (2011). Then, each shot can be weighted based on the probability that it will be a goal. In a forthcoming article Macdonald et al., the authors create a shot quality model similar to Krzywicki’s logistic regression models, and use the resulting weighted shots as the outcome variable in a ridge regression model similar to the one described in this paper. The results of this model are estimates of _W_ , an adjusted plus-minus rating based on weighted shots. 

Also, recall that Fenwick rating and Corsi rating are combinations of shots, missed shots, and blocked shots, and are a good indication of possession advantage and team performance in general. One could build on the idea of using those statistics and consider other statistics like hits, faceoffs, and zone starts as well. In Macdonald (2012), the author estimates the combinations of these statistics are the best predictors of goal scoring at the team level. The results of the model can be interpreted as “expected goals”. These expected goals are then used as the outcome in a ridge regression similar to the model described in this paper. The results are estimates of _E_ , an adjusted plus-minus rating based on expected goals. Another approach that uses several different statistics can be found in Schuckers et al. (2011). 

We hope that the ideas presented in this paper will be useful to fans, analysts, coaches and teams as they analyze the performance of NHL players, and will inspire future work in performance analysis in hockey. 

## **Acknowledgements** 

I would like to thank William Pulleyblank for many useful conversations about this work and for his comments and suggestions after reading a draft of the paper. I would also like to thank the referees for many comments and suggestions that improved the quality of this paper. 

## **References** 

- Bretscher, O. (2009): _Linear Algebra with Applications_ , Pearson Prentice Hall, 4th edition. 

- Fearnhead, P. and B. M. Taylor (2011): “On estimating the ability of nba players,” _Journal of Quantitative Analysis in Sports_ , 7, 11, URL `http://EconPapers.repec.org/RePEc:bpj:jqsprt:v:7: y:2011:i:3:n:11` . 

16 

- Ferrari, V. (2009): “Possession is Everything,” `http://vhockey.blogspot. com/2009/05/possession-is-everything.html` , Accessed 09-162011. 

- Girard, D. (1991): “Asymptotic optimality of the fast randomized versions of _GCV_ and _CL_ in ridge regression and regularization,” _Ann. Statist._ , 19, 1950–1963. 

- Hoerl, A. E. (1962): “Application of ridge analysis to regression problems,” _Chemical Engineering Progress_ , 58, 54?59, URL `http: //scholar.google.com/scholar?hl=en&btnG=Search&q=intitle: Application+of+ridge+analysis+to+regresion+problems#0` . 

- Hoerl, A. E., R. W. Kannard, and K. F. Baldwin (1975): “Ridge regression:some simulations,” _Communications in Statistics_ , 4, 105–123, URL `http:// www.tandfonline.com/doi/abs/10.1080/03610927508827232` . 

- Hoerl, A. E. and R. W. Kennard (1970): “Ridge regression: Biased estimation for nonorthogonal problems,” _Technometrics_ , 12, 55–67. 

- Hutchinson, M. (1989): “A stochastic estimator of the trace of the influence matrix for Laplacian smoothing splines,” _Commun. Stat. Simula._ , 18, 1059–1076. 

- Ilardi, S. and A. Barzilai (2008): “Adjusted Plus-Minus Ratings: New and Improved for 2007-2008,” `http://www.82games.com/ilardi2.htm` . 

- JLikens (2011): “Shots, Fenwick and Corsi,” `http://objectivenhl. blogspot.com/2011/02/shots-fenwick-and-corsi.html` , Accessed 09-03-2011. 

- Krzywicki, K. (2005): “Shot Quality Model: A logistic regression approach to assessing NHL shots on goal,” `http://www.hockeyanalytics.com/ Research_files/Shot_Quality_Krzywicki.pdf` . 

- Krzywicki, K. (2009): “Removing Observer Bias from Shot Distance - Shot Quality Model - NHL Regular Season 200809,” `http://www.hockeyanalytics.com/Research_files/ SQ-DistAdj-RS0809-Krzywicki.pdf` . 

- Krzywicki, K. (2010): “NHL Shot Quality 2009-10: A look at shot angles and rebounds,” `http://hockeyanalytics.com/2010/10/ nhl-shot-quality-2010/` . 

17 

- Kutner, M. H., C. J. Nachtsheim, and J. Neter (2004): _Applied Linear Regression Models_ , McGraw-Hill/Irwin, fourth international edition, URL `http://www.amazon.com/exec/obidos/redirect?tag= citeulike07-20&path=ASIN/0072955678` . 

- Lay, D. (2006): _Linear Algebra and its Applications (Third edition)_ , Pearson, Addison Wesley. 

- Lewin, D. (2007): “2004-2005 Adjusted Plus-Minus Ratings,” `http://www. 82games.com/lewin3.htm` . 

- Macdonald, B. (2011a): “A Regression-Based Adjusted Plus-Minus Statistic for NHL Players,” _Journal of Quantitative Analysis in Sports_ , 7, 29, URL `www.bepress.com/jqas/vol7/iss3/4/` . 

- Macdonald, B. (2011b): “An Improved Adjusted Plus-Minus Statistic for NHL Players,” _Proceedings of the MIT Sloan Sports Analytics Conference_ , URL `http://www.sloansportsconference.com/?p=2838` . 

- Macdonald, B. (2012): “An Expected Goals Model for Evaluating NHL Teams and Players,” _Proceedings of the 2012 MIT Sloan Sports Analytics Conference_ , `http://www.sloansportsconference.com/?p=6157` , Accessed 2-20-2012. 

- Macdonald, B., C. Lennon, and R. Sturdivant (????): “Evaluating NHL Goalies, Skaters, and Teams Using Weighted Shots,” _In preparation_ . 

- Marquardt, D. W. (1970): “Generalized inverses, ridge regression, biased linear estimation, and nonlinear estimation,” _Technometrics_ , 12, 591–612, URL `http://www.jstor.org/stable/1267205?origin=crossref` . 

- NHL.com (2010): “The official website of the National Hockey League,” `http: //www.nhl.com/` . 

- Rosenbaum, D. (2004): “Measuring How NBA Players Help Their Teams Win,” `http://www.82games.com/comm30.htm` . 

- Schuckers, M. (2011): “DIGR: A Defense Independent Rating of NHL Goaltenders using Spatially Smoothed Save Percentage Maps,” `http://www. sloansportsconference.com/?p=648` . 

- Schuckers, M. E., D. F. Lock, C. Wells, C. J. Knickerbocker, and R. H. Lock (2011): “National Hockey League Skater Ratings Based upon All On-Ice Events: An Adjusted Minus/Plus Probability (AMPP) Approach,” `http://myslu.stlawu.edu/~msch/sports/ LockSchuckersProbPlusMinus113010.pdf` . 

18 

- Sill, J. (2010): “Improved NBA Adjusted +/- Using Regularization and Out-ofSample Testing,” _Proceedings of the 2010 MIT Sloan Sports Analytics Conference_ . 

- Strang, G. (1988): _Linear Algebra and Its Applications_ , Brooks Cole, URL `http://www.amazon.ca/exec/obidos/redirect?tag= citeulike09-20{&}path=ASIN/0155510053` . 

- Thomas, A. C., S. L. Ventura, S. Jensen, and S. Ma (2012): “Competing Process Hazard Function Models for Player Ratings in Ice Hockey,” _ArXiv preprint:_ _`http: // arxiv. org/ abs/ 1205. 1746` , accessed 8-25-2012._ 

- Winston, W. L. (2009): _Mathletics: how gamblers, managers, and sports enthusiasts use mathematics in baseball, basketball, and football_ , Princeton University Press. 

- Witus, E. (2008): “Count the Basket,” `http://www.countthebasket.com/ blog/` . 

## **5 Appendix** 

### **5.1 Ordinary Least Squares** 

To find the “best fit” solution of (4) using ordinary least squares (OLS) regression, one finds the _β j_ s, _δ j_ s, and _ζ_ s that minimize the sum of squared error 



where _y_ ˆ _i_ is the predicted outcome for observation _i_ and is given by 





In matrix notation, the sum of squared error _Q_ in (5) can be written 



where ( _y − Xβ_ )<sup>_T_</sup> denotes the transpose of _y − Xβ_ . Equivalently, finding the least squares estimates of _β_ amounts to finding the _β_<sup>ˆ</sup> that solves the system 



19 

which is obtained by multiplying both sides of (4) by _X_<sup>_T_</sup> on the left. When there is only one predictor variable, finding _β_<sup>ˆ</sup> can be thought of as finding the line that best fits the data. With two predictor variables, one finds the plane that best fits the data. With more than two variables, the case we have in this paper, one finds the best fit hyperplane. 

If the kernel (or nullspace) of _X_ is 0, which is typically true when _N >> J_ , then _X_<sup>_T_</sup> _X_ is invertible, and we can solve for _β_<sup>ˆ</sup> by multiplying both sides of (8) by ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> on the left, giving 



Further details about OLS from a linear algebraic point of view can be found in most standard undergraduate linear algebra textbooks (for example, Strang (1988), Bretscher (2009), or Lay (2006)) or a multiple linear regression textbook (for example, Kutner et al. (2004)). 

Ordinary least squares was the approach taken in Macdonald (2011a) and Macdonald (2011b) and several of the basketball articles. Unfortunately, collinearity in _X_ results in high standard errors for _β_<sup>ˆ</sup> . A linear algebraist might prefer the viewpoint that if two teammates play together often, then two columns of _X_ are nearly the same, the columns of _X_ are nearly linearly dependent, and the corresponding columns (and rows) _X_<sup>_T_</sup> _X_ are nearly linearly dependent, which means that _X_<sup>_T_</sup> _X_ is nearly singular and has a high condition number. A high condition number means that solutions to (8) are sensitive to small changes in the data, an undesirable property. It also leads to large standard errors in the estimates of _β ._ 

### **5.2 Ridge Regression** 

In ridge regression, instead of finding the _β_ that minimizes (7), one standardizes the columns of _X_ and finds the _β_ that minimizes 



where _λ_ is a ridge parameter that needs to be chosen. Note that (9) is similar to (7) but with the penalty term _λβ_<sup>_T_</sup> _β_ included. Equivalently, instead of solving (8) for _β_<sup>ˆ</sup> , one solves the equation 



for _β_<sup>ˆ</sup> , where _I_ denotes the identity matrix. Note that (11) is similar to (8) but with the penalty term _λ I_ included. 

To solve (11), one multiples both sides of the equation by ( _X_<sup>_T_</sup> _X_ + _λ I_ )<sup>_−_1</sup> on the left, which gives 



20 

These estimates _β_<sup>ˆ</sup> are the estimates that we use in the next section to evaluate players. The interpretation of _β_<sup>ˆ</sup> is the same for ridge regression as it was with OLS regression. In our case, coefficients _β_<sup>ˆ</sup> are estimates of the offensive and defensive contributions of players in terms of goals per 60 minutes, independent of the strength of their teammates and opponents, and independent of the zone in which their shifts begin. 

The effect of the penalty term is to penalize large values for the coefficients _β_ . Ridge regression can be thought of like OLS regression, which finds the “best fit” hyperplane, but with constraints on the coefficients _β_ that prevent them from being poorly behaved. Note that for the choice _λ_ = 0, (9) becomes (7), and (11) becomes (8), so _λ_ = 0 in ridge regression corresponds to the ordinary least squares estimates, where the coefficients are unconstrained and may have high error bounds. As _λ_ increases, the coefficients tend to stabilize and move toward zero. 

We remark that including the penalty term _λ I_ in (11) can seem somewhat ad hoc or arbitrary, but fortunately there is a nice Bayesian justification for this approach. The ridge regression model (11) is equivalent to a Bayesian regression model in which the coefficients _β_ are given a normal prior distribution with mean 0 and a variance that depends on _λ_ . Changing _λ_ corresponds to changing how influential the mean 0 prior will be on the value of the estimates. From a linear algebra perspective, the term _λ I_ is effectively padding the diagonal of _X_<sup>_T_</sup> _X_ , which lowers its condition number, and makes the solutions _β_<sup>ˆ</sup> less volatile. 

### **5.3 Choosing** _λ_ 

Often, the ridge parameter _λ_ is chosen using cross-validation. With large data, specifically when _n_ , the number of rows, is large, computing _λ_ in this way can be computationally expensive, as it requires one to compute _n_ leave-one-out estimates. Another alternative is generalized cross-validation (GCV), which is also computationally expensive. To see why, consider the hat matrix 



Finding _H_ , or the trace of _H_ , is a required step for GCV. If _X_ has _n_ rows, then _H_ is an _n_ -by- _n_ matrix. For our even strength model, for example, we have well over 1,000,000 rows, meaning _H_ is a 1,000,000 by 1,000,000 matrix. 

In our work, we use an estimate of the trace of _H_ to get a randomized version of GCV simliar to that in Girard (1991). This method uses the following lemma given in Hutchinson (1989): 

**Lemma** (Hutchinson (1989)) **.** _Let B be an n × n symmetric matrix and let u_ = ( _u_ 1 _,..., un_ )<sup>_T_</sup> _be a vector of n independent samples from a random variable U with mean 0 and variance σ_<sup>2</sup> _. Then,_ 



21 

Note that _E_ ( _·_ ) denotes expectation and tr( _·_ ) denotes the trace of a matrix. The hat matrix _H_ is symmetric, so the lemma applies. The lemma is useful because <u>1</u><sup>iseasiertocomputethantr(</sup><sup>_H_),and</sup> <u>1</u><sup>isanunbiasedestimate</sup> _σ_<sup>2</sup><sup>_εTHε_</sup> _σ_<sup>2</sup><sup>_εTHε_</sup> for tr( _H_ ) according to the lemma. Also, the estimate is very accurate (see, for example Girard (1991) or Hutchinson (1989)). 

Note that using (13) and (12) we can write 



and since matrix multiplication is associative, we can group the terms in 



in any order. We can write (14) as 



Note that if _X_ is an _n × p_ matrix and _ε_ is an _n ×_ 1 matrix, then 



so our biggest matrix is _p × p_ . Since typically _p << n_ when _n_ is very large, it is much easier to work with a _p × p_ matrix than an _n × n_ matrix. In our case, for example, _n_ is on the order of 1,000,000, while _p_ is on the order of only 1,000. We used the estimate for the trace in (15) to obtain a randomized GCV choice for _λ_ as in Girard (1991). 

In some cases, we preferred to increase the value of _λ_ obtained by this method. This change can be justified in several ways. For example, in some cases, inspection of the trace curves (that is, the curves like those in Figure 1) revealed that the estimates did not yet appear to be stabilized at those values of _λ_ , and this observation can be used to justify increasing _λ ._ We also considered the HoerlKannard-Baldwin estimate Hoerl et al. (1975) of _λ_ . The Hoerl-Kennard-Baldwin estimate is given by 



where MSE denotes mean-squared error. Finally, we considered variance inflation factors (VIF), which quantify the level of collinearity present in the data, when choosing _λ ._ As stated in Marquardt (1970), the VIF can be expressed as the diagonal elements of 



22 

Typically, values in the single digits are preferred. Often the VIF were high for the values of _λ_ that we got using GCV. We chose _λ_ at least high enough so that the VIF were below 10. 

These four pieces of information were considered when choosing _λ_ for each of our 8 models that used 4 seasons of data from the 2007-08 through 2010-2011 seasons. We also used this information with models that only used a single season’s worth of data, giving 8 more values of _λ_ for each season. In each case, we chose the highest value of _λ_ suggested by these four methods. These values of _λ_ were used in (11) to obtain estimates of the coefficients in each of our models. The vertical line at _λ_ = 0 _._ 5 in Figure 1 indicates the value of _λ_ that we chose for that model. Note that the estimates seem to have stabilized for the most part by the time _λ_ reaches 0.5. 

### **5.4 Supplemental figures** 



<!-- Start of picture text -->
Histogram of shift lengths on the power play Histogram of shift lengths when a PP goal is scored<br>0 20 40 60 80 100 120 0 20 40 60 80 100 120<br>Shift length in seconds Shift length in seconds<br>60000 500<br>50000<br>400<br>40000<br>300<br>30000<br>Frequency 20000 Frequency 200<br>10000 100<br>0 0<br><!-- End of picture text -->

Figure 4: A comparison of the shift lengths during power play situations for all shifts (left) and only shifts during which a goal is scored (right). Typically, shift lengths are longer for the shifts when a goal is scored. This observation is similar to that made by (Thomas et al., 2012, Figure 6) for even strength situations. 

23 



<!-- Start of picture text -->
Histogram of even strength ice time for players Histogram of power play ice time for players<br>0 2000 4000 6000 8000 10000 12000 14000 500 1000 1500 2000<br>Minutes Minutes<br>350<br>300 200<br>250<br>150<br>200<br>Frequency 150 Frequency 100<br>100<br>50<br>50<br>0 0<br><!-- End of picture text -->

Figure 5: Distribution of players’ ice time during even strength (left) and power play (right) situations. The small grouping of players with more than 10,000 minutes of even strength playing time are all goalies. 

24 


