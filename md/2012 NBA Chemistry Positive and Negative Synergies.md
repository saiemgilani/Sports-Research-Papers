<!-- source: 2012 NBA Chemistry Positive and Negative Synergies.pdf -->

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



# **NBA Chemistry: Positive and Negative Synergies in Basketball** 

Allan Maymin, Philip Maymin (contact author), and Eugene Shen NYU-Polytechnic Institute Six MetroTech Center, Brooklyn, NY 11201 <u>philip@maymin.com</u> 

## **Abstract** 

We introduce a novel Skills Plus Minus (“SPM”) framework to measure on-court chemistry in basketball.  First, we evaluate each player’s offense and defense in the SPM framework based on three basic categories of skills:  scoring, rebounding, and ball-handling.  We then simulate games using the skill ratings of the ten players on the court.  The results of the simulations measure the effectiveness of individual players as well as the 5-player lineup, so we can then calculate the synergies of each NBA team by comparing their 5-player lineup’s effectiveness to the “sum-ofthe-parts.”  We find that these synergies can be large and meaningful.  Because skills have different synergies with other skills, our framework predicts that a player’s value is dependent on the other nine players on the court. Therefore, the desirability of a free agent depends on the players currently on the roster.  Indeed, our framework is able to generate mutually beneficial trades between teams.  Other ratings systems cannot generate ex-ante mutually beneficial trades since one player is always rated above another.  We find more than two hundred mutually beneficial trades between NBA teams, situations where the skills of the traded players fit better on their trading partner’s team. 

## **1   Introduction** 

“My model for business is The Beatles. They were four guys who kept each other’s negative tendencies in check. And the total was greater than the sum of the parts. Great things in business are not done by one person; they are done by a team of people.” 

– Steve Jobs 

With the third pick in the 2005 NBA draft, the Utah Jazz selected Deron Williams, a 6’3” point guard who played collegiately at Illinois.  Using the very next pick, the New Orleans Hornets drafted Chris Paul, a 6’0” point guard from Wake Forest.  Since the moment they entered the league, the careers of Williams and Paul have often been compared.  Which one is the better point guard?  Did Utah make a mistake in selecting Williams ahead of Paul? 

The box score statistics seem to favor Paul.  His career statistics (18.7 points per game, 4.6 rebounds, 9.9 assists, 2.4 steals, 0.571 true shooting percentage (“TS%”)) are better than Williams across the board (17.2 points, 3.2 rebounds, 9.2 assists, 1.1 steals, 0.560 TS%).  Paul has played in more All-Star games (4 vs. 2) and appeared on more All-NBA teams (3 vs. 2).  Supporters of Williams point to his better regular season record (0.590 winning percentage vs. 0.555 for Paul), relative playoff success (20 playoff wins vs. 10), head-to-head record against Paul, size, strength, and durability.  They argue that Williams is a stronger one-on-one defender who does not gamble for steals. 

At the end of the 2009-2010 season, if Utah had traded Deron Williams for Chris Paul, would they have been better off?  If New Orleans had traded Chris Paul for Deron Williams, would they have been better off?  Using the framework introduced in this paper, we can answer these questions: surprisingly, the answer is YES to both.  A Williams-for-Paul swap would have made both teams better off and is an example of a mutually beneficial trade. 

This paper introduces a novel Skills Plus Minus (“SPM”) framework to measure on-court chemistry in basketball. This SPM framework builds upon the Advanced Plus Minus (“APM”) framework first introduced by Rosenbaum [1].  While APM evaluates each player based on the points scored while they are in the game, SPM evaluates each player based on the offensive and defensive components of three basic categories of skills:  scoring, rebounding and ball-handling.  For example, a player’s “steal” ratings (part of the ball-handling category) are determined by how many steals occur while he is in the game.  Like APM, SPM considers the other nine players on the court.  A benefit of the APM and SPM framework is the ability to capture skills that are not found in traditional box score measures, such as off-the-ball defense, boxing out, and setting picks.  Also, in contrast to other ratings such as Wins Produced, APM and SPM do not make position and team adjustments to the player ratings. 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



We use the SPM framework to simulate games using the skill ratings of the ten players on the court.  These simulations incorporate how each play starts: out-of-bounds, steal, defensive rebound or offensive rebound.  We find these starting conditions materially affect the outcome of the possession.  The simulations are then used to measure the effectiveness of individual players and 5-player lineups. 

We investigate which basketball skills have synergies with each other.  Traditionally, team chemistry has been difficult to measure.  Berri and Jewell [2] use roster stability as a proxy for chemistry.  While they acknowledge the “potential impact of disruptive players,” (which we would call negative synergies in our framework) they note that “identifying and quantifying the impact of such players appears problematic.”  Our framework solves this problem. 

Another method to measure chemistry compares the “lineup APM” versus the sum of the constituent single player APM’s.  The problem with that approach is that there are too many possible five-player lineup combinations.  The APM’s of the five-player lineups have small sample problems since the minutes played of any given five-player lineup can be small.  Our innovation is that we are able to predict synergies while avoiding this problem. 

We calculate the synergies of each NBA team by comparing their 5-player lineup’s effectiveness to the “sum-of-theparts.” These synergies can be large and meaningful. Because skills have different synergies with other skills, a player’s value depends on the other nine players on the court.  Therefore the desirability of a free agent depends on the players currently on the roster. 

Finally, our framework is able to generate mutually beneficial trades.  Other ratings systems cannot generate mutually beneficial trades, since one player is always rated above another, c.f. Kubatko, et al [3] for a review of most of them, or Berri [4] or Berri [5] for more detail on Wins Produced.  Berri and Brook [6] investigate whether trades are ex-post mutually beneficial and argue that trades can be ex-ante mutually beneficial if the ex-post distribution of minutes is known and different.  In contrast, our framework generates ex-ante mutually beneficial trades without a change in the distribution of minutes played. Using our framework, we find many mutually beneficial trades, when the skills of the traded players fit better on their trading partner’s team.  One such mutually beneficial trade is Chris Paul for Deron Williams. 

## **2   Description of Data** 

While our primary innovation is a theoretical framework to model on-court chemistry, we use data to illustrate. Berri and Schmidt [7] criticize APM because the player ratings are not stable from year-to-year. They favor ratings that use box score statistics (e.g. Wins Produced), because the ratings are more predictable from year-to-year. We acknowledge Berri and Schmidt’s criticism and therefore use data from four NBA seasons (2006-2007 through 2009-2010) to achieve better estimates for player skills. While Fearnhead and Taylor [8] allow their APM ratings to be time-varying, we estimate one rating for all four years. The data we use is from http://basketballgeek.com/data, maintained by Ryan J. Parker, and represents a processed version of the play-by-play information from the NBA and ESPN. The data includes the names of all players on the court at each time, the location of the shots taken, result of possession, and more. The data set includes 4,718 games and 987,343 plays. 

## **3   Description of Model** 

In our Skills Plus Minus (“SPM”) framework, we run a series of nested probit regressions to estimate the likelihood of various events for a given play.  We order a series of events { _EVTi, i = 1,…n_ } sequentially.  We then define , the conditional probability of each _EVTi_ occurring, as: 



is the probability of the event _i,_ conditional on all prior events in the sequence not occurring (since only one event can occur per play). is the cdf of the standard normal distribution, is a constant associated with the event, is the home court dummy variable, is the possession start variable, and and are player dummy variables. is 1 if the home team has possession, and 0 if the away team has possession. are dummy variables for either “Defensive Rebound”, “Offensive Rebound”, or “Steal”.  “Out of Bounds” has been normalized to 0. are the dummy variables that indicate the offensive players on the court during the play, while are the dummy variables that indicate the defensive players.  We have dummy variables for the 360 

2 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



players who have participated in the most plays in our data sample, and define all others to be “replacement level” players. , , , and are coefficients associated with the variables, for event _i_ . Each player has two ratings in any given event: offense and defense. 

For example, if Rajon Rondo plays on the road on a team with four other replacement level players, against a team with five replacement level players, the probability of a steal for a possession that started out-of-bounds would be: 

if Rondo’s team has the ball 

if Rondo’s opponent has the ball 

We bucket each event into the following “skill” categories: 

- **Ball-handling Category** : Steal, Non-steal turnover 

- **Rebounding Category** : Rebound of a missed field goal, Rebound of a missed free throw **Scoring Category** : Made field goal (2 or 3 points), Missed field goal, Made free throw (1,2,3, or 4 points), Missed free throw (0,1,2, or 3 points). 

## **4   Features of the Model** 

### _Uses simulations to estimate both mean and variance of outcomes_ 

The SPM framework estimates how the start-of-play state variable (defensive rebound, offensive rebound, steal or out of bounds) affects the probability of an outcome.  If we start a game with an out of bounds play, we are able to simulate an entire basketball game, since we can use the estimated coefficients to estimate the probability of every possible outcome and the resultant end-of-play state variable.  We can then convert these simulations into winning percentages and point differentials.  To rate each player, we simulate games with the player and four “replacementlevel” players on one team, and five “replacement level” players on the other team.  We calculate a “steady-state” level of outcomes, and rank each player by the estimated point differential of an average length game.  Although we rank on estimated point differential, the simulations can give us a range of outcomes, not just a point estimate.  We can also use the framework to calculate the optimal strategy for end of game situations when there are only a few possessions remaining. 

### _Models at the “play” level instead of the “possession level”_ 

Imagine a situation where a team misses five consecutive field goals, and grabs five consecutive offensive rebounds, before finally making a field goal.  Traditional APM will consider that sequence of events one possession which results in two points.  Our SPM framework will instead count six plays, five of which end in missed field goals and offensive rebounds, and the sixth resulting in a made field goal.  SPM will determine that the team with the ball has poor scoring skills but excellent offensive rebounding skills.  Our framework distinguishes this sequence of events from a situation where the team immediately scores a field goal, since the outcomes were achieved in dramatically different ways.  In the former scenario, the defensive team may want to counter with a defensive rebounder, while in the latter scenario, the defensive team could counter with a stronger on-the-ball defender. 

### _Considers how a play starts_ 

Unlike traditional APM, our framework identifies how each play starts:  out-of-bounds, steal, defensive rebound or offensive rebound.  We find that the start variable materially affects the outcome of the play.  For example, we find that if a play starts with a steal, the average points scored increases from 0.83 to 1.04. 

### _Reveals the strengths and weaknesses of each player_ 

SPM provides granularity to a player’s offensive and defensive ratings.  If a player is a strong defender, is it because they create steals, prevent scoring, or grab defensive rebounds? 

## **5   Individual Player Ratings** 

In this section we provide the results of the skill ratings of the 360 players who participated in the most plays in our data sample. See Appendix 1 for the various tables of player ratings.  To estimate the contribution of each skill (e.g. steals), we isolate a player’s “steals” ratings, and set his other skills to replacement levels.  For example, we create a fictional player who has Ronnie Brewer’s “steals” ratings, but is replacement level in all other skills.  We then simulate games where one team consists of the fictional player and four replacement players, and their opponent utilizes five replacement players.  The estimated point differential of this game is the player’s ratings for that particular skill.  For example, we estimate that Ronnie Brewer’s defensive ball-handling skills are worth 3.2 points per game. 

3 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



We rank the players by Points Over Replacement Player (“PORP”), the average expected point differential if the player plays an entire game with replacement players. For instance, a team with LeBron James and four replacement players would outscore a team with five replacement players by 15.1 points per game on average. The weighted average PORP across our data set is 2.82 points. 

## **6   SPM Can Predict Which Skills Go Well with Each Other** 

To investigate synergies, we took the best players in the six skills and isolated their skills by setting their other skills to zero, or replacement level.  We then tested combinations to see which skills have synergies.  The six players are shown in Table 1. 

We measured synergies by how many additional points a combination of two skills create.  For example, Chris Paul's offensive ballhandling is worth 4.8 points, while Reggie Evans' offensive rebounding is worth 3.1 points.  We calculate that a team with Chris Paul's offensive ballhandling and Reggie Evans’ defensive rebounding will have a 8.1 point advantage.  Therefore we calculate synergies as worth 0.2 points (8.1-4.8-3.1).  Synergies are the difference between the point differential of the combined team and the sum of the two individual players; they tell us which types of players work well with one another.  Table 2 has the results.  We highlight a few of the bigger numbers. 

Offensive ballhandling (preventing turnovers) has negative synergies with itself (-0.825) because a lineup with one great ballhandler does not need another.  Defensive ballhandling (creating turnovers) has positive synergies with itself (0.307) because defenders who create turnovers feed off each other, creating more turnovers than they would individually.  Offensive scoring has negative synergies with itself (-0.826) because players must share one ball. Defensive scoring has negative synergies with itself (-0.284) because most defensive stands end with a stop anyway. 

Offensive rebounding has positive self-synergies (0.293), while defensive rebounding has negative self-synergies (- 0.394).  This differential sign illustrates a larger aspect of SPM. Because synergy is the excess to the total beyond the sum of the individual parts, any skill that adds to an event that is already likely to happen (such as securing a defensive rebound) will not give as much benefit as a skill that adds to an event that is unlikely to happen (such as securing an offensive rebound). 

The cross-terms are more complex. Offensive ballhandling has positive synergies with offensive rebounding (0.550) because offensive ballhandling helps a team convert possessions into shot attempts, and offensive rebounding increases the number of possessions over which the ballhandler can protect the ball.  Similarly, offensive ballhandling has positive synergies with offensive scoring (0.550) because the team receives more scoring opportunities, and those opportunities are good ones. 

Offensive scoring has positive synergies with defensive rebounding (0.254) and negative synergies with offensive rebounding (-0.191) because defensive rebounding increases the number of potential scoring opportunities while offensive rebounding is more valuable when offensive scoring is low, since poor offensive players generate more offensive rebounding opportunities. 

## **7   SPM Can Be Used to Calculate Synergies for Each NBA team** 

For each NBA team, we formed lineups using the top five players in terms of plays played in our data sample.  We calculated their ratings individually and as the 5-player lineup.  For a given lineup of players x1, x2, x3, x4 and x5, define PORP(x1,x2,x3,x4,x5) to be the estimated point differential between a game played by this team of players against a lineup of replacement players (“RP”).  We then define synergies as the difference of the sum-of-the-parts from the team total: 

The results are in Table 3.  Orlando’s lineup has the highest amount of synergies, over one point per game, while Minnesota’s negative synergies cost their lineup just under one point per game.  Using the Pythagorean expectation formula with coefficients between 14 and 16.5 (c.f. Morey [9]), 1-2 points per game can translate into 3-6 wins per season (for a team that would otherwise score and allow 100 points per game). Thus a team that consistently fields a highly positively synergistic lineup will win up to six games more than if it consistently fields a highly negatively synergistic lineup.  Such a differential could be the difference between making or missing the playoffs. 

4 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



To investigate why Orlando’s lineup has positive synergies, we replace players from their lineup one-by-one with replacement players and see how the synergies change.  We find that Jameer Nelson and Hedo Turkoglu play well together.  Our framework suggests that Nelson’s superior ballhandling skills complement Turkoglu’s offensive skills, since Nelson gives Turkoglu more chances to score. 

Using the same method, we find that Minnesota’s Ryan Gomes and Randy Foye are not good fits since they are both good offensive players who protect the ball well.  As noted earlier, our framework predicts negative synergies for both offense (since the players must share the ball) and offensive ball-handling (since one good ball-handler is enough for one lineup). 

## **8   SPM Gives Context Dependent Player Ratings** 

An implication of the SPM framework is that player values depend upon the other players on the court.  To illustrate this concept, we took the top four players in terms of plays played for each team.  We then put everyone else into a "free agent" pool.  For each team, we calculated which free agent would be the best fit for the remaining four players.  In this analysis, Kevin Garnett is a “free agent” because he switched teams from Minnesota to Boston in our data sample, and played only the fifth highest number of minutes for Boston.  Not surprisingly, he would be the most coveted free agent by every single team.  Russell Westbrook, a “free agent” because he played only two seasons in our data sample, is likewise highly coveted. There are, however, significant differences among the more marginal players.  For example, Eddie Jones, although retired, would fit well in a team like Minnesota (who rank him the fourth most desirable free agent), but would not fit in on the Spurs (who rank him seventeenth).  Likewise, Marcus Camby would be coveted by the Knicks or Nets (ranked sixth), but not by the Pacers (ranked nineteenth). The Table 4 shows the “free agent” fits for each team. 

## **9   Using SPM to Find Mutually Beneficial Trades** 

Other player rating systems like WP or Win Shares (see Oliver [10]) cannot generate ex-ante mutually beneficial trades because one player is always ranked higher than another (unless the distribution of minutes is changed).  In contrast, the SPM framework can generate mutually beneficial trades because each potential lineup has different synergies.  To search for mutually beneficial trades, we examined every possible two player trade from one team’s starting five to another team’s starting five.  There are a total of possible team trading partners. Each pair of teams has possible trades, so there are possible trades.  We found 222 mutually beneficial trades, or 2% of all possible trades.  These trades do not consider the distribution of minutes or the composition of the team’s bench.  We list a few trades in Table 5. 

Figure 2 shows the network of the 222 mutually beneficial trades among the various teams.  Not surprisingly, the teams with the lowest synergies (Minnesota and San Antonio) have the most possible trading partners and are near the interior of this “trade network”.  Meanwhile the teams with the highest synergies (Orlando and Cleveland) have the fewest trading partners and are on the perimeter. 

Why is Chris Paul for Deron Williams a mutually beneficial trade?  Overall, our SPM ratings rate Chris Paul and Deron Williams nearly the same, but with differences in skills.  Paul is a better ballhandler, Williams a slightly better rebounder, and Williams is better at offense and defense. See Table 6. 

The SPM framework predicts that Chris Paul is a better fit for Utah because he creates a lot of steals (3.1 steals per 48 minutes (“SP48M”)), while no one else in the New Orleans lineup does (West 1.0 SP48M, Stojakovic 1.1, Chandler 0.7, Butler 0.9).  Utah, on the other hand, has many players who create steals (Kirilenko 2.0, Boozer 1.5, Millsap 1.7, Okur 0.9, Williams 1.4).  Because defensive steals has positive synergies in our system, Chris Paul's ballhawking skills fit better in Utah, where he can team up with others and wreak havoc to opponents' ballhandlers. 

Conversely, why would New Orleans trade for Deron Williams?  Our framework predicts that Williams is a better offensive fit with New Orleans.  There are negative synergies between two good offensive players since they must share only one ball, and the New Orleans starters take fewer shots than Utah’s.  At New Orleans, Deron Williams would not need to share the ball with so many players. 

The Utah lineup of Williams (PG), Okur (F-C), Boozer (F-C), Kirilenko (F) and Millsap (F) may seem big.  The next player on Utah’s roster in terms of plays in our sample is Ronnie Brewer (G-F).  If we substitute Millsap for Brewer, the case for a Deron Williams for Chris Paul trade becomes stronger, since Brewer is good at steals (2.7 SP48M). 

5 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **10   Conclusion** 

We provide a novel Skills Plus Minus (“SPM”) framework that can be used to measure synergies within basketball lineups, provide roster-dependent rankings of free agents, and generate mutually beneficial trades. To our knowledge, the SPM framework is the first system that can generate ex-ante mutually beneficial trades without a change in the minutes played. Other ranking systems cannot generate mutually beneficial trades because one player is always ranked ahead of another. 

The appendices provide complete player rankings for various skills and synergies, present further empirical evidence in support of the SPM framework, measure the range of synergies, compare the results with traditional box score statistics, and provide a context for evaluating the movement of select star players in recent years. 

Future research could use the SPM framework to calculate the optimal substitution patterns that maximize overall synergies given a fixed distribution of minutes played to each player, highlight the risks and exposures each team with respect to the specific skills, and evaluate the possibility of a separate synergy factor of players that may improve the skills of their teammates by even more than would be suggested by the synergies of the skills. 

## **Acknowledgments** 

The authors thank Kevin Arnovitz, David Berri, Jeff Chuang, Harry Gakidis, Matt Goldman, Shane Kupperman, Irwin Lee, Wayne Winston, and members of the APBRmetrics forum for their helpful feedback and comments. 

## **References** 

[1] Dan T. Rosenbaum, “Measuring How NBA Players Help their Teams Win.” 82games.com, <u>http://www.82games.com/comm30.htm, 2004.</u> 

[2] D. J. Berri and R.T. Jewell, “Wage inequality and firm performance: Professional basketball's natural experiment.” Atlantic Economic Journal, 32:2, 130-139, 2004. 

[3] Justin Kubatko, Dean Oliver, Kevin Pelton, and Dan T. Rosenbaum, "A Starting Point for Analyzing Basketball Statistics," Journal of Quantitative Analysis in Sports 3:3, Article 1, 2007. 

[4] D. J. Berri, Who is most valuable? Measuring the player’s production of wins in the National Basketball Association. Managerial and Decision Economics, 20, 411-427, 1999. 

[5] D. J. Berri, A simple measure of worker productivity in the National Basketball Association. In The Business of Sport; eds. Brad Humphreys and Dennis Howard, 3 volumes, Westport, Conn.: Praeger: 1-40, 2008. 

[6] D. J. Berri and Stacey L. Brook, “Trading Players in the National Basketball Association: For Better or Worse”, in Sports Economics: Current Research; eds. John Fizel, Elizabeth Gustafson, and Larry Hadley, 135-151, 1999. 

[7] D. J. Berri, M.B. Schmidt, Stumbling on Wins: Two Economists Explore the Pitfalls on the Road to Victory in Professional Sports. Financial Times Press (Princeton, NJ), 2010. 

[8] Paul Fearnhead and Benjamin Matthew Taylor, “On Estimating the Ability of NBA Players,” Journal of Quantitative Analysis in Sports, 7:3, Article 11, 2011. 

[9] Daryl Morey in John Dewan, Don Zminda, STATS, Inc. Staff, STATS Basketball Scoreboard, STATS, Inc.. p. 17, 1993. 

[10] Dean Oliver, Basketball on Paper.  Potomac Books Inc., 2004. 

[11] ElGee, “Interpreting Advanced Statistics in Basketball”, http://www.backpicks.com, <u>http://www.backpicks.com/2011/01/24/interpreting-advanced-statistics-in-basketball/, 2011.</u> 

[12] Kevin Pelton, “WARP2 Electric Boogaloo”, www.basketballprospectus.com, <u>http://basketballprospectus.com/article.php?articleid=1209, 2010.</u> 

6 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



**Table 1** . The best players in each of the six skills. 

||**Offensive**|**Defensive**|
|---|---|---|
|**Ballhandling**|Chris Paul|Ronnie Brewer|
|**Rebounding**|Reggie Evans|Jason Collins|
|**Scoring**|Steve Nash|Kevin Garnett|



**Table 2.** Synergies between skills. 



7 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



**Table 3.** Synergies within teams. 

||**Player1**|**Player2**|**Player3**|**Player4**|**Player5**|**Separate**<br>**Co**|**mbined Syn**|**ergies**|
|---|---|---|---|---|---|---|---|---|
|ORL|D. Howard|R. Lewis|H. Turkoglu|J. Nelson|K. Bogans|24.3|25.6|1.2|
|CLE|L. James|A. Varejao|Z. Ilgauskas|D. Gibson|M. Williams|30.7|31.8|1.1|
|IND|D. Granger|T. Murphy|M. Dunleavy|J. Foster|B. Rush|18.2|19.3|1.1|
|DEN|C. Anthony|N. Hilario|J. Smith|K. Martin|A. Iverson|14.9|16.0|1.1|
|SAC|K. Martin|B. Udrih|J. Salmons|F. Garcia|B. Miller|12.9|14.0|1.0|
|NOK|D. West|C. Paul|P. Stojakovic|T. Chandler|R. Butler|23.0|23.8|0.8|
|DAL|D. Nowitzki|J. Terry|J. Howard|J. Kidd|E. Dampier|25.4|26.0|0.6|
|LAL|K. Bryant|L. Odom|D. Fisher|P. Gasol|A. Bynum|28.1|28.6|0.4|
|NJN|V. Carter|D. Harris|B. Lopez|R. Jefferson|J. Kidd|23.6|24.0|0.4|
|SEA|K. Durant|J. Green|N. Collison|E. Watson|R. Westbrook|18.6|18.8|0.2|
|DET|T. Prince|R. Hamilton|R. Wallace|R. Stuckey|J. Maxiell|15.4|15.5|0.1|
|BOS|P. Pierce|R. Rondo|R. Allen|K. Perkins|K. Garnett|29.4|29.5|0.0|
|UTA|D. Williams|M. Okur|C. Boozer|A. Kirilenko|P. Millsap|25.0|25.0|0.0|
|HOU|S. Battier|L. Scola|R. Alston|T. McGrady|C. Hayes|22.3|22.3|0.0|
|GSW|M. Ellis|A. Biedrins|S. Jackson|B. Davis|K. Azubuike|18.0|18.0|0.0|
|PHI|A. Iguodala|S. Dalembert|A. Miller|W. Green|T. Young|18.6|18.5|-0.1|
|CHA|R. Felton|G. Wallace|E. Okafor|B. Diaw|M. Carroll|13.2|13.1|-0.2|
|LAC|C. Kaman|A. Thornton|C. Mobley|E. Gordon|B. Davis|10.2|10.0|-0.2|
|TOR|C. Bosh|A. Bargnani|J. Calderon|A. Parker|R. Nesterovic|19.1|18.9|-0.2|
|CHI|L. Deng|K. Hinrich|B. Gordon|D. Rose|J. Noah|19.8|19.5|-0.3|
|MIA|D. Wade|U. Haslem|M. Chalmers|M. Beasley|D. Cook|18.0|17.7|-0.4|
|NYK|D. Lee|N. Robinson|W. Chandler|J. Crawford|J. Jeffries|14.3|13.9|-0.4|
|ATL|J. Johnson|J. Smith|M. Williams|A. Horford|M. Bibby|20.0|19.6|-0.4|
|PHX|S. Nash|A. Stoudemire|L. Barbosa|G. Hill|R. Bell|26.2|25.6|-0.6|
|POR|B. Roy|L. Aldridge|T. Outlaw|S. Blake|M. Webster|19.6|19.0|-0.6|
|MEM|R. Gay|M. Conley|O. Mayo|H. Warrick|M. Gasol|10.0|9.4|-0.6|
|WAS|A. Jamison|C. Butler|D. Stevenson|A. Blatche|B. Haywood|18.2|17.6|-0.6|
|MIL|A. Bogut|C. Bell|M. Redd|C. Villanueva|M. Williams|14.6|13.9|-0.7|
|SAS|T. Duncan|T. Parker|M. Ginobili|M. Finley|B. Bowen|25.8|25.1|-0.7|
|MIN|R. Gomes|A. Jefferson|R. Foye|C. Brewer|C. Smith|8.2|7.3|-0.8|



8 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



**Table 4** : “Free agents” and synergies. 

|CHI|**Top Choice**<br>K. Garnett|**2nd Choice**<br>R. Westbrook|**3rd Choice**<br>A. Johnson|**4th Choice**<br>N. Batum|**5th Choice**<br>R. Hibbert|**6th Choice**<br>C. Billups|
|---|---|---|---|---|---|---|
|PHX|K. Garnett|R. Hibbert|A. Johnson|R. Westbrook|N. Batum|B. Jennings|
|ATL|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|E. Jones|
|HOU|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|T. Young|
|IND|K. Garnett|R. Westbrook|A. Johnson|N. Batum|C. Billups|B. Jennings|
|LAC|K. Garnett|A. Johnson|R. Westbrook|N. Batum|R. Hibbert|C. Billups|
|MIL|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|T. Young|
|NOK|K. Garnett|A. Johnson|R. Westbrook|N. Batum|R. Hibbert|C. Billups|
|NYK|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|N. Batum|M. Camby|
|POR|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|C. Billups|
|TOR|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|N. Batum|C. Billups|
|WAS|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|N. Batum|C. Billups|
|DEN|K. Garnett|R. Westbrook|C. Billups|N. Batum|A. Johnson|B. Jennings|
|SAS|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|Y. Ming|
|CHA|K. Garnett|A. Johnson|R. Westbrook|N. Batum|R. Hibbert|T. Young|
|CLE|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|C. Billups|
|DET|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|T. Young|
|MIN|K. Garnett|A. Johnson|R. Westbrook|E. Jones|N. Batum|R. Hibbert|
|NJN|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|M. Camby|
|PHI|K. Garnett|A. Johnson|R. Westbrook|R. Hibbert|N. Batum|T. Young|
|SAC|K. Garnett|R. Westbrook|N. Batum|C. Billups|A. Johnson|R. Hibbert|
|SEA|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|C. Billups|N. Batum|
|UTA|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|N. Batum|T. Young|
|BOS|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|T. Young|
|DAL|K. Garnett|R. Westbrook|N. Batum|A. Johnson|R. Hibbert|C. Billups|
|MEM|K. Garnett|R. Westbrook|A. Johnson|C. Billups|N. Batum|E. Jones|
|LAL|K. Garnett|R. Westbrook|A. Johnson|R. Hibbert|N. Batum|C. Billups|
|MIA|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|E. Jones|
|ORL|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|B. Jennings|
|GSW|K. Garnett|R. Westbrook|A. Johnson|N. Batum|R. Hibbert|T. Young|



**Table 5** . Some mutually beneficial trades. 



**Table 6.** Comparison of Chris Paul and Deron Williams 

||**Off**|**Def**|**Off**|**Def**|**Off**|**Def**|
|---|---|---|---|---|---|---|
||**Ballhand.**|**Ballhand.**|**Rebound.**|**Rebound.**|**Scoring**|**Scoring**|
|Chris Paul|4.8|1.2|-0.4|-1.4|4.7|-0.9|
|Deron Williams|1.9|-0.3|-1.7|0.1|6.5|1.4|



9 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



|**Possession**<br>**Start**<br>**Event**<br>**Sub-event**<br>**Points**<br>**Sub-event**<br>**Change**<br>**End****|
|---|
|Steal<br>Steal<br>0<br>Yes<br>Steal<br>\<br>/|
|OOB<br>Non-Steal<br>0<br>Yes<br>OOB<br>\<br>Turnover<br>/|
|Made<br>2,3<br>Yes<br>OOB<br>\<br>Oreb<br>FGA<br>/|
|Oreb<br>No<br>Oreb<br>\<br>Missed<br>0<br>/|
|Dreb<br>Yes<br>Dreb<br>\<br>/|
|Made<br>1,2,3,4<br>Yes<br>OOB<br>\|
|Dreb<br>FTA*<br>/|
|Oreb<br>No<br>Oreb<br>\<br>Missed<br>0,1,2,3<br>/|
|Dreb<br>Yes<br>Dreb<br>\<br>/|



**Figure 1** . Flow chart of events.<sup>12</sup> 



**Figure 2** . Trade network of mutually beneficial trades. 

- Free throw events include “and-1” situations. 

- ** Steals, Oreb, and Dreb sometimes end with an OOB situation if a timeout is taken or a non-shooting foul is committed, for example. 

10 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **Appendix 1:  Player Ratings** 

_Best and Worst Overall_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|LeBron James|15.1|Johan Petro|-3.3|
|Steve Nash|14.3|Gerald Green|-3.3|
|Dwyane Wade|13.5|Joel Anthony|-3.8|
|Kevin Garnett|13.3|Brian Skinner|-4.5|
|Kobe Bryant|10.2|Dominic McGuire|-4.5|
|Dirk Nowitzki|9.7|Hakim Warrick|-4.9|
|Tim Duncan|9.6|Earl Boykins|-5.4|
|Chris Bosh|9.5|Eddy Curry|-6.7|
|Manu Ginobili|9.4|Josh Powell|-7.8|
|Russell Westbrook|9.4|J.J. Hickson|-8.8|



_Best and Worst Offensive Ballhandling (preventing steals and turnovers)_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Chris Paul|4.8|Mikki Moore|-2.4|
|Brandon Jennings|4.6|Andrew Bogut|-2.4|
|Kobe Bryant|4.3|Louis Amundson|-2.5|
|Sasha Vujacic|3.8|Hilton Armstrong|-2.7|
|Sam Cassell|3.6|Kwame Brown|-2.8|
|LeBron James|3.3|Yao Ming|-2.8|
|Chauncey Billups|3.2|Ryan Hollins|-3.3|
|Mike Conley|3.1|Kendrick Perkins|-3.4|
|Daequan Cook|3.1|Joel Przybilla|-3.5|
|Jason Terry|3.0|Eddy Curry|-6.3|



_Best and Worst Defensive Ballhandling (creating steals and turnovers)_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Ronnie Brewer|3.2|Tim Duncan|-2.0|
|Gerald Wallace|2.9|Michael Finley|-2.3|
|Thabo Sefolosha|2.9|Brook Lopez|-2.4|
|Devin Harris|2.9|Aaron Brooks|-2.5|
|Monta Ellis|2.8|Andrew Bynum|-2.5|
|Renaldo Balkman|2.8|Taj Gibson|-2.6|
|Rajon Rondo|2.7|Joel Anthony|-2.8|
|Luc Richard Mbah a Moute|2.7|Amare Stoudemire|-3.3|
|C.J. Watson|2.7|Erick Dampier|-3.6|
|Eddie Jones|2.7|J.J. Hickson|-4.2|



11 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



_Best and Worst Offensive Rebounding_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Reggie Evans|3.1|Chris Quinn|-1.9|
|Matt Harpring|3.0|Jannero Pargo|-2.0|
|Kevin Love|2.9|Donte Greene|-2.0|
|Jeff Foster|2.7|Brandon Rush|-2.1|
|Jason Maxiell|2.6|Rashard Lewis|-2.3|
|Louis Amundson|2.5|Damon Stoudamire|-2.3|
|Leon Powe|2.2|Danilo Gallinari|-2.4|
|Amir Johnson|2.1|Travis Diener|-2.5|
|Joakim Noah|2.0|Stephen Curry|-2.8|
|Jared Jeffries|2.0|Jonny Flynn|-2.8|



_Best and Worst Defensive Rebounding_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Jason Collins|3.0|Francisco Garcia|-1.5|
|Tim Duncan|2.6|Sasha Vujacic|-1.5|
|Joel Przybilla|2.5|Eddie House|-1.6|
|Jeff Foster|2.5|Josh Childress|-1.6|
|Andrew Bogut|2.3|Dominic McGuire|-1.6|
|Zydrunas Ilgauskas|2.3|Darren Collison|-1.6|
|Nene Hilario|2.2|Charlie Bell|-1.7|
|Roy Hibbert|2.2|Jamaal Tinsley|-1.8|
|Rasho Nesterovic|2.2|Travis Diener|-2.1|
|Samuel Dalembert|2.0|Earl Boykins|-2.1|



_Best and Worst Offense (assuming no turnovers)_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Steve Nash|12.7|James Singleton|-2.3|
|Dwyane Wade|9.4|Josh Powell|-2.3|
|LeBron James|7.8|Hilton Armstrong|-2.4|
|Deron Williams|6.5|Louis Amundson|-2.4|
|Kevin Martin|6.4|Brian Skinner|-2.4|
|Kobe Bryant|6.3|Ben Wallace|-2.5|
|Goran Dragic|6.2|Jason Collins|-2.7|
|Dirk Nowitzki|5.9|Eric Snow|-3.0|
|Manu Ginobili|5.9|Renaldo Balkman|-3.4|
|Danny Granger|5.9|Nene Hilario|-3.7|



12 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



_Best and Worst Defense (assuming no turnovers)_ 

|**Best**|**PORP**|**Worst**|**PORP**|
|---|---|---|---|
|Kevin Garnett|6.2|Damien Wilkins|-3.0|
|Brendan Haywood|5.7|Josh Powell|-3.0|
|Tim Duncan|5.4|Kevin Martin|-3.0|
|Joel Przybilla|5.2|Gerald Green|-3.0|
|Amir Johnson|5.0|Marreese Speights|-3.2|
|Andrew Bogut|4.8|Juan Carlos Navarro|-3.2|
|Chris Andersen|4.5|Royal Ivey|-3.4|
|Jacque Vaughn|3.9|Jose Calderon|-3.4|
|Yao Ming|3.9|Sasha Vujacic|-3.7|
|Kendrick Perkins|3.9|Will Bynum|-4.2|



To rank the most one-dimensional and most well-rounded players, we lump the skills into four categories:  offense, defense, total rebounding and total ballhandling.  For most one-dimensional, we calculate the difference between the player’s best skill and their second best skill.  For most-rounded, we rank by the player’s worst skill. 

### _Most One-Dimensional_ 

||**Best**|**2nd **|**Best**|
|---|---|---|---|
|**One-dimensional**|**PORP**|**PORP **|**Skill**|
|Steve Nash|12.7|2.2|Offense|
|Dwyane Wade|9.4|3.9|Offense|
|Deron Williams|6.5|1.6|Offense|
|Kevin Martin|6.4|1.5|Offense|
|Danny Granger|5.9|1.0|Offense|
|Mike Miller|5.5|0.7|Offense|
|Aaron Brooks|4.5|-0.2|Offense|
|Kevin Love|4.8|0.3|Rebounding|
|Jacque Vaughn|3.9|-0.3|Defense|
|Carlos Boozer|4.8|0.6|Offense|



_Most Well-Rounded_ 

||**Worst**|
|---|---|
|**Well-Rounded**|**PORP**|
|LaMarcus Aldridge|1.4|
|Luol Deng|0.9|
|Omri Casspi|0.9|
|Thaddeus Young|0.8|
|Marcus Camby|0.7|
|Julian Wright|0.6|
|Anderson Varejao|0.5|
|Jonas Jerebko|0.5|
|Kevin Garnett|0.5|
|Lamar Odom|0.4|



13 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **Appendix 2:  Empirical Evidence Suggests that Synergies Exist** 

Our framework predicts that skills that affect rare events (e.g. steals, offensive rebounds) will have positive synergies, while skills that contribute to common events (e.g. defensive rebounds) will have negative synergies.  This feature is a result of our nested probit specification.  Is this specification realistic?  Do two players with strong defensive ballhandling skills create more turnovers than one? 

To investigate this question, we sorted the 987,343 observations into one hundred buckets, ordered by predicted steals.  Within each bucket (each with 9873 or 9874 observations), we calculated the total predicted steals and the total actual steals.  In the following scatterplot, we graph the one hundred data points, each representing a bucket of actual steals and predicted steals.  If positive synergies in steals do not exist, then we would see that actual steals are less than predicted steals, for high levels of predicted steals. 

Instead, we find only three points out of one hundred fall outside the 95% confidence intervals: two below and one above.  This evidence suggests that our choice of probit to model the synergies in steals is a reasonable one. 

### **Actual Steals (y-axis) versus Predicted Steals (x-axis), with 95% probability confidence bands** 



Our framework also predicts that offensive rebounding has positive synergies with itself.  Using the same methodology, we plot actual offensive rebounds versus predicted offensive rebounds.  We have 407,154 missed field goals in our data set, so that each bucket contains 4,071 or 4072 observations.  The below scatterplot shows that only four points out of one hundred fall outside the 95% confidence bands.  These two scatterplots suggest that positive synergies do exist for both steals and offensive rebounds, as our framework predicts. 

**Actual Offensive Rebounds (y-axis) versus Predicted Offensive Rebounds (x-axis), with 95% probability confidence bands** 



14 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **Appendix 3:  Measuring the Range of Synergies** 

We calculated the synergies of a lineup that consisted of the four Houston Rockets who played the most minutes (Battier, Scola, Alston and McGrady), with each of the 360 players rated in our database. 

We chose the Rockets because they are near the league average for both combined PORP and estimated synergies. The following graph plots the estimated synergies with the PORP of each player. 

The synergies range from -2 to 1 points per game, confirming our previous estimates.  The range does not seem to depend on the level of PORP, meaning that differing synergies can be found for all levels of players.  The analysis suggests that teams should consider synergies as an important variable when evaluating players of similar overall skill levels. 



15 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



## **Appendix 4: Comparing SPM With Box Score Statistics** 

We examine the relationship between the six SPM ratings with box score statistics.  We collected box score data from www.basketball-reference.com for the same seasons we used for our SPM ratings (2006-2007, 2007-2008, 2008-2009, and 2009-2010).  Using the same 360 player data set, we then regressed each of the six ratings against the following pool of explanatory variables: 

|**Explanatory**|||
|---|---|---|
|**Variable**|**Numerator**|**Denominator**|
|2Pts%|2*2FGM|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|3Pts%|3*3FGM|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|FTM%|1*2FTM|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|2FGA%|2FGA|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|3FGA%|3FGA|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|FTA%|FTA|MP/(TmMP/5)*(TmFGA+0.44*TmFTA)|
|AST%|Ast|((MP / (Tm MP / 5)) * Tm FGM) - FGM|
|STL%|STL|MP/(TmMP/5)*(OppFGA+0.44*OppFTA+OppTOV)|
|TOV%|TOV|MP/(TmMP/5)*(TmFGA+0.44*TmFTA+TmTOV)|
|ORB%|ORB|MP/(TmMP/5)*(Tm ORB+OppDRB)|
|DRB%|DRB|MP/(TmMP/5)*(Tm DRB+OppORB)|
|BLK%|Blk|MP/(TmMP/5)*(OppFGA-Opp3PA)|
|Minutes/Game|MP|G|
|Foul%|PF|MP/(TmMP/5)*(OppFGA+0.44*OppFTA+OppTOV)|
|Height|Height||
|BMI|Weight*4.88|Height^2|
|Age|Age||



For each regression, we began with all of the explanatory variables, and then eliminated variables one-by-one by order of least significant until all the remaining explanatory variables had a t-statistic greater than 2.  The coefficients of the regressions are given below.  All the coefficients in the table are significant. 

16 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



||**Oball**|**Dball**|**Oreb**|**Dreb**|**Oscore**|**Dscore**|
|---|---|---|---|---|---|---|
|Constant|1.63|-0.01|-1.18|-9.36|-12.65|-1.50|
|(t-stat)|(2.05)|(-0.01)|(-6.45)|(-5.83)|(-5.31)|(-4.09)|
|2Pts%|-31.17|-13.63|-8.84||124.78||
|(t-stat)|(-3.43)|(-4.28)|(-3.82)||(8.45)||
|2FGA%|28.63||||-56.73||
|(t-stat)|(6.24)||||(-7.74)||
|3Pts%|43.73|-12.03|||237.20||
|(t-stat)|(9.04)|(-2.29)|||(5.30)||
|3FGA%|||||-58.97||
|(t-stat)|||||(-3.45)||
|FTM%|10.47|||-7.57|71.15||
|(t-stat)|(3.14)|||(-3.47)|(4.40)||
|FTA%||5.89|11.05||-37.33||
|(t-stat)||(2.21)|(5.31)||(-2.96)||
|AST%|10.04|-1.65||1.95|10.93|4.06|
|(t-stat)|(13.24)|(-2.49)||(3.23)|(9.52)|(3.12)|
|BLK%|-9.75|-13.93|-8.28|-11.02||64.28|
|(t-stat)|(-2.35)|(-3.24)|(-2.2)|(-2.96)||(8.95)|
|TOV%|-139.66|||||-49.61|
|(t-stat)|(-14.80)|||||(-3.75)|
|STL%|33.26|188.59|33.41|-33.46|||
|(t-stat)|(3.09)|(16.77)|(3.99)|(-3.76)|||
|ORB%|||28.25|5.87|||
|(t-stat)|||(16.09)|(2.99)|||
|DRB%|||-6.55|5.72||4.74|
|(t-stat)|||(-5.69)|(4.64)||(2.41)|
|Foul%||9.52||18.85|-20.60||
|(t-stat)||(2.00)||(4.04)|(-2.94)||
|Minutes/Game||||0.03||0.03|
|(t-stat)||||(3.71)||(3.15)|
|Height||||0.75|1.70||
|(t-stat)||||(3.31)|(4.81)||
|BMI|-0.05|-0.07||0.08|||
|(t-stat)|(-2.02)|(-2.52)||(3.54)|||
|Age|-0.02|||0.02|||
|(t-stat)|(-2.15)|||(2.74)|||
|R-squared|71.6%|54.5%|53.6%|58.1%|65.8%|36.0%|



The R-squareds show that defensive scoring (the ability to prevent an opponent from scoring) was, not surprisingly, the most difficult to measure based on box score statistics.  On the other hand, offensive ball-handling and offensive scoring had the highest R-squareds, meaning that box score statistics did a better job explaining their SPM ratings. 

It is important to note that correlation does not imply causality for these regressions.  For example, in the offensive ball-handling category, two point field goal attempts has a positive coefficient while two point field goal made has a negative coefficient.  These results do not, however, suggest that missing a lot of shots makes a player a better ballhandler.  Instead, we can infer that players who take a lot of shots tend to protect the ball well (e.g. Carmelo Anthony).  Perhaps these players are adept at positioning themselves to receive the ball in a safe manner.  The offensive rebounding category provides another example.  Defensive rebounding has a negative sign, which seems like a counterintuitive result until we consider court positioning.  Players who grab a lot of defensive rebounds but 

17 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



not offensive rebounds tend to be big men who shoot from the outside (e.g. Dirk Nowitzki and Rasheed Wallace). If a team’s big men play on the perimeter, then the team will grab fewer offensive rebounds. 

We calculate fitted values using the regression coefficients for the 360 players in our data set.  The correlation between these fitted values and a player’s SPM ratings is 70%.  Here’s a comparison of the top and bottom 10 SPM players and a top 10 list generated by the fitted values in the regressions. 

|**Top 10 SPM**|**PORP**|**Top 10 Fitted Values**|**PORP**|
|---|---|---|---|
|LeBron James|15.1|Chris Paul|13.6|
|Steve Nash|14.3|LeBron James|12.0|
|Dwyane Wade|13.5|Dwyane Wade|10.5|
|Kevin Garnett|13.3|Manu Ginobili|9.6|
|Kobe Bryant|10.2|Jason Kidd|8.5|
|Dirk Nowitzki|9.7|Chauncey Billups|8.4|
|Tim Duncan|9.6|Kobe Bryant|8.1|
|Chris Bosh|9.5|Gilbert Arenas|8.1|
|Manu Ginobili|9.4|Baron Davis|7.5|
|Russell Westbrook|9.4|Dirk Nowitzki|7.0|
|**Bottom 10 SPM**|**PORP**|**Bottom 10 Fitted Value**|**sPORP**|
|Johan Petro|-3.3|Brian Skinner|-1.4|
|Gerald Green|-3.3|Yakhouba Diawara|-1.5|
|Joel Anthony|-3.8|Hilton Armstrong|-1.7|
|Brian Skinner|-4.5|Jamaal Magloire|-2.2|
|Dominic McGuire|-4.5|Josh Powell|-2.3|
|Hakim Warrick|-4.9|Adam Morrison|-2.3|
|Earl Boykins|-5.4|Desmond Mason|-2.4|
|Eddy Curry|-6.7|Trenton Hassell|-2.4|
|Josh Powell|-7.8|Jason Collins|-2.4|
|J.J. Hickson|-8.8|Eddy Curry|-2.5|



## **Appendix 5: Comparison of SPM with Wins Produced and Win Shares** 

We compared the SPM ratings with two commonly used box score ratings systems:  Wins Produced and Win Shares.  (See Oliver [10] for details on Win Shares.)  We use the same 360 players over the 2006-2010 period.  SPM has a 56% correlation to Win Shares, and a 52% correlation to Wins Produced.  Here are the top 10 lists for both rating systems on a per-48 minutes basis.  WS48 is Win Shares per 48 minutes, while WP48 is Wins Produced per 48 minutes. 

18 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



|**Top 10 WS48**|**WS48**|**Top 10 WP48**|**WP48**|
|---|---|---|---|
|LeBron James|0.266|Chris Paul|0.317|
|Chris Paul|0.249|LeBron James|0.282|
|Manu Ginobili|0.227|Jason Kidd|0.278|
|Dirk Nowitzki|0.215|Manu Ginobili|0.277|
|Tim Duncan|0.209|Dwight Howard|0.270|
|Chauncey Billups|0.207|Chris Andersen|0.265|
|Dwight Howard|0.202|Marcus Camby|0.264|
|Yao Ming|0.202|Steve Nash|0.255|
|Amare Stoudemire|0.201|Josh Childress|0.239|
|Kevin Garnett|0.199|Ben Wallace|0.235|



We regressed the SPM ratings on WS48 and WP48, and then regressed the residuals on box score statistics. 

The results of these regressions show that Wins Produced and Win Shares tend to: 

- Undervalue assists and overvalue points scored.  Good passers create scoring opportunities for scorers and should be given more credit for the scoring done by a team. 

- Overpenalize missed field goals.  Sometimes a team’s best offensive players are asked to take lower percentage shots as the shot clock winds down.  They are then penalized if they miss the shots, when all five players on the court should share responsibility.  ElGee [11]at Backpicks.com echoes this sentiment when he writes “Wins Produced just assumes that scoring at a reasonably high baseline-rate will happen automatically”.  In other words, if a team has five Ben Wallaces on the floor, they cannot expect one of them to automatically turn into a baseline-rate shooter. 

- Overpenalize missed 3-pointers.  Kevin Pelton [12] explains, “there appears to be a value to spacing the floor that is not captured by individual statistics of three-point shooters.” 

- Undervalue steals.  A steal can lead to fast break opportunities.  As documented earlier, possessions which begin with steals have higher expected points scored. 

## **Appendix 6:  Using the SPM Framework to Evaluate Transactions Involving James and Anthony** 

Our data set ends with the 2009-2010 season, but we can use our framework to analyze personnel movements that occurred during the 2010-2011 season.  In this section, we examine LeBron James’ move to South Beach, and Carmelo Anthony’s trade to the Big Apple. 

_Does the new Miami lineup have positive or negative synergies?_ 

Our framework predicts that a lineup of LeBron James, Dwayne Wade, Chris Bosh, Mario Chalmers and Joel Anthony would be the strongest in the league, despite having negative synergies. 

19 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



|**Miami Heat**|**PORP**|
|---|---|
|Dwyane Wade|13.5|
|LeBron James|15.1|
|Chris Bosh|9.5|
|Mario Chalmers|3.1|
|Joel Anthony|-3.8|
|Synergies|-0.4|
|Total|36.9|



||**Off**|**Def**|**Off**|**Def**|**Off**|**Def**|
|---|---|---|---|---|---|---|
||**Ballhand.**|**Ballhand.**|**Rebound.**|**Rebound.**|**Scoring**|**Scoring**|
|LeBron James|3.3|1.3|0.5|-1.0|7.8|3.0|
|Dwyane Wade|2.2|1.7|0.6|-0.9|9.4|0.4|
|Chris Bosh|0.8|-0.6|0.1|1.3|5.5|2.3|
|Mario Chalmers|0.9|2.2|-1.1|0.4|2.3|-1.5|
|Joel Anthony|-2.2|-2.8|0.5|-0.5|-2.1|3.2|



While Joel Anthony is a strong one-on-one defender (+3.2 pts defensive PORP), he is not particularly adept at creating turnovers like his teammates (-2.8 pts defensive ballhandling).  Since defensive ballhandling has positive synergies with itself, Joel Anthony’s lack of ball-hawking skills make him a poor fit for the Heat lineup. 

The Miami heat example shows that the question of synergy fades quickly when a team has a chance to add Wade or LeBron.  Who cares about a point or two in synergy if the player brings double-digit points worth of talent?  Wade and LeBron are so much better than everybody else, that no amount of synergies would overcome the talent difference.  Synergy matters when a team is making decisions between players of otherwise relatively equivalent total talent. 

_Was the Carmelo Anthony trade a mutually beneficial trade?_ 

Players are traded for a variety of reasons, including on-court ability, contract situation, salary cap issues, synergies with teammates, age, leadership skills and locker room fit.  Our framework can be used to evaluate the trades from the quality of play perspective.  Here are the starting lineups, pre-trade and post-trade, of the Knicks and Nuggets. Unfortunately, Landry Fields and Ty Lawson did not play enough possessions to be rated. 

20 

MIT Sloan Sports Analytics Conference 2012 March 2-3, 2012, Boston, MA, USA 



|**Knicks Pre-Trade**|**PORP**|**Knicks Post-Trade**|**PORP**|
|---|---|---|---|
|Amare Stoudemire|0.1|Amare Stoudemire|0.1|
|Danilo Gallinari|5.6|Carmelo Anthony|4.3|
|Jared Jeffries|4.1|Jared Jeffries|4.1|
|Raymond Felton|7.1|Chauncey Billups|7.3|
|Landry Fields|NA|Landry Fields|NA|
|Synergies|-0.7|Synergies|-0.2|
|Total|16.2|Total|15.6|
|**Nuggets Pre-Trade**|**PORP**|**Nuggets Post-Trade**|**PORP**|
|Carmelo Anthony|4.3|Danilo Gallinari|5.6|
|Kenyon Martin|2.0|Kenyon Martin|2.0|
|Nene Hilario|-0.2|Nene Hilario|-0.2|
|Chauncey Billups|7.3|Raymond Felton|7.1|
|Ty Lawson|NA|Ty Lawson|NA|
|Synergies|0.7|Synergies|1.4|
|Total|14.0|Total|15.7|



The SPM ratings suggest that the Nuggets benefited more from the trade.  Danilo Gallinari has a higher overall rating than Carmelo Anthony, while Raymond Felton and Chauncey Billups have similar overall ratings.  While it is debatable whether Gallinari is actually better than Anthony, both teams’ synergies interestingly improve with the trade. 

Gallinari and Felton fit better in Denver because they cause more turnovers than Anthony and Billups.  Recall that defensive ballhandling has synergies with itself.  Kenyon Martin and Nene Hilario are also adept at forcing turnovers, so that Gallinari and Felton would combine to force many turnovers.  On the Knicks side, recall that offensive rebounding has positive synergies with itself.  Anthony and Billups are better offensive rebounders than Gallinari and Felton, and would combine better with Stoudemire and Jefferies, both of whom are solid offensive rebounders. 

21 


