<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2012/2012 - Effort vs. Concentration The Asymmetric Impact of Pressure on NBA Performance - Unknown Authors.pdf -->

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



# Effort vs. Concentration: The Asymmetric Impact of Pressure on NBA Performance<sup>1</sup> 

Matt Goldman UC San Diego Dept. of Economics La Jolla, CA 92093 mrgoldman@ucsd.edu 

Justin M. Rao Yahoo! Research Santa Clara, CA 95054 jmrao@yahoo-inc.com 

## Abstract 

How and why does performance change under pressure? Psychologists have argued that pressure can both distract, motivate and generate too much self-focus (thinking about the details of how one should accomplish a goal, as opposed to “just doing it"). Studies have implicated self-focus as the key factor in pressure-associated performance declines. To understand if these results extend to highly trained experts, we examine two fundamentally different actions within the context of the same professional sport, basketball. The first action, free throw shooting, requires quiet concentration, while the second, offensive rebounding, is based on effort exerted in the heat of the moment. Home vs. Away variation allows us to understand how a supportive audience moderates the impact of pressure. Using a dataset over 1.3 million possessions and 300,000 free-throws, we find that home free throw shooters do significantly worse in clutch situations, with the effect being larger for poor shooters. Road players show no change in behavior under pressure, indicating distraction plays a limited role in this task. In stark contrast, the home team gets significantly better at offensive rebounding in pressure packed moments, while again the road team shows no relationship between performance and pressure. The results show a clear asymmetric impact of a supportive audience—it can both inspire effort and lead to detrimental self-focus, even for experienced agents. From a sports perspective, it shows how the traditional notion of home-court advantage is not inconsistent with some pressure-related disadvantages (“home choke"). 

> 1We thank Douglas J. Brown for detailed comments on the manuscript. Ned Augenblick provided many helpful comments. 

0 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



## 1 Introduction 

At some point, nearly everyone has to perform under pressure. Pressure can come in the form of, for example, large audiences, increased financial stakes or the presence of an individual one particularly wants to impress. In laboratory studies of motor action (ex. golf putting) and cognitive problem solving (ex. math problems), novices tend to perform worse when pressure inducing factors are experimentally heightened (Baumeister, 1984; Lewis and Linder, 1997; Beilock et al., 2002; Wilson et al., 2007; Gucciardi and Dimmock, 2008). This performance drop has been linked to increased “self-focus"—disruptive concentration on how to perform the task at hand. In motor action, this means too much attention is applied to “do the right motion" and this serves to disrupt the natural or “automatic" ability to perform. To understand this point, consider the act of shooting a free throw in basketball. A self-focused player might think “lead with the legs, elbow-in, follow-through straight," while his relaxed counterpart simply shoots the ball as practiced. In experiments that are designed to lower self-focus in a high pressure situation, for instance by requiring the subject to call out random letters at fixed intervals, the negative effect of pressure tends to decrease or go away entirely (Lewis and Linder, 1997; Beilock et al., 2002). 

A criticism these papers have faced is that the average subject, or even an amateur athlete, has little experience dealing with the particular type of pressure induced in a laboratory study. Observation of behavior in familiar settings in the field may be both more interesting and of more practical relevance. This paper addresses the question: how do highly incentivized experts respond to pressure in their day to day performance? Prior work has studied professional athletes to address this question. Initial findings that home-teams “choke" in championship games (Baumeister and Showers, 1986) were driven by small samples, and have not held up (Schlenker et al., 1995). Wright et al. 1991 find that golfers tend to play worse than expected in their hometown—the authors conclude that this is because they choke under the pressure of disappointing their home fans. However since all golf courses and player composition in a tournament are different, the analysis is hampered by the fact that it is hard to know how well the players “should do." Other authors have argued that the “home-choke" phenomenon is real, but supportive data are scarce (Wallace et al., 2005; Dohmen, 2008).<sup>2</sup> 

To study the question of how experts perform under pressure one would ideally satisfy the following conditions: 1) a well-defined action with outcomes that map directly to success or failure of the team 2) a precise metric of the importance (pressure) of the situation facing the athlete3) a large sample of data of the situation occurring in high and low pressure situations 4) different motor tasks satisfying (1-3) allowing for different levels of self-focus. Free throws and offensive rebounds in National Basketball Association (NBA) games meet all these requirements. Freethrow attempts and offensive rebounding opportunities can be isolated in any play-by-play log, and it is safe to assume that the free throw shooter’s goal is to make the shot while the rebounding team’s goal is to secure the ball (1). The large number of NBA games and high frequency of both free throw shooting and rebounding provide ample data (3)—in fact all the findings we cite in this paper are significant at the _0.005 level or greater_ , far in excess of previous work. To satisfy condition (2), we develop a model of an NBA game that estimates the value of a point scored at each juncture of the game. The value is the impact the point has on the probability a given team will win the game. As any fan knows, a point is more likely to impact the game at the end of close games—our model formalizes this notion using data from over 1.3 million NBA possessions. Condition (4) is satisfied because, while free-throws are taken when play is stopped, at the timing and discretion of the shooter, offensive rebounds occur in the midst of fast-paced game play. A player clearly has less opportunity to contemplate his performance while battling for a rebound as compared to taking a free-throw. 

Using detailed play-by-play data for all NBA games from 2005-2010 (six seasons) we find that in general, home team players shoot free throws _better_ at home. Yet in clutch situations they do significantly _worse_ than road players, who show no difference in performance in clutch versus regular situations. In fact, the players who decline the most in performance are generally worse free throw shooters (but good free-throw shooters are not more likely 

> 2Dohmen (2008) finds that soccer players shooting penalty kicks score less frequently at home, but the result is only marginally significant (p=0.10) and the findings do not demonstrate an impact of the game being close (when the shot should have more pressure). We view these results as roughly supportive of ours, but the relatively small sample leaves the study underpowered. In contrast, all the results we report are significant at the 0.005 level of greater. 

1 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



to do better than they normally do). These pieces of evidence support the notion that a supportive audience can induce pressure-related performance deterioration and suggest it is due to increased self-focus. The latter follows because home fans generally “go crazy" in clutch situations by making noise and wild arm motions for away player free throws, while remaining totally quiet for home player free throws (in fact, the lower performance in regular situations could be explained by this difference in visual distraction). If the pressure impact was due to distraction, we’d expect the road team to do worse in the clutch. Since worse shooters are probably more likely to rely on procedural thinking (“what should I do") than their more naturally gifted counterparts, the greater decline for these players is also supported by the self-focus hypothesis.<sup>3</sup> 

For purposes of comparison, we also consider the impact of high pressure situations on offensive rebounding. We first establish that the home team has a significant advantage in offensive rebounding rate in typical situations, which is consistent with the voluminous evidence from psychology literature that a supportive audience tends to induce more effort (see (Strauss, 2002) for a review).<sup>4</sup> In the clutch, the advantage gets significantly _larger_ . The offensive rebounding rate of the home team increases monotonically with the importance of the point, but the away team’s rate is flat, indicating the result is due to the supportive crowd and not other confounding factors. In contrast to free throws, for which the home team shows a decline in performance, pressure amplifies home-court advantage in the heat of the moment. 

The struggles of even highly experienced experts while performing a concentration-based task in high-pressure moments before a supportive audience lend support to the large laboratory literature on the underlying causes of the negative impact of pressure on concentration-based performance. The finding that, in contrast, performance in an effort-based “heat of the moment” task _improves_ under pressure demonstrates that a supportive audience can be a positive as well, consistent with the notion that pressure can help inspire effort. Taken together, we show how the purported “home choke” phenomenon can live alongside the traditional notion of home-court advantage.<sup>5</sup> 

The paper proceeds as follows. In Section 2 we describe our model of a basketball game, which is necessary to estimate the importance of each of the more than one million possessions in our sample. We present the results Section 3 and conclude in Section 4. 

## 2 Analysis Preliminaries: Modeling a Game of Basketball 

In basketball you win the game by scoring more points than your opponent. Consider two teams, home ( _h_ ) and away ( _a_ ). Let _Sh,N_ and _Sa,N_ denote the current scores for the home and away team with _N_ offensive possessions (for each team) remaining in the game respectively. Let _Ph,i_ and _Pa,i_ denote the number of points scored by the home/away team on the _i_<sup>_th_</sup> possession from the end of the game. The home team wins if they have more points at the end of the game. This is equal to the current score plus the points scored in subsequent possessions, as given by: 



To model how points teams generate points, let _{µh, σh_<sup>2</sup><sup>_}_and</sup><sup>_{µa, σ_</sup> _a_<sup>2</sup><sup>_}_representthemeanandvarianceof</sup> points per possession that each team is able to achieve in the match-up. If the number of remaining possessions, _N_ , is large, the central limit theorem gives the probability of the home team winning as: 

> 3It is also consistent with the hypothesis that part of being a good free throw shooter is the ability to focus to an appropriate degree, so outside influences have less impact on these player. 

> 4One might be concerned that this is due to home players knowing they are less likely to get a foul called, but we do not see a home team bonus in “team” rebounds which result from a referee decision to award the ball after a rebound is knocked out of bounds, or as the result of an ’over the back’ call. 

> 5Part of home court advantage, but not all, can be attributed to referee bias (Maskias, 2011). See http://www.teamrankings.com/blog/nba/nba-home-court-advantage-really-just-the-refs for discussion in the context of basketball. 

2 



MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



where Φ is the CDF of the standard normal distribution. Examining this expression, we see that if the score is tied and the teams are equal in quality, the game is a coin toss. An ability advantage ( _µ_ higher than opponent) matters proportional to the number of remaining possessions, which is intuitive. If you are the better team, the game outcome more likely to reflect this when there are many possessions remaining. Each factor’s marginal impact on winning the game is easily obtained by differentiating equation (3). The following expression gives the impact of a point scored for the home team on win probability: 



Expression (4) shows that points become increasingly impactful on the game outcome when the current score is close ( _|Sh,N − Sa,N |_ small) and few possessions remain. The impact becomes exceedingly small when the score margin is high. To estimate this equation, we first impute the number of remaining possessions using the teamspecific paces in a given match-up and by adding one possession to the team currently holding the ball. Given the standard normal specification, it is natural to estimate equation (3) via Probit. The output gives the probability the home team will win at each point in game. By plugging the estimates into equation 4, we get the value of a point in each of the 1.3 million possessions in our sample. 



Figure 1: Miami’s probability of winning Game 4 of the 2011 Finals, along with score margin. Panel 1 gives the whole game. Panels 2 and 3 zoom in on the first and fourth quarters respectively. Panel 4 shows the final 2 minutes of the game. The blue dots give the impact of D. Wade making free-throw 1 and then missing free-throw 2. 

To understand the model output we’ll use game 4 of the 2011 NBA Finals as an exemplar. Figure 1 presents two key pieces of information: Miami’s lead in the game and their estimated probability of winning. Considering 

3 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



the characteristics of the two teams and the location of the game (Dallas), the game started almost exactly 50/50 (the horizontal line shows 0.50 chance of Miami winning). Panel 1 shows the whole game. Panel 2 zooms in on the first quarter. In the first quarter, though the point differential fluctuates Miami’s winning chances remain relatively unchanged. With many possessions remaining, the relative quality of the two teams is the key driver of win probability. The situation is completely different in the 4th quarter, which shows a tight relationship between winning probability and score margin. This is because points are much more impactful on the eventual outcome late in relatively close games. Panel 4 shows the last two minutes. When the margin remains unchanged, the jagged parts of the win probability curve represent possession changes. The dots show a moment in which Dwanye Wade was awarded a shooting foul (Miami is down 2 with 30 seconds remaining). This represents a very high pressure situation as each point (and possession of the ball) increases the chance of winning by about 0.15. As compared to the moment before he was fouled, he has the ability to double his team’s chance of winning by making both free throws (and then surrendering possession of the ball). As shown in the graph, he made his first free throw, then missed the second—Dallas scored on their next possession dashing Miami’s chances. 





Figure 2: The marginal impact of a point, as a function of score margin and time remaining in the game for the whole game (Panel 1) and only the first three quarters (Panel 2). 

Figure 2 generalizes this exemplar with a 3-D plot showing how the win value of a point (WVP) varies with time remaining on the clock and the point differential for a generic match-up. Panel 1 plots the whole game, whereas Panel 2 shows just the first quarter to provide better contrast (note the change in axes scale). The results are intuitive. The spine is at score margin equal to zero, indicating that, all else equal, points matter most in close games. Moving toward the end of the game raises the value of points in relatively close games and lowers their value 

4 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



when the score margin is large, indicating the game is, as the colloquialism goes, “over.” 

## 3 Results 

The estimates shown in Figure 2 are generated by modeling the win probability of every regular season game between 2005 and 2010 comprising over 1.3 million possession and 300,000 free-throws. The large dataset allows us to accurately gage the marginal impact on the chance of winning for each possession in our sample, yielding a precise measure of each moment’s pressure. In this section, we relate our pressure measure and home/away status to our two metrics of performance: free-throw shooting and offensive rebounding. 

We estimate the probability a free throw will be made using the random coefficients model of Swamy (1970), which flexibly allows parameter values to differ by player. The key explanatory variables of interest are whether the shot was taken at home, the importance of the point (WVP), the point importance interacted with the home dummy (which gives the differential impact of home pressure), and the time remaining in the game. Table 1 is the key to our analysis of free throws. It provides the aggregated coefficients of the model estimates, weighted by the inverse of the variance. The weighted average of the home clutch parameter (Home*WVP) is -0.1371 with an associated t-statistic of _−_ 3 _._ 733 _, p <_ 0 _._ 0002. The likelihood this relationship is due to chance is exceedingly small. The simple average of this parameter is -0.37 and median is -0.22; both of which are significantly different from zero at thresholds well exceeding conventional standards. The weighted estimate indicates the average NBA player is 1-2 percentage points worse in a moderately clutch situation in a home game. The impact of pressure on road shooters is given by the coefficient on WVP. Here we see that the weighted average is a statically insignificant 0.06 ( _p_ = 0 _._ 12). The simple average is also 0.06 and the median is 0.017, weak statistical evidence that road players do a bit better in the clutch. Road players do not appear to respond, or respond very little, to the pressure of the moment, which stands in stark contrast to the behavior of home players. 

Table 1: GLS Random-coefficient model estimates of the impact of pressure on Free-throw success 

|Explanatoryvariable<br>Weighted average Coeffcient|t-ratio|
|---|---|
|WVP<br>0.0624|1.5761|
|Home*WVP<br>-0.1371|-3.733*|
|Home<br>0.0058|3.7693*|
|Players=443, Shots=360452, *p<.001<br>Inverse variance weights used to aggregate coeffci|ents.|



The coefficient on the home dummy gives the estimate of how home players fare in non-clutch situations— the estimate is positive and significant. Home shooters generally shoot 0.5 percentage points better in non-clutch situations, but get worse in the clutch, with performance ending up below that of road shooters. It is difficult to know why home players are slightly more accurate in non-clutch situations. One natural explanation is that road players face higher visual distraction, due to those crazy fans behind the basket. Other plausible hypotheses include the positive role of a supportive audience in low pressure situations and a physical advantage of shooting in one’s home gym.<sup>6</sup> Unfortunately, these hypothesis cannot be differentiated with observational data such as ours. This difficulty highlights the importance of having a continuous pressure metric. Factors such as the “home gym effect” do not vary with the pressure of the moment, allowing for a clean analysis. 

To understand which players are responsive to pressure, Table 2 gives the players that are estimated to be statistically significantly “home choke” or“home clutch” as measured by the coefficient on the interaction term in the above described regression. Note that there are three times more players that register as significant home choke versus home clutch—this is consistent with the evidence from Table 1. The statistical significance of home choking, 

6It could be the case that all basketball goals are slightly different, so shooting on the basket your team practices on could be an advantage. 

5 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



on the player level, far exceeds home clutch. Interestingly we note that Robert Horry, who’s nickname is “Big Shot Bob,” shows up as sufficiently clutch, and the Spurs’ crunch-time hero, Manu Ginobili, is the only player in our sample who is indisputably “clutch" (t=3.45, p=.0003). 

The relationship between home choke and ability is estimated through a GLS regression of our clutch estimate = on player (overall) free-throw percentage. The estimate on free-throw percentage is positive and significant (coeff 1 _._ 54, _t_ = 3 _._ 09 _p <_ 0 _._ 005), demonstrating that better free-throw shooters are less likely to falter, relative to their normal performance, under pressure. 

Table 2: Biggest chokers and clutch players in sample 

|Negative h<br>|ome clutch<br>||Positive<br>|home clutch<br>|<br>|
|---|---|---|---|---|---|
|Player|Estimate|t-ratio|Player|Estimate|t-ratio|
|Jordan Hill<br>|-11.21|-3.04249|Manu Ginobili|2.13|3.45|
|Paul Pierce<br>|-1.54|-2.87|Quinton Ross|8.16|2.34|
|Samuel Dalembert|-2.94|-2.86|Kwame Brown|3.56|2.27|
|Kurt Thomas|-4.21|-2.71|Robert Horry|7.43|2.14|
|Al Harrington|-2.38|-2.66|Greg Monroe|9.18|2.14|
|Gary Payton|-6.65|-2.62|Jared Dudley|2.96|2.00|
|Jason Williams|-4.36|-2.59||||
|Javaris Crittenton|-8.93|-2.47||||
|Joakim Noah|-3.15|-2.44||||
|Michael Finley|-4.00|-2.36||||
|Juwan Howard|-3.21|-2.33||||
|Spencer Hawes|-5.82|-2.26||||
|Derrick Brown|-10.53|-2.19||||
|JaVale McGee|-4.39|-2.10||||
|Dominic McGuire|-8.44|-2.05||||
|Yi Jianlian|-3.03|-1.99||||
|Malik Allen|-7.97|-1.97||||
|Shareef Abdur-Rahim|-4.24|-1.97||||
|Andrew Bynum|-2.86|-1.96||||



We now shift the focus to offensive rebounding. Unlike a free-throw, which is taken when the game is stopped (with the player waiting until ready to shoot), offensive rebounding occurs in the course of fast-paced game play. Since a team averages approximately 1.06 points per possession, an additional offensive rebound is about as a valuable as a point. This makes it a natural comparison to a free-throw, with self-focus as the key varying factor. In Figure 3 we plot the relationship between the value of a point and the offensive rebounding rate for home and away teams. We use the final 8 minutes of the game because the value of a point varies significantly in this period and both teams typically play their starters (back-ups often start the 4th quarter based on many coaches rotational timing). The positive relationship is unmistakable. For games that are truly “over” (WVP equal to approximately zero), how and away teams rebound at the same rate. In the moderate importance range (0.01), the home team does slightly better. As points become more and more valuable, the home team’s edge increases dramatically. A supplementary regression confirms this relationship is statistically significant ( _t_ = 4 _._ 6440 _, p <_ 0 _._ 00001) for the home team, but statistically insignificant (though slightly positive) for the away team ( _t_ = _._ 9115 _, p_ = _._ 3620). 

We have thus shown that in fairly typical situations, the home team does better at both free-throw shooting and offensive rebounding. Yet as the pressure of a moment increases, the home team does worse at free-throws but better at offensive rebounding. The road team shows a relatively flat profile for both, which offers controls for other game factors like fatigue, which should be similar across both teams. The large sample of over 1.3 million possessions and 300,000 free-throws allows us to be confident, through strong statistical significance of 0.005 or greater for all our estimates, that our results are not due to chance, but rather are truly reflect the asymmetric impact of pressure on player performance. 

6 



MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



Figure 3: A kernel estimator of offensive rebounding rates for the home and away team, as a function of point importance. Bandwidth is chosen to include 8% of the available data on either side (if possible). 

## 4 Discussion and Conclusion 

In this paper we address a question that is of interest to psychologists and sports fans alike: how does performance change under pressure? Psychologists have argued that pressure can both distract and lead to more self-focus. Selffocus is thinking about the details of how one should accomplish a goal, as opposed to “just doing it.” Psychology studies have implicated self-focus in reducing performance for motor and cognitive skill tasks. Other studies show that a supportive audience generally make people try harder. Before now, it was unclear if these results extended to highly trained experts or are limited to situations in which one has little experience, such as a laboratory study. 

In this paper we deepen the understanding of pressure by studying two fundamentally different acts within the context of the same game. Free-throw shooting is a task that requires quiet concentration while offensive rebounding is an effort-based task done in the heat of the moment. The frequency of these actions combined with our large dataset enables firm statistical conclusions—all results are significant at the 0.005 level or greater. We use variation in a home vs. away audience to understand how pressure moderates performance. When taking a free-throw on the road, distraction is high while at home the 20,000 or so supportive souls are waiting in a nervous, quiet arena. It turns out that the latter environment is more difficult—choking occurs for the home team, which we argue is due to increased self-focus, hampering the natural ability of a player to make a free-throw. This is consistent with the psychological notion that letting down a supportive audience is stressful. We show that a home crowd can also improve performance as home teams gather offensive rebound better in the clutch, consistent with past findings that a supportive audience increases effort. Taken together, the results highlight the asymmetric impact of a supportive audience in performance under pressure. 

## References 

- Baumeister, R. (1984). Choking under pressure: Self-consciousness and paradoxical effects of incentives on skillful performance. _Journal of Personality and Social Psychology_ , 46(3):610. 

- Baumeister, R. and Showers, C. (1986). A review of paradoxical performance effects: Choking under pressure in sports and mental tests. _European Journal of Social Psychology_ , 16(4):361–383. 

7 

MIT Sloan Sports Analytics Conference 2012 March 1–2, 2012, Boston, MA, USA 



- Beilock, S., Carr, T., MacMahon, C., and Starkes, J. (2002). When paying attention becomes counterproductive: Impact of divided versus skill-focused attention on novice and experienced performance of sensorimotor skills. _Journal of Experimental Psychology: Applied_ , 8(1):6. 

- Dohmen, T. (2008). Do professionals choke under pressure? _Journal of Economic Behavior and Organization_ , 65(3):636–653. 

- Gucciardi, D. and Dimmock, J. (2008). Choking under pressure in sensorimotor skills: Conscious processing or depleted attentional resources? _Psychology of Sport and Exercise_ , 9(1):45–59. 

- Lewis, B. and Linder, D. (1997). Thinking about choking? attentional processes and paradoxical performance. _Personality and Social Psychology Bulletin_ , 23(9):937–944. 

- Maskias, T. (2011). Referee bias and the home-court advantage in professional sports. In _Proceedings of the MIT Sloan Sports Analytics Conference_ , pages 1–10. 

- Schlenker, B., Philips, S., Boniecki, K., and Schlenker, D. (1995). Championship pressures: Choking or triumphing in one’s own territory? _Journal of Personality and Social Psychology_ , 68:621–643. 

- Strauss, B. (2002). Social facilitation in motor tasks: A review of research and theory. _Psychology and Sport Science_ , 3:237–256. 

- Swamy, P. (1970). Efficient inference in a random coefficient regression model. _Econometrica: Journal of the Econometric Society_ , pages 311–323. 

- Wallace, H., Baumeister, R., and Vohs, K. (2005). Audience support and choking under pressure: A home disadvantage? _Journal of Sports Sciences_ , 23(4):429–438. 

- Wilson, M., Chattington, M., Marple-Horvat, D., and Smith, N. (2007). A comparison of self-focus versus attentional explanations of choking. _Journal of Sport and Exercise Psychology_ , 29(4):439. 

- Wright, E. F. and W., J. (1991). The home-course disadvantage in golf championships: Further evidence for the undermining effect of supportive audience on performance under pressure. _Journal of Sport Behavior_ , 14(3):51– 60. 

8 


