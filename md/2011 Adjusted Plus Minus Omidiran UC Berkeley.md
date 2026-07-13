<!-- source: 2011 Adjusted Plus Minus Omidiran UC Berkeley.pdf -->

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



# **A New Look at Adjusted Plus/Minus for Basketball Analysis** 

Dapo Omidiran University of California, Berkeley, Berkeley, California, USA, 94707 Email: dapo@eecs.berkeley.edu 

## **Abstract** 

We interpret the Adjusted Plus/Minus (APM) model as a special case of a general penalized regression problem indexed by the parameter<sup></sup> _λ_ . We  provide a fast technique for solving this problem for general values of _λ_ . We  then use cross-validation to select the parameter _λ_ and demonstrate that this choice yields substantially better prediction performance than APM. 

## **1 Introduction** 

> We model basketball as a sequence of _N_ independent events between two teams. During each event, the home team scores _Y i_ net points ( _Y i_ is actually defined slightly differently, but this is close enough for intuition.) These events are called “possessions” in basketball. For each event, we have a list of players on the floor, five for the home team and five for the away 

> team. We also have _p_ total players in the league. We can then represent the 

> current players on the floor for possession _i_ with a vector _X i_ of length _p_ which is defined as follows: 



We want to define a functional relationship between _X i_ and _Y i_ , i.e., find a function _f_ such that _Y_ ≈ _f_  _X i_  . One natural way to do this is through a linear regression model, which defines the relationship 



MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



Associated with each “possession” is an integer weight for each term, _w i_ . Thus each observation _Y i_ , _X i_ actually represents _w i_ possessions. 

For notational convenience, we stack the variables _Y i_ , _W i_ , and _ϵ i_ into the _n_ vectors _Y_ , _W_ , and _ϵ_ and the variables _X i_ into the _n_ × _p_ matrix _X_ . 

This yields the matrix expression 



The scalar variable _β hc a_ in Equation (1) represents a home court advantage term, while the _p_ vector _β_ is then interpreted as the net number of points each of the _p_ players in the league “produce” per minute. Note that this is different from the number of points they directly score. The model described by Equation (1) recognizes players who by their presence on the floor, their team is more effective (e.g. players who set hard screens, play good defense, etc.) 



 The values _β L S_ are called the adjusted plus/minus (APM) values for the players. See the website Basketballvalue.com [4] for computed _β_<sup></sup> _LS_ values for different players in the league for several recent seasons. 

## **2 Improvements to APM** 

While algorithm (2) is a reasonable approach for estimating the parameters   _β L S_ and _β hc a_ , it doesn’t take into account the following three pieces of information: 

1. Sparsity. By and large, the NBA is a game dominated by elite players. Lesser players have far less impact on wins and losses. While this is not some sort of fact, it is certainly commonly accepted wisdom and thus informs player acquisitions, salaries, etc. For example, with say a $60 million budget on players, one would much rather hire three elite $15 million players and fill out the rest of the roster with cheap roleplayers, then spend tons of money on roleplayers and skimp on elite players (this is the road the Boston Celtics did in the summer of 2007 when trading 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



their roleplayers and other assets for Kevin Garnett and Ray Allen [8], and the Miami Heat did in the summer of 2010 by building a team around three star players [9].) We shall incorporate this prior information through _ℓ_ 1 regularization. This effectively penalizes models that are not sparse, and should cause only elite players to stand out in the regression. 

2. Box score information. Another valuable piece of information useful in inferring player worth is to take into account box score statistics. You expect good players to not only have good APM numbers, but also to generally produce assists, blocks, steals, etc. Thus, we prefer ratings vectors _β_<sup></sup> which are consistent with box score statistics. 

3. We expect that some sort of weighted sum of player ratings should be close to zero, simply because the net number of points scored as a whole in the NBA is zero. Thus, the inner product of the vector _v_ = _y_<sup>_T_</sup> ∣ _X_ | and _β_ should be close to zero. 

We can encode the above prior information through the following function _g_ defined as 



- where  _λ_ is shorthand notation for  _λ_ 1 _, λ_ 2 _, λ_ 3 _, λ_ 4  . In the above expression 

   1. _R_ is a _p_ × _d_ matrix containing the box-score statistics of the _p_ different players. There are _d_ different box score statistics. 

   2. The variable _z_ gives us weights for each of the box score statistics. 

   3. The variable _z_ 0 can be interpreted as an average player rating. 

   4. The variable _β me d ian_ is used to center the betas around whatever the correct offset is. 

   - 

   - 5. The parameter _λ_ are different regularization weights. 

We can then find a model consistent with both the data and the prior information by solving the following convex optimization problem: 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



_β hc a , β , z_ 0 _, z , β me d ian_ =arg min _g_  _β hca , β , z_ 0 _, z , β me di an ;_<sup></sup> _λ_  (3) We call the procedure described by Equation (3) the<sup></sup> _λ P M_ algorithm. 

One important difference between<sup></sup> _λ P M_ and certain other approaches is that it yields both a player rating vector _β_ and a box score weights vector _z_ . Thus for player _i_ , we can compare the variable _β i_ to the variable 

_Ri z_  _β me an_ to understand how “overrated” or underrated player _i_ is relative to his box score production (note that _Ri_ is the _i_<sup>_t h_</sup> row of the matrix _R_ .) This is pretty useful, since many players produce great box score stats, but are less effective than their stats indicate due to poor defense, ballhogging, etc. 

 Furthermore, it is worth noting that _λ P M_ encompasses both the APM algorithm [1] and the SPM algorithm [3]. APM corresponds to the choice of   _λ_ =0 , while SPM can be viewed as the limit of _λ P M_ as _λ_ 1  0 , with _λ_ 2 , _λ_ 3 , _λ_ 4 fixed at zero. 

For<sup></sup> _λ P M_ to be useful, we need to be able to select the parameters<sup></sup> _λ_ very quickly. Our general methodology is to first derive a fast algorithm for solving<sup></sup> _λ P M_ for a fixed value of  _λ_ , then use cross-validation to select the correct value of<sup></sup> _λ_ . We can then compare the predictive power of this method to other approaches by evaluating predictive power on a test set. 

## **3 Experimental Results** 

## **3.1 Cross Validation** 

We implemented the cyclical coordinate descent solver for<sup></sup> _λ P M_ as well as a cross-validation procedure and ran it on the 2007-2008 NBA dataset. Experimentally we determined that the best values of<sup></sup> _λ_ are 

 _λ_ = _λ_ 1 _,λ_ 2 _, λ_ 3 _, λ_ 4= 215 _,_ 211 _,_ 25 _,_ 1 (4) 

Our procedure for selecting this value was to start from the vector _λ_ 0=1 _,_ 1 _,_ 1 _,_ 1 , and then for each of the four components _λ_ 1 , _λ_ 2 , _λ_ 3 and _λ_ 4 , iterate over the following sequence of values 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 





> where 2 _kmax_ is a value that causes the optimization variables to all be zero. For each value _λ i_ , we get the following plot: 



**Figure 1:** 25 fold CV, exponential grid in _λ i_ , all other components fixed. Best value roughly  2<sup>15</sup> _,_ 2<sup>11</sup> _,_ 2<sup>5</sup> _,_ 1 

> Again, the above plots were generated with _λ_<sup></sup> 0=1 _,_ 1 _,_ 1 _,_ 1 . We can take the best point on each plot to obtain the parameter vector _λ_ 1= 2 15 _,_ 211 _,_ 25 _,_ 1  , and re-run to get similar plots. While this doesn’t 

> necessarily mean that _λ_<sup></sup> 1 is the best possible point, it is suggestive. It seems plausible that a rigorous justification for this heuristic could be made using convex analysis. 

## **3.2 Predictive Power** 

 _λ P M_ with the choice  _λ_ = 215 _,_ 211 _,_ 25 _,_ 1 fits a particular model. But how do we evaluate this model? In classical linear regression, there are various goodness-of-fit tests [5] that we can do, which are valid under certain assumptions on the underlying model (e.g., gaussianity.) 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



Another choice is to test predictive power on a sample of games. To be explicit, we can estimate the 1230 NBA regular season games, build a model on say the first 800, then evaluate the model’s ability to predict the final margin of victory on the remaining 430 games. 

We compare the following three estimates: 

1. A dummy estimator that predicts that the home team wins each possession by 3.5 points. 

2. The APM estimate, which computes player ratings using least squares and uses those in predicting the margin of victory for the home team. 

- 15 11 5 

- 3. The _λ P M_ estimate with the choice of parameters<sup></sup> _λ_ = 2 _,_ 2 _,_ 2 _,_ 1 . Recall that this choice of parameters was obtained via cross-validation in the previous subsection. 

Once we train the above models, we get an estimate of the net number of points scored by the home team per possession. Since we don’t know a priori the number of possessions that will be involved in the game, we need an estimate of this. A very crude estimate is just the average number of possessions used per game in the 2007-2008 season, which is 92.4 [2]. 

Figure 3.2 is a plot of the resulting errors over the course of the last 348 games of the 2007-2008 NBA season, using the 882 games that came before it for cross-validation. 



**Figure 2:** Comparison of Home Court Advantage estimate, APM estimate, and<sup></sup> _λ P M_ estimate. 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



It is pretty clear from the above that<sup></sup> _λ P M_ produces better estimates than APM. We will also look at some statistical properties of the error variable for each game: 

||HCA|APM|_λ P M_|
|---|---|---|---|
|Fraction of|0.3793|0.3333|0.3017|
|Games||||
|Guessed Wrong||||
|Mean of|11.54|15.83|10.06|
|Absolute Error||||
|Variance of AE|70.38|149.02|58.61|
|Median of AE|9.50|13.88|9.10|
|Min of AE|0.3|0.00|0.00|
|Max of AE|48.30|72.64|33.50|
|Empirical|0.95|0.95|0.92|
|_P__A E_1||||
|Empirical|0.89|0.87|0.81|
|_P__A E_3||||
|Empirical|0.76|0.81|0.66|
|_P__A E_5||||
|Empirical|0.49|0.61|0.45|
|_P__A E_10||||



As the above table indicates, this method has substantially better predictive power than either the dummy model or the APM approach. As an aside, while the above two plots might reflect poorly on APM, it doesn’t necessarily mean that APM is useless. Part of the problem with using pure APM is that it is simply too sensitive to outliers. A player who plays only one minute of the first 882 games, but very good things happen in that minute might have an outrageously high _β i_ associated with him. If he then starts playing major minutes later in the season, then his high rating will cause lots of errors on games. It is likely that a Huber loss function might lead to better results for APM than the quadratic loss. 

## **3.3 Polynomials in** _R_ 

We also took a look at different polynomial transformations of the box-score matrix _R_ . It appears that different transformations of these variables seems to improve performance. For example, we can expand the matrix _R_ to 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



> include all pairwise product of the basic variables. If _R_ is say a _p_ by 14 14 

> matrix, this leads to a _p_ by 14<sup>_R_2.</sup> 2<sup>matrix</sup>  

## 3.3.1 _R_<sup>2</sup> 



**Figure 3:** 25 fold CV using _R_<sup>2</sup> exponential grid in _λ i_ , all other components fixed. Best value roughly  2<sup>14</sup> _,_ 2<sup>12</sup> _,_ 2<sup>2</sup> _,_ 2<sup>2</sup>  . 

This yields the following plot 



**Figure 4:** Comparison of Home Court Advantage estimate, APM  estimate, and _λ P M_ estimate with matrix _R_<sup>2</sup> . 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



It isn’t completely clear from the above plot that<sup></sup> _λ P M_ is the best. We examine the statistical properties of the absolute error variable over the block of games we want to predict: 

||HCA|APM|_λ P M_|
|---|---|---|---|
|Fraction of|0.3793|0.3333|0.2874|
|Games||||
|Guessed Wrong||||
|Mean of|11.54|15.83|10.58|
|Absolute Error||||
|Variance of AE|70.38|149.02|65.07|
|Median of AE|9.50|13.88|9.10|
|Min of AE|0.3|0.00|0.00|
|Max of AE|48.30|72.64|41.02|
|Empirical<br>|0.95|0.95|0.94|
|_P__A E_1||||
|Empirical|0.89|0.87|0.80|
|_P__A E_3||||
|Empirical|0.76|0.81|0.70|
|_P__A E_5||||
|Empirical|0.49|0.61|0.46|
|_P__A E_10||||



This more convincingly demonstrates the superiority of  _λ P M_ with the expanded box score matrix _R_<sup>2</sup> . 

## **4 Concluding Remarks** 

We have introduced<sup></sup> _λ P M_ , a powerful new statistical inference procedure for the NBA, which contains APM as a special case. We found a fast, iterative numerical algorithm for solving the convex optimization problem defining  _λ P M_ . We then utilize cross-validation to perform parameter selection. Finally, we compare the statistical performance of our approach to APM and find that the performance is dramatically improved. 



MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 

## **References** 

- [1] 82games.com. Adjusted plus/minus. http://www.82games.com/ilardi1.htm. 

- 

- [2] basketball reference.com. Pace estimate. http://www.basketball <u>reference.com/leagues/NBA_2008.html.</u> 

- 

- [3] basketball reference.com. Statistical plus/minus. http://www.basketball <u>reference.com/blog/?p=1351.</u> 

- [4] basketballvalue.com. Player ratings. http://www.basketballvalue.com. 

- [5] Julian J. Faraway. _Linear Models with R_ . Chapman & Hall/CRC, Boca Raton, FL, 2004. ISBN 1-584-88425-8. 

- [6] Jerome Friedman, Trevor Hastie, Holger Höfling, and Robert Tibshirani. Pathwise coordinate optimization. _Annals of Applied Statistics_ , 2:302– 332, 2007. 

- [7] Jerome Friedman, Trevor Hastie, and Robert Tibshirani. Regularization paths for generalized linear models via coordinate descent. _Journal of Statistical Software_ , 33(1):1–22, 2010. 

- 

- [8] NBA.com. Garnett Trade. http://www.nba.com/celtics/news/press073107 <u>garnett.html.</u> 

- [9] sun sentinel.com. LeBron James, Chris Bosh join the Heat. <u>http://articles.sun-sentinel.com/2010-07-08/sports/sfl-lebron-jamesdecision-070810_1_james-and-bosh-dwyane-wade-lebron-james.</u> 

- [10] Robert Tibshirani, Iain Johnstone, Trevor Hastie, and Bradley Efron. Least angle regression. _The Annals of Statistics_ , 32(2):407–499, April 2004. 

- [11] Tong Tong Wu and Kenneth Lange. Coordinate descent algorithms for lasso penalized regression. _Annals of Applied Statistics_ , 2:224–244, 2008. 


