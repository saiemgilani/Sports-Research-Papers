<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2014/2014 - A Data-driven Method for In-game Decision Making in MLB - Unknown Authors.pdf -->



# **A Data-driven Method for In-game Decision Making in MLB** 

Gartheeban Ganeshapillai, John Guttag Massachusetts Institute of Technology Cambridge, MA, USA 02139 Email: garthee@mit.edu 

## **Abstract** 

In this paper we show how machine learning can be applied to generate a model that could lead to better on-field decisions by predicting a pitcher’s performance in the next inning. Specifically we show how to use regularized linear regression to learn pitcher-specific predictive models that can be used to estimate whether a starting pitcher will surrender a run if allowed to start the next inning. 

For each season we trained on the first 80% of the games, and tested on the rest. The results suggest that using our model would frequently lead to different decisions late in games than those made by major league managers. There is no way to evaluate would have happened when a manager lifted a pitcher that our model would have allowed to continue. From the 5<sup>th</sup> inning on in close games, for those games in which a manager left a pitcher in that our model would have removed, the pitcher ended up surrendering at least one run in that inning 60% (compared to 43% overall) of the time. 

## **1   Introduction** 

Perhaps the most important in-game decision a baseball manager makes is when to relieve a starting pitcher [2]. Today, managers rely on various heuristics (e.g., pitch count) to decide when a starting pitcher should be relieved [2, 17]. In this paper, we use machine learning to derive a model that can be used to assist in making these decisions in a principled way. 

Pitchers are divided into two categories, starters (the first pitcher for each team) and relievers (all subsequent pitchers). Starters rarely pitch the complete game, and deciding when to replace the starter is often the most important in-game decision that a manager has to make. Early in the game the decision is based upon many factors, including the effectiveness of the starter and the manager’s desire to conserve the bullpen. Later in the game, the decision is based primarily on the manager’s estimate of the relative expected effectiveness of the starter and the pitcher (or pitchers) who would replace him. Our work is designed to provide useful information in the second half of close games. 

We pose the problem as a classification problem of predicting whether the team would give up at least one run if the starting pitcher is allowed to start the next inning. (This formulation seems appropriate late in close games, but is not the right formulation early in a game or during a blowout.) Our method uses information about the past innings’ at-bats, the game situation, and historical data. 

First, we reformulate our problem into a regression problem using Pitcher’s Total Bases (PTB) [9] (defined later) as the dependent variable. We use PTB rather than the more obvious runs allowed, because we believe that PTB is a better indicator of pitcher effectiveness. We solve the regression problem using regularized least squares to produce a pitcher-specific predictor for the expected PTB in the next inning. We then binarize the outputs of the regression, and find a pitcher specific cut-off on the estimated PTB to maximize the prediction accuracy of a validation set. 

We evaluate our method on the MLB 2006-2010 data set from STATS LLC., which contains a record of each pitch thrown in MLB games in both the regular and post seasons. We train our model using the first 80% of the games of each season and test it on the last 20%. We also look at how our method, applied to MLB 2013 data from MLB.com, fared in the 2013 post-season. We evaluate our model relative to what actually occurred in the games in the test set. First, we learned a model, called the manager model, which closely reflects the actual decisions made by MLB managers. It is well known that managers rely heavily on pitch count and the opposing team’s scoring to determine when to relieve the starting pitcher [2, 17, 12]. Our manager model learns pitcher-specific parameters that fit these two variables against the manager’s decisions on the training data. For the 76 pitchers who pitched at least 500 pitches in each year, our manager model accurately models the manager’s decision for 95%(±1.2%) of the 



2014 Research Paper Competition Presented by: 



<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->



innings, i.e., it is a reasonably accurate model of what major league managers actually do. When the manager model is used to predict whether or not a run will be scored if the starter remains in the game, it correctly predicts 75%(±4.6%) of the innings. In contrast, our model makes a correct prediction for 81%(±4.9%) of the innings. Our model also outperforms the manager model in F-score (0.41 vs. 0.26) and odds ratio (3.2 vs. 1.2). Here, F-score is the harmonic mean of precision and recall. Odds ratio is the odds of an inning with runs among the innings that are predicted to have runs versus the odds of an inning with runs among all the innings. 

We demonstrate that applying our model would have led to a different decision 48% of the time from the fifth inning on in close games. There is no way to evaluate would have happened when a manager lifted a pitcher that our model would have allowed to continue. For those close game situations in which a manager actually left a pitcher in that the model would have removed, 60% of the time the pitcher surrendered a run. 

## **2   Related Work** 

Baseball was one of the first sports to attract statistical analysis. As a sport, it has all the necessary characteristics for performing quantitative analyses: a rich dataset with detailed records for several decades, ordered game progression that allows activity to be nicely segmented, and a reasonable amount of independence between events. This has led to the development of many statistical methods for assessing individual baseball players over the years [14, 1, 11, 3]. 

Bill James used statistical data in the 1980s to analyze why teams win and lose. He termed his approach sabermetrics. In an effort to quantify the contribution of players to wins and losses he invented many statistical measures such as runs created, Component ERA, and similarity scores [16]. 

Baseball Prospectus, published by Gary Huckabay from 1996, uses a system called Vladimir to predict a player’s performance in the next season using the context of the player’s statistics such as the venue in which the game is played. It projects how the performance evolves as a player ages [8, 15]. In 2003, Nate Silver published a system, PECOTA, for forecasting MLB player performance. It is a nearest neighbor based similarity metric that searches through thousands of players to find the ones with similar profiles. It computes the odds of a drafted player having a successful future [14]. It extended the method used to compute the statistical similarity between any two majorleague players published in Baseball Abstract by Bill James in 1986 [10]. Since then there have been many commercial systems developed to model the progression of players [1, 11, 3, 13, 15]. 

Other than [6], which described a method for predicting the next type of pitch, almost all of the existing baseball statistical methods address high level problems that span multiple games: projecting a player’s performance over the years, evaluating a player’s contributions to the wins and losses, and optimizing a team budget. In contrast, we present a machine learning method to assist in decision making during a game. 

## **3   Method** 

We first build a pitcher-specific predictor for the PTB in the next inning. We then use this prediction to build a classifier that predicts whether a run will be surrendered in the next inning. 

### **3.1   Features** 

The independent variable _x_ of our model incorporates the groups of information available to a manager at the time a decision has to be made. The inset on the right describes the features used by the model. 

### **3.1.1   Categorical Variables** 

Many of the important predictors that provide contextual information such as the next batter, the venue in which the game is played, etc., are categorical variables. We convert these categorical variables into continuous variables by deriving associations between these variables and various 

#### **Feature Vector** 

##### **Current game statistics:** 

   - Batting team score 

   - Pitching team score 

- Outs, Inning number, and Pitch count 

- **Previous inning statistics (averages):** 

   - Strikes, Balls (intentional balls discounted) 

   - Bases advanced, Home runs, Hits in play 

   - Walks (intentional walks discounted) 

   - Steals, Strike outs 

   - Pitch velocity & Pitch Zone (binned histogram) 

##### **Priors:** 

- Pitcher-Inning (Count, SLG, ERC, Runs, Hits) 

- • Pitcher-Batting team (Count, SLG, ERC, Runs, Hits) 

- Pitcher-Venue (Count, SLG, ERC, Runs, Hits) 

- Pitcher-Defense (Count, SLG, ERC, Runs, Hits) 

- Pitcher-Batter1,2,3 (Count, SLG, ERC, Runs, Hits) 

- Batter1,2,3 (SLG, ERC, Runs, Hits) 



2014 Research Paper Competition Presented by: 



<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->



statistics in the historical data. For example, the batting team is represented by prior statistics such as the average number of hits against the current pitcher. We call these statistical associations _priors_ . In those cases where the amount of data available to derive an association is small, we shrink the prior using global averages to prevent overfitting. 

Our predictors incorporate information about the batting team, game statistics, and the context of the game statistics. For instance, the pitcher-venue prior implicitly captures information about the dimensions of the stadium where the game is played. Such information can provide critical predictive information for some pitchers and batters. For example, in 2012, the Boston Red Sox pitcher Felix Doubront’s ERA was almost a full run higher in Fenway Park than elsewhere. 

### **3.1.2   Shrinkage** 

Sometimes, these priors may be unreliable because of small support. A particular pitcher might not have faced a particular batter, or thrown only a few pitches to that batter. In such cases, the prior statistics may not be meaningful. We improve the utility of values with low support by shrinking them towards the global average [4]. 

### **3.1.3   Luck and Randomness** 

When choosing the predictors, we try to minimize the influence of luck, and focus on variables that are less erratic and capture the actual performance. For instance, we use slugging percentage to capture the skill of batters rather than batting average or RBI. Similarly, strikeouts, walks, and steals yield predictive information about the skills of the pitching team. When using balls and walks counts, we discount intentional walks. 

The actual number of runs fails to take into account luck and near misses. In baseball short-term outcomes are often dominated by randomness. In order to take that into account, we use Pitcher’s Total Bases (PTB) in place of runs as the dependent variable. PTB is a factor in Component ERA, a baseball statistic invented by Bill James [3,9]. Here, H is hit, HR is home run, BB is walk, HBP is hit by pitch, and IBB is intentional walk. 

PTB  =0.89×(1.255×(H−HR)+4×HR)  +0.56×(BB+HBP−IBB) 

### **3.1   Problem Formulation** 

First, we formulate our problem as a regression problem, and solve it using regularized least squares [7]. For pitcher 𝑗, our training data is a set of 𝑛! points of the form {(𝑥!!, 𝑟!!)|𝑥!! ∈ℜ!, 𝑟!! ∈ℜ  }!!!!! , where 𝑟!! is PTB and 𝑥  is a feature vector. min! 𝑛1<sup>!</sup> !!!!<sup>!</sup> (𝑟!! −  𝑥!! 𝑤!!)! +  𝜆 𝑤! ! We next move to the binary problem of predicting whether there will be a run given in the next inning. We binarize ! the outputs of the regression 𝑟! , and find a pitcher specific cut-off 𝑏!<sup>on the estimated PTB that maximizes the</sup> ! ! prediction accuracy on the validation set. Prediction outputs are given by 𝑠𝑖𝑔𝑛(𝑥! 𝑤! −𝑏!<sup>).</sup> !! ! ! max 𝑦!(𝑥! 𝑤! −𝑏!<sup>)</sup> !! !!! 

Our model is pitcher-specific, and we learn feature weights independently for each pitcher. However, we want to take advantage of the fact that feature weights have some relationship across pitchers (e.g., Fenway Park presents challenges for many left handed pitchers) and use this to increase the number of samples used. Therefore, we rewrite the problem as a multi-task learning formulation [5] to share information across pitchers 𝑗= 1,2, … , 𝐽. 



Here, 𝑤! =  𝑤! + 𝑣!. Regularization parameters 𝜆!, 𝜆! and shrinkage coefficients are found by maximizing the area ! under the ROC curve for true class labels ! 𝑦! (whether a run is given in the next inning) and the prediction scores 𝑟! (estimated PTB) on the validation set. 

## **4   Experimental Results** 

We evaluate our method on the MLB data for years 2006-2010 from STATS Inc., which contains a record of each pitch thrown in both the regular and post seasons [6]. We train our model using the first 80% of the games of each 





<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->

2014 Research Paper Competition Presented by: 



season, and test it on the last 20%. We choose the regularization parameter and the threshold cut-off to binarize the regression outputs using cross validation on the training set. 

We first evaluate our model (Ours) relative to our manager model. We learn a manager model based on actual decisions of MLB managers. As discussed earlier, our manager model learns pitcher-specific parameters that fit pitch count and runs given up against the manager’s decisions on the training data. For the 76 pitchers who pitched at least 500 pitches in each year, this heuristic model accurately models the manager’s decision in 95%(±1.2%) of the innings (Fscore 0.87±0.02), i.e., it is a reasonably accurate model of major league managers. 



The manager model predicts whether a run will be scored in 75%(±4.6%) of the innings. In contrast, our model makes a correct prediction for 81%(±4.9%) of the innings. Figure 1 plots the histogram of accuracies for both methods. Notice that each method is far more accurate for some pitchers than for others. 

**Figure 1 Histogram of accuracies** 

### **4.1   Useful Features** 

The weights of a linear regression can be used to identify the most useful predictors. Below left we list the top 5 predictors based on the mean of the weights across pitchers. Surprisingly, pitch count does not appear in the list. However, two inning-related features, which are highly correlated with pitch-count, do. We can only speculate on why inning seems to be more important than pitch count: perhaps cooling down and warming up takes a toll on pitchers or perhaps psychological factors are highly influential. Below right we list the predictors with the highest standard deviation of the weights across pitchers. Notice that two features appear in both lists. 

Top predictors across pitchers: 

- Pitcher-Inning prior (SLG) 

- Pitcher-Batting team prior (SLG) 

- Pitcher-1<sup>st</sup> batter (in the lineup) prior (Runs) 

- Pitcher-3<sup>rd</sup> batter prior (Runs) 

Predictors with high variance across pitchers: 

- Pitcher-Inning prior (ERC) 

- Pitcher-home team prior (ERC) 

- Pitcher-batting team prior (ERC) 

- Pitcher-3<sup>rd</sup> batter (in the lineup) prior (Runs) 

### **4.2   Predictability** 



<!-- Start of picture text -->
Figure 2 Accuracy of the models for each inning<br><!-- End of picture text -->

Next, we test the accuracy in various situations. Figure 2 plots the average accuracy against the inning number across all the pitchers for our method and the manager model. The sizes of the circles denote the number of games. 

At the beginning of the game, both methods have similar predictability. The difference increases drastically in later innings. As the game progresses (especially after the 4th inning, i.e., in the second half of a game), our method becomes more accurate because it exploits information in previous innings to track the progression of the game 



2014 Research Paper Competition Presented by: 



<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->



## **5   Case Study: 2013 Post Season** 

For the results in the section we trained our model using 2013 regular season data provided by MLB.com. 

### **5.1   Game 2 of 2013 ALCS** 

Game 2 of 2013 ALCS between Detroit Tigers and Boston Red Sox was a pivotal game in the series. A highly debated moment occurred when the Detroit starter, Max Scherzer, was pulled after the 7<sup>th</sup> inning. Our model would have indicated that Scherzer should not have been removed. Detroit relievers (Detroit used 4 relievers in the bottom of the 8th inning) ended up giving 4 runs. 

### **5.1   Red Sox Starting Pitching** 

We applied our method to predict the performances of all Boston Red Sox starting pitchers during 2013 post season. Table 1 lists the results of predictions. 

**Table 1 Red Sox Post Season 2013: Prediction Results** 

|**Pitcher**|**Innings **|**Games**|**Accurac**<br>Manager<br>Model|**y (%)**<br>Our<br>Model|**F-Sc**<br>Manager<br>Model|**ore**<br>Our<br>Model|**Odds**<br>Manager<br>Model|**Ratio**<br>Our<br>Model|
|---|---|---|---|---|---|---|---|---|
|**Jon Lester**|37|5|82|81|0.01|0.31|0.1|2.78|
|**John Lackey**|28|4|58|69|0.33|0.46|3.88|27.1|
|**Clay Buchholz**|22|4|79|86|0.1|0.33|0.1|2.53|
|**Jake Peavy**|14|3|65|75|0.02|0.5|0.1|1.9|



In Table 2, we demonstrate the potential impact of our method. There were 96 innings pitched by Red Sox starters, of which, 33 were beyond the 4th inning. In 24 of those innings our model would have agreed with the manger to keep the starter in. The starter ended up giving a run in 3 (12.5%) of those innings. There were 9 innings where the manager kept the starter in, but our model wouldn’t have, and starter ended up giving a run in 5 (55%) of those innings. In only one game (World series 3rd Game), would our model have allowed the pitcher to continue, but the manager didn’t. 

**Table 2 Red Sox Post Season 2013: Potential Impact** 

|**Pitcher**|**Innings**|**Innings > 4**|**Both Kept**<br>**(Gave up runs)**|**Ours would have removed**<br>**(Gave up runs)**|
|---|---|---|---|---|
|**Jon Lester**|37|15|10 (0)|5(2)|
|**John Lackey**|28|11|8 (1)|3 (2)|
|**Clay Buchholz**|22|5|4 (1)|1 (1)|
|**Jake Peavy**|14|2|2 (1)|0 (0)|







<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->

2014 Research Paper Competition Presented by: 



## **6   Potential Impact** 

In this section, we discuss the potential impact of using our method to decide when to remove a starting pitcher. We consider only the fifth inning on, since in the early parts of the game many factors other than expected effectiveness figure into the decision of whether to remove the starting pitcher. 

Out of **21,538** innings, our model disagreed with the manager’s actual decision (not our manager model) a surprisingly high **48%** of the time. 

- There were **5,012** innings which the manager removed the starting pitcher and our model would reach the same decision. 

- There were **6,201** innings in which the manager allowed the starting pitcher to continue and for which our model would reach the same decision. In roughly **17.7%** of those innings the starting pitcher surrendered at least one run. 

- There were **9,288** innings in which the manager elected to leave the starting pitcher in, but our model would make the opposite decision. In roughly **31.5%** of those innings the starting pitcher surrendered at least one run. 

- There were **1,037** innings in which the manager removed the starting pitcher and our model would have allowed the starter to continue. There is no way to know how the starter would have done had he not been removed. 

## **7   Limitations and Future Work** 

There are several technical limitations in evaluating the real world application of our method. First, it is impossible to say what would have happened in those situations where a manager removed a pitcher that the model would have kept, since we don’t know whether or not the removed pitcher would have given up a run had he not been removed. Hence, our evaluations are one sided. 

We consider only whether a run will be given up in the next inning to decide whether to let the starting pitcher start the next inning. In practice, many other considerations come into play, particularly in early innings. Also, we don’t have a model that predicts the performance of possible replacements for the starter. Finally, the starting pitcher is often removed in the middle of the inning. Our current method doesn’t address this scenario. We intend to do batter-by-batter prediction in our future work. 

We expect that our method can be applied to other similar sports. For instance, in cricket, we can use the same approach to predict the best bowler to bowl the next over. 

## **8   Conclusion** 

Using information about the at bat from the past innings, game situation, and historical data, we estimate the number of runs given in the next inning. Using our method, MLB team managers can decide when a starting pitcher should be relieved. The results suggest that using our model might have led to better decisions than those typically made by major league managers. 

## **9   Acknowledgements** 

We would like to thank STATS LLC and MLB.com for providing us with the data and Quanta Computers Inc. and Qatar Computer Research Institute for supporting this work. 





<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->

2014 Research Paper Competition Presented by: 



## **References** 

[1] J. Albert. Pitching statistics, talent and luck, and the best strikeout seasons of all-time. Journal of Quantitative Analysis in Sports, 2(1):2, 2006. 

[2] G. Baseball. The pitching rotation and the bullpen @ONLINE. 

http://www.howbaseballworks.com/RotationandBullpen.htm, Jan. 2013. 

[3] B. Baumer and S. Ben. Why on-base percentage is a better indicator of future performance than batting average: An algebraic proof. Journal of Quantitative Analysis in Sports, 4(2):3, 2008. 

[4] R. M. Bell and Y. Koren. Scalable collaborative filtering with jointly derived neighborhood interpolation weights. In Data Mining, 2007. ICDM 2007. Seventh IEEE International Conference on, pages 43–52. IEEE, 2007. [5] T. Evgeniou and M. Pontil. Regularized multi–task learning. In Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, pages 109–117. ACM, 2004. 

[6] G. Ganeshapillai and J. Guttag. Predicting the next pitch. Sloan Sports Analytics Conference, 2012. 

[7] A. E. Hoerl and R. W. Kennard. Ridge regression: Biased estimation for non-orthogonal problems. Technometrics, 12(1):55–67, 1970. 

[8] G. Huckabay. 6-4-3: Reasonable person standard @ONLINE. http://www.baseballprospectus.com/article.php? articleid=1581, Aug. 2002. 

[9] Imagine sports. Glossary @ONLINE. http: //imaginesports.com/bball/reference/glossary/ popup, Jan. 2013. 

[10] B. James. Whatever happened to the Hall of Fame? Free Press, 1995. 

[11] J.Keri. Baseball Prospectus. Baseball Between the Numbers: Why Everything You Know about the Game Is Wrong. Basic Books, 2007. 

[12] Baseball Prospectus. Baseball Prospectus 2004. Wiley, 2004. 

[13] Baseball Prospectus. Baseball Prospectus 2011. Wiley, 2011. 

[14] N. Silver. Introducing PECOTA. Baseball Prospectus, 2003:507– 514, 2003. 

[15] N. Silver. The Signal and the Noise: Why So Many Predictions Fail-but Some Don’t. Penguin Group US, 2012. [16] S. Sullivan. State of the art: The actuarial game of baseball @ONLINE. http://www.contingencies.org/ mayjun04/stat.pdf, June 2004. 

[17] F. Zimniuch and L. Smith. Fireman: The Evolution of the Closer in Baseball. Triumph Books, 2010. 





<!-- Start of picture text -->
Presented by:<br><!-- End of picture text -->

2014 Research Paper Competition Presented by: 


