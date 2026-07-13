<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - Estimating (four) Factor Values inthe NBA A Seemingly Unrelated Regression Analysis - Unknown Authors.pdf -->

**_Jonathan Bosch_** Estimating (Four) Factor Values in the NBA: **_Dax Speakman Dr. Shane Sanders_** A Seemingly Unrelated Regression Analysis 





<!-- Start of picture text -->
Effective Field Goal<br>•<br>Percentage (eFG%)ge (eFG%)e (eFG%)(eFG%)eFG%))<br>Turnover Rate (TOV%) •<br>Rebounding Rate<br>(TRB%)TRB%))<br>Free Throw Rate (FTr)<br><!-- End of picture text -->

<u><mark>Background</mark></u> <sup>1</sup> Dean Oliver’s Four Factors of Basketball Success: **Effective Field Goal Percentage (eFG%)ge (eFG%)e (eFG%)(eFG%)eFG%)) Turnover Rate (TOV%)**  A unit improvement in an offensive factor is equal **Rebounding Rate** to a defensive factor unit improvement (in terms of **<u>(TRB%)TRB%))</u>** score margin implication) **Free Throw Rate (FTr)** 





<!-- Start of picture text -->
•<br>Normal distributions<br>•<br>Average (Salary) ~ RPM<br><!-- End of picture text -->

anticipated correlation not 

seen as an issue 

- <sup>2</sup> Research shows offensive factor improvements are 2.5 times more valuable than defensive factor improvements in the NBA free agent market. 

<mark>What is the worth of these factor differentials in free agency?</mark> 

 Sampled data into train (80%) & test (20%) sets 

- **Can we find a difference in the NBA free agency market valuation of the factors such that a win-maximizing team can exploit?** 

 We want to estimate the following two equations in order to: 

- Can players whose win value arise from relatively expensive factors be shed, in favor of those whose win value arise from relatively inexpensive factors? <u><mark>Data</mark></u> 

- a)Estimate the weights in which our four factor differentials compute to RPM b) Estimate the value (in salary) of one unit of RPM 



# 3 - <u>Contract details</u> 

- Player name, age, position, team (signed to), year (2014-2018), length of 



contract, yearly average salary 

   - Anticipate correlated errors between the two equation 

- 4 

- - <u>Player Stats</u> (from Year - 1) 

- - Player name, season (2013-2017), games, eFG%  TOV%  FTr (and for opponent), TRB% 

|%  FTr (and for|Chose to run the two regressions simultaneously||
|---|---|---|
||“systemfit” package - run seemingly unrelated regress<br>**RPM**<br>**Average Salary**|ion<sup>6 </sup>(SUR) in R|
||**RPM**<br>1.0<br>-0.048<br><br>The correlations|of the residuals after SUR analysis|
||**Average Salary**<br>-0.048<br>1.0||
||RPM<br>Averag|e Salary|
|*10.0643 is the average total rebounding<br>|Variable<br>Coefficient (β)<br>Variable|Coefficient (β)|
|rate in the NBA|Intercept<br>-1.140<br>Intercept|-13,207,208|
||eFGdiff<br>0.126<br>RPM|1,754,800**|
||TOVdiff<br>0.145<br>Age|-192,462*|
||FTrdiff<br>0.049<br>PG|-719,087|
||REBdiff<br>0.088<br>SG|455,403|
||SF<br>−All variables significant at 99% confidence|435,743|
||PF<br> <br>−RMSE: 2.1<br>|-1,470,012|
||−R-squared: 0.26||
||−* significant at 95%<br>−RMSE: 6,217,319<br> <br>We apply chain rule to calculate the|, ** significant at 99%|
||−R-squared: 0.35<br>following factor differential values:||



- - 

- <u>Real Plus Minus</u><sup>5</sup> (from Year - 1) 

   - 2013-2017 RPM 

   - Player name, season ( ), 

- Four Factors manipulation 

- - eFG difference =     eFG% - eFG% opponent 

- - TOV difference =     TOV% - TOV% opponent 

- - FTr difference =     FTr - FTr opponent 

- - REB difference =     TRB% - 10.0643 





<!-- Start of picture text -->
Exploratory Data Analysis<br><!-- End of picture text -->















<mark>How much are teams actually paying for factor differentials?</mark> 



|W|e compare th|ese coefficie|nts|Variable|Coefficient (β)|
|---|---|---|---|---|---|
|wi|th the factor d<br>we previous|ifferential va<br>ly calculated.|lues|Intercept<br>eFGdiff|4,205,598<br>195,351**|
|Factor|Market|Market|Percent|TOVdiff|280,772**|
|eFGdiff|Price<br>$195,000|Value<br>$221,000|Overpaid<br>-11.8 %<br>(underpaid)|FTrdiff<br>REBdiff<br>Age|182,468**<br>371,481**<br>-61,817|
|TOVdiff|$281,000|$254,000|10.6 %|PG|3,369,446|
|||||SG|2,608,987|
|FTrdiff|$182,000|$86,000|111.6 %|SF|3,827,043*|
|REBdiff|$371,000|$154,000|141.0 %|PF<br>−* significant at 95%<br>−RMSE: 6,903,649<br>−R-squared: 0.20|-418,686<br>, ** significant at 99%|



- <u><mark>Conclusions</mark></u> 

- Holding factor values constant, PF the cheapest on the FA market 

   - →Construct cheaper, role-players at the PF position 

- REB and FT factors are much more overpaid than EFG and TOV 

   - →EFG and TOV not salient because of opponent factor 

- PG strongly overpaid - better estimated by RPM 

- →Factors blame PG for TOV, but don’t credit for passing/playmaking <u><mark>Future Work</mark></u> 

- Similar analysis with 8 factors – break up the differentials 

   - →Is Offense or Defense driving these valuations? 

- 9 Factors – passing/playmaking component 

   - →Too important part of the game to ignore at the player level 

- <u><mark>References</mark></u> 

- 1. Oliver, Dean. Basketball on Paper: Rules and Tools for Performance Analysis. Potomac Books, Inc., 2011. 

- 2. Ehrlich, J., Sanders, S., & Boudreaux, C. J. (2019). The relative wages of offense and defense in the NBA: A setting for win-maximization arbitrage? Journal of Quantitative Analysis in Sports. https://doi.org/10.1515/jqas-2018-0095 

- 3. “NBA Contracts.” Spotrac.com, www.spotrac.com/nba/contracts/. 4. “NBA Player Stats.” NBA Stats, stats.nba.com/players/. 5. “ESPN RPM.” ESPN, ESPN Internet Ventures, 19 June 2019, www.espn.com/nba/statistics/rpm. 6. Perform Seemingly Unrelated Regression in R. UCLA: Statistical Consulting Group. from https://stats.idre.ucla.edu/r/faq/how-can-i-perform-seemingly-unrelated-regression-in-r/ <u><mark>Contact</mark></u> 

- jbosch@syr.edu djspeakm@syr.edu sdsander@syr.edu 

jbosch@syr.edu 

sdsander@syr.edu 


