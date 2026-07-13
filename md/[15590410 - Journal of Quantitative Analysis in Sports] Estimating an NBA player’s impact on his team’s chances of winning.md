<!-- source: [15590410 - Journal of Quantitative Analysis in Sports] Estimating an NBA player’s impact on his team’s chances of winning.pdf -->

J. Quant. Anal. Sports 2016; 12(2): 51–72 

# Sameer K. Deshpande* and Shane T. Jensen **Estimating an NBA player’s impact on his team’s chances of winning** 

#### DOI 10.1515/jqas-2015-0027 

**Abstract:** Traditional NBA player evaluation metrics are based on scoring differential or some pace-adjusted linear combination of box score statistics like points, rebounds, assists, etc. These measures treat performances with the outcome of the game still in question (e.g. tie score with five minutes left) in exactly the same way as they treat performances with the outcome virtually decided (e.g. when one team leads by 30 points with one minute left). Because they ignore the context in which players perform, these measures can result in misleading estimates of how players help their teams win. We instead use a win probability framework for evaluating the impact NBA players have on their teams’ chances of winning. We propose a Bayesian linear regression model to estimate an individual player’s impact, after controlling for the other players on the court. We introduce several posterior summaries to derive rank-orderings of players within their team and across the league. This allows us to identify highly paid players with low impact relative to their teammates, as well as players whose high impact is not captured by existing metrics. 

**Keywords:** Basketball; Bayesian shrinkage; lasso; win probability. 

## **1  Introduction** 

Determining which National Basketball Association (NBA) players do the most to help their teams win games is perhaps the most natural question in basketball analytics. Traditionally, one quantifies the notion of helping teams win with a scoring statistic like points-per-game or true shooting percentage, a function of point differential like Adjusted Plus-Minus [see, e.g. Rosenbaum (2004), Ilardi and Barzilai (2008)] and variants thereof, or some 

***Corresponding author: Sameer K. Deshpande,** The Wharton School, University of Pennsylvania – Statistics, 434 Jon M. Huntsman Hall 3730 Walnut St., Philadelphia, Pennsylvania 19104, USA, e-mail: dsameer@wharton.upenn.edu. http://orcid.org/0000-0003-4116-5533 **Shane T. Jensen:** The Wharton School, University of Pennsylvania – Statistics, Philadelphia, Pennsylvania, USA 

combination of box score statistics and pace of play like the player efficiency rating (PER) of Hollinger (2004). 

While these metrics are informative, we observe that they ignore the context in which players perform. As a result, they can artificially inflate the importance of performance in low-leverage situations, when the outcome of the game is essentially decided, while simultaneously deflating the importance of high-leverage performance, when the final outcome is still in question. For instance, point differential-based metrics model the home team’s lead dropping from 5 points to 0 points in the last minute of the first half in exactly the same way that they model the home team’s lead dropping from 30 points to 25 points in the last minute of the second half. In both of these scenarios, the home team’s point differential is –5 points but, as we will see in Section 2.1, the home team’s chance of winning the game dropped from 72% to 56% in the first scenario while it remained constant at 100% in the second. We argue that a player’s performance in the second scenario has no impact on the final outcome and should therefore not be treated comparably to performance in the first. We address this issue by proposing a win probability framework and linear regression model to estimate each player’s contribution to his team’s overall chance of winning games. 

The use of win probability to evaluate the performance of professional athletes dates back at least to Mills and Mills (1970), who evaluated Major League Baseball players. As Studeman (2004) observes, their Player Wins Average methodology has been re-introduced several times since, most notably as win probability added (WPA). To compute WPA, one starts with an estimate of a team’s probability of winning the game at various game states. For each plate appearance, one then credits the pitcher and batter with the resulting change in their respective team’s win probability and then sums these contributions over the course of a season to determine how involved a player was in his team’s wins (or losses). A natural extension of the WPA methodology to basketball would be to measure the change in the win probability from the time a player enters the game to the time he is substituted out of the game and then sum these changes over the course of a season. Such an extension is identical to the traditional plus-minus statistic except that it 

**52** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

is computed on the scale of win probability instead of points scored. 

An inherent weakness of using plus-minus (on both the point and win probability scales) to assess a player’s performance is that a player’s plus-minus statistic necessarily depends on the contributions of his teammates and opponents. According to Gramacy, Jensen, and Taddy (2013), since the the quality of any individual player’s pool of teammates and opponents can vary dramatically, “the marginal plus-minus for individual players are inherently polluted.” To overcome this difficulty, Rosenbaum (2004) introduced Adjusted Plus-Minus to estimate the average number of points a player scores per 100 possession after controlling for his opponents and teammates. To compute Adjusted Plus-Minus, one first breaks the game into several “shifts,” periods of play between substitutions, and measures both the point differential and total number of possessions in each shift. One then regresses the point differential per 100 possessions from the shift onto indicators corresponding to the 10 players on the court. 

We propose instead to regress the change in the home team’s win probability during a shift onto signed indicators corresponding to the five home team players and five away team players in order to estimate each player’s _partial effect_ on his team’s chances of winning. Briefly, if we denote the change in the home team’s win probability in the _i_ th shift by _yi_ , we then model the expected change in win probability given the players on the court, as 



where θ = (θ1, … θ488)<sup></sup> is the vector of player partial effects and **h** _i_ = { _hi_ 1, …, _hi_ 5} and **a** _i_ = { _ai_ 1, …, _ai_ 5} are indices on θ corresponding to the home team (h) and away team (a) players. The intercept term μ _i_ may depend on additional covariates, such as team indicators. 

Fitting the model in Equation 1 is complicated by the fact that we have a relatively large number of covariates (viz. a total of 488 players in the 2013–2014 season) displaying a high degree of collinearity, since some players are frequently on the court together. This can lead to imprecise estimates of player partial effects with very large standard errors. Regularization, which shrinks the estimates of the components of θ towards zero, is therefore necessary to promote numerical stability for each partial effect estimate. 

We take a Bayesian approach, which involves specifying a prior distribution with mode at zero on each partial effect and using play-by-play data from the 2013–2014 season to update these priors to get a posterior distribution of the partial effects. As Kyung et al. (2010) argue, the Bayesian formulation of regularized regression produces 

valid and tractable standard errors, unlike popular frequentist techniques like the lasso of Tibshirani (1996). This enables us to quantify the joint uncertainty of our partial effect estimates in a natural fashion. 

Our proposed methodology produces a _retrospective_ measure of individual player contributions and does not attempt to measure a player’s latent ability or talent. Our estimates of player partial effect are context-dependent, making them unsuitable for forecasting future performance since the context in which a player plays can vary season-to-season and even week-to-week. Nevertheless, because our proposal is context-dependent, we feel that it provides a more appropriate accounting of what actually happened than existing player-evaluation metrics like PER and ESPN’s Real Plus/Minus (RPM). Taken together with such existing metrics, our estimates of player effect can provide insight into whether coaches are dividing playing time most effectively and help understand the extent to which a player’s individual performance translate to wins for his team. 

The rest of this paper is organized as follows. We detail our data and regression model in Section 2 and describe our estimation of win probability in Section 2.1. Section 3 presents a full Bayesian analysis of the joint uncertainty about player effects. In Section 3.1 we introduce _leverage profiles_ to measure the similarity between the contexts in which two players performed. These profiles enable us to make meaningful comparisons of players based on their partial effect estimates. In keeping with the examples of other player evaluation metrics, we propose two rankorderings of players using their partial effects. In Section 4, we rank players on a team-by-team basis, allowing us to determine each player’s relative value to his team. In Section 5, we present a single ranking of all players which balances a player’s partial effect against the posterior uncertainty in estimating his effect. We extend our analysis of player partial effects in Section 6 to five-man lineups and consider how various lineups matchup against each other. We conclude in Section 7 with a discussion of our results and several extensions. 

## **2  Data, models, and methods** 

Like Adjusted Plus/Minus, we break each game into shifts: periods of play between successive substitutions when the 10 players on the court is unchanged. During the 2013– 2014 regular season, a typical game consisted of around 31 shifts. In order to determine which players are on the court during each shift, we use play-by-play data obtained from 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **53** 

ESPN for 8365 of the 9840 (85%) of the scheduled regular season games in each of the eight seasons between 2006 and 2014. The play-by-play data for the remaining 15% of games were either incomplete or missing altogether. The majority of the missing games were from the first half of the time window considered. To the best of our knowledge, our dataset does not systematically exclude games from certain teams or certain types of games (early-season vs late-season, close game vs blow-out). Using the data from the 2006–2007 season to 2012–2013 season, we estimate the home team’s win probability as a function of its lead and the time elapsed. With these win probability estimates, we then compute the change in the home team’s win probability during each of _n_ = 35,799 shifts in the 2013–2014 regular season. We denote the change in the home team’s win probability during the _i_ th shift by _yi_ . This change in win probability can be directly attributed to the performance of the 10 players on the court during that shift. Thus, to measure each individual player’s impact on the change in win probability, we regress _yi_ onto indicator variables corresponding to which of the 488 players were on the court during the _i_ th shift. We model 

_yi_ | **hi , ai** = µ + θ _hi_ 1 +�+ θ _hi_ 5 − θ _ai_ 1 −�θ _ai_ 5 + τ _Hi_ − τ _Ai_ + σε _i_ , (2) 

where θ = (θ1, …, θ488)<sup></sup> is the vector of partial effects for the 488 players, τ = (τ1, …, τ30)<sup></sup> is a vector of partial effects for the 30 teams, with **h** _i_ = { _hi_ 1, …, _hi_ 5} and **a** _i_ = { _ai_ 1, …, _ai_ 5} are indices on θ corresponding to the home team (h) and away team (a) players, _Hi_ and _Ai_ are indices on τ corresponding to which teams are playing in shift _i_ , and the ε _i_ are independent standard normal random variables. We view μ as a league-average “home-court advantage” and σ as a measure of the variability in _yi_ that arises from both the uncertainty in measuring _yi_ and the inherent variability in win probability that cannot be explained by 

the performance of the players on the court. Since we are including team effects in Equation 2, each player’s partial effect is measured relative to his team’s average, so that players are not overly penalized. 

### **2.1  Estimation of win probability** 

In order to fit such a regression model, we must begin with an estimate of the probability that the home team wins the game after leading by _L_ points after _T_ seconds, which we denote by _pT_ , _L_ . Estimating win probability at specific intermediate times during a game is not a new problem; indeed, Lindsey (1963) estimated win probabilities in baseball in the 1960s and Stern (1994) introduced a probit regression model to estimate _pT_ , _L_ . Maymin, Maymin, and Shen (2012) expanded on that probit model to study when to take starters in foul trouble out of a game, Bashuk (2012) considered empirical estimates of win probability to predict team performance in college basketball, and Pettigrew (2015) recently introduced a parametric model to estimate win probability in hockey. Intuitively, we believe that _pT_ , _L_ is a smooth function of both _T_ and _L_ ; for a fixed lead, the win probability should be relatively constant for a small duration of time. By construction, the probit model of Stern (1994) produces a smooth estimate of the win probability and the estimates based on all games from the 2006–2007 to 2012–2013 regular seasons are shown in Figure 1(A), where the color of the unit cell [ _T_ , _T_ + 1]  × [ _L_ , _L_ + 1] corresponds to the estimated value of _pT_ , _L_ . 

To get a sense of how well the probit estimates fit the observed data, we can compare them to the empirical estimates of _pT_ , _L_ given by the proportion of times that the home team has won after leading by _L_ points after _T_ seconds. The empirical estimates of _pT_ , _L_ are shown in Figure 1(B). 



<!-- Start of picture text -->
40 40 40<br>20 20 20<br>0 0 0<br>–20 –20 –20<br>–40 –40 –40<br>0 500 1500 2500 0 500 1500 2500 0 500 1500 2500<br>T T T<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0<br>L L L<br><!-- End of picture text -->

**Figure 1:** Various estimates of _pT_ , _L_ . The probit estimates in (A), while smooth, do not agree with the empirical win probabilities shown in (B). Our estimates, shown in (C), are closer in value to the empirical estimates than are those in (A) but are much smoother than the empirical estimates. 

**54** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

We see immediately that the empirical estimates are rather different than the probit estimates: for positive _L_ , the probit estimate of _pT_ , _L_ tends to be much smaller than the empirical estimate of _pT_ , _L_ and for negative L, the probit estimates tend to overestimate _pT_ , _L_ . This discrepancy arises primarily because the probit model is fit using only data from the ends of the first three quarters and does not incorporate any other intermediate times. Additionally, the probit model imposes several rather strong assumptions about the evolution of the win probability as the game progresses. As a result, we find the empirical estimates much more compelling than the probit estimates. Despite this, we observe in Figure 1(B) that the empirical estimates are much less smooth than the probit estimates. Also worrying are the extreme and incongruous estimates near the edges of the colored region in Figure 1(B). For instance, the empirical estimates suggest that the home team will always win the game if they trailed by 18 points after five minutes of play. Upon further inspection, we find that the home team trailed by 18 points after five minutes exactly once in the seven season span from 2006 to 2013 and they happened to win that game. In other words, the empirical estimates are rather sensitive to small sample size leading to extreme values which can heavily bias our response variables _yi_ in Equation 2. 

To address these small sample issues in the empirical estimate, we propose a middle ground between the empirical and probit estimates. In particular, we let _NT_ , _L_ be the number of games in which the home team has led by ℓ points after _t_ seconds where _T_ – _ht_ ≤ _t_ ≤ _T_ + _ht_ and _L_ – _hl_ ≤ ℓ ≤ _L_ + _hl_ , where _ht_ and _hl_ are positive integers. We then let _nT_ , _L_ be the number of games which the home team won in this window and model _nT_ , _L_ as a Binomial ( _NT_ , _L_ , _pT_ , _L_ ) random variable. This modeling approach is based on the assumption that the win probability is relatively constant over a small window in the ( _T_ , _L_ )-plane. The choice of _ht_ and _hl_ dictate how many game states worth of information is used to estimate _pT_ , _L_ and larger choices of both will yield, in general, smoother estimates of _pT_ , _L_ . Since very few offensive possession last six seconds or less and since no offensive possession can result in more than four points, we argue that the win probability should be relatively constant in the window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2] and we take _ht_ = 3, _hl_ = 2. 

We place a conjugate Beta(α _T_ , _L_ , β _T_ , _L_ ) prior on _pT_ , _L_ and estimate _pT_ , _L_ with the resulting posterior mean _p_ ˆ _T_ , _L_ , given by 



The value of _yi_ in Equation 2 is the difference between the estimated win probability at the end of the shift and at the start of the shift. 

Based on the above expression, we can interpret α _T_ , _L_ and β _T_ , _L_ as “pseudo-wins” and “pseudo-losses” added to the observed counts of home team wins and losses in the window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2]. The addition of these “pseudo-games” tends to shrink the original empirical 

α _T_ <u>,</u> _L_ estimates of _pT_ , _L_ towards α _T_ , _L_ + β _T_ , _L_ . To specify α _T_ , _L_ and β _T_ , _L_ , it is enough to describe how many pseudo-wins and pseudo-losses we add to each of the 35 unit cells [ _t_ , + 1]  × [ℓ, ℓ + 1] in the window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2]. We add a total of 10 pseudo-games to each unit cell, but the specific number of pseudo-wins depends on the value of ℓ For ℓ < –20 we add 10 pseudo-losses and no pseudo-wins and for ℓ > 20, we add 10 pseudo-wins and no pseudo-losses. For the remaining values of ℓ, we add five pseudo-wins and five pseudo-losses. Since we add 10 pseudo-games to each cell, we add a total of α _T_ , _L_ + β _T_ , _L_ = 350 pseudo-games the window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2]. We note that this procedure does not ensure that our estimated win probabilities are monotonic in lead and time. However, the empirical win probabilities are far from monotonic themselves, and our procedure does mitigate many of these departures by smoothing over the window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2]. 

We find that for most combinations of _T_ and _L_ , _NT_ , _L_ is much greater than 350; for instance, at _T_ = 423, we observe _NT_ , _L_ = 4018, 11,375, 17,724, 14,588, and 5460 for _L_ = –10, –5, 0, 5, and 10, respectively. In these cases, the value of _p_ ˆ _T_ , _L_ is driven more by the observed data than by the values of α _T_ , _L_ and β _T_ , _L_ . Moreover, in such cases, the uncertainty of our estimate _p_ ˆ _T_ , _L_ , which can be measured by the posterior standard deviation of _pT_ , _L_ is exceeding small: for _T_ = 423 and –10  ≤ _L_ ≤  10, the posterior standard deviation of _pT_ , _L_ , is between 0.003 and 0.007. When _NT_ , _L_ is comparable to or much smaller than 350, the values of α _T_ , _L_ and β _T_ , _L_ exert more influence on the value of ˆ ˆ _pT_ , _L_ . The increased influence of the prior on _p T_ , _L_ in such rare game states helps smooth over the extreme discontinuities that are present in the empirical win probability estimates above. In these situations, there is a larger degree of uncertainty in our estimate of _p_ ˆ _T_ , _L_ , but we find that the posterior standard deviation of _pT_ , _L_ never exceeds 0.035. The uncertainty in our estimation of _pT_ , _L_ leads to additional uncertainty in the _yi_ ’s, akin to measurement error. The error term in Equation 2 is meant to capture this additional uncertainty, as well as any inherent variation in the change in win probability unexplained by the players on the court. 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **55** 

### **2.2   Bayesian linear regression of player effects** 

As mentioned in Section 1, we take a Bayesian approach to fitting the model in Equation 2. Because we have a large number of covariates displaying a high degree of collinearity, a regularization prior that shrinks each component of θ towards zero is needed to promote stability for each partial effect. Popular choices of regularization priors on the components θ _j_ include a normal prior, which corresponds to an ℓ2 penalty, or a Laplace prior, which corresponds to an ℓ1 penalty. Thomas et al. (2013) also consider a Laplace-Gaussian prior, which combines both ℓ2 and ℓ1 penalties. Maximum a posteriori estimation with respect to these priors correspond to ridge, lasso, and elastic net regression, respectively. 

We choose to use the Laplace prior, which was also considered by Thomas et al. (2013) to derive rankings of National Hockey League players. Between the normal and Laplace prior, we choose to use the Laplace prior since it tends to pull smaller partial effects towards zero faster than the normal prior, as noted by Park and Casella (2008). We are thus able to use the existing R implementation of Park and Casella (2008)’s Gibbs sampler in the monomvn package. Though the elastic net is better suited for regression problems in which there are groups of highly correlated predictors than is the lasso Zou and Hastie (2005), there is no widely-available Gibbs sampler and the computational challenge of implementation offsets the additional benefit we gain from using the Laplace-Gaussian prior. We let **P**<sup>_i_</sup> be a vector indicating which players are on the court during shift _i_ so that its _j_ th entry,<sup>**P**</sup> _ji_ , is equal to 1 if player _j_ is on the home team, –1 if player _j_ is on the away team, and 0 otherwise. Similarly, we let **T**<sup>_i_</sup> be a vector indicating which teams are playing during shift _i_ so that its _k_ th entry, **T** _ki_ , is equal to 1 if team _k_ is the home team, –1 is team _k_ is the away team, and 0 otherwise. Conditional on **P**<sup>_i_</sup> and **T**<sup>_i_</sup> , we model 



We place independent Laplacian priors on each component of θ and τ, conditional on the corresponding noise parameters σ<sup>2</sup> The conditional prior densities of (θ, τ) given σ<sup>2</sup> is given by 



where λ > 0 is a sparsity parameter that governs how much each component of θ is shrunk towards zero. We further place a flat prior on μ, a Gamma( _r_ , δ) hyper-prior on λ<sup>2</sup> , and non-informative hyper-priors on σ<sup>2</sup> , _r_ , and δ. 

Because of the hierarchical structure of our model, the joint posterior distribution of (μ, θ, τ, σ<sup>2</sup> ) is not analytically tractable and we must instead rely on a Markov Chain Monte Carlo (MCMC) simulation to estimate the posterior distribution. We use the Gibbs sampler described by Park and Casella (2008) that is implemented in the monomvn package in R. We note that our prior specification is the default setting for this implementation. 

In specifying this regression model, we make several strong assumptions. First, we assume that the<sup>_y_</sup> _i_<sup>′</sup> s<sup>are</sup> independent. Since it is generally not the case that all 10 players are substituted out of the game at the end of the shift, it is reasonable to expect that there will be some autocorrelation structure among the _y_ i’s. Indeed, as seen in the autocorrelation plot in Figure 2(B), we observe a small amount of autocorrelation (–0.1) between _yi_ and _yi_ + 1. We also observe that there is no significant autocorrelation at larger lags. While the independence assumption is not technically correct, the lack of persistent autocorrelation and the relatively weak correlation between _yi_ and _yi_ + 1, make the assumption somewhat more palatable. 

Our second modeling assumption is that, conditional on ( **P** _i_ , **T** _i_ ), the _yi_ ’s are Gaussian with constant variance. This conditional Gaussian assumption does not imply that the _yi_ ’s are marginally Gaussian (which does not seem to be the case in Figure 2(A)). Despite the fact that we have 35,799 shifts in our dataset, we find that there are 29,453 unique combinations of 10 players on the court. Thus, we only observe a few instances of each unique ( **P** _i_ , **T** _i_ ) making it difficult to assess the conditional normality assumption directly. The limited number of each ( **P** _i_ , **T** _i_ ) also makes it difficult to check the assumption of constance variance of the _yi_ ’s conditional on ( **P** _i_ , **T** _i_ ). In the Appendix, we explore several transformations and alternative specifications of the _yi_ ’s, but do not find alternatives that match these assumptions better than our current specification. 

At this point, it is also worth mentioning that our model does not explicitly include the duration of each shift as a predictor, despite the fact that _yi_ depends on shift length. Figure 3(A) shows the change in win probability associated with varying shift durations and varying lead changes. Quite clearly, we see that the curves in Figure 3(A) are different, indicating a dependence between _yi_ and shift duration, although we see in Figure 3(B) that the overall correlation is quite small. On a conceptual level, a player’s performance in a 15 s shift during which his team’s win 

**56** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 



**Figure 2:** Histogram and autocorrelation plot of the _yi_ ’s. 



<!-- Start of picture text -->
A B<br>0<br>–0.2<br>–0.4<br>30 s shift<br>60 s shift<br>90 s shift<br>–0.6 120 s shift<br>–0.8<br>–1.0<br>Change in win probability<br><!-- End of picture text -->



**Figure 3:** Change in win probability plotted against shift duration. 

probability increases by 20% has the same impact on his team’s chances of winning had the shift lasted 30 s. Since our ultimate goal is to estimate each player’s individual impact, as opposed to his playing time-adjusted impact or per-minute impact, including shift duration as an additional predictor distorts the desired interpretation of player partial effects. In fact, we assert that the change in win probability as an outcome variable is the most natural way to account for the effect of shift duration on a player’s overall impact on the court. 

## **3  Full posterior analysis** 

We use the Gibbs sampler function lasso in the monomvn R package to obtain 1000 independent samples from the full posterior distribution of (μ, θ, τ, σ<sup>2</sup> ). With these 

samples, we can approximate the marginal posterior density of each player’s partial effect using a standard kernel density estimator. Figure 4 shows the estimated posterior densities of the partial effects of several players. 

We see that these densities are almost entirely supported within the range [–0.02, 0.02], indicating that it is unlikely that any individual player, over the course of a single shift, is able to improve (or hurt) his team’s chances of winning the game by more than a percentage point or two. This is partly due to our regularization prior, which tends to pull the components of θ and τ towards zero, and to the fact that the _yi_ ’s are tightly concentrated near zero. Nevertheless, though our estimates of each player’s partial effect are small, we still see considerable heterogeneity in the approximate posterior densities. Most strikingly, we see that the posterior distribution of Dirk Nowitzki’s partial effect is mostly supported on the positive axis (in 991 out of our 1000 posterior samples, his effect is positive) while 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **57** 



**Figure 4:** Approximate posterior densities of several players’ partial effects. 

the posterior distribution of Alonzo Gee’s partial effect is mostly supported on the negative axis (his partial effect is negative in 976 out of 1000 posterior samples). 

Intuitively, we can measure a player’s “value” by his partial effect on his team’s chances of winning. Among the players in Figure 4, we see that Nowitzki was the most valuable since his density lies further to the right than any other player’s. However, there is considerable overlap in the support of his density and that of Kevin Durant, making it difficult to determine who is decidedly the “most valuable.” Indeed, we find that Nowitzki’s partial effect is greater than Kevin Durant’s in 692 out of 1000 posterior samples. We also observe high similarity in the posterior densities of Durant and LeBron James, who finished first and second, respectively, in voting for the 2013–2014 Most Valuable Player (MVP) award. On closer inspection, we find that Durant’s partial effect is greater than James’ in only 554 of the 1000 posterior samples, indicating that, by the end of the 2013–2014 regular season, Durant and James had very nearly the same impact on their teams’ chances of winning, with Durant enjoying a rather slight advantage. In the context of the MVP award, then, our results would suggest that Durant is only slightly more deserving than James, but Nowitzki is more deserving than both Durant and James. 

We can also track how the posterior distribution of player partial effects evolve over the course of the season, which helps to determine how many games worth of data is necessary to start differentiating the partial effects of 

different players. Figure 5 show the approximate posterior densities of Durant, Gee, James, and Nowitzki after weeks 1, 5, 10, 15, 20, and 25 of the season. 

Through the first five weeks of the season, the posterior distributions of each player’s partial effects are virtually identical. However, after 10 weeks, we begin to see some separation, with Gee’s density moving towards the left and Durant’s density moving towards the right. This suggests that we need at least 10 weeks worth of data (approximately 30–35 games) in order to identify differences in player partial effects. We see a rather considerable gap between Durant’s and James’ densities by week 15 and we observe that Durant’s partial effect is greater than James’ in nearly 75% of the posterior samples up to that time. Over the next 10 weeks, though, this gap shrinks considerably: visually, the two posterior densities become increasingly indistinguishable and the proportion of posterior samples in which Durant’s partial effect is greater than James’ shrinks back towards 0.5. This mirrors the general consensus described by Ballentine (2014) and Buckley (2014) about how the race for the MVP award evolved: Durant was the clear front-runner for the MVP award by late January (approximately week 13 of the season) but many reporters declared the race much closer after James’ historic performances in weeks 18 and 19 (including multiple 40-point performances and a 61-point performance against Charlotte). We also see that the separation between Nowitzki’s density and Durant’s density increases between weeks 15 and 20. 

### **3.1  Comparing players** 

Directly comparing partial effects for all pairs of players is complicated by the fact that players perform in different contexts. To determine which players are most comparable, we determine the total number of shifts each player played, his team’s average win probability at the start of these shifts, the average duration of these shifts, and the average length of each shift. We call this information a player’s _leverage profile_ . We then compute the Mahalanobis distance between the leverage profiles of each pair of players. Table 1 shows the four players with the most similar leverage profile for several players and Figure 6 shows comparison box plots of the posterior distribution of their partial effects. 

We see that the posterior distributions of partial effects for each player in Table 1 are well-separated from the posterior distribution of partial effects of the player with the most similar leverage profile. For instance, LeBron James’ leverage profile is most similar to DeAndre Jordan’s, but 

**58** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 



<!-- Start of picture text -->
Week 1 Week 5 Week 10<br>150 150 P(DN>KD)=0.5 150<br>Durant P(DN>KD)=0.516 Durant P(KD>LBJ)=0.502 Durant P(DN>KD)=0.459<br>James P(KD>LBJ)=0.562 James P(LBJ>AG)=0.685 James P(KD>LBJ)=0.657<br>Nowitzki P(LBJ>AG)=0.472 Nowitzki Nowitzki P(LBJ>AG)=0.813<br>Gee Gee Gee<br>100 100 100<br>50 50 50<br>0 0 0<br>–0.03 –0.02 –0.01 0 0.01 0.02 0.03 –0.03 –0.02 –0.01 0 0.01 0.02 0.03 –0.03 –0.02 –0.01 0 0.01 0.02 0.03<br>Partial effect Partial effect Partial effect<br>Week 15 Week 20 Week 25<br>150 150 150<br>Durant P(DN>KD)=0.494 Durant P(DN>KD)=0.648 Durant P(DN>KD)=0.692<br>James P(KD>LBJ)=0.745 James P(KD>LBJ)=0.662 James P(KD>LBJ)=0.554<br>Nowitzki P(LBJ>AG)=0.844 Nowitzki P(LBJ>AG)=0.902 Nowitzki P(LBJ>AG)=0.989<br>Gee Gee Gee<br>100 100 100<br>50 50 50<br>0 0 0<br>Density Density<br>Density Density<br><!-- End of picture text -->

**Figure 5:** Approximate posterior densities of Kevin Durant’s, LeBron James’, and Dirk Nowitzki’s partial effect as the season progresses. 

**Table 1:** Most similar leverage profiles. 

|**Player**<br>|**Similar players**||
|---|---|---|
|LeBron James|DeAndre Jordan (0.025)<br>|Kevin Durant (0.055)|
||Blake Griffin (0.082)<br>|Stephen Curry (0.204)|
|Chris Paul<br>|Shawn Marion (0.081)<br>|Courtney Lee (0.103)|
||Terrence Ross (0.126)<br>|Chris Bosh (0.141)|
|Kyrie Irving<br>|DeMarcus Cousins (0.080)|Tristan Thompson (0.087)|
||Brandon Bass (0.099)<br>|Randy Foye (0.109)|
|Zach Randolph|Jimmy Butler (0.020)<br>|David West (0.045)|
||Mike Conley (0.063)<br>|George Hill (0.073)|



Mahalanobis distance shown in parentheses. 

we see that James’ posterior distribution is located to the right of Jordan’s and we find that in 884 of the 1000 posterior samples, James’ partial effect is greater than Jordan’s. This suggests that while James and Jordan played in similar contexts, James’ performance in these situations was more helpful to his team than Jordan’s. 

### **3.2  Team effects** 

Recall that the inclusion of team effects, τ, in Equation 2 was to ensure that the partial effects of players were 

not overly deflated if they played on bad teams or overly inflated if they played on good teams. Figure 7 shows box plots of the posterior distribution of all team effects. 

We see that the Milwaukee Bucks and Sacramento Kings have a noticeably negative effect. This suggests that opposing teams generally increased their chances of winning, regardless of which five Bucks or Kings players were on the court. This is in contrast with the San Antonio Spurs, whose team effect is substantially positive. Figure 8 shows comparative box plots of the posterior distribution of the partial effects for a few Bucks, Kings, and Spurs players. 

The fact that the posterior distributions of Isaiah Thomas’, DeMarcus Cousins’, and Khris Middleton’s partial effects are predominantly concentrated on the positive axis indicates that their performance stood out despite the relatively poor quality of their team. On the other hand, the posterior distributions of Ben McLemore’s, O.J. Mayo’s, and Brandon Knight’s partial effects are predominantly concentrated on the negative axis, indicating that their teams’ already diminished chances of winning decreased when they were on the court. The fact that Manu Ginobili has such a large positive partial effect is especially noteworthy, given the Spurs’ already large positive effect. 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **59** 



<!-- Start of picture text -->
0.02 0.02<br>0.01 0.01<br>0 0<br>–0.01 –0.01<br>–0.02 –0.02<br>L. James D. Jordan K. Durant B. Griffin S. Curry C. Paul S. Marion C. Lee T. Ross C. Bosh<br>0.02 0.02<br>0.01 0.01<br>0 0<br>–0.01 –0.01<br>–0.02 –0.02<br><!-- End of picture text -->

**Figure 6:** Comparison box plots of partial effects of players with similar leverage profiles. 

## **4  Impact ranking** 

Since we may view a player’s partial effect as an indication of his value to his team, we can generate a rank-ordering of the players on each team based on their partial effects. Intuitively, we could rank all of the members of a particular team by the posterior mean or median of their partial effects. Such an approach, however, does not incorporate the joint uncertainty of the partial effects. Alternatively, for each team and each posterior sample of θ, we could rank the partial effects of all players on that team and then identify the rank-ordering with highest posterior frequency. Unfortunately, since there are over one trillion orderings of 15 players (the minimum number of players per team), such an approach would require an impractical number of posterior samples. Instead, we propose 

to average the player rankings over the 1000 posterior samples to get their **Impact Ranking** . Table 2 shows the Impact Ranking for the players on the San Antonio Spurs and the Miami Heat, with the most common starting lineup bolded and players who played very limited minutes starred. 

In Table 2, we see that the most impactful player for the Spurs, Manu Ginobili, is a bench player, while five of the next six most impactful players were the most common starters. This is in contrast to the Heat, for whom we only observe three starters in the top five most impactful players and a rather significant drop-off down to the remaining starters. For instance, Dwayne Wade was not nearly as impactful as several Heat bench players and Shane Battier was even less valuable than several players who had very limited minutes (DeAndre Liggins and 

**60** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 



**Figure 7:** Comparison box plots of the posterior distribution of team effects. 

Justin Hamilton) or limited roles (Greg Oden). This indicates that the Heat did not rely much on Wade or Battier to win games, despite their appearance in the starting lineup. We can further compare each player’s salary to his impact ranking to get a sense of which players are being over- or under-valued by their teams. For instance, Patty Mills earned only $1.3M, the eleventh highest salary on the Spurs, despite being the third most impactful player on the team. In contrast, Wade was the ninth most impactful player on Heat, despite earning nearly $15 million 

dollars more than Mario Chalmers, who was the third most impactful player for the Heat. 

## **5  Impact Score** 

A natural use of any player evaluation methodology is to generate a single ranking of all players and we could simply rank all players in the league according to the posterior mean of their partial effects. Unfortunately, since the mean by influenced by a few very extreme value, such a ranking can overvalue players whose partial effects have large posterior variance. To try to account for the joint variability of player effects, we can rank the players’ partial effect estimates in each of our 1000 simulated posterior samples. Then we could compute 95% credible intervals for each player’s partial effects-based rank. We find, however, that these intervals are rather long. For instance, we find that LeBron James had the largest partial effect among all players in only 11 of the 1000 posterior samples and the 95% credible interval for his rank is [3, 317]. Similarly, we find that Kevin Durant also had the largest partial effect among all players in 11 of the 1000 posterior samples and the 95% credible for his rank is [2, 300]. It turns out that Dirk Nowitzki had the largest partial effect in the most number of posterior samples (39 out of 1000) but the credible interval for his rank is [1, 158]. Given the considerable overlap in the posterior distributions of player partial effects as seen in Figure 4, it is not surprising to see the large joint posterior variability in player partial effects reflected in the rather long credible intervals of each player’s partial effects-based ranks. 



**Figure 8:** Comparison box plots of partial effects of selected Bucks, Kings, and Spurs players. 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **61** 

**Table 2:** Impact ranking for San Antonio Spurs and Miami Heat players. 

|**Rank **|**San Antonio Spurs**<br>|**Miami Heat**|
|---|---|---|
|1<br> <br>|Manu Ginobili ($7.5M, 0.719) <br>|**Chris Bosh**($19.1M, 0.650)<br>|
|2<br> <br>|**Danny Green**($3.8M, 0.540) <br> <br>|**LeBron James**($19.1M, 0.683)<br>|
|3<br>|Patty Mills ($1.3M, 0.531)<br>|**Mario Chalmers**($4M, 0.577)|
|4<br>|**Kawhi Leonard**($1.9M, 0.631)|Ray Allen ($3.2M, 0.571)|
|5<br>|**Tiago Splitter**($10M, 0.510)|Toney Douglas ($1.6M, 0.486)|
|6<br>|**Tony Parker**($12.5M, 0.554)|Roger Mason Jr. ($0.8M, 0.509)|
|7<br>|**Tim Duncan**($10.4M, 0.518)|Chris Andersen ($1.4M, 0.518)|
|8<br>|Damion James<sup>*</sup>($20K, 0.489)|James Jones ($1.5M, 0.520)|
|9<br>|Boris Diaw ($4.7M, 0.566)<br>|**Dwyane Wade**($18.7M, 0.515)|
|10<br>|Matt Bonner ($3.9M, 0.582)|DeAndre Liggins<sup>*</sup>($52K, 0.520)|
|11<br>|Jeff Ayres ($1.8M, 0.556)<br>|Norris Cole ($1.1M, 0.570)|
|12<br>|Nando de Colo ($1.4M, 0.561)|Justin Hamilton<sup>*</sup>($98K, 0.541)|
|13<br>|Austin Daye ($0.9M, 0.530)|Michael Beasley ($0.8M, 0.511)|
|14<br>|Aron Baynes ($0.8M, 0.513)|Greg Oden ($0.8M, 0.503)|
|15<br>|Cory Joseph ($1.1M, 0.583)|Rashard Lewis ($1.4M, 0.525)|
|16<br>|Marco Belinelli ($2.8M)<br> <br>|**Shane Battier**($3.3M, 0.618)<br>|
|17||Udonis Haslem ($4.3M)|



For each player, we report both his salary and the approximate probability that his partial effect is greater than the that of the player ranked immediately after him. Starred players played very limited minutes. 

We instead propose to rank players according to their **Impact Score** , which we define as the ratio between the posterior mean and the posterior standard deviation of a player’s partial effect. This definition is very similar to the Sharpe Ratio used in finance to examine the performance of an investment strategy. We may view Impact Score as a balance between a player’s estimated “risk” (i.e. uncertainty about his partial effect) and a player’s estimated “reward” (i.e. average partial effect). As an example, we find that the posterior mean of Iman Shumpert’s partial effect is less than the posterior mean of Chris Bosh’s partial effect (0.0063 compared to 0.0069). We also find that the posterior standard deviation of Shumpert’s partial effect is 0.0034 while it is 0.0039 for Bosh. Between the two players, Shumpert gets the edge in Impact Score rankings because we are less uncertain about his effect, despite him having a smaller average effect compared to Bosh. Table 3 shows the 30 players with largest Impact Scores. Somewhat unsurprisingly, we see a number of superstars in Table 3. Patrick Patterson is a notable standout; as Cavan (2014) and Lapin (2014) note, he provided valuable three-point shooting and rebounding off the bench for the Toronto Raptors. 

It is important to note that our reported Impact Scores are subject to some degree of uncertainty, since we have to estimate the posterior mean and standard deviation of each player’s partial effect. This uncertainty amounts 

**Table 3:** Players with the highest Impact Scores. 

|1. Dirk Nowitzki (2.329)|16. Eric Bledsoe (1.274)|
|---|---|
|2. Patrick Patterson (1.939)|17. Dwight Howard (1.273)|
|3. Iman Shumpert (1.823)|18. Danny Green (1.214)|
|4. Chris Bosh (1.802)|19. Deron Williams (1.212)|
|5. Manu Ginobili (1.779)|20. Matt Barnes (1.206)|
|6. James Harden (1.637)|21. Roy Hibbert (1.205)|
|7. Chris Paul (1.588)|22. J.J. Redick (1.201)|
|8. Zach Randolph (1.56)|23. Shaun Livingston (1.201)|
|9. Joakim Noah (1.555)|24. Marcin Gortat (1.185)|
|10. Stephen Curry (1.514)|25. Greivis Vasquez (1.175)|
|11. Nene Hilario (1.474)|26. Blake Griffin (1.174)|
|12. Andre Iguodala (1.445)|27. Anthony Tolliver (1.151)|
|13. Kevin Durant (1.410)|28. LaMarcus Aldridge (1.140)|
|14. LeBron James (1.324)|29. Courtney Lee (1.131)|
|15. Isaiah Thomas (1.310)|30. Nate Robinson (1.126)|



to MCMC simulation variability and induces some uncertainty in the reported player rankings. In order to quantify the induced uncertainty explicitly, we could run our sampler several times, each time generating a draw of 1000 simulated posterior samples and ranking the players according to the resulting Impact Scores. We could then study the distribution of each player’s ranking. While straightforward in principle, the computational burden of running our sampler sufficiently many times is rather impractical. Moreover, we suspect the simulation-to-simulation variability in Impact Scores is small. Since we are estimating the posterior mean and standard deviation of player partial effects with 1000 samples, we are reasonably certain that the estimated values are close to the true values. As a result, our reported Impact Scores are reasonably precise and we do not expect much variation in the player rankings. 

### **5.1   Comparison of Impact Score to other metrics** 

Hollinger (2004) introduced PER to “sum up all [of] a player’s positive accomplishments, subtract the negative accomplishments, and a return a per-minute rating of a player’s performance.” Recently, ESPN introduced RPM which improves on Adjusted Plus-Minus through a proprietary method that, according to Ilardi (2014), uses “Bayesian priors, aging curves, score of the game and extensive out-of-sample testing.” Figure 9 shows Impact Score plotted against PER and RPM. We note that of the 488 players in our data set, RPM was available for only 437. In Figure 9, we have excluded the six players whose PER is greater than 33 or less than –3 so that the scale of the figure is not distorted by these extreme values. 

**62** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 



**Figure 9:** Comparison of Impact Score to PER (A) and RPM (B). We find that RPM is much more consistent with Impact Score than is PER, though there are still several inconsistencies in overall player evaluation. Note that PER is calibrated so the league average is 15.00. 

We find that the correlation between Impact Score and PER is somewhat moderate (correlation 0.226) and that Impact Score is much more highly correlated with RPM (correlation of 0.655). This is somewhat expected, since PER is essentially context-agnostic and RPM at least partially accounts for the context of player performance. To see this, we note that the number of points a player scores is a key ingredient in the PER computation. What is missing, however, is any consideration of _when_ those points were scored. RPM is more context-aware, as it considers the score of the game when evaluation player performance. However, since the RPM methodology is proprietary, the extent to which the context in which a player performs influences his final RPM value remains unclear. 

As we noted in Section 1, metrics like PER and pointdifferential metrics can overvalue low-leverage performances. An extreme example of this is DeAndre Liggins’ PER of 129.47. Liggins played in a single game during the 2013–2014 regular season and in his 84 s of play, he made his single shot attempted and recorded a rebound. We note, however, that Liggins entered the game when his team had a 96.7% chance of winning the game and his performance did not improve his team’s chances of winning in any meaningful way. Figure 10 plots each player’s Impact Score, PER, and RPM against the average win probability of each player’s shifts. In Figure 10, we have included the players with very negative PER values who were excluded from Figure 9. 

In Figure 10, we see that the average starting win probability for Chris Smith, Vander Blue, Tony Mitchell, and DeAndre Liggins was less than 0.2 or greater than 0.8, suggesting that they played primarily in low-leverage situations. We see that while their PERs ranged from –23 to 130, 

their Impact Scores are all very close to zero. This confirms that our methodology correctly values so-called “garbage time” performance. It is interesting to note Hasheem Thabeet played when his team had, on average, above a 70% of winning the game. His negative Impact Score is an indication that his performance generally hurt his team’s chances of winning and we find that he had a negative partial effect in 678 of the 1000 posterior samples. 

While it is encouraging that there is at least some positive correlation between Impact Scores and PER, simply looking at the correlation is not particularly informative, as these metrics are measuring rather different quantities. Of greater interest, perhaps, is to see when PER and Impact Score agree and when they disagree. For instance, we find players like LeBron James, Chris Paul and Dirk Nowitzki who have both large PER values and large Impact Scores. The large PER values are driven by the fact that they efficiently accumulated more positive box-score statistics (e.g. points, assists, rebounds, etc.) than negative statistics (e.g. turnovers and fouls) and the large Impact Scores indicate that their individual performances helped improve their team’s chances of winning. On the other hand, Brook Lopez and Kyrie Irving have the ninth and twenty-ninth largest PER values but their rather middling Impact Scores suggest that, despite accumulating impressive individual statistics, their performances did not actually improve their teams’ chances of winning. 

In contrast to Irving and Lopez, players like Iman Shumpert and Andre Iguodala have below-average PER values but rather large Impact Scores. Shumpert has a PER of 9.66, placing him in the bottom 25% of the league, but has the fourth largest Impact Score. This suggests that even though Shumpert himself did not accumulate 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **63** 



**Figure 10:** Impact Score, PER, and RPM plotted against average starting win probability. Note that RPM was unavailable for 51 players. 

particularly impressive individual statistics, his team nevertheless improved its chances of winning when he was on the court. It is worth noting that Shumpert and Iguodala are regarded as top defensive players. As Goldsberry and Weiss (2013) remark, conventional basketball statistics tend to emphasize offensive performance since there are not nearly as many discrete defensive factors to record in a box score as there are offensive factors. As such, metrics like PER can be biased against defensive specialists. It is re-assuring, then, to see that Impact Score does not appear to be as biased against defensive players as PER. 

It is important to note that the fact that Shumpert and Iguodala have much larger Impact Scores than Lopez and 

Irving does not mean that Shumpert and Iguodala are inherently better players than Lopez and Irving. Rather, it means that Shumpert’s and Iguodala’s performances helped their teams much more than Irving’s or Lopez’s. One explanation for the discrepancies between Lopez and Irving’s Impact Scores and PERs could be coaching decisions. The fact that Lopez and Irving were accumulating impressive individual statistics without improving their respective teams’ chances of winning suggests that their coaches may not have been playing them at opportune times for their teams. In this way, when taken together with a metric like PER, Impact Score can provide a more complete accounting and evaluation of a player’s performance. 

**64** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

### **5.2  Year-to-year correlation of Impact Score** 

A natural question to ask about any player evaluation metric is how stable it is year-to-year. In other words, to what extent can we predict how a player ranks with respect to one metric in a season given his ranking in a previous season. Using play-by-play data from the 2012–2013 regular season, we can fit a model similar to that in Equation 2 and compute each player’s Impact Score for that season. There were 389 players who played in both the 2012–2013 and 2013–2014 seasons and Figure 11 plots there players’ 2012– 2013 Impact Scores against their 2013–2014 Impact Scores. 

We observe that the correlation between 2012–2013 and 2013–2014 Impact Score is 0.242, indicating a rather moderate positive trend. We notice, however, that there are several players whose Impact Scores in 2012–2013 are much different than their Impact Scores in 2013–2014. For instance, Iman Shumpert’s and Dirk Nowitzki’s Impact Scores increased dramatically between the two season. At the other end of the spectrum, players like Larry Sanders and Tyson Chandler displayed sharp declines in their Impact Scores. On further inspection, we find that all of these players missed many games due to injury in the seasons when they had lower Impact Scores. Upon their return from injury, they played 

fewer minutes while they continued to rehabilitate and readjust to playing at a high-level. In short, the variation in the _contexts_ in which these players performed is reflected in the the season-to-season variation in their Impact Score. 

Because it is context-dependent, we would not expect the year-to-year correlation for Impact Scores to be nearly as high as the year-to-year correlation for PER (correlation of 0.75), which attempts to provide a context-agnostic assessment of player contribution. Nevertheless, we may still assess the significance of the correlation we have observed using a permutation test. To simulate the distribution of the correlation between 2012–2013 and 2013– 2014 Impact Scores, under the hypothesis that they are independent, we repeatedly permute the observed 2013– 2014 Impact Scores and compute the correlation between these permuted scores and the observed 2012–2013 Impact Scores. Figure 12 shows a histogram of this null distribution based on 500,000 samples. 

We find that the observed correlation is significantly different than zero. This indicates that even though Impact Scores are inherently context-dependent, a player’s Impact Score is one season is moderately predictive of his Impact Score in the next, barring any significant changes in the contexts in which he plays. 



**Figure 11:** Impact Scores in 2012 and 2013. 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **65** 



<!-- Start of picture text -->
Null distribution of correlation between 2012 and 2013 Impact Scores<br>8<br>0.242<br>6<br>4<br>2<br>0<br><!-- End of picture text -->

**Figure 12:** Null distribution of correlation between 2012–2013 and 2013–2014 Impact Scores under the hypothesis that they are independent. The observed correlation of 0.242 is shown in red. 

### **5.3  Multi-season impact score** 

Though the context in which players perform between seasons can be highly variable, it is arguably more stable across multiple seasons. In light of this, we can re-fit our models using all of the play-by-play data from 2008–2009 to 2010–2011 and from 2011–2012 to 2013–2014, and estimated each player’s partial effect separately in both time period. Note that for each season considered, the change in win probability during a shift was estimated using data from all prior seasons. 

Somewhat surprisingly, we find that the posterior standard deviations of the player partial effects estimated over multiple seasons is not substantially smaller than when we consider one seasons at a time, despite having much more data. For instance, the posterior standard deviation of LeBron James’ partial effect in the 2013–2014 season is 0.0035 while it is 0.002 over the three season span from 2008–2009 to 2010–2011. Table 4 shows the top 10 Impact Scores over these two three-season periods. 

Quite clearly, LeBron James stands out rather prominently, especially in the 2008–2010 time period, as far and away the most impactful player over those three seasons. We note that James’ 2013–2014 Impact Score is much less than either of his multi-season Impact Scores. This indicates that while James may have been most impactful player over the course of several seasons, in that particular season, he was not as impactful. 

**Table 4:** Impact Score computed over three seasons windows. 

|**2008–2009 to 2010–2011**|**2011–2012 to 2013–2014**|
|---|---|
|LeBron James (5.400)|LeBron James (3.085)|
|Dirk Nowitzki (3.758)|Chris Paul (3.041)|
|Chris Paul (3.247)|Amir Johnson (2.982)|
|Dwyane Wade (2.948)|Stephen Curry (2.919)|
|LaMarcus Aldridge (2.775)|Andre Iguodala (2.805)|
|Steve Nash (2.770)|Mike Dunleavy (2.790)|
|Tim Duncan (2.679)|Dirk Nowitzki (2.733)|
|Matt Bonner (2.178)|Kevin Durant (2.426)|
|Kevin Garnett (2.125)|Paul George (2.332)|



Figure 13 shows the Impact Scores from 2011 to 2013 plotted against the Impact Scores 2008–2010. The correlation between these scores is 0.45, which is larger than the year-to-year correlation in Impact Score. The players with discordant single season Impact Scores highlighted in Figure 11 were all recovering from significant injuries that required them to miss many games and play restricted minutes for a good portion of the season. Since there are generally few injuries which span significant portions of multiple seasons, the context in which players perform tend to stabilize across several seasons. 

## **6  Lineup comparison** 

As a further study of the full covariance structure of θ and τ, we can compare how different five-man lineups 



**Figure 13:** Impact Scores computed over 2008–2010 and 2011–2013. 

**66** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

match up against each other. To simulate the posterior distribution of a five-man lineup’s effect on its team’s win probability, we simply sum the corresponding entries of each posterior sample of θ. With these samples, we can compute each lineup’s Impact Score just as we did for player’s in Section 5: we divide the posterior mean of the lineup’s effect by the posterior standard deviation of its effect. Table 5 shows the 10 lineups with the largest Impact Scores. 

We can also simulate draws from the posterior predictive distribution of the change in home team win probability for each home/away configurations of two five-man lineups using our posterior samples of (μ, θ, τ, σ<sup>2</sup> ). For a specific home/away configuration, we construct vectors of signed indicators, **P**<sup>*</sup> and **T**<sup>*</sup> , to encode which players and teams we are pitting against one another. For each sample of (μ, θ, τ, σ<sup>2</sup> ) we compute 



where _z_ ~ _N_ (0, 1), to simulate a sample from the posterior predictive distribution of the change in the home team’s win probability for the given matchup. In particular, we consider pitting the lineup with the largest Impact Score (Stephen Curry, Klay Thompson, Andre Iguodala, David Lee, Andrew Bogut) against three different lineups: the lineup with second largest Impact Score (Chris Paul, J.J. Redick, Matt Barnes, Blake Griffin, DeAndre Jordan), the lineup with the smallest Impact Score (Eric Maynor, Garrett Temple, Chris Singleton, Trevor Booker, Kevin Seraphin), and the lineup with the median Impact Score (Donald Sloan, Orlando Johnson, Solomon Hill, Lavoy Allen, Roy Hibbert). The median lineup’s Impact Score is the median of all lineup Impact Scores. Figure 14 shows the posterior predictive densities of the change in win probability in a single shift when the lineup with largest Impact Score plays at home. 

Unsurprisingly, when the lineup with largest Impact Score is pitted against the lineup with smallest Impact Score, the predicted change in win probability is positive about 65% of the time and is greater than 0.1 just over 23% of the time. It is also reassuring to see that the density corresponding to the matchup against the median lineup lies between the two extremes considered. Rather surprisingly, however, we find that when the lineup with largest Impact Score is pitted against the lineup with second largest Impact Score, the change in win probability is negative about 55% of the time. We find that posterior mean effect of the Paul-Reddick-Barnes-Griffin-Jordan lineup is 0.0166 while the posterior mean effect of the Curry-Thompson-Iguodala-Lee-Bogut lineup is 0.0150. The difference in Impact Score is driven by the difference in the posterior standard deviation of each lineup’s effect (0.0050 for Curry-Thompson-Iguodala-Lee-Bogut and 0.0058 for Paul-Reddick-Barnes-Griffin-Jordan). Because of the disparity in playing time (780.25 min vs 88.57 min), we are less uncertain about the effect of the CurryThompson-Iguodala-Lee-Bogut lineup and the additional certainty makes up for the smaller average effect. This highlights an important feature of Impact Score: it tries to balance the estimated effect against the uncertainty in this estimate. 

At this point, it is worth nothing that while the change in win probability over the course of any shift is constrained to lie between –1 and 1, none of our modeling assumptions restrict the range of the predicted change in win probability in any of the match-ups considered to lie in this range. In particular, since we have a conditional normal model, it could be the case that σ _z_ term pushes our prediction outside of the interval [–1, 1]. In light of this, it is reassuring to find that the support of posterior predictive distributions of the change in win probability in all of the match-ups considered is in [–0.4, 0.4]. 

**Table 5:** Lineups with the largest impact score. 

||**Lineup**|**Impact Score**|**Minutes**|
|---|---|---|---|
|1|Stephen Curry, Klay Thompson, Andre Iguodala David Lee, Andrew Bogut|2.98|780.25|
|2|Chris Paul, J.J. Redick, Matt Barnes Blake Griffin, DeAndre Jordan|2.88|88.57|
|3|Stephen Curry, Klay Thompson, Andre Iguodala David Lee, Jermaine O’Neal|2.82|31.75|
|4|George Hill, Lance Stephenson, Paul George David West, Roy Hibbert|2.58|1369.38|
|5|Mario Chalmers, Ray Allen, LeBron James Chris Bosh, Chris Andersen|2.57|34.28|
|6|Patrick Beverley, James Harden, Chandler Parsons Terrence Jones, Dwight Howard|2.51|589.97|
|7|Mario Chalmers, Dwyane Wade, LeBron James Chris Bosh, Chris Andersen|2.46|26.2|
|8|C.J. Watson, Lance Stephenson, Paul George David West, Roy Hibbert|2.42|118.27|
|9|John Wall, Bradley Beal, Trevor Ariza Nene Hilario, Marcin Gortat|2.38|384.03|
|10|Patrick Beverley, James Harden, Chandler Parsons Donatas Motiejunas, Dwight Howard|2.38|65.58|



S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **67** 



<!-- Start of picture text -->
5<br>Lowest Impact Score<br>Median Impact Score<br>2nd largest Impact Score<br>4<br>3<br>2<br>1<br>0<br><!-- End of picture text -->

**Figure 14:** Posterior predictive density in win probability of the lineup with the largest impact score matched up with three other lineups. 

## **7  Discussion** 

In this paper, we have estimated each NBA player’s effect on his team’s chances of winning, after accounting for the contributions of his teammate and opponents. By focusing on win probability, our model simultaneously downweights the importance of performance in low-leverage (“garbage time”) and up-weights the importance of highleverage performance, in marked contrast to existing measures like PER which provide context-agnostic assessments of player performance. Since our estimates of player effects depend fundamentally on the context in which players perform, our estimates and derived metrics are necessarily retrospective in nature. As a result, our results do not display nearly as high of a year-to-year correlation as other metrics. We would argue, however, that the somewhat lower year-to-year repeatability of our derived metrics are offset by the fact that they provide a much more complete accounting of how a player helped their teams win in a particular season. When taken together with a metric like PER, our results enable us to determine whether the performance of a player who recorded impressive box-score totals actually improved his team’s chances of winning the game. Ultimately, our model and derived metrics serve as a complement to existing measures of player performance and enables us to contextualize individual performances in a way that existing metrics alone cannot. 

We have introduced a new method for estimating the probability that a team wins the game as a function of its lead and how much time is remaining. Our win probability estimates can be viewed as a middle-ground between the empirical estimates, which display extreme discontinuity due to small sample size issues, and existing probit regression model estimates, which do not seem to fit the empirical observations well. Though our win probability estimates are generally quite precise, our choice of smoothing window [ _T_ – 3, _T_ + 3]  × [ _L_ – 2, _L_ + 2] is admittedly rather simplistic. This is most pronounced near the end of the game, when a single possession can swing the outcome and it less reasonable to expect the win probability when leading by 2 points is similar to the win probability when trailing by 2 points. To deal with this, one could let the window over which we aggregate games vary with both time and lead instead of using a fixed window. We also note that the choice of a hard threshold of _L_ = ±20 in determining the number of pseudo-wins, α _T_ , _L_ , and pseudo-losses, β _T_ , _L_ , to add is arbitrary and we could just as easily have selected _L_ = ±25 or ±30. Alternatively, α _T_ , _L_ and β _T_ , _L_ could be selected at random from a specified distribution depending on the time and lead or we can place a further hyper-prior on (α _T_ , _L_ , β _T_ , _L_ ). Unfortunately, estimates from the first approach may not be reproducible and explicitly computing the Bayes estimator of _pT_ , _L_ , in the second approach can be difficult. While a more carefully constructed prior can, in principle, lead to estimates that more accurately reflect our subjective beliefs about how win probability evolves, one must take care not to select a prior that can overwhelm the observed data. 

Looking at our win probability estimates, we find that a unit change in time corresponds to a smaller change in win probability than a unit change in lead, especially near the end of close games. This can introduce a slight bias against players who are frequently substituted into games on defensive possessions and taken out of the game on offensive possessions, since such players will not be associated with large changes in win probability. One way to overcome this bias is to account for which team has possession of the ball into our win probability estimates. In principle, it would be straightforward to include possession information into our win probability estimates: first we bin the games based on home team lead, time remaining, and which team has possession, and then we apply our estimation procedure twice, once for when the home team has possession and once for when the away team has possession. Our omission of possession information is driven largely by our inability to determine which team has possession on a second-by-second basis reliably due to errors in the order in which plays are recorded in the 

**68** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

play-by-play data we have used. In general, more sophisticated estimation of win probability remains an area of future exploration. 

Since our estimates of player effect are contextdependent, we have introduced leverage profiles as a way to determine which players’ partial effects are most directly comparable. Though we have not done so in this paper, one could use leverage profiles to cluster players based on the situations in which they play. This could potentially provide insight into how coaches use various players around the league and lead to a more nuanced understanding of each player’s role on his team. 

In keeping with the spirit of previous player-evaluation, we define two metrics, Impact Ranking and Impact Score, to determine a rank-ordering of players. Impact Ranking provides an in-team ranking of each player’s partial effect, allowing us to determine whether a player’s salary is commensurate with his overall contribution to his team’s chances of winning games. Impact Score balances a player’s estimated effect against the uncertainty in our estimate to generate a league-wide rank-ordering. 

We have found that any individual player’s effect on his team’s chances of winning during a single shift is small, generally less than 1%. We moreover have found rather considerable overlaps in the posterior distribution of player partial effects. This suggests there is no single player who improves his team’s chances of winning significantly more than the other players. That said, we are still able to distinguish clear differences in players’ impacts. Somewhat surprisingly, we find that Dirk Nowitzki had a larger impact on his team’s chances of winning that more prominent players like Kevin Durant and LeBron James. We also found that Durant and James’ impact were virtually indistinguishable. This is not to suggest that Nowitzki is a better or more talented player than Durant or James, per se. Rather, it indicates that Nowitzki’s performance was much more important to his team’s success than Durant’s or James’ performances were to their respective teams. 

There are several possible extensions and refinements to our proposed methodology. As mentioned earlier, our win probability estimation is admittedly simplistic and designing a more sophisticated procedure is an area for future work. It is also possible to include additional covariates in equation (2) to entertain two-way or threeway player interactions, in case there are any on-court synergies or mismatches amongst small groups of players. In its current form, Equation 2 does not distinguish the uncertainty in estimating the _yi_ ’s from the inherent variability in the change in win probability. It may be possible to separate these sources of variability by decomposing 

σ, though care must be taken to ensure identifiability of the resulting model. Finally, rather than focusing on each player’s overall impact, one could scale the predictors in Equation 2 by the shift length and re-fit the model to estimate each player’s per-minute impact on his team’s chances of winning. 

## **Appendix** 

As we discussed in Section 2, we have made several strong assumptions in specifying a Gaussian linear regression model. We now check and discuss the assumption that the errors in Equation 2 are Gaussian with constant variance. We also consider several transformations and alternative model specifications which could potentially align with these assumptions better than our original specification. In particular, we consider the following response variables, _y_<sup>(1)</sup> , _y_<sup>(2)</sup> and _y_<sup>(3)</sup> : 

–<sup>_y_</sup> _i_ (1) : our original response, the change in the win probability. –<sup>_y_</sup> _i_ (2) : the change in the log-odds of winning the game. Intuitively, this further down-weights the importance of low-leverage performance as a 5% change in win probability from 45% to 50% corresponds to a much larger change in the log-odds than a 5% change in win probability from 90% to 95%. 



mation of the shifted and re-scaled change in win probability. 

Figure 15 shows histograms of these response variables, along with a histogram of our original response, change in win probability. 

We notice that the distribution of _y_<sup>(1)</sup> and the distribution of _y_<sup>(3)</sup> are similar: both are rather tightly concentrated near 0 and 0.622, respectively and are more or less symmetric. We also observe that _y_<sup>(3)</sup> is much less variable than _y_<sup>(1)</sup> . Interestingly, we see in Figure 15(B), that the change in the log-odds of winning is slightly more heavytailed than these other distributions. In particular, we see that in about 2% of all shifts, the absolute value of the change in the log-odds of winning exceeds 5. These correspond to shifts in which there was a very large swing in the home team’s win probability during a given shift. For example, in the penultimate shift of the March 16, 2014 game between the Miami Heat and the Houston Rockets, the Heat went from trailing by 5 points with 6:13 left to leading by 9 points with a few seconds left. In doing so, 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **69** 



**Figure 15:** Histogram of _y_<sup>(1)</sup> (A), _y_<sup>(2)</sup> (B), and _y_<sup>(3)</sup> (C). 

the Heat increased their win probability from 22% to 98%, corresponding to a change in the log-odds of winning of about 5.86. Given the fact that for the vast majority of shifts that the change in win probability and the change in the log-odds of winning the game were very close to 0 (indicated by the large “spikes” in the histograms near 0) and the fact that we have imposed rather strong shrinkage on our player effects, we would not expect our model to be able to estimate such a large change in the log-odds reliably. This is borne out in the residual plot, show in Figure 16(B): these shifts had residuals near ±5. To find the fitted values in Figure 16, we first simulated 1000 

posterior draws of the conditional expectation function _E_ [ _yi_ ( ⋅) | **P** _i_ , **T** _i_ ] = **P** _i_ ⊤θ + **T** _i_ ⊤τ using our simulated posterior draws of θ and τ and then took the average. It is important to note that because of the regularization, the fitted values and residuals are biased so we do not expect that they will be Gaussian. 

We note that Figure 16(A) and (C) are very similar in shape, though we note that the residuals in (C) are much smaller. This is not particularly surprising, since the variance of _y_<sup>(3)</sup> is much smaller than the variance of _y_<sup>(1)</sup> . Just like we might in a standard least squares regression problem, we can form normal quantile plots of these residuals. It is important to note, however, that the residuals are not unbiased estimators of the error terms because of the regularization. Nevertheless, it may still be desirable to consider an alternative model specification in which the distribution of the resulting residuals is much closer to Gaussian than our original model. Figure 17 shows the resulting normal quantile plots. As anticipated, we see that none of the residual plots display the linear trend characteristic of Gaussian distributions. Interestingly, we also observe that the residuals corresponding to _y_<sup>(2)</sup> seem decidedly less Gaussian and the residuals corresponding to _y_<sup>(3)</sup> appear to be similar to our original residuals. In light of this, we do not find the suggested transformations particularly compelling, in terms of aligning with our original modeling assumptions. 

We now consider the issue of homoscedasticity. Once again, we note that we are assuming that, conditional on the players on the court, the variance of the change in win probability is constant. Since we only observe a handful of observations with the same 10 players on the court, we cannot check this assumption prior to fitting our model. Still, it is reasonable to suspect that the variance of _yi_ depends on the win probability at the start of the shift. Figure 18 shows box plots of the change in win probability binned according to the starting win probability of the shift, along with the standard deviation of the observations in each binned. 



<!-- Start of picture text -->
A y (1) B y (12) C y (13)<br>0.5 5 0.05<br>0 0 0<br>–0.05<br>–0.5 –5<br>–0.10<br>Residuals Residuals Residuals<br><!-- End of picture text -->

**Figure 16:** Residuals plotted against fitted variable for the original model, the log-odds model, and the inverse logit model. 

**70** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 



<!-- Start of picture text -->
0.5 5 0.05<br>0 0 0<br>–0.05<br>–0.5 –5<br>–0.10<br>–4 –2 0 2 4 –4 –2 0 2 4 –4 –2 0 2 4<br>Theoretical quantiles Theoretical quantiles Theoretical quantiles<br>Sample quantiles Sample quantiles<br><!-- End of picture text -->

**Figure 17:** Normal quantile plots of residuals from modeling _y_<sup>(1)</sup> (A), _y_<sup>(2)</sup> (B), _y_<sup>(3)</sup> (C). 



<!-- Start of picture text -->
1.0<br>0.5<br>0<br>–0.5<br>–1.0<br><!-- End of picture text -->

**Figure 18:** Change in win probability binned according to the starting win probability of the shift. Since win probability is constrained to the interval [0,1], as the win probability at start of the shift increases, the distribution of the change in win probability shifts from right-skewed to left-skewed. 

We see immediately that the binned standard deviations are not constant, indicating that the variance of _y_<sup>(1)</sup> does depend on the starting win probability. However, we see that this dependence really only manifests itself when the starting win probability is close to 0 or 1. It is worth mentioning that this dependence in and of itself does not invalidate our initial assumption that the variance of _y_<sup>(1)</sup> conditional on the players on the court is constant. However, it does suggest that we try re-weighting the response and predictors in Equation 2 so that the binned standard deviations of the re-weighted response are constant. This is similar to what we might do in a weighted least squares regression problem. We consider three reweighting schemes: 

   - Re-scale so that the binned standard deviations are all 1. This magnifies the response and predictors for all shifts. Denote the new response variable _y_<sup>(4)</sup> . 

- 

   - Re-scale so that the binned standard deviations are all 0.03. This shrinks the response and predictors for all high-leverage shifts but leaves the observations from low-leverage shifts relatively unchanged. Denote the new response variable _y_<sup>(5)</sup> . 

- 

   - Re-scale so that the binned standard deviations are all 0.12. This magnifies the response and predictors for all low-leverage shifts but leaves the observations from high-leverage shifts relatively unchanged. Denote the re-scaled response variable _y_<sup>(6)</sup> . 

- 



<!-- Start of picture text -->
A 0.4<br>0.3<br>0.2<br>0.1<br>0<br>–20 –15 –10 –5 0 5 10<br>y (4)<br>B 15<br>10<br>5<br>0<br>–0.6 –0.4 –0.2 0 0.2<br>y (5)<br>C 3<br>2<br>1<br>0<br>Density<br>Density<br>Density<br><!-- End of picture text -->

**Figure 19:** Histograms for _y_<sup>(4)</sup> , _y_<sup>(5)</sup> , and _y_<sup>(6)</sup> . 

S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning **71** 



<!-- Start of picture text -->
10<br>0.2 1<br>5<br>0 0 0<br>–5<br>–0.2 –1<br>–10<br>–15 –0.4 –2<br>–20<br>Residuals Residuals<br><!-- End of picture text -->

**Figure 20:** Residuals resulting from modeling _y_<sup>(4)</sup> , _y_<sup>(5)</sup> , _y_<sup>(6)</sup> . 

Figure 19 shows histograms of the three re-scaled responses and Figure 20 show the residuals that arise from fitting the three re-scaled models. Though it is not immediately apparent in Figure 20, we observe rather extreme values of _y_<sup>(4)</sup> like –22.62, mainly corresponding to late-game shifts during which the win probability changed dramatically. We find that _y_<sup>(5)</sup> and _y_<sup>(6)</sup> are somewhat more tightly concentrated near 0 than is _y_<sup>(1)</sup> . 

Figure 20 plots the residuals against the fitted values from the re-scaled models. Once again, these residuals are biased, so we do not expect them to resemble the residuals plots obtained in standard least squares regression problems. The noticeable negative trend, seen especially in Figure 20(A) and (C), is a good indication of the bias introduced by regularization. It is interesting that this bias is much more apparent after re-scaling the response and predictors than it was in our original model. 

Somewhat worryingly, we see that there is considerable variation in the residuals when the fitted value is near zero. This is in marked contrast to Figure 16(A), in which we see more or less constant variation in the residuals for all possible fitted values. It appears that correcting for potential heteroscedasticity results in residuals that are even less well-behaved than in our original model. As a result, we do not see any of the re-weighted models as being necessarily better than our original model. 

## **References** 

Ballentine, A. 2014. “Kevin Durant Cements Himself as MVP Frontrunner with Triple-Double in Return.” (http://bleacherreport. com/articles/1936881). 

- Bashuk, M. 2012. “Using Cumulative Win Probability to Predict NCAA Basketball Performance.” in _Sloan Sports Analytics Conference_ , pp. 1–10. 

Buckley, Z. 2014. “LeBron James Reminding Everyone 2013 MVP Race is Far from Over.” (http://bleacherreport.com/ articles/1980464). 

- Cavan, J. 2014. “Are NBA Teams Overvaluing Stretch 4s in Free Agency.” (http://bleacherreport.com/articles/2122446). 

- Goldsberry, K. and E. Weiss. 2013. “The Dwight Effect: A New Ensemble of Interior Defense Analytics for the NBA.” in _Sloan Sports Analytics Conference_ , pp. 1–11. 

Gramacy, R. B., S. T. Jensen, and M. Taddy. 2013. “Estimating Player Contribution in Hockey with Regularized Logistic Regression.” _Journal of Quantitative Analysis in Sports_ 9:97–111. 

Hollinger, J. 2004. _Pro Basketball Forecast_ . 2004–05 ed. 

Washington, DC: Brassey’s Sports. 

- Ilardi, S. 2014. “The Next Big Thing: Real Plus-Minus.” (http:// espn.go.com/nba/story//id/10740818/introducing-real-plusminus). 

- Ilardi, S. and A. Barzilai. 2008. “Adjusted Plus-Minus Ratings: New and Improved for 2007–2008.” (http://www.82games.com/ ilardi2.htm). 

- Kyung, M., J. Gill, M. Ghosh, and G. Casella. 2010. “Penalized Regression, Standard Errors, and Bayesian Lassos.” _Bayesian Analysis_ 5:369–412. 

- Lapin, J. 2014. “Under-the-Radar Free-Agent Bargains Houston Rockets Must Consider.” (http://bleacherreport.com/articles/2069174). 

- Lindsey, G. 1963. “An Investigation of Strategies in Baseball.” _Operations Research_ 11:477–501. 

- Maymin, A., P. Maymin, and E. Shen. 2012. “How Much Trouble is Early Foul Trouble? Strategically Idling Resources in the NBA.” _International Journal of Sport Finance_ 7:324–339. 

- Mills, E. G. and H. D. Mills. 1970. “Player Win Averages: A Complete Guide to Winning Baseball Players.” in _The Harlan D. Mills Collection_ . 

- Park, T. and G. Casella. 2008. “The Bayesian Lasso.” _Journal of the American Statistical Association_ 103:681–686. 

- Pettigrew, S. 2015. “Assessing the Offensive Productivity of NHL Players Using In-Game Win Probabilities.” in _Sloan Sports Analytics Conference_ , pp. 1–9. 

- Rosenbaum, D. 2004. “Measuring How NBA Players Help Their Teams Win.” (http://www.82games.com/comm30.htm). 

- Stern, H. 1994. “A Brownian Motion Model for the Progress of Sports Scores.” _Journal of the American Statistical Association_ 89:1128–1134. 

**72** S.K. Deshpande and S.T. Jensen: Estimating an NBA player’s impact on his team’s chances of winning 

- Studeman, D. 2004. “The One About Win Probability.” (http://www. hardballtimes.com/the-one-about-win-probability/). 

- Thomas, A., S. L. Ventura, S. T. Jensen, and S. Ma. 2013. “Competing Process Hazard Function Models for Player Ratings in Ice Hockey.” _The Annals of Applied Statistics_ 

   - 7:1497–1524. 

- Tibshirani, R. 1996. “Regression Shrinkage and Selection via the Lasso.” _Journal of the Royal Statistical Society. Series B_ ( _Methodological_ ) 85:267–288. 

- Zou, H. and T. Hastie. 2005. “Regularization and Variable Selection via the Elastic Net.” _Journal of the Royal Statistical Society. Series B_ ( _Methodological_ ) 67:301–320. 


