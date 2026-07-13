<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/undated/undated - A model-based risk-impact analysis of dribble actions in women's soccer - Beckman et al.pdf -->

# **A model-based risk-impact analysis of dribble actions in women’s soccer** 

Competition Track: Soccer Paper ID 193959 

## **1. Introduction** 

In soccer, offensive actions can mainly be split into three: shots, passes and dribbles. Interestingly, numerous research and model development has been done to quantify the value of shots (Anzer and Bauer 2021; Baron et al. 2023) and passes (Rein, Raabe, and Memmert 2017; Forcher et al. 2021; Anzer and Bauer 2022). In contrast, comprehensive studies on dribbles (Magdaci 2022) are rare to be seen, although dribbling in soccer is a crucial dimension of offensive play. These actions not only serve as a tactical element for overcoming compact defensive lines and creating new attacking options, but also enable the creation of space and force the defense to shift.  Hence, more emphasize should be put on analyzing dribbles in the context of individual ball handling and decision-making skills in 1v1 situations. 

To fill this gap in the scientific literature, we introduce a new model-based approach to quantify individual dribbles in this work.  In addition, acknowledging the limited study of women’s soccer so far, we have applied our models to dribbles in the Women’s World Cup 2023, while the approach and model are also applicable to men’s soccer. We use event data as it is more widely available than positional data in practice - especially in women's soccer, where tracking data coverage is still relatively low. 

In our approach, we undertake a comprehensive analysis of dribbles, in which both the risk and impact factors are considered. First, a distinct risk variable is developed to reflect the probability of success of a dribble. Therefore, following the model presented by (Forcher et al. 2023), we formulate a model to forecast the success of a dribble based on event data. Second, we derive a superior Expected Threat model (Singh 2018), which also accounts for the effects of adversary pressure, to quantify the impact of a dribble. In contrast to different previous approaches to quantify the value of dribbles, such as VAEP (Decroos et al. 2019) or Expected Possession (Fernández et al. 2019), an Expected Threat model has the advantage that it is risk independent. This is useful within our approach as it allows us to analyze the risk and the impact dimensions of a dribble separately respectively complementary. 

By combining our two model approaches, significant insights are generated for soccer clubs. For instance, we demonstrate which players consistently surpass expectations in their dribbling during the World Cup. Furthermore, we dissect which positions are more prone to risky dribbling. Lastly, we unveil how individual teams' playing philosophy can be disclosed by presenting the peril of their dribbling in a visual format. The results have an immediate impact for coaches and players for individual and team development as well as opponent preparation and for scouts and recruiters in assessing new hires for their teams. 

The remainder of the paper is structured as follows. Section 2 presents the data as well as our novel model to quantify the risk and reward of a dribbling for an offensive team. The latter part of this Section is divided into two parts: first, we introduce a new machine-learning approach to estimate 



1 

the success probability of a dribbling. Second, we develop an advanced pressure-dependent Expected Threat (xT) model, which allows us to measure the impact of a dribbling in an offensive attack in different pressure statuses. In Section 3, we present various use-cases, in which the derived model from the previous Section is applied in contexts like scouting or match analysis. Section 4 offers concluding remarks. 

## **2. Methods** 

### **2.1. Data** 

We use Stats Bomb’s 360 event stream data (StatsBomb 2023), which is extracted from broadcast video and consists of the regular human-annotated event stream data enhanced with snapshots of player positioning. Those snapshots capture the location and relationship of the ball carrier to all other players (teammates as well as opponents) visible in the video during each on-the-ball action. To ensure a meaningful Expected Threat model, we trained the model on all 509 publicly available women games from the StatsBomb data. For the risk analysis and the final use cases in Section 3, we use all 64 matches of the women’s world cup 2023. 

In contrast to StatsBomb, we use the terms dribbles and carries interchangeably as we aim to evaluate all actions in which female players carry the ball, regardless of whether they aim to gain space or bypass. 

### **2.2. Quantitative estimation of dribbling success** 

To accurately assess a player's dribbling ability, it is crucial to consider not only the success rate but also the expected success rate. Dribbling past several opponents towards the opponent's penalty area poses significantly greater difficulty than advancing the ball down the sidelines in a one-on-one situation. To assess the dribbling skills of players objectively, we have developed a model that calculates the probability of successful dribbling. 

Unlike the expected threat model, we are not considering the value of a dribble, but the target variable is purely to maintain possession of the ball in one’s own team, which we call dribble success. When discussing dribble risk, we refer to the probability of the opposite: 

𝐷𝑟𝑖𝑏𝑏𝑙𝑒 𝑠𝑢𝑐𝑐𝑒𝑠𝑠 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 = 1 – 𝑑𝑟𝑖𝑏𝑏𝑙𝑒 𝑟𝑖𝑠𝑘 

### **2.2.1. Factors influencing dribbling risk** 

Several factors impact the success of dribbling. Initially, we considered opponents and their effect on the likelihood of losing the ball. Thus, we evaluated the distance of the nearest opponents (“opponents_within_5m”, “opponents_within_10m”), the numerical superiority of opponents near the ball (“numerical_superiority_5m”, “numerical_superiority_10m”) and the pressure given by them (“tagged_pressure”, “calculated_pressure”). Additionally, we formulated Key Performance Indicators (KPIs) based on the locations (“x”, “y”, “y_symm”) and consider the direction of the dribble (“dribblings_towards_opponent_goal”), because our analysis shows that the starting point of the dribble has a major influence on success (see Figure 1). The appendix contains a description of all KPIs. 

The available data is considerably limited as it only displays the positions of the players visible in the video, thereby impeding a comprehensive analysis of all player positions. Still, as the camera is usually focused on the ball, information about the surrounding players is often captured, allowing for the correct calculation of the Pressure Metric and numerical superiority in many cases. 



2 



_Figure 1 Dribbling success rates in different areas of the pitch._ 

### **2.2.2. Model design** 

Before training a prediction model, we evaluated mutual correlations between the features and eliminated those correlated features with the least predictive value, which were opponents_within_5m, opponents_within_10m, numerical_superiority_5m and y value (see appendix). Subsequently, we trained various models - Logistic Regression, XGBoost and Random Forest Classifier. From these, we chose the best model based on a test set (30% of all data), which was XGBoost. Finally, we calculated SHAP values for the ultimate model to clarify what constitutes a high success probability of a dribble. 

### **2.2.3. Results** 

The evaluation is based on the test set, which consists of a total of 13,999 out of 46,663 actions (30%) where female players carried the ball. From these, the players maintained possession of the ball in 12,518 (89,4%) situations. Our model predicted a ball retention in 41,805 (90,85%) situations. The F1 score is 0,92. For a complete evaluation including the confusion matrix, refer to Figure 2. 

|Ground<br>Truth|Precision|Recall|F1-Score|Support|Confusion|Matrix|Predic<br>0|tion<br>1|
|---|---|---|---|---|---|---|---|---|
|0|0.26|0.22|0.24|1481|Ground<br>Truth|0|331|1150|
|1|0.91|0.92|0.92|12518||1|950|11568|



_Figure 2 Evaluation of the risk model on out-of-sample test data._ 



3 

To comprehend the model's prediction, SHAP values were analyzed (see Figure 3). These indicate that the model focuses primarily on the calculated pressure. High pressure at the beginning of a dribble greatly diminishes the chance of success. The position on the field is also a crucial factor, with dribbling in the opposing half and along the sidelines having lower chances of success (for further reference see Figure 1).  Furthermore, it is crucial to maintain numerical superiority when dribbling near the ball, as ball losses are expected to increase due to opponent doubling efforts. Interestingly, the direction of the dribble is not of paramount importance, although dribbling towards one's own goal at least promises a slightly higher chance of success. 



_Figure 3 The SHAP values illustrate the significance and impact of the various variables._ 

### **2.3. Expected Threat with and without pressure** 

To calculate the contribution of a dribble to an offensive attack, we rely on an Expected Threat (xT) model (Singh 2018). In simple terms, an xT model divides the field into a grid _G_ and calculates a scoring probability in the next couple of actions for each cell _(x,y)_ of the grid (Soccerment.com 2021) . The xT value for each cell is defined as the sum of the shot threat (shot probability _s(x,y)_ multiplied with the scoring  probability _g(x,y)_ ) in the respective cell and the expected payoff of moving the ball (the sum of the xT values of all cells, weighted with the corresponding transition probabilities from the respective cell). 



The value gained by an action (like a pass or dribble) is the difference between the xT value at the end cell and at the start cell of the action. Compared to expected Goal ( _xG_ ) or expected Assist ( _xA_ ) models, which rely on shots or respectively passes, this approach has the advantage that the value of dribbles can also be analyzed. Furthermore, actions that do not lead directly to goal scoring opportunities but have a high value in the offensive build-up by progressing the ball to more dangerous areas on the pitch, can be measured and assigned to individual players (Soccerment.com 2021). 

In contrast to other studies using xT, we expand the model by calculating advanced xT values, which also consider the pressure the ball carrier is facing. This is necessary in our point of view, as xT measures the probability of scoring a goal in the next couple of actions and this value is not only dependent on the location of an event, but also on the pressure on the current ball carrier. For 



4 

example, shot, pass and dribbles success rates are highly correlated with pressure, so that pressure should be considered in a xT model as an additional input variable. 

To calculate pressure-dependent xT values, we use event-data from all matches in women’s competitions in the open-source StatsBomb library (509 matches). First, we compute conventional xT _(x,y; general)_ for each cell in our 30x20 grid, considering all relevant events in the dataset (see Equation 1).  We use these xT values later to refer to events, in which pressure is not observable or unknown. 

In a second step, we calculate shot probabilities _s(x,y)_ , shot success rates _g(x,y)_ and transition matrices _T(x,y)_ with different pressure status values ( _Pressure_ and _no Pressure_ ) for each cell in our grid _G_ . This allows us to solve the following Equation 2. 

xT(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠) = 𝑠(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠) ⋅𝑔(𝑥, 𝑦, 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠) ,----------------.----------------/ shot threat + (1 − 𝑠(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠)) ⋅ 𝑇(*,,)→(/,0)(𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠) ⋅xT(z,w; general) 4 (/,0)∈2 ,----------------------------.----------------------------/ move threat 

_Equation 2 The pressure-dependent Expected Threat (xT) Model_ 

Note that these two models also rely on the _xT(x,y; general)_ values, as they quantify game situations after a transition to a new cell, when the status of pressure is unknown. With this model approach, we get two additional xT values for each cell _(x, y)_ on the pitch: one with pressure _xT(x, y; Pressure)_ and one without pressure _xT(x, y; no Pressure)_ on the ball carrier (see Figure 4 for the results). 



<!-- Start of picture text -->
 on the ball carrier (see Figure 4 for the results).<br><!-- End of picture text -->



<!-- Start of picture text -->
and one without pressure  xT(x, y; no Pressure)<br><!-- End of picture text -->

_Figure 4 Expected Threat xT with pressure (left) and without pressure (right)._ 

Our approach has the advantage, that a successful dribble with pressure on the ball carrier is not only rewarded by the movement of the ball to a new cell _(a, b)_ (like in standard xT models), but also by the dissolving of the pressure situation: 

x𝑇!"#$(𝑥, 𝑦) = xT(a, b; no Pressure)– 𝑥𝑇(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒) = 𝑥𝑇(𝑎, 𝑏; 𝑛𝑜 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒)– 𝑥𝑇(𝑎, 𝑏; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒) + 𝑥𝑇(𝑎, 𝑏; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒)– 𝑥𝑇(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒) @AAAAAAAAAAAAABAAAAAAAAAAAAAC @AAAAAAAAAAAABAAAAAAAAAAAAC %#&&'()#$* ,-.&&/-. &#0/"0#'$ 1').2.$0 0' " $.3 ('4"0#'$ 

We can also calculate 𝑥𝑇6788 values for unsuccessful dribbles, which do not only take into account the loss of possession, but also the change in possession. 



5 

x𝑇6788(𝑥, 𝑦) = − xT(𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒 𝑆𝑡𝑎𝑡𝑢𝑠) – 𝑥𝑇(𝑃𝑖𝑡𝑐ℎ 𝐿𝑒𝑛𝑔𝑡ℎ − 𝑥, 𝑦; 𝑃𝑟𝑒𝑠𝑠𝑢𝑟𝑒) ,--------.--------/ ,-----------.-----------/ 6788 9: ;9<<=<<>9? @ABCDE FC G788E88F7C 

In addition, we can estimate (ex-ante) values 𝑥𝑇2BFC for unsuccessful dribbles (where we assume that the dribble would have ended in the neighboring cell nearest to the goal) as well (ex-ante)  values 𝑥𝑇6788 for successful dribbles, so that we have outcome-independent values for 𝑥𝑇2BFCand 𝑥𝑇6788 for each carry. Following this approach in combination with the estimation of dribbling success, these two variables 𝑥𝑇2BFC and 𝑥𝑇6788 allow us to calculate an expected value of 𝑥𝑇2BFC, which is basically the sum of both variables, weighted with the dribble success probability _p_ (introduced in the previous Section 2.2): 



This metric enables us to identify locations on the pitch, where dribbles generate (ex-ante) the most (or the least) value for a team as well as players, who take valuable (or invaluable) decisions by choosing to dribble (instead of passing or shooting). 

## **3. Use Cases** 

By comparing the determined success probability, the expected threat, and the actual success of dribbles, a multitude of questions can now be answered. A comparison of success probability and dribbling success allows for an evaluation of technical abilities, while the combined analysis of success probability and value quantifies the decision-making process of the players. 

The results can be aggregated at the player level for scouting purposes to identify players with desired skills. Aggregation at the team level provides insights for game analysis, both in preparation for the upcoming opponent's playstyle and in optimizing one's own tactics. By considering the analyses based on players' positions on the field, actionable instructions for female players can be derived and incorporated into their training. 

The following section presents selected application cases. To ensure comparable results, all analyses were normalized to a game duration of 90 minutes. To prevent outliers, we only considered players who played at least 60 minutes in the tournament. This excludes players who achieve a high value through a few actions in an extremely short amount of playing time. 

### **3.1. Frequent Overperformers** 

Looking only at the risk dimension, it can be inferred that certain players are capable of performing successful dribbles much more consistently than others. To assess a player's skill, we calculate the predicted success rate for each individual dribble and compare it with the actual outcome. By adding up all of a player's dribbles and standardizing them to 90 minutes of playtime, we can determine their ability to exceed expectations and therefore evaluate their overall skill level. Figure 5 displays players who have the highest median in dribbling more successful than predicted. The boxplot shows the 



6 

outcome for all individual dribbles of the players, meaning that if a player dribbles successfully although the prediction was only 20%, it achieves a value of 0.8 for that dribble. 



<!-- Start of picture text -->
Figure 5 Overview how much the dribble outcomes of the best performers (highest median) exceeded the expectation.<br><!-- End of picture text -->

_Figure 5 Overview how much the dribble outcomes of the best performers (highest median) exceeded the expectation. Player photos taken from fifa.com._ 

### **3.2. Dangerous dribbles in the opponent’s half** 

Looking at all dribbles from all players in general, we can see that the distribution of dribbles is roughly symmetrical, i.e., that roughly the same number of dribbles take place in both halves of the pitch. Going one step further, two important findings can be confirmed with the help of our metrics: Firstly, dribbles in the own half are mainly about overcoming space and do not generate much immediate threat. They are mainly taken in situations with much less risk. On the other hand, dribbles in the opponents' half are used to create scoring chances. Dribbling that starts just outside the penalty area produces the highest 𝑥𝑇2BFC. 



<!-- Start of picture text -->
2BFC.  .<br><!-- End of picture text -->



_Figure 6 Amount of carries and dribbles (left), Sum of expected threat (xT) from successful dribbles (right)._ 

### **3.3. The teams' playing philosophy: Germany, England and Spain** 

Building on the general distribution of xT, one can analyze how individual teams play. Clear and concise overviews permit match analysts to gain insights rapidly. For instance, Germany is especially dangerous on the very left lane and the half right lane of the pitch. A comparison of the two finalists, 



7 

Spain and England, indicates that the Spanish are creating much more goalscoring threat through dribbling. 



<!-- Start of picture text -->
dribbling.<br><!-- End of picture text -->





_Figure 7 Comparison of the_ 𝑥𝑇!"#$ _per match by successful dribbles of Germany (top), England (left) and Spain (right)._ 

### **3.4. Combined analysis of risk and expected threat** 

Combining both models, one can gain additional insights. Figure 8 shows the average expected threat gain of successful dribbles in relation to the taken risk that players achieved during 90 minutes of playing time, where the bubble size shows the averaged normalized number of carries per player. This analysis compares different field positions, including the outer and inner lanes, to assess the risk and return associated with each. In practice, analysts can filter this diagram for particular teams, allowing for direct conclusions to be made about their playing style. 



8 



_Figure 8 Comparing risk and successful xT gain of players normalized to 90 minutes of playing time._ 

### **3.5. Outperforming XT** 

Finally, we can compare reality with the expected xT gain variable, which was introduced in Section 2.3. Players who have scored significantly more xT than can be expected by their situations demonstrate both a willingness to take risks and high technical skills. The top players of this category are shown in Figure 9. 



_Figure 9 Comparing Risk and successful xT gain of players normalized to 90 minutes of playing time._ 

_Player photos taken from fifa.com._ 



9 

## **4. Conclusion** 

Despite their obvious importance, there is a research gap in the systematic evaluation of dribbles. Closing this gap, we quantified the quality of dribbling by introducing an anticipated success rate that is dependent on the player's position and surrounding opponents. We then assessed the resulting dribbling value using an advanced expected threat model, which considers the opposition's nearby pressure since it significantly increases the threat of an action. Hence, this work allows a more comprehensive understanding of the importance of dribbles in the game of soccer. 

Our model gives practical insights to analysts and scouts, which they can use to identify key skills in players and to develop training methods. To demonstrate this, we have investigated the best dribblers, positional differences and team’s playing philosophy in the 2023 Women’s World Championship. We therefore identified players that continuously achieve high (or low) value dribbles at an above (or below) expected success rate or weaknesses in team defenses and provided drilldowns to analyze specific game situations, areas on the pitch or also formation-dependent behavior. 

In future work, further practical relevant cases relating to dribbles can be quantified. Dribbling is particularly effective in tight situations, as it allows players to get past tightly packed defenders and create dangerous situations in the penalty area. The psychological impact on opponents should not be underestimated either, as successful dribbles can boost a player's confidence and influence the morale of opponents, which can lead to more defensive behavior. Players with strong 1-on-1 dribbling skills can destabilize the opponent's defense by bringing unpredictability to the game. This helps to break tactical structures and allows the attacking team to advance into dangerous positions on the pitch. 



10 

## **References** 

Anzer, Gabriel, and Pascal Bauer. 2021. “A Goal Scoring Probability Model for Shots Based on 

   - Synchronized Positional and Event Data in Football (Soccer).” _Frontiers in Sports and Active Living_ 3. https://www.frontiersin.org/articles/10.3389/fspor.2021.624475. 

- ———. 2022. “Expected Passes.” _Data Mining and Knowledge Discovery_ 36 (1): 295–317. https://doi.org/10.1007/s10618-021-00810-3. 

- Baron, Ethan, Nathan Sandholtz, Timothy Chan, and Devin Pleuler. 2023. “Miss It Like Messi: Extracting Value from Off-Target Shots in Soccer.” arXiv. http://arxiv.org/abs/2308.01523. 

- Decroos, Tom, Lotte Bransen, Jan Van Haaren, and Jesse Davis. 2019. “Actions Speak Louder Than Goals: Valuing Player Actions in Soccer.” In _KDD ’19: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , 1851–61. https://doi.org/10.1145/3292500.3330758. 

- Fernández, Javier, F C Barcelona, Luke Bornn, and Dan Cervone. 2019. “Decomposing the Immeasurable Sport: A Deep Learning Expected Possession Value Framework for Soccer.” _Sloan Sports Analytics Conference_ . 

- Forcher, Leander, Tobias Beckmann, Oliver Wohak, Christian Romeike, Ferdinand Graf, and Stefan Altmann. 2023. “Prediction of Defensive Success in Elite Soccer Using Machine Learning - Tactical Analysis of Defensive Play Using Tracking Data and Explainable AI.” _Science and Medicine in Football_ 0 (0): 1–16. https://doi.org/10.1080/24733938.2023.2239766. 

- Forcher, Leander, Matthias Kempe, Stefan Altmann, Leon Forcher, and Alexander Woll. 2021. “The ‘Hockey’ Assist Makes the Difference—Validation of a Defensive Disruptiveness Model to Evaluate Passing Sequences in Elite Soccer.” _Entropy_ 23 (12): 1607. https://doi.org/10.3390/e23121607. 

- Magdaci, Ofir. 2022. “Evaluating Football Dribbling Skill by Utilizing the Elo Algorithm.” Medium. January 24, 2022. https://towardsdatascience.com/evaluating-football-dribbling-skill-byutilizing-the-elo-algorithm-9c6aa384b991. 

- Rein, Robert, Dominik Raabe, and Daniel Memmert. 2017. “Which Pass Is Better?” _Human Movement Science 55 (2017): 172-181_ . 

- Singh, Karun. 2018. “Introducing Expected Threat (xT).” https://karun.in/blog/expectedthreat.html. 

- Soccerment.com. 2021. “Expected Threat.” _Soccerment_ (blog). December 6, 2021. https://soccerment.com/expected-threat/. 

- StatsBomb. 2023. “StatsBomb Release Free 2023 Women’s World Cup Data.” StatsBomb | Data Champions. August 23, 2023. https://statsbomb.com/news/statsbomb-release-free-2023womens-world-cup-data/. 



11 

## **Appendix** 

Description of all calculated features: 

|**Feature**|**Description**|
|---|---|
|x|Start location of the dribble (x-coordinate)|
|y|Start location of the dribble (y-coordinate)|
|y_symm|Start location of the dribble (symmetric y-coordinate, measuring the distance from the<br>center)|
|dribbling_towards_opponent_goal|Whether the player dribbles towards the opponent’s goal (=1) or not (=0)|
|numerical_superiority_5m|Number of teammates subtracted by number of opponents within 5 m distance to the<br>start location of the dribble.|
|numerical_superiority_10m|Number of teammates subtracted by number of opponents within 10 m distance to the<br>start location of the dribble.|
|opponents_within_5m|Number of teammates within 5 m distance of the start location of the dribble.|
|opponents_within_10m|Number of teammates within 10 m distance of the start location of the dribble.|
|calculated_pressure|Own pressure calculation based on surrounding opponents at start location of a dribble:<br>it is a piecewise linear function mapping distances to pressures, ensuring a minimum of<br>zero and a maximum of 1, derived from specific distance-pressure pairs (0 m → 1, 2 m →<br>0.5, 10 m → 0).|
|tagged_pressure|“under_pressure” variable from StatsBomb which indicates whether a player was under<br>pressure during an action or not.|



We eliminated some highly correlated features, such as opponents within 10 meters, by observing the correlation matrix: 





12 


