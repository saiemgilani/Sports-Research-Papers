<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2023/2023 - An Events and 360 Data-Driven Approach for Extracting Team Tactics and Evaluating Performance in Football - Unknown Authors.pdf -->



# **An Events and 360 Data-Driven Approach for Extracting Team Tactics and Evaluating Performance in Football** 

### Paper Track 

Calvin Yeung<sup>1</sup> and Rory Bunker<sup>2</sup> 

Graduate School of Informatics, Nagoya University, Nagoya, Japan. 

## **Abstract** 

The collective behaviour of opposing multi-agent teams has been extensively researched in game theory, robotics, and sports analytics. In sports, team tactics frequently encompass individuals’ strategic spatial and action behaviours, and can be manifested in sequences of events during periods of possession in football. The analysis of team tactics is critical for training, strategy, and ultimately team success. While conventional notational and statistical analysis approaches can provide valuable insights into team tactics, contextual information has generally been overlooked, and teams' performance has not been holistically evaluated. To consider contextual information, we employed the sequential pattern mining algorithm PrefixSpan to extract team tactics from possessions, the Neural Marked Spatio Temporal Point Process �NMSTPP�model to model expected team behaviour for a fair comparison between teams, and the Holistic Possession Utilisation Score �HPUS�metrics to evaluate teams’ possessions. In the experiments, we identified five team tactics, validated the NMSTPP model when StatsBomb 360 data was incorporated, and analysed the English Premier League �EPL�teams in the 2022/2023 season. The results were visualised using radar plots and scatter plots with mean shift clustering. 

## **Introduction** 

The study of collective behaviour exhibited by opposing multi-agent teams holds significant importance across diverse domains such as game theory �1�, robotics �2�, and sports analytics �3�. This interdisciplinary field delves into comprehending how multiple agents interact and cooperate within various contexts, drawing insights from areas like multi-agent systems, distributed artificial intelligence, and behaviour-based robotics. This exploration encompasses investigating coordination and decision-making mechanisms, ultimately contributing to advancements in optimising team tactics and strategies in competitive scenarios. 

> 1 yeung.chikwong@g.sp.m.is.nagoya-u.ac.jp 

> 2 rory.bunker@g.sp.m.is.nagoya-u.ac.jp 

**1** 



In sports analytics, team tactics encompass the way in which individual players strategically manage their positioning and adapt to opponents during a game, with the aim of launching successful attacks �4�. These tactics are not always clearly defined, as they often change subtly or are even created spontaneously to avoid corresponding responses by the opposing team. The extraction and evaluation of a team's tactical style are critical for strategy, training, and performance evaluation. 

Literature on football, which is summarised in the recent review of Plakias et al. �5�, has mainly utilised clustering and statistical methods to analyse players' trajectories and location data to extract the (historical) styles of play of teams. However, these existing approaches face limitations in terms of evaluating teams’ actions and tactical performance and also exclude contextual information. Meanwhile, existing performance metrics, e.g., VAEP �6�, provide predicted probabilities with respect to only one event type by estimating the probabilities of scoring/conceding. To offer a more comprehensive evaluation of performance, a more holistic events prediction approach, which can predict a wider range of event types<sup>3</sup> and incorporate inferred spatio-temporal information, would be desirable. 

In this study, sequence pattern mining, an unsupervised learning technique that considers contextual information, was used to extract team tactics present within a sequence of actions and distinct zones during each possession. Furthermore, StatsBomb Event (on-ball event information including time, location and event type �7��and 360 freeze-frame data<sup>4</sup> (all visible players’ information from the broadcast video, including location, teammate, actor, and keeper) were incorporated into the Transformer-based Neural Spatio Temporal Point Process �NMSTPP�deep learning model �8�. The NMSTPP model predicts the action types, zones, and interevent times of the average team's subsequent events. This approach, which uses the Holistic Possession Utilisation Score �HPUS��8�, allows a fair comparison between different teams on how likely a possession will lead to an effective attack. Furthermore, possessions can be differentiated and valued using the extracted tactics. Finally, the tactics and performance of English Premier League �EPL�teams in the 2022/2023 season were analysed and visualised using radar graphs and mean shift clustering �9�. 

The remainder of this paper is structured as follows. First, related studies on team tactics extraction and evaluation are discussed. The proposed methodology is then thoroughly explained. The experimental results, which summarize the extracted tactics, are then presented, and the NMSTPP model with incorporated StatsBomb 360 freeze-frame data is validated and applied to the 2022/2023 EPL season. Finally, the paper is concluded. 

> 3 For example, obtaining the predicted probability of the next event being a cross. 

> 4 More details can be found at https://statsbomb.com/what-we-do/soccer-data/360�2/ 

**2** 



## **Related Work** 

This section discusses the current literature methodology and limitations in the extraction and evaluation of team tactics. 

#### **1. Team Tactics Extraction** 

Football team tactics have been extracted using a variety of analytical methods. By analysing passing patterns and possession statistics, researchers thoroughly examined - two primary attacking styles "Direct" and "Possession-based" �15�. The length and frequency of passes distinguish these styles, with "Direct" emphasising longer passes and "Possession-based" emphasising shorter passing sequences and ball control. The investigation of width-based tactics, such as crossing, has also aided in the comprehension of team strategies. Discriminant analysis, clustering, regression, and dimensionality reduction have been used to uncover patterns in player behaviour, providing valuable insights into team tactics �5�. Furthermore, passing networks, also known as flow motifs, have been used in �13��16�. Moreover, combining passing networks and passing positions �17�, as well as player information �18�. 

While existing tactics extraction methods provide valuable insights, they have inherent limitations. Traditional notational and statistical analysis techniques can produce useful results, but they exclude contextual information, limiting the overall understanding of team strategies �19�. Furthermore, tactical movement is not strictly labelled and identified by teams; because tactics used can subtly vary there is a large variety of tactics used. This demonstrates Sequential Pattern Mining's potential as a promising avenue for gaining comprehensive insights into team tactics. 

In this context, Sequential Pattern Mining, exemplified by methods like PrefixSpan introduced by �10�, offers a viable solution to the shortcomings of existing tactics extraction methods. Unlike conventional statistics, Sequential Pattern Mining delves deeper into football matches, enabling the revelation of nuanced tactical insights. This algorithm systematically analyses sequences of on-ball events performed by teams during matches, effectively identifying recurring patterns and dependencies. By uncovering these sequential patterns, PrefixSpan illuminates the underlying structure of team strategies, showcasing the specific sequences of actions or zones that teams employ to gain an advantage. Our study aims to establish further links between tactical analysis and real-world team performance in the English Premier League by applying this technique to historical event data and extracting sequential patterns linked to diverse playing styles, contributing to a deeper understanding of football strategies. 

**3** 



#### **2. Team Tactics Evaluation** 

Evaluating player actions in the context of a football match has conventionally relied on match statistics like goals, assists, and number of events in the final third. However, these statistics are primarily centred around goals, which are rare occurrences. This limitation poses a challenge when trying to assess player actions that don't directly result in goals. To address this issue, researchers have proposed metrics that assign value to actions based on the expected probability of specific outcomes. 

The cornerstone metric in this realm is the Expected Goal (xG) metric �20��21�, which estimates the likelihood of a goal. Similarly, the Expected Goal Value �EGV��22�, Dangerousity �DA�metric �23�, and Expected Probability of Shot On Target (xSOT��3� evaluate the potential of goals and shots on target. Expected Assist (xA)<sup>5</sup> gauges the anticipated probability of an assist, while Expected Threat (xT)<sup>6</sup> quantifies a player's offensive threat. Moreover, Valuing Actions by Estimating Probabilities �VAEP��6�, Goal Impact Metric �24��25�, Statsbomb's OBV<sup>7</sup> and ASA's G�consider changes in the likelihood of scoring or conceding due to different actions. Going beyond individual players, metrics like Off-Ball Scoring Opportunity �OBSO��26��27�and C�OBSO �28�, VDEP �29� and GVDEP �30�assess the value of off-ball players and defenders respectively. 

However, these metrics have largely focused on evaluating individual actions or players, leaving a gap in evaluating collective team actions during possession sequences. Addressing this gap, the Seq2Event model �31�predicts the expected location and event type at time 𝑡 based on events from 𝑡−1 to 𝑡−40. The Possession Utilisation score (poss-util) quantifies the probability that a predicted event will lead to an attack, similar to xG, but modelling the behaviour of an average team. This allows the evaluation of team possessions. Enhancing this approach, �8�introduced the Neural Marked Spatio Temporal Point Process �NMSTPP�model, incorporating temporal factors and point process concepts. The Holistic Possession Utilisation Score �HPUS�builds upon poss-util by considering expected interevent time and location, with a focus on the end of possessions to avoid overemphasising numerous actions. 

In this study, we leverage the NMSTPP model and HPUS to enhance evaluation. Our incorporation of StatsBomb 360 data, including off-ball player coordinates and additional details, has further improved the NMSTPP model's performance. More information on this enhancement can be found in the subsection Team Tactics Evaluation. 

> 5 Example of xA�https://statsbomb.com/articles/soccer/unpacking-ball-progression/ 

> 6 xT�https://karun.in/blog/expected-threat.html 

> 7 OBV�https://statsbomb.com/articles/soccer/introducing-on-ball-value-obv/ 

**4** 



## **Proposed Methods** 

In this section, the method to extract team tactics will be introduced first, followed by the method to evaluate the possession consisting of team tactics, and finally, the approach for visualisation of the evaluation of team tactics. 

#### **1. Team Tactics Extraction** 

Team tactics can be understood as how players manage their spatial positions while adapting and interacting with the opponent over time to achieve successful attacks �4�. Tactical movements are not something that is strictly labelled and identified because they are subtly changed or created afresh in order not to be read by the opponent. Therefore, unsupervised learning techniques, e.g. sequential pattern mining, can be employed to reveal team tactics in the series of actions and corresponding zones that constitute each possession. 

**Step 1�Action Categorisation.** In order to focus on events relevant to team tactics, events describing discernible on-ball actions were categorised and retained. The categorisation method is outlined in Table 1. A "possession end" action was appended as the last action of each possession (defined by StatsBomb). The remaining StatsBomb events not referenced were excluded, and the percentages were calculated from the train set, as will be elaborated upon in the Dataset and Preprocessing subsection. 

Table 1�StatsBomb event categorisation method 

|**Action Category**|**StatsBomb Event(s)**|**Percentage**|
|---|---|---|
|Pass|Half Start<sup>8</sup><br>Clearance<br>Pass �Not Corner/Cross)|48.06%|
|Dribble|Carry<br>Duel<br>Dribble<br>50/50|42.39%|
|Possession End|-|8.30%|
|Cross|Pass �Corner/Cross)|1.58%|
|Shot|Shot<br>Error<sup>9</sup>|1.25%|



> 8 In the StatsBomb data, the Half Start" is always followed by a pass, but for modeling purposes, we categorise it as Pass 9 According to the StatsBomb definition, an “Error” describes an event in which “a player is judged to make an on-the-ball mistake that leads to a shot on goal”. 

**5** 



**Step 2�Zone Segmentation.** To account for zones pertinent to team tactics, the pitch was divided into specific areas: own-half, opponent-wing, and opponent-central, as illustrated in the accompanying Figure 1. This segmentation drew inspiration from the concept of Juego de posición (position game), as depicted in Supplementary Figure 1. 



Figure 1�Pitch segmentation for zone sequence 

**Step 3�Sequential Pattern Mining.** The actions and zones that constitute each possession can be organised into possession sequences, such as [“pass”, “dribble”,..., ”shot”] and [“own-half”, “opponent-wing”,..., “opponent-central”], respectively. To extract patterns from possession sequences, the PrefixSpan algorithm �10�was employed. This algorithm has been widely used in data analysis for sequential pattern mining tasks, including pass sequences in football �11�. It is particularly effective at extracting recurrent patterns of varying lengths by extending subsequences, also known as prefixes. This flexibility renders PrefixSpan a valuable tool for recognising patterns in possession sequences that contribute to the team's tactics. 

#### **2. Team Tactics Evaluation** 

For the assessment of each possession, which is characterised by team tactics, we consider the likelihood of an average team executing an effective attack under similar circumstances. The Neural Marked Spatio Temporal Point Process �NMSTPP�model �8�is employed to model expected actions. By utilising this model, we are able to evaluate the possession's effectiveness using the Holistic Possession Utilisation Score �HPUS��8�. 

Furthermore, in this research, we enhance the NMSTPP model's performance by integrating StatsBomb 360 data. This augmentation serves to improve the model's performance. Subsequently, we conduct an in-depth analysis of team tactics, employing the HPUS and associated metrics. 

**6** 



**Step 1�Input and Target Features.** Following �8�, the target features to be predicted were the interevent time, zone, and action of the event occurring at time 𝑡. The input features encompassed the interevent time, zone, action, zone-derived features, and the StatsBomb 360 features of events from time 𝑡−1 to 𝑡−40. The details of the features are as follows: 

- Interevent time: The time difference in seconds between the current event and the previous event, ranging from 0 to 60. 

- Zone: The (x,y) coordinates of the event, which were translated into zones numbered 1 to 20 by employing the Juego de posición (position game) zoning method, illustrated in Supplementary Figure 1. 

- Action: Categorised from the StatsBomb event data and encoded arbitrarily. Additional details can be found in Table 1 above. 

- Zone-derived features: Encompass alterations in angle and distance between zones. 

- StatsBomb 360 features: The 360 data<sup>10</sup> captures player information present in the video frame for each event. This data includes five features: (x,y) coordinates, and binary indicators for goalkeeper, actor (the player executing the on-ball action), and teammate (associated with the player performing the on-ball action). In total, there are 5�22 features, as the video frame might not encompass all 22 players in an arbitrary order. Any absent player features in the captured frame are substituted with zeros. 

**Step 2�Modelling.** To integrate the StatsBomb 360 data into the NMSTPP model �8�, the StatsBomb 360 features were passed through a linear layer for information extraction and dimension reduction. Subsequently, these processed features were incorporated into the NMSTPP model. 

Figure 2 illustrates the architectural design of the NMSTPP model. Initially, the continuous features were passed through a linear layer to extract information and reduce dimensionality. Subsequently, a Transformer encoder �12�was employed to encode the features spanning from time 𝑡−1 to 𝑡−40, yielding a condensed vector serving as input for the subsequent phase. 

The subsequent stage involves the utilisation of three distinct neural networks. These networks were employed to forecast the interevent time, zone, and action, respectively. The neural networks executed predictions in a sequential manner, where the output from each preceding network served as input for the subsequent one. Ultimately, this process predicted the expected interevent time, zone, and action for the event at time 𝑡. 

> 10 More details can be found at https://statsbomb.com/what-we-do/soccer-data/360�2/ 

**7** 





Figure 2�Neural Marked Spatio Temporal Point Process �NMSTPP�model architecture incorporating the 360 features 

The model's loss function comprises the root mean square error �RMSE�for the interevent time and the cross-entropy loss �CEL�for the zone and action. RMSE and CEL are widely employed for continuous and discrete target variables respectively, where lower values indicate improved performance. Furthermore, to achieve a balance across the three losses, the RMSE was multiplied by a factor of 10 (determined via empirical observation in �8��. The cost function can be expressed as follows: 

𝐿𝑜𝑠𝑠= 10 × 𝑅𝑀𝑆𝐸 + 𝐶𝐸𝐿 + 𝐶𝐸𝐿 𝐼𝑛𝑡𝑒𝑟𝑒𝑣𝑒𝑛𝑡 𝑡𝑖𝑚𝑒 𝑍𝑜𝑛𝑒 𝐴𝑐𝑡𝑖𝑜𝑛 

We refer to the integration of the NMSTPP model and 360 features as NMSTPP�360. 

**Step 3�Tactics Evaluation.** With the expected events derived from the previous phase, we now possess the expected actions of an average team during each possession. To evaluate the possession, we can employ the Holistic Possession Utilisation Score �HPUS� �8�. The HPUS assigns a score to each action, termed the Holistic Action Score �HAS�, and accumulates these scores in an exponential manner, with a heightened focus on the concluding actions of a possession. Actions that effectively contribute to an attack near the opponent's goal are attributed a maximum HAS of 10, while a minimum possible HAS that can be assigned is 0. 

The formulae for computing HAS are outlined as follows, with the relevant areas depicted in Supplementary Figure 2� 

𝐻𝐴𝑆= 𝐸(𝑍𝑜𝑛𝑒)𝐸(𝐴𝑐𝑡𝑖𝑜𝑛|𝑍𝑜𝑛𝑒)/𝐸(𝐼𝑛𝑡𝑒𝑟𝑒𝑣𝑒𝑛𝑡 𝑡𝑖𝑚𝑒) 𝐸(𝑧𝑜𝑛𝑒) = 0𝑃(𝐴𝑟𝑒𝑎 1) + 5𝑃(𝐴𝑟𝑒𝑎 2) + 10𝑃(𝐴𝑟𝑒𝑎3) 

𝐸(𝐴𝑐𝑡𝑖𝑜𝑛|𝑍𝑜𝑛𝑒) = 0𝑃(𝑃𝑜𝑠𝑠𝑒𝑠𝑠𝑖𝑜𝑛 𝑒𝑛𝑑) + 5𝑃(𝐷𝑟𝑖𝑏𝑏𝑙𝑒, 𝑃𝑎𝑠𝑠) + 10𝑃(𝐶𝑟𝑜𝑠𝑠, 𝑆ℎ𝑜𝑡) 

- 𝐸(𝐼𝑛𝑡𝑒𝑟𝑒𝑣𝑒𝑛𝑡 𝑡𝑖𝑚𝑒) = 𝑚𝑎𝑥(1, 𝐼𝑛𝑡𝑒𝑟𝑒𝑣𝑒𝑛𝑡 𝑡𝑖𝑚𝑒) 

**8** 



The formulae for HPUS are outlined as follows: 



where 𝑛 is the number of actions in the possession. 

Moreover, the HPUS��8�serves as a metric for possessions that result in an “attack” (shot or cross). Specifically, HPUS�matches HPUS if the possession encompasses a shot or cross; otherwise, HPUS�takes on a value of 0. Furthermore, the HPUS ratio �8�was employed to assess the degree to which the potential attack, indicated by HPUS, converts into an actual attack, as reflected by the value of HPUS�. This HPUS ratio was computed by dividing the cumulative HPUS�value across matches by the aggregated HPUS value. 

#### **3. Radar Graph and Mean Shift Clustering** 

To visualise the evaluation of team tactics, we employed radar graphs and mean shift clustering �9�, drawing inspiration from �13�. The Radar Graph was utilised for comparing possession performance across different tactics and teams. The radar graph parameters and corresponding values encompass the derived sequential patterns and possession metrics, HPUS, and HPUS�(see step 3 in the subsection Team Tactics Evaluation for more details on possession metrics). 

Furthermore, mean shift clustering �9�was employed to categorise distinct team performances based on different tactics. This approach considers the HPUS ratio along with the frequency of the employed tactics for clustering. Mean shift clustering belongs to the realm of unsupervised learning and clusters similar data points by iteratively moving them toward regions of high data density. It adapts to the distribution of the data and automatically determines the number of clusters. This characteristic renders it effective for grouping teams. For a more comprehensive understanding, refer to �14�. 

## **Experiments** 

This section first describes the dataset and the preprocessing procedures used. Next, we present the extracted team tactics. We then validate the NMSTPP�360 model. Finally, we demonstrate the application of the model in the context of the 2022/2023 English Premier League season. The code utilised for this study is accessible on GitHub<sup>11</sup> . 

> 11 https://github.com/calvinyeungck/Football-Match-Event-Forecast-v2 

**9** 



#### **1. Dataset and Preprocessing** 

The dataset employed in this study was generously provided by StatsBomb, encompassing matches from both the 2021/2022 and 2022/2023 English Premier League seasons. Each match entry includes both the StatsBomb event data and the StatsBomb 360 data. Essential information such as possession details, interevent time, zone, and action were derived from the event data, while the 360 features were extracted from the corresponding 360 data. Following �8�, to model each 45-minute game as a point process trial, to enhance data quality and to avoid instances of infrequent occurrences or unusual situations, matches involving own-goals were excluded from consideration. Furthermore, events confined within the regular 45-minute duration of each half during the match were retained for analysis. 

In order to streamline the required computational power, the second half of the 2021/2022 season was selected specifically for the extraction of tactics through sequential pattern mining and the subsequent training of the NMSTPP model for tactics evaluation. A split of the matches into training, validation, and testing sets was performed using an 80%/10%/10% distribution. It is noteworthy that the match dates were meticulously sorted in ascending order to prevent any form of look-ahead bias, ensuring that future match data did not influence the modelling of historical matches. Furthermore, the season of 2022/2023 was employed as an illustrative application example within this study. 

#### **2. Extracted Team Tactics** 

The process of extracting discernible patterns within the action and zone sequence during a possession involved the utilisation of the PrefixSpan algorithm �10�. Notably, Table 2 presents the tactics patterns that emerged with notable frequency, achieving a frequency level of approximately 30% �0.3 support). 

Table 2�Team tactics extracted with sequential pattern mining 

|**Tactics**|**Sequential Pattern**|**Frequency**<br>**�N�12,812�**|
|---|---|---|
|Pass Based|[pass]*7|30%|
|Dribble Based|[dribble]*7|32%|
|Alternating Pass-Dribble<br>Based|[pass,dribble]*5/[dribble,pass]*5|31%/30%|
|Opponent-Wing Based|[opponent-wing]*5|25%|
|Own-Half Based|[own-half]*5|43%|



**10** 



For the action sequences, three tactics were extracted: "pass," "dribble," and "pass follows dribble." These tactics exhibited a frequency of at least 30%. The "pass" and "dribble" based tactics encompassed a minimum of 7 of the corresponding actions, whereas the "alternating pass-dribble" tactic entailed the occurrence of "dribble" following a "pass" or vice versa, repeated at least 5 times. 

In terms of zone sequences, two tactics emerged: "opponent-wing" and "own-half" based tactics, displaying frequencies of 25% and 43%, respectively. Both of these tactics were characterised by a minimum of 5 events taking place within their respective segmentation. 

These patterns shed light on frequently encountered possession strategies. Notably, tactics such as "opponent-wing" based and "pass-based" possessions could be linked to strategies like wing-based tactics and ball-control tactics. The extracted tactics, combined with the HPUS metrics, hold promise for conducting comprehensive analyses of team tactics and performance, as detailed in the subsection dedicated to the application on the English Premier League 2022/2023 season. 

Nevertheless, it's essential to acknowledge that confirming such connections would necessitate an in-depth understanding of the game and the insights of experts, which were not accessible for this study. Therefore, the validation and more intricate exploration of the relationship between possession patterns and tactics remain avenues for future research. 

#### **3. NMSTPP�360 Model Validation** 

During the validation process of the NMSTPP�360 model, the emphasis shifted towards confirming the indispensability of the 360 features. As previously addressed in �8�, a comparative analysis was conducted involving the NMSTPP model, common neural point process models, and time series models. However, for this study, our focus lies specifically on assessing the enhancement achieved through the incorporation of the 360 features. Consequently, our investigation was directed towards evaluating whether the addition of the 360 features indeed improved the NMSTPP model's performance. 

In this context, a comparison was undertaken between the performance of the NMSTPP�360 model and the fine-tuned NMSTPP model �8�. Detailed performance metrics for both models are presented in Table 3. 

**11** 



Table 3�Performance of the models on the validation set 

|**Model**|**Total Loss**|**Interevent Time**<br>**RMSE**|**Zone CEL**|**Action CEL**|
|---|---|---|---|---|
|NMSTPP�360|3.01|0.07|1.59|0.68|
|NMSTPP|3.11|0.07|1.66|0.70|



The obtained results indicated an overall enhancement in the performance of the NMSTPP�360 model, with a reduction of 0.09 observed in the total loss. This improvement was attributed to changes in the zone cross-entropy loss �CEL�of �0.07 and the action CEL by �0.02. Remarkably, the interevent time root mean square error �RMSE� exhibited no change. These findings suggest that the incorporation of the 360 features facilitated a more precise prediction of the upcoming event's zone and action type with the NMSTPP model. 

With the confirmation of the positive impact of the 360 features on the NMSTPP model performance, we proceeded to validate the predictions of the NMSTPP�360 model, following the methodology outlined in �8�. The final model<sup>12</sup> was attained after fine-tuning the class weights in the cross-entropy loss using the validation set. Subsequently, we visualised the outcomes through cumulative distribution plots for the interevent time �Figure 3�, confusion matrix plots for the zones �Figure 4�, and confusion matrix plots for the actions �Figure 5�. These graphical representations offered insights into the model's predictive capabilities and provided a comprehensive assessment of its performance. 



12 The model code and parameters are available on GitHub: <u>https://github.com/calvinyeungck/Football-Match-Event-Forecast-v2</u> 

**12** 



Figure 3�NMSTPP�360 model cumulative distribution plot for the interevent time (scaled) prediction 



Figure 4�NMSTPP�360 model confusion matrix plot for the zone prediction 



Figure 5�NMSTPP�360 model confusion matrix plot for the action prediction (columns and row label: pass, dribble, possession end, shot, cross) 

Figure 3 revealed a noteworthy alignment between the cumulative distribution of the predicted interevent times and actual interevent times. This convergence indicated that the NMSTPP�360 model proficiently predicted the timing of subsequent events, as reflected in the congruity between the predicted and observed values. 

Moving on to Figures 4 and 5, both confusion matrices prominently displayed the highest percentage of entries along the diagonal, indicating a substantial proportion of accurate predictions. This robust alignment along the diagonal signifies that the NMSTPP�360 

**13** 



model aptly anticipated the forthcoming event's zone and action. This outcome underscored the model's efficacy in effectively predicting interevent time, zone, and action, thus reinforcing its overall performance. 

Together, these findings collectively highlighted the capability and reliability of the NMSTPP�360 model in making precise predictions across multiple dimensions of the possession scenarios. 

#### **4. Application on the 2022/2023 English Premier League Season** 

Within this subsection, our analysis delves into the English Premier League �EPL� 2022/2023 season, utilising the extracted team tactics and the assessment metrics linked to HPUS. The analysis leverages both radar plots and mean shift clustering for a comprehensive examination. Additionally, we extend the HPUS-related metric analysis, mirroring the approach outlined in �8�. The analysis of HPUS-related metrics shows significant correlations. Notably, the HPUS�metric exhibits substantial correlation with expected goals (xG), actual goals, and final team ranking of 0.87, 0.78, and �0.67, respectively, demonstrating the HPUS metric’s ability to unveil teams' offensive ability and performance. 

#### **4.1. Radar Plot** 

To assess team performance and their opponents for each tactic, we created radar plots in which each tactic served as a variable, and the HPUS/HPUS�values were depicted. The teams considered were Manchester City �1st place), Arsenal �2nd place), and the average performance of all teams in the EPL during the 2022/2023 season. 

Figure 6 presents four radar plots, representing various metrics: the average HPUS (top left), HPUS�(bottom left), opponent HPUS (top right), and opponent HPUS�(bottom right) values, aggregated per match. These plots provide a visual representation of the performance of the specified teams and their opponents in terms of their different tactics and offer insights into their strategic approaches throughout the season. 

**14** 











Figure 6�Radar plot for average (top left) HPUS, (bottom left) HPUS�, (top right) opponent HPUS, and (bottom right) opponent HPUS�value per match 

To begin with, observing Figure 6 (top left), in terms of the average HPUS per match, both Manchester City and Arsenal demonstrated the highest HPUS values in the opponent wing and alternating pass-dribble based tactics. Moreover, for the average team, the opponent wing based tactics exhibited the most elevated HPUS value, surpassing other tactics by more than 100 HPUS. This HPUS signified the potential of these tactics to lead to an actual attack (cross or shot) during possession. 

**15** 



Moving on to Figure 6 (bottom left), the average HPUS�per match unveiled distinct patterns. Manchester City has the highest HPUS�values in the dribble and alternating pass-dribble based tactics. For Arsenal, among the extracted tactics, all except for opponent wing-based yielded similar HPUS�values for the team. Meanwhile, the average team displayed relatively similar HPUS�values across all extracted tactics. HPUS� quantified the extent to which a possession's attacking potential is effectively realised. 

Further scrutiny of Figure 6 (left) for both HPUS and HPUS�illustrated the comparative performance of the three teams. Manchester City outshined Arsenal, which in turn surpassed the average team. This hierarchy suggested that Manchester City excelled in offensive prowess, proficiently generated possessions with attack potential, and successfully converted them into actual attacks. 

Additionally, though opponent wing-based tactics yielded high HPUS scores, their HPUS� values remained comparable to other tactics, particularly for the average team. This implied that while the tactics exhibited substantial potential for an attack, their successful conversion into an attack might prove challenging. 

Moreover, it was evident from the same figure that alternative tactics (others), not extracted in this study, significantly yielded lower HPUS and HPUS�scores for both Manchester City and Arsenal. This underscored that the extracted tactics are indeed the most effective in generating attack potential and converting it into actual attacks among the EPL's top teams. 

Finally, Figure 6 (right) unveiled the opponent performance of the teams. Notably, Manchester City's opponents managed to create more opportunities �HPUS�than those of Arsenal. However, the ability of Manchester City's opponents to translate these opportunities into actual attacks �HPUS�lagged behind that of Arsenal's opponents, indicating Manchester City's formidable defensive capabilities. When combined with the earlier findings, this observation might elucidate why Manchester City clinched the title, despite not consistently leading the league tables. 

#### **4.2. Scatter Plot with Mean Shift Clustering** 

When evaluating team performances within specific extracted tactics, the frequency of employing such tactics could wield a significant influence. This encompasses both the team's inclination toward the tactic and their proficiency in executing it. Leveraging the outcomes of mean shift clustering, teams within each cluster exhibited comparable possession counts utilizing the tactics. In the case of opponent wing-based tactics, Figure 7 provides a scatter plot illustrating the relationship between HPUS ratio, the frequency of possessions, and the cluster centroid from mean shift clustering. Furthermore, the frequency level cluster was summarised in Table 4. 

**16** 





Figure 7�Scatter plot for opponent wing based tactics frequency and HPUS ratio with mean shift clustering (grey X is the centroid of a cluster) 

Table 4�Opponent wing based tactics frequency level clusters 

|**Frequency Level Cluster**|**Team**|
|---|---|
|6|Liverpool|
|5|Manchester City, Brighton & Hove Albion,<br>Chelsea, Tottenham Hotspur, Manchester United|
|4|Arsenal, Leeds United,<br>Wolverhampton Wanderers, Leicester City|
|3|Aston Villa, Newcastle United, Crystal Palace|
|2|Fulham, West Ham United, Brentford,<br>Southampton, Everton, AFC Bournemouth|
|1|Nottingham Forest|



Analysing Table 4 and Figure 7, within frequency level cluster 5, we can draw a meaningful comparison between Manchester City and Manchester United's HPUS ratios within opponent wing-based tactics. Notably, Manchester City exhibits a substantially higher 

**17** 



HPUS� ratio, indicating their superior ability to effectively convert opportunities compared to Manchester United, even when both teams utilise this tactic with similar frequency. Additionally, it's noteworthy that traditional Big 6 teams generally exhibit higher HPUS ratios compared to other teams, with Brighton & Hove Albion and Fulham standing as exceptions. 

These insights derived from the table, figure, and scatter plot provide valuable perspectives on how teams' tactical preferences, frequency of use, and conversion efficiency collectively impact their performance within specific extracted tactics. 

## **Conclusion** 

In summary, the purpose of this study was to extract team tactics without excluding contextual information and to evaluate actions and possessions that employ the extracted team tactics. To accomplish this goal, we used sequential pattern mining to consider contextual information and extracted five team tactics based on pass, dribble, alternating pass-dribble, opponent-wing, and own-half. Furthermore, we accurately modelled the teams' expected behaviour in possession using the NMSTPP�360 model and validated the StatsBomb 360 data needs. Furthermore, we deployed the HPUS and related metrics to evaluate the EPL 2022/2023 teams' possession performance under each extracted tactic, which was visualised using a radar plot and mean shift clustering. 

In the future, a more in-depth analysis of possession and the sequence of events could be performed with an in-depth understanding of the game and expert insights to gain a deeper understanding of the extracted sequential patterns and team tactics. Furthermore, only the radar plot and mean shift clustering were used to visualise team performance. To utilise HPUS metrics and extracted tactics, alternative visualisation techniques and player performance evaluation metrics could be considered. Nonetheless, we anticipate that this study will demonstrate the effectiveness of contextually analysing team tactics and will inspire future research in team tactics and collective behaviour analysis. 

## **Acknowledgements** 

This work was financially supported by JST SPRING, Grant Number JPMJSP2125. The author, Calvin Yeung, would like to take this opportunity to thank the “Interdisciplinary Frontier Next-Generation Researcher Program of the Tokai Higher Education and Research System.” 

**18** 



## **References** 

�1�Palacios-Huerta, I. �2003�. Professionals play minimax. The Review of Economic Studies, 70�2�, 395�415. 

�2�Liu, S., Lever, G., Wang, Z., Merel, J., Eslami, S. M., Hennes, D., ... & Heess, N. �2021�. From motor control to team play in simulated humanoid football. arXiv preprint arXiv:2105.12196. 

�3�Yeung, C.C.K., & Fujii, K. �2023�. A Strategic Framework for Optimal Decisions in Football 1-vs-1 Shot-Taking Situations: An Integrated Approach of Machine Learning, Theory-Based Modeling, and Game Theory. arXiv preprint arXiv:2307.14732. �4�Gréhaigne, J. F., Godbout, P., & Bouthier, D. �1999�. The foundations of tactics and strategy in team sports. Journal of teaching in physical education, 18�2�, 159�174. �5�Plakias, S., Moustakidis, S., Kokkotis, C., Tsatalas, T., Papalexi, M., Plakias, D., ... & Tsaopoulos, D. �2023�. Identifying soccer teams’ styles of play: a scoping and critical review. Journal of Functional Morphology and Kinesiology, 8�2�, 39. 

�6�Decroos, T., Bransen, L., Van Haaren, J., & Davis, J. �2019, July). Actions speak louder than goals: Valuing player actions in soccer. In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining (pp. 1851�1861�. 

�7�Van Roy, M., Robberechts, P., Yang, W. C., De Raedt, L., & Davis, J. �2023�. A Markov Framework for Learning and Reasoning About Strategies in Professional Soccer. Journal of Artificial Intelligence Research, 77, 517�562. 

�8�Yeung, C.C.K., Sit, T., & Fujii, K. �2023�. Transformer-Based Neural Marked Spatio Temporal Point Process Model for Football Match Events Analysis. arXiv preprint arXiv:2302.09276. 

�9�Fukunaga, K., & Hostetler, L. �1975�. The estimation of the gradient of a density function, with applications in pattern recognition. IEEE Transactions on information theory, 21�1�, 32�40. 

�10�Pei, J., Han, J., Mortazavi-Asl, B., Wang, J., Pinto, H., Chen, Q., ... & Hsu, M. C. �2004�. Mining sequential patterns by pattern-growth: The prefixspan approach. IEEE Transactions on knowledge and data engineering, 16�11�, 1424�1440. 

�11�Xie, X., Wang, J., Liang, H., Deng, D., Cheng, S., Zhang, H., ... & Wu, Y. �2020�. PassVizor: Toward better understanding of the dynamics of soccer passes. IEEE Transactions on Visualization and Computer Graphics, 27�2�, 1322�1331. 

�12�Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. �2017�. Attention is all you need. Advances in neural information processing systems, 30. 

�13�Bekkers, J., & Dabadghao, S. �2019�. Flow motifs in soccer: What can passing behavior tell us?. Journal of Sports Analytics, 5�4�, 299�311. 

�14�Derpanis, K. G. �2005�. Mean shift clustering. Lecture Notes, 32, 1�4. �15�Fernandez-Navarro, J., Fradua, L., Zubillaga, A., Ford, P. R., & McRobert, A. P. �2016�. Attacking and defensive styles of play in soccer: analysis of Spanish and English elite teams. Journal of sports sciences, 34�24�, 2195�2204. 

**19** 



�16�Castellano, J., & Echeazarra, I. �2019�. Network-based centrality measures and physical demands in football regarding player position: Is there a connection? A preliminary study. Journal of sports sciences, 37�23�, 2631�2638. 

�17�Wang, Q., Zhu, H., Hu, W., Shen, Z., & Yao, Y. �2015, August). Discerning tactical patterns for professional soccer teams: an enhanced topic model with applications. In Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 2197�2206�. 

�18�Cintia, P., Giannotti, F., Pappalardo, L., Pedreschi, D., & Malvaldi, M. �2015, October). The harsh rule of the goals: Data-driven performance indicators for football teams. In 2015 IEEE International Conference on Data Science and Advanced Analytics �DSAA�(pp. 1�10�. IEEE. 

�19�Rein, R., & Memmert, D. �2016�. Big data and tactical analysis in elite soccer: future challenges and opportunities for sports science. SpringerPlus, 5�1�, 1�13. 

�20�Macdonald, B. �2012, March). An expected goals model for evaluating NHL teams and players. In Proceedings of the 2012 MIT Sloan Sports Analytics Conference. �21�Eggels, H., van Elk, R., & Pechenizkiy, M. �2016�. Expected goals in soccer: Explaining match results using predictive analytics. In The machine learning and data mining for sports analytics workshop �Vol. 16�. 

�22�Lucey, P., Bialkowski, A., Monfort, M., Carr, P., & Matthews, I. �2015�. quality vs quantity: Improved shot prediction in soccer using strategic features from spatiotemporal data. 

�23�Link, D., Lang, S., & Seidenschwarz, P. �2016�. Real time quantification of dangerousity in football using spatiotemporal tracking data. PloS one, 11�12�, e0168768. �24�Liu, G., Luo, Y., Schulte, O., & Kharrat, T. �2020�. Deep soccer analytics: learning an action-value function for evaluating soccer players. Data Mining and Knowledge Discovery, 34, 1531�1559. 

�25�Liu, G., & Schulte, O. �2018�. Deep reinforcement learning in ice hockey for context-aware player evaluation. arXiv preprint arXiv:1805.11088. 

�26�Spearman, W. �2018, February). Beyond expected goals. In Proceedings of the 12th MIT sloan sports analytics conference (pp. 1�17�. 

�27�Spearman, W., Basye, A., Dick, G., Hotovy, R., & Pop, P. �2017, March). Physics-based modeling of pass probabilities in soccer. In Proceeding of the 11th MIT Sloan Sports Analytics Conference. 

�28�Teranishi, M., Tsutsui, K., Takeda, K., & Fujii, K. �2022, September). Evaluation of creating scoring opportunities for teammates in soccer via trajectory prediction. In International Workshop on Machine Learning and Data Mining for Sports Analytics (pp. 53�73�. Cham: Springer Nature Switzerland. 

�29�Toda, K., Teranishi, M., Kushiro, K., & Fujii, K. �2022�. Evaluation of soccer team defense based on prediction models of ball recovery and being attacked: A pilot study. Plos one, 17�1�, e0263051. 

**20** 



�30�Umemoto, R., Tsutsui, K., & Fujii, K. �2022�. Location analysis of players in UEFA EURO 2020 and 2022 using generalized valuation of defense by estimating probabilities. arXiv preprint arXiv:2212.00021. 

�31�Simpson, I., Beal, R. J., Locke, D., & Norman, T. J. �2022, August). Seq2Event: Learning the Language of Soccer using Transformer-based Match Event Prediction. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 3898�3908�. 

�32�Kingma, D. P., & Ba, J. �2014�. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980. 

**21** 



## **Appendix** 

#### **1. Football Pitch Segmentation** 



Supplementary Figure 1�Juego de posición (position game) pitch segmentation method 

#### with the centroid of each zone 



Supplementary Figure 2�HPUS area segmentation method 

**22** 


