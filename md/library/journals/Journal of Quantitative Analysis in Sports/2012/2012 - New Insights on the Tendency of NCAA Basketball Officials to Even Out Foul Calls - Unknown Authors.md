<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - New Insights on the Tendency of NCAA Basketball Officials to Even Out Foul Calls - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1402 

New Insights on the Tendency of NCAA Basketball Officials to Even Out Foul Calls 

**Cecilia A. Noecker,** _St. Olaf College_ **Paul Roback,** _St. Olaf College_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1402 

## New Insights on the Tendency of NCAA Basketball Officials to Even Out Foul Calls 

##### Cecilia A. Noecker and Paul Roback 

##### **Abstract** 

This analysis revises and strengthens a study by Anderson and Pierce (2009) on referee bias in NCAA basketball. Using a logistic regression model, they determined that referees display a statistically significant tendency to even out the foul count between the two teams—every additional increase in the foul differential (home team fouls minus visiting team fouls) raises the odds of a foul on the home team. This study analyzes Anderson and Pierce’s data on the 2004-2005 season from the Big Ten, Big East and ACC conferences, as well as additional data on the 2009-2010 season. Generalized linear mixed modeling, which takes into account the correlation in the data by game and by home and visiting teams, was used to consider the effect of several variables on the odds of a foul on the home team. These included the same variables used by Anderson and Pierce as well as additional terms including the timing and type of the foul. We also used estimates of the random effects in our models to study the relative proneness of different teams to fouls. 

In Anderson and Pierce’s logistic regression model, every additional unit of foul differential was found to raise the odds of a foul on the home team by 12.5% in 2004-2005. Using a generalized linear mixed model with the same terms, along with random effects for game, home team, and visiting team, raised that estimate to 19.9% and improved the quality of the model. A more indepth analysis of this data also found that a foul on the home team becomes less likely as the game progresses, particularly when the home team is winning. Similar results were found in an analysis of data from the 2009-2010 season. The 2009-2010 analysis also found evidence that the odds of more subjective offensive fouls were more affected by foul differential than personal or shooting fouls. The effect of individual referees on the amount of bias in each foul call was explored through a preliminary analysis but no significant results were found. 

A tendency to even out the number of foul calls on each team has the potential to lead to increased physicality in NCAA basketball if the referee tries to keep the foul count close even when one team is clearly playing more physically. These results strengthen the evidence that referees display this propensity significantly, consciously or unconsciously. 

**KEYWORDS:** college basketball, foul differential, referee bias, generalized linear mixed models 

**Author Notes:** We gratefully acknowledge Kyle Anderson and David Pierce for the use of their data, and Matt Richey for his assistance in obtaining additional data. This work was partially supported by National Science Foundation grant # 0354308. 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

### **1 Introduction** 

Fairness is a central value in human society, and multiple studies (Fehr et al (2008), Wallace et al (2007)) have suggested that fairness is an evolved genetic trait. For instance, Fehr et al found that young children prefer to divide candy among a group equally rather than take more for themselves. However, fair behavior might be simply one application of a more fundamental trait of maintaining peace among groups of people. In this case, creating an appearance of fairness is more highly valued than actually behaving fairly, a key distinction. Referees and officials play a crucial role as the arbiters of fairness in sports, and they are often under high pressure from teams and fans to make fair calls. However, making fair calls— making the correct decision each time, independent of any previous decisions—may come into conflict with the appearance of fair officiating, or seeming to favor neither team over the course of a game. Thus, referees and officials could occasionally have incentive, either consciously or subconsciously, to make an unfair individual decision to maintain the overall aura of fairness. 

A recent article by Anderson and Pierce (2009) described empirical evidence that officials in NCAA men’s college basketball tend to “even out” foul calls over the course of a game. Using logistic regression to model the effect of foul differential on the probability that the next foul called would be on the home team (controlling for score differential, conference, and whether or not the home team had the lead), Anderson and Pierce found that “the probability of the next foul being called on the visiting team can reach as high as 0.70.” In this article, we build on the results of Anderson and Pierce by strengthening their model through the use of generalized linear mixed effects models, by considering nuances of the association between foul differential and foul calls, and by examining the variance estimates of random effects to make inferences about individual teams. In addition, we collected more recent and comprehensive data on NCAA fouls to determine if the tendency to even out calls persists and, more significantly, if this effect is stronger for foul calls over which referees have greater control. While the tendency of referees to even out foul calls might be a natural human reaction as conflict arbitration, it has potential implications for competitive basketball, as teams are allowed to play more physically and aggressively with fewer consequences. 

Most of the studies conducted to investigate potential (conscious or subconscious) bias in sports referees have focused on the tendency of referees to favor the home team. These have demonstrated that officials can be very susceptible to fan influence. Greer (1983) and Nevill and Holder (1999) showed that the home field advantage enjoyed in most sports is due to the crowd’s effect on officials rather than the crowd’s effect on team performance or other advantages enjoyed by a home team (e.g., learning, travel, rules). In fact, Nevill et al (2002) later showed through 

1 

###### _Submission to Journal of Quantitative Analysis in Sports_ 

experimental methods that crowd noise has a dramatic effect on how officials respond to potential fouls on videotape. A recent book by Moskowitz and Wertheim (2011) summarizes and extends much of this work on home team referee bias. Like Nevill and Holder, they conclude that referee bias is the number one reason for home field advantage in sports. They cite new evidence from baseball (using called balls and strikes, especially in crucial situations) and football (using lost fumbles). Interestingly, some referee bias disappeared upon the introduction of QuesTec to track pitches in baseball and instant replay to review changes of possession in football, indicating that concern about outside assessment plays some role, conscious or subconscious, in the degree of bias. Furthermore, greater home team favoritism was found to be associated with sports in which there is greater referee influence (e.g., soccer, basketball). Moskowitz and Wertheim also offer ideas supported by the psychological literature on social influence related to why there may be a home team bias among sports referees, including deep-seated tendencies to conform to group behavior and reduce the potential for anxiety. Several other authors have confirmed the presence of home field bias in soccer specifically including Sutter and Kocher (2004), Buraimo et al (2010), and Dohmen (2008). 

Referee bias may result from other influences besides the home crowd. There often exists a tension between a referee’s desire to make fair and objective calls and the desire to give the impression that they are being fair to fans and players. A report by Pedowitz (2008), commissioned in response to a betting scandal involving referee Tim Donaghy in the NBA, discusses the difficulty of remaining objective. The report authors stated, “Referees were also conscious of game circumstances and considered them when making judgments about calls. For instance, we have been told that some referees maintained an awareness of substantial imbalances in foul calls against teams.” By calling an approximately equal number of fouls on each team, a referee appears more objective even if one team is actually deserving of more fouls. 

Plessner and Betsch (2001) were among the first, in soccer again, to systematically study the effects of previous referee calls on the current call. They used videotaped scenes from actual matches and found that participants’ decisions to award penalty kicks were influenced by past decisions in the same game. Schwarz (2011) showed a similar tendency exists in penalty kick decisions in actual games from the German Bundesliga. Anderson and Pierce (2009) then brought this approach to foul calls in college basketball, and their work received considerable interest in the popular press. Moskowitz and Wertheim’s book (2011) mentioned the results of Anderson and Pierce and proceeded to document instances in several other sports in which officials’ decisions seemed to be influenced by previous calls, often in a manner that served to “even out” calls. For instance, baseball umpires are more likely to call a ball on an 0-2 count and a strike on a 3-0 count. 

2 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

However, not all referee decisions are made under equal conditions, and the amount of discretion a basketball referee has in a call can vary depending on the type of foul or turnover, the stage of the game, the importance of a game, and characteristics of the individual referee. Price et al (2009) examined biases of NBA referees that favor home teams, teams losing during games, and teams losing in playoff series. Price et al hypothesized that any referee bias would be more evident on foul and turnover calls where referees are able to exercise greater discretion, after controlling for score differential and other important covariates. Turnovers were classified into two groups— discretionary (e.g., traveling, palming) and nondiscretionary (e.g., bad passes and lost balls that go out of bounds). They found that referees are more influenced by previous calls on discretionary turnovers, and on discretionary fouls (e.g., offensive) rather than less discretionary fouls (e.g., shooting). This “dose-response curve” provides even stronger evidence of a tendency toward evening out calls in the NBA than an analysis which treats all fouls and turnovers the same. 

Our results are presented in three parts. First, we present summaries of exploratory analysis from both 2004-05 and 2009-10 to examine (a) if overall trends indicate relationships between the team whistled for a foul and foul differential, score differential, and other covariates, and (b) if trends have remained constant between the two seasons. Second, we re-examine Anderson and Pierce’s data from 2004-05 after adding information about the referee crew for each Big Ten game to determine if additional insight can be discovered by applying a generalized linear mixed model, which seemed more appropriate given the hierarchical structure of the data and the presumed correlations within game, within referee, and within team. We analyzed the role of potential covariates including which team is leading, the score differential, the timing of each foul, and the referee involved. Third, we modeled data from the 2009-10 season to determine whether similar evidence that referees tend to even out foul calls existed five years later and whether the effect is greater among fouls over which officials have greater control. We hypothesized that we would find greater evidence of evening out calls among fouls over which the referee has greater discretion. 

### **2 Data** 

Data were collected from three different sources: 2004-05 season data on individual foul calls compiled by Anderson and Pierce (2009), 2004-05 information about referees for Big Ten games compiled from www.statsheet.com, and 2009-10 season data on individual foul calls compiled from www.cbssports.com. The dataset used by Anderson and Pierce (2009) includes information on all of the fouls in the first 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

halves of 365 NCAA men’s college basketball games played during the 2004-05 conference season in the Big Ten, Big East and ACC, as well as games in the NCAA tournament. Only first half fouls were included to avoid intentional fouls by trailing teams at the end of the second half. This study analyzes the 4143 fouls in the 272 regular season games in the three conferences, an average of 15.2 fouls per game. Information is included on whether each foul was on the home or visiting team, the number of the foul in the game chronologically, the difference in number of fouls between the two teams at the time, and the difference in scores between the two teams at the time. For each of the 98 Big Ten regular season games, the dataset was expanded to include the three referees, using information from www.statsheet.com. Lastly, similar but more extensive data were collected from www.cbssports.com on fouls from 340 regular season games in the same three conferences during the 2009-10 season. The second half was again excluded for consistency. The type of foul committed and the time left in the half when the foul was committed were also included in this dataset. 

### **3 Models and Results** 

#### **3.1 Exploratory Data Analysis** 

Summary statistics are very similar between the 2004-05 and 2009-10 datasets. 1941 of the 4143 fouls (46.9%) were on the home team in 2004-05, compared with 2384 of 4972 (47.9%) in 2009-10. The mean and standard deviation of the foul differential and the score differential at the time of the foul are shown in Table 1 for both seasons, and Figure 1 shows the distribution of foul differential in both seasons. In both seasons, the home team is in the lead more often than not, and it receives fewer foul calls overall. Table 2 shows that whichever team is winning receives a larger proportion of foul calls, but that the effect appears much larger when the visiting team is ahead. When the score is tied, the visiting team receives more foul calls. The 2009-10 data in Table 2 include offensive fouls, other personal fouls, and shooting fouls. A breakdown of 2009-10 foul types in Table 3 shows that personal fouls were the most common, followed by shooting fouls and finally offensive fouls. Technical fouls were excluded due to their relative rarity ( _n_ =26). 

Graphical evidence for the effect of foul differential is shown in Figures 2, 3 and 4. Each of these plots depicts both the proportion of fouls and the log odds of a foul on the home team under different circumstances, with loess curves illustrating patterns among subgroups. Approximately linear relationships can be seen between the log odds of a foul on the home team and the foul and score differentials, which indicates that a logistic generalized linear model would be appropriate for analysis 

4 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

Table 1: Foul and score differential for 4143 fouls from 272 games from 2004-05 and 4972 fouls from 340 games from 2009-10. 

||2004|-05|2009|-10|
|---|---|---|---|---|
||Mean|SD|Mean|SD|
|Foul differential|-0.96|2.72|-0.36|2.05|
|Score differential|2.24|9.74|2.04|7.24|





<!-- Start of picture text -->
−10 −5 0 5 −10 −5 0 5<br>Foul differential Foul differential<br>80<br>100<br>60<br>80<br>60<br>40<br>Frequency Frequency<br>40<br>20<br>20<br>0 0<br><!-- End of picture text -->

Figure 1: Distribution of foul differential in 2004-05 (left) and 2009-10 (right). 

Table 2: Foul counts in different game lead situations. 

||Percent of f|ouls on home team|
|---|---|---|
||2004-05|2009-10|
|When the home team is leading|51.7%|50.8%|
|When the score is tied|45.5%|46.3%|
|When the visitingteam is leading|42.3%|41.2%|



of this data. The plots showing proportions of fouls on the right of each figure are included for ease of interpretation. Figure 2 shows that fouls on the home team may be more likely when they are winning and when the visiting team has committed more previous fouls (i.e., the foul differential is negative). Figure 3 shows that the 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

Table 3: Number of different types of fouls in the 2009-10 dataset. 

|Foul type|Number of fouls|
|---|---|
|Offensive|484|
|Personal|2564|
|Shooting|1924|
|Total|4972|



effect of foul differential on the odds of a foul appears to be more pronounced for offensive fouls than other personal fouls, and for personal fouls more than shooting fouls. In Figure 4, the timing of the foul appears to have a potential interaction with the role of foul differential, which seems to have a slightly greater effect earlier in the game. Additionally, Figure 5 demonstrates the role of score differential. A larger difference in points between the home and visiting team seems to increase the odds of a foul on the home team; in fact, there is a noticeable jump in the log odds of a foul on the home team when the home team takes the lead—i.e., when the score differential crosses 0. 



<!-- Start of picture text -->
G G Home Team Winning G Home Team Winning<br>Home Team Losing or Tied Home Team Losing or Tied<br>G<br>G<br>G<br>G<br>G<br>G<br>G G G G G G<br>G G G G G<br>G<br>G G G<br>G G<br>G G<br>G G<br>−6 −4 −2 0 2 4 6 −6 −4 −2 0 2 4 6<br>Foul differential Foul differential<br>1.0<br>0.4<br>0.8<br>0.2<br>0.6<br>0.0<br>−0.2 0.4<br>−0.4<br>0.2<br>Log odds of Fouls on the Home Team in 2004−05 Proportion of Fouls on the Home Team in 2004−05<br>−0.6<br>0.0<br><!-- End of picture text -->

Figure 2: Log odds of a foul (left) and proportion of fouls (right) on the home team in 2004-05 vs. foul differential, when the home team is winning and when they are losing or tied. Each point represents the log odds or proportion of fouls on the home team for all fouls called when the foul differential was equal to a particular value. Loess smoothing curves are used to illustrate trends. Values of foul differential at which there were 5 or fewer fouls in the dataset were excluded. 

6 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 



<!-- Start of picture text -->
G G Offensive Fouls G Offensive Fouls<br>Personal Fouls Personal Fouls<br>Shooting Fouls Shooting Fouls<br>G<br>G<br>G G<br>G<br>G<br>G G G G<br>G G G G<br>G G G G<br>G<br>G<br>G<br>−8 −6 −4 −2 0 2 4 6 −8 −6 −4 −2 0 2 4 6<br>Foul differential Foul differential<br>1.5<br>1.0<br>1.0<br>0.8<br>0.5<br>0.0 0.6<br>−0.5<br>0.4<br>−1.0<br>0.2<br>Log Odds of Fouls on the Home Team in 2009−10 −1.5 Proportion of Fouls on the Home Team in 2009−10<br>−2.0 0.0<br><!-- End of picture text -->

Figure 3: Log odds of a foul (left) and proportion of fouls (right) on the home team in 2009-10 vs. foul differential for varying types of fouls. Each point represents the log odds or proportion of fouls on the home team for all fouls of one type called when the foul differential was equal to a particular value. Loess smoothing curves are used to illustrate trends. Values of foul differential at which there were 5 or fewer fouls in the dataset were excluded. 

#### **3.2 Analysis of 2004-05 Foul Data** 

##### **3.2.1 Original 2004-05 Model** 

Anderson and Pierce based their 2009 paper on the logistic regression model shown in the first column of Table 4. In a logistic model, the response is the logarithm of the odds of an event occurring—in this case, the log odds of a foul being called on the home team as opposed to the visiting team. Anderson and Pierce’s logistic model includes explanatory variables for the difference in fouls between the teams ( _foul.diff_ ), the difference in score ( _score.diff_ ), an indicator variable for whether the home team was leading ( _lead.home_ ), and indicator variables for the Big 10 ( _big10_ ) and ACC ( _acc_ ) conferences, using Big East as the reference level. Note that score and foul differentials are always calculated as home total minus visitor total. This logistic model has the following structure: 



7 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
G Last 10 minutes G Last 10 minutes<br>First 10 minutes First 10 minutes<br>G<br>G<br>G G<br>G G G G G G G G G G G G G G<br>G G G G<br>G G<br>G G<br>G<br>G<br>−8 −6 −4 −2 0 2 4 6 −8 −6 −4 −2 0 2 4 6<br>Foul differential Foul differential<br>2 1.0<br>0.8<br>1<br>0.6<br>0<br>0.4<br>−1<br>0.2<br>Log Odds of Fouls on the Home Team in 2009−10 Proportion of Fouls on the Home Team in 2009−10<br>−2 0.0<br><!-- End of picture text -->

Figure 4: Log odds of a foul (left) and proportion of fouls (right) on the home team in 2009-10 vs. foul differential for varying time remaining in the first half. Each point represents the log odds or proportion of fouls on the home team for all fouls in that time period called when the foul differential was equal to a particular value. Loess smoothing curves are used to illustrate trends. Values of foul differential for which there were 5 or fewer data points were excluded. 

where _pi_ is the probability that the _i_<sup>_th_</sup> foul in the data set is on the home team. 

In Anderson and Pierce’s original model using data from 2004-05, foul differential has a significant negative effect on the odds of a foul on the home team. As the visiting team accumulates another foul relative to the home team, the odds of a home foul increase by 12.5%, controlling for score differential, whether the home team has the lead, and conference. Notably, the variables for home team lead and score differential both affect the odds of a foul. Every point scored by the home team makes it significantly more likely that they will receive a foul call, but it becomes particularly more likely when the score differential crosses 0 (i.e., there is a non-linear jump in the log odds of a home team foul when the home team takes the lead). This is illustrated graphically in Figure 5, which shows how the chance of a foul on the home team varies with the score differential. 

##### **3.2.2 Original 2004-05 Model using GLMM** 

Anderson and Pierce’s model was then expanded into a generalized linear mixed model (GLMM) using the _lme4_ package in R (shown in the second column of Ta- 

8 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 



<!-- Start of picture text -->
G<br>G<br>G G G<br>G G<br>G G G G<br>G G<br>G<br>G G G<br>G G G G G G G G G G G G G G G G G G G G G G G<br>G G G G G G G G G G G G G G G G G<br>G<br>G<br>G G Home Team Losing or Tied G Home Team Losing or Tied<br>G G Home Team Winning G Home Team Winning<br>−15 −10 −5 0 5 10 15 −15 −10 −5 0 5 10 15<br>Score Differential Score Differential<br>G<br>G<br>G<br>G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G<br>G<br>G G<br>G<br>G Home Team Losing or Tied G Home Team Losing or Tied<br>G Home Team Winning G Home Team Winning<br>−20 −10 0 10 20 −20 −10 0 10 20<br>Score Differential Score Differential<br>1.0<br>0.0<br>0.8<br>−0.2 0.6<br>−0.4 0.4<br>Log odds of a home team foul in 2004−05 0.2<br>−0.6 Proportion of fouls on the home team in 2004−05<br>0.0<br>1.0<br>0.5<br>0.8<br>0.6<br>0.0<br>0.4<br>−0.5<br>Log odds of a home team foul in 2009−10 0.2<br>Proportion of fouls on the home team in 2009−10<br>−1.0 0.0<br><!-- End of picture text -->

Figure 5: Mean log odds of a foul (left) and proportion of fouls (right) on the home team in 2004-05 (top) and 2009-10 (bottom) vs. score differential. Each point represents the log odds or proportion of fouls on the home team for all fouls called when the score differential was equal to a particular value. Loess smoothing curves are used to illustrate trends. 

ble 4), with random effects for each game and each team. The values of the variance estimates associated with each random effect are given in Table 5. This model structure is more faithful to the manner in which data were accumulated than a generalized linear model with fixed effects only, because it acknowledges a correlation between foul calls in the same game or involving the same team. This model included random effects for each game and for each of the 33 home and visiting teams. 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

Table 4: Model coefficients and standard errors for models of 2004-05 fouls and 2009-10 fouls, with standard errors in parentheses and significance indicated with <u>asterisks.</u> 

|**Variable**|**Original**|**Original as GLMM**|**Expanded ’04-’05**|**’09-’10**|
|---|---|---|---|---|
|Intercept|-0.332(0.072)***|-0.387(0.112)***|-0.375(0.109)***|-0.247(0.130).|
|_foul.diff_|-0.118(0.0153)***|-0.182(0.017)***|-0.238(0.019)*|-0.172(0.034)***|
|_score.diff_|0.009(0.006)|0.016(0.007)*|0.031(0.008)***|0.034(0.008)***|
|_lead.home_|0.252(0.096)**|0.294(0.100)**|0.499(0.136)***|-0.150(0.175)|
|_foul.num_|||-0.002(0.010)||
|_big10_|0.023(0.080)|0.019(0.146)|||
|_acc_|-0.014(0.075)|-0.032(0.143)|||
|_time.left_||||-0.009(0.008)|
|_offensive_||||-0.081(0.110)|
|_personal_||||0.067(0.064)|
|_foul.diff*_<br>_score.diff_|||0.007 (0.002)***||
|_foul.num*_<br>_lead.home_|||-0.033 (0.013)*||
|_foul.diff*_<br>_offensive_||||-0.103 (0.053).|
|_foul.diff*_<br>_personal_||||-0.056 (0.032).|
|_foul.diff*_<br>_time.left_||||-0.009 (0.003)**|
|_lead.home*_<br>_time.left_||||0.026 (0.012)*|



Table 5: Variance estimates associated with random effects for the three mixed <u>models.</u> 

|Model|Groups|Number of observations|Variance|
|---|---|---|---|
||Game|272|0.053|
|Original Model as GLMM|Visiting team<br>Home team|34<br>34|0.042<br>0.036|
||Game|272|0.101|
|Expanded 2004-05 Model|Visiting team|34|0.060|
||Home team|34|0.044|
||Game|340|0.185|
|2009-10 Model|Visiting team|39|0.043|
||Home team|39|0.078|



power, considering the large number of teams included in the data, and because we were principally interested in trends in foul calls across teams rather than for par- 

10 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

ticular teams. Including games and teams as fixed effects produced similar results. The structure of the original mixed model can be seen below, where _pi j_ represents the probability that foul _j_ from game _i_ is on the home team. It includes the random effects terms _εi_ (for game _i_ ), _ηki_ (for home team _ki_ from game _i_ ), and _νmi_ (for visiting team _mi_ from game _i_ ). All random effects are assumed to be independently and identically distributed as normal random variables with mean 0 and separate variance terms; that is, _εi ∼ N_ (0 _, σG_<sup>2),</sup><sup>_ηk_</sup> _i_<sup>_∼N_(0</sup><sup>_,σ_</sup> _H_<sup>2), and</sup><sup>_νm_</sup> _i_<sup>_∼N_(0</sup><sup>_,σ_</sup> _V_<sup>2).</sup> 



Including these random effects lowered the model AIC value from 5641 to 5632, suggesting an improved model. The coefficients in the GLMM are generally of slightly higher magnitude and significance compared to the model without random effects, including the coefficient for foul differential. According to the GLMM model, each extra foul on the visiting team relative to the home team increases the odds that the next foul will be on the home team by 19.9% (95% confidence interval 16.0% to 24.0%). This effect is substantially greater than the estimate generated using the original Anderson and Pierce model, which suggested that each extra foul on the visiting team relative to the home team increases the odds of a home team foul by an estimated 12.5%, (95% confidence interval 9.2% to 16.0%). As an example, in a game between two Big East teams, when the score is tied and the visiting team has committed 5 more fouls than the home team, the GLMM predicts that the likelihood that the next foul is on the home team is around 62.8%. In the original model, the predicted likelihood that the next foul is on the home team is a more conservative 56.4%. 

##### **3.2.3 Expanded 2004-05 Model** 

Using the original GLMM model from section 3.2.2 as a starting point, we built new models using AIC scores to compare non-nested models and likelihood ratio tests to compare nested models. Likelihood ratio tests were used to determine whether the inclusion of random effects significantly improved the model. The insignificant conference terms were removed; the probability of a home foul appears constant in the three conferences after controlling for the other explanatory variables. A variable for the number of previous fouls in the game ( _foul.num_ ) was added to the model to represent the effect of time and investigate the possibility that referees may tend to even out fouls more or less as the game progresses. Finally, interactions 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

between the significant explanatory variables were tested, and we learned that the effect of foul differential depends on score differential and the effect of home team lead changes over time. The same random effects were included as in the previous model. 

The structure of the expanded model is shown below using the same indices as the previous model. A summary of the fixed effect coefficient estimates is presented in the third column of Table 4 and estimates of the variance components associated with the random effects are presented in the middle rows of Table 5. 



The model enhancements offer additional insights into the effect of foul differential on foul calls. The effect of foul differential is again negative and significant (indicating a significant tendency to even out foul calls), but it is slightly mitigated by an interaction with score differential. According to this model, as the home team accumulates a larger lead, the effect of a change in foul differential is reduced. If the home team is winning by 20 points, each extra foul on the visiting team relative to the home team increases the odds of a foul on the home team by only 10.8%, whereas if they are losing by 20 points, that same change in foul differential increases the odds by 45.1%. In a tie game, each foul on the visiting team raises the odds of another home team foul by 26.8%. 

Additionally, fouls on the home team become significantly less likely as the half progresses. This is especially true when the home team is winning, as reflected by the interaction between home team lead and foul number. For instance, a lead for the home team makes it 59.5% more likely that the next foul will be on them if it is the first foul of the game, but only 15.2% more likely if it is the 11th foul of the game. 

##### **3.2.4 Preliminary Analysis of the Role of Individual Referees** 

We wondered whether the tendency to even out foul calls in college basketball varied by referee. To investigate this question, we added referee names from the 88 Big Ten games to our 2004-05 dataset, which included 47 different referees. Because three referees officiate each NCAA game and our data did not specify which referee made which foul call, accounting for the effects of individual referees proved difficult. A logistic model with foul differential as the only explanatory variable was 

12 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

created for the subset of games involving each referee. Figure 6 shows the distribution of coefficient values for foul differential from these models, demonstrating that the effect of foul differential is highly variable depending on the referees involved. Figure 7 shows a plot of the effects of the foul differential on the log odds of a foul on the home team for the five most prevalent Big Ten referees, as well as for the games in which none of the five were involved. This plot seems to suggest that these busier referees have steeper slopes for the effect of foul differential— that they are more susceptible to considering the foul count in their calls than less frequently involved officials. However, we tested the interaction between referee and foul differential in several models and did not find the term to be statistically significant. 



<!-- Start of picture text -->
−0.6 −0.4 −0.2 0.0<br>Coefficient for foul differential<br>20<br>15<br>10<br>Frequency<br>5<br>0<br><!-- End of picture text -->

Figure 6: The distribution of the effect of foul differential for individual referees in Big Ten regular season games from 2004-05. 

#### **3.3 Analysis of 2009-10 Foul Data** 

We investigated the effect of foul differential and other factors on whether a foul is called on the home team using recently compiled 2009-10 data. A logistic random 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 



<!-- Start of picture text -->
G 5 Most Frequent Referees G 5 Most Frequent Referees<br>Others Others<br>G<br>G<br>G G<br>G<br>G<br>G<br>G<br>G<br>G<br>−4 −2 0 2 4 −4 −2 0 2 4<br>Foul Differential Before the Foul Foul Differential Before the Foul<br>1.0<br>0.5 0.8<br>0.6<br>0.0<br>0.4<br>−0.5 0.2<br>Log Odds of a Foul on the Home Team in 2004−05 Proportion of Fouls on the Home Team in 2004−05<br>0.0<br><!-- End of picture text -->

Figure 7: The effects of foul differential on the log odds (left) and proportion (right) of a foul on the home team for the most frequent referees compared with the rest of the referees officiating Big Ten regular season games from 2004-05. Each point represents the log odds or proportion of fouls on the home team for all fouls called when the foul differential was equal to a particular value. Loess smoothing curves are used to illustrate trends. 

effects model for the 2009-10 data, shown below using the same notation as previously, included additional information on the type of foul committed (offensive, personal, or shooting) and the time in minutes left in the half when the foul was committed ( _time.left_ ). 



Results of this model are shown in the fourth column of Table 4, with estimates of the variance components associated with the random effects in Table 5. Foul differential again has a similarly large and significant effect as in the 2004-05 season, indicating that a tendency to even out foul calls persists. As the foul differential decreases by 1 (the visiting team is called for an additional foul), the odds 

14 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

of a shooting foul on the home team increase by 18.7% at the end of the half, after controlling for the effects of score differential and whether the home team has the lead. However, the effect of foul differential varies depending on type of foul called and time left in the half—the tendency for evening out foul calls is stronger earlier in the half and when offensive and personal fouls are called instead of shooting fouls. 

The effect of foul differential decreases significantly by 0.9% for each extra minute that has passed in the half, after controlling for score differential, whether the home team has the lead, and type of foul (see Figure 4). For example, midway through the half ( _time.left_ =10), the odds that a shooting foul is on the home team increase by 29.5% for each extra foul on the visiting team, while at the end of the half ( _time.left_ =0) the odds increase by 18.7% for each extra visiting foul. If the score is tied and the visiting team has committed 5 more fouls than the home team when a shooting foul is called, there is an 72.3% chance that the foul will be on the home team in the middle of the half. At the end of the half, this percentage has decreased to 64.7%. 

According to the 2009-10 model, offensive fouls are most affected by the foul differential, followed by personal fouls and then shooting fouls (see Figure 3). These effects were marginally significant (p=0.052 for offensive fouls and p=0.078 for personal fouls), and their inclusion in the model improved the AIC. At the end of the half (when _time.left_ =0), one more foul on the visiting team relative to the home team makes it 18.7% more likely a foul will be called on the home team if it is a shooting foul, 25.5% more likely if it is a personal foul, and 31.7% more likely if it is an offensive foul. Again assuming the visiting team has committed 5 more fouls and the score is tied, the probability the next foul is on the home team at the end of the half is 64.7% for shooting fouls, 72.2% for personal fouls, and 74.0% for offensive fouls. 

Note that, after accounting for time and foul type, we found no evidence in 2009-10 of a foul differential by score differential interaction as we saw in 2004-05. That is, our newer data showed that the effect of foul differential does not change with the score of the game. Through our estimated variances in Table 5, we see the log odds of a foul on the home team varies most notably from game-to-game, and that the variance among home teams is larger than the variability among visiting teams. 

##### **3.3.1 Random Effects Estimates for Individual Teams** 

One valuable benefit of random effects modeling is the ability to produce estimates of the random effects for each of the groups, called best linear unbiased predictors 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

(BLUPS). In this case, we can estimate the effect of each of the home and visiting teams on the odds of a foul on the home team. These estimates provide an idea of which teams contribute the most and least to the odds of a foul on the home team, both as the home team, meaning they are particularly foul-prone, and as the visiting team, indicating that they cause their opponents to commit a lot of fouls. Figure 8 shows the random effects estimates for each of the 39 teams in the 200910 data. Some teams are clear standouts: DePaul, Virginia, Seton Hall and Indiana are estimated to be the most foul-prone teams whether at home or on the road, while Notre Dame, West Virginia and Syracuse appear to be the least foul-prone. These data also suggest that teams such as Georgia Tech, Marquette, and Pittsburgh play more aggressively at home but are less foul-prone on the road. However, the margins of error for these estimates are relatively large. 



<!-- Start of picture text -->
DEPAUL G ND G<br>SETON G WV G<br>STJNNY G NC G<br>CIN G MARQET G<br>VA G OHST G<br>NCST G PITT G<br>IN G MI G<br>NOVA G SYR G<br>IA G FLST G<br>SFL G GATECH G<br>GATECH G WF G<br>MIST G PSU G<br>RUT G CT G<br>MARQET G PUR G<br>PITT G SFL G<br>MIA G MD G<br>LOU G BC G<br>VATECH G NOVA G<br>IL G PROV G<br>PSU G RUT G<br>WI G MN G<br>WF G LOU G<br>BC G DUKE G<br>FLST G NCST G<br>NC G WI G<br>NW G GTOWN G<br>PROV G CIN G<br>MD G STJNNY G<br>OHST G VATECH G<br>DUKE G IL G<br>MI G NW G<br>GTOWN G MIA G<br>CLEM G MIST G<br>WV G CLEM G<br>CT G IA G<br>ND G SETON G<br>MN G VA G<br>SYR G DEPAUL G<br>PUR G IN G<br>−0.5 0.0 0.5 −0.6 −0.4 −0.2 0.0 0.2 0.4<br><!-- End of picture text -->

Figure 8: Estimates of the best linear unbiased predictors for each of the 39 home teams (left) and visiting teams (right) for the 2009-10 season. 

### **4 Discussion** 

This analysis updates and strengthens Anderson and Pierce’s 2009 model of referee bias in NCAA basketball foul calls while providing a more nuanced view of the effect of foul differential on a referee’s foul calls. Generalized linear mixed models account for the correlated structure of the data and estimate the effects of individual teams. Under all analyses, the difference in number of fouls between the home and 

16 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

visiting teams is found to be the most significant predictor of the odds of a foul on the home team, even after controlling for other significant predictors such as score differential, home team lead, the timing of the foul, and the type of foul committed. 

However, as Price et al (2009) and Moskowitz and Wertheim (2011) argue, if there is truly a (conscious or subconscious) tendency for referees to even out foul calls over the course of a game, we should observe a stronger effect of foul differential on calls that involve a greater degree of subjectivity by the referee. In basketball, offensive fouls are typically regarded as the toughest calls to make and therefore most prone to referee subjectivity, while shooting fouls are typically more obvious and less subjective. Indeed, we find some evidence in our 2009-10 data of an interaction between foul type and foul differential. Offensive fouls seemed to be associated with the strongest effects of foul differential, while shooting fouls seemed to be associated with the weakest foul differential effects. 

Using a generalized linear mixed model rather than a basic logistic model effectively accounts for the correlated nature of the foul data within individual games, home teams, and visiting teams. A mixed model applied to the 2004-05 data with exactly the same terms as Anderson and Pierce’s model, except with added random effects, found a larger effect of foul differential—each extra foul for the visiting team relative to the home team increases the odds of a foul on the home team by 19.9% compared with 12.5%. This difference is due to the GLMM’s ability to separate the trend from the similarities between calls in the same game and on the same team. The estimated odds increases for a decrease in the home-visitor foul differential were actually stronger in 2009-10 than 2004-05: 31.7% for offensive fouls, 25.5% for personal fouls, and 18.7% for shooting fouls. Continued expansion of the mixed model shows that the effect of foul differential in 2004-05 actually varied depending on the score. In 2009-10, there was no longer evidence that the effect of foul differential depended on the score of the game, but there was significant evidence that it depended on time elapsed in addition to foul type. 

The use of generalized linear mixed models also allows for study of the effects of individual teams by considering the estimates of the random effects for each team. DePaul, Virginia, Seton Hall and Indiana were estimated to be the most foul-prone teams in 2009-10 according to this method. However, it is important to note that these are based on conditional modes and the prediction intervals for these estimates are extremely large. 

The role of individual referees is another topic on which future study would be valuable. Figure 6 suggests that referees may display a foul differential bias to widely varying degrees. Although a preliminary study of graphical evidence (see Figure 7) suggests that more experienced referees may be more affected by foul differential than their less experienced counterparts in the Big Ten, we were unable to find significant evidence that any one referee is significantly more biased by foul 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

differential than others. To further examine the behavior of individual referees, knowing which fouls were called by which referees would be essential. 

The confirmation of a significant association between foul differential and foul calls with 2009-10 data, and evidence of a “dose-response” relationship based on perceived referee subjectivity suggests several directions for future analysis. It may have been slightly excessive to exclude the entire second half instead of just the last few minutes of each game, but doing so allowed us to follow and expand upon the previous work by Anderson and Pierce. It may be worthwhile to model second half fouls to see if the observed trends change at all, particularly the trend observed in the 2009-10 data showing that the effect of foul differential decreases as the game progresses. There are other potential sources of bias that could also be incorporated into this model, such as the caliber of the player committing the foul and how many fouls they already have in the game. Moskowitz and Wertheim (2011) previously demonstrated that both of these factors affect the odds of a foul. Several authors (e.g., Buraimo et al (2010) and Dohnen (2008)), when examining home team bias, have found evidence of greater bias when crowds are larger, more partisan, and closer to the field; crowd-related covariates could be included in future analyses of foul differential. 

Other possibilities include using a variable that represents the differential of the five most recent foul calls as a predictor, adding an indicator variable for when the foul differential crosses a certain limit (e.g., becomes greater than 5 in magnitude), or accounting for when one of the teams has reached a bonus situation, where teams are subject to additional penalties (opponent free throws) for each foul after their first 6 in the half. Another possibility is that the current streak of fouls, such as when 4 fouls in a row have been called on one team, is a stronger predictor than simply the overall difference in fouls between the two teams. One of these quantities may describe the inclination to even out foul calls more accurately than the simple foul differential. Finally, expanding our analyses to turnover calls, if that data were available for collegiate games, could further strengthen conclusions, especially by comparing discretionary and non-discretionary turnovers. 

Basketball is not the only sport in which officials may introduce bias to keep the appearance of fairness. Referees may show the same behavior in football and hockey. Umpires might tend to even out marginal strike calls, or use a smaller strike zone for pitchers who throw more strikes. Judges in sports such as gymnastics and ice skating could potentially tend to impose harder penalties on other competitors if one does poorly. 

Furthermore, there may be broader implications of this trend beyond sports. Recent studies in cognitive psychology, including Fehr et al (2008) and Wallace et al (2007), have suggested that fairness is an evolved genetic trait. But the appearance of fairness might be more fundamentally important than actual fairness, if the 

18 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

broader favorable trait is to maintain peace among groups of people. From a neuroscience perspective, one could address this question by studying whether the same regions of the brain are involved when a referee makes a call (particularly a call that evens out the foul differential) as when a child is determining how to divide up a bag of candy. 

The difference between creating an impression of fairness and actually behaving fairly has potential effects in many fields, particularly in any kind of assessment or evaluation. Teachers may grade some students harder or easier than others for the sake of avoiding conflict and encouraging each student to learn, even if that means departing from a completely fair grading scale. Similarly, David Brooks argues that intuition regarding fairness can have economic effects in his recent book _The Social Animal_ : “People demand salaries that seem fair, and managers have to take these moral intuitions into account when setting pay scales” (179). What seems like fair compensation to an employee may not correspond with what is actually fair based strictly on achievement, a disparity that can potentially have real positive or negative economic effects. 

The nature of the game of basketball in particular demonstrates that a preference for the appearance of fairness can have negative consequences, since teams may be willing to play more physically and aggressively as long as the foul differential remains small. Anderson and Pierce cite coach comments and an NCAA report indicating that the game has become increasingly physical in recent years. This paper strengthens the evidence that at least some of this change is due to officiating bias against the team with fewer fouls. 

### **5 References** 

- Anderson, K. J., and Pierce, D. A. (2009), “Officiating Bias: The Effect of Foul Differential on Foul Calls in NCAA Basketball,” _Journal of Sports Sciences_ , 27, 687-694. 

Automated Insights, Inc. (2012), _StatSheet_ , URL `www.statsheet.com` . 

- Bates, D., Maechler, M., and Bolker, B. (2012), _lme4: Linear mixed-effects models using S4 classes_ , R package version 0.999999-0, URL `http://CRAN. R-project.org/package=lme4` . 

- Brooks, D. (2011), _The Social Animal: The Hidden Sources of Love, Character, and Achievement_ , New York: Random House. 

19 

_Submission to Journal of Quantitative Analysis in Sports_ 

- Buraimo, B., Forrest, D., and Simmons, R. (2010), “The 12th Man?: Refereeing Bias in English and German Soccer,” _Journal of the Royal Statistical Society Series a-Statistics in Society_ , 173, 431-449. 

- CBS Interactive, Inc. (2012), _CBSSports College Basketball_ , URL `www.cbssports. com/collegebasketball` . 

- Dohmen, T. J. (2008), “The Influence of Social Forces: Evidence from the Behavior of Football Referees,” _Economic Inquiry_ , 46, 411-424. 

- Fehr, E., Bernhard, H., and Rockenbach, B. (2008), ”Egalitarianism in Young Children,” _Nature_ , 454, 1079-U1022. 

- Greer, D. L. (1983), “Spectator Booing and the Home Advantage - a Study of Social-Influence in the Basketball Arena,” _Social Psychology Quarterly_ , 46, 252-261. 

- Moskowitz, T. J. and Wertheim, L. J. (2011), _Scorecasting: The Hidden Influences Behind How Sports Are Played and Games Are Won_ , New York: Crown Publishing Group. 

- Nevill, A. M., Balmer, N. J., and Williams, A. M. (2002), “The Influence of Crowd Noise and Experience Upon Refereeing Decisions in Football,” _Psychology of Sport and Exercise_ , 3, 261-272. 

- Nevill, A. M., and Holder, R. L. (1999), “Home Advantage in Sport - an Overview of Studies on the Advantage of Playing at Home,” _Sports Medicine_ , 28, 221236. 

- Pedowitz, L. B. (2008), _Report to the Board of Governors of the National Basketball Association_ , URL `http://hosted.ap.org/specials/interactives/ _documents/100208nba_pedowitz.pdf` . 

- Plessner, H., and Betsch, T. (2001), “Sequential Effects in Important Referee Decisions: The Case of Penalties in Soccer,” _Journal of Sport & Exercise Psychology_ , 23, 254-259. 

- Price, J., Remer, M., and Stone, D. F. (2009), “Sub-Perfect Game: Profitable Biases of NBA Referees”, forthcoming in _Journal of Economics and Management Strategy_ , URL `http://papers.ssrn.com/sol3/papers.cfm?abstract_` 

20 

Noecker and Roback: The Tendency of NCAA Basketball Officials to Even Out Foul Calls 

`id=1377964` . 

- R Development Core Team (2011), R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. ISBN 3-900051-07-0, URL `http://www.R-project.org` . 

- Schwarz, W. (2011), “Compensating Tendencies in Penalty Kick Decisions of Referees in Professional Football: Evidence from the German Bundesliga 19632006,” _Journal of Sports Sciences_ , 29, 441-447. 

- Sutter, M., and Kocher, M. G. (2004), “Favoritism of Agents - the Case of Referees’ Home Bias,” _Journal of Economic Psychology_ , 25, 461-469. 

- Wallace, B., Cesarini, D., Lichtenstein, P., and Johannesson, M. (2007), “Heritability of ultimatum game responder behavior,” _Proceedings of the National Academy of Sciences_ , 104, 15631-15634. 

21 


