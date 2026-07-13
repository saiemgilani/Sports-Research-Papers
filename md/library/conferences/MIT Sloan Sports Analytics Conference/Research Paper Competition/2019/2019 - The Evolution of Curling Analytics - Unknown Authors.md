<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2019/2019 - The Evolution of Curling Analytics - Unknown Authors.pdf -->



# **The Evolution of Curling Analytics** 

Kevin Palmer, Gerry Geurts and Jason Gunnlaugson CurlingZone Paper ID 13281 

## **1. Introduction** 

Simple in concept but actually quite complex, curling is often called “chess on ice”.  Like innings in baseball, curling takes place over “ends” (8 or 10).  Each end comprises of 16 shots, with each shot a decision point in the contest.  In a 10-end game the captain of each team, known as the “skip”, makes 80 decisions.  This makes for 160 decisions between two teams.  In many cases the decision is universally accepted, but very often there can be disagreement on the correct called shot and one poor choice can turn the course of the game. Because of the way curling is played, each decision can be examined using analytics.  What is the chance my teammate will successfully execute this shot? What will my opponent likely do next?  What are the conditions of the ice and how will that effect our chance of making this shot and each subsequent shot?  Based on the outcome of my decision, what is my probability of winning the game? 

Given the shot-by-shot structure of curling, many would consider statistical analysis as both desired and perhaps necessary for success.  This is traditionally not the case.  Curling is a game steeped in tradition, where parents and grandparents pass on experience to the next generation.  In many instances, some of the best teams in the world stop and consider several options (while a chess timer is ticking away) when pre-planning could help clarify the correct decision much faster. Sometimes teams may make a clear strategic mistake because they simply don’t know the numbers and rely instead on gut or feel.  Teams can struggle to properly evaluate their own level of play while also failing to recognize opportunities to out maneuver opponents because they lack the information or incorrectly interpret small sample sizes from their own visual analysis. 

In this paper we will present the current information available to teams and how these datasets can be applied to analyze their own play, prepare for the opposition and evaluate in-game decision making.  We will conclude with considerations on possible next stages for curling analytics and what is needed to achieve these goals. 

## **2. Datasets** 

The data available for analyzing curling consists of game results (linescores) and shooting percentages. Linescores show the score each end, who held hammer (last shot of the end) in each end played, and the final score.  Shooting percentages are calculated based on a manual judging procedure.  Traditional scoring was done with a 4-point system, with zero being a miss and 4 a fully made shot.  CurlingZone developed advanced scoring which uses a 0 to 5 scale and incorporates sweeping factor and degree of difficulty (Table 1) [1]. Because of the manual judging of shooting percentages and the varied level of skill from volunteers who provide these numbers, there is disagreement on the validity of these percentages from game to game or event to event.  Teams and 





2019 Research Papers Competition Presented by: 

1 



coaches can try to interpret data from larger results over many games but there remains skepticism in many camps on its true value. 



**Table 1** :  Linescore at the top shows: team that started the game with the last shot of the end indicated by the picture of the small hammer, beside Homan and under the “H”; the stone colour; the score by each team in each end (“1” through “8”, shown at the top of the table); and numbers below “T” showing the total score of 8-7, a win for Team Hasselborg.  Shooting percentages show each player, number of shots and total points awarded, difficulty and sweeping factor and then calculated shooting percentages. 

### **2.1 Influence of the Scoreboard** 

The scoreboard in most sports can influence decisions a team or individual athlete makes during a game.  Late in the 4<sup>th</sup> quarter, a football team down 33 to 28 scores a touchdown. Leading by 1 point, they will likely try for a two-point conversion to go up three (36-33), rather than attempting to kick a single point.  The scoreboard may have more influence on curling than perhaps any other sport.  Immediately beginning the game, a team that has hammer holds an advantage and will deploy a different strategy than their opponent, who does not have the last shot of the end.  General 





2019 Research Papers Competition Presented by: 

2 



curling theory is for a team with hammer to try and score two points (a deuce) with hammer and force their opponent to one point when they do not have hammer.  When able to do so teams with hammer will almost always blank an end (no score, with no stones situated in the rings after all 16 shots) to hold hammer into the next end, rather than score a single point.  It is, of course, correct to take one in the final end of a tie game.  There are other rare instances during the late stages where a team may choose to take one, we examine on such example in Section 4.2.3.  To blank an end rather than take a single point has been accepted in living memory for generations, even if it was considered bad sportsmanship by Scotland fans during the first men’s World Championship in 1959 (then known as the Scotch Cup).  We previously calculated weighted value of each end (data from season 2003 to 2014) [2] and it supported this strategy along with providing the relative value of each score across a full game. 

|**Weighted Value of End Score**|
|---|



**Table 2** : Weighted Value of End Score.  B is a blank.  A plus (+) number is team scoring points with hammer and minus (-) number is impact of stolen points, relative to team with hammer.  Results from the final end are not used in the calculations. 

How a team attempts to score two (or more) and force one, and the risk they are willing to take, can change as soon as the second end.  On average, the team with hammer will score two points approximately 1/3 of the time in the first end and their opponent’s win probability will drop considerably (see 2.2 below).  As a team jumps ahead they will deploy different strategies to limit their opponent’s chances to mount a comeback, or if behind they may take considerably more risk, attempting to score more than two or steal (score points without hammer).  A baseball team down 2-0 after the first inning will not differ their strategy the next inning.  A curling team down two points, however, will call different shots, and the positioning of stones can develop very differently than if they were down 1 point, tied or ahead.  Having this understanding, ends can be grouped together based on the score differential.  For example, how a team performs when down 1 point with hammer can be grouped across all similar ends played and compared against other teams to look for strengths or find leaks in their play.  Details for this type of analysis is found in Section 4.1.2. 

### **2.2 Win Probability** 

Curling linescores allow us to determine the Win Probability [3] based on the current score differential at the beginning of each end.  Table 3 and 4 show the current Win Probability charts for men and women.  The data is collected from major events such as World Championships, Olympic Games, Olympic Qualifying events, Canadian Championships, Grand Slams, and World Curling Tour events.  Sample sizes are included in the tables below the percentages (for example 1783-0 is 1783 instances of this situation).  Legend for Tables 3 and 4 are as follows: 

ENDS REMAIN is the number of ends remaining in the game. TIED is a tied game. HMR is a team with hammer STL is a team without hammer UP means the team is ahead DN means the team is behind 



2019 Research Papers Competition Presented by: 



3 



ONE POINT, TWO POINT and THREE POINT indicate the differential of the score in the game. 

For example, if a team has hammer and are down 2 points after the 5<sup>th</sup> end of an 8-end game, we reference the row with “3” ENDS REMAIN, look across that row under TWO POINT and DN HMR to find their Win Probability = 18.5% (men) or 20.2% (women). 



**Table 3** : Win Probability for men’s teams from 2014/15 to 2017/18 Seasons. [4] 





2019 Research Papers Competition Presented by: 



4 



**Table 4** : Win Probability for women’s teams from 2014/15 to 2017/18 Seasons. [4] 

### **2.3 Shot Tracking** 

The ability to track every curling shot will exponentially increase the amount of data available for analyzing the game.  A study was done by CurlingZone to record each early shot during play at the 2012 men’s World Championships in Basel, Switzerland.  It produced interesting results that challenged common thinking for the sport. Teams with hammer who attempted to place their stones fully behind centre guards early in ends gave up more steals and found it difficult to score more than one point.  When the team hid only part of the stone, their opponents did not counter with nearly as aggressive tactics. This goes against traditional thinking as the “best” shot is currently considered a draw fully hidden behind the guard. 

With each stone (also called rock) tracked to a position on the ice, we will better be able to analyze probable results from each successive shot selection and use the data to determine whether the outcome on each shot is towards a positive or negative scoring opportunity. When we put a series of shots together, we can track which decisions are optimal towards scoring in each end.  Using CurlingZone’s Tactical Analysis Program (TAP), we will be able to help teams improve their knowledge of the games much quicker and dispel many of the myths about curling strategy.  Data is currently being collected on a wider scale this season for this purpose. 

## **3. Team Statistics** 

Several statistics were developed by CurlingZone [6] to provide numerical analysis of team performance.  These statistics measure efficiencies with and without hammer.  Note that “score” or “scored” refers to a team getting points with hammer and “steal” or “stolen” refers to points taken by the team without hammer. 

Curling teams do not have a balanced season like other sports, with teams playing the same number of games against the same opponents.  Curling teams choose to enter certain events or qualify for others based on their rankings.  The Grand Slams include the highest level of competition in the world, but there are currently only 6 regular events each season (a 7<sup>th</sup> event similar to match-play golf incorporates a very different game strategy and statistical outcome).  All level of teams will compete in different events where the ranking and skill level of teams can vary considerably.  The result is teams will play varying amounts of games in a season (some barely 50, others over 100) against teams of wildly different skill levels.  This can result in a lower ranked team who rarely competes against higher competition having similar or even better statistics than a higher ranked team.  A comparison would be if all professional baseball teams had no regular season and Major League, Single-A, Double-A, and Triple-A teams all competed randomly throughout a year.  In Figures 1 through 6 we compare team statistics for Top 20 teams ranked by Order of Merit (world ranking system) points earned in the 2017/18 Season [5].  We’ve kept the analysis limited to this subset of teams to group teams with similar schedule and skill level, but it is still an imperfect match.  Order of Merit is a simple comparison between teams’ level of play.  We have been working on a strength of schedule calculation to consider each opponent a team plays over the season which is in development. 

### **3.1 Game Statistics** 



2019 Research Papers Competition Presented by: 



5 



Point Differential is the difference in points scored per game (PF/G) and subtract points scored against per game (PA/G).  Teams play events with both 8-end and 10-end games.  Curling also has the unique rule that allows a team to quit at any time and it is considered good etiquette to concede when you are well behind and have no reasonable chance to win the game.  Some televised events require a minimum number of ends, but for the most part teams will shake hands when victory is deemed to be out of reach.  This current statistic for Point Differential does not account for these situations. 



<!-- Start of picture text -->
(1)<br><!-- End of picture text -->



**Figure 1** : Point Differential Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

There is a significant advantage to the team that begins the game with hammer.  Over curling history, this has been determined by different means, more commonly a coin flip or pre-determined hammer for major events.  The hammer is now determined by a competition of draws to the button (centre of the rings) by each team before the game, similar to how opponents in darts will “Diddle for the Middle” or pool players will lag for the break.  A team’s ability to secure hammer (sometimes called Last Shot First End or LSFE) is determined as follows: 

(2) 

### **3.2 Team Statistics in Ends with Hammer** 

Hammer Efficiency (HE) 

The percentage of time a team takes 2 or more points with hammer, in ends which are scored. Includes all non-blank ends in which a team has hammer. 





2019 Research Papers Competition Presented by: 

6 





**Figure 2** : Hammer Efficiency for Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

Steal Defence (SD) 

Ability to limit the number of stolen ends. Calculated by number of ends stolen against divided by ends with hammer. Blank ends are included. Lower is better. 



**Figure 3** : Steal Defense for Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

Hammer Factor (HF) 

In general, how a team performs with hammer provides a clearer measure of relative performance than its performance without hammer.  Teams often have varied strategies that can result in similar winning percentages or rankings despite different ranges of HE or SD.  A highly ranked team with a lower HE may have a lower SD, indicating they put less rocks in play and take fewer chances.  By subtracting these results, we can produce a Hammer Factor [7] which provides another indicator of a team’s level of play. 

_𝐻𝐹=_ 







2019 Research Papers Competition Presented by: 

7 





**Figure 4** : Hammer Factor for Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

### **3.3 Team Statistics in Ends without Hammer** 

Force Efficiency (FE) - measures the ability of a team to force their opponent to one point. Calculated by number of ends in which the opponent took 1 point divided by all ends without hammer where the opponent scores. Stolen and blank ends are not included in the calculation. 



**Figure 5** : Force Efficiency for Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

Steal Efficiency (SE) - the percentage of ends a team steals one or more points. It's calculated by dividing ends stolen without hammer by the total ends played without hammer, Blank ends are included. 



<!-- Start of picture text -->
𝑆𝐸= (6)<br><!-- End of picture text -->





2019 Research Papers Competition Presented by: 

8 





**Figure 6** : Steal Efficiency for Top 20 Teams Order of Merit (OOM) 2017/18 Season. 

## **4. Analysis** 

Using the available datasets and various statistics teams can examine their own play, prepare for opponents and make better in game decisions.  We will look at how a team can analyze results in particular situations and use that information to plan for their competition.  We will also work through the analysis of in-game decisions using some common examples. 

### **4.1. Pre-game Analysis** 

Teams can use available datasets to examine their results and consider if their strategy or execution are impacting their win-loss record.  Game planning for opponents is improved from traditional visual and experiential analysis to using data to examine how an opponent performs in certain situations and consider what types of shots their opponents are most likely to attempt. 

### **4.1.1 First End** 

Reference to Table 3 earlier, a team that surrenders two points in the first end of an 8-end game will see their win probability drop from 37.7% before the end started to 24.8% with 7 ends remaining (41.6% to 27.1% for women, Table 4).  How a team performs in the first end of games can have a significant impact on their overall results.  Different strategies are deployed, with some teams adjusting their approach based on their opponent, ice conditions, or other factors.   Some teams appear to have the same approach every game, either very conservative with few stones in play or aggressive with more stones in play.  Teams can analyze the results from an opponent’s first end performances and determine the likely situations they will face at the beginning of the game [8]. 

**First End: Team Jennifer Jones with Hammer 2017/18 Season** 

|END|BLANK|SCORE 3|SCORE 2|SCORE 1|STEAL 1|STEAL 2|ENDS|
|---|---|---|---|---|---|---|---|
|**1**|7 (9.2%)|10 (13.2%)|22 (28.9%)|26 (34.2%)|5 (6.6%)|1 (1.3%)|76|
||[W6-L1]|[W10-L0]|[W19-L3]|[W23-L3]|[W:4-L:1]|[W:1-L:0]||



**Table 5** : Example of top women’s team with hammer first end results during the 2017/18 season. Blanking at 9.2% is very low (some teams blank nearly 50% of their ends).  This lets an opponent know the likelihood of where this team will place its first few shots of the end.  In this case, Team Jones will likely place a corner guard if their opponent goes into the rings, rather than hitting the open stone. 



2019 Research Papers Competition Presented by: 



9 



**First End: Team Rachel Homan with Hammer 2017/18 Season** 

|END|BLANK|SCORE 3|SCORE 2|SCORE 1|STEAL 1|STEAL 2|ENDS|
|---|---|---|---|---|---|---|---|
|**1**|14 (43.8%)<br>[W10-L4]|0 (0%)<br>[W0-L0]|6 (18.8%)<br>[W6-L0]|8 (25%)<br>[W6-L2]|1 (3.1%)<br>[W:1-L:0]|3 (9.4%)<br>[W:1-L:2]|32|



**Table 6** : Example of another top women’s team with hammer first end results during the 2017/18 season. Blanking at 43.8% is very high (compare to Table 5 above).  In this case, Team Homan will likely hit an open stone if their opponent goes into the rings.  Their HE (.33) and SD (.13) are lower than their average (HE=.41 and SD=.18), indicating that late in the end that they may take less risk than they might attempt in other ends. 

**First End: Team Jamie Sinclair without Hammer 2017/18 Season** 

|END|BLANK|SCORE 3|SCORE 2|SCORE 1|STEAL 1|STEAL 2|ENDS|
|---|---|---|---|---|---|---|---|
|**1**|24 (48%)|3 (6%)|8 (16%)|14 (28%)|1 (1.7%)|0 (0%)|50|
||[W13-L11]|[W1-L2]|[W2-L6]|[W6-L8]|[W:1-L:0]|[W:0-L:0]||



**Table 7** : Example of top women’s team without hammer first end results during the 2017/18 season. Blanking at 48% is very high.  Team Sinclair will very likely put the first stone into the rings rather than a guard.  With only 1 steal in 50 ends and FE close to their team average, they are likely to avoid risks later in the end as well. 

### **4.1.2 Change Analysis** 

A Change Analysis table [9] includes the statistics explained in section 3, calculated for a specific score differential.  This provides an examination of how a team performs in various situations it faces and can help suggest what strategy and level of aggression they may be using in these ends. The SCORE column provides the score differential of a team ahead (up), tied, or down (dwn) for ends with hammer and without. Important to note the tied situations will include first ends (as all first ends are tied) and teams who play different in the first end from their normal strategy will see a change in results after the first end.  BL is the percentage of blank ends.  This table also allows us to see how often a team plays ahead (Control, Dominant and Ultimate) compared to behind (Longshot, Sever and Deficit). 

**Change Analysis: Team John Shuster 2017/18 Season** 

|**Total Games**<br>**Situational A**|**: 71**<br>**nalysis:**|WITH H|AMMER||||WITHO|UT HAMM|ER|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Situation|All<br>Ends|ENDS|SCORE|BL|HE|SD|ENDS|SCORE|BL|FE|SE|
|Longshot:|66|46|dwn3+|0.09|0.28|0.26|20|down2+|0.00|0.33|0.25|
|Severe:|78|48|dwn2|0.11|0.39|0.21|30|dwn1|0.07|0.55|0.27|
|Deficit:|158|62|dwn1|0.13|0.44|0.16|96|tied|0.17|0.50|0.17|
|Control:|124|66|tied|0.13|0.34|0.21|58|up1|0.07|0.41|0.26|
|Dominant:|73|28|up1|0.19|0.25|0.25|45|up2|0.16|0.71|0.22|
|Ultimate:|52|17|up2+|0.00|0.35|0.24|35|up3+|0.03|0.43|0.37|





2019 Research Papers Competition Presented by: 



10 



**Table 8** : When tied after the first end, this team has 18% blank ends with hammer and drops to 7% (from 17%) without hammer.  This indicates they will be very aggressive when tied without hammer and either want to steal or force.  Their performance when down 1 with hammer is better than other situations and Team Shuster may want to examine if their strategy in these ends is contributing to this result and consider how they can improve elsewhere. 

**Change Analysis: Team Brad Gushue 2017/18 Season** 

**<mark>Total Games: 92</mark>** 

|**Situational A**|**nalysis:**|WITH H|AMMER||||WITHO|UT HAMM|ER|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Situation|All<br>Ends|ENDS|SCORE|<br>BL|HE|SD|ENDS|SCORE|BL|FE|SE|
|Longshot:|26|17|dwn3+|0.06|0.44|0.06|9|down2+|0.22|0.60|0.22|
|Severe:|38|26|dwn2|0.09|0.63|0.12|12|dwn1|0.00|0.90|0.17|
|Deficit:|132|58|dwn1|0.10|0.45|0.14|74|tied|0.15|0.72|0.23|
|Control:|235|158|tied|0.25|0.52|0.09|77|up1|0.21|0.67|0.23|
|Dominant:|161|63|up1|0.20|0.42|0.14|98|up2|0.12|0.65|0.23|
|Ultimate:|146|44|up2+|0.07|0.66|0.07|102|up3+|0.15|0.57|0.22|



**Table 9** : Compare Team Gushue to Team Shuster.  Removing first end results, they have 17% blank ends when tied without hammer and 21% blank ends when up 1 without hammer.  These numbers indicate Gushue can often be more conservative in these situations. 

**Change Analysis: Team John Epping 2017/18 Season** 

**<mark>Total Games: 94</mark>** 

|**Situational A**|**nalysis:**|WITH H|AMMER||||WITHO|UT HAMM|ER|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Situation|All<br>Ends|ENDS|SCORE|<br>BL|HE|SD|ENDS|SCORE|BL|FE|SE|
|Longshot:|68|46|dwn3+|0.14|0.41|0.22|22|down2+|0.05|0.54|0.36|
|Severe:|100|66|dwn2|0.26|0.38|0.24|34|dwn1|0.18|0.48|0.21|
|Deficit:|218|75|dwn1|0.13|0.45|0.17|143|tied|0.22|0.61|0.21|
|Control:|166|92|tied|0.18|0.42|0.20|74|up1|0.16|0.57|0.20|
|Dominant:|94|30|up1|0.04|0.48|0.23|64|up2|0.19|0.56|0.28|
|Ultimate:|104|36|up2+|0.00|0.50|0.19|68|up3+|0.06|0.71|0.18|



**Table 10** : Team Epping has a very high number of blank ends in most situations.  Blank of 26% when down two points with hammer and 18% when one down without hammer is much more conservative than most other teams. 

### **4.2. In-game Decisions** 

We stated in the Introduction that a skip will make 80 shot decisions in a 10-end game. Win probability can be considered in every decision.  Each decision can be made by considering if the shot call will increase or decrease the chance to win.  There are several other factors to consider, some which may have numerical values, like shooting percentages, but many others that are more intuitive, such as ice conditions, assessing the opponent’s abilities and calculating the probable result of each subsequent shot in an end. 





2019 Research Papers Competition Presented by: 

11 



One common example of calculating a decision with Win Probability is the final shot of an end where a skip can choose a routine draw for a single point or attempt a more difficult shot for two. When this happens in the final end [10] with a team with hammer is behind one point, it determines whether the team will win, lose or extend the game to an extra end without hammer. 

### **4.2.1 Scenario 1: One down with hammer. Last shot of the final end.** 



**Figure 7** : Team Yellow is about to throw the last rock and is down 1 in the final end.  Their decision is whether to draw or hit for a single point and head to an extra end or attempt a double take-out, removing both Red stones and staying to sit two points and win the game. 

Using the Win Probability charts, in Table 3 and 4, we can examine the percentage of times Yellow needs to make the double takeout for it to be the correct call.  Let’s assume Yellow’s chance of taking a single point with a hit or draw is 95%.  Win Probability (WP) tied without hammer and one end remains is 25.1% for men and 31.9% for women.  On average, Yellow should attempt the double take-out if they have a better than 24% (30% for women) chance of making the double. There is also some small chance of scoring one with the double attempt, and this supports the decision to try the more difficult shot.  Yellow may also consider Team Red’s abilities and whether they are below or above average, along with the strength of his or her own team and adjust accordingly. 

### **4.2.2 Scenario 2: One up without hammer.  Second last shot of second to last end.** 





2019 Research Papers Competition Presented by: 

12 





**Figure 8** : Team Yellow (a men’s team) is ahead by one point without hammer in the second to last end.  This is their final stone, with Red having the last shot of the end.   The choices are hit and roll out, hit and stay, hit and roll behind the guard, draw up to the front of the red stone (freeze) or draw around the centre guard.   The thought process for Yellow is as follows: 

If the result is a Blank, Yellow’s Win Probability, WPy = 58.7% If Red is forced to one point, WPy = 74.9% If Yellow steals one point, WPy = 86.7% If Red scores two points, WPy = 41.3% 

Hitting and staying or rolling out will very likely result in a blank. For simplicity, we estimate as 100%, so WPy = 58.7% 

Hit and roll is a difficult shot to make perfectly and, in most cases, will result in a simple shot to blank the end.  Estimate a perfect hit and roll as 20% and assume if made Red will always score one point. 

WPy = (.2)(.749)+(.8)(.587) = .620 or 62% (7) 

A freeze is also a very difficult shot.  We would estimate it to be more difficult than the hit and roll so WPy will be below .620. 

Draw around centre guard could result in a steal, a force of one or Red scoring two points.  Yellow’s estimations of these outcomes will determine if it is the correct call. 

Estimates: 

Red scores 2 = 40% 



2019 Research Papers Competition Presented by: 



13 



Red scores 1 = 50% Yellow steals 10% 

WPy = (.4)(.413)+(.5)(.749)+(.1)(.867)= .627 or 62.7% (8) 

In this case, if Yellow is confident they can avoid Red scoring 2 less than 40% of the time, the draw around the centre would be the correct choice. 

### **4.2.3 Scenario 3: Tied without hammer.  First shot with 3 ends remaining.** 

Yellow (women’s team) is tied without hammer and three ends remain.  It is the first shot of the end.  Here are the potential Win Probabilities at the completion of this end: 

Blank End, WPy = 38.5% Yellow Steals, WPy = 63.4% Red Scores 1, WPy = 36.6% Red Scores 2, WPy = 17.5% 

A steal is clearly advantageous, but teams aggressively attempting to steal will put more rocks in play and increase chance of a multiple score end, which is a less desirable result.  Historically, teams in this position would place a centre guard, but in this situation, it can be better to place the first stone into the top rings, above the button.  Red will likely place a corner guard and then yellow can place a guard in front of their stone.  If Red chooses to hit instead, Yellow can then hit and it’s more likely that a blank (higher WPy than even a force) will occur with a reduced chance of Red scoring 2 or more points.  It is interesting to note, on Red’s last shot, faced with blanking the end or taking a single point, teams will nearly always blank in this situation, even though it’s mathematically incorrect to do so. 

### **4.2.4 Shot Tracking Analysis** 

Section 4.2.3 is an example of how shot tracking information will help a team better analyze a situation.  Currently teams make estimations of the likelihood of outcomes (a blank, force, deuce, or steal) but with a data lake of shot results they will be able to better predict the outcome based on placement of stones in real game situations.   Curling has recently adopted a new rule which restricts an opponent’s guard being removed until the 6<sup>th</sup> stone delivered in the end (known as the 5-rock Free Guard Zone or FGZ).  The rule previously was the 4-rock FGZ and the difference has an impact on a team’s strategy in many situations.  There were limited events played in this format prior to 2018/19 Season and time is required to collect the data necessary to provide useful analysis.  With all World Curling Tour and World Curling Federation events adopting the rules this season, we expect some meaningful analysis to be available by early 2019. 

## **5. Conclusion** 

In this paper we have presented currently available data and statistics for analyzing curling and shown examples of how teams can leverage this information to improve their play.  This work has been in development for over a decade but it’s only recently that some teams have started to incorporate analytics into their team development. 





2019 Research Papers Competition Presented by: 

14 



Over the 2017/18 season, CurlingZone worked with 2018 Olympic Gold Medalist, Sweden’s Team Hasselborg.  Sweden coach Maria Prytz quoted on working with Gerry Geurts: “He is incredibly skilled at tactics and numbers, so he can look at different teams and explain how they play in different modes. It has been worthwhile for me to raise different scenarios for the team”. Maria explained that when she and the team started working together, they first looked at their own game plan, “Then we started thinking about how we could take another step in (improving) tactics and start matching our game with the opponents.” 

Agnes Knochenhauer, second on Team Hasselborg on how they approached Korea in the gold medal final: “The stats played a major part because we knew how to play them to put them in an uncomfortable situation. We also knew what didn’t work since we lost to them in the round robin getting trapped in their game plan. With stats from CurlingZone we knew what type of game they had been playing all week with great success and it was our job to break that and take advantage of the game.” [11] 

CurlingZone has presented at several US high performance camps and 2018 Olympic Gold Medalist Team Shuster, referenced this as an influence on their success.  Second Matt Hamilton to Nate Silver and Neil Paine of the website FiveThirtyEight.com on its Podcast “The Lab” in March of 2018 [11]: “(Gerry) sat us down at our summer camp and explained to us where we sat (among) elite players at certain things, like with the hammer/without the hammer, up by one with the hammer/down by one with the hammer… and it went on for all of the potential scoring scenarios. And he gave us feedback (on) which positions we could be better at, which ones we’re really good at, where we need to keep doing what we’re doing. Then he gave us some info on other teams in those same kind of numbers… I’d be lying if I said that didn’t come into play at all.” 

There is more analysis that can be done even with the data available today. Shooting percentages could be examined further with the ability to link results to the outcomes and rankings of teams relative to competition can be improved.  The real opportunity, however, will come when we have a data pool of shot information. Eventually we will be able to collect every shot – its direction, speed, rotation, eventual location, linked to each game and situation.  CurlingZone’s Shot Tracking system TAP will analyze manually entered data for the first few stones of each end, but the goal is to have automated data capture of every shot in every game, similar to how SportVu and Second Spectrum transformed analytics for the NBA. 

Other curling research is in development, some of which disregards historical game data. Mike Bowling and Zaheen Ahmad at the University of Alberta have been working on an artificial intelligence program for curling.  This approach has worked in games like Checkers, Go and Poker. Games have no issue with physical accuracy, a card played is always successful, but a delivered stone has many possible locations after it’s stopped, and it will be interesting to see how machine learning models can apply to sports. 

Analytics within curling has taken time to gain acceptance, but players and coaches have begun to understand and are starting to push for more data and information.  The window for the adoption of analytics in curling is just starting to open, but in a sport compared to chess, as teams improve, and the level of skill equalizes, using analytics will become an essential piece for success in the future. 





2019 Research Papers Competition Presented by: 

15 



## **References** 

[1]http://www.thegrandslamofcurling.com/curling/masters/2018-canadian-beef-masters- <u>womens-scores/</u> and Geurts, G. and Bittle, D. article “Shot Tracker” published in “CurlingZone 2006- 

07 Edition of The Black Book of Curling”, Top Floor Media (2006). 

[2] Palmer, K. “The End Game” research paper, 2014. 

[3] Palmer, K. article “Curling With Math” published in Geurts, G. and Bittle, D. “CurlingZone 200607 Edition of The Black Book of Curling”, Top Floor Media (2006). 

[4] http://www.curlingzone.com/analytics.php#1. 

[5] 

<u>http://www.curlingzone.com/rankings.php?task=week&orderby=ytd&oomid=81&eventyear=201 8&week=39#1 and http://www.curlingzone.com/rankings.php?task=week&orderby=ytd&oomid=82&eventyear=201 8&week=39#1</u> 

[6] CurlingZone <u>http://www.curlingzone.com/ and Geurts, G. and Bittle, D. “CurlingZone 2005-06</u> Edition of The Black Book of Curling”, Top Floor Media (2005). 

[7] http://curlwithmath.blogspot.com/2018/11/a-new-statistic-hammer-factor.html 

[8] CurlingZone http://www.curlingzone.com/ 

[9] CurlingZone http://www.curlingzone.com/ 

[10] http://curlwithmath.blogspot.com/2006/10/1-up-in-9th-end-without-hammer.html 

[11] https://www.dn.se/sport/statistiknorden-hjalpte-sverige-med-guldtaktiken 

[12] https://fivethirtyeight.com/features/we-talk-curling-and-stats-with-the-guys-who-won-the- <u>gold/</u> 



Presented by: 



2019 Research Papers Competition 

16 


