<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Analytics, have some humility a statistical view of fourth down decision making - Unknown Authors.pdf -->

- **Analytics, have some humility: a statistical view of fourth down decision making** 

**Ryan Brill and Abraham Wyner** 

**University of Pennsylvania** 

**NESSIS, September 2023** 

1 

- **In-game strategic decision making** • The mathematical basis of in-game strategic decision making is a _value function V x x_ ( ) which tells us the value of game-state 

- • In American football: 1. Expected points (EP) 

2. Win probability (WP) 

- Make the decision which maximizes the value of the next game-state •<sup>Make the fourth down decision in</sup> Go FG Punt which { , , } 

- maximizes win probability 

2 

# **Model Land** 

- Two ways to build these EP/WP models: 

   1. Probabilistic state-space models 

   - require detailed specification of all game-states, actions, and their transition probabilities; incredibly hard 

   - • “Gei gazinta hait”  (Yiddish for “go in good health”)- explore these models on your own time, but will not be the subject of today’s talk 

   - 2. Statistical models • Data-driven regression/ML models fit from historical data 

      - Widely used today;  we will focus on these models 

      - • We discovered several problems with the way they are implemented, fit, and applied 

3 

# **Expected points models** 

4 

|**Well Kn**<br>|**own Expe**<br>|**cted Points Mode**<br> <br>|**ls**<br>|
|---|---|---|---|
|**Modeler**|**Model**|**Game-state Variables**<br>**Training set**|**Outcome Variable**|
|Romer (2006)|Instrumental variables<br>regression|yardline<br>all plays|_Points_of the next score,<br>a real number in<br>{7,3,2,0,-2,-3,-7}|
|Burke (2009)|Linear regression with a<br>spline|yardline<br>frst down plays|_^_|
|Yurko et al. (2018)|Multinomial logistic<br>regression|yardline, down, log<br>yards-to-go, time<br>remaining, goal-to-go,<br>under-two-minutes<br>all plays|_Outcome_of the next<br>score as categorical<br>variable in {TD, FG, …}<br>𝖤𝖯= 7 ⋅ℙ(TD)+ 3 ⋅ℙ(FG)+ ⋯|
|Baldwin (2021)|XGBoost|~~5~~<br>yardline, down, yards-<br>to-go, time remaining,<br>timeouts, home, roof<br>type, era<br>all plays|_^_|



~~5~~ 

- **EP models don’t adjust for team quality** 

- Existing EP models are functions of yard-line, down, yards-to-go, time remaining, timeouts, etc. 

- • But these models don’t adjust for team quality. 

- • Justification for omitting team quality: 1. Models represent EP for an _average_ offense facing an _average_ defense, and so imply decision making for _average_ teams. 

- 2. It is not easy to adjust for team quality alongside all these other variables, which have nonlinear relationships and interactions. 

6 

- **Thought experiment** 

- 1. What is the probability that an _“average” NFL kicker_ sinks a 70 yard field goal in neutral weather conditions? 

- 2. What is the probability that _Justin Tucker_ sinks a 70 yard field goal in neutral weather conditions? 

- 3. What is the probability that a _randomly drawn kicker_ sinks a 70 yard field goal in neutral weather conditions? 

7 

- **Problem 1. EP models don’t adjust for team quality** 





Failing to adjust for team quality causes problems: 

1. Models report EP for _randomly drawn teams_ , not for average teams. 

• No team wants this! • No such thing as a decision made by a random team! 

_Good teams have more plays_ 

_Good teams score more points_ 

2. **selection bias** problem; EP models are especially wrong/ biased 

Base-rate across all yardlines: (32%, 40%, 27%) 

8 Base-rate across all yardlines: (2.5, 1.7, 0.8) 

- **We need to adjust for team quality** EP models that don’t adjust for team quality are biased. 

9 

**Thought experiment 2** Suppose I have the following 8 aspects of team quality, each on the same scale, built from play success, and without data bleed. Then build an EP model with these 8 metrics as covariates. • Rank in terms of ( _predictive_ ) importance: A. Offensive team’s quarterback quality B. Offensive team’s non-quarterback offensive quality C. Defensive team’s defensive quality against the pass D. Defensive team’s defensive quality against the run E. Offensive team’s defensive quality against the pass F. Offensive team’s defensive quality against the run G. Defensive team’s quarterback quality H. Defensive team’s non-quarterback offensive quality 

10 

- **Impact of various aspects of team quality** 



<!-- Start of picture text -->
both  teams matters more than other aspects of team quality!<br><!-- End of picture text -->

- Created our own 8 measures of offensive & defensive quality • Carefully controlled for data bleed 

- • All 4 offensive quality metrics are more impactful than the defensive quality metrics 

- • Quarterback quality of _both_ teams matters more than other aspects of team quality! 

- • Output from an additive multinomial logistic regression model (similar to Yurko et al.’s): 



11 

- **Problem 2. So many variables…** • We need to adjust for team quality 

- • _Wow_ , that’s a lot of variables – team quality, yardline, down, yards-to-go, time remaining, etc. – with nonlinearities & interactions 

   - The task is not easy: we need to fit a very big and very complicated machine learning model, but we don’t want to overfit 

12 

- **Problem 2. Bias-Variance Tradeoff** 

- • We want to use machine learning to capture a complex high-dimensional function 

- • But ML models tend to aggressively overfit (play-by-play) data 

- • Typically deal with this using regularization or shrinkage towards simpler models 

- • Easily studied for parametric models in a Bayesian context; difficult for ML/trees 

- “The in-game models are not Bayesian.  Congratulations to you if you can figure out how to do that.  Most publicly available models are … XGBoost models. ” — Brian Burke, Wharton Moneyball, 19 Sept. 2023 

13 

- **Solution 2. Catalytic Priors to Mitigate Overfitting** • Inspired by Sam Kou’s catalytic prior, we found a way to Laplace smooth tree ML models 



14 

# **EP Model Comparison** 

|**Model**<br>**name**|**Model type**|**Team**<br>**quality**|**Out-of-sample**<br>**MAE**|
|---|---|---|---|
|Catalytic|**Catalytic XGBoost**|Yes|**3.744**|
|Yurko+|Multinomial logistic<br>regression|Yes|3.749|
|Baldwin+|XGBoost classifcation|Yes|3.753|
|Baldwin<br>(2021)|XGBoost classifcation|No|3.803|
|Yurko<br>(2018)|Multinomial logistic<br>regression|No|3.808|
|Burke<br>(2009)|Linear regression|No|3.833|
|Romer<br>(2006)|Instrumental variables<br>regression|No|3.864|



•<sup>EP models are biased and</sup> overfit, and we can improve upon that 

- <sup>On subsets of plays our model is</sup> _much_ better, and that can make a huge difference in decision making 

15 

- **Win probability models** 

16 

   - **Problem 3. Highly Auto-Correlated Data** 

- Play-by-play dataset of ≈ 500,000 plays 

- • But, _not_ 500,000 independent outcome variables • The response variable: 1 if the team with possession wins the game, else 0 

- • _Every game has only 1 winner_ (auto-correlated data) 

- • Effective sample size is closer to 4,000 (num. games in the last 15 years) 

- • This is nowhere near enough data to experience the full variability of the nonlinear and interacting variables of score diff., time remaining, team quality, yardline, down, distance, timeouts, etc. 

17 

# **WP Simulation** 

- To show you how hard it is to accurately fit WP using just ≈ 4000 games, we created a Random Walk version of football 

- It’s an extremely simple Random Walk but looks just like football! 

- • We can precisely calculate WP at every game-state 

- Then, simulate a historical play-by-play dataset with auto-correlated win/loss response variable 



- <sup>WP point estimates, fit using machine</sup> learning from one simulated dataset of simplified football plays, _get the general trend right_ (are unbiased). 

18 

# **WP Simulation** 

- To show you how hard it is to accurately fit WP using just ≈ 4000 games, we created a Random Walk version of football 

- It’s an extremely simple Random Walk but looks just like football! 

- • We can precisely calculate WP at every game-state 

- Then, simulate a historical play-by-play dataset with auto-correlated win/loss response variable 



- Bootstrapped WP confidence intervals, to achieve 90% coverage of true WP, need to be wide (8% WP on average). 

- • Real football exponentially more complex. Confidence intervals should be far wider. 

19 

- **Quantifying uncertainty of the optimal fourth down decision** 

- • Making fourth down decisions based solely on WP point estimates, which are highly uncertain, leads to overconfident decisions 

- • Quantify uncertainty in the 4th down decision by bootstrapping 

   - the randomized cluster bootstrap accounts for autocorrelation 

   - • **_boot %_** _d_ Go FG Punt — % of bootstrapped models which choose decision ∈{ , , } 



<!-- Start of picture text -->
d Go  FG  Punt<br> ∈{ , , }<br><!-- End of picture text -->

20 

- **Example Plays:** 

- **How Fourth Down Decision Making Changes** 

21 

# **Example 1** 

#### • CHI @ NYJ in Week 12 of 2022 

**FG looks like a strong decision based on the WP point estimate (+2%).** _Traditional analytics recommendation:_ **Field goal attempt.** 





22 

• CHI @ NYJ in Week 12 of 2022 

# **Example 1** 

### **FG looks like a strong decision based on the WP point estimate, but we don’t have enough data to trust our own point estimate.** _Our recommendation:_ **Coach’s discretion.** 

• For _many_ plays the optimal decision is uncertain! 







23 

# **Example 2** 

#### • WAS @ IND in Week 8 of 2022 

- **Punt has a tiny estimated edge over Go (+0.05%).** _Traditional analytics recommendation:_ **Tossup, or slight lean towards punt.** 





24 

# **Example 2** 

#### • WAS @ IND in Week 8 of 2022 

##### **Punt has a tiny estimated edge over Go, but we are confident that the edge is there.** _Our recommendation:_ **Punt (but not a tragedy if the coach overrides).** 

• Eeking out these tiny (but confident) edges are valuable because many more of them occur per game. 







25 

• LV @ LA in Week 14 of 2022 

# **Example 3** 

## **Go is a strong decision based on the WP point estimate (+3.5%).** _Traditional analytics recommendation:_ **Strong Go!** 





26 

# **Example 3** 

#### • LV @ LA in Week 14 of 2022 

##### **Go is a strong decision based on the WP point estimate, and we are certain it is the best decision.** 

- _Our recommendation:_ **Strong Go!** (LV punted, then LA won after a Mayfield 98 yard game winning drive). 







27 

- **Analytics, Have Some Humility** 

- • _must_ 

- Team quality be incorporated into EP/WP models 

- • We need shrinkage to mitigate overfitting in our ML models 

- • **_Humility:_** There are not enough games to fit an accurate statistical WP model to precisely learn the right fourth down decision at many game-states 

- • Far fewer 4th down decisions are as obvious as analysts widely claim **•**<sup>**Thank you!**</sup> 

- • Twitter: **@RyanBrill_** 

- • Email: **ryguy123@sas.upenn.edu** 

28 


