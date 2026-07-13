<!-- source: library/conferences/New England Symposium on Statistics in Sports/2009/2009 - Skill Importance in Women's Volleyball - Unknown Authors.pdf -->



Skill 

Importance in Volleyball 

Motivation 





The Data 

Importance Scores Models 

Men’s Results 

Women’s Results 

Suggestions 

Gilbert W. Fellingham, Ph. D. Michelle Miskin, M. S. C. Shane Reese, Ph. D. Dept. of Statistics Brigham Young University 

Summary 

Final Thoughts 

```
gwf@byu.edu
```

September 26, 2009 

Table of Contents 



Skill Importance in Volleyball 

> 1 Motivation 

Motivation 

The Data 

Importance Scores Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Final Thoughts 

> 2 The Data 

> 3 Importance Scores 

> 4 Models 

> 5 Men’s Results 

> 6 Women’s Results 

> 7 Suggestions 

> 8 Summary 



<!-- Start of picture text -->
9<br><!-- End of picture text -->

> 9 Final Thoughts 



# Original Motivation 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results Women’s Results 

- 2004 Olympics, US Men’s Volleyball Team 

_•_ Limited practice time, essentially two months 

_•_ Question — how do we maximize practice time? 

- That is, what skills matter most? 

Suggestions Summary 

Final Thoughts 



# Follow Up Issues 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

- 2006 BYU Women’s Volleyball Team 

- How should we value setting? 

Models 

Men’s Results 

Women’s Results 

- How does setting compare in importance to passing, hitting, etc? 

- Again, what skills matter most? 

Suggestions 

Summary 

Final Thoughts 



# The Data 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Final Thoughts 

## _•_ Men - USA National Team 

Data from 2002 World Championships and 2003 World Cup 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

Every skill except setting rated 21,990 observations for USA 



<!-- Start of picture text -->
2<br><!-- End of picture text -->



<!-- Start of picture text -->
3<br><!-- End of picture text -->

## _•_ Women - BYU 

Data from 2006 season 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

Every skill rated for every home game (setting done via film) 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

7,356 observations for BYU 



<!-- Start of picture text -->
3<br><!-- End of picture text -->



# Notion of Skill Importance 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

- How do we determine what matters? 

- Statistical model 

- Parameter _βi_ associated with every skill 

_•_ Importance Score = _E_ <u>(</u> _<u>βi</u>_ <u>)</u> _~~√~~ V_ ( _βi_ ) 

_•_ Question – appropriate way to estimate _E_ <u>(</u> _<u>βi</u>_ <u>)</u> _~~√~~ V_ ( _βi_ )<sup>?</sup> 

Summary 

Final Thoughts 

Ratings 



Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

- Each skill rated 

- Scale depended on skill 

- Slight differences for men and women 

- Passing and serving rated from 0-4 

- Setting rating based on distance from net, only for women 

- Ratings for digging and blocking less consistent 

Summary 

Final Thoughts 



# Men 

Skill 

Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Logistic model used to relate the response to the skill ratings 



for _i_ = 1 _, . . . ,_ 66. 

_Note:_ The _βj_ are interpreted as the effect of performing a skill at the noted level on the _Log Odds Ratio_ of scoring a point. Predicted probabilities of scoring points from 

Suggestions 

Summary 

Final Thoughts 



Used a Bayesian approach to provide a posterior distribution of _βi_ for each of the skills. 



Skill Importance in Volleyball 

# Women 

Logistic Regression Model Logistic model used to relate the response to the skill ratings 

Motivation 

The Data 

Importance Scores 

Pr[ _Y_ = 1 _<u>|</u>_ **skill** = **i** <u>]</u> log = _β_ 0 _i_ + _β_ 1 _i Rik_ � Pr[ _Y_ = 0 _|_ **skill** = **i** ] � 

Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Final Thoughts 

- Model assumes skill rating linearly related on log odds scale to positive outcome 

- Bayesian _χ_<sup>2</sup> goodness-of-fit tests indicated the logistic regression model does reasonably well modeling th probability of a score 

_•_ Importance score for skill, _E_ <u>[</u> _<u>β</u>_ <u>1</u> _<u>i |Y</u>_ <u>]</u><sup>basedonslope</sup> _~~√~~ V_ [ _β_ 1 _i |Y_ ]<sup>,</sup> parameter 



Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Final Thoughts 

# Women 

## Markov Model 

- Sequences of events (serve-outcome, pass-set-attackoutcome, and dig-set-attack-outcome) first-order Markov chains. 

- Transition matrix – elements of the matrix probability of moving from one state to another (e.g., a four-point pass to a set 3–5 feet off the net). 

- The 36 _×_ 36 transition matrix contained the transitions for float serves, jump serves, passes, set distances off the net, attacks, digs, and possible outcomes. 

- Outcomes of a rally were: rally continues, point for home team, point for visiting team. 



# Women 

Skill Importance in Volleyball 

## Markov Model - continued 

Motivation 

## _•_ A multinomial likelihood 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

_f_ ( _yi_ 1 _, . . . , yik |πi_ 1 _, . . . , πik_ ) _∝ πi_<sup>_y_</sup> 1<sup>_i_1</sup><sup>_π_</sup> _i_<sup>_y_</sup> 2<sup>_i_2</sup><sup>_. . . π_</sup> _ik_<sup>_yik,_</sup> (1) 

for each row, _i_ = 1 _, . . . , m_ , of the count matrix. _πij_ represents the probability of moving from state _i_ to state _j_ . 

_•_ We assumed the prior probability densities of each row were distributed as Dirichlet random variables 

Summary 

Final Thoughts 

_f_ ( _πi_ 1 _, . . . , πik |αi_ 1 _, . . . , αik_ ) _∝ πi_<sup>_α_</sup> 1<sup>_i_1</sup><sup>_−_1</sup> _πi_<sup>_α_</sup> 2<sup>_i_2</sup><sup>_−_1</sup> _. . . πik_<sup>_αik−_1</sup> _,_ (2) 



# Women 

Skill Importance in Volleyball 

## Markov Model - continued 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Final Thoughts 

- Importance score – unconditional probability of moving from a state (eg a four-point pass) fo a positive outcome. 

- Called _βi_ 

- To compute _βi_ , used all possible sequences of touches that could occur between the state and the outcome 

_•_ For each sequence, summed the appropriate probabilities at each MCMC draw, and used the resulting posterior to compute _E_ [ _βi |Y_ ] and � _V_ [ _βi |Y_ ] 



# Importance Scores 

Skill 

Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results Women’s Results 

Suggestions 

Summary 

Final Thoughts 

### Table: Skill/Rating Importance Scores. 

||Productive Skills|Count|er Productive Skills|
|---|---|---|---|
|_Ij_|`skill code`|_Ij_|`skill code`|
|27.94|Attack - Kill|-18.67|Serve - 1Pt|
|21.39|Receive - 4Pt|-12.11|Serve - 2Pt|
|15.45|Receive - 3Pt|-11.00|Attack - Error|
|11.06|Defend - StfBlk|-8.07|Serve - Error|
|6.46|Serve - Ace|-7.12|Attack - Blocked|
|6.37|Serve - 4Pt|-4.96|Receive - Error|
|3.35|Defend - BlkDigSame|-4.22|Receive - 1Pt|
|1.87|Defend - NoBlkDig|-4.22|Defend - BlkErr|
|1.62|Serve - 3Pt|-2.19|Defend - BlkDigOpp|
|1.04|Attack - DugNoBlk|-0.38|Receive - 2Pt|
|0.62|Attack - DugTchBlk|||





# Logistic Model 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results 

Women’s Results 

Suggestions Summary 

### Table: Importance scores for the volleyball logistic regression analysis. 

|Skill|_E_(_β_1_|Y_ )|_V_ (_β_1_|Y_ )|Importance Score|
|---|---|---|---|
|Pass|0.51946|0.00375|8.48683|
|Float Serve|0.81906|0.00992|8.22162|
|Jump Serve|0.74160|0.00949|7.61225|
|Set Distance|0.33156|0.00271|6.36639|
|Digs|0.51379|0.00951|5.26835|



Final Thoughts 



Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results 

Women’s Results Suggestions 

Summary 

Final Thoughts 

# Markov Model 

### Table: Importance scores for the volleyball Markov chain analysis. 

|Skill|_E_(_β|Y_ )|_V_ (_β|Y_ )|_Ij_|
|---|---|---|---|
|3 point Pass|0.50551|0.00017|38.32173|
|Set 3–5 feet of the net|0.51304|0.00018|37.88245|
|4 point Pass|0.51001|0.00020|36.51091|
|2 point Pass|0.48935|0.00019|35.78412|
|4 point Dig|0.43787|0.00016|34.67090|
|Set 5–8 feet of the net|0.49893|0.00025|31.60894|
|5 point Dig|0.50061|0.00025|31.58385|
|Left Attack|0.49665|0.00033|27.46854|
|Set 0–3 feet of the net|0.50669|0.00044|24.27541|
|Middle Attack|0.53806|0.00070|20.30614|
|Right Attack|0.55130|0.00101|17.35607|
|Set 8–10 feet of the net|0.42340|0.00066|16.50323|
|1 point Pass|0.36451|0.00054|15.67747|





Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions Summary 

Final Thoughts 

# Markov Model 

### Table: Importance scores for the volleyball Markov chain analysis. 

Skill _E_ <u>(</u> _<u>β|Y</u>_ <u>)</u> _V_ <u>(</u> _<u>β|Y</u>_ <u>)</u> _Ij_ Overpass Attack 0.65062 0.00270 12.52568 3 point Float Serve 0.26774 0.00054 11.56483 3 point Jump Serve 0.18633 0.00040 9.35556 Back Attack 0.38659 0.00197 8.71921 2 point Dig 0.38268 0.00211 8.33366 Set Dump Attack 0.54814 0.00776 6.22122 3 point Dig 0.48367 0.00665 5.93223 2 point Float Serve 0.24707 0.00216 5.31146 1 point Float Serve 0.21983 0.00188 5.07389 2 point Jump Serve 0.16202 0.00122 4.64685 1 point Jump Serve 0.16242 0.00168 3.96645 Out of System Attack 0.26291 0.00974 2.66430 



# Men’s National Team 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

## Men 

- 1 More practice time serving and receiving serve 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- 2 Weight serving more and blocking less when evaluating talent 

- 3 Pass and set further the net 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

- 4 Better attacking outweighs better defense 

Summary 

Final Thoughts 



# BYU Women’s Team 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

## Women 

> 1 Practice transition more 

> 2 Float serve appears preferable to jump serve 

Men’s Results 

Women’s Results 

> 3 Pass further the net 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

> 4 Forget back row offense 

Suggestions 

Summary 

Final Thoughts 

Overall 



Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores Models 

Men’s Results 

Women’s Results 

Suggestions 

> 1 Men’s game and women’s game are different. 

> 1 Men — Attack, Serve, Serve/Receive 

> 2 Women — Serve/Receive, Serve, Dig, Attack 

> 2 Libero? Important for women, less so for men 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

- 3 Type of athlete. Can’t coach size, but also can’t coach quickness 

Summary 

Final Thoughts 



# General Application 

Skill Importance in Volleyball 

Motivation 

The Data 

Importance Scores 

Models 

Men’s Results 

Women’s Results 

Suggestions 

Summary 

Although we demonstrated for volleyball, idea is applicable to all sports 

> 1 Golf – Drive for show, putt for dough 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

- 2 Basketball – assist, 3 pt. shot, 2 pt. shot, def. rebound, rebound 

> 3 Football – most important position 



<!-- Start of picture text -->
4<br><!-- End of picture text -->

- 4 Optimal line-up? 

Final Thoughts 


