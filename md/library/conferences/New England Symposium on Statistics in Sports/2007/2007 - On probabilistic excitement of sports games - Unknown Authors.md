<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - On probabilistic excitement of sports games - Unknown Authors.pdf -->



Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

# ~~Probabilistic Excitement of Sports Games~~ 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

Jan Vecer Tomoyuki Ichiba Mladen Laudanovic 

Department of Statistics, Columbia University, http://www.stat.columbia.edu/ _∼_ vecer 

Harvard University, September 29, 2007 

# ~~Abstract~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

In this talk we introduce a quantitative measure of the excitement of sports games. This measure can be thought of as the variability of the expectancy of winning as a game progresses. We illustrate the concept of excitement at soccer games for which the theoretical win expectancy can be well ~~approximated from a Poisson model of scoring. We show that~~ in the Poisson model, higher scoring rates lead to increased expected excitement. Given a particular strength of a team, the most exciting games are expected with opponents who are slightly stronger. We apply this theory to the FIFA World Cup 2006 games, where the winning expectancy was independently estimated by betting markets. Thus it was possible to compute the expected and the realized excitement of each given game from the trading data. 

# ~~Motivation~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

Higher Excitement comes with 

More changes in the score lead. ~~Changes that are more dramatic.~~ Decisive moments later in the game. 

Fluctuation of Win Expectancy satisfies the above criterions. More changes to the Win Expectancy, the less “predictable” is the outcome of the game. 

# ~~Defnition~~ 

Probabilistic Excitement of Sports Games 

We propose the following measure for excitement: 

Jan Vecer 

Motivation 

Excitement = Variability of the Winning Expectancy. (1) 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

Variability can be measured as the Total Variation (TV): 

_TV_ ( _f_ ) = max _|ti_ lim+1 _−ti |→_ 0 <u>�</u> _|f_ ( _ti_ +1) _− f_ ( _ti_ ) _|,_ (2) 

where 0 = _t_ 0 _< t_ 1 _< · · · < tn_ = _T_ is a partition of the interval [0 _, T_ ]. Total variation can be viewed as the vertical component of the arc-length of the graph of a given function _f_ . The longer the path of win expectancy for a given team, the more swings there are in the game, and thus the game is more exciting. 

# ~~Defnition - Continued~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation Definition 

Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

## Formally, we can define ~~Defnition~~ 

~~Excitement = TV(Probability of Team 1 Wins)~~ + TV(Probability of Team 2 Wins). (3) 

# ~~Defnition - Continued~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

This definition makes sense if a draw is not an option, such as in the elimination round games. If a draw is possible, we can use a modified version: 

~~Defnition~~ 

Excitement = TV(Probability that Team 1 Wins) 

+ TV(Probability of Draw) + TV(Probability that Team 2 Wins). (4) 

# ~~Defnition Explained~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

In general, the total variation of winning expectancy is mostly changed if there is a game deciding event close to the end of ~~the game, if there are a number of events where the game lead~~ is changed, or if the weaker team unexpectedly wins or draws the game. On the other hand, only small changes in the total variation of winning probabilities occur when the game is one sided, with an early lead from the favorite team. 

~~Win Expectancy~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

Our approach to quantitatively measure the excitement via variability of the win expectancy described in this talk is novel and it could be applied to all sports played with two competing ~~teams.~~ 

Win Expectancy can be computed/observed from The Model. 

Betting Market. 

# ~~Measurement from Model~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

There are already some cases of sports specific attempts to measure excitement based on model. The problem is that for many sports, it is not entirely clear how to determine the win <u>expectancy during the course of the game. The evolution of</u> the game can be modeled with rather simplifying assumptions for only a small number of sports. The simplest and analytically tractable models assume no memory during the game which suggests the use of Markov models. Sports whose evolution could be approximated well by Markov models include baseball, tennis, soccer, or hockey. 

# ~~Measuring from Betting Market.~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

Betting market (in play) provides excellent feedback on measuring probability of win/loss of a certain team. Betting markets are now organized as major financial exchanges (such <u>as betfair.com), and thus are very efcient and reliable in</u> estimating the correct Win Expectancy at any given point during the game. 

US entities cannot participate in the market for legal reasons, but the betting exchange trades US sports events as well (traded by foreign entities). 

# ~~Focus of the Talk~~ 

Probabilistic Excitement of Sports Games Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

We will focus on soccer in this talk since the it is both tractable from the model, and there is enough data from the betting market. 

# ~~Poisson Model~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

Poisson process is a memoryless counting process (i.e., taking integer values) in continuous time. Its evolution is given by 

P( _Xt_ +∆ _t_ = _Xt|Xt_ ) = 1 _− λ_ (∆ _t_ ) + _o_ (∆ _t_ ) _,_ (5) P( _Xt_ +∆ _t_ = _Xt_ + 1 _|Xt_ ) = _λ_ (∆ _t_ ) + _o_ (∆ _t_ ) _._ (6) 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

# ~~Score Evolution~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy 

We assume that the scores of the two teams evolve as independent Poisson processes. In particular, if _XT_ : _YT_ denotes the final score of the game, we have 

> <sup>_−t_</sup><sup><u>)]</u></sup><sup>_k_</sup> <u>P(</u> _<u>X</u>_ _~~T~~_ <u>=</u> _<u>X</u>_ _~~t~~_ <u>+</u> _<u>k</u>_ <u>) = exp[</u> _−λ_ <u>(</u> _<u>T</u> −_ _<u>t</u>_ <u>)]</u><sup><u>[</u></sup><sup>_λ_</sup><sup><u>(</u></sup><sup>_T_</sup> _<u>,</u>_ _~~k~~_ ~~!~~ 

and 

> <sup>_−t_</sup><sup><u>)]</u></sup><sup>_k_</sup> P( _YT_ = _Yt_ + _k_ ) = exp[ _−µ_ ( _T − t_ )]<sup><u>[</u></sup><sup>_<u>µ</u>_</sup><sup><u>(</u></sup><sup>_T_</sup> _, k_ ! 

where _Xt_ : _Yt_ is the current score at time _t_ in the game. Variable _T_ is the end time of the game, and it is assumed to be fixed. 

# ~~Score Evolution~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring 

Parameters _λ_ and _µ_ are called the scoring intensities of the two teams. They are related to the expected score by the following relationship: 

<u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

E[ _XT − Xt|Xt_ ] = _λ_ ( _T − t_ ) _,_ E[ _YT − Yt|Yt_ ] = _µ_ ( _T − t_ ) _._ 

Thus one should expect to see on average _λ_ ( _T − t_ ) and _µ_ ( _T − t_ ) goals for the two teams in the remaining _T − t_ time of the game. 

# ~~Win Expectancy~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

The Poisson model of scoring could be used for modeling the evolution of scoring in soccer or hockey games. The ~~memoryless property implies that the time between the goals is~~ exponentially distributed with parameters _λ_ and _µ_ respectively. In this model we can get explicit formulas for the win expectancy of each team, and the expectancy of a draw. 

# ~~Win Expectancy - Continued~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

If the current time is _t ∈_ [0 _, T_ ], and the current score is _Xt_ : _Yt_ , we have 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

~~P(Team 1 Will Win) = P(~~ _~~X~~ T_ _~~> Y~~ T_ ~~) =~~ 



# ~~Win Expectancy - Continued~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring 

<u>Win</u> 

Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

<u>P(Draw) = P(</u> _<u>XT</u>_ = _<u>YT</u>_ <u>) =</u> _∞_ = � _e_<sup>_−_(</sup><sup>_λt_+</sup><sup>_µt_)</sup> _·_ ( _kλ_ +max( _<u>t</u>_<sup>(</sup><sup>_k_+max(</sup> _X_<sup>_Xt_</sup> _t_ +<sup>+</sup> _Y_<sup>_Yt_</sup> _t_<sup>)</sup> )<sup>_−_</sup> _−_<sup>_Xt_</sup> _X_<sup>)</sup> _t_ )!<sup>_·_</sup> ( _kµ_ +max(<sup>(</sup> _<u>t</u>_<sup>_k_+max(</sup> _X_<sup>_Xt_</sup> _t_ +<sup>+</sup> _Y_<sup>_Yt_</sup> _t_<sup>)</sup> )<sup>_−_</sup> _−_<sup>_Yt_</sup> _Y_<sup>)</sup> _t_ )! _k_ =0 � � (8) 

# ~~Win Expectancy - Continued~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

P(Team 2 Will Win) = P( _YT > XT_ ) = 



<!-- Start of picture text -->
∞<br>= � P( YT =  k − Yt, XT < k − Yt )<br>k =0<br>∞ k−Xt + Yt − 1<br>= � e −µt µ kt k ! · � e −λt λ i ! t i (9)<br>k =0 � i =0 �<br><!-- End of picture text -->

# ~~Holland - Argentina~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

Evolution of probabilities (implied by a Poisson model of <u>scoring) of a draw, win of Holland and win of Argentina during</u> the Holland - Argentina game. The game ended with a 0:0 draw. The scoring intensity for Holland was estimated at 1.05, and for Argentina at 1.57. 

# ~~Draw~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � Draw �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~Holland~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

`P` � `Holland Win` � 



<!-- Start of picture text -->
1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~Argentina~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � Argentina Win �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~Togo - France~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

Evolution of probabilities (implied by a Poisson model of scoring) of a draw, win of Togo and win of France during the ~~Togo - France game. France scored in the 55th and the 61st~~ minute of the match. The betting market estimated the scoring intensities to be 0.37 for Togo and 2.65 for France. The expected excitement was 1.28, the lowest for all the games played in that championship. 

# ~~Draw~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � Draw �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~Togo~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 

`P` � `Togo Win` � 

```
1
0.8
```

`0.6 0.4 0.2 Time` � `Minutes` � <u>`20 40 60 80`</u> 

# ~~France~~ 

Probabilistic Excitement of Sports Games Jan Vecer 

Motivation Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � France Win �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~- Ghana USA~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

Evolution of probabilities (implied by a Poisson model of scoring) of a draw, win of Ghana and win of United States during the Ghana - United States <u>game.</u> Ghana scored in the 22nd minute, followed by the goal of United States in the 43rd minute and the second goal of Ghana in the 47th minute. The scoring intensity for Ghana was estimated at 1.37, and for the United States at 1.16. The expected excitement was 2.55, the highest expectation among all the games in the championship. 

# ~~Draw~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � Draw �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~Ghana~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation Definition Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � Ghana Win �<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->

# ~~USA~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
P � USA Win �<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>0.8<br>0.6<br>0.4<br>0.2<br>Time � Minutes �<br>20 40 60 80<br><!-- End of picture text -->



Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

|Game|_λ_1|_λ_2|Score|Win|Loss|Draw|Total|Model|Exp|
|---|---|---|---|---|---|---|---|---|---|
|Spain – France|1.16|0.92|1 - 3|1.48|1.16|1.41|4.05|4.53|2.42|
|Italy – Australia|1.65|0.62|1 - 0|1.57|0.35|1.68|3.60|3.52|2.11|
|Germany * – Argentina|1.22|1.06|1 - 1|0.62|1.27|1.47|3.36|3.62|2.47|
|Argentina * – Mexico|2.07|0.57|1 - 1|1.11|0.91|0.78|2.80|2.73|1.87|
|Italy * – France|0.97|0.82|1 - 1|0.97|0.93|0.87|2.77|2.77|2.36|
|Portugal – Holland|1.15|0.98|1 - 0|1.06|0.58|0.44|2.08|1.40|2.44|
|Brazil – France|1.56|0.78|0 - 1|0.57|0.82|0.59|1.98|2.18|2.28|
|England – Portugal *|0.78|1.22|0 - 0|0.46|0.58|0.61|1.65|1.40|2.33|
|Germany – Portugal|1.56|0.93|3 - 1|0.72|0.28|0.60|1.60|1.76|2.40|
|England – Ecuador|1.73|0.64|1 - 0|0.69|0.17|0.64|1.50|1.82|2.08|
|Portugal – France|0.77|1.13|0 - 1|0.73|0.33|0.42|1.48|1.48|2.34|
|Switzerland – Ukraine *|0.90|1.20|0 - 0|0.25|0.45|0.68|1.38|1.41|2.43|
|Germany – Italy *|1.06|0.91|0 - 0|0.66|0.39|0.30|1.35|1.38|2.39|
|Italy – Ukraine|1.43|0.60|3 - 0|0.44|0.15|0.28|0.86|0.91|2.16|
|Germany – Sweden|1.72|0.74|2 - 0|0.39|0.15|0.25|0.79|0.83|2.20|
|Brazil – Ghana|0.50|2.21|3 - 0|0.22|0.07|0.17|0.46|0.57|1.71|



Table: Elimination round games ordered by the excitement level, regulation time plus injury time. Draw was a possible outcome. Games marked by a star ended up with draw, and went into overtime. 



Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Definition Measuring <u>Win</u> Expectancy 

Poisson Model of Scoring 

Examples - FIFA 2006 World Cup Games 

|Game|Score|T1 Advance<br>T2 Advance|Total|
|---|---|---|---|
|England – Portugal *|0 - 0|1.47<br>1.53|3.00|
|Portugal – Holland|1 - 0|1.24<br>1.16|2.40|
|Italy * – France|1 - 1|1.10<br>1.16|2.26|
|Switzerland – Ukraine *|0 - 0|1.14<br>1.02|2.16|
|Germany * – Argentina|1 - 1|1.06<br>1.04|2.10|
|Spain – France|1 - 3|1.00<br>0.92|1.92|
|Italy – Australia|1 - 0|0.74<br>0.76|1.50|
|Brazil – France|0 - 1|0.71<br>0.70|1.41|
|~~Argentina – Mexico~~|~~2 - 1~~|~~0.67~~<br>~~0.55~~|~~1.22~~|
|Germany – Italy|0 - 2|0.57<br>0.56|1.13|
|Germany – Portugal|3 - 1|0.40<br>0.49|0.89|
|Portugal – France|0 - 1|0.48<br>0.40|0.88|
|England – Ecuador|1 - 0|0.41<br>0.38|0.79|
|Italy – Ukraine|3 - 0|0.26<br>0.26|0.52|
|Germany – Sweden|2 - 0|0.22<br>0.20|0.42|
|Brazil – Ghana|3 - 0|0.11<br>0.18|0.29|



Table: Elimination round games ordered by the excitement level, including overtime. Draw was not an option. Games marked by a star went into penalty shootouts. 

# ~~Expected Excitement - Poisson Model~~ 

Probabilistic Excitement of Sports Games 

Jan Vecer 

Motivation 

Measuring <u>Win</u> Expectancy Poisson Model of Scoring Examples - FIFA 2006 World Cup Games 



<!-- Start of picture text -->
3<br>5<br>2<br>4<br>1<br>0 3<br>0<br>1 2 Μ<br>2<br>3 1<br>Λ<br>4<br>5 0<br><!-- End of picture text -->

Figure: Expected excitement as a function of intensities of scoring. 


