<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Evaluating plate discipline in Major League Baseball with Bayesian Additive Regression Trees - Unknown Authors.pdf -->

Ryan Yee 

University of Wisconsin – Madison Department of Statistics 

New England Symposium on Statistics in Sports September 23, 2023 



What is the optimal decision? 









<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 2 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 



# What is the optimal decision? 









<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 2 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 



# What is the optimal decision? 









<!-- Start of picture text -->
HOME 2<br>AWAY 3<br>7 2 Outs 1-2<br><!-- End of picture text -->



<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 2 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 



# What is the optimal decision? 









<!-- Start of picture text -->
HOME 2<br>AWAY 3<br>7 2 Outs 1-2<br>Batter: Shohei Ohtani<br>Umpire: Angel ´ Hern´andez<br><!-- End of picture text -->



<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 2 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Evaluating Plate Discipline 



- It is not enough to just look at location... 

   - Analysis depends on location, game factors, and personnel 

   - Some pitches are harder to evaluate that others 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>3 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Evaluating Plate Discipline 



- It is not enough to just look at location... 

   - Analysis depends on location, game factors, and personnel 

   - Some pitches are harder to evaluate that others 

- Traditional plate discipline metrics: `O-Swing%` , `Z-Swing%` 

   - Analysis relies solely on the location of the pitch 

   - Treats every pitch inside (outside) the strike zone the same 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>3 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Evaluating Plate Discipline 



- It is not enough to just look at location... 

   - Analysis depends on location, game factors, and personnel 

   - Some pitches are harder to evaluate that others 

- Traditional plate discipline metrics: `O-Swing%` , `Z-Swing%` 

   - Analysis relies solely on the location of the pitch 

   - Treats every pitch inside (outside) the strike zone the same 

- Our Contribution 

   - Introduce framework for evaluating plate discipline which accounts for contextual factors in addition to location 

   - Framework facilitates uncertainty quantification in evaluations 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>3 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

Framework 



<!-- Start of picture text -->
E[ R| swing  = 1]<br>Swing 1 −P ( contact )<br>Decision<br>Take P ( strike )<br>E[ R| swing  = 0]<br>1 −P ( strike )<br>The optimal decision is to swing if E[ R|<br><!-- End of picture text -->



_R|_ `swing` = 1 Swing Take _R|_ `swing` = 0 

**Decision** 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>4 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

Framework 



<!-- Start of picture text -->
E[ R| swing  = 1]<br>Swing 1 −P ( contact )<br>Decision<br>Take P ( strike )<br>E[ R| swing  = 0]<br>1 −P ( strike )<br>The optimal decision is to swing if E[ R|<br><!-- End of picture text -->



_R|_ `swing` = 1 Swing **Decision** Take _R|_ `swing` = 0 

The optimal decision is to swing if _R|_ `swing` = 1 _> R|_ `swing` = 0 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>4 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

Framework 



<!-- Start of picture text -->
R| swing  = 1<br>Swing 1 −P ( contact )<br>Decision<br>Take P ( strike )<br>R| swing  = 0<br>1 −P ( strike )<br><!-- End of picture text -->



E[ _R|_ `swing` = 1] Swing **Decision** Take E[ _R|_ `swing` = 0] 

The optimal decision is to swing if E[ _R|_ `swing` = 1] _>_ E[ _R|_ `swing` = 0] 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 4 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 



<!-- Start of picture text -->
Swing 1  −P ( contact )<br>Decision<br>Take P ( strike )<br>R| swing  = 0<br>1 −P ( strike )<br><!-- End of picture text -->

# Framework 





<!-- Start of picture text -->
E[ R| swing  = 1 ,  contact  = 1]<br>P ( contact )<br>E[ R| swing  = 1]<br>Swing 1  −P ( contact )<br>E[ R| swing  = 1 ,  contact  = 0]<br>Decision<br>Take<br>E[ R| swing  = 0]<br><!-- End of picture text -->

The optimal decision is to swing if E[ _R|_ `swing` = 1] _>_ E[ _R|_ `swing` = 0] 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 4 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 

Framework 



<!-- Start of picture text -->
Swing 1  −P ( contact )<br>Decision<br>Take P ( strike )<br>R| swing  = 0<br>1  −P ( strike )<br><!-- End of picture text -->



E[ _R|_ `swing` = 1 _,_ `contact` = 1] _P_ ( `contact` ) E[ _R|_ `swing` = 1] Swing 1 _−P_ ( `contact` ) E[ _R|_ `swing` = 1 _,_ `contact` = 0] E[ _R|_ `swing` = 1 _,_ `strike` = 1] Take _P_ ( `strike` ) E[ _R|_ `swing` = 0] 1 _−P_ ( `strike` ) E[ _R|_ `swing` = 1 _,_ `strike` = 0] 

**Decision** 

The optimal decision is to swing if E[ _R|_ `swing` = 1] _>_ E[ _R|_ `swing` = 0] 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 4 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 

Framework 



<!-- Start of picture text -->
Swing 1  −P ( contact )<br>Decision<br>Take P ( strike )<br>R| swing  = 0<br>1  −P ( strike )<br><!-- End of picture text -->





<!-- Start of picture text -->
E[ R| swing  = 1 ,  contact  = 1]<br>P ( contact )<br>E[ R| swing  = 1]<br>Swing 1  −P ( contact )<br>E[ R| swing  = 1 ,  contact  = 0]<br>Decision<br>E[ R| swing  = 1 ,  strike  = 1]<br>Take P ( strike )<br>E[ R| swing  = 0]<br>1  −P ( strike )<br>E[ R| swing  = 1 ,  strike  = 0]<br><!-- End of picture text -->

The optimal decision is to swing if E[ _R|_ `swing` = 1] _>_ E[ _R|_ `swing` = 0] 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>NESSIS 2023 4 / 7</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Estimation 



- Desiderata: estimate each intermediate quantity as functions of their conditioning variables 

_P_ ( `strike` ) = _f_ ( `game state, personnel, location, ...` ) 

- Nonlinear 

- Complex interactions 

- Functional form difficult to specify 

- Propagate uncertainties from constituent models 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>5 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Estimation 



- Desiderata: estimate each intermediate quantity as functions of their conditioning variables 

_P_ ( `strike` ) = _f_ ( `game state, personnel, location, ...` ) 

   - Nonlinear 

   - Complex interactions 

   - Functional form difficult to specify 

   - Propagate uncertainties from constituent models 

- Solution: Bayesian Additive Regression Trees (BART; see Chipman, et. al.) 

   - Nonparametric Bayesian model that approximates the target function through an ensemble of piecewise constant step functions 

   - Ideal for modeling complex interactions due to tree-based structure 

   - Do not need to specify the functional form of the function 

   - Generates samples from the posterior distribution of target function 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>5 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Estimation 



- Desiderata: estimate each intermediate quantity as functions of their conditioning variables 

_P_ ( `strike` ) = _f_ ( `game state, personnel, location, ...` ) 

   - Nonlinear 

   - Complex interactions 

   - Functional form difficult to specify 

   - Propagate uncertainties from constituent models 

- Solution: Bayesian Additive Regression Trees (BART; see Chipman, et. al.) 

   - Nonparametric Bayesian model that approximates the target function through an ensemble of piecewise constant step functions 

   - Ideal for modeling complex interactions due to tree-based structure 

   - Do not need to specify the functional form of the function 

   - Generates samples from the posterior distribution of target function 

- Use same approach for modeling _P_ ( `contact` ) and E[ _R|_ `swing` _,_ `outcome` ] 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>5 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

Results 



## **Pitches where Trout made the optimal decision** 





Note: Pitches shown from umpire’s perspective (Trout stands to the left) 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>6 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

Results 



## **Pitches where Trout made the sub-optimal decision** 





Note: Pitches shown from umpire’s perspective (Trout stands to the left) 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>6 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Takeaways 



- Introduced framework for determining the optimal swing decision which utilizes contextual information about the game when the pitch was thrown 

- Bayesian approach facilities uncertainty propagation from constituent models to our determination of the optimal swing decision 

- Intermediate quantities estimated using Bayesian additive regression trees which outperform traditional approaches 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>7 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Takeaways 



- Introduced framework for determining the optimal swing decision which utilizes contextual information about the game when the pitch was thrown 

- Bayesian approach facilities uncertainty propagation from constituent models to our determination of the optimal swing decision 

- Intermediate quantities estimated using Bayesian additive regression trees which outperform traditional approaches 

- Addition results such as summary metrics can be found in the pre-print 

- ✉ Email: ryan.yee@wisc.edu 

- ☞ Website: https://ryanyee3.github.io 

Pre-print 

Rshiny app 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>7 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

# Takeaways 



- Introduced framework for determining the optimal swing decision which utilizes contextual information about the game when the pitch was thrown 

- Bayesian approach facilities uncertainty propagation from constituent models to our determination of the optimal swing decision 

- Intermediate quantities estimated using Bayesian additive regression trees which outperform traditional approaches 

- Addition results such as summary metrics can be found in the pre-print 

- ✉ Email: ryan.yee@wisc.edu 

- ☞ Website: https://ryanyee3.github.io 

Pre-print 

Rshiny app 

- Thank you!! 

<mark>Yee & Deshpande (UW Madison)</mark> 

<mark>7 / 7</mark> 

<mark>NESSIS 2023</mark> 

<mark>Bayesian Plate Discipline</mark> 

– Appendix Strike Model Validation 







– Appendix Contact Model Validation 







– Appendix Expected Runs Model Validation 





– Appendix Additional Figures 






