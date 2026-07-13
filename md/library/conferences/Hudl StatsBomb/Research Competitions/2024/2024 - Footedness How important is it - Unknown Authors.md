<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2024/2024 - Footedness How important is it - Unknown Authors.pdf -->



# **Footedness: How important is it?** 

_Which is better, a brilliant right footer or an average left footer?_ Mark Carter 

## **1. Introduction** 

_Why study footedness?_ 

Footedness is relatively unexplored as a concept in football performance, yet there are key stakeholders whose impact could be accelerated with a better understanding of this important area: 

- Answers to simple questions like ‘how many left footers should we expect to have?’ are not readily available but would provide essential benchmarks for those responsible for **talent identification and talent development systems** . 

- **Technical coaches** of junior and youth players should consider footedness in relation to practice design. Would coaching interventions aimed at developing a weaker left side provide players with more chance to play at a higher level or more opportunity to be impactful across a range of positions? 

- **Team coaches** may often deploy players into positions based on where they can make the biggest impact, but that may not always fit with what is best for their long-term skill development. For the rare left footer, this research may uncover important insight on how best to care for their long-term potential rather than just short-term team success. 

- For **coaches at a performance level** , it may be clear that impactful progression of the ball on the left side of the pitch is often compromised by playing right footed players at left back – however, it is not clear what exact difference we should expect a left footed player in that position to make. Analysis is needed to understand whether left footed players in key positions increase the likelihood of winning games, and - if so - what exactly those left footed players add. 



## **2. Aims** 

_What we will try to achieve and how content will be structured._ 

In short, this research aims to understand footedness better. The research uses StatsBomb game event data with the following aims: 

1. **To describe the overall picture of footedness in elite men’s and women’s football.** This includes descriptive statistics to find out how many left, right and two footed players there are. It will also include analysis by league, gender, position and nation. 

**1** 



2. **To understand the relationship between footedness of players and winning games.** This will explore the idea that having more left footed players, especially in key left-sided positions, increases the performance of a team and leads to more chance of winning. 

3. **To explore differences in action frequency and success rate between left and right footed players in key positions.** This will include comparing in-possession metrics for left footed players or passes with the same metrics for right footed players or passes. 



## **4. Existing work** 

_A short summary of some of what we know about footedness from academic research._ 

### **4.1 Footedness prevalence in the population** 

A 2020 meta-analyses examined the results of 164 studies into footedness and handedness prevalence, with a total sample size of approximately 150,000 people. The key relevant findings are: 

1. Estimates of left footedness in the population ranges from 12% using the most conservative criterion of left footedness to 24% including all left and mixed footers in a single non-right category. 

2. 60% of left-handers are left footed; 3% of right handers are left footed. 

3. Males are 4% more often non-right footed, compared to females. 

4. Footedness is only marginally influenced by cultural and social factors, which play a large part in the determination of handedness. 

Reference 

- Four meta-analyses across 164 studies on atypical footedness prevalence and its relation to handedness, _Packheiser J. et al, 2020, Scientific report_ 

### **4.2 Footedness at the men’s World Cup, France 1998** 

There are very few studies of footedness in elite football, and no large sample analysis at all related to elite women’s football. Following the France 1998 FIFA Men’s World Cup, an analysis of footedness of 19,295 touches from 236 players from 16 teams concluded that: 

- 79% of players were right footed. 

- Left footed players were as biased towards their preferred foot as their right footed counterparts. 

- Very few players used each foot with equal frequency. 

- 14% of passes are made with the weaker foot. 

- Pass completion was the same when using preferred and non-preferred foot. 

- There was no differences in pass completion rate between left and right footers: “Left footed players may be the mirror image of their right footed counterparts”. 

**2** 



### Reference 

- Footedness in World Soccer: an analysis of France ’98, _Carey D.P. et al, 2001, in Journal of Sports Sciences, 19(11)_ 

### **4.3 Footedness when shooting at goal in football** 

An analysis of shooting distance, footedness and success in elite men’s football in Europe found that: 

- Players are more likely to choose their preferred foot when they are further from the goal. 

- Shots taken from the left side were more often performed with the right foot and vice-versa, for both left and right footed players. 

- Differences were only found in foot selection, but not in performance, as success rate did not vary between feet in any position. 

### Reference 

- How positional constraints affect footedness in football: A notational analysis of five leagues in Europe, _Marcori A.J. et al, 2022, in Journal of Motor Behaviour, 54(3)_ 



## **5. Methodology** 

_An explanation of what data has been used and how it has been used._ 

### **5.1 Data** 

The main data used is StatsBomb game event data for the Premier League (England, men’s tier 1), Serie A (Italy, men’s tier 1) and the Women’s Super League (England, women’s tier 1) for all games in seasons 2022-23 and 2023-24. Together this provides a dataset of 1420 games. 

In addition, StatsBomb game event data for all 64 games of the FIFA Women’s World Cup 2023 has been used to describe differences in composition of national female teams. 

### **5.2 Distribution of footedness across men’s and women’s football** 

In order to describe the distribution of footedness, each player’s passes and shots have been counted and each player has been categorized into one of the following categories: 

- Left footed: a player who makes 66% or more of their passes or shots with their left foot. 

- Right footed: a player who makes 66% or more of their passes or shots with their right foot. 

- Two footed: a player who makes less than 66% of passes or shots with their most dominant foot. 

**3** 



Only players who have made a total of 25+ passes or shots over the two seasons have been categorized and included in the research. The StatsBomb game event data field _body_part_name_ has been used to identify left and right footed passes and shots. 

Data from the two seasons, 2022-23 and 2023-24, are analysed and presented together. Where interesting differences between men’s and women’s football have been found, these results are displayed separately, otherwise all three leagues’ data has been analysed and presented collectively. 

When analysing footedness by nationality, it is interesting to compare the difference between players who play in the league of their nationality with players who play in a nation which is different from their nationality. Although these terms may be clumsy, we use the references ‘home grown’ for players who are playing in the league of their nationality (i.e. English players in the WSL or Premier League; and Italian players in Serie A); and ‘imported’ for players who are playing abroad and are likely to be a transfer from overseas. 

### **5.3 Impact of footedness on match outcomes** 

In order to evaluate whether left footed players increase the chance of a successful game result, we use a match prediction model to assess the impact that left footers make. 

### **5.3.1 The model** 

The match prediction model is a multi-class logistic regression model which uses the following features, each for the home and away team: 

- Goals scored and goals conceded 

- Expected Goals (xG) for and against 

- Expected Threat (xT) for 

- Percentage possession 

- Opponent form factor 

Each of these features is a rolling mean of the past five games. The opponent form factor assesses the strength of the previous five opponents to account for the fact that some teams may have had much more difficult recent games than other teams. 

Table 1 shows a model evaluation of key classification models and demonstrates why a logistic regression model was chosen over other machine learning options. The model has been trained on a subset of the match data (n=1102) and tested with a different subset of the match data (n=276), with test size of 0.2. 

**4** 



||AUC|CA|F1|Precision|Recall|MCC|
|---|---|---|---|---|---|---|
|Logistic Regression|0.679|0.573|0.507|0.509|0.573|0.306|
|Random Forest|0.646|0.522|0.500|0.488|0.522|0.231|
|Neural Network|0.657|0.542|0.506|0.494|0.542|0.257|
|Tree|0.545|0.404|0.407|0.416|0.404|0.083|
|kNN|0.617|0.474|0.465|0.464|0.474|0.174|



Table 1: Initial model evaluation, pre feature selection 

### **5.3.2 Model evaluation** 



Figure 1: Evaluation of Receiver Operating Characteristic (ROC) and Area Under Curve (AUC) for chosen model 

When evaluating the model’s accuracy to predict each game into one of three classes – Home win, Draw or Away win, the overall accuracy of the model is 61%. The model predicts home and away wins more accurately than it predicts draws. This can be seen in Figure 1 where the orange line (ROC curve for Draw) is closer to the dotted black line, the dotted black line showing the success of a random chance prediction model. 

Log loss is a metric which indicates a model’s likelihood of finding the actual observed outcomes. A lower log loss value indicates better alignment between the model’s predictions and the observed outcomes, such that a perfect model would have a log loss of 0. The log loss for the logistic regression 

**5** 



model used is 0.91. In a three-class regression analysis, the log loss of a chance or ‘dumb’ model would be 1.1. 

### **5.3.3 Model use** 

The match prediction model works out the probability of each game ending in a home win, draw and away win. Using these probabilities we work out a new variable, ‘PredPoints’, which is a calculation of the expected pre-match points over a series of games.  We can then analyse the residual between PredPoints and Actual points for games in order to evaluate each team’s performance. Matches which have included a high proportion of left footed players can be assessed in relation to a team’s entire sample of games, in order to evaluate the impact of left footers on results. An example of model use is given in the Results section and this should provide some clarity to the above explanation. 

### **5.3.4 Positions and definitions** 

We are particularly interested in left footed players playing in the following three positions. These three positions are chosen as they are left-sided positions and are positions where teams and coaches seem to value playing a left-footed player: 

- Left back 

- Left centre back 

- Left wing 

These players are identified using StatsBomb game event data field _position_name_ . 

It is common for teams to make tactical changes including substitutions which result in more than one player playing in these positions within the same game. Where this is the case, we have identified a team as playing with a left footed player if they have had a left footer in that position for 50% of the game or more. 

When a team has played a left footed player in a key position for fewer than 10 games across the two seasons, we have excluded this team from our analysis. This is because the sample size of games is too small to be reliable. 

### **5.4 Action frequency and success rates** 

A variety of analyses have been used to evaluate what measurable difference left footers make to a match when they play in key positions. This study focuses solely on in-possession metrics and does not include out-of-possession events like interceptions or tackles, nor does it look at duel success. The key game event that is the focus of this study is passing. Passing is chosen because each pass can be denoted as a left or right foot pass in a way which a carry or dribble cannot. Passes with other body parts, e.g. head, have been excluded. Passes from set pieces have also been excluded. 

Analysis of passes has involved two different types of comparison: 

- Game event data for left footed players game vs right footed players. 

- Game event data for left footed passes vs right footed passes. 

**6** 



Both of these comparisons are valid and useful, although it is imperative to understand the difference between the two. The first compares all left and right foot passes for players who are left footed with all left and right foot passes for players who are right footed. The second compares all left foot passes for any player with all right foot passes for any player. (Note that for most analysis in this section, we remove the category ‘two-footed’ and focus only a player’s more dominant side – left or right). 

In some of the analysis, we use Expected Threat (or ‘xT’ for short) to value each pass. Expected Threat values regions on the pitch based on the likelihood that possession in that region results in a goal. Any transition between these regions, i.e., a pass, can therefore be valued based on the difference between the value of the end and start regions. The xT model has been trained on the same dataset of 1420 games. 

We also use the StatsBomb game event data field _pass_success_probability_ . This is a metric which expresses the probability that a pass is completed, i.e. it reaches a team mate successfully. The metric is based on a StatsBomb model which takes into account: the x,y co-ordinates of the start of the pass; the angle and distance of the pass; and whether there was pressure from an opponent on the passer of the ball. By comparing the accumulated pass success from the StatsBomb model with the actual completed pass success percentage, we can evaluate a player’s success at passing. 

Finally, in all pitch diagrams, the direction of play is left to right. 



## **6. Results** 

_Figures and tables which describe the key findings._ 

### **6.1 Distribution of footedness across men’s and women’s football** 

Overall, nearly one quarter of players were left-footed (n=1585, left=362, two-footed=51, right=1172). However, this varies widely between men’s and women’s football. In the WSL, only one in eight players were left-footed (n=509, left=62, two-footed=40, right=407). 

Interestingly, as seen in Figure 2, there was a larger proportion of two-footed players in the WSL than in Premier League and Serie A.  We will discuss this in more detail in the Discussion section later. 

**7** 













Left             Two               Right 

Figure 2: The percentage of players by foot and league (total players = 1585). 

Across all teams in the FIFA Women’s World Cup 2023, 15% of players were left-footed (n=356). However, this figure was generally higher for the more successful teams. Figure 3 shows the percentage of left footed players in each squad for five top European teams. England fielded two players who were left footed – Lauren Hemp and Alex Greenwood. This is a lower number than for the other European teams in the table, although care should be taken when interpreting this data as sample sizes of players are small for each nation. 











|% of left footed players|25%<br>4 out of 16|30%<br>6 out of 20|13%<br>2 out of 15|25%<br>4 out of 16|29%<br>4 out of 14|
|---|---|---|---|---|---|
|% of minutes played by<br>left footed players|28%|29%|16%|27%|30%|



Figure 3: The percentage of left footed players and minutes at FIFA Women’s World Cup 2023. 

Returning to club football, there is a great deal of variation in the percentage of left, right and two footed players between clubs. Figure 4 provides examples of some of the differences in footedness composition between clubs. For example, in the Premier League, 38% of Arsenal’s total game time was played by left footers, the most of any Premier League team. Conversely, at Brighton and Hove Albion, 80% of playing time was for right footed players. 

**8** 











20% two-footed                                      38% left footed                                     43% left footed 90% right footed                                     80% right footed                                  88% right footed 







Figure 4: Examples of club variation in footedness (% of total playing mins) 

Interestingly, we can look at the footedness distribution by nationality of player. Figure 5 shows this analysis, separately for WSL and for Premier League and Serie A. 









<!-- Start of picture text -->
      Left           Two             Right<br><!-- End of picture text -->



Figure 5: Footedness by nation of player (limited to eight nations with most players) 

In the WSL, English and Scottish players are more likely to be right footed compared to players with other nationalities. 81% of English players in the WSL are right footed (n=97). This trend is also similar in men’s football, where 74% of English players are right footed (n=147), a lower proportion than for other nations. 

Assuming that players with English nationality were developed in the English talent system (and Italian nationality in the Italian system in Serie A), we may conclude that ‘home grown’ players are less likely to left footed compared to players who are ‘imported’ talent from other nations. 

An analysis of left footed playing minutes by position shows that 83% of WSL left footers play at left back, left center back or left wing. This is a contrast to 56% and 54% in the Premier League and Serie A respectively. 

**9** 



By comparing the distributions of left footed ‘home grown’ players and left footed ‘imported’ players, we can identify positions where left footed imported players are more likely to play. This analysis seems to show that left footers are bought into the WSL and Serie A to play in central midfield positions, and in the Premier League to play left center back. These appear to be the positional gaps in the player pool which clubs need to fill by sourcing left footers from overseas. 

### **3.1 Impact of footedness on match outcomes** 

In order to demonstrate how we have assessed the impact of footedness on match outcomes, we will use the example of Chelsea Women’s FC, winners of the WSL in both the season’s we have used data for: 







Figure 6: Chelsea Women’s FC – actual points vs predicted points, all games 

Over the two seasons, Chelsea have 43 games included in our model. Based on three points for a win and one point for a draw, they gained an actual 113 points for their performances in these 43 games. However, our match prediction model predicted they would gain 88.8 points (PredPoints). We conclude that Chelsea have outperformed their predicted points by 0.56 points per game. This is the biggest ‘overperformance’ of any of the 59 teams included in the analysis. 







Figure 7: Chelsea Women’s FC – actual points vs predicted points, all games vs. games with a left footed LCB 

Figure 7 shows the same data but also includes a column for games where Chelsea played with a left footed left centre back (almost always Magdalena Eriksson). For the 11 games when Eriksson played, Chelsea accumulated 30 points compared to a predicted total of 21.8. They outperformed their expected points by 0.75 points per game. This is an even higher overperformance than in their total sample of games (0.75 vs. 0.56) and we can conclude that Chelsea Women performed better with a left footed centre back than without one. 

**10** 



Using the same method, and combining the results of all 59 teams, we can evaluate the difference of playing a left footed player at left back and left centre back. 

### <u>Left footed left backs</u> 

- a) Overall, there are 53 teams (from 59) who played a left footer played at left back for 10 games or more. These are the teams we will include in our analysis. 

- b) On average, these teams performed better with a left footer at left back than with a right footer at left back. 

- **c) This difference can be calculated at 0.8 points over a 38 games season. This is our calculation of the difference of playing a left footer at left back for 50% of the time or more.** 

### <u>Left footed left centre backs</u> 

- The difference in performance of playing a left footed centre back is positive but very small. 

### **3.1 Action frequency and success rates** 

In this section, we will examine the measurable affect left footers make to the game by exploring and comparing game event data. 

For context, and to help make sense of the data and visuals in this section, Table 2 presents the estimated percentage of total game time for left and right footed players in key positions. For example, over all three divisions and two seasons, clubs deploy left footed players at left back for 78% of the time. 

||Left<br>footed|Right<br>footed|
|---|---|---|
|Left back|78%|22%|
|Left centre back|56%|44%|
|Left wing|16%|84%|



Table 2: Usage of left and right footers in key positions (estimated game time, based on number of game actions) 

### **3.1.1 In-possession involvement** 

Firstly, Figures 8-10 plot heat maps for the three key positions: left back, left centre back and left wing. Each position has two heat maps, one for left footed players and one for right footed players. The heat maps include in-possession actions. 

**11** 







Figure 8: Heat map, in-possession actions, left backs, by dominant foot (n actions = 217,407 left, 61,450 right) 

Although the heat maps in Figure 8 for left backs seem very similar, there are some small but important differences. The lighter areas - which indicate areas of higher involvement – stretch further to the left of the pitch for the left footed left backs. This shows that they have more involvement higher up the pitch, nearer the opponent’s goal. 





Left footed players Right footed players 

Figure 9: Heat map, in-possession actions, left centre backs, by dominant foot (n actions = 237,950 left, 190,651 right) 

Figure 9 focuses on left centre backs. Again, keen observation is needed to spot differences. However, look at the area on the left side of the pitch, past the half-way line. The left footed left centre backs have more involvement in more advanced wider areas than their right footed counter parts. 

**12** 







Left footed players Right footed players 

Figure 10: Heat map, in-possession actions, left wingers, by dominant foot (n actions = 31,791 left, 170,036 right) 

In figure 10, the heat maps are for left wingers. The right footed left wingers seem to be involved more often in the opponent’s penalty area, whereas the left footed left wingers are more likely to stay wide. 

### **3.1.2 Direction of passing** 

Next, we will look at a pass flow map, which shows the involvement of players in each section of the pitch, alongside the mean angle of pass made in that section. This is shown for left footed and right footed players in figure 11. This heat map includes completed passes only. Higher involvement is indicated by lighter areas. 





Left footed players Right footed players 

Figure 11: Heat map, with mean pass angles, completed passes, by dominant foot (n actions = 297,117 left footed, 617,000 right footed) 

It is expected that left footed players will have more involvement on the left side of the pitch and right footed players on the right. This is confirmed by the distribution of lighter-coloured squares in the heat maps.  More interesting is the angle of passes: For left footed players on the left side, these are in a slightly more attacking direction than for right footed players on the left. Likewise, right footers on the right side of the pitch pass the ball in more attacking directions than left footers on the right. So, we can 

**13** 



conclude that players playing on the same side of the pitch as their dominant foot seem to play forward more often. 

### **3.1.3 Switches of play** 

Figure 12 shows switches of play for left backs, broken down by which foot is used to make the switch. The plots use the StatsBomb _pass_switch_ game event data field and only include completed passes. 





Left foot passes Right foot passes 

Figure 12: Heat map, with mean pass angles, completed passes, by dominant foot (n actions = 696 left, 249 right) 

Left backs make nearly three times as many switches of play with their left foot as they do with their right foot. (For context, left footed left backs play approximately 3.5 times the number of minutes as right footed left backs do). The left foot switches are on average two metres longer than the right foot switches. Finally, the switches of play appear to happen higher up the pitch when the left foot is used, when compared to when the right foot is used. 

### **3.1.4 Pass completion** 

Using StatsBomb _pass_success_probability_ game event data field, we can calculate the expected proportion of completed passes a player should make. We can then compare this to their actual pass completion rate to see how well they perform against expected. For example, for left footed left backs using their left foot, they are expected to complete 80% of passes and their actual percentage completion is 81%. So they overperform by a very small margin. The same analysis has been carried out for left backs and left centre backs by dominant foot and by passing foot. The only combination that doesn’t overperform is right footed left backs using their left foot. These players had the lowest expected pass completion (77%) and did not achieve better than this expectation. 

### **3.1.5 Crossing from the left side** 

A statistical test has been carried out to determine whether teams who play left footed players at left back and left centre back achieve more crosses from the left side of the pitch than teams who don’t play with left footed players in these positions. 

**14** 



Table 3 shows the results of these tests. Each team performance is defined as either 1 or 0, where 1 indicates they played a left footer for 50% of the game or more and 0 indicates that they didn’t. For example, teams who played a left footed at left back for at least half the game achieved an average of 5.8 crosses from the left per game. This is compared to 5.2 crosses per game for teams who didn’t play a left footer at left back for at least half the game. 

|**State**|**Left footed LB for**<br>**more than 50% of**<br>**game**|**Left footed LCB**<br>**for more than 50%**<br>**of game**|**Left footed**<br>**players playing**<br>**more than 20% of**<br>**total mins**|
|---|---|---|---|
|1 (Yes)|5.8|5.7|5.7|
|0 (No)|5.2|5.1|5.1|
||t < 0.01|t < 0.01|t < 0.01|



Table 3: Mean number of crosses from the left (total team performances, n = 1276) 

The final row shows the result of a t-test to compare the two game states, 1 and 0. In all three cases, the t-test shows a statistically significant difference between the two means, and we can conclude that playing left footers makes a real increase in the number of crosses achieved on the left wing. 

Further to this analysis, we can calculate that playing a left footer at left back and left centre back, each for more than 50% of the time, gives a team 29 more crosses from the left side per season (based on a 38-game season). 

### **3.1.6 Expected threat by area of the pitch** 

Expected Threat values regions on the pitch based on the likelihood that possession in that region results in a goal. Any transition between these regions, i.e., a pass, can therefore be valued based on the difference between the value of the end and start regions. The xT model has been trained on the same dataset of 1420 games. 

Overall, the mean xT for left footed and right footed passes is the same. However, there is variation in xT across the pitch, with left footed passes carrying highest threat in left attacking and defending areas. 

Figure 13 shows the difference in the xT between left foot passes and right foot passes in sections of the pitch. Yellow areas indicate that left foot passes are higher threat in this area, and blue areas indicate that right foot passes are higher threat in this area. 

**15** 





<!-- Start of picture text -->
_Left foot has higher mean xT _   |      _Right foot has higher xT _<br><!-- End of picture text -->

Figure 13: Mean percentage difference in xT between right foot passes and left foot passes (n, all completed passes= 961,411) 

There is wide variation in differences in mean xT, depending on x,y pitch position. In the defensive corners of the pitch, there is the largest difference between using the left foot and right foot to pass the ball. For example, in square a5, the dark blue colour shows the mean xT for passes originating in this part of the pitch is much greater if the right foot is used. This may indicate an advantage of playing left footed left backs and right footed right backs, as full backs will be key positions that cover these defensive corners of the pitch. 

There is also some difference in mean xT in the attacking corners of the pitch. The yellow f1 and f2 squares indicate that left footed passes are of higher threat in these areas. 

In lanes d and e, between the half-way line and the opposition penalty area, there doesn’t seem to be much difference in which foot is used. Right footed passes and left passes seem to carry equal threat, across the width of the pitch. These areas are ones where a right footed left winger may cut inside. It may also be where a highly skilled number 10 threads forward passes using either foot. This could make a case for two footed players being most effectively deployed in these zones. 

On the subject of xT, it should also be noted that players had 6% higher xT when passing with their stronger foot than when passing with their weaker foot. 

### **3.1.7 Expected threat by position** 

The final analysis in this section examines the xT and angle of passes for key left footed positions, comparing the difference between left footed players and right footed players. The analysis is presented 

**16** 



in sonar plots where the length of the wedge is equal to the proportion of total pass count. A darker colour indicates higher mean xT. The direction of play is left to right. 





<!-- Start of picture text -->
>0.030<br>0.030<br>0.028<br>0.026<br>0.024<br>0.022<br>0.020<br>0.018<br>0.016<br><0.016<br><!-- End of picture text -->

Figure 14: Left backs: Proportion of pass count (length of wedge) and xT (colour), by dominant foot (n, left=52, 094, right=15,215) 

The two sonar plots may look very similar, but there are some key differences. Most importantly, if we look at the length of the wedges, we can see that right footed left backs seem more likely to pass infield whereas the left footed left backs have longer wedges leading diagonally forward (where the colour is darkest and the xT is highest). 



<!-- Start of picture text -->
>0.030<br>0.030<br>0.028<br>0.026<br>0.024<br>0.022<br>0.020<br>0.018<br>0.016<br><0.016<br><!-- End of picture text -->



Figure 15: Left centre backs: Proportion of pass count (length of wedge) and xT (colour), by dominant foot (n, left =69,676, right=57,387) 

Figure 15 shows the same analysis and presentation for left centre backs. Again, the differences are small. However, right footed left centre backs appear to be more likely to play the ball infield. Left footed left centre backs appear to have a wider angle of higher threat passes, with three darker wedges leading in attacking directions compared to two for their right footed counterparts. 

**17** 





<!-- Start of picture text -->
>0.030<br>0.030<br>0.028<br>0.026<br>0.024<br>0.022<br>0.020<br>0.018<br>0.016<br><0.016<br><!-- End of picture text -->



Figure 16: Left wingers: Proportion of pass count (length of wedge) and xT (colour), by dominant foot (n, left=5,468, right=30,983) 

Figure 16 shows the sonar plots for left footed and right footed left wingers. Here the differences are more obvious and striking. Right footed left wingers are much more likely to play the ball diagonally backward whereas left footers are more likely to play the ball directly infield, and with higher threat. 



## **7. Summary of results** 

_A summary of what have we found._ 

The following bullet points summarise the key findings in our results: 

### **7.1 Distribution of footedness across men’s and women’s football** 

- a) Overall, one quarter of players are left-footed. 

- b) The percentage of players who are left footed is twice as high in men’s football compared to women’s football. 

- c) The use of left footed players in major women’s European national teams is about 27%-30% of playing minutes. For England women, this figure is approximately half this much. 

- d) Left footed players are much more likely to be played in key left footed positions in women’s football than in men’s football. 

- e) There is a great deal of variation in the percentage of left, right and two footed players between clubs. 

- f) ‘Home-grown’ players are less likely to be left footed when compared to ‘imported’ players. 

- g) Left footers are ‘Imported’ into the WSL and Serie A to play in central midfield, and in the Premier League to play left centre back. 

### **7.2 Impact of footedness on match outcomes** 

**18** 



- a) Based on our analysis, there is small but limited evidence to suggest left footers impact match outcomes. 

- b) The value of playing a left footer at left back for 50% of the time or more is calculated at 0.8 points over the course of a 38-game season. 

- c) The value of playing a left footer at left centre back is positive but insignificant. 

### **7.3 Action frequency and success rates** 

- a) Left footed left backs seem to be more involved higher up the pitch, in more attacking areas, when compared to right footed left backs (although the difference is small). 

- b) Left footed left centre backs seem to be involved in wider attacking areas, when compared to right footed left centre backs. 

- c) Players pass the ball in more attacking directions from wide areas if they are playing on the same side of the pitch as their dominant foot. 

- d) Left backs make three times as many switches of play with their left foot as they do with their right foot, the switches are higher up the pitch, and on average two metres longer. 

- e) Playing left footers makes a real increase in the number of crosses achieved on the left wing. Playing a left footer at left back and left centre back, each for more than 50% of the time, gives a team 29 more crosses from the left side per season 

- f) Overall, the mean xT for left footed and right footed passes is the same. However, there is variation in xT across the pitch, with left footed passes carrying highest threat in left attacking and defending areas. 

- g) Players had 6% higher xT when passing with their stronger foot than when passing with their weaker foot. 

- h) Playing left footed players in key left footed positions effects the angle of passes and xT of these passes. For example, left footed left backs seem to make higher xT infield passes than right footed left backs. 



## **8. Discussion and further work** 

_What do these conclusions mean for football development and what further work is required to understand this even better?_ 

### **8.1 The relationship between left-footed minutes and winning games is complicated** 

There are a number of important contextual considerations which deserve discussion in our investigation into the effect of left footers on match outcomes. These are summarised below. 

Budget 

- Richer clubs will be able to afford more left footed players as well as other better players. Highquality left footed players are limited and therefore expensive. This may mean that a richer club 

**19** 



is successful because it is rich, rather than because it has more left footed players. In relation to on-pitch achievement, it is hard to disentangle wealth from footedness. 

### Team selection 

- Right footed left backs and left centre backs are likely to be secondary options and play more games against weaker opponents or when the first choice left footed option is injured. Therefore, it could be possible that right footed players in certain positions are not getting the same level or challenge of opponent as the alternative left footed option. 

### Tactics and strategies 

- Coaches can implement ways of playing which negate the effects of having fewer left footed players. If a coach knows they don’t have good left footed options, they will adjust the way they play to be successful with right footers on the left. Many teams have won trophies and tournaments with very few left footers, if they have coaches and tactics which nullify any potential disadvantage. 

Together these contextual factors may act to distort the relationship between left footers and match outcomes and make it hard to identify any real trend. To some extent it may be possible to consider budget and account for it in a model (adjusting for transfer value, for example), however team selection and tactics and strategies are harder to control for. 

Our research found a small but limited advantage of playing left footers in key left sided positions and was able to quantify this as approximately one point a season (if they play a left footer at left back for at least 50% of the time). However, how much weight can we put on this finding given the contextual complexities described above? 

It makes sense to coaches and football analysts that left footers in left sided positions can provide better attacking options. However, more work is needed to fully understand the measurable advantages of these options. 

### **8.2 Women’s football in England may not produce and develop as many left footers as it should** 

Probably the most significant finding of this research is the large difference in footedness between the women’s WSL and the men’s Premier League and Serie A players. Existing work has shown that there may be a slightly lower proportion of non-right footers among females than males (4% difference between males and females, see section 4.1). However, the difference between WSL and men’s elite football is larger than this. Left footers seem to be twice as common in the men’s leagues with just 12% (one in eight) of WSL footballers are left footed compared to 26% in the Premier League and Serie A (one quarter). 

In addition, analysis of key European women’s World Cup squads shows many nations are able to reach the 25%-30% left footers in elite female football that is exemplified in elite men’s football in the Premier League and Serie A. This seems to suggest that the low proportion of left footers in the WSL is not so 

**20** 



much a female-specific issue but an _England_ female-specific issue. Assuming English players in the WSL and England World Cup squad are products of the English talent system, then the key discussion needs to be centred around the following key question: 

- Why is the English female talent system not developing the expected proportion of high-quality left footed players? 

Some of the clues to help answer this question may be found in this research. We found that 83% of female left footers play in the key left sided positions (left back, left centre back and left wing), compared to much lower proportions in elite men’s football. With left footers being rare in the WSL, it is not surprising they are deployed more often to wide areas. It is likely that the left footers experience of the English club youth system is similar: they were deployed almost solely to wide positions. A hypothesis then arises as follows: Their talent journey has perhaps not been as varied in experience as it needs to be to develop the decision-making skills and game understanding more deeply acquired by game experiences in central, more crowded positions. 

More work is needed to explore this hypothesis, for example exploring footedness and positional variation across ages and stages in grassroots clubs, talent centres and academies. If the hypothesis is found to have merit, then there are consequences for club and national technical staff across talent identification, talent development and talent selection. In particular: 

- Positional variation during the development journey needs to be widened and a firm positional decision may need to be delayed until an older age. 

- The characteristics used to profile a player into a position need to be considered beyond what a player can achieve now and more widely than physical or biometric attributes like current speed or height. 

### **8.3 Two footed players** 

This research has focused on left footed players playing left footed positions. However, there is also a need for similar work to consider the two-footed player. We saw earlier that these players are rare, although more common in the WSL (8%) than in the Premier League and Serie A (2%). 

Figure 17 shows the three two-footed players who have achieved highest mean xT and have played more than 500 passes, one for each division. The figures plot their highest threat passes, five with their left foot in red and five with their right foot in blue. 

**21** 















Figure 17: Examples of the most two footed players from each league (minimum 500 passes completed) 

Lia Wälti is an interesting player as her highest threat passes seem to have such little variation. She plays in left midfield, typically more defensively minded than attacking. All ten of her high-xT passes come from and enter into the same area of the pitch. This is a good example of what a two-footed player can provide: consistent threat and no compromise in decision-making, regardless of which foot the ball is to be played on. 

Raphaël Varane and Kevin Bonifazi both play right centre back. Their variation in high-threat passes provide impressive examples of what two-footed players can achieve if they play further back in more defensive areas. Varane has the ability to play dangerous longer-range passes with either foot. Bonifazi has the most variation in pass start location among the three players, demonstrating his passing ability in attacking areas of the pitch as well as more defensive areas. 

The technical requirements of elite football are becoming more demanding, with players needing to be able to control the ball in tighter areas, play at greater speed, make quicker decisions and have fewer touches of the ball per possession. Talent systems and coaches may wisely consider the development of two-footed players to be a better long-term aspiration than the development of more left footers. 

**22** 


