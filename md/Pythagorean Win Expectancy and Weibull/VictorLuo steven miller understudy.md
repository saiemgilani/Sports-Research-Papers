<!-- source: Pythagorean Win Expectancy and Weibull/VictorLuo steven miller understudy.pdf -->

## RELIEVING AND READJUSTING PYTHAGORAS 

IMPROVING THE PYTHAGOREAN FORMULA 

by 

VICTOR LUO 

STEVEN J. MILLER, ADVISOR 

A thesis submitted in partial fulfillment 

of the requirements for the 

Degree of Bachelor of Arts with Honors in Mathematics 

WILLIAMS COLLEGE Williamstown, Massachusetts 

May 20, 2014 

### ABSTRACT 

The Pythagorean expectation was invented by Bill James in the late 70’s as a way of calculating how many wins a baseball team should have by utilizing just runs scored and _<u>RS</u>_<sup>2</sup> runs allowed. His original formula predicts a winning percentage of _RS_<sup>2</sup> + _RA_<sup>2,where</sup><sup>_RS_</sup> stands for runs scored and _RA_ stands for runs allowed. Although the simplicity of the formula is a thing of beauty, with the development of more advanced baseball statistics it should be possible to enhance the formula such that it gives a more accurate prediction of a team’s wins. Implementing statistics such as ballpark effect as well as accounting for game state factors, we will test to see if it is indeed the case that adjusting the Pythagorean expectation formula gives a statistically significantly better prediction for a team’s wins than the unadjusted formula. 

In order to test these adjusted formulas, we will be culling data from the internet, specifically from http://www.retrosheet.org/gamelogs/index.html and espn. com. We will then import this data into _R_ and use our code to manipulate the data, calculating the new adjusted Pythagorean expectation and old Pythagorean expectation by year for each team. Then, using different regression models, we will determine which expectation formula is more accurate. 

In addition, it has been shown that we can use a Weibull distribution in order to model run production. The versatility of the distribution is due to the fact that it accounts for three parameters that can be varied to adjust the spread, shift, and scale of the distribution. We will explore whether a linear combination of Weibulls is able to more accurately determine a team’s run production. 

1 

### ACKNOWLEDGEMENTS 

First and foremost, I would like to thank my thesis advisor, Professor Steven J. Miller. Without his assistance and enduring support throughout the time of research and writing of this thesis, I would not have been able to complete this thesis. I could not have asked for a better and more involved advisor for my undergraduate thesis. 

I would also like to thank my second reader, Professor Qing Wang, for her encouragement and time in reading my thesis, as well as her meticulous and insightful comments. 

Last but not least, I would like to thank my friends and family: my parents Tie Luo and Ching Hua, my brother Lawrence Luo, my teammates on WUFO, and those that I have met and become close with in my four years at Williams. Their support has meant the world to me, and without it, the road would have been that much tougher in completion of this thesis. 

2 

### CONTENTS 

|1.|Introduction|4|
|---|---|---|
|1.1.|The History of the Pythagorean Win/Loss Formula|4|
|1.2.|Previous Findings|4|
|1.3.|Thesis Results|5|
|1.4.|Outline of the Thesis|5|
|2.|Preliminaries|6|
|2.1.|The Weibull Distribution|6|
|2.2.|Culling Data from the Internet|8|
|3.|Adjusting for Sabermetric Statistcs|10|
|3.1.|Ballpark Effect Trends|10|
|3.2.|Game State|13|
|3.3.|Sabermetric Statistics Considered|17|
|3.4.|Standardizing WAR|19|
|4.|Linear Combinations of Weibulls|23|
|4.1.|Linear Combination of Weibulls|23|
|4.2.|Moments Analysis|25|
|4.3.|Least Squares|26|
|4.4.|A Simpler Formula?|35|
|App|endix A.<br>2011 Game State Code|36|
|App|endix B.<br>2011 WHIP Code|40|
|App|endix C.<br>2011 WAR Code|45|
|App|endix D.<br>2007 Moments Code for_R_|51|
|App|endix E.<br>2011 Least Squares Code|52|
|Refe|rences|66|



3 

### 1. INTRODUCTION 

1.1. **The History of the Pythagorean Win/Loss Formula.** Bill James first started writing about baseball statistics as a security guard at a cannery. His writings contrasted to contemporary baseball pieces, which instead recounted games in meticulous detail. In order to expand his audience, James published his _Baseball Abstract_ in 1977, which had nearly one hundred pages of comprehensive analysis of data and statistics James compiled from the 1976 season. One of these statistics was the Pythagorean Win/Loss Formula. The Pythagorean Win/Loss Formula, also known as the Pythagorean formula or Pythagorean expectation, was invented by James in order to predict how many wins a baseball team should have won, given their runs scored and runs allowed. The original formula is given as 

### runs scored<sup>_γ_</sup> 

Win/Loss Percentage = runs scored<sup>_γ_</sup> + runs allowed<sup>_γ_.</sup> 

To find the expected number of wins, one only need multiply the team’s Win/Loss Percentage by the number of games the team played in the season. _γ_ was initially taken to be 2, but through analysis on observed runs scored and allowed, a _γ_ of 1.83 produces a more accurate Win/Loss Percentage. One is taken back by how simple the formula is, requiring only the runs scored and allowed by a team in a season, and the calculation can be done on any calculator. This simple, closed form expression of a team’s Win/Loss Percentage of only three parameters allows for easy calculations. However, having such a simple formula certainly has its drawbacks, most notably it cannot address all the subtleties and issues that come with a complicated game like baseball. 

1.2. **Previous Findings.** [MIL] and [MCGLP] provided theoretical justification for the Pythagorean W/L Formula by modeling runs scored and allowed by independent Weibull distributions. It was established that the single Weibull distribution did a very good job of mapping runs scored and allowed, and lead to a predicted win-loss percentage of 



where _RS_ and _RA_ are the means of the Weibull random variable corresponding to runs scored and allowed, respectively, while _RS − β_ and _RA − β_ are estimators of the observed runs scored and allowed. Analysis on the 14 American League teams from the 2004 season showed that runs scored and allowed were statistically independent and that the single Weibull with best fit parameters obtained from the maximum likelihood method and least squares method provide good fits for the observed data. 

4 

1.3. **Thesis Results.** Adjusting runs for certain sabermetric statistics that are discussed in Section 3 does not seem to increase the accuracy of the Pythagorean W/L Formula. Accuracy testing was done in _R_ , and the code used for each statistic is displayed in the Appendices. However, it was found that using a linear combination of Weibulls rather than a single Weibull increases the prediction accuracy of a team’s W/L percentage. More specifically, using Mathematica on the years from 2004-2012, we saw that the single Weibull’s predictions for a team’s wins were on average 4.22 games off (with a standard deviation of 3.03), while the linear combination of Weibull’s predictions for a team’s wins were from 2004-2012 were on average 3.11 games off (with a standard deviation of 2.33), producing about a 25% increase in prediction accuracy. We also compare our results to ESPN’s Expected WL and comment. Finally, we perform _χ_<sup>2</sup> goodness of fit tests for the linear combination of Weibulls and test the statistical independence of runs scored and allowed (a necessary assumption), and see that in fact the linear combination of Weibulls with properly estimated parameters obtained from least squares analysis closely maps the observed runs and that runs scored and allowed are in fact statistically independent. 

1.4. **Outline of the Thesis.** In this paper, we will first present preliminaries needed, notably the Weibull distribution and the method of culling data from the internet. We will then analyze whether the prediction accuracy of the Pythagorean W/L Formula when the runs scored and allowed are adjusted for various sabermetric statistics increases as these statistics are added in. Finally, we extend the work done in [MIL]; namely, we will see if a linear combination of Weibulls is a more precise model in mapping runs. 

5 

2. PRELIMINARIES 

In this section, we present the Weibull distribution, which will be utilized in great amounts later on. In addition, we also analyze tools that were used in order to test these statistics, and give a glimpse into the code that was written to experiment with these statistics. 

2.1. **The Weibull Distribution.** The Pythagorean Formula is given by _RSobs_<sup>_~~γ~~_</sup> _RS_<sup>+</sup> _<u>obs</u>_<sup>_γRA_</sup><sup>_~~γ~~_</sup> _obs_<sup>, where</sup> _γ_ is constant throughout the league. To give a theoretical justification for the Pythagorean Formula and a value of _γ_ , the number of runs scored and allowed in baseball games can be modeled as independent random variables taken from Weibull distributions with the same _β_ and _γ_ by different _α_ ; the probability density of the Weibull distribution is given by 



Using a single Weibull model leads (see [MIL]) to a predicted won-loss percentage of 

Won-Loss Percentage( _RS_ , _RA_ , _β_ , _γ_ )= ( _RS−_ <u>(</u> _βRS_ )<sup>_γ_</sup> +( _−βRA_ <u>)</u><sup>_γ_</sup> _−β_ )<sup>_γ._</sup> 

It is important to note that we assume that runs scored and allowed are taken from continuous, not discrete, distributions. This allows for us to deal with continuous integrals rather than discrete sums, which most of the time leads to easier calculations. While a discrete distribution would probably more effectively map runs in baseball, the assumption of drawing runs from a continuous distribution allows for more manageable calculations, and is a very sensible estimate of those runs observed. It also will lead to closed form expressions, which are much easier to work with. Weibulls lead to significantly easier calculations because if we have a random variable _X_ chosen from a Weibull distribution with parameters _α_ , _β_ , and _γ_ , it is the case that _X_<sup>1</sup><sup>_/γ_</sup> is exponentially distributed with parameter _α_<sup>_γ_</sup> ; thus, a change of variables will lead to a much simpler integral of exponentials, which will be able to be done in closed form (see Appendix 9.1 in [MCGLP]). 

The choice of the Weibull distribution is natural, as it takes on three flexible parameters which allow for wide and various shapes of the distribution, and given the almost random and erratic behavior of runs, it is fitting to choose a distribution with such a dynamic and malleable nature. _α_ determines the spread of the distribution, namely as _α_ increases, the distribution becomes more spread out. In addition, _γ_ , arguably the most important of the parameters, causes the distribution to have many varying shapes. This is demonstrated in Figure 1. Finally, _β_ shifts the distribution along the real line. 

6 



FIGURE 1. The varying distributions of the Weibull family with _α_ = 1 and _β_ = 0. 

One other important assumption we will make is that _β_ = _−_ 1 _/_ 2 for a particular Weibull. Fixing _β_ , along with _γ_ , we can determine _α_ so that the mean of our Weibull closely resembles those of the observed average runs scored/allowed per game (see (2.3)). Using the Method of Least Squares, we can find the best fit parameters _α_ , _β_ , and _γ_ for the observed data. The choice of _β_ = _−_ 1 _/_ 2 breaks the data into bins 



so that the centers of the bins are integer values 0,1, 2, and so on. These are the possible scores in a baseball game, taking _β_ = _−_ 1 _/_ 2 causes the possible integers scores to be in the middle of each bin, which will lead to the least amount of issues in determining the best fit values. 

Our final assumption is that runs scored and runs allowed are independent. This obviously cannot be true, as a baseball game never ends in a tie. So, if the Rangers and Angels are playing, if the Angels scored 4 runs, then the Rangers must have scored something other than 4 runs. However, analyzing the data shows that these issues will cancel each other out on average, and that runs score and allowed will tend to behave like they are statistically 

7 

independent if the runs scored and allowed are different. This can be shown by constructing an independence test with structural zeros, namely values in the contingency table that are not accessible (see Appendix 9.2 in [MCGLP] for a more rigorous description of the method). 

To end this section, we state the mean and variance of the Weibull distribution in a lemma, which will be used heavily later on in the thesis: 

**Lemma 2.1.** _The mean, µα,β,γ, is given by_ 



_while the variance, σ_<sup>2</sup> _α,β,γ_<sup>_, is given by_</sup> 



_∞ where_ Γ( _x_ ) _is the Gamma function, defined as_ Γ( _x_ ) = �0<sup>_e−uux−_1</sup><sup>_du._</sup> 

A derivation of the mean can be seen in Appendix 9.1 in [MCGLP]; the derivation of the variance follows in a similar fashion. 

2.2. **Culling Data from the Internet.** An important component of this thesis was having the ability to cull data from the internet, namely bringing in many large data sets from the internet of player and team statistics. Without this power, it would nearly impossible to be able to test different formulas. Two main programs were used, namely _R_ and a program written by Kevin Dayaratna. 

In _R_ , the main packages used were “XML" and “RCurl". First, the years were put into their own vector, as was the three letter abbreviation of each team. Then, for each team, in a given year, the url from baseball-reference was assigned. For example, if we were considering the Red Sox in the year 2008, the url would be http://www. baseball-reference.com/teams/BOS/2008-pitching.shtml. Then, using the command _rawPMI <- readHTMLTable_ (url), the various tables on the page of the url are assigned to the variable _rawPMI_ . Each table is given it’s own name, and to call a table, say the table _players.pitching_ , we need only enter _rawPMI$players.pitching_ . This process can be seen in Figure 2. After this data is culled, it is very easy to manipulate it in _R_ game by game, which allows for a wider range of sabermetric statistics to be used. 

The second program, written by Kevin Dayaratna, only requires the three letter abbreviation of a team and a year. 

8 



### FIGURE 2. Culling data from the internet using _R_ . 

Previewed in Figure 3, it writes that team’s runs scored and runs allowed for that year to a text document in two columns, where the first column is runs scored and the second is runs allowed, taking the data from the baseball-almanac website. This was important in bringing in runs scored and allowed into Mathematica; we will discuss the importance of Mathematica later on in the paper. 



FIGURE 3. Kevin Dayaratna’s Baseball Almanac program. 

It cannot be stressed enough how important the ability to cull data from the internet is. Without it, there would be much more time spent collecting data rather than analyzing data. 

9 

### 3. ADJUSTING FOR SABERMETRIC STATISTCS 

In this section, we analyze possible sabermetric statistics that can be used to adjust the Pythagorean W/L Formula to potentially increase its accuracy. 

3.1. **Ballpark Effect Trends.** One statistic that is easily accessible and has an obvious effect on runs is ballpark factors. Ballpark factor is calculated as 

### <u>(Runs Scored at Home + Runs Allowed at Home)/(Number of Home Games)</u> 

(Runs Scored Away + Runs Allowed Away)/(Number of Away Games) 

. 

A stadium with a ballpark factor over 1 (labeled as “hitter friendly”), such as Coors Field, home of the Colorado Rockies, indicates that the team has more overall runs at home than away, while a stadium with a ballpark factor under 1 (labeled as “pitcher friendly”) indicates that the team has less overall runs at home than away. It is apparent that ballpark factor can be a misleading statistic, as it does not account for pitching. If a team has a below average pitching staff, it could seem like the team’s ballpark is “hitter friendly”, as the team’s pitchers are increasing the overall runs, namely by allowing more runs at home, causing the ballpark factor to increase. Figure 4 details the trends of ballpark factors from 2005 to 2012 (as listed on espn.com): 



FIGURE 4. Ballpark factors from 2005-2012. 

10 

While a team’s ballpark factor should be fairly constant over the years, there are a few teams that seem to defy this logic. Taking a closer look, four teams stand out, namely the Colorado Rockies (COL), New York Yankees (NYA), New York Mets (NYN), and Texas Rangers (TEX). Mapping their ballpark factor trends produces Figure 5. 



FIGURE 5. Anomaly ballpark factors from 2005-2012. 

Each anomaly team’s peculiar ballpark factor behavior can be attributed to a cause. In 2012, the Rockies allowed an absurd 890 runs, over 100 more than they did in 2011. With their already high ballpark factor, it should come as a surprise that a majority of the influx of runs allowed were at home, thus inflating the ballpark factor even more. From 2005 to 2006, the sharp decrease in ballpark factor for the Yankees was due to an increase in runs scored away and decrease in runs scored at home. 2005 was an out of ordinary year for the Yankees, in which they scored an abnormally large number of runs at home, thus leading to a very inflated ballpark factor. In 2006, the Mets saw a 112 run increase in runs scored and an 83 run increase in runs allowed. However, the majority of these runs scored/allowed were away from home, thus leading to an atypically low ballpark factor in 2006. Finally, the Rangers had an absurd year in 2011 in terms of offensive production, seeing a 68 run increase in runs scored, the majority of which came at home, so it isn’t surprising that their ballpark factor in 2011 is so inflated. 

To test whether ballpark factors could increase the predictive power of the Pythagorean W/L formula, we looked at the scores of each game in an MLB season. We then divided the scores by the ballpark factor of whichever stadium the teams were playing in. So, if the 

11 

Angels scored 4 runs and the Rangers scored 6 runs at Globe Life Park in Arlington (Texas Rangers Stadium), which has a ballpark factor of 1.183, then their adjusted runs scored are 4 _/_ 1 _._ 183 = 3 _._ 38 and 6 _/_ 1 _._ 183 = 5 _._ 07, respectively. It makes the most sense to divide by the ballpark factor, as if a stadium is hitter friendly, then the scores are inflated, and since the ballpark factor is greater than 1 when the stadium is hitter friendly, dividing will deflate the scores. Similarly, if the stadium is “pitcher friendly", then the scores are deflated, and since the ballpark factor is less than 1 when the stadium is pitcher friendly, dividing will inflate the scores. 

Figure 6 details the R-squared values given when estimating teams’ W/L percentage by the Pythagorean W/L formula and Pythagorean W/L formula adjusted for ballpark factors for each year from 2005 to 2012 using a gamma of 1.83, where the Pythagorean W/L is the formula defined by taking runs scored squared over the sum of runs scored squared and runs allowed squared. Interestingly enough, it seems that ballpark factors only slightly increase the predictive power of the Pythagorean W/L formula in some years; however, the minuscule increases observed in some years cannot be considered statistically significant by any means. While at first this may seem strange, as the ballpark that a team is playing in should play a large role in determining the runs scored and allowed, we must remember that there are 2,430 games in an MLB season. In addition, the home and away team in a game are both equally hit by the ballpark factor of the home team’s stadium. Taking these two factors into account, eventually it should make sense that the factors wash out over the entire season, thus leading to a predictive power at least on par with that of the original Pythagorean W/L formula. 



FIGURE 6. R-squared values of normal Pythagorean W/L (Original Pythag) and Pythagorean W/L adjusted for ballpark factors (Adjusted Pythag) from 2005-2012 using a gamma of 1.83. 

12 

3.2. **Game State.** The next sabermetric statistic considered was game state. Game state essentially takes the situation that the game is in (number of outs, which inning, players on bases, and current score) and calculates the percentage that the team at bat has of winning the game in that certain game state, using past game results that encountered the same game state in those games. The site baseball-reference.com does exactly this, labeling it as Winning Team Win Expectancy (wWE), as seen in Figure 7 when one looks at the box score for a particular game. 





FIGURE 7. Top of the 3rd inning from box score for Texas Rangers at Los Angeles Angels on August 7, 2013. http://www. baseball-reference.com/boxes/ANA/ANA201308070. shtml. 

Accounting for game state is reasonable, as if a score progresses from say 9-0 in the bottom of the seventh to a final score of 12-0, those additional three runs are only inflating that team’s total runs scored. For all intensive purposes, when the game is at 9-0 at the bottom of the seventh (or even sooner in the game), the game should be considered over and that score should be used when calculated a team’s total runs scored and allowed at the end of the year. 

In order to implement this, we decided to pick a “threshold" wWE. Thus, if the game progressed to that threshold percentage (or 100 minus that threshold percentage, as wWE only represents the winning team), then we would consider the game over and use the scores at that state in the game as the final score. Two thresholds were used, namely 95% and 98%. In _R_ , this required bringing in each box score of every game in a season (so 2430 urls to go through), and then bringing in the play by play table from the url, and finally searching through the table to find the required threshold and recording the scores 

13 

of each team at that exact point. Going through so many urls and searches required a lot of computational capacity, and in order to get multiple years without spending weeks waiting for the data, we used the Amazon EC2 cloud. This allowed us to run code for different years at the same time in the cloud, which cut the culling time by about a quarter. We display the code used in Appendix A. 

After the data was culled, we used it in the original Pythagorean W/L Formula and the formula accounting for ballpark factors. Unfortunately, the game state adjusted data does not have better predictive power than the original data; in fact, it is notably worse, as we display in Figure 8 for a threshold of 98% in 2009. For the regular Pythagorean W/L Formula, we have an adjusted R-squared value of 0.8145, while for the Pythagorean W/L Formula adjusted for game state at a 98% threshold and ballpark factors, the adjusted R-squared value is 0.7261. 

This significant decrease in predictive power seems strange, as a threshold of 98% should give values almost similar to the original scores, with the exception of a few cases (the same decrease in power is evident in the case of a 95% threshold as well). This can probably be attributed to teams coming back more often than expected and the fact that we are throwing away good values that could evaluate a team. So, for example, if a team is down 0-6 in the bottom of the seventh, so the game is considered almost surely over, but comes back to win 7-6, those 7 runs thrown out are good values that are important in evaluating the team. So, we have problems with not looking at the entire game. 

We also tried a weighted game state approach, where we used the approach above, but afterwards, we multiplied the runs scored and runs allowed in a game by a factor of 9/(inning stopped in) so that we could get the runs for a complete, nine inning game. The (inning stopped in) factor is the inning in which the team last batted in. For example, if we cut the game off at the top of the seventh inning, we multiply the cut off score of the current team at bat by 9/7, and the other team’s cut off score by 9/6. If the game is cut off at the bottom of the fifth inning, we multiply the cut off score of both of the teams by 9/5. We display the results in Figure 9. 

It seems that we run into the problems stated in the original game state case; using a weighted game state at 95% threshold gives an _R_ -squared of 0.568, and that of a 98% threshold gives an _R_ -squared of 0.574, a significant decrease from the 0.882 using the original Pythagorean W/L Formula. Again, this can probably be attributed to teams coming back more often than expected and the fact that we are throwing away good values that could evaluate a team. 

14 







### (b) 

FIGURE 8. 2009 Teams’ W/L percentage modeled by (a) Pythagorean W/L formula with original scores and (b) Teams’ W/L percentage formula modeled by Pythagorean W/L adjusted for game state with 98% threshold and ballpark factors. 

15 



### (a) 



(b) 



### (c) 

FIGURE 9. 2011 Teams’ W/L percentage modeled by (a) Pythagorean W/L formula with original scores, (b) Teams’ W/L percentage formula modeled by Pythagorean W/L adjusted for weighted game state with 95% threshold, and (c) Teams’ W/L percentage formula modeled by Pythagorean W/L adjusted for weighted game state with 98% threshold. 

16 

The fact that the predictive power of the original Pythagorean W/L formula with the original scores is at least on par or better than the adjusted formulas really demonstrates the robustness of the formula, and that in some cases, the simplest formula is in fact the best one. 

3.3. **Sabermetric Statistics Considered.** It seems most natural to consider sabermetric statistics of pitchers, as pitchers have arguably the greatest impact on the runs allowed, and in turn the runs scored of the opposing team. With this intuition, we proceeded to seek sabermetric statistics that measured the effectiveness of a pitcher. Three came to mind, namely (1) Walks plus Hits per Innings Pitched (WHIP), (2) Adjusted ERA+ (ERA+), and (3) Wins Above Replacement (WAR). 

WHIP, given as (BB+H)/IP, where BB is walks, H is hits, and IP is innings pitched, is natural to consider as it is never negative, so there is no need to scale it, and it is readily available on many websites. In addition, it is relatively easy to evaluate a pitcher based on their WHIP; the lower the WHIP, the better the pitcher is usually. So, the way that we adjusted the runs in each game was to divide a team’s runs scored in a game by the opposing pitcher’s WHIP, since the higher the pitcher’s WHIP, the worse the pitcher is, which means the score is inflated. In Figure 10, we compare the R-squared values of the Pythagorean W/L Formula (Regular) to that of the formula where runs are adjusted for WHIP (WHIP), and that of the formula where runs are adjusted for by WHIP and ballpark factors (WHIP.Ballpark) for the 2011 season. In addition, we vary the _γ_ exponent, denoted by Pythag.Exp in the table. 

In calculating WHIP.Ballpark, we increased the magnitude of the ballpark factor and decreased that of the WHIP, since it did not seem that WHIP played an important role in the predictive power of the Pythagorean W/L Formula, while we had showed earlier that ballpark factors could slightly increase the predictive power of the Pythagorean W/L Formula. The powers by which we increased and decreased the magnitudes of the respective statistics can be seen in the code, which we provide in Appendix B. As can be seen from the table, the regular form of the Pythagorean W/L Formula is still a much better predictor of a team’s W/L percentage (this is true over all years). While WHIP may seem like an appropriate statistic to consider, as it basically evaluates a pitcher based on how effectively he keeps a batter off the bags, the low R-squared values may be due to the fact that pitchers have very little control over what happens after the ball is hit; more specifically, they do 

17 



FIGURE 10. Table of R-squared values of Pythagorean W/L Formula, Formula adjusted for WHIP, and for WHIP and ballpark over varying gammas for 2011. 

not control whether a ball hit in play actually goes for a hit, the rest of the team on the field does. 

ERA+ adjusts a pitcher’s earned run average (ERA) based on the ERA of the pitcher’s league as well as the ballpark which the pitcher pitches in. It is calculated as 

((League ERA) _∗_ (home ballpark factor) _∗_ 100)/(player’s ERA). 

ERA+ is calculated so that the league average is 100, and is never negative. Similar to WHIP, this makes it easy to implement in terms of adjusting runs. The higher an ERA+ a pitcher has, the better the pitcher is considered. Thus, it makes sense to adjust the runs by multiplying by (ERA+) _∗_ (1/100), including a scaling factor of (1/100) in order to bring the league average to 1. We display the R-squared values of the Pythagorean W/L Formula (Regular), those of the formula where runs are adjusted for ERA+ (ERA+), and those of the formula where runs are adjusted for by ERA+ and ballpark factors (ERA+.Ballpark) for the 2011 season in Figure 11. In addition, we vary the _γ_ exponent, denoted by Pythag.Exp in the table. 

Similarly to the WHIP.Ballpark case, in calculating ERA+.Ballpark, we increased the magnitude of the ballpark factor and decreased that of the ERA+, since it did not seem that 18 



FIGURE 11. Table of R-squared values of Pythagorean W/L Formula, Formula adjusted for ERA+, and for ERA+ and ballpark over varying gammas for 2011. 

ERA+ played an important role in the predictive power of the Pythagorean W/L Formula, while we had showed earlier that ballpark factors could slightly increase the predictive power of the Pythagorean W/L Formula. The powers by which we increased and decreased the magnitudes of the respective statistics can be seen in the code, which is very similar to the code in Appendix B. As can be seen from the table, again the regular form of the Pythagorean W/L Formula is still a much better predictor of a team’s W/L percentage than the formula with added in sabermetric statistics over all years. We note in the code that if a pitcher does not have an ERA+, then we give the pitcher an ERA+ of 100 and proceed with the calculations. The very low R-squared values produced from the adjusted formula with ERA+ could be due to the underlying inaccuracies of ERA, and namely what it means to be an earned run, which is an abstract and arbitrary term in and of itself (see http://en.wikipedia.org/wiki/Earned_run). 

3.4. **Standardizing WAR.** We also decided to consider WAR, as a pitcher’s WAR is directly related to their team’s W/L percentage (see http://www.baseball-reference. com/about/war_explained_pitch.shtml on how baseball-reference. 

19 

com computes WAR). WAR is interpreted as the number of wins a player adds (or subtracts) compared to a replacement level player (a team of replacement level players is expected to average 40-50 wins in a 162 game season). However, in order to adjust runs with respect to WAR, we needed to scale WAR so that it can’t be negative. This was done by first compiling the WAR for every pitcher in the league in a vector called NEW.WAR. We then got the the mean and standard deviation of NEW.WAR; call them new.war.mean and new.war.std. We then standardize the elements of NEW.WAR by the mean and std, namely subtracting new.war.mean and dividing by new.war.std for each element. Call this new vector of standardized values WAR.standard. We next find the minimum of WAR.standard, and call it WARstand.min. Finally, for each element of WAR.standard, we subtract WARstand.min so that the smallest element of the vector WAR.standard is 0, and then add 0.5 so that all the values will be positive. 

The implementation of this standardization can be seen in the code in Appendix C. The way that we tested the effectiveness of WAR is the same as how we tested that of ERA+, without the scaling factor of 1/100, i.e. multiplying the runs scored of a team by the opposing pitcher’s WAR. For the 2011 season, we show the R-squared values of the Pythagorean W/L Formula (Regular), those of the formula where runs are adjusted for WAR (WAR), and those of the formula where runs are adjusted for by WAR and ballpark factors (WAR.Ballpark) in Figure 12. In addition, we vary the _γ_ exponent, denoted by Pythag.Exp in the table. 

Similarly to the cases of WHIP.Ballpark and ERA+.Ballpark, in calculating WAR.Ballpark, we increased the magnitude of the ballpark factor and decreased that of the WAR, since it did not seem that WAR played an important role in the predictive power of the Pythagorean W/L Formula, while we had showed earlier that ballpark factors could slightly increase the predictive power of the Pythagorean W/L Formula. The powers by which we increased and decreased the magnitudes of the respective statistics can be seen in the code, which we provide in Appendix C. As can be seen from the table, again the regular form of the Pythagorean W/L Formula is still a much better predictor of a team’s W/L percentage than the formula with added in sabermetric statistics over all years. The low R-squared values produced from the adjusted formula with WAR can probably be attributed to the way that we standardized WAR; unfortunately, there is not a good, clean way of standardizing WAR. So, while it may seem that using WAR in adjusted runs is possibly the right statistic to consider, the lack of a true standardization hurts this realization. Another standardization method we tried was first standardizing WAR (so that the vector of values had mean 

20 



FIGURE 12. Table of R-squared values of Pythagorean W/L Formula, Formula adjusted for WAR, and for WAR and ballpark over varying gammas for 2011. 

0), then taking _e_ to the values (so that all the values are positive), and finally dividing by the mean of the new exponentiated values in order to have the vector centered around 1. However, we obtain _R_<sup>2</sup> values (displayed in Figure 13) worse than the ones we obtained in Figure 12; again, the lack of an accepted standardization most likely hurts the realization. 

Throughout the different statistics considered, the robustness of the regular form of the formula is truly startling; it is amazing that a formula devised in the 1970s can consistently beat out formulas with added in whistles and bells that intuitively should make the formula more accurate. With more time, it would have been interesting to consider more complicated pitcher statistics that were more defense-independent, such as Fielding Independent Pitching (FIP) or tRA (an extension of FIP). 

21 



FIGURE 13. Table of R-squared values of Pythagorean W/L Formula, Formula adjusted for exponentiated WAR, and for exponentiated WAR and ballpark over varying gammas for 2011. 

22 

### 4. LINEAR COMBINATIONS OF WEIBULLS 

We now state and prove our main result for a linear combination of two Weibulls, and leave the straightforward generalization to combinations of more Weibulls to the reader. The reason such an expansion is advantageous and natural is that, following [MIL], we can integrate pairs of Weibulls in the regions needed and obtain simple closed form expressions. The theorem below also holds if _γ <_ 0; however, in that situation the more your runs scored exceeds your runs allowed, the worse your predicted record due to the different shape of the Weibull (in all applications of Weibulls in survival analysis, the shape parameter _γ_ must be positive). 

### 4.1. **Linear Combination of Weibulls.** 

**Theorem 4.1.** _Let the runs scored and allowed per game be two independent random variables drawn from linear combinations of independent Weibull distributions with the same β’s and γ’s. Specifically, if W_ ( _t_ ; _α, β, γ_ ) _represents a Weibull distribution with parameters_ ( _α, β, γ_ ) _, and we choose non-negative weights_<sup>1</sup> 0 _≤ ci, c_<sup>_′_</sup> _j_<sup>_≤_1</sup><sup>_(soc_1+</sup><sup>_c_2=1</sup><sup>_and_</sup> _c_<sup>_′_</sup> 1<sup>+</sup><sup>_c′_</sup> 2<sup>= 1</sup><sup>_), then the density of runs scored, Xis_</sup> 



_and runs allowed, Y , is_ 



_In addition, we choose α_ RS1 _and α_ RS2 _so that the mean of X is_ RSobs _and choose α_ RA1 _and α_ RA2 _such that the mean of Y is_ RAobs _. For γ >_ 0 _, we have_ 





> 1If we had more terms in the linear combination, we would simply choose non-negative weights summing to 1. 

23 

_Proof._ Since the means of _X_ (runs scored) and _Y_ (runs allowed) are RSobs and RAobs, respectively, and the random variables are drawn from linear combinations of independent Weibulls, by Lemma 2.1, we have that 



We now calculate the probability that _X_ exceeds _Y_ . We constantly use the fact that the integral of a probability density is 1. We need the two _β_ ’s and the two _γ_ ’s to be equal in order to obtain closed form expressions.<sup>2</sup> We find 



We set 



> 2If the _β_ ’s are differen then in the integration below we might have issues with the bounds of integration, while if the _γ_ ’s are unequal we get incomplete Gamma functions, though for certain rational ratios of the _γ_ ’s these can be done in closed form. 

24 

for 1 _≤ i, j ≤_ 2, so that (4.5) becomes 



### completing the proof of Theorem 4.1. 



**Observation 4.2.** _We set γ to be the same for both distributions in the linear combination of Weibulls of runs scored and allowed as it allows for a closed form solution (one less parameter to worry about). It also really doesn’t make sense for there to be two different gammas over the entire league. In addition, we have γ >_ 0 _. Consider the simple case where c_ 1 = 1 _, we are left with α_ RS<sup>_γ_</sup> 1<sup>_/_(</sup><sup>_α_</sup> RS<sup>_γ_</sup> 1<sup>+</sup><sup>_α_</sup> RA<sup>_γ_</sup> 1<sup>)</sup><sup>_, which simplifies to_(</sup><sup>_RS −β_)</sup><sup>_γ/_((</sup><sup>_RS −β_)</sup><sup>_γ_+</sup> ( _RA − β_ )<sup>_γ_</sup> ) _(see_ [MIL] _). Let β_ = 0 _and γ_ = _−_ 1 _/_ 2 _<_ 0 _. If a teams scores 36 runs (RS=36) and allows 20 runs (RA=20), they are expected to have a winning percentage. However, with γ <_ 0 _, we obtain a winning percentage of_ 36<sup>_−_1</sup><sup>_/_2</sup> _/_ (36<sup>_−_1</sup><sup>_/_2</sup> + 20<sup>_−_1</sup><sup>_/_2</sup> ) = 0 _._ 427 _<_ 0 _._ 5 _, which intuitively doesn’t make sense. So, we only consider γ >_ 0 _._ 

4.2. **Moments Analysis.** The first attempt at estimating values for the parameters was by utilizing the moments. We looked at the moments of the distribution that runs scored was drawn from, namely 



From [MUR], and using the fact that the two Weibulls in the linear combination are independent, we obtained the following moments: 

First Moment = _c_ 1( _α_ RS1Γ(1 + _γ_<sup>_−_1</sup> ) + _β_ 1) + (1 _− c_ 1)( _α_ RS2Γ(1 + _γ_<sup>_−_1</sup> ) + _β_ 2) 



where _gi_ = Γ(1 + _γ_<sup>_<u>i</u>_), and Γ(</sup><sup>_x_) is the Gamma function defined as Γ(</sup><sup>_x_) =</sup> �0 _∞_<sup>_e−uux−_1</sup><sup>_du_.</sup> We next used _R_ to find the observed moments for teams’ runs scored from 2007. The code can be seen in Appendix D. In order to find estimates for the parameters, we wanted to minimize the sum of the squares of the difference in observed and expected values. To implement this, we used Mathematica; the code is displayed in Figure 14. In the code, _x_ represents _c_ 1, _a_ represents _α_ RS1, _b_ represents _α_ RS2, _c_ represents _γ_ , and we assume that _β_ 1 = _−_ 1 _/_ 2 = _β_ 2. 

The code in Figure 14 uses the observed moments of a team and attempts to minimize the sum of the squares of the difference in observed and expected moments using FindMinimum. As can be seen from the output (and error message), Mathematica was unable to find a reasonable minimum, and the parameter estimates do not seem feasible in the slightest. We also tried setting starting values for the parameters, but this did not help. This deterred us from utilizing moments analysis, and we instead turned our attention to least squares. 

4.3. **Least Squares.** We looked at the 30 teams of the entire league from the 2004 to 2012 season. We display results from the 2011, but the results from any other season are readily available. We implemented the method of least squares using the bins in (2.2). The method of least squares involved minimizing the sum of squares of the error of the runs scored data plus the sum of squares of the error of the runs allowed data; using the bins as in (2.2), there were seven free parameters, namely _α_ RS1, _α_ RS2, _α_ RA1, _α_ RA2, _γ_ , _c_ 1, and _c_<sup>_′_</sup> 1<sup>.Letting Bin(</sup><sup>_k_)</sup> be the _k_ th bin of 2 _._ 2, _RSobs_ ( _k_ ) and _RAobs_ ( _k_ ) represent the observed number of games with 

26 



FIGURE 14. Mathematica code used in moments analysis. 

number of runs scored and allowed in Bin( _k_ ), and _A_ ( _α_ 1 _, α_ 2 _, β_ 1 _, β_ 2 _, γ, c_ 1 _, k_ ) denote the area under the Weibull with parameters ( _α_ 1 _, α_ 2 _, β_ 1 _, β_ 2 _, γ, c_ 1) in Bin( _k_ ), then for each team we found the values of ( _α_ RS1 _, α_ RS2 _, α_ RA1 _, α_ RA2 _, γ, c_ 1 _, c_<sup>_′_</sup> 1<sup>) that minimized</sup> 



For each team, we found the best fit Weibulls with forms ( _α_ RS1 _, α_ RS2 _, −._ 5 _, −._ 5 _, γ, c_ 1) and ( _α_ RA1 _, α_ RA2 _, −._ 5 _, −._ 5 _, γ, c_<sup>_′_</sup> 1<sup>).InFigure15,wecomparedthepredictedwins,losses,</sup> and won-loss percentage with the observed ones. 

The code used can be seen in Appendix E. Using the method of least squares, the mean _γ_ over all 30 teams is 1.83 with a standard deviation of 0.18 (the median is 1.79). We can see that the exponent 1.83, considered as the best exponent, is within the region of one standard deviation from the mean _γ_ . Considering the absolute value of the difference between observed and predicted wins, we have a mean of 2.89 with a standard deviation of 2.34 (median is 2.68). Without considering the absolute value, the mean is 0.104 with a 

27 



FIGURE 15. Results for the 2011 season using Method of Least Squares. 

standard deviation of 3.75 (and a median of 0.39). We will only concern ourselves with the absolute value of the difference, as this really tells how accurate our predicted values are. 

These values are improvements on those obtained when using a single Weibull distribution to predict runs, which produces a mean number of games off of 4.43 with standard deviation 3.23 (and median 3.54) in the absolute value case. We display the results over seasons from 2004 to 2012 in Figure 16. It is apparent that the linear combination of Weibulls better estimates teams’ win/loss percentage; in fact, it is over one game better at estimating than the single Weibull! The mean number of games off for a single Weibull from 2004 to 2012 was 4.22 (with a standard deviation of 3.03), while that of the linear combination of Weibulls was 3.11 (with a standard deviation of 2.33). In addition, there is less standard deviation in the estimates. Thus, it appears that the linear combination of Weibulls provides a much tighter, better estimate than the single Weibull does. To further demonstrate how accurate the quality of the fit is, we compare the best fit linear combination of Weibulls of runs scored and allowed with those observed of the 2011 Seattle Mariners in Figure 18; we can see that the fit is visually very good. 

We conduct an independent two-sample t-test with unequal variances in _R_ using the t.test command to see if the difference between the games off determined by the single Weibull 28 



FIGURE 16. Mean number of games off (with standard deviation) for single Weibull and linear combination of Weibulls from 2004-2012. 

and those by linear combinations of Weibulls is statistically significant in Figure 17. With a _p_ -value less than 0.01 and a 95% confidence interval that does not contain 0, we can see that the difference is in fact statistically significant. 



FIGURE 17. t-test to determine whether the difference between the games off determined by the single Weibull and those by linear combinations of Weibulls is statistically significant. 

29 



(A) Single Weibull mapping runs scored and allowed. 



(B) Linear Combination of Weibulls mapping runs scored and allowed. 

FIGURE 18. Comparison of best fit linear combination of Weibulls versus single Weibull for runs scored (top) and allowed (bottom) for the 2011 Seattle Mariners against the observed distribution of scores. 

In addition, we compared the mean number of games off of ESPN’s calculated Expected WL (ExWL) and those of the linear combination of Weibulls from 1979 to 2013. For the years from 2002 to 2013, we utilize ESPN’s ExWL, which calculates a team’s expected WL as (runs scored<sup>2</sup> ) _/_ (runs scored<sup>2</sup> + runs allowed<sup>2</sup> ).<sup>3</sup> Since ESPN only had this data available down to the year 2002, we used baseball-reference.com’s Pythagorean WL (pythagWL) in order to obtain more data (baseball-reference. com allowed us to go all the way down to 1979). The pythagWL statistic is calculated as (runs scored<sup>1</sup><sup>_._83</sup> ) _/_ (runs scored<sup>1</sup><sup>_._83</sup> + runs allowed<sup>1</sup><sup>_._83</sup> ).<sup>4</sup> 

> 3 see bottom of page: http://espn.go.com/mlb/stats/rpi/_/year/2011. 

> 4 see section “What is Pythagorean Winning Percentage?": http://www.sports-reference. com/blog/baseball-reference-faqs/. 

30 

We display the results in Figure 19. The mean number of games off for ESPN’s ExWL was 3.09 with a mean standard deviation of 2.29, numbers slightly worse than those of the linear combination of Weibulls (mean of 3.03 with standard deviation of 2.21). So, we can see that the linear combination of Weibulls is doing, on average, about .06 of a game better than ESPN’s ExWL. We performed an independent two-sample t-test with unequal variances in _R_ using the t.test command to see if the difference between the games off determined by ESPN’s ExWL and the linear combination of Weibulls is statistically significant in Figure 20. With a very large _p_ -value, we fail to reject the null hypothesis, suggesting that the difference in mean number of games off is not in fact statistically significant. We also display a plot (Figure 21) that models the difference in the number of games between ESPN’s ExWL and the linear combination of Weibulls; it seems to be a constant positive value for the most part, suggesting that the linear combination of Weibulls is doing slightly better than ESPN’s ExWL. 



FIGURE 19. Mean number of games off (with standard deviation) for ESPN ExWL and linear combination of Weibulls from 1979-2013. 

Looking at Figure 21 more closely, we can see that there are blocks of the graph where ESPN does better, and blocks where linear combination of Weibulls does better. For example, it is clear in the era from 1979-1989 that ESPN’s ExWL is the more accurate statistic, beating the linear combination of Weibulls in 7 out of the 11 years. However, from 1990 

31 

to 2013, the linear combination of Weibulls beats ESPN’s ExWL 14 out of the 24 years, and by around 0.3/0.35 games in those years. When ESPN’s ExWL does beat the linear combination of Weibulls in the years from 1990 to 2013, it does so by around 0.25 games, including the point at 2004, which seems very out of the ordinary; without this point, ESPN’s ExWL wins by about .2 games in the years between 1990 and 2013 that it does beat the linear combination of Weibulls. Thus, in more recent years, it may make more sense to use the linear combination of Weibulls. In addition, with respect to the standard deviation of number of games off of ESPN’s ExWL (2.29) and the linear combination of Weibulls (2.21), we can see that the linear combination of Weibulls provides on average a tighter fit, i.e. there is less fluctuation in the mean number of games off for each team in each year (from 1990 to 2013, ESPN’s ExWL standard deviation in games off is 2.34 while that of the linear combination of Weibulls is 2.22, so we again see that the linear combination does noticeably better in recent years). 

It is important to note that ESPN just takes the functional form of the Pythagorean Win/Loss Formula with an exponent ( _γ_ ) of 2, while we give theoretical justification for our formula by utilizing some nice properties of the Weibull distribution and _Mathematica_ . We also note that in the years from 1979 to 2001, when we are comparing against baseball-reference.com’s Pythagorean Win/Loss Formula with an exponent of 1.83 rather than 2 (which ESPN’s ExWL uses), it seems that the difference in games off is more centered around zero than in the years when we are comparing against ESPN’s ExWL (2002-2013). Thus, it might make sense for ESPN to use an exponent of 1.83 when computing their ExWL rather than 2. 



FIGURE 20. t-test to determine whether the difference between the games off determined by ESPN ExWL and those by linear combinations of Weibulls is statistically significant. 

32 



FIGURE 21. Difference in mean number of games off for ESPN ExWL and linear combination of Weibulls from 1979-2013. 

We also performed _χ_<sup>2</sup> tests to determine the goodness of fit to see how well the linear combination of Weibulls maps the observed data, and whether runs scored and allowed are independent. We used the bins as in (2.2), namely 



and test statistic 



for the goodness of fit tests, with 2 _∗_ (#Bins _−_ 1) _−_ 1 _−_ 7 = 16 degrees of freedom, the factor of 7 coming from estimating 7 parameters, namely _α_ RS1, _α_ RS2, _α_ RA1, _α_ RA2, _γ_ , _c_ 1, and _c_<sup>_′_</sup> 1<sup>.</sup> We did not estimate _β_ 1 or _β_ 2, as we took them to be -.5. Having 16 degrees of freedom gives critical threshold values of 26.3 (at the 95% level) and 32.0 (at the 99% level). However, 

33 

since there are multiple comparisons being done (namely 30 for the different teams), we use a Bonferroni adjustment ( _αnew_ = (1 _−_ (1 _− α_ )<sup>_c_</sup> ), where _c_ is the number of comparisons, in our case the number of teams) and obtain critical thresholds of 37.7 (95%) and 42.5 (99%). From the first column of Figure 22, all the teams fall within the unadjusted 99% threshold, with the exception of the Texas Rangers (just barely!), who easily fall into the Bonferroni adjusted 95% threshold. Therefore, the observed data closely follows a linear combination of Weibulls with the proper estimated parameters. A more in depth discussion of the justification behind the tests can be seen in [MIL]. 



FIGURE 22. _χ_<sup>2</sup> test results of the 2011 season from least squares of goodness of fit and independence of runs score and allowed. 

Since the test for independence of runs scored and allowed requires that the row and column of the contingency table have at least one non-zero entry, the bins used to bin the runs score and allowed were 



We use integer endpoints because we are using the observed runs from games. So, we have a 12 by 12 contingency table with zeroes along the diagonal, since runs scored and allowed can never be equal. This leads to an incomplete 12 by 12 contingency table with (12 _−_ 1)<sup>2</sup> _−_ 12 = 109 degrees of freedom; constructing a test requires the use of structural zeroes. The theory behind tests using structural zeroes can be seen in Appendix 9.2 of [MCGLP]. We observe that 109 degrees of freedom give critical threshold values of 134.37 (at the 95% level) and 146.26 (at the 99% level). Again, since we are doing multiple comparisons, we use a Bonferroni adjustment, obtaining critical thresholds of 157.68 (95%) and 166.45 (99%). From the second column of Figure 22, all the teams fall within the 99% threshold, with the exception of the Los Angeles Angels (just barely!), who easily fall into the Bonferroni adjusted 95% threshold. Thus, runs scored and allowed are acting as though they are statistically independent. 

4.4. **A Simpler Formula?** While the one game improvement in prediction is very promising, the formula and curve fitting/parameter estimating is not very easily implemented. So, we tried to simplify the formula, even giving up some accuracy, in order to devise a formula that could be easily implemented using just a team’s runs scored and allowed (and the variance of each of these) in order to determine the team’s W/L percentage. Unfortunately, the weight parameters _c_ 1 and _c_<sup>_′_</sup> 1<sup>plays too much of a factor; for example, in 2011, the mean of</sup> the parameter _c_ 1 is 0.21 with a standard deviation of 0.39 (and a median of 0.21). With such large fluctuations in the weight parameters from team to team, the task of finding a simpler formula was almost impossible, as creating a uniform formula that every team could use was not feasible when two of the key parameters were so volatile. 

35 

### APPENDIX A. 2011 GAME STATE CODE 

#install.packages(c("XML","RCurl")) 

########################################################## ########################################################## #using try function .... not sure what it is doing. 

require(XML) require(RCurl) #clear all variables before evaluating code rm(list=ls(all=TRUE)) 

#variables 

#years=c("2006","2007","2008","2009","2010","2011","2012","2013") years=c("2011") 

months=c("03","04","05","06","07","08","09","10","11") days=c("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22"," 23","24","25","26","27","28","29","30","31") doubleheaders=c("0","1","2") teams=c("ANA", "ARI", "ATL", "BAL", "BOS", "CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU", "KCA", "LAN", "MIL", "MIN", "NYA", "NYN", "OAK", "PHI", "PIT", "SDN", "SEA", "SFN", "SLN", "TBA", "TEX", "TOR", "WAS") 

#data frame that will store everything seasonGameSt<-data.frame(Date=character(), Home_Team=character(),Home_ScoreGS=character(),Away_Team=character(),Away_ScoreGS=character()) 

for(year in years){ #add in ballpark effects here for(month in months){ for(day in days){ for(doubleheader in doubleheaders){ for(team in teams){ #getting box score for game of type team, year, month, day, doubleheader url<-paste("http://www.baseball-reference.com/ boxes/",team,"/",team,year,month,day,doubleheader,".shtml",sep="") #check to see if the url actually exists if(url.exists(url)){ rawhtml<-getURLContent(url) #final check to see if the url is actually valid if(identical(as.character(rawhtml),"")){ next() } rawPMI<-readHTMLTable(url) playBP<-as.data.frame(rawPMI$play_by_play) #attach(playBP)  probably don't need colnames(playBP)<-c("Inn","Score","Out", "RoB", "Pitch","RO","AtBat","Batter", "Pitcher", "wWPA", "wWE", "Play") #attach(playBP)   probably don't need #get rid of rows with NA in them for wWE newplayBP<- subset(playBP,! wWE %in% c(NA)) attach(newplayBP) #get the home and away team, and if necessary, convert away teams to original team names HomeTeam=team AwayTeam=as.character(AtBat[1]) if(identical(AwayTeam,"NYY")==TRUE){ AwayTeam<-"NYA" } if(identical(AwayTeam,"TBD")==TRUE){ AwayTeam<-"TBA" } if(identical(AwayTeam,"NYM")==TRUE){ 

36 

- AwayTeam<-"NYN" 

- } if(identical(AwayTeam,"LAA")==TRUE){ AwayTeam<-"ANA" 

- } if(identical(AwayTeam,"SFG")==TRUE){ AwayTeam<-"SFN" 

- } if(identical(AwayTeam,"KCR")==TRUE){ AwayTeam<-"KCA" 

- } if(identical(AwayTeam,"STL")==TRUE){ AwayTeam<-"SLN" 

- } if(identical(AwayTeam,"LAD")==TRUE){ AwayTeam<-"LAN" 

- } if(identical(AwayTeam,"CHW")==TRUE){ AwayTeam<-"CHA" 

- } if(identical(AwayTeam,"CHC")==TRUE){ AwayTeam<-"CHN" 

- } if(identical(AwayTeam,"SDP")==TRUE){ AwayTeam<-"SDN" 

- } 

if(identical(AwayTeam,"TBR")==TRUE){ AwayTeam<-"TBA" } 

- if(identical(AwayTeam,"WSH")==TRUE){ AwayTeam<-"WAS" 

- } 

- if(identical(AwayTeam,"WSN")==TRUE){ AwayTeam<-"WAS" 

- } 

- if(identical(AwayTeam,"MIA")==TRUE){ AwayTeam<-"FLO" 

- } 

- if(identical(AwayTeam,"FLA")==TRUE){ AwayTeam<-"FLO" 

- } 

###mlb site to get scores 

#correcting for site errors 

holderdouble<-"" 

if(identical(doubleheader,"0")||identical(doubleheader,"1")){ holderdouble<-"1" 

} 

else{ 

holderdouble<-"2" 

} 

url2<-paste("http://mlb.mlb.com/news/boxscore.jsp? 

gid=",year,"_",month,"_",day,"_",tolower(AwayTeam),"mlb_",tolower(HomeTeam),"mlb_",holderdouble,"&mode=box",sep="") rawPMI2<-try(readHTMLTable(url2)) 

#catch error in writing rawPMI2 if(class(rawPMI2)=="try-error"){ 

seasonGameSt<-rbind(seasonGameSt, 

data.frame(Date=paste(year,"/",month,"/",day,sep=""),Home_Team=HomeTeam, Home_ScoreGS="NA", Away_Team=AwayTeam, Away_ScoreGS="NA")) 

next; 

} 

#initialize variables... really dumb HomeScore<-"" AwayScore<-"" 

37 

#getting the adjusted for game state scores dummy<- FALSE for(i in 1:nrow(newplayBP)){ 

winExpect<-as.character(newplayBP$wWE[i]) winExpectNoP<-gsub("%","",winExpect) numericalWinEx<-as.integer(winExpectNoP) rankBoxScore<-i+1 

#if goes past and numericalWinEx still not past threshold ###just added in november 25, 2013 

if(rankBoxScore>nrow(newplayBP)){ 

HomeScore<-as.character(rawPMI2$`print-linescore`$R[2]) AwayScore<-as.character(rawPMI2$`print-linescore`$R[1]) dummy<-TRUE break 

} 

#98% threshold 

if((numericalWinEx>97) || (numericalWinEx<3)){ batTeam<-as.character(newplayBP$AtBat[i+1]) boxScore<-as.character(newplayBP$Score[i+1]) placeInn<-as.character(substring(newplayBP$Inn[i+1],1,1)) numInn<-as.character(substring(newplayBP$Inn[i+1],2)) minusLocation<-which(strsplit(boxScore, "")[[1]]=="-") batScore<-substr(boxScore,1,minusLocation-1) pitchScore<-substring(boxScore,minusLocation+1) HolderHomeTeam<-"" 

HolderHomeTeam2<-"" 

if(identical(HomeTeam,"NYA")==TRUE){ HolderHomeTeam<-"NYY" 

} 

- if(identical(HomeTeam,"NYN")==TRUE){ HolderHomeTeam<-"NYM" 

} 

- if(identical(HomeTeam,"ANA")==TRUE){ HolderHomeTeam<-"LAA" 

} 

- if(identical(HomeTeam,"SFN")==TRUE){ HolderHomeTeam<-"SFG" 

} 

- if(identical(HomeTeam,"KCA")==TRUE){ HolderHomeTeam<-"KCR" 

} 

- if(identical(HomeTeam,"SLN")==TRUE){ HolderHomeTeam<-"STL" 

} 

- if(identical(HomeTeam,"LAN")==TRUE){ HolderHomeTeam<-"LAD" 

} if(identical(HomeTeam,"CHA")==TRUE){ HolderHomeTeam<-"CHW" 

} 

- if(identical(HomeTeam,"CHN")==TRUE){ HolderHomeTeam<-"CHC" 

} 

- if(identical(HomeTeam,"SDN")==TRUE){ HolderHomeTeam<-"SDP" 

} 

- if(identical(HomeTeam,"TBA")==TRUE){ HolderHomeTeam<-"TBR" 

} 

if(identical(HomeTeam,"WAS")==TRUE){ HolderHomeTeam<-"WSH" HolderHomeTeam<-"WSN" 

} 

38 

if(identical(HomeTeam,"TBA")==TRUE){ HolderHomeTeam<-"TBD" } if(identical(HomeTeam,"FLO")==TRUE){ HolderHomeTeam<-"MIA" HolderHomeTeam2<-"FLA" } 

if(identical(batTeam,HomeTeam)||identical(batTeam,HolderHomeTeam)|| identical(batTeam,HolderHomeTeam2)){ 

if(identical("t",placeInn)){ HomeScore<-as.character(as.numeric(batScore)*(9/as.numeric(numInn))) AwayScore<-as.character(as.numeric(pitchScore)*(9/(as.numeric(numInn)-1))) } else{ HomeScore<-as.character(as.numeric(batScore)*(9/as.numeric(numInn))) AwayScore<-as.character(as.numeric(pitchScore)*(9/as.numeric(numInn))) } } else{ if(identical("t",placeInn)){ HomeScore<-as.character(as.numeric(pitchScore)*(9/(as.numeric(numInn)-1))) AwayScore<-as.character(as.numeric(batScore)*(9/(as.numeric(numInn)))) } else{ HomeScore<-as.character(as.numeric(pitchScore)*(9/as.numeric(numInn))) AwayScore<-as.character(as.numeric(batScore)*(9/as.numeric(numInn))) } } 

#need to exit the for loop now dummy<- TRUE break } 

#exits for loop if dummy is true if(dummy){break} 

} 

#insert things into the data frame 

seasonGameSt<-rbind(seasonGameSt, data.frame(Date=paste(year,"/",month,"/",day,sep=""), Home_Team=HomeTeam, Home_ScoreGS=HomeScore, Away_Team=AwayTeam, Away_ScoreGS=AwayScore)) 

print(seasonGameSt) 

#clearing things to potentially increase run speed? 

rm(list=setdiff(ls(),c("seasonGameSt","years","months","days", "doubleheaders", "teams", "year", "month", "day","doubleheader","team", "i"))) 

} 

} 

} 

} 

} 

} 

39 

### APPENDIX B. 2011 WHIP CODE 

#install.packages(c("XML","RCurl")) 

########################################################## ########################################################## #DON'T FORGET TO CHANGE YEAR IN URL (LINE 25), TEAMS (LINE 45), AND IN DATA (LINE 123) #marlins and rays change over years 

require(XML) require(RCurl) #clear all variables before evaluating code rm(list=ls(all=TRUE)) #variables pitcher.stats<-data.frame() years=c("2006","2007","2008","2009","2010","2011","2012","2013") teams=c("LAA", "ARI", "ATL", "BAL", "BOS", "CHW","CHC", "CIN", "CLE", "COL", "DET", "FLA", "HOU", "KCR", "LAD","MIL", "MIN", "NYY", "NYM", "OAK", "PHI", "PIT", "SDP","SEA", "SFG", "STL", "TBD","TEX", "TOR", "WSN") Team=c() 

for(team in teams){ #getting box score for team and year #IMPORTANT HERE #change year accordingly #REALLY IMPORTANT HERE url<-paste("http://www.baseball-reference.com/teams/",team,"/2011.shtml",sep="") rawhtml<-getURLContent(url) #final check to see if the url is actually valid if(identical(as.character(rawhtml),"")){ next() } rawPMI<-readHTMLTable(url) pitching<-as.data.frame(rawPMI$team_pitching) colnames(pitching)[3]<-"name" attach(pitching) pitcher.stats<-rbind(pitcher.stats,pitching) 

#get team #don't forget to change these for different years for(j in 1:nrow(pitching)){ if(identical(as.character(pitching$name[j]),"")==FALSE){ if(identical(team,"LAA")){ Team=c(Team,"ANA") } else if(identical(team,"CHW")){ Team=c(Team,"CHA") } else if(identical(team,"CHC")){ Team=c(Team,"CHN") } else if(identical(team,"FLA")){ Team=c(Team,"FLO") } else if(identical(team,"KCR")){ Team=c(Team,"KCA") } else if(identical(team,"LAD")){ Team=c(Team,"LAN") } else if(identical(team,"NYY")){ Team=c(Team,"NYA") } else if(identical(team,"NYN")){ 

40 

Team=c(Team,"NYM") } else if(identical(team,"SDP")){ Team=c(Team,"SDN") } else if(identical(team,"SFG")){ Team=c(Team,"SFN") } else if(identical(team,"STL")){ Team=c(Team,"SLN") } else if(identical(team,"TBD")){ Team=c(Team,"TBA") } else if(identical(team,"WSN")){ Team=c(Team,"WAS") }else{ Team=c(Team,team) } } } 

} 

#cleaning up the pitcher stats 

#first get rid of rows where there is no name numrows=nrow(pitcher.stats) for(i in 1:numrows){ if(identical(as.character(pitcher.stats$name[i]),"")){ pitcher.stats<-pitcher.stats[-i,] } } 

#update row indices rownames(pitcher.stats) <- 1:nrow(pitcher.stats) 

#getting rid of all the stars in the names Names.updated=c() for(i in 1:nrow(pitcher.stats)){ name.new <- as.character(pitcher.stats$name[i]) 

if(identical("*",substr(name.new,nchar(name.new),nchar(name.new)))){ Names.updated<-c(Names.updated,substr(name.new,0,nchar(name.new)-1)) 

} else{ Names.updated<-c(Names.updated,name.new) } } 

pitcher.stats<-pitcher.stats[,c(-3)] pitcher.stats<-cbind(Names.updated,Team,pitcher.stats) colnames(pitcher.stats)[28]<-"ERA.plus" 

####################################################################################### 

#pythag exponents table pythag.table <-data.frame() 

#now bring in data #depends on the year 

data<-read.csv("/Users/victorluo/Documents/Williams College/Senior Year/thesis/Complete Season Data/ 2011completedata.csv") 

ballpark<-read.csv("/Users/victorluo/Documents/Williams College/Senior Year/thesis/Ballpark/Outdated Ballpark Effects/ 2011ballparkeffects.csv") 

41 

teams.retro=c("ANA", "ARI", "ATL", "BAL", "BOS", "CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU", "KCA", "LAN", "MIL", "MIN", "NYA", "NYN", "OAK", "PHI", "PIT", "SDN", "SEA", "SFN", "SLN", "TBA", "TEX", "TOR", "WAS") 

#loop to find best pythag exponent power for(l in 1:25){ #pythag exponent power alpha <- runif(1,0.5,2.5) #intialize vectors teams.pythag<-c() teams.pythag.WHIP=c() teams.pythag.WHIP.park=c() teamsWL<-c() 

#loop over teams for(team in teams.retro){ RS<-c() RS.WHIP<-c() RS.WHIP.park<-c() wins <- 0 losses <- 0 RA<-c() RA.WHIP<-c() RA.WHIP.park<-c() 

#get runs scored for pythag WL #also get runs scored for WHIP pythag WL for (i in 1:nrow(data)){ #if the team is the home team if(data$Home_Team[i]==team){ RS=c(RS, data$Home_Score[i]) #get WHIP PLUS data indices <- match(as.character(data$Away_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Away_Team[i]))){ pitcher.plus<-as.character(pitcher.stats$WHIP[index]) 

} 

} #HERE IS WHIP PLUS DATA ############## RS.WHIP = c(RS.WHIP, data$Home_Score[i]*(as.numeric(pitcher.plus)*(1/100))) 

RS.WHIP.park = c(RS.WHIP.park, data$Home_Score[i]*((as.numeric(pitcher.plus)*(1/100))^(1/8)/(ballpark $BallparkEffect[data$Home_Team[i]])^(1.5))) 

#get w/l if(data$Home_Score[i]>data$Away_Score[i]){ wins <- wins+1 } else{ losses <- losses+1 } } #if the team is the away team if(data$Away_Team[i]==team){ RS=c(RS, data$Away_Score[i]) #get WHIP PLUS data indices <- match(as.character(data$Home_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Home_Team[i]))){ pitcher.plus<-as.character(pitcher.stats$WHIP[index]) } } #HERE IS WHIP PLUS DATA ############## RS.WHIP = c(RS.WHIP, data$Away_Score[i]*(as.numeric(pitcher.plus)*(1/100))) RS.WHIP.park = c(RS.WHIP.park, data$Away_Score[i]*((as.numeric(pitcher.plus)*(1/100))^(1/8)/(ballpark 

42 

$BallparkEffect[data$Home_Team[i]])^(1.5))) 

#get w/l if(data$Home_Score[i]<data$Away_Score[i]){ wins <- wins+1 } else{ losses <- losses+1 } } } #get runs allowed for pythag WL for (i in 1:nrow(data)){ #if team is the home team if(data$Home_Team[i]==team){ RA=c(RA, data$Away_Score[i]) #get WHIP PLUS data indices <- match(as.character(data$Home_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Home_Team[i]))){ pitcher.plus<-as.character(pitcher.stats$WHIP[index]) } } #HERE IS THE WHIP PLUS ############## 

RA.WHIP = c(RA.WHIP, data$Away_Score[i]*(as.numeric(pitcher.plus)*(1/100))) 

RA.WHIP.park = c(RA.WHIP.park, data$Away_Score[i]*((as.numeric(pitcher.plus)*(1/100))^(1/8)/(ballpark $BallparkEffect[data$Home_Team[i]])^(1.5))) 

} #if team is the away team 

if(data$Away_Team[i]==team){ 

RA=c(RA, data$Home_Score[i]) #get WHIP PLUS data 

indices <- match(as.character(data$Away_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Away_Team[i]))){ pitcher.plus<-as.character(pitcher.stats$WHIP[index]) } 

} #HERE IS WHIP PLUS DATA ############## 

RA.WHIP = c(RA.WHIP, data$Home_Score[i]*(as.numeric(pitcher.plus)*(1/100))) 

RA.WHIP.park = c(RA.WHIP.park, data$Home_Score[i]*((as.numeric(pitcher.plus)*(1/100))^(1/8)/(ballpark $BallparkEffect[data$Home_Team[i]])^(1.5))) 

} 

} 

#take sums over runs scored in every category# #regular RS and RA runs.score=sum(RS) runs.allow=sum(RA) #WHIP runs.score.WHIP=sum(RS.WHIP) runs.allow.WHIP=sum(RA.WHIP) #WHIP + park runs.score.WHIP.park=sum(RS.WHIP.park) runs.allow.WHIP.park=sum(RA.WHIP.park) 

#compute the pythag formula for regular PythagWL=(runs.score^(alpha))/(runs.score^(alpha)+runs.allow^(alpha)) #WHIP 

PythagWL.WHIP=(runs.score.WHIP^(alpha))/(runs.score.WHIP^(alpha)+runs.allow.WHIP^(alpha)) PythagWL.WHIP.park=(runs.score.WHIP.park^(alpha))/(runs.score.WHIP.park^(alpha)+runs.allow.WHIP.park^(alpha)) #add in the pythags into their vectors teams.pythag=c(teams.pythag,PythagWL) teams.pythag.WHIP=c(teams.pythag.WHIP,PythagWL.WHIP) 

43 

teams.pythag.WHIP.park=c(teams.pythag.WHIP.park,PythagWL.WHIP.park) 

#compute teams W/L for the season WL <- wins/(wins + losses) teamsWL=c(teamsWL, WL) } ######### end of loop over teams ################## 

model.pythag=lm(teamsWL~teams.pythag) model.pythag.WHIP=lm(teamsWL~teams.pythag.WHIP) model.pythag.WHIP.park = lm(teamsWL~teams.pythag.WHIP.park) 

reg <- summary(model.pythag)$r.squared plus <- summary(model.pythag.WHIP)$r.squared plus.park <- summary(model.pythag.WHIP.park)$r.squared 

#summary(fit)$r.squared 

pythag.table <- rbind(pythag.table, c(alpha,reg,plus,plus.park)) 

print(pythag.table) } ####### end of loop over pythag powers ################## colnames(pythag.table)<- c("Pythag.Exp", "Regular", "WHIP", "WHIP.Ballpark") 

sorted.table<-pythag.table[order(pythag.table$Regular),] 

#write.csv(sorted.table,"sorted.WHIP.ballpark2007") 

################################################################################## #interesting.... raising the WHIP to a power affects it #TRY 2007 NEXT (1/8, 1.5) 

#2009 (0,2.2) #2010 (0, 0.5) #2011 (0,1.5) #2012(0,0.5) 

44 

### APPENDIX C. 2011 WAR CODE 

#install.packages(c("XML","RCurl")) 

########################################################## ########################################################## #DON'T FORGET TO CHANGE YEAR IN URL (LINE 25), TEAMS (LINE 45), AND IN DATA (LINE 123) #marlins and rays change over years 

require(XML) require(RCurl) #clear all variables before evaluating code rm(list=ls(all=TRUE)) 

#variables pitcher.stats<-data.frame() pitcher.stats1<-data.frame() 

years=c("2006","2007","2008","2009","2010","2011","2012","2013") teams=c("LAA", "ARI", "ATL", "BAL", "BOS", "CHW","CHC", "CIN", "CLE", "COL", "DET", "FLA", "HOU", "KCR", "LAD","MIL", "MIN", "NYY", "NYM", "OAK", "PHI", "PIT", "SDP","SEA", "SFG", "STL", "TBD","TEX", "TOR", "WSN") Team=c() 

for(team in teams){ #getting box score for team and year #IMPORTANT HERE #change year accordingly #REALLY IMPORTANT HERE url<-paste("http://www.baseball-reference.com/teams/",team,"/2011.shtml",sep="") url1<-paste("http://www.baseball-reference.com/teams/",team,"/2011-pitching.shtml",sep="") 

rawhtml<-getURLContent(url) 

#final check to see if the url is actually valid if(identical(as.character(rawhtml),"")){ next() } rawPMI<-readHTMLTable(url) rawPMI1<-readHTMLTable(url1) pitching<-as.data.frame(rawPMI$team_pitching) pitching1<-as.data.frame(rawPMI1$players_value_pitching) colnames(pitching)[3]<-"name" attach(pitching) 

pitcher.stats<-rbind(pitcher.stats,pitching) pitcher.stats1<-rbind(pitcher.stats1,pitching1) 

#get team 

#don't forget to change these for different years for(j in 1:nrow(pitching)){ 

if(identical(as.character(pitching$name[j]),"")==FALSE){ if(identical(team,"LAA")){ Team=c(Team,"ANA") 

} 

else if(identical(team,"CHW")){ Team=c(Team,"CHA") 

} else if(identical(team,"CHC")){ Team=c(Team,"CHN") 

} else if(identical(team,"FLA")){ Team=c(Team,"FLO") 

} 

else if(identical(team,"KCR")){ Team=c(Team,"KCA") 

} 

else if(identical(team,"LAD")){ Team=c(Team,"LAN") 

45 

} else if(identical(team,"NYY")){ Team=c(Team,"NYA") } else if(identical(team,"NYN")){ Team=c(Team,"NYM") } else if(identical(team,"SDP")){ Team=c(Team,"SDN") } else if(identical(team,"SFG")){ Team=c(Team,"SFN") } else if(identical(team,"STL")){ Team=c(Team,"SLN") } else if(identical(team,"TBD")){ Team=c(Team,"TBA") } else if(identical(team,"WSN")){ Team=c(Team,"WAS") }else{ Team=c(Team,team) } } } 

} 

#cleaning up the pitcher stats 

#first get rid of rows where there is no name numrows=nrow(pitcher.stats) for(i in 1:numrows){ if(identical(as.character(pitcher.stats$name[i]),"")){ pitcher.stats<-pitcher.stats[-i,] } } #update row indices rownames(pitcher.stats) <- 1:nrow(pitcher.stats) 

#getting rid of all the stars in the names Names.updated=c() for(i in 1:nrow(pitcher.stats)){ name.new <- as.character(pitcher.stats$name[i]) 

if(identical("*",substr(name.new,nchar(name.new),nchar(name.new)))){ Names.updated<-c(Names.updated,substr(name.new,0,nchar(name.new)-1)) } else{ Names.updated<-c(Names.updated,name.new) } } 

pitcher.stats<-pitcher.stats[,c(-3)] pitcher.stats<-cbind(Names.updated,Team,pitcher.stats) 

####standard WAR#### ############# NEW.WAR<- c() for(j in 1:length(pitcher.stats1$WAR)){ if(as.character(pitcher.stats1$WAR[j])==""){ NEW.WAR<-c(NEW.WAR,"NA") next} else{ NEW.WAR<-c(NEW.WAR,as.character(pitcher.stats1$WAR[j]))} 

46 

} #getting mean and variance dummy.WAR<-c() for(k in NEW.WAR){ if(k=="NA"){ next} else{ dummy.WAR<-c(dummy.WAR,k)} 

} WAR.mean<-mean(as.numeric(dummy.WAR)) WAR.var<-sqrt(var(as.numeric(dummy.WAR))) 

#STANDARDIZATION 

WAR.standard<-(as.numeric(dummy.WAR)-WAR.mean)/(WAR.var) WARstand.min<-min(WAR.standard) final.WAR<-c() for(i in 1:length(NEW.WAR)){ if(identical(NEW.WAR[i],"NA")==TRUE){ final.WAR<-c(final.WAR, 1)} else{ stand<-(as.numeric(NEW.WAR[i])-WAR.mean)/(WAR.var) what.add<-(stand-WARstand.min+0.5) final.WAR<-c(final.WAR,what.add)} } final.WAR<-final.WAR/mean(final.WAR) pitcher.stats<-cbind(pitcher.stats,final.WAR) 

print(final.WAR) 

####################################################################################### 

#pythag exponents table pythag.table <-data.frame() 

#now bring in data #depends on the year data<-read.csv("/Users/victorluo/Documents/Williams College/Senior Year/thesis/Complete Season Data/ 2011completedata.csv") 

ballpark<-read.csv("/Users/victorluo/Documents/Williams College/Senior Year/thesis/Ballpark/Outdated Ballpark Effects/ 2011ballparkeffects.csv") 

teams.retro=c("ANA", "ARI", "ATL", "BAL", "BOS", "CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU", "KCA", "LAN", "MIL", "MIN", "NYA", "NYN", "OAK", "PHI", "PIT", "SDN", "SEA", "SFN", "SLN", "TBA", "TEX", "TOR", "WAS") 

#loop to find best pythag exponent power for(l in 1:25){ #pythag exponent power alpha <- runif(1,0.5,2.5) #intialize vectors teams.pythag<-c() teams.pythag.WAR=c() teams.pythag.WAR.park=c() teamsWL<-c() #loop over teams for(team in teams.retro){ RS<-c() RS.WAR<-c() RS.WAR.park<-c() wins <- 0 

47 

losses <- 0 RA<-c() RA.WAR<-c() RA.WAR.park<-c() #get runs scored for pythag WL #also get runs scored for WAR pythag WL for (i in 1:nrow(data)){ #if the team is the home team if(data$Home_Team[i]==team){ RS=c(RS, data$Home_Score[i]) #get WAR data indices <- match(as.character(data$Away_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Away_Team[i]))){ pitcher.plus<-pitcher.stats$final.WAR[index] } } #HERE IS WAR DATA ############## RS.WAR = c(RS.WAR, (data$Home_Score[i])*pitcher.plus) RS.WAR.park = c(RS.WAR.park, (data$Home_Score[i])*pitcher.plus^(1/8)/(ballpark$BallparkEffect[data $Home_Team[i]])^(1)) 

#get w/l if(data$Home_Score[i]>data$Away_Score[i]){ wins <- wins+1 } else{ losses <- losses+1 } } 

#if the team is the away team if(data$Away_Team[i]==team){ RS=c(RS, data$Away_Score[i]) #get WAR PLUS data indices <- match(as.character(data$Home_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Home_Team[i]))){ pitcher.plus<-pitcher.stats$final.WAR[index] } } #HERE IS WAR DATA ############## RS.WAR = c(RS.WAR, data$Away_Score[i]*(pitcher.plus)) 

RS.WAR.park = c(RS.WAR.park, data$Away_Score[i]*(pitcher.plus)^(1/8)/((ballpark$BallparkEffect[data $Home_Team[i]])^(1))) 

#get w/l if(data$Home_Score[i]<data$Away_Score[i]){ wins <- wins+1 } else{ losses <- losses+1 } } } 

#get runs allowed for pythag WL for(i in 1:nrow(data)){ #if team is the home team if(data$Home_Team[i]==team){ RA=c(RA, data$Away_Score[i]) #get WAR PLUS data indices <- match(as.character(data$Home_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Home_Team[i]))){ 

48 

pitcher.plus<-pitcher.stats$final.WAR[index] 

} } #HERE IS THE WAR DATA ############## 

RA.WAR = c(RA.WAR, data$Away_Score[i]*(pitcher.plus)) 

RA.WAR.park = c(RA.WAR.park, data$Away_Score[i]*(pitcher.plus)^(1/8)/((ballpark$BallparkEffect[data $Home_Team[i]])^(1))) 

} 

#if team is the away team if(data$Away_Team[i]==team){ RA=c(RA, data$Home_Score[i]) #get WAR PLUS data indices <- match(as.character(data$Away_Pitcher[i]),pitcher.stats$Names.updated) for(index in indices){ 

if(identical(as.character(pitcher.stats$Team[index]),as.character(data$Away_Team[i]))){ pitcher.plus<-pitcher.stats$final.WAR[index] } } #HERE IS WAR DATA ############## 

RA.WAR = c(RA.WAR, data$Home_Score[i]*(pitcher.plus)) 

RA.WAR.park = c(RA.WAR.park, data$Home_Score[i]*(pitcher.plus)^(1/8)/((ballpark$BallparkEffect[data $Home_Team[i]])^(1))) 

} 

} 

#take sums over runs scored in every category# #regular RS and RA runs.score=sum(RS) runs.allow=sum(RA) #WAR runs.score.WAR=sum(RS.WAR) runs.allow.WAR=sum(RA.WAR) #WAR + park runs.score.WAR.park=sum(RS.WAR.park) runs.allow.WAR.park=sum(RA.WAR.park) 

#compute the pythag formula for regular PythagWL=(runs.score^(alpha))/(runs.score^(alpha)+runs.allow^(alpha)) #WAR 

PythagWL.WAR=(runs.score.WAR^(alpha))/(runs.score.WAR^(alpha)+runs.allow.WAR^(alpha)) PythagWL.WAR.park=(runs.score.WAR.park^(alpha))/(runs.score.WAR.park^(alpha)+runs.allow.WAR.park^(alpha)) 

#add in the pythags into their vectors teams.pythag=c(teams.pythag,PythagWL) teams.pythag.WAR=c(teams.pythag.WAR,PythagWL.WAR) teams.pythag.WAR.park=c(teams.pythag.WAR.park,PythagWL.WAR.park) 

#compute teams W/L for the season WL <- wins/(wins + losses) teamsWL=c(teamsWL, WL) 

} 

######### end of loop over teams ################## 

model.pythag=lm(teamsWL~teams.pythag) model.pythag.WAR=lm(teamsWL~teams.pythag.WAR) model.pythag.WAR.park = lm(teamsWL~teams.pythag.WAR.park) 

reg <- summary(model.pythag)$r.squared plus <- summary(model.pythag.WAR)$r.squared plus.park <- summary(model.pythag.WAR.park)$r.squared 

#summary(fit)$r.squared 

49 

pythag.table <- rbind(pythag.table, c(alpha,reg,plus,plus.park)) 

print(pythag.table) 

} ####### end of loop over pythag powers ################## colnames(pythag.table)<- c("Pythag.Exp", "Regular", "WAR", "WAR.Ballpark") 

sorted.table<-pythag.table[order(pythag.table$Regular),] 

#write.csv(sorted.table,"sorted.WAR.ballpark2007") 

50 

### APPENDIX D. 2007 MOMENTS CODE FOR _R_ 

#install.packages("moments") 

require("moments") #now bring in data #depends on the year data<-read.csv("/Users/victorluo/Documents/Williams College/Senior Year 13-14/thesis/Complete Season Data/ 2007completedata.csv") 

teams.retro=c("ANA", "ARI", "ATL", "BAL", "BOS", "CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU", "KCA", "LAN", "MIL", "MIN", "NYA", "NYN", "OAK", "PHI", "PIT", "SDN", "SEA", "SFN", "SLN", "TBA", "TEX", "TOR", "WAS") moment.dataframe<-data.frame() 

for(team in teams.retro){ RS<-c() RA<-c() #get runs scored for pythag WL #also get runs scored for WHIP pythag WL for (i in 1:nrow(data)){ #if the team is the home team if(data$Home_Team[i]==team){ RS=c(RS, data$Home_Score[i]) } #if the team is the away team if(data$Away_Team[i]==team){ RS=c(RS, data$Away_Score[i]) } } #get runs allowed for pythag WL for (i in 1:nrow(data)){ #if team is the home team if(data$Home_Team[i]==team){ RA=c(RA, data$Away_Score[i]) } #if team is the away team if(data$Away_Team[i]==team){ RA=c(RA, data$Home_Score[i]) } } #calculate moments team.moments<-all.moments(RS,order.max=4) 

moment.dataframe<-rbind(moment.dataframe, team.moments) 

} moment.dataframe<-moment.dataframe[,-1] moment.dataframe<-cbind(teams.retro,moment.dataframe) 

colnames(moment.dataframe)<-c("Team","First","Second","Third","Fourth") 

51 

APPENDIX E. 2011 LEAST SQUARES CODE 

# **Pythagorean Formula -2011 H2 betasL Analysis Victor Luo Thesis 2013 - 2014** 



**H*Multivariate statistics package needed*L Needs@"MultivariateStatistics`"D** 

- **H* combined weibulls... *L** 

- **W@x_, a1_, a2_, b1_, b2_, c_, d_D :=** 

- **If@x ¥ d * b1 + H1 - dL * b2, d * Hc ê a1L HHx - b1Lê a1L ^ Hc - 1L * Exp@ -HHx - b1Lê a1L ^cD +** 

- **H1 - dL * Hc ê a2L HHx - b2Lê a2L ^ Hc - 1L * Exp@ -HHx - b2Lê a2L ^cD, 0D;** 

- **H*defines weibull as function of 6 parameters, area under combined weibull in interval @sp,epD*L AW@sp_, ep_, a1_, a2_, b1_, b2_, c_, d_D :=** 

**If@sp ¥ d * b1 + H1 - dL * b2, H1 - dL * HN@-Exp@-HHep - b2Lê a2L ^cD + Exp@-HHsp - b2Lê a2L ^cDDL + d * HN@-Exp@-HHep - b1Lê a1L ^cD + Exp@-HHsp - b1Lê a1L ^cDDL, If@ep > d * b1 + H1 - dL * b2, d * HN@1 - Exp@-HHep - b1Lê a1L ^cDDL + H1 - dL * HN@1 - Exp@-HHep - b2Lê a2L ^cDDL, 0DD;** 

**H*Team scores*L** 

**H* Team guide follows *L** 

**H* AL EAST *L** 

**H* Team 1 = Red Sox*L** 

**H* Team 2 = Yankees*L H* Team 3 = Orioles*L H* Team 4 = Devil Rays*L** 

**H* Team 5 = Blue Jays*L** 

**TeamNames = 8"Boston Red Sox", "New York Yankees", "Baltimore Orioles", "Tampa Bay Devil Rays", "Toronto Blue Jays", "Minnesota Twins", "Chicago White Sox", "Cleveland Indians", "Detroit Tigers", "Kansas City Royals", "Los Angeles Angels", "Oakland Athletics", "Texas Rangers", "Seattle Mariners", "Atlanta Braves", "Philadelphia Phillies", "Florida Marlins", "New York Mets", "Washington Nationals", "St. Louis Cardinals", "Houston Astros", "Chicago Cubs", "Cincinnati Reds", "Pittsburgh Pirates", "Milwaukee Brewers", "Los Angeles Dodgers",** 

- **"San Francisco Giants", "San Diego Padres", "Colorado Rockies", "Arizona Diamondbacks" <;** 

- **NumGames = 162;** 

**NumTeams = 30; H* number of teams*L** 

**DoubleNumTeams = 2 * NumTeams; H* twice the number of teams, each team has RS and RA data *L TeamScore@1D = 85, 5, 1, 1, 4, 0, 9, 4, 4, 5, 2, 6, 4, 8, 9, 0, 5, 4, 4, 5, 7, 1, 4, 6, 4, 0, 3, 9, 7, 3, 0, 2, 4, 9, 2, 6, 3, 5, 6, 7, 8, 1, 4, 15, 3, 5, 2, 4, 14, 14, 6, 4, 0, 3, 7, 4, 8, 9, 6, 6, 11, 8, 5, 16, 14, 0, 3, 4, 10, 2, 12, 14, 4, 1, 1, 4, 4, 0, 1, 5, 7, 10, 2, 7, 3, 6, 10, 10, 4, 8, 6, 9, 1, 15, 2, 4, 7, 3, 12, 1, 13, 12, 3, 1, 10, 5, 6, 3, 4, 3, 2, 10, 3, 8, 4, 2, 6, 4, 3, 3, 2, 0, 4, 7, 4, 6, 0, 11, 13, 6, 5, 9, 4, 2, 9, 2, 0, 12, 4, 0, 14, 10, 4, 2, 5, 1, 18, 4, 2, 4, 3, 5, 5, 18, 5, 4, 1, 2, 7, 3, 8, 3<; TeamScore@1 + NumTeamsD = 89, 12, 5, 3, 8, 1, 6, 9, 0, 16, 3, 7, 1, 1, 1, 5, 3, 2, 3, 0, 0, 4, 5, 2, 5, 2, 2, 5, 3, 5, 11, 9, 0, 5, 1, 7, 9, 4, 0, 5, 7, 0, 3, 5, 9, 1, 3, 2, 2, 1, 3, 3, 3, 7, 10, 7, 6, 8, 3, 4, 6, 3, 1, 4, 1, 4, 0, 2, 4, 4, 3, 5, 5, 5, 3, 6, 2, 5, 2, 2, 5, 4, 1, 9, 2, 4, 4, 3, 0, 6, 9, 5, 0, 10, 6, 0, 4, 1, 8, 3, 9, 5, 4, 3, 2, 3, 9, 2, 3, 7, 3, 4, 2, 6, 3, 5, 4, 5, 5, 1, 6, 4, 3, 1, 9, 1, 4, 5, 2, 0, 15, 3, 0, 5, 5, 4, 10, 7, 11, 1, 0, 11, 7, 7, 6, 9, 6, 5, 9, 3, 4, 8, 6, 9, 7, 6, 9, 6, 4, 6, 7, 4<; TeamScore@2D = 86, 10, 7, 4, 4, 4, 6, 9, 0, 7, 6, 3, 5, 6, 5, 6, 15, 6, 0, 2, 3, 12, 3, 5, 5, 5, 2, 0, 3, 4, 5, 12, 3, 3, 5, 4, 0, 5, 5, 6, 4, 13, 1, 7, 9, 3, 5, 7, 3, 4, 7, 5, 10, 4, 2, 3, 5, 4, 6, 3, 11, 4, 9, 0, 12, 12, 3, 1, 4, 10, 5, 4, 2, 2, 8, 6, 12, 5, 5, 5, 5, 2, 3, 9, 3, 1, 5, 1, 7, 1, 4, 7, 5, 2, 4, 1, 17, 3, 7, 10, 4, 2, 2, 8, 17, 4, 3, 6, 18, 7, 3, 4, 2, 4, 9, 6, 1, 9, 7, 9, 4, 8, 8, 4, 3, 5, 4, 22, 5, 0, 8, 3, 5, 5, 4, 3, 6, 9, 11, 5, 4, 4, 1, 0, 6, 9, 3, 1, 4, 7, 0, 6, 5, 4, 4, 8, 9, 6, 4, 2, 3, 7<; TeamScore@2 + NumTeamsD = 83, 6, 10, 3, 5, 3, 9, 4, 4, 4, 5, 5, 2, 5, 6, 2, 3, 3, 2, 3, 1, 3, 5, 4, 2, 3, 4, 4, 6, 1, 7, 5, 1, 4, 11, 5, 6, 7, 6, 2, 1, 2, 2, 3, 3, 7, 4, 3, 4, 5, 1, 0, 3, 2, 3, 2, 3, 6, 11, 8, 7, 0, 1, 1, 4, 4, 2, 3, 3, 4, 3, 2, 10, 4, 3, 4, 2, 2, 0, 1, 2, 3, 6, 2, 5, 5, 4, 0, 16, 7, 1, 2, 4, 3, 0, 2, 7, 4, 5, 3, 1, 9, 4, 3, 3, 2, 2, 0, 7, 2, 2, 10, 3, 6, 3, 5, 5, 2, 4, 7, 5, 4, 1, 9, 0, 6, 6, 9, 12,** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

52 

**2** _leastsquares.nb_ 

**2, 3, 2, 2, 9, 2, 2, 4, 3, 10, 3, 5, 5, 2, 6, 5, 3, 2, 2, 5, 6, 3, 4, 0, 2, 2, 15, 1, 2, 7, 5, 5, 8<; TeamScore@3D = 84, 3, 5, 5, 3, 9, 5, 1, 0, 4, 5, 2, 3, 2, 3, 11, 5, 1, 3, 3, 4, 5, 2, 10, 6, 6, 2, 5, 3, 1, 2, 2, 3, 7, 4, 2, 0, 6, 9, 7, 1, 2, 5, 8, 2, 5, 9, 6, 2, 2, 4, 3, 2, 2, 4, 5, 4, 4, 4, 3, 7, 5, 6, 5, 1, 4, 4, 2, 7, 8, 3, 4, 5, 5, 7, 2, 1, 6, 0, 4, 5, 4, 2, 5, 4, 3, 0, 6, 4, 5, 6, 8, 10, 6, 0, 1, 3, 3, 12, 0, 5, 4, 3, 3, 2, 8, 2, 4, 4, 6, 2, 6, 3, 6, 3, 4, 5, 8, 6, 4, 5, 3, 8, 1, 4, 8, 6, 6, 12, 2, 3, 2, 6, 0, 6, 3, 3, 1, 10, 3, 5, 5, 2, 4, 5, 2, 4, 6, 8, 6, 2, 6, 9, 7, 6, 6, 3, 6, 6, 6, 7, 4<; TeamScore@3 + NumTeamsD = 81, 1, 1, 1, 7, 5, 0, 13, 3, 7, 6, 8, 8, 4, 5, 0, 4, 3, 15, 6, 1, 4, 6, 4, 2, 4, 6, 6, 2, 9, 6, 8, 5, 6, 2, 1, 3, 0, 3, 8, 4, 13, 17, 3, 1, 3, 2, 5, 6, 4, 6, 4, 3, 1, 8, 3, 7, 2, 0, 2, 0, 7, 9, 6, 4, 3, 8, 4, 4, 3, 9, 5, 4, 10, 5, 6, 5, 9, 4, 5, 4, 13, 4, 13, 10, 10, 4, 8, 8, 6, 5, 3, 15, 2, 4, 6, 2, 9, 4, 3, 8, 2, 8, 17, 4, 2, 6, 9, 5, 2, 7, 7, 4, 4, 6, 5, 6, 5, 2, 8, 6, 8, 9, 7, 1, 1, 1, 1, 5, 0, 8, 3, 5, 13, 8, 2, 6, 8, 11, 5, 4, 4, 0, 5, 6, 5, 2, 2, 3, 2, 11, 5, 18, 5, 4, 5, 4, 5, 10, 3, 8, 3<; TeamScore@4D = 81, 1, 1, 3, 1, 1, 9, 2, 1, 16, 3, 4, 5, 4, 2, 5, 2, 4, 2, 4, 6, 2, 8, 15, 6, 5, 2, 5, 3, 2, 3, 6, 8, 5, 4, 8, 7, 3, 0, 3, 6, 2, 6, 2, 3, 3, 4, 3, 6, 5, 3, 7, 5, 5, 0, 2, 0, 3, 6, 5, 4, 4, 0, 7, 9, 1, 4, 0, 2, 5, 7, 2, 8, 1, 6, 5, 7, 14, 0, 4, 3, 3, 5, 8, 0, 2, 12, 5, 4, 0, 9, 5, 0, 4, 3, 0, 2, 4, 4, 5, 5, 1, 4, 10, 8, 2, 8, 1, 9, 7, 8, 0, 4, 2, 4, 8, 4, 5, 2, 1, 6, 4, 3, 8, 8, 2, 1, 3, 0, 6, 6, 12, 3, 0, 4, 2, 2, 6, 8, 5, 0, 5, 7, 6, 9, 5, 2, 2, 9, 3, 4, 8, 0, 2, 2, 15, 1, 6, 5, 5, 5, 8<; TeamScore@4 + NumTeamsD = 84, 3, 5, 5, 5, 5, 7, 4, 6, 5, 2, 3, 2, 3, 4, 0, 1, 1, 9, 6, 4, 0, 2, 3, 1, 8, 1, 6, 2, 3, 1, 2, 2, 3, 5, 2, 4, 0, 6, 9, 5, 6, 5, 3, 5, 5, 0, 6, 7, 0, 7, 0, 11, 4, 3, 8, 7, 2, 9, 1, 1, 3, 7, 5, 6, 2, 0, 3, 4, 1, 4, 1, 4, 5, 3, 1, 2, 10, 5, 3, 4, 5, 1, 3, 7, 3, 5, 1, 5, 1, 6, 9, 1, 5, 2, 4, 1, 10, 5, 0, 7, 6, 13, 8, 0, 3, 1, 3, 1, 6, 4, 8, 5, 1, 0, 7, 1, 1, 9, 3, 2, 0, 2, 0, 7, 5, 2, 2, 2, 1, 5, 0, 7, 2, 1, 7, 3, 3, 1, 1, 8, 4, 2, 5, 1, 2, 4, 6, 2, 4, 3, 5, 5, 4, 4, 8, 5, 2, 2, 2, 3, 7<; TeamScore@5D = 813, 6, 3, 7, 5, 1, 3, 5, 1, 7, 2, 8, 7, 1, 1, 1, 6, 2, 6, 4, 0, 6, 10, 6, 5, 5, 4, 2, 2, 3, 1, 7, 0, 2, 5, 7, 9, 2, 9, 11, 4, 5, 3, 2, 7, 2, 7, 4, 3, 1, 4, 9, 13, 11, 3, 9, 8, 3, 7, 2, 8, 9, 2, 1, 4, 1, 6, 4, 3, 3, 4, 1, 0, 1, 1, 5, 6, 5, 2, 6, 2, 2, 6, 3, 7, 9, 2, 4, 4, 11, 5, 7, 16, 7, 1, 2, 6, 11, 7, 2, 4, 3, 4, 3, 8, 3, 0, 7, 3, 1, 6, 5, 2, 7, 1, 8, 3, 1, 11, 5, 5, 13, 5, 7, 0, 1, 1, 4, 4, 6, 1, 5, 0, 7, 5, 13, 8, 2, 4, 3, 1, 0, 11, 7, 0, 5, 6, 6, 5, 5, 6, 3, 3, 6, 2, 4, 5, 2, 2, 3, 1, 3<; TeamScore@5 + NumTeamsD = 83, 1, 4, 6, 3, 2, 2, 6, 3, 8, 3, 3, 6, 4, 8, 9, 5, 6, 4, 6, 2, 4, 3, 7, 2, 3, 5, 5, 3, 2, 3, 4, 9, 5, 10, 6, 3, 0, 3, 3, 2, 6, 2, 5, 5, 3, 3, 5, 7, 3, 2, 8, 4, 1, 6, 13, 4, 5, 4, 3, 5, 8, 3, 5, 16, 14, 5, 1, 4, 2, 0, 2, 2, 5, 5, 4, 3, 0, 4, 7, 1, 6, 7, 5, 4, 7, 3, 6, 5, 7, 4, 1, 7, 1, 4, 7, 5, 6, 5, 12, 5, 0, 12, 0, 5, 2, 3, 3, 1, 9, 7, 4, 6, 2, 4, 4, 10, 5, 2, 4, 6, 7, 1, 0, 2, 5, 0, 6, 3, 9, 6, 6, 12, 3, 6, 0, 6, 3, 6, 9, 0, 14, 10, 4, 2, 4, 5, 18, 4, 4, 7, 0, 2, 10, 7, 3, 1, 6, 5, 4, 2, 2<;** 

**H* Team 6 = Twins*L H* Team 7 = White Sox*L H* Team 8 = Indians*L H* Team 9 = Tigers*L H* Team 10 = Royals*L** 

**TeamScore@6D = 83, 1, 4, 3, 5, 3, 2, 0, 3, 4, 5, 3, 2, 3, 4, 5, 0, 4, 3, 10, 4, 2, 3, 1, 3, 2, 3, 1, 3, 9, 0, 5, 1, 2, 7, 0, 3, 3, 2, 2, 4, 11, 7, 6, 2, 7, 4, 0, 5, 1, 5, 5, 7, 2, 8, 5, 7, 6, 6, 0, 3, 5, 3, 8, 6, 4, 1, 6, 1, 5, 9, 1, 1, 3, 1, 2, 0, 6, 1, 6, 7, 9, 7, 3, 5, 6, 8, 3, 6, 8, 1, 4, 4, 2, 3, 2, 7, 2, 2, 4, 2, 6, 9, 7, 1, 9, 3, 3, 1, 11, 1, 3, 1, 0, 6, 3, 5, 2, 1, 9, 1, 6, 4, 1, 9, 0, 1, 1, 1, 1, 1, 4, 11, 0, 6, 7, 13, 6, 1, 1, 0, 0, 5, 4, 2, 1, 0, 3, 6, 4, 5, 4, 4, 4, 3, 5, 2, 6, 6, 3, 7, 1<; TeamScore@6 + NumTeamsD = 813, 6, 3, 4, 4, 4, 1, 1, 5, 3, 10, 4, 5, 4, 2, 3, 11, 5, 1, 3, 3, 8, 15, 6, 4, 11, 10, 0, 2, 2, 4, 9, 2, 10, 9, 2, 9, 11, 5, 1, 3, 1, 8, 9, 3, 8, 2, 3, 6, 0, 6, 6, 8, 4, 2, 2, 2, 0, 4, 1, 2, 4, 9, 1, 1, 1, 0, 5, 0, 4, 2, 5, 2, 4, 11, 6, 15, 4, 0, 2, 8, 7, 0, 2, 12, 2, 5, 4, 3, 4, 2, 3, 3, 5, 6, 1, 5, 6, 8, 1, 5, 20, 8, 2, 4, 5, 8, 7, 5, 4, 7, 5, 6, 7, 8, 4, 2, 3, 3, 6, 7, 5, 8, 8, 4, 3, 4, 8, 6, 6, 8, 6, 4, 3, 8, 6, 5, 10, 4, 2, 4, 3, 4, 8, 3, 2, 4, 7, 7, 10, 6, 6, 5, 5, 2, 6, 8, 7, 4, 7, 4, 0<; TeamScore@7D = 815, 8, 1, 6, 10, 5, 7, 4, 6, 1, 6, 4, 3, 2, 2, 0, 1, 1, 9, 3, 0, 0, 2, 3, 1, 3, 4, 2, 4, 6, 0, 2, 2, 6, 5, 8, 2, 6, 4, 2, 4, 0, 4, 1, 8, 4, 9, 8, 0, 8, 1, 3, 2, 8, 4, 7, 10, 7, 6, 2, 3, 3, 5, 4, 9, 5, 3, 5, 1, 0, 1, 6, 8, 3, 3, 4, 5, 3, 1, 2, 3, 6, 6, 1, 1, 5, 3, 1, 2, 5, 4, 3, 8, 5, 3, 5, 2, 1, 3, 4, 6, 4, 2, 3, 2, 3, 2, 0, 7, 2, 5, 6, 7, 7, 4, 4, 6, 1, 5, 6, 8, 1, 2, 4, 3, 10, 4, 0, 4, 3, 9, 3, 8, 6, 1, 8, 2, 2, 4, 3, 4, 8, 4, 7, 3, 4, 0, 5, 2, 6, 3, 10, 3, 5, 8, 2, 1, 6, 1, 4, 2, 2<; TeamScore@7 + NumTeamsD = 810, 3, 7, 7, 7, 1, 9, 2, 1, 2, 5, 7, 4, 7, 4, 5, 2, 4, 2, 9, 9, 3, 0, 2, 3, 12, 10, 6, 6, 2, 1, 3, 3, 0, 2, 0, 6, 4, 3, 6, 3, 4, 3, 0, 2, 6, 2, 3, 4, 6, 2, 1, 4, 9, 13, 3, 7, 4, 4, 4, 7, 1, 1, 7, 4, 7, 2, 4, 4, 1, 4, 2, 2, 6, 2, 3, 9, 0, 2, 3, 2, 4, 4, 0, 3, 4, 5, 4, 6, 8, 3, 6, 2, 0, 4, 2, 4, 2, 0, 2, 3, 5, 1, 1, 10, 5, 3, 6, 18, 7, 3, 1, 0, 6, 3, 6, 3, 5, 4, 2, 7, 4, 4, 7, 2, 0, 5, 8, 2, 0, 3, 0, 6, 7, 8, 9, 18, 1, 0, 0, 5, 1, 8, 3, 7, 14, 5, 6, 7, 7, 10, 5, 4, 4, 4, 11, 11, 3, 2, 3, 1, 3<; TeamScore@8D = 810, 3, 7, 3, 8, 1, 12, 2, 6, 4, 0, 3, 8, 8, 4, 7, 4, 7, 2, 3, 3, 9, 7, 8, 9, 3, 5, 4, 1, 4, 1, 4, 5, 5, 2, 4, 5, 19, 7, 0, 2, 5, 2, 12, 3, 2, 2, 0, 7, 0, 1, 6, 13, 4, 2, 0, 0, 4, 1, 2, 7, 0, 1, 1, 0, 6, 2, 5, 5, 5, 7, 3, 4, 3, 0, 1, 5, 4, 6, 8, 3, 5, 6, 2, 5, 5, 7, 4, 1, 8, 6, 5, 3, 5, 6, 1, 5, 0, 2, 3, 1, 1, 0, 5, 3, 9, 2, 3, 7, 7, 7, 3, 3, 10, 3, 3, 3, 7, 4, 4, 1, 1, 7, 2, 7, 7, 2, 2, 8, 1, 2, 6, 4, 0, 5, 1, 9, 2, 1, 6, 1, 8, 3, 7, 4, 1, 4, 7, 10, 6, 6, 4, 4, 4, 11, 6, 8, 7, 4, 0, 6, 4<; TeamScore@8 + NumTeamsD = 815, 8, 1, 1, 4, 0, 3, 1, 4, 0, 2, 4, 2, 3, 2, 3, 5, 5, 3, 10, 4, 4, 2, 2, 5, 2, 4, 1, 3, 3, 2, 3, 6, 4, 8, 7, 4, 1, 3, 1, 8, 4, 1, 4, 2, 4, 14, 5, 3, 7, 11, 3, 9, 7, 11, 4, 2, 6, 0, 3, 11, 4, 9, 0, 4, 4, 6, 1, 1, 2, 8, 4, 3, 4, 1, 3, 4, 6, 2, 2, 1, 7, 3, 9, 3, 4, 11, 5, 7, 4, 5, 6, 8, 2, 3, 2, 7, 3, 4, 2, 2, 3, 12, 2, 5, 6, 3, 4, 3, 8, 5, 5, 2, 3, 4, 2, 1, 8, 1, 2, 4, 10, 8, 3, 5, 12, 9, 1, 7, 2, 1, 2, 3, 7, 4, 5, 6, 4, 10, 8, 8, 4, 7, 3, 10, 9, 7, 6, 4, 5, 12, 3, 5, 8, 2, 5, 2, 6, 6, 14, 9, 5<; TeamScore@9D = 83, 6, 10, 1, 7, 5, 5, 1, 5, 0, 5, 3, 3, 8, 2, 1, 8, 3, 3, 9, 9, 3, 3, 1, 2, 5, 2, 4, 3,** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

53 

_leastsquares.nb_ **3** 

**4, 4, 6, 4, 9, 5, 10, 10, 9, 3, 3, 2, 0, 3, 1, 2, 2, 6, 7, 1, 3, 3, 3, 6, 8, 4, 4, 4, 7, 13, 8, 3, 4, 2, 8, 3, 2, 4, 4, 6, 6, 4, 9, 0, 1, 7, 6, 6, 8, 4, 3, 9, 5, 3, 3, 6, 1, 0, 5, 3, 6, 6, 2, 2, 0, 4, 8, 5, 6, 8, 1, 5, 3, 5, 1, 7, 12, 1, 3, 6, 5, 2, 4, 4, 3, 2, 3, 4, 5, 6, 5, 6, 7, 5, 4, 10, 8, 5, 2, 2, 2, 8, 6, 4, 5, 2, 5, 8, 8, 9, 18, 4, 10, 8, 8, 3, 2, 14, 5, 6, 1, 3, 3, 3, 2, 6, 5, 4, 5, 10, 14, 9, 5<; TeamScore@9 + NumTeamsD = 86, 10, 7, 5, 3, 9, 2, 3, 9, 2, 4, 2, 0, 4, 6, 5, 3, 13, 2, 3, 0, 0, 7, 10, 7, 9, 3, 5, 5, 2, 0, 3, 7, 0, 2, 5, 2, 7, 1, 0, 4, 1, 4, 10, 6, 0, 3, 6, 14, 6, 4, 0, 5, 7, 2, 6, 2, 3, 7, 1, 7, 1, 3, 1, 7, 1, 0, 6, 2, 13, 5, 1, 4, 6, 5, 7, 0, 3, 2, 14, 16, 2, 4, 15, 3, 5, 1, 4, 1, 4, 13, 1, 8, 5, 3, 3, 7, 2, 2, 4, 2, 6, 4, 2, 12, 2, 5, 2, 5, 4, 5, 3, 3, 4, 3, 10, 3, 4, 5, 8, 9, 1, 6, 1, 1, 7, 2, 1, 3, 0, 1, 4, 11, 9, 1, 4, 11, 1, 8, 2, 2, 1, 6, 4, 2, 1, 4, 0, 5, 6, 1, 5, 0, 10, 3, 6, 3, 6, 6, 0, 6, 4<; TeamScore@10D = 82, 2, 5, 12, 7, 7, 2, 3, 9, 3, 10, 5, 6, 7, 2, 3, 5, 5, 3, 6, 1, 7, 4, 2, 2, 4, 11, 10, 6, 2, 9, 2, 4, 2, 1, 4, 11, 1, 0, 1, 3, 4, 2, 3, 0, 8, 3, 2, 5, 12, 1, 6, 8, 7, 2, 2, 2, 2, 0, 3, 5, 8, 3, 4, 5, 9, 7, 1, 4, 5, 4, 4, 2, 2, 3, 4, 3, 6, 3, 2, 1, 0, 6, 16, 4, 5, 4, 1, 4, 13, 1, 4, 2, 3, 3, 2, 4, 2, 10, 5, 0, 3, 9, 5, 4, 12, 2, 5, 2, 6, 9, 3, 3, 4, 1, 0, 7, 1, 5, 4, 2, 4, 7, 5, 3, 1, 9, 1, 6, 3, 9, 1, 7, 2, 9, 1, 4, 11, 4, 5, 6, 11, 7, 0, 1, 3, 4, 2, 4, 7, 7, 7, 10, 5, 10, 3, 11, 3, 2, 7, 4, 0<; TeamScore@10 + NumTeamsD = 84, 1, 4, 9, 6, 10, 5, 1, 5, 4, 5, 1, 5, 0, 3, 7, 4, 7, 2, 11, 3, 8, 9, 7, 8, 3, 2, 3, 5, 3, 1, 3, 3, 5, 3, 3, 5, 3, 3, 19, 7, 5, 1, 0, 3, 9, 5, 9, 6, 7, 10, 7, 10, 3, 0, 8, 5, 7, 6, 2, 8, 9, 2, 2, 7, 0, 4, 2, 8, 4, 5, 5, 7, 3, 5, 6, 2, 3, 4, 4, 4, 9, 9, 8, 5, 3, 1, 3, 6, 6, 2, 8, 1, 4, 4, 5, 2, 1, 4, 4, 5, 1, 13, 12, 3, 0, 5, 3, 8, 2, 4, 4, 4, 3, 2, 4, 8, 4, 1, 5, 6, 7, 9, 4, 4, 7, 4, 6, 4, 4, 6, 2, 8, 1, 5, 2, 5, 8, 5, 1, 9, 6, 4, 7, 4, 7, 2, 1, 0, 3, 2, 6, 3, 10, 2, 6, 1, 6, 1, 3, 7, 1<;** 

**H* AL WEST *L H* Team 11 = Angels*L H* Team 12 = Athletics*L H* Team 13 = Rangers*L H* Team 14 = Mariners*L** 

**TeamScore@11D = 84, 1, 4, 9, 5, 5, 2, 6, 3, 0, 2, 4, 4, 7, 4, 1, 15, 4, 2, 3, 0, 0, 5, 8, 1, 8, 1, 6, 5, 3, 5, 11, 2, 3, 6, 0, 6, 4, 1, 3, 4, 4, 0, 0, 1, 9, 4, 4, 4, 1, 4, 3, 6, 0, 6, 10, 3, 0, 3, 2, 3, 1, 1, 3, 2, 7, 0, 6, 4, 1, 4, 1, 7, 2, 2, 6, 8, 6, 2, 4, 11, 1, 0, 7, 3, 5, 1, 4, 5, 4, 9, 4, 3, 4, 3, 1, 0, 9, 1, 6, 2, 9, 2, 2, 3, 12, 2, 5, 2, 5, 4, 7, 1, 1, 2, 6, 3, 5, 5, 2, 4, 4, 3, 3, 2, 8, 9, 7, 5, 8, 7, 8, 5, 3, 13, 1, 4, 5, 10, 4, 7, 1, 3, 2, 6, 5, 3, 6, 4, 3, 2, 11, 2, 10, 7, 3, 1, 4, 5, 3, 3, 1<; TeamScore@11 + NumTeamsD = 82, 2, 5, 12, 3, 1, 3, 5, 1, 4, 0, 3, 3, 2, 2, 7, 4, 1, 4, 4, 5, 7, 0, 3, 2, 5, 2, 5, 9, 7, 3, 0, 1, 4, 5, 8, 2, 6, 4, 2, 5, 5, 14, 3, 2, 0, 5, 1, 1, 6, 1, 4, 5, 1, 5, 8, 7, 2, 2, 3, 5, 5, 4, 4, 4, 5, 9, 3, 0, 3, 3, 6, 3, 1, 5, 5, 3, 1, 3, 3, 5, 0, 5, 1, 1, 1, 0, 5, 1, 3, 3, 2, 5, 2, 4, 9, 7, 8, 0, 1, 3, 3, 3, 1, 1, 7, 12, 1, 3, 1, 11, 1, 0, 5, 1, 4, 9, 6, 1, 11, 5, 8, 7, 4, 1, 3, 8, 1, 4, 0, 11, 4, 9, 5, 6, 2, 3, 13, 6, 1, 3, 2, 1, 1, 0, 6, 6, 3, 1, 8, 6, 2, 3, 6, 2, 4, 3, 2, 6, 4, 10, 3<; TeamScore@12D = 82, 2, 7, 6, 3, 2, 1, 1, 5, 2, 5, 7, 0, 4, 6, 5, 5, 3, 0, 0, 9, 5, 0, 3, 2, 3, 2, 7, 5, 1, 3, 3, 3, 3, 5, 7, 2, 3, 6, 3, 5, 14, 3, 1, 1, 0, 4, 1, 6, 1, 4, 6, 4, 6, 0, 3, 2, 6, 8, 3, 2, 0, 2, 4, 7, 2, 4, 4, 2, 8, 5, 4, 2, 7, 2, 1, 0, 4, 1, 1, 0, 4, 5, 2, 7, 1, 2, 2, 0, 5, 6, 0, 5, 2, 4, 9, 3, 7, 7, 4, 5, 7, 6, 13, 8, 5, 8, 7, 4, 2, 4, 4, 8, 5, 4, 4, 10, 1, 1, 6, 2, 8, 6, 0, 2, 5, 0, 6, 6, 9, 15, 3, 0, 1, 2, 3, 7, 9, 3, 8, 6, 4, 7, 4, 8, 1, 6, 3, 1, 6, 1, 5, 0, 2, 2, 4, 3, 2, 6, 2, 7, 2<; TeamScore@12 + NumTeamsD = 86, 5, 1, 7, 5, 1, 2, 0, 3, 1, 6, 4, 3, 8, 2, 1, 0, 5, 1, 4, 1, 2, 5, 8, 1, 1, 11, 2, 4, 4, 1, 4, 2, 4, 2, 2, 7, 4, 2, 4, 4, 0, 4, 11, 2, 3, 5, 4, 1, 4, 3, 2, 2, 4, 5, 10, 4, 8, 9, 6, 4, 4, 3, 9, 5, 3, 5, 7, 1, 4, 2, 2, 1, 3, 3, 4, 1, 1, 3, 0, 3, 5, 4, 4, 2, 2, 4, 0, 6, 8, 7, 2, 3, 4, 3, 1, 8, 5, 17, 3, 7, 5, 1, 4, 10, 9, 3, 3, 8, 4, 7, 8, 0, 4, 1, 8, 3, 9, 7, 7, 6, 4, 5, 7, 0, 1, 1, 5, 4, 22, 5, 9, 4, 2, 6, 4, 0, 2, 0, 5, 11, 7, 0, 13, 7, 8, 3, 6, 4, 1, 3, 3, 3, 7, 3, 3, 1, 4, 5, 4, 0, 0<; TeamScore@13D = 89, 12, 5, 6, 3, 7, 0, 13, 3, 2, 4, 2, 5, 2, 5, 7, 4, 1, 11, 3, 8, 4, 3, 7, 2, 1, 11, 2, 4, 3, 5, 1, 1, 7, 5, 2, 7, 4, 2, 5, 4, 3, 5, 1, 2, 0, 2, 4, 6, 2, 7, 10, 7, 11, 4, 3, 7, 11, 4, 2, 7, 1, 7, 4, 9, 1, 1, 4, 4, 2, 6, 5, 2, 8, 5, 3, 8, 5, 5, 7, 3, 0, 15, 5, 4, 13, 4, 13, 6, 8, 7, 2, 5, 4, 5, 3, 7, 8, 0, 12, 5, 0, 20, 8, 2, 4, 2, 3, 3, 5, 4, 5, 8, 5, 5, 9, 7, 3, 9, 7, 7, 8, 7, 4, 1, 7, 2, 0, 4, 5, 2, 0, 11, 4, 9, 2, 1, 7, 10, 7, 11, 1, 8, 4, 13, 7, 8, 10, 9, 7, 0, 7, 3, 7, 3, 3, 5, 7, 12, 4, 10, 3<; TeamScore@13 + NumTeamsD = 85, 5, 1, 4, 2, 3, 5, 1, 0, 0, 5, 3, 3, 5, 6, 1, 15, 4, 6, 1, 7, 6, 10, 6, 5, 3, 2, 7, 5, 4, 2, 3, 4, 5, 12, 7, 2, 1, 3, 4, 0, 4, 4, 2, 3, 2, 0, 0, 8, 1, 12, 1, 6, 5, 5, 0, 4, 2, 0, 0, 13, 8, 3, 5, 3, 8, 6, 12, 12, 3, 2, 4, 4, 3, 4, 5, 1, 14, 8, 3, 2, 7, 5, 9, 6, 4, 2, 5, 0, 5, 6, 0, 0, 0, 1, 1, 0, 9, 1, 2, 4, 3, 6, 9, 7, 1, 3, 0, 7, 6, 5, 2, 7, 7, 3, 2, 6, 4, 1, 1, 6, 4, 3, 3, 2, 4, 3, 10, 0, 11, 13, 6, 7, 8, 5, 0, 4, 2, 0, 12, 4, 5, 0, 5, 4, 8, 1, 4, 1, 4, 4, 6, 0, 2, 2, 4, 3, 3, 5, 3, 3, 1<; TeamScore@14D = 86, 5, 1, 4, 2, 3, 3, 1, 4, 8, 3, 3, 1, 5, 0, 3, 3, 13, 2, 1, 4, 1, 2, 7, 10, 7, 5, 2, 2, 4, 2, 3, 3, 0, 2, 6, 2, 1, 4, 5, 1, 3, 2, 4, 4, 6, 8, 2, 3, 4, 5, 1, 4, 3, 1, 8, 7, 2, 9, 1, 1, 7, 1, 3, 1, 7, 3, 0, 3, 4, 1, 2, 5, 1, 0, 5, 2, 2, 1, 4, 3, 6, 0, 3, 2, 4, 0, 1, 3, 3, 2, 0, 0, 1, 1, 5, 6, 5, 4, 1, 8, 3, 1, 9, 0, 3, 1, 8, 4, 7, 0, 5, 1, 2, 6, 4, 4, 5, 5, 6, 7, 1, 2, 0, 7, 3, 5, 12, 9, 2, 0, 3, 5, 6, 2, 3, 2, 0, 5, 3, 2, 1, 4, 7, 2, 1, 3, 2, 2, 4, 6, 0, 12, 5, 5, 2, 3, 3, 5, 4, 0, 0<; TeamScore@14 + NumTeamsD = 82, 2, 7, 6, 3, 7, 12, 2, 6, 7, 2, 8, 5, 6, 7, 2, 8, 3, 3, 0, 0, 9, 5, 3, 1, 2, 4, 0, 3, 3, 5, 1, 2, 6, 5, 7, 4, 2, 5, 2, 2, 0, 1, 1, 0, 1, 7, 4, 0, 3, 4, 7, 3, 2, 2, 2, 0, 3, 6, 3, 5, 4, 4, 2, 8, 3, 6, 4, 1, 2, 5, 0, 6, 2, 1, 1, 4, 1, 3, 5, 5, 0, 1, 1, 1, 2, 2, 5, 4, 9, 4, 5, 4, 5, 3, 6, 11, 7, 7, 3, 12, 10, 4, 2, 8, 2, 8, 4, 2, 4, 1, 1, 2, 9, 7, 3, 6, 4, 3, 5, 13, 5, 3, 8, 8, 2, 7, 7, 2, 4, 3, 9, 3, 13, 1, 4, 9, 3, 8, 7, 1, 3, 1, 3, 4, 2, 9, 3, 1, 0, 7, 3, 6, 4, 4, 3, 5, 7, 12, 2, 7, 2<;** 

**H* NL EAST *L** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

54 

**4** _leastsquares.nb_ 

**H* Team 15 = Braves*L H* Team 16 = Phillies*L H* Team 17 = Marlins*L H* Team 18 = Mets*L H* Team 19 = Expos*L TeamScore@15D = 82, 3, 11, 2, 0, 4, 2, 6, 2, 0, 5, 1, 5, 4, 4, 2, 2, 10, 1, 3, 4, 5, 9, 3, 8, 7, 3, 2, 6, 6, 8, 8, 2, 5, 0, 5, 6, 3, 6, 4, 5, 3, 3, 3, 4, 1, 0, 5, 1, 2, 4, 1, 7, 2, 2, 4, 4, 6, 0, 4, 1, 3, 3, 11, 6, 4, 3, 3, 0, 9, 2, 4, 4, 2, 5, 5, 2, 10, 1, 3, 5, 5, 4, 5, 4, 4, 5, 9, 6, 2, 4, 1, 11, 2, 9, 7, 3, 2, 9, 6, 2, 3, 1, 4, 2, 2, 5, 5, 1, 3, 3, 6, 4, 7, 6, 8, 4, 6, 10, 4, 5, 5, 2, 5, 1, 4, 8, 1, 3, 5, 2, 8, 0, 2, 3, 5, 6, 1, 4, 0, 3, 2, 6, 5, 3, 3, 3, 4, 7, 4, 2, 1, 5, 5, 4, 0, 7, 1, 0, 2, 1, 3<; TeamScore@15 + NumTeamsD = 80, 6, 2, 1, 1, 5, 4, 3, 10, 3, 0, 5, 6, 2, 0, 3, 4, 1, 6, 5, 1, 2, 6, 5, 2, 0, 5, 3, 5, 2, 3, 0, 1, 0, 3, 2, 7, 7, 5, 5, 3, 2, 2, 1, 5, 2, 9, 4, 4, 0, 2, 5, 6, 1, 3, 5, 3, 3, 5, 6, 0, 2, 2, 4, 3, 1, 8, 4, 4, 8, 6, 5, 2, 0, 1, 1, 11, 1, 4, 1, 4, 3, 0, 4, 5, 1, 3, 1, 3, 3, 1, 14, 1, 5, 8, 4, 12, 3, 6, 4, 11, 4, 3, 3, 1, 5, 0, 1, 3, 5, 9, 4, 1, 11, 5, 5, 3, 2, 4, 8, 6, 4, 1, 7, 0, 2, 1, 0, 0, 4, 3, 3, 6, 9, 1, 2, 8, 2, 3, 9, 6, 3, 5, 1, 4, 4, 6, 5, 1, 1, 12, 0, 7, 6, 0, 4, 4, 4, 3, 4, 7, 4<; TeamScore@16D = 85, 9, 7, 1, 10, 11, 3, 10, 3, 4, 3, 4, 3, 3, 3, 0, 4, 3, 2, 4, 3, 0, 5, 8, 10, 2, 1, 4, 7, 7, 0, 3, 2, 6, 1, 5, 5, 3, 2, 1, 1, 2, 1, 3, 2, 0, 10, 3, 5, 10, 6, 5, 5, 5, 2, 1, 1, 3, 7, 3, 2, 2, 3, 7, 7, 4, 9, 8, 5, 3, 2, 5, 0, 10, 4, 2, 1, 1, 3, 5, 2, 2, 7, 5, 4, 1, 14, 6, 3, 1, 14, 7, 2, 8, 1, 4, 9, 3, 8, 5, 4, 7, 1, 1, 10, 7, 6, 4, 5, 8, 3, 9, 2, 1, 5, 2, 9, 2, 11, 2, 9, 4, 4, 5, 4, 10, 9, 4, 5, 3, 9, 3, 6, 5, 4, 4, 9, 6, 3, 7, 5, 3, 2, 1, 2, 1, 3, 2, 2, 9, 0, 3, 3, 0, 5, 1, 1, 3, 9, 4, 7, 4<; TeamScore@16 + NumTeamsD = 84, 4, 3, 7, 7, 0, 6, 2, 0, 7, 2, 0, 4, 2, 6, 9, 3, 0, 0, 2, 1, 4, 7, 4, 3, 1, 2, 1, 4, 3, 5, 0, 5, 4, 2, 3, 4, 5, 3, 3, 2, 1, 7, 2, 0, 2, 3, 6, 4, 4, 4, 2, 9, 4, 10, 2, 2, 6, 3, 1, 6, 0, 4, 5, 1, 3, 1, 1, 4, 0, 4, 1, 2, 2, 0, 12, 0, 4, 1, 0, 1, 5, 6, 3, 7, 0, 2, 7, 2, 4, 1, 2, 11, 5, 6, 2, 1, 1, 6, 3, 5, 2, 2, 4, 3, 4, 5, 3, 0, 6, 0, 2, 1, 3, 3, 1, 8, 4, 3, 3, 2, 1, 8, 0, 5, 0, 4, 7, 6, 2, 0, 0, 4, 3, 8, 5, 0, 3, 2, 2, 3, 2, 3, 5, 5, 0, 1, 1, 4, 2, 5, 4, 4, 3, 7, 6, 2, 6, 4, 2, 1, 3<; TeamScore@17D = 86, 4, 2, 3, 7, 3, 4, 7, 1, 0, 5, 6, 4, 2, 6, 6, 9, 4, 1, 6, 5, 4, 4, 7, 3, 9, 6, 5, 8, 3, 2, 2, 8, 4, 2, 3, 6, 1, 4, 2, 5, 1, 5, 5, 0, 5, 7, 1, 2, 6, 0, 4, 5, 5, 5, 2, 5, 2, 0, 2, 2, 6, 5, 1, 9, 1, 1, 4, 0, 1, 4, 1, 1, 5, 5, 1, 4, 1, 0, 3, 5, 5, 9, 6, 0, 2, 7, 5, 6, 6, 5, 6, 1, 13, 7, 4, 0, 3, 3, 6, 8, 5, 11, 7, 5, 0, 1, 3, 7, 4, 4, 2, 1, 4, 5, 3, 2, 2, 0, 2, 4, 6, 5, 1, 3, 1, 3, 6, 6, 2, 6, 1, 1, 6, 2, 5, 3, 8, 5, 9, 4, 0, 13, 3, 4, 5, 1, 1, 1, 1, 3, 4, 3, 6, 0, 4, 1, 4, 5, 4, 3, 1<; TeamScore@17 + NumTeamsD = 82, 6, 9, 2, 4, 5, 3, 5, 7, 5, 1, 5, 3, 3, 0, 0, 5, 1, 3, 3, 4, 2, 5, 6, 4, 5, 5, 7, 7, 6, 3, 5, 0, 6, 1, 5, 5, 0, 8, 1, 7, 5, 3, 3, 4, 1, 6, 0, 3, 1, 8, 15, 2, 6, 6, 3, 6, 7, 1, 3, 3, 4, 9, 5, 12, 9, 8, 5, 3, 5, 7, 2, 2, 2, 6, 5, 2, 2, 1, 0, 4, 15, 5, 4, 1, 14, 6, 0, 3, 1, 4, 3, 2, 3, 5, 1, 4, 14, 5, 7, 5, 4, 2, 5, 2, 5, 5, 1, 3, 3, 7, 3, 2, 8, 8, 4, 6, 1, 3, 5, 7, 5, 12, 3, 4, 14, 4, 8, 5, 3, 5, 2, 5, 0, 3, 7, 5, 4, 4, 3, 7, 1, 4, 0, 1, 4, 7, 4, 3, 2, 0, 1, 4, 5, 4, 0, 4, 6, 9, 6, 2, 3<; TeamScore@18D = 82, 6, 9, 7, 7, 0, 2, 8, 3, 6, 4, 5, 4, 2, 0, 3, 1, 3, 9, 4, 6, 8, 6, 6, 3, 3, 1, 2, 6, 0, 5, 6, 4, 2, 1, 4, 9, 6, 3, 7, 1, 3, 1, 2, 3, 3, 1, 7, 3, 4, 2, 9, 7, 1, 3, 9, 3, 5, 6, 2, 6, 4, 8, 2, 7, 1, 4, 4, 8, 3, 6, 3, 3, 3, 4, 1, 14, 8, 14, 16, 2, 1, 2, 3, 5, 6, 5, 0, 5, 1, 2, 2, 11, 5, 1, 4, 6, 2, 7, 5, 4, 4, 8, 8, 10, 8, 0, 2, 3, 3, 1, 11, 5, 9, 5, 5, 2, 3, 4, 3, 5, 1, 7, 1, 9, 2, 0, 4, 7, 6, 2, 5, 0, 3, 7, 7, 7, 6, 3, 7, 1, 5, 1, 5, 4, 6, 2, 2, 0, 1, 12, 0, 7, 6, 5, 8, 2, 6, 4, 5, 4, 3<; TeamScore@18 + NumTeamsD = 86, 4, 2, 1, 10, 11, 6, 4, 7, 7, 5, 6, 9, 4, 4, 2, 6, 4, 1, 1, 4, 4, 4, 3, 4, 10, 2, 1, 7, 2, 2, 3, 2, 4, 2, 3, 5, 4, 7, 4, 2, 0, 0, 1, 7, 9, 11, 4, 9, 6, 5, 5, 3, 5, 9, 8, 6, 0, 4, 1, 7, 1, 1, 3, 0, 3, 3, 0, 9, 4, 1, 7, 7, 2, 1, 8, 5, 5, 3, 9, 5, 5, 5, 2, 2, 0, 3, 6, 2, 3, 4, 7, 2, 8, 4, 2, 5, 6, 6, 8, 5, 2, 6, 2, 9, 5, 3, 3, 7, 4, 4, 7, 6, 8, 4, 9, 3, 4, 6, 5, 4, 6, 3, 6, 11, 6, 10, 9, 4, 0, 1, 1, 6, 2, 5, 3, 8, 3, 9, 4, 0, 6, 5, 4, 5, 10, 3, 3, 2, 10, 2, 1, 5, 11, 6, 6, 1, 3, 9, 6, 5, 0<; TeamScore@19D = 80, 6, 2, 2, 4, 5, 6, 4, 7, 7, 2, 0, 4, 8, 5, 8, 3, 0, 2, 6, 2, 4, 3, 4, 3, 1, 5, 2, 1, 4, 3, 3, 5, 0, 7, 7, 5, 5, 0, 8, 4, 0, 0, 17, 3, 1, 3, 6, 4, 2, 1, 4, 4, 10, 2, 6, 0, 0, 9, 4, 2, 1, 3, 2, 2, 2, 8, 10, 7, 8, 4, 4, 6, 2, 1, 9, 0, 2, 3, 5, 0, 2, 3, 4, 2, 5, 3, 5, 9, 2, 1, 2, 1, 5, 8, 5, 6, 2, 7, 6, 1, 2, 5, 2, 5, 3, 3, 5, 9, 4, 3, 5, 7, 3, 3, 2, 3, 4, 3, 6, 1, 3, 8, 0, 5, 4, 0, 2, 1, 3, 3, 4, 9, 1, 2, 3, 8, 3, 7, 3, 4, 4, 3, 8, 3, 3, 2, 10, 0, 1, 4, 4, 3, 7, 6, 4, 4, 3, 6, 2, 3<; TeamScore@19 + NumTeamsD = 82, 3, 11, 3, 7, 3, 2, 8, 3, 4, 3, 4, 3, 4, 1, 6, 5, 5, 7, 3, 4, 6, 6, 3, 0, 2, 2, 0, 4, 7, 7, 2, 2, 8, 6, 3, 6, 6, 1, 4, 2, 3, 1, 5, 8, 2, 11, 7, 6, 1, 2, 5, 5, 2, 1, 1, 4, 2, 4, 5, 1, 3, 7, 1, 1, 0, 6, 0, 4, 4, 2, 7, 5, 1, 0, 5, 3, 1, 4, 11, 1, 1, 5, 3, 10, 4, 2, 4, 10, 3, 2, 0, 11, 2, 9, 2, 7, 3, 2, 7, 3, 11, 7, 5, 8, 0, 2, 3, 3, 6, 6, 3, 15, 2, 1, 4, 4, 2, 11, 4, 2, 1, 4, 5, 4, 1, 2, 4, 8, 4, 6, 5, 2, 3, 5, 7, 7, 6, 2, 7, 7, 3, 9, 2, 2, 2, 0, 1, 3, 4, 3, 3, 0, 5, 1, 7, 1, 0, 4, 3, 1<;** 

**H* NL CENTRAL *L H* Team 20 = Cardinals*L H* Team 21 = Astros*L H* Team 22 = Cubs*L H* Team 23 = Reds*L H* Team 24 = Pirates*L H* Team 25 = Brewers*L TeamScore@20D = 83, 3, 2, 3, 3, 1, 4, 2, 6, 8, 8, 15, 9, 11, 9, 1, 6, 5, 5, 4, 3, 3, 5, 6, 11, 5, 3, 5, 5, 7, 7, 6, 6, 0, 3, 6, 4, 9, 5, 3, 7, 3, 2, 5, 4, 0, 3, 9, 3, 3, 1, 10, 4, 4, 3, 4, 5, 7, 6, 5, 3, 7, 1, 9, 0, 3, 3, 6, 0, 4, 4, 5, 5, 2, 0, 12, 4, 3, 0, 6, 5, 9, 5, 1, 3, 1, 8, 8, 1, 6, 7, 4, 5, 4, 1, 2, 5, 6, 6, 9, 3, 10, 3, 2, 3, 9, 13, 3, 2, 8, 5, 7, 3, 2, 8, 3, 1, 5, 6, 1, 6, 2, 4, 7, 4, 0, 6, 1, 2, 4, 8, 5, 0, 7, 2, 8, 8, 8, 6, 2, 1, 4, 2, 4, 4, 6, 5, 6, 3, 4, 2, 5, 4, 11, 6, 6, 1, 2, 3, 4, 13, 8<;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

55 

_leastsquares.nb_ **5** 

**TeamScore@20 + NumTeamsD = 85, 11, 0, 4, 2, 3, 5, 3, 1, 2, 13, 5, 5, 2, 2, 2, 8, 3, 0, 2, 5, 0, 6, 5, 7, 3, 2, 6, 6, 5, 8, 3, 0, 4, 1, 4, 11, 1, 6, 7, 9, 1, 1, 1, 2, 3, 0, 8, 1, 2, 3, 3, 15, 3, 7, 3, 7, 12, 1, 4, 2, 4, 4, 2, 8, 5, 4, 8, 10, 7, 5, 4, 4, 10, 4, 2, 5, 6, 5, 2, 1, 6, 3, 5, 8, 0, 1, 9, 4, 7, 6, 2, 6, 1, 3, 4, 6, 2, 4, 1, 4, 5, 1, 4, 5, 2, 5, 6, 6, 7, 10, 4, 2, 1, 4, 5, 5, 2, 1, 6, 2, 6, 5, 2, 5, 3, 2, 2, 13, 9, 4, 4, 7, 4, 1, 3, 4, 11, 4, 3, 4, 2, 0, 3, 3, 3, 6, 4, 2, 2, 9, 0, 3, 6, 5, 8, 5, 1, 2, 5, 6, 0<; TeamScore@21D = 84, 4, 3, 2, 4, 3, 3, 5, 7, 4, 11, 5, 1, 2, 5, 6, 6, 4, 1, 7, 9, 1, 6, 5, 7, 0, 2, 5, 10, 2, 4, 3, 1, 4, 1, 3, 4, 4, 7, 4, 2, 1, 1, 2, 5, 5, 3, 4, 4, 2, 6, 3, 2, 12, 7, 3, 7, 1, 3, 2, 4, 4, 2, 4, 3, 1, 8, 0, 3, 4, 7, 7, 0, 3, 4, 5, 1, 2, 10, 3, 2, 7, 5, 4, 1, 3, 1, 8, 0, 3, 1, 4, 0, 6, 5, 2, 7, 3, 2, 1, 4, 5, 1, 4, 5, 0, 2, 4, 4, 1, 5, 1, 5, 3, 9, 9, 3, 5, 0, 1, 0, 3, 6, 4, 6, 7, 4, 5, 6, 6, 3, 1, 1, 4, 7, 8, 2, 2, 2, 0, 1, 4, 4, 3, 9, 2, 5, 5, 0, 3, 1, 3, 3, 4, 0, 9, 11, 2, 3, 5, 6, 0<; TeamScore@21 + NumTeamsD = 85, 9, 7, 8, 12, 2, 4, 7, 1, 5, 2, 9, 0, 4, 3, 8, 1, 3, 9, 14, 6, 4, 5, 6, 11, 5, 1, 0, 4, 3, 10, 2, 6, 5, 6, 7, 3, 6, 3, 7, 3, 3, 5, 4, 2, 7, 2, 3, 5, 1, 7, 11, 4, 7, 3, 1, 4, 3, 6, 7, 7, 1, 9, 11, 6, 4, 3, 1, 7, 5, 3, 0, 1, 8, 5, 3, 5, 7, 14, 7, 3, 0, 7, 10, 2, 5, 5, 2, 5, 6, 6, 5, 4, 4, 7, 5, 6, 2, 4, 5, 5, 10, 3, 2, 3, 4, 6, 5, 3, 5, 4, 8, 7, 7, 1, 11, 6, 8, 1, 6, 7, 4, 5, 3, 0, 5, 6, 9, 8, 7, 1, 2, 2, 3, 4, 2, 0, 8, 8, 4, 3, 1, 5, 4, 3, 8, 1, 2, 1, 4, 2, 2, 2, 6, 2, 6, 2, 4, 19, 4, 13, 8<; TeamScore@22D = 83, 5, 4, 4, 6, 4, 7, 0, 5, 5, 2, 9, 0, 8, 5, 1, 2, 4, 2, 10, 3, 3, 3, 2, 4, 5, 3, 2, 4, 5, 4, 3, 0, 4, 11, 1, 11, 0, 4, 5, 7, 5, 5, 9, 1, 11, 4, 9, 2, 0, 3, 7, 3, 1, 1, 4, 2, 2, 2, 4, 4, 5, 1, 3, 1, 5, 5, 12, 3, 3, 4, 6, 2, 3, 6, 2, 3, 7, 7, 3, 2, 5, 4, 0, 3, 4, 2, 4, 10, 4, 6, 1, 3, 2, 3, 5, 6, 2, 1, 4, 5, 5, 2, 0, 2, 2, 5, 6, 5, 11, 1, 7, 4, 11, 7, 1, 4, 4, 4, 8, 6, 4, 5, 3, 5, 3, 2, 0, 4, 3, 3, 2, 4, 2, 7, 5, 0, 1, 5, 6, 4, 2, 6, 4, 5, 10, 12, 1, 2, 6, 4, 2, 2, 5, 1, 7, 5, 1, 2, 0, 6, 2<; TeamScore@22 + NumTeamsD = 86, 3, 5, 1, 5, 6, 4, 6, 6, 4, 11, 5, 5, 3, 9, 0, 1, 5, 12, 8, 7, 5, 4, 11, 2, 3, 4, 5, 1, 1, 5, 2, 2, 6, 4, 9, 4, 3, 7, 7, 5, 1, 15, 3, 5, 1, 7, 3, 4, 10, 2, 12, 7, 3, 6, 5, 3, 8, 8, 1, 3, 7, 7, 4, 0, 4, 9, 7, 1, 4, 10, 3, 3, 4, 4, 3, 6, 3, 13, 6, 1, 2, 6, 1, 1, 5, 3, 5, 9, 7, 3, 9, 6, 1, 13, 7, 1, 4, 9, 2, 1, 4, 3, 2, 4, 9, 13, 3, 3, 6, 0, 6, 3, 4, 8, 3, 2, 3, 10, 4, 5, 3, 6, 4, 4, 0, 6, 3, 5, 2, 8, 5, 6, 3, 0, 2, 4, 3, 7, 3, 3, 4, 3, 5, 4, 6, 8, 2, 7, 8, 3, 1, 3, 2, 5, 1, 1, 2, 3, 2, 2, 9<; TeamScore@23D = 87, 4, 12, 8, 12, 2, 2, 6, 8, 3, 8, 2, 1, 11, 6, 3, 4, 1, 7, 2, 5, 0, 9, 2, 7, 6, 4, 5, 4, 3, 10, 5, 2, 2, 6, 7, 3, 6, 7, 9, 7, 7, 0, 3, 4, 1, 4, 3, 6, 4, 4, 5, 6, 1, 7, 2, 4, 2, 8, 6, 8, 8, 1, 3, 2, 10, 2, 6, 3, 7, 2, 0, 2, 3, 2, 10, 4, 10, 5, 5, 3, 4, 2, 1, 7, 0, 1, 9, 4, 7, 8, 3, 6, 1, 3, 0, 0, 3, 4, 11, 4, 2, 6, 2, 9, 4, 7, 9, 3, 5, 4, 3, 4, 8, 7, 2, 3, 2, 5, 13, 3, 4, 2, 1, 11, 3, 5, 8, 5, 3, 4, 6, 5, 2, 0, 0, 4, 11, 4, 3, 3, 4, 3, 4, 7, 1, 8, 2, 7, 8, 3, 1, 1, 2, 6, 2, 3, 3, 5, 6, 5, 0<; TeamScore@23 + NumTeamsD = 86, 2, 3, 2, 4, 3, 13, 1, 10, 2, 2, 3, 6, 2, 7, 9, 5, 3, 4, 4, 3, 3, 5, 3, 6, 7, 3, 9, 10, 2, 4, 4, 3, 0, 1, 3, 4, 5, 3, 7, 4, 5, 5, 5, 5, 2, 12, 10, 3, 5, 10, 1, 7, 2, 3, 7, 3, 1, 11, 9, 2, 2, 4, 0, 3, 2, 4, 4, 2, 2, 3, 4, 1, 5, 4, 2, 5, 5, 7, 0, 4, 3, 8, 3, 5, 1, 8, 8, 5, 8, 4, 4, 5, 4, 1, 2, 1, 1, 6, 2, 3, 4, 8, 8, 10, 3, 2, 0, 4, 1, 5, 4, 11, 7, 10, 3, 2, 1, 3, 1, 7, 6, 1, 3, 8, 5, 4, 6, 6, 2, 3, 3, 4, 3, 9, 3, 6, 8, 6, 2, 4, 2, 6, 1, 12, 4, 12, 1, 2, 6, 6, 10, 8, 3, 4, 0, 4, 4, 4, 5, 4, 3<; TeamScore@24D = 86, 3, 5, 4, 2, 3, 1, 4, 4, 5, 0, 1, 6, 2, 7, 9, 0, 0, 5, 7, 3, 4, 2, 2, 2, 3, 1, 8, 4, 5, 7, 2, 6, 5, 4, 3, 0, 2, 2, 6, 2, 5, 5, 10, 6, 0, 0, 2, 4, 10, 2, 3, 5, 9, 8, 2, 6, 3, 8, 3, 0, 1, 3, 0, 3, 1, 7, 5, 1, 1, 2, 3, 9, 5, 3, 6, 2, 7, 1, 6, 1, 5, 3, 10, 5, 5, 2, 7, 3, 9, 4, 4, 7, 2, 1, 1, 4, 1, 4, 3, 3, 1, 5, 3, 4, 5, 3, 6, 0, 6, 5, 2, 3, 5, 0, 9, 2, 0, 1, 6, 5, 2, 8, 5, 4, 1, 9, 4, 2, 4, 4, 7, 4, 4, 2, 0, 4, 3, 7, 3, 3, 1, 5, 4, 0, 1, 6, 4, 2, 6, 2, 1, 1, 0, 5, 5, 4, 4, 4, 9, 4, 3<; TeamScore@24 + NumTeamsD = 83, 5, 4, 3, 3, 1, 7, 3, 6, 6, 6, 4, 1, 11, 6, 3, 6, 6, 9, 2, 6, 2, 3, 0, 5, 0, 4, 4, 3, 6, 4, 3, 1, 4, 1, 10, 2, 5, 8, 9, 4, 0, 3, 1, 2, 2, 2, 4, 2, 0, 3, 7, 1, 3, 9, 1, 3, 7, 5, 2, 2, 8, 2, 7, 1, 0, 3, 4, 5, 5, 5, 8, 3, 4, 1, 4, 4, 6, 2, 2, 2, 3, 4, 2, 3, 1, 8, 4, 6, 1, 0, 6, 5, 0, 0, 3, 6, 9, 3, 1, 4, 2, 2, 10, 7, 6, 5, 11, 1, 7, 15, 13, 7, 0, 6, 2, 7, 1, 2, 2, 4, 7, 11, 3, 5, 8, 2, 11, 0, 8, 5, 0, 7, 7, 8, 2, 6, 1, 5, 6, 1, 4, 4, 13, 3, 4, 5, 6, 3, 2, 7, 6, 15, 1, 3, 8, 3, 3, 5, 8, 6, 7<; TeamScore@25D = 86, 2, 3, 1, 1, 5, 4, 4, 6, 6, 6, 4, 3, 4, 1, 6, 9, 3, 14, 6, 4, 5, 3, 6, 5, 1, 0, 2, 3, 0, 1, 0, 4, 1, 4, 8, 6, 5, 8, 9, 2, 0, 5, 0, 7, 3, 3, 11, 7, 6, 4, 3, 6, 3, 7, 3, 6, 3, 6, 7, 1, 7, 1, 8, 5, 4, 0, 4, 9, 7, 4, 4, 3, 4, 5, 3, 4, 11, 6, 2, 2, 0, 2, 8, 7, 6, 3, 3, 5, 8, 4, 4, 3, 0, 8, 4, 0, 11, 5, 0, 4, 2, 1, 3, 2, 4, 4, 6, 5, 6, 7, 10, 8, 7, 7, 5, 5, 2, 7, 1, 2, 3, 2, 3, 1, 6, 11, 6, 8, 2, 11, 0, 5, 6, 3, 1, 3, 4, 8, 8, 4, 4, 2, 0, 2, 3, 2, 3, 2, 2, 6, 10, 8, 2, 5, 1, 4, 6, 9, 8, 6, 7<; TeamScore@25 + NumTeamsD = 87, 4, 12, 2, 0, 4, 2, 7, 0, 5, 0, 1, 4, 8, 5, 3, 0, 4, 7, 9, 1, 9, 2, 7, 0, 2, 5, 6, 8, 8, 2, 6, 0, 3, 3, 6, 13, 2, 2, 6, 1, 3, 2, 1, 6, 2, 1, 3, 6, 4, 5, 2, 0, 7, 2, 4, 5, 2, 5, 2, 2, 6, 4, 0, 3, 3, 1, 5, 5, 12, 10, 2, 12, 8, 1, 6, 3, 1, 2, 12, 5, 5, 6, 7, 9, 8, 7, 1, 4, 7, 8, 3, 12, 4, 7, 3, 3, 3, 2, 4, 2, 4, 2, 2, 0, 2, 0, 2, 4, 2, 8, 5, 1, 5, 3, 3, 1, 5, 2, 0, 1, 0, 1, 1, 5, 1, 9, 2, 1, 9, 4, 2, 2, 4, 2, 2, 8, 8, 2, 2, 0, 1, 4, 2, 7, 5, 3, 2, 1, 6, 3, 1, 1, 5, 1, 7, 1, 4, 5, 9, 4, 3<;** 

**H* NL WEST *L H* Team 26 = Dodgers*L H* Team 27 = Giants*L H* Team 28 = Padres*L H* Team 29 = Rockies*L H* Team 30 = Diamondbacks*L TeamScore@26D = 82, 4, 0, 7, 0, 5, 4, 4, 2, 6, 4, 3, 5, 2, 2, 2, 4, 1, 6, 5, 12, 8, 7, 4, 2, 5, 3, 2, 0, 5, 1, 1, 3, 2, 4, 1, 10, 2, 4, 0, 1, 1, 3, 5, 1, 6, 2, 3, 3, 5, 1, 3, 1, 8, 7, 8, 0, 1, 11, 9, 1, 6, 0, 7, 5, 11, 10, 4, 2, 2, 3, 0, 1, 4, 6, 5, 3, 1, 3, 15, 4, 0, 5, 1, 1, 2, 0, 3, 6, 1, 1, 4, 6, 2, 1, 0, 3, 1, 2, 7, 3, 8, 3, 1, 9, 4, 3, 6, 1, 0, 7, 5, 3, 3, 1, 8, 1, 6, 7, 0, 1, 1, 5, 8, 6, 3, 2, 13, 9, 6, 7, 6, 4, 8, 4, 6, 8, 2, 3, 2, 7, 7, 2, 3, 1, 2, 4, 3, 2, 7, 6, 15, 2, 5, 8, 2, 0, 6, 4, 6, 7<; TeamScore@26 + NumTeamsD = 81, 3, 10, 5, 3, 7, 2, 0, 7, 1, 5, 4, 9, 11, 9, 1, 2, 10, 1, 3, 2, 10, 3, 5,** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

56 

**6** _leastsquares.nb_ 

**4, 4, 2, 5, 7, 2, 4, 5, 6, 4, 2, 4, 3, 0, 3, 1, 4, 2, 0, 8, 3, 4, 9, 8, 4, 4, 2, 2, 6, 0, 1, 2, 3, 2, 8, 6, 3, 2, 2, 9, 6, 7, 8, 6, 3, 7, 7, 7, 0, 0, 1, 7, 8, 6, 2, 0, 6, 1, 0, 7, 3, 5, 6, 5, 0, 0, 0, 1, 4, 3, 4, 5, 5, 0, 7, 6, 1, 5, 2, 3, 5, 6, 6, 2, 0, 3, 4, 3, 4, 5, 2, 9, 0, 1, 0, 3, 2, 3, 1, 2, 7, 5, 1, 2, 4, 1, 6, 7, 1, 5, 2, 4, 6, 1, 4, 7, 3, 4, 1, 0, 8, 7, 5, 2, 6, 2, 1, 1, 1, 8, 2, 0, 3, 2, 2, 7, 5<; TeamScore@27D = 81, 3, 10, 5, 1, 8, 5, 3, 1, 1, 5, 4, 5, 5, 5, 8, 6, 2, 1, 2, 6, 3, 0, 5, 0, 2, 2, 0, 7, 2, 2, 4, 3, 3, 1, 4, 3, 4, 3, 4, 3, 8, 3, 2, 3, 5, 1, 6, 0, 5, 2, 0, 7, 3, 7, 12, 3, 1, 2, 5, 1, 3, 0, 3, 2, 4, 6, 5, 2, 2, 2, 1, 2, 5, 2, 4, 1, 3, 13, 6, 1, 2, 4, 15, 3, 3, 3, 6, 2, 2, 3, 4, 6, 6, 3, 4, 5, 5, 0, 2, 4, 2, 2, 2, 4, 3, 2, 0, 2, 1, 8, 0, 2, 1, 3, 0, 6, 2, 1, 3, 5, 4, 1, 7, 0, 0, 5, 6, 5, 2, 1, 2, 2, 3, 0, 2, 4, 6, 2, 1, 7, 6, 1, 1, 0, 8, 8, 3, 3, 8, 9, 6, 12, 1, 8, 2, 1, 2, 2, 3, 7, 3<; TeamScore@27 + NumTeamsD = 82, 4, 0, 7, 3, 4, 4, 2, 6, 6, 4, 3, 2, 3, 6, 1, 3, 10, 4, 5, 9, 2, 2, 2, 3, 1, 5, 2, 6, 0, 5, 3, 2, 0, 0, 3, 2, 11, 0, 7, 5, 5, 1, 1, 0, 4, 5, 7, 1, 4, 3, 6, 3, 4, 5, 7, 1, 2, 1, 4, 2, 1, 3, 2, 10, 2, 5, 2, 3, 5, 4, 2, 9, 1, 1, 3, 0, 1, 7, 3, 2, 5, 3, 3, 6, 5, 5, 5, 1, 5, 1, 2, 2, 1, 11, 3, 0, 3, 1, 4, 2, 1, 7, 1, 1, 4, 7, 9, 5, 6, 1, 3, 9, 2, 1, 5, 0, 9, 2, 0, 2, 5, 2, 5, 1, 6, 7, 4, 7, 1, 3, 1, 1, 4, 7, 5, 0, 2, 7, 4, 2, 4, 3, 2, 3, 1, 3, 2, 1, 5, 1, 5, 5, 2, 5, 8, 3, 15, 5, 1, 0, 6<; TeamScore@28D = 85, 11, 0, 3, 4, 2, 0, 7, 2, 2, 3, 0, 4, 3, 8, 0, 1, 5, 0, 0, 2, 1, 5, 2, 0, 2, 5, 7, 3, 6, 4, 4, 0, 4, 3, 6, 13, 7, 9, 8, 8, 1, 2, 1, 1, 0, 1, 1, 2, 3, 1, 2, 5, 3, 5, 3, 4, 3, 6, 7, 0, 2, 3, 7, 1, 1, 0, 3, 3, 3, 5, 0, 4, 5, 5, 5, 11, 1, 4, 4, 4, 4, 0, 1, 1, 5, 5, 5, 1, 0, 0, 1, 2, 1, 11, 3, 4, 14, 5, 1, 6, 3, 5, 1, 3, 4, 2, 6, 8, 2, 0, 3, 15, 13, 7, 8, 4, 9, 3, 3, 1, 7, 4, 6, 3, 3, 4, 14, 4, 7, 1, 0, 1, 1, 1, 5, 2, 0, 4, 7, 2, 4, 3, 1, 2, 5, 7, 3, 2, 1, 2, 3, 1, 8, 2, 4, 0, 3, 2, 2, 2, 9<; TeamScore@28 + NumTeamsD = 83, 3, 2, 1, 8, 4, 4, 2, 3, 8, 2, 1, 2, 5, 6, 1, 2, 4, 3, 2, 4, 3, 3, 8, 7, 3, 2, 0, 4, 5, 7, 3, 6, 3, 4, 8, 6, 12, 7, 2, 4, 6, 5, 0, 4, 4, 6, 3, 3, 1, 2, 1, 4, 2, 4, 4, 7, 1, 3, 2, 3, 0, 5, 3, 2, 2, 2, 1, 6, 6, 6, 1, 5, 14, 4, 1, 2, 10, 1, 3, 2, 1, 6, 0, 3, 3, 3, 6, 2, 1, 1, 4, 6, 6, 3, 4, 0, 3, 3, 3, 8, 5, 4, 6, 4, 3, 3, 10, 3, 6, 1, 0, 5, 2, 3, 9, 5, 5, 2, 5, 13, 3, 5, 1, 7, 1, 3, 1, 3, 5, 2, 5, 3, 6, 4, 8, 4, 3, 5, 2, 7, 6, 1, 4, 3, 6, 6, 8, 3, 3, 0, 1, 5, 2, 1, 0, 2, 0, 6, 0, 6, 2<; TeamScore@29D = 86, 3, 3, 7, 7, 3, 6, 6, 7, 5, 6, 9, 5, 3, 9, 1, 3, 10, 1, 3, 3, 5, 4, 0, 4, 4, 3, 6, 2, 3, 2, 0, 2, 3, 5, 12, 7, 2, 7, 5, 1, 7, 6, 2, 1, 12, 2, 1, 3, 3, 15, 3, 1, 2, 3, 1, 2, 1, 3, 0, 5, 9, 6, 7, 8, 1, 6, 6, 13, 5, 1, 8, 4, 3, 4, 3, 4, 3, 3, 2, 4, 9, 9, 8, 1, 3, 1, 3, 3, 2, 0, 12, 4, 7, 3, 4, 12, 3, 6, 8, 3, 0, 5, 2, 3, 3, 10, 3, 3, 0, 6, 6, 3, 15, 2, 10, 3, 2, 1, 1, 6, 2, 7, 5, 12, 2, 7, 5, 9, 8, 7, 1, 6, 7, 1, 4, 2, 3, 5, 2, 7, 8, 3, 1, 12, 4, 1, 6, 5, 1, 5, 5, 2, 1, 0, 6, 2, 4, 19, 1, 0, 6<; TeamScore@29 + NumTeamsD = 87, 1, 0, 5, 1, 4, 4, 5, 6, 4, 5, 4, 0, 8, 5, 8, 6, 2, 4, 1, 6, 3, 3, 3, 1, 8, 4, 4, 3, 4, 3, 3, 1, 4, 9, 7, 9, 8, 4, 3, 2, 1, 7, 3, 3, 4, 5, 2, 6, 10, 4, 4, 7, 8, 0, 3, 1, 2, 0, 2, 3, 7, 5, 11, 10, 3, 3, 3, 6, 4, 9, 7, 3, 4, 2, 8, 6, 7, 2, 3, 6, 0, 6, 16, 4, 5, 9, 6, 2, 1, 2, 3, 0, 8, 4, 7, 3, 2, 9, 4, 12, 7, 8, 3, 1, 2, 6, 8, 4, 5, 8, 3, 5, 7, 3, 7, 2, 3, 2, 6, 1, 6, 4, 6, 5, 8, 6, 3, 5, 6, 6, 6, 7, 6, 5, 9, 4, 0, 4, 7, 10, 3, 5, 4, 7, 1, 2, 2, 8, 9, 6, 12, 8, 2, 4, 9, 11, 2, 3, 3, 7, 3<; TeamScore@30D = 87, 1, 1, 5, 6, 13, 1, 10, 2, 13, 5, 2, 3, 6, 5, 3, 4, 1, 4, 4, 4, 7, 4, 11, 2, 3, 4, 4, 4, 3, 3, 6, 3, 0, 3, 2, 3, 1, 4, 4, 6, 5, 2, 8, 9, 3, 4, 5, 2, 6, 7, 11, 4, 15, 2, 6, 1, 4, 2, 4, 5, 2, 2, 4, 9, 5, 12, 5, 2, 3, 4, 2, 2, 7, 3, 5, 7, 0, 3, 4, 6, 2, 4, 4, 2, 8, 7, 1, 4, 7, 6, 2, 4, 3, 4, 3, 3, 2, 4, 4, 12, 7, 6, 4, 3, 5, 6, 6, 5, 6, 1, 4, 3, 4, 1, 11, 6, 8, 4, 6, 5, 3, 2, 1, 2, 1, 0, 1, 2, 4, 8, 5, 3, 6, 5, 9, 4, 2, 7, 4, 10, 3, 5, 4, 3, 6, 6, 7, 5, 2, 0, 1, 5, 1, 3, 8, 3, 15, 5, 2, 7, 5<; TeamScore@30 + NumTeamsD = 86, 3, 4, 6, 4, 2, 6, 8, 8, 8, 15, 5, 5, 5, 4, 1, 7, 4, 6, 8, 0, 5, 8, 2, 4, 5, 3, 3, 6, 2, 4, 0, 4, 1, 4, 3, 4, 0, 1, 8, 1, 4, 1, 7, 6, 2, 12, 2, 1, 3, 6, 3, 2, 4, 5, 5, 6, 0, 0, 9, 8, 3, 0, 6, 5, 1, 9, 6, 5, 2, 1, 6, 8, 2, 2, 3, 6, 6, 8, 5, 4, 6, 5, 2, 7, 6, 3, 3, 1, 6, 7, 4, 6, 2, 1, 0, 11, 5, 0, 8, 3, 0, 1, 3, 4, 9, 4, 3, 2, 1, 8, 7, 5, 3, 9, 9, 3, 5, 3, 4, 3, 2, 9, 4, 4, 8, 1, 4, 0, 2, 1, 0, 1, 1, 1, 4, 2, 6, 2, 1, 7, 8, 3, 1, 2, 5, 7, 2, 4, 3, 2, 3, 1, 0, 5, 5, 1, 2, 2, 4, 6, 7<;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

57 

_leastsquares.nb_ **7** 

**H* this is a very important function. it has two inputs, the bins used to analyze the team data and find the best fit parameters, and the bins used for the chisquare test on the indep of rs and ra. *L H* these are stored in Bins and ChiIndepBins. the program below computes the lengths and other relevent quantities which are used by programs later. To make sure there is at least SOME choice of bins,*L BinCreate@binlist_, chibinlist_D := Module@8<, Bins = binlist; ChiIndepBins = chibinlist; NumBins = Length@BinsD - 1; NumBinsChiTests = Length@ChiIndepBinsD - 1; FirstBin = Bins@@1DD; FinalBin = Last@BinsD; MaxBinValue = Last@BinsD; Print@"Set of Bins is = ", Bins, " and number of bins = ", NumBinsD; Print@"Set of Bins for Independence tests of rs and ra is ", ChiIndepBins, " and the number of bins = ", NumBinsChiTestsD; Print@" "D; H* these lines assign to each integer what bin it is in *L H* we store that in xtoBins *L For@k = 0, k § 40, k ++, 8 For@m = 1, m § NumBins, m ++, 8 If@k ¥ Bins@@mDD && k < Bins@@m + 1DD, xtoBins@kD = mD; <D; <D; D; H* end of module *L H* We now 'bin' the TeamScore data. It is important that we know there are NumGames = 162 in a season. In fact, we put an error check on that below. The program above bins the data and saves to ObsTeamScore. We go from i=1 to i=NumTeams. We initialize a temporary array to be zero, and then for each game we see which bin the score falls into. this is easily done using the Ceiling function. we increment the temp counter by one. after finishiing this loop we initialize ObsTeamScore to be zero and then save the temp array here. As some of the older code uses NumObs, we set that to be NumGames. *L H* in the code below I changed the formula inside to 1 + Hteamscore - 1stbinL ê binsize; the reason is a team could score zero and this would then be stored in the zeroth entry of our list, which would be bad. *L BinTeamData@binlist_, chibinlist_D := Module@8<, BinCreate@binlist, chibinlistD; H*Loop over double num teams for rs and ra*L For@i = 1, i § DoubleNumTeams, i ++, 8 Clear@TempBinD; NumObs = Length@TeamScore@iDD; For@j = 0, j § NumBins + 2, j ++, TempBin@jD = 0D; For@j = 1, j § NumObs, j ++, 8 For@k = 1, k § NumBins, k ++, If@TeamScore@iD@@jDD ¥ Bins@@kDD && TeamScore@iD@@jDD < Bins@@k + 1DD, TempBin@kD ++DD; H*If it lies in bin k*L < D; ObsTeamScore@iD = 8<; For@k = 1, k § NumBins + 1, k ++, ObsTeamScore@iD = Append@ObsTeamScore@iD, TempBin@kDDD; If@Sum@ObsTeamScore@iD@@kDD, 8k, 1, NumBins<D ¹≠ NumObs, Print@"Error - do not have enough games! Trouble with team ", i, "; only have ", Sum@ObsTeamScore@iD@@kDD, 8k, 1, NumBins<D, " games."DD; H*Error message if not enough games*L <D; D;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

58 

**8** _leastsquares.nb_ 

**H* This gives area in Bin k. note it is a function of the parameters a1,** 

**a2,b1,b2,c,d and we need to know the two endpoints, as we need the starting point of the bin and the ending point. *L AWBin@k_, a1_, a2_, b1_, b2_, c_, d_D := AW@Bins@@kDD, Bins@@k + 1DD, a1, a2, b1, b2, c, dD; H*We must multiply area by NumGames. The integral over everything gives 1, but we observe NumGames things. As the sum Pred equals the sum of the Obs, we must mult each area by NumGames *L Pred@team_, k_, a1_, a2_, b1_, b2_, c_, d_D := Length@TeamScore@teamDD * AWBin@k, a1, a2, b1, b2, c, dD ; ChiPred@team_, sp_, ep_, a1_, a2_, b1_, b2_, c_, d_D := Length@TeamScore@teamDD * AW@sp, ep, a1, a2, b1, b2, c, dD ; H* This is the difference bêw Obs and Pred in bin k for team team_. *L ObsPred@team_, k_, a1_, a2_, b1_, b2_, c_, d_D := HObsTeamScore@teamD@@kDD - Pred@team, k, a1, a2, b1, b2, c, dDL ^2 ; ChiObsPred@team_, sp_, ep_, a1_, a2_, b1_, b2_, c_, d_D := HH Sum@If@TeamScore@teamD@@jDD ¥ sp && TeamScore@teamD@@jDD < ep, 1, 0D, 8j, 1, Length@TeamScore@teamDD< D - ChiPred@team, sp, ep, a1, a2, b1, b2, c, dDL ^ 2 L ê ChiPred@team, sp, ep, a1, a2, b1, b2, c, dD; H* This is the total error, again for just ONE team." *L Error@team_, a1_, a2_, b1_, b2_, c_, d_D := Sum@ObsPred@team, k, a1, a2, b1, b2, c, dD, 8k, 1, NumBins<D H* this is the predicted mean score from a weibull with params a1,a2,b,c,d *L MeanScore@a1_, a2_, b1_, b2_, c_, d_D := d * Hb1 + a1 * Gamma@1 + H1 ê cLDL + H1 - dL * Hb2 + a2 * Gamma@1 + H1 ê cLDL H* this calculates the mean of a team's scores *L MeanOfTeam@i_D := 1.0 * Sum@TeamScore@iD@@jDD, 8j, 1, Length@TeamScore@iDD<D ê Length@TeamScore@iDD; H* predict number of wins*L PredWonLoss@a1rs_, a2rs_, a1ra_, a2ra_, b1rs_, b2rs_, b1ra_, b2ra_, c_, d_, f_D := 8Hd * fL * Ha1rs^c êHa1rs^c + a1ra^cLL + HdL * H1 - fL * Ha1rs^c êHa1rs^c + a2ra^cLL + HfL * H1 - dL * Ha2rs^c êHa2rs^c + a1ra^cLL + HH1 - dL * H1 - fLL * Ha2rs^c êHa2rs^c + a2ra^cLL, HMeanScore@a1rs, a2rs, b1rs, b2rs, c, dD - Hd * b1rs + H1 - dL * b2rsLL, HMeanScore@a1ra, a2ra, b1ra, b2ra, c, dD - Hf * b1ra + H1 - fL * b2raLL< H*Won Loss shift for different bins*L PredWonLossShift@a1rs_, a2rs_, a1ra_, a2ra_, b1rs_, b2rs_, b1ra_, b2ra_, b2_, c_, d_, f_D := 8Hd * fL * Ha1rs^c êHa1rs^c + a1ra^cLL + HdL * H1 - fL * Ha1rs^c êHa1rs^c + a2ra^cLL + HfL * H1 - dL * Ha2rs^c êHa2rs^c + a1ra^cLL + HH1 - dL * H1 - fLL * Ha2rs^c êHa2rs^c + a2ra^cLL, HMeanScore@a1rs, a2rs, b1rs, b2rs, c, dD - Hd * b1rs + H1 - dL * b2rsL + b2L, HMeanScore@a1ra, a2ra, b1ra, b2ra, c, dD - Hf * b1ra + H1 - fL * b2raL + b2L< H*Won Loss percentage*L ObservedWonLossPercentage@i_D := Sum@ If@TeamScore@iD@@jDD > TeamScore@i + NumTeamsD@@jDD, 1, 0D, 8j, 1, Length@TeamScore@iDD<D ê H1.0 * Length@TeamScore@iDDL;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

59 

_leastsquares.nb_ **9** 

- **H*we will save data about the teams from our curve fitting here. 1L a_RS1... 2L a_RS2... 3L a_RA1... 4La_RA2... 5L b_RS1... 6Lb_RS2 7L b_RA1 8L b_RA2 9L c... 10L d** 

- **11L error from least squares 12L error from chisquare RS 13L error from chisquare RA 14L observed number of wins 15L observed number of losses 16L predicted number of wins 17L predicted number of losses 18L observed won-loss percentage 19L predicted won-loss percentage 20L number of games off by 21L error from independence tests *L For@i = 1, i § NumTeams, i ++, For@k = 1, k § 21, k ++, TeamBestFits@i, kD = 0DD;** 

- **For@i = 1, i § NumTeams, i ++, 8 H*Observed number of wins*L TeamBestFits@i, 15D = Sum@If@TeamScore@iD@@jDD > TeamScore@i + NumTeamsD@@jDD, 1, 0D, 8j, 1, Length@TeamScore@iDD<D;** 

- **H*Observed number of losses*L TeamBestFits@i, 16D = Sum@If@TeamScore@iD@@jDD > TeamScore@i + NumTeamsD@@jDD, 0, 1D, 8j, 1, Length@TeamScore@iDD<D;** 

- **H*Observed won-loss percentage*L TeamBestFits@i, 19D = ObservedWonLossPercentage@iD;** 

- **<D;** 

**H* THIS IS THE KEY PART OF THE CODE. IT FINDS THE BEST VALUES FOR THE PARAMETERS TO MINIMIZE THE SUM OF SQUARES OF ERRORS. WE ASSUME RS AND RA COME FROM TWO INDEPENDNET WEIBULLS WITH PARAMS Ha1rs,a2rs,b1rs,b2rs,c,dL AND Ha1ra,a2ra,b1ra,b2ra,c,dL; *L H* the input is which team we want to study *L H* if printchoice = 1 it prints out results, else does not print *L BestWeibullParameters@i_, printchoice_, list_D := Module@ 8a1rs, a2rs, a1ra, a2ra, b1rs, b2rs, b1ra, b2ra, c, d, f<, H* i represents the team *L Clear@a1rsD; Clear@a2rsD; Clear@a1raD; Clear@a2raD; Clear@b1rsD; Clear@b2rsD; Clear@b1raD; Clear@b2raD; Clear@cD; Clear@dD; Clear@fD; b1rs = -.5; b2rs = -.5; b1ra = -.5; b2ra = -.5; temp3 = NMinimize@ 8Error@i, a1rs, a2rs, b1rs, b2rs, c, dD + Error@i + NumTeams, a1ra, a2ra, b1ra, b2ra, c, fD, a1rs > 0, a2rs > 0, a1ra > 0, a2ra > 0, c > 0, d ¥ 0, f ¥ 0<, 8a1rs, a2rs, a1ra, a2ra, c, f<, MaxIterations Ø MaxNumItersD; TeamBestFits@i, 1D = Last@temp3@@2, 1DDD; TeamBestFits@i, 2D = Last@temp3@@2, 2DDD; TeamBestFits@i, 3D = Last@temp3@@2, 3DDD; TeamBestFits@i, 4D = Last@temp3@@2, 4DDD; TeamBestFits@i, 5D = b1rs; TeamBestFits@i, 6D = b2rs; TeamBestFits@i, 7D = b1ra; TeamBestFits@i, 8D = b2ra; TeamBestFits@i, 9D = Last@temp3@@2, 5DDD; TeamBestFits@i, 10D = Last@temp3@@2, 6DDD ; TeamBestFits@i, 11D = Last@temp3@@2, 7DDD ; H*First@temp3D*L D** 

**H*Chi Square Test of the Weibull parameters *L ChiSquareTestWeibullParams@i_, a1_, a2_, b1_, b2_, c_, d_, chierrorlist_D := Sum@ChiObsPred@i, chierrorlist@@kDD, chierrorlist@@k + 1DD, a1, a2, b1, b2, c, dD, 8k, 1, Length@chierrorlistD - 1<D;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

60 

**10** _leastsquares.nb_ 

**H*chi sq test for independence of rs and ra*L H* we have a grid NumBins by NumBins,say an r x c table. the predicted value of entry E_8r,c< is HSum of row rL*HSum of colmn ccL ê SampleSize. Then we look at sum_8r,cc< HObs - ExpL^2 ê Exp. *L H* RS is the rows, RA is the columns *L ChiSquareTestIndepRSRA@i_, chierrorlist_D := Module@8chinumgames, numloop, rowO, colO<, H*Initialize everything as 0*L For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, 8 Obs@k1, k2D = 0; Expect@k1, k2D = 0; < DD; chinumgames = 0; For@j = 1, j § Length@TeamScore@iDD, j ++, 8 k1 = 0; k2 = 0; For@z = 1, z § Length@chierrorlistD - 1, z ++, 8 If@TeamScore@iD@@jDD ¥ chierrorlist@@zDD, k1 = zD; H*Runs scored*L If@TeamScore@i + NumTeamsD@@jDD ¥ chierrorlist@@zDD, k2 = zD; H*Runs allowed*L < D; Obs@k1, k2D ++; chinumgames ++; < D; H*Error messsage to make sure each row and column has observations*L For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, If@Sum@ Obs@k1, ccD, 8cc, 1, Length@chierrorlistD - 1<D ã 0, Print@"Danger: row ", k1, " has 0 observations."DD;D; For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, If@Sum@ Obs@r, k2D, 8r, 1, Length@chierrorlistD - 1<D ã 0, Print@"Danger: column ", k2, " has 0 observations."DD;D; H* NEW EXPECTED VALUE ASSIGNMENTS *L For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, Expect@k1, k2D = 1; D; D; For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, 8 Expect@k1, k1D = 0; rowO@k1D = Sum@ Obs@k1, k2D, 8k2, 1, Length@chierrorlistD - 1<D; colO@k1D = Sum@ Obs@k2, k1D, 8k2, 1, Length@chierrorlistD - 1<D; <D; H* DIAG ENTRIES 0 *L For@numloop = 2, numloop § 100, numloop ++, 8 For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, 8 If@Mod@numloop, 2D ã 0, TempExpect@k1, k2D = N@Expect@k1, k2D * rowO@k1D ê Sum@ Expect@k1, ccD, 8cc, 1, Length@chierrorlistD - 1<DD , TempExpect@k1, k2D = N@Expect@k1, k2D * colO@k2D ê Sum@ Expect@cc, k2D, 8cc, 1, Length@chierrorlistD - 1<DD; D; <D;D; For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, Expect@k1, k2D = TempExpect@k1, k2DD;D; <D; H* END NUMLOOP *L For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++, 8 TempExpect@k1, k2D = 0; <D; D; For@k1 = 1, k1 § Length@chierrorlistD - 1, k1 ++, For@k2 = 1, k2 § Length@chierrorlistD - 1, k2 ++,** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

61 

_leastsquares.nb_ **11** 

**TempExpect@k1, k1D = 1; D; D; H*chi sq for independence of rs and ra*L TeamBestFits@i, 22D = N@Sum@ HObs@k1, k2D - Expect@k1, k2DL ^2 ê HExpect@k1, k2D + TempExpect@k1, k2DL, 8k2, 1, Length@chierrorlistD - 1<, 8k1, 1, Length@chierrorlistD - 1<DD;** 

**D;** 

**H*end chi sq for independence of rs and ra*L** 

**H*Finds Weibull parameters using max likelihood method*L MaxLIikelihoodWeibullParams@i_, chierrorlist_D := NMaximize@ 8Sum@ ObsTeamScore@iD@@kDD Log@ AW@chierrorlist@@kDD, chierrorlist@@k + 1DD, ars1, ars2, -.5, -.5, c, dDD , 8k, 1, Length@chierrorlistD - 1<D + Sum@ ObsTeamScore@i + NumTeamsD@@kDD Log@ AW@chierrorlist@@kDD, chierrorlist@@k + 1DD, ara1, ara2, -.5, -.5, c, fDD, 8k, 1, Length@chierrorlistD - 1<D, ars1 > 2, ars2 > 2, ara1 > 2, ara2 > 2, ars1 > ars2, ara1 > ara2, c > 1, c < 4, d ¥ 0, d § 1, f ¥ 0, f § 1<, 8ars1, ars2 , ara1, ara2, c, d, f<D; H* used to be c < 15 made c < 5 as issues compiling *L Clear@LeastSqsD; For@i = 1, i § 21, i ++, For@j = 1, j § 8, j ++, LeastSqs@i, jD = 0DD; chilistRSRA = 8-.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, Infinity<; BinTeamData@chilistRSRA, 8-.5, .5, 1.5, 2.5, 3.5, 4.5, Infinity<D; For@ii = 1, ii § NumTeams, ii ++, 8 temptemp = MaxLIikelihoodWeibullParams@ii, chilistRSRAD; H*Print@temptempD;, maybe a problem here... switch rs and ra*L tars1 = Last@temptemp@@2, 1DDD; tars2 = Last@ temptemp@@2, 2DDD; tara1 = Last@temptemp@@2, 3DDD; tara2 = Last@temptemp@@2, 4DDD; tc = Last@temptemp@@2, 5DDD; td = Last@temptemp@@2, 6DDD; tf = Last@temptemp@@2, 7DDD; LeastSqs@ii, 1D = tars1; LeastSqs@ii, 2D = tars2; LeastSqs@ii, 3D = tara1; LeastSqs@ii, 4D = tara2; LeastSqs@ii, 5D = tc; LeastSqs@ii, 6D = td; LeastSqs@ii, 7D = tf; LeastSqs@ii, 8D = ChiSquareTestWeibullParams@ii, tars1, tars2, -.5, -.5, tc, td, chilistRSRAD + ChiSquareTestWeibullParams@ii + NumTeams, tara1, tara2, -.5, -.5, tc, tf, chilistRSRAD ; Print@"Team = ", TeamNames@@iiDD D; Print@"Pred Ave RS = ", td * Htars1 * Gamma@1 + H1.0 ê tc LD - .5L + H1 - tdL * Htars2 * Gamma@1 + H1.0 ê tc LD - .5L, "; Pred Ave RA = ", tf * Htara1 * Gamma@1 + H1.0 ê tc LD - .5L + H1 - tfL * Htara2 * Gamma@1 + H1.0 ê tc LD - .5L, "; Pred c = ", tc , "; Pred d = ", td, ";Pred f = ", tf, "; Pred RS_1 = " , tars1, "; Pred RS_2 = " , tars2, "; Pred RA_1 = " , tara1, "; Pred RA_2 = " , tara2D; Print@"Total ChiSq for RSRA = ", LeastSqs@ii, 8D, " with ", 2 * HLength@chilistRSRAD - 1L - 1 - 3, " deg freedom."D; <D;** 

**Off@NMaximize::cvmitD** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

62 

**12** _leastsquares.nb_ 

**H*finding least squared won loss for team*L LeastSqsWonLossPercentageForATeam@i_D := Module@8a1rs, a2rs, a1ra, a2ra, b1rs, b2rs, b1ra, b2ra, c, d, f<, H* we are studing team i *L Print@"Analysis for team = ", i, ", the ", TeamNames@@iDDD; BestWeibullParameters@i, 1D; H* find the best fit params, print out answers *L a1rs = LeastSqs@i, 1D; a2rs = LeastSqs@i, 2D; a1ra = LeastSqs@i, 3D; a2ra = LeastSqs@i, 4D; b1rs = -.5; b2rs = -.5; b1ra = -.5; b2ra = -.5; c = LeastSqs@i, 5D; d = LeastSqs@i, 6D; f = LeastSqs@i, 7D;** 

**TeamBestFits@i, 20D = First@PredWonLoss@a1rs, a2rs, a1ra, a2ra, b1rs, b2rs, b1ra, b2ra, c, d, fDD; TeamBestFits@i, 21D = HObservedWonLossPercentage@iD - First@PredWonLoss@a1rs, a2rs, a1ra, a2ra, b1rs, b2rs, b1ra, b2ra, c, d, fDDL * Length@TeamScore@iDD; TeamBestFits@i, 17D = TeamBestFits@i, 20D * Length@TeamScore@iDD; TeamBestFits@i, 18D = H1 - TeamBestFits@i, 20DL * Length@TeamScore@iDD;** 

**Print@"RS: Predicted = ", MeanScore@a1rs, a2rs, b1rs, b2rs, c, dD, " Actual = ", MeanOfTeam@iDD; Print@"RA: Predicted = ", MeanScore@a1ra, a2ra, b1ra, b2ra, c, fD, " Actual = ", MeanOfTeam@i + NumTeamsDD; Print@"Wins: Observed = ", TeamBestFits@i, 15D, "; Predicted = ", TeamBestFits@i, 17DD; Print@"Losses: Observed = ", TeamBestFits@i, 16D, "; Predicted = ", TeamBestFits@i, 18DD; Print@"Observed Won-Loss Percentage = ", TeamBestFits@i, 19D D; Print@"Predicted Won-Loss Percentage = ", TeamBestFits@i, 20DD; Print@"Uncorrected Pred Won-Loss Percentage = ", First@PredWonLossShift@a1rs, a2rs, a1ra, a2ra, b1rs, b2rs, b1ra, b2ra, .5, c, d, fDD , "; this is without subtracting 1ê2."D Print@"Number of Games off by is about ", TeamBestFits@i, 21DD;** 

**Print@"Error Analysis: ChiSquare for RS + RA = ", LeastSqs@i, 8D, "; deg freedom = ", 2 * HLength@chilistRSRAD - 1L - 1 - 3D; H*FIXING INDETERMINATE CASES*L H*pirates really messed up*L chilistIndep = 80, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, Infinity<; If@i ã 17, chilistIndep = 80, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, Infinity<D; If@i ã 24, chilistIndep = 80, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Infinity<D; If@i ã 28, chilistIndep = 80, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, Infinity<D; If@i ã 30, chilistIndep = 80, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, Infinity<D; H* chilistIndep = 80,1,2,3,4,5,6,7,8,9,10,11,12,Infinity<; *L ChiSquareTestIndepRSRA@i, chilistIndepD; Print@"Error Analysis: ChiSquare for Independence of RS and RA = ", TeamBestFits@i, 22D, "; deg freedom = ", HLength@chilistIndepD - 1 - 1L ^2 - HLength@chilistIndepD - 1LD; H* MUST SUBTRACT Length@chierrorlistD-1 AS CANNOT HAVE RS = RA IN A GAME -- STRUCTURAL ZEROS *L Print@" "D; D;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

63 

_leastsquares.nb_ **13** 

**H*Printing out analysis of the teams*L For@i = 1, i § NumTeams, i ++, LeastSqsWonLossPercentageForATeam@iDD cData = 8<; dData = 8<; gamesoffDataUnsigned = 8<; gamesoffDataSigned = 8<; For@i = 1, i § NumTeams, i ++, 8** 

**cData = Append@cData, LeastSqs@i, 5DD; dData = Append@dData, LeastSqs@i, 6DD; fData = Append@dData, LeastSqs@i, 7DD; gamesoffDataUnsigned = Append@gamesoffDataUnsigned, Abs@TeamBestFits@i, 21DDD; gamesoffDataSigned = Append@gamesoffDataSigned, TeamBestFits@i, 21DD;** 

**<D; Print@"Median c = ", Median@cDataD, "; Mean c = ", Mean@cDataD, "; StDevHMean of cL = ", StandardDeviation@cDataDD; Print@"Median d = ", Median@dDataD, "; Mean d = ", Mean@dDataD, "; StDevHMean of dL = ", StandardDeviation@dDataDD; Print@"Median f = ", Median@fDataD, "; Mean f = ", Mean@fDataD, "; StDevHMean of fL = ", StandardDeviation@fDataDD; Print@"UNSIGNED: Median Ò games off = ", Median@gamesoffDataUnsignedDD; Print@"UNSIGNED: Mean Ò games off = ", Mean@gamesoffDataUnsignedDD; Print@"UNSIGNED: StDevHMean Ò games offL = ", StandardDeviation@gamesoffDataUnsignedDD; Print@"SIGNED: Median Ò games off = ", Median@gamesoffDataSignedDD; Print@"SIGNED: Mean Ò games off = ", Mean@gamesoffDataSignedDD;** 

**Print@"SIGNED: StDevHMean Ò games offL = ", StandardDeviation@gamesoffDataSignedDD;** 

**SimOutput =** 

**88StyleForm@Team, "Subsection"D, StyleForm@Obs Wins, "Subsection"D, StyleForm@Pred Wins, "Subsection"D, StyleForm@ObsPerc, "Subsection"D, StyleForm@PredPerc, "Subsection"D, StyleForm@GamesDiff, "Subsection"D, StyleForm@" g ", "Subsection"D<<;** 

**For@i = 1, i § NumTeams, i ++,** 

**SimOutput = Append@SimOutput, 8TeamNames@@iDD, TeamBestFits@i, 15D,** 

**SetAccuracy@TeamBestFits@i, 17D, 2D, SetAccuracy@TeamBestFits@i, 19D, 4D, SetAccuracy@TeamBestFits@i, 20D, 4D, If@Abs@TeamBestFits@i, 21DD > .1,** 

**SetAccuracy@TeamBestFits@i, 21D, 3D, SetAccuracy@0.0, 0DD, SetAccuracy@cData@@iDD, 3D<D;D; PaddedForm@TableForm@SimOutput, TableAlignments Ø 8Left, Center, Center, Center, Center, Right<D, 4D** 

**SimErrOutput = 88StyleForm@Team, "Subsection"D,** 

**StyleForm@"RS+RA c2: 16 d.f.", "Subsection"D, StyleForm@"Indep c2: 109 d.f", "Subsection"D<<; For@i = 1, i § NumTeams, i ++,** 

**SimErrOutput = Append@SimErrOutput, 8TeamNames@@iDD, SetAccuracy@LeastSqs@i, 8D, 3D, SetAccuracy@TeamBestFits@i, 22D, 3D<D;D;** 

**PaddedForm@TableForm@SimErrOutput, TableAlignments Ø 8Left, Center, Center, Right<D, 8D** 

#### **SimOutput =** 

**88StyleForm@Team, "Subsection"D, StyleForm@"Obs RS", "Subsection"D, StyleForm@"Pred RS", "Subsection"D, StyleForm@"z-stat", "Subsection"D, StyleForm@"Obs RA", "Subsection"D, StyleForm@"Pred RA", "Subsection"D, StyleForm@"z-stat", "Subsection"D<<;** 

**H*MeanScore@a1_,a2_,b1_,b2_,c_,d_D *L** 

**For@i = 1, i § NumTeams, i ++, SimOutput = Append@SimOutput, 8TeamNames@@iDD, SetAccuracy@MeanOfTeam@iD, 3D, SetAccuracy@MeanScore@LeastSqs@i, 1D, LeastSqs@i, 2D, -.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 6DD, 3D, SetAccuracy@HMeanOfTeam@iD - MeanScore@LeastSqs@i, 1D, LeastSqs@i, 2D, -.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 6DDL ê HStandardDeviation@TeamScore@iDD ê Sqrt@Length@TeamScore@iDDDL, 3D, SetAccuracy@MeanOfTeam@i + NumTeamsD, 3D, SetAccuracy@MeanScore@LeastSqs@i, 3D, LeastSqs@i, 4D, -.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 7DD, 3D, SetAccuracy@HMeanOfTeam@i + NumTeamsD - MeanScore@LeastSqs@i, 3D, LeastSqs@i, 4D, -.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 7DDL ê HStandardDeviation@TeamScore@i + NumTeamsDD ê Sqrt@Length@TeamScore@iDDDL, 3D<DD; PaddedForm@TableForm@SimOutput, TableAlignments Ø 8Left, Center, Center, Center, Center, Center<D, 4D** 

**H*Gets rid of Nminimize error messages*L H*MIGHT NEED TO GET RID OF THIS LINE LATER*L Off@NMinimize::cvmitD** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

64 

**14** _leastsquares.nb_ 

**H* WARNING: when we run this, we change the bins *L BinCreate@8-.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, Infinity<, 8-.5, .5, 1.5, 2.5, 3.5, 4.5, Infinity<D BinTeamData@8-.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, Infinity<, 8-.5, .5, 1.5, 2.5, 3.5, 4.5, Infinity<D Bins chilistRSRA NumBins = Length@BinsD - 1 ObsTeamScore@1D ObsTeamScore@1D@@xtoBins@Floor@14.5DDDD ObsStepFn@i_, x_, ra_D := If@x < Bins@@1DD, 0, If@x > Bins@@NumBins + 1DD, 0, ObsTeamScore@i + ra * NumTeamsD@@xtoBins@Floor@x + .5DDDDDD** 

**Bins For@i = 1, i § NumTeams, i ++, 8** 

**NumObs = Length@TeamScore@iDD; Print@"Team = ", i, ": Plots of RS Hpredicted vs observedL for ", TeamNames@@iDDD; Print@Plot@8ObsStepFn@i, x, 0D, NumObs * W@x, LeastSqs@i, 1D, LeastSqs@i, 2D, -.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 6DD<, 8x, -.5, 20<DD; Print@"Team = ", i, ": Plots of RA Hpredicted vs observedL for ", TeamNames@@iDDD; Print@Plot@8ObsStepFn@i, x, 1D, NumObs * W@x, LeastSqs@i, 3D, LeastSqs@i, 4D,** 

**-.5, -.5, LeastSqs@i, 5D, LeastSqs@i, 6DD<, 8x, -.5, 20<DD; Print@" "D;** 

**<D;** 

<mark>Printed by Wolfram Mathematica Student Edition</mark> 

65 

### REFERENCES 

- [MCGLP] - Steven J. Miller, Taylor Corcoran, Jennifer Gossels, Victor Luo, and Jaclyn Porfilio. “Pythagoras at the Bat”. Social Networks and the Economics of Sports (organized by Victor Zamaraev). To be published by Springer-Verlag. 2014. 

- [MIL] - Steven J. Miller. “A Derivation of the Pythagorean Won-Loss Formula in Baseball”. Chance Magazine. 2007. 

- [MUR] - G. Muraleedharan. “Characteristic and Moment Generating Functions of Three Parameter Weibull Distribution-an Independent Approach”. Research Journal of Mathematical and Statistical Sciences, Vol. 1(8), 25-27, September 2013. 

66 


