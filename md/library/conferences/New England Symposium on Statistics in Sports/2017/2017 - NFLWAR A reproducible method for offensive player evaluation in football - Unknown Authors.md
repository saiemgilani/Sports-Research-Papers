<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - NFLWAR A reproducible method for offensive player evaluation in football - Unknown Authors.pdf -->





Ron Yurko Sam Ventura Max Horowitz 

Department of Statistics Carnegie Mellon University 

NESSIS, 2017 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>1 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 







# Reproducible Research with `nflscrapR` 

**Recent work in football analytics is not easily reproducible:** Reliance on proprietary and costly data sources Data quality relies on potentially biased human judgement 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 2 / 36</mark> 

<mark>nfWAR</mark> 

# Reproducible Research with `nflscrapR` 

**Recent work in football analytics is not easily reproducible:** Reliance on proprietary and costly data sources Data quality relies on potentially biased human judgement 

`nflscrapR` **:** 



- `R` package created by Maksim Horowitz to enable easy data access and promote reproducible NFL research 





Collects play-by-play data from NFL.com and formats into `R` data frames Data is available for all games starting in 2009 

**Available on Github, install with:** `devtools::install github(repo=maksimhorowitz/nflscrapR)` 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>2 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 



# Pittsburgh Fans React 

Pittsburgh Post-Gazette article by Liz Bloom covered recent `nflscrapR` research and status of statistics in football 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>3 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# Pittsburgh Fans React 

Pittsburgh Post-Gazette article by Liz Bloom covered recent `nflscrapR` research and status of statistics in football 

**And the comments...** 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>3 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

Another Comment... 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 4 / 36</mark> 

<mark>nfWAR</mark> 

# Tremendous Insight! 

Recognizes the key flaws of raw football statistics: 

Moving parts in every play Need to assign credit to each player involved in a play Ultimately evaluate players in terms of wins 









Using `nflscrapR` we introduce **nflWAR** for offensive players: Reproducible framework for **wins above replacement** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 5 / 36</mark> 

<mark>nfWAR</mark> 

Goals of 











Properly evaluate every play Assign individual player contribution on each play Evaluate relative to replacement level Convert to a wins scale Estimate the uncertainty in WAR Apply this framework to each available season, 2009-2016 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 6 / 36</mark> 

<mark>nfWAR</mark> 

# How to Value Plays? 

**Expected Points (EP):** Value of play is in terms of _E_ ( _points of next scoring play_ ) How many points have teams scored when in similar situations? Several ways to model this 

**Win Probability (WP):** Value of play is in terms of _P(Win)_ Have teams in similar situations won the game? Common approach is logistic regression 

Can apply **nflWAR** framework to both, but will focus on **EP** today 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>7 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# How to Calculate EP? 

**Response** : _Y ∈{_ Touchdown ( **7** ), Field Goal ( **3** ), Safety ( **2** ), -Touchdown ( **-7** ), -Field Goal ( **-3** ), -Safety ( **-2** ), No Score ( **0** ) _}_ 

**Covariates** : _X_ = _{_ down, yards to go, yard line, ... _}_ 

**“Nearest Neighbors”:** 



Identify similar plays in historical data based on down, yards to go, yard line, etc. and take the average 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>8 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# How to Calculate EP? 

**Response** : _Y ∈{_ Touchdown ( **7** ), Field Goal ( **3** ), Safety ( **2** ), -Touchdown ( **-7** ), -Field Goal ( **-3** ), -Safety ( **-2** ), No Score ( **0** ) _}_ 

**Covariates** : _X_ = _{_ down, yards to go, yard line, ... _}_ 

**“Nearest Neighbors”:** 

Identify similar plays in historical data based on down, yards to go, yard line, etc. and take the average **But what defines a similar play?** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 8 / 36</mark> 

<mark>nfWAR</mark> 

# How to Calculate EP? 

**Response** : _Y ∈{_ Touchdown ( **7** ), Field Goal ( **3** ), Safety ( **2** ), -Touchdown ( **-7** ), -Field Goal ( **-3** ), -Safety ( **-2** ), No Score ( **0** ) _}_ 

**Covariates** : _X_ = _{_ down, yards to go, yard line, ... _}_ 

**“Nearest Neighbors”:** 

Identify similar plays in historical data based on down, yards to go, yard line, etc. and take the average **But what defines a similar play? Linear Regression:** 

_E_ ( _Y |X_ ) = _β_ 0 + _β_ 1 _Xdown_ + _β_ 2 _Xyards to go_ + _. . ._ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>8 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# How to Calculate EP? 

**Response** : _Y ∈{_ Touchdown ( **7** ), Field Goal ( **3** ), Safety ( **2** ), -Touchdown ( **-7** ), -Field Goal ( **-3** ), -Safety ( **-2** ), No Score ( **0** ) _}_ 

**Covariates** : _X_ = _{_ down, yards to go, yard line, ... _}_ 

**“Nearest Neighbors”:** 

Identify similar plays in historical data based on down, yards to go, yard line, etc. and take the average **But what defines a similar play? Linear Regression:** 

_E_ ( _Y |X_ ) = _β_ 0 + _β_ 1 _Xdown_ + _β_ 2 _Xyards to go_ + _. . ._ 

**But is treating the next score as continuous appropriate?** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>8 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

Distribution of Next Score 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>9 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

Linear Regression Approach... 

**What are the assumptions of linear regression?** _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ) ( _iid_ ) 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>10 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

Linear Regression Approach... IS A DISASTER! 

## **What are the assumptions of linear regression?** _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ) ( _iid_ ) 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>11 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# Multinomial Logistic Regression 

Logistic regression to **model the probabilities** of 

_Y ∈{_ Touchdown ( **7** ), Field Goal ( **3** ), Safety ( **2** ), 

-Touchdown ( **-7** ), -Field Goal ( **-3** ), -Safety ( **-2** ), No Score ( **0** ) _}_ 

Specified with 6 logit transformations relative to No Score: 



... 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 12 / 36</mark> 

<mark>nfWAR</mark> 

# Multinomial Logistic Regression 

**Model is generating probabilities, agnostic of value associated with each next score type** 

Next Score: _Y ∈{_ Touchdown (7), Field Goal (3), Safety (2), No Score (0), -Safety (-2), -Field Goal (-3), -Touchdown (-7) _}_ Situation: _X_ = _{_ down, yards to go, yard line, ... _}_ 

Outcome probabilities: _P_ ( _Y_ = _y |X_ ) **Expected Points (EP)** = _E_ ( _Y |X_ ) =<sup>�</sup> _y_<sup>_P_(</sup><sup>_Y_=</sup><sup>_y|X_)</sup><sup>_∗y_</sup> 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 13 / 36</mark> 

<mark>nfWAR</mark> 







# Expected Points Added 

**Expected Points Added (EPA)** estimates a play’s value based on the change in situation, providing a point value 



_EPA_ = _EP − EP playi playi_ +1 _playi_ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>14 / 36</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# Expected Points Added 

**Expected Points Added (EPA)** estimates a play’s value based on the change in situation, providing a point value 



_EPA_ = _EP − EP playi playi_ +1 _playi_ 

For passing plays can use **air yards** to calculate **airEPA** and **yacEPA** (yards after catch EPA): 





_airEPAplayi_ = _EPin air playi − EPstart playi yacEPAplayi_ = _EPplayi_ +1 _− EPin air playi_ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 14 / 36</mark> 

<mark>nfWAR</mark> 

# Expected Points Added 

**Expected Points Added (EPA)** estimates a play’s value based on the change in situation, providing a point value _EPA_ = _EP − EP playi playi_ +1 _playi_ 

For passing plays can use **air yards** to calculate **airEPA** and **yacEPA** (yards after catch EPA): 





_airEPAplayi_ = _EPin air playi − EPstart playi yacEPAplayi_ = _EPplayi_ +1 _− EPin air playi_ 

But how much credit does each player deserve? e.g. On a pass play, how much credit does a QB get vs the receiver? **One player is not solely responsible for a play’s EPA** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 14 / 36</mark> 

<mark>nfWAR</mark> 







# How to Allocate EPA? 

Using proprietary, manually collected data, **Total QBR** _(Oliver et al., 2011)_ divides credit between those involved in passing plays 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 15 / 36</mark> 

<mark>nfWAR</mark> 

# How to Allocate EPA? 

Using proprietary, manually collected data, **Total QBR** _(Oliver et al., 2011)_ divides credit between those involved in passing plays **Publicly available data only includes those directly involved:** 



Passing: 





Individuals: passer, target receiver, tackler(s), interceptor Context: air yards, yards after catch, location, and if the passer was hit on the play 



Rushing: 





Individuals: rusher and tackler(s) Context: run gap and location 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 15 / 36</mark> 

<mark>nfWAR</mark> 

# Multilevel Modeling 

Growing in popularity (and rightfully so): 



“Multilevel Regression as Default” - Richard McElreath 





Natural approach for data with **group structure** , and different levels of variation within each group e.g. QBs have more pass attempts than receivers have targets Every play is a repeated measure of performance 



Baseball example: Deserved Run Average _(Judge et al., 2015)_ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 16 / 36</mark> 

<mark>nfWAR</mark> 

# Multilevel Modeling 

Key feature is the **groups are given a model** - treating the levels of groups as similar to one another with **partial pooling** Simple example of **varying-intercept** model: 

_EPAi ∼ N_ ( _QBj_ [ _i_ ] + _RECk_ [ _i_ ] + _βxi , σEPA_<sup>2)</sup><sup>_,fori_=1</sup><sup>_, . . . ,_#</sup><sup>_ofplays,_</sup> _QBj ∼ Normal_ ( _µQB , σQB_<sup>2)</sup><sup>_,forj_=1</sup><sup>_, . . . ,_#</sup><sup>_ofQBs,_</sup> _RECk ∼ Normal_ ( _µREC , σREC_<sup>2)</sup><sup>_,fork_=1</sup><sup>_, . . . ,_#</sup><sup>_ofReceivers_</sup> 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 17 / 36</mark> 

<mark>nfWAR</mark> 

# Multilevel Modeling 

Key feature is the **groups are given a model** - treating the levels of groups as similar to one another with **partial pooling** Simple example of **varying-intercept** model: 

_EPAi ∼ N_ ( _QBj_ [ _i_ ] + _RECk_ [ _i_ ] + _βxi , σEPA_<sup>2)</sup><sup>_,fori_=1</sup><sup>_, . . . ,_#</sup><sup>_ofplays,_</sup> _QBj ∼ Normal_ ( _µQB , σQB_<sup>2)</sup><sup>_,forj_=1</sup><sup>_, . . . ,_#</sup><sup>_ofQBs,_</sup> _RECk ∼ Normal_ ( _µREC , σREC_<sup>2)</sup><sup>_,fork_=1</sup><sup>_, . . . ,_#</sup><sup>_ofReceivers_</sup> 

Unlike linear regression, no longer assuming independence Provides estimates for **average play effects** while providing necessary **shrinkage** towards the group averages 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 17 / 36</mark> 

<mark>nfWAR</mark> 

# nflWAR Modeling 

Use varying-intercepts for each of the grouped variables With location and gap, create **Team-side-gap** as O-line proxy e.g. PIT-left-end, PIT-left-guard, PIT-middle Separate passing and rushing with different grouped variables Passing: Offensive team, QB, receiver, defensive team Rushing: Team-side-gap, rusher, defensive team 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 18 / 36</mark> 

<mark>nfWAR</mark> 

# nflWAR Modeling 

Use varying-intercepts for each of the grouped variables With location and gap, create **Team-side-gap** as O-line proxy e.g. PIT-left-end, PIT-left-guard, PIT-middle Separate passing and rushing with different grouped variables Passing: Offensive team, QB, receiver, defensive team Rushing: Team-side-gap, rusher, defensive team 

Each individual intercept for player groups is an estimate for a player’s effect, **individual points added (iPA)** Intercepts for team groups are **team points added (tPA)** Multiply iPA/tPA by attempts to get **individual/team points above average (iPAA/tPAA)** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 18 / 36</mark> 

<mark>nfWAR</mark> 

# Rushing Breakdown 

With EPA as the response, two separate models: 

- RB/FB/WR/TE designed rushing plays Adjust for rusher position as non-grouped variable QB - designed runs, scrambles, and sacks Replace Team-side-gap with offensive team Provides _iPArush_ and _tPArush side−gap_ estimates 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 19 / 36</mark> 

<mark>nfWAR</mark> 

# Group Variation for RB/FB/WR/TE Rushing Model 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 20 / 36</mark> 

<mark>nfWAR</mark> 

# Group Variation for QB Rushing Model 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 21 / 36</mark> 

<mark>nfWAR</mark> 

# Which Teams Ran Efficiently in 2016? 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 22 / 36</mark> 

<mark>nfWAR</mark> 

# Passing Breakdown 

Could simply use EPA, or **take advantage of air yards** Two separate models for airEPA and yacEPA, where both models consider all pass attempts but the response depends on the model: Receptions assigned airEPA and yacEPA for respective models Incomplete passes use observed EPA **Emphasize importance of completions** Both adjust for QBs hit, receiver positions, and pass location yacEPA model adjusts for air yards 

Provides _iPAair_ and _iPAyac_ estimates 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 23 / 36</mark> 

<mark>nfWAR</mark> 

# Variation of Passing Intercepts (airEPA) 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 24 / 36</mark> 

<mark>nfWAR</mark> 

# Variation of Passing Intercepts (yacEPA) 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 25 / 36</mark> 

<mark>nfWAR</mark> 

# Passing Efficiency in 2016 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 26 / 36</mark> 

<mark>nfWAR</mark> 

# Relative to Replacement Level 

Following an approach similar to **openWAR** _(Baumer et al., 2015)_ , defining replacement level based on roster 

For each team and position sort by number of attempts (separate RB/FB replacement level for rushing and receiving) 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 27 / 36</mark> 

<mark>nfWAR</mark> 

# Relative to Replacement Level 

Following an approach similar to **openWAR** _(Baumer et al., 2015)_ , defining replacement level based on roster For each team and position sort by number of attempts (separate RB/FB replacement level for rushing and receiving) 

Player _i_<sup>_′_</sup> _s iPAAi,total_ = _iPAAi,rush_ + _iPAAi,air_ + _iPAAi,yac_ Creates a replacement-level iPAA that “shadows” a player’s performance, denote as _iPAA_<sup>_replacement_</sup> _i_ Player _i_<sup>_′_</sup> _s_ **individual points above replacement (iPAR)** as: 

_iPARi_ = _iPAAi,total − iPAA_<sup>_replacement_</sup> _i,total_ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 27 / 36</mark> 

<mark>nfWAR</mark> 

# Convert to Wins 

“Wins & Point Differential in the NFL” - _(Zhou & Ventura, 2017)_ (CMU Statistics & Data Science **freshman** research project) 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 28 / 36</mark> 

<mark>nfWAR</mark> 

WAR! 

Fit a linear regression between wins and total score differential: 

1 _Points per Win_ = ˆ _βScore Diff_ 

e.g. In 2016 _β_<sup>ˆ</sup> _Score Diff_ = 0 _._ 0319, roughly **31 points per win** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 29 / 36</mark> 

<mark>nfWAR</mark> 

WAR! 

Fit a linear regression between wins and total score differential: 

1 _Points per Win_ = ˆ _βScore Diff_ 

e.g. In 2016 _β_<sup>ˆ</sup> _Score Diff_ = 0 _._ 0319, roughly **31 points per win** 

and finally arrive at **wins above replacement (WAR)** : 

_iPAR WAR_ = _Points per Win_ 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 29 / 36</mark> 

<mark>nfWAR</mark> 

# QB WAR in 2016 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 30 / 36</mark> 

<mark>nfWAR</mark> 

# RB WAR in 2016 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 31 / 36</mark> 

<mark>nfWAR</mark> 

TE WAR in 2016 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 32 / 36</mark> 

<mark>nfWAR</mark> 

# WR WAR in 2016 



<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 33 / 36</mark> 

<mark>nfWAR</mark> 

# Recap and Future of nflWAR 

Properly evaluating every play with EPA generated with multinomial logistic regression model 

Multilevel modeling provides an intuitive way for estimating player effects and **can be extended with data containing every player on the field for every play** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 34 / 36</mark> 

<mark>nfWAR</mark> 

# Recap and Future of nflWAR 

Properly evaluating every play with EPA generated with multinomial logistic regression model 

Multilevel modeling provides an intuitive way for estimating player effects and **can be extended with data containing every player on the field for every play** 

**Naive to assume player has same effect for every play!** 

Need to **estimate the uncertainty** in the different types of iPA to generate intervals of WAR values 

Refine the definition of replacement-level, e.g. what about down specific players? 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 34 / 36</mark> 

<mark>nfWAR</mark> 

# Carnegie Mellon Sports Analytics Conference 



**Clear your calendars for Oct 28th! And visit www.cmusportsanalytics.com/conference for more information! #CMSAC** 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 35 / 36</mark> 

<mark>nfWAR</mark> 

# Acknowledgements 

**Max Horowitz** for creating `nflscrapR` 

**Sam Ventura** for advising every step in the process **Jonathan Judge** for answering questions on multilevel modeling **Rebecca Nugent** and **CMU Statistics and Data Science** for all of their instruction, motivation, and support! 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 36 / 36</mark> 

<mark>nfWAR</mark> 

References I 

[Gelman and Hill, 2007]. [Baumer et al., 2015]. [Oliver, ]. 

[Hastie et al., 2009]. [Carroll et al., 1998]. 

[Pasteur and David, 2017]. [Goldner, 2017]. [Berri and Burke, 2017]. [Carter and Machol, 1971]. [Burke, ]. [out, ]. [num, ]. 



Football outsiders. 





Baumer, B., Jensen, S., and Matthews, G. (2015). openwar: An open source system for evaluating overall player performance in major league baseball. _Journal of Quantitative Analysis in Sports_ , 11(2). 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>1 / 4</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

# References II 









Berri, D. and Burke, B. (2017). Measuring productivity of nfl players. In Quinn, K., editor, _The Economics of the National Football League_ , pages 137–158. Springer, New York, New York. Burke, B. Advanced football analytics. Carroll, B., Palmer, P., Thorn, J., and Pietrusza, D. (1998). _The Hidden Game of Football: The Next Edition_ . Total Sports, Inc., New York, New York. Carter, V. and Machol, R. (1971). Operations research on football. _Operations Research_ , 19(2):541–544. 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 2 / 4</mark> 

<mark>nfWAR</mark> 

References III 







Gelman, A. and Hill, J. (2007). _Data Analysis Using Regression and Multilevel/Hierarchical Models_ . Cambridge University Press, Cambridge, United Kingdom. Goldner, K. (2017). Situational success: Evaluating decision-making in football. In Albert, J., Glickman, M. E., Swartz, T. B., and Koning, R. H., editors, _Handbook of Statistical Methods and Analyses in Sports_ , pages 183–198. CRC Press, Boca Raton, Florida. Hastie, T., Tibshirani, R., and Friedman, J. (2009). _The Elements of Statistical Learning: Data Mining, Inference, and Prediction_ . Springer, New York, New York. 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>3 / 4</mark> 

<mark>NESSIS, 2017</mark> 

<mark>nfWAR</mark> 

References IV 





Oliver, D. Guide to the total quarterback rating. 

Pasteur, R. D. and David, J. A. (2017). Evaluation of quarterbacks and kickers. In Albert, J., Glickman, M. E., Swartz, T. B., and Koning, R. H., editors, _Handbook of Statistical Methods and Analyses in Sports_ , pages 165–182. CRC Press, Boca Raton, Florida. 

<mark>Ron Yurko (@Stat Ron)</mark> 

<mark>NESSIS, 2017 4 / 4</mark> 

<mark>nfWAR</mark> 


