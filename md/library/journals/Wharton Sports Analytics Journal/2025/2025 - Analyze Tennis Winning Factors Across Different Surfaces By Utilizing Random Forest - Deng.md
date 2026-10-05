<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Analyze Tennis Winning Factors Across Different Surfaces By Utilizing Random Forest - Deng.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/analyze-tennis-winning-factors-across-different-surfaces-by-utilizing-random-forest/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2025 -->
<!-- authors: Wuhuan Deng -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

WUHUAN DENG

Department of Applied Mathematics, University of Washington, Seattle, WA briandeng0216@gmail.com

Abstract. Tennis is one of the most popular sports worldwide, with a rich calendar of professional tournaments played across three court surfaces: hard, grass, and clay. Each surface has unique physical characteristics that significantly influence ball behavior, player movement, and match dynamics. As a result, different playing styles tend to be more effective on certain surfaces. This research investigates the surface-dependent nature of match outcomes by exploring statistical trends and performance indicators that contribute to success on each court type. Understanding these differences can provide deeper insights into player adaptability, match strategies, and surface-specific training.

## 1. Introduction

2 1.1. Motivation. Grass, clay, and hard courts differ significantly from one another, each possessing 3 unique characteristics that influence gameplay. Grass courts are the most traditional surface, 4 featuring low, unpredictable bounces and a fast pace. They are preferred by players who favor 5 a serve-and-volley style [Nag, 2022a]. Roger Federer is widely regarded as the greatest player on 6 grass, having won eight Wimbledon men’s singles titles between 2003 and 2017 [?]. 7 Clay courts are made of crushed stone and other minerals. They produce higher bounces and 8 slow down the ball, making it more challenging to hit winners [Nag, 2022a]. This surface tends to 9 benefit players who excel in long rallies. Rafael Nadal, also known as the ”King of Clay,” has won 10 the most men’s singles titles at Roland Garros, with 14 championships [Chennai, 2024]. 11 Hard courts are the most common surface in modern tennis. The speed of play on hard courts 12 varies depending on the composition of the top layer, but in general, they are faster than clay 13 courts and slower than grass courts [Nag, 2022a]. The US Open and Australian Open—two of the 14 four Grand Slams—are played on hard courts. This surface is often favored by all-around players 15 without significant weaknesses, such as Novak Djokovic [Nag, 2022a].

2 ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

16 Given this information, different techniques and strategies are required to succeed on each surface. 17 In this research, we are going to analyze professional match data from grass, clay, and hard courts 18 to examine how various match features influence winning probabilities on each surface.

Figure 1. Distribution of 1st-serve speed across the three surfaces. Grass courts generally yield the fastest serve speeds, while clay courts have the lowest.

19 1.2. Related Works. Soomedha Vasudevan and Nick Chu analyzed how various match features in20 fluence winning percentage across the three surfaces using linear regression methods [Vasudevan and Chu, 2023]. 21 They computed the R-squared values between individual features and surface-specific win percent22 ages, finding that the same feature could have slightly different R-squared values depending on the 23 surface. However, most of these R-squared values were close to zero, and the differences across sur24 faces were minimal. Moreover, their analysis did not reveal how changes in feature values influence 25 win probability, beyond simple scatter plots. Our research extends this work by using Random 26 Forest classifiers with multiple input features, enabling nonlinear modeling and capturing interac27 tions between variables. By incorporating feature importance and partial dependence analysis, our 28 method uncovers more nuanced and surface-specific patterns in match outcomes that linear models 29 may overlook.

## 2. Materials and Methods

31 2.1. Dataset. The match data used in this research was collected from GitHub [Sackmann, 2024]. 32 The dataset includes matches from three Grand Slam tournaments: the US Open (2018, 2019, 33 2023, and 2024), Wimbledon (2021, 2022, 2023, and 2024), and the French Open (2015 and 2016). 34 In total, the dataset contains 479 matches played on grass, 437 on hard courts, and 187 on clay

ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST 3

35 courts. The data is structured on a point-by-point basis, with each row corresponding to a single 36 point and each column representing a specific match feature.

37 2.2. Random Forest. Random Forest is a widely used supervised learning algorithm for both 38 classification and regression tasks. It is composed of multiple decision trees and outputs a class 39 label for classification problems or an average prediction for regression problems [Breiman, 2001]. 40 Each tree in the forest is trained on a bootstrap sample of the data, and at each node split, a 41 random subset of features is considered to promote diversity among trees. Given an input x and a 42 Random Forest consisting of n trees, the predicted output is defined as: yˆ

=

1 n

Σtn=1 fi

(x),

43 where fi(x) is the prediction from the ith decision tree. By ensembling multiple trees, Random 44 Forest reduces variance and helps prevent overfitting compared to using a single decision tree. 45 In this research, three separate Random Forest models are trained—one for each court sur46 face. The input to each model consists of 10 player-specific features, and the output is a binary 47 classification indicating the match outcome: 0 for a loss and 1 for a win.

Feature Name 1st-speed 2nd-speed ace-rate double-fault-rate 1st-rate

1st-win-rate 2nd-win-rate net-win-rate winner-rate unforced-error-rate

Description Average first serve speed Average second serve speed Number of ace / Number of serves Number of double faults / Number of service points Number of 1st serve in / Total 1st serve attempts Points won on 1st serve / Number of 1st serve in Points won on 2nd serve / Number of 2nd serve in Points won at net / Number of net approaches Number of winners / Total points played Number of unforced errors / Total points played

Table 1. This table lists the 10 input features and their basic descriptions. For clarification: an ace is a serve that lands in the service box and is not touched by the returner; a winner is any shot that lands in bounds and is not returned by the opponent; and an unforced error is a mistake made when the player is not under pressure—in other words, an error that should be avoidable at the professional level.

4 ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

Surface Grass Clay Hard n estimators 100 50 100 max depth 10 5 10 min samples leaf 5 5 5 bootstrap True True True

Table 2. This table shows the Random Forest parameter values used for each surface. All other parameters not listed here are set to their default values from the scikit-learn package.

48 2.3. Feature Importance. To assess the importance of each feature in predicting match outcomes

49 using the Random Forest model, we computed feature importance based on Mean Decrease in

50 Impurity (MDI) [Breiman, 2001]. This metric quantifies the total reduction in node impurity

51 attributed to each feature across all trees in the forest. Given a feature xj, its importance I(xj) is

52 defined as:

I (xj )

=

1 n

Σtn=1

Σk∈Nj(t) p(k

)

·

∆i(k),

53 where n is the number of trees, Nj(t) is the set of nodes in tree t where feature xj is used for splitting,

54 p(k) is the proportion of training samples reaching node k, and ∆i(k) is the impurity reduction

55 achieved at that node [Louppe et al., 2013]. This quantitative metric provides a ranking of features

56 based on their influence on the model’s final predictions. The MDI for each feature ranges from 0

57 to 1, and the sum of all feature importances equals 1.

MDI Value > 0.15

0.05 - 0.15 0.01 - 0.05

< 0.01

Importance Level Very important - dominant feature Moderately important - strong signal

Weak but maybe useful Not useful

Table 3. This table explains the interpretation of each MDI value range in terms of feature importance.

58 2.4. Partial Dependence. To further analyze the impact of each feature, we utilized Partial De-

59 pendence (PD) and visualized it across different features and court surfaces. A Partial Dependence

60 Function (PDF) measures the average model prediction as a function of one or more selected input

61 features, while averaging out the effects of all other features [Friedman, 2001]. Given a prediction

62 function f (x) trained by a Random Forest model, and a subset of features S, the PDF is defined

63 as: fˆs(xs)

=

1 n

Σni=1f

(xs, x(Ci)),

ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST 5

64 where C is the complement of S, and xC(i) represents the values of the remaining features for the ith 65 instance in the dataset. This metric estimates the expected model output when the features in S 66 are fixed, while the other features vary according to their observed distribution. For example, if a 67 player has a 1st-win-rate of 0.75 and the corresponding partial dependence value is 0.76, it means 68 that if all players had a 1st-win-rate of 0.75, the model would predict an average win probability 69 of 76%, regardless of the other feature values.

## 3. Result

71 3.1. Random Forest. To ensure that the computed feature importance and partial dependence 72 values are meaningful and reliable, it is essential to begin with well-performing Random Forest 73 models. Therefore, we require all three models—one for each surface—to achieve at least 80% 74 accuracy on the testing set. The testing data consists of 20% of the total matches for each surface, 75 randomly selected from the dataset.

Surface Grass Clay Hard

Training Accuracy Score 0.925% 0.934% 0.906%

Testing Accuracy Score 0.904% 0.819% 0.833%

Table 4. This table shows Random Forest model performance results for each court surface.

76 3.2. Feature Importance. Next, we computed the feature importance scores for each input fea77 ture using the trained Random Forest models.

6 ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

Figure 2. Feature importance of each model.

78 Unsurprisingly, 1st-win-rate is the most influential feature across all three surfaces, with impor79 tance scores of 0.36 on grass, 0.33 on hard, and 0.36 on clay. This aligns with both our expectations 80 and traditional tennis insights from players and coaches—capitalizing on first-serve opportunities 81 is widely considered one of the most critical factors for match success. The 2nd-win-rate ranks 82 second in importance, although its contribution on grass courts is notably lower compared to hard 83 and clay surfaces. This observation is reasonable, as every point begins with a serve—whether first 84 or second—and the ability to consistently win serve points strongly correlates with overall match 85 outcomes. Given that 1st-win-rate and 2nd-win-rate dominate the model, it becomes especially 86 important to examine the remaining features to uncover more nuanced, surface-specific patterns. 87 The third most important feature on hard courts differs from that on grass and clay courts. 88 Winner-rate ranks third in importance on both grass and clay surfaces, whereas unforced-error89 rate holds the third position on hard courts. This may suggest that aggressive playing styles—which 90 often result in more winners—are more advantageous on grass and clay courts. This is particularly 91 true for clay courts, where the slower surface makes it harder to hit winners; thus, players who can 92 still generate them may gain a significant competitive edge. 93 Although winner-rate is not ranked third on hard courts, its importance score (0.10) is equal to 94 that of unforced-error-rate, suggesting a balanced contribution from both features. This supports 95 the earlier observation that all-around players tend to perform better on hard courts, where no

ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST 7

96 single playing style is dominant. In comparison, the importance of unforced-error-rate on grass 97 and clay courts is lower, at 0.07 for both. This implies that while unforced errors are still relevant, 98 taking calculated risks that may result in winners can be more rewarding on grass and clay surfaces. 99 Focusing on serve-related features, grass courts show the highest feature importance for both 100 ace-rate and double-fault-rate, each with a value of 0.07. This highlights the critical role of serving 101 on grass—players are rewarded not only for their ability to generate aces but also for their ability 102 to minimize errors. In contrast, double-fault-rate has a much lower importance on clay courts, with 103 a value of just 0.02, suggesting that serve-related mistakes are less consequential on slower surfaces 104 like clay. 105 Ace-rate holds moderate importance on both clay and hard courts, with a value of 0.05 for each. 106 While serving may not offer as significant an advantage as it does on grass courts, it remains a 107 critical component of success across all surfaces. These results indicate that although grass courts 108 demand the most from serve performance, the ability to serve effectively continues to play an 109 important role in winning matches on any surface. 110 3.3. Partial Dependence. To further explore how each feature influences winning probability, 111 we conducted a detailed analysis of several selected features.

Figure 3. Partial dependence of winner-rate on winning probability across the three court surfaces.

112 From the graph above, it is evident that a higher winner-rate consistently correlates with in113 creased winning probabilities across all three court surfaces. When the winner-rate is below 0.12, 114 the predicted winning probability remains low and relatively flat. On hard courts, the winning

8 ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

115 probability begins to rise once the winner-rate exceeds 0.13, indicating that even a slight increase 116 in aggressive play can lead to better outcomes. Grass courts follow a similar pattern, with a no117 ticeable increase occurring at a comparable threshold. In contrast, the clay court curve rises more 118 gradually at first but shows a sharp increase once the winner-rate surpasses 0.16. 119 When the winner-rate reaches 0.20, the winning probabilities on both hard and grass courts begin 120 to plateau. However, on clay courts, the upward trend continues sharply until approximately 0.22. 121 Beyond this point, the growth levels off, but clay courts maintain the highest predicted winning 122 probability when the winner-rate exceeds 0.20. This pattern suggests that on slower surfaces like 123 clay, the ability to generate winners has a particularly significant impact on match outcomes. 124 Overall, increasing the winner-rate from 0.12 to 0.24 leads to at least a 0.15 increase in predicted 125 winning probability across all surfaces. This underscores the critical role of hitting winners in 126 achieving match success, regardless of the court surface.

Figure 4. Partial dependence of unforced-error-rate on winning probability across the three court surfaces.

127 From the graph above, we observe that achieving a winning probability above 0.5 requires a very 128 low unforced-error rate—below 0.1—across all three surfaces. As the unforced-error-rate increases, 129 the winning probability consistently decreases, with the steepest decline occurring on hard courts. 130 In contrast, grass and clay courts exhibit more gradual declines. When the unforced-error rate 131 exceeds 0.2, the winning probabilities on all surfaces fall below 0.45, with hard courts showing the 132 lowest values. This suggests that consistency plays a particularly important role on hard courts, 133 where minimizing unforced errors yields the greatest impact on match outcomes.

ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST 9

Figure 5. Partial dependence of ace-rate on winning probability across the three court surfaces.

134 From the graph above, the relationship between ace rate and winning probability shows greater 135 variability compared to winner-rate. When the ace-rate exceeds 0.05, both clay and hard courts 136 show an increase in winning probability, while the grass court curve unexpectedly dips before 137 beginning to rise again around 0.075. Between an ace-rate of 0.13 and 0.15, all three surfaces reach 138 their peak predicted winning probabilities, with clay courts showing the highest value. However, 139 beyond 0.15, winning probabilities drop sharply on both hard and grass courts, while the value 140 on clay remains relatively stable. A possible explanation is that aces are more difficult to achieve 141 on clay, the slowest surface; thus, players who manage to hit many aces on clay may be more 142 well-rounded. In contrast, on faster surfaces, players who rely heavily on aces might lack other 143 essential skills—such as groundstrokes—leading to lower overall performance. As previously noted, 144 all-around players tend to have an advantage on hard courts in particular.

## 4. Discussion

146 This research currently focuses on individual features. However, in actual matches, many metrics 147 are closely related—for example, aces and double faults, or winners and unforced errors. It would 148 be reasonable to create more informative features by combining related variables and incorporating 149 them into the model. Additionally, although we separated the data by surface type, there are still 150 notable differences between tournaments held on the same surface. For instance, the Australian 151 Open and US Open—both played on hard courts—have different surface characteristics. Therefore, 152 analyzing surface conditions at the tournament level could provide more practical insights for

10ANALYZE TENNIS WINNING FACTORS ACROSS DIFFERENT SURFACES BY UTILIZING RANDOM FOREST

153 players preparing to compete. Lastly, our analysis has focused on outcome-based statistics, such as 154 aces, rather than the mechanics of the actions themselves, like serve speed or spin rate. To further 155 improve player performance, it may be beneficial to analyze technical attributes of individual shots.

## 5. Conclusion

157 Although it is well known that increasing 1st-win-rate and 2nd-win-rate benefits players, our 158 model results offer additional, previously unseen insights. Hard courts demand well-rounded skills, 159 requiring players to excel in both serving and groundstrokes. On clay courts, where the surface 160 slows down play, players who can still produce aces and winners gain a distinct advantage. For grass 161 courts, effective serving is crucial, but controlling double faults is equally important. We believe 162 our analysis can offer practical suggestions for professional players in preparing their strategies for 163 different surfaces. Of course, these insights alone cannot directly enhance performance—consistent 164 training, both on and off the court, remains essential.

## Acknowledgments

166 I would like to thank the authors of the tennis-slam-pointbypoint GitHub repository for making 167 their dataset publicly available, which provided a valuable foundation for this research.

## References

169 [Breiman, 2001] Breiman, L. (2001). Random forests. Machine Learning, 45(1):5–32. 170 [Chennai, 2024] Chennai (2024). Rafael nadal at french open: Full list of titles won, nadal’s record at roland garros 171 before 2024 match against zverev. 172 [Friedman, 2001] Friedman, H. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of 173 Statistics, 29(5):1189–1232. 174 [Louppe et al., 2013] Louppe, G., Wehenkel, L., Sutera, A., and Geurts, P. (2013). Understanding variable impor175 tances in forests of randomized trees. 26. 176 [Nag, 2022a] Nag, U. (2022a). Everything you need to know about tennis courts. 177 [Nag, 2022b] Nag, U. (2022b). Roger federer at wimbledon: When ’king roger’ ruled. 178 [Sackmann, 2024] Sackmann, J. (2024). tennis slam pointbypoint. 179 [Vasudevan and Chu, 2023] Vasudevan, S. and Chu, N. (2023). Decoding surface deominance: The skills behind 180 tennis triumphs.
