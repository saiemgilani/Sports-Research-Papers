<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1430 

Using Conditional Estimates to Simulate InPlay Outcomes in Limited Overs Cricket 

**Jonathan RT Sargent,** _RMIT University_ **Anthony Bedford,** _RMIT University_ 

©2012 American Statistical Association. All rights reserved. 

## Using Conditional Estimates to Simulate InPlay Outcomes in Limited Overs Cricket 

Jonathan RT Sargent and Anthony Bedford 

#### **Abstract** 

This paper uses conditional probability distributions to simulate batsman outcomes—that is, runs and dismissals—while a limited overs cricket match is in play. The research was motivated by the potential to assess, and reassess, the likelihood of a batsman achieving a certain score within a specified interval. These likelihoods were conditional on the batsman type, a linear combination of batsman order, strike rate and contribution to team runs, and the delivery number, both discrete variables. A Visual Basic program, SimScore, was written to simulate batsman scores from the probability distributions pertaining to the match stages of interest. The scores were then adjusted for team strength, innings and venue effects, using multiple regression. The paper demonstrates the benefits of the model by fitting log-normal distributions to simulated innings (n=500) by Australia’s Ricky Ponting in the 2011 cricket World Cup quarter final. The distributions allowed us to approximate how likely he was to achieve a certain score prior to the match and at 10-, 20and 30-over stages. It is anticipated that real-time information of a batsman's score expectations will add confidence to wagering in individual performance markets—such as “highest individual score”—as well as making possible in-play player rating revisions. 

**KEYWORDS:** conditional probability, simulation, log-normal distribution 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

### **1. Introduction** 

“Limited overs”, or One-Day International (ODI), cricket is played between two teams. Each team needs to accumulate as many runs as possible for a maximum of 50 “overs” (one innings)<sup>1</sup> or until 10 of the 11 batsmen in the batting team are dismissed (or “out”). The winning team is that which has accumulated the most runs when one of these terminal points is reached in the second innings. Each match consists of a maximum of 300 legitimate independent trials (deliveries)<sup>2</sup> per innings where designated bowlers from team _k_ bowl consecutive deliveries to the “in” batsmen from team _j_ . It is the batsmen’s objective to score as many runs as possible through various means (see Section 2.) to contribute to their team’s score. A batsman’s score is the aggregate of runs accumulated during his innings prior to: a) himself being dismissed; b) all remaining teammates being dismissed; or c) the bowling team reaching its 50 overs without having dismissed 10 opponent batsmen. For cases b) and c), the batsman would be recorded as “not out”. 

While the avenues for scoring runs are nearly identical in ODI and traditional “test match” cricket, the durations differ, with a test match played over a maximum of five days. Test match cricket deliveries follow a continuous distribution: prior to the match, it is unknown how many overs will be bowled in one of a possible four innings (two innings per team during the match); wickets are the only discrete resource. Given a batsman has only 50 overs to accumulate his score in ODI matches, his scoring rates tend to be more frenetic, yet more predictable, than in test matches.<sup>3</sup> In developing optimal scoring rates for ODI matches, Clarke (1988) worked under the commonly shared principle that batsmen are more cautious in early and middle stages of their team’s innings in an attempt to preserve team resources, while the latter stages of the innings are prone to aggressive batting to maximize team runs and to increase the probability of victory. A batsman, however, adopts the latter tactic at his own peril because sustained aggression increases the risk of dismissal (Swartz et al 2006). 

Numerous efforts have been made over the last century to retrospectively fit models to batsmen’s scores. Early work by Elderton (1945) proposed test match cricket batting scores followed a geometric distribution, but subsequent research revealed this distribution provided an inadequate fit for zero and extreme scores (Wood 1945). Bailey and Clarke (2004) log-transformed batting scores to alleviate this problem in the tail of the distribution, while Bracewell and Ruggiero (2009) employed a beta distribution to model zero scores, separate to non-zero 

> 1 An over consists of six deliveries. 

> 2 Matches usually extend beyond 300 deliveries because illegitimate deliveries, such as ones deemed by the umpire to be too wide of the batsman, are required to be bowled again. 

> 3 Test match batsmen are able to patiently bat for up to and exceeding 90 overs in a full day’s play. 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

scores that were modeled with a geometric fit. Kimber and Hansford (1993) addressed problems associated with traditional batting averages by investigating the hazard functions of batsmen. However, there is a scarcity of models that can statistically describe a batsman’s scoring progress and expectation while a match is in play. 

Our research was motivated by the potential to assess, and then reassess, the probability of batting outcomes while an ODI event was in play. For this, we investigated “ball-by-ball” run estimations for “in” and remaining batsmen in team _j_ , at any stage in the first innings,<sup>4</sup> by forward simulating the outcome of a discrete random variable, _X_ . The distribution of _X_ was described by probabilities that were conditional on the following match resources: batsman type; a classification reflecting batting ability and style; and the delivery number, _b_ , an indication of time remaining in the first innings. Batsman type was assessed by an algorithm that classified each batsman in a simulated match as one of “high risk, fast scorer” ( _F_ ), “low risk, medium scorer” ( _M_ ), “low risk, slow scorer” ( _S_ ), and “bowlers” ( _B_ ). These categories were statistically determined by a linear combination of the order of the batsman (from 1 to 11), the rate at which he scores (“strike rate”) at predefined stages in his innings (early, middle and late), and his derived contribution to his team’s total runs. 

The joint distribution of runs and dismissals, given batsman type and delivery number, effectively described the match “state” by offering a dynamic set of scoring and dismissal likelihoods at any delivery; these probabilities were useful for observing and predicting a batsman’s scoring strategy. Swartz et al (2009) employed a similar conditional process to simulate ODI cricket match outcomes, with outcome probabilities dependent on batsman/bowler combinations, the number of dismissals and deliveries, and the current match score. Each outcome in our discrete distributions was smoothed over the 300 deliveries to eliminate unrealistic zero and extreme probabilities in the tails of distributions derived from statistically smaller samples. A batsman’s runs, simulated from each trial, were added from _b_ 1,…, _bn_ where _n_ is either the batsman’s simulated dismissal or his team’s simulated innings completion point. Using a multiple regression model, we adjusted the aggregate simulated runs to reflect any difference in opponent strength, and the presence of innings (the advantage of batting first or second) and venue effects. This paper will ultimately demonstrate the benefits of simulation by fitting log-normal distributions to 500 score iterations by Australia’s Ricky Ponting in the 2011 ODI World Cup quarterfinal, at the 0-, 10-, 20- and 30-over mark of the match, providing a statistical context for his observed score. 

> 4 The second innings is a more complicated task because the model must incorporate runs required for the second batting team to win, in conjunction with the decay of delivery and batting resources. 

2 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

ODI cricket’s discrete format is an attractive property for player run and dismissal prediction and, hence, in-play wagering. Easton & Uylangco (2007) provided some evidence of the ability of market odds to predict the outcomes of impending deliveries in ODI matches. Our in-play simulation methodology adds further appeal to wagering on markets such as “highest-scoring batsman” because there is a real-time knowledge of the match conditions with which to generate likelihoods of a batsman outscoring all others in his team. It is expected that this investigation will augment work on retrospective modeling of ODI batting scores for wagering purposes, such as that undertaken by Bailey and Clarke (2004). Moreover, the in-play simulation methods will be useful in real-time player rating calculations. 

### **2. Scoring** 

The batsman facing the bowler (defined as “on strike”) is responsible for contributing to the team’s runs through a number of scoring actions. The most common scoring action is the on-strike batsman hitting the ball into a space on the field, away from the fielders, allowing the two batsmen to run to their opposite end of the rectangular pitch (approximately 20 yards in length). A run is scored each time the batsmen cross and safely reach their opposite end.<sup>5</sup> Batsmen can cross up to four times from a single delivery should the ball be hit into a large enough space on the field. The second score action is for the batsman to hit the ball with sufficient force so it reaches the boundary of the field after touching the ground at least once; four runs are instantly awarded to the batsman, and the batsmen do not have to cross. The third score action sees the batsman forcibly strike the ball so it clears the boundary without touching the ground; six runs are instantly awarded to the batsman, and the batsmen do not have to cross. If a batsman is dismissed, or he was unable to be dismissed by the bowling side before its 50 overs were bowled, his total runs scored are aggregated to produce his final score. 

Batsman _p_ ’s run total, _R_ , at any stage in the match is simply: 



> 5 A fielder, from the bowling team, must retrieve a hit ball and throw it to either end of the pitch, where there are wickets (three upright wooden poles aligned in the turf). The batsman is dismissed if he is short of the end to which he is running and a fielder strikes the wickets. 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

for _n_ deliveries faced in his innings, where _x_ is an outcome from the discrete bivariate random variable, _X_ = { _x_ , _d_ }, at each delivery, _b_ , where _x_ = (0,1,2,3,4,6) runs scored<sup>6</sup> and _d_ is a binary batsman dismissal (0 = _in_ , 1= _dismissed_ ). 

It is trivial to simulate an ODI cricket scoring scenario, where batsman _p_ is facing the first delivery of the first over in the match. As an example: First delivery: hit into a space to the batsman’s left, allowing batsman _p_ and batsman _q_ to cross the length of the pitch once (that is, one run) before the ball is thrown by an opposition fielder back to the wicket keeper<sup>7</sup> to end the play. Batsman _q_ is subsequently on strike after the batsmen crossed for an odd number (one) of runs. Should they have crossed twice (two runs) or four times (four runs), batsman _p_ would retain the strike position. Second delivery: batsman _q_ chooses not to hit and allows the ball to go through to the wicket keeper. Third delivery: batsman _q_ hits firmly and the ball lands, bounces once, and then reaches the field boundary (four runs). Fourth delivery: batsman _q_ hits into space behind the pitch, resulting in a safe, single cross of the batsmen (one run). Fifth delivery: batsman _p_ hits the ball along the ground, directly to a fielder on his right, but the batsmen do not attempt to cross over because the fielder picks up and returns the ball quickly to the wicket keeper. Final delivery: batsman _p_ hits the ball into space for the batsmen to safely cross twice (two runs). Each batsman’s run total for this simulated over can be numerically represented as: 



with the delivery number, _b_ , in subscript. 

In the case of dismissal ( _d_ = 1), where, for example, an opposition fielder catches a ball hit by batsman _p_ before it touches the ground, batsman _p_ would be replaced by batsman _r_ who would assume the scoring process with batsman _q_ . This sequence continues in the first innings until all 10 batting resources, or 300 delivery resources, are exhausted. No runs are awarded to a batsman on dismissal, or ( _x_ = 0 | _d_ = 1). 

### **3. Methods** 

The dearth of practical match data quantifying ODI match delivery outcomes is a hurdle for in-play modeling. Swartz et al (2006) applied a log-linear approach to simulate runs scored during any stage in a match for a proposed batting order. Our research benefited from extensive ball-by-ball ODI match commentary found at www.espncricinfo.com. Using a tailored Visual Basic script, relevant data was 

> 6 While 5 runs are possible in cricket, the occurrence was considered too rare for inclusion in this research. 

> 7 A wicket keeper is similar to a catcher in baseball. 

4 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

extracted from the commentary of all completed ODI matches played between sixteen nations from January 2006 until October 2011. The final dataset comprised approximately 215,000 independent trials from the first innings of these matches. The script prepared key simulation variables for import into statistical software: bowler, batsman, batsman order, delivery ( _b_ ), runs scored (from _b_ ), and a binary dismissal (from _b_ ) variable ( _d_ ). The batsman’s team, opponent, innings number, and match venue were also included for postsimulation adjustments. 

Once collated, the ball-by-ball data revealed extensive match information—indiscernible in match summary data—to complement decision making for wagering, coaching, or player rating calculations. After collapsing the dismissal data from deliveries into overs, a simple dot chart was generated (Figure 1a)), and presented important trends. 



<!-- Start of picture text -->
a) b)<br><!-- End of picture text -->

Figure 1:  Dot charts displaying dismissal frequencies a) per over, b) per over by batting order 

Predictably, dismissals possessed a positive trend in the final 10 overs because batsmen are inherently more aggressive knowing delivery resources are decaying. However, we recognized the need to further examine the noticeable increase in dismissals between the 18th and 20th overs. By introducing a second condition, batting order, it was possible to extrapolate additional dismissal information. Figure 1b) shows a modal point for fourth-order dismissals at the 20over mark. Our data confirmed that fourth-order batsmen were most exposed in 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

this over, accounting for approximately 3.4% of balls faced in their innings, increasing the likelihood of dismissal relative to other overs. 

Figure 1b) also confirms a first-order batsman’s susceptibility in the first over. He faces the first delivery of the innings largely uncertain of any influential match factors—for example, pitch condition—and, as a result, has a higher likelihood of dismissal. As the game progresses, other batsmen are advantaged because they can witness the conditions as well as receive first-hand information from dismissed batsmen. 

#### **3.1 Batsmen classification** 

Classification of batsmen according to their “type” was an extension of the batting-order analysis, discussed in the previous section. Using simulated annealing, Swartz et al (2006) addressed the importance of a well-selected batting order by analyzing the many permutations within a team’s batting lineup. Moreover, Bailey and Clarke (2004) concluded that batting order was a highly significant predictor of runs scored ( _p_ < .001) when analyzing batsman head-tohead wagering. While it is well established that batting order is correlated with batting ability (see Figure 2), it is flawed to assume that batsmen of the same order possess the same run-scoring approach. For example, third-order batsmen from different teams will be among the strongest batsmen in their team, but almost certainly will possess differing batting “styles”. 



Figure 2: Mean runs scored per batting order 

Our approach was to categorize batsmen, dependent on the order of the batsman (from 1 to 11), the rate at which he scores (“strike rate”) in that order at early (first third of his innings), middle (second third) and latter (last third) stages, and his derived contribution to his team’s run total in each match (batsman total 

6 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

runs/team total runs). The strike rate for batsman _p_ can be simply calculated at any match stage by: 



where _x_ is each run outcome from the first ( _b_ = 1) to final delivery ( _n_ ) faced in his innings. 

A discriminant classification process was engaged to assign each player in our dataset to the type vector, _t_ = [ _F_ , _M_ , _S_ ], where _F_ = “high risk, fast scorer”, _M_ = “low risk, medium scorer” and _S_ = “low risk, slow scorer”. Batsmen of order 9, 10 and 11 in a match were automatically assigned to a fourth type, “bowlers” ( _B_ ), because it was considered safe to assume they were specialist bowlers of consistently limited batting ability. Type _F_ batsmen played aggressively from the early stage of their innings; these batsmen were likely to achieve higher strike rates but also a higher rate of dismissals than other types of batsmen (Swartz et al 2006). Type _M_ batsmen were more cautious in early stages, with strike rates improving as their innings progressed. They generally played longer innings, with higher average scores than other batting types. Type _S_ batsmen were players of lesser ability (lower strike rates and average runs) than _F_ and _M_ . 

With an intrinsic knowledge of these batting styles, a training sample was formulated, with 50 batsmen manually assigned to the _t_ vector. For reference in this paper, a batsman of order 3 and type _F_ , for example, is represented by the notation _α_ = _F_ 3. The equation for classifying the remaining batsmen cases ( _n_ = 1,036) was: 



where _dup_ is the _u_<sup>th</sup> discriminant function for batsman _p_ , _Xik_ is the mean value of his strike rate at innings period, _i_ after match _k_ , _Xjk_ is the value of his contribution to team runs, _bo_ is a constant, and _bi,j_ are discriminant coefficients selected to maximise the Mahalanobis distance between the three type centroids in _t_ . Sampaio et al (2006) used similar discriminant approaches to distinguish between basketball player positions in professional European leagues. 

Figure 3 provides a snapshot of the classification results with respect to the mean strike rates by batsmen of each type (excluding bowlers). The most interesting outcome was the similarity in strike rates between _F_ 3 and _M_ 3, and _F_ 4 and _M_ 4. An ANOVA post-hoc test confirmed _F_ 3 and _M_ 3 ( _p =_ .845) and _F_ 4 and _M_ 4 ( _p_ = .551) strike rate means were not statistically different. This phenomoenon is probably due to the requirement of batsmen in these positions to avoid batting in a 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 

high-risk fashion because they typically bat through the middle stages of an innings, protecting batting resources for aggressive batting in the latter overs. Subsequent orders displayed increasing _F_ strike rates. 

Table 1 offers further insight, with a breakdown of each batsman type’s mean strike rates in early-, middle-, and latter-innings stages. _F_ 7, 8 batsmen possessed higher strike rates at the three innings stages than any other order because it is common for these batsmen to be “in” at latter team innings stages, where it is customary to bat aggressively in an attempt to score as many runs as possible (Clarke, 1988). The ANOVA test confirmed _F_ 8 ( _p_ = .000) strike rate was significantly different to _M_ 8 and _S_ 8 strike rates, while _M_ 8 and _S_ 8 strike rates were statistically similar ( _p_ = .343). Moreover, the _F_ 5, 6 strike rates systematically increase at a higher rate than any other type, suggesting these batsmen are capable of rapid scoring when the innings enters an aggressive phase. 



Figure 3: Boxplots of mean Strike Rate by batsman type 

8 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

||I<br>|nnings stage<br>|<br>|
|---|---|---|---|
|Orders<br>Type|Early|Middle|Latter|
|_F_|0.74|0.80|0.79|
|1, 2<br>_M_|0.51|0.62|0.67|
|_S_|0.29|0.38|0.42|
|_F_|0.53|0.65|0.71|
|3, 4<br>_M_|0.60|0.66|0.68|
|_S_|0.31|0.43|0.46|
|_F_|0.70|0.98|1.08|
|5, 6<br>_M_|0.52|0.63|0.70|
|_S_|0.31|0.41|0.47|
|_F_|0.82|1.08|1.12|
|7, 8<br>_M_|0.50|0.61|0.68|
|_S_|0.41|0.59|0.65|



Table 1: Mean strike rates for batsmen types at early, middle, and latter innings stages 

#### **3.2 Conditional probability estimation** 

Probabilities for the joint distributions given by _X =_ { _x, d_ } were derived from a frequency matrix, _Amn_ , using data from the first innings of the collected matches, where each _mn_ is a unique match state describing a batsman of type _m_ ’s scoring/dismissal outcomes at delivery _n_ . Swartz et al (2009) employed a similar frequency approach to estimate conditional probabilities associated with runs scored from illegitimate deliveries in ODI cricket. Our frequency distribution provided 8,100 unique match states (300 deliveries x 27 groups<sup>8</sup> ) and, in turn, 56,700 independent raw probabilities (8,100 match states x 7 outcomes of _X_ ). Each { _x, d_ } in each _mn_ was then assigned to a conditional probability distribution _,_ such that: 



where _a_ �{(0,…,4) � (6)} and _α_ is the type of batsman facing delivery _b_ ( _n_ = 1,…,300) _._ 

In certain _Amn_ elements, particularly the left tails of lower-order batsmen’s score distributions, missing values and an extremely small sample size for certain _X_ outcomes produced unrealistic zero and one raw probabilities. To correct this, a fourth-order polynomial smooth, _f'_ ( _X_ ), was applied through each _f_ ( _X_ ) = _P_ ( _X_ = _x,d_ 

> 8 3 batsman types x 8 orders + 3 bowlers 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

_| α,b_ ) at each _b_ to interpolate missing values and to reduce extreme probabilities in the relevant distributions. Non-parametric median smoothing was also tried but failed the requirement of a low-response smooth. The preferred smooth for _f_ ( _X_ ) took the form: 



where _v, w, x_ and _y_ are smoothing order coefficients, _z_ is the intercept, and the denominator ensured: 



Figure 4 displays the polynomial smooth of probabilities for a batsman _α = F_ 1 scoring _x_ = 4 at each _b_ in an innings. Interestingly, the smooth achieved two maximal points around _b_ = 36 (Over 6) and _b_ = 276 (Over 46), suggesting opening batsmen of type _F_ were more likely to engage in offensive strategies at the early and latter stages of their innings, rather than in the middle stages. 

A discussion on the contribution of delivery resources and batting-type combinations to several unique match scenarios is worthwhile. The influence of delivery number on scoring in a match was evident from our data; Figure 4 exemplifies how commonplace aggressive batting is in the last 10 overs ( _b_ > 240), particularly by type _F_ batsmen. When two higher-order batsmen are active towards the end of the innings, a state of sturdy team progress is observed, whereas lower-order batsmen active at a relatively early match stage reflects a poor innings due to the loss of top-order resources. Our generated probability distributions reflected the various match states: for example, the difference in a _M_ 4 batsman’s probability of dismissal in the first three overs, _P_ ( _d_ = 1 | _M_ 4, _b ≤_ 18) = 0.008 ( _σ =_ 0.003), compared with the final three overs, _P_ ( _d_ = 1 | _M_ 4, _b ≥_ 282) = 0.055 ( _σ =_ 0.002), was statistically significant ( _p <_ .001) because the former scenario required the batsman to play a defensive role in response to the loss of top-order resources. 

10 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 



Figure 4: Polynomial smooth, _f'_ ( _X_ ) of _f_ ( _X_ ) = _P_ ( _x =_ 4 _| F_ 1, _b_ 1,…,300) 

Table 2 is a very small segment of _Amn_ distributions of type _M_ batsmen, but reveals the dynamic nature of the probabilities from an early stage in the innings for each ( _b_ = 1 | _α = M_ 1), ( _b_ = 20 | _α = M_ 5), ( _b_ = 100 | _α_ = _M_ 11), and from the final delivery in the innings ( _b_ = 300 | _α = M_ 1,5,11). The opening batsman, for example, was noticeably more defensive (zero runs scored from a delivery) at the first delivery of the innings ( _P_ ( _x_ = 0 | _M_ 1,1) = 0.760) than at the final delivery of the innings ( _P_ ( _x_ = 0 | _M_ 1,300) = 0.200). This was because, initially, he had the luxury of 100% batting and delivery resources available, allowing him the most time of any batsman to adapt to the physical conditions of the match (such as bowling quality, climate, and pitch condition). A bottom-order batsman was almost certainly one of the team’s specialist bowlers and, therefore, a poor batsman, which was reflected in the marginal difference in the probability of dismissal at a relatively early match stage ( _P_ ( _d_ = 1 | _M_ 11,100) = 0.120) and at the final delivery ( _P_ ( _d_ = 1 | _M_ 11,300) = 0.165). 

|_α_|_b_|_P_(_x_=0)|_P_(_x_=1)|_P_(_x_=2)|_P_(_x_=3)|_P_(_x_=4)|_P_(_x_=6)|_P_(_d_=1)|
|---|---|---|---|---|---|---|---|---|
|_M_1|1|0.760|0.156|0.032|0.006|0.047|0.001|0.002|
|_M_1|300|0.200|0.444|0.189|0.001|0.069|0.011|0.064|
|_M_5|20|0.814|0.109|0.009|0.002|0.046|0.001|0.001|
|_M_5|300|0.111|0.339|0.174|0.015|0.139|0.082|0.139|
|_M_11|100|0.867|0.002|0.000|0.000|0.000|0.000|0.120|
|_M_11|300|0.245|0.444|0.058|0.006|0.063|0.009|0.165|



Table 2: Probabilities for _α=M_ 1,5,11 at early- and late-innings stages 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

#### **3.3 Simulation** 

A Visual Basic simulator, _SimScore_ , was written specifically for this research to estimate unknown run quantities for each “in” and remaining batsman, by calling our conditional probability matrix. An attractive property of the simulated approach is that batsmen’s run estimates can be revised following any ball in a live match scenario, reflecting the match state at _Amn_ . Furthermore, live match scores feed into _SimScore,_ allowing the user to refresh the simulated batting scores after critical events, such as a dismissal. 

The initial routine in _SimScore_ produces a random probability, _u_ 1 ~ U(0,1) at each _b_ , with the outcome, _X_ = { _x_ , _d_ }, determined by the cumulative distribution function: 



To demonstrate, batsman _p_ is facing the first delivery of an innings: if _u_ 1 = 0.70 and _F'_ (0) = 0.75, then _xp_ = 0. Each trial is repeated at a specified delivery in a match, through the last specified delivery (usually _b_ = 300) for each batsman. Batsman _p_ ’s revised total runs, _R_ , are easily recalculated at any delivery, _b_ , by: 



where _r_ is total observed runs at _b_ , and _n_ is the final delivery of batsman _p_ ’s simulated innings. 

For _SimScore_ to properly reflect a match state, its logic had to extend to assigning strike (facing the next delivery) to each “in” batsman, given certain outcomes of _X_ , for example, batsman _q_ assuming strike after batsman _p_ scored one run (the batsmen crossed once). Two sets of rules were written for assigning strike, _S_ , should batsman _p_ and _q_ be in, and batsman _p_ faced the previous delivery, _bt_ : 



where _Sb_  _t_  1 is the rule for the last delivery of each over, after which a new bowler bowls from the opposite end to the previous over. 

12 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

#### **3.4 Adjustment for match attributes** 

As in most team contests, an ODI match consists of two teams of varying strengths, usually competing at one of the team’s home ground. It was important to adjust simulated batsman scores (after each simulation) to reflect the relative strengths of these two competing sides,<sup>9</sup> as well as physical factors, such as different scoring conditions due to an unfamiliar pitch. A multiple regression model was applied to estimate total team runs at match end from any point _b_ : 



where _Yb_ is final team runs estimated from delivery _b_ , _x_ 1 is the historical score interaction between competing teams _j_ and _k_ , _x_ 2 is innings number (1, 2) effect, _x_ 3 is any venue effect, and _βi_ are estimated coefficients ( _i_ = 1,…,3) with an error term, _ε_ . The difference between _Yb_ and the sum of observed and simulated batsmen’s scores in a team was redistributed through the current and remaining batsmen’s scores after each simulation, such that each current and remaining resource received: 



where _φp_ is the adjustment to _R_ (equation (7)) for any batsman _p_ of order _τ_ after delivery _b_ , where _w_ batsmen have been dismissed. 

In 2005, in response to conservative middle-innings scoring, increased fielding restrictions were introduced. These extra men inside the 30-meter circle, for a brief period, increase the opportunity of batsmen achieving scores of four or six. Hence, scoring rates typically increase during these ‘Powerplays’, although risk taking (big hitting to the boundary) by the batsmen can also lead to higher dismissal rates. The estimation of _Yb_ in equation (8) recognizes the post-hoc contributions of Powerplays in each match—that is, marginal additions to total team runs/dismissals as a result of the Powerplay. However, the intricacies of inplay predictions of Powerplay effect for individual batsmen score simulation would command a separate research paper. 

> 9 An opening batsman from Australia, a recognised cricket nation, is expected to be of greater ability and be supported by more able batting partners than an opening batsman from Canada. 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **4. Results** 

Validation of the simulation model was performed in two stages. A generalized validation involved a measurement of average simulated runs, irrespective of batsman type, at each delivery stage. One thousand match simulations were performed and each batsman’s score was logged at each delivery. We then compared the overall fit of the simulated runs with a holdout sample of observed data from 10 recent matches. Preliminary analysis revealed no significant difference between the mean simulated and holdout samples of batsman runs through each delivery, assuming equal variances ( _p =_ .186). We then proceeded to compare the means of pre-smooth ( _Sim_mean_ ) and post-smooth ( _Sim_S_mean_ ) run means with the holdout sample, irrespective of batsman type, at three match phases: early, middle and latter (see Figure 5). Intraclass correlation coefficients were calculated to measure the resemblance of means within each group to the holdout mean at each phase. A negligible difference in means existed between the smoothed and unsmoothed run means in the early phase. However, the decision to smooth the probabilities was justified in the latter stages of the game, with _Sim_mean_ ( _ρ =_ 0.632) shifting further from the holdout mean than _Sim_S_mean_ ( _ρ =_ 0.798). These results confirmed a good overall fit for the smoothed _SimScore_ model. Increasing variance in the final 10 overs could be explained by the combination of top- (higher run scoring) and lower-order (lower run scoring) batsmen alternating strike on the latter deliveries. 

A second-stage validation involved a parametric approach, designed to address any anomalies resulting from a particular batsman type’s run simulations. We investigated runs scored by Australia’s Ricky Ponting in the 2011 ODI World Cup quarterfinal against India. Ponting was classified as _α = M_ 3 and scored 104 runs, considered a milestone for any batsman. _SimScore_ ran 500 iterations of Ponting’s innings from four match stages: pre-match ( _b_ = 0), after 10 overs were bowled ( _b_ = 60), after 20 overs ( _b_ = 120), and after 30 overs ( _b_ = 180). His score was calculated after each iteration from each stage, using equation (7) where _r_ was Ponting’s observed runs at the particular simulation start stage: ( _r_ = 0 | _b_ = 0), ( _r_ = 0 | _b_ = 61), ( _r_ = 22 | _b_ = 121), and ( _r_ = 48 | _b_ = 181). At the end of the 10th over ( _b_ = 60), the opening batsman, Watson, was dismissed, so Ponting faced delivery 61 without any runs to his name, or _r_ = 0. 

14 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 



Figure 5: Intraclass correlation of _Sim_mean_ and _Sim_S_mean_ with holdout mean 

We were specifically interested in the distribution of how many _more_ runs Ponting would score, after _b_ = 60, 120 and 180, or: 



A log-normal distribution, LN( _μ, σ_<sup>2</sup> ), was fitted at each stage to approximate the likelihood of Ponting achieving his observed runs, _r_ = 104, in the match. Figure 6 displays the fit at each stage, with Figure 6(A) a pre-match approximation—that is, starting the simulation procedure from _b_ = 1. Figure 6(A) confirmed a good fit at the early and latter simulated run stages; also, a solution to run modeling problems in the left and right tails, encountered as early as Elderton (1945). The probability of Ponting reaching _R_ = 104 prior to match commencement was 1 - _P_ ( _R_ < 104) = 0.075. After 10 overs (Figure 6(B)), the score expectation increased to 1 - _P_ ( _R_ < 104) = 0.091, as more certainty in the outcome had been established by the in-play conditional estimations. An improved fit around the 30- and 60-run curve areas was also observed. After 20 overs (Figure 6(C)), a further improvement in fit was observed as Ponting gained momentum during his innings. Ponting’s new simulated run target, _R_ , was 104 - ( _r_ = 22) = 82, with probability 1 - _P_ ( _R_ < 82) = 0.098. After 30 overs (Figure 6(D)), an increased likelihood (1 - _P_ ( _R_ < 56) = 0.125) met our expectations because Ponting’s observed run target of 104 was incrementally closer than at previous deliveries. Moreover, the log-normal fit was considered satisfactory after 30 overs, given the 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

negligible difference between _P_ ( _R_ < 56) = 0.125 and _P_ ( _X_ < 56) = 0.135. The application of this methodology to the other batsman scoring with Ponting and with subsequent batsmen in the order would help ascertain a strategy with which to determine the highest-scoring batsman in the innings. 







































Figure 6: Ricky Ponting’s simulated runs fitted with log-normal distributions after A) 0 overs, B) 10 overs, C) 20 overs, D) 30 overs 

### **5. Conclusion** 

A batsman’s runs in an ODI cricket match were effectively estimated in a realtime scenario using forward simulation methodology. A Visual Basic simulator, calling a conditional probability matrix, described how likely a batsman was to score runs, or to be dismissed, at certain stages in the match. The shape of these distributions was conditional on the type of the batsman and on the delivery 

16 

Sargent and Bedford: Using Conditional Estimates to Simulate In-Play Outcomes in Limited Overs Cricket 

number at the point of execution. The most attractive feature of the simulator was its ability to reassess a batsman’s scoring likelihoods from any point in a live match; this enabled log-normal distribution fits on multiple iterations of Ricky Ponting’s innings in the 2011 ODI World Cup quarterfinal. The distributions were appropriate for estimating likelihoods of Ponting reaching a particular score. The in-play approach also improves the fit in the tails of log-normal score distributions because there is added certainty surrounding the momentum of the player’s innings. The ever-increasing online gambling space provides ample opportunity for the application of such developments, particularly wagering on markets such as “highest-scoring batsman”. Bailey and Clarke (2004) designed strategies to maximize profits derived from wagering on one batsman outscoring another (“head-to-head”) during the 2003 ODI World Cup. The simulated score estimations detailed in this work are expected to augment such wagering strategies because they increase the likelihood of detecting market inefficiencies by offering real-time or live score estimates, not just a pre-match approximation. The authors expect quantifying the gain from the application of _SimScore_ in the betting space to be a complex project, one which will be documented in future research papers. _SimScore_ estimates are also expected to provide a valuable footing for real-time player rating developments as it becomes unnecessary to wait until match completion to update a player’s rating. 

### **6. References** 

- Bailey, M.J. & Clarke, S.R. (2004) Market inefficiencies in player head-to-head betting on the 2003 cricket world cup. _Economics, Management and Optimization in Sports_ (P.Pardalos & S. Butenko eds.) pp. 185-201, New York: Springer 

- Bracewell, P.J. & Ruggiero, K. (2009) A parametric control chart for monitoring individual batting performances in cricket. _Journal of Quantitative Analysis in Sports._ Vol. 5, Iss. 3, Art. 5. 

- Clarke, S.R. (1988) Dynamic programming in one-day cricket-optimal scoring rates. _Journal of Operational Research Society_ . Vol. 39, Iss. 4, pp. 331337. 

- Easton, S. & Uylangco, K. (2007) An examination of in-play sports betting using one-day cricket matches. _Journal of Prediction Markets_ . Vol. 1, Iss. 2, pp. 93-109. 

- Elderton, W.P. (1945) Cricket scores and some skew correlation distribution. _Journal of the Royal Statistical Society, Series A_ . 108, pp. 1-11. 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

Kimber, A.C. & Hansford, A.R. (1993) A statistical analysis of batting in cricket. _Journal of the Royal Statistical Society, Series A._ 156(3), pp.443-455. 

- Sampaio, J., Janeira, M., Ibanez, S.J. & Lorenzo, A. (2006). Discriminant analysis of game-related statistics between basketball guards, forwards and centres in three professional leagues. _European Journal of Sport Science_ , Vol. 6, pp. 173-178. 

- Swartz, T.B., Gill, P.G., Beaudoin, D. & deSilva, B.M. (2006) Optimal batting orders in one-day cricket. _Computers & Operations Research,_ 33, pp. 1939-1950. 

- Swartz, T.B., Gill, P.G. & Muthukumarana, S. (2009) Modelling and simulation for one-day cricket. _The Canadian Journal of Statistics,_ Vol. 37, No. 2, pp. 143-160. 

- Wood, G.H. (1945) Cricket scores and geometric progression. _Journal of the Royal Statistical Society, Series A._ 108, pp. 12-22. 

18 


