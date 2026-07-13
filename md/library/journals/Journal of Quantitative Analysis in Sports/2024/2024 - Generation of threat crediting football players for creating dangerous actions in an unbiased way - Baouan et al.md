<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2024/2024 - Generation of threat crediting football players for creating dangerous actions in an unbiased way - Baouan et al.pdf -->

J. Quant. Anal. Sports 2025; aop 

### **Research Article** 

Ali Baouan*, Sébastien Coustou, Mathieu Lacome, Sergio Pulido and Mathieu Rosenbaum 

# **Generation of threat: crediting football players for creating dangerous actions in an unbiased way** 

https://doi.org/10.1515/jqas-2024-0107 Received July 23, 2024; accepted August 1, 2025; published online September 24, 2025 

**Abstract:** We introduce an innovative methodology to identify football players at the origin of threatening actions in a team. In our framework, a threat is defined as entering the opposing team’s _danger area_ . We investigate the timing of threat events and ball touches of players, and capture their correlation using Hawkes processes. Our modelbased approach allows us to evaluate a player’s ability to create danger both directly and through interactions with teammates. We define a new index, called _Generation of Threat_ (GoT), that measures in an unbiased way the contribution of a player to threat generation. For illustration, we present a detailed analysis of Chelsea’s 2016–2017 season, with a standout performance from Eden Hazard. We are able to credit each player for his involvement in danger creation and determine the main circuits leading to threat. In the same spirit, we investigate the danger generation process of Stade Rennais in the 2021–2022 season. Furthermore, we establish a comprehensive ranking of Ligue 1 players based on their generated threat in the 2021–2022 season. Our analysis reveals surprising results, with players such as Jason Berthomier, Moses Simon and Frederic Guilbert among the top performers in the GoT rankings. 

**Keywords:** football; generation of threat; Hawkes processes; performance metrics; player ranking 

***Corresponding author: Ali Baouan** , Centre de Mathématiques Appliquées, CMAP, Ecole Polytechnique, route de Saclay, 91128 Palaiseau Cedex, France, E-mail: ali.baouan@polytechnique.edu 

**Sébastien Coustou and Mathieu Lacome** , Parma Calcio 1913 Performance and Analytics, Parma, Italy 

**Sergio Pulido** , Université Paris–Saclay, CNRS, ENSIIE, Univ Évry, LaMME, Évry, France 

**Mathieu Rosenbaum** , Centre de Mathématiques Appliquées, Ecole Polytechnique, Palaiseau, France 

## **1 Introduction** 

Which player should be credited for a successful action or sequence in a football match? In the case of a goal, the striker obviously plays an important role. However, we all have in mind goals where the striker just needs to push the ball after a great assist. In that case, the passer is certainly the most important player involved. Some argue that the second-to-last pass is actually the most crucial component as it is often this pass that creates disequilibrium. Sometimes, we even see a clearance by a goalkeeper being at the origin of a dangerous situation. 

In this work, our goal is to build a quantitative and unbiased methodology enabling us to assess the importance of a player in the generation of dangerous actions. By a threat, we simply mean a situation where a player of the team of interest gets the ball in the danger area of the opposing team. The danger area is defined as a rectangular region around the opponent’s goal where the likelihood of scoring from a shot is high. To achieve our objective, we need to model interactions between players, taking into account past events in the game accurately. This is because we want, for example, to be able to credit a defender for a great pass that leads to a dangerous situation after several ball touches following the initial pass. Therefore, at the timestamp where the action is considered dangerous (in our case when the ball reaches the danger area), we must “remember” the original pass of the defender. 

Thus, at a given time _t_ , we want to draw links between past events in the game and its future. With this objective in mind, simply relying on the current state of the game (players and ball’s positions) as the information set is not enough for modeling the game accurately. It is important to consider the dynamics that occurred prior to time _t_ . This is in contrast to the so-called Markovian approach where one summarizes information obtained from the beginning of the game until time _t_ by the state of the game at time _t_ . The Markovian setting is in fact underlying some very relevant and successful metrics introduced recently such 

Open Access. © 2025 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

as the expected goals (Green 2012) and expected assists (Whitmore 2021). For example, the expected goal estimates the probability that a shot results in a goal based on factors such as the distance to the goal and the angle of the shot, both attributes of the game state at time _t_ . The Markov assumption is in that case natural as these features give a reasonable estimate of the quality of the chance. Similarly, the expected assists aim at measuring the probability that a pass leads to a goal, by looking at a different subset of game state features, such as the type of the pass and the coordinates of the target. What these two approaches have in common is that given time _t_ they define a value for an action (pass or shot), that is determined by the game state at time _t_ only and does not look at the past patterns of play. In the same spirit, the expected threat introduced in (Singh 2018) assigns a value to each game state depending only on the position of the ball. This value combines the possibilities of a direct shot or a pass to another position in quantifying the expected number of goals. 

To account for the effect of past events in the future dynamics of a game, we introduce Hawkes processes (Hawkes 1971a,b) to reproduce interactions between players. Hawkes processes are stochastic models used to model sequences of random events. They are widely used in various fields such as earthquake modeling (Adamopoulos 1976; Ogata 1988), neuroscience (Bonnet et al. 2022a; Lambert et al. 2018) and finance (Jaisson and Rosenbaum 2015). 

In our case, the events are the times when players touch the ball. Specifically, we implement a Hawkes process with 11 components (number of players in the team), with component _i_ corresponding to player _i_ of the team of interest. The value of this component at time _t_ is simply the number of times player _i_ has touched the ball from the beginning of the game to time _t_ . At each time the player touches the ball, his corresponding component increases by one. The innovation here is that we collect information from these timestamps and their correlations from one player to the other teammates. 

The specificity of Hawkes processes is that at time _t_ , the probability that player _i_ gets the ball shortly after _t_ depends on which players had possession of the ball before _t_ and how long ago they had it. The impact on this probability of a player touching the ball a long time before _t_ is negligible compared to a player who had possession right before _t_ . The ability to reproduce the decaying impact of events with time is a particularly useful property of Hawkes processes in our context. For instance, let us consider a central defender. At time _t_ , the probability that he gets the ball in the near future should be high if, in the recent past (last few seconds), he already touched the ball and/or another central defender 

did. On the contrary, if the forward players have held the ball for the past minute, this probability should be low. 

Then, we add a twelfth component to our Hawkes process that we call threat. The value of the threat component at time _t_ is simply the number of times the ball has reached the danger area of the opposing team between the beginning of the game and time _t_ . Treating this component as part of our Hawkes process, we are able to model the influence of each player in the generation of threat. 

Calibrating our model allows us to assess the contribution of each player of a team to the creation of dangerous situations. We are therefore able to investigate carefully the subtle dynamics and connections leading to ominous situations. In particular, we can emphasize the crucial role of certain players that are not spotted by other statistics. Note that our calibration requires the analysis of a data set of at least 10 games. So we are not evaluating each action occurring in a game but rather the global performance of players in terms of threat generation over a sequence of games. 

More precisely, the structure of Hawkes processes allows us to define the Generation of Threat (GoT) indices to objectively evaluate a player’s involvement in the creation of threats over a considered series of games. These metrics quantify the expected number of dangerous situations for which a player can be credited. The direct generation of threat indices GoT<sup>(</sup><sup>_dir_)</sup> and GoT<sup>(</sup><sup>_dir_)</sup> measure the number of 90 threats the player is directly responsible for generating per touch of the ball and per 90 min, respectively. Directly generating a threat can be viewed as being the last link in the chain of events leading to it. On the other hand, the indirect generation of threat indices GoT<sup>(</sup><sup>_ind_)</sup> and GoT<sup>(</sup> 90<sup>_ind_)</sup> measure the indirect contribution per touch and per 90 min, respectively, adding the danger created via the interactions with other players too. In this case, we count all the instances where the player participates in the chain of events leading to the dangerous situation. As an application, we use the GoT indices to rank the Ligue 1 players in the 2021–2022 season. Not surprisingly, the top positions are dominated by established offensive players. However, we also identify some surprising picks, including Jason Berthomier, Moses Simon and Frederic Guilbert, who rank among the top 20 players. We also compare the performance of the Ligue 1 central defenders in terms of GoT<sup>(</sup> 90<sup>_ind_)</sup> . Naturally, defenders from Paris Saint-Germain stand out and benefit from the offensive performance of their forwards. However, we also identify other excellent center-back pairs such as Nayef Aguerd and Warmed Omari from Stade Rennais, and Facundo Medina and Jonathan Gradit from Lens. Moreover, our approach allows us to rate these players based on their performance 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 3** 

in specific positions in a formation, providing a tool to identify the optimal position for each player. 

Our approach has the property of being easily interpretable using the immigration-birth representation of linear Hawkes processes, see (Hawkes and Oakes 1974). This representation induces a notion of hierarchy between events and allows us to visualize the interactions between different event types in a graph. All player touches can be viewed as individuals in a population, and each individual independently generates offsprings, that are threat events or ball touches of the same player or other players. In particular, this enables us to effectively interpret the estimated GoT metrics as a measure of the hierarchical relationship between the player’s touch and subsequent threat events. Furthermore, we can construct interaction networks of football teams and graphically analyze a team’s in-game dynamics and danger creation circuits. We apply this approach to investigate games from Chelsea in the 2016–2017 season and Stade Rennais in the 2021–2022 season. We are able to effectively capture the main threat creation circuits that the opponent should try to control. Identifying specific patterns and evaluating the ability of players to create threat with our methodology paves the way to more informed decisions about tactics. 

The article is organized as follows. In Section 2, we describe the event-based data we have in hand and how it is processed. We also provide an overview of Hawkes processes and recall the results that are useful for our football application. Furthermore, we present the interpretation of the estimated parameters in the context of football and define the Generation of Threat (GoT) metrics. In Section 3, we briefly describe the maximum likelihood estimation methodology. We also conduct a study on simulated data to measure estimation accuracy that can be expected on real datasets depending on the amount of available data. We find that reliable estimation can be obtained from 600 min of football data. Section 4 presents the results of our analysis on a collection of Chelsea games in the 2016–2017 season. In Section 5, we establish a ranking of Ligue 1 players in the 2021–2022 season based on their GoT indices. Finally, in the Appendix, we present the analysis of the Stade Rennais games in the 2021–2022 Ligue 1 season. 

## **2 Modeling event-based football data** 

This section provides a short overview of Hawkes processes as applied to football event data. It includes necessary definitions and theoretical results for a better understanding 

of the subsequent analysis of football dynamics. Furthermore, we discuss the interpretation of the parameters of the Hawkes process in this context and introduce the Generation of Threat (GoT) metrics to quantify a player’s influence on creating dangerous situations. 

### **2.1 Description of the data** 

We use the F24 files provided by Stats-perform. Each file gives comprehensive information about a football match, including the formation of each team and the position of each player on the pitch. Unlike real-time tracking datasets, the F24 files do not record the continuous movement of all players; instead, they focus on discrete events. Specifically, this dataset is a time-coded feed that lists all player action events within the game, detailing the player involved, team affiliation, event type, the coordinates on the pitch and the timestamp. Event types include passes, shots, goals, set pieces, etc. Each event is further described by a series of qualifiers that provide additional context and specifics. 

The temporal nature of the dataset naturally encourages the use of point process models to analyze in-game events. In the Stats-perform classification system, each position on the pitch is assigned a number _p_ in {1 _, ... ,_ 11} for each formation. Therefore, we construct a multivariate counting process that tracks the number of events associated with the player in each position _p_ at all times _t_ . Analyzing the relationships between the components of this process can provide interesting insights into the playing dynamics of the team. To capture the impact of the ball touches of each player on the offensive performance, we use Hawkes processes to model the constructed counting processes. Details on how the counting process is constructed are provided in Section 2.3. 

### **2.2 Hawkes processes** 

As mentioned in the introduction, Hawkes processes are a class of multivariate point processes introduced in (Hawkes 1971a). If we consider a vector _N_ ( _t_ ) = ( _Ni_ ( _t_ )) _i_ ∈{1 _,_ … _,d_ }, where _Ni_ ( _t_ ) denotes the number of events for the _i_ -th component between 0 and _t_ , the associated intensity process can essentially be defined as: 



Here,  _t_ is the filtration generated by { _Ns, s < t_ }, that is the information set available at time _t_ . The intensity of a counting process determines the rate at which new jumps occur based on past events, see (Brémaud 1981) for a more 

> **4 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

rigorous definition. In the case of Hawkes processes, the intensity is a linear combination of past jump times. 

Moreover, a Hawkes process is said to be stable if ∫0<sup>∞</sup><sup>_𝜙i,j_(</sup><sup>_t_)d</sup><sup>_t<_∞forall</sup><sup>_i,j_andifthespectralradius</sup><sup>_𝜌_(</sup><sup>_K_)</sup> of the branching matrix satisfies: 

**Definition 1** (Hawkes process). A _d_ -variate Hawkes process is a counting-process _N_ ( _t_ ) ∈ ℝ<sup>_d_</sup> whose _i_ -th component is determined by its intensity of the form: 



See (Jaisson and Rosenbaum 2015) for more details. 



In the context of football event-based data, _K_ provides us with a measure of the interaction between players. The higher the value of _Ki, j_ , the more likely there are ball touches from player _i_ following a ball touch from player _j_ . Finally, we use the parametric class of exponential kernels in our estimation methodology. 

where the _t_<sup>(</sup><sup>_j_)thetimesofeventsfordimension</sup><sup>_j_</sup> ( _k_ ) _k_ ≥1<sup>are</sup> for _j_ = 1 _, ... , d_ . _𝜇i_ ∈ ℝ<sup>+</sup> is a constant baseline intensity and _𝜙i, j_ : ℝ<sup>+</sup> → ℝ<sup>+</sup> is a non-negative kernel. We can write the expression for the intensity in the vectorial form: 

**Definition 3** (Exponential kernels). The exponential kernel is as 



where _𝛼i, j_ , _𝛽 i, j_ are nonnegative real numbers. 

with _𝜇_ ∈ ℝ<sup>+</sup><sup>_d_</sup> and _𝜙_ =<sup>{</sup> _𝜙i, j_ }0≤ _i, j_ ≤ _d_<sup>:ℝ+→ℝ</sup><sup>_d_×</sup><sup>_d_anon-</sup> negative matrix-valued kernel. 

Exponential kernels are particularly nice from a computational viewpoint in estimation. Additionally, their parameters are easy to interpret. In fact, the branching matrix in this case is simply given by _K_ = _𝛼i,_ _<u>j</u>_ and the ( _𝛽i, j_ ) _i, j_ decay parameter _𝛽 i, j_ indicates the speed at which cross excitation decreases. 

The underlying idea behind Hawkes processes is that a constant intensity _𝜇_ generates the initial batch of jumps across all dimensions. These jumps are random but the rate of their occurrence remains constant over time. Then, each jump increases the intensity in the near future; therefore, exciting new jumps, that in turn trigger other jumps. This leads to a chain reaction called the self-excitation property of Hawkes processes. 

### **2.3 Processing of the data for Hawkes inference** 

In this work, the counting process _N_ ( _t_ ) records the ball touches of each player and the self-excitation property is desirable. In fact, whenever a player touches the ball, it raises the probability of further touches – either by the same player or by teammates – in the near future. Consequently, we expect diagonal components _𝜙i,i_ of the kernel to be significant, since a player’s own touches often occur in short succession. More generally, the off-diagonal kernels _𝜙i, j_ reflect how a touch from player _j_ increases the likelihood of a subsequent touch from player _i_ . To quantify the level of interaction between the components of a Hawkes process, we introduce the notion of branching matrix. This definition is also necessary to state conditions for the system to be stable. 

We study our event-based data using Hawkes processes. Doing so, we can gain insights from timestamps of events and information about the spatial coordinates of the ball. For each game, the players occupying each position are provided, with each position assigned a number _p_ in {1 _, ... ,_ 11} following the Stats-perform classification system. For a given team and a list of its games, we build a 12-dimensional point process for each game. Each dimension _p_ ∈ {1 _, ... ,_ 11} records the timestamps of ball touches by the player occupying position _p_ , regardless of his identity. The twelfth dimension represents the threat state and is triggered every time there is a ball touch by a player from the considered team in the danger area of the opponent. The danger area is defined as a box around the opposing goal covering 50 % of the width of the pitch and 25 % of its length, as illustrated in Figure 1. When a player has possession of the ball in this region, the probability of a shot occurring is high, see (Singh 2018) for an estimate of the shot probability at each location on the pitch. Compared to the penalty surface, the danger area is slightly closer to the midfielders and 

**Definition 2** (Branching matrix, stability). The branching matrix of a Hawkes process is defined as, 



A. Baouan et al.: Crediting football players for creating dangerous actions **— 5** 



**Figure 1:** Representation of the danger area. 

defenders, enabling us to capture more threat events generated by these positions. 

The following rules are applied when constructing the process: 

1. Every time a player in the considered team touches the ball, there is a jump in the dimension _p_ ∈ {1 _, ... ,_ 11} associated with his position. 

2. Every time a player in the considered team touches the ball inside the opposing threat area, there is a jump in the twelfth dimension at the corresponding timestamp. In this case, no jump is recorded in the component associated with the player. 

3. Once a threat state is triggered, no jumps or time are recorded until the ball exits the danger area. We resume counting the jumps when the ball is outside the danger area by at least two meters. 

4. When the ball is lost (when there is an event where the opposing team has the ball), the time and events are not recorded until the ball is won again. Upon regaining possession, we resume recording the events in our point process by adding a random duration, with an average of 12 seconds, generated from the sum of two exponential distributions of parameter six. 

5. We exclude crossing events coming from a free kick or a corner. 

Rule 3 is considered to avoid consecutive threat states. We are not interested in the auto-exciting property of the threat events. Therefore, we stop recording once a threat state is achieved and only resume when the team is outside the opposing surface by at least two meters. In Rule 4, we want to avoid having large durations where no event occurs. This is the case every time the considered team loses the ball to the opposition. Thus, the possession times of the opponent are compressed into an average of 12 seconds. The choice of the 12 seconds threshold is based on the 

average duration between events to which we add another exponential random variable as a penalization for losing the ball. The constructed point process considers possession stretches of the team to be uninterrupted. Rule 5 is implemented because the crossing events are highly correlated with threat events. In particular, the designated set piece taker of each team is naturally responsible for more threats. Therefore, we choose to discard these events to remove bias from our measure of danger creation and ensure fair player comparisons. 

Figure 2 displays an example of the resulting point process in the game of Chelsea against Manchester United on October 2022. Each line tracks the cumulative number of ball touches of a player, with the final line corresponding to the threat event. Given a collection of games of a team, the point processes built from each game are assembled into one process. The aim is to determine the hierarchical relationship between these player touches by examining the timing of their occurence. Additionally, we are interested in identifying the positions where a ball touch is directly correlated to a future jump in the twelfth dimension, which represents a threat. We also want to measure the indirect contribution of a player to the generation of threat through his interaction with other players. 

**Remark 1** (A different twelfth dimension). In this work, we have incorporated a twelfth dimension that tracks the instances of entering the opposing danger area. This is done because we want to identify the players who are responsible for creating the threat events. Our approach can be extended for various analyses by selecting an alternative twelfth state. For example, we can choose to record the timestamps of ball losses in the twelfth dimension instead of threats. This would enable us to identify the players who are most accountable for losing possession and measure the correlation between their touches and subsequent turnovers. 

Since we assemble point processes from different games, it is essential to ensure that the components of these processes correspond to the same positions across all games. In particular, the role associated with the position number _p_ can vary depending on the formation used. To maintain homogeneity between assembled game segments, the analysis is conducted only on games where each position represents the same role. This is determined by looking at the formation used in the game. Given the large number of formations and their similarity, we group them into clusters based on their structural shapes. Within each cluster, formations have the same number of players in each line, allowing for a one-to-one assignment between corresponding positions. 

> **6 —** A. Baouan et al.: Crediting football players for creating dangerous actions 



**Figure 2:** Staircase plots illustrating the cumulative number of events for each of the 11 players and the threat event over the first 8 min of the game of Chelsea against Manchester United on October 2016. 

Subsequently, we use matches from the most commonly used cluster for each team. The clusters are determined as follows: 

- Cluster 1: 433, 4,141, 4,231, 4,321. 

- Cluster 2: 442, 41,212, 451, 4,411, 4,222. 

- Cluster 3: 532, 352, 31,312, 3,511, 3,412. 

- Cluster 4: 343, 541, 3,421. 

The distribution of the positions for each formation clusters is shown in Figure 3. 

**Remark 2.** In the following, we aim at evaluating a player’s performance when he plays in a specific position. To achieve this, we only consider sequences of games where the player in question is playing in that position. We record ball touches in the other positions regardless of the identity of the player occupying them. In Section 4 and Appendix A where we analyze the interactions between the starting eleven players in given teams, we only record sequences of games where the same eleven players play in their respective positions. 

### **2.4 Immigration-birth representation** 

Introduced in (Hawkes and Oakes 1974), the immigrationbirth representation provides an intuitive way to understand linear Hawkes processes. Let us consider a stable _d_ -variate Hawkes process _N_ ( _t_ ) with a baseline intensity _𝜇_ and a kernel _𝜙_ . The law of such point process can be described through a population approach. Essentially, we 

consider a population where immigrants of _d_ types arrive at random times. Each of them gives birth to children of all types. Then the children, grand-children, grand-grandchildren etc. also give birth to children of all types. More precisely, the dynamic is constructed as follows: 

- For _j_ = 1 _,_ 2 _, ... , d_ , we consider an instance of a Poisson process with rate _𝜇 j_ , with its elements called immigrants of type _j_ . Generation 0 consists of the immigrants; 

- Recursively, given generations 0 _,_ 1 _, ... , n_ , each individual born at time _s_ of type _j_ in generation _n_ generates its offspring of type _i_ as an independent instance of a nonhomogeneous Poisson process with rate _𝜆_<sup>_s_</sup> _t_<sup>_,n_</sup> := _𝜙i, j_ ( _t_ − _s_ ) for _t_ ≥ _s_ . The union of these offspring of all types constitutes generation _n_ + 1. 

- The point process is then defined as the union of all generations. 

The resulting process has the law of a Hawkes process. In this representation, stability means each individual has less than one child on average in the case _d_ = 1, which ensures some good mathematical properties for the process. From now on, we assume that all considered Hawkes processes are stable. Additionally, under this construction, _Ki, j_ = ∫0<sup>∞</sup><sup>_𝜙i,j_(</sup><sup>_t_)d</sup><sup>_t_canbeinterpretedastheexpectednum-</sup> ber of direct children of type _i_ of an individual of type _j_ . The following proposition provides a closed-form formula for the expected number of descendants of a single individual. It includes both immediate descendants and those 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 7** 





**Figure 3:** The number associated with each position for each group of formations. 

from later generations. This result is derived similarly to the one-dimensional case in (Jaisson and Rosenbaum 2015), and allows us to quantify the average number of events originating from each jump from each dimension. 

**Proposition 1.** _The entry i, j of the matrix K(I_ − _K)_<sup>−</sup><sup>_1_</sup> _gives the expected number of descendants of type i generated by an individual of type j._ 

The immigration-birth representation is particularly powerful in the context of football event modeling as it captures the hierarchical and interdependent nature of ingame actions. Each event can be viewed as an individual that potentially triggers a cascade of subsequent events. This framework allows us to model not only the direct influence of a player’s action on future events but also the indirect effects by looking at its descendants. 

### **2.5 Generation of threat (GoT) indices** 

The immigration-birth representation of Hawkes processes explained in Section 2.4 allows us to establish connections between the events in a football match. Essentially, each ball touch or threat event can be seen as an individual in a population, that generates first-generation children of various types – ball touches from other players and threat situations. These offspring, in turn, generate additional ball 

touches or threat events etc. When we say that an event generates a ball touch or a dangerous situation, we mean that it is responsible for its occurrence. This is a subtle definition because being responsible for an action does not necessarily mean providing the pass that leads to it. In some instances, the second-to-last pass is the most crucial step in creating the dangerous situation. There may even be several events between the generating ball touch and the dangerous action. Our approach eliminates these “noisy” inbetween events and associates events through parent-child connections. Hawkes processes impute the responsibility of generating a threat to the most likely parent event, even if it occurred prior to other ball touches. In particular, they allow us to quantify the average number of dangerous actions that can be attributed to a given player. 

Using this population representation, we define the following GoT indices to assess the ability of a player to generate threat when he plays in a given position. The first two indices evaluate the impact of one touch of the player whereas the latter two measure the impact of the player’s touches over 90 min. 

#### **2.5.1 Direct GoT per touch (GoT**<sup>**(**</sup><sup>**_dir_)**</sup> **)** 

A ball touch from the player in position _p_ generates first-generation children of type threat. We refer to these instances as the _direct_ threat events generated by the player 

> **8 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

touch. We define GoT<sup>(</sup><sup>_dir_)</sup> as the average number of these threat events that occur because of one touch from player _p_ . This metric describes the intrinsic ability of the player to create dangerous situations. It can be calculated through the estimated branching matrix: 



#### **2.5.2 Indirect GoT per touch (GoT**<sup>**(**</sup><sup>**_ind_)**</sup> **)** 

A ball touch from a given player can be directly responsible for a threat event, but can also generate other ball touches that then generate danger. To quantify the total impact of a single player touch on the danger creation process, we use Proposition 1 and consider the matrix 



The coefficient _M_ 12 _, p_ represents the expected number of threat events where the ball touch from the player _p_ originates the chain of events leading to it. This includes the threat directly generated but also the one resulting from a sequence of other player touches. The difference with the GoT<sup>(</sup><sup>_dir_)</sup> index is that we credit the player touch for being at the root of the generation process and not for the crucial creative step. 



#### **2.5.3 Direct GoT per 90 min (** GoT<sup>**(**</sup> **90**<sup>**_dir_))**</sup> 

We may want to account for the involvement in the game of a given player by normalizing GoT<sup>(</sup><sup>_dir_)</sup> by his expected number of touches. We define the direct GoT per 90 min as the expected number of dangerous actions over 90 min<sup>1</sup> for which we credit the player: 



where _T_ = 90 min. The expected number of touches vector can be approximated thanks to the law of large numbers: 



#### **2.5.4 Indirect GoT per 90 min (** GoT<sup>**(**</sup> **90**<sup>**_ind_))**</sup> 

This index measures the expected number of threats over 90 min where a given player is involved in the building 

> **1** Note that here 90 min corresponds to 90 min of data after processing which does not translate to 90 min in a football match. This is notably because of the concatenation of sequences of possession explained in Section 2.3. 

circuit. We define the indirect GoT per 90 min as the average number of threat events subtracted by the average number of threat events if the considered player is removed from the pitch. The GoT90<sup>(</sup><sup>_ind_)</sup> index is therefore calculated as follows: 



where _K_<sup>(−</sup><sup>_p_)</sup> is defined as the matrix K where the _p_ th row and _p_ th column are set to zero. Likewise, _𝜇_<sup>(−</sup><sup>_p_)</sup> is defined as the vector _𝜇_ where the _p_ th coordinate is set to 0. The expected number of threats can be approximated using the branching matrix and the baseline intensity _𝜇_ : 



**Remark 3.** Calculating the _GoT_<sup>(</sup> 90<sup>_ind_)</sup> by multiplying the GoT<sup>(</sup><sup>_ind_)</sup> index by the average number of ball touches of the player would overestimate the player’s involvement in danger creation. In fact, we would count multiple times the circuits leading to threat where the player touches the ball more than once. 

Additionally, a ball touch from a player can also be responsible for generating ball touches from other players or himself. In this case as well, this is not necessarily achieved through a direct pass. Hawkes processes allow us to estimate the expected number of these generated ball touches. Similar to the GoT<sup>(</sup><sup>_dir_)</sup> index definition, the branching coefficient _K p_ 1 _, p_ 2 indicates the expected number of touches of player _p_ 1 that happen because a given ball touch from player _p_ 2 occurred before. The graphical representation of these interaction indices through a graph helps us gain a better understanding of the danger creation process. In particular, it allows us to identify the patterns of play that end in a threat. 

## **3 Maximum likelihood estimation** 

### **3.1 Likelihood of Hawkes process** 

This section describes briefly parameters estimation for multivariate Hawkes processes, see (Ogata et al. 1978, Bonnet et al. 2022b). Consider a _d_ -variate point process ( _N_ ( _t_ )) on [0 _, T_ ] with intensity of the form 



where _𝜃_<sup>∗</sup> = ( _𝜇_<sup>∗</sup> _, 𝛼_<sup>∗</sup> _, 𝛽_<sup>∗</sup> ) are some unknown parameters. Given fixed parameters _𝜃_ = ( _𝜇, 𝛼, 𝛽_ ) and a realization of the Hawkes process, the log-likelihood is calculated as follows: 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 9** 



The maximum likelihood estimator is the parameter that maximizes the above function. It can be observed from Equation (1) that the likelihood can be separated into _d_ distinct subfunctions, each dependent on the parameters _𝜇i_ and ( _𝛼i, j, 𝛽i, j_ ) _j_ =1 _,_ … _,d_ for _i_ in {1 _, ... , d_ }. As a result, the optimization can be performed separately _d_ different times to estimate each subset of parameters. It is shown in (Ogata et al. 1978) that this estimator is consistent. Additionally, the log-likelihood can be simplified in the case of exponential kernels and computed in time complexity of <sup>(</sup> _d_<sup>2</sup> _N_ ( _T_ )<sup>)</sup> , see (Ogata 1981). For example, for _d_ = 1 and _T_ = _tn_ , the likelihood is given by: 



_i_ −1 where _R_ ( _i_ ) = ∑ e<sup>−</sup><sup>_𝛽_(</sup><sup>_ti_−</sup><sup>_tj_)</sup> can be computed recursively for i _j_ =1 in {2 _, ... , n_ }: 



**Remark 4.** The likelihood function is not concave with respect to ( _𝛽k,l_ ) _k,l_ =1 _,_ … _,d_ in the exponential case. This means that convergence to the global maximum is not guaranteed, especially in large dimensions. Fixing _𝛽 k,l_ = _𝛽 k_ for all _l_ = 1 _, ... , d_ as proposed by (Bonnet et al. 2022b) produces very good results for _d_ = 12. In this case, each of the objective functions is not concave in only one parameter instead of _d_ . 

**Remark 5.** In the context of football, the effect of a ball touch on the intensity of the process should last no longer than a few seconds. When _n_ realizations of football matches are concatenated and treated as one long game, the likelihood function should not be altered by much. In fact, the rapid decay of the exponential kernel compared to the duration of games makes the induced error negligible. 

### **3.2 Simulation study** 

The goal of this section is to evaluate the maximum likelihood estimation using a simulated dataset that reproduces similar dynamics as those in a football game. We want to determine the amount of data required for an accurate estimation of the branching matrix. We also want to assess the model’s ability to detect a null kernel between two dimensions. A null kernel _𝜙i, j_ means a jump in dimension _j_ has 

no exciting effect on dimension _i_ . In the context of football, it is particularly informative to detect such an absence of connection between players. 

We perform 100 simulations over different horizons. For each simulation, the parameters are sampled as follows: 

- _𝜇_ is chosen from a uniform random variable over [0.006, 0.01]. 

- _𝛽_ is chosen to be constant for all _i, j_ in {1 _, ... ,_ 12} sampled from a uniform random variable over [0.5, 1]. 

- The _𝛼i, j_ are chosen independently from a geometric distribution of parameter _p_ = 0.4 scaled by 40 for all _i, j_ so that 40 % of the values are equal to 0. 

Then we fit a 12-dimensional Hawkes process to this data using the algorithm from (Bonnet et al. 2022b). We analyze the resulting accuracy as a function of the simulation horizon. Table 1 presents the results through three different metrics, averaged accross the 100 simulations for each horizon value: 

- False positive: Percentage of branching matrix coefficients _Ki, j_ =<sup>_𝛼_</sup> _𝛽i_<sup>_i_</sup> _,_<sup>_<u>,</u>_</sup> _j_<sup>_<u>j</u>_wronglyestimatedasnullwhen</sup><sup>_Ki,j>_</sup> 0. The estimated parameter is considered null if its value is not statistically significant, with a threshold set at 10<sup>−8</sup> . Our estimation correctly detects existing links even for small horizons. 

- Error on false negative: Our estimation consistently detects at least 50 % of null links _Ki, j_ = 0. The estimation on the remaining 50 % is generally very low as can be seen in Table 1. 

- Relative error: The weighted mean absolute percentage error when _Ki, j >_ 0. This metric is defined as the mean absolute error divided by the average value of _Ki, j_ : 



The maximum likelihood estimate is good enough for our purposes given the high dimensionality. Figure 4a shows the 

**Table 1:** Accuracy results of the maximum likelihood estimation of Hawkes parameters on the simulated datasets. 

|**Horizon (minutes)**|**False**|**Error** **on** **false**|**Relative**|
|---|---|---|---|
||**positive**|**negative**|**error**|
|300|3.1 %|0.0094|27.0 %|
|600|0.4 %|0.0063|18.6 %|
|1,200|0.0 %|0.0043|13.4 %|
|2,400|0.0 %|0.0030|9.5 %|



> **10 —** A. Baouan et al.: Crediting football players for creating dangerous actions 









**Figure 4:** Heatmaps of the true branching matrix and the estimated one from a simulation of horizon 600 min. 

estimated branching matrix from a simulation of horizon 600 min. We observe that the estimated branching matrix appears to correctly approximate the true branching matrix in Figure 4b. 

## **4 Analysis of Chelsea FC in the 2016–2017 season** 

As a first example, we perform our analysis on a selection of Chelsea FC matches from the 2016–2017 season. The team had a stable formation and a constant starting 11 over 13 games in the Premier League. This is quite convenient because we retrieve a large amount of data where each position _p_ in {1 _, ... ,_ 11} is associated with one player. Similar analysis for Stade Rennais in the 2021–2022 season is provided in Appendix A. 

**Table 2:** List of selected games with the same starting 11 for Chelsea FC. 

|**Date**|**Opponent**|**Home** **or**<br>**away**|**Competition**|
|---|---|---|---|
|Oct 15, 2016|Leicester City|Home|English Premier League|
|Oct 23, 2016|Manchester United|Home|English Premier League|
|Oct 30, 2016|Southampton|Away|English Premier League|
|Nov 5, 2016|Everton|Home|English Premier League|
|Nov 20, 2016|Middlesbrough|Away|English Premier League|
|Nov 26, 2016|Tottenham Hotspur|Home|English Premier League|
|Dec 11, 2016|West Bromwich Albion|Home|English Premier League|
|Jan 4, 2017|Tottenham Hotspur|Away|English Premier League|
|Jan 22, 2017|Hull City|Home|English Premier League|
|Feb 4, 2017|Arsenal|Home|English Premier League|
|Feb 12, 2017|Burnley|Away|English Premier League|
|Apr 8, 2017|Bournemouth|Away|English Premier League|
|Apr 30, 2017|Everton|Away|English Premier League|



### **4.1 Selected games** 

### **4.2 Results and discussion** 

In Table 2, we give the list of selected games for Chelsea FC. In each of these games, the flat 343 formation is used for at least 60 minutes and the starting 11 remains the same: 

- Thibaut Courtois. 

- Gary Cahill – David Luiz – Cesar Azpilicueta. 

- Marcos Alonso – Nemanja Matic – N’Golo Kante – Victor Moses. 

- Eden Hazard – Diego Costa – Pedro Rodriguez. 

Therefore, we use the data before the first substitution from Chelsea FC in each game to build the counting process. 

In Table 3, we display the different GoT indices for the Chelsea players. We include Monte Carlo estimates of the standard error (SE) for the indices. Using the estimated parameters, we generate 100 sample paths of the same length as the original dataset, and then the parameters are re-estimated again. Figure 5 graphically represents the direct interactions between players as well as their GoT<sup>(</sup><sup>_ind_)</sup> indices and Figure 6 shows the estimated branching matrix. We can identify two buildup schemes along the wings with two triangles: Cahill-Alonso-Matic and 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 11** 

Kante-Azpilicueta-Moses. The main channel of communication between both sides is based on the Matic-Kante link. Below is a list of observations on players: 

**Table 3:** Generated threat metrics for the players of Chelsea FC. The table is sorted by GoT<sup>(</sup> 90<sup>_ind_).</sup> 

|**Player** **name**|**GoT** <sup>**(**</sup><sup>**_dir_)** </sup>**(SE)**|**GoT** <sup>**(**</sup><sup>**_ind_)** </sup>**(SE)**|GoT <sup>**(** </sup><sup>**_dir_** </sup><sup>**)**</sup><br>**90**<br>**(SE)**|GoT <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**<br>**(SE)**|
|---|---|---|---|---|
|Eden Hazard|0.16 (0.020)|0.21 (0.025)|14.2 (2.019)|15.0 (2.060)|
|Victor Moses|0.07 (0.017)|0.11 (0.021)|5.7 (1.471)|7.5 (1.500)|
|Pedro Rodriguez|0.08 (0.016)|0.12 (0.020)|5.5 (1.218)|6.7 (1.277)|
|N’Golo Kante|0.02 (0.012)|0.07 (0.016)|2.7 (1.351)|6.2 (1.399)|
|Nemanja Matic|0.01 (0.010)|0.06 (0.014)|1.5 (1.082)|5.2 (1.244)|
|Marcos Alonso|0.02 (0.011)|0.06 (0.016)|1.9 (1.095)|5.1 (1.296)|
|Diego Costa|0.07 (0.022)|0.10 (0.028)|3.6 (1.214)|4.8 (1.256)|
|Cesar Azpilicueta|0.00 (0.005)|0.04 (0.009)|0.0 (0.581)|4.1 (0.812)|
|Gary Cahill|0.00 (0.006)|0.04 (0.010)|0.0 (0.550)|3.0 (0.842)|
|David Luiz|0.00 (0.005)|0.01 (0.008)|0.0 (0.492)|1.0 (0.591)|
|Thibaut Courtois|0.00 (0.006)|0.01 (0.009)|0.0 (0.334)|0.6 (0.373)|



#### **4.2.2 N’Golo Kante** 

Ranking fourth in GoT<sup>(</sup> 90<sup>_ind_)</sup> is evidence to Kante’s important role in Chelsea’s success in the 2016–2017 season. The winner of the PFA Players’ Player of the Year 2017 award is definitely not limited to defense as the numbers show that he is largely involved in danger creation. This is explained by the fact that Kante is a box to box midfielder and that he is at the center of multiple circuits that end in a threat: 

- Kante → Pedro → Threat. 

- Kante → Moses → Pedro → Threat. 

- Kante → Matic → Hazard → Threat. 

#### **4.2.3 David Luiz** 

The contribution of the central defender David Luiz in the generation of threat is minimal. This is not surprising as the flat 3-4-3 system relies heavily on the wings. David Luiz naturally passes the ball to either Gary Cahill or Azpilicueta in the build-up to spread the play. 

#### **4.2.1 Eden Hazard** 

#### **4.2.4 Diego Costa** 

Unsurprisingly, the offensive player, ranked second in the PFA Players’ Player of the Year 2017 award, leads all GoT metrics. In particular, there is no significant difference between his GoT<sup>(</sup> 90<sup>_dir_)</sup> and GoT<sup>(</sup> 90<sup>_ind_)</sup> indices, indicating that his primary way of creating danger is through direct threat. Hazard was well known for his aggressive and direct play as well as for his dribbling. 

Costa generates a small number of threats despite being a striker. This is expected as he is responsible for transforming the goalscoring chances rather than being at the origin of the danger. Moreover, his GoT<sup>(</sup> 90<sup>_ind_)</sup> statistic is particularly low since he has a low number of touches per time unit and many of his touches in the danger zone are not recorded in the constructed counting process. 





**Figure 5:** Graph summarizing the interactions between Chelsea players. The width of an arrow from player _p_ 1 to player _p_ 2 is proportional to the expected number of touches of player _p_ 2 generated by one touch from player _p_ 1. The size of the circle of player _p_ is proportional to the sum of the arrow sizes received, indicating the involvement of the player in the considered games. The color of the circle represents the GoT<sup>_i_</sup> index for each player. 

> **12 —** A. Baouan et al.: Crediting football players for creating dangerous actions 





**Figure 6:** Estimated branching matrix for Chelsea FC. 

We can clearly see that considering indirect contribution to threat generation is important for defenders and midfielders. These positions are generally at the base of the danger creation process. They have small GoT<sup>(</sup><sup>_dir_)</sup> indices. However, indirect generated threat combined with the consideration of the number of touches allows us to effectively compare players playing in deeper positions. 

From the graphical representation in Figure 5, we can identify some patterns that lead to a dangerous situation. When facing a team like Chelsea in the 2016–2017 season, some strategies can be derived from this analysis: 

- As illustrated in Figure 5, the right side of Chelsea combines a lot for threat generation and should be disrupted at the root. Azpilicueta should be stopped from feeding the ball to the midfielders or directly to Pedro. 

- The left side relies much more on the direct offensive output of Eden Hazard. In fact, all of Gary Cahill, Matic and Marcos Alonso mostly aim at delivering the ball to the left winger. To neutralize the threat of the left side, it is essential to prevent the ball from reaching Hazard. This can be achieved by marking him closely or by constantly closing the passing lanes to him. 

- Goalkeeper Courtois is successful in targetting Marcos Alonso directly. This passing pattern should be considered when pressing Chelsea. 

consider for each team the games where they use their main formation cluster, see Table 12 in Appendix B for the list of formation clusters of each team. 

### **5.1 Generated threat to rank players in a position** 

Each position on the pitch imposes a different role on the player who occupies it. In particular, we cannot expect the same player to produce the same GoT metrics at two different positions. Therefore, we choose to evaluate players when they play in a particular position. This approach will also allow us to determine the optimal position for a player to maximize a GoT metric of interest. Additionally, we apply a filter to consider only players who play at least 600 min at a given position, with playing time calculated based on games in which the player features for at least 45 min. 

Given a player and a position, we record the games in which the player occupies the position. The remaining positions may feature different players at each game. Whenever a player from his team is substituted, we do not consider the rest of the game in the construction of the counting process. We fit a Hawkes process and assign to the player the generated threat indices of his position. Tables 4 and 5 present the top 20 players in Ligue 1 in terms of GoT<sup>(</sup><sup>_dir_)</sup> and GoT<sup>(</sup> 90<sup>_ind_)</sup> , respectively (see Tables 10 and 11 in Appendix B for the Top 100). The tables also include Monte Carlo estimates of the standard error using 100 samples. We display these two indices because they quantify the two extremes of the danger generation process. GoT<sup>(</sup><sup>_dir_)</sup> isolates the direct impact of players while GoT<sup>(</sup> 90<sup>_ind_)</sup> measures their participation in the chain of events leading to threats. 

In reference to the results in Section 3.2, one should keep in mind that the fewer minutes a player plays in a position, the less accurate the estimate of his generated threat is. Moreover, our estimation relies on selected games only. When a player has a limited number of minutes in a position, a good GoT metric should be interpreted as a measure of performance across the considered games only. For example, Moses Simon ranking third in GoT<sup>(</sup><sup>_dir_)</sup> should not be surprising as he provided seven assists in the 1,200 min but only gave one more assist in the remaining games when the team plays in a different formation or when he plays in a different position. 

Below are some observations based on the results: 

## **5 Ligue 1 2021–22 season analysis** 

#### **5.1.1 GoT**<sup>**(**</sup><sup>**_dir_)**</sup> **versus** GoT<sup>**(**</sup><sup>**_ind_)**</sup> **90** 

In this section, we provide a ranking of players and teams from Ligue 1 in the 2021–2022 season based on their generation of threat. To maintain homogeneity, we only 

GoT<sup>(</sup><sup>_dir_)</sup> captures the intrinsic ability of a player to advance the ball to the opponent’s danger area while GoT<sup>(</sup> 90<sup>_ind_)</sup> 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 13** 

**Table 4:** Ranking of Ligue 1 players in terms of GoT<sup>(</sup><sup>_dir_)</sup> . 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|**GoT** <sup>**(**</sup><sup>**_dir_)** </sup>**(SE)**|
|---|---|---|---|---|---|
|1|Lionel Messi<br>|10|Paris Saint-Germain|630|0.130 (0.025)|
|2|Ángel Di María|10|Paris Saint-Germain|1,171|0.128 (0.020)|
|3|Moses Simon|11|Nantes|1,222|0.120 (0.024)|
|4|Kylian Mbappé|9|Paris Saint-Germain|1,338|0.110 (0.026)|
|5|Lionel Messi|9|Paris Saint-Germain|675|0.109 (0.023)|
|6|Martin Terrier|11|Rennes|1,386|0.108 (0.017)|
|7|Kylian Mbappé|11|Paris Saint-Germain|1,066|0.107 (0.020)|
|8|Romain Faivre|7|Brest|630|0.106 (0.024)|
|8|Houssem Aouar|7|Lyon|810|0.106 (0.023)|
|10|Sofiane Boufal|9|Angers|771|0.100 (0.020)|
|11|Jonathan Ikoné|7|Lille|767|0.096 (0.024)|
|12|Wissam Ben Yedder|9|Monaco|1,625|0.094 (0.020)|
|13|Franck Honorat|11|Brest|838|0.093 (0.021)|
|13|Karl Toko-Ekambi|11|Lyon|1,855|0.093 (0.015)|
|15|Benjamin Bourigeaud|10|Rennes|1,719|0.092 (0.014)|
|16|Sofiane Boufal|11|Angers|665|0.091 (0.024)|
|17|Justin Kluivert|11|Nice|1,207|0.090 (0.020)|
|19|Dimitri Payet|9|Marseille|617|0.088 (0.022)|
|19|Kevin Gameiro|10|Strasbourg|673|0.088 (0.024)|
|19|Neymar|11|Paris Saint-Germain|1,258|0.088 (0.014)|



**Table 5:** Ranking of Ligue 1 players in terms of GoT<sup>(</sup> 90<sup>_ind_).</sup> 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|GoT <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**<br>**(SE)**|
|---|---|---|---|---|---|
|1|Lionel Messi|10|Paris Saint-Germain|630|14.911 (2.816)|
|2|Ángel Di María|10|Paris Saint-Germain|1,171|13.218 (2.045)|
|3|Neymar|11|Paris Saint-Germain|1,258|12.724 (1.709)|
|4|Marco Verratti|4|Paris Saint-Germain|602|12.581 (2.655)|
|5|Lionel Messi|9|Paris Saint-Germain|675|12.353 (2.338)|
|6|Romain Faivre|7|Brest|630|10.402 (2.412)|
|7|Houssem Aouar|7|Lyon|810|10.077 (2.014)|
|8|Téji Savanier|7|Montpellier|2,209|9.608 (1.294)|
|9|Marco Verratti|8|Paris Saint-Germain|1,069|9.446 (1.442)|
|10|Jason Berthomier|7|Clermont|1,244|9.340 (1.305)|
|11|Benjamin Bourigeaud|10|Rennes|1,719|9.211 (1.228)|
|12|Sofiane Boufal|9|Angers|771|9.100 (1.799)|
|13|Bruno Guimarães|4|Lyon|900|8.817 (1.995)|
|14|Dimitri Payet|9|Marseille|617|8.815 (2.021)|
|15|Moses Simon|11|Nantes|1,222|8.790 (1.806)|
|16|Martin Terrier|11|Rennes|1,386|8.639 (1.335)|
|17|Kylian Mbappé|11|Paris Saint-Germain|1,066|8.577 (1.657)|
|18|Frédéric Guilbert|2|Strasbourg|2,428|8.421 (1.002)|
|19|Ruben Aguilar|2|Monaco|1,205|8.019 (1.417)|
|20|Lovro Majer|7|Rennes|1,302|7.927 (1.321)|



> **14 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

#### **5.1.6 Optimal position for some players** 

incorporates possible combinations with teammates. There- **5.1.6 Optimal position for some players** fore, the style of play and the ability of teammates can have an impact on the value of GoT<sup>(</sup> 90<sup>_ind_)</sup> . These two indices Romain Faivre stands out in both GoT<sup>(</sup><sup>_dir_)</sup> and GoT<sup>(</sup> 90<sup>_ind_),</sup> describe different ways to contribute to threat generation ranking among the top 20 players. This is in fact expected and allow us to select different profiles of players. For because, when playing as a right midfielder in the 442 forexample, the Paris Saint-Germain midfielder Verratti promation of Brest, the player performed well and was involved duces high values of GoT<sup>(</sup> 90<sup>_ind_)</sup> while Moses Simon from FC in six goals in just 660 min. Similarly, Houssem Aouar was Nantes features in the top positions in terms of GoT<sup>(</sup><sup>_dir_)</sup> . successful as an interior midfielder in the 433 formation. He scored three and assisted three more in the considered period, earning him a top spot on our list. 

#### **5.1.2 Jason Berthomier as a surprising pick** 

In his only season in Ligue 1, Jason Berthomier delivered excellent values of GoT<sup>(</sup> 90<sup>_ind_)</sup> . The Clermont Foot midfielder ranks 43rd in terms of GoT<sup>(</sup><sup>_dir_)</sup> and climbs up to the tenth position in the GoT<sup>(</sup> 90<sup>_ind_)</sup> ranking. This proves that he is consistently involved in the generation of dangerous situations for his team and is successful in feeding the forward players. 

#### **5.1.3 Téji Savanier excels in midfield** 

Téji Savanier stands out as an interior midfielder in the 433 formation of Montpellier. With eight goals and seven assists, it is no surprise that he is central to the process of threat generation of his team. He ranks eighth in GoT<sup>(</sup> 90<sup>_ind_)</sup> and outperforms many offensive players in the league. This confirms the quality of Téji Savanier and his good performance during the 2021–2022 season. 

#### **5.1.4 A defender in the top 20** 

Frederic Guilbert of Strasbourg is a defender who excels at creating threats, ranking 18th in GoT<sup>(</sup> 90<sup>_ind_)</sup> . In fact, his team deploys a 532 formation that provides enough cover for the fullbacks to play offensively. The same holds for Jonathan Clauss who acts almost as a right midfielder in the Lens formation and ranks 33rd in GoT<sup>(</sup> 90<sup>_ind_)</sup> . This is also not surprising as Clauss ranks third in the league in the number of passes that lead to a shot, another proof of his creative play. 

#### **5.1.5 A good season from Messi in generated threat** 

Despite underperforming in terms of scoring goals, Lionel Messi delivers outstanding values of generated threat both directly given his dribbling and passing quality, and indirectly given his involvement in ball possession. Additionally, we observe that his performance increases slightly when playing in his natural position as a 10 in the 433 formation. The right wing is Messi’s best position as he poses more of a threat cutting inside from the right. 

#### **5.1.7 A metric that does not value center forwards** 

Very few strikers make the Top 20 in the two metrics. This is because the role of some center forwards is to receive the ball in the danger area and not necessarily to be at the origin of the threat. This is even more pronounced when looking at GoT<sup>(</sup> 90<sup>_ind_)</sup> . For example, Mbappé, the top scorer in the league, barely makes it to the Top 20. Mbappe is not known for participating in possession and touching the ball a lot but as an aggressive transition player. In contrast, midfielders such as Verratti and Guimarães, that are involved in the build-up of a lot of dangerous situations, feature in the top positions in terms of GoT<sup>(</sup><sup>_ind_)</sup> 90<sup>.</sup> 

### **5.2 Ranking the central defenders’ involvement in terms of GoT** 

To quantify the involvement of central defenders in danger creation, we use the indirect generation of threat per 90 min. This is because the direct generation of threat (GoT<sup>(</sup><sup>_dir_)</sup> ) values are particularly low for defenders and therefore cannot be used to compare players. While GoT<sup>(</sup> 90<sup>_ind_)</sup> is influenced by the quality of the offensive players and team style of play, it also provides valuable information on the role of defenders in the team’s build-up scheme. For instance, a center-back who is technically proficient but avoids taking risks and does not contribute much to ball progression will have a low value of GoT<sup>(</sup> 90<sup>_ind_)</sup> . This metric strikes a balance in measuring a player’s intrinsic ability as well as their involvement within the team. Table 6 displays the Top 10 best central defenders with the highest values of GoT<sup>(</sup><sup>_ind_)</sup> 90<sup>.</sup> 

It is no surprise that Marquinhos and Kimpembe take the first two spots, given that they are part of Paris SaintGermain, the most dominant team in Ligue 1. This is of course due to their technical ability, but there is also a factor due to the high possession values and danger creation ability of their team. The same holds for Nayef Aguerd and Warmed Omari that contribute significantly to ball progression, primarily through accurate long balls. The third-placed 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 15** 

**Table 6:** Ranking of Ligue 1 central defenders in terms of GoT<sup>(</sup> 90<sup>_ind_).</sup> 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|GoT <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**<br>**(SE)**|
|---|---|---|---|---|---|
|1|Marquinhos|5|Paris Saint-Germain|2,340|5.625 (0.805)|
|2|Presnel Kimpembe|6|Paris Saint-Germain|1,840|5.230 (0.747)|
|3|Facundo Medina|4|Lens|1,329|4.953 (1.008)|
|4|Nayef Aguerd|6|Rennes|1,698|4.908 (0.694)|
|5|William Saliba|5|Marseille|1,800|4.652 (0.756)|
|6|Jason Denayer|6|Lyon|630|4.591 (1.075)|
|7|Jonathan Gradit|6|Lens|1,710|4.535 (0.739)|
|8|Warmed Omari|5|Rennes|1,710|4.407 (0.747)|
|9|Damien Da Silva|5|Lyon|612|4.182 (1.458)|
|10|Dante|6|Nice|2,880|3.707 (0.609)|
|11|Duje Caleta-Car|6|Marseille|1,397|3.462 (0.715)|
|12|Lucas Perrin|6|Strasbourg|2,329|3.185 (0.614)|
|13|Kevin Danso|5|Lens|1,620|3.105 (0.651)|
|14|Benoît Badiashile|6|Monaco|975|3.075 (0.762)|
|15|Castello Lukeba|6|Lyon|1,375|3.074 (0.693)|
|16|Mamadou Sakho|6|Montpellier|1,962|2.998 (0.554)|
|17|Florent Ogier|6|Clermont|2,329|2.949 (0.526)|
|18|Guillermo Maripán|6|Monaco|810|2.916 (0.989)|
|19|Guillermo Maripán|5|Monaco|605|2.915 (1.486)|
|20|Jean-Clair Todibo|5|Nice|3,123|2.864 (0.526)|



is Facundo Medina. The Lens defender is well known for his range of passing and for his ability to switch play from one side to the other. In particular, he ranks tenth in the league in terms of accurate passes per 90 min. William Saliba naturally completes the Top 5. The Marseille player excels with the ball at his feet and ranks third in accurate passing in Ligue 1. The player has now moved to Arsenal, a team that likes to play from the back, and continues to deliver in that aspect of the game. 

### **5.3 GoT**<sup>**(**</sup><sup>**_dir_)**</sup> **to rank teams** 

To verify the consistency of our metrics, we rank Ligue 1 teams based on their aggregate values of GoT<sup>(</sup><sup>_dir_)</sup> . This metric can be considered as an indicator of squad quality. For each club, we fit a 12-dimensional Hawkes process to all matches in which they use their primary formation cluster, regardless of the players occupying each position. We then sum the estimated direct threat per touch GoT<sup>(</sup><sup>_dir_)</sup> for all the positions. 

Table 7 shows the resulting Top 10 based on generated threat. Our metric describes an important part of the offensive performance but obviously does not cover all aspects of the game. Nevertheless, it remains a very good measure of the quality of the team. Our ranking shows a significant 

**Table 7:** Top 10 Ligue 1 teams with respect to aggregated GoT<sup>(</sup><sup>_dir_)</sup> of starting eleven. 

|**Team**|**GoT** <sup>**(**</sup><sup>**_dir_)** </sup>**(SE)**|**Ligue** **1** **ranking**|**Goals** **scored**|
|---|---|---|---|
|Paris Saint-Germain|0.42 (0.024)|1|90|
|Rennes|0.41 (0.027)|4|82|
|Monaco|0.41 (0.035)|3|65|
|Lyon|0.36 (0.025)|8|66|
|Marseille|0.36 (0.033)|2|63|
|Lens|0.30 (0.029)|7|62|
|Nice|0.28 (0.023)|5|52|
|Strasbourg|0.26 (0.021)|6|60|
|Lille|0.26 (0.022)|10|48|
|Reims|0.26 (0.035)|12|43|



62 % Kendall correlation with the realized ranking of Ligue 1. This is achieved while only looking at ball touch and threat event timestamps to infer player abilities. Below are some observations from the ranking: 

- Rennes climbs to the second position in our ranking. This is because the team was very attack-minded in the 2021–2022 season and managed to score 82 goals, one of the highest totals in Europe. Their expected threat is proof of their offensive output. 

> **16 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

– Olympique Lyonnais, ranked eighth in Ligue 1, still had a very prolific season offensively. They have the thirdhighest total of goals and the second-highest total of expected goals. It is therefore natural they are fourth with respect to our offensive metric. 

## **6 Conclusion and future work** 

In order to measure a player’s ability to create threat in football, we develop model-based metrics that rely on Hawkes processes. These processes provide an easy to interpret way to capture hierarchy between event times. Thanks to this modeling, we are able to identify the players whose touches are most consistently correlated with subsequent threats. We derive four different metrics each describing different ways to create danger. On the one hand, the direct generation of threat metrics GoT<sup>(</sup><sup>_dir_)</sup> and GoT<sup>(</sup><sup>_dir_)</sup> allow us to 90 isolate the intrinsic ability of players. On the other hand, GoT<sup>(</sup><sup>_ind_)</sup> and GoT<sup>(</sup><sup>_ind_)</sup> indicate the indirect contribution to 90 the generation of threat through interactions with other positions. Beyond crediting players for danger generation, our approach can also be used to quantify and visualize the synergies between players on the pitch and identify the patterns that lead to dangerous situations. 

We demonstrate our methodology can successfully detect and rank the key players in the 2021–2022 Ligue 1 season, who contribute to their team’s offensive output. The results we find are consistent with the observed performances of the retrieved players, but also reveal some surprising choices. Through the example of Chelsea in the 2016–2017 season, we show that our model-based approach can help teams make data-driven decisions about their tactics. By primarily looking at timestamps of ball touches, we gain a deeper understanding of the threat generation process of a team. 

Our methodology can be adapted to study the dynamics of other sports that have available event data. This is particularly valid for sports where the set of players on the pitch is relatively stable like football. This stability allows us to construct counting processes where each component consistently corresponds to the same player. Applying this approach to basketball, for example, presents additional challenges due to the high frequency of substitutions. To address this, one strategy is to design a point process where each component tracks the events of a specific role (point guard, shooting guard, small forward, power forward, center) regardless of the player’s identity. This approach is similar to the analysis presented in Section A of the Appendix. Metrics estimated for each role can then be attributed to the player occupying that position the most during the game. 

Furthermore, a notable advantage in basketball is that the frequent scoring events can be used to represent threats. 

Future work will include exploring the application of our model-based metrics for optimal team selection. In fact, if we are capable of inferring the branching matrix parameters linking players from different teams, we can measure the impact of a potential transfer on the danger creation process. In addition, we can use this framework to capture interactions of players with other game states different from threats. In particular, by replacing the threat events with ball losses, we can effectively analyze the defensive aspect of the game and determine players whose touches are most correlated with a turnover. 

**Acknowledgments:** The authors thank Anna Bonnet for her help with the estimation of Hawkes processes in large dimensions. They are also grateful to Charlotte Dion and Céline Duval. 

##### **Research ethics:** Not applicable. 

##### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

##### **Use of Large Language Models, AI and Machine Learning** 

**Tools:** None declared. 

**Conflict of interest:** The authors state no conflict of interest. **Research funding:** The authors gratefully acknowledge financial support from the chairs “Machine Learning & Systematic Methods in Finance” and “Deep Finance and Statistics”. 

**Data availability:** The data are not publicly available. 

## **Appendix** 

### **A: Stade Rennais** 

In this appendix, we present a detailed analysis of one of the Ligue 1 teams in the 2021–2022 season. 

### **A.1: Selected games** 

In the same spirit as Section 4, we choose a collection of games where the formation is the same and starting lineup is as stable as possible. Table 8 shows the selected matches for Stade Rennais. The team plays in a 433 formation in all of these games but the starting 11 is not always exactly the same. In fact, some players are sometimes rotated for a game or two, but we assume that the substitute behaves approximately the same as the starting player. Stade 

A. Baouan et al.: Crediting football players for creating dangerous actions **— 17** 

**Table 8:** List of selected games for Stade Rennais F.C. 

|**Date**|**Opponent**|**Home or away**|**Competition**|
|---|---|---|---|
|May 11, 2022|Nantes|Away|French Ligue 1|
|Apr 2, 2022|Nice|Away|French Ligue 1|
|May 14, 2022|Marseille|Home|French Ligue 1|
|Dec 22, 2021|Monaco|Away|French Ligue 1|
|Mar 20, 2022|Metz|Home|French Ligue 1|
|Apr 15, 2022|Monaco|Home|French Ligue 1|
|Apr 30, 2022|St Etienne|Home|French Ligue 1|
|Apr 24, 2022|Lorient|Home|French Ligue 1|
|Nov 20, 2021|Montpellier|Home|French Ligue 1|
|May 21, 2022|Lille|Away|French Ligue 1|
|Nov 7, 2021|Lyon|Home|French Ligue 1|



**Table 9:** Generated threat metrics for the players of Stade Rennais. The table is sorted by GoT90<sup>(</sup><sup>_ind_).</sup> 

|**Player** **name**|**GoT** <sup>**(**</sup><sup>**_dir_)**</sup>|**GoT** <sup>**(**</sup><sup>**_ind_)**</sup>|**GoT** <sup>**(** </sup><sup>**_dir_** </sup><sup>**)**</sup><br>**90**|**GoT** <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**|
|---|---|---|---|---|
|Benjamin Bourigeaud|0.14|0.16|11.8|12.6|
|Martin Terrier|0.13|0.17|8.6|9.5|
|Lovro Majer|0.08|0.11|6.9|8.1|
|Flavien Tait|0.06|0.09|5.5|7.2|
|Adrien Truffert|0.02|0.06|2.4|5.2|
|Hamari Traoré|0.01|0.05|1.5|4.6|
|Nayef Aguerd|0.00|0.04|0.0|4.5|
|Baptiste Santamaría|0.00|0.05|0.4|4.3|
|Warmed Omari|0.00|0.04|0.0|4.0|
|Gaëtan Laborde|0.04|0.08|2.0|3.0|
|Alfred Gomis|0.00|0.01|0.0|0.7|



Rennais line up as follows in the selected games, where the main player in each position is in bold: 

### **A.2: Results and discussion** 

- **Gomis** /Alemdar 

- **Traore** – **Omari** /Bade – **Aguerd** /Bade/Santamaria – **Truffert** /Meling 

- **Majer** – **Santamaria** /Martin – **Tait** 

- **Bourigeaud** – **Laborde** /Guirassy – **Terrier** 

We construct a 12-dimensional counting process from the selected Stade Rennais games regardless of the players starting. We use the data from each game as long as the 11 players on the pitch correspond to the scheme provided above. We then fit a 12-dimensional Hawkes process and associate the estimated metrics of each position with the main player occupying it. 

In Table 9, we rank the Stade Rennais players with respect to generated threat metrics. Figure 7 graphically represents the direct interactions between them and Figure 8 displays the estimated branching matrix. We can see that the team adopts a 433 shape that progresses mainly through the wings. The danger creation is asymmetric with more combinations occurring on the right side, where Majer is the most creative midfielder. Interestingly, despite being a central midfielder, Flavien Tait delivers a large value of GoT<sup>(</sup> 90<sup>_ind_)</sup> , indicating that he is a significant contributor to the team’s offensive efforts. In contrast, although Santamaria has more possession, he has 





**Figure 7:** Graph summarizing the interactions between Stade Rennais players. The width of an arrow from player _p_ 1 to player _p_ 2 is proportional to the expected number of touches of player _p_ 2 generated by one touch from player _p_ 1. The size of the circle of player _p_ is proportional to the sum of the arrow sizes received, indicating the involvement of the player in the considered games. The color of the circle represents the GoT<sup>_i_</sup> index for each player. 

> **18 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

limited involvement in creating threats. This difference in their threat generation can be attributed to their distinct roles on the field. On one hand, Tait is a more box-to-box midfielder who frequently projects forward and has a considerable direct threat metric. On the other hand, Santamaria belongs to a class of defensive midfielders who act as anchor points. They participate in the buildup close to the center backs and have limited interactions with the forward positions. 

The main threat sources are Bourigeaud, Majer, and Terrier. These three players are outstanding going forward. Terrier is the leader of the team in goalscoring and ranks third in Ligue 1 but seems to be involved in danger creation as well. Bourigeaud generating the most threat is not surprising since he is the creative force of the team. In fact, he ranks first in the league in terms of key passes with 3.2 per game, and first in accurate crosses with 104 in the season. 

As expected, the center backs have zero direct threat contribution. However, in terms of indirect threat per 90 min GoT<sup>(</sup> 90<sup>_ind_)</sup> , Aguerd and Omari rank fourth and sixth in the team respectively. The pair generates danger through their involvement in team build-up and possession. In particular, Aguerd and Omari are comfortable with the ball at their feet and rank eighth and twentieth in the league, respectively, in the number of passes per game with high success rates. 

Finally, we can observe from Figure 7 some remarkable circuits that lead to dangerous situations. These patterns of play should be taken into account by an opposing team when facing Stade Rennais: 

- Aguerd → Truffert → Terrier → Threat. 

- Terrier → Tait → Threat. Terrier is highly effective in generating direct threats, but he also frequently combines with Flavien Tait to create danger. Similarly, 

Bourigeaud often gives the ball to Lovro Majer to generate indirect threat. 

– Omari → Traoré → Bourigeaud → Threat. 

– Omari → Bourigeaud → Threat. This is a straightforward pattern from defense to attack that should be controlled. Omari is highly successful in progressing the ball, both through slow build-up play by passing the ball to the right-back Traoré, as well as through fast transitions with direct passes to Bourigeaud. 

### **B: Top 100 ranking of Ligue 1 player in terms of GoT** 

See Tables 10 and 11. 





**Figure 8:** Estimated branching matrix for Stade Rennais. 

**Table 10:** Ranking of Ligue 1 players in terms of GoT<sup>(</sup><sup>_dir_)</sup> . 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|**GoT** <sup>**(**</sup><sup>**_dir_)**</sup>|
|---|---|---|---|---|---|
|1|Lionel Messi|10|Paris Saint-Germain|630|0.130|
|2|Ángel Di María|10|Paris Saint-Germain|1,171|0.128|
|3|Moses Simon|11|Nantes|1,222|0.120|
|4|Kylian Mbappé|9|Paris Saint-Germain|1,338|0.110|
|5|Lionel Messi|9|Paris Saint-Germain|675|0.109|
|6|Martin Terrier|11|Rennes|1,386|0.108|
|7|Kylian Mbappé|11|Paris Saint-Germain|1,066|0.107|
|8|Romain Faivre|7|Brest|630|0.106|
|8|Houssem Aouar|7|Lyon|810|0.106|
|10|Sofiane Boufal|9|Angers|771|0.100|
|11|Jonathan Ikoné|7|Lille|767|0.096|
|12|Wissam Ben Yedder|9|Monaco|1,625|0.094|



A. Baouan et al.: Crediting football players for creating dangerous actions **— 19** 

**Table 10:** (continued) 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|**GoT** <sup>**(**</sup><sup>**_dir_)**</sup>|
|---|---|---|---|---|---|
|13|Franck Honorat|11|Brest|838|0.093|
|13|Karl Toko-Ekambi|11|Lyon|1,855|0.093|
|15|Benjamin Bourigeaud|10|Rennes|1,719|0.092|
|16<br>|Sofiane Boufal<br>|11<br>|Angers<br>|665<br>|0.091<br>|
|17|Justin Kluivert|11|Nice|1,207|0.090|
|19|Dimitri Payet|9|Marseille|617|0.088|
|19|Kevin Gameiro|10|Strasbourg|673|0.088|
|19|Neymar|11|Paris Saint-Germain|1,258|0.088|
|21|Jodel Dossou|10|Clermont|1,762|0.086|
|22|Lucas Da Cunha|10|Clermont|606|0.084|
|22|Jim Allevinah|11|Clermont|858|0.084|
|24|Frédéric Guilbert|2|Strasbourg|2,428|0.082|
|25|Armand Laurienté|9|Lorient|842|0.080|
|26|Ludovic Blas|7|Nantes|810|0.078|
|27|Gaël Kakuta|9|Lens|976|0.077|
|28|Arnaud Kalimuendo-Muinga<br>|11|Lens|724|0.075|
|29|Cengiz Ünder|10|Marseille|1,047|0.074|
|29|Florent Mollet|10|Montpellier|1,269|0.074|
|31|Téji Savanier|7|Montpellier|2,209|0.071|
|32|Ghislain Konan|3|Reims|1,007|0.070|
|33|Lovro Majer|7|Rennes|1,302|0.068|
|34|Kevin Volland|7|Monaco|1,131|0.067|
|34|Jonathan Clauss|2|Lens|1,940|0.067|
|36|Angelo Fulgini|8|Angers|630|0.066|
|36|Andy Delort|10|Nice|1,478|0.066|
|38|Javairô Dilrosun|9|Bordeaux|675|0.064|
|39|Vanderson|10|Monaco|619|0.061|
|40|Lucas Paquetá|7|Lyon|1,248|0.060|
|40|Burak Yilmaz|9|Lille|1,900|0.060|
|43|Jonathan Bamba|11|Lille|1,763|0.059|
|43|Thomas Foket|2|Reims|631|0.059|
|43|Jason Berthomier|7|Clermont|1,244|0.059|
|45|Amine Gouiri|9|Nice|1,749|0.058|
|46|Gaëtan Laborde|9|Rennes|1,305|0.057|
|47|Ibrahima Sissoko|7|Strasbourg|826|0.055|
|48|Jonathan David|10|Lille|2,072|0.054|
|49|Dimitri Lienard|3|Strasbourg|1,728|0.050|
|51|Flavien Tait|8|Rennes|1,129|0.046|
|51|Florian Sotoca|10|Lens|1,119|0.046|
|51|Jérémy Le Douaron|10|Brest|759|0.046|
|53|<br>Andy Delort|9|Nice|795|0.045|
|55|Youcef Atal|2|Nice|1,032|0.044|
|55|Randal Kolo Muani|9|Nantes|876|0.044|
|55|Stephy Mavididi|11|Montpellier|1,585|0.044|
|55|Aleksandr Golovin|11|Monaco|607|0.044|
|58|Elbasan Rashani|11|Clermont|1,588|0.043|
|59|Mohamed Bayo|9|Clermont|2,331|0.042|
|60|Abdu Conté|3|Troyes|695|0.041|
|60|Sanjin Prcic|11|Strasbourg|652|0.041|
|64|<br>Bruno Guimarães|4|Lyon|900|0.040|



> **20 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

**Table 10:** (continued) 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|**GoT** <sup>**(**</sup><sup>**_dir_)**</sup>|
|---|---|---|---|---|---|
|64|Anthony Caci|3|Strasbourg|1,400|0.040|
|64|Kevin Gameiro|9|Strasbourg|1,458|0.040|
|64|Hicham Boudaoui|7|Nice|1,304|0.040|
|64|Gerson|8|Marseille|704|0.040|
|67|Sofiane Diop|11|Monaco|631|0.039|
|68|Igor Silva|2|Lorient|1,197|0.038|
|69|Renato Sanches|8|Lille|951|0.037|
|69|Issa Kaboré|2|Troyes|1,679|0.037|
|71|Mohamed-Ali Cho|10|Angers|807|0.035|
|71|Angelo Fulgini|9|Angers|751|0.035|
|74|Akim Zedadka|2|Clermont|3,330|0.034|
|74|Pol Lirola|2|Marseille|863|0.034|
|74|Adrien Thomasson|7|Strasbourg|1,853|0.034|
|76|Habib Diallo|10|Strasbourg|859|0.033|
|76|Xavier Chavalerin|11|Troyes|949|0.033|
|78|Jean-Ricner Bellegarde|11|Strasbourg|1,454|0.032|
|78|Maxence Caqueret|8|Lyon|1,389|0.032|
|80|Vital N’Simba|3|Clermont|2,731|0.031|
|80|Ruben Aguilar|2|Monaco|1,205|0.031|
|83|Seko Fofana|8|Lens|1,861|0.030|
|83|Ismail Jakobs|3|Monaco|650|0.030|
|83|Terem Moffi|10|Lorient|911|0.030|
|87|Valère Germain|9|Montpellier|1,083|0.029|
|87|Stéphane Bahoken|10|Angers|657|0.029|
|87|Youssouf Fofana|8|Monaco|1,116|0.029|
|87|Mattéo Guendouzi|7|Marseille|1,350|0.029|
|87|Ludovic Ajorque|10|Strasbourg|1,334|0.029|
|90|Ludovic Ajorque|9|Strasbourg|1,243|0.028|
|90|Marco Verratti|4|Paris Saint-Germain|602|0.028|
|93|Baptiste Santamaría|8|Rennes|675|0.027|
|93|Vincent Le Goff|3|Lorient|1,440|0.027|
|93|Ricardo Mangas|3|Bordeaux|613|0.027|
|96|Caio Henrique|3|Monaco|1,454|0.026|
|96|Mihailo Ristic|3|Montpellier|1,150|0.026|
|96|Junior Sambia|2|Montpellier|732|0.026|
|98|Souleyman Doumbia|3|Angers|1,797|0.025|
|98|Przemyslaw Frankowski|3|Lens|1,191|0.025|
|100|Florian Tardieu|8|Troyes|1,530|0.024|



A. Baouan et al.: Crediting football players for creating dangerous actions **— 21** 

**Table 11:** Ranking of Ligue 1 players in terms of GoT<sup>(</sup> 90<sup>_ind_).</sup> 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|GoT <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**|
|---|---|---|---|---|---|
|1|Lionel Messi|10|Paris Saint-Germain|630|14.911|
|2|Ángel Di María|10|Paris Saint-Germain|1,171|13.218|
|3|<br>Neymar|11|Paris Saint-Germain|1,258|12.724|
|4|Marco Verratti|4|Paris Saint-Germain|602|12.581|
|5|Lionel Messi|9|Paris Saint-Germain|675|12.353|
|6|Romain Faivre|7|Brest|630|10.402|
|7|Houssem Aouar|7|Lyon|810|10.077|
|8|Téji Savanier|7|Montpellier|2,209|9.608|
|9|Marco Verratti|8|Paris Saint-Germain|1,069|9.446|
|10|Jason Berthomier|7|Clermont|1,244|9.340|
|11|Benjamin Bourigeaud|10|Rennes|1,719|9.211|
|12|Sofiane Boufal|9|Angers|771|9.100|
|13|Bruno Guimarães|4|Lyon|900|8.817|
|14|Dimitri Payet|9|Marseille|617|8.815|
|15|Moses Simon|11|Nantes|1,222|8.790|
|16|Martin Terrier|11|Rennes|1,386|8.639|
|17|Kylian Mbappé|11|Paris Saint-Germain|1,066|8.577|
|18|Frédéric Guilbert|2|Strasbourg|2,428|8.421|
|19|Ruben Aguilar|2|Monaco|1,205|8.019|
|20|Lovro Majer|7|Rennes|1,302|7.927|
|21|Lucas Da Cunha|10|Clermont|606|7.882|
|22|Kylian Mbappé|9|Paris Saint-Germain|1,338|7.733|
|23|Ghislain Konan|3|Reims|1,007|7.721|
|24|Sanjin Prcic|11|Strasbourg|652|7.624|
|25|Sofiane Boufal|11|Angers|665|7.547|
|26|Lucas Paquetá|7|Lyon|1,248|7.450|
|27|Karl Toko-Ekambi|11|Lyon|1,855|7.365|
|28|Jonathan Ikoné|7|Lille|767|7.285|
|29|Franck Honorat|11|Brest|838|7.207|
|30|Achraf Hakimi|2|Paris Saint-Germain|1,781|7.125|
|31|Idrissa Gueye|8|Paris Saint-Germain|662|7.090|
|32|Dimitri Lienard|3|Strasbourg|1,728|7.050|
|33|Gerson|8|Marseille|704|7.016|
|34|Vanderson|10|Monaco|619|6.939|
|35|Ibrahima Sissoko|7|Strasbourg|826|6.892|
|36|Ludovic Blas|7|Nantes|810|6.816|
|37|Gaël Kakuta|9|Lens|976|6.802|
|38|Jonathan Clauss|2|Lens|1,940|6.757|
|39|Justin Kluivert|11|Nice|1,207|6.700|
|40|Flavien Tait|8|Rennes|1,129|6.671|
|41|Kevin Gameiro|10|Strasbourg|673|6.569|
|42|Florent Mollet|10|Montpellier|1,269|6.465|
|43|Angelo Fulgini|8|Angers|630|6.459|
|44|Renato Sanches|8|Lille|951|6427|
|45|<br>Henrique|3|Lyon|619|.<br>6.385|
|46|Danilo Pereira|4|Paris Saint-Germain|879|6.346|
|47|Pol Lirola|2|Marseille|863|6.327|
|48|Jim Allevinah|11|Clermont|858|6.303|
|49|Youcef Atal|2|Nice|1,032|6.258|
|50|Maxence Caqueret|8|Lyon|1,389|6.229|



> **22 —** A. Baouan et al.: Crediting football players for creating dangerous actions 

**Table 11:** (continued) 

|**Rank**|**Name**|**Position**|**Team**|**Minutes**|GoT <sup>**(** </sup><sup>**_ind_** </sup><sup>**)**</sup><br>**90**|
|---|---|---|---|---|---|
|51|Vital N’Simba|3|Clermont|2,731|6.066|
|52|Anthony Caci|3|Strasbourg|1,400|6.023|
|53|<br>Emerson|3|Lyon|1,848|6.019|
|54|Aleksandr Golovin|11|Monaco|607|5.973|
|55|Birger Meling|3|Rennes|776|5.936|
|56|Juan Bernat|3|Paris Saint-Germain|777|5.929|
|57|Jodel Dossou|10|Clermont|1,762|5.864|
|58|Caio Henrique|3|Monaco|1,454|5.855|
|59|Jonas Martin|4|Rennes|1,115|5.810|
|60|Thomas Foket|2|Reims|631|5.805|
|61|Jonathan Bamba|11|Lille|1,763|5.632|
|62|Marquinhos|5|Paris Saint-Germain|2,340|5.625|
|63|Florian Sotoca|10|Lens|1,119|5.598|
|64|Jordan Ferri|8|Montpellier|2,129|5.516|
|65|Aurélien Tchouaméni|4|Monaco|1,620|5.431|
|66|Malo Gusto|2|Lyon|1,369|5.382|
|67|Cheick Oumar Doucouré|7|Lens|1,350|5.372|
|68|Armand Laurienté|9|Lorient|842|5.345|
|69|Akim Zedadka|2|Clermont|3,330|5.281|
|70|Presnel Kimpembe|6|Paris Saint-Germain|1,840|5.230|
|71|Ismail Jakobs|3|Monaco|650|5.199|
|72|Fábio|3|Nantes|726|5.154|
|73|Thilo Kehrer|2|Paris Saint-Germain|632|5.144|
|74|Cengiz Ünder|10|Marseille|1,047|5.079|
|75|Léo Dubois|2|Lyon|1,246|5.060|
|76|Mattéo Guendouzi|7|Marseille|1,350|4.995|
|77|Facundo Medina|4|Lens|1,329|4.953|
|78|Adrien Thomasson|7|Strasbourg|1,853|4.921|
|79|Nayef Aguerd|6|Rennes|1,698|4.908|
|80|Abdu Conté|3|Troyes|695|4.891|
|81|Javairô Dilrosun|9|Bordeaux|675|4.845|
|82|Hamari Traoré|2|Rennes|1,878|4.836|
|83|Przemyslaw Frankowski|3|Lens|1,191|4.778|
|84|Wissam Ben Yedder|9|Monaco|1,625|4.685|
|85|Vincent Le Goff|3|Lorient|1,440|4.669|
|86|Valentin Rongier|2|Marseille|899|4.668|
|87|Angelo Fulgini|9|Angers|751|4.661|
|88|William Saliba|5|Marseille|1,800|4.652|
|89|Boubacar Kamara|4|Marseille|1,497|4.636|
|90|Nuno Mendes|3|Paris Saint-Germain|1,246|4.599|
|91|Jason Denayer|6|Lyon|630|4.591|
|92|Baptiste Santamaría|8|Rennes|675|4.536|
|93|Jonathan Gradit|6|Lens|1,710|4.535|
|94|YoussoufFofana|8|Monaco|1116|4517|
|95|<br>Florian Tardieu|8|Troyes|,<br>1,530|.<br>4.496|
|96|Jordan Lotomba|2|Nice|1,410|4.454|
|97|Mihailo Ristic|3|Montpellier|1,150|4.439|
|98|Warmed Omari|5|Rennes|1,710|4.407|
|99|MelvinBard|3|Nice|2470|4350|
|100|<br>Seko Fofana|8|Lens|,<br>1,861|.<br>4.345|



A. Baouan et al.: Crediting football players for creating dangerous actions **— 23** 

**Table 12:** The main formation clusters for each team in Ligue 1 in the 2021–2022 season. 

|**Team**|**Formation cluster**|
|---|---|
|Angers|3|
|Bordeaux|3|
|Brest|2|
|Clermont|1|
|Lens|3|
|Lille|2|
|Lorient|3|
|Lyon|1|
|Marseille|1|
|Metz|3|
|Monaco|1|
|Montpellier|1|
|Nantes|1|
|Nice|2|
|Paris Saint-Germain|1|
|Reims|3|
|Rennes|1|
|St Etienne|4|
|Strasbourg|3|
|Troyes|4|



## **References** 

Adamopoulos, L. (1976). Cluster models for earthquakes: regional comparisons. _J. Int. Assoc. Math. Geol._ 8: 463−475,. 

Bonnet, A., Dion-Blanc, C., Gindraud, F., and Lemler, S. (2022a). Neuronal network inference and membrane potential model using multivariate Hawkes processes. _J. Neurosci. Methods_ 372: 109550,. Bonnet, A., Herrera, M. M., and Sangnier, M. (2022b). Inference of multivariate exponential Hawkes processes with inhibition and application to neuronal activity. _arXiv preprint arXiv:2205.04107_ . Brémaud, P. (1981). _Point Processes and Queues: Martingale Dynamics_ , Vol. 50. Springer. Green, S. (2012)., Assessing the performance of Premier League goalscorers. Available at: https://www.statsperform.com/resource/ assessing-the-performance-of-premier-league-goalscorers/. Hawkes, A. G. (1971a). Point spectra of some mutually exciting point processes. _J. Roy. Stat. Soc.: Ser. B (Methodological)_ 33: 438−443,. Hawkes, A. G. (1971b). Spectra of some self-exciting and mutually exciting point processes. _Biometrika_ 58: 83−90,. Hawkes, A. G. and Oakes, D. (1974). A cluster process representation of a self-exciting process. _J. Appl. Probab._ 11: 493−503,. Jaisson, T. and Rosenbaum, M. (2015). Limit theorems for nearly unstable Hawkes processes. _Ann. Appl. Probab._ 25, https://doi.org/10.1214/14aap1005. Lambert, R. C., Tuleau-Malot, C., Bessaih, T., Rivoirard, V., Bouret, Y., Leresche, N., and Reynaud-Bouret, P. (2018). Reconstructing the functional connectivity of multiple spike trains using Hawkes models. _J. Neurosci. Methods_ 297: 9−21,. Ogata, Y. (1981). On lewis’ simulation method for point processes. _IEEE Trans. Inf. Theor._ 27: 23−31,. Ogata, Y. (1988). Statistical models for earthquake occurrences and residual analysis for point processes. _J. Am. Stat. Assoc._ 83: 9−27,. Ogata, Y. (1978). The asymptotic behaviour of maximum likelihood estimators for stationary point processes. _Ann. Inst. Stat. Math._ 30: 243−261,. Singh, K. (2018)., Introducing Expected Threat (xT). Available at: https:// karun.in/blog/expected-threat.html. Whitmore, J. (2021)., What Are Expected Assists (xA)?. Available at: https://theanalyst.com/eu/2021/03/what-are-expected-assists-xa/. 


