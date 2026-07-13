<!-- source: library/conferences/New England Symposium on Statistics in Sports/2013/2013 - The Hot Hand A New Approach to an Old 'Fallacy' - Unknown Authors.pdf -->

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 



<!-- Start of picture text -->
5<br><!-- End of picture text -->

> 5 Testing for the Hot Hand 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

> 6 Conclusions 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>2 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# What is the Hot Hand? 

In the context of basketball, the _Hot Hand_ is the belief that a player who has made several of his past shots is more likely to make his next shot. In other words, shots are not independent events - the likelihood of make depends on the outcome of past shots. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 3 / 28</mark> 

<mark>The Hot Hand</mark> 

# The Hot Hand is a Fallacy... 

The Hot Hand has been disproven in academic literature: 



Most famously by Gilovich, Vallone, and Tversky in 1985 (“The Hot Hand in Basketball: On the Misperception of Random Sequences”) 

- Authors show that _P_ ( _Hit_ ) does not vary conditional on the number of consecutive hits or misses. 

- The length of “streaks” observed is consistent with the expected length under the assumption of independence. 

- There is no streakiness in free-throw shooting. 



Subsequent studies have provided additional evidence that these results hold. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>4 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# The Hot Hand is a Fallacy... 

And is accepted as a fallacy by the academic community: 



- This past winter, Larry Summers addressed the Harvard basketball team after one of their practices. 

   - He asked them if they believed in the Hot Hand. After they nodded, he told them they were wrong. “People apply patterns to random data” he explained. 



In February, David Brooks wrote a NYT op-ed about the philosophy of big data. In it, he uses the Hot Hand as an example of when our intuition leads us astray. 

- “When a player has hit six shots in a row, we imagine that he has tapped into some elevated performance groove. In fact, its just random statistical noise, like having a coin flip come up tails repeatedly. Each individual shots success rate will still devolve back to the players career shooting percentage.” 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 5 / 28</mark> 

<mark>The Hot Hand</mark> 

...Or is it? 

The famous Gilovich, Vallone, and Tversky results hinge on one critical assumption: 

_“It may seem unreasonable to compare basketball shooting to coin tossing because a player’s chances of hitting a basket are not the same on every shot. Lay-ups are easier than 3-point field goals and slam dunks have a higher hit rate than turnaround jumpers. Nevertheless, the simple binomial model is equivalent to a more complicated process with the following characteristics: Each player has an ensemble of shots that vary in difficulty (depending, for, example, on the distance from the basket and on defensive pressure), and each shot is randomly selected from this ensemble.”_ 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>6 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

...Or is it? 

This is the assumption we challenge in our paper. 

If players believe in the Hot Hand, their perception of heat may affect the difficulty of the shots they select. If hot players select more difficult shots, this could the of heat. 

Therefore, the question we seek to answer is twofold: 

> 1 Do players attempt more difficult shots as they become hotter? 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- 2 Are hot players more likely to make their next shot, _controlling for the difficulty of that shot?_ 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 7 / 28</mark> 

<mark>The Hot Hand</mark> 

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 



<!-- Start of picture text -->
5<br><!-- End of picture text -->

> 5 Testing for the Hot Hand 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

> 6 Conclusions 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>8 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Raw Data 

We were able to obtain and merge data from four different sources: 

> 1 **NBA Roster:** Player traits, including height, weight, and position 

> 2 **NBA Expanded Play-by-Play:** Lists all major events in the game, with additional data such as the time and player(s) associated with the event 



<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
3<br><!-- End of picture text -->

- 3 **SportVU Optical Tracking:** Spatial data that includes _x, y , z_ coordinates for each player and the ball in 1/25 of second increments 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 **SportVU Play-by-Play Optical:** This dataset has a unique sequence number that matches events in the NBA Play-by-Play data to the SportVU Optical Tracking data 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>9 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Data by the Numbers 

















6 cameras on each court 15 arenas with cameras (50% of total) 30 teams all with partial data 474 players with shots taken ˜3,500 data events per game 83,000 shots attempts in 2012-2013 season ˜1 million optical observations per game. 600+ million optical observations in our dataset. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 10 / 28</mark> 

<mark>The Hot Hand</mark> 

# Shot Log 

We used this data to compile a shot log. For every shot attempted, we had data on: Shot Conditions: Shot location, Shot Type (13 mutually exclusive categories), etc. Game Conditions: Score differential, time remaining, quarter, etc. Defensive Conditions: Locations of all defenders, defender angle, etc. From these datapoints, we can further extrapolate other variables, such as measures of defensive pressure. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 11 / 28</mark> 

<mark>The Hot Hand</mark> 

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 



<!-- Start of picture text -->
5<br><!-- End of picture text -->

> 5 Testing for the Hot Hand 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

> 6 Conclusions 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>12 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Measuring Shot Difficulty 

To measure shot difficulty, we came up with a model that predicts the probability that player _i_ makes shot _s_ : 

ˆ _Pis_ = _α_ + _β ∗_ ( _Game Condition Controlsis_ ) + _γ ∗_ ( _Shot Controlsis_ ) + _δ ∗_ ( _Defensive Controlsis_ ) + _θ ∗_ ( _Player Fixed Effectsi_ ) 

_P_ ˆ gives us a single number that is easily interpretable and encapsulates the overall difficulty of a given shot. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 13 / 28</mark> 

<mark>The Hot Hand</mark> 

# Testing the Model 

To test the accuracy of the model, we ran it on a randomized training set. We then applied the model on the remaining data to predict the _P_<sup>ˆ</sup> ’s. The figure below compares the predicted and actual make percentages: 



<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 14 / 28</mark> 

<mark>The Hot Hand</mark> 

# Measuring Heat 

How do we define a player’s heat? We use two distinct methods: 

- 1 **Simple Heat** _n_ measures a player’s shooting percentage over his past _n_ shots. 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> ▶ _Example:_ If a player made 3 out of his past 4 shots, then Simple Heat4 =<sup><u>3</u></sup> 4<sup>= 0</sup><sup>_._75</sup> 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- 2 **Complex Heat** _n_ measures the difference between a player’s actual and _P_ ˆ valuesexpectedof thoseshootingshots.percentage over the past _n_ shots, based on the 

> ▶ _Example:_ If a player made 3 out of his past 4 shots, and those shots had _P_<sup>ˆ</sup> of 0.1, 0.5, 0.8, and 0.6 then Complex Heat4 = 4<sup><u>3</u></sup><sup>_−_</sup> � <u>0</u> _<u>.</u>_ <u>1+0</u> _<u>.</u>_ <u>5+04</u> _<u>.</u>_ <u>8+0</u> _<u>.</u>_ <u>6</u> � = 0 _._ 75 _−_ 0 _._ 5 = 0 _._ 25 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 15 / 28</mark> 

<mark>The Hot Hand</mark> 

# Complex Heat is the Better Measure 

Though perhaps less intuitive, we argue that Complex Heat is a better measure of heat. 





It measures _true_ overperformance - a player who goes 2 for 3 from the 3-point line is “hotter” than the player who makes 2 out of 3 layups. It controls for serial correlation betweens shots: 

_Complex Heat_ = _Actual Pct. − Expected Pct._ = _Simple Heat − Expected Pct._ � <u>�� �</u> difficulty of past shots 

_Example:_ A player is covered by a short defender. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 16 / 28</mark> 

<mark>The Hot Hand</mark> 

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 

> 5 Testing for the Hot Hand 

> 6 Conclusions 



<!-- Start of picture text -->
5<br><!-- End of picture text -->



<!-- Start of picture text -->
6<br><!-- End of picture text -->

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>17 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Do Players Believe in the Hot Hand? 

If players believe in the Hot Hand, they will adjust their play accordingly. Do hot players take shots from further away? Do defenders cover hot players more closely? Are hot players more likely to take their team’s next shot? Does overall shot difficulty increase with heat? 

If players do believe in the Hot Hand, we would expect that the answers to these questions are yes. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 18 / 28</mark> 

<mark>The Hot Hand</mark> 

# Empirical Strategy 

_Shot Distanceis_ = _α_ + _β ∗_ ( _Heatis_ ) + _γ ∗_ ( _Controlsis_ ) + _θ ∗_ ( _Player Fixed Effectsi_ ) _Defender Distanceis_ = _α_ + _β ∗_ ( _Heatis_ ) + _γ ∗_ ( _Controlsis_ ) + _θ ∗_ ( _Player Fixed Effectsi_ ) _P_ ( _Sameis_ ) = Φ( _α_ + _β ∗_ ( _Heatis_ ) + _γ ∗_ ( _Controlsis_ ) + _θ ∗_ ( _Player Fixed Effectsi_ )) ˆ _Pis_ = _α_ + _β ∗_ ( _Heatis_ ) 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 19 / 28</mark> 

<mark>The Hot Hand</mark> 

# Results 

The results suggest that players do believe in the Hot Hand, and alter their play to reflect these beliefs. 

|VARIABLES|(1)<br>Distance|(2)<br>Distance|(3)<br>(4)<br>Defender Distance<br>P(Same)|(5)<br>P(Same)|
|---|---|---|---|---|
|Simple Heat (4)|2.385***<br>(0.186)||0.0578***<br>(0.00871)||
|Complex Heat (4)||2.240***<br>(0.185)|-0.151***<br>(0.0397)|0.0637***<br>(0.00909)|
|Constant|7.249***<br>(0.289)|8.387***<br>(0.266)|4.123***<br>(0.135)||
|Observations<br>_R_<sup>2</sup>|45,123<br>0.290<br>|45,047<br>0.289<br>|45,047<br>45,115<br>0.161<br>|45,039|
||Robu|st standard <br>*** p_<_0.01, *|errors in parentheses<br>* p_<_0.05, * p_<_0.1||
||Response<br>|Raw<br>|Efect Size<br>% Efect Size<br><br>||
||Shot Distance<br>||7.0 in<br>4.6%<br><br>||
||Defender Dist<br>P(Take Next|ance<br>Shot)|0.5 in<br>1.0%<br>1.4%<br>7.2%||



These effect sizes reflect a player making an additional shot of his last four attempts. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 20 / 28</mark> 

<mark>The Hot Hand</mark> 

# Results - Individual Player Evidence 





<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 21 / 28</mark> 

<mark>The Hot Hand</mark> 

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 



<!-- Start of picture text -->
5<br><!-- End of picture text -->

> 5 Testing for the Hot Hand 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

> 6 Conclusions 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>22 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Testing for the Hot Hand 

We have established that heat affects shot selection. This proves that critical Tversky assumption of “random shot selection” does not hold. Next, we want to see if after controlling for shot difficulty, a Hot Hand effect does emerge. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 23 / 28</mark> 

<mark>The Hot Hand</mark> 

# Empirical Strategy 

Baseline specification (no difficulty controls): 

_P_ ( _Makeis_ ) = _α_ + _β ∗_ ( _Heatis_ ) + _θ ∗_ ( _Player Fixed Effectsi_ ) 

Difficulty-controlled specification: 

_P_ ( _Makeis_ ) = _α_ + _β ∗_ ( _Heatis_ ) + _γ ∗ P_<sup>ˆ</sup> _is_ 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 24 / 28</mark> 

<mark>The Hot Hand</mark> 

# Results - Simple Heat 

When we do not control for difficulty, we do not find evidence of the Hot Hand. 



Simple Heat does not control for within-player variation. 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 25 / 28</mark> 

<mark>The Hot Hand</mark> 

# Results - Complex Heat 

When we control for difficulty and use Complex Heat, a positive and significant Hot Hand effect emerges. 



<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 26 / 28</mark> 

<mark>The Hot Hand</mark> 

# Table of Contents 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

> 1 Introduction 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

> 2 Data 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

> 3 Empirical Preliminaries 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Do Players Believe in the Hot Hand? 



<!-- Start of picture text -->
5<br><!-- End of picture text -->

> 5 Testing for the Hot Hand 



<!-- Start of picture text -->
6<br><!-- End of picture text -->

> 6 Conclusions 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>27 / 28</mark> 

<mark>September 21, 2013</mark> 

<mark>The Hot Hand</mark> 

# Conclusions 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

- 1 Players believe in the Hot Hand and act accordingly. 

   - They take shots from further away 

   - Defenders cover them closer 

   - They are more likely to take their team’s next shot 

   - They take more difficult shots (controlling for the difficulty of their prior shots) 

- 2 Players who are hot (outperforming given the difficulty of the shots they have taken) are more likely to make their next shot, controlling for their next shot’s difficulty. 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- Said differently, the Hot Hand emerges when we control for both past and current shot difficulty 

<mark>Bocskocsky, Ezekowitz, and Stein (Harvard)</mark> 

<mark>September 21, 2013 28 / 28</mark> 

<mark>The Hot Hand</mark> 


