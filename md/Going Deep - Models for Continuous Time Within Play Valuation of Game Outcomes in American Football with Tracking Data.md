<!-- source: Going Deep - Models for Continuous Time Within Play Valuation of Game Outcomes in American Football with Tracking Data.pdf -->

# **Going Deep: Models for Continuous-Time Within-Play Valuation of Game Outcomes in American Football with Tracking Data** 

Ronald Yurko, Francesca Matano, Lee F. Richardson, Nicholas Granered, Taylor Pospisil, Konstantinos Pelechrinis, Samuel L. Ventura 

November 3, 2019 

##### **Abstract** 

Continuous-time assessments of game outcomes in sports have become increasingly common, complex, and important in the last decade. But in American football, only discrete-time estimates of the value of plays and game situations were possible until recently, since the most advanced public football datasets were recorded at the play-by-play level. While measures such as expected points and win probability are useful for evaluating football plays and game situations, there has been no research into how these values change throughout the course of a play. In this work, we make two main contributions: First, we provide a general framework for continuoustime within-play valuation in the National Football League (NFL) using the NFL’s Next Gen Stats player and ball tracking data. Our framework incorporates several modular sub-models, so that other recent work involving player tracking data in football can be easily incorporated into our framework. Second, we construct a _ball-carrier model_ . The ball-carrier model estimates how many yards the ball-carrier will gain from their current position, conditional on the locations and trajectories of the ball-carrier, their teammates, and their opponents. We test several modeling approaches for the ball-carrier model, and ultimately find that a long short-term memory (LSTM) recurrent neural network outperforms alternative approaches. For each moment of 

1 

each play, we use the LSTM to continuously update the ball-carrier model, and we use this estimate to determine the estimated end-of-play yard line. Then, we use the estimated end-of-play yard line as input to a between-play model for game situation value, such as the expected points or win probability added models from Yurko et al. (2019). This yields an estimate of within-play value in these terms. Our research has several key benefits: The framework is adaptable, so that any measure of play value (or any model for expected points or win probability) can be used. The framework is modular, so that (for example) existing models for pass attempt outcomes or quarterback decision-making can be applied within this framework. Finally, the fully-implemented framework will allow for continuous-time assessment of all 22 players on the field, which was never before possible at such a granular level. 

_Keywords:_ football, recurrent neural networks, expected points, win probability, player tracking data. 

## **1 Introduction** 

Quantitative analyses of sports have become increasingly complex in the last decade, mostly due to the advent of player and object tracking data across most major sports. Tracking data captures the position and trajectory of the athletes and objects of interest (e.g. balls, pucks, etc) on the playing surface for a given sport. Statistical analysis of tracking data in sports has been an increasingly popular area of research in recent years; we encourage interested readers to read the review paper on this topic from Gudmundsson and Horton (2016) for a detailed summary of the work in this area. 

In this work, we focus on a particular but important area of player tracking data analysis: Continuous-time valuation of game outcomes – in our case, for American football. Figure 1 provides a visual representation of what we look to achieve in this paper: Providing continuous-time, within-play valuations of football game outcomes. The Figure shows how the expected points (A) and win probability (B) change continuously in reaction to on-field events throughout the course of a 47-yard touchdown run by Cordarrelle Patterson. 

Below, we provide a brief overview of discrete-time valuation of game outcomes in football, continuous-time valuation of game outcomes in all sports, and continuous-time valuation of game outcomes in football specifically. 

2 



Figure 1: The change in (A) expected points and (B) win probability during Cordarrelle Patterson’s 47 yard TD run. 

### **1.1 Previous Work: Discrete-Time (Play-by-Play) Evaluation of Football Game Outcomes** 

Commonly, there are two classes of models for discrete-time evaluation of game outcomes in football: models for _expected points_ , and models for _win probability_ . Models for expected points seek to answer the question: How many points is the current game situation worth, in expectation, conditional on the features of that game situation (e.g. down, distance, yard line, score differential, time remaining, etc)? Models for win probability ask a fundamentally different question: How likely is it that the possession team will win the game, conditional on the features of that game situation (e.g. down, distance, yard line, score differential, time remaining, etc)? Yurko et al. (2019) provide an overview of these play-valuation frameworks, including a review of prior approaches for building these models, new approaches for building these models, and examples of how these models 

3 

and their derived metrics can be used to evaluate individual players and teams. We point interested readers to this work for a complete overview. These models are typically estimated at the play-by-play level ( _between plays_ ), since this is the finest level of granularity at which datasets are available. However, there has been no work to-date studying how valuation of football game outcomes evolves _within plays_ . 

### **1.2 Previous Work: Continuous-Time Models for Game Outcomes in Sports** 

Although tracking data is not _technically_ collected in continuous-time – most systems track the locations and trajectories of athletes and objects of interest at rates of 10 to 25 Hz – it is fundamentally different from play-by-play or event-level datasets. In particular, the unit of interest in play-by-play or event-level data is a single (discrete) play or event, while the units of interest in tracking data are the continuously changing locations and trajectories of players and objects on the playing surface. 

Using tracking data, several approaches exist for continuous-time modeling of game outcomes in sports. In basketball, Cervone et al. (2014) and Cervone et al. (2016) provide models for _expected possession value_ (EPV), which is a continuous-time estimate of expected points scored by the team in possession during a single basketball possession, conditional on the locations and trajectories of players (and the ball). The authors use a two-level Markov chain approach to do this. First, they model the competing hazards of (discrete) possession-changing events (e.g. passes, shot attempts, turnovers). Second, they model (continuous) player movement on the court. These two models, each of which condition on the locations and trajectories of the players and the ball, are combined hierarchically to estimate EPV at each moment. 

In soccer, Link et al. (2016) quantifies the performance of attacking teams in terms of their probability of scoring. The authors provide continuously updating estimates of the probability of a goal being scored at each moment throughout the course of a possession. Fern´andez et al. (2019) use deep learning to estimate EPV in soccer. They take a multi-level approach similar to Cervone et al. (2016), where discrete-time estimates of “expected goals” (describing the likelihood of a shot resulting in a goal, if taken), “passing value” (describing the value, in terms of expected goals, of a pass), and “drive value” (describing the value, in terms of expected goals, of a drive to the net) are combined with continuous-time estimates 

4 

of action likelihood (shot, pass, or drive) to provide an overall, continuous-time measure of EPV. Each of the sub-models in this approach conditions on the locations and trajectories of the players and the ball. 

Observant readers will note several similarities between our approach and the approaches of Cervone et al. (2016) and Fern´andez et al. (2019): combining discrete-time and continuous-time models, continuously estimating the value of game outcomes within plays, and using the resulting metrics to quantify the value added of individual athletes. 

### **1.3 Previous Work: Continuous-Time Models for Football** 

In December 2018, the National Football League (NFL) temporarily made public a subset of player and ball-tracking data from Weeks 1-6 of the 2017 season for its inaugural “Big Data Bowl” competition. Although the data has since been taken down, several authors have contributed interesting work to the literature using this data. 

Burke (2019) uses a deep learning approach to model outcomes of the passing game. In different variants of this model, the author uses DeepQB to model each receiver’s target probability, the pass outcome probability (complete, incomplete, interception), and the expected yards gained. Each of these variants of DeepQB can be incorporated into the general framework for within-play valuation of game outcomes that we provide in this paper. 

Deshpande and Evans (2019) provide innovative statistical models for the hypothetical completion probability of a pass. The authors use counterfactual analysis of within-play features to impute upstream and downstream features like the time at which the ball will arrive to the targeted receiver. This model can also be incorporated into the general framework for within-play valuation of game outcomes that we provide in this paper. 

Several other authors have undertaken interesting research topics using the NFL-provided tracking data. For example, Chu et al. (2019) use mixture modeling to automatically identify, cluster, and characterize route types of receivers. Similarly, Sterken (2019) use a convolutional neural network to classify the route types of receivers. Dutta et al. (2019) use clustering models to provide unsupervised, probabilistic annotations for the coverage type of defensive backs. Haar (2019) provides an exploratory analysis of NFL passing plays. These works all involve improving upon the existing league-provided tracking data by providing additional information that can be estimated from the underlying player locations and trajectories. However, they do not attempt to model game outcomes, so they 

5 

are of limited relevance to this paper. 

### **1.4 Our Contributions** 

Our paper makes two main contributions. First, we provide a general framework for continuous-time within-play valuation of game outcomes in the NFL, using the league-provided tracking data. Our framework, described in Section 3, incorporates several modular sub-models, so that the recent work involving player tracking data in football described above can be easily incorporated into our framework. 

Second, we construct a novel _ball-carrier model_ , which estimates the yards gained from a ball-carrier’s current position (and thus, the end-of-play yard line), conditional on the locations and trajectories of the ball-carrier, their teammates, and their opponents. We find that long short-term memory (LSTM) recurrent neural networks outperform alternative approaches for this modeling task. 

We update the predictions from the LSTM at each frame of the tracking data to continuously update our estimate of the yards gained from the ball-carrier’s current position, and we use the corresponding estimated end-of-play yard line as input to the discrete-time (between play) models for game situation value (expected points and win probability) from Yurko et al. (2019). As a result, we obtain a continuous-time estimate of within-play value in terms of expected points and/or win probability on rushing plays. We provide examples of these withinplay valuations of game outcomes in Section 5, and we demonstrate how changes in within-play valuations of game outcomes can be used for player evaluation. 

Our research has several key benefits: First, the framework is adaptable, so that measure of play value (or any model for expected points or win probability) can be used. Second, the framework is modular, so that (for example) any model for pass attempt outcomes or quarterback decision-making can be substituted into this framework in place of the approach we use here. For example, one could use the models from Burke (2019) or Deshpande and Evans (2019) in the appropriate places of the framework described in Section 3. Finally, the fully-implemented framework will allow for continuous-time assessment of offball player movement, quarterback decision-making, ball-carrier value added, receiver value added, blocking value added, defensive player value added, and many other evaluative tools that were never before possible at such a granular level. 

6 

## **2 Player and Ball Tracking Data** 

In December 2018, the NFL became the first North American professional sports league to release a portion of their tracking data to the public when temporarily made available a subset of this data from Weeks 1-6 of the 2017 season for the inaugural “Big Data Bowl” competition.<sup>1</sup> 

The NFL’s tracking data collected as follows: Two radio frequency identification (RFID) chips are placed in each player’s shoulder pads (and in the ball). The RFID chips emit a signal to sensors in each stadium, which triangulate the location of the chip on the field. The data is collected at a rate of 10 Hz, so that the on-field location, speed, and angle of each player (and the ball) is recorded 10 times per second. Event annotations (e.g. ball snapped, first contact, pass thrown, etc) are recorded by the NFL for each play. In total, the dataset contains 1,075,720 unique frames (not counting frames separately for each player and ball) across 14,167 plays, each of which records the locations and trajectories (speed, angle) of all 22 players (and the ball) on the field. 

Table 1 shows an example of this data for a 47 yard TD run by WR Cordarrelle Patterson, which occurred in a Week 6 game between the Los Angeles Chargers and Oakland Raiders in 2017. Four frames from this play are displayed in Figure 2 displaying the coordinates of the offense (blue), defense (orange), and the ballcarrier (black) at particular events in the play. 

Table 1: Example of tracking data for Cordarrelle Patterson’s 47 yard TD run. 

|frame.id|x|y|s|dir|event|displayName|
|---|---|---|---|---|---|---|
|24|60.64|29.70|7.55|175.34|handoff|Cordarrelle Patterson|
|25|60.77|28.94|7.61|177.10|NA|Cordarrelle Patterson|
|...|...|...|...|...|...|...|
|44|55.20|14.62|8.92|226.45|frst<br>~~c~~ontact|Cordarrelle Patterson|
|...|...|...|...|...|...|...|



This data can easily be joined to existing play-by-play data from the NFL’s API (e.g. via the `nflscrapR` package), which contains additional information about each play (Horowitz et al., 2017). For the models in Section 4, we identified all ball-carrier sequences for running plays, which includes designed runs 

> 1The NFL ran a separate competition involving analyzing tracking data for punts. However, the data made available for this competition only covered punt plays, and thus is not relevant for this paper. 

7 



Figure 2: A display of the tracking data for Cordarrelle Patterson’s 47 yard TD run with the offense (blue), defense (orange), and ball-carrier (black) at (A) snap, (B) handoff, (C) first contact, and (D) crossing the endzone. 

and QB scrambles. While the tracking data records the location of the ball in addition to the players, it does not identify who is the ball-carrier for a particular frame. We first identified the ball-carriers for every type of play (pass attempts, runs, returns, etc.) based on the information available from the NFL’s API via `nflscrapR` , which denotes who was directly involved in each play. Given the roles a player can have (passer, runner, receiver, interceptor, or returner), we used the provided event annotations to determine when a player became the ball-carrier. Since we focus our attention on running plays in this manuscript, we identify the beginning of the ball-carrier sequence when the runner received the ball by either a handoff, lateral, or direct snap (all snaps included for QB runs). The end of the ball-carrier sequence was marked when either the player was tackled, ran out of bounds, fumbled, or scored a touchdown. We excluded all plays missing the necessary information from the NFL API, as well as plays where the snap of the play was missing in the tracking data, and any ball-carrier sequences where either the starting or ending events were missing. After further pre-processing for the covariates described in Section 4, our final modeling dataset consisted of 153,184 

8 

frames from 4,447 unique ball-carrier sequences on running plays. Figure 3(A) displays the distribution for the length of ball-carrier sequences, revealing that majority of ball-carrier sequences are between two to five seconds in length, while Figure 3(B) displays the observed change in field position from the ball-carrier’s current location that will be modeled as discussed in 3.4. 



Figure 3: Distributions of the (A) length of the ball-carrier sequences in the modeling dataset, and (B) the observed change in yards from the ball-carrier’s location at the current frame with respect to the target endzone. 

## **3 A Framework for Continuous-Time Play Value in Football** 

Our approach for providing continuous-time within-play valuations involves several key pieces, which we combine via the framework presented in Section 3.3. 

9 

We first discuss models for evaluating game situations at a discrete level between each play (Section 3.2). Next, we describe several sub-models for computing various within-play quantities that comprise the rest of our within-play valuation framework: A ball-carrier model (Section 3.4), a quarterback decision model (Section 3.5), a target probability model (Section 3.6), an incompletion probability model (Section 3.7), and a catch probability model (Section 3.8). 

### **3.1 Notation** 

Here, we summarize the notation used in the rest of this section, for easy reference. 

- Let _t >_ 0 be some time between the start (i.e. the snap) and end of a play 

- Let _Y_ be a random variable representing the yards gained from the ballcarrier’s current position on the field, and _Y_<sup>_∗_</sup> be the corresponding end-ofplay yard line 

- Let _Xt_ be a data structure representing the locations and trajectories of all players and the ball from the start of the play until time _t_ 

- Let F( _Xt_ ) be some filtration of the locations and trajectories of all players and the ball from the start of the play until time _t_ , borrowing notation from Cervone et al. (2016) 

- Let _E_ ( _Yi|_ F _carry_ ( _Xt,i_ )) be the expected yards gained from the ball-carrier’s current position, and _E_ ( _Yi_<sup>_∗|_F</sup><sup>_carry_(</sup><sup>_Xt,i_)) be the corresponding expected end-</sup> of-play yard line 

- Let _Tj,i_ be a binary random variable describing whether receiver _j_ was targeted ( _Tj,i_ = 1) or not ( _Tj,i_ = 0) on play _i_ 

- Let _Ii_ be a binary random variable describing whether a pass on play _i_ is incomplete ( _Ii_ = 1) or caught by an offensive or defensive player ( _Ii_ = 0) 

- Let _Ck,i_ be a binary random variable describing whether player _k_ caught the ball ( _Ck,i_ = 1) or not ( _Ck,i_ = 0), where _k_ represents one of the 16 players who can catch a pass (five eligible offensive receivers and 11 defenders) 

- Let _P_ ( _Di_ = _dk|_ F _decision_ ( _Xt,i_ )) be a probability mass function over the set of decisions a QB can make: _{d_ 1 = throw away _, d_ 2 = run/sack _, d_ 3 = pass _}_ 

10 

- Let _P_ ( _Tj,i|_ F _pass_ ( _Xt,i_ ) _, Di_ = Pass) be a probability mass function describing the likelihood that a receiver is targeted on play _i_ 

- Let _P_ ( _Ii|_ F _inc_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1) be a probability mass function describing the outcome (incomplete or caught) of a pass on play _i_ targeted to receiver _j_ 

- Let _P_ ( _Ck,i|_ F _catch_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1 _, Ii_ = 0) be a probability mass function describing whether player _k_ caught the ball ( _Ck,i_ = 1) or not ( _Ck,i_ = 0) 

### **3.2 Estimating Between-Play Value** 

In Section 1.1, we described prior approaches for estimating between-play value in football. Here, we posit that no additional information from the tracking data described in Section 2 will influence the _between-play_ valuations of a football game, regardless of which model for between-play valuation is used. That is, the value of a game situation between when the previous play ends and the next play begins is a function of _only_ the factors that are observable between plays (e.g. down, yards to go, yard line, score, time remaining, timeouts remaining, etc); these values are conditionally independent of any information that can be gathered from within-play tracking data. 

Intuitively, this makes sense: If the home team has possession of the ball on 3rd down with 2 yards to go at the opponent’s 26 yard line, we should assign the same value to that situation regardless of how they got to that point (e.g. via a lucky catch in the middle of the field vs. an open catch near the sideline). 

Because of this, it is not necessary to develop new models for between-play value using tracking data. One benefit of this is that any model for betweenplay value can be substituted into this piece of our framework, without affecting any other piece of the framework. For the remainder of this paper, we use the expected points and win probability models from Yurko et al. (2019) for this purpose, since they are reproducible, publicly available, well-calibrated, and interpretable in terms of game outcomes. 

### **3.3 Framework for Continuous-Time Play Value** 

Given an appropriate model for between-play value, our goal is now to model the features that are used as input to the between-play model. From Yurko et al. (2019), these features include the down, yard line, yards to go, score differential, 

11 

and other minor factors.<sup>2</sup> We notice that the down, yard line, yards to go, and score differential on play _i_ + 1 are each functions of the yard line at which the play _i_ ended. As such, in order to update the estimates of between-play value, we _only_ need to estimate the yard line at which the current play ends, and then update the other between-play variables accordingly. 

Our framework for providing continuously-updating within-play valuations is organized as follows: 

**Rushing Plays** : Model the expected yards gained from the ball-carrier’s current position, _E_ ( _Yi|_ F _carry_ ( _Xt,i_ )) 

- Obtain the associated expected end-of-play yard line, _E_ ( _Yi_<sup>_∗|_F</sup><sup>_carry_(</sup><sup>_Xt,i_)),</sup> through linearity of expectations ( _Y ∗_ = _Y_ + [player’s current yard line]) 

- Use this quantity as input into the chosen play value model from Section 3.2, along with common-sense updates to other covariates used in the play value model (e.g. increment the down or reset it to 1, adjust the time remaining, update the score, etc) at the end of the play.<sup>3</sup> 

**Passing Plays** : Model the QB’s decision probabilities, _P_ ( _Di|_ F _decision_ ( _Xt,i_ )) 

#### • _Di_ = **Throw Ball Away** : 

- The play ends at the play’s original yard line 

- Update the covariates for the play value model accordingly (e.g. increment the down, adjust the time remaining) 

#### • _Di_ = **Run / Sack** : 

   - Use the ball-carrier model 

   - Follow the same procedure used for rushing plays 

- _Di_ = **Pass** : Model _P_ ( _Tj,i_ = 1 _|_ F _pass_ ( _Xt,i_ ) _, Di_ = Pass), each receiver’s target probability on play _i_ 

2Other factors may include the time remaining, which can be estimated using common-sense methods; the timeouts remaining for each team, which do not change within plays; and indicators that are direct functions of the yard line or the time remaining. 

> 3For simplicity, we do not model rare events like fumbles or laterals within the ball-carrier model. This is discussed in depth in Section 6. 

12 

- Normalize these probabilities at each time _t_<sup>4</sup> 

- **For each receiver** _j_ : Model _P_ ( _Ii_ = 1 _|_ F _inc_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1), the incompletion probability of a pass on play _i_ 

   - <sup>**Incomplete**:Theplayends;updatethecovariatesfortheplay</sup> value model accordingly (e.g. increment the down, adjust the time remaining, maintain same yard line) 

   - <sup>**Caught**:Model</sup><sup>_P_(</sup><sup>_C_</sup> _k_<sup>= 1</sup><sup>_|_F</sup> _catch_<sup>(</sup><sup>_X_</sup> _t,i_<sup>)</sup><sup>_,D_</sup> _i_<sup>= Pass</sup><sup>_,T_</sup> _j_<sup>= 1</sup><sup>_,I_</sup> _i_<sup>= 0),</sup> for _k_ as each of the 5 offensive receivers and 11 defenders 

      - Normalize to 1 _− P_ ( _Ii_ = 1 _|_ F _inc_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1) 

      - **For each potential pass-catcher** : Assume they are the ballcarrier, and input the current situation into the ball-carrier model, following the same procedure used for rushing plays 

The above framework is illustrated in Figure 4. In the above framework, the predictions from every model are updated at each time _t_ throughout the play, and (given the play type) can be combined to get an overall expected end-of-play yard line. For rushing plays, the expected end-of-play yard line directly estimated. For passing plays, each possible node ( _D, T, I,C_ ) on the decision tree in the framework above has two pieces of information: 

1. The node’s probability of being achieved, which is computed using the estimated probabilities at each step/split in the tree 

2. The expected end-of-play yard line, since each node eventually ends with the ball-carrier model’s estimate of the yards gained (or ends without a ballcarrier, in the case of an incompletion or throw away) 

These two pieces of information are easily combined across all nodes into a single estimate of the expected end-of-play yard line. 

After we estimate the end-of-play yard line, we can easily determine the additional covariates in the play value model from Section 3.2. For example, the updated down number and yards to go depend only on the previous yards to go and the yards gained on the play. Similarly, the possession team is easily determined, since the pass catcher is either on the offensive or defensive team, and turnovers on downs occur only if the yards gained on the play is less than the previous yards to go. 

> 4We suggest the use of Softmax normalization here, to handle rare cases where the estimated target probabilities are all 0. 

13 



Figure 4: Continuous-time play value framework. The blue squares represent sub-models, that can be estimated independently. The green circles are discrete outcomes of previous events, and the red diamonds indicate either the start of the play, the end of the play, or whether the play is a run or a pass. 

14 

### **3.4 Ball-Carrier Model** 

First, we model _E_ ( _Yi|_ F _carry_ ( _Xt,i_ )), the yards gained by the ball-carrier from their current position on the field conditional on the team in possession and the locations and trajectories of all 22 players on the field (including the ball-carrier). 

This ball-carrier model is the most important model in our continuous-time play value framework, because (1) it is the only model used for all rushing plays, and (2) all non-incomplete passing plays require the estimation of the yards gained by the ball-carrier (QB, receiver after catching the ball, defender after intercepting the ball, etc) from the current position on the field. 

Of key importance, only a single model is needed, and this model can be used for _any_ situation in which a player is carrying the ball (with no intent to pass). In other words, our framework requires a single model for all of the following ball-carrier situations: 

- a running back on rushing plays 

- a quarterback on scrambles or designed quarterback rushes 

- a wide receiver on end-arounds, reverses, etc 

- a pass-catcher after that player catches the ball (comprising both offensive players who catch a pass and defensive players who intercept a pass) 

We experiment with several implementations of this model for rushing plays, described in Section 4. Once we estimate _E_ ( _Yi|_ F _carry_ ( _Xt,i_ )), we can easily obtain an estimate of the end-of-play yard line, _E_ ( _Yi_<sup>_∗|_F</sup><sup>_carry_(</sup><sup>_Xt,i_)),byaddingtheball-</sup> carrier’s current yard line to _E_ ( _Yi|_ F _carry_ ( _Xt,i_ )), due to linearity of expectations. 

### **3.5 Quarterback Decision Model** 

For passing plays, we must model the decision that a quarterback will make. Specifically, on a given passing play, the quarterback has three possible decisions, described by the set _D_ = _{d_ 1 _,..., d_ 3 _}_ , where: 

- _d_ 1: Throw the ball away 

- _d_ 2: Run (or be sacked) 

- _d_ 3: Pass to a receiver 

15 

Let _P_ ( _Di|_ F _decision_ ( _Xt,i_ )) be a probability mass function for the decision made by the quarterback on play _i_ , a passing play, conditional on the locations and trajectories of all players and the ball over the course of play _i_ up until time _t_ . _P_ ( _Di|_ F _decision_ ( _Xt,i_ )) follows a multinomial distribution over the set _D_ . 

We leave the implementation of this model as a task for future work. Possible methods for implementing this model include recurrent neural networks with a multinomial response, multinomial logistic regression, or decision tree frameworks like random forests (Breiman, 2001) or XGBoost (Chen and Guestrin, 2016). 

### **3.6 Pass Target Probability Model** 

For passing plays where the QB’s decision is to pass (rather than run, be sacked, or throw the ball away), we must model each receiver’s target probability, _P_ ( _Tj,i_ = 1 _|_ F _pass_ ( _Xt,i_ ) _, Di_ = Pass). Since _Tj,i_ is a binary response variable, there are many suitable methods implementing this model. 

Importantly, when training this model, each play in the tracking dataset should be replicated five times (once for each possible targeted receiver on the offensive team), and each replicated play’s explanatory and response variables should be updated to be with respect to the receiver in question. That is, if a receiver _j_ 1 is targeted on this play, then _R j_ 1 = 1, and _R j_ 2 = _R j_ 3 = _R j_ 4 = _R j_ 5 = 0. Similarly, F _pass_ ( _Xt,i_ ) will be with respect to _j_ 1. 

Once the target probability is calculated for each of the five receivers, these five quantities must be Softmax-normalized so that they form a valid probability distribution over the space of possible targeted receivers. 

We leave the implementation of this model as a task for future work. 

### **3.7 Incompletion Probability Model** 

For each possible targeted receiver, we next model _P_ ( _Ii_ = 1 _|_ F _inc_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1), the probability that a pass to that receiver will be incomplete. 

It may seem counterintuitive to model _incompletion_ probability rather than _completion_ probability, but we do this for a specific purpose: So that the catch probabilities for each offensive receiver and defensive player (from the subsequent pass catching model) can be computed with the same model, and then Softmaxnormalized to the quantity 1 _− P_ ( _Ii_ = 1 _|_ F _inc_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1). 

A pass can only be caught or not caught (incomplete), so our random variable _Ii_ can take only two values: 1 if the pass is incomplete, and 0 if the pass is 

16 

caught (by an offensive receiver or defensive player). Since _Ii_ is a binary response variable, there are many suitable methods implementing the incompletion model (e.g. logistic regression, tree-based methods, or a recurrent neural network with a binomial response). 

We do not implement this model in this paper, since this area has been extensively studied. For example, Deshpande and Evans (2019) implement a similar model, but for catch probability. 

### **3.8 Catch Probability Model** 

Finally, we model _P_ ( _Ck,i_ = 1 _|_ F _catch_ ( _Xt,i_ ) _, Di_ = Pass _, Tj_ = 1 _, Ii_ = 0), the probability that player _k_ catches the ball, given that the pass targeted to receiver _j_ was not incomplete. 

Similar to the target probability model, when training the catch probability model, each play in the tracking dataset should be replicated 16 times (once for each eligible receiver on the offensive team, and once for each of the 11 defensive players), and each replicated play’s explanatory and response variables should be updated to be with respect to the receiver in question. That is, if a receiver _k_ 1 is targeted on this play, then _Ck_ 1 _,i_ = 1, and _Ck_ 2 _,i_ = _..._ = _Ck_ 16 _,i_ = 0. Similarly, F _catch_ ( _Xt,i_ ) will be with respect to _k_ 1. 

Since _Ck,i_ is a binary response variable, there are many suitable methods implementing the incompletion model (e.g. logistic regression, tree-based methods, or a recurrent neural network with a binomial response). 

Once the catch probability is calculated for each of the 16 possible passcatchers, these 16 quantities must be Softmax-normalized so that they form a valid probability distribution over the space of possible pass-catchers. 

We leave the implementation of this model as a task for future work. 

## **4 The Ball-Carrier Model** 

An advantage of our framework is the modularity of the models. Modularity implies that we can develop each model independently, then plug the best model for each task into the framework. For example, once we develop a ball-carrier model, we can use this model to compute continuous-time play value for each moment in a game when a player is running the football. 

Our ball-carrier model estimates the yards gained from the player’s current yard line (and thus the final yard line a ball carrier will reach on a play), condi- 

17 

tional on the locations and trajectories of all 22 players in the field. Section 4.1 introduces the features we use for our ball-carrier model, Section 4.2 describes the different ball-carrier models we tried, and Section 4.3 describes how we evaluate our ball-carrier models. 

### **4.1 Features for the Ball-Carrier Model** 

The tracking data provides a wealth of information about a football play, including who is on the field, where they are on the field, which direction they are facing, how fast they’re running, and more. A first step in developing our ball-carrier model is deciding what information will be helpful to use in modeling the yards gained from the ball-carrier’s current position. 

The first set of features we use is based on the location of each player relative to the ball-carrier. For each player, we record their _x_ -coordinate, _y_ -coordinate, speed, direction, distance traveled in the previous frame, and Euclidean distance to the ball-carrier. We split the players into three groups: ball-carrier, offense, and defense. For the offensive and defensive groups, we order the players based their Euclidean distance to the ball-carrier. For example, the feature `defense2 x` gives the _x_ -coordinate of the second closest defender, the feature `bc s` gives the speed of the ball-carrier, and so on. 

The second set of features uses the Voronoi tessellation of player locations (Voronoi, 1908). The Voronoi tessellation partitions the playing surface into regions, where each region corresponds to the area of the playing surface closest to an individual player. These regions help expose some of the more complex geometric relationships between the players.<sup>5</sup> 

We extract three simple features from the Voronoi tessellation: the area of the Voronoi region associated with the ball carrier, and the x-coordinates of the closest and farthest points from the target endzone on the boundary of the ball-carrier’s Voronoi region. Figure 5 exhibits these features for the handoff and first contact frames from the Cordarrelle Patterson TD run example from Figure 2. 

We created the Voronoi tessellations with the `deldir` package in `R` (Turner, 2019). For each frame of each play, we calculate both the complete set of vertices that define the tessellation, and the area of each player’s region. The set of vertices lets us calculate the features described above. This set of vertices also allows for future exploration of Voronoi features for the ball-carrier model (and, potentially, 

> 5Several authors use Voronoi tessellations to analyze tracking data in sports. For an overview, see Gudmundsson and Horton (2016). 

18 



Figure 5: A display of the Voronoi tessellation Cordarrelle Patterson’s 47 yard TD run at handoff (left) and first contact (right). The region for the ballcarrier is shaded. 

for other models in the continuous-time play value framework). A complete list of the features used in our ball-carrier model is given in Table 2. 

Each feature in Table 2 is centered and scaled. We also explored lagged variables, but did not find that these variables improved the performance of our models. This list of features is only a starting point, and future feature engineering, such as the space ownership approach from Fernandez and Bornn (2018), may significantly improve the ball-carrier model. Similarly, we currently do not have a good approach for directly accounting for the positioning of blockers, which may be especially useful for ball-carrier segments in the open field (though this is done indirectly via the Voronoi features). Improving upon the feature space used as input for the ball-carrier model may improve the model’s prediction accuracy, and is a task left to future work. 

### **4.2 Models** 

The ball-carrier model has several important aspects: 

- **High dimensions** . Since there are 22 players on the field, and each player has an x-coordinate, y-coordinate, angle, speed, etc., we can use many features to estimate the final yard-line of the ball-carrier. 

- **Non-linearity** . We don’t expect the best prediction for the final yard-line to have a simple linear structure. For example, we would expect a player facing the ball-carrier to have a better chance of making the tackle than a player than a player not facing the ball-carrier. 

- **Interactions** . Our features should depend on each-other. For example, a defender is more likely to tackle the ball-carrier if no one is blocking him. 

19 

<u>Table 2: List of features used in our ball-carrier model</u> 

|Variables|Description|
|---|---|
|`bc`<br>`x`,<br>`offenseX`<br>`x`,<br>`defenseX`<br>`x`|Horizontal x coordinate on feld for the ball-carrier,<br>`X` closest teammate, and `X` closest defender. For ex-<br>ample,`defense1`<br>~~`x`~~represents the x-coordinate of the<br>closest defender.|
|`bc`<br>`y`,<br>`offenseX`<br>`y`,<br>`defenseX`<br>`y`|Vertical y coordinate on feld for the ball-carrier, `X`<br>closest teammate, and`X`closest defender.|
|`bc`<br>`s`,<br>`offenseX`<br>`s`,<br>`defenseX`<br>`s`|Speed in yards/second for ball-carrier,`X`closest team-<br>mate, and`X`closest defender.|
|`bc`<br>`dir`,<br>`offenseX`<br>`dir`,<br>`defenseX`<br>`dir`|Direction in degrees the ball-carrier, `X` closest team-<br>mate, and`X`closest defender is facing.|
|`bc`<br>`dis`,<br>`offenseX`<br>`dis`,<br>`defenseX`<br>`dis`|Distance traveled since previous frame by the ball-<br>carrier,`X`closest teammate, and`X`closest defender.|
|`offenseX`<br>`dist`<br>`to`<br>~~`b`~~`a`<br>`defenseX`<br>`dist`<br>`to`<br>~~`b`~~`a`|`ll`,<br>`ll`<br>Euclidean distance from ball-carrier for `X` closest<br>teammate and`X`closest defender.|
|`voronoi`<br>~~`b`~~`c`<br>~~`c`~~`lose`|X-coordinate of the ball-carrier’s Voronoi region that<br>is closest to the target endzone.|
|`voronoi`<br>~~`b`~~`c`<br>~~`f`~~`ar`|X-coordinate of the ball-carrier’s Voronoi region that<br>is farthest to the target endzone.|
|`voronoi`<br>~~`b`~~`c`<br>~~`a`~~`rea`|Area of the Voronoi region associated with the ball-<br>carrier.|



- **Time** . Since we’re estimating the final yard-line at each time frame, the predictions should be smooth from frame-to-frame, and we should be able to use this temporal structure in our models. 

Thus, we select models that capture these aspects of the data, and we use appropriate regularization to avoid overfitting. Before moving to more complicated models, we establish a baseline model. The baseline model only uses an intercept, which means it doesn’t use any of the features described in Section 4.1. We use the baseline model to set an initial performance benchmark. 

The next model we use is the LASSO regression model (Tibshirani, 1996). 

20 

The LASSO works well in high dimensions, is easy to interpret, and has a fast implementation. We used the `glmnet` implementation in `R` , choosing the one standard error regularization penalty from model training via cross validation (Friedman et al., 2010). 

We also explored additive gradient boosting trees using the popular XGBoost implementation (Chen and Guestrin, 2016). Like the LASSO, XGBoost works in high dimensions, and also accounts for non-linear interactions in the data via tree-based partitioning. Of course, the LASSO can also account for non-linear interactions, but that would require the explicit construction of additional features. We implemented XGBoost via the `xgboost R` package, and found the default settings (100 trees, max depth of 3 splits) to yield the best results in cross-validation training among the regularization parameters that were considered. 

Another flexible model that works well in high dimensions, and can capture non-linear interactions, is a feedforward neural network (Haykin, 1998). Chapter 6 of Goodfellow et al. (2016) provides a clear and detailed overview of this type of model. We used a feedforward neural network with three layers, where each layer has five hidden units. We used a ReLu activation function for each layer<sup>6</sup> , and regularized each layer with an L1 penalty. We trained the network with the Adam algorithm (Kingma and Ba (2014)), and implemented the network with the `keras R` package (Allaire and Chollet (2019)). 

So far, none of our models have explicitly accounted for the temporal structure of the data. To remedy this, we can adapt our feedforward neural network into a _recurrent neural network_ . Specifically, we use a long short-term memory (LSTM) network (Hochreiter and Schmidhuber (1997)). Our LSTM has three layers, with five inputs in each layer, and we use a recurrent dropout rate of 20% for each layer. Finally, because not all ball-carrier sequences are the same length, we zero-pad each sequence to the size of the longest ball-carrier sequence. Table 3 summarizes the five different models we use, in terms of aspects we considered in the beginning of this section. 

### **4.3 Model Validation** 

Since our ultimate goal is to generate continuous-time valuations for every playertracking frame in the data, we need to ensure that our selected model is performing well across the sample of provided games. As a computationally feasible 

6Glorot et al. (2011) describe the ReLu activation function, and show that it outperforms other activation functions for deep networks. 

21 

Table 3: Comparison of ball-carrier models. 

|**Model**|High-dimensions|Non-linear|Interactions|Time|
|---|---|---|---|---|
|Baseline|||||
|LASSO|✓||||
|XGBoost|✓|✓|✓||
|Feedforward Neural Network|✓|✓|✓||
|Longshort-term memory (LSTM)|✓|✓|✓|✓|



alternative to the ideal leave-one-frame-out cross validation, we use leave-oneweek-out (LOWO) cross-validation (e.g. train on all frames from games in weeks one through five, then generate predictions on all frames from games in holdout week six) to select the ball-carrier model. We evaluate the LOWO predictions with three criteria: (1) overall root mean-squared error (RMSE), (2) weighted average RMSE across number of frames from end of ball-carrier sequence, and (3) the mean expected points added. 

The first criterion, overall holdout RMSE, is connected to our goal of generating baseline continuous-time within-play values across all individual frames. The second criteria places more emphasis on frames closer to the end of the ballcarrier sequences due to the variation in the length of runs as seen in Figure 3(A). A model is unlikely to accurately forecast the outcome of a ball-carrier sequence at the first frame when the length of entire ball-carrier sequence is long. The model should be more accurate on frames closer to the end of the ball-carrier sequence. The final criterion connects the generated results from the ball-carrier model to the end-goal of generating well-calibrated expected points values, as described in Yurko et al. (2019). If the ball-carrier model is ultimately generating expected points added values that are not centered at 0, this would indicate a bias in the established baseline used for evaluating movements within a play. 

## **5 Results** 

This section walks through various results and analysis of our ball-carrier model. 

### **5.1 Model Comparison and Selection** 

Table 4 displays the overall LOWO CV RMSE for each of the candidate models. We see that the LSTM performs best with the lowest RMSE. Unsurprisingly, 

22 

Table 4: LOWO CV RMSE for each model. 

|Model|RMSE|
|---|---|
|Baseline|7.72|
|LASSO|6.43|
|XGBoost|5.98|
|Feedforward Neural Network|6.18|
|LSTM|5.65|



Table 5: Weighted mean LOWO CV RMSE across the number of frames from end of ball-carrier sequence for each model. 

|Model|Weighted average RMSE|
|---|---|
|Baseline|6.10|
|LASSO|4.68|
|XGBoost|4.41|
|Feedforward Neural Network|4.60|
|LSTM|4.11|



all covariate-informed models perform better than the intercept-only baseline approach. Additionally, we see that the LASSO results in higher RMSE as compared 

The results for our second criterion are displayed in Table 5, revealing that the LSTM again performs best when up-weighting the predictions for frames closer to the end of the ball-carrier sequences. For reference, Figure 6 displays the RMSE across the number of frames away from the end of the ball-carrier sequence that are used for generating the weighted values in Table 5. We see the poor performance of the baseline across all moments in ball carrier sequences, and also that the LSTM appears to displays the optimal performance across the majority of frames in sequences. The increase in RMSE as we get farther out from the end of the play is to be expected, due to selection bias: plays that are 100 frames from the end of the ball-carrier sequence (i.e. 10 seconds from the play ending) are almost always long runs. 

To measure the _calibration_ of the candidate models, we perform the calculation of continuous-time play value for rushing plays, as described in Section 3.2, by using the LOWO CV model predictions. The predicted yard line a ball-carrier 

23 



Figure 6: Comparison of RMSE values for each model by number of frames from end of ball-carrier sequence. 

is expected to reach then determines the subsequent down (incremented by one if a first-down is not achieved, and reset to 1 if a first down is achieved or if there is a turnover on downs), the possession team (changes only if a turnover on downs takes place), the resulting yards to go for a first down or goal-down situation, and the score differential (changes only if a touchdown was scored on the run). For now, we use the observed time of the ball-carrier sequence for adjusting the amount of time remaining in the game. This adjusted contextual information is used to generate the expected points _EPt,i_ for each frame in the ball-carrier using the multinomial logistic regression model from Yurko et al. (2019). The calculations for _EPt,i_ were done using the `calculate` ~~`e`~~ `xpected` ~~`p`~~ `oints` function available in `nflscrapR` (Horowitz et al., 2017). The input features for the win probability model from Yurko et al. (2019) are similar to those of the expected points model, and thus require no additional explanation here. 

Figure 7 displays a comparison of the holdout expected points added (EPA) 

24 

values for the different candidate models, displaying the mean plus or minus two standard errors. Here, we see a clear bias in the baseline model, as well as noticeable mean-shifts from zero for both the LASSO and feedforward neural network models, but can clearly see that the LSTM has the closest mean to zero. 



Figure 7: Comparison of the mean LOWO CV expected points added values plus/minus two standard errors. 

Since the LSTM meets all three criteria of achieving accurate predictions according to RMSE, while also providing well-calibrated expected points added values, we proceed to train a LSTM model on the full six weeks of data. We use the same settings described in Section 4.2 on all of the available ball-carrier sequences to generate the results for the example play and player evaluations with the full LSTM model below. 

25 

### **5.2 Analysis of Feature Importance** 

For context regarding the covariates considered, we additionally trained the XGBoost and LASSO models on the entire dataset. Figure 8 displays the top ten variables in terms of importance from the XGBoost model. It shows that the two most important variables are the distance the to closest defender ( `defense1` ~~`d`~~ `ist` ~~`t`~~ `o ball` ) and the ball-carrier’s current speed ( `bc` ~~`s`~~ ). This is consistent with the top variables selected by the LASSO model trained on the entire dataset, as indicated by Figure 9. The directions of the LASSO coefficients are consistent with intuition, e.g. the faster the ball-carrier is moving the further they are expected to carry the football. 



Figure 8: Variable importance plot for the XGBoost model trained on all data. Only the top ten variables are displayed. 

26 



Figure 9: Top ten variables by absolute value of coefficient estimates for LASSO trained on all data. 

### **5.3 Continuous-Time Play Value: Examples** 

Using the LSTM model from Section 5.1 trained on all available data, we again calculate the continuous-time play values by feeding the LSTM predictions into both the expected points and win probability models from Yurko et al. (2019), making the appropriate corrections as described in Section 5.1. This framework for computing expected points additionally allows us to generate the continuoustime win probability _WPt,i_ by using the adjusted time remaining and frame-level _EPt,i_ as inputs for the generalized additive win probability model in Yurko et al. (2019). The calculation for _WPt,i_ was done using the `calculate` ~~`w`~~ `in probability` function available in `nflscrapR` (Horowitz et al., 2017). 

We return to the Cordarrelle Patterson TD run from Figure 2 to demonstrate. On offense, the Raiders trailed the Chargers 14-10 in the fourth quarter with eight minutes left on 2<sup>nd</sup> down with two yards to go to at the Chargers’ 47 yard line. Figure 1 displays the change in expected points and win probability estimates over 

27 

the course of the run, starting with the initial between-play value and changing over the course of the play until reaching the endzone for a touchdown. This resulted in the Raiders taking the lead and advancing their win probability beyond the 50% mark. 

Figure 10 displays an updated version of Figure 2 with the expected yard line (in red), that the ball-carrier (black) is predicted to reach given all information regarding his teammates (blue) and opponents (orange) using the LSTM model at (A) handoff, (B) first contact, and (C) the first frame when the expectation was a touchdown. At handoff the expectation is roughly an eleven-yard gain and increases steadily through first contact, as captured by Figure 1, until the expectation reaches the prediction of a TD run. 

For context in understanding the change in the expected points and win probability within the touchdown run, Figure 11 displays the (A) change in the distance to closest defender, as well as (B) Patterson’s speed and (C) Patterson’s Voronoi area in each frame of the run. We see that the moment Patterson was no longer expected to score a touchdown occurred when the closest defender was within the same distance as the point of first contact. But he then gained additional separation from the opponent, leading to an expectation of scoring a touchdown once again. 

### **5.4 Player Evaluation with Continuous-Time Play Value** 

As noted in Section 1.3, we can use the resulting continuous expected points values from the LSTM model to gain insight into the contributions of individual athletes over the course of a play. Figure 12 demonstrates this by displaying the joint distribution of the EPA per frame and and frame-level success rate, a novel update of Brian Burke’s success rate (Burke, 2009) now calculated to be the proportion of player frames leading to positive expected points added. For simplicity, this figure only displays players with a minimum of 1000 frames of carrying the football. We see running back Leonard Fournette stand out for his high EPA per frame, while Seattle Seahawks’ QB Russell Wilson appears to provide the most value with his legs among qualified QBs during these first six weeks of the 2017 NFL season. In this small sample of data, these player-level metrics are heavily influenced by long runs and touchdown runs. For example, Leonard Fournette had six touchdown runs in the first six weeks of the 2017 season, including long runs of 90 and 75 yards. 

We are also able to calculate the total win probability added (WPA) for each player from their various movements over the course of the runs using our ball- 

28 



Figure 10: The red line indicates the expected yard line Cordarrelle Patterson (in black) will reach at (A) handoff, (B) first contact, and (C) the first frame he’s expected to reach the endzone. Blue points indicate the ball-carrier’s teammates while orange represents the opponents. 

29 



Figure 11: The change in (A) distance to closest defender, (B) ball-carrier speed, and (C) the ball-carrier’s Voronoi area during Cordarrelle Patterson’s 47 yard TD run. 

carrier model. Tables 6 and 7 display the top and bottom five players according to the total WPA accumulated from their ball-carrier movements. 

With limited data, it is difficult to evaluate these frame-level metrics and make claims about their discriminatory ability. Each of these continuous-time estimates are a function of all twenty-two players on the field, while the above metrics are merely attributing the observed change in value of the frame-level data to the ball carrier. Regression-based approaches such as the implementation in Yurko et al. (2019) could provide a starting point for dividing the credit among players within the play. Additionally, our model accounts for the player’s speed as an input which is an inherent function of the ball-carrier. Future work would consider imputing average speed levels for all ball-carriers at particular moments over the course of the run or generate the ball-carrier model without speed accounted for. However, due to the limited availability of data this currently presents a challenge that could be addressed when more data are made available. 

30 



Figure 12: Joint distribution of EPA per frame and frame-level success rate for players with at least 1000 ball-carrier frames. 

Table 6: Top five players with highest total WPA as ball-carriers. 

|Name|Total WPA|
|---|---|
|Leonard Fournette|0.23|
|Kareem Hunt|0.23|
|Dak Prescott|0.22|
|Cordarrelle Patterson|0.21|
|Orleans Darkwa|0.19|



Table 7: Bottom five players with lowest total WPA as ball-carriers. 

|Name|Total WPA|
|---|---|
|Le’Veon Bell|-0.40|
|TyMontgomery|-0.41|
|Chris Carson|-0.46|
|Melvin Gordon|-0.51|
|JayAjayi|-0.60|



31 

## **6 Discussion & Future Directions** 

In this work, we provide a framework for continuous-time within-play valuations of game outcomes in football using player and ball-tracking data from the National Football League. We implement the core piece of this framework, a model for the expected yards gained from a ball-carrier’s current yard line, conditional on the locations and trajectories of all 22 players on the field, and we test several different modeling approaches for doing so. As input for this ball-carrier model, we create a rich set of features that describe the location of the ball-carrier relative to other players on the field, e.g. with features generated from Voronoi tessellations of all 22 players on the field. For this ball-carrier model, we find that all tested models substantially outperform a baseline intercept-only model, but that a long short-term memory (LSTM) recurrent neural network outperforms alternative approaches according to the three evaluation measures we set forth in this paper. 

We provide the results of the ball-carrier model and, thus, an implementation of continuous-time valuation of game outcomes in football for all rushing plays, using the NFL-provided tracking data from Weeks 1-6 of the 2017 season. Using these within-play estimates of expected points and win probability, we briefly discuss metrics for evaluating individual rushers, such as each player’s expected points added per frame and frame-level rushing success rate. 

There are many potential directions for future work. First, there are several remaining aspects to a football game that we do not currently handle. First, we assume the play type is known at the start of the play, which could be problematic. For example, run-pass options have become increasingly popular in recent seasons, with teams like the 2018 Baltimore Ravens using this as a core feature of their offensive game-plan in the second half of the season (Pennington, 2018). Currently, our models condition on the play type at the top level of the framework in Figure 4. 

Second, we currently do not handle special teams. A brief sketch of how this important piece of a football may fit into our framework is as follows: For kickoff and punt returns, we can use the ball-carrier model, provided enough training data (this was not possible with only six weeks of data for this paper). For field goals, since blocked kicks are rare, continuous-time play value is likely of limited additional value above what is possible with discrete-time (between-play) play value models. Similarly, blocked punts are rare, so attempting to model these may prove more challenging than its worth. 

Third, we currently do not handle fumbles by the ball-carrier. To do so, we 

32 

would have to incorporate a survival component into our model, accounting for the hazard of a fumble at each moment throughout a ball-carrier sequence, conditional on the features of that sequence that may be indicative of changes in fumble rates. However, fumbles are rare events, and even rarer in a six-week sample of games (there were only 77 rushing fumbles in 153,184 rushing frames across 4,447 ballcarrier sequences in our dataset), rendering the estimation of this component of the ball-carrier model impractical. This task is left to future work, if/when multiple seasons of tracking data are available. 

Fourth, we currently use an ad hoc approach for estimating the time remaining at the end of plays. An elegant approach would be to model the joint distribution of the yards gained from the ball-carrier’s current position and the time remaining at the end of the play. However, doing so would (at least) double the size of the parameter space. Additionally, time remaining is typically of little value in a between-play model for play value, and only comes into play in somewhat rare situations at the end of the 1st or 2nd half. With a limited set of six weeks of tracking data, the ad hoc approach we use here will suffice. 

Fifth, there is more work to be done in the area of feature engineering. As discussed, using a Voronoi-like approach that accounts for the velocity of players on the field, similar to what Fernandez and Bornn (2018) do for modeling space creation and occupation in soccer, may yield some improvements in model predictions. Additionally, accounting for blockers (e.g. by joining the adjacent Voronoi polygons of teammates to identify a path through which the ball-carrier can travel) may also lead to improved prediction accuracy. 

Sixth, in the context of player evaluation, researchers should be careful about how they use our models when evaluating players. As demonstrated in Figure 8, the ball-carrier speed is one of the most important features in modeling yards gained from the current position on the field. However, if we condition on the speed of a player in the model, any gains a ball-carrier makes as a result of being faster than other ball-carriers (or losses from being slower) will be not be attributed to that ball-carrier. As such, researchers using our models for player evaluation should consider using the average speed of player when evaluating individuals, so that deviations above and below average are attributed to that player. 

Along these lines, future researcher may use our continuous-time, within-play valuation of game outcomes to evaluate micro-actions of all players on the field, similar to what has been done in basketball (Sicilia et al., 2019) and soccer (Fernandez and Bornn, 2018; Decroos et al., 2019). Similar ideas have been implemented for players at offensive skill positions at the discrete-time level in football (Yurko et al., 2019), but never implemented for all 22 players on the field, and 

33 

never implemented in a continuous-time framework. 

Next, Pospisil and Lee (2018) propose methods for conditional density estimation with random forests and neural networks, which may prove valuable in our ball-carrier model. In particular, estimating the entire distribution of possible outcomes at each frame would provide a more complete picture of the possible outcomes at each portion of the play, and would allow for more interesting methods of player evaluation. For example, instead of using metrics like frame-level expected points added (which compare players to average), similar metrics could be generated that measure performance relative to a baseline (e.g. replacement level) that can be objectively defined from conditional density estimates. 

Finally and most importantly, we currently only provide an implementation of the ball-carrier model, and we do not implement the other modular sub-models in our framework for continuous-time play value (e.g. QB decision model, target probability model, catch probability model, etc). Implementation of these models is somewhat straightforward, given an appropriate feature space: Since the responses in these models are either binary (target probability, incompletion probability, catch probability) or multinomial (QB decision), simple adjustments can be made to LSTM we use for the ball-carrier model to enable a similar approach to be used for these pieces of the framework. Additionally, some authors implement excellent versions of these models already. For example, Deshpande and Evans (2019) implement a catch probability model, and Burke (2019) implements both a QB decision model and a target probability model. We look forward to incorporating these models in our framework for continuous-time valuation of game outcomes in football. 

## **References** 

- Allaire, J. and F. Chollet (2019): _keras: R Interface to ’Keras’_ , URL `https: //CRAN.R-project.org/package=keras` , r package version 2.2.4.1. 

- Breiman, L. (2001): “Random forests,” _Machine Learning_ , 45, 5–32, URL `https://doi.org/10.1023/A:1010933404324` . 

- Burke, B. (2009): “How coaches think: Run success rate,” URL `https://www.advancedfootballanalytics.com/index.php/home/ research/general/114-how-coaches-think-run-success-rate` . 

- Burke, B. (2019): “Deepqb: Deep learning with player tracking to quan- 

34 

tify quarterback decision-making & performance,” _MIT Sloan Sports Analytics Conference_ , URL `http://www.sloansportsconference.com/wpcontent/uploads/2019/02/DeepQB.pdf` . 

- Cervone, D., A. D’Amour, L. Bornn, and K. Goldsberry (2014): “Pointwise: Predicting points and valuing decisions in real time with nba optical tracking data.” _MIT Sloan Sports Analytics Conference_ , 28, 3, URL `http://www.sloansportsconference.com/wp-content/uploads/ 2018/09/cervone_ssac_2014.pdf` . 

- Cervone, D., A. D’Amour, L. Bornn, and K. Goldsberry (2016): “A multiresolution stochastic process model for predicting basketball possession outcomes,” _Journal of the American Statistical Association_ , 111, 585–599, URL `https: //arxiv.org/abs/1408.0777` . 

- Chen, T. and C. Guestrin (2016): “Xgboost: A scalable tree boosting system,” in _Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’16, New York, NY, USA: ACM, 785– 794, URL `http://doi.acm.org/10.1145/2939672.2939785` . 

- Chu, D., L. Wu, M. Reyers, and J. Thomson (2019): “Routes to success,” _NFL Big Data Bowl_ , URL `https://danichusfu.github.io/files/Big_Data_ Bowl.pdf` . 

- Decroos, T., L. Bransen, J. V. Haaren, and J. Davis (2019): “Actions speak louder than goals: Valuing player actions in soccer,” _MIT Sloan Sports Analytics Conference_ . 

- Deshpande, S. K. and K. Evans (2019): “Expected hypothetical completion probability,” _NFL Big Data Bowl_ , URL `https://operations.nfl.com/media/ 3668/big-data-bowl-deshpande_evans.pdf` . 

- Dutta, R., R. Yurko, and S. L. Ventura (2019): “Unsupervised methods for identifying pass coverage among defensive backs with nfl player tracking data,” . 

- Fernandez, J. and L. Bornn (2018): “Wide open spaces: A statistical technique for measuring space creation in professional soccer,” _MIT Sloan Sports Analytics Conference_ . 

35 

- Fern´andez, J., L. Bornn, and D. Cervone (2019): “Decomposing the immeasurable sport: A deep learning expected possession value framework for soccer,” _MIT Sloan Sports Analytics Conference_ , URL `http://www.sloansportsconference.com/wp-content/uploads/ 2019/02/Decomposing-the-Immeasurable-Sport.pdf` . 

- Friedman, J., T. Hastie, and R. Tibshirani (2010): “Regularization paths for generalized linear models via coordinate descent,” _Journal of Statistical Software_ , 33, 1–22, URL `http://www.jstatsoft.org/v33/i01/` . 

- Glorot, X., A. Bordes, and Y. Bengio (2011): “Deep sparse rectifier neural networks,” in G. Gordon, D. Dunson, and M. Dudk, eds., _Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics_ , _Proceedings of Machine Learning Research_ , volume 15, Fort Lauderdale, FL, USA: PMLR, _Proceedings of Machine Learning Research_ , volume 15, 315– 323, URL `http://proceedings.mlr.press/v15/glorot11a.html` . 

- Goodfellow, I., Y. Bengio, and A. Courville (2016): _Deep Learning_ , MIT Press, `http://www.deeplearningbook.org` . 

- Gudmundsson, J. and M. Horton (2016): “Spatio-temporal analysis of team sports - A survey,” _CoRR_ , abs/1602.06994, URL `http://arxiv.org/abs/1602. 06994` . 

- Haar, A. V. (2019): “Exploratory data analysis of passing plays using nfl tracking data,” _NFL Big Data Bowl_ , URL `https://operations.nfl.com/media/ 3672/big-data-bowl-vonder-haar.pdf` . 

- Haykin, S. (1998): _Neural Networks: A Comprehensive Foundation_ , Upper Saddle River, NJ, USA: Prentice Hall PTR, 2nd edition. 

- Hochreiter, S. and J. Schmidhuber (1997): “Long short-term memory,” _Neural computation_ , 9, 1735–1780. 

- Horowitz, M., R. Yurko, and S. L. Ventura (2017): _nflscrapR: Compiling the NFL play-by-play API for easy use in R_ , URL `https://github.com/ maksimhorowitz/nflscrapR` , r package version 1.4.0. 

- Kingma, D. P. and J. Ba (2014): “Adam: A method for stochastic optimization,” _arXiv preprint arXiv:1412.6980_ . 

36 

- Link, D., S. Lang, and P. Seidenschwarz (2016): “Real time quantification of dangerousity in football using spatiotemporal tracking data,” _PLoS ONE_ , 11, URL `https://doi.org/10.1371/journal.pone.0168768` . 

- Pennington, B. (2018): “The ravens down-to-earth approach is unnerving the n.f.l.” _The New York Times_ , URL `https://www.nytimes.com/2018/12/14/ sports/baltimore-ravens-lamar-jackson.html` . 

- Pospisil, T. and A. Lee (2018): “Rfcde: Random forests for conditional density estimation,” URL `https://arxiv.org/abs/1804.05753` . 

- Sicilia, A., K. Pelechrinis, and K. Goldsberry (2019): “Deephoops: Evaluating micro-actions in basketball using deep feature representations of spatiotemporal data,” . 

- Sterken, N. (2019): “Routenet: a convolutional neural network for classifying routes,” _NFL Big Data Bowl_ , URL `https://operations.nfl.com/media/ 3671/big-data-bowl-sterken.pdf` . 

- Tibshirani, R. (1996): “Regression shrinkage and selection via the lasso,” _Journal of the Royal Statistical Society. Series B (Methodological)_ , 58, 267–288, URL `http://www.jstor.org/stable/2346178` . 

- Turner, R. (2019): _deldir: Delaunay Triangulation and Dirichlet (Voronoi) Tessellation_ , URL `https://CRAN.R-project.org/package=deldir` , r package version 0.1-16. 

- Voronoi, G. (1908): “Nouvelles applications des paramtres continus la thorie des formes quadratiques. premier mmoire. sur quelques proprits des formes quadratiques positives parfaites.” _Journal fr die reine und angewandte Mathematik_ , 133, 97–178, URL `http://eudml.org/doc/149276` . 

- Yurko, R., M. Horowitz, and S. Ventura (2019): “nflwar: A reproducible method for offensive player evaluation in football,” _Journal of Quantitative Analysis in Sports_ , Forthcoming, URL `https://arxiv.org/abs/1802.00998` . 

37 


