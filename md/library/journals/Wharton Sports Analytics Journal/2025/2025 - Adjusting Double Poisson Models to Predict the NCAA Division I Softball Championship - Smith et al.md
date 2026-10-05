<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Adjusting Double Poisson Models to Predict the NCAA Division I Softball Championship - Smith et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/adjusting-double-poisson-models-to-predict-the-ncaa-division-i-softball-championship/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2025 -->
<!-- authors: Liam Smith; Brendan Ames -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Adjusting Double Poisson Models to Predict the NCAA Division I Softball Championship

1Liam Smith, 2Brendan Ames

1The University of Alabama, Randall Research Scholars Program 2University of Southampton, School of Mathematical Sciences

April 2025

Abstract While its viewership has surged in recent years, college softball remains an under-researched sport in the domain of sport analytics, partially due to a lack of a longstanding major professional league. However, the postseason format of major college softball - a four-stage layout with two four-team double elimination phases and two best-of-three series - presents an intriguing challenge for predictive models. Primarily focusing on the first of these four stages, we evaluate the effectiveness of a Double Poisson model in predicting the outcome of this competition. This model, previously developed and advanced for use in predicting the outcome of soccer matches, posits that a team’s number of runs scored takes a Poisson distribution, with a mean based on its own offensive strength and its opponent’s defensive strength, with strengths expressed in terms of scoring averages. Using game-by-game results for runs scored and runs against, we construct two additional pairs of factors used in constructing the means of these Poisson random variables for each team that account for a team’s strength of schedule and conference membership. From these additional factors, we construct an adjusted model that aims to account for these factors, and assess both the unadjusted base model and the adjusted model’s ability to predict the 2024 NCAA Division I Softball Tournament through simulation, with the aim of better understanding factors associated with success in this compelling tournament format.

1 1 Introduction

2 The eight team Women’s College World Series (WCWS), held in Oklahoma City, is the culmination of 3 each edition of the NCAA Division I Softball Tournament. In recent years, both in-person attendance and 4 television viewership for the event has surged. In the best-of-three finals of the 2024 WCWS, in which 5 Oklahoma defeated rival Texas to win its fourth consecutive national title, television viewership on the 6 ESPN family of networks reached the highest levels on record, with two million viewers tuning in (Callahan, 7 n.d.). The 2022 edition of the finals, also between Oklahoma and Texas, eclipsed the corresponding series of 8 the Men’s (Baseball) College World Series (MCWS), with an average of 1.7 million viewers tuning into the 9 softball event, whereas the most-viewed game of the MCWS finals between Ole Miss and Oklahoma averaged 10 1.63 million viewers (Staff, n.d.). Meanwhile, a recent expansion of the host stadium for the WCWS has 11 enabled continued growth in attendance. Whereas the event hosted an average of 72,747 fans in the 2010s, it 12 averaged 112,123 between 2021 and 2023, the first three seasons of increased seating capacity in Oklahoma

13 City, an increase of over 54 percent (National Collegiate Athletic Association, 2024b). 14 Despite this live and televised success, college softball - with its compelling, multi-level postseason format 15 - remains an under-researched sport in analytics literature. In this paper, we adjust a model, the Double 16 Poisson, that has previously been used to predict the outcomes of soccer matches by constructing two sets 17 of adjustment factors based on teams’ conference affiliation and performance relative to schedule. We build 18 an adjusted model that incorporates these factors into the computation of the mean of the Poisson random 19 variables and evaluate the adjusted model against a base implementation of the Double Poisson (using 20 only runs scored and allowed averages) in predicting the outcomes of the 2024 NCAA Division I Softball 21 Championship, beginning at the regional phase and progressing through the Women’s College World Series.

22 1.1 NCAA Division I Softball Tournament Structure

23 The first NCAA Division I Softball Tournament was held in 1982 with a 16-team structure and culminated 24 in a championship held in Omaha, Nebraska. Over time, the number of participants has grown to the current 25 64-team setup, with 31 teams earning automatic bids by winning their respective conferences, and 33 teams 26 being selected by a committee to receive at-large bids. Of these 64 teams, 16 are chosen to host four27 team double elimination tournaments, termed regionals, on the first round of competition; the Tuscaloosa 28 Regional from the 2024 edition of the tournament is shown below as an example. In this example, the “if 29 necessary” game was not required because the undefeated team (Alabama) defeated the team with one loss 30 (Southeastern Louisiana), thereby eliminating Southeastern Louisiana with the Lions’ second loss.

The winners of these sixteen regionals move on to a best-of-three series against another regional winner,

Figure 1: 2024 Tuscaloosa Regional Bracket

32 held at the higher seed’s ballpark on the second weekend of the tournament and termed the super regionals. 33 The eight super regional winners advance to the Women’s College World Series (WCWS) in Oklahoma City. 34 In WCWS play, the eight teams are split into two four-team double elimination brackets and essentially 35 repeat the first two rounds over the course of nine days, culminating in the best-of-three WCWS Finals. The 36 only difference is that the loser of the winner’s bracket championship in each four-team bracket moves to the 37 other four-team bracket instead of remaining in its own bracket (National Collegiate Athletic Association, 38 2024b). The complexity of this multistage tournament format, as well as the variation in team quality due 39 to all conferences receiving at least one bid, make this a challenging format to build predictive models for.

Figure 2: 2024 Women’s College World Series Bracket 3

40 1.2 Double Poisson Models

41 Using Poisson random variables to model outcomes in English soccer was first proposed by M.J. Maher in 42 1982, under the justification that a team has many individual chances to score over the course of a match, but 43 that the probability of any individual opportunity being successful was relatively low. In such a model, the 44 number of goals scored by team i against team j, Xij, is assumed to be Poisson distributed with a mean de45 termined based on the offensive strength of team i and defensive vulnerability of team j, where the strengths 46 are measured in expressions related to the number of goals scored and allowed (Maher, 1982)(Wackerly, 47 Mendenhall III, & Scheaffer, 2008). Under this model, the probability that team i defeats team j with Xij 48 as defined above is P (Xij) > P (Xji). 49 More recently, Penn and Donnelly have advanced this work, using a Double Poisson model to predict the 50 results of the 2020 Euro soccer team tournament between European national teams. In their analysis, at51 tacking (offensive) strengths and defensive vulnerability values are calculated using maximum likelihood 52 estimation, and matches against teams with exceedingly large defensive vulnerability values were removed 53 prior to recalculating such values (Penn & Donnelly, 2022). In their work, issues with including teams with 54 poor defensive quality were noted often; whereas their work removed such teams from the dataset, we include 55 such teams, as even a team with a weak defensive strength may still win its conference and advance to NCAA 56 tournament play, and attempt to construct adjustment variables to properly situate these teams. 57 When attempting to use the same algorithm and starting values used by Penn and Donnelly to solve the 58 system of equations for offensive strength and defensive vulnerability, the system did not converge beyond 59 a reasonable threshold, possibly due to a much larger number of teams in the dataset or additional sparsity 60 in the team-versus-team competition matrices, as teams in college softball played roughly ten percent of the 61 overall 296 team dataset in 2024 (mpenn114, 2022). In this work, rather than using the previously-built 62 maximum likelihood estimation methods for determining the mean of the Poisson distributions correspond63 ing to run scoring, we build a base formulation and use adjustment factors to determine whether these 64 factors, build from the structures inherent to college softball, can build an implementation of the model to 65 appropriately predict postseason competition.

2 66 Materials and Methods

67 2.1 Data

68 The dataset for this model includes all regular-season games from the 2024 NCAA Division I softball season. 69 Game-by-game data was scraped from stats.ncaa.org using a purpose-built scraper in Python for each team 70 (National Collegiate Athletic Association, 2025). For the purposes of this work, only games between full 71 Division I member schools were considered; games against member schools transitioning to Division I or 72 those in Division II, III, or the NAIA were not considered as such schools may operate under different 73 association-imposed scholarship restrictions and thus be inherently competitively imbalanced.

74 2.2 Base Model

75 For all Double Poisson models in this work, we consider the offensive strength (Oxi ) and defensive vulner76 ability (Vxi , where Vxiu is the unscaled version) of team x1 (out of a set of m full member institutions 77 x1, x2, ..., xm) in the following way. Given a team’s set of n games prior to the NCAA tournament indexed 78 by g, (g, f, a), where f represents the number of runs for (scored by) team xi in game g, and a represents 79 the number of goals against team xi in game g, we have:

Oxi = n g=1 f

, n

Vxiu = n g=1 a

, n

Vxi = 1 m

Vx1u m j=1

Vxju

.

80 Thus, Oxi is the average number of runs scored in a particular year by team xi across all games prior to 81 the tournament, and Vxiu (unscaled defensive vulnerability) is the average number of runs allowed in a 82 particular year by team xi across all games prior to the tournament. The Vxi value is then taken by dividing 83 the unscaled defensive vulnerability by the average of all unscaled defensive vulnerabilities.

84 This definition of Ox and Vx differs significantly, however, from the derivation of those values in the previous 85 work of Penn and Donnelly. In their work, offensive strength and defensive vulnerability parameters were 86 estimated, using the maximum likelihood estimator, as the solutions to a system of equations. The objective 87 function for such a system involved, for m teams, two square matrices of dimension m. In the matrix used 88 for games played, here denoted G, the entry gij denoted the number of international games played between 89 countries i and j in their dataset. The number of goals scored by country i against country j was recorded 90 similarly in a score matrix, here denoted S. (Penn & Donnelly, 2022).

91 However, there are situational differences between the work of Penn and Donnelly and the challenge of 92 applying this model to college softball. In this work, we seek to understand how the inherent structure of

93 college softball in the form of conferences and the inherent imbalance in team scheduling can be leveraged 94 to adjust a base model to create better predictions, so we propose a na¨ıve base model to use as a standard 95 of comparison in which team strengths are expressed purely in terms of scoring averages. In addition, 96 this model aims to solve a problem found by Penn and Donnelly introduced by teams with large defensive 97 vulnerabilities; whereas their work fixed the largest V value at 1, we scale our V values relative to the mean 98 so that a single weak defensive team has less impact on the remaining teams’ V values.

99 From these offensive and defensive vulnerabilities, we calculate the mean of the Poisson random variables 100 representing the predicted number of runs scored by team a against team b and vice versa. Letting µa,b 101 represent the mean of Ra,b, the predicted number of runs scored by a, and µb,a represent the mean of Rb,a, 102 the predicted number of runs scored by b, these are expressed as follows in the base Double Poisson model: µa,b = (Oa)(Vb), µb,a = (Ob)(Va),

Ra,b ∼ P oisson(µa,b),

Rb,a ∼ P oisson(µb,a).

103 Therefore, the probability of team a defeating team b, pa,b is given by the following for the case where ties 104 are possible: pa,b = P (Ra,b > Rb,a).

105 However, a significant difference between predictive modeling in soccer matches versus college softball is the 106 issue of ties. In soccer, a game may end after regulation is played in a tie. However, ties are extraordinarily 107 rare - and usually the result of weather-related interruptions, as was the case between Auburn and Virginia 108 Tech in 2024. In that situation, the game concluded in a 5-5 tie due to unplayable field conditions following 109 an extended rain delay near the end of the game (Virginia Tech, 2024). Because the Poisson distribution is 110 discrete, P (Ra,b = Rb,a) ≠ 0, so we must consider the situation of ties.

111 Ties in softball at the end of regulation play are, except in these rare cases, settled with extra innings. We 112 assume that the strengths that a team has during the seven innings of regulation play carry over to extra 113 innings, so the relative probabilities of victory should remain constant. While this assumption may not be 114 true in select cases, such as a player becoming injured or otherwise unable to continue, it is likely not a 115 major source of error, as softball teams routinely play more than seven innings per day, especially during 116 early-season non-conference tournaments - and even the NCAA tournament. Under this assumption, we 117 eliminate the possibility of ties by maintaining this proportionality and define pa,b, the probability that team 118 a defeats team b, in the following manner for the remainder of this work: pa,b

=

P (Ra,b

P (Ra,b > Rb,a) > Rb,a) + P (Rb,a

>

Ra,b)

119 To account for the vast difference in team quality between college softball teams and correct some of 120 the errors associated with the above “base” model, we propose two pairs of factors to account for this: 121 the conference adjustment factors and schedule adjustment factors. Each factor is constructed such that 122 a “theoretically average” team would have a value equal to 1, and each pair of factors contains one factor 123 adjusting the team’s offensive strength and one factor adjusting the team’s defensive vulnerability with 124 respect to the attribute under study.

125 2.3 Conference Adjustment Factors

126 The underlying assumption of the conference-adjustment factors is that teams compete in conferences 127 that contain teams of relatively similar quality, so a team’s conference affiliation provides some information 128 about its expected performance. Because of this, non-conference games may be used to construct an approx129 imate judgment of the conference’s quality. For instance, Marist, a member of the MAAC, was within the 130 top 20 in overall runs per game in 2024. However, the MAAC’s schedule-adjusted defensive vulnerability, 131 as defined below, was roughly 1.35, meaning that teams in the MAAC allowed non-conference opponents to 132 score 35 percent more than their season-long averages in the typical game, adding context to Marist’s high 133 run-scoring totals.

134 Let the set (g, f, a, xi) be the set of G non-conference games played by teams in conference C1, indexed by

135 g ∈ {1, 2, 3, ..., G}, in which teams in conference g scored f runs and allowed a runs against team xg. Then

136 the schedule-adjusted offensive strength, OC1 , and schedule-adjusted defensive vulnerability, VC1 are defined

137 as follows:

OC1 =

G g=1

( f Vxgu

)

G

VC1 = gG=1( a Oxg

)

G

138 Essentially, a conference’s offensive strength is the average, over all non-conference games, of the ratio 139 between the number of runs scored by that conference’s team to the season-long average runs allowed by the 140 team’s opponent. Conversely, the conference’s defensive vulnerability is the average, over all non-conference 141 games, of the ratio between the number of runs given up by that conference’s team to its opponent’s season142 long average number of runs scored. We would expect a “theoretically-average” conference to have teams 143 that give up as many runs as their opponents typically score, so this “theoretically average” conference would 144 have OC = 1 and DC = 1. The top five and bottom five conferences in schedule-adjusted offensive strength 145 and schedule-adjusted defensive vulnerability are shown below for the 2024 season. As may be expected, 146 this set of variables primarily benefits schools in “Power” conferences:

Conference SEC Big 12 ACC Pac-12

Big Ten ...

MAAC NEC MEAC Horizon SWAC

2024 OC Value 1.655 1.634 1.482 1.365 1.284 ... 0.7412 0.7161 0.6406 0.6159 0.5409

Conference SEC Pac-12 Big 12 ACC

Sun Belt ...

America East MAAC Horizon MEAC SEAC

2024 VC Value 0.440 0.594 0.679 0.705 0.797 ... 1.333 1.346 1.464 1.584 1.679

Table I: Top and Bottom Five Conference Offensive Strength, Defensive Vulnerability Values

147 2.4 Schedule Adjustment Factors

148 Meanwhile, the underlying assumption of the schedule-adjusted factors is that strong teams will score 149 more than their opponents usually allow - and conversely allow fewer runs than their opponents typically 150 score, and that these quantities can shed light on the quality of a team’s offense and defense. This can serve 151 as a testament to the success of even the most successful offenses: Oklahoma’s 8.1 runs per game in the 152 2024 season ranked near the top of college softball, but their offensive dominance becomes clear when their 153 schedule-adjusted offensive strength value is examined as defined below: the Sooners scored 96 percent more 154 runs, on average, than their opponents’ average number of runs allowed.

155 Let the set (g, f, a, xg) be the set of games played by team xi over the course of a season, indexed by 156 g ∈ {1, 2, 3, ...G}, where team xi scores f runs and allows a runs against team xg. Then the schedule157 adjusted offensive strength of team xi, denoted OSi , and schedule-adjusted defensive vulnerability of team 158 xi, denoted VSi , are given by:

Gf

Ga

OSi = g=1 Vxgu

G

VSi = g=1 Oxg

G

160 Essentially, a team’s schedule-adjusted offensive strength is the average, over all games played, of the ratio 161 between its number of runs scored in the particular game and the average number of runs allowed by its 162 opponent. Conversely, a team’s schedule-adjusted defensive vulnerability is the average, over all games 163 played, of the ratio between its number of runs allowed in the game to the average number of runs scored 164 by its opponent over the course of the season. We propose that a “theoretically average” team would score 165 as much as each of its opponents usually allows - and give up as many runs as its opponents usually score 166 thereby having OS = VS = 1. The following gives the top five and bottom five schedule-adjusted offensive 167 strength and defensive vulnerability values for the 2024 season:

Team Florida Miami-Ohio Florida State Oklahoma Texas

... Arkansas Pine Bluff

Alcorn State FDU

Detroit-Mercy Lafayette

2024 OS Value 2.194 2.083 1.999 1.962 1.919 ... 0.483 0.476 0.453 0.401 0.399

Team Boston Duke Oklahoma Tennessee Stanford

... UMES Detroit-Mercy Alabama A-M St. Bonaventure Mississippi Valley State

2024 VS Value 0.296 0.322 0.333 0.340 0.413 ... 1.882 1.907 1.964 2.100 2.131

Table II: Top and Bottom Five Schedule-Adjusted Offensive Strength, Defensive Vulnerability Values

168 2.5 Adjusted Model

169 The adjusted Double Poisson aims to incorporate both factors associated with stronger conference member170 ship and strength of schedule into its predictions. Using the same notation for µa,b and Ra,b as before with 171 team a in conference i and team b in conference j, we define: µa,b = (Oa)(Vb)(OCi )(VCj )(OSa )(VSb ), µb,a = (Ob)(Va)(OCj )(VCi )(OSb )(VSa ),

Ra,b ∼ P oisson(µa,b),

Rb,a ∼ P oisson(µb,a).

173 The probability of team a defeating team b is defined in the same manner as in the base model in section 2.2, 174 so as to account for the fact that ties are not permitted at any stage of the tournament under consideration.

3 175 Results

176 3.1 High-Level Overview

177 To assess the performance of the adjusted model against its base counterpart, the 2024 edition of the NCAA 178 Division I Softball Championship was simulated in its entirety 2000 times from the starting 64-team bracket, 179 with the winners noted on both a game-by-game and stage (e.g., the winner of a particular regional) level. 180 In our analysis of results, we assess the models’ performance based on their ability to predict winners at a 181 stage level, rather than a game-by-game level, as there are multiple paths to stage-level victory for a team 182 due to the double-elimination nature of the tournament. 183 The following shows the model success at the conclusion of three of the four stages: regional, super regional, 184 and Women’s College World Series finals play. Outside of the finals, in which there is one series to predict, 185 model success is defined as the average, over all competitions within a stage, of the number of trials in which 186 the winner was correctly chosen at that stage. As may be expected, model success decreases over the course 187 of the tournament because a round’s results in a given trial are dependent on the prior simulations within 188 that trial.

Figure 3: Model Success in Regionals, Super Regionals, and Women’s College World Series for 2024 189 As shown below, the adjusted model performed better at each stage of the competition compared to the 190 base model. This demonstrates the adjusted model’s ability to discriminate between teams of both similar 191 quality and vastly different quality, as teams become more evenly-matched over the course of the tournament.

192 3.2 Regional Results

Figure 4: Number of Trials Correctly Predicting Winner by Regional 193 In 13 of the 16 regionals in 2024, the adjusted model outperformed the base model, with the adjusted model 194 correctly predicting the regional winner in all 2000 trials for four regionals. In the Norman regional, then195 three-time defending national champion (and second overall seed) Oklahoma was chosen to advance from its 196 regional correctly in just 1001 of 2000 trials under the base model, whereas the adjusted model chose the 197 Sooners to advance in 1969 trials. Proportionally, the largest increase in model performance occurred in the 198 Tuscaloosa Regional, hosted by Alabama. As shown in the bracket in the introduction, the Crimson Tide 199 advanced easily from its regional, but was chosen to advance from the regional round in just 7.9% of trials, 200 whereas the adjusted model chose the Crimson Tide to advance in 48.5% of trials.

202 Because the regional round is not dependent on the result of any prior rounds, we may directly investigate 203 differences between the models that explain the adjusted model’s increased rate of success through tables 204 describing the probability that, under a given model, one team defeats another. The following tables give 205 the probability, for the 2024 Tuscaloosa Regional (won by Alabama), that the team in a given row defeats 206 the team in a given column under both models.

2024 Tuscaloosa Regional (under base model) Alabama Clemson Southeastern Louisiana USC Upstate

2024 Tuscaloosa Regional (under adjusted model) Alabama Clemson Southeastern Louisiana USC Upstate

Alabama

0.702 0.740 0.506 Alabama

0.521 0.208 0.012

Clemson

0.298

0.563 0.288 Clemson

0.479

0.130 0.001

Southeastern Louisiana 0.260 0.437

0.247

USC Upstate

0.494 0.712 0.753

Southeastern Louisiana 0.792 0.870

0.049

USC Upstate

0.989 0.999 0.951

Table III: Probability Tables for 2024 Tuscaloosa Regional

207 As shown above, the base model does not favor Alabama, which was seeded 14th in the nation by the 208 selection committee, in any of its matchups against regional opponents, which is unlikely to be the case. The 209 adjusted model largely corrects for this, as the Crimson Tide are favored against two of three opponents; as 210 shown in the regional bracket in the introduction, Alabama did not face Clemson in regional play.

211 3.3 Super Regional Results

Figure 5: Number of Trials Correctly Predicting Winner by Super Regional 212 Unlike the regional round, the majority of super regionals in 2024 were correctly predicted by the base 213 model, as the adjusted model correctly predicted just three super regionals correctly more often than the 214 base model. However, the difference in performance for these three super regionals (Austin, Norman, and

215 Gainesville) is much greater than the difference in model performance for the five correctly predicted more 216 often by the base model. The Knoxville Super Regional, in which Alabama defeated host Tennessee, was 217 correctly predicted in the fewest number of trials. This can be understood in the context of regional results; 218 Alabama advanced to the super regional round in relatively few trials under the adjusted model and especially 219 in the base model, whereas Tennessee advanced to the super regional round in each of the 2000 trials under 220 the adjusted model and in over three-quarters of trials in the base model.

221 3.4 Women’s College World Series Results

222 As shown below, the adjusted model correctly predicted Oklahoma to win the national championship in 223 nearly twice the number of trials as compared to the base model. Furthermore, the predictions made by the 224 base model were far more egalitarian than those made by the adjusted model, as Oklahoma and Tennessee 225 finished as national champions in over three-quarters of trials under the adjusted model, whereas the most common national champion choice under the base model accounted for under one quarter of trial results.

Figure 6: Comparison of National Champion Predictions

227 These results also point to another fundamental flaw of the base model: overestimating the strength of 228 teams that performed well against weaker competition. The most common national champion among tri229 als simulated under the base model was Boston University, which performed well in the regular season 230 against a weaker conference schedule and was eliminated in the regional round (National Collegiate Athletic 231 Association, 2024a).

4 232 Discussion and Conclusion

233 4.1 Discussion

234 The performance of the adjusted model both indicates that conference affiliation and performance relative 235 to schedule, as measured by the ratio of single-game results to season-long averages, are associated with 236 success in the college softball postseason, and that the factors constructed in this work are effective ways to 237 account for these as opposed to relying solely on run scoring and allowance averages. In addition, this work 238 provides a framework for future work to construct additional adjustment factors and determine the proper 239 weighting of adjustment factors to accurately predict team success, as well as the ability to better quantify 240 the extent of an upset in the early rounds of the tournament. 241 While the adjusted model does consider several key factors associated with success, there are limitations in242 herent to the implementation of these factors, primary among which is the effect of the model on teams with 243 abilities significantly different than their conferences’ strength, as it overestimates the strength of weaker 244 teams in strong conferences and likewise underestimates the strength of strong teams in weak conferences. 245 Because roughly half of the tournament field qualifies for the tournament by winning their respective confer246 ences, this may be considered in future implementations. Similarly, there is no consideration in this model 247 for home field advantage, the phenomenon in which teams tend to perform better when playing at home; 248 because these regionals are hosted by the top team competing in them, this factor may be considered in the 249 future. 250 Besides predicting the outcomes in major college softball, this modeling serves two broader purposes. First, 251 it provides a conceptual framework (leveraging the nature of the sport itself) to use in other cases where 252 the traditional implementation of the Double Poisson alone runs into similar problems. On a broader level, 253 however, it serves to build the very limited amount of analytics research done specifically on college softball, 254 providing a baseline for further work, which may include refining models to eliminate some of the previously 255 discussed limitations to this implementation, in this sport, with a goal of increasing long-term quantitative 256 interest in this under-researched sport.

257 4.2 Conclusion and Future Work

258 In this paper, we have proposed a base model that estimates the parameters of the Double Poisson for a 259 setting in which team-versus-team matrices are sparse and evaluated the performance of the model against 260 alternatives that take into account attributes of strength of schedule and conference affiliation. We have

261 found that these alternative models bring with them greater accuracy, on average, but also greater variance 262 in the distribution of those accuracy values. Future work in this area could involve assessing the relative 263 performance of these models in the second (Super Regional) round of the NCAA Division I Softball Tour264 nament, as well as the Women’s College World Series, and constructing an algorithm to predict which of 265 the four models would work best given a set of input teams. These investigations would serve to advance 266 quantitative approaches to this under-researched, yet quickly growing, sport. 267 In addition to adding adjustment factors and modifying their weights, future work in this area can include 268 assessing the accuracy of the model in predicting the remainder of the regular season after a given date - and 269 how this accuracy changes with changes to the given cutoff date. Other work could involve attempting to 270 implement the traditionally-defined Double Poisson model with strengths calculated via maximum likelihood 271 estimation on a conference-versus-conference level then on a team-by-team level within conferences to avoid 272 issues related to sparse matrices.

273 4.3 Acknowledgments

274 The authors acknowledge the Randall Research Scholars Program at The University of Alabama for providing 275 computing resources used to obtain data, analyze team strengths, and simulate results in this paper.

## 276 References

277 Callahan, K. (n.d.). Espn viewership clears the bases during 2024 division i ncaa softball season. ESPN

Press Room. Retrieved 2024-08-31, from https://espnpressroom.com/us/press-releases/2024/

06/espn-viewership-clears-the-bases-during-2024-division-i-ncaa-softball-season/

280 Maher, M. (1982). Modelling association football scores. Statistica Neerlandica, 36 , 109–118. doi: https:// doi.org/10.1111/j.1467-9574.1982.tb00782.x

282 mpenn114. (2022). Euro 2020 predictor. Retrieved from https://github.com/mpenn114/Euro 2020

Predictor

284 National Collegiate Athletic Association. (2024a). 2024 ncaa division i softball official bracket. Retrieved

2024-09-01, from https://www.ncaa.com/brackets/softball/d1/2024

286 National Collegiate Athletic Association. (2024b). 2024 women’s college world series® records book. National

Collegiate Athletic Association. Retrieved 2024-08-31, from http://fs.ncaa.org.s3.amazonaws

.com/Docs/stats/softball wcws rb/FullBook.pdf

289 National Collegiate Athletic Association. (2025). Ncaa statistics database. Retrieved from https://www

.stats.ncaa.org

291 Penn, M. J., & Donnelly, C. A. (2022). Analysis of a double poisson model for predicting football results in euro 2020. PLOS One. doi: https://doi.org/10.1371/journal.pone.0268511

293 Staff, T. A. (n.d.). Women’s college world series final outgains men’s final, averages 1.7 million viewers. The

Athletic. Retrieved 2024-08-31, from https://www.nytimes.com/athletic/4169889/2022/06/29/ womens-college-world-series-final-outgains-mens-final-averages-1-7-million-viewers/

296 Virginia Tech. (2024). Peck rips grand slam to give hokies 9-5 lead, before play was suspended in top of the seventh. Retrieved from https://hokiesports.com/news/2024/02/10/peck-rips-grand-slam

-to-give-hokies-9-5-lead-before-play-was-suspended-in-top-of-the-seventh

299 Wackerly, D. D., Mendenhall III, W., & Scheaffer, R. (2008). Mathematical statistics with applications.

Thomson.
