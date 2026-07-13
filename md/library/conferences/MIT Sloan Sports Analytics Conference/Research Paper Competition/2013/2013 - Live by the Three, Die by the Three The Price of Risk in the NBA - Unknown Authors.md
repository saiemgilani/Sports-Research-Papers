<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2013/2013 - Live by the Three, Die by the Three The Price of Risk in the NBA - Unknown Authors.pdf -->



# Live by the Three, Die by the Three? The Price of Risk in the NBA 

Matthew Goldman Justin M. Rao UC San Diego Microsoft Research Dept. of Economics 102 Madison Ave. La Jolla, CA 92093 New York, NY 10016 mrgoldman@ucsd.edu justin.rao@microsoft.com 

## Abstract 

An important problem facing a basketball team is determining the right proportion of 2 and 3 point shots to take. With many possessions remaining, a team should maximize points—a 3-pointer is simply worth 1.5 2-pointers. 3-point attempts have roughly double the per-shot variance as 2-point attempts, but a team should be “risk neutral.” As time remaining decreases, the trailing team _should_ place an increasingly positive value on risk; the opposite holds for the leading team. Our game theoretic analysis yields a testable optimality condition: 3-point success rate _must_ fall relative to 2-point success rate when a team’s preference for risk increases. Using four years of play-by-play data, we find strong evidence this condition holds for the trailing team only. As a lead decreases, the leading team should become more risk-neutral, but teams in this circumstance actually tighten up and become more risk averse, contrary to what their risk preferences ought to be to maximize the chance of winning the game. We also show that if the offense shoots more 3’s as it becomes risk-loving this implies the attack can be varied more readily than the defensive adjustment. 3-point usage does increase with the trail team’s preference for risk, but actually falls for the leading team. Teams get it right when losing and wrong when winning. We also find a strong motivating effect of losing—the trailing teams displays an overall boost in efficiency for both shot types. 



2013 Research Paper Competion Presented by: 





## 1 Introduction 

In order to optimize, a basketball team must determine the right proportion of 2 and 3 point shots to take. In this paper we study how NBA teams solve this problem. The trade-off between 2’s and 3’s depends critically on the score margin and the time-remaining in the game. Early in the game, a team should maximize points per possession—a 3 pointer is simply worth 1.5 2-pointers. Since 3-pointers have about double the per-shot variance in point outcomes as 2-pointers, this implies a team should be “risk neutral” in these situations. Moving towards the end of the game changes this trade-off. With a relatively small number future opportunities, the trailing team should place an increasingly positive value on risky 3-point opportunities because they need a large swing in points to catch up; conversely the leading team should place a negative value on risk, favoring predictable scoring opportunities. Using detailed play-by-play data for six years of NBA games, we empirically quantify the true value of 3-pointers relative to 2-pointers as a function of score margin and time remaining. We do so by calculating the impact a made shot of each type has on the chance the team wins the game for all the game states in our sample. It is not uncommon for a made 3-pointer to be worth as much as 1.8 and as little as 1.2 times the “win value” of a made 2-pointer. 

We model a team’s choice of the proportion of shots between 2 and 3-pointers using the tools of game theory. Solving the model gives the optimal mix of 2’s and 3’s. If we assume the defense cannot adjust, then when the offense’s preference for risk increases, optimality implies it shoots more 3-pointers, 3-pointer efficiency falls, 2- pointer efficiency rises and the win value of 3’s rises. The model makes clear that even in the risk-neutral setting, optimal shot selection does not imply that 2 and 3 pointers offer the same average points per attempt (average efficiency). 

We extend the model by allowing for the defense to adjust the allocation of scarce defensive attention between two and three-point defense. An increasing preference for risky 3-pointers by the offense is associated with an increase in the defense’s incentive to guard against them. Allowing for a flexible class of defensive responses, we show that 3-point efficiency should be inversely correlated with a team’s preference for risk—as a team becomes more risk loving, optimal shot selection implies that 3-point percentage _must_ go down. Our final extension allows for a direct motivating effect of trailing; in this case the key prediction is the 3-point percentage must fall relative to 2-point percentage. The defensive adjustment model shows that the offense shoots more 3’s when their preference for risk goes up only if the offense’s ability to vary the“attack” exceeds the defense’s ability to adjust. 

We empirically test these predictions using four seasons of NBA play-by-play data. We allow for different model estimates for each team-season and condition non-parametrically on both the offensive and defensive 5-man lineup to control for potential biases induced by substitution. Consistent with optimal shot selection, the trailing team exhibits strong statistical evidence ( _t_ = 8 _._ 28) that the point value of 3’s falls relative to 2’s as the offense’s preference for risk increases. The trailing team also shoots more 3’s. In stark contrast, the leading team significantly violates our key optimality proposition. Leading teams shoot _fewer_ 3’s as their preference for risk increases and these 3’s have _higher_ point value. As a lead decreases, the leading team should become more risk-neutral, but instead tighten up and actually become more risk averse, contrary to what their risk preferences ought to be to maximize the chance of winning the game. 

Interestingly, we also find a large motivating effect of being behind (also discussed in our related paper [4])—for a given offensive and defensive line-up, the trailing team displays an increase in efficiency for both 2 and 3-pointers. This effect is similar in spirit to the findings of Pope and Berger (2011) [1] that a team trailing by 1-point at halftime wins slightly more often than the team leading by 1-point. The extra motivation of being behind has ties to Kahneman and Tversky (1979)’s theory of “loss aversion”—the principle that people are more motivated to “remove losses” than “seek gains” [8].<sup>1</sup> In the context of the NBA, our results indicate that these sort of motivational links do not depend on a halftime speech, tactical adjustments or line-up changes. Whether this effect is driven by the leading team’s complacency or the trailing team’s motivation (or both) is not a question our data can speak to, but the net effect is clear. 

The loss-aversion finding combined with the suboptimal shot selection of leading teams helps explain why teams tend to stage more comebacks than we’d otherwise expect. Since games tend to get close late, clutch moments are 

1Rick and Loewenstein (2008) [6] also provide laboratory evidence in favor of this type of “motivational loss aversion.” 2013 Research Paper Competion Presented by: 





1 



relatively frequent. We show that for an average team it’s harder to score in clutch moments, but very good offenses actually do better in the clutch and bad defenses get worse. Taken together, this means good teams have an even greater advantage when the chips are down. 

## 2 Quantifying a Team’s Objective Function 

A team’s goal is to win the game. Accordingly, we are interested in estimating the mathematical function that gives the “win value” of a given action. “Win value” refers to the impact the action has on the probability a team wins the game. The three most important factors that determine the win value of an action at a given game state, especially late in the game, are the score margin, time remaining and possession of the ball. The increase in win probability of adding 2 or 3 points to the team’s current score are denoted _WV_ 2 and _WV_ 3 respectively. The most straightforward estimation approach for these quantities is to take a large number of games at a given game state _X_ and compare the probability of winning at _X_ to a “nearby” state _X_<sup>_0_</sup> . For example, natural variation in actions taken at _X_ give us some cases where a shot was missed, some where a 2-pointer was made and some where a 3-pointer was made. Intuitively, comparing the frequency which a team wins after these outcomes gives us the value these actions. 

We define _p_ ( _X_ ) as the probability a team wins the game in state _X_ . Econometrically we have two options to calculate this quantity. The first method is “non-parametric”—it relies on local averages as described in the above paragraph. The second is the “parametric” procedure developed in Goldman and Rao (2012) [3]. We describe it here in the Appendix for completeness. This approach conditions on team quality, home court and game-state using a Probit regression. Appendix Figure 1 shows that both methods yield very similar projections. Given the lower noise in the parametric estimates (smoother function, Panel 1), our analysis will proceed using those estimates. The relationship between the win value of 3’s and 2’s can be represented by the parameter _↵_ defined as: 



_↵_ defines the degree to which 3-pointer win value diverges from 1.5 2-pointers. We refer to standard point values as “nominal values.” In a most game situations, especially in the first half, scoring 3 points on a given possession is worth very close to 1.5 times scoring 2 points. When _↵>_ 1 _._ 5, the win value of a 3-pointer exceeds it’s nominal value. This occurs for the trailing team, especially late in the game. The effect can be seen in the convexity in the trailing region of Appendix Figure 1. The reason is that the trailing team needs a relatively large swing in points to catch-up—a higher variability shot is worth more because it increases the chance of this large swing. The opposite is true for the leading team (which has _↵<_ 1 _._ 5)—here a 3-pointer is worth relatively less than usual since the team should be risk-averse. 

In Figure 1 Panel 1 we plot _↵_ as function of game state (margin, time remaining) for even strength teams on a neutral court over the first 3 quarters (Panel 1) and the fourth quarter (Panel 2, note the change in y-axis scale). In the first half _↵_ is always close to 1.5. In the third quarter we see more variation; _↵_ is between 1.4 and 1.6 provided the margin is less than 11 points. In the 4th quarter, _↵_ varies widely. With fewer possessions remaining, the trailing (leading) team’s preference for risk increases (decreases) dramatically.<sup>2</sup> 

## 3 Modeling a Team’s Shot Allocation Problem 

We express a team’s optimization problem as a function of _↵_ , solving gives the optimal mix of 2 and 3-pointers for each game situation. We will employ a concept in basketball analysis called the “usage curve” [5, 7, 2]. The 

> 2 _↵_ is a natural proxy for a team’s preference for risk because it maps directly to the relative preferences over potential outcomes. Consider a case where _p_ 2 = 0 _._ 50 and _p_ 3 = 0 _._ 33. In this case there is an expected nominal value of one point for reach shot. The variance in the return of a 3-point attempt is 3<sup>2</sup> _._ 33 _⇤ ._ 66 = 1 _._ 96 and for the two-pointer 2<sup>2</sup> _._ 5<sup>2</sup> = 1. Suppose _↵_ = 1 _._ 7. This means the expected utility (expected real value) of a 3-pointer is 0.33*1.7* _WV_ 2=0.561* _WV_ 2 and 2-pointer is worth 0 _._ 5 _⇤ WV_ 2; or in other words, the 3-pointer is worth 12% more in win value, despite having equal nominal value. If we model the team as have preference over mean and variance, we could map any _↵_ to a utility value of variance. However, we view _↵_ as a more directly interpretable parameter. 

2013 Research Paper Competion Presented by: 





2 























Figure 1: _↵_ as a function of game state. Quarters 1-3 (left) and Quarter 4 (right). 

usage curve relates the frequency of a given shot (in this case a 2 or 3-pointer) to it’s success rate. Usage curves are naturally assumed to be downward sloping and were estimated as such in Goldman and Rao (2011). This feature implies that as a team shoots more 3’s, the probability of success on each successive 3-point attempt goes down.<sup>3</sup> Let _φ_ ( _u_ 3) denote the average probability of success for 3-pointers when the fraction of shots attempted as 3’s is _u_ 3 _2_ [0 _,_ 1] and (1 _− u_ 3) the corresponding average probability of success on 2-poin attempts. The downward sloping assumption implies _dudφ_ 3<sup>_<_0,</sup> _du_<sup>_d_</sup> 3<sup>_>_0—asateamshootsmore3-pointerstheaveragereturnsto3’sgo</sup> down and the average returns to 2’s goes up. Recalling that we define the win value of 3’s in relation to 2’s as _WV_ 3 = _↵WV_ 2, we can now write the team’s maximization problem as: 





The first order condition states that the marginal returns to 2-pointers and 3-pointers should be equal. The left side gives the marginal returns to shooting a 3-pointer. Shooting an extra 3-pointer returns the current average value _↵ ⇤ φ_ ( _u_ 3), but it also impacts the average value of all the other 3-pointers taken _u_ 3 by a degree given by the slope of the usage curve ( _φ_<sup>_0_</sup> ( _u_ 3)). The right hand side gives the marginal returns to shooting a 2-pointer and can be understood with similar logic. In this model with no defensive adjustment, _u_ 3 is increasing with _↵_ . To see this note that if _↵_ increases then the left side goes up because the term _φ_ ( _u_ 3) + _φ_<sup>_0_</sup> ( _u_ 3) _⇤ u_ 3 has to be positive, otherwise the marginal 3-pointer nets negative value. So the left side must increase, to counter-act this, the right side must go up as well which occurs only when _u_ 3 increases. 

Appendix Figure 2 gives a graphical representation of the maximization problem and the impact of an increase in _↵_ . Starting at _↵_ = 1 _._ 5, point _A_ determines the baseline optimal shot mix. Optimal shot choice does not imply 2-pointers and 3-pointers offer the same average point value. The difference in average shot value is determined by the slope of the usage curves and the y-intercepts. In practice 3-pointers tend to return greater average efficiency and are shot less often than 2’s, together this imples a higher y-intercept and a steeper slope in the usage curve for 3’s. The figure also shows the impact of an increase in _↵_ , which is represented by the shift out in the 3-point value 

> 3Goldman and Rao (2011) give an empirical reason for downward sloping usage curves in this setting. If we model the offense as getting shot opportunity arrivals over the course of a 24-second shot-clock, then to take more 3’s, the team has to accept lower quality 3-point opportunities on the margin. 



2013 Research Paper Competion Presented by: 



3 



curve. The new equilibrium is given by the vertical line intersecting _A_<sup>_0_</sup> . Point _B_<sup>_0_</sup> gives the new win value of 2’s and point _C_<sup>_0_</sup> the new win value of 3’s. Point _D_ gives the new nominal value of 3’s (the point value). We are now now in a position to state our first proposition: 

Proposition 1 _In the model with no defensive adjustment, as ↵ increases the fraction of 3’s attempted (u_ 3 _) goes up, the nominal value of attempted 3’s goes down, the nominal value of attempted 2’s goes up and the real value of attempted 3’s goes up._ 

#### _Proof: See Appendix_ 

The model without defensive adjustment is useful to provide intuition and also can be interpreted as representing a world in which defensive adjustments matter relatively little, which may apply, for instance, to a team playing man-to-man defense that lacks the quickness and length to alter their strategy and really clamp down on opposing 3-point shooters. Incorporating defensive adjustments to our model is straightforward; the defense’s objective is simply the opposite of the offense’s (it wants to minimize equation 2)—an increase in the value of 3’s increases the incentive to defend against them. We assume the defense has a unit of “defensive resources,” which it can apply to defending 2’s and 3’s: _d_ 2 + _d_ 3 = 1; more defensive attention lowers the success rate of a shot type. We modify the usage curves to include defense ( _φ_ ( _u_ 3 _, d_ 3) _, β_ ( _u_ 2 _, d_ 2)). Analysis of this model is involved so we have placed it to the Appendix. Interested readers are directed there. We now state our second and third propositions: 

Proposition 2 _In the model with defensive adjustment, as ↵ increases the nominal value of attempted 3’s falls and the nominal value of attempted 2’s rises._ 

#### _Proof: See Appendix_ 

Proposition 3 _In the model with defensive adjustment, as ↵ increases the change in the usage rate of 3’s is ambiguous. It depends on the slope of the 3-point usage curve, the impact of defensive on the marginal shot values and the concavity of the usage curves with respect to defensive pressure._ 

#### _Proof: See Appendix_ 

Proposition 2 states that the prediction of the no-defense model that carries through is the drop in the nominal efficiency of 3’s as _↵_ increases. Proposition 3 states that the other predictions of the simple model are not robust when we allow for a large class of defensive pressure adjustments. With defensive adjustment, the offense will shoot more 3’s provided the defense cannot adjust pressure effectively enough to discourage these additional attempts. The details, which are in the Appendix, are a bit a hard to grasp at first, but the main intuition comes down to relative flexibilities of the offensive attack and defensive response. 

Our final extension of the model is to allow for a multiplicative function of _↵_ on each usage curve that accounts for a possible motivational impact of being behind in the game (we could also model this as an additively separable term). It is easy to show that this term will cancel out of the first order conditions. However, we must amend Proposition 2 to be: 

Proposition 4 _If we allow for a motivational impact of trailing and defensive adjustment, then as ↵ increases the nominal value of 3’s falls relative to the nominal value of 2’s._ 

When 3’s become more valuable, maximization implies that the efficiency of 3’s must fall relative to 2’s. This is our most robust prediction, as it is true in the very general defensive adjustment setting and allowing for an extra motivational impact of being behind. Optimization _requires_ that Proposition 4 holds. 





2013 Research Paper Competion Presented by: 

4 



## 4 Results 

In our empirical analysis, we are careful to exclude situations in which one team has less than a 5% chance of winning. Actions in “garbage time” lack meaningful consequences and tell us nothing useful about whether a team is optimizing. We also eliminate fast-breaks (shot clock _>_ 14) and end of quarter shots, as they tend to have very deifferent strategic considerations. 

### 4.1 Frequency of 3-point vs. 2-point shot attempts 

We first examine the impact of _↵_ on the usage rate of 3-pointers. We model the probability a team’s first shot on a possession is a 3-pointer using a random coefficient linear probability model, which allows coefficients to vary for each team in each season (a “team-year”). We control for unique five-man offensive lineup ( _δ_ ) and opposing defensive lineup ( _γ_ ) using fixed effects for each line-up. Our estimating equation is given by: 



where _Offp_ and _Defp_ denotes the five-man offensive and defensive line-ups on possession _p_ , respectively, and _↵p_ denotes the value of _↵_ faced by the offensive team on possession _p_ . This specification is very general and ensures that we are not confounded by lineup effects. _β_ 1 gives the impact of an increase in _↵_ for possessions when _↵<_ 1 _._ 5, which corresponds to the case when the team is leading. In this case, _↵_ increasing pushes the team closer to the risk-neutral baseline. _β_ 2 gives the impact of an increase of _↵_ when _↵>_ 1 _._ 5, meaning the team is trailing. In this case, _↵_ increasing moves the team to a more desperate, risk-loving situation. In both cases, as _↵_ increases, the team’s preference for 3-pointers is increases relative to 2-pointers. Estimating this model for each team-year in our sample produces 120 total estimates of each parameter. 

Table 1: Random _−_ coefficient estimates of the impact of _↵_ on three _−_ <u>point usage rates.</u> 

|Explanatory<br>Variable|Weighted average<sup>_†_</sup><br>coeffcient|Mean<br>coeffcient|Median<br>coeffcient|
|---|---|---|---|
||_t−stat_|_t−stat_|_t−stat_<sup>_‡_</sup>|
|_β_1 :_↵p ⇥_1_{↵p _1_._5_}_|_−_0.105|_−_0.108|_−_0.0799|
||_t=−8.21_|_t=−8.24_|_t=−2.37_|
|_β_2 :_↵p ⇥_1_{↵p >_1_._5_}_|0.231|0.243|0.175|
||_t=13.40_|_t=13.44_|_t=3.47_|



Team-years=120, Shots=481,544 _†_ Inverse variance weights used to aggregate coefficients. 

_‡_ Sign test used to construct t _−_ statistics on the median. 

Table 1 aggregates the estimated coefficients. Examining the first row, we see that _β_ 1 is significantly _negative_ . When a leading team’s _↵_ increases, it shoots fewer 3-pointers; that is, the opposite direction as predicted by the no-defensive adjustment model. As shown in Figure 1, _↵_ increasing for the leading team means, all else equal, the game is getting closer. The leading team appears to tighten up in this situation, shooting fewer 3’s, despite the fact their preference for 3’s is increasing. Taken alone, we cannot conclude that this pattern of behavior, while perhaps surprising, is a violation of optimal shot selection because in our model with defensive adjustments that the impact of _↵_ on 3-point usage rate depends on the relative adjustment ability of the offense vs. defense. However the estimates of _β_ 2 give us some evidence that this negative coefficient is in fact a sign of sup-optimal behavior. Examining the second row, we see that for the trailing team, as _↵_ increases the team shoots more 3’s. 

The usage behavior displays an interesting asymmetry. When a trailing team’s preference for 3’s goes up (becomes more risk-loving), it shoots more 3’s and fewer 2’s. But when a leading team should become more risk- 



2013 Research Paper Competion Presented by: 



5 



neutral, it actually behaves in a more risk-averse way, switching to 2-pointers. If we make the reasonable assumption that the defensive adjustment technology is similar when a team is leading vs. trailing, then the usage estimates indicate that trailing teams respect changing risk preferences (the “price of risk”), but leading teams do not, even so far as inverting the relationship. 

### 4.2 The efficiency of 3-point vs. 2-point shot attempts 

We delve further into this asymmetry in our analysis of shooting efficiency. Recall that our most robust prediction is given by Proposition 4. Even if players get generally better when they are trailing, our theoretical model still implies that 3-point opportunities cannot increase in value as much as 2-point opportunities. That is, the gap in point value between 3 and 2-point attempts must be declining with _↵_ . We investigate this claim with the following random-coefficients linear regression model: 



We again include fixed effects for each unique five-man offensive and defensive line-up to exclude confounding effects from lineup selection. We have written expected points as the dependent variable, but we actually use 3 different, albeit similar, measures (we will use the word “efficiency” to refer to the class of dependent variables we use and discuss differences below). _β_ 1 can be interpreted as the average efficiency differential between 3 and 2-point shots in a risk-neutral ( _↵_ = 1 _._ 5) game state. _β_ 2 captures the impact of _↵_ on 2-pointer efficiency for the leading team ( _↵ _ 1 _._ 5), while _β_ 3 captures this effect for the losing team. _β_ 4 and _β_ 5 directly test Proposition 4, these coefficients represent the _differential_ effect of _↵_ on the efficiency of 3-point attempts for a winning and losing team respectively. 

The three dependent variables are reported in Panels 1–3 of Table 2. Panel 1 gives the“effective field goal %,” which is simply the points scored on the shot for shooters that were not fouled. Panel 2 gives “true shooting %,” which takes the number of points scored on the shot plus any free-throws made related to the shot<sup>4</sup> . In Panel 3 we report “gross offensive efficiency,” which is the number of points scored on a possession after the shot attempt occurs (this includes the shot going in, free-throws related to the shot and any points scored after an offensive rebound(s)). By using all three variables we can discern if the effects are being driven by differential offensive rebounding rates across shot types or fouling patterns by the defense. 

Estimates of _β_ 1 _−_ 5 are computed for each team-year. The following results apply to all three dependent variables, we discuss differences where necessary. _β_ 1 is strongly positive—3 pointers have higher average point returns in the risk-neutral baseline. For gross-offensive efficiency and true shooting %, the mean estimate is about 0.15 points-pershot. Recall that this implies a higher constant and steeper slope for the 3-point usage curve. The estimates for _β_ 2 and _β_ 3 are dramatically, and very significantly, positive. This means that as a team goes from being ahead to being behind, 2-pointers get more and more efficient. This effect is in fact stronger for a trailing team ( _β_ 3 _> β_ 2). This is strong evidence of the motivational impact of losing.<sup>5</sup> We note that the _β_ 3 : _β_ 2 ratio is highest for gross possession efficiency, indicating that some of the motivational effect of losing is coming through offensive rebounds (which the two other measures ignore, the estimates indicate about 30% of the effect is coming through rebounding). 

The key test of optimality lies in the estimates of _β_ 4 and _β_ 5. Proposition 4 states that optimal response to changing incentives over risk requires that both coefficients are negative. The reason is that as _↵_ increases, a offense should become more risk-loving and the defense should want to defend 3’s more—since the true value of a 3- pointer has increased, the nominal or point value of a 3 should decrease in equilibrium. First the positive results: this optimality condition is met for trailing teams, _β_ 5 is significantly negative ( _p <_ 0 _._ 0001 for the weighted average in all specifications). As the trailing team becomes increasingly risk-loving, the point value of 3-pointers declines relative to 2-pointers just as predicted by the theory. Recall from Table 1 that the trailing team also responds by 

> 4Note these first two measures are usually computed with a 1 for a made 2-pointer and 1.5 for a made 3-pointer in order to have the same scale as traditional FG%. We instead use 2 and 3 respectively (effectively doubling the value), in order to stay consistent with our other third measure. 

5The impact of losing on player motivation and performance is examined more closely in a related paper of ours [4]. 2013 Research Paper Competion Presented by: 





6 



Table 2: Random _−_ coefficient estimates of the impact of _↵p_ on nominal returns to three point attempts. 

||Effect|ive Field Goa|l %|Tru|e Shooting|%|Gross Po|ssession Eff|ciency|
|---|---|---|---|---|---|---|---|---|---|
|Explanatory<br>Variable|Weighted<sup>_†_</sup><br>avg. coeff.|Mean<br>coeff.|Med.<sup>_‡_</sup><br>coeff.|Weighted<sup>_†_</sup><br>avg. coeff.|Mean<br>coeff.|Med.<sup>_‡_</sup><br>coeff.|Weighted<sup>_†_</sup><br>avg. coeff.|Mean<br>coeff.|Med.<sup>_‡_</sup><br>coeff.|
|_β_1 : 1_{_3PA_p}_|0.223|0.221|0.218|0.143|0.142|0.143|0.155|0.155|0.158|
||_t=49.50_|_t=48.59_|_t=10.77_|_t=31.95_|_t=31.40_|_t=10.22_|_t=34.74_|_t=34.20_|_t=10.59_|
|_β_2 :_↵_<sup>_⇤_</sup><br>_p_<sup>_⇥_</sup>|1.71|1.78|1.65|1.58|1.65|1.54|1.84|1.92|1.76|
|1_{↵p _1_._5_}_|_t=39.72_|_t=40.21_|_t=10.22_|_t=39.04_|_t=39.76_|_t=10.22_|_t=45.54_|_t=46.14_|_t=10.22_|
|_β_3 :_↵p⇥_|2.3|2.34|2.14|2.8|2.83|2.64|3.33|3.35|3.25|
|1_{↵p >_1_._5_}_|_t=38.20_|_t=37.05_|_t=10.22_|_t=50.82_|_t=49.16_|_t=10.95_|_t=60.30_|_t=58.26_|_t=10.77_|
|_β_4 : 1_{_3PA_p} ⇥↵p_|0.213|0.185|0.142|0.343|0.337|0.348|0.387|0.384|0.317|
|_⇥_1_{↵p _1_._5_}_|_t=2.44_|_t=2.03_|_t=0.91_|_t=3.97_|_t=3.74_|_t=2.56_|_t=4.47_|_t=4.26_|_t=2.37_|
|_β_5 : 1_{_3PA_p} ⇥↵p_|_−_0.71|_−_0.758|_−_0.66|_−_1.1|_−_1.18|_−_0.965|_−_0.969|_−_1.03|_−_1.05|
|_⇥_1_{↵p >_1_._5_}_|_t=−5.92_|_t=−6.11_|_t=−2.92_|_t=−9.45_|_t=−9.73_|_t=−4.56_|_t=−8.28_|_t=−8.47_|_t=−4.56_|
|<br>Team-years=120, Shot<br>_‡_Sign test used to con|s=481,544,_†_ <br>struct t_−_statis|Inverse varia<br>tics on the m|nce weights<br>edian. <sup>_⇤_</sup>We|used to aggrega<br>suppress the|te coeffcien<br>_−_1_._5.|ts||||



shooting more 3-pointers as well, meaning the results are consistent with the offensive having a greater ability to adjust than the defense (qualitatively consistent with the no defensive adjustment model). The offense shoots more 3’s and the average value falls—making this trade-off respects the true value of 3-pointers in terms of winning the game and is consistent with a downward sloping usage curve. 

The results take a different turn when we examine the behavior of the leading team. _β_ 4 is estimated to be significantly _positive_ (about 1/3 the magnitude of _β_ 5). This is the wrong direction and is a violation of optimal shot selection. Recall that we found in Table 1 that the leading team tends to shoot fewer 3’s when _↵_ increases. Here we see that this decrease in usage is accompanied by an increase in efficiency, which is again consistent with a downward sloping usage curve and limited defensive adjustment. For a leading team, as the game gets closer, the team _should_ become more risk-neutral, yet the team actually behaves in a more risk averse manner. Leading teams do not appear to place the right price on risk, whereas trailing teams do. 

### 4.3 The Rubber-band effect and performance in the clutch 

So far we have documented two important behavioral patterns that increase the likelihood of a comeback by the trailing team. First, the trailing team shows a boost in efficiency for both shot types. Second, the leading team tightens up as the score gets closer – shooting fewer 3’s and more 2’s, contrary to the change in their incentives. We call the combined impact the “rubber band effect.”<sup>6</sup> More games tend to be close late than we’d otherwise expect to observe. What this means is that performance in the clutch tends to be very important in the NBA, because clutch moments are relatively frequent. 

The natural question is “how is team quality related to clutch performance.” To answer this question we estimate how gross offensive efficiency relates to the win value of a point (a natural measure of how importance points are). Our estimating equation is given by, where we again use line-up fixed effects: 



We plot the results in Figures 2 and 3. The y-axis measures the difference in performance in a clutch moment (WVP=0.07, a moment in which each point increases the teams chance of winning by 8 percentage points, which corresponds to about the 97th percentile of importance) as compared to how that team does in a median moment (WVP=0.02). We call this measure the “clutch bonus” and plot it as points per 100 possessions. In Figure 2, the x-axis gives baseline offensive efficiency (points scored per 100 possessions in typical situations). This is a natural measure of pace-adjusted offensive quality. Each dot represents a team-year. It is clear that on average teams do 

6Substitutions to conserve star players for games down the road could also contribute and is outside the scope of our ‘fixed lineup’ analysis. 2013 Research Paper Competion Presented by: 





7 



worse in clutch moments—for most teams it’s harder to score when the chips are down. The slope of the fitted line is 1 _._ 65 and highly significant ( _t_ = 7 _._ 27). This indicates that the better a team is at offense, the better it does in the clutch relative to its own baseline—bad teams do much than their worse than their baseline, average teams do a little worse and very good teams actually get better in the clutch. 

In Figure 3 shows how defense quality relates to clutch performance. Defensive efficiency, given on the x-axis, is points allowed per 100 possessions, so lower numbers correspond to stingier defenses. The y-axis gives the clutch bonus of the opposing team. It measures how well the defense performs in the clutch, with negative values being good. Again we see most values are negative—the average defense is better in the clutch. The clutch bonus is more negative for better defensive teams; for rather poor defensive teams the value is positive, meaning they consistently do worse in the clutch as compared to baseline scenarios. The slope of the fitted line is _−_ 1 _._ 09 ( _t_ = 4 _._ 20). 

Comparing the absolute values of the fitted lines and the _R_<sup>2</sup> of the regressions, we conclude the impact of unit quality on clutch performance is significantly stronger and less noisy on the offensive side of the ball. What this means is that for two evenly matched-up teams in terms of baseline performance, a team with a good offense will tend to have an advantage in the clutch. For teams of differing overall ability, the better team will have an advantage in the clutch on both sides of the ball and will thus tend to pull out more close games than their baseline advantage would suggest. 

























Figure 2: Offense clutch performance vs. baseline efficiency. 

Figure 3: Defense clutch peformance vs. baseline efficiency. 

## 5 Conclusion 

We theoretically and empirically investigate the optimality of NBA shooting decisions in response to changing incentives over risk. The most robust theoretical requirement is that the gap in nominal efficiency between 3 and 2-point attempts must be negatively correlated with the offense’s preference for risk. We find adherence to our key test of optimality for the trailing team—as a trailing team gets in a more desperate situation (becomes more riskloving), the efficiency of their 3-point attempts falls. The trailing team also tends to increase their fraction of 3-point attempts in proportion to their preference for risk, consistent with the ability to shift the offensive attack more flexibly than the defense can adjust resources. The leading team, however, violates our optimality requirement; leading teams shoot fewer 3’s as their preference for risk increases and these 3’s actually offer higher average point value (consistent with a downward sloping usage curve). As a lead decreases, the leading team should become more risk-neutral, but teams in this circumstance actually tighten up and become more risk averse, contrary to what their risk preferences ought to be to maximize the chance of winning the game. 

We also find a strong motivational effect of trailing on the scoreboard—a given lineup sees a boost inefficiency 



2013 Research Paper Competion Presented by: 



8 



for both 2’s and 3’s—combined with the sub-optimal shot selection of the leading teams this helps explain the surprising frequency of comebacks in the NBA and means clutch moments tend to occur more frequently that we’d otherwise expect. We show that for an average team it’s harder to score in clutch moments, but very good offenses actually do better in the clutch, whereas bad defenses actually get worse. Taken together, this means good teams have an even greater advantage when the chips are down. 

## References 

- [1] J. Berger and D. Pope. Can losing lead to winning? _Management Science_ , 57(5):817–827, 2011. 

- [2] Matthew Goldman and Justin M. Rao. Allocative and dynamic efficiency in nba decision making. In _Proceedings of the MIT Sloan Sports Analytics Conference_ , pages 1–10, 2011. 

- [3] Matthew Goldman and Justin M. Rao. Effort vs. concentration: The asymmetric impact of pressure on nba performance. In _Proceedings of the MIT Sloan Sports Analytics Conference_ , pages 1–10, 2012. 

- [4] Matthew Goldman and Justin M. Rao. Motivational loss aversion. 2013. 

- [5] D. Oliver. _Basketball on paper: Rules and tools for performance analysis_ . Brassey’s Press, 2004. 

- [6] S. Rick and G. Loewenstein. Hypermotivation. _Journal of Marketing Research_ , 45(6):645–648, 2008. 

- [7] B. Skinner. Scoring strategies for the underdog: Using risk as an ally in determining optimal sports strategies. _Journal of Quantitative Analysis in Sports_ , 7, 2011. 

- [8] A. Tversky and D. Kahneman. Loss aversion in riskless choice: A reference-dependent model. _The Quarterly Journal of Economics_ , 106(4):1039–1061, 1991. 

## 6 Appendix 

### 6.1 Figures 





















Appendix Figure 1: Parametric projects of win probability conditional on score margin and time remaining for the home team in even match-up; Panel 2: non-parametric estimates of the same function. 



2013 Research Paper Competion Presented by: 



9 





Appendix Figure 2: Graphical representation of the no-defensive adjustment model. The initial “profit maximizing” condition given by the line intersecting point _A_ and the impact of an increase in _↵_ with the new equilbrium given by the line intersecting _A_<sup>_0_</sup> . 

### 6.2 The model with defensive adjustment 

Offense (defense) seeks to maximize (minimize) the offenses increase in win probability in a given possession. This utility function (for the offense) is 



subject to the constraints that 



We assume the following (written in terms of _φ_ but they all hold for too): 

1. Usage curves are downward sloping: _φ_ 1 _<_ 0. 

> <sup>_<u>φ</u>_</sup><sup><u>(</u></sup><sup>_u_3))</sup> 2. Usage curves are such that marginal shots have declining value:<sup>_d_2(</sup><sup>_u_3</sup><sup>_·_</sup> = 2 _φ_<sup>_0_</sup> ( _u_ 3) + _u_ 3 _φ_<sup>_00_</sup> ( _u_ 3) _<_ 0 _du_<sup>2</sup> 3 2013 Research Paper Competion Presented by: 





10 



3. Defensive pressure lowers shooting percentage: _φ_ 2 _,_ 2 _<_ 0. 

4. Defense has diminishing returns: _φ_ 22 _,_ 22 _>_ 0. 

5. Using more possessions in a certain way increases (makes more negative) returns to defense against that type of use: ( _φ_ 2 + _u_<sup>_⇤_</sup> 3<sup>_φ_21)</sup><sup>_<_0.</sup> 

Let starred values denote the equilibrium quantities. Then the defense’s first order condition is given by 



where the subscript denotes a derivative in the corresponding argument. The offense’s first order condition is given by 



where the bracketed quantities represent marginal shot probabilities for 3 and 2 point shots respectively. Both of these must both be greater than 0. Taking total differentiation of (4) and omitting the arguments of _φ_ and yields 



and rearranges to 



where the values of _a_ 11 _, a_ 12 and _b_ 1 are defined implicitly. A similar analysis of equation (5) gives 



where the values of _a_ 21 _, a_ 22 and _b_ 2 defined implicitly. In matrix notation 



Then by Cramer’s Rule 



To sign these derivatives not that, _a_ 11 _<_ 0 (marginal shots have diminishing value), _a_ 22 _>_ 0 (diminishing returns to defense), and _a_ 12 = _a_ 21 _<_ 0 (shooting more 3s raises the effectiveness of defense on 3s). Thus both denominators are negative. Also _b_ 1 _>_ 0 (its a marginal shot value) and _b_ 2 _<_ 0 ( _φ_ 2 _<_ 0). Signing this derivative states that defensive pressure on 3’s must increase with _↵_ . 

_Proof of Proposition 2_ 



2013 Research Paper Competion Presented by: 



11 





<!-- Start of picture text -->
b 1 a 12 z (+) } | { z (+) } | {<br>dud↵ ⇤ 3 =  − � ����� ab 112 aa 2212���� � � = a | 11 b 2 aa 2212  − − {z ba 121 a 22 a 12} =? .<br>�� a 21 a 22�� ( − )<br>3<br>Manipulating the numerator, we have that du⇤<br>d↵ >  if and only iff:<br>a 12 > a 22<br>b 1 b 2<br><!-- End of picture text -->

We first note that both sides of this inequality are negative, it is convenient to write: 



_a_ 12 = _↵_ ( _φ_ 2 + _u_<sup>_⇤_</sup> 3<sup>_φ_12)+(2+</sup><sup>_u⇤_</sup> 2<sup>12) is the cross-partial marginal effect of defense.It says “how much more effective</sup> does defense become when an offense increases its fraction of 3’s. This terms gives the incentive for the defense to adjust into 3’s. _b_ 1 is the offense’s marginal shot value of a 3, as the usage curve gets steeper, this value falls. On the RHS, the numerator is a term, _↵u_<sup>_⇤_</sup> 3<sup>_φ_22+</sup><sup>_u⇤_</sup> 2<sup>22, that captures the concavity of the defense’s response function.</sup> The denominator captures the marginal impact of defense. If the above equation holds, the offense will take more 3’s when their preference for risk increases. This equation says this is more likely to occur when the defense has a concave adjustment function (they face strong diminishing returns to selective pressure), when the cross partial is low (the extra impact of guarding 3’s does not increase much with the offense’s 3-point usage) and when the usage curve of a 3-pointer relatively flat (raising the marginal value of a 3-pointer, which raises the denominator on the LHS). 

_Proof of Proposition 3_ 

Other comparative statics are directly implied by our constraints, 



which first does not appear signable, but can be rearranged to 





2013 Research Paper Competion Presented by: 



12 



where the middle term in the numerator can be signed by noting that _b_ 2 _<_ 0 and ( _φ_ 2 _a_ 11 _− φ_ 1 _a_ 12) = _φ_ 1 _φ_ 2(1 + 2 _u_<sup>_⇤_</sup> 3<sup>)</sup><sup>_>_0.</sup> 



follows by symmetry to the above calculation. 

### 6.3 Proofs for the baseline model 

_Proof of Proposition 1_ The only part of Proposition 1 not shown in the text is that the win value of 3’s must increase. We think intuition can be best scene through the lense of a classic economics setup. Consider a monopolist facing demand curve _P_ ( _q_ ) and an upward slope marginal cost curve _C_<sup>_00_</sup> ( _q_ ) _<_ 0. Imagine a subsidy from the government of so that for each dollar earned, the firm earns 1 + _x_ = _↵>_ 1 dollars. What the proposition states is that if the government offers subsidy _x_ , the price cannot fall by more than _x_ . 

This problem is isomorphic to our shot allocation problem because the downward sloping 2-point usage curve implies an increasing marginal opportunity cost of shooting 3’s. As I shoot more 3’s, I give up better and better 2-pointers. The first order condition of this problem is: 



Taking the total derivative, rearranging and multiplying by<sup>_d_</sup> _dq_<sup>_<u>p</u>_we get:</sup> 



We are interested in whether _p ⇤ ↵_ is greater than the orginal price, this amounts to whether: 



Plugging, in our condition becomes, is: 

Cross-multiplying and rearranging we have: 



where the second line follows because _qp_<sup>_00_</sup> ( _q_ ) + 2 _p_<sup>_0_</sup> ( _q_ ) _<_ 0 (marginal revenue is downward sloping). Canceling out and simplying, this equation reduces to: 



where _✏_ is the elasticity of demand. The last line must hold, otherwise the firm earns negative marginal revenue. 2013 Research Paper Competion Presented by: 





13 



### 6.4 Parametric model of win probability 

A game of NBA basketball has 48 minutes of game time, with ties being settled by a 5-minute overtime. Consider two teams, home ( _h_ ) and away ( _a_ ). Let _Sh,N_ and _Sa,N_ denote the current scores for the home and away team with _N_ offensive possessions (for each team) remaining in the game. Let _Ph,i_ and _Pa,i_ denote the number of points scored by the home/away team on the _i_<sup>_th_</sup> possession from the end of the game. The home team wins if it has more points at the end of the game, which we can express as: 



To model how teams generate points, let _{µh, σh_<sup>2</sup><sup>_}_and</sup><sup>_{µa, σ_</sup> _a_<sup>2</sup><sup>_}_representthemeanandvarianceofpointsper</sup> possession that each team is able to achieve in the match-up. If the number of remaining possessions, _N_ , is large, the central limit theorem gives the probability of the home team winning as: 



where Φ is the CDF of the standard normal distribution. Examining this expression, we see that an ability advantage ( _µ_ higher than opponent) matters proportional to the number of remaining possessions. Each factor’s marginal impact on winning the game is easily obtained by differentiating equation (8). The following expression gives the impact of a point scored for the home team on win probability: 



where lower-case _φ_ is the standard normal PDF. To estimate this equation, we first impute the number of remaining possessions using the team-specific paces-of-play in a given match-up and by adding one possession to the team currently holding the ball. Given the standard normal specification, it is natural to estimate equation (8) with Probit regression. The projections give the probability the home team will win at each of state of the game. Figure 1 Panel 1 shows these projections. 



2013 Research Paper Competion Presented by: 



14 


