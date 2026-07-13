<!-- source: Rao-Blackwellizing Field Goal Percentage.pdf -->

# Rao-Blackwellizing Field Goal Percentage 

### Daniel Daly-Grafstein<sup>1</sup> and Luke Bornn<sup>1</sup> 

> 1Simon Fraser University 

August 14, 2018 

**Abstract** Shooting skill in the NBA is typically measured by field goal percentage (FG%) - the number of makes out of the total number of shots. Even more advanced metrics like true shooting percentage are calculated by counting each player’s 2-point, 3-point, and free throw makes and misses, ignoring the spatiotemporal data now available (Kubatko et al. 2007). In this paper we aim to better characterize player shooting skill by introducing a new estimator based on post-shot release shot-make probabilities. Via the Rao-Blackwell theorem, we propose a shot-make probability model that conditions probability estimates on shot trajectory information, thereby reducing the variance of the new estimator relative to standard FG%. We obtain shooting information by using optical tracking data to estimate three factors for each shot: entry angle, shot depth, and left-right accuracy. Next we use these factors to model shot-make probabilities for all shots in the 2014-15 season, and use these probabilities to produce a Rao-Blackwellized FG% estimator (RB-FG%) for each player. We demonstrate that RB-FG% is better than raw FG% at predicting 3-point shooting and true-shooting percentages. Overall, we find that conditioning shot-make probabilities on spatial trajectory information stabilizes inference of FG%, creating the potential to estimate shooting statistics earlier in a season than was previously possible. 

1 

## **1 Introduction** 

Field goal percentage is a common measure of shooting skill and efficiency in the National Basketball Association (NBA), and general shooting prowess is often defined for players by their overall FG%. It can be used in its raw form, or as a component of more advanced metrics like true-shooting percentage (TS%) or effective field goal percentage (eFG%). Shooting percentages play a large role in influencing both fan and coaching evaluation of players, and are often used to predict future player performance when making decisions regarding free agency or draft selection. 

Predicting a player’s FG% given past shooting is a difficult task. Shooting percentages are highly variable, especially on longer shots like 3-point attempts. For example, it takes roughly 750 3-point attempts before a player’s shooting percentage stabilizes, where over half of the variation in their 3-point percentage (3P%) is explained by shooting skill, rather than noise (Blackport 2014). Additionally, 3P% has been shown to be an unreliable metric in terms of its ability to discriminate between players and its stability from one season to the next (Franks et al. 2016). As the proportion of shot attempts taken as 3-pointers increases, with total attempts having risen nearly 50% over the last 8 years (Young 2017), overall FG% becomes more variable and less stable. 

Part of the large variation in shooting percentages is likely due to the many contextual factors that contribute to the probability of a shot make. Improvements to FG% prediction have been made by including some of these covariates in shot-make prediction models (Cen et al. 2014, Piette et al. 2010). However, because of the small differences that separate the true shooting skill of players in the NBA, chance variation may also contribute significantly to the variation and instability of FG%. Optical tracking data of shot trajectories can potentially reduce noise in shooting metrics by allowing us to differentiate shots that rim 

2 

out, air balls, and (unintentional) banks, giving us more information about players’ shooting skill with fewer shots. This idea has been demonstrated recently during practice shooting sessions, where FG% augmented by precise shot factor information gathered during these sessions improved the prediction of future shooting (Marty and Lucey 2017, Marty 2018). Accurate estimates of shot factors using live-game optical tracking data may allow for a similar improvement in the prediction of in-game shooting metrics. 

In this paper, we seek to reduce the variation in predicting player FG% using NBA optical tracking data. We begin the paper by introducing a new estimator for FG%, RB-FG%, based on aggregating shot-make probabilities. Estimation of shot-make probabilities is then split into two main parts. First, using spatio-temporal information provided by the tracking data, we model shot trajectories in order to estimate the depth, left-right distance, and entry angle of balls entering the basket. Next, we use a regression model to estimate the probability of each shot going in. We define the average of these estimated probabilties, RB-FG%, as our new estimator of FG% for each player. Finally, we compare the predictive ability of the RB-FG% and RB-TS% estimators to their raw counterparts that don’t utilize contextual information. 

## **2 The Rao-Blackwellized Estimator** 

In this section we introduce our new estimator for FG% based on shot-make probabilities. When trying to predict a player’s future FG% using their past FG%, each shot _Xi_ is treated as Bernoulli random variable with probability of success _θ_ , where _θ_ is a measure of the player’s true FG%. Under this model the probability that the player’s next shot goes in is treated as a constant unknown parameter. Alternatively, we can define a new model where the 

3 

probability that each shot goes in varies, and shots are modelled as Beta-Bernoulli random variables _Xi ∼ Bern_ ( _pi_ ) with _pi ∼ Beta_ ( _θv,_ (1 _− θ_ ) _v_ ), where again _θ_ is the true FG% of a player, defining their corresponding Beta distribution of shot-make probabilties. 

As shown below, inference under the model in which shots are treated as Bernoulli random variables and inference under the expected Beta-Binomial of our new model is the same. Let Π( _Xi|θ, v_ ) be the likelihood of the expected Beta-Binomial distribution, and let _B_ ( _·_ ) be the beta function. 





Suppose we obtain _Xi_ (make or miss) and _pi_ (the probability that shot _i_ will go in). Let Π( _Xi, pi|θ, v_ ) be the joint distribution of _Xi_ and _pi_ . It follows that: 



where Π( _Xi|pi_ ) and Π( _pi|θ, v_ ) are the Bernoulli and Beta distributions, respectively. Consequently we have that given _pi_ , _Xi_ is independent of _θ_ , so _pi_ is sufficient for _θ_ . Now let _θ_<sup>ˆ</sup> be the raw FG% estimate and _θ_<sup>ˆ</sup> _RB_ be the RB-FG% estimate. We have: 

4 



By the Rao-Blackwell Theorem: 



Therefore if we are able to estimate shot-make probabilities, we can produce a new statistic RB-FG% with lower variance than raw FG%. 

## **3 Estimating Shot-Make Probabilities** 

### **3.1 Measuring Shot Factors** 

In order to model shot-make probabilities, we first measure 3 shot factors based on how each shot entered the basket - left-right accuracy, depth, and entry angle - following the procedure of Marty and Lucey (2017). We define left-right accuracy as the deviation of the ball from the centre of the hoop as the ball crosses the plane of the basket (Figure 1a). Shot depth is defined as the distance of the ball from a tangent line through the front of the hoop as the ball crosses the plane of the basket (Figure 1a), with the front of the hoop adjusted to be from the perspective of the shooter. We specify the adjusted front of the rim as depth 0, so 

5 



<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

Figure 1: Shot factors at the plane of the hoop. Figure (a) denotes the left-right and depth factors, Figure (b) denotes the entry angle factor. 

a shot crossing the basket plane at the center of the hoop has a depth of 9 inches. Finally, the entry angle is defined as the angle between the plane of the hoop and a tangent line through the ball as it is entering the basket (Figure 1b). See Marty and Lucey (2017) for further detail regarding these measurements. 

To obtain these shot factor estimates, we use shot trajectory information provided by the SportVu optical tracking data from STATS LLC. The data provides measurements of the X and Y coordinates for all 10 players and X,Y, and Z coordinates of the ball 25 times per second. Our dataset consists of 1212 games from the 2014-15 NBA regular season and 1206 games from the 2015-16 regular season. We first restrict our analysis to 3-point shots as these shots have the most trajectory information and we can assume all shooters are attempting to hit the centre of the basket (no shot attempts purposely off the backboard). In total our dataset consists of trajectory information for 47,631 3-point shots from the 2014-15 season and 49,876 3-point shots from the 2015-16 season. 

Although the optical tracking data gives X,Y, and Z coordinates of the ball at the basket, 

6 

the location data is noisy, especially in measuring the height of the ball. To obtain a better estimate of the position of the ball near the basket we model a quadratic best fit line through the trajectory data given by the tracking database. If _Zi_ is the height of shot _i_ , and _xi_ and _yi_ are the X,Y coordinates of the shot in the tracking data, we use a quadratic polynomial to model the height, and estimate the coefficients by a least-squares regression: 



We use the point where the model specifies the ball crosses 10 feet in height as the estimated X,Y location of the ball at the basket, and use this location to calculate the shot’s depth, left-right accuracy, and entry angle. 

We compare the above model with a second model in which we try to leverage pre-existing knowledge of shot trajectories. We know each shot starts at the player’s location at the time of release (player location is less noisy than ball location in the tracking database) and ends around the basket. Therefore, we can improve estimation by biasing the start and end points of our modeled trajectories to incorporate this prior knowledge. To accomplish this we introduce a Bayesian regression model using pseudo-data to establish priors that reflect this knowledge. This is an informal empirical Bayes method where instead of using data to estimate the priors, we use prior knowledge of how the data should look. Given the quadratic model (1) for each shot, we can specify a Bayesian regression model with a conjugate Normal prior for _β_ of the form _ρ_ ( _β|σ_<sup>2</sup> _, z, X_ ) _∼ N_ ( _u_ 0 _, σ_<sup>2</sup> Λ<sup>_−_</sup> 0<sup>1).Thisresultsinaconjugateinverse</sup> gamma prior for _σ_<sup>2</sup> written as _ρ_ ( _σ_<sup>2</sup> _|z, X_ ) _∼ IG_ ( _a_ 0 _, b_ 0). We can then update our mean and precision parameters as: 

7 



where _un_ is the posterior mean of _β_ , and Λ _n_ is the posterior precision matrix for _β_ . We update the parameters twice, once using pseudo-data reflecting our prior knowledge of where shots start and finish, and a second time using the shot trajectory data from the optical tracking data. We specify 4 pseudo-data points, 2 at the start of the shot set at the X,Y coordinates of the player when the shot is released and at a height of 7 feet, and 2 set at the centre of the hoop and at 10 feet in height. After two Bayesian learning updates we take the posterior mean of _β_ , _u_ 2, and use it as the estimate for the coefficients in the quadratic polynomial model (1). 

We then use (1) to compute the 3 shot factors for each shot using both the ordinary linear regression (OLR) and Bayesian regression approaches. Comparing the two models, we find both predict shots to have a mean depth value of 11”, a mean left/right value of 0”, and a mean entry angle around 45<sup>_◦_</sup> . As in Marty and Lucey (2017) we find shots entering the basket at 11” in depth, 2” deeper than the centre of the basket, and 0” in left-right accuracy are made with the highest percentage. However, we find shot depths are evenly distributed around 11”, in contrast to the findings of Marty and Lucey (2017) who found that shooters have a mean shot depth value of 9”, at the centre of the hoop. The variance in left/right distance and entry angle between the two models is similar, however the variance in shot depth is much larger in the OLR compared to the Bayesian regression model (Figure 2). Overall, variances in shot factors under the Bayesian model match the variances of the precise shot factor measurements of Marty and Lucey (2017) more closely than the OLR model. Furthermore, we will see later that when we model shot probabilities the Bayesian model produces a lower misclassification rate than the OLR model. Moving forward, we decide to use shot factors calculated via the Bayesian regression model. 

8 



Figure 2: Estimated shot factor measurements under the ordinary and Bayesian regression models. Left/right and depth measurements are given as distance in feet in relation to the centre of the basket, where the depth of the centre of the basket is 0.75 feet. Entry angle measurements are given in radians to allow for the values to be on the same axis. 

### **3.2 Modeling Shot-Make Probabilities** 

In this section we train a shot-make probability model using 3-point shots from the 2014-15 season. To obtain shot-make probabilities for each shot, we use the shot factors described previously as covariates in a logistic regression: 



where _Si_ is an indicator function equal to 1 when a shot goes in and 0 went it misses, _σ_ (x) = exp(x) _/_ (1+exp(x)), and _Di_ , _LRi_ , and _Ai_ are the estimated depth, left-right distance, 

9 

and entry angle of shot _i_ , respectively. Although our Bayesian regression model biases shot trajectories toward the basket, some trajectories are still quite variable. Modeled trajectories that are too far from the raw data are removed and instead assigned a probability of 1 or 0 for a make or miss, respectively. We use factors from the remaining shots to estimate shot-make probabilities with model (2). To assess how accurate the model is we perform a tenfold cross validation with a probability cutoff of 0.5, and obtain the mean misclassification rate for the held out data. We repeat this procedure with shot factors estimated from the OLR model. The covariates estimated via OLR and Bayesian regression resulted in misclassification rates of 0.246 and 0.204, respectively. Therefore, our Bayesian model is able to predict makes/misses correctly about 80% of the time, a higher rate than other shot prediction models that use contextual covariates such as distance to basket and nearest defender (Cen et al. 2015). However, this is still lower than the accuracy of the Noah Shooting System - a dedicated hardware install found in practice facilities that provides shooting information not available in live games. Marty and Lucey (2017) were able to define a guaranteed make zone of over 90% based on Noah System shot factors. Similar to 





Figure 3: Figure (a) shows the distribution of mean predicted shot-make probabilities over different shot entry angles. Included are all 3-point shots in the 2014-15 season in which trajectory information is used to train our model (2). Figure (b) shows the distribution of predicted shot-make probabilities over different values of shot depth and left-right accuracy in relation to the basket. 

10 

probabilities based on raw FG% (Marty and Lucey 2017), predicted shot-make probabilities are highest for shots at 11 inches depth, 0 inches of left-right deviation, and similar for shots with entry angles in the mid-40s. These can be seen in relation to the basket in Figure 3. 

## **4 Applications of the RB-FG% Estimator** 

### **4.1 Predicting Three-Point Field Goal Percentage** 

In this section we aim to create a new estimate for player FG% by aggregating estimated shotmake probabilities given by (2). Without loss of generality, we focus first on 3-point shots for clarity of presentation. We gather shot trajectories for 3-point shots taken from the first half of the 2015-16 NBA season in the SportVu tracking database (N=24855), and predict the probability of each shot going in using model (2) trained by shots taken in the 2014-15 season. The mean of these estimated shot-make probabilities is the RB-FG% estimate, _θ_<sup>ˆ</sup> _RB_ , for each player’s FG%. We wish to see whether _θ_<sup>ˆ</sup> _RB_ is better than raw FG%, _θ_<sup>ˆ</sup> , at predicting a player’s future FG%, _θ_ . When we compare the ability of _θ_<sup>ˆ</sup> _RB_ and _θ_<sup>ˆ</sup> to predict 3-point FG% in the second half of the 2015-16 season we find _θ_<sup>ˆ</sup> _RB_ has a lower mean absolute error than _θ_<sup>ˆ</sup> (Table 1), As both _θ_<sup>ˆ</sup> and _θ_<sup>ˆ</sup> _RB_ are unbiased estimators of _θ_ , the decrease in meanabsolute error of our modeled estimator is predominately due to a reduction in variance (Figure 4). 

Rao-Blackwellizing the estimator for FG% does reduce variance and improve the prediction accuracy, but these estimators are based on low sample sizes for most players. We are able to further reduce the variance of _θ_<sup>ˆ</sup> _RB_ by introducing a empirical Bayesian shrinkage factor 

11 



Figure 4: The distribution of standard deviations for the Rao-Blackwellized and raw 3-point FG% estimators for 260 players in the first half of the 2015-16 season. The variance of the raw estimator for each player is calculated according to a binomial distribution as _θ_<sup>ˆ</sup> (1 _−θ_<sup>ˆ</sup> ) _/n_ , where _θ_<sup>ˆ</sup> is the raw FG% for each player. The variance of the Rao-Blackwellized estimator is calculated according to the proposed Beta distribution that each player’s shot probabilities ˆ are drawn from as (ˆ _αβ_<sup>ˆ</sup> ) _/_ ( _n_ (ˆ _α_ + _β_<sup>ˆ</sup> )<sup>2</sup> (ˆ _α_ + _β_<sup>ˆ</sup> + 1)), where _α_ and _β_<sup>ˆ</sup> are calculated by maximum likelihood using Nelder-Mead optimization. 

towards a Beta prior. We apply a prior distribution to each player’s first half 3-point shooting of the form Beta(10,18), in essence adding 10 league-average shots to each player’s estimate. Table 1 shows that the shrunk-RB estimator is a better predictor than the shrunk-raw estimator, and this improvement is illustrated in Figure 5. Hence while Rao-Blackwellizing significantly improves prediction, leveraging knowledge about the distribution of 3P%’s can further improve the RB-FG% estimator (Morris and Effron 1977). 

In addition to predicting future shooting, we can also use _θ_<sup>ˆ</sup> _RB_ to estimate players’ 3P% with less data than when using _θ_<sup>ˆ</sup> . The root-mean-square error (RMSE) of both estimators for inferring end-of-season 3P% is presented in Figure 6. RB-FG% has a lower RMSE than the FG% when calculated using less than 30% of games, and the biggest improvements occur with low sample sizes. Some bias is introduced by RB-FG% as shot probabilities are modeled 

12 



Figure 5: Mean prediction error for the raw, Rao-Blackwellized, and shrunk-RaoBlackwellized 3-point FG% estimators of 20 players in the first half of the 2015-16 season. Errors are measured for predicting 3-point FG% in the second half of 2015-16. 

using the entire set of 3-point shots, while estimates are calculated seperately for each player. We only used a single set of priors to estimate shot factors in our Bayesian regression, but each player should have their own set of priors due to differences in height and shooting style. However, specifying individual priors and creating separate shot trajectory models for each player is difficult because individual players take too few shots to obtain accurate parameter estimates. Additionally, the reduction in variance outweighs the small level of bias introduced by _θ_<sup>ˆ</sup> _RB_ (Figure 6). Because we are comparing these estimators to raw FG% on the full sample, the raw estimator eventually becomes better if we increase the proportion of games used. However, even full-season shooting numbers are highly variable and based on low sample sizes for most players. Thus RB-FG% is a better overall estimate on any size of data, but for small sample sizes it is a better estimate of end-of-season FG% than FG% itself. 

13 



Figure 6: The RMSE of _θ_<sup>ˆ</sup> and _θ_<sup>ˆ</sup> _RB_ estimating players’ true 3-point FG% for the 2014-15 NBA season. These estimators are calculated using shots from a subset of games and compared to each player’s 3-point FG% at the end of the season. RMSE is calculated separately for each sub-box using 5%, 10%, 15%, 20%, 25%, and 30% of the games from the 2014-15 season. 

### **4.2 Predicting True Shooting Percentage** 

Although we’ve focused on three-point shots, we are able to Rao-Blackwellize any shooting statistic provided we have enough trajectory information to accurately estimate shot factors. We now expand our selection of shots and try to improve predictions of TS% using our shot factor and shot probability models. We repeat the procedure described in section 3 to estimate shot factors for all two-point shots and free throws in the 2014-15 season, and use these to create separate Rao-Blackwellized two-point FG% and free throw percentage (FT%) estimates. As before, shots that do not have enough location data or resulted in trajectory predictions very far from the raw data are not included in training or prediction datasets. In 

14 

total, shot-make probabilities are estimated for 21,153 out of 24,832 free throws and 21,890 out of 73,925 two-point shots, with remaining probabilities assigned as 1 or 0 for a shot make and miss, respectively. The new RB estimators are again used to predict two-point FG%, FT% and TS% in the second half of the 2015-16 season. As with 3P%, we find the shrunk Rao-Blackwellized estimator for TS% results in the lowest mean absolute error (Table 1). 

Rao-Blackwellizing 2-point shots results in only a modest decrease in MAE compared to the shrunk raw estimator. This may be because we are only able to estimate shot-make probabilities for a small fraction of two-point shots using the optical tracking database. Many 2-point shots are taken close to the basket or intended as bank-shots, resulting in insufficient or inaccurate trajectory information. These 2-point shots are not included in our prediction model and thus 2-point FG% is only partially Rao-Blackwellized. Interestingly, Rao-Blackwellizing FT% also resulted in only a minor improvement in prediction. This is not due to lack of trajectory information as most free throws are included in our shotmake model, but may be because free throws more closely follow a Bernoulli distribution than either 2-point or 3-point shots. Free throws are certainly more homogeous than other shot attempts as they are not affected by contextual factors like changing shot distance or defender pressure. There has been some research showing serial correlation between free throws (Arkes 2010). Though even when shown this effect is considerably smaller than the effects contextual factors have on field-goal shot-make probabilities. The closer that a player’s free throw attempts follow a Bernoulli distribution, the less potential there is to decrease the mean-squared error of the raw estimator of FT% through Rao-Blackwellization. If a player’s free throw attempts perfectly follow a Bernoulli distribution the number of makes and misses becomes a sufficient statistic for FT% and Rao-Blackwellizing would give no improvement in prediction accuracy. 

15 

Table 1: Mean Absolute Prediction Errors of FG% Estimators 

||Raw|Grand Mean|RB|Shrunk Raw|Shrunk RB|
|---|---|---|---|---|---|
|3-point shots|0.0790|0.0620|0.0590|0.0689|0.0572|
|Free throws|0.0809|0.0834|0.0713|0.0702|0.0691|
|2-point shots|0.0549|0.0486|0.0502|0.0440|0.0428|
|True-Shooting|0.0467|0.0436|0.0408|0.0417|0.0379|



Estimators are for FG% in the first half of the 2015-16 NBA season, errors based on prediction of FG% in the second half of 2015-16. The raw estimator uses make/miss data, while the Rao-Blackwell (RB) estimator uses predicted shot-make probabilities. 

### **4.3 Example of an Improvement in Inferring Player FG%** 

We now present an example of when evaluating a player using _θ_<sup>ˆ</sup> _RB_ instead of _θ_<sup>ˆ</sup> may change the interpretation of that player’s shooting and prediction of their future FG%. After signing with Miami Lebron James improved his 3-point shooting ability drastically, shooting 36.5% from three during the 2010-11 to 2014-15 seasons compared to just 32.9% in his first 7 seasons in Cleveland (Paine 2016). However, during the 2015-16 season Lebron shot just 30.9% from three. Was there a real difference in his 3-point shooting ability during this season compared to the previous 5? If we attempt to answer this question using raw FG%, we can estimate a 90% confidence interval via a normal approximation of (0 _._ 264 _,_ 0 _._ 354). Thus with 90% confidence we can say there was a real difference between Lebron’s 3-point shooting during 2015-16 compared to the previous 5 years. More traditional advanced metrics also fail to explain James’s dip in 3-point FG%. Compared to the 2014-15 season (where James shot 35.4% from three), in 2015-16 he shot from more favorable 3-point zones, shot fewer threes late in the shot clock, more of his threes came from assists, and fewer threes came against ”tight” defensive pressure as classified by the SportVu tracking data (Paine 2016). All these indicators suggest that James’s 3-point shooting should have improved in 2015-16, yet he shot his poorest percentage since his rookie year. Based on these statistics, one may 

16 

have concluded that there was a real decrease in 3-point shooting skill during the 2015-16 season, and we may have predicted that this poor shooting would continue in upcoming seasons. However, if we instead use RB-FG% as an estimator of 3P%, we estimate his 3- point percentage during 2015-16 to be 34.7%, with a 90% confidence interval of (0 _._ 321 _,_ 0 _._ 374). Therefore, according to his RB-FG% Lebron did not have an appreciable decline in 3-point shooting ability, and we would predict that his FG% should revert back to somewhere around his average over the previous 5 years. As we’ve seen, this was indeed the case as his 3P% returned to 36.3% during the 2016-17 season. 

## **5 Disussion and Conclusion** 

In this paper we were able to construct an improved estimator for FG% based on shotmake probabilities calculated from shot trajectories. Via the Rao-Blackwell theorem, we demonstrated that if we model shots according to a Beta-Bernoulli distribution, rather than a Bernoulli, aggregating shot-make probabilities for individual players is a more accurate estimator for future shooting than raw FG%. Shot trajectory data has been shown to improve estimation of FG% in other contexts. Marty (2018) demonstrates, using precise shot data captured by Noahlytics during practice shooting sessions, that raw shooting percentage augmented with 9 spatial rim patterns is a better estimate of shooting skill than raw FG%. We are able to extend this idea to live-games, and show that shot features measured using the less precise optical tracking data can still provide improvement in FG% prediction and estimation. Our method differs in that we create a new shooting statistic, one based on shot-make probabilities only, rather than use raw FG% augmented with spatial features. Comparing the estimation ability of _θ_<sup>ˆ</sup> _RB_ and Marty’s raw FG% augmented with spatial features is not explored in this paper, but both methods show distinct improvements when 

17 

performing estimation on low sample sizes. 

Another way to quantify the quality of our Rao-Blackwellized metrics is to measure how well they are able to discriminate between players. We can accomplish this by comparing the discrimination meta-metric for Rao-Blackwellized and raw shooting metrics (Franks et al. 2016). This meta-metric quantifies the fraction of variance between players that is due to differences in true shooting skill. Table 2 shows that RB-3P% and RB-TS% are both more discriminative metrics than their raw counterparts. Franks et al. (2016) also define the meta-metric stability: the fraction of total variance in a metric that is due to true changes in player skill over time, rather than chance variability. We did not calculate this meta-metric as we do not have enough seasons of trajectory data to obtain accurate estimates. 

There have been many other models that use game-specific context variables like defender distance and shot location to try and estimate the probability that shots will go in (Cen et al. 2015, Chang et al. 2014). These models are also Rao-Blackwellizing FG%, as they are assuming shot probabilities vary for each shot (see Section 2). However, _θ_<sup>ˆ</sup> _RB_ should still improve on these models because our estimated shot factors are sufficient for all in-game contextual variables that contribute to shot-make probabilities. Including the location of the shot or the nearest defender distance should not change the probability a shot will go in given its depth, left-right accuracy, and entry angle at the basket. We are able to classify shots correctly 79.6% of the time using predicted make probabilities based on trajectory information, higher than the 61% classfication rate we found using nearest defender distance and shot 

Table 2: Discrimination Values for Raw and Rao-Blackwellized Shooting Metrics 

||Raw 3P%|RB-3P%|Raw TS%|RB-TS%|
|---|---|---|---|---|
|Discrimination|0.432|0.548|0.713|0.804|



Estimates are based on Discrimination metrics for the 2014-15 season. The RB metrics are shrunk as defined in Section 4.1. 

18 

location as predictors of raw FG%, and also higher than those found in more complex contextual models (Cen et al. 2015, Chang et al. 2014). Additionally, adding shot-distance and nearest-defender distance as dimensions to RB-FG% did not improve classification. 

Because RB-FG% allows us to more accurately estimate true FG% with smaller sample sizes, we should be able to more accurately predict how contextual shooting variables like defender distance impact a player’s shooting. Unfortunately, it is difficult to compare coefficients for contextual variables when fitting predicted probabilities compared to a binary shot response (make/miss) because we are estimating coefficients using different loss functions. Therefore, when we try to compare these coefficient estimates to a ”true” value, for example how defender-distance affects FG% for a player over the entire season, we are comparing two estimated coefficients to a ”true” coefficient value which is also estimated using a binary shot response. Even if the coefficient for defender distance estimated using _θ_<sup>ˆ</sup> _RB_ as a response is a better indicator of how a player responds to defensive pressure, it is difficult to compare this to any standard value for that player. 

Although all NBA teams almost exclusively use raw FG% and its aggregate statistics to evaluate player shooting, many teams use shot trajectory characteristics to evaluate and coach player shooting in practice. The Noah Shooting System is used by a number of teams to analyze player shooting and to improve shot trajectories during practice shooting sessions. Analysis of trajectories in games, however, is not typically done due to the noisiness of the location data in the SportVu database. This paper provides a method to utilize in-game shot trajectories provided by the optical tracking data to better evaluate and predict player shooting. 

19 

## **References** 

- Aesrk, J. 2010. ”Revisiting the Hot Hand Theory with Free Throw Data in a Multivariate Framework.” _Journal of Quantitative Analysis in Sports_ 6(1): Retrieved 12 Jun. 2018, from doi:10.2202/1559-0410.1198. 

- Blackport, D. 2014. ”How Long Does it Take for Three Point Shooting to Stabilize?” https://fansided.com/-2014/08/29/long-take-three-point-shooting-stabilize/. Accessed November 11th, 2017. 

- Chang, Y.H., R. Maheswaran, J. Su, S. Kwok, T. Levy, A. Wexler, and K. Squire. 2014. ”Quantifying Shot Quality in the NBA.” _Proceedings of the 2014 MIT Sloan Sports Analytics Conference_ . 

- Cen, R., H. Chase, C. Pena-Lobel, and D. Silberwasser. 2015. ”NBA Shot Prediction and Analysis.” https://hwchase17.github.io/sportvu/. Accessed November 11th, 2017. 

- Efron, B., and C. Morris. 1977. ”Stein’s paradox in statistics.” _Scientific American_ 236:119127. 

- Franks, A., A. D’Amour, D. Cervone, and L. Bornn. 2016. ”Meta-Analytics: Tools for Understanding the Statistical Properties of Sports Metrics.” _Journal of Quantitative Analysis in Sports_ 12:151-165. 

- Kubatko, J., D. Oliver, K. Pelton, and D.T. Rosenbaum. 2007. ”A Starting Point for Analyzing Basketball Statistics.” _Journal of Quantitative Analysis in Sports_ 3(3): Retrieved 12 Jun. 2018, from doi:10.2202/1559-0410.1070. 

- Marty, R. 2018. ”High-resolution Shot Capture Reveals Systematic Biases and an Improved Method for Shooter Evalutation.” _Proceedings of the 2018 MIT Sloan Sports Analytics Conference_ . 

- Marty, R. and S. Lucey. 2017. ”A Data-Driven Method for Understanding and Increasing 3-Point Shooting Percentage.” _Proceedings of the 2017 MIT Sloan Sports Analytics Conference_ . 

- Paine, N. 2016. ”LeBron’s 3-Point Shot Has Abandoned Him.” https://fivethirtyeight.com/features/lebrons-3-point-shot-has-abandoned-him/. Accessed January 3rd, 2018. 

- Piette, J., A. Sathyanarayan, and K. Zhang. 2010. ”Scoring and Shooting Abilities of NBA Players.” _Journal of Quantitative Analysis in Sports_ 6(1): Retrieved 12 Jun. 2018, from doi:10.2202/1559-0410.1194. 

- Young, S. 2016. ”The NBA’s 3-point Revolution” https://bballbreakdown.com/2016/12/16/thenba-3-point-revolution/. Accessed December 14th, 2017. 

20 


