<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2024/2024 - Estimating NBA Team Shot Selection Efficiency from Aggregations of True, Continuous Shot Charts A Generalized Additive Model Approach - Unknown Authors.pdf -->

# **Estimating NBA Team Shot Selection Efficiency from Aggregations of True, Continuous Shot Charts: A Generalized Additive Model Approach** 

### Basketball 193942 

GAM dashboard: https://sportdataviz.syr.edu/TrueShotChart/ 

- - - Open-Source Code Repository: <u>https://github.com/Syracuse University Sport Analytics/continous_shot_selection</u> 

## **<mark>1. Introduction</mark>** 

<mark>We develop a novel type of basketball shot chart that uses a generalized additive model to estimate total shot proficiency continuously in the half-court. This shot chart incorporates missed shots that draw a shooting foul, and shot-pursuant free throw scoring, to determine total or true scoring yield following a shot decision. A</mark> traditional discrete, or binned, shot chart is a size- and color-coded spatial plot that tracks both location-dependent volume and points yielded from the floor, respectively, on field goal attempts (FGAs). Shot charts provide distilled summaries of shotdistributional efficiency and are therefore a leading analytic tool for team game-planning (see, e.g., Papalexakis and Pelechrinis 2018; Jiao, Hu, and Yan 2021; <mark>Jieying, Guanyu, and Jun 2021</mark> ; <mark>Franks, Miller, Bornn, and Goldsberry 2015</mark> ; <mark>Fichman and O’Brien 2019</mark> ; <mark>Skinner and Goldman 2015; Goldman and Rao 2011; Narayan 2019</mark> ; <mark>Winston, Nestler, and Pelechrinis 2022).</mark> While descriptive, traditional shot charts do not account for free throw scoring pursuant to shots from the field, nor the locations of those shots from the field that lead to the free throw scoring opportunities. By considering missed shots that result in a shooting foul, which are not considered FGAs, and made shots that result in an “and-one” free throw opportunity, we correct for location-conditional scoring yield estimate distortions in traditional shot charts. 

<mark>Despite their limitations, traditional shot charts have been integral to improving shooting efficiency in the NBA.</mark> In a 2020 NPR interview, Kirk Goldsberry, a basketball shot chart pioneer, discussed the ability to infer disequilibria from shot chart aggregations: “It's that wild margin of inefficiency that’s driven sort of these cartoonish trends and the rapid increase in 3-point shooting across the NBA.” Shot charts, and their aggregations, have served as a key input in the NBA’s three-point revolution. Figures 1a-b show the increased reliance on three-point shooting in the NBA during the past decade, which has allowed teams to further leverage efficiency gains from the three-point premium. The righthand side plot of Figure 1 shows the time trend in average number of three-point attempts (3PAs) per NBA team-game. We observe a marked increase in the locally upward slope of the trend beginning in 2013-14, coinciding with the ubiquitous adoption of SportVU player tracking technology in all NBA arenas. The only precedent for such a steep rise in 3PA volume occurred from 1994 through 1997, when the three-point line was moved inward “above the break” from 23.75 feet to 22 feet before being restored to its previous location. These negating leaguewide three-point line position changes account for the locally steep rise-and-fall pattern of the mid-1990s. The lefthand 



1 

side plot of Figure 1 features team-game level three-point attempt distributions for the 1980, 1985, 1990,…, and 2020 seasons (i.e., at five-year staggers).  This plot also demonstrates marked rightward shifts in the team-game level 3PA density plots of 2015 and 2020 relative to earlier such plots. 

**Figure 1a and 1b: NBA 3-Point Shots Taken Per Team-Game, Time Trend and Density** Plots 



## **<mark>2. Shot Charts with Spatial Continuity and True Estimates of Point Yield</mark>** 

<mark>Shot charts help us understand trends in shot selection and the efficiency therefrom.  To obtain a full picture of shot efficiency, however, we must consider all scoring pursuant to a given shot. Herein, we overcome limitations of previous shot chart types by developing a generalized additive model (GAM) continuous shot chart that accounts for all shot-pursuant free throw scoring. A GAM is a type of generalized linear model, where the outcome variable depends linearly upon smooth functions of the explanatory variables.  In fitting a generalized additive model, these smooth functions are estimated. A GAM shot chart allows for the estimation of player or team shot efficiency as a continuous, three-dimensional surface, where the third dimension is represented not by the physical height of a surface at a particular (x,y) coordinate but via continuous color-coding. Hastie and Tibshirani (1987) first developed GAMs to serve as a flexible and interpretable family of non-linear models.</mark> 

<mark>We call the GAM shot charts developed herein C</mark> _<mark>ontinuous True Shot Charts</mark>_ <mark>and make them available on a custom, searchable project dashboard at</mark> <u><mark>https://sportdataviz.syr.edu/TrueShotChart.</mark></u> <mark>- - - The project Github repository is available at: https://github.com/Syracuse</mark> <u><mark>University Sport Analytics/continous_shot_selection. Figure 2 shows a</mark></u> _<mark>Continuous True Shot Chart</mark>_ <mark>for the 2021-22 Milwaukee Bucks. In a</mark> _<mark>Continuous True Shot Chart</mark>_ <mark>, expected true point yield, from the field and line, for each possible shot location of the half-court, is estimated, and the estimate is color-coded into</mark> 



2 

<mark>the chart. Yellow ridge curves represent iso-yield curves or spatial level sets on yield such that shots along a given set generate equal expected true points.</mark> 



<!-- Start of picture text -->
Figure 2: Continuous True Shot Chart, 2021-22 Milwaukee Bucks<br><!-- End of picture text -->

<mark>The present work represents the first example of a continuous (GAM-based) true shot chart, to the authors’ best knowledge. When examining the 2021-22 Milwaukee Bucks’</mark> _<mark>Continuous True Shot Chart</mark>_ <mark>of Figure 2, we observe some surprises and some expected results. When including shotpursuant free throw scoring, we find the expected result that the Bucks scored proficiently at or near the rim, as well as from the wing three-point region extended and the left corner three-point area. However, we also find the surprising result that, for the Bucks of that season, long 2PAs were not nearly as low yielding as the conventional wisdom would suggest. The black far-midrange regions suggest that long 2PAs along the baseline extended were higher yielding than either close midrange shots in the paint or midrange shots off the elbows. Even more surprisingly, long 2PAs just inside the left three-point line break provided the Bucks with substantial yield (greater than 1.2 points per shot!). The 2021-22 Bucks obtained elite yield from a long 2PA region of the floor but middling yield for much of the near-midrange paint region. Further, the Bucks obtained elite scoring yield on 3PAs in some regions out to perhaps 26 feet, indicating that deep-threat 3PAs can have substantial scoring benefits in addition to the spacing benefits they afford an offense. However, any efficient scoring benefits of deep 3PAs fell off sharply beyond ~26 feet.</mark> 



3 

<mark>At its limit, a modern shot chart reduces a team’s shooting regions down to 3PAs and 2PAs at or near the rim. When considering shot-pursuant free-throw scoring, we observe that these distilled areas are important but that there are potentially glaring exceptions to such reductionism. In Figure 3, we consider James Harden’s 2019-20 shot chart. We chose this player-season for several reasons. This was Harden’s last year in Houston, where he was the on-court leader of a revolution in shot chart reductionism, Daryl Morey having been the accompanying front office leader of said revolution. Further, Harden won his third consecutive scoring title that season. Lastly, Harden has an exceptionally high free throw rate such that we expect a great deal of additional information in his true shot chart. In that season, Harden’s FT rate (FTA/FGA) was 0.557 or about 2.14 times the league average of 0.26. We then consider the 2022-23 shot chart of Jimmy Butler in Figure 4. We select Butler’s shot chart because he also has an all-time FT rate, especially among fellow Small Forwards. In fact, the present authors cannot find a Small Forward with a higher seasonal FT rate than Butler. His FT rate has been as high as 0.709 for a season and was 0.625 in 2022-23. As such, we also expect Butler’s true shot charts to look substantially different than his traditional chart.</mark> 



<!-- Start of picture text -->
Figure 3: 2019-20 Continuous True Shot Chart of James Harden<br><!-- End of picture text -->



4 



<!-- Start of picture text -->
Figure 4: 2022-23 Continuous True Shot Chart of Jimmy Butler<br><!-- End of picture text -->

<mark>Figures 3-4 have rich commonalities and differences. Buoyed by prolific free throw activity, both charts feature the expected hot spots in parts of the three-point region, as well as at or near the rim. However, some aspects of these shot charts reinforce surprises from the previous chart of Figure 2. We observe areas of premium yield along the baseline extended long 2PA regions for Harden; these same areas are of moderate yield for Butler, rather than low. As in the case of Figure 2, we observe that premium long 2PA regions exist in the modern NBA shot chart when accounting for shotpursuant FT scoring.</mark> 

<mark>For the 2021-22 Bucks again, Figure 5 presents a differential shot chart that visualizes the difference, from each point in the half court, between the color coding, or yield, of the</mark> _<mark>Continuous True Shot Chart</mark>_ <mark>and that of a conventional shot chart that does not include shot-pursuant FT scoring.</mark> 



5 

**<mark>Figure 5: Differential Shot Chart, Continuous True Shot Chart Yield minus Continuous Conventional Shot Chart Yield, 2021-22 Milwaukee Bucks</mark>** 



<mark>We observe from Figure 5 that failing to include shot-pursuant FT scoring places a substantial, and typically downward, bias on the estimated yield of shots near the basket. In general, the differential is variable across the floor, suggesting a variable underlying shot position conditional FT rate. Thus, traditional shot charts can substantially distort spatial characterizations of scoring yield. These same results bear out for many other team seasons, as can be observed on our custom shot chart dashboard at https://sportdataviz.syr.edu/TrueShotChart/. Figure 5 also</mark> _<mark>explains</mark>_ <mark>the unexpected result that, in a true shot chart, shots from the left baseline extended long 2PA region generated a high yield for the 2021-22 Bucks. Shots from this region generated a high made FT rate. It can be observed on the dashboard that James Harden’s 2019-20 yield premium from this region also partly depended on a relatively high made FT rate for shots in that region.</mark> 

<mark>Though largely reviled in the modern era of basketball analytics, long 2PAs in some cases generate a high true scoring yield. In fact, we observe from Figure 2 that long 2PAs from this region for the 2021-22 Bucks returned a similar point yield, on average, than if the player had stepped back to the adjacent three-point range! In this case, a comparison of Figures 2 and 5 suggests that the step-back 3PA garnered more points from the field but fewer points from the line. In consideration of the latter effect, step-backs may discourage defenders from fouling because a foul on a missed 3PA allows the offense 50% more points, in expectation, than fouling on a missed 2PA. Assuming league average FT proficiency, a missed 3PA that draws a shooting foul would garner an expected</mark> 

<mark>points, whereas a missed 2PA that draws a shooting foul would garner an expected points. This premium is certainly not commensurate with any three-point premium that exists in the absence of a shooting foul, as we will observe later in the paper. Therefore, fouling</mark> 



6 

<mark>on a 3PA disproportionately punishes the defense. This calculus likely explains at least part of the lower FT rate on 3PAs in Figure 5, as well as the lack of a sharp efficiency distinction between certain 3PAs and their neighboring long 2PAs. In the subsequent section, we aggregate</mark> _<mark>Continuous True Shot Charts</mark>_ <mark>to determine whether results such as this suggest an erosion of the three-point premium in recent NBA seasons.</mark> 

## **<mark>3. Assessing Shot Selection Efficiency from Continuous True Shot Charts</mark>** 

<mark>Another issue surrounding conventional shot chart analysis is the lack of a comprehensive measure by which to summarize a shot chart in terms of shot selection efficiency. The present work therefore further develops a shot selection measure called</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>that takes as input a player’s or team’s expected true points and expected proportional volume from a simulated grid of shots attempted somewhere on the half court and computes the player’s or team’s spatial Pearson correlation between expected proportional volume and expected true points, from the field and free throw line, across the half court.</mark> 

<mark>This represents a measure of a player’s or team’s shot selection efficiency. The measure does not depend on overall shooting ability but, rather, on how proficient a player or team is in shooting from hot spots and avoiding cold spots on the floor, while taking into account shot location conditional free throw scoring rate. A separate measure of</mark> _<mark>exogenous shooting ability</mark>_ <mark>is developed to estimate distinctly the average expected true points for a player (team) if they took a shot from every possible location on the shot chart with equal likelihood. As such, this latter variable estimates shooting ability but is exogenous of shot selection in that it weights each shot location equally. With this control measure, we are subsequently able to validate the statistical contribution or marginal effect of</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>to a basketball offense while controlling out the effect of</mark> _<mark>exogenous shooting ability</mark>_ <mark>. We validate the</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>measure by specifying an XGBoost model, as well as linear, fixed effects regression models, at the team-season level that estimate Pythagorean expected win percentage conditional on a set of variables that survived a Variance Inflation Factor variable-paring model specification approach to limit multicollinearity. These include</mark> _<mark>exogenous shooting ability, defensive rating (DRtg), own turnover rate (TOV%), offensive rebounding rate (ORB%), team fixed effects</mark>_ <mark>,</mark> _<mark>Normalized Payroll</mark>_ <mark>, and</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>. It stands to reason that these specific control variables survived VIF-paring. They encompass the non-shooting offensive four factors (i.e., the offensive four factors not related to shot selection efficiency or shooting ability) and the team’s overall defensive effectiveness in that season.  Table 1 summarizes the dependent and independent variables of the study.</mark> 



7 

**Table 1: Feature Summary Statistics (n=210)** 

|**Characteristic**|**Median (SD) Range**|
|---|---|
|Pyth.W.proportion|0.50 (0.14) 0.18 - 0.82|
|W.proportion|0.50 (0.14) 0.18 - 0.82|
|Net.Rating|0.40 (4.6) -10.5 - 11.6|
|Shot.selection.efficiency|0.27 (0.06) 0.01 - 0.44|
|Exogenous.shooting.ability|0.88 (0.05) 0.76 - 1.03|
|TOV%|12.60 (0.90) 9.90 - 14.90|
|ORB%|22.80 (2.21) 17.90 - 30.20|
|DRtg|111.2 (3.3) 102.9 - 120.0|
|Payroll (millions $)|123.57 (22.32) 79.18 - 192.91|
|Normalized.Payroll|-0.02 (0.99) -2.93 - 2.59|



_<mark>Payroll normalized</mark>_ <mark>represents a team’s payroll in z-score terms, with respect to the distribution of NBA team payrolls in that season.</mark> _<mark>Net Rating</mark>_ <mark>is a team’s average scoring margin per 100 possessions, which approximates the average possessions per game in the 2022-23 NBA season. In 2022-23, the average points per NBA game was 114.7, and the average points per 100 NBA possessions was 114.8. Therefore, average possessions per game in that season was (114.7/114.8) or about 99.9.  This value has been converging upward throughout the course of the NBA playertracking movement, which has largely emphasized quick sets involving ball-movement, quicklydeveloping isolation plays, and pull-up 3PAs over slow sets involving foot-movement, slowlydeveloping isolation plays, and fewer pull-up 3PAs. Interestingly, rate stats for the NBA have been measured in</mark> _<mark>per 100 possession</mark>_ <mark>terms for decades, and the NBA’s analytic movement, which has greatly propelled the prominence of these rate stats, has helped to converge these</mark> _<mark>per 100 possession</mark>_ <mark>stats to the magnitude of</mark> _<mark>per game</mark>_ <mark>stats on league average. At least for the time being, this creates the advantage of less currency exchange in dealing with these two levels of statistics. In analyzing league-wide data for 2022-23, the choice of per game or per 100 possession stats is almost immaterial (material only at a margin of error less than 0.1%).</mark> 

<mark>The median value for</mark> _<mark>Exogenous Shooting Ability</mark>_ <mark>is 0.88, which matches the sample mean for this variable. This is interpreted as median true points per shot for a team that randomly selects shot locations, with equal likelihood, from across its shot chart. One might think of this team as one that plays “hot potato” on offense or one programmed to get the ball to any point in the half court with equal likelihood and then shoot. As mean and median are equal for this variable, such a team is expected to score 0.88 true points per shot compared to the observed sample average true points per shot of 1.13. We can meaningfully difference these two values to estimate that the net value of shot selection, on league average, in our sample is approximately a quarter of a point per shot taken.</mark> 



8 

<mark>All teams in the sample exhibit a positive</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>value. Recall that this variable represents the Pearson correlation between shot volume and true scoring from a grid of shot locations across the floor. The median value is 0.27, suggesting that the typical NBA team is mildlyto-moderately effective in identifying hot spots and avoiding cold spots in shot selection.  The minimum observed value is 0.01, suggesting there was a team in a season (the 2017-18 Portland Trail Blazers) that had essentially no correlation between shot volume and true scoring in its shot selection across the floor! Luckily for that team, it had a high exogenous shooting ability such that their overall offense was effective. The maximum</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>was 0.44 and was set by the 2021-22 Boston Celtics, a team well-known for analytically-driven sets and shot selection. Another descriptive data summary question is whether the</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>has improved as we progress deeper into the analytic era of basketball. Figure 6 addresses this question with a time trend and embedded box plots for the variable by season.</mark> 

**<mark>Figure 6: Improvement of Shot Selection Efficiency over Time</mark>** 



<mark>In Figure 6, we observe a positive trend in expected team</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>over time. In 2016-17, the trend value was 0.23. By 2022-23, the trend value had risen to 0.32. With progressive advances in analytics, NBA offenses have improved in</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>over time. This trend result matches previous findings that offensive efficiency, and not defensive efficiency, is a leading indicator of analytic advances (see, e.g., Ehrlich and Sanders 2021). Having summarized the key model variables, a regression analysis will now estimate the respective marginal effects of</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>,</mark> _<mark>Exogenous Shooting Ability</mark>_ <mark>, and other variables upon team-season win performance and net rating. Equations 1-3 provide the three primary model specifications.</mark> 



9 

<mark>Equation 1-3 for Win Production Models</mark> 



<mark>Model 1 estimates</mark> _<mark>Pythagorean Expected Win Proportion</mark>_ <mark>for a team in a season as a function of the team’s shot selection efficiency, exogenous shooting ability, and a vector of control variables in that season. Our Pythagorean exponent for the model is 14, updating from similar earlier estimates, e.g., by Morey (1993), such that a team’s Pythagorean Expected Win Proportion in a season is given as</mark> 

!"#$!" !"#$!"%&"#$!" ~~.~~ Model 2 features the same righthand side but with each team’s (actual) _Win_ _<mark>Proportion</mark>_ <mark>as the dependent variable, while Model 3 substitutes</mark> _<mark>Net Rating</mark>_ <mark>as the dependent variable. Results for the models are given In Table 2 as follows.</mark> 

#### **<mark>Table 2: Shot</mark>** **<u><mark>Selection Efficiency Effect on Win Performance Models</mark></u>** 

|_Predictors_|**Pyth W**<br>_Estimates_|**Prop**<br>_std._<br>_Error_|**ortion**<br>_p_|**W P**<br>_Estimates_|**roport**<br>_std._<br>_Error_|**ion**<br>_P_|_Estimates_|**NetRtg**<br> <br>_std._<br>_Error_|<br>_p_|
|---|---|---|---|---|---|---|---|---|---|
|(Intercept)|2.218|0.224|**<0.001**|2.097|0.249|**<0.001**|55.099|7.041|**<0.001**|
|DRtg|-0.028|0.002|**<0.001**|-0.027|0.002|**<0.001**|-0.945|0.049|**<0.001**|
|gam shot<br>selection<br>efficiency|0.400|0.086|**<0.001**|0.334|0.095|**0.001**|14.149|2.691|**<0.001**|
|exogenous<br>shooting<br>ability|1.307|0.107|**<0.001**|1.393|0.119|**<0.001**|49.073|3.355|**<0.001**|
|off TOV%|-0.025|0.006|**<0.001**|-0.021|0.007|**0.001**|-0.791|0.185|**<0.001**|
|off ORB%|0.018|0.002|**<0.001**|0.016|0.003|**<0.001**|0.535|0.073|**<0.001**|
|Observations|210|||210|||210|||
|R<sup>2</sup>/ R<sup>2</sup><br>adjusted|0.719 / 0|.712||0.672 / 0|.664||0.757 / 0|.75||





<mark>The regression data constitutes every NBA team-season from 2016-17 through 2022-23 (30 teams multiplied by 7 years).</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>has a positive and highly-significant conditional effect on</mark> _<mark>Pythagorean Expected Win Proportion</mark>_ <mark>,</mark> _<mark>Win Proportion</mark>_ <mark>, and</mark> _<mark>Net Rating</mark>_ <mark>. If an NBA team in a</mark> 



10 

<mark>season can improve its weighted correlation between shot-volume and expected true points by 0.1 units, it gains an expected 0.04 units of win proportion or about 3.28 additional wins per 82-game regular season, according to the</mark> _<mark>Pythagorean Expected Win Proportion</mark>_ <mark>model. In other words, a team’s expected regular season win count increases by 1 for roughly every 0.03 units of increase in the spatial Pearson correlation between shot-volume and expected true points. To rephrase once more, a standard deviation increase in</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>yields the expectation of a 0.17 standard deviation increase in</mark> _<mark>Pythagorean Expected Win Proportion</mark>_ <mark>, which suggests that variation in shot selection efficiency is a primary driver of winning in the NBA. From Model 3, we find that if an NBA team in a season can improve</mark> _<mark>Shot Selection Efficiency</mark>_ <mark>by 0.1 units, it gains an expected 1.41 points in terms of average game-level score margin (</mark> _<mark>Net Rating</mark>_ <mark>).</mark> 

_<mark>Exogenous Shooting Ability</mark>_ <mark>is also significant and substantial in explaining team performance, as are the other factor-type control variables. These results are both highly significant and substantial. Further, shot selection gains do not necessarily require a costly roster overhaul. In principle at least, shot selection efficiency is something that can be taught to players. We next examine whether subsequent regressions will determine whether shot selection efficiency is a “moneyball,” or inefficiently-priced source of wins. The three models feature strong explanatory power (𝑅</mark> ' <mark>between 0.672 and 0.757).</mark> 

## **4. Is Shot Selection Efficiency Money(ball)?** 

Another model was estimated to consider the payroll-conditional effect of _Shot Selection Efficiency_ on team success by adding the features _Normalized Payroll_ and _Normalized Payroll Squared_ to Model 1.  As stated, the _Normalized Payroll_ feature is the raw payroll standardized (center and scale) by season, which is calculated by subtracting the mean of payroll and then dividing by the standard deviation. We also included a _Normalized Payroll Squared_ feature to allow for a possible quadratic payroll effect (due, e.g., to the possibility of some large-market teams being managerially inefficient). Table 3 models represent payroll-augmented linear and quadratic versions of Model 1. 



11 

#### **<u>Table 3: Moneyball Shot Selection Efficiency Opportunity</u>** 

||**Pyth**|**W Propo**|**rtion**|**Pyth**|**W Propo**|**rtion**|
|---|---|---|---|---|---|---|
|_Predictors_|_Estimates_|_std. Error_|<br>_P_|_Estimates_|_std. Error_|<br>_P_|
|(Intercept)|2.218|0.224|**<0.001**|2.143|0.221|**<0.001**|
|DRtg|-0.028|0.002|**<0.001**|-0.026|0.002|**<0.001**|
|gam shot selection<br>efficiency|0.400|0.086|**<0.001**|0.379|0.084|**<0.001**|
|exogenous shooting<br>ability|1.307|0.107|**<0.001**|1.195|0.111|**<0.001**|
|off TOV%|-0.025|0.006|**<0.001**|-0.023|0.006|**<0.001**|
|off ORB%|0.018|0.002|**<0.001**|0.018|0.002|**<0.001**|
|normalized payroll||||0.018|0.006|**0.002**|
|normalized payroll sq.||||-0.003|0.003|0.336|
|Observations|210|||210|||
|R<sup>2</sup>/ R<sup>2</sup>adjusted|0.719 / 0|.712||0.733 / 0|.724||



__________________ 

Payroll is significantly productive of expected wins in both models.  Further, the quadratic term on _Normalized Payroll_ is negative but insignificant in Model 2. The _in-sample_ relationship between payroll and expected wins is quadratic (inverted-U), but the coefficient on the quadratic payroll term is insignificant. Even conditional on payroll, _Shot Selection Efficiency_ is positive and significant, indicating that the win productivity of _Shot Selection Efficiency_ is not explained by variation in team-season payroll. This may suggest either that players have different observed levels of _Shot Selection Efficiency_ but that the player labor market is not valuing higher levels of the attribute or that team coaching and analytic staffs (i.e., team culture and values) are largely responsible for variation in team _Shot Selection Efficiency_ . In either case, _Shot Selection Efficiency_ is a “moneyball” or supra-payroll source of wins in the NBA. The magnitude of the coefficient for _Shot Selection Efficiency_ remains essentially the same when we control for team-season payroll.  This suggests that the NBA player labor market is essentially not pricing in any variation in _Shot Selection Efficiency_ observed at the player level. Rather, this variation is driven by team coaching/analytics. 

## **5. Robustness Check of Shot Selection Efficiency using XGBoost** 

To robustness check our linear, fixed effect model results, we fit an XGBoost model (Liu and Lust, 2020) to understand how _Shot Selection Efficiency_ , along with other covariates, relate to _Pythagorean Expected Win Proportion_ . The covariates of interest include _Normalized Payroll, DRtg, ORB%, TOV%, Exogenous Shooting Ability_ , and _Season_ . We partitioned 90% of the data into a training set and 10% into a test set. The out-of-sample mean absolute error was 0.052 and the out 



12 

of sample R-squared was 0.625, comparable to that observed in the linear, fixed effects models. For the full model, the mean absolute error was 0.0004, and the R-squared was 0.999989. Also, Shapley Additive exPlanations (SHAP) (Lundberg and Lee, 2017) values were calculated. Figure 7 shows a beeswarm summary plot, which demonstrates the estimated effect of each parameter on expected wins. 

**Figure 7: Beeswarm Summary Plot** 



_Shot Selection Efficiency_ has a positive estimated Shapley Value such that the XGBoost results are consistent with those of the linear, fixed effects models. Two SHAP dependency plots were also rendered, where each shows estimated marginal effect that each feature has on Pythagorean Expected Win Proportion. Figure 8 demonstrates the monotonically positive impact that _Shot Selection Efficiency_ has on _Pythagorean Expected Win Proportion_ . This confirms that shot selection efficiency is indeed important to team performance. For teams with a _Shot Selection Efficiency_ greater than 0.23, shot selection positively contributed toward winning, according to Figure 8. 



13 

##### **Figure 8: Shot Selection Efficiency Effect on Pythagorean Wins** 



##### **Figure 9: Payroll Effect on Pythagorean Wins** 



## **6. Does an NBA 3PA Premium Remain according to Aggregations of True Shot Charts?** 

By accounting for FT scoring, _Continuous True Shot Charts_ can comprehensively address many fundamental questions in basketball, such as: _Does a three-point premium still exist in the NBA given the escalation in three-point attempt volume_ ? See, for example, Ehrlich and Sanders (2021), who develop the first discrete, true shot chart to find evidence that the three-point premium eroded to 



14 

some degree during the 2010s. While aggregations of _conventional_ shot charts suggest the threepoint yield premium remains intact for the NBA, what happens when we consider shot-pursuant FT scoring for recent seasons? 

To consider this question, we aggregate both Continuous True Shot Charts and traditional shot charts for all NBA shots taken in each season from 2016-17 through 2021-22. Doing so allows us to estimate the three-point premium, with and without shot-pursuant free throw scoring in each season. Figure 10 reports those results, where the red trend line is estimated from aggregations of traditional shot charts and therefore reports the estimated difference between 3PA and 2PA yield when not considering shot-pursuant FTAs. The blue line is estimated from aggregations of Continuous True Shot Charts and therefore reports the estimated difference between 3PA and 2PA yield when considering shot-pursuant FTAs. 

#### **Figures 10: NBA Three-Point Premium, 2016-17 – 2021-22: A Tale of Two Shot Charts** 



Observing the red trend line, we find a significant and fairly substantial leaguewide three-point _premium_ that existed from 2016-17 through 2020-21 when considering aggregations of _traditional_ shot charts. That is, NBA players scored significantly more proficiently _from the field_ on three-point attempts than on two-point attempts from 2016-17 through 2020-21.  In magnitude, this premium ranged between 0.025 and 0.064 points per three-point shot over these years.  In 2021-22, there was no significant leaguewide three-point premium or dispremium when considering aggregations of _traditional_ shot charts.  However, when considering aggregations of _true shot charts_ , we find a significant and deepening three-point _dispremium_ at the league level since the 2018-19 season! In 2021-22, this dispremium swelled to -0.066 points per three-point shot or roughly a point less for each 15 three-point shots.  Despite these findings, we observe that leaguewide three-point shot volume has continued to rise dramatically.  It appears as though the typical team continued to follow _perceived_ three-point premia from aggregations of traditional shot charts rather than 



15 

significant dispremia from aggregations of _true shot charts_ . In the case of 3PA volume, there is evidence that NBA teams overshot their market, assisted by a mis-specified analytic tool in the form of traditional shot charts. 

## **<mark>7. Conclusion</mark>** 

<mark>In this work, we have developed a set of novel GAM-estimated, Continuous True Shot Charts for NBA teams and players and have demonstrated that they correct distortions in scoring yield estimates found in traditional shot charts. They do so by including shot-pursuant FT scoring into the color coding (scoring yield estimate) of the chart at all locations. We further construct a measure of team shot selection efficiency as a means to summarize team and player shot charts in terms of efficiency.  This measure represents the Pearson correlation between expected proportional volume and expected true points, from the field and free throw line, across the half court. Through linear, polynomial, and XGBoost modeling, we find that shot selection efficiency contributes to team expected win proportion significantly and substantially.  Further, shot selection efficiency is found to be a “moneyball” or supra-payroll source of wins in the NBA. Lastly, we use Continuous True Shot Charts to find that there has been a widening NBA three-point dispremium since 2018-19.  This dispremium result is not available if one aggregates from traditional shot charts, which do not consider shot-pursuant FT scoring. Continuous True Shot Charts are both novel and meaningful in basketball league settings.</mark> 

## **8. References** 

<mark>Ehrlich, J. A., Ghimire, S., Sadler, T. R., & Sanders, S. D. (2022). Policy and Policy Response on the Court: A Theoretical and Empirical Examination of the Three-Point Line Extension in Basketball.</mark> _<mark>Journal of Sports Economics</mark>_ <mark>, 15270025221111790.</mark> 

- <mark>Fichman, M., & O’Brien, J. R. (2019). Optimal shot selection strategies for the NBA.</mark> _<mark>Journal of Quantitative Analysis in Sports</mark>_ <mark>,</mark> _<mark>15</mark>_ <mark>(3), 203-211.</mark> 

<mark>Franks, A., Miller, A., Bornn, L., & Goldsberry, K. (2015, February). Counterpoints: Advanced</mark> 

- <mark>defensive metrics for NBA basketball. In</mark> _<mark>9th Annual MIT Sloan Sports Analytics Conference, Boston, MA</mark>_ <mark>.</mark> 

<mark>Goldman, M., & Rao, J. M. (2011, March). Allocative and dynamic efficiency in NBA decision making. In</mark> _<mark>In Proceedings of the MIT Sloan Sports Analytics Conference</mark>_ <mark>(pp. 4-5).</mark> 

<mark>Goldsberry, K. (2019).</mark> _<mark>Sprawlball: A visual tour of the new era of the NBA</mark>_ <mark>. Mariner Books.</mark> Hastie, T., & Tibshirani, R. (1987). Generalized additive models: some applications. _Journal of the American Statistical Association_ , _82_ (398), 371-386. 

<mark>Jiao, J., Hu, G., & Yan, J. (2021). A Bayesian marked spatial point processes model for basketball shot chart.</mark> _<mark>Journal of Quantitative Analysis in Sports</mark>_ <mark>,</mark> _<mark>17</mark>_ <mark>(2), 77-90.</mark> 

<mark>Jieying, J., Guanyu, H., & Jun, Y. (2021). A Bayesian marked spatial point processes model for basketball shot chart.</mark> _<mark>Journal of Quantitative Analysis in Sports</mark>_ <mark>,</mark> _<mark>17</mark>_ <mark>(2), 77-90.</mark> 

- <mark>Lundberg, S. M., & Lee, S.-I. (2017).</mark> _<mark>A Unified Approach to Interpreting Model Predictions</mark>_ <mark>. https://arxiv.org/abs/1705.07874</mark> 

- <mark>Massey, C., & Thaler, R. H. (2013). The loser's curse: Decision making and market efficiency in the National Football League draft.</mark> _<mark>Management Science</mark>_ <mark>,</mark> _<mark>59</mark>_ <mark>(7), 1479-1495.</mark> 

- Morey, D. 1993. “STATS Basketball Scoreboard.” Pp. 1–288 in STATS Basketball Scoreboard, edited by J. Dewan and D. Sminda. New York: STATS, Inc. 



16 

- <mark>Narayan, S. (2019).</mark> _<mark>Applications of machine learning: basketball strategy</mark>_ <mark>(Doctoral dissertation, Massachusetts Institute of Technology).</mark> 

- <mark>NBA. (2022). Example Shot Chart. Available Online at:</mark> 

   - <mark>https://www.nba.com/stats/events/?flag=3&CFID=33&CFPARAMS=2021-</mark> 

- <mark>22&PlayerID=201939&ContextMeasure=FGA&Season=2021-22&section=player&sct=hex NPR (2020). The Science of Hoops. Available online at:</mark> 

   - <mark>https://www.npr.org/transcripts/911898347</mark> 

- <mark>Otto, C. A., & Volpin, P. F. (2018). Marking to market and inefficient investment decisions.</mark> _<mark>Management Science</mark>_ <mark>,</mark> _<mark>64</mark>_ <mark>(8), 3756-3771.</mark> 

- <mark>Papalexakis, E., & Pelechrinis, K. (2018, October). thoops: A multi-aspect analytical framework for spatio-temporal basketball data. In</mark> _<mark>Proceedings of the 27th ACM International Conference on Information and Knowledge Management</mark>_ <mark>(pp. 2223-2232).</mark> 

- <mark>Piette, J., Anand, S., & Zhang, K. (2010). Scoring and shooting abilities of NBA players.</mark> _<mark>Journal of Quantitative Analysis in Sports</mark>_ <mark>,</mark> _<mark>6</mark>_ <mark>(1).</mark> 

- <mark>Reich, B. J., Hodges, J. S., Carlin, B. P., & Reich, A. M. (2006). A spatial analysis of basketball shot chart data.</mark> _<mark>The American Statistician</mark>_ <mark>,</mark> _<mark>60</mark>_ <mark>(1), 3-12.</mark> 

- <mark>Romer, D. (2006). Do firms maximize? Evidence from professional football.</mark> _<mark>Journal of Political Economy</mark>_ <mark>,</mark> _<mark>114</mark>_ <mark>(2), 340-365.</mark> 

- Sandholtz, N., Mortensen, J., Bornn, L. (2019) Chuckers: Measuring Lineup Shot Distribution Optimality Using Spatial Allocative Efficiency Models Sloan Sports Analytics Conference 2019. 

- <mark>Santos-Fernandez, E., Denti, F., Mengersen, K., & Mira, A. (2022). The role of intrinsic dimension in high-resolution player tracking data—Insights in basketball.</mark> _<mark>The Annals of Applied Statistics</mark>_ <mark>,</mark> _<mark>16</mark>_ <mark>(1), 326-348.</mark> 

- <mark>Skinner, B., & Goldman, M. (2015). Optimal strategy in basketball.</mark> _<mark>arXiv preprint arXiv:1512.05652</mark>_ <mark>.</mark> 

- <mark>Winston, W. L., Nestler, S., & Pelechrinis, K. (2022). 37. SportVU, Second Spectrum, and the Spatial Basketball Data Revolution. In</mark> _<mark>Mathletics</mark>_ <mark>(pp. 321-340). Princeton University Press.</mark> 

- <mark>Yang Liu and Allan Just (2020). SHAPforxgboost: SHAP Plots for 'XGBoost'. R package version 1.7.5.1. https://github.com/liuyanguu/SHAPforxgboost/</mark> 



17 


