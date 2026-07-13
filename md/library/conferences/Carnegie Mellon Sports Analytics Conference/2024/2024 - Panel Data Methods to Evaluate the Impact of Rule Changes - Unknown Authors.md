<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2024/2024 - Panel Data Methods to Evaluate the Impact of Rule Changes - Unknown Authors.pdf -->

**Panel Data Methods to Evaluate the Impact of Rule Changes** Lee Kennedy-Shaffer, PhD Department of Biostatistics, Yale School of Public Health 

# **Abstract** 

In recent years, several major team sports have instituted rule changes in attempts to improve game play and the viewing experience. From 2020 to 2023, Major League Baseball instituted several rule changes affecting team composition, player positioning, and game time. Understanding the effect of these rules—both on the game as a whole and on individual teams and players—is crucial for leagues, teams, players, and other relevant parties to assess their impact and either push for further changes or to roll back existing rules. Panel data and quasiexperimental methods provide useful tools for causal inference in these settings. I demonstrate this potential by analyzing the effect of the 2023 shift ban at both the overall and player-specific levels. Using difference-in-differences analysis, I show that the policy increased BABIP and OBP for left-handed batters by a modest amount. For individual players, synthetic control analyses identify several players whose offensive performance (OBP, OPS, and wOBA) improved significantly because of the rule change, and other players with previously high shift rates for whom it had little effect. This work both estimates the impact of this specific rule change and demonstrates how these methods for causal inference are potentially valuable for sports analysis—at the player, team, and league levels—more broadly. 

# **Introduction** 

Professional sports provide seemingly endless opportunities for data-driven changes and experimentation, as teams and players identify and exploit potential advantages. The leagues that govern these sports are not immune to these pressures, changing rules, formats, and broadcast schedules in attempts to increase viewership, relevance, and profits. For example, the National Football League has instituted multiple changes to kick-off and tackling rules to try to balance player safety and excitement (1,2); the National Basketball Association has instituted rules around star player rest days (3); and Major League Baseball (MLB) implemented several changes around hitting, pitching, baserunning, and fielding play, largely designed to reduce game times and/or increase offense and the number of baserunners (4–6). 

Analyzing the effects of these rules—on both their intended and unintended outcomes— should be approached with the same degree of statistical rigor as the analysis of players and teams. However, for a variety of reasons, this has generally not been the case. There is less incentive for this analysis as there is limited benefit to anyone other than the league; even if it does occur by either leagues or teams, it is unlikely to be public. In addition, there is a statistical challenge: these leagues are somewhat one-of-a-kind and therefore the core statistical requirement of repetition and multiple observations is difficult. 

1 

Panel data methods and so-called quasi-experimental causal inference can provide a solution to the statistical problem, given that certain key assumptions are met. These frameworks, which are often used in policy and economic evaluation, comprise a variety of methods with different assumptions and data requirements (7–10). They generally rely on longitudinal or panel data sets, where the outcome is measured repeatedly, in some cases before and in some cases after the policy goes into effect. The simplest approach, a pre-post design or interrupted time series, compares the post-policy outcome to the pre-policy outcome, either using the time points closest in time to each other, averages before and after the change, or a model of the time trend (7). This approach, although not often stated as such, is commonly used in publicfacing articles around rules changes (see, e.g., (6)). The major downsides are that it assumes a consistent and predictable time trend in the outcome and cannot disentangle the policy of interest from any other changes occurring at the same time. 

To address these drawbacks, controlled pre-post designs can be used if there are time series available both for observations that are affected by the policy change and for observations that are not affected (7). One such approach, difference-in-differences (DID), requires the affected and unaffected observations or groups to have parallel time trends in the counterfactual world where no policy change occurs, but we do not need to explicitly model that trend (8). Another approach, the synthetic control method (SCM), requires multiple unaffected time series; none of these needs to follow the time trend of the affected time series, but the method identifies a weighted average of those unaffected groups that is a good match for the affected group (8). These methods have been used in settings as diverse as identifying the effects of minimum wage increases (11), geopolitical case studies across countries (12), and, recently, the impact of COVID-19 interventions (13) and vaccines (14), among many others. More detailed discussions of the requirements and implementations of these methods are available in, e.g., (9,10,15,16). 

In sports, these methods have become popular in evaluation of the economic and social impacts of sports events, teams, or stadiums (17–21) and in business analyses of revenue and attendance effects of decisions (22–24). A recent study also looked at the effect of MLB’s automatic baserunner rule in extra innings on game times using DID (5). As far as I am aware, however, there has been little use of these methods on in-game outcomes such as team, league, and player statistics. This provides an opportunity to use modern statistical methods to fully understand the impact of these rule changes. 

In this paper, I study the effect of the recent MLB rule banning the infield shift (6) on batting outcomes. I look at both league-level and player-level outcomes, which provide estimates of effects of interest to different audiences: namely the league and team business operations, who are most interested on the rule’s ability to increase “exciting” game events; and team baseball operations and the players and their representatives, who may be interested in the rule’s effect on their own game and how to change their playing style. I also discuss the broader potential for the 

2 

use of these methods in sports analytics, as well as open questions that will inform for which applications, settings, and outcomes they can be most beneficially used. 

# **Data and Methods** 

All code, data, and results are available in the <u>GitHub repository.</u> 

_Analysis 1: League-Wide Effects_ 

To analyze league-wide effects of the rule change, we are interested in comparing shift situation plate appearances (PAs) to non-shift situation PAs. Previous cross-sectional (within a single season) analyses have compared shifted and non-shifted PAs, or to give a less biased comparison, shifted vs. non-shifted PAs among players with substantial numbers of each (25– 27). Of course, after the shift ban, there are no shifted PAs, so we cannot use shifted and nonshifted PAs as our time series. Other analyses have compared right-handed to left-handed batters, given that left-handed batters are shifted much more frequently (6,28), performing analyses similar to DID when looking at the effect of the ban. Here, I use this approach, limiting to basesempty PAs, settings where shifts are even more common. Data are collected from the FanGraphs Splits Leaderboard (29) across MLB, by batter handedness for PAs with no runners on. 

Using these data, I conduct a DID analysis comparing left-handed batters (LHBs) to right-handed batters (RHBs) in these PAs, after vs. before the shift ban (i.e., in the 2023 season vs. the 2022 season). The same analysis is conducted for earlier seasons (2015–2022, excluding the shortened 2020 season) compared to one season prior, where we should see no effect because no policy change occurred. The 2015 season was chosen as the starting point for two reasons: first, it is the beginning of full Statcast data on fielder positioning, which will be relevant for other analyses; second, it is a reasonable starting point for the modern shift era where all teams were employing it to some degree (25). For this analysis, where the emphasis is on league-wide effects and MLB may be the most relevant audience, I consider two outcomes: batting average on balls in play (BABIP) and on-base percentage (OBP), which relate to MLB’s goals for the policy change of increasing base hits and having more baserunners (30,31). 

_Analysis 2: Player-Specific Effects_ 

To analyze the effects of the policy change on specific players, we turn to player-specific data and the synthetic control method. First, season-average or -total batting statistics were collected for all players with at least 250 PAs in any of the 2015–2023 seasons, excluding the shortened 2020 season, via Baseball Savant’s Statcast Custom Leaderboard (32). Shift rates for all players who had at least 250 PAs in each of 2021–2023 were obtained from Baseball Savant’s Statcast Batter Positioning Leaderboard (33), and they were categorized into low (no more than 20% of PAs), high (at least 80%) and medium (20–80%) shift rates based on their 2022 shift rate in bases-empty PAs. This resulted in 26 players in the high-shift category; these target players 

3 

will be the focus of the analysis. The 59 players in the low-shift category form the controls or “donor pool” for the SCM analysis. Here, I consider three batting outcomes that are useful in assessing the batting value of the player and would be relevant directly to him, his team, and his representatives: OBP, on-base plus slugging (OPS), and weighted on-base average (wOBA). 

For each of the 26 target players, I add to the 2021–2023 data the seasons from 2015– 2019 in which they had at least 250 PAs. Their donor pool is obtained by finding the players in the overall donor pool who had at least 250 PAs in at least those same seasons. For each outcome, a synthetic control is fit using the time series of the outcome prior to 2023 as the series to match. The outcome, PAs, hits, singles, home runs, base-on-balls percentage, and strikeout percentage are used as the predictors in all pre-intervention seasons, with all covariates except the outcome itself used individually for 2021 and 2022 and averaged over all included pre-2020 seasons (see (16) for details on the method). This yields a weighted average of players in the donor pool (i.e., low-shift players) whose history of that statistic in recent seasons is most similar to the target player. Those same weights are then applied to the donor players’ 2023 results to get a synthetic (or counterfactual) outcome for the target player: what we would expect their 2023 outcome to be if the rule had not been changed. This is compared to their actual 2023 outcome to get an estimate of the effect of the rule on their result. 

I then perform placebo tests to compare these estimates to the underlying variability of the statistics and methods. The same SCM analysis is conducted for each of the 59 low-shift control players as if they were the target player, excluding them from the donor pool. This gives a placebo or null distribution of the estimates we would see among players if there were no effect of the rule change, due to the natural uncertainty of the weighting algorithm and the year-to-year fluctuations in batting performance. 

# **Results** 

# _Analysis 1: League-Wide Effects_ 

The results of the league-wide DID analysis for BABIP and OBP with bases empty are given in <u>Table 1. Both indicate a modest increase in the outcome for left-handed batters in 2023</u> compared to what would have been expected in the absence of a rule change, with both estimates (coincidentally) equal to 0.009, or 9 points. To situate this magnitude in terms of yearly fluctuations and assess the parallel trends assumption, Figure 1 plots the trends in the two outcomes by batter handedness and year, beginning in 2015 and excluding 2020 (A,B) and the same analysis for each of these seasons compared to the previous full season (C,D). Other batting summary outcomes (average, slugging percentage, OPS, wOBA) had similar results (see the GitHub repository or the <u>interactive R Shiny app</u> for all results). The estimated effect of the rule change for both base-on-balls and strikeout percentage was an increase, with a higher magnitude for walks (0.5 percentage points) than strikeouts (0.1). 

4 

For years where no policy change occurred, the DID estimate centered around 0, generally with a small magnitude. This indicates the larger 2023 estimate likely represents a true effect. However, both 2021 and 2022 had estimates (pre-trends) less than 0. This may reflect a divergence in the trends of RHBs and LHBs, possibly due to effective fielder positioning or other rule changes with a differential effect (like the universal designated hitter). If anything, this may indicate that LHBs would have continued to worsen compared to RHBs, causing the 2023 estimates to underestimate the positive effect of the change. 



_Figure 1._ Trends by batter handedness (A,B) and DID estimates (C,D) for  BABIP (A,C) and OBP (B,D) by year, 2015–2023, excluding 2020, for bases empty plate appearances. The counterfactual 2023 value is also shown (A,B) assuming the increase from 2022 would be the same for LHBs as for RHBs in the absence of the rule change. Each DID estimate (C,D) is a comparison of LHBs to RHBs for the listed season compared to the previous full season. Data source: FanGraphs Splits Leaderboard (29). 

# _Analysis 2. Player-Specific Effects_ 

To illustrate the player-specific SCM estimates, I show results here for Corey Seager. Seager had over 650 PAs and the fourth-highest shift rate (96.5%) of any of the target players in 2022 (33) and was specifically noted as a player likely to benefit from the new rule (34). That analysis relied on modelling his batted-ball locations in 2022 and identifying balls in play that would have likely been hits in the absence of the shift. While valuable, that analysis cannot 

5 

account for changes in approach (by both pitcher and batter) in the shift-ban environment or for other changes in the batting environment that made 2023 different from 2022. The SCM does account for these changes but relies on the identified weighted average being a good comparison for the particular player, so there is value in conducting both analyses and comparing the results. 

For both OPS and wOBA, the SCM for Corey Seager gave the highest weight to Trea Turner (51% weight for OPS, 59% for wOBA). Justin Turner was second for both wOBA (29%) and OBP (33%), Starling Marte was first for OBP (67%) and fourth for OPS (2%), and Jean Segura was second for OPS (25%) and third for wOBA (6%). This transparency feature of the SCM allows the investigator to assess the validity of the weights using other qualitative or quantitative information. In this case, for example, Trea Turner has a high similarity score with Corey Seager (35), which may provide plausibility to the results. 

Seager’s synthetic OBP in 2023 was estimated to be 0.315, compared to an observed OBP of 0.390, for an estimated effect of the rule change of 75 points. For OPS, the synthetic was 0.744, the observed 1.013, for an estimated effect of 269 points. For wOBA, the synthetic was 0.330, the observed 0.419, for an estimated effect of 89 points. In all cases, the estimates point to a positive effect of the rule change on Seager’s performance, increasing his offensive output by more than 20% compared to what it would have been under the old rules. 



_Figure 2._ Synthetic and observed outcomes (OBP, OPS, wOBA) for Corey Seager compared to the synthetic control constructed by donor players with shift rates no higher than 20% in 2022. Constructed using full (non-2020) seasons from 2016–2023 excluding seasons where Seager had fewer than 250 PAs (i.e., 2018). Donor players had at least 250 PAs in the same seasons. Data sources: Baseball Savant’s Statcast Custom Leaderboard (32) and Statcast Batter Positioning Leaderboard (33). 

6 

The results for all target players are given in <u>Table 2; individual player results can be</u> downloaded from the <u>GitHub repository or explored in the interactive R Shiny app. The</u> estimated effects of the rule change for each player for each of the three outcomes are included, as well as a p-value based on the placebo tests. This indicates the proportion of the placebo test estimates (and that target estimate) that the target estimate tied or exceeded in absolute value. Because of the relatively small number of donor players for some target players, the coarseness of this type of placebo test, and the large numbers of results, these are more useful as an indicator of the reliability of the result rather than as strict hypothesis tests. Plots of the estimates for each of the three outcomes for all target and donor pool players, as well as their pre-intervention fit, are given in Figure 3. 

Overall, for each of the three outcomes, most target players (over 75%) had an estimated increase. The placebo test estimates, as expected, had estimates greater than 0 near 50% of the time (although it was somewhat higher for OPS and wOBA, indicating possible systemic underestimation of the 2023 outcomes). The mean and median value of the estimates across the target players were also much larger (4.5–15 times) than those for the placebo test players. 



_Figure 3._ Plots of estimated effects of the shift ban rule change in 2023 with preintervention trends in the difference between synthetic control estimated and observed statistic for OBP (A), OPS (B), and wOBA (C). All included players had at least 250 PAs in each of the 2021–2023 seasons; target players had at least an 80% shift rate in 2022 while placebo players had no more than a 20% shift rate in 2022. Data sources: Baseball Savant’s Statcast Custom Leaderboard (32) and Statcast Batter Positioning Leaderboard (33). 

7 

# **Discussion** 

In 2023, MLB implemented the ban on infield shifts among a suite of rules changes, with the hope of increasing offense and restoring the look of the game (30,31). Analyses before and after the implementation of the ban generally relied on one or more of the following approaches: pre-post analyses of overall trends (6,28,36); cross-sectional comparisons of right- and lefthanded batters or different types of batted balls (6,28); models of batted ball outcomes with specific fielder positioning data (34,36,37); or within-batter comparisons of shift vs. non-shift PAs (26,27,38,39). These can provide valuable estimates of the effect of shifting, specifically its primary effect on how similarly-hit balls or similarly-used batters are affected by infield alignment. When they include 2023 data, they are estimating the effect of the shift ban in the 2023 run environment, while pre-ban analyses are estimating its effect in a different environment. Nonetheless, the results generally aligned: the shift caused a modest decrease in BABIP for left-handed batters affected by it, which led to lower batting average, OBP, OPS, and wOBA for them as well. 

Comparing modeled outcomes or shifted vs. non-shifted PAs from the pre-2023 era, however, neglects how other rules changes affect play and ignores second- and third-order effects of the shift ban. Specifically, batters and pitchers will change their approaches in response to fielder placement and league rules. Because of this, batters will get different amounts of playing time and face different situations than they would have otherwise, as teams and managers adjust to the new environment (25,30,31,39). These higher-order effects, while presumably smaller in magnitude, are best able to be captured by quasi-experimental designs like the analyses undertaken here. Unlike other pre-post analyses, by using comparison time series that are differentially affected by the shift ban but (presumably) similarly affected by other rules changes, these methods can even attempt to disentangle the effects of different rules changes. 

These analyses found a modest benefit to left-handed batters league-wide in terms of BABIP and OBP (9 points for each). Known as the “average treatment effect on the treated” or ATT, these estimate the effect of the shift ban on these outcomes _for left-handed batters in the 2023 season_ . This is context-specific and may change over time as teams and players adjust their strategies accordingly. While slightly different estimates, they are generally within the ranges predicted from differences between shifted, shaded, and non-shifted PA results by Russell Carleton’s within-batter analysis (38,39). Repeating the analysis using complete 2024 data will provide some indication of whether these effects are lasting, or whether they decline as teams adopt new fielding strategies as predicted by some authors (30,31). 

Player-specific analyses found that many high-shift players saw some benefit from this shift ban; four players (Corey Seager, Yordan Alvarez, Shohei Ohtani, and Matt Olson) saw estimated wOBA increases over 80 points and OPS increases over 200 points, for example. Another four (Cody Bellinger, Brandon Belt, Josh Naylor, and José Ramírez) had estimated OPS increases over 100 points and OBP increases over 30 points. Again, these are ATTs: in this case, 

8 

estimated effects of the shift ban on these outcomes _for that specific player in the 2023 season_ . The most- and least-affected players somewhat align with analyses based on batted ball modeling (36). The differences in the results may arise from using different outcomes, full- vs. partialseason data, and the batted ball analysis not accounting for player’s changes due to other factors of the 2023 batting environment. 

These analyses rely on assumptions to have causal interpretations: for DID, the assumption of parallel trends in the absence of the policy change is needed; for SCM, the weights must be stable over time for the player’s performance in the absence of the policy change. Both analyses also require the assumption of no spillover; that is, that the policy change did not affect the units we consider unaffected. This is clearly not true, as the policy change could somewhat affect all players. Our proxies are presumably less affected, but this can introduce bias; generally it would result in underestimating the magnitude of the effect. Moreover, the ATT estimates these methods produce are not necessarily generalizable. They may change over time for the reasons mentioned above, or due to other policy changes or batting environment changes, and they may be different in different leagues. In addition, the specific choices made in the SCM analysis can affect the results; this includes the choice to drop players entirely for seasons with fewer than 250 PAs, the covariates in the model, and the linear functional form used. Changes to missing data procedures or these choices could provide higher validity of the SCM fits. More complex DID and SCM methods could be useful in addressing assumption violations or for other sports settings (9,10,14,16). Investigating these open questions (parallel trends, spillover, generalizability, time-varying effects) not only enables better use of these methods but improves understanding of the game and how to affect it more generally. 

Overall, quasi-experimental methods can provide a useful framework for causal inference in some sports settings. They allow analysts to estimate causal effects in the specific context, and with transparency and interpretability of the causal assumptions. SCM for player performance in particular has the attractive feature of making clear which players are highly weighted in the control, allowing the assessment of validity using other qualitative or quantitative data. These analyses are particularly useful for assessing rules changes and policies that affect players or teams differently within a league, as they can be used in settings with a small number of affected units. In this way, they can provide a substitute or complement to randomized experiments or pilot studies conducted in other leagues—e.g., the minor leagues (30,40)—which have their own limitations on generalizability. Further research is needed to understand for which settings and outcomes these methods work particularly well, and for which their assumptions may falter. As MLB and other leagues continue to change the rules of the game, the leagues, teams, and players can all benefit from another approach to understanding those effects. 

9 

# **Tables** 

_Table 1._ Two-by-two DID analysis for the effect of the shift ban in 2023, comparing left-handed and right-handed batters’ BABIP and OBP with the bases empty for 2023 vs. 2022. Data source: FanGraphs Splits Leaderboard (29). 

|**Batter**||**BABIP**|||**OBP**||
|---|---|---|---|---|---|---|
|**Handedness**|**2022**|**2023**|**_Difference_**|**2022**|**2023**|**_Difference_**|
|**LHB**|0.275|0.287|_0.012_|0.299|0.315|_0.015_|
|**RHB**|0.291|0.294|_0.003_|0.303|0.309|_0.006_|
|**_Difference_**|_-0.016_|_-0.007_|_0.009_|_-0.004_|_0.006_|_0.009_|



_Table 2._ Shift rates in 2022 and estimated effects of the shift ban in 2023 on OBP, OPS, and wOBA, with associated placebo test p-values, for players with at least an 80% shift rate in 2022 and at least 250 PAs in each of the 2021–2023 seasons. Data sources: Baseball Savant’s Statcast Custom Leaderboard (32) and Statcast Batter Positioning Leaderboard (33). 

||**Shift Rate**|**OB**|**P**|**OP**|**S**|**wOB**|**A**|
|---|---|---|---|---|---|---|---|
|**Player**|**(2022)**|**Est.**|**P**|**Est.**|**P**|**Est.**|**P**|
|Corey Seager|96.5%|0.075|0.017|0.269|0.017|0.089|0.017|
|Joey Gallo|95.6%|-0.001|0.967|0.037|0.617|0.018|0.550|
|Kyle Tucker|94.5%|0.043|0.150|0.095|0.217|0.038|0.183|
|Yordan Alvarez|92.5%|0.015|0.483|0.214|0.017|0.083|0.017|
|Seth Brown|92.2%|-0.026|0.300|-0.029|0.650|-0.018|0.550|
|Kyle Schwarber|91.9%|0.018|0.433|0.061|0.433|0.026|0.333|
|Max Kepler|91.7%|0.024|0.317|0.096|0.217|0.044|0.117|
|Shohei Ohtani|91.7%|0.076|0.017|0.241|0.017|0.083|0.017|
|Cody Bellinger|91.6%|0.041|0.167|0.130|0.100|0.047|0.117|
|Brandon Lowe|90.6%|0.019|0.400|0.078|0.350|0.033|0.233|
|Anthony Rizzo|90.5%|-0.005|0.783|-0.050|0.483|-0.013|0.667|
|Max Muncy|89.7%|0.005|0.800|0.004|1.000|-0.005|0.850|
|EddieRosario|88.5%|0.001|0.967|0.001|1.000|0.003|0.950|
|Brandon Belt|87.6%|0.044|0.133|0.115|0.167|0.047|0.117|
|Cavan Biggio|86.5%|0.015|0.483|0.030|0.650|0.020|0.500|
|Rowdy Tellez|84.8%|-0.025|0.300|-0.073|0.350|-0.019|0.533|
|Matt Olson|84.5%|0.075|0.017|0.222|0.017|0.085|0.017|
|Josh Naylor|84.2%|0.031|0.267|0.136|0.083|0.047|0.117|
|Mike Yastrzemski|83.5%|0.009|0.683|0.096|0.217|0.035|0.200|
|Eugenio Suárez|83.0%|0.002|0.917|-0.078|0.350|-0.024|0.400|
|José Ramírez|81.8%|0.058|0.050|0.109|0.200|0.046|0.117|
|Daniel Vogelbach|81.2%|0.001|0.983|0.013|0.900|-0.039|0.150|
|Joc Pederson|81.0%|0.024|0.317|-0.006|1.000|0.001|0.983|
|Byron Buxton|80.4%|-0.022|0.333|0.085|0.267|0.020|0.517|
|Carlos Santana|80.2%|-0.004|0.817|0.028|0.667|0.006|0.800|
|Jorge Soler|80.0%|0.021|0.333|0.081|0.300|0.028|0.300|



10 

# **References** 

1. Pennington B. _New York Times_ . 2018 [cited 2024 Sep 3]. The N.F.L.’s New Tackling Rule: The Good, the Bad and the Confusing. Available from: https://www.nytimes.com/2018/09/10/sports/nfl-new-tackling-rule.html. 

2. Sullivan B. NPR. 2024 [cited 2024 Sep 3]. Kickoffs will look radically different in the NFL next year. Here’s how and why. Available from: https://www.npr.org/2024/03/27/1241203861/nfl-new-kickoff-rule. 

3. Marks B. ESPN. 2023 [cited 2024 Sep 3]. How the NBA’s new rules on resting stars will work. Available from: https://www.espn.com/nba/story/_/id/38386013/how-nba-new-rulesresting-stars-work. 

4. Doolittle B. ESPN. 2022 [cited 2024 Sep 3]. MLB’s universal DH is here: What it means-and doesn’t mean--might surprise you. Available from: https://www.espn.com/mlb/insider/story/_/id/33361880/mlb-universal-dh-here-means-meansurprise-you. 

5. Kennedy-Shaffer L. Baseball’s natural experiment. _Significance_ . 2022;19(5):42–5. 

6. Mains R. The 2023 rules changes: It’s not that simple. In: _Baseball Prospectus 2024: The Essential Guide to the 2024 Season_ . United States: Baseball Prospectus; 2024. p. 5–8. 

7. Craig P, Katikireddi SV, Leyland A, Popham F. Natural experiments: An overview of methods, approaches, and contributions to public health intervention research. _Annu Rev Public Health_ . 2017;38(1):39–56. 

8. Basu S, Meghani A, Siddiqi A. Evaluating the health impact of large-scale public policy changes: Classical and novel approaches. _Annu Rev Public Health_ . 2017;38(1):351–70. 

9. Cunningham S. _Causal Inference: The Mixtape_ . New Haven, CT: Yale University Press; 2021. 

10. Huntington-Klein N. _The Effect: An Introduction to Research Design and Causality_ . Boca Raton, FL: CRC Press; 2022. 

11. Card D, Krueger A. Minimum wages and employment: A case study of the fast food industry in New Jersey and Pennsylvania. _Am Econ Rev_ . 1994;84(4):772–93. 

12. Abadie A, Diamond A, Hainmueller J. Comparative politics and the synthetic control method. _Am J Polit Sci_ . 2015;59(2):495–510. 

13. Cowger TL, Murray EJ, Clarke J, Bassett MT, Ojikutu BO, Sánchez SM, et al. Lifting universal masking in schools — Covid-19 incidence among students and staff. N Engl J Med. 2022 Nov 24;387(21):1935–46. 

14. Kennedy-Shaffer L. Quasi-experimental methods for pharmacoepidemiology: difference-indifferences and synthetic control methods with case studies for vaccine evaluation. _Am J Epidemiol_ . 2024;193(7):1050–8. 

11 

15. Caniglia EC, Murray EJ. Difference-in-difference in the time of cholera: A gentle introduction for epidemiologists. _Curr Epidemiol Rep_ . 2020;7(4):203–11. 

16. Abadie A. Using synthetic controls: Feasibility, data requirements, and methodological aspects. _J Econ Lit_ . 2021;59(2):391–425. 

17. Pyun H. Exploring causal relationship between Major League Baseball games and crime: a synthetic control analysis. _Empir Econ_ . 2019;57(1):365–83. 

18. Bradbury JC. Does hosting a professional sports team benefit the local community? Evidence from property assessments. _Econ Gov_ . 2022;23(3–4):219–52. 

19. García Bulle B, Shen D, Shah D, Hosoi AE. Public health implications of opening National Football League stadiums during the COVID-19 pandemic. _Proc Natl Acad Sci_ . 2022;119(14):e2114226119. 

20. Kobierecki MM, Pierzgalski M. Sports mega-events and economic growth: A synthetic control approach. _J Sports Econ_ . 2022;23(5):567–97. 

21. Suggs W, Monday AB, May-Trifiletti J, Hearn JC. Institutional effects of adding football: A difference-in-difference analysis. _Res High Educ_ . 2024;65(6):1243–68. 

22. Cisyk J. Impacts of performance-enhancing drug suspensions on the demand for Major League Baseball. _J Sports Econ_ . 2020;21(4):391–419. 

23. Brook SL. General admission alcohol availability at American college football bowl subdivision stadiums: A difference-in-difference with timing variation analysis of football program concession revenues and ticket sales. _Int J Sport Finance_ . 2022;17(3):154–64. 

24. Cardazzi A, Rodriguez Z. Demand for offense: Designated hitters and MLB attendance. _Appl Econ_ . 2024;1–14. 

25. Carleton RA. _The Shift: The Next Evolution in Baseball Thinking_ . Chicago, Illinois: Triumph Books; 2018. 

26. Petriello M. MLB.com. 2018 [cited 2024 Sep 3]. 9 things you need to know about the shift. Available from: https://www.mlb.com/news/9-things-you-need-to-know-about-the-shiftc276706888. 

27. Carleton RA. Baseball Prospectus. 2018 [cited 2024 Sep 3]. Baseball Therapy: How To Beat The Shift. Available from: https://www.baseballprospectus.com/news/article/40088/baseballtherapy-how-beat-shift/. 

28. Pavitt C. Plummeting Batting Averages Are Due to Far More Than Infield Shifting, Part One: Fielding and Batting Strategy. Baseb Res J [Internet]. 2024;(Spring 2024). Available from: https://sabr.org/journal/article/plummeting-batting-averages-are-due-to-far-more-than-infieldshifting-part-one-fielding-and-batting-strategy/. 

29. Splits Leaderboard [Internet]. https://www.fangraphs.com: FanGraphs; 2024 [cited 2024 Aug 29]. Available from: https://www.fangraphs.com/leaders/splits-leaderboards. 

12 

30. Arthur R. Baseball Prospectus. 2022 [cited 2024 Sep 5]. The Shift Ban Won’t Work. Available from: https://www.baseballprospectus.com/news/article/77323/moonshot-the-shiftban-wont-work/. 

31. Carleton RA. Baseball Prospectus. 2022 [cited 2024 Sep 5]. Should They Just Shift Anyway? Available from: https://www.baseballprospectus.com/news/article/77778/baseball-therapyshould-they-just-shift-anyway-shift-mlb-rules-changes/. 

32. Statcast Custom Leaderboard [Internet]. https://baseballsavant.mlb.com: MLB Baseball Savant; 2024 [cited 2024 Sep 5]. Available from: https://baseballsavant.mlb.com/leaderboard/custom. 

33. Statcast Batter Positioning Leaderboard [Internet]. https://baseballsavant.mlb.com: MLB Baseball Savant; 2024 [cited 2024 Aug 29]. Available from: https://baseballsavant.mlb.com/visuals/batter-positioning. 

34. Petriello M. MLB.com. 2023 [cited 2024 Sep 3]. With no more shift, look for this player to rake. Available from: https://www.mlb.com/news/how-corey-seager-can-benefit-from-newshift-rules. 

35. Corey Seager [Internet]. https://www.baseball-reference.com/players/: Baseball Reference; 2024 [cited 2024 Sep 3]. Available from: https://www.baseballreference.com/players/s/seageco01.shtml. 

36. Petriello M. MLB.com. 2023 [cited 2024 Sep 3]. Here’s who has been helped (or hurt) by the shift limits. Available from: https://www.mlb.com/news/players-helped-or-hurt-by-shiftlimits-in-2023. 

37. Petriello M. MLB.com. 2023 [cited 2024 Sep 3]. No more shift could mean quite a few more hits for these batters. Available from: https://www.mlb.com/news/hitters-likely-to-beaffected-by-shift-ban. 

38. Carleton RA. Baseball Prospectus. 2022 [cited 2024 Sep 5]. How the Shift Ban Could Go Wrong. Available from: https://www.baseballprospectus.com/news/article/79083/baseballtherapy-new-shift-rules-2023/. 

39. Carleton RA. Baseball Prospectus. 2023 [cited 2024 Sep 5]. The Afterlife of the Shift. Available from: https://www.baseballprospectus.com/news/article/83984/baseball-therapythe-afterlife-of-the-shift/. 

40. Lindbergh B, Arthur R. The Ringer. 2021 [cited 2024 Sep 3]. MLB Just Tried a Bunch of Experimental Rules in the Minors. How Well Did They Work? Available from: https://www.theringer.com/mlb/2021/10/21/22736400/experimental-rules-atlantic-leaguerobo-umps. 

13 


