<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2023/2023 - Clustering Football Game Situations via Deep Representation Learning - Unknown Authors.pdf -->



# **Clustering Football Game Situations via Deep Representation Learning** 

Zitian Tang<sup>∗1</sup> , Xing Wang<sup>2</sup> , Shaoliang Zhang<sup>3</sup> 

- 1 Computer Science Department, Brown University 

- 2 Faculty of Physical Activity and Sports Sciences, Polytechnic University of Madrid 

- 3 Division of Sports Science and Physical Education, Tsinghua University 

## **1. Introduction** 

To prepare for a football game, a coaching team analyzes the strengths and weaknesses of the opponent and develops corresponding strategies. However, watching previous games and discovering the opponent’s tactical characteristics is laborious. In the past decade, sports data companies collected a large amount of event data in football games, and many performance evaluation methods [2][11] are built upon it. These methods can quantify the value of each action and usually draw heatmaps to show in which areas high action values are created. However, a team can face different situations when they hold the ball at the same location. The opponent may be performing a low-block defense or high press. And it is also possible that they are in a counter-attack, and there is an open area behind the opponent’s defensive line. Since a team is not supposed to have the same performances under different situations, it is more reasonable to tell the different situations apart when analyzing a team. 

In recent years, StatsBomb has collected tactical event data (a.k.a. StatsBomb 360 data), which includes the positions of all the visible players when an event happens. With this information provided, it becomes possible to distinguish the different situations from the events at the same location. This work aims to fill this gap. Specifically, our goal is to cluster the freeze frames in StatsBomb 360 data into various situations and conduct performance analysis based on the discovered situations. 

The original data format of the freeze frames is too complex to apply traditional clustering algorithms directly. To address this issue, we propose first compressing the frames into low-dimensional features via deep representation learning, then clustering them in the feature space to discover different game situations in each pitch area. Furthermore, we propose a novel performance evaluation metric, Situational Expected Threat (Situational xT), which replaces the positional states in the Expected Threat model [11] with our discovered game situations. By evaluating a team’s actions using Situational xT and summarizing their values according to the event situation index, our method can demonstrate in what situations they play more effectively. 

In this paper, we use our method to analyze the performances of several English Premier League teams in the 2021/22 season. We analyze their offensive and defensive styles and effectiveness, revealing in what 

> ∗   This work was completed when Zitian Tang was at Institute for Interdisciplinary Information Sciences, Tsinghua University. 

**1** 



situations and why they play well or badly. We also compare their performances between the 2021/22 and 2022/23 seasons. In particular, we investigate the offensive effectiveness changes of Arsenal in their midfield. The model used in this work is released at _<u>https://github.com/ZitianTang/FootballSituation</u>_ <u>,</u> which can be used to study team performances in other leagues. 

The rest of this paper is structured as follows: In Section 2, we review the works related to this paper. Section 3 introduces our method to cluster football game situations via deep representation learning. We describe Situational xT in Section 4. In Section 5, we show the applications of our method in football performance analysis, with the English Premier League as an example. Section 6 concludes this paper. 

## **2. Literature Review** 

### **2.1 Representation Learning in Sports Analytics** 

Representation learning trains deep neural networks on supervised or self-supervised tasks to derive lowdimensional features of high-dimensional data (image, video, audio, etc.). This feature can be utilized in downstream tasks and lead to good performance. This method has achieved great success in natural language processing and computer vision. In recent years, representation learning has been adapted to develop valuable applications in sports analytics. 

Singh uses an Auto-Encoder [4] to compress the frames in football tracking data and retrieves similar game situations [12]. The Auto-Encoder takes in an image representing the positions of all the players and the ball. It reconstructs a soft Voronoi diagram as a representation learning task. In this way, the encoder compresses a raw tracking frame into a 32-dimensional feature, and similar situations can be retrieved by computing the feature-level similarity. Moreover, by analyzing the distribution of the situation features a team has faced, Singh develops team fingerprints, which qualitatively show what situations a team encountered more. 

In basketball, Nistala and Guttag use an Auto-Encoder to learn a representation of a single player's movement trajectory [8]. The trajectory is drawn on a 2D image, and the Auto-Encoder learns to reconstruct it. They conduct K-Means clustering over the trajectory features given by the encoder. The derived clusters are semantically meaningful, e.g. screen actions above the wings and runs along the baseline. With these clusters, cluster-profiles are generated for the NBA players to show what movements they performed more. They use this tool to see the differences across players and analyze the individual changes of players over seasons. 

### **2.2 Performance Evaluation in Football Game** 

The principle of performance evaluation is to quantify the scoring chances created by a team. The most traditional way is to count the number of goals and shots, known as a _count-based approach_ . However, the shots vary in difficulty to be converted. The Expected Goal (xG) [6][10] is proposed to evaluate the shot chances. They use various machine learning methods to approximate the scoring probability with respect to the positions of the shooting player and others. 

**2** 



To evaluate all types of actions rather than only shots, _action-based approaches_ [2] and _possession-valuebased approaches_ [11][7][1] are developed. Their rationales are both to estimate the future scoring probability at each time step and then value an action by the metric difference before and after it. However, action-based approaches, such as Valuing Actions by Estimating Probabilities (VAEP) [2], utilize binary classifiers to estimate the scoring probability by considering the characteristics of the past few actions. In contrast, possession-value-based approaches consider the game dynamics in a Markov model manner. 

A well-known possession-value-based approach is Expected Threat (xT) [11]. It splits the football pitch into grids and considers the grid location of the ball as its state. In this model, the transition probability from zone to zone and the threat of each zone is estimated. However, the other players' locations also significantly affect the game dynamics. Contextual xT [7] and Expected Possession Value (EPV) [1] are proposed to address this issue. They use Convolutional Neural Networks (CNNs) to predict the likelihood of an action being taken in the given context, making the action evaluation more accurate. Nevertheless, they cannot estimate the transition probabilities between states because the states are continuous and complicated. They have to simplify the states in the future or implicitly estimate the value of a state. 

A common limitation of the works above lies in their ways of aggregating the evaluation results. It is popular to sum the evaluation metric for a team or a player according to the action locations. However, similar locations do not ensure similar situations. To comprehensively analyze the performance, it is required to categorize the situations and aggregate the evaluations case by case. 

## **3. Situation Clustering** 

This work aims to group the freeze frames in football tactical event data into different situations. A freeze frame in tactical event data records the positions of all the visible players in the broadcast video. Different frames may display different numbers of players, and we do not know the identities of these players. Therefore, it is difficult to define a distance metric between frames, which is required in clustering algorithms. To address this issue, we propose to train a deep representation learning model, which can compress the freeze frames into low-dimensional features and then cluster the frames directly in the feature space. Representation learning is a technique that trains a model with pre-training tasks, such as cloze for language models and image rotation degree estimation for vision models, and the intermediate features in the model can be used as data representations in downstream tasks. For the freeze frame data, we design three pre-training tasks: soft Voronoi diagram construction, pass success probability estimation and next action prediction, which are introduced in Section 3.1. 

An overall pipeline of our method is demonstrated in Figure 1. We first develop an Auto-Encoder [4] trained with the three pre-training tasks mentioned above. After training, we use the encoder to compress all the freeze frames into low-dimensional representations. To group the frames, we divide the pitch into 

**3** 



distinct zones and cluster the events in each zone respectively over the representation space. Finally, we examine each cluster’s properties quantitatively and qualitatively and describe the situation it represents. The details of each step are introduced in the following. 



_Figure 1 –_ **_Overall pipeline of football game situation clustering._** _Our method consists of four steps: (a) Representation learning for freeze frames with three pre-training tasks. (b) Splitting the pitch into 30 zones. (c) Clustering the events in each zone over the representation space. (d) Analyzing the property of each resulting cluster._ 

### **3.1 Representation Learning for Freeze Frames** 

In the first stage, we use a CNN-based Auto-Encoder to learn representations for freeze frames. The encoder takes in several manual features constructed from raw tactical event data and compresses them into low-dimensional features. Three decoders are developed to tackle three different tasks with the representations as inputs. After joint training, the representations given by the encoder contain the most valuable features of freeze frames, and they can be utilized in the downstream clustering process. 

- We split the pitch into a 64 × 96 grid and construct the following spatial feature maps as model input: 

1. **Player positions** – 4 maps representing the locations of the event actor, offensive team players, defensive team players, and goalkeepers. Each grid cell has a value of 1 if at least one player is in it. Otherwise, 0. 

2. **Relative positions to the event actor** – 3 maps representing the relative horizontal distance, relative vertical distance, and straight-line distance from each grid cell to the event actor. 

3. **Relative positions to the goal of the defensive team** – 3 maps representing the relative horizontal distance, relative vertical distance and straight-line distance from each grid cell to the goal of the defensive team. 

The three tasks used as representation learning tasks are the following: 

1. **Soft Voronoi diagram construction** – Soft Voronoi diagram is a spatial map indicating the difference between the two teams’ control strengths at each location. For a grid cell inside the visible area, (𝑖𝑖, 𝑗𝑗) 

**4** 



let be the distance to the nearest offensive player, be that to the nearest defensive one. The ground truth value of the cell is 𝑖𝑖,𝑗𝑗 𝑖𝑖,𝑗𝑗 𝑂𝑂 ~~𝑂~~ 2 𝐷𝐷 ~~𝐷~~ 2 32 32 . (𝑖𝑖, 𝑗𝑗) 𝑖𝑖,𝑗𝑗 𝑖𝑖,𝑗𝑗 An example is shown in Figure 1(a). We use a CNN-based decoder to construct this map from the 𝑖𝑖,𝑗𝑗 𝑉𝑉 = 𝑒𝑒<sup>−1</sup> − 𝑒𝑒<sup>−1</sup> compressed representation. Mean Square Error serves as the task objective ℒVoronoi . 

2. **Pass success probability estimation** – Pass success probability surface [3], shown in Figure 1(a), is a spatial map indicating the pass success probability from the actor’s location to each grid cell. Although the performed action in a freeze frame may not be a pass, every frame is supposed to have such a surface. To derive this, we first train a pass success probability estimation model using U-Net [9] with all the pass events, then estimate this surface for all the frames. In the Auto-Encoder, a CNN-based decoder constructs this surface from the representation. With the U-Net’s estimations as supervision, we use Binary Cross Entropy as the objective ℒPass for this task. 

3. **Next action prediction** – This task aims to measure the probability to take each type of action (pass, carry, or shot) in a given freeze frame. We first train a CNN to predict the action probability using all the pass, carry, and shot events, then estimate this probability for all freeze frames. In the AutoEncoder, an MLP predicts the action probabilities from the representation, and Cross Entropy is the objective ℒActoin for this task. 

We jointly train the encoder and the three task heads with a weighted loss ℒ= ℒVoronoi + ℒPass + 0.1ℒ𝐴 𝐴 . 𝑖𝑖𝐴𝐴 

We train the model using Adam [5] optimizer with a learning rate of 0.001 and a batch size of 512 for 200 epochs. The checkpoint with the smallest validation loss is chosen as the final model. 

### **3.2 Clustering over Representation Space** 

After representation learning, we use the encoder of the Auto-Encoder model to compress all the freeze frames into low-dimensional representations. In the second step, we conduct clustering over the representation space to discover different situations in football. Instead of directly clustering all the data points into dozens of groups, we first divide the pitch into 30 zones as Figure 1(b) shows and group the freeze frames based on which zone the event actor is in. Then, we conduct clustering over each zone’s data points respectively. In this way, we can better interpret the property of each resulting cluster. 

To cluster the freeze frames in each zone, we run K-Means with Euclidean distance over the representation space. To understand each resulting cluster, we qualitatively and quantitatively analyze the properties of each cluster. For example, we draw the pass end location heatmap, relative player position to the event actor heatmap and other maps, and compute the average defensive distance, average number of players in front, team centroids’ relative location, etc. We can easily figure out the differences between clusters with the help of these attributes. To determine the number of clusters, we try different k (from 2 to 10) and manually find the one with the best interpretability for each zone. Each resulting cluster is regarded as a situation in football games. 

**5** 



In this work, we focus on the tactics in open play. We use the on-ball open-play events in the English Premier League 2021/22 season to develop our method, including the representation learning and clustering stages. In total, our method splits all the freeze frames in open play into 95 distinct situations, with two to four situations in each zone. We write a textual description for each situation according to the calculated attributes. The results are shown in Figure 2. Some essential attributes that help us describe the situations in each zone are listed in the Appendix. However, a crucial limitation of our grouping method is that a sample may not necessarily conform to the description of the situation it falls into. Any quantitative analysis derived from our results is only an approximation rather than accurate counting. 

_Figure 2 –_ **_Situations discovered by our method._** _There are 95 situations in total, and we manually give a textual description for each one. The Situation xT values computed in Section 4 are also listed._ 

|**Zone**|**Situation**|**Description**|**xT (%)**|
|---|---|---|---|
|1|1|Defensive distance large.|0.09|
|1|2|Defensive distance small.|0.08|
|2|1|Defensive distance large.|0.12|
|2|2|Defensive distance small.|0.13|
|3|1|Defensive distance large.|0.09|
|3|2|Defensive distance small.|0.09|
|4|1|Opponent returned to defense. Defensive distance large.|0.20|
|**4**|2|Opponent returned to defense. Defensive distance small.|0.14|
|**4**|3|Opponent not returned to defense.|0.15|
|**5**|1|Opponent returned to defense. Defensive distance large.|025|
|**5**|2|Opponent returned to defense. Defensive distance small.|0.19|
|**5**|3|Opponent not returned to defense.|0.18|
|**6**|1|Opponent returned to defense. Defensive distance large.|0.26|
|**6**|2|Opponent returned to defense. Defensive distance small.|0.20|
|**6**|3|Opponent not returned to defense.|0.19|
|**7**|1|Opponent returned to defense. Defensive distance large.|0.25|
|**7**|2|Opponent returned to defense. Defensive distance small.|0.19|
|**7**|3|Opponent not returned to defense.|0.17|



**6** 



|**8**|1|Opponent returned to defense. Defensive distance large.|0.19|
|---|---|---|---|
|**8**|2|Opponent returned to defense. Defensive distance small.|0.15|
|**8**|3|Opponent not returned to defense.|0.14|
|**9**|1|Opponent returned to defense. Defensive distance large.|0.35|
|**9**|2|Opponent returned to defense. Defensive distance small.|0.29|
|**9**|3|Opponent not returned to defense.|0.24|
|**10**|1|In front of opponent's defensive line. Defensive distance large.|0.45|
|**10**|2|In front of opponent's defensive line. Defensive distance small.|0.39|
|**10**|3|Between opponent's defensive lines.|0.30|
|**11**|1|In front of opponent's defensive line. Defensive distance large.|0.50|
|**11**|2|In front of opponent's defensive line. Defensive distance small.|0.42|
|**11**|3|Between opponent's defensive lines.|0.34|
|**12**|1|In front of opponent's defensive line. Defensive distance large.|0.46|
|**12**|2|In front of opponent's defensive line. Defensive distance small.|0.41|
|**12**|3|Between opponent's defensive lines.|0.28|
|**13**|1|Opponent returned to defense. Defensive distance large.|0.36|
|**13**|2|Opponent returned to defense. Defensive distance small.|0.30|
|**13**|3|Opponent not returned to defense.|0.23|
|**14**|1|Defensive distance large. Many teammates in front.|0.66|
|**14**|2|Defensive distance large. Few teammates in front.|0.55|
|**14**|3|Defensive distance small. Many teammates in front.|0.66|
|**14**|4|Defensive distance small. Few teammates in front.|0.43|
|**15**|1|In front of opponent's defensive line. Defensive distance large.|0.80|
|**15**|2|In front of opponent's defensive line. Defensive distance small.|0.74|
|**15**|3|Between opponent's defensive lines.|0.55|
|**16**|1|In front of opponent's defensive line. Defensive distance large.|0.87|



**7** 



|**16**|2|In front of opponent's defensive line. Defensive distance small.|0.78|
|---|---|---|---|
|**16**|3|Between opponent's defensive lines.|0.61|
|**17**|1|In front of opponent's defensive line. Defensive distance large.|0.87|
|**17**|2|In front of opponent's defensive line. Defensive distance small.|0.76|
|**17**|3|Between opponent's defensive lines.|0.56|
|**18**|1|Defensive distance large. Many teammates in front.|0.70|
|**18**|2|Defensive distance large. Few teammates in front.|0.62|
|**18**|3|Defensive distance small. Many teammates in front.|0.62|
|**18**|4|Defensive distance small. Few teammates in front.|0.44|
|**19**|1|Defensive distance large. Many teammates in penalty area.|1.11|
|**19**|2|Defensive distance large. Few teammates in penalty area.|0.99|
|**19**|3|Defensive distance small. Many teammates in penalty area.|1.09|
|**19**|4|Defensive distance small. Few teammates in penalty area.|0.81|
|**20**|1|Opponent's defensive line retreated to penalty area. Defensive distance large.|1.72|
|**20**|2|Opponent's defensive line retreated to penalty area. Defensive distance small.|1.96|
|**20**|3|Opponent's defensive line press outside penalty area. Many players in front.|1.37|
|**20**|4|Opponent's defensive line press outside penalty area. Few players in front.|1.16|
|**21**|1|Opponent's defensive line retreated to penalty area. Defensive distance large.|2.40|
|**21**|2|Opponent's defensive line retreated to penalty area. Defensive distance small.|3.56|
|**21**|3|Opponent's defensive line press outside penalty area. Many players in front.|1.59|
|**21**|4|Opponent's defensive line press outside penalty area. Few players in front.|1.27|
|**22**|1|Opponent's defensive line retreated to penalty area. Defensive distance large.|1.95|
|**22**|2|Opponent's defensive line retreated to penalty area. Defensive distance small.|2.17|
|**22**|3|Opponent's defensive line press outside penalty area. Many players in front.|1.45|
|**22**|4|Opponent's defensive line press outside penalty area. Few players in front.|1.16|
|**23**|1|Defensive distance large. Many teammates in penalty area.|1.33|



**8** 



|**23**|2|Defensive distance large. Few teammates in penalty area.|0.91|
|---|---|---|---|
|**23**|3|Defensive distance small. Many teammates in penalty area.|1.49|
|**23**|4|Defensive distance small. Few teammates in penalty area.|1.04|
|**24**|1|Defensive distance large.|1.24|
|**24**|2|Defensive distance small. Many teammates in penalty area.|1.43|
|**24**|3|Defensive distance small. Few teammates in penalty area.|0.99|
|**25**|1|Defensive distance large.|1.41|
|**25**|2|Defensive distance small. Many teammates in penalty area.|1.38|
|**25**|3|Defensive distance small. Few teammates in penalty area.|1.15|
|**26**|1|Near the goal area line. Many players in the middle.|3.60|
|**26**|2|Near the goal area line. Few players in the middle.|3.42|
|**26**|3|Near the goal line.|2.60|
|**27**|1|Almost inside the goal area.|17.18|
|**27**|2|Near the penalty area line.|8.90|
|**27**|3|Near the goal area line. Formation skewed to the left.|10.42|
|**27**|4|Near the goal area line. Formation skewed to the right.|10.78|
|**28**|1|Near the goal area line. Many players in the middle.|4.25|
|**28**|2|Near the goal area line. Few players in the middle.|3.55|
|**28**|3|Near the goal line.|2.62|
|**29**|1|Defensive distance large.|1.73|
|**29**|2|Defensive distance small. Many teammates in penalty area.|1.68|
|**29**|3|Defensive distance small. Few teammates in penalty area.|1.29|
|**30**|1|Defensive distance large.|1.79|
|**30**|2|Defensive distance small. Many teammates in penalty area.|1.18|
|**30**|3|Defensive distance small. Few teammates in penalty area.|1.03|



**9** 



## **4. Situational Expected Threat** 

Expected Threat (xT) [11] measures the goal probability in the current possession given the ball holder’s location. This method is based on the Markov model. It splits the pitch into dozens of grids and considers each grid a state in the model. By estimating the transition probability from historical data and solving the model, we can compute the goal probability in each state. 



_Figure 3 –_ **_Markov model of Situational xT._** _The on-ball player can choose to pass or carry to a target zone, or he/she can choose to shoot. If the action is a pass or carry, the model randomly transitions to a situation in the target zone or a failed state._ 

<mark>Once our method discovers various situations in football games, we can regard each situation as a Markov model state and develop Situational Expected Threat (Situational xT). This can measure the goal probabilities under different situations even at the same location, which leads to more accurate dynamics for football. In this Markov model, as Figure 3 demonstrates, the action space of the on-ball player is a shot or a pass/carry to any zone. Once the player chooses to pass or carry to a zone, the state randomly transitions to a situation in the target zone or to a state representing a failed action. The transition probability depends on the current situation, target situation, and action type.</mark> 



<mark>We can estimate these parameters from the historical data and derive the xT values for all the situations through solving the linear system formulated by Equation (4-1). The resulting xT values are listed in F</mark> igure 2 <mark>. We observe that different situations located in the same zone may have different xT values. For instance, in the midfield zones, the xT value is larger in situations with large defensive distance than in those with small distance. This is because the players tend to pass or carry the ball forward when the opponents are far away from them, while they prefer moving the ball backward under pressure.</mark> 

**10** 



<mark>Once we get the xT under each situation, an action can be valued as the Situational xT difference before and after the action. We denote this value by x</mark> Tadd . Specifically, for a pass or carry that is taken under situation and results in situation , its xTadd value is 𝑥𝑥 𝑦𝑦 



To analyze a team’s performance under a given situation, we can sum up the xTadd values of all the actions taken by this team under this situation. This value evaluates their offensive performance. Besides, we can sum up the xTadd values of their conceded actions when their opponents are under this situation. This measures the defensive performance when encountering the given situation in defense. 

## **5. Model Applications** 

Many previous works in football analysis only summarize a team’s performance according to the event location, demonstrating where they play better on the pitch. With the various situations we have discovered, the team performance analysis in each zone can be further detailed. By summing up the action xTadd values created and conceded in a situation, we can evaluate the offensive and defensive strengths of the team in the situation. As the examples shown later in this section illustrate, one team may play effectively in one situation but badly in another in the same zone. It is our analysis method that quantitatively reveals this phenomenon. 

In the following, we analyze the performances of ten selected teams from the English Premier League to showcase how our method works. In this work, we focus on open-play performance. We utilize the openplay actions in games between the ten teams (90 games in total) in the 2021/22 season to build up our model, including representation learning, clustering, and Situational xT. The developed model is available at _<u>https://github.com/ZitianTang/FootballSituation</u>_ <u>. Using this model, Section 5.1 analyzes the offensive</u> performances in the 2021/22 season, while Section 5.2 analyzes the defensive performances. Furthermore, the developed model can also be applied in other seasons and leagues. As an example, Section 5.3 evaluates the ten teams’ performances in the 2022/23 season and compares them with the 2021/22 ones. In each part of the following, we only analyze the performances of a few teams in a few situations in detail as case studies. One can do other cases using our tool in the same way. 

### **5.1 Offensive Performance Analysis** 

We propose two metrics to analyze a team’s offensive style and strength: 

**11** 



1. **Created occurrence** – For a given team and situation, the average number of times per game that the team encountered the situation in attack. 

2. **Created** 𝐱 𝐚 – For a given team and situation, the average total xTadd per game created by the team in attack. 𝐚𝐚 



_Figure 4 –_ **_Created occurrence and xTadd in Zone 14~18 during the Premier League 2021/22 season._** _In (a) created occurrence heatmap, deeper red indicates the team encountered the situation for more times. In (b) created xTadd heatmap, deeper red indicates better offensive performance while deeper blue indicates worse performance._ 

Figure <mark>4 shows the created occurrence and</mark> xTadd of the ten Premier League teams in several midfield zones behind the half-way line (Zone 14~18 in Figure 1(b)) during the 2021/22 season. From the created occurrence, we can discover that the occurrence proportions of the different situations in a zone vary from team to team. This reveals their different offensive strategies. For instance, in Zone 15, 16, and 17, Manchester City, Chelsea, and Liverpool met the first two situations (in front of defensive line with large/small defensive distance) much more than the third one, which indicates that they are always in front of the opponent’s defensive line in attack. In contrast, Leeds United, Brentford, and Everton create more occurrences in the third situation (between defensive lines), showing that it is more usual for them to possess the ball between the opponent’s defensive lines in these zones. 

A team may have different offensive strengths in different situations of a zone. We can see this from the heatmap of created xTadd shown in Figure 4(b). In Zone 16, Manchester City, the champion in the 2021/22 season, created the most xTadd in the second situation but negative value in the first one. We investigate the reason by examining what and whose actions contribute to the created value. For the 0.0040 total xTadd value made in Situation 16-2, Manchester City’s passes contribute 0.0033. Their line-breaking passes beyond the defensive line are an effective way to attack. Among these, an action value of 0.0027 is created by Kevin De Bruyne, one of the best midfielders nowadays. However, in Situation 16-1, although their passes contribute 0.0030 xTadd , their carries gain a total value of -0.0044, indicating their bad carry choices and accomplishments when the defensive distance is large. In comparison, Tottenham Hotspur is completely the opposite. They created the most action value in Situation 16-1 but the least in 16-2 among all the ten teams. In Situation 16-1, their passes contribute 0.0038 value while carries contribute 0.0037. The significant pass value is mainly made by a line-breaking pass beyond the last defensive line, and the carry value is created by Harry Kane, Steven Bergwijn, and Heung-Min Son through carrying the ball toward the opponent’s goal. In Situation 16-2, where the defensive distance is short, however, their pass 

**12** 



and carry values are both negative. Moreover, Liverpool’s best situation in Zone 16 is the third one, where they hold the ball between defensive lines. This is because Sadio Mane, Curtis Jones, and Thiago made great carries with their outstanding dribbling, creating 0.0067 xTadd value. This also tells us that a team may perform better in situations which they encounter fewer times. 



_Figure 5 –_ **_Created occurrence and xTadd in corner zones during the Premier League 2021/22 season._** 

<mark>As another example, F</mark> igure <mark>5 shows the created occurrence and</mark> xTadd in corner zones (Zone 24, 25, 29, and 30 in Figure 1(b)) of the ten teams. In Zone 29, Manchester City create the most significant total action values among the ten teams in both Situation 29-1, where the defensive distance is large, and Situation 29-3, where the defensive distance is small and few teammates are in the penalty area. In the first situation, Ilkay Gundogan, Rodrigo Hernandez, and Riyad Mahrez’s crosses into the center of the penalty area contribute 0.0151 xTadd out of the total 0.0130. Bernardo Silva’s inside cuts also create a total value of 0.0060. As for the 0.0057 value in Situation 29-3, it is mainly made by a cross from Fernandinho with a value of 0.0053. However, in the second situation, Manchester City’s total pass and carry values are both negative. Tottenham is again the opposite as they create 0.0166 value in Situation 29-2, which is the most among the teams. This is mainly made by the passes of Dejan Kulusevski, Emerson Aparecido, and HeungMin Son. 

### **5.2 Defensive Performance Analysis** 

We propose two metrics to analyze a team’s defensive style and strength: 

1. **Conceded occurrence** – For a given team and situation, the average number of times per game that 

- the team encountered the situation in defense. 

- 2. **Conceded** 𝐱 𝐚 – For a given team and situation, when the team is in defense, the average total xTadd per game created by the opponents. 𝐚𝐚 

Figure 6 <mark>shows the conceded occurrence and x</mark> Tadd of the ten teams in midfield zones before the halfway line (Zone 9~13 in Figure 1(b)) during the 2021/22 season. From the conceded occurrence heatmap, we find that different teams tend to lead the game into different situations when defending. For Manchester City and Liverpool, when their opponents possess the ball in Zone 10, 11, and 12, they are more likely to be in front of the defensive line with a small defensive distance (the second situation of each zone) or between the defensive lines (the third situation). This illustrates their high-pressing defensive strategy. In comparison, Tottenham, Manchester United, and Everton prefer leading the game 

**13** 



into the first situation of each zone, where their opponents are in front of the defensive line with a large defensive distance. This aligns with their low-block defensive strategy. 



_Figure 6 –_ **_Conceded occurrence and xTadd in Zone 9~13 during Premier League 2021/22 season._** _In (a) conceded occurrence heatmap, deeper red indicates the team encountered the situation for more times. In (b) conceded xTadd heatmap, deeper red indicates worse defensive performance while deeper blue indicates better performance._ 

The conceded xTadd heatmap demonstrates how much action value a team’s opponents create in each situation, reflecting the team’s defensive strength. The league champion, Manchester City, performed very effectively in defense. Their opponents could not almost create a positive total xTadd in these midfield zones. Besides, we can discover that some teams played poorly in defense in some situations. For example, the league’s fifth-place team, Arsenal, concede 0.0048 xTadd in Situation 11-2 – 0.0034 from pass and 0.0014 from carry. Examining their opponents’ actions with large action values, we find that Arsenal conceded many long passes beyond their last defensive line and some long carries toward their goal. This reveals a defensive weakness of Arsenal. Furthermore, Manchester United concede 0.0029 xTadd in Situation 11-3, where the opponents hold the ball between their defensive lines. The opponents accomplished many long carries into the final third from this situation, creating a total value of 0.0035, indicating they have trouble preventing their opponents from dribbling in counter-attacks. 

### **5.3 Performance Comparison across Seasons** 

Although our model parameters are estimated from historical data of the Premier League 2021/22 season, it does not mean that it can only be used to analyze team performance in this season. By inferring the representation of each freeze frame, figuring out the situation it belongs to, and evaluating an action by the Situational xT model, we can use the model to analyze other seasons and leagues. As an example, we do this for the Premier League 2022/23 season and compare the results to those of the 2021/22 season. 

Figure 7 is the ten teams’ created <mark>occurrence and</mark> xTadd in midfield Zone 9~13 in the 2021/22 and 2022/23 seasons. Here, we focus on the performance of Arsenal, who finished fifth in 2021/22 but clinched the runner-up position in 2022/23. Comparing the two heatmaps of created occurrence, we find that Arsenal’s offensive style in this area did not change too much. In both seasons, they almost encountered the second situation of each zone the most and the third situation the least. 

**14** 





_Figure 7 –_ **_Created occurrence and xTadd in Zone 9~13 during the Premier League 2021/22 and 2022/23 seasons._** 

However, several changes in their offensive effectiveness can be observed in the created xTadd heatmaps. In Situation 10-2, where they possess the ball in front of their opponents with a small defensive distance, their total action value increases from -0.0009 to 0.0039. Investigating the reason, we find that their passes in 2022/23 create a 0.0043 value. Particularly, Gabriel Magalhaes and Granit Xhaka accomplished many long passes down the left flank, contributing values of 0.0021 and 0.0011, respectively. Besides, we find that Gabriel Magalhaes also made such passes in 2021/22, but his total xTadd of passes created in that season is only 0.0007. This verifies that long passes down the flank became an effective way to attack in the 2022/23 season for Arsenal. In Situation 13-3, where their opponent players have not returned to defense, Arsenal’s created value increases from -0.0007 to 0.0057. In the 2022/23 season, their carries from this situation contribute a total value of 0.0053. Bukayo Saka and Ben White accomplished many long carries down the right flank, creating 0.0020 and 0.0014 xTadd , respectively. In comparison, their carries in 2021/22 only make values close to 0. Their improvements in dribbling brought more efficient attacking to Arsenal. 

## **6. Conclusion** 

This work groups freeze frames in tactical event data, especially StatsBomb 360 data, into different football game situations. With the grouping result, we can study a team’s performance in different 

**15** 



situations in each area of the pitch. This method is more detailed than previous location-based performance summaries, revealing a team’s different offensive and defensive effectiveness in different contexts. 

To group the freeze frames, we first train an Auto-Encoder with three representation learning tasks: soft Voronoi diagram construction, pass success probability estimation, and next action prediction. The trained model can compress each frame into a low-dimensional representation vector. We cluster the event frames in each pitch zone over the representation space to group them. We discover 95 football game situations in total and describe each of them by examining a few statistics. Moreover, we develop Situational xT by modeling football with the Markov model and regarding each situation as a state. This novel metric can take the game situation into account when evaluating an on-ball action. 

We use our model to analyze the performance of several teams in the English Premier League 2021/22. Moreover, we also investigate their performance changes from the 2021/22 to the 2022/23 season. Our method can determine which situations a team encountered more and in which ones their offensive or defensive performances are better, indicating their tactical style and strength. It is observed that different teams may encounter different situations more, and a team may play effectively in one situation but poorly in another even in the same zone. Furthermore, the situation where a team performed well is not necessarily the one they encountered much. Many strengths and weaknesses of the Premier League teams are discovered by our analysis. 

Finally, our model is publicly released. The football analytics community can use it to analyze the performance of any team in any league they are interested in. 

## **References** 

[1] Cervone, D., Fernández, J., & Bornn, L. (2019) Decomposing the immeasurable sport: A deep learning expe cted possession value framework for soccer. _MIT Sloan Sports Analytics Conference._ 

[2] Decroos, T., Bransen, L., Haaren, J.V., & Davis, J. (2020). VAEP: An Objective Approach to Valuing On-the-B all Actions in Soccer (Extended Abstract). _International Joint Conference on Artificial Intelligence._ 

[3] Fern `á` ndez, J., & Bornn, L. (2020). SoccerMap: A Deep Learning Architecture for Visually-Interpretable Anal ysis in Soccer. _ECML/PKDD_ . 

[4]  Hinton, G.E., & Salakhutdinov, R. (2006). Reducing the Dimensionality of Data with Neural Networks. _Scien ce, 313_ , 504 - 507. 

[5] Kingma, D.P., & Ba, J. (2014). Adam: A Method for Stochastic Optimization. _CoRR, abs/1412.6980_ . 

[6] Lucey, P., Bialkowski, A., Monfort, M., Carr, P., & Matthews, I. (2015). "Quality vs Quantity": Improved Sho t Prediction in Soccer using Strategic Features from Spatiotemporal Data. 

[7] Matthews, T., Norman, T., Ramchurn, G., Everett, G., & Beal, R. (2022) Contextual expected threat using sp atial event data. _StatsBomb Conference._ 

[8] Nistala, A., & Guttag, J.V. (2019). Using Deep Learning to Understand Patterns of Player Movement in the NBA. _MIT Sloan Sports Analytics Conference._ 

[9] Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional Networks for Biomedical Image Segm entation. _ArXiv, abs/1505.04597._ 

**16** 



[10] Ruiz, H., Power, P., Wei, X., & Lucey, P. (2017). "The Leicester City Fairytale?": Utilizing New Soccer Analyt ics Tools to Compare Performance in the 15/16 & 16/17 EPL Seasons. _Proceedings of the 23rd ACM SIGKDD In ternational Conference on Knowledge Discovery and Data Mining._ 

[11] Singh, K. (2019). Introducing expected threat. Retrieved May 9, 2023, from Karun’s Blog Website: <u>https:// karun.in/blog/expected-threat.html.</u> 

[12] Singh, K. (2020). Learning to watch football: Self-supervised representations for tracking data. _Opta Pro F orum._ 

**17** 



## **Appendix** 

In Figure 8~16, we list the important statistical attributes of the discovered situations that help us describe them. The values colored red and blue are those distinguishing one situation from others within the same zone. The involved attributes are 

**1. Defensive distance** – The distance from the on-ball player to the closest opponents. 

**2. Team centroid depth** – The _x_ -coordinate of the centroid of the offensive team players. The _x_ -axis is along the field length, ranging from 0 (the offensive team’s goal) to 120 (the defensive team’s goal). 

**3. Team centroid** **_y_ -coordinate** – The _y_ -coordinate of the centroid of the offensive team players. The _y_ - axis is along the field width, ranging from 0 (left sideline) to 80 (right sideline). 

**4. # Visible opponents** – Number of visible opponents in the event freeze frame. 

**5. # Opponents in front** – Number of opponents in front of the on-ball player, i.e., opponents with larger _x_ -coordinates than the on-ball player. 

**6. # Opponents in penalty area** – Number of opponents in the penalty area. 

**7. # Visible teammates** – Number of visible teammates in the event freeze frame. 

**8. # Teammates in front** – Number of teammates in front of the on-ball player. 

**9. # Teammates in penalty area** – Number of teammates in the penalty area. 

**10. # Teammates in goal area** – Number of teammates in the goal area. 

**11. # Teammates in center space** – Number of teammates with _y_ -coordinates in [30, 50] (width of the goal area). 

_Figure 8 –_ **_Statistical attributes of situations in Zone 1~3._** 

|**Zone-Situation ID**|**Defensive distance**|
|---|---|
|**1 – 1**|8.43|
|**1 – 2**|3.43|
|**2 – 1**|12.94|
|**2 – 2**|7.43|
|**3 – 1**|8.67|
|**3 – 2**|3.63|



**18** 



_Figure 9 –_ **_Statistical attributes of situations in Zone 4~9 and 13._** 

|**Zone-Situation ID**|**Defensive distance**|**# Visible opponents**|**# Opponents in front**|
|---|---|---|---|
|**4 – 1**|9.60|5.85|5.17|
|**4 – 2**|3.85|5.82|4.22|
|**4 – 3**|9.42|5.25|3.29|
|**5 – 1**|13.60|5.20|4.95|
|**5 – 2**|5.30|5.58|4.64|
|**5 – 3**|8.55|5.52|3.52|
|**6 – 1**|15.92|4.72|4.61|
|**6 – 2**|7.27|5.08|4.64|
|**6 – 3**|7.14|5.67|3.41|
|**7 – 1**|13.83|5.14|4.88|
|**7 – 2**|5.78|5.21|4.65|
|**7 – 3**|7.39|5.68|3.65|
|**8 – 1**|9.45|5.90|5.25|
|**8 – 2**|3.58|5.85|4.36|
|**8 – 3**|7.82|5.43|3.10|
|**9 – 1**|10.83|7.11|6.20|
|**9 – 2**|4.26|7.15|5.59|
|**9 – 3**|5.86|6.81|3.50|
|**13 – 1**|10.03|6.96|6.08|
|**13 – 2**|4.11|7.25|5.89|
|**13 – 3**|5.36|6.79|3.49|



**19** 



_Figure 10 –_ **_Statistical attributes of situations in Zone 10~12 and 15~17._** 

|**Zone-Situation ID**|**Defensive distance**|**# Visible opponents**|**# Opponents in front**|
|---|---|---|---|
|**10 – 1**|11.92|6.82|6.41|
|**10 – 2**|5.63|7.13|6.37|
|**10 – 3**|4.84|6.78|3.68|
|**11 – 1**|12.35|6.83|6.60|
|**11 – 2**|6.09|7.11|6.56|
|**11 – 3**|5.00|6.76|3.83|
|**12 – 1**|11.65|6.69|6.30|
|**12 – 2**|5.83|7.10|6.48|
|**12 – 3**|4.46|6.87|3.64|
|**15 – 1**|10.36|8.50|7.87|
|**15 – 2**|4.82|8.77|7.85|
|**15 – 3**|4.39|8.06|4.81|
|**16 – 1**|10.70|8.31|7.90|
|**16 – 2**|4.65|8.55|7.73|
|**16 – 3**|4.43|8.07|4.80|
|**17 – 1**|9.67|8.51|7.88|
|**17 – 2**|4.69|8.74|7.94|
|**17 – 3**|4.29|8.08|4.88|



**20** 



_Figure 11 –_ **_Statistical attributes of situations in Zone 14 and 18._** 

|**Zone-Situation ID**|**Defensive distance**|**# Visible teammates**|**# Teammates in front**|
|---|---|---|---|
|**14 – 1**|9.70|7.19|4.71|
|**14 – 2**|8.44|7.05|2.42|
|**14 – 3**|4.29|7.00|4.13|
|**14 – 4**|4.14|7.09|2.89|
|**18 – 1**|9.18|7.19|4.87|
|**18 – 2**|9.05|7.24|2.94|
|**18 – 3**|4.13|7.02|4.11|
|**18 – 4**|4.04|7.02|2.45|



_Figure 12 –_ **_Statistical attributes of situations in Zone 19 and 23._** 

|**Zone-Situation ID**|**Defensive distance**|**# Teammates in penalty area**|
|---|---|---|
|**19 – 1**|7.10|1.11|
|**19 – 2**|8.14|0.06|
|**19 – 3**|3.43|0.96|
|**19 – 4**|4.40|0.11|
|**23 – 1**|7.92|0.87|
|**23 – 2**|5.68|0.04|
|**23 – 3**|4.10|1.61|
|**23 – 4**|3.95|0.28|



**21** 



_Figure 13 –_ **_Statistical attributes of situations in Zone 20~22._** 

|**Zone-Situation ID**|**Defensive distance**|**# Opponent in penalty area**|**# Teammates in front**|**# Opponents in front**|
|---|---|---|---|---|
|**20 – 1**|7.24|3.00|3.74|7.16|
|**20 – 2**|3.41|4.60|3.46|7.34|
|**20 – 3**|3.36|1.84|4.17|8.01|
|**20 – 4**|3.81|0.43|2.39|5.05|
|**21 – 1**|6.15|2.85|4.04|7.31|
|**21 – 2**|3.04|5.02|3.64|7.31|
|**21 – 3**|3.21|1.64|4.10|7.76|
|**21 – 4**|3.62|0.28|1.97|4.57|
|**22 – 1**|6.72|3.21|3.91|7.31|
|**22 – 2**|3.40|5.12|3.69|7.58|
|**22 – 3**|3.53|1.84|4.18|7.95|
|**22 – 4**|3.59|0.41|2.13|4.67|



**22** 



_Figure 14 –_ **_Statistical attributes of situations in Zone 24, 25, 29, and 30._** 

|**Zone-Situation ID**|**Defensive distance**|**# Teammates in penalty area**|
|---|---|---|
|**24 – 1**|6.78|1.76|
|**24 – 2**|3.64|2.12|
|**24 – 3**|3.04|1.68|
|**25 – 1**|6.34|1.90|
|**25 – 2**|3.34|3.08|
|**25 – 3**|3.06|1.80|
|**29 – 1**|6.46|2.16|
|**29 – 2**|3.36|2.64|
|**29 – 3**|4.60|1.48|
|**30 – 1**|4.35|3.11|
|**30 – 2**|3.42|2.03|
|**30 – 3**|3.50|1.57|



_Figure 15 –_ **_Statistical attributes of situations in Zone 26 and 28._** 

|**Zone-Situation ID**|**# Teammates in center space**|**# Teammates in goal area**|**Team centroid depth**|
|---|---|---|---|
|**26 – 1**|3.04|0.11|103.64|
|**26 – 2**|2.41|0.05|100.81|
|**26 – 3**|2.80|0.30|106.78|
|**28 – 1**|3.02|0.14|104.69|
|**28 – 2**|2.38|0.05|102.42|
|**28 – 3**|2.76|0.33|106.95|



**23** 



_Figure 16 –_ **_Statistical attributes of situations in Zone 27._** 

|**Zone-Situation ID**|**# Teammates in goal area**|**Team centroid depth**|**Team centroid****_y_-coordinate**|
|---|---|---|---|
|**27 – 1**|1.43|109.15|39.26|
|**27 – 2**|0.04|100.32|39.00|
|**27 – 3**|0.18|104.50|37.39|
|**27 – 4**|0.19|104.31|45.60|



**24** 


