<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Models for Third Down Conversion in the National Football League - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1383 

## Models for Third Down Conversion in the National Football League 

**Ryan Cafarelli,** _Southern Illinois University Edwardsville_ **Christopher J. Rigdon,** _Southern Illinois University Edwardsville_ **Steven E. Rigdon,** _Saint Louis University_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1383 

## Models for Third Down Conversion in the National Football League 

Ryan Cafarelli, Christopher J. Rigdon, and Steven E. Rigdon 

### **Abstract** 

Several models are proposed for the probability of converting a third down attempt in the National Football League. The probability, which can depend on the number of yards to go, the strength of the offense, and the strength of the defense, leads to a logistic regression. We approach the problem through a hierarchical Bayes model and estimate parameters by using Markov chain Monte Carlo (MCMC). This MCMC estimation in the context of a hierarchical Bayes model may be relevant in other sports situations where a probability depends on the difference of strengths of the two teams. We find that the statistic "third-down conversion rate" to be a nearly meaningless measure of the efficiency of an offense. Even when this is adjusted for yards to go for a first down, there is little evidence that teams differ in their ability to achieve a first down on a third down conversion. 

**KEYWORDS:** hierarchical Bayes, Markov chain Monte Carlo 

**Author Notes:** We wish to thank the editor and two reviewers whose comments and suggestions at every step have certainly led to a better presentation of the material. 

Cafarelli et al.: Third Down Conversions in the NFL 

### 1. Introduction and Background 

American football began in the 1870s as a continuous flow game similar to rugby. Players could carry the ball, pass the ball (backwards or sideways), or kick the ball. If a player was tackled with the ball, a scrum (a sort of “face off” with both teams arranged in a tight pattern) ensued. A player who carried the ball across the goal line got a chance (against no opposition) to kick the ball through the goal posts. This free flowing game changed in 1880 (see Carroll, Palmer and Thorne, 1998) when Walter Camp introduced rules that would allow one team to maintain possession. After a player was tackled, his team was allowed to kick the ball (not “hike”) from the point of the tackle to another player on his team. Thus, the scrum was replaced by the “line of scrimmage.” There was no limit to the number of times that a team could repeat this process. Weak teams were therefore able to hold on to the ball (much like the “four corners”offense in college basketball before the introduction of the shot clock) and run the clock out. The next year, the rules were changed to give teams just three chances (or downs) to have the ball. If the team gained five yards or lost ten yards from the original line of scrimmage, they got a new set of downs, or a “first down”in modern language. In 1910 a fourth down was added. 

Current rules allow a team four downs to advance the ball ten yards, and if this is achieved, the team gets a new set of four downs (i.e., a first down). If a team fails to advance the ball ten yards, the opposing team takes over possession at the current line of scrimmage. On fourth down (the last chance to get a first down), most teams choose to punt (kick) the ball to the other team. This often puts the ball 35 to 40 yards down the field where the other team takes possession. Punting is done to avoid the risk of not making a first down on a fourth down attempt and giving the ball to the other team in a much better position (from the view of the opposing team). Therefore, third down is usually the last chance a team has to make a first down. 

Data are kept and reported on the number of third down plays and the number of conversions. We often hear during an NFL telecast statistics about what percentage of times a team has been successful on their third-down plays. For example, we might hear that one team is 0 for 4, while their opponent is 3 for 5. Since the likelihood of making a first down on a third down play depends on the number of yards to go on third down, these raw statistics can be misleading. In the example stated, the team that was 0 for 4 might have had several penalties and incomplete passes early in their set of downs, leading to third-and-long every time. On the other hand, the team that was 3 for 5 might have been successful gaining a few yards by running or passing on first 

1 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

and second down, setting up third and short on most of their third down plays. It is clear then, that the raw percentage of successful third-down attempts is not a good measure of the team’s play on third down. 

One might think that over the course of a season, the yards to go (YTG) on third down will average out. There is, in fact, quite a bit of variability in the distribution of YTG across the 32 NFL teams. Figure 1 shows histograms for the YTG for all 32 teams for the 2007 season. The average YTG varied from 5.8 for the Saints to 7.7 for the Rams. For many teams, the number of yards to go on third down is roughly uniform over the interval from 1 to 10, with probabilities tailing off after 10 yards. Teams facing fewer YTG on average will tend to have a higher conversion rate for this reason alone. For example, the Saints had the lowest average YTG on third down (5.8) and the highest raw third down conversion rate (56.7%) and the Rams had the highest YTG on third down (7.7) and the lowest raw conversion rate (28.1%). Table 1 shows the 2007 NFL standings, the raw third-down conversion rates, and other statistics for the season. 

Even if the teams’yards to go on third down averaged about the same, comparing the percentage of times that teams convert third down plays is still troublesome because some teams play in a division that is loaded with strong defensive teams. A team that makes 30% of first downs in a division with weak defensive teams will not be as strong as a team that makes 30% of its first downs in a division with stronger defensive teams. 

In order to compare the strengths of offenses in converting third down plays adjusted for YTG (and in the case of Model 3, the strengths of defensive teams in stopping third down plays) we propose three models for the probability of a successful a third-down conversion. 

Model 1 assumes that the probability depends on YTG according to a logistic regression model, but does not depend on the offensive or defensive teams. 

Model 2 assumes that the probability depends on YTG and which team is on 

Model 3 assumes that the probability depends on YTG and both the and defensive teams. 

For Model 1, we propose a Bayesian model for the parameters in the logistic regression. For Models 2 and 3, we propose a hierarchical Bayes model for the team-specific parameters. A hierarchical Bayes approach borrows information across all other teams in the sense that all other teams 

2 

Cafarelli et al.: Third Down Conversions in the NFL 

**Figure 1:** Histograms of yards to go on third down.  There were a few instances of more than thirty yards to go (Bears 3rd and 37, Chargers 3rd and 31 and 3rd and 32, Giants 3rd and 33, Raiders 3rd and 31 and 3rd and 40, Seahawks 3rd and 40, Steelers 3rd and 31, and Texans 3rd and 35).  The number within each plot is the average number of yards to go. 



<!-- Start of picture text -->
49ers Bears Bengals Bills<br>7.1 7.5 6.2 6.9<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Broncos Browns Buccaneers Cardinals<br>7.1 6.8 6.5 7.3<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Chargers Chiefs Colts Cowboys<br>7.4 7.2 5.9 7.3<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Dolphins Eagles Falcons Giants<br>7.0 6.4 7.4 6.4<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Jaguars Jets Lions Packers<br>6.9 6.9 7.4 6.4<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Panthers Patriots Raiders Rams<br>6.8 6.0 7.3 7.7<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Ravens Redskins Saints Seahawks<br>6.7 6.4 5.8 6.6<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>Steelers Texans Titans Vikings<br>7.5 6.0 6.8 7.3<br>0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30<br>30<br>0<br>30<br>0<br>30<br>0<br>30<br>0<br>30<br>0<br>30<br>0<br>30<br>0<br>30<br>0<br><!-- End of picture text -->

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

**Table 1:** Standings, Points, Yards, Turnovers and Raw Third Down Conversion Rates for the 2007 NFL Season 

|||||**Points**|||**Yards**||**Tu**|**rnove**|**rs**|**Raw 3rd**<br>**Down**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**AFC East**|**W **|**L**|**For  A**|**gainst**|**Diff**|**For**|**Against**|**Diff**|**For A**|**gainst**|**Diff**|**Conv Rate**|
|New England Patriots|16|0|589|274|315|6580|4613|1967|31|15|16|45.9|
|Buffalo Bills|7|9|252|354|−102|4434|5807|<sup>−1373</sup>|30|21|9|32.5|
|New York Jets|4|12|268|355|−87|4715|5310|−595|21|25|−4|34.7|
|Miami Dolphins|1|15|267|437|−170|4600|5475|−875|22|29|−7|33.3|
|**AFC North**|||||||||||||
|Pittsburgh Steelers|10|6|393|269|124|5239|4262|977|25|22|3|45.9|
|Cleveland Browns|10|6|402|382|20|5621|5753|−132|27|29|−2|38.7|
|Cincinnati Bengals|7|9|380|385|−5|5568|5580|−12|35|30|5|36.5|
|Baltimore Ravens|5|11|275|384|−109|4832|4825|7|23|40|−17|42.4|
|**AFC South**|||||||||||||
|Indianapolis Colts|13|3|450|262|188|5739|4475|1264|37|19|18|34.6|
|Jacksonville Jaguars|11|5|411|304|107|5719|5021|698|30|21|9|33.6|
|Tennessee Titans|10|6|301|297|4|4987|4665|322|34|34|0|36.7|
|Houston Texans|8|8|379|384|−5|5337|5507|−170|25|38|−13|41.5|
|**AFC West**|||||||||||||
|San Diego Chargers|11|5|412|284|128|5044|5124|−80|48|24|24|48.8|
|Denver Broncos|7|9|320|409|−89|5541|5376|165|30|29|1|30.8|
|Oakland Raiders|4|12|283|398|−115|4717|5466|−749|26|37|−11|35.7|
|Kansas CityChiefs|4|12|226|335|−109|4429|5111|−682|22|33|−11|36.0|
|||||**Points**|||**Yards**||**Tur**|**nove**|**rs**|**Raw 3rd**<br>**Down**|
|**NFC East**|**W **|**L**|**For  A**|**gainst**|**Diff**|**For**|**Against**|**Diff**|**For A**|**gainst**|**Diff**|**Conv Rate**|
|Dallas Cowboys|13|3|455|325|130|5851|4922|929|29|24|5|39.4|
|New York Giants|10|6|373|351|22|5302|4880|422|25|34|−9|37.4|
|Washington Redskins|9|7|334|310|24|5334|4884|450|24|29|−5|37.0|
|Philadelphia Eagles|8|8|336|300|36|5729|4982|747|19|27|−8|41.5|
|**NFC North**|||||||||||||
|Green Bay Packers|13|3|435|291|144|5931|5013|918|28|24|4|48.1|
|Minnesota Vikings|8|8|365|311|54|5379|5410|−31|31|30|1|38.4|
|Detroit Lions|7|9|346|444|−98|5166|6042|−876|35|36|−1|35.8|
|Chicago Bears|7|9|334|348|−14|4692|5675|−983|33|34|−1|32.5|
|**NFC South**|||||||||||||
|Tampa Bay Bucs|9|7|334|270|64|5229|4454|775|35|20|15|36.9|
|Carolina Panthers|7|9|267|347|−80|4559|5197|−638|30|29|1|40.5|
|New Orleans Saints|7|9|379|388|−9|5780|5570|210|23|30|−7|56.7|
|Atlanta Falcons|4|12|259|414|−155|4816|5688|−872|28|24|4|44.2|
|**NFC West**|||||||||||||
|Seattle Seahawks|10|6|393|291|102|5583|5149|434|34|24|10|33.8|
|Arizona Cardinals|8|8|404|399|5|5505|5283|222|29|36|−7|32.2|
|San Francisco 49ers|5|11|219|364|−145|3797|5539|<sup>−1742</sup>|22|34|−12|29.4|
|St. Louis Rams|3|13|263|438|−175|4760|5457|−697|27|37|−10|28.1|



4 

Cafarelli et al.: Third Down Conversions in the NFL 

the estimates of the hyperparameters, which in turn affect the estimates of parameters from the individual teams. With many parameters to estimate, a frequentist approach is likely to produce estimates that are too disperse, whereas a hierarchical Bayes method will tend to shrink the estimates toward the middle. The assumption that the teams vary in their ability to do any task makes sense. For example, if team i’s “true”ability on some task is θi, and if the abilities vary across all teams, then it seems reasonable, that θ1, θ2, . . . , θ32 have some common prior distribution. This is similar to a random effects model in ANOVA, where the treatment means are assumed to have come from some distribution. This leads to the concept of exchangeability as discussed in Albert and Chib (1997). 

Section 2 describes the logistic model and how it accounts for YTG and the teams on offense and defense. Sections 3, 4, and 5 describe, respectively, Models 1, 2, and 3. For Models 2 and 3 we describe a hierarchical Bayes model and we use Markov chain Monte Carlo (MCMC) to estimate the parameters. This MCMC estimation in the context of a hierarchical Bayes model may be relevant in other sports situations where a probability depends on the difference of strengths of the two teams or players. 

### 2. The Logistic Model 

We assume that the probability π of making a first-down depends on YTG, which we call x, in the logistic form 



or, in terms of the logit, or log odds transformation, 



We can make various assumptions about the parameters α and β. The simplest model, of course, is to assume that α and β are the same for every third down play, regardless of the offensive or defensive team. This is Model 1, and is analyzed in the next section. 

Model 2 assumes that the parameters α and β depend on the offensive team, but not on the defensive team. In this case, the probability that team i converts a third-down-and-x-yards-to-go is 



_Submission to Journal of Quantitative Analysis in Sports_ 

Here, αi and βi represent the slope and intercept for logit π for team i. 

The most thorough model (Model 3) assumes different α parameters and different β parameters for the offensive and defensive teams. Under this model, the parameters α and β in (1) and (2) depend on the difference between the strength of the offense and defense; specifically, α = αOi − αDj and β = βOi − βDj. The logit is thus 



which makes the probability of conversion equal to 



The differencing in (5) creates an identifiability problem, because adding any fixed constant to both αOi and αDj (or to βOi and βDj) produces exactly the same probability. With a hierarchical Bayes method, we can overcome this identifiability problem by “anchoring” the prior distribution for two of the parameters at 0. We have assumed that the prior distributions for the defensive parameters αDj and βDj have mean zero (although we could just as easily have done this for the offensive parameters instead). With the defensive parameters having a prior mean of zero, we can then interpret the parameters αOi, βOi, αDj, and βDj in (5) from the perspective of offensive team i. The probability of making a first down involves the parameters αOi and βOi, just as with any first-order logistic regression, but these values are adjusted up or down according to the strength of the defense that team i is facing at the time. 

If we knew the strengths of the defenses, i.e., the αDj and βDj parameters, then we could use the method of maximum likelihood or a straightforward Bayesian approach to estimate the offensive parameters αOi and βOi; conversely, if we knew the offensive parameters, we could estimate the defensive parameters. The problem is that neither is known. This is similar to the problem in educational measurement, where we often want to estimate the ability of a set of examinees and simultaneously the diffi culty of the test items; in this situation, the probability of getting a test item correct is a function of the difference between the examinee’s ability and the item diffi culty. This problem has been addressed by Bock and Aitken (1981) and Rigdon and Tsutakawa (1983), who applied the EM algorithm of Dempster, Laird, and Rubin (1977), although Albert and Chib (1997) suggested a more effi cient, and more generally applicable, method using Markov chain Monte Carlo (MCMC). We will address the use of MCMC in the next section. This model is related to 

6 

#### Cafarelli et al.: Third Down Conversions in the NFL 

a Bradley-Terry (1952) model since the log-odds of success involves a difference between parameters for the offense and the defense. Bock (1997) pointed out the connection between the educational measurement problem and the Bradley-Terry model. 

We analyze data from the 2007 NFL season. For each third down attempt, we recorded the offensive team, the defensive team, the yards to go, and whether a was achieved. 



and 

xijk = number of yards needed to make a first down. 

Then, Yijk has a Bernoulli distribution (i.e., a binomial distribution with n = 1) having probability of success πijk. Under Model 3, this is 



giving altogether 128 unknown model parameters that must be estimated: 32 values (one for each NFL team) for αOi, 32 values for αDj, 32 values for βOi, and 32 values for βDj. 

### 3. Model 1: Conversion Probability Curve is the Same for All Teams 

The simplest model assumes that all teams have the same logistic curve for the probability of making a first down on a third down attempt. In this case, the probability is just 



There are just two parameters to estimate: α and β. For Model 1, we assume very diffuse independent priors: α ∼ N (0, 1), and β ∼ N (0, 1) . With such a large sample, the prior has little effect on the posterior distribution. 

We then used the software WinBUGS (Lunn et al. (2000)) which uses Gibbs sampling to estimate the posterior distributions through simulation. Basically, Gibbs sampling simulates through several thousand iterations of a Markov process whose steady state distribution is the desired posterior distribution. Thus, we need to simulate until the steady state is essentially reached, and then simulate enough additional observations (from the steady state) that we 

7 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

can get a good idea about the important characteristics, such as the posterior mean and standard deviation. The simulations made before we infer that the steady state is reached is called the burn-in. In Appendix A we discuss the issue of convergence to the steady state. We have found that several hundred to a few thousand iterations is generally suffi cient for the burn-in period. We thus discard the first 10,000 iterations, and then run an additional 100,000 iterations (110,000 in total). We do this for four separate starting points, giving a total of 400,000 observations from which we estimate the posterior distributions. The parameter estimates for this model are shown in Table 2, and the estimated logistic curve is shown in Figure 2. 

Table 2: Parameter estimates α and β in Model 1. 

||Posterior|Posterior|
|---|---|---|
|Parameter|Mean|St. Dev.|
|α|0.6448|0.04724|
|β|−0.1529|0.00654|



As expected, the estimate for β is negative, indicating that as YTG increases, the probability of conversion decreases. If α + βx is fairly close to zero, then 



so that each additional YTG decreases the probability of successful conversion by approximately 0.1529/4 ≈ 0.04. 

### 4. Model 2: Separate Curves for Each Offensive Team 

Model 2 assumes that the conversion probability depends on YTG and on the offensive team, but not on the defensive team. We assume that the model parameters (the α’s and β’s) have prior distributions 



Here, the τ ’s represent the prior precision, that is, the reciprocal of the variance. (The reason for using τ 3 instead of τ 2 will become apparent in the next section.) The parameters µ1, µ2, τ 1, and τ 3 are called hyperparameters, and each has its own prior distribution whose parameters are known. (If we assumed these parameters were unknown, we would have to put priors on these, 

8 

#### Cafarelli et al.: Third Down Conversions in the NFL 

**Figure 2:** Probability of first down conversion assuming all teams have the same offensive and defensive strength (Model 1) 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>5 10 15 20<br>Yards to Go<br>Figure 3:   Probability of first down conversion on offense for each of the 32<br>teams against an average defense under Model 3.<br>1.0<br>0.8<br>0.6<br>Steelers<br>0.4<br>0.2 49ers<br>0.0<br>5 10 15 20<br>Yards to Go<br>Probability of Conversion<br>Probability of Conversion<br><!-- End of picture text -->

**Figure 4:** Probability of allowing a first down conversion by offense for each of the 32 teams against an average offense under Model 3. 



<!-- Start of picture text -->
1.0<br>Colts<br>0.8<br>Lions<br>0.6<br>0.4<br>0.2<br>Chiefs &<br>Patriots<br>0.0<br>5 10 15 20<br>Yards to Go<br>Probability of Conversion<br><!-- End of picture text -->

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

and the process would never end.) The choice of prior distributions for Model 3 is detailed in Appendix B. We use the same priors for Model 2 as we do for Model 3, although Model 3 has more parameters. The prior distributions for µ1, µ2, τ 1, and τ 3 are 



Point estimates of parameters are taken to be the posterior means. Estimates of the hyperparameters are shown in Table 3 and estimates for the model parameters (32 α’s and 32 β’s) are shown in Table 4. 

Table 3: Estimates of hyperparameters for Model 2. 

||Posterior|Posterior||Posterior|Posterior|
|---|---|---|---|---|---|
|Parameter|Mean|St. Dev.|Parameter|Mean|St. Dev.|
|µ1|0.6497|0.05553|τ1|31.61|12.10|
|µ2|−0.1533|0.008891|τ3|776.4|223.8|



### 5. Model 3: A Hierarchical Bayes Model with Parameters for Each and Defensive Team 

We consider a model with two parameters (αOi and βOi) for each offense and two parameters (αDj and βDj) for each defense. To estimate the 128 parameters (32 values for each of αOi, αDj, βOi, βDj), we take a hierarchical Bayes approach and assume priors 



Here the τ ’s represent the precision of the normal distribution, that is, the reciprocal of the variance. The parameters µ1, µ2, τ 1, τ 2, τ 3, and τ 4 are hyperparameters, and each has its own prior distribution which is known completely. Note that the defensive parameters have a prior centered at 0, whereas the offensive parameters αOi and βOi have priors that are centered at arbitrary values: µ1 and µ2, respectively. Altogether, there are 134 parameters to estimate: 4 × 32 = 128 parameters in the logistic model, plus the six hyperparameters. 

10 

Cafarelli et al.: Third Down Conversions in the NFL 

**Table 4:** Estimated  parameters α O and β O for Model 2. 

||αO|,_i_|βO|,_i_|
|---|---|---|---|---|
|**Team**|**Posterior**<br>**Mean**|**Posterior**<br>**StDev**|**Posterior**<br>**Mean**|**Posterior**<br>**StDev**|
|49ers|0.2309|0.0323|−0.1697|0.0230|
|Bears|0.2400|0.0318|−0.1791|0.0221|
|Bengals|0.3582|0.0409|−0.1305|0.0223|
|Bills|0.2439|0.0370|−0.1630|0.0243|
|Broncos|0.3059|0.0371|−0.1436|0.0219|
|Browns|0.3242|0.0379|−0.1468|0.0223|
|Buccaneers|0.2624|0.0363|−0.1690|0.0234|
|Cardinals|0.2742|0.0353|−0.1652|0.0222|
|Chargers|0.3194|0.0365|−0.1336|0.0215|
|Chiefs|0.2429|0.0329|−0.1695|0.0223|
|Colts|0.3640|0.0423|−0.1373|0.0226|
|Cowboys|0.3300|0.0380|−0.1439|0.0216|
|Dolphins|0.2807|0.0351|−0.1607|0.0220|
|Eagles|0.2723|0.0358|−0.1780|0.0231|
|Falcons|0.2745|0.0330|−0.1568|0.0213|
|Giants|0.2761|0.0369|−0.1767|0.0233|
|Jaguars|0.3570|0.0378|−0.1229|0.0209|
|Jets|0.2971|0.0355|−0.1412|0.0216|
|Lions|0.2584|0.0358|−0.1646|0.0227|
|Packers|0.3262|0.0394|−0.1326|0.0225|
|Panthers|0.2522|0.0338|−0.1692|0.0226|
|Patriots|0.3494|0.0430|−0.1451|0.0237|
|Raiders|0.2949|0.0365|−0.1529|0.0221|
|Rams|0.2871|0.0342|−0.1475|0.0210|
|Ravens|0.2622|0.0339|−0.1645|0.0224|
|Redskins|0.2954|0.0366|−0.1492|0.0226|
|Saints|0.3329|0.0409|−0.1416|0.0230|
|Seahawks|0.2508|0.0350|−0.1639|0.0233|
|Steelers|0.3887|0.0372|−0.1178|0.0199|
|Texans|0.2679|0.0393|−0.1771|0.0248|
|Titans|0.2979|0.0380|−0.1565|0.0228|
|Vikings|0.2635|0.0343|−0.1668|0.0223|



11 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

The prior distributions for the parameters were based on data from the 2003 season (Rigdon and Rigdon, 2004) and were selected so that any reasonable logistic curve has a chance of occurring a priori. If anything, we err on the side of having priors that are too diffuse, rather than too tight. We chose the following priors for the hyperparameters; the explanation of how these prior parameters were obtained is a bit involved, so we put the explanation in Appendix B. The priors are 



For a reader interested in just whether these priors are broad enough to cover any reasonable logistic curve, we suggest taking a look at Figure 9, where we plot one hundred logistic curves whose parameters were chosen at random from these prior distributions. Although there are some clearly unreasonable curves, any reasonable curve should be covered by these priors. 

Again, we used WinBUGS to estimate the posterior distributions. The estimates for the six hyperparameters (µ1, µ2, τ 1, τ 2, τ 3, τ 4) are shown in Table 5. Table 6 shows the posterior mean and standard deviation of all 4×32 = 128 of the model parameters for Model 3. The posterior means for the defensive “intercept”parameters and the defensive “slope”parameters are centered very close to zero, which is to be expected since the prior mean was 0. 

Table 5: Estimates of hyperparameters for Model 3. 

||Posterior|Posterior||Posterior|Posterior|
|---|---|---|---|---|---|
|Parameter|Mean|St. Dev.|Parameter|Mean|St. Dev.|
|µ1|0.6614|0.06279|τ1|30.88|11.93|
|µ2|−0.1548|0.01097|τ2|37.60|13.73|
||||τ3|728.90|213.30|
||||τ4|734.00|214.70|



All 32 logistic curves for offensive teams playing against an average defensive team under Model 3 are shown in Figure 3. The curve that is lowest (almost uniformly) belongs to the 49ers. While there are many teams having nearly the highest curve, the Steelers’curve is clearly the highest past about 8 YTG. Figure 4 shows the logistic curves for the probability of an average offensive team converting a third down and x yards to go against each of the 32 defensive teams. The teams with the highest and lowest curves are noted on Figure 4. 

12 

Cafarelli et al.: Third Down Conversions in the NFL 

**Table 6:** Estimated  parameters α O, α D, β O, and β D for Model 3. 

||αO|,_i_|αD|,_i_|βO|,_i_|βD|,_i_|
|---|---|---|---|---|---|---|---|---|
|**Team**|**Posterior**<br>**Mean**|**Posterior **<br>**StDev**|**Posterior**<br>**Mean**|**Posterior **<br>**StDev**|**Posterior**<br>**Mean**|**Posterior **<br>**StDev**|**Posterior**<br>**Mean**|**Posterior**<br>**StDev**|
|49ers|0.4918|0.1573|−0.0494|0.1334|−0.1751|0.0246|0.0081|0.0229|
|Bears|0.6404|0.1509|0.1000|0.1360|−0.1863|0.0235|0.0174|0.0232|
|Bengals|0.7378|0.1494|0.0272|0.1344|−0.1300|0.0238|−0.0052|0.0240|
|Bills|0.5012|0.1567|−0.0391|0.1376|−0.1645|0.0255|−0.0049|0.0225|
|Broncos|0.6300|0.1539|−0.0413|0.1350|−0.1450|0.0233|−0.0174|0.0227|
|Browns|0.7418|0.1543|0.1331|0.1396|−0.1468|0.0238|−0.0092|0.0224|
|Buccaneers|0.6491|0.1487|−0.0238|0.1356|−0.1745|0.0247|0.0113|0.0230|
|Cardinals|0.6859|0.1540|−0.0663|0.1357|−0.1708|0.0235|−0.0018|0.0219|
|Chargers|0.5937|0.1543|0.0025|0.1358|−0.1327|0.0231|0.0002|0.0228|
|Chiefs|0.5584|0.1515|0.1094|0.1401|−0.1738|0.0236|0.0260|0.0232|
|Colts|0.8214|0.1506|−0.1587|0.1411|−0.1343|0.0243|0.0257|0.0244|
|Cowboys|0.7334|0.1547|−0.0387|0.1376|−0.1441|0.0232|−0.0091|0.0217|
|Dolphins|0.6862|0.1516|−0.0638|0.1368|−0.1575|0.0236|−0.0177|0.0220|
|Eagles|0.8093|0.1511|0.0346|0.1343|−0.1827|0.0246|0.0101|0.0224|
|Falcons|0.5839|0.1515|0.0363|0.1353|−0.1642|0.0227|0.0234|0.0246|
|Giants|0.8166|0.1526|0.0559|0.1392|−0.1782|0.0247|−0.0041|0.0221|
|Jaguars|0.6307|0.1495|−0.0088|0.1377|−0.1192|0.0225|−0.0156|0.0215|
|Jets|0.5630|0.1507|−0.0750|0.1378|−0.1370|0.0231|0.0282|0.0242|
|Lions|0.6039|0.1533|0.0285|0.1331|−0.1657|0.0241|−0.0439|0.0225|
|Packers|0.6030|0.1506|0.0815|0.1372|−0.1328|0.0241|−0.0144|0.0218|
|Panthers|0.5995|0.1495|−0.0113|0.1345|−0.1715|0.0241|−0.0180|0.0220|
|Patriots|0.8344|0.1552|0.0896|0.1390|−0.1458|0.0250|0.0244|0.0236|
|Raiders|0.6570|0.1525|−0.0122|0.1360|−0.1540|0.0237|0.0233|0.0222|
|Rams|0.5706|0.1521|−0.0254|0.1393|−0.1515|0.0224|−0.0142|0.0217|
|Ravens|0.6084|0.1500|0.0641|0.1363|−0.1685|0.0237|0.0198|0.0230|
|Redskins|0.6266|0.1501|−0.0135|0.1348|−0.1513|0.0241|0.0209|0.0231|
|Saints|0.7252|0.1466|0.0031|0.1371|−0.1421|0.0244|−0.0288|0.0220|
|Seahawks|0.5531|0.1527|0.0074|0.1356|−0.1675|0.0247|0.0002|0.0218|
|Steelers|0.7427|0.1518|−0.0090|0.1369|−0.1197|0.0213|−0.0082|0.0214|
|Texans|0.7700|0.1515|−0.0397|0.1383|−0.1800|0.0263|−0.0041|0.0226|
|Titans|0.7068|0.1523|−0.0920|0.1349|−0.1567|0.0243|0.0298|0.0230|
|Vikings|0.6563|0.1539|0.0208|0.1357|−0.1669|0.0236|−0.0175|0.0219|



13 

_Submission to Journal of Quantitative Analysis in Sports_ 

The Colts were the weakest third-and-1 team, while the Lions were the worst third-and-long team. (We consider third down and six or more yards to go to be third and long.) The Chiefs and Patriots are the two best teams at stopping third and long. 

From Table 6, we can estimate the probability of any team successfully converting a third down and x YTG against any defensive team, under the assumptions of Model 3. Consider, for example the probability of the 49ers converting a third-and-x against the Chiefs (the best at stopping third-and-1) and the Colts (the worst at converting a third-and-1). The estimated logistic curve for the 49ers versus the Chiefs is 



The curve for the 49ers versus the Colts is determined similarly. The probability of the 49ers converting a third-and-1 is 0.545 against the Chiefs and 0.611 against the Colts. These two curves, displayed in Figure 5, show the extent of the differences among the offensive teams. Figure 6 shows how the curves can differ for the 49ers (the worst third-and-10 team) against the best (Chiefs) and worst (Lions) at stopping a third-and-10. The probabilities of the 49ers converting a third-and-10 against the Chiefs is 0.164 and against the Lions is 0.300. 

For Model 3, Figure 7 shows the probabilities and margins of error for making a third-and-1 and a third-and-10 conversion for all 32 teams, ranked from lowest to highest. Playoff teams for the year 2007 are shown in red. 

### 6. Discussion 

To get a rough measure of the logistic fit, consider Figure 8, where we have plotted the actual conversion rates for third-and-x for x = 1, 2, . . . , 10 for each of the 32 NFL teams. The curve shown on each graph is the logistic curve if the team played against an average defense. Note that this is not simply the logistic curve estimated from the given team’s data. For some teams, such as the Patriots, most of the points are above the curve, suggesting that they tended to play below average defensive teams. Other teams, such as 

14 

Cafarelli et al.: Third Down Conversions in the NFL 

**Figure 5:** Estimated probability of conversion for the worst 3rd-and-1 team (the 49ers) versus the best (Chiefs) and worst (Colts) 3rd-and-1 defenses. 



<!-- Start of picture text -->
1.0<br>0.8<br>vs. Colts<br>0.6<br>0.4<br>vs. Chiefs<br>0.2<br>0.0<br>5 10 15 20<br>Yards to Go<br>Figure 6:   Estimated probability of conversion for the worst 3rd-and-10 team<br>(the 49ers) versus the best (Chiefs) and worst (Lions) 3rd-and-10 defenses.<br>1.0<br>0.8<br>0.6<br>0.4<br>vs. Lions<br>0.2<br>vs. Chiefs<br>0.0<br>5 10 15 20<br>Yards to Go<br>Probability of Conversion<br>Probability of Conversion<br><!-- End of picture text -->

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

**Figure 7.** Posterior means and 2.5 and 97.5 percentiles for probabilities of making Third-and-1 and Third-and-10 under Model 3. 

Third and 1 Third and 10 Third and 1 Third and 10 

16 

#### Cafarelli et al.: Third Down Conversions in the NFL 

**Figure 8.** Estimated logistic curves for each offense against an average defense.  Circles indicate the actual proportion of successful third-and- _x_ - yards-to-go, for _x_ = 1, 2, ..., 10. 



<!-- Start of picture text -->
49ers Bears Bengals Bills<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Broncos Browns Bucaneers Cardinals<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Chargers Chiefs Colts Cowboys<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Dolphins Eagles Falcons Giants<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Jaguars Jets Lions Packers<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Panthers Patriots Raiders Rams<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Ravens Redskins Saints Seahawks<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>Steelers Texans Titans Vikings<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>YTG YTG YTG YTG<br>17<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br>0            1 0            1 0            1 0            1<br><!-- End of picture text -->

_Submission to Journal of Quantitative Analysis in Sports_ 

the Jaguars have most points below the curve, suggesting that they tended to play above average defensive teams. The fit of the curves seems fairly good, with the possible exception of third-and-one. Twenty four of the 32 NFL teams had actual third-and-one conversion rates that were above the values predicted (when playing against an average defense). This suggests that third-and-short is slightly easier than the model predicts. It also may be accounted for by the fact that “third-and-inches”is recorded as third-and-one, whereas if more that one yard but less than two yards are needed, the play is recorded as third-and-two. There is a large proportional difference between third-and-inches being recorded as third-and-one, and third-and-just-over-one being recorded as third-and-two. 

Comparing different models with different numbers of parameters is inherently diffi cult, because we would expect models with more parameters to fit better than models with fewer parameters, and to make matters worse, it is often diffi cult to count parameters in a hierarchical model. The deviance information criterion (DIC) suggested by Spiegelhalter et al. (2002) attempts to account for the “effective number of parameters”in a model, as well as the fit of the model. The DIC is the Bayesian analogue to the Akaike information criterion. 



Smaller values of DIC indicate a better fitting model, adjusted for the number of parameters. The values of DIC, calculated in WinBUGS, are shown in Table 7. Model 1, where all teams are assumed to have the same logistic curve has the lowest DIC, mainly because of the small number of effective parameters (2.00). Model 3, with slope and intercept parameters for both the offensive and defensive teams, has the highest DIC. The results in Table 7 suggest that third-down conversion rates could be the same, or nearly so, across all NFL teams. This casts doubt on the effectiveness of using third-down conversion rates, even adjusted for yards to go, to measure the strength of an offense. 

18 

Cafarelli et al.: Third Down Conversions in the NFL 

Table 7: Deviance Information Criterion (DIC) for the three models 

|Model|Parameters|¯D|ˆD|pD|DIC|
|---|---|---|---|---|---|
|1|α, β|8638.89|8636.89|2.00|8640.88|
|2|αOi, βOi (ofensive team)|8607.72|8572.36|35.36|8643.07|
|3|αOi, βOi (ofensive team)<br>αDj,βDj (defensive team)|8584.80|8517.16|67.64|8652.45|



### 7. Summary and Conclusion 

We have proposed three models for estimating the probability of converting a third down play. The simplest model assumes that the probability of conversion depends on YTG, but not on the offensive or defensive team. The most complicated is one that depends on (1) the number of yards to go, (2) the strength of the offense, and (3) the strength of the defense. A hierarchical Bayes method is used to avoid the identifiability issue that arises when we look at the difference between the strength of the offense and the strength of the defense. Gibbs sampling is used, through the software package WinBUGS, to estimate the posterior distributions of the parameters. 

The raw third down conversion rate is a practically meaningless measure of offensive effi ciency since it is so heavily dependent on YTG. The conversion probability is estimated to be a decreasing function of yards to go, but the curves differ little across all 32 teams. In fact, the model with the lowest DIC is the model where the logistic curve is assumed to be the same for all teams. A further analysis of third down effi ciency might focus on field position as well as play selection. For example, teams may be less aggressive in trying for a first down when they are already in field goal range. Also, there are times, such as third-and-20, where a team will virtually give up on getting a first down by selecting a running play (which has little chance of making a first down) rather than a pass play (which carries a fair chance of making a first down but also carries risk, such as a sack or interception). 

### Appendix A: Convergence of MCMC 

We applied WinBUGS to Model 3 with data from the 2007 NFL season using four sets of initial values of the parameters and ran 3000 iterations of the Markov chain (which takes about thirty minutes on a PC running Windows). 

19 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

After these 3000 iterations, we checked the trace plots and the BGR plots (based on the work of Gelman and Rubin (1992) and Brooks and Gelman (1998)). The trace plots of the various parameters (for all four starting values) suggest thorough mixing within a hundred or so iterations. The BGR plots, which compare the values of the posterior draws from the various starting values, suggest thorough mixing for most parameters after a thousand or so iterations. For some parameters, the BGR plots do not stabilize until about 2500 iterations. To be rather confident of convergence, we take the burn-in period to be the first 10,000 iterations. We then ran through 110,000 iterations from each of four initial values for the parameters, discarding the first 10,000 from each stream. The results are then based on these 4 × 100, 000 = 400, 000 steps through the Markov chain. 

### Appendix B: Choice of Prior Distributions 

We have tried to choose prior distributions for Model 3 that are reasonable for the type of problem considered here. With the hierarchical Bayes method for Model 3, we allow the prior distributions of the model parameters (αO, αD, βO, βD) to depend on unknown parameters called hyperparameters. The choice of a prior for the hyperparameters has less influence than the choice of a prior for a model parameter. 

Consider first the parameters αOi, i = 1, 2, . . . , 32. We assume that the prior is N�µ1, τ<sup>−</sup> 1<sup>1</sup> � , where µ1 and τ 1 are the (unknown) hyperparameters. By contrast, the parameters αDj, j = 1, 2, . . . , 32 are centered at zero to avoid the identifiability problem. Consider an offense playing against an average defense, that is, a defense having αDj = 0. For a “third-and-ε”play, where ε is a number very close to zero, the probability of a successful conversion is 



A reasonable estimate of this probability, a priori, is about 2/3; for this estimate we have used data from Rigdon and Rigdon (2004) based on the 2003 NFL season. With π = 2/3, we find that 



We thus take 0.693 as the center for the distribution of µ1; note that we are not taking 0.693 as the center for the prior distribution of αOi (where the mean is µ1), but rather for the center of the prior for µ1. For the precision of the 

20 

Cafarelli et al.: Third Down Conversions in the NFL 

prior for µ1, we take the center to be 25, that is, with a standard deviation of 51<sup>= 0.2.Thisimpliesthattherangefrom</sup> 



should cover most of our prior beliefs for µ1. The prior for µ1 is therefore taken to be N�0.693, 25<sup><u>1</u></sup> � . 

Now consider the prior for τ 1. A team that converted 80% of third-and-ε would be considered excellent; for such a team 



On the other hand a team that made only 50% of third-and-ε would be considered poor, and for such a team we would have 



Thus we would expect the αO’s to be between 0 and 1.386 (centered at about 0.7), and if this is the center plus and minus 2 standard deviations, then a reasonable value for the standard deviation is 0.7/2 = 0.35. The precision should thus be about τ 1 = 1/0.35<sup>2</sup> ≈ 8. We therefore take the prior to be centered at 8 with a fairly large variance so as to make the prior somewhat noninformative. Since the precision must be a positive quantity, we choose the prior to be GAMMA(1, 0.125) ; in WinBUGS, the GAMMA(α, β) distribution is parameterized to have mean α/β and variance α/β<sup>2</sup> . 

The prior distribution for αD is N�0, τ<sup>−</sup> 2<sup>1</sup> � , where τ 2 is the only hyperparameter. We choose the same prior distribution for τ 2 as we did for τ 1, figuring that our prior knowledge about the αD’s will be about as spread out as our knowledge of the αO’s. 

Our prior for βO is taken to be N(µ2, τ 3) , so we now try to find reasonable priors for the hyperparameters µ2 and τ 3. The βO parameter is like a slope parameter, so we cannot elicit prior information about its prior solely from third-and-ε situations. Instead, let’s consider the third-and-10 situation. For average teams αO ≈ 0.693 and αD = βD = 0, so we would have 



21 

_Submission to Journal of Quantitative Analysis in Sports_ 

Solving for βO gives 



Consider a low, middle, and high value for the probability π of making a third-and-10. 



We take the prior mean for µ2 to be near the center −0.131. If the high and low values are two standard deviations above and below the mean, then the standard deviation would be about 0.03, making the precision about 1000. We take the prior for µ2 to be N�−0.131, 10001 � . 

Consider next, the prior for the hyperparameter τ 3. Since βO is a “slope” parameter, we consider low and high slopes: 

Low: 3rd-and-ε (π = 0.5) , 3rd-and-10 (π = 0.4) , leading to βO ≈−0.041 

High: 3rd-and-ε (π = 0.9) , 3rd-and-10 (π = 0.1) , leading to βO ≈−0.439. 

If these are two standard deviations below and above the center, then the standard deviation should be about 0.0995, making the precision approximately 100. Our prior for τ 3 is then taken to be GAMMA(1, 0.01) . The prior for τ 4 is the same. 

Finally, we can assess our choice of prior distributions by looking at what kinds of logistic curves we obtain by selecting from the various priors. Figure 9 shows the results of simulating 100 sets of parameters, beginning with the hyperparameters and finishing with the model parameters. We want to guard against choosing priors that are too tight, that is, have too little variation, which can cause the posteriors to be highly dependent on where we choose the priors. In Figure 9, we see a wide variety of logistic curves. Although some of these curves are totally unrealistic, it is hard to imagine that this set of prior distributions would exclude any reasonable logistic curve for third down conversion. This suggests that our priors are suffi ciently diffuse, and therefore 

22 

Cafarelli et al.: Third Down Conversions in the NFL 

reasonably noninformative. Therefore, the posteriors will be dominated by the data, not the prior. 

Figure 9: One hundred logistic curves whose parameters were selected at random using the prior and hyperprior distributions. 



### References 

- Albert, J. and Chib, S. (1997) “Bayesian Tests and Model Diagnostics in Conditionally Independent Hierarchical Models,” Journal of the American Statistical Association, 92, pp. 916—925. 

- Bock, R. D. (1997) “A Brief History of Item Response Theory,” Educational Measurement: Issues and Practice, 16, pp. 21—33. 

- Bock, R. D. and Aitken, M. (1981). “Marginal Maximum Likelihood Estimation of Item Parameters: Application of an EM Algorithm,”Psychometrika, 46, pp. 443—459. 

- Bradley, R. A. and Terry, M. E. (1952) “Rank Analysis of Incomplete Block Designs: I The Method of Paired Comparisons,” Biometrika, 39, pp. 324—345. 

- Brooks, S. P. and Gelman, A. (1998) “General Methods for Monitoring Convergence if Iterative Simulations,”Journal of Computational and Graphical Statistics, 7, pp. 434—455. 

- Carroll, B., Palmer, P., and Thorn, J. (1998) The Hidden Game of Football: The Next Edition, Warner Books: New York. 

- Gelman, A., and Rubin, D. (1992), “Inference from Iterative Simulation using Multiple Sequences,”Statistical Science, 7, pp. 457—511. 

23 

_Submission to Journal of Quantitative Analysis in Sports_ 

- Lunn, D. J., Thomas, A., Best, N., and Spiegelhalter, D. (2000) “WinBUGS —a Bayesian modelling framework: concepts, structure, and extensibility.” Statistics and Computing, 10, pp. 325—337, available at 

- http://www.mrc-bsu.cam.ac.uk/bugs/ . 

- Rigdon, C. J., and Rigdon, S. E. (2004) “Models for Third-down Effi ciency in the NFL”, Paper presented at the Joint Statistical Meetings, Toronto, ON, August 2004. 

- Rigdon, S. E. and Tsutakawa, R. K. (1983) “Parameter Estimation in Latent Trait Models,”Psychometrika, 48, pp. 567—574. 

- Spiegelhalter, D. J., Best, N. G., Carlin, B. P.; van der Linde, A. (2002). “Bayesian Measures of Model Complexity and Fit (With Discussion)” Journal of the Royal Statistical Society, Series B, 64 (4): pp. 583—639 

- Watterson, J. S. (2000) College Football: History, Spectacle, Controversy, Johns Hopkins University Press: Baltimore. 

24 


