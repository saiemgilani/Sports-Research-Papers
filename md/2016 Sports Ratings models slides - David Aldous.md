<!-- source: 2016 Sports Ratings models slides - David Aldous.pdf -->







David Aldous 

January 27, 2016 





- **Sports** are a popular topic for course projects – usually involving details of some specific sport and statistical analysis of data. 



- In this lecture we imagine some non-specific sport; either a team sport – _(U.S.) football, baseball, basketball, hockey; soccer cricket_ – or an individual sport or game – _tennis, chess, boxing_ . 



- We consider only sports with matches between two 

- teams/individuals. But similar ideas work where there are many contestants – _athletics, horse racing, automobile racing, online video games_ . 

Let me remind you of three things you already know about sports. 

**Reminder 1.** Two standard “centralized” ways to schedule matches: league or tournament. 



<!-- Start of picture text -->
2014–15 Premier League<br>Standings<br># Team GP W D L GF GA GD PTS<br>1 Chelsea 38 26 9 3 73 32 41 87<br>2 Man City 38 24 7 7 83 38 45 79<br>3 Arsenal 38 22 9 7 71 36 35 75<br><!-- End of picture text -->

|20<br>Sta<br>|14–15 Premier League<br>ndings<br><br>|<br>|||||||
|---|---|---|---|---|---|---|---|---|
|#|Team<br>GP|W|D|L|GF|GA|GD|PTS|
|1|Chelsea<br>38|26|9|3|73|32|41|**87**|
|2|Man City<br>38|24|7|7|83|38|45|**79**|
|3|Arsenal<br>38|22|9|7|71|36|35|**75**|
|4|Man United<br>38|20|10|8|62|37|25|**70**|
|5|Tottenham<br>38|19|7|12|58|53|5|**64**|
|6|Liverpool<br>38|18|8|12|52|48|4|**62**|
|7|Southampton<br>38|18|6|14|54|33|21|**60**|
|8|Swansea City<br>38|16|8|14|46|49|-3|**56**|
|9|Stoke City<br>38|15|9|14|48|45|3|**54**|
|10|Crystal Palace<br>38|13|9|16|47|51|-4|**48**|
|11|Everton<br>38|12|11|15|48|50|-2|**47**|
|12|West Ham<br>38|12|11|15|44|47|-3|**47**|
|13|West Brom<br>38|11|11|16|38|51|-13|**44**|
|14|Leicester City<br>38|11|8|19|46|55|-9|**41**|
|15|Newcastle<br>38|10|9|19|40|63|-23|**39**|
|16|Sunderland<br>38|7|17|14|31|53|-22|**38**|
|17|Aston Villa<br>38|10|8|20|31|57|-26|**38**|
|18|Hull City<br>38|8|11|19|33|51|-18|**35**|
|19|Burnley FC<br>38|7|12|19|28|53|-25|**33**|
|20|QPR<br>38|8|6|24|42|73|-31|**30**|
||Show less||||||||









Barclays Premier League table, current & previous standings www. **premierleague** .com/en-gb/.../ **league** - **table** .html Premie <mark>r L</mark> eague 





These schemes are clearly “fair” and produce a “winner”, though have two limitations 



Limited number of teams. 



Start anew each year/tournament. 



Require central organization – impractical for for games ( _chess, tennis_ ) with many individual contestants. 

**Reminder 2.** In most sports the winner is decided by _point difference_ . One could model point difference but we won’t. For simplicity we will assume matches always end in win/lose, no ties. 

**Reminder 3.** A main reason why sports are interesting is that the outcome is uncertain. It makes sense to consider the **probability** of team A winning over team B. In practice one can do this by looking at gambling odds [next slide]. Another lecture will discuss data and theory concerning how probabilities derived from gambling odds change over time. 



# Winner of 2015-16 season Superbowl – gambling odds at start of season. 

|**Outcome**|**PredictWise**|**Derived Betfair Price**|**Betfair Back**|**Betfair Lay**|
|---|---|---|---|---|
|Seattle Seahawks|18 %|$ 0.171|5.80|5.90|
|Green Bay Packers|14 %|$ 0.137|7.20|7.40|
|Indianapolis Colts|9 %|$ 0.089|11.00|11.50|
|New England Patriots|8 %|$ 0.077|12.50|13.50|
|Denver Broncos|6 %|$ 0.063|15.50|16.50|
|Dallas Cowboys|5 %|$ 0.047|21.00|22.00|
|Baltimore Ravens|4 %|$ 0.038|26.00|27.00|
|Philadelphia Eagles|3 %|$ 0.036|26.00|30.00|
|Pittsburgh Steelers|3 %|$ 0.035|28.00|30.00|
|Miami Dolphins|3 %|$ 0.033|29.00|32.00|
|Arizona Cardinals|3 %|$ 0.026|36.00|40.00|
|Cincinnati Bengals|2 %|$ 0.024|40.00|42.00|
|Kansas City Chiefs|2 %|$ 0.022|44.00|46.00|
|Carolina Panthers|2 %|$ 0.021|44.00|55.00|
|Atlanta Falcons|2 %|$ 0.020|48.00|50.00|
|New Orleans Saints|2 %|$ 0.019|50.00|55.00|
|Buffalo Bills|2 %|$ 0.018|50.00|65.00|
|Detroit Lions|2 %|$ 0.017|55.00|60.00|
|New York Giants|2 %|$ 0.017|55.00|60.00|
|Minnesota Vikings|2 %|$ 0.017|55.00|65.00|
|San Diego Chargers|1 %|$ 0.016|60.00|65.00|





<!-- Start of picture text -->
St Louis Rams 1 % $ 0.014 65.00 75.00<br>Houston Texans 1 % $ 0.013 75.00 80.00<br>San Francisco 49ers 1 % $ 0.010 90.00 110.00<br>New York Jets 1 % $ 0.010 100.00 110.00<br>Chicago Bears 0 % $ 0.006 160.00 200.00<br>Cleveland Browns 0 % $ 0.004 200.00 260.00<br>Washington Redskins 0 % $ 0.003 290.00 400.00<br>Tampa Bay Buccaneers 0 % $ 0.003 270.00 500.00<br>Oakland Raiders 0 % $ 0.003 310.00 410.00<br>Tennessee Titans 0 % $ 0.002 520.00 600.00<br>Jacksonville Jaguars 0 % $ 0 002 450 00 600 00<br>POLITICS<br><!-- End of picture text -->



Obviously the probability A beats B depends on the **strengths** of the teams – a better team is likely to beat a worse team. So the problems estimate the strengths of A and B estimate the probability that A will beat B 

must be closely related. This lecture talks about two ideas for making such estimates which have been well studied. However the connection between them has not been so well studied, and is suitable for simulation-style projects. 

**Terminology.** I write **strength** for some hypothetical objective numerical measure of how good a team is – which we can’t observe – and **rating** for some number we can calculate by some formula based on past match results. Ratings are intended as estimates of strengths. 



# **Idea 1: The basic probability model.** 

Each team A has some “strength” _xA_ , a real number. When teams A and B play 



for a specified “win probability function” _W_ satisfying the conditions 



Implicit in this setup, as mentioned before 



each game has a definite winner (no ties); 





no home field advantage, though this is easily incorporated by making the win probability be of the form _W_ ( _xA − xB ±_ ∆); not considering more elaborate modeling of point difference 

and also 



strengths do not change with time. 



# **Some comments on the math model.** 



_W_ : R _→_ (0 _,_ 1) is continuous, strictly increasing 

_W_ ( _−x_ ) + _W_ ( _x_ ) = 1; lim _x→∞_<sup>_W_(</sup><sup>_x_) = 1</sup><sup>_._</sup> 

There is a reinterpretation of this model, as follows. Consider the alternate model in which the winner is determined by point difference, and suppose the random point difference _D_ between two teams of equal strength has some (necessarily symmetric) continuous distribution not depending on their common strength, and then suppose that a difference in strength has the effect of increasing team A’s points by _xA − xB_ . Then in this alternate model 

P(A beats B) = P( _D_ + _xA−xB ≥_ 0) = P( _−D ≤ xA−xB_ ) = P( _D ≤ xA−xB_ ) _._ So this is the same as our original model in which we take _W_ as the distribution function of _D_ . 



This basic probability model has undoubtedly been re-invented many times; in the academic literature it seems to have developed “sideways” from the following type of statistical problem. Suppose we wish to rank a set of movies _A, B, C , . . ._ by asking people to rank (in order of preference) the movies they have seen. Our data is of the form (person 1): _C , A, E_ 

(person 2): _D, B, A, C_ (person 3): _E , D_ 

. . . . . . . . . 

One way to produce a consensus ranking is to consider each pair ( _A, B_ ) of movies in turn. Amongst the people who ranked both movies, some number _i_ ( _A, B_ ) preferred _A_ and some number _i_ ( _B, A_ ) preferred _B_ . Now reinterpret the data in sports terms: team _A_ beat _B i_ ( _A, B_ ) times and lost to team _B i_ ( _B, A_ ) times. Within the basic probability model (with some specified _W_ ) one can calculate MLEs of strengths _xA, xB , . . ._ which imply a ranking order. 



This method, with _W_ the logistic function (discussed later), is called the _Bradley-Terry_ model, from the 1952 paper _Rank analysis of incomplete block designs: I. The method of paired comparisons_ by R.A. Bradley and M.E. Terry. 

An account of the basic Statistics theory (MLEs, confidence intervals, hypothesis tests, goodness-of-fit tests) is treated in Chapter 4 of H.A. David’s 1988 monograph _The Method of Paired Comparisons_ . 

So one can think of **Bradley-Terry as a sports model** as follows: take data from some past period, calculate MLEs of strengths, use to predict future win probabilities. 



Considering Bradley-Terry as a sports model: 

# **positives:** 

- allows unstructured schedule; 

- use of logistic makes algorithmic computation straightforward. 

- **negatives:** 

- use of logistic completely arbitrary: asserting 

if P( _i_ beats _j_ ) = 2 _/_ 3 _,_ P( _j_ beats _k_ ) = 2 _/_ 3 then P( _i_ beats _k_ ) = 4 _/_ 5 

as a universal fact seems ridiculous; 

- by assuming unchanging strengths, it gives equal weight to past as to 

- recent results; 

- need to recompute MLEs after each match. 

The Bradley-Terry model could be used for interesting course projects – take the Premier league data and ask _what is the probability that Chelsea was actually the best team in 2014-15?_ . 



**Reminder 4.** Another aspect of what makes sports interesting to a spectator is that strengths of teams change over time – if your team did poorly last year, then you can hope it does better this year. 

In the context of the Bradley-Terry model, one can extend the model to allow changes in strengths. Seem to be about 2-3 academic papers per year which introduce some such extended model and analyze some specific sports data. Possible source of course projects – apply to different sport or to more recent data. 



**Idea 2: Elo-type rating systems** [show site] 

(not ELO). The particular type of rating systems we study are known loosely as Elo-type systems and were first used systematically in chess. The Wikipedia page _Elo rating system_ is quite informative about the history and practical implementation. What I describe here is an abstracted “mathematically basic” form of such systems. Each player _i_ is given some initial rating, a real number _yi_ . When player _i_ plays player _j_ , the ratings of both players are updated using a function Υ ( `Upsilon` ) 

if _i_ beats _j_ then _yi → yi_ + Υ( _yi − yj_ ) and _yj → yj −_ Υ( _yi − yj_ ) if _i_ loses to _j_ then _yi → yi −_ Υ( _yj − yi_ ) and _yj → yj_ + Υ( _yj − yi_ ) .<sup>(2)</sup> 

Note that the sum of all ratings remains constant; it is mathematically natural to center so that this sum equals zero. 



The*Elo*raSngs*are*based*on*the*following*formulas: 



- **Rn** *is*the*new*raSng,* **Ro** *is*the*old*(preJmatch)*raSng. 

- **K** *is*the*weight*constant*for*the*tournament*played: 

- **60** 

- **50** 

- **40** 

- **30** *for*all*other*tournaments; 

- **20** *for*friendly*matches. 

- **K half** *if*a* game*is*won*by*two*goals,*by* **3/4** *if*a*game*is*won*by*three*goals,*and*by* **3/4$+$ (N=3)/8** if*the*game*is*won*by*four*or*more*goals,*where* **N** *is*the*goal*difference. 

- **W** *is*the*result*of*the*game*( **1** *for*a*win,* **0.5** *for*a*draw,*and* **0** *for*a*loss). 

- formula: **We** *is*the*expected*result*(win*expectancy),*either*from*the*chart*or*the*following* 

- We*=*1*/*(10<sup>(Jdr/400)</sup> *+*1) 

- **dr 100** *points*for*a*team*playing*at*home. 



Schematic of one player’s ratings after successive matches. The _•_ indicate each opponent’s rating. 



<!-- Start of picture text -->
rating r<br>6<br>r<br>r<br>r<br>r<br>r<br><!-- End of picture text -->



**Math comments on the Elo-type rating algorithm.** We require the function Υ( _u_ ) _, −∞ < u < ∞_ to satisfy the qualitative conditions 



We will also impose a quantitative condition 



To motivate the latter condition, the rating updates when a player with (variable) strength _x_ plays a player of fixed strength _y_ are 



and we want these functions to be _increasing_ functions of the starting strength _x_ . 

Note that if Υ satisfies (3) then so does _c_ Υ for any scaling factor _c >_ 0. So given any Υ satisfying (3) with _κ_ Υ _< ∞_ we can scale to make a function where (4) is satisfied. 



The logistic distribution function 



is a common choice for the “win probability” function _W_ ( _x_ ) in the basic probability model; and its complement 



is a common choice for the “update function shape” Υ( _x_ ) in Elo-type rating systems. That is, one commonly uses Υ( _x_ ) = _cF_ ( _−x_ ). 





possible _W_ ( _x_ ) possible Υ( _x_ ) 

Whether this is more than a convenient choice is a central issue in this topic. 



Elo is an algorithm for producing ratings (and therefore rankings) which (unlike Bradley-Terry) does not assume any probability model. It implicitly attempts to track changes in strength and puts greater weight on more recent match results. 

**How good are Elo-type algorithms?** This is a subtle question – we need to 



use Elo to make predictions 



choose how to measure their accuracy 



compare accuracy with predictions from some other ranking/rating scheme (such as Bradley-Terry or gambling odds). 

The simplest way to compare schemes would be to look at matches where the different schemes ranked the teams in opposite ways, and see which team actually won. But this is not statistically efficient [board]. Better to compare schemes which predict **probabilities** . 

Although the Elo algorithm does not say anything _explicitly_ about probability, we can argue that it _implicitly_ does predict winning probabilities. 



# **A math connection between the probability model and the rating algorithm.** 

Consider _n_ teams with unchanging strengths _x_ 1 _, . . . , xn_ , with match results according to the basic probability model with win probability function _W_ , and ratings ( _yi_ ) given by the update rule with update function Υ. When team _i_ plays team _j_ , the expectation of the rating change for _i_ equals 



So consider the case where the functions Υ and _W_ are related by 



# In this case 

_(*) If it happens that the difference yi − yj in ratings of two players playing a match equals the difference xi − xj in strengths then the expectation of the change in rating difference equals zero_ 

whereas if unequal then (because Υ is decreasing) the expectation of ( _yi − yj_ ) _−_ ( _xi − xj_ ) is closer to zero after the match than before. 





These observations suggest that, under relation (6), there will be a tendency for player _i_ ’s rating _yi_ to move towards its strength _xi_ though there will always be random fluctuations from individual matches. So if we believe the basic probability model for some given _W_ , then in a rating system we should use an Υ that satisfies (6). 

_Recall that in the probability model we can center the strengths so that_ � _i_<sup>_xi_= 0</sup><sup>_,andsimilarlywewillinitializeratingssothat_�</sup> _i_<sup>_yi_= 0</sup><sup>_._</sup> What is the solution of (6) for unknown Υ? 

This can be viewed as the setup for a mathematician/physicist/statistician joke. 



# `Problem` 

solve Υ( _u_ ) _/_ Υ( _−u_ ) = _W_ ( _−u_ ) _/W_ ( _u_ ) _, −∞ < u < ∞._ 

# `Solution` 



physicist (Elo): Υ( _u_ ) = _cW_ ( _−u_ ) 





mathematician: Υ( _u_ ) = _W_ ( _−u_ ) _φ_ ( _u_ ) for arbitrary symmetric _φ_ ( _·_ ). statistician: Υ( _u_ ) = _c_ � _W_ ( _−u_ ) _/W_ ( _u_ ) (variance-stabilizing _φ_ ). 

These answers are all “wrong” for different reasons. And so in fact it’s hard to answer “what Υ to use?” 

However we can work backwards; when people use the “complement of logistic” as the update function Υ, we can use (6) to argue that they are implicitly imagining the Bradley-Terry with _W_ the logistic function. So this gives a way to use Elo ratings to predict win probabilities. 



There is a link to my more mathematical write-up of the topic above. 

There are several related possible **simulation projects** . For instance, consider a league on _n_ teams, whose strengths has some SD _σ_ , the strengths change in time via some rule with rate parameter _λ_ . We take the probability model with logistic _W_ and the update model with function _c_ Υ for logistic Υ. Study how the optimal value of _c_ depends on ( _n, σ, λ_ ). 



**Some other aspects of rating models.** 

**1.** Recent book “The Science of Ranking and Rating” treats methods using undergraduate linear algebra. The lecture in this course in 2014 was based more on that book (link on web page). 

**2.** People who attempt realistic models of particular sports, using e.g. statistics of individual player performance, believe their models are much better than general-sport methods based only on history of wins/losses or point differences. But a recent paper _Statistics-free sports prediction_ claims that (using more complex prediction schemes) they can do almost as well using only match scores. 

**3.** I have talked about comparing different schemes which predict **probabilities** – after we see the actual match results, how do we decide which scheme is better? I will discuss this in a different context, the lecture on Geopolitics forecasting. 

**4.** Both schemes are poor at assessing new players. Xbox Live uses its “TrueSkill ranking system” [show page] which estimates both a rating and the uncertainty in the rating, as follows. 







Here a rating for player _i_ is a pair ( _µi , σi_ ), and the essence of the scheme is as follows. When _i_ beats _j_ 

(i) first compute the conditional distribution of _Xi_ given _Xi > Xj_ , where _Xi_ has Normal( _µi , σi_<sup>2)distribution</sup> 

(ii) then update _i_ ’s rating to the mean and s.d. of that conditional distribution. 

Similarly if _i_ loses to _j_ then _i_ ’s rating is updated to the mean and s.d. of the conditional distribution of _Xi_ given _Xi < Xj_ . 

**Discussion.** `The authors seem to view this as an approximation to some coherent Bayes scheme, but to me it fails to engage both ‘‘uncertainty about strength" and ‘‘uncertainty about match outcome".` 

So another simulation project is to compare this to other schemes. Note this implicitly predicts winning probabilities via P( _Xi > Xj_ ). 



[show slides from previous year lecture] 

People often think that bookmakers adjust their offered odds so that, whatever the outcome, they never lose money. This just isn’t true. [show ESPN article] 

Finally, there is an interesting paradox involved in designing matches to be exciting to spectators [board]. 


