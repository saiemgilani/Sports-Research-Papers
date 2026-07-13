<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - The Tennis Formula How it can be used in professional tennis - Unknown Authors.pdf -->

# The Tennis Formula: How it can be used in Professional Tennis 

# A. James O’Malley 

Harvard Medical School Email: omalley@hcp.med.harvard.edu September 29, 2007 

1 

# Overview 

# • Tennis scoring 

# • The tennis formula and its properties 

# • Other tennis-related formulas 

- Applications of tennis formula 

- Future work 

2 

# Scoring in tennis 

- points: love, 15, 30, 40, deuce, advantage. 

- games: love, 1, 2, 3, 4, 5, 6, (7). 

- sets: love, 1, 2, (3). 

- first to win four points or more by margin of two wins the 

   - game. 

- to win six of two or otherwise seven 

- first games by margin wins the set at six 

- games (tiebreaker all). 

- first to win two (or three) sets wins the match. 

3 

# “Tennis Formula” 

- Let p denote the probability that a player wins a single point serving. 

- Assume probability is fixed throughout game (match). 



4 

Tennis formula, its derivative, and integral functions 



<!-- Start of picture text -->
1<br>0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>3<br>2 Derivative function<br>1<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>0.4 Integral function<br>0.3<br>0.2<br>0.1<br>Pr(win if p<=0.5) = 0.0616 Pr(win if p>=0.5) = 0.4384<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Pr(Point)<br>Pr(Game)<br>Derivative<br>Cumulative Probability<br><!-- End of picture text -->

5 

# Properties of tennis formula 

- Asymmetric - point of inflection at p = 0.5. 

# • Monotone increasing 

- Derivative function reveals where improve performance is most 



- Integral function gives probability of winning when serving probability selected at random. 



6 

# Other probabilities 

# • Probability of winning: 

– tie-breaker. 

# – set or match. 

# – from a break down in set. 

- Derive similarly to the tennis formula; using tree diagram/dynamic programming approach. 

7 

# Probability of winning tiebreaker 

- Tie-breaker is longer than a regular service game. 

– Involves both = players serving, q opponents probability of on serve. winning point 

– When = 1 − curve to be than for the q p expect steeper tennis formula. 

8 



<!-- Start of picture text -->
Probability of winning tie−breaker<br>1<br>Pr(Win receiving point)=0.5<br>0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>1<br>Pr(Win serve point)=Pr(Win receiving point)<br>0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>1<br>0.8 Pr(Win serve point)−Pr(Opponent wins serve point)=0.02<br>0.6<br>0.4<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Pr(Win serve point)<br>Pr(Win Tiebreaker)<br>Pr(Win Tiebreaker)<br>Pr(Win Tiebreaker)<br><!-- End of picture text -->

9 

# Probability of winning set and match 

# • Functions of game and tie-breaker winning probabilities. 

# – Thus, also of point-winning probabilities. 

- Interested in how steeply odds favor better player. 

10 



<!-- Start of picture text -->
Probability of winning match<br>1<br>Pr(Win receiving point)=0.5<br>0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>1<br>Pr(Win serve point)=Pr(Win receiving point)<br>0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>1<br>0.9<br>0.8 Pr(Win serve point)−Pr(Opponent wins serve point)=0.02<br>0.7<br>0.6<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Pr(Win serve point)<br>Pr(Win Match)<br>Pr(Win Match)<br>Pr(Win Match)<br><!-- End of picture text -->

11 



<!-- Start of picture text -->
Difference of probabilities over match duration<br>0.06<br>0.04<br>0.02<br>0<br>−0.02<br>−0.04<br>−0.06<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Pr(Win point)<br>Pr(Win | 5 sets) − Pr(Win | 3 sets)<br><!-- End of picture text -->

12 

# Comparison of tennis formula to empirical data? 

- Formula’s are based on assumptions: 

   - Independence between points. 

   - Homogeneous probabilities. 

- Obtained data from Wimbledon 2007 (Mens singles). 

- Compare empirical game winning percentages to predictions. 

13 



<!-- Start of picture text -->
Predicted v. Actual Proportion of Service Games Won<br>1<br>0.95<br>0.9<br>0.85<br>0.8<br>0.75<br>0.7<br>0.65<br>Mean predicted = 0.8236<br>Mean observed = 0.8309<br>0.6<br>t−stat of difference = −0.16<br>0.55<br>0.5<br>0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1<br>Predicted probability<br>Observed proportion<br><!-- End of picture text -->

14 

# Lack of of across homogeneity points game 

- 118 saves out of 208 break points, psave = 0.549. 

- 2,101 out of 3,156 service points won at other stages of game, pother = 0.666. 

- P-value of ≈ 0.0053. 

15 

# Applications of tennis formula 

- By players to focus training efforts. 

- to evaluate where to concentrate match 

- By players preparation. 

- teams to make broadcast more 

- By commentary interesting. 

- Useful in determining effect of a rule change. 

16 

# Training and match preparation 

- of one on serve and while re- 

- Compute proportion points ceiving against all opponents. 

- Evaluate corresponding probabilities of winning a match. 

- Determine if more beneficial to improve serve or return game. 

- Work on improving that aspect of game. 

- Could extend this by averaging over types of opponents (left-handers, right-handers) to obtain more accuracy. 

- Before playing a match analyze head-to-head data. 

17 

# Example 

- Probability win service point = 0.65. 

- Probability win receiving point = 0.37. 

- Probability win 3 set match = 0.5985. 

- focused could serve 

- Suppose training improve probability by 1.1 percentage points or return by 1 percentage point. Where to focus 

- If improve service by 10%: Pr(match) = 0.6497. 

- If improve return by 10%: Pr(match) = 0.6466. 

- Better to improve serve! 

18 

# tennis more Making commentary interesting 

- Report likelihood that each player wins match if: 

– Current point-winning percentage is maintained. – Players revert to historical winning proportions. – Probabilities became equal. 

– Stopped playing and tossed a coin. 

- Calibrate statement “match is effectively over if player A breaks serve”. 

19 

# Chance of winning when break down in final set. Scenario 



<!-- Start of picture text -->
= 0.62 = 0.67 = 0.645 = 0.5<br>p p p p<br><!-- End of picture text -->

||p = 0.62|p = 0.67|p = 0.645|p = 0.5|
|---|---|---|---|---|
|Situation|q = 0.67|q = 0.62|q = 0.645|q = 0.5|
|4-5|0.1420|0.2165|0.1775|0.2500|
|3-5|0.0880|0.1451|0.1145|0.1250|
|2-5|0.0546|0.0972|0.0738|0.0625|
|3-4|0.2033|0.3038|0.2513|0.3125|
|2-4|0.1371|0.2217|0.1765|0.1875|
|1-4|0.0850|0.1486|0.1139|0.0938|
|2-3|0.2350|0.3526|0.2914|0.3438|
|1-3|0.1675|0.2716|0.2162|0.2266|
|0-3|0.1145|0.2006|0.1538|0.1367|





<!-- Start of picture text -->
Situation = 0.67 = 0.62 = 0.645 = 0.5<br>q q q q<br>4-5 0.1420 0.2165 0.1775 0.2500<br>3-5 0.0880 0.1451 0.1145 0.1250<br><!-- End of picture text -->



<!-- Start of picture text -->
2-5 0.0546 0.0972 0.0738 0.0625<br>3-4 0.2033 0.3038 0.2513 0.3125<br>2-4 0.1371 0.2217 0.1765 0.1875<br><!-- End of picture text -->



<!-- Start of picture text -->
1-4 0.0850 0.1486 0.1139 0.0938<br>2-3 0.2350 0.3526 0.2914 0.3438<br>1-3 0.1675 0.2716 0.2162 0.2266<br><!-- End of picture text -->



<!-- Start of picture text -->
0-3 0.1145 0.2006 0.1538 0.1367<br><!-- End of picture text -->

20 

# Rule change 

# • In 1999 a change in the scoring of tennis was proposed. 

- Replace deuce-advantage system with sudden death. 

- At deuce the next point decides the game. 

- Pete Sampras was against, Andre Agassi supported, the change. 

21 

# New Tennis formula 

# • of under new Probability winning game scoring system changes to: 

pr(game − new) = p<sup>4</sup> +4p<sup>4</sup> (1 − p)+10p<sup>4</sup> (1 − p)<sup>2</sup> +20p<sup>4</sup> (1 − p)<sup>3</sup> 

- Compute change in probability of winning match. 

22 

# Sampras-Agassi Data (from 1999) 



|Statistic|Sampras|Agassi|
|---|---|---|
|Serving point|0.709|0.657|
|Return point|0.371|0.418|
|Pr(Win match - new)|0.8210|0.8092|
|Pr(Win match - old)|0.8331|0.8296|
|Net gain|-0.0121|-0.0205|





<!-- Start of picture text -->
Serving point 0.709 0.657<br><!-- End of picture text -->



<!-- Start of picture text -->
Return point 0.371 0.418<br>-<br>Pr(Win match new) 0.8210 0.8092<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>Pr(Win match old) 0.8331 0.8296<br><!-- End of picture text -->



23 

# Future work 

- 

- • More realistic models allow probabilities to vary through stages of match. 

   - At deuce, on break- or set-points, between sets. 

- Use models to examine player performance at crucial stages of a match. 

   - When to be most wary or optimistic against certain opponents. 

24 


