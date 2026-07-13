<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Calculating Wins over Replacement Player (WORP) for NHL Goaltenders - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1358 

## Calculating Wins over Replacement Player (WORP) for NHL Goaltenders 

**Stephen M. Shea,** _Saint Anselm College_ **Christopher E. Baker,** _hockeymetrics.com_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1358 

## Calculating Wins over Replacement Player (WORP) for NHL Goaltenders 

Stephen M. Shea and Christopher E. Baker 

#### **Abstract** 

We present formulas for calculating wins over replacement player (WORP) for NHL goaltenders. If a team's primary objective is victory over its opponent, then a player's value may best be determined by his ability to help his team win games. Furthermore, a player's contribution to his team's wins would be a universal unit of measure and would allow for direct comparisons of goalie and skater production. We found inspiration for our work in Keith Woolner’s calculations of “value over replacement player“ (VORP) for MLB players, and we will make use of Bill James’ “Pythagorean Method” as it was applied to the NHL by Cochran and Blackstock in 2009. 

**KEYWORDS:** goalie, goaltender, NHL, Pythagorean Method, WORP 

**Author Notes:** We thank the anonymous referee for helpful comments, and in particular, for pointing out Keri (2006), which we reference in Section 7. 

Shea and Baker: Calculating WORP for NHL Goaltenders 

### **1 Introduction** 

Statistical methods for evaluating the on ice impact of a National Hockey League (NHL) goaltender have evolved over time. Initially, a simple comparison of goals against averages was common practice. The addition of save percentages in 198283 (see NHL.com, 2010) shed new light on a goalie’s ability to block shots. Recent studies of shot quality, such as Krzywicki (2010), have the potential to again redefine how we measure a goalie’s performance. These rate statistics well quantify a goalie’s production, but do not directly reveal a goalie’s contribution towards his team’s ultimate ambition. If a team’s primary objective is victory over its opponent, then a player’s value may best be determined by his ability to help his team win games. Furthermore, a player’s contribution to his team’s wins would be a universal unit of measure and would allow for direct comparisons of goalie and skater production. While this type of valuation is not well understood for goaltenders in the game of hockey, we can glean insight from recent studies of baseball statistics. 

Bill James (1988) started a statistical revolution in baseball with the annual Baseball Abstract (available 1979-1988). Through the formulation of new statistics such as runs created, James redefined how we measure a baseball player’s worth to his team. Woolner (2002) added a new twist to the definition. Instead of simply determining a player’s value to his team, Woolner decided it was more beneficial to understand the value of an individual when compared to an average player at that position. This new statistic, called a player’s value over replacement player (VORP), calculates the value of a hitter or pitcher (in runs) to their respective baseball team over some hypothetical replacement player. The replacement player is taken to be a player that produces at some percentage of the league average that season for the position being replaced. According to Neyer (2007), the specific percentage varies depending on position. This variation limits both the understanding of the statistic and the ability to easily compare players at one position to another. The output in runs is also not ideal. As stated above, if a team’s main objective is to win games, then the most appropriate unit of measure for a player’s worth to their team is wins. There are several sites such as BaseballProspectus.com (for which Woolner is an author) that calculate wins above replacement (WAR) for baseball players at all positions. While this statistic is loosely definable, there does not seem to be a consensus on how best to calculate it. 

Here, we present formulas for calculating wins over replacement player (WORP) for NHL goalies. We begin by using a multiple regression model with two independent variables (team goals for and team goals against) to predict wins. We believe this model has value in its simplicity. Next, we use the Pythagorean Method, invented by James (1980), and applied to the NHL by Cochran and Blackstock (2009) to relate goals for and goals against to win percentage, and thus wins. 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

In Sections 4 and 5, we define a new statistic we call goals against saved, and use it to calculate WORP. We expand upon the concept of WORP in Section 6, by introducing team-independent WORP (TIWORP). In Section 7, we discuss our particular choice of a replacement player. We finish by discussing future directions. 

### **2 Multiple Regression** 

Multiple regression is an extension of simple linear regression where we use more than one independent (or predictor) variables. Our independent variables are a team’s goals for ( _GF_ ) and goals against ( _GA_ ) in a given season. The dependent variable in our model is the team’s _total wins_ . Here, _total wins_ = _wins_ + (0 _._ 5) _ties_ . In other words, we will count a tie as half a win. Prior to the 2005-06 season, the NHL awarded 2 points to a win and 1 point to a tie. So, for these seasons, _total wins_ =<sup>_<u>points</u>_</sup> 2 . Since the 2005-06 season, the NHL has given the same number of points to an over-time loss (1 point) as they gave to a tie prior to 200506 (see Cochran and Blackstock, 2009). For the seasons since 2005-06, we will count an overtime loss as a tie. In other words, for the seasons since 2005-06, _total wins_ = _wins_ + (0 _._ 5)( _overtime losses)_ . A change in the rules during the era we are considering is not ideal for our statistical study; however, by defining _total wins_ as we have, we will stay consistent with the NHL’s attribution of points in that _total wins_ is always points divided by two. Our choice is also consistent with Cochran and Blackstock (2009), which we will use later in our article. In this section, we first compute a multiple regression for all seasons combined. We then compute a separate regression for each season. At the end of Section 3, we compute the sum of squared errors (or residuals) for both methods. The method using separate regressions for each season is a considerable improvement over the multiple regression for all seasons combined. This improvement may be, in part, due to the rules change. From this point on, a _win_ (in the NHL) means a _total win_ as defined above. For our multiple regression, we are looking for an optimal _a_ , _b_ , and _c_ in the equation 



The optimal coefficients are the coefficients that minimize the sum of squared errors (SSE): 



where _Wi_ represents the number of wins for team _i_ and _Wi_<sup>_′_is the projected number</sup> of wins for the same team by the multiple regression. 

2 

Shea and Baker: Calculating WORP for NHL Goaltenders 

We used all records from the 1982-83 through 2009-10 seasons. We found the function with optimal coefficients to be 



In this case, our standard error (SE) for the wins estimate was 4.33. 

We then computed a separate multiple regression for each individual season from the same time period. The NHL game has changed over the last 30 years. By computing a separate regression for each season, we hope to account for any significant differences in, for example, style of play since 1982-83. Table 1 displays our results. 

Table 1: Multiple Regression by Season 

|Seas.|a|b|c|SE|Seas.|a|b|c|SE|
|---|---|---|---|---|---|---|---|---|---|
|82-83|.1354|_−_.1380|40.8|2.11|96-97|.1608|_−_.1607|41.0|1.77|
|83-84|.1582|_−_.1362|33.0|2.38|97-98|.1677|_−_.1790|43.5|1.68|
|84-85|.1516|_−_.1201|30.2|2.05|98-99|.1866|_−_.1660|36.5|2.11|
|85-86|.1615|_−_.1347|31.5|2.51|99-00|.1595|_−_.1562|42.5|2.14|
|86-87|.1503|_−_.1598|42.8|2.51|00-01|.1799|_−_.1719|41.2|2.12|
|87-88|.1347|_−_.1510|44.8|2.22|01-02|.1951|_−_.1459|32.5|2.09|
|88-89|.1566|_−_.1362|33.9|1.96|02-03|.1714|_−_.1724|43.8|1.66|
|89-90|.1407|_−_.1441|41.0|2.07|03-04|.1580|_−_.1691|45.7|2.23|
|90-91|.1363|_−_.1579|46.0|2.53|05-06|.1715|_−_.1724|43.5|3.25|
|91-92|.1501|_−_.1523|40.6|2.04|06-07|.1472|_−_.1823|51.4|2.61|
|92-93|.1373|_−_.1679|51.3|2.36|07-08|.1445|_−_.1785|50.7|2.04|
|93-94|.1451|_−_.1303|38.0|3.10|08-09|.1903|_−_.1736|39.1|2.20|
|94-95|.1770|_−_.1376|18.4|1.92|09-10|.1691|_−_.1782|48.1|2.03|
|95-96|.1510|_−_.1644|44.4|2.21||||||



### **3 Pythagorean Method** 

It wouldn’t surprise most baseball fans that runs scored ( _RS_ ) and runs allowed ( _RA_ ) are related to a team’s win/loss percentage ( _W_ %). Here, 



After all, a team wins if they score more runs than their opponent. James (1980) found that 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 



James dubbed this approach the “Pythagorean Method” because of its similarities to the Pythagorean theorem. The Pythagorean theorem states that the square of the hypotenuse of a right triangle is the sum of the squares of the other two sides. 

Cochran and Blackstock (2009) developed a similar relationship in the NHL. Recall that the NHL has ties. As we have done in the previous section, Cochran and Blackstock considered a tie (or overtime loss) as a half a win. They let 



(where again _wins_ means _total wins_ as defined in the previous section). Applying equation (5) to the NHL, we find 



An obvious question is whether the exponent of 2 in this case is optimal. Cochran and Blackstock (2009) set out to “find the exponent that minimizes the sum of the absolute errors when using James’ Pythagorean method” for data collected from the 1917 through 2007 seasons. Their formula was the following: 



where _t_ indexes the season, _nt_ is the number of teams in the NHL in season _t_ , teams are indexed by _i_ = 1 _,_ 2 _,...nt_ in each season _t_ , and _wlpctit_ (resp. _git_ , resp _sit_ , resp. _ait_ ) is the _W_ % (resp. number of games played, resp. number of goals scored, resp. number of goals allowed) for team _i_ in season _t_ . 

Cochran and Blackstock (2009) found the optimal coefficient to be _x_ = 1 _._ 927. The mean error was approximately 2 _._ 831%. There, mean error was the average value of the absolute values of the errors. In the modern 82 game schedule, 2 _._ 831% is approximately 2.32 games. When they restricted to data from 1980 through 2007, the optimal coefficient was _x_ = 1 _._ 99063 and the mean error was approximately 3 _._ 050%. In the modern 82 game schedule, 3 _._ 050% is approximately 2.50 games. Since we have restricted our focus to the 1982-83 through 2009-10 seasons, we are more interested in the coefficient _x_ = 1 _._ 99063, yielding the equation 

4 

Shea and Baker: Calculating WORP for NHL Goaltenders 



We have now presented three methods to predict wins using goals for and goals against. The three methods were the multiple regression for all seasons combined, the separate multiple regressions for each season, and the Pythagorean method. One way to compare the accuracy of the three models is to compute the sum of squared errors (or residuals) in each case (see equation 2). For a given team in a given season a model will predict a certain number of wins, _W_<sup>_′_</sup> . That team will have an actual number of wins, _W_ , in the same season. The error is ( _W_<sup>_′_</sup> _−W_ ) and the squared error is ( _W_<sup>_′_</sup> _− W_ )<sup>2</sup> . We then sum the squared errors where the sum is taken over all teams in each season from the 1982-83 season through the 2009-2010 season (690 entries in all). The sum of squared errors for the multiple regression for all seasons combined was approximately 12885.02. That’s an average squared error of approximately 18.67. The sum of squared errors for the separate multiple regression for each season was approximately 3083.22. That’s an average squared error of approximately 4.47. The sum of squared errors for the Pythagorean method was approximately 5416.74. That’s an average squared error of approximately 7.85. The difference in the sum of squared errors between the multiple regression for all seasons combined and the Pythagorean method speaks to the value of the Pythagorean method. The separate multiple regression for each season had the lowest sum of squared errors. Unlike the other two methods, this method has the benefit of computing a separate formula for each season. 

### **4 Save Percentage and Goals Against Saved** 

Save percentage (SV%) is defined to be 



We will use the average save percentage (ASV%) in a given season as the representative statistic for the replacement goalie in that season. Table 2 displays the total shots on goal (SOG), excluding empty net shots, total goals against (GA), excluding empty net goals, and ASV% for all NHL seasons played from 1982-83 though 2009-10. 

We will define a quantity goals against saved for each goalie in a given season. Goals against saved represents the difference in goals against for a given goalie and the goals that a hypothetical replacement would allow if he faced the same number of shots on goal. This quantity is calculated by multiplying the shots 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

on goal a given goalie faced by the difference between the save percentage of the goalie and the league save percentage for that season. For player _r_ on team _s_ in season _t_ , we define goals against saved over the replacement player (GAS) to be 



where _SV_ % _t_ is the average save percentage in season _t_ , and _SOGrst_ (resp. _GArst_ , resp. _SV_ % _rst_ ) are the shots on goal faced (resp. goals allowed, resp. save percentage) for goalie _r_ on team _s_ in season _t_ . The expression (1 _− SV_ % _t_ )( _SOGrst_ ) represents the projected goals allowed by the hypothetical replacement goalie. GAS is positive for goalies that have a higher SV% than the average SV% in their respective season. GAS will be an essential component in our definition of WORP. For a discussion of why we chose the league save percentage as the statistic for our replacement, see Section 7. 

Table 2: Average Save Percentage 

|Season|SOG|GA|ASV%|Season|SOG|GA|ASV%|
|---|---|---|---|---|---|---|---|
|1982-83|51310|6380|0.8757|1996-97|63364|6037|0.9047|
|1983-84|51401|6503|0.8735|1997-98|58115|5449|0.9062|
|1984-85|50883|6372|0.8748|1998-99|61544|5675|0.9078|
|1985-86|52147|6556|0.8743|1999-00|64053|6124|0.9044|
|1986-87|50400|6046|0.8800|2000-01|67957|6574|0.9033|
|1987-88|51145|6146|0.8798|2001-02|67654|6241|0.9078|
|1988-89|51027|6154|0.8794|2002-03|69601|6345|0.9088|
|1989-90|50515|5996|0.8813|2003-04|68821|6129|0.9109|
|1990-91|49973|5696|0.8860|2005-06|73573|7264|0.9013|
|1991-92|53557|5990|0.8882|2006-07|72574|6877|0.9052|
|1992-93|62327|7173|0.8849|2007-08|71288|6476|0.9092|
|1993-94|66017|6927|0.8951|2008-09|74081|6779|0.9085|
|1994-95|36522|3631|0.9006|2009-10|74371|6599|0.9113|
|1995-96|64344|6536|0.8984|||||



### **5 WORP** 

Dominik Hasek is one of the best NHL goalies of all time. In 1996-97, he had one of his best seasons, where he played in 67 games, posted a 37-20-10 record (37 wins, 20 losses, 10 ties), and had a save percentage of 0.930. In addition, he faced a total 

6 

Shea and Baker: Calculating WORP for NHL Goaltenders 

of 2177 shots on goal (SOG) that season. The Sabres had a record of 40-30-12. To get a sense of how valuable Hasek was to his Buffalo Sabres that particular season, we might want to go back to 1996, replace Hasek in net with some other goaltender, perhaps a goalie closer to the average in terms of statistical production, and then everything else being equal, let the season play out. Presumably, the Hasek-less Sabres would finish with fewer wins than they totaled with Hasek in net for the greater part of 1996-97. 

Unfortunately, we cannot go back in time and play the entire season over with our desired changes. However, we do know that the average save percentage for the 1996-97 season was 0.9047, and Hasek posted a 0.930 save percentage that season. Furthermore, we know that Hasek faced 2177 SOG as the goalie for the Sabres that season. Had a goalie with the average save percentage of .9047 faced 2177 SOG, he would have given up approximately 54.41 more goals that season than Hasek. So, how many fewer games would the Sabres have won with the hypothetical average replacement in net as compared to the great Dominik Hasek? To determine the difference in wins, we will use functions _f_ ( _GA, GF_ ) = _wins_ that take the goals for and goals against for a given team in a season and output wins. During the 1996-97 season, the Sabres scored 237 goals and let in 208 goals. To determine the value (in wins) of Hasek over the average replacement goalie to the Sabres in the 1996-97 season, we use the formula _f_ (208 _,_ 237) _− f_ (208 + 54 _._ 41 _,_ 237). All that is left is to determine _f_ . 

Our _f_ functions will come from the work in the previous sections. We will use the multiple regression from equation (3) of Section 2. We will also use the multiple regression equations calculated for each season that are collected in Table 1 in Section 2. Finally, we will use Cochran and Blackstock (2009), specifically equation (9) of Section 3. Since this equation relates win percentage (and not wins) to goals for and goals against, we will multiply the equation by the games played by the team in the respective season. Then, 



Let’s begin with the multiple regression, equation (3), that was computed using all data from 1982-83 through 2009-2010. Using eq. (3), we calculate WORP for player _r_ on team _s_ in season _t_ as follows. 

_WORP_ = [(0 _._ 16422) _GFst_ +( _−_ 0 _._ 14741) _GAst_ + 36 _._ 95095] _−_ [(0 _._ 16422) _GFst_ + ( _−_ 0 _._ 14741)( _GAst − GArst_ +( _SOGrst_ )(1 _− SV_ % _t_ ))+ 36 _._ 95095] 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 



where _GFst_ (resp. _GAst_ ) are the goals scored (resp. goals against) for team _s_ in season _t_ , _GArst_ are the goals allowed by player _r_ on team _s_ in season _t_ , _SOGrst_ are the shots on goal faced by goalie _r_ for team _s_ in season _t_ , and _SV_ % _t_ is the average save percentage for season _t_ . 

We present the top 10 and bottom 5 WORP (using a multiple regression for all seasons combined) in Tables 3 and 4. In total, there were 34 instances where goalies produced a WORP at 5 or above. Of the 2276 total records, 949 yielded a positive WORP. Of our records, 39 were on players that played minimal to no time and generated a WORP of 0. 

Table 3: Top 10 WORP from 1982-83 through 2009-10 using a multiple regression for all seasons combined (eq. 13) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|1|Curtis Joseph|92-93|STL|68|2202|.911|57.4|8.46|
|2|J. Vanbiesbrouck|93-94|FLA|57|1912|.924|55.6|8.20|
|3|D. Hasek|97-98|BUF|72|2149|.932|54.5|8.03|
|4|D. Hasek|96-97|BUF|67|2177|.930|54.4|8.02|
|5|D. Hasek|98-99|BUF|64|1877|.937|54.1|7.97|
|6|D. Hasek|93-94|BUF|58|1552|.930|53.8|7.94|
|7|R. Luongo|03-04|FLA|73|2475|.931|48.4|7.14|
|8|P. Lindbergh|84-85|PHI|65|1929|.899|47.6|7.01|
|9|Patrick Roy|91-92|MON|67|1806|.914|47.0|6.93|
|10|Patrick Roy|89-90|MON|54|1524|.912|46.9|6.91|



Table 4: Bottom 5 WORP from 1982-83 through 2009-10 using a multiple regression for all seasons combined (eq. 13) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|2272|Denis Herron|82-83|PIT|31|931|.838|_−_35.2|_−_5.19|
|2273|Jeff Hackett|92-93|SJS|36|1220|.856|_−_35.6|_−_5.25|
|2274|B. Hayward|85-86|WPG|52|1373|.842|_−_44.4|_−_6.54|
|2275|P. Sidorkiewicz|92-93|OTT|64|1737|.856|_−_50.1|_−_7.38|
|2276|C. Billington|93-94|OTT|63|1801|.859|_−_65.0|_−_9.58|



Next, we present the results using the Pythagorean formula (equation (12)) in Table’s 5 and 6. Combining eq. (12) with the methods presented in this section, _WORP_ = 

8 

Shea and Baker: Calculating WORP for NHL Goaltenders 





where _GPst_ is the number of games played by team _s_ in season _t_ . 

Using equation (14), there were 50 instances (out of 2276) where a goalie posted a WORP of 5 or better. 949 of the records yielded a positive WORP (the same as with the previous method). Hasek takes the top 4 spots in the rankings. Hasek also had an impressive strike-shortened season in 1994-95. Using equation (14), Hasek’s 1994-95 season for the Sabres ranks 23rd with a WORP of 6.32. Since there were only 48 games that season, there was less opportunity for any goalie in 1994-95 to accumulate WORP (either positive or negative). The top ranking 200910 season belongs to Ryan Miller of the Buffalo Sabres. Miller’s 6.54 wins over replacement player ranks 19th. 

Comparing the two formulas presented thus far, 8 of the top 10, including the top 7 records using equation (13) show up in the top 10 when using equation (14). The two seasons that drop out of the top 10 remain in the top 18. Craig Billington’s 1993-94 season for the Ottawa Senators takes last place for both formulas. Typically, it is difficult to accumulate negative WORP as poor performance often leads to diminished playing time. One has to wonder why Ottawa played Billington in 63 games in 1993-94 in spite of his amazingly high 4.59 goals against average and unimpressive save percentage of .859. 

Table 5: Top 10 WORP from 1982-83 through 2009-10 using the Pythagorean method (eq. 14) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|1|D. Hasek|98-99|BUF|64|1877|.937|54.1|10.91|
|2|D. Hasek|97-98|BUF|72|2149|.932|54.5|10.38|
|3|D. Hasek|96-97|BUF|67|2177|.930|54.4|9.44|
|4|D. Hasek|93-94|BUF|58|1552|.930|53.8|9.00|
|5|J. Vanbiesbrouck|93-94|FLA|57|1912|.924|55.6|8.16|
|6|Jose Theodore|01-02|MON|67|1972|.931|45.9|7.98|
|7|Patrick Roy|91-92|MON|67|1806|.914|47.0|7.93|
|8|Curtis Joseph|92-93|STL|68|2202|.911|57.4|7.78|
|9|M. Kiprusoff|05-06|CGY|74|1951|.923|41.6|7.69|
|10|R. Luongo|03-04|FLA|73|2475|.931|48.4|7.54|



In Section 2, we computed a multiple regression for each season. The data are collected in Table 1. In Table’s 7 and 8, we present WORP using a separate multiple regression for each season. Comparing Table 7 to Table 3, we see that 8 of 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

Table 6: Bottom 5 WORP from 1982-83 through 2009-10 using the Pythagorean method (eq. 14) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|2272|Arturs Irbe|02-03|CAR|34|816|.877|_−_25.6|_−_4.26|
|2273|Olaf Kolzig|07-08|WAS|54|1423|.892|_−_23.7|_−_4.38|
|2274|C. Osgood|08-09|DET|46|1208|.887|_−_26.5|_−_4.41|
|2275|B. Hayward|85-86|WPG|52|1373|.842|_−_44.4|_−_4.91|
|2276|C. Billington|93-94|OTT|63|1801|.859|_−_65.0|_−_5.38|



the top 10 using eq. (13) remain in the top 10 when we compute separate regressions for each season. In both instances, Curtis Joseph remained in the top 2 and Hasek put 4 seasons in the top 10. Comparing the WORP figures in the three methods, the Pythagorean method yielded the most positive and least negative numbers. Table 9 displays the 0th, 25th, 50th, 75th and 100th percentiles of the three methods. 

Table 7: Top 10 WORP from 1982-83 through 2009-10 using a separate multiple regression for each season (Table 1) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|1|D. Hasek|97-98|BUF|72|2149|.932|54.5|9.76|
|2|Curtis Joseph|92-93|STL|68|2202|.911|57.4|9.64|
|3|D. Hasek|98-99|BUF|64|1877|.937|54.1|8.98|
|4|D. Hasek|96-97|BUF|67|2177|.930|54.4|8.75|
|5|R. Luongo|03-04|FLA|73|2475|.931|48.4|8.19|
|6|J. Vanbiesbrouck|93-94|FLA|57|1912|.924|55.6|7.25|
|7|M. Kiprusoff|05-06|CGY|74|1951|.923|41.6|7.18|
|8|Patrick Roy|91-92|MON|67|1806|.914|47.0|7.16|
|9|Tim Thomas|08-09|BOS|54|1694|.933|41.0|7.12|
|10|D. Hasek|95-96|BUF|59|2011|.920|43.3|7.11|



### **6 Team Independent WORP** 

In the previous section, we calculated the wins over the average replacement player for a given player on a given team. The final WORP calculation always depended on the shots on goal the goalie faced on his given team. This is as one might expect, since the more shots a goalie faces, the more valuable or detrimental his ability to stop shots becomes for his team. However, one might hope for a team independent WORP, some measure of a goalies value in wins that is not dependent on the team 

10 

Shea and Baker: Calculating WORP for NHL Goaltenders 

Table 8: Bottom 5 WORP from 1982-83 through 2009-10 using a separate multiple regression for each season (Table 1) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|GAS|WORP|
|---|---|---|---|---|---|---|---|---|
|2272|S. Caron|03-04|PIT|40|1179|.883|_−_33.0|_−_5.58|
|2273|B. Hayward|85-86|WPG|52|1373|.842|_−_44.4|_−_5.98|
|2274|Jeff Hackett|92-93|SJS|36|1220|.856|_−_35.6|_−_5.98|
|2275|P. Sidorkiewicz|92-93|OTT|64|1737|.856|_−_50.1|_−_8.41|
|2276|C. Billington|93-94|OTT|63|1801|.859|_−_65.0|_−_8.47|



<u>Table 9: Percentiles of 3 methods</u> 

|Method|100%|75%|50 %|25%|0%|
|---|---|---|---|---|---|
|Multiple regression for all||||||
|seasons combined(eq. 13)|8.46|.5289|_−_.1326|_−_.8253|_−_9.38|
|Pythagorean method(eq. 14)|10.91|.5553|_−_.1340|_−_.8535|_−_5.38|
|Separate multiple regression||||||
|for each season(Table 1)|9.76|.5574|_−_.1447|_−_.8860|_−_8.47|



he plays for. To do this, we suppose the given goalie has seen the average shots on goal rate in the given season for the amount of time that the goalie played. We then multiply this number of shots on goal by the difference in the given goalie’s save percentage and the league save percentage. This projects how many more (or fewer) goals the goalie would save over a league average replacement, if the goalie faced the league average shots on goal rate. This can be seen as a variation of goals against saved. We then convert this quantity to a team independent WORP. In this section, we will use the multiple regression formulas collected in Table 1. One could just as easily use the other two methods. Here is our formula for team independent WORP (TIWORP) for player _r_ , team _s_ and season _t_ . 



where _minrst_ (resp. _SV_ % _rst_ ) is the minutes played by (resp. save percentage of) goalie _r_ for team _s_ in season _t_ , _mint_ (resp. _SOGt_ , resp. _SV_ % _t_ ) is the total minutes (resp. total shots on goal, resp. average save percentage) for goalies in season _t_ , and _bt_ is the b in Table 1 associated with season _t_ . We again emphasize that we are summing the data when goalies are in net and thus, excluding empty net statistics. We present our results in Tables 10 and 11. 

In Table 10, Ed Belfour makes his first appearance among our top 10 lists. Belfour played behind some very good defenses in Chicago in the early 1990’s. As a result, Belfour did not consistently see as many SOG as Hasek, for example. In 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

1996-97, Hasek saw 2177 SOG in 67 GP. In 1990-91, Belfour saw 1883 SOG in 74 GP. Having seen fewer SOG, Belfour was not able to accumulate WORP to the same level as Hasek. TIWORP is dependent on the total SOG in a given season and not the SOG for a given goalie in that season. As a result, TIWORP, in a sense, puts Belfour and Hasek on a level playing field. For more comments on this, see Remark 4 of Section 8. For each record, we calculated TIWORP and WORP using Table 1. We then took the difference (TIWORP _−_ WORP, which we’ll denote by ∆). The top five differences are presented in Table 12. We see a larger positive difference for goalies that performed well but saw below average SOG per minute. We also see a larger positive difference for goalies that performed poorly and saw an above average SOG per minute. In total, 3 goalies saw a difference of 1 or greater, and only 24 saw an increase of .5 or more. 

Table 10: Top 10 TIWORP from 1982-83 through 2009-10 using a separate multiple regression for each season (Table 1) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|TIWORP|
|---|---|---|---|---|---|---|---|
|1|Dominik Hasek|97-98|BUF|72|2149|.932|8.75|
|2|Curtis Joseph|92-93|STL|68|2202|.911|8.71|
|3|Dominik Hasek|98-99|BUF|64|1877|.937|8.49|
|4|Mikka Kiprusoff|05-06|CGY|74|1951|.923|8.11|
|5|Dominik Hasek|96-97|BUF|67|2177|.930|8.04|
|6|Patrick Roy|91-92|MON|67|1806|.914|7.77|
|7|Ed Belfour|90-91|CHI|74|1883|.910|7.67|
|8|Dominik Hasek|93-94|BUF|58|1552|.930|7.62|
|9|Ed Belfour|92-93|CHI|71|1880|.906|7.43|
|10|Pete Peeters|82-83|BOS|62|1482|.904|7.19|



Table 11: Bottom 5 TIWORP from 1982-83 through 2009-10 using a separate multiple regression for each season (Table 1) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|TIWORP|
|---|---|---|---|---|---|---|---|
|2272|Jeff Hackett|92-93|SJS|36|1220|.856|_−_4.97|
|2273|Dan Cloutier|06-07|LAK|24|608|.860|_−_5.15|
|2274|Brian Hayward|85-86|WPG|52|1373|.842|_−_6.05|
|2275|Craig Billington|93-94|OTT|63|1801|.859|_−_7.78|
|2276|P. Sidorkiewicz|92-93|OTT|64|1737|.856|_−_8.41|



12 

Shea and Baker: Calculating WORP for NHL Goaltenders 

Table 12: Top 5 TIWORP _−_ WORP (∆) from 1982-83 through 2009-10 using a separate multiple regression for each season (Table 1) 

|Rank|Goalie|Seas.|Team|GP|SOG|SV%|∆|
|---|---|---|---|---|---|---|---|
|1|Pete Peeters|82-83|BOS|62|1482|.904|1.36|
|2|Martin Brodeur|96-97|NJD|67|1633|.927|1.02|
|3|Jeff Hackett|92-93|SJS|36|1220|.856|1.01|
|4|M. Kiprusoff|05-06|CGY|74|1951|.923|.93|
|5|Ed Belfour|92-93|CHI|71|1880|.906|.83|



### **7 On the Choice of a Replacement Player** 

We calculated the wins over replacement for NHL goaltenders where the replacement player produced a save percentage equal to the league’s save percentage for the given season. This was not the only choice we could have made for a replacement. We believe the hypothetical replacement should satisfy certain conditions. First, WORP should be computed using the same replacement for all goalies in a given season. Second, the replacement should be based on actual statistics from the given season. Furthermore, these statistics should be representative of the typical goalie production for that season. So, for example, using the best goalie’s production (or the worst) on a given season as the replacement would not be appropriate. By calculating WORP based on a replacement that is representative of the typical goalie production in each respective season, we can compare WORP values of goalies from different seasons without converting the numbers. This is something that cannot be done with traditional metrics, such as save percentage. Table 2 shows a general trend upward in average save percentage by season. A save percentage of .890 would have been above average in the early 1980’s, but below average in recent years. Our choice of a replacement based on the league save percentage for a given season meets these conditions that we believe are important for any choice of a replacement in a calculation like ours. 

We were motivated to define WORP, in part, by Woolner’s definition of VORP for baseball players. According to Keri (2006) “[VORP], developed by Baseball Prospectus’s Keith Woolner, shows the number of runs a player contributes beyond what a replacement-level player (defined as a fringe major leaguer readily available off the waiver wire) at the same position would contribute if given the same percentage of team plate appearances.” The fringe major leaguer tends to be the thirtieth (or so) best replacement in a given season. We could have similarly attempted to approximate the thirtieth or so best goaltender in each season. This can be accomplished by multiplying the league save percentage by some coefficient (.90, for example). In other words, we could have chosen the replacement to 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 

be a player that produced a save percentage of 90% of the league save percentage in each season. According to Neyer (2007), “Woolner defines a replacement hitter as being roughly 80 percent as good as an average major league hitter at his position (the number actually varies somewhat, depending on the position).” 

In the NHL, the actual ability of the likely replacement of a given goaltender varies a great deal. One might expect replacements to perform below the league save percentage. However, there are examples where this would likely not be the case. For example, in 2009-10, the Boston Bruins used back-up goalie Tuukka Rask in 45 games, and in those games Rask produced league bests with a 1.97 goals against average and a .931 save percentage. Rask still (in 2011) sits primarily as the back-up to starter Tim Thomas. If Rask were called on to replace Thomas, he would likely out produce the league save percentage. 

The great variability in actual replacements in the NHL makes justifying (statistically) a coefficient such as .90 (to multiply the league save percentage by) quite difficult. Without sound statistical justification, the choice of coefficient can be perceived as arbitrary. A seemingly arbitrary choice of coefficient can make the end calculation of WORP more difficult to interpret. 

We chose to make our replacement goaltender representative of the average goaltender production in a given season. Again, we emphasize that this is not the only possible choice. One could run the calculation of WORP using our formulas only replacing the league save percentage with .90 times the league save percentage (or any other percentage of the league save percentage). One could also use our formulas to compare one goalie to another (such as a current starter to his back-up) by plugging in an appropriate save percentage (perhaps the back-up’s career save percentage) for the league save percentage. See Remark 1 in the next section for more discussion on this idea. We also leave open the possibility that there is some yet to be discovered formula for a replacement save percentage that would generate interesting results when substituted for league save percentage in our formulas. 

In summary, we believe our choice of a replacement meets several important criteria for any choice of a replacement in a calculation of this sort. By choosing the league save percentage as the production level of the replacement, we have a replacement that is representative of the typical goalie production in that season. With the choice of the league save percentage, as opposed to some (relatively arbitrary) percentage of the league save percentage, we have a final WORP calculation that we believe is particularly easy to interpret. Still, we leave open the possibility that other choices of a replacement will yield interesting results. We encourage others to explore this possibility. 

14 

Shea and Baker: Calculating WORP for NHL Goaltenders 

### **8 Remarks and Future Directions** 

1. Our method for calculating the value in wins of a given goalie to his team over the average replacement goalie can also be used to project how many wins can be gained or lost by replacing a given goalie on a team with another goalie. An NHL team might be considering signing a high priced free agent to start in net. Using our formula, they could project by how many wins their team would improve with the free agent in net over their current options. One could also run a similar comparison at the NHL trade deadline. 

2. Here we focus on goalies. The natural next step would be to calculate WORP for skaters. Since the goalie position is far different from any other position on the ice, our formulas do not translate to skaters. Skaters contribute both offensively and defensively. We predict that more complex methods than were used here will be necessary to calculate a meaningful WORP for skaters. 

3. We see no reason why our methods would not translate to leagues outside of the NHL. For example, one could run the same study in the American Hockey League. 

4. Team independent WORP may be modified to take into account shot quality. To do this, we envision computing a team independent save percentage that takes into account the quality of shots a goalie has faced in a given season. In this way, a goalie who has seen a higher than average percentage of high quality shots will have a higher team independent save percentage than save percentage. We would then repeat our work in the previous sections only replacing save percentage with team independent save percentage. Krzywicki (2010) has done a nice job analyzing shot quality in the NHL in 2009-2010, but there is a limited history of NHL shot quality statistics. We did not believe that there are enough data or enough analysis on the data pertaining to shot quality to determine a formula for team independent save percentage. In time, there will be enough data and, through the work of Kryzwicki and others, one could calculate an adjusted WORP that factors in shot quality. 

### **References** 

Cochran, J. J. and R. Blackstock (2009): “Pythagoras and the national hockey league,” _Journal of Quantitative Analysis in Sports_ , Vol. 5: Iss. 2, Article 11. James, B. (1980): _Baseball Abstract_ , self-published. 

James, B. (1988): _The Bill James Baseball Abstract_ , Ballantine Books. 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

Keri, J. (2006): “Understanding and measuring replacement level,” in J. Keri, ed., _Baseball Between the Numbers: Why Everything You Know About the Game is Wrong_ , Basic Books: New York. 

Krzywicki, K. (2010): “Nhl shot quality 2009-2010,” 

http://hockeyanalytics.com/2010/10/nhl-shot-quality-2010/. 

Neyer, R. (2007): “The world according to vorp,” 

http://sports.espn.go.com/mlb/hotstove06/columns/story?columnist=neyer rob&id=2751842. 

- NHL.com (2010): “Rookie of the year? wings goaltender howard ranks among top 10 in 3 categories,” http://www.nhl.com/ice/news.htm?id=522773. 

- Woolner, K. (2002): “Understanding and measuring replacement level,” in _Joe Sheehan ed., Baseball Prospectus 2002_ , Brassey’s Inc: Dulles, VA, 55–66. 

16 


