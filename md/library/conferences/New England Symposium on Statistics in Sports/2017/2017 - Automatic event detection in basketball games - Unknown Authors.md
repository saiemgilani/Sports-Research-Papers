<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - Automatic event detection in basketball games - Unknown Authors.pdf -->

# Automatic Event Detection in Basketball 

Suraj Keshri, Min-hwan Oh, Sheng Zhang, Garud Iyengar September 22, 2017 IEOR Department, Columbia University 

Introduction 

Motivation 

- Recognizing player match-ups and game events, e.g. ball screen, drive, post-up, etc., crucial for gaining insights both on players and teams 

- Manually labeling these events not scalable 

- Goal: Detect events automatically using player tracking data! 

1 

Player Tracking Data 



Installed in 2013. Tracks: 

- ( _x, y_ ) locations of all 10 players 

- ( _x, y, z_ ) locations of ball 

- 25 observations per second 

- Event annotations (shots, passes, fouls, etc.) 

1230 games per season: _≈_ 1 billion space-time points per season 

2 

# Defense Assignment 

Defense Attraction in Basketball 

3 

Basic Setting 



- _Dti_ : location of defender _i_ at time _t_ 

- _Otj_ : location of offender _j_ at time _t_ 

- _Itij_ = 1: _i_ guards _j_ at time _t_ 

- Stochastic model 



- Defender location is determined by offender characteristics 

4 

## Basic Setting - player and location dependency 





<!-- Start of picture text -->
• Γ is player and location<br>dependent:<br>Γ pk = [ γpk o , γ pk b , γ pk h ]<br>p = g ( ·, · ) grid picker<br>Dti|Itij = 1 ∼N ( Z T tj Γ g ( t,j ) , σ D 2 )<br>• Prior on Γ p = [Γ p 1 , ...,  Γ pK ]<br>Γ p ∼N ( µ Γ , K )<br><!-- End of picture text -->

5 

## Hidden Markov Model 

- Model the evolution of man-to-man defense using HMM 

- Hidden states ( _It_ ): defensive mapping 



<!-- Start of picture text -->
I 0 I 1 I 2 I 3 . . .<br>D 0 D 1 D 2 D 3<br><!-- End of picture text -->

- How about transition probability? 

6 

## Transition Probability 

- Total of 5<sup>5</sup> (= 3125) matchings _⇒_ intractable to learn probabilities for all transitions 

- Propose a bond energy based defensive assignment transition 

   - Single defensive match-up: bond 

   - Defensive switching: breaking and forming a new bond. 

- 4 types of bonds: 1-on-1 on-ball (or off-ball) bond, extra on-ball (or off-ball) bond 

- Transition probability proportional to energy difference 



7 

## Transition Probability: Example 

- Double team match-ups have higher energy (more unstable) than 1-1 match-up. Hence, more likely to switch to 1-1 match-up 



<!-- Start of picture text -->
Defense Offense Defense Offense<br>1 6 1 6<br>2 7 2 7<br>3 8 3 8<br>4 9 4 9<br>5 10 5 10<br><!-- End of picture text -->

Figure 1: On-ball double team 

Figure 2: One-to-one match-up 

8 

## Graphical Model: Defense Assignment 



<!-- Start of picture text -->
e σD 2<br>I D<br>T<br>Ω<br>Γ<br>P<br>µ ϕ, ζ<br><!-- End of picture text -->

- For player _p_ and location _k_ : sample Γ _pk ∼N_ ( _µ_ Γ _, K_ ) 

• For all times _t_ , sample defensive assignment _It_ using energy based transition 

- Sample each defender’s location at _t_ 

_Dti|Itij_ = 1 _∼N_ ( _Z_<sup>_⊤_</sup> _tj_<sup>Γ</sup><sup>_g_(</sup><sup>_t,j_)</sup><sup>_, σ_</sup> _D_<sup>2</sup> ) 

- Iterate until convergence 

9 

Inference: Defense Assignment 

- Initialize all the fixed parameters for GP prior, bond energies e, and _σD_<sup>2.Let</sup><sup>_θ_denote all the fixed parameters</sup> 

- Until convergence 

   - Sample from _P_ ( _I|_ Γ _, D, θ_ ) using forward filtering backward sampling algorithm 

   - Update energy parameters e given the sample of _I_ 

   - Sample _P_ (Γ _|I, D, θ_ ) 

   - Update kernel parameters, and _σD_<sup>2given the sample of Γ</sup> 

10 

# Event Detection 

Event Detection 

- Want to detect events without labeled data 

- Model sequence of event progression using HMM 

- Define the binary hidden state at each time point as an indicator of whether an event is taking place or not 

- Specify the parametric form of the emission distributions which are characteristic to actions 

- Using HMM, compute most likely sequence of hidden state 

11 

## Ball Screen 

- _St_ : indicator of ball screen event 



<!-- Start of picture text -->
S 0 S 1 S 2 . . .<br>X 0 X 1 X 2<br>Y 0 Y 1 Y 2<br>W 0 W 1 W 2<br><!-- End of picture text -->

- _Xt_ : distance between on-ball defender and potential screener 

- _Yt_ : distance between hoop and ball handler 

- _Wt_ : speed of potential screener 

_Xt|St_ = 1 _∼_ exp( _λx_ ) _Yt|St_ = 1 _∼_ log _N_ ( _µy, σy_<sup>2)</sup> _Wt|St_ = 1 _∼_ exp( _λw_ ) 

_Xt|St_ = 0 _∼_ log _N_ ( _µx, σX_<sup>2)</sup> _Yt|St_ = 0 _∼_ Unif(0 _, θy_ ) _Wt|St_ = 0 _∼_ log _N_ ( _µw, σw_<sup>2)</sup> 

12 

Drive 

- _Rt_ : indicator of drive event 



<!-- Start of picture text -->
R 0 R 1 R 2 . . .<br>V 0 V 1 V 2<br>Y 0 Y 1 Y 2<br><!-- End of picture text -->

- _Vt_ : velocity of ball handler towards hoop 

- _Yt_ : distance between hoop and ball handler 

1 _|Rt_ = 1 _∼_ exp( _λv_ ) _V_<sup>+</sup> _t Yt|Rt_ = 1 _∼_ exp( _λy_ ) 

_Vt|Rt_ = 0 _∼ N_ ( _µv, σv_<sup>2)</sup> _Yt|Rt_ = 0 _∼_ Unif(0 _, θy_ ) 

13 

## Post-up 



<!-- Start of picture text -->
• Ut : indicator of post-up event<br>U 0 U 1 U 2 . . . • At : distance between on-ball<br>defender and ball handler<br>• Yt : distance between hoop and ball<br>A 0 A 1 A 2 handler<br>• Ht : speed of ball handler<br>Y 0 Y 1 Y 2 At|Ut = 1 ∼ exp( λa )<br>Yt|Ut = 1 ∼ log  N ( µy, σy 2)<br>Ht|Ut = 1 ∼ exp( λh )<br>H 0 H 1 H 2<br><!-- End of picture text -->

|_At|Ut_ =1|_∼_|exp(_λa_)|
|---|---|---|
|_Yt|Ut_ =1|_∼_|log_N_(_µy, σ_<sup>2</sup><br>_y_<sup>)</sup>|
|_Ht|Ut_ =1|_∼_|exp(_λh_)|
|_At|Ut_ =0|_∼_|log_N_(_µa, σ_<sup>2</sup><br>_a_<sup>)</sup>|
|_Yt|Ut_ =0|_∼_|Unif(0_, θ_)|
|_Ht|Ut_ =0|_∼_|log_N_(_µh, σ_<sup>2</sup><br>_h_<sup>)</sup>|



14 

## Inference 

- _h_ = hidden state of event indicator ( _St, Rt, Ut_ ) 

- _x, y, z, ..._ = sequences of observed states 

   - Initialize _P_<sup>ˆ</sup> ( _h_ 0) _, P_<sup>ˆ</sup> ( _x|h_ ) _, P_<sup>ˆ</sup> ( _y|h_ ) _, ...,_ and _P_<sup>ˆ</sup> ( _h_<sup>_′_</sup> _|h_ ) randomly 

   - Until convergence 

      - E Step: For each sequence _x, y, z, ..._ , compute _P_ ˆ( _h_ 0 _|x, y, z, ..._ ) _,_ ˆ _P_ ( _ht, ht_ +1 _|x, y, z, ..._ ) _,_ ˆ _P_ ( _h_<sup>_′_</sup> _|h_ ) using forward-backward algorithm 

      - M Step: Update the model parameters _P_<sup>ˆ</sup> ( _h_ 0) _, P_<sup>ˆ</sup> ( _x|h_ ) _, P_<sup>ˆ</sup> ( _y|h_ ) _, ...,_ and _P_ ˆ( _h_<sup>_′_</sup> _|h_ ) using MLE 

   - Compute most likely sequence of hidden states, _h_ = ( _h_ 0 _, ..., hT_ ) using Viterbi algorithm 

15 

Results 

## Estimated Defense Assignments and Events 



- Lines represent estimated defense assignments 

- Ball screen and drive actions are captured in the sequence 

16 

Accuracy 

Table 1: Defense Assignment Accuracy Comparison 

|Model|Accuracy|
|---|---|
|Closest Defender|0.7597|
|FixedΓModel (Franks et al.)|0.9179|
|Player Attraction based Model|0.9541|



Table 2: Event Detection Accuracy 

|Event|Accuracy|
|---|---|
|Ball Screen|0.868|
|Drive|0.953|
|Post-up|0.994|



17 

Table 3: Ball Screen Detection 

||Pred<br>|iction<br>|
|---|---|---|
|Actual|Positive|Negative|
|Positive|79|5|
|Negative|23|106|
|Table|4: Drive Det<br>Pred|ection<br>iction|
|Actual|Positive|Negative|
|Positive|65|2|
|Negative|4|58|



18 

Table 5: Post-up Detection 

||Predi|ction|
|---|---|---|
|Actual|Positive|Negative|
|Positive|8|0|
|Negative|2|334|



19 

## Γ Heatmap for Selected Players 

### • Stephen Curry DeAndre Jordan LeBron James 





<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br><!-- End of picture text -->



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br><!-- End of picture text -->

20 

## Γ Results for Golden State Warriors 

- High _γo_ : (S.C.) Stephen Curry, (K.T.) Klay Thompson 

- Low _γo_ : (A.B.) Andrew Bogut, (A.I.) Andre Iguodala 





21 

## Γ Results for Cleveland Cavaliers 

- High _γo_ : (K.I.) Kyrie Irving, (J.S.) J. R. Smith, (L.J.) LeBron James 

- Low _γo_ : (T.M.) Timofey Mozgov, (T.T.) Tristan Thompson 





22 

# Questions? 

22 


