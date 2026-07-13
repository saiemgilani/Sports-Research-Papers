<!-- source: library/conferences/New England Symposium on Statistics in Sports/2011/2011 - RUSH Ratings using score histories - Unknown Authors.pdf -->



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br><!-- End of picture text -->





Todd Graves<sup>1</sup> , Kary Myers<sup>1</sup> , Earl Lawrence<sup>1</sup> , Shane Reese<sup>2</sup> 

1Statistical Sciences Group Los Alamos National Laboratory 

2Department of Statistics Brigham Young University 

New England Symposium on Statistics in Sports 2011 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Pre-1998<br><!-- End of picture text -->



<!-- Start of picture text -->
Pre-1998<br><!-- End of picture text -->



“National champion”(s) named by Associated Press poll of sportswriters and poll of coaches 



No effort to match up top teams in bowl games Miami or Washington, 1991 Nebraska or Penn State, 1994 Michigan or Nebraska, 1997 



Much agitation about college football being the only major sport without a playoff system to determine the national champion 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Formation of the Bowl Championship Series (BCS)<br><!-- End of picture text -->





In 1998, two teams selected to play in national championship game using a formula Formula elements: 







poll of sportswriters poll of coaches 

- “computer rankings”: statistical rating systems using that season’s game results as data 



Much agitation about nerds who know nothing about football affecting the postseason, and how there is still no playoff system 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Discontent with BCS<br><!-- End of picture text -->



<!-- Start of picture text -->
Discontent with BCS<br><!-- End of picture text -->





Annual complaints about the BCS (especially “computers”) Generally, the number of deserving teams is not 2. 2003 NCG: LSU vs. Oklahoma. 



Sportswriters’ poll had USC as #1. 





Hal Stern, “In Favor of a Quantitative Boycott of the Bowl Championship Series”, Journal of Quantitative Analysis in Sports, 2006 People want a playoff already!!! 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Goals for a new rating system<br><!-- End of picture text -->



Help select teams for a playoff system involving 2 or more teams 



Compare undefeated teams from weaker conferences with teams from stronger conferences 





Use the sparse information efficiently Do not reward running up the score 

Graves, Myers, Lawrence, Reese 

RUSH 

History and Background Goals Major families of rating methods The RUSH Method Results Summary 





<!-- Start of picture text -->
Methods that ignore the score<br><!-- End of picture text -->





BCS requires its official ratings to do this, for sportsmanship reasons Example: Bradley-Terry 

_ai_ Pr _{_ Team _i_ beats Team _j}_ = _ai_ + _aj_ 





Blowouts are treated the same as nailbiters Can overvalue undefeated teams with weak schedules 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Margin of victory (MOV)<br><!-- End of picture text -->







Example: least squares fit of (visitor score - home score) on dummy variables for visiting team and home team Losing by 1 is about the same as winning by 1 Thought to have contributed to unpopular BCS choices 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
RUSH: Ratings Using Score Histories<br><!-- End of picture text -->





Use the _score process_ the score of a game at every point in time. Use this to downweight meaningless scoring plays. 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Example data from one game<br><!-- End of picture text -->

|Week|Visitor|Home|Time|Score Margin|
|---|---|---|---|---|
|13|AUB|ALA|3.43|-7|
|13|AUB|ALA|6.35|-14|
|13|AUB|ALA|13.03|-21|
|13|AUB|ALA|21.98|-24|
|13|AUB|ALA|24.87|-17|
|13|AUB|ALA|30.93|-10|
|13|AUB|ALA|40.58|-3|
|13|AUB|ALA|43.92|-6|
|13|AUB|ALA|48.08|1|



Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Auburn 28, Alabama 27<br><!-- End of picture text -->



<!-- Start of picture text -->
AUB 0 0 0 0 7 14 21 21 28<br>ALA 7 14 21 24 24 24 24 27 27<br>0 10 20 30 40 50 60<br>20<br>10<br>0<br>-10<br>-20<br><!-- End of picture text -->

Graves, Myers, Lawrence, Reese RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Oregon 72, New Mexico 0<br><!-- End of picture text -->



<!-- Start of picture text -->
Oregon 72, New Mexico 0<br><!-- End of picture text -->



<!-- Start of picture text -->
UNM 0 0 00 0 0 0 0 0 0 0 0<br>ORE 7 142128 35 42 49 5259 62 65 72<br>0 10 20 30 40 50 60<br>Time<br>20<br>10<br>0<br>-10<br>-20<br><!-- End of picture text -->

Graves, Myers, Lawrence, Reese RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Family of hypothetical 28-0 games<br><!-- End of picture text -->



<!-- Start of picture text -->
Family of hypothetical 28-0 games<br><!-- End of picture text -->

Consider games that the visitor wins 28-0, with 7-point touchdowns at evenly spaced intervals, e.g. 1 2, 4, 6, 8 minutes 2 5, 10, 15, 20 minutes 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

15, 30, 45, 60 minutes 



<!-- Start of picture text -->
Games that end 28-0<br>1<br>2<br>3<br>0 5 10 15<br>Time of Score<br>20<br>15<br>10<br>5<br>Visitor ability - home ability<br>0<br><!-- End of picture text -->

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Notation and elements of the model<br><!-- End of picture text -->



_θj_ = ability of team _j_ 



_η_ = home field advantage 



_λ_ = expected number of scores per unit time 





different for each game, equals _τVisitor_ + _τHome τj_ = one team’s contribution to _λ_ 



_S_ = _{−_ 8 _, −_ 7 _, −_ 6 _, −_ 4 _, −_ 3 _, −_ 2 _,_ 2 _,_ 3 _,_ 4 _,_ 6 _,_ 7 _,_ 8 _}_ set of possible scores 



_πs_ = _π−s_ fraction of scores of each type 

_π−_ 2 + _π_ 2 _π−_ 3 + _π_ 3 _π−_ 4 + _π_ 4 _π−_ 6 + _π_ 6 _π−_ 7 + _π_ 7 _π−_ 8 + _π_ 8 1 in 133 1 in 4 1 in 700 1 in 15 2 in 3 1 in 60 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Markov point process<br><!-- End of picture text -->



Let _α_ = _θv − θh − η_ be the difference between the abilities of the two teams. 



Let _M_ ( _t_ ) = _V_ ( _t_ ) _− H_ ( _t_ ) be the score margin at time _t_ . 

## 

- _f_ ( _t, m, s_ ) = Pr0 _{M_ ( _T_ ) _>_ 0 _|M_ ( _t_ ) = _m_ + _s}−_ Pr0 _{M_ ( _T_ ) _>_ 0 _|M_ ( _t_ ) = _m}._ 

# Assume 

Pr _α{M_ ( _t_ + ∆ _t_ ) = _m_ + _s|M_ ( _t_ ) = _m} ∝ λ_ ∆ _t πs_ exp _{αf_ ( _t, m, s_ ) _}_ Pr _α{M_ ( _t_ + ∆ _t_ ) = _m|M_ ( _t_ ) = _m} ∝_ (1 _− λ_ ∆ _t_ ) 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Computing the ratings<br><!-- End of picture text -->



Not trivial. 







However, with evenly matched teams, scores occur according to a homogeneous Poisson process, with the probabilities of the various types of scores fixed and known Many important quantities can be precomputed MCMC computations done in YADAS (yadas.lanl.gov) 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Calibrated predictions for Visitor - Home score<br><!-- End of picture text -->



<!-- Start of picture text -->
Calibrated predictions for Visitor - Home score<br><!-- End of picture text -->



<!-- Start of picture text -->
Week 2 Week 3 Week 4 Week 5 Week 6 Week 7 Week 8<br>0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8<br>Week 9 Week 10 Week 11 Week 12 Week 13 Week 14 Bowls<br>0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8 0.0 0.4 0.8<br>0.8 0.8 0.8 0.8 0.8 0.8 0.8<br>0.4 0.4 0.4 0.4 0.4 0.4 0.4<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>1.0 1.0 1.0<br>0.8 0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4 0.4<br>0.2 0.2 0.2<br>0.0 0.0 0.0 0.0<br><!-- End of picture text -->

Compute the quantile in the predictive distribution of each actual result. If the predictions are well-calibrated, each week should be a sample from the Uniform(0,1) distribution. 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Comparing predictions to BT and MOV<br><!-- End of picture text -->



<!-- Start of picture text -->
Comparing predictions to BT and MOV<br><!-- End of picture text -->



<!-- Start of picture text -->
RUSH minus B/T RUSH minus MOV<br>2 4 6 8 10 12 2 4 6 8 10 12<br>Week Week<br>0.15 0.15<br>0.05 0.05<br>-0.05 -0.05<br>-0.15 -0.15<br><!-- End of picture text -->

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
2010 Cast of Characters<br><!-- End of picture text -->



NATIONAL CHAMPIONSHIP GAME: 





Auburn (14-0): champions of SEC, the strongest league. Defeated Oregon 22-19 in NCG. Oregon (12-1): champions of Pac 10. Many impressive wins. 



DOMINANT IN MEDIUM-STRENGTH CONFERENCES: TCU (13-0): champions of Mountain West. Boise State (12-1), lost only to Nevada (13-1). Many lopsided wins. 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
2010 RUSH Ratings<br><!-- End of picture text -->

||E(rank)|team|record|_E_(_θ_)|sd|_τ_|
|---|---|---|---|---|---|---|
|1|2.62|Boise St|12-1|6.563|0.79|4.21|
|2|4.31|Oregon|12-1|6.014|0.79|4.87|
|3|4.37|TCU|13-0|6.031|0.84|4.01|
|4|4.40|Ohio St|12-1|5.973|0.75|4.21|
|5|5.29|Stanford|12-1|5.768|0.77|4.38|
|6|7.03|Alabama|10-3|5.403|0.77|4.11|
|7|8.15|Auburn|14-0|5.154|0.62|4.76|
|8|10.36|Nevada|13-1|4.874|0.70|4.60|
|9|10.95|Wisconsin|11-2|4.807|0.74|4.62|
|10|11.06|Oklahoma|12-2|4.791|0.76|4.67|



Graves, Myers, Lawrence, Reese 

RUSH 

History and Background Goals Major families of rating methods The RUSH Method Results Summary 





<!-- Start of picture text -->
Posterior distribution for RUSH ratings<br><!-- End of picture text -->

1 BSU (12−1) 2 ORE (12−1) 3 TCU (13−0) 4 OSU (12−1) 5 STAN (12−1) 6 ALA (10−3) 7 AUB (14−0) 8 NEV (13−1) 9 WIS (11−2) 10 OKLA (12−2) 2 3 4 5 6 7 8 9 10 Graves, Myers, Lawrence, Reese RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Why is Auburn #7??<br><!-- End of picture text -->



<!-- Start of picture text -->
Why is Auburn #7??<br><!-- End of picture text -->









Auburn won games by 1, 3, 3, 3, 3, 7, 8. This includes a home overtime win over #35 Clemson and a 3-point win on the game’s last play against #63 Kentucky. And they won a game by 22 after trailing in the 4th quarter. They were a great story and deserving national champions, but they were very lucky: in 100 simulated seasons, they went undefeated in 3 and lost 3 or more in 48. 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Why is Boise State #1??<br><!-- End of picture text -->

This is the complete set of their _halftime_ leads: 6, 34, 14, 38, 29, 41, 21, 21, 38, 20, 17, 22, 13. 



In 100 simulated seasons they went undefeated in 48, lost twice or more in only 10. 



In the 2007-2009 seasons, the top rankings for mid-major teams were #14 BYU, #6 TCU, #3 TCU 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Rankings of teams in other rating systems<br><!-- End of picture text -->



<!-- Start of picture text -->
Rankings of teams in other rating systems<br><!-- End of picture text -->

|RUSH|Team|Record|BT|MOV|
|---|---|---|---|---|
|1|Boise St|12-1|6|1|
|2|Oregon|12-1|3|2|
|3|TCU|13-0|2|5|
|4|Ohio St|12-1|7|6|
|5|Stanford|12-1|4|3|
|6|Alabama|10-3|11|4|
|7|Auburn|14-0|1|7|
|16|Michigan St|11-2|13|44|
|17|LSU|11-2|5|14|
|51|TopFCS Team|*|19|33|



# *Top FCS Team is Eastern Washington (12-2) in BT, Villanova (9-5) in MOV and RUSH. 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Questions?<br><!-- End of picture text -->

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
The resulting likelihood function<br><!-- End of picture text -->



# where 



_n_ is the number of scores; 







_si_ is the number of points scored on the _i_ th scoring play; _ti_ is the time of the _i_ th score; 

_mi_ =<sup>�</sup><sup>_i_</sup> _k_ =1<sup>_si_is the</sup><sup>_i_th value of the score margin, and</sup><sup>_m_(</sup><sup>_t_)</sup> is the margin written as a function of time 

Graves, Myers, Lawrence, Reese 

RUSH 



<!-- Start of picture text -->
History and Background<br>Goals<br>Major families of rating methods<br>The RUSH Method<br>Results<br>Summary<br>Other choices of  f<br><!-- End of picture text -->



<!-- Start of picture text -->
Other choices of  f<br><!-- End of picture text -->







_f_ ( _t, m, s_ ) = _s_ yields<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_f_(</sup><sup>_ti, mi−_1</sup><sup>_, si_) =</sup><sup>_m_(</sup><sup>_T_), a model for</sup> the margin of victory! _f_ ( _t, m, s_ ) = sign( _m_ + _s_ ) _−_ sign( _m_ ) yields _n_ � _i_ =1<sup>_f_(</sup><sup>_ti, mi−_1</sup><sup>_, si_) = sign(</sup><sup>_m_(</sup><sup>_T_)), a Bradley-Terry-type</sup> model. (Which behaves a bit strangely.) 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Point process math<br><!-- End of picture text -->



Write the probability of no scores in ( _t, t_ + ∆ _t_ ) as (1 _− λ_ ∆ _t_ ) divided by the normalizing constant 







Write the probability of no scores in the interval ( _t, v_ ) as a product of probabilities for the intervals of length ∆ _t_ that make up ( _t, v_ ) This is a product of terms like (1-small number). Approximate using 1 _− x ≃_ exp( _−x_ ), then rewrite the product as exp _{−_ sum of small numbers _}_ . The sum of small numbers in the exponential is a Riemann integral as ∆ _t →_ 0. 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Computational remarks<br><!-- End of picture text -->

The RUSH likelihood is not a delight to deal with, but: When _α_ = 0, which we need when calculating _f_ , the number of scores remaining after time _t_ is Poisson( _λ{T − t}_ ), so: 



_e_<sup>_−λ_(</sup><sup>_T−t_)</sup> <u>[</u> _λ_ <u>(</u> _T −t_ <u>)]</u><sup>_k_</sup> Pr0 _{M_ ( _T_ ) _>_ 0 _|M_ ( _t_ ) = _m}_ =<sup>�</sup><sup>_∞_</sup> _k_ =0 _k_ ! _ξk_ ( _m_ ), where _ξk_ ( _m_ ) = Pr0 _{M_ ( _T_ ) _>_ 0 _|M_ ( _t_ ) = _m, k_ scores remain _}_ does not depend on _λ_ or _t_ so can be precomputed, if the _π_ 



_ξk_ ( _m_ ) can be computed exactly for small _k_ , and a normal approximation can be used for large _k_ . (Actually we compute _ζk_ ( _m, s_ ) = _ξk_ ( _m_ + _s_ ) _− ξk_ ( _m_ ).) 

Graves, Myers, Lawrence, Reese 

RUSH 



History and Background Goals Major families of rating methods The RUSH Method Results Summary 



<!-- Start of picture text -->
Computation, continued<br><!-- End of picture text -->



The integrand in the likelihood is smooth. We compute the integrals using Simpson’s rule. 



Final MCMC computations done in YADAS. Previous (Newton-Raphson) version in R, which we still use to precompute the _ζ_ s and some additional quantities to help with the numerical integrations. 

Graves, Myers, Lawrence, Reese 

RUSH 


