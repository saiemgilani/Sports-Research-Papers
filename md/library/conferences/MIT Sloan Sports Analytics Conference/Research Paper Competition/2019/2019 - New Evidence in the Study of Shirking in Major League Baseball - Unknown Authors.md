<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2019/2019 - New Evidence in the Study of Shirking in Major League Baseball - Unknown Authors.pdf -->



# **New Evidence in the Study of Shirking in Major League Baseball** 

### Richard Paulsen<sup>1</sup> 

Baseball Track Paper ID 13244 

## **1. Introduction** 

The proper alignment of incentives in principal-agent relationships is a long-studied issue in the field of economics (Ross 1973; Holmstrom 1979). One relationship that has received attention is the relationship between employer (the principal) and employee (the agent). In this relationship, the employer is concerned with the potential for moral hazard to arise. Moral hazard may arise if the employee has job security, and subsequently exerts diminished effort, or shirks, and performs at a low level. Professional sports are an ideal environment to study this potential for shirking because players commonly have contracts with guaranteed salary, contract data is publicly available, and while effort is not directly observable, performance is. This paper will use variation in contract length in Major League Baseball (MLB) to study the relationship between player performance and years remaining on the player’s contract. 

As shirking in Major League Baseball has received some attention in the literature, it is important to call attention to this paper’s contributions. First, this paper will use a player fixed-effects estimation strategy to identify the impact of years remaining on a contract and player performance. A fundamental challenge in identifying the relationship between years remaining on a player’s contract and performance is that those players who receive multiyear contracts are of higher ability that those who do not. As ability is positively related to both contract length and performance, failing to control for this positive selection into multi-year contracts will cause the estimated coefficient in a regression of performance on years remaining to be upward biased. A player fixed-effects regression controls for innate ability by estimating a player-specific coefficient, controlling for time-invariant player characteristics. When estimating this coefficient, other time-varying player characteristics that affect player performance are held constant. Second, past literature has identified relationships between contract years remaining and decreased performance and argued this is due to shirking, without consideration of other potential explanations for this relationship. One alternative explanation is that a player entering into a new multi-year contract may join a new team, and subsequently face an adjustment process. Another 

1 Northeastern University Department of Economics, 301 Lake Hall, 360 Huntington Avenue, Boston, MA 02115. Phone: 315-525-6640. Email: Paulsen.ri@husky.neu.edu. 





2019 Research Papers Competition Presented by: 

1 



alternative explanation is that teams sign players to multi-year contracts if they believe the players are likely to improve over time, which would lead to a negative relationship between performance and contract years remaining even in a fixed-effects specification. This paper will address these alternative explanations and will present evidence that is consistent with the argument that the relationship is driven by player shirking. 

Shirking occurs when an employee exerts effort in an employer-employee relationship that is sub-optimal in the eyes of the employer. For such behavior to occur, the relationship must have certain characteristics. Effort improves production, but the relationship between effort and production is noisy. While production is observable, effort is not and is costly to monitor, and cannot be contracted upon. The employee must face a cost to exerting effort. If such characteristics exist, the employee may find it optimal to shirk (Holmstrom 1979). While the potential for shirking may arise in some number of employment relationships<sup>2</sup> , professional sports, and notably MLB, present settings that are ideal for trying to identify such behavior<sup>3</sup> . Players in MLB are typically signed to contracts that vary in length from one year to ten or more years. Due to the strength of the MLB Player’s Association, these contracts are essentially guaranteed<sup>4</sup> . Fixed-length multi-year contracts allow for the identification of shirking as player incentives vary throughout the duration of the contract. Assuming future employers place more weight on recent performance when hiring, when an employee is in a multi-year contract and anticipates signing a new contract at the end of the current contract, the employee has an incentive to shirk and exert low effort at the start of the contract but increase levels of effort as the contract approaches its end (Cantor 1988). 

> 2 Tenure for school teachers and college professors is a setting where shirking has been studied. For theoretical papers on tenure see Carmichael (1988) and McPherson and Schapiro (1999). For professors, studies have found evidence of a fall in publishing with age, and a drop-off following tenure (Holley 1977; Levin and Stephan 1991; Faria and McAdam 2015). Rises in absenteeism following tenure have been found for school teachers (Hansen 2009; Jacob 2013; Jones 2015). Increases in absenteeism have also been found following law changes making it harder to fire workers (Scoppa 2010; Ichino and Riphahn 2005). 

3 Early studies of shirking in Major League Baseball (Lehn 1982; Krautmann 1990; Scoggins 1993; Krautmann 1993) find mixed results, and identification is generally poor. More recent literature on shirking in professional sports (Krautmann and Solow 2009; Hakes and Turner 2008; Krautmann and Donley 2009; and Berri and Krautmann 2005) find mixed results as well, and also do an insufficient job of addressing selection into multi-year contracts. 

4 Player contracts outline scenarios where a team may terminate a contract, including the failure to conform to standards of “good sportsmanship and good citizenship”, failure of the player to keep himself in “first-class physical condition” or to “obey the Club’s training rules”, failure to “exhibit sufficient skills or competitive ability”, and failure to “render his services” as outlined in the contract. However, the Player’s Association has made many attempts to void contracts without paying unsuccessful. This includes instances of players being charged with driving while intoxicated, assault, smuggling drugs with intent to distribute, and solicitation of a prostitute. A rare case where a player was successfully terminated occurred when a player grabbed his team’s general manager by the neck and repeatedly slammed him to the ground (Macramalla 2013). 



2019 Research Papers Competition Presented by: 



2 



The primary research question that this study looks to answer is “Does signing Major League Baseball players to contracts that are multiple years in length cause players to shirk in the early years of such contracts?” This paper looks to first identify a causal relationship between the number of years remaining on a player’s contract and player performance. Players who receive multi-year contracts are likely to have higher levels of innate ability or greater propensity to exert effort than those who do not. As a simple regression of player performance on contract years remaining is likely to lead to biased results, a fixed-effects regression strategy will be used to address positive selection into multi-year contracts. Using this strategy, evidence of a negative relationship between contract years remaining and performance is found. 

Past studies that find evidence of a negative relationship between contract length and player performance claim that this is due to shirking in the early years of a contract<sup>5</sup> . However, there are alternative explanations for why player performance may improve throughout the duration of a contract other than shirking. For example, signing a new, multi-year contract could mean the player is undergoing other changes if this new contract is signed with a new team. The adjustment process involved with joining a new team involves playing home games in a new stadium, hitting more frequently against different opposing pitchers, and more. Teams may be more likely to sign players that they expect to improve over time to multi-year contracts. If this is the case, a negative relationship between years remaining on a contract and performance will also be observed, as the player improves through the duration of the contract. Regressions will be run including additional control variables to address these two alternative explanations. To further convince the reader that the results are driven by shirking, heterogeneity in player performance between non-pitchers and pitchers, and between offensive and defensive performance for non-pitchers, will be considered. A player shirks in MLB by violating the terms of his contract. Knowing how a player can shirk helps in predicting for which types of player and within which parts of the game shirking is more likely to occur<sup>6</sup> . The results presented in this study are consistent with the hypothesis that negative relationship between years remaining and performance is being driven by player shirking. 

5 Lehn (1982), Scoggins (1993), Krautmann and Solow (2009), and Hakes and Turner (2008) all find evidence of a negative relationship between contract length and player performance. Krautmann and Donley (2009) and Berri and Krautmann (2006) both use two different dependent variables, and find evidence of a negative relationship with one of the two measures but not the other. 

6 The Uniform Player’s Contract presented in the collective bargaining agreements between the thirty teams and the Players Association outlines expectations for players. Specifically, the player is expected to use his “exceptional and unique skill and ability as a baseball player” in performance for his team during spring training, the regular season, and the playoffs. Also, players are expected to remain in “first-class physical condition” and follow training rules specified by the team (“20072011 Basic Agreement”; “2012-2016 Basic Agreement”; “2017-2021 Basic Agreement”). 



2019 Research Papers Competition Presented by: 



3 



The rest of the paper proceeds as follows. Section II presents a theoretical model of shirking behavior. Data and empirical methodology are discussed in section III. Section IV presents evidence of a relationship between contract years remaining and performance. Section V presents evidence that the negative relationship found between years remaining and performance is driven by player shirking. Section VI concludes. 

## **2. Theory and Model** 

To understand player decision making during a multi-year contract, a model will be introduced using a utility maximizing framework. Players are assumed to maximize utility, where utility is an increasing function of expected future consumption, and a negative function of effort. The utility function for player _i_ is of the form _𝑈𝑖=𝑈𝑖𝐶𝑝𝑡𝑒𝑡, 𝑒𝑡,_ where _𝐶_ is the present discounted value of consumption and _𝑒𝑡_ is effort in time _t_ . The present value of consumption depends on performance in time _t_ , _𝑝𝑡_ , among other factors. Performance in time _t_ depends on effort in time _t_ . The player is assumed to choose effort in time t to maximize utility. To solve the model and develop predictions, a functional form will be assumed. 

The player’s career is assumed to last an infinite number of periods<sup>7</sup> . Future consumption will be discounted at rate _ρ_ , so the present value of consumption can be written as _𝐶=𝑐𝑡+𝜌𝑐𝑡+1+𝜌2𝑐𝑡+2+…_ . 

Consumption in time _t_ , _𝑐𝑡_ , comes from salary earned in time _t_ , _𝑠𝑡_ . Players who are under contract have salaries that are fixed, and do not depend on effort in the current year. At the end of the current contract, future player salaries depend on performance in prior years, among other factors, and notably for the player future salaries depend on performance in the current year, _𝑝𝑡_ . Player performance in time _t_ will be assumed to be a linear function of effort in time _t_ , _𝑒𝑡_ , and a random error term, _𝜇𝑡_ . This random error term prevents teams from contracting on effort. For seasons beyond the end of the current contract, salary in time _𝑡+𝑛_ can be written as 

_𝑠𝑡+𝑛=𝛽𝑡+𝑛+𝛼𝑛−1(𝑒𝑡+𝜇𝑡)_ , 

where _𝛽𝑡+𝑛_ is a constant term that captures performance in prior seasons other than season _t_ and other factors that may affect salary in time _t_ , and the impact of past performance on salary, _𝑝𝑡_ , is discounted at rate _𝛼_ by the team. Expected future consumption with _n_ remaining years of guaranteed contract can be written as 

_𝐶=𝑠𝑡+…+𝜌𝑛−1𝑠𝑡+𝑛+𝜌𝑛𝛽𝑡+𝑛+1+𝛼𝑛𝑒𝑡+𝜇𝑡+…_ . 

This can be simplified to 

#### _𝐶=𝑆+𝛽+(𝛼𝜌)𝑛1−𝛼𝜌𝜇𝑡+(𝛼𝜌)𝑛1−𝛼𝜌𝑒𝑡_ , 

> 7 This assumption can be relaxed without impacting the key findings of the model. 





2019 Research Papers Competition Presented by: 

4 



where _S_ is the present value of guaranteed salaries, and _𝛽_ is the portion of the present discounted value of future salaries that does not depend on current effort. 

Utility is an increasing function of present discounted consumption and a decreasing function of effort. The disutility of effort is assumed to enter quadratically<sup>8</sup> , so utility in time _t_ can be written as 

_𝑈𝑡=𝑆+𝛽+(𝛼𝜌)𝑛1−𝛼𝜌𝜇𝑡+(𝛼𝜌)𝑛1−𝛼𝜌𝑒𝑡−𝑒𝑡2_ . 

The player chooses effort in time _t_ to maximize utility. This level is found by setting the partial derivative of _𝑈𝑡_ with respect to _𝑒𝑡_ equal to zero, so 

_𝜕𝜕𝑒𝑡𝑈𝑡=(𝛼𝜌)𝑛1−𝛼𝜌𝑒𝑡−2𝑒𝑡=0_ . 

Solving for effort gives _𝑒𝑡=(𝛼𝜌)𝑛2(1−𝛼𝜌)_ . 

Predictions about player performance can be drawn from the theoretical model. The key prediction of the model is that as the number of years remaining on the contract, _n_ , increases, effort in time _t_ decreases. This is the shirking hypothesis. One simplification of the model presented is that the player is assumed to live infinitely. Since players have finite careers, the sum of a finite series will be less than that of an infinite series. Consequently, player effort is a decreasing function of the remaining career length. 

The model presented does not set a limit on the extent to which a player can shirk. This may be unrealistic. While the guaranteed nature of player contracts allows players to shirk, the desire to earn future contracts may cause players to want to shirk without being caught to avoid developing a reputation as a shirker. As performance depends on effort but with noise, a player can perform below expectation by a certain amount without a team knowing the player shirked. Suppose the team expects the player to perform at level _𝑝𝑡_ equal to player performance in the last year of a contract. If the noise on performance, _𝜇_ , falls between _−𝜇𝑡_ and _+𝜇𝑡_ , player performance must be at least _𝑝𝑡−𝜇𝑡_ . Therefore, shirking behavior will increase with contract length but may reach a maximum and level off. 

## **3. Data and Empirical Strategy** 

This study looks to identify the relationship between years remaining on a player’s contract and player performance. The key independent variable is the number of years remaining on the player’s contract. Player contract data comes from the Cot’s Baseball Contracts website. This website has team payroll data dating back to 2000, and player contract data starting with the 2009 MLB season (Euston n. d.). Consequently, the data 

8 This assumption was made to be able to solve for a closed form solution. Other functions forms for effort can be chosen without impact the model’s predictions. The model’s key predication depends primarily on the player and team discounting the future. 





2019 Research Papers Competition Presented by: 

5 



employed in this study for the primary analysis consists of yearly player data from the 2010 to 2017 seasons. 

For purpose of the main analysis, the sample in this study will be restricted to non-pitchers, as is standard in the literature, with three or more years of MLB service<sup>9</sup> . The final sample includes 1,829 contract-year observations, 1,068 of which come from players in the first year of a new contract. The sample consists of observations for 535 unique players, with the average player appearing in the sample for 3.4 seasons. 

Table 1 shows contract lengths of new contracts in the sample. Just over twenty-five percent of contracts in the sample exceed one year in length. Of contracts greater than one year in length, contracts of two years are most common, with the frequency of contracts decreasing as contract length increases. 

|TABLE 1<br>Contract Lengths of New C<br> <br>|ontracts<br>|
|---|---|
|Length (Years)<br>Frequency|Percentage|
|1<br>798|74.72|
|2<br>139|13.01|
|3<br>52|4.87|
|4<br>30|2.81|
|5<br>19|1.78|
|6<br>8|0.75|
|7<br>9|0.84|
|8<br>8|0.75|
|9+<br>5|0.46|
|Total<br>1,068|100.00|



The measure of performance will be Wins Above Replacement (WINS<sup>10</sup> ). Data for WINS comes from the Baseball-Reference website (Baseball-Reference.com). Wins Above Replacement is a newer advanced metric developed by baseball statisticians to measure 

9 The reason the sample is restricted to only those with at least three years of experience is because of rules regarding player contracting outlined in the Collective Bargaining Agreement (CBA). For players acquired by a team through the player draft, the team has rights over the player outlined in the CBA. The player must accept the team’s offer if the player has less than three years of MLB experience. As a result, players in the first three years are typically given one-year contracts that pay approximately the league minimum. For those with greater than three but less than six years of service, the team will make the player a contract offer, but the player has a right to renegotiate the contract through an arbitration process. As a result, salaries for players with between three and six years of experience are generally comparable to those of players with greater than six years of experience. Those with six years or more of experience not under contract enter free agency, where all teams can make contract offers to the player (”2017-2021 Basic Agreement”). 10 The standard acronym for Wins Above Replacement is WAR. The use of WINS here is due to author preference. 





2019 Research Papers Competition Presented by: 

6 



player performance. The goal of WINS is to have an all-inclusive measure of player contribution to his team. The value of WINS is interpreted as the number of wins a player adds to his team relative to a replacement level AAA (minor league) or MLB bench player. While multiple sites calculate WINS, the two most commonly used measures come from Fangraphs.com and Baseball-Reference.com. WINS data for this study come from BaseballReference.com<sup>11</sup> . Position players contribute wins through batting, base-running, and fielding. To calculate WINS<sup>12</sup> , one adds batting runs added, base-running runs added, and fielding runs added, and then divides by runs per win. In this calculation, adjustments are made by position and league. 

Additional independent variables which will serve as control variables will be included in regressions as well. These variables include age, MLB experience (service), league, and position. Data for these variables comes from the Baseball-Databank website. This website has comprehensive player and team data dating back to 1871 (Baseball-Databank.org). 

Descriptive statistics are presented in Table 2. Means and standard errors are presented first for the whole contract-year sample, then for one-year contracts, then for multi-year contracts with one year remaining, then for contracts with two or more years remaining. The mean value of WINS is 1.48. Despite being significantly younger on average, players on one-year contracts have WINS that are significantly lower than that of players in final year of a multi-year contract. Positive selection into multi-year contracts is likely driving this difference. This highlights the need to control for this selection. Mean performance for those under multi-year contract is higher with two or more years remaining than in the final year. This runs counter to the shirking hypothesis. However, the players are significantly older in the final year of multi-year contracts, which highlights the need to control for age. 

|||TAB<br>Summar|LE 2<br>y Statistics|||
|---|---|---|---|---|---|
|Variable|All Contracts|One Year|All Multi-<br>Year|One Year<br>Left (Multi-<br>Year)|Two+ Years<br>Left (Multi-<br>Year)|
|WINS|1.48|0.97|1.89|1.54|2.07|
||(0.05)|(0.06)|(0.07)|(0.11)|(0.09)|
|YEARS LEFT|1.87|1.00|2.58|1.00|3.36|



11 batters in 2017, six of the top ten in WINS are common across the two sites. For a detailed description of differences between these two measures and other common measures see www.baseball-reference.com/about/war explained comparison.html. 

12 On-Base Plus Slugging Percentage (OPS) has been commonly used in the literature. The primary difference between the two measures of performance is that WINS is a function of batting, fielding, baserunning, and games played, while OPS is only a function of batting. Using OPS to calculate the results presented later on gives similar results to those presented using WINS. 



2019 Research Papers Competition Presented by: 



7 



||(0.04)|(0)|(0.06)|(0)|(0.07)|
|---|---|---|---|---|---|
|AGE|31.23|30.99|31.43|32.37|30.96|
||(0.08)|(0.13)|(0.10)|(0.17)|(0.12)|
|AL|0.50|0.51|0.50|0.51|0.49|
||(0.01)|(0.02)|(0.02)|(0.03)|(0.02)|
|EXPERIENCE|6.87|6.09|7.51|8.07|7.23|
||(0.08)|(0.13)|(0.10)|(0.17)|(0.12)|
|SALARY|6.42|2.85|9.29|7.80|10.00|
||(0.13)|(0.09)|(0.19)|(0.26)|(0.24)|
|N|1,829|815|1,014|337|677|



Notes: Standard errors are presented in parentheses below the means. The sample here consists of contract year observations, so N is the number of contract-years in each category. Salary is measured in inflation adjusted (base year = 2010) millions of dollars. AL is a dummy variable indicating that the player plays in the American League. One-year contracts are those contracts which are one year in length. Multi-year contracts are those exceeding on year in length. 

When trying to identify the relationship between years remaining on a player contract and player performance, it is important to address positive selection into multi-year contracts. Teams are most likely to give multi-year contracts to the best players. As player ability is likely to be positively related to both contract length and performance, omitting player ability in regressions of performance on contract years remaining will lead to coefficient estimates that are upward biased. As discussed previously, a player fixed-effects estimation strategy will be used to address this bias. To test for the impact of contract years remaining on player performance, regressions will be run of the form 

_𝑃𝐸𝑅𝐹𝑂𝑅𝑀𝐴𝑁𝐶𝐸𝑖𝑡=𝛽0+𝛽1𝑌𝐸𝐴𝑅𝑆𝐿𝐸𝐹𝑇𝑖𝑡+𝛽2𝑂𝑁𝐸𝑌𝐸𝐴𝑅𝑖𝑡+𝛽_ **_𝑿𝑿_** _𝑖𝑡+𝛼𝑖+𝜆𝑡+𝜀𝑖𝑡,_ 

where performance will be measured using WINS, _𝑌𝐸𝐴𝑅𝑆𝐿𝐸𝐹𝑇_ is years remaining on the contract, _ONEYEAR_ is a dummy variable indicating a one year contract, **_X_** is a vector of control variables with include age and age-squared, experience, league, and position dummies, _𝛼𝑖_ is the individual fixed effect, and _𝜆𝑡_ is a time fixed effect. The coefficient of interest here is _𝛽1_ . If players shirk, this coefficient is expected to be negative. 

It is also possible that the relationship between years remaining on a contract and performance is non-linear. Krautmann and Donley (2009) suggest that players may want to avoid gaining a reputation as a shirker because this could hurt their chances of receiving multi-year contracts in the future. If this is the case, players may shirk, but only up to some maximum level. Since it is likely that professional athletes enjoy playing the sport that is their job, players could also place a limit on shirking behavior if they fear that too much shirking could lead to reduced playing time. If shirking by players is bounded by some upper limit, rather than seeing performance monotonically decrease with contract length, it is possible that it plateaus. To address the possibility that the relationship between years remaining (YEARSLEFT) and performance (PERFORMANCE) is non-linear, regressions will 





2019 Research Papers Competition Presented by: 

8 



also be run where years remaining is split into separate dummy variables indicating two years remaining, three years remaining, and four or more years remaining<sup>13</sup> . The estimating equation in this case is 

_𝑃𝐸𝑅𝐹𝑂𝑅𝑀𝐴𝑁𝐶𝐸𝑖𝑡=𝛽0+𝛽1𝑇𝑊𝑂𝑌𝐸𝐴𝑅𝑆𝐿𝐸𝐹𝑇𝑖𝑡+𝛽2𝑇𝐻𝑅𝐸𝐸𝑌𝐸𝐴𝑅𝑆𝐿𝐸𝐹𝑇𝑖𝑡+𝛽3𝐹𝑂𝑈𝑅𝑃𝐿𝑈_ 

_𝑆𝑌𝐸𝐴𝑅𝑆𝐿𝐸𝐹𝑇𝑖𝑡+𝛽4𝑂𝑁𝐸𝑌𝐸𝐴𝑅𝑖𝑡+𝛽_ **_𝑿𝑿_** _𝑖𝑡+𝛼𝑖+𝜆𝑡+𝜀𝑖𝑡,_ 

where _TWOYEARSLEFT_ , _THREEYEARSLEFT,_ and _FOURPLUSYEARSLEFT_ are dummy variables indicating two, three and four or more years remaining on a contract. 

## **4. Results** 

#### **4.1 Fixed Effects Regression Results** 

To identify the impact of contract years remaining on player performance, regressions are run with WINS as the measure of performance. Table 3 shows the results of these regressions. Column one shows results without the inclusion of player fixed-effects. Years left is regressed linearly in the second column, and with separate dummy variables for two years left, three years left, and four or more years left in the third column. 

As predicted by theory, the results show a negative relationship between years remaining on the contract and player performance using WINS as the outcome variable. In the first specification, without fixed effects, the coefficient on Years Left is positive, suggesting that having more years remaining on a contract improves performance. This highlights the positive selection into multi-year contracts. This positive selection is also supported by the negative and significant coefficient on the variable indicating having a one-year contract. Adding in fixed effects in the second column causes the coefficient on years left to turn negative. The magnitude of the coefficient indicates that each additional year remaining causes player performance to fall by about 0.07 WINS. This is a sizeable impact relative to the mean. 

||Performa|TABLE 3<br>nce Regression Results|
|---|---|---|
|Variable|WINS|WINS<br>WINS|
|Years Left|0.135***|-0.070*|
||(0.038)|(0.038)|
|2 Years Left||-0.305***|
|||(0.118)|
|3 Years Left||-0.297*|
|||(0.170)|



13 A separate but closely related literature looks at player performance in the final year of a contract. In this literature, the key independent variable is a dummy variable taking on a value of one if the player is in the last year. Within this literature, O’Neill (2013) has employed a fixedeffects estimation strategy and found evidence of an increase in performance in the final year. 



2019 Research Papers Competition Presented by: 



9 



|4 Or More Years Left|||-0.209<br>(0.187)|
|---|---|---|---|
|One Year Contract|-0.358***|0.294**|0.189|
||(0.114)|(0.118)|(0.128)|
|Age|-0.688**|1.169***|1.126***|
||(0.202)|(0.387)|(0.384)|
|Age Squared|0.007**|-0.016***|-0.015***|
||(0.003)|(0.005)|(0.004)|
|Experience|0.079**|-0.564*|-0.571**|
||(0.037)|(0.290)|(0.289)|
|American League|0.095|-0.124|-0.139|
||(0.101)|(0.097)|(0.097)|
|Position Dummies|Yes|Yes|Yes|
|Year Fixed-Effects|Yes|Yes|Yes|
|Player Fixed-Effects|No|Yes|Yes|
|N|1,829|1,829|1,829|
|Number of Players|535|535|535|
|Adj. R-sq.|0.112|0.218|0.220|



Notes: The sample is restricted to non-pitchers. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

The third specification tests for the possibility that the relationship between contract years remaining and performance may be non-linear. As indicated by coefficients on the years remaining variables, the impact of years remaining on performance does not appear to increase linearly. Rather, it appears that performance is at its highest in the final year of the contract and at a comparable lower level in all other years. Relative to the final year of the contract, with two or more years remaining players add about 0.3 fewer wins relative to a replacement level player. 

#### **4.2 Additional Sample Restriction** 

To ensure the robustness of the presented results showing the relationship between years remaining and performance, regressions are run with an additional sample restriction. The sample is restricted to include only those players with at least six years of service in MLB. While the previous analysis included those with at least three years of service, this further restriction causes the sample to include only those who are free agent eligible, rather than those free agent or arbitration eligible. While this greatly reduces the sample for analysis, this is the sample restriction most common in the literature. 

Results of regressions using a sample of free-agency eligible players only are presented in Table 4. Like Table 3, the first column shows results without the inclusion of fixed-effects. Here again the coefficients on years left and the one-year contract indicator suggest 





2019 Research Papers Competition Presented by: 

10 



positive selection into multi-year contracts. In the fixed effects specifications, columns two and three, the coefficients indicate a negative and significant relationship between years remaining on a contract and performance. 

||Free-AgencyEli<br>|TABLE 4<br>gible OnlyRegression Results<br> <br>|
|---|---|---|
|Variable|WINS|WINS<br>WINS|
|Years Left|0.152***|-0.115**|
||(0.048)|(0.048)|
|2 Years Left||-0.241*<br>(0.139)|
|3 Years Left||-0.260<br>(0.211)|
|4 Or More Years Left||-0.453*<br>(0.236)|
|One Year Contract|-0.419***|0.246*<br>0.188|
||(0.123)|(0.149)<br>(0.156)|
|Age|-0.774**|0.923<br>0.929|
||(0.310)|(0.599)<br>(0.597)|
|Age Squared|0.008*|-0.008<br>-0.009|
||(0.004)|(0.007)<br>(0.007)|
|Experience|0.082|-0.908**<br>-0.890**|
||(0.051)|(0.413)<br>(0.415)|
|American League|0.153|-0.161<br>-0.174|
||(0.130)|(0.129)<br>(0.130)|
|Position Dummies|Yes|Yes<br>Yes|
|Year Fixed-Effects|Yes|Yes<br>Yes|
|Player Fixed-Effects|No|Yes<br>Yes|
|N|1,019|1,019<br>1,019|
|Number of Players|323|323<br>323|
|Adj. R-sq.|0.160|0.284<br>0.283|



Notes: The sample is restricted to non-pitchers with six or more years of service. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

## **5. Evidence of Shirking** 

A drawback of past work studying the relationship between contract length and player performance in MLB is a lack of convincing evidence that the observed relationship is driven by shirking, rather than some alternative explanation. There are other potential reasons to believe that an observed negative relationship between years remaining on contracts and player performance is possible. Two possible alternative explanations will be 





2019 Research Papers Competition Presented by: 

11 



addressed here. First, the possibility that the observed relationship is due to players adjusting to signing multi-year contracts with a new team will be addressed. Second, the possibility that teams sign players they expect to improve to multi-year contracts will be addressed. 

Evidence that is consistent with what would be expected of shirking players will be also presented. First, WINS for our non-pitcher sample will be split into offensive WINS and defensive WINS. Under the assumption that players do not want to get caught shirking, players may be more likely to shirk on offensive than on defense. Second, results will be presented for pitchers. As the pitcher’s game is controlled more closely by the team, and pitchers report to the team for Spring Training earlier than hitters, pitchers should be less likely to shirk. 

#### **5.1 Addressing Alternative Explanations** 

One possible explanation for this observed relationship is that signing a new contract may lead to changes for the player. Signing a new contract could involve signing with a new team. Adjusting to a new situation could cause performance to suffer at the start of a new contract. During a player’s a tenure with his team, he is likely to acquire some firm specific human capital. This firm specific human capital could be related to experience playing in the home stadium, playing with a group of teammates and coaches, or more. Pollard (2002) finds that teams experience a fall in home field advantage when moving to a new stadium. As such it is reasonable to believe that a player may see an effect when moving to a new home stadium. 

To address the possibility that changing teams is driving the relationship between years remaining and performance, two approaches are taken. Regressions are run controlling for whether a player has joined a new team and interacting this new team dummy with the years remaining variables. A second approach is to control for the player’s tenure with his team. Table 5 shows results for these regressions. The first two specifications include the controls relating to joining a new team, while the last two specifications control for tenure. In the first specification, the impact on years left remains negative and significant, while the coefficient on the interaction term is not significant. In the second specification the two and three years left coefficients increase in magnitude and are significant. The coefficients on the new team-two years left interaction term is positive and significant, while the other interaction terms are not significant. The third and fourth specification control for player tenure with his team. Relative to the results presented in Table 3, the coefficients on the years remaining variables have increased when controlling for tenure. As the coefficients of interest remain negative and significant in each of these specifications, there is not evidence to support that this alternative explanation is driving the relationship between years remaining and performance. 

#### TABLE 5 

New Team Alternative Explanation Regression Results 



2019 Research Papers Competition Presented by: 



12 



|Variable|WINS|WINS|WINS|WINS|
|---|---|---|---|---|
|Years Left|-0.068*<br>(0.039)||-0.087**<br>(0.039)||
|2 Years Left||-0.443***||-0.334***|
|||(0.146)||(0.120)|
|3 Years Left||-0.329*<br>(0.178)||-0.349**<br>(0.173)|
|4 Or More Years Left||-0.188<br>(0.198)||-0.284<br>(0.188)|
|One Year Contract|0.246*|0.169|0.236*|0.124|
||(0.126)|(0.142)|(0.123)|(0.134)|
|New Team|0.143|0.083|||
||(0.103)|(0.111)|||
|Years Left*New Team|-0.036<br>(0.063)||||
|2 Years Left* New Team||0.415*<br>(0.220)|||
|3 Years Left* New Team||-0.027<br>(0.433)|||
|4 Or More Years Left* New||-0.295|||
|Team||(0.324)|||
|Age|1.122***|1.077***|1.191***|1.142***|
||(0.382)|(0.377)|(0.387)|(0.384)|
|Age Sq.|-0.017***|-0.015***|-0.016***|-0.015***|
||(0.005)|(0.004)|(0.005)|(0.004)|
|Experience|-0.550*|-0.530*|-0.589**|-0.595**|
||(0.288)|(0.288)|(0.291)|(0.290)|
|Tenure|||-0.050**<br>(0.021)|-0.049**<br>(0.021)|
|American League|-0.131|-0.138|-0.123|-0.139|
||(0.097)|(0.098)|(0.097)|(0.097)|
|N|1,829|1,829|1,829|1,829|
|Number of Players|535|535|535|535|
|Adj. R-sq.|0.219|0.224|0.222|0.224|



Notes: Position dummies, year, and player fixed effects are included in both regressions. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

Another possibility is that teams sign players to multi-year contracts if they expect the player to improve over time. If a team correctly believes the player they are signing to a multi-year contract is on an upward trajectory, the relationship between years remaining on a contract and performance will be negative, just as would be the case if the player 



2019 Research Papers Competition Presented by: 



13 



shirks. To address the possibility that the observed relationship between years remaining and performance is due to the team signing players that they expect to improve, regressions will be run controlling for player salary<sup>14</sup> . In a competitive labor market, players will be paid salaries commensurate with their marginal revenue product. If the team signs a player they expect to improve to a multi-year contract, this should be reflected in the yearly salaries during the contract. For this analysis, the sample will be restricted to only players with six years of service. This is because the salaries of free agent eligible players will be most reflective of the team’s valuation of the player. For arbitration eligible players, the team has greater monopsony power and the salary may not be representative of the team’s valuation. 

Table 6 presents the results of regressions testing the possibility that team expectations of player improvement are driving the relationship between years remaining and performance. When including years left linearly, the coefficient of interest remains negative and significant. This too supports the notion that the relationship between contract years remaining and performance is not being driven by those players teams expect to improve during the contract. The second specification again shows an increasing relationship between years left and WINS, like that of the restricted sample presented in Table 4. While the coefficients on the years remaining variables are no longer significant in two-tailed tests at the ten percent level, two of the three coefficients are significant at the ten percent level with one-tailed tests. 

|Team E<br>|TABLE 6<br>xpectation of Improvement Regression Results<br> <br>|
|---|---|
|Variable|WINS<br>WINS|
|Years Left|-0.098**|
||(0.047)|
|2 Years Left|-0.222|
||(0.137)|
|3 Years Left|-0.184<br>(0.206)|
|4 Or More Years Left|-0.382|
||(0.232)|
|One Year Contract|0.021<br>-0.039|
||(0.180)<br>(0.189)|
|Salary (in Millions)|-0.058**<br>-0.060**|
||(0.025)<br>(0.020)|
|Age|1.209*<br>1.215*|
||(0.630)<br>(0.631)|



14 Salary is measured in millions of dollars, adjusted for inflation using the Consumer Price Index (base year = 2010). Salary is yearly salary, which varies throughout the duration of player contracts. 



2019 Research Papers Competition Presented by: 



14 



|Age Squared|-0.013*<br>(0.008)|-0.014*<br>(0.008)|
|---|---|---|
|Service|-0.841**|-0.821*|
||(0.415)|(0.419)|
|American League|-0.143<br>(0.125)|-0.154<br>(0.126)|
|Service > 6|Yes|Yes|
|Service>3|No|No|
|N|1,019|1,019|
|Number of Players|323|323|
|Adj. R-sq.|0.290|0.290|



Notes: Position dummies, player and year fixed effects are included in all regressions. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

#### **5.2 Shirking Evidence** 

Based on the expectations for players outlined in the Uniform Player Contract outlined in recent iterations of the Collective Bargaining Agreement, there are two ways in which a player can shirk. Either players shirk by not remaining in good physical shape, or players fail to exert optimal effort during games (“2007-2011 Basic Agreement”; “2012-2016 Basic Agreement”; “2017-2021 Basic Agreement”). Two sources of heterogeneity will be used to shed light on shirking behavior. First, heterogeneity in offensive and defensive performance will be explored for non-pitchers. Assuming the player does not want to get caught and labeled as a “shirker”, the player may try to shirk in ways that are the least observable. As such, a player may not want to shirk on defense. When playing in the field, it is easy to observe a player that does not give maximum effort when chasing down a fly ball or making throws to first base. Offensive shirking may be more difficult to observe. Shirking on offense could take the form of swinging more frequently at bad pitches. It takes effort to be patient and wait for quality pitches. Having longer at-bats also requires the player to spend more time actively engaged in the game. Players could also shirk on offense by not taking enough batting practice. Even the best players go through “slumps” at the plate. Shirking on offense may be difficult to distinguish from the typical “slump”. Generally, there is more noise in the relationship between effort and performance for offense than for defense. As a result, those who shirk may be more likely to do so on offense than on defense. The second source of heterogeneity that will be explored is performance by non-pitchers and pitchers. As we have seen already, evidence suggests that non-pitchers shirk. Pitchers are likely to find it more difficult to shirk. Within games, pitchers are expected to throw the pitch that the catcher asks for. Pitchers are also taken out of the game by the manager whenever the manager feels the pitcher is done for the day. Pitchers almost never pitch complete games. While non-pitchers can be replaced, this happens infrequently. Pitchers are also expected to report to the team for Spring Training about a 





2019 Research Papers Competition Presented by: 

15 



week sooner than are non-pitchers. This means the pitcher has less time during the offseason to shirk on preparation. 

WINS is a function of offense, defense, and games played. WINS can be decomposed into offensive WINS and defensive WINS. Offensive WINS are the components of WINS that come from hitting, base-running, and not hitting into double-plays. Defensive WINS come from performance in the field while the opposing team is hitting. To test for differences in offensive and defensive performance, regressions comparable to those presented in Table 3 will be run using offensive WINS and defensive WINS as outcome variables. 

Regression results testing for differences in the impact of years remaining on offensive and defensive performance are presented in Table 7. The first and second columns show results for offensive WINS, while the third and fourth columns show results for defensive WINS. Years remaining has a negative and significant impact on offensive WINS, in magnitudes comparable to the results for overall WINS. The impact of years remaining on defensive WINS is small and generally statistically insignificant. These findings are consistent with players shirking in games in a way that is a less observable. 

TABLE 7 

||Offensive and D|efensive Perform|ance Regression Re|sults|
|---|---|---|---|---|
|Variable|Off. WINS|Off. WINS|Def. WINS|Def. WINS|
|Years Left|-0.075**||0.010||
||(0.033)||(0.016)||
|2 Years Left||-0.245**||-0.053|
|||(0.099)||(0.052)|
|3 Years Left||-0.324**||0.012|
|||(0.145)||(0.082)|
|4 Or More||-0.259||0.071|
|Years Left||(0.165)||(0.075)|
|One Year Left|0.170*|0.086|0.108*|0.086|
||(0.097)|(0.106)|(0.059)|(0.061)|
|Age|1.232***|1.197***|-0.127|-0.133|
||(0.328)|(0.324)|(0.179)|(0.178)|
|Age Squared|-0.016***|-0.015***|0.001|0.001|
||(0.004)|(0.004)|(0.002)|(0.002)|
|Service|-0.564**|-0.569**|0.003|0.002|
||(0.246)|(0.245)|(0.115)|(0.115)|
|American|-0.074|-0.085|-0.056|-0.060|
|League|(0.082)|(0.083)|(0.057)|(0.057)|
|N|1,829|1,829|1,829|1,829|
|Number of|535|535|535|535|
|Players|||||
|Adj. R-sq.|0.222|0.223|0.063|0.065|





2019 Research Papers Competition Presented by: 



16 



Notes: The sample is restricted to non-pitchers. Position dummies and player and year fixed effects are included in all regressions. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

In understanding shirking behavior, another source of heterogeneity that will be considered are differences between non-pitchers and pitchers. Since the pitcher’s game is under greater control by the catcher and manager, and the pitcher reports to the team sooner for spring training, it is possible pitchers may be less likely to shirk. As non-pitcher results have already been presented, results for pitchers will now be presented. The sample of pitchers for the 2010-2017 period with the same sample restrictions as those for non-pitchers includes 1,679 contract-year observations for 522 unique players, and 1,114 unique contracts. In the pitcher sample multi-year contracts occur at a rate of about 21 percent, with the longest contracts being seven years in length. 

Table 8 shows regression results for pitchers comparable to the results presented for nonpitchers in Table 3. Just like in Table 3, the first specification shows a position and significant impact of years left on WINS, highlighting positive selection in multi-year contracts for pitchers as well. In the second specification, the coefficient on years left is positive, but not-significant. In the third specification, each of the years left coefficients are not significant. These results support the hypothesis that pitchers are less likely to be able to shirk than are non-pitchers. These results and the results of the offense and defense regressions would suggest that the observed negative relationship between years remaining and performance is due to shirking. 

||Pitche<br>|TABLE 8<br>r Regression Results<br>||
|---|---|---|---|
|Variable|WINS|WINS|WINS|
|Years Left|0.520***|0.057||
||(0.079)|(0.070)||
|2 Years Left|||-0.166<br>(0.131)|
|3 Years Left|||0.022<br>(0.137)|
|4 Or More Years Left|||0.137<br>(0.270)|
|One Year Contract|-0.179|0.011|-0.096|
||(0.118)|(0.114)|(0.125)|
|Age|-0.778***|0.568*|0.582*|
||(0.197)|(0.305)|(0.304)|
|Age Squared|0.011***|-0.000|-0.000|
||(0.003)|(0.004)|(0.004)|
|Service|0.015|-0.818***|-0.830***|





2019 Research Papers Competition Presented by: 



17 



|American League|(0.027)<br>0.162*|(0.148)<br>-0.085|(0.149)<br>-0.091|
|---|---|---|---|
||(0.095)|(0.097)|(0.098)|
|Player Fixed-Effects|No|Yes|Yes|
|Year Fixed-Effects|Yes|Yes|Yes|
|N|1,679|1,679|1,679|
|Number of Players|522|522|522|
|Adj. R-sq.|0.013|0.100|0.101|



Notes: The sample is restricted to pitchers. Regressions are run using heteroskedasticity robust standard errors, clustered on player. All hypothesis tests are two tailed, with *** indicating p < 0.01, ** indicating p > 0.05, and * indicating p < 0.1. 

## **6. Conclusion** 

Teams frequently sign players to multi-year contracts yet results in the literature on performance throughout the duration of such contracts are mixed. Fans and the media are often skeptical of large contracts being awarded over long time durations, yet to land the best players teams often must give up substantial sums of money over these long periods of time. This study adds to the literature on shirking in Major League Baseball by presenting causal evidence of an inverse relationship between the number of years remaining on a player contract and player performance. Using player fixed-effects regression specifications, this study finds that having multiple years remaining on a multi-year contract causes the player to perform at a lower level early in the contract relative to performance during the final year of a contract. 

While this finding is of interest to MLB teams and managers, this finding is also of interest to employers in other industries. If multi-year contracts of fixed duration lead MLB players to exert low levels of effort, one could imagine that guaranteed contracts of unlimited duration, such as those given to school teachers and college professors under the tenure system, would lead to low levels of effort as well. Balancing the costs and benefits of guaranteed contracts is important for maximizing profits in all occupations. 

Despite some past studies in the literature on shirking in MLB having presented evidence of a negative relationship between years remaining on a contract and performance, past studies have failed to convincingly persuade readers that this relationship is due to shirking as opposed to alternative explanations. The primary contribution of this study is to present such evidence. First, evidence is presented to address the possibility that this negative relationship is driven by player adjustment to a new team. Evidence is also presented to address to the possibility that the relationship is driven by teams signing players they expect to improve to multi-year contracts. Second, evidence is presented that is consistent with what would be expected of shirking behavior. Players are found to shirk in their offensive performance, but not in defensive performance. Such behavior would be consistent with players shirking during the season only in ways that are less observable to 





2019 Research Papers Competition Presented by: 

18 



the team to avoid gaining a reputation as a shirker. Pitchers, who less freedom in being able to shirk, are not found to exhibit a negative relationship between years remaining on a contract and performance, while non-pitchers are. 

There is still much work to be done in understanding the impacts of contracts on player performance in MLB. In addition to varying in length and salary, contracts may also be extended, include performance incentives, or include option years. The work on such contract components is scarce, with notable exceptions being Krautmann (2018) on contract extensions and Gross and Link (2017) on contract options. As players continue to receive multi-year contracts over time, further work should be done to understand why teams would continue to give such contracts despite evidence of the negative impact on performance. Understanding how long player relationships impact fan engagement and team chemistry could shed light on this issue. In the absence of such evidence, teams should think twice before committing players to multi-year contracts. 





2019 Research Papers Competition Presented by: 

19 



## **References** 

- [1] “2007-2011 Basic Agreement,” Effective December 1, 2006. 

   - http://legacy.baseballprospectus.com/compensation/cots/ 

- [2] “2012-2016 Basic Agreement,” Effective December 1, 2011. http://legacy.baseballprospectus.com/compensation/cots/ 

- [3] “2017-2021 Basic Agreement,” Effective December 1, 2016. http://legacy.baseballprospectus.com/compensation/cots/ 

- [4] Baseball-DataBank.org. _Database in Comma-Delimited Form with Table Defs [Data File]._ n. d. <u>http://www.baseball-databank.org/</u> 

- [5] Baseball-Reference.com. _WAR data archive [Data File]._ n. d. 

- <u>http://www.baseball reference.com/data/</u> 

[6] Berri, D. J. and A. C. Krautmann. “Shirking On The Court: Testing For The Incentive Effects of Guaranteed Pay.” _Economic Inquiry,_ 44(3), 536-546. 

- [7] Cantor, R. “Work Effort and Contract Length.” _Economica,_ 55(219), 1988, 343-353. 

[8] Carmichael, H. L. “Incentives in Academics: Why is There Tenure?” _Journal of Political Economy,_ 96(3), 1988, 453-472. [9] Euston, J. _MLB Contracts, by Team [Data File]._ n. d. Distributed by Cot’s Baseball Contracts, http://legacy.baseballprospectus.com/compensation/cots/ [10] Faria, J. R. and P. McAdam. “Academic productivity before and after tenure: the case of the ‘specialist’.” _Oxford Economic Papers,_ 67(2), 2015, 291-309. [11] Gross, A. and C. Link. “Does Option Theory Hold for Major League Baseball Contract? _Economic Inquiry,_ 55(1), 2017, 425-433. 

[12] Hansen, M. “How Career Concerns Influence Public Workers’ Effort: Evidence from the Teacher Labor Market.” _Calder Working Paper No. 40,_ 2009, 1-55. 

[13] Holmstrom, B. “Moral Hazard and Observability.” _The Bell Journal of Economics,_ 10(1), 1979, 74-91. [14] Holley, J. W. “Tenure and Research Productivity.” _Research in Higher Education,_ 6(2), 1977, 181-192. 

[15] Ichino, A. and R. T. Riphahn. “The Effect of Employment Protection on Worker Effort: Absenteeism During and After Probation.” _Journal of the European Economic Association,_ 3(1), 2005, 120-143. 

- [16] Jacob, B. A. “The Effect of Employment Protection on Teacher Effort.” _Journal of Labor Economics,_ 31(4), 2013, 727-761. 

[17] Jones, M. D. “How do teachers respond to tenure?” _IZA Journal of Labor Economics,_ 4(8), 2015, 1-19. 

[18] Krautmann, A. C. “Shirking or Stochastic Productivity in Major League Baseball?” _Southern Economic Journal,_ 56(4), 1990, 961-968. 

- [19] Krautmann, A. C. “Shirking or Stochastic Productivity in Major League Baseball: Reply” _Southern Economic Journal,_ 60(1), 1993, 241-243. 

[20] Krautmann, A. C. “Contract Extensions: The Case of Major League Baseball.” _Journal of Sports Economics,_ 19(3), 2018, 299-314. 



2019 Research Papers Competition Presented by: 



20 



[21] Krautmann, A. C., and T. D. Donley. “Shirking in Major League Baseball Revisited.” _Journal of Sports Economics,_ 10(3), 2009, 292-304. [22] Krautmann, A. C. and M. Oppenheimer. “Contract Length and the Return to Performance in Major League Baseball.” _Journal of Sports Economics,_ 3(1), 2002, 6-17. 

[23] Krautmann, A. C. and J. L. Solow. “The Dynamics of Performance over the Duration of Major  Leauge Baseball Long-Term Contracts.” _Journal of Sports Economics,_ 10(1), 2009, 6- 22. 

[24] Lehn, K. “Property Rights, Risk Sharing, and Player Disability in Major League Baseball.” _The Journal of Law & Economics,_ 25(2), 1982, 343-366. 

[25] Levin, S. G. and P. E. Stephan. “Research Productivity Over the Life Cycle: Evidence for Academic Scientists.” _The American Economic Review,_ 81(1), 1991, 114-132. 

[26] Macramalla, E. 2013. “Voiding MLB contracts.” http://www.sportsbusinessnews.com/content/voiding-mlb-contracts. 

[27] McPherson, M. S. and M. O. Shapiro. “Tenure Issues in Higher Education.” _The Journal of Economic Perspectives,_ 13(1), 1999, 85-98. 

[28] O’Neill, H. M. “Do Major League Baseball Hitters Engage in Opportunistic Behavior?” _International Advances in Economic Research,_ 19, 2013, 215-232. 

[29] Pollard, R. “Evidence of a reduced home advantage when a team moves to a new stadium.” _Journal of Sports Sciences,_ 20(12), 2002, 969-973. 

[30] Ross, S. A. “The Economic Theory of Agency: The Principal’s Problem.” _The American Economic Review,_ 63(2), 1973, 134-139. 

[31] Scoggins, J. F. “Shirking of Stochastic Productivity in Major League Baseball: Comment.” _Southern Economic Journal,_ 60(1), 1993, 239-240. 

[32] Scoppa, V. “Shirking and employment protection legislation: Evidence from a natural experiment.” _Economic Letters,_ 107, 2010, 276-280. 





2019 Research Papers Competition Presented by: 

21 


