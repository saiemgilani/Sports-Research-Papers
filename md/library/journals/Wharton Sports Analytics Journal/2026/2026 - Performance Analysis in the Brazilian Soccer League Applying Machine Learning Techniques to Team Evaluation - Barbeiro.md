<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Performance Analysis in the Brazilian Soccer League Applying Machine Learning Techniques to Team Evaluation - Barbeiro.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/performance-analysis-in-the-brazilian-soccer-league-applying-machine-learning-techniques-to-team-evaluation/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: José Vinicius Boaventura Barbeiro -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

## 1 Performance Analysis in the Brazilian Soccer

## 2 League: Applying Machine Learning Techniques to

Team Evaluation

José Vinicius Boaventura Barbeiro1, Bruno Samways dos Santos2

1 Universidade Tecnológica Federal do Paraná (UTFPR), Londrina, Brazil

2 Advisor. Universidade Tecnológica Federal do Paraná (UTFPR), Londrina, Brazil

March 11, 2026

## Abstract

This study presents a method for analyzing the sports performance of teams through artificial intelligence, using data from the Série A of the Brazilian Championship. Machine learning methods were applied, highlighting K-Means clustering for identifying patterns among teams, Random Forest for pointing out the most relevant variables, and SHapley

Additive exPlanations (SHAP) analysis to interpret the importance of these variables in each profile. The clustering revealed six distinct groups of teams, ranging from aged and less competitive squads to young, offensive, and disciplined teams. Variables such as the number of goals, average age of the starters, betting market odds, and number of fouls stood out as determinants for performance. The results demonstrate how the application of artificial intelligence enhances game interpretation, offering deeper insights and more solid bases for strategic decisions, contributing to understanding the factors influencing team performance, and strengthening sports analysis based on objective data and advanced methods.

Keywords: Machine Learning; Clustering; Explainable Artificial Intelligence; Soccer

1 22 Introduction

23 Artificial Intelligence (AI) has been revolutionizing the world’s most popular sport: Soccer.

24 As a global industry that generates billions of dollars annually (Fimmanò, 2024), soccer is

25 increasingly reliant on advanced technologies to optimize performance, engage fans, and achieve

26 results. In this context, AI enables large-scale, precise, and personalized analyses, transforming

27 how clubs, athletes, and governing bodies manage, play, and commercialize the sport. Through

28 machine learning, it becomes possible to predict match outcomes with greater accuracy, analyze

29 tactics in real time, and assess both individual and team performance. As a sporting and

30 economic phenomenon, soccer is entering a new era driven by the power of data and artificial

31 intelligence (Andreff, 2021).

Due to its democratic and universal nature, soccer goes beyond being merely a sport. In

33 recent years, however, the game has also solidified its status as a major industry, where success

34 on the field is increasingly tied to investments in infrastructure, technology, and performance

35 analysis. The modernization of club management, especially with the adoption of the Sociedade

36 Anônima do Futebol (SAF) model, or Soccer Joint-Stock Companies, has contributed to greater

37 professionalization, enabling teams to incorporate advanced tools for data analytics and tactical

38 scouting.

This evolution has enabled a more scientific approach to the game, incorporating statisti-

40 cal techniques and machine learning to identify patterns in team performance. The relationship

41 between financial resources and sporting success had already been evident for some years.

42 However, with the growing availability of data and the development of more sophisticated

43 analytical methods, it has now become possible to extract tactical insights with an unprecedented

44 level of precision (Okazaki et al., 2012). This progress allows for a deeper understanding of

45 game strategies and how investments can be optimized to improve on-field results (Rein and

46 Memmert, 2016).

In this context of the increasing transformation of sports information into digital data,

48 quantitative performance analysis has emerged as a fundamental strategic tool, reshaping how

49 teams are evaluated and developed tactically. The use of AI in sports databases enables the

50 identification of tactical and behavioral patterns with a high degree of accuracy (Pisaniello, 2024).

51 Through machine learning algorithms, it is possible to analyze large volumes of performance

52 data, such as positional metrics, offensive transitions, and defensive effectiveness. These

53 tools provide quantitative support for the evaluation of strategies, optimizing decision-making

54 processes, and allowing for evidence-based tactical adjustments. This approach represents a

55 significant advancement in sports analysis, integrating technological and scientific methods into

56 team preparation (Pisaniello, 2024).

Considering this context, the present study aimed to analyze how machine learning

58 techniques, particularly clustering methods combined with classifiers (Random Forest) and

59 feature importance analysis with SHapley Additive exPlanations (SHAP), can characterize team

60 performance in the Brazilian Championship. The research specifically focuses on identifying

61 collective performance patterns and conducting comparative analyses between teams using

62 competition performance data. This approach not only enhances the understanding of the league

63 but also provides a foundation for more effective strategies in analysis and decision-making.

64 In addition to this introductory section, the remainder of the article is organized into four

65 main sections: Section 2 discusses previous studies that apply machine learning in soccer;

66 Section 3 describes the data, methods, and tools used; Section 4 presents the results of the

67 clustering, Random Forest, and SHAP analysis, including charts, descriptive analyses, and

68 practical implications; finally, Section 5 outlines the conclusions and contributions of the study.

69 The references are provided at the end of the article.

2 70 Correlated Works

71 The use of machine learning in sports analysis has been explored by many authors in the past 72 years with many applications and different areas. These studies are focused on predicting match 73 results, finding playing styles, game strategies, or identifying features that can help teams better 74 understand how they can prepare for opponents. Soccer, being one of the most popular sports in 75 the world, has certainly gained space in this arena. Analyzing some studies related specifically 76 to soccer we can find many of them that use clusterization algorithms to find how matches, 77 players or teams are related to each other.

Diquigiovanni and Scarpa (2018) developed an innovative hierarchical clustering method

79 that enables the characterization of playing styles within Italian Serie A teams. This method

80 identified the relationship between playing styles and performance during the 2015–2016 season,

81 focusing on the effect of playing styles on the number of goals scored. They were able to prove

82 the key role of one of them in the match results. Using a different technique, Fernandez-Navarro

83 et al. (2016) also identified patterns and playing styles in teams playing the Spanish La Liga

84 and the English Premier League. Their work utilizes Principal Component Analysis (PCA) and

85 distributes the teams into clusters based on this factor analysis, allowing them to create a playing

86 style profile to help teams better prepare for opponents in competition.

Bilek and Ulas (2019) investigated how situational variables and performance indicators

88 such as fouls, passes, offsides, yellow and red cards, among others, could affect a match outcome

89 considering the quality of the opposition. Their results confirmed the importance of some of

90 these variables and the influence of the opposite team on match results.

Other variables were investigated by Lago (2009), such as match location and possession

92 strategies to better understand their influence on the match results and how teams can alter their

93 playing styles during the match in response to match status. The author examined twenty-seven

94 games from the 2005–2006 domestic league season in a professional Spanish soccer team. The

95 findings emphasize the relevance of accounting for these variables when studying tactics and

96 performance in soccer. Malamatinos (2022) conducted a study using multiple Machine Learning

97 methods to predict the outcome of games in the Greek Super League. The results found the most

98 important features that affect the results as Home Team Form and Away Team Form, for most

99 models. The Greek Super League was found to be the most predictable among the 3 leagues

100 analyzed, reporting 67.73% of accuracy with CatBoost.

Musa et al. (2021) analyzed the Asian beach soccer tournament through hierarchical

102 agglomerative cluster analysis, identifying relevant essential performance parameters that could

103 describe winning and losing performance in the tournament. A similar analysis was conducted

104 to find predictive variables of winning and losing in the Belgian soccer division by Geurkink

105 et al. (2021). Their results using Extreme Gradient Boosting showed an accuracy of 89.6% and

106 using TreeExplainer they found the most important variable for the prediction to be “total shots

107 on target from attacking penalty box”, followed by player’s physical indicators as number of 108 accelerations, runs and distance, and contextual variables as Home/Away match.

3 109 Materials and Methods

110 This research employs both unsupervised machine learning methods (for the clustering task)

111 and supervised methods (for selecting feature importance), in order to analyze and assess the

112 influence of different variables on the performance of teams in the Série A of the Brazilian

113 Championship. To ensure the robustness of the study, the data were consolidated from two

114 complementary sources.

The first data source used comprises match statistics from the Brazilian Football Cham-

116 pionship (Série A) spanning the years 2003 to 2024. The records were obtained through the plat-

117 form basedosdados.org, which consolidates information originally sourced from Transfermarkt,

118 a football-specialized database. This dataset includes game metrics and team characteristics for

119 each match. The data are structured separately for home and away teams.

To complement the analysis, a second dataset was incorporated, obtained from the

121 portal football-data.co.uk, containing probabilistic information on matches from the Brazilian

122 Championship between 2012 and 2024. These data represent the average odds offered by betting

123 companies for three possible outcomes: home win, away win, and draw. The inclusion of these

124 probabilistic variables enriches the study by adding a market perspective and mathematical

125 expectations regarding match outcomes.

The integration of the datasets enabled a more comprehensive analysis by combining

127 descriptive statistics with implied probabilities, thereby expanding the scope of the investigation.

128 After consolidating the data, the year 2019 was specifically selected for modeling, as it presented

129 the most complete set of information across both datasets.

For the clustering task, the K-Means algorithm was adopted, a method particularly suit-

131 able given the predominantly numerical nature of the variables and the objective of identifying

132 multivariate performance patterns among teams. K-Means is simple and flexible (Nayini et al.,

133 2017), and while easy to implement, it is also highly efficient and widely used across various

134 fields of knowledge (Chong, 2021).

The original data (organized by matches) were transformed into a team-level structure,

136 generating the variables presented in Table 1, which include totals, means, standard deviations,

137 minimums, and maximums of the defined metrics.

Variable

Table 1: Variables used in the team-level dataset.

Variable

Variable

Total Goals First Half Average Odds Total Shots Minimum Shots Off Target Minimum Set Pieces Minimum Fouls Minimum Age Victories Playing Against Team Bellow

Total Goals Total Shots Off Target Average Shots Maximum Shots Off Target Maximum Set Pieces Maximum Fouls Maximum Age Matches Against Team Above

Total Offsides Standard Deviation of Shots Standard Deviation of Offsides Total Set Pieces Total Fouls Average Age Victories Playing Against Team A

To neutralize the impact of differing variable scales given the distance-based nature of

139 the K-Means algorithm, the dataset was normalized using the MinMaxScaler method, converting

140 all values to the [0, 1] range. This standardization ensured that metrics with different units

141 (such as average age and number of goals) had equivalent weight in the cluster analysis. As a

142 preliminary step to clustering, a Principal Component Analysis (PCA), proposed by Hotelling

143 (1933), was conducted using five components that captured approximately 75% of the total data

144 variance. This dimensionality reduction served two key purposes: (1) it eliminated redundancies

145 among highly correlated variables, particularly relevant in interrelated sports metrics. This

146 transformation is based on the decomposition of the covariance matrix into eigenvalues and

147 eigenvectors, where the eigenvectors determine the directions of the new variables and the

148 eigenvalues indicate the variance explained by each component; (2) it preserved the essential

149 structure of the data by retaining most of the original information (Jolliffe and Cadima, 2016).

To determine the optimal cluster configuration, the silhouette score was employed. This

151 metric revealed that the configuration with six clusters yielded the highest average silhouette

152 score, indicating a more coherent clustering structure compared to solutions with fewer clusters.

153 The choice of six clusters is justified not only by the statistical criterion but also by its ability to

154 preserve strategic heterogeneity among teams, avoiding the excessive generalization observed

155 in broader groupings. This refined segmentation enabled the identification of distinct tactical

156 patterns and variations in operational efficiency.

The K-Means algorithm, selected for this analysis, stands out for its effectiveness in

158 segmenting numerical data into cohesive groups, operating through an iterative process that

159 minimizes the intra-cluster sum of squares. Specifically, the method: (1) initializes k centroids

160 randomly; (2) assigns each observation to the nearest centroid, calculated using Euclidean

161 distance; and (3) recalculates the centroids as the mean of the observations in each cluster,

162 repeating this process until convergence (Bramer, 2016). This approach ensures the progressive

163 minimization of intra-cluster variance and is particularly suitable for our preprocessed sports

164 dataset, where the goal is to maximize tactical homogeneity within each group while maintaining

165 clear strategic distinctions between clusters (Bezdek, 2022).

Complementing the cluster analysis, a Random Forest classifier was employed to assess

167 the importance of the variables in the formation of the clusters. This method quantifies the

168 contribution of each feature through the mean decrease in accuracy when its values are permuted,

169 enabling the identification of the most influential attributes for the resulting segmentation (Géron,

170 2019). To further enhance interpretability, the SHAP (SHapley Additive exPlanations) technique

171 was additionally applied. Based on cooperative game theory, SHAP assigns fair values to each

172 variable’s contribution to a model’s prediction. It sheds light on the underlying reasoning behind

173 machine learning model outputs (Lan et al., 2024), thus overcoming the limitations of black-box

174 models that typically offer only prediction results after training (Ferreyra et al., 2024). This

175 approach allowed us to: (1) identify the most discriminative variables across clusters using

176 Random Forest; (2) understand the direction and magnitude of each feature’s impact on specific

177 clusters through SHAP values, which capture how the presence or absence of a variable alters

178 the clustering prediction. Furthermore, the decomposition into Shapley values made it possible

179 to uncover variable interactions, revealing how specific combinations of attributes influence the

180 distinct tactical profiles of the six identified clusters.

Figure 1 illustrates the complete process: from data integration and transformation (with

182 PCA and normalization), through clustering using K-Means (k = 6 clusters), to the interpretive

183 analysis via Random Forest and SHAP, identifying the most relevant variables for the detected

184 performance-based groupings.

Figure 1: Flowchart of the analysis process for the Brazilian Championship dataset.

4 185 Results and Discussion

186 4.1 Distribution of Teams by Cluster

187 Figure 2 represents the distribution of teams in their respective cluster for better understanding in 188 the following analyses, while Figure 3 shows the top 5 relevant features concerning the clusters 189 created.

Figure 2: Heatmap distribution by cluster.

Figure 3: Graph Top 5 features importance x Cluster distribution.

190 4.2 Top 5 Features Importance x Cluster Distribution

191 Regarding Figure 3(a), the variable Average Odds reflects the betting market’s perception of each

192 team’s average probability of winning, where higher odds values indicate a lower probability

193 of victory. Notably, Clusters 1 and 6 exhibit the highest odds in the championship. This is

194 consistent, as these clusters include Avaí, Ceará, and Chapecoense—teams that demonstrated

195 low offensive performance and limited expectations of winning, both at home and away. These

196 teams finished at the bottom of the league table, with Avaí and Chapecoense being relegated to

197 the second division. Cluster 3 is particularly significant for its consistently low odds, indicating

198 a high probability of victory. This can be attributed to the dominant performance of the teams in

199 this cluster throughout the season, especially Flamengo. Cluster 5 displays the lowest average

200 odds among all clusters and includes Grêmio and Santos, which maintained relatively consistent

201 performances during the championship.

Analyzing Figure 3(b), the Total Goals variable represents the total number of goals

203 scored by each team during the championship. Clusters 1 and 2 recorded the fewest goals in

204 the league, characterized by unproductive attacks with limited creativity and offensive presence.

205 Cluster 3 includes the team with the highest number of goals, Flamengo. Clusters 4 and 5 are

206 composed of teams with offensive potential but display varied playing styles, as some teams

207 scored many goals while others scored relatively few. Cluster 6 consists of teams with low

208 offensive output, but which often secured victories by narrow scorelines.

Regarding Figure 3(c), this variable represents the team with the highest average age

210 among starting players. Two standout clusters in this chart are Cluster 1, which consists of

211 lineups with older players meaning more experienced squads, though sometimes lacking physical

212 intensity, which can be detrimental on the field, and Cluster 3, composed of teams with the

213 youngest squads among all clusters, typically showing higher offensive intensity when analyzed

214 in relation to other variables.

As for Figure 3(d), the variable represents the percentage of victories against higher-

216 ranked teams. Clusters 1 and 2 are composed of teams that struggle to overcome opponents with

217 stronger squads. In contrast, Clusters 5 and 6 include teams that perform well against superior

218 opponents, often traditional clubs that, despite being in a poor phase, still manage to remain

219 competitive. Teams such as Corinthians, Santos, and Palmeiras are present in these clusters.

Still discussing the findings from Figure 3, an interesting correlation was observed

221 between total goals and fouls: teams with low offensive output tend to commit more fouls, often

222 as a way to compensate for their lack of creativity and control of the game by adopting a more

223 physical and defensive style of play (Silva et al., 2009). Furthermore, teams with older squads

224 generally display a slower pace, which contributes to a higher number of fouls committed, as

225 lower intensity makes it harder to recover defensively and leads to more interruptions in play to

226 stop the opponent (Neto et al., 2020).

227 4.3 SHAP Analysis

228 To verify deeply the most important features in each cluster formation, Figure 4 illustrates the

229 SHAP values for each cluster.

Figure 4(a) illustrates Cluster 1, which groups teams with older squads on average

231 (Poli et al., 2018), including even among their younger players. These teams tend to struggle

232 offensively and show low competitiveness against opponents ranked above them. The presence

233 of Avaí, which was relegated at the end of the season, and Ceará, which also fought against

234 relegation, reinforces that this cluster represents teams with weak overall performance.

As shown in Figure 4(b), Cluster 2 includes younger teams that make little use of set

Figure 4: Graph SHAP Analysis.

236 pieces. There is no clear trend when it comes to their performance against higher-ranked

237 opponents, but these teams tend to take good advantage of playing at home, often securing wins

238 against weaker sides. Teams such as CSA and Cruzeiro, both relegated in 2019, along with

239 Atlético-MG, Internacional, and Vasco form a group with highly heterogeneous results, yet they

240 share similar tactical and structural profiles.

The analysis of Figure 4(c) reveals that Cluster 3 is characterized by teams with young

242 and dynamic squads, typically top-table teams that, in most matches, faced lower-ranked

243 opponents and were favored by the odds. These teams tend to have reliable defenses and likely

244 adhere to fair play principles, as indicated by a low number of fouls committed (Bunker and

245 Susnjak, 2022). They employ offensive and efficient playing styles, with little reliance on set

246 pieces, favoring either direct attacks or well-constructed plays combined with strong tactical

247 control. The presence of Flamengo, the league champion, and Fortaleza, a well-structured team,

248 reinforces this pattern of dominant and consistent performance throughout the 2019 season.

Regarding Figure 4(d), Cluster 4 is represented by experienced teams, with both high

250 average and maximum player ages. These teams are defensively disciplined and register a lower

251 number of set pieces, which may suggest a playing style based on physical pressure. Although

252 they are not always the protagonists, they remain competitive, a trait reflected in both the odds

253 and their tactical organization. This group includes mid-table teams with solid performance, as

254 well as some that had more consistent campaigns. The presence of Palmeiras and São Paulo,

255 both with experienced squads and a history of defensive solidity, reinforces the profile of this

256 cluster.

Based on the data from Figure 4(e), Cluster 5 comprises highly offensive teams, char-

258 acterized by intense attacking volume, sustained pressure in the opponent’s half, and a high

259 frequency of set-piece opportunities. These teams are consistently favored in betting odds due

260 to their aggressive positioning and relentless goal-seeking approach, though this style also leads

261 to tactical vulnerabilities. Notably, Grêmio and Santos epitomize this profile, combining rapid

262 transitions, sustained attacking pressure, and a high shot conversion rate.

Figure 4(f) demonstrates that Cluster 6 groups teams with striking characteristics related

264 to offensive inefficiency and a more defensive playing style, typically attempting many shots

265 during matches but with little accuracy. This is evidenced by the strong negative impact

266 associated with the total number of off-target shots and the highest number of missed shots

267 in a single match (Dwyer and Young, 2024). This combination indicates that while creating

268 opportunities, these teams have clear difficulties in finishing plays. Teams tend to carry some

269 favoritism in certain games, as shown by the influence of average odds, though this favoritism

270 doesn’t always translate into performance, especially when the team in question, like Corinthians,

271 is in poor form. Lower odds (indicating favoritism) have a positive impact, while higher odds

272 (indicating less market confidence) are associated with worse performances, which fits well with

273 Chapecoense, generally seen as underdogs. Another key point is that the high number of fouls

274 committed by teams in this cluster often reflects a more physical or reactive approach that may

275 compromise game rhythm. The prediction suggests these teams perform slightly better when

276 adopting a more restrained offensive posture, perhaps opting for a more conservative strategy.

277 The presence of older players is also notable, particularly when observing the maximum age

278 value of athletes, which tends to negatively affect predicted performance, likely by limiting

279 game intensity, physical recovery capacity, and transition speed.

280 4.4 Team Placement Dispersion and Cluster During the Championship

281 To better understand the behavior of the teams over time, Figure 5 shows the league standings 282 for each cluster.

Figure 5: Graph Team placement dispersion and cluster during the championship.

Cluster 1, shown in Figure 5(a), is characterized by a constant battle against relegation.

284 This group, composed of Avaí, Ceará, and Cruzeiro, displays the championship’s worst average

285 performance. From the very first rounds, these clubs occupied the bottom positions and remained

286 near the relegation zone throughout the competition. The Cluster 1 line in the first graph stays

287 consistently at the bottom of the table after the conclusion of the first round, indicating these

288 teams were technically weaker with little ability to recover during the tournament.

Cluster 2, shown in Figure 5(b), is characterized by a promising but unstable start. Com-

290 prising Atlético-MG, CSA, Internacional, and Vasco, this group showed significant fluctuation,

291 particularly in the early rounds. While some clubs started reasonably well, their performance

292 throughout the championship was marked by inconsistency. The cluster’s average trajectory

293 suggests either a performance decline or difficulty sustaining results, remaining predominantly

294 in the bottom half of the table.

As shown in Figure 5(c), Cluster 3, composed of Flamengo RJ, Fluminense, and For-

296 taleza, presents a distinct performance profile. Although the group as a whole falls within a

297 mid-table range in the round-by-round standings graph, this average is skewed by Flamengo’s

298 strong performance as the competition champions. Thus, Cluster 3 can be interpreted as a group

299 with consistent performances, featuring one outlier (Flamengo) that raised the group’s standard

300 while not substantially altering the average trajectory of the collective performance.

Figure 5(d) presents Cluster 4, composed of Atlético-PR, Bahia, Botafogo RJ, Goiás,

302 Palmeiras, and São Paulo. This is the largest group and represents competitive teams that

303 challenged for top-six positions (G6) without necessarily excelling. The cluster’s trend line in

304 the first graph occupies the upper-mid table range, indicating solid average performance but

305 lacking the consistency required to seriously compete for top positions.

Cluster 5, shown in Figure 5(e), is characterized by having the highest average perfor-

307 mance. Composed of Grêmio and Santos, its trend line remained in top positions throughout

308 virtually the entire tournament, with both teams demonstrating remarkable consistency and

309 competitiveness. The stability and sustained performance of these clubs established them as

310 strong title contenders.

Cluster 6, as evidenced in Figure 5(f), represents unfulfilled expectations. Composed

312 of Chapecoense-SC and Corinthians, this cluster stood out for displaying mediocre to poor

313 performance, with consistent positioning in the lower half of the table. The most intriguing

314 aspect here is Corinthians’ presence alongside Chapecoense, indicating that, despite the his-

315 torical differences between these clubs, their performances in that particular tournament were

316 statistically similar in terms of volatility and table positioning. The cluster’s trend line remains

317 in the lower-mid table range, revealing underwhelming performance relative to expectations.

5 318 Conclusion

319 This study primarily aimed to explore the use of machine learning techniques, with emphasis 320 on combining data clustering methods, a Random Forest classifier, and interpretative SHAP 321 analysis, to delineate performance profiles of teams in the Brazilian Soccer Championship.

322 The integration of these approaches enabled a structured and explainable understanding of the

323 patterns characterizing different collective team behaviors throughout the competition.

The results demonstrated that applying these techniques in sports contexts can not only

325 enhance the analytical capabilities of professionals in the field but also strengthen data-driven

326 decision-making. The cluster analysis revealed six distinct team profiles, ranging from groups

327 with aging squads and low competitiveness to intensely offensive teams with high shot volumes

328 and constant presence in the opponent’s half. The study also highlighted groups featuring young,

329 dynamic squads with solid and disciplined performances, as well as clusters of teams with low

330 offensive efficiency despite high shot counts, employing more physical or reactive strategies.

331 This segmentation underscores the championship’s tactical and structural diversity, providing a

332 concrete foundation for predictive analysis and more informed strategic decisions.

The Random Forest implementation identified key determining variables, including: goal

334 totals, starting lineup’s average age, win percentage against higher-ranked opponents, betting

335 market odds, and foul counts, all suggesting direct impacts on collective performance. The

336 correlation between these characteristics revealed a novel perspective for performance analysis

337 in soccer analytics.

The limitations of this study may be found in the sample size (i.e., the number of

339 teams considered from only one specific championship) and in the variables used, as several

340 other factors could characterize teams’ playing styles, such as ball possession, for example.

341 Additionally, teams’ historical performance in other competitions or derby victories could also

342 influence results from a psychological perspective.

For future studies, we recommend enhancing the proposed model by incorporating

344 additional statistical and contextual variables, such as ball possession, pass completion rates,

345 average player ratings per match, weather conditions, stadium attendance figures, data from

346 concurrent tournaments, player tracking (GPS) data, and even physiological metrics. These

347 additions could significantly enrich the analyses and enhance their practical applicability in real-

348 world sports management scenarios. Furthermore, integrating hybrid approaches that combine

349 clustering with supervised predictive models could expand the methodology’s potential for

350 match outcome prediction and tactical strategy optimization.

## 351 Acknowledgments

352 The authors would like to thank Fundação Araucária for the financial support through a research 353 scholarship conceded to the first author. The authors also acknowledge the Research Group in 354 Optimization and Data Mining at the Universidade Tecnológica Federal do Paraná (UTFPR), 355 Londrina campus, for the institutional support and collaborative environment.

## 356 References

357 Andreff, W. (2021). Economic globalization of the sports industry. In Maguire, J., Liston, K., 358 and Falcous, M., editors, The Palgrave Handbook of Globalization and Sport, pages 271–295. 359 Palgrave Macmillan, London, UK. 360 Bezdek, J. C. (2022). Elementary Cluster Analysis: Four Basic Methods that (Usually) Work. 361 CRC Press, Boca Raton, FL. 362 Bilek, D. G. and Ulas, E. (2019). Predicting match outcome according to the quality of opponent 363 in the English Premier League using situational variables and team performance indicators. 364 International Journal of Performance Analysis in Sport. 365 Bramer, M. (2016). Principles of Data Mining. Springer, London, UK, 3rd edition. 366 Bunker, R. and Susnjak, T. (2022). The application of machine learning techniques for predicting 367 match results in team sport: a review. Journal of Artificial Intelligence Research, 73:1285– 368 1322. 369 Chong, B. (2021). K-means clustering algorithm: a brief review. Academic Journal of Computing 370 & Information Science, 4(5):37–40. 371 Diquigiovanni, J. and Scarpa, B. (2018). Analysis of association football playing styles: an 372 innovative method to cluster networks. Statistical Modelling, 19(1):28–54. 373 Dwyer, D. B. and Young, C. M. (2024). Shots at goal in Australian football: historical trends, 374 determinants of accuracy and common strategies. Journal of Science and Medicine in Sport, 375 27:354–359.

376 Fernandez-Navarro, J. et al. (2016). Attacking and defensive styles of play in soccer: analysis of 377 spanish and english elite teams. Journal of Sports Sciences, 34(24):2195–2204.

378 Ferreyra, L. F. M., Tauil, Y. B., Adigneri, H. M., Santos, B. S., and Lima, R. (2024). Análise 379 da satisfação com a economia a partir de modelos de aprendizado de máquina e inteligência 380 artificial explicativa. Navus – Revista de Gestão e Tecnologia, 15:1–16.

381 Fimmanò, F. R. (2024). Towards a global regulation of the football industry. Corporate 382 Governance and Research & Development Studies, (2):93–114.

383 Géron, A. (2019). Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow. 384 O’Reilly Media, Sebastopol, CA, 2nd edition.

385 Geurkink, Y. et al. (2021). Machine learning-based identification of the strongest predictive 386 variables of winning and losing in Belgian professional soccer. Applied Sciences, 11:2378.

387 Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. 388 Journal of Educational Psychology, 24(6):417–441.

389 Jolliffe, I. T. and Cadima, J. (2016). Principal component analysis: a review and recent 390 developments. Philosophical Transactions of the Royal Society A, 374(2065):20150202.

391 Lago, C. (2009). The influence of match location, quality of opposition, and match status 392 on possession strategies in professional association football. Journal of Sports Sciences, 393 27(13):1463–1469.

394 Lan, H., Wang, S., and Zhang, W. (2024). Predicting types of human-related maritime ac395 cidents with explanations using selective ensemble learning and SHAP method. Heliyon, 396 10(9):e30046.

397 Malamatinos, M.-C. (2022). On predicting soccer outcomes in the Greek league using machine 398 learning. Computers, 11(9):133.

399 Musa, R. M. et al. (2021). An information gain and hierarchical agglomerative clustering 400 analysis in identifying key performance parameters in elite beach soccer. In Zakaria, M.,

401 Abdul Majeed, A., and Hassan, M., editors, Advances in Mechatronics, Manufacturing, and 402 Mechanical Engineering, Lecture Notes in Mechanical Engineering. Springer, Singapore. 403 Nayini, S. E. Y., Geravand, S., and Maroosi, A. (2017). A novel threshold-based cluster404 ing method to solve K-means weaknesses. In 2017 International Conference on Energy, 405 Communication, Data Analytics and Soft Computing (ICECDS), pages 47–52, Chennai, India. 406 Neto, E. K., Barbosa, S., Teoldo, I., and Cardoso, F. (2020). Influência da idade relativa na 407 participação de jogadores de futebol na Série A do Campeonato Brasileiro. Rev. Bras. Futebol, 408 13(3):41–53. 409 Okazaki, V. H. A., Dascal, J. B., Okazaki, F. H. A., and Teixeira, L. A. (2012). Ciência e 410 tecnologia aplicada à melhoria do desempenho esportivo. Revista Mackenzie de Educação 411 Física e Esporte, 11(1):143–157. 412 Pisaniello, A. (2024). The game changer: how artificial intelligence is transforming sports 413 performance and strategy. Geopolitical, Social Security and Freedom Journal, 7(1):75–84. 414 Poli, R., Ravenel, L., and Besson, R. (2018). Is there an optimum squad age to win in football? 415 Technical Report 32, CIES Football Observatory. 416 Rein, R. and Memmert, D. (2016). Big data and tactical analysis in elite soccer: future challenges 417 and opportunities for sports science. SpringerPlus, 5(1410). 418 Silva, S. A., Silva, C. D., Paoli, P. B., Bottino, A. A., and Marins, J. C. B. (2009). Análise de cor419 relação dos indicadores técnicos que determinam o desempenho das equipes no Campeonato 420 Brasileiro de futebol. Rev. Bras. Futebol, 2(2):40–45.
