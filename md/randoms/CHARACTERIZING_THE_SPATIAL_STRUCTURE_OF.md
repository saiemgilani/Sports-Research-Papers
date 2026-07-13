<!-- source: randoms/CHARACTERIZING_THE_SPATIAL_STRUCTURE_OF.pdf -->

_Submitted to the Annals of Applied Statistics_ arXiv: `stat.ME./0907.0000` 

# **CHARACTERIZING THE SPATIAL STRUCTURE OF DEFENSIVE SKILL IN PROFESSIONAL BASKETBALL** 

By Alexander Franks<sup>_∗_,</sup><sup>_†_</sup> , Andrew Miller<sup>_‡_</sup> , Luke Bornn<sup>_†_</sup> , and Kirk Goldsberry<sup>_§_</sup> 

_Department of Statistics, Harvard University_<sup>_†_</sup> _Department of Computer Science, Harvard University_<sup>_‡_</sup> _Institute of Quantitative Social Science, Harvard University_<sup>_§_</sup> 

Although basketball is a dualistic sport, with all players competing on both offense and defense, almost all of the sport’s conventional metrics are designed to summarize offensive play. As a result, player valuations are largely based on offensive performances and to a much lesser degree on defensive ones. Steals, blocks, and defensive rebounds provide only a limited summary of defensive effectiveness, yet they persist because they summarize salient events that are easy to observe. Due to the inefficacy of traditional defensive statistics, the state of the art in defensive analytics remains qualitative, based on expert intuition and analysis that can be prone to human biases and imprecision. 

Fortunately, emerging optical player tracking systems have the potential to enable a richer quantitative characterization of basketball performance, particularly defensive performance. Unfortunately, due to computational and methodological complexities, that potential remains unmet. This paper attempts to fill this void, combining spatial and spatio-temporal processes, matrix factorization techniques, and hierarchical regression models with player tracking data to advance the state of defensive analytics in the NBA. Our approach detects, characterizes, and quantifies multiple aspects of defensive play in basketball, supporting some common understandings of defensive effectiveness, challenging others, and opening up many new insights into the defensive elements of basketball. 

> _∗_ The authors would like to thank STATS LLC for providing us with the optical tracking data, as well as Ryan Adams, Edo Airoldi, Dan Cervone, Alex D’Amour, Carl Morris, and Natesh Pillai for numerous valuable discussions. 

_Keywords and phrases:_ Basketball, Hidden Markov Models, Nonnegative Matrix Factorization, Bayesian Hierarchical Models 

1 

# CONTENTS 

|1|Intr|oduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>2|
|---|---|---|
||1.1|Method Overview . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
|2|Wh|o’s Guarding Whom . . . . . . . . . . . . . . . . . . . . . . . .<br>4|
||2.1|Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>6|
||2.2|Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|3|Para|meterizing Shot Types<br>. . . . . . . . . . . . . . . . . . . . . .<br>11|
||3.1|Point Process Decomposition<br>. . . . . . . . . . . . . . . . . .<br>11|
||3.2|Fitting the LGCPs . . . . . . . . . . . . . . . . . . . . . . . .<br>13|
||3.3|NMF Optimization . . . . . . . . . . . . . . . . . . . . . . . .<br>14|
||3.4|Basis and Player Summaries . . . . . . . . . . . . . . . . . . .<br>15|
|4|Freq|uency and Efciency: Characteristics of a Shooter . . . . . . .<br>17|
||4.1|Shrinkage and Parameter Regularization . . . . . . . . . . . .<br>17|
||4.2|Shot Frequency . . . . . . . . . . . . . . . . . . . . . . . . . .<br>18|
||4.3|Shot Efciency . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
||4.4|Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>22|
|5|Res|ults<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>23|
|6|Disc|ussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|Su|pple|mentary Material . . . . . . . . . . . . . . . . . . . . . . . . . .<br>29|
|Re|feren|ces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>30|
|Au|thor’|s addresses . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>31|



2 

FRANKS ET AL. 

**1. Introduction.** In contrast to American football, where different sets of players compete on offense and defense, in basketball every player must play both roles. Thus, traditional ‘back of the baseball card’ metrics which focus on offensive play are inadequate for fully characterizing player ability. Specifically, the traditional box score includes points, assists, rebounds, steals and blocks per game, as well as season averages like field goal percentage and free throw percentage. These statistics paint a more complete picture of the _offensive_ production of a player, while steals, blocks, and defensive rebounds provide only a limited summary of _defensive_ effectiveness. These metrics, though they explain only a small fraction of defensive play, persist because they summarize recognizable events that are straightforward to record. 

A deeper understanding of defensive skill requires that we move beyond simple observables. Due to the inefficacy of traditional defensive statistics, modern understanding of defensive skill has centered around expert intuition and analysis that can be prone to human biases and imprecision. In general, there has been little research characterizing individual player habits in dynamic, goal-based sports such as basketball. This is due to 1) the lack of relevant data, 2) the unique spatial-temporal nature of the sport and 3) challenges associated with disentangling confounded player effects. 

One of the most popular metrics for assessing player ability, individual plus/minus, integrates out the details of play, focusing instead on aggregate outcomes. This statistic measures the total team point or goal differential while a player is in the game. As such, it represents a notion of overall skill that incorporates both offensive and defensive ability. The biggest difficulty with individual plus/minus, however, is player confounding. That is, plus/minus depends crucially on the skill of an individual’s teammates. One solution to this problem is to aggregate the data further by recording empirical plus/minus for all pairs or even triplets of players in the game (Kubatko et al., 2007). As an alternative, several approaches control for confounding using regression adjusted methods (Rosenbaum, 2004; Sill, 2010; Macdonald, 2011). 

Only recently have more advanced hierarchical models been used to analyze individual player ability in sports. In hockey, for instance, competing process hazard models have been used to value players, whereby outcomes are goals, with censoring occurring at each player change (Thomas et al., 2013). As with all of the plus/minus approaches discussed earlier, this analysis looked at discrete outcomes, without taking into consideration withinpossession events such as movements, passes, and spatial play formations. Without analyzing the spatial actions occurring within a possession, mea- 

3 

suring individual traits as separate from team characteristics is fraught with identifiability problems. 

There is an emerging solution to these identifiability concerns, however, as player tracking systems become increasingly prevalent in professional sports arenas. While the methodology developed herein applies to basketball on all continents, for this research we use optical player tracking data from the 2013-2014 NBA season. The data, which is derived from cameras mounted in stadium rafters, consist primarily of _x, y_ coordinates for the ball and all ten athletes on the court (five on each team), recorded at 25 frames per second. In addition, the data include game and player specific annotations: who possesses the ball, when fouls occur, and shot outcomes. 

This data enables us for the first time to use spatial and spatio-temporal information to solve some of the challenges associated with individual player analysis. The spatial resolution of these data have changed the types of questions we can answer about the game, allowing for in-depth analyses into individual players (Goldsberry, 2012, 2013). Model-based approaches using this rich data have also recently gained traction, with Cervone et al. (2014) employing multi-scale semi-Markov models to conduct real-time evaluations of basketball plays. 

While it is clear that player tracking systems have the potential to enable a richer quantitative characterization of basketball performance, this potential has not yet been met, particularly for measuring defensive performance. Rather than integrate out the details of play, we exploit the spatio-temporal information in the data to learn the circumstances that lead to a particular outcome. In this way, we infer not just who benefits their team, but _why_ and _how_ they do so. Specifically, we develop a model of the spatial behavior of NBA basketball players which reveals interpretable dimensions of both offensive and defensive efficacy. We suspect the proposed methodology might also find use in other sports. 

1.1. _Method Overview._ We seek to fill a void in basketball analytics by providing the first quantitative characterization of man-to-man defensive effectiveness in different regions of the court. To this end, we propose a model which explains both shot selection (who shoots and where) as well as the expected outcome of the shot, given the defensive assignments. We term these quantities shot _frequency_ and _efficiency_ , respectively; see National Basketball Association (2014) for a glossary of other basketball terms used throughout the paper. Despite the abundance of data, critical information for determining these defensive habits is unavailable. First and most importantly, the defensive matchups are unknown. While it is often clear 

4 

FRANKS ET AL. 

to a human observer who is guarding whom, such information is absent from the data. While in theory we could use crowd-sourcing to learn who is guarding whom annotating the dataset is a subjective and labor intensive task. Secondly, in order to provide meaningful spatial summaries of player ability, we must define relevant court regions in a data driven way. Thus, before we can begin modeling defensive ability, we devise methods to learn these features from the available data. 

Our results reveal other details of play that are not readily apparent. As one example, we demonstrate that two highly regarded defensive centers, Roy Hibbert and Dwight Howard, impact the game in opposing ways. Hibbert reduces shot efficiency near the basket more than any other player in the game, but also faces more shots there than similar players. Howard, on the other hand, is one of the best at reducing shot frequency in this area, but tends to be worse than average at reducing shot efficiency. We synthesize the spatially varying efficiency and frequency results visually in the _defensive_ shot chart, a new analogue to the oft depicted offensive shot chart. 

**2. Who’s Guarding Whom.** For each possession, before modeling defensive skill, we must establish some notion of defensive intent. To this end, we first construct a model to identify which offender is guarded by each defender at every moment in time. To identify who’s guarding whom, we infer the canonical, or central, position for a defender guarding a particular offender at every time _t_ as a function of space-time covariates. A player deviates from this position due to player or team specific tendencies and unmodeled covariates. Throughout each possession, we index each defensive player by _j ∈_ 1 _, . . . ,_ 5 and each offensive player by _k ∈_ 1 _, . . . ,_ 5. Without loss of generality, we transform the space so that all possessions occur in the same half. To start, we model the canonical defensive location for a defender at time _t_ , guarding offender _k_ , as a convex combination of three locations: the position of the offender, _Otk_ , the current location of the ball, _Bt_ , and the location of the hoop, _H_ . Let _µtk_ be the canonical location for a defender guarding player _k_ at time _t_ . Then, 



with Γ = [ _γo, γb, γh_ ]. 

Let _Itjk_ be an indicator for whether defender _j_ is guarding offender _k_ at time _t_ . Multiple defenders can guard the same offender, but each defender 

5 



Fig 1 _. The canonical defending location is a convex combination of the offender, ball and hoop locations._ 

can only be guarding one offender at any instant. The observed location of a defender _j_ , given that they are guarding offender _k_ , is normally distributed about the mean location 



We model the evolution of man-to-man defense (as given by the matrix of matchups, **I** ) over the course of a possession using a hidden Markov model. The hidden states represent the offender that is being guarded by each defensive player. The complete data likelihood is 



where _P_ ( _Dtj|Itjk_ = 1 _,_ Γ _, σD_<sup>2) is a normal density as stated above. We also</sup> assume a constant transition probability, i.e. a defender is equally likely, a priori, to switch to guarding any offender at every instant 



for all defenders, _j_ . Although in reality there should be heterogeneity in _ρ_ across players, for computational simplicity we assume homogeneity and 

6 

FRANKS ET AL. 

later show that we still do a good job recovering switches and who’s guarding whom. The complete log likelihood is 



2.1. _Inference._ We use the EM algorithm to estimate the relevant unknowns, _Itjk, σD_<sup>2, Γ and</sup><sup>_ρ_. At each iteration,</sup><sup>_i_, of the algorithm, we perform</sup> the E-step and M-step until convergence. In the E-step, we compute _Etjk_<sup>(</sup><sup>_i_)=</sup> _E_ [ _Itjk|Dtj,_ Γ<sup>ˆ(</sup><sup>_i_)</sup> _,_ ˆ _σD_<sup>2(</sup><sup>_i_)</sup><sup>_,_ˆ</sup><sup>_ρ_(</sup><sup>_i_)]and</sup><sup>_A_(</sup> _tjkk_<sup>_i_)</sup><sup>_′_=[</sup><sup>_ItjkI_(</sup><sup>_t−_1)</sup><sup>_jk′|Dtj,_ˆΓ(</sup><sup>_i_)</sup><sup>_,_ˆ</sup><sup>_σ_</sup> _D_<sup>2(</sup><sup>_i_)</sup><sup>_,_ˆ</sup><sup>_ρ_(</sup><sup>_i_)]for</sup> all _t_ , _j_ , _k_ and _k_<sup>_′_</sup> . These expectations can be computed using the forwardbackward algorithm (Bishop et al., 2006). Since we assume each defender acts independently, we run the forward-backward algorithm for each _j_ , to compute the expected assignments ( _Etjk_<sup>(</sup><sup>_i_)) and the probabilities for every pair</sup> of two successive defensive assignments ( _A_<sup>(</sup> _tjkk_<sup>_i_)</sup><sup>_′_)foreachdefenderatevery</sup> moment. In the M-step, we update the maximum likelihood estimates of _σD_<sup>2,</sup> Γ, and _ρ_ given the current expectations. 

Let **X** = [ **O** _,_ **B** _,_ **H** ] be the design matrix corresponding to the offensive location, ball location and hoop location. We define _Xtk_ = [ _Otk, Bt, H_ ] to be the row of the design matrix corresponding to offender _k_ at time _t_ . 

In the _i_ th iteration of the M-step we first update our estimates of Γ and _σ_<sup>2</sup> _D_ 



This maximization corresponds to the solution of a constrained generalized least squares problem and can be found analytically. Let Ωbe the diagonal matrix of weights, in this case whose entries at each iteration are _σ_<sup>2ˆΓ is the maximum likelihood estimator subject to the constraint</sup> _D_<sup>_/E_</sup> _tjk_<sup>(</sup><sup>_i_). As</sup> that Γ<sup>ˆ</sup> **1** = 1, it can be shown that 



where, Γ<sup>ˆ</sup> _gls_ = ( _X_<sup>_T_</sup> Ω<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> Ω<sup>_−_1</sup> _D_ is the usual generalized least squares estimator. Finally, the estimated defender variation at iteration _i_ , _σ_ ˆ<sup>2</sup> , is simply: 

7 



Where _E_ = diag( _Etjk_<sup>(</sup><sup>_i−_1)</sup> ) for all _t_ , _j_ , _k_ in iteration _i_ and _NX_ = nrow(X). Next, we update our estimate of the transition parameter, _ρ_ , in iteration _i_ : 



It is easy to show, under the proposed transition model, that the maxi- _<u>ρ</u>_ mum likelihood estimate for the odds of staying in the same state, _Q_ = 1 _−ρ_<sup>,</sup> is 



and hence the maximum likelihood estimate for _ρ_ is 



Using the above equations, we iterate until convergence, saving the final estimates of Γ,<sup>ˆ</sup> _σ_ ˆ _D_<sup>2,and</sup><sup>_ρ_ˆ.</sup> 

2.2. _Results._ First, we restrict our analysis to the parts of a possession in which all players are in the offensive half court – when the ball is moved up the court at the beginning of each possession, most defenders are not yet actively guarding an offender. We use the EM algorithm to fit the HMM on 30 random possessions from the database. We find that a defender’s canonical position can be described as 0 _._ 62 _Otk_ + 0 _._ 11 _Bt_ + 0 _._ 27 _H_ at any moment in time. That is, we infer that on average the defenders position themselves just over two thirds ( 0 _._ 27+00 _<u>.</u>_ <u>62</u> _._ 62<sup>_≈_0</sup><sup>_._70)ofthewaybetweenthe</sup> hoop and the offender they are guarding, shading slightly toward the ball (see Figure 1). Since the weights are defined on a relative, rather than absolute scale, the model accurately reflects the fact that defenders guard players more closely when they are near the basket. Furthermore, the model captures the fact that a defender guards the ball carrier more closely, since the ball and the offender are in roughly the same position. In this case, on average the defender positions himself closer to three fourths (0 _._ 73 _Otk_ + 0 _._ 27 _H_ ) of the way between the ball carrier and the basket. 

8 

FRANKS ET AL. 







Fig 2 _. Who’s guarding whom. Players 0-4 (red circles) are the offenders and players 5-9 (blue triangles) are defenders. Line darkness represents degree of certainty. We illustrate a few properties of the model: (a) Defensive assignments are not just about proximity– given this snapshot, it appears as if 5 should be guarding 1 and 9 should be guarding 4. However, from the full animation, it is clear that 9 is actually chasing 1 across the court. The HMM enforces some smoothness, which ensures that we maintain the correct matchups over time. (b) We capture uncertainty about who is guarding whom, as illustrated by multiple faint lines from defender 5. There is often more uncertainty near the basket. (c) Our model captures double teams (defenders 7 and 9 both guarding 0). Full animations are available in Supplement B (Franks et al., 2015)._ 

As a sensitivity analysis, we fit EM in 100 different games, on different teams, using only 30 possessions for estimating the parameters of the model. The results show that thirty possessions are enough to learn the weights to reasonable precision and that they are stable across games: Γ<sup>ˆ</sup> = (0 _._ 62 _±_ 0 _._ 02 _,_ 0 _._ 11 _±_ 0 _._ 01 _,_ 0 _._ 27 _±_ 0 _._ 02). Values of the transition parameter are more variable but have a smaller impact on inferred defensive matchups: values range from _ρ_ = 0 _._ 96 to _ρ_ = 0 _._ 99. Empirically, the algorithm does a good job of capturing who’s guarding whom. Figure 2 illustrates a few snapshots from the model. While there is often some uncertainty about who’s guarding whom near the basket, the model accurately infers switches and double teams. See Supplement B for animations demonstrating the model performance (Franks et al., 2015). 

This model is clearly interesting in its own right, but most importantly it facilitates a plethora of new analyses which incorporate matchup defense. For instance, the model could be used to improve _counterpart statistics_ , a measure of how well a player’s counterpart performs (Kubatko et al., 2007). Our model circumvents the challenges associated with identifying the most appropriate counterpart for a player, since we directly infer who is guarding whom at every instant of a possession. 

9 

The model can also be used to identify how much defensive attention each offender receives. Table 1 shows the league leaders in attention received, when possessing the ball and when not possessing the ball. We calculate the average attention each player receives as the total amount of time guarded by all defenders divided by the total time playing. This metric reflects the perceived threat of different offenders. The measure also provides a quantitative summary of exactly how much a superstar may free up other shooters on his team, by drawing attention away from them. 

||**On Ball**|||**Of Ball**||
|---|---|---|---|---|---|
|Rank|Player|Attention|Rank|Player|Attention|
|1|DeMar DeRozan|1.213|1|Stephen Curry|1.064|
|2|Kevin Durant|1.209|2|Kevin Durant|1.063|
|3|Rudy Gay|1.201|3|Carmelo Anthony|1.048|
|4|Eric Gordon|1.187|4|Dwight Howard|1.044|
|5|Joe Johnson|1.181|5|Nikola Pekovic|1.036|



Table 1 

_Average attention drawn, on and off ball. Using inference about who’s guarding whom, we calculate the average attention each player receives as the total amount of time guarded by each defender divided by the total time playing (subset by time with and without the ball). At any moment in time, there are five defenders, and hence five units of “attention” to divide amongst the five offenders each possession. On ball, the players receiving the most attention are double teamed an average of 20% of their time possessing the ball. Off ball, the players that command the most attention consist largely of MVP caliber players._ 

Alternatively, we can define some measure of _defensive entropy_ : the uncertainty associated with whom a defender is guarding throughout a possession. This may be a useful notion, since it reflects how active a defender is on the court, in terms of switches and double teams. If each defender guards only a single player throughout the course of a possession, the defensive entropy is zero. If they split their time equally between two offenders, their entropy is one. Within a possession, we define a defender’s entropy as �5 _k_ =1<sup>_Zn_(</sup><sup>_j, k_) log(</sup><sup>_Zn_(</sup><sup>_j, k_)),where</sup><sup>_Zn_(</sup><sup>_j, k_)isthefractionoftimedefender</sup> _j_ spends guarding offender _k_ in possession _n_ . 

By averaging defender entropy over all players on a defense, we get a simple summary of a team’s tendency for defensive switches and double teams. Table 2 shows average team entropies, averaged over all defenders within a defense as well as a separate measure averaging over all defenders faced by an offense (induced entropy). By this measure, the Miami Heat were the most active team defense, and additionally they induce the most defensive entropy as an offense. 

These results illustrate the many types of analyses that can be conducted with this model, but there are still many ways in which the model itself 

10 

FRANKS ET AL. 

|Rank|Team|Entropy|Rank|Team|Induced Entropy|
|---|---|---|---|---|---|
|1|Mia|0.574|1|Mia|0.535|
|2|Phi|0.568|2|Dal|0.526|
|3|Mil|0.543|3|Was|0.526|
|4|Bkn|0.538|4|Chi|0.524|
|5|Tor|0.532|5|LAC|0.522|
|26|Cha|0.433|26|OKC|0.440|
|27|Chi|0.433|27|NY|0.440|
|28|Uta|0.426|28|Min|0.431|
|29|SA|0.398|29|Phi|0.428|
|30|Por|0.395|30|LAL|0.418|



Table 2 

_Team defensive entropy. A player’s defensive entropy for a particular possession is defined as_<sup>�5</sup> _k_ =1<sup>_Zn_(</sup><sup>_j, k_)</sup><sup>_log_(</sup><sup>_Zn_(</sup><sup>_j, k_))</sup><sup>_,whereZn_(</sup><sup>_j, k_)</sup><sup>_isthefractionoftimethedefender_</sup> _j spends guarding offender k during possession n. Team defensive entropy is defined as the average player entropy over all defensive possessions for that team. Induced entropy is the average player entropy over all defenders facing a particular offense._ 

could be extended. By exploiting situational knowledge of basketball, we could develop more complex and precise models for the conditional defender behavior. In our model it is theoretically simple to add additional covariates or latent variables to the model which explain different aspects of team or defender behavior. For instance, we could include a function of defender velocity as an additional independent variable, with some function of offender velocity as a covariate. Other covariates might relate to more specific in game situations or only be available to coaches who know the defensive game plan. Finally, by including additional latent indicators, we could model defender position as a mixture model over possible defensive schemes and simultaneously infer whether a team is playing zone defense or man defense. Since true zone defense is rare in the NBA, this approach may be more appropriate for other leagues. 

We also make simplifying assumptions about homogeneity across players. It is possible to account for heterogeneity across players, groups of players, or teams by allowing the coefficients, Γ, to vary in a hierarchy (see Maruotti and Ryd´en (2008) for a related approach involving unit level random effects in HMM’s). Moreover, the hidden Markov model makes strong assumptions about the amount of time each defender spends guarding a particular offender. For instance, in basketball many defensive switches tend to be very brief in duration, since they consist of quick “help defense” or a short double team, before the defender returns to to guarding their primary matchup. As such, the geometric distribution of state durations associated with the HMM may be too restrictive. Modeling the defense with a hidden _semi-Markov_ model, which allows the transition probabilities to vary as a 

11 

function of the time spent in each state, would be an interesting avenue for future research (Yu, 2010; Limnios and Oprisan, 2001). 

While theoretically straightforward, these extensions require significantly more computational resources. Not only are there more coefficients to estimate, but as a consequence the algorithm must be executed on a much larger set of possessions to get reasonable estimates for these coefficients. Nevertheless, our method, which ignores some of these complexities, passes the “eye test” (Figure 2, Supplement B, (Franks et al., 2015)) and leads to improved predictions about shot outcomes (Table 3). 

In this paper we emphasize the use of matchup defense for inferring individual spatially referenced defender skill. Using information about how long defenders guard offenders and who they are guarding at the moment of the shot, we can estimate how defenders affect both shot selection and shot efficiency in different parts of the court. Still, given the high resolution of the spatial data and relatively low sample size per player, inference is challenging. As such, before proceeding we find an interpretable, data driven, low-dimensional spatial representation of the court on which to estimate these defender 

**3. Parameterizing Shot Types.** In order to concisely represent players’ spatial offensive and defensive ability, we develop a method to find a succinct representation of the court by using the locations of attempted shots. Shot selection in professional basketball is highly structured. We leverage this structure by finding a low dimensional decomposition of the court whose components intuitively corresponds to _shot type_ . A _shot type_ is a cluster of ‘similar’ shots characterized by a spatially smooth intensity surface over the court. This surface indicates where shots from that cluster tend to come from (and where they do not come from). Each player’s shooting habits are then represented by a positive linear combination of the global shot types. 

Defining a set of global shot types shared among players is beneficial for multiple reasons. Firstly, it allows us to concisely parameterize spatial phenomena with respect to shot type (for instance, the ability of a defensive player to contest a corner three point shot). Secondly, it provides a low dimensional representation of player habits that can be used to specify a prior on both offensive and defensive parameters for possession outcomes. The graphical and numerical results of this model can be found in Section 3.4. 

3.1. _Point Process Decomposition._ Our goal is to simultaneously identify a small set of _B_ global _shot types_ and each player’s loadings onto these shot types. We accomplish this with a two-step procedure. First, we find a non- 

12 

FRANKS ET AL. 

parametric estimate of each player’s smooth intensity surface, modeled as a log Gaussian Cox process (LGCP) (Møller, Syversveen and Waagepetersen, 1998). Second, we find an optimal low rank representation of all players’ intensity surfaces using non-negative matrix factorization (NMF) (Lee and Seung, 1999). The LGCP incorporates individual spatial information about shots while NMF pools together global information across players. This pooling smooths each player’s estimated intensity surface and yields more robust generalization. For instance, for _B_ = 6, the average predictive ability across players of LGCP+NMF outperforms the predictive ability of independent LGCP surfaces on out of sample data. Intuitively, the global bases define long range correlations that are difficult to capture with a stationary covariance function. 

We model a player’s shot attempts as a point process on the offensive half court, a 47 ft by 50 ft rectangle. Again, shooters will be indexed by _k ∈{_ 1 _, . . . , K}_ , and the set of each player’s shot attempts will be referred to as **x** _k_ = _{xk,_ 1 _, . . . , xk,Nk }_ , where _Nk_ is the number of shots taken by player _k_ , and _xk,m ∈_ [0 _,_ 47] _×_ [0 _,_ 50]. 

Though we have formulated a continuous model for conceptual simplicity, we discretize the court into _V_ one-square-foot tiles for computational tractability of LGCP inference. We expect this tile size to capture all interesting spatial variation. Furthermore, the discretization maps each player into R<sup>_V_whichisnecessaryfortheNMFdimensionalityreduction.</sup> +<sup>,</sup> 

Given point process realizations for each of _K_ players, **x** 1 _, . . . ,_ **x** _K_ , our procedure is 

1. Construct the count matrix **X** _kv_ = number of shots by player _k_ in tile _v_ on a discretized court. 

2. Fit an intensity surface _λk_ = ( _λk_ 1 _, . . . , λkV_ )<sup>_T_</sup> for each player _k_ over the discretized court (LGCP) (Figure 3(b)). 

3. Construct the data matrix **Λ** = ( _λ_<sup>¯</sup> 1 _, . . . , λ_<sup>¯</sup> _K_ )<sup>_T_</sup> , where _λ_<sup>¯</sup> _k_ has been normalized to have unit volume. 

4. Find low-rank matrices **L** _,_ **W** such that **WL** _≈_ **Λ** , constraining all matrices to be non-negative (NMF) (Figure 3(c)). 

This procedure yields a spatial basis **L** and basis loadings, **w** ˆ _k_ , for each individual player. 

One useful property of the Poisson process is the superposition theorem (e.g., Kingman, 1992), which states that given a countable collection of independent Poisson processes **x** 1 _,_ **x** 2 _, . . ._ , each with intensity _λ_ 1 _, λ_ 2 _, . . ._ , their 

13 













Fig 3 _. NBA player shooting representations, from left to right: original point process data from two players, LGCP surface, and NMF reconstructed surfaces (B_ = 6 _). Made and missed shots are represented as blue circles and red ×’s, respectively._ 

superposition, defined as the union of all observations, is distributed as 



Consequently, with the non-negativity of the basis and loadings from the NMF procedure, the basis vectors can be interpreted as sub-intensity functions, or ‘shot types’, which are archetypal intensities used by each player. The linear weights for each player concisely summarize the spatial shooting habits of a player into a vector in R<sup>_B_</sup> +<sup>.</sup> 

3.2. _Fitting the LGCPs._ For each player’s set of points, **x** _k_ , the likelihood of the point process is discretely approximated as 



14 

FRANKS ET AL. 

where, overloading notation, _λk_ ( _·_ ) is the exact intensity function, _λk_ is the discretized intensity function (vector), ∆ _A_ is the area of each tile (implicitly one from now on), and _ppois_ ( _·|λ_ ) is the Poisson probability mass function with mean _λ_ . This approximation comes from the completely spatially random property of the Poisson process, which renders disjoint subsets of space independent. Formally, for two disjoint subsets _A, B ⊂X_ , after conditioning on the intensity the number of points that land in each set, _NA_ and _NB_ , are independent. Under the discretized approximation, the probability of the number of shots in each tile is Poisson, with uniform intensity _λkv_ . 

Explicitly representing the Gaussian random field **z** _k_ , the posterior is 



where the prior over **z** _k_ is a mean zero normal with covariance 



and _z_ 0 is an intercept term that parameterizes the mean rate of the Poisson process. This kernel is chosen to encode prior belief in the spatial smoothness of player habits. Furthermore, we place a gamma prior over the length scale, _νk_ , for each individual player. This gamma prior places mass dispersed around 8 feet, indicating the reasonable a priori belief that shooting variation is locally smooth on that scale. Note that _νk_ = ( _νk_ 1 _, νk_ 2), corresponding to the two dimensions of the court. We obtain posterior samples of _λk_ and _νk_ by iteratively sampling _λk|_ **x** _k, νk_ and _νk|λk,_ **x** _k_ . 

We use Metropolis-Hastings to generate samples of _νk|λk,_ **x** _k_ . Details of the sampler are included in Supplement A (Franks et al., 2015). 

3.3. _NMF Optimization._ Identifying non-negative linear combinations of global shot types can be directly mapped to non-negative matrix factorization. NMF assumes that some matrix **Λ** , in our case the matrix of playerspecific intensity functions, can be approximated by the product of two low rank matrices 



where **Λ** _∈_ R<sup>_N_</sup> +<sup>_×V_</sup> , **W** _∈_ R<sup>_N_</sup> +<sup>_×B_</sup> , and **L** _∈_ R<sup>_B×_</sup> +<sup>_V_</sup> , and we assume _B ≪ V_ . The optimal matrices **W**<sup>_∗_</sup> and **L**<sup>_∗_</sup> are determined by an optimization procedure 

15 

that minimizes _ℓ_ ( _·, ·_ ), a measure of reconstruction error or divergence between **WL** and **Λ** with the constraint that all elements remain non-negative 



Different choices of _ℓ_ will result in different matrix factorizations. A natural choice is the matrix divergence metric 



which corresponds to the Kullback-Leibler (KL) divergence if **A** and **B** are discrete distributions, i.e.,<sup>�</sup> _ij_<sup>_Aij_=�</sup> _ij_<sup>_Bij_=1(LeeandSeung,2001).</sup> Although there are several other possible divergence metrics (i.e. Frobenius), we use this KL-based divergence measure for reasons outlined in Miller et al. (2014). We solve the optimization problem using techniques from Lee and Seung (2001) and Brunet et al. (2004). 

Due to the positivity constraint, the basis **L**<sup>_∗_</sup> tends to be disjoint, exhibiting a more ‘parts-based’ decomposition than other, less constrained matrix factorization methods, such as PCA. This is due to the restrictive property of the NMF decomposition that disallows negative bases to cancel out positive bases. In practice, this restriction eliminates a large swath of ‘optimal’ factorizations with negative basis/weight pairs, leaving a sparser and often more interpretable basis (Lee and Seung, 1999). 

3.4. _Basis and Player Summaries._ We graphically depict the shot type preprocessing procedure in Figure 3. A player’s spatial shooting habits are reduced from a raw point process to an independent intensity surface, and finally to a linear combination of _B_ nonnegative basis surfaces. There is wide variation in shot selection among NBA players - some shooters specialize in certain types of shots, whereas others will shoot from many locations on the court. 

We set _B_ = 6 and use the KL-based loss function, choices which exhibit sufficient predictive ability in Miller et al. (2014), and yield an interpretable basis. We graphically depict the resulting basis vectors in Figure 4. This procedure identifies basis vectors that correspond to spatially interpretable shot types. Similar to the parts-based decomposition of human faces that NMF yields in Lee and Seung (1999), LGCP-NMF yields a shots-based decomposition of NBA players. For instance, it is clear from inspection that one basis corresponds to shots in the restricted area, while another corresponds to shots from the rest of the paint. The three point line is also split into 

16 

FRANKS ET AL. 













Fig 4 _. Basis vectors (surfaces) identified by LGCP-NMF for B_ = 6 _. Each basis surface is the normalized intensity function of a particular shot type, and players’ shooting habits are a weighted combination of these shot types. Conditioned on a certain shot type (e.g. corner three), the intensity function acts as a density over shot locations, where red indicates likely locations._ 

corner three point shots and center three point shots. Unlike PCA, NMF is not mean-centered, and as such a residual basis appears regardless of _B_ ; this basis in effect captures positive intensities outside of the support of the relevant bases. In all analyses herein, we discard the residual basis and work solely with the remaining bases. 

The LGCP-NMF decomposition also yields player specific shot weights that provide a concise characterization of their offensive habits. The weight _wkb_ can be interpreted as the amount player _k_ takes shot type _b_ , which quantifies intuitions about player behavior. These weights will be incorporated into an informative prior over offensive skill parameters in the possession outcome model. We highlight individual player breakdowns in Supplement A (Franks et al., 2015). While these weights summarize offensive _habits_ , our aim is to develop a model to jointly measure both offensive and defensive _ability_ in different parts of the court. Using who’s guarding whom and this data driven court discretization, we proceed by developing a model to quan- 

17 

tify the effect that defenders have on both shot selection (frequency) and shot efficiency. 

**4. Frequency and Efficiency: Characteristics of a Shooter.** We proceed by decomposing a player’s habits in terms of shot frequency and efficiency. First, we construct a model for where on the court different offenders prefer to shoot. This notion is often portrayed graphically as the _shot chart_ and reflects a player’s spatial shot _frequency_ . Second, conditioned on a player taking a shot, we want to know the probability that the player actually makes the shot: the spatial player _efficiency_ . Together, player spatial shot _frequency_ and _efficiency_ largely characterize a basketball player’s habits and ability. 

While it is not difficult to empirically characterize frequency and efficiency of shooters, it is much harder to say something about how defenders affect these two characteristics. Given knowledge of matchup defense, however, we can create a more sophisticated joint model which incorporates how defenders affect shooter characteristics. Using the results on who’s guarding whom, we are able to provide estimates of defensive impact on shot frequency and efficiency, and ultimately a defensive analogue to the offensive shot chart (Figure 3(a)). 

4.1. _Shrinkage and Parameter Regularization._ Parameter regularization is a very important part of our model because many players are only observed in a handful of plays. We shrink estimates by exploiting the notion that players with similar roles should be more similar in their capabilities. However, because offense and defense are inherently different, we must characterize player similarity separately for offense and defense. 

First, we gauge how much variability there is between defender types. One measure of defender characteristics is the fraction of time, on average, that each defender spends guarding a shooter in each of the _B_ bases. Figure 5 suggests that defenders can be grouped into roughly three defender types. The groupings are inferred using three cluster K-means on the first two principal component vectors of the “time spent” matrix. Empirically, group 1 corresponds to small point guards, group 2 to forwards and guards, and group 3 to centers. We use these three groups to define the shrinkage points for defender effects in both the shot selection and shot efficiency models. 

When we repeat the same process for offense, it is clear that the players do not cluster; specifically, there appears to be far more variability in offender types than defender types. Thus, to characterize offender similarity, we instead use the normalized player weights from the non-negative matrix factorization, **W** , introduced in Section 3 and described further in Supple- 

18 

FRANKS ET AL. 



<!-- Start of picture text -->
Group 2<br>Carmelo Anthony<br>Group 3 LeBron James<br>Roy Hibbert Kawhi Leonard<br>Tim Duncan<br>Dwight Howard<br>Steve Nash<br>Group 1<br>Chris Paul<br><!-- End of picture text -->

Fig 5 _. Defensive Clusters. We ran SVD on the N × B matrix of time spent in each basis. The x and y axis correspond to principal components one and two of this matrix. The first two principal components suggest that three clusters reasonably separate player groups. Group 1 (green) roughly corresponds to small point guards, group 2 (red) to forwards and guards, and group 3 (blue) to centers._ 

ment A (Franks et al., 2015). Figure 6 shows the loadings on the first two principal components of the player weights. The points are colored by the player’s listed position (e.g. guard, center, forward, etc). While players tend to be more similar to players with the same listed position, on the whole, position is not a good predictor of an offender’s shooting characteristics. 

Consequently, for the prior distribution on offender efficiency we use a normal conditional autoregressive (CAR) model (Cressie, 1993). For every player, we identify the 10 nearest neighbors in the space of shot selection weights. We then connect two players if, for either player in the pair, their partner is one of their ten closest neighbors. We use this network to define a Gaussian Markov random field prior on offender efficiency effects (Section 4.3). 

4.2. _Shot Frequency._ We model shot selection (both shooter and location) using a multinomial distribution with a logit link function. First, we discretize the court into _B_ regions using the pre-processed NMF basis vectors (see Section 3) and define the multinomial outcomes as one of the 5 _×B_ shooter/basis pairs. The court regions from the NMF are naturally disjoint (or nearly so). In this paper, we use the first five bases given in Figure 4. 

19 



<!-- Start of picture text -->
Center Shooting Guard<br>Forward−Center Guard<br>Forward Point Guard<br>Guard−Forward Small Forward<br>Power Forward DeAndre Jordan<br>Dwight Howard<br>Danny Green<br>Steve Novak<br>Kawhi Leonard<br>LeBron James Tyson Chandler<br>Jose Calderon<br>Kevin Love<br>Victor Oladipo Tony Parker<br>Tim Duncan<br>Carmelo Anthony<br>Chris Paul<br><!-- End of picture text -->

Fig 6 _. Offender similarity network. We ran SVD on the N ×B matrix of NMF coefficients (Section 3). The x and y axis correspond to principal components one and two of this matrix. The projection into the first two principal components shows that there is no obvious clustering of offensive player types, as was the case with defense. Moreover “player position” is not a good indicator of shot selection._ 

Shot selection is a function of the offensive players on the court, the fraction of possession time that they are guarded by different defenders, and defenders’ skills. Letting _Sn_ be a categorical random variable indicating the shooter and shot location in possession _n_ , 



Here, _αkb_ is the propensity for an offensive player, _k_ , to take a shot from basis _b_ . However, in any given possession, a players’ propensity to shoot is affected by the defense. _βjb_ represents how well a defender, _j_ , suppresses shots in a given basis _b_ , relative to the average defender in that basis. These values are modulated by entries in a possession specific covariate matrix _Zn_ . The value _Zn_ ( _j, k_ ) is the fraction of time defender _j_ is guarding offensive player _k_ in possession _n_ , with<sup>�5</sup> _k_ =1<sup>_Zn_(</sup><sup>_j, k_) = 1.Weinfer</sup><sup>_Zn_(</sup><sup>_j, k_)foreach</sup> possession using the defender model outlined in Section 2. Note that the 

20 

FRANKS ET AL. 



Fig 7 _. Shot efficiency vs. distance. We plot empirical shot efficiency as a function of the guarding defender’s distance, by region. We compute the empirical log-odds of a shot by binning all shots from each region into 5 bins. Within region, between 0 and 6ft the log-odds of a made shot appears to be nearly linear in distance. After about 6ft (depending on the basis), increased defender distance does not continue to increase the odds of a made shot._ 

baseline outcome is “no shot”, indicating there was a turnover before a shot was attempted. 

We assume normal random effects for both the offensive and defensive player parameters: 



Here, _µαb_ and _µβGb_ represent the player average effect in basis _b_ on offense and defense respectively. For defenders, _G_ indexes one of the 3 defender types (Figure 5), so that there are in fact 3 _B_ group means. Finally, we specify that 



4.3. _Shot Efficiency._ Given a shot, we model efficiency (the probability that the shot is made) as a function of the offensive player’s skill, the defender at the time of the shot, the distance of that defender to the shooter, and where the shot was taken. For a possession _n_ , 

21 



Here, _Yn_ is an indicator for whether the attempted shot for possession _n_ was made and _Dn_ is the distance in feet between the shooter and defender at the moment of the shot, capped at some inferred maximum distance. The parameter _θkb_ describes the shooting skill of a player, _k_ , from basis _b_ . The two terms, _φjb_ and _ξbDn_ are meant to represent orthogonal components of defender skill. _φjb_ encompasses how well the defender contests a shot regardless of distance, _ξbDn_ is independent of the defender identity and adjusts for how far the defender is from the shot. Within a region, as the defender gets further from the shooter, their effect on the outcome of the shot decreases at the same rate, _ξb_ ; as the most likely defender approaches the exact location of the shooter, the defensive effect on the log-odds of a made shot converges toward _φjb_ . Figure 7 supports this modeling choice: empirically, the log-odds of a shot increase roughly linearly in distance up until a point (around 5 or 6 feet depending on the region) at which distance no longer has an effect. 

We again employ hierarchical priors to pool information across players. On defense we specify that: 



Here, _µφGb_ represents the player average effect in basis _b_ on defense. Again, _G_ indexes one of 3 defender types, so that there are in fact 3 _B_ group means. 

On offense, we use the network defined in Section 4.1 (Figure 6) to specify a CAR prior. We define each player’s efficiency to be, a priori, normally distributed with mean proportional to the mean of his neighbors’ efficiencies. This operationalizes the notion that players who have more similar shooting habits should have more similar shot efficiencies. Explicitly, the efficiency, _θ_ , of an offender, _k_ in a region _b_ with mean player efficiency _µθb_ has the prior distribution 



where _N_ ( _k_ ) are the set of neighbors for offender _k_ and _ζ ∈_ [0 _,_ 1) is a discount factor. These conditionals imply the joint distribution 



22 

FRANKS ET AL. 

where D is the diagonal matrix with entries _σ_<sup><u>1</u></sup> _k_<sup>2and</sup><sup>_M_is the matrix such that</sup> _M ′_ = <u>1</u><sup>offenders</sup><sup>_k_and</sup><sup>_k′_areneighborsandzerootherwise.This</sup> _k,k |N_ ( _k_ ) _|_<sup>if</sup> joint distribution is proper as long as ( _I − ζM_ )<sup>_−_1</sup> _D_ is symmetric positivedefinite. The matrix is symmetric when _σk_<sup>2</sup><sup>_∝_</sup> _N_ <u>1(</u> _k_ )<sup>.Wechose</sup><sup>_ζ_=0</sup><sup>_._9to</sup> guarantee the matrix is positive-definite (Cressie, 1993). The number of neighbors (Figure 6) determines the shrinkage point for each player and _ζ_ control how much shrinkage we do. We chose the number of neighbors to be relatively small and hence the _ζ_ to be relatively large, since the players in a neighborhood should be quite similar in their habits. 

Again we use normal priors for the group means: 



Finally, for the distance effect, we specify that 



where _N_<sup>+</sup> indicates a half-normal distribution. We chose a prior distribution with positive support, since increased defender distance should logically increase the offenders efficiency. 

4.4. _Inference._ We use Bayesian inference to infer parameters of both the shot frequency and shot efficiency models. First, we consider different methods of inference in the shot frequency model. The sample size, number of categories, and number of parameters in the model for shot selection are all quite large, making full Bayesian inference challenging. Specifically, there are 5 _× B_ + 1 = 26 outcomes (one for each shooter-basis pair plus one for turnovers) and nearly 150,000 observations. To facilitate computation, we use a local variational inference strategy to approximate the true posterior of parameters from the multinomial logistic regression. The idea behind the variational strategy is to find a lower bound to the multinomial likelihood with a function that looks Gaussian. For notational simplicity let **_η_** _n_ be the vector with elements _ηnk_ = _αkb_ +<sup>�5</sup> _j_ =1<sup>_Zn_(</sup><sup>_j, k_)</sup><sup>_βjb_.Then,thelowerbound</sup> takes the form 



where **bn** and _cn_ are variational parameters and **A** is a simple bound on the Hessian of the log-sum-exp function (B¨ohning, 1992). This implies a Gaussianized approximation to the observation model. Since we use normal priors on the parameters, this yields a normal approximation to the posterior. By iteratively updating the variational parameters, we maximize the 

23 

lower bound on the likelihood. This yields the best normal approximation to the posterior in terms of KL-divergence (see Murphy (2012) for details). 

In the variational inference, we fix the prior parameters as follows: _σα_<sup>2= 1,</sup> _σβ_<sup>2= 0</sup><sup>_._01,</sup><sup>_τ_2</sup> _α_<sup>= 1,and</sup><sup>_τ_2</sup> _β_<sup>= 0</sup><sup>_._01.Thatis,wespecifymorepriorvariability</sup> in the offensive effects than the defensive effects at both the group and individual level. We use cross-validation to select these prior parameters, and then demonstrate that despite using approximate inference, the model performs well in out of sample prediction (Section 5). Since the variational method is only approximate, we start with some exploratory analysis to tune the shrinkage hyperparameters. We examine five scales for both the offense and defense group level prior variance to find the shrinkage factors that yield the highest predictive power. Because the random effects are normal and additive, we constrain _σβ_<sup>2</sup><sup>_<σ_</sup> _α_<sup>2foridentifiability.Wethenfixthesum</sup> _σtotal_ = _σα_<sup>2+</sup><sup>_σ_</sup> _β_<sup>2, and search over values such that</sup><sup>_σ_</sup> _β_<sup>2</sup><sup>_< σ_</sup> _α_<sup>2. We also examine</sup> different scales of _σtotal_ . This search at multiple values of _σtotal_ yields the _σ_<sup>2</sup> optimal ratio _σαβ_<sup>2tobebetween0</sup><sup>_._1and0</sup><sup>_._2.</sup> 

For the efficiency model, we found Bayesian logistic regression to be more tractable: in this regression, there are only two outcomes (make or miss) and approximately 115,000 possessions which lead to a shot. Thus, we proceed with a fully Bayesian regression on shot efficiency, using the variational inference algorithm to initialization the sampler. Inference in the Bayesian regression for shot efficiency was done using hybrid Monte Carlo (HMC) sampling. We implemented the sampler using the probabilistic programming language STAN (Stan Development Team, 2014). We use 2000 samples, and ensure that the _R_<sup>ˆ</sup> statistic is close to 1 for all parameters (Gelman and Rubin, 1992). 

**5. Results.** We fit our model on data from the 2013-2014 NBA regular season, focusing on a specific subset of play: possessions lasting at least 5 seconds, in which all players are in the half-court. We also ignore any activity after the first shot and exclude all plays including fouls or stoppages for simplicity. 

First, we assess the predictive performance of our model relative to simpler models. For both the frequency and efficiency models, we run 10-fold cross validation and compare four models of varying complexity: (i) the full offense/defense model with defender types and CAR shrinkage, (ii) the full offense/defense model without defender types or CAR shrinkage, (iii) a model that ignores defense completely, (iv) a model that ignores defense and space. The frequency models (i-iii) all include 5 ‘shot-types’, and each possession results in one of 26 outcomes. Frequency model (iv) has only 6 

24 FRANKS ET AL. 

||Full Model|No Shrinkage|No Defense|No Spatial|
|---|---|---|---|---|
|Shooter log-likelihood|**-25474.93**|-25571.41|-25725.17|-26342.83|
|Basis log-likelihood|**-25682.16**|-25740.27|-25809.14|N/A|
|Full log-likelihood|**-41461.74**|-41646.81|-41904.48|N/A|
|Efciency log-likelihood|**-3202.09**<br>Ta|-3221.44<br>ble 3|-3239.12|-3270.99|



_Out of sample log-likelihoods for models of increasing complexity. The first row corresponds to the average out of sample likelihood for predicting only the shooter. The second row similarly summarizes out of sample likelihood for predicting only which basis the shot comes from (not the shooter). The third row is the average out of sample log likelihood over the product space of shooter and shot location. We demonstrate that not only does our model outperform simpler models in predicting possession outcomes, but that we outperform them in both shooter and basis prediction tasks individually. In the fourth row, we display the out of sample likelihoods for shot efficiency (whether the shooter makes the basket). The four different models from left to right are (i) the full offensive and defensive model with parameter shrinkage (incorporating inferred defender type and offender similarity), (ii) the offensive and defensive model with a common shrinkage point for all players, (iii) the offense only model, (iv) the offense only model with no spatial component. Incorporating defensive information, spatial information, and player type clearly yields the best predictive models. All quantities were computed using 10-fold cross validation._ 

outcomes - who shot the ball (or no shot). The outcomes of the efficiency model are always binary (corresponding to made or missed shots). 

Table 3 demonstrates that we outperform simpler models in predicting out of sample shooter-basis outcomes. Moreover, while we do well in joint prediction, we also outperform simpler models for predicting both shooter and shot basis separately. Finally, we show that the full efficiency model also improves upon simpler models. Consequently, by incorporating spatial variation and defensive information we have created a model that paints a more detailed and accurate picture of the game of basketball. 

As our main results we focus on parameters related to defensive shot selection and shot efficiency effects. Here we focus on defensive results as the novel contribution of this work, although offender-specific parameters can be found in Supplement A (Franks et al., 2015). A sample of the defensive logistic regression log-odds for basis one (restricted area) and five (center threes) are given in Tables 4 and 5 respectively. For shot selection, we report the defender effects, _βjb_ , which corresponds to the change in log-odds of a shot occurring in a particular region, _b_ , if defender _j_ guards the offender for the entire possession. Smaller values correspond to a reduction in the shooter’s shot frequency in that region. 

For shot efficiency we report _φj_ + _ξbDjb_<sup>_∗_where</sup><sup>_D_</sup> _jb_<sup>_∗_is player</sup><sup>_j_’s difference in</sup> median distance (relative to the average defender) to the offender in region 

25 

**Basis 1 - Efficiency** 

|Group 1||Group 2||Group 3||
|---|---|---|---|---|---|
|Player|_φ_+ _ξD_<sup>_∗_</sup>|Player|_φ_+ _ξD_<sup>_∗_</sup>|Player|_φ_+ _ξD_<sup>_∗_</sup>|
|J. Smith|-0.116|Kidd-Gilchrist|-0.068|R. Hibbert|-0.618|
|J. Lin|-0.029|K. Singler|0.016|E. Brand|-0.484|
|K. Thompson|-0.011|T. Evans|0.017|R. Lopez|-0.462|
|P. Pierce|0.024|Antetokounmpo|0.035|A. Horford|-0.461|
|E. Bledsoe|0.034|A. Tolliver|0.040|K. Koufos|-0.450|
|_Average_|0.191|_Average_|0.142|_Average_|-0.170|
|B. Jennings|0.358|J. Meeks|0.327|C. Boozer|-0.017|
|R. Rubio|0.406|J. Salmons|0.334|J. Adrien|0.006|
|J. Wall|0.414|C. Parsons|0.344|D. Cunningham|0.045|
|B. Knight|0.452|J. Harden|0.375|O. Casspi|0.102|
|J. Teague|0.512|E. Gordon|0.524|T. Young|0.126|



**Basis 1 - Frequency** 

|Group 1||Group 2||Group 3||
|---|---|---|---|---|---|
|Player|_β_|Player|_β_|Player|_β_|
|C. Paul|-0.422|L. Deng|-0.481|L. Aldridge|-0.050|
|G. Hill|-0.375|L. Stephenson|-0.464|C. Boozer|-0.039|
|I. Thomas|-0.367|A. Afalo|-0.450|N. Pekovic|-0.027|
|C. Anthony|-0.344|L. James|-0.449|T. Thompson|-0.026|
|K. Hinrich|-0.334|H. Barnes|-0.432|D. Lee|0.005|
|_Average_|-0.255|_Average_|-0.333|_Average_|0.157|
|S. Marion|-0.144|J. Dudley|-0.226|A. Drummond|0.313|
|G. Dragic|-0.136|P. George|-0.213|S. Hawes|0.327|
|D. Lillard|-0.134|A. Aminu|-0.191|J. Henson|0.338|
|J. Smith|-0.133|T. Ross|-0.186|E. Kanter|0.376|
|B. Jennings|-0.132|J. Meeks<br>Table4|-0.148|R. Lopez|0.470|



_Basis 1. Shot efficiency (top table) and frequency (bottom table). We list the top and bottom five defenders in terms of the effect on the log-odds on a shooters’ shot efficiency in the restricted area (basis 1). Negative effects imply that the defender_ decreases _the log-odds of an outcome, relative to the global average player (zero effect). The three columns consist of defenders in the three groups listed in Figure 5 and the respective group means. Roy Hibbert, considered one of the best defenders near the basket, reduces shot efficiency there more than any other player. Chris Paul, a league leader in steals, reduces opponents’ shot frequency more than any other player of his type._ 

_b_ . A defender’s overall effect on the outcome of a shot depends on how close he tends to be to the shooter at the moment the shot is taken, as well as the players’ specific defensive skill parameter _φj_ . Again, smaller values correspond to a reduction in the shooter’s shot efficiency, with negative values implying a defender that is better than the global average. 

First, as a key point, we illustrate that defenders can affect shot frequency 

26 

FRANKS ET AL. 

**Basis 5 - Efficiency** 

|Group 1||Group|2|Group|3|
|---|---|---|---|---|---|
|Player|_φ_+ _ξD_<sup>_∗_</sup>|Player|_φ_+ _ξD_<sup>_∗_</sup>|Player|_φ_+ _ξD_<sup>_∗_</sup>|
|D. Collison|-0.183|C. Lee|-0.165|B. Bass|-0.075|
|S. Curry|-0.170|D. Wade|-0.142|D. Green|-0.060|
|N. Cole|-0.165|D. DeRozan|-0.137|D. West|-0.032|
|A. Bradley|-0.164|J. Crawford|-0.117|T. Jones|-0.016|
|P. Mills|-0.149|L. Stephenson|-0.114|B. Grifn|0.012|
|_Average_|-0.055|_Average_|-0.030|_Average_|0.073|
|J. Holiday|0.014|J. Green|0.053|P. Millsap|0.088|
|J. Jack|0.020|C. Parsons|0.055|T. Gibson|0.105|
|D. Williams|0.027|M. Harkless|0.060|T. Thompson|0.114|
|J. Smith|0.042|J. Smith|0.063|A. Davis|0.148|
|M. Dellavedova|0.062|G. Hayward|0.072|L. Aldridge|0.188|



**Basis 5 - Frequency** 

||Group 1||Group 2||Group|3|
|---|---|---|---|---|---|---|
|Pla|yer|_β_|Player|_β_|Player|_β_|
|G.|Dragic|-1.286|R. Foye|-1.325|B. Bass|-1.378|
|D.|Lillard|-1.251|C. Parsons|-1.306|C. Frye|-1.357|
|T.|Burke|-1.183|J. Anderson|-1.298|S. Ibaka|-1.321|
|W.|Johnson|-1.163|H. Barnes|-1.296|C. Bosh|-1.312|
|G.|Hill|-1.121|K. Korver|-1.282|B. Grifn|-1.308|
|_Ave_|_rage_|-1.031|_Average_|-1.184|_Average_|-1.325|
|S.|Livingston|-0.911|R. Allen|-1.097|P. Millsap|-1.212|
|M.|Dellavedova|-0.903|T. Hardaway Jr.|-1.079|T. Thompson|-1.190|
|K.|Walker|-0.894|M. Barnes|-1.073|Z. Randolph|-1.186|
|D.|Williams|-0.857|I. Shumpert|-1.049|T. Gibson|-1.159|
|J. J|ack|-0.819|D. Waiters<br>Table 5|-1.036|T. Harris|-1.132|



_Basis 5. Shot efficiency (top table) and frequency (bottom table). We list the top and bottom five defenders in terms of the effect on the log-odds on a shooters’ shot efficiency from center three (basis 5). Negative effects imply that the defender_ decreases _the log-odds of an outcome, relative to the global average player (zero effect). The three columns consist of defenders in the three groups listed in Figure 5 and the respective group means. Kawhi Leonard, a highly regarded perimeter defender, ranks number one in defensive impact on both shot frequency. Hibbert, who is the best defender near the basket (Table 4), is the worst at defending on the perimeter. His opponents have higher log-odds of making a three point shot against him, likely because he is late getting out to the perimeter to contest shots._ 

(where an offender shoots) and shot efficiency (whether the basket is made) and that, crucially, these represent distinct characteristics of a defender. This is well illustrated via two well regarded defensive centers, Dwight Howard and Roy Hibbert. includes effects for defenders in the restricted area (basis 1). Roy Hibbert ranks first (Table 4) and fourth out of 167 defenders in 

27 

his effect on shot efficiency in the paint (bases 1 and 2). Dwight Howard, is ranked 50 and 117 respectively out of 167 in these two base. In shot selection, however, Dwight Howard ranks 11th and 2nd respectively in his suppression of shot attempts in the paint (bases 1 and 2), whereas Roy Hibbert ranks 161 in both bases 1 and 2. Whereas one defender may be good at discouraging shot attempts, the other may be better at challenging shots once a shooter decides to take it. This demonstrates that skilled defenders may impact the game in different ways, as a result of team defensive strategy and individual skill. Figure 8 visually depicts the contrasting impacts of these defenders. 

The defender effects do not always diverge so drastically between shot efficiency and frequency, however. Some defenders are effective at reducing both shot frequency and efficiency. For instance, Brandon Bass is the top ranked defender in reducing both shot frequency and shot efficiency in the perimeter (Table 5). 

Importantly, our model is informative about how opposing shooters perform against any defender in any region of the court. Even if a defender rarely defends shots in a particular region, they may still be partly responsible for giving up the shot in that region. As a point guard, Chris Paul defends relatively few shots in basis 1, yet the players he guards get fewer shots in this area relative to other point guards (Table 4), perhaps in part because he gets so many steals or is good at keeping players from driving toward the rim. As a defender he spends very little time in this court space, but we are still able to estimate how often his man beats him to the basket for a shot attempt. 

Finally, it is possible to use this model to help infer the best defensive matchups. Specifically, we can infer the expected points per possession a player should score if he were defended by a particular defender. Fittingly, we found that one of the best defenders on LeBron James is Kawhi Leonard. Leonard received a significant attention for his tenacious defense on James in both the 2013 and 2014 NBA finals. Seemingly, when the Heat play the Spurs and when James faces Leonard, we expect James to score fewer points per possession than he would against almost any other player. 

While our results yield a detailed picture of individual defensive characteristics, each defender’s effect should only be interpreted in the context of the team they play with. Certainly, many of these players would not come out as favorably if they did not play on some of the better defensive teams in the league. For instance, how much a point guard reduces opposing shot attempts in the paint may depend largely on whether that defender plays with an imposing center. Since basketball defense is inherently a team sport, isolating true individual effects is likely not possible without a comprehensive 

28 

FRANKS ET AL. 



<!-- Start of picture text -->
Dwight Howard LeBron James Chris Paul<br>Roy Hibbert Kevin Durant Tony Parker<br>qe ( 1 6 ) qe ( 5 6 ) qf  ( 1 6 ) qf  ( 5 6 )<br><!-- End of picture text -->

Fig 8 _. Defensive shot charts. The dots represent the locations of the shots faced by the defender, the color represents how the defender changes the expected shot efficiency of shots, and the size of the dot represents how the defender affects shot frequency, in terms of the efficiency quantiles qe and frequency quantiles qf . Hibbert and Howard’s contrasting defensive characteristics are immediately evident. Small circles illustrate that, not surprisingly, Chris Paul, the league leader in steals, reduces opponents’ shot frequency everywhere on the court._ 

understanding of both team defensive strategy and a model for the complex interactions between defenders. Nevertheless, our model provides detailed summaries of individual player effects in the context of their current team– a useful measure in its own right. A full set of offender and defender coefficients with standard errors can be found in Supplement A (Franks et al., 2015). 

**6. Discussion.** In this paper, we have shown that by carefully constructing features from optical player-tracking data, one is able to fill a current gap in basketball analytics – defensive metrics. Specifically, our approach allows us to characterize how players affect both shooting _frequency_ and _efficiency_ of the player they are guarding. By using an NMF-based 

29 

decomposition of the court, we find an efficient and data-driven characterization of common shot regions which naturally corresponds to common basketball intuition. Additionally, we are able to use this spatial decomposition to simply characterize the spatial shot and shot-guarding tendencies of players, giving a natural low-dimensional representation of a player’s shot chart. Further, to learn who is guarding whom we build a spatio-temporal model which is fit with a combination of the EM-algorithm and generalized least squares, giving simple closed-form updates for inference. Knowing who is guarding whom allows for understanding of which players draw significant attention, opening the court up for their teammates. Further, we can see which teams induce a significant amount of defensive switching, allowing us to characterize the “chaos” induced by teams both offensively and defensively. 

Combining this court representation and the mapping from offensive to defensive players, we are able to learn how players inhibit (or encourage) shot attempts in different regions of the court. Further, conditioned on a shot being taken, we study how the defender changes the probability of the shot being made. Moving forward, we plan to use our results to understand the effects of coaching by exploring the spatial characteristics and performance of players before and after trades or coaching changes. Similarly, we intend to look at the time-varying nature of defensive performance in an attempt to understand how players mature in their defensive ability. 

# SUPPLEMENTARY MATERIAL 

# **Supplement A: Additional Methods, Figures and Tables** 

(doi: COMPLETED BY THE TYPESETTER; .pdf). We describe detailed methodology related to the shot type parameterizations and include additional graphics. We also include tables ranking players impact on shot frequency and efficiency (offense and defense) in all court regions. 

# **Supplement B: Animations** 

(doi: COMPLETED BY THE TYPESETTER; .zip). We provide GIF animations illustrating the “who’s guarding whom” algorithm on different NBA possessions. 

30 

FRANKS ET AL. 

# **References.** 

National Basketball Association (2014). A Glossary of NBA Terms. http://www.NBA.com/analysis/00422966.html. 

Bishop, C. M. et al. (2006). _Pattern recognition and machine learning_ **1** . springer New York. 

- B¨ohning, D. (1992). Multinomial logistic regression algorithm. _Annals of the Institute of Statistical Mathematics_ **44** 197–200. 

- Brunet, J.-P., Tamayo, P., Golub, T. R. and Mesirov, J. P. (2004). Metagenes and molecular pattern discovery using matrix factorization. _Proceedings of the National Academy of Sciences of the United States of America_ **101.12** 4164-9. 

- Cervone, D., D’Amour, A., Bornn, L. and Goldsberry, K. (2014). POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data. 

- Cressie, N. (1993). _Statistics for spatial data_ **900** . Wiley New York. 

- Franks, A., Miller, A., Bornn, L. and Goldsberry, K. (2015). Supplement to “Characterizing the Spatial Structure of Defensive Skill in Professional Basketball”. 

- Gelman, A. and Rubin, D. B. (1992). Inference from iterative simulation using multiple sequences. _Statistical science_ 457–472. 

- Goldsberry, K. (2012). Courtvision: New visual and spatial analytics for the NBA. MIT Sloan Sports Analytics Conference. 

- Goldsberry, K. (2013). The Dwight Effect: A New Ensemble of Interior Defense Analytics for the NBA. MIT Sloan Sports Analytics Conference. 

- Kingman, J. F. C. (1992). _Poisson Processes_ . Oxford university press. 

- Kubatko, J., Oliver, D., Pelton, K. and Rosenbaum, D. T. (2007). A starting point for analyzing basketball statistics. _Journal of Quantitative Analysis in Sports_ **3** 1–22. 

- Lee, D. D. and Seung, H. S. (1999). Learning the parts of objects by non-negative matrix factorization. _Nature_ **401** 788–791. 

- Lee, D. D. and Seung, H. S. (2001). Algorithms for non-negative matrix factorization. _Advances in Neural Information Processing Systems (NIPS)_ **13** 556–562. 

- Limnios, N. and Oprisan, G. (2001). _Semi-Markov processes and reliability_ . Springer. 

- Macdonald, B. (2011). A regression-based adjusted plus-minus statistic for NHL players. _Journal of Quantitative Analysis in Sports_ **7** 4. 

- Maruotti, A. and Ryd´en, T. (2008). A semiparametric approach to hidden Markov models under longitudinal observations. _Statistics and Computing_ **19** 381–393. 

- Miller, A. C., Bornn, L., Adams, R. and Goldsberry, K. (2014). Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball In _Proceedings of the 31st International Conference on Machine Learning (ICML)_ . 

- Møller, J., Syversveen, A. R. and Waagepetersen, R. P. (1998). Log Gaussian Cox processes. _Scandinavian Journal of Statistics_ **25** 451–482. 

- Murphy, K. (2012). _Machine Learning: A Probabilistic Perspective_ . The MIT Press. 

- Rosenbaum, D. T. (2004). Measuring how NBA players help their teams win. _82Games. com (http://www.82games.com/comm30. htm)_ 4–30. 

- Sill, J. (2010). Improved NBA adjusted plus-minus using regularization and out-ofsample testing. In _Proceedings of the 2010 MIT Sloan Sports Analytics Conference_ . 

- Stan Development Team (2014). Stan: A C++ Library for Probability and Sampling, Version 2.2. 

- Thomas, A., Ventura, S. L., Jensen, S. T., Ma, S. et al. (2013). Competing process hazard function models for player ratings in ice hockey. _The Annals of Applied Statistics_ **7** 1497–1524. 

31 

Yu, S.-Z. (2010). Hidden semi-Markov models. _Artificial Intelligence_ **174** 215–243. 

Alexander Franks & Luke Bornn 1 Oxford Street, Cambridge, MA 02138 E-mail: afranks@fas.harvard.edu bornn@stat.harvard.edu 

Andrew Miller & Kirk Goldsberry 33 Oxford Street, Cambridge, MA 02138 E-mail: acm@seas.harvard.edu kgoldsberry@fas.harvard.edu 


