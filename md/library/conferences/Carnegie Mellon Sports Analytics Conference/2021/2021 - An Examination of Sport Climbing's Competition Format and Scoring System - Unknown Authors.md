<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2021/2021 - An Examination of Sport Climbing's Competition Format and Scoring System - Unknown Authors.pdf -->

# An Examination of Sport Climbing’s Competition Format and Scoring System 

Quang Nguyen<sup>∗</sup> Hannah Butler<sup>†</sup> Gregory J. Matthews<sup>‡</sup> 

2021 CMSAC Reproducible Research Competition 

#### **Abstract** 

Sport climbing, which made its Olympic debut at the 2020 Summer Games, generally consists of three separate disciplines: speed climbing, bouldering, and lead climbing. However, the International Olympic Committee (IOC) only allowed one set of medals per gender for sport climbing. As a result, the governing body of sport climbing, rather than choosing only one of the three disciplines to include in the Olympics, decided to create a competition combining all three disciplines. In order to determine a winner, a combined scoring system was created using the product of the ranks across the three disciplines to determine an overall score for each climber. In this work, the rank-product scoring system of sport climbing is evaluated through simulation to investigate its general features, specifically, the advancement probabilities for climbers given certain placements. Additionally, analyses of historical climbing contest results are presented and real examples of violations of the independence of irrelevant alternatives are illustrated. Finally, this work finds evidence that the current competition format is putting speed climbers at a disadvantage. 

> ∗Loyola University Chicago. Corresponding author, nnguyen22@luc.edu. 

> †Colorado State University 

> ‡Loyola University Chicago 

1 

## **1 Introduction** 

### **1.1 Combined Competition Format** 

The 2020 Summer Olympics in Tokyo, Japan marked the first appearance of sport climbing on the Olympic stage. This sport is broken down into three disciplines: speed climbing, bouldering, and lead climbing. However, since only one set of Olympic medals is awarded to each gender event of sport climbing at Tokyo 2020, all three disciplines were included together, forming one single combined event. Under this “triathlon” format, every climber must compete in all three concentrations, and their individual score is determined as the product of the ranks across the three disciplines, with the lowest rank product declared the winner. 

The decision to combine the three climbing events and only award one set of medals for both men’s and women’s events in the Olympics has received a large amount of criticism from climbing athletes all over the world. In a series of interviews conducted by Climbing Magazine in 2016 (Blanchard, 2016), a number of climbers shared their thoughts and concerns about the new Olympics climbing format. Legendary climber Lynn Hill compared the idea of combining speed climbing, bouldering, and lead climbing to “asking a middle distance runner to compete in the sprint.” She then added “Speed climbing is a sport within our sport.” Other climbers also hold the same opinion as Hill regarding speed climbing, using words and phrases like “bogus,” “a bummer,” “less than ideal,” “not in support,” and “cheesy and unfair” to describe the new combined competition format. Courtney Woods stated “Speed climbers will have the biggest disadvantage because their realm isn’t based on difficult movements.” Mike Doyle believed “Honestly, the people that will suffer the most are the ones that focus only on speed climbing. Those skills/abilities don’t transfer as well to the other disciplines.” The climbers also expressed their hope for a change in the competition format in future climbing tournaments. 

### **1.2 Rank-product Scoring System** 

At the 2020 Summer Olympics, both sport climbing competitions for male and female begin with 20 climbers who have previously qualified for the Olympics from qualifying events held in 2019 and 2020. All 20 athletes compete in each of the three disciplines in the qualification round, and their performances in each concentration are ranked from 1 to 20. A competitor’s combined score is computed as the product of their ranks in the three events; specifically, 



where _Ri_<sup>_S_,</sup><sup>_R_</sup> _i_<sup>_B_,and</sup><sup>_R_</sup> _i_<sup>_L_aretheranksofthe</sup><sup>_i_-thcompetitorinspeedclimbing,bouldering,andlead</sup> climbing, respectively. 

The 8 qualifiers with the lowest score in terms of product of ranks across the three disciplines 

2 

advance to the finals, where they once again compete in all three events. Similar to qualification, the overall score for each contestant in the final stage is determined by multiplying the placement of speed, bouldering, and lead disciplines, and the athletes are ranked from 1 to 8. The climbers with the lowest, second lowest, and third lowest product of ranks in the final wins the gold, silver, and bronze medal, respectively. 

This type of scoring system heavily rewards high finishes and relatively ignores poor finishing results. For instance, if climber A finished 1st, 20th, and 20th and climber B finished 10th, 10th, and 10th, climber B would have a score of 1000 whereas climber A would have a much better score of 400, despite finishing last in 2 out of 3 of the events. 

To the best of our knowledge, we know of no sporting event, team or individual, that uses the product of ranks to determine an overall rankings. There are examples of team sports that use the rank-sum scoring to determine the winning team such as cross country, where the squad with the lowest sum of ranks of the top five runners is awarded with a first place finish. However, Hammond (2007) and Boudreau et al. (2018) pointed out several problems with rank-sum scoring in cross country, including violations of social choice principles. In addition, some individual sports such as the decathlon and heptathlon rely on a sum of scores from the ten or seven events, however, these scores are not determined based on the ranks of the competitors. That is, a decathlete’s score is entirely based upon their times, distances, and heights, and their overall score will be exactly the same if the times, distances, and heights remain the same regardless of the performance of other individuals (Westera, 2006). Furthermore, there are other individual competitions consisted of several events combined that do base their scoring on ranks, such as crossfit competitions. In each event, points are earned based on the competitor’s rank in the event based on a scoring table, and a competitors final score is based on the sum of their scores across all the events (CrossFit, 2021). 

In this paper, we perform statistical analysis to investigate the limitations of sport climbing’s combined competition format and ranking system. We will evaluate whether the concerns of the professional climbers were valid. The manuscript is outlined as follows. We first begin with a simulation study to examine the key properties of rank-product scoring in sport climbing in Section 2. Our analyses of past competition data are then presented in Sections 3. Finally, in Section 4, we provide a summary of our main findings as well as some discussion to close out the paper. 

## **2 Simulation Study** 

In this section, we perform a simulation study to examine the rankings and scoring for climbers in both qualification and final rounds. For each round, we execute 10000 simulations, and this was accomplished by randomly assigning the ranks of each event to every participant, with the assumption that the ranks are uniformly distributed. After that, we calculate the total scores for every simulated round, as well as the final standings for the climbing athletes. The simulation results allow us to explore different properties of sport climbing’s rank-product scoring system, 

3 

including the distributions of total score for qualifying and final rounds, and the probabilities of advancing to the finals and winning a medal, given certain conditions. 

We are particularly interested in the following questions: 

- For a qualifier, what is the probability that they advance to the final round (i.e. finish in the top 8 of qualification), given that they win any discipline? 

- For a finalist, what is the probability that they win a medal (i.e. finish in the top 3 of the finals), given that they win any discipline? 

Our simulation results, as illustrated by Figure 1, show that a climber is almost guaranteed to finish in the top 8 of qualification and advance to the final round if they win at least one of the three climbing concentrations (99.48% chance). Regarding the finals, a climber is also very likely to claim a top 3 finish and bring home a medal if they win any event (85.01% chance). Moreover, we notice that if a climber wins any discipline, they are also more likely to finish first overall than any other positions in the eventual qualification and final rankings. This shows how significant winning a discipline is to the overall competition outcome for any given climber. 

In addition, we are interested in examining the distribution of the total score for both qualification and final rounds. Figure 2 is a summary of the expected score for each qualification and final placement. According to our simulations, on average, the qualification score that a contestant should aim for in order to move on to the final round is 435 (for 8th rank). Furthermore, we observe that in order to obtain a climbing medal, the average scores that put a finalist in position to stand on the tri-level podium at the end of the competition are 10, 21, and 34 for gold, silver, and bronze medals, respectively. 



<!-- Start of picture text -->
Qualification Final<br>1<br>1<br>2<br>3 2<br>4<br>3<br>5<br>6 4<br>7<br>5<br>8<br>9 6<br>10<br>7<br>11<br>0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00<br>Probability Density<br>Distribution Cumulative Probability<br>Rank<br><!-- End of picture text -->

Figure 1: The distributions for the probability of finishing at each rank of both qualification and final rounds, given that a climber wins any discipline, obtained from simulations. The probability of finishing exactly at each given rank is coded blue, whereas the probability of finishing at or below each given rank is coded maroon. 

4 



<!-- Start of picture text -->
Qualification Final<br>643 266<br>600<br>533<br>200<br>435<br>165<br>400<br>351<br>279 111<br>217 100<br>200 76<br>163<br>116 51<br>74 34<br>37 10 21<br>0 0<br>1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8<br>Rank<br>Average Score<br><!-- End of picture text -->

Figure 2: The average scores for the top 10 qualification ranks and all 8 final ranks, obtained from simulations. 

## **3 Analysis** 

### **3.1 Correlation** 

Throughout this section, we will be using data from the Women’s Qualification at the 2020 Summer Olympics (Wikipedia contributors, 2021) as a case study for examining the relationship between the climber rankings in each individual discipline and the overall standings. The main attributes of this data are the name and nationality of the climbers; the finishing place of climbers in speed climbing, bouldering, and lead climbing; the total score (which equals the product of the discipline ranks); the overall placement; and the performance statistics associated with speed (race time), bouldering (tops-zones-attempts), and lead climbing (highest hold reached). We utilize this data to analyze the correlations between the event ranks and final table position, as well as to look at how often the final orderings change if one athlete is removed and the remaining climbers’ ranks and total scores in each discipline are re-calculated. 

Figure 3 is a multi-panel matrix of scatterplots of the ranks of the individual events and the final women’s qualification standings. We use Kendall’s Tau (Kendall, 1938) as our measure of ordinal association between the ranked variables. Table 1 shows the Kendall rank correlation coefficients between the overall rank and the ranks of speed, bouldering, and lead disciplines; along with corresponding 95% confidence intervals obtained from bootstrapping (Efron & Tibshirani, 1986). 

It is evidently clear that there exists a fairly strong and positive association between the final rank and the ranks of both bouldering ( _τ_ = 0 _._ 432, _p_ -value = 0 _._ 00735, Bootstrapped 95% CI: (0.107, 0.691)) and lead climbing ( _τ_ = 0 _._ 463, _p_ -value = 0 _._ 00378, Bootstrapped 95% CI: (0.112, 0.753)). 

5 

This implies that climbers with high placements in both bouldering and lead also tend to finish at a higher ranking spot overall. 

On the other hand, the correlation with the final rank is not as strong for speed climbing as the other two events ( _τ_ = 0 _._ 147), and there is insufficient evidence for an association between the rank of speed climbing and the overall rank ( _p_ -value = 0 _._ 386, Bootstrapped 95% CI: (-0.191, 0.469)). Thus, this offers evidence that speed climbers are at a disadvantage under this three-discipline combined format, compared to those with expertise in the other two concentrations. This validates the concerns of climbers from the interviews mentioned in Section 1.1. 



<!-- Start of picture text -->
Speed Bouldering Lead<br>20<br>10<br>0<br>5 10 15 20 5 10 15 20 5 10 15 20<br>Rank<br>Overall<br><!-- End of picture text -->

Figure 3: Scatterplots of overall rank and speed, bouldering, and lead ranks for Women’s Qualification at Tokyo 2020. 

Table 1: Kendall’s tau values, along with correlation test statistics, p-values, and bootstrapped 95% confidence intervals, for the overall rank and the rank of speed, bouldering, and lead disciplines of Women’s Qualification at Tokyo 2020. 

|Discipline|Kendall’s Tau|Test Statistic|p-value|Bootstrapped 95% CI|
|---|---|---|---|---|
|Speed|0.147|109|0.386|(-0.191, 0.469)|
|Bouldering|0.432|136|0.00735|(0.107, 0.691)|
|Lead|0.463|139|0.00378|(0.112, 0.753)|



In addition, we perform principal component analysis (PCA) to summarize the correlations among a set of observed performance variables associated with the three climbing disciplines. In particular, using the data from the Women’s Qualification round at Tokyo 2020, we look at the racing time (in seconds) for speed; the number of successfully completed boulders (“tops”); and the number of holds reached for lead. 

6 

Figure 4 is a PCA biplot showing the PC scores of the climbers and loadings of the skill variables. We notice that the lead and bouldering performances strongly influence PC1, while speed time is the only variable contributing to PC2, separated from the other two skills. Moreover, since the two PC1 vectors are close and form a small angle, the two variables they represent (bouldering tops and lead holds reached) are positively correlated. This implies that a climber that does well in bouldering is also very likely to deliver a good performance in lead climbing. 



Figure 4: PCA Biplot for Women’s Qualification at Tokyo 2020 

### **3.2 Leave-one-climber-out Analysis** 

Another question that we are interested in investigating is “What would happen to the rankings if a single climber is removed?” There is a connection between this situation and the idea of independence of irrelevant alternatives (IIA). The IIA criterion is a property of a voting system which states that after a winner is determined, if one of the losing candidates drops out and the votes are recounted, there should not be a change in the winner. First mentioned by Arrow (1951), the IIA condition is also known as Luce’s choice axiom (Luce, 1959) in probability theory, and it has had a number of applications in the fields of decision theory, economics, and psychology over the years. We notice a link between the concept of IIA and the topic of ranking system in sports. As an illustration, suppose we have 3 players A, B, and C participating in a competition. If A finishes in the first place and C is later disqualified and removed, A should still win. If the original winner (A) 

7 

loses the modified competition (with C removed), then the Independence of Irrelevant Alternatives has been violated. For our particular case, this sort of analysis can be helpful in examining the overall outcome for a climbing contest, specifically how a disqualification can affect the standings of medalists in the final round. 

In the analysis that follows, we use data from the 2018 Youth Olympics Women’s Final (Olympic World Library, 2018). This event also implemented the combined format and rank-product scoring system, but only consisted of 6 climbers competing in the final, rather than 8 as Tokyo 2020. We modify the data as follows. After an athlete is dropped (by their rank), the new ranks for each discipline of the remaining players are re-calculated. The new final scores can then be obtained by multiplying the three event ranks, which then determines the new overall ranks. 

Figure 5 shows the modified versions of the rankings after each ranked climber is excluded for the Women’s Final at the 2018 Youth Olympics. We have clear evidence from this plot that removing a single climber changes the rankings drastically, especially in terms of the order of medalists. One particular interesting case is where an athlete’s position changes when someone who originally finished behind them drops out. This situation is illustrated by panel 5 of the women’s competition, where the fifth-place climber, Krasovskaia, was excluded; and Meul, whose actual final rank was fourth, moved up to the second spot and would have claimed the silver medal. Furthermore, this clearly demonstrates that the rank-product scoring method of Olympics sport climbing violates the IIA criterion. 



<!-- Start of picture text -->
0 1 2 3<br>Lettner 1 1 1<br>Lukan 2 1 3<br>Lammer 3 2 2<br>Meul 4 3 3 2<br>Krasovskaia 5 4 5 4<br>Nakamura 6 5 4 5<br>0 20 40 60<br>4 5 6<br>Lettner 1 1 1<br>Lukan 2 3 2<br>Lammer 3 4 3<br>Meul 2 4<br>Krasovskaia 4 5<br>Nakamura 5 5<br>0 20 40 60 0 20 40 60 0 20 40 60<br>Score<br><!-- End of picture text -->

Figure 5: This figure illustrates the changes to the 2018 Youth Olympics Women’s Final rankings when each climber is left out. Each panel represents the rank of the drop-out athlete, with 0 being the original final results. Each case with a change in rank orderings is highlighted by a black panel border, and any player with a rank change is represented by a red-filled bar 

8 

## **4 Conclusion and Discussion** 

In this paper, we examined the general features of the rank-product scoring system of sport climbing, in particular, the advancement probabilities and scores for the climbers. Most importantly, through analyses of past competition data, we pointed out several problems of the combined competition format and rank-product scoring system of sport climbing. First, combining the three disciplines speed, bouldering, and lead together into a “triathlon” competition format is putting speed climbers in an unfavorable position. Second, the sport climbing scoring method violates the independence of irrelevant alternatives. There is a dependency on irrelevant parties in this scoring method, as the orderings of medalists can be affected with a drop-out of a lower-ranked climber. 

We suggest that speed climbing should have its own set of medals in future climbing tournaments, whereas bouldering and lead climbing can be combined into one event. In fact, it was confirmed that in the next Summer Olympics held in Paris in 2024, there will be two competitions and two sets of climbing medals for each gender event: combined lead and bouldering, and speed-only (Goh, 2020). This is consistent with what we have shown, as bouldering and lead climbing performances are highly correlation with each other and with the overall result, whereas speed climbing should be separated from the combined format. 

## **Supplementary Material** 

All materials related to this manuscript are publicly available on `GitHub` at https://github.com/ qntkhvn/cmsac_rrc. In addition, a series of blog posts on sport climbing can be found on the corresponding author’s website at https://qntkhvn.netlify.app/blog. 

## **References** 

Arrow, K. J. (1951). _Social choice and individual values_ . Wiley: New York. 

- Blanchard, B. (2016). _Olympic climbing survey: 15 pro climbers weigh in_ . https://www.climbing. com/news/olympic-climbing-survey-15-pro-climbers-weigh-in 

- Boudreau, J., Ehrlich, J., Raza, M. F., & Sanders, S. (2018). The likelihood of social choice violations in rank sum scoring: Algorithms and evidence from NCAA cross country running. _Public Choice_ , _174_ (3), 219–238. 

- CrossFit. (2021). _About the games_ . https://games.crossfit.com/about-the-games 

- Efron, B., & Tibshirani, R. (1986). Bootstrap Methods for Standard Errors, Confidence Intervals, and Other Measures of Statistical Accuracy. _Statistical Science_ , _1_ (1), 54–75. 

- Goh, Z. K. (2020). _Breaking, sport climbing, surfing, skateboarding confirmed as additional sports for paris 2024_ . https://olympics.com/en/news/breaking-sport-climbing-surfing-skateboardingparis-2024 

9 

- Hammond, T. H. (2007). Rank injustice? How the scoring method for cross-country running competitions violates major social choice principles. _Public Choice_ , _133_ (3), 359–375. 

- Kendall, M. G. (1938). A new measure of rank correlation. _Biometrika_ , _30_ (1/2), 81–93. Luce, R. D. (1959). _Individual choice behavior: A theoretical analysis_ . Wiley: New York. 

- Olympic World Library. (2018). _Official results books: Buenos aires 2018 youth olympic games_ (Vol. 26). https://library.olympics.com/Default/doc/SYRACUSE/177522/official-results-booksbuenos-aires-2018-youth-olympic-games-buenos-aires-youth-olympic-games-organi 

- Westera, W. (2006). Decathlon, towards a balanced and sustainable performance assessment method. _New Studies in Athletics_ , _21_ (1), 39–51. 

- Wikipedia contributors. (2021). _Sport climbing at the 2020 summer olympics – women’s combined_ . https://en.wikipedia.org/wiki/Sport_climbing_at_the_2020_Summer_Olympics__Women’s_combined 

10 


