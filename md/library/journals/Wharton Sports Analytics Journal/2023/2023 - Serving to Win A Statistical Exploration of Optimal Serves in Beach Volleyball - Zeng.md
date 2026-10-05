<!-- source: library/journals/Wharton Sports Analytics Journal/2023/2023 - Serving to Win A Statistical Exploration of Optimal Serves in Beach Volleyball - Zeng.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/serving-to-win-a-statistical-exploration-of-optimal-serves-in-beach-volleyball/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2023 -->
<!-- authors: Zachary Zeng -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 1

Serving to Win: A Statistical Exploration of Optimal Serves in Beach Volleyball

Zachary Zeng

Southridge School, BC, Canada

## Abstract

7 Serving is the only part of a game of volleyball that is the same every time. Despite this,

8 serving strategy and philosophy vary greatly. Teams who use the analytically optimal serve

9 the most can gain a distinct advantage. In identifying the optimal serve, conclusions about

10 best serve type, best serve location, and relationships between errors and effectiveness can 11 be understood. This study analyzed 200,000 serves throughout the FIVB 2022 women's

12 beach volleyball season with metrics such as serve type, serve location, error rate, and 13 which team won the rally through location heatmaps, linear regression, and bar plots. jump-

14 topspin serves were found to be more effective than jump-float serves. However, jump-

15 topspin serves resulted in more errors; the serve effectiveness had no relationship with

16 errors, but there was a strong relationship between serve effectiveness and errors for jump-

17 float serves. These results will guide training and in-game beach and indoor volleyball 18 serving strategies.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 2

## Introduction

Volleyball is played with two people outside on a beach or with six people indoors on

23 hardwood, but serving remains the same. Serving is essential, because how well an

24 opposing offense can return a serve determines how well the setter can set up the hitter. If

25 the pass is high and close to the net, the setter can deliver an easy ball to hit, almost always

26 leading to the receiving team’s point. Still, if the setter can barely keep the ball alive, the

27 hitter may only send over a free ball, giving the serving team the advantage.

Serving happens at the beginning of each rally, and no matter what happens in a

29 game, the conditions for serving are the same. Despite how crucial serving is and how

30 controlled the serving conditions are, making them easier to study and generalize, the

31 volleyball world has little consensus on what serve type is optimal and should be used the

32 most. By identifying the optimal serve in beach volleyball, players can practice hitting this

33 exact type of serve to exact locations on the court, which they know will have the best

34 outcome, giving an advantage over a team that guesses which serve would be the best. In

35 finding the optimal serve in beach volleyball, conclusions about serve types, amount of

36 errors, and serve location can be generalized to beach and indoor volleyball.

This study will focus on serves during the 2022 FIVB women's beach volleyball

38 season using metrics such as serve type, serve location, winner of rally, error frequency,

39 quality of pass, and quality of opposing attack to find the optimal serve. Using the statistics,

40 the relationship between error frequency and effectiveness will be measured in various

41 ways, and the areas of the court served to most effectively will be compared to their own

42 error frequency. Using these various comparisons, the optimal service type and location will

43 be determined.

Foundational Knowledge

There are four types of serves that the dataset records: jump-float, standing float,

47 jump-topspin, and sky ball. Understanding the nature of each serve is important when

48 interpreting the analysis results. A jump-float serve and a standing float serve rely on the

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 3

49 server hitting the ball with a flat hand so that the ball has no spin and moves unpredictably

50 through the air like a knuckleball, making it difficult for the passers to predict where the ball

51 will go. In contrast, a standing float is performed by tossing the ball in front of the server,

52 taking two or three steps, jumping, then hitting the ball with “float.” A standing float is

53 performed by the server tossing the ball slightly in front of the server and delivering the same

54 serve while remaining on the ground. A jump-topspin serve aims to create a topspin on the

55 serve so it drops like a curveball; by doing so, the server can hit the ball harder, therefore

56 serving faster without worrying about the ball flying too far out of the court. The serve is

57 performed by throwing the ball in front of the server and letting the ball roll off the tips of the

58 finger so that the ball spins forward. Then, the server takes two to four steps and will jump

59 and hit the ball while snapping their wrist to create even more topspin. Because the ball

60 drops, the server can hit the ball much harder, so it aims to beat the passers with speed, not

61 lateral movement. Finally, a sky ball is an underhand serve in which the server tries to

62 launch the ball as high as possible while still landing the ball in the receiving team's court. A

63 sky ball serve falls fast, making it difficult to receive, and by serving it so high, passers have

64 a difficult time predicting where the ball will land, especially as the sun gets in their eyes in

65 outdoor beach volleyball.

## Literature Review

Serving is the only part of volleyball where a single person has total control of the

69 outcome and where the choice of technique is not affected by the conditions set by the flow

70 of the game. Therefore, volleyball statistics have long been used to try to uncover the

71 secrets of and optimize the serve. This review will outline the advances in serving data and

72 outline where this paper may offer breakthroughs or fill gaps in knowledge.

Before making any conclusions about volleyball serving as a whole, it is important to

74 acknowledge that this study was conducted only using women's beach volleyball data and

75 there are massive differences in serving between men and women. The most obvious

76 difference between men and women, when serving, are their choices in serve type. As

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 4

77 outlined by a study comparing serving between men and women, men opt to jump-topspin

78 serve 46.9% of the time and jump-float or standing float the other 53.1% of time, while

79 women opt to jump-topspin serve 19.9% of the time and jump-float serve or standing float

80 serve the other 80.1% (Koch & Tilp, 2009). Additionally men more often set the ball

81 overhand with their hands, while women prefer to set underhand with a bump set. Another

82 study, which looks at indoor volleyball serving, found that men prefer to jump-topspin serve

83 while women prefer jump-floats (Kitsiou et al., 2020). The study also found that men and

84 women servers varied in serve location. When playing indoor volleyball, women aimed jump-

85 topspin serves to the middle and jump-float serves to the sidelines, while men tended to aim

86 jump-topspin serves to the sidelines and would serve jump-float serves closer to the net,

87 therefore serving shorter than women.

In terms of the performance of each serve type, although measured differently, a

89 study on serving in Italy’s top indoor’s men’s league had similar conceptual results. It was

90 found that topspin serves, although resulting in more errors and negative outcomes, yield far

91 more positive outcomes than the jump-float serve. Whilst the jump-float serve had far fewer

92 negative outcomes, it rarely resulted in positive outcomes, and overwhelmingly resulted in

93 neutral outcomes (Ciuffarella et al., 2013). In terms of position data, another study found

94 similar results to Ciuffarella et al., with 74% of women’s serves and 75% of men’s serves

95 going to the back third of the court (Dyba, 2013). FInally a study on international men’s

96 beach volleyball supports the idea that the jump-topspin serve is harder to perform. At the

97 beginning of beach volleyball sets, points one through seven, men serve jump-topspin

98 89.7% of the time, but for the final six points of a set, that number drops to 27.3% as players

99 get more fatigued (Jiménez-Olmedo et al., 2012).

In terms of comparing error percentage between different serve types, serve

101 locations, and knockout percentage based on serve type and location, this paper builds

102 upon past studies while offering a new dataset and different metrics. This paper fills in gaps

103 of knowledge and has the potential for breakthrough in its identified correlation between

104 errors and knockout percentage between different serve types. The benefit of being a player

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 5

105 is feeling firsthand that aggression in depending on serve type leads to errors and affects

106 outcome. The data concludes what I as a player believe to be true, which is that as you are

107 aggressive and make more errors when jump-float serving, the knockout percentage will

108 also increase, but when jump-topspin serving, errors and aggression do not correlate with a

109 greater knockout percentage.

## Methodology: Data Collection

The data used in this study was provided by Brian Hurler, a performance analyst for

113 the US National Beach volleyball team. The dataset included nearly every contact with the

114 ball during the FIVB Beach Pro Tour: Elite 16, FIVB Beach Pro Tour Challenge, FIVB Beach

115 Pro Tour Finals, and FIVB World Championships. However, it should again be noted that the

116 data is limited to only women's matches. The dataset is over 2.6 GB; of the over 1.6 million

117 rows of data, over 200,000 were serving data. Within the actual dataset, data about each set

118 included the type of serve, where the serve went (within a six-by-six grid of the receiving side

119 of the court), a brief description of how the opponent was able to return the ball (either

120 negative opponent free attack, ok no first tempo possible, positive no attack, or an ace), and

121 which team won the point.

## Methodology: Variables and Metrics

The data only provides the outcome for each serve. To measure a serve on a serve

125 type or player basis, the variables are primarily converted into three metrics: knockout

126 percentage, break percentage (also known as “side out percentage”), and error percentage.

127 Knockout percentage is meant to measure the number of times the serve forces the other

128 team not to be able to run everything in their offense, also known as “out of system”. Being

129 out of the system entails overpassing, getting aced, or passing an out-of-system pass.

130 Knockout percentage refers to serves that put the other team out of system over the total

131 number of serve attempts (which includes errors). Error percentage is the frequency of

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 6

132 errors, where the serve is out, and a point is given to the other team. Finally, break 133 percentage is the frequency at which the serving team wins the rally on their serve. 134

137 138

## Methodology: Data Processing

For data cleaning, the evaluation of the serve was converted from short phrases to a

141 number 0-3: negative opponent free attack = 3, ok no first tempo possible = 2, positive no

142 attack = 1, or an ace = 0. The location data originally came on a three-by-three grid labeled

143 1-9, with each zone having a letter representing the subzone A-D. To simplify plotting of the

144 locations, the zones were converted to a six-by-six grid, each with an x and y location. From

145 there, the data was binned into each serve type and then further binned to each location on

146 the court.

## Results: Overall Data

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 7

Figure 1: Bar Graph for number of occurrences of type of serve in the dataset

Figure 1 illustrates how often each serve was used in the data frame. The jump-float

153 is the most popular, while sky balls and standing float serves are rare. Due to the limited

154 data on standing floats and sky balls, they will not be analyzed in detail because sky balls

155 are never used consistently and are more of a gag that people do at the end of games.

156 Additionally, jump-floats are superior to standing floats—and thus used more frequently—

157 because when the ball is contacted at a higher point, the path the ball takes is flatter and,

158 therefore, shorter, meaning that it takes less time to reach the passer because it is hit harder

159 and still makes it into the court. jump-topspin serves are still used consistently but not near

160 the amount that jump-float serves are used.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 8

Figure 2: Bar graph for percentage of errors per serve type

As seen in Figure 2, the jump-topspin serve is by far the riskiest serve as it is the

167 hardest to perform and has an error frequency more than double a jump-float serve, the

168 safest serve. To reiterate, an error means the serve hits the ground outside of the receiving

169 team's court, granting the receiving team a point and the serve. The results from skyball and

170 standing float error frequency are inconclusive because of the limited amount of occurrences

171 since no players use them consistently.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 9

Figure 3: A bar graph representing the knockout percentage of each serve type

Yet again, the data for sky balls and standing float serves aren’t conclusive due to

179 the lack of occurrences. Figure 3 demonstrates that the error percent of jump-topspin serves

180 is greater than the jump-float serve. In this case, the error% means that for around 21%

181 jump-topspin serves, there is no chance of adding to the knockout percentage. That means

182 for the serves that go in, there is approximately 0.155 / (1-0.21) = 0.196 chance that the

183 serve knocks the receiving team out of the system. On the other hand, for jump-float serves,

184 there is a 0.13 / (1 - 0.095) = 0.144 chance that the serve knocks the receiving team out of

185 the system. Therefore, although the jump-topspin serve is more risky and will result in more

186 errors when it goes in, it will be far more effective.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 10

188 - y = 0.074567 + 0.700290x - R² = 0.3407 - p-value < 2.2e-16

Figure 4: Linear relationship between knockout percent and error percent for jump-float serve

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 11

193 - y = 0.16952 + 0.06911x - R² = 0.008972 - p-value = 0.243

194 Figure 5: Linear relationship between knockout percent and error percent for topspin serve

In both graphs, each data point represents the knockout percentage and error

197 percentage of a player's season total for each type of serve, if they had served said serve

198 type more than 100 times. For jump-float serves, there is a strong positive linear relationship

199 between the number of errors and knockout percentage, with an R-squared of 0.3401 and a

200 p-value far less than 0.01. Yet, a negative correlation is to be expected, because when you

201 make an error, you have no chance of putting the other team out of system, meaning that by

202 committing more errors, you have fewer chances to put the other team out of system

203 naturally, leading to a lower knockout percentage. Nevertheless, the relationship is positive.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 12

204 This is because, at the highest levels, errors aren’t a reflection of mistakes but a reflection of 205 how aggressive and fast a serve is, especially for float serves. After all, the ball doesn’t 206 curve down like a top spin by serving faster; it makes it much harder to keep the ball from 207 missing far. Therefore, the more aggressive you are with your serve, as signified by error 208 percent, the greater the knockout percentage you will have. On the other hand, there is no 209 clear relationship between errors and knockout percentage for jump-topspin serves, with an 210 R-squared of 0.008972 and a p-value of 0.243. Since there is close to no correlation and 211 relationship between errors and knockout percentage, there is a way to have a high 212 knockout percentage without a high error percentage. jump-topspin serves, therefore, can be 213 much better than jump-float serves because there isn’t a high error percentage associated 214 with a high knockout percentage. Therefore, the success of a jump-topspin serve has more 215 to do with the skill and power of the server rather than the risk of error a server is willing to 216 take. 217

218 219 Figure 6: Knockout percentage for each serve type based on location (row 6 close to net, row 1 far from net)

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 13

223 Figure 7: Relative frequency for each serve type based on location (row 6 close to net, row 1 far from net)

As demonstrated by Figure 6, jump-topspin serves have an all-around higher

227 knockout percentage in almost all zones of the court, compared to jump-float spins. This

228 supports the previous conclusion that even though jump-topspin results in more errors, they

229 are more effective overall. Additionally, both serves seem to achieve the highest KO

230 percentages in row 5. That’s because the only way a ball can land in rows 6 and 5 is if it hits

231 the top of the net and rolls over, which is not something that severs aim for and is neither a

232 serve that the passers are ready for and are essentially either lucky for the server or unlucky

233 for the passer. Looking at the relative frequency of serve location, it is clear that the first half

234 of the court is the hardest to hit because, for a serve to be fast, the ball takes a flatter path

235 rather than a slow, lofty serve. A flat trajectory reduces how much a ball drops, making it

236 more likely to clear the net and reach the opposing court, as demonstrated by Figure 7,

237 which illuminates how very few serves went to rows 4-6 for both serve types. Furthermore,

238 serves only land in the front few rows if they hit the net. This explains why the knockout

239 percentage there is so high: because there are so few serves that go short, the knockout

240 percentage is a bit inaccurate, and the passers aren’t ready. For both jump-topspin and

241 jump-float serves, most serves go to rows 2 and 3 because those are the most natural

242 places for a hard serve that lands to land. Additionally, for both serve types, it is clear that

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 14

243 the highest knockout percentage within the high-frequency rows (rows 2 and 3) occurs in 244 columns 1, 3, 4, and 6, or in other words, from columns 2 and 5. That is simply because the 245 two passers will stand in columns 2 and 5 to cover more court between them. Therefore, by 246 serving columns 3 and 4, the serve goes between the two servers, forcing them to make a 247 split-second decision on who’s going to pass the ball and then forcing them to take steps to 248 move toward the ball, increasing the amount of time it takes to react to the serve. The same 249 logic applies to rows 1 and 6, but rather, the passer has to decide whether the ball is in or 250 out and has to take time to move to the ball. Overall, jump-topspin serves have a higher 251 knockout percentage overall, in the high-frequency rows, between passers, and on the 252 sideline, making it a better overall serve in terms of knockout percentage. 253

Figure 8: Break% map based on serve location

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 15

Figure 9: Break% x relative frequency based on serve location

While knockout percentage is important while evaluating the quality of a serve

261 because it shows how well the receiving team returned the serve, it doesn’t take into account

262 what happens after the receiving team returns the ball and ultimately who wins the point.

263 Break% is simply the percentage that the serving team wins the point. As demonstrated by

264 Figure 7, a vast majority of serves go to rows 2 and 3, so a serve type having a good

265 break% in those rows is so important that when evaluating the break% of a serve, most of

266 the attention should be on the break% in those rows. For both serves in the high-frequency

267 rows (rows 2 and 3), the break% is significantly below 50%. In volleyball, receiving the serve

268 is an advantage because the receiving team can attack first, giving them an advantage.

269 They get to attack more times throughout the rally, and a proper attack will put the other

270 team out of system again, giving the receiving team an advantage. Even in terms of break%,

271 the jump-topspin serve has an advantage over the jump-float serve, although there is a slight

272 caveat. In terms of break%, jump-topspin serves are better in the high-frequency rows when

273 the passer is forced to move the sideline or in between other passers in columns 1, 3, 4, and

274 6 by 3-5%, but jump-float serves are better by 1-2% when the ball goes directly at the

275 passers in columns 2 and 5. A jump-float serve would be better than a jump-topspin serve

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 16

276 when it is served directly at the passer because of its unpredictable, knuckleball-like lateral 277 movement. While a jump-topspin serve drops in a predictable pattern, making it easy to 278 receive straight on, the slight movements of a jump-float serve keep the passers guessing 279 and makes it difficult to receive even if the passer doesn’t have to move much to receive the 280 ball. Knowing that a jump-topspin serve is significantly more effective when aimed away from 281 columns 2 and 5 means that overall the jump-topspin serve is better in terms of break% 282 since the servers will be aiming for the areas away from the passers when serving. 283

284 285 Figure 10: Bubble map showing average relative frequency in size and Topspin break% jump-float break%

Finally Figure 10 is another way of visualizing Figures 8 and 9. The size of the circles

289 represent the average frequency of both serves and the color represents break% for jump

290 top serves at that location subtracted by jump-float break% in the same location, meaning

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 17

291 green favors jump-topspin serves and red favors jump-float serves. Using average relative

292 frequency doesn’t take into account how the two serve types are served to different locations

293 at different frequencies, though what is clear is that in the high-frequency rows of 2 and 3, 9

294 out of 12 spots favor jump-topspin serves again demonstrating how jump-topspin serves are

295 more effective where the servers would be aiming.

## Conclusion

In conclusion, the statistically optimal serve in beach volleyball is a jump-topspin

299 serve away from the passers in columns 1, 3, 4, and 6. Although jump-topspin serves result

300 in more errors, losing points, the jump-topspin serve has a much higher knockout

301 percentage and has a much higher break percentage in the areas that servers should be

302 aiming for. Furthermore, since error% and knockout% are not correlated for jump-topspin

303 serves, unlike for jump-float serves, there is more upside in developing an accurate and

304 powerful topspin serve.

The key takeaway away from this paper that can be used in indoor volleyball is the

306 correlation between errors% and knockout%. Since for jump-float serves knockout% and

307 error% are correlated coaches have to expect more errors out of highly effective jump-float

308 serve yet can challenge jump-topspin serves to limit their errors while mostly maintaining

309 high knockout%. It also demonstrates how jump-topspin serves have more upside because

310 high-level servers can realistically have high knockout% with limited error%.

## Limitations and Future Work

Some confounding variables that would affect this study include: jump-topspin

314 servers are generally considered harder than jump-float serves, meaning potentially better

315 servers would use it; more errors could occur with jump-topspin serves since they are

316 susceptible to weather conditions because they require a toss; and that the data is limited to

317 women’s play.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 18

Future work would include running similar tests but on both men's beach volleyball

319 data and indoor volleyball data. Further work would also include getting speed and lateral

320 movement data of serves and seeing how those variables correlate to knockout%, break%,

321 and error%.

## Acknowledgements

I am grateful to Payton Yang of Sunny Hills High School in California and Finley

325 Workman of Xavier College Preparatory in Arizona for being amazing group members during

326 the presentation of this project at Wharton’s Moneyball Academy. I would also like to thank

327 Zeke for his help with our group's Moneyball Academy presentation. Finally I would like to

328 thank Professor Wyner and Ryan Brill for being amazing teachers at Moneyball Academy.

A STATISTICAL EXPLORATION OF OPTIMAL SERVES 19

## References

330 Ciuffarella, A., Russo, L., Masedu, F., Valenti, M., Izzo, R. E., & De Angelis, M. (2013).

Notational analysis of the volleyball serve. Timisoara Physical Education and

Rehabilitation Journal, 6(11), 29-35. https://doi.org/10.2478/tperj-2013-0013

333 Dyba, R. W. (2013). An analysis of beach volleyball: Techniques and tactics used by junior men and women (Master's thesis, University of Alberta). 25-53. https://doi.org/10.7939/R3ZT4B

336 Jiménez-Olmedo, J. M., Penichet-Tomás, A., Sáiz-Colomina, S., Martínez-Carbonell, J. A., &

Jove-Tossi, M. A. (2012). Serve analysis of professional players in beach volleyball.

Journal of Human Sport & Exercise, 7(3), 709-711.

339 Kitsiou, A., Sotiropoulos, K., Drikos, S., Barzouka, K., & Malousaris, G. (2020). Tendencies of the volleyball serving skill with respect to the serve type across genders. Journal of

Physical Education and Sport, 20(2), 566-569. https://doi.org/10.7752/jpes.2020.02083

342 Koch, C., & Tilp, M. (2009). Beach volleyball techniques and tactics: A comparison of male and female playing characteristics. Kinesiology, 41(1), 54.
