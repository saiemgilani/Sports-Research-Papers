<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2024/2024 - The coach's dilemma how a yellow card can change the course of a match - Unknown Authors.pdf -->



# **The coach's dilemma: how a yellow card can change the course of a match.** 

Oleg Durygin, Daniil Gumin, Egor Gumin XGLAB.PRO 

## **Introduction** 

In football, each action can have an impact on the outcome of the game, and a yellow card is a significant factor. Yellow cards are an integral part of football games, serving as a tool for controlling aggressive behavior and reducing the occurrence of rule infringements. However, their impact extends beyond simply penalizing individual players, as they can influence the course of a game, the decisions made by coaches, and the overall strategy of teams. This study aims to investigate the effects of yellow cards on player behavior, team decision-making, and opponent actions. We aim to explore how coaches can utilize data to make informed decisions that minimize risks and enhance team performance. 

Coaches must weigh the potential consequences of keeping a player on the field after issuing a yellow card against the risks of having them removed from the match. This decision-making process can significantly impact the dynamics of the game and the strategies employed by both teams. 

One of the significant challenges that coaches encounter after a player has received a yellow card is the decision on whether to substitute them. On one hand, retaining a player on the field carries the risk of receiving a second yellow card, which may result in their dismissal and weaken the team's performance. Conversely, premature substitution may adversely affect the team's overall attacking potential and efficiency. In this research, we aim to address the question: How do yellow cards influence football players' playing style, and should coaches consider substituting them? 

To achieve this, we will investigate how players adjust their play after receiving a yellow card and how these adjustments affect team strategy. Furthermore, we will analyze how opposing teams take advantage of such alterations. Modern analytical techniques, such as xYC (expected yellow card) and examining player and team performance changes based on statistical data, will be utilized. 

**1** 



## **Methodology** 

To achieve the objectives of our research and answer the key questions regarding the impact of yellow cards in football, we will utilize match data collected through the StatsBomb platform. This data comprises both event-based and 360 information for 2 seasons in the Italian Serie A and English Premier League leagues 1160 matches). 

### **2.1. The Impact of Yellow Cards on Player Performance and Opponent Strategies** 

Receiving a yellow card in a football match can often be an important turning point not only for the team whose player received the yellow card, but also for the opposing team. The opposing team may adjust its tactics by exerting increased pressure on the warned player in an attempt to provoke additional violations or disrupt his ability to control the course of the game. This can lead the cautioned player to become more conservative and less successful in defending their own area. 

### **2.1.1 Data Selection** 

We only considered players who: 

- Played the full match 

- Received exactly one yellow card 

- Were not sent off 

### **2.1.2 Defining Player Control Zones** 

To test our hypothesis, we introduced the concept of a "player control zone." We divided the pitch into 30 equal rectangles 6 along the length and 5 across the width) and analyzed the frequency of player actions in each rectangle, filtering out outliers. This approach resulted in a digital heat map of player activity on the field, allowing for a more nuanced analysis than traditional nominal positions. **ADD IMAGE** 

### **2.1.3 Analyzing Player Movement** 

We compared players' heat maps before and after receiving yellow cards. On average, players were active in 8.83 zones before receiving a yellow card and 8.6 zones after. While 6.16 zones overlapped, players typically ceased activity in 2.67 zones and became active in 2.44 new zones after being cautioned. 

It's worth noting that the average yellow card is given between the 60th and 70th minute, which may conflate the effects of the yellow card with typical late-game tactical shifts. 

### **2.2. xYC - Expected Yellow Card** 

**2** 



Metrics such as expected goals (xG) and assists (xA) have been widely used by coaches and analysts to assess the effectiveness of offensive play. However, there remains an under-researched area that has a significant impact on the outcome of matches: the risk of receiving a yellow card for committing a foul. 

To solve this problem, we propose to introduce a new indicator - the expected yellow card (xYC), which would allow us to predict the probability that a player will receive a warning. To create the xYC model, the gradient boosting method CatBoost) will be used, which allows you to effectively analyze complex datasets and identify nonlinear dependencies. 

### **2.2.1 Data Selection** 

To create a reliable xYC model, we excluded second yellow and red cards during the data preparation stage. The dataset was then split into training and test sets: 

- **Training Set** : Data from the 2022/2023 seasons of the Italian Serie A and English Premier League 580 matches). 

- **Test Set** : Data from the 2023/2024 seasons of the Italian Serie A and English Premier League 580 matches). 

In the initial phase, we tested various machine learning approaches, including gradient boosting, logistic regression, and neural networks, to evaluate different classification models using tabular data. Ultimately, CatBoost emerged as the most effective model, delivering the best performance metrics. 

The model's input features include 1 

- Minute of the match 

- Number of visible opponents 

- Number of visible teammates 

- Distance to the nearest defender 

- Play pattern 

- Number of defenders positioned between the actor and the goal 

- Player position 

- Offensive value OBVagainst before the event 

- Offensive value OBVfor before the event 

- Advantage after a foul committed 

- Number of visible opponents within 5 meters 

- Number of visible teammates within 5 meters 

- Number of fouls committed in the match before current foul 

- Number of fouls committed by the team before current foul 

**3** 



### **2.2.2 Limitations** 

- **No Video Files.** One major limitation of our dataset is the absence of video files. This restricts the ability to visually validate and contextualize fouls and gameplay interactions in real-time using computer vision models. Such validation could enhance the understanding of player behavior and the context surrounding the fouls. 

- **Lack of Referee Positioning in 360 Data** . Another constraint is the unavailability of referee positioning data within the 360 dataset. The refereeʼs location and sightline play a significant role in decision-making during matches. Without this information, it becomes impossible to analyze how the refereeʼs proximity and visual angle may influence foul and card assessments, potentially impacting the reliability of the xYC predictions. 

- **Missing Jersey Numbers in 360 Data.** The absence of jersey numbers for players within the 360-degree data limits our ability to create reliable tracking information. This gap hinders the detailed analysis of player movements, speeds, and the spatial relationships between the player committing the foul and the opposing player at the moment of the incident. 

- **Cumulative Fouls and xYC Evaluation.** Recognizing that fouls can be a cumulative factor in refereeing decisions, where yellow cards may be awarded based on an accumulation rather than a singular incident, we focused solely on the first foul committed by each player in a match to isolate and accurately assess expected yellow card (xYC) probabilities. 

### **2.2.3 Metrics** 

While addressing the classification problem, conventional binary classification metrics proved insufficient, as our objective extended beyond a simple binary outcome to estimating the probability of an event. Therefore, we adopted the Brier Score 2as a primary metric to evaluate the accuracy of probabilistic predictions, providing insight into the calibration of our model's outputs. 



Figure: Brier Score definition 

Additionally, we utilized RMSE Root Mean Square Error) 3to further assess the deviation between the predicted probabilities of receiving a yellow card and the actual outcomes, ensuring a comprehensive evaluation of predictive performance. 

**4** 





Figure: RMSE definition 

For thorough validation, we also calculated traditional classification metrics such as Balanced Accuracy, F1 Score, and ROC AUC, which offered supplementary perspectives on the modelʼs effectiveness in identifying positive and negative instances accurately. 

### **2.2.4 Calibration** 

Platt Scaling Calibration 4is a linear method effective for cases where the model tends to underestimate or overestimate probabilities uniformly across the entire probability range. This technique adjusts the model's output by fitting a logistic regression model to the predicted probabilities, resulting in more reliable probability estimates. 



Figure: Platt Scaling Calibration definition. 

Isotonic Regression Calibration 5, on the other hand, is a monotonic, nonlinear method suitable for correcting complex distortions in the model's predictions. It proves particularly useful when the model exhibits local variations, such as overestimating or underestimating probabilities in specific ranges, allowing for more flexible probability calibration and improved reliability. 



Figure: Isotonic Regression definition 

While Platt Scaling and Isotonic Regression are commonly applied independently, using them in sequence can be beneficial for models where correcting both global bias and local deviations is essential. This dual approach can be particularly advantageous for high-calibration precision tasks, ensuring more accurate probability estimates. 

### **2.3. Fouls analysis** 

The purpose of this research is to identify trends related to fouls and examine how players and referees respond to them in various game scenarios. We are considering not 

**5** 



only quantitative indicators of fouls, but also geographic and temporal trends, as well as possible leniency on the part of referees towards specific players and situations. This study will assist coaches in gaining a better understanding of the risks associated with fouls and adapting their strategies based on the specific context of each match. 

As part of this part of the study, we solve the following tasks: 

- Referee Leniency Towards High xYC Players: Evaluating whether referees exhibit leniency towards players who commit fouls with high expected yellow card (xYC) scores. 

- Referee Leniency Towards High-Foul, Low xYC Players: Investigating referee behavior towards players who accumulate a high number of fouls but maintain low xYC scores. 

- Geographic Distribution of Fouls: Mapping foul locations on the field to identify areas where yellow cards are most commonly issued. 

- Temporal Patterns of Fouls: Analyzing when fouls are most likely to occur during a match to understand time-based trends. 

- Number of Fouls Before Receiving a Yellow Card: Determining the average number of fouls committed by a player before receiving a yellow card. 

The objectives outlined above lead to the following hypotheses: 

- Geographic Distribution of Fouls: Certain areas of the field are more likely to result in a yellow card being issued, supporting the analysis of foul locations. 

- Impact of Increasing xYCAs the danger associated with fouls (xYC score) increases, the subsequent foul—even if less dangerous—is more likely to result in a yellow card, which relates to understanding referee leniency towards high xYC players. 

- Referee Leniency: Referees may show leniency towards players who commit numerous fouls but maintain low xYC scores, linking to the investigation of how referees handle players with a high number of low-risk fouls. 

We explored the relationship between the total number of fouls and their associated risk, as represented by the xYC metric. To achieve this, we created xYC danger categories based on quantile distribution: 

- Low xYC 

- Medium xYC 

- High xYC 

For each player, we recorded the number of fouls per match and calculated the mean xYC value for their fouls. 

**6** 



## **Results** 

### **3.1 Quantitative Analysis: Opponent Attack Patterns** 

We first examined the number of attacks through a player's control zone before and after they received a yellow card. We mapped all opponent possessions to the zones they passed through and calculated the percentage of attacks that intersected with the cautioned player's control zones. 

Contrary to our hypothesis, we found no significant difference in the proportion of attacks going through a player's control zone before and after they received a yellow card. 

### **3.2 Qualitative Analysis: Threat of Opponent Attacks** 

To assess the quality of attacks, we utilized the `obv_for_net` parameter, which indicates how much each opponent's action increases their probability of scoring. We calculated the sum of `obv_for_net` values for opponent possessions both inside and outside the player's control zone, before and after the yellow card was issued. 

Our analysis revealed that: 

- Before receiving a yellow card, an average of 29.915% of the opponent's offensive value ( `obv` ) was generated in the player's control zone. 

- After receiving a yellow card, this figure was 29.844%. 

This minimal difference further disproves our initial hypothesis. 

### **3.3 xYC** 

As part of the study, we developed the xYC metric, which allows us to predict the probability of a player receiving a yellow card based on a number of factors. The xYC model has shown relatively high accuracy in predicting whether players will receive yellow cards. 

Figure: Key feature importances of the CatBoost model 

|**Feature name**|**Importances**|
|---|---|
|x coord|19.11|
|foul_committed_advantage|10.60|
|visible_opponents|10.53|



**7** 



|play_pattern|7.78|
|---|---|
|position|6.86|
|minute|6.75|
|visible_teammates|5.63|
|obv_for_before|5.49|
|num_fouls_by_match|5.47|
|obv_against_before|4.55|
|y coord|4.28|
|distance_to_nearest_defender|3.53|
|num_defenders_on_goal_side_of_actor|3.41|
|visible_teammates_in_5_meters|2.45|
|num_fouls_by_team|2.24|
|visible_opponents_in_5_meters|1.25|



Figure: Result metrics 

|**Metric name**|**Value**|
|---|---|
|Brier score|0.082|
|RMSE|0.287|
|Balanced Accuracy|0.67|
|F1 score|0.31|
|ROC AUC|0.67|



Our findings suggest that the likelihood of receiving a yellow card is influenced by factors such as the player's field position, movement speed, and the distance between the referee and the incident. However, despite the promising results, certain limitations must be acknowledged when applying the xYC model. A major limitation is the absence of video footage, which restricts a comprehensive assessment of fouls. While statistical data and event information offer valuable insights, they only provide a partial understanding. Situational context, such as the referee's interpretation of player intent, contact intensity, or the behavior of involved players, often cannot be fully captured without video analysis. 

**8** 



Figure: xYC distribution on test dataset. 



### **3.4 Fouls analysis** 

In this section, we provide an overview of card-related statistics and analyze the patterns associated with fouls and yellow cards in matches. This analysis helps illustrate how referees' decision-making can be influenced by the context of fouls and game aggression levels. 

To understand the distribution of fouls and card issuance, we present the following summary of events: 

Figure: Card overview. 

|**Event**|**Number of event**|**Percentile of fouls**|
|---|---|---|
|Foul|30677|100%|
|Yellow card|3611|11.77%|



**9** 



|Second yellow card|67|0.21%|
|---|---|---|
|Red card|55|0.17%|



These figures highlight the proportion of fouls resulting in disciplinary actions, emphasizing the relatively low frequency of second yellow and red cards. 

To further contextualize these findings, we examined the average number of fouls required for a player to receive a yellow card: 

Figure: Mean number of fouls for receiving yellow card. 

|**Mean number of fouls for receiving yellow**<br>**card**|**Value**|
|---|---|
|Per player|1.67|
|Per team|8.86|
|Per match|16.54|



These values indicate how fouls accumulate before a caution is issued and provide insight into referee behavior and game management. 

We visualized the distribution of fouls using a heatmap, which demonstrated that fouls are most frequently committed in the central areas and along the flanks, aligning with the main zones of player interactions. This finding highlights the significance of the x-coordinate feature in the xYC model. 

**10** 



Figure: Heatmap of fouls. 



Similarly, an analysis of yellow card distribution revealed that yellow cards are most often issued in a teamʼs own half, reflecting a pattern of strategic defensive behavior. 

**11** 



Figure: Heatmap of yellow cards. 



To deepen our understanding, we calculated the probability of a player receiving a yellow card based on the number of fouls committed for different levels of foul severity. Our findings indicate that in games with low degrees of danger, a greater number of fouls are required for a player to receive a yellow card. However, in games with medium or high degrees of danger, even a single foul can lead to a yellow card being given. 

**12** 



Figure: Number of fouls per for receiving yellow card for each dangerous degree. 



Further analysis indicated an inverse relationship between the number of fouls committed and the average xYC value. This trend suggests that players who commit a large number of minor, non-threatening fouls are less likely to be penalized with a yellow card, pointing to a degree of referee leniency. A bar chart illustrating this relationship confirmed that as the number of fouls required to receive a yellow card increases, the average xYC value per foul decreases, emphasizing how cumulative minor infractions can impact referee decisions. 

**13** 



Figure: Mean xYC score per foul for number of foul per player bar chart. 



In summary, our research highlights that in matches characterized by lower levels of aggression, players generally need to commit more fouls before receiving a yellow card. Conversely, in more aggressive games, even minor infractions may result in yellow cards. Additionally, our study confirmed that referees often display greater leniency towards players who commit numerous non-aggressive fouls. 

Our analysis revealed that: 

- We developed and trained an xYC model to predict the probability of a player receiving a yellow card. 

- In games with a low degree of danger, the number of fouls required per player to receive a yellow card tends to increase. 

- In medium or high-danger matches, a single foul may be sufficient to result in a yellow card. 

- There is a notable relationship between the total number of fouls committed by a player and their xYC value, suggesting that referees may be more lenient towards players who commit multiple low-risk fouls. 

**14** 



## **Model Applications** 

The findings from our research indicate that receiving a yellow card does not have a significant impact on a player's overall performance. This insight can guide coaches to make more informed decisions, helping them avoid unnecessary substitutions after a player receives a yellow card. Coaches can trust that players will generally be able to continue fulfilling their roles effectively even after being cautioned. 

Practical Applications and Future Directions: 

- **Coaching Strategy.** Our results provide valuable recommendations for coaching staff, suggesting that yellow cards do not critically diminish a player's defensive or offensive contributions. This can lead to more strategic use of substitutions and better resource management during matches. 

- **VAR System Integration.** A promising application of our xYC model lies in its potential integration into the Video Assistant Referee VARsystem. By incorporating xYC data, an automated tool could be developed to assist referees in making more informed decisions, particularly in contentious situations. This approach could add an additional layer of objective data to support judgment calls. 

- **Automated VAR Systems.** Looking ahead, overcoming current limitations could pave the way for the development of a fully automated VAR system. Such a system would leverage our xYC model to enhance decision-making processes and contribute to more consistent refereeing. 

## **Conclusion** 

Our findings indicate that receiving a yellow card does not significantly affect a player's performance. Specifically, there is no substantial change in the frequency of opponent attacks targeting the area controlled by the cautioned player, nor in the effectiveness or danger level of these attacks. This suggests that players are generally able to maintain their level of play even after being shown a yellow card. 

These insights can help coaching staff make more informed and strategic decisions, reducing the perceived need for immediate substitutions when a player receives a yellow card. Coaches can be confident that a cautioned player will likely continue performing effectively for the remainder of the match. 

Through our analysis, we successfully developed and trained an xYC model to estimate the probability of a player receiving a yellow card. Our observations showed that in matches with lower intensity, players typically need to commit more fouls before receiving 

**15** 



a caution. Conversely, in higher-stakes or more aggressive matches, even a single infraction may be sufficient to draw a yellow card. Additionally, we identified a pattern in which players who commit numerous low-risk fouls tend to have lower xYC values, indicating that referees may exercise more leniency in such cases. 

These findings offer valuable insights into how yellow card dynamics unfold, contributing to more nuanced match preparation and player management strategies. 

## **References** 

1 Statsbomb. (n.d.). _open-data/doc/StatsBomb Open Data Specification v1.1.pdf at master · statsbomb/open-data_ . GitHub. 

https://github.com/statsbomb/open-data/blob/master/doc/StatsBomb%20Open%20Data%20Spec ification%20v1.1.pdf 

2 Wikipedia contributors. (2024, September 11). _Brier score_ . Wikipedia. https://en.wikipedia.org/wiki/Brier_score 

3 Wikipedia contributors. (2024b, October 15). _Root mean square deviation_ . Wikipedia. <u>https://en.wikipedia.org/wiki/Root_mean_square_deviation</u> 

[4] Wikipedia contributors. (2024b, September 15). _Platt scaling_ . Wikipedia. https://en.wikipedia.org/wiki/Platt_scaling 

[5] Wikipedia contributors. (2024d, October 24). Isotonic regression. Wikipedia. <u>https://en.wikipedia.org/wiki/Isotonic_regression</u> 

## **Appendix** 

**16** 



Figure: A bar chart of the number of fouls per player for receiving a yellow card. 



**17** 



Figure: A bar chart of the number of fouls per team for receiving a yellow card. 



**18** 



Figure: A bar chart of the number of fouls per match for receiving a yellow card. 



**19** 


