<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - A Comparative Analysis of Rating Systems in the US Junior Tennis Development Pathway - Abramson.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/a-comparative-analysis-of-rating-systems-in-the-us-junior-tennis-development-pathway/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Koray S. Abramson -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

A Comparative Analysis of Rating Systems in the US Junior Tennis Development Pathway

Koray S. Abramson

Science Research Program

Pine Crest School

## Abstract

23 The United States Tennis Association (USTA) has historically used point-per-round rankings to 24 determine competitive tournament entry and seeding, but this system often rewards participation 25 over quality of play and can be distorted by random draw effects. Alternative systems such as 26 Universal Tennis Rating (UTR) and World Tennis Number (WTN) use algorithmic predictive 27 modeling based on prior head-to-head results to estimate player ability across gender, age, and 28 geography. Although previous studies (Im, 2023; Kiely, 2025; Krall, 2025; Mayew, 2023) have 29 evaluated predictive accuracy between these two systems using smaller, elite-level samples, 30 large-scale analyses spanning all competitive levels of U.S. junior tennis remain limited. This 31 study addresses that gap through a comprehensive, multi-level analysis of 70,822 USTA junior 32 matches (scraped from January–July 2024), evaluating UTR, WTN, and USTA rankings for both 33 accuracy and bias. Overall, UTR predicted 78.5%, WTN 74.2%, and USTA 70.1% of matches 34 correctly, respectively, with statistically significant differences. Geographic bias was evident 35 across systems, favoring players from less-competitive sections. In matches between similarly 36 rated opponents, players from stronger sections won 61.7% (USTA), 59.0% (WTN), and 53.9% 37 (UTR), indicating systematic underestimation of those cohorts. By combining a large-scale 38 comparative analysis with the first known bias assessment of these systems, this study extends 39 prior evaluations and contextualizes newer findings. The results demonstrate that UTR is the 40 most accurate and least-biased predictor of match outcomes, supporting the adoption of 41 algorithmic, data-driven rating frameworks such as UTR over traditional point-per-round ranking 42 systems in junior tennis. 43 44

45 1. Introduction

Tennis is a sport increasingly analyzed by various systems assessing player performance.

47 While player advancement within tournaments is determined by wins against competing players,

48 the competitiveness of an individual match can be analyzed, allowing for the skill-level of a

49 player to be estimated with greater accuracy. Knowing player skill-level is useful for a wide

50 range of applications: players looking for other players to train with; college coaches assessing a

51 player they might be recruiting; or tournament directors accepting and seeding players in

52 tournaments. This study analyzes various rating and ranking systems utilized by players and

53 coaches in the USTA junior development pathway.

54 1.1 History of Ranking Systems in Tennis

Since tennis’ inception, player strength has been primarily assessed by some variation of

56 a ranking system. The USTA, the ATP (Association of Tennis Professionals), the WTA

57 (Women’s Tennis Association), and the ITF (International Tennis Federation) (ITF, 2023;

58 USTA, 2020; USTA, 2022; Wilson, 2023) utilize rankings to determine which players gain entry

59 into tournaments, as well as the seeding of players within a draw, based on the idea that the

60 stronger the level of the player, the better the player’s ranking is. Most rankings use a point-per-

61 round (PPR) system. The PPR system first attributes points to a tournament; a tournament with

62 more points attributed to it generally attracts more competitive players than one with less points.

63 For example, in the USTA, the winner of an L1 (i.e., highest-level tournament) receives 3000

64 points compared to an L5 winner who receives 300 points. Points are awarded based on how far

65 (i.e., how many “rounds”) a player advances in a tournament and are aggregated on a rolling 12-

66 month basis, with a player’s ranking based off only the best 6 tournaments of the year for each of

67 singles and doubles (USTA, 2020; USTA, 2022).

There are some significant limitations and flaws to ranking systems. One limitation is the

69 influence of random factors, commonly called the “luck of the draw”, which relate to the random

70 nature of a tournament’s draw. For example, one player may play the top seed in the first round,

71 while another similarly-leveled player in the same tournament may randomly obtain a much

72 easier path to the later rounds, consequently allowing the “luckier” player to gain more ranking

73 points. Another example could be an injury of an opponent leading to forfeiture that then gives

74 points to a player who did not even compete. Additionally, since USTA rankings are based on a

75 player’s best six matches (USTA, 2022), it can reward quantity of play more than quality (e.g., a

76 player competing in eight tournaments a year will have a harder time achieving six great results

77 based on the “luck of the draw” than a player who plays 24 tournaments a year).

78 1.2 Introduction of Rating Systems to Tennis

More recently, different organizations have started comparing the levels and status of

80 players through new models attempting to create a more accurate system than traditional

81 rankings. Most of these algorithms are variations of the Elo system utilized in chess, such that in

82 head-to-head matches, it is a zero-sum system where the gain in the rating of one player must be

83 offset equally by the loss in the rating of the opponent (Chess.com; Vernon, 2024).

84 1.2.1 Universal Tennis Rating

In 2008, Universal Tennis Rating (“UTR”) was introduced. UTR is a “universal” rating

86 system, which means it attempts to put all players on a single rating scale from 1.00 to 16.50

87 across all demographics, including gender, geography, and age (UTR Sports, 2023). UTR’s

88 algorithm relies on the percentage of games won relative to the rating of an opposing player and 89 is based on a weighted average of a player’s last 30 matches, with more recent matches receiving 90 more weight. Unlike rankings, it assesses the competitiveness of a match to determine a “rating” 91 relative to another rated opponent (UTR Sports, 2023). For example, if a player loses 0-6, 0-6 to 92 a 10-UTR competitor, UTR assumes the losing player is significantly below a 10-UTR. In 93 contrast, if the losing player loses 6-0, 6-7, 6-7, UTR will assign a rating for that match greater 94 than the 10-UTR winner, indicating the losing player is stronger; while the losing player lost 2 95 out of 3 sets, he or she won 56% of the games (18 out of 34). UTR does not care about who wins 96 a match and only looks at percentage-of-games-won relative to the rating of the competitor (UTR 97 Sports, 2023).

98 1.2.2 World Tennis Number

During the COVID-19 shutdown, UTR gained traction as there were fewer tournaments

100 occurring and naturally rankings became less meaningful. Some tournaments started using UTR

101 for seeding and entry. UTR’s parent company also started running its own UTR Tournaments,

102 thus competing with the USTA.

In 2021, World Tennis Number (WTN) was created as an alternative to UTR by the

104 International Tennis Federation (ITF) (ITF, 2024b), which is affiliated with the USTA. WTN,

105 like UTR, applies a rating by assessing the competitiveness of a match and is also meant to be

106 universal. WTN’s algorithm differs from UTR’s in that it is based only on the percent of sets

107 won; consequently, ratings improve more by winning in straight sets rather than splitting sets in a

108 match (ITF, 2024a). WTN operates on a 40-point scale, with lower numbers denoting higher

109 skill levels, which is the opposite of UTR’s convention (USTA, 2023).

110 1.2.3 Comparison of UTR and WTN

UTR and WTN are correlated (r2>0.9) for both gender divisions (Figure 1). As skill level

112 increases variability decreases, suggesting greater alignment of the systems for advanced players.

113 114 115

Boys - Regression of WTN vs. UTR

0.00

Girls - Regression of WTN vs. UTR

0.00

5.00

5.00

10.00

10.00

15.00

15.00

WTN WTN

20.00

20.00

25.00

25.00

30.00 35.00 y = -0.1536x2 + 0.4107x + 30.936 R! = 0.9085

30.00 35.00 y = -0.1942x2 + 0.2536x + 31.589 R! = 0.9019

40.00

0.00

2.00

4.00

6.00

8.00

10.00

12.00

14.00

UTR

40.00

0.00

2.00

4.00

6.00

8.00

10.00

12.00

14.00

UTR

Figure 1: Scatterplots showing a gender-separated dataset of WTN (inverted scale) vs. UTR for 17,278 unique players. The correlation between the two rating scales is calculated with a quadratic line of best fit, with r2 values larger than 0.9.

116 1.3 Existing research investigating rating systems in tennis

Previous research on the comparative accuracies of UTR, WTN, and USTA rankings

118 addressed each system’s ability to predict match outcomes, although with limited datasets and

119 only at elite level of play (Im, 2023; Kiely, 2025; Krall, 2025; Mayew, 2023).

The first such study analyzed comparative accuracy between UTR and WTN and found

121 these systems to be statistically comparable (Mayew, 2023). The study analyzed 1,532 matches

122 from the USTA National Championships (i.e., elite-level players), spanning two age divisions

123 (16s and 18s). Consequently, the results were limited in that they did not address system

124 performance for younger and developing players in the developmental pathway, thus excluding

125 the majority of junior players. The authors of this study then performed a follow-up investigation

126 (Krall, 2025) using a dataset twice as large, but still limited to the championship level, to assess

127 the effect of a 2023 WTN algorithm change; this study also concluded that neither system had a

128 statistical advantage. Another recent study (Im, 2023) compared UTR, WTN, and USTA

129 rankings and validated previous conclusions indicating that WTN and UTR have similar

130 predictive accuracy; however, across its sample size of approximately 800 matches, it also

131 demonstrated the superior predictive performance of both UTR and WTN relative to USTA

132 rankings.

Most recently, a more comprehensive analysis (Kiely, 2025) from the authors of the

134 initial study compared the predictive accuracy between WTN and UTR within international

135 competition by analyzing 585 matches from the ITA All-American Championships (N.B.

136 international players are a significant portion of collegiate tennis players) and 3,142 matches

137 from various international championship level tournaments for the 12s and 14s division (e.g.,

138 Junior Orange Bowl, Les Petits As Mondial). While their initial studies showed comparable

139 performance for UTR and WTN when applied to US-only players within championship-level

140 play, once international competition was a significant part of the dataset, UTR statistically

141 outperformed WTN; the authors surmised that this was potentially due to other countries not

142 being as fully onboarded to WTN as with UTR.

143 1.4 Purpose of Study

This study seeks to improve upon previous efforts to assess the predictive accuracy of

145 UTR, WTN, and USTA rankings for match outcomes, as described in section 1.3 above.

146 Specifically, the analysis investigates results from 70,822 junior USTA matches scraped from the

147 USTA official website from January through July 2024, combined with rating metrics for 17,278

148 unique players recorded weekly over this period. The large size of the dataset used in this study

149 permits an evaluation of each system’s ability to predict match results across skill level, gender,

150 and other sub-categories at a statistically significant level. This is also the first study to analyze 151 rating-system universality by quantifying geographic bias across USTA regional sections, 152 identifying whether rating systems systematically under- or over-estimate player ability. Through 153 this combination of large-scale, multi-level data and bias evaluation, this study provides a 154 comprehensive assessment of rating-system performance and practical implications for equitable 155 seeding, tournament placement, and advancement within the US junior tennis pathway.

156 2. Methodology

To evaluate the predictive accuracies of three tennis rating/ranking systems relative to

158 each other across various player levels and gender, and to determine if any internal geographic

159 bias exists in what are supposed to be universal ratings, a large dataset of match results with

160 corresponding player attributes (e.g., gender, ranking/ratings, level, geography) was required.

161 2.1 Data Collection

UTR, WTN, and USTA Rankings were scraped weekly from the USTA-affiliated

163 matchtennisapp.com website (Match Tennis App; Octoparse). Because player ratings/rankings

164 continually adjust for all players to include the most recent results, data was captured each

165 Thursday in advance of weekend matches; consequently, the dataset contains weekly historical

166 player ratings that are not readily available to the public.

Data was collected for every player competing in Boys’ and Girls’ Divisions for L1

168 through L5 tournaments in the 12s, 14, 16s, and 18s from January through July 2024. If a match

169 did not contain complete pre-match fields for both players (i.e., current rating, ranking, name,

170 division, section, gender, match date, and tournament level), it was excluded from the dataset. In

171 total, 83,403 unique player profiles were captured across 17,278 unique players (i.e., individual

172 players that competed in multiple tournaments through the 7-month recording period) with 173 ratings and rankings captured at the time of each match. Match results were then collected from 174 the official USTA website. In total, 70,822 matches had complete player profiles for both 175 competitors, after removing matches between players with an identical rating for UTR or WTN.

176 2.2 Calculation of Predictive Accuracy for Each Rating / Ranking System

In any given match, UTR, WTN, and USTA rankings all predict a winner based on which

178 player has a higher-level rating or ranking. The predicted result of each system was then

179 evaluated compared to actual match results. Understanding predictive accuracy across multiple

180 skill levels was of interest as previous studies were limited to only the highest skill levels and

181 age groupings. This study allows for a cross-sectional analysis across all skill levels from

182 intermediate to elite juniors.

To analyze predictive ability across different skill levels, matches were grouped into ten

184 evenly spaced decile cohorts based on the average UTR rating of the competitors, independently

185 determined for Boys’ and Girls’ Divisions. The dataset was further filtered to look at matches

186 between closer-leveled competitors, which was defined as matches between players with a small

187 differential in UTR (between 0.05-0.25) or WTN (0.13-0.65) rating, yielding 19,772 matches to

188 analyze with significant sample sizes within each skill-level cohort (Table 1). This filter attempts

189 to remove the matches that are easy to predict and artificially boost the accuracy of each rating

190 system, as a significant portion of the full dataset contains matches, often in early rounds of

191 tournaments, between players of very different abilities.

193 194 195 196 197 198

!"#$%FG()*++F,(-.(/0*11(23%34#(5634(7811(!"#$%FG7(("+,(6*1#F4F,(934(!"#$%FG(7)F#:FF+(213GF1.(;"#F,(<1".F4G7= !"#$%&#'()*+&,(-#*'&.%(,&/01&,(*%2(34)(50//&.&1+0*#(6768967:8($.(;4<(50//&.&1+0*#(67=>967?8@

!"#$%FG >?@>A

!"#$%FG @>?B>A

!"#$%FG B>?C>A

!"#$%FG C>?M>A

!"#$%FG M>?E>A

!"#$%FG E>?F>A

!"#$%FG F>?G>A

!"#$%FG G>?H>A

!"#$%FG H>?I>A

!"#$%FG I>?@>>A

811 !"#$%FG

)3.G(JK;(;"+LF M*41G(JK;(;"+LF

811(!"#$%FG )#:+N(213GF1.(;"#F,

!"!!#$"%& !"!!#%"(!

+-!+% (-&,&

$"%&#'"(! %"(!#$"!!

+-!$, (-&)(

'"(!#'")$ $"!!#$"*!

+-&!! (-&+)

'")$#*"') $"*!#'"&(

+-!$* (-&$,

*"')#+"(& '"&(#'"*(

+-!)+ &-)*(

+"(&#+",% '"*(#*"&(

+-&!$ &-,!)

+",%#,"$% *"&(#*"*$

+-!,( &-,&!

,"$%#)"!% *"*$#+"((

+-!,% &-+''

)"!%#)",% )",%#&*"!! +"((#+"), +"),#&*"!!

+-!,$ &-+&%

+-&!' (-!(%

+!-,(( &)-++(

Table 1: 70,822 matches were segmented into decile cohorts (>7,000 matches per cohort) based on the average UTR of the two competitors. Higher cohorts represent more advanced junior players (e.g., in the top decile, while this dataset is for USTA juniors under the age of 18, this UTR range would be typical for an NCAA Division 1 college player). The dataset was also filtered to matches between closely rated players, defined as having a small differential between how the competitors were rated by UTR (>=0.05, <=0.25) or WTN (>=0.13, <=0.65).

199 2.3 Determination of Geographic Bias

To analyze potential geographic bias within rating/ranking systems, which has not been

201 previously studied, matches between similarly-leveled players from “more competitive” regional

202 sections and “less competitive” sections were analyzed; if a system is geographically universal, a

203 similarly-rated player from a less competitive section should have an equal chance of beating a

204 player from a more competitive section. Section competitiveness was determined by analyzing

205 USTA sectional quote data for the 17 geographic sections (USTA, 2024) and was based on a

206 60%/40% weighting of: (i) sections having the largest player number ranked in the top 150

207 nationally and (ii) the percentage of section registrants in the top 150 nationally. The most

208 competitive sections (Florida, Southern California, Southern, Northern California, and Eastern)

209 are some of the larger sections, and contain almost 50% of all players nationally (Figure 2).

210 211 212 213 214

Figure 2: Map of the 17 USTA Sections (i.e., geographic groupings) separated by section competitiveness, determined by analyzing the USTA quota data for entry into the national championship level tournaments. “Most Competitive Sections” are orange on the map and represent 45% of total players nationally. The darker the shading of each color reflects the relative strength of a section with the “Most” and “Less” categories.

Matches from the top 5 skill-level deciles were considered, as this is the most relevant

216 intersectional play; there were 8,096 matches between players from a competitive section and a

217 less competitive section. A subset of “toss-up” matches was analyzed, defined as a differential of

218 0.25 in UTR, 0.65 for WTN, or 50 spots in ranking. The predictive rating/ranking average was

219 computed for these matches, with a differential of near-zero for all systems (Table 2). The

220 difference of results from the null “50-50” parity hypothesis is interpreted as geographical bias.

!"#$%&$'#()"*+,#'-$&*.$#I$$"*0$,%1234(5,6$"#*76,8$%&*9%):*+)%$*,";*<$&&*=):L$#(#(5$*?$'#()"& !"#$%&'()*++&'&,-*$#./(012345678(91:345;78(2$,<*,=374>

@AB

CA0

77B

A)#,6*+,#'-$&

76,8$%*I5GJ* B,#("GHB,"F("G

+)&#*=):L$#(#5$*?$'#()"&*M+=?N <$&&*=):L$#(#5$*?$'#()"&*M<=?N

B,"F("G*H*B,#("G*I;5,"#,G$*#)*+=?

!"#$$ '()! '()! %(%%

!"#%# *!()+ *!()+ %(%%

!"#&$ *), *)) -*

Table 2: Table represents matches between similarly rated/ranked players from one of the more competitive sections (“MCS”) competing against a player from a less competitive section (“LCS”). The near equivalence for UTR and WTN (i.e., no differences to the reported precision of 0.00 rating) suggests a player from either section type should have an equal chance of winning. The ranking differential of -2 spots minimally favors the LCS players.

222 2.4 Statistical Assumptions and Modeling

Throughout this study, conservative binomial assumptions and uncertainties were used to

224 estimate p-values and statistical significance. Given the large size of the dataset, in most of the

225 subcategories, the p-values for the accuracy difference between the rating systems were

226 negligible, and the statistical significance was consequently extremely high. In subsets

227 segmented by skill level, in addition to p-values computed using conservative binomial statistics,

228 McNemar’s test was used to quantitatively assess each system’s performance given the same set

229 of match outcomes, as it focuses on only discordant prediction pairs (i.e., where only one rating

230 system predicts the correct outcome).

231 3. Results & Analysis

232 3.1 Predictive Accuracy of Each Rating/Ranking System

Across all 70,822 matches, UTR’s predictive accuracy is highest at 78.5%. WTN and

234 USTA rankings also obtain high accuracy levels of 74.2% and 70.1% respectively (Figure 3).

235 The relative differences in accuracy are at high levels of statistical significance, with p-values of

236 effectively zero, demonstrating a clear difference in the performance quality between the three

237 systems (Table 3). While each system exhibits greater predictive performance for Girls’

238 Divisions vs. Boys’, this differential is small and not statistically significant (Figure 3).

UTR performs the best across all skill-level deciles, with outperformance greatest at the

240 lower and middle skill-level deciles. At the higher skill-level deciles, UTR’s superior

241 performance relative to WTN diminishes, and for the top two deciles UTR’s predictive accuracy

242 is only 0.4% above WTN’s. However, at higher skill levels, USTA Ranking becomes far less

243 predictive relative to both UTR and WTN (Figure 3).

Overall, these results display considerable and comprehensive evidence for different

245 predictive performance across the three rating systems. UTR consistently outperforms WTN

246 (although marginally at the highest skill-levels), while both systems outperform USTA rankings.

!"#$%&%G()*+!"&&*,G+-&*.(,G("I+0+"1+2%G(I3+456G*#6+7,&"66+%88+9%G,:*6+;<%&=+L(I*6?+%I.+@*I.*&+;L(3:G+L(I*6?

IG0

IF0

CM2+;HISG0+%)3S?

!"&&*,G+-&*.(,G("I+0

HG0

HF0

APQ4

NG0

@R2L4

TMU+;HNSL0+%)3S? --2+;HFSO0+%)3S?

247 248 249 250 251 252

NF0 9%G,:*6+FJOF0 9%G,:*6+OFJLF0 9%G,:*6+LFJMF0 9%G,:*6+MFJNF0 9%G,:*6+NFJGF0 9%G,:*6+GFJNF0 9%G,:*6+NFJHF0 9%G,:*6+HFJIF0 9%G,:*6+IFJOF0 9%G,:*6+OFJOFF0

A"56B+CM2+2%I3*+++ @(&86B+CM2+2%I3*+++

I+;9%G,:*6?+++

!"!!#$"%& !"!!#%"(!

+-!+%

$"%&#'"(! %"(!#$"!!

+-!$,

'"(!#'")$ $"!!#$"*!

+-&!!

'")$#*"') $"*!#'"&(

+-!$*

*"')#+"(& '"&(#'"*(

+-!)+

+"(&#+",% '"*(#*"&(

+-&!$

+",%#,"$% *"&(#*"*$

+-!,(

,"$%#)"!% *"*$#+"((

+-!,%

)"!%#)",% +"((#+"),

+-!,$

)",%#&*"!! +"),#&*"!!

+-&!'

<*,(8*+!":"&G6+"1+7)*&%3*+9%G,:+CM2+7,&"66+788+9%G,:*6+;:(3:*&+6=(88+8*)*86+G"+G:*+&(3:G?

Figure 3: Comparative predictive accuracy for match outcomes of UTR, WTN and USTA Rankings. UTR (78.5% accurate) in aggregate outperformed WTN (74.2%) and USTA (70.1%). At lower skill levels UTR has the greatest differential in performance. While it outperforms WTN at the highest skill-level cohorts, the separation is minimal (Table 3). USTA Ranking becomes even less predictive at higher skill levels. The lighter-shaded lines represent predictive accuracy by gender at each skill-level cohort.

Using McNemar’s test, which analyzes the disagreement subset (i.e., isolating outcomes

254 where one algorithm is correct while the other is not), UTR is statistically more accurate when

255 considering all matches, with a p-value near zero. At high levels of statistical significance, UTR

256 outperformed WTN in all skill-level cohorts except in the top two deciles (Table 3). When UTR

257 and WTN disagreed in their prediction of the winner, UTR was correct 62.6% of the matches vs.

258 37.4% for WTN, with the greatest differential in the lower and intermediate skill-levels (Figure

259 4). UTR also statistically outperforms USTA Rankings in all cohorts with p-values near zero.

260 Finally, WTN statistically outperforms USTA Rankings when considering all matches, and in all

261 cohorts except for the lower-skilled players comprising cohort 2 (Table 3).

262 263 264 265 266

267 268 269

!"#$%&G(")*"+*,-./*0-1*%)2*.%)3*4&52G67G85*45&+"&#%)65*96&"((*9::*;%76<5(*%)2*=L*?3G::@A585:*"+*!"#$57G7"&(

Shaded p-values are statistically significant

;%76<5( B@CBM

;%76<5( CB@NBM

;%76<5( NB@FBM

;%76<5( FB@GBM

;%76<5( GB@HBM

;%76<5( HB@IBM

;%76<5( IB@JBM

;%76<5( JB@KBM

;%76<5( KB@LBM

;%76<5( LB@CBBM

9:: ;%76<5(

M"L(*,-.*.%)N5 OG&:(*,-.*.%)N5 -"7%:*;%76<5(

!"!!#$"%& !"!!#%"(!

+-!+%

$"%&#'"(! %"(!#$"!!

+-!$,

'"(!#'")$ $"!!#$"*!

+-&!!

'")$#*"') $"*!#'"&(

+-!$*

*"')#+"(& '"&(#'"*(

+-!)+

+"(&#+",% '"*(#*"&(

+-&!$

+",%#,"$% *"&(#*"*$

+-!,(

,"$%#)"!% *"*$#+"((

+-!,%

)"!%#)",% +"((#+"),

+-!,$

)",%#&*"!! +"),#&*"!!

+-&!'

+!-,((

,-.*!"&&567 0-1*!"&&567 .%)3*!"&&567

+)"(. *,",. +!"%.

,!"%. +&"+. +("'.

+)"!. +("'. +!"+.

+)"%. +%"'. +&"!.

+)"*. +'"&. +("!.

+)"). +*"'. +&"%.

+,"+. ++"(. *)"(.

+,"'. +*",. *)"*.

+*",. +*"+. *)"!.

+%"+. +%"&. *'"'.

+,"'. +$"(. +!"&.

,-. P@75(7*$@Q%:R5 8(T 0-1 ;615#%&S(*$@8%:R5

,-. P@75(7*$@Q%:R5 8(T .%)3 ;615#%&S(*$@8%:R5

0-1 8(T

P@75(7*$@Q%:R5

.%)3 ;615#%&S(*$@8%:R5

!"!!! !"!!!

!"!!! !"!!!

!"!$) !"!%*

!"!!! !"!!!

!"!!! !"!!!

!"()% !"($,

!"!!! !"!!!

!"!!! !"!!!

!"!&* !"!!*

!"!!! !"!!!

!"!!! !"!!!

!"!!& !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!%) !"!!&

!"!!! !"!!!

!"!!! !"!!!

!"!&$ !"!!!

!"!!! !"!!!

!"!!! !"!!!

!",&& !"*+$

!"!!! !"!!!

!"!!! !"!!!

!"$!% !"&(+

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

Table 3: UTR statistically outperformed WTN across all 70,822 matches with a p-value near zero. It also statistically outperformed WTN in all skill-level cohorts except for the two highest-level deciles. Both UTR and WTN statistically outperform USTA Rankings with p-values near zero.

!"#$%&%G()*+,&*-(.G("/+0+"1+234+%/-+536+78*/+4%G(/9+:;<G*#<+%&*+(/+=(<%9&**#*/G+7(G8+4*<$*.G+G"+L(?*@;+A%G.8+BCG."#*

,&*-(.G("/+0+58*/+234+%/-+536+=(<%9&**

OF0

MPUO0 NF0

MOUI0

MOUM0

MJUN0

MIUL0

MHUO0

234 536 234

MF0

LLUO0

LNUL0

VMIUM0+%)9UP

LF0

LFUP0 OPUH0

LIUO0 ONUI0

OOUM0

OIUL0

OF0

JLUO0

JMUJ0

JNUL0

JOUI0

JFUI0

JHUO0

JF0

## 536 VJNUO0+%)9UP

IF0

HF0

F0 A%G.8*<+FGHF0 A%G.8*<+HFGIF0 A%G.8*<+IFGJF0 A%G.8*<+JFGOF0 A%G.8*<+OFGLF0 A%G.8*<+LFGMF0 A%G.8*<+MFGNF0 A%G.8*<+NFGOF0 A%G.8*<+OFGPF0 A%G.8*<+PFGHFF0

,*&.*/G(@*+!"8"&G+N;+234+4%G(/9+"1+A%G.8*<+++

A%G.8*<+78*&*+&%G(/9<+<;<G*#<+-(<%9&**+++ 3"G%@+#%G.8*<+(/+."8"&G+++

0+"1+#%G.8*<+78*&*+234+Q+536+-(<%9&**+++

R";<S+234+4%/9*+++ T(&@<S+234+4%/9*+++

A%G.8*< FGHF0

!"#$% &")&+ (%,(-

),)).',+! ),)).+,()

A%G.8*< HFGIF0

!"%&# &")'# (+,#-

',+!.$,() +,().',))

!"8"&G<+N;+,*&.*/G(@*+"1+M)*&%9*+A%G.8+234+V@"7*<G+G"+8(98*<GP

A%G.8*< IFGJF0

!"$%& &"!)) ((,!-

$,().$,*' ',)).',%)

A%G.8*< JFGOF0

!"'%' &")'% (),#-

$,*'.%,$* ',%).$,!(

A%G.8*< OFGLF0

!"(#$ &")*& !#,!-

%,$*.&,(! $,!(.$,%(

A%G.8*< LFGMF0

!"))& &"!)' !',(-

&,(!.&,#+ $,%(.%,!(

A%G.8*< MFGNF0

*') &")#( !+,+-

&,#+.#,'+ %,!(.%,%'

A%G.8*< NFGOF0

#!' &")#+ !!,$-

#,'+.*,)+ %,%'.&,((

A%G.8*< OFGPF0

%#% &")#' *,&-

*,)+.*,#+ &,((.&,*#

A%G.8*< PFGHFF0

&*' &"!)$ !!,(-

*,#+.!%,)) &,*#.!%,))

M@@ A%G.8*<

!(")*! &)"#(( !&,!-

Figure 4: When UTR and WTN disagree in predicted outcomes, UTR is the more predictive system across all skill levels. As skill level increases, so does the relative performance of WTN, although it lags UTR in all cohorts.

While each rating/ranking systems had high levels of predictive accuracy (i.e., all above

271 70%), this is not surprising given tournament construct placing stronger players in different parts

272 of the bracket such that they play head-to-head in later rounds; as a result, in early rounds where

273 a significant number of matches occur, competitors are often at different levels. Across the entire

274 dataset, 50% of matches had UTR differentials of greater than 0.71 (on a 16.50 rating scale) and 275 WTN differentials of 1.58 (on a 40-point rating scale) (Table 4); these differentials imply a 276 meaningful difference in the skill level of opponents, and the higher the differential in rating 277 between players, the easier it is to predict the outcome (Mayew, 2023). For example, for matches 278 with a separation greater than a 0.71 in UTR in competitor rating (which is the median 279 differential across all matches), UTR was correct in predicting the winner 91.4% of the time; 280 WTN was correct 86.8% of the time for matches with a separation greater than 1.58 (Table 4).

281 282 283 284 285

!"#$"%&'(")*+,*-.&'%/*0',,"#"%&'.(*,+#*12-*.%3*425*6+78"&'&+#)

!"#$"%&'("

9:;

<:;

=:;

>:;

?:;

@:;

A:;

B:;

C:;

*******12-*0',,"#"%&'.( *******425*0',,"#"%&'.(

!"#$

!"%&

!"'!

!"((

:DA9

!")!

#"#'

#"'(

#")&

!"%)

!"(&

!"*)

#"%%

9D?B

#"))

%"(#

$"#&

'"%%

+,-./012345361.7448094:.;.)#"'< =,>./012345361.7448094:.;.*?"*<

Table 4: Matches were placed in deciles based on competitor rating differential; the smaller the differential, the more competitive a match should be. Over 50% of total matches are between players with differentials greater than 0.71 for UTR and 1.58 for WTN, suggesting that a large percentage of matches should be easy to predict since there are significant disparities in opponent skill levels.

To directly analyze matches between competitors of similar skill levels to exclude easily-

287 predicted contests, matches where competitors were within 0.25 in UTR differential or 0.65 in

288 WTN were analyzed. When considering these closely-rated matches, UTR again statistically

289 outperformed WTN, and did so at all skill levels with the exception of decile nine (Table 5). This

290 finding corroborates the statistical significance determined in 3.1.1 when looking at the dataset in

291 its entirety, with UTR outperforming WTN, and contrasts with conclusions of some previous

292 studies (Im, 2023; Krall, 2025; Mayew, 2023) while corroborating the conclusion of the most

293 recent paper published (Kiely, 2025). The superior performance of UTR is most pronounced

294 between lower- and middle-level competitors but is still apparent using McNemar’s test among

295 the highest-skilled players.

296 297 298 299

!"#$%FG(")*"+*,-.*%)/*0-1*23F+"F#%)43*5G673F3/*+"F*89$3473/*!6"(3*:%74;3(*<=*>?G66*!";"F7 !"#$%&#'()*+(,-.("%$$#/#&0%)1(232452364(7/(8-9("%$$#/#&0%)1(23:;523<4=

Shaded p-values are statistically significant

:%74;3( ABCAM

:%74;3( CABNAM

:%74;3( NABFAM

:%74;3( FABGAM

:%74;3( GABHAM

:%74;3( HABIAM

:%74;3( IABJAM

:%74;3( JABKAM

:%74;3( KABLAM

:%74;3( LABCAAM

@66 :%74;3(

M"=(*,-.*.%)N3 OGF6(*,-.*.%)N3 -"7%6*:%74;3(

!"!!#$"%& !"!!#%"(!

(-&,&

$"%&#'"(! %"(!#$"!!

(-&)(

'"(!#'")$ $"!!#$"*!

(-&+)

'")$#*"') $"*!#'"&(

(-&$,

*"')#+"(& '"&(#'"*(

&-)*(

+"(&#+",% '"*(#*"&(

&-,!)

+",%#,"$% *"&(#*"*$

&-,&!

,"$%#)"!% *"*$#+"((

&-+''

)"!%#)",% +"((#+"),

&-+&%

)",%#&*"!! +"),#&*"!!

(-!(%

&)-++(

,-.*!"FF347 0-1*!"FF347

**"'. ''"(.

*,"(. '*"(.

*'",. ''"!.

*'"&. ''"*.

*$"!. '$"+.

*("&. ''",.

*&"(. '+"'.

*&"%. '*"%.

')"!. ',"+.

'+",. ''"%.

*%"%. '*"!.

,-. PB73(7*$BQ%6R3 T(U 0-1 :413#%FS(*$BT%6R3

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!!! !"!!!

!"!(% !"!!)

!"!!% !"!!!

!",*( !",*!

!"&&% !"!$'

!"!!! !"!!!

Table 5: Analysis of matches between closely rated players (as defined above) demonstrates high levels of UTR outperformance in predictive accuracy with statistical significance overall and within all skill-level cohorts with the exception of the 9th cohort.

300 3.2 Geographical bias

In analyzing the potential for geographical bias, the study filtered the dataset to matches

302 that were considered, at least on paper, to be close to a “toss-up” (competitor differential of UTR

303 <= 0.25, WTN <= 0.65, Ranking <= 50) and between players from a more competitive section

304 and a less competitive section. There were 1,633 toss-up matches measured by UTR, 1606 by

305 WTN, and 1643 by USTA rankings (Table 2). Under the no-bias hypothesis that can be utilized

306 due to the near-zero average differential across every model’s subset, the even expectation for a

307 match winner is 50%, assuming the systems are universal (Table 2, Figure 5).

When analyzing match results, however, the “competitive section” player won 53.9% for

309 UTR, 59.0% for WTN, and 61.7% for USTA Ranking (Figure 5). Under the null hypothesis of

310 50-50 parity between sections, the p-value for the UTR-even matches in this subset is 0.0009,

311 and the p-values for WTN and USTA Rankings were effectively zero. Thus, a significant level of

312 bias was observed for all three systems; UTR exhibited the least bias, and USTA rankings were

313 the most biased. (Note: USTA Rankings are not intended to be universal by sectional geography,

314 which is why USTA uses a quota system for entry into some national tournaments.)

316 317 318 319 320 321

!"#$%&G&()*(+,)-.#I0G1#$(2G#&(G"(34"G5,.&#$3(6#7G"-(8%&7,9&

!"#$%&%'(%)*+,#-$%.(I*%0-1%2$,*13)*+,#-$%45,+6*7%'(%85,#$9%)(7,*:%#$%45,+6*7%-0%)#:#;51;(%85,*<%=;5(*17>

AIO

GIO =H:@O

=@:IO

G>:AO

=IO

JG:>O

JIO

J>:IO

H<:HO

PXI,17,L( 6,&N$7()*(=IO( !&&N9G"-(Q)( 8,17G)"(2G#&

PG"(O(U%(8,17G)"(B%I,

N)&7(V)9I,7G7G5,(8,17G)"& 6,9#G"G"-(8,17G)"&

HIO

?IO

>IO

IO

!5-:(6#7G"-()*(;$#%,.((( B)7#$(C"7,.M8,17G)"(N#710,&(((

O",MB#G$,L(B,&7F(MM&1).,((( IM5#$N,(((

4B6

<:=>

<:=>

>FGHH H:>?

I:III@

PBQ

?>:=@

?>:=@

>FGIG A:?J

I:IIII

;;6(R6#"ST

?=A

?==

>FGJH @:J?

I:IIII

Figure 5: The chart depicts the correct prediction percentage for “toss-up” matches (i.e., near equivalent rating/ranking) between the more competitive sections and less competitive sections (defined per Methodology section) for each system. The difference between the 50-50 expected results and actual percentage of matches won for the more competitive sections demonstrates statistical geographical bias within each of the models, with a p-value of 0.0009 for UTR and effectively zero for WTN and USTA rankings.

322 4. Discussion

This study improved upon and reached different conclusions than previous studies

324 investigating predictive accuracy of tennis rating/ranking systems, particularly when applied to

325 the US junior development pathway. Overall, both UTR and WTN outperformed USTA

326 rankings, validating conclusions in the ITF Coaching & Sport Science Review (Im, 2023) study

327 that showed that head-to-head rating models are superior in predictive accuracy. When

328 comparing UTR and WTN, this study demonstrates that UTR outperforms WTN significantly

329 when looking at the entire junior developmental pathway, which includes younger and not-yet-

330 elite-level players. Even at the most elite level of play in the study (i.e., skill-level cohort 10),

331 UTR statistically outperformed WTN when removing the dilution from easier-to-predict matches

332 between competitors with larger rating differentials.

The results of this study diverge from prior research analyzing US-based player datasets

334 (Im, 2023; Krall, 2025; Mayew, 2023), which collectively concluded that UTR and WTN do not

335 exhibit statistically significant differences in predictive accuracy. The most recent investigation

336 (Kiely, 2025), which studied international competition at both the collegiate and 12s and 14s age

337 divisions, concluded that UTR statistically was more predictive than WTN, and surmised that

338 this finding was potentially due to the lack of homogeneity in international competition where

339 WTN is less prevalent, contradicting their previous study on an only US-based player dataset,.

This study, with a dataset encompassing 70,822 matches between US-based players

341 across all competitive levels, demonstrates that even when removing the international element,

342 UTR is still the superior system. By expanding the framework to decompose predictive

343 performance by skill tier, match parity, and geographic region, the study determined that WTN’s

344 relative accuracy declines progressively with lower player levels and that UTR sustains stronger

345 predictive consistency across divisions. Even within the highest-skill cohort, once easily

346 predicted matches are excluded, UTR demonstrates statistically significant superiority,

347 underscoring the model’s robustness under more stringent predictive conditions.

UTR’s superior accuracy could be due to multiple factors. For example, UTR uses more

349 granular inputs as it is based on games within sets, while WTN only considers the winner of sets

350 without considering internal game scores. UTR also has a richer dataset since it aggregates more

351 match sources than WTN (e.g., UTR-only tournaments, high school matches, etc.).

352 4.1 Limitations

While demonstrating geographic bias for UTR and WTN, this study could not evaluate

354 other elements of universality – specifically as it relates to age and gender. There was no ability

355 to capture the age of a player as the division they are playing in is not representative of their birth

356 year. For gender, while there is no real recorded competition between genders that could result in

357 a meaningful dataset, analysis would suggest that one or both of UTR and WTN is not actually 358 universal across gender. If both systems were universal, the regression of WTN against UTR 359 would produce similar results for both Boys’ and Girls’ Divisions. As illustrated in Figure 6, this 360 is not the case, indicating that at least one of the rating systems is not universal across gender.

361 362 363 364 365

*+, *+, *+,

!"!! #"!! $!"!! $#"!! %!"!! %#"!! &!"!! &#"!! G!"!!

!"!!

/01234 .56752280930:3*+,3;2"3-+.

!"#"$%&G()*+, -"%&.G%/+"-")%&0)* 12"#"%&0%3(

%"!!

G"!!

("!!

)"!!

$!"!!

$%"!!

$G"!!

-+.

!"!! #"!! $!"!! $#"!! %!"!! %#"!! &!"!! &#"!! G!"!!

!"!!

<87=234 .56752280930:3*+,3;2"3-+.

!"#"$%&G0.,+, -"%&,()*+"-")G&(30 12"#"%&0%G0

%"!!

G"!!

("!!

)"!!

$!"!!

$%"!!

$G"!!

-+.

>0?@A7AB8;53*+,3;"3-+.3.5675228093C13<59D57

!"!!

#"!!

$!"!!

$#"!!

%!"!!

%#"!! &!"!!

4$567

8$567

&#"!!

!"!!

%"!!

G"!!

("!!

)"!!

$!"!!

$%"!!

$G"!!

-+.

Figure 6: Figure 1 is demonstrated here with the addition of a separate graph displaying just the regression lines for boys and girls UTR vs WTN values. The regression line difference demonstrates that either one or both of the two ratings cannot be truly universal, as the correlation between values of UTR and WTN starkly differentiates between genders as skill level increases.

Additionally, the dataset used in this study predates the September 2024 WTN algorithm

367 update. The ITF stated that their expectation for the outcomes of this revision is that it would

368 have the most significant benefit at the more junior levels (ITF, 2024; Kiely, 2025); this would

369 be of significant importance as WTN underperformance is most pronounced at lower skill levels.

370 Future research incorporating post-update junior data could further validate this interpretation.

371 5. Conclusions

UTR, in both predictive accuracy and geographical bias, had the best performance of the

373 rating systems studied, at high levels of statistical significance. WTN is also statistically more

374 predictive than USTA Rankings. UTR’s outperformance diminishes as skill levels of competitors

375 increase, but when directly selecting matches with closely-rated players (i.e., removing the

376 diluting effect of easily-predicted matches), UTR outperforms WTN across all matches, and does

377 so statistically in nine out of the ten skill-level cohorts.

This study also demonstrates that UTR and WTN are not truly universal when

379 considering geography (i.e., USTA regional sections) as bias was observed. If the systems

380 applied a single scale across all players as they were designed, near equal-rated players from one

381 section would win nearly 50% of the time when competing with a player from another section.

382 This was not the case, and these win-rates deviate significantly (p-values near zero) from the

383 50% parity that is expected when assuming no geographical bias. However, UTR’s bias is lower

384 than both WTN’s and USTA’s, again implying that UTR is the better measurement of skill level.

In summary, while all models analyzed exhibit limitations in their evaluation of player skill

386 level, UTR consistently outperforms both WTN and USTA rankings in both predictive accuracy

387 and in the degree of regional bias over almost all subsets of the dataset, including across skill level

388 and gender. Future studies across additional dimensions and algorithmic design could shed more

389 light on the underlying differences between the predictive performance of these systems.

390 5.1 Application in Sport

This analysis is applicable to all aspiring tennis players and coaches in the USTA junior

392 development pathway, as it includes data from intermediate-through-advanced skill-level

393 tournaments. While USTA rankings, and at times WTN, are used by the USTA for tournament

394 entry and seeding, these are the two least-predictive systems for assessing skill level compared to

395 UTR; this is especially pronounced for players earlier in their development (i.e., at lower skill

396 level). One recommendation would be for the USTA to preferentially utilize UTR (or even

397 WTN) in granting entry to tournaments, as it is most predictive at assessing player skill level.

Youth tennis has a very significant burnout rate (Gould, 1993) in large part due to the

399 required frequency of play and travel necessary to build a ranking. A majority of players from

400 top college teams previously attended “alternative education” systems (e.g., online schools,

401 tennis academy schools, etc.), as national and ITF tournaments do not align with regular school

402 schedules, with tournaments extending beyond the weekend. Furthermore, players participating

403 in ITF tournaments travel weeks at a time, which adds significant expense to the process.

If USTA and/or ITF utilized UTR (or a similar rating system) for tournament acceptance,

405 burnout rates should decrease. The most-skilled players could then play local tournaments in

406 older divisions against higher-rated players to build their rating with successful outcomes,

407 allowing players to avoid the necessity of travel and excessive tournament play that is currently

408 required to gain ranking points for entry to national-level and ITF tournaments.

409 6. Acknowledgements

410 I would like to thank Jed Biesiada, PhD, for his invaluable help through his continued 411 mentorship throughout this project. I very much appreciate his education on the research process, 412 commitment to detail, and his guidance on how to overcome the obstacles that were encountered. 413 I also want to thank my Pine Crest Science Research teachers, Dr. Ganden and Mrs. Gordinier, 414 for both building my foundation of knowledge for creating this project, and their much415 appreciated suggestions they provided throughout the research process.

416 7. References

417 1. Chess.com. ELO rating system. https://www.chess.com/terms/elo-rating-chess

418 2. Gould, D., Tuffey, S., Udry, S., & Loehr, J. (1993). Burnout in competitive junior tennis players. https://doi.org/10.1123/tsp.10.4.322

420 3. Im, S., & Lee, C.-H. (2023). World Tennis Number: The new gold standard, or a failure? ITF

Coaching & Sport Science Review, 31(91), 6-12. https://doi.org/10.52383/itfcoaching.v32i91.371

423 4. International Tennis Federation (ITF). (2023). ITF World Tennis Ranking points tables. https://www.itftennis.com/media/9074/itf-points-tables-2023.pdf

425 5. ITF. Frequently asked questions: What is the ITF World Tennis Number? https://worldtennisnumber.com/eng/faq

427 6. ITF. (2024a). Enhancement to the ITF World Tennis Number calculation. https://worldtennisnumber.com/eng/news/enhancement-to-the-itf-world-tennis-numbercalculation

430 7. ITF. (2024b). Taking centre court: The rise of the World Tennis Number. https://www.itftennis.com/en/news-and-media/articles/taking-centre-court-the-rise-of-theworld-tennis-number

433 8. Kiely, L. A., Mayew, R. L., & Mayew, W. J. (2025, April 10). An updated assessment of the predictive accuracy of World Tennis Number and Universal Tennis Ratings. Unpublished manuscript.

436 9. Krall, N., Maroulis, N., Mayew, R., & Mayew, W. (2025). Initial evidence on the impact of the 2023 World Tennis Number algorithm change for predicting match outcomes. ITF

Coaching & Sport Science Review, 32(94), 52–58.

439 10. Match Tennis App. Match! Tennis. https://web.matchtennisapp.com

440 11. Mayew, R. L., & Mayew, W. J. (2023). Which global tennis rating better measures player skill? Evidence from the 2022 USTA Junior National Championships. The Sport Journal,

26(2).

443 12. Octoparse. Easy web scraping for anyone. https://www.octoparse.com

444 13. USTA. (2024). Quota for 2024 USTA National Championships. https://www.usta.com/content/dam/usta/2024-pdfs/2024-quota-final.pdf

446 14. USTA. (2023). Manual and automatic seeding. https://customercare.usta.com/hc/enus/articles/360053180492-Manual-and-Automatic-Seeding

448 15. USTA. (2020). USTA Junior Tournaments Ranking System. https://www.usta.com/content/dam/usta/pdfs/junior-tournaments-ranking-system.pdf

450 16. USTA. (2022). USTA National Junior Rankings Overview. https://docs.google.com/document/d/1QhbtKvMAM5ZQvcwKm6cwiF7l8sZpIqL/edit#heading=h.30j0zll

453 17. UTR Sports. (2023). How UTR rating works. https://www.utrsports.net/blogs/news/how-utrworks

455 18. Vernon, J. (2024). Understanding the algorithm – complete summary. UTR Sports. https://support.universaltennis.com/support/solutions/articles/9000151830-understandingthe-algorithm-complete-summary

458 19. Wilson. (2023). Tennis rankings explained. https://www.wilson.com/en-us/blog/tennis/howtos/tennis-rankings-explained
