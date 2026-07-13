<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - A survey of advanced modeling techniques for forecasting college football game outcomes - Unknown Authors.pdf -->



- **_A Survey of Advanced Modeling Techniques for Forecasting College Football Game Outcomes_** 



Charles South<sup>1</sup> , PhD and Edward Egros<sup>2</sup> , MS 

## **:** **<u>Purpose</u>** 

Can we use box score, point spread, and recruiting data to accurately forecast outcomes of college football games using modern machine learning and Bayesian modelling approaches? 

## **<u>Data:</u>** 

The data used for this college football forecast consisted of 4,339 games between Football Bowl Subdivision (FBS) teams between the 2011 and 2016 seasons<sup>3</sup> . The data set was augmented with composite team ratings<sup>4</sup> for each recruiting class dating back to 2008 to account for seniors in the 2011 season. 

# **Data Prep/Manipulation Process:** 

Create training data Cycle through each team (2011-2014 data) and test and each year, find data (2015 data), evaluate cumulative averages and select top model _within_ year. paradigm. Create matchup numbers to combat issue of the Recompile data set with same game repeating cumulative averages. twice (with home and away team permuted). Cre <mark>ate covariates related Me</mark> rge recruiting data, to relative differences add 4 lags of composite between the teams rather rankings as well as than absolute averages of previous 2, 3, performance. and 4 composite rankings. 3http://www.seldomusedreserve.com/?page_id=8805 4http://247sports.com/Article/247Rating-Explanation-81574 

|**Modelling Paradigms:**<br>**Penalized Regression**<br>Elastic Net<br>Ridge<br>Regression<br>Lasso<br>**Non-Parametric**<br>Random<br>Forests/Gradient<br>Boosting<br>K-Nearest<br>Neighbors<br>Neural Networks|**Bayesian**<br>Random<br>Precision<br>Only<br>Random<br>Slopes and<br>Precision|
|---|---|
|**Modelling Details:**<br>•<br>Dependent Variable: point differential<br>•<br>R packages utilized:_glmnet_,_randomForest_,_FNN_,_nne_<br>•<br>Where applicable, the_caret_package was used to tune<br>•<br>For the Bayesian models, a the model was compresse<br>selected by the lasso.<br>•<br>Bayesian framework:<br>𝒚𝒊𝒋~𝑵𝒐𝒓𝒎𝒂𝒍<br>𝝁𝒊𝒋, 𝝉𝒊**,**<br>𝝁𝒊𝒋= 𝜷𝟎+ 𝜷𝟏𝑿𝟏𝒊𝒋+ ⋯+ 𝜷𝒑𝑿𝒑𝒊𝒋**,**<br>𝜷𝒑~𝑵𝒐𝒓𝒎𝒂𝒍<br>𝟎. 𝟎𝟎𝟏, 𝟎. 𝟎𝟎𝟏**,**<br>𝝉𝒊~𝑮𝒂𝒎𝒎𝒂<br>𝟏, 𝟏<br>**predicted point difference**<br>**for team**𝒊**on game**𝒋<br>**Lasso Retained Variables**<br> <br>|_t_,_xgboost_.<br>the models.<br>d to only include variables<br>**random precision for**<br>**team**𝒊<br>|
|**Yards Per Pass Attempt (YPPA)**<br>**Yards Per Rush Attempt (YPRA)**|**Rush Attempts**|
|**Total Yards**<br>**Yards Per Play (YPP)**|**Turnovers (TO)**|
|**Opponent Points Scored**<br>**Opponent YPRA**|**Opponent Total Yards**|
|**Opponent Turnovers**<br>**Opponent Penalty Yards**|**Average Point Differential**|
|**Opponent Offense Passing Yards**<br>**Opponent Offense YPRA**|**Opponent Offense Total Yards**|
|**Opponent Offense YPP**<br>**Opponent Defense Total Rush Yds**|**Opponent Defense YPRA**|
|**Opponent Defense Total Yards**<br>**Opponent Def YPP**|**Opponent Defense TO**|
|**Opponent Average Points**<br>**Differential**<br>**Difference in Win Percentage**|**Home Field Advantage**|
|**Composite Ranking, Lag 2 (CR)**<br>**Average CR (Last 2 Years)**|**Average CR (Last 3 Years)**|



# **Final Predictions:** 

All generated models made predictions for the same game twice. Our decision rule was designed to be as intuitive as possible – if both predictions resulted in the same team being favored, the favored team was deemed the predicted winner. If the predictions diverged, the team with the larger predicted point differential was deemed the predicted winner. 

|**Summary of Results:**||||
|---|---|---|---|
|**Model**|**Overall**<br>**Prediction**|**PPV**|**NPV**|
|**Lasso**|**75.0%**|**77.3%**|**72.4%**|
|Random Forest|74.1%|**78.9%**|69.0%|
|Gradient Boosting|72.9%|76.9%|68.5%|
|K-Nearest Neighbors|69.0%|71.3%|66.3%|
|Neural Network|71.6%|75.8%|66.4%|
|Bayesian|74.1%|76.5%|71.5%|



# **Conclusions/Future Work:** 

• The lasso was the top performer, slightly edging out the Bayesian model and random forests. • In terms of variable importance, composite recruit rankings are important, though it appears it takes at least 2 years for players to develop. • Volume and efficiency are important – as is home field advantage. • Of the 27 predictors identified by the lasso, 15 were directly related to opponent strength. Schedule matters. • 

Volume and efficiency are important – as is home field advantage. Of the 27 predictors identified by the lasso, 15 were directly related to opponent strength. Schedule matters. An ensemble method may improve predictive ability. 

1South Statistical Consulting and Analytics, LLC 2Fox 4 News (Dallas), InsideSportsAnalytics.com 


