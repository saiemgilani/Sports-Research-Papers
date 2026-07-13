<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2025/2025 - Pairwise-Elo rating system - Wong et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

#### **Research Article** 

#### Kin Hang Wong* and Kazuhiko Shinki 

# **Pairwise-Elo rating system** 

https://doi.org/10.1515/jqas-2025-0150 Received September 18, 2025; accepted March 27, 2026; published online June 1, 2026 

**Abstract:** This paper proposes a binary time-series model which captures intransitivity in paired comparison by extending the classic Elo Rating System (ELO). Most existing rating systems assume that players’ ratings are totally ordered and that transitivity holds, which precludes situations where a player performs exceptionally well against a specific opponent regardless of their overall ability. The proposed model, called the Pairwise-Elo (P-ELO) model, allows us to (i) construct a hypothesis test for the existence of pairwise advantages (i.e., intransitivity) across the players, and (ii) estimate winning probabilities for each pair while incorporating these pairwise effects. We compare P-ELO to ELO and mElo2 _k_ on Sumo Wrestling, Mixed Martial Arts, StarCraft II, and Large Language Models (LLMs) evaluations, in terms of match outcome prediction and probability estimation. 

**Keywords:** time series; paired comparison; sports forecasting; intransitivity; Sumo wrestling; online games 

## **1 Introduction** 

The classic Elo Rating System (ELO) introduced by Elo (1978) is extensively applied in many areas. Examples include, but are not limited to assigning ratings to players in zerosum games like chess (Glickman and Doan 2024), as well as in certain individual/team sports such as pool (Fargorate 2018) and football (FIFA 2024; Hvattum and Arntzen 2010), ranking scientific journals (Lehmann and Wohlrabe 2017) and even assessing and monitoring changes in dominance relationships in highly dynamic animal systems (Neumann et al. 2011). ELO operates under the assumption that the probability of player _i_ defeating player _j_ is given by a 

***Corresponding author: Kin Hang Wong** , Department of Mathematics, Wayne State University, Detroit, USA, E-mail: kinhang@wayne.edu **Kazuhiko Shinki** , Department of Mathematics, Wayne State University, Detroit, USA, E-mail: shinki@wayne.edu 

univariate logistic function, where the only explanatory (or independent) variable is the difference between the current ratings of the two players (Elo 1978). The ratings of the two players will be updated after each game: _Ri_ ← _Ri_ + _K_ ( _X_ − _pij_ ) and _R j_ ← _R j_ − _K_ ( _X_ − _pij_ ), where _X_ is the game result for player _i_ (Loss = 0/Win = 1), _pij_ is the probability of player _i_ wins against player _j_ and _K_ is the speed of rating adjustment. The reward for the weaker player to win is correspondingly higher, reflecting their lower probability of winning. _K_ must be set in advance; a larger _K_ allows ratings to adjust more heavily to players’ recent performance but can introduce greater volatility, while a smaller _K_ leads to slower adjustments but more stable ratings. If the players’ strengths are constant over time, the BradleyTerry model (Bradley and Terry 1952) could estimate ratings more stable than ELO, as it is essentially a logistic regression with players’ ratings as independent continuous variables. However, since the Bradley–Terry model produces static ratings: once estimated, they remain fixed unless the model is re-calibrated with new data. By contrast, ELO is dynamic because individual ratings are updated sequentially after each game. In real-life applications, when the true strengths are believed to be constant, the Bradley-Terry model outperforms ELO. In May 2023, an ELO ranking (Chiang et al. 2024) was implemented for ranking Large Language Models (LLMs) (Zheng et al. 2023); however, in December 2023, it was replaced by the Bradley-Terry model because it is believed that LLMs should have constant true strengths by their nature (Chiang et al. 2023). 

Originally, ELO was not perceived as a time series model but only an online-approximation to the BradleyTerry model. Nevertheless, this approximation effectively captures time-varying strengths. Aldous (2017) illustrated how ELO could capture time-varying true strengths with simulations. Fahrmeir and Tutz (1994) and Duffield et al. (2024) acknowledged ELO as an updating scheme for time-varying performance and developed their own nonGaussian state space model to estimate time-varying abilities. 

Researchers have extended ELO and Bradley-Terry model as prediction tools on sports, for example tennis (Kovalchik 2016, 2020). In tennis (Kovalchik 2020), the concept of Margin of Victory (MoV) has been introduced into the ELO update formulas, thus replacing the binary outcome 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

with MoV and adjusting the winning probability accordingly. In the game of Go, one can extend the Bradley-Terry to include multiple factors such as offensiveness and susceptibility (Stanescu 2011), in addition to the rating difference. 

Since the logistic function maps rating differences to winning probabilities, it naturally models the binary outcome of a match. Throughout this paper, we will interpret ELO as a binary time-series model. From a statistical perspective, ELO can be viewed as a latent variable frequentist time-series model with players’ ratings as latent variables, and parameter _K_ , i.e., _no hyperparameters_ . This perspective has rarely, if ever, been investigated in the paired-comparison literature. In time series analysis, however, such perspective is common. The most popular one is the generalized autoregressive conditional heteroskedasticity (GARCH) model (Bollerslev 1986; Engle 1982), in which the latent time-varying volatility is estimated by a similar structure as the autoregressive moving average (ARMA) model. This perspective on ELO allows us to utilize the rich literature on statistical estimation and hypothesis test. 

Some researchers think that the constant adjustment speed of rating is not optimal. Ratings should adjust more quickly when only a few data points are available but update more slowly once sufficient data exists to reliably assess a player’s strength. To address the issue, the Glicko system developed by Glickman (1999, 2001) employed Bayesian framework. It incorporates a ratings deviation (RD) to distinguish the speed of updating ratings by the amount of information available for each player. A more recent development of Bayesian model is Microsoft’s TrueSkill (Herbrich et al. 2006) on online multiplayer teambased shooter games such as Gears of War and Halo. It assumes each player’s performance _pi_ follows a normal distribution around their skill _si_ with fixed variance, where skill is another normal distribution with the true strength _𝜇i_ as the mean and _𝜎i_<sup>2asthevariance.Giventhegame</sup> outcome, TrueSkill updates the posterior distributions over strength, and it is done using expectation propagation (Minka 2013). TrueSkill2 (Minka et al. 2018) is a model based on TrueSkill with additional information such as player’s tendency to quit in the middle of the game, player’s experiences, and more. 

In ELO, transitivity is intrinsically assumed between any 3 players, i.e., if player 1 is likely to beat player 2 and player 2 is likely to beat player 3, then it is implied that player 1 is likely to beat player 3 (detailed in a later section). Specifically, given _p_ 12 and _p_ 23, the logistic function used in ELO fully determines _p_ 13. As a result, rejecting such transitivity would automatically reject the Bradley-Terry model/ELO (Tang et al. 2025). The assumption of transitivity is often questionable in real-world settings. Although we can relax 

the model assumptions to better fit the data, for example by replacing the logistic function with another cumulative distribution function _F_ , it is impossible to fully relax the transitivity assumption when intransitivity is severe, e.g., a strong player may have a weakness against a specific weak opponent, resulting in a winning probability below 0.5. This is because for any strictly increasing function _F_ with _F_ (0) = 0.5, we always have that _F_ ( _a_ − _b_ ) _>_ 0.5 and _F_ ( _b_ − _c_ ) _>_ 0.5 imply _F_ ( _a_ − _c_ ) _>_ 0.5, showing a transitive relationship. To explain the intransitivity, at least one more dimension is needed. One convincing real-world example of intransitivity is that left-handed fencers have an advantage over righthanded fencers (Harris 2010). However, such a predictor is not always available, and one predictor may not fully explain all instances of intransitivity. In such a case, we may want to model the intransitivity exclusively based on the match results. 

Several prior studies have investigated intransitivity. The Blade-Chest model and the generalized Blade-Chest model (Chen and Joachims 2016; Gu et al. 2021) extend the Bradley-Terry model by adding parameters to identify pairwise advantages and to incorporate player intransitivity. They improve game prediction accuracy on certain types of games, such as StarCraft II and Street Fighter IV, while accuracy does not improve for other games, such as tennis and DotA 2. One reason could be that intransitivity is not significant for these games because of their nature. Kiraly and Qian developed a similar but more general model and analyzed English Premier League outcomes (Király and Qian 2017). Disc Decomposition by Bertrand used 2 _kn_ parameters to capture both additive and transitive components to allow intransitivity and significantly improved performance on probability estimation (Bertrand et al. 2023). Multi-dimensional Elo (mElo2 _k_ ), proposed by Balduzzi et al. at Google’s DeepMind (Balduzzi et al. 2018), extends standard Elo ratings by utilizing combinatorial Hodge theory and introduces cyclic components of dimension _n_ × 2 _k_ to better approximate empirical winning probabilities. These cyclic components capture non-transitive, pairwise advantages between players in addition to their scalar skill ratings. mElo2 _k_ introduces two additional hyperparameters, i.e., the dimension and the learning rate of the cyclic components, which must be tuned. Empirical studies indicate that the model performs best in settings where players’ true strengths are relatively stable over time and pairwise interaction effects are substantial (Lazaridis 2020a). Another dynamic model successfully relaxed the transitivity assumption by replacing the static parameters of pairwise-comparison models with continuoustime Gaussian processes and incorporating interaction features (Maystre et al. 2019). This approach improved game 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 3** 

prediction accuracy for StarCraft II, outperforming the Blade-Chess model in terms of log loss. 

In this paper, we extend ELO to account for pairwise advantages between any two players, thereby removing the need for the transitivity assumption. Our focus is on binary outcomes, win or loss. As described earlier, we draw inspiration from methodologies like ARCH (Engle 1982) and GARCH (Bollerslev 1986), and view ELO as a time series model with one parameter (one parameter _K_ driving _n_ latent timevarying variables, i.e., _n_ players’ ratings) for a binary time series, i.e., game results. 

To account for pair-specific strength between players, we introduce one additional parameter _K_ 2 to drive ( _n_ 2 ) additional latent variables, time-varying pairwise advantages, to capture player _i_ ’s advantage or disadvantage over player _j_ . We retain the parsimonious advantage of ELO to ensure that updates of the latent variables remain computationally manageable. ELO relies on players’ overall performance to determine winning probabilities between any two players. In contrast, our approach incorporates both general and pairwise track records to assess these probabilities. Although pairwise information is available, it does not replace the value of the general track record. For example, if player A and player B had a fifty-fifty head-to-head record many years ago but player A has since improved substantially, player B should no longer be expected to win 50 % of the time today. On the other hand, players’ pairwise advantage becomes particularly significant when a weaker player defeats a stronger opponent more often than anticipated. However, the pairwise advantage is less relevant when a strong player consistently wins against a weaker opponent, as such outcomes fall within expected norms. With this newly developed rating system, any intransitivity can be detected for player pairs with a sufficiently large number of encounters. When transitivity is strong, _K_ dominates _K_ 2, enabling the model to use all game results to estimate players’ strengths. When intransitivity is strong, _K_ 2 exceeds _K_ , and the model relies heavier on pairwise records to estimate winning probabilities. Our approach is conceptually related to mElo2 _k_ , but it is designed to be more robust to time-varying player strengths and observational noise by learning pairwise advantages sequentially. We call this model Pairwise-Elo (P-ELO) rating system. 

Most existing studies on ELO focus primarily on estimating players’ skill ratings. In contrast, our work focuses on estimating the parameters _K_ and _K_ 2, treating players’ ratings as latent variables rather than primary objects of inference. Within this framework, time-varying winning probabilities are inferred indirectly through the evolution of these latent ratings. By virtue of the parsimonious setting 

and the notion of _K_ and _K_ 2 as statistical parameters, our model also enables the testing on transitivity, which is rare in literature. An empirical hypothesis test is constructed using the likelihood ratio as the test statistic, with an empirical critical value determined by simulations. We use this hypothesis test to determine whether the transitivity assumption holds, and how significant the intransitivity is. 

The remainder of this paper is organized as follows. First, we re-introduce ELO and introduce our proposed model P-ELO in Section 2.1, presenting both in a GARCH-style time series formulation to highlight the similarities between ELO-type model and GARCH. Second, we develop the associated hypothesis-testing framework and conduct simulation studies in Section 2.2 and Appendix A to characterize the null distribution, find the empirical critical value and evaluate the power of the proposed test. Third, in addition to standard metrics such as accuracy and area under the curve, we introduce a performance measure in Section 2.3 based on a hypothetical value-betting evaluation for comparing binary prediction models. Fourth, we evaluate and compare the performance of ELO, mElo2 _k_ , and P-ELO in Section 3 on simulated datasets. Fifth, in Section 4, we apply our hypothesis test and model to four real-world datasets: Sumo Wrestling (Sumo), Mixed Martial Arts (MMA), StarCraft II (SC2), and large language model (LLM) evaluations; detecting intransitivity using corresponding empirical critical values and comparing models using accuracy, area under the curve, and the hypothetical value-betting evaluation. Finally, we provide a working example of P-ELO in Section 4.4 on Sumo wrestling to examine the evolution of player strengths and pairwise advantages. 

#### **List of abbreviations** 

Throughout this paper, we adopt the abbreviations listed in Table 1 for conciseness. 

**Table 1:** List of abbreviations used throughout the paper. 

|**Abbreviation**|**Description**|
|---|---|
|ELO|Classic Elo rating system|
|P-ELO|Pairwise Elo rating system|
|MLE|Maximum likelihood estimate|
|LRT|Likelihood ratio test|
|KS|Kolmogorov–Smirnov test|
|AD|Anderson–Darling test|
|AUC|Area under the curve|
|Sumo|Sumo wrestling|
|MMA|Mixed martial arts|
|SC2|StarCraft II|
|LLM|Large language model|



> **4 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

## **2 Methodology** 

#### **2.1 Models** 

##### **2.1.1 Classic ELO rating system (ELO)** 

In ELO, the difference between the two players’ ratings determines their winning probability. Suppose the _t_ th game is player _i_ versus player _j_ , then the probability of player _i_ with rating _Ri,t_ −1 wins against player _j_ with rating _R j,t_ −1 is a function of the difference in rating _Ri,t_ −1 − _R j,t_ −1, i.e., _pij,t_ = _P_ ( _i_ beats _j_ in the _t_ th game) = _u_ ( _Ri,t_ −1 − _R j,t_ −1), _u_ is a comparison function chosen to be a logistic function _𝜙_ . After the encounter, their ratings are updated based on _pij,t_ , the game result, and the parameter _K_ . A small _K_ makes the fluctuation of ratings smaller over time, which is appropriate when player strengths are constant. In practice, it is more realistic to expect that players’ abilities evolve: younger players tend to improve, older players may experience decline, and individual performance can fluctuate even over relatively short time horizons. 

To formulate ELO in a compact format for _n_ players and _N_ games, we use the following vector notation. 

1. **R0** = ( _R_ 1 _,_ 0 _, R_ 2 _,_ 0 _,_ … _, Rn,_ 0 )<sup>_T_</sup> ∈ ℝ<sup>_n_</sup> , the predefined/known initial ratings of the _n_ players 

2. **Rt** = ( _R_ 1 _,t, R_ 2 _,t,_ … _, Rn,t_ )<sup>_T_</sup> ∈ ℝ<sup>_n_</sup> , the ratings of the _n_ players after _t_ games 

3. _t_<sup>_g_</sup> ⋅⋅<sup>isthe</sup><sup>_t_thgamepairing.Givenaschedule,although</sup> _t_ determines first player _i_ and second player _j_ , we use _t_<sup>_g_</sup> _ij_<sup>asaconvenientwaytodenotethegamepairingat</sup><sup>_t_,</sup> where _i_ ≠ _j_ ∈ {1 _,_ 2 _,_ … _, n_ }. _t gij_ is a column vector takes the form _e_<sup>′</sup> _i_<sup>−</sup><sup>_e_′</sup> _j_<sup>where</sup><sup>_e_′</sup> _k_<sup>denotesthe</sup><sup>_k_thbasisvector</sup> of ℝ<sup>_n_</sup> 

4. _SN_ = {1 _g_ ⋅⋅ _,_ 2 _g_ ⋅⋅ _,_ … _, N g_ ⋅⋅}, a fixed _N_ -games schedule 



<!-- Start of picture text -->
⎛ 0 ⎞<br>⎜ ⎟<br>⎜ ... ⎟<br>⎜ ⎟<br>⎜ 0 ⎟<br>⎜ ⎟<br>⎜ 1 ⎟<br>⎜ ⎟<br>⎜ 0 ⎟<br>⎜ ⎟ player 1 is i , i th entry is 1;<br>t g i j = e ′ i − e ′ j = ⎜⎜ ... ⎟⎟ playerthe 2otheris j , entries j th entryareis0 . −1;<br>⎜ 0 ⎟<br>⎜ ⎟<br>⎜−1⎟<br>⎜ ⎟<br>⎜ 0 ⎟<br>⎜ ⎟<br>⎜ ... ⎟<br>⎟<br>⎜⎝ 0 ⎠<br><!-- End of picture text -->



with _p_ denotes the winning probability of the first player. In a typical ELO, _𝜙_ is a logistic function, 



Ratings of player _i_ and player _j_ will be updated according to (1) the game result, (2) the winning probabilities, and (3) parameter _K >_ 0. As derived in Appendix B: Update rules, the ratings of player _i_ and player _j_ after the _t_ th game are: 



Holistically, 



which could be written concisely using the recursive function below, 

where **Rt** depends on **Rt−1** , _K_ , the game pairing _t gij_ and game result _Xt_ . Therefore, contrary to the intuition that there are _n_ parameters in the model, **Rt** is actually a latent vector that evolves over time and is driven by only one parameter _K_ . This parsimonious setting is also observed in a popular time series model GARCH. 

##### **2.1.2 Pairwise-Elo rating system (P-ELO)** 

ELO employs a logistic comparison function _𝜙_ , which is strictly increasing and symmetric with _𝜙_ (0) = 0.5. As a result, the winning probabilities between any two players are expressed as monotonic functions of the differences between two latent variables, i.e., their ratings. By construction, winning probabilities for multiple pairs have to satisfy transitivity. We make the following example to illustrate this. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 5** 

**Example.** Suppose there are only 3 players in the player pool and two of the winning probabilities are known, i.e., _P_ (player 1 beats player 2) = _𝜙_ ( _R_ 1 − _R_ 2) = 0.6 and _P_ (player 2 beats player 3) = _𝜙_ ( _R_ 2 − _R_ 3) = 0.7. Then we have, 





The structure of ELO implies linear stochastic transitivity (Fishburn 1973), and consequently implies strong and weak stochastic transitivity (Davidson and Marschak 1959) which are below. 

**Definition 1** (Linear Stochastic Transitivity (LST)). There exist real-valued latent strength _𝜇k_ for each player _k_ and a increasing and symmetric function _F_ : ℝ → [0 _,_ 1] such that, for any pair of players _i_ and _j_ , 



**Definition 2** (Strong Stochastic Transitivity (SST)). For any three players _A_ , _B_ , and _C_ , if 



then 



**Definition 3** (Weak Stochastic Transitivity (WST)). For any three players _A_ , _B_ , and _C_ , if 



then 



In real-world settings, transitivity is often questionable. For instance, in the example above, the true (or empirical) probability _P_ (player 1 beats player 3) may be less than 0.5, violating the weak stochastic transitivity (WST); or it may between 0.6 and 0.7, violating the strong stochastic transitivity (SST). To achieve better calibration of winning probabilities, it is necessary to relax the transitivity assumptions. Our approach is to replace _Ri_ − _R j_ with _Ri_ + _qij_ − _R j_ for all _i, j_ , where _qij_ is a pair-specific term that allows for intransitivity. 

_n_ Building on ELO, we introduce ( 2 ) time-varying pairwise advantages as latent variables, between any two players. Let _Qt_ be a _n_ by _n_ matrix containing the pairwise advantages at time _t_ , 



where positive _qij,t_ denotes the advantage of player _i_ over player _j_ and negative _qij,t_ denotes the disadvantage of player _i_ over player _j_ , at time _t_ . It is worth observing that _Qt_ is an antisymmetric matrix, i.e., _qii,t_ = 0 for all _i_ , and _qij,t_ = − _qji,t_ for all _i, j_ and for all _t_ , 



_n_ so the total number of pairwise advantages in _Qt_ is ( 2 ) = _n_ <u>(</u> _n_ −1)<sup>This</sup><sup>_n_×</sup><sup>_n_pairwiseadvantagematrixcanbeviewed</sup> 2<sup>.</sup> as analogous to the pairwise advantage representation ( _C_<sup>_⊤_</sup> ) _n_ ×2 _k_ (Ω)2 _k_ ×2 _kC_ 2 _k_ × _n_ in mElo2 _k_ . However, unlike mElo2 _k_ , our approach does not rely on matrix decomposition or the introduction of a tuning hyperparameter _k_ . Instead, the matrix in Equation (7) has ( _n_ 2 ) latent parameters. Its entries are updated incrementally on a strictly pairwise basis: after a match between players _i_ and _j_ , _only_ the ( _i, j_ ) and ( _j, i_ ) entries of the pairwise advantage matrix are updated. The magnitude of these updates is governed by the newly introduced parameter _K_ 2 and the corresponding model-implied winning probabilities. Because updates are localized and do not propagate across unrelated player pairs, no orthogonalization is required. 

In mElo2 _k_ , the pairwise advantage matrix is parameterized by 2 _k_ latent variables. Because all pairwise advantages are functions of this shared low-rank latent representation, updating any of the 2 _k_ latent variables necessarily affects multiple, and potentially unrelated, pairwise interactions. Consequently, a match between players _i_ and _j_ induces changes not only in the estimated winning probability of _i_ versus _j_ , but also in the winning probabilities of player _i_ against all other players, and similarly for player _j_ . In other words, a single observation results in global adjustments rather than localized updates. While global adjustments are advantageous when players’ latent strengths remain constant over time, their performance under time-varying 

> **6 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

latent strengths is less well understood. In particular, it remains unclear whether global adjustments preserve or distort the temporal structure of inferred rating series, and how this affects the quality of winning probability estimates. 

_Ri,t_ −1 by _Ri,t_ −1 + _qn_ ( _i_ −1)+ _j,t_ −1. We also extend the game pairing column vector _t gij_ to _thij_ of the form _ei_ − _e j_ + _eni_ + _j_ with dimension _n_ + _n_<sup>2</sup> , where _ek_ is the basis vector of ℝ<sup>_n_+</sup><sup>_n_2</sup> . We multiply _ei_ , _e j_ and _eni_ + _j_ (note that the subscript shifted by + _n_ ) on **Wt** to obtain the player _i_ rating, player _j_ rating and pairwise advantage of _i_ on _j_ respectively. Such formulation is useful so that we can write: 

Moreover, from an algorithmic perspective, P-ELO can learn and infer pairwise advantages without requiring random initialization of the pairwise advantage matrix (Lazaridis 2020b). The initial pairwise advantage matrix in P-ELO is set to be the zero matrix. 



Suppose **Q** _t_ = vec( _Qt_ ) is a _row-major flattened_ vector of length _n_<sup>2</sup> , where the entry _qij,t_ of _Qt_ corresponds to the component _qn_ ( _i_ −1)+ _j,t_ of **Q** _t_ . We combine **Q** _t_ with **R** _t_ into **W** _t_ = ( **R** _t,_ **Q** _t_ ) ∈ ℝ<sup>_n_+</sup><sup>_n_2</sup> . The number of unknowns in **W** _t_ is only _n n_ + . ( 2 ) 

where 



**Example** (Row-major Flattening) Suppose _n_ = 3. Let 

After flattening _Qt_ , the resulting vector **Q** _t_ = vec( _Qt_ ) ∈ ℝ<sup>9</sup> takes the form: 



The update rules for _qij,t_ are similar to ELO Rating, derived in Appendix B: Update rules, with _K_ 2 ∈ ℝ being another appropriate parameter to be estimated, 

The corresponding **_W_** _t_ is ( **_R_** _t,_ **_Q_** _t_ ) = ( _R_ 1 _,t, R_ 2 _,t, R_ 3 _,t,_ 0 _, q_ 12 _,t, q_ 13 _,t,_ − _q_ 12 _,t,_ 0 _, q_ 23 _,t,_ − _q_ 13 _,t,_ − _q_ 23 _,t,_ 0). 

**Wt** can be introduced into formula (2), since now player _i_ has pairwise advantage _qij,t_ on player _j_ , we should replace 



Since **Wt** consists of **Rt** and **Qt** , we build on top of Equation (5): 



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 7** 

which could be written concisely using the recursive function below, 



where **Wt** depends on **Wt−1** , _K_ , _K_ 2, the game pairing _thij_ and game result _Xt_ . When _K_ 2 = 0, P-ELO reduced to ELO. 

P-ELO hereby assumes a game outcome _Xt_ depends not only on the ratings of the two involved players _i_ and _j_ , it also depends on the pairwise advantages _qij,t_ . **Wt−1** could be viewed as the _n_ + ( _n_ 2 ) latent variables driving the process { _Xt_ } _t_ ∈[1 _,_ 2 _,_ … _,N_ ]. 



#### **2.2 Estimation and statistical testing** 

##### **2.2.1 Estimation** 

Although _K_ is commonly treated as a constant governing the speed of adjustment in the Elo rating system, from a statistical perspective it should be optimized from the data. Similarly in P-ELO, we optimize the parameters _K_ and _K_ 2. Player ratings and the pairwise advantage matrix serve as latent variables in our framework, initialized to conventional values where each player is assigned a rating of 1,500 and all pairwise advantages are set to zero. This approach is consistent with ELO, and the ratings and pairwise advantages are updated iteratively throughout the optimization procedure. 

Given a fixed game schedule _SN_ and game results **X** = { _Xt_ } _t_ ∈[1 _,_ 2 _,_ … _,N_ ] ( _Xt_ = 1 and _Xt_ = 0 denote the win and loss of the first player, respectively), the likelihood under ELO is: 



_K_ determines how ratings evolve over time from the initial ratings **R0** , and therefore dictates the winning probability for each game, implying that _K_ can be estimated by maximum likelihood. On the other hand, the likelihood under P-ELO is: 



Parameters _K_ and _K_ 2 determine how the ratings and pairwise advantages evolve over time from the initial ratings 

and pairwise advantages **W0** , and therefore dictate the winning probability for each game. Similarly, _K_ and _K_ 2 can be estimated by maximum likelihood. Importantly, we do not restrict _K_ 2 to be non-negative, as we are testing whether _K_ 2 = 0, a value on the boundary of the constrained parameter space [0 _,_ +∞). While a positive _K_ 2 allows pairwise advantages to grow with repeated matchups, one possible natural interpretation of a negative _K_ 2 is: it captures a form of momentum or motivational asymmetry, whereby a player who previously lost may be more determined to prevail in their next encounter. A negative _K_ 2 therefore reflects a tendency for past outcomes to reverse rather than persist, which is a plausible behavioral pattern in combat sports such as Sumo wrestling and MMA. 

We note that, in P-ELO, the model extends the ELO framework by introducing ( _n_ 2 ) time-varying latent pairwise advantage variables. While maintaining these latent states incurs _O_ ( _n_<sup>2</sup> ) space complexity, once the parameters _K_ and _K_ 2 are estimated, the computational cost of rating updates remains _O_ (1) for each completed game, as only the pairwise advantage of the two competing players and their individual ratings are updated after each match using the observed outcome and the estimated parameter _K_ 2. In both ELO and P-ELO, re-estimating the update parameters _K_ in ELO (or ( _K, K_ 2 ) in P-ELO) via maximum likelihood has computational complexity _O_ ( _N_ ), where _N_ is the number of games. The actual runtime also depends on the optimization algorithm used to compute the MLE. 

##### **2.2.2 Statistical testing** 

With the maximum likelihood estimation of parameters _K_ and _K_ 2, we consider a standard likelihood ratio test to see whether ELO (the null hypothesis) is rejected against P-ELO (the alternative hypothesis). More precisely, this test examines whether the game results satisfy linear stochastic transitivity with a logistic CDF, as assumed in ELO. 

Under this hypothesis test: 



We define the test statistic of our test to be the likelihood ratio test (LRT) statistic: 



Since **Wt** changes over time, the winning probabilities are path dependent, i.e., a player with higher rating or pairwise advantage against another player means this player is more likely to win the next game. Although the game results 

> **8 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

are not i.i.d., they are conditionally independent, similar to GARCH, i.e., given the current rating, the game result does not depend on past game results. The joint probability function of all games depends on **Wt** , therefore depends on the binary game results. Although a sufficient condition to guarantee the regularity assumptions required for Wilks’ Theorem (Wilks 1938) is that game results are i.i.d., we did not analytically prove or disprove in this paper whether those regularity conditions hold for our model, given the complexity of the likelihood functions. Consequently, we defer the development of asymptotic theory to future work, and instead employ parametric bootstrapping to obtain an empirical critical value as the decision threshold. The full simulation and parametric bootstrapping results are available in Appendix A, demonstrating that the reliability of the likelihood ratio test depends strongly on both the number of players and the number of matchups per pair. If matchups in the full dataset are sparse, estimation can be restricted to a subset containing only top players, whose head-to-head encounters tend to be more frequent. 

We also examine the distributional behavior of _𝜆n_ empirically. Our simulations in Appendix A indicate that when the number of games _N_ is sufficiently large relative to the number of players _n_ , _𝜆n_ is well approximated by a _𝜒_<sup>2</sup> (1) distribution. Therefore, when computational resources are limited, using _𝜒_ 1<sup>2</sup> − _𝛼_<sup>(1)forasignificancelevel</sup><sup>_𝛼_asthecritical</sup> value provides a practical shortcut, supported by empirical evidence. 

#### **2.3 Performance comparison via a hypothetical value-betting evaluation** 

The strength of P-ELO over ELO lies in its ability to produce better probabilities in most cases using pairwise advantages. However, this refined probability, obtained through likelihood optimization, does not always result in significant improvements in binary prediction (Tang et al. 2025). This is particularly true when the prediction involves players with significantly different ratings, such that the outcome remains unchanged with a 50 % threshold (accuracy) or across all thresholds (AUC). For example, if player A has a 90 % winning probability against player B under ELO and 

60 % under P-ELO, both predictions still indicate that A will win. Another situation is the number of possible pairs is so large that the prediction improvement of P-ELO is limited because the same pair may not appear frequently. For example, with 200 players, there are 19,900 possible pairs, requiring a vast number of games to ensure each pair appears frequent enough. Therefore, relying solely on accuracy or AUC as performance measures may not be sufficient when the probabilities are consistently but slightly improved. On the other hand, while using likelihood or log-likelihood to compare model performance is a natural choice in our case, it may not be as straightforward as accuracy and AUC. In light of this, it is worthwhile to seek an alternative straightforward quantitative measure for comparing binary prediction model performance. 

Bookmakers usually rely on the pool of bettors to determine odds for sports betting. Hypothetically, if every bettor uses probabilities from ELO, it would determine the bookmaker’s (named X) odds. Now, consider a special bettor, Y, who instead estimates winning probabilities using P-ELO, which Y considers a closer approximation of the true outcome likelihood. From these estimates, Y constructs _their own set of fair odds_ reflecting not the market’s view, but their own. Instead of making a profit by speculating on the winning player, Y could profit solely by _value-betting_ , i.e., betting on “good deals” only. A good deal exists for Y whenever X’s offered odds are higher than the odds Y would assign to the same outcome. In the ELO and P-ELO context, this strategy is profitable most of the time only if P-ELO can produce more accurate, even if only slightly, _winning probabilities_ than ELO. 

It is worth noting that when a bookmaker’s odds perfectly reflect the true probabilities, value betting yields zero expected profit regardless of the model used. To illustrate, suppose bettor _Y_ assigns probability _py_ to a game outcome, the bookmaker assigns _p_ book, and the true probability is _p_ true. When 1∕ _p_ book _>_ 1∕ _py_ , the bookmaker’s odds on the outcome is a “good deal” to _Y_ ; otherwise, the odds on the opposing outcome are favorable. Concretely, if 1∕ _p_ book _>_ 1∕ _py_ , bettor _Y_ wagers on the first player; otherwise, on the second. The expected payoff, or expected value (EV), of a $d bet is: 



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 9** 

|from exploiting a poorly calibrated bookmaker<br> from this ground truth would yield high<br>calibration), and similarly for AUC. However,|f<br>**Bettor’s** **expected**<br>**value** **(EV)** **on** **$1**<br>**bet:** Use Equation<br>(16)<br>$0.20|$0.20|$0.14<br>_Remarks: positive EVs indicate that the bettor_|_remains_ _profitable_ _in_ _the_ _long_ _run,_ _despite_ _the_<br>_directional_ _predictions._|
|---|---|---|---|---|
|and AUC can profit <br>a dataset generated <br>g directions, better|**r’s** **decision:**<br> **if** odd **_>_**<br>_odd**,** bet P2 i<br>**_<_** fair_odd<br>on P1|on P1|on P2||
|accuracy <br>ersus D:  <br>es (wron <br>n.|**Betto**<br>**bet** **P1** <br>fair<br>odd  <br>bet $1|bet $1|bet $1<br>–||
|ng how a better-calibrated model with low <br>for matches A versus B, B versus C, and C v<br>n) and low accuracy for the bettor estimat<br>ning it is a profitable strategy in the long ru|**Model** **B:** **bettor**<br>**estimate** **of** **win**<br>**prob** **of** **P1** **(**est_wp_bet**);**<br>fair_odd **=**<br>1/est_wp_bet<br>0.51|0.52|0.48<br>_Remarks: the estimates are better but the_|_directions are off, i.e., low accuracy/AUC_|
|LO context, illustrati<br>e the ground truth <br>ons, worse calibratio<br>hree matches, mea|||_the directions are_||
|A value betting example, not limited to the ELO and P-E<br>ith high accuracy and AUC. The first three columns defin<br>e accuracy for the bookmaker estimates (correct directi<br>cted value (EV) of the bettor’s strategy is positive for all t|**True** **winning**<br>**probabilities** **of** **P1**<br>**(**real_wp**)**<br>**Model** **A:** **bookmaker**<br>**estimate** **of** **win**<br>**prob** **of** **P1**<br>**(**est_wp_bm**);** odd<br>**=** 1/est_wp_bm<br>0.48<br>0.40|0.49<br>0.41|0.51<br>0.57<br>–<br>_Remarks: the estimates are off but_|_correct,_ _i.e.,_ _high_ _accuracy/AUC_|
|**e** **2:** <br>el w<br>ictiv<br>expe|**P2**<br>B|C|D<br>–||
|**Tabl**<br>mod<br>pred<br>the|**P1**<br>A|B|C<br>–||



> **10 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

When the bookmaker’s odds reflect the true probabilities, i.e., _p_ book = _p_ true, the expected value of any bet of size $d is zero, regardless of the chosen outcome. Consequently, _py_ becomes irrelevant, showing that no predictive model can yield a positive expected edge under these conditions. 

In practice, the bettor observes only the bookmaker’s implied probabilities inferred from odds (and distorted by the margin), while the true data generating probabilities remain latent and outcomes are stochastic draws from this underlying distribution. Assessing a strategy’s performance therefore requires simulation, which yields a distribution of realized profits. The mean of this distribution will approach zero to the extent that the bookmaker’s probabilities are well-calibrated; conversely, it will be positive if the bettor’s probability estimates are better calibrated than the bookmaker’s. 

Table 2 is an example of how value betting works, independent of the ELO and P-ELO context. Value betting does not require the bettor to predict match outcomes correctly; it only requires the bettor’s probability estimates to 

be _better calibrated_ than the bookmaker’s. If the bookmaker systematically misprices odds, a bettor with more accurate probability estimates can achieve a positive expected value on each bet (i.e., profit in the long run), even if their directional predictions (i.e., who wins) are wrong. 

To analyze the distribution of the profit and the frequency of profitable outcomes, we simulate this strategy using the bootstrap method. Suppose Y does not bet on all available games but only chooses random games to bet $1 on. The bootstrap method involves repeatedly sampling with replacement from the original test dataset (all available games to bet on) to create multiple simulated datasets (a set of games Y chose to bet on). For each simulated dataset, we calculate the profit based on the betting strategy described. By analyzing the distribution of these profits across multiple simulations, we can estimate the expected profit and the probability of making a profit with this strategy. 

Figure 1 displays the profit distributions across several scenarios based on the designed example in Table 2: Model 

### **Hypothetical Value Betting Profit Distributions** 

_True prob: oracle (A vs B = 0.48, B vs C = 0.49, C vs D = 0.51) Model A: aggressive high−accuracy overestimator (0.40, 0.41, 0.57) Model B: near−true low−accuracy estimator (0.51, 0.52, 0.48) Each column shares the same bookmaker. Red dashed line = breakeven._ 



<!-- Start of picture text -->
Bettor: Model A Bettor: Model B<br>Bookmaker: True prob Bookmaker: True prob<br>600 600<br>500 500<br>400 400<br>300 300<br>200 200<br>100 100<br>0 0<br>−50 0 50 100 150 −50 0 50 100 150<br>Profit Profit<br>Bettor: Model A Bettor: Model B<br>Bookmaker: Model B Bookmaker: Model A<br>600 600<br>500 500<br>400 400<br>300 300<br>200 200<br>100 100<br>0 0<br>−50 0 50 100 150 −50 0 50 100 150<br>Profit Profit<br>Frequency Frequency<br>Frequency Frequency<br><!-- End of picture text -->

**Figure 1:** Simulated profit distributions from value betting under different bettor–bookmaker pairings. Bookmaker odds are derived from the probabilities in Table 2: true probabilities (oracle), Model A, and Model B. The red dashed line marks the breakeven point. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 11** 

A (an aggressive, high-accuracy overestimator) and Model B (a near-true, low-accuracy estimator), each benchmarked against the true probability, as well as Model A against Model B and vice versa. When the true probability serves as the bookmaker, neither Model A nor Model B exhibits any edge, confirming Equation (16) under _p_ book = _p_ true. When Model A acts as the bookmaker, however, the profit distribution of Model B shifts substantially to the right, i.e., indicating profit on every simulated instance, whereas when Model B acts as the bookmaker, the profit distribution of Model A shifts only marginally to the right. This asymmetry suggests that Model B’s probability estimates are better calibrated to the truth than Model A’s, and that a bookmaker pricing closer to the true probabilities affords less exploitable edge to competing estimators. 

For real-world datasets, where true winning probabilities are unobservable, we treat ELO as a well-established baseline model acting as the bookmaker, while P-ELO and other models function as the bettor’s probability estimators. The bettor has an edge when the probability distribution is systematically shifted to the right relative to the bookmaker (Figure 1). 

**Disclaimer:** This hypothetical value-betting evaluation is introduced solely as a performance comparison tool for probabilistic models. It is not intended to represent, approximate or encourage any real-world betting behavior. 



<!-- Start of picture text -->
3−Cycle Dominance Map<br>Red = Intransitive, Grey = Transitive<br>P4 P3<br>P5 P2<br>P6 P1<br>P7 P10<br>P8 P9<br><!-- End of picture text -->

**Figure 2:** Simulation 1: graphical representation of intransitivity derived from Table 3. 

## **3 Performance comparison on simulated data: Elo, mElo2** **_k_ , P-ELO** 

In this section, we examine how the proposed method captures pairwise advantages and its impact on prediction and winning probability estimation. We compare ELO, the Multi-dimensional ELO (mElo2 _k_ ), and our proposed P-ELO in scenarios where significant intransitivity exists. Since player strengths are not fully ordered in the presence of significant intransitivity, we do not attempt to produce an absolute ranking of the players. We generate datasets for two simulations: 

- **Simulation 1:** Player strengths remain constant over time. Game outcomes are simulated using a time-invariant winning probability matrix that incorporates extreme differences in player strengths as well as extreme intransitivities. Figure 2 illustrates the intransitivity cycles. This simulation design is motivated by the observations of the developer of the mElo2 _k_ R package, called “mElo” (Lazaridis 2020a), which point out that the matrix _C_ in mElo2 _k_ may not be adequately estimated if match outcomes are highly uncertain and/or players’ true ability is time-varying. 

- **Simulation 2:** This simulation is more general, with player strengths evolving over time, as illustrated in Figure 3, and incorporates a non-zero pairwise advantage matrix, as defined in Table 4. The resulting winning probabilities are also time-varying and the match results can be highly uncertain at some time periods, particularly when the winning probabilities hover around 0.5. 

We require a substantial number of games for each possible pair, but we also need to avoid excessive number of games due to computational limitations. Therefore, we generated 4,500 game results involving 10 players. Each player competes against every other player, resulting in 45 possible pairs. With 4,500 games, there are approximately 100 encounters in average between any two players, i.e., each pair’s performance is adequately represented. We evaluate performance using accuracy, area under the curve (AUC), and the hypothetical value-betting evaluation. 

For each simulation dataset, we performed a train/test split. The first 80 % (i.e., 3,600) of games were allocated for training, while accuracy, AUC, and hypothetical valuebetting evaluation, were conducted on the remaining 20 % (i.e., 900) of games. Specifically, under the hypothetical 

> **12 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



<!-- Start of picture text -->
Time−Varying Player Strengths<br>Player_A Player_B Player_C Player_D Player_E<br>0 1000 3000 0 1000 3000 0 1000 3000 0 1000 3000 0 1000 3000<br>Player_F Player_G Player_H Player_I Player_J<br>0 1000 3000 0 1000 3000 0 1000 3000 0 1000 3000 0 1000 3000<br>Time<br>2200 2200 2200 2200 2200<br>1800 1800 1800 1800 1800<br>1400 1400 1400 1400 1400<br>Strength 1000 1000 1000 1000 1000<br>2200 2200 2200 2200 2200<br>1800 1800 1800 1800 1800<br>1400 1400 1400 1400 1400<br>1000 1000 1000 1000 1000<br><!-- End of picture text -->

**Figure 3:** Simulation 2: true strength of the 10 players. 

**Table 3:** Simulation 1: winning probability matrix between 10 players. 

||**P1**|**P2**|**P3**|**P4**|**P5**|**P6**|**P7**|**P8**|**P9**|**P10**|
|---|---|---|---|---|---|---|---|---|---|---|
|P1|0|~~0.95~~|~~0.05~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P2|~~0.05~~|0|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P3|~~0.95~~|~~0.05~~|0|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P4|~~0.05~~|~~0.05~~|~~0.05~~|0|~~0.95~~|~~0.05~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P5|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|0|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P6|~~0.05~~|~~0.05~~|~~0.05~~|~~0.95~~|~~0.05~~|0|~~0.95~~|~~0.95~~|~~0.95~~|~~0.95~~|
|P7|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|0|~~0.95~~|~~0.05~~|~~0.95~~|
|P8|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|0|~~0.95~~|~~0.05~~|
|P9|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.95~~|~~0.05~~|0|~~0.95~~|
|P10|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.05~~|~~0.95~~|~~0.05~~|0|



**Table 4:** Simulation 2: pairwise advantages between the 10 players, i.e., a time-invariant matrix (7) with _n_ = 10. 

||**Player** **A**|**Player** **B**|**Player** **C**|**Player** **D**|**Player** **E**|**Player** **F**|**Player** **G**|**Player** **H**|**Player** **I**|**Player** **J**|
|---|---|---|---|---|---|---|---|---|---|---|
|Player A|0|380|40|−220|−300|−200|−380|20|−220|140|
|Player B|−380|0|−40|−260|−220|−220|60|40|180|−240|
|Player C|−40|40|0|240|−120|−300|80|240|−340|400|
|Player D|220|260|−240|0|−20|−160|320|400|−220|200|
|Player E|300|220|120|20|0|220|−240|200|120|−120|
|Player F|200|220|300|160|−220|0|40|340|−200|180|
|Player G|380|−60|−80|−320|240|−40|0|160|360|380|
|Player H|−20|−40|−240|−400|−200|−340|−160|0|80|100|
|Player I|220|−180|340|220|−120|200|−360|−80|0|−160|
|Player J|−140|240|−400|−200|120|−180|−380|−100|160|0|



value-betting evaluation, the bettor employing an alternative model randomly selects 400 games out of 900, with replacement, permitting duplicates. This betting strategy 

results in a profit or loss after all game results are revealed. This process is repeated 10,000 times to generate a distribution of profit and loss. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 13** 

#### **3.1 Simulation 1 results** 

**Table 5:** Comparison of model performance in simulation 1: accuracy and AUC. 

##### **3.1.1 MLE of parameters and evidence of intransitivity** 

During training, we estimate the maximum likelihood parameters for ELO, mElo, and P-ELO models. We used 1,500 as initial ratings, 0 as the initial pairwise advantages, and we retained the default initialization of the matrix _C_ as implemented in the mELO R package and do not pursue a separate investigation of initialization choices (Lazaridis 2020b) in this work. Specifically, we obtained the MLE of _K_ = 31 _._ 75 for ELO; for mElo, the MLEs are _k_ = 3, _𝜂_ 1 = 17 _._ 32, _𝜂_ 2 = 0 _._ 27 for the dimension, the learning rate for ratings and the learning rate for C respectively; and for P-ELO, the MLEs are _K_ = 25 _._ 82 and _K_ 2 = 140 _._ 58. The negative log-likelihoods of ELO and P-ELO are 1,325.98 and 884.79, respectively, resulting in a LRT statistic of 882.38. This value far exceeds the empirical critical value 4.018, specific to this simulation, indicating a high level of intransitivity. 

##### **3.1.2 Accuracy, area under the curve, hypothetical value-betting evaluation** 

The performance of the three models was evaluated using both accuracy and AUC; see Table 5. In terms of accuracy, the ELO/mElo/P-ELO models achieved 0.859/0.911/0.959 respectively, indicating that P-ELO consistently outperformed the other models. Similarly, for AUC, ELO/mElo/P-ELO obtained 0.824/0.823/0.863 respectively, demonstrating that P-ELO not only provides higher overall prediction accuracy but also has better discriminative ability. 

The hypothetical value-betting evaluation further illustrates the models’ performance in terms of calibration of winning probabilities, see Figure 4. Both mElo and P-ELO 

|**Metric**|**ELO**|**mElo**|**P-ELO**|
|---|---|---|---|
|Accuracy|0.859|0.911|0.959|
|AUC|0.824|0.823|0.863|



demonstrate promising profitability when ELO serves as the bookmaker, with P-ELO achieving a slightly higher mean profit than mElo. 

##### **3.1.3 Recovering the true winning probabilities** 

While accuracy and AUC remain key performance measures, the accurate estimation of winning probabilities is equally important. Since the dataset is simulated from a true winning probability matrix (Table 3), in addition to the hypothetical value-betting evaluation, we can directly assess the ability of the three models in terms of winning probabilities recovery. This comparison underscores the models’ capacity to recover the probabilistic structure of the data, an evaluation that is not feasible with real-world datasets since true winning probabilities are inherently unobservable. 

In total, we have 45 winning probabilities to recover for 10 players. Figure 5 illustrates the recovery of several of these probabilities across the three models. When pairs of players belong to the same group, as shown in Figure 2, namely P1 versus P2 and P9 versus P10, intransitivity is present, ELO performs significantly worse compared to mElo and P-ELO. In contrast, when pairs of players come from different groups, namely P1 versus P7, P2 versus P8, P4 



<!-- Start of picture text -->
Hypothetical Value Betting Scheme: Simulation 1<br><!-- End of picture text -->



<!-- Start of picture text -->
Profit of mElo  Profit of P−Elo<br> against Elo   against Elo<br> mean = 435.32  mean = 487.8<br>0 500 1500 0 500 1500<br>Profit Profit<br>1200<br>1000<br>600<br>400<br>Frequency Frequency<br>0 0<br><!-- End of picture text -->

**Figure 4:** Comparison of model performance in simulation 1: hypothetical value-betting evaluation. 

> **14 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 5:** Comparison of model performance in simulation 1: winning probabilities recovery. 

versus P8 and P6 versus P7, the performance of ELO is comparable to that of mElo and P-ELO. Furthermore, examining the recovery from mElo and P-ELO reveals that while mElo’s estimated winning probabilities generally approximate the true probabilities closely, they tend to be less stable than the estimates produced by P-ELO. 

**Table 6:** Comparison of model performance in simulation 2: accuracy and AUC. 

|**Metric**|**ELO**|**mElo**|**P-ELO**|
|---|---|---|---|
|Accuracy|0.733|0.626|0.774|
|AUC|0.791|0.653|0.842|



#### **3.2 Simulation 2 results** 

##### **3.2.2 Accuracy, area under the curve, hypothetical value-betting evaluation** 

##### **3.2.1 MLE of parameters and evidence of intransitivity** 

In this simulation, we obtained the MLE of _K_ = 28 _._ 92 for ELO; for mElo, the MLEs are _k_ = 1, _𝜂_ 1 = 1 and _𝜂_ 2 = 1 for the dimension, the learning rate for ratings, and the learning rate for C respectively; and for P-ELO, the MLEs are _K_ = 27 _._ 10 and _K_ 2 = 45 _._ 77. The negative log-likelihoods of ELO and P-ELO are 1,952.09 and 1,791.71, respectively, with corresponding LRT statistic of 320.76. Compared to the corresponding statistic in Simulation 1, this value is lower, suggesting a relatively weaker signal of intransitivity, consistent with the design. However, it still far exceeds the empirical critical value 4.048, specific to this simulation, indicating a statistically significant level of intransitivity. 

The accuracy and AUC performance of the three models was evaluated, see Table 6. Compared to Simulation 1, all models exhibited lower performance, reflecting the increased uncertainty intentionally introduced into the match outcomes. The ELO/mElo/P-ELO model achieved accuracies of 0.733/0.626/0.774 respectively, indicating that P-ELO consistently outperformed the other models, observed previously. For AUC, ELO/mElo/P-ELO obtained 0.791/0.653/0.842 respectively, confirming the same relative ordering of model strength as in Simulation 1. Overall, P- ELO provides higher overall prediction accuracy and better discriminative ability in distinguishing between match outcomes. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 15** 

## Hypothetical Value Betting Scheme: Simulation 2 



<!-- Start of picture text -->
Profit of mElo  Profit of P−Elo<br> against Elo   against Elo<br> mean = 64.67  mean = 215.43<br>−100 100 300 0 100 300 500<br>Profit Profit<br>1000 1000<br>400 400<br>Frequency Frequency<br>0 0<br><!-- End of picture text -->

**Figure 6:** Comparison of model performance in simulation 2: hypothetical value-betting evaluation. 

The hypothetical value-betting evaluation in Figure 6 indicates that mElo outperforms ELO, achieving profitability in over 50 % of the simulations, with a mean profit of 64.67. This suggests that mElo generally produces bettercalibrated probability estimates than ELO, enabling positive expected returns despite somewhat lower predictive accuracy. However, some miscalibrated estimates reduce both its discriminative power and overall profitability. In contrast, P-ELO substantially outperforms both ELO and mElo, achieving profitability in 100 % of the simulated comparisons against bookmaker ELO and attaining an expected profit of 215.43, markedly higher than that of mElo. 

##### **3.2.3 Recovering the winning probabilities** 

When comparing the recovery of winning probabilities, we first note that mElo fails to produce reliable estimates, consistent with the limitation reported by Lazaridis (2020a). In contrast, P-ELO outperformed ELO in cases of strong pairwise advantage, as shown in Table 4. Specifically, for Player A versus B ( _qAB_ = 380), Player A versus G ( _qAG_ = −380), and Player D versus H ( _qDH_ = 400), ELO systematically underestimates winning probabilities when the advantage is positive and overestimates them when the advantage is negative. For the pairs with weak or moderate pairwise advantages, such as Player B versus H ( _qBH_ = 40), Player F versus G ( _qFG_ = 40), and Player I versus J ( _qIJ_ = −160), the performance of ELO and P-ELO are comparable (Figure 7). 

## **4 Real-life examples: Sumo wrestling, MMA, StarCraft II and large language models** 

Sumo wrestling is a traditional Japanese sport where two wrestlers, or rikishi, face off in a circular ring called a dohyo. Wrestlers aim to force their opponent out of the ring or make them touch the ground with any part of their body other than their feet. It is widely known that certain pairs of Sumo wrestlers exhibit specific pairwise advantages due to differences in style, physical characteristics, experience, psychology, and training methods. The Grand Sumo Tournament has 6 seasons each year, and the 6 seasons (called basyo) are held in January, March, May, July, September and November. One exception is that there was no season in March 2011. There are 500–1,000 active wrestlers (called rikishi) in each season, and they are divided into six divisions: Makunouchi, Juryo, Makushita, Sandanme, Jyonidan and Jyonokuchi, by their rank. Each season consists of 15 days, and each of wrestlers in the top two divisions (Makunouchi and Juryo) plays 15 matches in each season, one match per day. All matches are made within the divisions, but occasionally there are cross-divisional matches. The top division consists of approximately 40 wrestlers in each season. The match results in the Grand Sumo Tournament are widely available through several publishers such as the Baseball Magazine Sha Co., Ltd. In this article, the data were 

> **16 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 7:** Comparison of model performance in simulation 2: Winning probabilities recovery. 

scraped from the Grand Sumo Tournament Records website at https://sumo-hositori.com/index.html. The data of the top division matches (i.e., Makunouchi) are collected from July 2001 to March 2019, and there were 31,013 matches between 204 wrestlers. Since wrestlers’ ring names (called shikona) occasionally change, all changes have been accounted for to maintain consistent records across name changes. 

Mixed Martial Arts (MMA) is a widely recognized fullcontact combat sport. Unlike Sumo wrestlers, MMA fighters do not face each other frequently. This characteristic makes MMA an intriguing case to explore the effectiveness of the proposed hypothesis test. This key characteristic suggests that, even if pairwise advantages exist between some players, they may play a less significant role in MMA match outcome prediction than in sports where competitors face each other more frequently. For this analysis, we used a publicly available dataset from Kaggle (2023). In MMA, we observed that many fighters did not appear frequently. Therefore, we selected the top 500 fighters based on the number of appearances and included only their matches. Note that these matches could involve a frequent fighter versus an infrequent fighter. 

StarCraft II has become a widely used benchmark for evaluating rating systems in online competitive environments. As a real-time strategy game, it features asymmetric gameplay in which players control one of three distinct races – Terran (T), Protoss (P), or Zerg (Z) – and most competitive matches are played in a one-versus-one format. Each race is designed to support a different strategic approach: Terran is generally regarded as balanced and adaptable, offering a wide range of tactical options but requiring careful economic and positional management; Protoss units are individually powerful and technologically advanced, though they are relatively expensive and limited in number; and Zerg emphasizes rapid unit production and territorial control, often at the cost of unit durability. These race-specific characteristics introduce complex, context-dependent interactions between players, making StarCraft II particularly well-suited for evaluating rating models that go beyond transitive strength assumptions. The dataset used in this study (Aligulac 2025) consists of StarCraft II matches played between January 1, 2011, and December 31, 2016, totaling 374,794 games. A large proportion of players in this dataset participated in only one or two matches, which may introduce noise and hinder meaningful 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 17** 

strength estimation. To address this, we filtered the dataset to include only frequent player pairings – specifically, those that occurred at least 7 times. This filtering process yielded a refined dataset comprising 37,215 matches involving 566 players. 

Large Language Models (LLMs), as introduced earlier, have been ranked using Bradley-Terry models. However, as demonstrated in the previous section, if there are pairwise advantages between any two LLMs, the reliability of rating estimations may be compromised, resulting in an inaccurate ranking. Our objective is to investigate the presence of pairwise advantages (transitivity) among LLMs. The search for a more effective leaderboard mechanism will be left to future research. The dataset we used is available online (Kaggle 2024). While we excluded draws from the dataset to facilitate the direct application of our proposed method, it is feasible to incorporate draws into the P-ELO method. 

expected, as MMA fighters rarely compete against the same opponents repeatedly; therefore, potential pairwise advantages between particular players do not substantially influence the results of matchups. 

#### **4.2 Accuracy and AUC** 

For all four datasets (Sumo, MMA, SC2, and LLM), we use the first 80 % of games/comparisons as the training dataset. We use the training data to find the MLE of _K_ and/or ( _K, K_ 2) and then use these estimates to predict game results/comparisons on the remaining 20 % of games/comparisons. For mElo2 _k_ , we use the default values _k_ = 1, _𝜂_ 1 = 16 and _𝜂_ 2 = 1 directly rather than optimizing due to the high computational cost and model instability. 

#### **4.1 Likelihood ratio test** 

##### **4.2.1 Sumo wrestling (Sumo)** 

As described in Section 2.2.2, large values of the test statistic _𝜆n_ , see Equation (15), provide strong evidence to reject the null hypothesis of no pairwise advantages among the pool of players. Using a significance level of _𝛼_ = 0.05, the rejection region is defined as _𝜆n_ greater than or equal to the corresponding empirical critical values, which are shown in Table 7. 

In the previous section, we showed that intransitivity is statistically significant among Sumo wrestlers. However, although the MLE of _K_ 2 is _K_ 2 = 19 _._ 04, significantly different from 0, the accuracy and AUC show little improvement. This is partly due to the limited number of matchups between wrestlers with similar ratings, in which pairwise advantage would matter most. In addition, with 204 wrestlers, 31,012 games, and 5,696 unique matchups, many pairs do not compete frequently enough for P-ELO to outperform ELO. When a pair competes infrequently, or when the estimated pairwise advantage is small, the pairwise advantage estimate may effectively function as noise, leading to spurious predictions. This negative effect may not be adequately offset when the overall number of frequently competing pairs is limited. Consequently, accuracy and AUC may be suboptimal metrics for evaluating model performance in datasets with sparse interactions (Table 8). 

The test statistic in Equation (15) was computed for all four real-world datasets using the full dataset. In the instances of Sumo, SC2 and LLM, we reject the null hypothesis with strong evidence (especially strong for SC2), indicating the significant violation of transitivity among the pool of wrestlers/players/models. Conversely, for MMA, we are unable to reject the null hypothesis. This outcome was 

**Table 7:** LRT on real-life datasets: Sumo, MMA, SC2, LLM. 

||**Sumo**|**MMA**|**SC2**|**LLM**|.|||||
|---|---|---|---|---|---|---|---|---|---|
|log-likelihood|−20,062.68|−3,506.47|−24,268.77|−24,967.94||||||
|under ELO<br>log-likelihood<br>under P-ELO|−20,017.81|−3,505.09|−24,105.38|−24,953.01|**Table** **8:** MLE of para<br>wrestling.|meters; and|the accuracy|and AUC on Sum|o|
|_𝜆_ _n_<br>Empirical|89.72<br>3.910|2.77<br>3.820|326.80<br>3.887|29.86<br>4.048|**Sumo wrestling**|**_K_**|**_K_** **2**|**Accuracy**|**AUC**|
|critical value|||||ELO|16.65|–|0.586|0.635|
|Evidence of|Strong|Very Weak|Very strong|Moderate|P-ELO|16.02|19.04|0.588|0.637|
|intransitivity|||||mElo 2|–|–|0.562|0.583|



> **18 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

##### **4.2.2 Mixed martial arts (MMA)** 

##### **4.2.4 Large language model (LLM)** 

In the analysis of MMA, we included only matches in which at least one participant was a frequent fighter, defined as a fighter with more than one appearance in the dataset. This filtering yielded 5,181 games involving 1,755 fighters, of whom 500 are classified as frequent. 

The dataset comprises 4,964 different matchups, with only one matchup appearing five times (Brandon Moreno vs. Deiveson Figueiredo), two appearing four times, 25 appearing three times, 157 appearing twice, and 4,779 appearing only once. Given this distribution, we can reasonably expect that pairwise advantages do not play a significant role in predicting outcomes in this dataset, even if they exist between some players. With such a limited number of frequent pairings, the estimate of _K_ 2 cannot be accurately calibrated, leading to a counterintuitive value −113.28 (Table 9). 

##### **4.2.3 StarCraft II (SC2)** 

In the analysis of SC2, we have analyzed a dataset comprising 567 players and 37,215 matches, post-selection of frequent matchups, i.e., each match up appeared at least seven times. 

The dataset contains 3,313 unique matchups. The estimated parameter _K_ 2 is notably higher than _K_ . While the AUC show greater improvement than in the Sumo wrestling dataset, potentially reflecting stronger intransitivity, the gains of both accuracy and AUC remain modest (Table 10). 

**Table 9:** MLE of parameters; and the accuracy and AUC on MMA. 

|**MMA**|**_K_**|**_K_** **2**|**Accuracy**|**AUC**|
|---|---|---|---|---|
|ELO|85.38|–|0.550|0.566|
|P-ELO|86.80|−113.28|0.547|0.563|
|mElo 2|–|–|0.510|0.514|



In the analysis of LLM, we have analyzed a dataset comprising 64 models and 39,716 comparisons from which draws were excluded. 

Within this dataset, we’ve identified 1,245 unique pairings. The results of the LRT indicate the presence of pairwise advantages while rejecting the assumption of transitivity. In our evaluation of the test dataset, consisting of 7,943 comparisons, we observed 350 prediction mismatches between ELO and P-ELO due to estimated pairwise advantages. Among these mismatches, ELO’s winning probabilities range from 0.44 to 0.56, whereas P-ELO’s range from 0.44 to 0.57. ELO accurately predicted 165 out of the 350 cases while P-ELO achieved 185 correct predictions. This modest difference accounts for the similarity in accuracy between the two models. 

Observe that the MLE estimates, _K_ in ELO and _K_ 2 in P-ELO, are small relative to a typical rating 1,500, indicating that model strengths do not vary rapidly or substantially over time. The estimated _K_ 2 is also small, a hint that the intransitivity exists but not strong, aligned with the LRT result in Table 7. A different approach, such as the Bradley-Terry model, may be more appropriate (Table 11). 

#### **4.3 Hypothetical value-betting evaluation** 

P-ELO demonstrated slightly better accuracy and AUC in predicting outcomes in Sumo and StarCraft II when intransitivity was particularly strong, and negligible improvement in LLM when intransitivity was moderate. In contrast, for MMA, the LRT did not reject the null hypothesis, suggesting that pairwise advantages have minimal impact on predictive performance. Although Sumo and LLM exhibit strong intransitivity, P-ELO did not yield substantial accuracy or AUC gains over traditional models. Consequently, we employ the hypothetical value-betting evaluation introduced earlier to assess the advantages of P-ELO over ELO. 

**Table 10:** MLE of parameters; and the accuracy and AUC on SC2. 

**Table 11:** MLE of parameters; and the accuracy and AUC on LLM. 

|**SC2**|**_K_**|**_K_** **2**|**Accuracy**|**AUC**|**LLM**|**_K_**|**_K_** **2**|**Accuracy**|**AUC**|
|---|---|---|---|---|---|---|---|---|---|
|ELO|20.16|–|0.626|0.680|ELO|8.79|–|0.649|0.708|
|P-ELO|14.89|38.06|0.628|0.684|P-ELO|8.29|3.42|0.649|0.708|
|mElo 2|–|–|0.585|0.610|mElo 2|–|–|0.602|0.642|



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 19** 



<!-- Start of picture text -->
Profit of Profit of<br>mElo against Elo P−Elo against Elo<br>(Sumo) (Sumo)<br> mean = 85.87  mean = 174.08<br>1200 1200<br>1000 1000<br>800 800<br>600 600<br>400 400<br>200 200<br>0 0<br>−200 −100 0 100 200 300 0 100 200 300 400<br>Profit Profit<br>Profit of Profit of<br>mElo against Elo P−Elo against Elo<br>(MMA) (MMA)<br> mean = 7.48  mean = −2.33<br>1500 1500<br>1000 1000<br>500 500<br>0 0<br>−50 0 50 100 −50 0 50<br>Profit Profit<br>Profit of Profit of<br>mElo against Elo P−Elo against Elo<br>(SC2) (SC2)<br> mean = 44  mean = 362.97<br>1000 1000<br>800 800<br>600 600<br>400 400<br>200 200<br>0 0<br>−200 −100 0 100 200 300 100 200 300 400 500 600<br>Profit Profit<br>Profit of Profit of<br>mElo against Elo P−Elo against Elo<br>(LLM) (LLM)<br> mean = −95.02  mean = 149.3<br>1000 1000<br>800 800<br>600 600<br>400 400<br>200 200<br>0 0<br>−400 −300 −200 −100 0 100 200 −200 −100 0 100 200 300 400 500<br>Profit Profit<br>Frequency Frequency<br>Frequency Frequency<br>Frequency Frequency<br>Frequency Frequency<br><!-- End of picture text -->

**Figure 8:** Profit distributions for mElo2 and P-ELO against Elo across the Sumo, MMA, SC2, and LLM datasets, based on 10,000 simulations. 

> **20 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

Figure 8 illustrates the profit and loss distribution of this betting strategy. In addition, we also compared mElo2 against ELO. 

We observe that mElo2 consistently underperforms relative to P-ELO, except on MMA, where ELO, mElo2, and P-ELO perform comparably. This underperformance is primarily due to overconfident probability estimates near zero, causing mElo2 to miss certain value-betting opportunities. Compared to ELO, mElo2 generally performs better in the presence of intransitivity, except on the LLM dataset, where it appears to overemphasize the inherent intransitivity patterns. Overall, the hypothetical valuebetting evaluation suggests that mElo2 achieves better calibration than ELO under intransitivity, despite lower accuracy and AUC, as shown in the previous section. P-ELO, on the other hand, outperforms both ELO and mElo2, 

achieving a higher probability of profit and a greater mean profit. 

In Sumo, selecting 3,101 out of 6,202 games for betting, P-ELO yields a profit 99.65 % of the time, with a mean profit/loss of +$174.08 and a standard deviation of $64.87. For MMA, selecting 518 out of 1,036 games, P-ELO does not outperform ELO. It achieves profitability in only 45.72 % of cases and yields an average profit/loss of −$2.33, indicating that P-ELO performs essentially on par with ELO with a slight disadvantage. In StarCraft II, choosing 3,722 out of 7,443 games, P-ELO achieves profitability 100 % of the time, with a mean profit/loss of $362.97 and a standard deviation of $72.76. Similarly, for LLM comparisons, P-ELO outperforms ELO, achieving profitability 96.8 % of the time, with a mean profit/loss of $149.30 and a standard deviation of $81.98. Overall, the profitability of P-ELO 

**Table 12:** 30 player matchups with the largest pairwise advantages or disadvantages for Player A. 

|**Index**|**Player** **A**|**Player** **B**|**Match** **count**|**ELO** **acc.** **(%)**|**P-ELO** **acc.** **(%)**|**Improved** **(T/F)**|**Gain** **(%** **points)**|
|---|---|---|---|---|---|---|---|
|1|Aminishiki|Asasekiryuu|19|53 %|58 %|True|5 %|
|2|Aminishiki|Tamakasuga|13|23 %|46 %|True|23 %|
|3|Aminishiki|Tochiouzan|34|62 %|71 %|True|9 %|
|4|Aoiyama|Takarafuji|20|75 %|85 %|True|10 %|
|5|Asase.|Juumon.|13|69 %|77 %|True|8 %|
|6|Asasekiryuu|Tokitenkuu|29|48 %|62 %|True|14 %|
|7|Asasekiryuu|Yoshikaze|13|46 %|62 %|True|15 %|
|8|Asasyouryuu|Kyokutenhou|37|95 %|95 %|True|0 %|
|9|Baruto|Kisenosato|27|52 %|67 %|True|15 %|
|10|Baruto|Kotoousyuu|26|42 %|50 %|True|8 %|
|11|Chiyotaikai|Wakanosato|27|70 %|81 %|True|11 %|
|12|Dejima|Kotonowaka|14|50 %|86 %|True|36 %|
|13|Futenou|Tochinonada|13|54 %|69 %|True|15 %|
|14|Gagamaru|Tamawashi|16|56 %|56 %|True|0 %|
|15|Goueidou|Takayasu|29|45 %|45 %|True|0 %|
|16|Harumafuji|Kotosyougiku|62|44 %|53 %|True|10 %|
|17|Hokutoriki|Tamanoshima|21|71 %|67 %|False|−5 %|
|18|Iwakiyama|Kakizoe|17|71 %|88 %|True|18 %|
|19|Kaiou|Kyokutenhou|34|88 %|88 %|True|0 %|
|20|Kakuryuu|Kotoousyuu|30|57 %|57 %|True|0 %|
|21|Kakuryuu|Takekaze|20|85 %|90 %|True|5 %|
|22|Kakuryuu|Tochiouzan|47|49 %|49 %|True|0 %|
|23|Kisenosato|Miyabiyama|21|71 %|76 %|True|5 %|
|24|Kitataiki|Tokitenkuu|19|47 %|68 %|True|21 %|
|25|Kotoousyuu|Miyabiyama|28|79 %|75 %|False|−4 %|
|26|Kotoousyuu|Syouhouzan|10|20 %|20 %|True|0 %|
|27|Kotosyougiku|Tokitenkuu|22|55 %|64 %|True|9 %|
|28|Mitakeumi|Tamawashi|18|67 %|78 %|True|11 %|
|29|Miyabiyama|Tamanoshima|20|80 %|85 %|True|5 %|
|30|Takamimori|Wakanosato|24|83 %|83 %|True|0 %|



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 21** 

against ELO across the Sumo, SC2, and LLM datasets aligns with the magnitude of the corresponding test statistic in Table 7. 

#### **4.4 Working example** 

In this section, we examine the largest pairwise advantages and disadvantages in Sumo wrestling. We compare ELO with _K_ = 15 _._ 6 and P-ELO with ( _K,̂ K_ 2 ) = (14 _._ 9 _,_ 17 _._ 9), which the parameters are estimated using the full dataset. Table 12 presents the top 30 player pairings with the most pronounced pairwise advantages, each based on at least 12 encounters. For most of these matchups, incorporating pairwise effects leads to substantial improvements in predictive accuracy. In several cases, no improvement is observed because the estimated pairwise advantage aligns with the 

stronger player, where the baseline ELO model already performs well. Two exceptional cases exhibit a slight decrease in accuracy; in these matchups, the players have similar ratings, causing ELO and P-ELO to agree on most predictions, while small rating perturbations introduced by the pairwise term occasionally (Index 17 and 25) cause P-ELO to make incorrect predictions when the two ratings are nearly identical. Such perturbations occur more frequently when the pairwise advantage is relatively small or when the number of encounters is limited; in both cases, prediction accuracy decreases, a decrease that can offset the anticipated improvements. 

In Table 13, we take a closer look at a significant improvement, i.e., Tamakasuga versus Aminishiki. Both ELO and P-ELO ratings consistently indicate that Tamakasuga is the weaker wrestler relative to Aminishiki, 

**Table 13:** Match history and ELO and P-ELO predictions for Tamakasuga versus Aminishiki. 

|**Season**|**A**|**B**|**Result**|**A_ELO**|**B_ELO**|**ELO pred.**|**A_PELO**|**B_PELO**|**PairAdv**|**PELO pred.**|
|---|---|---|---|---|---|---|---|---|---|---|
|200107|Tama.|Amini.|1|1,500.58|1,511.01|0|1,500.53|1,510.38|0.00|0|
|200111|Tama.|Amini.|1|1,456.52|1,502.65|0|1,458.09|1,501.84|9.22|0|
|200201|Tama.|Amini.|1|1,476.82|1,502.90|0|1,477.91|1,502.17|19.07|0|
|200203|Tama.|Amini.|1|1,467.22|1,531.05|0|1,468.70|1,528.50|28.17|0|
|200205|Tama.|Amini.|1|1,467.08|1,514.76|0|1,469.27|1,512.43|37.94|0|
|200207|Tama.|Amini.|0|1,478.11|1,505.25|0|1,478.98|1,504.58|47.04|1|
|200209|Tama.|Amini.|1|1,529.35|1,502.35|1|1,529.36|1,502.58|37.52|1|
|200409|Tama.|Amini.|1|1,394.87|1,464.37|0|1,399.26|1,464.91|44.85|0|
|200411|Tama.|Amini.|1|1,410.13|1,446.08|0|1,412.68|1,447.45|54.35|1|
|200501|Tama.|Amini.|1|1,461.70|1,422.82|1|1,460.85|1,426.19|62.81|1|
|200503|Tama.|Amini.|1|1,452.02|1,462.50|0|1,450.28|1,464.61|69.32|1|
|200505|Tama.|Amini.|1|1,480.20|1,509.74|0|1,477.99|1,510.53|76.87|1|
|200607|Tama.|Amini.|1|1,499.57|1,570.40|0|1,501.19|1,566.02|84.70|1|



**Table 14:** Match history and ELO and P-ELO predictions for Asasekiryuu versus Juumonji. 

|**Season**|**A**|**B**|**Result**|**A_ELO**|**B_ELO**|**ELO pred.**|**A_PELO**|**B_PELO**|**PairAdv**|**PELO pred.**|
|---|---|---|---|---|---|---|---|---|---|---|
|200303|Asase.|Juumon.|0|1,472.54|1,445.91|1|1,474.12|1,448.23|0.00|1|
|200305|Asase.|Juumon.|1|1,469.49|1,496.07|0|1,471.54|1,497.78|−9.63|0|
|200309|Asase.|Juumon.|1|1,515.47|1,442.11|1|1,515.54|1,446.00|0.26|1|
|200401|Asase.|Juumon.|1|1,462.87|1,466.50|0|1,466.22|1,469.95|7.44|1|
|200407|Asase.|Juumon.|1|1,521.97|1,467.91|1|1,521.32|1,473.09|16.31|1|
|200505|Asase.|Juumon.|1|1,489.16|1,518.15|0|1,491.83|1,520.57|23.63|0|
|200507|Asase.|Juumon.|1|1,493.89|1,473.44|1|1,496.37|1,478.08|32.72|1|
|200509|Asase.|Juumon.|1|1,544.55|1,435.21|1|1,544.07|1,439.72|40.38|1|
|200511|Asase.|Juumon.|1|1,548.92|1,480.73|1|1,547.77|1,483.67|45.81|1|
|200601|Asase.|Juumon.|1|1,520.41|1,466.05|1|1,522.75|1,469.50|52.03|1|
|200603|Asase.|Juumon.|1|1,520.89|1,466.34|1|1,521.97|1,471.36|58.35|1|
|200609|Asase.|Juumon.|1|1,581.39|1,444.04|1|1,579.53|1,445.58|64.60|1|
|200701|Asase.|Juumon.|1|1,597.95|1,394.73|1|1,596.47|1,400.21|68.93|1|



> **22 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

a conclusion that appears to contradict the observed match outcomes, in which Tamakasuga wins most encounters. Under the P-ELO framework, a positive pairwise advantage emerges from 0 and after approximately six matches, it begins to materially influence predictions. As this pairwise advantage continues to build up, P-ELO predictions increasingly diverge from those of standard ELO and achieve better predictive performance, particularly in later matches. 

In Table 14, we take a closer look at a case of slight improvement, i.e., Asasekiryuu versus Juumonji. Both ELO and P-ELO produce similar overall ratings; however, P- ELO additionally estimates a positive pairwise advantage arising from Asasekiryuu’s consistent victories, even as Asasekiryuu becomes the stronger player in later stages. Because the direction of the pairwise advantage aligns with the stronger player, it improves predictive accuracy primarily during the early period when the two players’ ratings have not yet substantially diverged. 

## **5 Conclusions** 

We propose an extension of the ELO rating system designed to capture intransitivity between players and develop an empirical hypothesis test framework for detecting this intransitivity. We begin by interpreting ELO as a binary time series model with _K_ as its sole parameter. Building on this, we introduce P-ELO, an extension of ELO that incorporates an additional parameter, _K_ 2, to model pairwise advantages. Both models remain parsimonious, enabling the use of an empirical likelihood ratio test (LRT) to formally detect intransitivity. 

The P-ELO model simultaneously estimates individual player strengths and pairwise advantages. When two players compete frequently, the pairwise advantage has a greater influence on predicted outcomes. We applied our approach to real-world datasets, including StarCraft II, Sumo wrestling, MMA, and LLM comparisons. The empirical likelihood ratio test shows that LLM, Sumo wrestling, and StarCraft II exhibit moderate, strong, and very strong intransitivity respectively, while MMA does not exhibit intransitivity, possibly due to the lack of repeated matchups. We also assessed improvements in predictive accuracy, AUC, and winning probability calibration. 

A key strength of P-ELO is its ability to estimate winning probabilities more accurately, as demonstrated through the hypothetical value-betting evaluation. Notably, improvements in accuracy and AUC are most pronounced 

in matchups that occur frequently with significant pairwise advantages. 

###### **Research ethics:** Not applicable. 

###### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

###### **Use of Large Language Models, AI and Machine Learning** 

**Tools:** Used ChatGPT to improve language. 

**Conflict of interest:** The authors state no of interest. 

###### **Research funding:** None declared. 

**Data availability:** In this article, the main dataset Sumo Wrestling data were scraped from the Grand Sumo Tournament Records website at https://sumo-hositori.com/index. html. The MMA dataset is obtained from Kaggle. https:// www.kaggle.com/datasets/danmcinerney/mma-differentials-and-elo/data. License: GNU Lesser General Public License. (2025 Sep update: the dataset has been deleted either by user/Kaggle). The StarCraft2 dataset is obtained from Aligulac. Starcraft 2 progaming statistics and predictions. http://aligulac.com/. The LLM dataset is obtained from Kaggle. https://www.kaggle.com/competitions/lmsys-chatbot-arena **.** License: Attribution-NonCommercial 4.0 International. The R package used in this paper is now available anonymously at https://github.com/pelointransitivity/PELO, a simple example is also provided. The package can be installed in R using the following command: remotes::install_ github(“pelointransitivity/PELO”). 

## **Appendix A** 

#### **Empirical null distribution: Monte Carlo simulation under random and realistic schedules** 

#### **Random schedules** 

To simulate the distribution of _𝜆n_ , we generate match outcomes under minimal assumptions. To foster engagement, players of comparable skill levels are typically matched against one another more frequently, but it remains unclear how to generalize this tendency for simulation purposes. Imposing any specific game scheduling framework would introduce restrictive assumptions, which is undesirable when the goal is to use simulation to obtain an empirical null distribution. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 23** 

Therefore, we generated simulated datasets across a grid defined by varying numbers of players and games, as shown in Table 15, and conducted random pairings for each configuration. The results can be found in Figures 10–27 and Tables 18–26. Given _n_ players, there are ( _n_ 2 ) possible pairings. The small, medium, and large regimes in Table 15 is defined by the average appearances of each pair, i.e., _N_ ∕( _n_ 2 ). It remains stable across _n_ , with approximate values of 0.7, 1.8, and 10.7 appearances per pair, respectively. 

Here we outline the general procedure used to conduct the simulations; detailed methodological steps are provided in Appendix C: Simulation Setup. Game schedules were generated randomly for varying numbers of players and games, and all player ratings were initialized to **R** 0 = 1 _,_ 500. Game results were then simulated sequentially under ELO, updating each player’s rating after every match using the true parameter _K_ . This sequential simulation reflects the assumption that a player’s current strength is captured by their latest rating, so subsequent game results depend on updated ratings. For each set of simulated outcomes, we computed the MLE of _K_ and ( _K, K_ 2), and calculated the corresponding statistic _𝜆n_ . The process was repeated for 1,000 distinct random seeds to obtain the distribution of the _𝜆n_ . This process is repeated for 11 distinct values of true parameter _K_ ∈ {0 _,_ 8 _,_ 16 _,_ … _,_ 80} with true parameter _K_ 2 = 0. 

The simulation results indicate that the quality of the _𝜒_<sup>2</sup> (1) approximation for the test statistic _𝜆n_ depends primarily on the number of players and number of games. In the smallest configurations, such as those involving eight players and 20/50 games (small/medium regime), the approximations are poor. Although the empirical means of the simulated statistics occasionally approach the theoretical value of one, the variances are consistently inflated and the distributions exhibit heavy tails. We conducted two goodness-of-fit tests: Kolmogorov–Smirnov(KS) and Anderson–Darling(AD), which frequently reject the null hypothesis that the test statistic follows _𝜒_<sup>2</sup> (1). QQ-plots show clear curvature and systematic departures from the reference line. These patterns demonstrate that the _𝜒_<sup>2</sup> (1) distribution does not provide a reliable approximation for the test statistic at this scale. 

**Table 15:** Pairs of ( _n, N_ ) for simulation setup. 

|**Players**|**Small** **regime**|**Medium** **regime**|**Large** **regime**|
|---|---|---|---|
|**(****_n_)**|**(**≈**0****_._7)**|**(**≈**1****_._8)**|**(**≈**10****_._7)**|
|8|(8, 20)|(8, 50)|(8, 300)|
|32|(32, 360)|(32, 900)|(32, 5,400)|
|128|(128, 5,800)|(128, 14,500)|(128, 87,000)|



When the number of games increases to 300 (large regime) in the same eight-player setting, the distributional behavior improves but remains unstable. The empirical means move closer to the one and the variances exhibit modest reductions; however, goodness-of-fit tests and graphical diagnostics continue to signal lack of similarities to a _𝜒_<sup>2</sup> (1) distribution. 

In contrast, once the experimental design expands to 32 players with a few hundred games (small/medium regime), the approximation improves substantially. Across the number of games scenarios, the empirical means and variances align closely with those of the _𝜒_<sup>2</sup> (1) distribution, and goodness-of-fit tests rarely reject the null. Visual diagnostics show only minor random deviations around the theoretical quantiles. As the number of games increases into the thousands (large regime), the approximation becomes reliable and the distribution of _𝜆n_ conforms closely to asymptotic expectations. 

For large number of players, 128 players and thousands of games, simulations show promising agreement with the _𝜒_<sup>2</sup> (1) reference distribution across all regimes. The sample means and variances remain extremely close to their theoretical counterparts, goodness-of-fit tests provide no meaningful evidence against the null, and QQ-plots well follow the reference line. In these data-rich settings, the asymptotic approximation stabilizes. 

Overall, the results reveal a clear pattern: the _𝜒_<sup>2</sup> (1) approximation becomes more accurate when there are sufficient number of players and games. Simulations with small number of players, even with several hundred games, fail to meet this requirement, whereas simulations with larger number of players and larger number of games satisfy it readily. Consequently, the determining factor is the scale of the experiment. 

#### **Realistic schedules – Sumo wrestling** 

As noted earlier, to promote engagement, players of similar skill levels are generally paired more frequently. Although it is unclear how to generalize game scheduling for simulation purposes, we show that, when applying the actual schedule from the Sumo Wrestling dataset, the null distribution remains close to _𝜒_<sup>2</sup> (1), as illustrated in Figures 28 and 29. The distribution largely follows _𝜒_<sup>2</sup> (1), however, the QQplots reveal deviations in the tails, prompting some concern. These are further examined using the goodness-of-fit tests, the KS and AD tests, as summarized in Table 27. 

For 11 values of true parameter _K_ , using a significance level of _𝛼_ = 0.05, the Bonferroni-adjusted threshold is 0.05∕11 ≈ 0.0045. Despite the tail departure, both the KS and AD tests indicate that the empirical distribution of _𝜆n_ is 

> **24 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

**Table 16:** Summary statistics of _𝜆n_ when _K_ is fixed at _K_ = 16. Means, variances and 95th-percentile are reported with 95 % bootstrap confidence intervals based on 1,000 resamples. The distribution of _𝜆n_ is well approximated by _𝜒_<sup>2</sup> (1). 

|**_K_**|**Mean**|**Variance**|**95th-percentile**|**KS**|**AD**|
|---|---|---|---|---|---|
||**[95** **%** **CI]**|**[95** **%** **CI]**|**[95** **%** **CI]**|**_p_-value**|**_p_-value**|
|16|1.03 [0.97, 1.10] 2.22|[1.85, 2.64]|3.91 [3.60, 4.17]|0.86|0.92|



approximately consistent with _𝜒_<sup>2</sup> (1). Furthermore, based on 1,000 resamples, the bootstrap confidence intervals for the observed mean and variance of the test statistic include the theoretical values _E_ ( _𝜒_<sup>2</sup> (1)) = 1 and Var( _𝜒_<sup>2</sup> (1)) = 2, respectively, thereby reinforcing the validity of our results. 

#### **Empirical critical value** 

As discussed earlier in Section 2.2.2, we determine the critical value empirically using parametric bootstrapping. The simulation setup mirrors that of the Sumo experiments described in Section 5, with the exception that the parameter _K_ is fixed at its MLE, _K_ = 16, under ELO. Based on 1,000 bootstrap replications, we obtain an estimated 95th percentile of the simulated test statistics of 3.91, with corresponding confidence interval [3.60 _,_ 4.17]; see Table 16. This estimate constitutes the empirical critical value for a test conducted at level _𝛼_ = 0.05. 

#### **Power of the test** 

How likely is the test to reject _H_ 0 when true parameter _K_ 2 ≠ 0? The test is only useful if it can identify _K_ 2 effectively, i.e., the test is more likely to reject _H_ 0 when true parameter | _K_ 2| is larger. This question can be addressed through 

**Table 17:** Simulation of _𝜆n_ , power curve of the test. 

|**_K_** ****|**_P_** **_H_** **1** **(reject** **_H_** **** **):** **%** **of** **_𝝀_** **_n_**<br>**larger** **than** **3.91**|**[0,** **1]**|
|---|---|---|
|−24|1.000||
|−16|0.974||
|−8|0.494||
|0|0.043||
|8|0.504||
|16|0.959||
|24|0.999||



simulations, following the same approach as in the previous section. Since the null distribution remains unchanged when using the Sumo Wrestling dataset, we employ it here to evaluate the power of the test. Assuming a significance level of _𝛼_ = 0.05, the power is defined as the probability that the LRT statistic exceeds the empirical critical value 3.91. 

The simulation approach parallels that of the empirical null distribution section. We constructed game schedules based on the Sumo Wrestling dataset, initializing all player ratings at 1,500 and all pairwise advantages at 0. For each of the seven distinct values of true parameter _K_ 2 ∈ {−24 _,_ −16 _,_ −8 _,_ 0 _,_ 8 _,_ 16 _,_ 24}, with true parameter _K_ = 40, we used 1,000 independent random seeds to produce distinct game outcomes. For each outcome, we computed the MLEs of _K_ and of ( _K, K_ 2), and obtained the corresponding statistic _𝜆n_ . The distribution of _𝜆n_ is illustrated in Figure 9, while Table 17 reports the proportion of the 1,000 values exceeding the threshold, representing the power. We can see that the power curve is standard, i.e., the larger the | _K_ 2|, the more likely we can reject _H_ 0. 



**Figure 9:** Distributions of test statistic under different values of true parameter _K_ 2. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 25** 

#### **Graphs and tables** 



**Figure 10:** (8 players 20 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 



**Figure 11:** (8 players 20 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

> **26 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

**Table 18:** (8 players 20 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|1.047 [0.972, 1.126]|1.518 [1.335, 1.709<br>]|6<br>4<br>0<br>0.0|0.0032|
|8|1.027 [0.952, 1.102]|1.455 [1.274, 1.641<br>]|7<br>3<br>1<br>0.0|2<br>6<br>0<br>0.0|
|16|1.009 [0.935, 1.083]|1.394 [1.214, 1.584<br>]|4<br>5<br>2<br>0.0|8<br>5<br>0<br>0.0|
|24|0.988 [0.915, 1.062]|1.372 [1.196, 1.560<br>]|3<br>5<br>8<br>0.0|0<br>9<br>3<br>0.0|
|32|0.987 [0.916, 1.062]|1.352 [1.174, 1.533<br>]|2<br>4<br>1<br>0.0|8<br>7<br>0<br>0.0|
|40|0.997 [0.927, 1.070]|1.321 [1.161, 1.479<br>]|0<br>9<br>0<br>0.0|0.0022|
|48|0.964 [0.895, 1.036]|1.281 [1.125, 1.438<br>]|0<br>1<br>5<br>1.0|1<br>0<br>4<br>0.0|
|56|0.959 [0.891, 1.028]|1.245 [1.093, 1.403<br>]|0<br>6<br>7<br>1.0|8<br>5<br>3<br>0.0|
|64|0.990 [0.923, 1.060]|1.229 [1.079, 1.387<br>]|2<br>8<br>0<br>0.0|0.0003|
|72|0.983 [0.915, 1.052]|1.213 [1.064, 1.371<br>]|2<br>2<br>2<br>0.0|0.0004|
|80|0.997 [0.928, 1.067]|1.243 [1.094, 1.396<br>]|1<br>6<br>0<br>0.0|0.0003|









**Figure 12:** (8 players 50 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 27** 



**Figure 13:** (8 players 50 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

**Table 19:** (8 players 50 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|1.195 [1.094, 1.301]|2.718 [2.109, 3.471]|0.002|0.000|
|8|1.165 [1.071, 1.266]|2.537 [1.992, 3.204]|0.002|0.000|
|16|1.118 [1.024, 1.217]|2.488 [1.955, 3.090]|0.101|0.060|
|24|1.128 [1.033, 1.228]|2.484 [1.990, 3.009]|0.029|0.024|
|32|1.120 [1.026, 1.215]|2.327 [1.904, 2.779]|0.018|0.008|
|40|1.124 [1.030, 1.221]|2.348 [1.964, 2.764]|0.108|0.025|
|48|1.086 [0.993, 1.182]|2.258 [1.846, 2.738]|0.349|0.121|
|56|1.147 [1.049, 1.247]|2.566 [2.057, 3.153]|0.030|0.013|
|64|1.160 [1.065, 1.260]|2.457 [1.993, 2.976]|0.014|0.003|
|72|1.179 [1.081, 1.282]|2.678 [2.161, 3.254]|0.023|0.002|
|80|1.222 [1.120, 1.329]|2.879 [2.320, 3.531]|0.005|0.000|



> **28 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 14:** (8 players 300 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 0, 8, 16, 24, 32, 40. 



**Figure 15:** (8 players 300 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 48, 56, 64, 72, 80. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 29** 

**Table 20:** (8 players 300 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|1.004 [0.924, 1.090]|1.838 [1.469, 2.250]|0.213|0.127|
|8|1.039 [0.957, 1.126]|1.874 [1.550, 2.219]|0.168|0.152|
|16|1.070 [0.984, 1.161]|2.003 [1.640, 2.395]|0.002|0.015|
|24|1.114 [1.022, 1.208]|2.317 [1.766, 2.955]|0.002|0.001|
|32|1.134 [1.039, 1.231]|2.415 [1.991, 2.866]|0.006|0.012|
|40|1.055 [0.966, 1.147]|2.148 [1.718, 2.617]|0.111|0.167|
|48|1.028 [0.941, 1.120]|2.097 [1.657, 2.574]|0.103|0.238|
|56|1.015 [0.929, 1.107]|2.004 [1.580, 2.464]|0.411|0.261|
|64|1.056 [0.970, 1.144]|1.994 [1.584, 2.483]|0.053|0.054|
|72|1.081 [0.988, 1.178]|2.386 [1.819, 3.050]|0.092|0.128|
|80|1.069 [0.973, 1.165]|2.380 [1.793, 3.083]|0.073|0.154|





**Figure 16:** (32 players 360 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 

> **30 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 17:** (32 players 360 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

**Table 21:** (32 players 360 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. All confidence intervals include the mean or variance. The Bonferroni-adjusted threshold is approximately 0.0045. All values are above this threshold. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|1.031 [0.942, 1.124]|2.239 [1.721, 2.855]|0.730|0.819|
|8|1.028 [0.944, 1.119]|2.040 [1.649, 2.473]|0.575|0.649|
|16|0.991 [0.907, 1.078]|1.863 [1.492, 2.296]|0.661|0.765|
|24|1.012 [0.932, 1.097]|1.774 [1.450, 2.136]|0.145|0.214|
|32|1.053 [0.969, 1.146]|2.060 [1.616, 2.572]|0.132|0.092|
|40|1.033 [0.947, 1.123]|2.060 [1.631, 2.570]|0.670|0.701|
|48|1.016 [0.931, 1.105]|1.963 [1.562, 2.463]|0.720|0.769|
|56|1.049 [0.958, 1.149]|2.346 [1.765, 3.037]|0.557|0.449|
|64|1.051 [0.958, 1.152]|2.490 [1.773, 3.451]|0.427|0.694|
|72|1.044 [0.955, 1.138]|2.211 [1.704, 2.778]|0.159|0.376|
|80|1.043 [0.956, 1.135]|2.129 [1.714, 2.577]|0.391|0.659|



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 31** 



**Figure 18:** (32 players 900 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 0, 8, 16, 24, 32, 40. 



**Figure 19:** (32 players 900 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 48, 56, 64, 72, 80. 

> **32 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

**Table 22:** (32 players 900 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|0.955 [0.878, 1.033]|1.571 [1.256, 1.932]|0.037|0.067|
|8|0.983 [0.903, 1.065]|1.693 [1.340, 2.089]|0.095|0.053|
|16|1.030 [0.947, 1.116]|1.904 [1.582, 2.252]|0.475|0.419|
|24|1.041 [0.954, 1.133]|2.045 [1.673, 2.446]|0.392|0.196|
|32|1.009 [0.925, 1.098]|1.959 [1.590, 2.365]|0.526|0.629|
|40|0.970 [0.894, 1.048]|1.564 [1.312, 1.843]|0.369|0.527|
|48|0.935 [0.859, 1.017]|1.632 [1.314, 1.990]|0.602|0.550|
|56|1.004 [0.921, 1.088]|1.855 [1.513, 2.246]|0.633|0.727|
|64|0.973 [0.887, 1.065]|1.981 [1.490, 2.578]|0.581|0.664|
|72|0.995 [0.911, 1.083]|1.935 [1.513, 2.412]|0.803|0.956|
|80|1.002 [0.917, 1.090]|1.961 [1.521, 2.442]|0.645|0.659|





**Figure 20:** (32 players 5,400 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 33** 



**Figure 21:** (32 players 5,400 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

**Table 23:** (32 players 5,400 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. All confidence intervals include the mean or variance of _𝜒_<sup>2</sup> (1). The Bonferroni-adjusted threshold is approximately 0.0045. All values are above this threshold. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|0.993 [0.904, 1.087]|2.179 [1.685, 2.775]|0.224|0.231|
|8|0.962 [0.883, 1.046]|1.795 [1.465, 2.144]|0.868|0.546|
|16|0.991 [0.905, 1.079]|2.008 [1.603, 2.494]|0.870|0.896|
|24|1.036 [0.950, 1.126]|2.005 [1.619, 2.429]|0.233|0.142|
|32|0.971 [0.887, 1.058]|1.945 [1.592, 2.323]|0.105|0.221|
|40|0.971 [0.884, 1.065]|2.151 [1.527, 3.036]|0.746|0.593|
|48|0.961 [0.879, 1.045]|1.783 [1.428, 2.189]|0.830|0.890|
|56|0.945 [0.869, 1.028]|1.662 [1.328, 2.048]|0.362|0.381|
|64|1.006 [0.923, 1.093]|1.876 [1.510, 2.266]|0.674|0.748|
|72|1.009 [0.928, 1.097]|1.851 [1.522, 2.215]|0.371|0.490|
|80|1.035 [0.944, 1.127]|2.170 [1.731, 2.664]|0.844|0.748|



> **34 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 22:** (128 players 5,800 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 0, 8, 16, 24, 32, 40. 



**Figure 23:** (128 players 5,800 games) Empirical distribution of _𝜆n_ with _𝜒_<sup>2</sup> (1) density overlay, and QQ-plots, _K_ = 48, 56, 64, 72, 80. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 35** 

**Table 24:** (128 players 5,800 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|0.998 [0.912, 1.087]|2.037 [1.559, 2.605]|0.937|0.933|
|8|0.976 [0.891, 1.065]|2.011 [1.577, 2.496]|0.185|0.215|
|16|0.979 [0.894, 1.066]|1.902 [1.527, 2.295]|0.852|0.762|
|24|0.987 [0.899, 1.078]|2.084 [1.668, 2.543]|0.557|0.553|
|32|1.000 [0.912, 1.089]|2.031 [1.642, 2.453]|0.909|0.977|
|40|0.989 [0.907, 1.077]|1.907 [1.520, 2.350]|0.931|0.780|
|48|0.999 [0.919, 1.085]|1.793 [1.443, 2.166]|0.273|0.208|
|56|1.096 [1.008, 1.189]|2.116 [1.770, 2.482]|0.096|0.030|
|64|0.987 [0.901, 1.076]|2.064 [1.487, 2.855]|0.874|0.885|
|72|1.053 [0.962, 1.145]|2.205 [1.778, 2.654]|0.756|0.712|
|80|0.964 [0.883, 1.049]|1.839 [1.452, 2.251]|0.519|0.509|





**Figure 24:** (128 players 14,500 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 

> **36 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 



**Figure 25:** (128 players 14,500 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

**Table 25:** (128 players 14,500 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|0.945 [0.861, 1.036]|1.911 [1.461, 2.447]|0.518|0.342|
|8|0.932 [0.848, 1.020]|1.891 [1.474, 2.366]|0.076|0.063|
|16|0.973 [0.889, 1.060]|1.943 [1.521, 2.413]|0.769|0.712|
|24|0.894[0.816, 0.977]|1.711 [1.372, 2.074]|0.020|0.011|
|32|0.980 [0.889, 1.074]|2.192 [1.744, 2.701]|0.181|0.131|
|40|0.942 [0.859, 1.030]|1.942 [1.448, 2.564]|0.110|0.095|
|48|0.968 [0.888, 1.051]|1.756 [1.396, 2.155]|0.969|0.963|
|56|1.019 [0.936, 1.105]|1.839 [1.490, 2.226]|0.166|0.232|
|64|1.022 [0.934, 1.114]|2.164 [1.710, 2.666]|0.925|0.876|
|72|1.002 [0.917, 1.088]|1.911 [1.537, 2.334]|0.850|0.859|
|80|1.038 [0.950, 1.133]|2.171 [1.623, 2.923]|0.294|0.213|



K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 37** 



_n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=0,8,16,24,32,40.</sup> 

**Figure 26:** (128 players 87,000 games) Empirical distribution of _𝜆_ 



**Figure 27:** (128 players 87,000 games) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,</sup><sup>_K_=48,56,64,72,80.</sup> 

> **38 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

**Table 26:** (128 players 87,000 games) Summary statistics of _𝜆n_ across different values of _K_ . Means and variances are reported with 95 % bootstrap confidence intervals. Confidence intervals that do not include the mean or variance of _𝜒_<sup>2</sup> (1) are shown in red. The Bonferroni-adjusted threshold is approximately 0.0045. Values below this threshold are shown in red. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|0.985 [0.900, 1.072]|1.911 [1.536, 2.328]|0.273|0.398|
|8|0.992 [0.908, 1.082]|1.965 [1.600, 2.359]|0.229|0.552|
|16|0.952 [0.870, 1.036]|1.835 [1.454, 2.265]|0.547|0.473|
|24|1.021 [0.938, 1.109]|1.879 [1.536, 2.271]|0.201|0.254|
|32|0.986 [0.902, 1.076]|1.963 [1.420, 2.619]|0.282|0.281|
|40|0.971 [0.884, 1.062]|1.998 [1.593, 2.454]|0.157|0.172|
|48|0.961 [0.869, 1.056]|2.254 [1.697, 2.933]|0.027|0.019|
|56|1.100[1.002, 1.202]|2.602[2.074, 3.190]|0.525|0.182|
|64|1.102[1.000, 1.204]|2.678[2.031, 3.423]|0.592|0.307|
|72|1.044 [0.953, 1.141]|2.314 [1.800, 2.906]|0.211|0.263|
|80|0.992 [0.910, 1.079]|1.866 [1.535, 2.212]|0.423|0.714|





**Figure 28:** (Sumo wrestling) Empirical distribution of _𝜆n_<sup>with</sup><sup>_𝜒_2(1)densityoverlay,andQQ-plots,trueparameter</sup><sup>_K_=0,8,16,24,32,40.</sup> 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 39** 

**Table 27:** (Sumo wrestling) Summary statistics of _𝜆n_ across different values of true parameter _K_ . Means and variances are reported with 95 % bootstrap confidence intervals based on 1,000 resamples. All confidence intervals include the mean or variance of _𝜒_<sup>2</sup> (1). The Bonferroni-adjusted threshold is approximately 0.0045. All values are above this threshold. 

|**_K_**|**Mean** **[95** **%** **CI]**|**Variance** **[95** **%** **CI]**|**KS** **_p_-value**|**AD** **_p_-value**|
|---|---|---|---|---|
|0|1.032 [0.945, 1.121]|2.013 [1.640, 2.428]|0.36|0.50|
|8|1.018 [0.935, 1.105]|1.927 [1.537, 2.363]|0.03|0.16|
|16|1.013 [0.923, 1.108]|2.191 [1.636, 2.875]|0.93|0.90|
|24|0.984 [0.902, 1.069]|1.870 [1.515, 2.261]|0.44|0.58|
|32|0.996 [0.911, 1.084]|1.980 [1.608, 2.383]|0.24|0.45|
|40|0.968 [0.882, 1.060]|1.996 [1.562, 2.481]|0.10|0.24|
|48|0.974 [0.889, 1.064]|1.997 [1.531, 2.566]|0.62|0.77|
|56|0.999 [0.918, 1.084]|1.728 [1.417, 2.069]|0.77|0.68|
|64|1.055 [0.964, 1.148]|2.232 [1.721, 2.818]|0.05|0.23|
|72|0.968 [0.883, 1.055]|1.859 [1.419, 2.403]|0.75|0.73|
|80|0.987 [0.899, 1.083]|2.208 [1.705, 2.795]|0.64|0.62|



## **Appendix B: Update rules** 

We have presented the update rules for both ELO and P-ELO ratings, Equations (3) and (9), respectively. Although the ELO update rules are widely reported in the literature in multiple formats, often with or without formal derivations, we provide a full derivation here for the sake of completeness and clarity. 

In the ELO/P-ELO, the winning probability of player _i_ against player _j_ is modeled using a logistic-like function, often scaled and with a base change (we have suppressed the subscript _t_ for notational simplicity): 



The corresponding likelihood and log-likelihood function for a single outcome _X_ (where _X_ = 1 indicates a win for player _i_ and _X_ = 0 otherwise) is given by: 





The score function is then: 





Using the explicit form of _𝜙_ (⋅), the score functions become: 



Computationally, using the gradient **ascent** method, we want to update _Ri_ , _R j_ and _qij_ in the direction that **maximizes** the log-likelihood function: 



The update rules, i.e., Equations (3) and (9), can be written by considering the cases _X_ = 0 and _X_ = 1 separately, and then restoring the subscript _t_ to the ratings and pairwise advantages to indicate the time step. 

> **40 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

## **Appendix C: Simulation setup** 

#### **Game schedule generation** 

See Figure 30 



**Figure 30:** Flowchart for uniform random game schedule generation. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 41** 

#### **Game result generation** 

See Figure 31 



**Figure 31:** Flowchart for game-by-game simulation under the ELO/P-ELO model with fixed _K_ . 

> **42 —** K. H. Wong and K. Shinki: Pairwise-Elo rating system 

#### **Obtain the null distribution** 

See Figure 32 



**Figure 32:** Flowchart for computing the likelihood-ratio test statistic test_stat for a single simulation seed. 

## **References** 

Aldous, D. (2017). Elo ratings and the sports model: a neglected topic in applied probability? _Stat. Sci._ 32: 616−629,. 

Aligulac (2025). Aligulac.com, Available at: http://aligulac.com/. 

Balduzzi, D., Tuyls, K., Perolat, J., and Graepel, T. (2018). Re-evaluating 

evaluation. _Adv. Neural Inf. Process. Syst._ 31. 

Bertrand, Q., Czarnecki, W.M., and Gidel, G. (2023). On the limitations of the elo, real-world games are transitive, not additive. In: 

_Proceedings of the 26th international conference on artificial intelligence and statistics_ . PMLR, pp. 2905−2921. 

Bollerslev, T. (1986). Generalized autoregressive conditional 

heteroskedasticity. _J. Econom._ 31: 307−327,. 

Bradley, R.A. and Terry, M.E. (1952). Rank analysis of incomplete block designs: I. The method of paired comparisons. _Biometrika_ 39: 324−345,. 

- Chen, S. and Joachims, T. (2016). Modeling intransitivity in matchup and comparison data. In: _Proceedings of the ninth ACM international conference on web search and data mining_ , pp. 227−236. 

Chiang, W.L., Li, T, Gonzalez, J.E., and Stoica, I. (2023). Chatbot arena: new models & ELO system update, _Blog post, Dec_ , Available at: 

https://lmsys.org/blog/2023-12-07-leaderboard/#transitionfrom-online-elo-rating-system-to-bradley-terry-model. 

Chiang, W.L., Zheng, L., Sheng, Y., Angelopoulos, A.N., Li, T., Li, D., Zhu, B., Zhang, H., Jordan, M., Gonzalez, J.E., et al. (2024). Chatbot arena: an open platform for evaluating llms by human preference. In: _Proceedings of the 41st international conference on machine learning_ , Vol. 235. PMLR. 

Davidson, D. and Marschak, J. (1959). Experimental tests of a stochastic decision theory. In: _Measurement: definitions and theories_ , 17. Springer, Dordrecht, Netherlands. 

Duffield, S., Power, S., and Rimella, L. (2024). A state-space perspective on modelling and inference for online skill rating. _J. Roy. Stat. Soc. C Appl. Stat._ 73: 1262−1282,. 

Elo, A.E. (1978). _The rating of chessplayers, past and present_ . Ishi Press, USA. Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with 

estimates of the variance of United Kingdom inflation. _Econometrica_ 50: 987−1007,. 

- Fahrmeir, L. and Tutz, G. (1994). Dynamic stochastic models for time-dependent ordered paired comparison systems. _J. Am. Stat. Assoc._ 89: 1438−1449,. 

- Fargorate (2018). FargoRate − a look behind the curtain − FargoRate blog, Available at: https://www.fargorate.com/fargorateblog/ archive/behindthecurtain/. 

K. H. Wong and K. Shinki: Pairwise-Elo rating system **— 43** 

- FIFA (2024). Men’s ranking, Available at: https://inside.fifa.com/fifaworld-ranking/men. 

- Fishburn, P.C. (1973). Binary choice probabilities: on the varieties of 

   - stochastic transitivity. _J. Math. Psychol._ 10: 327−352,. 

- Glickman, M.E. (1999). Parameter estimation in large dynamic paired comparison experiments. _J. Roy. Stat. Soc. C Appl. Stat._ 48: 377−394,. 

- Glickman, M.E. (2001). Dynamic paired comparison models with stochastic variances. _J. Appl. Stat._ 28: 673−689,. 

- Glickman, M. and Doan, T. (2024). The US chess rating system, Available at: https://new.uschess.org/sites/default/files/media/documents/ us_chess_rating_system_specs-2024-03-01.pdf. 

- Gu, Y., Duan, J., and Kashima, H. (2021). An intransitivity model for matchup and pairwise comparison. In: _2020 25th international conference on pattern recognition (ICPR)_ . IEEE, pp. 692−698. 

- Harris, L.J. (2010). In fencing, what gives left-handers the edge? Views from the present and the distant past. _Laterality_ 15: 15−55,. 

- Herbrich, R., Minka, T., and Graepel, T. (2006). TrueSkill<sup>TM</sup> : a Bayesian skill rating system. _Adv. Neural Inf. Process. Syst._ 19. 

- Hvattum, L.M. and Arntzen, H. (2010). Using ELO ratings for match result prediction in association football. _Int. J. Forecast._ 26: 460−470,. 

- Kaggle. (2023). UFC/MMA biggest dataset with differentials, Available at: https://www.kaggle.com/datasets/danmcinerney/mmadifferentials-and-elo/data. 

- Kaggle. (2024). LMSYS − Chatbot arena human preference predictions, Available at: https://www.kaggle.com/competitions/lmsys-chatbotarena. 

- Király, F.J. and Qian, Z. (2017). Modelling competitive sports: Bradley-Terry-Elo models for supervised and on-line learning of paired competition outcomes. _arXiv e-prints_ arXiv:1701.08055. 

- Kovalchik, S.A. (2016). Searching for the GOAT of tennis win prediction. _J. Quant. Anal. Sports_ 12: 127−138,. 

- Kovalchik, S. (2020). Extension of ELO to margin of victory. _Int. J. Forecast._ 36: 1329−1341,. 

- Lazaridis, D. (2020a). An R package for multidimensional ELO ratings, Available at: https://github.com/dclaz/mELO/. 

- Lazaridis, D. (2020b). Impact of noisy or probabilistic outcomes in mELO models, Available at: https://dclaz.github.io/mELO/articles/03_ noise.html. 

- Lehmann, R. and Wohlrabe, K. (2017). Who is the ‘Journal Grand Master’? A new ranking based on ELO. _J. Informetr._ 11: 800−809,. 

- Maystre, L., Kristof, V., and Grossglauser, M. (2019). Pairwise 

   - comparisons with flexible time-dynamics. In: _Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining_ , pp. 1236−1246. 

- Minka, T.P. (2013). Expectation propagation for approximate Bayesian inference. _arXiv preprint_ , arXiv:1301.2294. 

- Minka, T., Cleven, R., and Zaykov, Y. (2018). Trueskill 2: an improved Bayesian skill rating system. _Technical Report_ , Available at: https:// www.microsoft.com/en-us/research/publication/trueskill-2improved-bayesian-skill-rating-system/. 

- Neumann, C., Duboscq, J., Dubuc, C., Ginting, A., Irwan, A.M., Agil, M., Widdig, A., and Engelhardt, A. (2011). Assessing dominance hierarchies: validation and advantages of progressive evaluation with Elo-rating. _Anim. Behav._ 82: 911−921,. 

- Stanescu, M. (2011). Rating systems with multiple factors, Master’s thesis. School of Informatics, University of Edinburgh. 

- Tang, S., Wang, Y., and Jin, C. (2025). Is elo rating reliable? A study under model misspecification. _arXiv e-prints_ arXiv:2502.10985. 

- Wilks, S.S. (1938). The large-sample distribution of the likelihood ratio for testing composite hypotheses. _Ann. Math. Stat._ 9: 60−62,. 

- Zheng, L., Sheng, Y., Chiang, W.L., Zhang, H., Gonzalez, J.E., and Stoica, I. (2023). Chatbot arena: benchmarking LLMs in the Wild with ELO ratings. _Blog post, May_ , Available at: https://lmsys.org/blog/202305-03-arena/. 


