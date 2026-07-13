<!-- source: 2012 Experience and Winning in the NBA.pdf -->

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



# **Experience and Winning in the National Basketball Association** 

James Tarlow University of Oregon Eugene, Oregon, USA, 97401 Email: jamesmtarlow@gmail.com 

## **Abstract** 

When commenting on the ability of NBA teams it is commonplace to cite a young team’s inexperience as a negative and the experience of a veteran laden team as a positive. However, there is a lack of empirical investigation into the effects of player or coach experience on team performance.  In this paper I analyze the effects of player, coach, and team experience levels on franchise postseason wins.  This study uses hand gathered panel data detailing the 804 NBA seasons played by 30 NBA franchises between 1979 and 2008.  I find that increased postseason player experience increases a team’s ability to make the playoffs while not increasing their ability to win in the playoffs.  A coach’s postseason experience does contribute to a team’s ability to win in the playoffs.  I also find that teammate experience, a proxy variable for team chemistry, significantly increases a team’s postseason success.  I also offer plausible explanations for these effects.  These results should be of interest to team executives, league analysts, and NBA commentators as it provides quantitative insight to an issue that has previously been based almost entirely on conjecture. 

1 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **1   Introduction** 

There is a lack of empirical investigation into the effect of experience on winning in the literature of sports economics and sports analytics.  As a result, the valuation of experience in the National Basketball Association (NBA) has been relegated to the assumption that experience is always better than inexperience.  This assumption has been applied liberally and developed into an attitude that experience has a causal relationship with winning and losing. 

This is never expressed more often in the NBA than during the playoffs.  Teams composed of relatively young players are criticized for their lack of NBA experience.  Teams made of players new to the playoffs are questioned by comments such as, “They’ve never been in this position before…”  Lesser experienced coaches receive similar comments as well.  On the other hand, highly experienced players and coaches are referred to as “savvy veterans.”  When an inexperienced team wins a series over a veteran laden team, the criticism is not corrected, but only augmented with positive attributes like “young legs” or athleticism.  These valuations of experience are all offered as self-evident by the empirically unsupported, yet accepted assumption that experience has a causal relationship with winning. 

It is also interesting that aggregate experience between teammates is rarely mentioned as a contributing factor of success.  Aggregate experience might be considered a metric for experiential team chemistry.  In the game of basketball a player’s ability to make good decisions during play is directly dependent upon his knowledge of each of his teammate’s abilities, limitations, and tendencies. For instance, such knowledge allows a player to know where on the floor his teammates are most efficient scorers, where they usually get beat on the defensive end, when they are likely to backdoor their man and cut to the basket, whether the center can handle a bounce pass in the open court, etc. Longtime teammates often only need eye contact to communicate during a game.  These things improve the efficiency of a team’s play.  Players acquire this teammate information through experience playing with one another and, while the rosters of the NBA change each year, some change more than others.  Are teams that remain intact, thereby allowing their players to develop this knowledge, more successful in the postseason than those that do not? 

In this paper I present an econometric study of the NBA from 1979 to 2008 in order to investigate the effects of coach, player, and team experience levels on franchise postseason wins.  The objective of this study is to bring specificity and value to the relationship between experience and winning in the postseason.  In other words, the goal is to take the first step in determining which, if any, forms of experience show evidence of a causal relationship to winning and to provide an estimate of that relationship in terms of postseason wins. 

I expect to find player NBA experience to be correlated with postseason success because it takes players time to adjust to professional play.  I expect the behavior of teams to follow the same pattern.  However, I do not expect to find any evidence that player postseason experience helps a team to win in the postseason.  Players in the NBA have played at the highest levels of competition for their age group their entire lives.  Having probably been the stars of their high school and college teams they have been relied on in high pressure situations their entire amateur careers.  They reached the NBA because they have continually performed well in high pressure circumstances. It would be surprising if teams composed of such players suddenly performed differently when playing under the pressure of the NBA. However, comments directed at coaches frequently focus on postseason experience because of the strategic maneuvering required by the playoffs. In the postseason a coach’s team faces the same opponent up to seven times in a row, compared to the regular season where they face a new opponent each game.  Coaches have compared the difference in strategy between the playoffs and the regular season to that of chess and checkers.  Coaching in the playoffs may or may 

2 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



not be a skill acquired specifically through postseason coaching experience.  I also expect to find evidence that team experience has a strong relationship with postseason wins. 

## **2   Data** 

This econometric study uses panel data detailing 804 NBA seasons played by thirty NBA franchises between the 1979-80 and 2008-09 seasons. 

All experience variables were hand collected from Basketballreference.com and compiled from a sample of 4,020 players [1]. 

Variables referring to “players” are calculated from the five players receiving the most playing time in minutes during the regular season for a given team during a given season.  Such variables are not calculated based on the entire roster or all players receiving an established baseline of playing time. 

Player experience data is divided into NBA experience and postseason experience. **Player NBA experience** is defined as the average number of years played in the NBA per player and **player postseason experience** is defined as the average number of postseason games played per player. Separating player experience into these two groups was done with the intent of isolating the effects of season and postseason experience by controlling for each of them.  Furthermore, players on each team are not homogenous in experience level.  There are teams composed mostly of players new to the league, teams composed of older veterans of the league, and teams composed of both.  In order to control for the heterogeneity of player experience within each team the player experience variables **variance of player NBA experience** and **variance of player playoff experience** are included. 

Coaching experience data is also separated into NBA experience and postseason experience, however, also included as coaching experience variables are coach’s winning percentage for postseason games, coach tenure, and a coach postseason experience dummy variable. **Coach NBA experience** is defined as years spent as a head coach in the NBA. **Coach postseason experience** is defined as number of postseason games coached as a head coach. **Coach postseason win %** is defined as (postseason games won) / (postseason games coached). **Coach tenure** is defined as the number of previous years spent as the head coach of the team in question. **Coach postseason dummy** is 1 if the coach has postseason coaching experience and is 0 if the coach does not have postseason coaching experience. 

New players to a team are represented in these data as either a rookie or a veteran new to the team.  The variable **rookies started** is defined as the number of players among the top five regular season minute getters for a given team and season who are in the first season of their NBA career. **New veterans** is defined as the number of players among the top five regular season minute getters for a given team and season who have at least one season of prior NBA experience. 

This study includes experiential team chemistry as an explanatory variable that is quantified by the years of shared NBA experience between teammates. **Chemistry** then is defined as the number of years the five players playing the most minutes during the regular season have been on their current team with one another.  Each point in a team’s chemistry rating represents one year of shared experience between two players on their current team. 

All data are relevant only to the time prior to a given data point’s season.  For example, the number of postseason games coached included in the data point for a team’s 1991-92 season is the sum of postseason games that their head coach has coached in his career previous to that season. 

Table 1, in the appendix, lists the variables previously defined along with their respective sample means and standard deviations. 

3 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **3   Estimation Results** 

Table 2 lists the estimation results for the three models from which I derive my main analysis.  All regressions use multiple least squares regression and include a lagged dependent variable. Teams performing well the previous year are likely to perform well the following year.  Including a lagged dependent variable controls for this persistence.  Regression 1 estimates the effects of independent variables on postseason wins while regression 2 estimates the effects for regular season wins.  Regression 3 is a model of postseason wins restricted to a sample of teams with one or more postseason wins.  The intent of the restricted model is to focus on the variation among playoff teams rather than all NBA teams. 

**<u>Table 2.</u>** 

|**Independent Variable**<br>|**1.(Postseason)**|**2.(Season)**<br>|**3.(Restricted)**|
|---|---|---|---|
|Constant|-1.26(.96)|15.08(2.70)|.32(.87)|
|Player NBA Experience|.61(.34)*|1.95(.94)**|.85(.64)|
|Player NBA Experience Squared|-.07(.03)**|-.17(.08)**|-.08(.05)|
|Variance of Player NBA Experience|.01(.03)|-.16(.07)**|.06(.04)|
|Player Postseason Experience|.04(.02)***|.07(.04)**|.02(.02)|
|Variance of Player Postseason|-.0003(.0002)|.0008(.0005)|-.0003(.0003)|
|Experience||||
|Chemistry|.06(.02)**|.08(.06)|.06(.03)*|
|Chemistry Including Coach|-|-|-|
|Coach NBA Experience|-.08(.04)**|.05(.09)|-.11(.06)**|
|Coach Tenure|-.01(.05)|.17(.14)|-.07(.09)|
|Coach Postseason Experience|<br>.008(.005)*|<br>-.01(.01)|<br>.01(.007)**|
|Coach Postseason Win %|2.08(.69)***|7.00(1.82)***|1.39(1.22)|
|Coach Postseason Dummy<br>|-|-<br>|-|
|New Veterans|.026(.19)|-.534(.51)|.21(.33)|
|Rookies Started|-.35(.3)|-1.32(.81)|-.62(.60)|
|Postseason Games Won Previous Year|.27(.05)***||.19(.07)***|
|Season Games Won Previous Year||.43(.04)***||
|R^2|.35|.498|.24|
|Total Panel Observations<br>|774|774<br>|382|



**Notes: Numerical results are reported for variables as: Regression Coefficient(Standard Error) Statistical significance at the 10%, 5%, and 1% levels are denoted by *, **, and *** respectively.** 

### **3.1   Player Experience** 

Regression 1 of Table 2 estimates player NBA experience to have a quadratic correlation to postseason wins significant at the 10% level.  A quadratic relationship is intuitive considering the skill of a basketball player rises initially, peaks at some point, and eventually falls with age until retirement. This model estimates that the effectiveness of a team follows the same pattern as that of its individual 

4 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



players.  The estimated coefficients for player NBA experience and player NBA experience squared are .61 and -.07 respectively.  Interpreting these estimates indicates an ideal average player NBA experience level for a team to be 4.33 seasons played per player.  In other words, the model estimates that 4.33 seasons played per player is the level at which a team’s effectiveness peaks just as an individual player would peak.  The sample mean for this variable is 4.9 years per player.  It appears that, on average, NBA franchises operate near this optimum level. 

However, more important is whether being above or below this level would yield a large disparity in postseason wins.  Holding other explanatory variables constant, the optimum level of 4.33 years per player is estimated to have an effect of 1.31 postseason games won from player NBA experience.  A team below this optimum level by one standard deviation would estimate an effect of 1.06 postseason games won, a difference of about .25 postseason games.  This effect could be considered large enough to support citing a lack of team experience as a weakness for a team, but being statistically significant at just the 10% level points to the ambiguity of this variable rather than the strength of it. 

Player postseason experience on the other hand is significant at the 1% level and yields a coefficient of .04 providing initial evidence supporting the conclusion that postseason experience leads to winning in the postseason.  A coefficient of .04 may seem small, but considering that the sample mean of player postseason experience is 26.31 postseason games played per player, the effect of this variable is 1.05 postseason games won.  Furthermore, the standard deviation of this variable is 23.13, meaning the variance between teams in postseason experience is large.  This model estimates that teams one standard deviation below the mean (3.18 postseason games played per player) can expect to win about 1.76 _fewer_ postseason games than teams one standard deviation above the mean (49.44 games per player).  1.76 games is a large effect and seems unreasonably high. 

A closer look, through the lens of regression 3, reveals that player postseason experience becomes statistically insignificant when the sample is restricted to include only teams winning one or more postseason games for a given year.  This is an indication that player postseason experience may get a team into the playoffs, thus providing the _opportunity_ to win postseason games, while not increasing their _ability_ to win postseason games.  The coefficient in regression 1 can be seen as a byproduct of teams making the playoffs.  Teams that have an opportunity to win postseason games will inevitably win more than those that do not.  This conclusion is further supported considering regression 2, the model employing regular season wins as the dependent variable.  Regression 2 estimates player postseason experience to be significant at the 5% level with the variable’s mean value correlated with 1.93 regular season wins. Regressions 2 and 3 both reveal the bigger picture that while player postseason experience may be correlated with entry into the postseason, it is not a cause of winning once in the postseason. 

### **3.2   Coaching Experience** 

Multiple measures of coaching experience are initially statistically significant when regressed against postseason wins, however, not all can confidently be considered important to winning in the postseason. 

Coach NBA experience is statistically significant at the 5% level when regressed against postseason wins in both regression 1 and regression 2.  The coefficient in regression 1 is -.08, surprisingly showing coaches NBA experience to be negatively correlated with postseason wins.  This negative correlation is the result of controlling for coach’s postseason games coached.  When postseason games coached are held constant while regular seasons coached increases, it would translate to a coach achieving less postseason games per season.  Considering the only way to increase postseason games coached per year is to win postseason games, having less postseason games 

5 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



coached per season means there were less postseason wins per season.  By controlling for coach postseason experience the coefficient for coach NBA experience yields a negative regression coefficient. 

However, when the coach postseason dummy variable replaces coach postseason experience and coach postseason win % from regression 1, coach NBA experience becomes statistically insignificant rather than maintaining a statistically significant negative effect.  This change is because the number of postseason games coached is no longer held constant while years coached varies.  This result suggests that a coach’s general NBA experience is not causally related to winning in the postseason. 

While the coach postseason dummy variable discredits coach’s NBA experience as a contributor to winning in the postseason, it reaffirms the importance of a coach’s postseason experience.  The coefficient for coach postseason dummy is estimated to be .67 and is significant at the 5% level.  Intuitively, this means that a team who has a head coach with postseason experience is estimated to win .67 more postseason games than if the team were headed by a coach without postseason experience.  Furthermore, regression 1 estimates the regression coefficient of coach postseason experience to be .014 postseason games won per postseason game coached.  The sample mean being 43.57 postseason games coached yields .61 postseason wins due to coach postseason experience. 

While regular season coaching experience does not seem to have much importance to postseason success, there is evidence that having postseason coaching experience, as well as the amount of that experience, does contribute to winning in the postseason.  This makes sense considering the NBA is the only major basketball league in which playoffs are played in a series format where opponents play one another up to seven times in a row.  The uniqueness of this tournament format to basketball would also make experience coaching within it unique, and plausibly valuable. 

### **3.3   Experiential Team Chemistry** 

Chemistry is statistically significant when regressed against postseason wins in regressions 1 and 3.  Regression 1 estimates chemistry’s coefficient to be .06 at 5% statistical significance.  Meaning each year of shared experience between two teammates is correlated with .06 postseason wins.  Again, this effect may seem small, but the sample mean for team chemistry is 12.73 with a standard deviation of 10.75.  The average team is estimated to win .74 postseason games due to their team chemistry.  A team composed of players who have very little history of playing with one another, one standard deviation below the sample mean, would have a chemistry rating of approximately 2 and could estimate .12 postseason wins from this effect.  However, the distribution of this variable is skewed to the right and it is not unusual for teams to have chemistry ratings above 30.  A team composed of longtime teammates who have 30 seasons of shared experience are correlated to win 1.74 postseason games, a difference of 1.62 postseason wins compared to the inexperienced team. 

Regression 3 supports this estimate after being corrected for multicollinearity.  Chemistry, as defined in this study, is strongly correlated with two other variables.  Chemistry is correlated with the dependent variables new veterans and rookies started.  Chemistry has an approximate linear relationship with these two variables because introducing a new player to a roster, either a rookie or a new veteran, will by definition decrease that team’s chemistry rating (the exception being when the new player replaces a player who was new the previous year).  When these two variables are included in the model, and therefore held constant, their linear relationship with chemistry confounds its effect because holding them constant limits the variation of chemistry.  In the unrestricted model of regression 1 the sample size was large enough that multicollinearity did not pose a problem. However, 

6 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



when the sample is restricted in regression 3 it reduces the number of observations by 51% and multicollinearity becomes an issue.  The coefficients of these two variables are statistically insignificant in regression 1 and when withheld from regression 3, chemistry has an estimated coefficient of .056 significant at the 5% level. The original estimate from regression 1 is reduced by 6.7% and retains its statistical significance, strengthening evidence of chemistry’s causal relation to postseason wins. 

Regression 2 reports chemistry to be statistically insignificant when regressed against regular season wins.  This is because the variable, intended to represent five players playing together during games, inadequately describes an 82 game regular season where lineups are commonly in flux.  The five players on the court at any given time vary during the regular season as coaches experiment with different lineups and distributions of playing time.  Injuries also contribute to this as players have less incentive to play through their injuries during the regular season than they do in the postseason.  The variability of lineups in the regular season means that the five players used in calculation of the chemistry variable spend less time on the court together during regular season games.  This leads to chemistry’s lack of statistical significance when regressed against regular season wins in regression 2. 

The chemistry variable is also impactful considering its potential to change between seasons. A team that leaves their roster alone, allowing their players to gain another year of teammate experience, will see their chemistry rise by 10 years of teammate experience from the previous season. Using the more conservative estimate, this increase would correlate with .56 more wins in the postseason than their previous season.  On the other hand, teams that insert new players to their rosters can lose far more than the 10 years of teammate experience gained by leaving it intact.  The 1999 Utah Jazz for example, was a team that had remained intact and had a chemistry rating of 60. They won four playoff games that year and during the offseason they replaced Jeff Hornacek and Howard Eisley with John Starks and Donyell Marshall, who were acquired during the off-season. Making the transaction dropped the Jazz’s chemistry rating from 60 to 29.  The model would estimate this drop, in terms of chemistry alone, to reduce their postseason wins by 1.7 games.  The following season the Jazz managed to win just two playoff games, losing in the first round.  This model is not predictive and does not indicate that the Jazz should not have acquired Starks and Marshall.  Part of the intention of this study was to estimate the impact of these forms of experience and this example is offered in order to illustrate that potential impact. 

The potential impact of this chemistry variable could be understood as a disincentive to make transactions.  A player's worth to a team includes the knowledge he has accumulated about his teammates as well as his teammates’ about him.  This study indicates the new player’s production and the efficiency of the team is likely to be diminished simply because they are unfamiliar with their teammates.  It is most relevant when a prospective new player would be acquired as a short term investment because the teammate experience lost by making the transaction would not be recouped. 

However, this study does not offer information nearly specific enough to make such analysis possible.  Further research is needed to do so.  Such research would focus on team and player production when a player enters a new team.  It is reasonable to hypothesize that experiential chemistry is subject to diminishing returns.  By this I mean that the first year teammates play together would produce more efficacy than their tenth year playing together.  The variable also might have a disproportionate effect between player positions.  It could be that knowing one’s teammates has a greater impact as a point guard than as a center. 

There are several weaknesses to this variable that are worth discussing.  First, chemistry is a proxy.  It in no way represents the way two or more players might naturally work well together on the court, which is the usual way that one thinks about a team’s chemistry.  The variable simply quantifies the number of years the five players receiving the most minutes during the regular season have played with one another in order to quantify teammate knowledge within a basketball team.   That being said, 

7 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



this proxy may not capture the entire effect that teammate experience actually has on postseason success or it may overestimate it.  However, there is considerable evidence that it plays a role in postseason wins.  Also a potential drawback to this variable is that it is regressed on postseason wins when the variable is calculated from regular season minutes played.  It would have been more accurate to use postseason minutes played as the filter to decide which five players would be used to calculate this variable.  It was an oversight I made while gathering data.  However, regular season distribution of minutes closely matches that of playoff minutes as coaches put their best players on the floor as often as they can whether it is a regular season or a playoff game.  What does go unrecognized by this variable are injuries that prevented players from playing in the playoffs, but this is a minor inaccuracy considering both the sample size of the 4,020 players included in the calculation of this variable and the rarity of such injuries. 

## **4   Conclusion** 

In light of these results, I would respond to comments aired each year in the NBA with three statements.  First, the most common criticism is of the inexperience of younger teams and this study does not support this conclusion, regardless of whether their NBA experience or playoff experience is the topic of discussion.  Second, the number of years of experience a coach has in the NBA is an irrelevant figure.  It is a coach’s playoff experience, not the length of their NBA coaching career, which is relevant to winning in the postseason.  Finally, it suggests that what should be assigned more attention is the value associated with keeping teammates together. 

Indirectly this study also takes the first step in quantifying a disincentive to make transactions.  At the end of each season the teams that achieved their goals have the luxury of satisfaction.  For everyone else their instinct generally says to try something new, however, these results suggest that sometimes the right decision is to do nothing in order to give the current team the time to improve as a unit.  More research is needed before “sometimes” in the previous sentence can be specified. 

## **5   Acknowledgments** 

I would like to thank Jeremy Piger for valuable input to this paper.  I would also like to thank the owners of the webpage basketball-reference.com for making their data publicly available. 

## **6   References** 

[1] _Basketball-Reference_ . (2010). http://www.basketball-reference.com/ 

[2] Berri, David, Martin Schmidt and Stacey Brook. _The Wages of Wins._ Stanford: Stanford University Press, 2006. Print. 

[3] Berri, David J., Martin B. Schmidt, and Stacey L. Brook. ”Stars at the Gate: The Impact of Star Power on NBA Gate Revenues.“ _Journal of Sports Economics,_ Feb 2004; vol. 5: pp 33-50. Sage Publications. 27 August, 2010. 

[4] Berri, David, Brian P. Soebbing, Joseph Price, and Brad R. Humphreys. “Tournament Incentives, League Policy, and NBA Team Performance Revisited.” _Journal of Sports Economics_ Vol. 11 (2010): 117135. _Sage Publications._ Web. 27 August, 2010. 

[5] Borick, Christopher P., Paul B. Bursik, Kevin Gs. Quinn, and Lisa Raethz. “Do New Digs Mean more Wins?: The Relationship between a New Venue and a Professional Sports Team’s Competitive 

8 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



Success.” _Journal of Sports Economics_ Vol. 4 No. 3 (2003): 167-182. _Sage Publications_ . Web. 27 August, 2010. 

[6] Bougheas, Spiros, and Paul Downward. “The Economics of Professional Sports Leagues: Some Insights on the Reform of Transfer Markets.” _Journal of Sports Economics_ Vol. 4 (2003): 87-107. _Sage Publications_ . 2 September, 2010. 

[7] Coates, Dennis, and Brad R. Humphreys. “The Economic Impact of Postseason Play in Professional Sports.” _Journal of Sports Economics_ Vol. 3 (2002): 291-299. _Sage Publications_ . Web. 27 August, 2010. 

[8] John Fizel, Elizabeth Gustafson and Lawrence Hadley, ed. _Sports Economics: Current Research_ . London: Praeger, 1999. Print. 

[9] Fizel, John, ed. _Handbook of Sports Economics Research._ New York: M.E. Sharp, 2006, Print. [10] Fizel, John, Elizabeth Gustafson and Lawrence Hadley, ed. _Sports Economics: Current Research_ . London: Praeger, 1999. Print. 

[11] Fort, Rodney and James Quirk. “Owner Objectives and Competitive Balance.” _Journal of Sports Economics_ Vol. 5 (2004): 20-32. _Sage Publications._ Web. 2 September 2010. 

[12] Fort, Rodney and Joel Maxcy. “Competitive Balance in Sports Leagues: An Introduction.” _Journal of Sports Economics_ , Vol. 4 (2003) 154-160. _Sage Publications._ Web. 18 January, 2010. 

[13] Frank A. Scott, James E. Long and Ken Somppi. “Salary Vs. Marginal Revenue Product Under Monopsony and Competition: The Case of Professional Basketball.” In _The Economics of Sport Vol. 1_ . Edited by Andrew Zimbalist, 429-439. Northhampton, MA.: Edward Elgar Publishing, 2001. 

[14] Groothuis, PaterA., James Richard Hill, and Timothy J. Perri. “Early Entry in the NBA Draft: The Influence of Unraveling, Human Capital, and Option Value.” _Journal of Sports Economics_ Vol. 8 (2007): 223-243. _Sage Publications._ Web. 27 August, 2010. 

[15] Hofler, Richard A. and James E. Payne. “Efficiency in the National Basketball Association: A Stochastic Frontier Approach with Panel Data.” _Managerial and Decision Economics_ , June 2006, v. 27, iss. 4, pp. 279-85. 

[16] Jerry A. Hausman and Gregory K. Leonard. “Superstars in the National Basketball Association: Economic Value and Policy.” In _The Economics of Sport Vol. 1_ . Edited by Andrew Zimbalist, 544-583. Northhampton, MA.: Edward Elgar Publishing, 2001. 

[17] Kesenne, Stefan. “Revenue Sharing and Competitive Balance in Professional Team Sports.” In _The Economics of Sport Vol 1._ Edited by Andrew Zimbalist, 182-195. Northhampton, MA.: Edward Elgar Publishing, 2001. 

[18] Leadley, John C., and Zenon X. Zygmont. “When is the Honeymoon Over?  National Basketball Association Attendance 1971-2000.” _Journal of Sports Economics_ Vol. 6 (2005): 203-221. _Sage Publications_ . Web. 27 August, 2010 

[19] Leeds, Michael, Peter von Allmen. _The Economics of Sports_ . Pearson Inc. 2005. Print. 

[20] Michaelides, Marios. “A New Test of Compensating Differences: Evidence on the Importance of Unovserved Heterogeneity.” _Journal of Sports Economics_ Vol. 11 (2010): 475-495. _Sage Publications._ Web. 27 August, 2010. 

[21] Mohamed El-Hodiri and James Quirk. “An Economic Model of a Professional Sports League.” In _The Economics of Sport Vol. 1_ , Edited by Andrew Zimbalist, 80-98. Northhampton, MA.: Edward Elgar Publishing, 2001. 

[22] National Basketball Association.  www.Nba.com 

[23] Rottenberg, Simon. “The Baseball Players’ Labor Market.” In _The Economics of Sport Vol 1_ . Edited by Andrew Zimbalist, 3-20. Northhampton, MA.: Edward Elgar Publishing, 2001. Print. 

[24] Sanderson, Allen R. “The Many Dimensions of Competitive Balance” _Journal of Sports Economics_ Vol. 3 (2002): 204-228. 2002. _Sage Publications_ . Web. 18 January, 2010. 

9 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



[25] Vrooman, John. “A General Theory of Professional Sports Leagues” In _The Economics of Sport Vol. 1_ . Edited by Andrew Zimbalist, 152-172. Northhampton, MA.: Edward Elgar Publishing, 2001. 

[26] Vrooman, John. “Theory of the Perfect Game: Competitive Balance in Monopoly Sports Leagues.” _Review of Industrial Organization_ , February 2009, v. 34, iss. 1, pp. 5-44. 

[27] Yilmaz, Mustafa R., and Sangit Chatterjee. “Patters of NBA Team Perforance from 1950 to 1998.” _Journal of Applied Statistics_ , July 2000, v. 27, iss. 5, pp. 555-66. 

[28] Zimbalist, Andrew. “Reflections on Salary Shares and Salary Caps.” _Journal of Sports Economics_ Vol. 11 (2010): 17-28. _Sage Publications_ . Web. 18 January, 2010. 

[29] Zimbalist, Andrew. “Competitive Balance Conundrums: Response to Fort and Maxcy’s Comment.” _Journal of Sports Economics_ , Vol. 4 (2003): 161-163. _Sage Publications_ . Web. 18 January, 2010. 

## **7   Appendix** 

**<u>Table 1. Variable Statistics</u>** 

|**Variable name**|**Mean(Standard Deviation)**|
|---|---|
|Player Experience|4.9 (1.91)|
|Player Experience Squared|27.69 (20.85)|
|Variance Player Experience|9.78 (7.53)|
|Player Postseason Experience|26.31 (23.13)|
|Variance Player Postseason Experience|692.26 (1085.97)|
|Player Postseason Experience Dummy|3.82 (1.41)|
|Chemistry|12.73 (10.15)|
|Coach Experience|6.67 (6.46)|
|Coach Playoff Win %|0.44 (0.16)|
|Coach Playoff Experience|43.57 (53.99)|
|Coach Tenure|2.16 (2.86)|
|New Veterans|0.83 (.95)|
|Rookies Started|0.34 (.59)|
|Post Games Won|2.64 (4.11)|



10 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



|Season Wins|41 (12.72)|
|---|---|



11 


