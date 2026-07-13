<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - Statistical models for the evaluation of fielding in baseball - Unknown Authors.pdf -->

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

Shane T. Jensen Kenny Shirley Abraham Wyner 

Department of Statistics, The Wharton School, University of Pennsylvania 

- 2007 New England Symposium on Statistics in Sports 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Quantifying Fielding Performance~~** 

**Overall goal** : performance of each major league baseball player Many aspects of game (eg. hitting, pitching) are easy to quantify and tabulate finite number of outcomes, baserunner configurations Fielding is a more **continuous** aspect of the game presents a greater data and modeling challenge 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Popular Fielding Evaluation Methods~~** 

**Ultimate Zone Rating** (Mitchel Lichtman): divides field into large zones and tabulates of successful vs. unsuccessful plays for each fielder within zones **Probabilistic Model of Range** (David Pinto): Field is cut into 18 pie slices (every 5 degrees) on either side of second base replacement for UZR (which now has limited availability) Both methods have similar weakness: separate zones used when field is actually a **single continuous surface** Each zone/slice is large which limits ability to detect small 

Need **higher-resolution data** for continuous models 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Baseball Info Solutions (BIS) Data~~** 

**High-resolution BIS data** available via ESPN grant 4 years (02-06) with 120000 balls-in-play (BIP) per year 42% grounders 33% flys 25% liners 

Each BIP is mapped to a **much smaller area** (4 × 4 feet) than the UZR zones **Velocity** information also but only as category 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Smooth Fielding Curves~~** 

**smooth curves** to the **continuous playing field** 



**Plus-Minus System** (John Dewan) also based on BIS data, but does not use smooth curves 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~SAFE: Spatial Aggregate Fielding Evaluation~~** 

- **1** Fit smooth curve for in each position: 

Using all players, estimate probability of success on a BIP as function of distance, direction and velocity 

- **2** Fit separate smooth curve for each 

- **3** Calculate **difference** at each point between average curve and each individual curve 

- **4** Weight difference at each point by **BIP frequency** 

- **5** Weight difference at each point by **run consequence 6 Aggregate** runs saved/cost over all points for each fielder Numerical integration over a fine grid used for aggregation 

**SAFE = (Individual - Average)** × **BIP Freq.** × **Run conseq.** 

~~<u>Our SAFE Method</u>~~ 

~~<u>Results Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

## **~~Different Ball-In-Play Types~~** 

**Two-dimensional curves** needed for : success depends on distance and direction to BIP **One-dimensional curves** needed for **grounders** : success depends on direction and angle between fielder and BIP 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Logistic function for each smooth curve~~** 

Logistic functions used to model curves for **probability** _P_ of a successful fielding play 

## **Logistic function for grounders:** 





###### 



Different β 1 used for moving **forward vs. back** 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Average model for each position~~** 

## Average model estimated by using **all players at position** . 

##### **Baseline probability of making a play for each infield position** 



<!-- Start of picture text -->
SS 2B<br>3B 1B<br>P<br>0 20 40 60 80<br>Degrees<br>1.0<br>0.8<br>0.6<br>Probability<br>0.4<br>0.2<br>0.0<br><!-- End of picture text -->

Curves centered at point with **highest success prob** . Each distance is an estimate since we don’t know exactly where fielder was standing at start of each play 

Note the different curves for moving to the left vs. right 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Individual models for Grounders~~** 

Fit different 1-D logistic curves for each . 

### **2005 Shortstop Range on Groundballs** 



<!-- Start of picture text -->
Average SS<br>Adam Everett<br>Michael Young<br>3rd Base 2nd Base<br>1.0<br>0.8<br>0.6<br>0.4<br>Probability of Success<br>0.2<br>0.0<br><!-- End of picture text -->

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Individual models for Fly Balls~~** 

Fit different 2-D logistic curves for each . 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Curve Differences~~** 

Calculate **point-by-point differences** between individual <u>felder curves and average curves at the position</u> 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Weighting by BIP Frequency~~** 

Could add up curve differences (individual - aggregate) over all points, but not all points have **same frequency** Need to **weight this tabulation** so that more frequent distances or angles are more important 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Weighting by Run Consequence~~** 

Also calculate the **run consequence** of a unsuccessful play using frequencies of each hit type at the point Weight each point by run consequence to put differences in terms of **runs saved/cost** 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Putting it all together with an example~~** 

Carl Crawford has a 0.95 **probability of making a catch** on BIPs to a particular point in CF 

The average CF has a 0.85 probability, giving Carl a **positive difference** of 0.10 

**BIP frequency** for this point is 15 balls per season, so Carl catches an extra 15 × 0 . 1 = 1 . 5 BIP to that point How many **runs** are these extra 1.5 catches worth? 

Frequency of singles, doubles and triples to this point used to calculate average **run consequence** of missed catch which is 0.65 runs per BIP for this point 

So Carl has saved 1 . 5 × 0 . 65 = 0 . 975 runs at that point Aggregating Carl’s run values across all points in CF gives the **total runs saved/cost** for Carl Crawford 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Results for Infelders: Top 10 (average run value across 02-05)~~** 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Results for Infelders: Top 10 (average run value across 02-05)~~** 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Results for Outfelders: Top 10 (average run value across 02-05)~~** 



~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Comparison of Results~~** 

Decent **overall agreement** between SAFE and UZR Overall correlation between SAFE and UZR around 0.5 No gold standard for comparison, but can examine **correlation between years** 



1B seems to be biggest problem for SAFE (even worse performance in other year-by-year comparisons) 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Summary~~** 

Higher resolution BIP data allows more detailed examination of differences between players Model-based approach: **smooth probability function** with estimated parameters for each player 

Smoothing reduces variance of results by sharing information between all points near to a fielder In contrast, UZR tabulates each zone independently 

**SAFE run value** aggregates individual differences while weighting for BIP frequency and run consequence **Year-to-year correlation** compares favorably with UZR but still has problems with some positions (eg. 1B) 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Small Sample Issues~~** 

## Small samples for some players leads to **highly variable estimates** of their smooth probability curves 

#### **2005 Centerfielder Curves** 



<!-- Start of picture text -->
Individual<br>Aggregate<br>0 50 100 150 200 250 300<br>Distance<br>1.0<br>0.8<br>0.6<br>0.4<br>Success Probability<br>0.2<br>0.0<br><!-- End of picture text -->

Can use **hierarchical model** instead of estimating each player’s curve separately 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Hierarchical Shrinkage Model~~** 

**Shares information** between parameters for each player Result is player curves are **shrunk** towards aggregate Players with small samples have curves shrunk the most 

#### **2005 Centerfielder Curves** 



<!-- Start of picture text -->
Individual<br>Shrunk<br>Aggregate<br>0 50 100 150 200 250 300<br>Distance<br>1.0<br>0.8<br>0.6<br>0.4<br>Success Probability<br>0.2<br>0.0<br><!-- End of picture text -->

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

## **~~Differences between Ballparks~~** 

Current analysis does not take into account **differences in the playing field** for different parks Could impact both evaluation of infielders (turf vs. grass) and outfielders (different outfield shapes) 



will account for differences in shape but will have higher variance (less data) 

~~<u>Our SAFE Method</u>~~ 

~~<u>Summary and Extensions</u>~~ 

~~<u>Introduction and Data</u>~~ 

~~<u>Results</u>~~ 

# **Thank you!** 

∼ **http://stat.wharton.upenn.edu/ stjensen/research/safe.html** 

**Google search: shane jensen safe** 


