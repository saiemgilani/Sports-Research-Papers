<!-- source: 2023 Analytics have some humility a statistical view of fourth-down decision making - Brill.pdf -->

# Analytics, have some humility: a statistical view of fourth-down decision making 

Ryan S. Brill<sup>*</sup> and Abraham J. Wyner<sup>†</sup> 

November 8, 2023 

##### **Abstract** 

Expected points (EP) and win probability (WP) are value functions fundamental to strategic in-game decision making in American football, particularly for fourth down decision making. The EP and WP functions which are widely used today are statistical models fit from historical data. These models, however, are subject to serious statistical flaws: selection bias, overfitting, ignoring autocorrelation, and ignoring uncertainty quantification. We develop a machine learning framework that accounts for these issues and extracts our analysis into a decision-making inference. Along the way, we introduce a novel methodological approach to mitigate overfitting in machine learning models. Specifically, we extend the catalytic prior, initially developed in the context of linear models, to smooth our tree machine learning models. Our final product is a major advance in fourth-down strategic decision making: far fewer fourth-down decisions are as obvious as analysts claim. 

## **1 Introduction** 

In-game strategic decision making is one of the fundamental objectives of sports analytics. To mathematically compare strategies, analysts need a value function that measures the value of each game-state. The optimal decision maximizes the value of the next game-state. Across sports, however, value functions are not observable quantities; they are defined by models. It is the sports analysts’ task to infer the value of each game-state from the massive dataset of all plays in the recent history of a given sport. 

> *Graduate Group in Applied Mathematics and Computational Science, University of Pennsylvania. Correspondence to: ryguy123@sas.upenn.edu 

> †Dept. of Statistics and Data Science, The Wharton School, University of Pennsylvania 

1 

The two most widely used value functions by analysts of American football are expected points and win probability. _Win probability_ (WP) measures the probability that the team with possession at the current game-state wins the game. _Expected points_ (EP) measures the expected value of the net number of points of the next scoring event in the half given the current game-state.<sup>1</sup> The most prominent example of analysts using these value functions to dictate in-game strategy is fourthdown decision making. On fourth down, a football coach has three choices: go for it (Go), attempt a field goal (FG), or punt the ball (Punt). Initial attempts from Romer (2006) and Burke (2009b) suggest making the decision that maximizes expected points. Modern attempts from Baldwin (2021a) and Burke<sup>2</sup> suggest making the decision that maximizes win probability.<sup>3</sup> These analyses found that NFL coaches are too conservative on fourth down; they often settle for kicks even when they should go for it. 

These value functions arise broadly from one of two classes of models, probabilistic state-space models or statistical models. State-space models simplify the game of football into a series of transitions between game-states. Transition probabilities are estimated from play-level data and are then propagated into WP or EP by simulating games. When done right, these models are a good way to estimate value functions, but they are difficult to do: they require a careful encoding of the convoluted rules of football into a set of states and the actions between those states, careful estimation of transition probabilities, and enough computing power to run enough simulated games to acheive desired granularity. Each of these are nontrivial. 

On the other hand, statistical models are fit entirely from historical data. Given the results of a set of observed football plays, statistical models fit the relationship between certain game-state variables using data-driven regression or machine learning approaches. These models are widely used today in the football analytics community because rich publicly available play-by-play data (e.g., nflFastR (Carl and Baldwin, 2022)) and powerful off-the-shelf machine learning models (e.g., XGBoost (Chen and Guestrin, 2016)) have become widely accessible. Additionally, due to a perceived abundance of data, these machine learning models are viewed as more trustworthy than previous mathematical models that make more simplifying assumptions. For these reasons, we focus on statistical EP and WP models in this paper. 

These statistical models, however, are subject to several serious statistical issues. By not adjusting for team quality, EP models are victims of selection bias.<sup>4</sup> Hence we must adjust for team quality. 

> 1Net points is relative to the team with possession (negative if the opposing team is expected to score more points next). 

> 2Burke’s method is proprietary. 

> 3Burke (Twitter: `@bburkeESPN` ) and Baldwin (Twitter: `@ben` ~~`b`~~ `ot` ~~`b`~~ `aldwin` ) post their fourth down recommendations on Twitter during and after real football games. 

> 4Because good teams have more plays and good teams score more points, EP for randomly drawn teams is different from EP for average teams, _ceteris paribus_ . 

2 

The task is then to fit a complicated function of many variables that interact and have nonlinear relationships. Additive regression models underfit, but blackbox machine learning models like XGBoost aggresively overfit. WP models, moreover, do not account for the auto-correlated nature of football play-by-play data.<sup>5</sup> Although a dataset of 511 _,_ 264 plays from 2006 to 2021 may seem large enough to fit an accurate statistical WP model, it actually is not. In particular, auto-correlation reduces the effective sample size and inflates WP standard errors. This uncertainty should percolate into the fourth-down decision procedure, which currently treats EP and WP as known quantities rather than estimates. 

We address the aformentioned issues with these statistical models. To mitigate selection bias, we create measures of team quality and adjust for them. Including these additional covariates exacerbates overfitting of our machine learning models. To reduce overfitting and smooth these models, we introduce a novel methodological approach: we extend the catalytic prior to our machine learning framework. Initially developed in the context of linear models (Huang et al., 2020, 2022), the catalytic prior involves using synthetic data imputed from a simpler smoother model as a prior for a more complex model with interactions. We find that a catalytic prior from a simpler additive regression model effectively “Laplace smooths” our tree machine learning models. Then, we construct bootstrapped WP confidence intervals which account for auto-correlation, and validate our methods on a simulated random walk version of football in which true win probabilities are known. Finally, we percolate uncertainty estimates through the fourth-down decision procedure using bootstrap voting. Our final product is a major advance in fourth-down strategic decision making: far fewer fourth-down decisions are as obvious as analysts claim. Thus, we ask football analysts to have some _humility_ : for many game-states, there is simply _not enough data_ to know which decision is optimal. 

The remainder of this paper is organized as follows. In Sections 2 and 3, respectively, we discuss statistical EP and WP models, including model specifications, issues, and how we address those issues. In Section 2 we also detail our extension of catalyitc priors to our machine learning context. We discuss our improved fourth down decision procedure in Section 4 and conclude in Section 5. 

## **2 Expected points models** 

The mathematical approach to in-game strategic decision making is to make the decision which maximizes the value of the next game-state. The first value function used for fourth-down decision making in American football (by Romer (2006)) was _expected points_ (EP), the expected value of 

> 5 Concisely, _every game has only one winner_ . The binary win/loss response values are not independent, as all plays from the same game share the exact same draw of the win/loss outcome. 

3 

the net number of points of the next score in the half. In this Section, we discuss statistical expected points models in detail. We begin with an overview of existing open-source expected points models. These models are fit from historical data but don’t adjust for team quality, leading to selection bias. Hence we need to adjust for team quality. This task is not easy: we need to fit expected points as a function of team quality, yardline, down, yards to go, time remaining, timeouts, and more game-state variables. We want to capture the nonlinear and interacting relationships between these variables, but we don’t want to overfit. Moreover, we find that widely used XGBoost EP models overfit even without adjusting for team quality. To mitigate overfitting, we use a catalytic prior to shrink XGBoost towards a simpler smoother model. We find that our catalytic machine learning model indeed performs best. 

### **2.1 Problems with statistical expected points models** 

In Table 1 we summarize well known open-source statistical expected points models. The covariates **x** encode the game-state. There are seven potential outcomes of the next scoring event in the half after the current play, 



Each event has an associated value, the net points scored from the event. Earlier approaches from Romer (2006) and Burke (2009a) treat EP as a regression problem in which the outcome variable is a real number, the net points of the next score. More recent approaches from Yurko et al. (2018) and Baldwin (2021b) treat EP as a classification problem in which the outcome variable is categorical. Given estimated outcome probabilities, the expected points at game-state **x** is given by the weighted sum 



We include detailed specifications of these models in Appendix A.1. 

None of these expected points models adjust for team quality. There are two reasons for this. First, these models are viewed as representing EP for an average offense facing an average defense, and so imply decision making for average teams. For instance, Romer (2006) writes that his EP model represents the “expected long-run value ... of the difference between the points scored by the team with the ball and its opponent when the two teams are evenly matched, average NFL teams.” Also, 

4 

|modeler|model|game-state variables|trainingset|outcome variable|
|---|---|---|---|---|
|Romer(2006)|instrumental<br>variables<br>regression|yardline|all plays|points of<br>the next<br>score (a<br>real number)|
||linear||||
|Burke(2009a)|regression<br>with a<br>spline|yardline|frst down<br>plays|_∧_|
|Yurko et al.(2018)|multinomial<br>logistic<br>regression|transformations of<br>yardline, down,<br>yards to go,<br>time remaining|all plays|outcome<br>of the<br>next score<br>(categorical)|
|||yardline, down,<br>yards to go,|||
|Baldwin(2021b)|XGBoost|time remaining,<br>home, era,<br>roof type,<br>timeouts|all plays|_∧_|



Table 1: Summary of well known open-source statistical expected points models. 

it is not easy to adjust for team quality alongside all the other game-state variables, as they have nonlinear and interacting relationships. 

To illustrate why not adjusting for team quality causes problems, we conduct a thought experiment via three questions. 

   1. What is the probability that an _“average” NFL kicker_ sinks a 70 yard field goal in neutral weather conditions? 

   2. What is the probability that _Justin Tucker_<sup>6</sup> sinks a 70 yard field goal in neutral weather conditions? 

   3. What is the probability that a _randomly drawn kicker_<sup>7</sup> sinks a 70 yard field goal in neutral weather conditions? 

- Justin Tucker made a 66 yard field goal in 2021, the longest field goal in NFL history. Just one 

> 6Justin Tucker is widely considered the best NFL kicker of all time. In Appendix C.3 we show that Tucker has the highest career mean “kicker quality” of all kickers in our dataset. 

> 7Randomly drawn from our dataset of all field goal attempts from 2006 to 2021. 

5 

kicker has made a 64 yard field goal, just 6 kickers have made a 63 yard field goal, and each of these kickers were above average. So, for purposes of this thought experiment, suppose an “average” kicker has 0 probability of sinking a 70 yard field goal. On the other hand, since Justin Tucker is the best kicker in the NFL, suppose he has some _ε >_ 0 probability of sinking a 70 yard field goal. Then a randomly drawn kicker also has a positive probability, since we can randomly draw Justin Tucker. 

This thought experiment highlights the difference between an average player and a randomly drawn player. Expected points models, which don’t adjust for team quality, report EP for randomly drawn teams, not for average teams. This causes problems for several reasons. First, no team wants an EP value for a randomly drawn team, and there is no such thing as a decision made by a random team. The 2022 Philadelphia Eagles have a great offense and want it’s team’s EP. Failing to adjust for team quality also introduces selection bias. Specifically, good teams have more plays and good teams score more points, which we visualize in Figure 1. As a result, expected points for a team from a randomly drawn play from our historical dataset is not the same as expected points for an average team, all else equal. So, these statistical EP models are biased, and a better model should adjust for team quality.<sup>8</sup> 





Figure 1: Good teams have more plays (a) and good teams score more points (b) conditional on being near the opposing team’s endzone. Specifically, on the left: a higher proportion of plays feature good teams (large negative point spreads) than bad teams (large positive point spreads). On the right: the average empirical net points of the next score is higher for good teams. 

These expected points models also don’t adjust for score differential, leading to further bias, which 

> 8Today, some proprietary expected points models do adjust for team quality. For instance, Burke’s EP model at ESPN accounts for team strength using FPI (football power index). 

6 

we discuss in detail in Appendix A.3. To mitigate selection bias and score differential bias, we include score differential and measures of offensive and defensive quality as covariates. Point spread is the easiest way to adjust for the difference in strength between the offensive and defensive teams. Additionally, in Appendix A.4, we create our own measures of offensive and defensive quality which leverage information from each of a team’s previous plays while carefully controlling for data bleed. 

An interesting football lesson that arises from modeling EP using our own team quality metrics is that offensive quality is more predictive of points than defensive quality (see Appendix A.5). Further, using a modified version of the knockoffs procedure from Candes et al. (2016) and Ren et al. (2020) to fit the autocorrelated nature of our football play-by-play dataset, we find that each of the offensive quality metrics and none of the defensive quality metrics are significant (see Appendix A.6). In other words, our defensive quality metrics are not significantly distinguishable from noise in predicting the points of the next score. This provides further evidence that offense matters more than defense for scoring points. 

Back to the task at hand, we want to fit an EP model as a function of many parameters – yardline, yards to go, time remaining, team quality, score differential, etc. – replete with nonlinear relationships and interactions. We want to fit a flexible enough model to capture a sufficiently complex relationship, but we don’t want to overfit. An additive model like multinomial logistic regression underfits and lack interactions. For example, expected points via multinomial logistic regression doesn’t capture the right trajectory of EP at the end of the half.<sup>9</sup> A flexible machine learning model like XGBoost has the capacity to fit such a complicated function given enough data, but in practice we find that it overfits. For example, expected points via XGBoost classification isn’t monotonic in certain variables such as yardline even though it should be.<sup>10</sup> Whereas expected points via XGBoost regression is monotonic in these variables, XGBoost regression also has trouble fitting EP at the end of each half.<sup>11</sup> We visualize the underfitting and overfitting of these models in Figure 2. We find further evidence that XGBoost overfits in its relatively poor out-of-sample predictive performance in our EP model comparison (Section 2.3). 

> 9At the end of the half, EP should converge to 0 far from the opponent’s endzone (large yardlines). EP from multinomial logistic regression wrongly converges to a positive number (Figure 2a), whereas EP from XGBoost classification correctly converges to 0 (Figure 2c). 

> 10EP should be increasing in yardline even though it isn’t as shown in Figure 2d (yardlines 92-94). We can’t use monotonicty constraints in XGBoost classification because the probability that the next score is a field goal, for instance, is not monotonic in yardline. 

> 11We can leverage monotonicity constraints in XGBoost regression because expected points itself is monotonic in yardline. But, in Figure 2b we see that EP via XGBoost regression, like that from multinomial logistic regression, doesn’t converge to 0 at the end of the half. XGBoost classification fits EP at the end of the half better than XGBoost regression because it explicity fits the probability that there is no next score in the half, which increases as time remaining decreases. 

7 









Figure 2: Predicted EP vs. yardline for various values of half seconds remaining according to multinomial logistic regression (Figure (a)), XGBoost regression (Figure (b)), and XGBoost classification (Figure (c)), holding other variables constant. According to multinomial logistic regression and XGBoost regression, EP<sup>�</sup> doesn’t converge to 0 far from the oponent’s endzone at the end of the half, which is wrong. Although EP<sup>�</sup> correctly converges to 0 far from the oponent’s endzone at the end of the half according to XGBoost classification, it is not monotonic in yardline (Figure (d), yardlines 92-94). 

### **2.2 Catalytic prior to mitigate overfitting** 

We want to use machine learning to capture a complex high-dimensional function, but flexible machine learning models like XGBoost tend to aggresively overfit football play-by-play data. The statistics community typically deals with overfitting using regularization or shrinkage towards simpler models. These methods are well known for parametric models in a Bayesian context, but are much more difficult in the context of blackbox machine learning. Burke aptly summarized this problem on the September 19, 2023 episode of the Wharton Moneyball podcast,<sup>12</sup> 

> 12 `https://businessradio.wharton.upenn.edu/wharton-moneyball/` 

8 

“The in-game models are not Bayesian. Congratulations to you if you can figure out how to do that. Most publicly available models are ... XGBoost models.” 

To mitigate the overfitting of machine learning EP models, we extend the idea of a catalytic prior from Huang et al. (2020, 2022) to shrink a complex XGBoost classification model towards a simpler multinomial regression model. The idea is to generate synthetic prior data from a simpler model, the _catalytic prior_ model, and then use this synthetic data to represent the prior distribution. The catalytic prior serves as a prior on functions or models, and the goal is to “pull” the complex target model towards the simpler model in order to reduce overfitting. This process is catalytic in that a catalyst in chemistry stimulates a reaction to take place. Here, the reaction is fitting our model. Although catalytic priors were introduced in the context of linear models (Huang et al., 2020, 2022), we are the first, to our knowledge, to use catalytic priors in a machine learning context. 



Figure 3: The catalytic prior modeling process from Huang et al. (2022). 

We visualize the catalytic modeling process in Figure 3. In our context of expected points models for American football, the catalytic modeling process begins with fitting a catalytic prior model (e.g., a multinomial logistic regression model) to observed data. The observed data ( **X** _,_ **y** ) consists of real football plays, where **X** encodes game-states and **y** encodes the response (either the outcome or points of the next score). Next, we generate fake football plays ( **X** _∗,_ **y** _∗_ ). Specifically, we generate a matrix **X** _∗_ of synthetic game-states by sampling with replacement from each column of **X** and jittering the continuous-valued variables using Gaussian noise. Then, for each synthetic game-state in **X** _∗_ we generate a synthetic response variable using our fitted catalytic prior model, yielding synthetic reponse vector **y** _∗_ . Next, we combine the observed football plays with the synthetic football plays, potentially downweighting the synthetic plays since they are fake. Finally, we fit a more complicated model (e.g., a XGBoost model) on this combined dataset ( _{_ **X** _,_ **X** _∗}, {_ **y** _,_ **y** _∗}_ ). 

More specifically, to fit a catalytic XGBoost classification model, we use a multinomial logistic regression catalytic prior model to generate fake outcomes of the next score. The number of synthetic datapoints and the weight of each synethic datapoint are treated as hyperparameters in 

9 

the XGBoost tuning process. On the other hand, to fit a catalytic XGBoost regression model, we use a linear regression or multinomial logistic regression catalytic prior model to generate a vector of synthetic expected points numbers. We use fake _expected_ points of the next score, rather than fake points of the next score in _{_ 7 _,_ 3 _,_ 2 _,_ 0 _, −_ 2 _, −_ 3 _, −_ 7 _}_ , because it allows the complex target model to digest the information of the simpler prior model using fewer synthetic datapoints. 

### **2.3 Model comparison** 

Now, we compare the out-of-sample predictive performance of various EP models. We use data from from nflFastR, an R package created to efficiently scrape NFL play-by-play data going back to 1999 (Carl and Baldwin, 2022), to train and test our models. 

We begin with a dataset of 511 _,_ 264 non-special teams football plays (and 216 _,_ 149 first down plays) from 2006 to 2021. We use an alternative data truncation to Burke’s that removes garbage time plays but keeps plays in the second and fourth quarters, allowing us to model EP as a function of score differential and time remaining.<sup>13</sup> This yields a dataset 346 _,_ 400 plays (and 146 _,_ 845 first down plays). Our dataset is clustered into _epochs_ , groups of plays which share the same outcome of the next score. To keep the clustered nature of our dataset intact and to avoid data bleed, we split our dataset in half by randomly sampling 50% of all epochs. The first down plays from the first 50% of these epochs form the hold-out test set. We test on first down plays because fourthdown decision making relies on the value of having a first down (see Appendix C.1 for details). The plays from the other 50% of these epochs form the training set. To tune XGBoost models, we again split the training set in half, preserving the epoch correlation structure, to form a hyperparameter validation set and a training set. We then tune our XGBoost models in a similar fashion as in Baldwin (2021a).<sup>14</sup> 

We visualize the results of our model comparison in Table 2. In Appendix A.1 we include detailed specifications of the well known statistical EP models and in Appendix A.2 we we include detailed specifications of the remaining models.<sup>15</sup> We denote the best version of XGBoost classification (resp., multinomial logistic regression) we could find by Baldwin+ (resp., Yurko+). The best catalytic machine learning model uses Baldwin+ as the complex target model and Yurko+ as the catalytic prior. We use _M_ = 3 million synthetic outcomes generated from the catalytic prior. Only _MU_ = 100 of thse synthetic outcomes come from under _U_ = 30 half seconds remaining; we shrink less at the end of each half because XGBoost is better than MLR at the end of each half. 

> 13 Details of our data truncation and Burke’s data truncation are included in Appendix A.3. 

> 14We don’t use the cross validation default in the XGBoost R package to tune XGBoost models because it doesn’t preserve the epoch correlation structure. 

> 15Note that we fit Yurko et al. and Baldwin’s models without their row weighting procedure in order to judge the underlying structure of their models. See Appendix A.3 for more details. 

10 

We tune the catalytic hyperparameters ( _M, MU ,U_ ) in a similar manner as the standard XGBoost hyperparameters. 

|model|model|team|out-of-sample|
|---|---|---|---|
|name|type|quality|MAE|
|Catalytic|Catalytic|point spread|3.744|
|Yurko+|Multinomial logistic regression|point spread|3.749|
|Baldwin+|XGBoostclassifcation|point spread|3.753|
||XGBoostregression|point spread|3.757|
||Multinomial logistic regression|ours<sup>16</sup>|3.768|
|Baldwin(2021b)|XGBoostclassifcation|none|3.803|
|Yurko et al.(2018)|Multinomial logistic regression|none|3.808|
|Burke(2009a)|Linear regression|none|3.833|
|Romer (2006)|Instrumental variables regression|none|3.864|



Table 2: Predictive performance of various EP models. 

Romer and Burke’s methods perform worst because they are univariate functions of yardline. Romer’s method performs worse than Burke’s because it averages across all downs, whereas Burke’s is fit on just first downs. Yurko et al. and Baldwin’s models perform better because they adjust for other confounders. The models which adjust for team quality significantly outperform those that don’t. Models which adjust for team quality using point spread outperform those which use our hand-crafted measures because point spread is more up-to-date (e.g., it accounts for injury information). XGBoost classification outperforms XGBoost regression because leveraging the knowledge that there are seven potential outcomes of the next score yields a better EP model near the end of each half. That the best multinomial logistic regression model we could find outperforms the best XGBoost model we could find provides evidence that XGBoost overfits the data. Finally, the catalytic model, which shrinks the complex XGBoost model towards the simpler multinomial logistic regression model, performs best. This validates our hypothesis that expected points models fit using XGBoost need to be regularized or shrunk to create a better model subject to less overfitting. 

## **3 Win probability models** 

Romer (2006) uses expected points as the basis of fourth-down decision making, but it is the wrong objective function. A team’s goal is to win the game, not score more points on average, so _win probability_ (WP) is the right objective function.<sup>17</sup> In Figure 4 we visualize an example 

> 16See Appendix A.4 for details of our 8 measures of offensive and defensive quality. 

> 17Expected points is only the first moment of win probability, which is a combination of the expected value and the variance of the points of the next score. 

11 

play in which the decision which maximizes expected points is clearly suboptimal. Even though attempting a field goal produces more points over average, scoring just 3 points when down by 6 at the end of the game all but guarantees a loss. 



Figure 4: An example of EP-based fourth-down decision making which shows that EP is the wrong objective function. Kicking a field goal yields more points on average, but the offense is down by 6 points with 1 minute to go, so it needs to go for a touchdown. 

Hence in this Section we discuss statistical win probability models, which form the basis of the fourth-down decision procedure used today. These models, however, are fit from highly autocorrelated observational football data, so they produce highly uncertain win probability estimates. To understand just how difficult it is to accurately fit a win probability model from historical data, we conduct a simulation study using a simplified random walk version of football in which the true win probabilities are known. Although statistical win probability models find the general trend of true win probability (i.e., they are unbiased), they are subject to substantial uncertainty (to obtain good coverage, WP confidence intervals need to be substantially wide). 

### **3.1 Problems with statistical win probability models** 

Statistical win probability models are fit from historical play-by-play data in a manner similar to expected points models. As before, the covariates **x** encode the game-state. The game-state for WP models includes pre-game point spread and score differential, so WP isn’t as biased as EP. The binary outcome variable _y_ is 1 if the team with possession wins the game, else 0. In Table 3 we provide a summary of well known open-source win probability models. We include detailed specifications of these models in Appendix B.1. Further, in Appendix B.3, we conduct a model selection. A catalytic WP model, where XGBoost is the complex target model and a GAM is the catalytic prior, outperforms other models. 

Football analysts see a dataset of 511 _,_ 264 plays from 2006 to 2021 and think this is enough data to fit accurate statistical WP models. This is not true because the binary win/loss response variable is noisy and highly auto-correlated: _every game has only one winner_ . Formally, the binary response 

12 

|modeler|model|game-state variables|trainingset|outcome variable|
|---|---|---|---|---|
|Yurko et al.(2018)|GAM|transformations of<br>score differential,<br>time remaining,<br>timeouts remaining,<br>expected points|all plays|binary win/loss|
|||transformations of<br>score differential,|||
|Baldwin(2021a)|XGBoost|time remaining,<br>timeouts remaining,<br>yardline, down, yards to go,<br>home,receive 2<sup>_nd_ </sup>half kickoff|all plays|binary win/loss|



Table 3: Summary of well known open-source statistical win probability models. 

variable _yi_ of the _i_<sup>_th_</sup> play indicates whether the team with possession won the game.<sup>18</sup> The reponse values are not independent, as all plays from the same game share the _same draw_ of the response column. Thus the effective sample size is somewhere between the number of plays (511 _,_ 264) and the number of non-tied games (4 _,_ 101) from 2006 to 2021.<sup>19</sup> This is not enough data to experience the full variability of the nonlinear and interacting variables of score differential, time remaining, point spread, yardline, yards to go, timeouts, etc. In fitting win probability models, we are in a limited-data context, and as such we expect wide confidence intervals for WP point estimates. 

### **3.2 Simulation study: random walk football** 

To illustrate just how difficult it is to accurately fit a statistical win probability model from highly auto-correlated observational data, we conduct a simulation study. Specifically, we create a simplified random walk version of football in which the true win probability at each game-state is known. Then, we see how well statistical WP models recover the true win probability. These models find the general WP trend: they are unbiased, with a mean absolute error of less than 2% WP. But, they are subject to substantial uncertainty: to obtain 90% coverage, bootstrapped WP confidence intervals have a substantially wide average width of 8% WP. As real football is exponentially more complex, its confidence intervals should be far wider. 

**Rules of random walk football.** Random walk football begins at midfield. Each play, the ball 

> 18The response variable for fitting EP models from observational data is also auto-correlated, as plays are clustered into _epochs_ (plays which share the same next score outcome). But our dataset contains 47 _,_ 874 epochs and we find that auto-correlation impacts EP models significantly less than it affects WP models. 

> 19The effective sample size is larger for plays closer to the end of the game in that uncertainty in win probability and the fourth-down decision diminishes towards the end of the game (see Section 4 for details). 

13 

moves left or right by one yardline with equal probability. If the ball reaches the left (right) end _−_ of the field, team one (two) scores a touchdown, worth +1 ( 1) point. The ball resets to midfield after each touchdown. After _N_ plays, the game ends. If the game is still tied after _N_ plays, a fair coin is flipped to determine the winner. We include the formal mathematical specification of the game in Appendix B.4. We also explicitly compute true win probability as a function of time, field position, and score differential using dynamic programming in Appendix B.4. 

**Simulation methodology.** _M_ = 25 times, we simulate _G_ games, each with _N_ plays per game. We use _L_ = 4 yardlines so that the average number of first down plays between each score is similar to that of a real football game. This yields _M_ simulated datasets of simplified football plays, each of the form 



For each play of game _g_ we record the timestep _n_ , the field position _Xgn_ , the score differential _Sgn_ , and a binary variable _ygn_ indicating whether the team with possession wins the game. The response variable _y_ is auto-correlated, as each play within the same game shares the same random draw of _y_ . 

On each simulated dataset, we use machine learning to estimate win probability as a function of timestep _n_ , field position _x_ , and score differential _s_ , 



We then compute the mean absolute error between the true and estimated win probabilities averaged over the _M_ simulations. We also compare the coverage and lengths of the WP confidence intervals produced by various bootstraps, discussed below, averaged over the _M_ simulations. 

**Bootstrap confidence interval methodology.** We compare the coverage and lengths of WP confidence intervals produced by the standard bootstrap, cluster bootstrap, and randomized cluster bootstrap, averaged over the _M_ simulations. In the standard bootstrap, which assumes each row (play) of the dataset is independently drawn, each of _B_ bootstrapped datasets are formed by resampling _N_ plays with replacement. In the cluster bootstrap, each of _B_ bootstrapped datasets are formed by resampling _G_<sup>_′_</sup> games with replacement, keeping each observed row within each resampled game. Finally, in the randomized cluster bootstrap, each of _B_ bootstrapped datasets are formed by resampling _G_<sup>_′_</sup> games with replacement, and within each game resampling plays with replacement. To acheive better coverage, we re-sample half as many games as in the original dataset, _G_<sup>_′_</sup> = _G/_ 2. Then, for each bootstrap method, we fit a WP model WP _b_ to each bootstrapped dataset _b_ . The confidence interval for the WP estimate at game-state **x** is defined by the 2 _._ 5<sup>_th_</sup> and 97 _._ 5<sup>_th_</sup> quantiles of _{_ WP1( **x** ) _,...,_ WP _B_ ( **x** ) _}._ As we want our WP confidence intervals to be quickly 

14 

evaluable for fourth-down decision making, we use _B_ = 26.<sup>20</sup> 

**Simulation results.** We report the results of our simulation study in Table 4. For the first row, each simulated dataset consists of _G_ = 4 _,_ 101 games and _N_ = 53 plays per game, which matches the number of games and the average number of first down plays in our dataset of real football plays. Each game in each of these datasets consists of _K_ = 53 auto-correlated plays per game. For the second row, each simulated dataset consists of _G_ = 4 _,_ 101 _·_ 53 games and _N_ = 53 plays per game. Then, we remove all but _K_ = 1 play per game so that each timestep _n_ has exactly 4 _,_ 101 corresponding i.i.d. rows. In other words, those datasets consist of 217 _,_ 353 plays with an i.i.d. response column. 

|G|N|K|MAE bt<br>WPand <sup>�</sup><br>WP|CI<br>covg.<br>SB|CI<br>covg.<br>CB|CI<br>covg.<br>RCB|CI<br>length<br>SB|CI<br>length<br>CB|CI<br>length<br>RCB|
|---|---|---|---|---|---|---|---|---|---|
|4_,_101|53|53|0.0179|0.73|0.85|**0.90**|0.048|0.067|**0.079**|
|4_,_101_·_53|53|1|0.0164|0.78|0.78|0.78|0.049|0.049|0.049|



Table 4: Simulation study results. SB means standard bootstrap, CB means cluster bootstrap, and RCB means randomized cluster bootstrap. 

In the simulation study with auto-correlation ( _K_ = 53), the mean absolute error (MAE) between the true and estimated WP is less than 2% over average. Also, the MAE is smaller than about 3 _._ 5% WP across all values of true win probability (see Figure 15a of Appendix B.4). So, XGBoost recovers the general trend of true WP, which we visualize in Figure 5a. In the simulation study without auto-correlation ( _K_ = 1), the MAE is similar but slightly smaller. This suggests that much of the bias induced by fitting WP from observational data is the result of having limited data and a noisy binary response column, not from auto-correlation. 

The length and coverage of WP confidence intervals, on the other hand, are significantly impacted by auto-correlation. In the simulation study with auto-correlation ( _K_ = 53), the standard bootstrap, which ignores auto-correlation, produces confidence intervals which are too narrow at an average width of about 5% WP, leading to a subpar 73% coverage. The cluster bootstrap produces wider confidence intervals at an average width of about 7% WP, leading to a higher 85% coverage. The randomized cluster bootstrap produces even wider confidence intervals at an average width of about 8% WP, leading to a satisfactory frequentist coverage of 90% over average. In other words, to achieve satisfactory coverage, WP confidence intervals need to be substantially wide, which we visualize in Figure 5b. 

Coverage is similar across all values of true win probability except near 0 and 1 (see Figure 15b 

> 20Specifically, we use the original dataset together with 25 bootstrapped datasets, forming 26 total datasets. 

15 





Figure 5: On the left: WP estimates (dotted line) get the general trend right. On the right: bootstrapped WP confidence intervals need to be substantially wide to acheive good coverage. In both figures: true WP is given by the solid line, and we display the results from one simulation and at yardline _x_ = 3. 

of Appendix B.4). To increase coverage at the extremes, we widen our confidence intervals when � WP _<_ 0 _._ 025 to have a lower bound of 0 and when WP<sup>�</sup> _>_ 0 _._ 975 to have an upper bound of 1. Also, average confidence interval length from the randomized cluster bootstrap is at most 12% for some values of true WP, and C.I. length decreases as true WP moves towards the extremes (see Figure 15c of Appendix B.4). 

In the simulation study without auto-correlation ( _K_ = 1), each bootstrap method is identical and yields an average confidence interval length of about 5% WP (similar to the average C.I. length from the standard bootstrap on auto-correlated data). The frequentist coverage is 78%; to increase coverage we could widen the confidence intervals by resampling fewer than _N_ plays per game in the standard bootstrap. 

## **4 Fourth-down decision making** 

Current popular fourth-down decision procedures involve making the decision d _∈{_ Go _,_ FG _,_ Punt _}_ which maximizes estimated win probability.<sup>21</sup> These existing decision procedures, based solely on effect size, ignore the uncertainty inherent in estimating win probability from highly autocorrelated historical data. Thus, in this Section, we modify the decision procedure to account for uncertainty. We find that decision making changes substantially. In particular, far fewer fourth- 

21In Appendix C.1 we detail how we estimate win probability if a team goes for it, attempts a field goal, or punts as a function of win probability if a team has possession and a first down at a certain game-state. 

16 

down decision are as obvious as analysts claim. 

### **4.1 Uncertainty in the estimated optimal decision** 

We use bootstrapping to incorporate uncertainty quantification into the fourth-down decision procedure. We use the same bootstrapping structure from the simulation study from Section 3.2 since it acheived adequate coverage. Specifically, we use a randomized cluster bootstrap to create _B_ bootstrapped datasets. Each bootstrapped dataset arises from resampling games with replacement and then within each game resampling plays with replacement. We use just _B_ = 26 bootstrapped datasets, a fairly small number for bootstrapping, because we want to be able to quickly evaluate decision uncertainty during a football game.<sup>22</sup> 

Then, to each bootstrapped dataset, we fit a win probability model using catalytic XGBoost.<sup>23</sup> Each bootstrapped model produces an estimated optimal decision, the decision which maximizes estimated win probability. To quantify uncertainty of this estimate, we use _bootstrap percentage_ , the percentage of bootstrapped models which report decision d as optimal. If most of the bootstrapped models say d is optimal, we are more confident in the point estimate of the optimal decision. If the bootstrapped models are split across multiple decisions, we cannot rely on our point estimate. 

Bootstrap percentage is a measure of _data reliability_ . At each game-state the model produces a point estimate of the fourth-down decision; bootstrap percentage tells us how reliable this estimate is, or how much the data trusts its own estimate. To understand, think of the outcome (winning team) of each row (play) in the dataset as a random draw. If some of these draws resulted in different outcomes, our fitted win probability functions would be different. The less data we have access to, the more sensitive models are to the random idiosyncrasies of any particular training dataset. The bootstrap quantifies this sensitivity: given the amount of data we have, it quantifies the spectrum of variability in potential resulting fitted models. Specifically, it measures: given the amount of data we have, in what proportion of draws of the training set would d be the optimal decision according to win probability point estimates? 

Bootstrap percentage is the right way to bring uncertainty into the decision procedure because it quantifies uncertainty of the _decision itself_ (Friedman et al., 1999). This is distinct from uncertainty in the win probability estimates of each individual decision (Go, FG, or Punt) because these individual estimates are correlated across different draws of the training dataset. For example, across different draws of the training set, for some game-states Go is always better than FG 

> 22Note that in each of the _B_ = 26 bootstrapped datasets we sample with replacement half as many games as in the original observed dataset. We validated this approach in the simulation study from Section 3.2. 

> 23In Appendix B.3 we conduct a WP model selection. Our catalytic WP model, where XGBoost is the complex target model and a GAM is the catalytic prior, outperforms other models. 

17 

even though individual WP estimates are highly variable. Another measure of decision confidence which accounts for this correlation is the bootstrapped confidence interval<sup>24</sup> of the win probability _gain_ of a decision (e.g., the _difference_ in WP between Go and FG). 

### **4.2 How fourth-down decision making changes** 

When we account for uncertainty in win probability estimates, fourth-down decision making changes substantially. We illustrate this using example plays. 

**Example play 1.** First we compare Baldwin’s fourth-down decision making procedure to ours. Baldwin suggests making the decision which maximizes estimated win probability. Further, he measures the strength of a decision by the estimated gain in win probability by making that decision. Figures 6a and 6b illustrate Baldwin’s decision making<sup>25</sup> for a play from the 2023 AFC Championship game. Baldwin views Go as a “strong” decision because he estimates that going for it provides a 3 _._ 8% gain in win probability over attempting a field goal. In Figure 6c we add uncertainty quantification to Baldwin’s decision making. Although our point estimate (the blue column) suggests that Go provides a 1 _._ 5% gain in win probability over FG, our confidence interval [ _−_ 3 _._ 7% _,_ 4 _._ 5%] suggests that Go could either be a terrible or a great decision. There is not enough data to estimate win probability with enough granularity to know which decision is best. Further, about half of the boostrapped models say Go is better than FG (the orange column), reflecting considerable uncertainty in the optimal fourth-down decision. 

**Example play 2.** Next we compare Burke’s fourth-down decision making procedure to ours. Burke, whose win probability model is proprietary, also suggests making the decision which maxizimes estimated win probability. Figure 7a illustrates Burke’s fourth-down decision boundary chart<sup>26</sup> for a play from the 2023 NFC Championship game. The chart visualizes the estimated optimal decision (color) as a function of yardline ( _x_ -axis) and yards to go ( _y_ -axis), holding the other game-state variables constant. Burke views Go as the right decision because the yellow dot (representing the actual play’s yardline and yards to go) lies squarely in the red region and is far from the decision boundary. The chart, however, says nothing about the estimated strength of making the optimal decision or about uncertainty quantification. Hence in Figure 7b we show our version of Burke’s chart<sup>27</sup> which uses color intensity to visualize the estimated gain in win probability by making a decision (darker colors indicate larger values). The pink dot (representing the actual 

> 24This confidence interval is the 2 _._ 5 _th_ and 97 _._ 5 _th_ quantiles of the estimated gain in win probability across all the bootstrapped samples. 

> 25These figures were taken from Baldwin’s fourth down Twitter bot `@ben` ~~`b`~~ `ot` ~~`b`~~ `aldwin` . 

> 26This figure was taken from Burke’s Twitter `@bburkeESPN` . 

> 27We use green for Go, yellow for FG, and red for Punt because we liked Burke’s Twitter thought that fourth-down decision making is like a traffic light. 

18 







Figure 6: For example play 1, Figures (a) and (b) illustrate Baldwin’s decision making and Figure (c) shows our decision making. 

play’s yardline and yards to go) lies in a light green region, indicating a smaller estimated gain in win probability by going for it. Being far from the decision boundary, however, does not imply it the best decision with certainty. Hence in Figure 7c we provide an additional chart which illustrates uncertainty in the estimated optimal decision. Here, the color intensity indicates the proportion of bootstrapped models which make the estimated optimal decision. Aside from some darker patches in the lower left and upper right, most of the figure features lighter colors, indicating high uncertainty. For these game-states, including the actual play, we don’t have enough data to know which decision is best. 

### **4.3 Our improved fourth-down decision procedure** 

By accounting for uncertainty in win probability estimates, our fourth-down decision making procedure recognizes when we don’t know the best decision. We illustrate our improved decision procedure through more example plays. 

**Example play 3.** In Figure 8 we visualize our decision procedure<sup>28</sup> for a fourth-down play in 

28To compare our decision making procedure to the decisions that actual football coaches tend to make, we model the probability that a coach chooses a decision in _{_ Go _,_ FG _,_ Punt _}_ as a function of game-state. We discuss this _baseline coach model_ in detail in Appendix C.5 and include the model’s predictions in our decision figures. 

19 







Figure 7: For example play 2, Figure (a) illustrates Burke’s decision making and Figures (b) and (c) show our decision making. 

which the Bears had the ball against the Jets in Week 12 of 2022. FG provides a solid edge over Go according to the WP point estimate (+2 _._ 1% WP). But our confidence interval of the estimated gain in win probability by attempting a field goal is [ _−_ 3 _._ 7% _,_ 4 _._ 4%], indicating that FG could either be a great or a terrible decision. Also, about half of our bootstrapped models say Go is better. In other words, we do not have enough data to be confident in our win probability point estimates, and we don’t know the optimal fourth-down decision at this game-state. So, we recommend leaving the fourth-down decision to the coach’s discretion. Further, in the bottom right plot, notice how most of the colors are light. This indicates that the optimal decision is uncertain at most other combinations of yardline and yards to go at this game-state. 

**Example play 4.** In Figure 9 we visualize our decision procedure for a fourth-down play in which the Commanders had the ball against the Colts in Week 8 of 2022. Punt provides a slight edge over Go according to the WP point estimate (+0 _._ 5% WP). But, nearly all of the bootstrapped models say Punt is better and our confidence interval of the estimated gain in win probability by punting is [0% _,_ 4 _._ 8%], which is positive. So, even if the edge is small, we are confident in this edge and recommend that the Commanders should Punt. Further, in the bottom right plot, notice how most of the colors are dark outside of a large white boundary region. This indicates that we have higher certainty in our estimated optimal decision at this game-state. 

**Example play 5.** In Figure 10 we visualize our decision procedure for an infamous fourth-down play in which the Raiders had the ball against the Rams in Week 14 of 2022. Go provides a strong edge over Punt according to the WP point estimate (+3 _._ 5% WP). Further, 100% of the bootstrapped models say Go is better and our confidence interval of the estimated gain in win probability by going for it is [0 _._ 30% _,_ 5 _._ 23%], which is strictly positive. Thus, we are confident in 

20 







Figure 8: Our decision making for example play 3. 







Figure 9: Our decision making for example play 4. 

this edge, and we strongly recommend that the Raiders should Go.<sup>29</sup> 

> 29In real life, the Raiders punted. Then, Rams quarterback Baker Mayfield countered with a successful 98 yard drive to win the game. 

21 







Figure 10: Our decision making for example play 5. 

### **4.4 Analytics, have some humility** 

The practical football lesson arising from our new decision procedure is that far fewer fourthdown decisions are as obvious as analysts claim. In Figure 11 we quantify the extent to which fourth-down decisions are less obvious than before. We define a decision as “obvious” according to our decision procedure if the percentage of bootstrapped models making that decision is above, say, 85%. We define a decision as “obvious” according to the previous decision procedure if the estimated gain in WP by making that decision is above, say, 0 _._ 015. We call non-obvious decisions “nebulous.” Of the 1 _,_ 968 fourth-down decisions from 2018-2022 that were previously considered obvious, we consider 8 _,_ 139 (24%) to be nebulous. There is an asymmetry: 32% of previously obvious Go decisions are nebulous and 19% of previously obvious kicks are nebulous. This reflects substantial overconfidence in WP point estimates. 

Thus, we ask football analysts to have some _humility_ : for many game-states there is simply _not enough data_ to use statistical win probability point estimates to make fourth-down decisions. In these cases of high uncertainty, regardless of the point estimate it is arrogant for analysts to recommend decisions to play calling experts and coaches. These experts spend a significant amount of time with their players and have access to information which doesn’t show up in the data. For instance, Eagles coach Nick Sirianni may notice that his usually dominant offensive line is missing a key player today, which does not currently appear in the data. When the estimated optimal fourthdown decision has too much uncertainty, we suggest leaving the decision to the coach’s discretion. Similarly, a football analyst should evaluate a coach’s fourth-down decision making only on plays 

22 



Figure 11: Quantifying the extent to which fourth-down decisions are less obvious than before using all fourth-down plays from 2018-2022. 

where uncertainty is low. 

Although football analysts have been overconfident in their point estimates, the football analytics community was largely correct that NFL coaches do not go for it enough on fourth down. Across all fourth-down plays from 2018-2022 that we consider obvious, the coach made the right decision for 91% plays where he should have kicked but just 55% of plays where he should have gone for it. Play calling in the NFL is still far too conservative: coaches consistently make wrong decisions, particularly when they should go for it. 

## **5 Discussion** 

In-game strategic decision making in sports, and in particular the fourth-down decision problem in American football, is a classic example of a rich applied statistics problem. Statistical expected points and win probability models fit from historical data form the backbone of the decision procedure: make the decision which maximizes the value of the next game-state. In developing these models, however, we encounter a series of complex statistical notions. By not adjusting for team quality, well known open-source statistical EP models suffer from selection bias.<sup>30</sup> Adding additional covariates to adjust for this exacrbates overfitting. Open-source statistical WP models, moreover, don’t account for the auto-correlated nature of play-by-play football data. These issues are not just unique to our specific data problem, but appear in applied statistics problems across 

> 30Today, some proprietary expected points models do adjust for team quality (e.g., Burke’s EP model at ESPN accounts for team strength using FPI (football power index)). 

23 

#### many domains.<sup>31</sup> 

In this paper we discussed these issues in detail and devised ways to mitigate them. To adjust for selection bias, we created and included measures of team quality as covariates. To reduce overfitting and smooth XGBoost, we extended the catalytic prior to our machine learning framework. To quantify uncertainty in win probability models, and thus in the fourth-down decision itself, we used a version of the bootstrap which accounts for auto-correlation and is tuned on a simplified random walk version of football. 

Our main contribution to the statistics community is our extension of the catalytic prior, initially developed in the context of linear models (Huang et al., 2020, 2022), to a machine learning context. We found that the catalytic prior, which used synthetic data imputed from a simpler smoother model as a prior for a more complex model with interactions, effectively smoothed our tree machine learning models. Our other contribution to the statistics community is our framing of this paper as an exemplary case study of how to conduct a real-world data analysis. We take the reader through formulating a problem, dissecting a classic, massive, rich dataset, identifying and facing a series of complex statistical obstacles (including selection bias, overfitting, and auto-correlation), incorporating uncertainty quantification, and synthesizing our analysis into a final decision making inference. 

Our contribution to the football analytics community is a major advance in fourth-down strategic decision making. We devised a better expected points model, as well as quantified uncertainty in win probability and in the fourth-down decision itself. The practical football lesson arising from our new decision procedure is that far fewer fourth-down decisions are as obvious as analysts claim. In particular, for a huge proportion of game-states, there is too much uncertainty in the estimated optimal decision. Thus, we ask football analysts to have some humility: there is simply not enough data to use statistical win probability point estimates to make fourth-down decisions in many cases. For game-states in which uncertainty is high, we suggest leaving the decision to the coach, an on-field expert who has access to information that doesn’t show up in the data. Nonetheless, NFL coaches still skew too conservatively: they still don’t go for it enough on fourth down even when it is mathematically obvious. 

Although our analysis improves the state of the art, it is not without limitations. Even though the randomized cluster bootstrap produces substantially wide confidence intervals for win probability estimates, it underestimates uncertainty because it quantifies sampling uncertainty<sup>32</sup> but not model 

> 31For instance, auto-correlation appears in climate statistics (e.g., McShane and Wyner (2011)) and finance (e.g., Yang et al. (2013)), selection bias arises in epidemiology (e.g., Tripepi et al. (2010); Hern´an et al. (2004)), and overfitting is prevalent throughout the literature (e.g., Peng and Nagata (2020); Subramanian and Simon (2013)). 

> 32Uncertainty in our point estimates resulting from fitting a model on a finite dataset, also known as “variance.” 

24 

uncertainty.<sup>33</sup> In our simulation study from Section 3.2, there is no model uncertainty because we know true win probability is indeed a function of time, score differential, and field position. Win probability in real football, however, is highly likely a function of unobserved confounders. For example, how well Tom Brady slept the previous night could affect his team’s win probability. Additionally, our analysis doesn’t capture uncertainty in the conversion probability model, field goal probability model, and expected next yardline after punting model. These models are fit from thousands of play-level i.i.d. observations, and so are subject to little sampling uncertainty, but are subject to nontrivial model uncertainty as they make simplifying assumptions. Conversion probability in particular is a delicate concept, as it depends on the offensive play call, the defensive play call, and the individual characteristics of each of the players on the field. A more fine-grained analysis would account for this additional uncertainty. 

Also, because statistical win probability models produce estimates that are too uncertain at many game-states, we suggest in future work exploring probabilistic state-space models to estimate win probability. Probabilistic models simplify the game of football into a series of transitions between game-states. Transition probabilities are estimated from play-level data and win probability is calculated by simulating games. The effective sample size of transition probability models is the number of plays because they are fit from independent play-level observations. Some analysts in private industry have created proprietary probabilistic win probability models, which they believe are more accurate than statistical models because they have a larger effective sample size. Through the lens of the bias-variance tradeoff, proprietors of these models believe that introducing bias in order to reduce variance improves the overall accuracy of the resulting win probability estimator. Nevertheless, these models are subject to their own set of issues, and we believe they aren’t as lowvariance as some analysts claim. Specifically, properly modeling the distribution of the outcome of a play is nontrivial. In contrast to the simple binary win/loss outcome of statistical win probability models, the outcome variable of a transition probability model is the next game-state, which could include a change in yardline, score, or time. This distribution is quite complex: there is a spike at gaining 0 yards for incompletions, a spike for a touchdown, spikes for penalties, and other smooth possibly multimodal distributions for the outcome of run or pass plays, each of which change as a function of team quality and other confounders. Uncertainty in these transition probabilities may, after being properly propagated through a state-space model, result in just as much (if not more) uncertainty in estimated win probability than estimates from statistical models. Additionally, one must take great care to carefully encode all the subtle rules of football into her model, and one needs sufficient computing power to simulate enough games to estimate win probability with enough granularity. We look forward to a public facing exploration of probabilistic win probability models 

> 33Uncertainty caused by our model being wrong or biased, also known as “bias.” 

25 

in the future. 

## **Acknowledgements** 

The authors thank the many football analysts who contributed to the development of expected points models, win probability models, and the fourth down problem. In particular, we thank Brian Burke for providing helpful feedback. The authors acknowledge the High Performance Computing Center (HPCC) at The Wharton School, University of Pennsylvania for providing computational resources that have contributed to the research results reported within this paper. 

## **References** 

- Baldwin, B. (2021a). NFL win probability from scratch using xgboost in R. 

- Baldwin, B. (2021b). nflfastR EP, WP, CP xYAC, and xPass models. 

   - `https://www.opensourcefootball.com/posts/2020-09-28-nflfastrep-wp-and-cp-models` . 

- Burke, B. (2009a). _The 4th Down Study - Part 1_ . 

   - `http://www.advancedfootballanalytics.com/2009/09/4th-down-study-part-1. html` . 

- Burke, B. (2009b). _The 4th Down Study - Part 3_ . 

   - `http://www.advancedfootballanalytics.com/2009/09/4th-down-study-part-3. html` . 

- Burke, B. (2014). Expected Points (EP) and Expected Points Added (EPA) Explained. 

   - `http://www.advancedfootballanalytics.com/2010/01/` 

   - `expected-points-ep-and-expected-points.html` . 

- Candes, E., Fan, Y., Janson, L., and Lv, J. (2016). Panning for gold: Model-free knockoffs for high-dimensional controlled variable selection. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 80. 

- Carl, S. and Baldwin, B. (2022). _nflfastR: Functions to Efficiently Access NFL Play by Play Data_ . https://www.nflfastr.com/. 

- Carroll, B., Palmer, P., and Thorn, J. (1989). _The Hidden Game of Football_ . A Football ink book. Grand Central Pub. 

26 

- Carter, V. and Machol, R. E. (1971). Technical Note—Operations Research on Football. _Operations Research_ , 19(2):541–544. 

- Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’16, pages 785–794, New York, NY, USA. ACM. 

- Eager, E. (2020). PFF WAR: Modeling Player Value in American Football. 

- Friedman, N., Goldszmidt, M., and Wyner, A. (1999). Data analysis with bayesian networks: A bootstrap approach. In _Proceedings of the Fifteenth Conference on Uncertainty in Artificial Intelligence_ , UAI’99, page 196–205, San Francisco, CA, USA. Morgan Kaufmann Publishers Inc. 

- Hastie, T. and Tibshirani, R. (1986). Generalized Additive Models. _Statistical Science_ , 1(3):297 – 310. 

- Hern´an, M. A., Hern´andez-D´ıaz, S., and Robins, J. M. (2004). A structural approach to selection bias. _Epidemiology_ , 15(5):615–625. 

- Huang, D., Stein, N., Rubin, D. B., and Kou, S. C. (2020). Catalytic prior distributions with application to generalized linear models. 

- Huang, D., Wang, F., Rubin, D. B., and Kou, S. C. (2022). Catalytic priors: Using synthetic data to specify prior distributions in bayesian analysis. 

- Lock, D. and Nettleton, D. (2014). Using random forests to estimate win probability before each play of an nfl game. _Journal of Quantitative Analysis in Sports_ , 10. 

- Lopez, M. (2017). _All win probability models are wrong — Some are useful_ . `https://statsbylopez.com/2017/03/08/all-win-probability-modelsare-wrong-some-are-useful` . 

- McShane, B. B. and Wyner, A. J. (2011). A statistical analysis of multiple temperature proxies: Are reconstructions of surface temperatures over the last 1000 years reliable? _The Annals of Applied Statistics_ , 5(1):5 – 44. 

- Medvedovsky, K. and Patton, A. (2022). _Daily Adjusted and Regressed Kalman Optimized projections — DARKO_ . https://apanalytics.shinyapps.io/DARKO/. 

- Peng, Y. and Nagata, M. H. (2020). An empirical overview of nonlinearity and overfitting in machine learning using covid-19 data. _Chaos, Solitons & Fractals_ , 139:110055. 

27 

- Pro Football Reference (2023). _The P-F-R Win Probability Model_ . 

`https://www.pro-football-reference.com/about/win_prob.htm` . 

- Ren, Z., Wei, Y., and Cand`es, E. (2020). Derandomizing knockoffs. 

- Romer, D. (2006). Do Firms Maximize? Evidence from Professional Football. _Journal of Political Economy_ , pages 340–365. 

- Schneider, T. (2023). _Gambletron 2000_ . 

   - `https://www.gambletron2000.com/nfl/30295/new-england-patriotsat-atlanta-falcons` . 

- Subramanian, J. and Simon, R. (2013). Overfitting in prediction models – is it a problem only in high dimensions? _Contemporary Clinical Trials_ , 36(2):636–641. 

- Tripepi, G., Jager, K. J., Dekker, F. W., and Zoccali, C. (2010). Selection Bias and Information Bias in Clinical Research. _Nephron Clinical Practice_ , 115(2):c94–c99. 

- Yang, H., Wan, H., and Zha, Y. (2013). Autocorrelation type, timescale and statistical property in financial time series. _Physica A: Statistical Mechanics and its Applications_ , 392(7):1681–1693. 

- Yurko, R., Ventura, S., and Horowitz, M. (2018). nflWAR: A Reproducible Method for Offensive Player Evaluation in Football. 

28 

## **A Expected points details** 

### **A.1 Statistical expected points models** 

**Early models.** Expected points models for American football have a long history, beginning with former Cincinatti Bengals quarterback Virgil Carter who created expected points (Carter and Machol, 1971). Later, Carroll et al. (1989) developed the first linear expected points model, a linear version of Burke’s Method (below). Romer (2006) developed an expected points model using instrumental variable regression and used expected points in the context of fourth-down decision making. 

**Burke’s method.** Burke (2009a) uses linear regression to model expected points as a cubic spline in yardline. In particular, Burke models 



where _P_ is the points of the next score (a real number in _{_ 7 _,_ 3 _,_ 2 _,_ 0 _, −_ 2 _, −_ 3 _, −_ 7 _}_ , which is positive if the team with possession scores next and negative if the opposing team scores next), **x** is a yardline spline basis, and _ε_ is mean zero noise. Then, the estimated expected points of the next score is **x**<sup>_⊤_</sup> _β_<sup>ˆ</sup> . Burke estimates the spline coefficients _β_<sup>ˆ</sup> from a historical dataset of first down plays. Burke estimates EP from just first down plays because fourth-down decision making relies on the value of a first down (see Appendix C.1 for details). 

**Yurko’s method.** Yurko et al. (2018) model the probability of each potential outcome of the next score and compute expected points as a function of these outcome probabilities. Specifically, they use a multinomial logistic regression (MLR) to model the log-odds of the next scoring event as a function of the game-state, 



where **y** denotes the outcome of the next scoring event in the half after the current play, 



**x** encodes the game-state: yardline, down (categorical), half seconds remaining, log yards to go to acheive a first down, goal-to-go, and an under-two-minutes indicator. Then, the expected points at 

29 

game-state **x** is 



where 



Yurko et al. estimate the coefficients _β_<sup>�</sup> _k_ from historical data. 

**Baldwin’s method.** Baldwin (2021b) uses XGBoost (Chen and Guestrin, 2016) to estimate the probability that the next score results in each of the seven outcomes from Formula (A.3) as a function of game-state. Baldwin uses a larger feature set than previous expected points models, codifying the game-state using yardline, down, yards to go, whether the team with possession is at home, half seconds remaining, roof type (retractable, dome, or outdoors), timeouts remaining for each team, and era (1999-2001, 2002-2005, 2006-2013, 2014-2017, and 2018-present). 

### **A.2** EP **model specification details** 

**Yurko+.** We denote the best multinomial logistic regression EP model we could find by Yurko+. As before, the response variable is the outcome of the next score ( **y** from Formula (A.3)), and the model structure is the same from Formula (A.2) except with different game-state covariates **x** . This model is trained only on first down plays. We include the R code for Yurko+ below. 

```
multinom(label~
```

```
bs(yardline,knots=c(7,33,67,93))+
```

```
bs(half_seconds_remaining,degree=1,knots=c(30))+
```

```
utm:as.numeric(posteam_timeouts_remaining==0)+
```

```
factor(era)+
```

```
posteam_spread+posteam_spread:yardline+
```

```
I((score_differential<=-11))+###waybehind
```

```
I((score_differential>=11))+###wayahead
```

```
I((score_differential<=-4)*(game_seconds_remaining<=900))+###needTD
```

```
I((-3<=score_differential&score_differential<=0)*(game_seconds_remaining<=900))+
I((1<=score_differential&score_differential<=3)*(game_seconds_remaining<=900))+
I((4<=score_differential&score_differential<=10)*(game_seconds_remaining<=900))
```

```
).
```

**The best multinomial logistic regression which uses our eight team quality metrics.** The best multinomial logstic regression which uses our eight hand-crafted team quality measures from Appendix A.4 (four each for the offensive and defensive teams) is similar to the Yurko+ model, except we replace the point spread terms with eight linear terms, one for each metric. 

30 

**Baldwin+.** We denote the best XGBoost EP model we could find by Baldwin+. The best XGBoost model is a XGBoost classification model which predicts the probability of each of the seven potential outcomes of the next score as a function of game-state: yardline, half seconds remaining, half, score differential, point spread, timeouts remaining for the offensive team, and era (2006-2013, 2014-2017, 2018-present). This model is trained only on first down plays. The hyperparameters of Baldwin+ are 

```
{
booster:gbtree
objective:multi:softprob
eval_metric:mlogloss
num_class:7.0
eta:0.087408
gamma:2.2223731e-05
subsample:0.38
colsample_bytree:0.8571429
max_depth:3
min_child_weight:17
nrounds:146.0
}.
```

**The best** XGBoost **regression.** The best XGBoost regression is similar to Baldwin+ except it directly predict the expected points of the next score rather than the probability of each potential outcome of the next score. It uses the same covariates as Baldwin+ and is also trained on first down plays. The hyperparameters of this model are 

```
{
booster:gbtree
objective:reg:logistic
eval_metric:mae
eta:0.0544011
gamma:1.3450771e-06
subsample:0.12
colsample_bytree:0.7142857
max_depth:7
min_child_weight:24
monotone_constraints:
-
-1.0(foryardline)
```

31 

- `0.0 (for half seconds remaining)` 

```
-
1.0(forera)
```

```
-
1.0(foroffensiveteam’stimeoutsremaining)
```

```
-
0.0(forhalf)
```

```
-0.0(forscoredifferential)
-
-1.0(forpointspread)
nrounds:234.0
```

```
}.
```

EP<sup>(0)</sup> **model.** The simple EP<sup>(0)</sup> model which we fit on hold-out data from 1999-2005 in order to craft our team quality metrics is a linear regression in which the points of the next score is a linear function of yardline, log yards to go, and one combined indicator for third and fourth down. 

### **A.3 Score differential bias details** 

Score differential influences the expected points of the next score. For instance, when a team is leading by a large number of points at the end of a game, it will sacrifice scoring points for letting time run off the clock (Yurko et al., 2018). Burke (2014) fits his EP model on all plays from the first and third quarters featuring a score differential within 10 points, allowing him to ignore score differential as a covariate without incurring much bias. His model, however, isn’t suitable for decision making in the second and fourth quarters, where EP substantially differs from the first and third quarters. Yurko et al. (2018) and Baldwin (2021b), on the other hand, use a row weighting procedure to adjust for score differential. Specifically, they weight each row (play) such that the closer a play is to having a score differential magnitude of zero (tie game), the more weight that play is given. As team play style changes subtantially depening on the interation between score differential and time remaining, a more fine-grained EP model would instead include both score differential and time remaining as covariates. In this Section we discuss the details and issues with Burke’s data truncation and Yurko et al. and Baldwin’s row weighting procedure. 

**Burke’s data truncation.** (Burke, 2014) truncates his dataset by only including plays in the first and third quarters where the score differential is within 10 points. By restricting the range of the score differential, Burke removes garbage time plays. It is important to remove garbage time plays because fourth-down decision models are useful when the game is still winnable. Additionally, by removing all second and fourth quarter plays, Burke can exclude score differential as a covariate without incurring much bias. Expected points, however, is subtantially different at the end of a half than at the beginning of a half. In particular, the less time remaining in a half, the more likely that neither team scores before the half ends due to the clock running out. Therefore, a more finegrained EP model would include score differential and time remaining as covariates and train on 

32 

plays from all four quarters. In other words, the fundamental problem with Burke’s data truncation is that it removes too many plays from the dataset. 

**Alternative data truncation.** In order to fit an EP model which allows us to make better fourthdown decisions in the second and fourth quarters, we use an alternative data truncation to Burke’s. Our data truncation keeps plays in the second and fourth quarters, allowing us to model EP as a function of score differential and time remaining, but eliminates garbage time plays. In particular, we construct a simple win probability model WP<sup>(0)</sup> as a function of score differential and time remaining, using held-out data from 1999 to 2005 to avoid data bleed. Then, we keep all plays with WP<sup>(0)</sup> _∈_ [0 _._ 15 _,_ 0 _._ 85]. We discuss the details of our WP<sup>(0)</sup> model in Appendix B.2. 

**Yurko et al. and Baldwin’s row weighting procedure.** Yurko et al. (2018) and Baldwin (2021b), on the other hand, use a row weighting procedure to adress the score differential problem. Because they primarily use expected points for player valuation rather than decision making, their row weighting procedure isn’t as much of an issue for them as it is for us. They weight each row (play) such that the closer a play is to having a score differential magnitude of zero (tie game), the more weight that play is given. Specifically, they weight the _i_<sup>_th_</sup> play in their dataset using the score differential _Si_ by 



The primary problem with this row weighting procedure is that is emphasizes plays where the game is closer to being tied, even though a coach may want to use an EP-based decision making procedure for other values of the score differential (e.g., being down by seven). Plays in which the team with possession is down by, say, seven points should have different EP values (depending on the time remaining) than if the game were tied, so using such a weighted EP model for decision making at all score differentials is wrong. Moreover, even though garbage time plays are downweighted, they still influence the resulting EP model. 

In addition to weighting plays by their score differential, Yurko et al. and Baldwin also weight plays according to their “distance” to the next score in terms of the number of drives. For each play _i_ , they find the difference in the number of drives from the next score, _Di_ = _d_ next score _− di_ , where _d_ next score and _di_ are the drive numbers for the next score and play _i_ , respectively. This difference is then scaled from zero to one in the same way as the score differential in Formula (A.6). The score differential and drive score difference weights are then added together and again rescaled from zero to one in the same manner, resulting in a combined weighting scheme. By combining the two weights, they are placing equal emphasis on both the score differential and the number of drives until the next score. 

33 

The primary problem with weighting plays by the number of drives until the next score is that it introduces bias. Possessions at the beginning of an epoch (which are downweighted) feature punts and turnovers, and possessions at the end of an epoch (which are upweighted) feature scores, and more generally plays at yardlines closer to scoring. Thus, for instance, an EP model using this row weighting scheme may overestimate EP at yardlines close to scoring. 

In this paper, we do not use either of these row weighting procedures in fitting our EP models. Additionally, in the EP model comparison of Section 2.3, we fit Yurko et al. and Baldwin’s EP models without these row weights to test the quality of their underlying model structures. 

### **A.4 Adjusting for team quality** 

In this Section we create our own measures of offensive and defensive quality. In crafting our player and team quality metrics, we use the result of each play, rather than each possession or game, because it leads to better predictive performance. A common and good way of quantifying play success is _expected points added_ (EPA) (Yurko et al., 2018). The EPA of play _n_ is the difference in expected points between the end and the beginning of the play, 



Recall, however, that our goal is to develop team quality metrics to mitigate selection bias in expected points models. This creates a paradox: we want to use EP in order to fit EP models. If we were not careful, we would first fit an EP model that ignores team quality, denoted EP<sup>(0)</sup> . Then we would use EP<sup>(0)</sup> to create EPA based team quality metrics (e.g., EPA per play). Finally, we would fit an EP model which adjusts for team quality. This, however, would introduce data bleed into our analysis. Specifically, we would use the response column **y** to fit EP<sup>(0)</sup> , which we would then transform into features used to fit the team quality adjusted EP model, which is to use **y** to predict **y** . So, to avoid data bleed, we remove all plays from 1999 to 2005 from our play-by-play dataset and fit EP<sup>(0)</sup> to this held-out data. Now, we can use EPA<sup>(0)</sup> to fit EP models which adjust for team quality. The specification of our simple EP<sup>(0)</sup> model is detailed in Appendix A.2. 

Now, we use EPA<sup>(0)</sup> (EPA derived from EP<sup>(0)</sup> ) to craft our team and player quality metrics. For concreteness, consider deriving the quarterback quality of Patrick Mahomes. Index all the plays from 2006 to 2021 in which Mahomes passes or runs the ball by _n_ . We define Mahomes’ quarterback quality prior to play _n_ by a weighted sum of the EPA<sup>(0)</sup> of his previous plays, 



34 



Figure 12: The career mean quarterback quality of each quarterback with over 1750 attempts and whose rookie season came after 2006. 

where _q_ 0 := 0 and EPA<sup>(0)</sup> 0 := 0. We use an exponential decay weight _α_ to upweight more recent plays (Medvedovsky and Patton, 2022). We set _α_ = 0 _._ 995 for each of our team and player quality metrics. For instance, a play which occured 138 plays ago is weighted half as much as the previous play since 0 _._ 995<sup>138</sup> = 0 _._ 5. Also, a play which occured 459 plays ago is weighted one-tenth as much as the previous play since 0 _._ 995<sup>459</sup> = 0 _._ 1. Additionally, at the start of each season, we shrink by a multiplicative factor _γ_ . So, the shrinkage weight _γn_ of play _n_ is _γ_ if this is Mahomes’ first play of the season, otherwise it is 1. We use different shrinkage values _γ_ for each team and player quality metric, shown in Table 5. We tuned these _γ_ values to optimize predictive performance on a held-out validation set. A smaller _γ_ reflects a quantity that is noiser from year to year. Finally, we standardize each offensive and defensive quality metric to have mean zero and standard deviation 1 _/_ 2. In Figure 12 we plot the career mean quarterback quality of each quarterback with over 1750 attempts and whose rookie season came after 2006. As expected, Patrick Mahomes has by far the highest quarterback quality. We construct the other team quality metrics described in Table 5 in a similar fashion, via Formula (A.8). 

35 

|variable|_γ_|
|---|---|
|quarterback quality|3_/_4|
|non-quarterback offensive quality|1_/_2|
|defensive quality against the pass|1_/_3|
|defensivequalityagainst the run|1_/_3|



Table 5: Summary of team quality metrics computed via Formula (A.8) and their start-of-season shrinkage parameters _γ_ . Each of these metrics apply to both the offensive and defensive teams in a play, yielding eight total metrics. 

### **A.5 Offense is more important than defense for scoring points** 

In Figure 13 we visualize the best multinomial logistic regression EP model<sup>34</sup> which uses our eight hand-crafted team quality measures<sup>35</sup> (four each for the offensive and defensive teams). Each metric is standardized to have mean 0 and s.d. 1 _/_ 2. For each team quality metric, we plot expected points as a function of yardline for various values of that metric, holding each of the other seven team quality values fixed at 0 (representing the average). The offensive team’s quarterback quality and the defensive team’s quarterback quality have the largest and second largest impact on expected points, respectively. We visualize this “impact” by the width of the lines in the spaghetti plot. The offensive team’s remaining offensive quality and the defensive team’s remaining offensive quality have the third and fourth largest impact on expected points, respectively. Finally, each defensive quality metric has minimal impact on expected points. This provides further evidence for the notion that offense is more important than defense in scoring points, and hence in constructing a successful football team.<sup>36</sup> 

### **A.6 Team quality knockoffs** 

Defensive quality has a minimal impact on scoring points, and we wonder whether this impact is significant. To investigate, we modify the knockoffs procedure from Candes et al. (2016) and Ren et al. (2020) to fit the autocorrelated nature of our football play-by-play dataset. In particular, the original model- **X** knockoffs framework assumes each predictor **X** _j_ consists of i.i.d. observations, which does not hold for our team quality metrics. Across 25 runs of the knockoffs procedure, each offensive quality metric is selected each time, indicating that offensive quality matters in predicting the points of the next score. The defensive quality metrics, on the other hand, are not selected most of the time. In other words, our defensive quality metrics are not significantly better at predicting points than random noise. 

> 34See Appendix A.2 for details. 

> 35See Appendix A.4 for details. 

> 36Eager (2020) also provides evidence that offense is more valuable than defense. 

36 



Figure 13: Expected points as a function of yardline for various values of our eight hand-crafted team quality measures, according to a multinomial logistic regression model, holding other confounders constant. Quarterback quality has the largest impact on EP. Defensive quality has a minimal impact on EP. 

Each team quality metric has a similar form. For instance, Mahomes’ quarterback quality prior to play _n_ from Formula (A.8) is equivalently expressed as 



We think of the result of play _k −_ 1, and hence EPA<sup>(0)</sup> _k−_ 1, as the realization of a random variable. As the rolling sum of these play results, each resulting team quality vector ( _qn_ ) does not consist of independent observations. But, due to Formula (A.9), to construct a valid knockoff of each team quality metric we need only construct a valid knockoff of the vector EPA<sup>(0)</sup> . 

To construct a knockoff of the observed EPA<sup>(0)</sup> vector, we need to model the distribution of the EP<sup>(0)</sup> vector. We model EP<sup>(0)</sup> using ridge regression<sup>37</sup> and use Gaussian noise with mean given by predictions from the ridge regression<sup>38</sup> to generate a synthetic EP<sup>(0)</sup> vector. Then, we construct a synthetic EPA<sup>(0)</sup> vector from this synthetic EP<sup>(0)</sup> vector, recalling that EPA<sup>(0)</sup> _k−_ 1 = EP<sup>(0)</sup> _k −_ EPA<sup>(0)</sup> _k−_ 1. Finally, we keep just every 5<sup>_th_</sup> observation, which makes the vector EPA<sup>(0)</sup> nearly uncorrelated and its generated synthetic counterpart nearly uncorrelated. Thus, we generate a knockoff EPA<sup>�(0)</sup> of EPA<sup>(0)</sup> such that they are approximately equal in distribution, visualized in Figure 14. 

> 37Specifically, we use ridge regression to model EP(0) as a function of yardline, an indicator for 3 _rd_ or 4 _th_ down, and log yards to go to match the EP<sup>(0)</sup> model from Appendix A.2, and indicators for offensive team-season and defensive team-season since the result of a play depends on the teams playing. 

> 38and with s.d. 1 _/_ 20 

37 



Figure 14: Distribution of EPA<sup>(0)</sup> and a knockoff EPA<sup>�(0)</sup> . 

With our knockoff of each team quality metric constructed from our knockoff of EPA<sup>(0)</sup> , the procedure from Candes et al. (2016) holds. In particular, for any subset _S ⊂{_ 1 _,..., p}_ , denote the original predictor matrix by **X** and its knockoff by **X**<sup>�</sup> . Let ( **X** _,_ **X**<sup>�</sup> )swap( _S_ ) refer to concatenating **X** with **X**<sup>�</sup> and swapping each predictor in **X** with its knockoff. Then, we still approximately have 



Also, we construct the knockoffs **X**<sup>�</sup> without looking at the response variable (e.g., points of the next score). Therefore, Lemma 3.2, Lemma 3.3, and Theorem 3.4 from Candes et al. (2016) still hold. 

Now, using a knockoff **X**<sup>�</sup> of **X** , we fit a lasso regression where the response variable is the points of the next score and the predictor variables are the game-state, the eight real team quality metrics, and the eight knockoff team quality metrics. As in Candes et al. (2016), we select the team quality variables _j_ where the statistics 



are larger than a smartly chosen threshold. Here, _λ_ is the lasso penalty hyperparameter, _b_<sup>ˆ</sup> _j_ is the fitted lasso coefficient of the real team quality metric, and _b_<sup>ˆ</sup><sup>_′_</sup> _j_<sup>isthefittedlassocoefficientofthe</sup> knockoff team quality metric. Moreover, as in Ren et al. (2020), we de-randomize the knockoffs procedure by repeating the procedure 25 times. 

In Table 6 we show the proportion of the 25 knockoffs procedures in which each team quality vari- 

38 

able is not selected. Each offensive quality metric is selected each time, indicating that offensive quality matters in predicting the points of the next score. The defensive quality metrics, on the other hand, are not selected much of the time. This provides evidence that our defensive quality metrics are not significantly better than noise at predicting the points of the next score. 

|variable|not selectedproportion|
|---|---|
|offensive team’s quarterback quality|0|
|defensive team’s quarterback quality|0|
|offensive team’s non-quarterback offensive quality|0|
|defensive team’s non-quarterback offensive quality|0|
|defensive team’s defensive quality against the pass|0.88|
|offensive team’s defensive quality against the pass|0.84|
|defensive team’s defensive quality against the run|0.40|
|offensive team’s defensivequalityagainst the run|0.76|



Table 6: The proportion of knockoffs procedures in which each team quality variable is not selected. 

## **B Win probability details** 

### **B.1 Statistical win probability models** 

**Yurko’s method.** Yurko et al. (2018) use a generalized additive model (GAM) (Hastie and Tibshirani, 1986) to estimate win probability from historical data. A GAM allows win probability to vary according to the sum of smooth nonlinear functions of the dependent variables. Formally, they model 



where _s_ is a smooth function while the other variables are defined in Table 7. 

**Baldwin’s method.** Baldwin (2021a) uses XGBoost (Chen and Guestrin, 2016) to estimate win probability from historical data. The response variable is again a binary variable indicating whether the team with possession wins the game. Baldwin models win probability as a function of score differential, game seconds remaining, half seconds remaining, yardline, down, yards to go, whether the team with possession is at home, whether the team with possession receives the second half kickoff, and the number of timeouts remaining for each team. Baldwin uses two additional features 

> 39We use EP(0), an EP model fit on hold-out data from 1999-2005, to avoid data bleed in implementing Yurko et al.’s win probbility model (see Appendix A.2 for details). 

39 

|variable|variable description|
|---|---|
|_y_|1 if the team with possession wins the game, else 0|
|_u_|1 if time remaining in half is under two minutes, else 0|
|_h_1|1 if frst half, else 0|
|_h_2|1 if second half, else 0|
|_sh_|half seconds remaining|
|_sg_|game seconds remaining|
|_t_off|timeouts remaining for offensive team|
|_t_def|timeouts remaining for defensive team|
|E[_S_]|expected score differential=EP+_S_|
||whereEP=expectedpoints<sup>39 </sup>and_S_=score differential|



Table 7: Variables in Yurko et al.’s win probability model. 

to capture the change in impact of point spread and score differential over the course of a game, 



and 



Baldwin includes monotonic constraints for many covariates,<sup>40</sup> which reduces overfitting. It makes sense to include monotonic constraints in WP classification models but not in EP classification models because, for instance, the probability that the next score is a field goal is not monotonic in yardline but win probability is. 

**Other methods.** Lock and Nettleton (2014) and ESPN (via Burke and Gargiulo) also estimate win probability from historical data – the former use a random forest and the latter an ensemble of machine learning methods (Lopez, 2017). On the other hand, Schneider (2023) uses live betting market data and Pro Football Reference (2023) uses a normal approximation to estimate win probability. In this paper, we give detailed descriptions of Baldwin’s method since it underlies his popular public fourth-down decision framework,<sup>41</sup> and of Yurko’s method since we use it as a catalytic prior. Although Burke’s method is also used for fourth-down decision making in the public sphere, his method is proprietary. 

> 40Specifically, he includes monotonic constraints for yardline, yards to go, down, score differential, timeouts remaining for each team, spread-time, and diff-time-ratio. 

> 41via Baldwin’s Twitter `@ben bot baldwin` . 

40 

### **B.2** WP **model specification details** 

**Yurko+.** We denote the best GAM WP model we could find by Yurko+. As before, the response variable is a binary variable indicating whether the team with possession won the game, and the model structure is the same from Formula (B.1) except with different game-state covariates. This model is trained only on first down plays. Formally, the model is 



where era is a categorical variable denoting whether the season is in 2006-2012, 2013-2017, or 2018-present, and the other variables are detailed in Table 7. 

**Baldwin+.** We denote the best XGBoost WP model we could find by Baldwin+. The best XGBoost model is a XGBoost classification model which predicts win probability as a function of gamestate: score differential, game seconds remaining, point spread, yardline, receive 2<sup>_nd_</sup> half kickoff indicator, timeouts, and 



to help fit win probability at the very end of the game. This model is trained only on first down plays. This model uses fewer covariates than Baldwin’s original model and includes a few new ones. The hyperparameters of Baldwin+ are 

```
{
eta:0.0658986
gamma:0.0079786
subsample:0.98
colsample_bytree:0.875
max_depth:4
min_child_weight:4
monotone_constraints:
-1.0(forscoredifferential)
```

41 

- `0.0 (for game seconds remaining)` 

- `-1.0 (for point spread)` 

- `-1.0 (for yardline)` 

- `1.0 (for score-time-ratio)` 

- `0.0 (for receive 2nd half kickoff)` 

- `1.0 (for offensive team’s timeouts remaining)` 

```
-
-1.0(fordefensiveteam’stimeoutsremaining)
nrounds:189.0
test_loss:0.4413572
```

```
}.
```

WP<sup>(0)</sup> **model.** The simple WP<sup>(0)</sup> model which we fit on hold-out data from 1999-2005 in order to truncate our dataset in a way that removes garbage time plays but keeps plays in the second and fourth quarters to train our EP models is a logistic regression as a function of time remaining, score differential, and their interaction. 

### **B.3** WP **model comparison** 

In this Section, we compare the out-of-sample predictive performance of various WP models. Our full dataset consists of all football plays from 2006 to 2021. The dataset is clustered into games, as plays from each game share the same winning team. To keep the clustered nature of our dataset intact and to avoid data bleed, we split our dataset in half by randomly sampling 50% of all games. The first down plays from the first 50% of these games form the hold-out test set. We test on first down plays because, as discussed in Appendix C.1, fourth-down decision making relies on the value of having a first down. The plays from the other 50% of these games form the training set. To tune XGBoost models, we split the training set in half by randomly sampling 50% of the games from the training set. The plays from the first 50% of these games form the XGBoost training set, and the remaining plays form the validation set for hyperparameter tuning. We then tune our XGBoost models in a similar fashion as Baldwin (2021a). 

We visualize the results of our model comparison in Table 8. We discussed Yurko et al. and Baldwin’s models in Section B.1. We give detailed descriptions of the best GAM (Yurko+) and XGBoost (Baldwin+) models in Appendix B.2. 

An improved GAM outperforms Baldwin’s XGBoost because the latter overfits. An improved XGBoost model outperforms an improved GAM because win probability is a highly nonlinear function of the interacting fundamental variables of score differential and time remaining. The best catalytic machine learning model only slightly edges out the best XGBoost model because XGBoost 

42 

|model|model|team|out-of-sample|
|---|---|---|---|
|name|type|quality|logloss|
|Catalytic|Catalytic|point spread|0.438|
|Baldwin+|XGBoost|point spread|0.439|
|Yurko+|GAM|point spread|0.442|
|Baldwin|XGBoost|spread-time|0.476|
|Yurko|GAM||0.480|



Table 8: Predictive performance of various WP models. 

classification for win probability takes advantage of monotone constraints (e.g., because win probability is monotone in yardline), whereas XGBoost classification for expected points couldn’t.<sup>42</sup> The best catalytic model used the Baldwin+ XGBoost classification model as the complex target model and the Yurko+ GAM model as the catalytic prior. We used _M_ = 25,000 synthetic win probability estimates generated from the catalytic prior. We tuned the catalytic hyperparameter _M_ in a similar manner as the standard XGBoost hyperparameters. There are significantly fewer generated datapoints from the WP catalytic prior than from the EP catalytic prior because we generate fake win probability estimates WP<sup>�</sup> _∈_ [0 _,_ 1] rather than synthetic outcomes of the next score **y** _∈{_ TD _,_ FG _,...}_ . Win probability estimates WP<sup>�</sup> carry a similar amount of information as, say, 100 win outcomes in _{_ 0 _,_ 1 _}_ : for instance, a win probability estimate of 0 _._ 45 can be equivalently represented by 45 generated ones and 55 zeros. 

### **B.4 Simulation study details** 

**Generating plays.** Formally, the outcome of the _n_<sup>_th_</sup> play of the _g_<sup>_th_</sup> game is 



The game starts at midfield, _Xg_ 0 = _L/_ 2, and the game begins tied, _Sg_ 0 = 0. The field position at the start of play _n_ is 



> 42See Section 2.1 for details. 

43 

and the score differential at the start of play _n_ is 



The response column _win_ is 



As in our dataset of real football plays, this response column is highly autocorrelated – plays from the same game share the same draw of the winner of the game. 

**Generating observational data.** We create a dataset of plays from _G_ games. Each game consists of _N_ plays, and the field consists of _L_ yardlines. The results from each game yield a simulated dataset 



**True win probability.** The true win probability 



of our simplified version of football is computed explicitly using dynamic programming, 



and 



**Visualizing the simulation study results.** In Figure 15 we visualize the MAE of WP estimates and the confidence interval lengths and coverages, averaged over all of the simulations. 

44 







Figure 15: As a function of true WP, MAE of true and estimated WP (Figure (a)), coverage of true WP by randomized cluster bootstrap (Figure (b)), and confidence interval length of randomized cluster bootstrap (Figure (c)). 

45 

## **C Fourth-down decision making details** 

### **C.1 Fourth-down decision framework** 

In this Section we compute the value (e.g., expected points or win probability) of the next gamestate if a team punts, kicks a field goal, or attempts a conversion. 

**The value of a punt.** Suppose the offensive team has a fourth down at yardline _y_ . If the offensive team punts, the opposing team has a first down at the next yardline, which we think of as a random variable. Hence the value of punting is negative the opponent’s expected value of having a first down at the next yardline _y_<sup>_′_</sup> , 



Here, _V_ 1 is the value of having a first down (according to EP or WP). For simplicity, we instead compute the value of having a first down at the expected next yardline after punting, 



Because _V_ 1 is linear in yardline for many game-states, this simplification is reasonable. We discuss the details of our model of the expected next yardline after punting, which is a function of yardline and punter quality, in Appendix C.2. Note that in computing _V_ 1, we flip the game-state variables which are relative to the team with possession (e.g., score differential, team quality metrics, timeouts remaining, etc.) and we don’t alter the game-state variables which apply to both teams (e.g., time remaining, etc.). 

**The value of a field goal.** Suppose the offensive team has a fourth down at yardline _y_ and attempts a field goal. If the offensive team misses the field goal, the opposing team has a first down at yardline 100 _− y_ . If it makes the field goal, the offensive team scores three points and the opposing team has a first down after a kickoff. Now, the expected value of kicking a field goal is 



Here, letting _s_ denote score differential, 



46 

and _V_ 1 is the value of having a first down (according to EP or WP). As before, in computing _V_ 1 and _V_ (make FG), we flip the game-state variables which are relative to the team with possession (e.g., score differential, team quality metrics, timeouts remaining, etc.) and we don’t alter the gamestate variables which apply to both teams (e.g., time remaining, etc.). We discuss the details of our field goal probability model, which is a function of yardline and kicker quality, in Appendix C.3. Similar to the simplification we made in computing the value of a punt, here we simplify by 



assuming the kickoff ends in a touchback. 

**The value of going for it.** Suppose the offensive team has a fourth down and _z_ yards-to-go at yardline _y_ . If the offensive team goes for it and gains ∆ _≥ z_ yards, then in the next play it has a first down at yardline _y −_ ∆. Conversely, if the offensive team goes for it and gains ∆ _< z_ yards, then in the next play the opposing team has a first down at yardline 100 _−_ ( _y −_ ∆). Hence the expected value of going for it on fourth down is 



where _V_ 1 is the value of having a first down (according to EP or WP). As the probability density of the yards gained on a conversion attempt is complex, we employ a standard simplification from Burke (2009b). In particular, if the offensive team converts on fourth down and _z_ yards-to-go at yardline _y_ , we assume they gain _z_ yards on that play. Also, if the offensive team fails to convert, we assume they turn the ball over at the initial yardline of the play, leaving the opposing team with a first down at yardline 100 _− y_ . Thus the value of going for it becomes 



We discuss the details of our conversion probability model, which is a function of yardline, yardsto-go, and offensive and defensive quality, in Appendix C.4. As before, in computing _V_ 1, we flip the game-state variables which are relative to the team with possession (e.g., score differential, team quality metrics, timeouts remaining, etc.) and we don’t alter the game-state variables which apply to both teams (e.g., time remaining, etc.). 

47 

### **C.2 Expected next yardline after a punt model** 

In this Section, we model the expected next yardline (from the perspective of the receiving team) after a punt as a function of yardline and punter quality (from the perspective of the punting team). Our punter quality adjustment, detailed below, is similar to our offensive and defensive quality adjustments from Section A.4. 

**Punter quality.** We define a punter’s quality by a weighted sum of his punt yards over expected over all his previous punts in his career. To begin, we fit a simple expected next yardline after punting model E<sup>(</sup> Punt<sup>0)onaheld-outdatasetofallpuntsfrom1999to2005toavoiddatableed.</sup> We fit E<sup>(</sup> Punt<sup>0)using linear regression as a function of yardline (specifically,a cubic polynomial in</sup> yardline). Then, we define the _punt yards over expected_ (PYOE) of the _n_<sup>_th_</sup> punt by 



Now, we define punter quality, using Rams’ punter Johnny Hekker for concreteness. Index all of Hekker’s punts from 2006 to 2021 by _n_ . We define Hekker’s punter quality prior to punt _n_ by a weighted sum of the punt yards over expected from his previous kicks, 



where pq0 := 0 and PYOE0 := 0. As before, we use an exponential decay weight _α_ = 0 _._ 995 to upweight more recent punts. Finally, we standardize the punter quality column to have mean zero and standard deviation 1 _/_ 2. In Figure 16a we plot the career mean punter quality of each punter with over 250 punt attempts from 2006 to 2021. As expected, Johnny Hekker has the highest punter quality. 

**Expected next yardline after a punt model.** We use linear regression to model the expected next yardline after a punt as a function of yardline and punter quality (pq). Formally, our best model of the expected next yardline after punting is 



The model is trained on a dataset of 36 _,_ 493 punts from 2006 to 2021, all beyond the 30 yardline. In Figure 16b we plot the expected next yardline after a punt according to our model as a function of yardline for various punter quality values. 

48 





Figure 16: On the left, the career mean punter quality of each punter with over 250 punts from 2006 to 2021. On the right, the expected next yardline after a punt according to our model as a function of yardline for various punter quality values. 

### **C.3 Field goal probability model** 

In this Section, we model the probability that a kicker makes a field goal as a function of yardline and kicker quality. It is important to adjust for kicker quality to avoid selection bias, as good kickers attempt more field goals from long distance than bad kickers. Our kicker quality adjustment, detailed below, is similar to our punter quality adjustment from the previous Section. 

**Kicker quality.** We define a kicker’s quality by a weighted sum of his field goal probability added over all his previous kicks in his career. To begin, we fit a simple field goal probability model _P_<sup>(0)aheld-outdatasetofallfieldgoalsfrom1999to2005toavoiddatableed.Wefit</sup><sup>_P_(0)</sup> FG<sup>on</sup> FG using logistic regression as a function of yardline (specifically, a cubic polynomial spline with five degrees of freedom on the yardline). Then, we define the _field goal probability added_ (FGPA) of 

49 

the _n_<sup>_th_</sup> field goal by 



Now, we define kicker quality, using Ravens’ kicker Justin Tucker for concreteness. Index all of Tucker’s field goals from 2006 to 2021 by _n_ . We define Tucker’s kicker quality prior to field goal _n_ by a weighted sum of the field goal probability added in his previous kicks, 



where kq0 := 0 and FGPA0 := 0. As before, we use an exponential decay weight _α_ = 0 _._ 995 to upweight more recent kicks. Finally, we standardize the kicker quality column to have mean zero and standard deviation 1 _/_ 2. In Figure 17a we plot the career mean kicker quality of each kicker with over 100 field goal attempts from 2006 to 2021. As expected, Justin Tucker has by far the highest kicker quality. 

**Field goal probability model.** We use logistic regression to model the probability that a kicker makes a field goal as a function of yardline and kicker quality (kq). Formally, our best field goal probability model is 



Fitting this model on our dataset of 15 _,_ 472 observed field goals from 2006 to 2021 yields nontrivial probability predictions for extremely long field goals that have never before been made (e.g., nontrivial probability for a 73 yard field goal from the 55 yardline). To shrink these field goal probability predictions to zero, we impute 500 synthetic missed field goals, randomly distributed from the 51 to the 99 yardline, into our dataset. In Figure 17b we plot the probability of making a field goal according to our model as a function of yardline for various kicker quality values. 

### **C.4 Conversion probability model** 

In this Section, we model fourth down conversion probability as a function of yards to go and team quality. One difficulty with fitting a fourth down conversion probability model is there are only 8 _,_ 258 fourth down conversion attempts in our dataset from 2006 to 2021. Existing models use third down as a proxy for fourth down, as they are also high pressure situations in which the offensive team attempts to gain a first down on that play (Romer, 2006). There may be, however, a fundamental difference in conversion probability between third and fourth down plays, perhaps due to psychological reasons. Therefore, in our model comparison, we test models on a random 

50 





Figure 17: On the left, the career mean kicker quality of each kicker with over 100 field goal attempts from 2006 to 2021. On the right, the probability of making a field goal according to our model as a function of yardline for various kicker quality values. 

50% of fourth down plays, and we train some models on a dataset consisting entirely of fourth down plays and other models on a dataset consisting of third and fourth down plays. We find that the parameters of our best conversion probability model, detailed below in Formula (C.14), borrow strength from third down plays. 

Our best logistic regression model adjusts for yards to go, down (third vs. fourth down), and our offensive and defensive quality metrics from Section A.4: quarterback quality of the offensive team (qbqot), non-quarterback offensive quality of the offensive team (oqrot), defensive quality of the defensive team against the pass (dqdtap), and defensive quality of the defensive team against 

51 

the run (dqdtar). Formally, our best conversion probability model is 



In Figure 18 we visualize conversion probability as a function of yardline for various values of yards to go. We see a large spike in conversion probability with one yard to go, potentially due to quarterback sneaks. Additionally, in Figure 19 we plot conversion probability as a function of yards to go for various values of team quality. We find that quarterback quality significantly impacts conversion probability, but the other team quality measures have little impact. 



Figure 18: Conversion probability according to our model as a function of yards to go, assuming average team quality. 



Figure 19: Conversion probability according to our model as a function of yards to go for various values of team quality. Quarterback quality has by far the largest impact on conversion probability. 

A more elaborate conversion probability model may adjust for yardline. In particular, it is plausible that it is more difficult to convert near each endzone, where space is more constricted. Additionally, a more fine-grained model would be continuous in yards to go rather than treating it as an 

52 

integer. Of course, our model can only be as good as available data, which treats yards to go as an integer. But, anecdotally, 4<sup>_th_</sup> down and inches has a significantly higher conversion probability than fourth down and one yard to go. Finally, conversion probability depends on the offensive and defensive play call. On this view, in practice it may be better for teams to input their own conversion probability estimates as they are more informed on their play calling tendecies. 

### **C.5 Baseline coach’s decision model** 

To compare our decision making procedure to the decisions that actual football coaches tend to make, we model the probability that a coach chooses a decision in _{_ Go _,_ FG _,_ Punt _}_ as a function of game-state. We use XGBoost to fit these coach probabilities. XGBoost works well here because we have 94 _,_ 786 fourth down plays in our full dataset of plays from 1999 to 2022, and each play is an independent observation of a coach’s decision. In particular, we fit these coach probabilities as a function of yardline, yards to go, game seconds remaining, score differential, point spread, and era (1999-2001, 2002-2005, 2006-2013, 2014-2017, and 2018-present). In Figure 20 we visualize these coach decision models, and the results make intuitive sense. For the most part, coaches punt deep in their own territory and kick field goals near the opponent’s endzone, except for with one and sometimes two yards to go. Also, at the end of the game, coaches’ decision making changes depending on the number of points they need to score to win the game. 

In Figure 21 we visualize the variable importance (via gain) of our XGBoost model. Interestingly, point spread has an extremely small impact on coachs’ fourth-down decisions. Perhaps this is because coaches don’t like to admit when their teams are underdogs as some sort of psychological leadership tool. We find, however, that point spread should impact fourth-down decision making. For instance, in certain game-states, it is advantageous for the favorites to be more aggressive (e.g., late in close games). 

The parameters of our XGBoost model are 

```
{
booster:gbtree
objective:multi:softprob
eval_metric:mlogloss
num_class:3.0
eta:0.0453573
gamma:0.0013761
subsample:0.6698295
colsample_bytree:0.8924051
```

53 









Figure 20: Visualizing our model of the typical coach’s fourth-down decision as a function of yardline and yards to go, for various values of time remaining and score differential. Green, yellow, and red indicate that Go, FG, and Punt is the most likely decision, respectively. The darkness of the color reflects the likelihood that a coach makes that decision. 

```
max_depth:4
min_child_weight:6
nrounds:592
```

```
}.
```

54 



Figure 21: Variable importance (gain) for coach’s decision probability model. 

55 


