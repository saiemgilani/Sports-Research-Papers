<!-- source: Estimating locomotor demands during team play from broadcast-derived tracking data.pdf -->

# Estimating locomotor demands during team play from broadcast-derived tracking data 

Jacob Mortensen, Luke Bornn 

January 22, 2020 

#### **Abstract** 

The introduction of optical tracking data across sports has given rise to the ability to dissect athletic performance at a level unfathomable a decade ago. One specific area that has seen substantial benefit is sports science, as high resolution coordinate data permits sports scientists to have to-the-second estimates of external load metrics, such as acceleration load and high speed running distance, traditionally used to understand the physical toll a game takes on an athlete. Unfortunately, collecting this data requires installation of expensive hardware and paying costly licensing fees to data providers, restricting its availability. Algorithms have been developed that allow a traditional broadcast feed to be converted to x-y coordinate data, making tracking data easier to acquire, but coordinates are available for an athlete only when that player is within the camera frame. Obviously, this leads to inaccuracies in player load estimates, limiting the usefulness of this data for sports scientists. In this research, we develop models that predict offscreen load metrics and demonstrate the viability of broadcast-derived tracking data for understanding external load in soccer. 

## **1 Introduction** 

In order to reduce fatigue, prevent injury, and improve performance, sports scientists seek to monitor the physical impact that participation in training and competition has on an athlete. A number of different metrics, broadly referred to as load metrics, have been used to try and quantify the intensity of a given activity for an athlete. These metrics consist of two general categories: internal and external. Halson (2014) defines internal load as “the relative physiological and psychological stress imposed” on an athlete. Internal load measures are not treated in this work and we make no further note of them other than to 

1 

mention that they exist and include, for example, individual reporting of perceived exertion, heart-rate-derived training impulse, and summated-heart-rate-zones (Borresen and Lambert, 2008; McLaren et al., 2018). External load is defined as “the work completed by the athlete, measured independently of his or her internal characteristics” (Halson, 2014). Metrics in this category include distance measures (both total distance over a training session or match and distance traveled stratified by intensity of the activity) (Coutts and Duffield, 2010; Rampinini et al., 2009; Dalen et al., 2016; McLaren et al., 2018) and acceleration-derived measures (Dalen et al., 2016; Delaney et al., 2016; McLaren et al., 2018; Nicolella et al., 2018; Boyd et al., 2011). Existing methods for accurately capturing external load metrics consist of an athlete wearing a device, whether that be a global positioning system (GPS) (Sykes et al., 2013; Mullen et al., 2019) or local positioning system (LPS) tracker (V´azquez-Guerrero et al., 2019), or an accelerometer (Boyd et al., 2011), which can give accurate readings of instantaneous velocity and acceleration. However, it is not always possible for an athlete to wear such a device, and so optical tracking data has been used as an alternative means to capture measures of external load (Gregson et al., 2010). 

Since its initial introduction in soccer by Prozone in 1999 (Medeiros, 2017), multicamera optical tracking data has spread across a variety of sports, providing detailed location data for players multiple times per second. The prevalance of this data allows sports analysts to move beyond the limitations of box score statistics, capturing tactics, strategy, and nuance in a manner that is impossible with the simple enumeration of discrete events. This type of data allows analysts to move from simply noting when an assist occurred to answering questions like: “where were the assisting players teammates when the assist occurred?”, “what type of defensive pressure was the assist made under?”, and “what types of actions increase the likelihood of an assisted goal?” The value of this data is shown clearly by Cervone et al. (2016), who introduced the idea of expected possession value (EPV) by using tracking data from the National Basketball Association to show how the value of a possession evolves over time, accounting for contextual information like which players were on the court, where they were located, and potential actions. This EPV framework was later extended to soccer by Fern´andez et al. (2019), who were able to use it to show, as just one example, where space was being created on the pitch and how space creation increased or decreased the value of a possession. 

Tracking data is useful for sports scientists because it allows them to derive metrics related to distance, speed and acceleration that serve as a proxy for the stress placed on a player’s body as a result of their athletic performance. Because the equipment to produce this data is fixed in the arena and not hampered by either league rules or player cooperativeness, this results in a much more expansive sample of player load than is possible via wearable devices. 

2 

However, despite the distinct advantages provided by multicamera optical tracking data two extant issues remain: exclusivity and sparsity. This data is exclusive because obtaining it requires installation of expensive hardware and paying large licensing fees, restricting its availability to only the most elite leagues. The data is sparse in the sense that it has become widespread only in recent years, preventing historical comparison. As a result, any ability to draw conclusions about load metrics and their relationship to health outcomes is limited. Broadcast-derived tracking data has the capacity to overcome both of these problems because it allows coordinates to be extracted from regular broadcast video using computer vision techniques (Lu et al., 2013). This eliminates the need to install special cameras and has the potential to provide x-y coordinate data for any game with a video feed. 

Despite its exciting possibility, broadcast-derived tracking data comes with one glaring issue: coordinate data is only available for a player as long as they are within the camera frame. Our purpose in this paper is to assess the viability of broadcast-derived tracking data for estimation of a variety of external load metrics commonly used across sports. Specifically, our focus is on estimating load metrics during the time that a given player is offscreen. We do this by using games for which complete multicamera tracking data is available, and manually censoring observations to emulate the broadcast-derived tracking data. Approaching the problem in this way allows us to establish a ground truth, answering definitively, given that the broadcast tracks are accurate, whether or not broadcast-derived tracking data can be used to assess external load. 

## **2 Methods** 

### **2.1 Data** 

Our data comes from 18 of the 19 home games played by Chelsea FC in the 2014-15 English Premier League and includes information for 248 players (this number does not include goalkeepers, which are excluded from our analysis). The data contains complete x-y coordinate data for all players in each game at a frequency of 10 measurements per second, providing a continuous track for a player for the entire time he was in the game, with a break at match halftime. Additionally, the data includes event information, which consists of the location and description of actions such as a touch, pass or tackle. In order to emulate the broadcast derived tracking data while retaining true offscreen values, we simulate a camera track by linearly interpolating between event locations and place a 40 _×_ 40 meter window centered on the camera track. Player locations outside of the window are treated as unobserved, and metrics calculated from these censored tracks are the values we predict in this paper. Each 

3 

time the track transverses the edge of the camera window, we split the multicamera track into a new segment, which we refer to as a subtrack, and assign it a unique ID. This process results in 149,680 subtracks generated from an original 820 tracks, giving an average of 8315.6 (+/- 411.9) subtracks per game from a median of 45.5 (range=44-47) original player tracks per game. The median subtrack length is 17.0 m (range=0.0-830.1 m) with a median time of 8.1 s (range=0.1-556.7 s). Subtrack information is augmented by player position information scraped from transfermarkt.com, with each player classified as either a defender (n = 85), midfielder (n = 85), or forward (n = 78). 

In order to make predictions a variety of features were constructed from the tracks, at both the subtrack level and aggregated to the game level. For each subtrack, we record the x and y location for where the player left and re-entered the camera window and calculate the Euclidean distance and time elapsed between them. Distance, velocity, and acceleration are calculated for each 0.1 second interval, and used to calculate the load metrics detailed below as well as average velocity and average absolute acceleration in the 2 second intervals preceding and following each subtrack. The raw accelerations exhibit some unrealistic values, with some instantaneous accelerations greater than 50 m _/_ s<sup>_−_2</sup> , so in order to reduce this noise, we smooth the accelerations using a Nadaraya-Watson kernel smoother (Nadaraya, 1964; Watson, 1964). At the game level, most of the features consist of the load metrics calculated for the observed portion of the game, but we also calculate the total time in seconds that a player was censored, percent of playing time a given player was censored, and their average observed velocity. 

### **2.2 Player load metrics** 

The suite of external load metrics we consider in this work were selected because of their use throughout the literature (see, for example, Varley and Aughey (2013); Gabbett and Ullah (2012); Dwyer and Gabbett (2012); Johnston et al. (2014); Dalen et al. (2016); Borresen and Lambert (2008); McLaren et al. (2018)). Because specific definitions of load metrics vary wildly throughout the literature, we provide definitions for the metrics we use in Table 1. Note that although we are only making predictions for the eight load metrics outlined in Table 1 that they fall into the three broad categories of distance, velocity, and acceleration derived measures. In general, any external load metric that falls into one of these categories can be calculated from broadcast-derived tracking data, though prediction accuracy for specific censored metrics should be assessed individually. 

Exploratory analysis of this data and the calculated metrics reveals two patterns worth highlighting. The first is that there is a very strong correlation between the amount of 

4 

censored playing time in a game and most of the censored load metrics, as shown in Figure 1 for total acceleration. When keepers are removed from the data, the values for Pearson’s correlation coefficient between elapsed time for a censored subtrack and most of the other metrics range between 0.596 and 0.998, the exceptions being peak velocity and acceleration density. This suggests that in many cases fairly good estimates can be obtained by simply regressing the metric on censored subtrack time. The second pattern becomes clear if we assume that the censored data is missing completely at random (MCAR) (Rubin, 1974); that is, we assume that there is no relationship between the pattern of missingness and the values of the observed and censored load metrics. To illustrate, consider total distance (though the following relationship holds for the other player metrics). Under this assumption, the ratio of observed distance, _Do_ , to censored distance, _Dc_ is equivalent to the ratio between observed time, _To_ , and censored time _Tc_ , or in mathematical notation, 



This in turn implies that we can estimate _Dc_ by setting _Dc_ = _Do TToc_<sup>.Becausewearesimply</sup> scaling the observed metric value by the ratio of censored to observed time, we refer to this as a scaling estimator. Despite its appealing simplicity, examination of the residuals, shown for four of the metrics in Figure 2, reveals that the assumption that data is MCAR is incorrect. We see that residuals become increasingly negative (censored values are overestimated) as the amount of censoring increases for most of the metrics, with the exception being the amount of time spent in the slowest velocity band. The systematic differences between player movement on- and off-camera demonstrated in these plots can be summarized simply as “players move faster when on camera.” 

### **2.3 Models** 

In order to establish a baseline level of comparison, we use a linear regression model for each load metric of the form 



where _i_ indexes the player-match combination, _yi_ is the value of the censored metric at the game level, _Ti_ is the amount of censored time for the game, _xi_ is the value of the observed metric at the game level, and _ϵ_ is a normally distributed error term. The remaining models that we compare are all fit using gradient boosting (Friedman, 2001) as implemented by the `xgboost` package (Chen and Guestrin, 2016) within the statistical programming language `R` (R Core Team, 2019). Gradient boosting is an ideal tool for this application for several 

5 

Table 1: External load metric 

|Category|Metric|Defnition|
|---|---|---|
|Distance|Total distance|Sum of the distance travelled by<br>an athlete.|
||High speed distance|Sum of the distance travelled by<br>an athlete with speed between 3.5<br>and 5.7 m/s.|
||Very high speed distance|Sum of the distance travelled by<br>an athlete with speed greater than<br>5.7 m/s.|
|Velocity|Time spent in velocity band [_x, y_)|Number of seconds spent with ve-<br>locity (_m/s_), _v_, in the interval<br>_x ≤v < y_. Intervals considered<br>are [0_,_3_._5), [3_._5_,_5_._7), and [5_._7_, ∞_),<br>based on the work of Dwyer and<br>Gabbett (2012).|
||Peak _x_-second velocity|Max velocity of average velocities<br>calculated over _x_ = 1_,_3_,_5_,_ and 10<br>second rolling windows.|
|Acceleration|Total Acceleration<br>Acceleration density<br>Time spent in acceleration band [_x, y_)|Sum of the absolute values of ac-<br>celeration at 0.1 second intervals.<br>Mean acceleration.<br>Number of seconds spent with ac-<br>celeration (_m/s_<sup>2</sup>), _a_, in the inter-<br>val _x ≤a < y_. Intervals consid-<br>ered are [0_._65_,_1_._46), [1_._46_,_2_._77),<br>and [2_._77_, ∞_), based on the work<br>of Johnston et al. (2014)|



6 



<!-- Start of picture text -->
Censored Time vs. Censored Acceleration<br>G<br>4000030000 GGGGGGGG G GG G G G GG G G GGG GG GG GG G G G GG GGGGG G G GG GGG GG G G GG GG G G GGGGG GG G G GG G G GGGGGGGG G GGGGGGGGG G G GGGG G G GGGG G GGGGGG G G G GGGGGGGGGGGGGGGGGGGGGG G G G G GG G PositionG defender<br>G midfield<br>20000 G G<br>G G forward<br>G<br>keeper<br>G<br>G<br>10000 G G<br>G G<br>GG GG<br>0 GGG<br>0 2000 4000<br>Censored Time (s)<br>)<br>2<br>s<br>m<br>Censored Acceleration (<br><!-- End of picture text -->

Figure 1: Censored time versus censored total acceleration. Note that once keepers are removed from the data, the relationship between censored time and censored total acceleration is almost exactly linear. 

7 

#### Scaled Estimator Residuals vs. Percent of Censored Data 



<!-- Start of picture text -->
Total Distance Total Acceleration<br>0 G G G<br>0 G G G G G G G G G G G G G G G G G G G G GG GG<br>−1000−500 G G G G G G G G G GG G GGGGGGG G G G −5000 G G G G G G GG G GGGGG G G G G G GG G G<br>G G −10000 GG G G<br>−1500 G G GG G G G G<br>G<br>G<br>−2000 G −15000 G<br>G Position<br>0.2 0.4 0.6 0.2 0.4 0.6 G defender<br>Time in Velocity Band [3.5, 5.7) Time in Velocity Band [0, 3.5) midfield<br>forward<br>G<br>0 G G G 400 G G<br>G G GGG G G G GGG GGG 300 G GGGG<br>−100 G GG G G G G G G<br>G G GGGGGGGGGGGGGG G 200 GG GGG G GGG G G G G<br>−200 G GGG 100 G G G GG G GG G<br>G G G G G G GG<br>G G GG<br>−300 G 0 G G<br>0.2 0.4 0.6 0.2 0.4 0.6<br>Percent Censored<br>y<br> −<br>y<br><!-- End of picture text -->

Figure 2: Residuals for the scaling estimator in Section 2.2 versus the percentage of data that is censored. The scaling estimator consistently underestimates the amount of time spent in the slowest velocity band, whereas it consistently overestimates values for the other load metrics, resulting in negative residuals. This is clear evidence that the way players move on camera differs systematically from how they move offscreen. 

8 

reasons: it fits a model, then iterates, fitting a model on the residuals of each previous model until no further improvements can be made, then averages all of the models together, yielding very accurate predictions; it is flexible because it allows the use of both linear and nonlinear (tree-based) boosters; and it has the convenient feature of performing automatic variable selection, permitting us to take a “kitchen-sink” approach and include all potential predictors for consideration in the model. Additionally, as implemented in `xgboost` it is extremely fast, allowing models to be fit to a large amount of data in just a short span of time. 

We compare two different approaches to obtaining game level estimates: predicting the values for each subtrack individually and then aggregating them to the game level versus predicting game level metrics directly. We combine these two levels of estimation with three different models: a linear model with no interactions, a linear model that considers all twoway interactions, and a random forest model. We train each model on the first thirteen games of the season, reserving the final five games for testing, which results in 361 playermatch observations in the training set and 138 player-match observations in the test set. We assess model performance by comparing root mean square predictive error (RMSPE), defined RMSPE = ~~�~~ <u>�(</u> _yi − y_ ˆ _i_ )2 _/n_ , where _y_ ˆ _i_ is the predicted value for observation _yi_ and _n_ is the number of observations, and the coefficient of variation (CV), defined CV = _RMSPE/y_ ¯, where _y_ ¯ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_yi/n_.InthiscontextCVisusefulbecauseittellsushowlargetheerrors</sup> are relative to the values themselves, giving an indication of how much the overall variance in the data was reduced by the given model. 

The predictors included in the various models are denoted in Table 2. All numeric variables were centered and scaled so that they have a mean of 0 and standard deviation of 1, which, for the linear models, allows us to determine relative significance of each predictor in the model simply by comparing the size of their associated coefficients. 

Here we briefly note that 100% of the peak _x_ -second velocity values in the 18 games in our data set occur within the camera window, and as such, there is no need to try and estimate these values for the censored tracks. While it may not always be the case that peak velocities are always observed, this suggests that any exceptions will be rare, and so peak velocity is omitted from the subsequent analysis. 

## **3 Results** 

The full results for each of the predicted metrics at the subtrack and game levels are shown in Tables 3 and 4, respectively. In all cases, estimating the player metrics at the subtrack level and then aggregating to obtain game level estimates outperforms making predictions 

9 

Table 2: Model predictors. Inclusion for consideration in subtrack or game level models is indicated by the x. All variables that begin with “observed” are measured at the game level, so an x in the subtrack model column for “observed total acceleration” means that the sum of the absolute value of accelerations for the entire game is used as a predictor when estimating individual subtrack outcomes. 

|Predictor<br>Included at subtrack level|Included at game level|
|---|---|
|player position<br>x|x|
|ofscreen time<br>x||
|censored total time|x|
|ofscreen distance<br>x||
|observed total distance|x|
|average velocity in previous two seconds<br>x||
|average velocity in following two seconds<br>x||
|average absolute acceleration in previous two seconds<br>x||
|average absolute acceleration in following two seconds<br>x||
|observed average acceleration<br>x|x|
|observed total acceleration<br>x|x|
|observed average velocity<br>x|x|
|observed high speed distance<br>x|x|
|observed very high speed distance<br>x|x|
|observed time in velocity band [0_,_3_._5)<br>x|x|
|observed time in velocity band [3_._5_,_5_._7)<br>x|x|
|observed time in velocity band [5_._7_, ∞_)<br>x|x|
|observed time in acceleration band [0_._65_,_1_._46)<br>x|x|
|observed time in acceleration band [1_._46_,_2_._77)<br>x|x|
|observed time in acceleration band [2_._77_, ∞_)<br>x|x|



10 

purely at the game level, as seen in the lower RMSPE and CV values. For seven of the eleven player load metrics under consideration, the linear model with interactions performs the best, though the random forest has the lowest RMSPE and CV in three cases. Predicting acceleration density is the only case where the linear model with no interactions results in the best predictions. 

CV values are less than or equal to 0.10 for six of the eleven models, indicating a significant reduction in standard error relative to the overall size of the response. The largest CV is 0.31, for both very high speed distance and time in velocity band [5 _._ 7 _, ∞_ ), both outcomes for which the nonlinear model performs the best. This result can be explained when we consider that the correlations of these two metrics with censored total time are 0.599 and 0.605, respectively, indicating that these predictions do not benefit from the very strong relationship with censored total time that the other metrics do. Considering the RMSPE values themselves helps us understand just how well each metric is being predicted. For example, despite its CV of 0.31, the RMSPE for time in velocity band [5 _._ 7 _, ∞_ ) is still only 6.4 seconds. The RMSPE for total distance is 183 meters, minimal error considering players on average travel 3524 meters in each game. 

An examination of the residuals for a given response variable against the percent of data that is censored, shown for total distance in Figure 3, is illuminating. Unsurprisingly, we see that the variability in the predictions increases with the amount of censored data, but in general the predictions appear unbiased, and even when as much as 50% of the data is missing, the range of the residuals being approximately (-500, 500) indicates a significant reduction in variability when compared to the empirical standard deviation for the response of 1506 meters. Figure 3 also shows a clear demarcation in the amount of censoring across the various positions, with defenders experiencing the most time off camera and midfielders spending the most time within the camera frame. 

Due to the nature of gradient boosting, our ability to make inference is limited, but we can get a sense of the impact of certain predictors by taking the top five covariates with either the greatest importance (for the random forest) or largest coefficients<sup>1</sup> (for the linear models) for each model and tallying how frequently each is included. Offscreen time is included as the first or second most significant variable in the models for all eleven load metrics, a fact foreshadowed by the strong correlation noted in Section 2.2. Offscreen distance and position are both top variables in eight of the eleven models, while the velocity and acceleration entering and leaving the camera window are in the top five for four of the models, primarily the distance metrics. All remaining predictors occur in the top five for just three or fewer of the load metrics. 

> 1Recall that all variables were centered and scaled, making this a valid comparison. 

11 



<!-- Start of picture text -->
Residuals for Total Distance vs. Percent of Censored Data<br>500<br>250<br>Position<br>defender<br>0<br>midfield<br>forward<br>−250<br>−500<br>0.2 0.4 0.6<br>Percent Censored<br>y<br> −<br>y<br><!-- End of picture text -->

Figure 3: Residuals for total distance predictions versus percent of total data that is censored. 

12 

## **4 Practical Applications** 

Broadcast-derived tracking data has tremendous potential and in this work we have demonstrated its viability for use when evaluating player load in soccer. Because we used out-ofthe-box statistical methods with no modification, this type of modeling is widely accessible and should be relatively easy to adopt in practice. Examination of RMSPE and CV values shows that in general, predictions for the various load metrics are very accurate. Some of the stratified metrics, i.e., time in velocity band [5 _._ 7 _, ∞_ ) and very high speed distance, have larger CV values due to the small amount of time players spend in these states, but the RMSPE in these cases is still low enough for use in a practical setting. One consideration when applying our results is how estimate accuracy varies by position and across players. For example, when considering total distance, the RMSPE for defenders, midfielders, and forwards is 216, 164, and 160, respectively. This is driven primarily by differences in censoring rates, with forwards and midfielders being censored just 43.4 and 35.4 percent of the time, versus 52.5 percent of the time for defenders. Censoring rates also vary significantly from player to player, ranging from 19.7 to 60.04 percent of data censored. Accounting for differences in censoring can increase prediction accuracy and improve the efficacy of using broadcast-derived tracking data for external load metric estimation in soccer. 

13 

Table 3: RMSPE and CV for the base model and subtrack level models on each of the responses 

||**Base m**|**odel**|**Linear m**|**odel**|**Linear mod**|**el w/ int**|**Random **|**forest**|
|---|---|---|---|---|---|---|---|---|
||RMSPE|CV|RMSPE|CV|RMSPE|CV|RMSPE|CV|
|total distance (m)|288.2|0.08|202.0|0.06|188.3|0.05|**183.0**|**0.05**|
|high speed distance (m)|164.5|0.22|113.8|0.15|**106.0**|**0.14**|113.4|0.15|
|very high speed distance (m)|60.4|0.44|53.4|0.39|53.3|0.39|**42.8**|**0.31**|
|time in velocity band [0_,_3_._5) (s)|49.9|0.03|30.4|0.02|**29.1**|**0.02**|29.8|0.02|
|time in velocity band [3_._5_,_5_._7) (s)|37.8|0.22|26.4|0.15|**24.5**|**0.14**|26.4|0.15|
|time in velocity band [5_._7_, ∞_) (s)|8.8|0.43|7.9|0.38|7.9|0.38|**6.4**|**0.31**|
|total acceleration (_m/s_<sup>2</sup>)|2473|0.11|1448|0.07|**1365**|**0.06**|1366|0.06|
|acceleration density (_m/s_<sup>2</sup>)|0.140|0.12|**0.113**|**0.10**|0.129|0.11|0.119|0.11|
|time in acceleration band [0_._65_,_1_._46) (s)|34.9|0.06|25.8|0.05|**25.7**|**0.05**|29.5|0.05|
|time in acceleration band [1_._46_,_2_._77) (s)|45.3|0.13|30.6|0.09|**27.8**|**0.08**|29.5|0.05|
|time in acceleration band [2_._77_, ∞_) (s)|36.5|0.22|21.5|0.13|**20.9**|**0.13**|22.3|0.13|



Table 4: RMSPE and CV for the base model and game level models on each of the responses 

||**Base m**|**odel**|**Linear m**|**odel**|**Linear mod**|**el w/ int**|**Random **|**forest**|
|---|---|---|---|---|---|---|---|---|
||RMSPE|CV|RMSPE|CV|RMSPE|CV|RMSPE|CV|
|total distance (m)|288.2|0.08|257.0|0.08|267.1|0.08|286.5|0.08|
|high speed distance (m)|164.5|0.22|150.6|0.20|153.1|0.21|159.1|0.21|
|very high speed distance (m)|60.4|0.44|60.4|0.44|61.7|0.45|68.1|0.50|
|time in velocity band [0_,_3_._5) (s)|49.9|0.03|41.4|0.02|42.0|0.02|60.3|0.03|
|time in velocity band [3_._5_,_5_._7) (s)|37.8|0.22|34.8|0.20|35.2|0.20|37.5|0.22|
|time in velocity band [5_._7_, ∞_) (s)|8.8|0.43|9.0|0.43|9.1|0.44|9.91|0.48|
|total acceleration (_m/s_<sup>2</sup>)|2473|0.11|1748|0.08|1658|0.08|2227|0.10|
|acceleration density (_m/s_<sup>2</sup>)|0.140|0.12|0.126|0.11|0.140|0.12|0.156|0.14|
|time in acceleration band [0_._65_,_1_._46) (s)|34.9|0.06|25.7|0.05|27.4|0.05|38.1|0.07|
|time in acceleration band [1_._46_,_2_._77) (s)|45.3|0.13|32.3|0.09|31.7|0.09|40.4|0.12|
|time in acceleration band [2_._77_, ∞_) (s)|36.5|0.22|26.7|0.16|25.3|0.15|29.2|0.17|



## **References** 

- Borresen, J. and Lambert, M. I. (2008). Quantifying training load: A comparison of subjective and objective methods. _International Journal of Sports Physiology and Performance_ , 3(1):16–30. 

- Boyd, L. J., Ball, K., and Aughey, R. J. (2011). The reliability of minimaxx accelerometers for measuring physical activity in australian football. _International Journal of Sports Physiology and Performance_ , 6(3):311–321. 

- Cervone, D., D’Amour, A., Bornn, L., and Goldsberry, K. (2016). A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes. _Journal of the American Statistical Association_ , 111(514):585–599. 

- Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , volume KDD ’16, pages 785–794, San Francisco, California, USA. 

- Coutts, A. J. and Duffield, R. (2010). Validity and reliability of GPS devices for measuring movement demands of team sports. _Journal of Science and Medicine in Sport_ , 13(1):133– 135. 

- Dalen, T., Jorgen, I., Gertjan, E., Havard, H. G., and Ulrik, W. (2016). Player load, acceleration, and deceleration during forty-five competitive matches of elite soccer. _Journal of Strength and Conditioning Research_ , 30(2):351–359. 

- Delaney, J. A., Duthie, G. M., Thornton, H. R., Scott, T. J., Gay, D., and Dascombe, B. J. (2016). Acceleration-based running intensities of professional rugby league match play. _International Journal of Sports Physiology and Performance_ , 11(6):802–809. 

- Dwyer, D. B. and Gabbett, T. J. (2012). Global positioning system data analysis: Velocity ranges and a new definition of sprinting for field sport athletes. _Journal of Strength and Conditioning Research_ , 26(3):818–824. 

- Fern´andez, J., Bornn, L., and Cervone, D. (2019). Decomposing the Immeasurable Sport : A deep learning expected possession value framework for soccer. In _Sloan Sports Analytics Conference_ , pages 1–20. 

- Friedman, J. (2001). Greedy Function Approximation : A Gradient Boosting Machine. _The Annals of Statistics_ , 29(5):1189–1232. 

16 

- Gabbett, T. J. and Ullah, S. (2012). Relationship between running loads and soft-tissue injury in elite team sport athletes. _Journal of Strength and Conditioning Research_ , 26(4):953–960. 

- Gregson, W., Drust, B., Atkinson, G., and Salvo, V. D. (2010). Match-to-match variability of high-speed activities in premier league soccer. _International Journal of Sports Medicine_ , 31(4):237–242. 

- Halson, S. L. (2014). Monitoring Training Load to Understand Fatigue in Athletes. _Sports Medicine_ , 44:139–147. 

- Johnston, R., Watsford, M., Pine, M., and Spurrs, R. (2014). Standardisation of acceleration zones in professional field sport athletes. _International Journal of Sports Science and Coaching_ , 9(5):1161–1168. 

- Lu, W. L., Ting, J. A., Little, J. J., and Murphy, K. P. (2013). Learning to track and identify players from broadcast sports videos. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 35(7):1704–1716. 

- McLaren, S. J., Macpherson, T. W., Coutts, A. J., Hurst, C., Spears, I. R., and Weston, M. (2018). The Relationships Between Internal and External Measures of Training Load and Intensity in Team Sports: A Meta-Analysis. _Sports Medicine_ , 48(3):641–658. 

- Medeiros, J. (2017). How data analytics killed the Premier League’s long ball game. 

- Mullen, T., Twist, C., and Highton, J. (2019). Stochastic ordering of simulated rugby match activity produces reliable movements and associated measures of subjective task load, cognitive and neuromuscular function. _Journal of Sports Sciences_ , 37(21):1–7. 

- Nadaraya, E. (1964). On Estimating Regression. _Theory of Probability and Its Applications_ , 9(1):141–142. 

- Nicolella, D. P., Torres-Ronda, L., Saylor, K. J., and Schelling, X. (2018). Validity and reliability of an accelerometer-based player tracking device. _PLOS ONE_ , 13(2):1–13. 

- R Core Team (2019). _R: A Language and Environment for Statistical Computing_ . R Foundation for Statistical Computing, Vienna, Austria. 

- Rampinini, E., Impellizzeri, F. M., Castagna, C., Coutts, A. J., and Wisløff, U. (2009). Technical performance during soccer matches of the Italian Serie A league: Effect of fatigue and competitive level. _Journal of Science and Medicine in Sport_ , 12(1):227–233. 

17 

- Rubin, D. B. (1974). Characterizing the estimation of parameters in incomplete-data problems. _Journal of the American Statistical Association_ , 69(346):467–474. 

- Sykes, D., Nicholas, C., Lamb, K., and Twist, C. (2013). An evaluation of the external validity and reliability of a rugby league match simulation protocol. _Journal of Sports Sciences_ , 31(1):48–57. 

- Varley, M. C. and Aughey, R. J. (2013). Acceleration profiles in elite Australian soccer. _International Journal of Sports Medicine_ , 34:34–39. 

- V´azquez-Guerrero, J., Jones, B., Fern´andez-Vald´es, B., Moras, G., Reche, X., and Sampaio, J. (2019). Physical demands of elite basketball during an official U18 international tournament. _Journal of Sports Sciences_ , 37(22):1–8. 

- Watson, G. (1964). Smooth Regression Analysis. _Sankhy: The Indian Journal of Statistics; Series A_ , 26(4):359–372. 

18 


