<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Forecasting NFL Wide Receiver Touchdowns with a Temporal Linear Regression Model - Chung.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/forecasting-nfl-wide-receiver-touchdowns-with-a-temporal-linear-regression-model/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Ruben Chung -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

TITLE PAGE

Forecasting NFL Wide Receiver Touchdowns with a

Temporal Linear Regression Model

Author: Ruben Chung

Author affiliation: Brown University, Providence, Rhode Island

Contact information author:

Ruben Chung

Ruben_chung@brown.edu

18 1

Forecasting NFL Wide Receiver Touchdowns with a

Temporal Linear Regression Model

Ruben Chung

Brown University, Providence, Rhode Island

24 1. Abstract

25 Forecasting touchdowns for NFL wide receivers is a challenging but valuable problem in 26 football analytics and player evaluation. Touchdowns are notoriously volatile, influenced by red 27 zone usage, quarterback play, and situational variance, making year-to-year outcomes difficult to 28 predict. This study develops a temporal linear regression model to project wide receiver 29 touchdown totals using a feature-rich dataset spanning 1990–2024. The dataset incorporates 30 lagged statistics, two-year rolling averages, player age and experience, team offensive strength, 31 and efficiency metrics such as catch rate and touchdowns per target. The model was trained on 32 1990–2010 player-seasons and tested on 2011–2024 data, with strict time-bounded feature 33 engineering to prevent data leakage.

34 Results show strong predictive accuracy (R² = 0.803, MAE = 0.82 TDs), demonstrating that 35 systematic patterns can be identified even within a highly volatile statistic. Feature importance 36 analysis indicates that efficiency and usage metrics are more reliable predictors than raw prior37 year touchdown totals, aligning with football intuition and highlighting regression-to-the-mean

38 effects. The model generates 2025 projections that identify both elite scorers and likely 39 regression candidates, providing insight into the stability of touchdown production.

40 This work demonstrates that with careful feature engineering, a transparent and interpretable 41 linear model can yield valuable insights in sports analytics. Beyond forecasting, the results 42 underscore the importance of efficiency and opportunity metrics in understanding touchdown 43 outcomes, offering a framework that can inform research on statistical predictability in 44 professional sports.

45 2. Introduction

46 Touchdowns are a critical driver of value in football analytics and player evaluation. However, 47 among all wide receiver (WR) statistics, touchdowns are the most volatile and thus among the 48 hardest to predict. This volatility stems from their dependence on situational factors such as red 49 zone usage, play-calling tendencies, and defensive matchups, which often vary widely from 50 game to game and season to season. As a result, analysts and bettors often find touchdowns to be 51 the hardest statistic to predict due to its inherent volatility. Early football analytics research 52 emphasized team-level scoring and play-calling (Burke, 2009), with less attention given to 53 forecasting individual player outcomes. More recent work has examined broader statistical 54 properties of NFL performance (Lopez, Matthews, & Baumer, 2018) and player-level evaluation 55 metrics such as nflWAR (Yurko, Ventura, Horowitz, & Balasubramanian, 2019). However, few 56 studies have addressed the predictability of touchdowns specifically, particularly using 57 temporally valid models.

58 This paper introduces a linear regression model designed to project wide receiver touchdowns 59 using a multi-season dataset with both player-level and team-level features. Unlike models that 60 rely solely on prior-year performance, we incorporate lag features, two-year rolling averages, 61 age and experience indicators, and contextual team metrics such as offensive scoring and pace. 62 This richer feature set allows the model to better account for nonlinear career arcs, regression to 63 the mean, role changes within an offense, and changes in structure of the offense itself.

64 The model is trained on NFL player-seasons from 1990 to 2010 and tested on data from 2011 65 through 2024. Our approach emphasizes temporal integrity to avoid lookahead bias: all 66 engineered features respect chronological boundaries. Despite the interpretability and 67 transparency of a linear model, our results show it captures meaningful signal in a noisy domain 68 and yields actionable projections. We conclude by applying the model to 2024 data to forecast 69 2025 WR touchdown outcomes.

70 For clarity, the following abbreviations are used throughout this paper: TD = touchdowns; RZ = 71 red zone; MAE = mean absolute error; RMSE = root mean squared error; R² = coefficient of 72 determination.

73 2.1 What is Linear Regression

74 Linear regression is one of the most widely used statistical techniques for modeling the 75 relationship between a dependent variable and one or more independent variables. In our case, 76 the dependent variable 𝑦𝑦 is the number of receiving touchdowns, and the independent variables 77 𝑥𝑥1, 𝑥𝑥2, … , 𝑥𝑥𝑛𝑛 are the engineered features describing a player’s past performance, efficiency, and 78 context (things such as yards per game or catch rate for example)

79 The core idea of linear regression is to fit a straight-line (or hyperplane, in higher dimensions) 80 relationship between inputs and output, such that the predicted values are as close as possible to 81 the observed values. Linear Regression thus assumes:

1. The relationship between predictors and the target is approximately linear.

2. The residuals (errors) are independent and have constant variance.

3. No predictor is an exact linear combination of others (no perfect multicollinearity).

85 In practical terms, the model estimates how much the target variable changes (touchdowns), on 86 average, when each feature changes by one unit, holding all other features constant.

87 2.2 Mathematical Formula of Linear Regression

88 For a dataset with 𝑛𝑛 observations and 𝑝𝑝 predictors, linear regression models the target 𝑦𝑦 as: 𝑦𝑦𝑖𝑖 = 𝛽𝛽0 + 𝛽𝛽1𝑥𝑥𝑖𝑖1 + 𝛽𝛽2𝑥𝑥𝑖𝑖2 + ⋯ + 𝛽𝛽𝑝𝑝𝑥𝑥𝑖𝑖 + 𝜀𝜀𝑖𝑖

90 where:

• 𝒚𝒚𝒊𝒊= the actual value of the dependent variable for observation 𝑖𝑖

• 𝒙𝒙𝒊𝒊𝒊𝒊= the value of predictor 𝑗𝑗 for observation 𝑖𝑖

• 𝜷𝜷𝟎𝟎 = intercept term

• 𝜷𝜷 = coefficient for predictor 𝑗𝑗

• 𝜺𝜺𝒊𝒊 = residual error for observation 𝑖𝑖

96 The goal is to find the coefficient vector �����⃗𝛽 = (𝛽𝛽0, 𝛽𝛽1, … , 𝛽𝛽𝑝𝑝 that minimizes the Residual Sum of 97 Squares (RSS): 𝑛𝑛 𝑝𝑝

𝑅𝑅𝑅𝑅𝑅𝑅(β) = �(𝑦𝑦𝑖𝑖 − 𝛽𝛽0 − � 𝛽𝛽𝑗𝑗𝑥𝑥𝑖𝑖)2 𝑖𝑖=1 𝑗𝑗=1

99 This minimization yields the ordinary least squares (OLS) solution: 𝛽𝛽 = (𝑋𝑋𝑇𝑇𝑋𝑋)−1𝑋𝑋𝑇𝑇𝑦𝑦

101 where:

• 𝑋𝑋 = 𝑛𝑛 ∗ (𝑝𝑝 + 1) matrix of features (including a column of ones for the intercept)

• 𝑦𝑦 = 𝑛𝑛 ∗ 1 vector of target values

104 In the context of this paper each 𝛽𝛽𝑗𝑗 represents the expected change in touchdowns for a given 105 player for a change of one-unit for the feature 𝑥𝑥𝑗𝑗 while assuming all other variables remain 106 constant. Positive coefficients would imply a positive correlation between that feature and 107 expected touchdowns scored – and vice-versa.

108 3. Materials & Methods

109 3.1 Data Sources

110 To build a model capable of projecting wide receiver touchdowns, a comprehensive dataset of 111 NFL WR performance spanning over three decades was assembled. The dataset pulls together

112 information from multiple sources and levels — including individual player statistics, rushing 113 contributions, and some context about their team and situation.

114 The core data were scraped from Pro-Football-Reference.com (Pro-Football-Reference.com, 115 2025), including:

• Receiving stats (e.g., targets, receptions, yards, touchdowns, yards per reception)

• Rushing stats (for WRs with occasional carries)

• Team stats (e.g., points scored, total offensive plays, yards per play)

119 These were compiled into season-level records for every wide receiver from 1990 through 2024.

120 3.2 Feature Engineering

121 To support accurate preseason forecasting, a variety of derived features were constructed from 122 player and team data. These included both static and historical variables, with all temporal 123 metrics carefully bounded by year to prevent data leakage.

Static Features:

• Age and Experience Indicators: Variables such as player age, total seasons active, and binary flags for career stages (e.g., prime years at ages 25–29 or rookie/sophomore seasons at age ≤ 23).

• Individual Performance: Core metrics including Catch Rate (completions per target), targets per game, and yards per game.

• Scoring Efficiency: Touchdowns per reception (TD_Per_Reception) and per target

(TD_Per_Target), capturing how effectively players convert opportunities into scores.

• Team Context: Offensive strength measures, such as Team_Offense_Strength (points per game).

Historical Features:

• Prior Season Performance: Key statistics from the previous year, including touchdowns, targets, receptions, and receiving yards (e.g., TD_Prev, Yds_Prev).

• Long-Term Trends: Two-year rolling averages for touchdowns, receptions, and yards

(e.g., TD_Avg2, Rec_Avg2, Yds_Avg2) to capture sustained performance over time.

• Career Experience: Number of years a player has appeared in the dataset.

145 All features were designed to mirror the type of information available during the preseason, 146 ensuring the model’s evaluation aligns with real-world forecasting constraints.

147 3.3 Problem Framing

148 This section describes the process used to model and project WR touchdown totals. The 149 approach involves preparing the dataset, training a linear regression model and testing it on a 150 different dataset.

151 We frame WR touchdown prediction as a supervised regression task. For each player-season, the 152 goal is to predict the number of receiving touchdowns (TD) a player will score based on a

153 variety of contextual and historical features. The modeling target is continuous (TD ∈ ℝ⁺), and we 154 use a linear regression framework for its transparency and interpretability.

155 An inherent characteristic of this modeling framework is regression to the mean: extreme 156 touchdown totals in one season are statistically likely to move closer to league-average levels in 157 subsequent seasons. In a linear regression context, unless a predictor perfectly explains the 158 target, the model’s fitted values tend to be “pulled” toward the overall mean. This property helps 159 prevent overestimation of repeat peak seasons and avoids overreacting to one-off scoring spikes, 160 which is particularly important for touchdowns given their volatility.

161 3.4 Feature Set and Target Variable

162 The features used in the model fall into the following categories:

• Lag Features: Stats from the previous season (e.g., TD_Prev, Yds_Prev, Tgt_Prev, Y/R_Prev)

• Rolling Averages: Two-year rolling means for TDs, targets, receptions, and yards

(TD_Avg2, etc.)

• Player Traits: Age, experience (Age, Age_Squared, Experience, Prime_Age, Rookie_Sophomore)

• Efficiency Metrics: TD_Per_Target, Catch_Rate, Target_Share, Yards_Per_Game

• Red-Zone Data (RZ): Rz_Targets, RZ_receptions, RZ_yards, RZ_TDs, RZ_INTs, RZ_Catch_Rate

• Team Context: Offensive output per game (Team_Offense_Strength), and scoring environment

• Durability: Games played

172 The target variable is the actual number of receiving touchdowns scored by a player in that 173 season.

174 3.5 Temporal Validation and Data Leakage Prevention

175 To ensure robust backtesting, we implement a chronologically consistent train/ test split of the 176 data set:

• Training Set: Player-seasons from 1990–2010

• Test Set: Player-seasons from 2011–2024

179 All temporal features (e.g., lag stats and rolling averages) are computed using only prior seasons 180 up to the year being predicted. This simulates a true forward-looking forecast and ensures the 181 prevention of data-leakage.

182 3.6 Model Choice and Evaluation

183 We trained the Linear Regression model using scikit-learn (Pedregosa et al., 2011), with the 184 following characteristics:

• No regularization (ordinary least squares)

• Standardization applied to numeric features via StandardScaler

187 This choice was made to prioritize interpretability, making it easier to identify which features 188 positively or negatively influence TD outcomes.

189 We apply 5-fold cross-validation on the training set to assess in-sample error and variance in the 190 model. In this procedure, the training data is split into five equal parts – called folds. The model 191 is trained on four folds and evaluated on the remaining fold, repeating so that each fold serves 192 once as the evaluation set.

## 193 Five folds were chosen as a balance between:

• Bias and variance estimation – Too few folds can yield noisy estimates of model performance, while too many folds (e.g., leave-one-out) can produce low-bias but highvariance estimates.

• Computational efficiency – Five folds provide stable performance metrics without making training time excessive.

Metrics reported include:

• MAE (Mean Absolute Error)

• RMSE (Root Mean Squared Error)

• R² Score

203 The final model is evaluated on the full test set (2011–2024) to measure out-of-sample 204 generalization.

205 4. Results and Data Visualization

206 The linear regression model was trained on NFL WR data from 1990 to 2010 and evaluated on a 207 temporally isolated test set spanning 2011 through 2024. Results from the out-of-sample backtest 208 show that the model captures meaningful signal in a high-variance target variable: receiving 209 touchdowns.

210 4.1 Top Features

211 The figure below shows the features used in training and testing the model, a positive coefficient 212 value implies a positive correlation with touchdowns (and vice-versa). A larger magnitude 213 implies a stronger correlation.

Figure 1. Feature coefficients for touchdown prediction using linear regression.

Positive coefficients (blue) indicate features that increase projected touchdowns; negative coefficients (red) decrease them.

218 The most influential features in the model, ranked by coefficient magnitude, were:

1. Catch Rate – A higher catch rate reflects a receiver’s reliability and ability to convert targets into completions. Consistently catching passes increases red-zone efficiency and scoring opportunities.

2. Yards Per Game – Sustained yardage production per game signals a player’s central role in the offense and strong target volume, both of which correlate strongly with touchdown opportunities.

3. Two-Year Average Receiving Yards (Yds_Avg2) — In this model, the coefficient is negative conditional on other features (e.g., catch rate, usage). This can occur if highyardage profiles come from between-the-20s usage while lower-yardage receivers see proportionally more red-zone targets.

229 Notably, the model emphasizes efficiency and sustained production metrics over raw prior-year 230 touchdown totals. This aligns with established football intuition: touchdowns are more often the 231 product of consistent usage and high-value opportunities than the simple repetition of past high232 scoring seasons. By identifying players with stable efficiency profiles, the model highlights 233 candidates most likely to sustain or improve their touchdown output.

234 4.2 Test Set Performance

235 The model achieves strong performance on the 2011–2024 test set, as shown in Table 1.

Metric

Value

Mean Absolute Error (MAE)

## 0.82 TDs

Root Mean Squared Error (RMSE) 1.29 TDs

R² Score

0.803

Table 1: Performance metrics for the linear regression model predicting WR touchdowns (2011–2024 test set).

239 240 The low mean absolute error (MAE) of 0.82 touchdowns indicates that most predictions are 241 within ±1 TD of actual outcomes. The root mean squared error (RMSE) of 1.29 TDs reflects a 242 modest penalty for larger errors, while the R² of 0.803 suggests that the model explains over 243 80% of the variance in wide receiver touchdown totals. These results demonstrate strong 244 predictive accuracy for a linear model, particularly given the high volatility and perceived non245 linearity of touchdowns.

246 4.3 Cross-Validation (Train Set)

247 During training (1990–2010), the model achieved a cross-validation MAE of 0.45 ± 0.08, 248 suggesting low variance and good generalization. The consistency between train and test scores 249 supports the model’s robustness and lack of overfitting.

250 4.4 Data Visualization

Figure 2. Predicted vs actual WR touchdowns (2011-2024 test set) with identity and best-fit lines; alignment indicates low systematic bias.

255 The best fit regression line is given by the equation: 𝑦𝑦 = 1.06𝑥𝑥 − 0.18 where y represents actual 256 touchdowns scored, and x represents our models projected touchdowns. Our slope being 1.06, 257 greater than 1, implies a slight tendency to underpredict at the high end of the distribution, while 258 the intercept of –0.18 is close to zero, indicating minimal systematic bias.

259 A comparison of the model’s best-fit line to the identity line (𝑦𝑦 = x, perfect predictions) reveals 260 systematic patterns. When touchdowns are low (< 3) the identity line is above the model’s best 261 fit line. This means that in this range of touchdowns the model slightly overpredicts touchdowns. 262 On the contrary, when touchdowns are higher ( > 3) the identity line is below the best fit line. 263 This means the model slightly underpredicts touchdowns. In fact, the distance between the two 264 lines increases as touchdowns increase, so this under projection becomes worse as touchdowns 265 increase (reflecting the increased variance in elite level touchdown scoring). This reflects both 266 the increased variance among elite scorers and the model’s natural regression toward the mean.

267 4.5 Projections for Upcoming Season

268 After evaluation, the trained model was applied to WRs from the 2024 season to generate 269 touchdown projections for 2025.

270 The model’s projections for 2025’s top 10 touchdown scorers are presented in Table 2.

Player

Tm

Ja'Marr Chase

CIN

Age

Games

TD Projection TD / Game

11.03

0.649

Justin Jefferson

MIN

9.85

Brian Thomas

JAX

8.52

Drake London

ATL

7.89

Terry McLaurin

WAS

7.69

Amon-Ra St. Brown DET

7.4

A.J. Brown

PHI

7.26

Ladd McConkey

LAC

7.26

Jerry Jeudy

CLE

7.14

Jameson Williams

DET

7.09

0.579 0.501 0.464 0.452 0.435 0.558 0.454 0.42 0.473

Table 2. Model projections for the top 10 wide receivers by touchdown total in the 2025 NFL season

(based on 2024 data).

273 These results align closely with expectations for elite WRs, with Ja’Marr Chase topping the list 274 with 11.03 projected touchdowns. While this is still an elite projection, it represents a decline 275 from his 2024 production due to reversion to the mean — the statistical tendency for extreme 276 performances to move closer to league-average levels in subsequent seasons.

277 The list includes many established stars (e.g., Justin Jefferson, Amon-Ra St. Brown, A.J. 278 Brown), however, the model does not incorporate external situational factors for 2025 that could 279 materially influence these projections. For example:

• Justin Jefferson and Drake London will be playing with new quarterbacks.

• Brian Thomas may see target share competition from 2nd overall pick, rookie teammate

Travis Hunter.

284 These contextual elements, while important for interpretation, fall outside the model’s current 285 feature set. Future work could incorporate roster changes, quarterback stability, and offensive 286 scheme adjustments to better capture these external influences and provide perhaps more 287 accurate projections.

288 5. Discussion

289 The results of our linear regression model provide several important insights into the 290 predictability of WR touchdowns and the broader dynamics of NFL scoring.

291 5.1 Interpretable and Stable Performance

292 The model's R² of 0.803 and MAE under 1 TD demonstrate that touchdowns, while high 293 variance, are not entirely random. By relying on a broad, temporally valid feature set, the model 294 captures stable indicators of future scoring — particularly catch efficiency, receiving volume, 295 and team context. This shows that touchdown regression and breakout candidates can be 296 detected systematically using historical data.

297 Moreover, the model’s strong cross-validation performance (MAE = 0.45 ± 0.08) further 298 validates its generalizability and lack of overfitting, despite the additive, linear structure of the 299 model.

300 5.2 Feature Importance Reveals Underlying Mechanics

301 The most predictive features — such as Catch_Rate, Yards_Per_Game — reflect sustainable 302 opportunity and role in an offense rather than raw scoring alone. This aligns with the football

303 intuition that touchdowns are often a function of consistent usage and efficiency rather than 304 isolated high-touchdown seasons.

305 Interestingly, past touchdown totals (TD_Prev) did not rank among the top linear features, 306 suggesting that surface-level regression models relying on "he scored X touchdowns last year" 307 may be overly simplistic; guidelines based on prior-year scoring are insufficient for reliable 308 forecasting in such a volatile statistic.

309 5.3 Limitations

310 Limitations 311 While this project provides a strong foundation for touchdown prediction, the model has several 312 notable limitations:

• Linear form: Cannot capture nonlinear effects, such as diminishing returns or interactions between variables (e.g., age and usage).

• No injury or situational awareness: Lacks inputs for offseason and in-season changes, including depth chart shifts, quarterback changes, and play-calling adjustments.

• No adversarial defense data: Matchup strength and opposing defensive rankings were not incorporated.

• Limited positional scope: Focuses exclusively on wide receivers, excluding other offensive positions.

## 321 Future Work 322 Future research could address these gaps by:

• Applying the methodology to predict other wide receiver statistics—such as receiving yards or receptions—to build a more complete player profile.

• Expanding the framework to include additional positions, such as tight ends or running backs.

• Incorporating richer data sources, including play-by-play logs, tracking metrics, defensive matchup data.

• Adding offseason and situational information, such as coaching staff changes, injury history, and team roster moves.

• Exploring more advanced modeling techniques—such as tree-based ensembles or neural networks—to capture nonlinear relationships and complex feature interactions.

333 5.4 Practical Applications

334 Despite its simplicity, the model offers clear, actionable value across multiple areas. Its linear 335 regression framework makes it highly interpretable, allowing outputs to be analyzed and trusted 336 in real-world decision-making. By ranking players based on projected touchdowns and grouping 337 them into tiers, the framework can inform evaluation. In professional contexts, the model 338 highlights the attributes most strongly associated with scoring, assisting scouts, analysts, and 339 coaching staff in talent assessment and development. In broader analytics applications, the 340 projections and feature importance provide a benchmark for understanding which statistics most 341 reliably translate into future scoring outcomes.

344 6. Conclusion

345 This study developed and validated a linear regression model to forecast NFL WR touchdown 346 totals using feature-rich, temporally consistent dataset spanning 1990–2024. By incorporating 347 lagged performance statistics, rolling averages, efficiency metrics, and team-level context, the 348 model achieved strong predictive accuracy in one of football’s most volatile metrics, 349 touchdowns.

350 Evaluation on an out-of-sample test set (2011–2024) yielded an R² of 0.803 and an MAE of 0.82 351 touchdowns, demonstrating that even in the presence of perceived randomness in scoring 352 touchdowns, systematic patterns can be identified and exploited. The model’s interpretability 353 allowed for clear insights into which factors most influence touchdown outcomes — with 354 efficiency and volume metrics outperforming raw prior-year touchdown counts as predictors.

355 The resulting projections for 2025 offer actionable guidance for sports analytics and player 356 evaluation by identifying likely regression and breakout candidates. While the linear framework 357 is interpretable and robust, future work could explore nonlinear modeling, additional contextual 358 variables such as red zone usage or quarterback efficiency, and integration of play-by-play 359 tracking data.

360 In sum, this work shows that with careful feature engineering and strict prevention of data 361 leakage, a transparent linear regression model can provide valuable and interpretable forecasts 362 for one of football’s most volatile statistics.

## 364 Acknowledgements

365 The author is an undergraduate student at Brown University, Providence, RI. This research was 366 conducted independently and did not receive formal guidance or funding from a specific course, 367 program or research grant.

## 368 References

369 Burke, B. (2009). The hidden game of football: A quantitative analysis of scoring and play 370 calling in the NFL. Journal of Quantitative Analysis in Sports, 5(3), Article 6. 371 https://doi.org/10.2202/1559-6458.1102

372 Lopez, M. J., Matthews, G. J., & Baumer, B. S. (2018). How often does the best team win? A 373 unified approach to understanding randomness in North American sport. The Annals of Applied 374 Statistics, 12(4), 2483–2516.

375 Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, 376 É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 377 2825–2830.

378 Pro-Football-Reference.com. (2025). NFL player statistics. Sports Reference LLC. 379 https://www.pro-football-reference.com/

380 Yurko, R., Ventura, S. L., Horowitz, M., & Balasubramanian, V. (2019). nflWAR: A 381 reproducible method for offensive player evaluation in football. Journal of Quantitative Analysis 382 in Sports, 15(3), 163–183.

## 384 Statements and Declarations

385 Ethical considerations 386 Not applicable. This research used publicly available secondary data (NFL statistics) and did not 387 involve human participants, human tissue, or human data requiring ethical approval.

## 388 Consent to participate 389 Not applicable

## 390 Consent for publication 391 Not applicable

392 Declaration of conflicting interest 393 The author declares no potential conflicts of interest with respect to the research, authorship, 394 and/or publication of this article.

395 Funding statement 396 The author received no financial support for the research, authorship, and/or publication of this 397 article.

398 Data availability 399 All raw data used in this study are publicly available from Pro-Football-Reference 400 (https://www.pro-football-reference.com/). Processed datasets and model predictions generated 401 during the current study are available from the author on reasonable request.

402 403 404 405
