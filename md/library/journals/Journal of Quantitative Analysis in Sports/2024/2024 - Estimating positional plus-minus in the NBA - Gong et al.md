<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2024/2024 - Estimating positional plus-minus in the NBA - Gong et al.pdf -->

J. Quant. Anal. Sports 2024; 20(3): 193–217 

### **Research Article** 

Hua Gong* and Su Chen 

# **Estimating positional plus-minus in the NBA** 

https://doi.org/10.1515/jqas-2022-0120 Received December 25, 2022; accepted April 3, 2024; published online April 25, 2024 

**Abstract:** Plus-minus is a widely used performance metric in sports. Players with high plus-minus ratings are often considered more efficient than others. While numerous plus-minus models have emerged since the introduction of adjusted plus-minus in 2004, most of these metrics focus on evaluating player performance at the individual level. In the present study, we follow the plus-minus framework and adopt a hierarchical Bayesian linear model to estimate plus-minus at the position level in the NBA from 2015–16 to 2021–22. Results show that players with versatile offensive skills and big players who defend the paint area are the most valuable offensive and defensive contributors respectively. We also find that the gaps in offensive plus-minus between offensive position groups have decreased over time. Overall, our analysis offers valuable information regarding average positional values in the NBA, allowing more objective player comparisons within position groups. We also show improved prediction accuracy in player plus-minus when factoring in player positions. 

**Keywords:** basketball; Bayesian analysis; player positions; player evaluation 

## **1 Introduction** 

How to objectively evaluate player performance is a core question in the field of sports analytics. So far, scholars have proposed a variety of metrics to study player and team performance (Baghal 2012; Franks et al. 2015). Among these, the plus-minus rating is perhaps the most popular one (Engelmann 2011; Fellingham 2022; Hvattum 2019; Macdonald 2012; Rosenbaum 2004; Sill 2010; Winston 2012). In general, plus-minus intends to measure how players contribute to team offense and defense while they are on the 

***Corresponding author: Hua Gong** , Department of Sport Management, Rice University, Houston, TX, USA, E-mail: hg37@rice.edu **Su Chen** , Department of Statistics, Rice University, Houston, TX, USA 

court (Grassetti et al. 2021; Sabin 2021). If players are effective in helping teams win, their plus-minus should be high. Due to the nature of sport competition, the plus-minus metric is often divided into two parts, offensive plus-minus and defensive plus-minus. Offensive plus-minus measures players’ contributions to team offense, while defensive plusminus quantifies players’ contributions to team defense (Macdonald 2011). 

Prior studies of plus-minus predominately focus on estimating plus-minus for individual players (Deshpande and Jensen 2016). For example, Plus-minus metrics such as regularized adjusted plus-minus (RAPM) (Engelmann 2011; Sill 2010), adjusted plus-minus (Rosenbaum 2004), ESPN’s real plus-minus (Ilardi and Engelmann 2014), and estimated plus-minus (Snarr 2022), have developed over the past decade to measure player efficiency. In this study, we explore NBA player plus-minus ratings at the position level by introducing a hierarchical structure to previous plusminus models (Sabin 2021; Thomas et al. 2013; Yurko et al. 2019). 

Understanding positional values is pivotal to NBA teams in trades and free agency as these values can serve as average group ratings in player evaluation (Whitehead 2019). For example, NBA teams may compare player plusminus to positional plus-minus in order to more accurately assess player efficiency. Studying positional values over several seasons also allows teams to analyze the overall trend of player efficiency in different player positions. For example, certain position groups may improve their efficiency over time, whereas others may worsen. 

Position-level analysis in basketball frequently faces the challenge of establishing clear definitions of player roles (Beckler et al. 2013; Page et al. 2013). Traditionally, a basketball game employs five player positions: center, power forward, small forward, shooting guard, and point guard (Anıl Duman et al. 2021; McBasketball 2017). Yet, as the game of basketball continues to evolve, the definitions of player positions become less clear, as players with the same traditional position now can play vastly different roles on the court (Whitehead 2019). For example, some point guards may prioritize orchestrating the offense, whereas others may focus on scoring. To better evaluate positional plusminus, this study redefines eight offensive and three defensive positions. This is achieved through the utilization of 

> **194 —** H. Gong and S. Chen: Positional plus-minus 

the Fuzzy K-means algorithm, coupled with play type and official player position data from the NBA (Mallepalle et al. 2020). 

Overall, our study employs a hierarchical Bayesian linear model to estimate positional offensive and defensive plus-minus in the NBA from 2015–16 to 2021–22 based on redefined player positions. Then, we compare estimated plus-minus ratings across positions and seasons to determine which positions yield the highest offensive and defensive values on average. 

In so doing, our study offers several contributions. First, we present a novel perspective on the values of positions in basketball. Instead of clustering players based on traditional positions, we rely on play type data to inform players’ offensive roles on the court (Whitehead 2019). Then, the plus-minus framework with a hierarchal linear model is employed to derive positional values. This modeling structure takes the performance of teammates and opponents into account while maintaining the flexibility of constructing group level parameters (Sabin 2021). Second, we adopt a Bayesian approach to estimate positional plus-minus. Bayesian analysis allows us to quantify the uncertainty of group parameters so inference can be done easily compared to frequentist methods (Jensen et al. 2009; Santos-Fernandez et al. 2019; Thomas et al. 2013). Lastly, we improve on previous player plus-minus ratings by showing that the new player plus-minus ratings produce more predictive results when factoring in player positions. 

The rest of this paper is organized as follows. First, we introduce data and models in Sections 2 and 3. We then report the main findings in Section 4. Section 5 discusses possible explanations for these findings. We perform additional analyses and report analysis results in Section 6. Section 7 concludes this paper with a discussion of limitations and future studies. 

## **2 Data** 

Our analysis of positional plus-minus in the NBA uses data from three main sources. First, we rely on NBA play type data to determine players’ offensive positions, and utilize official player position data to identify defensive positions. Play type data document how players use their offensive possessions (McBasketball 2017). Specifically, the company Synergy Sports categorizes every offensive possession into one of the 11 play types (see Table 1). The raw play type data set tracks the number of offensive possessions finished under each play type. We standardize these numbers by computing the percentage of play types for each player. Play 

**Table 1:** Definitions of play types. 

|**Play type**|**Description**|
|---|---|
|Cut|Players using cut actions to score|
|Miscellaneous|Possessions do not fit in any other play types|
|Post-up|Players receiving the ball in the post to score|
|P & R man|Pick-and-Roll actions with screeners as scorers|
|Putback|Scoring after receiving offensive rebounds|
|Transition|Scoring in transition when defense is not set.|
|Hand-off|Scoring through hand-off actions|
|Off-screen|Players running off of screens to score|
|P & R handler|Pick-and-Roll actions with ball handlers as scorers|
|Spot-up|Players spotting up to score|
|Isolation|One-on-one actions to score|



type data are available on the NBA official statistics website since the 2015–16 season. 

It is worth noting that Synergy does not report play types for all players on the NBA website. To be qualified, a player must play at least 10 minutes per game during a regular season and have at least 10 possessions in a particular play type. For example, if a player averaged 5 minutes per game throughout a regular season, this player would not appear in any play type data set. In other cases, if a player averaged more than 10 minutes per game but played fewer than 10 possessions in one play type, this player would not appear in that particular play type data set. Therefore, there exist some missing values in play type data. 

We take several steps to handle the missing values to ensure the completeness of the data set. First, for players who play less than 10 minutes per game in a regular season and consequently lack play type data, we categorize them into a new group labeled as low usage players. Table 2 shows the number of low usage players from 2015–16 to 2021–22. On average, low usage players account for 20 percent of all players in a given season. Second, for players missing particular play type data due to the insufficient count of possessions, we assume equal percentages for these missing play types. For example, if a player misses data on three play types with 3 percent of unassigned offensive possessions, then we assume each missing play type accounts for 1 percent of the player’s offensive possessions. 

We also draw official player position data from the NBA official statistics website in order to identify players’ defensive positions. NBA players may play different positions throughout a season. Thus, it is common to see multiple positions associated with one player. The NBA offers seven combinations of player positions between C (Center), F (Forward), and G (Guard) (see Table 3). We rely on these official player positions to group players into one of the three defensive positions, Big, Forward, and Guard. 

> H. Gong and S. Chen: Positional plus-minus **— 195** 

**Table 2:** Number of players by position and season. 

|**Position**|**2015–16**|**2016–17**|**2017–18**|**2018–19**|**2020–21**|**2021–22**|**Total**|
|---|---|---|---|---|---|---|---|
|Skilled Big|44|41|48|46|57|65|301|
|Versatile Scorer|49|48|52|50|36|44|279|
|Secondary Attacker|53|45|63|56|85|82|384|
|Pick and Roll Attacker|65|73|75|75|70|66|424|
|Roll and Cut Big|52|50|51|45|51|57|306|
|Movement Shooter|34|42|38|41|28|28|211|
|Post-up Big|56|41|37|40|29|18|221|
|Spot-up Shooter|42|49|57|75|88|111|422|
|Big|98|92|88|87|88|91|544|
|Forward|126|122|129|137|141|148|803|
|Guard|171|175|204|204|215|232|1201|
|Low usage|81|97|120|103|97|134|632|



**Table 3:** Defensive position map. 

**Table 4:** Number of stints by season. 

|**Defensive position**|**NBA official player position**|
|---|---|
|Big|C, C–F, F–C|
|Forward|F, F–G|
|Guard|G, G–F|



Big players are often interior defenders, primarily tasked with protecting the paint area, while Guards and Forwards are generally exterior defenders. We rely on players’ primary position, typically denoted by the first letter of their official player positions, to determine their defensive roles. Specifically, if the primary position of a player is C, then this player will be placed into the Big group. Players with the primary position F and G will be assigned to the Forward and Guard groups respectively. The only exception is the players with the official position F–C. In this case, we place this set of players in the Big group rather than the Forward group, since they may appear more often as interior defenders with their secondary position being C. 

Lastly, we gather NBA play-by-play data between 2015–16 to 2021–22 from the NBA official statistics website. We omit the NBA 2019-20 season from our analysis, since it was interrupted by the COVID-19 pandemic and had many games played at neutral sites. NBA play-by-play data track a sequence of game-related events on the court, capturing information such as team scores, time left, and player or team actions at a particular point in an NBA game. Many advanced player metrics, such as RAPM, are derived from play-by-play data (Engelmann 2017; Franks et al. 2016; Pelechrinis and Papalexakis 2016). 

From NBA play-by-play data, we extract information related to the performance of stints. A stint can be defined as a unique matchup between five offensive players from 

|**Season**<br>**Number**|
|---|
|2015–16<br>61,502|
|2016–17<br>60,902|
|2017–18<br>60,548|
|2018–19<br>62,133|
|2020–21<br>52,784|
|2021–22<br>61,271|



one team and five defensive players from another team. We treat a stint as the unit of observation in our statistical model. For each stint in a season, we count the total number of offensive possessions played and the total number of points scored by players on the offensive team. Table 4 reports the total number of unique stints in each season from 2015–16 to 2021–22. It is worth mentioning that some plus-minus studies do not distinguish offensive and defensive teams in stints. Consequently, their counts of stints can be considerably smaller than what we present in Table 4 (Deshpande and Jensen 2016; Jacobs 2019). 

## **3 Methodology** 

Our analysis of positional plus-minus in the NBA consists of two main steps. First, we establish players’ offensive positions by analyzing NBA play type data with the Fuzzy K-means clustering algorithm. Subsequently, we construct a hierarchical linear model to estimate positional plus-minus based on position groups defined in the first step. 

The Fuzzy K-means clustering method is a powerful algorithm for partitioning data points into smaller groups. Unlike the traditional K- means algorithm that assigns each data point to a group in a binary way, Fuzzy K-means calculates to which degree each observation belongs to different groups (Bezdek et al. 1984). This approach works well in our analysis, as some players may not perfectly fit into any single position. Thus, we use a player’s probabilities of belonging to various 

> **196 —** H. Gong and S. Chen: Positional plus-minus 

offensive positions to represent the uncertainty associated with Fuzzy K-means clustering results. We also employ the K-means++ algorithm to choose the initial values of centroids that are well separated from each other. This initialization step ensures more stable clustering outcomes (Arthur and Vassilvitskii 2007). 

Before implementing the Fuzzy K-means algorithm, we standardize all play type percentage numbers and exclude data from the miscellaneous category. This category, as defined by Synergy Sports, encompasses offensive possessions that cannot be clearly classified into any other play type. In total, we feed 10 standardized play types to the Fuzzy K-means algorithm to group players into distinct offensive roles. For defensive positions, we rely on official player positions to define three defensive roles, Big, Forward, and Guard, as detailed in Section 2. 

After assigning one offensive and one defensive position to each player, we propose a hierarchical linear model to estimate positional offensive and defensive plus-minus in the NBA. The model has the following specification: 



where _X_ is an m by 2 _n_ player matrix filled with values of 1, −1, and 0. The letter _n_ represents the number of unique players in a season. The matrix _X_ has 2 _n_ columns because the first _n_ columns represent offensive players while the last _n_ columns indicate defensive players. The letter m denotes the total number of stints in a given season. The letter e is a vector of independent errors with a mean equal to 0 and variance equal to _𝜎_<sup>2</sup> . 

The value of 1 in _X_ indicates a player is on the floor and is with the team playing offense in a stint. The value of −1 suggests a player is on the court and is with the team playing defense. The value of 0 means the player is not on the floor. The letter _Z_ represents an m by 2 _k_ team matrix filled with 1, −1, and 0, where _k_ equals the number of unique teams in a season. The first _k_ columns represent offensive teams and the last _k_ columns denote defensive teams. Similar to the player matrix, the values of 1, −1, and 0 in the _Z_ matrix indicate offensive, defensive, and other teams respectively in a stint. 

The response variable _y_ is an m by one vector, representing points scored per 100 possessions by offensive teams in stints. For example, if an offensive team in a stint scored 20 points in 20 possessions, the response value will be equal to 100. Let _yi_ denotes the _i_ th element of _y_ . Model (2) implies that _yi_ ’s are independent of each other and follow a normal distribution with constant variance, conditional on _X_<sup>_i_</sup> and _Z_<sup>_i_</sup> , 



The intercept term _𝛽_ 0 represents a baseline effect. The coefficient _𝛽_ is a vector of 2 _n_ player effects. The coefficient _𝛾_ is a vector of 2 _k_ team effects. We put the following priors on model coefficients _𝛽_ and _𝛽_ 0. 







where the player effect _𝛽 p_ follows a mixture of normal distributions with each normal distribution having a group mean of _𝜇 j_ and group variance of _𝜏_<sup>2where</sup><sup>_j_isfrom1to11witheightoffensiveandthree</sup> _j_<sup>,</sup> defensive positions. The notation _𝜔 j_<sup>_p_referstoplayer</sup><sup>_p_’sprobability</sup> of belonging to position j, which is estimated from the Fuzzy K-means algorithm for offensive positions. If a player is low usage, then we 

assume its player effect _𝛽_ low follows a normal distribution with a mean equal to 0 and variance equal to 5, where _low_ refers to a low usage player. The intercept term _𝛽_ 0 has a non-informative normal distribution with mean 0 and variance 1,000,000. 

We assume the team effect _𝛾 t_ comes from a normal distribution with a mean equal to 0 and variance equal to 5. 



where _t_ represents an individual team. 

Below are the hyperprior distributions for the group mean _𝜇 j_ , group variance _𝜏_<sup>2</sup> _j_<sup>, error variance</sup><sup>_𝜎_2.</sup> 



We then construct a Gibbs sampler to derive the posterior distributions for group level parameters (i.e., _𝜇 j_ , and _𝜏_<sup>2</sup> _j_<sup>).Thegrouplevel</sup> parameters are key of interest, but similar inference can be done for individual level and team level parameters in this study. In Sections 4.2 and 4.3, we will report positional plus-minus and the top player plusminus ratings for each position group respectively. The details of the Gibbs sampler can be found in Appendix A. 

To demonstrate the predictive power of new plus-minus ratings, we also conduct a cross-validation analysis to compare the prediction accuracy of our player plus-minus to other plus-minus metrics. Specifically, we apply 5-fold cross-validation to single season data, and evaluate the Root Mean Square Error (RMSE) between our model and other models. When selecting reference groups for comparison, we pick the RAPM model, which is a non-positional metric, and the model using three position groups (i.e., Big, Forward, Guard) to classify players’ offensive and defensive roles. All cross-validation models include an intercept term, player effects, and team effects. 

## **4 Results** 

### **4.1 Player positions** 

We apply the Fuzzy K-mean algorithm to NBA play type data to derive eight clusters, with each cluster representing a distinct offensive player position. The elbow plot (Figure 1) shows the relationship between the number of clusters and the corresponding total within-clusters sum of squares (WSS). Our decision to choose eight clusters is grounded in the examination of the Fuzzy K-means elbow plot and our domain knowledge in basketball. Determining the optimal number of clusters in Fuzzy K-means can be challenging, as the algorithm is often considered as a heuristic method (Brusco and Cradit 2001). Consequently, scholars often search for the stopping point at which the subsequent number of clusters no longer significantly reduces the WSS. In our case, the eighth cluster seems to produce the relatively low WSS. Another consideration of selecting eight clusters is that the chosen number of clusters can result in 

> H. Gong and S. Chen: Positional plus-minus **— 197** 



**Figure 1:** Fuzzy K-means elbow plot. 

a sufficient number of players in each cluster (see Table 2). This, in turn, enables player plus-minus to effectively inform positional plus-minus. 

In Table 5, we present the centroids of the eight offensive positions. These centroid values serve as the basis for assigning names to the derived positions. These offensive positions are labeled as follows: Roll and Cut Big, Post-up Big, Skilled Big, Movement Shooter, Spot-up Shooter, Versatile Scorer, Pick and Roll Attacker, and Secondary Attacker. In particular, players categorized as Roll and Cut Bigs often employ pick-and-roll and cutting actions as their primary means of scoring. They also contribute to team offense through putbacks after securing offensive rebounds. Postup Bigs predominantly depend on post-up actions to score points. They also utilize pick-and-roll actions to score, but 

not as frequently as Roll and Cut Bigs. It is worth noting the there is a substantial decline in the presence of Post-up Bigs in the league over time. Table 2 shows the number of Post-up Bigs has reduced from 56 players during the 2015–16 season to a mere 18 players in the 2021–22 season. On the other hand, Skilled Bigs, who can score not only through pick-and-rolls but also spot-up shooting, have witnessed a notable growth in their representation. Their numbers have increased from 44 in 2015–16 to 65 in 2021–22 (see Table 2). 

Movement Shooters appear to be the best shooters in the league. Their offensive possessions are largely finished with off-screen, hand-off, and spot-up plays, which require proficient shooting skills in players. In contrast to Movement Shooters, Spot-up Shooters exceedingly rely on spot-up shooting on offense. They often position in the 

**Table 5:** Centroids of play types for offensive positions. 

||**Cut**|**Post-up**|**P & R man**|**Putback**|**Transition**|**Hand-off**|**Off-screen**|**P & R handler**|**Spot-up**|**Isolation**|
|---|---|---|---|---|---|---|---|---|---|---|
|Skilled Big|10 %|7 %|14 %|8 %|12 %|2 %|3 %|3 %|30 %|4 %|
|Versatile Scorer|3 %|4 %|2 %|2 %|15 %|5 %|4 %|31 %|15 %|14 %|
|Secondary Attacker|5 %|2 %|2 %|3 %|19 %|7 %|5 %|18 %|30 %|5 %|
|Pick and Roll Attacker|3 %|2 %|1 %|2 %|15 %|6 %|3 %|36 %|20 %|7 %|
|Roll and Cut Big|24 %|6 %|23 %|18 %|8 %|1 %|1 %|1 %|7 %|2 %|
|Movement shooter|4 %|2 %|2 %|2 %|16 %|11 %|16 %|13 %|28 %|3 %|
|Post-up Big|13 %|22 %|19 %|11 %|7 %|1 %|2 %|1 %|12 %|4 %|
|Spot-up Shooter|7 %|3 %|4 %|5 %|19 %|4 %|4 %|7 %|39 %|3 %|



> **198 —** H. Gong and S. Chen: Positional plus-minus 

**Table 6:** Mean and standard deviation of positional plus-minus mean estimate. 

|**Position**|**2015–16**|**2016–17**|**2017–18**|**2018–19**|**2020–21**|**2021–22**|
|---|---|---|---|---|---|---|
|Skilled Big|2.9 (1.1)|3.2 (1.1)|2.9 (1.2)|2.9 (1.1)|3.6 (1.1)|3.3 (1)|
|Versatile Scorer|5.8 (1.2)|5.9 (1.3)|4.7 (1.1)|5 (1.1)|7.6 (1.2)|5.7 (1.2)|
|Secondary Attacker|4 (1)|4 (1.1)|3.2 (1)|3.7 (1)|4.3 (1)|2.9 (1)|
|Pick and Roll Attacker|4.6 (1)|4.2 (1.2)|3.5 (1.1)|3.7 (1)|4.8 (1.1)|3.2 (1.1)|
|Roll and Cut Big|1.5 (1)|2.6 (1.1)|0.2 (1.2)|3.4 (1.1)|3.1 (1.2)|4 (1.1)|
|Movement Shooter|4.8 (1.2)|4.4 (1.3)|4.1 (1.1)|3.9 (1.1)|5.8 (1.3)|3.8 (1.2)|
|Post-up Big|3.1 (1.1)|3.7 (1.2)|1.6 (1.4)|4.6 (1.2)|3.8 (1.4)|3.9 (1.3)|
|Spot-up Shooter|3.6 (1.1)|4.1 (1.1)|2.6 (1)|3.7 (1)|3.8 (1)|2.9 (1)|
|Big|5.1 (1.1)|3.6 (1)|3.3 (1)|3.7 (0.9)|2.4 (1.2)|3 (1.3)|
|Forward|3.4 (1.1)|2.2 (1)|1.9 (0.8)|1.8 (0.9)|1.3 (1)|1.7 (1.2)|
|Guard|1.7 (1)|−0.2 (0.9)|1.2 (0.9)|0.1 (0.9)|−0.4 (1)|1.6 (1.2)|



Standard deviations are in parentheses. 

**Table 7:** Mean and standard deviation of positional plus-minus variance estimate. 

|**Position**|**2015–16**|**2016–17**|**2017–18**|**2018–19**|**2020–21**|**2021–22**|
|---|---|---|---|---|---|---|
|Skilled Big|9.5 (6)|3.1 (3.8)|6.3 (5.4)|8.5 (6.3)|2.8 (3.7)|12.7 (1.8)|
|Versatile Scorer|10.3 (5.4)|16.9 (6.8)|7.9 (5.2)|8.2 (5.3)|6.6 (5.7)|5.5 (6)|
|Secondary Attacker|2.3 (2.7)|4.1 (3.8)|2.2 (2.6)|8.7 (4.4)|2.6 (2.8)|9.3 (3.7)|
|Pick and Roll Attacker|3.4 (3.2)|11.1 (4.6)|4.9 (3.5)|7.6 (4.2)|8 (4.4)|4 (4.5)|
|Roll and Cut Big|2.3 (3)|1.1 (1.8)|12.3 (6.7)|2.9 (3.8)|3.3 (3.9)|3.7 (4.4)|
|Movement Shooter|8 (6.2)|11.6 (7.1)|2.5 (3.4)|6.6 (5.4)|4 (4.8)|4.7 (4.7)|
|Post-up Big|3.2 (3.2)|12.1 (6.5)|20.3 (9.5)|9.3 (6.9)|11 (9.9)|3.1 (5.9)|
|Spot-up Shooter|2.1 (2.9)|1 (1.6)|2.8 (3.1)|7.3 (4.5)|1.7 (2.4)|5 (2.7)|
|Big|3.2 (2.7)|1.6 (1.8)|2.6 (2.5)|1.1 (1.5)|0.6 (1)|1.4 (0.9)|
|Forward|3.1 (2.2)|3.4 (2.4)|0.6 (1)|4.3 (2.3)|2.2 (2.3)|4.4 (1.6)|
|Guard|4.5 (1.9)|1.8 (1.4)|6.3 (2.1)|2.5 (1.6)|3.1 (2.2)|5 (1.7)|



Standard deviations are in parentheses. 

corners of a basketball court and wait to catch and shoot the ball. Notably, the number of Spot-up Shooters has increased considerably since the NBA 2020–21 season (see Table 2). Versatile Scorers are all-around players capable of scoring through various actions, such as isolation, transition, and pick-and-roll. Next, Pick-and-Roll Attackers primarily employ pick-and-roll strategies to score points, dedicating far fewer possessions to isolation plays than Versatile Scorers. Lastly, Secondary Attackers are intermediate players positioned between Pick-and-Roll Attackers and Spotup Shooters. While they can score through pick-and-roll actions, they do not do so as often as Pick-and-Roll Attackers. Similarly, they can score with spot-up shooting, but not as frequently as Spot-up Shooters. 

### **4.2 Positional plus-minus** 

positional plus-minus. Tables 6 and 7 summarize the mean and standard deviation of position level mean and variance parameters. In the following text, we focus on comparing the values of parameters across positions and seasons as well as interpreting the differences in these values. 

#### **4.2.1 Comparison of plus-minus across positions by season** 

Figure 2 visualizes average offensive plus-minus for various positions in the NBA from the 2015–16 to 2021–22 seasons.<sup>1</sup> These results indicate that Versatile Scorers consistently outperform the other positions in terms of offensive plus-minus. To estimate the probabilities that Versatile Scorers’ offensive plus-minus is higher than the others, we draw samples from the posterior distributions of offensive 

After we determine offensive and defensive positions for players, we run the same hierarchical Bayesian linear model for each of the six NBA seasons separately to estimate 

**1** Dashed lines represent posterior means. 

> H. Gong and S. Chen: Positional plus-minus **— 199** 



**Figure 2:** NBA positional offensive plus-minus mean estimate from 2015–16 to 2021–22. 



**Figure 3:** Eighty percent credible intervals of the differences of offensive plus-minus between Versatile Scorers and the other offensive positions. 

plus-minus and compute the differences between these posterior samples. Figure 3 displays the 80 % credible intervals of the differences of offensive plus-minus between Versatile Scorers and the other positions. Notably, the majority of these intervals lie above zero, indicating that Versatile 

Scorers are the most valuable offensive contributors in most seasons.<sup>2</sup> 

**2** Red dots represent the means of differences. 

> **200 —** H. Gong and S. Chen: Positional plus-minus 

Another observation from Figure 2 is that the gaps in positional offensive plus-minus have diminished over the years. In particular, there are notable differences in offensive plus-minus in 2015–16 among position groups, with Versatile Scorers leading and Roll and Cut Bigs at the bottom of the list. By the 2021–22 season, these differences narrowed as the average offensive plus-minus values for each position move closer to each other. However, Versatile Scorers consistently stood out, maintaining higher plus-minus ratings than the rest. This trend suggests that while distinctions in positional offensive plus-minus have become subtler over the years, Versatile Scorers persist as the cornerstone of team offense. 

On the defensive side, Figure 4 illustrates that Bigs’ average defensive plus-minus consistently ranks the highest among the position groups. To estimate the probabilities that Bigs’ defensive plus-minus surpasses the other positions’ defensive plus-minus, we construct the 80 % credible intervals of the differences of defensive plus-minus between Bigs and the other defensive positions 

from 2015–16 to 2021–22 in Figure 5. Most intervals locate well above zero, providing strong evidence that Bigs create more defensive value than the others in the NBA. 

In addition to deriving average positional ratings<sup>(</sup> _𝜇 j_ ), the variance of positional plus-minus _𝜏_<sup>2</sup> can be easily ( _j_ ) estimated in our study. Figure 6 shows the consistently low variance of offensive plus-minus for Spot-up Shooters compared to the other offensive positions. On the other hand, Post-up Bigs and Versatile Scorers display notably higher variances of their offensive plus-minus relative to the other positions. These observations indicate that there might be significant variation in offensive plus-minus among players in these two positions. Meanwhile, the offensive efficiency of Spot-up Shooters appears to be relatively consistent across different players. 

Figure 7 plots the posterior distributions of positional defensive plus-minus variance estimates. The mean variance of Guards’ defensive plus-minus seems notably greater than these of the other positions. This finding indicates that Guards display a broader range of defensive efficiency 



**Figure 4:** NBA positional defensive plus-minus mean estimate from 2015–16 to 2021–22. 



**Figure 5:** Eighty percent credible intervals of the differences of defensive plus-minus between Bigs and the other defensive positions. 

> H. Gong and S. Chen: Positional plus-minus **— 201** 



**Figure 6:** NBA positional offensive plus-minus variance estimate from 2015–16 to 2021–22. 



**Figure 7:** NBA positional defensive plus-minus variance estimate from 2015–16 to 2021–22. 

compared to Forwards and Bigs. The 80 % credible intervals of the variance differences between Guards and the other defensive positions do not include zero in most cases.<sup>3</sup> This offers some evidence that the variation in Guards’ defensive plus-minus is greater than the other positions’. 

> **3** Eighty percent credible intervals are not shown here. They are available upon request. 

#### **4.2.2 Comparison of plus-minus across seasons by position** 

Figure 8 aims to compare offensive plus-minus across seasons by position. In particular, Roll and Cut Bigs have shown significant progress in their offensive plus-minus from 2015–16 to 2021–22. Both Post-up Bigs and Skilled Bigs also saw enhancements in their offensive plus-minus over 

> **202 —** H. Gong and S. Chen: Positional plus-minus 



**Figure 8:** NBA offensive plus-minus mean estimate by position. 



**Figure 9:** NBA offensive plus-minus variance estimate by position. 

this period. The other positions’ offensive plus-minus stays relatively stable from season to season. 

Figure 9 shows the posterior distributions of offensive plus-minus variance estimates across eight offensive roles. The mean variances of positional offensive plus-minus 

appear to be fairly consistent over the seasons. Figures 10 and 11 visualize the posterior distributions of defensive plus-minus mean and variance estimates respectively. Neither of them exhibits any particular pattern over the years. 

> H. Gong and S. Chen: Positional plus-minus **— 203** 



**Figure 10:** NBA defensive plus-minus mean estimate by position. 



**Figure 11:** NBA defensive plus-minus variance estimate by position. 

### **4.3 Player plus-minus and cross-validation** 

While our analysis of plus-minus focuses on estimating positional values in the NBA, it maintains the flexibility of estimating plus-minus ratings for individual players. We report the top five plus-minus ratings for each offensive and defensive position group in Appendix C. 

We also conduct cross-validation tests to demonstrate the improved predictive power of our player plus-minus ratings. Table 8 shows the RMSE for RAPM with a range of penalty values _𝜆_ (i.e., 500, 1500, and 3000), the RMSE for the model using three traditional basketball position groups (3-position) (i.e., Big, Forward, Guard), and the RMSE for our model with redefined eight offensive positions (8-position). Cross-validation results show both 3-position and 8-position 

models outperform the RAPM models in all six seasons. This finding suggests that the player position is an important factor to consider in estimating player plus-minus. In addition, the 8-position model produces the best RMSE among all models across six seasons. This result indicates that redefined offensive positions by play type data may better capture offensive roles of NBA players than traditional position groups in basketball, and thus can help estimate more predictive player plus-minus ratings. 

## **5 Discussion** 

Recall in Figures 2 and 3 we show that Versatile Scorers produce the highest offensive value among all the offensive 

**Table 8:** Cross-validation results. 

|**Model**|**_𝝀_**|**2015–16 RMSE**|**2016–17 RMSE**|**2017–18 RMSE**|**2018–19 RMSE**|**2020–21 RMSE**|**2021–22 RMSE**|
|---|---|---|---|---|---|---|---|
|RAPM|500|78.725|79.758|80.152|79.921|80.223|80.612|
|RAPM|1500|78.710|79.739|80.142|79.911|80.207|80.610|
|RAPM|3000|78.733|79.763|80.171|79.940|80.232|80.626|
|3-position||78.691|79.718|80.118|79.900|80.194|80.600|
|**-position**||**.**|**.**|**.**|**.**|**.**|**.**|



Bold values represent the RMSE from the model adopted in the present study. Lower RMSE values indicate better model performance. 

> **204 —** H. Gong and S. Chen: Positional plus-minus 

positions. We define Versatile Scorers as players who primarily rely on isolation, transition, and pick-and-roll actions to score points. As such, these players are likely to be the ball-dominant players who control the ball most of the time on the court. Teams often allow star players to take on this role because they are generally more proficient at scoring. Hence, it is not surprising that Versatile Scorers register higher offensive plus-minus ratings than players in the other positions. 

By comparing estimation results across the six NBA seasons, we show that the gaps in offensive plus-minus between the eight offensive positions have diminished over time. After further examining how offensive plus-minus have changed over the years for each position, we notice that the improvement of Roll and Cut Bigs may significantly contribute to the shortened gaps. Specifically, Figure 8 shows a consistent upward trend in their offensive plus-minus from 2015–16 to 2021–22. Considering that the quantity of Roll and Cut Bigs remains relatively stable over the years (as shown in Table 2), we believe the enhanced offensive plus-minus could be attributed to increased offensive efficiency among Roll and Cut Bigs. Furthermore, we note a gradual increase in Post-up Bigs’ and Skilled Bigs’ offensive plus-minus over time, though their plus-minus ratings do not seem to rise as significantly as Roll and Cut Bigs’. 

The estimated variances of positional plus-minus also present some interesting findings. Recall in Figure 6 that the mean variances of Spot-up Shooters’ offensive plus-minus are the smallest in most seasons spanning from 2015–16 to 2021–2022. This finding could be attributed to the role of Spot-up Shooters, which typically involves less prominent involvement in team offense. On the contrary, the mean variances of Post-up Bigs’ and Versatile Scorers’ offensive plus-minus are consistently higher than the others in Figure 6. The steep decline in quantity and the relatively low number of Post-up Bigs in the NBA may partially explain the high variation in Post-up Bigs’ offensive plus-minus (see Table 2). This finding may also indicate that scoring proficiency in offense-oriented positions, such as Versatile Scorers and Post-up Bigs, can vary greatly from one player to another in the NBA. 

On the defensive side, Figure 4 shows that Bigs tend to provide more defensive value than the other positions. This finding is not surprising as Bigs are not only responsible for defending opposing Bigs but also play a crucial role in preventing opponents from scoring in the paint area. As such, interior players may carry more defensive responsibility, creating more defensive impact than exterior players. Guards, limited by their size, offer the least 

defensive value to teams in Figure 4. Additionally, it is worth noting that despite Guards having the lowest defensive plus-minus, they exhibit the highest variability in defensive performance among the three defensive positions. In simpler terms, the defensive plus-minus values for Guards are more dispersed around the average compared to those of Bigs and Forwards. This observation implies that there may exist some exceptional defenders or some extremely poor defenders in the Guard position. 

Another significant contribution of our findings is that the prediction accuracy of the new player plus-minus surpasses that of many existing player plus-minus metrics, as reported in Section 4.3. While our study does not intend to optimize the prediction accuracy of player effects, it shows that factoring in player positions when setting priors for player plus-minus may improve metric performance (Matano et al. 2023). A similar study conducted by Intraocular (2022) echoes our finding that considering player positions in player prior distributions may help produce more predictive player plus-minus. However, one major difference between our analysis and Intraocular’s model lies in the fact we assign players into one of the eight offensive roles based on their play types, while Intraocular’s model considers traditional basketball player positions, Bigs, Wings, and Guards. Our cross-validation results in Table 8 suggest that player plus-minus estimated from the 8-position model may perform better than the estimates from the 3-position model in most seasons. This finding suggests that using well-defined player roles can potentially enhance the predictiveness of player plus-minus ratings. 

Our analysis of positional plus-minus also resembles Sabin’s (2021) study that uses similar Hierarchical Bayesian models to estimate player plus-minus in the NFL. In constructing priors for player-level plus-minus, he redefined variance parameters in a t-distribution by linking them to position-level parameters. Our study follows a similar hierarchical structure in constructing priors for player-level plus-minus, but with different prior distributions (i.e., a mixture of Gaussians). Additionally, Sabin (2021) considered linear weighted player positions in constructing prior parameters with weights being players’ predicted percentages of snaps at different positions. Our model also uses weighted positions in player priors, but with the weights determined by the probabilities of a player belonging to each position group. Despite these differences, both our model and Sabin’s model point to the same conclusion that factoring in player positions produces more predictive player plusminus results. 

> H. Gong and S. Chen: Positional plus-minus **— 205** 

## **6 Additional analyses** 

To check the robustness of our estimation results, we conduct a few additional analyses. First, we refine our play-byplay data set by filtering out garbage time in which teams do not place their best possible players on the court. Second, we re-estimate both positional offensive and defensive plus-minus based on traditional basketball player positions, Guard, Forward, and Big. We report these analysis results below. 

### **6.1 Garbage time** 

We employ the definition of garbage time from the basketball analytics website, Cleaning the Glass (Falk n.d.). In general, the website considers the time when the score differential is large toward the end of the game and two teams no longer field their best players as garbage time. Specifically, three factors are used to determine garbage time, the quarter, score differential, and the number of starters on the floor. For example, if a game is in the fourth quarter, one team is leading the other by 15 points with 2 min left on the clock, and the total number of starters on the floor combined from the two teams is 1, then the website will consider this period as garbage time. The details of garbage time thresholds can be found in Table 9 in Appendix B. 

Overall, we find similar positional plus-minus estimation results as before. To better visualize these findings, 

we place the estimates from play-by-play data with and without garbage time side by side in Figures 12 and 13. It is clear that removing garbage time from play-by-play data does not significantly alter our prior findings, except for the 2020–21 season when positional plus-minus from the full data set seems higher than positional plus-minus derived from the data set without garbage time. We suspect this is because 2020–21 season games contain more garbage time than games in the other seasons, as 2020–21 is the first full season since the interrupted 2019–20 season due to the COVID-19 pandemic. Data analysis provides some support for this possibility. After counting the percentage of garbage time in each of the six seasons examined in this study, it appears that almost 4 percent of possessions are classified as garbage time in the 2020–21 season, whereas only 3.4 to 3.7 percent of possessions are considered garbage time in the other seasons. 

### **6.2 Three offensive positions** 

We also re-estimate positional offensive plus-minus based on three positions groups (i.e., Guard, Forward, and Big). Recall that our main analysis defines eight offensive roles based on players’ play types, while defensive positions are derived from traditional basketball positions. Here we reestimate offensive plus-minus similarly to defensive plusminus in order to compare the results derived from conventional player positions with those from play type-based positions. 



**Figure 12:** Comparison of positional offensive plus-minus mean estimate across seasons with and without garbage time. 

> **206 —** H. Gong and S. Chen: Positional plus-minus 



**Figure 13:** Comparison of positional offensive plus-minus variance estimate across seasons with and without garbage time. 



**Figure 14:** NBA offensive plus-minus from 2015–16 to 2021–22 with three offensive positions. 

Figures 14 and 15 show the posterior distributions of offensive plus-minus for the three traditional positions, Guard, Forward, and Big. Similar to our main findings, the estimates suggest the gaps in positional offensive plusminus have shrunk over time. In particular, Bigs’ offensive plus-minus has increased considerably from 2015–16 to 2021–22. These findings provide further evidence that the improvement by Bigs narrows the gap in offensive plusminus between the eight offensive positions. 

Figure 16 compares offensive and defensive plus-minus variance estimates between Bigs, Forwards, and Guards. Results show that the mean variances of offensive plusminus generally surpass those of defensive plus-minus in most seasons. This suggests that the variation in defensive ability is relatively small among NBA players than offensive ability. Figure 16 also shows the low correlations between offensive and defensive plus-minus variance estimates. 

> H. Gong and S. Chen: Positional plus-minus **— 207** 



**Figure 15:** NBA offensive plus-minus across three offensive positions. 



**Figure 16:** Comparison of NBA positional plus-minus variance estimate between Bigs, Forwards, and Guards. 

## **7 Conclusions** 

In this study, we have employed a hierarchical Bayesian linear model to estimate positional plus-minus from 2015–16 to 2021–22 based on redefined offensive and defensive positions in the NBA. Our analysis finds that Versatile Scorers and Bigs have the highest positional offensive and defensive plus-minus respectively. We also show that the variance of Spot-up Shooters’ offensive plus-minus is the lowest among the eight offensive positions, while the variances of Post-up Bigs’ and Versatile Scorers’ offensive plus-minus are substantially higher than the others. On the defensive side, we note that Guards have the lowest average defensive plus-minus, but the highest variance among the three defensive positions. 

Through the analysis of positional offensive plus-minus from 2015–16 to 2021–22 in the NBA, it becomes evident 

that the gaps in offensive plus-minus between the eight offensive positions have decreased over the years. That is, the positional offensive plus-minus values become closer to each over time, except for Versatile Scorers, whose offensive plus-minus consistently ranks higher than the others. Additionally, we have noted that the increase in offensive plus-minus for Roll and Cut Bigs may play a significant role in closing the gaps. 

In addition to estimating positional plus-minus values and comparing them across position groups and seasons, our analysis develops more predictive plus-minus ratings for individual NBA players. Cross-validation results show that the new player plus-minus produces higher prediction accuracy than non-positional plus-minus models (i.e., RAPM) and the 3-position plus-minus model in most seasons. 

Our study of positional plus-minus has a few limitations. First, the response variable, points scored per 100 

> **208 —** H. Gong and S. Chen: Positional plus-minus 

possessions, employed in this study does not reflect the importance of points in a game. In fact, we treat points scored or allowed equally throughout a game. However, it is common to see points scored in a close game toward the end of the game are far more important than points acquired in the first quarter. Second, the clustering results for offensive positions are subjective as the Fuzzy K-means algorithm is a heuristic method. Therefore, the eight offensive positions we proposed in this study may not be the best solution for grouping players. 

Future studies of positional plus-minus may consider using win probability as the response variable. The calculation of win probability takes game situations into consideration. Thus, regressing the change in win probability over stints may better estimate positional contributions to team success (Deshpande and Jensen 2016). Future research may also employ new data to cluster players. In particular, the availability of player tracking data in major sports leagues may allow scholars to produce more detailed and accurate classifications of player positions in sports. 

**Acknowledgments:** The authors would like to thank the editors and reviewers for their constructive and thoughful feedback and comments. 

in Equation (3). The vector indicates which position group player _p_ belongs to in an iteration and has a multinomial distribution with the player’s probabilities of belonging to different position groups. For each iteration in Gibbs sample, we first draw _z_ for each player. Then we use the following conditional posterior distributions for _𝜇 j_ and _𝜏_<sup>2</sup> _j_ to draw posterior samples. 



where _k_ is the number of players that belong to group _j_ in an iteration. The notation _p j_ refers to player _p_ who belongs to position _j_ in an iteration. The letter _𝛽_ represents player effects. 

**Research ethics:** Not applicable. 

**Author contributions:** The authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Competing interests:** The authors state no conflict of interest. 

**Research funding:** None declared. 

**Data availability:** Not applicable. 

## **Appendix A** 

We construct a hierarchical Bayesian liner model to estimate positional plus-minus in this study. The Gibbs sampling method with 30,000 iterations and a burn-in period of 1000 is used to derive the estimates in the model. Our variables of interest are the mean and variance of positional plus-minus _𝜇 j_ and _𝜏_<sup>2</sup> _j_<sup>,where</sup><sup>_j_isfrom1to11witheight</sup> offensive positions and three defensive positions. 

To facilitate Gibbs sampling, we introduce a vector of latent variables _z_<sup>_p_</sup> to the mixture of normal distributions 

## **Appendix B** 

**Table 9:** Thresholds of NBA garbage time defined by the website Cleaning the Glass. 

||**Condition**|
|---|---|
|1|Game is in the 4th quarter|
|2|Score differential is larger than 25 when 9–12 min left|
|3|Score differential is larger than 20 when 6–9 min left|
|4|Score differential is larger than 10 when 0–6 min left|
|5|A total of two or fewer starters combined from the two teams<br>on the field|



The website also notes the game can never change from being garbage time to being non-garbage time. If any of the above conditions is not met and the game switches from being garbage time to being non-garbage time, then the garbage time clock resets. 

> H. Gong and S. Chen: Positional plus-minus **— 209** 

## **Appendix C** 

**Table 10:** NBA 2015–16 top five plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Draymond Green|8.2|Skilled Big|68 %|
|Patrick Patterson|5.9|Skilled Big|47 %|
|Mirza Teletovic|5.7|Skilled Big|27 %|
|Serge Ibaka|5.2|<br>Skilled Big|76 %|
|Kristaps Porzingis|5.1|Skilled Big|53 %|
|LeBron James|10.2|Versatile Scorer|72 %|
|Kevin Durant|8.7|Versatile Scorer|49 %|
|Chris Paul|8.7|Versatile Scorer|71 %|
|Russell Westbrook|8.6|Versatile Scorer|60 %|
|James Harden|7.9|Versatile Scorer|71 %|
|Eric Gordon|5.4|Secondary Attacker|42 %|
|Anthony Morrow|5.1|Secondary Attacker|30 %|
|Iman Shumpert|5|Secondary Attacker|43 %|
|Kentavious Caldwell-Pope|4.9|Secondary Attacker|79 %|
|C. J. Watson|4.7|Secondary Attacker|40 %|
|Kyle Lowry|8.1|Pick & roll Attacker|56 %|
|Jrue Holiday|6.5|Pick & roll Attacker|65 %|
|<br>Andre Miller|6|Pick & roll Attacker|41 %|
|Ricky Rubio|6|Pick & roll Attacker|85 %|
|<br>Rodney Hood|5.9|Pick & roll Attacker|44 %|
|Brandon Bass|3.7|Roll & cut Big|48 %|
|Willie Cauley-Stein|2.9|Roll & cut Big|80 %|
|Amir Johnson|2.7|Roll & cut Big|78 %|
|Alex Stepheson|2.6|Roll & cut Big|27 %|
|Cody Zeller|2.4|Roll & cut Big|70 %|
|Avery Bradley|7|Movement Shooter|83 %|
|Wesley Matthews|6.9|Movement Shooter|33 %|
|Klay Thompson|6.9|Movement Shooter|52 %|
|J. J. Redick|6.5|Movement Shooter|53 %|
|Nicolas Batum|6.2|Movement Shooter|64 %|
|Ryan Anderson|5.5|Post-up Big|36 %|
|<br>Dirk Nowitzki|4.7|<br>Post-up Big|62 %|
|Gorgui Dieng|4.5|Post-up Big|87 %|
|Paul Millsap|4.5|Post-up Big|56 %|
|Karl-Anthony Towns|4.3|Post-up Big|85 %|
|Jason Terry|4.8|Spot-up Shooter|47 %|
|Danny Green|4.7|Spot-up Shooter|52 %|
|Solomon Hill|4.5|Spot-up Shooter|64 %|
|Axel Toupane|4.5|Spot-up Shooter|66 %|
|<br>Harrison Barnes|4.4|<br>Spot-up Shooter|33 %|
|**Player**|**Defensive**|**plus-minus**|**Position**|
|Nikola Jokic||6.5|Big|
|Steven Adams||6.4|Big|
|Tim Duncan||6.3|Big|
|DeAndre Jordan||6.2|Big|
|Dwight Powell||6.2|Big|



> **210 —** H. Gong and S. Chen: Positional plus-minus 

**Table 10:** (continued) 

|**Player**|**Defensive plus-minus**|**Position**|
|---|---|---|
|Draymond Green|6.3|Forward|
|Kawhi Leonard|5.3|Forward|
|Wesley Johnson|4.8|Forward|
|Blake Griffin|4.7|Forward|
|Chris Bosh|4.7|Forward|
|Tony Snell|4.6|Guard|
|Danny Green|4.5|Guard|
|Kyle Korver|3.9|Guard|
|Evan Turner|3.7|Guard|
|Michael Carter-Williams|3.6|Guard|



**Table 11:** NBA 2016–17 top five plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Patrick Patterson|5|Skilled Big|45 %|
|Draymond Green|4.4|Skilled Big|55 %|
|Marvin Williams|4.2|Skilled Big|73 %|
|Okaro White|4.2|Skilled Big|48 %|
|Frank Kaminsky|4.2|Skilled Big|73 %|
|Kawhi Leonard|11.7|Versatile Scorer|80 %|
|Kyle Lowry|10.9|Versatile Scorer|61 %|
|LeBron James|9.8|Versatile Scorer|62 %|
|Russell Westbrook|9.8|Versatile Scorer|82 %|
|Chris Paul|9.6|Versatile Scorer|82 %|
|Patty Mills|6.6|Secondary Attacker|52 %|
|Tim Hardaway Jr.|5.8|Secondary Attacker|45 %|
|Aaron Gordon|5.7|Secondary Attacker|45 %|
|Jae Crowder|5.6|Secondary Attacker|36 %|
|Norman Powell|5.6|Secondary Attacker|39 %|
|Isaiah Thomas|10.6|Pick & roll Attacker|42 %|
|Lou Williams|8.8|Pick & roll Attacker|74 %|
|Kemba Walker|8.5|Pick & roll Attacker|76 %|
|Darren Collison|8.3|Pick & roll Attacker|88 %|
|Mike Conley|8.2|Pick & roll Attacker|46 %|
|David Lee|3.5|Roll & cut Big|71 %|
|Mason Plumlee|3.5|Roll & cut Big|78 %|
|Shawn Long|3.4|Roll & cut Big|59 %|
|Myles Turner|3.4|Roll & cut Big|39 %|
|Montrezl Harrell|3.3|Roll & cut Big|90 %|
|Stephen Curry|10.9|Movement Shooter|25 %|
|Gordon Hayward|8.3|Movement Shooter|35 %|
|J. J. Redick|7.5|Movement Shooter|65 %|
|Bradley Beal|6.9|Movement Shooter|57 %|
|<br>Marco Belinelli|6.8|Movement Shooter|86 %|
|Nikola Jokic|8.6|Post-up Big|99 %|
|Blake Griffin|7.8|Post-up Big|44 %|
|Karl-Anthony Towns|7.1|Post-up Big|90 %|
|Greg Monroe|7.1|Post-up Big|90 %|
|Kevin Love|6.5|Post-up Big|64 %|



> H. Gong and S. Chen: Positional plus-minus **— 211** 

**Table 11:** (continued) 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Andre Iguodala|4.9|Spot-up Shooter|68 %|
|Kyle Anderson|4.8|Spot-up Shooter|43 %|
|Derrick Jones Jr.|4.7|Spot-up Shooter|23 %|
|Rondae Hollis-Jefferson|4.7|Spot-up Shooter|26 %|
|Juancho Hernangomez|4.5|Spot-up Shooter|81 %|
|**Player**|**Defensive**|**plus-minus**|**Position**|
|Rudy Gobert||4.7|Big|
|Hassan Whiteside||4.3|Big|
|Nene||4.3|Big|
|Anthony Davis||4.2|Big|
|DeAndre Jordan||4.2|Big|
|P. J. Tucker||4.1|Forward|
|Paul Millsap||3.8|Forward|
|Draymond Green||3.7|Forward|
|Marcus Morris Sr.||3.7|Forward|
|Jonathon Simmons||3.5|Forward|
|Andre Iguodala||0.9|Guard|
|Chris Paul||0.9|Guard|
|Jrue Holiday||0.8|Guard|
|George Hill||0.7|Guard|
|Andre Roberson||0.7|Guard|



**Table 12:** NBA 2017–18 top five plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Bobby Portis|5.6|Skilled Big|48 %|
|Channing Frye|5|Skilled Big|71 %|
|Nikola Mirotic|4.9|Skilled Big|45 %|
|Frank Kaminsky|4.9|Skilled Big|65 %|
|DeMarcus Cousins|4.6|Skilled Big|27 %|
|Chris Paul|7.5|Versatile Scorer|60 %|
|Damian Lillard|7|Versatile Scorer|76 %|
|Russell Westbrook|6.7|Versatile Scorer|75 %|
|James Harden|6.6|Versatile Scorer|48 %|
|AustinRivers|6.2|Versatile Scorer|75 %|
|Eric Gordon|6|Secondary Attacker|39 %|
|Khris Middleton|5|Secondary Attacker|37 %|
|Robert Covington|4.2|Secondary Attacker|38 %|
|Tobias Harris|4.1|Secondary Attacker|38 %|
|Otto Porter Jr.|4.1|Secondary Attacker|47 %|
|Kemba Walker|6.6|Pick & roll Attacker|81 %|
|Eric Bledsoe|5.2|Pick & roll Attacker|64 %|
|Fred Van Vleet|5.1|Pick & roll Attacker|84 %|
|VictorOladipo|5|Pick & roll Attacker|46 %|
|Goran Dragic|5|Pick & roll Attacker|69 %|
|Jordan Bell|6|Roll & cut Big|64 %|
|John Henson|5.2|Roll & cut Big|88 %|
|Steven Adams|4.5|Roll & cut Big|93 %|
|CodyZeller|3.6|Roll & cut Big|77 %|
|Kevon Looney|3.1|Roll & cut Big|87 %|



> **212 —** H. Gong and S. Chen: Positional plus-minus 

**Table 12:** (continued) 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Stephen Curry|6.7|Movement Shooter|47 %|
|Allen Crabbe|4.9|Movement Shooter|90 %|
|Klay Thompson|4.8|Movement Shooter|52 %|
|Kyle Korver|4.7|Movement Shooter|58 %|
|Kentavious Caldwell-Pope|4.6|Movement Shooter|71 %|
|Karl-Anthony Towns|8.8|Post-up Big|99 %|
|Nikola Jokic|6.3|Post-up Big|99 %|
|Al Horford|5.7|Post-up Big|86 %|
|Anthony Davis|5.4|Post-up Big|68 %|
|LaMarcus Aldridge|4.3|Post-up Big|70 %|
|P. J. Tucker|4.5|Spot-up Shooter|67 %|
|Pascal Siakam|3.7|Spot-up Shooter|66 %|
|Luke Babbitt|3.6|Spot-up Shooter|34 %|
|Alex Abrines|3.5|Spot-up Shooter|60 %|
|Josh Hart|3.5|Spot-up Shooter|48 %|
|**Player**|**Defensive**|**plus-minus**|**Position**|
|Rudy Gobert||4.5|Big|
|Anthony Davis||4.3|Big|
|Myles Turner||4.3|Big|
|Joel Embiid||4.3|Big|
|Clint Capela||4.2|Big|
|Robert Covington||2.4|Forward|
|Jayson Tatum||2.3|Forward|
|Davis Bertans||2.2|Forward|
|Ersan Ilyasova||2.2|Forward|
|David West||2.2|Forward|
|Jrue Holiday||5.1|Guard|
|Dejounte Murray||4.6|Guard|
|Donovan Mitchell||4.5|Guard|
|Yogi Ferrell||4.4|Guard|
|Kyle Korver||4.3|Guard|



**Table 13:** NBA 2018–19 top five plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Kevin Love|6.1|Skilled Big|27 %|
|Jeff Green|5.9|Skilled Big|82 %|
|Brook Lopez|5.9|Skilled Big|45 %|
|Nemanja Bjelica|5.4|Skilled Big|41 %|
|Alex Len|4.7|Skilled Big|35 %|
|Kevin Durant|10.1|Versatile Scorer|66 %|
|James Harden|8.2|Versatile Scorer|32 %|
|Paul George|7.8|Versatile Scorer|68 %|
|Damian Lillard|7.4|Versatile Scorer|55 %|
|Russell Westbrook|7.2|Versatile Scorer|62 %|



> H. Gong and S. Chen: Positional plus-minus **— 213** 

**Table 13:** (continued) 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Eric Gordon|7.4|Secondary Attacker|86 %|
|Gordon Hayward|7.4|Secondary Attacker|47 %|
|Bradley Beal|7.2|Secondary Attacker|26 %|
|Kyle Kuzma|7.2|Secondary Attacker|37 %|
|Malcolm Brogdon|6.8|Secondary Attacker|83 %|
|Mike Conley|7.2|Pick & roll Attacker|47 %|
|Patty Mills|6.7|Pick & roll Attacker|56 %|
|Jamal Murray|6.5|Pick & roll Attacker|30 %|
|Lou Williams|6.4|Pick & roll Attacker|65 %|
|Trae Young|6.1|Pick & roll Attacker|69 %|
|John Collins|5.6|Roll & cut Big|44 %|
|Kevon Looney|4.7|Roll & cut Big|76 %|
|Dwight Powell|4.7|Roll & cut Big|60 %|
|Cody Zeller|4.5|Roll & cut Big|91 %|
|Tristan Thompson|4.5|Roll & cut Big|70 %|
|Stephen Curry|7.1|Movement Shooter|65 %|
|Bojan Bogdanovic|6.1|Movement Shooter|73 %|
|Langston Galloway|5.8|Movement Shooter|56 %|
|Darius Miller|5.3|Movement Shooter|97 %|
|Wesley Matthews|5.3|Movement Shooter|73 %|
|Joel Embiid|8.5|Post-up Big|79 %|
|Paul Millsap|8.3|Post-up Big|44 %|
|Andre Drummond|7|Post-up Big|44 %|
|Al Horford|6.4|Post-up Big|64 %|
|Marc Gasol|6|Post-up Big|76 %|
|Danny Green|7.5|Spot-up Shooter|37 %|
|Danuel House Jr.|7.5|Spot-up Shooter|74 %|
|Davis Bertans|6.4|Spot-up Shooter|67 %|
|Luol Deng|6.2|Spot-up Shooter|53 %|
|Jae Crowder|5.6|Spot-up Shooter|72 %|
|**Player**||**Defensive plus-minus**|**Position**|
|Steven Adams||4.3|Big|
|Rudy Gobert||4.3|Big|
|Ed Davis||4.3|Big|
|Jusuf Nurkic||4.2|Big|
|Willie Cauley-Stein||4.2|Big|
|Paul George||4.1|Forward|
|LeBron James||3.9|Forward|
|Royce O’Neale||3.9|Forward|
|Maxi Kleber||3.7|Forward|
|Giannis Antetokounmpo||3.7|Forward|
|Jrue Holiday||1.9|Guard|
|Danny Green||1.6|Guard|
|Josh Hart||1.3|Guard|
|De’Aaron Fox||1.3|Guard|
|Kyle Lowry||1.3|Guard|



> **214 —** H. Gong and S. Chen: Positional plus-minus 

**Table 14:** NBA 2020–21 top player plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Marcus Morris Sr.|5.5|Skilled Big|38 %|
|Draymond Green|5.2|Skilled Big|41 %|
|DaniloGallinari|4.9|Skilled Big|42 %|
|Paul Reed|4.5|<br>Skilled Big|<br>41 %|
|P. J. Washington|4.4|Skilled Big|91 %|
|Kyrie Irving|9.6|Versatile Scorer|94 %|
|C. J. McCollum<br>|9.4<br>|Versatile Scorer<br>|68 %<br>|
|Jrue Holiday|9.2|Versatile Scorer|83 %|
|Luka Doncic|9|Versatile Scorer|77 %|
|Kawhi Leonard|8.7|Versatile Scorer|79 %|
|Kyle Lowry|5.8|Secondary Attacker|44 %|
|Norman Powell|5.7|Secondary Attacker|58 %|
|Dillon Brooks|5.6|Secondary Attacker|59 %|
|Marcus Smart|5.6|Secondary Attacker|47 %|
|Michael Porter Jr.|5.6|Secondary Attacker|41 %|
|Trae Young|9.5|Pick & roll Attacker|70 %|
|Ja Morant<br>|8.4<br>|Pick & roll Attacker<br>|64 %<br>|
|Zach LaVine|8.2|Pick & roll Attacker|62 %|
|Anfernee Simons|7.9|Pick & roll Attacker|58 %|
|Reggie Jackson|7.4|Pick & roll Attacker|40 %|
|Enes Freedom|5.5|Roll & cut Big|57 %|
|Chris Boucher|4.9|Roll & cut Big<br>|41 %|
|Kevon Looney|4.5|Roll & cut Big|76 %|
|Willy Hernangomez|4.5|Roll & cut Big|84 %|
|Bruce Brown|4.4|Roll & cut Big|29 %|
|Stephen Curry|8.4|Movement Shooter|71 %|
|Bradley Beal|7.9|Movement Shooter|30 %|
|Joe Harris|7.2|Movement Shooter|93 %|
|Buddy Hield|6.2|Movement Shooter|72 %|
|Frank Jackson|6.1|Movement Shooter|98 %|
|Joel Embiid|7.2|Post-up Big|63 %|
|Zion Williamson|6.7|Post-up Big|24 %|
|Nikola Jokic<br>|6.5|Post-up Big|94 %|
|John Collins|5.9|Post-up Big|48 %|
|Karl-Anthony Towns|5.4|Post-up Big|66 %|
|Edmond Sumner|5.4|Spot-up Shooter|37 %|
|Terance Mann|5.1|Spot-up Shooter|44 %|
|Danny Green|5.1|Spot-up Shooter|55 %|
|Juancho Hernangomez|4.9|Spot-up Shooter|64 %|
|Mikal Bridges|4.9|Spot-up Shooter|74 %|
|**Player**||**Defensive plus-minus**|**Position**|
|Rudy Gobert||2.8|Big|
|<br>Mike Muscala||2.7|Big|
|DeMarcus Cousins||2.6|Big|
|Robin Lopez||2.6|Big|
|<br>Jusuf Nurkic||2.6|Big|
|Paul George||2.5|Forward|
|Tobias Harris||2.4|Forward|
|Giannis Antetokounmpo<br>||2.4<br>|Forward<br>|
|Jimmy Butler<br>Kawhi Leonard||2.3<br>2.3|Forward<br>Forward|



> H. Gong and S. Chen: Positional plus-minus **— 215** 

**Table 14:** (continued) 

|**Player**|**Defensive plus-minus**|**Position**|
|---|---|---|
|P. J. Dozier|1.4|Guard|
|Mike Conley|1.1|Guard|
|Garrett Temple|1|Guard|
|Michael Carter-Williams|1|Guard|
|De Andre’Bembry|0.9|Guard|



**Table 15:** NBA 2021–22 top player plus-minus ratings by position. 

|**Player**|**Offensive plus-minus**|**Position**|**Position probability**|
|---|---|---|---|
|Aaron Gordon|5.2|Skilled Big|31 %|
|Karl-Anthony Towns|5.1|Skilled Big|36 %|
|Danilo Gallinari|4.7|Skilled Big|39 %|
|Anthony Gill|4.5|Skilled Big|62 %|
|Jaren Jackson Jr.|4.2|Skilled Big|44 %|
|Jrue Holiday|11.7|Versatile Scorer|94 %|
|Jayson Tatum|9.7|Versatile Scorer|86 %|
|Trae Young|8.3|Versatile Scorer|73 %|
|Shai Gilgeous-Alexander|8.2|Versatile Scorer|63 %|
|Darius Garland|8.2|Versatile Scorer|60 %|
|Gary Trent Jr.|5.7|Secondary Attacker|64 %|
|Dillon Brooks|5.3|Secondary Attacker|37 %|
|Miles Bridges|5.1|Secondary Attacker|51 %|
|<br>Bogdan Bogdanovic|5|<br>Secondary Attacker|47 %|
|Malik Monk|4.9|Secondary Attacker|84 %|
|Tyler Herro|7|Pick & roll Attacker|54 %|
|Cade Cunningham|6.9|Pick & roll Attacker|67 %|
|LaMelo Ball|6.3|Pick & roll Attacker|92 %|
|D’Angelo Russell|6.3|Pick & roll Attacker|87 %|
|Donovan Mitchell|6.2|Pick & roll Attacker|81 %|
|Jakob Poeltl|5.5|Roll & cut Big|90 %|
|Clint Capela|5.4|Roll & cut Big|94 %|
|Isaiah Hartenstein|5.3|Roll & cut Big|97 %|
|Goga Bitadze|5.2|Roll & cut Big|82 %|
|Rudy Gobert|5.2|Roll & cut Big|99 %|
|Stephen Curry|4.9|Movement Shooter|69 %|
|Jordan Poole|4.8|Movement Shooter|55 %|
|Garrison Mathews|4.8|Movement Shooter|63 %|
|Buddy Hield|4.7|Movement Shooter|90 %|
|Max Strus|4.6|Movement Shooter|94 %|
|Nikola Jokic|6|Post-up Big|95 %|
|Joel Embiid|6|Post-up Big|56 %|
|Bam Adebayo|4.5|Post-up Big|60 %|
|Jusuf Nurkic|4.5|Post-up Big|90 %|
|Montrezl Harrell|4.4|Post-up Big|78 %|



> **216 —** H. Gong and S. Chen: Positional plus-minus 

**Table 15:** (continued) 

|**Player**|**Offensive plus-minus**<br>**Position**|**Position probability**|
|---|---|---|
|Mikal Bridges|4.7<br>Spot-up Shooter|74 %|
|Dorian Finney-Smith|4.5<br>Spot-up Shooter|81 %|
|Coby White|4.5<br>Spot-up Shooter|39 %|
|Lauri Markkanen|4.5<br>Spot-up Shooter|57 %|
|Isaac Okoro|4.3<br>Spot-up Shooter|64 %|
|**Player**|**Defensive plus-minus**|**Position**|
|Jusuf Nurkic|3.4|Big|
|Domantas Sabonis|3.3|Big|
|Bam Adebayo|3.3|Big|
|Anthony Davis|3.2|Big|
|Rudy Gobert|3.2|Big|
|Paul George|2.6|Forward|
|Maxi Kleber|2.5|Forward|
|Jayson Tatum|2.5|Forward|
|Pascal Siakam|2.4|Forward|
|Cameron Johnson|2.4|Forward|
|Kenrich Williams|5.1|Guard|
|George Hill|4.6|Guard|
|Andre Iguodala|3.9|Guard|
|Fred Van Vleet|3.7|Guard|
|Derrick White|3.7|Guard|



## **References** 

- Anıl Duman, E., Sennaroğlu, B., and Tuzkaya, G. (2021). A cluster analysis of basketball players for each of the five traditionally defined positions. _Proc. Inst. Mech. Eng. P J. Sports Eng. Technol._ 238: 55−75,. 

- Arthur, D. and Vassilvitskii, S. (2007). _k-means_ ++ _: the advantages of careful seeding_ . Soda, pp. 1027−1035. 

- Baghal, T. (2012). Are the “four factors” indicators of one factor? An application of structural equation modeling methodology to NBA data in prediction of winning percentage. _J. Quant. Anal. Sports_ 8,. 

- Beckler, M., Wang, H., and Papamichael, M. (2013). NBA oracle. _Zuletzt besucht am_ 17. 

- Bezdek, J.C., Ehrlich, R., and Full, W. (1984). FCM: the fuzzy c-means clustering algorithm. _Comput. Geosci._ 10: 191−203,. 

- Brusco, M.J. and Cradit, J.D. (2001). A variable-selection heuristic for K-means clustering. _Psychometrika_ 66: 249−270,. 

- Deshpande, S.K. and Jensen, S.T. (2016). Estimating an NBA player’s impact on his team’s chances of winning. _J. Quant. Anal. Sports_ 12: 51−72,. 

- Engelmann, J. (2011) A new player evaluation technique for players of the National Basketball Association (NBA). In: _Proceedings of the MIT sloan sports analytics conference_ . 

- Engelmann, J. (2017). Possession-based player performance analysis in basketball (adjusted +/− and related concepts). In: _Handbook of statistical methods and analyses in sports_ . Chapman and Hall/CRC, Boca Raton, pp. 231−244. 

- Falk, B. (n.d.). Garbage time, Available at: _<_ https://cleaningtheglass .com/stats/guide/garbage_time _>_ . 

- Fellingham, G.W. (2022). Evaluating the performance of elite level volleyball players. _J. Quant. Anal. Sports_ 18: 15−34,. 

- Franks, A., Miller, A., Bornn, L., and Goldsberry, K. (2015) Counterpoints: advanced defensive metrics for NBA basketball. In: _9th annual MIT sloan sports analytics conference, Boston, MA_ . 

- Franks, A.M., D’Amour, A., Cervone, D., and Bornn, L. (2016). Meta-analytics: tools for understanding the statistical properties of sports metrics. _J. Quant. Anal. Sports_ 12: 151−165,. 

- Grassetti, L., Bellio, R., Di Gaspero, L., Fonseca, G., and Vidoni, P. (2021). An extended regularized adjusted plus-minus analysis for lineup management in basketball using play-by-play data. _IMA J. Manag. Math._ 32: 385−409,. 

- Hvattum, L.M. (2019). A comprehensive review of plus-minus ratings for evaluating individual players in team sports. _Int. J. Comput. Sci. Sport_ 18: 1−23,. 

- Ilardi, S. and Engelmann, J. (2014). The next big-thing: real plus-minus, Available at: _<_ https://www.espn.com/nba/story/_/id/10740818/ introducing-real-plus-minus _>_ . 

- Intraocular (2022). Why APM models should account for position, Available at: _<_ https://www.intraocular.net/posts/accounting-forposition _>_ . 

- Jacobs, J. (2019). Exercising error: quantifying statistical tests under RAPM (Part IV), Available at: _<_ https://squared2020.com/2019/10/03/ exercising-error-quantifying-statistical-tests-under-rapm-partiv/ _>_ . 

- Jensen, S.T., McShane, B.B., and Wyner, A.J. (2009). Hierarchical Bayesian modeling of hitting performance in baseball. _Bayesian Anal._ 4: 631−652,. 

- Macdonald, B. (2011). A regression-based adjusted plus-minus statistic for NHL players. _J. Quant. Anal. Sports_ 7,. 

> H. Gong and S. Chen: Positional plus-minus **— 217** 

- Macdonald, B. (2012). Adjusted plus-minus for NHL players using ridge regression with goals, shots, Fenwick, and Corsi. _J. Quant. Anal. Sports_ 8,. 

- Mallepalle, S., Yurko, R., Pelechrinis, K., and Ventura, S.L. (2020). 

   - Extracting NFL tracking data from images to evaluate quarterbacks and pass defenses. _J. Quant. Anal. Sports_ 16: 95−120,. 

- Matano, F., Richardson, L., Pospisil, T., Politsch, C.A., and Qin, J. (2023). Augmenting adjusted plus-minus in soccer with FIFA ratings. _J. Quant. Anal. Sports_ 19: 43−49,. 

- McBasketball, C. (2017). Nylon Calculus: how to understand synergy play type categories, Available at: _<_ https://fansided.com/2017/09/08/ nylon-calculus-understanding-synergy-play-type-data/ _>_ . 

- Page, G.L., Barney, B.J., and McGuire, A.T. (2013). Effect of position, usage rate, and per game minutes played on NBA player production curves. _J. Quant. Anal. Sports_ 9: 337−345,. 

- Pelechrinis, K. and Papalexakis, E. (2016). The anatomy of American football: evidence from seven years of NFL game data. _PLoS One_ 11: e0168716,. 

- Rosenbaum, T.D. (2004). Measuring how NBA players help their teams win, Available at: _<_ http://www.82games.com/comm30.htm#_ ftn1 _>_ . 

- Sabin, R.P. (2021). Estimating player value in American football using plus−minus models. _J. Quant. Anal. Sports_ 17: 313−364,. 

- Santos-Fernandez, E., Wu, P., and Mengersen, K.L. (2019). Bayesian statistics meets sports: a comprehensive review. _J. Quant. Anal. Sports_ 15: 289−312,. 

- Sill, J. (2010) Improved NBA adjusted +/− using regularization and out-of-sample testing. In: _Proceedings of the 2010 MIT sloan sports analytics conference_ . 

- Snarr, T. (2022). NBA player metric comparison, Available at: _<_ https:// dunksandthrees.com/blog/metric-comparison _>_ . 

- Thomas, A.C., Ventura, S.L., Jensen, S.T., and Ma, S. (2013). Competing process hazard function models for player ratings in ice hockey. _Ann. Appl. Stat._ 7: 1497−1524,. 

- Whitehead, T. (2019). Nylon Calculus: grouping players by offensive role, again, Available at: _<_ https://fansided.com/2019/05/29/nyloncalculus-grouping-players-offensive-role-again/ _>_ . 

- Winston, W.L. (2012). Mathletics. In: _Mathletics_ . Princeton University Press, Princeton. 

- Yurko, R., Ventura, S., and Horowitz, M. (2019). nflWAR: a reproducible method for offensive player evaluation in football. _J. Quant. Anal. Sports_ 15: 163−183,. 


