<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - A Markov Model of Football Using Stochastic Processes to Model a Football Drive - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1400 

## A Markov Model of Football: Using Stochastic Processes to Model a Football Drive 

**Keith Goldner,** _Northwestern University_ 

©2012 American Statistical Association. All rights reserved. DOI: 10.1515/1559-0410.1400 

## A Markov Model of Football: Using Stochastic Processes to Model a Football Drive 

### Keith Goldner 

### **Abstract** 

A team is backed into a 4th-and-26 from their own 25, down 3 points. What are the odds that drive ends in a field goal? In the 2003 playoffs, Donovan McNabb and the Eagles scoffed at such a probability as they converted and ultimately kicked a field goal to send the game into overtime. This study creates a mathematical model of a football drive that can calculate such probabilities, labeling down, distance, and yard line into states in an absorbing Markov chain. The Markov model provides a basic framework for evaluating play in football. With all the details of the model—absorption probabilities, expected time until absorption, expected points—we gain a much greater situational understanding for in-game analysis. 

**KEYWORDS:** stochastic processes, football, markov chain 

**Author Notes:** I would like to give a special thanks to Elton Hsu, Thomas Severini and David McClendon for all their help throughout the course of my research. In addition, I want to thank Albert Lyu for generously providing data. 

Goldner: A Markov Model of Football 

### **Introduction** 

After an 11-yard sack, Donovan McNabb and the Philadelphia Eagles were backed up to their own 25-yard line.  Down 17-14 to the Green Bay Packers with 1:12 remaining in the game, the top-seeded Eagles were on the verge of being eliminated from their first game in the 2003 playoffs.  On 4<sup>th</sup> -and-26, the Eagles call for a 25-yard slant.  McNabb drops back and throws a bullet to Freddie Mitchell in stride, converting and laughing in the face of probability<sup>1</sup> .  The Eagles then drove down the field and kicked a field goal, sending the game into overtime - where they would eventually win.  What are the odds that a drive containing a 4<sup>th</sup> and-26 from the 25 would end with a successful field goal? According to our model, a whopping 1 out of 175. 

A football team’s ultimate goal is to win.  Each season is divided into games, each game is divided into drives, and each drive is divided into plays.  The goal of this study is to use a mathematical model known as a stochastic process— more specifically, a Markov chain—to model a football drive. 

Each drive has a finite number of states.  A state is defined by down (1-4), distance to a first down (1-100), and yard line (1-99).  Each drive can only end in a finite number of ways as well: scoring play, giving the ball back to the other team, the end of the half or game.  Through this study, we will determine the probability of a drive ending in any number of ways based on the team being in any situation on the field.  For example, we can estimate a team’s chances of scoring a touchdown given that they have a 2<sup>nd</sup> down-and-4 to go on their own 40-yard line. 

From these probabilities, we will also be able to determine the expected number of plays a team will run before the drive ends.  In addition, we can create a model of expected points for every state.  That is, we can assign a value to every down, distance, and yard line that represents the expected number of points a team will score.  Expected points are extremely beneficial in measuring the efficiency of plays, players, and teams. 

The mathematical model can be used to give a greater understanding of a team’s position in a drive since it encompasses every possible situation.  From there, it can be used to optimize strategic decisions like play calling based on the probabilities and expected points.  With proper data, our model can be fit to measure specific play calling, players or teams. 

> 1 4th-and-26 video can be found here: http://www.youtube.com/watch?v=QOEq7p4r00U 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **Markov Models Across Sports** 

Markov models are commonly used to model sports, as there is typically a statedependent nature to games.  Whether it is modeling the score or in-game situation, estimating future outcomes enables higher quality decision-making. Paul Newton and Kamran Aslam developed a Markov model of tennis to predict game, set, and match winners based on four inputs—probability of winning a serve, winning a return, consistency on serve and return (Newton 2009). Similarly, Mark Pankin, among others, created a Markov model of baseball (Pankin 1985).  Baseball is inherently state-based and thus, lends itself to stochastic modeling.  States are determined by outs and base runners.  In more complex models, inning, score, and even pitch count are taken into account.  The primary goal of baseball modeling is to calculate the expected number of runs to be scored given any situation.  From this data, analysts can determine a player’s contribution above or below league average by comparing actual runs contributed versus expectation.  We will develop a parallel to expected runs from our football model, called expected points. 

### **Stochastic Processes & Markov Chains** 

A stochastic process is “any process in nature whose evolution we can analyze successfully in terms of probability” (Doob 1996).  That is, a process for which we do not know the outcome but can make estimates based on the probability of different events occurring over time.  A primary example of a stochastic process is the Markov chain.  The essence of a Markov chain is that the next state depends only on the current state (the Markov property, seen in equation **(1)** ); all previous events have no effect on the future of the chain. 

### **(1) P(Xn+1 = x | X1 = x1, … , Xn = xn) = P(Xn+1 = x | Xn = xn)** 

This equation simply means that the probability of event **_n + 1_** (the next event) being **_x_** given that we know all previous events **_1, 2, 3, … n_** , is the same as just knowing event **_n_** (the most recent event).  A good example of this is flipping a coin repeatedly, where the state is the number of heads observed.  If the number of heads is 60 after 100 flips, we do not know what this total will be after the 101<sup>st</sup> flip, but we can estimate based on probability—making this a stochastic process. Further, it does not matter what the total was after the 1<sup>st</sup> flip, the 20<sup>th</sup> flip, or the 99<sup>th</sup> flip; all we need to know is the total after the 100<sup>th</sup> flip in order to estimate the 101<sup>st</sup> flip—making this a Markov chain. 

We are specifically dealing with a discrete-time Markov chain with a finite number of states.  Discrete-time means that the process can be divided into 

2 

Goldner: A Markov Model of Football 

specific steps—in our case, plays, in the previous example, flips of a coin.  In football, if a team is in a certain situation, what happened previously has no effect on what will happen next.  For example, if we have a 1<sup>st</sup> -and-10 from our own 20, it does not matter if the previous play was a kickoff for a touchback or a 10-yard gain for a first down after a 3<sup>rd</sup> -and-10 from the 10-yardline.  Either way, we now have a new situation that will only directly affect the next play.  To qualify this, previous play-calls may affect future decision-making beyond the most recent play.  For example, if a team runs the ball several times to set up a play-action pass, that affects the probability of success on the play.  This, however, is determined almost entirely by game theory.  If we disregard specific play calling—as run and pass are not variables in the model—only a team’s current down, distance, and yard line determine the probability of future events in a drive. That is, the probability of going to any other state (which is only defined by down, distance, and yard line) is dependent only on the current, or most recent state. 

A football drive can be seen as an _absorbing Markov chain_ .  In an absorbing Markov chain, there is a set of special states known as absorbing states. The main distinction of an absorbing chain is that as time goes to infinity—in our case, as the number of plays in a drive gets higher—the probability of ending up in one of the absorbing states goes to 1.  Since a drive can only end in a specific number of ways, and a drive _must_ end, these drive-endings are the absorbing states.  Specifically, it is impossible to leave an absorbing state.  Once a team scores a touchdown, they cannot leave that state, the drive ends and the Markov chain is absorbed. 

In order to define a Markov chain, we must know the _transition probabilities_ .  A transition probability is the probability of going from one state to another in one step (seen in **(2)** ): 

### **(2) Px,y = Probability of going from state ‘x’ to state ‘y’ in one step** 

In a Markov chain with a finite number of states, like ours, these probabilities can be written in the form of a _transition matrix_ , seen below in **(3).** 

### **(3) Transition matrix for Markov chain with ‘n’ states:** 



3 

_Submission to Journal of Quantitative Analysis in Sports_ 

From these transition probabilities we can determine the probability of being absorbed into any of the absorbing states.  In addition, we can estimate the expected number of plays before being absorbed. 

### **Data** 

For this study, we used play-by-play data from the last 5 seasons (2005-2009). This includes about 200,000 plays, 30,000 drives, and 1,280 games<sup>2</sup> .  Play-byplay data was checked for accuracy against Pro-Football-Reference.com to ensure proper totals for categories like touchdowns, field goals, safeties, etc… 

### **A Mathematical Model of Football** 

The first step was to divide a drive into all possible situations and label them as distinct states.  The non-absorbing—non-drive-ending states, also known as transient states—were determined by down, distance-to-go, and yard line.  The field was divided into 20 zones, one for every 5 yards.  Similarly, the distance-togo was split into 5-yard increments<sup>3</sup> .  This was done to ensure high enough frequencies for every state; if there were any states that never occurred in a game in the past 5 years, it would detract from the accuracy of the model.  The range of frequencies was 6 to 6624, with an average of about 550 visits to each state. There were a total of 340 transient states. 

There are 9 possible drive-ending scenarios fitting into the three categories listed above: scoring, giving the ball back, end of half or game.  The absorbing states are as follows: touchdown, field goal, safety, missed field goal, fumble, interception, turnover on downs, punt, end of half or game. 

With this list of 349 states, we parsed the play-by-play to determine the start state and end state of every single play.  From here, we can calculate the transition probabilities for all states and create our transition matrix.  We looked at all the actual transitions of a specific start state—which end states the start state led to directly.  In other words, if we were in state **_x_** 100 times, 40 times we went to state **_y_** , 60 times we went to state **_z_** then the transition probabilities are **Px,y = 0.4, Px,z = 0.6** . 

These transition probabilities were then placed into a matrix with 349 rows and 349 columns, with the first 340 entries as the transient states and the last 9 as the absorbing states.  Thus, we have a transition matrix with entry **_(i,j)_** as the probability of going from state **_i_** to state **_j_** in one step.  Since a team cannot start in one of the absorbing states, the first 340 columns of the last 9 rows will all be 0. Similarly, since a team cannot leave an absorbing state, the last 9 columns of the 

> 2 Data was generously provided by Albert Lyu and AdvancedNFLStats.com 

> 3 All distance-to-go greater than 20 yards was lumped into one increment 

4 

Goldner: A Markov Model of Football 

last 9 rows will be all 0s except for a diagonal of 1s representing the probability of 1 going from an absorbing state to itself.  The general form of a transition matrix for an absorbing Markov chain with **_n_** transient states and **_r_** absorbing states can be seen in **Table 1** by partitioning the aforementioned matrix **P** into four parts (Grinstead 1997) **:** 

||**Table 1: Absorbing Transition Matrix**<br>_Partition of n x n transition matrix P by absorbing and transient states_<br> <br>|
|---|---|
||**Transient**<br>**Absorbing**|
|**Transient**|**Q**<br>**(****_n_ x****_n_) **<br>**R**<br>**(****_n_ x****_r_) **|
|**Absorbing**|**0**<br>**(****_r_ x****_n_) **<br>**I**<br>**(****_r_ x****_r_) **|



The whole transition matrix has **_n + r_** rows and columns, but can be divided into these four sub-matrices: **_Q, R, 0, I_** (the dimensions of which are labeled in **Table 1** ). 

### **Absorption Probabilities** 

In order to calculate absorption probabilities, we must perform some matrix manipulation.  As seen above, the transition matrix can be divided into 4 distinct segments—sub-matrices.  We attain a 340-row, 9-column matrix, **_B_** , with absorption probabilities from each state from equation **(5)** . 

### **(5)** **_B_ = [(I – Q)**<sup>**-1**</sup> **]*R** 

Here, **_I_** is a 340x340 identity matrix.  That is, entry **_(i,j)_** = 0 for all **_i,j_** unless **_i_** = **_j_** ; if **_i_** = **_j_** , **_(i,j)_** = 1.  An example of the absorption probabilities can be found at the end in **Table 3** .  The absorption probabilities for 1<sup>st</sup> -and-10 or 1<sup>st</sup> -and-Goal can be seen in **Figure 1.** 

Notice the three primary states that are affected: touchdown, field goal, and punt. As we approach the opponent’s goal line, touchdown and field goal probabilities increase dramatically, while punt probability decreases. Once a team reaches first down inside about the 10-yard line, field goal probability drops due to a precipitous increase in touchdowns. Similarly, we can look at the absorption probabilities on 4<sup>th</sup> down in **Figure 2** . 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 



**Figure 1** _shows the estimated transition probabilities from the Markov model including all nine absorbing states on 1_<sup>_st_</sup> _-and-10 or 1_<sup>_st_</sup> _-and-Goal based on the yards from the opponent's goal line._ 

On 4<sup>th</sup> down, both missed field goal and turnover-on-downs probabilities change significantly. We see an increase around the 30-yard line, as expected, when coaches have to make the tough decision whether to punt, kick a long field goal, or go for it. At this same spot on the field there is a steep, inverse change between punt probability and field goal probability. 

### **What do absorption probabilities tell us?** 

In other words, how can a team benefit from this?  Most great football minds have a general idea of how a drive will end up; coaches and strategists have an innate understanding of these probabilities.  But by assigning values to every single situation, we provide a framework for much greater detailed analysis of in-game play.  We know a good portion of 1<sup>st</sup> -and-10 situations from our own 20 will end in a punt, but now we know the exact probability around the league—49.8%.  A coach can then look at every time his team was in this situation versus how many times the team punted, to evaluate the efficiency of his team in that specific game situation.  Additionally, we can determine how many points a team is expected to score, which we will discuss in greater detail later.  Comparing a team’s past 

6 

Goldner: A Markov Model of Football 



**Figure 2** _displays the average absorption probabilities on 4_<sup>_th_</sup> _-down based on yards from opponent’s goal line for all nine absorbing states. Distances-to-go are grouped together due to the low frequency of 4_<sup>_th_</sup> _downs._ 

performance—whether one’s own team or the opponent—in certain situations versus the league expectation (those values from our model) creates a greater understanding for where that team is successful and unsuccessful.  The model, with additional data, can be tailored to a specific team, offense/defense, and ingame strategy like run versus pass or individual play calling.  For example, if we add in play-call as an additional indicator variable for run and pass, we could determine how efficient it is to run or pass based on the down, distance, and yard line. 

### **Accuracy of Absorption Probabilities** 

Since our transition probabilities were determined by actual data, the absorption probabilities will reflect actual team performance over the last 5 years. **Figure 1** behaves exactly as we would expect it to: punt probability decreases as we approach the opponent’s end zone while field goal and touchdown probabilities increase.  Once we reach the 10-yard line, field goal probability decreases due to a precipitous increase in touchdown probability—teams begin to go for it more often at this point. 

We can, however, assess the validity of our absorption probabilities.  Let’s take three random scenarios over the 2005-2009 time period: **(1)** 1<sup>st</sup> -and-10, 80 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 

yards from the opponent’s end zone, **(2)** 2<sup>nd</sup> -and-5, 40 yards from the opponent’s end zone, **(3)** 3<sup>rd</sup> -and-1, 15 yards from the opponent’s end zone. 

In situation **(1)** , the greatest difference in any of the 9 absorption probabilities is for Field Goals.  The Markov Model predicts that 9.3% of drives containing a 1<sup>st</sup> -and-10 from a team’s own 20 will end in a field goal; in reality, 10.3% of these drives ended in field goals, a difference of 1.0%.  The average deviation between actual results and the Markov probabilities is 0.45%. 

For situation **(2)** , the largest deviation from reality comes from drives ending in touchdowns.  Here, the sample size is a little smaller—a frequency of 69—so we will include 2<sup>nd</sup> -and-5 from the opponent’s 43 through 37, which gives us a higher frequency of 345. The Model indicates that teams would score a touchdown on 30.0% of drives but in reality, touchdowns were scored on 31.3% of drives, a difference of 1.3%; the average deviation among absorbing states is 0.78%. 

Last, we will look at situation **(3)** .  Again, we have a sample size issue of only 45 such situations occurring, so we will include 3<sup>rd</sup> -and-1 from the opponent’s 18 through 12, giving us a slightly better frequency of 235.  Here, the biggest difference is also in touchdowns scored.  The model estimates 37.9% of drives containing a 3<sup>rd</sup> -and-1 from the 15 will end in touchdowns, but over the 5- year period, 45.1% of those drives actually resulted in touchdowns, a difference of 7.2%.  The average deviation for situation **(3)** was 1.9% among the absorbing states. 

The difference in touchdown probability for situation **(3)** is mirrored by field goal probability. Field Goals were converted 6.8% less than expected by the model, which would lead to the conclusion that teams were converting to a new set of downs more frequently than the model suggests.  This makes sense since the model groups 3<sup>rd</sup> -and-1 in with 3<sup>rd</sup> -and-5, with conversion becoming less and less likely as the yards-to-go increases. 

So, what is the actual difference between a 3<sup>rd</sup> -and-1 and a 3<sup>rd</sup> -and-5 across the field? This is important to know since our model groups the two together to ensure high enough frequencies.  Out of all the grouped distances-togo, 3<sup>rd</sup> -and-1 to 3<sup>rd</sup> -and-5 is the most questionable.  We would expect the biggest differences to be when a team could easily convert on 3<sup>rd</sup> -and-1 versus 3<sup>rd</sup> -and-5, which leaves us with three primary absorbing states—touchdown, field goal, punt. The average deviation between actual results in these two situations across the field is 5.5% with the largest being punt (11.2%), touchdown (10.9%) and field goal (9.2%).  No other absorbing state has a deviation over 5%.  While clustering these distances-to-go is not optimal, it is necessary to ensure high enough frequencies.  As a result, when using these results for analysis, the probabilities and expected points can be adjusted slightly for touchdowns, field goals, and punts accordingly.  We know that converting a 3<sup>rd</sup> -and-1 will be easier, so the 

8 

Goldner: A Markov Model of Football 

corresponding touchdown probabilities will increase for 3<sup>rd</sup> -and-1 situations above the results from the model. 

### **Expected Absorption Time** 

Using our initial transition matrix, we can make a simple calculation to determine the expected number of steps before absorption.  That is, formula **(6)** gives an estimate for the length of remaining plays in a drive given that a team is in a specific state (Grinstead 1997). 

### **(6)** **_t_ = [(I – Q)**<sup>**-1**</sup> **]** **_c_** 

Vector **_t_** has 340 entries, each of which gives the expected number of plays before the chain is absorbed into a drive-ending state. **_c_** is a vector with 340 entries, all of which are 1.  More specifically, we are summing the rows of matrix **(I – Q)**<sup>**-1**</sup> . For some situations, this may seem meaningless—obviously on a 4<sup>th</sup> -andextremely long, the drive should only last 1 more play.  But, for example, knowing that a 2<sup>nd</sup> -and-7 from the opponents 32 should last approximately 4.36 more plays can help the play-calling process.  As mentioned, using all the information from the Markov chain can help build a basic structure for evaluation and decision-making.  The maximum expected time of absorption is 7.57 plays (for 1<sup>st</sup> -and-5 from a team’s own 16-20) and the minimum is 1 play.  Examples of expected number of plays before absorption can be found in **Table 3** . 

### **Expected Points** 

The idea of expected points was first developed by Virgil Carter in “ _Operations Research_<sup>_4_</sup> ” and was refined in _The Hidden Game of Football_ (Carroll, et al. 1989).  More recently, studies have attempted to better estimate expected points after the realization that there is not a linear relationship between field position and expected points<sup>5</sup> .  The general concept is that for every down, distance, and yard line, we can assign a numeric value that represents the expected number of points a team will score. In other words, we have a function of the form **_EP = f(down, distance, yard line)_** .  This can be calculated in two ways: using empirical game data and using the Markov model.  Generally, these values are determined as follows (empirically):  for down **_x_** , distance **_y_** , and yard line **_z_** , we look at every time a drive contained that situation in the play-by-play over several years and divide the total points scored over those drives by the number of drives in which 

> 4 Published with the Cincinnati Bengals in 1971 

> 5 Including Brian Burke at advancedNFLstats.com, Aaron Schatz at FootballOutsiders.com, and Ben Alamar author of _“Measuring Risk in NFL Playcalling”_ 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

our situation showed up.  For example, if 1<sup>st</sup> -and-10 from our own 20 showed up in 100 drives, and 14 of those drives scored touchdowns, 9 scored field goals, and 1 was a safety, the expected points will be: 

### **EP1,10,20 =** **_f(_ 1,10,20) = 14*7 + 9*3 + (-2)*1 = 123 / 100 = 1.23 expected points** 

A team gains 7 points for a touchdown, 3 for a field goal, and loses 2 for a safety since the other team gets 2 points<sup>**6**</sup> .  The division by 100 represents the total number of drives during which our situation occurred. For our Markov expected points model, we use the absorption probabilities rather than making calculations directly from the play-by-play.  For each state, we use equation **(7)** : 



Here ρ **v,a** represents the probability of being absorbed in drive-ending state **_a_** given that a team is in state **_v_** . **_v_** is a vector made up of down **_x_** , distance-to-go **_y_** , and yard line **_z_** .  For the above example of 1<sup>st</sup> -and-10 from the team’s own 20, if we use our model we get the following value: 

### **EP1,10,20 =** **_f(_ 1,10,20) = 0.138*7 + 0.093*3 + (-2)*0.002 = 1.24 expected points** 

Examples of the expected points can be found in **Table 3.** Since we are dealing with matrix manipulation, the expected points for every state can be found by multiplying the absorption probability matrix, **B,** by vector **A** , where vector **A** is made up of the values for each absorbing state—these values are 7 for a touchdown, 3 for a field goal, and -2 for a safety. The resulting vector will have the expected points for every state. 

> 6 In reality, we use 6.96 for the touchdown since there is a 96% chance of making the extra point and it is extremely rare that teams go for a two-point-conversion. 

10 

Goldner: A Markov Model of Football 

In **Figure 3** , we see a graph of expected points from our absorption probabilities on 1<sup>st</sup> -and-10 or 1<sup>st</sup> -and-Goal situations: 



**Figure 3** _displays the expected points on 1_<sup>_st_</sup> _-and-10 or 1_<sup>_st_</sup> _-and-Goal based on the yards from opponent’s end zone.  Dots represent the actual calculation from absorption probabilities._ 

Based on the above model, expected points gradually increase as we approach the opponent’s end zone. Even backed up against the goal line, a team is still expected to score around 0.72 points on the drive if it is first down. In contrast, a first down on an opponent’s 1-yard line is worth just less than six points (80.3% chance of a touchdown and 12.6% chance of a field goal). 

Expected points allow for a good measure of efficiency.  One example is the metric of Net Expected Points or NEP (Alamar 2010). NEP takes the difference in expected points between play **_n +_ 1** and play **_n_** to measure the efficiency of play **_n +_ 1** .  By looking at the difference between expected points before a play and after a play, as well as any points scored on the play, we can calculate NEP. This shows how productive the team was versus the league average in a similar situation. If the NEP is positive, the team did better than expected; if negative, the team did worse. 

Let’s look at the 2010 Philadelphia Eagles.  The Eagles finished 10-6 atop the NFC East, but would lose to the eventual Super Bowl Champion Green Bay Packers.  Through 16 regular season games, the Eagles greatly increased their chances of scoring above the league average.  According to our model, 

11 

#### _Submission to Journal of Quantitative Analysis in Sports_ 

Philadelphia scored 50.68 points above expectation on offense and prevented 25.19 points from being scored on defense.  On offense, however, they were only slightly above average in the passing game—adding 8.08 points above what a league-average offense would score if put in similar situations.  Their running game was the best in the league, thanks to Michael Vick.  The Eagles added 55.81 points above expectation on rushing plays<sup>7</sup> .  This kind of complete analysis surrounding the Eagles could help the Eagles prepare for games—maybe rely more heavily on designed run plays for Vick—and could help opponents prepare more adequately for defending the run versus the pass. 

**Table 2** displays overall, passing, and rushing efficiency numbers for each team over the course of the 2010 season.  On offense, teams above 0 performed above expectation; teams below 0 performed worse than expectation.  Conversely, on defense, teams below 0 performed above expectation and teams above 0 performed below expectation.  You may notice that PNEP + RNEP ≠ NEP. This is because there are additional play types other than run or pass (including aborted snaps and penalties among others).  To calculate run and pass efficiencies, we take the net expected points on those specific play calls.  Since run and pass are not variables in the model, we calculate them both on the same expected points scale. This is because passing is generally the more efficient option. Otherwise, we could potentially have a team with an above average rushing efficiency (versus the rushing efficiencies of the rest of the league) but that could still be detrimental to the team given that passing is the better option.  This way, we can determine whether teams are performing above or below expectation on each play call. 

**Table 2: 2010 Team NEP Based on Markov Model** 

_This table displays the total net expected points throughout the course of the 2010 season (similar to total runs added in baseball) on both offense and defense for all 32 NFL teams. PNEP and RNEP represent passing and rushing net expected points.  To calculate these, we look at the difference in expected points on pass play-calls and run play-calls. You will notice that it is more likely for a team to be above league-average passing the ball than running the ball, as passing is the more efficient option in general. NEP can also be looked_ _<u>at on a per play basis.</u>_ 

||<br>|**OFFENSE**<br>||**D**<br>|**EFENSE**<br>||
|---|---|---|---|---|---|---|
|**Team**|**NEP**|**PNEP**|**RNEP**|**D NEP**|**D PNEP**|**D RNEP**|
|ARI|-208.56|-183.36|-14.13|-13.73|2.95|-18.07|
|ATL|65.60|62.63|-10.22|-60.71|-48.55|-14.46|



7 Rushing (55.81) + Passing (8.08) > Total Offense (50.68) due to pre-snap penalties (listed as No Play) and aborted snaps, which both typically decrease a team’s chance of scoring. 

12 

Goldner: A Markov Model of Football 

|BAL|-9.88|8.22|-19.68|-85.66|-52.87|-31.62|
|---|---|---|---|---|---|---|
|BUF|-135.22|-92.78|-31.91|37.01|28.60|25.76|
|CAR|-242.26|-175.43|-50.42|-29.94|-15.12|-3.35|
|CHI|-109.96|-74.27|-32.29|-142.58|-91.68|-30.95|
|CIN|-83.14|-30.82|-60.15|-13.18|-22.51|11.37|
|CLE|-95.02|-79.50|-22.13|-29.14|-11.58|-9.87|
|DAL|-18.73|-3.74|1.19|-3.08|23.47|-12.85|
|DEN|-56.39|-3.99|-38.45|72.53|47.25|22.34|
|DET|-52.46|-17.76|-27.90|-23.55|-32.03|20.56|
|GB|51.28|66.33|-12.90|-144.30|-110.52|-21.89|
|HOU|71.46|26.12|37.97|116.87|105.01|13.76|
|IND|60.78|64.10|-11.94|-6.56|-0.63|15.90|
|JAC|-13.28|-48.75|42.58|84.35|72.81|13.89|
|KC|-6.15|12.16|-10.75|-65.43|-36.54|-18.17|
|MIA|-102.68|-58.48|-31.60|-60.96|-3.12|-36.86|
|MIN|-138.63|-116.17|-0.74|-43.20|-7.43|-29.11|
|NE|169.73|119.04|52.19|-53.23|-52.77|0.43|
|NO|29.41|53.88|-15.75|-48.20|-32.23|-13.54|
|NYG|-36.50|-11.87|-17.44|-115.02|-99.77|-2.07|
|NYJ|-50.31|-42.46|-0.92|-68.75|-28.04|-40.65|
|OAK|-35.23|-42.51|14.87|-24.83|-23.56|-15.70|
|PHI|50.68|8.08|55.81|-25.19|-15.33|-19.98|
|PIT|15.47|40.37|-10.48|-154.30|-119.02|-34.16|
|SD|56.92|91.72|-19.53|-109.90|-87.39|-20.85|
|SEA|-134.48|-99.52|-23.83|12.00|19.23|-0.55|
|SF|-77.51|-65.49|-10.93|-64.66|-23.73|-33.80|
|STL|-81.22|-58.85|-18.65|-74.20|-40.92|-20.43|
|TB|6.44|24.31|-3.74|-52.61|-47.48|1.35|
|TEN|-39.15|-9.26|-24.20|-37.68|-9.95|-32.33|
|WAS|-94.40|-68.81|-19.31|-15.58|6.58|0.53|



13 

_Submission to Journal of Quantitative Analysis in Sports_ 

This metric has been used to evaluate offensive play calling<sup>8</sup> as well as determine the relative importance of offense, defense, and special teams within the NFL (Goldner 2010). 

### **Conclusion** 

By determining the transition probabilities between any possible states on the football field, we are able to model a football drive by using an absorbing Markov chain.  While the accuracy of the model can be increased slightly by separating late-game situations and adding more data to ensure higher frequencies, our model gives a solid framework for basic analysis.  Teams can compare their actual performance against the model as well as gain a greater understanding on a situational level.  Additionally, the absorption probabilities lead us to an accurate expected points model, which can be used to measure the efficiency of plays, players, and teams. 

> 8 Ben Alamar used it to measure risk of play-calling in the NFL (Alamar 2010) 

14 

Goldner: A Markov Model of Football 

### **Table 3: Select Absorption Probabilities based on Down, Distance, Yard line** 

_This table shows absorption probabilities, expected points_ **_(EP)_** _, and expected plays remaining based on down, distance‐to‐go, and yard line_ _<u>for select situations across the field.</u>_ 

|**Yard line**|**Down**|**Distance**|**Downs**|**Fumble**|**Int**|**Punt**|**Missed FG**|**Field Goal**|**TD**|**Safety**|**EndHalf/Game**|**EP**|**E[Plays Remaining]**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|OWN 20|1|10|2.85%|5.12%|9.07%|49.80%|2.08%|9.30%|13.84%|0.15%|7.81%|1.24|6.65|
|OWN 20|2|10|2.49%|4.57%|7.92%|59.41%|1.69%|7.55%|11.45%|0.18%|4.74%|1.02|5.65|
|OWN 20|3|10|1.84%|3.86%|6.84%|70.27%|1.14%|5.10%|7.94%|0.13%|2.88%|0.70|3.94|
|OWN 20|4|10|0.36%|0.09%|0.15%|98.71%|0.05%|0.22%|0.31%|0.01%|0.11%|0.03|1.12|
|OWN 40|1|10|4.07%|5.11%|8.95%|37.16%|3.37%|14.81%|20.75%|0.01%|5.78%|1.89|6.41|
|OWN 40|2|10|3.86%|4.68%|7.91%|46.26%|2.89%|12.59%|17.31%|0.01%|4.50%|1.58|5.54|
|OWN 40|3|10|3.11%|3.11%|5.75%|63.13%|1.96%|8.48%|11.58%|0.01%|2.88%|1.06|3.99|
|OWN 40|4|10|0.97%|0.90%|0.39%|96.25%|0.12%|0.54%|0.71%|0.00%|0.12%|0.07|1.16|
|OPP 40|1|10|5.31%|4.34%|7.80%|16.74%|5.86%|24.13%|31.05%|0.01%|4.76%|2.88|5.66|
|OPP 40|2|10|6.22%|3.60%|6.61%|26.08%|5.36%|21.32%|26.99%|0.01%|3.80%|2.52|5.03|
|OPP 40|3|10|6.35%|2.86%|4.98%|45.65%|3.80%|14.85%|19.08%|0.01%|2.43%|1.77|3.68|
|OPP 40|4|10|6.20%|1.07%|0.68%|86.84%|0.38%|1.80%|2.54%|0.00%|0.50%|0.23|1.32|
|OPP 20|1|10|3.29%|3.48%|5.02%|1.06%|5.27%|35.27%|43.89%|0.01%|2.71%|4.11|4.33|
|OPP 20|2|10|3.80%|2.65%|4.63%|1.23%|7.05%|41.09%|37.35%|0.01%|2.20%|3.83|3.73|
|OPP 20|3|10|4.48%|1.82%|3.89%|1.22%|10.83%|50.55%|25.44%|0.01%|1.76%|3.29|2.71|
|OPP 20|4|10|5.87%|0.08%|0.79%|0.19%|18.48%|72.31%|1.85%|0.00%|0.41%|2.30|1.11|
|OPP 1|1|1|2.04%|1.89%|2.02%|0.11%|0.41%|12.58%|80.27%|0.03%|0.65%|5.96|2.26|
|OPP 1|2|1|3.57%|1.72%|2.16%|0.10%|0.55%|19.52%|71.55%|0.05%|0.78%|5.56|2.03|
|OPP 1|3|1|6.81%|1.33%|1.96%|0.09%|0.77%|33.01%|55.16%|0.09%|0.77%|4.83|1.68|
|OPP 1|4|1|14.98%|1.40%|0.40%|0.16%|1.04%|63.23%|18.41%|0.01%|0.36%|3.18|1.12|



15 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **References** 

- Alamar, Benjamin. (2010) "Measuring Risk in NFL Playcalling," _Journal of Quantitative Analysis in Sports_ : Vol. 6 : Iss. 2, Article 11. 

- Carroll, Bob, Pete Palmer, and John Thorn. _The Hidden Game of Football_ . New York: Warner Books, 1988. 

- Carter, Virgil, and Robert E. Machol.  “Operations Research on Football.” _Operations Research_ . Vol. 19, No. 2 (Mar. – Apr., 1971), pp. 541-544 

- Doob, J. L. "The Development of Rigor in Mathematical Probability (19001950)." _Amer. Math. Monthly_ **103** , 586-595, 1996. 

- Goldner, Keith. (2010) “The Ratio of Relative Importance: What Dictates Play in the NFL.” 

- Grinstead, Charles M., and J. Laurie Snell. "Chapter 11: Markov Chains." _Introduction to Probability._ Providence, RI: American Mathematical Society, 1997. _Http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probabi lity_book/Chapter11.pdf_ . Web. 

- Newton, Paul K. and Aslam, Kamran (2009) "Monte Carlo Tennis: A Stochastic Markov Chain Model," _Journal of Quantitative Analysis in Sports_ : Vol. 5: Iss. 3, Article 7. 

- Pankin, Mark. "A Note About "Percentage Baseball" Reconsidered." _Baseball Analyst_ 19 (1985): 14-15. _Society For American Baseball Research_ . Web. 20 Nov. 2011. <http://sabr.org/research/baseball-analyst-archives>. 

16 


