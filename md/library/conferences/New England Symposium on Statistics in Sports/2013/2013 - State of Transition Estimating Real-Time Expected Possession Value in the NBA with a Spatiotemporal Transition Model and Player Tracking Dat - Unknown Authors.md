<!-- source: library/conferences/New England Symposium on Statistics in Sports/2013/2013 - State of Transition Estimating Real-Time Expected Possession Value in the NBA with a Spatiotemporal Transition Model and Player Tracking Dat - Unknown Authors.pdf -->

# State of Transition: 

Estimating Real-Time Expected Possession Value in the NBA with a Spatiotemporal Transition Model and Player Tracking Data 

Dan Cervone<sup>1</sup> Alex D’Amour<sup>1</sup> 

> 1XY Hoops Group, Harvard University 

September 21, 2013 

# Optical tracking data 

For the 2012-13 we have almost 800 million data points! 

- 515 games 

- 2D locations for all 10 players and 3 referees, 3D location for 

   - the ball 

- 25 images per second 

- Annotations (dribbles, passes, shots) 

Optical tracking data 



<!-- Start of picture text -->
1 4<br>2<br>5<br>3<br><!-- End of picture text -->

- Red points: Spurs (offense) 

   - 1: Parker, 2: Jackson, 3: Green, 4: Duncan, 5: Diaw 

- Purple points: Thunder (defense) 

- Orange _⊕_ : ball 



# New frontiers for analyzing NBA offenses 

|#<br>W<br>B|#|W<br>B|#|W|B|#|W<br>B|
|---|---|---|---|---|---|---|---|
|1|7||13|||19||
|2|8||14|||20||
|3|9||15|||21||
|4|10||16|||22||
|5|11||17|||23|Be7#|
|6|12||18|||||



Table: Anderssen vs Kieseritsky, 1851 

What can we learn about this chess game from “ **23. Be7#** ”? 

# New frontiers for analyzing NBA offenses 

|#|W|B|#|W|B|#|W|B|#|W|B|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|e4|e5|7|d3|Nh5|13|h5|Qg5|19|e5|Qxa1+|
|2|f4|exf4|8|Nh4|Qg5|14|Qf3|Ng8|20|Ke2|Na6|
|3|Bc4|Qh4+|9|Nf5|c6|15|Bxf4|Qf6|21|Nxg7+|Kd8|
|4|Kf1|b5|10|g4|Nf6|16|Nc3|Bc5|22|Qf6+|Nxf6|
|5|Bxb5|Nf6|11|Rg1|cxb5|17|Nd5|Qxb2|23|Be7#||
|6|Nf3|Qh6|12|h4|Qg6|18|Bd6|Bxg1||||



Table: Anderssen vs Kieseritsky, 1851 

What can we learn about this chess game from “ **23. Be7#** ”? 

Like chess matches, NBA possessions are often won/lost before the ball does/doesn’t swish through the net. 

- A teammate eludes the defense and gets open in the paint. 

- The ballcarrier skips an easy shot to pass to a heavily defended teammate. 

- With no look at the basket and no easy passes, the ballcarrier dribbles to a different spot. 

# Expected Possession Value 

How many points is a team expected to score given the spatial evolution of its possession up to time _t_ ? 

EPV = _E_ [ _X |Ft_ ] 

   - _X_ = number of points scored on this possession ( **unknown** ). 

   - _Ft_ = space-time information of the possession up to time _t_ . 

- EPV tells us 

   - When and how value was created _during_ the possession 

   - Who created the value 

   - Who made the best decisions to increase their team’s 

      - expected points 

# EPV is all about _what happens next_ 

Let _A_ be the outcome of the next decision made by a player at time _t_ . 

- We could see, for instance, _A_ = pass, _A_ = take a shot, or 

   - _A_ = dribble to basket. 

By laws of probability, 

_E_ [ _X |Ft_ ] = _E_ [ _X |Ft, A_ = pass] _P_ ( _A_ = pass _|Ft_ ) + _E_ [ _X |Ft, A_ = shoot] _P_ ( _A_ = shoot _|Ft_ ) + _E_ [ _X |Ft, A_ = dribble] _P_ ( _A_ = dribble _|Ft_ ) 

EPV is a weighted average of future EPVs, where the weights are transition probabilities. 

# Calculating EPV: step 1 

More generally, let _S_ be a binning of the full-resolution data into discrete _states_ or _events_ (e.g. “The point guard has the ball at the top of the arc”). 

Let _st ∈S_ be the state the possession is in at time _t_ . Then: 

**EPV:** _E_ [ _X |Ft_ ] = � _E_ [ _X |st_ + _ϵ_ = _s, Ft_ ] _P_ ( _st_ + _ϵ_ = _s|Ft_ ) _s∈S_ 

# Calculating EPV: step 1 

More generally, let _S_ be a binning of the full-resolution data into discrete _states_ or _events_ (e.g. “The point guard has the ball at the top of the arc”). 

Let _st ∈S_ be the state the possession is in at time _t_ . Then: 

**EPV:** _E_ [ _X |Ft_ ] = � _E_ [ _X |st_ + _ϵ_ = _s, Ft_ ] _P_ ( _st_ + _ϵ_ = _s|Ft_ ) _s∈S_ 

**Step 1 of calculating EPV is to define** _S_ . Ideally, ▶ _E_ [ _X |st_ + _ϵ_ = _s, Ft_ ] _≈ E_ [ _X |st_ + _ϵ_ = _s_ ] for all _s ∈S_ . ▶ _E_ [ _X |st_ + _ϵ_ = _s_ ] easy to calculate for all _s ∈S_ (ie, empirical average). 

# Calculating EPV: step 2 

**We need** _P_ ( _st_ + _ϵ_ = _s|Ft_ ) **for all** _s ∈S_ **.** 

- We have chosen _S_ such that for all _s_ , a good estimate of _P_ ( _st_ + _ϵ_ = _s|Ft_ ) only needs: 

   - _P_ (shot in ( _t, t_ + _ϵ_ ) _|Ft_ ) 

   - _P_ (pass in ( _t, t_ + _ϵ_ ) _|Ft_ ) 

- 6 different types of pass/shot events indexed by _j_ . 

   - Shots made, shots missed 

   - Passes to each of 4 teammates 

- Points in space-time corresponding to event _j_ when player _i_ has the ball follow an inhomogenous Poisson Process: 



- All _Yj_<sup>_i_assumedindependent.</sup> 

# Additional model details 

We additionally assume ( _i_ superscripts omitted): 

log( _λj_ ( _t_ )) = _βj_<sup>_′Wj_(</sup><sup>_t_) +</sup><sup>_Hj_(</sup><sup>_ζt_)</sup> 

where 

> ▶ _Wj_ ( _t_ ) a _p_ -vector of (possibly) time-varying covariates. 

> ▶ Distance to nearest defender; player _i_ ’s velocity; has started dribbling, etc 

> ▶ _βj ∈_ R<sup>_p_</sup> are coefficients for main effects. 

> ▶ _ζt_ is player _i_ ’s location at time _t_ . 

- _Hj_ is a spatial random effects surface (Gaussian Process). 

# Spatial random effect surfaces for _made shot events_ 



<!-- Start of picture text -->
Parker Duncan Ginobili<br>3<br>4<br>4 2<br>1 2<br>2<br>0<br>0<br>0<br>−1<br>−2<br>−2 −2<br><!-- End of picture text -->



<!-- Start of picture text -->
Green Leonard Blair<br>4 4 4<br>3 3 3<br>2 2<br>2<br>1<br>1<br>0 1<br>0<br>−1 0<br>−1<br>−2 −1<br>−2<br><!-- End of picture text -->

# Spatial random effect surfaces for _pass events_ Parker to Duncan 



<!-- Start of picture text -->
Passer surface Receiver surface<br>2.0<br>1.5<br>1.5<br>1.0<br>0.5 1.0<br>0.0 0.5<br>−0.5 0.0<br>−1.0<br>−0.5<br>−1.5<br>−1.0<br><!-- End of picture text -->

## Duncan to Parker 



<!-- Start of picture text -->
Passer surface Receiver surface<br>2 2<br>1 1<br>0 0<br>−1 −1<br>−2 −2<br><!-- End of picture text -->

# Putting it all together 



<!-- Start of picture text -->
1 4 2<br>5<br>3<br><!-- End of picture text -->

### **Pass next** : 

_E_ [ _X |_ pass] = (0 _._ 78)(0 _._ 02) + (1 _._ 08)(0 _._ 14) + (0 _._ 84)(0 _._ 37) + (0 _._ 85)(0 _._ 46) = 0 _._ 87 

_P_ (pass) = 0 _._ 97 

**Shoot next** : 

_E_ [ _X |_ shot] = (3 _._ 00)(0 _._ 18) + (0 _._ 18)(0 _._ 82) = 0 _._ 69 

_P_ (shot) = 0 _._ 03 

- 1: Parker 

### **EPV** : 

- 2: Jackson 

- 3: Green 

- 4: Duncan 

(0 _._ 87)(0 _._ 97) + (0 _._ 69)(0 _._ 03) = **0** _._ **86** 

- 5: Diaw 

EPV in real-time 



# EPV during a possession 



<!-- Start of picture text -->
Parker poss.<br>Jackson poss.<br>Duncan poss.<br>Shot attempt<br>5 10 15<br>time<br>1.6<br>1.4<br>EPV 1.2<br>1.0<br>0.8<br><!-- End of picture text -->

# EPV during game 

|Player|Summed (_△_EPV)|
|---|---|
|Duncan|1.54|
|Jackson|0.50|
|Parker|1.44|
|Diaw|-0.02|
|Neal|0.40|
|Green|0.55|
|Blair|-1.21|
|Leonard|0.36|



Table: Total change in Spurs’ players’ EPV while they were handling the ball during November 1, 2012 game against OKC 

- Interpretation: Value added by players’ decision-making in this game _relative to their usual value_ . 

# The future of EPV 

EPV is a powerful new tool for analysing NBA offenses: 

- Diagrams where and how points are scored 

- Can track EPV in real-time as the possession evolves 

- Allows evaluation and quantification of players’ 

   - decision-making 

- In modeling EPV, we discover factors (including spatial effects) that influence players’ decision-making 

Nuances: 

- Players can’t systematically increase EPV 

- EPV as a measure of skill 

Future challenges: 

- Incorporating defense 

- Information-sharing across similar players (hierarchical models) 


