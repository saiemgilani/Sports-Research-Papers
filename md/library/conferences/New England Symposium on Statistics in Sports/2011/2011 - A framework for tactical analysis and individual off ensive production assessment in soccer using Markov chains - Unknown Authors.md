<!-- source: library/conferences/New England Symposium on Statistics in Sports/2011/2011 - A framework for tactical analysis and individual off ensive production assessment in soccer using Markov chains - Unknown Authors.pdf -->



## A Framework for Tactical Analysis and Individual Offensive Production Assessment in Soccer Using Markov Chains 

Sarah Rudd On Football Research and Consulting 



# What are we trying to solve? 

- How valuable are certain game situations? 

- How do these values vary across teams and what can we learn from that? 

- Can we quantify how much a player contributes to creating good goal scoring opportunities? 

**2** 

On Football Research and Consulting www.onfooty.com 



# Why is this hard? 

- Hard to capture all of the information about game state; off the ball movement is just as important as on the ball movement 

- Sparse data – we haven’t seen all possible combinations of game situations, and those we have seen only have a few data points 

- How do you divide up credit? 

**3** 

On Football Research and Consulting www.onfooty.com 



# Markov Chains 

- **What do they do?** 

   - Model the likely outcomes after a number of iterations based on the probabilities of transitioning from one state to another 

- **Why are they useful?** 

   - They allow us to look at all the possible ways a possession can unfold 

   - Absorption states means possessions of arbitrary lengths are handled nicely 

#### • **Downside?** 

- Assume that the current state is independent to the previous state (i.e. it doesn’t matter how we got here, the probabilities of moving to the next state are the same regardless of the past) 

**4** 

On Football Research and Consulting www.onfooty.com 



# Dataset 

- Touch-by-touch data provided by StatDNA 

   - _(x,y)_ coordinates 

   - event type 

   - defensive pressure 

   - defensive “state” 

- English Premier League 

   - 2010/11 Season 

   - 123 matches 

      - Minimum of 11 matches per team 

      - ~100,000 “deliberate” actions or about 800 actions per match 

**5** 

On Football Research and Consulting www.onfooty.com 



# States 

- 2 absorbing states: Goal or End of Possession 

- 7 set pieces 

- 30 states defined by zonal location and defensive state 39 total states 

**6** 

On Football Research and Consulting www.onfooty.com 



# Set Pieces 

- Penalty 

- Short Corner 

- Long Corner 

- Short Free Kick 

- Long Free Kick 

- Shallow Throw-in 

- Deep Throw-in 

**7** 

On Football Research and Consulting www.onfooty.com 



# Zones 



**8** 

On Football Research and Consulting www.onfooty.com 



# Crosses (Pressure A) 



> On Football Research and Consulting www.onfooty.com **9** 



# Crosses (Pressure B) 



> On Football Research and Consulting www.onfooty.com **10** 



# Shots 



> On Football Research and Consulting www.onfooty.com **11** 



# Goals 



On Football Research and Consulting www.onfooty.com 

**12** 



# Definitions 

- **Deliberate action** – any action where a player moves the ball in a controlled manner with an attempted outcome 

   - Deliberate: pass, shot, dribble, etc. 

   - Not deliberate: clearance, tackle, etc. 

- **Possession** – a series of consecutive deliberate actions performed by one team, only interrupted by a deliberate action performed by the other team or the end of a half. 

**13** 

On Football Research and Consulting www.onfooty.com 



# Transition Matrices 

- Calculate the probability of moving from state _Sa_ to _Sb_ for all combinations of the 39 states 

- Absorbing states are different, probability of remaining in same state is 1 and moving to another state is 0. 

   - _Once you are there you are stuck!_ 

- Multiplying a transition matrix by itself will give you the probability of ending up in a given state after 1 iteration 

- Multiplication can be repeated until probability of ending in an absorbing state converges ( _n=20_ ) 

**14** 

On Football Research and Consulting www.onfooty.com 



# Transition Matrix 

||End of Pos.|Goal<br>S1|Sn|
|---|---|---|---|
|End of<br>||||
|Pos||||
|.<br>Goal||||
|S1||||
|Sn||||





**15** 

On Football Research and Consulting www.onfooty.com 



# Validation – expected vs. actual 

Monte Carlo Bootstrapping 

K-Fold Validation 

- 1000 samples with replacement 

- 5 folds, 4 training and 1 one evaluation 





























**16** 

On Football Research and Consulting www.onfooty.com 



# Comparing P(Goal) 

- Column are teams ordered by final standing 

- Rows are P(Goal) for each state 

- As you move lower down the table, teams find it harder to score 

- Notable exceptions are Manchester City (3<sup>rd</sup> , underperform offensively) and Wolves (17<sup>th</sup> , overperform offensively) 



**17** 

On Football Research and Consulting www.onfooty.com 



# Results – Set Pieces 

|**State**<br>**P(Goal)**|
|---|
|Penalty<br>71.55%|
|Long Corner<br>2.39%|
|Short Corner<br>1.67%|
|Long Free Kick<br>1.67%|
|Shallow Throw in<br>1.46%|
|Deep Throw in<br>1.09%|
|Short Free Kick<br>1.08%|





**18** 

On Football Research and Consulting www.onfooty.com 



# Corners 

Offensive Probabilities 

##### Defensive Probabilities 









































**19** 

On Football Research and Consulting www.onfooty.com 



# Counter Attacks 



































































**20** 

On Football Research and Consulting www.onfooty.com 



# **Now for the good stuff…** 

**21** 

On Football Research and Consulting www.onfooty.com 



# Not all passes are created equal 

- Existing metrics don’t take into account context of game state 

   - Completed passes: back-pass, square-pass, through-ball that puts teammate 1-on-1 with keeper are all weighted equally 

   - Goals: all are weighted equally, no matter how easy they were to score 

   - Missed opportunities could still show up positively in metrics (i.e. a saved penalty could be considered a shot on target) 

### **Weight each action with incremental improvement of P(Goal)** 

**22** 

On Football Research and Consulting www.onfooty.com 



# How does it work? 

State: Player 1 Player 2 Player 3 Goal State A State B State C Scored P(Goal)= P(Goal)= P(Goal)= P(Goal)= 0.25 0.17 0.28 1 **Player 1: Player 2: Player 3: -0.08 +0.11 +0.72** 

> On Football Research and Consulting www.onfooty.com **23** 



# Another example 



<!-- Start of picture text -->
Player 1 Player 2 State:<br>Player 1<br>Earns  Takes  Penalty<br>State A<br>Penalty Penalty Missed<br>P(Goal)=<br>P(Goal)= P(Goal)= P(Goal)=<br>0.15<br>0.71 0.71 0<br>Player 1:  Player 2:<br>+0.56 -0.71<br>{ {<br><!-- End of picture text -->

Player 1 is rewarded for earning the penalty and Player 2 is heavily penalized for missing it. 

**24** 

On Football Research and Consulting www.onfooty.com 







# Top Performers 





- •Top performers are: 





- •Tim Cahill 



- •Yaya Toure 





- •Cesc Fabregas 







- •Jordan Henderson in top 25 







•Some surprises like James Morrison, Ricardo Fuller and Chris Baird 











> On Football Research and Consulting www.onfooty.com **25** 







# Worst Performers 







- Lots of goal keepers, also strikers and defenders 







- Poor Darren Bent 



- 1 goal was in sample set out of 17 he scored in the entire season 



- Had 19 opportunities where he had the ball with >10% chance of scoring (22% average) but only converted one 



- Clichy/Young/Kolarov – poor crossers of the ball? 







- Can dig deeper into the data to identify which situations 









**26** 

On Football Research and Consulting www.onfooty.com 



## Thank you for listening and special thanks to StatDNA for providing me with awesome data and this wonderful opportunity 

**27** 

On Football Research and Consulting www.onfooty.com 


