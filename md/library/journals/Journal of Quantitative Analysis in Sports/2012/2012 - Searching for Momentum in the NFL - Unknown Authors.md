<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Searching for Momentum in the NFL - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1362 

## Searching for Momentum in the NFL 

**Michael J. Fry,** _University of Cincinnati_ **F. Alan Shukairy,** _University of Cincinnati_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1362 

## Searching for Momentum in the NFL 

### Michael J. Fry and F. Alan Shukairy 

### **Abstract** 

We examine the question of whether or not momentum exists in an NFL football game. The concept of momentum is often cited by coaches, players, commentators and fans as a major factor in determining the outcome of the game and, consequently, in-game decision making. To examine the existence of momentum, we analyze particular game situations tied to what we consider to be “momentum-changing plays” (MCPs). These MCPs include fourth down conversions/stops, turnovers and scores allowed. We hypothesize that evidence of positive (negative) momentum would be characterized by increases (decreases) in yards gained, higher (lower) probability of converting a first down and greater (lesser) likelihood of scoring after a positive (negative) MCP. Our data set includes all plays from the 2002 to 2007 NFL seasons. We limit our analysis to game situations where the outcome of the game is still in doubt by removing plays that occur when a team is facing an insurmountable score differential. We use a pairwise matching comparison where we control for the game situations of home/away team, field position, time of game and score differential. We find little evidence for the existence of momentum in these events. Our results are in line with previous papers that find little empirical evidence of momentum in sports. While our findings cannot conclusively disprove the existence of momentum in the NFL, they further support the argument that momentum should not be a guiding factor for in-game decision making. 

**KEYWORDS:** football, momentum, pairwise matching 

Fry and Shukairy: Searching for Momentum in the NFL 

### **1. Introduction** 

Sports writer Frank Deford defines momentum as “the most important thing in football, even if I’m not quite sure what exactly it is … As football announcers tell us, if a team has momentum, that is good. If it doesn’t, a team must get momentum” (Deford, 1999). The belief in momentum – that certain positive (negative) events during a game cause a team to do better (worse) subsequent to that event – seems to be nearly unanimous among those who speak or write about the game. Players, coaches and pundits frequently reference “changes in momentum” as defining points during a game that, in hindsight, seemed to assure victory or defeat. Usually, these “momentum-changing” plays are single events that are either unexpected (e.g., a crucial turnover during an NFL game) or moments of high drama (e.g., an unsuccessful fourth-down conversion attempt). These events often seem to pinpoint the moment at which a losing team began their comeback or else the winning team became assured of victory. 

However, it is often difficult for human perception to separate intrinsic changes in probability from simple random occurrences. Consider the gambler who believes that a slot machine has suddenly grown ‘hot’ or ‘cold’ even when the underlying algorithm provides the same probability of a payout at all times. More related to sports, the seminal article by Gilovich et al. (1985) provided evidence that sports players tend to incorrectly believe in ‘hot streaks’ that could simply be the result of random chance. We believe that the same may be true of the belief in momentum. Here, we wish to examine the question of whether or not certain events during a game can lead to changes in ‘momentum’. Specifically, we wish to search for evidence of changes in momentum caused by in-game events using data collected from the National Football League (NFL). 

First, we must define what exactly we mean by the term ‘momentum’. We believe that momentum gains (losses) should be evidenced by a team’s propensity to perform better (worse) after the momentum-gaining (losing) play. Three possible measures of momentum gains would be gaining more yards on the subsequent play, a higher probability of converting their next set of downs and higher likelihoods of scoring after the momentum-changing play. Similarly, momentum-losing plays should result in the converse of these effects. Next, we must isolate such ‘momentum-changing plays’. We choose to examine four such events that players, coaches and writers often seem to point out as momentumchanging events. These are: 1) successful fourth-down conversions; 2) unsuccessful fourth-down conversions; 3) turnovers; and 4) allowing scores (touchdowns and/or field goals). For each of these events, we compare a teams’ performance subsequent to the momentum-changing event to plays from a control data set. The comparison data set is selected using pairwise-matching to control for field position, score differential, time of game and for whether the team is home or away. In all of our comparisons, we consider only game situations where the outcome is still in some doubt; we discard any game situations that occur 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

when one team holds what we define – through examination of historical game results – as an insurmountable lead. 

Examining the existence, and effect, of momentum in the NFL is important for several reasons. As mentioned previously, many coaches subscribe to the belief and importance of momentum-changing events. According to Garafolo (2009), The New York Giants track all ‘sudden-change’ situations – interceptions, fumbles and turnovers on downs – since they are “moments that are often considered the most important for a defense because they can swing the momentum of an entire game.” Thus, coaches clearly take the existence of momentum into consideration when determining play calling. Several studies have criticized NFL coaches for being too risk averse (e.g., Romer, 2006). If momentum does exist, then this might give support to such risk-averse strategies that seek to prevent momentum-losing plays. Additionally, many quantitative analyses of American football such as Romer (2006) employ Markov decision process (MDP) models that require a memoryless property, thereby inherently assuming that momentum does not exist. 

We find possible statistical evidence of positive momentum gains for a team after successfully converting a fourth-down in the NFL. However, we find no statistical evidence for the existence of in-game momentum resulting from turnovers or allowing scores1. In fact, in many cases, the teams’ performance appears to counter the expected effects of changes in momentum. Our inconclusive evidence of the existence of momentum agrees with the findings of other researchers from a variety of sports. We conclude that in many instances, players, coaches and writers may put too much credence on the existence of momentum and that this may affect play-calling. Furthermore, our results lend validity to the use of MDP-type analysis to model American football. 

### **2. Literature Review** 

The popular media is rife with mentions of ‘momentum’ in sports. Many of these momentum effects are cited in such observations as win streaks, batting streaks in baseball and other multi-game situations. Albright (1992) and Frohlich (1994) examine batting streaks in baseball for evidence of momentum. Using a variety of statistical tests, these authors find no evidence that batting streaks supported the idea of momentum, noting that such streaks would be expected due to randomness in independent trials. Vergin (2000) investigates win streaks from both Major League Baseball and the National Basketball Association (NBA). The author again finds no statistical evidence of momentum in these win streaks even though 

> 1 This is not to minimize the importance of a turnover that, for instance, gives the home team 1st and 10 on the opponent’s 30 yard line, trailing by four points with 10:00 minutes left in the game. The absence of evidence for momentum only means that the outcome of the game situation should be no different than, for instance, had the home team arrived at the identical situation after a 50yard drive following a touchback. 

2 

Fry and Shukairy: Searching for Momentum in the NFL 

most sports participants and observers believe in such an effect. A recent paper by Arkes and Martinez (2011) examines momentum effects in the NBA over multiple games. The authors use econometric models and report strong evidence for a positive momentum effect over multiple games. This represents one of the first papers to find such an effect, but it differs from our study in that the authors are examining the effects of wins and losses over multiple games in the NBA whereas we are examining evidence of in-game momentum in the NFL. 

More similar to our work, other researchers have searched for in-game momentum. These works generally examine whether or not certain events within a game lead to the gain or loss of momentum in succeeding events during that game where success is taken to be a proxy for the evidence of positive momentum. Perhaps the most famous academic study on this subject is the examination of the “hot hand in basketball” (Gilovich et al. 1985). Here, the authors use data from the National Basketball Association as well as controlled experiments to examine the question of whether a basketball player making (missing) a shot influences their chances of making (missing) subsequent shots. The authors find no evidence that a shooter’s past success (or failure) in making a shot influences their abilities of making the next shot. However, the authors find through survey data that both fans and players believe that they are more likely to make the next shot if they made the previous one. Many researchers have followed up on this area with additional experiments and alternative analysis techniques. Much of this research is summarized in Bar-Eli et al. (2006), but we mention one particular study by Huizinga and Weil (2004) that examined a much bigger data set than Gilovich et al. (1985) and a recent study by Arkes (2010) that presents contrary findings. In Huizinga and Weil (2004), the authors find that players who had made a field goal tended to shoot more, but did not make a higher percentage of their shots. In other words, players exhibited a false confidence in momentum gains that were not confirmed through empirical evidence. However, Arkes (2010) finds possible evidence of the “hot hand” effect using more recent NBA data on free throws and different modeling methods. Using multivariate models with individual fixed effects, the author finds that players who make the first of two free throws have a significantly higher chance of making the second free throw. The author also finds possible correlations between previous free throw sets and the first of two free throws in a new set; however, the author finds no correlation between a made field goal and a subsequent free throw. 

Richardson et al. (1988) and Klaassen and Magnus (2001) examine momentum effects in tennis. Richardson et al. (1988) conduct player interviews and examine the correlation between winning specific games and winning the tennis match. Unsurprisingly, the authors find correlations between winning certain games and winning the match. Player interviews suggest that tennis players have widely differing views of the effects of psychological momentum in tennis. Based on their analysis, the authors suggest that “investigators be cautious 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

in inferring psychological momentum … psychological momentum seems to be a highly individual matter” (Richardson et al., 1988, page 69). Klaasen and Magnus (2001) find some possible positive momentum effects in that tennis players that win the previous point have a higher probability of winning the next point. They also find that tennis players find it more difficult to win an ‘important’ point. 

Psychologists have also attempted to define and measure “psychological momentum” in contexts broader than that of the sports world (e.g., Adler 1981). The general idea here is that experienced successes increase an individual’s belief in their ability to succeed while failures diminish this belief. Hence, the ebb and flow of these beliefs may be observed by changes in the probability of successive success and failures. Taylor and Demick (1994) describe a “momentum chain” where such experienced successes (or failures) lead to changes in behavior that then result in changes to successive outcomes. However, at best, the evidence of such psychological momentum in a broad range of contexts is split. While most studies find that participants firmly believe in changes of momentum, it is very difficult to find statistical evidence that supports this belief. 

Fewer researchers have examined in-game momentum specific to American football, even though this idea seems to be commonly held by observers, commentators, players and coaches.  Romer (2006) examines decision making on fourth-down in the NFL, finding that NFL coaches clearly deviate from optimal strategies. Romer includes a short mention of the effects of momentum in the NFL; the author identifies plays as either ‘very good’ (scoring a touchdown) or ‘very bad’ (e.g., turnovers) and examines what happens on the play immediately following. Romer finds “no evidence for momentum effects… from the situation immediately following a very bad play to the next, the team that lost possession does somewhat better than average” (Romer, 2006, page 358). This analysis closely matches some of our work presented here for short-term momentum effects after scores and turnovers. However, we utilize a larger data set and consider longer-term effects such as the probability of converting the subsequent first down and the probability of scoring. 

### **3. Analysis** 

We test for momentum by first isolating what we consider to be “momentumchanging plays” (MCPs). We then examine the subsequent performance of the team that is hypothesized to have either gained or lost momentum from these critical plays. Football provides a useful setting in which to test our hypotheses as football is made up of a sequence of discrete plays – some of which are believed to have a particularly strong effect on subsequent outcomes. The MCPs that we identify are: 1) fourth-down conversions (or failed conversion attempts); 2) turnovers; and 3) scores allowed – we will consider the effects of allowing both field goals and touchdowns. 

4 

Fry and Shukairy: Searching for Momentum in the NFL 

In order to identify the possible presence of momentum, we select several performance metrics. We compare a teams’ performance metrics after one of our defined MCPs with a base case value chosen by controlling for the relevant game factors. The performance metrics that we will examine in search of momentum are: 1) average yards gained on the play immediately after the MCP; 2) probability of converting the set of downs following the MCP; and 3) probability of scoring on the drive following the MCP. We believe that this gives several possible time-frames for momentum effects from the very-short term to longer term. The in-game variables we control for are those we believe could also impact our performance metrics. The control variables are 1) identification of the home team; 2) field position; 3) time remaining in the game; and 4) score differential. The details of our approach are described below. 

### **3.1.  Data Set** 

Our data set initially contains all NFL plays from the 2002 through 2007 seasons. This play-by-play data is imported from CBS Sports’ website2. Using web queries designed in Visual Basic for Applications, we input the play-by-play data for each of the 256 regular season games per season in the 2002 through 2007 seasons. These data are then combined in a Microsoft Access database and imported into SAS Version 9.1.3 for data cleansing, manipulation and analysis. Prior to cleansing, the database contains 249,423 play entries from 1,536 games. Of these 1,536 games, 75 are excluded for a variety of reasons such as play-by-play transcription errors that occur throughout the game, missing data (or obvious errors), and one game that ended in a tie. We then exclude some data on a possession-by-possession level, removing overtime possessions and those with obvious data entry errors. 

We also only want to consider plays where we believe the game’s outcome is still undecided. This is particularly important when we examine fourth-down conversion attempts. Therefore, we seek to exclude plays that occur once the score differential has reached what we consider to be an “insurmountable lead” for one of the two competing teams. The input variables we consider when determining whether or not the score differential has reached an insurmountable lead are: 1) the score differential; 2) time remaining in the game; 3) whether or not the leading team has possession of the ball. Similar work to identify insurmountable leads in basketball has been conducted by James (2008). 

Interestingly, we find that NFL games reach an insurmountable-lead state earlier and at a lower point threshold than many casual fans would guess. In order to quantify insurmountable leads, we first define a “game shift” as one of the following two situations: 1) the team with possession of the ball is currently trailing its opponent but goes on to win the game; 2) the team with possession of 

> 2 Example: http://www.cbssports.com/nfl/gamecenter/playbyplay/NFL_20060907_MIA@PIT 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

the ball is currently leading but goes on to lose the game. Table 1 displays the number of game shifts that are observed during the fourth quarter of all games in our data set. The score differential is shown on the vertical axis (from -21 to +21 points) and the elapsed game time (46:00 minutes to 1:00:00 indicating the fourth quarter) is shown on the horizontal axis. The darkly shaded region indicates situations that we believe exhibit an insurmountable lead. This includes all scenarios where no game shifts have occurred as well as three scenarios where one game shift occurred in our data set. We believe those three are sufficient outliers such that the trailing team was playing in a desperation mode and that game decisions (particularly going-for-it on fourth-down) are not reflective of true in-game strategy3. Therefore, we remove all possessions from our data set that 4 occur during insurmountable leads . 

### **3.2.   Analysis Method: Pairwise Matching** 

We use a pairwise matching procedure for our control selection. This type of analysis is common in epidemiological studies and clinical trials matching control subjects to patients on multiple variables (Kupper et al., 1981). We want to isolate the impact of MCPs on succeeding plays, drives and game results. In order to do so we will define several control variables: 1) whether the team is playing Home or Away; 2) the remaining game time; 3) the score differential; 4) field position. Since we believe that these are confounding variables to our measurement for the presence of momentum, we will pair each play from the test set to a play from the 

> 3 For instance, in Week 5 of the 2003 season, visiting team Indianapolis assumed possession of the ball with 4:54 remaining in the fourth-quarter (elapsed game time 56:00) trailing Tampa Bay by 21 points (14 to 35). Indianapolis went on to win 38-35 in overtime. It should also be noted that two of these three outliers involve Peyton Manning as QB. 

> 4 Aside from the three exception games, there were 971 games with at least one insurmountable possession. We exclude all remaining plays in a game from analysis once the margin has been classified as insurmountable, even if the losing team should come back to tie or take the lead. Inspecting all excluded possessions, we find five games where the team facing the insurmountable deficit managed to tie the game before going on to lose. Only one team, Houston, playing against Tennessee in Week 7 of the 2007 season, ever trailed after building an insurmountable lead. The Texans had one fourth-quarter possession where they trailed by one point before going on to win. 

6 

#### Fry and Shukairy: Searching for Momentum in the NFL 

Table 1: Displays “insurmountable” leads for an NFL game based on point differential and game time. Cell values represent the number of games where the trailing team ended up winning the game at that particular game time and score differential. Dark-shaded cells represent game time-point differential combinations that we classify as an “insurmountable” lead based on historical game results. 

|||||||Fourth Q|uarter Game|Time|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Score Difference|1:00:00<br>0:59:00|0:58:00|0:57:00|0:56:00|0:55:00|0:54:00|0:53:00|0:52:00|0:51:00|0:50:00|0:49:00|0:48:00|0:47:00|0:46:00|
|21|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|1|0|
|20|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|
|19|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**||**0**||**0**|**0**|**0**|0|0|
|18|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|
|17|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**1**|**0**|**0**|**0**|1|0|
|16|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|
|15|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**||0|0|
|14|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|2|1|1|0|0|1|
|13|**0**<br>**0**|**0**|**0**|**0**|**1**|**0**|**0**|1|1|1|1|0|0|1|
|12|**0**|**0**|**0**||**0**|**0**|**0**|0|0|0|0|0|0|0|
|11|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|1|0|0|0|0|
|10|**0**<br>**0**|**0**|**0**|**0**|1|3|1|1|0|1|1|2|5|2|
|9|**0**|**0**|**0**|**0**|0|0|0|0|0|1|0|1|0|1|
|8|**0**<br>**0**|**0**|**0**|2|1|0|1|1|2|0|0|0|0|2|
|7<br>|**0**<br>**0**<br><br>|1<br>|1<br>|1<br>|4<br>|3<br>|2<br>|3<br>|2<br>|1<br>|2<br>|3<br>|4<br>|4<br>|
|6|**0**<br>**0**|2|3|2|2|2|2|0|4|1|4|4|1|3|
|5|**0**<br>**0**|1|0|1|1|1|0|1|1|3|3|3||5|
|4|**0**<br>1|1|5|3|7|3|1|4|1|5|3|1|4|4|
|3|**0**<br>3|3|4|8|4|2|5|3|5|5|6|8|5|8|
|2|**0**<br>0|1|3|1|0|3|1|2|0|4|3|1|1|2|
|1|**0**<br>0|1|0|4|2|2|4|4|5|4|5|2|5|4|
|Tied|||||||||||||||
|-1|2<br>3|8|4|6|5|5|4|9|3|8|4|8|4|10|
|-2|2<br>4|2|4|4|0|1|1|5|4|3|2|1|1|6|
|-3|7<br>8|15|4|5|7|2|5|5|9|5|7|11|6|16|
|-4|0<br>5|8|9|6|1|6|5|3|6|4|10|5|7|7|
|-5|0<br>1|1|1|2|3|2|3|3|2|0|2|2|4|3|
|-6|1<br>2|5|3|1|4|1|1|3|3|5|2|1|3|3|
|-7|**0**<br>2|5|6|3|3|0|2|3|5|4|2|4|3|6|
|-8|**0**<br>**0**|1|3|0|0|1|0|2|1|0|1|1|0|2|
|-9|**0**<br>**0**|0|0|0|0|0|0|0|0|1|2|1|2|1|
|-10|**0**<br>**0**|2|2|2|0|2|2|1|2|3|2|0|4|3|
|-11|**0**<br>**0**|**0**|1|1|0|1|0|1|0|0|0|1|1|1|
|-12|**0**<br>**0**|**0**|0|0|0|0|0|0|0|0|0|0|0|0|
|-13|**0**<br>**0**|**0**|1|1|1|0|1|0|2|1|2|0|1|0|
|-14|**0**<br>**0**|**0**|**0**|**0**|2|1|2|1|1|1|0|2|0|3|
|-15|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|0|0|0|0|0|
|-16|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|1|0|0|0|0|0|0|
|-17|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|1|0|1|0|0|0|2|
|-18|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|0|0|
|-19|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**||0|0|
|-20|**0**<br>**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|0|1|0|
|-21|**0**<br>**0**|**0**|**0**|**1**|**0**|**0**|**0**|**0**|**0**|**0**|**0**|1|0|1|



7 

_Submission to Journal of Quantitative Analysis in Sports_ 

control set that best matches it based on these four controls. The control set is composed of all plays in our cleansed data set other than those affected by the MCPs. Note also that when we match plays from the test set and control set, we are always matching on the first downs. For instance, when examining average yards gained following a 4th down conversion, we will always be comparing average yards gained on the subsequent 1st down from the test set with average yards gained on 1st down in similar game situations from the control set. 

We follow the procedure explained in Travis et al. (1996). The best match here is determined using the nearest centroid sorting clustering technique (Anderberg, 1973). We define Home vs. Away as a categorical variable that must be matched exactly, and the other three variables, remaining game time, score differential and field position, as continuous variables that are equally weighted in our matching. Clusters of observations are formed around the MCP plays by minimizing the within cluster sum of squares (see Anderberg, 1973). A test set play may be unmatched if its best match from the control set has a superior match with a different play in the test set. We then perform control validation analyses on each of our comparisons. We find no strong evidence that the distributions of our MCP-affected game situations are different from our control game situation distributions. 

### **3.3. Momentum and Fourth-Down Conversion Attempts** 

We begin our analysis by examining fourth-down conversion attempts. There has been considerable recent media interest in coaches choosing to “go-for-it” rather than punt on fourth down. Historically, NFL teams on fourth down almost exclusively choose to punt or kick a field goal rather than attempt to pick up a first down. However, Bill Belichick, coach of the New England Patriots, famously eschewed this thinking and chose to go-for-it in the 2009 season when facing a fourth-and-two from his own 28 yard line (i.e., 72 yards from goal) with 2:08 remaining in the game and his team up by six points. There was immediate derision of Belichick’s decision from many in the sports media (e.g., King, 2009; Simmons, 2009; and others)5 – mainly because the Patriots failed to pick up the first down and they went on to lose the game. Interestingly, one of the factors used to argue both sides of Belichick’s decision is the effect it had on the teams’ momentum (e.g., see Howe, 2009; Frigo, 2009). Fourth-down conversion attempts are widely believed to be momentum-changing plays. Brian Billick, former NFL coach of the Baltimore Ravens characterizes fourth down attempts as: 

> 5 It should be noted that many analysts – particularly the more quantitative-types – later defended the decision as at least not “obviously wrong” and perhaps even the correct decision; see Burke (2009), Winston (2009) among others. 

8 

Fry and Shukairy: Searching for Momentum in the NFL 

Something big is going to happen. Either you're going to convert in a crucial situation that keeps a drive alive, that allows you to score, that makes a difference in the game, that gives your team a huge emotional lift. The reverse of that is you go for it, you take your chances, you get stoned and it's a huge emotional drain for your team (Garber, 2007). 

Therefore, we seek evidence of a team gaining (losing) momentum after a successful (unsuccessful) fourth-down conversion. We examine the three sources of potential evidence for positive momentum outlined earlier: 1) an increase in the average yards gained on the play immediately following the successful fourthdown conversion; 2) an increase in the probability of converting the following set of downs; 3) an increase in probability of scoring after the conversion. 

Our successful fourth-down conversion data set consists of 765 data points once plays that occur during an insurmountable score differential are removed. We then compare these to our matched controls. We are able to match 761 of the 765 conversions (99.5% matching rate). Table 2 displays the test and control averages for the matching variables following a fourth-down conversion. We find no statistical differences between test and control data sets for successful fourthdown conversions. The data support a game situation when a team would be likely to go-for-it on fourth down. Trailing by 3.8 points on average, the team needs a touchdown to retake the lead. Having a 1st down on the opponent 30-yard line means that the team faced a fourth down decision in the part of the field (between the opponent 30 and 35-yard lines) where a 47 – 52 yard field goal is challenging, and a punt could easily go into the end-zone, resulting in only a 10 – 15 yard change in field position. The average remaining game time for both data sets – only 4-minutes have elapsed in the second half – adds additional confidence that the decision to go-for-it was not made out of desperation. 52% of the teams who converted a fourth down were home teams in both the test and control data sets. 

Table 2: Summary of data set comparisons for successful fourth-down conversions. 

|**Variable**|**Test: After 4**<br>**th Down**<br>**Conversion**|**Control**|
|---|---|---|
|Count|761|761|
|Home Team Percentage|52.0%|52.0%|
|Score Differential|-3.8|-3.8|
|Remaining Game Time|26:02|26:05|
|Yards-to-Goal|30.2|30.2|



Table 3 displays the results for our three positive-momentum metrics after a successful fourth-down conversion. We perform simple _t_ -tests to compare yards 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

gained and look at 2 x 2 and 2 x 3 frequency tables to compare the conversion and possession probabilities, respectively. We see no statistically-significant differences for yards gained on the play following a successful fourth-down conversion or on the probability of scoring. However, in each case the observed values are moving in a way consistent with the existence of positive momentum. The strongest evidence of positive momentum comes from examining the probability of converting the next set of downs after a successful fourth-down conversion. Here we find that the difference is significant at the 0.10 level and that the probability of converting increases from 66.1% to 70.3%. Thus, we conclude that there may be evidence of positive momentum gains from successfully converting a fourth-down attempt. 

Table 3: Test for momentum effects after successful fourth-down conversion. Only the probability of converting the next set of downs is significant at the 0.10 level. 

|**Yards Gained on Pla**|**y After Conversion**|||
|---|---|---|---|
||Mean|Standard Error|p-value|
|After Conversion|4.49|0.29|031|
|Control|4.07|0.30|.|
|**Probability of Conve**|**rting Downs After Con**|**version**||
||Prob(Convert)||p-value|
|After Conversion|70.3%||008|
|Control|66.1%||.|
|**Probability of Scorin**|**g After Conversion**|||
||Field Goal|Touchdown|p-value|
|After Conversion|23.8%|44.8%|030|
|Control|21.9%|43.0%|.|



However, we must also point out some potential limitations in our analysis. We use point differential as a matching variable in part to control for differences in team strengths. However, this may not accurately reflect such differences at all points in a game. Clearly earlier in the game the score 6 differential will be a less accurate proxy for the relative strengths of the team . Thus, it could still be the case that the stronger team tends to go-for-it more often since they should expect a higher chance of converting. By examining successful fourth-down conversion we may be biasing our analysis to looking at matchups between a stronger team and a weaker team. This could explain the higher probabilities for converting the following set of downs, as well as the directional advantage seen in yards gained and probability of scoring. 

Next we examine the opposite scenario: one team attempts a fourth-down conversion, but is unsuccessful in its attempt. We characterize such scenarios as 

> 6 However, we also examined the teams in the control set and the test set based on final game outcomes (margin of victory), and we found no statistically-significant differences between the teams in the two sets. 

10 

Fry and Shukairy: Searching for Momentum in the NFL 

“fourth-down stops.” We are able to match 529 of the 530 fourth-down stops in our data set (99.8%). Table 4 displays the test and control averages for the matching variables following a fourth down stop. Again, statistical tests indicate that we cannot conclude that there are any significant differences between the distributions for our test and control samples. 

Table 4: Summary of data set comparisons for fourth-down stops. 

|**Variable**|**Test: After 4**<br>**th Down**<br>**Stop**|**Control**|
|---|---|---|
|Count|529|529|
|Home Team Percentage|46.9%|46.9%|
|Score Differential|3.6|3.6|
|Remaining Game Time|27:41|27:42|
|Yards-to-Goal|66.6|66.5|



Table 5 displays the results of our analysis for fourth-down stops. Note that here we are measuring the yards gained, probability of conversion and probability of scoring for the team that has successfully _stopped_ the other team from converting (i.e., the team playing defense during the conversion attempt). Thus, positive momentum would still be reflected by an increase in our metrics. However, Table 5 shows that we do not see statistically-significant evidence of momentum gains after a fourth-down stop. In fact, the yards gained and the probability of converting the next set of downs both decrease in relation to the control group. This is similar to Romer’s (2006) finding that the team on the perceived momentum-losing side of the MCP actually performs slightly better after the momentum-changing event. However, none of these differences in our study are statistically significant. 

Table 5: Test for momentum effects after fourth-down stop. We find no significant momentum effects from fourth-down stops. 

|**Yards Gained on**|**Play After 4**<br>**th-Down Stop**<br><br>||
|---|---|---|
||Mean<br>Standard Error|p-value|
|After Stop|5.06<br>0.40|037|
|Control|5.58<br>0.43<br>|.|
|**Probability of Co**|**nverting Downs After 4**<br>**th-Down Stop**||
||Prob(Convert)|p-value|
|After Stop|62.9%|022|
|Control|66.5%<br>|.|
|**Probability of Sco**|**ring After 4**<br>**th-Down Stop**||
||Field Goal<br>Touchdown|p-value|
|After Stop|15.5%<br>18.7%|037|
|Control|13.8%<br>18.2%|.|



11 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **3.4.   Momentum and Turnovers** 

We next examine momentum effects and turnovers in the NFL. After data cleansing, we are able to match 3,244 of the 3,280 observations of turnovers (98.9% match rate). Table 6 displays the test and control averages for the matching variables following a turnover, once again not finding any differences between the distributions. The average value for each of the metrics however is close to the midpoint of each metric: 50.8% of the teams are home teams, the score differential is +1.6, the average game time is less than 2 minutes remaining in the first half, and the average field position is close to the 50-yard line (48.9). This seems to support the widely-held belief that turnovers happen largely randomly. 

Table 6: Summary of data set comparisons for possession following a turnover. 

|**Variable**|**Test: After Turnover**|**Control**|
|---|---|---|
|Count|3244|3244|
|Home Team Percentage|50.8%|50.8%|
|Score Differential|1.6|1.6|
|Remaining Game Time|31:22|31:20|
|Yards-to-Goal|48.9|48.9|



The momentum results appear in Table 7. Again we find no statistical evidence of the existence of changes in momentum as measured by the result of the following play, set of downs, or possession. As with fourth-down stops, our metrics apply to the team receiving the turnover, so we would expect values to go up if there was a positive impact due to a momentum gain for causing a turnover. Directionally, the test group had greater yardage gained and a higher probability of conversion than the control, but these differences are not statistically significant. Further, the scoring results of the possession following a turnover are nearly identical for the test and control data sets. Thus, we find no statisticallysignificant evidence of momentum from turnovers. Even if there is a momentum effect, then it is short lived and does not lead to a higher probability of scoring. 

12 

Fry and Shukairy: Searching for Momentum in the NFL 

Table 7: Test for momentum effects after a turnover. We find no significant momentum effects from turnovers. 

|**Yards Gained on Pla**|**y After Turnover**|||
|---|---|---|---|
||Mean|Standard Error|p-value|
|After Turnover|4.97|0.15|042|
|Control|4.80|0.15|.|
|**Probability of Conve**|**rting Downs After Tur**|**nover**||
||Prob(Convert)||p-value|
|After Turnover|69.0%||011|
|Control|67.1%||.|
|**Probability of Scorin**|**g After Turnover**|||
||Field Goal|Touchdown|p-value|
|After Turnover|23.2%|30.6%|> 099|
|Control|23.2%|30.6%|.|



### **3.5.   Momentum and Scoring** 

In this section we look for evidence of negative changes to momentum after allowing an opponent to score. We first examine the case where the opponent scores either a TD or a FG. Here we are only able to match 5,636 of the 8,329 possible observations of a team receiving the ball after an opponent scores (67.7% match rate). The lower match rate is due to the fact that here we are looking for matches to plays immediately following a score.  The ensuing drives start after a kickoff return; most such drives start with similar field position. This limits the possible matches in our control set on the yards-to-go dimension. 

In Table 8, we see that the average field position is around 70 yards-togoal. The differences in yards-to-goal, score differential and remaining game time are all statistically significant; however, this is likely due to the large data sets used here and is not practically significant. 

Table 8: Summary of data set comparisons for possessions after allowing an opponent score. 

|**Variable**|**Test: After Allowing**<br>**Score**|**Control**|
|---|---|---|
|Count|5636|5636|
|Home Team Percentage|49.0%|49.0%|
|Score Differential|-4.0|-3.2|
|Remaining Game Time|30:00|27:58|
|Yards-to-Goal|71.8|70.8|



The results of our analysis appear in Table 9. The yards gained here is measuring the average yards gained on first down by the team that received the kickoff following the opposing team’s score. Likewise, the probability of converting downs applies to the first set of downs following the kickoff. We see 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 

virtually no change in the average yards gained or probability of scoring after allowing a score. There is actually a slight increase in the probability of converting the next set of downs after an opponent score. This further directionally supports the counter-intuitive findings of Romer (2006), but again this finding is not statistically significant. 

Table 9: Test for momentum effects after allowing an opponent score. We find no significant momentum effects from allowing an opponent score. 

|**Yards Gained on Play A**|**fter Opponent Scor**<br>|**es**<br>||
|---|---|---|---|
||Mean|Standard Error|p-value|
|After Opponent Score|5.69|0.13|084|
|Control|5.66|0.13|.|
|**Probability of Convertin**|**g Downs After Opp**|**onent Scores**||
||Prob(Convert)||p-value|
|After Opponent Score<br>Control|68.1%<br>67.2%||0.30|
|**Probability of Scoring A**|**fter Opponent Scor**|**es**||
||Field Goal|Touchdown|p-value|
|After Opponent Score|12.7%|18.4%|093|
|Control|12.7%|18.2%|.|



Next we limit our test set only to situations where the opponent has scored a touchdown. This allows us to include the situations where the opponent just scored a field goal as part of the control set. This improves our matching rate to 80% (3,997 out of 4,992). Similar to our previous score comparison, there is a statistical difference between the groups for score differential and remaining game time (Table 10). These statistically-significant differences are again due to the large sample size and are not practically significant. 

Table 10: Summary of data set comparisons for possessions after allowing an opponent touchdown. 

|**Variable**|**Test: After Allowing**<br>**TD**|**Control**|
|---|---|---|
|Count|3997|3997|
|Home Team Percentage|47.5%|47.5%|
|Score Differential|-5.2|-4.6|
|Remaining Game Time|30:21|28:23|
|Yards-to-Goal|71.8|71.5|



Table 11 shows our analysis results. Once again, none of the results are statistically significant. Table 11 indicates that even when comparing only scores of a touchdown, there does not appear to be any strong evidence of momentum loss after an opponent scores. 

14 

Fry and Shukairy: Searching for Momentum in the NFL 

Table 11: Test for momentum effects after allowing an opponent touchdown. We find no significant momentum effects from allowing an opponent touchdown. 

|**Yards Gained on Play**|**After Opponent Score**<br>|**s TD**<br>||
|---|---|---|---|
||Mean|Standard Error|p-value|
|After Opponent TD|5.53|0.15|026|
|Control|5.78|0.16|.|
|**Probability of Converti**|**ng Downs After Opp**|**onent Scores TD**||
||Prob(Convert)||p-value|
|After Opponent TD<br>Control|67.6%<br>66.9%||0.50|
|**Probability of Scoring**|**After Opponent Score**|**s TD**||
||Field Goal|Touchdown|p-value|
|After Opponent TD|12.6%|18.7%|097|
|Control|12.6%|18.5%|.|



### **4. Conclusions** 

In this work we have tried to establish the existence of in-game momentum in the NFL. To do so, we examine particular game situations tied to what we consider to be “momentum-changing plays” (MCPs).  These MCPs represent plays that are commonly believed by coaches, players, commentators and fans to affect the momentum of a game. We hypothesize that evidence of positive (negative) momentum would be characterized by increases (decreases) in yards gained, higher (lower) probability of converting a first down and greater (lesser) likelihood of scoring after a positive (negative) MCP. We use a pairwisematching comparison where we control for the game situations of home/away team, field position, time of game and score differential. 

We find very little evidence of momentum in our study. Out of all of our tests, the only statistically-significant result indicates that teams may have a higher probability of converting their next series of downs after a successful fourth-down conversion than in our control data set. However, we characterize this as weak evidence of momentum, and we point out that a limitation of our study is that our proxy (score differential) for differences in team strengths is not perfect and this could possibly mitigate this finding. Otherwise, we find no evidence of momentum changes from fourth-down conversions/stops, turnovers, and allowing scores. 

We must also point out several additional limitations in our study of momentum in the NFL. It is possible that changes in momentum are not attributable to discrete events as we test for in this paper, but that momentum can be thought of as a limited continuous quantity that is traded back-and-forth by the competing teams during the course of a game. In such a case, our tests for momentum based on defined momentum-changing plays may be insufficient. 

15 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

However, this would seem counter to the popular notion of momentum described by coaches, players, fans and the media in the NFL where exact plays and events are often cited as the cause of a significant gain or loss of momentum. We also caution that as Huizinga has stated, “… if you look at something statistically and don’t find it, that doesn’t mean it doesn’t exist” (Ma, 2010). While we find little evidence of momentum in the NFL, this does not definitively prove that it does not exist. It is possible that we are still not correctly characterizing the causes and effects of momentum. However, when our study is added to the existing literature on momentum in sports, it adds additional credence to the claim that momentum could be more of a perception than reality. 

### **References** 

Adler, P. _Momentum: A Theory of Social Action_ . Sage Publications, Inc., Berkeley, CA, 1981. 

Albright, C. “Streaks and Slumps.” _OR/MS Today_ , 94-95. 1992. 

Anderberg, M. R., _Cluster Analysis for Applications_ , Academic Press, Inc, New York, NY, 1973. 

Arkes, J. “Revisiting the Hot Hand Theory with Free Throw Data in a Multivariate Framework,” _Journal of Quantitative Analysis in Sports_ , 6:1, 2010. 

Arkes, J., and J. Martinez. “Finally, Evidence for a Momentum Effect in the NBA,” _Journal of Quantitative Analysis in Sports_ , 7:3, 2011. 

Bar-Eli, M., S. Avugos and M. Raab. “Twenty Years of ‘Hot Hand Research: Review and Critique.” _Psychology of Sport and Exercise_ . 7:6, 525-553, 2006. 

th Burke, B. “Belichick’s 4 Down Decision vs the Colts,” _Advanced NFL Stats_ . Posted November 16, 2009. Available at: <u>http://www. advancednflstats.com /2009/11/belichicks-4th-down-decision-vs-colts.html.</u> 

Deford, F. “Momentum Gains Momentum.” _CNNSI.com_ . Posted February 3, 1999. Available at: <u>http://sportsillustrated.cnn.com/inside_game/deford/990127</u> 

Frigo, F. “The Anatomy of a (Fourth-Down) Decision.” _The Fifth Down: The New York Times N.F.L. Blog_ , Posted November 25, 2009. Available at: <u>http://fifthdown.blogs.nytimes.com/2009/11/25/the-anatomy-of-a-fourth-downdecision/.</u> 

Frohlich, C. “Baseball: Pitching No-hitters.” _Chance_ . 7:3, 24-30. 

16 

Fry and Shukairy: Searching for Momentum in the NFL 

Garafolo, M. “NY Giants Know They’re Capable of Stopping Opponents’ ‘Sudden Change’ Momentum.” _NJ.com_ . Posted September 19, 2009. Available at: <u>http://www.nj.com/giants/index.ssf/2009/09/ny_giants_know_theyre_capable.htm l</u> 

Garber, G. “Momentum is Key in Fourth-Down Decisions,” _ESPN.com_ , Posted October 31, 2007. Available at: <u>http://a.espncdn.com/nfl/columns/garber_greg /1453768.html.</u> 

Gilovich, T., R. Vallone and A. Tversky. “The Hot Hand in Basketball: On the Misperception of Random Sequences.” _Cognitive Psychology_ . 17, 295-314, 1985. 

Howe, J. “Patriots Standing Behind Bill Belichick’s Fourth-Down Decision,” _NESN.com_ . Posted December 9, 2009.Available at: http://www.nesn.com/2009/12 <u>/patriots-standing-behind-bill-belichicks-fourthdown-decisions.html,</u> 

Huizinga, J. and S. Weil. “Hot Hand or Hot Head? Overconfidence in Shot Making Ability in the NBA.”  2004. Available at: http://web.me.com/sandy1729 <u>/sportsmetricians_consulting/Hot_Hand_files/HH_Draft_v04.pdf</u> 

James, B. “The Lead Is Safe: How to tell when a college basketball game is out of reach.” _Slate.com_ . 2008. Available at: <u>http://www.slate.com/id/2185975/.</u> 

Klaassen, F. J. G. M. and J. R. Magnus. “Are Points in Tennis Independent and Identically Distributed? Evidence from a Dynamic Binary Panel Data Model.” _Journal of the American Statistical Association_ . 96, 500-509, 2001. 

King, P. “No Matter Which Way you Dissect It, Bill Belichick Made the Wrong Call,” _Monday Morning Quarterback_ at CNNSI.com. Posted November 16, 2009.Available at: http://sportsillustrated.cnn.com/2009/writers/peter_king/11/15/ <u>mmqb/ index.html.</u> 

Kupper, L. L., J. M. Karon, D. G. Kleinaum, H. Morgenstern and D. K. Lewis. “Matching in Epidemilogical Stuides: Validity and Efficiency Considerations,” _Biometrics_ , 37, 271-291, 1981. 

Ma, J. _The House Advantage_ . Palgrave Macmillan. New York, NY. 2010. 

Richardson, P. A., W. Adler and D. Hankes. “Game, Set, Match: Psychological Momentum in Tennis.” _The Sports Psychologist_ . 2, 69-76, 1988. 

Romer, D. “Do Firms Maximize? Evidence from Professional Football.” _Journal of Political Economy_ . 114:2, 340-365, 2006. 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

Simmons, B., “Belichick’s Fourth-and-Reckless,” _ESPN Page 2_ . Posted December 4, 2009. Available at: <u>http://sports.espn.go.com/espn/page2/story? page=simmonsnflpicks/091120.</u> 

Taylor, J. and A. Demick. “A Multidimensional Model of Momentum in Sports.” _Journal of Applied Sport Psychology_ . 6, 51-70, 1994. 

Travis, K. A., S. Arndt and N. C. Andreasen. “Pairwise Matching of Sample and Control Groups using PROC FASTCLUS,” _SAS Conference Proceedings: SAS Users Group International 21_ . 1996. Available at: <u>http://www.lexjansen.com /sugi/sugi21/po/183-21.pdf.</u> 

Winston, W. “Belichick Made the Right Call,” _The Huffington Post_ . Posted - November 16, 2009. Available at: <u>http://www.huffingtonpost.com/wayne winston/belichick-made-the-right_b_358871.html.</u> 

18 


