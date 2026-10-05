<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Boosting Draft Accuracy A Two-Stage Classifier Regressor Approach for NFL Wide Receiver Prospect Evaluation - Patangi.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/boosting-draft-accuracy-a-two-stage-classifier-regressor-approach-for-nfl-wide-receiver-prospect-evaluation/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Aadi Patangi -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

## 1 Boosting Draft Accuracy: A Two-Stage Classifier–Regressor

## 2 Approach for NFL Wide Receiver Prospect Evaluation

Aadi Patangi

Amador Valley High School

## 6 ABSTRACT

7 The NFL draft is an opportunity for teams to draft new players, address positional needs, and strengthen

8 their roster for the upcoming season. Teams often trade players or compensation packages to secure certain

9 prospects, which can be critical for team success. Wide receivers were selected as the focus of this study because the

10 position is heavily influenced by objective data — such as receiving statistics and combine metrics like speed,

11 agility, and explosiveness — making it well-suited for predictive modeling using machine learning. This study

12 presents a two-stage machine learning approach to first predict whether a wide receiver (WR) invited to the NFL

13 Scouting Combine will be drafted, and if so, at which overall position. Using physical testing data from the NFL

14 combine, college production statistics, and historical draft result training data from 2000 to 2024, we construct a

15 Gradient Boosting Classifier to predict draft likelihood followed by a CatBoost Regressor to estimate draft position

16 for those predicted to be selected. This approach provides NFL teams and scouts with a reliable estimate of whether

17 and when a combine-invited wide receiver will be drafted, helping them make more informed decisions and

18 strategically position themselves to select desired prospects. In validation, our classifier reached 89.2% accuracy

19 (F₁ = 0.936), and our regressor yielded a 49.2-pick MAE (ρ = 0.626), demonstrating robust predictive performance.

20 Keywords: predictive analytics, NFL draft, wide receivers, sports analytics, machine learning

22 23 24

## 25 Introduction

26 27 In recent years, the wide receiver has emerged as a crucial position for the success of teams in the National Football 28 League (NFL). NFL teams strive to have star wide receivers on their roster, which can often transform a team’s 29 offense into a high-powered, game-changing threat that can stretch the field and exploit defensive mismatches. Wide 30 receivers not only need to run various routes but also have the ability to jump and catch passes and occasionally 31 block. While teams can sign wide receivers through free agency, many teams prefer to draft core receivers out of 32 college. Many of the college football prospects each year, including wide receivers, are invited to the NFL Combine 33 if they receive an invitation from the Player Selection Committee based on college performance. Although only 34 select players are invited to the combine, a strong showing can significantly elevate a player's draft stock, while a 35 weak performance can just as easily cause it to fall. Thus, it’s possible to quantify and predict whether a player gets 36 drafted or not and if so, at what pick based on their college performance and their performance at the combine if 37 they got invited. 38 Past studies have used machine learning (ML) models to forecast binary football-related outcomes. Primarily, Clark 39 et al. (2013) constructed a logistic regression model using field goal play-by-play data from the 2000-2011 NFL 40 seasons to identify influential factors for field goal success and found that psychological factors have no statistically 41 significant effects on the probability of making a field goal whereas environmental factors such as temperature, 42 precipitation, and wind speed have a far more significant impact. Many predictor variables used in the study such as 43 weather indicators have a high degree of correlation and field goals themselves are random events affected by 44 human performance and this randomness is impossible to capture with a model. Additionally, a majority of data 45 consists of high-success probability scenarios as most field goals are likely attempted if there’s a high chance of 46 making them. A study by Gifford & Bayrak (2023) used all regular season game data from the 2002-2018 seasons 47 and constructed a logistic regression model and a decision tree model to identify the most important predictors of 48 NFL game outcomes. They achieved 83% validation accuracy with logistic regression in predicting NFL game

49 outcomes and found that turnovers lost on offense, turnovers forced on defense, total yards on offense, and total 50 yards allowed on defense were the most significant indicators. However, the study doesn’t account for statistics that 51 are derived from causation such as aggressive vs. conservative play style and doesn’t account for psychological 52 factors affecting gameplay such as confidence and shifts in momentum. A similar study by Baker & Kwartler (2015) 53 constructed two logistic regression models to predict the outcome of a play—whether a pass or run was executed— 54 using play-by-play data from the 2000–2012 seasons for the Cleveland Browns and Pittsburgh Steelers. The model 55 achieved 66.4% accuracy in predicting Cleveland’s plays and 66.9% accurate for Pittsburgh, representing only a 56 slight improvement over random guessing. The study did not employ a validation set and all data points were used 57 to train the model, which slightly flaws its accuracy. Additionally, team-based models might not be the strongest 58 indicator of play-calling compared to team personnel or coaching staffs, and the study doesn’t account for weather 59 conditions which can affect play-calling. It is a promising study that can inform the strategies of teams and 60 anticipate play selection. 61 Additionally, ML models have also been used for regression tasks in football, not involving binary outcomes and 62 rather predicting the numerical values of a variable. A study by Taylor (n.d.) utilized both a shallow convolutional 63 neural network (CNN) and transfer learning with the VGG19 image model to predict the offensive play call and 64 predict the yardage outcome of a play using play-by-play data along with images of the field before the snap of each 65 play for plays that only resulted in a yardage outcome (avoiding penalties, punts etc.). Using a cost function of mean 66 absolute yards, both models with tuned hyperparameters struggle to predict yardage outcomes with an improved 67 performance versus guessing the median of all training data for all plays, and the image data also contributed no 68 significant value. However, both the shallow CNN and VGG19 transfer learning had improved accuracy (both 69 0.606 accuracy) versus the benchmark (guess all plays are pass) for predicting play call but preformed slightly worse 70 than a simpler random forest model without image data (0.614 accuracy). A similar study by Teich et al. (2016) also 71 predicted yardage outcome of a play as well as well as the progress metric which calculates a scaled score between 0 72 and one based on the current down, achieved yards, and yards to go as a measure of success. For example, achieving 73 a 1st down receives a score of 1, and achieving yards but not reaching a 1st down gets a decimal which is smaller on 74 later downs, and not reaching a 1st down on a 3rd or 4th down receives a 0. All the machine learning methods used to 75 predict yards gained in a play resulted in a Mean Average Error (MAE) greater than 5 and an RMSE greater than 8, 76 which is a high error margin considering that 10 yards is a 1st down. However, all ML models on the progress

77 metric only had a MAE of 0.15 or less and a RMSE of 0.25 or less. While regression tasks in the NFL are inherently 78 difficult, using a scaled and context-aware metric like progress makes prediction more meaningful and can limit 79 prediction errors. 80 Very few papers actually predicted the order of the NFL draft. A study by Mulholland & Jensen (2014) used very 81 similar predictor variables to this study to predict the draft order of tight ends using a linear regression model and a 82 decision tree model. For the decision tree, college yards and the 40-yard dash seemed to be the most important 83 predictor variables while the linear regression chose the 40-yard dash and the bench press as the most important 84 predictor variables. Although the study achieved an RMSE of 56.52 using decision trees, the model only predicts 85 draft placement on tight ends who are known to be drafted. Although they briefly explored a logistic regression 86 model to predict whether a tight end is drafted, that analysis lacks depth and doesn’t mention any coefficients or 87 model diagnostics. Although they state that 40-yard dash time was the most significant predictor and that four of six 88 combine measures were selected in the final model, the absence of detailed metrics prevents a thorough evaluation 89 of the model’s predictive power. Although 40-yard dash is identified as the most significant predictor, the lack of 90 quantitative details limits the interpretability of the model. A more thorough analysis—such as reporting feature 91 weights or applying cross-validation—would enhance the practical value of their findings. Finally, Dhar (n.d.) 92 constructed a linear regression model and a recursive partitioning regression tree (CART) model to predict draft 93 order for wide receivers. Since the study uses only drafted receivers from 1999-2008 for training and also discards 94 receivers without college data available online, only 266 training data points were used. Surprisingly, the linear 95 regression model that combined college and combine variables with a R² of 0.302 had a 40-yard dash coefficient of 96 227.5, suggesting that a 0.1 second decrease in the 40-yard dash results in a 22.75 slot improvement in predicted 97 draft placement. The primary split in the CART was total college receiving yards at a threshold of 1627 yards with 98 players above being “over-achievers” and players below being “under-achievers”. However, running a fast 40-yard 99 dash could improve projected draft position for “under-achievers” confirming the NFL bias toward 40-yard dash 100 dash times. The study never uses any testing data, and all reported metrics came from the training data. Thus, no 101 prior research has addressed predicting whether a wide receiver invited to the combine will be drafted, or estimating 102 their draft position with proper evaluation on unseen data.

## 103 Methods

## 105 Data

106 Using the nfl_data_py Python library, we compiled NFL Combine data for all wide receivers who attended between

107 2000 and 2024. Data for the 2021 season was not included in the study, as it came from college pro days and not

108 from the invitation-only NFL combine. In addition to combine metrics, the dataset included each player’s height,

109 weight, college, draft year, and draft pick (if applicable). The draft year and draft pick fields were NaN for undrafted

110 players. College football receiving statistics were compiled from the 1999 to 2023 through the Sports Reference

111 website. The chosen fields were total receptions, total yards, touchdowns and yards per game. This left us with 1152

112 data points out of which 170 (14.6%) data points did not have any recorded college stats on the Sports Reference

113 website.

Variable

Description calculated_forty

Draft class–ranked 40-yard dash time (lower raw time ranked higher) calculated_bench

Draft class–ranked bench press repetitions (higher repetitions ranked higher) calculated_vertical

Draft class–ranked vertical jump (higher jump ranked higher) calculated_broad_jump Draft class–ranked broad jump (higher jump ranked higher) calculated_cone

Draft class–ranked 3-cone drill time (lower time ranked higher) calculated_shuttle

Draft class–ranked shuttle run time (lower time ranked higher)

REC

Number of receptions in final college season

YDS

Total receiving yards in final college season

Y_R

Yards per reception in final college season

TD

Receiving touchdowns in final college season

Y_G

Receiving yards per game in final college season ht_inches

Player height in inches wt

Player weight in pounds conf_ACC

Indicator variable for Atlantic Coast Conference conf_Big 12

Indicator variable for Big 12 Conference conf_Big Ten

Indicator variable for Big Ten Conference conf_Other

Indicator variable for non–Power Five conferences or independent programs conf_Pac-12

Indicator variable for Pac-12 Conference conf_SEC

Indicator variable for Southeastern Conference

116 Table 1. Feature names and descriptions

## 117 Data Preparation

118 Before the creation of our models, the data was cleaned to remove all NaN values and dummy variables were 119 created. The dataset included a draft_ovr field, which specified the overall draft position for each player if they were 120 drafted and was otherwise missing (NaN). We created a binary classification target variable, is_drafted, by assigning 121 a value of 1 to players with a non-missing draft_ovr and 0 to those with a missing value. We used the 122 IterativeImputer from the scikit-learn library, which fits a Bayesian Ridge regression model to estimate and

123 iteratively fill in missing values. Each variable with missing data is modeled as a function of the other variables, and

124 the imputation process is repeated for several iterations to improve accuracy. We created one imputer for power and

125 explosiveness metrics (e.g., height, weight, bench press) and a separate one for speed/agility metrics (e.g., 40-yard

126 dash, 3-cone drill, shuttle run). While the 40-yard dash has high feature importance, only 63 (5.47%) players were

127 missing it and they were all from early years. The rest of the features we imputed had minimal feature importance

128 compared to the 40-yard dash. Since college reception stats had a high feature importance and there’s no logical

129 way to impute it, we decided to remove all records without college stats leaving us with 982 records being used in

130 the study. Additionally, for players that played multiple years in college before attending the combine, only their

131 most recent year of college before attending the combine was kept in the study to ensure consistency. For all metrics

132 except height and weight, we applied feature ranking to standardize values and ensure consistency across different

133 draft years. This approach accounts for evolving athletic standards over time and reduces model variance as different

134 features have different scales. For example, a player who recorded the fastest 40-yard dash in his draft class received

135 a score of 1 in the calculated_forty feature. This ranked value was used in place of the raw time to reflect the fact

136 that wide receivers have become increasingly athletic over the years, and prospects are ultimately evaluated relative

137 to others in their draft class—not across eras. The logic accounted for the fact that a greater value in some features is

138 beneficial while a smaller numerical value in other features is better. If two prospects tie, then they both receive that

139 ranking. Height and weight were not ranked due to there not being a census on the optimal ranges. Additionally,

140 height and weight are subjective and highly dependent on play style and scheme fit, so we thus avoided misleading

141 assumptions into the model. College reception stats were also not ranked because we removed many prospects who

142 attended the combine but did not have college receiving statistics available on Sports Reference, as doing so would

143 result in inflated rankings for those with data available that ignore prospects without data available and introduce

144 bias into the model. We created the dummy variables conf_ACC, conf_Big 12, conf_Big Ten, conf_Pac-12,

145 conf_SEC, and conf_Other which are a 0 if a player does not attend a school in that conference and a 1 if they attend

146 a school in that conference. Table 1 lists all feature names and their labels that were used in the study. Table 2 lists

147 the statistics for all the features used in this study.

Variable calculated_forty

Role INPUT

Mean

Standard

Non-missing Missing Min Median Max. Skewness Kurtosis

Dev.

.

23.32

14.09

0.23

-0.89

149 150 calculated_bench calculated_vertical calculated_broad_jump calculated_cone calculated_shuttle REC YDS Y_R TD Y_G ht_inches wt conf_ACC conf_Big 12 conf_Big Ten conf_Other conf_Pac-12 conf_SEC

INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT INPUT

Table 2. Feature statistics

23.46 23.37 23.32 23.49 23.51

56.9 826.4 14.73

6.73 70.17 72.67 200.99

0.1 0.1 0.13 0.36 0.12 0.19

13.91 14.01 13.91 13.94 13.85 25.06 360.4

3.15 4.16 27.57 2.25 15.04 0.31

0.3 0.33 0.48 0.33 0.39

0.22

-0.86

0.22

-0.88

0.24

-0.86

0.26

-0.85

0.22

-0.84

55 158

0.42

0.12

799.5 2060

0.27

-0.15

14.35 29.6

0.7

1.88

0.74

0.62

0 0.3

68.2 187.3

0.23

0.05

0 65

-0.23

-0.23

0 149

201 247

-0.12

-0.07

2.58

4.65

2.63

4.93

2.26

3.13

0.59

-1.65

2.28

3.19

1.62

0.62

## 151 Model Creation

152 In order to predict draft likelihood and draft position for those predicted to be drafted, we built two models, a 153 classification model and a regression model. For both models, we initially used LazyPredict to test multiple models 154 for their baseline performance, and those with the best results were chosen. We then performed hyperparameter 155 tuning with a grid search through the GridSearchCV class within scikit-learn. The final classifier selected was a 156 Gradient Boosted Decision Trees (GBDT) model, which significantly outperformed baseline models such as logistic 157 regression and Support Vector Machines (SVM). A GBDT classifier combines multiple decision trees into a single 158 model, where each tree is trained to be maximally correlated with the negative gradient of the loss function, 159 associated with the entire ensemble (Natekin & Knoll, 2013). The tree recursively partitions data to determine which 160 traits a player should have in order to have the best chance to be drafted. Trees are added sequentially, with each one 161 trained to correct the errors made by the ensemble learned so far. We use the default cross-entropy loss, which 162 optimizes probabilistic classification and is also used in logistic regression. To determine the success of the 163 classification model, we looked at validation accuracy with classifying players as drafter or not. We also evaluated

164 the F1 score which helps us understand how well the model balances precision (how many predicted drafted players 165 were correct) and recall (how many players were captured as drafted) (Vakili et al., 2020). This penalizes the model 166 if it is biased towards drafted players and fails to perform on the minority undrafted players in the data. The equation 167 is shown below where TP = true positives, FP = false positives, and FN = false negatives.

F1 Score

=

⋅

�

TP TP + FP

�

⋅

�

TP TP + FN

�

�

TP TP + FP

�

+

�

TP TP + FN

�

171 For our regression model, we used a CatBoost regressor to predict the draft order for prospects predicted to be

172 drafted. CatBoost outperforms other boosting implementations such as XGBoost and LightGBM due to its use of

173 ordered boosting, which prevents target leakage and prediction shift during training by ensuring that each model

174 update is based only on past data in a permutation of the training set. In addition, CatBoost handles categorical

175 variables natively through ordered target statistics, which convert categorical features into numeric values using

176 historical data, thereby avoiding leakage while supporting high-cardinality features. For each tree split, CatBoost

177 also constructs combinations of categorical features already used in previous splits, allowing the model to capture

178 higher-order interactions between variables (Prokhorenkova et al., 2019). We optimized the CatBoost model using

179 the Mean Absolute Error (MAE) loss function, which represents the average number of draft picks the model is off

180 by from the actual draft outcome. 𝑛𝑛

MAE = 𝑛𝑛 �|𝑦𝑦𝑖𝑖 − ���𝑦𝚤𝚤| 𝑖𝑖=1

184 We also used R² to assess the model and it explains the proportion of variance in draft position explained by the

185 model. An R² of 0 would indicate that our model is no better than predicting the mean draft pick for all players,

186 while an R² of 1 indicates perfect predictions. Since we use a nonlinear regressor (GBDT), R² still reflects the

187 proportion of variance explained, while MAE provides additional context on prediction error. Finally, we decided to

188 also use Spearman's rank correlation coefficient as it provided the correlation coefficient between the rankings of

189 draftable players versus their order of being drafted, and thus, is not as affected by the uneven distribution of picks

190 each round. The Spearman coefficient ranges from -1 to 1 and is used to measure any monotonic relationship

191 between variables that do not follow an approximately normal distribution (Rovetta, 2020). For example, in 2020,

192 while our model predicted Justin Jefferson to be drafted at 21.77 (retain decimals to evaluate model), he ended up

193 being drafted at 22. This would make the MAE 0.23 while Justin Jefferson would contribute 0.000724 to the

194 spearman coefficient as he was predicted to be the first WR drafted by the model but ended up being the 5th WR

195 taken in the 2020 draft while 51 total WRs attended the combine according to this formula: ρ

=

−

6 ∑ 𝑑𝑑�2�𝑖 𝑛𝑛(𝑛𝑛2 − 1)

## 199 Model Training and Evaluation

200 We used Leave-One-Season-Out Cross-Validation (LOSOCV), in which each season (2020, 2022, 2023, and 2024) 201 was held out once as a test set while the remaining seasons excluding 2021 were used for training. In each fold, both 202 the classifier and regressor were retrained using the same hyperparameters. Results were reported separately for 203 each season to assess year-by-year performance. This cross-validation strategy was chosen to account for changes in 204 prospects and drafting styles over time. It provided more consistent performance estimates compared to standard 205 train-test splits or splitting by seasons. The classifier was trained on all players in the training data. We plotted 206 validation accuracy against the number of estimators for the classifier to identify the optimal number of boosting 207 stages. However, to ensure proper evaluation of the regression model, the regressor was trained only on players who 208 were actually drafted in the training set. This avoided penalizing the regressor for classifier errors and ensured that 209 evaluation metrics such as Mean Absolute Error (MAE) and R² reflected only cases where a draft position existed. 210 Figure 1 shows how the model operates on unseen data. First, raw wide receiver data is cleaned and transformed 211 through feature engineering, then passed into a binary classifier to predict draft status. If the player is classified as 212 drafted, the data is further processed by a regression model to estimate their draft position.

213 Figure 1. Model Flowchart 9

214 215

## 216 Results

218 The results of the study are summarized in Table 3. For both the classifier and the regressor, 2024 was the best year 219 of performance for both models while 2023 was the worst year for the classifier, and 2020 was the worst year for the 220 regressor based on the MAE, R², and Spearman coefficient. According to PFF, the 2023 draft class did not feature a 221 standout receiver and none of the top three prospects were nearly as developed as those from previous years 222 (Monson, 2023). Notably, Jaxon Smith-Njigba, widely regarded as the second-best receiver in the class, was 223 predicted to go undrafted by our classifier. This likely occurred because he did not run the 40-yard dash at the NFL 224 Combine—his unofficial Pro Day time was not included in the dataset—and because he missed most of the 2022 225 season with a hamstring injury, recording only 5 receptions for 43 yards. As our model uses only final-season 226 statistics for consistency, this limited his feature data considerably. Additionally, the imputed 40-yard dash was 227 beneficial and prevented dumping lots of early-season data but was not perfect even though it was based on other 228 speed/agility metrics. No solid evidence was found for the weak regressor performance in 2020. However, the strong 229 performance for both models in 2024 is likely due to the 2024 draft class being one of the strongest in the last 230 decade, but predicting draft position has more confounding variables compared to predicting whether a player is 231 drafted or not (Sikkema, 2024). While the regressor occasionally misranks individual players compared to other 232 mock drafts, it consistently succeeds in distinguishing between early- and late-round prospects. For instance, the 233 model’s top predicted wide receiver prospects in order were Brian Thomas, Xavier Legette, Malik Nabers, Rome 234 Odunze, Troy Franklin, and Marvin Harrison Jr. Another interesting player was George Pickens, who tore his ACL 235 in 2021 and missed most of his junior season, and finished with only 5 receptions for 107 yards after returning for 236 the latter part of the season. He was predicted to be drafted at 115.76 by our model and was ranked as the 21st best 237 receiver by our model, but he ended up being picked at 52 by the Pittsburgh Steelers as the 11th WR taken in his 238 class. This discrepancy highlights several limitations in using purely performance and combine data for draft 239 prediction. For Pickens, both behavior concerns and his ACL tear contributed to a wide range of team evaluations. 240 According to Bachar (n.d.), at least one NFL team removed Pickens from their draft board due to concerns about his

241 behavior during a pre-draft visit. Despite these concerns, the Steelers were willing to draft him and overlook his 242 injury history and other pre-draft concerns, valuing his high upside as a prospect. While the model penalized him for 243 lack of recent production, it couldn’t account for team-specific evaluations of his character, which can vary from 244 team to team.

## 246 Year

Classifier

Classifier F1

Accuracy

Score

2020 0.8431

0.8824

2022 0.8056

0.8727

2023 0.6042

0.6667

2024 0.8919

0.9355

Avg 0.7862

0.8393

247 248 Table 3. Model results 249 250

## 251 Discussion and conclusion

MAE on Drafted 66.80 52.26 55.15 49.18 55.85

R² on Drafted -0.0037 0.1635 0.1303 0.3233 0.1533

Spearman ρ

0.3006 0.4200 0.3562 0.6262 0.4257

252 Figure 2. Feature Importance 253

254 Our two-stage modeling approach showed that predicting whether a WR gets drafted or not with a high level of 255 accuracy is possible and predicting the exact draft slot is also possible, but much harder to do and is easily affected 256 by outlying variables. The classifier achieved high accuracy across seasons, especially in 2024, indicating strong 257 ability to identify whether a WR would be drafted. The regressor being able to predict the predict the overall draft 258 position of a player within 49.18 picks indicate that for prospects with no anomalies in college or in the combine, 259 predicting their draft round within 2 rounds is possible. Further tuning of the data, such as removing players who 260 were injured in their final season, and more data for more recent years with less missing data could lead both models 261 to become significantly more accurate and can offer an can offer an unbiased, statistical ranking of WRs, free from 262 media or player hype. According to Figure 2, the 40-yard dash was the most important predictor for both models, 263 followed by college touchdowns. Both models’ reliance on college statistics and combine measures and not being 264 able to quantify features like injury history, pre-draft interviews, and play style/team fit make the model weaker and 265 show the problems associated with a purely-data approach. Regression is also a much harder task as it is impacted 266 by team needs, position depth, and off-field behavior, which is unquantifiable. For this reason, the Spearman 267 coefficient tells a different story: while the predicted draft positions may not always be numerically close, the 268 overall ranking of receivers produced by our regressor was similar to the true draft order. Our average Spearman 269 coefficient of 0.4257 suggests a moderate correlation between the actual draft order of WRs and the order predicted 270 by our model. Unlike MAE which penalizes large errors and punishes predictions off by a few rounds, the Spearman 271 shows relative rankings of receivers and is useful when picks aren’t as important. Teams in need of a receiver want 272 baseline rankings for prospects, and can further do research on prospects based on the non-biased rankings of the 273 model. They can also use the regressor’s predicted draft slot for a player to gauge where they end up being drafted, 274 and can use this to trade up in order to secure the player. Prospects looking to boost their stock can also refer to the 275 feature importance rankings to identify which areas of performance matter most and where to focus their 276 improvement. Ideally, reducing the MAE to within one round (MAE ≤ 32), or even lower, would make the 277 predictions more practical. For example, misclassifying a WR3 as the WR6 might yield an MAE of 50 or 60, but the 278 relative ranking of the prospect is still informative—especially considering that 50+ wide receivers typically attend 279 the combine. This level of approximation can still provide meaningful value to NFL front offices during draft

280 evaluations. Potential areas of improvement for the model include using Natural Language Processing (NLP) to gain

281 sentiment analysis on prospects, although this would only really be effective for the top prospects and could

282 overshadow those from smaller schools. Using multiple years of college reception data for players who have it can

283 also be useful, especially for players that ended up being injured or had minimal production in their final season of

284 college football. Additionally, grading each NFL team on their need for wide receivers in a given draft class based

285 on roster depth could improve the regressor’s ability to predict actual pick order by accounting for team-specific

286 drafting behavior. This approach can be applied to other positions in the NFL but may be more difficult due to the

287 lesser importance given to the combine and greater emphasis on intangibles for positions other than WR. It can also

288 be applied for predicting draft outcomes in other sports. Still, this methodology holds promise for broader draft

289 analysis in football and other sports.

## 291 Acknowledgements

292 293 I would like to acknowledge Prasad Sharanabasawa for his invaluable opinions and guidance throughout the course

294 of this project.

## 296 References

297 298 Bachar, Z. (n.d.). George Pickens Reportedly Was Removed from Multiple NFL Teams’ Draft Boards in 2022.

Retrieved June 28, 2025, from https://bleacherreport.com/articles/25194649-george-pickens-reportedlywas-removed-multiple-nfl-teams-draft-boards-2022

301 Baker, R. E., & Kwartler, T. (2015). Sport Analytics: Using Open Source Logistic Regression Software to Classify

Upcoming Play Type in the NFL. Journal of Applied Sport Management, 7(2). https://doi.org/10.7290/jasm07c14e

304 Clark, T. K., Johnson, A. W., & Stimpson, A. J. (2013). Going for Three: Predicting the Likelihood of Field Goal

Success with Logistic Regression.

306 Dhar, A. (n.d.). Drafting NFL Wide Receivers: Hit or Miss. 307 Gifford, M., & Bayrak, T. (2023). A predictive analytics model for forecasting outcomes in the National Football

League games using decision tree and logistic regression. Decision Analytics Journal, 8, 100296. https://doi.org/10.1016/j.dajour.2023.100296

310 Monson, S. (2023, April 4). 2023 NFL Draft Rankings: Sam Monson’s top 15 wide receivers, including USC’s

Jordan Addison at No. 1. PFF. https://www.pff.com/news/draft-2023-nfl-draft-wide-receiver-rankings-sammonson-jordan-addison-jaxon-smith-njigba-quentin-johnston

313 Mulholland, J., & Jensen, S. T. (2014). Predicting the draft and career success of tight ends in the National Football

League. Journal of Quantitative Analysis in Sports, 10(4). https://doi.org/10.1515/jqas-2013-0134

315 Natekin, A., & Knoll, A. (2013). Gradient boosting machines, a tutorial. Frontiers in Neurorobotics, 7. https://doi.org/10.3389/fnbot.2013.00021

317 Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2019). CatBoost: Unbiased boosting with categorical features (No. arXiv:1706.09516). arXiv. https://doi.org/10.48550/arXiv.1706.09516

319 Rovetta, A. (2020). Raiders of the Lost Correlation: A Guide on Using Pearson and Spearman Coefficients to Detect

Hidden Correlations in Medical Sciences. Cureus. https://doi.org/10.7759/cureus.11794

321 Sikkema, T. (2024, April 22). 2024 NFL Draft Position Rankings: Wide receivers. PFF. https://www.pff.com/news/draft-2024-nfl-draft-position-rankings-wide-receivers

323 Taylor, C. (n.d.). Deep Learning for In-Game NFL Predictions.

324 Teich, B., Lutz, R., & Kassarnig, V. (2016). NFL Play Prediction (Version 1). arXiv. https://doi.org/10.48550/ARXIV.1601.00574

326 Vakili, M., Ghamsari, M., & Rezaei, M. (2020). Performance Analysis and Comparison of Machine and Deep

Learning Algorithms for IoT Data Classification (No. arXiv:2001.09636). arXiv. https://doi.org/10.48550/arXiv.2001.09636
