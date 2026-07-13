<!-- source: 2016 A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data - Scott Bruce.pdf -->

# **A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data** 

**Scott Bruce** 

_Temple University Department of Statistics 1801 Liacouras Walk Philadelphia, Pennsylvania, 19122, U.S.A._ 

**Abstract:** The release of NBA player tracking data greatly enhances the granularity and dimensionality of basketball statistics used to evaluate and compare player performance. However, the high dimensionality of this new data source can be troublesome as it demands more computational resources and reduces the ability to easily analyze and interpret findings. Therefore, we must find a way to reduce the dimensionality of the data set while retaining the ability to differentiate and compare player performance. 

In this paper, Principal Component Analysis (PCA) is used to identify four principal components that account for 68% of the variation in player tracking data from the 2013-2014 regular season and intuitive interpretations of these new dimensions are developed by examining the statistics that influence them the most. In this new high variance, low dimensional space, you can easily compare statistical profiles across any or all of the principal component dimensions to evaluate characteristics that make certain players and teams similar or unique. A simple measure of similarity between two player or team statistical profiles based on the four principal component scores is also constructed. The Statistical Diversity Index (SDI) allows for quick and intuitive comparisons using the entirety of the player tracking data. As new statistics emerge, this framework is scalable as it can incorporate existing and new data sources by reconstructing the principal component dimensions and SDI for improved comparisons. 

Using principal component scores and SDI, several use cases are presented for improved personnel management. Team principal component scores are used to quickly profile and evaluate team performances across the NBA and specifically to understand how New York’s lack of ball movement negatively impacted success despite high average scoring efficiency as a team. SDI is used to identify players across the NBA with the most similar statistical performances to specific players. All-Star Tony Parker and shooting specialist Anthony Morrow are used as two examples and presented with in-depth comparisons to similar players using principal component scores and player tracking statistics. This approach can be used in salary negotiations, free agency acquisitions and trades, role player replacement, and more. 

**Keywords:** Principal component analysis, NBA player tracking data, statistical diversity index, dimension reduction, personnel management, National Basketball Association 

## **1. Introduction** 

The National Basketball Association (NBA) launched a public database in September 2013 containing over 80 new statistics captured by STATS LLC through their innovative sportVU player tracking camera systems[1]. The cameras capture and record the location of players on the court as well as the location of the ball, and the data are used to derive many different interesting and useful stats that expand greatly upon the traditional stats available for analysis of basketball performance. We can now break down shot attempts and points by shot selection (e.g. driving shots, catch and shoot shots, pull up shots), assess rebounding ability for contested and uncontested boards, and even look at completely new statistics like average speed and distance and opponent field goal percentage at the rim. The availability of such data enables fans and analysts to dig into the data and uncover insights previously not possible due to the limited nature of the data at hand. 

1 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

2 

For example, techniques to uncover different ’positions’ based on grouping statistical profiles have become increasingly popular. It reflects the mindset of current NBA coaches and general managers who are very much aware of the different types of players beyond the five traditional roles, but a recent proposal[2] has received criticism for its unintuitive groupings and inability to separate out the impact of player talent[3]. The NBA player tracking data has the ability to differentiate player performance across more dimensions than before (e.g. shot selection, possession time, physical activity, etc.) which can provide better ways to evaluate the uniqueness and similarities across NBA player abilities and playing styles. Additionally, many research methods for basketball analysis rely on estimation of possessions and other stats to produce offensive and defensive ratings[4]. With the ability to track players’ time of possession and proximity to players in possession of the ball through player tracking, we can develop more accurate representations of possessions and better player offensive and defensive efficiency metrics. 

However, the high dimensionality of this new data source can be troublesome as it demands more computational resources and reduces the ability to easily analyze and interpret findings. We must find a way to reduce the dimensionality of the data set while retaining the ability to differentiate and compare player performance. One method that is particularly well-suited for this application is Principal Component Analysis (PCA) which identifies the dimensions of the data containing the maximum variance in the data set. This article applies PCA to the NBA player tracking data to discover four principal components that account for 68% of the variability in the data for the 2013-2014 regular season. These components are explored in detail by examining the player tracking statistics that influence them the most and where players and teams fall along these new dimensions. 

In addition to exploring player and team performances through the principal components, a simple measure of similarity in statistical profiles between players and teams based on the principal components is proposed. The Statistical Diversity Index (SDI) can be calculated for any pairwise player combination and provides a fast and intuitive method for finding players with similar statistical performances along any or all of the principal component dimensions. This approach is also advantageous from the standpoint of scalability. The possibilities to derive new statistics from the player tracking data are endless, so as new statistics emerge, this approach can again be applied using the new and existing data to reconstruct the principal components and SDI for improved player evaluation and comparisons. 

Numerous applications in personnel management exist for the use of SDI and the principal component scores in evaluating and comparing player and team statistical performances. Two specific case studies are presented to show how these tools can be used to quickly identify players with similar statistical profiles to a certain player of interest for the purpose of identifying less expensive, similarly skilled players or finding suitable replacement options for a key role player within the organization. 

This article is organized as follows. Section 2 describes the player tracking data and data processing. Section 3 provides the analysis and interpretations for the four principal components in detail, showing how players and teams can be compared across these new dimensions. Section 4 introduces the calculation for SDI and two case studies where principal component scores and SDI are used to find players with similar statistical profiles to All-Star Tony Parker and role player Anthony Morrow for personnel management purposes. Section 5 concludes the article with final remarks. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

3 

## **2. NBA Player Tracking Data** 

## **_2.1. Data Description_** 

Currently, there are over 90 new player tracking statistics, and data for all 482 NBA players from the 2013-2014 regular season are available. Separate records exist for players who played for different teams throughout the season, including a record for overall performance across all teams. Brief descriptions of the newly available statistics adapted from the NBA player tracking statistics website[5] are provided for reference and will be helpful in better understanding the analysis going forward. 

## **Shooting** 

Traditional shooting statistics are now available for different shot types: 

- _Pull up shots_ - shots taken 10 feet away from the basket where player takes 1 or more dribbles prior to shooting 

- _Driving shots_ - shots taken where player starts 20 or more feet away from the basket and dribbles less than 10 feet away from the basket prior to shooting 

- _Catch and shoot shots_ - shots taken at least 10 feet away from the basket where player possessed the ball for less than 2 seconds and took no dribbles prior to shooting 

## **Assists** 

New assist categories are available that enhance understanding of offensive contribution: 

- _Assist opportunities_ - passes by a player to another player who attempts a shot and if made would be an assist 

- _Secondary assists_ - passes by a player to another player who receives an assist 

- _Free throw assists_ - passes by a player to another player who was fouled, missed the shot if shooting, and made at least one free throw 

- _Points created by assists_ - points created by a player through his assists 

## **Touches** 

Location of possessions provides insight into style of play and scoring efficiency: 

- _Front court touches_ - touches on his team’s half of the court 

- _Close touches_ - touches that originate within 12 feet of the basket excluding drives 

- _Elbow touches_ - touches that originate within 5 feet of the edge of the lane and the free throw line inside the 3-point line 

- _Points per touch_ - points scored by a player per touch 

## **Rebounding** 

New rebounding statistics incorporate location and proximity of opponents: 

- _Contested rebound_ - rebounds where an opponent is within 3.5 feet of the rebound 

- _Rebounding opportunity_ - when a player is within 3.5 feet of a rebound 

- _Rebounding percentage_ - rebounds over rebounding opportunities 

## **Rim Protection** 

When a player is within 5 feet of the basket and within 5 feet of the offensive shooter, opponents’ shooting statistics are available to measure how well a player can protect the basket. 

## **Speed and Distance** 

Players’ average speeds and distances traveled per game are also captured and broken out by offensive and defensive plays. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

4 

## **_2.2. Data Processing_** 

Only players who played at least half the 2013-2014 regular season, 41 games, are included in this analysis. This restriction is made to reduce the influence of player statistics derived from only a few games played. Also fields containing season total statistics and per game statistics are dropped from the analysis since they could be influenced by number of games and minutes played throughout the season. Instead, per 48 minutes, per touch, and per shot statistics are used. The final data set contains 360 player records each containing 66 different player tracking statistics. 

## **3. Principal Component Analysis** 

With numerous player tracking statistics already available and the potential to develop infinitely many more, it is increasingly difficult to extract meaningful and intuitive insights on player comparisons. Now that the data are available for more granular and detailed comparisons, a methodology is needed that can analyze the entirety of the data set to extract a handful of dimensions for comparisons. These dimensions should be constructed in a way that ensures optimality in differentiating players (i.e. dimensions should retain the maximum amount of player separability possible from the original data) and can be understood in terms of the original statistics. 

Principal Component Analysis (PCA), developed by Karl Pearson in 1901[6] and later by Hotelling in 1933[7], is a particularly well-suited statistical tool that can accomplish this task through identifying uncorrelated linear combinations of player tracking statistics that contain maximum variance. Interested readers can find a brief technical introduction to PCA in Appendix A. Components of high variance help us to better differentiate player performance in these directions in hopes that the majority of the variance will be contained in a small subset of components. This simple and intuitive approach to dimension reduction provides a platform for player comparisons across dimensions that best separate players by statistical performance and can be implemented without expensive proprietary solutions, providing more visibility into how the method works at little to no additional cost. 

## **_3.1. Dimension Reduction_** 

PCA is sensitive to different variable scalings in the original data set such that variables with larger variances may dominate the principal components if not adjusted. To set every statistic on equal footing, all statistics are standardized with mean 0 and variance 1 prior to conducting the analysis. 

PCA is most useful when the majority of the total variance across variables are captured by only a few of the principal components, thus the dimension reduction. If this is the case for the NBA player tracking data set, it means that we are able to retain the ability to differentiate player performance without having to operate in such a high dimensional space. Figure 1 shows the variance captured by each principal component. Note the variance captured in the first principal component is very high and decreases drastically through the first four components. After that, the change in variance is relatively flat, forming an elbow shape in the plot. This means that the variances captured by the fifth component onward are very similar and much smaller than the first four components. Moreover, the first four components capture 68% of the variance across the original variables, so we utilize these four components going forward to analyze and compare player performance and playing styles. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

5 



<!-- Start of picture text -->
Variance of Principal Components<br>68% of total variance captured in first 4 PCs<br>1 2 3 4 5 6 7 8 9 10<br>Principal Component<br>25<br>20<br>15<br>Variance<br>10<br>5<br><!-- End of picture text -->

Figure 1: Variance captured by first ten principal components (color online). 

## **_3.2. Principal Components_** 

Each principal component (PC) is a linear combination of the original variables in the dataset. There is a vector for each principal component containing the coefficients associated with each of the variables in the original data set and are called _loading vectors_ . These describe the influence of each variable for each principal component and are used to interpret these new dimensions in terms of the original variables. Figure 2 plots the categorized loading coefficients for the four principal components and is explored in detail in the following sections. Variables can have a positive or negative contribution to the principal component. While the sign is arbitrary, understanding which variables contribute positively or negatively can help with interpreting the principal components. The most important statistics for each component are presented in the following sections, but tables containing all loading coefficients for variables contributing significantly to the principal components are also available in Appendix B for more details. 

Each player can then be given a set of PC scores by multiplying the standardized statistics by their corresponding loading coefficients and then taking a sum (see Appendix A for details). Figure 3 contains plots of the PC scores for all players with a select few noted for illustration. Using the loading and score plots here, we can begin to understand and interpret what these new dimensions are capturing and use them for player comparisons. 

## _3.2.1. PC 1: Inside vs. Outside_ 

The first principal component accounts for the most variation, 42% of the total variance. Table 1 lists statistics with highly positive and negative loadings for PC 1, and refer back to Figure 2 for categorized PC 1 loadings for all statistics. These are used to better understand the meaning of the scores along this dimension. Players with positive scores for PC 1 are able to secure rebounds of all kinds and are responsible for defending the rim and close shots. Notable examples are Andre Drummond, DeAndre Jordan, and Omer Asik. While players with negative scores for PC 1 drive the basketball to the hoop 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 6 



<!-- Start of picture text -->
Loading Plot: PC 1 vs. PC 2 Loading Plot: PC 3 vs. PC 4<br>Rebounding Outside Scoring Scoring Efficiency (Overall) Speed and Distance<br>Inside Scoring Driving Scoring Scoring Efficiency (Driving) Assisting and Passing<br>Inside Touches Assisting and Passing Scoring Efficiency (Catch and Shoot) Other<br>Rim Defense Other Rebounding Efficiency<br>0.2 0.2<br>0.0 0.0<br>-0.2 -0.2<br>-0.2 0.0 0.2 -0.2 0.0 0.2<br>PC 1 Loadings PC 3 Loadings<br>Figure 2: Categorized loading coefficients for all statistics (color online).<br>Score Plot 1 vs. 2 Score Plot 3 vs. 4<br>Chris PaulRicky Rubio<br>Tony Parker<br>5 5 Kevin Love Spencer Hawes<br>Stephen Curry DeAndre JordanOmer Asik Patty Mills<br>Andre Drummond<br>0 0 Dennis Schroder Shane Larkin<br>Carmelo Anthony<br>LeBron James<br>Kevin Durant Ish Smith<br>Tyreke EvansTony Wroten<br>-5 -5 Rodney Stuckey<br>Kyle Korver<br>Klay ThompsonAnthony Morrow<br>-20 -10 0 10 20 -5 0 5<br>PC 1 Score PC 3 Score<br>PC 2 Loadings PC 4 Loadings<br>PC 2 Score PC 4 Score<br><!-- End of picture text -->

Figure 3: Player PC scores for first four components (color online). 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

7 

and take pull up and catch and shoot shots often, which implies they tend to be outside players. These players also tend to possess the ball more often and generate additional offense through assists. Examples here are Stephen Curry, Tony Parker, and Chris Paul. 

|Loading|Statistic|Loading|Statistic|
|---|---|---|---|
|0.177|Contested Rebounds|-0.150|Front Court Touches<br>|
|0.176|Rebound Opportunities|-0.150|Pull Up Shot Attempts|
|0.172|Ofensive Rebounds|-0.146|Drives|
|0.172|Total Rebounds|-0.146|Team Driving Points<br>|
|0.171|Contested Ofensive Rebounds|-0.145|Pull Up Points<br>|
|0.170|Opponent Shot Attempts at the Rim|-0.143|Pull Up Made Shots|
|0.170|Contested Defensive Rebounds|-0.142|Time of Possession|
|0.169|Uncontested Rebounding Efciency|-0.140|Assist Opportunities|
|0.169|Opponent Made Shots at the Rim|-0.139|Catch and Shoot 3-Point Shooting Efciency|
|0.169|Ofensive Rebound Opportunities|-0.137|Points Created by Assists|



Table 1 

_Top 10 largest positive(left) and negative(right) loadings for PC 1 (per 48 minutes unless stated otherwise)._ 

## _3.2.2. PC 2: Assist and Drive vs. Catch and Shoot_ 

PC 2 accounts for another 12% of the total variance and Table 2 lists statistics with highly positive and negative loadings. Also refer to Figure 2 for categorized PC 2 loading coefficients. Players with positive PC 2 scores generate offense mainly through assists and driving shots. These players tend to possess the ball often and either kick the ball to teammates for shot attempts or drive the ball to the basket. Many point guards fall into this category with examples like Ricky Rubio, Tony Parker, and Chris Paul. Players with negative PC 2 scores provide offense primarily through catch and shoot shots and are very efficient scorers, especially from behind the 3-point arc. Primary examples are Klay Thompson, Kyle Korver, and Anthony Morrow. 

|Loading|Statistic|Loading|Statistic|
|---|---|---|---|
|0.246|Touches|-0.254|Catch and Shoot Points|
|0.237|Passes|-0.251|Catch and Shoot Attempts|
|0.208|Assist Opportunities|-0.242|Catch and Shoot Made Shots|
|0.206|Assists|-0.235|Catch and Shoot 3-Point Attempts|
|0.206|Points Created by Assists|-0.233|Catch and Shoot 3-Point Made Shots|



Table 2 

_Top 5 largest positive(left) and negative(right) loadings for PC 2 (per 48 minutes unless stated otherwise)._ 

## _3.2.3. PC 3: Scoring and Rebounding Efficiency vs. Speed_ 

Table 3 lists statistics with highly positive and negative loadings for PC 3 which explains 9% of the total variance. Also refer to Figure 2 for categorized PC 3 loading coefficients. Players with positive PC 3 scores are extremely quick on both sides of the ball and cover a lot of ground while on the court. Some examples are Ish Smith, Shane Larkin, and Dennis Schroder. Players with negative PC 3 scores are largely responsible for scoring when on the court and provide a significant amount of offensive production per 48 minutes. Scoring and rebounding efficiency characterize many of the superstars in the NBA with players like Kevin Durant, Carmelo Anthony, and LeBron James touting highly negative PC 3 scores. 

8 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

|Loading|Statistic|Loading|Statistic|
|---|---|---|---|
|0.306|Average Defensive Speed|-0.305|Points|
|0.300|Distance|-0.235|Rebounding Efciency|
|0.300|Average Speed|-0.232|Points per Touch|
|0.226|Average Ofensive Speed|-0.212|Defensive Rebounding Efciency|
|0.202|Opponent Points at the Rim|-0.173|Points per Half Court Touch|



Table 3 

_Top 5 largest positive(left) and negative(right) loadings for PC 3 (per 48 minutes unless stated otherwise)._ 

## _3.2.4. PC 4: Catch and Pass/Shoot vs. Slash_ 

Table 4 lists statistics with highly positive and negative loadings for PC 4 which accounts for another 4% of the total variance. Also refer to Figure 2 for categorized loading coefficients for PC 4. This component is characterized by players’ tendencies when they receive possession of the ball. Players with positive PC 4 scores tend to pass or convert catch and shoot shots when the ball goes their way (e.g. Kevin Love, Spencer Hawes, and Patty Mills) while players with negative PC 4 scores tend to drive the ball and score efficiently when they get touches (e.g. Tyreke Evans, Rodney Stuckey, and Tony Wroten). 

|Loading|Statistic|Loading|Statistic|
|---|---|---|---|
|0.311|Passes|-0.264|Points per Touch|
|0.250|Touches|-0.193|Drives|
|0.248|Catch and Shoot Made Shots|-0.167|Driving Shot Attempts|
|0.237|Catch and Shoot Shooting Efciency|-0.151|Points per Half Court Touch|
|0.236|Catch and Shoot Points|-0.137|Team Driving Points|



Table 4 

_Top 5 largest positive(left) and negative(right) loadings for PC 4 (per 48 minutes unless stated otherwise)._ 

## **_3.3. Team PC Scores_** 

Not only can we characterize players by principal components, but teams can also be profiled along these new dimensions as well. There are numerous ways to aggregate the player PC scores to form a team-level score, but here a simple weighted average is used. The _k_ th team PC score, _tk_ ( _team_ ), can be found by taking an average of the _k_ th PC scores across the _n_ players weighted by the minutes played throughout the season, _mi, i_ = 1 _, . . . , n_ . 



Figure 4 shows the distribution of all NBA teams across these dimensions as well as their corresponding 2013-2014 regular season winning percentage. This view is useful in seeing the differences and similarities in team playing styles and how they impact success. 

For example, the New York Knicks had an extremely negative PC 2 score. Further investigation shows it is partially the result of catch and shoot offense from J.R. Smith, Andrea Bargnani, and Tim Hardaway Jr. who were all in the top 50 in catch and shoot points per 48 minutes. However, another major factor is that 8 of the 12 New York players were below average in passes per 48 minutes (average was 58 passes per 48 minutes) which is indicative of poor ball movement. All-Star Carmelo Anthony is in this group and has long been labeled a ”ball hog”[8] which is supported by his below average 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 9 

passing and above average number of touches and scoring. In fact, Anthony’s top 10 performance in points per 48 minutes, points per touch, and rebounding efficiency helped earn his team the most negative PC 3 team average score. Note that team average PC 3 score is negatively correlated with winning percentage, yet the Knicks won only 37 games and failed to make the playoffs. 



<!-- Start of picture text -->
0.8 0.8<br>SAS SAS<br>OKC OKC<br>LAC IND LAC<br>MIA PORHOU MIAPOR IND HOU<br>0.6 DALTORPHXGSW CHIMEM 0.6 DALGSWPHXTOR CHIMEM<br>BKNWAS CHA BKNWAS CHA<br>MIN MIN<br>ATL NYK DEN NYK ATLDEN<br>0.4 CLE NOP 0.4 NOPCLE<br>LALSAC DET LAL SAC DET<br>UTA BOS BOS UTA<br>ORL ORL<br>PHI PHI<br>0.2 MIL 0.2 MIL<br>-2 -1 0 1 2 -2 -1 0 1 2<br>PC 1 Team Average Score PC 2 Team Average Score<br>0.8 0.8<br>SAS SAS<br>OKC OKC<br>LACIND INDLAC<br>MIAHOUPOR MIAHOU POR<br>0.6 GSWDALPHXTORMEMCHI 0.6 GSWPHXMEMTORDALCHI<br>BKNWAS CHA BKN CHAWAS<br>MIN MIN<br>NYK DENATL NYKDEN ATL<br>0.4 NOPCLE 0.4 NOP CLE<br>LALDETSAC DET SAC LAL<br>BOS UTA BOSUTA<br>ORL ORL<br>PHI PHI<br>0.2 MIL 0.2 MIL<br>-2 -1 0 1 2 -2 -1 0 1 2<br>PC 3 Team Average Score PC 4 Team Average Score<br>Winning Percentage Winning Percentage<br>Winning Percentage Winning Percentage<br><!-- End of picture text -->

Figure 4: Team average PC scores vs. 2013-2014 regular season winning percentage (color online). 

To better understand how these team average PC scores impact winning, Table 5 contains the results from a multiple linear regression analysis on winning percentage. Note that negative PC 3 scores are highly correlated with winning while positive PC 2 and PC 4 scores are also highly correlated with winning. Negative PC 3 scores are associated with high average scoring and rebounding efficiency. Referring back to Tables 2 and 4, passes, touches, and assists contribute positively to PC 2 and PC 4 scores. Regarding New York’s lackluster season, it seems that Anthony’s great offensive production was not enough to offset the negative impact of extremely poor passing and ball movement. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

10 

|Term|Coefcient|Std Error|_p_-value|
|---|---|---|---|
|Intercept|0.35|0.04|_<_0.001|
|PC 1 Score|-0.01|0.04|0.758|
|PC 2 Score|0.17|0.06|0.005|
|PC 3 Score|-0.20|0.04|_<_0.001|
|PC 4 Score|0.09|0.03|0.013|



Table 5 _Coefficient estimates in regression of team average PC scores on winning percentage (R_<sup>2</sup> _= 0.59)._ 

These results are better illustrated in Figure 5 where the regression-weighted sum of PC 2 and PC 4 scores (0 _._ 17 _∗_ [PC 2 Score] + 0 _._ 09 _∗_ [PC 4 Score]) determine the size of the points. Low average PC 3 scores (i.e. high average scoring and rebounding efficiency) have the strongest influence on winning percentages. However, controlling for PC 3 scores, teams with higher regression-weighted PC 2 and PC 4 scores (i.e. higher average passing, touches, and assisting) generally hold higher winning percentages. This helps account for the success of the Spurs, who distributed the scoring responsibilities more evenly across the team, resulting in lower average scoring efficiency and higher passing on average (9 of the 13 Spurs players were above the average 58 passes per 48 minutes). 

## **Team Average PC 3 Score vs. Winning Percentage** 



<!-- Start of picture text -->
SAS<br>OKC<br>LAC<br>IND<br>MIA HOUPOR<br>GSW<br>MEM<br>DAL<br>PHX TOR CHI<br>BKN WAS<br>CHA<br>MIN<br>ATL<br>NYK<br>DEN<br>NOP<br>CLE<br>DET<br>SAC<br>LAL<br>BOS UTA<br>ORL<br>PHI<br>MIL<br>-2 -1 0 1<br>Team Average PC 3 Score<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>Winning Percentage<br>0.3<br>0.2<br>0.1<br><!-- End of picture text -->

Figure 5: Team average PC 3 scores by regular season winning percentage. Point size determined by regression-weighted sum of PC 2 and PC 4 scores (color online). 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 11 

## **4. Statistical Diversity Index (SDI)** 

Another way the PC scores can be used to compare player statistical profiles is to combine them to produce one measure of how different one player’s statistical profile is from another. Here a simple calculation based on the sum of squared difference between the two players’ four PC scores is proposed. 

## **_4.1. Calculation_** 

For any two players, player _i_ and player _j_ , where _tk_ ( _i_ ) represents the _k_ th principal component score for player i, the Statistical Diversity Index (SDI) can be calculated as 



## **_4.2. Personnel Management_** 

A large SDI for two players indicates that their statistical profiles are very different across the four principal components defined above. Using this measure, we can develop lists of players that have statistical profiles most similar to certain players which has many applications in personnel management. 

## _4.2.1. Case Study 1: Tony Parker_ 

For coaches and general managers that have a certain player in mind they would like to add to their team, this measure can produce a list of players with the most similar statistical profiles who may also be good candidates to consider and might come at a lower price tag. For example, Table 6 lists the five players with the lowest SDI when compared with Tony Parker, meaning they have similar PC scores to Tony Parker, along with their 2013-2014 season salary. 

|Player|SDI|Salary|
|---|---|---|
|Jose Juan Barea (MIN)|0.7|$4,687,000|
|Brandon Jennings (DET)|2.8|$7,655,503|
|Mike Conley (MEM)|5.5|$8,000,001|
|Ty Lawson (DEN)|5.9|$10,786,517|
|Jef Teague (ATL)|6.1|$8,000,000|



Table 6 

_Players with lowest SDI compared with Tony Parker and 2013-2014 salary from_ _`http: // www. basketball-reference. com/`_ 

To better understand the additional value of the player tracking data, PC scores and SDI can be recalculated using only traditional statistics. This approach identifies DeMar DeRozan as the most similar player to Tony Parker although DeRozan and Parker have an SDI of 75 using player tracking statistics (89 other players have a lower SDI compared to Tony Parker). To better explore the difference between the comparisons using traditional and player tracking statistics, DeRozan is included in the next set of comparisons along with J.J. Barea and Brandon Jennings from Table 6. See Figure 6 for a comparison of the PC scores and Table 7 for selected statistics for these players. 

DeRozan and Parker have similar point totals per 48 minutes, but Parker generates more driving points compared to catch and shoot points while DeRozan is more balanced. Additionally, DeRozan doesn’t match the others in terms of assist categories, touches, and passes. This helps explain why 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 12 



<!-- Start of picture text -->
Score Plot 1 vs. 2 Score Plot 3 vs. 4<br>Tony Parker<br>5 Jose Juan BareaBrandon Jennings 5<br>0 DeMar DeRozan 0 Brandon Jennings Jose Juan BareaTony Parker<br>DeMar DeRozan<br>-5 -5<br>-20 -10 0 10 20 -5 0 5<br>PC 1 Score PC 3 Score<br>PC 2 Score PC 4 Score<br><!-- End of picture text -->

Figure 6: Player PC scores for first four components for Tony Parker comparison (color online). 

DeRozan’s PC 2 score is much smaller than the others as catch and shoot offense and lack of passing and assists contribute to negative PC 2 scores. Shot type, touches, and passes are key aspects of the player tracking statistics that add value by improving player comparisons beyond simple number of points and assists. 

With player tracking statistics, J.J. Barea rises as a less expensive option to Parker’s $12.5M salary who had the most similar statistical performance to Parker in the 2013-2014 season as measured by SDI. This can be seen in the similarities among PC scores and the selected statistics and shows how SDI can provide a quick method for identifying similar players for further detailed comparisons. 

|Statistic|Parker|Barea|Jennings|DeRozan|
|---|---|---|---|---|
|Points|27.1|21.5|21.7|28.5|
|Catch and Shoot Points|2.5|3.0|3.0|5.8|
|Driving Points|10.3|8|4.2|6.1|
|Assist Opportunities|19.4|20.5|21|10.4|
|Assist Points Created|21.9|22.5|23.7|12.6|
|Touches|123|121|113|76|
|Passes|90|89|84|43|



Table 7 

_Selected statistics for comparison (per 48 minutes unless stated otherwise)._ 

## _4.2.2. Case Study 2: Anthony Morrow_ 

Another situation where SDI can be useful is in finding suitable replacements for players who may be considering free agency. Finding candidates who can play a similar role in the organization can be difficult, but SDI can help identify candidates who may be more prepared to step into a specific role that needs to be filled. For example, Anthony Morrow left the Pelicans through free agency after the 2013-2014 season to join the Thunder who offered Morrow $3.2M for 2014-2015 compared to the 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 13 



<!-- Start of picture text -->
Score Plot 1 vs. 2 Score Plot 3 vs. 4<br>5 5<br>0 0 CJ Miles Martell Webster Terrence Ross<br>Klay Thompson<br>Anthony Morrow<br>Tim Hardaway Jr.<br>-5 Klay ThompsonCJ MilesTim Hardaway Jr.Anthony MorrowTerrence RossMartell Webster -5<br>-20 -10 0 10 20 -5 0 5<br>PC 1 Score PC 3 Score<br>PC 2 Score PC 4 Score<br><!-- End of picture text -->

Figure 7: Player PC scores for first four components for Anthony Morrow comparison (color online). 

$1.15M under his contract with the Pelicans[9]. Using SDI, the Pelicans can find players similarly suited to replace Morrow’s shooting ability at 54% effective shooting percentage and 60% catch and shoot effective shooting percentage (see Table 8). 

|Player|SDI|Salary|
|---|---|---|
|Klay Thompson (GSW)|2.3|$2,317,920|
|CJ Miles (CLE)|2.9|$2,225,000|
|Tim Hardaway Jr. (NYK)|3.0|$1,196,760|
|Terrence Ross (TOR)|3.8|$2,678,640|
|Martell Webster (WAS)|4.1|$5,150,000|



Table 8 

_Players with lowest SDI compared with Anthony Morrow and 2013-2014 salary from_ _`http: // www. basketball-reference. com/`_ 

Figure 7 shows that these players are very similar in terms of the first two PC scores with slight differences in PC 3 and 4. Based on the interpretation of the PC dimensions previously covered, these players generally produce offense through outside catch and shoot shots (negative PC 1 and 2 scores), but they vary more in shooting efficiency and passing (PC 3 and 4 scores). See Table 9. 

|Statistic|Morrow|Thompson|Miles|Hardaway Jr.|Ross|Webster|
|---|---|---|---|---|---|---|
|Catch and Shoot Points|9.7|12.3|11.4|9.3|10.4|9.7|
|Points per Touch|0.45|0.48|0.40|0.37|0.38|0.28|
|Passes|26.3|25.1|36.9|35.3|31.6|43.5|



Table 9 

_Selected statistics for comparison (per 48 minutes unless stated otherwise)._ 

In terms of catch and shoot points per 48 minutes, all of these players including Morrow are in the top 20 with the exception of Hardaway Jr. at 34th. However you can better see the differences among the players in terms of points per touch and passes which impact PC 3 and 4 scores. As SDI increases, the similarity between the players and Morrow’s points per touch and passes begin to break down. However, the Pelicans could use SDI not only to identify suitable replacements to pursue in the offseason but also to estimate the salary of comparable players for use in salary negotiations. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 

14 

## **5. Discussion and Further Remarks** 

This article explores the utility of the newly available NBA player tracking data in evaluating and comparing player and team abilities and playing styles through their statistical profiles. Using PCA, we identify and interpret four principal components that capture over 68% of the variance in the NBA player tracking data set and compare players along these new dimensions. A simple measure of comparison between two players or teams based on principal component scores, SDI, is also introduced. This framework is scalable as it can incorporate existing and new statistics that will emerge to reconstruct the principal component dimensions and SDI for improved comparisons. 

SDI and the principal component scores can be used by head coaches and general managers to evaluate team performance and personnel needs and also for quickly identifying players with similar statistical profiles to a certain player of interest for use in numerous personnel management applications (e.g. salary negotiations, free agency acquisitions, replacement options for key role players, etc.). This approach is advantageous as it allows for use of the entirety of the available data for finding suitable comparisons across the NBA quickly along with principal component scores to help understand why players are deemed similar statistically. This can serve as a starting point for more detailed comparisons by considerably narrowing down the number of players under consideration. 

This work could be extended by incorporating new data from the 2014-2015 season to see if principal component dimensions and player principal component scores change significantly from one season to another. Also this would provide data for players who didn’t see much playing time in the 2013-2014 season. Additionally, player tracking data at the game level could greatly extend this analysis by tracking how players’ statistical profiles change throughout the course of the season. 

## **References** 

- [1] ”NBA partners with Stats LLC for tracking technology”. NBA Official Release. September, 2013. `http://www.nba.com/2013/news/09/05/nba-stats-llc-player-tracking-technology/` 

- [2] Alagappan, Muthu (2012). ”From 5 to 13. Redefining the Positions in Basketball”. 2012 MIT Sloan Sports Analytics Conference. `http://www.sloansportsconference.com/?p=5431` 

- [3] Haglund, David. ”Does Basketball Actually Have 13 Positions?” Slate. May 2012. `http://www.slate.com/blogs/browbeat/2012/05/02/_13_positions_in_basketball_muthu_ alagappan_makes_the_argument_with_topology.html` 

- [4] Oliver, Dean, et al. (2007). ”A Starting Point for Analyzing Basketball Statistics.” Journal of Quantitative Analysis in Sports 3.1 Web. 

- [5] ”Player Tracking”. NBA.com. Last Accessed January 2016. `http://stats.nba.com/tracking/` 

- [6] Pearson, Karl (1901). ”On Lines and Planes of Closest Fit to Systems of Points in Space.” Philosophical Magazine 2 (11): 559–572. doi:10.1080/14786440109462720. 

- [7] Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. Journal of Educational Psychology, 24, 417-441, and 498-520. 

- [8] Naessens, Phil. ”Carmelo Anthony: The ball stops here”. Fansided.com. `http://fansided.com/ 2014/08/27/carmelo-anthony-ball-stops/` 

- [9] Hogan, Nakia. ”How much money will New Orleans Pelicans guard Anthony Morrow be worth this offseason?”. The Times-Picayune. April 2014. 

- [10] Jolliffe I.T. Principal Component Analysis, Series: Springer Series in Statistics, 2nd ed., Springer, NY, 2002, XXIX, 487 p. 28 illus. ISBN 978-0-387-95442-4 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 15 

## **Appendix** 

## **_A. Brief Introduction to Principal Components Analysis_** 

The method can be formulated[10] as an orthogonal linear transformation of the data into a new coordinate system such that the first direction (first principal component) contains the greatest variance in the data, the second direction (second principal component) contains the second greatest variance, etc. Consider a data matrix **X** _nxp_ whose _n_ rows represent observations each with _p_ different variables of interest. We define a set of _px_ 1 loading vectors, **w** ( _k_ ), _k_ = 1 _, . . . , p_ that map each row of observations in **X** _nxp_ , call it **x** ( _i_ ), _i_ = 1 _, . . . , n_ to a new vector of principal component scores, call it **t** ( _i_ ) such that **t** _k_ ( _i_ ) = **x** ( _i_ ) _∗_ **w** ( _k_ ). We can find the loading vector for the first principal component as **w** (1) such that the variance of the corresponding principal component scores **t** 1( _i_ ) is maximized and **w** (1) is of unit length, which can be expressed as: 



The remaining principal component loading vectors can be found in a similar fashion. To find the _k_ th component, subtract the first k-1 components from **X** : 



Then use the same variance maximization method on the new matrix **X**<sup>ˆ</sup> _k_ to find the _k_ th component: 



Principal component analysis can also be viewed as the eigenvalue decomposition of the covariance matrix where the eigenvectors are the principal components as stated above. There are numerous resources available for explaining the methodology in more detail, but a basic understanding as outlined above should for this article. 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 16 

## **_B. Principal Component Loading Vectors_** 

Variable loadings for coefficients greater than 0.1 in absolute value. Statistics are per 48 minutes unless otherwise stated. 

|Statistic|Loading|
|---|---|
|Contested Rebounds|0.178|
|Rebounding Opportunities|0.176|
|Ofensive Rebounds|0.173|
|Total Rebounds|0.172|
|Contested Ofensive Rebounds|0.171|
|Opponent Field Goal Attempts at the Rim<br>|0.17<br>|
|Contested Defensive Rebounds|0.17|
|Uncontested Rebounding Percentage|0.169|
|Opponent Field Goal Makes at the Rim|0.169|
|Ofensive Rebounding Opportunities|0.169|
|Defensive Rebounding Opportunities|0.166|
|Close Points|0.161|
|Close Attempts|0.159|
|Close Touches|0.158|
|Defensive Rebounds|0.156|
|Uncontested Rebounds|0.154|
|Uncontested Ofensive Rebounds|0.153|
|Uncontested Defensive Rebounding Percentage|0.153|
|Uncontested Ofensive Rebounding Percentage|0.145|
|Blocks|0.14|
|Uncontested Defensive Rebounds|0.14|
|Points per Half Court Touch|0.121|
|Elbow Touches|0.114|
|Catch and Shoot Efective Field Goal Percentage|-0.104|
|Catch and Shoot Attempts|-0.105|
|Catch and Shoot Makes|-0.106|
|Pull Up 3-Point Percentage|-0.116|
|Secondary Assists|-0.117|
|Free Throw Assists|-0.127|
|Pull Up 3-Point Makes|-0.128|
|Driving Points|-0.132|
|Driving Attempts|-0.137|
|Assists|-0.137|
|Pull Up 3-Point Attempts|-0.137|
|Points Created From Assists|-0.137|
|Catch and Shoot 3-Point Percentage|-0.139|
|Assist Opportunities|-0.14|
|Time of Possession|-0.142|
|Pull Up Makes|-0.143|
|Pull Up Points|-0.145|
|Team Driving Points|-0.146|
|Drives|-0.146|
|Pull Up Attempts|-0.15|
|Front Court Touches|-0.15|



Table 10 

_Significant statistic loadings for Principal Component 1_ 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 17 

|Statistic|Loading|
|---|---|
|Touches|0.246|
|Passes|0.237|
|Assist Opportunities|0.208|
|Assists|0.206|
|Points Created From Assists|0.206|
|Time of Possession|0.203|
|Secondary Assists|0.19|
|Free Throw Assists|0.183|
|Front Court Touches|0.18|
|Team Driving Points|0.147|
|Drives|0.146|
|Driving Attempts|0.125|
|Driving Points|0.125|
|Points per Half Court Touch|-0.114|
|Catch and Shoot 3-Point Percentage|-0.115|
|Points per Touch|-0.159|
|Catch and Shoot 3-Point Makes|-0.234|
|Catch and Shoot 3-Point Attempts|-0.235|
|Catch and Shoot Makes|-0.242|
|Catch and Shoot Attempts|-0.251|
|Catch and Shoot Points|-0.254|



Table 11 

_Significant statistic loadings for Principal Component 2_ 

|Statistic|Loading|
|---|---|
|Average Defensive Speed|0.306|
|Distance|0.3|
|Average Speed|0.3|
|Average Ofensive Speed|0.226|
|Opponent Points at the Rim|0.202|
|Close Shooting Percentage|0.156|
|Pull Up 3-Point Makes|-0.108|
|Catch and Shoot Efective Shooting Percentage|-0.113|
|Efective Shooting Percentage|-0.113|
|Catch and Shoot Attempts|-0.113|
|Defensive Rebounds|-0.114|
|Ofensive Rebounding Percentage|-0.119|
|Elbow Touches|-0.122|
|Catch and Shoot Points|-0.124|
|Uncontested Defensive Rebounds|-0.124|
|Pull Up Attempts|-0.138|
|Catch and Shoot Makes|-0.146|
|Catch and Shoot Percentage|-0.148|
|Pull Up Points|-0.151|
|Pull Up Makes|-0.153|
|Points per Half Court Touch|-0.173|
|Defensive Rebounding Percentage|-0.212|
|Points per Touch|-0.232|
|Rebounding Percentage|-0.235|
|Points|-0.305|



|Table12|
|---|



_Significant statistic loadings for Principal Component 3_ 

_Bruce 2015/A Scalable Framework for NBA Player and Team Comparisons Using Player Tracking Data_ 18 

|Statistic|Loading|
|---|---|
|Passes|0.311|
|Touches|0.25|
|Catch and Shoot Makes|0.248|
|Catch and Shoot Percentage|0.237|
|Catch and Shoot Points|0.236|
|Catch and Shoot Efective Shooting Percentage|0.224|
|Catch and Shoot Attempts|0.212|
|Average Ofensive Speed|0.209|
|Catch and Shoot 3-Point Makes|0.166|
|Distance|0.151|
|Secondary Assists|0.15|
|Average Speed|0.146|
|Defensive Rebounding Opportunities|0.142|
|Catch and Shoot 3-Point Attempts|0.141|
|Uncontested Defensive Rebounds|0.139|
|Defensive Rebounds|0.137|
|Uncontested Rebounds|0.117|
|Contested Defensive Rebounds|0.115|
|Opponent Makes at the Rim|0.114|
|Elbow Touches|0.102|
|Opponent Attempts at the Rim|0.101|
|Drives|-0.13|
|Team Driving Points|-0.137|
|Points per Half Court Touch|-0.151|
|Driving Attempts|-0.167|
|Drives|-0.193|
|Points per Touch|-0.264|



Table 13 

_Significant statistic loadings for Principal Component 4_ 


