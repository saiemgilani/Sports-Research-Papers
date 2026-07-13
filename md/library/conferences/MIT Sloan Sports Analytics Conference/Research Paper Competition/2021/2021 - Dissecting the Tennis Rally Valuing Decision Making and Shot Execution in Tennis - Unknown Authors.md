<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2021/2021 - Dissecting the Tennis Rally Valuing Decision Making and Shot Execution in Tennis - Unknown Authors.pdf -->



# **Dissecting the Tennis Rally: Valuing Decision Making and Shot Execution in Tennis** 

Robert Seidl<sup>1</sup> , Machar Reid<sup>1</sup> , Sam Robertson<sup>2</sup> 1Tennis Australia, 2Victoria University rob@talksportsdata.com 

## **1. Introduction** 

In the 2020 Australian Open final, Dominic Thiem faced defending champion Novak Djokovic to try to win his first Grand Slam title. After leading 2 sets to 1, he lost a very close five set match 4:6, 6:4, 6:2, 3:6, 4:6 after almost four hours. Tennis is a game of very thin margins where a player can win the same total number of points as his opponent but still lose the match. In this way, the scoreboard can be misleading or mask important details of points and matches that require further analysis to explain the victory. Indeed, with the advent of player and ball tracking data in professional tennis, there has been an emergence of data-driven analyses of shots [4-6]; all of which attempt to explain different shot level nuance of the game. However, multiple decisions precede every shot that is hit in professional tennis matches and the use of tracking data to decouple and inferentially examine the quality of decision-making by players remains overlooked. 

With this in mind, the paper takes a first step to objectively quantify the decision making and shot execution of a tennis player based on player and ball tracking data in the following way: 

- We train four neural network models to disentangle decision-making and execution for each shot hit at Australian Open 2020, where the aim is either to predict whether the player will win the point immediately (i.e., with that shot) or later within the rally (i.e., after subsequent shots). 

- We consider player performance on serve, return and in-rally play separately. 

- We measure the relative importance of a rally within a match using an in-match win probability model to understand the interaction between decision-making, execution and scoreboard pressure. 

Once established, these models are applied to analyze Thiem’s performance at Australian Open 2020 on the following four levels: 

- _on tournament level_ , we compare Thiem’s playing style to those of the other three semifinalists, and investigate his shot execution performance in the rounds leading up to the final, 

- _on match level_ , we inspect how his play evolved in the final against Djokovic, with a specific focus on high pressure moments, 



1 



- _on rally level_ , we judge the quality of his shot execution in an important rally decoupled from the actual outcome. 

## **2. Valuing decision making and execution in tennis rallies** 

Given the increased availability of event and tracking data in sports, researchers have tried to value action outcomes in football [1, 2], basketball [3] and tennis [4, 5, 6]. In tennis the goal is to predict if a shot will end the rally and win the point outright. There is a problem with this approach as most tennis players do not hit every shot with the intention of it being a winner but rather to gain small advantages throughout a rally which add up in the battle for time and space – thus oversimplifing a player’s shot selection process and undervalueing strategic play. The best-known player following this approach is Novak Djokovic, currently ranked No.1 in the world. 

A better choice for a target variable is to analyze whether a player will be able to win the rally at some point after the current shot. This is the delayed reward for playing strategically smart shots that players are aiming for. 



**Figure 1.** Sample tracking data and model evaluation. a) Visualization of Hawkeye player and ball tracking data at the moment when Thiem hits a forehand return. Positions and velocities vectors are shown in green, red and yellow for Thiem, Djokovic and the ball. b) The input features for the neural network and its predicted win probability for the rally. 

_Decroos et al._ [2] introduced the concept for separately valuing _decision_ and _execution_ in soccer. We transfer this idea to tennis as we disentangle decision making from execution by considering the moment of the shot (“when the ball leaves the racket”) to value the decision of a player to play a certain shot in the current situation as this is the last time where a player can actively change his 



2 



shot selection by varying direction, speed, spin or the target location. Furthermore, we consider the consecutive moment of the ball bounce in the opponent’s court as the execution of the shot as this will tell us about the direct outcome of the shot allowing for a shot by shot evaluation within a rally. 

Using Hawkeye ball and player tracking data from 2020 Australian Open we train four Neural Networks on 107,000 hits and 98,000 bounces<sup>1</sup> to learn the likelihood of a hit or bounce resulting in a direct winner and winning the rally, respectively. This allows the model to learn strategies of winning the point outright as well as strategies which aim on building up a point. To help distinguish between the different models, we abbreviate their outputs as xDW, xDR, xEW and xER for the expected decision and execution values for hitting a direct winner and winning the rally. 

As input features to the models we use position, speed and angle of both players and the ball at the time of the hit and bounce, respectively. We also add classifications that label a shot as a serve, return or rally shot. This way the model can treat the special cases of a serve and return, which happen at the beginning of each rally, differently than shots occurring later in a rally. Figure 1a shows a visualization of Hawkeye data for a forehand return Thiem played in the Australian Open final against Djokovic. The positions and velocities of each player and the ball are shown in green, red and yellow. Figure 1a presents a sample situation where Thiem plays a backhand return. The input features for the neural network and the estimated win probability of the rally predicted by the neural network at the time Thiem hits the ball are shown in Figure 1b. 

### **2.3. Model evaluation** 

Training the four different models, we achieve the results shown in Table 1. 

|**MODEL**|**DESCRIPTION**|**TARGET**|**AUC**|**ACCURACY**|
|---|---|---|---|---|
|xDW|Decision (Hit)|Direct winner|73 %|81 %|
|xDR|Decision (Hit)|Win rally|65 %|59 %|
|xEW|Execution (Bounce)|Direct winner|78 %|84 %|
|xER|Execution (Bounce)|Win rally|71 %|63 %|



#### **Table 1.** Model evaluation 

Decision accuracy is lower than execution accuracy as it is tougher to predict the immediate or rally winner at the time of hitting the ball compared to the time the ball bounces. Furthermore, predicting the winner of a rally given only a snapshot of a shot (either hit or bounce) is a very tough task where you cannot expect to achieve a very high accuracy. However, the models do a fairly good job with accuracies of 59% and 63%. 

## **3. Estimating in-match win probabilities** 

Having a model that predicts the likelihood of winning a point in tennis is valuable on its own but not all points in tennis are equally important [10]. To be able to capture this relative importance of a rally within a match we need to combine our model with a live win probability model. 

> 1 This refers to the training set, we use a test set of 12,000 hits and 11,000 bounces played in the tournament. 



3 



There exists a vast literature on match forecasting in tennis and we refer to [7] and the references within for a detailed description of our live win probability model. We just give a high-level overview of the method. The idea is to use pre-match information and relevant in-match information to predict the likelihood of a player winning the match at the current score. We employ the following four step process. 



**Figure 2.** In-match win prediction for Australian Open final for Djokovic vs. Thiem. The dashed horizontal line indicates the pre-match win probability. Vertical lines indicate the end of each set. 

1) **Pre-match prediction** . Calculate ELO ratings for each player and adjust them for court surface and previous matches played against the opponent. This yields the pre-match win probability for the players. 

2) **Calibration of pre-match prediction** . Convert the pre-match prediction into serve and return predictions that result in the same prediction at the first point of the match. 

3) **Bayesian in-match update** . Given the current score update the baseline serve predictions with the observed in-match serve probabilities that are based on the observed serve points won and played in the match. 

4) **In-match prediction** . Calculate the in-match win probability running a Barnett-Clarke model [8] using the updated in-match serve predictions. 

As an illustration Figure 2 depicts the in-match win probability for the Australian Open final Djokovic against Thiem which ended 6:4, 4:6, 2:6, 6:3, 6:4. The development of the win probability of Djokovic throughout the match is shown. The dashed horizontal line indicates the pre-match win probability derived from the ELO ratings of both players. Vertical lines indicate the end of each of the five sets. 

Given the in-match win probability model, we define _leverage_ as how much a point could influence the match outcome. This way we can identify high pressure situations in a match. 

## **4. Applications** 



4 



Being able to value each players decision and its execution for every shot within a tennis rally has multiple applications for performance analysis, media and sports betting. In this section we present 



**Figure 3.** Decision and Execution values for semi-finalists of 2020 Australian Open for ATP Tour 

different use-cases with the aim to objectively quantify Thiem’s performance at last year’s Australian Open in a data-driven way. 

First, we employ decision and contribution values to investigate the different playing styles of all four semifinalists. Second, we examine Thiem’s performance in the matches he won to reach the final. Third, we look into the close five set final he lost against Djokovic where we especially investigate what happened to Thiem’s game in the fifth set and how he performed on points where the pressure was high. Fourth, we dissect each shot of a point played in the fifth set which we found to have significant impact on the outcome of the match but the expected outcome differed significantly. 

### **4.1 Playing Styles of Mens Semi-Finalists**<sup>**2**</sup> 

As first application to show the value of both, decision and execution values for analyzing playing styles, we aggregate the values of each hit and bounce for all semifinalists of this year’s Australian Open. Figure 3 shows a summary of decision and execution values for shot and rally models for serve, return and rally. As discussed in Section 2, the shot decision model predicts the likelihood of winning the point immediately at the time when the ball leaves the racket and the rally decision model predicts the likelihood of winning the rally. The execution models predict the same quantities at the time of the bounce. Average player values are also shown. 

Looking at the serve models, we recognize that all four players serve over average with Zverev clearly leading in execution values on shot and rally level, meaning that he is most likely to win a point outright (shot model) but also later in the rally (rally model). 

2 We followed the same modelling process and applied it to WTA Tour matches. The decision and execution values for the women semi-finalists are shown in Appendix A1. 



5 



If we inspect the return models, the return play of Federer, Thiem and Zverev does not stand out but Djokovic’s return play is superb, both on winning a point outright and setting up on winning the rally. Especially the rally execution is more than 5 points over average. 

Focusing on the rally models, we see that Zverev does not stand out in terms of rally execution. He builds his advantage through his serve. Federer, Djokovic and Thiem achieve high rally execution values. Both Federer and Thiem also have a high shot execution which indicates that they try to win rallies immediately. Instead, Djokovic shot execution is lower than average which shows that he does not try to win points directly but try to outplay his opponents in longer rallies where he is building up the point slowly. 

### **4.2 Thiem’s march to Australian Open 2020 final** 

We saw how decision and execution values can give us insights into a players’ playing style. Focusing on execution values for the remainder of the paper, we are also able to investigate Thiem’s performance over previous matches. 





**Figure 4.** Shot execution values of Thiem on his way to the final. Vertical lines highlight 95% confidence intervals. Dashed lines indicate tournament averages. 

Figure 4 displays Thiem’s average execution values over the rounds to the final. It’s evident that he served well throughout the tournament, with exception of the quarterfinal. His return execution approximated the average for the field but he was clearly superior in rally play, especially on the forehand. It follows that his dominance with this wing might be a deciding factor in the final against Djokovic. 

### **4.3 How Thiem’s forehand cost him the title** 



6 



The final went down to the wire, with Djokovic edging out the Austrian 6:4 in the fifth. In applying our models in the same way as above but this time to Thiem’s execution in each set of the final, we examine what went wrong. 

Figure 5 summarizes the execution values for serve, return and forehand and backhand rally balls for each player for each set of the final. The dashed lines represent the average execution values of Thiem and Djokovic in the lead up to the final. 





**Figure 5.** Australian Open Final – Shot and rally execution values 

We turn our attention to set 5, where we observe some interesting shifts: 

- 1) Djokovic’s serve execution improved, 

- 2) Thiem’s return execution dropped, logically related to the improvement on Djokovic’s serve 3) The quality of Thiem’s ball striking in rally play fell away, with a sharp drop in forehand execution. This is stark, especially against the backdrop in Thiem having the best forehand execution values of all semifinalists. 

Interestingly, by applying the concept of leverage to quantify low (less than 5%) and high (more than 5%) scoreboard pressure situations (as it has been done in football, [9]), we are able to better understand where Thiem came unstuck (Figure 6).  In high pressure situations in the first four sets, Thiem’s backhand execution values were close to his tournament average while he outperformed on his forehand. The story couldn’t have been more different in the fifth set though, where his rally game unraveled, particularly on his favored forehand wing. If we look at Thiem’s decision values we observe that they stayed on the same level for his backhand and only dropped moderately compared to the drop in his forehand execution. While Djokovic clearly upped his own game, Thiem’s ball striking and dominant forehand execution succumbed to the pressure. 



7 







**Figure 6.** Rally execution and decision values for Thiem on high pressure points. The distribution for execution and decision values of all players is shown for forehand and backhand. Thiem’s average value before the final is highlighted as gray circle. The average he played in the final in sets 1 – 4 as green circle and his execution values in the final set as red circles. 

### **4.4. Dissecting the tennis rally** 

To this point, we have aggregated decision and execution values at the set, match and tournament level. However, these models also give rise to the opportunity to integrate the match win prediction model and identify situations where the outcome of a point and the shot execution values seem incongruent. We use the scoreline 4:6, 6:4, 6:2, 3:6, 1:2, Advantage Thiem to do this very thing. Here, the leverage is 21.15%. Thiem is down a break but manages to create an opportunity to break back on Djokovic’s serve. If he breaks serve, scores are level and he is “back in the match”. We can use our execution values to determine the actual in-rally win probability after each shot. 



8 



Furthermore, we can determine the expected match win probability by weighting the last observed in-rally win probability with the resulting match win probabilities for a positive and negative outcome of the point. This allows to get a more accurate evaluation of what is happening on the court. 



**Figure 7.** Evolution of Thiem’s rally win percentage after shot execution during a critical point in the fifth set. 

Figure 7 depicts Thiem’s winning probability during the rally in question (video of the rally can be seen here: <u>https://youtu.be/A9NA8gCCI2M , 1). Before the point, Thiem has a pre-rally match win</u> percentage of 19.27%. (2), which then updates in the plot at the time of the ball bounce for each shot. Green diamonds correspond to Djokovic’s shots and blue circles to Thiem’s shots. On the images below, the positions and movement directions of players and ball are highlighted for Djokovic (green), Thiem (red) and the ball (yellow). These were used as features in the modelling process. The point unfolds as follows ... 

(2.1) Djokovic hits a well-executed serve wide to the Thiem backhand, giving Thiem a 16% chance of winning the rally. 

(2.2) Thiem hits a backhand slice to the center of the court, which Djokovic volleys deep back to Thiem’s backhand corner. 

(2.3) Thiem moves backwards to return the Djokovic volley which is not played with much pace. This provides Thiem with options and his rally win percentage increases to 44.9%. 

(2.4) Thiem attempts a passing shot down-the-line but hits it wide. 

(3) The outcome does not reflect what happened in the rally. Thiem loses the point but before taking the shot he should expect to win it 44.9% of the time. His post-rally win probability of the match drops to 12.5% (- 6.77%) but incorporating his in-rally win percentage, his expected match 



9 



win percentage actually increased to 22.0% (+ 2.73%). This shows that Thiem played this important point well but this is not visible on the scoreboard. 

## **5. Conclusions** 

We introduced several models to evaluate a tennis players decision making and shot execution with a focus on either shot or rally level. This allowed us to investigate the performance of players on serve, return and in longer rallies. Various use-cases around Thiem’s performance at last Australian Open showed how the models can be used to interpret playing style and judge the performance of a player over a tournament, in-match on a set level, or even on rally level. 

Combining the shot execution model xER with an in-match win probability model allowed us to calculate the expected in-match win probability based on what actually happened in a rally. Furthermore, our in-match win predictor and the concept of leverage allowed us to investigate how Thiem played high-pressure points in the final. 

Even though we focused on presenting several use-cases related to measuring and interpreting Thiem’s performance at last Australian Open and especially in the final, the evaluation approach is not limited to only one player. Based on available player and ball tracking data, it allows to evaluate the performance of tennis players in an objective, automated and fully data-driven way. A possible next step is to investigate the performance of various players in high-pressure situations across serve, return and in-rally play. 

## **References** 

[1] Fernandez, J., Bornn, L., & Dan Cervone (2020). Decomposing the Immeasurable Sport: A deep learning expected possession value framework for soccer. _MIT Sloan Sports Analytics Conference_ . 

[2] Decroos, T., Van Haaren, J., Bransen, L., & Davis, J. (2019). Actions speak louder than goals: Valuing player actions in soccer. In _Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ (pp. 1851–1861). New York, NY, USA: Association for Computing Machinery. 

[3] Cervone, D., D’amour, A., Bornn, L., & Goldsberry, K. (2014). POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data. _MIT Sloan Sports Analytics Conference_ . 

[4] Wei, X., Lucey, P., Morgan, S., Reid, M., & Sridharan, S. (2016). "The Thin Edge of the Wedge": Accurately Predicting Shot Outcomes in Tennis using Style and Context Priors. _MIT Sloan Sports Analytics Conference_ . 

[5] Kovalchik, S, Ingram, M., Weeratunga, K., Goncu, C. (2020). Space-Time VON CRAMM: Evaluating Decision-Making in Tennis with Variational generation of Complete Resolution Arcs via Mixture Modeling, _arXiv preprint arXiv:2005.12853_ 



10 



<mark>[6] Floyd, C. M., Hoffman, M., & Fokoue, E. (2020). Shot-by-shot stochastic modeling of individual tennis points,</mark> _<mark>Journal of Quantitative Analysis in Sports</mark>_ <mark>,</mark> _<mark>16</mark>_ <mark>(1), 57-71</mark> 

[7] Kovalchik, S. & Reid, M. (2019). A calibration method with dynamic updates for within-match forecasting of wins in tennis. _International Journal of Forecasting, 35_ (2), 756–766 

[8] Barnett, T., & Clarke, S.R. (2005). Combining player statistics to predict outcomes of tennis matches. _IMA Journal of Management Mathematics_ , 16(2), 113-120 

[9] Bransen, L., Robberechts, P., Van Haaren, J., Davis, J. (2019). Choke or Shine? Quantifying soccer players’ abilities to perform under mental pressure. _MIT Sloan Sports Analytics Conference_ . 

[10] Morris, C. (1977). The Most Important Points in Tennis. _Optimal Strategies in Sports_ , 5, 131– 140 



11 



## **Appendix** 



**A 1.** Decision and execution values for semi-finalists of 2020 Australian Open for WTA Tour 



12 


