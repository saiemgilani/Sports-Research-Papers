<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - TRAP A Predictive Framework for Trail Running Assessment Performance - Unknown Authors.pdf -->



# **<u>TRAP:</u> A Predictive Framework for Trail Running Assessment of Performance** 



Riccardo Fogliato, Natalia Lombardi Oliveira, and Ronald Yurko 

Carnegie Mellon University Department of Statistics & Data Science 

## **Overview of Modeling** 

## **International Trail Running Association** 

## **EDA for UTMB 2017-2018 races** 



The International Trail Running Association (ITRA) is the world’s largest trail running association. Its website contains records of more than 1.6m runners in races such as UTMB, Lavaredo Ultra Trail, Western States, Sierre-Zinal... 

We model the runner’s performance at the checkpoint level: for each station, we output a prediction both for the following station and for the end of the race in Chamonix. 









We develop **ScrapITRA** , a Python package for scraping, downloading, and formatting data of both runners and races from the website of ITRA. ScrapITRA is available at 

Our models target three quantities: 

- **(I) probability of dropping out** (logistic regression, random forest, XGBoost); 

**(II) expected passage time** (LASSO, random forest, XGBoost); 

https://github.com/ricfog/ScrapITRA. How does ScrapITRA work? The package leverages Selenium and BeautifulSoup for dynamic scraping. 

- **(III) prediction interval for passage time** (random forest). 

Figure: Top left: Number of runners who dropped out of the race at each checkpoint for 2017 and 2018 UTMB. Top right: Finishing time distribution among runners who finished 2017 and 2018 UTMB. Bottom: Time to checkpoint for 2017 and 2018 UTMB. 



What do you obtain with ScrapITRA? Get data at I runner level: demographics and results; I race level: runners’ results and details on the trail. Why? You can now analyze performance of more than 1m runners over the last 15 years. 

We evaluate models with leave one-year-out (LOYO) cross validation (CV) for UTMB 2017-2018. 

## **(III) Prediction interval results** 

## **Modeling Results** 



<!-- Start of picture text -->
XGBoost with Ckpt+ITRA+Lag1& 2 - LOYO CV AUC: 0.88, liftAUC: 3.33. Quantile regression via random forest<br>1.00 1.00 1.00 300<br>0.90 0.90 200 Quantile0.05<br>0.750.500.25 Set of featuresCkpCkp+ITRACkp+ITRA+Lag1Ckp+ITRA+Lag1&2Intercept 0.750.500.25 ModelInterceptLogistic regRandom forestXgboost 0.750.500.25 Figure: Prediction interval for 5%, median, and 95% quantiles for100 3 4 5 6 7 8 9 10 11 12 Checkpoint13 14 15 16 17 18 19 20 21 22 23 24 0.50.95<br>0.100.00 0.100.00 0.00 a randomly selected runner.<br>0.00 0.10 0.25False positive fraction0.50 0.75 0.90 1.00 0.00 0.10 0.25 False positive fraction0.50 0.75 0.90 1.00 3 4 5 6 7 8 9 10 11Checkpoint12 13 14 15 16 17 18 19 20 21 22 23 24<br>Predicted time (minutes)<br>True positive fraction True positive fraction<br>Area Under the Curve (AUC)<br><!-- End of picture text -->

**(I) Best model:** XGBoost with Ckpt+ITRA+Lag1& 2 - LOYO CV AUC: 0.88, liftAUC: 3.33. 

## **UTMB** 

Ultra-Trail du Mont-Blanc (UTMB) is the “holy grail” of ultra trail running. Starting in 2003, 2500 runners from over 100 nations gather in Chamonix (France) in the last week of August for a tough challenge: 171 km with more than 10000 m of elevation gain passing through France, Italy, and Switzerland (Figure 1). While elite runners typically complete the race in **_⇠_** 20 hours, most runners cross the finish line in more than 40 hours, right before the time barrier of 46.5 hours. Due to its toughness and thanks to the beautiful landscape, UTMB is seen by many as the pinnacle of a career in trail running. 

## **Discussion and Future Work** 

Figure: Left and center: comparison of ROC curves for features and models with features Ckp+ITRA+Lag1& 2. Right: AUC by checkpoint for xgboost and features Ckp+ITRA+Lag1& 2. 

I dynamically adjust between checkpoint I integrate models (I) and (III) for classification I explore methodology for intervals, eg conformal I **propose alternative to the ITRA score** I test general framework on other races. 

**(II) Best model:** Random forest with Ckpt+ITRA+Lag1& 2 - LOYO CV RMSE: 15. Considerable improvement in model performance by including ITRA runner level information for tree-based models, capturing nonlinear interactions between runners and checkpoints. 



<!-- Start of picture text -->
Intercept-only LASSO Random Forest XGBoost<br>XGBoost 100<br>50<br>Random Forest Intercept-only RMSE 0<br>100<br>LASSO 50<br>20 2017-2018 LOYO CV RMSE30 40 50 0 5 10 15 20 25 5 10 15 20 Checkpoint25 5 10 15 20 25 5 10 15 20 25<br>Features Ckp Ckp+ITRA Ckp+ITRA+Lag1 Ckp+ITRA+Lag1&2 Number of runners 1600 1800 2000<br>2017<br>Model type RMSE<br>2018<br><!-- End of picture text -->



We hope that our seminal work might help the Data Science community gain interest in the (still unexplored) world of trail running. For this reason, we plan to release the ITRA data set on Kaggle. 

Figure: UTMB 2017 course map. 

## **References** 

Qualification to UTMB is based on a draft (last year 1 in 3 chances of getting in) and a minimum ITRA score is required to get into the draft. The extreme conditions of the race make prediction tasks challenging. 

- [1] Chen et al. _xgboost: Extreme Gradient Boosting_ , 2019. R package version 0.81.0.1. 

- [2] Trevor Hastie, Robert Tibshirani, and Jerome Friedman. _The Elements of Statistical Learning: Data Mining, Inference, and Prediction_ . Springer, New York, New York, 2009. 

Figure: Left: comparison of LOYO CV RMSE curves for features and models. Right: LOYO CV RMSE by checkpoint and year for models using Ckp+ITRA+Lag1& 2. 

Corresponding Author: Riccardo Fogliato. Email: rfogliat@andrew.cmu.edu 


