<!-- source: 2020 Unsupervised Methods for Identifying Pass Coverage Among Defensive Backs with NFL Player Tracking Data - Dutta, Yurko, Ventura.pdf -->

# **Unsupervised Methods for Identifying Pass Coverage Among Defensive Backs with NFL Player Tracking Data** 

Rishav Dutta<sup>1</sup> , Ronald Yurko<sup>2</sup> , Samuel L. Ventura<sup>2</sup><sup>_,_3</sup> 

> 1Carnegie Mellon University, School of Computer Science 

> 2Carnegie Mellon University, Department of Statistics & Data Science 

> 3Pittsburgh Penguins 

April 16, 2020 

#### **Abstract** 

Statistical analysis of defensive players in football has lagged behind that of offensive players, special teams, and coaching decisions, largely because data on individual defensive players has historically been lacking. With the introduction of player tracking data from the NFL, researchers can now tackle these problems. However, event and strategy annotations in the NFL’s tracking data are limited, especially when it comes to describing what defensive players do on each play. Moreover, methods for creating these annotations typically require extensive human labeling, which is difficult and expensive. Because of the importance of the passing game and the limited prior research on the defensive side of passing, we provide annotations for the pass coverage types of cornerbacks using unsupervised learning techniques, which require no training data. We define a set of features from the tracking data that distinguish between “man” and “zone” coverage. We use mixture models to create clusters corresponding to each group, allowing us to provide probabilistic assignments to each coverage type (or cluster). Additionally, we quantify each feature’s influence in distinguishing defensive pass coverage types. Our work makes possible several potential avenues of future NFL research into defensive backs and pass coverage strategies. 

## **1 Introduction** 

Statistical analysis of defensive players in the National Football League (NFL) is challenging, since the data collected and made publicly available for each play is limited to players directly involved in a play (e.g. the passer, rusher, receiver, tackler, etc). However, most of what happens throughout the course of a football play happens away from the ball: offensive linemen blocking, defensive linemen going after the quarterback or ball-carrier, defensive 

1 

backs covering receivers, etc. To date, publicly available statistics for the evaluation of defensive players are limited to simple counting measures like tackles, sacks, interceptions, etc. Private companies like Pro Football Focus likely provide innovative metrics to NFL teams, but this information is not available publicly. Aside from what has been recently made available via the NFL’s Next Gen Stats website, little work has been done publicly to analyze defensive players. 

However, the NFL now collects detailed player and ball tracking data, which marks the locations and trajectories (speed, angle) of all 22 players on the field and the ball at a rate of 10 Hz. Using this data, new measures of player performance are now possible for the first time. For example, Burke (2018) provides a method for analyzing pass rushers using NFL tracking data. 

Across all team sports, analyzing on-field events or strategies employed by teams or individual athletes is only possible if these events or strategies are annotated in the tracking dataset. For example, the NBA provides basic event annotations (e.g. passes, shots, turnovers) in its optical tracking data, but more detailed information (e.g. defensive schemes, picks, or set plays) must be identified by analysts. An example of this is the work of Miller and Bornn (2017), who identify and annotate set plays during basketball possessions. Similarly, the NFL provides some basic event annotations (e.g. ball snapped, handoff, first – contact, etc), but more detailed annotations especially those relating to defensive players – must be identified by analysts. We describe prior work in this area below. 

### **1.1 Prior Research on Annotating Events and Strategies with Tracking Data in Team Sports** 

Prior researchers have attempted to annotate individual events and strategies (in both football and other sports) using both supervised and unsupervised learning techniques. Here, it is first important to distinguish unsupervised learning techniques, which do not require potentially expensive sets of training data, from supervised learning techniques, which require training data to model specific outcomes. If researchers have access to an extensive set of ground truth labels for the outcome they seek to model, they should use a supervised learning approach like Burke (2019), which uses training data to predict which potential pass catcher a quarterback will target, among other contributions. Without labels, unsupervised techniques are preferable, as the researchers below have demonstrated. 

In soccer, Bialkowski et al. (2014) use player tracking data to identify a team’s playing style from their players’ positions and movements on the field. To do this, they design a set of role-specific features that reduces the entropy of role-specific occupancy maps. In doing so, the authors assign some formation-based roles to individual players, and then create occupancy maps based on these roles that are assigned. 

In basketball, Lucey et al. (2014) use the spatio-temporal changes in the team formation in order to determine what features allow for a player to create an “open” shot. Similar to Bialkowski et al. (2014), the authors create role-based features by initially assigning each player a role. In this case, they assign each of the five players on the court one of the traditional five basketball positions. After doing this, they can track the motion of the roles rather than individual players in order to create a permutation-free set of features. 

2 

Gudmundsson and Horton (2016) provides an excellent overview of prior work on formation identification in team sports. We encourage interested readers to visit this paper for more information on this topic. Most prior work in this area has focused on annotating teamwide strategies, as opposed to the strategies of individual athletes, as we do in this paper. Two exceptions are Miller and Bornn (2017) and Chu et al. (2019), who use unsupervised learning techniques such as mixture modeling to provide these supplemental annotations to users of the data. As mentioned above, Miller and Bornn (2017) annotate set plays in the NBA. To do this, they use complex mixtures of Bezier curves to cluster the simultaneous trajectories of the five players on the court. Chu et al. (2019) use a similar approach, but for individual wide receiver routes in football. 

The problem we tackle in this paper deviates from these prior approaches in two important ways. First, unlike most prior work, we seek to identify the coverage types of _individual_ defensive players, rather than look at team-wide strategies. Second, unlike Miller and Bornn (2017) and Chu et al. (2019), who each use mixture models to provide unsupervised labels for the patterns of movement of offensive players, we focus on defensive players. This is important, since in most team sports, offensive players dictate their own movements, while defensive players typically move in reaction to offensive players. Because the movements of players in defensive pass coverage are inherently reactive, we cannot simply cluster the defensive backs trajectories and expect to identify pass coverage types from the results. Instead, we take the approach described below. 

### **1.2 Our Contribution** 

In this paper, we introduce a unsupervised approach for annotating (or labeling) the coverage type of defensive backs in American football using NFL tracking data, using an extensive set of features that we create to characterize and distinguish the motions of defensive backs in relation to the corresponding offensive player. The unsupervised approach that we use has several benefits (described below), and can be extended to other event and strategy annotation problems in NFL tracking data. We choose to tackle the problem of identifying the type of pass coverage used by defensive backs for several reasons (described below). 

First, pass coverage types are not available publicly on a play-by-play level. NFL coaches may collect this information on their own (or turn to third-party companies like Pro Football Focus to provide this information), but doing so can be time-consuming and/or costly. By automating this process, we allow coaches to spend their time more effectively, and we allow resources to be allocated to other organizational needs. Importantly, our model can be used by NFL teams instantaneously during a game (assuming tracking data is available in real-time); this would, for example, allow coaches to have more information at hand when analyzing opponents’ strategies, and make on-the-fly adjustments at halftime or throughout the course of the game without the need for humans to manually label each play. Moreover, not all users of the NFL player tracking data also have access to an extensive set of plays with labeled pass coverage types. By automating this process using unsupervised techniques, we level the playing field for users of the data who lack this information or the resources to acquire it. 

Second, passing has become increasingly important in the NFL in recent years, with teams passing the ball (vs. running the ball) more than they ever have before. Despite this, 

3 

there has been limited public research into the play of defensive backs and the efficacy of different coverage schemes. By providing coverage type annotations, we pave the way for future researchers to tackle these important problems. 

Third, this problem is both challenging and adaptable to other event and strategy annotation problems. Unlike the work of Miller and Bornn (2017) or Chu et al. (2019), who provide annotations for offensive player movement (e.g. wide receiver routes), we address an analogous problem for defensive players. The key difference here is that offensive players control their movements on the playing surface, while defensive players act in reaction to the offensive players<sup>1</sup> . This means that techniques that cluster player trajectories on the field are not appropriate for identifying defensive coverage schemes. Instead, we generate a rich set of features describing the movements of defensive players _in relation to their teammates and to their counterparts on the offensive side_ (e.g. wide receivers). We use this extensive set of features to identify groups of plays with similar coverage, then use mixture models to assign “soft” cluster labels like “man coverage” or “zone coverage” (described in Section – 2) to the identified groups. Our approach generating an information-rich feature set and – using mixture models to assign labels can be adapted to almost any event or strategy annotation problem in the NFL, provided a set of tracking data. For example, this approach could be used to automatically identify run-blocking strategies (e.g. guard pulls), pass rush assignments, pass rush strategies (e.g. stunts, blitzes, etc), and other sub-problems. 

Finally, the use of mixture modeling (or “model-based clustering”) comes with several benefits. Most importantly, mixture models provide an actual statistical model to describe the cluster structure for a given problem. Because it is a density-based clustering approach, there are no heuristics involved in the estimation of the model. One advantage to densitybased methods is that the resulting clusters are typically more interpretable, since we can characterize each cluster by the features of the density we fit to the data (e.g. each group’s mean and variance in mixture modeling). Additionally, mixture models provide “soft” cluster – – assignments i.e. probabilities of membership in each cluster allowing us to quantify the uncertainty in each cluster assignment. 

The rest of this paper is organized as follows: We first describe defensive pass coverage schemes for passing plays in football in Section 2. Then, we provide detail on each step of our clustering process in Section 3. We detail the feature set that we design for the purposes of clustering pass coverage types in Section 3.2. We describe mixture modeling in Section 3.3, highlighting the features of this technique that make it suitable for identifying pass coverage types. We describe our approach for evaluating our clustering results and assessing the utility of each feature in Section 3.4. We present the results of these approaches in Section 4, and we discuss future directions for this work in Section 5. 

## **2 Characterizing Pass Coverage Types in Football** 

A defensive back in football is a player who lines up in the defensive backfield (typically at least a yard past the line of scrimmage, and to the outside of the field). Their primary objective is to prevent the offense from completing any passes by covering wide receivers 

> 1There are exceptions here, e.g. option routes where the offensive player’s route is chosen during the play in reaction to the pattern of motion of the defensive back. 

4 



**Figure 1:** Defensive Backs in Football. The left-most and right-most blue squares are cornerbacks (labeled clearly on the left figure); the top-most two blue squares are safeties (labeled clearly in the right figure). Cornerbacks and safeties are primariliy responsible for pass coverage. 

(offensive players who typically line up on the outside). In this section, we distinguish the different types of defensive backs, and we describe the two primary types of individual pass coverage that defensive backs play. 

### **2.1 Types of Defensive Backs** 

There are two different, specialized positions broadly classified as defensive backs: cornerback (CB) and safety (split into “strong safeties”, SS, and “free safeties”, FS). 

Generally, cornerbacks are more adept at providing close coverage on wide receivers and defending passes.The position requires speed and agility, and the ability to track a receiver (in man coverage) or occupy a space and read the quarterback (in zone coverage). 

Safeties usually start the play 10-15 yards beyond the line of scrimmage and can be thought of as the last line of defense. Their roles often depend on how the personnel is used by the offensive team: sometimes, they provide additional help in defending long passes; other times, they provide man coverage on additional offensive receivers that are on the field. They are also responsible for reading the play, quickly determining if it is a run or pass play, and reacting accordingly. The typical alignment of players at each of these positions is shown in Figure 1. 

In this paper, we focus primarily on pass coverage types of cornerbacks, which typically fit into one of two categories: man coverage and zone coverage. Below, we characterize each type of coverage and offer insight into the types of features that will be useful in distinguishing man coverage from zone coverage. 

### **2.2 Types of Individual Defensive Pass Coverage** 

Individual defensive backs typically play one of two types of pass coverage: man coverage and zone coverage, which we describe below. 

In man coverage, a defensive back is assigned to defend a specific offensive player (typically a wide receiver). Throughout the play, the defensive back follows that offensive player until the ball is thrown in an attempt to prevent that offensive player from making himself open and ultimately catching the ball. In man coverage, the defensive back is focused on the movement of the offensive player, often with his head turned toward the offensive player, and often not even looking at the quarterback or the ball. As such, the on-field motion of the defensive back may tend to mirror that of the offensive player that the cornerback is 

5 



**Figure 2:** In different forms of Zone coverage, players are assigned different areas of the field to cover (denoted by the circle). In some types, certain players will be assigned man coverage as well (denoted by the line). “Cover- _n_ ” means that _n_ players (typically safeties) are playing deep zone coverage, while the remaining players may be assigned to either man coverage or zone coverage closer to the line of scrimmage. Cover-4 may be used in situations when preventing deep passes is of utmost importance (e.g. 3rd-and-20, or during a two-minute drill). Cover-1 my be used more frequently in short-yardage situations. Cover-2 is probably the most common of these coverage schemes. 

covering. Importantly, this does not mean that the patterns of motion of defensive backs in man coverage will follow well-defined trajectories, as is the case for wide receivers. Instead, their patterns of motion will correlate closely with those of the player they are covering. In the context of our problem, generating features that reflect this type of motion will be important. This requires identifying the offensive player to which each defensive back is assigned to cover and building a set of features that capture this type of movement. 

In zone coverage, a defensive back is assigned a zone on the field to defend. These zones are constructed so that both the linebackers (who typically line up closer to the line of scrimmage and in the center of the field) and the defensive backs work together to provide a complete coverage of the possible passing areas in order to prevent the completion of a pass. Generally, when a player is in zone coverage, their eyes are on the quarterback and their movements are less reactive to the movements of specific offensive players. 

This is not always the case, however. For example, if a defensive back in zone coverage sees that there is only one offensive player near his zone, his responsibility shifts, so that he must now cover that single player in a way that resembles man coverage. In other words, the locations and trajectories of teammates, opponents, and the ball can cause the defensive back to adjust his assignment _in the middle of the play_ . This “hybrid” style of defensive coverage can be difficult to measure through feature generating, and can make the automatic identification of zone coverage challenging. 

Most of the time, teams employ some combination of man coverage and zone coverage on a single play. For example, some teams would play a variation of Cover 2 (example shown in Figure 2), where the cornerbacks are in man coverage and the safeties are in zone coverage. 

6 

## **3 Methods** 

In this section, we define a set of features describing the motion of each defensive back, and then apply several clustering methods to these features. In this way, we attempt to encapsulate the motion of the defensive backs and make a distinction between different types of coverage in an entirely unsupervised way. 

### **3.1 Data** 

We use NFL player and ball tracking data from the NFL’s inaugural Big Data Bowl. This dataset consists of game data from the first six weeks of the 2017 NFL season. Each play from each game uses the league’s player and ball tracking technology to record the locations and trajectories of all 22 players on the field (and the ball) throughout the duration of the play, at a rate of 10 Hz (10 frames per second). For each play, data is recorded starting from when the offense is set<sup>2</sup> . For each player, each frame contains their _x_ and _y_ coordinates on the field with 0 _≤ x ≤_ 120 and 0 _≤ y ≤_ 58 for each frame. Furthermore, for each player, each frame consists of their speed _s_ , displacement from last position, and direction of motion on the field described by the angle _θ_ , 0 _≤ θ ≤_ 360. A subset of frames are also labeled with text indicating the on-field event that happened at that frame (e.g. ball is snapped, first contact, etc). For the purposes of this paper, the relevant events are mostly `ball snap` and `pass` ~~`f`~~ `orward` . 

One piece of information that is not available to us is the orientation of the defensive players on the field. This is unfortunate, since the direction that a defensive back faces (relative to the offensive player to which he is assigned) would likely be one of the most informative features when distinguishing man vs. zone coverage. We discuss this further in Section 5 and offer insight into how this additional information may be used by NFL teams, who have access to this data. 

We use this data to generate features characterizing the movement of the defensive back, such that a clustering of these features will result in a meaningful interpretation of their coverage type. There are 6,712 pass plays that we examine from the data set. From these 6,712 pass plays we generate 16,316 feature vectors in the feature generation step. 

### **3.2 Feature Generation** 

The relationships between the type of pass coverage (man or zone) and the movements, positions, and trajectories of players (relative to offense or otherwise) change at different time periods throughout the play. For example, if a cornerback is facing the line of scrimmage at the start of a play, this tells us nothing about the type of coverage he is playing. However, if he is still facing the line of scrimmage at the time the ball is thrown, he is more likely to be playing zone coverage. For this reason, we design features that can be estimated at different points throughout the play that correspond to on-field events. 

> 2Because of this, the pre-snap motions of offensive players are included, and the corresponding reactionary movements of defensive players are captured, allowing us to use this information when identifying coverage types before the snap (similar to how a quarterback will read a defense by putting receivers or running backs in motion before the snap). 

7 



**Figure 3:** The time periods over which features are extracted 

These time periods are described in Figure 3: For each cornerback on each play, and for each of the time periods described in this figure, we generate a feature vector that consists of the features described in Table 1. The features are generated with respect to the cornerback being analyzed on each play. Let ( _xi,t, yi,t_ ) represent the coordinates of cornerback _i_ , and _si,t_ represents his speed, all at frame _t_ . Let _O_ and _D_ refer to the set of offensive players and set of defensive players respectively. _mi,t_ refers to player _i_ ’s direction of motion at frame _t_ . Let _T_ be the number of frames for the play in question (in practice, _T_ varies from play-to-play and would be indexed by the number of plays). In the table below, _µO_ ( _µD_ ) refers to the mean distance to the closest offensive (defensive) player, while _µm_ refers to the mean difference in directions of motion, _µx_ refers to the mean _x_ -coordinate on a play, and so on. Unless otherwise stated below, player _i_ refers to the cornerback in question on a given play (i.e. the defensive player for whom we are trying to predict the coverage type), player _j_ refers to the closest offensive player, and player _k_ refers to the closest teammate (another defensive player). 

|Feature Name|Feature Description|Feature Equation|
|---|---|---|
|`VAR`<br>~~`X`~~|Variance in the x coordinate|�_T_<br>_t_=1<sup>(</sup><sup>_xi,t−µx_)2</sup><br>_n_|
|`VAR`<br>~~`Y`~~|Variance in the y coordinate|�_T_<br>_t_=1<sup>(</sup><sup>_yi,t−µy_)2</sup><br>_n_|
|`SPEED`<br>~~`V`~~`AR`|Variance in the speed|�_T_<br>_t_=1<sup>(</sup><sup>_si,t−µs_)2</sup><br>_n_|
|`OFF`<br>~~`V`~~`AR`|Variance in the distance from the<br>nearest ofensive player at every<br>frame|�_T_<br>_t_=1<sup>(</sup><sup>_dt−µO_)2</sup><br>_T_<br>,<br>_dt_ = arg min<br>_j∈O_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup>|



8 

|`DEF`<br>~~`V`~~`AR`|Variance in the distance from the<br>nearest defensive player at every<br>frame|�_n_<br>_t_=1<sup>(</sup><sup>_dt−µD_)2</sup><br>_T_<br>,<br>_dt_ = arg min<br>_k∈D_<br>~~�~~<br>(_xk,t −xi,t_)<sup>2 </sup>+ (_yk,t −yi,t_)<sup>2</sup>|
|---|---|---|
|`OFF`<br>~~`M`~~`EAN`|Mean distance from the nearest of-<br>fensive player at every frame|�_n_<br>_t_=1 <sup>_dt_</sup><br>_T_<br>, _dt_ = arg min<br>_j∈O_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup>|
|`DEF`<br>~~`M`~~`EAN`|Mean distance from the nearest<br>defensive player at every frame|�_n_<br>_t_=1 <sup>_dt_</sup><br>_T_<br>, _dt_ = arg min<br>_k∈D_<br>�<br>(_xk,t −xi,t_)<sup>2 </sup>+ (_yk,t −yi,t_)<sup>2</sup>|
|`OFF`<br>~~`D`~~`IR`<br>~~`V`~~`AR`|Variance in the diference in de-<br>grees of the direction of motion be-<br>tween the player and the nearest<br>ofensive player|�_T_<br>_t_=1<sup>((</sup><sup>_mj,t−mi,t_)</sup><sup>_−µm_)2</sup><br>_T_<br>_j_ = arg min<br>_j∈D_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup>|
|`OFF`<br>~~`D`~~`IR`<br>~~`M`~~`EAN`|Mean diference in degrees of the<br>direction of motion between the<br>player and the nearest ofensive<br>player|�_T_<br>_t_=1<sup>(</sup><sup>_mj,t−mi,t_)</sup><br>_T_<br>_j_ = arg min<br>_j∈D_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup>|
|`RAT-MEAN` (_µr_)|Mean ratio of the distance to the<br>nearest ofensive player _j_ and the<br>distance from the nearest ofen-<br>sive player to the nearest defensive<br>player _k_|_µr_ =<br>�_T_<br>_t_=1<br>_√_<br>(_xj,t−xi,t_)<sup>2</sup>+(_yj,t−yi,t_)<sup>2</sup><br>_~~√~~_<br>(_xj,t−xk,t_)<sup>2</sup>+(_yj,t−yk,t_)<sup>2</sup><br>_T_<br>_j_ = arg min<br>_j∈O_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup><br>_k_ = arg min<br>_k∈D_<br>~~�~~<br>(_xk,t −xi,t_)<sup>2 </sup>+ (_yk,t −yi,t_)<sup>2</sup>|
|`RAT-VAR`|Variance of the ratio of the dis-<br>tance<br>to<br>the<br>nearest<br>ofensive<br>player and the distance from the<br>nearest ofensive player to the<br>nearest defensive player _k_|�_T_<br>_t_=1<sup>(</sup><br>_√_<br>(_xj,t−xi,t_)<sup>2</sup>+(_yj,t−yi,t_)<sup>2</sup><br>_~~√~~_<br>(_xj,t−xk,t_)<sup>2</sup>+(_yj,t−yk,t_)<sup>2</sup> <sup>_−µr_)2</sup><br>_T_<br>,<br>_j_ = arg min<br>_j∈O_<br>~~�~~<br>(_xj,t −xi,t_)<sup>2 </sup>+ (_yj,t −yi,t_)<sup>2</sup><br>_k_ = arg min<br>_k∈D_<br>~~�~~<br>(_xk,t −xi,t_)<sup>2 </sup>+ (_yk,t −yi,t_)<sup>2</sup>|



**Table 1:** Features describing the movement of defensive backs in pass coverage. 

From the features we generate, we would expect the two ratio ( `RAT-X` ) features to be most helpful in determining man vs. zone coverage, because in man coverage we would expect the defensive back to follow the offensive player he is covering very closely, whereas in zone coverage this is not necessarily true. Since there is generally a “hard” assignment 

9 

for each defender in man coverage (i.e. each defender has a specific player to cover), the ratio of the distance from the cornerback to the closest offensive player, to the distance from cornerback’s closest teammate to the same offensive player should be fairly small. That is, we expect the cornerback in man coverage to have a very small distance to his assignment, and any of the other remaining defenders to have a comparably larger distance to that player. We compute this value throughout the course of the play, and summarize those values with five quantities: the mean and variance of this value, in order to summarize the changes in this value throughout the play; the value of this quantity at the snap; at the time the ball is thrown; and at the mid-point between these two timepoints. 

Furthermore, another feature we expect to differentiate coverage types is the `OFF` ~~`D`~~ `IR` ~~`V`~~ `AR` and `OFF` ~~`D`~~ `IR MEAN` . This is because, similar to the above logic, a player in man coverage would be following their assignment around the field and would be much more “reactive” to the motion of the offensive player. Hence we would expect the direction of motion to be almost the same as their assignment throughout the course of the play. For a player in zone coverage, they are generally watching the quarterback rather than watching a receiver, and thus their motion might be more static, so that the difference in the direction of motion to the nearest offensive player would both be different and would have more variance. 

### **3.3 Mixture Models** 

Clustering is the process of partitioning observations in a dataset into groups without respect to some response variable (Hartigan, 1975). Often, this process is referred to as “unsupervised learning,” since clustering models can be used to assign labels for discrete groups without training data. 

Mixture modeling, or model-based clustering, is a type of clustering algorithm that fits a mixture of probability density functions to a dataset, where each density is representative of a single group or cluster. A mixture model can be written in the form: 



where _g_ indexes over the groups (or clusters) of the mixture model), _fg_ ( _x|ρg_ ) represents the density for group _g_ with parameters _ρg_ , and _f_ ( _x_ ) is the overall mixture distribution. 

Commonly, Gaussian mixtures (with _fg_ representing a Gaussian probability density function) are used because of their ease of implementation and theoretical properties. That said, any parametric distribution (or mixture of parametric distributions) can be used (Banfield and Raftery, 1993). The choice of _G_ is left to the user, and is commonly determined by searching over a range of possible values and determining the best with an evaluative measure like the Bayesian Information Criterion (BIC), though many methods for doing this exist. We direct interested readers to McNicholas (2016) for a complete overview of modelbased clustering and the related literature. 

In this paper, we use Gaussian mixture modeling with the features described in Section 3.2 to provide a model distinguishing man coverage from zone coverage. We take _fg_ to be Gaussian densities, and we test several different values of _G_ , with results provided in Section 

10 

4. For the remainder of this paper, we refer to our Gaussian mixture modeling approach as GMM. 

There are two key benefits to using mixture models, for our purposes. First, mixture models yield “soft” cluster assignments (i.e. probabilistic labels for each cluster), allowing us to quantify how certain we are when assigning man coverage or zone coverage labels. Second, mixture models are density-based, statistical models that estimate a empirical probability distribution from real data. As such, they come with several helpful properties. First, this allows us to characterize the resulting clusters in informative ways. For example, we can describe the _k_ -dimensional centroid of each cluster, or the values of each feature that correspond to the center of each cluster. In the context of our problem, this allows us to describe how each of our features distinguish man vs. zone coverage. Second, we can obtain cluster membership probabilities from the mixture model for _any_ observation, including data from a holdout set of data. In the context of football, this means that we can use our mixture model to make man vs. zone predictions for each defensive back on each play in real-time throughout the course of a football game, even though this game as not included in the data on which we estimated the model. Third, the probabilistic cluster labels allow us to provide an extensive evaluation of the clustering results, as we demonstrate later. 

### **3.4 Evaluation of Clustering Results with Cross-Validation** 

Many approaches exist for evaluating clustering results, but there is no “ground truth” data to which we can compare our clustering results. Moreover, even if an extensive set of labels existed, Hennig (2013) points out that “The fact that we know certain true classes doesn’t preclude other legitimate, or ‘true’ clusterings ... There could be better truths than the known one.” In other words, Hennig argues that clustering results should not always be evaluated against a set of ground truth labels, but by a critical evaluation of the model itself, and the features used to estimate the model. We take this approach below for choosing the number of clusters _G_ (Section 3.5) and assessing the influence of features (Section 3.6). 

We utilize the fact GMMs are fitting a statistical model for which we can generate (i.e. predict) cluster labels for data points to evaluate our clustering results. We use “leave-oneweek-out” cross-validation (LOWO CV) to compare test set partitions from mixture models fit on training data versus test data. For each week _k ∈{_ 1 _, . . . , K}_ ), we proceed as follows: 

1. fit GMM on training data _f_<sup>ˆtrain</sup> using weeks _{_ 1 _, . . . , K}\{k}_ , 

2. fit GMM on test data _f_<sup>ˆtest</sup> using week _{k}_ , 

3. create partitions _p_<sup>_train_</sup> _k_ and _p_<sup>_test_</sup> _k_ , using _f_<sup>ˆtrain</sup> and _f_<sup>ˆtest</sup> respectively, for each observation in holdout week _k_ by assigning cluster labels: 

   - let _f_<sup>ˆ</sup><sup>_∗_</sup> denote an arbitary GMM (either _f_<sup>ˆtrain</sup> or _f_<sup>ˆtest</sup> ), 

   - for a given point _x ∈_ R<sup>_d_</sup> , obtain the probability density from the estimated mixture density _f_<sup>ˆ</sup> _g_<sup>_∗_foreachlabel</sup><sup>_g_,</sup> 

   - compute _P_ ( _G_ ( _x_ ) = _g_ ) = _f_ ˆ _<u>g</u>_<sup>_∗_</sup><sup><u>(</u></sup><sup>_x_</sup><sup><u>)</u>where</sup><sup>_G_(</sup><sup>_x_)indicatesthelabelof</sup><sup>_x_,</sup> <u>�</u> _g_<sup>_f_ˆ</sup> _g_<sup>_∗_(</sup><sup>_x_),</sup> 

   - assign cluster label for _x_ with _g_<sup>_∗_</sup> = arg max _g P_ ( _G_ ( _x_ ) = _g_ ). 

11 

4. compare GMMs as a function of their holdout week partitions _hk_ ( _p_<sup>_train_</sup> _k , p_<sup>_test_</sup> _k_ ). 

For our purposes, we consider _h_ to be a function of pair agreements between the respective holdout partitions (i.e. for a given GMM _f_<sup>ˆ</sup><sup>_∗_</sup> do points _xi_ and _xj_ have same or different cluster label?). Following Steinley (2004), our notation for the pair agreements between our holdout partitions of interest _p_<sup>_train_</sup> _k_ and _p_<sup>_test_</sup> _k_ is presented in Table 2. A simple comparison is to use the Rand index (Rand, 1971, RI), which is just the ratio of pair agreements to the total number of pairs, RI _k_ ( _p_<sup>_train_</sup> _k , p_<sup>_test_</sup> _k_ ) =<sup>_<u>A</u>_</sup> _N_<sup><u>+</u></sup><sup>_<u>D</u>_,where</sup><sup>_N_=</sup><sup>_A_+</sup><sup>_B_+</sup><sup>_C_+</sup><sup>_D_.However,sincethe</sup> RI value can be inflated due to chance agreement we use the adjusted Rand Index (Hubert and Arabie, 1985, ARI) as our function _h_ compare holdout partitions, 



Under completely random partitions E[ARI _k_ ( _p_<sup>_train_</sup> _k , p_<sup>_test_</sup> _k_ )] = 0. This establishes an appropriate baseline for evaluating our clustering results, with _ARI_ ( _p_<sup>_train_</sup> _k , p_<sup>_test_</sup> _k_ ) _<_ 0 indicating that our GMMs fit separately on training versus test data are leading to worse than random cluster labels. Observing the maximum value of 1 indicates that the two holdout partitions being compared are identical to each other. Thus, we seek to fit GMMs that maximize ARI _k_ ( _p_<sup>_train_</sup> _k , p_<sup>_test_</sup> _k_ ) indicating a detection of clustering structure that is in agreement in both the training and test weeks of our LOWO CV procedure. While we compare two separate GMMs fit on the training and test data, one could replace either GMM above with any labeling process (e.g. expert labels of coverage). We direct readers to Steinley (2004) for an assessment of the properties of ARI, such as its advantage over the use of misclassification rate when the number of cluster labels equals the number of “true” labels. 

**Table 2:** Notation for the cross-tabulation of observation pairs from holdout partitions _p_<sup>_train_</sup> _k_ (rows) and _p_<sup>_test_</sup> _k_ (columns). 

||_p_<sup>_test_</sup><br>_k_<br>- same label|_p_<sup>_test_</sup><br>_k_<br>- diferent label|
|---|---|---|
|_p_<sup>_train_</sup><br>_k_<br>- same label|A|B|
|_p_<sup>_train_</sup><br>_k_<br>- diferent label|C|D|



### **3.5 Determining Number of Clusters** 

We choose the number of clusters _G_ using the LOWO CV procedure presented in Section 3.4. For each _G_ = 2 _, . . . ,_ 9, we apply the LOWO CV procedure, resulting in _K_ = 6 different ARI values, and compute the average across the holdout weeks: 



12 

We then pick the number of clusters yielding the highest average LOWO CV ARI across all weeks, _G_<sup>_∗_</sup> = arg max ARI _G_ . _G_ 

### **3.6 Assessment of Feature** 

Understanding the influence of different features in clustering and mixture models remains an open problem. A popular approach for GMMs casts the variable selection problem as a model-selection problem, greedily choosing which features to include based on BIC (Raftery and Dean, 2006) (see Fop and Murphy (2018) for an extensive review of variable selection for model-based clustering). Due to the number of features considered in Table 1, rather than implement a greedy search, we use our LOWO CV framework from Section 3.4 to measure each feature’s influence on the clustering results as follows for a fixed number of clusters _G_ : 

- _~~a~~ ll_ 

- 1. Compute average LOWO CV ARI using all features, ARI _G_<sup>_∗_,</sup> 

2. for each feature _m ∈{_ 1 _, . . . M }_ : 

   - ~~(~~ _−m_ ) 

   - (a) compute average LOWO CV ARI with feature _m_ removed, ARI _G_<sup>_∗_</sup> , 

   - (b) compute difference in average LOWO CV ARI with and without feature _m_ as a measure of its clustering influence: 



We then rank each feature by its LOWO CV _Influencem_ in Section 4.2, similar to feature importance plots commonly used for various supervised learning models. We interpret more positive values for _Influencem_ as indicating that the inclusion of feature _m_ leads to an improvement in the quality of the clustering results 

## **4 Results** 

We first assess the number of clusters in Section 4.1 and then the influence of each feature in improving the clustering results in Section 4.2, using the LOWO CV procedures explained in Sections 3.4-3.6. Next, we demonstrate the practical meaning of our approach and interpretation of results in the context of football. We closely examine several specific plays in Section 4.4, demonstrating how the predicted coverage type probabilities can change throughout the course of a play. We draw connections to common football strategies, and we explain why mixture models are ideal for this type of analysis. Finally, we provide an analysis of coverage types by player, team, and game situation (Section 4.3). 

For all results in this section, we apply the clustering models to only cornerbacks, since the features distinguishing the type of coverage by safeties should differ from those of cornerbacks. That said, the same process could be applied independently to safeties. All clustering results were generated using the `GaussianMixture` function in the Python `scikit-learn` library (Pedregosa et al., 2011), which uses the expectation-maximization (EM) algorithm to estimate the mixture model parameters. Due to the high degree of colinearity in our 

13 

feature space, we use an unconstrained “VVV” covariance structure when fitting the models (Banfield and Raftery, 1993). 

For the results in Sections 4.1, 4.2, and 4.3, we fit a mixture model using all features defined in Table 1 for all time periods defined in Figure 3 (i.e. each feature replicated over each of the five time periods). For the results in Sections 4.4 and 4.5, we fit mixture models separately for each time period, using only use the features available at the relevant time period of the play. 

### **4.1 Number of Clusters** _G_<sup>_∗_</sup> 

First, we determine the number of clusters _G_<sup>_∗_</sup> using the LOWO CV average ARI across the holdout weeks as explained in Section 3.5. As displayed in Figure 4, we found that _G_<sup>_∗_</sup> = 2 yields the highest value by a fairly wide margin, with an ARI over 0.9. This indicates that a two-cluster solution is the best fit for our data given our definition for evaluation in Section 3.4, which matches intuition in that there are primarily two types of cluster labels representing man and zone coverage. 



**Figure 4:** The ARI scores for the number of clusters from our features 

Because the mixture model’s clusters are completely data-driven, they do not come with common-sense labels like “man coverage” or “zone coverage”. Instead, we must make some determination of the type of coverage visually. We manually examined many animations of plays and determined whether each cornerback on each play was playing man, zone, or unknown coverage<sup>3</sup> . Using this information in conjunction with the cluster membership 

> 3In an appeal to our own authority, we note that the co-author who undertook this task has experience playing defensive back in high school football. 

14 

probabilities, it is fairly easy to tell which cluster corresponds to man coverage and which corresponds to zone coverage. We provide illustrations of how the coverage types can be visually distinguished throughout the course of a play in Section 4.4. 

### **4.2 Feature Influence on Clustering Results** 

We proceed to measure _Influencem_ for each of our considered features in Table 1 using the LOWO CV procedure explained Section 3.6. Figure 5 displays the top nine features in terms of the LOWO CV _Influencem_ . The majority of the top variables are measured before the ball is thrown, while the top feature is the variance in the difference of direction of motion between the player and the nearest offensive player after the ball is thrown. 



**Figure 5:** Top nine features by LOWO CV influence on clustering results (from bottom to top). 

### **4.3 Examining Soft Cluster Membership Probabilities** 

Figure 6 shows the distribution of predicted probabilities of membership in the “zone coverage” cluster from the mixture model. (The corresponding chart for man coverage, of course, is simply the reverse of Figure 6.) 

Here, we see similar distributions of cluster membership probabilities at different points throughout the play. Man coverage is more common the zone coverage, and the mixture model typically yields cluster membership probabilities near the extremes, indicating that the two coverage type clusters are well-separated. Before the ball is snapped, man coverage predictions are slightly more common than at other points throughout the play. As discussed in Section 4.4, this may relate to how teams disguise their coverage at the beginning of plays, and so there is less variation in the alignment of defenders before the ball is snapped. 

15 



**Figure 6:** Distribution of cluster membership probabilities for zone coverage cluster. 

### **4.4 Characterizing Pass Coverage Throughout Plays** 

In modern defensive schemes, teams may try to disguise their pass coverage at the start of the play, in order to confuse the opposing quarterback. Other schemes can involve a “read and react” approach to pass coverage, where specific coverage assignments depend on what happens at the start of the play. 

Interestingly, the mixture model does a good job of recognizing these scenarios. Coverage type probabilities often change substantially from the time of the snap to when the play has had a few seconds of “burn-in” time. Some examples are given below. In each of these examples, the offense is in red, and the defense is in blue. The arrows point to the players we focus on. 

In Figure 7, we can see the probabilities assigned to man and zone coverage at each frame throughout the play by the GMM. By the end of the play, the GMM predicts that Defense24 (top arrow) and Defense-20 (bottom arrow) to have been in zone coverage. We can see that they actually start out lined up as if they were going to play “press” coverage (a type of man coverage where the defensive back physically prevents the receiver from beginning his route at the start of the play), leading the GMM to predict both players to be playing man coverage with high probability. As the play develops, Defense-20 and Defense-24 do not 

16 



**Figure 7:** Play 3765 from Game ID 2017091000, with offense shown in red, and defense shown in blue. The play starts with the formation in the first frame and the ball is thrown in the last frame. The middle frame is exactly in between. In this case the top arrow points to player with jersey 24 (Defense-24) and the bottom to player with jersey 20 (Defense-20). 

17 

follow the men they initially lined up against and instead occupy their assigned zones. We see this change in the second and third frames, when they clearly are in zone coverage (as they are occupying a space rather than following another offensive player). The model reflects this with high probability. In this play, the defense was likely disguising their coverage type at the start of the play in an attempt to trick the quarterback into misreading the defense. Our mixture modeling approach quantifies this probabilistically as the play develops, until it is obvious that the defensive backs are actually playing zone coverage. 

In Figure 8, the offense is lined up with three receivers, and the defense does not line up in a way that indicates man coverage with high probability: Each of the players that we are tracking are lined up slightly farther away from the player they would be assigned to cover, possibly indicating that they are playing zone coverage. The GMM reflects this, cautiously predicting zone for Defense-23 ( _p_ = 0.8) and man for Defense-24 ( _p_ = 0.7). Before the ball is snapped, Defense-23 is lined up relatively far away from a corresponding offensive player, leading to the model’s prediction of zone coverage. Similar to the previously discussed play, this was likely an attempt by the defense to disguise the coverage scheme being used. As the play develops, however, we see that both defensive backs follow a specific offensive player until the ball is thrown, indicating that they were actually playing man coverage the whole time. This change in coverage type probability from thee GMM is reflected in the middle frame, as the probability of man coverage sharply rises for both players, and finishes in the final frame with high probabilities of man coverage for both players. 

In Figure 9, the offensive is lined up in a “shotgun” formation with four wide receivers, two on each side of the offensive line. Defense-21 and Defense 23 are playing relatively far from their closest receivers, while Defense-34 is relative close to his. The GMM predicts this starting formation to be man for each of the players, but with some uncertainty in the probabilities ( _p ≤_ 0 _._ 8 for each). As the play continues, Defense-21 and Defense-34 actually swap positions. In frame 1, Defense-34 is defending Offense-18, but as the play develops, we see that Defense-34 is in man coverage against Offense-88, who runs out from the offensive backfield. This unusual starting point and pattern of motion by Offense-88 leads to a reduced probability that Defense-34 is in man coverage according to the GMM. Defense-21 does not follow Offense-17 and instead occupies a zone in the middle frame, where his pattern of motion only slightly follows that of Offense-17. Finally, Defense-23 does not actually move much from his initial position at the start of the play, but Offense-81 runs a corner route towards his direction. Interestingly, the model gives about equal probability that Defense-23 is zone (54%) coverage and man (46%) coverage, because there is another defensive player nearby who might also be assigned to Offense-81. His lack of motion and the proximity of another defender is more common with zone coverage, but his proximity to Offense-81 and similar pattern of motion to that of Offense-81 indicates man coverage. Thus, the model gives a fairly uncertain prediction about his coverage type. This uncertainty is a positive feature of the mixture model: We should not assign hard cluster labels when it is unclear, even to the human eye, what type of coverage each player is playing. 

18 



**Figure 8:** Play 174 from Game ID 2017091004, with offense shown in red, and defense shown in blue. The play starts with the formation in the first frame and the ball is thrown in the last frame. The middle frame is exactly in between. In this case the top arrow points to player with jersey 24 (Defense-24) and the bottom arrow points to player with jersey 23 (Defense-23). 

19 



**Figure 9:** Play 1193 from Game ID 2017091713, with offense shown in red, and defense shown in blue. The play starts with the formation in the first frame and the ball is thrown in the last frame. The middle frame is exactly in between. In this case the top arrow points to player with jersey 34 (Defense-34), the middle arrow to player with jersey 21 (Defense-21), the bottom arrow points to player with jersey 23 (Defense-23) (in the first frame). In the last frame 21 and 34 swap20arrows. 



**Figure 10:** Probability motion is classified as Man 

### **4.5 Analysis of Coverage Types by Pattern of Motion, Player, Team, and Situation** 

Figures 10 and 11 show the patterns of motion of cornerbacks classified as playing man or zone coverage, respectively. Here, we see no apparent relationship between the patterns of motion and the probability of man or zone coverage. This makes sense in context, since the patterns of motion of cornerbacks are typically reactionary to what the opposing receiver is doing. This provided partial evidence that a trajectory clustering approach like that of Chu et al. (2019) or Miller and Bornn (2017) would not be appropriate for identifying coverage types of defensive backs. 

## **5 Discussion and Future Work** 

We present an unsupervised approach, using Gaussian mixture modeling, for identifying and annotating the type of pass coverage of cornerbacks during passing plays in the NFL, requiring no ground truth labels and minimal human oversight. We design a rich set of features that help distinguish between types of coverage and can be updated at each point during a play, and find that relate the direction of motion of the cornerback to that of the closest offensive players are most useful when separating “man coverage” from “zone coverage.” We use an out-of-sample prediction approach and find that a two-cluster solution (corresponding to man coverage and zone coverage) yields the best fit. We demonstrate how the mixture model’s probabilistic cluster assignments allow for interesting subsequent analyses, such as examining how pass coverage types evolve and become more obvious throughout the course of a play. 

We use Gaussian mixture modeling to address this problem, and find that the mixture 

21 



**Figure 11:** Probability motion is classified as Zone 

model’s flexibility, interpretability, and soft cluster assignments are more suitable for this problem. We demonstrate this with several case studies of specific plays, showcasing how our probabilistic coverage type assignments evolve throughout the course of a play in reaction to the on-field movements of cornerbacks in relation to other players on the field. We show how our model can be used to identify cases when defenses attempt to disguise their coverage types before the snap, before settling into patterns of motion common to the type of coverage they are playing as the play develops. 

We use an out-of-sample prediction approach and the well-studied adjusted Rand index to determine the appropriate number of clusters. Using this approach, we find that the twocluster solution yields the best ARIs, which conveniently matches our expectations given what we know about the dichotomy of coverage types in football to man and zone coverage. Furthermore, through manual review of animated example plays from each cluster, we assign “man” and “zone” labels to the groups identified by the two-cluster GMM solution. 

We use a similar approach to determine the utility of each feature in improving the clustering results. We find that the variability in the direction of motion of the cornerback relative to the nearest offensive player is the most important variable in improving the clustering results, as measured by the adjusted Rand index. We also find that other features examining the variability in the movement of the cornerback (in relation to offensive players or otherwise) are important in improving the clustering results. Interestingly, we find that comparing the directions of motion of the cornerback to his nearest teammate does little to improve the clustering results. 

The mixture model’s probabilistic cluster assignments are advantageous in the context of football, as we demonstrate through an examination of three plays. In particular, since modern defensive schemes involve disguising coverage types at the start of plays and reacting to what the offense is doing, we examine the GMM cluster membership probabilities at 

22 

different points throughout the course of a play, showing how these probabilities change in reaction to the patterns of motion of cornerbacks and their proximity to opposing receivers. 

We provide a brief analysis of coverage types by different game situations, though we acknowledge that there is more work to be done here. However, that encapsulates the primary purpose of this research: to provide additional annotations to NFL player and ball tracking data that will allow future researchers and NFL teams to explore interesting and innovative research problems. We look forward to seeing such new research. 

One limitation of our approach is that player orientation was not available in the data provided by the NFL via the 2019 Big Data Bowl. This is unfortunate, since this information would be helpful in distinguishing man vs. zone coverage for cornerbacks. NFL teams have access to this information at the frame-level, and they should be able to easily incorporate this into their feature set when replicating our mixture modeling approach internally. As an example, we propose a brief set of features involving the players’ orientations on the field that may help distinguish man vs. zone coverage. 

1. **Orientation of the defensive back relative to the line of scrimmage at different points throughout the play.** At the start of each play, cornerbacks typically face the line of scrimmage. As the play develops, cornerbacks in man coverage frequently turn their bodies while following the offensive player (e.g. wide receiver) that they are covering, while cornerbacks in zone coverage more frequently face the line of scrimmage, watching the quarterback’s actions as the play develops. One can design features around this idea. For example, the percentage of time that a cornerback is facing the line of scrimmage, the direction the cornerback is facing at the time the ball is thrown, etc. 

2. **Orientation of the cornerback relative to the corresponding offensive player at different points throughout the play.** As a passing play develops, cornerbacks in man coverage frequently mimic the on-field movements of the offensive player they are covering, so that the direction that they are facing on the field will closely match that of the offensive player. For cornerbacks in zone coverage, their orientation is more likely to deviate from the closest offensive player. One can design features around this idea. For example, one can compute the percentage of time throughout a play in which the two players facing the same direction (e.g. within some angle _θ <_ 45). 

These are just examples of how the feature set can be enriched with the addition of player orientation into the dataset. We encourage those with access to the full NFL player tracking data to explore these options and improve upon our feature set in their own work. 

Another limitation of our approach is addressing the correlation between the features considered. We emphasize that this is a first step in understanding the role of our constructed features in modeling defensive coverage, and leave further feature analysis, such as application of other model-based variable selection methods discussed in Fop and Murphy (2018), for future work. 

In future work, we apply this framework to analyzing the coverage types of safeties and, when appropriate, linebackers. We have briefly applied the framework to safeties in pass coverage as a proof-of-concept, and found that two coverage type clusters was the best fit, 

23 

though the size of the clusters were more disparate (most likely, safeties are playing zone coverage more than man coverage). However, a complete analysis of other positions would require the design of new features specific to the safety position and the patterns of motion of safeties in relation to their teammates and opponents. This task is left to future work. 

Additionally, we hope to examine using the coverage type of one player to help inform the coverage type prediction of another player. For example, knowing that the left cornerback is playing in man coverage could indicate that the right cornerback is likely also going to play man coverage; knowing that the safeties are playing “cover-2” might change our estimate of the probability that the cornerbacks are playing zone coverage. Additionally, incorporating team-specific features may help, since certain defensive coordinators may prefer certain defensive schemes against certain personnel packages. 

Finally, in future work, we hope to provide additional annotations of other on-field events (actions, coverage schemes, etc). The mixture modeling approach we use here should serve as a foundation for this future work, although a new set of features will need to be designed for each specific annotation problem. 

## **References** 

- Banfield, J. D. and A. E. Raftery (1993): “Model-based gaussian and non-gaussian clsutering,” _Biometrics_ , 49, 803–821, URL `https://www.stat.washington.edu/raftery/ Research/PDF/banfield1993.pdf` . 

- Bialkowski, A., P. Lucey, P. Carr, Y. Yue, S. Sridharan, and I. Matthews (2014): “Identifying team style in soccer using formations learned from spatiotemporal tracking data,” _2014 IEEE International Conference on Data Mining Workshop_ , 9–14. 

- Burke, B. (2018): “We created better pass-rusher and pass-blocker stats: How they work,” URL `http://www.espn.com/nfl/story/_/id/24892208/creating-better-nfl-passblocking-pass-rushing-stats-analytics-explainer-faq-how-work` . 

- Burke, B. (2019): “Deepqb: Deep learning with player tracking to quantify quarterback decision-making & performance,” URL `http://www.sloansportsconference.com/wpcontent/uploads/2019/02/DeepQB.pdf` . 

- Chu, D., L. Wu, M. Reyers, and J. Thomson (2019): “Routes to success,” _NFL Big Data Bowl_ , URL `https://danichusfu.github.io/files/Big_Data_Bowl.pdf` . 

- Fop, M. and T. B. Murphy (2018): “Variable selection methods for model-based clustering,” _Statist. Surv._ , 12, 18–65, URL `https://doi.org/10.1214/18-SS119` . 

- Gudmundsson, J. and M. Horton (2016): “Spatio-temporal analysis of team sports - A survey,” _CoRR_ , abs/1602.06994, URL `http://arxiv.org/abs/1602.06994` . 

- Hartigan, J. A. (1975): _Clustering Algorithms_ , New York, NY, USA: John Wiley & Sons, Inc., 99th edition. 

24 

- Hennig, C. (2013): “Measurement of quality in cluster analysis,” URL `http://www. homepages.ucl.ac.uk/~ucakche/presentations/cqualitybolognahennig.pdf` . 

- Hubert, L. and P. Arabie (1985): “Comparing partitions,” _Journal of Classification_ , 2, 193– 218, URL `https://doi.org/10.1007/BF01908075` . 

- Lucey, P., A. Bialkowski, P. Carr, Y. Yue, and I. Matthews (2014): ““how to get an open shot”: Analyzing team movement in basketball using tracking data,” _MIT Sloan_ . 

- McNicholas, P. D. (2016): “Model-based clustering,” _Journal of Classification_ , 33, 331–373, URL `https://doi.org/10.1007/s00357-016-9211-9` . 

- Miller, A. C. and L. Bornn (2017): “Possession sketches: Mapping nba strategies,” _MIT Sloan Sports Analytics Conference_ , URL `http://www.lukebornn.com/papers/miller_ ssac_2017.pdf` . 

- Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay (2011): “Scikit-learn: Machine learning in Python,” _Journal of Machine Learning Research_ , 12, 2825–2830. 

- Raftery, A. E. and N. Dean (2006): “Variable selection for model-based clustering,” _Journal of the American Statistical Association_ , 101, 168–178, URL `https://doi.org/10.1198/ 016214506000000113` . 

- Rand, W. M. (1971): “Objective criteria for the evaluation of clustering methods,” _Journal of the American Statistical Association_ , 66, 846–850. 

- Steinley, D. (2004): “Properties of the hubert-arabie adjusted rand index,” _Psychological Methods_ , 9, 386–396. 

## **6 Appendix** 

Figure 12 shows the proportion of cornerback coverages in man (blue) and zone (orange) by quarter. While some small differences exist in the first four quarters, they are mostly negligible, meaning we see no apparent trend in the type of coverage throughout the game. Interestingly, we see an increase in man coverage in overtime. However, this result is not statistically significant, since there were only 40 overtime plays in our dataset from the first six weeks of the 2017 season. This brief analysis does not control for factors like the score differential or opposing offensive formation, which may influence coverage type. 

Figures 14 and 15 show the top-10 teams by proportion of zone and man coverage, respectively. Tampa Bay, Chicago, and Green Bay have the highest rate man coverage play during this short span of six weeks, while Washington, Buffalo, and the New York Giants have the highest rate of zone coverage. Overall, man coverage is used more often than zone coverage by all 32 NFL teams in this provided sample of data. 

25 



**Figure 12:** Man:Zone Percentage by Quarter 

Finally, Figure 16 and 17 show the top-10 cornerbacks by their proportion of man and zone coverage, respectively (minimum 50 coverages). Bryce Callahan from the Chicago Bears led the NFL in percentage of man coverages during the first six weeks of the 2017 season with almost 80%, followed by Damarious Randall, Kevin King, Phillip Gaines, and others. Joshua Shaw, who played for the Bengals in 2017, led the league in percentage of zone coverages, with about 60%, followed by Janoris Jenkins, Bobby McCaine, Marcus Peters, and others. Figure 13 shows no apparent relationship between the down and the coverage type of cornerbacks. 

26 



**Figure 13:** Man:Zone Percentage by Down 



**Figure 14:** Top 10 teams with the highest Zone Coverage percentage 

27 



**Figure 15:** Top 10 teams with the highest Man Coverage percentage 



**Figure 16:** Top 10 players with the highest Man Coverage percentage 

28 



**Figure 17:** Top 10 players with the highest Zone Coverage percentage 

29 


