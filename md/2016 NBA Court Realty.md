<!-- source: 2016 NBA Court Realty.pdf -->



# **NBA Court Realty** 

Dan Cervone, Luke Bornn and Kirk Goldsberry New York Unversity, Simon Fraser University, and University of Texas (Austin) 

## **1 Intro: the Basketball Court is a Real Estate Market** 

Continuously throughout every basketball possession, players control different regions of the basketball court. Some regions are more valuable than others, and players’ control (or lack thereof) of valuable court space dictates the �low and strategy of a basketball possession for both the offense and defense. As professionals engaged in high-stakes competition, we assume players are rational actors, and the exchanges they make to acquire new court space represent a winning strategy for their team. This simple assumption allows us to infer the value (price) of court real estate based on player and ball movement alone. 

In this paper, we provide a de�inition of court space ownership, and infer the value of court space using SportVu player location data. Spatial tracking data has enabled a recent paradigm shift in basketball analytics [4, 7, 1, 3]; we add to this growing literature by focusing on _space_ , itself, as the object of investigation. By modeling court space and court ownership, we reveal different valuable regions of the court among the NBA’s players and teams, and insightful new metrics for both offense and defense. For instance, we can measure ballcarriers’ off-ball impact on offense by calculating the value of the space freed up for their teammates to control. For analyzing defense, we can quantify how effectively different teams (and players) contain the offense (and particular players) within low-value regions of the court. 

## **2 Quantifying Court Ownership** 

Unlike traditional property investments, players do not “own” any court space in any objective sense. Heuristically, though, it is easy to imagine a player completely owning the point he is standing on, having no control of a point very far away, and having moderate control of a point nearby (say 5 feet away)—except perhaps if another player is even closer to that point. With this in mind, we introduce a “weighted Voronoi” concept for de�ining each player’s court space ownership at any point in time. 

We �irst divide the half-court into _M_ = 576 equally sized cells, approximately 2<sup>_′_</sup> _×_ 2<sup>_′_</sup> each. For player _i_ , _X_<sup>_i_</sup> ( _t_ ) is a _M_ -vector representing his investment (level of ownership) in each of the _M_ court cells at time _t_ . The _m_ th entry of _X_<sup>_i_</sup> ( _t_ ) is inversely proportional to the distance between player _i_ and court cell _m_ at time _t_ only if no other player is closer to court cell _m_ : 









2016 Research Papers Competition Presented by: 

1 



Thus, court real estate is partitioned among the players according to the Voronoi diagram of player locations, and within each segment they control, players’ investment in court space is inversely proportional to their distance from this space. Figure 1 illustrates this with a sample of our data. 

Voronoi diagrams have previously been used for modeling sports data [9, 2], and offer several advantages. In particular, an offensive player’s court ownership implicitly encodes information on the defensive positioning. When a defender closes on player _i_ , player _i_ ’s Voronoi partition decreases, meaning more entries in the court ownership vector _X_<sup>_i_</sup> ( _t_ ) are zero. Thus, regardless of the inferred court location prices, player _i_ ’s total real estate investment value decreases as he gets less open. Moreover, because of the weighting we use, this decrease is more dramatic when the defender is close, and negligible when a defender is far away, where even after approaching player _i_ he is still open. 





Figure 1: Example court space ownership map. A player’s control of each court cell in his Voronoi segment (left) is inversely proportional to his distance from that cell (right). 

## **3 Inferring Property Value** 

Like pricing in other �inancial markets, the value of NBA court property re�lects a medium of exchange. Higher value regions can be identi�ied if, based on players’ movement and actions, they seem preferred to other regions on the court. For instance, when a player controlling a huge chunk of backcourt space passes to a teammate controlling a tiny section in the paint, this suggests that court space in the paint is more valuable than in the backcourt. The idea of inferring value based solely on asset transactions is used by Romer [8] to infer the relative value of picks in the NFL draft; our conceptual approach to valuing NBA court realty is very similar. 

Passes between players offer clean, easily interpretable transactions of court real estate. However, unlike transactions in other markets, we don’t expect the exchanges in court space implied by passes to be fair—because players in the offense cooperate instead of compete, passes should bene�it the offense as a whole. Assuming players are generally rational decision-makers, when player _i_ passes to player _j_ , this suggests (disregarding player-speci�ic effects) player _j_ is in a more valuable position than player _i_ ; the team bene�its from investing (ball control) in player _i_ ’s space instead player _j_ ’s space. 



2016 Research Papers Competition Presented by: 



2 



To formalize property value inference, let _β_ be a _M_ -vector, with _βm_ the price/value of court cell _m_ . Thus, the total value of player _i_ ’s court real estate—his portfolio value—at time _t_ can be written 



To estimate _β_ given player position data and pass events, we maximize: 



where _i, j_ index players in the data, and _λ_ penalizes the _ℓ_ 2 norm of _β_ . The positivity constraints on _β_ , as well as the _ℓ_ 2 penalty, are not strictly necessary, yet they lead to more stable and interpretable performanceofthismodel. Withoutthe _ℓ_ 2 penalty, theobjectivefunction _Lλ_ ( _β_ ) isconstantforconstant shifts in _β_ , _β_ + _c_ ; thus, the constraints on _β_ in (3) ensure that the lowest values for court space cells are near 0. 

Our model (3) can be represented as a penalized logistic regression problem (or as a penalized Plackett-Luce model [6]), and easily �it using the `glmnet` package in `R` or similar software. Viewed as a logistic regression problem, the binary outcome is whether player _i_ passes to player _j_ , or vice versa. Thus, our estimation of _β_ guarantees that the most probable feasible passes are those with the greatest gain in court property value from the passer to the pass target. 

We choose _λ_ using cross-validation [5], which can also be used to evaluate the �it and predictive performance of our court space pricing model. Given the players involved in a pass, we predict the direction of the pass ( _i → j_ versus _j → i_ ) extremely well—we are sometimes over 99% sure of the pass direction, yet measured on out-of sample test data, we are not over�itting. 

### **3.1 Team-Speci�ic Property Values** 

If we �it (3) using passing data from each team separately, we estimate team-speci�ic court value surfaces _β_<sup>_k_</sup> , where _k_ indexes the 30 teams in the NBA. Plotting _β_<sup>_k_</sup> thus reveals how teams value different areas of the court differently. Figure 2 shows the league average _β_ , as well as the differences from the league average for three teams: Golden State, Houston, and the New York Knicks. 

The league-wide _β_ plot reveals that space is most valuable near the basket, and in the corner 3 areas. There is a signi�icant drop in value beyond 15 feet from the basket, before increasing again near the three point line (except in the middle of the court, where the value is low beyond the arc). Golden State’s court value map is not drastically different from the league average (remember that our estimation of court space value does not use any shooting information), though there is more value in the wing three areas. Houston and New York both under-value and over-value mid-range shots, respectively, though Houston strongly values the area just inside the corner 3 (though this could mean they particularly value their corner 3 players being wide open, as an unguarded player in the corner would control signi�icant space in front of him, as well). 

### **3.2 Player-Speci�ic Property Values** 

It is also possible to estimate player-speci�ic property values, analogous to the team-speci�ic parameters _β_<sup>_k_</sup> . To do this, we modify our objective function (3) to include player adjustments to the court 





2016 Research Papers Competition Presented by: 

3 











- Figure 2: Court space value ( _β_ ) plots for the 2014-15 NBA (left); and the difference ( _β_<sup>_k_</sup> _β_<sup>NBA</sup> ) from this surface for Golden State, Houston, and New York, from left to right. 

space value vectors _β_ . Speci�ically, letting 



where _i_ = 1 _, . . . , P_ indexes players, we maximize 



This remains equivalent to a penalized logistic regression model, except note that we apply a different penalty to the player-speci�ic deviations from _β_ ( _α_<sup>_i_</sup> ) than we do to _β_ itself. This makes sense—since _α_<sup>_i_</sup> represent offsets from _β_ , they should be closer to 0 than _β_ is. As with (3), we learn _λ_ 1 and _λ_ 2 using cross-validation, and �it this model (4) using data from each team separately (giving us a team-speci�ic _β_<sup>_k_</sup> instead of a generic _β_ ). 









Figure 3: The leftmost plot is the 2014-15 Golden State Warriors’ baseline property value plot ( _β_<sup>_k_</sup> ); shown beside (from left to right) it are the player-speci�ic court space value ( _α_<sup>_i_</sup> ) plots for Stephen Curry, Klay Thompson, and David Lee. 

Figure 3 shows the _α_<sup>_i_</sup> values for the 3 players on the Golden State Warriors, as estimated from their championship 2014-15 season. Relative to the rest of the team, Steph Curry and Klay Thompson both 



2016 Research Papers Competition Presented by: 



4 



have much higher court values around the three point line (particularly so for Thompson); David Lee’s court space, on the other hand, is more valuable closer to the basket. 

## **4 Property Value Derived Metrics** 

With estimates of court space prices, we can track the value of each player’s real estate portfolio throughout any basketball possession. Figure 4 provides a glimpse of this, showing the court space each player controls and its associated portfolio value, at several moments during a possession from our data. Doing so provides useful quanti�ications of player positioning and spacing at the same level of temporal resolution as the original data, allowing basketball analysts to correlate these metrics with other events of interest. Two brief examples are presented below. 











Figure 4: Example possession with each player’s court ownership and real estate portfolio value illustrated. Offensive players are red and defensive players blue (darker color represents higher property portfolio value). 

### **4.1 Ball Movement and Floor Spacing** 

Our court real estate model helps us quantify a player’s effect on ball movement and �loor spacing, two offensive features that—when executed well—ensure that players on the offense have higher total court real estate portfolio values. When this happens, either players are occupying more valuable regions, or simply being more open from the defense. To do this, we calculate the total portfolio of all players on the court when a particular player is in the lineup, versus when that player is removed. The top 10 and bottom 10 players by this metric are presented in Table 4.1. 

### **4.2 Defensive Suppression** 

Though court space value is inferred only using offensive players’ court ownership (during passes), our overall framework reveals valuable inferences about defensive spatial strategy. The weighted Voronoi court ownership de�inition implicitly values good defense, since when in valuable regions of the court, a player’s portfolio value will drop when he is closely defended. 

Expanding on this idea, we can calculate the average portfolio of an offensive player against each defensive team he faces, both while in control of the ball and not. Low portfolio values suggest that the player is either closely guarded when in valuable space, or mainly occupying low-value space—both of which suggest effective space suppression by the defense. In table 4.2, we present LeBron James’ 





2016 Research Papers Competition Presented by: 

5 



||Name|On-Court Team Portfolio Value|Off-Court Team Portfolio Value|
|---|---|---|---|
|1|Jae Crowder|10.90|9.70|
|2|Jordan Clarkson|8.39|7.35|
|3|Ryan Kelly|8.45|7.42|
|4|Marcus Smart|10.53|9.78|
|5|Brandon Bass|10.50|9.75|
|6|Wayne Ellington|8.13|7.44|
|7|Jonas Valanciunas|10.35|9.71|
|8|Evan Turner|10.36|9.79|
|9|Josh Smith|11.42|10.89|
|10|LaMarcus Aldridge|9.80|9.31|
||...|...|...|
|271|Kelly Olynyk|9.82|10.27|
|273|Lou Williams|9.82|10.29|
|275|Patrick Patterson|9.84|10.31|
|274|Jordan Hill|7.44|7.97|
|275|Ed Davis|7.40|7.99|
|276|Jared Sullinger|9.65|10.43|
|277|Kobe Bryant|6.63|8.25|
|278|Ronnie Price|6.38|8.21|
|279|Jeff Green|8.38|10.77|
|280|Rajon Rondo|8.02|10.56|



Table 1: On-court and off-court average team real estate portfolio values. Top 10 and Bottom 10 oncourt _−_ off-court differentials for 2014-15 are shown. 

average portfolio value while on-ball and off-ball, taken separately against each opponent. Lower portfolio value scores represent the opposing defense’s ability to contain LeBron in low value court space situations. 

## **5 Conclusion** 

This paper combines economic reasoning and large-scale spatial data modeling in a novel analysis of NBA team and player strategy. The spatial impact of players, or speci�ic offensive/defensive schemes thatemphasize controllingparticularregionsof thecourt, is an important basketballanalyticsproblem that has eluded quanti�ication. By inferring the value of NBA court real estate, we enable new metrics for spacing and positioning, and uncover new axes to measure variation in team strategy. 

## **6 Acknowledgements** 

The authors would like to thank Alex D’Amour, Alex Franks, Kirk Goldsberry, and Andrew Miller for numerous helpful conversations and ideas. DC would like to acknowledge �inancial support from the Moore-Sloan Data Science initiative. 





2016 Research Papers Competition Presented by: 

6 



||Team|On-ball Portfolio Value|On-ball Portfolio Value|
|---|---|---|---|
|1|Por|2.02|2.09|
|2|Was|1.96|2.22|
|3|NO|1.95|2.10|
|4|Atl|1.95|2.03|
|5|Den|1.95|2.11|
|6|LAC|1.92|2.00|
|7|Bos|1.92|2.04|
|8|OKC|1.91|1.94|
|9|Mem|1.90|2.04|
|10|GS|1.89|1.86|
||...|...|...|
|21|Ind|1.76|1.86|
|22|Hou|1.76|1.81|
|23|Dal|1.73|1.86|
|24|Phi|1.73|1.96|
|25|Orl|1.69|2.05|
|26|Mil|1.69|1.97|
|27|LAL|1.69|1.85|
|28|Det|1.67|1.88|
|29|SA|1.62|1.76|
|30|Pho|1.61|1.98|



Table 2: On-ball and off-ball portfolio values for LeBron James in 2014-15, by opponent. Lower values indicate more suppression. 

## **References** 

- [1] Dan Cervone, Alexander D’Amour, Luke Bornn, and Kirk Goldsberry. Pointwise: predicting points and valuing decisions in real time with nba optical tracking data. _Proceedings MIT Sloan Sports Analytics_ , 2014. 

- [2] So�ia Fonseca, João Milho, Bruno Travassos, and Duarte Araújo. Spatial dynamics of team sports exposed by voronoi diagrams. _Human movement science_ , 31(6):1652–1659, 2012. 

- [3] Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Counterpoints: Advanced defensive metrics for nba basketball. MIT Sloan Sports Analytics Conference. Boston, MA, 2015. 

- [4] Kirk Goldsberry. Courtvision: New visual and spatial analytics for the nba. In _2012 MIT Sloan Sports Analytics Conference_ , 2012. 

- [5] Gene H Golub, Michael Heath, and Grace Wahba. Generalized cross-validation as a method for choosing a good ridge parameter. _Technometrics_ , 21(2):215–223, 1979. 

- [6] John Guiver and Edward Snelson. Bayesian inference for plackett-luce ranking models. In _proceedings of the 26th annual international conference on machine learning_ , pages 377–384. ACM, 2009. 





2016 Research Papers Competition Presented by: 

7 



- [7] Rajiv Maheswaran, Yu-Han Chang, Aaron Henehan, and Samantha Danesis. Deconstructing the rebound with optical tracking data. In _The MIT Sloan Sports Analytics Conference. Boston_ , 2012. 

- [8] David Romer. Do �irms maximize? evidence from professional football. _Journal of Political Economy_ , 114(2):340–365, 2006. 

- [9] Stefan Schiffer, Alexander Ferrein, and Gerhard Lakemeyer. Qualitative world models for soccer robots. In _Qualitative Constraint Calculi, Workshop at KI_ , volume 2006, pages 3–14, 2006. 





2016 Research Papers Competition Presented by: 

8 


