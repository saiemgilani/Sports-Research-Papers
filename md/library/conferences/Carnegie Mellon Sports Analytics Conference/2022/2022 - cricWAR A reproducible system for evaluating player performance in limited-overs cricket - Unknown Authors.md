<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2022/2022 - cricWAR A reproducible system for evaluating player performance in limited-overs cricket - Unknown Authors.pdf -->

# cricWAR: A reproducible system for evaluating player performance in limited-overs cricket 

### Hassan Rafique<sup>∗</sup> 

##### **Abstract** 

Cricket statistics mainly comprise simple averages (batting avg., bowling avg., strike rates, etc.) to account for player performance. For limited-overs cricket, these statistics fall short of providing a comprehensive picture of a player’s performance and contribution to the team’s success. Due to the rise of T20 cricket leagues, there is significant interest in comprehensive statistics that capture the net value-added by an individual player. Inspired by sabermetrics [1], we develop metrics such as runs above average (RAA), value over replacement player (VORP), and wins above replacement (WAR) for batters and bowlers in limited-overs cricket. These metrics are calculated using ball-by-ball data readily available through R package cricketdata, co-developed by us. We associate run value with each actual run scored using estimated expected runs. Some positions/situations are more conducive for scoring (or defending) during the innings, and we adjust the run values by using a variation of the Leverage Index [4]. Run values are adjusted for the venue, bowling pace (spin vs. pace), platoon advantage, and innings (first vs. second) using regression to estimate RAA. We assess the uncertainty in RAA and WAR estimates through a resampling and simulation-based approach and present results for the IPL 2019 regular season. Finally, we discuss the further avenues of research and comment on the possible implications of this work for the T20 teams. 

## **1 Introduction** 

Cricket is typically regarded as a major world sport, considering different measures such as global fanbase (2.5 billion), digital viewership, TV rights deals, etc. Most of the fanbase resides in South Asia, the UK, Australia, South Africa, and New Zealand. Cricket is significantly growing due to the popularity of the new format of T20 and the money this format has brought into the game. However, the public statistical analysis of the sport and use of analytics in cricket appear to lag behind the other major sports. Baseball has a long history of public sabermetrics research work, and the last decade has seen an explosion of public sports analytics work in basketball, ice hockey, soccer, and American football. On the other hand, cricket is in the nascent stages of the sports analytics era, and barring a few private T20 league teams, and one national team, the use of analytics seems very limited. 

One of the most fundamental focuses in team sports is to quantify the role played by individual players in team success. Since the goal is to win in sports, it is natural to be interested in estimating the number of wins a player contributes to their team. In cricket, like baseball, the role of players is clearly defined, and the actions are discrete, e.g., batters and bowlers (pitchers). Most of the cricket statistics evaluating player performances are simple averages, e.g., batting avg. = no. of inningsruns <u>scoredbatter</u> got out<sup>,bowlingavg.=</sup> no.runsof wicketsconcededtaken<sup>,strikerate=</sup> <u>runsballsscoredfaced* 100</u> . These stats may provide reasonable estimates for the players’ individual performances in batting/bowling and quality. However, they do not tell us about the contribution of the player’s performance to the team’s success. With the rise of T20 cricket leagues around the globe, there has been a significant interest in a comprehensive measure of overall player performance. 

> ∗University of Indianapolis, rafiqueh@uindy.edu 

1 

Inspired by sabermetrics, we are interested in estimating the value in terms of runs provided by the player compared to an average player (runs above average: RAA) and how that value translates to team wins compared to a replacement level player (win above replacement: WAR). RAA and WAR are useful metrics with simple meanings and units. RAA tells us how much value (runs) a player produces compared to a league-average player in the same situation of an innings after accounting for some confounding variables. Using ball-by-ball data, we can estimate RAA for each ball faced by a batter, which can then be aggregated over a part of the innings, the whole innings, or the season. RAA for the player is then compared with the RAA of a replacement level player to evaluate WAR. If Virat Kohli has a WAR of around one, we could expect to drop one game in the standings over a whole season if we were to replace him with a replacement-level player. 

### **1.1 Limited Overs Cricket** 

A cricket playing team consists of eleven players, and a maximum of ten can bat for a team. Wickets lost represent the number of outs for the batting team. A limited-overs cricket game comprises two innings, with the toss deciding which teams bat first. An over consists of six balls and limited-overs games have a fixed number of overs for each innings. The team batting first sets the target, equal to their innings total plus one, for the other team to score to win. E.g., if the first innings total is 149, the team batting second has to score 150 to win the game. An innings conclude if the allotted number of overs have been bowled, the batting team loses all ten wickets (outs), or the batting team has reached the target. For the rest of the paper, we will use Twenty20 (T20) games as an example of a limited-overs game. As the name suggests, there are twenty overs (120 balls) in each innings of a T20 game. 

### **1.2 Previous Work** 

[3] shows a way of estimating RAA by using the phase of the innings, wickets lost, and the venue. However, it does not account for other factors such as innings number, bowling speed, and platoon advantage. Also, grouping by phase of the innings, e.g., power play (over 1- 6), death overs (16-20), etc., is an oversimplification as we can lose the interesting dynamics of each over’s play within each phase. They also present the wins above average (WAA) metric. To simplify their WAA calculations, [3] uses the estimate of the second innings total if it were to continue even after reaching the target. This simplification would produce uncertainty in the WAA estimates, which the author does not address. WAA takes an average player as the baseline player and it is not easy or possible for a team to replace a player evaluated with a player of average quality. In addition, [3] lacks the uncertainty estimation for their proposed metrics. 

### **1.3 Contributions of cricWAR** 

cricWAR provides a framework for evaluating overall player performance, considering the context, and provides metrics such as run value, runs above average, and wins above replacement, which are easily interpretable. The run value for each play (ball) is estimated using expected runs. We adjust the run values (Section 2.1) for factors such as venue, innings (first or second), platoon advantage, and bowling pace (fast or spin) to allow for a fair comparison across different contexts. The adjusted run values are accredited (Section 2.2) to the players (batters and bowlers) using the run conservation framework [1]. A resamplingbased method (Section 3) is used to estimate uncertainty in the proposed metrics. The results (Section 4) are presented for Indian Premier League (IPL) 2019 season. cricWAR is fully reproducible and open-source. We use the `R` package `cricketdata,` which provides easy access to ball-by-ball and is co-developed by us. 

## **2 cricWAR Model** 

Our proposed measures RAA and WAR are based on the runs conservation framework, which depends on the difference between expected and actual runs scored on each ball. The first step is to establish the 

2 

expected number of runs that would be scored given the current state of the game. We define the states of a T20 game by the over (o), and the wickets lost(w). 

Note that the scoring is more prolific in cricket than baseball. On any given ball, a batter may take a single (1 run), a double (2 runs), a triple (3 runs) by running between wickets (bases) or hit a boundary which maybe a four (4 runs) or a six (6 runs). The game will progress from one state to another mostly through the change of the over, along with some state changes when a wicket falls which are quite significant. These aspects of the game influences the expected runs framework defined below. 

We define the expected runs (𝜃) for a state as 



The value 𝜃(𝑜, 𝑤) is estimated as the empirical average of the runs scored whenever a game was in the state (𝑜, 𝑤). We define the **run value** (𝛿) for a ball as 



where r is the actual runs scored on that ball. For each ball 𝑖, run value 𝛿𝑖 represent how well (positive) or worse (negative) a player did, compared to an ‘average player’, given the situation (state) of the game. 

The _runs conservation framework_ [1] dictates that the every run value 𝛿 gained by batter on a ball is accompanied by the bowler gaining −𝛿 for that ball. The extras (wides and no-balls) are completely attributed to the bowler. 

### **2.1 Adjusting Run Values** 

#### **2.1.1 Leverage Index** 

The T20 cricket has some fielding restrictions which affects the run scoring in different stages of the innings. For the first six overs of an innings, also called power play (PP), only a maximum of two fielders are allowed outside the 30-yard (inner) circle. After PP, a maximum of five players are allowed outside the inner circle. Additionally there can only be five players at a time on the leg side of the field. 

With only two fielders outside in the inner circle during PP, batters take advantage by hitting shots to cross the inner circle and score boundaries (4s or 6s). Right after PP, bowlers can place more fielders outside and control the scoring. Towards the end of the innings, in the last few overs (death overs), batters are trying to score quickly and taking more risks by hitting bigger shots to score boundaries. This means that players playing in different stages (PP, death overs, etc) can accumulate (or lose) run value quick and hinders the comparison of players across different playing positions. 

The weighted average of expected runs 𝜃, of all states, is evaluated and then 𝜃 for each state is divided by this weighted average to get the Leverage Index (LI) for each state. An LI of one corresponds to a state which is average wrt scoring rate, whereas a LI ≫ 1 means its a high scoring state, and a LI ≪ 1 means it is a low scoring state. 



The run value 𝛿 is divided by the corresponding leverage index (LI) and labelled as leveraged run value 𝛿<sup>𝑙𝑒𝑣</sup> . LI helps account for situations which might be conducive for scoring (power play with fielding restrictions, last few overs of an innings.) or defending (middle overs). 

3 

#### **2.1.2 Batting** 

There are different factors beyond the control of batters and bowlers that affects the run values and makes it hard to compare them across contexts. In particular, we want to account for the venue, innings (first Vs second), platoon advantage (right handed batter against left handed bowler or vice-versa), and the bowling pace (spin Vs pace). We adjust for these factors using a linear regression. We fit the leveraged run values using the covariates mentioned above. 



where all the covariates are categorical. The coefficients 𝛽, 𝛽1, 𝛽2, and 𝛽3 are the effects for the venue, innings (first Vs second), platoon advantage, and the bowling pace (spin Vs pace), on the leveraged run values, respectively. Ordinary least square is employed to estimate the coefficients. The estimated coefficients 𝛽, 𝛽1, 𝛽2, and 𝛽3 are evaluated by ordinary least square using all the ball-by-ball data in the season. 

The estimated residuals from the regression (Equation 1) 



indicate the part of the leveraged run values 𝛿𝑖<sup>𝑙𝑒𝑣</sup> that is not accredited to venue, innings, bowling pace, and platoon advantage and we refer to them as adjusted batting leveraged run values. 

#### **2.1.3 Bowling** 

The runs conservation framework dictates that the bowler gains leveraged run value −𝛿𝑖<sup>𝑙𝑒𝑣</sup> for each 𝛿𝑖<sup>𝑙𝑒𝑣</sup> leveraged run value gained by the batter. Along with that any extras (wides, noballs) 𝜔 are completely attributed to the bowler. Similar to Equation 1, we adjust the bowling leveraged run value -(𝛿𝑖 + 𝜔𝑖)<sup>𝑙𝑒𝑣</sup> for the venue, innings, platoon advantage, or the bowling pace 



The estimated residuals from the regression (Equation 2) 



indicate the part of the leveraged run values -(𝜔𝑖 + 𝛿𝑖)<sup>𝑙𝑒𝑣</sup> that is not accredited to venue, innings, platoon advantage or the bowling pace and we refer to them as adjusted bowling leveraged run values. 

### **2.2 Runs Above Average** 

To the best of our knowledge, the fielding tracking data is not available, at least publicly. In the absence of fielding data, we accredit these adjusted batting and adjusted bowling leveraged run values to the batter and bowler, respectively. 

𝑅𝐴𝐴<sup>𝑏𝑜𝑤𝑙</sup> 𝑖 =̂ 𝜂𝑖, 𝑅𝐴𝐴<sup>𝑏𝑎𝑡</sup> 𝑖 =̂ 𝜖𝑖 

The runs above average for each ball a player played (batted or bowled), over a season, is summed to get the total measure of 𝑅𝐴𝐴𝑋 for player 𝑋, where 𝐼(⋅) is the indicator function. 



4 

### **2.3 Value over Replacement Player** 

The usual attempts at evaluating Value over Replacement Player (VoRP) involves measuring player contribution on the scale of runs/points relative to a baseline player and a natural choice would be to choose a ‘league average’ player as that baseline. However, as discussed in openWAR [1] and nflWAR [5], the leagueaverage players are still quite valuable, and it is unlikely for a team to be able to replace the player in consideration with another league-average player. Instead, the team is more likely to look for a replacement player from a relatively inexperienced, at the pro level, group of players from their team roster. Hence, for the baseline comparison, we consider a _replacement level_ player to be one that is readily available to replace the player being evaluated. E.g., in MLB, replacement level player is more likely to come from minor leagues. 

We consider an approach similar to openWAR [1] and nflWAR [5] in defining a squad(roster)-based replacement level. We use the Indian Premier League (IPL) to illustrate the approach. IPL teams have a minimum of 18 players and a maximum of 25 players on their squad. On average, teams have played 19 distinct players each season over the last decade. We looked at the number of distinct batters and bowlers and how many matches they played. Considering these stats, we decided to take eight batters and eight bowlers as league-level players. We take the top 8𝑁 batters and 8𝑁 bowlers in regards to the playing time to be the league-level players, and the remaining players would be considered replacement-level players, where 𝑁 is the number of teams. 

All the replacement level players are pooled together, and their average performance is labeled as 𝑎𝑣𝑔.𝑅𝐴𝐴𝑟𝑒𝑝, which represents RAA per ball for a replacement-level player. For every actual player, we can associate a replacement-level shadow player with 𝑅𝐴𝐴𝑟𝑒𝑝 by taking the 𝑎𝑣𝑔.𝑅𝐴𝐴𝑟𝑒𝑝 and multiplying it by the number of balls played by the actual player. This replacement-level shadow player 𝑅𝐴𝐴𝑟𝑒𝑝 provides a relevant baseline for comparison, specific to the player being considered. 

Value over replacement player (VORP) is evaluated as 



where 𝑅𝐴𝐴𝑋 is the total 𝑅𝐴𝐴 for player 𝑋 in a season, 𝑎𝑣𝑔.𝑅𝐴𝐴𝑟𝑒𝑝 is the average 𝑅𝐴𝐴 of all the replacement level players as defined in [1], and the 𝐵𝑋 is the number of balls player 𝑋 played in (batted plus bowled). 

### **2.4 Wins above Replacement** 

Wins above replacement (WAR) is evaluated as 𝑊𝐴𝑅𝑋 =<sup>𝑉𝑂𝑅𝑃𝑋where𝑅𝑃𝑊istherunsperwinfor</sup> 𝑅𝑃𝑊<sup>,</sup> the league. Following the approach taken by [5], we use linear regression to estimate RPW by fitting the following model 



where 𝑊𝑖 is the team 𝑖<sup>′</sup> 𝑠 win total in a regular season and Run Diff𝑖 is the run differential for team i in that regular season. The estimate 𝛽 represents the increase in win total for each one unit increase in run differential of the team, meaning RPW can be estimated by 1/̂𝛽. After fitting the model, we got 𝑅𝑃𝑊≈ <u>1</u><sup>84.5.Wedidfitanothermodelwithseasonastheadditionalcovariate,buttheeffect</sup> 0.011839<sup>=</sup> of season was insignificant with same 𝛽 estimate. 

We also followed approach laid out in [1] to estimate RPW using the Pythagorean win expectation formula and the results were similar to run differential approach. 

5 

## **3 Uncertainty Estimation** 

Consider a player with fixed ability and repeat the same season for that player many times. In each of these (repeated) seasons, the player’s playing events would have variation in their outcome, leading to different season-level RAA and WAR values. We target this player outcome variability in our uncertainty estimates for RAA and WAR values. 

Following the approach in [1], we use a resampling strategy to generate distributions for each player’s RAA and WAR values. For a particular season, we resample (with replacement) individual balls, fit the regression model for adjusting run values, and use the adjusted run values for new RAA and WAR values for individual players. In Section 4, we present the uncertainty estimates with 1000 simulated seasons. The resampling approach quantifies the player outcome variability while maintaining the inherent correlation between the individual events. 



Figure 1: cricWAR RAA values for 2019 Indian Premier League (IPL) regular season. The season had 161 players play, and 46 were classified as replacement-level. Blue and red dots represent league-level and replacement-level players, respectively. Playing time for a player is evaluated as the number of balls faced by that player as a batter plus the number of balls bowled by that player as a bowler. The gray dots represent the replacement level shadow for each player. We highlight the difference between the player’s RAA and the RAA for their replacement-level shadow for three players. 

## **4 Results** 

We present the results for the Indian Premier League (IPL) 2019 regular season. For expected runs estimation, we use the data from IPL seasons 2015 through 2022 except 2020, which was played outside India. cricWAR results for multiple seasons are available in the shiny app https://dazzalytics.shinyapps. io/cricwar/. For the 2019 IPL season, 46 players are classified as replacement-level from the 161 players. 

6 

Table 1: Batting and bowling RAA for top eight best and worst performers from the IPL 2019 regular season. 

||(a) Batt|ing RAA|||(b) Bow|ling RAA||
|---|---|---|---|---|---|---|---|
|Best|RAA|Worst|RAA|Best|RAA|Worst|RAA|
|AD Russell|120.6|AT Rayudu|-75.8|JJ Bumrah|118.3|JD Unadkant|-52.4|
|HH Pandya|82.6|RV Uttappa|-58.0|JC Archer|103.3|R Parag|-48.7|
|CH Gayle|72.0|SPD Smith|-43.0|Rashid Khan|61.0|S Lamichhane|-48.6|
|RR Pant|55.6|Shubman Gill|-42.2|B Kumar|49.1|TG Southee|-42.1|
|PA Patel|48.3|V Shankar|-41.1|YS Chahal|46.8|DS Kulkarni|-40.3|
|SP Narine|36.0|MP Stonis|-39.7|NA Saini|44.4|PP Chawla|-36.2|
|JC Butler|32.5|F du Plessis|-39.7|SP Narine|40.2|K Gowtham|-28.4|
|JM Bairstow|28.9|KM Jhadav|-37.2|R Ashwin|39.6|VR Aaron|-26.8|



Across all players, WAR has right-skewed distribution with a median of 0.18, a mean of 0.36, and a standard deviation of 0.51. The skew is due to a few excellent players accumulating large WAR values. WAR for replacement players is approximately normal, with a mean of 0, a median of -0.075, and a standard deviation of 0.12. Figure 1 shows the RAA values for all players from the IPL 2019 season, differentiating the league-level players (blue) from the replacement-level (red) players. The gray dots represent the RAA values for replacement-level shadows associated with each actual player. Playing time for a player is evaluated as the number of balls faced by that player as a batter plus the number of balls bowled by that player as a bowler. 

Table 1 shows the top eight best and worst batters and bowlers, wrt RAA, in the 2019 regular season. The players who both bat and bowl are assigned the playing role of allrounders. We see AD Russell, an allrounder who bats lower in the order, topping the batting RAA. Gayle and Butler represent the opening batters on the list. In bowling, Bumrah and Archer are miles ahead of the competition. SP Narine, an excellent allrounder, rightfully makes an appearance in the top eight of both batting and bowling RAA list. Access the list of all players with cricWAR stats at https://dazzalytics.shinyapps.io/cricwar/. 

We consider the player outcome variability described in Section 3 by simulating 1000 seasons of the actual 2019 IPL regular season. Note that the variation in player performance is not constant. Figure 2 shows the distribution of WAR values for the top five players by playing role and are sorted by their actual WAR point estimates. AD Russell has the highest point estimate of 2.3 WAR and has the highest variation in simulated WAR. Russell is an allrounder, meaning he bats and bowls regularly. Table 2 shows the quantiles and width of 95% confidence intervals of the simulated seasons for the top ten players by playing role. Top allrounders have the highest variation, as shown by the large confidence interval width, whereas the top bowlers are among the ones with the least variation. JC Archer, a bowler, has the least simulated WAR variation among the top ten players and top 3 cricWAR point estimate among all players, which suggests that the Archer provides relatively consistent performance on a ball-by-ball basis compared to other players. 

Sports fans and media are always interested in comparing players and discussing if one player is better than the other. In particular, these discussions arise for awards such as MVPs (Mike Trout Vs. Miguel Cabrera[1]) etc. cricWAR point estimates along with the WAR interval estimates (Table 2) from simulated seasons allow for more refined analysis. Figure 3 the joint distributions of simulated WAR for a pair of bowlers and allrounders from the 2019 IPL season. AD Russell leads HH Pandya in WAR for almost 81% of the simulated seasons for allrounders. And AD Russell had a cricWAR point estimate of 2.3 compared to 1.7 of HH Pandya. Thus, we can say with some confidence that there is a high probability that AD Russell had a better season than HH Pandya. Bowlers, Bumrah, and Archer, had cricWAR point estimates of 2.1 and 2, respectively. From simulated seasons, we have Bumrah leading Archer in 58.1% of the seasons. Now, 

7 

here we have a situation where there is a significant overlap in the interval estimates, and point estimates have a slight difference. Hence, there is enough uncertainty suggesting not to make a conclusive statement about Bumrah being better than Archer. 



Figure 2: WAR simulation distributions of IPL 2019 regular season by playing role (batter, bowler, or allrounder) of top players. Distributions are based on 1000 simulated seasons. 

Table 2: Distribution of top ten players’ WAR for IPL 2019 regular season. Quantiles and 95% confidence interval width are based on 1000 simulated seasons 

|Player|Role|q2.5|q25|q50|q75|q97.5|conf. int. width|
|---|---|---|---|---|---|---|---|
|AD Russell|Allrounder|1.30|2.07|2.47|2.86|3.59|1.14|
|HH Pandya|Allrounder|0.86|1.48|1.85|2.23|2.96|1.05|
|SP Narine|Allrounder|0.92|1.48|1.80|2.10|2.73|0.91|
|DA Warner|Batter|0.67|1.23|1.55|1.85|2.47|0.90|
|CH Gayle|Batter|0.80|1.37|1.68|2.00|2.58|0.89|
|Rashid Khan|Bowler|0.79|1.40|1.66|1.92|2.46|0.835|
|R Ashwin|Bowler|0.56|1.11|1.37|1.63|2.17|0.81|
|JJ Bumrah|Bowler|1.47|1.93|2.18|2.43|2.96|0.74|
|RR Pant|Batter|0.61|1.05|1.29|1.55|2.03|0.71|



8 

|Player|Role|q2.5|q25|q50|q75|q97.5|conf. int. width|
|---|---|---|---|---|---|---|---|
|JC Archer|Bowler|1.42|1.86|2.10|2.32|2.77|0.67|



### **4.1 Metric Stability and Scoring Fast** 

We consider the stability of WAR from season to season by calculating the autocorrelation within players between consecutive seasons, presented in Table 3. The correlation has been relatively stable over the years. 

Table 3: Autocorrelation of WAR. WAR is estimated in consecutive seasons for each player, and the correlation between the players who played in both of the consecutive seasons is reported. 

||’15 -’16|’16 -’17|’17 -’18|’18 -’19|’21 -’22|
|---|---|---|---|---|---|
|**WAR correlation**|0.425|0.362|0.479|0.453|0.428|
|**Matched Players**|110|114|103|113|121|



Batting efficiency in limited over cricket is two-dimensional. You do not need only to score runs but score them at a fast rate. The reason is there are a limited number of balls to score, and that resource should be consumed effectively. Thus the strike rate (SR), runs scored per ball, is a convenient stat to profile a batter. The boundary percentage (BP), the percentage of balls hit for a four or a six for batters, is a popular stat in T20 and highly correlates with strike rate. We examine in Table 4, the correlations of batting RAA with SR and BP over the years for IPL while only considering the batters who faced at least sixty balls in a season. There is a strong correlation between RAA and the fast scoring stats of SR and BP. Note that these correlations have been stable over the years. 

Table 4: Correlation of batting RAA (of players with a minimum of 60 balls batted in a season) with their boundary percent and strike rate. 

||’15|’16|’17|’18|’19|’21|’22|
|---|---|---|---|---|---|---|---|
|**Boundary Percent**|0.853|0.862|0.867|0.838|0.859|0.895|0.892|
|**Strike Rate**|0.864|0.854|0.855|0.873|0.841|0.843|0.865|



## **5 Summary and Further Discussion** 

We present a novel and reproducible framework for evaluating overall player performance in limited-overs cricket. We develop metrics such as run value, RAA, and WAR, which are easily interpretable by the public. Along with point estimates, we present the uncertainty estimates for a better understanding of the metrics. The ball-by-ball data is used from the R package `cricketdata` , co-developed by us. 

There are several exciting areas for further research. One of the main limitations is the lack of availability of fielding data. The location of the fielders at the time of the delivery of the ball and the subsequent movement by fielders can help us better allocate the run value to batters (particularly when running for runs), bowlers (mainly when fielders make mistakes), and add the fielding contributions in the cricWAR framework as well. In the second innings, the batting team is chasing a target, and the required run rate per over affects the flow of the innings. Thus, the run values for second innings could be considered differently after accounting for the required run rate. 

9 





(a) Better Allrounder (WAR): AD Russell vs HH Pandya (b) Better Bowler (WAR): JJ Bumrah vs JC Archer 

Figure 3: Joint distribution of simulated WAR for a pair of allrounders and bowlers, 2019 IPL season. An approach to compare player performance considering the player outcome variability. 

### **5.1 Considerations for Teams** 

With the growing number of T20 cricket leagues around the globe, there is significant interest in evaluating the players for roster construction and drafting. These leagues draft from a pool of players who usually have played cricket at the international, league, or domestic level. And for the competitions/leagues, these players have played, we can estimate these players’ RAA and WAR values. Many of these players play in multiple leagues and have enough playing data. 

The teams could use RAA and WAR as objective measures to project the future career value of players in the T20 league drafts, similar to the work done for the NFL draft [2]. In addition, teams could create RAA and WAR based “draft pick value chart,” similar to the Jimmy Johnson chart, which has been improved by [2]. By considering the RAA of players at different phases (power play, middle, death) of the innings, team management may use players in different phases and adjust the playing order to maximize productivity. The T20 league teams draft players every year or every other year, and along with other information such as age, they could use RAA/WAR estimates to assess the contract values better. 

## **References** 

- [1] Benjamin S. Baumer, Shane T. Jensen, and Gregory J Matthews. “openWAR: An open source system for evaluating overall player performance in major league baseball”. In: _Journal of Quantitative Analysis in Sports_ (2015). doi: https://doi.org/10.1515/jqas-2014-0098. 

- [2] Nick Citrone and Sam Ventura. _Statistical Methods to Maximize Value in the NFL Draft_ . 2017. url: https://ww2.amstat.org/meetings/jsm/2017/onlineprogram/AbstractDetails.cfm?abstractid=322234. 

- [3] Himanish Ganjoo. _How many wins do the top players contribute to their team in an IPL season?_ 2020. url: https://www.espncricinfo.com/story/ipl-2020-how-many-wins-do-the-top-players-contribute-totheir-team-in-an-ipl-season-1236781. 

- [4] Tom Tango. _Crucial Situations_ . 2006. url: https://tht.fangraphs.com/crucial-situations/. [5] Ronald Yurko, Samuel Ventura, and Maskim Horowitz. “nflWAR: a reproducible method for offensive player evaluation in football”. In: _Journal of Quantitative Analysis in Sports_ (2019). doi: https://doi. org/10.1515/jqas-2018-0010. 

10 


