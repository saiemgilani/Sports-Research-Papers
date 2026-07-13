<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2025/2025 - Manager Over and Underachievement (MOU) Index Ranking Soccer Managers - George.pdf -->

# **The Manager Over and Underperformance (MOU) Index: Ranking Soccer Managers** 

Soccer Track 20251420 

## **1. Introduction** 

Data analytics in soccer has seen significant development in recent years. Most elite football clubs employ data analytics departments and many use data to motivate their decisions. The product that is delivered to fans has also changed, with pundits and commentators now regularly citing advanced statistics in broadcasts. In this time many statistics have been developed to judge player performance, but comparatively few to analyze team managers. 

The team manager represents an important role in soccer.<sup>1</sup> While squads are composed of over twenty individual players, each team only employs one team manager. The team’s decision making is often centralized around this individual, more so than in sports such as baseball or American football. The role of these managers is multifaceted, including not only squad decision making but being a representative of the club, handling media duties, instilling a culture within the organization, and the maintenance of the egos of both their playing and coaching staff. The most important job for a manager, however, is to lead a team to success by maximizing their performance. 

This paper seeks to quantify the ability of managers to improve the performance of their players above and beyond expectation. To this end, I develop a novel index based on advanced soccer statistics to directly compare and assess a manager’s capacity to induce player performance at both the squad level and the position group level. I generate a predictive algorithm to predict player performance and compare this with their actual performance to evaluate whether a manager is consistently able to generate higher performance from players. This index represents a novel contribution to the literature on managerial analysis in sports and is one of the first such models to integrate advanced analytics, direct manager comparisons, and the ability to evaluate managers by position groups. 

Existing literature on the impact of managers on subordinate performance in wider labor economics is sparse. In general, research looking at managers has focused on high level organizational leaders such as CEOs (Bennedson, Perez-Gonzalez, & Wolfenzon, 2007; Bennedson, Perez-Gonzalez, & Wolfenzon, 2012) or political leadership (Jones and Olken, 2005) instead of middle management. Papers that have looked more directly at these mid-level bosses have found productivity boosts associated with switching from low quality to high quality managers (Lazear et al., 2015). Most research in this domain has been conducted in sports. In the literature on sports managers, studies have consistently found that there are differences between top rated and bottom rated managers on performance (Muehlheusser et al., 2018). 

> 1 Some organizations in soccer refer to the tactical leader of their team as a manager, while others refer to them as head coaches. This paper will default to referring to these individuals as managers, although these terms are often interchangeable. 



1 

Throughout the literature, there have been attempts to control for the impact of team quality on success to isolate manager effects. Early analysis focused on the development of a statistic for managerial efficiency and its ability to predict survivability in baseball, providing a basis for the literature (Porter and Scully, 1982; Scully, 1994). These earlier studies in the literature focused on the impact of management on winning percentages and extending their tenure (Kahn, 1993; Scully, 1994). Some studies approached this problem by using stochastic frontier production function analyses from Aigner et al. (1977) to predict optimal team performance (Bridgewater, Kahn, and Goodall, 2011; Dawson & Dobson, 2002; Frick and Simmons, 2008). This prediction is most often based on team financial records (Kahn, 1993; Buzzacchi et al., 2021; Frick and Simmons, 2008; Dawson, Dobson, and Gerrard, 2000). In these studies, it has been found that managers who were high level athletes themselves tend to perform well, as do managers who are highly experienced in management (Bridgewater, Kahn, and Goodall, 2011). Additionally, managers can achieve higher points totals by reducing inefficiencies (Frick and Simmons, 2008). 

The research that has been conducted into managerial effects thus far has focused on the determinants of successful managers. On average, managers tend to have a significant influence on sporting and financial performance (Buzzacchi et al., 2021), with some estimating that 19% of team performance variation can be attributed to managers (Anderson and Sally, 2013). While this is lower than some may hope or expect, the existence of any managerial effect provides the opportunity for teams to optimize performance through appropriate manager selection. Managers with significant experience both as a player and a manager can increase the winning percentage and playoff success of their teams (Goodall, Kahn, and Oswald, 2011; Bridgewater, Kahn, and Goodall, 2011). This finding holds across sports, and has been found in basketball (Berri et al., 2009) and baseball (Kahn, 1993). 

Managerial turnover represents a significant hazard for managers, with short term fluctuations in form often resulting in early termination in a field with already short average tenure, emphasizing the need for constant success (Audas, Dobson, and Goddard, 2009; Barros, Frick, and Passos, 2009). The impact of this termination in improving performance, however, has been found to be small (Bryson et al., 2024).  As such, there is constant pressure on managers to improve performance. 

Many of these studies, however, have flaws in their assessment of manager performance. While they correctly try to control team quality, their outcome variables are imperfect measures of team performance. Assessing a manager based on points or winning percentage is logical in sports with a high sample size of games or high scores such as basketball and baseball as teams will have a higher chance of achieving their true value over the course of a season. In a low scoring, low sample size game like soccer, on the other hand, this same analysis is prone to error. Looking, for example, at the regular discrepancy between the true league table and the expected points table (xPTS) indicates that while performance is often correlated with winning, the correlation is imperfect.<sup>2</sup> The use of these variables in past studies is due to the lack of data availability, but with the advances in sports statistics we are now able to more accurately assess team performance. 

> 2 The xPTS table or “Justice” table is a tool to analyze team performance. It calculates the probability of a team winning, drawing, or losing a game based on the expected goals (xG) they generate in a match compared to their opponent, and multiplies these probabilities by the points totals (3 for a win, 1 for a draw, 0 for a loss) to find the amount of points a team has “earned” in a match. These points earned in a season can be divergent from true points totals. Justice tables for the Top 5 Leagues considered in this paper can be found on Understat.com. 



2 

Additionally, existing research is focused on aggregates. This is true in two senses, both looking at aggregates at the managerial level (i.e top vs bottom managers) and looking at teams at the aggregate instead of assessing them as groups of individual units (i.e defenders vs midfielders). This focus on group analysis simplifies the analysis to answer the question of managerial effectiveness but loses granularity through which we can compare managers. Some managers may be specialists instead of generalists, excellent at improving certain players but not others. Additionally, it is valuable to explore the full distribution of managers as done in Berri et al., (2009) to better understand relative performance and to challenge conventional beliefs surrounding the quality of certain figures. 

To answer these gaps in the literature and to advance the statistics regarding the assessment of coaching, this paper introduces the Manager Over and Underperformance (MOU) Index.<sup>3</sup> Following from the work of Berri et al., (2009), the MOU index looks at the deviation of a set of players from their expected performance under a manager instead of their impact on wins or points. Looking at these deviations on an individual level allows for easier analysis of different subsections of teams, giving a more holistic view of a manager’s qualities and strengths. This index also generates a single statistic through which managers can be directly compared, which is calibrated against manager Elo. This index is the first of its kind to leverage the newly developed wealth of soccer statistics. It provides a general formula for easy replication and development, as well as a potential outcome variable through which future studies may be able to better understand the impact of managerial qualities on performance. 

The paper is organized as follows: Section 2 introduces the methodology used in generating the MOU index, as well as an introduction to the data sources. Section 3 presents the main results of the paper by looking at the top and bottom performers on the index as well as attuning the index against manager Elo scores. Section 4 discusses the findings of the study, the strengths and limitations of the index, and potential avenues for future research using this methodology. 

## **2. Methods** 

### **2.1. Estimation** 

While a soccer manager may have many responsibilities, the primary function of the manager is to lead a team to on-field success. While this can be defined as winning trophies or matches, teams must often form more realistic performance expectations based on their means and status. As a result, onfield success can be more broadly defined to claim that a successful manager is one who induces a team to consistently perform above their expectation. To accomplish this, a manager must make individual players, or groups of players, perform above their expected performance. It is from this assumption that I derive my central model in equation (1). 𝑚 (1)<sup>−𝑥𝑥�𝑚</sup> 𝛿𝛿 = 𝜅𝜅<sup>𝑥𝑥𝑚</sup> 𝑚𝑚 𝑥𝑥� 

> 3 This name is a backronym of “Mou,” a popular nickname for Portuguese manager José Mourinho. 



3 

Where δ represents an index value for some manager _m_ over a position group _g_ . This δ is made up of two parts; firstly, the percentage difference in some statistic _x_ from its predicted value , and secondly a dampening factor defined as 𝑥𝑥� 𝜅𝜅 1 



Where _n_ is the number of season-level observations for a manager, and _N_ is the total number of seasons in the sample. This value can then be interpreted as an “unemployment penalty,” reducing the overall value of a manager if they perform well in only one or two seasons, helping us to avoid anomalous observations. 

The value _x_ can be defined broadly to allow for replication with alternative statistics. The only requirements on _x_ to form this index is that it represents some minutes weighted average of player performance. For the current analysis, it is defined as 



Where the value represents the sum of the individual level statistics _x_ for all players _p_ in position group _g_ for season _t_ , weighted by individual minutes played . Equally, the predicted value to which 𝑚𝑚 it is compared, 𝑥𝑥 looks at a weighted average of individual level predictions. The generation of strong predictions is necessary to the development of a sufficient statistic, but this is up to the discretion of 𝜇𝜇 𝑚𝑚 the analyst. The threshold for this prediction may change depending on the availability of data.  𝑥𝑥� 

The major assumption of this model is that when controlling for player quality, the deviation in performance is due to managerial differences in the aggregate. While other factors may influence individual performance such as club dynamics, network effects with groups of players, and various extraneous factors influencing individual players, the variation in position group aggregate performance is primarily attributed to the direct influence of managers or indirect managerial effects. 

### **2.2. Data and Testing** 

I tested this model in the context of men’s football in the “Top 5” European leagues from the beginning of the 2017/2018 season to the conclusion of the 2023/2024 season. Testing for this model was completed using publicly available data taken from various data sources. For the _x_ in my model, I used the DAVIES statistic developed by American Soccer Analysis (ASA).<sup>4</sup> DAVIES attempts to quantify a soccer player’s contribution to their team relative to a “standard” alternative, much like Wins Above Replacement in baseball or Player Efficiency in basketball. The developers of DAVIES first used a group of seventeen statistics to calculate a model for the expected Goals Added by a player 

> 4 DAVIES is a backronym, standing for Determining Added Value of Individual Effectiveness including Style. It was named after Canadian footballer Alphonso Davies. 



4 

through their on-pitch contributions (i.e passing, shooting, dribbling, defending). It then clusters players based on their attributes and statistics into both broad and specific categories for playing roles. This allows for a more granular analysis of a player’s contribution as they fulfil a specific niche, differentiating between individuals who may play the same position in different styles. These groups are then stratified by age and compared, creating a final statistic that reports the Goals Added by a player relative to a similar, average player who plays in the same role and has the same age.<sup>5</sup> 

DAVIES was selected as the statistic of interest for this model due to its ability to directly compare across position groups and its advanced statistical backing. To date, it represents the most complete statistic to compare players across specializations using open source, frequently updated data. DAVIES data is reported at the season level for each player who played in the Top 5 leagues over the course of our dataset. Further DAVIES data is available for some alternative leagues and in top women’s leagues, but the Top 5 European men’s leagues were selected for this first analysis. This was due to the availability of statistics such as Manager Elo with which to benchmark the value, and the ability to generate sufficiently strong predicted values. 

Supplemental data on player statistics and age are obtained from the website FBRef.com, the field’s standard source for open-source data. This data is provided by Opta. FBRef.com also has estimated wage data provided by Capology. For the Top 5 leagues many of these wage statistics are confirmed, but some have been estimated. Estimations are made primarily for youth players or newly promoted teams. I interpolated wage statistics for players who had missing wages in order to create player predictions for all relevant players. More information on this interpolation can be found in the appendix A.2. 

Manager tenure data was taken from Transfermarkt.com, which has appointment and dismissal dates for all teams in the dataset. A manager was attributed a team season if they took control of the team for greater than 50% of the days in the season (a season going from August 1<sup>st</sup> of one year to July 31<sup>st</sup> of the next). Days were selected above matches in charge to quantify manager tenure to consider the work managers are able to implement over periods with no matches such as international breaks and preseason training.<sup>6</sup> 

The data is calibrated primarily by comparing it to an existing measure of manager quality, manager ELO taken from <u>clubelo.com. This rating system uses a traditional ELO rating system like those used</u> in Chess and other events.<sup>7</sup> It awards points to individuals who win in direct competition with others, and subtracts from those who lose.<sup>8</sup> The points awarded or subtracted from the original score is 

> 5 A clear drawback of this statistic is its emphasis on goals added which will naturally favor attacking players in each positional group. A similar goals subtracted model is currently in development in ASA that can eventually be incorporated into the model. 

> 6 Season matches normally run between mid-to-late August each year and mid-to-late May each year, depending on the league. With international tournaments taking place from mid-June to midJuly, and players taking time off, players will generally recommence training towards the end of July for the new season, leading to August 1<sup>st</sup> as a reasonable date for the season threshold. 

> 7 ELO ratings are named after their creator Arpad Elo. 

> 8 The algorithm used for manager ELO rankings is ∆𝐸 where R is the result (1 for win, 0.5 for draw, 0 for loss), K is a constant scalar in this case set to 20, and E is defined as the ex𝐸𝐸= (𝑅𝑅−𝐸𝐸) ∗𝐾𝐾 



5 

proportional to the relative status of the two competitors before the contest. The strength of ELO systems is that with sufficient sample size an ELO rating should approach a true value of quality. It is currently used by FIFA as the primary ranking system for international football teams. As a manager rating system it performs fairly well, but ELO ratings between managers are endogenous to team quality and stature which may artificially inflate or deflate manager ratings based on factors outside their control. 

## **3. Results** 

The results are presented in three parts, firstly presenting the index, then a discussion of the prediction algorithm created for using DAVIES, and finally comparing the model to the existing measure of manager ELO. 𝑥𝑥� 

### **3.1. Manager Over and Underperformance Index** 

Overall, a MOU index value was generated for 241 managers representing 147 teams. The average number of attributed seasons to managers in the sample was 2.83. The MOU Index had a minimum value of -0.190, and a maximum of 0.350. The top and bottom 10 performing managers can be found in Table 1. A full ranking of the 241 managers in the sample can be found in appendix A.1. 

**Table 1** **_: Ranking of the Top 10 and Bottom 10 managers according to MOU Index_** 

||**Manager**|**Rating**||**Manager**|**Rating**|
|---|---|---|---|---|---|
|1|_Jurgen Klopp_|0.350|232|_Frank Kramer_|-0.050|
|2|_Pep Guardiola_|0.321|233|_Steve Bruce_|-0.050|
|3|_Gian Piero Gasperini_|0.286|234|_Jan Siewert_|-0.051|
|4|_Simone Inzaghi_|0.190|235|_Stefan Leitl_|-0.055|
|5|_Stefano Pioli_|0.165|236|_Sergio_|-0.057|
|6|_Julian Nagelsmann_|0.163|237|_Olivier Pantaloni_|-0.058|
|7|_Roberto De Zerbi_|0.084|238|_Christophe Pelissier_|-0.067|
|8|_Bruno Genesio_|0.069|239|_Pepe Bordalas_|-0.069|
|9|_Adi Hutter_|0.068|240|_Christian Streich_|-0.129|
|10|_Juan Carlos Unzue_|0.059|241|_Sean Dyche_|-0.190|



Upon general inspection, the MOU index performs well at separating successful and unsuccessful managers. The top two managers on the index, Jurgen Klopp and Pep Guardiola, are widely considered to be elite managers in the modern game. Similarly, managers such as Julian Nagelsmann, Gian Piero Gasperini, and Roberto De Zerbi have received many plaudits for their ability in recent years. The performance of managers in the bottom 10 is not as clear. While none of these managers are considered top of the field, managers such as Sean Dyche and Pepe Bordalas have been modestly 

1 ante win probability for a team defined as −𝑑 with _dr_ being the difference in ELO (10400 +1) between the two competitors before the contest.𝐸𝐸= 



6 

successful in recent years for their clubs. The appearance of Sean Dyche and Steve Bruce on the section of the list points towards the list favoring attacking managers instead of those who set up defensively, which is a deficiency of the DAVIES statistic.<sup>9</sup> 

A distribution of the MOU Index values can be found in Figure 1. The mean value of the MOU Index is 0.001 which is not significantly different from 0 (t= 0.313, p= 0.754, CI = [-0.005, 0.007]). The distribution is right skewed ( 3= 3.401) and leptokurtic (𝐾 𝐾 = 22.883). This signifies that the distribution is marked by the existence of several outliers, particularly large positive outliers. This indicates that while many managers have little to no correlation with player performance, a number 𝜇𝜇� of managers are associated with either largely positive or largely negative deviations in those performances. This is in keeping with findings from other papers on the differential impact of toplevel managers but the overall substitutability of managers in the field. 



**Figure 1** **_: Distribution of MOU Index Values with Gaussian density function_** 

The interpretation of MOU index values is not entirely clear due to the presence of the dampening factor κ. In the absence of this factor the MOU index would represent the percentage deviation in DAVIES attributed to each manager. However, with this factor involved the index should simply be interpreted as a standalone statistic. 

The MOU Index also gives the ability to look at manager performances with certain position groups in order to both directly compare managers as well as to assess managerial strengths. Figure 2 compares the top 2 managers in the overall index, Jurgen Klopp and Pep Guardiola, on their relative strengths. The top and bottom 10 performing manager position groups can be found in Appendix A.3.<sup>10</sup> 

> 9 Evidence for this can be found in Appendix B.1, where Sean Dyche appears to improve his defensive players, while having underperformances in other areas of the pitch. 

> 10 The index shows great flexibility for analysis. Only a subset of possible permutations and applications are shown here as a proof of concept. 



7 



**Figure 2:** **_A position wise comparison of Jurgen Klopp and Pep Guardiola_** 

### **3.2. Predicting Player Performance** 

The performance and success of the MOU Index is dependent on the choice and quality of the underlying prediction algorithm. The prediction algorithm chosen for the index presented in section 3.1 was the result of an iterative process. Four of the models considered for the index can be found in Table 2. 



8 

### **Table 2** **_: Selected DAVIES Prediction Algorithms_** 

||Dependent Va|riable:|||
|---|---|---|---|---|
||(1)|(2)|(3)|(4)|
|WeeklyWageEUR|0.00001***<br>(0.00000)|0.00001***<br>(0.00000)|0.00001***<br>(0.00000)|0.00000***<br>(0.00000)|
|Age|-0.043***|-0.060***|-0.048***|-0.041***|
||(0.004)|(0.002)|(0.003)|(0.003)|
|Minutes<br>||0.002***<br>(0.00001)|0.002***<br>(0.00001)|0.002***<br>(0.00002)|
|𝐷𝐷𝐸𝐷𝑝−1<br>|||0.189***<br>(0.006)|0.162***<br>(0.008)|
|𝐷𝐷𝐸𝐷𝑝−2||||0.068***<br>(0.007)|
|League|Yes|Yes|Yes|Yes|
|Role|No|Yes|Yes|Yes|
|Constant|1.005***|-1.967***|-2.018***|-2.210***|
||(0.111)|(0.069)|(0.084)|(0.106)|
|Observations<br><br>|14,196|13,811|9,756|6,784|
|𝑅<sup>2</sup><br>|0.132|0.728|0.762|0.773|
|Adjusted𝑅<sup>2</sup>|0.132|0.728|0.762|0.773|
|Resid. Std. Error|1.978<br>(df=14189)|1.108<br>(df=13797)|1.061<br>(df=9741)|1.050<br>(df = 6768)|
|F Statistic|359.934***<br>(df=6; 14189)|2,846.363***<br>(df=13;<br>13797)|2,232.285***<br>(df=14; 9741)|1,538.130***<br>(df=15; 6768)|



**_Notes_** : _Leagues included are Ligue 1, La Liga, Premier League, Bundesliga, and Serie A. Roles included are Creator, Deep Midfielder, Dribbler, Finisher,_ *p<0.1; **p<0.05; ***p<0.01 _Midfielder, Wide Defender, and Central Defender. These variables are included as dummies, not fixed effects specifications._ 

Regression 2 was selected as the eventual prediction algorithm for the final index. It was selected due to its combination of high value (Adjusted = 0.728) and number of observations (13,811). As can be seen in columns 1 and 3, the exclusion of variables included in model 2 significantly reduced 𝑅𝑅<sup>2</sup> 𝑅𝑅<sup>2</sup> 



9 

the of the model, and the inclusion of lagged statistics as in models 3 and 4 increased the of the model but at the cost of thousands of observations.<sup>11</sup> 𝑅𝑅<sup>2</sup> 𝑅𝑅<sup>2</sup> 

This choice of specification resulted in a pure prediction for 13,811 player seasons. The 385 observations lost between model 1 and model 2 were mainly players who had no logged minutes in a given season, which has no impact on analysis. There were 420 observations for whom predictions were not generated. This was mainly due to missing data on weekly wage. To not lose these players, their wage data was interpolated based on a prediction that is detailed in Appendix A.2. Figure 3 shows the relationship between predicted DAVIES and observed DAVIES. It is clear from this figure that the linear regression model is a strong fit for the observed data. 



**Figure 3:** **_DAVIES Prediction vs Observed Value with Line of Best Fit_** 

### **3.3. Comparison with manager ELO** 

To calibrate the MOU index beyond general inspection, it must be shown to perform well against existing measures of manager performance. As mentioned in Section 1 this data on individual manager performance is sparse, but some metrics do exist. I calibrate the model by comparing it to Manager Elo. The plot of the MOU Index against corresponding Manager Elo can be found in Figure 4. The Pearson correlation coefficient between these two variables was 0.4591, demonstrating a modest positive relationship between the two variables. 

> 11 The major driver of the prediction is the minutes variable. This makes sense, as the more minutes played gives more opportunities to add goals. Since the minutes played by players is a choice made by managers (except for in the instance of injuries), this model was preferred to an alternative specification with DAVIES per 90 minutes. 



10 



**Figure 4** **_: MOU Index value vs Manager Elo with Line of Best Fit_** 

This positive correlation is to be expected and a clear sign of the functioning of these two models. Managers who tend to be higher on the index will also tend to have higher Elo ratings. An issue with Elo ratings, however, is that when applied to soccer they are prone to bias. In a game where Elo is commonly used such as chess, each player is given equal material. When comparing managers in soccer teams, however, teams can be quite unevenly matched for player quality. This means that comparatively weak (strong) managers can have biased Elo ratings if they manage comparatively strong (weak) teams. 

This is exhibited in the variation of Elo that can be observed surrounding an index value of 0 in Figure 4. In a perfectly efficient labor market, the best managers would be sorted into the best positions based on merit and we would see both greater discrepancy in Elo ratings but also a higher correlation with the MOU index. The absence of this indicates inefficiency in the sorting of managers to positions. 

While it would be prudent to calibrate the MOU index further, it is at this time not possible. As soccer data develops, there will be more ways to verify and compare this index to alternative measures of manager performance. Additionally, in time, the index will develop with the introduction of new data, and it will be possible to observe whether managers that score higher on the index tend to have more successful careers in management. This index represents a first attempt at the development of a usable statistic on individual managers, which will develop as the field progresses. 

## **4. Discussion** 

The development of the Manager Over and Underperformance Index represents the first of its kind in soccer literature, and one of the only existing statistics to quantify managerial performance. As a metric, the MOU index indicates that there is high substitutability between most top-level managers, in keeping with other findings in the literature.. It is also correlated quite highly with existing metrics of managerial performance such as Manager ELO, while offering many advantages over these alternative statistics. This paper represents a novel contribution to soccer statistics and provides a 



11 

new way to analyze managerial effects, predict a manager’s success, and rate their overall performance. 

The MOU Index has several attributes that improve upon existing statistics. Firstly, it attempts to address the issue of endogeneity in existing metrics by controlling for player quality. Other forms of judging managers, such as points per game, manager ELO, or team success, are intrinsically linked to the players at a manager’s disposal but unrelated to the manager’s quality themselves. The algorithm underlying the MOU Index addresses this by measuring deviation from predicted player performance, allowing for direct comparison for managers between clubs. 

The MOU Index, while here constructed with a specific statistic, represents instead a broad algorithm for the judgement of managers. The formula is generalizable to other statistics or data sources. It is also malleable to advances in player statistics, allowing it to evolve over time as the judgement of player performance improves. 

The data requirements for the MOU Index ensure its transparency and replicability. It uses exclusively easy access open-source data. This data is also provided by several of the most trusted data providers in the sport in Opta and Transfermarkt. Due to the open-source nature of this dataset and the constantly developing state of statistics in world football, the MOU index can expect to only improve in future iterations as the field develops. 

Additionally, the index performs well in predicting managerial performance based on its correlation with ELO and general inspection. Observing whether the managers with higher indices rise to the top of the field in the coming years will further test the quality of its predictions. 

As a new development in the field, the index does come with drawbacks that may be improved in time. Firstly, the model makes several assumptions regarding the operation of clubs. It assumes that any excess deviations in player performance from expected is due to managerial effects. In truth, player deviation from expectation could be a result of a number of extraneous factors: media influence, returns from injury, cultural differences with players moving to different countries, internal politics, as well as other immeasurable factors. I contend that these are all potential factors influencing player performance that can be mediated by more effective management, and as such we can still attribute this deviation for the most part to managerial quality. 

Another critique of the model is that managers may be effective through alternative channels. A manager may have value to a club above and beyond their impact on player performance down to how they interact with the media, how they develop and represent the culture of a club, the commercial draw that a big name or well-liked manager may bring to an organization, or the network effects that may come with former players wanting to work with the manager again and moving to a club that they would have not otherwise. This critique is valid and appears to matter anecdotally in world football, however these effects are largely unquantifiable. If statistics exist to quantify and compare managers on these aspects, the general form of the MOU Index allows for them to be easily integrated to the model. While the index presented in this current paper does not consider these factors, it does not necessarily exclude them from managerial analysis in the future. 

The MOU Index represents a new paradigm in the world of soccer analytics, and a new way of analyzing aspects of the game. While it can be used to compare and contrast managers and assess performance, it also opens up the opportunity for future research. The MOU index could be used in 



12 

the future to try and determine which manager qualities best predict ability such as playing experience, age, or more advanced techniques like natural language processing of weekly press conferences. It has the capacity to look at the relative strengths of managers through their index for different position groups, thus increasing the information that employers may have and reducing current inefficiencies in labor markets. Similarly, it may allow clubs to better match their manager choices to the qualities of their squad to improve performance without the need for significant further investment. 

Overall, the Manager Under and Overperformance Index represents a new way of analyzing football. As statistics improve in the sport, teams and commentators will seek more clarity from data to quantify team, player, and manager performance in a single statistic. While significant strides have been made in this direction on the player and team side in recent years, the MOU index achieves the same goal for managers. 



13 

## **References** 

Aigner, D., Lovell, C. K., & Schmidt, P. (1977). Formulation and estimation of stochastic frontier 

production function models. _Journal of econometrics_ , 6(1), 21-37. 

Anderson, C., & Sally, D. (2013). _The numbers game: Why everything you know about soccer is wrong_ . Penguin. 

Audas, R., Dobson, S., & Goddard, J. (1999). Organizational performance and managerial turnover. 

_Managerial and Decision Economics_ , 20(6), 305-318. 

Barros, C. P., Frick, B., & Passos, J. (2009). Coaching for survival: The hazards of head coach careers in the German ‘Bundesliga’. _Applied Economics_ , 41(25), 3303-3311. 

Bennedsen, M., Perez-Gonzalez, F., & Wolfenzon, D. (2007). _Do CEOs Matter?_ (No. 13-2007). Working paper. 

Bennedsen, M., Pérez-González, F., & Wolfenzon, D. (2012). Estimating the value of the boss: 

Evidence from CEO hospitalization events. _Unpublished working paper. Columbia Business School, New York, NY_ . 

Berri, D. J., Leeds, M., Leeds, E. M., & Mondello, M. (2009). The role of managers in team 

performance. _International Journal of Sport Finance_ , 4(2), 75-93. 

Bridgewater, S., Kahn, L. M., & Goodall, A. H. (2011). Substitution and complementarity between 

managers and subordinates: Evidence from British football. _Labour Economics_ , 18(3), 275286. 

Bryson, A., Buraimo, B., Farnell, A., & Simmons, R. (2024). Special ones? The effect of head coaches on football team performance. _Scottish Journal of Political Economy_ , 71(3), 295-322. Buzzacchi, L., Caviggioli, F., Milone, F. L., & Scotti, D. (2021). Impact and efficiency ranking of 

football managers in the Italian Serie A: Sport and financial performance. _Journal of Sports Economics_ , 22(7), 744-776. 



14 

Dawson, P., & Dobson, S. (2002). Managerial efficiency and human capital: an application to English association football. _Managerial and Decision Economics_ , 23(8), 471-486. 

Dawson, P., Dobson, S., & Gerrard, B. (2000). Estimating coaching efficiency in professional team sports: Evidence from English association football. _Scottish Journal of Political Economy_ , 47(4), 399-421. 

Frick, B., & Simmons, R. (2008). The impact of managerial quality on organizational performance: Evidence from German soccer. _Managerial and Decision Economics_ , 29(7), 593-600. Goodall, A. H., Kahn, L. M., & Oswald, A. J. (2011). Why do leaders matter? A study of expert 

knowledge in a superstar setting. _Journal of Economic Behavior & Organization_ , 77(3), 265284. 

Jones, B. F., & Olken, B. A. (2005). Do leaders matter? National leadership and growth since World War II. _The Quarterly Journal of Economics_ , _120_ (3), 835-864. 

Kahn, L. M. (1993). Managerial quality, team success, and individual player performance in major league baseball. _ILR Review_ , 46(3), 531-547. 

Lazear, E. P., Shaw, K. L., & Stanton, C. T. (2015). The value of bosses. _Journal of Labor Economics_ , 33(4), 823-861. 

Muehlheusser, G., Schneemann, S., Sliwka, D., & Wallmeier, N. (2018). The contribution of managers to organizational success: Evidence from German soccer _. Journal of Sports Economics_ , 19(6), 786-819. 

Porter, P. K., & Scully, G. W. (1982). Measuring managerial efficiency: The case of baseball _. Southern Economic Journal_ , 642-650. 

Scully, G. W. (1994). Managerial efficiency and survivability in professional team sports. _Managerial and Decision Economics_ , 15(5), 403-411. 



15 

## **Appendix** 

### **Appendix A.1: Ranking of All Managers by MOU Index** 

||**Manager**|**Rating**||**Manager**|**Rating**||**Manager**|**Rating**|
|---|---|---|---|---|---|---|---|---|
|1|_Jurgen Klopp_|0.350|31|_Manuel Pellegrini_|0.034|61|_Giuseppe Iachini_|0.016|
|2|_Pep Guardiola_|0.321|32|_Robert Moreno_|0.033|62|_Marcelo Bielsa_|0.016|
|3|_Gian Piero Gasperini_|0.286|33|_Mauricio Pochettino_|0.032|63|_Paco Lopez_|0.016|
|4|_Simone Inzaghi_|0.190|34|_Michel Der Zakarian_|0.032|64|_Alfred Schreuder_|0.015|
|5|_Stefano Pioli_|0.165|35|_Marcelino_|0.031|65|_Frederic Hantz_|0.014|
|6|_Julian Nagelsmann_|0.163|36|_Luciano Spalletti_|0.030|66|_Oliver Glasner_|0.013|
|7|_Roberto De Zerbi_|0.084|37|_Carlo Ancelotti_|0.029|67|_Niko Kovac_|0.012|
|8|_Bruno Genesio_|0.069|38|_Pablo Machin_|0.029|68|_Christian Gourcuff_|0.012|
|9|_Adi Hutter_|0.068|39|_Andre Breitenreiter_|0.029|69|_Julen Lopetegui_|0.012|
|10|_Juan Carlos Unzue_|0.059|40|_Zinedine Zidane_|0.029|70|_Dieter Hecking_|0.010|
|11|_Paolo Fonseca_|0.055|41|_Pellegrino Matarazzo_|0.028|71|_Thomas Frank_|0.009|
|12|_Hansi Flick_|0.050|42|_Eddie Howe_|0.028|72|_Juan Muniz_|0.009|
|13|_Sebastian Hoeness_|0.049|43|_Ernesto Valverde_|0.028|73|_Unai Emery_|0.009|
|14|_Antonio Conte_|0.048|44|_Gerardo Seoane_|0.028|74|_Vincent Hognon_|0.008|
|15|_Franck Haise_|0.047|45|_Rudi Garcia_|0.027|75|_Vicente Moreno_|0.007|
|16|_Thomas Tuchel_|0.045|46|_Andoni Iraola_|0.026|76|_Xavi_|0.007|
|17|_Peter Bosz_|0.045|47|_Stephane Jobard_|0.026|77|_Jose Luis Mendilibar_|0.006|
|18|_Jupp Heynckes_|0.045|48|_Igor Tudor_|0.024|78|_Achim Beierlorzer_|0.006|
|19|_Ange Postecoglou_|0.043|49|_Philippe Montanier_|0.024|79|_Olivier Dall'Oglio_|0.006|
|20|_Lucien Favre_|0.043|50|_Gennaro Gattuso_|0.024|80|_Sinisa Mihajlovic_|0.005|
|21|_Laurent Blanc_|0.042|51|_Maurizio Sarri_|0.023|81|_Jesse Marsch_|0.005|
|22|_Edin Terzic_|0.041|52|_Eusebio Di Francesco_|0.023|82|_Alessio Dionisi_|0.005|
|23|_Marco Rose_|0.039|53|_Michel_|0.022|83|_Eusebio_|0.005|
|24|_Will Still_|0.039|54|_Philippe Clement_|0.022|84|_Quique Setien_|0.004|
|25|_Mikel Arteta_|0.038|55|_Gabriele Cioffi_|0.022|85|_Raffaele Palladino_|0.004|
|26|_Alessio Lisci_|0.037|56|_Ralf Rangnick_|0.021|86|_Rubi_|0.004|
|27|_Arsene Wenger_|0.037|57|_Peter Stoger_|0.019|87|_Patrick Vieira_|0.003|
|28|_Julien Stephan_|0.036|58|_Andrea Sottil_|0.018|88|_Domenico Tedesco_|0.003|
|29|_Xabi Alonso_|0.035|59|_Cuco Ziganda_|0.017|89|_Erik ten Hag_|0.002|
|30|_Pierre Sage_|0.035|60|_Frank Lampard_|0.016|90|_Andre Villas-Boas_|0.002|





16 

|91|_Steffen Baumgart_|0.002|126|_Patrice Garande_|-0.008|161|_Asier Garitano_|-0.019|
|---|---|---|---|---|---|---|---|---|
|92|_Nuno Espirito Santo_|0.002|127|_Vahid Halilhodzic_|-0.008|162|_Albert Celades_|-0.019|
|93|_Carles Martinez_|0.001|128|_Ole Werner_|-0.008|163|_David Wagner_|-0.019|
|94|_Alain Casanova_|0.001|129|_Antoine Kombouare_|-0.009|164|_Walter Mazzarri_|-0.019|
|95|_Brendan Rodgers_|0.001|130|_Roberto D'Aversa_|-0.009|165|_Roberto Donadoni_|-0.019|
|96|_Claude Puel_|0.001|131|_Rob Edwards_|-0.009|166|_Thiago Motta_|-0.020|
|97|_Gustavo Poyet_|0.001|132|_Laszlo Boloni_|-0.009|167|_Luka Elsner_|-0.020|
|98|_Graham Potter_|0.000|133|_Jean-Louis Gasset_|-0.010|168|_Tayfun Korkut_|-0.020|
|99|_Andrea Pirlo_|0.000|134|_Daniele De Rossi_|-0.010|169|_Sabri Lamouchi_|-0.020|
|100|_Xavier Pimienta_|0.000|135|_Marco Giampaolo_|-0.010|170|_Pacheta_|-0.021|
|101|_Dino Toppmoller_|0.000|136|_Jagoba Arrasate_|-0.011|171|_Leonardo Semplici_|-0.021|
|102|_Luis Enrique_|-0.001|137|_Gary O'Neil_|-0.011|172|_Ruben Baraja_|-0.021|
|103|_Eric Roy_|-0.001|138|_Diego Lopez_|-0.011|173|_Walter Zenga_|-0.022|
|104|_Imanol Alguacil_|-0.002|139|_Leonardo Jardim_|-0.011|174|_Dean Smith_|-0.022|
|105|_Francesco Farioli_|-0.002|140|_Abelardo_|-0.011|175|_Quique Flores_|-0.022|
|106|_Luis Garcia_|-0.002|141|_Ole Gunnar Solskjaer_|-0.012|176|_Pal Dardai_|-0.022|
|107|_Francisco Rodriguez_|-0.002|142|_Stefan Ruthenbeck_|-0.012|177|_Patrick Kisnorbo_|-0.022|
|108|_Bo Svensson_|-0.003|143|_Jess Thorup_|-0.012|178|_Jose Mourinho_|-0.022|
|109|_Cesare Prandelli_|-0.003|144|_Uwe Rosler_|-0.013|179|_Ralph Hasenhuttl_|-0.022|
|110|_Jorge Sampaoli_|-0.003|145|_Marco Silva_|-0.013|180|_Pascal Dupraz_|-0.023|
|111|_Ronald Koeman_|-0.004|146|_Stephane Moulin_|-0.014|181|_Sam Allardyce_|-0.023|
|112|_Christophe Galtier_|-0.004|147|_Jocelyn Gourvennec_|-0.014|182|_Neil Warnock_|-0.024|
|113|_Heiko Herrlich_|-0.004|148|_Giovanni Stroppa_|-0.015|183|_Luca Gotti_|-0.024|
|114|_Steven Gerrard_|-0.004|149|_Javi Gracia_|-0.015|184|_Thierry Laurey_|-0.024|
|115|_Bernard Blaquart_|-0.004|150|_Bruno Labbadia_|-0.016|185|_Davide Nicola_|-0.024|
|116|_Vladimir Petkovic_|-0.005|151|_Manuel Baum_|-0.016|186|_Diego Martinez_|-0.025|
|117|_Daniel Farke_|-0.005|152|_Frank Schmidt_|-0.016|187|_Javier Aguirre_|-0.025|
|118|_Paulo Sousa_|-0.005|153|_Vincenzo Italiano_|-0.016|188|_Davide Ballardini_|-0.026|
|119|_Markus Gisdol_|-0.005|154|_Aurelio Andreazzoli_|-0.016|189|_Rolando Maran_|-0.026|
|120|_Fabio Liverani_|-0.007|155|_Regis Le Bris_|-0.017|190|_Florian Kohfeldt_|-0.026|
|121|_Eduardo Coudet_|-0.007|156|_Gerald Baticle_|-0.017|191|_Massimiliano Allegri_|-0.026|
|122|_Rafael Benitez_|-0.007|157|_Carlos Carvalhal_|-0.017|192|_Mauricio Pellegrino_|-0.026|
|123|_Bruno Lage_|-0.007|158|_Scott Parker_|-0.018|193|_Ivan Juric_|-0.026|
|124|_David Arteaga_|-0.007|159|_Thomas Letsch_|-0.018|194|_Oscar Garcia_|-0.027|
|125|Fabio Liverani|-0.007|160|Friedhelm Funkel|-0.018|195|Marco Zaffaroni|-0.027|





17 

|196|_David Guion_|-0.028|212|_Gaizka Garitano_|-0.032|228|_Urs Fischer_|-0.041|
|---|---|---|---|---|---|---|---|---|
|197|_Jean-Louis Garcia_|-0.028|213|_Fabio Pecchia_|-0.033|229|_Enrico Maassen_|-0.042|
|198|_Martin Schmidt_|-0.028|214|_David Linares_|-0.035|230|_Markus Weinzierl_|-0.042|
|199|_Marco Baroni_|-0.029|215|_Sebastien Desmazeau_|-0.035|231|_Fabien Mercadal_|-0.046|
|200|_Nigel Pearson_|-0.029|216|_Uwe Neuhaus_|-0.035|232|_Michael Kollner_|-0.046|
|201|_Paolo Zanetti_|-0.029|217|_Diego Simeone_|-0.035|233|_Sergio_|-0.048|
|202|_Roy Hodgson_|-0.029|218|_Torsten Lieberknecht_|-0.037|234|_Steve Bruce_|-0.050|
|203|_Vincent Kompany_|-0.030|219|_Steve Cooper_|-0.037|235|_Olivier Pantaloni_|-0.050|
|204|_Domenico Di Carlo_|-0.030|220|_Thomas Reis_|-0.037|236|_Frank Kramer_|-0.050|
|205|_Pascal Gastien_|-0.030|221|_Claudio Ranieri_|-0.038|237|_Jan Siewert_|-0.051|
|206|_Alberto Gilardino_|-0.030|222|_Chris Hughton_|-0.039|238|_Stefan Leitl_|-0.054|
|207|_Sandro Schwarz_|-0.031|223|_Alvaro Cervera_|-0.040|239|_Christophe Pelissier_|-0.061|
|208|_Filippo Inzaghi_|-0.031|224|_Jerome Arpinon_|-0.040|240|_Pepe Bordalas_|-0.068|
|209|_Bruno Irles_|-0.031|225|_Chris Wilder_|-0.041|241|_Christian Streich_|-0.115|
|210|_Frederic Antonetti_|-0.031|226|_Dejan Stankovic_|-0.041|242|_Sean Dyche_|-0.171|
|211|_Alexander Blessin_|-0.032|227|_David Moyes_|-0.041||||





18 

### **Appendix A.2: Regression Table for Interpolation of Wage Data** 

||Dependent Variable<br>WeeklyWageEUR|
|---|---|
|Age|3,451.084***<br>(123.279)|
|Role|Yes|
|Team|Yes|
|Constant<br>|-101,073.100***<br>(12,702.420)|
|Observations<br><br>|13,810|
|𝑅<sup>2</sup><br>|0.479|
|Adjusted𝑅<sup>2</sup>|0.474|
|Resid. Std. Error|56,881.610<br>(df=13657)|
|F Statistic|82.747***<br>(df=152;13657)|
||*p<0.1;**p<0.05;***p<0.01|





19 

### **Appendix A.3: Top and Bottom 10 Manager and Position Groups** 

||**Manager**|**Position**|**Rating**||**Manager**|**Position**|**Rating**|
|---|---|---|---|---|---|---|---|
|1|_Gian Piero Gasperini_|_Dribbler_|0.779|1677|_Erik ten Hag_|_Creator_|-0.039|
|2|_Pepe Bordalas_|_Deep Mid._|0.577|1678|_Roberto Donadoni_|_Midfielder_|-0.039|
|3|_Gian Piero Gasperini_|_Creator_|0.516|1679|_Walter Zenga_|_Deep Mid._|-0.040|
|4|_Marcelo Bielsa_|_Midfielder_|0.516|1680|_Pepe Bordalas_|_Midfielder_|-0.040|
|5|_Gian Piero Gasperini_|_Finisher_|0.508|1681|_Dejan Stankovic_|_Dribbler_|-0.042|
|6|_Jurgen Klopp_|_Finisher_|0.482|1682|_Michael Kollner_|_Finisher_|-0.046|
|7|_Simone Inzaghi_|_Creator_|0.476|1683|_Christian Streich_|_Wide Def._|-0.048|
|8|_Jurgen Klopp_|_Dribbler_|0.451|1684|_Aurelio_<br>_Andreazzoli_|_Finisher_|-0.052|
|9|_Pep Guardiola_|_Finisher_|0.423|1685|_Sean Dyche_|_Dribbler_|-0.089|
|10|_Pep Guardiola_|_Cent. Def._|0.353|1686|_Sean Dyche_|_Creator_|-0.119|





20 

### **Appendix B.1: Chart of Sean Dyche’s Position-wise Performance** 





21 


