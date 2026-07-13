<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2024/2024 - Introducing Grid WAR rethinking WAR for starting pitchers - Brill et al.pdf -->

J. Quant. Anal. Sports 2024; 20(4): 293–329 

##### **Research Article** 

Ryan S. Brill* and Abraham J. Wyner 

# **Introducing Grid WAR: rethinking WAR for starting pitchers** 

https://doi.org/10.1515/jqas-2023-0095 Received October 21, 2023; accepted May 8, 2024; published online June 4, 2024 

**Abstract:** The baseball statistic “Wins Above Replacement” (WAR) has emerged as one of the most popular evaluation metrics. But it is not readily observed and tabulated; WAR is an estimate of a parameter in a vaguely defined model with all its attendant assumptions. Industry-standard models of WAR for starting pitchers from FanGraphs and Baseball Reference all assume that season-long averages are sufficient statistics for a pitcher’s performance. This provides an invalid mathematical foundation for many reasons, especially because WAR should not be linear with respect to any counting statistic. To repair this defect, as well as many others, we devise a new measure, Grid WAR, which accurately estimates a starting pitcher’s WAR on a per-game basis. The convexity of Grid WAR diminishes the impact of “blow-up” games and up-weights exceptional games, raising the valuation of pitchers like Sandy Koufax, Whitey Ford, and Catfish Hunter who exhibit fundamental game-by-game variance. Although Grid WAR is designed to accurately measure historical performance, it has predictive value insofar as a pitcher’s Grid WAR is better than Fangraphs’ FIP WAR at predicting future performance. Finally, at https:// gridwar.xyz we host a Shiny app which displays the Grid WAR results of each MLB game since 1952, including career, season, and game level results, which updates automatically every morning. 

**Keywords:** mathematical modeling; baseball; pitching; wins above replacement 

***Corresponding author: Ryan S. Brill** , Graduate Group in Applied Mathematics and Computational Science, University of Pennsylvania, Philadelphia, PA, USA, E-mail: ryguy123@sas.upenn.edu. https://orcid.org/00000001-6387-7713 

**Abraham J. Wyner** , Department of Statistics and Data Science, University of Pennsylvania, Philadelphia, USA, E-mail: ajw@wharton.upenn.edu 

### **1 Introduction** 

##### **1.1 Why calculate WAR?** 

Player valuation is one of the fundamental goals of sports analytics. In team sports, the goal in particular is to quantify the contributions of individual players towards the collective performance of their team. In baseball player roles are clearly defined and events are discrete (see Appendix A for a review of the rules of baseball). This has led to the development of separate player valuation measures for each aspect of the game: hitting, pitching, fielding, and baserunning (Baumer et al. 2015). Historically fundamental measures for evaluating hitters include batting average (BA), on-base percentage (OBP), and slugging percentage (SLG). Classical measures of pitching include earned run average (ERA) and walks and hits per inning pitched (WHIP). For a more thorough review of other player performance measures in baseball, we refer to the reader to Thorn and Palmer (1984), Lewis (2003), Albert and Bennett (2003), Schwarz and Gammons (2005), Tango et al. (2007), Baumer and Zimbalist (2014), and Baumer et al. (2015). 

The benefit of separately measuring different aspects of baseball is that it isolates different aspects of player ability. The drawback is that it doesn’t provide a comprehensive measure of overall player performance. This makes it difficult to compare the value of players across positions. For instance, is a starting pitcher with a 2.50 ERA more valuable than a shortstop with a 2.80 batting average? As the fundamental result of a baseball game is a win or loss, the ideal unified measure of a player’s performance is his contribution to the number of games his team wins. On this view, an analyst’s task is to apportion this total number of wins to each player. 

To this end, _wins above replacement (WAR)_ estimates an individual baseball player’s contribution on the scale of team wins relative to a replacement level player. Win contribution is not estimated relative to a league average player because average players themselves are valuable. A better baseline is a _replacement level_ player who is freely available to add to your team in the absence of the player being evaluated (e.g., a minor league free agent). With this 

Open Access. © 2024 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **294 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

baseline, Sandy Koufax having 11.5 wins above replacement in 1966 means that losing Koufax to injury is associated, on average, with his team dropping about 11.5 games in the standings over an entire season. 

##### **1.2 Standard WAR calculations** 

Traditional measures of player performance like ERA and others listed previously are counting statistics. In other words, they are statistics which tabulate what factually happened during a season. For instance, in 1966 Sandy Koufax had 62 earned runs in 323 innings, resulting in a 1.73 ERA. WAR, on the other hand, is not a readily observed counting statistic. In other words, how many of the 1966 Dodgers’ 95 wins were due to Koufax’s contributions is not a known or observable quantity. Rather, WAR must be _estimated_ from historical data. 

Estimating a player’s wins above replacement is an inherently difficult task because the ultimate win/loss result of a game is the culmination of a complex interaction of event outcomes involving players of varying roles. Accordingly, there have been many different attempts to estimate a baseball player’s WAR. The fundamental idea behind each of these estimation procedures is to capture the contribution of a player’s observed performance isolated from the factors outside of his control. The way in which we measure observed performance is a crucial component of estimating his contribution to winning games. 

To estimate WAR, a baseball analyst first chooses a base metric of performance and then maps this base metric to wins. Different choices of base metric yield substantially different estimates for WAR. For instance, FanGraphs builds separate WAR values for pitchers from two counting stats: fielding-independent pitching (FIP) and average runs allowed per nine innings (RA∕9). FIP is a weighted average of a pitcher’s isolated pitching metrics<sup>1</sup> (e.g., home runs, walks, and strikeouts) (Slowinski 2012). Baseball Reference builds WAR for pitchers from expected runs allowed (xRA), which assigns to each potential at-bat outcome<sup>2</sup> an expected run value (Baseball Reference 2011). For instance, the expected runs allowed off a single reflects the average number of runs that follow a single in a half-inning. 

**1** FanGraphs builds WAR from ifFIP (FIP with infield flies), 

if FIP :=<sup>13 ⋅HR + 3 ⋅</sup><sup><u>(BB + HBP) −</u>2 ⋅</sup><sup><u>(</u></sup><sup>_K_+ IFFB)</sup> IP + if FIP constant _,_ 

which is built from home runs (HR), walks (BB), hit by pitches (HBP), strikeouts (K), infield fly balls (IFFB), and innings pitched (IP). **2** The seven potential outcomes of an at-bat are out, walk, hit-by-pitch, single, double, triple, and home run. 

The difference between Runs Allowed, FIP, and xRA, and hence the associated WAR values for players, can be substantial. FIP, unlike runs allowed and xRA, ignores atbat outcomes involving fielders in order to fully disentangle pitching performance from fielding. Specifically, FIP excludes balls-in-play (singles, doubles, triples, ground outs, fly outs, etc.) because fielders’ actions play a role in the outcome of these plays. Furthermore, FIP and xRA, unlike runs allowed, do not depend on the sequencing of events in an inning. For example, consider an inning where a pitcher strikes out three, while allowing a home run, two walks, and a single. Depending on the sequence of the events, the pitcher could be charged with one to four runs. The pitcher’s FIP and xRA for this inning, however, are the same regardless of the sequence. For a more thorough review of the differences in their methodologies, we refer the reader to the supplementary materials of Baumer et al. (2015). 

After choosing a base measure of player performance, a baseball analyst then decides how to aggregate player performance over the course of a season. Current implementations of WAR from FanGraphs and Baseball Reference average pitcher performance over the entire season (e.g., RA per nine innings, FIP per inning, and xRA per out). 

##### **1.3 Problems with standard WAR calculations for starting pitchers** 

For starting pitchers in particular, there are two problems with standard WAR calculations. First, a base measure of pitcher performance should account for sequencing context; FIP and xRA do not. Second, pitcher performance should not be a simple average across innings and games. 

**Problem 1: excluding sequencing context.** Standard WAR calculations are functions of pitcher performance, traditionally one of FIP, xRA, or runs allowed. If the pitcher cannot affect the sequence of events in an inning, then it makes sense to measure his performance using FIP or xRA. If sequencing variation were due to chance alone, it would not be controlled by the pitcher and should reasonably be excluded. For starting pitchers, however, sequencing variability has other causes. Blake Snell in 2023 is a prime example: he has the highest walk rate since 2000<sup>3</sup> yet has the best ERA in baseball (2.33) and an exceptional 1.2 ERA through the last 23 games at the time of this writing. High-strikeout pitchers like Snell can give up walks strategically without giving up runs; he can increase his effort to strike out a batter when necessary. All this indicates 

**3** At this time of this writing, Snell has about five walks per nine innings and a walk rate of 13.4 %, the 14th highest walk rate since 1912. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 295** 

that he exerts some control over the sequencing of events.<sup>4</sup> Thus, we believe starting pitchers bear responsibility for their sequence of outcomes and that their performance in situations of varying leverage should be taken into account. For batters, there is enough evidence of this to generate a substantial debate – see for example, Bill James’ comparison of Altuve and Judge<sup>5</sup> – but for pitchers the argument against it is nonsense. Thus, we should not use FIP or xRA, which remove sequencing context, as a base measure of pitcher performance to estimate a starting pitcher’s WAR. Rather, in this paper we use runs allowed.<sup>6</sup> 

**Problem 2: averaging across games.** After selecting a base measure of pitcher performance, standard WAR calculations from FanGraphs and Baseball Reference then average pitcher performance over the entire season (e.g., RA per nine innings, FIP per inning, and xRA per out). If the pitcher doesn’t affect his variability across games, then it makes sense to average his performance across games. If variation across games were due to chance alone, it would not be controlled by the pitcher and should reasonably be excluded. For starting pitchers, however, we believe that game-by-game variability has causes other than chance. Sandy Koufax in 1966 is a prime example: he had an astounding 17 complete games in which he allowed at most one run<sup>7</sup> yet had three terrible “blow-up” games. The variability of pitchers like Koufax appears in noticeable patterns, indicating that his non-stationarity across games is a fundamental trait. Our method will account for the possibility that the version of Sandy Koufax that starts a game and gets tagged for six runs in two innings is fundamentally different from the Koufax who strikes out the first six batters (colloquially known as the “the left arm of God”). 

Since a starting pitcher’s game-by-game variability is not entirely due to chance, averaging pitcher performance across games is _wrong_ , specifically because _not all runs have the same value_ within each game. To understand this, think of a starting pitcher’s WAR in a single game as a function _R_ ↦ WAR( _R_ ) where _R_ is the number of runs allowed in that game.<sup>8</sup> We expect WAR to be a decreasing function of _R_ 

**4** Great pitchers are much better in high leverage situations, where the game is on the line. See for example https://www.baseballreference.com/players/split.fcgi?id=koufasa01&year=1966&t=p. 

because allowing more runs in a game should correspond to fewer wins above replacement. Additionally, we expect WAR to be a _convex_ function in _R_ (i.e. its second derivative is positive.) As _R_ increases, we expect the relative impact of allowing an extra run, given by WAR( _R_ + 1) − WAR( _R_ ), to decrease. For instance, allowing two runs instead of one should have a much steeper drop off in WAR than allowing eight runs instead of seven.<sup>9</sup> Therefore, by Jensen’s inequality, 



Traditional methods for computing WAR are reminiscent of the left side of Equation (1): first average a pitcher’s performance, then compute his WAR from the resulting average scaled by the number of innings pitched. Averaging weighs each run allowed equally, causing a pitcher’s “blow-up” games to unfairly dilute the value of high quality performances. Because winning a baseball game is defined by the runs allowed during a game, WAR should look like the right side of Equation (1) – compute the WAR of each of a pitcher’s individual games, and then aggregate. Crucially, these quantities are not the same. 

For concreteness, consider Max Scherzer’s six game stretch from June 12, 2014 through the 2014 All Star game, shown in Table 1 (ESPN 2014). We re-arrange the order of these games to aid our explanation. He was excellent in games one through five and had a 1.2 ERA (five runs in 37 innings). This corresponds to about 2 WAR according to standard metrics (the Detroit Tigers did in fact win all 5). In game six, Scherzer was rocked for ten runs in four innings, exiting in the fifth inning with runners on second and third and no outs. His ERA over the six game stretch ballooned to 3.3 (15 runs allowed in 41 innings), reducing his total WAR to about 1∕2 according to standard metrics. This is a complete absurdity: because a game can’t be lost more than once, accumulated “real” WAR cannot drop from 2 to 

**Table 1:** Max Scherzer’s performance over six games prior to the 2014 all star break, consisting of five excellent games and one bad “blow-up” game. 

|**Game**|**1**|**2**|**3**|**4**<br>**5**|**6**|**total**|
|---|---|---|---|---|---|---|
|Earned runs|0|1|2|1<br>1|10|15|
|Innings pitched|9|6|7|8<br>7|4|41|



**5** https://www.billjamesonline.com/judge_and_altuve/. 

**6** Critics of runs allowed as a base measure of pitcher performance argue it is confounded with the fielding, but we argue in Section 4 that the impact of fielding on WAR is small (smaller than ballpark, which itself is small). 

**7** In 1996 Koufax had eight complete game shutouts and nine one-run complete games. **8** As we will discuss in Section 2, think of game WAR as measuring a context-neutral version of win probability added derived only from 

a pitcher’s performance, invariant to factors outside of his control (e.g., his team’s batting). This is very different from the usual winprobability-added calculation, which is completely dependent on the starting pitcher’s team’s offense. **9** Because _you can only lose a game once_ . 

> **296 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

1/2 with the addition of one game! The correct assessment would charge Scherzer with the maximum possible damage, about −0.40 wins. So Scherzer’s “real” WAR over the six games should be about 1.5, which is three times higher than the standard calculation. By evaluating Scherzer’s performances using only the average, standard WAR significantly devalues his contributions during this six game stretch. The correct approach would be to calculate WAR per game and sum them up. 

Here is another revealing albeit hypothetical example. Suppose a pitcher tosses two nearly flawless eight inning starts, allowing one run in each start, followed by a terrible two-inning blow-up where he gives up eight runs. His averaged performance over the three games is a thoroughly mediocre five runs per nine innings, which translates to a WAR of about 0.0 when calculated using standard metrics. In contrast, it is clear that over the three starts his team will win, with near certainty, two out of three, which translates to a “real” WAR of about 0.8 in total. Our hypothetical pitcher, who is great in two out of three starts and terrible in every third, would accumulate more than eight WAR over a full season, constituting an all-time great season worthy of a Cy Young award.<sup>10</sup> In contrast, standard WAR metrics would suggest he be designated for assignment. What drives the difference? A poor performance can greatly affect the average, effectively allowing a single game to be “lost” more than once. Specifically, standard metrics allow the one blow-up game to count for two losses, resulting in 0 WAR. The example is somewhat extreme, but not that rare.<sup>11</sup> 

##### **1.4 Paper organization** 

These examples illustrate that calculating WAR as a function of pitcher performance averaged across games is wrong. Hence in Section 2 we devise Grid WAR, which estimates a starting pitcher’s WAR in each of his games. Grid WAR estimates the completely context-neutral win probability added above replacement at the point when a pitcher exits the game. Then in Section 3 we discuss our results. We find that averaging pitcher performance across games tends to, in general, undervalue mediocre and highly variable pitchers. This is because the convexity of GWAR diminishes 

> **10** Just two pitchers since 2016 have eclipsed eight Grid WAR. **11** Yankees’ starting pitcher Domingo Germán is a perfect real life example. In two June 2023, he threw a perfect game one game after being rocked for ten runs allowed in three innings. Across an entire season, a pitcher like Germán who alternates having great and terrible games would accumulate more than 3 real WAR and −4.5 standard WAR. 

the impact of games in which a pitcher allows many runs, and these pitchers have more of those games. We also find that Grid WAR has predictive value: past Grid WAR is more predictive than past FanGraphs WAR of future Grid WAR. This suggests that some pitchers’ game-by-game variance in performance is not just “bad luck” but a measurable characteristic. Finally, in Section 4 we conclude with a discussion. Notably, we compare the careers of starting pitchers via Grid WAR across baseball history. Although Grid WAR values many pitchers’ careers similarly as other metrics, it substantially changes our view of some pitchers who exhibit fundamental game-by-game variance. Sandy Koufax is a prime example: although his 1966 season is just the 20th best season of all time according to FanGraphs WAR, it is the best season of all time according to Grid WAR. Other methods incorrectly overweight his three outlying blow-up games. 

### **2 Defining Grid WAR for starting pitchers** 

Our task is to estimate a starting pitcher’s WAR for an individual game, which we call Grid WAR (GWAR). The idea is to estimate a context-neutral version of win probability added derived only from a pitcher’s performance, invariant to factors outside of his control such as his team’s batting.<sup>12</sup> This is very different from the usual win-probability-added calculation, which is completely dependent on the starting pitcher’s team’s offense. In Section 2.1 we detail our mathematical formulation of Grid WAR. We give a brief overview of our data in Section 2.2, and then we discuss how we estimate the grid functions _f_ and _g_ (Sections 2.3 and 2.4), the constant _𝑤_ rep (Section 2.5), and the park effects _𝛼_ (Section 2.6) which allow us to compute a starting pitcher’s Grid WAR for a baseball game. 

##### **2.1 Grid WAR formulation** 

In baseball, each team’s starting pitcher is the first pitcher in the game for that team. A starter usually exits midway through a game according to the discretion of the field manager (the equivalent of a head coach in baseball). 

> **12** Note that computing a player’s context neutral value added in each individual game was first introduced as “Support Neutral Win Loss” (Wolverton 1993, 1999, 2004). In our study, we use different methods, explore the statistical aspects of Grid WAR in much greater depth, and conduct a much more extensive comparison of Grid WAR to other WAR metrics which average pitcher performance over the entire season (specifically, FanGraphs WAR). 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 297** 

Generally a starter pitches for a significant portion of the game and sometimes pitches the entire game (known as a complete game). Often times, a starter is removed between innings.<sup>13</sup> We first define a starter’s Grid WAR for a game in which he exits at the end of an inning. To do so, we define the function _f_ = _f_ ( _I, R_ ) which, assuming both teams have league-average offenses, computes the probability a team wins a game after giving up _R_ runs through _I_ innings (the values of _f_ ( _I, R_ ) for integer values of _I_ and _R_ can be displayed in a simple grid). In short, _f_ is a context-neutral version of win probability, as it depends only on the starter’s performance. 

Note that _f_ also depends on the league (AL vs. NL), season, and ballpark. For example, games in which the home team is in the National League (NL) prior to 2022 did not feature designated hitters, whereas American League (AL) games did, leading to different run environments. Additionally, baseballs have different compositions across seasons, leading to different proportions of home runs and base hits, and hence different run environments. Finally, it is easier to score runs at some ballparks that at others. For instance, Coors Field at high altitude in Denver features many more home runs that other parks. Consequently, _f_ = _f_ ( _I, R_ ) is implicitly a function of league, season, and ballpark. 

To compute a wins _above replacement_ metric, we need to compare this context-neutral win-contribution to that of a potential replacement-level pitcher. A replacement-level player is freely available to add to your team in the absence of the player being evaluated (e.g., a minor league free agent). We use a constant _𝑤_ rep which denotes the probability a team wins a game with a replacement-level starting pitcher, assuming both teams have league-average offenses. We expect _𝑤_ rep _<_ 0.5 since replacement-level pitchers are worse than league-average pitchers. Then, we define a starter’s Grid WAR during a game in which he gives up _R_ runs through _I_ complete innings as 



We call our metric Grid WAR because the function _f_ = _f_ ( _I, R_ ) is defined on the 2D grid {1 _,_ … _,_ 9} × {0 _,_ … _, R_ max = 10}. 

Next, we define a starting pitcher’s Grid WAR for a game in which he exits midway through an inning. In this case, a starter exits an inning having thrown a certain number 

> **13** Recall that in a baseball game, the two teams switch back and forth between batting and fielding; the batting team’s turn to bat is over once the fielding team records three outs. One turn batting for each team constitutes an inning. A game is usually composed of nine innings, and the team with the greater number of runs at the end of the game wins (Wikipedia 2023). 

of outs _O_ ∈{0 _,_ 1 _,_ 2} and having potentially left baserunners on first, second, or third base, encoded by the base-state 

_S_ ∈{000 _,_ 100 _,_ 010 _,_ 001 _,_ 110 _,_ 101 _,_ 011 _,_ 111} _._ 

We define an auxiliary function _g_ = _g_ ( _r_ | _S, O_ ) which, assuming both teams have league-average offenses, computes the probability that, starting midway through an inning with _O_ outs and base-state _S_ , a team scores exactly _r_ runs through the end of the inning. Given _g_ , we define a starter’s Grid WAR during a game in which he gives up _R_ runs and leaves midway through inning _I_ with _O_ outs and base-state _S_ as the expected Grid WAR at the end of the inning, 



Finally, we define a starting pitcher’s Grid WAR for an entire season as the sum of the Grid WAR of his individual games. 

##### **2.2 Our data** 

In the remainder of Section 2, we discuss how we estimate the grid functions _f_ and _g_ , the constant _𝑤_ rep, and the park effects _𝛼_ which allow us to compute a starting pitcher’s Grid WAR for a baseball game (Equations (2) and (3)). In our analysis we use play-by-play data from Retrosheet. We scraped every plate appearance from 1990 to 2020 from the Retrosheet database. For each plate appearance, we record the pitcher, batter, home team, away team, league, park, inning, runs allowed, base state, and outs count. Our final dataset is publicly available online.<sup>14</sup> In our study, we restrict our analysis to every plate appearance from 2010 to 2019 featuring a starting pitcher. Additionally, we scraped FanGraphs RA∕9 WAR (abbreviated henceforth as FWAR(RA∕9)) and FanGraphs FIP WAR (abbreviated henceforth as FWAR(FIP)) using the baseballr package (Petti and Gilani 2021). All computations in our analysis are performed in R, and our code is publicly available online.<sup>15</sup> 

##### **2.3 Estimating the grid function** **_f_** 

Now, we estimate the grid function _f_ = _f_ ( _I, R_ ) which, assuming both teams have average offenses,<sup>16</sup> computes the probability a team wins a game after giving up _R_ runs 

> **14** https://upenn.app.box.com/v/retrosheet-pa-1990-2000. 

> **15** https://github.com/snoopryan123/grid_war. 

> **16** Technically, we assume both teams have offenses that are _randomly drawn_ from our dataset, rather than league-average offenses, since we don’t explicitly adjust for offensive quality. 

> **298 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

through _I_ complete innings. We call _f_ a grid because the values of _f_ ( _I, R_ ) for integer values of _I_ and _R_ can be displayed in a simple 2D grid. To account for different run environments across different seasons, leagues (NL vs. AL), and ballparks, it is imperative to estimate a different grid for each league-season-ballpark. Thus we estimate _f_ using a parametric mathematical model rather than a statistical or machine learning model fit from historical data. Here, we give an overview as to why; see Appendix B for a more detailed discussion. 

The naive solution to estimating _f_ is the empirical grid: across all combinations of _I_ and _R_ , simply take the observed proportion of times a starter’s team won the game. Due to a lack of data, the empirical grid fit on all half-innings from any given league-season massively overfits. In particular, it fails to be monotonic in _I_ or _R_ even though it should be.<sup>17</sup> Thus any ballpark-adjusted empirical grid would also massively overfit. To force the grid to be monotonic, we try XGBoost with monotonic constraints. While the fitted _f_ is monotonic and also convex in _R_ as expected, it still overfits, especially towards the tails (e.g., for _R_ large). Refitting the grid using a statistical model for each league-season is clearly not optimal. 

As there is not enough data to use machine learning to fit a separate grid for each league-season without overfitting, we turn to a parametric mathematical model. Specifically, we use an Empirical Bayes Poisson model from which we explicitly compute context-neutral win probability. We find that our Poisson model is a powerful approximation technique, yielding reasonable grids for our application which vary across each league, season, and ballpark without overfitting. Indeed, by distilling the information of our dataset into just a few parameters, our Poisson model creates a strong model from limited data. 

Because the runs allowed in a half-inning is a natural number, we begin our parametric modeling process by supposing that the runs allowed in a half-inning is a Poisson random variable. In particular, denoting the runs scored by the pitcher’s team’s batters in inning _i_ by _Xi_ and the runs scored by the opposing team in inning _i_ by _Y i_ (for innings after the pitcher exits the game), we model 



The two teams have their own runs per inning parameters _𝜆X_ and _𝜆Y_ because a baseball season involves teams of varying strength playing against each other. The assumption 

**17** For instance, _f_ should be monotonic decreasing in _R_ because as a pitcher allows more runs through a fixed number of innings, his team is less likely to win the game. 

that runs scored in an inning is independent across innings given a team’s strength, while technically false due to nonstationarity across innings,<sup>18</sup> is justified by _working_ . In particular, it yields a grid which looks like a smoothed, nonoverfit version of the empirical and XGBoost grids, and so we deem it a reasonable enough assumption. In other words, we view the independence and Poisson assumptions as tools for creating flexible, non-overfit grids which vary across league, season, and ballpark. 

Given the team strength parameters, the probability that a pitcher wins the game after allowing _R_ runs through _I_ innings, assuming win probability in overtime is 1∕2, is 



If _I_ = 9, this is equal to 





noting that the Skellam distribution arises as a difference of two independent Poisson random variables. To capture variability in team strength across each of the 30 MLB teams, we impose a positive normal prior, 



We estimate the prior hyperparameters _𝜆_ and _𝜎𝜆_<sup>2sep-</sup> arately for each league-season by computing each team’s mean and variance of the runs allowed in each half inning, respectively, and then averaging over all teams. The initial estimated values of _𝜎_<sup>2toolarge(e.g.,theprior</sup> _𝜆_<sup>are</sup> is overdispersed), so we include a tuning parameter _k_ designed to tune the dispersion across team strengths to match observed data. In particular, we use _k_ = 0.28, which minimizes the log-loss between the observed win/loss column and predictions from the induced grid. In particular, 

**18** For instance, there are differences in batter quality across innings. Usually better batters are clumped towards the top of the batting lineup and worse batters appear towards the bottom, so some innings feature more good batters while other innings feature more bad batters. Additionally, there are differences in pitcher quality across innings. Middle relievers, generally appearing in innings five through seven, are usually worse than starting and closing pitchers. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 299** 

the induced grid is given by the posterior mean grid, which we estimate using Monte Carlo integration with _B_ = 100 samples, 



where _𝜆_<sup>(</sup><sup>_b_)</sup> _X_<sup>and</sup><sup>_𝜆_</sup> _Y_<sup>(</sup><sup>_b_)are i.i.d. samples from the prior distribu-</sup> tion (8). 

Additionally, recall that _f_ = _f_ ( _I, R_ ) is implicitly a function of ballpark. To adjust for ballpark, we first define the _park effect 𝛼_ of a ballpark as the expected runs allowed in one half-inning at that park above that of an average park, if an average offense faces an average defense. With our parametric model, the ballpark adjustment is easy: we simply incorporate the park effect into our Poisson parameters. With a statistical model, the ballpark adjustment is more difficult and prone to overfitting, providing yet another justification of our mathematical model. As _𝜆_ represents the mean runs allowed in a half-inning for a given league-season, _𝜆_ + _𝛼_ represents the mean runs allowed in a half-inning at a given ballpark during that league-season. So, to adjust for ballpark, we use _𝜆_ + _𝛼_ in place of _𝜆_ in our Poisson model (9) and positive Normal prior (8). In Section 2.6 we estimate the park effects _𝛼_ . 

In Figure 1 we visualize the estimated grid _f_ according to our Poisson model (9), with prior (8), using the 2019 NL _𝜆_ and _𝜎_<sup>2</sup><sup>_f_grid for</sup> _𝜆_<sup>, without a park adjustment. Note that the</sup> other league-seasons are similar, but differ slightly according to the differing run environments _𝜆_ and _𝜎𝜆_<sup>2. We see that</sup> _f_ is monotonic decreasing in _R_ because as a pitcher allows more runs through a fixed number of innings, his team is 



**Figure 1:** Context-neutral win probability ( _y_ -axis) if a starter allowed _R_ runs ( _x_ -axis) through _I_ complete innings (color) according to the 2019 National League grid function _f_ , fit from our Poisson model (9) with positive normal prior (8). 

less likely to win the game. Also, _f_ is monotonic increasing in _I_ because giving up _R_ runs through _I_ innings is worse than giving up _R_ runs through _I_ + _i_ innings for _i >_ 0, since giving up _R_ runs through _I_ + _i_ innings implies a pitcher gave up no more than _R_ runs through _I_ innings. Further, _f_ is convex in _R_ for large values of _R_ because the marginal impact of allowing an additional run diminishes to zero as _R_ increases because, after giving up a certain number of runs, the game has essentially already been lost. Succinctly, “you can only lose a game once”. Finally, the grid _f_ is smooth. 

##### **2.4 Estimating the grid function** **_g_** 

Now, we estimate the function _g_ = _g_ ( _r_ | _S, O_ ) which, assuming both teams have league-average offenses, computes the probability that, starting midway through an inning with _O_ ∈{0 _,_ 1 _,_ 2} outs and base-state 



a team scores exactly _r_ runs through the end of the inning. We estimate _g_ ( _r_ | _S, O_ ) using the empirical distribution. Specifically, we bin and average over the variables ( _r, S, O_ ), using data from every game from 2010 to 2019. Because _g_ isn’t significantly different across innings, we use data from each of the first eight innings. In Figure 2 we visualize _g_ ( _r_ | _S, O_ = 0), with _O_ = 0 outs, for each base-state _S_ . 

#### **2.5 Estimating the constant** **_𝒘_ rep** 

To estimate wins _above replacement_ , we need to compare a starting pitcher’s context-neutral win contribution to that of a potential replacement-level pitcher. Thus we 



**Figure 2:** From base-state _S_ (color) and _O_ = 0 outs through the end of an inning, the context-neutral probability ( _y_ -axis) that the pitcher allows _R_ runs ( _x_ -axis) according to the grid function _g_ . 

> **300 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

estimate a constant _𝑤_ rep which represents the contextneutral probability a team wins a game with a replacementlevel starting pitcher, assuming both teams have a leagueaverage offense and league-average fielding. Fangraphs (2010) defines _replacement-level_ as the “level of production you could get from a player that would cost you nothing but the league minimum salary to acquire.” We could estimate _𝑤_ rep in a given season by averaging the context neutral win probability at the point when the starter exits the game across all games featuring a replacement-level starting pitcher. To facilitate fair comparison of Grid WAR to FanGraphs WAR, we instead estimate _𝑤_ rep so as to match FanGraphs’ definition of replacement-level. In particular, we choose _𝑤_ = 0.428 so that the sum of GWAR across rep all starting pitchers from 2010 to 2019 equals the sum of FWAR(RA∕9). 

#### **2.6 Estimating the park effects** **_𝜶_** 

Finally, we estimate the park effect _𝛼_ of each ballpark, which measures the expected runs scored in one half-inning at that park above that of an average park, if an average offense faces an average defense. To compute the park effects for 2019, we take all half-innings from 2017 to 2019 and fit a ridge regression, using cross validation to tune the ridge hyperparameter, where the outcome is runs scored during the half-inning and the covariates are fixed effects for each park, team-offensive-season, and team-defensiveseason. We compute similar three-year park effects for 

other seasons. We visualize the 2019 park effects in Figure 3. We use ridge regression, as opposed to ordinary least squares or existing park effects from ESPN, FanGraphs, or Baseball Reference, because, as detailed in Appendix D, it performs the best in two simulation studies and has the best out-of-sample predictive performance on observed data. 

### **3 Results** 

After estimating the grid functions _f_ and _g_ , the constant _𝑤_ rep, and the park effects _𝛼_ , we compute Grid WAR for each starting pitcher in each game from 2010 to 2019. As a quick exposition, we show the full 2019 Grid WAR rankings (Figure 4) and a full game-by-game breakdown of Justin Verlander’s 2019 season (Figure 5). The remainder of this section is organized as follows. In Section 3.1 we compare GWAR to FanGraphs WAR (FWAR) in order to understand the effect of averaging pitcher performance over the entire season on valuing pitchers. We find that averaging over the season allows a pitcher’s terrible performances to dilute the contributions of his great ones. This is because the convexity of GWAR diminishes the impact of games in which a pitcher allows many runs, whereas averaging across games doesn’t. Thus traditional measures of WAR have generally undervalued mediocre pitchers and higher variance pitchers who tend to have more of these terrible games. Then in Section 3.2 we quantify the value 



**Figure 3:** Our 2019 three-year park effects ( _x_ -axis), fit from half-inning data from 2017 to 2019, for each ballpark ( _y_ -axis). The abbreviations are retrosheet ballpark codes. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 301** 



**Figure 4:** Ranking starting pitchers in 2019 by Grid WAR. 

> **302 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 



**Figure 5:** A game-by-game breakdown of Justin Verlander’s 2019 season. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 303** 

lost by using FWAR to estimate pitcher quality rather than using GWAR. We find that pitcher rankings built from past GWAR are better than pitcher rankings built from past FWAR at predicting future pitcher rankings according to GWAR. This provides evidence that game-by-game variability in pitcher performance is a fundamental and measurable trait. 

##### **3.1 Averaging pitcher performance across games dilutes the contributions of his great games** 

In this section we compare GWAR to FanGraphs WAR (FWAR) in order to understand the effect of averaging pitcher performance over the entire season on valuing pitchers. We find that averaging over the season allows a pitcher’s terrible performances to dilute the contributions of his great ones. Note that to compare the _relative_ value of starting pitchers according to GWAR relative to FWAR(RA∕9), in this section we rescale GWAR in each year so that the sum of GWAR across all starters in each season equals the corresponding sum in FWAR(RA∕9). 

We begin with Figure 6, which visualizes GWAR versus FWAR(RA∕9) for starting pitchers in 2019. Pitchers who lie above the line _y_ = _x_ are undervalued according to GWAR relative to FWAR and pitchers who lie below the line are overvalued. To understand why some players are undervalued and others are overvalued, we compare players who have similar FWAR but different GWAR values in 2019. In Figure 7 we compare Homer Bailey’s 2019 season to Tanner Roark’s. They have the same FWAR(RA∕9), 2.7, but Bailey has a much higher GWAR (Bailey 3.43, Roark 2.48). Similarly, in Figure 8 we compare Mike Fiers’s 2019 season to Aaron 

Nola’s. They have the same FWAR(RA∕9), 4.1, but Fiers has a higher GWAR (Fiers 5.25, Nola 4.2). 

In each of these comparisons, we see a similar trend explaining the differences in GWAR. The pitcher with higher GWAR allows fewer runs in more games and allows more runs in fewer games. This is depicted graphically in the “Difference” histograms, which show the difference between the histogram on the left and the histogram on the right. The green bars denote positive differences (i.e. the pitcher on the left has more games with a given number of runs allowed than the pitcher on the right) and the red bars denote negative differences (i.e. the pitcher on the left has fewer games with a given number of runs allowed than the pitcher on the right). In each of these examples, the green bars are shifted towards the left (pitchers with higher GWAR allow few runs in more games) and the red bars are shifted towards the right (pitchers with lower GWAR allow many runs in more games). In Figure 7, Bailey pitches four more games than Roark in which he allows two runs or fewer and Roark pitches four more games than Bailey in which he allows three runs or more. Similarly, in Figure 8, Fiers pitches four more games than Nola in which he allows zero runs and Nola pitches five more games than Fiers in which he allows one run or more. The convexity of GWAR diminishes the impact of games in which a pitcher allows many runs, explaining why Bailey has more GWAR than Roark and why Fiers has more GWAR than Nola. 

Next, in Figure 9 we visualize GWAR versus FWAR(RA∕9) for each starting pitcher-season across all years from 2010 to 2019. Pitchers who lie above the line _y_ = _x_ (the solid black line) are undervalued according to GWAR relative to FWAR and pitchers who lie below the line are overvalued. Worse pitchers generally lie above the line 



**Figure 6:** Grid WAR ( _y_ -axis) versus FanGraphs WAR (RA∕9) ( _x_ -axis) for each pitcher-season in 2019. The pitcher name refers to the dot on its immediate left. 

> **304 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 



**Figure 7:** Histogram of runs allowed in a game in 2019 for Homer Bailey (left), Tanner Roark (middle), and the difference between these two histograms (right). Even though they have the same FWAR, Bailey has a higher GWAR than Roark because he has more games in which he allows fewer runs. 



**Figure 8:** Histogram of runs allowed in a game in 2019 for Mike Fiers (left), Aaron Nola (middle), and the difference between these two histograms (right). Even though they have the same FWAR, Fiers has a higher GWAR than Nola because he has more games in which he allows fewer runs. 



**Figure 9:** Grid WAR ( _y_ -axis) versus FanGraphs WAR (RA∕9) ( _x_ -axis) for each pitcher-season from 2010 to 2019. The solid black line is _y_ = _x_ and the dashed blue line is the regression line _y_ = 0.47 + 0.85 _x_ . The slope of the regression line is less than 1, indicating that worse pitchers are generally undervalued and better pitchers are generally overvalued by FWAR(RA∕9) relative to GWAR. 

_y_ = _x_ (the solid black line), and so are undervalued, whereas better pitchers generally lie below the line. The regression line _y_ = 0.47 + 0.85 _x_ (the blue dashed line), which has slope less than one, summarizes this phenomenon. This occurs because FWAR averages pitcher performance across an entire season, which dilutes the contributions of his good games. Since Grid WAR is (mostly) convex in runs allowed, GWAR downweights the contribution of the _R_ th run of a game for large _R_ , whereas FWAR weighs all runs allowed in a season equally. Since worse pitchers have many more occurrences than better pitchers of allowing a large number of runs allowed in a game, FWAR(RA∕9) undervalues worse pitchers in general. As we have constrained GWAR and FWAR to have the same sum, FWAR(RA∕9) must therefore overvalue better pitchers in general. 

In Figure 10 we show the six most undervalued and overvalued pitchers according to GWAR relative to 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 305** 



**Figure 10:** The six most undervalued (a) and overvalued (b) pitchers according to GWAR relative to FWAR(RA∕9), aggregated across all seasons from 2010 to 2019. The undervalued pitchers are generally considered worse pitchers and the overvalued pitchers are generally considered better pitchers. 



**Figure 11:** Histogram of Yovani Gallardo’s runs allowed in each game across three seasons. Gallardo has many great and terrible games. Traditional WAR metrics allow his terrible performances to dilute his great ones. 

FWAR(RA∕9), aggregated across all seasons from 2010 to 2019. As expected, the undervalued pitchers are generally considered worse pitchers and the overvalued pitchers are generally considered better pitchers. In Figure 11 we visualize the runs allowed distribution of the most undervalued pitcher, Yovani Gallardo, in his three most undervalued seasons. Gallardo has many great games (say, zero or one run allowed) and many terrible games (say, six or more runs allowed). GWAR diminishes the impact of these terrible games and magnifies the impact of these great games, increasing his estimated contribution to winning. 

As averaging pitcher performance across games allows a pitcher’s worse performances to dilute his better performances, we also expect FanGraphs WAR to undervalue higher variance pitchers. We see this in Figure 12 in which we visualize the relationship between a pitcher’s variability in performance across games and the extent to which he is undervalued by FanGraphs WAR. For each starting pitcher-season from 2010 to 2019 consisting of at least 30 games, we plot the difference between his seasonal GWAR and FWAR(RA∕9) against the game-by-game standard 

deviation of his GWAR. Higher variance pitchers indeed generally have higher GWAR than FWAR. 

##### **3.2 Grid WAR has predictive value** 

Recall that it is wrong to average pitcher performance across games in estimating a starting pitcher’s WAR. This is why we devised Grid WAR, which estimates WAR on a per-game basis and is the right way to estimate historical WAR for starting pitchers. Nonetheless, it is possible _a priori_ that averaging provides a stabler estimate of pitcher quality which is more predictive of future WAR. In particular, if game-by-game variability in pitcher performance is due mostly to chance, accounting for these variations introduces noise into estimates of pitcher quality. 

Because a pitcher’s historical WAR at the end of a season defines how valuable he was during the season, we want a predictive pitcher quality measure to predict his next season’s historical WAR as best as possible. In other words, pitcher quality is simply predicted future historical WAR. Hence our goal is to predict a starting pitcher’s future Grid WAR. _A priori_ , it is not immediately obvious whether 

> **306 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 



**Figure 12:** For each starting pitcher-season from 2010 to 2019 consisting of at least 30 games, the difference between his seasonal GWAR and FWAR(RA∕9) ( _y_ -axis) versus the game-by-game standard deviation of his GWAR ( _x_ -axis). Higher variance pitchers are undervalued by FWAR(RA∕9) because they allow a pitcher’s worse performances to dilute his better performances. 

a pitcher’s past Grid WAR is predictive of his future Grid WAR. In particular, if a pitcher’s game-by-game variance in runs allowed is due mostly to randomness rather than a fundamental identifiable trait, a WAR which averages pitcher performance over the season may be more predictive than Grid WAR of future Grid WAR. Thus, in this section, we compare the predictive capabilities of Grid WAR and FanGraphs WAR. We find that, in predicting future pitcher rankings according to Grid WAR, our predicted pitcher ranking built from Grid WAR is more predictive than that built from FanGraphs WAR. This suggests that some pitchers’ game-bygame variance in performance is a fundamental trait. 

To value a starting pitcher using his previous seasons’ WAR and number of games played, we could simply use his mean game WAR. The fewer games a pitcher has played, however, the less reliable his mean game WAR is in predicting his latent pitcher quality. Therefore, we use shrinkage estimation to construct a pitcher quality metric. In calculating pitcher _p_ ’s quality estimate _𝜇 p_ , the fewer games he has played, the more his mean game WAR is shrunk towards the overall mean pitcher quality. Specifically, we construct three shrinkage estimators of pitcher _p_ ’s quality, denoted _𝜇_<sup>GWAR</sup> _p_ , _𝜇_<sup>FWAR (FIP)</sup> _p_ , and _𝜇_<sup>FWAR (RA/9)</sup> _p_ , built from the three respective WAR metrics. We use a parametric Empirical Bayes approach in the spirit of Brown (2008) to formulate these shrinkage estimators, detailed in Appendix C. 

Recall that our goal is to predict each starting pitcher’s next season’s cumulative Grid WAR, which at the end of next 

season will represent his historical value added. So, using the 2019 season as a hold-out validation set, our goal is to predict each starting pitcher’s 2019 Grid WAR. We use our remaining data from 2010 to 2018 to estimate pitcher quality, built separately from GWAR and FWAR, in order to predict 2019 Grid WAR. Thus we restrict our analysis to the set of starting pitchers who have a FanGraphs’ WAR in at least one season from 2010 to 2018 (so, they must have at least 25 starts in that season). Our pitcher quality estimators, however, are on different scales since each WAR metric is on its own scale. To ensure fair comparison of Grid WAR and FanGraphs WAR, we map each estimator to a starting pitcher ranking, ranking each pitcher from one (best) to the number of pitchers (worst). We denote the three ranks of pitcher _p_ according to _𝜇_<sup>GWAR</sup> _p_ , _𝜇_<sup>FWAR (FIP)</sup> _p_ , and _𝜇_<sup>FWAR (RA/9)</sup> _p_ by _R_<sup>GWAR</sup> _p_ , _R_<sup>FWAR (FIP)</sup> _p_ , and _R_<sup>FWAR (RA/9)</sup> _p_ , respectively. In Figure 22 of Appendix C we visualize these starting pitcher rankings prior to the 2019 season according to these estimators _𝜇 p_ (left) and their associated ranks _R p_ (right). Additionally, we rank pitchers in 2019 by their observed cumulative 2019 Grid WAR, denoted _R_<sup>GWAR</sup> _p_ . Finally, we use root mean squared error (rmse) to measure how well the predicted pitcher rankings _R_ predict the observed rankings _R_ , shown in Table 2. We see that pitcher rankings built from Grid WAR are more predictive than those built from FanGraphs WAR. Formally, _A < B_ and _A < C_ , where _A_ , _B_ , and _C_ are defined in Table 2. In other words, baseball analysts lose value by not using Grid WAR to value pitchers. 

In Tables 3 and 4 we conduct a similar analysis, but restricting the test set to just the five most _undervalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to _R_<sup>FWAR (RA/9)</sup> (in Table 3) and relative to _R_<sup>FWAR (FIP)</sup> (in Table 4). Conversely, in Tables 5 and 6 we conduct a similar analysis, but restricting the test set to just the five most _overvalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to _R_<sup>FWAR (RA/9)</sup> (in Table 5) and relative to _R_<sup>FWAR (FIP)</sup> (in Table 6). We again find that baseball analysts lose value by not using Grid WAR to estimate pitcher quality. In particular, for these “extreme” pitchers who are highly undervalued or highly overvalued, analysts do worse predicting their quality when they use 

**Table 2:** The rmse of the observed pitcher ranking _R_<sup>GWAR</sup> in 2019 and three pitcher ranking estimates _R_ computed from three different WAR metrics. GWAR is more predictive than FWAR of future GWAR. 

|**Symbol**|**Observed ranking****_R_**|**Predicted ranking****_R_**|**rmse(****_R, R_)**|
|---|---|---|---|
|A|_R_<sup>GWAR</sup>|_R_<sup>GWAR</sup>|10.2|
|B|_R_<sup>GWAR</sup>|_R_<sup>FWAR (RA/9)</sup>|12.4|
|C|_R_<sup>GWAR</sup>|_R_<sup>FWAR (FIP)</sup>|13.1|



> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 307** 

**Table 3:** The rmse of the observed pitcher ranking _R_<sup>GWAR</sup> in 2019 and pitcher ranking estimates _R_ computed from three different WAR metrics, using just the five most _undervalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to each _R_<sup>FWAR (RA/9)</sup> . GWAR is more predictive than FWAR(RA∕9) of future GWAR, particularly for undervalued pitchers. 

**Table 5:** The rmse of the observed pitcher ranking _R_<sup>GWAR</sup> in 2019 and pitcher ranking estimates _R_ computed from three different WAR metrics, using just the five most _overvalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to each _R_<sup>FWAR (RA/9)</sup> . GWAR is more predictive than FWAR(RA∕9) of future GWAR, particularly for overvalued pitchers. 

|**Observed ranking****_R_**|**Predicted ranking****_R_**|**rmse(****_R, R_)**|
|---|---|---|
|_R_<sup>GWAR</sup>|_R_<sup>GWAR</sup>|7.2|
|_R_<sup>GWAR</sup>|_R_<sup>FWAR (RA/9)</sup>|15.7|



|**Observed ranking****_R_**|**Predicted ranking****_R_**|**rmse(****_R, R_)**|
|---|---|---|
|_R_<sup>GWAR</sup>|_R_<sup>GWAR</sup>|10.7|
|_R_<sup>GWAR</sup>|_R_<sup>FWAR (RA/9)</sup>|14.0|



**Table 4:** The rmse of the observed pitcher ranking _R_<sup>GWAR</sup> in 2019 and pitcher ranking estimates _R_ computed from three different WAR metrics, using just the five most _undervalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to each _R_<sup>FWAR (FIP)</sup> . GWAR is more predictive than FWAR(FIP) of future GWAR, particularly for undervalued pitchers. 

|**Observed ranking****_R_**|**Predicted ranking****_R_**|**rmse(****_R, R_)**|
|---|---|---|
|_R_<sup>GWAR</sup>|_R_<sup>GWAR</sup>|5.1|
|_R_<sup>GWAR</sup>|_R_<sup>FWAR (FIP)</sup>|15.0|



**Table 6:** The rmse of the observed pitcher ranking _R_<sup>GWAR</sup> in 2019 and pitcher ranking estimates _R_ computed from three different WAR metrics, using just the five most _overvalued_ starting pitchers in 2019 according to _R_<sup>GWAR</sup> relative to each _R_<sup>FWAR (FIP)</sup> . GWAR is more predictive than FWAR(FIP) of future GWAR, particularly for overvalued pitchers. 

|**Observed ranking****_R_**|**Predicted ranking****_R_**|**rmse(****_R, R_)**|
|---|---|---|
|_R_<sup>GWAR</sup>|_R_<sup>GWAR</sup>|10.2|
|_R_<sup>GWAR</sup>|_R_<sup>FWAR (FIP)</sup>|18.0|



FWAR rather than GWAR. In Figure 13 we visualize how our GWAR- and FWAR-based pitcher ranking predictions fare against the observed 2019 GWAR pitcher rankings. Specifically, the blue triangles (our 2019 GWAR-based predictions) are closer to the black squares (the observed 2019 pitcher rankings according to GWAR) than the red dots (our 2019 FWAR(FIP)-based predictions). 

Further, in Figure 14 we visualize the variability of Grid WAR and FanGraphs WAR from season to season. For each pitcher-season from 2011 to 2019, we plot a pitcher’s seasonal WAR against his previous season’s WAR. We see that FWAR(FIP) is more stable from season to season than GWAR 

and FWAR(RA∕9), which have similar levels of season-toseason variability. This makes sense: runs allowed, from which GWAR and FWAR(RA∕9) are constructed, is inherently more noisy than FIP, which doesn’t account for balls in play. Having greater stability across seasons, however, does not mean that FWAR(FIP) is a better pitcher valuation metric than GWAR. As shown previously in this section, an estimate of latent pitcher quality built from GWAR is more predictive of future GWAR than estimates built from FWAR(FIP) and FWAR(RA∕9). Predictiveness of future Grid WAR is a more important quality than year-to-year stability, as a general manager should want to acquire a starting pitcher who will have more Grid WAR in future seasons. 



**Figure 13:** Visualizing the observed pitcher rankings _R_<sup>GWAR</sup> in 2019 and pitcher ranking estimates _R_<sup>FWAR (FIP)</sup> of the five most undervalued (left) and overvalued (right) starting pitchers in 2019 (according to _R_<sup>GWAR</sup> relative to _R_<sup>FWAR (FIP)</sup> ). As the blue triangles (our 2019 GWAR-based predictions) are closer to the black squares (the observed 2019 pitcher rankings according to GWAR) than the red dots (our 2019 FWAR(FIP)-based predictions), GWAR is more predictive than FWAR of future GWAR. 

> **308 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 



**Figure 14:** For each pitcher-season from 2011 to 2019, a pitcher’s seasonal WAR ( _y_ -axis) versus his previous season’s WAR ( _x_ -axis). FWAR(FIP) is more stable from year to year than GWAR or FWAR(RA∕9), which have similar levels of season-to-season variability. 

So, a game-by-game measure of WAR like Grid WAR is not only the right way to measure historical WAR for starting pitchers, but is also predictive of future Grid WAR. In particular, an estimator of latent pitcher talent should be built using Grid WAR or some other game-by-game metric. Now that we have such an estimator of pitcher talent at our disposal, we explore the relationship between a pitcher’s talent according to _𝜇_<sup>GWAR</sup> _p_ and his game-by-game performance. We find that all pitchers have great games, but great pitchers have few terrible games. Therefore, averaging pitcher performance over the entire season dilutes the value of mediocre pitchers’ good games, causing existing WAR metrics to undervalue mediocrity. This agrees with our assessment from the previous section. 

In Figure 15 we provide a sense of the distribution of pitcher talent _̂ 𝜇_<sup>GWAR</sup> _p_ (left) and of the distribution of gameby-game Grid WAR (right). Then, in Figure 16a, we visualize the distribution of game-by-game Grid WAR conditional on 

being a bad pitcher (red), a typical pitcher (green), and a great pitcher (blue), according to _̂ 𝜇_<sup>GWAR</sup> _p_ . Bad pitchers, typical pitchers, and great pitchers all have great games. Great pitchers, on the other hand, pitch many fewer bad games than bad and mediocre pitchers do. In Figure 16b we view this phenomenon through another lens. We visualize the distribution of pitcher quality _̂ 𝜇_<sup>GWAR</sup> _p_ conditional on having a bad game (red), a typical game (green), and a great game (blue). Bad pitchers, typical pitchers, and great pitchers all have great games, but bad games feature a higher proportion of bad pitchers. 

Averaging pitcher performance over the season allows a pitcher’s bad performances to dilute the value of his good ones. Consequently, such WAR metrics like FanGraphs WAR devalue the contributions of mediocre and bad pitchers, who have many more bad games than great pitchers. In short, the baseball community has been undervaluing the contributions of the mediocre. 



**Figure 15:** Distribution of estimated pitcher talent _̂ 𝜇_<sup>GWAR</sup> _p_ (a) and game-by-game Grid WAR (b). The blue lines denote the respective means. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 309** 



**Figure 16:** All pitchers have terrible games, but great pitchers have fewer of them. (a) Shows the distribution of game-by-game Grid WAR conditional on being a bad pitcher (red), a typical pitcher (green), and a great pitcher (blue), according to _̂ 𝜇_<sup>GWAR</sup> _p_ . (b) Shows the distribution of estimated pitcher talent _̂ 𝜇_<sup>GWAR</sup> _p_ conditional on having a bad game (red), a typical game (green), and a great game (blue). 

### **4 Discussion** 

Traditional implementations of WAR for starting pitchers estimate WAR as a function of pitcher performance averaged over the entire season. Averaging pitcher performance, however, allows a pitcher’s bad games to dilute the performances of his good games. One bad “blow-up” game after averaging can reduce a pitcher’s WAR by more than minimum possible WAR in a game. Therefore, a starters’ seasonal WAR should be the sum of the WAR of each of his individual games. Hence we devise Grid WAR, which estimates a starting pitcher’s WAR in each of his games. Grid WAR estimates the context-neutral win probability added above replacement at the point when a pitcher exits the game. Grid WAR is convex in runs allowed, capturing the fundamental baseball principle that you can only lose a game once. 

Comparing starting pitchers’ Grid WAR to his FanGraphs WAR from 2010 to 2019, we find that standard WAR calculations undervalue mediocrity and variability relative to Grid WAR. Because all starters pitch great games, but great starters don’t pitch many terrible games, averaging pitcher performance over a season discounts the contributions of great games by mediocre and bad pitchers. We also show that past performance according to Grid WAR is predictive of future Grid WAR, providing evidence that a pitcher’s runs allowed profile is not entirely random, but is the result of an identifiable game-by-game variation. 

To compare starting pitchers across baseball history through the lens of Grid WAR, we created an interactive 

Shiny app,<sup>19</sup> hosted at https://gridwar.xyz, which displays the Grid WAR results of every starting pitcher game, season, and career since 1952. For many starters, Grid WAR is similar to FanGraphs WAR.<sup>20</sup> Grid WAR, however, looks much more favorably upon the careers of some starters with intrinsic game-by-game variance (that is, the occasional tendency to pitch an awful game).<sup>21</sup> There are many starters that have substantial differences including Whitey Ford and Catfish Hunter. Whitey Ford (resp., Catfish Hunter) has a whopping 25 (resp., 15) more career GWAR than FWAR! Ford is the 49th best starter since 1952 according to FanGraphs (53 FWAR) but is the 19th best according to Grid WAR (78 GWAR). Similarly, Hunter is the 107th best starter since 1952 according to FanGraphs (37 FWAR) but is the 32nd best according to Grid WAR (52 GWAR). What drives this difference? Ford and Hunter are extreme boom-bust pitchers. Standard WAR, from either FanGraphs and Baseball Reference, average pitcher performance across games, allowing these pitchers’ many blow-up games to dilute their great performances which accumulate into huge discrepancies across careers, significantly devaluing them relative 

**19** The website is built using pre-2008 play-by-play data from Retrosheet (2021) and play-by-play data since 2008 from Statcast (2023). We use the baseballr package in R to scrape from each of these data sources (Petti and Gilani 2021). We automatically scrape Statcast data each morning, so the website is up-to-date. 

**20** https://www.fangraphs.com/leaders/major-league?pos=all&lg=all& qual=y&type=8&month=0&ind=0&team=0&rost=0&players=0& startdate=&enddate=&season1=1952&season=2023&stats=sta&sortcol= 20&sortdir=default&pagenum=1&pageitems=2000000000. 

**21** There is an asymmetry due to selection bias: pitchers that are usually awful and occasionally brilliant don’t pitch for long. 

> **310 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

to other starters. To understand the fundamental game-bygame variance of these pitchers, consider Ford’s 1961 season and Hunter’s 1967 season. In 1961 Ford (7.2 GWAR) started 39 games with six complete game shutouts accompanied by seven blow-up games (lower than −0.1 GWAR). Similarly, in 1967 Hunter (4.5 GWAR) started 35 games with five complete game shutouts and four one-run complete games accompanied by eight blow-up games (lower than −0.1 GWAR). Grid WAR, which correctly values pitcher performance in each individual game, sees the value of pitchers having such strong variability across games. The public agrees with us: Catfish Hunter made the Hall-of-Fame (despite having just the 107th best career according to FanGraphs) and Whitey Ford won a Cy Young award in 1961. We continue our discussion of Grid WAR across baseball history in Appendix E. 

While we focus in this paper on developing WAR for starting pitchers, some of the principles we discussed should be used to estimate WAR for relief pitchers, opening pitchers, and batters and some should not. The primary difference between valuing starting and relief pitchers is that opposing batter context matters for valuing the latter but not the former. A relief pitcher who pitches the ninth inning up or down, say, three runs only marginally impacts the game, as its outcome has essentially already been decided. Conversely, a relief pitcher who pitches the ninth inning up or down, say, one run hugely impacts the game. Grid WAR for starting pitchers, as developed in this paper, doesn’t account for opposing batter context and so is not appropriate to value relief pitchers. Nonetheless, due to the massive variability in leverage for relief pitchers across games, relief pitcher WAR should be estimated separately for each game. Perhaps we should construct relief pitcher game WAR using a context-neutral version of win probability added that adjusts for score differential at the time the relief pitcher enters the game. 

Opening pitchers are starting pitchers, so we can use Grid WAR to estimate their value. Grid WAR provides a strong justification for the use of an opener. For concreteness, suppose you are the manager of the 2023 Padres, featuring closer Josh Hader who had a 1.28 ERA through 56 innings in 61 games. For simplicity, suppose Hader pitched for exactly one inning, the ninth inning, in each of 56 games, resulting in 1.7 FanGraphs WAR.<sup>22</sup> Now suppose he had instead pitched just the first inning in 56 games with that ERA, allowing an average of about 0.14 runs per inning, or 0 runs in 86 % of innings and 1 run in 14 % of innings. His 

> **22** https://www.fangraphs.com/players/josh-hader/14212/stats? position=P. 

average context neutral win probability per game would be about 



taking these values of _f_ from Figure 1, resulting in 



seasonal Grid WAR. Our preliminary analysis suggests that Hader would be much more valuable as an opener than as a closer. What drives the difference? Closers aren’t that valuable because many of the games they pitch in are low leverage situations in which the outcome of the game has essentially already been decided. Conversely, the performance of an opening pitcher _always matters_ . Allowing few runs through the first inning is very valuable since those innings always impact the outcome of the game. Of course, our initial analysis is overly simplistic and is intended to be just an impetus for further research. A closing pitcher’s dominant ERA doesn’t necessarily extrapolate to the first inning because, for instance, in each first inning but not necessarily in each ninth inning, a pitcher faces the opposing team’s best batters. A more thorough analysis would also need to account for the following telescoping phenomenon: if we moved the closing pitcher to the opening pitcher position, the setup man would become the closer and the middle relief pitcher would become the setup man; but, we expect the resulting potential loss of WAR to be much smaller than the positive gain in WAR from switching the closer to the opener position. Finally, if many teams used an opening pitcher, replacement-level _𝑤_ rep for openers may change. 

Game-by-game WAR, on the other hand, doesn’t make sense for batters. This largely stems from the fact that each individual batter has just three to five plate appearances in a typical nine-inning game. A batter doesn’t influence any individual game enough for the non-convexity of game-level WAR to meaningfully change his valuation over the course of a season. Also, these aren’t enough plate appearances to allow strong evidence of fundamental variance in batter performance across games to appear in the data. Finally, in each game the starting pitcher is responsible for the vast majority of his team’s (defensive) context (until he is pulled), which is not true for any individual batter. Having said that, in estimating seasonal batter WAR, batter performance should still be adjusted for opposing pitcher quality and park. 

Although Grid WAR improves substantially upon existing estimates of WAR for starting pitchers, our analysis is not without limitations. In particular, the version of Grid WAR described in this paper, as well WAR estimates from 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 311** 

FanGraphs and Baseball Reference, doesn’t adjust for opposing batter quality. Thus, for a pitcher who faces good offensive teams more often than other pitchers do, Grid WAR underestimates his WAR. In our updated version of Grid WAR at gridwar.xyz, we adjust for opposing batter quality via GWAR+ (details are included on the website). Additionally, the current version of Grid WAR doesn’t adjust for the pitcher’s team’s fielding. Thus, for a pitcher who plays with great fielders who reduce his runs allowed, Grid WAR overestimates his WAR. Nonetheless, we expect these adjustments to have a very small impact. In particular, we expect the effect of fielding to have a smaller total impact than ballpark, which itself has a small impact, except at extreme parks like Coors Field. This can be seen in Figure 27: Grid WAR computed with our ridge-adjusted park effects is extremely similar to Grid WAR without park effects. We leave the addition of batting and fielding adjustments to future work. 

Moreover, the distribution of runs scored in a halfinning is not Poisson; more likely it is a zero-inflated Poisson, a more general Conway-Maxwell-Poisson, or a similar distribution on the non-negative integers. Computationally, it is straightforward to modify the _f_ grid formula (Equation (5)) to accommodate different distributions. One interesting modification would adjust to allow different parameters for each inning depending on when a starting pitcher is pulled. In particular, middle relievers tend to be worse than starting pitchers, suggesting a higher value of _𝜆_ for those innings, and closers are often very good pitchers, suggesting a lower value of _𝜆_ . But there are several substantial benefits to sticking with a simpler Poisson model. First, it produces a closed-form formula which is quick to evaluate. Second, a simple parametric model makes it easier to adjust for ballpark (and other confounders like batting quality and fielding quality). Finally, the resulting _f_ grid is reasonable and quite accurate for our purposes. For example, while the Poisson model systematically underestimates the probability of big-deficit late inning comeback, these differences have an insignificant impact on Grid WAR. We leave any adjustment to the half-inning runs distribution as future work. 

Finally, there is a flaw in our Empirical Bayes shrinkage estimator of latent pitcher quality _𝜇 p_ . Formula (20) assumes that _𝜇 p_ remains constant over the entire decade from 2010 to 2019, but player quality is non-stationary over time, and a more elaborate estimator should account for this. In future work we suggest using a similar Empirical Bayes approach to estimate pitcher quality, with weights that decay further back in time (e.g., using exponential decay weighting as 

in Medvedovsky and Patton 2022) in the posterior mean Formulas (20) and (32). 

**Acknowledgments:** The authors thank Eric Babitz and Sam Bauman, who first calculated Grid WAR for starting pitchers and created the name Grid WAR, and Justin Lipitz, Emma Segerman, and Ezra Troy, who contributed to an early version of this paper. 

###### **Research ethics:** Not applicable. 

**Author contributions:** The authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Competing interests:** The authors state no conflict of interest. 

###### **Research funding:** None declared. 

**Data availability:** There is a link to the data in the paper and the raw data can be obtained on request from the corresponding author. 

### **Appendix A: A review of the rules of baseball** 

In a baseball game, two teams of nine players each take turns on offense (batting and baserunning) and defense (fielding and pitching). The game occurs as a sequence of plays, with each play beginning when the pitcher throws a ball that a batter tries to hit with a bat. The objective of the offensive team (batting team) is to hit the ball into the field of play, away from the other team’s players, in order to get on base. The goal of a baserunner is to eventually advance counter-clockwise around all four bases to score a “run”, which occurs when he touches home plate (the position where the batter initially began batting). The defensive team tries to prevent batters from reaching base and scoring runs by getting batters or baserunners “out”, which forces them out of the field of play. The pitcher can get the batter out by throwing three pitches which result in “strikes”. Fielders can get the batter out by catching a batted ball before it touches the ground, and can get a runner out by tagging them with the ball while the runner is not touching a base. The batting team’s turn to bat is over once the defensive team records three outs. The two teams switch back and forth between batting and fielding; one turn batting for each team constitutes an inning. A game is usually composed of nine innings, and the team with the greater number of runs at the end of the game wins. Most games end after the ninth inning, but if scores are tied at that point, extra innings are played (Wikipedia 2023). 

> **312 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

### **Appendix B: Estimating** **_f_ using a mathematical, not a statistical, model** 

In this section, we detail our modeling process for estimating the grid function _f_ = _f_ ( _I, R_ ) which, assuming both teams have randomly drawn offenses, computes the probability a team wins a game after giving up _R_ runs through _I_ complete innings. In particular, we compare statistical models fit from observational data to mathematical probability models, which are superior. 

To account for different run environments across different seasons and leagues (NL vs. AL), we estimate a different grid for each league-season. We begin by estimating _f_ from our observational dataset of half-innings from 2010 to 2019. The response variable is a binary indicator denoting whether the pitcher’s team won the game, and the features are the inning number _I_ , the runs allowed through that half-inning _R_ , the league, and the season. Note that if a home team leads after the top of the 9th inning, then the bottom of the 9th is not played. Therefore, to avoid selection bias, we exclude all 9th inning instances in which a pitcher pitches at home. 

With enough data, the empirical grid (e.g., binning and averaging over all combinations of _I_ and _R_ within a leagueseason) is a great estimator of _f_ . In Figure 17a we visualize the empirical grid fit on a dataset of all half-innings from 2019 in which the home team is in the National League. The function _f_ should be monotonic decreasing in _R_ . In particular, as a pitcher allows more runs through a fixed number of innings, his team is less likely to win the game. It should also be monotonic increasing in _I_ because giving up _R_ runs through _I_ innings is worse than giving up _R_ runs through _I_ + _i_ innings for _i >_ 0, since giving up _R_ runs 

through _I_ + _i_ innings implies a pitcher gave up no more than _R_ runs through _I_ innings. The empirical grid, however, is not monotonic in either _R_ or _I_ because each league-season dataset is not large enough. Moreover, even when we use our entire dataset of all half-innings from 2010 to 2019, the empirical grid is still not monotonic in _R_ or _I_ . 

To force our fitted _f_ to be monotonic, we use XGBoost with monotonic constraints, tuned using cross validation (Chen and Guestrin 2016). We visualize our 2019 NL XGBoost fit in Figure 17b. We indeed see that the fitted _f_ is decreasing in _R_ and increasing in _I_ . Additionally, _R_ ↦ _f_ ( _I, R_ ) is mostly convex: if a pitcher has already allowed a high number of runs, there is a lesser relative impact of throwing an additional run on winning the game. Nonetheless, XGBoost overfits, especially towards the tails (e.g., for _R_ large). For instance, the 2019 NL XGBoost model indicates that the probability of winning a game after allowing 10 runs through 9 innings is about 0.11, which is too large. 

As there is not enough data to use machine learning to fit a separate grid for each league-season without overfitting, we turn to a parametric mathematical model. Indeed, the power of parameterization is that it distills the information of a dataset into a concise form (e.g., into a few parameters), allowing us create a strong model from limited data. Because the runs allowed in a half-inning is a natural number, we begin our parametric quest by supposing that the runs allowed in a half-inning is a Poisson( _𝜆_ ) random variable. In particular, denoting the runs allowed by the pitcher’s team’s batters in inning _i_ by _Xi_ and the runs allowed by the opposing team in inning _i_ (for innings _i_ after the pitcher exits the game), we assume 



Then the probability that a pitcher wins the game after allowing _R_ runs through _I_ innings, assuming win probability 



**Figure 17:** Estimates of the 2019 National League function _R_ ↦ _f_ ( _I, R_ ) using the empirical grid (a) and XGBoost with monotonic constraints (b). 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 313** 

in overtime is 1∕2, is 



If _I_ = 9, this is equal to 





noting that the Skellam distribution arises as a difference of two independent Poisson distributed random variables. Then, we estimate _𝜆_ separately for each league-season by computing each team’s mean runs allowed in each half inning, and then averaging over all teams. 

In Figure 18a we visualize the estimated _f_ according to our Poisson model (11) using the 2019 NL _𝜆_ . We see that _f_ is decreasing in _R_ , increasing in _I_ , convex in the tails of _R_ , and is smooth. Nonetheless, some of the win probability values from this model are unrealistic. For instance, it implies the probability of winning the game after shutting out the opposing team through 9 innings is about 99 %, which is too high, and the probability of winning the game after allowing 10 runs through 9 innings is about 1 %, which is too low. 

The win probability values at both tails of _R_ are too extreme in our original Poisson model (11) because we assume both teams have the same mean runs per inning 

_𝜆_ . This is an unrealistic assumption: in real life, a baseball season involves teams of varying strength playing against each other. When teams of differing batting strength play each other, win probabilities differ. For instance, a great hitting team down seven runs has a larger probability of coming back to win the game than a worse hitting team would. Thus, accounting for random differences in team strength across games should flatten the _f_ ( _I, R_ ) grid. 

On this view, it is more realistic to assume the pitcher’s team and the opposing team have their own runs scored per inning parameters, 



and 



Moreover, to capture the variability in team strength across each of the 30 MLB teams, we impose a positive normal prior, 



We estimate the prior hyperparameters _𝜆_ and _𝜎𝜆_ separately for each league-season by computing each team’s mean and s.d. of the runs allowed in each half inning, respectively, and then averaging over all teams. 

Given _𝜆X_ and _𝜆Y_ , we compute Formula (15) similarly as before using the Poisson and Skellam distributions. We use Monte Carlo integration with _B_ = 100 samples to estimate the posterior mean grid, 



**Figure 18:** Estimates of the 2019 National League function _R_ ↦ _f_ ( _I, R_ ) using our Poisson model (11) with constant _𝜆_ (a) and our Poisson model (17) with a truncated normal prior (16) on two team strength parameters _𝜆X_ and _𝜆Y_ (b). 

> **314 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 



where _𝜆_<sup>(</sup><sup>_b_)</sup> _X_<sup>and</sup><sup>_𝜆_</sup> _Y_<sup>(</sup><sup>_b_)are i.i.d. samples from the prior distribu-</sup> tion (16). 

In Figure 18b we visualize the estimated _f_ according to this Poisson model (17), with prior (16), using the 2019 NL _𝜆_ and _𝜎_<sup>2Weseethat</sup><sup>_f_ismostlylinearin</sup><sup>_R_,rather</sup> _𝜆_<sup>.</sup> than convex, and the values of _f_ when _R_ is large are highly unrealistic. For instance, this model indicates that the probability of winning the game after allowing 10 runs through 9 innings is about 38 %, which is way too high. This is because our model is overdispersed, i.e. the estimated prior variance _𝜎𝜆_<sup>2is too large. For example, too large of a</sup><sup>_𝜎_</sup> _𝜆_<sup>2allows</sup><sup>_𝜆X_and</sup> _𝜆Y_ to be very far apart, so if a pitcher allows 10 runs through 9 innings and _𝜆X_ is much larger than _𝜆Y_ , then his team will have a significant chance of coming back to win. 

To resolve the overdispersion issue, we introduce a tuning parameter _k_ designed to tune the dispersion across team strengths to match observed data, 



In particular, we use _k_ = 0.28, which minimizes the log-loss between the observed win/loss column and predictions from the induced grid _f_ ( _I, R_ | _𝜆, 𝜎𝜆_<sup>2</sup><sup>_, k_). In Figure 19 we</sup> visualize the estimated _f_ according to our Poisson model (17), with tuned dispersion prior (18), using the 2019 NL _𝜆_ and _𝜎_<sup>2</sup><sup>_f_is decreasing in</sup><sup>_R_, increasing in</sup><sup>_I_, and</sup> _𝜆_<sup>. We see that</sup> convex when _R_ is large. In particular, it looks like a smoothed version of the XGBoost grid from Figure 17b. Additionally, the values of the grid at both tails of _R_ seem reasonable. For instance, the model indicates that allowing 0 runs through 



**Figure 19:** Estimates of the 2019 National League function _R_ ↦ _f_ ( _I, R_ ) using our Poisson model (17) with tuned dispersion prior (18). 

9 innings has about a 97 % win probability, which is more reasonable than before. For all of these reasons, we use this model for the grid _f_ to compute Grid WAR for starting pitchers. 

### **Appendix C: Estimating pitcher quality using Empirical Bayes** 

In this section, we describe how we estimate pitcher quality. Given enough data, a pitcher’s mean game WAR would suffice to capture his quality. In the MLB, however, a pitcher starts just a finite number of games per season, so for many pitchers there is not enough data to use just his mean game WAR to represent his quality. Therefore, in this section we use a parametric Empirical Bayes approach in the spirit of Brown (2008) to devise shrinkage estimators _̂ 𝜇_<sup>GWAR</sup> _p_ and _𝜇_<sup>FWAR</sup> _p_ , built from Grid WAR and FanGraphs WAR respectively, to represent pitcher _p_ ’s quality. In particular, _𝜇 p_ shrinks his mean game WAR to the overall mean in proportion to his number of games played. 

##### **C.1 Empirical Bayes estimator of pitcher quality built from Grid WAR** 

To begin, index each starting pitcher by _p_ ∈{1 _,_ … _,_ } and index pitcher _p_ ’s games by _g_ ∈{1 _,_ … _, N p_ }. Let _Xpg_ denote pitcher _p_ ’s observed Grid WAR in game _g_ . After observing his _N p_ games, we model 



In this model, _𝜇 p_ represents pitcher _p_ ’s unobservable “true” pitcher quality, or his latent underlying mean game Grid WAR. Similarly, _𝜎_<sup>2</sup> _p_<sup>represents pitcher</sup><sup>_p_’s latent game-</sup> by-game variance in pitcher quality, or his game-by-game variance in mean game Grid WAR. The prior parameters _𝜇_ and _𝜏_<sup>2</sup> represent the mean and variance, respectively, of pitcher quality across all pitchers. In Figure 20 we visualize the game-level Grid WAR of four starting pitchers. While Grid WAR is not actually normally distributed, it isn’t too unreasonable an approximation (particularly for typical pitchers). In particular, we use a Gaussian model because it produces a good and interpretable estimator of pitcher _p_ ’s latent pitcher quality, not because of accuracy. 

We estimate pitcher _p_ ’s pitcher quality _𝜇 p_ using the posterior mean, which as a result of our normal-normal conjugate model (19) is 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 315** 



**Figure 20:** For four starting pitchers _p_ , the distribution of his game-level GWAR{ _X pg_ } from 2010 to 2018. 



The posterior mean is a weighted sum between the observed total Grid WAR and the overall mean pitcher quality, weighted by the variances _𝜎_<sup>2</sup> _p_<sup>and</sup><sup>_𝜏_2andthenumber</sup> of games played _N p_ . In particular, the more games a pitcher has played, the closer his estimated quality is to his observed mean game Grid WAR. Conversely, the fewer games he has played, the closer his estimated quality is to the overall mean quality. 

Estimator (20), however, is defined in terms of unknown parameters _𝜇_ , _𝜏_<sup>2</sup> , and _𝜎_<sup>2</sup> _p_<sup>.Thus,toeffectivelyusethis</sup> estimator, we employ an Empirical Bayes approach in the spirit of Brown (2008). Specifically, in place of these estimators in Equation (20), we plug in their maximum likelihood estimates (MLE) _𝜇_ , _𝜏_<sup>2</sup> , and _𝜎_<sup>2</sup> _p_<sup>,estimatedfromthe</sup> data { _Xpg_ }. 

We being finding the MLE by noting the marginal distribution of _Xpg_ according to model (19), 



Thus the likelihood of pitcher _p_ ’s data { _Xpg_ : 1 ≤ _g_ ≤ _N p_ } is 



Therefore the log-likelihood of the full dataset { _X pg_ : 1 ≤ _g_ ≤ _N p,_ 1 ≤ _p_ ≤} is 



To find the MLE of _𝜇_ , we set the derivative of the loglikelihood with respect to _𝜇_ equal to 0 and solve for _𝜇_ , 



which yields 



We use a similar approach to find the MLE of _𝜏_<sup>2</sup> and _𝜎_<sup>2</sup> _p_<sup>.</sup> In particular, 

or equivalently 



Additionally, for each pitcher _p_ , 



or equivalently 



This process yields  + 2 Equations (25), (27), and (29) in  + 2 unknown variables _𝜇_ , _𝜏_<sup>2</sup> , and { _𝜎_<sup>2</sup> _p_ }. As suggested in Brown (2008), we solve these equations by iterating until convergence, detailed in iterative Algorithm 1. 

> **316 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

**Algorithm 1.** Compute the MLE of _𝜇, 𝜏_<sup>2</sup> , and <u>{</u> _𝜎_<sup>2</sup> _p_ <u>}</u> from model (21) 

1: **Input:** Grid WAR { _X pg_ : 1 ≤ _p_ ≤ _,_ 1 ≤ _g_ ≤ _N p_ }, _𝜖_ 

2: **Initialization:** 

1 3: _𝜇_ ( _t_ = 0) = <sup>1</sup> ∑ _p N p_ ∑ _g_<sup>_X_</sup> _pg_ 4: _𝜎_<sup>2</sup> _p_<sup>(</sup><sup>_t_= 0) = Var({</sup><sup>_X pg_: 1 ≤</sup><sup>_g_≤</sup><sup>_N p_})</sup> 5: _𝜏_<sup>2</sup> ( _t_ = 0) = Var({ _X pg_ : 1 ≤ _p_ ≤ _,_ 1 ≤ _g_ ≤ _N p_ }) − <sup>1</sup> ∑ _p_<sup>_𝜎_2</sup> _p_<sup>(</sup><sup>_t_= 0)</sup> 

6: _t_ = 1 

7: **while** TRUE **do** 

8: **Step .** Solve for _𝜇_ and save the result as _𝜇_ ( _t_ ): _𝜇_ ( _t_ ) = <u>∑</u> _<u>p,</u>_ ~~∑~~ _pg,Xg pg_ 1∕∕( _𝜏_ (<sup>2</sup> _𝜏_ (<sup>2</sup> _t_ (− _t_ −1)1)++ _𝜎𝜎_<sup>2</sup> _p_<sup>2(</sup> _p_<sup>_t_(−</sup><sup>_t_−1))1))</sup><sup>_._</sup> 9: **Step .** Solve for _𝜏_<sup>2</sup> (e.g., using a root finder) and save the result as _𝜏_<sup>2</sup> ( _t_ ):<sup>∑</sup> _p,g 𝜏_<sup>2</sup> + _𝜎_ 1<sup>2</sup> _p_<sup>(</sup><sup>_t_−1)=∑</sup> _p,g_ ( _𝜏_ (<sup>2</sup> _X_ + _<u>pg𝜎</u>_ −<sup>2</sup> _p𝜇_<sup>(</sup><sup>_t_</sup> (<sup>−</sup> _t_ ))<sup>1))22</sup><sup>_._</sup> 10: **for** _p_ = 1 to  **do** 11: **Step .** Solve for _𝜎_<sup>2</sup> _p_<sup>(e.g., using a root finder) and save the result as</sup><sup>_𝜎_2</sup> _p_<sup>(</sup><sup>_t_):</sup> _g_ ∑ _N_ = _p_ 1 _𝜏_<sup>2</sup> ( _t_ )1+ _𝜎_<sup>2</sup> _p_<sup>=</sup> _g_ ∑ _N_ = _p_ 1 (( _𝜏X_<sup>2</sup> _<u>pg</u>_ ( _t_ −)+ _𝜇𝜎_ ( _t_<sup>2</sup> _p_ ))<sup>)22</sup><sup>_._</sup> 12: **end for** 13: **if** | _𝜇_ ( _t_ ) − _𝜇_ ( _t_ − 1)| _< 𝜖_ , | _𝜏_<sup>2</sup> ( _t_ ) − _𝜏_<sup>2</sup> ( _t_ − 1)| _< 𝜖_ , and | _𝜎_<sup>2</sup> _p_<sup>(</sup><sup>_t_) −</sup><sup>_𝜎_2</sup> _p_<sup>(</sup><sup>_t_−1)|</sup><sup>_< 𝜖_∀</sup><sup>_p_</sup><sup>**then**</sup> 14: **break** the while loop 15: **else** 16: _t_ = _t_ + 1 17: **end if** 18: **end while** 19: **Output:** _̂ 𝜇_ = _𝜇_ ( _t_ ), _̂ 𝜏_<sup>2</sup> = _𝜏_<sup>2</sup> ( _t_ ), _̂ 𝜎_<sup>2</sup> _p_<sup>=</sup><sup>_𝜎_2</sup> _p_<sup>(</sup><sup>_t_)</sup> 

Using our dataset of all starting pitchers from 2010 to 2018,<sup>23</sup> we run Algorithm 1, yielding maximum likelihood estimators of _𝜇_ , _𝜏_<sup>2</sup> , and { _𝜎_<sup>2</sup> _p_ }. With _𝜖_ = 10<sup>−5</sup> , the algorithm converges after just four iterations. Then, we plug these estimators into Formula (20), yielding parametric Empirical Bayes estimators of { _𝜇 p_ }. In Figure 21 we compare these estimates { _𝜇_<sup>_GWAR_</sup> _p_ } to each pitcher’s observed mean game Grid WAR. For players with fewer games played (small gray dots), _𝜇 p_ is shrunk towards the overall mean _𝜇_ . For players with enough games played (large blue dots), _̂ 𝜇 p_ is essentially pitcher _p_ ’s mean game GWAR, lying on the line _y_ = _x_ . 

In Figure 22 we visualize starting pitcher rankings prior to the 2019 season according to _̂ 𝜇 p_ (left) and the associated ranks _R p_ (right). Clayton Kershaw has the highest _̂ 𝜇_<sup>GWAR</sup> _p_ and Ivan Nova has the lowest. 

> **23** Here we just use starting pitcher-seasons whose FanGraphs WAR is available online, because the purpose of crafting our pitcher quality 

> estimates _𝜇 p_ is to compare the predictive capability of Grid WAR to FanGraphs WAR. Specifically, these are the starting pitcher-seasons with at least 25 starts in a season. 

##### **C.2 Empirical Bayes estimator of pitcher quality built from FanGraphs WAR** 

Our estimator _𝜇_<sup>FWAR</sup> _p_ of latent pitcher quality built from pitcher _p_ ’s previous seasons’ observed FanGraphs WAR differs methodologically from our estimator built from Grid WAR in that FWAR is computed on the seasonal level and 



**Figure 21:** For starting pitchers _p_ from 2010 to 2018, his mean game GWAR versus his Empirical Bayes estimator _̂ 𝜇_<sup>GWAR</sup> _p_ . The dashed gray line is the line _y_ = _x_ . 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 317** 



**Figure 22:** Pitcher quality estimates _̂ 𝜇 p_ (a) and their associated ranks _R p_ (b) for a set of starting pitchers prior to the 2019 season. 

GWAR is computed on the game level. Accordingly, we slightly modify the procedure from the previous section. 

To begin, again index each starting pitcher by _p_ ∈ {1 _,_ … _,_ } and index pitcher _p_ ’s games by _g_ ∈{1 _,_ … _, N p_ }. Let _Xpg_ denote pitcher _p_ ’s unobserved FanGraphs WAR in game _g_ . Note that we observe his total FWAR, 



As before, we use model (19), which implies 



Therefore the posterior mean of pitcher _p_ ’s latent pitcher quality _𝜇 p_ is 



This estimator is analogous to that from Equation (20), using FWAR instead of GWAR. 

As before, we use a parametric Empirical Bayes approach to estimate each starting pitcher’s latent quality from his FanGraphs WAR. In particular, we compute maximum likelihood estimates for _𝜇_ , _𝜏_<sup>2</sup> , and { _𝜎_<sup>2</sup> _p_ } using the FanGraphs data { _X p_ }, which we plug in to Formula (32). We again begin finding the MLE by noting the marginal distribution of _X p_ according to model (31), 



Thus the log-likelihood of the full FanGraphs dataset { _X p_ } is proportional to 



Setting the derivative of the log-likelihood with respect to _𝜇_ (resp., _𝜏_<sup>2</sup> ) equal to 0 and solving for _𝜇_ (resp., _𝜏_<sup>2</sup> ) yields the following equations, 



and 



So, in designing an iterative algorithm analogous to Algorithm 1 but for FanGraphs WAR, we replace Equations (25) (Step 1) and (27) (Step 2) with Equations (35) and (36). 

Setting the derivative of the log-likelihood with respect to _𝜎_<sup>2</sup> _p_<sup>equal to 0 and solving for</sup><sup>_𝜎_2</sup> _p_<sup>, however, yields a triv-</sup> ial equation which doesn’t include _𝜎_<sup>2</sup> _p_<sup>.Intuitivelythisis</sup> because we can’t glean information about _𝜎_<sup>2</sup> _p_<sup>since we don’t</sup> observe the game-level FanGraphs WAR _Xpg_ . Therefore, in designing an iterative algorithm analogous to Algorithm 1 

> **318 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

but for FanGraphs WAR, we eliminate Equation (29) (Step 3) and replace _𝜎_<sup>2</sup> _p_<sup>in Steps 1 and 2 with a constant hyperparam-</sup> eter _𝜎_<sup>2</sup> . We then choose the value of _𝜎_<sup>2</sup> which minimizes the 

rmse between resulting estimated pitcher quality _𝜇 p_ and observed mean game FWAR in a hold-out set. We detail the full procedure in Algorithm 2. 

**Algorithm 2.** Compute the MLE of _𝜇_ and _𝜏_<sup>2</sup> from model (31) 

|1:**pr**|**ocedure**1|
|---|---|
|2:|**Input:**FanGraphs WAR {_X p_: 1≤_p_≤},_𝜖_,_𝜎_<sup>2</sup>|
|3:|<br>**Initialization:**<br>|
|4:|_𝜇_(_t_=0)= <sup>1</sup><br><br>∑<br>_p_<sup>_X _</sup>_p_<br>|
|5:|_𝜏_<sup>2</sup>(_t_=0)=Var({_X p_∕_N p_: 1≤_p_≤})−<sup>1</sup><br><sup>_𝜎_2</sup>|
|6:|_t_=1|
|7:|**while**TRUE**do**<br>∑<br>(_X p_∕_N p_)∕(_𝜏_<sup>2</sup>+_𝜎_<sup>2</sup>)|
|8:|**Step .**Solve for_𝜇_and save the result as_𝜇_(_t_):<br>_𝜇_=<br><br>_p_<br>  <br>~~∑~~<br>_p_<br>1∕(_𝜏_<sup>2</sup>+_𝜎_<sup>2</sup>)<br>_._|
|9:|**Step .**Solve for_𝜏_<sup>2 </sup>(e.g., using a root finder) and save the result as_𝜏_<sup>2</sup>(_t_): <sup>∑</sup><br>_p_<br>1<br>_𝜏_<sup>2</sup>+_𝜎_<sup>2</sup> <sup>= ∑</sup><br>_p_<br>(_X p_∕_N p_−_𝜇_)<sup>2</sup><br>(_𝜏_<sup>2</sup>+_𝜎_<sup>2</sup>)<sup>2</sup> <sup>_._</sup>|
|10:|**if**|_𝜇_(_t_)−_𝜇_(_t_−1)|_< 𝜖_and|_𝜏_<sup>2</sup>(_t_)−_𝜏_<sup>2</sup>(_t_−1)|_< 𝜖_**then**|
|11:|**break**the while loop|
|12:|**else**|
|13:|_t_=_t_+1|
|14:|**end if**|
|15:|**end while**|
|16:|**Output:**_𝜇_=_𝜇_(_t_),_𝜏_<sup>2 </sup>=_𝜏_<sup>2</sup>(_t_)|
|17:**e**|**nd procedure**|
|18:||
|19:**p**|**rocedure**2|
|20:|**Input:**FanGraphs WAR {_X p_: 1≤_p_≤},_𝜖_|
|21:|**Initialization:**<br><br><br><br>|
|22:|Split {_X p_} into a training set<br>{<br>_X_<sup>(train)</sup><br>_p_<br>}<br>and a validation set<br>{<br>_X_<sup>(test)</sup><br>_p_<br>}<br><br><br><br>|
|23:|In particular,<br>{<br>_X_<sup>(train)</sup><br>_p_<br>}<br>is all FWAR from 2010 to 2016,<br>{<br>_X_<sup>(test)</sup><br>_p_<br>}<br>is all FWAR from 2017 to 2018|
|24:|Sigmas=vector of smartly chosen positive values|
|25:|Losses=empty vector|
|26:|**for**_𝜎_<sup>2 </sup>in Sigmas**do**<br><br>|
|27:|**Step .**Run Procedure 1 with inputs<br>{<br>_X_<sup>(train)</sup><br>_p_<br>}<br>,_𝜖_, and_𝜎_<sup>2</sup>|
|28:|**Step .**Use_𝜇_and_𝜏_<sup>2 </sup>from Step 1 to estimate pitcher quality_𝜇p_(Formula(32))<br><br>|
|29:|**Step .**Append rmse(<br>{<br>_𝜇p, X_<sup>(test)</sup><br>_p_<br>}<br>) to Losses|
|30:|**end for**|
|31:<br>32:**e**|**Output:**_𝜎_<sup>2</sup><br>_p_ <sup>≡</sup><sup>_𝜎_2, where</sup><sup>_𝜎_2 corresponds to the minimum value in Losses</sup><br>**nd procedure**|



Using the same dataset of starting pitchers from 2010 to 2018 as before, we run Algorithm 2, yielding maximum likelihood estimators of _𝜇_ and _𝜏_<sup>2</sup> and an estimate of _𝜎_<sup>2</sup> _p_<sup>≡</sup><sup>_𝜎_2.</sup> With _𝜖_ = 10<sup>−5</sup> , the algorithm converges again after just four iterations. Then, we plug these estimators into Formula (32), yielding parametric Empirical Bayes estimators of { _𝜇 p_ }. In Figure 23 we compare these estimates { _𝜇_<sup>FWAR</sup> _p_ } to each pitcher’s mean game FanGraphs WAR from 2010 to 2018. As before, for players with fewer games played (small gray dots), _𝜇 p_ is shrunk towards the overall mean _𝜇_ . Also, for players with enough games played (large blue dots), _̂ 𝜇 p_ is 

essentially pitcher _p_ ’s mean game FWAR, lying on the line _y_ = _x_ . 

A weakness of our Empirical Bayes approach is that it assumes latent pitcher quality _𝜇 p_ is constant over the decade from 2010 to 2019. Player quality is, however, nonstationary over time. Therefore, in future work we suggest using a similar Empirical Bayes approach to estimate pitcher quality, except downweighting data further back in time (e.g., using exponential decay weighting as in Medvedovsky and Patton 2022) in the posterior mean Formulas (20) and (32). 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 319** 



**Figure 23:** For starting pitchers _p_ from 2010 to 2018, his mean game FWAR versus his Empirical Bayes estimator _̂ 𝜇_<sup>FWAR</sup> _p_ , built from FWAR(FIP) in (a) and FWAR(RA∕9) in (b). The dashed gray line is the line _y_ = _x_ . 

In Figure 22 we visualize starting pitcher rankings prior to the 2019 season according to _̂ 𝜇 p_ (left) and the associated ranks _R p_ (right). Clayton Kershaw has the highest _̂ 𝜇_<sup>FWAR (FIP)</sup> _p_ and _̂ 𝜇_<sup>FWAR (RA/9)</sup> _p_ , and Ivan Nova has the lowest such values. We see that there is a nontrivial difference between pitcher quality estimates and rankings built from Grid WAR and FanGraphs WAR. 

## **Appendix D: Estimating the park effects** **_𝜶_** 

In this section, we detail why we use ridge regression to estimate park effects. First, in Section D.1, we discuss existing park factors from ESPN, FanGraphs, and Baseball Reference. Then, in Section D.2, we discuss problems with these existing park effects. In Section D.3, we introduce our park effects model, designed to yield park effects which represent the 

expected runs scored in a half-inning at a ballpark above that of an average park, if an average offense faces an average defense. Then, in Sections D.4 and D.5, we conduct two simulation studies which show that ridge repression works better than other methods at estimating park effects. Then, in Section D.6, we show that our ridge park effects have better out-of-sample predictive performance than existing park effects from ESPN and FanGraphs. Finally, in Sections D.7 and 2.6, we discuss our final ridge park effects, fit on data from all half-innings from 2017 to 2019. 

##### **D.1 Existing park effects** 

FanGraphs, Baseball Reference, and ESPN each have runsbased park factors, which are all variations of a common formula: the ratio of runs per game at home to runs per game on the road. In particular, ESPN’s park factors are an unadjusted version of this formula (ESPN 2022), 



FanGraphs modifies this formula by imposing a form of regression onto the park factors (Appelman 2016). In particular, the FanGraphs park factors _𝛼_ FanGraphs are computed via 



> **320 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

where _𝑤_ is a regression weight determined by the number of years in the dataset (e.g., for a three year park factor, _w_ = 0.8). 

Finally, Baseball Reference’s park factors are a long series of adjustments on top of ESPN’s park factors, computed separately for batters and pitchers (Baseball Reference 2022). In particular, Baseball Reference begins with 



for batters and 



for pitchers as base park factors. Then, they apply several adjustments on top of these base values. For instance, they adjust for the quality of the home team and the fact that the batter doesn’t face its own pitchers. These adjustments, however, are a long series of convoluted calculations, so we do not repeat them here. 

##### **D.2 Problems with existing park effects** 

There are several problems with these existing runs-based park effects. First, ESPN and FanGraphs do not adjust for offensive and defensive quality at all, and Baseball Reference adjusts for only a fraction of team quality. It is important to adjust for team quality in order to de-bias the park factors. For example, the Colorado Rockies play in the NL West, a division with good offensive teams such as the Dodgers, Giants, and Padres. So, by ignoring offensive quality in creating park factors, the Rockies’ park factor may be an overestimate, since many of the runs scored at their park may be due to the offensive power of the NL West rather than the park itself. By ignoring team quality, the ESPN and FanGraphs park factors are biased. Baseball Reference’s park factors adjust for the fact that a team doesn’t face its own pitchers, albeit through a convoluted series of ad-hoc calculations. Although adjusting for not facing one’s own pitchers slightly de-biases the park factors, it does not suffice as a full adjustment of the offensive and defensive quality of a team’s schedule. 

Second, these existing runs-based park effects do not come from a statistical model. This makes it more difficult to quantitatively measure which park factors are the “best”, for instance via some loss function. In other words, it is more difficult to quantitatively know that Baseball Reference’s park factors are actually more accurate than FanGraphs’, in some mathematical sense, besides that it claims to adjust for some biases in its derivation, although we discuss a way to 

do so in Section D.6. Another benefit of a statistical model is that it will allow us to adjust for the offensive and defensive quality of a team and its opponents simultaneously. Finally, a statistical model will give us a firm physical interpretation of the park factors. 

Hence, in this paper, we create our own park factors, which are the fitted coefficients of a statistical model that adjusts for team offensive and defensive quality. 

##### **D.3 Our park effects model** 

In this section, we introduce our park effects model, designed to yield park effects which represent the expected runs scored in a half-inning at a ballpark above that of an average park, if an average offense faces an average defense. 

We index each half-inning in our dataset by _i_ , each park by _j_ , and each team-season by _k_ . We define the park matrix **P** so that **P** _ij_ is 1 if the _i_ th half-inning is played in park _j_ , and 0 otherwise. Similarly, we define the offense matrix **O** so that **O** _ik_ is 1 if the _k_ th team-season is on offense during the _i_ th half-inning, and 0 otherwise, and define the defense matrix **D** so that **D** _ik_ is 1 if the _k_ th team-season is on defense during the _i_ th half-inning, and 0 otherwise. We denote the runs scored during the _i_ th half-inning by _yi_ . Then, we model _yi_ using a linear model, 



where _𝜖i_ is mean-zero noise, 



Succinctly, we model 



where 



and 



The coefficients are fitted relative to the first park ANA (the Anaheim Angels) and relative to the first team-season ANA2017 (the Angels in 2017). By including distinct coefficients for each offensive-team-season and each defensiveteam-season, we adjust for offensive and defensive quality simultaneously in fitting our park factors. Finally, in order to make our park effects represent the expected runs scored 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 321** 

in a half-inning at a ballpark above that of an average park, we subtract the mean park effect from each park effect, 



##### **D.4 First simulation study** 

We have a park effects model, Formula (41), but it is not immediately obvious which algorithm we should use to fit the model. In particular, due to multicollinearity in the observed data matrix **X** , ordinary least squares is suboptimal. Hence we run a simulation study in order to test various methods of fitting model (41), using the method which best recovers the “true” simulated park effects as the park factor algorithm to be used in computing Grid WAR: ridge regression. 

**Simulation setup.** In our first simulation study, we assume that the park, team offensive quality, and team defensive quality coefficients are independent. Specifically, we simulate 25 “true” parameter vectors { _𝛽_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>accord-</sup> ing to 



Then, we assemble our data matrix **X** to consist of every half-inning from 2017 to 2019. Then, we simulate 25 “true” outcome vectors { _y_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>according to</sup> 



We use a truncated normal distribution, denoted by +, in order to make _yi_ positive. We round _yi_ so that it is a positive integer, since _yi_ represents the runs scored in the _i_ th inning. Although we don’t directly simulate _𝜖i_ , our simulated _yi_ still adheres to model (43), as it has mean **X** _i_ ∗ _𝛽_ . We choose the values in Formula (47) so that the simulated outcome vectors { _y_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>seem reasonable in representing</sup> the runs scored in a half-inning. 

Our goal is to recover the park effects _𝛽_<sup>(park)</sup> , so our evaluation metric of an estimator _𝛽_ is the average simulation error of the fitted park effects, 



Note that it doesn’t make sense to compare the existing ESPN and FanGraphs park factors to park effects methods based on model (41) as part of this simulation study because 

they are not based on model (41). In fact, ESPN and FanGraphs park effects are not based on any statistical model. Rather, in Section D.6, we separately compare these existing park factors to our model-based park factors. 

**Method 1: OLS without adjusting for team quality.** The naive method of estimating the park factors _𝛽_<sup>(park)</sup> is ordinary least squares regression while ignoring team offensive quality and team defensive quality, as done in Baumer et al. (2015, Formula 11). In other words, fit the park coefficients using OLS on the following model, 



In failing to adjust for offensive and defensive quality, we expect this algorithm to perform poorly. 

**Method 2: OLS.** Next, we adjust for offensive quality, defensive quality, and park simultaneously using ordinary least squares (OLS) on model (41). This method is similar to that from Acharya et al. (2008), although they compute game-level park factors and we compute half-inning-level park factors. This yields an unbiased estimate of the park effects, and so we expect this method to perform better than the previous one. 

**Method 3: Three-Part OLS.** Although OLS using model (41) is unbiased, the fitted coefficients have high variance due to the multicollinearity of the data matrix **X** . In particular, the park matrix **P** is correlated with the offensive team matrix **O** and the defensive team matrix **D** because in each half-inning, either the team on offense or defense is the home team. We may visualize the collinearity in **X** by denoting all of the half-innings (rows) in which the road team is batting by road, denoting the half-innings in which the home team is batting by home, and writing **X** (e.g., for one season of data) as 



To address this collinearity issue, we propose a threepart OLS algorithm. First, we estimate the offensive quality coefficients during half-innings in which the road team is batting. We do so via OLS on the following model, 



This yields a decent estimate _̂ 𝛽_<sup>(off)</sup> of _𝛽_<sup>(off)</sup> , in particular because for one season of innings, **P** road _,_ ∗ = **D** road _,_ ∗, and for multiple seasons of innings, **P** road _,_ ∗ ≃ **D** road _,_ ∗. 

Second, we estimate the defensive quality coefficients during half-innings in which the home team is batting. We do so via OLS using the following model, 



> **322 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

This yields a decent estimate _̂ 𝛽_<sup>(def)</sup> of _𝛽_<sup>(def)</sup> , in particular because **P** _home,_ ∗ ≃ **O** _home,_ ∗. 

Third, we use the fitted team quality coefficients _̂ 𝛽_<sup>(off)</sup> and _𝛽_<sup>(def)</sup> on all half-innings to obtain the park effects. Specifically, we run OLS on the following model, 



yielding fitted park coefficients _̂ 𝛽_<sup>(park)</sup> . 

**Method 4: Ridge.** Finally, we use ridge regression to fit model (41). In the presence of multicollinearity, ridge regression coefficient estimates may improve upon OLS estimates by introducing a small amount of bias in order to reduce the variance of the estimates (Hoerl and Kennard 1970). We tune the ridge parameter _𝜆_ using cross validation. 

**Simulation Results.** Recall from the start of this section that we simulate 25 sets of “true” parameters { _𝛽_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1 and 25 “true” outcome vectors { _y_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>.Then,usingthe</sup> observed data matrix **X** , which consists of all half-innings from 2017 to 2019, we run each of our five methods, yielding parameter estimates, and evaluate them using the average simulation error from Formula (49). We report the results in Table 7. 

The OLS estimator without adjusting for team quality performs worst, as ignoring team quality leads to a biased estimate of the park effects. OLS and three-part OLS, which include proper adjustments for team quality, perform similarly and are second best. Three-part OLS turns out not to be an improvement over OLS because despite the multicollinearity, there is enough linear independence between the batting-road and batting-home half-innings to obtain reasonably accurate team quality estimates. Also, if **X** contains multiple years worth of data, three-part OLS leads to slightly biased estimates of _𝛽_<sup>(off)</sup> and _𝛽_<sup>(def)</sup> since steps one and two only adjust for park. Additionally, three-part OLS uses half as much data to estimate team quality, which is significant because the outcome variable inning runs is 

**Table 7:** Results of our first simulation study. 

|**Method**|**Simulation error**|
|---|---|
|Ridge|**.**|
|OLS|0.0326|
|Three-part OLS|0.0330|
|OLS without adjusting for team quality|0.0610|



The bold value indicates the best method that has the lowest error. 



**Figure 24:** For one of 25 simulations from our first simulation study from Section D.4, plot the “true” park effects against the ridge estimates and the OLS estimates. The line _y_ = _x_ , shown in black, represents a perfect fit between the “true” and fitted park effects. The OLS estimates are biased, whereas the ridge estimates lie more evenly around the line _y_ = _x_ . 

so noisy. Lastly, ridge regression performs the best, and is significantly better than OLS. In Figure 24, we visualize one of the 25 simulations by plotting the “true” park effects against the ridge estimates and the OLS estimates. We see that OLS is biased, whereas ridge lies more evenly around the line _y_ = _x_ . 

##### **D.5 Second simulation study** 

A primary criticism of the first simulation study from Section D.4 is that in actual baseball, the offensive and defensive quality coefficients are not independent. Rather, often times offensive and defensive qualities are correlated within MLB divisions. For instance, in 2021, the Rays, Red Sox, Yankees, and Blue Jays of the AL East each had at least 91 wins, and so were all good offensive teams. Correlated offensive and defensive qualities within divisions introduces additional collinearity into the data matrix **X** , since teams play other teams within their division at a disproportionately high rate. 

Another criticism of the first simulation study is that it treats Colorado’s park effect as a draw from the same distribution as the other park effects, whereas in real life we know Colorado’s park effect is an outlier as a result of the high altitude. 

So, in this section, we conduct a second simulation study which incorporates intra-divisional collinearity and forces Colorado’s park effect to be an outlier. Specifically, we simulate 25 “true” parameter vectors { _𝛽_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>according to</sup> 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 323** 



where DEN refers to Coors Field in Denver, Colorado. In other words, each division has its own offensive and defensive quality means, coercing the offensive and defensive qualities within each division to be correlated. We choose the values in Formula (55) so that the simulated outcome vectors { _y_<sup>[</sup><sup>_m_]</sup> }<sup>25</sup> _m_ =1<sup>seem reasonable in representing the runs</sup> scored in a half-inning. 

Because Colorado is an outlier in this simulation study, we judge our methods based on two loss functions: the Colorado park effect average simulation error, 



and the non-Colorado park effect average simulation error, 



The remainder of the second simulation study proceeds identically to the first simulation study from the previous section. 

We report the results of our second simulation study in Table 8. Again, ridge regression performs the best. In particular, ridge performs significantly better than the other methods on the outlier Colorado, and better than the other methods on the other parks. In Figure 25, we visualize one of the 25 simulations by plotting the “true” park effects against the ridge estimates and the OLS estimates. We see that 

**Table 8:** Results of our second simulation study. 

|**Method**|**Non-Colorado**|**Colorado**|
|---|---|---|
||**simulation error**|**error**|
|Ridge|**.**|**.**|
|OLS|0.0483|0.1791|
|Three-part OLS|0.0490|0.1807|
|OLS without adjusting for team quality|0.0751|0.1893|



The bold value indicates the best method that has the lowest error. 



**Figure 25:** For one of the 25 simulations from our second simulation study from Section D.5, plot the “true” park effects against the ridge estimates and the OLS estimates. The line _y_ = _x_ , shown in black, represents a perfect fit between the “true” and fitted park effects. The OLS estimates are biased, whereas the ridge estimates lie more evenly around the line _y_ = _x_ . In particular, ridge regression much better captures the park effect of the outlier, Denver. 

ridge regression successfully fits the Colorado park effect, whereas OLS significantly overestimates Colorado. Colorado as an outlier in OLS exerts high leverage over the rest of the park effects, swaying their estimates upwards. One might suggest removing the outlier Colorado from the dataset and estimating it separately, but doing weakens the estimates of the other teams in its division as a result of removing too many games from the set schedule which determines the data matrix **X** . So, in both the first simulation study from Section D.4 and the second simulation study from this section, ridge regression most successfully estimates the “true” simulated park effects. 

##### **D.6 Comparing existing park effects and ridge park effects** 

Now, in this section, we compare our ridge park factors, which perform best in our simulation studies from Sections D.4 and D.5, to existing park effects from ESPN and FanGraphs. 

**Transforming ESPN and FanGraphs park factors to an “additive” scale.** Our ridge and OLS park effects of a ballpark, based on model (41), are “additive” in the sense that they represent the expected runs scored in a half-inning at that park above that of an average park, if an average offense faces an average defense. On the other hand, ESPN and FanGraphs park factors, defined in Formulas (37) and (38), are “multiplicative” in the sense that they represent the ratio of runs created at home to runs created on the road. 

> **324 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

Therefore, in order to compare these existing park factors to our park factors, we need to put them on the same scale. In particular, we transform the ESPN and FanGraphs park effects into “additive” park effects. To do so, we take the mean runs scored in a half-inning, 



and multiply it by a “multiplicative” park factor subtracted by 1. For example, if the ESPN Colorado park factor _𝛼_ in 2019 is 1.34, representing that teams score 34 % more runs in Colorado than in other parks, then the transformed “additive” ESPN park factor is 



After this transformation, the ESPN and FanGraphs park factors also represent the expected runs scored in a half-inning at that park above that of an average park. 

**Visualizing these park effect methods.** In Figure 26 we visualize the ridge, OLS, ESPN, and FanGraphs park effects (where the latter two are transformed to an “additive” scale), fit on all half-innings from 2017 to 2019. We use the park abbreviations from Retrosheet, our data source, as discussed in Section 2.2. As expected, we see that ridge park factors are a shrunk version of OLS park factors, and FanGraphs park factors are a shrunk version of ESPN park factors. The FanGraphs and ridge park factors are remarkably similar. Also, as expected, Coors Field (DEN02) has the largest park effect for all four methods. The Texas Ranger’s 

ballpark in Arlington (ARL02) has the second highest park effect for all four methods. These two parks have signifihas the lowest park effect for all four methods. 

Additionally, we visualize how these various park effects impact the Grid WAR of various starting pitchers. In Figure 27, we show the 2019 seasonal Grid WAR for a set of starters without park effects, with ridge park effects, and with (transformed) ESPN park effects. For most pitchers, the impact of including a park adjustment is small. For some pitchers, the impact of an ESPN park adjustment is massive. For instance, the GWAR of Mike Minor and Lance Lynn, who pitched for the Rangers in 2019, each increases by a staggering one whole WAR. Ridge park factors have a much more muted impact than ESPN park factors. This makes sense, as ridge regression shrinks the park coefficients closer to 0. For a few pitchers, however, even the ridge park effects make a nontrivial impact on their GWAR. This also makes sense, as some park effects, such as those of the Mets, Rockies, and Rangers, are far enough from zero. For instance, the GWAR of Noah Syndergaard and Jacob deGrom, who pitched for the Mets, each decreases by about one-quarter of a WAR. 

**Comparing these park effects quantitatively.** In deciding which park effects to use in our final Grid WAR calculations, we quantitatively compare the ridge, OLS, ESPN, and FanGraphs park factors. In particular, we compare the out-of-sample predictive performance of these park effects. 



**Figure 26:** Ridge, OLS, ESPN, and FanGraphs 2019 three-year park effects (where the latter two are transformed to an “additive” scale). The abbreviations are the retrosheet ballpark codes. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 325** 



**Figure 27:** Grid WAR on a set of pitchers from 2019 without park effects (red triangles), with ridge park effects (blue squares), and with ESPN park effects (green circles). 

We begin by fitting each park factor method using data from all half-innings from 2014 to 2016. Note that the OLS and ridge park factors adjust for team offensive and defensive quality, whereas the ESPN and FanGraphs park factors don’t. So, in order to fairly quantitatively compare which of these park factor methods is “best”, we adjust for team quality on all of these methods. Specifically, using the fitted park factors _𝛼_ from 2014 to 2016 for a given method, we regress out team offense and team defense indicators via OLS on the following model, where **P** , **O** , and **D** are the data matrices consisting of all half-innings from 2017 to 2019, 



Then, using these adjusted models based on Formula (60), we predict the expected runs scored _yi_ in each halfinning _i_ from 2017 to 2019, which are out-of-sample predictions relative to the park effects _𝛼_ which were estimated on data from 2014 to 2016. Finally, we compute the out-ofsample RMSE. 

Each of the four methods has the same out-of-sample RMSE, 1.504. For reference, the RMSE of the overall mean is 1.508, so park factors do improve prediction, albeit slightly. But, because the runs scored in a half-inning is so noisy, and because the differences across parks are so slight, out-ofsample RMSE isn’t sensitive enough to quantitatively show which park factors have the best predictive performance. 

To more clearly understand the differences in methods, we calculate the ecological RMSE to quantitatively compare the various park factor methods. This is done by first fixing a ballpark _p_ . Then for each park factor method, we take the mean of the vector of predicted runs scored in each half-inning at the given park _p_ , yielding _<u>y p</u>_ . Then we find the mean of the vector of observed runs scored in each half-inning at that park _p_ , yielding _<u>y p</u>_ . Finally, we compute the RMSE of the regression of <u>(</u> _<u>y p</u>_ ) on <u>(</u> _<u>y p</u>_ ) (each vectors of length 30), yielding the out-of-sample ecological RMSE. In Table 9 we show the out-of-sample ecological RMSE for several park factor methods. The ridge park effects perform best, outperforming the FanGraphs and ESPN park factors, mainly since Ridge adjusts for offensive and defensive quality. The ridge park effects outperform the OLS park effects 

> **326 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

**Table 9:** Out-of-sample ecological RMSE of predicting the runs scored in a half-inning using various park effect methods. 

validation, to fit our park effects, shown in Figure 3 in Section 2.6. 

|**Park effect**|**Ecological RMSE**|
|---|---|
|Ridge|**.**|
|FanGraphs|0.01578|
|ESPN|0.01579|
|OLS|0.01672|
|Overall mean<br>_y_|0.04658|



The bold value indicates the best method that has the lowest error. 

for the same reasons discussed in our simulation studies from Sections D.4 and D.5. 

Hence the ridge regression park effects lead to better out-of-sample predictions of the runs scored in a halfinning than existing park factor methods from ESPN and FanGraphs. 

##### **D.7 2019 three-year park effects** 

As discussed in Sections D.4 and D.5, the ridge park effects outperform other park effect methods in two simulation studies. Further, as discussed in Section D.6, ridge park effects outperform existing park effect methods from ESPN and FanGraphs. Therefore, we use ridge park effects in computing Grid WAR. In particular, we use ridge regression on our observed dataset { _y,_ **X** } consisting of all half-innings from 2017 to 2019, tuning the ridge parameter _𝜆_ using cross 

### **Appendix E: Grid WAR across modern baseball history** 

We visualize the top 15 starting pitcher-seasons of all time by total Grid WAR in Figure 28a. The pitcher with the highest total Grid WAR of all time in a single season is Sandy Koufax and it is not even close. In 1966, he accumulated 11.54 GWAR over 41 games in his final season which is half a game more GWAR than the second best season (Bob Gibson had 11.05 Grid WAR over 34 games in 1968) and the third best (Dwight Gooden had 11.04 Grid WAR over 35 games in 1985). Koufax’s 1966 season is an illuminating example of the value of Grid WAR compared to standard formulations. While his 1966 is the standout season of all time in terms of Grid WAR, it is just the sixth highest seasonal FWAR(RA∕9) and the 20th highest seasonal FWAR(FIP). The other methods incorrectly overweight his three outlying blow-up games (i.e. less than −0.1 GWAR). This is an excellent example of why it is a philosophical mistake to ignore variance and convexity. In 1966, there were two versions of Koufax: the “left arm of God” or worse than replacement. The “left arm of God” threw eight complete game shutouts and 9 one-run complete games. Grid WAR properly accounts for this variation while the standard metrics do not. Among the 15 all time best 



**Figure 28:** The top 15 starting pitcher-seasons post 1951 by total Grid WAR (a) and Grid WAR per game (b). 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 327** 

seasons, no other pitcher appears more than once, while Koufax appears on the list three times (1963, 1965, 1966) with his 1964 season only falling short because Koufax lost a quarter of the season due to injury. Koufax’s “duality” is not just chance variation, it is a systematic attribute and a significant contributor to his early retirement after the 1966 season. 

Grid WAR certainly favors pitchers that start more often and pitch deeper into the game. Consequently, all of the top pitcher-seasons of all time, according to cumulative Grid WAR, occurred prior to 2001. Moreover, no pitcherseason since 2001 has eclipsed 9.1 GWAR (Greinke in 2009 has the highest at 9.068). Just five pitcher seasons since 2009 have eclipsed 8.5 GWAR (Weaver in 2011, deGrom in 2018, Arrieta in 2015, and Greinke in 2009 and 2015), and only two pitcher-seasons since 2016 have eclipsed eight GWAR (deGrom in 2018 and Verlander in 2019). Starting pitchers are fundamentally less valuable today because top starters used to pitch many more games per season and more innings per game. Koufax started every fourth game in 1966, whereas high-end pitchers today start in every fifth game. Furthermore, the complete game is a thing of the past. Today, starters are typically removed prior to the seventh inning as a reaction to the time through the order penalty (Brill et al. 2023). 

We visualize the top 15 starting pitcher-seasons of all time by Grid WAR per game in Figure 28b. Today’s pitchers fare substantially better on a per-start basis. The most efficient individual pitcher-season of all time, subject to starting at least 25 games, is Pedro Martinez who in 2000 

finished with 0.355 Grid WAR over 29 games. Greg Maddux’s 1994 season is second all-time, with 0.330 Grid WAR over 25 games. Greg Maddux has third place too, with 0.328 Grid WAR over 28 games in 1995. These seasons were remarkable in terms of consistency. Pedro had zero blow-up games in 2000. All but two of his games resulted in positive GWAR, and his worst game featured just −0.068 GWAR. Similarly, across 1994 and 1995, Maddux had just five negative GWAR games in 53 starts, with at worst −0.13 GWAR in a game. 

We visualize the top 15 starting pitchers of all time by career Grid WAR per game in Figure 29b. The most efficient starter of all time over his career (minimum of 100 games) is Clayton Kershaw who currently averages 0.208 Grid WAR per start over 410 games. Jacob deGrom is a close second with 0.206 over his 215 games. Pedro Martinez is third with an average of 0.201 over 410 games. Interestingly, only two of the top 10 pitchers of all time by career efficiency played their entire careers prior to 2000 (the exceptions are Whitey Ford and Sandy Koufax). 

We visualize the top 15 starting pitchers of all time by total career Grid WAR in Figure 29a. The pitcher with the most career Grid WAR is Roger Clemens, who accumulated 139.8 GWAR across 24 seasons from 1984 to 2007. The starter with the second highest career Grid WAR, Greg Maddux, doesn’t come close to Clemens, as he accumulated 115.6 GWAR over 23 seasons from 1986 to 2008. Three of the top ten starters according to career GWAR (Clemens, Maddux, and Randy Johnson) played in the 1980s, 90s, and 00s, and the remaining seven (Tom Seaver, Nolan Ryan, Don Sutton, Gaylord Perry, Bert Blyleven, Steve Carlton, and Jim Palmer) 



**Figure 29:** The top 15 starting pitchers post 1951 by career Grid WAR (a) and career Grid WAR per game (b). 

> **328 —** R. S. Brill and A. J. Wyner: Introducing Grid WAR 

played in the 1960s, 70s, and 80s. Just five of the top 25 starters by career Grid WAR, on the other hand, began their career after 2000. The best such starters are Justin Verlander (85.7 GWAR over 19 seasons from 2005 to 2003) and Clayton Kershaw (85.1 GWAR over 16 seasons from 2008 to 2023). These are the 15th and 16th ranked pitchers, and they don’t come anywhere particularly close to Clemens or even Maddux, although their careers aren’t over. As discussed before, 

the pitchers with the highest career Grid WAR come from the previous millennium because top starters back then pitched more games per season and pitched more innings per game. 

Finally, we measure a starters peak performance by the maximum total Grid WAR across all his contiguous four year stretches. We combine a starter’s peak ranking with his ranking by total career Grid WAR using the geometric 



**Figure 30:** The hall-of-fame chart, or the top 30 starting pitchers post 1951 by the geometric mean of career Grid WAR and peak four-year Grid WAR. 

> R. S. Brill and A. J. Wyner: Introducing Grid WAR **— 329** 

mean, GeomMean( _a, b_ ) = √ _a_ ⋅ _b_ . We use the geometric mean as opposed to the arithmetic mean so as to value pitchers much more the closer they are to being the best (rank one). In Figure 30 we show the peak GWAR rank and geometric mean rank of the top 30 starting pitchers post 1951. Greg Maddux has the best geometric mean rank, as he has the second highest career GWAR and the fourth highest peak GWAR. We also include whether the pitcher was elected to the Hall of Fame by the Baseball Writers’ Association of America (BBWAA) or the veteran’s committee (Veterans), and hence call Figure 30 the hall-of-fame chart. Each of these pitchers who aren’t still playing (Kershaw, Verlander, Scherzer), recently retired (Sabathia), or mired by controversy (Clemens, Schilling) made the Hall of Fame, except notably Kevin Brown and Dave Steib ( _#_ 10 and _#_ 29 ranked geometric mean, respectively). These latter two have without a doubt been snubbed and should be in Cooperstown. There are many articles online corroborating this view.<sup>24</sup> 

### **References** 

- Acharya, R.A., Ahmed, A.J., D’Amour, A.N., Lu, H., Morris, C.N., Oglevee, B.D., Peterson, A.W., and Swift, R.N. (2008). Improving major league baseball park factor estimates. _J. Quant. Anal. Sports_ 4: 6,. 

- Albert, J. and Bennett, J. (2003). _Curve ball: baseball, statistics, and the role of chance in the game_ . Copernicus Books, New York. 

- Appelman, D. (2016). Park factors − 5 year regressed, Available at: https://library.fangraphs.com/park-factors-5-yearregressed/. 

- Baseball Reference (2011). Pitcher WAR calculations and details, Available at: https://www.baseball-reference.com/about/war_explained_ pitch.shtml. 

- Baseball Reference (2022). Park adjustments, Available at: https://www .baseball-reference.com/about/parkadjust.shtml. 

- Baumer, B. and Zimbalist, A. (2014). _The sabermetric revolution: assessing the growth of analytics in baseball_ . University of Pennsylvania Press, Philadelphia, Pennysylvania. 

- Baumer, B.S., Jensen, S.T., and Matthews, G.J. (2015). OpenWAR: an open source system for evaluating overall player performance in major league baseball. _J. Quant. Anal. Sports_ 11: 69−84,. 

**24** https://blogs.fangraphs.com/should-kevin-brown-be-in-the-hallof-fame/, https://www.fishstripes.com/22914710/kevin-brown-hall-offame-case. 

- Brill, R.S., Deshpande, S.K., and Wyner, A.J. (2023). A Bayesian analysis of the time through the order penalty in baseball. _J. Quant. Anal. Sports_ 1, https://doi.org/10.1515/jqas-2022-0116. 

- Brown, L.D. (2008). In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies. _Ann. Appl. Stat._ 2: 113−152,. 

- Chen, T. and Guestrin, C. (2016). XGBoost: a scalable tree boosting system. In: _Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, KDD ‘16_ . ACM, New York, NY, USA, pp. 785−794. 

- ESPN (2014). Max Scherzer 2014 game log, Available at: https://www .espn.com/mlb/player/gamelog/_/id/28976/year/2014/category/ pitching. 

- ESPN (2022). MLB park factors − 2019, Available at: https://www.espn .com/mlb/stats/parkfactor/_/year/2019. 

- Fangraphs (2010). Replacement level, Available at: https://library .fangraphs.com/misc/war/replacement-level/. 

- Hoerl, A.E. and Kennard, R.W. (1970). Ridge regression: biased estimation for nonorthogonal problems. _Technometrics_ 12: 55−67,. 

- Lewis, M. (2003). _Moneyball: the art of winning an unfair game_ . WW Norton & Company, New York. 

- Medvedovsky, K. and Patton, A. (2022). _Daily adjusted and regressed Kalman optimized projections_ | _DARKO_ , Available at: https:// apanalytics.shinyapps.io/DARKO/. 

- Petti, B. and Gilani, S. (2021). Baseballr: acquiring and analyzing baseball data. R package version 1.6.0, Available at: https://billpetti.github.io ./baseballr/. 

- Retrosheet (2021). Retrosheet play-by-play data files (event files), Available at: https://www.retrosheet.org/game.htm. 

- Schwarz, A. and Gammons, P. (2005). _The numbers game: baseball’s lifelong fascination with statistics_ . Thomas Dunne Books, New York. 

- Slowinski, P. (2012). WAR for pitchers, Available at: https://library .fangraphs.com/war/calculating-war-pitchers/. 

- Statcast (2023). Statcast search, Available at: https://baseballsavant.mlb .com/statcast_search. 

- Tango, T., Lichtman, M., and Dolphin, A. (2007). _The book: playing the percentages in baseball_ . Potomac Books, Dulles, Virginia. 

- Thorn, J. and Palmer, P. (1984). _The hidden game of baseball: a revolutionary approach to baseball and its statistics_ . Doubleday, Garden City, NY. 

- Wikipedia (2023). Baseball, Available at: https://en.wikipedia.org/wiki/ Baseball. 

- Wolverton, M. (1993). “Support-neutral” statistics − a method of evaluating the true quality of a pitcher’s start. _By The Numbers_ 5: 4−14. 

- Wolverton, M. (1999). The top pitchers of the 1990s: a support-neutral approach, Available at: https://www.baseballprospectus.com/ news/article/416/the-top-pitchers-of-the-1990s-a-support-neutralapproach/. 

- Wolverton, M. (2004). Baseball prospectus basics: the support-neutral stats, Available at: https://www.baseballprospectus.com/news/ article/2590/baseball-prospectus-basics-the-support-neutralstats/. 


