<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - Using data analysis to predict attendance for NHL regular season games - Unknown Authors.pdf -->

# Using Data Analysis to Predict Attendance for NHL Regular Season Games 

Brian Macdonald<sup>1</sup> Michael Peterson<sup>2</sup> James Cifu<sup>1</sup> 

- 1Florida Panthers Hockey Club, Sunrise, FL 

- 2Tampa Bay Lightning Hockey Club, Tampa, FL 



NESSIS, 09/23/2017 Twitter: @bmacNHL, @FlaPanthers, @TBLightning, #NESSIS 

# Attendance Model 



Goal: 

- Develop a model for predicting attendance for games using only information that is known before tickets go on sale. 

# Attendance Model 



Goal: 

- Develop a model for predicting attendance for games using only information that is known before tickets go on sale. 

This could help answer questions like: 

- Which games should be in which tiers for variable pricing? 

# Attendance Model 



Goal: 

   - Develop a model for predicting attendance for games using only information that is known before tickets go on sale. 

- This could help answer questions like: 

   - Which games should be in which tiers for variable pricing? 

   - What kinds of things could we request when the league is developing the schedule? 

# Attendance Model 



Goal: 

- Develop a model for predicting attendance for games using only information that is known before tickets go on sale. 

This could help answer questions like: 

- Which games should be in which tiers for variable pricing? 

- What kinds of things could we request when the league is developing the schedule? 

   - **Specific question** : Do we prefer good team on a Saturday and bad team during the week, or a good team during the week and a bad team on Saturday?" 

# Attendance Model 



Goal: 

- Develop a model for predicting attendance for games using only information that is known before tickets go on sale. 

This could help answer questions like: 

- Which games should be in which tiers for variable pricing? 

- What kinds of things could we request when the league is developing the schedule? 

   - **Specific question** : Do we prefer good team on a Saturday and bad team during the week, or a good team during the week and a bad team on Saturday?" 

   - What do we want Thanksgiving week? 



First, let’s plot some raw data. Attendance* by game, from 2007-08 to 2016-17, for all 30 teams. 



First, let’s plot some raw data. Attendance* by game, from 2007-08 to 2016-17, for all 30 teams. 

*Announced attendance, as published on nhl.com 

Snippet 



# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

Model 

1. 

2. That leaves us with ANA, CAR, CBJ, COL, DAL, FLA, NJ, NSH, NYI, OTT, PHX, STL, and TB. 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

Model 

1. 

2. That leaves us with ANA, CAR, CBJ, COL, DAL, FLA, NJ, NSH, NYI, OTT, PHX, STL, and TB. 

3. Remove a few games unusual characteristics. 

   - European games 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

## Model 

1. 

2. That leaves us with ANA, CAR, CBJ, COL, DAL, FLA, NJ, NSH, NYI, OTT, PHX, STL, and TB. 

3. Remove a few games unusual characteristics. 

   - European games 

   - Blizzards 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

## Model 

1. 

2. That leaves us with ANA, CAR, CBJ, COL, DAL, FLA, NJ, NSH, NYI, OTT, PHX, STL, and TB. 

3. Remove a few games unusual characteristics. 

   - European games 

   - Blizzards 

4. Use several predictor variables (next slide) 

# Attendance Data and Model 



Two observations 

1. For many teams, attendance is relatively flat. 

2. Winning matters. See BOS, CHI, LA, NSH, TB, WSH. 

## Model 

1. 

2. That leaves us with ANA, CAR, CBJ, COL, DAL, FLA, NJ, NSH, NYI, OTT, PHX, STL, and TB. 

3. Remove a few games unusual characteristics. 

   - European games 

   - Blizzards 

4. Use several predictor variables (next slide) 

5. Announced attendance is outcome we’re trying to predict 

# Predictors 



> ▶ home team, away team 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

- points during previous year for home/away (lag) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

- points during previous year for home/away (lag) 

- year-to-date points relative to average for home/away. 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

- points during previous year for home/away (lag) 

- year-to-date points relative to average for home/away. 

- day and month interaction (Sundays different in fall?) 

# Predictors 



> ▶ home team, away team 

> ▶ day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

- points during previous year for home/away (lag) 

> ▶ year-to-date points relative to average for home/away. 

- day and month interaction (Sundays different in fall?) 

- home team and day interaction 

# Predictors 



> ▶ home team, away team 

- day of week, month 

- holiday (Columbus Day, Thanksgiving week, etc., or none.) 

- season opener (Y or N) 

- same division (Y or N) 

- same conference (Y or N) 

- points during previous year for home/away (lag) 

- year-to-date points relative to average for home/away. 

- day and month interaction (Sundays different in fall?) 

- home team and day interaction 

- home team and month interaction 

   - (snowbird months good for us?) 



# Interpretation of regression model results 

> ▶ Impact that each of these variables have on attendance, 



# Interpretation of regression model results 

- Impact that each of these variables have on attendance, **independent of all other variables** . 



# Interpretation of regression model results 

- Impact that each of these variables have on attendance, **independent of all other variables** . 

- For example, we find the effect of day, controlling for all of the other variables in our model 



# Interpretation of regression model results 

- Impact that each of these variables have on attendance, **independent of all other variables** . 

- For example, we find the effect of day, controlling for all of the other variables in our model 

- That’s an important point. Example: If teams schedule big opponents on the weekend, then the effect of a weekend game could be overstated if we just look at day and ignore opponent. 

# Example: day of week 



<!-- Start of picture text -->
Effect of Day Of Week on Attendance<br>Mon −690<br>Tue −565<br>Wed −582<br>Thu −245<br>Fri 786<br>Sat 1056<br>Sun 240<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Day Of Week<br><!-- End of picture text -->



# Example: day of week 



<!-- Start of picture text -->
Effect of Day Of Week on Attendance<br>Mon −690<br>Tue −565<br>Wed −582<br>Thu −245<br>Fri 786<br>Sat 1056<br>Sun 240<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Day Of Week<br><!-- End of picture text -->



1. Attendance on Saturday is expected to be 1,056 higher than average, “holding all other variables constant." 

# Example: day of week 



<!-- Start of picture text -->
Effect of Day Of Week on Attendance<br>Mon −690<br>Tue −565<br>Wed −582<br>Thu −245<br>Fri 786<br>Sat 1056<br>Sun 240<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Day Of Week<br><!-- End of picture text -->



1. Attendance on Saturday is expected to be 1,056 higher than average, “holding all other variables constant." 

2. The difference between Saturday and Monday is expected to be 1,746 (1,056 + 690). 

# Example: day of week 



<!-- Start of picture text -->
Effect of Day Of Week on Attendance<br>Mon −690<br>Tue −565<br>Wed −582<br>Thu −245<br>Fri 786<br>Sat 1056<br>Sun 240<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Day Of Week<br><!-- End of picture text -->



1. Attendance on Saturday is expected to be 1,056 higher than average, “holding all other variables constant." 

2. The difference between Saturday and Monday is expected to be 1,746 (1,056 + 690). 

3. Not surprising. Stuff we knew. But now we’ve quantified. 

# Month 





<!-- Start of picture text -->
Effect of Month on Attendance<br>Oct −957<br>Nov −803<br>Dec −553<br>Jan 54<br>Feb 350<br>Mar 852<br>Apr 1057<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Month<br><!-- End of picture text -->

# Month 





<!-- Start of picture text -->
Effect of Month on Attendance<br>Oct −957<br>Nov −803<br>Dec −553<br>Jan 54<br>Feb 350<br>Mar 852<br>Apr 1057<br>−1000 −500 0 500 1000<br>Announced Attendance<br>Month<br><!-- End of picture text -->

> ▶ Attendance increases over the course of the season 

# Away Team 



<!-- Start of picture text -->
Effect of Away on Attendance<br>DET 1270<br>NYR 1162<br>PIT 1154<br>BOS 821<br>CHI 618<br>MTL 583<br>TOR 360<br>PHI 307<br>WSH 273<br>N.J 88<br>VAN 54<br>S.J −46<br>L.A −52<br>BUF −52<br>T.B −69<br>FLA −107<br>COL −112<br>WPG −121<br>NYI −138<br>EDM −162<br>ANA −171<br>CGY −340<br>ATL −376<br>DAL −527<br>MIN −564<br>CBJ −592<br>CAR −614<br>PHX −623<br>NSH −660<br>OTT −669<br>STL −696<br>−1000 0 1000<br>Announced Attendance<br>Away<br><!-- End of picture text -->



# Holidays 





<!-- Start of picture text -->
Effect of Holiday on Attendance<br>Columbus Day −146<br>Dec 22 491<br>Dec 23 1049<br>Dec 26 1214<br>Dec 27 2092<br>Dec 28 2232<br>Dec 29 2918<br>Dec 30 2110<br>Dec 31 2111<br>Easter −800<br>Election Day 681<br>Good Friday 150<br>Halloween −1602<br>MLK Day 905<br>none 0<br>Presidents Day 1748<br>Season Opener 2570<br>Thanksgiving Mon 580<br>Thanksgiving Tue 1237<br>Thanksgiving Wed 1361<br>Thanksgiving Fri 1006<br>Thanksgiving Sat 630<br>Thanksgiving Sun 177<br>Valentine's Day 564<br>Veterans Day 846<br>−2000 0 2000<br>Announced Attendance<br>Holiday<br><!-- End of picture text -->

# Day-month combinations 



<!-- Start of picture text -->
Effect of Day Month on Attendance<br>Mon.Oct 53<br>Mon.Nov −209<br>Mon.Dec 278<br>Mon.Jan −38<br>Mon.Feb −219<br>Mon.Mar 109<br>Mon.Apr −39<br>Tue.Oct 9<br>Tue.Nov 3<br>Tue.Dec 220<br>Tue.Jan −135<br>Tue.Feb −282<br>Tue.Mar 43<br>Tue.Apr 90<br>Wed.Oct 288<br>Wed.Nov −158<br>Wed.Dec 54<br>Wed.Jan −232<br>Wed.Feb 12<br>Wed.Mar 31<br>Wed.Apr −49<br>Thu.Oct −131<br>Thu.Nov 182<br>Thu.Dec −77<br>Thu.Jan 51<br>Thu.Feb 2<br>Thu.Mar −12<br>Thu.Apr −39<br>Fri.Oct −22<br>Fri.Nov 23<br>Fri.Dec −94<br>Fri.Jan 84<br>Fri.Feb 150<br>Fri.Mar −147<br>Fri.Apr 80<br>Sat.Oct −196<br>Sat.Nov 170<br>Sat.Dec −301<br>Sat.Jan 195<br>Sat.Feb 262<br>Sat.Mar −1<br>Sat.Apr −30<br>Sun.Oct −70<br>Sun.Nov −69<br>Sun.Dec −120<br>Sun.Jan 79<br>Sun.Feb 99<br>Sun.Mar 39<br>Sun.Apr 64<br>−200 0 200<br>Announced Attendance<br>Day Month<br><!-- End of picture text -->





# Opponent-day combinations, Other Notes 

Opponent-day: 

- Good team on Sat and bad team on Tue, or good team on Tue and bad team on Sat 



# Opponent-day combinations, Other Notes 

Opponent-day: 

- Good team on Sat and bad team on Tue, or good team on Tue and bad team on Sat 

- No evidence that there is a difference between these two, in terms of attendance. 



# Opponent-day combinations, Other Notes 

Opponent-day: 

- Good team on Sat and bad team on Tue, or good team on Tue and bad team on Sat 

- No evidence that there is a difference between these two, in terms of attendance. 

- Revenue, however, is another story. 



# Opponent-day combinations, Other Notes 

Opponent-day: 

- Good team on Sat and bad team on Tue, or good team on Tue and bad team on Sat 

- No evidence that there is a difference between these two, in terms of attendance. 

- Revenue, however, is another story. 

Record: 

- Record matters for both home team and away team. 



# Opponent-day combinations, Other Notes 

Opponent-day: 

- Good team on Sat and bad team on Tue, or good team on Tue and bad team on Sat 

- No evidence that there is a difference between these two, in terms of attendance. 

- Revenue, however, is another story. 

Record: 

- Record matters for both home team and away team. 

- Last year’s record matters too. 



Using prediction model to tier games 



# Using prediction model to tier games 





Actual vs Budget for 16-17 



Actual vs Budget for 16−17 



<!-- Start of picture text -->
12.5<br>10.0<br>7.5<br>5.0<br>5.0 7.5 10.0 12.5<br>Budget<br>Actual<br><!-- End of picture text -->

# Internal data 



1. Model using public data (2007-08 to 2016-17) 

2. Model using internal data (only 2014-15 to 2016-17, but can use ticket prices and revenue) 

3. Average 

# Predictions for 17-18 







# Total tickets and tickets 60 days out 





# Total tickets and tickets 60 days out 





# Total tickets vs tickets 60 days out 





<!-- Start of picture text -->
Total tickets vs tickets 60 days out<br><!-- End of picture text -->

# Total tickets vs tickets 60 days out 



# Similar relationship for _n_ days out 



# Similar relationship for _n_ days out 







# Joining two models 



Use both models. Ticket sales model gets better as game approaches 

# Joining two models 



Use both models. Ticket sales model gets better as game approaches 





Fin. 

@bmacNHL 

Lead scores 





# Lead scores 



<!-- Start of picture text -->
Canada 82% (n=11)<br>Northeast States 88% (n=26)<br>Other FL counties 82% (n=27)<br>Miami−Dade 90% (n=136<br>Palm Beach 89% (n=226<br>Broward 88% (n=768<br>0 25 50 75 100 125<br>Renewal Rate<br>Region<br><!-- End of picture text -->



# Show rate 



<!-- Start of picture text -->
1 95% (n=210<br>0.9 92% (n=345)<br>0.8 90% (n=224)<br>0.7 87% (n=135)<br>0.6 88% (n=112)<br>0.5 85% (n=68)<br>0.4 70% (n=46)<br>0.3 71% (n=24)<br>0.2 78% (n=18)<br>0.1 43% (n=14)<br>0 17% (n=12)<br>0 25 50 75 100 125<br>Show Rate<br><!-- End of picture text -->



# Win% in games attended 



<!-- Start of picture text -->
0.6 73% (n=11)<br>0.5 93% (n=592)<br>0.4 89% (n=341)<br>0.3 84% (n=144)<br>0.2 70% (n=66)<br>0.1 70% (n=30)<br>0 33% (n=24)<br>0 25 50 75 100 125<br>Renewal Rate<br>Wins Att P<br><!-- End of picture text -->

# Average total goals in games attended 





<!-- Start of picture text -->
5.6 93% (n=117)<br>5.2 91% (n=242)<br>4.8 94% (n=302)<br>4.4 94% (n=125)<br>4 84% (n=147)<br>3.6 94% (n=53)<br>3.2 78% (n=72)<br>2.8 84% (n=31)<br>2.4 76% (n=45)<br>2 59% (n=17)<br>1.6 71% (n=14)<br>0.8 58% (n=12)<br>0 25 50 75 100 125<br>Renewal Rate<br>Tot Goals Att P<br><!-- End of picture text -->



# Proportion of 1-goal games in games attended 



<!-- Start of picture text -->
0.6 94% (n=372)<br>0.55 92% (n=258)<br>0.5 90% (n=179)<br>0.45 86% (n=116)<br>0.4 83% (n=72)<br>0.35 88% (n=67)<br>0.3 79% (n=43)<br>0.25 77% (n=30)<br>0.2 60% (n=20)<br>0.1 79% (n=14)<br>0 21% (n=14)<br>0 25 50 75 100 125<br>Renewal Rate<br>One Goal Att P<br><!-- End of picture text -->


