<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - A Paradox of Blown Leads Rethinking Win Probability in Team Sports - Unknown Authors.pdf -->



<!-- Start of picture text -->
A Paradox of Blown Leads:<br>Rethinking Win Probability in Team Sports<br><!-- End of picture text -->

Jonathan Pipping and Abraham J. Wyner The Wharton School, University of Pennsylvania 

NESSIS 2025 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>1 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Case Study: Super Bowl LVII 









At the start of the 2nd half, the Chiefs trailed the Eagles 14–24 and faced a 3rd and 1 at their own 34 At that point, the Eagles’ projected win probability was 78.4% On the next play, Jerick McKinnon converted with a 14-yard run, and the Chiefs would go on to score, eventually winning 38–35. 

Data via nflfastR 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>2 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# How Often Do Blown Leads Occur? 



We’d like to understand how rare it is to blow a lead of this magnitude! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>3 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

How Often Do Blown Leads Occur? 











We’d like to understand how rare it is to blow a lead of this magnitude! 

Intuitively, most people would assume it happens very rarely (about 21.6% of the time), but maybe this is wrong. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>3 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

How Often Do Blown Leads Occur? 







We’d like to understand how rare it is to blow a lead of this magnitude! 

Intuitively, most people would assume it happens very rarely (about 21.6% of the time), but maybe this is wrong. To investigate this, we formalize the question mathematically. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>3 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Mathematical Framework 



The win probability of a team _i_ at time _t_ is a function of team strength _Si_ and game state ( _G, t_ ). Symbolically, _Wi_ ( _t_ ) = _f_ ( _Si , G, t_ ) _, t ∈_ [0 _, T_ ] 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>4 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Mathematical Framework 



The win probability of a team _i_ at time _t_ is a function of team strength _Si_ and game state ( _G, t_ ). Symbolically, 

_Wi_ ( _t_ ) = _f_ ( _Si , G, t_ ) _, t ∈_ [0 _, T_ ] 



In a two-team game between teams _A_ and _B_ , at any time _t_ we have _WA_ ( _t_ ) + _WB_ ( _t_ ) = 1 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>4 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Mathematical Framework 



The win probability of a team _i_ at time _t_ is a function of team strength _Si_ and game state ( _G, t_ ). Symbolically, 

_Wi_ ( _t_ ) = _f_ ( _Si , G, t_ ) _, t ∈_ [0 _, T_ ] 





In a two-team game between teams _A_ and _B_ , at any time _t_ we have _WA_ ( _t_ ) + _WB_ ( _t_ ) = 1 

For the **eventual loser** _ℓ_ , we know that _Wℓ_ ( _T_ ) = 0. So the quantity of interest (the maximum win prob. of the losing team) is given by the random variable 

_Mℓ_ = max _Wℓ_ ( _t_ ) _t_ 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>4 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Mathematical Framework 



The win probability of a team _i_ at time _t_ is a function of team strength _Si_ and game state ( _G, t_ ). Symbolically, 

_Wi_ ( _t_ ) = _f_ ( _Si , G, t_ ) _, t ∈_ [0 _, T_ ] 



In a two-team game between teams _A_ and _B_ , at any time _t_ we have _WA_ ( _t_ ) + _WB_ ( _t_ ) = 1 



For the **eventual loser** _ℓ_ , we know that _Wℓ_ ( _T_ ) = 0. So the quantity of interest (the maximum win prob. of the losing team) is given by the random variable 

_Mℓ_ = max _Wℓ_ ( _t_ ) _t_ 



We will investigate the distribution of _Mℓ_ as a function of the team strengths _SA_ and _SB_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>4 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 



Estimating the win probability function _f_ is difficult in practice. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 



Estimating the win probability function _f_ is difficult in practice. Game state ( _G, t_ ) is multi-dimensional highly non-linear. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 



Estimating the win probability function _f_ is difficult in practice. Game state ( _G, t_ ) is multi-dimensional highly non-linear. Team strengths _SA_ and _SB_ are non-trivial to estimate. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 





Estimating the win probability function _f_ is difficult in practice. Game state ( _G, t_ ) is multi-dimensional highly non-linear. Team strengths _SA_ and _SB_ are non-trivial to estimate. 

To simplify the problem, we specify a simple model to allow exact calculation of in-game win probabilities. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 





Estimating the win probability function _f_ is difficult in practice. Game state ( _G, t_ ) is multi-dimensional highly non-linear. Team strengths _SA_ and _SB_ are non-trivial to estimate. 

To simplify the problem, we specify a simple model to allow exact calculation of in-game win probabilities. 

Each team has an equal number of possessions _N_ . 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Simulation Setup 





- Estimating the win probability function _f_ is difficult in practice. Game state ( _G, t_ ) is multi-dimensional highly non-linear. Team strengths _SA_ and _SB_ are non-trivial to estimate. 

- To simplify the problem, we specify a simple model to allow exact calculation of in-game win probabilities. 

   - Each team has an equal number of possessions _N_ . 



- Team strengths _pA_ and _pB_ are fixed and correspond to each team’s probability of scoring on a given possession. Ties are broken by a weighted coin flip (overtime). 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Simulation Setup 



Estimating the win probability function _f_ is difficult in practice. 





- Game state ( _G, t_ ) is multi-dimensional highly non-linear. Team strengths _SA_ and _SB_ are non-trivial to estimate. 



To simplify the problem, we specify a simple model to allow exact calculation of in-game win probabilities. 





Each team has an equal number of possessions _N_ . 

- Team strengths _pA_ and _pB_ are fixed and correspond to each team’s probability of scoring on a given possession. Ties are broken by a weighted coin flip (overtime). 



So the win prob. for each possible game state ( _G, t_ ) is given by 

WP _A_ ( _t_ ) = P [Binom( _nt, pA_ ) + score _A_ ( _t_ ) _>_ Binom( _nt, pB_ ) + score _B_ ( _t_ )] 



where _nt_ = _N − t_ is the number of possessions remaining. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 









For each set of parameters _N, pA, pB_ , we do the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 









For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 



<!-- Start of picture text -->
1<br><!-- End of picture text -->

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 









For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 2 Simulate 10,000 games between two teams. 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 









For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 2 Simulate 10,000 games between two teams. 3 Extract the maximum win prob. attained by the eventual loser ( _Mℓ_ ). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 











For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 2 Simulate 10,000 games between two teams. 3 Extract the maximum win prob. attained by the eventual loser ( _Mℓ_ ). We consider the distribution of _Mℓ_ as _N, pA_ , and _pB_ vary. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 











For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 2 Simulate 10,000 games between two teams. 3 Extract the maximum win prob. attained by the eventual loser ( _Mℓ_ ). We consider the distribution of _Mℓ_ as _N, pA_ , and _pB_ vary. Case 1: _pA_ = _pB_ , _f_ is symmetric across teams 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Simulation Setup 





For each set of parameters _N, pA, pB_ , we do the following: 1 Calculate the win prob. for each possible game state ( _G, t_ ) 2 Simulate 10,000 games between two teams. 3 Extract the maximum win prob. attained by the eventual loser ( _Mℓ_ ). We consider the distribution of _Mℓ_ as _N, pA_ , and _pB_ vary. Case 1: _pA_ = _pB_ , _f_ is symmetric across teams Case 2: _pA_ = _pB_ , _f_ is asymmetric across teams 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Symmetric Case: _pA_ = _pB_ 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>7 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Symmetric Case: Threshold Plot 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>8 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Symmetric Case: Takeaways 









When _pA_ = _pB_ , the support of _Mℓ_ is [0 _._ 5 _,_ 1). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Symmetric Case: Takeaways 











When _pA_ = _pB_ , the support of _Mℓ_ is [0 _._ 5 _,_ 1). Holding _N_ constant, the distribution of _Mℓ_ is identical for all values of _pA_ = _pB_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Symmetric Case: Takeaways 





When _pA_ = _pB_ , the support of _Mℓ_ is [0 _._ 5 _,_ 1). Holding _N_ constant, the distribution of _Mℓ_ is identical for all values of _pA_ = _pB_ . 

Implies that the distribution of _Mℓ_ may depend only on some measure of the difference in probabilities (e.g., _|pA − pB |_ , _p_<sup>_<u>p</u>_</sup> _B_<sup>_<u>A</u>_,</sup><sup>_. . ._).</sup> 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Symmetric Case: Takeaways 













When _pA_ = _pB_ , the support of _Mℓ_ is [0 _._ 5 _,_ 1). Holding _N_ constant, the distribution of _Mℓ_ is identical for all values of _pA_ = _pB_ . 

Implies that the distribution of _Mℓ_ may depend only on some measure of the difference in probabilities (e.g., _|pA − pB |_ , _p_<sup>_<u>p</u>_</sup> _B_<sup>_<u>A</u>_,</sup><sup>_. . ._).</sup> Holding _pA_ = _pB_ constant, the distribution of _Mℓ_ becomes less discrete and approaches a continuous limit as _N_ increases. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Symmetric Case: Takeaways 









When _pA_ = _pB_ , the support of _Mℓ_ is [0 _._ 5 _,_ 1). Holding _N_ constant, the distribution of _Mℓ_ is identical for all values of _pA_ = _pB_ . 

Implies that the distribution of _Mℓ_ may depend only on some measure of the difference in probabilities (e.g., _|pA − pB |_ , _p_<sup>_<u>p</u>_</sup> _B_<sup>_<u>A</u>_,</sup><sup>_. . ._).</sup> Holding _pA_ = _pB_ constant, the distribution of _Mℓ_ becomes less discrete and approaches a continuous limit as _N_ increases. In **about half** of all games, the losing team attains a win probability of at least **66% or more** . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Asymmetric Case: _pA_ = _pB_ 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>10 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Asymmetric Case: Threshold Plot 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>11 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Asymmetric Case: Takeaways 









When _pA_ = _pB_ , the support of _Mℓ_ is [min _{pA, pB },_ 1). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Asymmetric Case: Takeaways 











When _pA_ = _pB_ , the support of _Mℓ_ is [min _{pA, pB },_ 1). Holding _N_ constant, the distribution of _Mℓ_ is constant whenever _|pA − pB |_ is constant. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Asymmetric Case: Takeaways 











When _pA_ = _pB_ , the support of _Mℓ_ is [min _{pA, pB },_ 1). Holding _N_ constant, the distribution of _Mℓ_ is constant whenever _|pA − pB |_ is constant. 

Implies that the distribution of _Mℓ_ depends only on the absolute difference in probabilities _|pA − pB |_ . 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Asymmetric Case: Takeaways 







When _pA_ = _pB_ , the support of _Mℓ_ is [min _{pA, pB },_ 1). Holding _N_ constant, the distribution of _Mℓ_ is constant whenever _|pA − pB |_ is constant. 

Implies that the distribution of _Mℓ_ depends only on the absolute difference in probabilities _|pA − pB |_ . 



Holding _N_ constant, the distribution of _Mℓ_ becomes increasingly right-skewed over the support as _|pA − pB |_ increases. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Asymmetric Case: Takeaways 





When _pA_ = _pB_ , the support of _Mℓ_ is [min _{pA, pB },_ 1). Holding _N_ constant, the distribution of _Mℓ_ is constant whenever _|pA − pB |_ is constant. 



Implies that the distribution of _Mℓ_ depends only on the absolute difference in probabilities _|pA − pB |_ . 



Holding _N_ constant, the distribution of _Mℓ_ becomes increasingly right-skewed over the support as _|pA − pB |_ increases. 



Larger strength differentials decrease the proportion of games where the losing team attains a high win probability. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 



We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 



We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: _Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 



We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: _Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 



We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. 







<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 





We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: _Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. Then we can define Team _A_ ’s win probability at each time step _k_ as a Doob martingale: 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 





We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: _Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. Then we can define Team _A_ ’s win probability at each time step _k_ as a Doob martingale: 





From here, define the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 





We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. Then we can define Team _A_ ’s win probability at each time step _k_ as a Doob martingale: 





From here, define the following: 

_MA_ = max0 _≤k≤N pk_ is the maximum win probability team _A_ attains. 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Closed-Form Solution 





We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. Then we can define Team _A_ ’s win probability at each time step _k_ as a Doob martingale: 





From here, define the following: 

_MA_ = max0 _≤k≤N pk_ is the maximum win probability team _A_ attains. _τx_ = min _{k ≤ N_ : _pk ≥ x}_ is the first time _pk_ exceeds _x_ . 





<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Towards a Closed-Form Solution 



We hope to derive a closed-form solution for the distribution of _Mℓ_ in our simplified model. To do this, we define the following: 







_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . _Y_ = **1** _{XN ≥_ 0 _}_ is the event that team _A_ wins the game. 



Then we can define Team _A_ ’s win probability at each time step _k_ as a Doob martingale: 





From here, define the following: 





_MA_ = max0 _≤k≤N pk_ is the maximum win probability team _A_ attains. _τx_ = min _{k ≤ N_ : _pk ≥ x}_ is the first time _pk_ exceeds _x_ . 



Since _τx_ is a stopping time, we invoke the optional stopping theorem to derive the distribution of _MA_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 



**Theorem 1:** The distribution of _MA_ satisfies: 

_FMA_ ( _x_ ) _≥_ 1 _−_<sup>_<u>p</u>_0</sup> _x ∈_ [ _p_ 0 _,_ 1) _x_<sup>_,_</sup> with equality when P( _τx_ = _N_ ) = 0 (continuous limits).<sup>1</sup> 

> 1Note that _MA_ has a point mass of weight _p_ 0 at 1. <mark>Pipping & Wyner (UPenn) A Paradox of Blown Leads</mark> 

<mark>14 / 30</mark> 

<mark>NESSIS 2025</mark> 

# Closed-Form Distributions: Discrete Case 



**Theorem 1:** The distribution of _MA_ satisfies: 





with equality when P( _τx_ = _N_ ) = 0 (continuous limits).<sup>1</sup> **Theorem 2:** The conditional distribution of _MA_ given that team _A_ loses satisfies: 



with equality when P( _τx_ = _N_ ) = 0 (continuous limits) 

> 1Note that _MA_ has a point mass of weight _p_ 0 at 1. <mark>Pipping & Wyner (UPenn) A Paradox of Blown Leads</mark> 

<mark>14 / 30</mark> 

<mark>NESSIS 2025</mark> 

Closed-Form Distributions: Discrete Case 









What about the distribution for team _B_ ? 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 



What about the distribution for team _B_ ? Recall that team _B_ ’s path is just a reflection of team _A_ ’s! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 



What about the distribution for team _B_ ? Recall that team _B_ ’s path is just a reflection of team _A_ ’s! So _MB_ has a similar form to _MA_ , but with _p_ 0 replaced by 1 _− p_ 0. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 





What about the distribution for team _B_ ? Recall that team _B_ ’s path is just a reflection of team _A_ ’s! So _MB_ has a similar form to _MA_ , but with _p_ 0 replaced by 1 _− p_ 0. So then what about the distribution of the **eventual** loser _Mℓ_ ? 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 





What about the distribution for team _B_ ? Recall that team _B_ ’s path is just a reflection of team _A_ ’s! So _MB_ has a similar form to _MA_ , but with _p_ 0 replaced by 1 _− p_ 0. So then what about the distribution of the **eventual** loser _Mℓ_ ? This is a **mixture** of the distributions ( _MA|A_ loses) and ( _MB |B_ loses) with weights (1 _− p_ 0) and _p_ 0, respectively. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Discrete Case 





What about the distribution for team _B_ ? Recall that team _B_ ’s path is just a reflection of team _A_ ’s! So _MB_ has a similar form to _MA_ , but with _p_ 0 replaced by 1 _− p_ 0. So then what about the distribution of the **eventual** loser _Mℓ_ ? This is a **mixture** of the distributions ( _MA|A_ loses) and ( _MB |B_ loses) with weights (1 _− p_ 0) and _p_ 0, respectively. But wait! In the region [min( _p_ 0 _,_ 1 _− p_ 0) _,_ max( _p_ 0 _,_ 1 _− p_ 0)), the distribution of _Mℓ_ comes entirely from the underdog! So we must define the distribution of _Mℓ_ piecewise. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Closed-Form Distributions: Discrete Case 



What about the distribution for team _B_ ? 



Recall that team _B_ ’s path is just a reflection of team _A_ ’s! So _MB_ has a similar form to _MA_ , but with _p_ 0 replaced by 1 _− p_ 0. So then what about the distribution of the **eventual** loser _Mℓ_ ? This is a **mixture** of the distributions ( _MA|A_ loses) and ( _MB |B_ loses) with weights (1 _− p_ 0) and _p_ 0, respectively. 

But wait! In the region [min( _p_ 0 _,_ 1 _− p_ 0) _,_ max( _p_ 0 _,_ 1 _− p_ 0)), the distribution of _Mℓ_ comes entirely from the underdog! So we must define the distribution of _Mℓ_ piecewise. 





**Theorem 3:** Since team labels are arbitrary, let team _A_ be the favorite ( _p_ 0 _≥_ 0 _._ 5). Then the distribution of _Mℓ_ satisfies: 



with equality when P( _τx_ = _N_ ) = 0 (continuous limits) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 



The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 





The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 





The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 





The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. Then _WPA_ (0) = 0 _._ 5 and _WPA_ (1) = _{_ 0 _,_ 1 _}_ , jumping the rest! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 





The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. 

- For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. Then _WPA_ (0) = 0 _._ 5 and _WPA_ (1) = _{_ 0 _,_ 1 _}_ , jumping the rest! What we need to prevent this behavior is **continuous sample paths** , which prevents the process from jumping over levels. 







<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 







The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. 

- For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. Then _WPA_ (0) = 0 _._ 5 and _WPA_ (1) = _{_ 0 _,_ 1 _}_ , jumping the rest! What we need to prevent this behavior is **continuous sample paths** , which prevents the process from jumping over levels. 

- How do we get continuous sample paths? By letting _N →∞_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# From Inequalities to Equality: The Brownian Limit 







- The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. Then _WPA_ (0) = 0 _._ 5 and _WPA_ (1) = _{_ 0 _,_ 1 _}_ , jumping the rest! What we need to prevent this behavior is **continuous sample paths** , which prevents the process from jumping over levels. 

How do we get continuous sample paths? By letting _N →∞_ . In this limit, the process becomes continuous and we can derive exact closed-form expressions for the distributions of _MA_ , _MB_ , and _Mℓ_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# From Inequalities to Equality: The Brownian Limit 





The inequalities in Theorems 1-3 are tight, but what if we want something stronger, like a density equality? What’s the limitation? In discrete time, there are **finitely-many** levels for _WPA_ and _WPB_ , so the process can “jump over” level _x_ at the final step. 







- For example, consider the simplest case: _N_ = 1 and _p_ 0 = 0 _._ 5. Then _WPA_ (0) = 0 _._ 5 and _WPA_ (1) = _{_ 0 _,_ 1 _}_ , jumping the rest! What we need to prevent this behavior is **continuous sample paths** , which prevents the process from jumping over levels. 



How do we get continuous sample paths? By letting _N →∞_ . 





- In this limit, the process becomes continuous and we can derive exact closed-form expressions for the distributions of _MA_ , _MB_ , and _Mℓ_ . In addition, **Donsker’s Invariance Principle** allows us to approximate the scoring process _Xk_ with a Brownian motion! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>16 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: _Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . 





<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . Then define the following quantities: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . Then define the following quantities: 

_µ_ = _pA − pB_ is the difference in scoring probabilities. 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 

_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . 



_Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . Then define the following quantities: 

- _µ_ = _pA − pB_ is the difference in scoring probabilities. 



- _σ_<sup>2</sup> = _pA_ (1 _− pA_ ) + _pB_ (1 _− pB_ ) is the variance of each step in the scoring process. 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Towards a Continuous Closed-Form 



We hope to derive a continuous closed-form for the distribution of _Mℓ_ in our simplified model. Like before, we have: 



_Xk_ = score _A_ ( _k_ ) _−_ score _B_ ( _k_ ) is the score differential at time _k_ . _Fk_ = _σ_ ( _X_ 0 _, . . . , Xk_ ) is the set of information available at time _k_ . Then define the following quantities: 





_µ_ = _pA − pB_ is the difference in scoring probabilities. _σ_<sup>2</sup> = _pA_ (1 _− pA_ ) + _pB_ (1 _− pB_ ) is the variance of each step in the scoring process. 



Then by Donsker’s Invariance Principle, we have that 



where _Bt_ is standard Brownian motion. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>17 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Towards a Continuous Closed-Form 









From here, note the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



From here, note the following: The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



## From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. 





<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 



## From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). 







<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). Now we can define Team _A_ ’s win probability as a Doob martingale: 

_pt_ = E[ _Y | Ft_ ] _, t ∈_ [0 _,_ 1] 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). Now we can define Team _A_ ’s win probability as a Doob martingale: 

_pt_ = E[ _Y | Ft_ ] _, t ∈_ [0 _,_ 1] 



Then we can define the following quantities: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). Now we can define Team _A_ ’s win probability as a Doob martingale: 

_pt_ = E[ _Y | Ft_ ] _, t ∈_ [0 _,_ 1] 



Then we can define the following quantities: 

_M_ = sup _pt_ is the maximum win probability team _A_ attains. 0 _≤t≤_ 1 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Towards a Continuous Closed-Form 





From here, note the following: 

The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). Now we can define Team _A_ ’s win probability as a Doob martingale: 

_pt_ = E[ _Y | Ft_ ] _, t ∈_ [0 _,_ 1] 



Then we can define the following quantities: 

_M_ = sup _pt_ is the maximum win probability team _A_ attains. 0 _≤t≤_ 1 _τx_ = inf _{t ∈_ [0 _,_ 1] : _pt_ = _x}_ is the first time _pt_ exceeds _x_ . 





<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Towards a Continuous Closed-Form 



From here, note the following: 



The discrete terminal event _{XN ≥_ 0 _}_ converges to _{B_ 1 + _µ_<sup>_∗_</sup> _≥_ 0 _}_ . So _Y_ = **1** _{B_ 1+ _µ∗≥_ 0 _}_ is the event that team _A_ wins the game. _p_ 0 = P( _Y_ = 1) = Φ( _µ_<sup>_∗_</sup> ). Now we can define Team _A_ ’s win probability as a Doob martingale: 

_pt_ = E[ _Y | Ft_ ] _, t ∈_ [0 _,_ 1] 



Then we can define the following quantities: 



_M_ = sup _pt_ is the maximum win probability team _A_ attains. 0 _≤t≤_ 1 _τx_ = inf _{t ∈_ [0 _,_ 1] : _pt_ = _x}_ is the first time _pt_ exceeds _x_ . Then we invoke the optional stopping theorem and use properties of Brownian motion to derive the distribution of _MA, MB_ , and _Mℓ_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>18 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Continuous Case 



**Theorem 4:** The distribution of _MA_ satisfies: 

_FMA_ ( _x_ ) = 1 _−_<sup>_<u>p</u>_0</sup> _, x ∈_ [Φ( _µ_<sup>_∗_</sup> ) _,_ 1) _x_<sup>= 1</sup><sup>_−_Φ(</sup> _x_<sup>_<u>µ∗</u>_</sup><sup><u>)</u></sup> 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>19 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Closed-Form Distributions: Continuous Case 



**Theorem 4:** The distribution of _MA_ satisfies: 





**Theorem 5:** The conditional distribution of _MA_ given that team _A_ loses satisfies: 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>19 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Closed-Form Distributions: Continuous Case 









What about the distribution for team _B_ ? 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>20 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Continuous Case 



What about the distribution for team _B_ ? In the discrete case, we just replaced _p_ 0 with 1 _− p_ 0. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>20 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Continuous Case 



What about the distribution for team _B_ ? In the discrete case, we just replaced _p_ 0 with 1 _− p_ 0. So in the continuous case, we just replace Φ( _µ_<sup>_∗_</sup> ) with Φ( _−µ_<sup>_∗_</sup> ). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>20 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Distributions: Continuous Case 





What about the distribution for team _B_ ? In the discrete case, we just replaced _p_ 0 with 1 _− p_ 0. So in the continuous case, we just replace Φ( _µ_<sup>_∗_</sup> ) with Φ( _−µ_<sup>_∗_</sup> ). We saw in the discrete case that the distribution of _Mℓ_ is a piecewise mixture. We use a similar logic to derive the distribution of _Mℓ_ . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>20 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Closed-Form Distributions: Continuous Case 



What about the distribution for team _B_ ? In the discrete case, we just replaced _p_ 0 with 1 _− p_ 0. So in the continuous case, we just replace Φ( _µ_<sup>_∗_</sup> ) with Φ( _−µ_<sup>_∗_</sup> ). 





We saw in the discrete case that the distribution of _Mℓ_ is a piecewise mixture. We use a similar logic to derive the distribution of _Mℓ_ . **Theorem 6:** Since team labels are arbitrary, let team _A_ be the favorite ( _µ_<sup>_∗_</sup> _≥_ 0). Then the distribution of _Mℓ_ satisfies 



where _p_ 0 = Φ( _µ_<sup>_∗_</sup> ). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>20 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Closed-Form Examples 









In evenly-matched games, we have the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Closed-Form Examples 









In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Examples 



In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Examples 





In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> In unevenly-matched games, we have the following: 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Examples 





In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> In unevenly-matched games, we have the following: Starting win probabillities differ ( _p_ 0 = 0 _._ 5). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Examples 





In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> In unevenly-matched games, we have the following: Starting win probabillities differ ( _p_ 0 = 0 _._ 5). _Mℓ_ is distributed **piecewise** over _x ∈_ [ _p_ 0<sup>(dog)</sup> _,_ 1). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# Closed-Form Examples 





In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> In unevenly-matched games, we have the following: Starting win probabillities differ ( _p_ 0 = 0 _._ 5). _Mℓ_ is distributed **piecewise** over _x ∈_ [ _p_ 0<sup>(dog)</sup> _,_ 1). From [ _p_ 0<sup>(dog)</sup> _, p_ 0<sup>(fav)</sup> ), only the underdog’s maxima contribute. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Closed-Form Examples 





In evenly-matched games, we have the following: Each team’s starting win probability ( _p_ 0) is 0 _._ 5. _FMℓ_ ( _x_ ) = 2 _− x_<sup><u>1</u>uniformlyoverall</sup><sup>_x∈_[0</sup><sup>_._5</sup><sup>_,_1).</sup> In unevenly-matched games, we have the following: Starting win probabillities differ ( _p_ 0 = 0 _._ 5). _Mℓ_ is distributed **piecewise** over _x ∈_ [ _p_ 0<sup>(dog)</sup> _,_ 1). From [ _p_ 0<sup>(dog)</sup> _, p_ 0<sup>(fav)</sup> ), only the underdog’s maxima contribute. From [ _p_ 0<sup>(fav)</sup> _,_ 1), both teams’ maxima contribute. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>21 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# But Wait. . . Does This Even Matter? 



The math is clean, but it’s still a major simplification of sports! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# But Wait. . . Does This Even Matter? 



The math is clean, but it’s still a major simplification of sports! Scoring often isn’t binary! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# But Wait. . . Does This Even Matter? 



The math is clean, but it’s still a major simplification of sports! Scoring often isn’t binary! True team scoring probabilities may vary throughout a game! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# But Wait. . . Does This Even Matter? 



## The math is clean, but it’s still a major simplification of sports! 

Scoring often isn’t binary! 



- True team scoring probabilities may vary throughout a game! Teams often have an unequal number of possessions! 





<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 







# But Wait. . . Does This Even Matter? 



## The math is clean, but it’s still a major simplification of sports! 

- Scoring often isn’t binary! 



- True team scoring probabilities may vary throughout a game! Teams often have an unequal number of possessions! Weather, injuries, game strategy, and other external factors matter! 







<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# But Wait. . . Does This Even Matter? 





- The math is clean, but it’s still a major simplification of sports! Scoring often isn’t binary! 

- True team scoring probabilities may vary throughout a game! Teams often have an unequal number of possessions! Weather, injuries, game strategy, and other external factors matter! 

- Let’s take a look at the distribution of _Mℓ_ for real-life games. . . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>22 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Evenly-Matched NFL Games (2002–2024, _|_ Spread _| <_ 2) 



Data via nflfastR (2002–2024) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>23 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Evenly-Matched NFL Games (2002–2024, _|_ Spread _| <_ 2) 



Data via nflfastR (2002–2024) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>24 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Unevenly-Matched NFL Games: 2002–2024, _|_ Spread _|_ = 3 



Data via nflfastR (2002–2024) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>25 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Unevenly-Matched NFL Games: 2002–2024, _|_ Spread _|_ = 3 



Data via nflfastR (2002–2024) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>26 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 









Our solutions closely match the empirical distribution of the maximum win probability of the eventual loser ( _Mℓ_ )! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>27 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 











Our solutions closely match the empirical distribution of the maximum win probability of the eventual loser ( _Mℓ_ )! Blown leads happen **all the time** , especially in even matchups! 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>27 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 







Our solutions closely match the empirical distribution of the maximum win probability of the eventual loser ( _Mℓ_ )! Blown leads happen **all the time** , especially in even matchups! Conditioning on an eventual loss **fundamentally changes** the distribution of the maximum win probability attained. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>27 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 









In Super Bowl LVII, the Eagles reached a maximum win probability of 78.4% before ultimately losing. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>28 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 











In Super Bowl LVII, the Eagles reached a maximum win probability of 78.4% before ultimately losing. 

From this position (assuming a well-calibrated model) **it’s true** that the Eagles only had a 21.6% chance of losing the game. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>28 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Conclusions 







In Super Bowl LVII, the Eagles reached a maximum win probability of 78.4% before ultimately losing. 

From this position (assuming a well-calibrated model) **it’s true** that the Eagles only had a 21.6% chance of losing the game. However, the event that the eventual loser of this game reached 78.4% is **provably closer** to 30%. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>28 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Acknowledgements 





Special thanks to Professor Jiaoyang Huang, Dr. Paul Sabin, and Dr. Ryan Brill for their helpful feedback. All work supported by the Wharton Sports Analytics & Business Initiative (WSABI) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>29 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

References 







Donsker, M. D. (1951). An invariance principle for certain probability limit theorems. _Memoirs of the American Mathematical Society_ , 6. Doob, J. L. (1953). _Stochastic Processes_ . New York: John Wiley & Sons. nflfastR: Carl, S. and Baldwin, B. (2025). _nflfastR: Functions to Efficiently Access NFL Play by Play Data_ . R package version 5.1.0.9000. Available at `https://www.nflfastr.com/` . 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>30 / 30</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 1 



**Theorem 1:** When _pA_ = _pB_ , the cumulative distribution of _M_ satisfies 

_FM_ ( _x_ ) _≥_ 1 _−_<sup>_<u>p</u>_0</sup> _x ∈_ [ _p_ 0 _,_ 1) _x_<sup>_,_</sup> with equality exactly when P( _τx_ = _N_ ) = 0. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>1 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 1 (continued) 





If _x ≤ p_ 0, then _τx_ = 0 a.s., so _M ≥ x_ a.s. and _FM_ ( _x_ ) = 0. For _x > p_ 0, by the optional stopping theorem on the bounded martingale ( _pk_ ) at _τx ∧ N_ : 





Decomposing this: 



_p_ 0 = E[ _pτx_ **1** _{τx <N}_ ] + E[ _pN_ **1** _{τx_ = _N}_ ] Since _pτx_ = _x_ on _{τx < N}_ and _pN_ = 1 on _{τx_ = _N}_ : 

_p_ 0 = _x_ P( _τx < N_ ) + P( _τx_ = _N_ ) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>2 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 1 (continued) 



Since P( _M ≥ x_ ) = P( _τx < N_ ) + P( _τx_ = _N_ ): 





For _x <_ 1, P( _τx_ = _N_ ) _≥_ 0 and we have: 





with equality exactly when P( _τx_ = _N_ ) = 0. When _x_ = 1, _τx_ = _N_ a.s., so: 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>3 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 2 



**Theorem 2:** When _pA_ = _pB_ , the cumulative distribution of _M_ conditional on _Y_ = 0 satisfies 



with equality exactly when P( _τx_ = _N_ ) = 0. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>4 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 2 (continued) 





P( _M ≥ x_ ) = P( _M ≥ x, Y_ = 0) + P( _M ≥ x, Y_ = 1) 



On _{Y_ = 1 _}_ , _pN_ = 1 _≥ x_ a.s. So _{M ≥ x} ∩{Y_ = 1 _}_ = _{Y_ = 1 _}_ : 





= _p_ 0 + (1 _− p_ 0)P( _M ≥ x | Y_ = 0) 









with equality exactly when P( _τx_ = _N_ ) = 0. 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>5 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 3 



**Theorem 3:** When _pA_ = _pB_ , the distribution of _Mℓ_ satisfies 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>6 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 3 (continued) 





Since _pA_ = _pB_ , we have _p_ 0 = 0 _._ 5 and the mixture weights are equal. From Theorem 2, both conditional distributions are identical: 





Since both teams have identical distributions, the mixture is simply: 

_FMℓ_ ( _x_ ) _≥_ 0 _._ 5 _· FMA|Y_ =0( _x_ ) + 0 _._ 5 _· FMB |Y_ =1( _x_ ) = 1 _−_<sup>1</sup><sup>_−x_</sup> = 2 _−_<sup>1</sup> _x x_ 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>7 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 4 



**Theorem 4:** When _pA_ = _pB_ , the cumulative distribution of _M_ satisfies 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>8 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 4 (continued) 



By the optional stopping theorem on the bounded martingale ( _pt_ ) at _τx ∧_ 1: 





Decomposing this: 

_p_ 0 = E[ _pτx_ **1** _{τx <_ 1 _}_ ] + E[ _p_ 1 **1** _{τx_ =1 _}_ ] 



Since _pτx_ = _x_ on _{τx <_ 1 _}_ and _p_ 1 = 1 on _{τx_ = 1 _}_ : 

_p_ 0 = _x_ P( _τx <_ 1) + P( _τx_ = 1) 



Since P( _M ≥ x_ ) = P( _τx <_ 1) + P( _τx_ = 1): 

_p_ 0 = _x_ P( _M ≥ x_ ) + P( _τx_ = 1) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>9 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 4 (continued) 



For _x <_ 1, P( _τx_ = 1) = 0 (continuous paths), so: 





When _x_ = 1, _τx_ = 1 a.s., so: 

P( _M ≥_ 1) = P( _M_ = 1) = _p_ 0 = Φ( _µ_<sup>_∗_</sup> ) 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>10 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 5 



**Theorem 5:** When _pA_ = _pB_ , the conditional distribution of _M_ given _Y_ = 0 satisfies 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>11 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 5 (continued) 



Decompose the event _{M ≥ x}_ : 

P( _M ≥ x_ ) = P( _M ≥ x, Y_ = 0) + P( _M ≥ x, Y_ = 1) 



On _{Y_ = 1 _}_ , _p_ 1 = 1 _≥ x_ a.s. So _{M ≥ x} ∩{Y_ = 1 _}_ = _{Y_ = 1 _}_ : 

P( _M ≥ x_ ) = P( _Y_ = 1) + P( _M ≥ x, Y_ = 0) = P( _Y_ = 1) + P( _Y_ = 0)P( _M ≥ x | Y_ = 0) = _p_ 0 + (1 _− p_ 0)P( _M ≥ x | Y_ = 0) 





From Theorem 4:<sup>_<u>p</u>_</sup><sup><u>0</u></sup><sup>_≥x| Y_= 0)</sup> _x_<sup>=</sup><sup>_p_0 + (1</sup><sup>_−p_0)P(</sup><sup>_M_</sup> Solving for P( _M ≥ x | Y_ = 0): 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>12 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

Proof of Theorem 6 



**Theorem 6:** When _pA_ = _pB_ , let team _A_ be the favorite ( _µ_<sup>_∗_</sup> _≥_ 0). Then the distribution of _Mℓ_ satisfies 



where _p_ 0 = Φ( _µ_<sup>_∗_</sup> ) and _Mℓ_ = 0 for _x ∈_ [0 _,_ 1 _− p_ 0). 

<mark>Pipping & Wyner (UPenn)</mark> 

<mark>13 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 6 (continued) 





The distribution of _Mℓ_ is a mixture: _FMℓ_ ( _x_ ) = (1 _− p_ 0) _FMA|Y_ =0( _x_ ) + _p_ 0 _FMB |Y_ =1( _x_ ). From Theorem 5, we have the conditional distributions: 



<mark>Pipping & Wyner (UPenn)</mark> 

<mark>14 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 

# Proof of Theorem 6 (continued) 













<mark>Pipping & Wyner (UPenn)</mark> 

<mark>15 / 15</mark> 

<mark>NESSIS 2025</mark> 

<mark>A Paradox of Blown Leads</mark> 


