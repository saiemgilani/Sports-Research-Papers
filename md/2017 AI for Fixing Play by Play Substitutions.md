<!-- source: 2017 AI for Fixing Play by Play Substitutions.pdf -->



# **Using AI to Correct Play-by-play Substitution Errors** 

### Steven Wu and Tim Swartz 

Simon Fraser University Email: swa157@sfu.ca, tim@stat.sfu.ca 

## **1. Introduction** 

The sophistication of analytics in the basketball community is at an all-time high due to the availability of spatio-temporal data in the NBA that is driving innovation. A significant proportion of the cutting edge research showcased in recent years of MIT SSAC is enabled by camera software that allows for tracking individual players and the ball. However, the cost of the camera software required to record this data is too high for virtually any basketball league other than the NBA. For those such leagues, the most common and acquirable granular data is play-by-play, which is manually recorded by scorekeepers. This method is inexpensive, as the only costs are for human labour and (optionally) software that assists the recording. For the uninitiated, play-by-play is a log that contains the details of the sequence of events (e.g.: steals, turnovers, shot attempts) that occur in a game of sport. 

It was not too long ago when basketball’s cutting edge analytics were derived from play-by-play data [1]. Smaller leagues that do not have the budget for tracking software, but which produce playby-play, should be able to enjoy the same level of analytical discourse that the NBA has had. Access to these analytics improve coaching strategy, roster management, and fan engagement. However, the problem of smaller budgets is a compounding one that affects the quality of the play-by-play itself: the less money that the league has to spend on the data collection, the less reliable the data is with respect to the true events that occurred in the game. 

An example of this problem is the data from the U Sports (formerly known as the Canadian Interuniversity Sport, or CIS) league, which will be the league analyzed throughout the rest of this paper. Specifically, smaller budgets affect the following factors that have a large influence on the data’s resulting quality: 

- software to assist in annotation: a keyboard software that maps shortcuts for event annotations presents the opportunity for mistakes made by mistyping keys 

- wage: keepers are not paid like industry data entry professionals, and are usually students whose primary incentives and motivations to work are their interest in the sport 

- training: there is no standardized training across the keepers for each school, leading to high variance in consistency and reliability of the keepers across schools 

Carleton University’s men’s basketball team, winners in 12 of the past 14 years in the U Sports league [2,3] - and still hungry for any edge it can gain over its opponents – were interested in the impact of specific units of players deployed. Methods that can answer such a question, such as With Or Without You (WOWY) or adjusted plus-minus, are dependent on knowing which ten players are on the court at all times during the course of the game. It was found to be impossible to get sensible results using these proven methodologies because it relied on the play-by-play’s substitution logs being accurate. An automated solution that can “clean” the play-by-play’s substitutions to guarantee 





2017 Research Papers Competition Presented by: 

1 



five players on each side of the court at all times is necessary – one that can suggest the five most likely players on the court that matches close to the reality of the game that occurred is ideal. 

In this paper, we present a novel implementation of an artificial intelligence agent which uses the contextual data surrounding the substitutions to reliably infer who is actually on the court, guaranteeing five players on the court for each team at all times. Because the goal state of our AI agent is unknown (without watching film of games to verify the correctness of the recorded playby-play substitutions) we define two performance measures that quantify the success of our agent. Using over 6000 games from the U Sports league, we discuss the results of our framework for automated play-by-play cleaning. 

## **2. Data** 

U Sports, which has 40+ participating universities across Canada for both the men’s and women’s league, has published their game data online every year since the 2009-2010 season. The data collected for this paper is six seasons of the publicly available play-by-play and boxscore data. For every game, one group of workers are responsible for recording the play-by-play and another group of workers are responsible for recording the boxscore tallies. 

The logging of substitutions in the play-by-play data is where we see the largest inconsistency in quality, with a variety of problems that occur repeatedly: 

- recording an unequal number of players entering the game vs. going to the bench 

- player’s substitution patterns not alternating between entering the game vs. going to the bench (i.e.: a player is marked as going to the bench, then the next substitution involving him is him going to the bench again) 

- recording the wrong player name, or not recording a name at all, in the substitution event 

- missing substitutions (most frequently between quarters, but mid-quarter substitutions too) 

- inconsistency between the recorded substitution and the events recorded before/after (e.g.: “DOE,JOHN goes to the bench” followed by “DOE,JOHN made layup”) 

- some games in each season have no substitutions recorded at all 

The play-by-play has four columns: timestamp, away team plays, score, and home team plays. The recorded events are: goes to the bench, enters the game, foul, turnover, steal, block, defensive or offensive rebound, and made or missed 2-pt jumpshot/3-pt jumpshot/layup/dunk/free throw/tip in. An example of the play-by-play and a sample of the errors are below in Figures 1 and 2. 





2017 Research Papers Competition Presented by: 

2 





**_Figure 1: An example of substitutions with no names. 201411121 StFX vs. UNB_** 



**_Figure 2: An example of uneven substitutions. 20160122 Laval vs. Bishops_** 

To aid our discussion, we will define terms that will repeatedly come up in the next sections: 

- **stoppage:** the play-by-play row index where the clock is stopped and a substitution is permissible 

- **substoppage:** the play-by-play row index where a stoppage in play occurs and at least one substitution was recorded in the play-by-play 

- **active play:** a recorded play performed by a player that is not a substitution or technical foul 

**_Table 1: The frequency of errors we can objectively identify without cross-referencing the data with video_** 

|**Season**|**#**<br>**games**|**#**<br>**games**<br>**w/ 0**<br>**subs**|**Avg # sub**<br>**stoppages**|**Avg #**<br>**subs**|**Avg #**<br>**unequal**<br>**substoppages**|**Avg # non**<br>**alternating**<br>**subs**|**Avg #**<br>**missing**<br>**playername**<br>**subs**|
|---|---|---|---|---|---|---|---|
|**2009**|798|112|39.71|115.30|2.87|55.46|0.000|
|**2010**|828|48|43.75|126.24|2.75|60.88|0.002|





2017 Research Papers Competition Presented by: 



3 



|**2011**|829|43|42.45|122.87|2.70|59.12|0.008|
|---|---|---|---|---|---|---|---|
|**2012**|883|23|43.68|127.42|2.66|61.00|0.003|
|**2013**|911|1|44.45|129.34|2.69|61.29|0.015|
|**2014**|895|1|44.64|129.52|3.09|62.12|0.102|
|**2015**|905|1|44.30|130.10|2.30|62.35|0.107|
|**Totals**|**6049**|**229**|**43.35**|**126.04**|**2.72**|**60.41**|**0.035**|



## **3. Automatically Cleaning Play-by-play Substitutions** 

#### **3.1. Artificial Intelligence Techniques** 

In general, an agent is an entity with sensors to perceive its environment and actuators to act upon its environment. The computer representation, or model, of the environment at a given point in time is called the state. A utility-based agent uses a utility function (or heuristic) to map the current state to the utility of the state, and behave in a goal-directed manner to maximize its utility. The goal state of an artificial intelligence agent is either known (and the search is directed toward finding it) or the goal state is unknown (and the search is an exploration to try and find it, or the best possible solution if not the true solution). 

Our goal state is the play-by-play which has the correct substitutions recorded to reflect the substitutions in the game that actually occurred. In our case, it is unknown – the only way to obtain it is to watch the game’s film, which is not a feasible task given how many games there are in a season. In our case, we want the best approximation to the truth. Below we describe how we model the agent’s environment and the heuristic functions it uses to move from state to state. 

We can break our problem of cleaning a game into sub-problems of cleaning the substitutions of each period. For each period, we can further partition the play-by-play by its substoppages. Formally, ( % % denote the whole game’s play-by-play as ℙ= ∪%&' 𝑃* , where 𝑃* , is period _j_ ’s play-by-play containing _n_ rows. For each period _j_ , there is a set of substoppages 𝕤<sup>%</sup> = {𝑠𝑠', … , 𝑠𝑠0} (for periods that do not have recorded substitutions attempting to account for transactions of players, i.e.: if _ss1_ != 0, we add 0 to the set). Recall that each substoppage refers to the row index where substitution occurs, so we also have a substitution map for period _j_ , 𝕊<sup>%</sup> , which maps substoppages to the substitutions observed at that substoppage. 

The initial state is the play-by-play received, with the set of current players in the game 𝜔= ∅.  The actions the agent performs are removing a recorded substitution or imputing a substitution that it believes should have been recorded, at each substoppage. For each period _j_ , the agent iterates through each substoppage _ssk_ ∈𝕤<sup>%</sup> . We assign a confidence score to each recorded substitution found in 𝕊<sup>%</sup> [ _ssk_ ] based on the contextual evidence and discard those substitutions which do not pass the classification threshold. If there are any correct substitutions, it updates 𝜔 by removing the players recorded as going to the bench and inserting the players recorded as entering the game. 



2017 Research Papers Competition Presented by: 



4 



% The agent uses 𝑃* [𝑠𝑠7: 𝑛] (where the 𝑃[𝑞: 𝑟] notation means the play-by-play from row index _q_ until row index _r_ ) to assign an activity score to every player and infer who the five most likely players are on the court for each side. Once all of the periods and substoppages are iterated through exactly once, the agent is finished its task. 

From surveying the data and common errors, substitution plays cannot be trusted as much as the active plays. Intuitively, it is easier as a record keeper to assign the correct player to a single action involving the ball during a live play than to correctly account for up to ten players substituting for each team. Given this, we can use the active plays as contextual data at each substoppage in the game to infer what player transactions were most likely to have actually occurred. Specifically, for each substoppage, we have two problems that we need solutions for: 

(1) remove the recorded substitutions that show enough evidence of being incorrect (detailed in **Section 3.2** ) 

(2) given the remaining substitutions, infer and impute the substitutions that should have been recorded, ensuring five unique players are on for each team ( **detailed in Section 3.3** ) 

#### **3.2. Binary classification of recorded substitutions** 

An important task for our agent is to accurately classify whether a recorded substitution correct or not, only using the context of the play-by-play surrounding it. A natural question from coaching staff is: how close is the resulting mutated game to the truth? Thus, it is desirable for our system to improve with examples of play-by-play that have had the substitutions annotated carefully by a separate party. 

To train our classifier, we obtained five video replays of full games featuring distinct teams from the 2015-2016 men’s season, which had commentators and a running score count on the video feed. For each game, we recorded which players were actually on the court for each row of the play-byplay. Knowing the true five players on the court for each side, we were able to deduce which substitutions were recorded correctly or incorrectly. Features that we believed to be predictive in whether a substitution is recorded correctly or not were collected for each substitution from the annotated games, and are detailed in the following subsection. 

The resulting dataset is 312 “enters the game” substitutions and 311 “goes to the bench” substitutions. 76.1% of the “enters the game” substitutions and 76.8% of the “goes to the bench” substitutions were correct. 

#### **3.2.1. Extracted Features** 

Using domain expertise from conversing with coaches, play-by-play record keepers, and from our own knowledge of the data, for each substitution _si_ in 𝕊<sup>%</sup> [ _ssk_ ] for substoppage _ssk_ we extract the following features for our model: 

**_Table 2: Description of extracted features for every recorded substitution in our dataset_** 

|**Notation**|**Name**|**Explanation**|
|---|---|---|
|𝑌>|Correct/incorrect substitution|Our response variable. The value is 1 when the<br>recorded substitution_si_is correct.|
|𝑋',>|Absolute difference of # in vs. # out<br>for team of player in_si_|Int. From 0 to 5. If𝕊<sup>%</sup>[_ssk_] contains an unbalanced<br>number of players entering and leaving, then all|





2017 Research Papers Competition Presented by: 



5 



|||substitution’s likelihoods of being correct should<br>be equally“punished”|
|---|---|---|
|𝑋@,>|Total number of substitutions for<br>team of player in_si_|Int. From 1 to 10. The higher the number of<br>substitutions that a record keeper has to track for<br>the team on this substoppage, the more<br>opportunityfor mistakes|
|𝑋A,>|More than five substitutions of the<br>same type for team ofplayer in_si_|Boolean. Like𝑋', a signal that the score keepers<br>made a mistake and that_si _is likelyincorrect|
|𝑋B,>|Is beginning of quarter|Boolean. It is not a practice consistent among<br>scorekeepers to record the transactions occurring<br>between periods, and even if they are recorded,<br>they are either wrong or redundant (recording a<br>player entering who was already last recorded as<br>entering)|
|𝑋C,>|Previous substitution is opposite|Boolean. Whether the most recent previous<br>substitution with the player’s name is opposite to<br>the type in_si_|
|𝑋D,>|Next substitution is opposite|Boolean. Whether the most recent next<br>substitution with the player’s name is opposite to<br>the type in_si_|
|𝑋E,>|Player appears more than once in<br>substoppage|Boolean. Whether the player appears more than<br>once in𝕊<sup>%</sup>[_ssk_]|
|𝑋F,>|Plays before ratio|Float. This is the ratio of player activity before the<br>substoppage (in𝑃*<br>%[𝑠𝑠7G': 𝑠𝑠7]). The numerator is<br>the sum of active plays seen by the player in the<br>substitution, and the denominator is the number of<br>total active plays by the player’s team. A small<br>adjustment of 1.0 is added to both the numerator<br>and denominator in cases where the denominator<br>is 0.|
|𝑋H,>|Plays after ratio|Same as𝑋F,>, except after the substoppage (in<br>𝑃*<br>%[𝑠𝑠7: 𝑠𝑠7I']).|



#### **3.2.2. Model for Classification** 

We use a logistic regression model for our classifier for the interpretability of the coefficients, the probabilistic framework (which allows us to adjust the classification thresholds), and the strong performance relative to the other classifiers we tried. 

Since the coefficients vary drastically depending on the type of substitution (intuitively, for a “enters the game” substitution we do not want to see any active plays before the substitution and we do want to see active plays afterwards – and vice versa for “goes to the bench”), we train a separate model for each substitution type using the same predictors. 

Thus our model for a substitution _i_ ’s of type _t_ correctness is: 

𝑃 𝑌> = 1 = 𝜎(𝑋M + 𝛽'𝑋',> + 𝛽@𝑋@,> + 𝛽A𝑋A,> + 𝛽B𝑋B,> + 𝛽C𝑋C,> + 𝛽D𝑋D,> + 𝛽E𝑋E,> + 𝛽F𝑋F,> + 𝛽H𝑋H,>)) QRS T where 𝜎 𝑋 = 

'IQRS (U) 





2017 Research Papers Competition Presented by: 

6 



#### **3.2.3. Experiment Results** 

|**Variable**|**Coefficient**|
|---|---|
|𝑋',>|-0.774|
|𝑋A,>|-0.875|
|𝑋B,>|1.153|
|𝑋C,>|0.045|
|𝑋D,>|-1.702|
|𝑋E,>|-0.284|
|𝑋F,>|0.320|
|𝑋H,>|-1.872|
|**10 CV score**|88.0%|



|**Variable**|**Coefficient**|
|---|---|
|𝑋',>|-0.906|
|𝑋A,>|-0.568|
|𝑋B,>|0.786|
|𝑋C,>|-0.149|
|𝑋D,>|-1.072|
|𝑋E,>|-0.182|
|𝑋F,>|-3.234|
|𝑋H,>|0.283|
|**10 CV score**|89.2%|



**_Table 3: Coefficients and 10 CV classification score for "goes to the bench" substitutions_** 

**_Table 4: Coefficients and 10 CV classification score for "enters the game" substitutions_** 

As expected, our coefficients indicate decreasing likelihood of a correct substitution if there is an unbalanced number of substitutions recorded, if the substoppage is at the beginning of the quarter, and if the player appears more than once in the same substoppage. Our intuition for a relationship existing between the number of substitutions recorded and the probability of a substitution being a successful recording seems to hold from the data as well. 

Note that 𝑋@,> was excluded from the results table due to lack of examples of substoppages with more than five substitutions of either type in our limited dataset. 

#### **3.3. Inferring substitutions that should have been recorded** 

After confidently determining which substitutions are incorrect, we discard them. Applying the remaining substitutions on 𝜔, we are left with either less than, exactly, or more than five players % in 𝜔. In all cases, we are interested in knowing who are the most active players from 𝑃* [𝑠𝑠7: 𝑠𝑠7I']. 

The “enters the game” substitutions not recorded by the record keepers are easily inferred by % sudden activity of a new player in 𝑃* [𝑠𝑠7: 𝑠𝑠7I'] who is not in 𝜔. Active plays, especially numerous counts, are almost sure indicators that a player is on the court. However, a lack of active plays does not necessarily mean the player is on the bench. As the period progresses, there is less opportunity to make a play. Due to variance in player skill, if the player is not a contributor (in terms of tallied/recorded events) they may play long stretches without a logged event. Thus, the classification step prior to this one is important to gain information on these situations where the evidence does not make it obvious who is on (when a missed “enters the game” occurs for a player who did not contribute much, or a missed “goes to the bench”). 





2017 Research Papers Competition Presented by: 

7 





Equation (1) shows our activity heuristic (AH) for player _p_ at substoppage 𝑠𝑠Y, where 

% • 𝕀 =<sup>1</sup> 𝑖𝑓 𝑟𝑜𝑤 𝑘 𝑖𝑛 𝑃* 𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑠 𝑝𝑙𝑎𝑦𝑒𝑟 𝑝 𝑚𝑎𝑘𝑖𝑛𝑔 𝑎𝑛 𝑎𝑐𝑡𝑖𝑣𝑒 𝑝𝑙𝑎𝑦 7,%,X 0 𝑒𝑙𝑠𝑒 

- _l+1_ is set to _n_ if _l_ is the last substoppage 

• 𝑙∗ =<sup>𝑛</sup> 𝑖𝑓 𝑙 𝑖𝑠 𝑡ℎ𝑒 𝑙𝑎𝑠𝑡 𝑠𝑢𝑏𝑠𝑡𝑜𝑝𝑝𝑎𝑔𝑒 𝑙+ 1 𝑒𝑙𝑠𝑒 

𝑛 𝑖𝑓 𝑙 𝑖𝑠 𝑡ℎ𝑒 𝑙𝑎𝑠𝑡 𝑠𝑢𝑏𝑠𝑡𝑜𝑝𝑝𝑎𝑔𝑒 • 𝑙∗∗ = 𝑟𝑜𝑤 𝑖𝑛𝑑𝑒𝑥 𝑎𝑓𝑡𝑒𝑟 𝑙∗𝑤ℎ𝑒𝑟𝑒 5 𝑢𝑛𝑖𝑞𝑢𝑒 𝑝𝑙𝑎𝑦𝑒𝑟𝑠 𝑠𝑒𝑒𝑛 𝑒𝑙𝑠𝑒 

% The reason why we add evidence from 𝑃* 𝑠𝑠Y∗: 𝑠𝑠Y∗∗ is because (a) sometimes 𝑠𝑠Y∗ is too close to % 𝑠𝑠Y to gather any meaningful evidence in 𝑃* [𝑠𝑠Y: 𝑠𝑠Y∗] and (b) the likelihood of all five players % substituting off at 𝑠𝑠Y is unlikely, and so the evidence in 𝑃* 𝑠𝑠Y∗: 𝑠𝑠Y∗∗ is likely to contain evidence about who should sub in at 𝑠𝑠Y (the evidence is down-weighted to reflect this uncertainty). 

We sort for the players who were most active by our heuristic and add the most active players to 𝜔. In the event where there are not enough correct substitutions nor active players seen to deduce who the five players should be on the court (usually at substoppages with incorrect substitutions at the end of a period), the tiebreaker for players is the boxscore minutes. 

Note: since deflections and out-of-bounds events are not recorded, not all stoppages can be determined from the play-by-play. Thus, we restrict ourselves to inferring substitutions only at the substoppages in the game. We can clean games that do not have substitutions at all, by replacing substoppages with the stoppages we can infer from the play-by-play (turnovers not forced by steal, fouls, timeouts, beginning/end of period). 

## **4. Results** 

Agent systems are evaluated on performance measures: an objective criterion for success of an agent’s behavior. We define two simple performance measures that can objectively quantify the result of our agent cleaning the play-by-play. 

#### **4.1. Minutes criterion** 

In the U Sports league, a separate party from the ones responsible for recording the play-by-play is responsible for compiling the boxscore statistics. It is important to emphasize the fact that the boxscore tallies do not result from the play-by-play itself. Since it is an account of the game from another objective party, we can use the minutes tallied in the boxscore to compare the minutes that are tallied from our cleaned boxscore. 



Equation (3) shows the minutes criterion (MCi) calculated for each game _i_ , where 





2017 Research Papers Competition Presented by: 

8 



- N = number of players in game _i_ 

- y 

- • 𝑝7 is player _k_ ’s minutes tallied from the cleaned game 

- { 

- • 𝑝7 is player _k_ ’s minutes tallied from the boxscore 

#### **4.2. Unknown players criterion** 

Though less frequently occurring, there is the possibility of an incorrect player name recorded for an active play. Particularly, this occurs when a lot of active plays are in quick succession or when inexperienced record keepers get lost behind in the action. In the situation where the evidence % suggests {P1, P2, P3, P4, P5} are on the court after _ss_ j, and in 𝑃* [𝑠𝑠%: 𝑠𝑠%I'] there is a record of P6 performing an active play, then (taking our estimate as the true lineup on the floor) there is a contradiction that must be resolved. We resolve it by replacing the player name observed with an “UNKNOWN,UNKNOWN” player. The solution which minimizes the frequency of this occurring is a better solution, since our agent uses the active plays as evidence for inferring the correct substitutions. 



Equation (4) shows the unknown players criterion (UPCi) calculated for each game _i_ , where 

- ni = number of play-by-play rows in game _i_ 

- 𝕀7 =<sup>1</sup> 𝑖𝑓 𝑡ℎ𝑒 𝑝𝑙𝑎𝑦 𝑖𝑛 𝑟𝑜𝑤 𝑘 𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑠 𝑡ℎ𝑒 "UNKNOWN,UNKNOWN" 𝑠𝑡𝑟𝑖𝑛𝑔 0 𝑒𝑙𝑠𝑒 

#### **4.3. Discussion of Results** 

**_Table 4: Performance measures of algorithm for every season for men's and women's games_** 

|**Season**|**Avg #**<br>**unknowns per**<br>**game**|**Avg # active**<br>**plays per game**|**Avg seconds**<br>**discrepancy per**<br>**player**|**Avg # of players**<br>**observed**<br>**playing per**<br>**game**|
|---|---|---|---|---|
|**2009**|2.96|376.60|192.92|20.20|
|**2010**|2.92|380.47|194.50|20.21|
|**2011**|3.12|377.52|194.87|20.33|
|**2012**|3.14|374.45|194.51|20.38|
|**2013**|3.23|375.46|199.10|20.51|
|**2014**|2.98|374.11|197.46|20.33|
|**2015**|3.01|377.12|197.27|20.28|





2017 Research Papers Competition Presented by: 



9 



**Total 3.08 376.33 197.30 20.33** 

Looking at the average number of “UNKNOWN,UNKNOWN” instances and active plays per game, we are unable to attribute a player that we estimate to be on the floor to an active play less than 1% of the time. The algorithm shows consistent performance across seasons with a very small sample of training data (relative to the number of games that have occurred). 

It is worth noting that the play-by-play’s timestamps are in MM:SS format, however the boxscores are only in MM format. Thus, even the correct play-by-play will have some discrepancy in minutes obtained from the log compared to minutes obtained from the boxscore. 

## **5. Conclusions** 

In this work, we explored the effectiveness of an automated single agent framework that can clean play-by-play showing a variety of inconsistencies in recorded substitutions. The solution can improve with more data when it is fed examples of manually cleaned play-by-play. To the best of our knowledge, this is the first type of automated solution that solves the problems that result from human recorded basketball play-by-play. We define two performance measures and show that the agent, with a small amount of initial training data and simple heuristic functions, is objectively successful – with the average absolute difference between minutes extracted from the play-by-play and from the boxscore being approximately three minutes per player. For our specific application, the U Sports league, the analysis that can be derived from the cleaned play-by-play provide access to historical and current statistics beyond the boxscore, such as adjusted plus-minus and WOWY, to coaches and avid fans. For coaching staff, these metrics can inform strategy, decision making and roster management in a similar fashion to how counterparts in the NBA community took advantage of play-by-play derived metrics in the past decade. For media and fans, it introduces and amplifies the growing analytical discourse that our game is seeing. As a league that recently rebranded in 2016 to appeal to a wider audience, as well as to spread stories of young Canadian university athletes [4], this is a cost-effective method that can help accomplish both of its stated goals. 

This approach can be extended to any other lower revenue leagues which suffer the same problems of possessing play-by-play containing manual errors which dramatically affect the results of metric calculations. Play-by-play is an important data medium, particularly for leagues that cannot afford the infrastructure for video tracking data.  We believe this work is an important step in raising the awareness and the standard of analytics for many basketball leagues around the world. 

## **References** 

[1] Sill, J. (2013) _Improved NBA Adjusted +/- Using Regularization and Out-of-Sample Testing_ . Paper presented at MITSSAC, 2010. 

[2] Past Champions – CIS. http://en.cis-sic.ca/championships/mbkb/past_champs. 

[3] Conn, J. R. (2014, March 3). The Canadian College Basketball Dynasty You’ve Never Heard Of. _Grantland_ . Retrieved from http://grantland.com. 

[4] Shoalts, D. (2016, October 10). CIS rebrands as U Sports, aims to bring student stories to Canadians. Retrieved from http://theglobeandmail.com. 



2017 Research Papers Competition Presented by: 



10 


