<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2019/2019 - playerElo - Unknown Authors.pdf -->

## Factoring Strength of Schedule into MLB Player Analysis 

# **playerElo** 

Jacob Richey, Professor Abraham Wyner | University of Pennsylvania 

Statistics updated to September 10<sup>th</sup> , 2019. 

Shiny App: <u>https://jrichey.shinyapps.io/playerelo/</u> 

FanGraphs Article: <u>https://community.fangraphs.com/playerelo-factoring-strength-of-schedule-into-playeranalysis/</u> 

### **Abstract** 

With the sabermetric revolution of the MLB, a plethora of new statistics have come into the mainstream, and a growing number of fantasy owners, ballclubs, and regular fans are turning to these new statistical methods for player analysis. However, I propose even advanced metrics such as wOBA, FIP, xwOBA, xFIP, and wRC+ are all missing a crucial element to accurately represent player performance thus-far. The playerElo system is able to reveal in aggregate the effects of previously unconsidered aspects of the game. Using an Elo ranking system determined by run-value calculations of all major league baseball players, the model incorporates context-dependent analysis and quality of competition to produce a proper evaluation of batters and pitchers. This enables playerElo to appropriately credit pitchers, especially relievers, for their true impact on the game, particularly when called upon in disadvantageous situations. Additionally, playerElo does not allow relative team strength, which confounds common counting statistics, to influence the evaluation of a player. The model is a holistic approach to the assessment of major league players and has incredible ramifications on player projections during free agency and player acquisition. 

### **Introduction** 

Consider the following comparison between Freddie Freeman (29) and Carlos Santana (33). Both players were starters for the 2019 All-Star teams of their respective leagues and are enjoying 

breakout seasons beyond their usual high production level with nearly identical statistics across 

the board. 

||**PA**|**wOBA**|**xwOBA**|**wRC+**|
|---|---|---|---|---|
|**Freeman, 1B**|643|0.398|0.396|144|
|**Santana, 1B**|624|0.389|0.371|141|



However, I argue there is an underlying statistic that makes Santana’s success less impressive and Freeman’s MVP-consideration worthy. Recall the quality of competition of pitchers faced. The 

Atlanta Braves’ division, the NL East, contains the respectable pitching competition of the Mets (11<sup>th</sup> league-wide in ERA), Nationals (12<sup>th</sup> ), Phillies (17<sup>th</sup> ), and Marlins (21<sup>st</sup> ). Contrast this with the competition of the Cleveland Indians in the AL Central: The Twins (8<sup>th</sup> ), White Sox (23<sup>rd</sup> ), Royals (26<sup>th</sup> ), and Tigers (28<sup>th</sup> ). Over his first 500 plate appearances, Santana faced a top 15 pitcher (ranked by FIP) just 15 times, compared to 43 times by Freeman. wRC+ controls for park effects and the current run environment, while xwOBA takes into account quality of contact, but all modern sabermetrics fail to address the problem of Freeman and Santana’s near-equal statistics, despite widely different qualities of competition. Thus, I present the modeling system of playerElo. 

### **Methodology** 

Conceived out of inspiration from Arpad Elo’s rating system for zero-sum games like chess, as well as FiveThirtyEight’s use of an Elo modeling scheme for MLB team ratings and season-wide 

predictions, playerElo treats all at-bats as events and maintains a running power ranking of all MLB batters and pitchers. The system uses expected run values over the 24 possible base-out states. Additionally, run values are calculated for each at-bat event by subtracting the run expectancy of the beginning state from the ending state, and adding the runs scored. 

𝑅𝑢𝑛 𝑉𝑎𝑙𝑢𝑒 𝑜𝑓 𝑃𝑙𝑎𝑦= 𝑅𝐸 𝐸𝑛𝑑 𝑆𝑡𝑎𝑡𝑒−𝑅𝐸 𝐵𝑒𝑔𝑖𝑛𝑛𝑖𝑛𝑔 𝑆𝑡𝑎𝑡𝑒+ 𝑅𝑢𝑛𝑠 𝑆𝑐𝑜𝑟𝑒𝑑 

The following run expectancy matrix presents the expected runs scored for the remainder of the inning, given the current run environment, baserunners, and number of outs. Data is sourced from all at-bats from 2016-2018, and expected run values are rounded to the second decimal place. For example, a grand slam hit with one out would shift the run expectancy from 1.54 to 0.27 and score four runs, so the run value of the play would be 2.73. 

|**1B**|**2B**|**3B**|**0 outs**|**1 out**|**2 outs**|
|---|---|---|---|---|---|
|-|-|-|0.51|0.27|0.11|
|1B|-|-|0.88|0.52|0.22|
|-|2B|-|1.15|0.69|0.32|
|-|-|3B|1.39|0.97|0.36|
|1B|2B|-|1.45|0.93|0.44|
|1B|-|3B|1.77|1.20|0.48|
|-|2B|3B|1.97|1.40|0.56|
|1B|2B|3B|2.21|1.54|0.75|



The model begins with a calibration year of 2018, and for 2019, players begin with their previous seasons’ ending playerElo, regressed to the mean slightly. If a player did not have a single plate 

appearance or batter faced pitching in 2018, such as Vladimir Guerrero Jr. or Chris Paddack, then they are assigned a baseline playerElo of 1000 (calibration year of 2018 began every player at 1000). For every at-bat, given the current base-out state, an expected run value for both the batter and pitcher is calculated, based on quadratic formulas of historic performance of players of that caliber in the given situation. The dependency of the Elo formula on the base-out state ensures the model is context-dependent, meaning it incorporates the fact that a bases-loaded double is far more valuable than a double with the bases empty, however, it also takes into account that runs were more likely to be scored in the former situation compared to the latter. 

It is important to note playerElo is a raw batting statistic and does not evaluate overall production, meaning stolen bases are not factored into the ranking system. Additionally, while the model does not take defense into account, it also does not count stolen bases or passed balls negatively against a pitcher, and likewise does not count changes in game states due to wild pitches positively for a batter. 

Once an expected run value is synthesized from the current state and the playerElo of the batter and the pitcher, park factor and home field advantage adjustments (if applicable) are made, and the expected run value of the play is then compared to the true run value outcome. The playerElo of both the batter and pitcher are then updated accordingly, dependent on the difference between the true run value and the expected run value. For example, if an excellent pitcher strikes out a mediocre batter, the batter will not lose much Elo, and the pitcher will not gain much Elo. Likewise, if a below-average batter does extremely well against a top pitcher, there will be a far greater change in the Elo of both players. Errors are also taken into account and will prevent a positive run value from counting against a pitcher or positively for a batter. 

Refer to the Technical Appendix at the end of the README.md on GitHub for further details regarding the playerElo methodology. 

### **Player Analysis** 



It is interesting to note Nolan Arenado and Edwin Encarnacion do particularly well in the model, even with park factor adjustments. This is can be attributed to the difficulty of schedule of the Rockies and Yankees, facing the tough pitching competition in the NL West and AL East respectively. The average pitching Elo faced by Arenado and Encarnacion is 1010.5 and 1009.6 (20<sup>th</sup> and 25<sup>th</sup> highest overall). Quality of contact does leave room to be desired for Arenado, however playerElo does not incorporate statistics like exit velocity and launch angle in its calculations, and thus the model is a better reflection of on-field performance than underlying swing metrics. In contrast to Arenado and Encarnacion, Yordan Álvarez has played incredibly since 

called up in June but has faced some of the easiest competition in the league, with an average Elo faced of only 986.8. 

Pitching wise, the breakout performances of Gray, Gallegos, and Bieber are all captured and supported by the playerElo model. Verlander recently wrenched the pitching Elo throne away from Scherzer following his no-hitter and several dominant outings.  Mike Minor ranks particularly high after seeing success against the high-powered offense of the Astros (3<sup>rd</sup> in runs scored), Athletics (7<sup>th</sup> ), Angels (13<sup>th</sup> ), and Mariners (17<sup>th</sup> ), and could have been an impact pitcher if dealt at the deadline. 

In contrast, playerElo has little faith in Trevor Bauer, one of the most discussed pitchers at the deadline and for whom the Reds paid a good price for. Bauer is ranked 166<sup>th</sup> among SPs with more than 100 batters faced, with a playerElo of 919 after beginning the season with a preseasonElo of 1111. He has struggled mightily against relatively easy divisions of the AL Central and NL Central, posting an xFIP of 4.40 against an average Elo faced of 979.5. We can visualize Bauer’s season long downward playerElo trend within the context of the league with the following graphic. Displayed below is the playerElo trends of the entire MLB for 2019, with specific batters and pitchers highlighted. The bold line on both graphs denotes the average playerElo. 



The graph illustrates Mike Trout has dominated since the start of the year and Harper has 

consistently been great and continues to rise in playerElo. Alvarez elevates from a rookie with a playerElo of 1000 to the top tier of players. On the pitcher side, Hyun-Jin Ryu was briefly the best pitcher in the game, as ranked by playerElo, for several starts, but has since come back to Earth hard with a sharp decline. Bauer’s long decline is evidenced throughout the season, with his playerElo reaching all-time lows over his past few starts. 

### **Team Analysis** 



Team Batting and Pitching Elo power rankings can also be created from playerElo, with weights for each individual playerElo determined by the plate appearances of the batter or innings pitched of the pitcher. To account for differences in variance, z-scores are used to weight team Batting and Pitching Elo to create an aggregate Team Elo.  Recall playerElo does not take into account defense or stolen bases, which will influence the ratings slightly. Speedster teams such as the Royals, Rangers, and the Mariners will rank slightly lower than their true abilities, and conversely the Padres and Cubs, who have had atrocious defensive performances thus far, will rank slightly higher 

than true value. However, the Team Elo rankings still give a fairly accurate view of the current state of the MLB, and particularly highlight upstart teams such as the Nationals and Athletics that could be even better than they have seemed thus-far. 

### **Sabermetric Context of playerElo** 

As playerElo only evaluates historical season performance to-date, and is not a prediction statistic, comparing playerElo with underlying swing metrics can enable accurate forecasts as to potential second-half decliners, and identify first-half breakouts that are for real. The below heat-map style table displays the top 40 players ranked by Expected Weighted On-Base Average (xwOBA), per Baseball Savant, with playerElo, Exit Velocity (EV), and Hard-Hit Percentage (HH%) also displayed. By evaluating the four statistics in collectively, it is easy to identify players such as J.D. Davis, Justin Smoak, C.J. Cron, and Gary Sanchez, whose quality of contact has been excellent, but have performed worse contextually or faced relatively easier pitching than other batters with similar quality of contact. Additionally, players such as Trout, Yelich, Rendon, Freeman, Bregman, and Marte have performed extremely well, and their contextual performance and level of competition backs up their success. 



### **Application** 

The playerElo system is able to reveal characteristics of the game and performance current metrics miss. For example, the context-dependent nature and run value calculations of playerElo appropriately credits a reliever who gets three outs without allowing a run after the previous pitcher loaded the bases, and similarly splits the credit of those runs being allowed between a pitcher who loaded the bases, and a reliever who failed to get the necessary outs to end the inning. 

Additionally, playerElo does not assign extra value to players who simply come up to the plate in high-powered offenses who often come up to the plate with runners on, nor docks players who simply do not get the same opportunities as their peers to accumulate as many counting statistics such as RBIs by nature of playing for a bad team. 

The difference between the playerElo rankings when run context-dependent, treating at-bats differently depending on the runs-out state, and context-free, meaning it treats all at-bats with equal weights of importance, highlight the important of including context in player evaluation. The greatest negative differences of rankings among the two models are all of hitters on the best offenses in the league: Yuli Gurriel, Justin Turner, and J.D. Martinez. The playerElo system accurately captures the favorable situations these hitters consistently bat in, and appropriately does not allow this to overinflate their value. Conversely, Alex Gordon of the atrocious Royals offense, rises significantly from, as does Renato Nunez from the Orioles. 

But most importantly, the fundamental aspect of the playerElo system is that the quality of competition is factored into player analysis. Once again, consider the comparison between Freeman and Santana, who have nearly identical statistics but clearly face different levels of pitching 

competition. 

||**PA**|**wOBA**|**xwOBA**|**wRC+**|**playerElo**|
|---|---|---|---|---|---|
|**Freeman, 1B**|643|0.398|0.396|144|1329|
|**Santana, 1B**|624|0.389|0.371|141|1146|



There is now a distinguishing factor between the two players, reflected by Freeman’s 5<sup>th</sup> best 

overall playerElo among batters versus Santana’s 55<sup>th</sup> overall playerElo. 


