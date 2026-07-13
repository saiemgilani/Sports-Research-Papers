<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Random Walk Picture of Basketball Scoring - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1416 

## Random Walk Picture of Basketball Scoring 

**Alan Gabel,** _Center for Polymer Studies and Department of Physics, Boston University, Boston_ 

**Sidney Redner,** _Center for Polymer Studies and Department of Physics, Boston University, Boston_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.11416 

## Random Walk Picture of Basketball Scoring 

Alan Gabel and Sidney Redner 

#### **Abstract** 

We present evidence, based on play-by-play data from all 6087 games from the 2006/07– 2009/10 seasons of the National Basketball Association (NBA), that basketball scoring is well described by a continuous-time anti-persistent random walk. The time intervals between successive scoring events follow an exponential distribution, with essentially no memory between different scoring intervals. By including the heterogeneity of team strengths, we build a detailed computational random-walk model that accounts for a variety of statistical properties of scoring in basketball games, such as the distribution of the score difference between game opponents, the fraction of game time that one team is in the lead, the number of lead changes in each game, and the season win/loss records of each team. 

**KEYWORDS:** scoring statistics, hot hand, stochastics, random walk, Poisson process, antipersistence 

**Author Notes:** We thank Guoan Hu for assistance with downloading and processing the data and Ravi Heugel for initial collaborations on this project. We also thank Aaron Clauset for helpful comments on an earlier version of the manuscript. This work was supported in part by NSF grant DMR0906504. 

Gabel and Redner: Random Walk Picture of Basketball Scoring 

### **1 Introduction** 

Sports provide a rich laboratory in which to study competitive behavior in a welldefined way. The goals of sports competitions are simple, the rules are well defined, and the results are easily quantifiable. With the recent availability of high-quality data for a broad range of performance metrics in many sports (see, for example, shrpsports.com), it is now possible to address questions about measurable aspects of sports competitions that were inaccessible only a few years ago. Accompanying this wealth of new data is a rapidly growing body of literature, both for scientific and lay audiences, on quantitative modeling and analysis of sports statistics (for general references, see, e.g., Mosteller (1997), Albert, Bennett, and Cochran (2005), Kubatko, Oliver, Pelton, and Rosenbaum (2007), Albert and Koning (2008), Glickman and Evans (2009), Arkes and Martinez (2011)). 

In this spirit, our investigation is motivated by the following simple question: can basketball scoring be described by a random walk? To answer this question we analyze play-by-play data for four seasons of all National Basketball Association (NBA) games. Our analysis indicates that a simple random-walk model successfully captures many features of the observed scoring patterns. We focus on basketball primarily because there are many points scored per game — roughly 100 scoring events in a 48-minute game — and also many games in a season. The large number of scoring events allows us to perform a meaningful statistical analysis. 

Our random walk picture addresses the question of whether sports performance metrics are determined by memory-less stochastic processes or by processes with long-time correlations (Gilovich, Vallone, and Tversky (1985), Miller and Weinberg (1991), Gould (1996), Dyte and Clarke (2000), Everson and GoldsmithPinkham (2008)). To the untrained eye, streaks or slumps — namely, sustained periods of superior or inferior performances — seem so unusual that they ought to have exceptional explanations. This impression is at odds with the data, however. Impartial analysis of individual player data in basketball has discredited the notion of a ‘hot hand’ (Gilovich et al. (1985), Ayton and Fischer (2004)). Rather, a player’s shooting percentage is independent of past performance, so that apparent streaks or slumps are simply a consequence of a series of random uncorrelated scoring events. Similarly, in baseball, teams do not get ‘hot’ or ‘cold’ (Vergin (2000), Sire and Redner (2009)); instead, the functional forms of winning and losing streak distributions 

In this work, we focus on the statistical properties of scoring during each basketball game. The scoring data are consistent with the scoring rate being described by a continuous-time Poisson process. Consequently, apparent scoring bursts or scoring droughts arise from Poisson statistics rather than from a temporally correlated process. Our main hypothesis is that the evolution of the score 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

difference between two competing teams can be accounted by a continuous-time random walk. 

This idealized picture of random scoring has to be augmented by two features — one that may be ubiquitous and one idiosyncratic to basketball. The former is the existence of a weak linear restoring force, in which the leading team scores at a slightly lower rate (conversely, the losing team scores at a slightly higher rate). This restoring force seems to be a natural human response to an unbalanced game — a team with a large lead may be tempted to coast, while a lagging team likely plays with greater urgency. A similar “rich get poorer” and “poor get richer” phenomenon was found in economic competitions where each interaction has low decisiveness (Durham, Hirschleifer, and Smith (1998), Garfinkel and Skaperdas (2007)). Such a low payoff typifies basketball, where the result of any single play is unlikely to determine the outcome of the game. The second feature, idiosyncratic to basketball, is _anti-persistence_ , in which a score by one team is more likely to be followed by a score from the opponent because of the change in ball possession after each score. By incorporating these attributes into a continuous-time random-walk description of scoring, we build a computational model for basketball games that reproduces many statistical features of basketball scoring and team win/loss records. 

### **2 Scoring Rate** 

Basketball is played between two teams with players each. Points are scored by making baskets that are each worth 2 points (typically) or 3 points. Additional single-point baskets can occur by foul shots that are awarded after a physical or technical foul. The number of successive foul shots is typically 1 or 2, but more can occur. The duration of a game is 48 minutes (2880 seconds). Games are divided into four 12-minute quarters, with stoppage of play at the end of each quarter. The flow of the game is ostensibly continuous, but play does stop for fouls, time-outs, and out-of-bounds calls. An important feature that sets the time scale of scoring is the 24-second clock. In the NBA, a team must either attempt a shot that hits the rim or score within 24 seconds of gaining possession of the ball, or else possession is forfeited to the opposing team. At the end of the game, the team with the most points wins. 

We analyze play-by-play data from 6087 NBA games for the 2006/07– 2009/10 seasons, including playoff games (see www.basketballvalue.com); for win/ loss records we use a larger dataset for 20 NBA seasons (www.shrpsports.com). To simplify our analysis, we consider scoring only until the end of regulation time. Thus every game is exactly 48 minutes long and some games end in ties. We omit 

2 

Gabel and Redner: Random Walk Picture of Basketball Scoring 

overtime to avoid the complications of games of different durations and the possibility that scoring patterns during overtime could be different from those during regulation time. 

We focus on what we term _scoring plays_ , rather than individual baskets. A scoring play includes any number of baskets that are made with no time elapsed between them on the game clock. For example, a 2-point play could be a single field goal or two consecutive successful foul shots; a 3-point play could be a normal field goal that is immediately followed by a successful foul shot, or a single successful shot from outside the 3-point line. High-value plays of 5 and 6 points involve multiple technical or flagrant fouls. Since they have negligible probability of occurence (Table 1), we will ignore them in our analysis. Consistent with our focus on scoring plays, we define the scoring rate as the number of scoring plays per second. This quantity is measured for each second of the game. For the 4 seasons of data, the average scoring rate is roughly constant over the course of a game, with mean value of 0.03291 plays/sec (Fig. 1). Averaging each quarter separately gives a scoring rate of 0.03314, 0.03313, 0.03243, and 0.03261 for first through fourth quarters, respectively. The scoring rate corresponds to 94.78 successful plays per game. Since there is, on average, 2.0894 points scored per play, each team has 99.018 points in an average game (Westfall (1990)). Parenthetically, the average scoring rate is constant from season to season, and equals 0.03266, 0.03299, 0.03284, 0.03315 for the 2006–07 to the 2009–10 seasons. 

|||Pointsper Play|Percentage|
|---|---|---|---|
|Pointsper Basket|Percentage|1 pt.<br>2 t|8.70%<br>7386%|
|1 pt.<br>2 pts.<br>3pts.|33.9%<br>54.6%<br>11.5%|ps.<br>3 pts.<br>4 pts.<br>5 pts.|.<br>17.28%<br>0.14%<br>0.023%|
|||6pts.|0.0012%|



Table 1: Point values of each basket (left) and each play (right) and their respective percentages. 

start and end of each quarter (Fig. 1(a)). During roughly the first 10 seconds of each quarter, scoring is unlikely because of a natural minimum time to make a basket after the initiation of play. Near the end of each of the first three quarters, the scoring rate first decreases and then sharply increases right at the end of the quarter. This anomaly arises because, within the last 24 seconds of the quarter, 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
0.08 0.2<br>1 st  Quarter<br>0.07 (a) (b)<br>2 nd  Quarter<br>0.06 0.15 3 rd  Quarter<br>0.05 4 th  Quarter<br>0.04 0.1<br>0.03<br>0.02 0.05<br>0.01<br>0 0<br>0 500 1000 1500 2000 2500 −30 −20 −10 0 10 20 30<br>Time [s] Time After Quarter Ends [s]<br>Scoring Rate [plays/s] Scoring Rate [plays/s]<br><!-- End of picture text -->

Figure 1: (a) Average scoring rate as a function of time over all games in our dataset. (b) Rate near the change of each quarter; zero on the abscissa corresponds to the start/end of a quarter. 

teams may intentionally delay their shot until the last moment, so that the opponent has no chance for another shot before the quarter ends. However, there is only an increase in the scoring rate before the end of the game, possibly because of the urgent effort of a losing team in attempting to mount a last-minute comeback via intentional fouls. While these deviations from a constant scoring rate are visually prominent, they occur over a small time range near the end of each quarter. For the rest of our analysis, we ignore these end-of-quarter anomalies and assume that scoring in basketball is temporally homogeneous. 

In addition to temporal homogeneity, the data suggest that scoring frequency obeys a Poisson-like process, with little memory between successive scores (see also de Sa´a Guerra, Gonz´alez, Montesdeoca, Ruiz, Arjonilla-L´opez, and GarcaManso (2011)). To illustrate this property, we study the probability _P_ ( _t_ ) of time intervals between successive scoring plays. There are two natural such time intervals: (a) the interval _t_ e between successive scores of either team, and (b) the interval _t_ s between successive scores of the same team. The probability _P_ ( _t_ e) has a peak at roughly 16 seconds, which evidently is determined by the 24-second shot clock. This probability distribution decays exponentially in time over nearly the entire range of data (Fig. 2). Essentially the same behavior arises for _P_ ( _t_ s), except that the time scale is larger by an obvious factor of 2. When all the same-team time intervals are divided by 2, the distributions _P_ ( _t_ e) and _P_ ( _t_ s) overlap substantially. The long-time tails of both _P_ ( _t_ e) and 2 _P_ ( _t_ s/2) are proportional to the exponential function exp(− λ tail _t_ ), with rate λ tail = 0.048 plays/sec. This value is larger than the actual scoring rate of 0.03291 plays/sec because scoring intervals of less than 10 seconds are common for the exponential distribution but are rare in real basketball games. Amusingly, the longest time interval in the dataset for which neither team 

4 

Gabel and Redner: Random Walk Picture of Basketball Scoring 



<!-- Start of picture text -->
−3<br>−4<br>−4<br>−5<br>−5<br>−6<br>−6<br>−7<br>−7<br>−8<br>−8<br>−9<br>−9<br>−10<br>−10<br>−11<br>−11<br>−12<br>0 50 100 150 200 0 100 200 300 400<br>te [s] ts [s]<br>ln(P) ln(P)<br><!-- End of picture text -->

Figure 2: Probability distributions of time intervals between successive scores for either team, _P_ ( _te_ ) vs. _t_ e (a), and for the same team, _P_ ( _t_ s) vs. _t_ s (b). The line is the least-squares linear fit of ln( _P_ ) vs. _t_ over the range _t_ e > 30 sec and _t_ s > 60 sec and corresponds to a decay rate λ tail = 0.048 and 0.024, respectively. 

scored was 402 seconds, while the longest interval for which a single team did not score was 685 seconds. 

It is instructive to compare the distribution of total score in a single game to that of a Poisson process. Under the assumption that scores occur at the empiricallyobserved rate of λ = 0.03291 plays/sec, the probability that a game has _k_ scoring plays is given by the Poisson distribution, Prob(# plays = _k_ ) = _k_<sup><u>1</u></sup> !<sup>(λ</sup><sup>_T_)</sup><sup>_ke_−λ</sup><sup>_T_,</sup> where _T_ = 2880 sec. is the game duration. Since the average score of each play is _~~s~~_ = 2.0894 points, a game that contains _k_ scoring plays will have a total score of approximately _S_ = _~~sk~~_ . By changing variables from _k_ to _S_ in the above Poisson distribution, the probability that a game has a total score _S_ is 



This probability agrees reasonably with game data (Fig. 3), considering that (1) is derived using only the mean scoring rate and mean points per play. By including the different point values for each play, the resulting score distribution would broaden. Furthermore, if we impose a cutoff in the probability of short scoring intervals (see Fig. 2) the total score distribution of Fig. 3 would shift slightly to the left which would bring the model prediction closer to the data. 

An important aspect of the time intervals between successive scoring events is that they are weakly correlated. To illustrate this feature, we take the time-ordered list of successive scoring intervals _t_ 1, _t_ 2, _t_ 3,..., for all games and compute the n-lag 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
0.02<br>0.015<br>0.01<br>0.005<br>0<br>140 160 180 200 220 240 260 280<br>Total Score [points]<br>Probability<br><!-- End of picture text -->

Figure 3: Probability Prob(score = _S_ ) for a total score _S_ in a single game. Circles are the data, and the solid curve is the Poisson distribution (1). 

correlation function (Box and Jenkins (1976)) 



Thus _n_ = 1 gives the correlation between the time intervals between successive scores, _n_ = 2 to second-neighbor score intervals, etc. For both the intervals _t_ e (independent of which team scored) and _t_ s (single team), we find that _C_ ( _n_ ) < 0.03 for _n_ ≥ 1. Thus there is little correlation between scoring events, suggesting that basketball scoring is a nearly memory-less process. Accordingly, scoring bursts or scoring droughts are nothing more than manifestations of the fluctuations inherent in a Poisson process of random and temporally homogeneous scoring events. 

### **3 Random-Walk Description of Scoring** 

We now turn to the question of _which_ team scores in each play to build a randomwalk description of scoring dynamics. After a given team scores, possession of the ball reverts to the opponent. This change of possession confers a significant disadvantage for a team to score twice in succession. On average, immediately after a score, the same team scores again with probability _q_ = 0.348, while the opponent scores with probability 0.652. This tendency for alternating scores is characteristic of an _anti-persistent_ random walk (Garc´ıa-Pelayo (2007)), in which a step in a given direction is more likely to be followed by a step in the opposite direction. 

6 

Gabel and Redner: Random Walk Picture of Basketball Scoring 

As we now discuss, this anti-persistence is a determining factor in the streaklength distribution. A streak of length _s_ occurs when a team scores a total of _s_ consecutive points before the opposing team scores. We define _Q_ ( _s_ ) as the probability for a streak to have length _s_ . To estimate this streak-length probability, note that since _~~s~~_ = 2.0894 points are scored, on average, in a single play, a scoring streak of _s_ points corresponds to _s_ ~~/~~ _~~s~~_ consecutive scoring plays. In terms of an anti-persistent _~~s~~_ random walk, the probability _Q_ ( _s_ ) for a scoring streak of _s_ points is _Q_ ( _s_ ) = _Aq_<sup>_s_</sup><sup>~~/~~</sup> where _A_ = _q_<sup>−1</sup><sup>~~/~~</sup> _~~s~~_ − 1 is the normalization constant. This simple form reproduces the observed exponentially decaying probability of scoring streaks reasonably accurately (Fig. 4). 



<!-- Start of picture text -->
−2 Q(s)=Aq s/2.1<br>Refined Model<br>−4 Game Data<br>−6<br>−8<br>−10<br>−12<br>0 5 10 15 20 25 30<br>Streak Length [points]<br>ln(Q)<br><!-- End of picture text -->

Figure 4: Probability _Q_ ( _s_ ) for a consecutive point streak of _s_ points (◦). The dashed _~~s~~_ line corresponds to _Q_ ( _s_ ) = _Aq_<sup>_s_</sup><sup>~~/~~</sup> , with _q_ = 0.348 and _A_ the normalization constant. The solid line corresponds to a refined model that incorporates the different probabilities of 1, 2, 3, and 4-point plays (see Eqs. (4) and (5)). 

the different probabilities for 1, 2, 3, and 4 point plays. Let _w_ α be the probability that a play is worth α points (Table 1) and let _vm_ be the value of the _m_<sup>th</sup> play in a streak. A scoring sequence { _v_ 1,... _vn_ } that results in _s_ points must satisfy the constraint ∑<sup>_n_</sup> _k_ =1<sup>_vk_=</sup><sup>_s_,where</sup><sup>_n_isthenumberofplaysinthesequence.The</sup> probability for this streak is given by ∏<sup>_n_</sup> _k_ =1<sup>_wv_</sup> _k_<sup>.Because a streak of length</sup><sup>_s_points</sup> involves a variable number of plays, the total probability for a streak of _s_ points is 



7 

_Submission to Journal of Quantitative Analysis in Sports_ 

Here the inner sum is over all allowed sequences { _vk_ } of _n_ consecutive pointscoring events, and the factor _q_<sup>_n_−1</sup> (1 − _q_ ) gives the probability for a streak of exactly _n_ plays. For example, the probabilities for streaks up to _s_ = 4 are: 



A direct calculation of these probabilities for general _s_ becomes tedious for large _s_ , but we can calculate them recursively for _s_ > 4. To do so, we decompose a streak of _s_ points as a streak of _s_ − _vn_ points, followed by a single play that of _vn_ points. The probability of such a play is _qwvn_ . Because the last play can be worth 1, 2, 3, or 4 points, the probability for a streak of length _s_ is given recursively by 



Using Eqs. (4) and (5), we may calculate _Q_ ( _s_ ) numerically for any _s_ . The resulting probabilities closely match the empirical data (Fig. 4), suggesting that streaks arise only from random statistical fluctuations and not from teams or individuals getting hot or cold. 

Another intriguing feature of basketball games is that the scoring probability at any point in the game is affected by the current score: the probability that the winning team scores decreases systematically with its lead size; conversely, the probability that the losing team scores increases systematically with its deficit size (Fig. 5). This effect is well-fit by a linear dependence of the bias on the lead (or deficit) size. (Such a linear restoring force on a random walk is known in the physics literature as the Ornstein-Uhlenbeck model (Uhlenbeck and Ornstein (1930)). For basketball, the magnitude of the effect is small; assuming a linear dependence, a least-squares fit to the data gives a decrease in the scoring rate of 0.0022 per point of lead. Naively, this restoring force originates from the winning team ‘coasting’ or the losing team increasing its level of effort. 

We now build a random-walk picture for the time evolution of the difference in the score ∆ ( _t_ ) between two teams. Each game starts scoreless and ∆ ( _t_ ) subsequently increases or decreases after each scoring play until the game ends. The trajectory of ∆ ( _t_ ) versus _t_ qualitatively resembles the position of a random walk as a function of time. Just as for random walks, the statistically significant quantity is σ<sup>2</sup> ≡ var( ∆ ( _t_ )), the variance in the score difference, averaged over many games. For a classic random walk, σ<sup>2</sup> = 2 _Dt_ , where _D_ is the diffusion coefficient. As illustrated in Fig. 6, σ<sup>2</sup> does indeed grow nearly linearly with time for NBA 

8 

Gabel and Redner: Random Walk Picture of Basketball Scoring 



<!-- Start of picture text -->
0.6<br>0.55<br>0.5<br>0.45<br>0.4<br>0.35<br>−40 −20 0 20 40<br>Lead Size [points]<br>Scoring Probability<br><!-- End of picture text -->

Figure 5: Data for the probability _S_ ( _L_ ) that a team will score next given a lead _L_ (◦). The line is the least-squares linear fit, _S_ ( _L_ ) = 2<sup><u>1</u>−0.0022</sup><sup>_L_.</sup> 

basketball games, except for the last 2.5 minutes of the game; we will discuss this latter anomaly in more detail below. A least-squares linear fit to all but the last 2.5 minutes of game data gives σ<sup>2</sup> = 2 _D_ fit _t_ , with _D_ fit = 0.0363 points<sup>2</sup> /sec. 

We may also independently derive an effective diffusion constant from the time evolution of the score difference from basic parameters of an anti-persistent random walk. For such a walk, two successive scores by the same team correspond to two random-walk steps in the same direction. As mentioned above, we found that the probability of this outcome is _q_ = 0.348. Conversely, the probability for a score by one team immediately followed with a score by the opposing team is 1 − _q_ . Let us define _P_ ( ∆ , _t_ ) as the probability that the score difference equals ∆ at time _t_ . Using the approach of Garc´ıa-Pelayo (2007) for an anti-persistent random walk, _P_ ( ∆ , _t_ ) obeys the recursion 



where ℓ is the point value of a single score. To understand this equation, we rewrite it as 



The second factor in (6b) corresponds to two scores by alternating teams; thus the score difference equals ∆ at time _t_ − τ and again at time _t_ + τ . This event occurs with probability 1− _q_ . The terms in the square bracket correspond to two successive scores by one team. Consequently a score difference of ∆ ± 2ℓ at time _t_ − τ evolves 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
200<br>150<br>100<br>50<br>0<br>0 500 1000 1500 2000 2500<br>Time [s]<br>2]<br> [points<br>2<br>σ<br><!-- End of picture text -->

Figure 6: Variance in the score difference, σ<sup>2</sup> , as a function of time. The line σ<sup>2</sup> = 2 _D_ fit _t_ is the least-squares linear fit, excluding the last 2.5 minutes of data. The variance reaches its maximum 2.5 minutes before the end of the game (dashed line). 

to a score difference ∆ at time _t_ + τ . Thus the corresponding walk must be at ∆ ± ℓ at time _t_ but _not_ at ∆ at time _t_ − τ . 

Expanding _P_ ( ∆ , _t_ ) _t_ and second order in ∆ yields 



where _D_ ap is the effective diffusion associated with an anti-persistent random walk. Notice that for _q_ = 2<sup><u>1</u>thescoreevolutionreducestoasimplesym-</sup> metric random walk, for which the diffusion coefficient is _D_ ap = ℓ<sup>2</sup> /(2 τ ). Substituting in the values from the game data _q_ = 0.348 (probability for the same team to score consecutively), ℓ = 2.0894 (the mean number of points per scoring event), and τ = 30.39 seconds (the average time between successive scoring events), we obtain 



This diffusion is satisfyingly close to the value _D_ fit = 0.0363 from the empirical time dependence σ<sup>2</sup> , and suggests that an anti-persistent random-walk accounts for its time dependence. We attribute the small discrepancy in the two estimates of the diffusion coefficient to our neglect of the linear restoring force in the diffusion equation (7), 

Thus far, we have treated all teams as equivalent. In fact, the of team strengths on basketball scoring is not decisive — weaker teams can (and do) 

10 

Gabel and Redner: Random Walk Picture of Basketball Scoring 



<!-- Start of picture text -->
0.8<br>t=48min (final)<br>0.7 t=45.5min<br>t=12min<br>0.6<br>Model at t=45.5min<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>−3 −2 −1 0 1 2 3<br>∆/�2Dfitt<br>Probability<br><!-- End of picture text -->

Figure 7: Probability for a given score difference at the end of the quarter, after 45.5 minutes, and at the end of the game. The abscissa is rescaled by linear fit of variance, σ<sup>2</sup> ≈ 2 _D fitt_ (see Fig. 6). The dashed curve is the distribution from simulated games with team strength variance, σ _X_<sup>2= 0.0083 (see Sec. 4).</sup> 

win against better teams. The data show that the winning team in any game has a better season record than the losing opponent with probability 0.6777. Thus within our random-walk picture, the underlying bias that arises from the disparity in the strengths of the two competing teams is masked by random-walk fluctuations. For a biased random walk with bias velocity _v_ and diffusion coefficient _D_ , the competition between the bias and fluctuations is quantified by the _P´eclet_ number _Pe_ ≡ _v_<sup>2</sup> _t_ /2 _D_ (see, e.g., Probstein (1994), Redner (2001)), the ratio of the average displacement squared ( _vt_ )<sup>2</sup> to the mean-square displacement 2 _Dt_ caused by random-walk fluctuations. For _Pe_ ≪ 1, bias effects due to disparities in team strengths are negligible, whereas for _Pe_ ≫ 1 the bias is important. For basketball, we estimate a typical bias velocity from the observed average final score difference, | ∆ | ≈ 10.7 points, divided by the game duration of _t_ = 2880 seconds to give _v_ ≈ 0.0037 points/sec. Using _D_ ≈ 0.0363 points<sup>2</sup> /sec, we obtain _Pe_ ≈ 0.55, which is small, but not negligible. Consequently, the bias arising from intrinsic differences in team strengths is typically not large enough to predict the outcome of typical NBA basketball games. 

Finally, the scoring anomaly associated with the last 2.5 minutes of the game is striking. If the score evolves as an anti-persistent random walk, the distribution 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

of the score difference should be Gaussian whose width grows with time as ~~√~~ _Dt_ . As shown in Fig. 7, the distribution of score difference has a Gaussian appearance, with a width that grows slightly more slowly than ~~√~~ _Dt_ . We attribute this small deviation to the weak restoring force, which gives a diffusion constant that decreases with time. However, in the final 2.5 minutes of the game, the score-difference distribution develops a spike at ∆ = 0 and dips for small | ∆ |. Thus close games tend to end in ties much more often than expected from the random-walk picture of the score evolution. This anomaly may stems from the losing team playing urgently to force a tie, a hypothesis that accords with the observed increase in scoring rate near the end of the game (Fig. 1). 

### **4 Computational Model** 

From all of the empirical observations about scoring, we now construct a computational random-walk model that broadly accounts for point-scoring statistical phenomena, as well as the win/loss record of all teams at the end of the season. In our model, games are viewed as a series of temporally homogeneous and uncorrelated scoring plays. The time between plays is drawn from a Poisson distribution whose mean is the observed value of 30.39 seconds. We ignore the short-lived spikes and dips in the scoring rate at the end of each quarter (Fig. 1) and also the very rare plays of 5 or 6 points. Thus plays can be worth 1, 2, 3, or 4 points, with corresponding probabilities drawn from the observed distribution in Table 1. Simulations of scoring events continue until the final game time of 48 minutes is reached. 

There are three factors that determine _which_ team scores. First, the better team has a greater intrinsic chance of scoring. The second factor is the antipersistence of successive scoring events that arises from the change of possession after a score. The last is the linear restoring force, in which the scoring probability of a team decreases as its lead increases (and vice versa for a team in deficit). We therefore write the probabilities _PA_ and _PB_ that team A or team B scores next, immediately after a scoring event, as: 



Here _IA_ and _IB_ are the intrinsic scoring probabilities (which must satisfy _IA_ + _IB_ = 1; and the term ±0.152 _r_ accounts for the anti-persistence. Here _r_ is defined as 



12 

Gabel and Redner: Random Walk Picture of Basketball Scoring 

and ensures that the average probability for the same team to score twice in succession equals the observed value of 0.348. Finally, the term 0.0022 ∆ (with ∆ the score difference) accounts for the restoring force with the empirically measured restoring coefficient (Fig. 5). 

In our minimalist model, the only distinguishing characteristic of team α is its intrinsic strength _X_ α . We estimate team strengths by fitting simulated team win/loss records to that predicted by the classic Bradley-Terry competition model (Bradley and Terry (1952)), in which the intrinsic scoring probabilities are given by 



To simulate a season, we assign a strength parameter to each team that is fixed for the season. We assume that the distribution of strengths is drawn from a Gaussian distribution with average µ _X_ and variance σ _X_<sup>2(James, Albert, and Stern</sup> (1993)). Nearly identical results arise for other team strength distributions. Since the intrinsic probabilities, _IA_ and _IB_ , depend only on the strength ratio _XA_ / _XB_ , we may choose µ _X_ = 1 without loss of generality, so the only free parameter is σ _X_<sup>2.</sup> We determine σ<sup>2</sup> _X_<sup>by simulating many NBA seasons for a league of 30 teams for a</sup> range of σ _X_<sup>2values and comparing the simulated probability distributions for vari-</sup> ous fundamental game observables with corresponding empirical data. 

we examined: (i) The distribution of a given score difference (already shown in Fig. 7). (ii) The season team winning percentage as a function of its normalized rank (Fig. 8 (a)); here, normalized rank is defined so that the team with the best winning percentage has rank 1, while the team with worst record has rank 0. (iii) The probability for a team to lead for a given fraction of the total game time (Fig. 8 (b)). (iv) The distribution of the number of lead changes during a game (Fig. 8 (c)). 

Our motivation for focusing on these measures is that they provide useful statistical characterizations of how basketball games evolve. The score difference is the most basic information about the outcome of a basketball game. Similarly, the relation between rank and winning percentage provides a clean overall test of our model. The probability for a given lead time is motivated by the well-known, but mysterious arcsine law (Feller (1968)). According to this law, the trajectory of a one-dimensional random walk is likely to always be on one side of the origin rather than the walk spending equal amounts of time to the left and to the right of the origin. The ramification of the arcsine law for basketball is that a single team is likely to lead for the most of the game rather than both teams to equally sharing the time in the lead. As a corollary to the arcsine law, there are typically √ _N_ crossings of the origin for a one-dimensional random walk of _N_ steps, and the distribution of 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
x 10−4<br>0.8<br>0.7<br>8<br>0.6<br>0.5 6<br>0.4<br>4<br>0.3<br>0.2 (a) 2 (b)<br>0 0.2 0.4 0.6 0.8 1 0 500 1000 1500 2000 2500<br>Rank Time Leading [s]<br>0.12<br>0.1<br>0.08<br>0.06<br>0.04<br>0.02 (c)<br>0 10 20 30<br>Lead Changes<br>Probability<br>Winning Percentage<br>Probability<br><!-- End of picture text -->

Figure 8: (a) Winning percentage as a function of team rank. The data (circles) correspond to the 1991–2010 NBA seasons. The solid curve is the simulated win/loss record when the team strength variance σ _X_<sup>2= 0.0083. The dashed curve is the simu-</sup> lated win/loss record if all teams have equal strength, σ _X_<sup>2= 0.(b) Probability that a</sup> randomly-selected team leads for a given total time. (c) Probability for the number of lead changes per game: data (◦) and simulation (curve). Simulations were run for 10<sup>4</sup> seasons with σ<sup>2</sup> _X_<sup>= 0.0083.</sup> 

the number of lead changes is Gaussian. These origin crossings correspond to lead changes in basketball games. 

For each of the four empirical observables listed above, we compare game data with the corresponding simulation results for a given value of the team strength variance σ<sup>2</sup> _X_<sup>. We quantify the quality of fit between the game data and the simulation</sup> results by the value χ<sup>2</sup> defined by 



Here _FE_ ( _x_ ) is one of the four above-mentioned empirical observables, _FS_ ( _x_ ) is the corresponding simulated observable, and _x_ is the underlying variable. For example, _FE_ ( _x_ ) and _FS_ ( _x_ ) could be the empirical and simulated probabilities of the final score difference and _x_ 

14 

Gabel and Redner: Random Walk Picture of Basketball Scoring 



<!-- Start of picture text -->
6<br>Difference<br>Lead Changes<br>5<br>Time in Lead<br>Rank<br>4<br>3<br>2<br>1<br>0 0.005 0.01 0.015<br>σ 2<br>X<br>2 min<br>χ<br> /<br>2<br>χ<br><!-- End of picture text -->

Figure 9: χ<sup>2</sup> as a function of σ _X_<sup>2for:the score difference distribution at 45.5 min-</sup> utes (◦), number of lead changes per game (▽), distribution of time that a team is leading (⊲), and winning percentage as a function of rank (△). Each point is based on simulation of 10<sup>3</sup> seasons. 

Figure 9 shows the values of χ<sup>2</sup> as a function of σ _X_<sup>2for the four observables.</sup> The best fit between the data and the simulations all occur when σ _X_<sup>2is in the range</sup> [0.00665, 0.00895]. To extract a single optimum value for σ _X_<sup>2, we combine the four</sup> χ<sup>2</sup> measurements into a single function. Two simple and natural choices are the additive and multiplicative forms 



where the sum and product are over the four observables, χ _i_<sup>2is associated with the</sup> _i_<sup>th</sup> observable, and min( χ _i_<sup>2)isitsminimumoverallσ</sup> _X_<sup>2values.Thedenominator</sup> allows one to compare the quality of fit for disparate functions. In the absence of any prior knowledge about which statistical measure about basketball scoring is most important, we have chosen to weight them equally. With this choice, both _f_ add and _f_ mult have minima at σ _X_<sup>2= 0.0083.Moreover, for this value ofσ</sup> _X_<sup>2, the value of</sup> χ _i_<sup>2for each observable exceeds its minimum value by no more than 1.095.These</sup> results suggest that the best fit between our model and empirical data arises when we choose σ<sup>2Thusroughly2/3oftheNBAteamshavetheirintrinsic</sup> _X_<sup>= 0.0083.</sup> strength in the range 1 ± � σ _x_<sup>2</sup> ≈ 1 ± 0.09. 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **5 Outlook** 

From all the play-by-play data of every NBA basketball game over four seasons, we uncovered several basic features of scoring statistics. First, the rate of scoring is nearly constant during a basketball game, with small correlations between successive scoring events. Consequently, the distribution of time intervals between scoring events has an exponential tail (Fig. 2). There is also a scoring anti-persistence, in which a score by one team, is likely to be followed by a score by the opponent because of the possession change after each basket. Finally, there is a small restoring force that tends to reduce the score difference between competitors, perhaps because a winning team coasts as its lead grows or a losing team plays more urgently as it falls behind. 

Based on the empirical data, we argued that basketball scoring data is well described by a nearly unbiased continuous-time random walk, with the additional features of anti-persistence and a small restoring force. Even though there are differences in the intrinsic strengths of teams, these play a small role in the random-walk picture of scoring. Specifically, the dimensionless measure of the effect of disparities in team strength relative to stochasticity, the P´eclet number, is small. The smallness of the P´eclet number means that it is difficult to determine the superior team by observing a typical game, and essentially impossible by observing a short game segment. We simulated our random-walk model of scoring and found that it satisfyingly reproduces many statistical features about basketball scoring in NBA games. 

This study raises several open issues. First, is the exponential distribution of time intervals between scoring events a ubiquitous feature of sports competitions? We speculate that perhaps other free-flowing games, such as lacrosse (Everson and Goldsmith-Pinkham (2008)), soccer (Dyte and Clarke (2000)), or hockey (Thomas (2007), Buttrey, Washburn, and Price (2011)), will have the same scoring pattern as basketball when the time intervals between scores are rescaled by the average scoring rate for each sport. It also seems plausible that other tactical metrics, such as the times intervals between successive crossings of mid-field by the game ball (or puck) may also be described by Poisson statistics. If borne out, perhaps there is a universal rule that governs the scoring time distribution in sports. 

Seen through the lens of coaches, fans, and commentators, basketball is a complex sport that requires considerable analysis to understand and respond to its many nuances. A considerable industry has thus built up to quantify every aspect of basketball and thereby attempt to improve a team’s competitive standing. However, this competitive rat race largely eliminates systematic advantages between teams, so that all that remains, from a competitive standpoint, are small surges and ebbs in performance that arise from the underlying stochasticity of the game. Thus seen 

16 

Gabel and Redner: Random Walk Picture of Basketball Scoring 

through the lens of the theoretical physicist, basketball is merely a random walk (albeit in continuous time and with some additional subtleties) and many of the observable consequences of the game follow from this random-walk description. 

### **References** 

- Albert, J., J. Bennett, and J. J. Cochran, eds. (2005): _Anthology of Statistics in Sports_ , _ASA-SIAM Series on Statistics and Applied Probability_ , volume 61, Philadelphia, PA: SIAM. 

- Albert, J. and R. H. Koning (2008): _Statistical Thinking in Sports_ , Boca Raton: Taylor and Francis. 

- Arkes, J. and J. Martinez (2011): “Finally, Evidence for a Momentum Effect in the NBA,” _J. Quantitative Analysis in Sports_ , 7. 

- Ayton, P. and I. Fischer (2004): “The hot hand fallacy and the gamblers fallacy: Two faces of subjective randomness?” _Memory & Cognition_ , 32, 1369. 

- Box, G. E. P. and G. Jenkins (1976): _Time Series Analysis: Forecasting and Control_ , Holden-Day. 

- Bradley, R. A. and M. E. Terry (1952): “Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons,” _Biometrika_ , 39, 324. 

- Buttrey, S. E., A. R. Washburn, and W. L. Price (2011): “Estimating NHL Scoring Rates,” _J. Quantitative Analysis in Sports_ , 7. 

- de Sa´a Guerra, Y., J. M. M. Gonz´alez, S. S. Montesdeoca, D. R. Ruiz, N. ArjonillaL´opez, and J. M. Garca-Manso (2011): “Basketball scoring in nba games: an example of complexity,” Arxiv:1108.0779. 

- Durham, Y., J. Hirschleifer, and V. L. Smith (1998): “Do the Rich Get Richer and the Poor Poorer? Experimental Tests of a Model of Power,” _Am. Econ. Rev._ , 88, 891. 

- Dyte, D. and S. R. Clarke (2000): “A Ratings Based Poisson Model for World Cup Soccer Simulation,” _J. Oper. Res. Soc._ , 51, 993. 

- Everson, P. and P. S. Goldsmith-Pinkham (2008): “Composite Poisson Models for Goal Scoring,” _J. Quantitative Analysis in Sports_ , 4. 

- Feller, W. (1968): _An Introduction to Probability Theory and its Applications_ , volume 1, New York: Wiley. 

- Garc´ıa-Pelayo, R. (2007): “Solution of the persistent, biased random walk,” _Physica A_ , 384, 143. 

- _Handbook of Defense Economics_ , Amster- 

- dam: Elsevier, North-Holland, volume 2, chapter 3, 649. 

- Gilovich, T., R. Vallone, and A. Tversky (1985): “The Hot Hand in Basketball: On the Misperception of Random Sequences,” _Appl. Cognitive Psych._ , 17, 295. 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

- Glickman, M. and S. Evans (2009): “The 2009 New England Symposium on Statistics in Sports,” _J. Quantitative Analysis in Sports_ , 6. 

- Gould, S. J. (1996): _Full House: The Spread of Excellence from Plato to Darwin_ , New York: Three Rivers Press. 

- James, B., J. Albert, and H. S. Stern (1993): “Answering Questions About Baseball Using Statistics,” _Chance_ , 6, 17–22. 

- Kubatko, J., D. Oliver, K. Pelton, and D. T. Rosenbaum (2007): “A Starting Point for Analyzing Basketball Statistics,” _J. Quantitative Analysis in Sports_ , 3. 

- Miller, S. and R. Weinberg (1991): “Perceptions of psychological momentum and their relationship to performance,” _Sport Psychologist_ , 5, 211. 

- Mosteller, F. (1997): “Lessons from Sports Statistics,” _Amer. Statistician_ , 51, 305– 310. 

- Probstein, R. F. (1994): _Physicochemical Hydrodynamics_ , New York: J. S. Wiley & Sons, 2 edition. 

- Redner, S. (2001): _A Guide to First-Passage Processes_ , New York: Cambridge University Press. 

- Sire, C. and S. Redner (2009): “Understanding baseball team standings and streaks,” _Eur. Phys. Jour. B_ , 67, 473. 

- Thomas, A. C. (2007): “Inter-arrival times of goals in ice hockey,” _J. Quantitative Analysis in Sports_ , 3. 

- Uhlenbeck, G. E. and L. S. Ornstein (1930): “On the theory of the Brownian motion,” _Phys. Rev._ , 36, 823. 

- Vergin, R. (2000): “Winning streaks in sports and the misperception of momentum,” _J. Sports Behavior_ , 23, 181. 

- Westfall, P. H. (1990): “Graphical Presentation of a Basketball Game,” _Am. Statistician_ , 44, 305. 

18 


