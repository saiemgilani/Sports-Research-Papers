<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Beyond the Expert An Algorithmic Approach to Correcting Expert Bias in Fantasy Football Projections - Jayanti.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/beyond-the-expert-an-algorithmic-approach-to-correcting-expert-bias-in-fantasy-football-projections/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Vishnu Datta Jayanti -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

BEYOND THE EXPERT: AN ALGORITHMIC APPROACH TO CORRECTING EXPERT BIAS

IN FANTASY FOOTBALL PROJECTIONS

Vishnu Datta Jayanti Senior at Allen High School

Allen, Texas vishnudattaj@gmail.com

## ABSTRACT

While traditional fantasy football projections have long relied on expert intuition, the rise of datadriven forecasting has shifted the analytical landscape. This analysis evaluates four XGBoost models designed for quarterbacks, running backs, wide receivers, and tight ends; the models were trained on a dataset spanning the 2013 through 2023 NFL seasons and validated against the 2024 season. Custom features such as career-maximum performance indicators and lagged inputs were added to the dataset to aid the models in identifying trends and a player’s talent ceiling. This research investigates whether

"pure" algorithmic models can mitigate the cognitive biases present in the "hybrid" models utilized by industry leaders such as ESPN. Performance was assessed using Mean Absolute Error and Spearman’s

Rank Correlation Coefficient to benchmark the model against ESPN’s preseason projections for the

2025 NFL season. Results indicate that while industry projections maintain superior accuracy in minimizing absolute error, the algorithmic models demonstrate highly competitive ordinal ranking performance. These findings suggest that “pure” machine learning models can serve as a viable supplement to publicly available fantasy football rankings.

14 Keywords fantasy football · machine learning · sports analytics · bias · feature engineering

## 15 Introduction

16 The transformation of fantasy football into a multi-billion-dollar industry has elevated the importance of preseason 17 projections (Bloomberg, 2026). The methods utilized by experts to form these baselines have evolved dramatically

18 over the years. Traditionally, experts synthesized fantasy football rankings through a blend of box score tracking, trade 19 publications, and direct communication with insiders. However, the rise of the internet fundamentally transformed 20 the work of analysts, expanding the available data from static box-score metrics into massive datasets comprised of 21 advanced statistics (Group, 2024). The complexity of the data surged with the advent of Next Gen Statistics (NGS). 22 A long-term collaboration between the NFL and Amazon Web Services, NGS utilizes RFID chips embedded within 23 the players’ shoulder pads and the football itself to capture sub-second positional data (Content, 2019). This flow of 24 “tracking data”, in which variables such as top speed, separation, and completion probability were measured, shifted the 25 role of analysts from collecting data manually to building complex algorithms. 26 The industry standard is currently defined by a "hybrid" framework, which ESPN describes as utilizing “a mixture 27 of statistical calculations and subjective inputs” (Clay, 2025). In this model, algorithmic outputs serve as guidelines 28 that are subsequently “corrected" by human experts to account for any trends the model may have neglected. A key 29 limitation of this system is that it hinges upon humans, who are innately biased, to refine the model’s outputs. By 30 injecting subjective judgment into the final projections, the rankings may inadvertently prioritize narrative over facts. 31 Extensive research has already been conducted on human bias in the context of predictive modeling. Specifically, Helmi 32 Hirsimäki conducted a literature review focused on forecasting inaccuracies within the business industry. Her thesis 33 focuses on instances where human experts attempt to correct model-generated outputs and identifies four primary biases 34 that disrupt forecasting: algorithm aversion—losing confidence in models after a mistake; anchoring bias—over-relying 35 on the first piece of information; optimism bias—producing unrealistically positive estimates; and misinterpretation 36 bias—seeing trends in noisy data (Hirsimäki, 2024). Although her analysis focuses on the business sector, the underlying 37 mechanisms behind these distortions can apply to fantasy football as well. 38 While Hirsimäki outlines the theoretical cognitive biases that plague human forecasting, Martin Spann and Bernd 39 Skiera provide evidence for this phenomenon in sports: more specifically, soccer. Analyzing data from the German 40 Premier Soccer League, their study evaluates the effectiveness of prediction markets, betting odds, and professional 41 tipsters in maximizing returns in a betting market (Spann & Skiera, 2009). Tipsters are individuals who provide 42 subjective game forecasts based on intuition and experience rather than objective data. Spann and Skiera concluded that 43 while prediction markets and betting odds achieved comparable levels of accuracy, both consistently outperformed 44 the subjective forecasts of tipsters. Although their study benchmarked tipsters’ performance against betting odds and 45 predictive markets, their conclusions regarding the limitations of expert intuition can be applied to the methodologies 46 used to calculate preseason projections in fantasy football as well. Their research creates a logical opening to test 47 whether modern algorithmic models can similarly outperform the expert-adjusted projections used by industry leaders 48 like ESPN. This research aims to evaluate whether purely algorithmic models can mitigate the inherent biases of hybrid 49 forecasting systems to provide more reliable preseason projections for fantasy football players.

## 50 Materials and Methods

51 The machine learning algorithm used for this study is eXtreme Gradient Boosting (XGBoost) (Chen & Guestrin, 2016). 52 In comparison to other traditional machine learning models, XGBoost is unique in that it can handle unbalanced datasets 53 (Imani et al., 2025). This is necessary, as the NFL’s production distribution is heavily skewed. Typically, the vast 54 majority of players are “average”. For example, there are hundreds of wide receivers who record 200-400 yards in 55 a season, but only a handful are capable of recording 1500+ yards. This is problematic for most machine learning 56 algorithms as they become “blind” to high performers, treating them as statistical anomalies. XGBoost mitigates 57 these errors through gradient boosting, a technique where multiple weak decision trees are trained sequentially (Clark 58 & Lee, 2025). In this framework, each subsequent tree is specifically designed to minimize the residual errors of 59 its predecessors, iteratively refining the model’s accuracy. This approach differs from Random Forest, a model I 60 initially considered, which utilizes bagging to build independent trees in parallel (IBM, 2021). While bagging reduces 61 variance by averaging results, gradient boosting allows XGBoost to capture complex, non-linear relationships within the 62 dataset more effectively (Lev, 2022). Therefore, the model is well-suited for the highly volatile nature of NFL player 63 performance.

64 To account for positional differences, four XGBoost regressors were developed, each utilizing a comprehensive dataset 65 featuring over 7100 data points spanning the 2012–2024 seasons (Hyde, 2024). The following hyperparameters were 66 optimized to balance both efficiency and model capacity: n_estimators was set to 400 to allow for sufficient iterations 67 while preventing overfitting; a learning_rate of 0.05 was implemented to ensure that models don’t overcorrect based 68 on previous iterations; and max_depth was restricted to 3 to limit model complexity and avert overfitting (XGBoost 69 Parameters — Xgboost 1.5.2 Documentation, 2022). To maximize computational efficiency, the tree_method was 70 set to hist, while the multi_strategy utilized a multi_output_tree to capture the underlying correlations between the 71 various outputs being measured. Furthermore, subsample and colsample_bytree were both maintained at 0.7 to prevent 72 any feature from dominating; gamma was set to 1, allowing the tree to partition conservatively; and the objective was 73 selected as reg:squarederror to minimize the mean squared error. Finally, a fixed random_state was used to maintain 74 the reproducibility of this study. Overall, these hyperparameters were chosen with the intent of preventing overfitting 75 and balancing computational efficiency.

76 In order to maximize the predictive signal extracted from the raw dataset, custom features were implemented. Beyond 77 standard counting statistics (e.g., total yards, touchdowns), several time-series aggregate methods were incorporated as 78 well. For example, a three-year rolling window was implemented by creating a lagged variable for every feature within 79 the dataset. By utilizing the ‘Past-n’ prefix to denote the specific year of the temporal lag, the features allow the models 80 to evaluate a player based on their trajectory rather than a single data point.

81 While lagged features capture recent performance, they can fail to account for a player’s inherent talent. To address 82 this, ‘career_max’ features were generated for rushing, receiving, and passing yards. These features prevent the models 83 from becoming overly sensitive to recent variance. While a three-year rolling window captures short-term trajectories,

84 exclusive reliance on these features risks the models rendering a mid-tier player at their peak and an elite player in a 85 slump as statistically identical.

86 For example, consider a scenario where Wide Receiver A and Wide Receiver B have near-identical production across 87 the Past-1, Past-2, and Past-3 features, such as three consecutive seasons of 800 receiving yards. A model restricted to a 88 three-year window would view these players as identical assets. However, if Player A has a career max of 1,500 yards 89 while Player B’s career max is 850 yards, the model is given the context to distinguish Player A as the more talented 90 one out of the two. The career max serves as an indicator of a player’s "ceiling," signaling to the XGBoost regressor 91 that Wide Receiver A is much more likely to explode back into high-tier production than Wide Receiver B.

92 To capture these nuanced distinctions without introducing personal bias, this research expands the feature set beyond a 93 few selected metrics. In an effort to remain objective, I chose to avoid the "hand-picking" of data. Instead of relying on 94 a pre-defined set of features, the model was given access to 1,933 unique variables. By utilizing the inherent feature 95 selection capability built into XGBoost, the model autonomously identified and prioritized attributes with the highest 96 predictive utility. This allows the model to project based on statistical correlation rather than heuristic bias.

97 Once the feature space was defined, the model was moved into the training and evaluation phase, where the updated 98 dataset was split into a training and testing split. The models were trained on historical data spanning from 2012 through 99 2023, while the 2024 season was used to evaluate the models on unseen data, where the Coefficient of Determination 100 was monitored to assess the models’ fit. Rather than predicting fantasy points as a whole, the models were trained to 101 forecast each component of the fantasy scoring formula independently. Following the inference phase, these individual 102 stat projections (e.g., projected yards, touchdowns, and receptions) were aggregated and used in modified versions of 103 ESPN’s Points Per Reception (PPR) formula to generate a final fantasy point total, which was then used to create the 104 models’ rankings (Scoring Formats, 2014). This component-based approach ensures that the models capture the specific 105 scoring nuances of the PPR format instead of attempting to predict the fantasy point total directly. Noisy outputs were 106 removed from each formula, such as receiving statistics for quarterbacks (QB) and passing statistics for skill players 107 (i.e., running backs (RB), wide receivers (WR), and tight ends (TE)), ensuring rankings are not skewed by unrelated 108 metrics. The formulas are displayed below.

PY

RY

F PQB = 25 + 4(P T D) + 10 + 6(RT D) − 2(IN T ) − 2(F U M )

(1)

RecY

RY

F PSkill =

+ 6(RecT D) + REC + + 6(RT D) − 2(F U M ) 10

(2)

Where F PQB represents QB fantasy points, F PSkill skill player fantasy points, P Y passing yards, P T D passing touchdowns, RY rushing yards, RT D rushing touchdowns, IN T interceptions, F U M fumbles, RecY receiving yards, RecT D receiving touchdowns, and REC total receptions. 110 In order to measure the models’ success for the 2025 NFL season, the 2022 to 2024 seasons were extracted as inputs. In 111 this time period, the data from the 2024 season was assigned as ’Past-1’ variables, while the 2023 and 2022 seasons 112 were assigned as ’Past-2’ and ’Past-3’, respectively. The ‘career_max’ features were simultaneously updated to include

113 the 2024 season. The outputs generated by the models and the preseason consensus from ESPN were recorded as the 114 baseline predictors. Following the conclusion of the 2025 season, the final PPR rankings were scraped to allow for a 115 head-to-head evaluation between the XGBoost regressors and ESPN’s pre-season rankings.

116 In order to measure the performance of the model, three key parameters were taken into account: the Coefficient of 117 Determination (R2), Mean Absolute Error (MAE), and Spearman’s Rank Correlation Coefficient (SRCC). The latter 118 two were used to evaluate ESPN’s preseason projections as well, in order to create a competitive baseline. This allows 119 for an objective assessment of the “pure” algorithmic approach compared to the “hybrid” industry standard. R2 was 120 utilized as a metric to determine how well the model explained the variability in the dataset (Brenndoerfer, 2025). 121 Therefore, R2 offers a standardized measurement of the effectiveness of the algorithm in transforming raw historical 122 data into a predictive tool. The mathematical formula for R2 is:

R2 = 1 − n i=1

(yi

− yˆi)2 in=1(yi − y¯)2

(3)

Where yi represents the actual observed value, yˆi is the value predicted by the XGBoost model, and y¯ is the mean of the observed data.

124 While R2 was incorporated as a metric evaluating model features, MAE was used as a baseline to assess the accuracy

125 of the models’ predictions. Unlike traditional approaches that measure error in raw fantasy points, this study utilizes

126 MAE as a measure of the deviation in player rankings. By calculating the average distance between a player’s predicted

127 rank and their actual end-of-season rank, the metric provides a direct measure of the models’ ranking accuracy (Frost,

128 2025). It is worth noting that MAE is susceptible to outliers. For the MAE analysis, a higher numerical value represents

129 a greater deviation from the actual results, while a lower value indicates superior predictive accuracy. The formula for

130 rank-based MAE is defined as:

1n

M AERank = n

|Rp,i − Ra,i|

(4) i=1

Rank-based Mean Absolute Error, where n is the number of players, Rp,i is the predicted rank of player i, and Ra,i is the actual rank of player i.

132 On the other hand, SRCC is used to evaluate the “strength and direction of association between two ranked variables” 133 (Laerd Statistics, 2018). In other words, it allows for the evaluation of ordinal accuracy that MAE does not support. 134 While MAE measures the actual distance between the ranks, SRCC measures the extent to which the model maintains 135 the structure of the leaderboard. This is especially important in fantasy football, as the ability to accurately pick the top 136 "tiers" of players is arguably more important for a successful draft than the numerical accuracy of a single ranking. It 137 is worth noting that SRCC is resistant to outliers. SRCC utilizes a scale where negative values represent an inverse 138 relationship and results near zero indicate no correlation; therefore, a higher coefficient signifies a stronger, more 139 accurate alignment between the projected and actual rankings. The mathematical representation of SRCC is expressed 140 as: ρ

=

−

6 n(n2 di2 − 1)

(5)

Spearman’s Rank Correlation Coefficient (ρ), where di represents the difference between the predicted and actual rank for each player and n represents the total number of players in the sample.

142 In using both MAE and SRCC, the evaluation framework attempts to assess all aspects of model performance from 143 a holistic perspective. While rank-based MAE offers a close look at the average “distance” of miss, SRCC attempts 144 to ensure that the models maintain the hierarchical integrity of the draft board. In other words, the models are being 145 assessed not only on their accuracy regarding individual players, but also on their general ability to navigate the tiers 146 of fantasy football. The Python implementation of the XGBoost models, including the training scripts and statistical 147 evaluations can be found in the project repository (Jayanti, 2026).

## 148 Results

149 To evaluate the XGBoost models, I first used R2 to measure how accurately the regressors captured the variance for 150 each statistical category. The performance across all 9 variables is detailed in Table 1.

Table 1: Model Fit (R2) for Individual Performance Metrics

151 The XGBoost models performed best when predicting yardage across all four positions. These categories consistently 152 produced R2 values between 0.34 and 0.42, showing a moderate relationship between the features and the outcomes.

153 Scoring metrics like touchdowns were more difficult to predict and resulted in lower scores near 0.20 or 0.30. Rare 154 events such as rushing statistics for tight ends or fumbles for pass catchers showed very little correlation, often having 155 values near 0. 156 After analyzing R2, I examined the features that drove the predictions before benchmarking the final rankings along with 157 ESPN’s hybrid projections. Of the 1,933 features employed during model training, the 10 most influential predictors for 158 each regressor are illustrated in the four variable importance plots below.

Figure 1: Feature Importance in each model 159 The feature importance distribution shows that, as expected, there is a focus on recent performance, as evidenced by 160 the dominance of ’Past-1’ variables within the top 10. Surprisingly, none of the ‘career_max’ metrics were present 161 on the graphs, ultimately highlighting the models’ preference to incorporate recent data when generating rankings. 162 While the feature importance plots reveal the internal logic of the models, the ultimate measure of their utility lies 163 in their predictive accuracy relative to industry standards. To quantify this, the models’ outputs were benchmarked 164 alongside ESPN’s preseason projections using MAE; the results are displayed below. To ensure the data remained 165 relevant for fantasy football fans, all metric comparisons were restricted to the top 20 quarterbacks and tight ends, the 166 top 50 running backs, and the top 60 wide receivers.

Figure 2: MAE comparison between XGBoost regressors and ESPN 167 After thorough comparison, it is evident that although the XGBoost regressors had achieved comparable accuracy to 168 ESPN’s hybrid projections in the QB and TE positions, a notable gap in performance was present for RBs and WRs. It 169 is worth noting that the algorithmic model had a slight edge over ESPN in the QB category. While Rank-based MAE 170 provides a measure of absolute deviation, it only captures one dimension of model performance. Conversely, SRCC 171 measures how well the model preserved the “tiers” in fantasy football. The degree to which each model preserved these 172 tiers is illustrated in the graph below.

Figure 3: SRCC comparison between XGBoost regressors and ESPN 8

173 Once again, the algorithmic model outperformed the industry standard for QBs and TEs. Surprisingly, the model 174 achieved a score almost identical to ESPN for WRs, despite vastly underperforming in MAE. The tight end model 175 demonstrated a significant improvement over ESPN, whose projections displayed a negligible correlation with the final 176 season outcome. A similar trend was observed in the quarterback results; however, it is notable that both ESPN and the 177 "pure" model struggled with this metric, as the XGBoost regressor scored near zero while ESPN’s projections had a 178 negative correlation. Conversely, ESPN maintained a substantial advantage in the running back category, mirroring the 179 MAE findings. To ensure the evaluation focused on predictive performance rather than injury luck, six players (who 180 happened to all be RBs and WRs) who failed to play a single game during the season were removed from the rankings. 181 Following their removal, both the MAE and SRCC were recalculated to provide a more accurate reflection of model 182 consistency. The injury-accounted MAE results are illustrated in Figure 4 below.

Figure 4: Injury accounted MAE comparison between XGBoost regressors and ESPN 183 Because the six players removed were exclusively wide receivers and running backs, the results for the quarterback and 184 tight end models remained unchanged from the previous analysis. However, within the running back and wide receiver 185 categories, the gap in MAE narrowed significantly, although both models continued to lag behind the preseason industry 186 projections. Similarly, the recalculated SRCC values, adjusted for player availability, are provided in the following 187 comparison.

Figure 5: Injury accounted SRCC comparison between XGBoost regressors and ESPN

188 The recalculated ordinal metrics showed minor improvements for RBs, though they were less dramatic than those found 189 in the MAE analysis. Surprisingly, however, the WR SRCC decreased after accounting for injuries.

## 190 Discussion

191 The results of the XGBoost models provide a clear picture of which player statistics are the most predictable from one 192 season to the next. The R2 values represent the proportion of variance in each metric that the model was able to explain 193 using historical data. Higher values, like those seen in yardage and receptions, indicate that the model found a strong, 194 repeatable signal in the data. Conversely, values near zero or below suggest that those specific metrics are driven more 195 by random chance than available inputs. 196 The difference between the values for yards and touchdowns for R2 demonstrates an important truth regarding football 197 analysis. While yards are a high-volume stat that will always accurately represent a player’s contribution and ability, 198 touchdowns are much more subject to small sample size and luck. A player can gain 100 yards through consistent 199 performance, but a touchdown often depends on a single play or a specific coaching decision. This demonstrates why 200 touchdowns are naturally much harder for any model to accurately predict with high precision due to their "noisy" 201 nature and large fluctuations from week to week. The findings of this research also indicate a significant divergence in 202 the effectiveness of "pure" algorithmic models for various positions within the National Football League. 203 Applying Hirsimäki’s framework of misinterpretation bias, it becomes evident why the model outperformed human 204 analysts in QB evaluation. As the most scrutinized position in the NFL, quarterbacks are under constant media pressure, 205 with every throw, decision, and body language cue dissected by fans and pundits alike. This high-stakes environment 206 creates a "noise" of public opinion that often bleeds into professional evaluation. Consequently, variables are frequently

207 used to evaluate QBs that aren’t necessarily tied to their actual performance, resulting in a clear form of misinterpretation 208 bias where these external factors are mistaken for the quarterback’s individual skill (Bennett, 2025). The model’s 209 success over ESPN proves that the "pure" approach was able to mitigate such bias by focusing strictly on objective 210 markers, thereby achieving superior scores over the "hybrid" approach for QBs in both MAE and SRCC. By filtering 211 out the narrative-driven noise that human experts struggle to ignore, the algorithmic approach isolates the true "signal" 212 to create viable QB rankings. However, it is also worth noting that both ESPN and the XGBoost regressor struggled 213 in SRCC, despite the model’s superior performance in comparison to ESPN. This highlights the volatility of the QB 214 position in general, as after the “elite” tier of QBs, it becomes increasingly difficult to rank subsequent players who are 215 often subject to high-variance performance (Kartes, 2025).

216 The next position for which the model achieved notable success was the TE position. Within this category, the model’s 217 success was especially noteworthy, as the model dominated ESPN in SRCC and was on par in terms of MAE. Such 218 results may be explained by anchoring bias, a cognitive error in which analysts tend to rely too heavily on the initial 219 information they receive regarding a particular player. Most often, this manifests as an over-reliance on a player’s draft 220 capital or physical profile before the draft, as these are often the primary "anchors" for a player’s ceiling (Myers, n.d.). 221 Analysts often fall in love with a player’s draft stock, be it a blazing 40-yard dash time or a prototypical "big-bodied" 222 physical profile, and often do not adjust their evaluation of a player’s ability despite on-field performance indicating a 223 lack of efficiency. The superior rank correlation provided by the model seems to indicate that, by essentially ignoring 224 a player’s physical ability and instead focusing on production, it can provide a more accurate reflection of a player’s 225 talent.

226 The cases of Caleb Williams and Kyle Pitts exemplify the conclusions reached above. While ESPN’s pre-season 227 evaluations significantly undervalued these athletes, their subsequent performance validated the “pure” models’ higher 228 projections. Although the "pure" models also underestimated these players, the margin of error was substantially 229 narrower than ESPN’s, demonstrating a more accurate assessment of their elite potential.

230 Entering the 2025 season, Caleb Williams was highly scrutinized for his rookie season. Picked first overall in the 2024 231 NFL draft, Williams was a highly sought-after talent who failed to meet expectations. ESPN’s QB-specific projections 232 reflected this widespread skepticism, ranking him 17th. In contrast, the model positioned Williams at 10th, which was 233 significantly closer to his eventual 5th-place finish. ESPN’s significant undervaluation serves as a clear instance of 234 anchoring bias, where his debut season disproportionately influenced future projections, causing him to plummet in the 235 rankings despite his underlying talent profile.

236 The evaluation of Kyle Pitts serves to further illustrate these distortions, specifically the misinterpretation bias. After a 237 historic 1,000-yard performance as a rookie, Pitts went on to have three consecutive subpar seasons where he was unable 238 to reach 700 yards. ESPN’s rankings responded to this recent performance with a lack of confidence, dropping him to a 239 17th-place evaluation to start the season. The human evaluators gave in to the emotional response of a multi-year slump, 240 whereas the model understood that a player of Pitts’ historical production deserved a statistical chance to perform at a

241 high-end. The model’s evaluation of 8th place was vindicated as Pitts went on to have a dominating season, finishing in 242 2nd place overall. This advantage, however, was not present across all positions.

243 The two positions ESPN dominated regarding the “pure” model approach were RBs and WRs. In both positions, the 244 model dominated MAE even after adjusting for injuries; similar trends were displayed in SRCC, although the WR 245 model achieved comparable results when using this metric. Running backs and wide receivers are, by nature, difficult to 246 project because their statistical output is not based solely on the player’s natural talent, but also on a number of external 247 factors. RBs, for example, are highly dependent upon the strength of the offensive line; in addition, a player’s statistical 248 output may vary greatly depending upon whether the offense is running to protect a lead or if they are forced to pass 249 in order to catch up. On a similar note, WR performance is often tied to coaching schemes and the QB. Because the 250 “pure” model wasn’t given the context to process these situational variables, it suffered in comparison to ESPN when 251 creating its projections. The "hybrid" method used by ESPN, in this case, may have actually worked in their favor, as 252 the inclusion of qualitative data, such as training camp reports or exclusive interviews, may have picked up on a shift in 253 a player’s usage before it was reflected statistically. Outside of predictive accuracy, the "pure" algorithmic approach 254 provides a significant benefit in efficiency. While a sports media giant like ESPN must utilize a large group of analysts 255 to "correct" and improve their projections, which is both time-consuming and expensive, the XGBoost model was able 256 to create comparable rankings at near-zero cost.

257 These results help identify the limitations of the “pure” model approach, serving as a diagnosis to further iterate upon 258 the model. Chief among these limitations is that the model was only evaluated on two seasons’ worth of data, with 259 2024 being used exclusively to calculate R2, and 2025 being used to benchmark the model against ESPN. In order 260 to apply the results of the study in a more general context, more testing must be conducted. Another limitation is 261 that the regressor has no understanding of context. In order to truly win at fantasy football, one must do more than 262 identify talent. Many factors influence the performance of a player: these include the players around them, the coaching 263 staff, and their injury history. These are factors that weren’t included in the model, representing a gap between purely 264 historical projection and the dynamic reality of professional sports. These are all taken into consideration by ESPN 265 when making their rankings, whether by using more nuanced data or using human experts to reflect these changes. 266 There are, however, ways to mitigate these issues when using the “pure” model approach.

267 Although quantifying the effect of a new coaching staff or roster change is a complex challenge, it can be addressed by 268 analyzing team statistics. Every year, Mike Clay projects individual player statistics across the entire league before 269 the start of the NFL season (Clay, 2026). While these are presented as player-specific forecasts, they are built on a 270 team-level framework, meaning they account for the context missing in the XGBoost models. By aggregating these 271 individual projections, which means summing the projected passing, rushing, and receiving outputs for all players on a 272 roster, one can calculate a projected total for team yardage, touchdowns, and points. These aggregate totals serve as 273 an excellent baseline, providing the environmental data necessary to refine the model’s predictive accuracy. However, 274 even with a perfect situational context, the model remains vulnerable to the physical unpredictability of the players 275 themselves.

276 As mentioned earlier, another limitation of the model is that it fails to account for injury volatility, specifically by 277 including players who are set to miss the entire season or the inevitable performance drop-off often seen in athletes 278 returning from significant medical setbacks. Fortunately, medical data is well documented in the NFL. This means 279 that players who sustain season-ending injuries before the season begins can be filtered out of the model. Furthermore, 280 specialized injury features can be appended to the dataset, encompassing both recent setbacks and historical career 281 data; this allows the model to learn the correlation between past medical issues and the future durability or performance 282 potential of a player. By integrating these contextual team-level frameworks and injury data, the model can move 283 beyond simple talent identification and begin to account for the complex variables that define professional football.

## 284 Conclusion

285 In this study, I investigated whether algorithmic modeling, specifically through XGBoost regressors, could provide a 286 more objective and accurate alternative to the “hybrid” models used by industry leaders, where algorithmic outputs are 287 “corrected” by human analysts. The results of the study highlight a nuanced performance landscape: while the ESPN 288 consensus remains superior in projecting RB and WR success, the XGBoost regressors were more consistently able to 289 rank QBs and TEs.

290 This disparity in performance by position likely indicates that the effectiveness of "correction" by a human analyst 291 is heavily dependent on the nature of the data being analyzed. In high-variance positions such as RBs or WRs, the 292 "hybrid" approach is likely benefiting from the ability to understand qualitative changes, such as a shift in philosophical 293 approach on offense or a player’s improved standing in the depth chart, which are not yet reflected in historical data. 294 In contrast, the "pure" approach’s stronger performance in ranking QBs and TEs indicates that in these positions, 295 "correction" is sometimes a source of cognitive interference. Future versions, which incorporate situational context, 296 may further render the results of this study more pronounced.

## 297 Acknowledgments

298 I am especially grateful to Professor Chris Davis (University of Texas at Dallas) for his insights into the viability of 299 feature-dense datasets in sports analytics, which were instrumental in shaping my approach to feature engineering.

## 300 References

301 Bennett, M. (2025, October). Qb or not qb? measuring discrimination in foot- ball labor markets working paper. https://www.magdalenabennett.com/files/mbennett_nfl.pdf

303 Bloomberg, L. (2026). Fantasy football: From a hobby to a billion-dollar business. Theblackandwhite.net. https :

//theblackandwhite.net/81936/sports/fantasy-football-from-a-hobby-to-a-billion-dollar-business/

305 Brenndoerfer, M. (2025, September). R-squared (coefficient of determination): Formula, intuition model fit in regression.

Mbrenndoerfer.com. https://mbrenndoerfer.com/writing/r-squared-coefficient-of-determination-formulaintuition-model-fit

308 Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining - KDD ’16, 1, 785–794. https://doi.org/

10.1145/2939672.2939785

311 Clark, B., & Lee, F. (2025, April). What is gradient boosting? Ibm.com. https://www.ibm.com/think/topics/gradientboosting

313 Clay, M. (2025, March). Mcbride’s bad td luck and 40 other things learned while doing 2025 fantasy football projections

- espn. ESPN.com. Retrieved March 22, 2026, from https://www.espn.com/fantasy/football/story/_/id/

44417717/2025-fantasy-football-projections-draft-trends-carry-target-shares

316 Content, W. S. J. C. (2019, January). How machine learning and analytics are transforming the nfl. AWS. https :

//partners.wsj.com/aws/how-machine-learning-and-analytics-are-transforming-the-nfl-analytics/

318 ESPN Fan Support. (2014). Scoring formats. https://support.espn.com/hc/en-us/articles/360003914032-Scoring-

Formats

320 Frost, J. (2025). Mean absolute error. Statistics By Jim. https://statisticsbyjim.com/glossary/mean-absolute-error/

321 Group, D. S. (2024, January). The evolution of fantasy sports powered by data. Medium. https : / / medium . com /

@marketing_25315/the-evolution-of-fantasy-sports-powered-by-data-eabe85c07b6f

323 Hirsimäki, H. (2024). Human biases in forecasting: Impact on judgmental adjustments. Aalto.fi. Retrieved March 22,

2026, from https://aaltodoc.aalto.fi/items/db51bfe0-016d-4594-9b38-547e9c3ee0c7

325 Hyde, P. (2024). Nfl stats 2012-2024. Kaggle.com. Retrieved March 22, 2026, from https://www.kaggle.com/datasets/ philiphyde1/nfl-stats-1999-2022?select=yearly_player_stats_offense.csv

327 IBM. (2021, September). Bagging. Ibm.com. https://www.ibm.com/think/topics/bagging

328 Imani, M., Beikmohammadi, A., & Arabnia, H. R. (2025). Comprehensive analysis of random forest and xgboost performance with smote, adasyn, and gnus under varying imbalance levels. Technologies, 13, 88. https :

//doi.org/10.3390/technologies13030088

331 Jayanti, V. D. (2026). Fantasy football ranking generator. GitHub. https://github.com/vishnudattaj/NFL-Fantasy

332 Kartes, J. (2025, July). Fantasy football projections: Exploring positional bias in projections - fantasy football analytics.

Fantasy Football Analytics. Retrieved March 22, 2026, from https://fantasyfootballanalytics.net/2025/07/ fantasy-football-projections-exploring-positional-bias-in-projections.html

335 Lev, A. (2022, December). Xgboost versus random forest | qwak’s blog. www.qwak.com. https://www.qwak.com/post/ xgboost-versus-random-forest

337 Myers, J. (n.d.). Statistical analysis identifies factors that predict long-term career success for nfl tight ends.

Retrieved March 22, 2026, from https : / / www . amstat . org / asa / files / pdfs / pressreleases / 2015 -

StatAnalysisFactorsPredictCareerSuccessNFL.pdf

340 Spann, M., & Skiera, B. (2009). Sports forecasting: A comparison of the forecast accuracy of prediction markets, betting odds and tipsters. Journal of Forecasting, 28, 55–72. https://doi.org/10.1002/for.1091

342 Statistics, L. (2018). Spearman’s rank-order correlation. Laerd Statistics. https : / / statistics . laerd . com / statistical guides/spearmans-rank-order-correlation-statistical-guide.php

344 XGBoost Developers. (2022). Xgboost parameters — XGBoost 1.5.2 documentation. https://xgboost.readthedocs.io/en/ stable/parameter.html
