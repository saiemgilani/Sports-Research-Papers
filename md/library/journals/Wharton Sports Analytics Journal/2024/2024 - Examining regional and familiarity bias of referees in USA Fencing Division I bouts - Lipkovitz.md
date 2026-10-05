<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - Examining regional and familiarity bias of referees in USA Fencing Division I bouts - Lipkovitz.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/examining-regional-and-familiarity-bias-of-referees-in-usa-fencing-division-i-bouts/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2024 -->
<!-- authors: Rivka Lipkovitz -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Examining regional and familiarity bias of referees in USA Fencing Division I bouts

1 Rivka Lipkovitz 2 Proof School, San Francisco, CA, USA

3 Abstract 4 This study examines whether USA Fencing referees exhibit favoritism toward competitors from their 5 designated regions, as frequent officiating within local areas could establish familiarity and 6 potentially lead to unconscious bias. This issue is particularly relevant in foil and saber, where 7 referees make subjective judgments on "right-of-way" during simultaneous hits, and in epee, where 8 penalty decisions hold significant weight. Unlike other sports with subjective scoring that utilize 9 referee panels, fencing relies on a single referee, granting them considerable control over bout 10 outcomes. Despite the opportunity for prejudice, there are no studies of referee bias in fencing; this 11 study aims to be the first to do so. Utilizing a substantial dataset of 35,111 Division I pool bouts from 12 2012 to 2019, I applied linear and logistic regression models to analyze the effect of regionality on 13 score differentials and bout outcomes. The results revealed limited evidence of regional bias, with 14 nonsignificant negative effects in foil and saber and a minimal positive effect in epee. These findings 15 diverge from similar studies in other sports, suggesting that regular referee-player interactions do not 16 necessarily result in biased officiating. The minimal positive effect in epee suggests the need for 17 further investigation into how decision-making may differ between scoring and penalty calls. 18 Additionally, the findings highlight the necessity for more research on how referees’ relationships 19 with players influence their judgments.

20 Keywords: regional bias, familiarity bias, fencing, referee, discrimination, official, linear regression, 21 logistic regression, referee bias

22 1 Introduction

23 Fencing referees wield significant influence, acting as the sole arbiters who give penalties, judge

24 ambiguous touches, award points, and ultimately shape the outcome of a bout. Recently, the

25 subjectivity of fencing refereeing has come under scrutiny. On April 24, 2024, USA Fencing

26 suspended two referees (Wendell, 2024) who had “acknowledged communicating with each other

27 during an Olympic qualifying tournament in California” (Longman, 2024). It grew so concerned

28 about two other referees that it asked the sport’s global governing body to “ensure that those two

29 judges were no longer assigned to any matches involving Americans.” Historically, fencing

30 refereeing has always been subjective. In the 1900s, fencing was not electrified, requiring fencers to

31 persuade two side judges about the legitimacy of their hits. These judges would then communicate

32 their opinions to the main referee, who made the final decision. The subjective aspect of judging hits

33 created many opportunities for officials to cheat (Cohen, 2003).

Despite the advent of electronic scoring for all fencing weapons in recent decades, fencing

35 refereeing remains subjective. In foil and saber, the referee plays a crucial part due to the "right-of-

36 way" or “priority” rule, a subjective system determining which fencer scores a point when two

37 fencers land hits simultaneously. Czajkowski (2009) succinctly describes this dynamic: “in offensive

38 actions, [the fencer] fights to be ahead in gaining the right-of-way: he must be first to initiate the

39 attack (not only in his own but, above all, in the referee’s opinion).” While the concept of "right-of-

40 way" is straightforward, its nuances are intricate and challenging to quantify. Due to the complexity

41 of determining priority, a referee is responsible for making the decisive call on points at tournaments.

42 This responsibility makes fencing bouts particularly susceptible to referee bias, as a biased referee

43 may choose not to award a point to a fencer who initiates a well-defined attack. Crucially, priority

44 decisions must be made within seconds, and fencing actions occur at high speeds, requiring referees

45 to process complex information and render judgments almost instantaneously. This time pressure

46 adds another layer of complexity to the referee's task and potentially increases susceptibility to bias.

However, referees can make subjective decisions even in the absence of “right-of-way.” In

48 epee fencing, where both fencers get a point on simultaneous hits, referees still maintain the authority

49 to subjectively issue penalties for common infractions or situations. For example, a referee needs to

50 distinguish between “jostling,” which incurs a penalty, and incidental body contact between fencers,

51 which does not result in a penalty. This scenario is like soccer, where players are permitted to use

52 their body to gain control over the ball but are prohibited from pushing or shoving their opponents.

53 Minor and first-time infractions lead to an issuance of a yellow card, serving as a warning without

54 impacting the score. Major infractions or repeated offenses lead to a red card, awarding the opponent

55 an additional point. Rarely, egregious offenses can lead to black cards, resulting in exclusion from

56 the tournament. With rare exceptions, such as late-stage bouts featuring video replay (where the

57 referee still holds final authority), fencers are generally prohibited from contesting rulings on priority

58 and penalty calls. At the elite Division I level tournaments—events significant for Olympic selection

59 and NCAA recruitment—referees' decisions can have considerable ramifications on the trajectory of

60 athletes' careers.

There is a wealth of literature examining referee bias, primarily in mainstream sports such as

62 soccer and basketball. Studies in other sports have presented many ways that referees can be

63 influenced, such as home-court bias (Boyko et al., 2007), racial bias (Magistro & Wack, 2023),

64 nationalistic bias (Lyngstad et al., 2020), linguistic bias (Faltings et al., 2023), reputation bias (Bose

65 et al., 2021), and referee-team familiarity bias (Hlasny & Kolaric, 2015). However, the niche sport of

66 fencing has received little attention in this regard, with scant research on referee bias. Despite modern

67 fencing dating back to the 18th century and being one of the few sports included in every modern

68 Olympic Games, officiating bias remains surprisingly understudied. Existing literature on fencing

69 bias relies on surveys of referees and fencers (Abdelfatah et al., 2022), or attempts to automate

70 refereeing (Mo, 2022; Sunal et al., 2021). This study aims to be the first to investigate the presence

71 and extent of referee bias in fencing competitions. Fencing offers a unique case study due to the

72 significant influence a single referee wields over the bout. In contrast to other sports with subjective

73 scoring, such as gymnastics or ski jumping, which utilize referee panels to mitigate the impact of an

74 individual referee’s preferences, fencing relies solely on a single referee, granting them substantial

75 control over the final score. Therefore, the magnitude of referee bias can be greater in fencing than in

76 other sports.

The Fédération Internationale d'Escrime is the international governing body for the sport of

78 fencing, and USA Fencing is the national governing body for fencing in the United States. This

79 national body has roughly 35,000 members, including competitive fencers and individuals such as

80 referees, coaches, and other active participants. These members belong to one of nearly 70 local

81 divisions based on their location of residence. Each division falls under one of six geographic regions

82 established by USA Fencing as illustrated in Figure 1. These regions play a vital role in qualifying

83 athletes for prestigious national tournaments like the Junior Olympics and National Championships.

84 To qualify, fencers must amass a minimum number of regional points, which are exclusively earned

85 at tournaments within their designated region. With approximately 20 regional events occurring

86 annually in each of the six geographic regions, fencers and coaches often travel to different divisions

87 to accumulate points. Additionally, to address the shortage of referees at regional-level tournaments,

88 organizers bring in officials from other divisions. As a result, fencers, coaches, and referees within

89 the same region connect through frequent interactions, gradually becoming acquainted and familiar

90 over time.

91 Figure 1: USA Fencing region map.

92 93 National-level fencing tournaments attempt to balance fairness with practicality. While referees are

94 barred from officiating athletes from their local division due to conflict-of-interest concerns, they can

95 officiate athletes from their broader region. This raises concerns about potential subconscious bias.

96 Research in other sports, such as Hlasny and Kolaric’s (2015) study on soccer referees, demonstrated

97 how familiarity can lead to systematic biases. Their findings suggested that referees awarded fewer

98 cards to teams they were more familiar with, and older referees, presumably with deeper existing

99 relationships, displayed greater home-advantage bias. They also argued that other trends of bias (such

100 home-court, racial, and prestige bias), could be attributable to “implicit lifelong bonds between

101 referees and players.” Similar findings emerged in baseball, where Mills (2013) demonstrated that

102 catchers, who have frequent interactions with the umpire, received fewer strike calls when batting

103 compared to other players. Moreover, Emerson et al. (2009) proposed that stylistic bias could

104 contribute to nationalistic bias in Olympic diving.

In fencing, referees' familiarity with clubs and fencers in their region could introduce

106 unintended biases. Having observed prior performances, referees may unconsciously form

107 preconceived notions about a fencer's technique or style. Bias may also emerge from a preference for

108 common regional fencing styles. Additionally, psychological phenomena such as the "mere exposure

109 effect" (Zajonc, 1968) could play a role, where repeated exposure to familiar fencers might lead to

110 more favorable judgments. To investigate potential regional bias in fencing referees, I analyze score

111 differentials and bout outcomes using linear and logistic regression. The hypothesis is that, in the

112 presence of regional bias, fencers will have a significantly higher score differential and chance of 113 winning when officiated by a referee from their own region.

114 2 Materials and Methods

115 I used web scraping to extract Division I pool bouts from USA Fencing's official results website

116 (https://usfencingresults.org/results/), over a seven-year span; from October 2012 to December 2019.

117 Pools are groups of 6-7 competitors of varying skill levels that fence a round-robin of 5-touch bouts

118 to determine their seeding for the direct elimination round. Pool bouts do not have video replay, so

119 the referee’s decision is final. I chose this timeframe because prior to 2012, USA Fencing did not

120 consistently record the referee’s division and post-2019 data was unavailable. I selected the Division

121 I category because the outcomes of these events determine Olympic qualification, and this was the

122 category where the referees had been caught colluding. For each bout, the recorded data included the

123 final score, outcome (win/loss), divisions of both fencers, and the referee's division. I also mapped

124 each person’s division to its respective region. Since the outcome depends on the bout’s perspective,

125 the primary fencer for each bout was randomized.

I restricted my focus to non-championship Division I national events with one round of pools to

127 ensure homogeneity of pool bouts across events. Championship events have higher qualification

128 standards, and top fencers only participate in the second round of events with two rounds of pools,

129 potentially altering bout characteristics. I also excluded pools with two referees listed because it was

130 unclear which referee oversaw each bout (they alternate refereeing bouts in a nonsystematic way).

131 Since men's and women's events occur concurrently at the same location with the same referees and

132 had similar bout score distributions, I consolidated bouts from both genders. I assumed referee bias

133 would be consistent across genders. However, I analyzed the three fencing weapons separately due to

134 their distinct rulesets. My final dataset consisted of 14,011 foil bouts, 10,575 epee bouts, and 10,525

135 saber bouts. Of these, 2,344 foil bouts (17%), 1,584 epee bouts (15%), and 2,282 saber bouts (22%)

136 had a referee and fencer from the same region.

The automated system that assigns referees to pools does not consider regional affiliation,

138 except for preventing referees from officiating fencers from their own division. I exploit this quasi-

139 random assignment to isolate and examine potential regional bias in referee decisions. By leveraging

140 the randomness in referee-pool assignments, I ensure that any observed effects are not a result of

141 systematic bias in the assignment process. To measure the effect of a fencer and referee being from

142 the same region, I used linear and logistic regression with heteroskedasticity-robust standard errors.

## 143 My specification is as follows:

144 𝑌�𝑌�𝑖 = 𝛽𝛽0 + 𝛽𝛽1Primary fencer and referee from same region𝑖𝑖 + 𝛽𝛽2Primary fencer region𝑖𝑖 +

145 𝛽𝛽3Event gender𝑖𝑖 + 𝛽𝛽4Primary fencer region𝑖𝑖 ∗ Event gender𝑖𝑖 + 𝜀𝜀𝑖𝑖

146 In the linear regression, my outcome variable is the score differential in bout i, which is measured as 147 the primary fencer’s score minus their opponent’s score. In the logistic regression, my outcome 148 variable is whether the primary fencer won bout i. The categorical covariate for region adjusts for the 149 variation in fencer population and skill between regions. For example, Region 3 foil fencers win 53% 150 of their bouts, whereas Region 6 foil fencers win 37% of their bouts; additionally, Region 3 fencers 151 are overrepresented among bouts where a fencer and referee are from the same region. The 152 interaction term with gender allows for variation in average regional skill between male and female 153 events. Note that fencers and referees who are not from the United States (and do not have a region) 154 are not counted as being from the same region.

155 3 Results 156 Table 1 provides summary statistics for the characteristics of the primary fencers, referees, and event 157 genders of the 35,111 Division I pool bouts from 2012-2019. Regions varied substantially in their 158 populations of both referees and fencers.

159 Table 1: Summary statistics.

Variable # of total bouts # of bouts from a men's event # of bouts where primary fencer from No region (foreign fencer) Region 1 Region 2 Region 3 Region 4 Region 5 Region 6 # of bouts where referee is from No region (foreign referee) Region 1 Region 2 Region 3 Region 4 Region 5 Region 6 # of bouts where both primary fencer and referee are from Region 1 Region 2 Region 3 Region 4 Region 5 Region 6

Foil

Epee Saber

14011 10575 10525

8856 6921 5931

1515 373 1241 5953 3066 646 1217

964 385 1063 3411 2273 1370 1109

849 569 501 4391 2224 346 1645

1032 1518 1752 3840 2247 1332 2290

561 975 1458 2862 1956 999 1764

1542 480 720 4416 1947 384 1036

29 135 1510 465 48 157

859 1743

160 Table 2 presents the linear and logistic regression results examining the effect of regional affiliation

161 on referee decisions across the three fencing weapons. Contrary to initial expectations, the data

162 provided limited evidence of general favoritism by referees toward fencers from their own region. In

163 both models, the effect of the referee and primary fencer being from the same region was slightly

164 negative and nonsignificant for foil and saber. This suggests that having a referee from the same

165 region did not confer an advantage to foil and saber fencers in terms of scoring or the likelihood of

166 winning a bout. In epee, a positive effect was observed, but it was only significant at the p < 0.1

167 level. Although this effect was only marginally significant, this could indicate that epee fencers with 168 referees from the same region have a slight advantage: approximately one point every seven bouts.

169 Table 2: Linear and logistic regressions on the score differential and log odds ratio of victory.

Weapon

Foil β

SE

Epee β

SE

Effect of referee and fencer being from same region on score difference

-0.0368 0.073 0.1387* 0.075

Effect of referee and fencer being from same region on log odds of winning -0.0058 0.047 0.1070* 0.056

Saber β

SE

-0.0034 0.076

-0.0289 0.052

170 The coefficients for the other variables are omitted for succinctness. *p < 0.1, **p < 0.05, ***p < 171 0.01.

172 4 Discussion

173 To my knowledge, this is the first quantitative study investigating referee bias in fencing

174 tournaments. The large sample sizes for each weapon, combined with referees being randomly

175 assigned to bouts, provided optimal conditions for detecting regional bias, if it existed. Despite the

176 significant potential for fencing referees to influence bout outcomes due to their great discretionary

177 power, my comprehensive dataset comprising 35,111 pool bouts over a seven-year period revealed

178 limited evidence to support the hypothesis of regional bias. The linear and logistic regression models

179 indicated a non-significant negative effect in foil and saber, while epee displayed a minimal positive

180 effect that was significant only at the p < 0.1 level. This effect may be spurious considering the

181 multiple testing across all three fencing weapons and should be interpreted with caution.

My results, utilizing score differential as an indicator of bias, differ from the study conducted

183 by Hlasny and Kolaric (2015). Their research demonstrated a small but statistically significant

184 regional bias using the differential in number of yellow cards as a measure. It is possible that there

185 are unique aspects of fencing that make it less prone to regional bias. However, it is also plausible

186 that a bias in assigning penalties exists in fencing but does not impact the final score. While penalties

187 do play a role in foil and saber, referees must split their concentration between making right-of-way

188 calls and watching for penalties. In epee, the referee’s full focus is on potential infractions. Perhaps

189 biased penalty judgments mostly result in yellow cards, which serve as warnings without impacting

190 the outcome. This could potentially explain the weakly significant result in epee and would also

191 suggest a potential compartmentalization in referee behavior: they may exhibit regional bias in

192 awarding penalties while maintaining impartiality in scoring decisions. Penalties often address

193 misconduct or rule violations, suggesting that referees might be more inclined to suspect infractions

194 from unfamiliar individuals while maintaining objectivity in other areas.

While my findings also contrast with Mills’ (2013) scoring related results, which showed that

196 umpires make fewer strike calls against catchers, it is important to note that Mills’ study examines

197 the umpire-catcher dynamic over the course of a single game, whereas referees have repeated, short-

198 term interactions with fencers from the same region. These varying interaction patterns may lead to

199 different relationships between referees and athletes. Nevertheless, the absence of evidence for

200 regional bias in scoring, although specific to fencing, offers broader insights on the numerous studies

201 on nationalistic bias in sports with subjective scoring (Emerson et al., 2009; Krumer et al., 2022;

202 Lyngstad et al., 2020; Zitzewitz, 2006) My findings suggest that nationalistic bias could be more

203 associated with conscious patriotic sentiments rather than unconscious preferences shaped by shared

204 regional identities, affiliations, or styles.

One limitation of my study was the lack of penalty data. Ideally, conducting an analysis of

206 penalties assigned during bouts could offer a nuanced perspective on referee behavior, providing an

207 alternative approach to assess partiality beyond the score, which can only indirectly measure the

208 impact of penalties. This would also allow a better evaluation of referee bias in epee, as most of the

209 subjectivity in this weapon arises from penalties. Moreover, it would enable a direct comparison of

210 my results with those of Hlasny and Kolaric’s (2015). Unfortunately, penalty information is not

211 available on https://usfencingresults.org, limiting my investigation to the score differentials of the

212 bouts. Further studies could address this limitation by using videos of bouts or live observation to

213 determine the number of penalties issued, although this would likely result in a smaller sample size.

214 Another constraint is that I do not know the extent of referee’s interactions with fencers in their

215 region. Future research could benefit from collecting data on the frequency and nature of these

216 interactions, potentially through surveys or by tracking referee assignments at regional events, to

217 better understand how different levels of familiarity might influence decision-making.

While this study finds limited evidence of regional bias in fencing, it cannot definitively rule

219 out the existence of other forms of bias. Firstly, referees may favor fencers from larger, well-known

220 clubs or high-seeded "favorites," as documented in other sports (Bose et al., 2021). Secondly, the

221 historical and current dominance of European fencers, representing over 50% of the combined top-10

222 FIE world ranking across all weapons in 2024 (Fédération Internationale d’Escrime, 2024), raises

223 questions about potential biases. While this success could result from cultural factors or superior

224 coaching, it's important to consider possible implicit biases towards European styles or evolving

225 "right-of-way" rules potentially aligning better with their technique. Thirdly, people of color are

226 underrepresented in fencing. As of 2023, only 19.9% of USA Fencing's membership comprises

227 people of color, compared to the United States Olympic and Paralympic Committee's benchmark of

228 39.9% (USA Fencing, 2023). Since racial bias has been identified in other sports (Magistro & Wack,

229 2023), it may manifest in fencing. Fencing officiating bias remains understudied, and these areas

230 offer valuable avenues for future research.

231 5 Conclusion 232 In conclusion, this study explored the possibility of regional bias in fencing referees by analyzing 233 tournament data across all three weapons: foil, epee, and saber. Utilizing an extensive dataset of 234 35,111 pool bouts over seven years, I found limited evidence of regional bias at USA Fencing 235 national events, with nonsignificant effects in foil and saber and a minimal positive effect in epee. 236 These findings contrast with similar studies in other sports, suggesting that regular interactions

237 between referees and players do not necessarily result in biased officiating in fencing. The minimal 238 positive effect observed in epee suggests the need for further research into how decision-making 239 processes may differ between scoring and penalty calls. Additionally, my findings indicate the 240 importance of investigating how referees’ relationships with players influence their judgments.

241 6 Acknowledgements 242 The author thanks Michael Yetman for his help in drafting this paper.

243 7 References

244 Abdelfatah, A., Hemmat, D., & Ala Allah, M. (2022). Attitudes of Players and Referees Towards

Video Assistant Referee (VAR) at an Aiding Tool in Fencing. International Journal of Sports

Science and Arts, 21(1), 69–88. https://doi.org/10.21608/eijssa.2022.146329.1163

247 Bose, P., Feess, E., & Mueller, H. (2021). Favoritism towards high-status clubs: Evidence from

German soccer. The Journal of Law, Economics, and Organization, 38(2), 422–478. https://doi.org/10.1093/jleo/ewab005

250 Boyko, R. H., Boyko, A. R., & Boyko, M. G. (2007). Referee bias contributes to home advantage in

English premiership football. Journal of Sports Sciences, 25(11), 1185–1194. https://doi.org/10.1080/02640410601038576

253 Cohen, R. (2003). By the sword a history of Gladiators, musketeers, samurai, swashbucklers, and

Olympic Champions; 10th anniversary edition. Modern Library.

255 Czajkowski, Z. (2009). The essence and importance of sense of timing in fencing. Studies in Physical

Culture and Tourism, 16(3), 241-247.

257 Emerson, J. W., Seltzer, M., & Lin, D. (2009). Assessing judging bias: An example from the 2000

Olympic Games. The American Statistician, 63(2), 124–131. https://doi.org/10.1198/tast.2009.0026

260 Faltings, R., Krumer, A., & Lechner, M. (2023). Rot‐jaune‐Verde: On linguistic bias of referees in

Swiss soccer. Kyklos, 76(3), 380–406. https://doi.org/10.1111/kykl.12332

262 Fédération Internationale d’Escrime. (2024, February 25). Athletes & Rankings. International

Fencing Federation - The International Fencing Federation Official Website. https://fie.org/athletes

265 Hlasny, V., & Kolaric, S. (2015). Catch me if you can. Journal of Sports Economics, 18(6), 560–591. https://doi.org/10.1177/1527002515588955

267 Krumer, A., Otto, F., & Pawlowski, T. (2022). Nationalistic bias among international experts:

Evidence from professional ski jumping. The Scandinavian Journal of Economics, 124(1),

278–300. https://doi.org/10.1111/sjoe.12451

270 Longman, J. (2024, May 9). Fencing rattled by suspensions and accusations ahead of Olympics. The

New York Times. https://www.nytimes.com/2024/05/09/world/europe/fencing-olympicsturmoil.html

273 Lyngstad, T. H., Härkönen, J., & Rønneberg, L. T. (2020). Nationalistic bias in sport performance evaluations: An example from the ski jumping World Cup. European Journal for Sport and

Society, 17(3), 250–264. https://doi.org/10.1080/16138171.2020.1792628

276 Magistro, B., & Wack, M. (2023). Racial bias in fans and officials: Evidence from the Italian serie A.

Sociology, 57(6), 1302–1321. https://doi.org/10.1177/00380385221138332

278 Mills, B. M. (2013). Social pressure at the plate: Inequality aversion, status, and mere exposure.

Managerial and Decision Economics, 35(6), 387–403. https://doi.org/10.1002/mde.2630

280 Mo, J. (2022). Allez go: Computer Vision and audio analysis for AI fencing referees. Journal of

Student Research, 11(4). https://doi.org/10.47611/jsrhs.v11i4.3394

282 Sunal, C. E., Willcocks, C. G., & Obara, B. (2021). Real time fencing move classification and detection at touch time during a fencing match. 2020 25th International Conference on Pattern

Recognition (ICPR). https://doi.org/10.1109/icpr48806.2021.9412024

285 Wendell, B. (2024, April 24). USA Fencing Receives Preliminary Findings from Saber Investigation,

Offers Updates on Disciplinary Hearing. USA Fencing. https://www.usafencing.org/news_article/show/1307976

288 USA Fencing. Diversity, Equity, Inclusion and Belonging. USA Fencing. (2023). https://www.usafencing.org/deib

290 Zajonc, R. B. (1968). Attitudinal effects of mere exposure. Journal of Personality and Social

Psychology, 9(2, Pt.2), 1–27. https://doi.org/10.1037/h0025848

292 Zitzewitz, E. (2006). Nationalism in Winter Sports Judging and Its Lessons for Organizational

Decision Making. Journal of Economics & Management Strategy, 15(1), 67–99. https://doi.org/10.1111/j.1530-9134.2006.00092.x
