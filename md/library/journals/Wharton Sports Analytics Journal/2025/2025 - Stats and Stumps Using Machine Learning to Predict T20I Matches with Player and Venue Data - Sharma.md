<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Stats and Stumps Using Machine Learning to Predict T20I Matches with Player and Venue Data - Sharma.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/stats-stumps-using-machine-learning-to-predict-t20i-matches-with-player-and-venue-data/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2025 -->
<!-- authors: Archith Sharma -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

1 Stats & Stumps: Using Machine Learning to Predict T20I Matches with Player and Venue Data

Archith Sharma1

1Texas Academy of Mathematics and Science

## Abstract

Cricket is gaining popularity worldwide rapidly, and at the front is the newest format of the game,

Twenty20 Internationals (T20I), and big data. This project attempts to predict cricket match outcomes using player-level performance metrics and machine learning models. A dataset of 1,029 T20I matches was analyzed, with player-level features engineered from batting and bowling statistics such as runs, strike rate, boundaries, wickets, economy rate, and maiden overs. These features were normalized by ground-specific scoring rates to account for venue effects. Four modeling approaches were compared: a simple heuristic based on total player impact, logistic regression with regularization, random forests, and support vector machines (SVMs). All models were implemented in R using packages such as glmnet and e1071. Logistic regression achieved the highest test accuracy of 70.24%, balancing predictive performance with model interpretability. The final model was used to generate win probabilities for both past and unseen matches, including the 2024 T20 World Cup Final (India vs South Africa) and a March 2025 match between New Zealand and Pakistan. These predictions reflect tight contests and demonstrate the model’s ability to quantify match uncertainty. Overall, the project illustrates how venue-adjusted, player-level impact metrics can enable robust and interpretable match outcome prediction and player comparison in international T20 cricket.

21 Keywords: 22 T20I, Cricket, Machine Learning, Player Impact, Cricket Analytics, Venue Adjustment, Regression

24 GitHub Code for Data Processing, Figure Generation and Analysis, Modeling: 25 https://github.com/ArchithSharma/CricketPredictions

## 26 Contents

27 1 Introduction

28 2 Materials and Methods

2.1 Description of Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Derivation of Impact Factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2.1 Definition of Bat and Bowl Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.2.2 ANOVA and Histogram Validation of Bat/Bowl Similarity . . . . . . . . . . . . . . . . 6

2.3 Determining Impact Factors to be used in Prediction . . . . . . . . . . . . . . . . . . . . . . . 7

2.3.1 Player Ratings and Impact Calculation . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3.2 Ground Buffs (Venue Factors) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3.3 Weighting by Player Ranking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3.4 Impact Per Game Adjustments to be used for prediction . . . . . . . . . . . . . . . . . 8

2.3.5 Calculation of Total Player Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.4 Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

40 3 Results

3.1 Player and Venue visualizations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

3.2 Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

43 4 Discussion

4.1 Analysis of Players and Venues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4.1.1 Player Analysis: Virat Kohli . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4.1.2 Player Analysis: Ajantha Mendis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4.1.3 Player Analysis: Glenn Maxwell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

4.1.4 Venue Analysis: England vs. Subcontinent Venues . . . . . . . . . . . . . . . . . . . . 11

4.1.5 Team Rankings Based on Recent Matches . . . . . . . . . . . . . . . . . . . . . . . . . 12

4.2 Analysis of Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

51 5 Conclusions

52 6 Acknowledgements

## 53 References

## 54 Appendices

55 A Player and Venue Visualizations, Code Used for Analysis and Figure Generation

A.1 Player and Venue Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

A.2 Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

## 58 B Glossary of Cricket Terms Used

1 59 Introduction

60 Cricket is a bat-and-ball sport that originated in England and has grown into one of the most popular

61 sports worldwide, particularly in countries like India, Australia, South Africa, and Pakistan. Played between

62 two teams of 11 players each, the game involves batting, bowling, and fielding, with the primary objective

63 being to score more runs than the opposing team. Cricket is played in different formats, ranging from the

64 traditional five-day Test matches to the fast-paced Twenty20 (T20) format.

T20 cricket, the shortest and most explosive format of the game, revolutionized the sport with its fast-

66 paced action and entertainment value. Each team gets a maximum of 20 overs (120 balls) to bat, encouraging

67 aggressive stroke play, quick scoring, and strategic bowling. Since its official introduction in 2003, T20 cricket

68 has gained massive popularity, leading to global tournaments such as the ICC T20 World Cup and franchise-

69 based leagues such as the Indian Premier League (IPL) and the Big Bash League (BBL). With its thrilling

70 finishes, power-hitting, and emphasis on adaptability, T20 cricket has attracted a new generation of fans

71 while maintaining the essence of the sport.

The rise of predictive analytics in cricket has closely coincided with the rapid growth of the T20 format.

73 With T20 matches fast-paced and often decided by fine margins, teams, analysts, and betting markets have

74 increasingly turned to data-driven approaches to gain a competitive edge. The shorter format requires quick

75 decision making, making real-time data analysis and predictive modeling crucial to optimize team strategies,

76 player selection, and match predictions.

In this paper, a unique approach will be taken that focuses on a new impact factor (IF) of players for

78 both batting and bowling, in addition to consideration of match venues. These factors will then be used to

79 train 3 types of models commonly used in sports prediction: Regularized logistic regression, random forest

80 classifier, and support vector machines (SVMs), with high test set accuracies of 67 - 70%. (Vistro et al.,

81 2019)

The paper is organized as follows. Section 2 (Materials and Methods) will explore the Cricinfo dataset

83 and derive the impact factor used for batting and bowling, along with a ground-based scaling to account

84 for different venues. Afterwards, multiple models are tested on the adjusted comprehensive impact factors.

85 Section 3 shows the accuracy percentages of the models along with its prediction on select matches. Section

86 4 and 5 analyze the impact factor for different players and venues, followed by a discussion of the models

87 and some conclusions/limitations. There are two appendices, the first containing figures generated that are

88 used in the analysis and the code used (A), and the second containing a definition of common cricket terms

89 used throughout the paper and the test-playing nations list (B).

2 90 Materials and Methods

91 All data pre-processing, analysis and modeling was performed in R. (R Core Team, 2024) See Appendix A.2 92 to locate the code used on GitHub and regenerate the figures.

93 2.1 Description of Data

Figure 1: Batting Data

The data is taken from ESPN Cricinfo, a reputable source containing in-depth statistics on all T20Is

95 played and the players themselves. (ESPN, 2025a) To access the data in R, the cricketdata package made

96 by Rob Hyndman (Hyndman et al., 2025) was used to access the Statsguru data in R as a dataframe. A

97 screenshot of the batting dataframe is shown above in Figure 1.

The data is then filtered to only include T20Is between the test-playing full ICC members, defined in

99 Appendix B. The data is also joined by match to determine the total impact factor of teams in their matches,

100 both bowling and batting.

101 2.2 Derivation of Impact Factor

102 At the core of this analysis is the novel impact factor used in comparing batting and bowling impacts. To

103 determine the formula for batting and bowling impact, correlation to the target metric between the total

104 impact of both teams was prioritized in addition to similarity in the distribution of the impact factors each

105 game.

The impact factor was manually tuned to a quantity that sufficiently addressed both criteria. They are

107 defined below in Equations 1 and 2:

108 2.2.1 Definition of Bat and Bowl Impact Batting Impact = (R × 0.125) + ((SR − 130) × 0.025) + (4s × 0.3) + (6s × 0.5) − OutPenalty (1) where:

R = Runs scored SR = Strike rate =

Runs Balls Faced

×

4s = Number of fours hit

6s = Number of sixes hit

OutPenalty = Fixed penalty of 0.5 if the batter is dismissed

Example:

A batter scores R = 40 runs off 28 balls, hits 3 fours, 2 sixes, and is dismissed.

SR

=

40 28

×

≈

142.86,

OutPenalty = 0.5

Batting Impact = (40 × 0.125) + ((142.86 − 130) × 0.025) + (3 × 0.3) + (2 × 0.5) − 0.5

= 5 + (12.86 × 0.025) + 0.9 + 1.0 − 2.5 = 5 + 0.3215 + 0.9 + 1.0 − 0.5 ≈ 6.72

Bowling Impact = (W × 3.25) + (M × 3) − ((E − 7.4) × 0.5)

(2) where: W = Number of wickets taken

M = Number of maiden overs bowled

E = Economy rate =

Runs Conceded Overs Bowled

7.4 = Baseline economy rate for adjustment

0.5 = Penalty per unit increase in economy above 7.4

Example:

A bowler takes W = 2 wickets and a E = 6.85 economy rate 3 and has no maiden overs.

Bowling Impact = (2 × 3.25) + (0 ∗ 3) − ((6.85 − 7.4) ∗ 0.5) = 6.5 + 0.55 ∗ 0.5 ≈ 6.775

Both batting and bowling equations consider a baseline adjustment for strike rate and economy rate

116 based on the average score of around 149 in T20Is. (Statsguru, 2025) Both example players did very well in

117 their respective games and had high similar impacts of around 6.75, showing the relevance of the heuristic.

Afterwards, the batting and bowling impacts were grouped by their totals by game for each team.

119 Afterwards, the differences between total impact factors are used as a heuristic to be correlated to the

120 winner of the match (interpreted numerically as 1, 0). As can be seen in the code, the correlation value is

121 0.773 for 1029 T20Is, and the R2 is 0.598, approximately 0.6 which indicates high explainability.

122 2.2.2 ANOVA and Histogram Validation of Bat/Bowl Similarity

123 To validate the assumption that the distributions are similar, an analysis of variance (ANOVA) is performed 124 by modeling the batting impacts on the bowling impacts and the result is displayed in Table 1. The p125 value that is almost 0 shows that the distributions are very similar. In addition the visual validation of 126 the histogram in Figure 2 shows how similar the total impact factors are, and that they can be used for modeling.

Term

Df Sum Sq Mean Sq F value

Pr(>F)

Total Bowling

19376

19376

95.95 < 2 × 10−16

Residuals

2068 417623

Table 1: ANOVA Results

Figure 2: Impact Distributions

128 2.3 Determining Impact Factors to be used in Prediction

129 In this study, the performance of players in a T20 match is evaluated through a series of factors that 130 encompass both their batting and bowling abilities. The impact of each player is adjusted for various game131 specific conditions, including venue-based adjustments and player rankings. Below, the rationale behind the 132 decision-making process is outlined for each factor used in the calculation of player impact.

133 2.3.1 Player Ratings and Impact Calculation

134 Each player’s performance is assessed based on their batting and bowling ratings, which are derived from his135 torical performance data. These ratings are extracted from the player_rankings_2 dataset, which includes 136 batting impact (BatImpactperGame) and bowling impact (BowlImpactperGame) for each player. These rat137 ings reflect the overall contribution of a player to their team’s performance in previous matches.

138 2.3.2 Ground Buffs (Venue Factors)

139 The performance of players is also adjusted based on the specific characteristics of the ground where the 140 match is played. Each ground has unique attributes that can influence player performance, such as pitch 141 conditions, weather, and altitude. The venue_factors dataset provides ground-specific adjustments known 142 as “ground buffs”. These buffs are applied to both batting and bowling ratings to account for the venue’s 143 impact on player performance. The following ground buffs are considered:

144 • Batting Buff (BattingScale2): This factor adjusts the batting impact based on ground-specific conditions such as pitch type, boundary size, and weather.

146 • Bowling Buff (BowlingScale2): This factor adjusts the bowling impact based on similar ground conditions that affect how bowlers perform, including pitch conditions and boundary dimensions.

148 2.3.3 Weighting by Player Ranking

149 The weight assigned to each player’s performance is influenced by their relative ranking in the team. Batting 150 and bowling impact are adjusted according to player rankings:

151 • Batting Impact: The top 8 batsmen (top and middle order) in the playing XI receive a weighted adjustment to their batting impact. The adjustment is proportional to the player’s ranking, with higher-ranked players receiving a greater weighting. The weight is calculated as a function of the player’s position in the batting order, with later batsmen receiving lower weights to reflect their reduced role in the match.

156 • Bowling Impact: Similarly, the top 6 bowlers are given weighted adjustments to their bowling impact, based on their ranking. The adjustment is calculated in a similar manner, with higher-ranked bowlers receiving greater weight. The bottom bowlers are excluded from the impact calculation, as they are less likely to bowl in the match.

160 2.3.4 Impact Per Game Adjustments to be used for prediction 161 Once the initial ratings are adjusted for venue buffs and player rankings, the resulting impact values 162 (BatImpactperGame_2 and BowlImpactperGame_2) are calculated for each player. The calculations are 163 performed iteratively for both teams, with batting and bowling impacts adjusted according to the above 164 factors: 165 • For batsmen, the weight is scaled according to their position in the batting order. 166 • For bowlers, a similar scaling is applied, with the most prominent bowlers receiving higher weights. 167 • The adjusted values for each player are stored and used to update the overall team impact.

168 2.3.5 Calculation of Total Player Impact

169 Finally, the adjusted batting and bowling impacts are compiled into a total impact score for each player. This

170 score is split into batting and bowling impacts, with the first 8 players in the batting order contributing to

171 the batting total, and the next 6 players contributing to the bowling total. The impact scores for each player

172 from both teams are then consolidated into a total impact matrix, which represents the overall performance

173 potential of the two teams based on individual player ratings and match conditions.

In summary, the impact factors in this methodology are derived from a combination of player rankings,

175 ground-specific adjustments, and positional weights. These factors provide a comprehensive assessment of

176 player performance, accounting for both individual ability and contextual factors, such as venue and team

177 composition.

178 2.4 Modeling

179 To predict T20I match outcomes based on player-level performance metrics, several classification models were 180 implemented and evaluated using a dataset where each match was represented by the total impact scores of 181 28 players (14 per team). As a baseline, a simple heuristic predicted the team with the higher cumulative 182 impact score as the winner. This naive method yielded an accuracy of 64%, providing a benchmark for 183 more advanced models.

A logistic regression model with elastic net regularization was trained using 5-fold cross-validation to tune

185 the hyperparameters α and λ. (Tay et al., 2023) To convert predicted probabilities into binary outcomes,

186 optimal classification thresholds were selected by averaging the best thresholds across ROC curves in 10-fold

187 cross-validation. (Robin et al., 2011) Repeating this process over 30 iterations, the logistic regression model

188 achieved a maximum accuracy of 70.24%, outperforming the heuristic approach and all other models.

To enhance explainability, the coefficient weights were extracted from the logistic model. Features associ-

190 ated with top-order batters and key bowlers—such as the highest run scorers, highest strike rate performers,

191 and wicket-takers—were consistently assigned large absolute coefficients, indicating their strong influence on

192 match outcomes. Notably, impact scores from players in the top three batting positions had the greatest

193 positive association with winning probability, while low-performing bowlers negatively influenced predicted

194 outcomes. In addition, Batters 7-8 and Bowlers 5-6 had large coefficients, showing that the model respected

195 lineup depth and all-rounder ‘X-factor’ performances.

A random forest model with 500 trees was also tried, tuning the mtry parameter via internal 5-fold CV.

197 This model achieved a maximum accuracy of 67.8%. Feature importance rankings from the random forest

198 agreed with the logistic regression: early-order batters and strike bowlers had the greatest influence, though

199 the non-linearity of the random forest also surfaced some interactions among lower-order players.

Lastly, a linear Support Vector Machine (SVM) was evaluated using a grid of cost values C = 2−5, . . . , 25

201 and 5-fold cross-validation. (Meyer et al., 2023) The best SVM model reached an accuracy of 69.7%,

202 comparable to the logistic regression model.

Among all approaches, logistic regression offered the best performance while also allowing for direct

204 interpretability through model coefficients. This suggests that linearly weighted combinations of individual

205 player impacts can be powerful predictors of T20I match outcomes.

3 206 Results

207 3.1 Player and Venue visualizations

208 Now that the impact factors are clearly defined, they can be used to construct rankings of players by batting, 209 bowling, or all-around play and venue factors. Similarly, teams can be ranked by their recent impact factors. 210 The full visualizations of the Top 15 in Career Impact and Impact per Game for batsmen are found in 211 Appendix A.1 containing Figures 4, 5, 6, and 7. All-rounders are defined as individuals in the top two-thirds 212 of all players in batting and in the top 55th percentile of all players in bowling. The average venue impact 213 was also min-max scaled to be used as a multiplier in the predictive modeling phase.

214 3.2 Model Results

The modeling results are organized below in Table 2.

## Model

Heuristic (Total Impact Comparison) Logistic Regression (Elastic Net) Random Forest Support Vector Machine (Linear Kernel)

Mean Accuracy (%)

64.00 68.32 66.08 67.42

95% CI (%)

[64.00, 64.00] [66.42, 70.24] [64.91, 67.80] [65.53, 69.70]

Table 2: Model performance based on mean accuracy and 95% confidence intervals over 30 iterations

The following data in Table 3 is the model’s output for select matches.

Match

IND vs RSA (T20 WC Final 2024) NZ vs PAK (Unseen Match, March 26) BAN vs. WI Dec 19 2024 IND vs. PAK Oct 23 2022

Win Probability (%)

IND: 50.46 NZ: 55.45 BAN: 50.62 IND: 64.5

Actual Winner

IND NZ BAN IND

Margin

7 runs 8 wickets 80 runs 4 wickets

Table 3: Predicted Win Probabilities and Actual Outcomes for Select T20I Matches

4 217 Discussion

218 4.1 Analysis of Players and Venues

219 4.1.1 Player Analysis: Virat Kohli

220 Virat Kohli is considered by many to be the world’s best batsman, scoring the third most runs of all time

221 and having the second most total hundreds. (ESPN, 2025b) However, many have shown doubt about his

222 performances in the shortest format of the game, especially due to concerns about his strike rate. (TOI

## 223 Sports Desk, 2024)

The impact factor method considers him one of the best, if not the best T20I batsmen despite his strike

225 rate. He is ranked the best batsman by total career batting impact, while he finds the third spot in batting

226 impact per game. His low strike rate is not enough of a hindrance due to the constant amount of runs he

227 amasses. The impact factor is able to find value in his ability to facilitate the innings.

228 4.1.2 Player Analysis: Ajantha Mendis

229 Ajantha Mendis (labeled BAW Mendis) was a spinner for Sri Lanka between 2008 and 2014. He is the 230 only player to take 6 wickets in a T20I twice, and also won Emerging Player of the Year in 2008. Labelled 231 a mystery spinner, when batsmen figured him out, he began to get hit all around the park. His biggest

232 criticism was the lack of consistency, and he disappeared from Sri Lanka’s XI in favor of Rangana Herath

233 and other spinners. (Cricbuzz, 2025)

The impact factor method has a shortcoming when considering a spinner like Mendis. Recent matches do

235 not get weighted more since the model does not have a time factor, and high performances in a small dataset

236 could push his impact as high as the third rank. To address it in model predictions, adding a random effect

237 to the player impact based on the number of games played could make a difference.

The theoretical framework would be that the more matches someone plays, the less deviation their impact

239 score would have. Comparing Mendis and Kohli, where the former played one thirds the games the latter

240 did, Mendis’s variance parameter estimate would have 3 times the variance of Kohli’s parameter and thus

241 represent his inconsistency. Player dropping ensures the model stays representative regardless of consistency

242 because inconsistent players tend to be dropped.

243 4.1.3 Player Analysis: Glenn Maxwell

244 Glenn Maxwell is considered the quintessential T20 player for the combination of his golden arm and power

245 hitting. He can steal wickets from loose shots, and send loose deliveries 100 meters away. Most of his impact,

246 however comes from batting. Unorthodox shots make him hard to stop when he gets going (ESPN, 2023),

247 and his high batting impact scores and semi-decent bowling performances push him up the all-rounder list.

This is in contrast to someone like Wanindu Hasaranga higher on the list, who is a handy batsman lower

249 in the order, but does most of his damage with the ball in his hands. Hardik Pandya is different from both,

250 being middle-of-the-pack in bowling and batting. The impact factor method gives them high, yet roughly

251 equal impacts which correspond to a correct aggregation.

252 4.1.4 Venue Analysis: England vs. Subcontinent Venues

253 The venue analysis by impact factor is mostly accurate to real-life ground impacts. 12 out of the top 20 best

254 batting venues are located in either India or Pakistan, reflecting the popular opinion that many pitches in

255 the subcontinent are batting paradises.

However, the grounds in England tend to be more balanced and favor the bowlers more. In total impact

257 relative to batting, Lord’s places 79th out of 105 venues. The famous slope at Lord’s makes bowling relatively

258 favorable as well. Southampton, The Oval and Headingley are all in the 60-70 range, reflecting England’s

259 moderate preference for bowling, showing that the scaling based on impact factor is an accurate measure of

260 ground impacts.

261 4.1.5 Team Rankings Based on Recent Matches

262 Based on the impact factor, rankings based on the total accumulated impact can be constructed for the last 263 6 months. The data shows that India is far and away the most in-form team, followed by Australia and 264 Afghanistan. South Africa and Pakistan are lower on the list, especially due to recent series losses to India 265 and New Zealand, respectively. Ireland is also placed higher since they have not played the top teams in the 266 last 6 months outside of Zimbabwe. However, overall, the list is an accurate representation of the current 267 T20I landscape.

Figure 3: Rankings based on performance for last 6 months

268 4.2 Analysis of Models

269 Four different approaches were tested for predicting T20I match outcomes: a simple heuristic model, logistic

270 regression with regularization, random forests, and support vector machines (SVM). The heuristic model,

271 which selects the team with the highest total player impact, achieved an accuracy of approximately 64%,

272 serving as a useful baseline. Logistic regression outperformed the others, reaching a maximum test accuracy

273 of 70.24%, with hyperparameter tuning and threshold optimization via cross-validation. Random forests and

274 SVMs followed closely with peak accuracies of 67.8% and 69.7%, respectively.

Logistic regression was selected for final prediction due to its strong performance and interpretability.

276 The model provides probabilistic outputs, allowing uncertainty to be quantified. For example, in the 2024

277 T20 World Cup Final between India and South Africa, the model assigned India a win probability of 50.46%,

278 reflecting an essentially even matchup which can be seen in the small result margin of 7 runs. Similarly, for

279 the March 26 match between New Zealand and Pakistan, the model predicted a New Zealand win probability

280 of 55.45%, indicating a slight edge.

These results suggest that logistic regression provides both competitive performance and actionable prob-

282 abilities for match outcome predictions. Moreover, its explainability makes it suitable for understanding how

283 individual player features contribute to team-level predictions.

5 284 Conclusions

285 This paper has been maximizing the value of a simple model in T20I prediction. More complex models can 286 consider strategy with the toss before matches, as many pitches get better to bat on because of the dew in 287 the night, meaning there is a significant advantage in batting second. (Krishnaswamy, 2022) In addition, 288 recent player form can change the parameter passed into the logistic regression. For example, Virat Kohli 289 was in a bad run of form during the T20 World Cup, only crossing 10 runs twice in the 7 matches before 290 the final. Specific bowler-batsman combinations are not considered either, such as the Indian top order’s 291 issues with left arm pace bowlers.(Iyer, 2023) Overall, however, this paper’s methods have had an accuracy 292 of 70% in predictions and an explainable impact factor that can be used to quantify team performance. This 293 framework can streamline cricket analysis and objectively pit players and teams against each other through 294 the power of data.

6 295 Acknowledgements

296 I would like to thank the Wharton Sports Analytics and Business Initiative for the opportunity to share my 297 work, and especially Professor Adi Wyner for organizing the Wharton High School Data Science Competition, 298 which sparked my interest in sports analytics. I am also grateful to the broader cricket analytics community, 299 particularly ESPN Cricinfo and the open source contributors to the R Project. Special thanks to Dr. Rob 300 J Hyndman, the creator of the cricketdata package, for enabling data-driven sports research. I would also 301 like to thank my grandfather, Giridhara Govinda Rao for introducing me to the game of cricket and inspiring 302 my love for it.

## 303 References

304 Cricbuzz. (2025). Ajantha mendis. Cricbuzz. Retrieved April 4, 2025, from https : / / www . cricbuzz . com / profiles/1390/ajantha- mendis#:~:text=Ajantha%20Mendis%20won%20the%20Emerging, has%

20accomplished%20that%20feat%20twice.

307 ESPN. (2023, November). Afghanistan vs australia 07 11 2023. ESPNcricinfo. Retrieved April 4, 2025, from https://www.espncricinfo.com/series/icc- cricket- world- cup- 2023- 24- 1367856/afghanistan- vsaustralia-39th-match-1384430/live-cricket-score

310 ESPN. (2025a). Espncricinfo. ESPNcricinfo. Retrieved April 4, 2025, from https://www.espncricinfo.com/

311 ESPN. (2025b). Virat kohli records. ESPNcricinfo. Retrieved April 4, 2025, from https://www.espncricinfo. com/cricketers/virat-kohli-253802/tests-odi-t20-records

313 Hyndman, R., Gray, C., Gupta, S., Hyndman, T., Rafique, H., & Tran, J. (2025). Cricketdata: International cricket data [R package version 0.3.0, https://github.com/robjhyndman/cricketdata]. https://pkg. robjhyndman.com/cricketdata/

316 Iyer, R. (2023, September). Why do indian batsmen struggle against left-arm pacers? rohit sharma and co.’s record against left-armers detailed. Sportingnews.com. Retrieved April 4, 2025, from https :

//www.sportingnews.com/in/cricket/news/why- do- indian- batsmen- struggle- against- left- armpacers-rohit-sharma-and-cos-record-against-left-armers-detailed/aomdbaj3kqbxdyimaxsefxrm

320 Krishnaswamy, K. (2022, April). The (un)dew advantage: What choice do teams batting first have? ESPNcricinfo. Retrieved April 4, 2025, from https://www.espncricinfo.com/story/ipl-2022-pbks-vs-kkrthe-undew-advantage-what-choice-do-teams-batting-first-have-1308698

323 Meyer, D., Dimitriadou, E., Hornik, K., Weingessel, A., & Leisch, F. (2023). E1071: Misc functions of the department of statistics, probability theory group (formerly: E1071), tu wien [R package version

1.7-14]. https://CRAN.R-project.org/package=e1071

326 R Core Team. (2024). R: A language and environment for statistical computing. R Foundation for Statistical

Computing. Vienna, Austria. https://www.R-project.org/

328 Robin, X., Turck, N., Hainard, A., Tiberti, N., Lisacek, F., Sanchez, J.-C., & Müller, M. (2011). Proc: An open-source package for r and s+ to analyze and compare roc curves. BMC Bioinformatics, 12, 77.

330 Statsguru. (2025). Total match results: T20 internationals. Cricinfo. Retrieved April 4, 2025, from https:

//stats.espncricinfo.com/ci/engine/stats/index.html?class=3;orderby=matches;orderbyad=reverse; template=results;type=aggregate

333 Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. Journal of Statistical Software, 106 (1), 1–31. https://doi.org/10.18637/jss.v106.i01

335 TOI Sports Desk. (2024, April). ’usually he isn’t this slow’: Former india cricketers express concerns about virat kohli’s strike rate. The Times of India. Retrieved April 4, 2025, from https://timesofindia. indiatimes.com/sports/cricket/ipl/top- stories/usually- he- isnt- this- slow- former- india- cricketersexpress-concerns-about-virat-kohlis-strike-rate/articleshow/109615198.cms

339 Vistro, D., Rasheed, F., & David, L. (2019). The cricket winner prediction with application of machine learning and data analytics. International Journal of Scientific & Technology Research. https:// www.kclas.ac.in/wp-content/uploads/2021/01/The-Cricket-Winner-Prediction-With-Application-

Of-Machine-Learning-And-Data-Analytics-.pdf

## 343 Appendices

A 344 Player and Venue Visualizations, Code Used for Analysis and

Figure Generation

346 A.1 Player and Venue Diagrams

(a) Batting Career Impact

(b) Bowling Career Impact

Figure 4: Total Career Bat/Bowl Impact Top 15

(a) Batting Impact by game

(b) Bowling Impact by game

Figure 5: Bat/Bowl Impact Top 15 per game

(a) All Rounder Total Impact

(b) All Rounder Impact by game

Figure 6: All Rounder by game/career impact

(a) Best Bowling Venues

(b) Best Batting Venues

Figure 7: Best Venues for Batting/Bowling

347 A.2 Code

348 All code used to process data, generate figures, & tune parameters/validate model at 349 https://github.com/ArchithSharma/CricketPredictions.

B 350 Glossary of Cricket Terms Used

## 351 Batting Terms

352 Runs Total number of runs scored by a batsman.

353 Strike Rate The average number of runs scored per 100 balls faced. A higher strike rate indicates more aggressive scoring.

355 Boundary A scoring shot that results in four (4) or six (6) runs.

356 Fours & Sixes A four occurs when the ball crosses the boundary after touching the ground; a six is when it crosses without touching the ground.

358 Batting Impact Score A custom metric combining runs, strike rate, and boundaries to evaluate batting effectiveness.

360 Top Order The group of batsmen who come out to bat first and score most of the runs, typically the first three or four guys in.

362 Middle Order The group of batsmen that are typically all-rounders and power hitters to try and get quick runs near the end.

## 364 Bowling Terms

365 Wickets The number of batsmen a bowler dismisses.

366 Maiden Overs Overs in which no runs are conceded.

367 Economy Rate Runs conceded per over bowled. A lower economy indicates more efficient bowling.

368 Spinner A bowler who bowls slow but gets the ball to turn, deceiving batsmen.

369 Pacer A bowler who bowls quick to try and beat batsmen with variations and leave them helpless.

370 Bowling Attack The group of bowlers in a team and their combined effectiveness.

371 Bowling Impact Score A weighted metric assessing bowling performance using wickets, maidens, and economy rate.

## 373 Match Context

374 T20I Twenty20 International – a short-format cricket match where each team bowls a maximum of 20 overs.

375 Venue Factor A numerical measure of how batting-friendly or bowling-friendly a stadium is, based on its average scoring.

377 Playing XI The eleven players selected to participate in a match.

## 378 Strategy Terms

379 All-Rounder A player who contributes significantly with both bat and ball.

380 Toss The coin toss where the captain who wins decides whether to bat or bowl first.

381 Run rate Runs per over (6 balls).

382 Pitch Surface that the bowlers bowl to the batsmen on, can heavily influence team decisions by favoring batting or a certain kind of bowling.

## 384 Test playing nations list

385 Afghanistan, Australia, Bangladesh, England, India, Ireland, New Zealand, Pakistan, South Africa, Sri 386 Lanka, West Indies, Zimbabwe.
