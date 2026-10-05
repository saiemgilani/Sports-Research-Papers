<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - The Contract Effect Why NHL Players Perform Differently When Money Is on the Line - Palisin.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/the-contract-effect-why-nhl-players-perform-differently-when-money-is-on-the-line/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Vanessa Palisin -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

The Contract Effect: Why NHL Players Perform Differently When Money Is on the Line

ABSTRACT Literature has shown that athletic performance fluctuates across the years of a long-term contract [1] [2] [3]. This variability may be attributed to a range of factors, both uncontrollable – such as injuries, mid-season adjustments, or unforeseen complications – and controllable, like opportunistic behavior. Players are incentivized to perform at their highest level in pursuit of a long-term, lucrative contract; After this is signed and official, certain players may exhibit a tendency to experience diminished motivational incentives to keep pursuing their all [1]. This phenomenon is commonly referred to as strategic and shirking behavior [3]. Building upon Rosen and Sanderson’s (2001) marginal revenue product model [2], more research is needed to determine whether player compensation accurately reflects player performance over the entire contract cycle. This study focuses on the National Hockey League (NHL), which Bruggink and Williams (2011) heavily analyzed [3]. Bruggink and Williams found significant increases in offensive contributions just before free agency status. With statistically significant data indicating short-term statistical spikes, the research also found performance often regressed to prior levels once contract deals are solidified. All in all, this study found that players produced approximately 5.6 fewer production units, representing a statistically significant decline relative to projected trends. Understanding these behavioral patterns is critical for teams and general managers seeking to optimize contract structures, mitigate moral hazard, and align incentives with long-term organizational goals.

## INTRODUCTION

## Introduction

The theory that multi-year contracts inspire athletes to alter the amount of effort exerted over a contract cycle was not developed simply based on presumptions. One study, conducted by Maxcey et al. (2002), detailed the concept of opportunistic behavior, or more specifically, strategic and shirking behavior [1]. This terminology substantiates contract theory (CY) by elucidating possible worker – or athlete – behaviors that are formed under circumstances of asymmetric information.

Because a player seeks to enhance his perceived value in the year preceding free agency eligibility, he is incentivized to increase his effort, thereby improving his performance [1]. This is noted as “strategic behavior.” Conversely, after a player commits to a multi-year contract, he potentially loses the same incentive that he once sought, moreover prompting a decrease in effort. This “shirking behavior” causes overall diminished productivity. This study relies on the notion that performance generates more fruitful contracts, making it highly relevant to many ongoing discussions of CY analyses.

The foundation for understanding further analyses of CY is rooted in traditional economic theories involving production and incentive alignment. Alchian and Demsetz define the mark of a capitalistic society as resources being owned and allocated by nongovernmental organizations such as firms, households, and markets [12]. Entity owners can apply their available resources as they see fit, thus increasing productivity through specialization and facilitated cooperation. However, as the paper describes, when two men jointly lift heavy cargo into trucks it is impossible to determine each person’s marginal productivity [12]. Team production is solely measurable by observing the team’s total output, and by definition, is not a sum of separable outputs of each of its members.

Free-riding – the process of an individual benefiting from something without expending much effort or paying for it [13] – then becomes a concern. In terms of athletics, if a player gains fame and benefits from a team’s success without exerting an equal level of effort as his teammates, he is effectively manipulating the team and taking advantage of the sports system for personal fulfillment. To counterbalance these actions, organizations need to create incentive systems that motivate players to keep pushing their limits. By aligning both individual and team goals, a person in the system is less likely to slack off and abandon their duties, therefore maximizing production.

This study identified a research gap with academic papers covering the contract year effect in the NHL in addition to the lack of use of machine learning. This study aimed to:

1)​ Examine how player performance varies during contract years compared to preceding seasons

2)​ Identify the key performance indicators that most strongly predict production value in a contract year

3)​ Assess the effectiveness of machine learning statistical models in explaining and predicting contract-year outcomes

As a way of monitoring player performance, this study collected a range of NHL free-agent statistics for two years prior to a new contract, the initial contract year, and then two years after the contact year. For each of the five variables of interest, univariate linear regressions were completed and explored individually to examine the relationship between this metric and player performance. This was important as it provided the “best” environment for measuring player performance. After performing a multivariate regression with the statistically significant features, this information was then used to complete a backward stepwise regression analysis. This provided the final model which could be employed to provide insights on player fulfillment.

Some variables were further removed to account for variable insignificance and multicollinearity. The multivariate regression model was then recalibrated, indicating the optimum terms for an ANOVA analysis.

Production was selected to be the most competent figure for measuring overall player output, so it was therefore used in a machine learning algorithm process. ESPN defines this as “the average ice time per point recorded” [15]. Because this metric reflects how efficiently players generate points relative to their total ice time, a lower production value indicates a player mandates less time to contribute to the team. The formula is listed below:

𝑃𝑟𝑜𝑑𝑢𝑐𝑡𝑖𝑜𝑛 𝑉𝑎𝑙𝑢𝑒 =

𝑇𝑜𝑡𝑎𝑙 𝐼𝑐𝑒 𝑇𝑖𝑚𝑒 𝐺𝑜𝑎𝑙 𝑃𝑜𝑖𝑛𝑡𝑠 + 𝐴𝑠𝑠𝑖𝑠𝑡 𝑃𝑜𝑖𝑛𝑡𝑠

This found the optimum algorithm model to learn patterns from each player’s first two years of data and predict their expected performance during the contract year (t0). These predicted values were then compared to the actual t0 performance, and the residuals were inspected to determine over- or under-performance.

## Literature Review

Building on the economic foundation of the CY phenomenon, Rosen and Sanderson (2001) introduced the marginal revenue product (MRP) model [2]. Because the demand for labor is derived from the demand for the ultimate goods/services that the labor is used to produce, customers are willing to pay an elevated price for higher quality products [2]. In this scenario, the products are professional athletes, and the economic output is their individual performance. Today’s sports culture allows for a plethora of data on athletic production, so it is one of few cases where the marginal product of a player can be investigated directly [2]. The study then continued to detail how contract salaries should reflect a player’s contribution to team revenue. In other words, the sports organization is paying an appropriate price for the amount of output that is to be produced.

Through qualitative case studies, Rosen and Sanderson also highlighted how veteran leadership and consistent line pairings (i.e. playing with the same group of players on the field, court, or ice) support better individual and team outcomes [2]. One can analyze athletic statistics for long periods of time, but there are many factors, such as organizational culture, playing tactical systems, and overall team depth/structure, that cannot be summarized in a quantitative form. For instance, a free agent joining a new team may experience increases or decreases in productivity depending on the influence of surrounding players. Although year-to-year statistics can reveal certain trends, they cannot account for all environmental effects impacting a player. Therefore, this study is particularly relevant for understanding the role of performance-based incentives and the economic trade-offs between rewarding past performance and managing future risk [3].

Extensive research has been conducted in other professional and emerging sports leagues, including the National Basketball Association (NBA), NCAA March Madness, and Major League Baseball (MLB).

Stiroh (2007) found evidence of strategic behavior when analyzing the 1988-2002 NBA. This paper sought to examine whether multi-year contracts caused players to alter their effort over a contract cycle [3]. Agreeing with the previously defined opportunistic behavior terminology, Stiroh hypothesized that players would perform above average levels in the year prior to free agency, but then perform below average levels in the subsequent years after signing a contract. This study’s results postulated that a one point increase in a player’s scoring average was associated with an annual salary increase exceeding $300,000 [4]. Results such as this were backed by two theories: (1) asymmetric information and (2) moral hazard.

First, although a player might maintain elevated levels of effort during games because of the high visibility, competitiveness, and media presence of professional sports, this does not guarantee the same level of effort during off-season conditioning or in-season practice. These areas lack the immediate incentives present in game-day environments, and performance often is difficult to monitor. Second, a player might act differently when he is protected against losses. In order to secure a highly pursued contract, players will maximize their effort to then magnify their personal gains; Once the contract is finalized, however, the same player might no longer have the incentive to maintain that level of effort, having already achieved the desired outcome [4]. So even if performance declines, the player continues to receive a certain percentage of the agreed-upon compensation. This reasoning also illustrates the importance of contract length: Longer contracts provide more opportunity for a player to underperform relative to his salary.

Jean (2010) drew on Stiroh’s (2007) framework to examine strategic/shirking behavior in the NBA, employing player efficiency – an advanced performance metric – as the dependent variable [3]. This form of statistics can better evaluate player performance when compared with basic fields (i.e. points, assists, penalties, etc.). This study found evidence of strategic and shirking behavior, while Strioh only found strategic [6]. This difference can be attributed to the use of advanced statistics.

Sen and Rice (2011) examined how being in the final year of a contract influenced player performance in the NBA. Often referred to as the “agency problem,” the principal–agent problem refers to the conflicts in interest and priorities that arise when one entity (the "agent") takes actions on behalf of another person or entity (the "principal") [5]. This paper created a three-period, principal-agent game between the team, which is risk neutral, and the player, who is risk averse [3]. The player must then choose how much effort he is willing to exert during each period of the game. The main driver behind this decision derives from the ability to affect future wages, because the current period wage is pre-negotiated and already set [3]. A team can then evaluate the level of output and compensate the player in his next contract (either a one- or two-period contract).

Sen and Rice (2011) found that when a team rewarded a player with a two-period contract, effort increased over the span of the contract, therefore increasing performance in period two when compared with period one [3]. The authors conclude that this is because of players “discounting the future.” Contract expiry is imminent in period two, so in order to secure a contract for period three, the player must exert more effort. One might note that players would exert their maximum amount of effort with single-period contracts, for this motivates players throughout each individual period. Although this would be the prime option for all teams, players are risk averse and place a high value on security [3]. Thus, players will sacrifice a given amount of compensation in return for longer guaranteed contracts.

Although this study supported the notion that the largest decreases in player effort occur during the early years of a long-term contract, and that effort increases as contract expiration approaches, it did not account for other factors that might motivate a player later in his career other than future wages. One prime example of this is winning a championship. Whether that be winning a Super Bowl, World Series, or Stanley Cup, some players consider such achievements to be more valuable than any monetary compensation a contract could provide. NBA player David West opted out of a $12.6 million contract with the Indiana Pacers to then sign with the San Antonio Spurs for a mere $1.6 million [3]. Over a decade of play, West earned nearly $87.5 million, yet he never won a championship. This also creates a stipulation that teams would rather allocate funds to younger players who have the potential to be productive for a longer amount of time than older players, who might have less incentive to perform at such a high level [3].

Ichniowski and Preston (2012) examined how a player’s historical performance compared with his final contract year performance in assessing whether performance in the NCAA “March Madness” tournament influences draft status. Amongst the extensive literature explaining biases and heuristics utilized by executives to make draft decisions, Ichniowski and Preston juxtaposed the concepts of “availability heuristic” and “slow thinking” [3]. The idea that decisions are modified by the most recent, vivid, and dramatic memories aligns with the concept of the “availability heuristic,” which is particularly relevant given that March Madness is the final major competition before the NBA draft [7]. Conversely, the study acknowledges that executives have several months to make draft decisions, and this relates more to the “slow thinking” concept [7]. Relating this to the contract year phenomenon, players might engage in opportunistic behavior and elevate their performance during high-visibility times – such as March Madness – to maximize their possible performance value. Executives, being susceptible to decision-making biases, offer inflated contracts based on short-term surges rather than long-term dependability.

MLB has served as a primary research source for many years due to the structure of the game allowing researchers to isolate and measure individual player performance, or in other words manipulate specific variables, and control for the unwanted static effects of other factors. Ahlstrom, Si, and Kennelly (1999) used seasonal data from 1976-1992 and found significant results of opportunistic behavior in player performance and MLB contracts [3]. One statistic that attracts attention is the decline in performance for batting average, which was estimated to be approximately 0.14 percentage points in the year after the initial contract season [8]. This figure may seem minute, but considering that a decent batting average in 1992 hovered around .256 [10], a drop of 0.14 constitutes a significant decline. Not to mention, the results also indicated that players who signed long-term contracts (amount of time was not specified) spent fifty percent more time on the disabled/injured list [8].

A limitation of this study is that it was conducted nearly three decades ago, but Mark White and Kennon Sheldon (2014) found similar results in their study. Applying ANOVA methods, this study also found that players underperformed in post-contract years compared to their performance in contract years [9]. The analysis of three year time trends (before contract year, contract year, and after contract year) revealed a decline in batting average, home run, slugging percentage (hitting power), and on-base percentage to levels below pre-contract years [9].

While much research has been conducted centering around the NBA and MLB, researchers have only recently started dabbling into the National Hockey League (NHL). Fort (2018) is said to offer one of the most comprehensive examinations of salary dynamics in professional sports, with focus in the NHL [3]. While the information is not heavily research-driven (i.e. statistic heavy), it is nonetheless crucial for framing the broader context of the NHL environment and understanding the factors that shape salary outcomes.

Fort (2018) found that while players often receive higher initial salaries following strong contract year performances, the sustainability of the salary boost varies significantly depending on player position, career longevity, and market context [3]. This is to be expected as each position carries specific responsibilities, injuries can significantly affect a player’s “prime” years, and team structures and dynamics are connected to every statistical output on which salaries are often based. Fort later emphasized that because teams overcompensate based on inflated contract-year statistics, large financial distortions arise and lead to inefficient salary cap allocation and long-term payroll challenges [3]. Contracts are based on expected performance value, and when the current statistics are not indicative of consistent performance, teams are led astray.

On a team-by-team basis, the presence of star players and the strategic priorities of the organization are major sources of distortion in evaluating individual player salary outcomes. Fort (2018) argued that star players – such as the Edmonton Oiler’s Connor McDavid and Leon Draisaitl – could significantly increase team revenue through consistent game attendance and media exposure [3]. As a result, the Oilers’ headliners gain more visibility while growing their reputations, often translating into higher salaries or trade value. The study further found that players in possession-heavy systems experienced inflated offensive metrics when compared to those emphasizing forechecking [3]. This could be attributed to many other factors, namely the preference for high-scoring games, but it also underlines how players can become easily undervalued during negotiations.

Fort (2018)’s results aligned those of Bruggink and Williams (2011), who documented significant increases in offensive contributions (i.e. goal scoring and shot attempts) preceding free agency when analyzing NHL contract year surges [3]. Illustrating a strong correlation between impending negotiations and short-term statistical spikes, their analysis featured the consistent, incentive-based phenomenon across professional athletics. Not only did player performance often regress once long-term contracts were secured, players in structured systems were also more likely to benefit from high quality scoring chances, both of which boost players’ impending valuations [3].

Fort (2018) highlighted the growing importance of context-adjusted metrics and noted that incorporating advanced metrics further transforms how teams evaluate contract value [3]. Scoring a goal against recent double-Stanley Cup champions, the Florida Panthers, is far more difficult than against the under-.500 San Jose Sharks. Yet, if a player scored one goal against each team, the ledger would record two goals; This system is static and does not account for the skill level of the opponent. Hence, the need for more context-adjusted metrics like Corsi and Fenwick (number of shot attempts) and Expected Goals or xG (probability of a shot becoming a goal). Gustafson and Hadley (2017) used similar metrics to build predictive models that estimated future value, motivating teams to base contracts on anticipated output rather than past performance [3]. Their results support the idea that teams employing strategic forecasting and team-specific, context-adjusted statistics can more effectively influence contract decisions (who and for what amount). In the end, this will lead to player compensation that is better aligned with projected performance rather than historical statistics.

Contract theory is becoming increasingly discussed across the sports industry, and all of the cross-league research previously mentioned strengthens the argument that the contract year phenomenon is a consistent, incentive-based issue across multiple different athletic organizations.

This research will primarily center on the NHL, which as previously mentioned, is less studied when compared to professional sports. Interestingly enough, NHL viewership is steadily increasing, while NBA followership is decreasing. One article observed that following the NHL 4 Nations Faceoff (featuring Canada, the United States, Finland, and Sweden), many fans took to social media to complain that NBA players should demonstrate more heart, care, and pride in their performance – similar to what they saw from NHL players [11]. The NHL continues to grow and adapt, paying close attention to what fans want from their coveted hometown teams. This receptiveness is admirable, particularly today when professional sports often function more as an industry than a pastime.

In the discussion of today’s culture, it is vital to recognize the extent to which professional athletes are idolized. Teachers, healthcare and social workers, airline pilots, and other everyday professionals – who arguably have a greater impact on society – are often paid far less than professional athletes. Although athletics play a central role in American culture, the disparity of a teacher’s and professional athlete’s contract salary is astonishing. If teams are paying this high proportion of money, they should at least be compensated with adequate playing effort and results. This study hopes to highlight common areas of player overvaluation and identify specific instances where contract-year performance does not align with long-term output.

One benefit of this research is its ability to address the limitations of prior studies by incorporating both traditional (i.e. goals, assists, time on ice…) and advanced performance metrics (i.e. expected goals, Corsi score, Fenwick score…). This combination of features is likely to increase the likelihood of obtaining statistically significant results. In addition, with the help of Python and Machine Learning, the methodology process can be done in an efficient and effective manner.

## METHODOLOGY

The Data

In this study, data was gathered from four locations: [14] PuckPedia, [15] ESPN or Entertainment and Sports Programming Network, [16] Hockey Reference, and [17] MoneyPuck.

PuckPedia compiles NHL signings and various trade transactions from multiple licensed sources including the official teams involved, NHL announcements, and/or reliable public transaction reports. Before releasing and updating their official records, PuckPedia matches and aggregates the various sources of information to then build contract entries. This, henceforth, allows the website to be regularly, and often in real-time, updated as signings are announced. Founder Hart Levine oversees this website after being inspired by many sites who pioneered the trail of providing valuable and interesting content to hockey fans around the world.

ESPN – one of the most utilized primary sources of athletic statistics and performance data – provides a comprehensive overview of what is occurring in the NHL industry. From top headlines, daily scoreboards, must-see moments (i.e. game highlights), Fantasy Hockey tips and tricks, to trending topics off the ice, ESPN was a crucial source of data for this study. Similarly to PuckPedia, ESPN is constantly updated, with real-time scores and news during live games. This allows not only the team statistics to be highly accurate, but also allows site-users to see individual players’ statistics. This feature is immensely useful. ESPN is jointly owned by The Walt Disney Company (80%) and Hearst Communications (20%) through a joint venture called ESPN, Inc.

Hockey-Reference, part of Sports Reference, LLC, aggregates historical box scores, game logs and compiled season/player totals. Using licensed datasets like Dan Diamond and Associates, this source functions as a family of sports databases maintained by both staff and volunteer contributors who correct and update historical records. The core data from every completed game is updated daily, and although not as efficient as the previously cited sources, the official data is processed shortly after every game and season.

Unlike the previously mentioned websites, MoneyPuck is a website specifically designed to specialize in advanced hockey analytics. Known for its predictive models, data visualizations, and metrics like Expected Goals (xG), it provides a range of hockey-related statistics, including live in-game win probabilities, power rankings, and playoff odds. This was employed in the study in order to capture a more comprehensive measure of player performance beyond traditional or basic statistics. Advanced metrics, such as expected goals and possession-based indicators, provide deeper insight into a player’s on-ice impact. Including these statistics helps control for external factors like team strength, allowing for a more accurate assessment of how performance influences contract values (i.e. production not due to luck but rather individual player performance). MoneyPuck was created and is currently maintained by Peter Tanner – site founder and creator – and the MoneyPuck team.

Players who met the following criteria were included in this study’s dataset:

Quality

Reason as to Why

Skaters only (goalies excluded)

Goaltenders’ performance metrics differ substantially from skaters

Signed contracts during the 2013–2025 Collective Bargaining Agreement (CBA) era

Ensures consistency in league-wide contract regulations, salary cap limits, and negotiation standards across all observations

Contract length ≥ 3 years

Ensures the sample includes established NHL players, reducing the likelihood of including players who briefly reach the league and then decline or exit shortly after

No rows were eliminated based on average annual value (AAV), as removing those data points would have significantly reduced the sample size and lowered the statistical power of the analysis, making it more difficult to identify meaningful relationships between performance metrics and contract values.

For each player in the dataset, the contract signing year, total contract amount, and contract length were recorded. From these values, the Average Annual Value (AAV) was calculated by dividing the total contract amount by the number of years in the contract. To evaluate player performance in relation to contract outcomes, both basic and advanced performance statistics were collected for a five-year window surrounding each signing; Specifically, for the two seasons preceding the contract year, the contract year itself, and the two seasons following the signing. All features were recorded consistently across data sources, with contract variables derived from PuckPedia, basic statistics verified through ESPN and Hockey-Reference, and advanced metrics obtained from MoneyPuck. This structure allowed for a comprehensive analysis of player performance trends before and after signing a long-term contract.

The final dataset consisted of 278 players, totaling 1,390 observations across 29 variables. The appendix indicates variables utilized alongside a brief description. Players without complete data for any of the five observation years were excluded from the analysis. The following players were removed during this process:

Contract Year 2013

Player Nathan Horton

Stephen Weiss Ryane Clowe Matt Cooke Patrick Wiercioch Dave Bolland Mikhail Grabovski Stéphane Robidas

Nino Niederreiter Calvin de Haan

Reason for Removal No data for 2014–2015 and 2015–2016 seasons No 2015–2016 season No 2015–2016 season No 2015–2016 season No 2011–2012 season No 2016–2017 season No 2016–2017 season No data for 2015–2016 and 2016–2017 seasons No 2012–2013 season No 2012–2013 season

2015 2016 2017

2020 2021 2022

Joe Vitale Erik Condra Alexander Radulov

Martin Hanzal Matt Hunwick Tyler Pitlick Frederick Gaudreau

Ilya Kovalchuk

Sven Bärtschi Michael Grabner Thomas Hickey Ross Johnston Nick Seeler

Gustav Nyquist Jake Gardiner Micheal Ferland

Jake Bischoff

Vladislav Gavrikov Patrik Nemeth Tucker Poolman Johnny Gaudreau

No 2016–2017 season

No 2017–2018 season

No data for 2014–2015 and 2015–2016 seasons

No 2019–2020 season

No 2019–2020 season

No 2015–2016 season

No data for 2016–2017 and 2019–2020 seasons

No data for 2016–2017, 2017–2018, and 2020–2021 seasons

No 2020–2021 season

No 2020–2021 season

No 2019–2020 season

No 2016–2017 season

No data for 2016–2017 and 2020–2021 seasons

No 2020–2021 season

No 2020–2021 season

No data for 2020–2021 and 2021–2022 seasons

Only played 2019–2020 season (missing 4 other years)

No 2018–2019 season

No 2023–2024 season

No 2023–2024 season

No 2024–2025 season

Throughout 2013-2025 Throughout 2013-2025

Alexander Wennberg Joseph Anderson

Unavailable Advanced Stats for 1+ seasons

Unavailable Advanced Stats for 1+ seasons

Preliminary Analysis

An initial correlation analysis was conducted to identify overarching data trends, followed by the creation of a heatmap to visually illustrate these relationships. Prior to developing the final machine learning model, the relationship between each independent variable and the five dependent variables was examined. This exploratory phase involved conducting a series of univariate regression models to assess the strength and direction of relationship between each feature and outcome variable of interest. Specifically, five dependent variables – Production, Expected Goals per 60 Minutes, On-Ice High Danger Shot Attempts per 60 Minutes, Takeaways, and Games Played – were analyzed individually against all independent variables. A Python for-loop was created to store the results in a new data frame to accomplish this for each dependent variable.

Although univariate regression is not fully sufficient to explain the primary drivers of performance, it serves as an important first step in identifying statistically significant features and understanding their correlations with each dependent variable. This process helped determine which variables had the most meaningful relationships with each outcome and provided a foundation for variable selection in subsequent modeling. Each univariate regression used a 95% confidence interval, with a p-value below 0.05 indicating statistical significance.

Following the univariate analyses, multivariate regression models were developed to identify the combination of statistically significant features alongside each dependent variable. In other words, only variables that demonstrated statistical significance in the univariate regressions were included in further phases.

Constructing the Final Models

In order to achieve the best possible subset of variables that influenced the outcome measure of each model, stepwise regression was employed. This tool allows the researcher to evaluate different model combinations without having to manually compute each calculation. This also produces the sets of independent variables that have the highest degree of influence on the dependent variable of interest. While one can complete this process using R-squared, this study wanted to avoid overfitting and, thus, employed Akaike Information Criterion or AIC to determine the fit of the model. While R-squared constantly increases with more variables, AIC penalizes the model for taking on too many variables, thereby deterring the model from becoming overly complex.

When applied to this study, the procedure is to search for the set of independent variables that will minimize the AIC value of the overall model while also trying to simplify the model as much as possible. There are two separate ways to approach a stepwise model: Forward and Backward. Forward stepwise models start with the most significant independent variable and then sequentially attempt to add one variable at each step. If the added variable hurts overall performance, it will not be included. Once the variable is added, the model is reevaluated to ensure all variables are still significant; Any that are deemed insignificant, are then dropped. On the other hand, backward stepwise regression begins with a single, large model that contains all independent variables. It then goes through and removes the least significant variable. The model selects the variable whose removal reduces the AIC the most, and if it benefits the model, the variable is then removed entirely.

The backward stepwise regression approach was employed, using the AIC as the selection criterion. A second backward stepwise regression was conducted in Python using R-squared as the selection criterion instead of AIC. This approach retained a larger set of features, which increased the model’s complexity. Two approaches were used to verify consistency and the robustness of Python’s modeling capabilities with AIC:

(1)​Manual Backward Elimination (using statsmodels) Beginning with all significant variables, each feature was temporarily removed, and the resulting AIC was computed. The feature whose removal produced the largest AIC reduction was eliminated from the model.

(2)​Automated Backward Elimination (using mlxtend’s SequentialFeatureSelector) A custom AIC scoring function

Both methods produced identical results, confirming the stability of the selected features and the reliability of the AIC-based feature selection process.

After the models were constructed, the variance inflation factor (VIF) was computed for each independent variable. This was used in regression analysis to detect multicollinearity, or when two or more features in a model are highly correlated. High multicollinearity negatively affects the regression analysis as the coefficients become unstable and hard to interpret. It was deemed that any VIF coefficient greater than nine was removed from the model. The features left would, thus, not show high concern for multicollinearity and be suitable for inclusion in the appropriate model.

To assess whether player performance varied across two contract stages – pre-contract and post-contract – a repeated measures ANOVA was performed. This test compared mean performance metrics between the two periods (contract stages) while accounting for repeated observations of the same players. The F-statistic captured overall variance between stages, and follow-up T-tests identified which metrics differed significantly. Only variables showing statistically significant differences were retained.

Production was determined to be the most direct variable of interest due to its ability to dedicate uniqueness to each player and the relationship between performance and contact value. While the later stages of modeling focused primarily on production as the main dependent variable, the results from the other independent variables were incorporated into overall analysis to provide a broader understanding of player statistics (i.e. offensive, defensive, and other specific metrics).

Machine Learning: Production

This study’s final model aimed to predict t0 (contract year) production value statistics based on t-2 and t-1 (pre-contract years). Utilizing various machine learning methods, the dataset was divided into an 80/20 train-test split, and four models were developed. Two of these models were linear, and thus required scaling, while the other two were tree-based and did not require scaling. The linear pipeline implemented Ridge and Lasso regression with StandardScaler (selected scaling technique), and hyperparameters were optimized using GridSearchCV. The tree-based pipeline included Random Forest and XGBoost regressions, with GridSearchCV tuning parameters as well.

In order to make sure the best features were selected for an optimized model, this study implemented SelectKBest. This is a type of filter-based feature selection method in machine learning that relies on statistical measures to score and rank the features [18]. SelectKBest uses statistical tests such as chi-squared test, ANOVA F-test, and/or mutual information score to score and rank the features based on their relationship with the output variable of interest [18]. Then, it selects the K features (top number of features) with the highest scores to be included in the final feature subset. After evaluating model performance, the best-performing model was selected for residual analysis to compare predicted and actual production values at t0.

## RESULTS

Correlation Analysis

The preliminary correlation analysis revealed that production value in minutes is most positively associated with blocks (r = 0.40), followed by hits (r = 0.18) and age (r = 0.12). Conversely, the strongest negatively associated relationships are with variables such as expected_goals_per_60min (r = -0.63), shooting percentage (r = -0.59), and adjusted_expected_goals (r = -0.55). These results indicate that more defensive measures are positively correlated with production value in minutes, while offensive metrics are more negatively correlated with the dependent variable of interest. It was noted that the offensive variables performed stronger (i.e. closer to -1 rather than 0) due to production value being composed of points from goals and assists, both offensive features. The following heatmap was created from the preliminary correlation analysis.

The heatmap visually reinforces the results of the preliminary correlation analysis. This pattern highlights that defensive contributions are positively related to production efficiency, whereas offensive measures display stronger inverse relationships. This is attributed to their direct inclusion in the formula for production (i.e. variables are mathematically intertwined). Production Value In Minutes

Table 1 shows the results of the first set of regressions that were conducted on production value in minutes. Production value was converted to a consistent 60 minute format to allow for ease of interpretation. A for-loop was implemented in Python to efficiently run multiple simple linear regression models. This automated approach allowed each regression to be fit sequentially using Ordinary Least Squares (OLS), with key statistics such as the coefficient, p-value, R-squared, adjusted R-squared, and F-statistic stored in a results list. By iterating through all features, the process significantly reduced manual repetition and ensured consistency across models.

TABLE 1 Production Value in Minutes Univariate Regression Results

These models indicate that there are numerous (17/18) predictor variables with p-values less than 0.05. This demonstrates that these features are statistically significant and valuable to this study. The strongest features in terms of variance explained (R-squared) are expected_goals_per_60min (0.397), shooting_pct (0.345), and adjusted_expected_goals (0.306). These features each account for a measurable portion of the variance in production, detailing that they are meaningful and influential variables in explaining performance outcomes. Although one would consider an R-squared value over 0.70 to indicate a strong relationship, given the context of sports analytics where player performance is influenced by a high number of external factors, these R-squares values can still indicate a moderate level of explanatory power. The coefficient values describe how production changes when that feature increases, considering only that feature by itself. For example, the coefficient for hits (0.3119) indicates that, on average, each additional hit is associated with a 0.31 increase in production_value_in_min when analyzed independently. This positive and statistically significant relationship suggests that players who record more hits tend to have a slightly higher production value per minute. Penalty_minutes is not a significant variable of production and explains practically no variance in the dependent variable (R-squared value of approximately 0). This indicates that changes in penalty minutes have little to no relationship with production value, suggesting that this feature can be safely excluded from further analysis.

Table 2 presents the preliminary OLS multivariate regression results, which incorporates all statistically significant features identified in the univariate analysis alongside production value. This model evaluates how these variables collectively explain variation in production value, thereby providing a more comprehensive understanding of their combined effects on player performance.

TABLE 2 Production Value in Minutes Multivariate Regression Results

However, after employing backward stepwise regression analysis and accounting for each feature’s VIF to address multicollinearity, the following features and their corresponding VIF values were retained in the final model:

Feature expected_goals_per_60 min shooting_pct corsi ppg blocks takeaways games_played hits plus_minus_rating extension

VIF 3.343722 2.185177 1.889158 2.167643 2.592768 1.442033 1.985140 1.373780 1.139787 1.036835

The multivariate regression model was then refitted. Table 3 shows the results. TABLE 3

Production Value in Minutes Refitted Multivariate Regression Results

When compared to the initial results presented in Table 2, the refined model in Table 3 demonstrates improved efficiency and interpretability. Despite this reduction in variables, the model’s explanatory power remained virtually unchanged (R-squared of 0.513 compared to the initial 0.514). This indicates that the excluded features contributed minimal additional insight, but their removal also prevents the model from overfitting. The refitted model in Table 3 is simpler and captures the same amount of variance as the original model in Table 2 but with fewer and more meaningful features. The final regression model explains 51.3% of the variance in player production, indicating that just over half of the variation in production value in minutes is accounted for by the selected features. Several variables demonstrate significant relationships with production. Positive effects include ppg and hits, suggesting that players who score more points per game or record more hits experience small increases in production. Alternatively, several features display negative effects on production. Higher corsi values are strongly associated with lower production, therefore implying that possession-related metrics may be inversely related to overall production output. Similarly, players with greater expected_goals_per_60min, plus_minus_rating, takeaways, and games_played tend to have lower levels of production.

The constant value represents the baseline level of production for a player when all other predictors are held at zero. This was necessary to have in order to complete the regression in Python. Two features were found to be not statistically significant in the refitted model: (1) blocks and (2) extension. These will be removed for future analysis.

The ANOVA analysis was used to see how player performance changed across specific contract years, with the F-statistic showing how much variation occurred over time. These results are available in Table 4.

TABLE 4 Production Value in Minutes ANOVA Results

Several features showed significant differences, meaning player performance tended to shift throughout the contract cycle. Expected_goals_per_60min (F = 3.54) increased immediately before and after the contract year. This suggests players may improve their offensive efficiency when approaching a new deal, in addition to carrying this momentum into their initial contract year. On the other hand, hits (F = 11.77) dropped leading up to the contract year but rose again afterward. This could indicate changes in effort depending on how reserved the player wants to be before free-agent status.

Overall, these results show that player performance in the form of production value is not consistent across time.

Expected Goals per 60 Minutes Table 5 shows the results of the first set of regressions that were conducted on expected goals per 60 minutes. It captures how effectively a player generates scoring opportunities and does not take into account goals actually scored. In other words, if a player receives the option to shoot the puck at the goal, this is considered an expected goal, and it is adjusted accordingly given the odds of becoming a goal. For example, a rebound shot off the goal line may have a 50% of going in and be worth 0.5 expected goals, while a shot from the blueline – measured at 64 feet from the goal line – may be worth 0.01 expected goals.

TABLE 5 Expected Goals per 60 Minutes Univariate Regression Results

These models indicate that there are numerous (13/16) predictor variables with p-values less than 0.05. This demonstrates that these features are statistically significant and valuable to this study. The strongest variables in terms of variance explained (R-squared) are adjusted_expected_goals (0.606), shooting_pct (0.470), and production_value_in_min (0.397). Shooting adjusted expected goals being the stronger feature is logical due to the fact that it incorporates both shot quality and individual shooting ability. Calculated as Expected Goals × (1 + Shooting Talent Above Average), this is the number of goals a player is expected to score given their expected goals and their individualized shooting talent. For example, if hockey legend Alex Ovechkin and a new hockey prospect were shooting from the blue line, Ovechkin’s adjusted goals would be valued more due to his experience and precision. This, therefore, not only captures the quantity and quality of scoring opportunities, but also the likelihood of converting these actions into goals.

The coefficient for points per game (PPG, 5.65) indicates that, on average, each additional point per game is associated with a 5.65 increase in expected goals per 60 minutes when analyzed independently. This positive and statistically significant relationship suggests that players who generate more points per game also tend to create improved scoring opportunities. This is a reasonable relationship that demonstrates how actual scoring production and offensive efficiency are connected. Giveaways, plus_minus_rating, and penalty_minutes are not significant features due to their p-values being greater than 0.05. Explaining no variance in the dependent variable, they will be removed for future analysis.

Table 6 presents the preliminary OLS multivariate regression results, incorporating all statistically significant features identified in the univariate analysis alongside expected goals per 60 minutes.

TABLE 6 Expected Goals per 60 Minutes Multivariate Regression Results

However, after employing backward stepwise regression analysis and accounting for each feature’s VIF to address multicollinearity, the following features and their corresponding VIF values were retained in the final model:

Feature adjusted_expected_goals shooting_pct production_value_in_min ppg blocks

VIF 5.123666 2.167166 1.995753 3.014841 2.193627 corsi takeaways high_danger_shots_per_60min position games_played hits age fenwick

2.011669 1.536510 3.238733 1.108312 2.463169 1.377953 1.103064 3.094096

The multivariate regression model was then refitted. Table 7 shows the results.

TABLE 7 Expected Goals per 60 Minutes Refitted Multivariate Regression Results

When compared to the initial model presented in Table 6, the refined model in Table 7 demonstrates improved efficiency and interpretability. After applying backward stepwise regression and reviewing each variable’s VIF, two statistically insignificant features were removed. Despite this reduction in variables, the model’s explanatory power remained unchanged (R-squared of 0.858), indicating that the excluded features contributed minimal additional explanatory value. The refitted model therefore captures the same degree of variance in expected goals per 60 minutes while relying on fewer and more meaningful features, which prevents overfitting.

The final regression model explains approximately 85.8% of the variance in expected goals per 60 minutes. This reflects a very strong model fit with the selected features. Several variables show statistically significant relationships with expected goals per 60 minutes and overall offensive efficiency. Notably, adjusted_expected_goals and high_danger_shots_per_60min are positive variables, indicating that players with higher quality shot skills and more frequent high-danger opportunities while on the ice tend to generate higher expected goal rates.

Conversely, some features such as ppg, blocks, and games_played exhibit negative coefficients. This implies that players with higher point totals per game, more blocked shots, and/or more games may generate fewer expected goals per 60 minutes when controlling for other factors. The blocked shot and number of games played is reasonable, but the inverse relationship between points per games and expected goals per 60 minutes is intriguing.

The constant value represents the baseline level of production for a player when all other predictors are held at zero. This was necessary to have in order to complete the regression in Python. Two features were found to not be statistically significant in the refitted model: (1) corsi and (2) age.

The ANOVA analysis was used to see how player performance changed across different contract years, with the F-statistic showing how much variation occurred over time. These results are available in Table 8.

TABLE 8 (2 sections) Expected Goals per 60 Minutes ANOVA Results

Several features showed significant differences, meaning player performance tended to shift throughout the contract cycle. Adjusted expected goals exhibited one of the strongest patterns (F = 22.68), decreasing prior to the contract year and increasing significantly afterward. This demonstrates that players tend to generate higher-quality scoring opportunities following the signing of a new contract. Similarly, hits (F = 11.77) showed significant movement across the contract cycle, decreasing prior to the contract year and rising afterward. This pattern could suggest that players tend to engage in more physical game styles following the signing of a new contract. On the other hand, high-danger shots per 60 minutes (F = 16.84) declined across the entire contract cycle. This may indicate a decrease in the quantity of premium scoring chances over time.

Overall, these results show that player performance in the form of expected goals is not consistent across time.

On-Ice High Danger Shots per 60 Minutes

Table 9 shows the results of the first set of regressions that were conducted on on-ice high danger shots per 60 minutes. This metric measures unblocked shot attempts with a 20% or higher probability of resulting in a goal. This provides a standardized measure of how frequently a player generates premium scoring opportunities relative to skating time, emphasizing offensive pressure rather than actual goal-point outcomes. High-danger shots make up roughly 5% of all shot attempts and account for approximately 33% of total goals.

TABLE 9 On-Ice High Danger Shots per 60 Minutes Univariate Regression Results

These models indicate that there are numerous (13/18) predictor variables with p-values less than 0.05. This demonstrates that these features are statistically significant and valuable to this study. The strongest variables in terms of variance explained (R-squared) are fenwick (0.631), expected_goals_per_60min (0.083), and points_per_game (0.065). Fenwick being the strongest feature – not to mention the large difference between this and the second highest feature – is sensible as this measures the percent of all unblocked shot attempts the player's team gets while the player is on the ice compared to the other team. For example, if a player's team gets 6 unblocked shot attempts and the opposing team gets 4 unblocked shot attempts while the player is on the ice, the player earns a fenwick percent calculation of 60%.

The coefficient for shots on goal (SOG, 5.96) indicates that, on average, each additional shot on goal is associated with a 5.96 increase in high danger shots per 60 minutes when analyzed independently. This positive and statistically significant relationship suggests that players who generate more shots also tend to create a higher volume of dangerous scoring opportunities. This justifies the link between overall shooting pressure and offensive efficiency due to the fact players who consistently shoot more pucks are more likely to produce high-quality chances on the goal. On the other hand, variables such as blocks, plus_minus_rating, hits, position, and adjusted_expected_goals are statistically insignificant, meaning that they explain little to no variance. These features will be removed from future analysis.

Table 10 presents the preliminary OLS multivariate regression results, incorporating all statistically significant features identified in the univariate analysis alongside on-ice high danger shots per 60 minutes.

TABLE 10 On-Ice High Danger Shots per 60 Minutes Multivariate Regression Results

However, after employing backward stepwise regression analysis and accounting for each feature’s VIF to address potential multicollinearity, the following features and their corresponding VIF values were retained in the final model:

Feature fenwick expected_goals_per_60min ppg games_played

VIF 1.015080 1.774231 1.895031 1.441192 giveaways

1.590167

The multivariate regression model was then refitted. Table 11 shows the results.

TABLE 11 On-Ice High Danger Shots per 60 Minutes Refitted Multivariate Regression Results

When compared to the initial model presented in Table 10, the refined model in Table 11 demonstrates improved efficiency and interpretability. After applying backward stepwise regression and reviewing each variable’s variance inflation factor (VIF), several statistically insignificant features – corsi, production value in minutes, shots on goal (SOG), shooting percentage, age, takeaways, extension, penalty minutes – were removed. Despite this large subtraction of features, the model’s explanatory power remained unchanged (Table 10’s 0.693 to Table 11’s 0.692), indicating that the excluded features contributed minimal additional explanatory value. The refitted model therefore captures nearly the same degree of variance in on-ice high danger shots per 60 minutes while relying on fewer and more meaningful variables.

The final regression model explains approximately 69.2% of the variance in on-ice high danger shots per 60 minutes. This reflects a moderately strong overall model fit with the selected features. Fenwick and expected_goals_per_60min are the strongest positive features. This emphasizes that both overall unblocked shot attempts and shot quality influence the percentage rate of high-danger scoring opportunities generated. Suggesting that players who are more offensively involved – either with scoring and/or overall puck possession – tend to be involved in a larger number of high-danger chances.

The constant value represents the baseline level of production for a player when all other predictors are held at zero. This was necessary to have in order to complete the regression in Python. All features were found to be statistically significant in the refitted model

The ANOVA analysis was used to see how player performance changed across different contract years, with the F-statistic showing how much variation occurred over time. These results are available in Table 12.

TABLE 12 On-Ice High Danger Shots per 60 Minutes 60 Minutes ANOVA Results

Several features showed statistically significant differences, indicating that player performance tended to shift throughout the contract cycle. Fenwick (F = 30.19) demonstrated one of the strongest patterns in the study, with values increasing in the contract year but declining significantly in the years that followed. This illustrates that players generate more unblocked shot attempts leading up to and during their contract year but tend to drop off afterward. On the other hand, games played (F = 17.74) revealed a strong positive shift after the contract year, which may suggest that players play more conservatively before signing contract opportunities in hopes of not sustaining an injury.

Overall, these results show that player performance in the form of on-ice high danger shots is not consistent across time.

Takeaways Table 13 shows the results of the first set of regressions that were conducted on takeaways, a direct defensive contribution to player performances. This metric quantifies the number of times the player successfully gained possession of the puck from an opponent. This measures defensive skill, ice position awareness, and puck recovery abilities. Takeaways are key to transitioning the puck back to offensive position, and thus, reflect a player’s ability to disrupt the opposing team’s rhythm.

TABLE 13 Takeaways Univariate Regression Results

These models indicate that there are numerous (14/17) predictor variables with p-values less than 0.05. This demonstrates that these features are statistically significant and valuable to this study. The strongest features in terms of variance explained (R-squared) are adjusted_expected_goals (0.232), games_played (0.214), and giveaways (0.135). Adjusted expected goals is a plausible link as players who generate higher-quality offensive opportunities may be more practiced at recovering puck possessions.

The coefficient for adjusted expected goals (0.20) indicates that, on average, each unit increase in takeaways is associated with a 0.20 increase in adjusted expected goals when analyzed independently. This positive and statistically significant relationship suggests that players who generate more takeaways tend to also create higher offensive opportunities and improved overall performance. When putting this in context of the game itself, breakaway goals are there own metric: Players may strip the puck away from the opponent and have such a large physical distance between themselves and the nearest defender that the only line of defense is the goalie at the net. Similarly, games played (0.42) demonstrate a strong positive association with takeaways. This implies that players who receive more playing time have more opportunities to engage in defensive actions. On the other hand, blocks, hits, and fenwick are not statistically significant and, therefore, explaining virtually no variance in takeaways. They will be removed for future analysis.

Table 14 presents the preliminary OLS multivariate regression results, incorporating all statistically significant features identified in the univariate analysis alongside takeaways.

TABLE 14 Takeaways Multivariate Regression Results

However, after employing backward stepwise regression analysis and accounting for each feature’s VIF to address potential multicollinearity, the following features and their corresponding VIF values were retained in the final model:

Feature adjusted_expected_goals games_played giveaways ppg plus_minus_rating high_danger_shots_per_60min

VIF 3.056324 1.884780 1.506142 2.796142 1.028440 1.277652 age position penalty_minutes

1.066140 1.068713 1.188390

The multivariate regression model was then refitted. Table 15 shows the results.

TABLE 15 Takeaways Refitted Multivariate Regression Results

When compared to the initial model presented in Table 14, the refined model in Table 15 demonstrates improved efficiency and interpretability. After applying backward stepwise regression and evaluating each variable’s variance inflation factor (VIF), several statistically insignificant variables – sog, expected_goals_per_60min, shooting_pct, corsi, age, and extension – were removed. Despite this reduction in features, the model’s explanatory power remained effectively unchanged (R-squared value decreased slightly from 0.356 to 0.354), indicating that the excluded features contributed minimal additional explanatory value. This allows the refitted model to rely on a smaller amount of features, while providing an equal level of variability.

The final regression model explains approximately 35.4% of the variance in takeaways. This suggests a moderately weak model fit with the remaining selected variables. Several variables show statistically significant relationships with the dependent variable and player defensive performance. Namely, adjusted_expected_goals, games_played, and giveaways arose as the strongest positive features. This indicates that players who play more games and generate more stable puck interactions tend to record higher takeaway counts. On the other hand, ppg and penalty_minutes display significant negative coefficients, suggesting that players who focus more on offensive production or incur more penalties may engage less frequently in puck recovery in the form of takeaways.

The constant value represents the baseline level of production for a player when all other predictors are held at zero. This was necessary to have in order to complete the regression in Python. Age was the only feature that was found to be not statistically significant, and is therefore removed from the model.

The ANOVA analysis was used to see how player performance changed across different contract years, with the F-statistic showing how much variation occurred over time. These results are available in Table 16.

Takeaways ANOVA Results

TABLE 16 (2 sections)

Several features showed statistically significant differences, indicating that player performance tended to shift throughout the contract cycle. Adjusted expected goals (F = 22.68) demonstrated one of the strongest shifts in this analysis and study: It showed a clear decline from t-2 to t-1 followed by a visible increase from t-1 to t+2. These trends suggest that a player’s ability to form quality scoring opportunities tends to dip leading up to a contract year but rebounds strongly after signing. This, moreover, reflects improved production post-contract.

Games played (F = 17.74) followed a similar trajectory, decreasing from t-2 to t0 before increasing significantly from t0 to t+2. This indicates that players may appear in fewer games before their contract year, possibly due to wanting to be cautious and avoid potential injury. However, after gaining the security of a contract, players become more routinely active.

Overall, these results show that player performance in the form of takeaways is not consistent across time.

Games Played Table 17 shows the results of the first set of regressions that were conducted on the amount of games played. Games played measures the total number of games when a player stepped onto the ice for at least one shift (approximately 30-60 seconds). So although a player might have not started on the ice at the start of the game, if their skates touched ice during any of the three periods, the player will have recorded a game played. This study wanted to include this as a way of interpreting injury. Although a player might have missed a game for another reason (maybe paternity leave or sickness), injury was assumed to be the most common.

TABLE 17 Games Played Univariate Regression Results

These models indicate that there are numerous (13/17) predictor variables with p-values less than 0.05. This demonstrates that these features are statistically significant and valuable to this study. The strongest features in terms of variance explained (R-squared) are giveaways (0.270), takeaways (0.214), and adjusted_expected_goals (0.202). Giveaways being the strongest variable is presumable, given that players who appear in more games are naturally more involved in puck movement. This increases their opportunities to create – but also lose – possession. This explains why takeaways are second to this value, and the R-squared values are relatively close. The coefficient for shots on goal (SOG, 2.23) indicates that, on average, each additional game played is associated with a 2.23 increase in shots on goal when analyzed independently. This positive and statistically significant relationship suggests that players who play in more games create a higher probability of scoring. Similarly, hits (1.12) demonstrates a positive and significant relationship, showing that players who appear in more games also contribute more physically aggressive through body contact. This might be somewhat inevitable – like fights in hockey – due to the game being very physically intense. Table 18 presents the preliminary OLS multivariate regression results, incorporating all statistically significant features identified in the univariate analysis alongside the amount of games played.

TABLE 18 Games Played Multivariate Regression Results

However, after employing backward stepwise regression analysis and accounting for each feature’s VIF to address potential multicollinearity, the following features and their corresponding VIF values were retained in the final model: giveaways

Feature takeaways adjusted_expected_goals sog penalty_minutes blocks hits ppg shooting_pct expected_goals_per_60min high_danger_shots_per_60min plus_minus_rating

VIF 1.912768 1.492159 8.233324 1.663124 1.671061 2.400121 1.779150 2.932261 2.100517 6.919408 2.088580 1.070911

The multivariate regression model was then refitted. Table 19 shows the results.

TABLE 19 Games Played Refitted Multivariate Regression Results

When compared to the initial model presented in Table 19, the refined model in Table 20 demonstrates improved efficiency and interpretability. After applying backward stepwise regression and evaluating each variable’s variance inflation factor (VIF), one statistically insignificant feature, corsi, was removed. Despite this reduction, the model’s explanatory power remained constant (R-squared of 0.636), indicating that the excluded variables contributed minimal additional explanatory value. The refitted model therefore maintains the same high level of explanatory strength while relying on a smaller and interpretable set of features.

The final regression model explains approximately 63.6% of the variance in games played. This represents a decently strong model fit with the remaining variables. Several variables exhibit statistically significant relationships with player and season availability. Particularly, adjusted expected goals, shots on goal (SOG), and hits emerged as strong positive features. Players who generate more scoring opportunities, stay more active in offensive play while on the ice, and as an effect, increase engagement with more games. In contrast, points per game (PPG) and expected goals per 60 minutes display significant negative coefficients. This may suggest that players who perform very well offensively do so in a smaller amount of games (i.e. more efficient while on the ice).

The constant value represents the baseline level of production for a player when all other predictors are held at zero. This was necessary to have in order to complete the regression in Python. All features were found to be statistically significant and, therefore, none were removed from the model.

The ANOVA analysis was used to see how player performance changed across different contract years, with the F-statistic showing how much variation occurred over time. These results are available in Table 20.

Takeaways ANOVA Results

TABLE 20 (2 sections)

Several features showed significant differences, meaning player performance tended to shift throughout the contract cycle. Adjusted_expected_goals (F = 22.68) demonstrated one of the strongest patterns, with values increasing sharply after the contract year. This suggests players generate higher-quality scoring opportunities following renewed and/or freshly solidified contracts. Similarly, shots on goal (SOG, F = 6.11) rose substantially after the contract year. This reinforces the trend that players tend to become more offensively active when compared to pre-contract years. Penalty_minutes (F = 11.93) and hits (F = 11.77) followed similar patterns: Both fell leading into the contract year but increased afterward. This suggests a shift in physical play once aspired job security in the form of a contract is attained.

Overall, these results show that player performance in the form of games played is not consistent across time.

Machine Learning

After the univariate, multivariate, and ANOVA analyses of all the selected dependent variables, production value per minute was selected as the primary focus for the machine learning portion of this study. This metric provides the most comprehensive and effective measure of player performance. Because this statistic represents a player’s on-ice performance value, it ties into both offensive and defensive factors.

After filtering the data for pre-contract and initial contract years, a player_id column was added to the data set. This approach ensured that players who signed multiple contracts during the study period were treated as separate data observations. In other words, the player_id variable was created to allow Python to correctly interpret the data set, thereby grouping each player name by their consecutive contract_cycle sequences (t-2, t-1, and t0).

Results from the multivariate regression results were utilized to limit the number of features, while also increasing the odds of significant data. The independent variable data frame was then pivoted for each player_id to have one row (i.e. hits_t-2, hits_t-1, hits_t0…). For each player_id, only the production_value_in_min corresponding to the t0 contract cycle was retained. This formed the dependent variable (y) dataset, which was later combined with the independent variables for the machine learning analysis. This created a final data frame of 278 rows and 26 columns.

The X and y variables were defined and then split into training and testing subgroups. This created a Training shape of ((222, 16), (222,)) and Testing shape of ((56, 16), (56,)), indicating the 80/20 split.

The four algorithm models were designated into two separate pipelines: Linear Ridge and Lasso regressions (need scaling) and Tree-based RandomForest and XGBoost (no scaling necessary). After utilizing GridSearchCV to identify the optimal hyperparameters for each machine learning model, the following parameter settings were determined to produce the best performance:

The same models were then run utilizing the feature selection method SelectKBest to highlight the strongest predictors. This provided insight into whether simplifying the feature set could improve model performance and interpretability.

The table and accompanying visualization below compare the performance of the original models with those optimized using SelectKBest. Unlike the test R-squared, which measures how well the final model predicts unseen data, the cross-validation R-squared reflects performance across multiple training subsets, offering a more reliable indicator of overall model stability and generalization.

After applying the SelectKBest feature selection method, model performance generally improved across most – three out of four – algorithms. Both the Lasso and Random Forest models demonstrated higher R-squared scores. This indicates better predictive accuracy after less impactful features were removed. The Ridge model’s R-squared remained unchanged, suggesting that its regularization already optimized feature weights effectively without further benefit from feature selection. Notably, the XGBoost model experienced the largest improvement in R-squared, rising from 0.468 to 0.567. This represents the highest cross-validation performance among all models.

Overall, while Ridge initially produced the strongest results in the original models, XGBoost with SelectKBest ultimately achieved the best performance, highlighting the advantage of combining feature selection with a more flexible learning algorithm. Using the given parameters identified through GridSearchCV, each model was trained and evaluated on the test data. Among all models, SelectKBest Ridge regression demonstrated the highest R-squared value (0.430) and the lowest MSE (263.800) and RMSE (16.241), illustrating it explained the greatest proportion of variance in player production with the smallest prediction error. Additionally, the model achieved a competitive MAE (11.84), reflecting a relatively low average difference between predicted and actual values. While MSE and RMSE emphasize larger deviations by squaring the errors, MAE provides a more balanced view of typical prediction accuracy. This highlights the SelectKBest Ridge model’s consistency and reliability across individual observations.

These results, moreover, indicate that this model provided the most accurate and well-balanced predictions for player production in this study. While the XGBoost model with SelectKBest achieved the highest cross-validation R-squared value, indicating strong generalization performance during training, the Ridge regression model with SelectKBest ultimately performed best on the test data. In other words, although XGBoost showed the strongest performance across training subsets, the Ridge model proved more effective and reliable when applied to the actual dataset. Figure 1 displays the SelectKBest Ridge regression coefficients, illustrating how each feature contributes to the model’s predictions of player production value. Features with positive coefficients – bars extending to the right – are associated with higher predicted production values. This means that as these feature values increase, the model predicts an increased level of player productivity. Alternatively, features with negative coefficients – bars extending to the left – are associated with lower predicted production values. This indicates that increases in these variables are associated with declines in predicted productivity values.

Figure 1

Games_played_t-2 (.242) and plus_minus_rating_t-1 (1.63) are the strongest positive predictors. This suggests that players who consistently appeared in more games two seasons prior to the original contract year and those who contributed positively to their team’s point differential in the season before their contract year, are more likely to maintain higher levels of performance when approaching a new agreement. On the other hand, several variables showed notable negative relationships with production value. The largest negative coefficients were observed for expected_goals_per_60min_t-1 (-3.24) and expected_goals_per_60min_t-2 (-2.93). This suggests that players who generated high scoring opportunities in previous seasons did not always convert those opportunities efficiently during their contract year. Similarly, shooting_pct_t-1 (-2.17) and shooting_pct_t-2 (-1.74) recorded strong negative correlations, demonstrating players whose prior shooting success rates may have been unsustainably high and regressed toward average performance levels for both years prior to t0.

The study then used a 5-fold cross-validation to evaluate how well the SelectKBest Ridge regression model would respond to unseen data. The model achieved an R-squared of 0.41497, therefore explaining approximately 41% of the variance in player production on average. The standard deviation of 0.08670 suggests that the model varies approximately .08 between folds. This demonstrates moderate stability and consistent predictive capability.

The mean residuals for all possible models are negative, indicating that, on average, each model slightly overpredicted player production. SelectKBest Ridge and Ridge models (-5.63) showed the largest negative means, where the predictions tended to be slightly higher than the actual value. However, because the residual mean is relatively small compared to the overall range, this bias is modest and suggests the model remains fairly well standardized. Figure 2 illustrates all models and their appropriated mean residuals. Figure 3 clarifies just the SelectKBest Ridge model’s results.

Figure 2

Figure 3

Figures dedicated to visualizing residuals versus predicted values help evaluate whether the model’s errors are random or systematic. Ideally, one wants the residuals to form a random cloud of points around the zero line. This would mean the model captures the underlying data pattern without much bias. Figures 4 - 11 reveal the residual vs model’s predicted values.

Figures 4 - 11

The Ridge and SelectKBest Ridge regression models displayed the most scatter-like residual pattern compared to all the tree-based models. The Lasso models showed a similar residual distribution to the Ridge models, suggesting that both linear regularization methods captured the underlying data more effectively than the Random Forest and XGBoost models.

The Ridge models’ residual plot shows that a majority of points fall below the zero line, indicating that it slightly overpredicted player production. Meaning, the models’ predicted values were generally higher than the actual statistics. This further supports the models’ finding that players generally underperformed in their contract year relative to their previous performances.

The mean residual of –5.63 indicates that, on average, players produced about 5.63 units less than expected based on their prior years’ trends. The median residual (–5.47) aligns closely with the mean, suggesting that this pattern of underperformance is consistent across most players. While there are certainly players who use the prior contract years’ momentum in their contract year, this model’s residuals were not driven by drastic outliers. Going hand-in-hand with this, the standard deviation of 16.12 reflects moderate variability in residuals. While the overall trend points to underperformance, some players still exceeded expectations. Figure 8 shows the overall distribution of the residual values.

Figure 8

Finally, to incorporate the concept of contract value, this study compared each player’s average annual value (AAV) with both their production value measured in minutes and their residual values. Figure 9 illustrates the relationship between players’ AAV and their actual production during the contract year.

Figure 9

There is a clear, mid-strength negatively sloped trend, meaning that as AAV increases, actual production for most players tends to slightly decrease. In other words, on average, players with higher salaries produced less in their contract year than lesser-paid players. The data is widely scattered, which does indicate that there is some variation. Figure 10 compares players' annual salary to the residual values from the Ridge model.

Figure 10

This trendline is approximately flat, with a miniscule downward slope near the higher end of the AAV range. While some players with large salaries may overperform, there is no consistent pattern. Thus, there is no direct connection between salary and whether a player underperforms or overperforms in a new contract cycle stage.

DISCUSSION & CONCLUSION Discussion These results from each of these models show that player performance is not consistent across the pre-contract, contract, and post-contract years. With specific instances being highlighted in each model’s ANOVA results, one can notice numerous statistically significant changes in player statistics throughout the contract cycle. While not a constant pattern, many metrics experienced a stronger increase after the initial contract year. This may be due to many factors: Spark in motivation after changing teams and training styles, personal development, and/or bonus incentives involved in new contract terms. Offensive statistics, throughout the study, tested more significantly and produced stronger results, therefore suggesting that offense metrics play a more prominent role in determining overall performance. This comes to be no surprise due to the fact that defensive players in hockey are expected to transition and adapt to constant puck movements (i.e. are constantly making offensive and defensive moves on both sides of the puck).

Regression models varied in strength, with the strongest being expected goals per 60 minutes (R-squared of 0.86), on-ice high danger shots per 60 minutes (R-squared of 0.69), production value in minutes (R-squared of 0.51), and games played (R-squared of 0.64). The weakest model involved the takeaways metric, R-squared value of 0.35. This is consistent with the offensive statistics having stronger influence over player production outcomes. In addition to this, expected goals per 60 minutes accounting for the most amount of variance demonstrates the strong relationship this plays with player performance. Capturing the underlying patterns, the model also indicates that there is no single metric that can fully explain or predict a player’s performance.

This study mainly focuses on production value in minutes. Explaining a little more than half of the variance in player performance, the most significant predictors were corsi, expected goals per 60 minutes, and shooting percentage. These were all statistically significant and had negative influences (negative coefficients). The ANOVA testing revealed various conclusions: Player metrics both increased and decreased before the contract year in addition to increased after the contract year.

Expected goals per 60 minutes decreased early – from t-2 to t-1 – and then rose sharply from t-1 to t0. This supports that players want to generate more scoring chances to make themselves look more valuable, leading to a more lucrative contract. The corsi measure also increased from t-2 and t-1 to t0, moreover increasing offensive activity before the contract signing period. While these are more advanced statistics, the plus-minus rating increased from t-1 to t0, indicating an improved goal differential. Other features including points per game, games played, and hits declined from t-2 and/or t-1 to t0. This may suggest that players adopt a more conservative style of play to reduce the risk of injury prior to securing a new contract. No players want to suffer from a career ending injury, which then influences their contract prospects.

Nevertheless, takeaways, games played, and hits rose after the initial contract year. This implies that physical effort and engagement maintains a more constant level after securing a new contract. In direct comparison with the measures that suffered a decrease before this initial contract year, games played and hits suffer a complete rebound. In fact, most variables remained stable or increased after t0. This post-contract performance seems to be more consistent.

Using the machine learning-made Ridge regression model, this study determined that players produced around 5.6 production units less than expected based on their prior years’ trends. While not all players suffered from this decline, there are a significant number of instances where players lost their prior contract’s momentum and production declined. This study aimed to examine how player performance relates to the profitability of their contracts. Figure 9 illustrates the negative slope of the trendline, suggesting how some higher-paid players tend to produce less production value when compared to lower-paid individuals. There is high variability, but this could still bring to concern the concept of diminishing returns with contract value. Just because a player is paid more, does not necessarily mean that contract value will come to terms on the ice.

From a managerial perspective, NHL general managers, agents, and analytics departments can leverage these models to monitor and enhance player performance. When players exceed their projected value, executives can capitalize on this momentum by implementing targeted incentives to sustain high performance. Alternatively, if players underperform relative to expectations, executives should reevaluate the contract structure or bonus mechanisms to realign incentives and encourage performance improvements.

## Limitations and Areas for Future Study

This study examined performance trends before and after signing a new multi-year contract. The compiled data, while consistent across contract terms due to the Collective Bargaining Agreement, is relatively small. Because teams differ in the tangible and intangible resources available to recruit new players, the number of players signed by various teams is not normally distributed. The scope of this study also includes the seasons that were affected by the pandemic COVID-19; Although all players experienced a decline in the number of recorded metrics due to fewer games played (league-wide), this could still skew the data.

There are certain variables that were not accounted for due to either not being publicly accessible or immeasurability, including coaching staff changes throughout the seasons and the opposing team’s power. While the advanced metrics take into account the opponent’s rank, the basic statistics cannot. A single goal scored against a weaker opponent is valued the same as a goal scored against the Stanley Cup Champions. The contract valuation is based on the sum amount a player would earn per their contract negotiations. This study was not able to gain contract specifics, such as performance bonuses and the minimum a player would earn if they were to sustain a long term injury.

Regarding the methodology, linear regressions are simply stated and straightforward as they assume a direct relationship between any independent variables and the variable of interest. This study assumed a linear relationship between player performances and the features analyzed. While easy to interpret, this also limits the model’s ability to capture nonlinear and/or complicated variable relationships. The regressions, in the end, may have been too simple to capture complex interrelationships between variables.

In addition to alleviating some of the mentioned weaknesses, researchers could examine what factors motivate players. In the form of a more psychological study, future research could examine what drives a player to perform better: Higher contract value, better odds of winning a Stanley Cup, being surrounded by respected and veteran players, etc.. In addition to this, a study dedicated to determining how players are awarded a certain contract would be enlightening. Researchers could determine if teams prioritize age, metrics, marketability, or playing strategy and then assess the awarded contract value. It would be interesting to see if certain teams investing more in players receive high quality performances in return.

## Conclusion

This study demonstrates the importance of regulating players' paychecks and performance outcomes. Modern athletic contracts are steadily rising in value, so professional organizations should be adequately compensating players for their efforts. Because contract theory and players altering their amount of exerted effort are common areas of study, teams need to implement policies to measure player value. Just because a player excels and has a stellar season in their final contract season does not automatically equate to this individual being the ultimate solution for a new team. According to the findings of this study, teams should exercise greater discretion when deciding which players to extend or sign. Whether based on offensive or defensive measures, players’ performance is quite volatile, highlighting the importance of long-term consistency. Objectively, all players will have seasons where they excel and seasons where they hit a rough patch. One needs to distinguish between winning/losing streaks and possible moments of momentum and growth. Combined with the use of data-based decision making, teams will maximize their probabilities of getting the highest returns on their investments.

## APPENDIX

Summary list of variables utilized

Variable Name

Description

AAV (Average Annual Value)

Contract Value divided by Years; represents the player’s annual salary cap hit.

Age

The player’s age at the start of the corresponding season.

Blocks

Total number of opponent shot attempts

Contract Cycle Contract Value Corsi (CF%)

Encoded Contract Cycle Expected Goals (xG) per 60 Minutes

Extension Fenwick (FF%)

Giveaways blocked by the player.

Indicates the player’s position within the five-year contract cycle (−2, −1, 0, +1, +2 relative to contract year t).

Total dollar value of the player’s contract as reported by Puckpedia.

The percent of all shot attempts the player's team gets while the player is on the ice compared to the other team.

For example, if a player's team gets 6 shot attempts and the opposing team gets 4 shot attempts while the player is on the ice, the player's Corsi % is 60%.

A numerical encoding of the contract cycle for statistical modeling purposes.

The chance of an unblocked shot attempt being a goal.

For example, a rebound shot in the slot may have a 50% of going in and be worth 0.5 expected goals, while a shot from the blueline while short handed may be worth 0.01 expected goals.

Binary variable indicating whether the contract was an extension (1) or a new signing (0).

The percent of all unblocked shot attempts the player's team gets while the player is on the ice compared to the other team.

For example, if a player's team gets 6 unblocked shot attempts and the opposing team gets 4 unblocked shot attempts while the player is on the ice, the player's Fenwick % is 60%.

Number of times the player lost possession of the puck to the opposing team.

Hits On-Ice High Danger Shot Attempts per 60 Minutes

Player Name Plus Minus Rating

Position PPG (Points per Game) Pre/Post Contract Year Production Value Production Value in Minutes Season Year Shooting % Shooting Talent Adjusted Expected Goals

Number of body checks the player delivered that separated an opponent from the puck.

Unblocked Shot attempts with ≥ 20% probability of being a goal.

High danger shots account for ~5% of shots and ~33% of goals.

The full name of the skater included in the dataset.

Tracks a player's goals for and against their team during even-strength and shorthanded situations.

A player gets a +1 when their team scores a goal while they are on the ice, and a -1 when the opposing team scores in those same situations

Player’s on-ice role (e.g., C or Center, D or Defenseman, F or Forward, W or Wing).

Total points (goals + assists) divided by total games played in the season.

Identifies whether the observation occurred before, during, or after the player's contract signing year.

A composite statistic representing the player’s on-ice performance value (derived from basic and advanced stats).

The player’s production value normalized per 60 minutes of ice time to adjust for playing time differences.

The NHL season corresponding to each observation.

Percentage of shots on goal that resulted in goals.

Expected goals * (1 + Shooting Talent Above Average).

SOG Takeaways

Team Years

This is the number of goals a player is expected to score given their expected goals and their shooting talent.

Number of shots on goal recorded by the player during the season.

Number of times the player successfully gained possession of the puck from an opponent.

The NHL team the player was rostered with during that season.

Length of the player’s contract in years.

## REFERENCES

[1] Maxcey, M., et al. (2002). The effectiveness of incentive mechanisms in Major League Baseball. Journal of Behavioral Decision Making, 15(5), 463–485. ResearchGate. https://www.researchgate.net/publication/227574531_The_Effectiveness_of_Incentive_Mechani sms_in_Major_League_Baseball

[2] Rosen, S., & Sanderson, A. (2001). Labour markets in professional sports. The Economic Journal, 111(469), F47–F68. Wiley Online Library. https://onlinelibrary.wiley.com/doi/epdf/10.1111/1468-0297.00598

[3] The relationship between player salary and performance in Major League Baseball. (n.d.). Bryant University Honors Projects in Economics (Paper 48). DigitalCommons@Bryant University. https://digitalcommons.bryant.edu/honors_economics/48/

[4] Stiroh, K. J. (2007). Playing for keeps: Pay and performance in the NBA. Economic Inquiry, 45(1), 145–161. Wiley Online Library. https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1465-7295.2006.00004.x

[5] Wikipedia. (n.d.). Principal–agent problem. Wikimedia Foundation. Retrieved November 4, 2025, from https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem

[6] Jean, N. (2016). Contract year phenomenon in Major League Baseball. Duke Journal of Economics. Duke University. https://sites.duke.edu/djepapers/files/2016/10/Jean-Neal_DJE.pdf

[7] Ichniowski, C., & Preston, A. E. (2012). Motivating and monitoring in teams: The role of joint production and team manager in MLB (Working Paper No. 17928). National Bureau of Economic Research. https://www.nber.org/system/files/working_papers/w17928/w17928.pdf

[8] Ahlstrom, D., Si, S., & Kennelly, J. J. (2016). Free-agent performance in Major League Baseball: Do teams get what they expect? Asia Pacific Journal of Management, 33(1), 43–65. https://www.researchgate.net/publication/289444873_Free-Agent_Performance_in_Major_Leag ue_Baseball_Do_Teams_Get_What_They_Expect

[9] White, M. A., & Sheldon, K. M. (2014). Contract year syndrome in the NBA and MLB: A test of the self-determination theory. Psychology of Sport and Exercise, 15(6), 620–626. Self-Determination Theory. https://selfdeterminationtheory.org/wp-content/uploads/2020/10/2014_WhiteSheldon_ContractY earSyndromeNBAandMLB.pdf

[10] Highest batting averages in one season. (n.d.). Baseball Almanac. https://www.baseball-almanac.com/hitting/hibavg4.shtml

[11] The declining NBA vs. the surging NHL. (2025, February 26). Oratory Prep Omega. https://www.oratoryprepomega.org/2025/02/26/the-declining-nba-vs-the-surging-nhl/

[12] Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism. The Quarterly Journal of Economics, 84(3), 488–500. https://www.jstor.org/stable/1879431

[13] Free rider problem. (n.d.). Corporate Finance Institute. https://corporatefinanceinstitute.com/resources/economics/free-rider/

[14] PuckPedia. (n.d.). NHL salary cap, player contracts and salary cap analysis. https://puckpedia.com/

[15] ESPN. (n.d.). NHL statistics. Retrieved November 4, 2025, from https://www.espn.com/nhl/stats

[16] Sports Reference LLC. (n.d.). Hockey-Reference.com — Hockey statistics & history. Hockey-Reference.com. https://www.hockey-reference.com/

[17] MoneyPuck. (n.d.). NHL analytics, playoff odds, power rankings, and data. MoneyPuck.com. https://moneypuck.com/

[18] K., D. (2023, September 22). Optimizing performance: SelectKBest for efficient feature selection in machine learning. Medium. https://medium.com/@Kavya2099/optimizing-performance-selectkbest-for-efficient-feature-sele ction-in-machine-learning-3b635905ed48#a64d
