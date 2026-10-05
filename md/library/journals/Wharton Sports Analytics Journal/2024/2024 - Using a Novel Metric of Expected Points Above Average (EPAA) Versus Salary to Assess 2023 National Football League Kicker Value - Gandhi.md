<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - Using a Novel Metric of Expected Points Above Average (EPAA) Versus Salary to Assess 2023 National Football League Kicker Value - Gandhi.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/using-a-novel-metric-of-expected-points-above-average-epaa-versus-salary-to-assess-2023-national-football-league-kicker-value/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2024 -->
<!-- authors: Jayan Gandhi -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Using a Novel Metric of Expected Points Above Average (EPAA) Versus

Salary to Assess 2023 National Football League Kicker Value

Jayan D. Gandhi

Buckingham, Browne & Nichols School

37 38 39 40

41 Abstract 42 43 In the National Football League (NFL), team salary caps mean money spent on players on one 44 position reduces the ability to spend resources on others. Salary cap hits for kickers in 2023 45 ranged from under $1M to almost $6M, with cash salaries exhibiting an even wider range (<$1M 46 to >$9M). Kickers have been primarily judged on the overall accuracy of their kicks within 47 specific kick ranges. However, such an approach does not include factors such as wind, 48 humidity, temperature, and other variables that could affect the probability of a successful kick. 49 This paper describes a new, up-to-date metric, expected points above average (EPAA), that 50 incorporates significant weather-related factors in addition to kick distance to evaluate kicker 51 performance. Subsequently, each kicker's EPAA is compared to their salary to assess the cost of 52 performance to determine kicker value. In 2023, there was no correlation between EPAA and 53 kicker salaries. The lack of correlation between EPAA and salary presents an opportunity: NFL 54 executives can use this metric as a screening tool to identify kickers that can deliver strong 55 results at a relatively low cost to generate a source of potential competitive advantage in a salary56 cap-constrained environment. Using this method for the most recent NFL season in 2023, twelve 57 kickers were found to have high EPAA ratings and low cost and warrant further consideration as 58 players who could improve rosters. Conversely, four kickers were identified as having low 59 EPAA scores and high salaries and similarly could be evaluated further for potential 60 replacement. 61 62 Introduction 63 In 2023, National Football League (NFL) teams were limited to a $224.8 million salary cap 64 threshold. The NFL enforces a “hard cap,” meaning the cumulative spend for all players on a

65 team must stay below the designated level, and money a team spends on one player, by

66 definition, reduces the money available to spend on others. For many teams, quarterbacks will be

67 the highest-paid players, and top NFL quarterbacks can utilize over $50 million of cap spend by

68 themselves. While NFL kickers fall towards the lower end of the position spending range, NFL

69 kicker salaries vary meaningfully (Sportrac). In 2023, kicker salaries ranged between below $1M

70 to over $9M. Through salary cap management strategies based on calculation rules, NFL

71 executives have the ability to alter “cap hit,” but in spite of these measures, kicker salary cap hits

72 in 2023 had a wide range of below $1M to almost $6M.

Kickers are critical members of football teams and have two main purposes: kickoffs,

74 where they kick the ball away to the other team during the start of a half or after a score, and

75 kicking attempts. Kicking attempts consist of extra points: a kick from thirty-three yards away

76 worth one point after a team scores a touchdown, and field goals (FG), a kick varying in distance

77 based on where the team offense is on the field, worth three points. A successful kick consists of

78 a kicker kicking the football between the goalposts.

Many have measured kickers' effectiveness using various methods and performance

80 metrics for different purposes. For example, prior work describes kicker value for fantasy

81 football or evaluates kickers in clutch, high-pressure situations (Klein, Riske). The most common

82 metric used to evaluate kickers is their accuracy for specified kick distance ranges. While this is

83 a useful measure, it does not precisely assess how good a kicker is since many other factors,

84 particularly weather, can affect the probability of a successful kick. To address this limitation

85 and to attempt to determine which variables affect kick accuracy, several others have created

86 logistic regression models to predict the probability of kick success by incorporating weather

87 variables and other factors such as game situations (Clement, Long, Stuart, Riske, Pasteur and

88 Cunningham-Rhoades, Osborne and Levine). These prior analyses have two limitations. First,

89 they are dated and kickers have improved over time (Stuart). Moreover, while kick distance is a

90 significant factor in assessing kick success probability across all prior work, other weather

91 variables such as wind speed are noted to be meaningful in some models but not others (Delong,

92 Clement), again underscoring the need for a model with recent, up-to-date data. Second, prior

93 analyses only focused on assessing kicker performance and did not measure the value of a kicker

94 by mapping kicker performance to the cost of obtaining those results. This paper addresses both

95 of these limitations.

In this analysis, I measure performance through the creation of a new logistic regression

97 model with up-to-date data to determine the expected field goal and extra-point success

98 probability based on kick distance and several important weather-related factors including wind

99 speed, humidity, presence of precipitation, and temperature. Utilizing this model, the expected

100 points that a kicker should have had in the most recent 2023 NFL season are determined, and

101 then the kicker's actual performance is compared to his expected value to generate a metric

102 called expected points above average (EPAA). Each kicker’s 2023 performance using EPAA is

103 compared to his 2023 salary to determine which kickers offered the most value to their NFL

104 teams in 2023. If no or minimal correlation between EPAA and salary exists, this approach

105 would create a useful screening tool to identify kickers with a high EPAA and low salary,

106 thereby offering a source of potential roster improvement and competitive advantage in a salary

107 cap-constrained environment.

111 4

112 113 Methods 114 115 Data 116 I used the nflfastR (v2.3.1) dataset, which contains play-by-play data beginning in 1998. From 117 the package, only plays involving field goals or extra points from 2015 to 2023 were included to 118 allow for consistency in kicking rules. Variables studied for association with kick likelihood 119 included distance, wind speed, humidity, type of surface, and rain. The presence of rain was 120 determined from the weather string and included rain, snow, showers, and ‘Cloudy, chance of 121 rain increasing up to 75%.’ 122 123 Creation of Prediction Model 124 Variables noted to be significant on univariate analysis with a p-value of <0.05 (Table 1) were 125 then used to create a multivariable logistic regression model, a tool used to predict a binary 126 outcome, such as whether a kick goes in based on input variables. Distance was studied as both a 127 linear and quadratic variable. The linear distance was selected as the best fit for the data by 128 comparing the Akaike information criteria (AIC) metric. Additionally, I studied interactions 129 between significant variables that are associated with kick likelihood. Temperature on univariate 130 analysis was not significant but became significant when an interaction between temperature and 131 distance was included. The final multivariable model included an interaction term between 132 temperature and kick distance. The type of surface was not found to be significant on univariate 133 analysis and was not included in the model. Only data points with complete values for each of 134 these variables were included (16,768 of 20,905 kicks). 135

136 The logistic regression equation is represented as follows: E(Kick) represents the expected log

137 odds for the success of a kicking attempt with coefficients (Table 2).

𝐸𝐸(𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘) = 𝐵𝐵0 + 𝐵𝐵1 ∗ 𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷 + 𝐵𝐵2 ∗ 𝑊𝑊𝑊𝑊𝑊𝑊𝑊𝑊𝑊𝑊 + 𝐵𝐵3 ∗ 𝑇𝑇𝑇𝑇 + 𝐵𝐵4 ∗ 𝐻𝐻𝐻𝐻𝐻𝐻 + 𝐵𝐵5 ∗ 𝑇𝑇𝑇𝑇 ∗ 𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷

## 141 Calculation of EPAA (expected points above average)

142 Once the model computed the probability of making each kick, I assessed each individual

143 kicker’s season and determined how many points they earned relative to how many points that

144 the average kicker would have had with the same opportunities to calculate EPAA. When

145 weather information was missing for an individual kick in indoor stadiums, values for weather

146 were imputed with average humidity, temperature of 70 degrees, and no rain. Otherwise, kicks

147 with missing weather values were not used in the individual player calculations.

148 149 This metric allowed determination of how many “extra points'' each kicker added to their

150 respective teams relative to an average kicker. For example, if an average kicker had an eighty

151 percent chance of making a field goal, which is worth three points, the expected points would be:

152 0.8 * 3 = 2.4. If the individual kicker made this field goal and garnered 3 points for their team,

153 the EPAA value from this kick would be 0.6 (3.0 minus 2.4). The EPAA from a season was the

154 summation of each of the kicks for an individual kicker and could be negative if the kicker

155 performed below average.

156 157 Determination of player value

158 Individual kicker salaries for 2023 were assigned based on cash spent in the overthecap.com

159 database (Over The Cap). In the scatterplot (Figure 3), each individual kicker from 2023 is

160 represented by a point whose location is a function of his salary (x-axis location) and EPAA (y161 axis location) in order to assess kicker value. 162 Results 163 The dataset consisted of 8,714 field goals (FGA) and 10,580 extra points (PATA) attempts by 164 102 kickers from the 2015-2023 NFL seasons. The association between individual variables and 165 kick likelihood was studied in Table 1. As expected, longer kick distance was strongly correlated 166 with lower kick success. In addition, humidity, wind speed, and the presence of rain were 167 significantly associated with a decreased likelihood of kick success. 168 169 Table 1 - Univariate associations with kick success

Variable Kick distance (mean, yards)

Kicks made Kicks missed p-value* n=15,040 n=1,728

(89.7%)

(10.3%)

34.9

42.5

<0.001

Temperature (mean, oF)

60.2

59.7

0.29

Humidity (mean, %)

59.4

60.8

0.009

Wind Speed (mean, mph)

8.0

8.5

Rain No Yes

14160 880

1592 136

Season (not included in prediction model)

170 *T-test for continuous variable and chi-squared test for categorical 171

<0.001 0.001

0.27

172 The coefficients for the prediction model are shown in Figure 1 using the univariate predictors, 173 as well as temperature and its interaction term with distance. 174 175 Figure 1- Model Coefficients 176

177 178 179 All variables remained significant at a p-level of less than 0.05 in the multivariable model. 180 Decreasing kick distance, higher temperature, lower wind speed, lower humidity, and lack of 181 rain increased the likelihood of a successful kick. 182 183 Figure 2 displays the likelihood of kick success by distance, where more recent seasons (2021184 2023) are shown in blue, older seasons in red (2015-2017), and those in the middle (2018-2020) 185 are in green. Kick probabilities by distance were not noticeably different over the study period. 186 187 188 189 190 191 192 193

194 Figure 2 - Probability of kick success by distance across seasons

195 196 197 The EPAA for the 2023 season for each individual kicker was calculated, and annual salaries for 198 each player were obtained from Overthecap.com and spotrac.com. Kickers who earned under 199 $750,000 cash compensation in 2023 were excluded from as they largely reflected those who 200 were cut or injured and did not kick enough to warrant inclusion in the EPAA vs salary analysis. 201 202 These values were plotted in 2 dimensions (salary and EPAA) in Figure 3. We can see that there 203 is no correlation between EPAA and salary values. In the green box are players with good value 204 in that they have high EPAAs and are relatively less costly. In the red box are players who have 205 low value; namely, they have low EPAA scores and are expensive. Players who fall outside these

206 boxes are those of intermediate value: those who have high EPAAs and are costly or those with 207 low EPAAs and less costly. 208 209 Figure 3 - Individual players 2023 salaries plotted by EPAA 210

211 212 213 214 215 216 217

218 In total, 12 kickers were identified to be high value, and 4 kickers of poor value as shown in 219 Table 2. 220 Table 2 - Individual kicker EPAA values and cash salary for 2023

221 222 223

224 Discussion 225 In a salary cap-constrained environment, kicker value should go beyond measuring 226 performance. Rather, the value should be determined by mapping effectiveness versus the cost to 227 achieve it. Therefore, two inputs are needed: 1) A metric to assess performance and 2) Kicker 228 salaries to assess cost. To evaluate performance, I created a logistic regression model that 229 included all field goal attempts and extra point attempts from 2015-2023, where data were 230 available. 2015 was chosen as the start year for analysis as that was the first year after the extra 231 point distance was moved such that the snap was from the 15-yard line instead of the 2-yard line. 232 Of the variables tested, kick distance and wind speed were most significant when determining 233 the probability of a kick going in. Temperature was not significant by itself but became highly 234 significant when an interaction with distance was included. This makes sense as colder air is 235 denser, and the effect should be evident at longer distances and is consistent with prior work that 236 cited that temperature matters when it is very cold (below freezing) for field goals beyond 25 237 yards (Burke). The prediction model found humidity to be a significant variable. Increasing 238 humidity is associated with decreasing air density which might allow the ball to travel farther. 239 However, greater humidity could also make the ball wet which could cause a kick to be more 240 difficult or affect the quality of the hold. Data on hold quality was not easily available and testing 241 hold quality in univariate analysis or with an interaction with humidity would be interesting for 242 future study. Like humidity, the presence of rain also was modestly significant, and this finding is 243 similar to findings in prior work. Collectively the prediction model was largely comparable to 244 other efforts. Kick distance, not surprisingly, was the variable that had the lowest p-value when 245 determining kick success. Humidity was not present or tested in many other prior models, but its 246 effect appears modest and is potentially confounded by hold quality.

Kicker effectiveness in 2023 was determined by using the kicker’s actual performance in

248 2023 and compared to what the model would have predicted for a kicker under similar

249 conditions. In 2023, EPAA ratings ranged from 14.98 (Harrison Butker, Chiefs) to -12.97 (Chad

250 Ryland, Patriots). This means Harrison Butker, the kicker with the highest EPAA score,

251 generated almost 15 points above what would have been expected from the average kicker

252 kicking the same field goals and extra points. The magnitude of ~15 EPAA points is quite

253 meaningful, as it is possible that these extra points could have made a difference in helping the

254 Chiefs win games. Even if the extra points above average did not produce the winning margin,

255 the performance of the kicking game can alter several strategic decisions and choices that could

256 alter the trajectory of a game. The lowest EPAA score was generated by Chad Ryland of the

257 Patriots, who anecdotally was thought to have a substandard season.

Beyond assessing individual kicker performance using EPAA, to determine kicker value,

259 a player’s EPAA was evaluated versus their salary to assess the cost of obtaining those results.

260 While 2023 EPAA is based on 2023 performance and 2023 salary is likely based on expectations

261 derived from the prior year or years of performance, it is still a valuable comparison to assess

262 how a kicker performed relative to his contract. What is noticeable in Figure 3 is that no

263 correlation between EPAA and kicker salaries appears to exist. This is possibly because 2023

264 salaries are mainly based on expectations derived from historical performance, and many

265 kickers, like players at other positions, outperformed or underperformed their contracts. Kickers

266 in the green square in Figure 3 represent the best value–they have high EPAA scores while

267 costing the team less money than many of their peers. Conversely, kickers in the red rectangle

268 have below-average EPAA scores while costing teams a lot of money. Table 2 groups kickers

269 into high-, intermediate-, and poor-value categories. High-value kickers all generated at least a

270 positive EPAA score of 4.83 while costing their team less than $5M cash salary in 2023. Poor

271 value kickers had negative EPAA scores and cost teams over $6M in cash salary. Interestingly,

272 some kickers generally considered to be among the best in the game, such as Justin Tucker of the

273 Ravens, who generated a positive 4.86 EPAA in 2023 and would have made the high-value list

274 based on performance but did not because of their relatively high salary and were dropped to the

275 intermediate value category.

There are several limitations to this analysis. It’s possible that NFL executives value

277 specific attributes of performance not captured by EPAA. For example, EPAA scores a kick

278 relative to its predicted probability of going in but not on strategic value. “Clutch kicks,” or kicks

279 in high-pressure situations, are not given any extra weight in the model. Similarly, it’s possible

280 some executives would place greater value on long-distance kicks because it shortens the field

281 for the team’s offense, and a missed kick from afar would set the opposing team up with a good

282 field position. While longer distance kicks with a lower probability of going in offer potentially

283 more EPAA points if a kick goes in, it is possible that a kicker can generate a high EPAA from a

284 large volume of easier kicks. Further, there is also potential for selection bias in the model in

285 terms of unequal opportunities to assess kick performance. For example, only the best kickers

286 may get a chance to attempt longer, lower-probability field goals, and therefore, the data for

287 longer distances may not reflect the entire range of kickers. This selection bias increases the

288 expected probability of kick success at longer distances relative to an average kicker and

289 therefore lowers collective EPAA scores for kickers that attempt deep kicks. Moreover, it’s

290 possible that an excellent kicker has a low EPAA simply because he is on a very strong offense

291 that scores touchdowns often and has fewer field goal attempts. However, EPAA, even in this

292 case, can be helpful to calculate since it captures utilization–a team that relies less on its kicker

293 for field goals may not want to allocate as many dollars to the position.

These limitations mean EPAA should not be considered the definitive measure of kicker

295 effectiveness. Rather, EPAA could be used as a screening tool and a good starting point to

296 evaluate kicker performance because it is a quantitative, objective metric that aims to account for

297 multiple variables outside of only accuracy and kick distance. Other limitations in the analysis

298 could be attributed to the model itself. I was not able to incorporate variables such as wind

299 direction, hold quality, or altitude. Wind direction and hold quality were difficult to find and/or

300 had lots of missing data. I tested kicks from Denver (city at high altitude) on univariate analysis

301 as a proxy for altitude, but this was not found to be significant (data not shown) though others

302 have found kicks from Denver have success probabilities similar to fields goals that are several

303 yards shorter from lower altitude locations. To estimate the cost of performance, I used the 2023

304 cash salary as this number rather than the salary cap number, which is the actual dollars a team

305 spent on the player in that calendar year. It’s possible that a cash salary each year does not reflect

306 an average salary, given teams can move cash around in a multi-year contract for salary cap

307 management. Nonetheless, the actual cash spent reflects the true cost for that calendar year.

308 Finally, I only mapped 2023 EPAA versus 2023 salaries. It is possible that EPAA and salary

309 could be correlated in other years.

## 311 Conclusions

312 EPAA is an up-to-date metric that utilizes critical weather-related factors in addition to typically

313 used factors of kick accuracy and distance to assess kicker performance. When comparing EPAA

314 to kick salaries in 2023, no correlation exists. While EPAA may not capture everything

315 important to NFL managers, at a minimum, comparing EPAA to salaries can provide NFL

316 executives with a useful screening tool to evaluate the value they are getting from their own

317 kickers and to assess value in other kickers. In 2023, twelve kickers screened well, generating a

318 high EPAA value while having low to intermediate salaries and warrant further consideration as

319 players who could potentially improve rosters at an attractive cost. Conversely, four kickers did

320 not fare well on this metric by having a negative EPAA score and a high salary and should be

321 evaluated further for potential replacement.

322 323

## 324 References

325 Burke, B. (2012, January 17). Temperature and Field Goals. Advancedfootballanalytics.com. https://www.advancedfootballanalytics.com/2012/01/temperature-and-field-goals.html

328 Clement, C. (2018, December 17). Three Point Plays: The Analytics of Field Goals.

Blogspot.com. https://passesandpatterns.blogspot.com/2018/12/three-point-playsanalytics-of-field.html

332 Klein, K. (2018, October 3). A Statistical Approach To Choosing Your Fantasy Kicker. Medium;

Medium. https://medium.com/@kkwrites/a-statistical-approach-to-choosing-yourfantasy-kicker-bbc00aec4790

336 Long, J. A. (2019, December 8). Building a statistical model for field goal kicker accuracy.

Jacob Long; Jacob Long. https://jacob-long.com/post/kickers-methods-notes/

339 NFL Rankings. (2024). Spotrac.com. https://www.spotrac.com/nfl/rankings/kicker/

341 Osborne, J. A., & Levine, R. A. (2017). Shrinkage estimation of NFL field goal success probabilities. Journal of Sports Analytics, 3(2), 129–146. https://doi.org/10.3233/jsa-

16140

345 Overthecap.com. (2023). 2023 Kicker Contracts and Salaries | Over The Cap. Over the Cap. https://overthecap.com/position/kicker/2023

348 R. Drew Pasteur, & Cunningham-Rhoads, K. (2014). An expectation-based metric for NFL field goal kickers. Journal of Quantitative Analysis in Sports, 10(1). https://doi.org/10.1515/jqas-2013-0039

352 Riske, T. (2022, January 21). Assessing the true value of an NFL kicker. PFF; PFF. https://www.pff.com/news/nfl-assessing-true-value-nfl-kickers

355 The Greatest Field Goal Kickers Of All Time II, Part I. (2015, September 8).

Footballperspective.com. https://www.footballperspective.com/the-greatest-field-goalkickers-of-all-time-ii-part-i/
