<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - Beyond the Boundary Revolutionizing the IPL MVP Index - Rajaram et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/beyond-the-boundary-revolutionizing-the-ipl-mvp-index/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2024 -->
<!-- authors: Shreyas Rajaram; Sehaj Doshi; Aarush Bahel; Benjamin Pearlberg; Neil Jaiswal -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

## 1 Beyond the Boundary: Revolutionizing the IPL MVP Index

Shreyas Rajaram - The Dalton School ‘26

Sehaj Doshi - Awty International School ‘25

Aarush Bahel - Haberdashers’ Boys’ School ‘25

Benjamin Pearlberg - The Pennington School ‘25

Neil Jaiswal - Bridgewater-Raritan Regional High School ‘25

## 8 Abstract

9 Since its inception in 2008, the Indian Premier League (IPL) has attracted many of the world’s 10 most skilled cricket players, offering a highly competitive arena for them to showcase their 11 talents. Each season, the IPL awards the Most Valuable Player (MVP) title to the player who 12 achieves the highest rating on the league’s MVP metric. Ideally, this award recognizes the top 13 performer of the season, with high rankings indicating outstanding achievement among elite 14 players. However, the calculation used by the IPL to assess player performance lack consistency, 15 are limited in scope, and rely on arbitrary criteria. This paper employs a multivariate regression 16 model to develop a more robust formula, assigning mathematically optimized weights to devised 17 metrics that better capture player contributions. With an R² value of 0.80—compared to the 18 existing system’s 0.66—this new formula provides a more accurate and comprehensive 19 evaluation of player performance.

## 20 Introduction

21 The Indian Premier League (IPL) is a franchise-based T20 cricket league and currently ranks as 22 the second most lucrative sports league globally, generating $9.5 billion in revenue in 2023.

23 Since its inception in 2008, the IPL has attracted many of the world’s strongest cricketers, 24 providing a highly competitive platform to showcase their abilities. In this talent-packed 25 tournament, the Most Valuable Player (MVP) award holds immense significance as it is widely 26 regarded as a prestigious honor among cricketers. Currently, the method of determining this 27 award is arbitrary, limited in scope, and flawed in reasoning. This paper seeks to address these 28 shortcomings by developing a new metric to improve the existing rating system.

## 29 Overview of Cricket Rules

30 The fundamental objective in T20 cricket, the format used in the IPL, is to score more runs than 31 the opposing team within 20 overs (an over is a set of six balls delivered by a bowler/pitcher). 32 There are three main ways to score runs: fours, sixes, and running between the wickets. Four 33 runs are awarded when a batsman hits the ball past the boundary after it bounces at least once in 34 play (similar to a ground-rule double in baseball). Six runs are awarded when the ball crosses the 35 boundary on the fly (similar to a home run). Lastly, a run between the wickets occurs when a 36 batsman hits the ball into play, and both batsmen swap ends; each swap counts as one run. 37 Batsmen can swap ends multiple times, though typically do so once or twice to minimize the risk 38 of being run-out if the ball reaches the stumps before they do. A batsman is out if the ball is 39 caught on the fly by a fielder, they are run-out, or the ball hits the stumps behind them. When a 40 batsman is out, they are replaced and cannot bat again in that game. If 10 out of 11 batsmen are 41 out before all overs are bowled, the inning concludes. Refer to the appendix for additional details 42 on cricket-specific terms and rules mentioned in this paper.

## 44 The Traditional MVP Metric: A Flawed System

45 Historically, the IPL’s MVP award has been determined through metrics focused on individual 46 match events, assigning points as follows:

● Batting: 3.5 points per six, 2.5 points per four

● Bowling: 3.5 points per wicket, 1 point per dot ball

● Fielding: 2.5 points per run-out or stumping, 2.5 points per catch

50 While these metrics offer a straightforward means of quantifying contributions, they fail to 51 capture the full scope of player performance. For example, a batsman’s ability to score runs 52 quickly (strike rate) or a bowler's efficiency in conceding runs (economy rate) are not adequately 53 emphasized, as accumulating boundaries and dot balls do not necessarily reflect these qualities. 54 Furthermore, situations such as the following arise: for two batsmen who each face six balls, a 55 batsman scoring 8 runs through 1s or 2s is credited with fewer MVP points than a counterpart 56 who scores one single boundary and five dot balls, despite the former contributing more runs. 57 Similarly, a bowler who concedes 20 runs in their allotted 4 overs with 4 dot balls would earn 58 fewer MVP points than one who concedes 40 runs with 3 dot balls—an illogical outcome. These 59 flaws could result in players who make significant contributions to their teams’ success—without 60 relying on boundaries, wickets, or dot balls—being undervalued.

## 61 Established Cricket Statistics

62 While cricket analytics are still in a relatively early stage of development, several statistics have 63 traditionally been used to rate player performances. Although these metrics are not currently 64 included in the IPL’s MVP rating system, this paper will incorporate the following:

## 65 Batting Statistics

Runs Scored (RS): The total number of runs scored by a batsman in the season.

Strike Rate (SR): The speed at which a batsman scores runs.

Batting Average (BA): The number of runs a batsman scores per dismissal.

## 71 Bowling Statistics

Balls Bowled (BB): The total number of balls bowled by a bowler in a season.

Runs Allowed (RA): Total runs conceded by a bowler in a season.

Economy (Econ): Measures the runs a bowler concedes per over.

Wickets (W): Wickets attributed to a bowler for a season.

Balls per Wicket (BpW): The average number of balls bowled per wicket taken.

B𝑝𝑝W

=

𝐵𝐵𝐵𝐵𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑊𝑊𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏

## 79 Methodology

80 From a general perspective, our model incorporates several devised metrics inspired by Strike 81 Rate, Batting Average, Economy, and Balls per Wicket. These metrics are benchmarked against 82 league averages for the season and adjusted based on the frequency of actions. Ultimately, 83 individual player contributions are aggregated by team and correlated with the team’s winning 84 percentage for the season.

## 85 Statistics Developed for Our Model

86 In cricket, player evaluation metrics such as Strike Rate, Batting Average, and Economy provide 87 insight into performance but often lack contextual weight. The devised metrics in this model 88 address this gap by assessing batting and bowling efficiency in relation to team success, aiming 89 to isolate individual contributions from overall team dynamics. Each formula has been 90 constructed to capture distinct aspects of a player’s efforts relative to the league standards. This 91 approach enhances the model’s ability to quantify a player’s impact, especially under high 92 variability conditions, such as match-to-match fluctuations in strike rates, dismissals, and bowler 93 economies.

## 1. Hitting Value (HV):

97 5

98 The Hitting Value (HV) metric quantifies a batsman’s ability to score efficiently, comparing

99 their strike rate to the league average. A higher strike rate indicates faster scoring, which is

100 critical for maximizing a team’s total runs within a limited number of overs. The difference

101 between an individual batsman’s strike rate and the league average measures their scoring

102 efficiency relative to others. Dividing by 100 sets this difference in runs per ball, as strike rate is

103 calculated per 100 balls. Multiplying by the batsman’s total runs scored scales the HV to reward

104 players who sustain high efficiency over larger volumes of runs, thereby capturing both the

105 speed and volume of scoring. This approach also penalizes batsmen with low strike rates,

106 especially if they face a high number of deliveries without significant run production, as this

107 hampers team momentum.

## 2. Dismissal Weighted Runs Above Average (dwRAA):

111 112 dwRAA accounts for a batsman’s consistency and output by factoring in their batting average 113 relative to the league, scaled by the number of times they are dismissed. The metric compares the 114 batsman’s average against the league average, capturing their consistency in converting 115 appearances into runs. Multiplying by the number of dismissals controls for batsmen who score 116 heavily without frequent dismissals, ensuring that an exceptionally high average due to few 117 dismissals does not unduly skew a player’s evaluation. This normalization maintains balance by 118 rewarding consistent scoring and penalizing those with inflated averages due to minimal 119 dismissals. 120

## 3. Runs Below Average (RBA):

123 124 RBA assesses a bowler’s ability to restrict scoring, a critical skill for maintaining team control

125 over run rates in limited-overs cricket. The formula first divides the league’s average economy

126 rate by 6, converting the rate into runs conceded per over. By multiplying by balls bowled, an

127 expected runs value can be derived based on league norms. Subtracting the actual runs allowed

128 compares performances to league average: a positive RBA indicates that the bowler concedes

129 fewer runs than expected, reflecting an ability to limit scoring. This metric effectively rewards

130 bowlers who maintain control over opposing batsmen and sustain a low economy rate, both of

131 which are essential in matches.

## 4. Wicket Frequency (WF):

135 136 WF captures a bowler’s effectiveness in taking wickets, which directly contributes to disrupting 137 the opposition’s batting lineup. The formula computes the frequency of wicket-taking by 138 comparing the average balls per wicket across the league to the bowler’s balls per wicket. 139 Multiplying this ratio by the bowler’s total wickets rewards bowlers who maintain efficiency while 140 taking a high number of wickets. A high WF score is indicative of a bowler who consistently

141 requires fewer deliveries to take wickets, constantly disrupting the opposing batting lineup and 142 therefore limiting the opposition’s scoring potential. 143 144 Each metric aligns with core principles of cricket strategy, where efficiency and consistency are 145 valued over raw output. For batting, HV and dwRAA prioritize fast and consistent run-scoring, 146 which are essential for accumulating a competitive total. Similarly, RBA and WF for bowling 147 emphasize economy and wicket-taking frequency, both critical to curbing an opposing team’s 148 progress. By anchoring each metric to league averages, the model ensures fair comparisons 149 among players with varying roles. It balances traditional measures of performance (strike rate, 150 average, economy) with a more nuanced approach that reflects actual game impact.

151 The model also incorporates fielding, recognizing that taking catches and effecting run-outs and 152 stumpings (stumpings are a specific type of run-out) are critical to a team’s success. Given the 153 lack of fielder tracking data to evaluate the difficulty of individual performances, the model uses 154 two fielding statistics: the number of catches taken and the number of run-outs and stumpings 155 effected. However, unlike the existing system’s arbitrary weightings, the multivariate regression 156 model accounts for the lesser impact of fielding performances on team success compared to 157 batting and bowling metrics.

## 159 Data

160 The data for this paper was obtained from two sources: the Cricsheet Database and the official 161 IPL website. The Cricsheet Database was used for play-by-play analysis, while the IPL website 162 provided data on team performance per season, existing MVP ratings, and fielding statistics,

163 including catches and run-outs. This model utilized data from the 2021 to 2024 IPL seasons, as 164 fielding data has been consistently available only since 2021. Data from the 2022 to 2024 165 seasons was used for training, while the 2021 season was used for testing. 166

## 167 Multivariate Regression Model

168 For the training dataset, each of the six aforementioned metrics was Z-scored for every player in 169 individual seasons and then aggregated for each team. The aggregated Z-scores were 170 subsequently correlated with each team’s winning percentage. The logic is that teams with 171 stronger metric aggregates should win more matches overall, regardless of whether the 172 contributions come from a large group of above-average players or a single exceptional 173 performance. The optimized equation is as follows: 174

175 176 177 Ultimately, when applied to our testing data, this model had an R2 value of 0.80, greater than the 178 existing method’s value of 0.66.

## 179 Correlation Graphs of IPL Data (2021-2024)

180 181 Overall, our correlation is significantly stronger than that of the current metric, even when 182 evaluated using data from a single season. 183

## 184 Residual Plot

185 186 The residual plot above shows no visible trend, indicating that the regression model has no 187 consistent systematic error. 188

## 189 Player MVP Calculation

190 Using the equation above, individual player ratings are calculated with a minor adjustment. To 191 ensure that specialist batsmen or bowlers are not unfairly penalized for poor performance or 192 limited opportunities in the opposite discipline, players with lower ratings in either batting or 193 bowling (after the coefficients for dwRAA and HV or RBA and WF are applied and the metrics 194 summed) are capped at a minimum rating of 0. In other words, a batsman with a positive batting

195 rating (after considering Z-scored HV and dwRAA) and a negative bowling rating will have the 196 bowling rating set to 0. However, for players with below-average performances in both 197 disciplines, only the lower of the two ratings will be set to 0, while the other rating remains 198 negative. 199 200 Player Rating Distribution

201 202 The graph above illustrates that the data is mostly normally distributed, suggesting that our rating 203 system effectively captures a balanced distribution of both stronger and weaker players. Most 204 players are clustered around the league average rating, corresponding to a Z-score of 0.

## 205 Discussion

206 The multivariate regression model proves to be a stronger predictor of team performance 207 compared to the existing metric. Additionally, the optimized coefficients reveal several key 208 implications, including:

● Appropriate Weighting of Disciplines: Both batting and bowling are given roughly equal weight, as the sums of the coefficients for the batting and bowling statistics used in the regression model are nearly equal. This balance is a strength of our model, as it reflects the necessity for a cricket team to perform well in both disciplines to win matches. Fielding, on the other hand, is given significantly less weight, as fielding contributions are one of many ways to dismiss batsmen. The model correctly places less importance on fielding compared to batting and bowling, reflecting the relative impact of these disciplines on team success.

● Batting – Balance Between Volume and Efficiency: For batting, the volume of runs a batsman scores is his most critical quality. However, the efficiency with which a batsman scores runs remains significant. According to our model, a batsman cannot be effective by excelling in only one of these aspects – he must perform well in both. This is logical, since a highly rated batsman should be able to score runs consistently without negatively impacting the team’s momentum through slow run-scoring.

● Bowling – Control Over Wickets: There has been an age old debate in cricket that questions whether taking wickets or conceding fewer runs is more important. Our model suggests that bowlers who control the run rate are far more valuable than those who frequently take wickets. The coefficient for RBA is over 3.5 times greater than that of

WF, a disparity much larger than the difference between the batting statistics, where dwRAA is less than twice as significant as HV. Particularly in the IPL, where matches are played over 20 overs and teams are rarely all out, it is sensible that controlling runs is a greater contributor to winning matches than taking wickets.

## 231 Results

## 232 Comparison of the Top 10 Players Across Both Metrics

233 234 Ratings are scaled to 100

235 In the tables above, the top 10 players from the past four years have been normalized to a 100236 point scale for both the existing MVP metric and our Impact Rating. The most notable difference 237 between the results of our Impact Rating and the traditional MVP metric lies in the spread of the 238 data. Using the traditional MVP metric, the rating gap between the third-place player and the 239 best player is larger than the gap between the best and the tenth-best player in our Impact Rating. 240 Since this list consists of established, world-class international cricketers, the compression in our

241 results underscores a key strength of our method: its ability to provide a more balanced 242 assessment across the player pool.

243 Our Impact Rating also highlights strong performances across a season that may have lacked the 244 glamor of wickets and boundaries. For instance, Jasprit Bumrah, ranked 4th on our list, had an 245 exceptional season as a bowler in 2024, which statistically was the most batting-dominated IPL 246 season in history. However, his strength manifested less in taking wickets and more in restricting 247 run-scoring, even as his counterparts struggled to do the same. While Bumrah does not even 248 figure in the top 10 players under the traditional metric (having less than 60% of the impact of 249 Sunil Narine), our model appropriately credits his performance with a rating of 90% of Narine’s 250 impact.

251 There are, however, some agreements between the two rating systems since strong performances 252 often include scoring boundaries and taking wickets. The top three players are identical, 253 featuring Sunil Narine, who excelled in 2024 as both a top batsman and bowler, as well as Jos 254 Buttler and Shubman Gill, both of whom were the highest run-scores of their respective seasons 255 by a considerable margin.

## 257 Case Studies

258 To demonstrate the efficacy of our new calculation compared to the existing MVP metric, this 259 section examines the 2021 IPL season performances of two key players: Harshal Patel and AB 260 de Villiers.

261 Harshal Patel: 262 Patel was named the MVP of the 2021 season for his record-breaking 32 wickets. However, his 263 high economy rate, particularly in one of the lowest-scoring seasons ever, undermined his overall 264 contribution. Despite his wicket-taking prowess, he conceded a significant number of runs per 265 ball, reducing the overall effectiveness of his performance. Our model places a greater value on 266 bowling control (RBA) than on wicket-taking (WF). While Patel’s WF was among the highest of 267 the season, it was offset by a negative RBA, ultimately lowering his overall rating. In our system, 268 he ranked 44th for the season. This, while above average, reflects the detrimental impact of his 269 high economy rate compared to his wicket-taking achievements.

270 AB de Villiers: 271 De Villiers was ranked 40th in the traditional MVP rankings in 2021. While his batting strike 272 rate and average were above the league average, his lower total runs limited his MVP score. In 273 contrast, our model accounted for the impact of his consistently high strike rate even with a 274 relatively modest number of boundaries, as well as his fielding contributions — he was the top275 rated fielder of the season. As a result, our model ranked him 8th for the 2021 season, reflecting 276 a more comprehensive assessment of his all-round contribution.

## 278 Conclusion

279 The new MVP metric provides a more accurate representation of a player's contribution to their 280 team's success by considering a broad range of factors and leveraging advanced statistical 281 techniques to quantify individual performances. Compared to the existing rating system, it 282 significantly improves the ability to capture a player's all-round impact.

283 Despite its strengths, the current model has room for improvement. While the context284 independent nature of the metric makes it accessible and easy to interpret for players and fans, an 285 ideal rating system would account for the context of player contributions. For example, our 286 method treats a batsman scoring 40 runs off 20 balls in a losing effort the same as one achieving 287 the same score while facing the opposition’s best bowlers in a match-winning situation. Future 288 iterations of the metric could integrate contextual factors, such as the strength of opposing 289 players and the significance of key match moments, to deliver a more nuanced evaluation.

290 A significant limitation of cricket analytics lies in the availability of comprehensive data. The 291 data used in this model was limited to play-by-play scoring data, which restricts the depth of 292 analysis, particularly in areas such as strategy execution. Additionally, there is a scarcity of 293 scholarly research on player impact valuation, with limited exploration into alternative 294 performance metrics. As cricket analytics continues to evolve, more effective statistics and 295 innovative data collection methods will emerge, offering exciting new possibilities for refining 296 player evaluations.

297 298

## 299 Acknowledgements

300 We would like to thank Professor Adi Wyner from the Wharton Moneyball Academy for 301 inspiring us to build this model. Additionally, we are grateful to Zeke Kelz, Jonathan Pipping, 302 Ryan Brill, and Rafiz Sadique for their invaluable guidance throughout the development and 303 presentation of our model. 304

## 305 Appendix: Glossary of Cricket Terms and Rules

## 306 Cricket to Baseball Dictionary:

● Bowler = Pitcher

● Batsman = Hitter

● 4s ~ ground rule doubles

● 6s ~ home runs

● Batting Average ~ Player runs scored per appearance

● Wickets/Dismissals = Outs

● Economy (ECON) ~ ERA per over (six balls)

● Run-out ~ Groundout

● Catch ~ Flyout

● Dot Balls ~ Strike

## 318 Batting:

## 319 Ways to score runs:

● Sixes (6s) - A batsman hits the ball over the boundary on the fly. (Comparable to a home run in baseball)

● Fours (4s) - A batsman hits the ball past the boundary after it bounces in play at least once. (Comparable to a ground-rule-double in baseball)

● Running Between the Wickets/Stumps - A batsman hits the ball into play, and both batsmen swap ends. Each successful swap counts as one run.

## 326 Batting Average (BA):

BA = (Number of runs a batsman scores) / (Number of times a batsman gets out)

## 328 Strike Rate (SR):

SR = (Number of runs a batsman scores) / (Number of balls a batsman faces) * 100

## 331 Bowling/Fielding:

## 332 Wickets (W): Number of batsmen a bowler dismisses (gets out)

## 333 Economy Rate (Econ):

Econ = (Number of runs a bowler concedes) / (Number of overs bowled)

335 Run-Outs: A run-out occurs when batsmen are running between the wickets and the fielding

336 team gets the ball to one of the ends before a batsman has crossed the crease line near the wicket.

337 Dot Balls (Dot): A delivery (pitch) that does not result in any runs being scored. (Comparable to

338 a strike in baseball)

## 340 References

341 Board of Control for Cricket in India. "MVP Rating." IPLT20. Last modified May 2024.

Accessed November 8, 2024. https://www.iplt20.com/stats/2024.

344 Cricsheet. "Match Data." Cricsheet. Last modified November 8, 2024. Accessed November 8,

2024. https://cricsheet.org/matches/.

347 Pearlberg, Benjamin. "Could Moneyball Methodology Improve Indian Cricket?" Firstpost. Last modified August 2024. Accessed November 8, 2024. https://www.firstpost.com/opinion/could-moneyball-methodology-improve-indiancricket-13806487.html.
