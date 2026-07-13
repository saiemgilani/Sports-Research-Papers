<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Estimating individual contributions to team success in women s college volleyball - Unknown Authors.pdf -->



Estimating individual contributions to team success in women’s college volleyball 

Scott Powers, Luke Stancil and Naomi Consiglio 

NESSIS 2023 



0 

## Outline 

**Act 1: Estimating Point Win Probability** _Technique: Markov Chain Model_ **Act 2: Evaluating Individual Contributions** _Technique: Domain Knowledge_ **Act 3: Adjusting for Strength of Schedule** _Technique: Linear Mixed-E↵ect Models_ 

1 



**(Act 0: Introduction to Volleyball)** 

2 



<!-- Start of picture text -->
Introduction to Volleyball<br><!-- End of picture text -->

## Introduction to Volleyball 

|**1**<br>**2**<br>**3**<br>**4**<br>**5**<br>**6**|
|---|



3 



<!-- Start of picture text -->
Introduction to Volleyball<br><!-- End of picture text -->

## Introduction to Volleyball 

**Setter (S)** _Setting_ 

**Outside Hitter (OH)** _Passing, Attacking_ 



<!-- Start of picture text -->
OH MB OPP<br>L OH S<br><!-- End of picture text -->

**Middle Blocker (MB)** _Blocking, Attacking_ **Opposite Hitter (OPP)** _Blocking, Attacking_ **Libero (L)** _Passing_ 

4 



<!-- Start of picture text -->
Existing metrics<br><!-- End of picture text -->

## Existing metrics 

### _•_ Standard metrics 

- Serving: Ace%, Error% 

- Receiving: Error%, Passer Rating 

- Digging: Digs / Set, Digs / Opportunity 

- Setting: Assists / Set 

- = – 

- Attacking: Hitting Efficiency (Kills Errors) / Attempts 

- Blocking: Blocks / Set 

### _•_ State of the art 

- Fellingham (JQAS 2022): PAAPS 

_•_ Similar to regularized adjusted plus-minus in basketball 

- Gordon (volleydork.com): Value Added above Expectation 

_•_ Very similar to the present work 

5 



**Act 1: Estimating Point Win Probability** _Technique: Markov Chain Model_ 

6 



<!-- Start of picture text -->
Example: First Point of 2022 National Championship<br><!-- End of picture text -->

## _Example:_ First Point of 2022 National Championship **Texas Louisville** 

|**Player**|**Skill**|**Eval**|**(X, Y)**|**Attack Code**|
|---|---|---|---|---|
|Anna Deeber|Serve|–|(2.99, -0.13)||
|Emma Halter|Reception|#|(0.93, 5.80)||
|Saige K.-Torres|Set|#|(2.13, 3.13)||
|Molly Phillips|Attack|–|(3.33, 3.20)|X6|
|Raquel Lazaro|Dig|+|(0.86, 4.98)||
|Elena Scott|Set|#|(2.99, 1.65)||
|Claire Chaussee|Attack|–|(0.63, 2.83)|V5|
|Kayla Ca↵ey|Block|+|(3.26, 3.43)||
|Phekran Kong|Dig|!|(0.89, 3.13)||
|Raquel Lazaro|Set|#|(0.97, 2.61)||
|Claire Chaussee|Attack|#|(0.67, 2.91)|X5|



Evaluation Codes: **#** _>_ **+** _>_ **!** _>_ **–** _>_ **/** _>_ **=** Dataset: 4,147 matches, 600K+ points, 5M+ contacts, _⇠_ 6,000 players 

7 

## Markov Chain Model: Game State 

_Definition:_ A **volley** is a sequence of consecutive contacts by the same team 

The game state on each contact is given by: 

- Whether the team started the point by serving or receiving 

- The sequence of contacts made during the current volley (including evaluation code _except_ for contacts ending a volley) 

Terminal states: (S, P) and (R, P) 

_Example:_ (S, D#) _!_ (S, D#S#) _!_ (S, D#S#A) _!_ (R, P) 

8 



<!-- Start of picture text -->
Example: First Point of 2022 National Championship<br><!-- End of picture text -->

## _Example:_ First Point of 2022 National Championship 

|**Player**|**Skill**|**Eval**|**State**|**P(Sideout)**|
|---|---|---|---|---|
|Anna Deeber|Serve||(S, SV)|57%|
|Emma Halter|Reception|#|(R, R#)|63%|
|Saige K.-Torres|Set|#|(R, R#S#)|64%|
|Molly Phillips|Attack||(R, R#S#A)|64%|
|Raquel Lazaro|Dig|+|(S, D+)|49%|
|Elena Scott|Set|#|(S, D+S#)|47%|
|Claire Chaussee|Attack||(S, D+S#A)|47%|
|Kayla Ca↵ey|Block|+|(R, B+)|56%|
|Phekran Kong|Dig|!|(S, D!)|51%|
|Raquel Lazaro|Set|#|(S, D!S#)|51%|
|Claire Chaussee|Attack||(S, D!S#A)|51%|
|**Point Louisville**||||**0%**|



9 



**Act 2: Evaluating Individual Contributions** _Technique: Domain Knowledge_ 

10 



<!-- Start of picture text -->
How a Point Progresses<br><!-- End of picture text -->

## How a Point Progresses 

|**Volley 1**<br>**Team A**|**Volley 2**<br>**Team B**|**Volley 3**<br>**Team A**|**Volley 4**<br>**Team B**|**Volley 5**<br>**Team A**|
|---|---|---|---|---|
|Serve|Reception<br>Set<br>Attack|Dig<br>Set<br>Attack|Dig<br>Set<br>Attack|Dig<br>...|



11 



<!-- Start of picture text -->
How a Point Progresses<br><!-- End of picture text -->

## How a Point Progresses 

**Volley 1 Volley 2 Volley 3 Volley 4 Volley 5 Team A Team B Team A Team B Team A** Serve Reception Set Attack Dig Set Attack Dig Set Attack Dig ... 

12 

## Attack Outcome Tree 



<!-- Start of picture text -->
Attack<br>91% ATT; 9% SET<br>Error No<br>100% BLK<br>70% ATT; 30% SET<br>Block No<br>52% BLK; 48% DIG<br>100% BLK 69% ATT; 31% SET<br>81% ATT; 19% SET<br>No Error Dig/Kill<br>100% BLK<br>73% ATT; 27% SET<br>Return Through<br>100% BLK 28% BLK; 72% DIG<br>89% ATT; 11% SET 79% ATT; 21% SET<br>Dig/Kill Dig/Kill<br><!-- End of picture text -->

13 



<!-- Start of picture text -->
Example: First Attack of 2022 National Championship<br><!-- End of picture text -->

## _Example:_ First Attack of 2022 National Championship 











|TOT|+6%|+8%|–29%|–15%|Standard Stats|
|---|---|---|---|---|---|
|ATT|+5%|+6%|–20%|–9%|1 attempt, 0 kills, 0 errors|
|SET|+1%|+2%|–9%|–6%|0 assists|
|BLK|—|–8%|+15%|+7%|—|
|DIG|—|—|+14%|+14%|1 opportunity, 1 dig|



**Caution:** Blocker/digger assignment is a work in progress 

14 



<!-- Start of picture text -->
Distribution of Points Gained per Opportunity<br><!-- End of picture text -->

## Distribution of Points Gained per Opportunity 



<!-- Start of picture text -->
Serve Set Attack<br>−10% −5% 0% 5% 10% −10% −5% 0% 5% 10% −10% −5% 0% 5% 10%<br><!-- End of picture text -->



<!-- Start of picture text -->
Reception Dig Block<br>−10% −5% 0% 5% 10% −10% −5% 0% 5% 10% −10% −5% 0% 5% 10%<br><!-- End of picture text -->

15 

## Standard vs. Advanced Metrics: Back Row Defense 



<!-- Start of picture text -->
Player A<br>Player B<br>50% 65% 80%<br>Digs per Opportunity (min. 200 opportunities)<br>+5%<br>0%<br>Points Gained per Opportunity<br>−5%<br><!-- End of picture text -->

### **Player A:** 

72% digs per opportunity +3.6% PG per opportunity No block touch: 85% Perfect dig rate: 48% 

### **Player B:** 

72% digs per opportunity +1.2% PG per opportunity No block touch: 66% Perfect dig rate: 36% 

**Caution:** Dig evaluation codes are biased against setters by design 

16 



**Act 3: Adjusting for Strength of Schedule** _Technique: Linear Mixed-E↵ect Models_ 

17 

## Server vs. Receiver 

Exp. Points Gained = _β_ Server + _δ_ Receiver 

(good) 

Exp. Points Gained = ( _β_ Team + _β_ Server) + 

(better) 

( _δ_ Team + _δ_ Receiver) 

Exp. Points Gained = ( _β_ Conf + _β_ Team + _β_ Server) + ( _δ_ Conf + _δ_ Team + _δ_ Receiver) 

(best) 

- Fit random-e↵ects model using lme4 package in R 

### Server: 

- Adj. Points Gained _⇡_ Points Gained – ( _δ_<sup>ˆ</sup> Conf + _δ_<sup>ˆ</sup> Team + _δ_<sup>ˆ</sup> Receiver) 

   - Requires a de-biasing step 

   - Some generalization required for extension to other skills 

18 



<!-- Start of picture text -->
Results: Top 10 Conferences (all skills)<br><!-- End of picture text -->

## Results: Top 10 Conferences (all skills) 

|Conference|Avg SoS|
|---|---|
|Big Ten|+0.23|
|Pac-12|+0.23|
|SEC|+0.21|
|Big 12|+0.20|
|ACC|+0.15|
|West Coast|+0.09|
|American|+0.04|
|Big West|+0.04|
|Mountain West|+0.02|
|Mid-American|+0.01|



SoS units: points gained per set 

19 



<!-- Start of picture text -->
Example: Conference Comparison (all skills)<br><!-- End of picture text -->

## _Example:_ Conference Comparison (all skills) 



<!-- Start of picture text -->
BEFORE Adjustment AFTER Adjustment<br>Pac−12 Pac−12<br>Summit League Summit League<br>−0.5 0.0 0.5 −0.5 0.0 0.5 1.0<br>Points Gained per Set (all skills, min. 50 sets) ADJ Points Gained per Set (all skills, min. 50 sets)<br>25 20<br>20<br>15<br>15<br>10<br>10<br>Number of Players Number of Players<br>5<br>5<br>0 0<br><!-- End of picture text -->

   - Separation between conferences is evident 

- One elite player from the Summit League still stands out 

- **Caution:** Additive assumption is not literally true in real life 

20 



<!-- Start of picture text -->
Example: Teammate Comparison (outside hitters)<br><!-- End of picture text -->

## _Example:_ Teammate Comparison (outside hitters) 



<!-- Start of picture text -->
Player A<br>Player B<br>−5% 0% +5% +10%<br>Strength of Schedule (points gained per attack)<br>150<br>100<br>50<br>Number of Attacks<br>0<br><!-- End of picture text -->

- Player A average SOS: +1.4% (PG per attack) 

- Player B average SOS: –0.1% (PG per attack) 

Toughest SoS: Player A vs. Nebraska, +13.0% Kaitlyn Hord blocking, Lexi Rodriguez digging 

**Caution:** SoS depends on which zone the attacker hits 

21 



### **(Act 4: Discussion)** 

22 



<!-- Start of picture text -->
Question: Where does Logan Eggleston rank?<br><!-- End of picture text -->

## Question: Where does Logan Eggleston rank? 



<!-- Start of picture text -->
Adjusted Points Gained per Set<br>Logan Eggleston<br>All−Am. 1st Team<br>All−Am. 2nd Team<br>All−Am. 3rd Team<br>Honorable Mention<br>−0.5 0.0 0.5 1.0<br><!-- End of picture text -->



23 



<!-- Start of picture text -->
Application: Defensive Specialist Strategy<br><!-- End of picture text -->

## Application: Defensive Specialist Strategy 

- 63% of teams replace at least one OH with a DS in back row 



<!-- Start of picture text -->
Reception<br>All−Around OH<br>Front−Only OH<br>DS<br>−5% 0% +5%<br>Reception Points Gained per Opportunity (season−long average)<br>800<br>600<br>400<br>Number of Player−Sets 200<br>0<br><!-- End of picture text -->

Reception PG <u>per</u> opportunity 

All-Around OH: +1 _._ 1% 

Front-Only OH: _−_ 1 _._ 4% 

Defensive Specialist: +0 _._ 9% 

Substitutable Opportunities: 

      - 0.1 opportunities per point 

- _Example:_ Point win probability 50% _!_ 50 _._ 2% 

   - Match win probability 50% _!_ 52% 

Pythagorean formula for volleyball: _p_<sup>10</sup> _/_ ( _p_<sup>10</sup> + (1 _− p_ )<sup>10</sup> ) 

24 



<!-- Start of picture text -->
Limitations and Next Steps<br><!-- End of picture text -->

## Limitations and Next Steps 

- Improve blocker and digger assignments 

- Correct bias for digs made by setter 

- Reward good decision-making in strength of schedule 

- Account for whether setter is back row or front row 

- Leverage (X, Y) coordinate information 

25 



# Thank You! 

26 


