<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - Scheduling effects in the NBA and NHL and their betting markets - Unknown Authors.pdf -->

**2017 New England Symposium on Statistics in Sports at Harvard University, Cambridge, MA** 

_•_ Fitted SLR of home MOV on Vegas Line (V) in the NBA: _MOV_<sup>�</sup> = 0 _._ 01 + _._ 95 _V_ 



# **Scheduling Effects in the NBA and NHL** 

Justin B. Post, Len Stefanski and Jason A. Osborne 

## Introduction 

De t. of Statistics, N.C. State Universit <u>p y</u> 

## Perceived Schedule Effects 



## Data Sources 

- Fatigue effects on spread highly significant. _r_<sup>2</sup> = _._ 82 of variability in spread explained by linear model. _MSE_ = 2 _._ 9 



- _•_ covers.com _•_ 

- pro-basketball-reference.com hockey-reference.com 

- Unadjusted plots: 

- Who’s at home explains a bit more variation than who’s visiting. 





|The SAS System - The GL|M Proce|dure||||
|---|---|---|---|---|---|
|Dependent Variable: veg|aswinby|||||
|||Sum of||||
|Source|DF|Squares|Mean Square|F Value|Pr > F|
|Model|302|222536.6167|736.8762|87.03|<.0001|
|Error|5816|49241.3050|8.4665|||
|Corrected Total|6118|271777.9216||||
|R-Square<br>Coeff Var|Ro|ot MSE<br>veg|aswinby Mean|||
|0.818818<br>100.3955|2.|909729|2.898268|||
|Source|DF|Type III SS|Mean Square|F Value|Pr > F|
|hteam(season)|145|111447.1980|768.6014|90.78|<.0001|
|vteam(season)|145|98784.6556|681.2735|80.47|<.0001|
|h_ystrday|2|1206.0397|603.0199|71.22|<.0001|
|v_ystrday|2|602.0291|301.0146|35.55|<.0001|
|h_ystrday*v_ystrday|4|33.7255|8.4314|1.00|0.4083|



- On teams who score average, today played yesterday signifi- 

- cantly less than those that were idle. (Entine and Small (2008).) 

- Scheduling discrepancy has rested home teams playing tired visitors. Particularly for NBA West teams. In an attempt to balance this advantage, other teams have reduced _dis_ advantage as road teams. cs ~~i~~ rl (See map courtesy of reddit user: ) 

- After adjustment for scheduling discrepancy using factorial effects in linear/generalized linear models, much of the home ice advantage in the NHL vanishes. Some of it remains in the NBA. 

## Linear and generalized linear models 

## Scheduling discrepancy for visitors 

For a given season, linear models for margin of victory _Y_ with factorial effects for yesterday and team: 

- Visitors played yesterday more than **twice as frequently as the home team** (both NHL/NBA). 

|Home, Visiting team effects<br>|||
|---|---|---|
|_Yi_=_β_0+<br>�<br>��<br>�<br>�<br>_β_<sup>_H_</sup><br>_t _<sup>_xH_</sup><br>_it_ <sup>+</sup><br>�<br>_β_<sup>_V_</sup><br>_t _<sup>_xV_</sup><br>_it_<br>+_β_<sup>_HP_</sup>_xi,_31+_β_<sup>_V P_</sup>_xi,_32+<br>�<br>|_β_<sup>_HV P_</sup>_xi,_33<br>�<br>+_ϵi_=**x**_i_|_β_+_ϵi_|
|_t_<br>_t_<br>��<br>Fatigue effec|ts||
|_•_Model then pools over last 4 seasons, with team effects nested in sea<br>_• x_<sup>_H_</sup>_, x_<sup>_V_ </sup>- indicators for which home, visiting team,_xi,_31_, xi,_32_, xi,_33-<br>_•_Similarly for win probability (_π_) models, withlog<br>�<br>_πi_<br>1_−πi_<br>�<br>=_xi·β_|son.<br>indicators for playing|yesterday|
|proc glimmix data=teamseq; title "yesterday-idle";<br>class hteam vteam hidle_yest vidle_yest season;|||
|*<sup>model home_mov=hteam(season) vteam(season) hidle_yest|vidle_yest </sup>|<sup>;</sup>||
|model home_wins(event=’1’)=hteam(season) vteam(season) hidle_yest<br>estimate "intercept" intercept 1/ilink;<br>lsmeans hidle_yest|vidle_yest/ilink;<br>Parameter Estimates<br>Estimated margin of victory (points/goals):||vidle_yest /dist=bina|ry;|
|Adjusted margin of victory<br>Adju|sted win probability||
|Visitor(NBA)<br>Visitor(NHL)<br>Visitor(NBA)|Visitor(NHL)||
|Home<br>Played<br>Idle<br>Mean<br>Played<br>Idle<br>Mean<br>Played<br>Idle|Mean<br>Played<br>Idle|Mean|
|Played<br>2.3<br>0.6<br>1.5<br>**0.0**<br>0.12<br>0.06<br>0.60<br>0.52<sup>_~~∗~~_</sup>|0.57<br>0.49<br>0.50|0.49|
|Idle<br>3.8<sup>_∗_</sup><br>2.6<sup>_∗_</sup><br>3.2<br>0.45<sup>_∗_</sup>0.23<sup>_∗_</sup><br>0.34<sup>_∗_</sup><br>0.65<br>0.60|0.63<br>0.58<sup>_∗_</sup>0.54<sup>_∗_</sup>|0.56<sup>_∗_</sup>|
|Mean<br>3<br>1.6<br>2.3<br>0.22<sup>_~~∗~~_</sup>0.17<sup>_~~∗~~_</sup><br>0.19<sup>_~~∗~~_</sup><br>0.63<br>0.57|0.60<br>0.54<br>0.52|0.53<sup>_~~∗~~_</sup>|
|NBA(Points)<br>NHL(Goals)<br>NBA|NHL||
|_•_After adjustment for team & fatigue effects, estimated NHL home <br>estimate is 0.5. Fatigue effects plausibly additive|team MOV is 0, win|probability|



#### **Overtime effects** 

- NBA teams a little more likely to have played yesterday: 

- For betting the over/under, including overtime effect debiases estimators of team capacities to score and give up points. 

|NBA<br>Visitor<br>Home|
|---|
|Home<br>Played<br>Idle<br>Total|
|Played<br>346<br>332<br>678<br>**(14%)**|
|Idle<br>1143<br>3099<br>4242|
|Visitor Total<br>1489<br>3431<br>4920|
|**(30%)**|
|NHL<br>Visitor<br>Home<br>|
|Home<br>Played<br>Idle<br>Total|
|Played<br>234<br>280<br>514<br>**(10.4%)**|
|Idle<br>967<br>3439<br>4406|
|Visitor Total<br>1201<br>3719<br>4920|
|**(24.4%)**<br>_•_Effect is most pronounced for GSW,DEN,MIA,UTA,POR,HOU.<br>NBA Regional effects (see map) highly signifcant (_p < ._0001)<br>|
|2016-2017<br>Team rested,<br>Team tired,|
|Team<br>Location<br>opptired<br>opprested<br>Advantage|
|GS<br>home<br>15<br>0<br>15|
|GS<br>away<br>3<br>14<br>-11|
|CHI<br>home<br>8<br>3<br>5|
|CHI<br><br>5<br>10<br>5|
|away<br><br><br>-<br>**Regional advantages in the NBA**|
|G<br>G<br>G<br>10|
|G<br>G<br>G<br>G|
|G<br>5|
|chedule Advantage<br><br>0<br>~~G~~<br>West, Home<br>Not West, Home<br>West, Visiting<br>Not West, Visiting|
|S<br>−5|
|10|
|09−10<br>10−11<br>11−12<br>12−13<br>13−14<br>14−15<br>15−16<br>16−17<br>−|



- Forecasting today’s game using data til yesterday with/without OT effect 

|%macro betday(season,pickday);|
|---|
|proc glm data=temp; title "overunder - prospective betting";|
|iplay_f gdate<br><= &pickdate and<br>season="&season";|
|class hteam vteam ; *overtime;|
|model gsum2=hteam<br>vteam overtime2; * gsum2 missing, overtime2=0 today;|
|*<sup>model gsum2=hteam</sup><br>vteam;<br>* <sup>both observed yesterday;</sup>|
|output<br>out=bets p=p;|
|%mend;|
|* <sup>loop over season, pickday ;</sup>|



**–** Forecasts from models without OT bigger than forecasts from models with OT 

� **–** = Use diff between forecast and over/under: _PD_ 5 _round_ sum _−_ over/under ( _,_ 5), _PD_ 5 � = 54% select games where _| |_ large, win with with _p_ when using OT effect. Counts Winning percentage Without overtime Without overtime <u>(With overtime)</u> PD5 _<_ 10 PD5 _<u>≥</u>_ 10 PD5 _<_ 10 PD5 _<u>≥</u>_ 10 PD5 _<_ 10 3215 174 .503/.505 .454<sup>_~~∗~~_</sup> PD5 _<u>≥</u>_ 10 256 898 .508/.504 .543<sup>_∗_+</sup> .535 

+ significantly different from 0.5 ( _p_ = _._ 01), _∗_ winning pct equal for both forecasts 

## Findings 

      - Broad takeaways: (1) Fatigue explains some home court and a lot of home ice advantage. (2) Some of the NBA Western conference dominance is attributable to systematic home court scheduling advantage over Eastern conference, with home team a moderately greater determinant of victory than road team. 

- Using the fitted models, the best, worst teams, on average: 

   - 2017 Home Court GS Warriors win by 14.8 points, 2017 Road GS Warriors win by 7.6 points 2014 Home Courts 76ers lose by 10.6 points, 2015 Road 76ers lose by 12.7 2017 Home Ice Caps win by 1.6 goals, 2017 Road Rangers win by 0.9 goals 2015 Home Ice Coyotes lose by 1.3 goals, 2015 Road Sabers lose by 1.7 goals 

- Technical takeaways: Schedule effects highly significant on both points/goals and win probability. After adjustment for team strength and schedule effects, estimated home ice advantage for both teams rested estimate is 0. NBA home court advantage remains at � = 2 _._ 3 _µ_ , averaging equally over fatigue conditions. Estimating team scor- 

- ing/defending effects improved by inclusion of OT effect, preliminary evidence of betting market inefficiency. 



### **References** 

Entine, O. A. and Small, D. S. (2008), ‘The role of rest in the nba home-court advantage’, _Journal of Quantitative Analysis in Sports_ **4** (2). 

Season 


