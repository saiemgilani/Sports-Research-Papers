<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Age-Structured Transition Analysis of Competitive Exit in U.S. Fencing Continuation, Temporary Absence, Return, and Terminal Non-Return - Liu.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/age-structured-transition-analysis-of-competitive-exit-in-u-s-fencing-continuation-temporary-absence-return-and-terminal-non-return/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Jeremiah Liu -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

1 Age-Structured Transition Analysis of Competitive Exit in U.S. Fencing: Continuation, 2 Temporary Absence, Return, and Terminal Non-Return

## 3 Jeremiah Liu

4 Lexington High School, Lexington, Massachusetts

6 Keywords: fencing; competitive exit; dropout dynamics; temporary absence; return; adolescent

7 vulnerability; youth sport retention

## 9 Abstract

Youth sport dropout is often described by the last age of participation, but competitive

11 participation changes over time. An athlete may continue from season to season, become inactive

12 for a period, return later, or leave competition completely. This study examined competitive exit

13 in U.S. fencing using an age-structured, observed-state transition analysis. We analyzed 13,206

14 USA Fencing athlete records from 2017 to 2025 and built an athlete-age panel in which each active

15 season was followed by one of three next outcomes: continuation to the next age, absence followed

16 by later return, or terminal non-return within the available follow-up period. We estimated age-

17 specific transition probabilities by weapon and sex, modeled absence onset and terminal non-return

18 across age, quantified return within 2 years after absence onset, described gap duration among

19 returners, and calculated approximate expected remaining active seasons. Continuation was most

20 common at younger ages in all three weapons, but it declined from adolescence onward. Terminal

21 non-return increased from late adolescence into early adulthood. Temporary absences occurred

22 across the age range but were less common than continuation or terminal non-return. Return was

23 more likely when absence began earlier, and most recoverable gaps lasted only 1 year. Expected

24 remaining active seasons decreased with starting age and were generally longest in épée. These

25 results show that competitive exit in fencing is better understood as an age-structured transition

26 process than as a single quitting age.

## 28 Introduction

Organized youth sport is widely recognized as an important context for physical,

30 psychological, and social development, yet sustained participation through adolescence remains

31 difficult to maintain (Battaglia et al., 2024; Butcher et al., 2002; Crane & Temple, 2015; Fraser-

32 Thomas et al., 2008). Across sports, adolescence is repeatedly identified as the period in which

33 participation becomes most vulnerable to withdrawal, as training demands intensify and academic,

34 social, financial, and motivational pressures accumulate (Battaglia et al., 2024; Butcher et al.,

35 2002; Crane & Temple, 2015; Fraser-Thomas et al., 2008). At the same time, recent work has

36 emphasized that dropout is not a single, self-evident event. Its measured rate depends strongly on

37 how withdrawal is defined, what form of participation is being tracked, and whether temporary

38 inactivity is distinguished from permanent exit (Battaglia et al., 2024). These definitional issues

39 are not minor technical details; they shape how dropout is interpreted and how retention strategies

40 are designed.

Fencing provides a particularly informative setting in which to study competitive exit. It is an

42 individual, one-on-one sport organized into three weapons—foil, épée, and saber—that differ in

43 rules, tactical experience, and competitive culture. Long-term progression typically depends on

44 continued club access, coaching, travel, tournament entry, and equipment investment, all of which

45 can amplify dropout pressure during adolescence. Because fencing results are direct and

46 individual, competitive experiences may shape disengagement differently than in many team

47 sports. For some athletes, disengagement may occur as a final one-step exit; for others, it may pass

48 through a period of temporary inactivity before return or before permanent non-return.

Previous research has documented how youth sport dropout typically develops. Studies in

50 organized youth sport consistently identify adolescence as the period of greatest vulnerability,

51 linking withdrawal to intensified specialization, changing self-perceptions of competence,

52 competing obligations, and shifts in motivational climate (Battaglia et al., 2024; Butcher et al.,

53 2002; Crane & Temple, 2015; Fraser-Thomas et al., 2008). Prior research suggests that perceived

54 competence and social context are important for youth sport retention, including in studies of

55 adolescent girls’ withdrawal from physical activity (Slater & Tiggemann, 2010; Weiss &

56 Williams, 2004). More generally, review papers have argued that dropout is not only an individual-

57 level motivational problem but also a structural one, shaped by access, culture, opportunity, and

58 system design (Balish et al., 2014; Battaglia et al., 2024). These findings are highly relevant to

59 fencing, which combines individualized outcomes with substantial logistical and financial

60 demands.

However, most dropout analyses remain descriptive, centered on final participation age or last

62 observed season. Such summaries are useful, but they do not reveal whether competitive exit is

63 driven primarily by a breakdown of year-to-year continuation, a surge of temporary absence, or

64 rising permanent non-return after temporary disengagement. Nor do they show whether age-

65 related vulnerability is driven by direct disappearance from competition or by interruptions that

66 become harder to reverse over time. Those are dynamic questions, and they require a transition-

67 based framework.

The present study applies an observed-state, age-structured analysis to U.S. fencing

69 competition histories. Rather than asking only when athletes are last observed, it asks how the age-

70 structured transition system itself changes across development. Specifically, this paper addresses

71 four questions. First, for an athlete who is competitively active at age 𝑎, what is the probability of

72 continuation, temporary absence with later return, or terminal non-return? Second, how do the age

73 patterns of absence onset and terminal non-return vary across weapon and sex? Third, once

74 absence begins, how likely is return within a fixed time horizon, and how long do recoverable gaps

75 tend to last? Fourth, what do the observed transition dynamics imply for expected remaining active

76 seasons across weapon, sex, and starting age?

These questions are mathematically and practically important. A descriptive age distribution

78 of final participation may indicate where exit is concentrated, but it does not reveal whether the

79 underlying issue is a breakdown of continuation, a surge of temporary absence, or rising terminal

80 non-return after temporary disengagement. By modeling athlete histories as an age-structured

81 observed transition system, the present study aims to provide a more mechanistic account of

82 competitive exit in fencing and to clarify how continuation, temporary absence, return, and

83 terminal non-return change across development.

## 84 Materials and Methods

## 85 Data source and cohort

The study cohort was defined using USA Fencing membership data from the 2020–2021

87 season. A cohort identified before the end of the observation window was needed so that athletes

88 could be followed long enough to distinguish continuation, temporary absence, and terminal non-

89 return in later competition records. Competition histories for cohort members were then linked

90 across the 2017–2025 seasons to reconstruct age-specific participation records. The final dataset

91 included 13,206 athletes distributed across the three weapons—Foil, Épée, and Saber—and the

92 two gender categories used in the dataset. Table 1 summarizes the composition of the unique-

93 athlete cohort, with age defined as 2025−birth year; the transition analyses below are based on 94 athlete-age observations derived from each athlete’s linked competition history in FencingTracker.

95 Table 1. Composition of the unique-athlete cohort by age in 2025, weapon, and sex (n = 13,206).

Age

Foil M

Foil F Épée M Épée F Saber M Saber F Total

1,098

1,180

1,241

1,415

1,391

1,263

Total

3,742

2,262

2,211

1,244

2,375

1,372 13,206

## 97 Weapon affiliation

Athletes may appear across more than one weapon over the course of a multi-year career. To

99 ensure consistent subgroup assignment, each athlete was assigned a primary weapon

100 corresponding to the discipline in which they competed most frequently across the observed

101 record. This allowed all athlete-age observations for that athlete to be analyzed within a single

102 weapon group.

## 103 Athlete-age panel construction

The data were converted into a long athlete–age panel. A non-missing competition record at

105 a given age was used to classify the athlete as competitively active at that age. Each such record

106 created one active athlete-age observation:

(𝑖, 𝑎): athlete 𝑖 active at age 𝑎.

108 This yielded an age-by-season participation history for each athlete. These athlete-age records 109 formed the base panel from which the transition outcomes below were constructed.

## 110 Observed-state transition definition

For each active athlete-age observation, the next competitive path was classified using only

112 empirically observable outcomes. Let 𝑌𝑖,𝑎 denote the observed next-step outcome after athlete 𝑖 is 113 active at age 𝑎. Three categories were defined:

• Continue (𝐶): the athlete was active again at age 𝑎 + 1.

• GapReturn (𝐺): the athlete was inactive at age 𝑎 + 1 but returned to competition at a later age.

• TerminalNonReturn (𝐸): the athlete had no later observed competitive activity within the observable follow-up window.

119 These categories define the observed transition decomposition:

𝑌𝑖,𝑎 ∈ { 𝐶, 𝐸, 𝐺}.

Let 𝐴𝑎 denote the condition that an athlete is competitively active at age 𝑎. For each weapon-

122 sex subgroup, age-specific transition probabilities were estimated as

124 123 with 𝑝𝐶(𝑎) = 𝑃(𝑌 = 𝐶|𝐴𝑎), 𝑝𝐺(𝑎) = 𝑃(𝑌 = 𝐺|𝐴𝑎), 𝑝𝐸(𝑎) = 𝑃(𝑌 = 𝐸|𝐴𝑎), 𝑝𝐶(𝑎) + 𝑝𝐺(𝑎) + 𝑝𝐸(𝑎) = 1.

126 This is an observed-state system, not a fully identified latent-state absorbing Markov chain.

127 Recoverable gaps are directly observed, but latent temporary disengagement that never returns

128 cannot be separated cleanly from direct terminal exit using the current dataset alone.

## 129 Absence onset

Because recoverable gap probability combines both the onset of inactivity and the later

131 possibility of return, absence onset was also modeled directly. Absence onset at age 𝑎 + 1 was

132 defined as

AbsenceOnset𝑖,𝑎 = 1

134 if athlete 𝑖 was active at age 𝑎 and inactive at age 𝑎 + 1. This outcome includes both athletes

135 who later return and athletes who do not. The age-specific absence-onset probability was

136 estimated as 𝑝𝐴(𝑎) = 𝑃(AbsenceOnset = 1|𝐴𝑎).

## 138 Terminal non-return and right-censoring

Terminal non-return was defined conservatively to reduce false labeling of temporary

140 inactivity as permanent exit. Because the observation window ends in 2025, later ages near the

141 right edge of the panel are vulnerable to incomplete follow-up. To address this, terminal non-return

142 was assigned only when sufficient later observation time existed to determine that no later

143 competitive return was present under the selected follow-up rule. If there was not enough future

144 data, those observations were treated as incomplete when analyzing whether athletes had

145 permanently exited the observed competition record.

## 146 Smoothed age patterns and vulnerability-window fitting

Age-specific observed probabilities were first computed directly from the athlete-age

148 transition counts. To aid visual interpretation, smoothed age trends were then fitted. For terminal

149 non-return, an age-localized vulnerability-window model was used:

𝐵(𝑎, 𝑐, 𝑤)

= ex p

(−

(𝑎−𝑐)2 2𝑤2 ),

151 where 𝑐 is the center of vulnerability and 𝑤 is its width. When the parametric fit proved unstable

152 or poorly identified for a subgroup, a nonparametric smoother was used instead, and the curve was

153 interpreted descriptively rather than mechanistically. For absence onset, nonparametric smoothing

154 was used to show the age trend, focusing on visualizing the developmental pattern rather than

155 fitting a strict parametric model.

## 156 Return within 2 years after absence onset

A recoverable absence episode was defined when an athlete was active at age a, inactive at

158 age a + 1, and then returned to competition later. To minimize ambiguity from varying follow-up

159 times, return was analyzed within a fixed time frame: 𝑟2(𝑎) = 𝑃(return within 2 years|absence onset after age 𝑎).

160 Return probabilities were summarized by absence-onset age bins, with 95% confidence intervals.

## 162 Gap-duration distribution among returners

For athletes who returned after a competitive absence, gap duration was defined as the number

164 of consecutive inactive years before reappearance in the record. The empirical distribution of

165 recoverable gap duration was then estimated separately by weapon and sex.

## 166 Approximate expected remaining active seasons

To summarize the expected future length of competitive participation, we estimated the

168 approximate number of active seasons remaining for a fencer who was active at age 𝑎. Let 𝑝𝐶(𝑎) 169 denote the observed probability of direct continuation from age 𝑎 to age 𝑎 + 1, conditional on

170 being active at age 𝑎. Let 𝑝𝐺,𝑑(𝑎) denote the observed probability, again conditional on being

171 active at age 𝑎, of returning after a temporary absence of 𝑑 inactive years. Terminal non-return

172 contributes no future active seasons beyond the current one and therefore enters the recursion only

173 through the remaining probability mass. The approximate expected remaining active seasons,

174 𝐸(𝑎), were then calculated recursively as

𝐸(𝑎) = 1 + 𝑝𝐶(𝑎) 𝐸(𝑎 + 1) + ∑ 𝑝𝐺,𝑑 (𝑎) 𝐸(𝑎 + 𝑑 + 1), 𝑑≥1

175 where the leading 1 represents the current active season. The summation is taken over the gap

176 durations supported in the observed data. This recursion was evaluated backward from older ages

177 to younger ages within each weapon-sex subgroup using the observed continuation and return

178 structure.

## 180 Statistical visualization

All analyses were carried out using MATLAB. Observed probabilities were shown with 95%

182 confidence intervals where applicable. For return probability, age-binned estimates were used to

183 stabilize inference in sparse older-age ranges.

## 184 Results

## 185 Observed transition decomposition from active competition

The observed transition decomposition revealed a clear age-structured competitive pathway

187 in all three weapons (Figure 1). At younger ages, continuation overwhelmingly dominated the

188 next-step dynamics. In every subgroup, the probability of Continue remained high through

189 childhood and early adolescence, indicating that once athletes were competitively active, most

190 remained active at the next age.

That continuation dominance weakened progressively with age. In foil and saber, continuation

192 began to erode in the mid-teen years and declined further into the twenties. Épée showed a more

193 persistent continuation profile, with high continuation extending farther into adolescence before

194 declining more gradually. This weapon contrast is consistent with the broader impression that épée

195 may support a somewhat more durable competitive pathway than foil or saber.

The complementary rise occurred primarily in TerminalNonReturn, not in GapReturn. Across

197 all subgroups, terminal non-return remained low at younger ages, then increased markedly from

198 adolescence onward. The age at which this increase became pronounced varied somewhat by

199 weapon and gender, but the overall pattern was consistent: the main observable change in the

200 transition system was a shift away from continuation toward terminal disappearance from the

201 competitive record. Recoverable gaps occurred across the age range, but they were much less

202 common than either continuation or terminal non-return.

This distinction is important. A final-age distribution alone cannot tell whether athletes are

204 increasingly disappearing through recoverable inactivity or direct terminal non-return. The

205 transition decomposition shows that competitive exit in fencing is dominated by the latter.

206 Temporary absence is present, but it is not the main pathway driving age-related dropout in the

207 observed record.

208 209 Figure 1: Observed transition decomposition from active competition for (Left column) female 210 and (Right column) male fencers in Foil (top row), Saber (middle row), and Épée (bottom row). 211 Blue circles denote the probability of Continue, orange circles denote GapReturn, and yellow 212 circles denote TerminalNonReturn after an active competitive season at each age.

## 213 Absence onset as an age-dependent process

The age-specific probability of absence onset rose steadily from childhood into adolescence

215 and early adulthood in all six subgroups (Figure 2). In younger ages, the observed absence-onset

216 probability was low, indicating that next-year inactivity after an active season was relatively

217 uncommon. As age increased, however, absence onset became substantially more likely.

220 Figure 2: Age-specific probability of absence onset for (Left column) female and (Right column)

221 male fencers in Foil (top row), Saber (middle row), and Épée (bottom row). Open circles show the

222 observed age-specific probabilities, error bars show 95% confidence intervals, and the red curve

223 shows a nonparametric smoothed age trend.

The overall shape was broadly similar across weapon-sex groups, but the levels differed. Foil

226 and saber generally exhibited higher absence-onset probabilities than épée, especially in later

227 adolescence and the early twenties. The smoothed curves showed that the age trend was not purely

228 linear. In several groups, absence onset increased sharply during the later teen years, leveled

229 somewhat in the early twenties, and remained elevated thereafter. The widening uncertainty bars

230 at older ages reflect the smaller number of athletes remaining at risk rather than a breakdown of

231 the overall trend.

232 These results indicate that the erosion of continuous participation begins before terminal non233 return becomes dominant. In other words, athletes initially become more likely to miss a year of 234 competition, and permanent dropout rises only later. This makes absence onset a useful early signal 235 of competitive vulnerability. 236 237 Terminal non-return and age-localized vulnerability

Terminal non-return displayed a strong age structure in every subgroup (Figure 3). At

239 younger ages, the observed probability of terminal non-return after an active season was low. It

240 then rose into a late-adolescent or early-adult window before flattening or declining at the oldest

241 ages with adequate support.

242 243 Figure 3: Age-specific probability of terminal non-return for (Left column) female and (Right

244 column) male fencers in Foil (top row), Saber (middle row), and Épée (bottom row). Open circles

245 show the observed age-specific terminal non-return probabilities, error bars show 95% confidence

246 intervals, and the red curve shows either a fitted vulnerability-window model or a nonparametric

247 smoother when the parametric fit was unstable.

In five of the six subgroups, the age pattern was sufficiently stable to support an interpretable

250 vulnerability-window fit. The estimated centers in these stable subgroups clustered in the late-

251 adolescent to early-adult range, roughly from the low twenties to the high twenties, with moderate

252 widths. Épée males displayed the lowest overall terminal non-return levels and the narrowest fitted

253 window among the stable parametric fits, whereas foil and saber generally showed broader or 254 higher-risk windows. For foil females, the parametric fit was unstable, and a nonparametric 255 smoother was used instead. That instability itself suggests that the age pattern in that subgroup is 256 better described as a broad developmental rise than as a sharply localized parametric window. The 257 terminal non-return curves therefore identify the clearest age-localized vulnerability feature in the 258 dataset. Adolescence does not merely coincide with more athletes being last observed; rather, it 259 marks the developmental period in which active competitors become much more likely to 260 disappear from the record without later return.

## 261 Return within 2 years after absence onset

Temporary disengagement remained a meaningful pathway, even though continuation and

263 terminal non-return were more common overall. Figure 4 shows the probability of returning

264 within 2 years after absence onset by absence-onset age bin. In general, return was more likely

265 when absence began at younger ages and less likely when it began in mid-adolescence or early

266 adulthood.

The pattern varied somewhat by subgroup. Among foil males, return probability declined

268 gradually across age bins. Foil females showed a less regular pattern, but the overall trend was still

269 downward, with greater uncertainty in the oldest supported bins. Both saber males and saber

270 females had lower return probabilities in the mid- to late-adolescent bins than at younger onset

271 ages. Épée had the highest return probabilities overall, especially among males, consistent with its

272 stronger overall participation continuity.

Using age bins helped stabilize the estimates and reduced overinterpretation of sparse older-

274 age data. Even so, the confidence intervals widened at later ages because fewer athletes initiated

275 observable gaps there. Overall, the result is clear: temporary absence was more likely to be

276 reversible when it began earlier.

279 Figure 4: Probability of return within 2 years after absence onset for (Left column) female and 280 (Right column) male fencers in Foil (top row), Saber (middle row), and Épée (bottom row). Open 281 blue circles denote observed bin-level return probabilities by absence-onset age bin, with 95% 282 confidence intervals. 283

## 284 Gap duration among returners

Among athletes who did return after an absence, the overwhelming majority returned after 1-

286 year gaps (Figure 5). Two-year gaps were much less common, and longer recoverable absences

287 were rare in every subgroup. This pattern was strikingly consistent across weapon and sex. Foil

288 and épée showed the highest concentration of 1-year recoverable gaps, while saber exhibited a

289 somewhat broader but still strongly 1-year-dominated gap distribution. The rarity of longer

290 recoverable gaps means that competitive return, when it occurs, usually happens quickly. This

291 supports the choice of a 2-year return horizon in the main return analysis: most recoverable

292 behavior is already captured within that time frame.

294 Figure 5: Distribution of gap duration among returners for (Left column) female and (Right 295 column) male fencers in Foil (top row), Saber (middle row), and Épée (bottom row). Blue bars 296 denote the probability that a recoverable competitive absence lasted 1, 2, 3, or more years before 297 return. 298 299 Approximate expected remaining active seasons

Using the observed age-specific continuation and return structure, we estimated the

301 approximate number of active competitive seasons remaining for a fencer who was active at a

302 given starting age. This quantity includes the current active season plus future active seasons

303 reached either through direct continuation to the next age or through later return after a temporary

304 absence. The approximate expected number of future active competitive seasons declined

305 monotonically with starting age in all six subgroups (Figure 6). This monotonicity is what one

306 would expect in an age-structured competitive system, but the subgroup differences are

307 informative. Épée athletes had the longest expected remaining active seasons at nearly every

308 starting age, followed by saber and then foil. Within each weapon, males generally had slightly

309 higher expected remaining active seasons than females, though the magnitude of the difference

310 varied.

312 Figure 6: Approximate expected remaining active seasons as a function of starting age for (Left

313 column) female and (Right column) male fencers in Foil (top row), Saber (middle row), and Épée

314 (bottom row). Blue circles denote the estimated number of future active competitive seasons

315 derived from the observed continuation and return structure.

The shape of the decline was not perfectly linear. In several groups, especially saber and épée,

318 the curve flattened somewhat in the late teens or early twenties before continuing downward. This

319 reflects the fact that competitive life expectancy is jointly influenced by continuation, absence

320 onset, and return, not by age alone. Nevertheless, the broad interpretation is straightforward: earlier

321 ages provide more remaining competitive opportunity, and that expected horizon is longest in the

322 subgroup structure with the most persistent continuation and lowest terminal non-return.

## 323 Discussion

This study reframed competitive exit in U.S. fencing as an age-structured observed transition

325 system rather than a single quitting age. That change in perspective yielded several important

326 findings.

First, the main structural change with age is the weakening of continuation together with the

328 rise of terminal non-return. In childhood and early adolescence, active fencers in all three weapons

329 usually remained active at the next age. As age increased, that continuity weakened. The transition

330 decomposition showed that this weakening was not mainly absorbed by a large increase in

331 recoverable gaps. Instead, a growing share of athletes disappeared from the competitive record

332 without later return. This distinction matters because a final-age summary alone cannot show

333 whether athletes are mainly pausing or leaving the competitive pathway altogether. The present

334 results indicate that, in the observed record, the larger shift is toward terminal non-return.

Second, absence onset and terminal non-return followed related but distinct age patterns.

336 Absence onset began rising earlier, from adolescence into early adulthood, indicating that the

337 erosion of year-to-year continuity starts before permanent non-return reaches its highest levels. In

338 this sense, absence onset acts as an earlier sign of competitive vulnerability, whereas terminal non-

339 return is the later and more definitive expression of that vulnerability. The terminal non-return

340 curves further suggest that risk is concentrated in a broad late-adolescent to early-adult window

341 rather than at a single sharply defined quitting age.

Third, temporary absence remained meaningful even though it was not the dominant pathway.

343 Recoverable absences were observed across the age range, and return within 2 years was more

344 likely when absence began earlier. At the same time, most recoverable gaps lasted only 1 year,

345 with 2-year gaps already much less common and longer recoverable gaps rare. This pattern

346 suggests that reversible disengagement in fencing is usually short. When athletes do return, they

347 tend to do so quickly. From a retention standpoint, that implies that early re-engagement efforts

348 may have value, but that the practical window for successful return is limited.

Fourth, weapon differences were consistent across the analyses. Épée showed lower absence

350 onset, lower terminal non-return, higher return probabilities, and longer expected remaining active

351 seasons than foil or saber. These differences do not by themselves identify a causal mechanism,

352 but they do suggest that competitive exit is not uniform across fencing weapons. Possible

353 explanations include differences in competitive format, athlete selection, club structure, travel

354 patterns, or developmental culture. Whatever the cause, the results indicate that fencing should not

355 be treated as a single retention environment.

The approximate expected remaining active seasons help connect the age-specific transitions

357 to a more intuitive summary of competitive persistence. These curves declined with starting age

358 in every subgroup, as expected, but the subgroup contrasts were informative. Épée athletes

359 generally had the longest remaining competitive horizon, followed by saber and then foil. The

360 curves also showed that future competitive persistence depends on more than age alone: it is

361 shaped jointly by continuation, absence onset, and the possibility of return after temporary

362 absence.

These findings have several practical implications. Retention work in fencing should focus

364 not only on who eventually leaves, but also on who is beginning to lose year-to-year continuity.

365 The results suggest that adolescence and early adulthood are the key ages at which the competitive

366 pathway becomes less stable. Support during this stage may need to emphasize continuity of

367 participation, rapid response to emerging absences, and low-barrier routes back into competition

368 after short interruptions. Because most recoverable gaps are short, re-entry efforts are likely to be

369 most effective when they occur quickly rather than after long inactivity.

Several limitations should be noted. The analysis is restricted to sanctioned competition

371 histories and therefore does not capture recreational fencing, noncompetitive club participation, or

372 informal involvement in the sport. Terminal non-return from the record is not identical to complete

373 withdrawal from fencing. In addition, the observed-state framework does not fully identify latent

374 inactive states, so the expected remaining active seasons are approximate rather than exact

375 absorbing-chain quantities. Finally, inference becomes less stable at older ages because fewer

376 athletes remain under observation there.

Even with these limitations, the observed-state framework adds something important that

378 descriptive final-age summaries cannot provide. It shows how competitive exit is generated:

379 through declining continuation, rising absence onset, increasing terminal non-return, and only

380 limited recovery once continuity is lost. For retention research in fencing, that age-structured

381 dynamic perspective is likely to be more informative than final participation age alone.

## 382 Conclusion

Competitive exit in U.S. fencing is better understood as an age-structured transition process

384 than as a single quitting age. Using 13,206 athlete records, this study showed that continuation

385 dominates at younger ages but weakens from adolescence onward, while terminal non-return rises

386 into late adolescence and early adulthood. Absence onset also increases with age, providing an

387 earlier sign of competitive vulnerability, but most recoverable gaps are short and return is more

388 likely when absence begins earlier. Across nearly all analyses, épée showed the most persistent

389 competitive pathway. These results move fencing dropout research beyond descriptive final-age

390 patterns toward a more mechanistic view of competitive retention. By distinguishing continuation,

391 temporary absence, return, and terminal non-return, the study clarifies how athletes move away

392 from the competitive pathway and when those changes become most pronounced. This framework 393 provides a stronger basis for understanding competitive exit in fencing and for designing age394 targeted strategies to support longer-term participation. 395

## 396 Acknowledgments

The author gratefully acknowledges the availability of USA Fencing competition-history

398 records accessed through FencingTracker, which made this analysis possible.

## 400 References

401 Balish, S. M., McLaren, C., Rainham, D., & Blanchard, C. (2014). Correlates of youth sport attrition: A review and future directions. Psychology of Sport & Exercise, 15(4), 429-439. https://doi.org/10.1016/j.psychsport.2014.04.003

404 Battaglia, A., Kerr, G., & Tamminen, K. (2024). The Dropout From Youth Sport Crisis: Not as

Simple as It Appears. Kinesiology Review, 13(3), 345-356. https://doi.org/10.1123/kr.2023-0024

407 Butcher, J., Lindner, K. J., & Johns, D. P. (2002). Withdrawal from competitive youth sport: a retrospective ten-year study. Journal of Sport Behavior, 25, 145+. https://link.gale.com/apps/doc/A86049189/AONE?u=mlin_n_umass&amp;sid=ebsco&a mp;xid=cbd7e3f3

411 Crane, J., & Temple, V. (2015). A systematic review of dropout from organized sport among children and youth. European Physical Education Review, 21(1), 114-131. https://doi.org/10.1177/1356336x14555294

414 Fraser-Thomas, J., Côté, J., & Deakin, J. (2008). Understanding dropout and prolonged engagement in adolescent competitive sport. Psychology of Sport & Exercise, 9(5), 645-

662. https://doi.org/10.1016/j.psychsport.2007.08.003

417 Slater, A., & Tiggemann, M. (2010). “Uncool to do sport”: A focus group study of adolescent girls’ reasons for withdrawing from physical activity. Psychology of Sport & Exercise,

11(6), 619-626. https://doi.org/10.1016/j.psychsport.2010.07.006

420 Weiss, M. R., & Williams, L. (2004). The Why of Youth Sport Involvement: A Developmental

Perspective on Motivational Processes. In Developmental sport and exercise psychology:

A lifespan perspective. (pp. 223-268). Fitness Information Technology. https://research.ebsco.com/linkprocessor/plink?id=c01fbbff-f100-3efa-91da-

0996e6f6b7f1
