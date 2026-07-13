<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - How much of the NBA home court advantage is explained by rest - Unknown Authors.pdf -->

How Much of the NBA Home Court Advantage Is Explained by Rest? Oliver Entine Dylan Small Department of Statistics, The Wharton School, University of Pennsylvania 

## Home Court Advantage in Different Pro Sports 

||Home Team<br>Winning%|
|---|---|
|Basketball(NBA)|0.608|
|Football(NFL)|0.581|
|Hockey (NHL)|0.550|
|Baseball(Major Leagues)|0.535|



Data from NBA 2001-2002 through 2005-2006 seasons; NFL 2001 through 2005 seasons; NHL 1998-1999 through 20022003 seasons; baseball 1991-2002 seasons. 

Summary: The home advantage in basketball is the biggest of the four major American pro sports. 

## Possible Sources of Home Court Advantage in Basketball 

- Psychological support of the crowd. 

- Comfort of being at home, rather than traveling. 

- Referees give home teams the benefit of the doubt? 

- Teams are familiar with particulars/eccentricities of their home court. 

- Different distributions of rest between home and away teams (we will focus on this). 

# Previous Literature 

• Martin Manley and Dean Oliver have studied how the home court advantage differs between the regular season and the playoffs: They found no evidence of a big difference between the home court advantage in the playoffs vs. regular season.  Oliver estimated that the home court advantage is about 1% less in the playoffs. 

- We focus on the regular season. 

## Distribution of Rest for Home vs. Away Teams 

|Days of Rest|Home Team|AwayTeam|
|---|---|---|
|0|0.14|0.33|
|1|0.59|0.47|
|2|0.18|0.13|
|3|0.06|0.05|
|4+|0.04|0.03|



#### Source: 1999-2000 season. 

Summary: Away teams are much more likely to play back to back games, and are less likely to have two or more days of rest. 

# Data and Questions of Interest 

• Data will be analyzed from the 1999-2000 NBA season (Lakers won championship over Pacers). 

- Questions of interest: 

   - What is the impact of rest? 

– If the distribution of road team rest was set equal to the distribution of home team rest, how much of the home court advantage would go away? – Does the length of time a team has been on a road trip have an effect above and beyond its rest? 

# Basic Facts 

- Home teams in the 1999-2000 season won 61.7% of the time. 

- The average margin of victory for home teams was 3.62 points. 

# Model 

> _Yij_ =Margin of victory when team _i_ plays at home . against team _j_ 

_Yij_ = θ _i_ −θ _j_ + δ _i_ + β1 * _I_ [Home Rest = 0] + β2 * _I_ [Home Rest = 1] + β3 * _I_ [Home Rest=2] + 0* _I_ [Home Rest>2] − β1 _I_ [Away Rest = 0] − β2 _I_ [Away Rest = 1] − β3 _I_ [Away Rest = 2] − 0* _I_ [Away Rest>2] + _e_ 

> <sup>=Strength of home team</sup> 

> <sup>θ</sup> _i_ 

θ _j_ =Strength of away team<sup>=δ</sup> _i_ Home court advantage for team i 

if home rest = away rest 

β1,β2,β3 =Effect of rests of zero, one and two days respectively compared to rest of three or more days 

_e_ =Mean zero, normally distributed random variable 

# Effect of Rest 

• 

||Estimate|SE|p-value|
|---|---|---|---|
|1<br>β|-2.26|1.17|0.05|
|2<br>β|-1.09|1.13|0.34|
|3<br>β|<sup>-0.58</sup>|1.22|0.63|



The effect of having three or more days rest compared to playing back to back games is estimated to be 2.26 points; compared to having one day rest is estimated to be 1.09 points and compared to having two days rest is estimated to be 0.58 points. 

- Only the back to back vs. three or more days effect is statistically significant. 

- Other Aspects of Model Fit 

- • Approximate Average Prediction Error in Using Team Strengths and Home, Road Team Rest = Root Mean Square Error = 11.39 points. 

### • Normality Assumption for Residuals Appears Reasonable 



## Amount of Home Court Advantage Explained by Differences in Rest 

- Home Court Advantage for 1999-2000 = 3.62 points. 

- What would happen if the home team and road team had same distribution of rest? 

Average Home Court Advantage = Mean (<sup>δ</sup> _i_<sup>)</sup> 

Point Estimate: 3.31 95% CI: (2.63, 3.99) 

The different distributions of rest for home vs. away teams is estimated to only account for 9% of the home court advantage. 

## Does the Length of Team’s Road Trip Matter? 

ˆ = −0.25 γ 95% CI for =(-0.78, 0.28)γ 

The point estimate is that away teams actually do better the longer they have been on the road but it is not statistically significant. 

# Effect of Rest on Winning 

_Y_ =1 if team _i_ wins, 0 if team _j_ wins where team _i_ is the home team. _ij_ 

_P_ ( _Yij_ = 1) = expit{θ _i_ −θ _j_ + δ _i_ + β1 * _I_ [Home Rest = 0] + β2 * _I_ [Home Rest = 1] + β3 * _I_ [Home Rest=2] + 0* _I_ [Home Rest>2] − β1 _I_ [Away Rest = 0] − β2 _I_ [Away Rest = 1] − β3 _I_ [Away Rest = 2] − 0* _I_ [Away Rest>2]} 

_x_ 

_e_ where expit( _x x_ )=1+ _e_ 

> <sup>=Strength of home team</sup> 

> <sup>θ</sup> _i_ 

θ _j_ =Strength of away team 

> <sup>=</sup> 

> <sup>δ</sup> _i_ Home court advantage for team i 

if home rest = away rest 

β1,β2 ,β3 =Effect of rests of zero, one and two days respectively compared to rest of three or more days 

# Effect of Rest on Winning 

|•|
|---|



||Estimate|95% CI|
|---|---|---|
|exp(<br>1<br>β )|0.62|(0.39,1.00)|
|exp(<br>2<br>β )|0.76|(0.48,1.20)|
|exp(<br>3<br>β )|<sup>0.74</sup>|(0.45,1.22)|



Playing back to back games compared to having three or more days rest is estimated to multiply the odds of winning by 0.62. 

Playing on one day’s rest compared to having three or more days of rest is estimated to multiply the odds of winning by 0.76. 

Playing on two day’s rest compared to having three or more days of rest is estimated to multiply the odds of winning by 0.74. 

- Only the comparison between back to back games and three or more days rest is statistically significant. 

# Summary 

- _Rest does matter_ .  The effect of playing back to back games compared to playing on three or more days rest is estimated to be about 2.25 points. 

- _Rest is less important than home court advantage_ .  The home court advantage in the season studied was 3.62 points, greater than the difference between playing on three or more days rest vs. back to back games. 

• _Rest does not explain much of the home court advantage_ .  Home teams play on substantially more rest than away teams.  But this difference in rest does not appear to explain much of the home court advantage (it was estimated to only explain 9% of the home court advantage in the season studied). 

# Future Research 

- Analysis of more seasons 

- Random effects for team strengths and home court advantages. 

- Study the effects of the pattern of rest (e.g., how many games has the team played in the last four days, five days, …) 

- Investigation of other possible sources of home court advantage. 


