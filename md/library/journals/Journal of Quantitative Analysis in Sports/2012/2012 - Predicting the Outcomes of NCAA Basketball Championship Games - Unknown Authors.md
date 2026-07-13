<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Predicting the Outcomes of NCAA Basketball Championship Games - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1373 

## Predicting the Outcomes of NCAA Basketball Championship Games 

**Herman O. Stekler,** _George Washington University_ **Andrew Klein,** _George Washington University_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1373 

## Predicting the Outcomes of NCAA Basketball Championship Games 

Herman O. Stekler and Andrew Klein 

### **Abstract** 

This paper uses the difference in seeding ranks to predict the outcome of March Madness games. It updates the Boulier-Stekler method by predicting the outcomes by rounds. We also use the consensus rankings obtained from individuals, systems and poll. We conclude that the consensus rankings were slightly better predictors in the early rounds but had the same limitations as the seedings in the later rounds. 

**KEYWORDS:** sports forecasts, March Madness, ranking methods, expert forecasts, consensus forecasts 

Stekler and Klein: NCAA Championship Games 

Every year college basketball fans participate in March Madness. They enter office pools or bet on the outcome of the 63 games that constitute the National Collegiate Athletic Association’s (NCAA) basketball championship tournament.  One web site indicated that billions of dollars are bet on the outcomes of games during this tournament. Moreover, Google Scholar found over 18,000 references to the term “March Madness Betting”. Not all of these references are relevant to economics, but at least some include optimal betting strategies, e.g. Metrick, 1995; Kaplan and Garstka, 2001; Clair and Letscher, (2007). So it is no surprise that there has been interest in methods for forecasting the outcomes of these games. 

A variety of statistical methods have been used to forecast which team should win each game. Although there are many other approaches, one forecasting procedure is to use rankings based on the seeds of the teams as determined by the NCAA committee and to always select the team that has the better seeding. Boulier and Stekler (1999) showed that between 1985 and 1995 the higher-ranked men’s basketball team beat lower-ranked opponents 73.5% of the time. There are three reasons to explore this approach further. 

First, as we explain below, this method has limitations. Given the nature of the NCAA tournament (which will be explained below), this methodology can only be used to predict the outcomes of the first four (of six) rounds of the tournament. It can not be used in forecasting winners among the Final Four teams. Second, this method may be successful in some rounds of the tournament but not in others. Thus we explore the forecasting accuracy of this method by the rounds of the tournament. Finally, an entirely new data set that yields a different set of rankings is available to make forecasts about the outcomes of these games. These data are obtained from an average of the teams’ rankings obtained from 29-45 (depending upon the year) individuals, systems, and polls. Predictions that could be obtained from these data have never previously been analyzed. Moreover, this approach can be applied to all six rounds of the tournament.  In addition to being available for all six rounds, these consensus rankings may have a valuable forecasting characteristic. The macroeconomic forecasting literature has shown that the mean of a set of predictions is usually more accurate than any one given estimate. Thus, the difference in the consensus rankings may be more accurate than the difference in seeds, which is the ranking established by the NCAA committee. 

This paper updates the procedures of Boulier and Stekler to the period 2003-2010, including an analysis of the results by round, and determines whether the consensus rankings contain any information that is not already embodied in the seedings. The next section describes the structure of the NCAA tournament and is followed by a data and methodology section. This is followed by a discussion of the results and conclusions. 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

### 1. THE STRUCTURE OF THE NCAA TOURNAMENT 

Since 1985 the actual NCAA tournament has consisted of 64 teams, but until 2011 a 65<sup>th</sup> team was selected and there was a play-in game that eliminated one of the lower-ranked teams. In 2011 68 teams were selected and the number of play in games was increased to four. In that year, two of these games were for two 16<sup>th</sup> seeds and one each for a 11<sup>th</sup> and 12<sup>th</sup> seed. 

The remaining 64 teams are then divided into four groups (regions) of 16 teams each. Within each region the teams are ranked 1 through 16, and in the first round the best team (ranked 1) plays the lowest-ranked team. The Number 2 plays Number 15, etc. Since this is a single elimination tournament, the winner plays in the second round; the loser goes home. If the difference in seedings yielded perfect forecasts, in the second round Number 1 would play Number 8 and Number 2 would play Number 7, etc. This process continues through two more rounds, yielding four regional winners (the Final Four) who then play two more rounds to determine the National Champion. 

However, in virtually every tournament there have been upsets and these outcomes have not occurred. It is thus possible and necessary to determine whether the difference in rankings has predictive value. The seedings in the regional rounds cannot be used in making predictions for these final two rounds because they only refer to the team rankings in each region and do not measure the overall difference in the abilities of these teams. Thus the Boulier-Stekler method of using the difference in ranks as a forecast of the winner cannot be used in these rounds, but the new data, the consensus rankings, do provide this information. 

### 2. LITERATURE REVIEW 

A number of different methods for predicting the winner of a game in the NCAA tournament have been proposed. These predictors include a variety of information about the teams’ performance during the regular season and various ratings systems. (See Carlin, 1996; Harville, 2001; Caudill, 2003; Kvam and Sokol, 2006). Currently, a frequently used methodology has been to use the difference in seeds either as a predictor by itself or in models which predict the probability that the better seeded team will win (Schwertmann et al., 1991; Schwertmann et al., 1996; Boulier and Stekler, 1999; Jacobson and King, 2009). 

Boulier and Stekler presented two sets of results. The first was descriptive and provided information about the winning percentage by rank and the overall result that higher-ranked teams defeated lower-ranked opponents 73.5% of the time. These results were obtained by aggregating the results over the first four rounds of the tournament. The statistical method was a probit function, in which 

2 

#### Stekler and Klein: NCAA Championship Games 

the outcome of a discrete event, (winning or losing), was related to the difference in the seeds of the two teams. This approach was applied in pseudo real time by recursively estimating the probits and evaluating the forecasts using a quantitative measure. 

This quantitative measure is the Quadratic Probability Score (QPS) also known as the Brier Score (Brier, 1950). In essence this is the mean square error of the probability forecasts. For each method this statistic is calculated by equation (1). 





> where _ft_ represents the forecasted probability that the better ranked team will win 

> the game, _ot_ is the actual outcome of the game (0 if the underdog won  and 1 if the favored team won) and N is equal to the number of games in each round. 

### 3. DATA AND METHODOLOGY 

### 3.1 Data 

The data cover the NCAA tournaments of 2003-2010. These years were selected because the consensus forecasts were not available prior to 2003.The seedings and the outcomes of the games were obtained from the NCAA Web site. The second set of data is the consensus (average) rankings of each Division I team obtained from 29-45 individuals, systems, and polls. These rankings are gathered by Kenneth Massey and are archived on his web site, _www.masseyratings.com_ . The rankings that are used in this analysis were those that were available just before each NCAA tournament began. 

### 3.2 Methodology 

The methodology used in this analysis is similar to that of Boulier and Stekler. We first calculated the percentage of times when the better rated team won. This was done for both the seedings and the consensus rankings, yielding the descriptive statistics. A variation of the earlier procedure was to calculate these percentages for each round not just for the entire tournament as was done by Boulier and Stekler. 

In order to establish the relationship between the difference in seedings (consensus rankings) and the probability that the better ranked team wins, we use probit models. These probits were calculated for the entire tournament and for 

3 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

each of the rounds. A probit model relates the probability that a discrete event (winning or losing) is explained by either the difference in tournament seedings or the difference in consensus rankings. 

Formally, the probit model is written as: **Pr(y=1|x) = Φ(xb),** where **Φ** is the standard cumulative normal probability distribution; y =1 is a win; the xis are the explanatory variables, the difference in seedings and consensus rankings; and a one unit change in x increases the probability of a win by  b units. Our procedure differs slightly from that of Boulier-Stekler because these probits are estimated for the four rounds for which the seedings data are available and the six rounds for which the consensus data are available. There is an additional difference from the Boulier-Stekler procedure. They recursively estimated the probit models for each year while this paper calculates only a single ex post set of equations. 

### 4. RESULTS 

There were 504 games in the eight tournaments between 2003 and 2010, with 480 occurring in the first four rounds.  The seedings and consensus rankings data were <u>both</u> available for only the 480 games in these rounds. In all but 21 of these 480 games, both rankings agreed on which team was considered better. These differences primarily occurred in the first round and involved the teams seeded eighth (seventh) playing the ninth (tenth) seed. 

In the first four rounds, forecasts based on the difference in the consensus rankings were slightly more accurate but not significantly different than those based on the difference of the seeds, 73.8% versus 72.3% (Table 1). In Rounds 1- 3, both measures provide predictions that are significantly different from chance, with p values close to zero, but in Round 4, the Regional Championship, neither measure was significantly better than flipping a coin. 

Only the consensus rankings were available for Rounds 5 and 6, the Final Four and Tournament Championship games. Those results are mixed. The results for Round 5, when 12 of the favored 16 favored teams won, are significantly different from those that would have been obtained from flipping a coin; those for Round 6 are no better than chance, i.e. 5 of 8. If the results for those two rounds are combined, the better ranked team won 17 of the 24 games which is significantly better than chance with a p value of .032. However, if the results based on the difference in consensus rankings for Rounds 4-6 are combined, the results, once again are not better than chance. 

4 

Stekler and Klein: NCAA Championship Games 

Table 1 Percentage of Time Better Ranked Team Won; by Seed and Consensus Rankings, by Round 

|||Seed|Consensus|
|---|---|---|---|
|**Overall**|NumberofGames|480|504|
||%|72.3|73.6<sup>a</sup>|
|Round 1|NumberofGames|256|256|
||%|75.8|77.7|
|Round 2|Number of Games|128|128|
||%|68.8|71.1|
|Round 3|NumberofGames|64|64|
||%|75.0|75.0|
|Round 4|NumberofGames|32|32|
||%|53.1|50.0|
|Round 5|NumberofGames|N/A|16|
||%|N/A|75.0|
|Round 6|NumberofGames|N/A|8|
||%|N/A|62.5|



a. The winning percentage for the 480 Round 1-4 games was 73.8% 

Table 2 

Magnitude of Difference in Seedings and Consensus Rankings by Round 

||Seedings|Consensus<br>Rankings|
|---|---|---|
|Round 1|8|62|
|Round 2|5.6|25|
|Round 3|4.2|16|
|Round 4|2.7|11|
|ound 5|N/A|7.6|
|Round 6|N/A|4.8|



5 

_Submission to Journal of Quantitative Analysis in Sports_ 

One explanation for the difference in the results for Rounds1-3 and those for Rounds 4-6 is that the teams in the later rounds are more comparable in quality, thus making forecasting more difficult. The difference in rankings based on either set of rankings is much smaller in the later rounds. (Table 2). As further evidence about the difficulty of forecasting the outcomes of games when the teams are similar in quality, we examined the first round games between teams ranked 7 and 10 and 8 and 9. The better ranked team won only 53% of the time. 

Table 3 presents the coefficients obtained from estimating the probits. The difference in the seedings (consensus) is defined as the rank of favored team minus that of the underdog. Therefore, the sign of the coefficient is expected to be negative, i.e. the bigger the difference, the greater the probability that the favorite will win. 

Table 3 

Coefficient Estimates of the Effect of Differences in Seedings (Consensus) on Probability of Better Ranked Team Winning—Obtained from Profits by Round 

||Difference in<br>seedings Only|Difference in<br>consensus<br>Only|Difference in|Both   Variables|
|---|---|---|---|---|
||||Seedings|Consensus|
|All rounds|-0.14<br>(8.40)xxx|-0.02<br>(6.40)xxx|-0.05<br>(1.62)|-0.01<br>(3.09)xxx|
|Round 1|-0.15<br>(7.64)xxx|-0.02<br>(6.40)xxx|-0.06<br>(1.23)|-0.01<br>(2.75)xx|
|Round 2|-0.12<br>(2.63)xx|-0.04<br>(4.53)xxx|0.009<br>(0.166)|-0.04<br>(3.72)xxx|
|Round 3|-0.21<br>(2.37)xx|-0.05<br>(2.80)xx|-0.14<br> (.96)|-0.02<br>(0.73)|
|Round 4|-0.1<br>(.88)|- 0.03<br>(1.01)|0.062<br>(0.3)|-0.04<br> (0.86)|
|Round 5|NA|-0.03<br> (0.93)|||
|Round 6|NA|-0.04<br>(0.38)|||



Numbers in parentheses are t-ratios; xxx, xx significant at 1% and 5% levels 

The results confirm this hypothesis. When the probits are estimated using either variable alone, the coefficients are negative and significantly different from zero beyond the 1% level for the first three rounds. (The information in either variable does not add to that contained in the other one- see the multiple 

6 

Stekler and Klein: NCAA Championship Games 

regression results in the right-hand columns of Table 3). The size of the coefficients indicates that each unit increase in the difference of the ranks increases the probability of the favored team’s winning by 1-2%. While the results for the two approaches were similar, it should, however, be noted that the consensus rankings were slightly more accurate and were available for the later rounds. 

### 5. CONCLUSION 

Using data for 2003-2010, this paper evaluated the Boulier-Stekler methodology, derived from another set of tournaments, for predicting the winners in the NCAA Tournaments. We showed that this approach was successful in predicting the overall winners and those of the first three rounds. Its record was no better than chance in the fourth Round. 

Because these data were not available for the Final Four and Championship games, we also evaluated another set of data that was available for all six rounds. These data consisted of the average rankings of analysts, etc. We showed that the consensus rankings were slightly more accurate than the seedings in the early games, but had the same limitations as the seedings in the later rounds. We also showed that the quality of the teams, as measured by the consensus rankings, were more similar in those later games, thus making predictions more difficult. 

### References 

- Boulier, B., and Stekler, H. O. (1999). “Are Sports Seedings Good Predictors?: An Evaluation,” _International Journal of Forecasting_ , 15, 83-91. 

- Carlin, B. P. (1996). “Improved NCAA Basketball Tournamant Modeling via Point Spread and Team Strength Information,” _The American Statistician_ , 50, 39-43. 

- Caudill, S. B. (2003). “Predicting Discrete Outcomes with the Maximum Score Estimator: The Case of the NCAA Men’s Basketball Tournament”, _International Journal of Forecasting_ , 19, 313-317. 

- Clair, B., and Letscher, D. (2007). “Optimal Strategies for Sports Betting Pools”, _Operations Research_ , 55, 1163-1177. 

- Harville, D. A. (2003). “The Selection or Seeding of College Basketball or Football Teams for Postseason Competition”, _Journal of the American Statistical Association_ , 98,17-27. 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 

Jacobson, S. H., and King, D.M. (2009). “Seeding in the NCAA Men’s Basketball Tournament: When is a Higher Seed Better?”, _The Journal of Gambling Business and Economics_ , 3, 63-87. 

- Kaplan, E. H., and Garska, S. J. (2001). “March Madness and the Office Pool”, _Management Science, 47_ , 369-382. 

- Kvam, P., and Sokol, S. J. (2006). “A Logisitic Regression/Markov Chain Model for NCAA Basketball”, _Naval Research Logistics_ , 53,788-803. 

- Metrick, A. (2001). “March Madness? Strategic Behavior in NCAA Basketball Tournament Betting Pools”, _Journal of Economic Behavior and Organization_ , 30, 159-172. 

- Schwertman, N. C., McCready, T. A., and Howard, L. (1991). “Probability Models for the NCAA Regional Basketball Tournaments”, _The American Statistician_ , 45, 35-38. 

- Schwertman, N. C., Schenk, K. L., and Holbrook, B. C., (1996). “More Probability Models for the NCAA Regional Basketball Tournaments”, _The American Statistician_ , 50, 34-38. 

8 


