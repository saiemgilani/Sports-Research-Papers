<!-- source: library/conferences/New England Symposium on Statistics in Sports/2013/2013 - Crossing in Soccer has a Strong Negative Impact on Scoring Evidence from the English Premier League and the German Bundesliga - Unknown Authors.pdf -->



Jan Vecer, Frankfurt School of Finance and Management 

Motivation 



<!-- Start of picture text -->
Crossing in soccer has a strong negative<br>impact on scoring:<br>Evidence from the English Premier League and the German<br>Bundesliga<br><!-- End of picture text -->

The Statistical Model Graphs Conclusions 

Jan Vecer, Frankfurt School of Finance and Management 

NESSIS 2013, Harvard University 

September 21, 2013 



<!-- Start of picture text -->
Abstract<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Graphs 

Conclusions 

Crossing in soccer plays a significant role in scoring, about 15% of all goals scored in the recent seasons of the English Premier League are the result of open play crosses. However, crossing from an open play is hugely inefficient, only 1 open cross out of 91.92 leads to a goal on average. When we estimate the impact of open crossing on scoring of the individual teams using multilevel Poisson regression, we conclude that the net effect of crossing is typically negative or neutral at best. An average team can score up to additional 0.656(?) goals per game if it reduced open crossing. The quality of the team is the major explanatory factor on the number of such missed scoring opportunities, stronger teams miss more goal opportunities in general when crossing than weaker teams. 



<!-- Start of picture text -->
Abstract<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model Graphs Conclusions 

Stronger teams have more options how to score and open play crossing seems as one of the suboptimal ways of a goal creation. Teams such as Arsenal, Chelsea, Liverpool, Manchester City or Tottenham have a potential of scoring an extra goal per match if they reduced open crossing. A reversed picture is seen in the defense analysis, more goal opportunities are missed in general when crossing against weak teams than crossing against strong teams. Interestingly, the actual conversion of open crosses to goals plays only a minor role for explaining the impact of open crossing on goals. 



<!-- Start of picture text -->
Original Motivation<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

The original question leading to this research was if there is any way to get a better prediction of the outcome of the soccer game from statistics obtained during the game. There is a large and liquid in-play betting market on soccer that trades various events: 

Win, 



Draw, 





Loss, 

The Statistical Model Graphs Conclusions 

a team in a given game plus additional contracts such as the 

Total Number of Goals (including more than N + 0.5 goals), Exact Score, 







Team to Score Next + No Goal. 

There is an extensive paid database of the betting quotes from Betfair. 



<!-- Start of picture text -->
How to Compute these Odds?<br><!-- End of picture text -->

A reasonable approximation of the dynamics of the soccer score is a Poisson process for the goal distribution. The goals scored in the remainder of the game should follow 

Jan Vecer, Frankfurt School of Finance and Management 





for the home team and 

The Statistical Model Graphs 





Conclusions 

Here, the λt and µt play the role of scoring intensities for the two teams, the expected number of goals to be scored in the remainder of the match. Furthermore, if we assume independence of the goals scored, it is relatively straightforward to obtain all the betting quotes from the Poisson model, where parameters λt and µt serve as inputs. 



<!-- Start of picture text -->
Known Limitations of Poisson Model<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 



The scores are not independent. The correlation of the score in the English Premier League since 2006 is −0.057. Moreover, the realized fraction of draws is higher than implied from an independent Poisson model. 

The Statistical Model Graphs 

Conclusions 



There is some memory in goals, but this effect is reasonably small. One can fully estimate this effect from betting contracts on the Next Goal (which team scores next). The Poisson model implies that the quote on the Next Goal should stay the same before and after each goal. 



<!-- Start of picture text -->
Implied Intensities<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management Motivation The Statistical Model Graphs Conclusions 



<!-- Start of picture text -->
1.5<br>1.0<br>0.5<br>0.0<br>0 20 40 60 80 100<br><!-- End of picture text -->

Figure: Arsenal-Chelsea 0:0, April 21, 2012 

The Statistical Model Graphs Conclusions 



<!-- Start of picture text -->
Inference of the Intensities from the Athletic<br>Performance<br><!-- End of picture text -->

Do the scoring intensities depend on some athletic performance data? Source of data: 

Jan Vecer, Frankfurt School of Finance and Management 









OPTA (since 2008, 1900+ games) www.espnfc.com (match reports since 2008) www.premierleague.com (since 2006, 2700+ games) www.bundesliga.de (since 2009, 1250+ games, tracking since 2011) 

What are the significant variables? 







Top Speed (Bundesliga) Discipline + Stoppages Open Crosses(!) 



<!-- Start of picture text -->
Some Facts about Crossing<br><!-- End of picture text -->

A cross is an airborn delivery of a ball from the side of the field across to the front of the goal. 

Jan Vecer, Frankfurt School of Finance and Management 





An average EPL team makes 18.2 open crosses per game and scores 1.33 goals per game, an average Bundesliga team makes 11 open crosses per game and scores 1.45 goals per game. 

In the EPL, 18.2 open crosses produce 3.7 good crosses and 14.5 bad crosses, meaning that the vast majority of open crosses results in a loss of the possession in a favorable position. 

The Statistical Model Graphs 

Conclusions 





A goal is scored per 92 open crosses. 

The quality of crossing is highly variable among the teams, Manchester United needs 43.8 crosses to score a goal, Southampton needs 143.2 crosses to score a goal. 



Stong observational bias on TV highlights that show mostly good crosses and crosses leading to goals. 



- There is an ongoing discussion about effectiveness of open crossing among football bloggers, but the analysis has been limited only to descriptive statistics. 



<!-- Start of picture text -->
Football Pitch<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

The Statistical Model Graphs 

Conclusions 





<!-- Start of picture text -->
Conversion Statistics - Attack<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

The Statistical Model Graphs Conclusions 

|Manchester Utd|
|---|
|<br>Chelsea|
|Norwich City|
|<br>Burnley|
|Manchester City|
|<br>Arsenal|
|Aston Villa|
|Blackpool|
|Liverpool|
|Everton|
|<br>Reading|
|Swansea City|
|Sunderland|
|<br>Tottenham|
|Newcastle Utd|
|QP Rnr<br>|
|<br>Bolton<br>ages|
|es romwc|
|Fulham<br>|
|Hull City|
|Wolverhampton|
|<br>West Ham<br>|
|Stoke City|
|ouamon|
|<br>Blackburn<br>|
|Wigan Athletic|
|<br>Portsmouth|
|Birmingham City|
|Middlesbrough|
|0.01<br>0.02<br>0.03<br>0.04|
|Conversion|



Figure: The fraction of open crosses (blue), final third entries (red) and outside the box shots (green) that results in a goal for individual attacking teams. 



<!-- Start of picture text -->
Conversion Statistics - Defense<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

The Statistical Model Graphs 

Conclusions 

|Manchester City<br>Fulham||
|---|---|
|<br>Portsmouth||
|<br>Birmingham City||
|<br>Aston Villa||
|<br>Swansea City||
|<br>Chelsea<br>Stoke City||
|West Bromwich||
|Sunderland||
|Hll i<br>Burnley||
|<br>u Cty||
|Manchester Utd||
|Blackpool||
|Middlbrh<br>Arsenal||
|esoug||
|Everton||
|<br>Blackburn||
|QP Rangers||
|Norwich City<br>||
|Liverpool||
|<br>Bolton<br>||
|West Ham||
|Wolverhampton||
|Th<br>Newcastle Utd<br>||
|<br>ottenam||
|Wigan Athletic||
|Reading||
|Southampton||
|0.01|0.02<br>0.03<br>0.04<br>0.05|
||Conversion|



Figure: The fraction of open crosses (blue), final third entries (red) and outside the box shots (green) that results in a goal for individual defending teams. 



<!-- Start of picture text -->
Concerns<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

The Statistical Model Graphs Conclusions 

Estimation of the impact of crossing on goals should addresses the following issues: 

Crosses may lead to goals indirectly in a follow up play. By crossing the team is giving up an alternative way of playing. Analysis of Goals regressed on Open Crosses addresses that. 



<!-- Start of picture text -->
The Statistical Model<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Multilevel cross sectional Poisson regression: the teams are grouped according to the attack (using variable j[i]) and the defense (using variable k[i]): 



Graphs 

Conclusions 

uj ∼ N(0, Σu) vk ∼ N(0, Σv ) 



<!-- Start of picture text -->
EPL Model<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Graphs Conclusions 

||Model 1|
|---|---|
|(Intercept)|0.473376<br>(0.100849)|
|OpenCross|-0.022861<br>(0.003196)|
|Home|0.417204<br>(0.029636)|
|AIC|4229|
|BIC|4286|
|Log Likelihood|-2106|
|Deviance|4211|
|Num. obs.|3800|
|Num. groups: Team|29|
|Num. groups: Against|29|
|Variance: Team.(Intercept)|0.121923|
|Variance: Team.OpenCross|0.000110|
|Variance: Against.(Intercept)|0.112291|
|Variance: Against.OpenCross|0.000028|











<!-- Start of picture text -->
EPL Model - Attack<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Graphs 

Conclusions 

||(Intercept)|OpenCross|Home|
|---|---|---|---|
|Arsenal|1.042368|-0.030510|0.417203|
|Aston Villa|0.425882|-0.019876|0.417203|
|Chelsea|1.097310|-0.031954|0.417203|
|Everton|0.671642|-0.024262|0.417203|
|Fulham|0.273865|-0.017672|0.417203|
|Liverpool|0.860616|-0.029654|0.417203|
|Manchester City|0.846105|-0.029128|0.417203|
|Manchester Utd|0.798300|-0.011707|0.417203|
|Newcastle Utd|0.565930|-0.024579|0.417203|
|Norwich City|0.377409|-0.017618|0.417203|
|Southampton|0.593570|-0.025884|0.417203|
|Stoke City|0.011150|-0.011515|0.417203|
|Sunderland|0.472198|-0.026832|0.417203|
|Swansea City|0.387274|-0.022690|0.417203|
|Tottenham|1.024221|-0.040664|0.417203|
|West Bromwich|0.539959|-0.027303|0.417203|
|West Ham|0.241390|-0.015480|0.417203|









<!-- Start of picture text -->
EPL Model - Defense<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Graphs 

Conclusions 

||(Intercept)|OpenCross|Home|
|---|---|---|---|
|Arsenal|0.048665|-0.016203|0.417203|
|Aston Villa|0.446672|-0.022443|0.417203|
|Chelsea|-0.093416|-0.013975|0.417203|
|Everton|0.146778|-0.017741|0.417203|
|Fulham|0.331304|-0.020634|0.417203|
|Liverpool|-0.062757|-0.014456|0.417203|
|Manchester City|0.003006|-0.015487|0.417203|
|Manchester Utd|-0.152201|-0.013053|0.417203|
|Newcastle Utd|0.569296|-0.024365|0.417203|
|Norwich City|0.646480|-0.025575|0.417203|
|Southampton|0.541325|-0.023927|0.417203|
|Stoke City|0.358285|-0.021057|0.417203|
|Sunderland|0.439709|-0.022333|0.417203|
|Swansea City|0.340518|-0.020778|0.417203|
|Tottenham|0.149979|-0.017791|0.417203|
|West Bromwich|0.670652|-0.025954|0.417203|
|West Ham|0.612075|-0.025036|0.417203|









<!-- Start of picture text -->
Bundesliga Model<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management Motivation 

Graphs Conclusions 

||Model 1|
|---|---|
|(Intercept)|0.374347<br>(0.088441)|
|OpenCross|-0.020001<br>(0.004450)|
|Home|0.281266<br>(0.034298)|
|AIC|3009|
|BIC|3061|
|Log Likelihood|-1495|
|Deviance|2991|
|Num. obs.|2536|
|Num. groups: Team|24|
|Num. groups: Against|24|
|Variance: Team.(Intercept)|0.064105|
|Variance: Team.OpenCross|0.000080|
|Variance: Against.(Intercept)|0.070237|
|Variance: Against.OpenCross|0.000070|











<!-- Start of picture text -->
Bundesliga Model - Attack<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Graphs 

Conclusions 

||(Intercept)|OpenCross|Home|
|---|---|---|---|
|1899 Hofenheim|0.343475|-0.015867|0.281266|
|1.FC Nurnberg|0.278478|-0.024494|0.281266|
|1.FSV Mainz 05|0.384550|-0.026493|0.281266|
|Bayer 04 Leverkusen|0.662520|-0.021821|0.281266|
|Borussia Dortmund|0.860156|-0.027790|0.281266|
|Borussia Mgladbach|0.390397|-0.021744|0.281266|
|Eintracht Frankfurt|0.326103|-0.019196|0.281266|
|FC Bayern Munchen|0.903426|-0.015981|0.281266|
|FC Schalke 04|0.506178|-0.012962|0.281266|
|Hamburger SV|0.419429|-0.021852|0.281266|
|Hannover 96|0.483677|-0.024369|0.281266|
|SC Freiburg|0.332071|-0.020679|0.281266|
|SV Werder Bremen|0.462857|-0.011292|0.281266|
|VfB Stuttgart|0.624621|-0.027100|0.281266|
|VfL Wolfsburg|0.511445|-0.017644|0.281266|









<!-- Start of picture text -->
Bundesliga Model - Defense<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

Graphs 

Conclusions 

||(Intercept)|OpenCross|Home|
|---|---|---|---|
|1899 Hofenheim|0.397648|-0.020738|0.281266|
|1.FC Nurnberg|0.326835|-0.018498|0.281266|
|1.FSV Mainz 05|0.260753|-0.016407|0.281266|
|Bayer 04 Leverkusen|0.162643|-0.013303|0.281266|
|Borussia Dortmund|-0.158434|-0.003145|0.281266|
|Borussia Mgladbach|0.426736|-0.021658|0.281266|
|Eintracht Frankfurt|0.356889|-0.019448|0.281266|
|FC Bayern Munchen|-0.327126|0.002192|0.281266|
|FC Schalke 04|0.134238|-0.012404|0.281266|
|Hamburger SV|0.384058|-0.020308|0.281266|
|Hannover 96|0.482066|-0.023409|0.281266|
|SC Freiburg|0.398418|-0.020762|0.281266|
|SV Werder Bremen|0.517723|-0.024537|0.281266|
|VfB Stuttgart|0.403881|-0.020935|0.281266|
|VfL Wolfsburg|0.479178|-0.023317|0.281266|









<!-- Start of picture text -->
Things to Notice<br><!-- End of picture text -->



The impact of crossing on goals is negative for most of the teams, it is neutral at best. 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 



Stronger attacking teams tend to have a more negative impact on scoring than weaker teams with a single exception of Manchester United. This is due to the fact that aerial delivery of the ball has less precision and thus more luck than skill is involved. Stronger teams benefit more from situations that depend on skill in contrast to situations that depend on luck. 

Graphs 

Conclusions 



The negative impact on scoring is more visible for weaker defending teams. It may be neutral against strong teams (FC Bayern Munchen). 



Long balls and corners played inside the box (set play cross) have similar negative impact pattern on scoring (but with lower statistical significance), suggesting that alternative play that keeps the possession of the ball can be more optimal. 



<!-- Start of picture text -->
Tottenham Attack<br><!-- End of picture text -->

# **Tottenham** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Arsenal Attack<br><!-- End of picture text -->

# **Arsenal** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Manchester United Attack<br><!-- End of picture text -->

# **Manchester Utd** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Chelsea Attack<br><!-- End of picture text -->

# **Chelsea** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Liverpool Attack<br><!-- End of picture text -->

# **Liverpool** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Manchester City Attack<br><!-- End of picture text -->

# **Manchester City** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Stoke City Attack<br><!-- End of picture text -->

# **Stoke City** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
FC Bayern Munich Attack<br><!-- End of picture text -->

# **FC Bayern Munchen** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Borussia Dortmund Attack<br><!-- End of picture text -->

# **Borussia Dortmund** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Werder Bremen Attack<br><!-- End of picture text -->

# **SV Werder Bremen** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Manchester United Defense<br><!-- End of picture text -->

# **Manchester Utd** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Tottenham Defense<br><!-- End of picture text -->

# **Tottenham** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Arsenal Defense<br><!-- End of picture text -->

# **Arsenal** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Chelsea Defense<br><!-- End of picture text -->

# **Chelsea** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Liverpool Defense<br><!-- End of picture text -->

# **Liverpool** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Manchester City Defense<br><!-- End of picture text -->

# **Manchester City** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
West Bromwich Defense<br><!-- End of picture text -->

# **West Bromwich** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
FC Bayern Munich Defense<br><!-- End of picture text -->

# **FC Bayern Munchen** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Borussia Dortmund Defense<br><!-- End of picture text -->

# **Borussia Dortmund** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Werder Bremen Defense<br><!-- End of picture text -->

# **SV Werder Bremen** 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation 

The Statistical Model 

Conclusions 



<!-- Start of picture text -->
0 10 20 30 40 50<br>Open Cross<br>8<br>6<br>4<br>Goals<br>2<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
Conclusions<br><!-- End of picture text -->

Is open crossing dead? 

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model Graphs 

No, but it should be either used by weaker teams playing against stronger teams when the luck plays a more important role, or the stronger teams must improve the crossing quality to the point of Manchester United (43.8 open crosses per goal) to make it neutral. This would need a big improvement, the second best crossing team, Chelsea, needs 62.6 open crosses per goal. 

At the present time, the teams seem to overuse open crossing. Its reduction can increase scoring for most of the teams. Some top teams can score 40+ extra goals in seasons by reducing crossing. That’s about how many goals scores Messi in his top season. 

Motivation The Statistical Model Graphs 



<!-- Start of picture text -->
Conclusions<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

So what if we see indeed the decrease of open crossing and increase of scoring? 

Do not forget to send me a check for such goals or for winning the championship, I am OK with half of Messi’s salary. 

I do not need the Golden Shoe for the best scorer. 



<!-- Start of picture text -->
Conclusions<br><!-- End of picture text -->

Jan Vecer, Frankfurt School of Finance and Management 

Motivation The Statistical Model Graphs 

I will post a new version of the paper on www.ssrn.com in the near future. An old version that uses a standard linear regression is available, but the conclusions are pretty much the same. 


