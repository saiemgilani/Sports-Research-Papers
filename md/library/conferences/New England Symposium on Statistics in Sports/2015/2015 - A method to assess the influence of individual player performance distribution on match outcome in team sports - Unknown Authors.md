<!-- source: library/conferences/New England Symposium on Statistics in Sports/2015/2015 - A method to assess the influence of individual player performance distribution on match outcome in team sports - Unknown Authors.pdf -->





**A method to assess the influence of individual player performance distribution on match outcome in team sports** 

**Sam Robertson, PhD** Ritu Gupta, PhD Sam McIntosh Sam.robertson@vu.edu.au @Robertson_SJ 

26<sup>th</sup> September, 2015 

## **PROJECT ORIGINS** 

- Can star players be relied upon by teams to win matches, or is a spread of contributors preferable in order to achieve success? 

- How can our answers to this question be used to inform player scouting, selection, development and contracting in elite team sports? 

- Can we quantify player contributions to the team in a way whereby they are able to be compared longitudinally 



- Between matches and seasons; within  player and team 



## **AUSTRALIAN RULES FOOTBALL** 



<!-- Start of picture text -->
Introductory video to AFL<br><!-- End of picture text -->



|**Performance Indicator**|**Definition**|
|---|---|
|**Kick**|Disposing of the football with any part of the leg below the knee.|
|**Mark**|Catching or taking control of the football after it has been kicked by another player a distance of at least 15 metres<br>without touching the ground or being touched by another player.|
|**Handball**|Disposing of the football by hitting it with the clenched fist of one hand, while holding it with the other.|
|**Disposals**|Total count of kicks and handballs.|
|**Goals**|The maximum possible score (6 points) achieved by kicking the ball between the two goal-posts without touching a post<br>or any player|
|**Behind**|A score worth one point, achieved by the ball crossing between a goal post and a behind post, or by the ball hitting a<br>goal post, or by the ball being touched prior to passing between the goalposts|
|**Tackle**|Taking hold of an opposition player in possession of the ball, in order to impede his progress or to force quick disposal<br>of the ball|
|**Inside 50**|The act of running or passing the ball into the 50 m arc at the opposition's defensive end of the field.|
|**Rebound 50**|The act of running or passing the ball outside of the 50 m arc at the opposition’s offensive end of the field.|
|**Clearance**|Clearing of the ball out of a stoppage (congested) situation to the advantage of one’s team|
|**Contested possession**|A possession achieved as a result of winning a contest.|
|**Uncontested possession**|A possession achieved without having to engage in a contest.|
|**Mark inside 50**|The act of a player from the attacking team marking the ball inside the 50 m arc at their offensive end of the field|



## **BACKGROUND:** Performance indicators 







_Robertson, S. J., Back., N., & Bartlett (2015).Explaining match outcome in elite Australian Rules football using performance indicators. Journal of Sports Sciences_ 



## **BACKGROUND:** Importance of team? 







<!-- Start of picture text -->
Accuracy = 85.67%<br>•<br>Win accuracy = 88.96%<br>•<br>Loss accuracy = 82.30%<br><!-- End of picture text -->

|**Accuracy = 85.67%**|
|---|
|• Win accuracy = 88.96%|
|• Loss accuracy = 82.30%|
|**Considered additional**<br>**influence of:**|
|• Team|
|• Margin|
|• Quarter|
|• **↑**PI’s|
|Potential for use in-game?|





<!-- Start of picture text -->
Considered additional<br>influence of:<br>• Team<br>•<br>Margin<br>•<br>Quarter<br>• ↑  PI’s<br><!-- End of picture text -->



<!-- Start of picture text -->
Potential for use in-game?<br><!-- End of picture text -->



## **Directions…** 

**Question Method** What? ‘Traditional’ PA Where? Spatio-temporal When? Spatio-temporal How? Coaching Why? Coaching **Who? ?** 



## **PROJECT AIMS** 

- To propose a method of describing the distribution of player performances in 

- team sports 

- To determine whether these distributions can be modelled to explain match outcome, using Australian Rules football as an example 

- To provide an applied example of how the results can be used in player coaching, development and scouting 

   - Roster structure 





## **METHODOLOGY:** Data collection 

- 2014 AFL season data (198 games) 

- Player and Team values for 13 x performance indicators obtained 

- All 22 players contributions converted to a percentage of team total 

   - Allows for direct comparison to be made across 

matches 

- Allows for team distributions to be obtained 



_(Stewart et al., 2007; Robertson, Back & Bartlett, 2015; Tangalos, Robertson, Spittle & Gastin, 2015;_ 

|**Performance**<br>**Indicator**|**Total**<br>**observations**|
|---|---|
|Kicks|81,364|
|Handballs|62,393|
|Marks|34,895|
|Disposals|143,757|
|Goals|4,962|
|Behinds|3,522|
|Tackles|26,353|
|Rebound 50’s|14,640|
|Inside 50’s|19,886|
|Clearances|15,077|
|Contested poss.|54,401|
|Uncontested poss.|88,215|
|Marks inside 50|3,771|





## **METHODOLOGY:** Feature extraction 

16 9.0% 14 8.0% 12 7.0% **7.85%** 6.0% 10 5.0% 8 4.0% 6 3.0% **191 kicks** 4 2.0% 2 1.0% **1.05%** 0 0.0% 



<!-- Start of picture text -->
7.85%<br><!-- End of picture text -->





## **METHODOLOGY:** Feature extraction 



<!-- Start of picture text -->
Identifiers<br>Team  N  = 18<br>Player  N  = 22<br>Match result<br>Outcome  Win/Loss<br>Margin  ± Points<br><!-- End of picture text -->





<!-- Start of picture text -->
Performance<br>indicators<br>Kicks<br>Handballs<br>Marks<br>Disposals<br>Goals<br>Behinds<br>Tackles<br>Rebound 50’s<br>Inside 50’s<br>Clearances<br>Contested poss.<br>Uncontested poss.<br>Marks inside 50<br><!-- End of picture text -->



<!-- Start of picture text -->
Team features<br>Maximum<br>Minimum<br>Standard deviation<br>Mean<br>P5<br>P10<br>P25<br>P50<br>P75<br>P90<br>P95<br><!-- End of picture text -->



<!-- Start of picture text -->
Match feature<br>set<br>PI’s  13<br>Features  11<br>Team  2<br>Total  286<br><!-- End of picture text -->



## **METHODOLOGY:** Feature extraction 



**Max** 

**Mean SD** 

**Min** 





- Process repeated for remaining 12 performance indicators 

- • Match outcome [i.e., ‘Win’, +8 points] 



## **STATISTICAL ANALYSIS** 

- Model to explain match outcome (Win/Loss) as a function of the feature set for the performance indicators 

- Generalized estimating equations [GEE] (Geepack in _R_ ) 

   - Adjusting for the dependence of the 18 teams. 

   - Exchangeable correlation structure 

- Median match outcome classification accuracy obtained 

   - 10-fold cross-validation using random 33% of data 

- Decision tree (‘J48’ in R-Weka) 





## **RESULTS:** GEE models 

### • 8 features meaningfully contribute to explaining outcome in 2014 AFL season 



|**Feature**|**β**|**S.E**|**χ2**|**_P_**|
|---|---|---|---|---|
|Intercept|0.25|1.71|0.02|_0.88_|
|**Disposal.P25**|101.51|35.47|8.19|_<0.001_|
|**Disposals.P50**|77.85|33.90|5.27|_0.02_|
|**Marks.P25**|38.89|17.95|4.69|_0.03_|
|**Goals.P75**|-21.70|3.82|32.27|_<0.001_|
|**Goals.P95**|-7.53|2.18|11.91|_<0.001_|
|**Goals.P90**|-9.91|3.08|10.36|_<0.001_|
|**Behinds.P90**|-6.33|2.00|10.04|_<0.001_|
|**Inside50’s.P95**|-10.61|4.17|6.47|_0.01_|





<!-- Start of picture text -->
Intercept  0.25  1.71  0.02  0.88<br>Disposal.P25  101.51  35.47  8.19  <0.001<br>Disposals.P50  77.85  33.90  5.27  0.02<br>Marks.P25  38.89  17.95  4.69  0.03<br><!-- End of picture text -->



<!-- Start of picture text -->
Goals.P75  -21.70  3.82  32.27  <0.001<br>Goals.P95  -7.53  2.18  11.91  <0.001<br>Goals.P90  -9.91  3.08  10.36  <0.001<br>Behinds.P90  -6.33  2.00  10.04  <0.001<br>Inside50’s.P95  -10.61  4.17  6.47  0.01<br><!-- End of picture text -->

- Not only magnitude of differences that are important! 

- • Potential to combine with pre-existing models? 





## **RESULTS:** Goals 





## **RESULTS:** Goals P.75 by AFL team 







## **What about margin?** 



<!-- Start of picture text -->
?<br><!-- End of picture text -->





## **RESULTS:** J48 decision tree 



<!-- Start of picture text -->
83.5% accuracy<br>86.3% for Loss<br>80.7% for Win<br><!-- End of picture text -->

83.5% accuracy 86.3% for Loss 80.7% for Win 



Ross Quinlan (1993). C4.5: Programs for Machine Learning. Morgan Kaufmann Publishers, San Mateo, CA. 

## **APPLICATIONS:** Positional line contributions 

### **Defenders** 

|**DEFENDERS**|**Games**<br>**Played**|**Kicks**|**Marks**|**Handballs**|**Disposals**|**Goals**|**Behinds**|**Tackles**|**Rebound 50s**|**Inside 50s**|**Clearances**|**Contested**<br>**Possessions**|**Uncontested**<br>**Possessions**<br>|**Marks Inside**<br>**50**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Austin, Mark|11|2.7%|4.1%|2.3%|2.5%|0.0%|0.0%|1.9%|3.7%|1.2%|1.0%|2.5%|2.5%|0.0%|
|Darley, Sam|5|4.1%|3.4%|3.5%|3.8%|1.1%|0.0%|3.4%|12.0%|0.8%|1.1%|2.5%|4.5%|0.0%|
|Goodes, Brett|2|4.0%|4.0%|1.5%|2.8%|0.0%|0.0%|2.2%|4.4%|1.2%|1.2%|1.2%|3.2%|0.0%|
|Higgins, Shaun|20|5.6%|4.9%|5.7%|5.6%|4.0%|2.5%|4.4%|9.0%|5.2%|1.7%|3.5%|6.7%|1.3%|
|Howard, Christian|2|2.1%|0.7%|1.8%|1.9%|0.0%|0.0%|3.2%|0.0%|4.3%|2.1%|1.3%|2.3%|0.0%|
|Johannisen, Jason|11|5.2%|5.1%|3.7%|4.5%|1.7%|5.5%|3.9%|6.6%|4.5%|1.4%|3.2%|5.3%|1.3%|
|Morris, Dale|20|3.1%|5.7%|3.2%|3.2%|0.0%|0.0%|3.4%|5.9%|1.1%|0.8%|3.0%|3.3%|0.0%|
|Murphy, Robert|22|7.0%|5.5%|4.3%|5.7%|1.5%|2.2%|2.5%|12.7%|5.0%|1.1%|3.5%|6.4%|1.9%|
|Picken, Liam|22|5.1%|5.2%|4.9%|5.0%|0.9%|3.0%|5.8%|8.4%|3.9%|2.3%|4.0%|5.5%|1.7%|
|Roberts, Fletcher|5|2.0%|2.9%|2.0%|2.0%|0.0%|1.8%|2.7%|0.0%|1.4%|0.9%|2.2%|1.6%|2.5%|
|Roughead, Jordan|15|3.2%|6.3%|3.0%|3.1%|0.0%|0.6%|3.1%|8.5%|1.3%|1.2%|2.7%|3.5%|0.0%|
|Talia, Michael|3|3.2%|4.5%|3.3%|3.3%|0.0%|0.0%|0.5%|4.8%|1.3%|0.9%|3.8%|3.0%|0.0%|
|Wood, Easton|18|3.8%|4.8%|4.6%|4.2%|0.4%|1.7%|3.5%|6.0%|4.7%|1.7%|4.1%|4.3%|0.0%|
|Young, Tom|4|2.7%|3.7%|3.6%|3.1%|1.5%|0.0%|1.7%|6.5%|1.9%|1.0%|2.9%|3.5%|0.0%|
|**Defenders Average**|**11.4**|**4.4%**|**5.0%**|**4.0%**|**4.2%**|**1.1%**|**1.7%**|**3.5%**|**7.6%**|**3.3%**|**1.4%**|**3.3%**|**4.6%**|**0.8%**|
|**Team Average**|**11.9**|**4.6%**|**4.6%**|**4.6%**|**4.6%**|**4.7%**|**4.6%**|**4.5%**|**4.6%**|**4.6%**|**4.3%**|**4.5%**|**4.7%**|**4.6%**|





<!-- Start of picture text -->
0.0%<br>1.1%<br>0.0%<br>4.0%<br>0.0%<br>1.7%<br>0.0%<br>1.5%<br>0.9%<br>0.0%<br>0.0%<br>0.0%<br>0.4%<br>1.5%<br>1.1%<br>4.7%<br><!-- End of picture text -->



<!-- Start of picture text -->
3.7%<br>12.0%<br>4.4%<br>9.0%<br>0.0%<br>6.6%<br>5.9%<br>12.7%<br>8.4%<br>0.0%<br>8.5%<br>4.8%<br>6.0%<br>6.5%<br>7.6%<br>4.6%<br><!-- End of picture text -->



## **APPLICATIONS:** Positional line contributions 

### **Forwards** 

||**Games**<br>**Played**|**Kicks**|**Marks**|**Handballs**|**Disposals**|**Goals**|**Behinds**|**Tackles**|**Rebound 50s**|**Inside 50s**|**Clearances**|**Contested**<br>**Possessions**|**Uncontested**<br>**Possessions**<br>|**Marks Inside**<br>**50**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**FORWARDS**|||||||||||||||
|Campbell, Tom|7|1.6%|2.3%|2.0%|1.8%|6.7%|3.2%|4.6%|0.0%|2.2%|3.3%|3.4%|0.8%|6.2%|
|Cordy, Ayce|1|1.9%|0.9%|3.4%|2.6%|0.0%|0.0%|5.0%|0.0%|0.0%|6.3%|4.5%|1.6%|0.0%|
|Crameri, Stewart|22|4.0%|5.6%|3.6%|3.8%|13.9%|8.5%|3.6%|0.3%|5.3%|0.8%|3.9%|4.0%|15.1%|
|Dahlhaus, Luke|21|6.0%|5.0%|6.0%|6.0%|8.2%|12.5%|5.9%|3.6%|5.5%|4.9%|6.8%|5.4%|8.9%|
|Dickson, Tory|4|2.3%|2.7%|2.8%|2.6%|6.3%|2.5%|3.8%|0.0%|3.3%|1.3%|2.4%|2.6%|7.1%|
|Giansiracusa, Daniel|15|3.5%|3.6%|2.4%|2.9%|8.1%|6.6%|1.7%|2.3%|3.9%|1.4%|1.9%|3.5%|8.0%|
|Grant, Jarrad|4|3.3%|5.7%|3.3%|3.3%|3.5%|0.0%|3.3%|0.0%|3.7%|2.5%|2.5%|4.2%|6.3%|
|Honeychurch, Mitch|3|1.5%|3.1%|3.4%|2.3%|2.4%|6.7%|4.0%|0.0%|2.6%|2.2%|1.9%|2.9%|0.0%|
|Hrovat, Nathan|12|4.4%|4.9%|5.2%|4.8%|6.3%|5.5%|4.4%|2.1%|4.2%|4.3%|5.1%|4.8%|6.1%|
|Hunter, Lachie|14|4.7%|5.5%|3.2%|4.0%|5.6%|12.6%|3.7%|2.0%|6.0%|3.7%|3.9%|4.0%|9.1%|
|Jones, Liam|10|3.1%|5.2%|2.5%|2.8%|8.6%|4.6%|2.6%|0.3%|3.7%|1.8%|4.0%|2.3%|14.8%|
|Redpath, Jack|3|1.5%|2.7%|2.3%|1.8%|4.9%|0.0%|2.2%|0.0%|1.4%|1.4%|1.6%|2.0%|11.4%|
|Stringer, Jake|18|3.8%|4.2%|2.9%|3.4%|11.4%|11.3%|3.4%|3.5%|3.8%|1.4%|4.4%|3.0%|14.5%|
|Williams, Tom|7|3.6%|5.0%|2.3%|2.9%|7.4%|1.3%|1.3%|2.5%|2.5%|0.6%|2.7%|2.9%|2.7%|
|**Forwards Average**|**10.1**|**3.9%**|**4.6%**|**3.5%**|**3.7%**|**8.6%**|**7.8%**|**3.6%**|**1.8%**|**4.3%**|**2.5%**|**4.0%**|**3.6%**|**9.9%**|
|**Team Average**|**11.9**|**4.6%**|**4.6%**|**4.6%**|**4.6%**|**4.7%**|**4.6%**|**4.5%**|**4.6%**|**4.6%**|**4.3%**|**4.5%**|**4.7%**|**4.6%**|





<!-- Start of picture text -->
0.0%<br>0.0%<br>0.3%<br>3.6%<br>0.0%<br>2.3%<br>0.0%<br>0.0%<br>2.1%<br>2.0%<br>0.3%<br>0.0%<br>3.5%<br>2.5%<br>1.8%<br>4.6%<br><!-- End of picture text -->



<!-- Start of picture text -->
3.3%<br>6.3%<br>0.8%<br>4.9%<br>1.3%<br>1.4%<br>2.5%<br>2.2%<br>4.3%<br>3.7%<br>1.8%<br>1.4%<br>1.4%<br>0.6%<br>2.5%<br>4.3%<br><!-- End of picture text -->



<!-- Start of picture text -->
6.2%<br>0.0%<br>15.1%<br>8.9%<br>7.1%<br>8.0%<br>6.3%<br>0.0%<br>6.1%<br>9.1%<br>14.8%<br>11.4%<br>14.5%<br>2.7%<br>9.9%<br>4.6%<br><!-- End of picture text -->



<!-- Start of picture text -->
6.7%<br>0.0%<br>13.9%<br>8.2%<br>6.3%<br>8.1%<br>3.5%<br>2.4%<br>6.3%<br>5.6%<br>8.6%<br>4.9%<br>11.4%<br>7.4%<br>8.6%<br>4.7%<br><!-- End of picture text -->



## **APPLICATIONS:** Positional line contributions 

### **Midfielders** 

|**MIDFIELDERS**|**Games**<br>**Played**|**Kicks**|**Marks**|**Handballs**|**Disposals**|**Goals**|**Behinds**|**Tackles**|**Rebound 50s**|**Inside 50s**|**Clearances**|**Contested**<br>**Possessions**|**Uncontested**<br>**Possessions**<br>|**Marks Inside**<br>**50**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bontempelli, Marcus|16|4.3%|4.6%|4.4%|4.4%|8.7%|7.4%|4.7%|3.4%|7.9%|5.3%|5.1%|4.2%|8.7%|
|Boyd, Matthew|19|6.8%|4.8%|7.9%|7.3%|3.2%|6.7%|6.3%|3.9%|6.6%|11.8%|8.0%|6.8%|3.5%|
|Cooney, Adam|18|5.6%|4.9%|5.4%|5.4%|6.3%|4.7%|4.9%|5.1%|6.1%|7.0%|5.2%|5.6%|3.6%|
|Griffen, Ryan|19|6.0%|2.2%|6.9%|6.4%|4.6%|6.5%|7.3%|3.6%|7.7%|12.3%|7.2%|5.8%|3.7%|
|Jong, Lin|6|2.4%|2.2%|3.9%|3.2%|3.5%|2.1%|6.6%|5.1%|3.3%|4.0%|3.9%|2.8%|0.0%|
|Liberatore, Tom|22|5.7%|4.0%|7.4%|6.6%|2.8%|2.7%|11.0%|5.7%|6.6%|17.4%|9.5%|4.9%|1.3%|
|Macrae, Jack|21|7.4%|7.8%|7.2%|7.4%|3.6%|2.8%|5.8%|5.6%|7.1%|5.5%|5.5%|8.6%|2.8%|
|Smith, Clay|1|4.3%|1.4%|3.0%|3.7%|0.0%|9.1%|2.6%|3.4%|4.8%|7.9%|3.5%|3.0%|0.0%|
|Stevens, Koby|20|3.7%|5.0%|5.9%|4.7%|6.9%|5.2%|3.6%|2.6%|3.0%|4.5%|4.2%|5.3%|6.9%|
|Tutt, Jason|7|5.1%|2.9%|2.7%|3.9%|11.1%|5.4%|5.5%|1.3%|7.0%|1.3%|3.6%|4.4%|5.1%|
|Wallis, Mitch|13|3.1%|2.0%|6.0%|4.5%|1.1%|1.7%|5.9%|2.2%|4.6%|8.7%|5.4%|4.1%|1.7%|
|**Midfield Average**|**14.7**|**5.3%**|**4.4%**|**6.2%**|**5.8%**|**4.9%**|**4.7%**|**6.3%**|**4.1%**|**6.2%**|**8.7%**|**6.2%**|**5.6%**|**3.8%**|
|**Team Average**|**11.9**|**4.6%**|**4.6%**|**4.6%**|**4.6%**|**4.7%**|**4.6%**|**4.5%**|**4.6%**|**4.6%**|**4.3%**|**4.5%**|**4.7%**|**4.6%**|





<!-- Start of picture text -->
5.3%<br>11.8%<br>7.0%<br>12.3%<br>4.0%<br>17.4%<br>5.5%<br>7.9%<br>4.5%<br>1.3%<br>8.7%<br>8.7%<br>4.3%<br><!-- End of picture text -->



<!-- Start of picture text -->
4.7%<br>6.3%<br>4.9%<br>7.3%<br>6.6%<br>11.0%<br>5.8%<br>2.6%<br>3.6%<br>5.5%<br>5.9%<br>6.3%<br>4.5%<br><!-- End of picture text -->



<!-- Start of picture text -->
4.4%<br>7.9%<br>5.4%<br>6.9%<br>3.9%<br>7.4%<br>7.2%<br>3.0%<br>5.9%<br>2.7%<br>6.0%<br>6.2%<br>4.6%<br><!-- End of picture text -->



## **APPLICATIONS:** Player evaluation 

|0.1<br>0.12<br>Marks<br>Goal Assists|
|---|
|0<br>0.02<br>0.04<br>0.06<br>0.08<br>Goals<br>Behi<br>Tackles<br>Rebound 50's<br>Clearances<br>Contested Possessions<br>ntested Possessions<br>Contested Marks|







## **APPLICATIONS:** Actual vs expected 



<!-- Start of picture text -->
Disposals<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>Normal Range Player Rolling Average<br><!-- End of picture text -->





## **LIMITATIONS** 

- Observational dependencies: 

   - Only controlled for team dependence within GEE model 

- Choice of correlation structure? 

- Issues with linear models? Mixed effect models? 

- Interpretability of data format by coaches? 



## **FUTURE DIRECTIONS** 

- Combined with magnitude data 

   - Preliminary analyses are positive 

- Additional of further data types 

   - Player couplings 

   - Ball movement motifs 

   - Other performance factors? 

- Which elements of the game do we most need versatility and player flexibility? 

- Other analysis techniques 







# **Questions?** 

sam.robertson@vu.edu.au @Robertson_SJ 




