<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/undated/undated - A Graph Neural Network deep-dive into successful counterattacks - Sahasrabudhe et al.pdf -->

# **A Graph Neural Network deep-dive into successful counterattacks** 

### Soccer Paper ID: 754863 Amod Sahasrabudhe, Joris Bekkers 

## **Abstract** 

<mark>A counterattack in soccer is a high speed, high intensity direct attack that can occur when a team transitions from a defensive state to an attacking state after regaining possession of the ball. The aim is to create a goal-scoring opportunity by covering a lot of ground with minimal passes before the opposing team can recover their defensive shape. The purpose of this research is to build gender-specific, first-of-their-kind Graph Neural Networks to model the likelihood of a</mark> 

<mark>counterattack being successful and uncover what factors make them successful in both men's and women's professional soccer. These models are trained on a total of 20,863 frames of algorithmically identified counterattacking sequences from synchronized StatsPerform on-ball event data and SkillCorner spatiotemporal (broadcast) tracking data. This dataset is derived from 632 games of MLS (2022), NWSL (2022) and international women’s soccer (2020-2022). With this data we demonstrate that gender-specific Graph Neural Networks outperform architecturally identical gender-ambiguous models in predicting the successful outcome of counterattacks.</mark> We show, using Permutation Feature Importance, that byline to byline speed, angle to the goal, angle to the ball and sideline to sideline speed are the node features with the highest impact on model performance. 

Additionally, we offer some illustrative examples on how to navigate the infinite solution search space to aid in identifying improvements for player decision making. 

T <mark>his research is accompanied by a GitHub repository of all data and Python code to allow the reader to replicate and improve upon our research.</mark> 

## **1. Introduction** 

Over the past couple of years, the engagement with the women’s game has increased significantly compared to years prior. The United States 2-0 victory over the Netherlands in the 2019 World Cup final became the most watched Women’s World Cup match ever with an increased viewership of 56% compared to the 2015 final [13]. Live viewers for the 2022 EURO increased by more than 50% compared to 2017 and 214% compared to 2013 [32]. The NWSL reported a 71% increase in viewers for the 2022 Championship final compared to 2021 [22]. Not only did the women’s game make these great strides forward on engagement, but it also did financially. FIFA more than tripled the prize money for the 2019 World Cup to $50 million (from $15 million in 2015) [14]. In 2022 U.S. Soccer, the USWNTPA and the USNSTPA agreed to a collective bargaining agreement that achieved equal pay through identical economic terms for both senior national teams [33]. And the creation of more women’s national competitions has ensured more women can play professionally. This increase in fan engagement and financial opportunity should be followed by an increase in data availability and subsequent data analysis to add additional support for the growth of the women’s game. Unfortunately, existing research into women’s soccer tactical decision-making is still scarce, but researchers have successfully mapped differences between genders in shooting tendencies [7, 24, 35] and [29] used women’s event and freeze-frame positional data to profile 



1 

passing in different competitions. To the best of our knowledge, no research exists to date that leverages tracking data to analyze differences in tactical tendencies between the men’s and women’s game. 

#### **1.1. Research** 

This research is the first of its kind to use a full season of women’s and men’s professional soccer spatiotemporal broadcast tracking data (synced with on-ball event data). We use this data to train gender-specific state-of-the-art binary classification Graph Neural Networks (GNNs) with the aim of predicting the successful outcome of counterattacks. 

<mark>Counterattacks (or attacking transitions) are an important part of soccer strategy, and they play a prominent role in the U.S. Soccer Federation’s internal style of play guide.</mark> 

<mark>In general, a counterattack in soccer can be defined as a high speed, high intensity direct attack that can occur when a team transitions from a defensive state to an attacking state after regaining possession of the ball. The aim is to create a goal-scoring opportunity by covering a lot of ground with minimal passes before the opposing team can recover their defensive shape [23].</mark> 

<mark>As per our algorithm described in Section 2, 7.5% of all shots attempted came from a counterattack in the 2022 MLS season. These counterattacking shots lead to 9.7% of goals scored. Similarly, in the 2022 NWSL season 6.2% of total shots came from counterattacks. These shots lead to 9.5% of all goals scored during that season.</mark> 

#### **1.2. Graphs** 

<mark>Graph Neural Networks rely on graph representations of frames of soccer data to capture the relevant information within it.</mark> In graph theory, a graph consists of a set of points (nodes) linked together by lines (edges). Historically, on-ball event data has been used to analyze _The Beautiful Game_ with such graphs by describing team, match and/or season aggregate information to represent players as the nodes of the graph and passes as the edges between these nodes, because the on-ball event data does not contain information of players off the ball. Researchers have used these graph representations of soccer to describe games in the form of pass networks [4, 21], create adjacency matrices of all passes in a team to calculate the importance of players in a pass network [8] and flow motifs to identify unique playing styles from passing behavior of teams and players [6, 17, 25]. 

With the advent of (broadcast) tracking data – consisting of x, y coordinates of all players and the ball at 10 or 25 frames per second – it becomes possible to represent individual frames of tracking data with a similar graph representation. In these graphs, the players are still the nodes, but the edges now simply describe the relationship between all players on the pitch during a particular frame. Figure 1 depicts a schematic, stylized representation of two teams (red and blue) connected to all their teammates and to the opposing team through the ball (in the center). 

Most contemporary research that leverages neural networks in soccer use a range of different image representations of the player and ball coordinates [3, 11, 30] to communicate the information in a frame of soccer data to the neural network, because conventional convolutional neural networks are built to process images, not graphs. Starting only a few years ago, when GNNs started to become more mainstream due to their integration within machine learning packages [12, 16, 18], did we see researchers try their hand at representing on-ball event data [19] and coordinate tracking data [15, 31, 36] as graphs. 



2 



_Figure 1: Schematic stylized graph representation of a single frame of tracking data_ 

Representing frames of tracking data as graphs allows us to not only incorporate the position of the players, but it makes it considerably simpler to add information to each node of the graph about a player’s speed, acceleration, distance to goal or even their preferred shoe color if we thought that mattered. Similarly, the edge features of the graph contain information on the connections between players, such as the inter-player distances or the inter-player angles. 

The ability to add this level of granular detail to the models allows us to manage the issues raised in [30] such as incomplete frames and games with less than 22 players on the pitch (due to red cards, injuries, or data inconsistencies etc.). Because we do not have to convert the set of coordinates to an image (and thereby losing valuable and interpretable information), and because we can include more detail into each graph, we can get a better understanding of which features have an impact on the model performance. 

## **2. Methodology** 

In this research we build different GNNs on three datasets (a women’s dataset, a men’s dataset, and a combined dataset) with the aim of predicting the outcome (successful or unsuccessful) of sequences of play considered a counterattack according to a rules-based algorithm. Subsequently, we use the different models built with these datasets to learn more about the differences between the men’s and women’s game by calculating the impact each of the individual features has on the model accuracy. Finally, we dive more deeply into some example situations to see what situationally dependent adjustments players could have made to improve their chances of successfully completing a counterattack according to our models. 

To accomplish this, we use synchronized StatsPerform on-ball event data, and SkillCorner broadcast spatiotemporal (10Hz) tracking data of a total of 632 recent games from the National Women’s Soccer League, International Women’s Friendlies, SheBelieves Cup, Olympic Women’s Tournament and Major League Soccer. 

Due to the nature of broadcast tracking data some players will periodically be out of view of the camera. Even though GNNs can deal with different amounts of players in different graphs we use SkillCorner’s predicted coordinates for these out-of-view players to be able to have 22 players in most frames.  We ensure the models are built on good quality data by only using games that have a SkillCorner player and ball quality ratings of 4 out of 5 or above. 

To build a Graph Neural Network model to predict the successful outcome of counterattacks requires us to first identify phases of play that can be labeled as part of a counterattack in both the men’s and women’s game. Because [2] has shown us how manually labeling specific situations in soccer can be a time intensive task, we have opted to algorithmically identify counterattacks and subsequently label them successful or unsuccessful using a set of on-ball event driven rules 



3 

comprised and verified in collaboration with USWNT and USMNT Performance Analysts, and in accordance with the U.S. Soccer Federation’s internal style of play guide. 

Though the exact set of rules can be found in the Appendix, it is important to note – due to the limited number of goal attempts in our dataset – we consider a successful counterattack to end with the attacking team moving the ball in the opposing team’s penalty area, either via a successful onball run, or by receiving the ball in the box successfully. 

The algorithmic approach yields a set of sequences of on-ball events considered to be a counterattack. We use this set of sequences to label all individual frames of SkillCorner broadcast tracking data as part of a successful counterattack (1) or part of an unsuccessful counterattack (0) and we omit all frames not considered part of a counterattack. 

This means that our model only uses individual frames (without timeseries components), and each frame is labeled with the future outcome (successful or unsuccessful) of the sequence within which it lies. 

In the on-ball event data model VAEP (Valuing Actions by Estimating Probabilities) [9] a similar forward-looking labeling technique is used, but instead each on-ball action is annotated when a goal is scored or conceded within 10 actions from the current action. 

#### **2.1. Model Architecture** 

The individual raw tracking data frames are converted into a graph representation to train the GNNs with the Python library _Spektral_ [16]. The graph representation consists of individual matrices with node features, edge features and an adjacency matrix for each frame. The node features are comprised of normalized player’s coordinates, velocity, angle of motion, distance to goal, angle to goal, distance to the ball, angle to the ball and an attacking team flag. The edge features consist of inter-player angles (in the form of a sine and cosine value) and normalized interplayer distances. Within the adjacency matrix players from the same team are connected to each other and every player is connected to the ball node, as shown in Figure 1. 

Figure 2 depicts the GNN model architecture. It contains three CrystalConv layers [37] (a method originally built to predict crystalline properties using connections of atoms) to directly learn game state properties from the connections between players in each graph, a Global Average Pool layer, a Dense layer with ReLu activation, a Dropout layer and ultimately a Sigmoid activation function. 



_Figure 2: GNN model architecture_ 



4 

#### **2.2. Dataset** 

The GNNs are trained on a balanced training set (consisting of 70% of samples) containing 50% successful, and 50% unsuccessful counterattacks. One model is trained on only women’s data, one on only men’s data and one combined model trained using all men and women’s data. Due to the lower number of samples available for the women’s data (due to fewer games), the models trained using the women’s data are trained on 100 epochs whereas the other models are trained on 200 epochs. Table 1 describes the data used for training these models. 

_Table 1: Data breakdown_ 

||**Women**|**Men**|**Combined**|
|---|---|---|---|
|**Competitions**|NWSL<br>International Friendlies<br>SheBelieves Cup<br>Olympics Tournament|MLS|NWSL<br>International Friendlies (W)<br>SheBelieves Cup<br>Olympic Tournament (W)<br>MLS|
|**Games**|157|475|632|
|**Counterattacks**|942|3782|4727|
|**Counterattack frames**|3720|17143|20863|



#### **2.3. Open source** 

<mark>In the interest of expanding the research conducted using women’s spatiotemporal data, to give others an opportunity to build on top of our models and more importantly to try to improve them, we have made both t</mark> he dataset (in its anonymized graph representation form as used in this research), and an interactive Python Jupyter Notebook used to train our models available for download on the U.S. Soccer Federation’s Official GitHub page [34]. 

We encourage readers to try to improve our models’ results by including different node and edge features and by trying out different types of adjacency matrices (all of which have been included in the downloadable datasets) in addition to examining different model architectures. 

## **3. Results** 

<mark>To evaluate our model performance, we compare the gender-specific models to a naïve baseline model that assumes a 50/50 class split (resulting in a naïve Log-Loss of 0.693 and an ROC-AUC of 0.50) and we compare it to the model trained on the combined dataset.</mark> 

<mark>Table 2 shows the Log-Loss and ROC-AUC scores for the naïve model, the combined model, and the gender-specific models. The lower Log-Loss and the higher ROC-AUC scores for the gender-specific models indicate that it pays to train gender-specific models to improve model performance, and it can achieve this with a significantly smaller sample size (as shown in Table 1).</mark> 

<mark>The seemingly high Log-Loss for all models can, for the most part, be attributed to the predictions made on frames where play is concentrated in the center of the pitch. In this area, predictions</mark> 



5 

<mark>mostly lie within the 40-60% success range, meaning that we are essentially trying to predict the outcome of a coin-flip. With this in mind, we do believe that even though our model architecture can most likely be improved, our models already performed well given the difficulty of the prediction problem.</mark> 

_Table 2: Model performance metrics_ 

||**Women**|**Men**|**Combined**|**Naive**|
|---|---|---|---|---|
|**Testing**<br>**Log Loss**|0.48|0.51|0.56|0.69|
|**ROC-AUC**|0.83|0.78|0.76|0.50|



#### **3.1. Model Calibration** 

<mark>Due to the pseudo-probabilistic nature of the predictions, they can only aid in our understanding of the game if they are well-calibrated. We can measure the calibration by calculating the Expected Calibration Error (ECE). The ECE gives a weighted average over the difference between the absolute accuracy and the confidence, calculated per probability bin. T</mark> he ECE values for the men’s and women’s model are 0.15 and 0.18 respectively. 

<mark>The Calibration Curves (displayed in Figure 3)</mark> represent the distribution of the predicted probabilities for the men’s model and women’s model. 

The ECE values and the Calibrations curves clearly indicated that our models are indeed well calibrated. 



_Figure 3: CrystalConv model calibration curves_ 

#### **3.2. Feature Importance** 

<mark>The increased model performance in both the men and women’s model compared to the combined model indicates that these gender-specific models must weigh their respective model’s features differently to achieve these improved results. We use Permutation Feature Importance [1] to calculate the feature importance within both gender’s models to uncover where these differences lie. Permutation Feature Importance allows us to identify the importance of each individual feature</mark> 



6 



_Figure 4: Attacking and Defending Feature Importance for the Women’s and Men’s model._ 



7 

<mark>by measuring the increase in prediction error when breaking the relationship between individual features and the observed result through the application of a random permutation to the feature’s values. In other words, we use the test set to randomly shuffle the values for one feature and recalculate the model error [20]. Next, we return those shuffled values to their true state and repeat the process for every other feature individually.</mark> 

<mark>Applying multiple independent random shuffles and calculating the model’s error for each individual shuffle allows us to analyze both the average and the spread of the acquired model errors for each feature.</mark> 

<mark>The feature importance is measured by subtracting the AUC obtained after randomly shuffling the values for a feature from the AUC of the actual model.</mark> 

<mark>In Figure 4 we show the results of applying this Permutation Feature Importance random shuffle to each of the 10 node features 15 times, both for the attacking players (on the left) and for the defending players (on the right) for both gender-specific models. Because it is impossible to shuffle the edge features without completely breaking the logic of the individual graphs, we have left those out of the scope of this feature importance analysis.</mark> 

<mark>In Figure 4 we see that the x-component of the velocity vector (in other words, the players’ speed from byline to byline) and the players’ angle to the goal are the two features with the highest impact on our model’s performance. The ball angle between each player and the ball, the y- component of the velocity vector (sideline to sideline speed) and each player’s distance to the ball are also relatively important. Finally, we see how the x and y coordinates, the speed and the direction of movement are the least impactful. This can be partially attributed to the fact that these values are highly correlated with the distance and angle to the goal, and the components of the velocity vector respectively. Finally, notice how the defending team’s features are more important to the model’s performance than the attacking players features. This could be because, by definition, a counterattack exists solely during a phase of disorganized defending.</mark> 

## **4. Application** 

The impact of the differences between these gender-specific models on an aggregated node feature level is challenging to translate into actionable insights from a figure like Figure 4, nor are they easily understood (at this time) by visually inspecting frames and comparing the differences to their respective counterattack success probability like in Figure 5 and 6. More research is needed to translate the information from Figure 4 into actionable insights, and to connect that knowledge into a direct understanding of the probabilistic differences between Figure 5 and 6. 

The importance of these gender-specific models at the time of writing lies in the opportunity to offer a Women’s team’s coaching staff the ability to interact with a model that is trained specifically on women’s data, because currently most, if not all, models are trained primarily on men’s data. It is therefore better suited to offer input for analysis and visual inspection of sequences of play relevant to the women’s game. 



8 



_Figure 5: An example prediction with the Women’s model. The blue team is attacking from left to right._ 



_Figure 6: An example prediction with the Men’s model. The blue team is attacking from left to right._ 

#### **4.1. An infinite search space** 

The models created for this research can be highly valuable when they are built into an interactive tool such as [5]. Tools like this allow coaches, technical staff, analytics staff, and players alike to interactively navigate the infinite optimization search space of individual frames or even specific sequences of play. This can help them to find small improvements or novel solutions for their tactical approaches and their positioning and movement decisions, both from an attacking and a defending perspective. 

Figure 7 shows an example of a search for an improved attacking run during a counterattack. To offer some additional visual guidance we have reinforced the figure with a Pitch Control model [27]. To find this improvement (and the improvements shown in Figure 8, 9, 10 and 11) we have changed the highlighted player’s movement direction by increments of 15° to uncover a potentially improved run trajectory. Finding these improvements in practice could be accomplished with a computer-assisted interactive search tool. 



_Figure 7: An improved run trajectory for the right winger. The faint arrow represents the original trajectory of the player. Pitch control added for visual guidance only._ 



_Figure 8: An improved run trajectory for the left winger. The faint arrow represents the original trajectory of the player. Pitch control added for visual guidance only._ 

When the right winger’s trajectory in Figure 7 is rotated by 30° to the inside the probability of successfully completing this counterattack increases by 1.8 percentage points. 



9 

Using the same frame again in Figure 8 but now rotating the left winger’s trajectory outwards by 30° increases the prediction by 2 percentage points. In this case, running away from the direction of the defensive player, and running into a channel with more space, increases the likelihood of a successful counterattack. Figure 9 shows how both improvements simultaneously can help increase the success probability by 3.8 percentage points. 



_Figure 9: An improved run trajectory for both the right winger and left winger. The faint arrow represents the original trajectory of the player. Pitch control added for visual guidance only._ 

In the next on-ball action, the right winger has taken control of the ball. The left winger can now choose to position more centrally as shown in Figure 10. This results in the model prediction dropping down by 1.4 percentage points, because that run is directed towards a part of the pitch which would be dominated by the opposition team. 

On the other hand, a run in the wide channel as depicted in Figure 11, will lead to the highlighted player occupying more open space. This leads to an increase of 1.4 percentage points in the probability of successfully completing the counterattack. 



_Figure 10: A worse run trajectory for the left winger. The faint arrow represents the original trajectory of the player. Pitch control added for visual guidance only._ 



_Figure 11: An improved run trajectory for the left winger. The faint arrow represents the original trajectory of the player. Pitch control added for visual guidance only._ 



10 

In addition to searching for these run optimizations, these models can be used to evaluate both player and team performance in counterattacks, to uncover players that help reduce their team’s likelihood of conceding a successful counterattack, or player that can improve their team’s chance of completing a successful counterattack via their positioning or their run selection. 

## **5. Discussion** 

Within this research we have built and open-sourced two gender-specific Graph Neural Network models to predict the outcome of counterattacks, leveraging individual frames of spatiotemporal tracking data by algorithmically assigning labels to them from on-ball event data. In comparison to Expected Possession Value (EPV) models [10] build using conventional convolutional neural networks, our GNN models can incorporate more features, such as speed and direction of motion. A major difference between this EPV model and our models is the use of the penalty area as the target for successfully completing a counterattack. We would have preferred to use (expected) goals (or goal attempts) as the successful end-product; however, we did not have enough samples to satisfy this preference. This means that, for example, the improvements found in section 5.1 will help us control the ball inside the box, but they might also reduce the chance of scoring a goal. 

In contrast to on-ball event data-based models, our implementation allows us to value each individual player’s contribution, both on and off the ball, primarily due to the nature of the spatiotemporal data. But, contrary to VAEP it does not evaluate the risk of conceding a new counterattack for the current attacking team. Our output is simply an assessment of the threat going forward, like Expected Threat [26]. 

Additionally, we need to acknowledge that even though we attempted to reduce the risk of overfitting (especially on the smaller women’s dataset) by reducing the number of epochs during training this research certainly lacks a thorough validation of the model performance. 

Furthermore, we need to accept that the use of an on-ball event-based algorithm to identify counterattacks is not a perfect solution. However, we feel that manually annotating counterattacks for both genders is perhaps even more prone to introducing biases into the training sample. 

To extend this work we would like to conduct more research on the interpretation of the feature importances, and how they can be narrowed down further into actionable insights. Supplementing our approach with a model that predicts the likelihood of a counterattack starting given all the players’ positioning, speed and directionality values could help us streamline the model’s usage. 

Unfortunately, after finalizing this research we became aware of [28]. This Expected Goals research conducted by StatsBomb describes a gender-aware approach.  In this third option – gender-specific and a simple combined setup being the other two – a feature is added to their tabular data to indicate the gender of the player taking the shot. Even though this seems obvious in hindsight, due to the non-tabular nature of our GNN datasets, it was not immediately evident to us to attempt to add such a variable at the time of conducting our research. As a result, we suggest future gendered GNN research incorporated a female/male variable (as a node features) to uncover if this makes a difference. 

Finally, to facilitate more public research into gendered counterattacking GNNs we have released an additional (imbalanced) Graph dataset on GitHub [34]. This dataset consists of 210,000 frames belonging to counterattacking phases of play split equally between women and men. Approximately 



11 

5% of frames in this dataset are labeled a success as they belong to counterattacks that lead to a goal. 

## **6. Conclusion** 

<mark>We have demonstrated that it is possible to build gender-specific Graph Neural Network models that outperform gender-ambiguous models in predicting the successful outcome of counterattacks while relying on a significantly smaller sample size (especially for the Women’s model)</mark> . With the help of Permutation Feature Importance, we have shown that byline to byline speed and angle to the goal have the biggest impact on model performance for both genders, in attack and defense. Using the same technique, we have also uncovered that the defending players’ node features have more impact on model performance than of their attacking counterparts. To better understand these implications, we propose an interactive tool to help navigate the infinite movement, speed, and positioning search space to aid players and coaching staff in finding small improvements or novel solutions for their tactical approaches and their positioning and movement decisions, both from an attacking and a defending perspective. Finally, we challenge the reader to improve our model architecture and the choices we have made for the node and edge features, by using the models and data provided in the U.S. Soccer GitHub repository. 



12 

## **References** 

[1] Altmann, A., Toloşi, L., Sander, O., & Lengauer, T. (2010). Permutation importance: a corrected feature importance measure. Bioinformatics, 26(10), 1340-1347. 

[2] Bauer, P., & Anzer, G. (2021). Data-driven detection of counterpressing in professional football. Data Mining and Knowledge Discovery, 35(5), 2009-2049. 

[3] Bauer, P., Anzer, G., & Shaw, L. (2021). Putting Team Formations in Association Football into Context. [4] Bekkers, J. (2017, July 10). Pass Maps 2.0. https://unravelsports.github.io/2017/07/10/passmaps-v2.html [5] Bekkers, J. (2022, March 6). Interactive Digital Tactics Board. https://unravelsports.github.io/2022/03/06/tactics-board.html [6] Bekkers, J., & Dabadghao, S. (2019). Flow motifs in soccer: What can passing behavior tell us?. Journal of Sports Analytics, 5(4), 299-311. 

[7] Bransen, L., & Davis, J. (2021). Women’s football analyzed: interpretable expected goals models for women. In _AI for Sports Analytics (AISA) Workshop at IJCAI 2021_ . 

[8] Clemente, F. M., Couceiro, M. S., Martins, F. M. L., & Mendes, R. S. (2015). Using network metrics in soccer: a macro-analysis. Journal of human kinetics, 45, 123. 

[9] Decroos, T., Bransen, L., Van Haaren, J., & Davis, J. (2020). VAEP: an objective approach to valuing on-the-ball actions in soccer. In Proceedings of the twenty-ninth international joint conference on artificial intelligence, IJCAI-20 (pp. 4696-4700). International Joint Conferences on Artificial Intelligence Organization. [10] Fernández de la Rosa, J. (2022). A framework for the analytical and visual interpretation of complex spatiotemporal dynamics in soccer. [11] Fernández, J., & Bornn, L. (2020, September). Soccermap: A deep learning architecture for visually interpretable analysis in soccer. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (pp. 491-506). Springer, Cham. [12] Fey, M., & Lenssen, J. E. (2019). Fast graph representation learning with PyTorch Geometric. arXiv preprint arXiv:1903.02428. 

[13] FIFA. (2019, October 18). FIFA Women’s World Cup 2019™ watched by more than 1 billion. https://www.fifa.com/tournaments/womens/womensworldcup/france2019/news/fifa-women-sworld-cup-2019tm-watched-by-more-than-1-billion 

[14] FIFA. (2019, October 26). FIFA Council makes key decisions for the future of football development. https://www.fifa.com/about-fifa/organisation/fifa-council/media-releases/fifacouncil-makes-key-decisions-for-the-future-of-football-development 

[15] Friend of Tracking. (2021, April 29). _Paul Power: neural networks for understanding defending_ [Video]. YouTube. https://www.youtube.com/watch?v=d5NBm4CFygo 

[16] Grattarola, D., & Alippi, C. (2021). Graph neural networks in TensorFlow and keras with Spektral. IEEE Computational Intelligence Magazine, 16(1), 99-106. 

[17] Gyarmati, L., Kwak, H., & Rodriguez, P. (2014). Searching for a unique style in soccer. arXiv preprint arXiv:1409.0308. 

[18] Hu, W., Fey, M., Zitnik, M., Dong, Y., Ren, H., Liu, B., … & Leskovec, J. (2020). Open graph benchmark: Datasets for machine learning on graphs. Advances in neural information processing systems, 33, 22118-22133. 

[19] Minogue, P. (2022, June 4). An introduction to graph neural networks: Classifying soccer player positions from passing networks _._ https://paulminogue.com/posts/375ea85d-fc58-4c13-a9dc5a45ba3c368f 



13 

[20] Molnar, C. (2022, November 12). Interpretable Machine Learning: A guide for making black box models explainable. https://christophm.github.io/interpretable-ml-book/featureimportance.html 

[21] Mullenberg, J. (2017, March 9). The sense and nonsense of a passmap. https://www.tussendelinies.nl/the-sense-and-nonsense-of-a-passmap/ 

[22] National Women’s Soccer League [@NWSL]. (2022, November 1). _Those are some numbers The 2022 #NWSL Championship drew in 915,000 viewers Saturday, a +71% jump from last_ [Image Attached] [Tweet]. Twitter. https://twitter.com/NWSL/status/1587449315361886209 [23] Osmanbašić, A. (2020, April 1). The Evolution of Counterattacking. https://spielverlagerung.com/2020/04/01/the-evolution-of-counterattacking/ 

[24] Pappalardo, L., Rossi, A., Natilli, M., & Cintia, P. (2021). Explaining the difference between men’s and women’s football. PloS one, 16(8), e0255407. 

[25] Pena, J. L., & Touchette, H. (2012). A network theory analysis of football strategies. arXiv preprint arXiv:1206.6904. 

[26] Singh, K. (2018, December 24). Introducing Expected Threat (xT). https://karun.in/blog/expected-threat.html 

[27] Spearman, W., Basye, A., Dick, G., Hotovy, R., & Pop, P. (2017, March). Physics-based modeling of pass probabilities in soccer. In Proceeding of the 11th MIT Sloan Sports Analytics Conference. [28] StatsBomb. (2022, November 9) Analytics And Modelling In Women’s Football. https://statsbomb.com/articles/soccer/analytics-and-modelling-in-womens-football/ [29] StatsBomb. (2022, October 3) _StatsBomb Conference 2022: Dr. Will Morgan_ [Video]. YouTube. https://www.youtube.com/watch?v=RG6_eisU-0M 

[30] Stats Perform. (2020, March 18). _OptaProAnalyticsForum– Learning to watch football: Selfsupervised representations for tracking data_ [Video]. YouTube. https://youtu.be/H1iho17lnoI?t=1508 

[31] Stöckl, M., Seidl, T., Marley, D., & Power, P. (2021). Making offensive play predictable using a graph convolutional network to understand defensive performance in soccer. In Proceedings of the 15<sup>th</sup> MIT Sloan Sports Analytics Conference (Vol. 2022). 

[32] UEFA. (2022, August 31). Women’s EURO watched by over 365 million people globally. https://www.uefa.com/insideuefa/news/0278-15ff73f066e1-c729b5099cbb-1000--365-millionpeople-watch-euro-2022/ 

[33] U.S. Soccer Federation. (2022, August 26). U.S. Soccer, USWNTPA, and USNSTPA will officially sign historic new collective bargaining agreements on the field post-game following the USA vs Nigeria match in Washington D.C. https://www.ussoccer.com/stories/2022/08/us-socceruswntpa-usnstpa-to-officially-sign-historic-cbas-following-uswnt-vs-nigeria-in-dc [34] U.S. Soccer Federation. (2022, November 21). Gender-specific Counterattack GNNs. https://github.com/USSoccerFederation/ussf_ssac_23_soccer_gnn 

[35] Worville, T. (2020, April 19). Explained: How different are men’s and women’s football? https://theathletic.com/1756375/2020/04/20/womens-vs-mens-football-the-trends/ [36] Xenopoulos, P., & Silva, C. (2021, December). Graph Neural Networks to Predict Sports Outcomes. In 2021 IEEE International Conference on Big Data (Big Data) (pp. 1757-1763). IEEE. [37] Xie, T., & Grossman, J. C. (2018). Crystal graph convolutional neural networks for an accurate and interpretable prediction of material properties. Physical review letters, 120(14), 145301. 



14 

## **Appendix** 

#### **Labeling Algorithm** 

To assign labels to every instance of the dataset we use sequence of on-ball event data to identify a successful or unsuccessful counterattack. Before identifying whether a counterattack is successful or not, it is crucial to identify counterattacks in the first place. To identify counterattacks, we use a system that applies the following rules: 

- Starting point of the sequence is in the defensive half of the pitch 

- The sequence of events does not contain a set piece (such as freekick, corner, throw-in, etc.) 

- The ball moves at least 10 meters forward 

- The ball travels with a forward velocity of at least 4 m/s. 

The following rules are used for labelling the counterattack as successful: 

- The ball enters the 18-yard penalty box 

- The coordinates from where the last event in the sequence occurs should be within the defined ellipse as shown in Figure A. 



_Figure A: Coordinates of the last sequence of the frame should be within this elliptical shape._ 

The set of algorithmic rules are built and verified (using video) in collaboration with Performance Analysts from USWNT and USMNT. 



15 


