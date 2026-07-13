<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - Probability and optimization models for racing - Unknown Authors.pdf -->

**1** 



# **Probability and Optimization Models for Racing** 

**Victor S. Y. Lo University of British Columbia Fidelity Investments** 



<!-- Start of picture text -->
University of British Columbia<br>Fidelity Investments<br>Disclaimer: This presentation does not reflect the opinions of<br>Fidelity Investments. The work here was completed at<br>University of British Columbia and the University of Hong Kong.<br><!-- End of picture text -->

**2** 



# **Outline** 



### **Areas to Discuss in Racing:** 



**Favorite-longshot Bias (Economics, Statistics) Ordering Probabilities and Optimal Investment (Probability, Statistics, Finance)** 



<!-- Start of picture text -->
Favorite-longshot Bias<br>(Economics, Statistics)<br>Ordering Probabilities and<br>Optimal Investment (Probability,<br>Statistics, Finance)<br><!-- End of picture text -->

**3** 



<!-- Start of picture text -->
longshots<br>Hall (1988), Ali (1977)<br><!-- End of picture text -->

# **Part 1: Favorite-Longshot Bias** 

**<u>Favorites are underbet and</u> –** **<u>longshots are overbet</u> Busche & Hall (1988), Ali (1977)** 

**A well-known phenomenon in - economic literature Ziemba – (2004); Creating opportunities Bolton & Chapman (1986), Bentor (1994) Economic interpretation: Riskloving behavior** 









**4** 



<!-- Start of picture text -->
Favorite-Longshot Bias<br>Define:<br>P<br>i  = Bet fraction on horse i, i.e. consensus win<br>probability,  i  = 1, …, n<br>= (1- track take)/(1 +  Oi ), where  Oi  = Odds on i<br><!-- End of picture text -->

π _i = objective (true) win probability of i_ 







<!-- Start of picture text -->
'<br>if π i s are low<br>'<br>π s are<br>if i high<br><!-- End of picture text -->



~~π~~ _i_ < _P i if_ π _i_ ' _s are low_ π > _P_ π ' _s are i i if i high_ 

**5** 



<!-- Start of picture text -->
literature –<br>Quandt (1984)<br><!-- End of picture text -->

**Statistical Model Many techniques mentioned in the literature – Ali (1977), Asch and Quandt (1984) Propose to use a simple logit model, Bacon-Shone, Lo, and Busche (1992a):** =1 _Pnj_ ∑ β _P_ _<u>i</u>_ = π _i n_ β _P_ ∑ _j_ = _j_ 1 





**6** 



<!-- Start of picture text -->
β>1 → risk-prefer<br><!-- End of picture text -->

# **Statistical Model (continued)** 

β **>1 →→ β>1 → risk-prefer** _P_ _<u>i</u>_ = π _i n_ β _P_ **β =1 → risk-neutral** ∑ _j_ = _j_ 1 









**β<1 →<1 →→ risk-averse** 





<!-- Start of picture text -->
β<1 →<1 →→<br><!-- End of picture text -->

**7** 



<!-- Start of picture text -->
Universal Comparisons<br>US racetracks consistently have a risk-prefer bias with β > 1β > 1 > 1<br>p-value for<br>Racetrack # races Estimated β H1: β  n.e.  1 Average pool size<br>US (Quandt's 83-84):<br>Atlantic City 712 1.10 0.08 unknown<br>Meadowlands 705 1.12 0.02<br>US (Ali's 70-74):<br><!-- End of picture text -->

**Universal Comparisons** US racetracks consistently have a risk-prefer bias with β > 1β > 1 > 1 

|Racetrack<br># races|Estimated β|p-value for<br>H1:β_n.e._1|Averagepool size|
|---|---|---|---|
|US (Quandt's 83-84):<br>Atlantic City<br>712|1.10|0.08|unknown|
|Meadowlands<br>705|1.12|0.02|$52K|
|US (Ali's 70-74):||||
|Saratoga<br>9,072|1.16|~0|$25K|
|Roosevlt<br>5,806|1.13|~0|$218K|
|Yonkers<br>5,369|1.13|~0|$228K|
|Japan (90)<br>1,607|1.07|0.01|$168K|
|Hong Kong (81-89):||||
|Happy Valley<br>2,212|1.04|0.25|$1.1M|
|Shatin<br>1,943|0.94|0.04|$1.1M|
|China (23-35):||||
|Shanghai<br>730|1.03|0.38|unknown|



**8** 



<!-- Start of picture text -->
Expected utility maximizer<br>It can be shown:<br>= =<br>E U K ∀ i 1<br>( i ) ,...,<br> ∑ P<br><!-- End of picture text -->

**Utility Function Interpretation Expected utility maximizer is indifferent between betting on any horses in a race:** See Ali (1977), Lo (1992) **It can be shown:** 

= = _E U K_ ∀ _i_ 1 _n_ . ( _i_ ) ,..., β  _P_  ∑ _j_  _<u>j</u>_ ≠ _i_ β  β _U_ (1 + _O i_ ) = _K_ 1 + β (1 + _O i_ )  ∝ (1 + _O i_ ) 1 + _t_ ( )     Power utility − Then,Arrow PrattMeasureof Absolute Risk Aversion − _~~U~~_ ('' _x_ ) − − = = _x_ 2 (β /)1 ( ) _U_ (' _x_ ) < ,0 and increases with wealth,if β>1 - ⇒ Bettors take more risk as capital decline" Risk lovers" 

**9** 



<!-- Start of picture text -->
Favorite-longshot<br>racetracks –<br><!-- End of picture text -->

**Conclusion and Research Opportunities Favorite-longshot bias exists in many US racetracks (but not huge)… …but does not exist in some Asian racetracks – would it depend on the Pool Size?** 

**Bias in other investment areas – see Ziemba (2004)** 







**Opportunity to understand bias or accuracy in complicated bets, e.g. Lo and Busche (1994)** 









**Opportunity to apply similar logit models in other applications and other sports, e.g. Lo (1994a), Willoughby (2002)** 



**10** 



<!-- Start of picture text -->
Running time distribution (Ti’s) is key to<br>=<br>π i P ( Tii < MIN { T r })<br>r ≠ i<br>∞<br><!-- End of picture text -->

**Part 2: Ordering Probabilities Running time distribution (Ti’s) is key to determine ordering probabilities:** 

= π _i P_ ( _Tii_ < _MIN_ { _T r_ }) _r_ ≠ _i_ ∞ = − 1 _F t_ | θ _t_ | θ _dt_ 3 [ ( _i r_ )] _f_ ( _i i_ ) _i_ , ( ) ∫ ∏ 0 _r_ ≠ _i_ = _where_ θ _E T or location i_ ( _i_ ) _parameter_ , _and and F are and_ . _f_ (.) (.) _pdf cdf_ , _resp_ ' ' _Given_ π _s solve_ θ _s_ . _Then_ : _i_ , _for i compute_ = π _ij P_ ( _Ti_ < _T j_ < _MIN_ { _T r_ }) _r_ ≠ _i_ , _j_ ∞ = − ∫ _F_ ( _t j_ | θ _i_ )∏ [1 _F_ ( _t j_ | θ _r_ )] _f_ ( _t j_ | θ _j_ ) _dt j_ ( 4 ) 0 _r_ ≠ _i_ , _j_ 



<!-- Start of picture text -->
'<br><!-- End of picture text -->

**11** 



<!-- Start of picture text -->
literature, all assuming independent<br>times:<br>−<br>Exponentiall Harville (1973:)1973:):)<br><!-- End of picture text -->

**Running Time Distribution The following types have been considered in literature, all assuming independent running times:** 1 − = − _Exponentiall Harville_ (1973:)1973:):) _f_ ( _ti_ |θ _i_ ) exp( _ti_ /θ _i_ ) θ _i_ − ~ _Normal Henery_ (1981:) _Ti N_ (θ _i_ )1, − ~ _Gamma Stern_ 1990 _T Gamma r_ θ ( :) _i_ ( , _i_ ), _where r is the shape parameter_ 

**12** 



# **Exponential Running Time** 

**Strictly speaking, we only need g(T) ~ Exponential, where g(.) is a monotonically increasing function** 

= π _P i_ 1 _st and_ 2 _nd_ ( _finishes j finishes_ ) _ij_ π π _i_ _<u>j</u>_ = 5 , ( ) − 1 π _i where_ π _i can be estimated by bet fraction Pi_ = π _P i_ 1 _st_ 2 _nd k_ 3 _rd_ ( _finishes_ , _j finishes_ , _finishes_ ) _ijk_ π π π _i_ _<u>j</u> k_ = (6) − − − π 1 π π 1( _i_ )( _i j_ ) 

**13** 



<!-- Start of picture text -->
equations, for θiθii<br>compute (4)<br><!-- End of picture text -->

## **Normal and Gamma Running Time** 

**The formulas are complex, as one has to solve (3), a system of integral equations, for θiθii ’s, and then compute (4)** 

**Henery(1981) proposed to use a first-order Taylor series approximation under normal running time** 









**Lo and Bacon-Shone (2007) proposed a simple approximation…** 



**14** 



<!-- Start of picture text -->
λ<br><!-- End of picture text -->

# **Simple Approximation** 

#### Lo and Bacon-Shone (2007): 

λ τ π π _<u>j k</u>_ = π π 7 _ijk i_ λ τ ( ) π π _s t_ ∑ ∑ _s_ ≠ _i t_ ≠ _i_ , _j where_ π ' _s can be estimated bet P_ ' _s i by fractions i_ , − λ _andndd_ τ _are parameter values in Lo and Bacon Shone_ (2007).2007).). = = _Note that for Exponentiall time_ , λ τ ,1 (7)7)) _reduces to_ (5)5)) _and_ (6).6).). 



<!-- Start of picture text -->
=<br>π π 7<br>ijk i λ τ ( )<br>π π<br>s t<br>∑ ∑<br>s ≠ i t ≠ i , j<br>where π ' s can be estimated bet P ' s<br>i by fractions i ,<br>−<br>λ andndd τ are parameter values in Lo and Bacon Shone (2007).2007).).<br>= =<br>Note that for Exponentiall time , λ τ ,1<br>(7)7)) reduces to (5)5)) and (6).6).).<br><!-- End of picture text -->

**15** 



## **Running Time Distribution Competiton** 

**So, which distribution should be used?** 

**Lo and Bacon-Shone (1994) found that Harville model has a systematic bias in estimating ordering probabilities based on Hong Kong data and Henery model is clearly superior** 



**Bacon-Shone, Lo, and Busche (1992b) had a similar conclusion using Meadowlands data, however…** 









<!-- Start of picture text -->
and Harville using Japan<br><!-- End of picture text -->



**~~…~~ Lo (1994b) found that Stern model with r=4 is better than both Henery and Harville using Japan data!** 



**16** 



<!-- Start of picture text -->
Constant correlatio i.e.<br>n,<br>reduces to Henery; more<br>-<br>A) Non constant correlatiocorrelation<br><!-- End of picture text -->

# **Correlated Running Times** 

= Constant correlatio i.e. _T_ ∀ _i_ ≠ n, Corr( _i,T j_ ) ρ _j_ , reduces to more dcases : Henery; complicate Non - constant correlatiocorrelation : = ∀ _i_ ≠ A) ρ _ij_ ψ _i_ ψ _j j_ , 1 <u>ψ</u> _<u>i</u>_ − − − = = where δ θ θ θ θ log( ) γ( _i_ ), _i_ , ∑ − 1 _n_ ψ _i i_ i.e. correlations higher for stronger pairs. - = − Non constant variance :σ κ θ θ B) _i_ exp[ ( _i_ )], i.e.,if κ > 0, weaker horses will have higher variance. = = If γ κ ,0it reduces to Henery. 

**17** 



<!-- Start of picture text -->
Empirical Results<br>First order Ta lor series a rox em lo ed for<br>y pp p y<br>complexity<br>p-value of Lik<br>ratio test rel to<br>Model<br>Estimates Henery<br>A) Non-constant<br>= 0.58 0.06<br>correlation (γ only)γ only) only) γ<br>A) Non-constant<br>correlation (γ and δ)γ and δ) and δ)δ)) γ  = 0.60, δ =0.05δ =0.05 =0.05 0.18<br>B) Non-constant Non-constant on-constant<br>variance κ = 0.08 0.06<br><!-- End of picture text -->



<!-- Start of picture text -->
complexity<br>p-value of Lik<br>ratio test rel to<br>Model<br>Estimates Henery<br>A) Non-constant<br>correlation (γ only)γ only) only) γ = 0.58 0.06<br>A) Non-constant<br>correlation (γ and δ)γ and δ) and δ)δ)) γ  = 0.60, δ =0.05δ =0.05 =0.05 0.18<br>B) Non-constant Non-constant on-constant<br>variance κ = 0.08 0.06<br>Non-constant correlation with slope γ only or<br>non-constant variance shows some promise<br><!-- End of picture text -->



<!-- Start of picture text -->
of capital: Wages on allopportunitaW≤=)(maopportunitaW≤=)(ma)(maaW≤=)(ma≤=)(ma tX ,11 t = Wt io (tr E −∑ i oe t a w XX<br>=<br>arg max { E (log Wtt |)<br><!-- End of picture text -->

**18** 

## **Kelly Criterion for Optimal Investment** 

**Instead of mean-variance criterion, we → maximize expected log wealth growth rate** * * _T_ **of capital:** Wages on allopportunitaW≤=)(maopportunitaW≤=)(ma)(maaW≤=)(ma≤=)(ma **_tX_** ,11 **_t_** = _tWt_ **io** (tr _E_ ∑−∑ _i_ oe **t** a **w** **_XXX_** ies in race t, ( _X t_ 1,..., _X tm_ ) = arg max { _E_ (log _Wtt_ |) _X ti_ ≤ _Wt_ −1, _X ti_ ≥ 0∀ _i_ } ∑ _X t_ 1 ,... _X tm i_ where _W_ = total wealth at the end of race t. _t_ 







**Breiman(1960), Thorp(1971), Algoet & Cover(1988) show long-run asymptotic optimality Adopted by Hausch, Ziemba, & Rubinstein(1981) using exponential running times, and Lo, BaconShone, & Busche(1995) and Hausch, Lo, & Ziemba (1994) using other running time distributions, all showed promises** 







**19** 



<!-- Start of picture text -->
probabilities<br><!-- End of picture text -->

**Conclusion and Research Opportunities Knowing the appropriate running time distribution is key to determining ordering probabilities There appears to be no universal best distribution but Henery (Normal) and Stern (Gamma) are competitive Simple approximation is available for Henery and Stern** 







**Correlated running time model is more complex but may be better Other approximation methods may be considered especially for more complicated models (Fractional) Kelly is promising for optimal betting** 









**20** 



<!-- Start of picture text -->
Political Economy, 84, p.803-815., 84, p.803-815.<br>J. of Business 57, p.165-174.<br>Probability,” Research Report Research Report 10, Dept. of Statistics, the University of Hong Kong.<br>Efficiency of Racetrack Betting Markets, Academic Press, p.183-198.<br><!-- End of picture text -->

##### **References for Favorite-Longshot Bias** 

**Ali, M.M. (1977) “Probability and Utility Estimates for Racetrack Bettors,” J. of Political Economy, 84, p.803-815., 84, p.803-815.** 

**Asch, P., Malkiel, B., and Quandt, R. (1984) “Market Efficiency in Racetrack Betting,” J. of Business 57, p.165-174. Bacon-Shone, J., Lo, V.S.Y., and Busche, K. (1992a) “Modelling the Winning Probability,” Research Report Research Report 10, Dept. of Statistics, the University of Hong Kong. Benter, W. (1994) “Computer Based Horse Race Handicapping and Wagering Systems: A Report,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.183-198.** 

**Bolton, R.N. and Chapman, R.G. (1986) “Searching for Positive Returns at the Track, A Multinomial Logit Model for Handicapping Horse Races,” Management Science, 32, p.1040-1059. Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.237-247.** 

**Busche, K. and Hall, C.D. (1988) “An Exception to the Risk Preference Anomaly,” J. of Business, 61, p.337-346.** 



**Lo, V.S.Y. (1992) “Statistical Modelling of Gambling Probabilities,” PhD Thesis, Dept. of Statistics, The University of Hong Kong Lo, V.S.Y. (1994a) “Application of Logit Models in Racetrack Data,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Ac** **~~a~~ demic Press, p.307-314.** 





<!-- Start of picture text -->
Efficiency of Racetrack Betting Markets,<br>Efficiency of Racetrack<br>, 33, No.3, p.215-220.<br>Mathematical Finance Seminar, Stanford University., Stanford University.<br><!-- End of picture text -->



**Lo, V.S.Y. and Busche, K. (1994) “How Accurately do Betters Bet in Doubles?,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.465-468.** 



**Willoughby, K.A. (2002) “Winning Games in Canadian Football: A Logistic Regression Analysis,” The College Mathematics Journal, 33, No.3, p.215-220. Ziemba, W.T. (2004) “Behavioral Finance, Racetrack Betting and Options and Futures Trading,” Mathematical Finance Seminar, Stanford University., Stanford University.** 





**21** 



<!-- Start of picture text -->
Complicated Bets,” Research Report 11Research Report 11, Dept. of Statistics, the University of Hong<br>Kong.<br>Competitions,” J. of American Statistical Association, 68, p.312-316.<br>Racetrack Betting,” Management Science, Management Science, 27, p.1435-1452.<br><!-- End of picture text -->

##### **References for Ordering Probabilities** 

**Bacon-Shone, J.H., Lo, V.S.Y., and Busche, K. (1992b) “Logistic Analyses of Complicated Bets,” Research Report 11Research Report 11, Dept. of Statistics, the University of Hong Kong.** 

**Harville, D.A. (1973) “Assigning Probabilities to the Outcomes of Multi-Entry Competitions,” J. of American Statistical Association, 68, p.312-316.** 

**Hausch, DB., Ziemba, W.T., and Rubinstein, M. (1981) “Efficiency of the Market for Racetrack Betting,” Management Science, Management Science, 27, p.1435-1452.** 

**Henery, R.J. (1981) “Permutation Probabilities as Models for Horse Races,” J. of Royal Statistical Society B, 43, p.86-91.** 

**Henery, R.J. (1985) “On the Average Probability of Losing Bets on Horses with Given Starting Price Odds,” J. of Royal Statistical Society A, 148, p.342-349. Lo, V.S.Y. (1994b) “Application of Running Time Distribution Models in Japan,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.237-247.** 











<!-- Start of picture text -->
The Statistician, ,<br>Handbook of Investments: Efficiency of Sports and<br>J. of American<br>85, p.558-564.<br><!-- End of picture text -->



**Lo, V.S.Y. and Bacon-Shone, J. (1994) “A Comparison between Two Models for Pr** **~~e~~ dicting Ordering Probabilities in Multiple-Entry Competitions,” The Statistician, , 43, No.2, p.317-327.** 

**Lo, V.S.Y. and Bacon-Shone, J. (2007) “Approximating the Ordering Probabilities of Multi-Entry Competitions By a Simple Method,” To appear in: Hausch, D.B. and Ziemba, W.T. ed. (2007) Handbook of Investments: Efficiency of Sports and Lottery Markets, Elsevier.** 



**Stern, H. (1990) “Models for Distributions on Permutations,” J. of American Statistical Association, 85, p.558-564.** 



**22** 



<!-- Start of picture text -->
Asymptotic Equipartition<br>Annals of Probability,<br>W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press,<br>p.183-198.<br>Optimal in a Long-run Sense,” Naval Research Logistics Quarterly, 7,<br>p.647-651.<br><!-- End of picture text -->

##### **References for Optimal Investment Strategy** 

**Algoet, P.H. and Cover T.H. (1988) “Asymptotic Optimality and Asymptotic Equipartition Properties of Log-optimum Investment,” The Annals of Probability, 16, No.2, p.876-898. Benter, W. (1994) “Computer Based Horse Race Handicapping and Wagering Systems: A Report,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.183-198.** 

**Breiman, L. (1960) “Investment Policies for Expanding Businesses Optimal in a Long-run Sense,” Naval Research Logistics Quarterly, 7, p.647-651.** 

**Haigh, J. (2000) “The Kelly Criterion and Bet Comparisons in Spread Betting,” The Statistician, 40, Part 4, p.531-539. Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. (1994) “Pricing Exotic Racetrack Wagers,” in Hausch, D.B., Lo, V.S.Y., and Ziemba, W.T. ed. (1994) Efficiency of Racetrack Betting Markets, Academic Press, p.469483.** 









**Hausch, DB., Ziemba, W.T., and Rubinstein, M. (1981) “Efficiency of the Market for Racetrack Betting,” Management Science, 27, p.1435-1452. Lo, V.S.Y., Bacon-Shone, J., and Busche, K. (1995) “The Application of Ranking Probability Models to Racetrack Betting,” Management Science, 41, p.1048-1059.** 



<!-- Start of picture text -->
of the<br>Management Science, 27, p.1435-1452.27, p.1435-1452.<br>Management Science,<br>Business and<br>Mathematical Finance Seminar, Stanford University., Stanford University.<br><!-- End of picture text -->





**Thorp E.O. (1971) “Portfolio Choice and the Kelly Criterion,” Business and Economics Statistics Section, Proceedings of the American Statistical Association.** 



**Ziemba, W.T. (2004) “Behavioral Finance, Racetrack Betting and Options and Futures Trading,” Mathematical Finance Seminar, Stanford University., Stanford University.** 




