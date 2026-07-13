<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - The Pitcher's Dilemma A Game-Theoretical Model of Pickoffs and Stolen Bases - Melville et al.pdf -->

# **The Pitcher's Dilemma: A Game-Theoretical Model of Pickoffs and Stolen Bases** 

Baseball 106 

## **1. Introduction** 

In 2023, Major League Baseball (MLB) introduced two rule changes that had noticeable effects on stolen base attempt and success rates. First, they increased the width of the bases from 15 to 18 inches [5], reducing the distance a base stealer needed to cover and increasing stolen base success rates from 75% to 79% [13]. Second, they limited the pitcher's disengagements to two, where a disengagement is a pickoff attempt or step-off. A third failed pickoff attempt results in a balk [4]. This led to an increase in stolen base attempts because baserunners assume that pitchers are less likely to attempt another pickoff after each attempt, allowing them to increase their lead and steal more easily. 

In this work, we present a comprehensive analysis of stolen base and pickoff strategies under the 2023 rule changes. We model the interaction between pitcher and base stealer as an extensive-form game called _the pitcher's dilemma_ . In Section 3, we describe how we define optimal strategies for lead distances, stolen base attempts, hit and runs, pickoffs, and pitchouts by solving for Nash equilibria in four different versions of the pitcher's dilemma. Then in Section 4 we present the optimal strategies we identified and discuss the implications. 

### **1.1. The Pitcher’s Dilemma** 

The pitcher's dilemma is a stochastic, zero-sum, imperfect-information, extensive-form game. This type of game is depicted with a graph theory tree where the nodes represent game states where a player chooses an action, the edges represent the possible actions, and the leaves represent terminal game states [17, 18]. Our game is explicitly defined by _P, H, Z, A, u_ , and _I_ where 

- _P_ = {baserunning team, pitching team, chance} is the set of players. 

- _H_ is the set of nonterminal nodes. Each nonterminal node is assigned an actor _p_ ∈ _P_ who takes action in that node. _H_ can be partitioned into choice nodes and chance nodes based on the actor: choice nodes are nodes where the baserunning team or pitching team is the actor, and chance nodes are nodes where the chance player is the actor. In chance nodes, actions are sampled from a predefined probability distribution over the set of possible actions. We describe those probability distributions in more detail in Section 2. 

- _Z_ is the set of terminal nodes. We terminate our game at the end of the plate appearance, after a successful pickoff, after a third failed pickoff attempt, and after a stolen base attempt because all of those events reset the pitcher's disengagement count [4]. 

- _A_ is the set of actions. We can partition _A_ into the actions available to the baserunning team _Ab_ , the actions available to the pitching team _Ap_ , and the chance actions _Ac_ . Each node _h_ ∈ _H_ is assigned an appropriate subset of actions based on the game state and the actor in that node. There are four different versions of the game depending on _Ab_ and _Ap_ . _Ab_ = _L_ × _B_ where _L_ is the finite set of lead distances and _B_ is the baserunner's intent. We define _B_ as either 



1 

{steal, stay} or {steal, stay, hit&run}. _Ap_ is either {pitch, pickoff}, in which case the pitcher can choose to pickoff or to throw a generic pitch, or _G_ × _T_ ∪ {pickoff}, in which case the pitcher can choose a specific pitch from a grid of intended pitch locations _G_ and the set of pitch types that the pitcher throws _T_ or they can choose to pickoff. The four versions of the game are shown in the following table. 

|Version|_B_|_Ap_|
|---|---|---|
|Generic|(steal, stay}|{pitch, pickoff}|
|Pitch Specific|{steal, stay}|_G_×_T_ ∪{pickoff}|
|Generic w/ Hit & Runs|{steal, stay, hit&run}|{pitch, pickoff}|
|Pitch Specific w/ Hit &<br>Runs|{steal, stay, hit&run}|_G_×_T_ ∪{pickoff}|



- _u_ : _Z_ → ℝ is the utility function. The utility function in our game represents the runs that score plus the change in expected runs from transitioning from the root choice node to the terminal node. It follows that the baserunning team wants to choose actions to maximize utility, and the pitching team wants to choose actions to minimize utility. 

- _I_ = ( _Ib, Ip_ ) are partitions of choice nodes for the baserunning ( _Ib_ ) and pitching ( _Ip_ ) teams into sets called _information sets_ . An information set is a set of choice nodes that are indistinguishable to the corresponding player. In the pitcher's dilemma, the baserunning team can distinguish between all of their choice nodes, so their information sets trivially contain just one choice node. The pitching team can observe the baserunner's lead distance _l_ ∈ _L_ , but they cannot observe the baserunner's intent _b_ ∈ _B_ , so their information sets contain | _B_ | choice nodes, one for each of the baserunner's choices of _b_ ∈ _B_ . 

The full game tree can be broken into 36 subtrees corresponding to every possible combination of balls, strikes, and number of disengagements. Figure 1 depicts the 3-2-2 subtree (3 balls, 2 strikes, 2 disengagements) for the generic game. Note, we intentionally remove foul balls from the set of chance actions _Ac_ . This prevents the batter from fouling off strike three indefinitely, which keeps the game finite. Additionally, since we are primarily interested in stolen base/pickoff strategies, and since foul balls interfere with base stealing strategy by forcing base stealers to return to their starting base, we think it is best to ignore them. Consequently, the game must terminate at the end of the 3-2-2 subtree, so the chance nodes in Figure 1 all transition to terminal nodes. The △ nodes are the maximizing baserunning team's nodes, the ▽ nodes are the minimizing pitching team's nodes, and the ◯ nodes are the chance nodes. Terminal nodes are represented by their utility _u_ ( _z_ ). The baserunning team acts first in the subtree by choosing a lead distance in _L_ and a baserunner intent in _B_ = {steal, stay}. The dashed circles represent the pitching team's information sets. There is one information set for each choice of lead distance and two choice nodes in each information set, one for when the baserunner chose to steal and one for when they chose to stay. In each information set, the pitcher can choose to pitch or pickoff, which results in a chance node. For simplicity, we did not depict the correct probability distributions for the chance nodes or utilities for the terminal nodes in Figure 1. We will define them more precisely in Section 2. Note, in the hit and run versions of the game, we have an additional pitcher choice node in each information set corresponding to the 



2 

baserunning team choosing to hit and run. In the pitch-specific versions of the game, the pitcher nodes have | _G_ × _T_ | + 1 edges corresponding to each pitch in _G_ × _T_ plus the pickoff action instead of the two edges corresponding to picking off or pitching. The subtrees for other combinations of balls, strikes, and disengagements are similar only the chance nodes may transition to other ball-strike-disengagement subtrees in addition to terminal nodes. 



Figure 1: An example subtree in the generic pitcher's dilemma. The baserunner plays first by choosing a lead distance and to steal or stay. The pitcher can observe the lead distance but not the baserunner's intent to steal, so the pitcher has one information set for every lead distance with two choice nodes corresponding to the baserunner choosing to steal or stay. The pitcher chooses to pitch or pickoff, which results in a chance node where we simulate the outcome of the pitch/pickoff and transition to a terminal node. 

Note, we abuse notation with the terms game tree and subtree. Our game model may have multiple paths from the root node to a subsequent node. For example, in Figure 1, the pickoff action leads to the same chance node regardless of the baserunner's choice to steal or stay because the result of a pickoff attempt does not depend on the baserunner's intent to steal. Additionally, we do not have separate subtrees for all the different paths to the 3-2-2 subtree or any other balls-strikes-disengagements subtree. For example, the sequence ball-ball-ball-strike-strike-pickoff-pickoff leads to the same 3-2-2 choice node as ball-strike-ball-strike-pickoff-ball-pickoff. This modeling decision reduces the number of information sets in the smallest, generic game from _O_ (10<sup>12</sup> ) to a much more manageable _O_ (100), but it means the underlying graph is technically a directed acyclic graph (DAG) rather than a tree. 



3 

A strategy in an extensive-form game is a decision rule that a player uses to choose an action at each of their information sets. If _β_ is the baserunner's strategy, then we say that _π_ is a _best response_ strategy for the pitcher if it minimizes the expected utility given _β_ . Similarly, _β_ is the baserunner's best response strategy to _π_ if it maximizes the expected utility given _π_ . A pair of strategies ( _β_ *, _π_ *) is a _Nash equilibrium_ if _β_ * is a best response strategy to _π_ * and if _π_ * is a best response strategy to _β_ *. We define optimal strategies for lead distances, stolen base attempts, hit and runs, pickoffs, and pitchouts by solving for Nash equilibria in the four different versions of the pitcher's dilemma. 

## **2. The Chance and Terminal Nodes** 

In this section, we define the Nash equilibrium value, which we will denote _V*_ , of the chance and terminal nodes. We begin with the terminal nodes, whose values are given directly by the utility function. The value of a chance node is the expected value of its children's values, which we define using models of the probability distributions over those children. 

### **2.1. Terminal Nodes and the Utility Function** 

Recall, the utility function represents the runs that score plus the change in expected runs from transitioning from the root choice node to the terminal node. Also recall that the game terminates at the end of the plate appearance, after a stolen base attempt, after a successful pickoff, and after a third failed pickoff attempt. Thus, we can partition the set of terminal nodes _Z_ into terminal nodes where the plate appearance has ended, _Z1_ , and terminal nodes where the plate appearance has not yet ended, _Z2_ . Let _h0_ be the root node and _z_ be some terminal node. We assume that zero runs score anytime we transition to a three-out state. Therefore, the runs that score from transitioning from _h0_ to _z_ are 



where br( _h_ ) is the number of baserunners in node _h_ and o( _h_ ) is the number of outs in node _h_ . We have one fewer run for _z_ in _Z2_ than for _z_ in _Z1_ because the plate appearance has not yet ended, so we do not add the batter's contribution to runs scored. 

We define the expected runs of a node using a run expectancy table, which gives the expected runs that score for the remainder of an inning from a ball-strike-baserunners-outs game state [19]. Thus, if _r_ ( _h_ ) is the expected runs for node _h_ , then we define the utility function of terminal node _z_ in a game with root node _h0_ as 



We define the value of _z_ as 





4 

### **2.2. Pickoff Nodes** 

Data giving the lead distances of baserunners on pickoff attempts are not openly shared by MLB. Thus, rather than learning our own model of the probability of a successful pickoff attempt, we use + − an existing model defined by [14]. For arbitrary pickoff chance node _h_ , denote 𝑐 and 𝑐 as the 𝑝𝑜 𝑝𝑜 children corresponding to a successful and failed pickoff attempt respectively. [14] define 𝑝ℎ( ) using a mixed-effects logistic regression model with fixed effect for the lead distance and random effect for the pitcher, 



where  is the sigmoid function, σ 𝑙 ∈𝐿 is the lead distance in feet, and  is the pitcher-specific γ random effect drawn from a normal distribution with mean 0 and standard deviation 1.167. Although [14] did not publish the random effects for individual pitchers, we can use the standard deviation of 1.167 to estimate pickoff success rates for pitchers with n<sup>th</sup> percentile pickoff skill for any arbitrary n (Figure 2). Finally, we define the value of pickoff chance node _h_ as the expected value of its children's values 







5 

Figure 2: The probability of a successful pickoff attempt as a function of lead distance and pitcher skill. Similar plots can be seen in [14]. 

### **2.3. Pitch Nodes** 

In this subsection we define the value of chance nodes where the pitching team chose to pitch and the baserunning team chose to stay. We will refer to these chance nodes as pitch nodes. Recall that we do not allow foul balls in our game model, so the set of possible pitch outcomes is = {ball, called 𝑋 strike, swinging strike, batted ball out, single, double, triple, home run, batter hit by pitch}. Denote the set of children of arbitrary node _h_ as 𝐶 ⊂𝐻∪𝑍. When _h_ is a pitch chance node, each pitch ℎ 

outcome χ∈𝑋 gives a probability distribution over 𝐶 , 𝑝χ( ). We assume that balls, strikes, triples, ℎ 

home runs, and hit by pitches give deterministic probability distributions: balls increase the ball count by one, strikes increase the strike count by one, home runs and triples clear the bases with triples adding a baserunner to third base, and hit by pitches add a runner to first base and move any necessary runners over one base. For batted ball outs, singles, and doubles, we define 𝑝χ( ) using the transition rates between baserunner and out game states in MLB play-by-play data from 2019 to 2023 collected from retrosheet [1]. The value of pitch outcome  in pitch chance node χ _h_ is then given by 



and the value of _h_ is the expected value of (2) over 𝑋. That expected value is defined differently in the generic versions of the game and in the pitch-specific versions of the game. 

In the generic versions of the game, for each  in  we defined χ 𝑋 𝑝ℎ( ) as the rate at which  occurred χ in the ball and strike count corresponding to pitch chance node _h_ in 2023 MLB pitch tracking data [2, 3, 15]. Then the value of _h_ in the generic versions of the game is given by 



In the pitch-specific versions of the game, pitch chance node _h_ corresponds to a specific choice of pitch type 𝑡 ∈𝑇 and intended pitch location 𝑔 ∈𝐺. Since pitchers often miss their intended target, we use an existing model of pitcher command skill to define 𝑝𝑔, 𝑡( ), which is the probability distribution over actual pitch locations, , given a pitcher's choice of pitch type and intended 𝑔<sup>~</sup> 

location, _t_ and _g_ [16]. We define a pitch-specific pitch outcome distribution, denoted 𝑝𝑔<sup>~</sup> , 𝑡 using ( )<sup>,</sup> an XGBoost classifier trained on MLB pitch tracking data from 2022-2023 [2, 3, 15]. The classifier takes as input the pitcher and batter handedness, the pitch's velocity, movement, and location, and the ball and strike count. When a pitcher chooses pitch type _t_ , the relevant velocity and movement is their average velocity and movement for pitch type _t_ . Finally, we define the value of pitch chance node _h_ in the pitch-specific versions of the game as 



6 

(4) 



which is the expected value of (2) over the pitch-specific pitch outcome distribution and the pitcher's command skill distribution. 

### **2.4. Pitch Nodes with Stolen Base Attempts** 

In this subsection, we define the value of the chance nodes where the pitching team chose to pitch and the baserunning team chose to attempt a steal. We will refer to these chance nodes as stolen base nodes. We scraped MLB stolen base attempt data from 2016 to 2025 [8], which we used to train generic and pitch-specific stolen base logistic regression models. The models are defined in Table 1. The inputs to the generic model are the baserunner's lead distance, their average sprint speed [10], their average jump speed, the catcher's average pop time [9], and a flag indicating if the stolen base attempt was before or after the 2023 rule changes. All but the average jump speed were included in the initial scraped dataset. Average jump speed is a feature we engineered to represent the base stealer's quickness during the small window of time between a pitcher's first move and pitch release. To define a player's average jump speed, we fit a power law curve to their 90 foot running splits [7], which gives the average time it took a runner to run _x_ feet for _x_ values ranging from 0 to 90 in 5 foot increments. For example, Figure 3 shows the fitted power law curves for exceptionally slow and fast baserunners Alejandro Kirk and Chandler Simpson compared to their 90 foot splits data. We then used the fitted power law curves to estimate the jump time on each stolen base attempt, which is the estimated time it took each base stealer to cover the distance that they gained from the pitcher's first move to the pitch release. We then calculated jump speed as the distance gained divided by the estimated jump time. A baserunner's average jump speed is then the average jump speed on all of their stolen base attempts. 





7 

Figure 3: The fitted power law curves compared to the splits data for slow baserunner Alejandro Kirk and fast baserunner Chandler Simpson. 

The pitch-specific stolen base logistic regression model has the same inputs as the generic model. Additionally, it has the pitch's velocity and location and the interaction between pitch location and batter handedness. We encode the exact pitch location into five possible zones, depicted in Figure 4. Any pitch in the strike zone is in zone 0. Pitches up and to the left from the catcher's perspective are in zone 1, up and to the right are in zone 2, down and to the left are in zone 3, and down and to the right are in zone 4. These zones allow us to analyze pitchout decisions. For example, the pitch-specific stolen base model determined that pitches in zone 2 to a right-handed batter, which is where a pitcher would try to throw a pitchout, are more likely to result in a caught stealing than pitches in the strike zone or pitches in zone 3. 



Figure 4: The pitch location zones for the pitch-specific stolen base model. Zone 0 is any pitch in the strike zone, zone 1 is up and to the left from the catcher's perspective, zone 2 is up and to the right, zone 3 is down and to the left, and zone 4 is down and to the right. 

Now, partition the pitch outcome set  into 𝑋 𝑋1 = {ball, called strike, swinging strike} and 𝑋2 = {batted ball out, single, double, triple, home run, batter hit by pitch}. A baserunner cannot be credited with a successful stolen base, nor can they be caught stealing, on any pitch outcome in 𝑋2. Thus, for any  in χ 𝑋 , the probability distribution over 𝐶 depends only on the pitch outcome , χ 2 ℎ meaning we have 𝑝χ( ) just like in Section 2.3. On the other hand, for any  in χ 𝑋1, the probability distribution over 𝐶 depends on both the pitch outcome and the outcome of the stolen base attempt. ℎ We assume these probability distributions are deterministic. For example, suppose _h_ is a stolen base 



8 

chance node with a runner on first base, no outs, and a ball and strike count of 0-0. If  is the called χ + + ball outcome, then 𝑝χ, 𝑠𝑏 where 𝑠𝑏 indicates a successful stolen base attempt, is 1 if _c_ is the child with a runner on second base, a count of 1-0, and no outs, and 0 otherwise. Likewise, ( )<sup>,</sup> 𝑝χ, 𝑠𝑏− , where 𝑠𝑏− indicates a failed stolen base attempt, is 1 if _c_ is the child with no runners on base, a 1-0 ( ) count, and 1 out, and it is 0 otherwise. Thus, if _h_ is a stolen base chance node in the generic versions of the game, then the expected value of its children is given by 



where 𝑝ℎ( ) and 𝑝ℎ( ) are defined using the generic stolen base model and 𝑝ℎ( ) is defined as in (3). 

Table 1: Learned coefficients for the generic and pitch-specific stolen base logistic regression models. 



If _h_ is a stolen base chance node in the pitch-specific versions of the game, then the expected value of its children is given by 





9 



### **2.5. Pitch Nodes with Hit and Runs** 

In this subsection, we define the value of the chance nodes in the hit and run versions of the game where the pitching team chose to pitch and the baserunning team chose to attempt a hit and run. We will refer to these chance nodes as hit and run nodes. A hit and run play begins with a runner on first base attempting to steal second base. Typically, the middle infielder on the opposite side of the batter (the second baseman for right-handed batters and the shortstop for left-handed batters) responds to the stolen base attempt by covering second base. This leaves a wide open hole in the opposite side of the infield. The batter's job is to hit a groundball through that hole. If everything goes well, the base stealer easily advances to third base because they got a head start, and the batter gets a single on a ball that would normally be a groundout. If the batter fails to swing or fails to make contact, the runner is in jeopardy of being caught stealing. Therefore, the batter is expected to swing at any pitch, no matter how bad it is, and they will often use a shorter swing to prioritize making contact. 

Similar to the stolen base nodes (Section 2.4), we partition the set of pitch outcomes into 𝑋 = {ball, 1 called strike, swinging strike} and 𝑋2 = {batted ball out, single, double, triple, home run, batter hit by pitch}. For singles, doubles, triples, home runs, and hit by pitches, we assume 𝑝χ( ) is deterministic. A single is a successful hit and run, so it results in runners on first and third base. We assume that doubles always score the baserunner, since they get a head start, as do triples and home runs. Doubles and triples put the batter on second and third base respectively. Finally, batter hit by pitches move the runner from first to second and put the batter on first base. Arguably, hit by pitches should not be possible on hit and runs because the batter is expected to swing at every pitch. However, if the batter gets hit by the pitch, the baserunner cannot be thrown out at second, so we decided to assume the batter will not swing at pitches that are going to hit them because the runner is not in jeopardy of being caught stealing on those pitches. For batted ball outs, we filtered MLB pitch and bat-tracking data from 2023-2025 [2, 3, 15] down to swings that had a positive attack direction and that were at least one standard deviation shorter than the league average swing length [6, 11]. These swings represent likely hit and run swings because the positive attack angle would shoot the ball to the opposite field, and the shorter than average swing length suggests an emphasis on making contact. In addition to the hit and run swings, we also included hit by pitches. We then filtered the data down further to the swings and hit by pitches with a runner on first base where the baserunner was attempting to steal second on the pitch. Finally, we defined 𝑝χ( = 𝑏𝑎𝑡𝑡𝑒𝑑 𝑏𝑎𝑙𝑙 𝑜𝑢𝑡) using the empirical baserunner and out state transition rates of the swings in that dataset that resulted in a batted ball out. 



10 

+ − For  in χ 𝑋 , the hit and run becomes a stolen base attempt, so we define 𝑝χ, 𝑠𝑏 and 𝑝χ, 𝑠𝑏 1 ( ) ( ) exactly as we did for the stolen base chance nodes. Of course, called balls and called strikes are impossible on hit and runs because the batter has to swing, so the only relevant pitch outcome in 𝑋1 is  = swinging strike. χ 

In the generic game with hit and runs, we define 𝑝ℎ( ) for each  as the rate at which  occurred in χ χ the hit and run swing data that we used to define 𝑝χ( = 𝑏𝑎𝑡𝑡𝑒𝑑 𝑏𝑎𝑙𝑙 𝑜𝑢𝑡). Since that data contains only swings and hit by pitches, we have 𝑝ℎ( ) = 𝑝ℎ( ) = 0, as desired. Then the value of hit and run chance node _h_ in the generic game with hit and runs is given by (5) with 𝑝ℎ( ) and 𝑝χ( ) replaced with the hit and run versions of those distributions. 

In the pitch-specific game with hit and runs, we define a pitch-specific outcome distribution with an XGBoost classifier that takes as input the pitcher and batter handedness, the pitch's velocity, movement, and location, and the ball and strike count. This classifier is similar to the one we defined for the pitch-specific pitch chance nodes, except that it is trained on the 2023-2025 swings that had positive attack direction and swing lengths shorter than one standard deviation below league average. Thus, it represents the distribution over pitch outcomes when the batter makes a hit and run swing or gets hit by the pitch. The value of a hit and run chance node _h_ in the pitch-specific 

game with hit and runs is then given by (6) with 𝑝𝑔(<sup>~</sup> , 𝑡) given by the hit and run XGBoost classifier and 𝑝χ( ) given by the hit and run version of that distribution. 

## **3. Solving for a Nash Equilibrium** 

Although the pitcher's dilemma is guaranteed to have at least one Nash equilibrium [18], it may require that the baserunner and/or pitcher play a non-deterministic strategy. Intuitively, if a pitcher always chooses to pitch, the baserunner knows they can lead off as far as they want and steal as frequently as they want without having to worry about being picked off. Thus, an optimally behaving pitcher will mix in some pickoff attempts. Similarly, a pitcher can simply ignore a baserunner who never steals, so it is usually optimal for baserunners to attempt to steal with some frequency to force pitchers to pickoff and increase their disengagement count. We can define non-deterministic strategies by allowing the players to use a _behavioral strategy_ . A behavioral strategy for a player is a probability distribution over the actions in each of their information sets. A player takes action under a behavioral strategy in an information set by randomly sampling the action from the corresponding probability distribution for that information set. In this section, we describe our approach to identifying a pair of behavioral strategies for the baserunner and pitcher that make up a Nash equilibrium in any version of the pitcher's dilemma. 

We begin with the 3-2-2 subtree (Figure 1). Since we chose to ignore foul balls, we know that all chance nodes transition to terminal nodes in this subtree. Suppose we have _n_ lead distances, that is 𝑡ℎ |𝐿| = 𝑛. For arbitrary integer _k_ satisfying 1 ≤𝑘 ≤𝑛, let 𝑃 be the |𝐵| × 𝐴 payoff matrix for the 𝑘 𝑘 | 𝑝| 

𝑡ℎ 𝑡ℎ lead distance in _L_ whose 𝑖 row corresponds to the baserunner taking action 𝑖 ∈𝐵 and whose 𝑗 column corresponds to the pitcher taking action 𝑗∈𝐴 . The entries of 𝑃 are the values of the 𝑝 𝑘 corresponding chance node as defined in Section 2. For example, in Figure 1, we have _B_ = {steal, stay} and 𝐴 = {pitch, pickoff}, so 𝑃 is a 2 × 2 matrix with (1, 1) entry equal to the expected value 𝑝 𝑘 



11 

of 𝑢𝑧 and 𝑢𝑧 , (2, 1) entry equal to the expected value of 𝑢𝑧 and 𝑢𝑧 , and (1, 2) and (2, 2) ( 𝑎) ( 𝑏) ( 𝑒) ( 𝑓) entry equal to the expected value of 𝑢𝑧 and 𝑢𝑧 . ( 𝑐) ( 𝑑) 

𝑃 is the _normal-form_ representation [18] of the subgame where the baserunning team has already 𝑘 𝑡ℎ chosen the 𝑘 lead distance and now must choose an action in _B_ , and the pitching team has 𝑡ℎ observed the 𝑘 lead distance and must choose an action in 𝐴 . Let π be the behavioral strategy 𝑝 𝑘 𝑡ℎ vector of length 𝐴 whose 𝑗 entry gives the probability that the pitcher plays action 𝑗∈𝐴 in the | 𝑝| 𝑝 𝑃 subgame. The solution to the following linear programming problem gives the pitcher's 𝑘 * * equilibrium strategy, π and the equilibrium value of the 𝑃 subgame, 𝑉 . 𝑘 𝑘 𝑘 



The dual of this problem gives the baserunner's equilibrium strategy in the 𝑃 subgame, which we 𝑘 * * * denote β . In other words, β , π is a Nash equilibrium in the normal-form game with payoff 𝑘 ( 𝑘 𝑘) matrix 𝑃 . Then, we can define a full Nash equilibrium pitching strategy for the 3-2-2 subtree by 𝑘 * using (7) to solve for π for each lead distance _k_ . We assume that the baserunner will choose the 𝑘 * lead distance _k_ that maximizes 𝑉 . Therefore, the baserunner's full Nash equilibrium strategy in the 𝑘 * * 3-2-2 game tree is simply the β corresponding to the _k_ that maximizes 𝑉 . 𝑘 𝑘 

If we repeat this process 35 times for the other subtrees, we can define a Nash equilibrium for the full game tree. Thus, we partition the 36 subtrees into eight stages. The subtrees in stage _i_ are all subtrees whose balls, strikes, and disengagements sum to _i_ - 1. The chance nodes of subtrees in stage _i_ transition to either terminal nodes or to the root nodes of subtrees in stage _i_ + 1. Therefore, if we solve the 3-2-2 subtree first, which is the only subtree in stage eight, then we can define the 𝑃 𝑘 

matrices for all the subtrees in stage seven using the terminal values or the value of the root node in the 3-2-2 subtree in stage eight. Then, once we solve for Nash equilibria in all the stage seven subtrees, we can solve stage six, then stage five, and so on to stage one. 

## **4. Examples** 

The primary purpose of the pitcher's dilemma is to provide baserunners and pitchers/catchers with useful strategies that they can use during games to maximize or minimize runs on the bases. In this section, we solve for equilibria in several versions of the game and condense the resulting strategies into simple heuristics and visuals that players could use in games. In the first subsection, we focus primarily on baserunners and identify lead distance and steal attempt strategies. We then shift our attention to pitchers and catchers and determine optimal pitchout strategies. We conclude with a 



12 

discussion of hit and runs. All of the results in this section assume that we only have a runner on first base, but similar results could be generated for other baserunner states. 

### **4.1. Lead Distances and Stolen Base Attempts** 

Intuitively, a pitcher is less likely to attempt another pickoff after each disengagement because of the two-disengagement limit. Baserunners can therefore increase their lead distance after every pickoff attempt because the risk of getting picked off has decreased. This intuition was formalized in [14] with what they refer to as the “two-foot rule.” The two-foot rule states that after each disengagement, the runner should increase their lead by two feet on average. In particular, they should increase their lead by about 1.5 feet after the first disengagement and 2.5 feet after the second. This useful rule of thumb is easy for players to remember and implement during a game. However, [14] used a different methodology than we used in the pitcher's dilemma. Thus, we sought to confirm the two-foot rule, or define a similar alternative, using the generic pitcher's dilemma. 

Figure 5 shows the equilibrium lead distance broken down by count, outs, and disengagement number in the generic game with an average baserunner and pitcher with average pickoff skill. Not surprisingly, there is an upward trend: as disengagement number increases, the recommended lead distance increases as well. After one disengagement, the average increase in lead distance is 1.9 feet. After a second disengagement, the average increase in lead distance is 2.5 feet. The overall average increase after each disengagement is 2.2 feet, so our results support the two-foot rule of thumb from [14]. However, it is clear from Figure 5 that the recommended lead distance depends on the number of outs and the ball and strike count. It also depends on the pitcher's pickoff skill and the baserunner's skill (Appendix: Figures 11 and 12). Finally, the two-foot rule provides no guidance to baserunners on when they should attempt to steal. 



13 



Figure 5: The recommended lead distance by outs, count, and number of disengagements for an average baserunner against an average pitcher. 

Inspired by the positioning cards that fielders can often be seen pulling out of their back pocket and reviewing to make sure they are positioned correctly for the next batter, we addressed the shortcomings of the two-foot rule with a stolen base strategy visualization that could easily be printed onto an index card and given to baserunners or the first-base coach before a game. Figure 6 shows an example card for an average baserunner. The cells are broken down by outs, number of disengagements, and the count. The top number in the cell is the recommended lead distance. The bottom number is the recommended stolen base attempt rate. Additionally, the cell is colored by stolen base attempt rate: green means go and red means stay. Finally, the asterisks by the lead distance serve as a warning to the baserunner to be especially prepared for a potential pickoff attempt. Those are all the game states where the pitcher's equilibrium strategy calls for a pickoff attempt. 



14 



Figure 6: A stolen base strategy index card for an average baserunner. The top number in each cell is the recommended lead distance, and the bottom number is the optimal stolen base attempt rate. The cells are also colored by stolen base attempt rate with green meaning go and red meaning stay. Finally, the asterisks serve as a warning to the baserunner by indicating game states where an optimal pitcher will attempt a pickoff. 

In the Appendix, we display similar stolen base strategy cards for bad baserunner Alejandro Kirk (Figure 13), elite baserunner Chandler Simpson (Figure 14), an average baserunner against a pitcher with 20th percentile pickoff skill (Figure 15), and an average baserunner against a pitcher with 80th percentile pickoff skill (Figure 16). Comparing these figures with each other and with Figure 6, we can identify some trends. Not surprisingly, exceptionally bad baserunners like Alejandro Kirk should not attempt to steal many bases. Elite baserunners like Simpson should attempt to steal more frequently than average. An average baserunner facing a pitcher with a bad pickoff move should steal at a rate similar to that of Simpson when he faces an average pitcher. Baserunners should steal noticeably less frequently against a pitcher with a good pickoff move. Nobody should attempt to steal in a 3-0 count, and in general it is better to attempt to steal in pitchers' counts like 0-2 or 1-2 than in hitters' counts like 2-0, 3-1, or 2-1. 

The stolen base strategy cards can easily be generated for baserunners of varying skill levels facing off against pitchers with various pickoff moves. They can also be printed on index cards that players or first-base coaches could reference during games. Therefore, we conclude that the stolen base cards are just as practical as a simple rule of thumb like the two-foot rule, but they provide richer and more effective stolen base attempt and lead distance strategies. 

### **4.2. Pitching Out** 

If a pitcher or catcher suspects that a baserunner is going to attempt to steal, they may choose to pitchout by throwing a fastball high and outside. This makes it difficult for the batter to make contact and puts the catcher in a good position to quickly throw out the base stealer, as evidenced 



15 

by the coefficients in Table 1, which show that faster pitches that are high and outside are harder to steal against than other pitches. In this subsection, we use the pitch-specific pitcher's dilemma to identify the situations where a pitcher should pitchout. 

Recall, the pitch-specific versions of the game require a grid of intended pitch locations _G_ . The grid we used is given by the 25 aim points in Figure 7. The orange locations represent the possible aim points for a pitcher who is pitching out to a left-handed batter, and the green locations represent the possible aim points for a pitcher who is pitching out to a right-handed batter. We therefore define the game states where it is optimal for a pitcher to pitchout as the game states where the equilibrium strategy calls for them to aim a fastball at one of those locations. 



Figure 7: The grid of intended pitch locations, _G_ . The orange points represent aim points for a pitcher who is pitching out to a left-handed batter, and the green points represent aim points for a pitcher who is pitching out to a right-handed batter. 

The pitch-specific version of the game also requires the pitcher's command skill distribution, 𝑝𝑔, 𝑡( ) , which is the distribution over actual pitch locations given an intended pitch location and choice of pitch type. We only had access to a handful of these estimated command skill distributions from [16], so we chose to focus on two pitchers: right-handed Jacob deGrom and left-handed Blake Snell. Both of these pitchers throw a four-seam fastball (FF), a curveball (CU), a changeup (CH), and a slider (SL), so the set of pitch types was _T_ = {FF, CU, CH, SL}. Thus, the pitcher action set contained 100 possible intended pitches, one for each element in 𝐺 ×𝑇, plus the pickoff action for a total of 101 possible actions. 

For each of the two pitchers, we first assumed they had 50th percentile pickoff skill and solved for equilibria when they faced a right-handed batter with an average runner on first base, Alejandro Kirk on first base, and Chandler Simpson on first base. We then solved for equilibria when they had 20th and 80th percentile pickoff skill with an average runner on first base. We then repeated that 



16 

process with a left-handed batter instead of a right-handed batter. In total, we defined the optimal pitching strategy for 2160 possible game states. In 1212 of those 2160 game states, the optimal strategy was to pitch rather than pickoff, and just 20 of those 1212 pitches were pitchouts. All 20 pitchouts were recommended in game states where the pitcher was ahead in the count or the count was even at 1-1 or 0-0, which suggests that pitchers should not pitchout except in counts where they can afford to give up a ball. Additionally, none of the pitchouts were against Chandler Simpson, suggesting that pitchouts are less valuable against good base stealers who are likely to be safe no matter what. However, given the small fraction of game states where the optimal strategy was to pitchout, we conclude that pitchers should almost never pitchout to prevent stolen bases. The increased likelihood of catching a potential base stealer almost never outweighs the cost of giving up a ball. 

Another reason a pitcher would choose to pitchout is to prevent a hit and run, which we did not consider in this subsection. Our conclusion that pitchers should almost never pitchout only applies to pitching out to prevent a stolen base. In the next subsection, we will see that pitching out to prevent a hit and run is optimal, and offenses need to limit their hit and run attempts to avoid incentivizing pitchouts. 

### **4.3. Hit and Runs** 

Hit and runs are very difficult to successfully execute. Offenses will typically only call for a hit and run with an exceptionally skilled batter who they trust will be able to hit any pitch on the ground to the opposite field. Even with a skilled batter, the offense also needs to get lucky with the pitcher's pitch selection. Ideally, the pitcher will throw an outside fastball, which is easy to hit on the ground to the opposite field. Any other pitch may be difficult to hit to the opposite field, or difficult to hit at all. Thus, the hit and run play is traditionally only called on fastball counts like 2-1, 1-0, or 1-1 against a somewhat predictable pitcher with good command [12]. 

We began our investigation into hit and run strategy with the hit and run version of the generic game. Figure 8 shows the resulting optimal hit and run attempt rates for an average baserunner facing a pitcher with 50th percentile pickoff skill broken down by count, disengagements, and outs. The results were fairly similar for different baserunners and different pickoff skill levels. The generic game equilibria never recommend a hit and run with two outs. This makes sense because one advantage of a hit and run is it helps prevent a ground ball double play, but the offense does not need to worry about double plays if they already have two outs. The equilibria also never recommend hit and runs when the hitter is ahead in the count. This directly contradicts the traditional idea that hit and runs should be executed on fastball counts like 2-1, 1-0, and 1-1. It also raises some concerns about using the generic game to analyze hit and runs. Pitchers can safely pitchout when they are ahead in the count because they can afford to give up a ball. Therefore, an offensive strategy that hits and runs only when the hitter is behind in the count incentivizes a pitcher to throw pitchouts outside the zone for strike three. Thus, we continued our investigation with the pitch-specific version of the game with hit and runs. 



17 



Figure 8: Optimal hit and run attempt rates in the generic game with hit and runs. These results suggest that the generic game does not appropriately model the threat of a pitchout when defining hit and run strategies. It is unlikely that an offense could hit and run 100% of the time in pitchers' counts without pitchers responding with pitchouts. 

We defined equilibrium strategies in the same 2160 possible game states that we considered in Section 4.2 only this time we included the hit and run action in the offense's action set. There were 223 game states where the pitching team chose to pitch and the offense played a hit and run with nonzero probability. Only one of the 223 hit and runs came with two outs, which supports the conclusion from the generic game that hit and runs should not be used with two outs. However, unlike the generic game, many of the 223 hit and runs were called for in the traditional hit and run counts of 2-1, 1-0, and 1-1. Additionally, none of the optimal strategies called for a hit and run 100% of the time. The highest hit and run rate was 70%. Both of these discrepancies between the generic and pitch-specific games are likely due to the threat of a pitchout not being appropriately considered in the generic version. 

The pitching strategy where the offense hits and runs 70% of the time is shown in Figure 9. The game state had Snell with 20th percentile pickoff skill facing a left-handed batter with no outs, a 1-0 count, and two disengagements. In Snell's pitching strategy he mixes between two fastballs in the strike zone. This pitching strategy should be ideal for a left-handed batter to hit a ball to the opposite field. Thus, one may wonder why the offense does not hit and run more frequently in this situation. Figure 10 shows Snell's best response if the offense chooses to hit and run 100% of the 



18 

time instead of just 70% of the time. Not surprisingly, if Snell knows the offense is hitting and running, he should throw a pitchout. This shows that even though in the equilibrium Snell is throwing pitches that are ideal for hit and runs, the offense cannot hit and run more frequently because if they do they create an incentive for Snell to switch to a pitchout, which is much harder to hit and run against. In other words, the offense is hitting and running as frequently as they possibly can if they want Snell to throw pitches that are good for hit and runs. The threat of a pitchout prevents offenses from hitting and running 100% of the time in any game state. 



Figure 9: The equilibrium pitching strategy in the game state where the offense attempted a hit and run most frequently. Snell mixes between two fastballs that are ideal for hit and runs. 

## **5. Conclusion** 

We modeled the interaction between baserunners and defenses in a zero-sum game called _the pitcher’s dilemma_ . We used this model to analyze lead distance, stolen base attempt, pickoff attempt, pitchout, and hit and run strategies. We confirmed a previously established rule of thumb called the “two-foot rule” [14], which states that after each disengagement, a baserunner should increase their lead distance by two feet on average. We then supplemented the simple two-foot rule with stolen base strategy cards that could easily be provided to baserunners or first-base coaches before games. These cards show the optimal lead distance and stolen base attempt rate broken down by game state. They also warn the baserunner when they need to worry about a possible pickoff attempt from the pitcher. We then investigated pitchout strategies. We found that pitchers should very rarely pitchout to prevent a stolen base, but they should pitchout to prevent hit and runs. Consequently, teams utilizing hit and runs need to be careful not to hit and run too frequently or else they create an incentive for the pitcher to pitchout and thwart the hit and run attempt. 



19 



Figure 10: Snell's best response if the offense switches from hitting and running 70% of the time to 100% of the time. Comparing to Figure 9, we see that the offense cannot hit and run too frequently or else Snell will switch from throwing good hit and run pitches to throwing a pitchout, which is hard to hit and run against. 

## **References** 

[1] https://www.retrosheet.org/. [2] Baseball savant. https://baseballsavant.mlb.com/. 

[3] Statcast. https://www.mlb.com/glossary/statcast. 

[4] Balk (bk) & disengagement violation (2023 rule change). https://www.mlb.com/glossary/ rules/balk, 2023. 

[5] Base sizes (2023 rule change). https://www.mlb.com/glossary/rules/base-sizes, 2023. [6] Attack direction. https://www.mlb.com/glossary/statcast/attack-direction, 2025. [7] Statcast 90ft running splits leaderboard. https://baseballsavant.mlb.com/leaderboard/ running_splits, 2025. [8] Statcast basestealing run value leaderboard. https://baseballsavant.mlb.com/ leaderboard/basestealing-run-value, 2025. [9] Statcast pop time leaderboard. https://baseballsavant.mlb.com/leaderboard/poptime, 2025. 

[10] Statcast sprint speed leaderboard. https://baseballsavant.mlb.com/leaderboard/ sprint_speed, 2025. 

[11] Swing length. https://www.mlb.com/glossary/statcast/swing-length, 2025. [12] Dan Blewett. Is the hit and run in baseball a smart play? https://danblewett.com/ hit-run-baseball-smart-play/, Feb 2022. 

[13] Ben Clemens. The steals will continue until success rates decline. 



20 

https://blogs.fangraphs.com/the-steals-will-continue-until-success-rates-decline/, Apr 2025. 

[14] jfhahn2. Github - jfhahn2/pickoff-game-theory, 2024. 

[15] James LeDoux. Introducing pybaseball: An open source package for baseball data analysis. https://jamesrledoux.com/projects/open-source/introducing-pybaseball/, Jul 2017. 

[16] William Melville, Jesse Melville, Theo Dawson, Delma Nieves-Rivera, Christopher Archibald, and David Grimsman. A game theoretical approach to optimal pitch sequencing. In _MIT Sloan Sports Analytics Conference_ , 2023. 

[17] Stuart Jonathan Russell and Peter Norvig. _Artificial intelligence : a modern approach._ Pearson, Cop, Boston, 2010. 

[18] Yoav Shoham and Kevin Leyton-Brown. _Multiagent systems : algorithmic, game-theoretic, and logical foundations_ . Cambridge University Press, Cambridge ; New York, 2009. [19] Tom Tango. Tangotiger blog. https://tangotiger.com/index.php/site/article/ re288-run-expectancy-by-the-24-base-out-states-x-12-plate-count-states-recu, 2018. 

## **Appendix: Supplemental Figures** 



Figure 11: The recommended lead distance with zero outs by count, number of disengagements, and baserunner skill for an average baserunner, an elite baserunner (Chandler Simpson), and a bad baserunner (Alejandro Kirk). 



21 



Figure 12: The recommended lead distance with zero outs broken down by count and number of disengagements for an average baserunner against pitchers with varying levels of pickoff skill. 



Figure 13: Stolen base strategy index card for bad baserunner Alejandro Kirk. 



22 



Figure 14: Stolen base strategy index card for elite baserunner Chandler Simpson. 



Figure 15: Stolen base strategy index card for an average baserunner against a pitcher with 20th percentile pickoff skill. 



23 



Figure 16: Stolen base strategy index card for an average baserunner against a pitcher with 80th percentile pickoff skill. 



24 


