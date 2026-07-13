<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2024/2024 - Modelling Team Play Style Using Tracking Data to Evaluate the Effectiveness of Variance in Tactical Behaviour - Unknown Authors.pdf -->



# **Modelling Team Play Style Using Tracking Data to Evaluate the Effectiveness of Variance in Tactical Behaviour** 

Michael Gleeson | University College Dublin 

## **Defining Team Play Style** 

Team play style is one of the most important factors in the success of a football team. At an elite level,the difference between obtaining European Football and missing out, or relegation and safety, can come down to a single point, so how a team defends, passes, and creates goal-scoring opportunities is crucial in gaining as many points as possible – meaning the role of team Head Coach is arguably the most important in football. A cliché among football pundits is “the best teams donʼt have a plan B, they just make plan A betterˮ<sup>1</sup> , and so my analysis of team play style uses tracking and event data to determine how each team plays their own style of football introspectively, to gain an understanding of the number of the ‘plansʼ each team possesses. 

### **1.1 Variables Utilised** 

A mixture of both tracking and event data were used in my modelling for team play style, containing: 

- Basic variables such as passes completed per possession, pass accuracy, etc., 

- Advanced metrics, including xG, net-On the Ball Value OBV, and expected pass completion, 

- Geometric variables, such as Balance Score, which measures the numerical superiority of teams, both in attack and defense. 

Within my analysis, I have tried to mitigate team strength bias as much as possible. For instance, instead of computing xG per team, I used xG per shot as a measure of the quality of shooting for each team. 

### **1.2 Determining Subsections within the Data to Analyse** 

To analyse the data more effectively, each match was subsectioned based on time and game-state. The opening 25 minutes of each match was classified as the “Earlyˮ period of the match, the two “Interimˮ periods of the match ranged from 25 minutes to 75 minutes, with the final 15 minutes with the addition of added time defined as the “Lateˮ 

> 1 Sharland, P. 2017, July 26. _Jurgen Klopp: The talk of a Plan B 'shows a lack of understanding'_ . tntsports.co.uk. https://www.tntsports.co.uk/football/premier-league/20172018/jurgen-klopp-the-talk-of-a-plan-b -shows-a-lack-of-understanding_sto6267115/story.shtml 

**1** 



period of the match. Each period was appended with a “Game-Stateˮ variable (“Winningˮ, “Drawˮ, “Losingˮ), and a “Contextˮ column, which included the Game-State of the previous period. 

In the following table, Team A conceded and were losing in the middle of Match 3, but recovered to draw in the “Lateˮ period. In Match 4, they took an early lead. 

|||**Table 1**<br>|||
|---|---|---|---|---|
|**Match_ID**|**Variable_1**|**Period**|**Game_State**|**Context**|
|3|X1|Interim|Losing|Draw|
|3|X2|Interim|Losing|Losing|
|3|X3|Late|Draw|Losing|
|4|X4|Early|Winning|Match Start|
|4|X5|Interim|Winning|Winning|



## **Using Gowerʼs Distance to Analyse Dissimilarity in Play Style** 

The variables used in this analysis were of categorical and numerical nature. Some numerical values ranged between 0 and 1, others ranged between 1000 and 3000. To analyse this mixed data, I implemented Gowerʼs Distance<sup>2</sup> . 

For Gowerʼs Distance, the Similarity 𝑆 is defined as: 



The weights 𝑤 are set to 1 in my analysis, as no variable is given greater importance 𝑖𝑗𝑘 over another. If the variable is binary, the value of 𝑠 is either 1 or 0. If the variable is 𝑖𝑗𝑘 continuous, 𝑠𝑖𝑗𝑘 = 1 − <u>|𝑥𝑖𝑅−𝑥𝑘 𝑗|</u> ~~,~~ where 𝑅𝑘 is the range of the 𝑘𝑡ℎ variable. 𝑠𝑖𝑗𝑘 always ranges between 0 and 1, with values closer to 0 representing more similar objects, and values closer to 1 representing less similar objects. 

> 2 Gower, J. C. 1971. A General Coefficient of Similarity and Some of Its Properties. _Biometrics_ , _27_ 4, 857871. https://doi.org/10.2307/2528823 

**2** 



I applied Gowerʼs Distance to my model of team play style to assess the dissimilarity in individual teamʼs play style between matches, obtaining a distance matrix within which can identify matches where play style was significantly dissimilar. The matrix below shows an example of how Gowerʼs Distance is used to create a dissimilarity matrix. As distances are pairwise, 𝑆 and 𝑆 are equal. 𝑖𝑗 𝑗𝑖 

|||**Table 2**<br>||
|---|---|---|---|
|**MATCH_ID**|**1**|**2**|**3**|
|**1**|0|𝑆12|𝑆13|
|**2**|𝑆21|0|𝑆23|
|**3**|𝑆31|𝑆32|0|



Using this matrix, one can identify large dissimilarities through graphical and numerical methods. 

### **2.1 Average Variance** 

To quickly identify which teams vary more than others, I computed the mean variance for team ‘ _v_ ʼ for each dissimilarity matrix based on time period ‘ _t_ ʼ. 



<!-- Start of picture text -->
𝑛<br>∑ 𝑠<br>𝑖𝑗<br>𝑖=1,𝑗=1<br>=<br>𝑆<br>𝑣,𝑡 𝑛<br><!-- End of picture text -->



**3** 



Computing the mean variance for each team, and each match period, in the data can provide us with a very rough idea of which teams vary their play style more than others. From the bar chart above, one can see how variation in team play style differs over time. Red represents the first 25 minutes, Green represents 2550 minutes, Blue from 5075, and Purple from 75. 

Immediately, the limitations are clear: there is a possibility of team-strength bias within the data – the stronger teams will always have more shots, passes, and actions than weaker teams. Itʼs notable that the stronger teams also have more variance during the opening minutes of the match than the final minutes; this could be due to a game-state effect, and would be interesting to research further. 

Another limitation to note when analysing play style is manager bias. A lot of these teams, such as Chelsea, had multiple managers over the two seasons of data, which requires addressing during this analysis. 

### **2.2 Dissimilarity Matrices** 



In the image to the left, a graph can be seen representing the dissimilarity between the first 25 minutes of matches, specifically in this instance for the opening nine games of Tottenham Hotspurʼs 22/23 season. The more dissimilar two objects, the stronger the edges – in this instance, Spursʼ play style in the opening 25 minutes of matches 245 and 275 were noticeably dissimilar to matches 312 and 308 respectively. 

|||**Table 3**<br>||||
|---|---|---|---|---|---|
|**Match_ID**|**Match**|**Forward Pass per**<br>**Possession %**|**Defensive**<br>**Third xPC**|**Aerial**<br>**Pass %**|**Game-State**|
|245|Chelsea A|45%|86%|11%|Losing|
|275|West Ham A|49%|91%|10%|Draw|
|308|Leicester H|56%|77%|35%|Winning|
|312|Arsenal A|60%|75%|33%|Losing|



**4** 



Table 3 gives a snippet of information on the play Style of Spurs during the opening minutes of their matches against Chelsea, West Ham, Leicester and Arsenal. Itʼs quite clear to see, even from only a few variables, that there is a noticeable difference in play style between these matches. The match which Spurs were expected to win was Leicester H, and their play style reflects this: on average, 56% of their passes during a given possession were forward, and their average Expected Pass Completion (xPC) was 77%, indicating positive, proactive play. Compare this to West Ham A, where around half of their passes were backwards, and they were much more risk-averse in their defensive third. 

The two most interesting fixtures to compare are Chelsea Aand Arsenal A. Both London derbies, Spurs played with high dissimilarity between the two. Against Chelsea, the stats suggest they were quite negative, playing the majority of passes backwards and with high probability of completing the pass. Against Arsenal, they played 60% of their passes forward, and a third of their passes in the air. This apparent change in play style did not have an effect on the score of the game after 25 minutes, but it raises questions as to when changes in play style can positively, or negatively, affect outcomes. 

### **2.2.1 Teamsʼ Approach to Derbies** 





Spursʼ approach to their first fixture vs. Arsenal in the 22/23 was clearly an outlier – their strategies in the following games were very different. As seen in the image to the left, the match 312 Arsenal A, 22/23 varied the most in play style compared to the other matches. As seen in Table 4, there isnʼt a clear pattern as to how Spurs approached these derby games. This can be explained for many reasons, most notably that of Spursʼ change in manager<sup>3</sup> . Antonio Conte was head coach during the 22/23 season, while Ange 

Postecoglou was head coach during the 23/24 season. Comparing the respective home and away fixtures, a clear change in approach can be seen: Postecoglou played fewer aerial passes, more safer passes, and more forward passes per possession than Conte. Again, itʼs unclear whether these tactical differences and dissimilarities brought about any tangible change in results. 

> 3 Pogrund, A. 2024, April 9. _Tottenham: Eric Dier explains how Ange Postecoglou differs from Antonio Conte and Jose Mourinho_ . standard.co.uk. 

> https://www.standard.co.uk/sport/football/tottenham-dier-postecoglou-conte-mourinho-b1150276. html 

**5** 



|||**Table**<br>|**4**<br>|||
|---|---|---|---|---|---|
|**Match_ID**|**Match**|**Forward Pass per**<br>**Possession %**|**Defensive**<br>**Third xPC**|**Aerial Pass %**|**Game-St**<br>**ate**|
|312|Arsenal A<br>22/23|60%|75%|33|Losing|
|421|Arsenal H<br>22/23|43%|83%|22|Losing|
|805|Arsenal A<br>23/24|64%|89%|9|Draw|
|101|Arsenal H<br>23/24|50%|86%|14|Losing|



### **2.3 Between-Team Analysis** 

Gowerʼs Distance can also be used to analyse how differently teams play in given situations. For this, I looked at the dissimilarities in team play style when playing Chelsea Away, and Spurs Away. 









The above images show Dissimilarity Histograms for team play style against Chelsea A and Spurs Arespectively. Visually, one can see that the dissimilarity among team play style against Chelsea is much more spread out than that for teams against Spurs. In numeric terms, the dissimilarity mean of team play style against Spurs is 0.18, while against Chelsea it is 0.21. I used hypothesis testing to determine if the difference in means is statistically significant. 

**6** 



Using a Welch Two Sample t-test<sup>4</sup> , the following formula can be used to test whether or not the true difference in means is equal to zero: 



Computing this, I obtained a t statistic of 13.206 and a p-value ≈ 0. Thus, the null hypothesis that the true difference in means is equal to 0 is rejected. 





Dissimilarities in team play style against Chelsea and Spurs can also be analysed through boxplots. In the above graphs, one can firstly recognise that dissimilarity among play styles is higher within teams that play against Chelsea in comparison to teams playing against Spurs. Secondly, it can be seen that for those teams who win away at Spurs and Chelsea, mean rolling dissimilarity is higher. The sample size is too small for us to form any concrete conclusions, but with more data and further analysis, this could potentially be proven. 

## **Analysing Variance in Tactical Behaviour** 

By using Gowerʼs Distance, hierarchical clustering can be used to classify different play styles of teams into factors which can be analysed. Once clustered, the original dataframe can be reevaluated using clustering results, to further analyse team play style. After much testing, I found four clusters to produce the most accurate and interpretable results. 

By segmenting the data in this way, it can be seen which teams “made plan A betterˮ, and which teams were comfortable in varying their play style. 

> 4 Graeme D. Ruxton, The unequal variance _t_ -test is an underused alternative to Student's _t_ -test and the Mann–Whitney _U_ test, _Behavioral Ecology_ , Volume 17, Issue 4, July/August 2006, Pages 688690, <u>https://doi.org/10.1093/beheco/ark016</u> 

**7** 



### **3.1 Hierarchical Clustering** 

To identify clusters which could be analysed as play styles, I used Wardʼs Method of clustering<sup>5</sup> . Based on the dissimilarity matrix created using Gowerʼs distance, I used 2 2 Wardʼs Method to define clusters based on the maximisation of 𝑟 , where 𝑟 represents “the proportion of variation explained by a particular clustering of the observationsˮ<sup>6</sup> , or: 



Hierarchical clustering can be visualised in the form of a dendrogram, seen in the image to the right. Visualising the graph as a tree, four distinct branches can be seen, colour coded for increased clarity (the diagram is only for demonstration purposes). The closer two observations are within branches, the more similar they are. From the graph, these matches could be separated into three or four clusters. Using the cutree() function in R<sup>7</sup> , one can decide how many clusters to segment the data into. From the explanatory diagram, it seems that four would be the ideal number of clusters for this data. 





> 5 Ward, J.H. 1963. Hierarchical Grouping to Optimize an Objective Function. _Journal of the American Statistical Association, 58_ , 236244. 

> 6 Eberly College of Science, P. S. 2014. _Applied Multivariate Statistical Analysis 14.7 - Ward's Method_ . Online.Stat.psu.edu. https://online.stat.psu.edu/stat505/lesson/14/14.7 

> 7 R. _Cutree: Cut a Tree into Groups of Data_ . Rdocumentation.org. 

> https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/cutree 

**8** 



### **3.2 Analysing Clusters – Within Teams** 

|||**Table 5**<br>**Brentford**|||
|---|---|---|---|---|
|**Variable**|**Cluster 1**<br>**Positive)**|**Cluster 2**<br>**Direct**|**Cluster 3**<br>**Passive)**|**Cluster 4**<br>**Balanced)**|
|Mean Aerial Pass %|17.5%|53.5%|29%|32.9%|
|Mean xG per Shot|0.083|0.154|0.058|0.103|
|Mean Forward Pass<br>% per Possession|52.9%|59.8%|46.1%|50.7%|



The above table gives some indication as to how play style differed among clusters for Brentford. In particular, “Cluster 2ˮ has a much higher Aerial Pass % mean than the other clusters, as well as a higher Mean xG per Shot, and a higher Mean Forward Pass % per possession (the percentage of completed passes that were forward per possession). 











As seen in the above bar charts, Brighton and Brentford, two teams with similar results within the two seasons of the data, had differing clustering situations. During the 5075<sup>th</sup> minute periods of matches, over half of Brentfordʼs matches were classified into cluster ‘3ʼ, while Brightonʼs were much more evenly distributed. Please note that the clustering numbers for each team, while they overlap, are independent of each other i.e: “Cluster 3ˮ for Brentford could have very different variables compared to Brightonʼs “Cluster 3ˮ. Analysing each season in the data individually returns some interesting results. 

**9** 











Both Brentford and Brighton recorded historical seasons during the 22/23 season: Brighton finished 6<sup>th</sup> , achieving Europa League football, while Brentford finished 9<sup>th</sup> , their highest ever Premier League finish. Brentfordʼs play style was clustered highly in ‘3ʼ, but apart from that their play style was broadly varied, as was Brightonʼs. 









In 23/24, both teams lost key players. Brentfordʼs captain Ivan Toney was suspended for the first half of the season, and Brighton sold their key midfield partnership of Moises Caicedo and Alexis Mac Allister<sup>8</sup> . Neither team signed a like-for-like replacement for any of these key players, and it showed. Both finished in the lower half of the table, and their variance in play style had a much higher concentration in two clusters. Thomas Frank, 

> 8 Barbadikar, N. 2023, August 10. _Brilliant Brighton: The Seagull's Recruitment Strategy Explained_ . Analyticsfc.co.uk. 

https://analyticsfc.co.uk/blog/2023/08/10/brilliant-brighton-the-seagulls-recruitment-strategy-expl ained/ 

**10** 



manager of Brentford, has spoken before about his teamʼs approach to “Plan Bˮ<sup>9</sup> , which they seemed to employ a lot more during this season, rather than a varied approach to team play style. Brighton, losing such quality in midfield, started to play fewer risky passes in midfield and more passes per possession. This wasnʼt the sole cause for their poorer league position, but it seems that when teams have the quality to vary their play style, they are more than happy to do so, and very successful in that approach. When they have less player quality, they are less likely to vary their play style. To prove these statements, more analysis and data is required. 

The dropoff in frequency of “Cluster 2ˮ from the 22/23 season to the 23/24 season could be a direct correlation to Ivan Toneyʼs suspension. The 6ʼ4ˮ striker was a remarkable option in the air, and his absence significantly impacted Brentfordʼs results, both from his quality and his presence as an alternative for build up play. 

## **The Effectiveness of Varying Play Style** 

To assess the effectiveness of variance within team play style, Game Theory can be used to determine where and when teams gain an advantage from variation in Tactical Behaviour. Unfortunately, the data does not have too many matches which can be analysed in specific situations: these results only suggest possibly successful strategies for teams – these are not indications of certainty in results. 

### **4.1 Game Theory – Points Won in Final Minutes** 

Treating football matches as simultaneous games<sup>10</sup> , where both teams are making moves at the same time, probabilities of winning, losing, and drawing can be caluclated, given that the team in question are drawing with fifteen minutes left to go in a match. This game can be represented in matrix form, where each square of the matrix indicates the payoffs of the **home team** and the **away team** (points won/lost from a drawing position). 

> 9 Brentford FC 2023, February 18. _Frank: We need to cherish these moments_ . Brentfordfc.com. https://www.brentfordfc.com/en/news/video/thomas-frank-interview-brentford-1-crystal-palace-1 premier-league 

> 10 Policonomics 2017, January 1. _Game theory IISimultaneous games_ . Policonomics.com. https://policonomics.com/lp-game-theory2-simultaneous-game/ 

**11** 



|||Away|Team|
|---|---|---|---|
||3837317|**D**|**S**|
|Home|**D**|(**0.33, 0.22**)|(**0.11,0.11**)|
|Team|**S**|(**0.86, 0.43**)|(**0.31, 0.06**)|



**_Figure 12Simultaneous Game Given that teams were drawing at 75 minutes played)_** 

A team playing Dissimilarly Dindicates that the dissimilarity between play styles during the 5075 minute period and the 75minute period are above the average computed, and a team playing Similarly Srepresents a dissimilarity between play styles below the average. 

Using Game Theory, a dominant strategy can be obtained for this game. As Sstrictly dominates Dfor both the Away Team and the Home Team, the NE is S,S, with payoffs 0.31, 0.06. These payoffs represent the points gained/lost per match. For the away team in the above game, their only chance to win points is if they do not change play style majorly in the final fifteen minutes. There are quite obvious limitations within this game: 

- 1 The data contains five of the traditional “Top 6ˮ, and their strength in comparison to the other teams creates bias within the game, 

- 2The data does not contain a lot of samples to analyse. 

Taking these limitations into account, these clusters can be further analysed, and it can be determined how teams playing similarly/dissimilarly can have an effect on a given matchʼs outcome. 

|||**Clust**<br>|**ers**<br>||
|---|---|---|---|---|
||**1**|**2**|**3**|**4**|
|**Mean Forward**<br>**Pass %**|53.8<br>%|53.6%|53.2%|41%|
|**Cluster**<br>**Mean Aerial Pass %**|29.4%|17.4%|11.5%|55%|
|**Variables**<br>**Mean xG per Shot**|0.11|0.12|0.09|0.10|
|**Mean Attacking**<br>**Balance Score**|2.07|1.99|2.09|2.05|



**12** 



To investigate the variation between clusters, the previous table gives some information on how these clusters differ from one another. For some variables, such as Mean xG per Shot, the differences are very small. However, for Mean Aerial Pass %, Cluster 1 and 4 are noticeably different to Cluster 2 and 3. The Mean Attacking Balance Score represents, in an attacking scenario, how many attackers the team has compared to how many opposition players are defending. Using this table for reference, one can look at how frequently these clusters appear within the data, given that the team is drawing at the 75th minute of the match. 

|||50<br>Fre<br>**1**|75 Minu<br>quency<br>**2**|te Clust<br>Within D<br>**3**|ers<br>ata)<br>**4**|
|---|---|---|---|---|---|
||**1**|36|20|15|6|
|75Minute<br>Clusters|**2**|12|8|3|2|
|Frequency Within<br>Data)|**3**|5|10|6|6|
||**4**|27|2|5|16|



Studying the frequency of pairings of clusters between the 5075 minute and 75minute periods of matches in the data, itʼs clear that Clusters 1 and 4 are the most frequently observed. This information can be used to identify which pairs of clusters return positive, or negative, outcomes. 

|||5<br>**1**|075 Minu<br>**2**|te Cluste<br>**3**|rs<br>**4**|
|---|---|---|---|---|---|
||**1**|0.25|0.65|0.73|0.33|
|75Minute|**2**|0.25|0.625|1|0|
|Clusters|**3**|0|1.2|0.71|0|
||**4**|0.22|0|0.2|0.3125|



The above table represents the points gained per match within each cluster pairing. Most notably, Cluster 4 High Mean Aerial Pass %, Low Mean Forward Pass%returned the worst outcomes, especially when this cluster was identified in both the 5075th minute 

**13** 



and 75minute periods. Clusters 2 and 3 were very successful, however this cannot be - taken as a credible result there isnʼt enough data to suggest that these play styles are more successful than other clusters. 

Considering the effectiveness of varying tactical behaviour, pairings can be examined where the cluster in the 75minute period differs from that of the 5075 minute period. In these scenarios, variation seems to have a positive correlation with match outcome. Of course, these claims cannot be proven within this project due to the low sample size, but with more data this could be examined further to identify if a causal relationship does exist between varying play style and match outcome. My research indicates that a relationship might exist, but overall it is inconclusive. 

## **Conclusion** 

Of course, there are simply too many variables to consider to ascertain a model that indicates what the correct decision to make is at the correct time. My analysis of clustering play style indicates that variance within play styles could have a positive correlation with positive match outcomes, however, my model would need more data and more research to prove such a relationship exists. 

When tactical clustering was analysed for Brighton and Brentford, it was clear that when they lost players of high quality, they varied tactical behaviour less. Brentford, in contrast to Brighton, were expected to face difficulty in staying in the league after losing Ivan Toney, yet they stayed up. It would be very interesting to include teams that ended up in relegation places in this project, to compare whether or not variance in play style would have resulted in safety, or if variance was one of the reasons for their relegation. 

This project, unfortunately, cannot predict when would be the time to vary tactics, or identify the situation where variance would hamper performance. That, however, was never the aim of the project – thatʼs for coaches and players to decide. So many factors couldnʼt be included in this project that would influence the variance in how teams play. Most notably of all, reputation. Fabius Maximus, dictator of Rome during a war against Hannibal of Carthage, deployed the first recorded military policy of guerilla warfare. While his military policies were successful, his seemingly passive methods were criticized by Rome, and he was replaced by more aggressive military commanders, leading to disastrous losses<sup>11</sup> . Sometimes, the most appropriate tactic doesnʼt lead to the expected – outcome it could lead to career suicide by a manager. While selfish and unwise, less variance in playing style can be respected by fans and owners as not shying away from challenge – even if it leads to worse outcomes. 

> 11 Hunt, P. 2024, March 1. Quintus Fabius Maximus Verrucosus. Encyclopedia Britannica. https://www.britannica.com/biography/Quintus-Fabius-Maximus-Verrucosus 

**14** 



## **References** 

1Sharland, P. 2017, July 26. _Jurgen Klopp: The talk of a Plan B 'shows a lack of understanding'_ . tntsports.co.uk. -  - - - - - <u>https://www.tntsports.co.uk/football/premier league/2017 2018/jurgen klopp the talk of</u> - - - - - - - <u>a plan b shows a lack of understanding_sto6267115/story.shtml</u> 

2Gower, J. C. 1971. A General Coefficient of Similarity and Some of Its Properties. _Biometrics_ , _27_ 4, 857871. https://doi.org/10.2307/2528823 

3Pogrund, A. 2024, April 9. _Tottenham: Eric Dier explains how Ange Postecoglou differs from Antonio Conte and Jose Mourinho_ . standard.co.uk. - - - - - <u>https://www.standard.co.uk/sport/football/tottenham dier postecoglou conte mourinho</u> 

<u>b1150276.html</u> 

4Graeme D. Ruxton, The unequal variance _t_ -test is an underused alternative to Student's _t_ -test and the Mann–Whitney _U_ test, _Behavioral Ecology_ , Volume 17, Issue 4, July/August 2006, Pages 688690, <u>https://doi.org/10.1093/beheco/ark016</u> 

5Ward, J.H. 1963. Hierarchical Grouping to Optimize an Objective Function. _Journal of the American Statistical Association, 58_ , 236244. 

6Eberly College of Science, P. S. 2014. _Applied Multivariate Statistical Analysis 14.7 - Ward's Method_ . Online.Stat.psu.edu. <u>https://online.stat.psu.edu/stat505/lesson/14/14.7</u> 7 R. _Cutree: Cut a Tree into Groups of Data_ . Rdocumentation.org. <u>https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/cutree</u> 

8 Barbadikar, N. 2023, August 10. _Brilliant Brighton: The Seagull's Recruitment Strategy Explained_ . Analyticsfc.co.uk. <u>https://analyticsfc.co.uk/blog/2023/08/10/brilliant-brighton-the-seagulls-recruitment-strategy-expl ained/</u> 

9 Brentford FC 2023, February 18. _Frank: We need to cherish these moments_ . Brentfordfc.com. <u>https://www.brentfordfc.com/en/news/video/thomas-frank-interview-brentford-1-crystalpalace-1-premier-league</u> 

10 Policonomics 2017, January 1. _Game theory IISimultaneous games_ . Policonomics.com. <u>https://policonomics.com/lp-game-theory2-simultaneous-game/</u> 

11 Hunt, P. 2024, March 1. Quintus Fabius Maximus Verrucosus. Encyclopedia - - - Britannica. https://www.britannica.com/biography/Quintus <u>Fabius Maximus Verrucosus</u> 

## **Bibliography** 

- I. Goes-Smit, Floris & Kempe, Matthias & Norel, J & Lemmink, Koen A.P.M.. 2021. Modelling team performance in soccer using tactical features derived from position tracking data. IMA Journal of Management Mathematics. 32. 115. 10.1093/imaman/dpab006. 

- II. Shaw, L., & Glickman, M.E. 2019. Dynamic analysis of team strategy in professional football. 

**15** 



## **Appendix** 

- Expected Pass Completion: The probability of a pass being completed (received by a teammate). 

- On-the-Ball-Value (OBV): The change in probability of a team scoring (or conceding) as a result of an event anywhere on the pitch. 

- xG: The probability of a shot resulting in a goal, based on historical data of shots with similar characteristics. 

## **Variables Used to Cluster Team Play Style** 

- Centralisation: 

   - The highest percentage of possessions in which a player made at least one pass. 

- Average Pass Length 

- Location of Opposition Entries into Final Third: 

   - The location from which opposition players entered the teamʼs defensive third. 

- Aerial Pass % 

- Expected Pass Completion(xPc) in the Defensive Third 

- Passes in the Final Third with End Location in the Penalty Area % 

   - Given a number of passes made within the final third, the percentage of passes which had an end location in the penalty area. 

- Involvement of Midfielders per Possession: 

   - The percentage of possessions in which midfielders made at least one pass. 

- Average Net On-the-Ball-Value OBVper event 

- Concentration of Passes Made within Defensive Third within Given Clusters: 

   - Given a number of passes made within the defensive third, the concentration of passes within clusters of passing sequences. 

- Concentration of Passes Made within Middle Third within Given Clusters 

- Forward Passes % per Possession 

- Expected Goals (xG) per Shot: 

   - The expectation of a goal per shot. 

- Defensive Balance Score: 

   - The number of a teamʼs players defending vs. the number of opposition playerʼs attacking per attacking scenario. 

- Attacking Balance Score 

- xPc in Middle Third 

- Involvement of Goalkeeper per Possession: 

   - The percentage of possessions in which the goalkeeper made at least one pass. 

**16** 


