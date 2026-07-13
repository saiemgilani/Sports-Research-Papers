<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2022/2022 - The Racial Imbalance in College Football Coaching - Unknown Authors.pdf -->



# The Racial Imbalance in College Football Coaching 



CMSAC Fall 2022 Reproducible Research Competition 

## Abstract 

<mark>College football has had a race problem since its inception. From issues of team integration to paying student athletes to demographics of the coaching community, race is never far afield from the preeminent issues that permeate the college football landscape. This paper presents a data-driven look at just how inequitable the current racial distribution is in FBS coaching and provides some insights into how this can change.</mark> 

<mark>This project uses regression, community detection, and classification models to show that there are persistent racial imbalances in the ranks of college football coaching. The imbalances are not due to performance but are perpetuated by reliance on connections within the coaching community and potentially exacerbated further by implicit or explicit racial bias. To mitigate these imbalances, significant shifts are needed within the paradigms that govern hires made at the highest level of the sport.</mark> 

## 1. Introduction 

<mark>Coaching jobs at the highest level of college football have become extremely lucrative. It has been widely demonstrated (and confirmed in our initial data exploration) that the racial composition of these coaching jobs does not match the racial composition of the pool of candidates, which primarily consists of lowerlevel coaches or former players. As Ivan Maisel detailed in 2020 [5], the lack of Black coaches at the highest levels of college football may be the aspect of the game that has changed the least in the preceding few decades. Recently, Chris Vannini brought attention to some of the interviewing practices that may help to perpetuate the current situation [11].</mark> 







<mark>Looking back over the past 20 years, the percentage of Black players in college football has continued to grow steadily, while the percentage of Black coaches has failed to keep pace, much less approach the racial distribution of the players themselves.</mark> 

<mark>This project uses data to analyze just how substantive the problem is, to see if the data could point us toward the root causes of the problem, and to provide some ways forward toward more just outcomes in the college football coach hiring process.</mark> 

## 2. Data 

Data for this project comes from three different primary sources. The first is a dataset of coaching staffs from the year 2000 to 2021 provided by Geoff Hutchinson. The data consists of 27,516 observations including 3,740 unique assistant coaches, coordinators, and head coaches across 130 teams at the FBS level. Each coach was tagged by race and by whether they played college football, based on college football team pages and coach biographies. It was determined that 92.7% of FBS coaches since 2000 were former Division 1, 2, or 3 college football players. That is, former college football players comprise the vast majority of the FBS coaching pool. 

The second source of data was NCAA.org [7], from which player demographic data was obtained. The NCAA began collecting this self-reported data from active member schools in 2000. It showed that Black athletes make up 39% of athletes from all levels of college football. Given that 92.7% of FBS coaches come from this pool and given the demographic makeup of the US population to represent the other 7.3%, the expected distribution of the racial makeup of college football coaches can be formulated and compared to the reality. 

The final data source was the Sportsdataverse [2] college football package, cfbfastR [3], which is an API wrapper package around collegefootballdata.com [10]. This data provided season-by-season statistics for each team’s performance over the time period of interest. In particular, EPA and Success Rate were used as the primary net impact metrics because they have been found to be two of the most predictive public performance metrics. EPA is the result of an XGBoost model by the cfbfastR team, and an explanatory primer by Alok Pattani can be found at ESPN.com [9]. An explanation and defense of Success Rate by Bill Connelly can be found at Football Study Hall [1]. 

## 3. Preliminary Analysis 

### 3.1 Candidate Pool Demographics 

The expected racial composition of FBS coaches based on the representative candidate pool is 37% Black and 51% White. Instead, Black coaches make up slightly more than 10% of head coaches and offensive coordinators. Although the racial distribution improves to 18% for defensive coordinators, there are still half as many Black defensive coordinators as would be expected. For a thorough examination of why there are more Black coaches on the defensive side of the ball, see Richard Johnson’s excellent work [4] from 2017 which describes, among other things, how Black players are funneled into positions thought to require less cognitive and leadership abilities. 





### 3.2 Tenure Comparison 

<mark>One of the contributing factors to this difference between reality and expectation is that Black coaches simply have shorter tenures in their positions. B</mark> elow is a basic comparison of the average tenure at different coaching positions by race. 



<mark>Black head coaches and coordinators have shorter tenures on average than their White counterparts. There could be three primary causes for this tenure discrepancy:</mark> 

<mark>1. Black coaches could be promoted sooner.</mark> 

<mark>2. Black coaches could be justifiably fired sooner due to poor performance.</mark> 

<mark>3. Black coaches could be</mark> _<mark>un</mark>_ <mark>justifiably fired sooner.</mark> 

<mark>The first cause would result in shorter tenures for coordinators and longer tenures for head coaches. However, the average discrepancy in the table above is even larger among head coaches than it is among coordinators. Ruling out the first option, analysis of coaching performance is necessary to see if this tenure discrepancy is justifiable based on on-field results.</mark> 

### 3.3 Creation of On-field Improvement Metrics 

<mark>Joining the performance metrics obtained from cfbfastR with the coaching dataset enabled a comparison of metrics during a coach’s tenure with metrics from the preceding years to provide a metric showing net impact on team performance for each coach. The net impact was measured as the overall net change in team performance for head coaches and net change on a particular side of the ball for coordinators.</mark> 

<mark>Overall, the analysis includes seven specific ways of grouping and evaluating the performance of the coaches, which analyze team performance for head coaches, offensive performance for offensive coordinators, defensive performance for defensive coordinators, before and after getting head coaching jobs, grouped by race.</mark> 

## <mark>4. Methodology</mark> 

### 4.1 Regression 

For each of the groupings referenced above, a regression analysis was performed with the net impact metrics as the response variable and the race of the coach as the predictor variable. Prior to fitting the regression model, outlier detection was performed, and residual analysis was used to test the model assumptions. 

### 4.2 Community Detection 

The Louvain algorithm was then employed to help detect the communities that exist within the large network of college football coaching. The Louvain algorithm is a commonly used and relatively computationally efficient unsupervised machine learning algorithm for community detection that aims to create subgroups by maximizing the modularity of the graph [8]. Modularity measures how dense the connections are within subsets of nodes (coaches) by comparing the actual density to the expected density of a random graph. 

The algorithm separated 1,431 coaches into 41 different communities. These networks were used to analyze whether professional connections are contributing to the racial discrepancy in college football coaching. This algorithm provided four different metrics for each coach - “betweenness”, “closeness”, “degree”, and “eigenvector” centrality. Betweenness is a measure of how important one vertex is in connecting other vertices in the graph (a measure this project refers to as “Networking.”). Closeness is a measure of how many edges can be traced back to one vertex (“Influence”). Degree centrality measures the number of direct connections a vertex has (“Connections”). Eigenvector centrality is another measure of influence that emphasizes connections to other highly connected vertices (“InfluencePlus”). 

These metrics were grouped by the race of the coaches to find if there were significant differences revealed by this analysis of coaching communities. Unlike the team performance metrics discussed above, these connection metrics did reveal significant differences between coaches grouped by race. 

### 4.3 Feature Selection 

Finally, the team-based metrics and individual connection-based metrics were combined to create a classification model to attempt to predict which coordinators will be hired as head coaches. If the hiring decisions of the past are repeated going forward, who will be hired in coming years? 

For this part of the project, the years 2015-2021 were used as target years. Then, those 7 years of data were combined into one dataframe with 70% of the data randomly chosen as training data, while the other 30% serves as the test data. A response column called “BecameHC” was created to indicate whether an individual coordinator became a head coach in the target year. In this overall dataset of 2000 coordinator years, 61 of these coordinators became a head coach in the target year. 

This dataset included 11 potential features; the four outputs of the Louvain algorithm, four team net impact statistics, the race of the coach, the tenure length of the coach in years, and whether the coach was an offensive or defensive coach. The correlation was examined between features to see if any multicollinearity existed. As expected, there was some apparent correlation between features. Therefore, Elastic Net regularization was deployed to help with variable selection while accounting for this multicollinearity. This resulted in six recommended features: Connections, Net EPA, Net Passing Success Rate, Race, Tenure, and Role (whether offensive or defensive coordinator). These six features, along with the response “BecameHC”, were used to begin training potential classification models. 

### 4.4 Classification 

Six different types of classification models were tested to assess what type of model would make the best predictions. These included: Logistic Regression, K-Nearest Neighbors, Support Vector MachinesKernel, Adaboost, XGBoost, and Neural Networks. Some of the models included parameter tuning and classification thresholds. With each model, predictions were generated for the BecameHC response and then compared with the actual test responses. 

## 5. Evaluation and Results 

### 5.1 Regression 

The regression analysis does not show any evidence that coaching performance is the root cause of the shorter tenures that Black coaches experience in college football. A representative regression analysis using race as the predictor variable and Net EPA as the outcome variable yields p-values around 0.3, far outside of the statistically significant range, and has an R-Squared value of 0.0093, meaning that race accounts for less than 1% of the variance seen in head-coaching performance. A regression for defensive coordinators who became head coaches produces nearly identical p-values and an R-squared value of 0.013 when using race as the predictor and Net Defensive EPA as the outcome variable. 

The other results are similar. In all seven cases outlined in the methodology section, the data shows that the race of the coach has no statistical significance in determining improvement of on-field performance. What does that tell us? Performance is not the underlying reason for the racial discrepancy of coaching hires and tenure lengths at the FBS level. Equally competent Black coaches are unjustifiably being hired less frequently and fired sooner than their White counterparts. 

### 5.2 Community Detection 

<mark>On the other hand, race does significantly correlate with the level of connection that a coach has. Using the Louvain algorithm to analyze the degree centrality of the coaching community revealed that White coaches have 43% more connections than Black coaches do. More stunning is that White coaches are seven times more influential than Black coaches on average. Further, it is apparent that the vast majority of head coaches with the most Connections have hired a below-average number of coordinators of color. This can be seen in the table below [6], which includes the top 20 head coaches in terms of Connections. Only 3 of these 20 coaches have been shown to hire coordinators of color at an above-average rate and tenure-length.</mark> 





<mark>In fact, Non-white head coaches employ Non-white coordinators 30% more frequently than do their White counterparts. Unfortunately, this perpetuates a cycle leading to homogenous coaching community subgroups like the one shown below, which was created from the Louvain machine learning model.</mark> 





### 5.3 Feature Selection 

<mark>The six significant features selected using Elastic Net were Connections, Net EPA, Net Passing Success Rate, Race, Tenure, and Role. Based on how the Race categorical variable was encoded, the negative coefficient indicated that Black coordinators are less likely to become head coaches than White coordinators. The Role feature indicated that being a defensive coordinator was negatively predictive of becoming a head coach, which was especially interesting for our research considering that Black coaches are about twice as likely to become defensive coordinators as offensive coordinators.</mark> 

<mark>Further, Connections significantly influenced who became a head coach, and as mentioned above, White Coaches had 43% more connections on average than Black coaches in our dataset. The two impact metrics included here, Net EPA and Net Passing Success Rate, did not have statistically significant differences between coaches of different races. Thus, the importance of Connections, Role, and Race in selecting which coordinators will become head coaches perpetuates the racialized gap in college football head coaching.</mark> 

### 5.4 Classification 

<mark>After selecting variables, six different classification models were fitted and tuned, as described above. Because the number of coaches in the dataset who actually became head coaches was relatively small, simply using accuracy or misclassification rate for the predictions was not the best tool for evaluating the models. A model that predicted no one to become a head coach would have achieved an accuracy of around 96%. Thus, the more indicative result was whether or not the coordinators became head coaches who were predicted to become head coaches by the model.</mark> 

<mark>The test dataset included 21 coaches who actually became head coaches in the target year. One interesting result is that many of the predictions the classification models made did not necessarily happen in the target year, but many of the predicted head coach hires did eventually become head coaches. That information is included in the model comparison below.</mark> 





<mark>The K-Nearest Neighbors model proved to be the best at identifying coaches who would be hired in the target year, as 15.8% of that model’s predictions were correct in our test dataset. However, the SVM model with the laplacian kernel was the most accurate at identifying coaches who would eventually become head coaches, as 82% of the identified coaches from the test dataset would become head coaches in future years. Perhaps, this reveals that head coaching candidates may become appealing rather quickly, but decision makers can be slow to recognize these candidates. This would be a good subject for further research.</mark> 

<mark>For future predictions, the two models identified above were chosen to run on the most recent data to see which coordinators are identified as the most likely future head coaching hires. The SVM model gave two predictions: Bill O’Brien and Jeff Grimes. The KNN model gave ten predictions. Of note, all twelve</mark> 

<mark>predictions between the two models were White. However, looking simply at the performance-based metrics identified as significant revealed that three of the top twelve candidates are Black. Clearly, the hiring practices that rely to some degree on Race, Connections, and Role heavily influenced the candidate pool away from simply those coordinators with the best proven track records of performance improvement.</mark> 

## 6. Discussion 

<mark>Our forward-looking predictions indicate that the racial imbalance is likely to continue, as the twelve predictions made by our models for future hires are all White. If those in position to influence the hiring of college football coaches are to substantially change the current imbalance in the rank of college football coaches, they must increasingly emphasize performance-based qualifications.</mark> 

<mark>Specifically, we suggest five coordinators who should be strongly considered for FBS head coaching jobs in the coming cycle. Brain Norwood is currently the Assistant Head Coach at UCLA and has past stints as Defensive Coordinator at Navy, Kansas State, Tulsa, and Baylor. Josh Gattis is the new Offensive Coordinator at Miami and has already excelled as Offensive Coordinator at Michigan and Alabama. Newland Isaac is the Co-Offensive Coordinator at Coastal Carolina, and he has helped to oversee the offensive explosion for the Chanticleers after serving as Offensive Coordinator at Albany State. Alex Atkins is the newly promoted Offensive Coordinator at Florida State, and he has past impressive tenures as OL coach at FSU and OC at Charlotte. Finally, Maurice Harris is the OC for Liberty and has previously served as Tight Ends coach at both Ole Miss and Arkansas State.</mark> 

<mark>These five coaches have all produced net gains in EPA and success rate on their respective sides of the ball that far outpace an average coordinator’s impact. These would be five more Black head coaches and five more coaches who are more likely to hire Non-White coordinators. In a recent Sports Illustrated article, Richard Johnson identifies two of the same Black coordinators as key candidates in the upcoming hiring cycle [12].</mark> 

<mark>This would simply be a first step toward closing the gap between the current racial make-up of college football coaches and the racial make-up of the candidate pool. The figure below illustrates just how much change would be necessary for the actual distribution to match the expectation. Thirty-five more Black head coaches are needed in the FBS for the coaching ranks to match the hiring pool.</mark> 





## 7. Conclusion 

<mark>Through regression analysis, community detection, and feature selection, evidence was compounded that there is racial discrimination present in the hiring practices for college football coaches. There is no statistical difference in team performance based on the race of the coaches, but there is statistical difference in the community connections held by coaches of different races. Feature Selection reveals that race itself is a predictor of future hires, as Black coaches are less likely to be hired while holding all other features equal. Additionally, the importance of connections and role exacerbate the discrimination against Black coordinators seeking to become head coaches.</mark> 

<mark>The gap between the percentage of Black players and Black coaches is higher than it was in 2000. Black head coaches get 1.5 fewer years than their White counterparts.</mark> 

<mark>The imbalance is not based on differences in performance. However, the hiring of head coaches and coordinators is largely based on social networks. White coaches are 43% more connected than Black coaches. Non-White coaches hire 30% more Non-White coordinators, but most of the opportunities to hire go to White coaches. The 20 head coaches who have employed the smallest percentage of NonWhite Coordinators are White; the 19 most influential head coaches are White, but only 4 of them are above average in hiring Non-White coordinators. White head coaches have more connections, and they hire more White coaches.</mark> 

<mark>The racial imbalance in college football coaching is real and persistent. But this imbalance does not have to be a permanent fixture. It can be mitigated with intentionality. Coaches with significant influence can do their part. One new Black head coach can have ripple effects for years at multiple schools. There are promising candidates of color who could and should get hired in the next cycle. It’s time to act.</mark> 

## 8. Acknowledgements 

This paper is being submitted in memory of Geoff Hutchinson. In addition to creating the dataset of college football coaches used for this analysis, he was an active contributor to the Sportsdataverse and the author of the wehoop package for working with women’s college and professional basketball data in R. More importantly he was a fun, loyal, and loving member of his community in Brooklyn, at Vanderbilt University, and in the digital sports analytics community around the world. 

## 9. References 

[1] Connelly, Bill. “In Defense of Success Rates.” _Football Study Hall_ , Vox Media, LLC, 16 Feb. 2012, <u>https://www.footballstudyhall.com/2012/2/16/2798555/in-defense-of-success-rates.</u> 

[2] Gilani, Saiem. “Sportsdataverse.” _SDV_ , 2021, <u>https://sportsdataverse.org/.</u> 

[3] Gilani, Saiem, et al. “cfbfastR Data and Tools for College Football.” _CfbfastR_ , Sportsdataverse, <u>https://cfbfastr.sportsdataverse.org/.</u> 

[4] Johnson, Richard. “Football's Lack of Black Head Coaches Is the Result of a Flawed Pipeline.” _Banner Society_ , Vox Media, LLC, 9 Aug. 2017, <u>https://www.bannersociety.com/2017/8/9/20726457/black-head-coaches.</u> 

[5] Maisel, Ivan. “The Lack of Black college football coaches is still glaring, and so are the excuses behind It.” _ESPN_ , 3 Dec. 2020, https://www.espn.com/college-football/story/_/id/30435797/the-lack- <u>black-college-football-coaches-glaring-the-excuses-it.</u> 

[6] Mock, Thomas. “Functions and Themes for Gt Tables.” _The MockUp_ , 28 Sept. 2020, <u>https://themockup.blog/posts/2020-09-26-functions-and-themes-for-gt-tables/.</u> 

[7] “NCAA Demographics Database.” _NCAA.org_ , <u>https://www.ncaa.org/sports/2018/12/13/ncaademographics-database.aspx.</u> 

[8] McNulty, Keith. _Handbook of Graphs and Networks in People Analytics: With Examples in R and Python_ . CRC Press, 2022. 

[9] Pattani, Alok. “Expected Points and EPA Explained.” _ESPN_ , 15 Sept. 2012, https://www.espn.com/nfl/story/_/id/8379024/nfl-explaining-expected-points-metric. 

[10] Radjewski, Bill. “College Football Data.” _CollegeFootballData.com_ , 2022, <u>https://collegefootballdata.com/.</u> 

[11] Vannini, Chris. “After Brian Flores' NFL Lawsuit, Black College Football Coaches Reflect on Interview Experiences and What Must Change.” _The Athletic_ , 2 Mar. 2022, <u>https://theathletic.com/3157462/2022/03/02/after-brian-flores-nfl-lawsuit-black-college-football-coachesreflect-on-interview-experiences-and-what-must-change/?article_source=search.</u> 

[12] Johnson, Richard. “The Black Coaches Who Should Be on Decision-Makers’ Radars This College Football Season.” _Sports illustrated_ , 23 August 2022, https://www.si.com/college/2022/08/23/college- <u>football-season-preview-2022-black-coaches-on-industry-radar.</u> 


