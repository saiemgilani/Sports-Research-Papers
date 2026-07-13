<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Aiming for Competitive Balance Designing Fair Handicap Systems for Darts using a Markov Decision Process Framework - Unknown Authors.pdf -->

_Applied Optimization Lab, University of Toronto_ 

**Aiming for Competitive Balance** Designing Fair Handicap Systems for Darts using a Markov Decision Process Framework 

#### Rachael Walker 

Joint work with 

Craig Fernandes and Timothy Chan 

Department of Mechanical and Industrial Engineering University of Toronto 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
The Rules of Darts<br><!-- End of picture text -->

- Two players with starting score of 501 

- Race to zero 

- To “check out”, must hit a “double” and result in score of exactly zero 

- Can also “bust” by landing on a score where checking out is impossible 









<!-- Start of picture text -->
Double Ring<br>Single<br>Bullseye<br>Single<br>Triple Ring<br><!-- End of picture text -->

2 

Image Sources: https://www.vecteezy.com/free-vector/dart-game and  https://thenounproject.com/icon/darts-642047/ 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Competitive Imbalance and Handicap Systems<br><!-- End of picture text -->

- Wide range of skill levels 



vs. 



- **Handicap systems** create competitive balance between mismatched players 

- Existing darts handicaps use heuristics to give weaker player a head-start 











<!-- Start of picture text -->
501 0<br><!-- End of picture text -->

3 

Image Sources: https://www.flaticon.com/free-icon/start-line_2078790 and https://www.flaticon.com/free-icon/finish-line-flag_1647 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Research Goals<br><!-- End of picture text -->

- Develop optimization-driven handicapping for darts 

- Build intuition around fairness in darts 

- Model a novel dynamic credit handicap in darts (Chan and Singal, 2016) 

   - Credit: deterministically choose outcome for single “throw” 

- Propose a handicap system that mathematically balances competition 



4 

Image Sources: https://www.vecteezy.com/png/9663096-scale-weight-icon-png-transparent and https://www.vecteezy.com/png/9664450-scale-weight-icon-png-transparent 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

## Modelling Framework 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->



<!-- Start of picture text -->
Player<br>State<br>𝑠∈𝑆<br><!-- End of picture text -->

###### **Environment** 



6 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->

##### **State** 

𝑠∈𝑆 

###### 1. Player’s Remaining Score 

{0, … , 501} 

###### 2. Player’s Remaining Credits 

{0, … , 9} 

7 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->

**Player** Action 𝑎∈𝐴 State 𝑠∈𝑆 

###### **Environment** 



8 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->

##### **Action** 

𝑎∈𝐴 

𝐴= 𝐴!"#$% ∪𝐴&#'()! 





𝐴!"#$% contains 729 targets on the board that a player may aim for 

𝐴&#'()! contains the 62 possible board regions that a player may “hit” with perfect execution 



9 

Image Sources : https://thenounproject.com/icon/dart-253393/ and https://thenounproject.com/icon/token-3842652/ 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->



<!-- Start of picture text -->
Player Environment<br>Action 𝑎∈𝐴<br>Transition<br>State  Probabilities<br>𝑠∈𝑆 𝑝 𝑠′ 𝑠, 𝑎)<br><!-- End of picture text -->

10 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Model: Markov Decision Process (MDP) 

**Transition Probabilities** 𝑠′ 𝑝 𝑠, 𝑎) 



###### **Uncertain Outcome** 

𝒂∈𝑨 𝒕𝒉𝒓𝒐𝒘 Use professional player’s skill model* 







𝒩(𝜇, Σ) 





**Deterministic Outcome** 𝒂∈𝑨 𝒄𝒓𝒆𝒅𝒊𝒕 Hit desired board region with certainty *(Haugh and Wang, 2022) 

11 

Image Sources: https://www.flaticon.com/free-icon/data_993762 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->



<!-- Start of picture text -->
Player Environment<br>Action 𝑎∈𝐴<br>Transition<br>State  Probabilities<br>𝑠∈𝑆 Outcome 𝑝 𝑠′ 𝑠, 𝑎)<br>Cost 𝑐<br><!-- End of picture text -->

12 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Markov Decision Process (MDP)<br><!-- End of picture text -->



<!-- Start of picture text -->
Player Environment<br>Action 𝑎∈𝐴<br>Transition<br>Next State  Probabilities<br>𝑠′ ∈𝑆 Outcome 𝑝 𝑠′ 𝑠, 𝑎)<br>Cost 𝑐<br><!-- End of picture text -->

13 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Model: Different Skill Levels<br><!-- End of picture text -->

𝝐 Different skill levels are modelled using an **execution error multiplier** (Chan et al, 2022) 

𝒩(𝜇, Σ) **Strongest Player** 𝝐= 𝟏 

𝒩 𝝐 2(𝜇, Σ) **Weaker Players** 𝝐> 𝟏 







14 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Model: Markov Decision Process (MDP) 

**Model Definition Solution** Optimal Policy **Bellman Equation** Optimal Value 



<!-- Start of picture text -->
Optimal Policy<br><!-- End of picture text -->





15 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Value Function Interpretation<br><!-- End of picture text -->

###### **Theorem 1** 

Value function is the expected number of throws  for a player to check out when using a given policy. 

###### **Definition 1** 

The **weaker player** has a higher expected throws to check out when starting from a score of 501 (with no credits). 

###### **Definition 2** 

**Competitive balance** occurs when two players have an equal number of expected throws to check out. 

###### **Theorem 2** 

There exists a unique number of credits that gives a weaker player the needed advantage to check out with equal or less expected throws compared to a stronger player 

16 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

# Results* 

- Solved a more complex model formulation which includes the turn feature of the game (i.e., players alternate every 3 throws). 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Solving without Dynamic Credits<br><!-- End of picture text -->

𝒩6(𝜇, Σ) 𝒩4(𝜇, 2Σ) 𝒩5(𝜇, 8Σ) 𝒩3(𝜇, 9Σ) 𝝐= 𝟏 𝝐= 𝟐 … 𝝐= 𝟖 𝝐= 𝟗 𝑵𝒐𝑪𝒓𝒆𝒅𝒊𝒕𝒔 … Strongest Weakest 



18 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Execution Error and Optimal Policy<br><!-- End of picture text -->



<!-- Start of picture text -->
Skill Model<br>(target = bullseye)<br>Optimal Policy<br><!-- End of picture text -->



Distribution of throw outcomes (top) vs. optimal policy (bottom) for players with 𝜖= 1 (left) and 𝜖= 9 (right) 

**19** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Results: Sources of Imbalance 

Main imbalance at end of game 



Stronger player could dominate across all scores (head-start could never balance competition) 

Expected turns remaining at different scores for players with different execution error 

**20** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Results: Heuristic Head-Start Handicap 



Current heuristic head-start handicaps do not balance competition 

Heuristic spot point handicap when stronger player has 𝜖= 1 (markers) 

**21** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Optimized Head-Start Handicap<br><!-- End of picture text -->



Optimized spot point handicap when stronger player has 𝜖= 1 (markers) 

**22** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Testing Handicaps with Simulation<br><!-- End of picture text -->



<!-- Start of picture text -->
Optimal<br>Policy<br><!-- End of picture text -->



<!-- Start of picture text -->
Solved MDP for<br>Player 1<br>Simulate<br>Match  Win<br>10,000<br>Outcomes Probabilities<br>matches<br>Solved MDP for<br>Player 2<br>Optimal<br>Policy<br>Optimal<br>Policy<br><!-- End of picture text -->



<!-- Start of picture text -->
Optimal<br>Policy<br><!-- End of picture text -->

23 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Results: Optimized Head-Start Handicap 



Stronger player wins less than 50% of the time using this handicap 

Probability that the stronger player wins after 10,000 simulated matches for different skill mismatches 

**24** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Optimized Head-Start Handicap<br><!-- End of picture text -->



Number of turns for two mismatched players in simulation with 10,000 iterations 

**25** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Optimized Head-Start Handicap<br><!-- End of picture text -->



Number of turns for two mismatched players in simulation with 10,000 iterations 

**26** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Optimized Head-Start Handicap<br><!-- End of picture text -->



Number of turns for two mismatched players in simulation with 10,000 iterations 

**27** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Adding Dynamic Credits<br><!-- End of picture text -->



<!-- Start of picture text -->
𝝐= 𝟏 𝝐= 𝟐 … 𝝐= 𝟖 𝝐= 𝟗<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑵𝒐𝑪𝒓𝒆𝒅𝒊𝒕𝒔<br>𝟏𝑪𝒓𝒆𝒅𝒊𝒕<br>…<br>𝟖𝑪𝒓𝒆𝒊𝒅𝒕𝒔<br>𝟗𝑪𝒓𝒆𝒅𝒊𝒕𝒔<br><!-- End of picture text -->

































28 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Dynamic Credits<br><!-- End of picture text -->



Dynamic credit handicap finds the number of credits where the weaker player and stronger player have the same expected number of turns starting from a score of 501 

**29** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Results: Dynamic Credit Handicap 



Stronger and weaker players have ~equal probability of winning 

Probability that the stronger player wins after 10,000 simulated matches for different skill mismatches 

**30** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Results: Dynamic Credit Handicap<br><!-- End of picture text -->



Number of turns for two mismatched players in simulation with 10,000 iterations 

**31** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

### Results: Dynamic Credit Handicap 



Dynamic credits reshape the distribution to equalize win probability 

Number of turns for two mismatched players in simulation with 10,000 iterations 

**32** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Revisiting Competitive Balance<br><!-- End of picture text -->

occurs **Competitive balance** when two players have an equal expected number of throws to check out 



**Fairness** occurs when two players have an equal probability of winning 

- One-player model 

   - Two-player model 

- Handicap by aligning expectations 

   - Handicap by aligning distributions 

- ~ 2 million states 

- • Single MDP 

- • Takes < 1 minute to solve, regular RAM sufficient 

- ~ 2 billion states 

- • System of MDPs 

- Takes 17 hours to solve, high RAM required 

**33** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
Conclusion<br><!-- End of picture text -->

- Existing head-start handicap approaches are not fair 

   - Main imbalance occurs at the end of the game and cannot be mitigated by a head-start 

   - Heuristic head-start leaves the **weaker** player at a disadvantage 

   - Optimized head-start leaves the **stronger** player at a disadvantage 

   - Finding the “fair” head-start is possible but computationally impractical 

   - Still possible that no optimal head-start exists 

- A novel dynamic credit handicap system is a promising alternative 

   - Guaranteed to always have a value that can balance competition 

   - Alters the distribution of turns to check-out of weaker player so that it mimics that of the stronger player 

   - Can be accurately estimated with simplified modelling framework 

**34** 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 

# Thanks for listening! 

### Questions? 

Rachael Walker University of Toronto rachael.walker@mail.utoronto.ca 

rachael.walker@mail.utoronto.ca 

_Applied Optimization Lab, University of Toronto_ 



<!-- Start of picture text -->
References<br><!-- End of picture text -->

- Timothy C. Y. Chan and Raghav Singal. A markov decision process-based handicap system for tennis. _Journal of Quantitative Analysis in Sports_ , 12(4):179–188, 2016. doi: doi:10.1515/jqas2016-0057. URL https://doi.org/10.1515/jqas-2016-0057. 

- M. B. Haugh and C. Wang. Play like the pros? solving the game of darts as a dynamic zero-sum game. _INFORMS journal on computing,_ 2022. doi: 10.1287/ijoc.2022.1197. URL https://arxiv.org/abs/2011.11031. 

- Timothy C. Y. Chan, Douglas S. Fearing, Craig Fernandes, and Stephanie Kovalchik. A Markov process approach to untangling intention versus execution in tennis. _Journal of Quantitative Analysis in Sports_ , 18(2):127–145, 2022. doi: doi:10.1515/jqas-2021-0077. URL https://doi.org/10.1515/jqas-2021-0077. 

- Dimitri Bertsekas and John Tsitsiklis. Introduction to Probability. Athena Scientific, Belmont, Mass., 2008. 

36 


