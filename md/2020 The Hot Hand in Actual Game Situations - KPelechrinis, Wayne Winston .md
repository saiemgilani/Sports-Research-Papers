<!-- source: 2020 The Hot Hand in Actual Game Situations - KPelechrinis, Wayne Winston .pdf -->

Konstantinos Pelechrinis<sup>_∗_</sup> and Wayne Winston<sup>_†_</sup> 

# **The Hot Hand in Actual Game Situations** 

From the classic work of Gillovich, Vallone and Tversky (GVT) [4], to the most recent major development from Miller and Sanjurjo [8] that seems to be settling the debate, the amount of ink that has been used to write on the topic of hot hand must supersede any other topic in the field of sports analytics. While originally and the vast majority of studied have been focused on basketball (the original setting at the GVT study), other sports have seen their share of hot hand studies [3, 10, 7, 5]. While the question has been open for decades and there have been several studies with conflicting results, the popular opinion has been based on the GVT conclusion; i.e., the “hot hand” is a fallacy. Miller and Sanjurjo [8] pointed out that the GVT study - and many others that followed a similar analytical approach - suffered from the streak selection bias that appears in small samples (similar to the ones used in these studies) and essentially goes to 0 for infinite sequences. The intuition behind this bias is “simple” - after someone (in this case Miller and Sanjurjo) points it out. If we take a finite series of makes (M) and misses (X) for a sequence of iid shots with constant make probability of 0.5, and we randomly choose one of the makes, then the probability that the next attempt was a make is lower than 0.5! For example, if we consider a sequence of 20 shots with exactly 10 makes and 10 misses, then once we randomly select one of the makes, the probability that the next shot is a make is 9 19<sup>_≈_0</sup><sup>_._47.According to Miller and Sanjurjo analysis a good way to answer the debate of hot hand is</sup> to perform a permutation test on the sequence of makes and misses and compare the observed probability Pr[ _M | M . . . M_ <u>� ��</u> �] _data_ with the empirical distribution of Pr[ _M | M . . . M_ <u>� ��</u> �] _perm_ obtained through a _k times k times_ number of permutations. For example, let’s consider the sequence of shots in Figure 1. Let us further assume that all shots are from the same spot (e.g., practise right corner 3 shots). For _k_ = 1, we have Pr[ _M |M_ ] _data_ to be equal to 0.6. We randomly permuted the shots 1000 times and we obtained the distribution for Pr[ _M |M_ ] _perm_ presented in the figure. The average of Pr[ _M |M_ ] _perm_ is 0.47, which is smaller than 0.5, as expected by [8]. Furthermore, in only 8% of the permutations, the resulting sequence exhibited a higher than 0.6 probability of a make following a make. This is essentially the empirical p-value of the permutation test, and one can say that there is quiet some evidence that this sequence exhibits the “hot hand”. Now the same sequence, if we use the Wald-Wolfowitz test, which is what the GVT study used, the corresponding p-value is 0.17, which essentially translates to more than twice the probability of the observed sequence being a result of chance as compared to the permutation test. This is due to the streak selection bias. 

The majority of these studies are focusing on a specific situation that satisfies the “identical” part of the iid assumption. For example, GVT focused on free throws, while other studies [9, 6] examine data from NBA three point contests. While these situations allow to draw some conclusions it does not directly examine what happens on the court, _in the wild_ . To the best of our knowledge, the only study that considers in-game situations in the context of hot hand is the work by Bocskocsky _et al._ [1]. The authors use optical tracking data from SportVU and show that a player who scores more 

> _∗_ School of Computing and Information, University of Pittsburgh (kpele@pitt.edu) 

> _†_ Kelley School of Business, Indiana University (winston@indiana.edu) 

**1** 

**K. PELECHRINIS AND W. WINSTON** 

**2** 



**Figure 1.** _Using a permutation test we can obtain the empirical distribution for_ Pr[ _M |M_ ] _perm under the null hypothesis. In this case, there is about 8% that the observed sequence was due to chance, i.e., the sequence exhibits the “hot hand”._ 

points than expected (based on the quality of the shots he takes) on a series of shots tend to take tougher shots consequently, rendering the independence assumption not true in a game setting. They further run a regression, controlling for the shot difficulty, and show that a player that has exceeded expectations in the last _k_ shots, has slightly increased chances of scoring the next one<sup>1</sup> . However, the specification provided and the definition of a player’s “heat”, is different than that of the majority of the hot hand literature. In particular, the authors consider the degree of “heat” for a player to be the difference between the actual and the expected FG percentage over the past _k_ shots. This means that a player can be “hot” (to some degree) even if he missed half of his last _k_ shots. Many people might argue that this is not a hot player on a streak, and while there is not a right or wrong way to define what constitutes a hot hand, we want to keep the same notion of “hotness” as in the majority of the literature - but avoid the streak sampling bias. At the same time we want to consider the heterogeneity that exists within in-game situations in terms of shot quality. So essentially we have a sequence of _n_ shots _S ∈{M, X}_<sup>_n_</sup> , with an associated shot make probability vector **P** , where _pi_ = Pr[ _si_ = _M_ ]. Given that the shots are not identical, we cannot simply permute the outcomes of the shots and have the same test as shown in Figure 1. However, having an estimate of _pi ∀si ∈S_ allows us to resample the shot sequence several times and build the empirical null distribution (i.e., the one expected under the _H_ 0 of independent shots). The shot sequence is essentially a non-homogeneous Bernoulli process with success probability **P** , _S ≈ B_ ( _n,_ **P** ). Hence, we can obtain an estimate for Pr[ _M |M_ ] _sample_ and compare with the observed value of Pr[ _M |M_ ] _data_ . 

The first thing we have to do is to create a model for estimating the probability _pi_ of making a shot 

> 1From a technical standpoint, the authors also use OLS (instead of the more appropriate logistic regression) to model a binary variable, which violates the constant variance assumption of linear regression. This means that the t-statistic might not truly follow a t-distribution, leading to biased estimation of the corresponding p-value. 

**THE HOT HAND IN ACTUAL GAME SITUATIONS** 

**3** 



**Figure 2.** _The probability calibration of the neural network model is very good._ 

_si_ given a set of covariates **z** . For this purpose we use a dataset obtained from the SportVU optical tracking system for the seasons 2013-14 and 2014-15 with approximately 200K shots each season<sup>2</sup> . The dataset includes several variables that we use as our model covariates: 

- Distance to the basket 

- Distance of the closest defender 

- Player IDs for the shooter and the closest defender 

- Touch time prior to shooting 

- Number of dribbles before shooting 

- Shot type (e.g., floater, tip etc.) 

We use the first season in our dataset to train and evaluate the shot probability model<sup>3</sup> . We build a feedforward neural network with 4 hidden layers. Each layer has 250 units and relu activation. We use a validation set for early stopping during training. Our final model is evaluated on a held out set and has an accuracy of 66%, which is on par with the state-of-the-art shot make probability models [2]. We also evaluate the calibration of the output probabilities. Figure 2 presents the reliability curve, where as we can see the predicted probabilities follow closely the observed shot make probabilities. 

We can now estimate the shot make probability for each shot in the 2014-15 season, which we will use for identifying the presence of “hot hand” or not. We first filter players with at least 1000 shots during the whole season. For each player we only consider games for which we have information for 

> 2https://github.com/hwchase17/sportvu 

> 3 All the code and our analysis is available at: https://github.com/kpelechrinis/HotHand-NBA-Tracking. 

**K. PELECHRINIS AND W. WINSTON** 

**4** 

all of their shots in that game. For example, in some cases the distance of the closest defender or the touch time is not provided. In this case we cannot estimate the shot make probability, and we filter out not only this specific shot, but all the shots from the same game, since the sequence will essentially be broken. 

|**Player**|Pr[_M|M_]_data_<br>Pr[_M|M_]_sample_|p-val|
|---|---|---|
|LaMarcus Aldridge|0.47<br>0.44|0.10|
|**Rudy Gay**|0.49<br>0.40|_<_0.001|
|Pau Gasol|0.46<br>0.46|0.48|
|**Chris Paul**|0.48<br>0.41|0.01|
|Anthony Davis|0.51<br>0.52|0.73|
|**Damian Lillard**|0.42<br>0.37|0.05|
|Victor Oladipo|0.43<br>0.42|0.38|
|LeBron James|0.46<br>0.48|0.68|
|Dwyane Wade|0.47<br>0.46|0.28|
|Monta Ellis|0.44<br>0.42|0.20|
|Russell Westbrook|0.42<br>0.37|0.06|
|Andrew Wiggins|0.39<br>0.43|0.91|
|**Blake Griffn**|0.52<br>0.48|0.02|
|James Harden|0.44<br>0.40|0.07|
|Tyreke Evans|0.48<br>0.45|0.16|
|Stephen Curry|0.46<br>0.47|0.56|
|John Wall|0.48<br>0.45|0.13|
|Dirk Nowitzki|0.42<br>0.38|0.11|
|Kyrie Irving|0.42<br>0.38|0.07|
|**Klay Thompson**|0.49<br>0.44|0.02|
|**Markieff Morris**|0.48<br>0.41|0.01|
|**Nikola Vucevic**|0.50<br>0.44<br>**Table 1**<br>_Hot Hand Results_|0.01|



Table 1 presents the results for _k_ = 1<sup>4</sup> . Column Pr[ _M |M_ ] _data_ is the probability of a Make to be followed by another Make as observed in the data, while column Pr[ _M |M_ ] _sample_ presents the average probability of a Make to be followed by another Make after resampling 1000 the Bernoulli process _Bij_ ( _nij,_ **P** _ij_ ) _, ∀j_ for player _i_ during game _j_ . As we can see out of the 22 qualified players, we observe for 7 players a Pr[ _M |M_ ] _data_ that has less than 5% chance of being a result of chance. With no hot hand, we would expect 5% of the players to have a p-value of 0.05 or less<sup>5</sup> . If each player has a 5% chance of having a p-value of 0.05 or less by chance, then there is only about 7-in-100,000 chance of finding at least 7 players out of the 22 with a p-value of 0.05 or less when there is no hot hand effect. These observations point to the presence of the hot hand within game situations, and the effect size up to 8%. 

> 4We provide more results at the code repository provide above. 

> 5 The significance level _α_ is also the false positive rate of the test. 

**THE HOT HAND IN ACTUAL GAME SITUATIONS** 

**5** 

In conclusion, we have taken the incredible observation from Miller and Sanjurjo [8] and adopted it for application in settings where the identical assumption of consecutive shots does not hold. Using optical tracking data from SportVU we identify that the “hot hand” exist in actual game situations. 

## **REFERENCES** 

- [1] A. BOCSKOCSKY, J. EZEKOWITZ, AND C. STEIN, _The hot hand: A new approach to an old fallacy_ , 2014. 

- [2] D. DALY-GRAFSTEIN AND L. BORNN, _Rao-blackwellizing field goal percentage_ , Journal of Quantitative Analysis in Sports, 15 (2019), pp. 85–95. 

- [3] R. DORSEY-PALMATEER AND G. SMITH, _Bowlers’ hot hands_ , The American Statistician, 58 (2004), pp. 38–45. 

- [4] T. GILOVICH, R. VALLONE, AND A. TVERSKY, _The hot hand in basketball: On the misperception of random sequences_ , Cognitive psychology, 17 (1985), pp. 295–314. 

- [5] B. GREEN AND J. ZWIEBEL, _The hot-hand fallacy: Cognitive mistakes or equilibrium adjustments? evidence from major league baseball_ , Management Science, 64 (2018), pp. 5315–5348. 

- [6] J. J. KOEHLER AND C. A. CONLEY, _The hot hand myth in professional basketball_ , Journal of sport and exercise psychology, 25 (2003), pp. 253–259. 

- [7] J. A. LIVINGSTON, _The hot hand and the cold hand in professional golf_ , Journal of Economic Behavior & Organization, 81 (2012), pp. 172–184. 

- [8] J. B. MILLER AND A. SANJURJO, _Surprised by the hot hand fallacy? a truth in the law of small numbers_ , Econometrica, 86 (2018), pp. 2019–2047. 

- [9] J. B. MILLER AND A. SANJURJO, _Is it a fallacy to believe in the hot hand in the nba three-point contest?_ , (2019). 

- [10] A. VESPER, _Putting the hot hand on ice_ , CHANCE, 28 (2015), pp. 13–18. 


