<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2023/2023 - Kelly criterion and fractional Kelly strategy for non-mutually exclusive bets - Jacot et al.pdf -->

J. Quant. Anal. Sports 2023; 19(1): 37–42 

### **Research Article** 

Benjamin P. Jacot* and Paul V. Mochkovitch 

# **Kelly criterion and fractional Kelly strategy for non-mutually exclusive bets** 

https://doi.org/10.1515/jqas-2020-0122 Received November 25, 2020; accepted January 3, 2023; published online January 17, 2023 

**Abstract:** This paper examines how the Kelly criterion, a strategy for maximizing the expected log-growth of capital through informed betting, can be applied to non-mutually exclusive bets. These are bets where there is no one-toone correspondence between the bets and the possible outcomes of the game. This type of situation is common in horse racing, where multiple types of bets are available for a single race. The paper begins by providing a theoretical overview of the Kelly betting strategy and then discusses how it can be extended to non-mutually exclusive bets. A new formulation of the fractional Kelly strategy, which involves betting a fixed fraction of the amount suggested by the Kelly criterion, is also presented for this type of scenario. 

**Keywords:** constrained programming; Kelly criterion; optimization; risk; sports. 

## **1 Introduction** 

favorable odds are present (Maclean, Thorp, and Ziemba 2011), it can also result in highly volatile paths to profitability, with common occurrences of downswings that result in the loss of more than half of the capital (Benter 1994). To mitigate this risk, some researchers have suggested adding constraints, such as limiting maximum drawdown (Busseti, Ryu, and Boyd 2016) or the time horizon of the strategy (Deza, Huang, and Metel 2015), or using a fractional Kelly strategy which involves betting a fixed fraction of the amount suggested by the Kelly criterion (Maclean, Thorp, and Ziemba 2011). 

The Kelly criterion is a useful tool for making informed decisions about how to allocate capital when betting on horse races, particularly when considering a single type of bet (Benter 1994) – most common types of bets are shown in Table 1. While there have been case studies examining the use of the Kelly criterion for the Win bet (Smoczynski and Tomkins 2010) and, less frequently, for exotic bets like Superfecta (Deza, Huang, and Metel 2015), there has not yet been a comprehensive approach to applying the Kelly criterion to situations where multiple types of bets are available for a single race. This is the gap in research that the current paper aims to address. 

### **1.1 How much should a gambler bet?** 

When a gambler has identified favorable odds, they must decide how much to bet. The correct amount will depend on the gambler’s objectives. For example, a gambler may want to maximize the expected value of their capital by betting all of it, but this strategy is risky in the long run and could lead to the gambler’s ruin if they continue to play indefinitely. 

The Kelly criterion (Kelly 1956), on the other hand, aims to maximize the expected log-growth of capital by betting a fixed fraction of available capital, thereby avoiding ruin<sup>1</sup> While the Kelly criterion has some desirable properties,<sup>2</sup> such as almost surely diverging to infinity when 

For more details, an exhaustive listing of pros and cons of the Kelly criterion is given in (Maclean, Ziemba, and Blazenko 1992, Table 1). 

***Corresponding author: Benjamin P. Jacot** , Independent Researcher, Paris, France, E-mail: bjacot@alum.mit.edu. https://orcid.org/0000-0001-7054-647X **Paul V. Mochkovitch** , Independent Researcher, Paris, France 

### **1.2 Introducing the Kelly criterion: a simple case** 

Assume a coin-tossing game where probabilities for Heads and Tails are _p_ and _q_ respectively. Naturally, _p_ + _q_ = 1. Before each new toss, the player is offered to bet on Heads. The return is _r_<sup>+</sup> _>_ 0 when the player wins. Reversely, it is _r_<sup>−</sup> = −100%. The coin is biased to the player’s advantage, such that _p > q_ . 

As the tosses are independent and _p_ , _q_ and _r_<sup>+</sup> are constant, the bet amount is a constant ratio _a_ of the player’s capital (Thorp 2006). For an initial capital _C_ 0, the capital _CN_ after _N_ trials becomes: 



where _W_ and _L_ are the respective number of experienced wins and losses, and _W_ + _L_ = _N_ . The log-growth of capital 

> **38 —** B. P. Jacot and P. V. Mochkovitch: Kelly strategies for non-mutually exclusive bets 

**Table 1:** Examples of bets for horse race wagering. 

|**Type**|**Explanation**|
|---|---|
|Win|Pick the winning horse.|
|Place|Pick the horse finishing first or second.|
|Show|Pick the horse finishing first, second or third.|
|Exacta|Pick top two finishers in correct order.|
|Quinella|Pick top two finishers in either order.|
|Trifecta|Pick top three finishers in correct order.|
|Superfecta|Pick top four finishers in correct order.|



over _N_ trials _GN_ is given by: 









Here, log functions contain the discount factor of capital for each outcome. In addition, they are each weighted by the probability of the given outcome. In what follows, _G_ ∞ will be expressed in more complex ways but this interpretation will hold true. 

The Kelly criterion consists in maximizing (3) under constraint: 



as neither short betting, nor leverage are usually allowed or feasible in most betting platforms. Equation (3) being concave, the maximum is found when its first derivative is zero-valued. Providing (4) is met, the corresponding ratio is: 



The fractional Kelly strategy then consists in betting only a fraction _a f_ of _a_<sup>∗</sup> each time. It is good practice to have _a f_ ≤ _a_<sup>∗</sup> ∕2 (Benter 1994). It enables to counterbalance the estimation errors for _p_ and _q_ , as they are usually unknown. It also directly reduces the drawdowns of the strategy, as less capital is bet at each new trial. Finally, the fractional Kelly strategy deteriorates _G_ ∞ by a lower factor than _a f_ ∕ _a_<sup>∗</sup> , because of its concavity. This goes to the bettor’s interest. 



then according to (3), _k_ ≈ 0.75 for _a f_ ∕ _a_<sup>∗</sup> = 0.5 and _k_ ≈ 0.55 for _a f_ ∕ _a_<sup>∗</sup> = 0.33. Therefore, 75% (respectively 55%) of the maximal expected log-growth is preserved when dividing the optimal allocation by 2 (respectively 3). 

### **1.3 Extension of the Kelly criterion to mutually exclusive bets** 

Bets are considered to be mutually exclusive if there is a one-to-one correspondence between bets and all possible outcomes, as illustrated in Figure 1. In a race with _n_ horses, a Win bet defines _n_ mutually exclusive outcomes, each corresponding to betting on a single horse to win. It is assumed that only one horse can win and there is no possibility of a tie. The probability for outcome _i_ , e.g. horse _i_ wins the race, is denoted as _pi_ and thus<sup>∑</sup> _pi_ = 1. 

The Kelly criterion directly extends to such bets. Let _ri_<sup>+</sup> and _ri_<sup>−= −100% be the returns for bet</sup><sup>_i_in case of success</sup> or loss, respectively. Then (3) becomes: 



where **_a_** = ( _ai_ )1≤ _i_ ≤ _n_ is the vector of bet amounts expressed as constant ratios of the player’s capital and _b_ is the constant ratio of capital that is not bet: 



Again, the log functions in (7) contain the discount factor of capital for each outcome, weighted by the probability of the latter. For a given outcome, only one bet brings a positive return whereas all others are lost. The final capital is thus the sum of the capital that was not bet and the gains from the winning bet. 

Taking the example of small favorable odds such as _p_ = 51%, and for _r_<sup>+</sup> = +100%, then (5) brings _a_<sup>∗</sup> = 2%.<sup>3</sup> Defining: 

**3** This is a is a well-known result (Kelly 1956; Kempton 2011; Thorp 2006). 

**Figure 1:** Mutually exclusive bets: each bet delivers a positive return for strictly one of all possible outcomes. There are as many bets as possible outcomes. 

> B. P. Jacot and P. V. Mochkovitch: Kelly strategies for non-mutually exclusive bets **— 39** 

Maximizing (7) can be performed with Lagrangian optimization. More precisely, closed-form solutions for **_a_**<sup>∗</sup> can be derived from solving Karush–Kuhn–Tucker conditions – see (Kempton 2011) for detailed resolution. 

However, the fractional Kelly strategy becomes more complex. For a given _k_ as defined in (6), what is the fraction _a f ,i_ of each optimal allocation ratio _a_<sup>∗</sup> _i_<sup>?Putdifferently,</sup><sup>**_a_**</sup><sup>_f_</sup> needs to solve: 







It is indeed desirable to bet as little capital as possible while keeping the expected log-growth above threshold _k_ . Naturally, **_a_** _f_ must also verify **1**<sup>⊺</sup> **_a_** _f_ ≤ 1. The resolution of (9) is described in the next section, for the broader case of nonmutually exclusive bets. 

## **2 Generalization to non-mutually exclusive bets** 

### **2.1 Theoretical framework** 

Let _n_ and _m_ denote the number of different outcomes and bets respectively. Similarly Figures 1 and 2 illustrates the non-mutually exclusive bets situation. In a horse race, the _n_ different outcomes correspond to the order in which the horses finish first, second, and third. All bets except the Superfecta bet from Table 1 are offered, totaling _m_ bets. This means that _m > n_ and the bets are non-mutually exclusive, as more than one bet may have positive returns for each outcome. 

The vector of bet returns for outcome _i_ needs to be introduced to generalize the Kelly criterion to non-mutually exclusive bets: 



Here, several returns within **_r_** _i_ may be positive and the others are equal to −100%. For _Ii_ the set of bet indices with positive returns under outcome _i_ , (7) becomes: 



which simplifies, using (8) and (10), as: 



This equation is a more general expression of (7). Thanks to (10), _G_ ∞ is now expressed in a much simpler way 

**Figure 2:** Non-mutually exclusive bets: each bet delivers a positive return for one or several of all possible outcomes. The number of outcomes _n_ and bets _m_ is different. 

as compared to (11). It is thus a pivotal step in the resolution of Kelly criterion for non-mutually exclusive bets. The advantage is indeed that the computation of the gradient and Hessian becomes straightforward: 





and the Kelly criterion can be expressed as the following optimization problem: 









Deriving closed-form solutions analytically for such optimization problem is tedious, as opposed to the case of mutually exclusive bets in (Kempton 2011). Karush– Kuhn–Tucker conditions are valid since the objective function is concave and all inequality constraints are linear and regular enough. Solving the system of equations resulting from (12) to (13) is complex due to the expressions of _G_ ∞ and ∇ **_a_** _G_ ∞. Therefore, a gradient-descent numerical approach is preferred in the examples of the following section. This approach is particularly efficient because it uses the gradient, which is the direction of steepest ascent, to iteratively update the solution and find the optimal solution more quickly. In the context of (12) and (13), knowing the gradient allows the approach to efficiently update the solution because the gradient points in the direction that will result in the greatest increase in the 

> **40 —** B. P. Jacot and P. V. Mochkovitch: Kelly strategies for non-mutually exclusive bets 

objective function. Similarly, in the context of (9), knowing the gradient of the non-linear constraint in (9b) allows the approach to efficiently update the solution because it can use the gradient to determine the direction that will result in the greatest increase in the constraint. Overall, having access to the gradient information allows the gradient-descent numerical approach to more quickly find the optimal solution. 

### **2.2 Examples** 

#### **2.2.1 Two bets, two outcomes** 

Taking the same coin-tossing game as in the single bet example, two bets are now proposed. All else equal, the infinite log-wealth becomes: 



under constraints: 





and its gradient is: 



Yet, ∇ _G_ ∞ = **0** is not always verified where (16) is maximal. If it were, then per (18): 



Because of (17a) and (17b), the determinant of such system is necessarily zero-valued, leading to _r_ 1<sup>+</sup><sup>_r_</sup> 2<sup>−=</sup><sup>_r_</sup> 2<sup>+</sup><sup>_r_</sup> 1<sup>−.</sup> Therefore: 

- A maximum with zero-valued gradient in both directions exists if returns are proportional between both bets. The determinant of (19) being zero-valued, maximum is not unique and verifies: 



- 

Cases (b) and (c) in Figure 3 and Table 2 illustrate each of these two cases, respectively. In addition, case (a) shows that no bets are placed when no favorable odds exist, i.e. _p_ = 50% and positive returns are equal to negative ones in absolute terms. 

#### **2.2.2 Two bets, three outcomes** 

This example is summarized in Table 3. Here, the two bets are non-mutually exclusive, as both bring a positive return if outcome 1 occurs. However they are opposed under 















<!-- Start of picture text -->
(a) (b) (c)<br><!-- End of picture text -->

**Figure 3:** Three examples of _G_ ∞ for two bets and two outcomes, as detailed in Table 2. 

> B. P. Jacot and P. V. Mochkovitch: Kelly strategies for non-mutually exclusive bets **— 41** 

**Table 2:** Parameters used in cases (a), (b) and (c) in Figure 3. 

|**Case**|**_p_**|~~(~~**_r_+**<br>**1** <sup>**_, r_−**</sup><br>**1**<br>~~)~~|~~(~~**_r_+**<br>**2** <sup>**_, r_−**</sup><br>**2**<br>~~)~~|**_a_**<sup>**∗**</sup>|**_af_(****_k_ = 0.75)**|**_G_∞(****_a_**<sup>**∗**</sup>**)**|
|---|---|---|---|---|---|---|
|(a)|50%|(100%,−100%)|(100%,−100%)|(0%, 0%)|(0%, 0%)|0|
|(b)|60%|(100%,−100%)|(100%,−100%)|_a_<sup>∗</sup><br>1 <sup>+</sup><sup>_a_∗</sup><br>2 <sup>= 20%</sup>|_af_,+_af_,=10.1%|0.0201|
|(c)|50%|(100%,−80%)|(120%,−100%)|<br> <br>(12.5%, 0%)|(6.2%, 0%)|0.0062|



**Table 3:** Input and output summary. 

|**Outcome**|**_pi_**||**_ri_**|**_a_**<sup>**∗**</sup>|**_af_(k = 0.75)**|**_G_∞(****_a_**<sup>**∗**</sup>**)**|
|---|---|---|---|---|---|---|
|_i_=1|60%|(200%,|100%)||||
|_i_=2|20%|(−100%,−|100%)|(20%, 40%)|(16.3%, 14.5%)|0.2059|
|_i_=3|20%|(−100%,|100%)||||



Oliphant 2020). The gradient of non-linear constraint (9b) given by (13) is specified for faster convergence of the algorithm. The computed **_a_** _f_ is also shown in Figure 4. It should be noted that the most allocated bet in **_a_**<sup>∗</sup> and **_a_** _f_ is different, stressing the interest for risk versus reward considerations. 

outcome 3. Finally, they both correspond to a loss under outcome 2. Overall, the first bet brings a higher return than the second one, but not as frequently. Both bets seem therefore of interest. 

Here, **_a_**<sup>∗</sup> is found by solving (15) using the trust region algorithm developed in (Conn, Gould, and Toint 2000) and implemented in (Virtanen, Gommers, and Oliphant 2020). This gradient-descent approach is of interest as it handles efficiently boundary constraints (15c) and (15d) and takes (14) into account for more efficient descent. The computed **_a_**<sup>∗</sup> is shown in Figure 4. As expected, the Kelly criterion keeps both bets in its allocation. 

Then, (9) is solved for _k_ = 0.75 using the trustregion constrained method from (Virtanen, Gommers, and 









**Figure 4:** _G_ ∞ for two bets and three outcomes. 

## **3 Conclusions** 

The existing research on wagering for horse racing typically focuses on individual bet types, such as selecting the winning horse (Smoczynski and Tomkins 2010) or placing a Superfecta bet (Deza, Huang, and Metel 2015). 

However, in order to maximize profits, it is necessary to consider the full range of available bet types. Some allocation models, such as the Kelly criterion, have difficulty accounting for multiple bet types because they involve allocating capital between non-mutually exclusive bets. The research presented in this paper addresses this issue and opens up possibilities for further study, such as using Lasso penalization to constrain the optimal allocation to have as many null values as possible for ease of implementation. 

It is worth noting that this allocation strategy has limitations, including the need for reliable estimates of the probability of each outcome and the returns for each bet type, which can be challenging to obtain in the context of horse racing (Benter 1994; Silvermann 2013). In that respect, recent developments have shown how to modify the Kelly criterion in order to take the uncertainty in _pi_ into account (Baker and McHale 2013; Chu, Wu, and Swartz 2018). Other challenges include the variable odds that depend on the bets made by other bettors and the potential for noise from bettors following the same strategy when placing bets at the last minute. 

**Author contributions:** All the authors have accepted responsibility for the entire content of this submitted manuscript and approved submission. 

**Research funding:** None declared. 

**Conflict of interest statement:** The authors declare no conflicts of interest regarding this article. 

> **42 —** B. P. Jacot and P. V. Mochkovitch: Kelly strategies for non-mutually exclusive bets 

## **References** 

- Baker, R. D., and I. G. McHale. 2013. “Optimal Betting under Parameter Uncertainty: Improving the Kelly Criterion.” _Decision Analysis_ 10 (3): 189−99,. 

- Benter, W. 1994. “Computer Based Horse Race Handicapping and Wagering Systems: A Report.” In _Efficiency of Racetrack Betting Markets_ , 183−98. Singapore: World Scientific **.** 

- Browne, S. 1999. “Reaching Goals by a Deadline: Continuous-Time Active Portfolio Management.” _Advances in Applied Probability_ 31: 551−7. 

- Busseti, E., E. K. Ryu, and S. Boyd. 2016. “Risk-constrained Kelly Gambling.” _Journal of Investing_ 25: 118−34 **.** 

- Chu, D., Y. Wu, and T. Swartz. 2018. “Modified Kelly Criteria.” _Journal of Quantitative Analysis in Sports_ 14: 1−11 **.** 

- Conn, A. R., N. I. M. Gould, and P. L. Toint. 2000. “Trust Region Methods.” In _MOS-SIAM Series on Optimization_ . Philadelphia: Society for Industrial and Applied Mathematics **.** 

- Deza, A., K. Huang, and M. Metel. 2015. “Chance Constrained Optimization for Parimutuel Horse Race Betting.” arXiv. 

- Deza, A., K. Huang, and M. Metel. 2017. “Managing Losses in Exotic Horse Race Wagering.” _Journal of the Operational Research Society_ 69: 319−25,. 

- Kelly, J. L. 1956. “A New Interpretation of Information Rate.” _The Bell System Technical Journal_ 35: 917−26,. 

- Kempton, C. 2011. “Horse Play: Optimal Wagers and the Kelly Criterion. Under Sup. of John Morrow.” PhD thesis, University of Washington. 

- Maclean, L. C., E. O. Thorp, and W. T. Ziemba. 2011. “The Kelly Capital Growth Investment Criterion.” _World Scientific_ 3, https://doi.org/10 .1142/7598. 

- Maclean, L. C., W. T. Ziemba, and G. Blazenko. 1992. “Growth versus Security in Dynamic Investment Analysis.” _Management Science_ 38: 1562−85,. 

- Silvermann, N. 2013. “Optimal Decision with Multiple Agents of Varying Performance”. PhD thesis, UCLA. 

- Smoczynski, P. B., and D. Tomkins. 2010. “An Explicit Solution to the Problem of Optimizing the Allocation of a Bettor’s Wealth when Wagering on Horse Races.” _The Mathematical Scientist_ 35: 10−7. 

- Thorp, E. O. 2006. “The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market.” In _Handbook of Asset and Liability Management_ , 1, 385−428. Amsterdam: North Holland. 

- Virtanen, P., R. Gommers, and T. E. Oliphant. 2020. “SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python.” _Nature Methods_ 17: 261−72 **.** 


