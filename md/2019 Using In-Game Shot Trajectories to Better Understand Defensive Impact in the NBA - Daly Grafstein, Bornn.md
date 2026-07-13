<!-- source: 2019 Using In-Game Shot Trajectories to Better Understand Defensive Impact in the NBA - Daly Grafstein, Bornn.pdf -->

# Using In-Game Shot Trajectories to Better Understand Defensive Impact in the NBA 

Daniel Daly-Grafstein<sup>1</sup> and Luke Bornn<sup>1</sup> 

1Simon Fraser University 

May 3, 2019 

**Abstract** As 3-point shooting in the NBA continues to increase, the importance of perimeter defense has never been greater. Perimeter defenders are often evaluated by their ability to tightly contest shots, but how exactly does contesting a jump shot cause a decrease in expected shooting percentage, and can we use this insight to better assess perimeter defender ability? In this paper we analyze over 50,000 shot trajectories from the NBA to explain why, in terms of impact on shot trajectories, shooters tend to miss more when tightly contested. We present a variety of results derived from this shot trajectory data. Additionally, pairing trajectory data with features such as defender height, distance, and contest angle, we are able to evaluate not just perimeter defenders, but also shooters’ resilience to defensive pressure. Utilizing shot trajectories and corresponding modeled shot-make probabilities, we are able to create perimeter defensive metrics that are more accurate and less variable than traditional metrics like opponent field goal percentage. 

1 

## **1 Introduction** 

Perimeter defense in the NBA involves defenders attempting to stop, contest, or block outside jump shots by the opposing team. With three-point attempt rates continuing to rise, players’ perimeter defensive ability is an important factor in determining a team’s defensive success. However, it is difficult to quantify the ability of perimeter defenders. Additionally, while it is well-known that tightly contesting outside shots results in poorer shooting (Chang et al. 2014), little has been done to study why contesting shots decreases field-goal percentage (FG%) and how contests affect the trajectory of shots. 

Defensive metrics are in general more difficult to measure and, traditionally, provide us less information than their offensive counterparts (Franks et al. 2015). Common box score metrics such as blocks and steals rely on discrete and easily countable events that do not provide us with a full picture of a player’s defensive ability. Metrics like opponent FG% and perimeter defense rating that try to quantify perimeter defense still rely on counting discrete events and can be highly variable. For example, players’ opponent 3P% (three-point percentage where the given player is the closest defender) has almost zero correlation year-to-year (Narsu 2017). Even commonly used advanced metrics like defensive rating and adjusted plus/minus do not give us information about why certain defenders are effective or not. With the introduction of player tracking data, a suite of new defensive metrics have been developed to try and fill the gap between offensive and defensive metrics (Franks et al. 2015, Goldsberry and Weiss 2013). While many of these new metrics do incorporate spatial player information, they still do not utilize the shot trajectory information given by the optical tracking data. Metrics that are based solely on binary make/miss shot information can be unstable, as a player’s FG% over a single season is inherently low sample size and may be highly variable (Daly-Grafstein and Bornn 2019). Additionally, these metrics still do not address the question of how contesting shots causes them to miss more frequently. 

2 

In this paper we introduce a variety of results derived from shot trajectories in an attempt to quantify how contesting shots affects shooting percentage. We begin by using spatio-temporal information provided by optical tracking data to estimate shot trajectories and shot-make probabilities. We quantify each trajectory using three shot factor measures: depth, left-right distance, and entry angle (Daly-Grafstein and Bornn 2019, Marty 2018, Marty and Lucey 2017), and use these shot factors to model shot-make probabilities. Next, we pair defender and trajectory information to present a collection of results, including trajectory variation in relation to open vs. contested shots, and how defender height and distance affect shot angles and shot depths. In Section 3, we show using regression models that metrics derived from shot trajectory information stabilize inference, allowing us to estimate defender skill and shooter resiliency to defensive pressure in fewer games than previously possible. 

## **2 Methods** 

### **2.1 Dataset** 

The data used for our analysis is the SportVu spatio-temporal tracking data provided by STATS LLC. This optical tracking data provides the _x_ and _y_ coordinates of the 10 players on the court and the _x_ , _y_ , and _z_ coordinates of the ball, 25 times per second. The data are also tagged with play-by-play event codes that indicate when events such as shots, dribbles, passes, etc. take place. We restrict our analysis to 50,916 three-point shots from the 2014-15 season. Following DalyGrafstein and Bornn (2019), we now present a model for estimating shot-make probabilities. 

3 



Figure 1: A graphical depiction of the shot trajectories from the SportVu database. The points represent data from the optical tracking database, while the smooth lines represent our modeled best-fit lines estimated using the Bayesian regression model (1). 

### **2.2 Estimating Shot Trajectories** 

To accurately estimate the ball’s position near the basket, we fit a quadratic best fit line through the trajectory of each shot _i_ of the form: 



We estimate the coefficients in (1) using a Bayesian regression with a conjugate Normal prior for _β_ of the form _ρ_ ( _β |σ_<sup>2</sup> _, z, X_ ) _∼ N_ ( _u_ 0 _, σ_<sup>2</sup> Λ<sup>_−_</sup> 0<sup>1), and a conjugate inverse gamma prior</sup><sup>_ρ_(</sup><sup>_σ_2</sup><sup>_|z,X_)</sup><sup>_∼_</sup> _IG_ ( _a_ 0 _, b_ 0). The parameters of these priors are modeled using non-informative conjugate hyperpriors updated with pseudo-data reflecting our prior knowledge of shot trajectories. We specify 4 pseudo-data points: 2 set at the _x_ , _y_ location of the shooter and 7 feet in height, and 2 set at the centre of the basket and 10 feet in height. After updates using the pseudo-data and optical tracking data, we take the posterior mean of _β_ as our estimate for the coefficients in (1) (Figure 1). 

4 

We then use (1) to calculate three shot factors for each trajectory - the shot depth, left-right distance, and entry angle - following the procedure of Marty and Lucey (2017). Shot depth is defined as the depth of the ball relative to the front rim as it enters the basket. Left-right distance is defined as the deviation of the ball from the center of the hoop. Entry angle is defined as the angle between the ball and the rim as it enters the basket. See Marty and Lucey (2017) and DalyGrafstein and Bornn (2019) for further details. 

### **2.3 Modeling Shot-Make Probabilities** 

The shot trajectories and derived shot factors described above give us more information on each shot than simply whether it is a make or a miss. If we summarize this trajectory information in a shot-make probability model, we can effectively Rao-Blackwellize shooting metrics and their derivatives by conditioning each shot’s binary outcome on its make probability (Daly-Grafstein and Bornn, 2019). To accomplish this, we use the estimated shot factors described above as covariates in a logistic regression: 



with _P_ ( _Si_ = 1) representing the probability shot _i_ is a make, _σ_ (x) = exp(x) _/_ (1 + exp(x)), and _D_ ˆ _i_ , _LR_ ˆ _i_ , and _A_ ˆ _i_ representing the estimated depth, left-right distance, and entry angle of shot _i_ , respectively. We train this model using 46,093 of the 50,916 threes from the 2014-15 NBA season, removing shot trajectories that were partially missing, especially noisy, or that resulted in modeled shot trajectories from (1) that were too far from the raw data. We show the distribution of modeled probabilities in relation to our three shot factors and the basket in Figure 2. 

5 





Figure 2: Figure (a) shows the mean predicted shot-make probabilities over the range of entry angles given by (2). Figure (b) shows the distribution of predicted shot-make probabilities over different values of shot depth and left-right accuracy in relation to the basket. Note the shot-make probability legend applies to both figures 

## **3 Results** 

### **3.1 The Effect of Defenders on Shot Trajectories** 

Here we present results based on shot trajectories that help give some insight into how exactly defending shots lowers shooting percentages. Firstly, when comparing open and contested 3- point shots, we find shots that are tightly contested have a 56% larger variance in depth and a 38% larger variance in left-right distance compared to open shots (Figure 3). Contesting shots does not appear to introduce bias into the left-right accuracy of shooters, but does appear to cause shooters to bias their shots shorter than what is optimal. We also find that a smaller nearest defender distance (NDD) results in both higher entry angles and depths shorter in the hoop (Figure 4a, 4b). Additionally, conditional on defender distance, taller defenders result in higher shot trajectory angles when contesting 3-point shots (Figure 4a). The same trend is not as pronounced between defender heights and shot depths. Both our shot factors and those measured in Marty 

6 



Figure 3: The distribution of open and contested 3-point attempts from the 2014-15 NBA season. Open and contested shots are defined as attempts with a NDD greater than 6 feet and less than 4 feet, respectively. Here NDD is taken as the distance of the closest defender to the shooter when the shot is released. Depth and left-right measurements are given in feet. 

(2018) and Marty and Lucey (2017) using the Noah shooting system find that entry angles in the mid-40’s result in the highest shooting percentage. Thus it appears that taller defenders are causing opponent shot trajectories to deviate from optimal angles. However, shooting percentages are more consistent over a range of entry angles compared to either left-right distance or shot depth, indicating the effect that taller defenders have on shot angles relative to overall shooting percentages may be minor. The more important effect may be how NDD affects shot depths. As in Marty and Lucey (2017), we find shot depths between 10" and 11" maximize 3P%. In our dataset, shots landing at 9" depth are made at 60.1% of the time, while shots landing at 10" depth are made 64.5% of the time. Thus, some of the drop in expected shooting percentage caused by contesting shots may be attributed to shooters biasing their shots shorter when confronted with tight defense. When looking at if defenders affected the left-right accuracy of shots, we do not find any effect of defender angle on shot trajectories. Specifically, defenders contesting from the left or the right of the shooter do not appear to bias shots in either direction. 

7 





Figure 4: The entry angle (a) and shot depth (b) of all 3-point shot attempts during the 2014-15 season. Shot attempts are categorized by the nearest defender’s distance (NDD) and the nearest defender’s height. In Figure (b) the dotted horizontal line indicates the shot depth at which 3P% is maximized. 

### **3.2 Evaluating Perimeter Defenders and Shooters** 

As mentioned in Section 1, a player’s opponent 3P% is not a reliable perimeter defensive metric because it is quite variable, having almost no year-to-year correlation. Here we try to improve this metric by utilizing the modeled shot-make probabilities calculated in Section 2.2. To this end, we create 2 regression models to evaluate each player’s defensive ability when they are tagged as the nearest defender. The first estimates the defensive impact of each player using make/miss indicators as the response (model 1), essentially giving the magnitude of difference between 3P% when the defender of interest is defending compared to a weighted average of the offensive players’ 3P% over the season. The second model does similar, except uses shot-make probabilities as the response (model 2). These models have the form: 



8 

where _Yi jk_ is the _i_<sup>_th_</sup> shot taken by the _j_<sup>_th_</sup> player and defended by the _k_<sup>_th_</sup> player. _Yi jk_ is either a binary indicator in the case of model 1, or the modeled shot-make probability of shot _i_ in the case of model 2. Using sum-to-zero contrasts, the _α j_ ’s are the differences between each player’s 3P% and the league average in the first model, and estimated differences between each player’s mean shot-make probability and the league average shot-make probability in the second. Similarly, the _γk_ ’s are estimates of each defender’s impact on opponent 3P% in the first model, and estimates of each defender’s impact on opponent three-point shot-make probability in the second model. 

If we consider the _γk_ values estimated using binary shot outcomes over the entire 2014-15 season as each player’s true perimeter defensive impact, we can show that using shot-make probabilities allows us to estimate coefficients with less data than when using make/miss responses (Figure 5a). The MSEs of coefficients estimated using fewer than 50% of the games from the 2014-15 season are smaller when using shot-make probabilities, and these gains are especially evident at low sample sizes. Additionally, we find that when comparing ranks of defenders from the first and second half of the 2014-15 season, coefficients estimated using shot-make probabilities out= perform those estimated with make/miss outcomes in terms of consistency of player ranks ( _ρ_ 0.17 vs. 0.025, respectively). Thus, we can use our new metric to more accurately rank perimeter defenders compared to opponent 3P% (Table 1). 

We can perform a similar analysis to measure how effective shooters are at responding to defensive pressure. We again create 2 regression models, this time to evaluate how players’ shooting percentage changes based on nearest defender distance. The first model estimates the change in a player’s 3P% for every foot change in the NDD, while the second estimates the change in mean shot-make probability for every foot change in NDD. These models have the form: 



9 





Figure 5: Figure (a) depicts the mean squared error (MSE) of the _γk_ ’s from (3) estimated using 10%, 20%, 30%, 40%, and 50% of the games in the 2014-15 season. Coefficients using model 1 (Raw) and model 2 (Prob) are compared to coefficients estimated using the entire 2014-15 season data and make/miss responses. These coefficients correspond to the defensive impact of each player. Figure (b) depicts the same MSE as (a) except the coefficients correspond to each shooter’s interaction with NDD, denoted as _γ j_ in (4). 

where _Yi j_ is the _i_<sup>_th_</sup> shot taken by the _j_<sup>_th_</sup> player, and the _α j_ ’s are defined similarly to (3). The _γ j_ ’s now denote the estimated interaction effect between each shooter and the NDD. Thus the _γ j_ co- 

Table 1: Nearest Defender Impact on Shots 

|Rank|Defender|_γk ∗_100|OppProb|Rank|Defender|_γk ∗_100|OppProb|
|---|---|---|---|---|---|---|---|
|1|Boris Diaw|-6.71|30.0%|137|Derrick Williams|8.57|45.8%|
|2|Draymond Green|-5.92|32.0%|136|Channing Frye|7.15|43.0%|
|3|Langston Galloway|-5.25|30.6%|135|Vince Carter|5.96|41.7%|
|4|Patrick Beverley|-4.55|31.9%|134|Kirk Hinrich|5.93|42.2%|
|5|Wesley Johnson|-4.39|31.7%|133|Jameer Nelson|5.69|42.8%|



The top and bottom perimeter defenders estimated via (3) using shot-make probabilities from (2). The _γk ∗_ 100 values represent the estimated difference in 3-point shot-make probability percentage per 100 shots when the given player is the primary defender compared to a weighted average of probabilities based on their opponent’s shooting skill. The Opp Prob column denotes the mean estimated shot-make probability of shots where player _k_ is the closest defender. Restricted to players who defended at least 100 three-point shots during 2014-15. 

10 

efficients represent the estimated change in mean 3P% (shot-make probability) for every one foot change in the NDD for each shooter. Again we find that we can estimate coefficients using less data (Figure 5b) and that shooter rankings are more consistent when using shot-make probabilities ( _ρ_ = 0.20 vs. 0.033, respectively). Shooter rankings based on changes in shot-make probability are presented in Table 2. For example, Kemba Walker’s estimated mean three-point shot-make probability decreases 1.98% points less than the league average for every foot closer the nearest defender is. 

## **4 Discussion and Conclusion** 

Substituting shot-make probabilities for binary make/miss outcomes is an example of Rao-Blackwellizing FG%. If we model shots as Beta-Bernoulli random variables, shot-make probabilities become a sufficient statistic for shooting ability, and thus conditioning on these probabilities will, by the Rao-Blackwell theorem, result in an estimator with lower variance (Daly-Grafstein and Bornn 

Table 2: Perimeter Shooter Resiliency to Shot Contests 

|Rank|Shooter|_γj ∗_100|Rank|Shooter|_γj ∗_100|
|---|---|---|---|---|---|
|1|Michel Carter-Williams|3.45|137|Aaron Brooks|-2.54|
|2|Rasual Butler|3.39|136|Langston Galloway|-2.41|
|3|Austin Rivers|2.86|135|Russell Westbrook|-2.37|
|4|Kemba Walker|1.98|134|Nik Stauskas|-2.35|
|5|Gerald Henderson|1.58|133|Rovert Covington|-2.02|



The top and bottom shooters resilient to defensive pressure estimated via (4) using shot-make probabilities. Values represent the estimated change in each player’s 3-point shot-make probability per 100 shots for every 1 foot decrease in NDD relative to the league average. Restricted to players who attempted at least 100 three-point shots during 2014-15. 

11 

2019). The results presented in this paper are just a few examples of the improvements RaoBlackwellization can give. With tracking data now available in hockey, football, and soccer, trajectory data can be leveraged to calculate similar goal/pass-make probabilities that may result in improvements similar to those seen in this paper. 

The results presented in Section 3 illustrate the improvements gained by using shot trajectories estimated from the tracking data to evaluate defender skill. We believe this work has opened up many areas of future research. For example, nearest defender distance is not the most reliable way to quantify the defensive pressure on a shot. It does not give us any indication of how the defender is oriented in relation to the shooter, and also may tag a player that is not the primary defender. We may be able to improve our defensive impact metric by using a more reliable measure of who the primary defender is (e.g. Franks et al. 2015), or by trying to incorporate the intensity of the defensive contest (e.g. Csapo and Raab 2014). Furthermore, we defined a relatively simple model in (3) that estimates a mean for each player’s defensive impact. Conditioning on other covariates, such as shot location, shooter position, or even NDD, may give a more accurate estimation of players’ perimeter defensive ability. Finally, opponent FG%, and its counterpart based on shot-make probabilities defined in this paper, may themselves be flawed metrics in evaluating perimeter defense. These metrics do not take into account defenders who stopped opponents from attempting a shot, forced their opponent to pass or create a turnover, or even prevented the opponent shooter from receiving the ball altogether. Combining the metrics defined in this paper with those that account for how defenders affect shot volumes and efficiency over the course of an entire defensive possession (e.g. Franks et al. 2015) may give a fuller picture of a player’s perimeter defensive ability. 

In this paper we sought to provide new descriptions for how defenders affect shots as well as construct metrics that are better able to estimate perimeter defender and shooter behavior. Following Marty and Lucey (2017), we presented a variety of results derived from shot trajectories. Similar 

12 

to Marty and Lucey (2017), we found that three-point probabilities are highest at a depth of 10", and shots have a fairly consistent make probability over a range of entry angles. Additionally, we found that NDD increases variability in shot depth, while also biasing shots short. However, neither NDD nor defender angle seemed to bias the left-right location of shot trajectories, with NDD only increasing its variability. Thus it appears players are shooting with sub-optimal shot depths when facing defensive pressure. This may give players that train to correct this bias an opportunity to improve their three-point shooting. Furthermore, our new metrics based on makeprobabilities decreased the variation in estimation relative to their raw counterparts. These metrics may allow coaches to more accurately assess a player’s perimeter defense, as well as indicate which outside shooters are most affected by tight defensive pressure. Teams could use this information to make better decisions about which players to guard on the three-point line, or to better evaluate their players’ shot selection based on defensive pressure. 

## **References** 

- Chang, Y.H., R. Maheswaran, J. Su, S. Kwok, T. Levy, A. Wexler, and K. Squire. 2014. "Quantifying Shot Quality in the NBA." _Proceedings of the 2014 MIT Sloan Sports Analytics Conference_ . 

- Csapo, P. and M. Raab. 2014. "Hand down, man down. Analysis of defensive adjustments in response to the hot hand in basketball using novel defense metrics." _PLoS ONE_ 9(12): Retrieved 19 Feb. 2019, from https://doi.org/10.1371/journal.pone.0114184. 

- Daly-Grafstein, D. and L. Bornn. 2019. "Rao-Blackwellizing field goal percentage." _Journal of Quantitative Analysis in Sports_ 0(0): Retrieved 19 Feb. 2019, from doi:10.1515/jqas2018-0064. 

- Franks, A., A. Miller, L. Bornn, and K. Goldsberry. 2015. "Characterizing the spatial structure of defensive skill in professional basketball." _Annals of Applied Statstics_ 9(1): 94-121. 

- Franks, A., A. Miller, L. Bornn, and K. Goldsberry. 2015. "Counterpoints: Advanced defensive metrics for NBA basketball." _Proceedings of the 2015 MIT Sloan Sports Analytics Conference_ . 

13 

- Goldsberry, K., and E. Weiss. 2013. "The Dwight effect: A new ensemble of interior defense analytics for the NBA." _Proceedings of the 2013 MIT Sloan Sports Analytics Conference_ . 

- Marty, R. 2018. "High-resolution shot capture reveals systematic biases and an improved method for shooter evaluation." _Proceedings of the 2018 MIT Sloan Sports Analytics Conference_ . 

- Marty, R. and S. Lucey. 2017. "A data-driven method for understanding and increasing 3-point shooting percentage." _Proceedings of the 2017 MIT Sloan Sports Analytics Conference_ . 

- Narsu, K. 2017. "Shot defense and separating metrics from actions." htpps://fansided.com/2017/01/12/nyloncalculus-shot-defense-metrics-actions/. Accessed December 3rd, 2018. 

14 


