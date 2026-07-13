<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2023/2023 - An Analysis of the Influence of Game Context on Team Playing Style - Unknown Authors.pdf -->



# **An Analysis of the Influence of Game Context on Team Playing Style** 

Deniz Can Oruç, Lorenzo Cascioli, Luca Stradiotti, Maaike Van Roy, Pieter Robberechts, and Jesse Davis 

KU Leuven, Dept. of Computer Science; Leuven.AI, B�3000 Leuven, Belgium 

## **Introduction** 

Preparing for a soccer match requires an extensive analysis of the opposing team’s playing style, tendencies and tactics. Such analysis enables coaches and analysts to formulate well-informed game plans and tactical adjustments, aiming to exploit the opponent's weaknesses and capitalize on their strengths. Previous studies have therefore explored techniques to measure various offensive and defensive factors that delineate a team’s playing style such as ball possession �1�, passing tendencies �2�, pressing behavior �3�, team formations �4�, attacking patterns �5�, etc. 

However, contextual variables such as match venue, opposition strength and game state were previously found to be associated with changes in teams’ dynamics within and between matches �6���10�. Typically, methods for tactical analysis do not take these contextual variables into account and aggregate the analysis over an entire game or season �11�, �12�. Alternatively, they perform separate analyses for small epochs of a game �13�, which reduces sample sizes. Our research aims to provide a broader perspective and more comprehensive understanding of the influence of game context on a team’s tactical behaviors, decision-making, and overall effectiveness by integrating contextual variables in the analysis. 

Specifically, in this study, we will analyze the effect of the game state (i.e., time remaining, scoreline and venue) on the passing decisions that players make in soccer. Here, passing decisions serve as a proxy towards team style and, more pertinently, how that style changes depending upon the game state. Indeed, previous research has shown that losing or drawing teams prefer a direct playing style (characterized by instances of play where teams attempt to move the ball quickly toward the opposition’s goal through the use of riskier direct or long passes), whereas winning teams prefer shorter passing sequences �14���16�. 

Nonetheless, these analyses offer only a limited breakdown of pass types and the specific phase of play in which they are executed. We hypothesize that the situational context manifests itself differently across different phases of play (e.g., build-up vs. final third) and in terms of the types of pass options available to a player (e.g., opportunities 

**1** 



for through balls vs. crosses). Therefore, a more detailed framework should be provided for analyzing context-dependent styles of play. 

Our approach is two-fold. First, we extend the SoccerMap architecture �17�by introducing limited game state information into the model training process. This game state information is reshaped into surfaces, which are used as additional channels for the prediction architecture. The spatial dissimilarity of the predicted passing distribution across different game states provides an interpretable visualization of how game state affects passing tendencies in specific situations. Second, we propose an encoder-decoder architecture for isolating the effect of game state factors on a player’s pass decision. The resulting latent space represents the learned relationship between game state factors and pass decisions, providing insights into how teams are expected to react to specific game state changes. 

The main contributions of this work are the following: 

1. We show how the SoccerMap architecture can be modified to predict passing tendencies in a given situational context. 

2. We present an encoder-decoder architecture that can generate a compact embedding for describing how a player’s pass selection decision was affected by the situational context. 

3. We show how these embeddings can be used to get a better insight into a team’s playing style and how they tend to vary their game plan based on the situational context. 

## **Modeling the Passing Dynamics of a Soccer Team** 

In this paper, we are interested in the problem of automatically inferring how a team adjusts its in-possession playing style to the game context. Our approach hinges on analyzing passing dynamics as a proxy for a team's in-possession playing style. Indeed, the typical passing choices made by players on a team are closely linked to the team's playing style. For example, the preference for short, quick passes over long, probing ones can provide insights into whether a team prefers a possession-based strategy or a more direct, counter-attacking approach. Similarly, the distribution of passes between wide and central areas of the pitch can reveal the extent to which a team exploits the flanks or opts for a more centrally-focused buildup. 

In this section, we explain how a team’s passing dynamics and the game context can be modeled independently based on tactical event stream data. Then, in the next sections, we discuss two complementary approaches for integrating the analysis of passing dynamics and game context. 

**2** 



### **Data Description** 

This work uses StatsBomb 360 tactical event stream data. In this type of data, each match is described by the regular human-annotated event stream data, augmented with partial spatial context extracted from broadcast video. Namely, each event comes with a snapshot providing the location and relationship to the ball carrier (i.e., teammate or opponent) of all the players appearing in the broadcast video at the time of the event. The annotated events include passes, dribbles and shots observed during the match. Each event is characterized by its time of occurrence in the match, the origin and destination location, the player executing the action, the outcome of the action, and the body part used to execute the action. We convert the original event stream to its SPADL representation �18�. 

We focus exclusively on passes to analyze teams’ playing styles. Additionally, we filter out passes not performed by foot, passes from dead-ball situations (i.e., corners, free-kicks, goal-kicks, kick-offs, and throw-ins), and passes for which the origin or destination location falls outside the visible area of the 360 snapshot. 

Applying the aforementioned filters, we construct a training dataset comprising 162,991 passes from the 2021/22 Premier League, and 164,423 passes from the 2022/23 Premier League. These two datasets only contain games involving a team that finished in the top-10 of the league in the considered season. Additionally, a dataset of 19,544 passes extracted from EURO2020 data has been set aside for the purpose of evaluating the models and developing the use cases. 

### **Modeling Passing Dynamics** 

Setting aside individual player decision-making tendencies and team-specific tactics, we posit that passing dynamics in soccer are primarily shaped by two key factors: 

1. **Phase of play** : This encompasses distinctions such as build-up play versus chance creation, which is closely tied to the location of the ball. 

2. **Available passing options** : This involves assessing opportunities for various types of passes, such as through balls or crosses, and is intricately linked to the positioning of other players on the field. 

Existing pass selection models use the ball’s location and possible passing options to predict the destination �17�or recipient �19�, �20�of a pass. Consequently, these models effectively capture the passing dynamics of a generic team in a generic match context. 

We use the SoccerMap model �17�, which is a modern deep convolutional neural network architecture specifically designed to analyze spatiotemporal data in soccer. As the input of the architecture, we use a 9-channel spatiotemporal representation constructed from the 360 snapshot of the relevant pass and its two preceding actions �21�: 

**3** 



1. Sparse matrix with locations of the attacking team. 

2. Sparse matrix with locations of the defending team. 

3. Dense matrix with distance to the ball for every location. 

4. Dense matrix with distance to the goal of the defending team for every location. 5. Dense matrix with the sine of the angle between every location and the ball. 

6. Dense matrix with the cosine of the angle between every location and the ball. 7. Dense matrix between every location and the goal. 

8. Matrix with the x component of the velocity vector of the ball, derived from the timestamps and ball location in the event data during the two preceding actions 

9. The same matrix with the y component of the velocity vector. 

These channels are processed by convolutional layers that create a feature hierarchy with scales of 1x, 1/2x, and 1/4x �Figure 1�. These different scaled spatial-aware features are upsampled nonlinearly and merged using fusion layers. Finally, a sigmoid activation layer model estimates the probability of passing to each position on the pitch. The model is trained using the log-loss. The cell corresponding to the destination of the pass is selected by multiplying the probability surface with a binary masked matrix. 



**Figure 1.** We use the SoccerMap deep learning architecture to predict the likelihood of each possible pass. The game state is represented as a tensor in which each channel contains low-level information extracted from the 360 snapshot. Through a combination of convolutional layers at different resolutions, the network can capture relevant information at both local and global levels, producing location-wise predictions that are spatially aware. Figure taken from �17�. 

**4** 



### **Game State Factors** 

We analyze three factors that affect team dynamics during a soccer match. In the following, we refer to these three factors as game state factors. 

1. **Venue** . Teams often adapt their playing style based on whether they are playing at home or away. When playing in the comfort of their home stadium, teams frequently exhibit a more assertive and attacking style of play. Conversely, when facing an away fixture, teams often adopt a more cautious and strategic approach �22�. 

   - We encode the venue as a binary variable, indicating whether the team in possession plays at home or away. 

2. **Scoreline** . The scoreline of the match plays a role in shaping teams’ risk-aversive behavior. When a team is losing a game, they may take more risks to create scoring opportunities. On the other hand, when a team is winning, they often become more focused on defending their lead. Teams tend to prioritize maintaining their advantage, often adopting a "parking the bus" strategy to ensure defensive solidity �23�. 

   - We categorize the scoreline into six distinct groups: ��3, �2, �1, draw, �1, �2, �3. 

3. **Time remaining** . The remaining time on the clock also affects teams’ dynamics. When time is running out, teams may adopt a more aggressive and direct style of play. They might employ tactics such as quick counters, long balls, and all-out attacks in an attempt to score goals rapidly. Conversely, if a team holds a comfortable lead late in the match, they may prioritize ball retention and time-wasting strategies to run down the clock and protect their advantage �24�. We represent the remaining time as a discrete variable by dividing the game into quarters and subdividing the last quarter into 5-minute intervals. 

We use a one-hot encoding to represent these three game state factors as a 16-dimensional vector �1 bit indicating whether the in-possession team plays at home or away, 7 bits for the scoreline, and 8 bits for the time remaining). 

## **Predicting how the game state will impact a specific pass decision** 

SoccerMap �17�provides us with a powerful tool for conducting a fine-grained analysis of generic passing tendencies in various game situations. However, a team strongly adapts its passing tendencies, depending upon the game state and the team’s corresponding objectives. Unfortunately, the original SoccerMap architecture lacks the capacity to capture the contextual playing styles of a team. It consistently generates the same probability surface for a given spatiotemporal snapshot of the game, irrespective of the team in ball possession and the game state. 

Therefore, in this section, our goal is to incorporate the team identity and aforementioned game state factors into the SoccerMap input to obtain probability surfaces that are aware of the actual game situation. 

**5** 



### **Adapting SoccerMap to Include Game State and Team Identity** 

This requires deciding (i) how to input the game state into the model and (ii) how to adapt the structure of the network to integrate the spatiotemporal information and the game state. 

In our approach, we transform the original SoccerMap input by concatenating the game state and team identity to the input channels �Figure 2�. We use the aforementioned one-hot encoding of the game state and concatenate a 23-dimensional<sup>1</sup> one-hot encoding of the team that executes the pass. The game state and team information is subsequently compressed to a 21-dimensional vector using a fully connected layer. However, this dimensionality does not align with the sizes of the input channels representing the pitch. Therefore, we treat each variable in this vector as a 68�104 channel and replicate its value across each cell. Subsequently, we concatenate this matrix with the original SoccerMap input matrix, creating a 30�68�104 matrix. 

With this approach, we can embed categorical information into the spatiotemporal input independently of the spatial location. The intuition behind this idea is that the information provided by the game state remains consistent across all pitch coordinates. We then apply 1�1 convolutional filters to blend the original SoccerMap information with the game state and reduce the dimensions of the input channels to match the original 9�68�104 SoccerMap input size. 

Our method of integrating additional information into the SoccerMap differs from the approach employed by Pleuler �25�. That work used a parallel network to encode the individual decision-making tendencies of players into latent space embeddings. These embeddings are subsequently reshaped into surfaces and used as additional channels within the prediction architecture. Reshaping those embeddings, concatenating them with spatial input, and using convolutional layers to process them has two problems. Firstly, reshaping the embeddings and concatenating them with a matrix with spatial information creates a spatial behavior for this embedding which does not exist naturally. Secondly, processing it with convolutional networks with a kernel size larger than one infuses a locality for player information which is again not correct. In contrast, our approach integrates information into all locations of the pitch, which seems more appropriate for the game state because it intuitively has a global influence. We concatenate the same embedding with each location and use 1�1 convolutions to integrate it with the spatial data without considering neighboring locations. 

> 1 23 teams appear in the 2021/22 and 2022/23 Premier League seasons 

**6** 



**Figure 2.** Illustration of our approach for adding the game state and team identity to the SoccerMap input. 

### **Experiment and Results** 

We used data from both the 2021/22 and 2022/2023 Premier League seasons to train the model. To facilitate model selection, we designated a random 20% subset of the passes as a validation set. 

We train both the baseline SoccerMap model and the modified SoccerMap model using a learning rate of 1e-6 and a batch size of 32. We use early-stopping with patience set to 10 epochs and a delta of 1e−5. The maximum number of epochs is set to 500. 

Table 1 compares the performance and model properties of the vanilla SoccerMap architecture and our modified version. The modified version performs better both in log-loss and Brier score, which indicates that the addition of team identity and game state context allows the model to make more accurate predictions. Also, the number of parameters increases only marginally due to our 1�1 convolutional approach which does not need as many parameters as fully connected layers. 

**Table 1.** Results for the benchmark models and the modified team- and game state-aware SoccerMap model. 

|**Model**|**Log-loss**|**Brier Score**|**Nb. of**<br>**parameters**|
|---|---|---|---|
|SoccerMap|5.989|0.988|271,000|
|SoccerMap + Game state + Team ID|5.961|0.987|275,000|



**7** 



### **Practical Applications** 

Our modified SoccerMap allows us to visualize how a team will respond to different game states. We simply have to select a particular situation (i.e., the location of players and the ball), and we can then alter the game state parameters to produce different pass probability surfaces. To illustrate this, we select two passes from the dataset. We then alter one component of the game state while holding the others constant. To generate these, we sampled passes from EURO2020 data. This has the advantage of being separate from the data used for training (i.e., less risk of misleading results due to overfitting) but the disadvantage is that the lineup of players may be less typical of the considered teams. 

First, we investigate how the time remaining in a match affects Liverpool’s build-up when they play at home and the score is tied. Figure 3 shows the difference in pass probability surfaces between the 30�45 minutes and the 85�90 for a specific situation. Liverpool would be more likely to take a more cautious approach near the end of the first half. With ample time to score a goal in the second half, they are more inclined to opt for a backward pass to one of their central defenders. In contrast, when the score remains tied near the end of the game, a shift in the probability mass occurs towards a more direct offensive passing strategy. There is a greater likelihood of Liverpool choosing to pass the ball directly to one of their fullbacks or offensive midfielders. 



**8** 



**Figure 3.** When playing at home with the score being tied in the last five minutes of the game, Liverpool adopts a more direct build-up strategy. 

Second, we explore the influence of the venue on Arsenal’s passing dynamics between minutes 15�30 in a tied game. Figure 4 shows the difference in pass probability surfaces between home and away. When playing away, Arsenal has a stronger preference for a patient build-up through the center. However, at their home ground, they are more likely to directly play the ball to the flanks. 



**Figure 4.** When playing away, Arsenal has a greater preference for a patient build-up through the center. At their home ground, they are more likely to directly seek the flanks. The other game state factors are fixed to the score being tied in the second quarter of the game. 

## **Describing how the game state alters a team’s passing strategy** 

While our modified SoccerMap architecture allows us to investigate individual situations, it would also be informative to take a more holistic view to summarize how teams typically respond to changes in the game state. To address this problem, we employ a neural network-based encoder-decoder architecture. Given the SoccerMap probability surface for a specific situation, the actual passing choice (the so-called mask), and the team that performed the pass, the model will predict the corresponding game state. The encoder 

**9** 



will learn a small, latent representation that captures how teams react to different game states. 

### **A Game State Encoder-Decoder** 

A key design decision in an encoder-decoder approach is choosing the appropriate prediction task. We consider two possibilities. First, we train a model that jointly predicts all three components of the game state. This has the advantage of capturing synergies among these components. However, it makes the prediction task more difficult and training the network more complicated, which we will discuss below. Second, we train separate models to predict each component of the game state. This simplifies learning at the expense of missing any interactions that arise among the time remaining, goal difference and home/away. Regardless of the approach, we use the same encoder model. However, each task has a slightly different decoder. 

The encoder compresses the probability surfaces, mask, and team information into a 16-dimensional latent space. It has two parts: a Convolutional Encoder and a Combined Encoder. The first applies 3 convolutional layers to the 2D inputs (the probability surface for the pass-selection and its corresponding mask) to obtain a flattened representation. This representation is then concatenated with the team information and fed into the second encoder with the purpose of integrating the pass and team information. This Combined Encoder uses three fully connected layers to compress the data into the 16-dimensional latent space. 

First, the decoder expands the latent vector to a 256-dimensional vector by using three fully connected layers. Second, we employ a predictor network to predict the game state. The predictor network depends on the considered setting. When jointly predicting all elements of the game state, the model consists of three parallel networks, one for each component of the game state, each containing 3 fully connected layers. In the separate setting, the predictor network simply has 3 fully connected layers. 

To train the network, we use the following loss functions: binary cross entropy for home/away, categorical cross entropy for the time period, and categorical cross entropy for the goal difference. There are two key challenges here: 

1. Certain game states, namely those involving a goal difference of zero, occur way more often. We compare two ways to approach this. First, for each game state, we sample a maximum of 2000 passes (if there are �2000 passes then all are selected). Second, we inversely weigh each game state by its frequency. This has the effect of making it seem that each game state occurs the same number of times in the data. 

2. The loss functions are on different scales, which is only relevant when training the joint model. If not accounted for, the model may simply focus on improving the 

**10** 



predictions for the component of the loss that has the largest value. We address this by normalizing the losses and assigning an equal weight to each component. 

### **Experiment and Results** 

To train the encoder-decoder model, we first train SoccerMap to obtain probability surfaces that will be used as one of the inputs for the encoder. For training both the vanilla SoccerMap and the encoder-decoder model, we used the PyTorch Lightning framework with the adaptive moment estimation �ADAM�algorithm for optimizing the weights. For the vanilla SoccerMap �17�, we use a learning rate of 5e-6 and a batch size of 32. For the encoder-decoder model, we use a learning rate of 1e-6 and a batch size of 32. 

For training the SoccerMap model and the encoder-decoder model itself, we used 2021/22 Premier League data. We use data from the 2022/23 Premier League for evaluating the encoder-decoder model and computing the quantitative results. Again, we split 20% of the training data for validation. 

Table 2 shows the accuracy for predicting each of the three game-state components for both the joint model and the separate models. We also report the accuracy of random guessing as a baseline. Overall, we can see that training a separate encoder-decoder to predict each component of the game state has better predictive performance, except for on home vs. away. The joint model is even worse than random guessing for two of the tasks. This happens because the joint prediction task is too complicated and therefore the model is not able to infer the actual game state from the teams’ passes. 

**Table 2.** Accuracy for the three game state components for the model with separate prediction tasks and the joint model. 

|**Model**|**Accuracy**<br>**home/away**|**Accuracy**<br>**goal**<br>**difference**|**Accuracy**<br>**remaining time**|
|---|---|---|---|
|Separate model|0,5056|0,1291|0,**1824**|
|Joint model|**0.5122**|0,1027|0,1081|
|Random guess|0.5|**0.143**|0.125|



Moreover, we evaluate our design choices to cope with the imbalance in the dataset. To verify the effectiveness of our approach, we compare it with two other models: the first samples the passes without weighting them according to their frequency, while the latter weighs each sample but the training is done using the whole dataset. Table 3 shows the accuracy of the three models on three prediction tasks. Overall, the model with only sampling has the highest average accuracy. This probably happens because rare game states are so infrequent that they have a high weight, meaning that a small improvement 

**11** 



in predicting their value can have a large effect on improving the loss function. Thus the model focuses on these at the expense of the more frequent ones. 

**Table 3.** Log-loss for the three game-state components for the model with separate prediction tasks and the joint model. 

|**Model**|||**Accuracy**<br>**home/away**|**Accuracy**<br>**goal**<br>**difference**|**Accuracy**<br>**remaining time**|
|---|---|---|---|---|---|
|Separate<br>sampling<br>weighting|model|+<br>+|0,5056|0,1291|**0,1824**|
|Separate<br>sampling|model|+|**0,5108**|**0,3066**|0,1421|
|Separate<br>weighting|model|+|0,5085|0,0916|0,1421|



### **Practical Applications** 

The latent space of the encoder-decoder model effectively captures the relationship between a team’s passing decision (model input) and the game state (model output) for each pass in the dataset. Hence, we can gain insight into how teams adapt their passing strategy to specific game state changes by analyzing how a team’s vectors in this latent space change according to the various game state factors. 

Since each pass results in one latent vector �Figure 5�, we need a way to aggregate the latent vectors to be able to derive insights about a team’s contextual playing styles. Therefore, for a specific game state, we retrieve all the latent vectors for passes performed in that game state and average them. This mean vector can be viewed as the team’s typical dynamic in that game state. By comparing the distance among the teams’ mean vectors in the latent space we can analyze/discuss how different or similar teams’ passing dynamics are across particular game states. 

**12** 





**Figure 5.** A 2D projection of the latent vectors using t-SNE. Each dot corresponds to (the latent vector of) a pass and is colored according to the team that executed the pass. The passes of the same team are clustered together, indicating that the latent space captures team-specific passing dynamics. 

We first analyze the influence of remaining time on team strategies for all 20 teams in the 2022/23 Premier League season. Specifically, we aim to quantify how much each team tends to change its playing style between the first and the last quarter of a match. To achieve this, we filter the passes that belong to either of the two analyzed quarters and subsequently average all the latent vectors per team and per quarter. The difference between each team’s two resulting vectors reveals how much the teams vary their playing style between the start and the end of a game. These differences are visualized in Figure 6. Fulham has the lowest difference between the two considered time periods, showing that its playing style is very consistent throughout the entire game. On the other hand, Bournemouth and Liverpool are the teams that are most influenced by the remaining time. 

**13** 





**Figure 6.** The degree to which each team varied their playing style between the first and last quarter of a match in the 2022/23 Premier League season. 

Second, we analyze the extent to which team strategies are affected by the match venue �Table 7�. Here, we compute the mean latent vectors for each team when playing at home and when playing away. Aston Villa is the least dependent on home/away conditions. Remarkably, Liverpool and Bournemouth are again among the teams for which the passing tendencies are most affected. 



**Figure 7.** The degree to which each team varied their playing style when playing at home vs away in the 2022/23 Premier League season. 

## **Conclusions** 

Both of the proposed methods clearly showed that a team’s playing style can be strongly affected by the game state. The modified SoccerMap model makes it possible to observe this effect in a specific context. We showed that it is possible to estimate how a certain team will adapt their decision for a specific pass as a function of the game state. This can be especially useful for coaches and players to adapt their play and actions in different states of a game. The Encoder-Decoder model proposes a method to describe how the 

**14** 



game state will alter the team passing strategy, which is a useful tool for both the technical team and the media. 

For the future, we need to address two main issues that made isolating the effect of game state a hard problem. Firstly, the imbalance is a huge problem that we tried to address by sampling or weighting the loss. Also learning from joint loss was a harder problem so it is better to learn the effect of each game state factor separately which misses interactions. A method that takes account of interactions without complexing the learning task can increase the accuracy of the model. Finally, the signal in the data is too sparse. This may be complicated by the fact that we consider a fine-grained resolution of the field. It is possible that taking a higher-level or more qualitative approach may be more suitable. 

## **References** 

- �1�D. Link and M. Hoernig, “Individual ball possession in soccer,” PLOS ONE, vol. 12, no. 7, p. e0179953, Jul. 2017, doi: 10.1371/journal.pone.0179953. 

- �2�Q. Wang, H. Zhu, W. Hu, Z. Shen, and Y. Yao, “Discerning tactical patterns for professional soccer teams: An enhanced topic model with applications,” in Proceedings of the 21th ACM SIGKDD international conference on knowledge 

   - discovery and data mining, in KDD ’15. New York, NY, USA�Association for Computing Machinery, 2015, pp. 2197�2206. doi: 10.1145/2783258.2788577. 

- �3�I. Bojinov and L. Bornn, “The pressing game: Optimal defensive disruption in soccer,” in Proceedings of the 10th MIT sloan sports analytics conference, in SSAC ’16. Boston, USA, 2016, pp. 1�8. 

- �4�A. Bialkowski, P. Lucey, P. Carr, Y. Yue, S. Sridharan, and I. Matthews, “Identifying Team Style in Soccer Using Formations Learned from Spatiotemporal Tracking Data,” in 2014 IEEE International Conference on Data Mining Workshop, Dec. 2014, pp. 9�14. doi: 10.1109/ICDMW.2014.167. 

- �5�T. Decroos, J. Van Haaren, and J. Davis, “Automatic discovery of tactics in spatio-temporal soccer match data,” in Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining, in KDD ’18. New York, NY, USA�Association for Computing Machinery, 2018, pp. 223�232. doi: 10.1145/3219819.3219832. 

- �6�C. H. Almeida, A. P. Ferreira, and A. Volossovitch, “Effects of Match Location, Match Status and Quality of Opposition on Regaining Possession in UEFA Champions League.,” J. Hum. Kinet., vol. 41, pp. 203�214, Jun. 2014, doi: 10.2478/hukin-2014�0048. 

- �7�J. B. Taylor, S. D. Mellalieu, N. James, and D. A. Shearer, “The influence of match location, quality of opposition, and match status on technical performance in professional association football,” J. Sports Sci., vol. 26, no. 9, pp. 885�895, Jul. 2008, doi: 10.1080/02640410701836887. 

- �8�C. Lago, “The influence of match location, quality of opposition, and match status on possession strategies in professional association football,” J. Sports Sci., vol. 27, no. 13, pp. 1463�1469, Nov. 2009, doi: 10.1080/02640410903131681. 

- �9�R. Marcelino, I. Mesquita, and J. Sampaio, “Effects of quality of opposition and match status on technical and tactical performances in elite volleyball,” J. Sports Sci., vol. 29, 

**15** 



no. 7, pp. 733�741, Apr. 2011, doi: 10.1080/02640414.2011.552516. 

- �10� M. Konefał, P. Chmura, M. Zacharko, J. Chmura, A. Rokita, and M. Andrzejewski, “Match outcome vs match status and frequency of selected technical activities of soccer players during UEFA Euro 2016,” Int. J. Perform. Anal. Sport, vol. 18, no. 4, pp. 568�581, Jul. 2018, doi: 10.1080/24748668.2018.1501991. 

- �11�J. Clijmans, M. Van Roy, and J. Davis, “Looking Beyond the Past: Analyzing the Intrinsic Playing Style of Soccer Teams,” in Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2022, Grenoble, France, September 19�23, 2022, Proceedings, Part VI, Berlin, Heidelberg: Springer-Verlag, Mar. 2023, pp. 370�385. doi: 10.1007/978�3�031�26422�1_23. 

- �12� J. Muller, “Who never fouls? Who presses? Who hoofs it? What our data experiment says about your team,” The Athletic. Accessed: Sep. 26, 2023. �Online]. Available: https://theathletic.com/3050603/2022/01/05/who-never-fouls-who-presses-who-ho ofs-it-what-our-data-experiment-you-about-your-team/ 

- �13� Q. Wang, H. Zhu, W. Hu, Z. Shen, and Y. Yao, “Discerning Tactical Patterns for Professional Soccer Teams: An Enhanced Topic Model with Applications,” in Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, in KDD ’15. New York, NY, USA�Association for Computing Machinery, Aug. 2015, pp. 2197�2206. doi: 10.1145/2783258.2788577. 

- �14� P. Paixão, J. Sampaio, C. H. Almeida, and R. Duarte, “How does match status affects the passing sequences of top-level European soccer teams?,” Int. J. Perform. Anal. Sport, vol. 15, no. 1, pp. 229�240, Mar. 2015, doi: 10.1080/24748668.2015.11868789. 

- �15� J. Fernandez-Navarro, L. Fradua, A. Zubillaga, and A. P. McRobert, “Influence of contextual variables on styles of play in soccer,” Int. J. Perform. Anal. Sport, vol. 18, no. 3, pp. 423�436, May 2018, doi: 10.1080/24748668.2018.1479925. 

- �16� J. Monte, “Using xPass To Measure The Impact Of Gamestate On Team Style,” StatsBomb. Accessed: Aug. 25, 2023. �Online]. Available: https://statsbomb.com/articles/soccer/using-xpass-to-measure-the-impact-of-games tate-on-team-style/ 

- �17�J. Fernández and L. Bornn, “SoccerMap: A Deep Learning Architecture for Visually-Interpretable Analysis in Soccer,” in arXiv:2010.10202 [cs], 2021, pp. 491�506. doi: 10.1007/978�3�030�67670�4_30. 

- �18� T. Decroos, L. Bransen, J. Van Haaren, and J. Davis, “Actions Speak Louder than Goals: Valuing Player Actions in Soccer,” in Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining - KDD ’19, Anchorage, AK, USA�ACM Press, 2019, pp. 1851�1861. doi: 10.1145/3292500.3330758. 

- �19� P. Rahimian, K. Hyunsung, M. Schmid, and L. Toka, “Pass Receiver and Outcome Prediction in Soccer Using Temporal Graph Networks,” presented at the 10th Workshop on Machine Learning and Data Mining for Sports Analytics, Turin, Italy, Sep. 18, 2023. 

- �20� V. Vercruyssen, L. De Raedt, and J. Davis, “Qualitative spatial reasoning for soccer pass prediction,” in CEUR workshop proceedings, CEUR�WS. org, 2016. 

- �21� P. Robberechts, M. Van Roy, and J. Davis, “un-xPass: Measuring soccer player’s creativity,” in Proceedings of the 29th ACM SIGKDD conference on knowledge discovery and data mining, in KDD ’23. New York, NY, USA�ACM, 2023. doi: 10.1145/3580305.3599924. 

- �22� C. L.�P. Pedro Santos and O. García-García, “The influence of situational variables 

**16** 



on defensive positioning in professional soccer,” Int. J. Perform. Anal. Sport, vol. 17, no. 3, pp. 212�219, 2017, doi: 10.1080/24748668.2017.1331571. 

- �23� J. García-Rubio, M. Á. Gómez, C. Lago-Peñas, and J. S. Ibáñez, “Effect of match venue, scoring first and quality of opposition on match outcome in the UEFA Champions League,” Int. J. Perform. Anal. Sport, vol. 15, no. 2, pp. 527�539, Aug. 2015, doi: 10.1080/24748668.2015.11868811. 

- �24� E. Morgulev and Y. Galily, “Analysis of time-wasting in English Premier League football matches: Evidence for unethical behavior in final minutes of close contests,” J. Behav. Exp. Econ., vol. 81, pp. 1�8, 2019, doi: https://doi.org/10.1016/j.socec.2019.05.003. 

- �25� D. Pleuler, “Player Masks: Encoding Soccer Decision Making Tendencies,” presented at the Nessis 21, 2021. �Online]. Available: https://www.nessis.org/nessis21 

**17** 


