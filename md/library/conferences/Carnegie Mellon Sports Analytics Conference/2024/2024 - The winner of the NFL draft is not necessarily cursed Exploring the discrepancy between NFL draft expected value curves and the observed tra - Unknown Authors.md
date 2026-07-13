<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2024/2024 - The winner of the NFL draft is not necessarily cursed Exploring the discrepancy between NFL draft expected value curves and the observed tra - Unknown Authors.pdf -->

# **Exploring the discrepancy between NFL draft expected value curves and the observed trade market** 

Ryan S. Brill<sup>1</sup> and Abraham J. Wyner<sup>2</sup> 

### **Abstract** 

Football analysts traditionally value a future draft pick position by its expected performance or surplus value. But, these expected value curves do not match the valuation implied by the observed trade market. One takeaway is general managers are making terrible trades on average. An alternative explanation is they are using some other value function that captures an essential piece of the puzzle missing from previous analyses. We are partial to the latter explanation. In particular, traditional analyses don’t consider how variance in performance outcomes changes over the draft. Because variance decays convexly accross the draft, eliteness (e.g., right tail probability) decays much more steeply than expected value. We suspect general managers value performance nonlinearly, placing exponentially higher value on players as their eliteness increases. This is because elite players have an outsize influence on winning the Super Bowl. Thus, in this paper we consider nonlinear draft value curves that capture the outsize influence of elite players. Such nonlinear value functions produce steeper draft value curves that more closely resemble the observed trade market. 

**Reproducibility statement:** the code and data in this analysis is reproducible and publicly available on Github at `https://github.com/snoopryan123/NFL_draft_chart_Ryan` . 

# **1 Introduction** 

NFL teams often find themselves wanting to trade draft picks. A general manager may want to trade up to draft a particular player before he is taken by another team. He may also want to trade up to be able to draft players of a certain caliber at a particular position. In exchange for trading up, a general manager often offers a trade of current and/or future draft picks. This naturally leads to the following questions. If a team wants to trade for a particular draft pick, which picks should it offer in exchange? And if a team is offered a bundle of draft picks in exchange for another bundle of draft picks, should it accept or reject the trade? We are interested in the relative value of draft picks. 

## **1.1 Traditional NFL draft trade value charts** 

Prior to the draft, we do not know how well a player drafted at pick _x ∈{_ 1 _, ...,_ 256 _}_ will perform in the NFL. Thus, we think of the performance outcome _Y_ associated with pick _x_ as a random variable, denoted by a capital letter. Throughout this paper, we let the realization of _Y_ be a player’s observed second contract value relative to the salary cap (APY cap percentage). This is a reflection of a player’s first contract performance value since he signs his second contract in free agency just after his first contract ends. Though free agent APY cap percentage is an 

> 1Graduate Group in Applied Mathematics and Computational Science, University of Pennsylvania. Correspondence to: ryguy123@sas.upenn.edu 

> 2Dept. of Statistics and Data Science, The Wharton School, University of Pennsylvania 

1 

imperfect measure of a player’s performance and first contract value is an incomplete measure of the total value he provides to his team (as it excludes the rest of his career), the focus of this paper is to value draft picks assuming a performance measure, not to choose the best performance measure. We leave further analysis of various measures of performance to future work. 

From the dataset _{_ ( _xi, Yi_ ) _}_ of all recent draft picks in NFL history, we want to learn the denoised relationship between pick number _x_ and performance outcome _Y_ . Traditional analyses use a standard approach but with differing measures of first contract performance (Massey and Thaler, 2013; Stuart, 2012; Fitzgerald and Spielberger, 2024; Pro Football Focus, 2024; Baldwin, 2024). The de-noised relationship they estimate from data is the expected value of _Y_ given _x_ . 

This traditional approach proceeds as follows. First, fit the expected performance curve. This is the conditional mean function _x �→_ E[ _Y |x_ ]. Second, calculate the compensation curve. This is the cost function _x �→_ cost( _x_ ). Cost is first contract compensation, which is essentially a deterministic function of _x_ . Third, calculate the expected surplus curve. This is the difference between the expected performance curve and the compensation curve, _x �→_ E[ _Y −_ cost( _x_ ) _|x_ ]. Finally, normalize each of these curves so that the value of the first pick is 1. They normalize by dividing by the value of the first pick. 

We fit these traditional draft value curves using our outcome variable _Y_ (second contract APY cap percentage), which we visualize in Figure 1. We use spline regression to fit the expected performance curve from a publicly available dataset of all draft picks from 2013 to 2023 (Ho and Carl, 2024). We calculate the compensation curve as in Baldwin (2024): beginning with the actual 2023 salary cap (about $225 million) and assuming a cap growth rate of 7% over the next three seasons (2024, 2025, and 2026), we convert the total dollar amount of the rookie contract into a percentage of the cap. Then, for each draft pick we average the compensation values across the four seasons. We calculate the expected surplus curve as the difference between the expected performance curve and compensation curve. 

Expected performance value (blue) is less steep than compensation (red), indicating that players are underpaid on average in their first contracts. This yields positive expected surplus value (green) across most of the draft. Expected surplus value (green) is larger than 1 throughout the first round, peaking in the middle of the first round. This indicates that later first round picks provide more value on average than top picks relative to their cost. This phenomenon is the “loser’s curse” documented in Massey and Thaler (2013): the worst teams who pick at the beginning of the first round get less surplus value on average than better teams who pick later in the first round. 

In Figure 1 we also visualize Jimmy Johnson’s draft curve (pink) and the Weibull trade market curve (orange). At the request of Dallas Cowboys coach Jimmy Johnson, vice president Mike McCoy created the first draft value chart based on gut instinct and past trades. This is known today as the Jimmy Johnson chart. Devised in Massey and Thaler (2013), the Weibull curve attempts to fit the dataset of all observed trades as best as possible. If all teams used one additive trade value chart for each trade, it would look like the Weibull curve. 

The Weibull and Jimmy Johnson curves are quite similar. They are much steeper than the expected performance and surplus curves and aren’t even the same shape as the expected surplus 

2 



Figure 1: In blue is expected performance value _x �→_ E[ _Y |x_ ] _/_ E[ _Y |x_ = 1], where _Y_ is second contract APY cap percentage and _x_ is draft pick. In red is first contract compensation _x �→_ cost( _x_ ) _/_ cost( _x_ = 1). In green is expected surplus value _x �→_ E[ _Y −_ cost( _x_ ) _|x_ ] _/_ E[ _Y −_ cost( _x_ = 1) _|x_ = 1]. In pink is Jimmy Johnson’s value curve. In orange is the Weibull value curve implied by the trade market. 

curve. Thus, it seems NFL general managers do not trade based on expected performance value or expected surplus value. It also implies that teams should trade down in the draft more often. According to surplus value, even teams at the very top of the draft should trade down, particularly towards the middle of the first round. This result is counterintuitive because very top picks are so highly regarded by general managers and football fans. 

## **1.2 Expected value charts don’t tell the full story** 

The discrepancy between the trade market and expected performance/surplus value curves hasn’t changed since the publication of Massey and Thaler (2013). One explanation is that general managers haven’t learned from these analyses. They have continued to make terrible trades on average, not trading down often enough and overpaying when they trade up. An alternative explanation is that expected value curves don’t tell the full story. General managers are using some other value function that captures an essential piece of the puzzle missing from previous analyses. We are partial to the latter explanation. 

Previous analyses don’t consider how the variance of performance outcomes changes as the draft progresses. In Figure 2 we visualize the conditional mean _x �→_ E[ _Y |x_ ] and standard deviation _x �→_ sd( _Y |x_ ) of performance _Y_ as a function of draft pick _x_ . These graphs look remarkably similar. The key insight is that the conditional mean _and variance_ of performance _Y_ decreases as draft pick _x_ increases. Moreover, they decrease convexly. Since an earlier pick has a much higher expected value and variance than a later pick, it has a much fatter right tail. In other words, an earlier pick has a significantly higher probability of becoming an elite player, moreso than we would expect if we just considered expected value. 

Elite players have an outsize influence on winning the Super Bowl. Tom Brady or Patrick Mahomes won seven of the ten Super Bowls from 2014-2023 because they’re just that good. 

3 



Figure 2: The black dots indicate the empirical mean (left) and s.d. (right) of _Y_ (performance, i.e. second contract APY cap percentage) given _x_ (draft pick). The blue lines are smoothed curves _x �→_ E[ _Y |x_ ] (left) and _x �→_ sd( _Y |x_ ) (right). 

Mathematically, winning the Super Bowl is like exceeding a high threshold of team performance. Far right tail players exponentially increase the odds of exceeding such a high threshold. The difference in Super Bowl win probability between adding an elite player and an average player to your team is massive. In particular, it is much larger than suggested by the difference in performance outcome _Y_ . 

Thus, if a general manager’s goal is to win a Super Bowl, then accepting a trade because it yields higher performance or surplus value _on average_ is not necessarily optimal. We suspect general managers value performance nonlinearly, place exponentially higher value on players as their eliteness increases. Ideally we would quantify the probability of winning the Super Bowl if a team drafts a player of performance value _Y_ . We would need to adjust for confounders such as the team’s current roster and the position of the drafted player. This is extremely difficult to estimate from data for many reasons. The Super Bowl win/loss outcome is sparse and the confounders are complex. 

Instead, in this paper we consider simpler alternative value functions beyond expected performance or surplus value. We focus on nonlinear transformations of _Y_ that capture the outsize influence of elite players. The most intuitive example is right tail probability, which places high value on elite performance and no value on lesser performance. We find that such nonlinear value functions produce steeper draft value curves that more closely resemble the observed trade market. 

# **2 Exploring nonlinear transformations of performance** 

## **2.1 Right tail probability** 

Intuitively, one reason a general manager trades up is that he wants to add an elite player to his roster. Often, he is interested in an elite quarterback. This suggests we consider a draft trade value curve proportional to right tail probability, _x �→_ P( _Y > r|x_ ). Assuming additivity, this is equivalent to valuing a bundle of draft picks _{xj}_<sup>_n_</sup> _j_ =1<sup>bytheexpectednumberofelite</sup> 

4 

players it is expected to produce, 



We calculate right tail probability from the conditional density P( _Y |x_ ), which we estimate using a Bayesian “spike plus Beta regression” model.<sup>3</sup> As both the mean and variance of _Y_ decay convexly over the draft (recall Figure 2), the right tail decays convexly as well. The densities of top picks feature fat right tails, which shift lefward and morph into a spike near 0 as the draft progresses. 

In Figure 3 we visualize right tail probability P( _Y > r|x_ ) and its associated value curve _v_ elite( _x_ ) = P( _Y > r|x_ ) _/_ P( _Y > r|x_ = 1). We overlay the expected performance value curve _v_ EV( _x_ ) = E[ _Y |x_ ] _/_ E[ _Y |x_ = 1] and the Weibull trade market curve. The right tail curves are much steeper than the expected value curve. To draft for eliteness, not expected value, earlier picks are much more valuable. The higher the cutoff defining elite, the steeper the curve. 

The observed trade market curve is as steep as some of the right tail curves. The way general managers trade resembles valuing picks by the number of elite players they are expected to produce. Though we can’t peer into the minds of general managers, if they were trading for eliteness we would have seen a similar trade market. In particular, the right tail curve with _r ≈_ 0 _._ 15 closely matches the Weibull curve. When trades occur, the price of a pick appears proportional to the probability it results in an extremely elite player (whose second contract APY cap percentage exceeds _≈_ 15%). This is a high bar: in our dataset of draft picks from 2013 to 2023, just 16 players ( _≈_ 0 _._ 57%) satisfy _Y ≥_ 0 _._ 15. 



Figure 3: On the left: right tail probability P( _Y > r|x_ ) ( _y_ -axis) as a function of draft pick _x_ and right tail cutoff _r_ (color). On the right: right tail probability relative to the first pick _v_ elite( _x_ ) = P( _Y > r|x_ ) _/_ P( _Y > r|x_ = 1). The black dotted line is the relative expected performance value curve _v_ EV( _x_ ) = E[ _Y |x_ ] _/_ E[ _Y |x_ = 1] and the black dashed line is the Weibull trade market curve. 

> 3Due to space constraints, we exclude the full details of our Beta regression model, instead summarizing it here. We model the right tail using Beta regression, which works because _Y ∈_ [0 _,_ 1] and it seems reasonable when we eyeball the empirical densities. Using the mean-precision parameterization of the Beta distribution (Ferrari and Cribari-Neto, 2004), we model _Y |x, Y >_ 0 _._ 005 _∼_ Beta( _µ_ ( _x_ ) _, ϕ_ ( _x_ )) where _µ_ ( _x_ ) = logistic(spline( _x|β_ )) and _ϕ_ ( _x_ ) = exp( _γ_ 0 + _γ_ 1 _· x_ ). We model the spike near zero, the _bust spike_ , using logistic regression, P( _Y ≤_ 0 _._ 005 _|x_ ) = logistic( _α_ 0 + _α_ 1 _· x_ ). We estimate the posterior distribution of each parameter in Stan. 

5 

## **2.2 S curves** 

An oddity of valuing a draft pick by right tail probability P( _Y > r|x_ ) is that it so sharply characterizes success and failure. Formally, it is the expected value of a step function, P( _Y > r|x_ ) = E[ _g_ step( _Y_ ) _|x_ ] where _g_ step( _y_ ) = I ( _y > r_ ). We visualize such a step function in Figure 4a. A general manager who values performance outcome _Y_ by _g_ step( _Y_ ) views a player as a total success if _Y > r_ and a total failure if _Y < r_ . 









Figure 4: Performance outcome value functions _g_ step( _y_ ) = I ( _y > r_ ) (a), two _g_ s curves (b,c), and _g_ line( _y_ ) = _y_ (d). 

A general manager could use some other function _g_ to measure how he values outcomes. An outcome valuation function _y �→ g_ ( _y_ ) then implies a draft pick valuation function _x �→ v_ ( _x_ ) by _v_ ( _x_ ) _∝_ E[ _g_ ( _Y_ ) _|x_ ]. For example, _g_ step implies _v_ elite and _g_ line( _y_ ) = _y_ implies _v_ EV. Given any _g_ , we can calculate the corresponding _v_ using the conditional density P( _Y |x_ ). In particular, 1 E[ _g_ ( _Y_ ) _|x_ ] = �0<sup>_g_(</sup><sup>_y_)P(</sup><sup>_y|x_)</sup><sup>_dy._</sup> 

The step function _g_ step is extreme. It is sharp, ascribing _Y_ = _r_ a total failure and _Y_ = _r_ + _ε_ a total success. Also, it values all outcomes above _r_ equally. On the other end of the spectrum is the expected performance value curve. It corresponds to the identity function _g_ line( _y_ ) = _y_ (see Figure 4d). A general manager who uses _g_ line values outcomes linearly. For instance, he values the difference between 0 _._ 02 and 0 _._ 01 the same as the difference between 0 _._ 09 and 0 _._ 08. _g_ line is also extreme since it discounts the outsized influence of elite players on winning. If you believe great players are exponentially more valuable than typical players, it is critical to use a nonlinear _g_ . 

We propose a nonlinear outcome valuation function _g_ between the two extremes of _g_ step and _g_ line. To capture nonlinearity in performance outcomes but in a less sharp way, we use an _s_ curve. We use the CDF of the beta distribution, a sufficiently rich family of _s_ curves, denoted by _g_ s and parameterized by _α_ and _β_ , 



We visualize two of these _s_ curves in Figures 4b and 4c. For example, _g_ s in Figure 4b assigns near failure to busts and near total success to elite players. The two dashed gray lines indicate where _g_ s<sup>_′_(</sup><sup>_y_)=1.When</sup><sup>_y_isbetweenthetwograylines,</sup><sup>_g_</sup> s<sup>_′_(</sup><sup>_y_)</sup><sup>_>_1.Thisreflects,forexample,</sup> that the difference in outcome value between a good and median player is much larger for _g_ s 

6 

than for _g_ line (as _g_ line<sup>_′_</sup> ( _y_ ) _≡_ 1). Similarly, the difference in outcome value between a median and a bad player is much larger for _g_ s than for _g_ line. 

A _g_ s curve implies a draft value curve _v_ s( _x_ ) _∝_ E[ _g_ s( _Y_ ) _|x_ ], which we visualize in Figure 5 alongside other curves. The least steep curve is the expected performance value curve (beige). It ignores that variance declines steeply over the draft. The steepest curves are the Jimmy Johnson curve (gray), Weibull curve (teal), and right tail probability curve with high cutoff _r_ = 0 _._ 15 (pink). Those curves place extreme value on elite players. The _s_ curves (chartreuse and yellow) lie between the expected performance value curve and the extremely steep curves. They place exponentially increasing value on increasingly good players while still placing nonzero value on less-than-elite production. 



Figure 5: Various trade market value functions _v_ ( _x_ ). 

## **2.3 Surplus value** 

Massey and Thaler (2013), an economics paper at heart, are interested in surplus value, the difference between performance value and cost. This accounts for the varying cost of each draft pick. We visualize the cost/compensation curve by the orange line in Figure 5. It matches the steepness of the other steep curves through the first round but then asymptotes above zero due to the minimum salary. In this section, we account for compensation and consider surplus value. 

Denote the first contract compensation of draft pick _x_ by cost( _x_ ). As before, denote the performance outcome associated with a draft pick by _Y_ , a random variable. The surplus value of a pick is _S_ = _Y −_ cost( _x_ ). Massey and Thaler (2013) model expected surplus value, E[ _S|x_ ] = E[ _Y −_ cost( _x_ ) _|x_ ] = E[ _g_ line( _Y −_ cost( _x_ )) _|x_ ], where _g_ line( _y_ ) = _y_ . We discussed in the previous section the problem with valuing performance outcomes _Y_ linearly. This logic extends to surplus value. We’d like to consider nonlinear valuations of surplus _S_ , _v_ ( _x_ ) _∝_ E[ _g_ ( _S_ ) _|x_ ] = E[ _g_ ( _Y −_ cost( _x_ )) _|x_ ]. 

In Figure 6 we visualize various surplus and performance value curves. For each _g_ , the corresponding performance curve is steeper than the corresponding surplus curve. This is because the compensation curve is itself steep, which reduces the relative value of earlier picks. The surplus curves corresponding to _s_ (orange) and right tail (teal) _g_ functions are much steeper 

7 

than the traditional linear surplus curve (blue). Even after accounting for the varying cost of players across the draft, placing exponentially more value on eliteness than lesser outcomes produces a steeper value curve. Further, recall the loser’s curse from Massey and Thaler (2013) and Section 1. According to the expected surplus value curve (blue), bad teams who generally pick at the top of the draft have less valuable picks than better teams who pick later in the first round. The effect size of the loser’s curse diminishes significantly if we use a nonlinear _g_ . The surplus peaks of the orange and teal curves barely lie above 1, and those peaks appear earlier in the first round than the peak of the blue curve. 



Figure 6: Various trade market value functions _v_ ( _x_ ). 

## **2.4 Adjusting for position** 

It is imperative to adjust for position (pos), or at least for quarterbacks (qb), in modeling the density of performance outcomes. Notably, quarterbacks command the largest contracts in the NFL, they have by far the highest wins above replacement according to PFF WAR (Eager, 2020), and anyone who watches football knows elite quarterbacks like Brady or Mahomes are incredibly valuable. Formally, quarterbacks have a much fatter right tail than other positions, as they have a much higher mean and variance than other positions. 

Accordingly, we estimate the conditional density P( _Y |x,_ pos) using a Bayesian hierarchical model.<sup>4</sup> It is crucial to shrink positional estimates towards a common mean since there are so few datapoints for each position. The standard errors of the positional conditional densities (and conditional means) are huge and need to be accounted for. We don’t find large or significant differences across non-quarterback positions. But, quarterbacks have significantly higher conditional mean and variance curves (and hence fatter right tails) than non-quarterbacks. Thus, in formulating draft trade value curves, we consider just quarterbacks and non-quarterbacks. We define the non-quarterback conditional density by averaging over all the non-quarterback positions, P( _Y |x,_ not qb) := #pos1 _−_ 1 � _k_ =qb<sup>P(</sup><sup>_Y |x,_pos =</sup><sup>_k_).</sup> 

First, we consider performance value curves for quarterbacks and non-quarterbacks. Formally, we consider curves proportional to E[ _g_ ( _Y_ ) _|x,_ qb] and E[ _g_ ( _Y_ ) _|x,_ not qb]. We normalize both of 

> 4We devise a Bayesian hierarchical model that includes position-specific parameters for each of the _α_ , _β_ , and _γ_ parameters from the previous model. We shrink the position-specific coefficients _α∗,_ pos, _β∗,_ pos, and _γ∗,_ pos towards overall mean parameters _α∗_ , _β∗_ , and _γ∗_ . We omit details due to space constraints. 

8 

these curves to be relative to the value of a first pick qb. In Figure 7 we visualize several of these curves for various choices of _g_ . 



Figure 7: Various draft trade performance value curves relative to the value of a first pick qb. 

The non-quarterback curves are less steep than the quarterback curves. This is because the mean and variance of top pick quarterbacks are so extraordinarily high relative to other positions and later picks (see Figure 8), particularly the variance. For the curves derived from extreme right tail probabilities _g_ step( _y_ ) = I ( _y >_ 0 _._ 15) (orange) and _g_ step( _y_ ) = I ( _Y >_ 0 _._ 20) (blue), a non-quarterback first pick is worth about 10% and 1%, respectively, of a quarterback first pick. The value of later non-quarterback picks quickly converges to 0% of a first pick quarterback. This makes sense: just about the only way to get an extremely elite, far right tail performance outcome is from a quarterback. For the traditional expected performance value curves (yellow) corresponding to _g_ line( _y_ ) = _y_ , a non-quarterback first pick is worth about 60% of a first pick quarterback. This makes sense: a non-quarterback drafted first will on average provide less value than a quarterback drafted first, but nowhere near as much less value than if we value performance by eliteness. The _s_ curves _g_ s (magenta and chartreuse) lie between the extremes of _g_ step and _g_ line. 



Figure 8: For pos _∈{_ qb _,_ not qb _}_ , the posterior mean estimates (lines) of _µ_ ( _x,_ pos), sd( _x,_ pos), and bp( _x,_ pos) as a function of draft pick _x_ and position pos (color). We also include 95% credible intervals (the shaded regions) to these curves. 

Next, we consider surplus value. Formally, we consider curves proportional to E[ _g_ ( _S_ ) _|x,_ qb] and E[ _g_ ( _S_ ) _|x,_ not qb]. We again normalize both of these curves to be relative to the value of a first pick qb. In Figure 9 we visualize several of these curves for various choices of _g_ . 

For both qb and not qb, the traditional expected surplus value curve (yellow) corresponding to _g_ line( _y_ ) = _y_ features the loser’s curse (a spike in the middle of the first round). For quarterbacks, 

9 



Figure 9: Various draft trade surplus value curves relative to the value of a first pick qb. 

the loser’s curse all but disappears for other nonlinear outcome valuations _g_ s and _g_ step. Placing exponentially higher value on elite outcomes produces surplus curves lying just about entirely below 1. The far right tails of _Y_ are so fat for top pick qb’s that even the high cost of top picks doesn’t massively diminish their value. For non-quarterbacks, the loser’s curse is more prominent, even for nonlinear _g_ . Surplus value peaks in the middle of the first round and decays across the draft. This makes sense: early picks’ compensation are priced for the ultra high mean and variance of quarterbacks. On average, this price becomes too high for other positions. Further, the more value a general manager places on eliteness (i.e., as _g_ transitions from _g_ line to _g_ s to _g_ step), the smaller the effect size of the loser’s curse for not qb. This makes sense: the more eliteness matters to a general manager, the more he is willing to justify paying the high cost of earlier picks. 

# **3 Discussion** 

Traditional NFL draft position value curves are proportional to expected performance or surplus value. These curves are much less steep than the value curve implied by the trade market and Jimmy Johnson’s trade value curve. To proponents of traditional curves, general managers on average make terrible trades. They often overpay when they trade up in the draft and they don’t trade down often enough. We, on the other hand, posit that general managers are using some other value function that may have merit. Valuing a pick by its expected value does not necessarily align with a general manager’s primary problem of interest, which is to maximize the chance of winning the Super Bowl. To win a Super Bowl, elite players, and particularly elite quarterbacks, are exponentially more valuable than good or median players. Accounting for such nonlinear valuations of performance outcomes, for instance using right tail probability, yields steeper draft trade value curves that more closely resemble the market. 

# **Acknowledgments** 

The authors thank Blake Zilberman, Cade Massey, and Christopher N. Avery for inspiring them to explore the analytics behind NFL draft value trade charts. We also thank Cade and Chris for sending NFL draft data for an early version of this project. 

10 

# **References** 

- Baldwin, B. (2024). NFL Draft Value Chart: Constructing surplus value from scratch. `https://opensourcefootball.com/posts/2023-02-23-nfl-draft-value-chart/` . 

- Eager, E. (2020). Pff war: Modeling player value in american football. 

- Ferrari, S. and Cribari-Neto, F. (2004). Beta regression for modelling rates and proportions. _Journal of Applied Statistics_ , 31(7):799–815. 

- Fitzgerald, J. and Spielberger, B. (2024). Fitzgerald-Spielberger NFL Draft Trade Value Chart. `https://overthecap.com/draft-trade-value-chart` . 

- Ho, T. and Carl, S. (2024). _nflreadr: Download ’nflverse’ Data_ . R package version 1.4.0.12, https://github.com/nflverse/nflreadr. 

- Massey, C. and Thaler, R. H. (2013). The loser’s curse: Decision making and market efficiency in the national football league draft. _Management Science_ , 59(7):1479–1495. 

- Pro Football Focus (2024). The PFF draft value chart. 

`https://www.pff.com/news/draft-pff-draft-value-chart` . 

- Stuart, C. (2012). Draft Value Chart. 

   - `https://www.footballperspective.com/draft-value-chart/` . 

11 


