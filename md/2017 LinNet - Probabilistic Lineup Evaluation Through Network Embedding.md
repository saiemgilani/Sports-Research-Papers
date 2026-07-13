<!-- source: 2017 LinNet - Probabilistic Lineup Evaluation Through Network Embedding.pdf -->



### LinNet **: Probabilistic Lineup Evaluation Through Network Embedding** 

Konstantinos Pelechrinis School of Computing and Information University of Pittsburgh kpele@pitt.edu 

#### **Abstract** 

Which of your team’s possible lineups has the best chances against each of your opponents possible lineups? In order to answer this question we develop LinNet. LinNet exploits the dynamics of a directed network that captures the performance of lineups at their matchups. The nodes of this network represent the different lineups, while an edge from node _j_ to node _i_ exists if lineup _λi_ has outperformed lineup _λj_ . We further annotate each edge with the corresponding performance margin (point margin per minute). We then utilize this structure to learn a set of latent features for each node (i.e., lineup) using the **node2vec** framework. Consequently, LinNet builds a model on this latent space for the probability of lineup _λA_ beating lineup _λB_ . We evaluate LinNet using NBA lineup data from the five seasons between 2007-08 and 2011-12. Our results indicate that our method has an out-of-sample accuracy of 67%. In comparison, utilizing the adjusted plus-minus of the players within a lineup for the same prediction problem provides an accuracy of 55%. More importantly, the probabilities are well-calibrated as shown by the probability validation curves. One of the benefits of LinNet - apart from its accuracy - is that it is generic and can be applied in different sports since the only input required is the lineups’ matchup performances, i.e., not sport-specific features are needed. 

# **1 Introduction** 

One of the decisions that a basketball coach has to make constantly is what lineup to play in order to maximize the probability of outperforming the opponent’s lineup currently on the court. This lineup evaluation problem has been traditionally addressed through player and lineup ratings based on (adjusted) plus/minus-like approaches. In this work, we propose a different approach that is based on network science methods. In particular, we first define the matchup network: 

### **Definition 1.1: Matchup Network** 

The matchup network _G_ = ( _V, E, W_ ), is a weighted directed network where nodes represent lineups. An edge _ei,j ∈E_ points from node _i ∈V_ to node _j ∈V_ iff lineup _j_ has outperformed lineup _i_ . The edge weight _wei,j_ is equal to the performance margin of the corresponding matchup. 

Using this network we then obtain a network embedding, which projects the network nodes on a latent space _X_ . For our purposes we adopt the **node2vec** [1] framework for learning the latent space. Simply put the embedding learns a set of features **x** _u_ for node u. These features are then utilized to build a logistic regression model for the probability of lineup _λi_ outperforming lineup _λj_ , Pr[ _λi ≻ λj|_ **x** _λi,_ **x** _λj_ ]. Figure 1 visually captures LinNet. 

1/10 

NDSL 





**Figure 1. The** LinNet **lineup evaluation method** 

Our evaluations indicate that LinNet is able to predict the outcome of a lineup matchup correctly with 67% accuracy, while the probabilities are well-calibrated with a Brier score of 0.19. Furthermore, the probability validation curve of LinNet is statistically indistinguishable from the _y_ = _x_ line and hence, the logistic regression model captures accurately the lineup’s matchup probabilities. In comparison, we evaluate two baseline methods; (i) a PageRank-based ranking using the same matchup lineup networks, and (ii) a model based on the adjusted plus/minus of the players consisting each lineup. These two methods have accuracy ranging between 52-58%. 

The rest of the paper is organized as following. In Section 2 we present in details the operations of LinNet as well as the datasets we used. Section 3 presents our results, while Section 4 discusses the implications and limitations of our work. 

# **2 Materials and Methods** 

In this section we will present in detail (a) the design of LinNet, (b) the baseline methods for comparison, and (c) the datasets we used for our evaluations. 

## **2.1** LinNet 

The first step of LinNet is defining the matchup network _G_ . There is flexibility in choosing the performance margin that one can use for the edge weights. In the current implementation of LinNet, the weights of _G_ correspond to the point margin per minute for the two lineups. 

Once the network is obtained the next step is to learn the network embedding. As our network embedding mechanism we will utilize the approach proposed by Grover and Leskovec [1], namely, node2vec. node2vec utilizes (2<sup>_nd_</sup> order) random walks on the network in order to learn the latent features of the nodes, i.e., a function _f_ : _V →ℜ_<sup>_d_</sup> , where _d_ is the dimensionality of the latent space. Starting from node _u_ in the network and following the random walk strategy _R_ the network neighborhood _NR_ ( _u_ ) of _u_ is defined. Then node2vec learns the network embedding _f_ by solving the following optimization problem: 



Simply put, the network embedding maximizes the log-likelihood of observing a network neighborhood _NR_ ( _u_ ) for node _u_ conditioned on the network embedding _f_ . The random walk strategy is defined by two parameters, _p_ and _q_ , that offer a balance between a purely breadth-first search walk and a purely depth-first search walk. In particular, the random walk strategy of node2vec includes a bias term _α_ controlled by parameters p and q. Assuming that a random walk is on node _u_ (coming from node _v_ ), 

2/10 

NDSL 



the unnormalized transition probability _πux_ = _αpq_ ( _v, x_ ) _· wux_ . With _dux_ being the shortest path distance between _u_ and _x_ we have: 



As alluded to above parameters _p_ and _q_ control the type of network neighborhood _NR_ ( _u_ ) we obtain. Different sampling strategies will provide different embeddings. For example, if we are interested in having set of nodes that are tightly connected in the original network close to each other in the latent space, _p_ and _q_ need to be picked in such a way that allows for “local” sampling. In our application we are interested more in identifying structurally equivalent nodes, i.e., nodes that are similar because of their connections in the network are similar (not necessarily close to each other with respect to network distance). This requires a sampling strategy that allows for the network neighborhood of a node to include nodes that are further away as well. Given this objective and the recommendations by Grover and Leskovec [1] we choose _q_ = 3 and _p_ = 0 _._ 5 for our evaluations. Furthermore, we generate 3,000 walks for each network, of 3,500 hops each. Finally, we choose as our latent space dimensionality, _d_ = 128. Increasing the dimensionality of the space improves the quality of the embedding as one might have expected, however, our experiments indicate that increasing further the dimensionality beyond _d_ = 128 we operate with diminishing returns (with regards to computational cost and improvement in performance). 

Once the latent space _X_ is obtained, we can build a logistic regression model for the probability of lineup _λi_ outperforming _λj_ . In particular, we use the Bradley-Terry model. The Bradley-Terry model is a method for ordering a given set of items based on their characteristics and understanding the impact of these characteristics on the ranking. In our case the set of items are the lineups and the output of the model for items _i_ and _j_ provides us essentially with the probability of lineup _λi_ outperforming _λj_ . In particular, the Bradley-Terry model is described by [2]: 



where _πi_ is the _ability_ of team _i_ . Given a set of lineup-specific explanatory variables **z** _i_ , the difference in the ability of lineups _λi_ and _λj_ can be expressed as: 



where _U ∼ N_ (0 _, σ_<sup>2</sup> ). The Bradley-Terry model is then a generalized linear model that can be used to predict the probability of team _i_ winning team _j_ . In our case, the explanatory variables are the latent space features learned for each lineup, **x** _λi_ . 

**Previously Unseen Lineups:** One of the challenges (both in out-of-sample evaluations as well as in a real-world setting), is how to treat lineups that we have not seen before, and hence, we do not have their latent space representation. In the current design of LinNet we take the following simple approach. In particular, for each lineup _λi_ of team _T_ we define the similarity in the players’ space _σλi,λj_ of _λi_ with _λj ∈LT_ , as the number of common players between the two lineups. It is evident that the similarity value ranges from 0 to 4. One might expect that lineups with high overlap in the players’ space, should also reside closely in the embedding space. In order to get a feeling of whether this is true or not, we calculated for every team and season the correlation between the similarity between two lineups in the players’ space (i.e., _σλi,λj_ ) with the distance for the corresponding latent features (i.e., `dist` ( **x** _i,_ **x** _j_ )). As we can 

3/10 

NDSL 



see from Figure 2 all teams exhibit negative correlations (all correlations are significant at the 0.001 level), which means the more common players two lineups have, the more close they will be projected in the embedding space. Of course, the levels of correlation are moderate at best since, the embedding space is obtained by considering the performance of each lineup, and two lineups that differ by only one player might still perform completely differently on the court. With this in mind, once we obtain the lineup similarity values, we can assign the latent feature vector for the previously unseen lineup _λi_ as a weighted average of the lineups in _LT_ : 



It is evident that this is simply a heuristic that is currently implemented in LinNet. One could think of other ways to approximate the latent space features of a lineup not seen before. 



**Figure 2. Lineups with higher overlap in terms of players exhibit smaller distance in the latent embedding space** _X_ 

## **2.2 Baselines** 

For comparison purposes we have also evaluated two baseline approaches for predicting lineup matchup performance. The first one is based on network ranking that operates directly on the matchup network (i.e., without involving any embedding of the network), while the second one is based on the adjusted plus/minus rating of the players that belong to the lineup. 

**Network Ranking:** In our prior work we have shown that ranking teams through a win-loss network, achieves better matchup prediction accuracy as compared to the win-loss percentage [3]. Therefore, we follow a similar approach using the lineup matchup network and ranking lineups based on their PageRank score. The PageRank of _G_ is given by: 



where _A_ is the adjacency matrix of _G_ , _α_ is a parameter (a typical value of which is 0.85) and _D_ is a diagonal matrix where _dii_ = max(1 _, ki,out_ ), with _ki,out_ being the out-degree 

4/10 

NDSL 



of node _i_ . Using the PageRank score differential ∆ _rij_ = _rλi − rλj_ as our independent variable we build a logistic regression model for the probability: Pr( _λi ≻ λj|_ ∆ _rij_ ). 

**Adjusted plus/minus (APM):** The APM statistic of a player is a modern NBA statistic - and for many people the best single statistic we currently have for rating players. It captures the additional points that the player is expected to add with his presence in a lineup consisting of league average players matching up with a lineup with league average players. APM captures the impact of a player beyond pure scoring. For instance, a player might impact the game by performing good screens that lead to open shots, something not captured by current box score statistics. The other benefit of APM is that it controls for the rest of the players in the lineups. More specifically the APM for a player is calculated through a regression model. Let us consider that lineup _λi_ has played against _λj_ , and has outscored the latter by _y_ points per 48 minutes. _y_ is the dependent variable of the model, while the independent variable is a binary vector **p** , each element of which represents a player. All elements of **p** are 0 except for the players in the lineups. Assuming _λi_ is the home lineup<sup>1</sup> , _pn_ = 1 _, ∀pn ∈ λi_ , while for the visiting lineup, _pn_ = _−_ 1 _, ∀pn ∈ λj_ . Then these data are used to train a regression model: 



where **a** is the vector of regression coefficients. Once obtaining this vector, the APM for player _pn_ is simply _apn_ . The rating of lineup _λi_ , _ρλi_ is then the average APM of its players: 



Using the lineup rating differential ∆ _ρij_ = _ρλi − ρλj_ as our independent variable we again build a logistic regression model for the probability: Pr( _λi ≻ λj|_ ∆ _ρij_ ). 

## **2.3 Datasets** 

In order to evaluate LinNet we used lineup data during the 5 NBA seasons between 2007-08 and 2011-12. This dataset includes aggregate information for all the lineup matchups for each of the 5 seasons. In particular, for each pair of lineups (e.g., _λi_ , _λj_ ) that matched up on the court we obtain the following information: 

1. Total time of matchup 

2. Total point differential 

3. Players of _λi_ 

4. Players of _λj_ 

We used these data in order to obtain both the matchup network as well as to calculate the APM for every player in each season. 

# **3 Analysis and Results** 

We now turn our attention in evaluating LinNet. Our focus is on evaluating the accuracy of LinNet in predicting future lineup matchups, as well as the calibration of the inferred probabilities. For every season, we build each model using 80% of the 

> 1If this information is not available - e.g., because the input data include the total time the lineups matched up over multiple games - W.L.O.G. we can consider the home lineup to be the one with lower ID number. This is in fact the setting we have in our dataset. 

5/10 

NDSL 



matchups and we evaluate them on the remaining 20% of the matchups (which might also include lineups not seen before). Our evaluation metrics are (i) prediction accuracy, (ii) Brier score and (iii) the probability calibration curves. 

Figure 3 presents the accuracy performance of the various methods. As we can see LinNet outperforms both the PageRank and APM systems over all 5 seasons examined. LinNet’s accuracy is 67%, while APM exhibits a 55% average accuracy and PageRank a 53% accuracy. 



<!-- Start of picture text -->
1.00<br>0.75<br>Method<br>APM<br>0.50 LinNet<br>PageRank<br>0.25<br>0.00<br>2007-08 2008-09 2009-10 2010-11 2011-12<br>Season<br>Accuracy<br><!-- End of picture text -->

**Figure 3.** LinNet **outperforms in accuracy baseline methods over all 5 seasons examined** 

However, equally as important for the quality of the model is the calibration of the output probabilities. We begin by first computing the Brier score [4] for each model and dataset. In the case of a binary probabilistic prediction the Brier score is calculated as: 



where _N_ is the number of observations, _πi_ is the probability assigned to instance _i_ being equal to 1 and _yi_ is the actual (binary) value of instance _i_ . The Brier score takes values between 0 and 1 and evaluates the calibration of these probabilities, that is, the level of confidence they provide (e.g., a 0.9 probability is _better_ calibrated compared to a 0.55 probability when the ground truth is label 1). The lower the value of _β_ the better the model performs in terms of calibrated predictions. Our model exhibits an average Brier score _β_ of 0.19, while both PageRank and APM models have a worse Brier score. Typically the Brier score of a model is compared to a baseline value _βbase_ obtained from a _climatology_ model [5]. A climatology model assigns the same probability to every observation, which is equal to the fraction of positive labels in the whole dataset. Therefore, in our case the climatology model assigns a probability of 0.5 to each observation. As alluded to above we do not have information about home and visiting lineup so our model estimates the probability of the lineup with the smaller ID outperforming the one with the larger ID. Given that the lineup ID has no impact on this probability the climatology model probability is 0.5. The Brier score for this reference model is _βbase_ = 0 _._ 25, which is of lower quality as compared to LinNet and also slightly worse than our baselines. 

6/10 

NDSL 





<!-- Start of picture text -->
0.25<br>0.20<br>0.15<br>Method<br>APM<br>LinNet<br>PageRank<br>0.10<br>0.05<br>0.00<br>2007-08 2008-09 2009-10 2010-11 2011-12<br>NBA Season<br>Brier Score<br><!-- End of picture text -->

**Figure 4.** LinNet **exhibits better calibrated probabilities as compared to the baselines (smaller Brier score translates to better calibration)** 

As alluded to above we have picked a dimensionality for the embedding of _d_ = 128. However, we have experimented with different embedding dimensionality values and our results are presented in Figure 5. As we can see, low dimensionality does not provide any benefit over the baselines, while increasing further the dimensionality (above 128) exhibits diminishing returns. 



<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0 100 200 300 400 500<br>Embedding Dimensionality<br>Accuracy<br><!-- End of picture text -->

**Figure 5. The choice of** _d_ = 128 **for the embedding dimensionality of** LinNet **provides a good tradeoff between accuracy and (computational) complexity** 

Finally, we evaluate the accuracy of the probability output of LinNet by deriving the probability validation curves (for _d_ = 128). In order to evaluate this we would ideally want to have every matchup played several times. If the favorite lineup were given a 75% probability of outperforming the opposing lineup, then if the matchup was played 100 times we would expect the favorite to outperform in 75 of them. However, this is not realistic and hence, in order to evaluate the accuracy of the probabilities we 

7/10 

NDSL 



will use all the games in our dataset. In particular, if the predicted probabilities were accurate, when considering all the matchups where the favorite was predicted to win with a probability of x%, then the favorite should have outperform the opponent in x% of these matchups. Given the continuous nature of the probabilities we quantize them into groups that cover a 5% probability range. Fig 6 presents the predicted win probability for the reference lineup (i.e., the lineup with the smaller ID) on the x-axis, while the y-axis presents how many of these matchups this reference lineup won. Furthermore, the size of the points represents the number of instances in each situation. As we can see the validation curve is very close to the _y_ = _x_ line, which practically means that the predicted probabilities capture fairly well the actual matchup probabilities. In particular, the linear fit has an intercept of 0.1 and a slope of 0.85. 



<!-- Start of picture text -->
1.00<br>0.75<br>Count<br>2000<br>0.50 4000<br>6000<br>0.25<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>Predicted Lineup Matchup Probability<br>Fraction of Correct Predictions<br><!-- End of picture text -->

**Figure 6. The** LinNet **probability validation curve is very close to the** _y_ = _x_ **line, translating to fairly accurate probability estimations** 

**Season Win-Loss Percentage and Lineup Performance:** How well can lineup _ratings_ obtained from LinNet explain the win-loss record of a team? One should expect that there is a correlation between LinNet lineup ratings and the record of a team - which as we will see indeed is the case. However, this correlation is also not expected to be perfect, since it relies also on coaching decisions as well as availability of the lineups (e.g., a lineup can be unavailable due to injuries). In order to examine this we focus on lineups that played for a total of more than a game (i.e., 48 minutes) during the season. Then with _pλi_ being the average probability of lineup _λi_ (of team _τ_ ) outperforming each of the opponent’s lineups (i.e., _pλi_ = <u>�</u> _λj ∈L\Lτ_<sup>Pr(</sup><sup>_λi≻λj_)</sup> , where _|L \ Lτ | Lτ_ is the set of all lineups of team _τ_ and _L_ is the set of all league lineups), the LinNet team rating of team _τ_ is: 



where _γi_ is the total time lineup _λi_ has been on the court over the whole season. Our 

8/10 

NDSL 



results are presented in Figure 7. The linear regression fit has a statistically significant slope (p-value _<_ 0.001), which translates to a statistically important relationship. However, as we can see there are outliers in this relationship, such as the 2008-09 Cavaliers and the 2011-12 Nets. The linear relationship explains 27% of the variability at the win-loss records of the teams. This might be either because teams do not choose (due to various reasons) their best lineup to matchup with the opponent, or because the time that a lineup is on court is important for its performance (we discuss this in the following section), something that LinNet currently does not account for. Overall, the correlation coefficient between the LinNet team rating and the win-loss record is 0.53 (p-value _<_ 0.0001). 



**Figure 7. The** LinNet **probability validation curve is very close to the** _y_ = _x_ **line, translating to fairly accurate probability estimations** 

# **4 Discussion** 

In this work we presented LinNet, a network embedding approach in evaluating lineups. Our evaluations indicate that the probability output from LinNet is well calibrated and more accurate than traditional lineup evaluation methods. However, there are still some open issues with the design of LinNet. More specifically, a matchups between specific lineups might last only for a few minutes (or even just a couple of possessions). This creates a reliability issue with any predictions one tries to perform with similar information. Even though we adjust the performance margin on a per minute basis, it is not clear that a lineup can keep up its performance over a larger time span. 

Furthermore, currently for lineups we have not seen before we use as its latent features a weighted average of already seen lineups of the team, weighted based on their similarity in the players’ space. However, there are other approaches that one might use for this task that could potentially provide even better results. For example, a regression (similar to the adjusted plus/minus) can be used to infer the latent features based on the players in the lineup. This is something that we plan in exploring in the future. 

# **References** 

1. Grover A, Leskovec J (2016) node2vec: Scalable feature learning for networks. In: Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, pp. 855–864. 

9/10 

NDSL 



2. Agresti A (2007) An introduction to categorical data analysis. Wiley series in probability and statistics. Hoboken (N.J.): Wiley-Interscience. 

3. Pelechrinis K, Papalexakis E, Faloutsos C (2016) Sportsnetrank: Network-based sports team ranking. In: ACM SIGKDD Workshop on Large Scale Sports Analytics. 

4. Brier GW (1950) Verification of forecasts expressed in terms of probability. Monthly weather review 78: 1–3. 

5. Mason SJ (2004) On using “climatology” as a reference strategy in the brier and ranked probability skill scores. Monthly Weather Review 132: 1891–1895. 

10/10 

NDSL 


