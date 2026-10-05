<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Using Injury-Risk Forecasting to Quantify Financial Impact in the NBA - Wang.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/using-injury-risk-forecasting-to-quantify-financial-impact-in-the-nba/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Ethan Wang -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

## 1 Using Injury-Risk Forecasting to Quantify

Financial Impact in the NBA

Ethan Wang

## 5 Abstract

Injuries in the NBA have become consequential not only for team success but for the financial

7 costs those teams suffer. This study develops a machine learning framework that predicts next-game

8 injury risk using publicly available box-score data, player attributes, and injury history, then translates

9 these probabilities into expected financial costs. Combining five datasets from 2010-2022, I derived

10 sixteen workload and recency features and trained a Random Forest model optimized with five-fold

11 cross-validation. At a 2% threshold for classification, the model predicts out-of-sample 69% of injuries

12 while correctly ruling out 62% of healthy games, indicating better-than-chance predictive power is

13 possible using solely public data. Feature-importance analysis identified workload shifts and rest as

14 primary predictors. Extending beyond prediction, this study gives a new way to interpret the financial

15 implications of injuries, looking at how strategic rest decisions can minimize financial loss. This study

16 offers NBA organizations a data-driven tool linking injury prevention with financial optimization,

17 bridging injury forecasting with economic decision-making.

18 1. Introduction

Injuries have been a longstanding problem in all of sports, but in the NBA their impact stands

20 out dramatically. With smaller rosters and superstars carrying a tremendous share of responsibility, the

21 loss of one player can upend an entire season. Unlike football or baseball, where depth and roster size

22 provide cushion for absences, a single injury to a team can swing playoff odds, alter franchise direction,

23 and dramatically weaken league ratings. In the 2024 NBA season, for instance, teams like the 76ers

24 and Pelicans were hit particularly hard with injuries and saw their postseason hopes vanish. These

25 losses don’t just hurt on-the-court performance, but can wreck teams financially, with over $350

26 million being spent on injury-related costs throughout an NBA season (Smith, 2016). Over time, staying

27 ahead of NBA injuries isn’t just about player health and safety, it’s the key to a competitive edge

28 against others.

In the past, teams have approached injury prevention rigorously, using machine learning to

30 analyze both publicly available data, like game statistics, along with data from wearable technologies,

31 like heart rate or step count (Dowsett, 2022). While prior research on forecasting injuries using machine

32 learning models have focused primarily on identifying injury odds, this study extends that work by

33 translating predicted injury probabilities into expected financial costs, giving teams a quantitative

34 framework to assess health and monetary risk. In doing so, this research connects performance

35 analytics with financial optimization, an area largely unexplored in current sports injury-forecasting

36 literature.

I set out to answer a practical question for NBA front offices: Can a machine learning model

38 that combines regular box-score data, and player attributes effectively predict whether a player will

39 miss the next game with an injury– and if so, how can these predictions be used to estimate the financial

40 cost of injuries to NBA teams? To do this, I merged five public datasets (injury logs 2010-2022, game-

41 level box scores with minutes played, season-level box score and player attribute descriptions, team-

42 level box scores per game, and player salaries) into a dataset where each observation is unique to a

43 game-player. I engineered and derived 16 workload and recency metrics, treated missing values, and

44 trained a Random Forest classifier for predicting injuries. To optimize my model, I utilized five-fold

45 cross-validation to guide hyper-parameter tuning and performance estimation.

To preview my results, I found that simple box score data can be useful for successfully

47 predicting injuries. The model predicts 69% of injuries while correctly ruling out 62% of healthy

48 games. In practice, this means I can generate early warnings for over two-thirds of forthcoming

49 injuries, giving teams a powerful tool to minimize injury odds. Additionally, using the model’s logit

50 injury probabilities, I demonstrate a framework to give teams financial insight into the benefits of

51 resting players who are at high risk of injury, and show that this can be used to save upwards of $5.7M

52 across teams in the NBA if optimized.

54 1.1 Literature Review

In the past, several studies have researched injury prediction in professional basketball. Cohan,

56 Schuster, and Fernandez (2021) forecasted injuries using a deep learning model with injury history and

57 game activity logs. They found that their model can learn to create meaningful features as a

58 combination of raw features to predict injuries. In doing so, their model achieved 93.4% accuracy, with

59 a Receiver Operating Characteristic (ROC) Area Under the Curve (AUC) of 0.80. Their research

60 highlights the severe class imbalance within injury datasets, noting that a model predicting every case

61 as a non-injury would still achieve approximately 98% accuracy. Charest et al. (2021) studied the

62 effect of distance and direction of back-to-back games in the NBA, ultimately finding that specific

63 travel patterns worsen recovery and performance. Although my study doesn’t include travel distance

64 between games, I do consider related metrics, such as days in between games or back-to-back games–

65 measured by the rest variable. Lu et al. (2022) focused on analyzing lower-extremity muscle strains

66 (LEMSs) within NBA injuries from 1999 to 2019. They compared performance across different

67 classification models trained on NBA injury data, finding that the best predicting machine learning

68 algorithm for predicting LEMs was XGBoost. They identified that pre-existing injury history helped

69 best predict LEMs. Chan et. al (2024) conducted a systematic review on the relationship between

70 workload spikes and injury risk. Accumulating evidence over 11 studies, they found that training load

71 was correlated with injury risk, highlighting the importance of including workload variables inside ML

72 prediction models.

While Charest et al. (2021) and Lu et al. (2022) looked at specific drivers of injury, my research

74 utilizes a wide array of publicly available data for injury prediction, similar to Cohan et al. (2021).

75 Unlike prior studies, however, my study extends beyond prediction to include a cost-related threshold

76 evaluation that weighs the consequences between false positives and false negatives. Additionally, I

77 use an expected cost framework to identify the financial burden of player injuries, giving new insights

78 into the economic dimension of injury prediction.

80 2. Material

This study utilizes multiple publicly available datasets from Kaggle to conduct the analysis.

82 Together, these sources provide injury history, player-level workload, anthropometric information,

83 and team-level game context.

85 2.1 Injuries Dataset

This study uses the nba-injuries dataset from Kaggle (Hopkins, 2018). The dataset consists

87 of public injury reports and game summaries, covering detailed information about player injuries

88 across ten NBA seasons (2010–2020). The dataset includes fields like the date of the injury, the

89 player who got injured, and the type of injury. This dataset is the foundation for the injury

90 prediction variable in the study. Using this dataset, I identified who was injured and the type of

91 injury that was suffered. In Figure 1, I show the five most frequent injuries reported in the dataset.

92 Because the majority of these injuries are reported as “unknown” type, I constructed a binary injury

93 label that groups all injuries together (i.e. “injury next game: yes/no”). For more details about

94 “known” injury types, see Figure S1 where I sort known injuries by frequency and severity.

Figure 1: Top 5 most frequent injuries within dataset

97 98

Certain types of injury labels are outside the scope of my prediction model: illness and

100 infection, health and safety protocols, load-management and conditioning, personal, legal, and

101 administrative (considered to be injuries because they are still logged on the IL). Therefore I do

102 not include them as injuries in forecasting. If a player has an injury detail that corresponds to the

103 following values, the injury indicator will be counted as 0, instead of 1. I decided against dropping

104 them from the dataset, because they still provide useful game-level information and help preserve

105 the continuity of player records. The study acknowledges that this means there will be significantly

106 more non-injuries than injuries in the dataset, and will talk about this in the limitations section.

108 2.2 Team Statistics by Game and Season Dataset

The NBA Traditional Stats dataset from Kaggle compiles team-level box score statistics

110 across multiple NBA seasons (Jóźwiak, 2024). For this study, I used the final team scores for each

111 game to craft close game indicators in each game. The purpose of this feature was to capture game

112 intensity, under the hypothesis that players who regularly play in tightly competitive games may

113 have higher physical stress and therefore a higher injury risk.

115 2.3 Player Attributes

The NBA players dataset from Kaggle contains biometric, biographic, and basic box score

117 data from 1996 to 2022 (Cirtautas, 2023). I use variables such as height, weight, and season

118 averages per player to look at whether player attributes change injury likelihood odds.

119 2.4 Player Stats

The NBA Game Details dataset is a player-level dataset that contains useful box-score

121 related metrics (Lauga, 2020). From this dataset, I use the “minutes played” variable, which is the

122 minutes and seconds that a player plays per NBA game. I used the minutes played to construct the

123 following features: (1) avg. minutes (last 5 games), (2) change in minutes since last game, (3) avg.

124 high minute streak (last 20) and (4) high minute games in the last 20. Avg. minutes (last 5 games)

125 measures the mean amount of games in a player’s last five games, which provides a short term

126 glimpse of a player’s recent playing time. Change in minutes since the last game provides an

127 understanding of how a player’s current game compares to the last game, with sudden workload

128 changes having a dramatic impact on injury odds. Avg. high minute streak (last 20) measures the

129 average length of consecutive-game stretches, within a player’s last 20 games, where they played

130 heavy minutes (above 35 minutes). In other words, it provides an understanding of how often and

131 how long a player sustains extended workloads without a break, highlighting patterns of

132 accumulated risk. High minute games in the last 20 reflects how much games in a player’s 20 most

133 recent games are of heavy minutes (above 35 minutes). All of these variables potentially signal

134 workload spikes which may impact risk of injury.

136 2.5 Player Salary

The NBA Player Stats and Salaries 2010-2025 dataset is a player-level dataset that

138 contains both box-score data and details on a player’s salary (Ratin21, 2025). From this dataset, I

139 will be extracting the salaries for an understanding of the financial cost of injuries. The

140 distribution of player salaries in the NBA is skewed right, with the league minimum being the

8 141 lowest possible salary and super-max contracts being some of the highest. Throughout the years, 142 contracts have progressively climbed because of the increase in salary cap and inflation. 143

144 3. Preprocessing the Datasets

145 3.1 Merging the Datasets for Modeling

To construct the dataset that my model uses, I merged across all previous datasets by

147 player-game.

149 3.2 Feature Engineering in The Merged Dataset

An indicator for close basketball games is included to measure how game intensity may

151 affect injury odds. If a game is closer, is the player playing harder? Could this put a higher demand

152 on their body? To add an indicator for close games, I have to consider multiple factors. The NBA

153 considers a close game as a game where the point differential is confined within a 10 point margin

154 before the start of the fourth quarter and narrows down to a 5 point or less disparity at the end of

155 the game. For the sake of simplicity and because I don’t have access to the score of the game at

156 the start of the fourth quarter, I will be considering close games as games with a point differential

157 of 5 points or less by the end.

I used minutes played and prior player performance statistics to engineer a series of

159 workload and recency variables. First, I created binary indicators for high-minute games (>30

160 minutes) and mid-minute games (>23 minutes), and then calculated streaks of consecutive

161 occurrences in each respective category. From there, I calculated rolling metrics over a player’s 162 last 20 and last 5 games, including the number and average length of high- and mid-minute streaks 163 within trailing games. I also added short-term features that capture workload and recovery such as 164 change in minutes since last game, days of rest, and days since last injury. To observe a given 165 player’s injury history, I included season-to-date injury counts and total career injuries. Finally, I 166 incorporated previous-season averages (rebounds, 3-point attempts, free-throw attempts, and 167 minutes) to provide an understanding of player tendencies. 168

169 3.3 Cleaning the Datasets for NA and Filling in Values

Some features contained missing values, which could interfere with the quality of my

171 modeling fits. I resolved these missing values in the following ways:

## 1. Categorical

fields.

The final dataset contains a variable called Relinquished. In the context of my study, this is a team transferring a player to the injured list. In games where no player is transferred,

Relinquished cannot be meaningfully interpreted; therefore I replaced NA entries in

Relinquished with the string “unknown”.

2. Numerical box-score statistics and recovery metrics (mean imputation).

16% (22631/140879) of my observations had NA values in box-score related statistics., because omitting NA values in the dataset for box-score statistics leads to significant data loss, for conventional game-level performance figures–e.g., three-point and free-throw counts and percentages, rebounds, and the rest variable–I first used each player’s own seasonal mean wherever at least one non-missing value existed. If an athlete had no observed data in a given column, I substituted the league-wide mean. Following common practice in sports workload analysis (see Benson et al., 2021), I used each player’s seasonal mean wherever a non-missing value existed; if none existed, I substituted the league-wide mean. For missing age values, I first looked for if the player had any previous existing age in other years, and attempted to use the difference in seasons as either an addition or subtraction to calculate a missing age value. If the player didn’t have any preexisting age values in the dataset, I used the overall mean.

3. Streak, recency, and workload indicators (median imputation).

Variables that are inherently skewed–such as streak magnitudes (Last high‑minute streak length, Avg. high‑minute streak (last 20), etc.), workload counts (High‑minute games in last 20, Avg. minutes (last 5 games)), and recency measures (Days since last injury)–were imputed with the within-player median to mitigate the influence of outliers. This approach is described as appropriate for skewed data (Mohammed et al., 2021). As with the mean strategy above, I fell back on the overall-sample median only when a player was missing all previous values.

199 3.4 Final Dataset

The final dataset contains 21 total variables, where each observation is identified by a

201 unique game-player. See Table 1 for details. The data spans from 2012 to 2023 and includes 8253

202 unique games and 1211 unique players. On average, players played 20.14 minutes per game (SD

203 = 12.60), with an injury rate of 0.03 (SD = 0.17). Players typically had around 16 games of rest

204 between games (SD= 56.34), with a total of 9151 games where a player played on a back-to-back

205 (one day of rest). While the dataset’s mean rest time is 16 days, this value is skewed by the

206 significant number of low-minute or inactive players (as seen by the median of 4). The typical

207 number of days separating a player and his last injury is 254.49 (SD = 312.23).

Table 1: Descriptive Statistics

12 211

212 4. Method

I modeled injury risk using a Random Forest classifier (RF) coupled with 5-fold cross-

214 validation. The RF method was preferred for three reasons. First, it can predict injuries with a non-

215 linear interaction that is highly dependent on multiple complex factors, such as workloads, player

216 playstyle tendencies from previous season averages, and player attributes. Second, because each

217 tree only considers a random subset of variables in each split, the model helps lessen the impact

218 of highly correlated variables and reduces over-fitting. Third, the model allows for easy post-hoc

219 interpretability. More specifically, the algorithm enables the computation of Gini-based

220 importance scores allowing us to identify pertinent metrics.

Model assessment and parameter tuning were done using 5-fold cross-validation. The data

222 was stratified into five subsets, with four out of the five subsets being used as training data, and

223 one out of five subsets used as testing data. I repeated this five times for five different subset

224 combinations and checked confusion matrix results to ensure that my results are robust and

225 generalize to different test samples.

The Random Forest Model is a machine learning model that makes predictions by

227 combining many small decision trees. Each tree looks at a random portion of the data and different

228 player statistics, adopting its own pattern of when injuries occur. The model then averages all the

229 tree's predictions to make one overall injury probability. This approach is useful as it helps capture

230 complex patterns while avoiding overfitting to any single part of the data.

This study implements the RF model using the “randomForest” package in R.

232 Hyperparameters within the function include the following: ntree, mtry, nodesize, maxnodes,

233 replace, sampsize, and classwt among others.

The number of trees (ntree) was fixed at 500, consistent with the default in R’s

235 randomForest package. As noted by Breiman (2001), the generalization error of a random forest

236 converges as the number of trees increases, and Liaw & Wiener (2002) observe that the out-of-

237 bag error stabilises once ‘enough trees’ are grown. Thus, 500 trees was chosen because it provides

238 model stability without excessive computational cost.

The mtry parameter controls the amount of variables that are considered at each split. A

240 smaller value increases the diversity among the trees but weakens the individual trees, while a

241 larger value reduces bias but risks high correlation. In section 5.1, mtry is fitted by maximizing

242 the area under the ROC curve.

I chose the default values (nodesize= 1; maxnodes= NULL) for the trees, allowing them to

244 be grown to full depth. This setting minimizes bias and allows trees within the RF model to capture

245 complex interactions. Higher nodesize or lower maxnodes values would have restricted tree depth,

246 leading to higher bias but lower variance among the trees.

Bootstrap sampling parameters were also set to their default values (replace = TRUE; samp

248 size = n). This allows for each tree in the RF to be trained on a more diverse dataset created by

249 random sampling with replacement. The result lowers variance and reduces overfitting once the

250 trees are averaged.

Class weights in the Random Forest model were set to the default value (classwt = NULL),

252 which weighed both injuries and non-injuries as equal. While class weighting is useful in

253 addressing imbalanced outcomes by penalizing misclassification of injuries more heavily, I chose

254 to handle imbalance through threshold tuning. Doing this allowed me to directly control the trade-

255 off between false-positives and false-negatives to reflect the practical costs of missed injuries vs

256 false alarms.

Threshold is the final classification layer of the RF model. Prior to this layer, my RF model

258 generates a logit (or “probability”) of getting injured in the next game. The threshold converts this

259 logit into a binary classification (“yes/no”). Lower thresholds (close to 0) mean that most logits

260 will be classified as “yes”, while higher thresholds (close to 1) classify most logits as “no”. Section

261 5.2 details the process for which the threshold is fitted.

263 5. Results

The goal of this study is to develop a machine learning framework that predicts next-game

265 injury risk using publicly available data, then translate these probabilities into expected financial

266 costs. To accomplish this, the result section follows four steps: (1) tune and validate the model to

267 make sure it works beyond chance, (2) pick a decision threshold that balances the false positives

268 and false negatives based on cost, (3) show the out-of-sample performance of the model at that

269 optimal threshold, (4) identify which features matter most for predicting injuries, and (5) use injury

270 probabilities to generate an understanding of financial risk.

272 5.1 Parameter Tuning

To tune the random forest’s mtry hyperparameter, I fixed mtry to values between 1 and 16

274 (the total number of variables that are used for prediction) and computed ROC points across a grid

275 of decision thresholds for each fold of a 5-fold cross-validation. The thresholds were 0.9, 0.5, 0.15,

276 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.007, 0.005, 0.003, and 0.001. As the

277 threshold decreases toward 0, both the true-positive rate (TPR) and false-positive rate (FPR)

278 increase, ultimately tracing out the ROC relationship (see Figure 2A).

For each fold, I recorded FPR and TPR at every threshold, then averaged these across the

280 five-folds to obtain an average ROC curve (Figure 2A, black line). I included a 45° reference line

281 to represent random chance. Because the average ROC curve sits well above this chance line, the

282 model performs better than random classification of injuries.

To identify the optimal mtry value for the random forest model, I approximated the area

284 under the average ROC curve (AUC) for every value of mtry and selected the value that produced

285 the highest value (Figure 2B, red line). I estimated the AUC by summing the true positive rates

286 (TPR) across all thresholds, as the AUC represents the model’s overall ability to distinguish

287 between injured and non-injured players. A higher AUC indicates stronger class separation

288 (injuries from non-injuries). Among all possible configurations, the model with mtry = 16 achieved

289 the highest approximate AUC of 8.087, slightly outperforming other values of mtry (2nd best mtry

290 = 14, AUC = 8.078; 3rd best mtry = 13, AUC = 8.077).

292 5.2 Threshold Testing

To determine which threshold minimizes cost, I first define a cost ratio between false

294 negatives and false positives. Then, I plot an estimated cost score based on three cost ratios (0.5,

295 1, 1.5) in three different colors against different thresholds from 0 to 0.9 (see Figure 2C). Cost

296 ratio, c, is defined as c = cost of a FN (false negative) / cost of a FP (false positive).

When c < 1, false negatives are being weighed as less than false positives. At a c = 1, false

299 negatives and false positives are viewed equally, while c > 1 implies that a false negative is viewed

300 as more costly than a false positive. The true cost ratio will vary by team, player, and contract.

301 Therefore, I report results at c = 1, as a neutral expected-value baseline that does not include

302 unverified cost-related assumptions, but my methodology is robust to any cost ratio. For a cost

303 ratio of 1, the threshold that minimizes cost is 0.02 (minimum of green line in Figure 2C).

Figure 2: Model performance evaluation for the Random Forest classifier

306 (A) ROC curves averaged across folds for mtry = 16, (B) area under the ROC (AROC) across mtry

307 values, and (C) cost–threshold curves illustrating false-negative/false-positive trade-offs.

308 309

310 311 312

313 5.3 Optimal Model and Feature Importance

In Table 2, I present the confusion matrix for my model. At a conservative 2% threshold, I

315 predicted 69% of true, out-of-sample, injuries while correctly ruling out 63% of healthy games. In

316 practice, this means I can generate early warnings for roughly two thirds of forthcoming injuries,

317 giving teams a tool to minimize injury odds.

Table 2. Confusion matrix

320 Means and standard errors (in parentheses) across 5 folds. Accuracy and proportion correct in grey.

Actual

Predicted

13577.20

(41.32)

182.60 (8.89)

0.99

8160.00

(47.13)

400.20 (7.55)

0.05

0.62

0.69

Accuracy 329

0.63

After training the Random Forest model, I examined which variables most strongly

333 influenced injury prediction through their feature importance score. A feature importance score

334 measures how much a variable contributes to reducing impurity or how well a variable helps the

335 model separate injured from non-injured players. High scores mean the feature was more useful

336 for making cleaner splits between injuries vs non-injuries. Feature importance scores (Gini gain)

337 ranked the following predictors as the most important predictors, in the following order: change

338 in minutes since last game, average minutes in the last 5 games, days since last injury, and rest.

339 The following variables were the least predictive of injury: age, number of high minutes played

340 (games above 30 minutes played) in the last 20 games, player height, and number of injuries

341 previously in the season.

The results are intuitive: players who have a sudden change in minutes compared to their

343 last game, have suffered an injury recently, have a recency in the last 5 games of playing a

344 significant amount of time, and aren’t well rested have a higher injury risk. Specifically, players

345 with more rest have significantly lower injury odds compared to those on 0-5 days of rest. Most

346 injuries tend to happen on short amounts of rest, while long rests minimize injury chances, as

347 expected. Contrary to my expectations, physical attributes, like age and a player’s height, were not

348 particularly useful to the model. This is inconsistent with previous findings such as Lu et al. (2022),

349 where age was a driving factor in the predictions.

For days since the player’s last injury, I find that players who re-injure tend to have had

351 less time since their previous injury. I find that for a player’s change in minutes since their previous

352 game, a small increase in minutes is a mild risk amplifier, while extreme shifts either more or less

353 are red flags. For the variable encoding the average number of minutes played in the last five

354 games for a player, I found that the majority of injuries happened above the 20 minute zone, and

355 injury risk slowly increased until it peaked at around 30 minutes. Like the rest of the top 4

356 predictors, injuries also happen frequently under 20 minutes, which suggests that Avg. minutes

357 (last 5 games) is most powerful in combination with other predictors, and not a standalone

358 predictor.

Figure 3: Feature importance score for variables within the model

362 5.4 Expected Cost and Salary Analysis

While previous studies have looked at forecasting injury probabilities using box-score

364 related data, they have all stopped at predicting who is likely to get injured, without examining the

365 financial consequences of those injuries. Utilizing salaries, and the predicted probabilities of

366 injuries generated in the Random Forest Model, I construct a method for calculating expected cost:

E[Cost] = P(injury) x (salary ÷ 82) x (average duration of injury)

Here P(injury) is the model’s predicted probability of an injury, and salary/82 represents

371 the player’s per game salary, assuming an 82 game regular season. The average duration of injury

372 is calculated as the mean number of games typically missed per injury. This calculation ultimately

373 allows for a per-game estimation of a player’s financial risk on the team. Figure 4A shows an

374 example team (New Orleans, 2018), where each player’s expected injury cost fluctuates

375 throughout the season based on model predictions.

To complement this estimate, I calculate the actual financial cost of injury by multiplying

377 the number of games missed after each injury by the player’s per-game salary. This allows for a

378 direct comparison between the expected and realized financial losses. Expected cost values were

379 derived from the model’s predicted probability of injury for each player, multiplied by their per-

380 game salary and the average duration of injury. Figure 4B plots expected versus actual financial

381 costs, showing a high degree of correlation between the model’s expected cost and real financial

382 outcomes (r = 0.955). Figure 4C shows the aggregated total expected costs by team and season.

383 Expected cost has gone up throughout the years as a result of inflationary changes of salary. All

384 together, these analyses demonstrate how injury prediction models can be used to estimate

385 financial risk to a team.

Figure 4: Expected and realized injury-related financial costs

390 (A) Player-level expected cost heatmap for New Orleans (2018), (B) correlation between expected

391 and actual team-level financial losses, and (C) league-wide expected injury costs over time (2012–

392 2022).

393 394 395 396 397 398

399 400 401 402 403 404 405

24 406

407 5.5 League-Wide Injury Cost Simulations

To explore the potential value of rest, I simulated a scenario in which high-risk players

409 were rested before their next games. In this scenario, I selected a threshold that would be

410 considered risky, and determined the days between the player's current game and the next team

411 game that he could participate in (within the season). To demonstrate how to calculate league-wide

412 costs, I selected a risky threshold at 0.10 and carried out cost-analysis. This selection is arbitrary,

413 but it allows teams to take on a relatively high level of injury risk tolerance.

Building on this, I simulated the effect of resting players exceeding the threshold, rather

415 than letting them play the next game. Specifically, I increased each player’s rest and days since

416 last injury variables by the number of days between the current and next game.

I then applied the previously developed Random Forest model using these updated

418 variables to generate new injury probabilities. Using these revised probabilities, I recalculated each

419 player’s expected injury cost. Comparing the new expected costs to my original estimates allowed

420 me to quantify the financial effect of resting high-risk players for one game.

Table 2 presents the financial outcomes of this simulation. Across multiple seasons, I show

422 original estimates (Expected Cost Before), new estimates with simulated rest (Expected Cost

423 Updated), and the total savings from simulated rest across all teams in the NBA (League Wide

424 Savings). Positive League Wide Savings indicates cost savings from avoided injuries, while

425 negative League Wide Savings would indicate losses due to unnecessary rest. Note that League

426 Wide Savings is positive for every season between 2012 and 2023, and achieves a maximum of

427 approximately $5.7M in 2021. This estimate is also conservative, as 9,551 observations in the

428 dataset lack salary information, meaning true savings are likely even higher.

This framework can be extended to evaluate the effects of giving players multiple games

430 of rest, allowing for estimation of optimal rest durations. Alternatively, it can be coupled with

431 additional metrics related to the contribution of a player to each game, allowing teams to weigh

432 the cost-benefit of resting a high-injury-risk player.

Table 2: Expected financial savings of simulated rest

436 437

## 438 Discussion

This study set out to answer a practical question for NBA front offices: Can a machine

440 learning model that combines publicly available data be used to not only forecast player injuries,

441 but also to estimate their financial impact?

To answer this, I merged five public datasets (injury logs 2010-2022, game-level box

443 scores with minutes played, player salary details by season, season-level box score and player

444 attribute descriptions, and team-level box scores per game) into a single game, individual player

445 based dataset. I engineered and derived 16 workload and recency metrics, treated missing values,

446 and trained a Random Forest classifier for predicting injuries. To optimize the model, I utilized 5-

447 fold cross-validation to guide hyper-parameter tuning (mtry testing 1-16, threshold testing) and

448 tested the model out-of-sample for performance estimation.

My results show that simple box score data can predict injuries with above-chance

450 accuracy. At a 2% threshold, the model predicted around 69% of true injuries out-of-sample, while

451 ruling out 62% of healthy games, suggesting that my model can offer teams early warnings for

452 most upcoming injuries well above chance. Beyond predictive accuracy, the integration of

453 financial risk modeling introduces a novel extension of injury forecasting. Across seasons,

454 expected injury-related costs showed steady inflation from $53.1M in 2012 to $471.1M in 2022,

455 closely aligning with the model’s updated estimates after rest simulation. On average, resting

456 players above the injury-risk threshold produced league-wide savings each year, peaking at

457 $5.75M in 2021 (Table 2). By translating injury probabilities into salary-adjusted costs, my

458 analysis offers teams a quantitative framework for managing both player health and financial cost.

## 461 Feature Interpretation

Because the dataset only had a small proportion of injuries, the accuracy of the model

463 exceeded my expectations. Since I decided on a lower injury threshold (0.02), I accepted a high

464 number of false positives in exchange for identifying more true injuries. The average across five-

465 folds yielded a 63% specificity (TN/(TN+FP)) and 69% sensitivity (TP/(TP+FN)). The top

466 features in my model illustrate that changes in player workload and recovery dynamics are key

467 drivers of injury likelihood. Any spikes in last game minute change are red flags for injury

468 likelihood. The amount of days since the players’ last injury is also a valuable metric, as if the time

469 is shorter, there may be a chance that the player didn’t fully recover from his previous injury.

470 Average minutes of a players’ last 5 games gives a representation of how much time a player has

471 been playing recently (around the past two weeks). Rest is a powerful metric as it totals the number

472 of days a player has in between games to potentially recover their body.

## 474 Practical Implications

My research is most impactful for NBA organizations. For load-management staff the

476 model provides a flag for early-warnings toward injuries. Rather than simply proving the fact that

477 longer rest lowers injury risk, the model quantifies when and for whom rest produces the greatest

478 economic return. In particular, rest emerged as one of the strongest predictors in the feature-

479 importance analysis, and the financial simulation demonstrated that players flagged as high-risk

480 who were strategically rested generated expected savings for teams. For example, given the sheer

481 amount of money allocated to star players, the expected savings from model-guided rest decisions

482 remained positive throughout every season.

Future research can extend this framework by refining the optimal amount of days to look

484 at alternative scenarios for player rest, and determining a truly optimal cost ratio between false

485 positives and false negatives. By integrating salary and injury prediction, my research moves

486 beyond just injury prediction, and gives outlets into what can be done with injury probabilities.

## 488 Limitations

There are three main limitations to my findings. First, when I decided to use previous

490 season statistics as features in my model, I sacrificed 16% (22631/140879) of total rows of the

491 final data. However, I decided that it was a reasonable compromise because previous season

492 statistics such as rebounds and free-throw attempts give insight into certain players’ physical

493 playstyle. Especially with free-throw attempts, a player getting fouled is something that could

494 greatly increase injury odds. Second, one of my engineered predictors (number of close games in

495 the last 20 games) rely on end of game point differentials which is a simplification from the NBA’s

496 definition of close games. Additionally, throughout the injury dataset, the third most frequent type

497 of injury is “Placed on IL” with no other description. With this description, I am unable to

498 determine if “Placed on IL” is something that is an injury that could be predicted or something

499 else like being placed on the IL for personal reasons or NBA health and safety protocols.

500 Throughout my study, I will be treating “Placed on IL” as a predictable injury, which may increase

501 the amount of injuries in the dataset. Furthermore, I do not consider illness and infections as

502 injuries. This means the model treats many instances where players log big minutes, get sick, and

503 miss the next game as non-injuries (0). The model may learn that heavy minutes are less risky than

504 they really are if there are significant amounts of high minute trends that lead to sickness. Finally

505 I acknowledge that the salary analysis process may be an oversimplification of real-world

506 scenarios. For example, I don’t take into account the money lost from rest, and I assume that salary

507 is evenly distributed across an 82-game season, which may be inaccurate considering NBA

508 playoffs. Additionally, variables were not reset at the end of each season and were continuously

509 counted across the end and start of seasons.

## 511 Conclusion

This research demonstrates that publicly available data and machine-learning methods can

513 meaningfully forecast NBA injury risk and, at the same time, quantify its financial consequences.

514 By combining injury-probability generated from a machine learning model with salary-based cost

29 515 estimates, the study introduces a new framework for NBA teams that connect topics in sports 516 medicine and health analytics to economic decision making in basketball. While this study doesn’t 517 dive into an optimization system, the approach demonstrates how predictive models can inform 518 load-management strategy while reducing expected salary loss. Future work may work on 519 expanding this framework by optimizing rest-time, deciding on a better “risk-threshold”, or taking 520 into account the financial cost of resting players. Ultimately, injury forecasting offers front offices 521 a simple, yet effective tool to preserve both player health and economic success.

527 528 529 530 531

## 532 Acknowledgements

I would like to express my gratitude for Professor Peter Kempthorne for his guidance in

534 helping me develop the methodological foundation for this study and his continued support

535 throughout the research process. I also cannot thank Brenden Eum enough for his mentorship

536 throughout both the methodological and paper-writing process. His guidance was invaluable in the

537 implementation of the nuanced parameter tuning for my model and all the other facets of this

538 project. Finally, I would like to thank my favorite NBA team, the Philadelphia 76ers, for inspiring

539 this project. Watching Joel Embiid and other crucial players battle through injuries, while my

540 hopes for a championship slowly vanished, motivated me to explore injury forecasting.

## 542 References

1. Smith, S. (2016, May 16). What is the real cost of injuries in professional sport? Medium. https://medium.com/@stephensmith_ie/what-is-the-real-cost-of-injuries-in-professional-sportfee1d66a7502

2. Dowsett, B. (2022, August 8). The NBA is turning to wearable sensors to prevent player injuries.

FiveThirtyEight. https://fivethirtyeight.com/features/the-nba-is-turning-to-wearable-sensors-toprevent-player-injuries ABC News

3. Cohan, A., Schuster, J., & Fernandez, J. (2021). A deep learning approach to injury forecasting in NBA basketball. Journal of Sports Analytics, 7(1), 1–12. https://doi.org/10.3233/JSA-200529

4. Charest, J., & Samuels, C. H. (2021). Impacts of travel distance and travel direction on back-toback games in the National Basketball Association. Journal of Clinical Sleep Medicine, 17(11),

2269-2274. https://doi.org/10.5664/jcsm.9446

5. Lu, Y., et al. (2022). Machine learning for predicting lower extremity muscle strains in the NBA.

Orthopaedic Journal of Sports Medicine. https://pubmed.ncbi.nlm.nih.gov/35923866

6. Chan, C. C., Yung, P. S. H., & Mok, K.-M. (2024). The relationship between training load and injury risk in basketball: A systematic review. Healthcare, 12(18), 1829. https://doi.org/10.3390/healthcare12181829

7. GHopkins. (2018). NBA injuries (2010–2018) [Dataset]. Kaggle. https://www.kaggle.com/datasets/ghopkins/nba-injuries-2010-2018

8. SzymonJWiak. (n.d.). NBA traditional stats [Dataset]. Kaggle. https://www.kaggle.com/datasets/szymonjwiak/nba-traditional

9. Justinas. (n.d.). NBA players data [Dataset]. Kaggle. https://www.kaggle.com/datasets/justinas/nba-players-data

10. NathanLauga. (n.d.). NBA games details: EDA [Code/dataset]. Kaggle. https://www.kaggle.com/code/nathanlauga/nba-games-eda-let-s-dive-into-thedata/input?select=games_details.csv

11. Ratin21. (n.d.). NBA player stats and salaries (2010–2025) [Dataset]. Kaggle. https://www.kaggle.com/datasets/ratin21/nba-player-stats-and-salaries-2010-2025

12. Jwiak, S. (2024). NBA traditional boxscores 1997–2024 [Dataset]. Kaggle. https://www.kaggle.com/datasets/szymonjwiak/nba-traditional

13. Benson, L. C., Clermont, C. A., Bošnjak, E., Ferber, R., & Osis, S. T. (2021). Evaluating methods for imputing missing data from athlete workload datasets. Sensors, 21(7), 2371. https://doi.org/10.3390/s21072371

14. Mohammed, M. B., Zulkafli, H. S., Adam, M. B., Ali, N., & Baba, I. (2021). Comparison of five imputation methods in handling missing data in a continuous frequency table. AIP

Conference Proceedings, 2355(1), 040006. https://doi.org/10.1063/5.0053286

15. Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324

16. Liaw, A., & Wiener, M. (2002). Classification and regression by randomForest. R News,

2(3), 18–22. https://journal.r-project.org/articles/RN-2002-022/RN-2002-022.pdf

587 588

## 589 Supplementary

To get an understanding of the frequency and different types of injury that occur in my

591 dataset, I construct three severity tiers to categorize injuries for better understanding: severe,

592 moderate, and minor. Frequency of injuries in my dataset can be seen in Graph A. In graph B, the

593 top five most frequent injuries are displayed by severity. In my dataset, the highest frequency in

594 the severe injury category were injuries that sidelined players for the season but with no further

595 injury detail. The second most common was a sprained right ankle that ruled players out for the

596 season, followed by a sprained left ankle of the respective nature. For the moderate tier, regular

597 sprained left and right ankles were of highest frequency. For minor injuries, sore left and right

598 knees were the most frequent. It is also noticeable that there are much more minor and moderate

599 injuries compared to severe ones.
