<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Robust Rankings for College Football - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1405 

## Robust Rankings for College Football 

#### **Samuel Burer,** _University of Iowa_ 

©2012 American Statistical Association. All rights reserved. 

## Robust Rankings for College Football 

###### Samuel Burer 

###### **Abstract** 

We investigate the sensitivity of the Colley Matrix (CM) rankings---one of six computer rankings used by the Bowl Championship Series---to (hypothetical) changes in the outcomes of (actual) games. Specifically, we measure the shift in the rankings of the top 25 teams when the win-loss outcome of, say, a single game between two teams, each with winning percentages below 30%, is hypothetically switched. Using data from 2006--2011, we discover that the CM rankings are quite sensitive to such changes. To alleviate this sensitivity, we propose a robust variant of the rankings based on solving a mixed-integer nonlinear program, which requires about a minute of computation time. We then confirm empirically that our rankings are considerably more robust than the basic CM rankings. As far as we are aware, our study is the first explicit attempt to make football rankings robust. Furthermore, our methodology can be applied in other sports settings and can accommodate different concepts of robustness besides the specific one introduced here. 

###### **KEYWORDS:** rankings, college football, robust 

**Author Notes:** Department of Management Sciences, University of Iowa, Iowa City, IA, 52242-1994, USA. Email: samuel-burer@uiowa.edu. The research of this author was supported in part by NSF Grant CCF-0545514. 

Burer: Robust Rankings 

### **1 Introduction** 

College football has been played in the United States since the 1860s and enjoys enormous popularity today. Colleges and universities of all sizes across the country sponsor teams that play each year (or _season_ ) within numerous conferences and leagues. We focus our attention on teams in the Football Bowl Subdivision (FBS). Roughly speaking, the FBS includes the largest and most competitive collegiate football programs in the country. In 2011, there were 120 teams in the FBS, each of which typically played 12 games per season (not including post-season games). 

For historical reasons, the FBS teams do not organize themselves into an elimination tournament at the end of a season to determine the best team (or _national champion_ ). Instead, the most successful teams from the regular season are paired for a group of extra games, called _bowl games_ . In particular, every FBS team plays in at most one bowl game. Ostensibly, the bowl games serve to determine the national champion—especially if the bowl match ups are chosen well. However, there has always been considerable debate over how to choose the bowl match ups. 

Prior to the year 1998, the bowl match ups were made in a less formal manner than today. One of the most important factors for determining the match ups were the human-poll rankings, such as the AP Poll provided by the Associated Press. As a result, the poll rankings have long had considerable influence in college football. (Although computer-generated rankings existed at the time, they were not used with any consequence.) In fact, prior to 1998, the national champion was generally considered to be the team ranked highest in the polls after completion of the bowl games. However, even this simple rule was problematic because the final polls could disagree on the top-ranked team. This occurred, for example, after the 1990 season. 

Since 1998, the Bowl Championship Series (BCS) has been implemented to alleviate the ambiguity of determining the national champion in college football [1]. The BCS procedure is essentially as follows. At the end of the regular season, multiple human-poll and computer rankings are combined using a simple mathematical formula to determine a _BCS score_ for each FBS team. The FBS teams are then sorted according to BCS score, which determines the _BCS rankings_ . Then, following a set of pre-determined rules and policies, ten of the top teams according to the BCS rankings are matched into 5 bowl games. In particular, the top-2 teams are matched head-to-head in a single game, so that the winner of that game can reliably be called the national champion. 

Even with the BCS now in place, there is still considerable reliance on rankings (human and now also computer). It is clear that quality rankings are necessary for the BCS to function properly, i.e., to reliably setup the game that will determine the national champion and to setup other quality games. 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

However, it can be quite challenging to determine accurate rankings, especially in college football. Intuitively, good sports rankings are easy to determine when one has data on many head-to-head matchups, which allow the direct comparison of many pairs of teams. This happens, for example, in Major League Baseball, where many pairs of teams play each other often, and thus a team’s winning percentage is a good proxy for its ranking. In college football, the large number of teams and relatively short playing season makes such head-to-head information scarce. For example, for 120 FBS teams each playing 12 games against other FBS teams, only 720 games are played out of 7140 = �1202 � possible pairings. In reality, even less information is available because FBS teams often play non-FBS teams and because conference teams mainly play teams in the same conference (making it hard to compare across conferences). 

Nevertheless, there are many ranking systems for college football that perform well in practice. One such method, which is one of six computer rankings used by the BCS and which we will investigate in this paper, is the Colley Matrix (CM) method [12]. For a given schedule of games involving _n_ teams, this method sets up a system _Cr_ = _b_ of _n_ equations in _n_ unknowns, where the _n × n_ matrix _C_ depends only on the schedule of games and the _n_ -vector _b_ depends only on the win-loss outcomes of those games. In particular, _b_ does not depend in any way on the points scored in the games. The solution _r_ is called the _ratings vector_ , and it can be shown mathematically to be the unique solution of _Cr_ = _b_ . To determine the rankings of the _n_ teams, the entries of _r_ are sorted, with more positive entries of _r_ indicating better ranks. The CM method shares similarities with other ranking systems; see, for example, [17, 18, 14]. 

In this paper, we investigate whether computer ranking systems can be improved, and we focus in particular on improving the CM method. We do not mean to presume or imply that the CM method needs improvement while the other five BCS computer rankings do not, but the CM method is the only one of the six that is published fully in the open literature and hence can be systematically investigated [6]. 

We are especially interested in the robustness of the CM rankings, and our research was in part motivated by a situation that arose at the end of the 2010 regular season (i.e., immediately before the bowl match ups were to be determined): 

The final BCS ratings show LSU ranked 10th and Boise State 11th. But ...Wes Colley’s final rankings, as submitted to the BCS, were incorrect. The Appalachian State-Western Illinois FCS playoff game was missing from his data set ...the net result of that omission in Colley’s rankings is that LSU, which he ranked ninth, and his No. 10, Boise State, should 

2 

###### Burer: Robust Rankings 

be switched. Alabama and Nebraska, which he had 17th and 18th, would also be swapped. ...LSU and Boise State are so close in the overall BCS rankings (.0063) that this one error switches the order. Boise State should be 10th in the overall BCS rankings and LSU should be No. 11. [5] 

In other words, the CM rankings—and hence the BCS rankings—proved quite sensitive to the outcome (or rather, the omission) of a single game. Moreover, this game was played between two FCS (Football Championship Subdivision) teams, and FCS teams are generally considered to be much less competitive than the topranked FBS teams and play relatively few games against the FBS teams. 

We are also motivated by a recent work of Chartier et al. [9] that investigates the sensitivity of the Colley Matrix rankings (and other types of rankings) under perturbations to a hypothetical “perfect” season in which all teams play one another and the correct rankings are clear (i.e., the top team wins all its games, the second team beats all other teams except the top team, etc). In this specialized setting, the authors conclude that the Colley Matrix rankings are stable but also present a real-world example where the rankings are unstable. 

We propose that the top rankings provided by computer systems should be more robust against the outcomes of inconsequential games, that is, games between teams that should clearly not be top ranked. Of course, the top rankings should still be sensitive to important games played between top contenders or even to games played between one top contender and one non-contender. 

To this end, we develop a modification of the CM method that protects against modest (hypothetical) changes in the win-loss outcomes of (actual) inconsequential games. We do not handle the case of omitted games (as exemplified in the quote above) since, in principle, accidental omission can be prevented by more careful data handling. Rather, our goal is to devise a ranking system whose top rankings are stable even if a “far away,” inconsequential game happens to have a different outcome. This is our choice of what it means for rankings to be robust. While there certainly may be other valid definitions of robustness, we believe our approach addresses a limitation of computer rankings and could also be easily modified for other definitions. Our approach also depends on the definition of “inconsequential,” but this can be adjusted easily to the preferences of the user, too. We also remark that, since our approach considers only win-loss outcomes, it naturally incorporates other notions of robustness that strive to produce similar rankings even when a game’s point margin of victory is (hypothetically) perturbed. 

We stress our point of view that one should protect against _modest_ changes to the inconsequential games. As an entire collection, the inconsequential games are probably of great consequence to the top-ranked teams, and so we do not propose, 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

say, simply deleting the inconsequential games from consideration before calculating the rankings. Rather, our approach asks, “Suppose the outcomes of _just a few_ of the inconsequential games switched, but we do not necessarily know which ones. Can we devise a ranking that is robust to these hypothesized switches?” 

Our approach is derived from the fields of robust optimization [7] and robust systems of equations [13]. Ultimately, this leads to a mixed-integer nonlinear programming (MINLP) model, which serves as the robust version of the system _Cr_ = _b_ . Solving this MINLP provides a robust ratings vector _r_ , which is then sorted to obtain the final robust rankings just as in the CM method. We remark that there exist other ranking methods that utilize optimization; see, for example, [10, 11, 15]. 

Our method depends on a user-supplied integer Γ _≥_ 0, which is the number of switched inconsequential games to protect against. In this way, the parameter Γ signifies the conservatism of the user, mimicking the robust approach of [8]. For example, if the user is not worried about inconsequential games affecting the top rankings at all, then he/she can simply set Γ = 0 (protect against no games changing), and then the ratings vector _r_ is simply the usual CM ratings. On the other hand, choosing Γ = 10 means the user wants robust rankings that take into account the possibility that up to 10 inconsequential games happen to switch. It should be pointed out that there is no best _a priori_ choice of Γ; rather, it will usually depend on the user’s experience and conservatism. 

It is important to point out that our approach is not stochastic. For example, we do not make any assumptions about the distributions of switched inconsequential games, and we do not study average rankings. Rather, we calculate a single set of rankings that intelligently takes into account the possibility of Γ switched games— but without knowing anything else about the switched games. This is characteristic of robust optimization approaches, which differentiates them from stochastic ones. 

This paper is organized as follows. Section 2 reviews the CM method and discusses the data we use in the paper. We also describe our focus on FBS rankings even though our data contains non-FBS data as well. Section 3 then empirically investigates the sensitivity of the top rankings in the CM method to modest changes in the win-loss outcomes of games between teams with losing records. In Section 4, we propose and study the MINLP, which we solve to make the CM method robust to modest changes in the data. In Section 5, we provide several examples and repeat the experiments of Section 3 except with our own robust rankings. We conclude that our rankings are significantly less sensitive than the CM rankings. Finally, we conclude the paper with a few final thoughts in Section 6. 

4 

Burer: Robust Rankings 

### **2 The Colley Matrix Method and Our Data** 

Colley proposed the following method for ranking teams, called the Colley Matrix (CM) method [12]. The CM method uses only win-loss information (as required by the BCS system) and automatically adjusts for the quality of a team’s opponent (also called the team’s _strength of schedule_ ). We refer the reader to Colley’s paper for a full description; we only summarize it here. 

Let [ _n_ ] := _{_ 1 _, . . . , n}_ be a set of teams, which have played a collection of games in pairs such that each game has resulted in a winner and a loser (i.e., no ties). Define the matrix _W ∈ℜ_<sup>_n×n_</sup> via 



In particular, _Wij_ = _Wji_ = 0 if _i_ has not played _j_ , and _Wii_ = 0 for all _i_ . Note that _ij_ -th entry of _W_ + _W_<sup>_T_</sup> encodes the number of times that _i_ and _j_ have played each other, and letting _e_ be the all-ones vector, the _i_ -th entries of ( _W_ + _W_<sup>_T_</sup> ) _e_ and ( _W − W_<sup>_T_</sup> ) _e_ give the total number of games played by _i_ and its win-loss spread, respectively. With _I_ the identity matrix, also define 



where Diag( _·_ ) places its vector argument into a diagonal matrix. Colley shows that _C_ is diagonally dominant and hence positive definite, which implies in particular that _C_<sup>_−_1</sup> exists. He then defines the _ratings vector r_ to be the unique solution of the linear system 



or equivalently, _r_ := _C_<sup>_−_1</sup> _b_ . Then Colley sorts _r_ in descending order, i.e., determines a permutation _π_ of [ _n_ ] such that the vector ( _rπ_ 1 _, . . . , rπn_ )<sup>_T_</sup> is sorted in descending order. Then the _rankings vector_ is precisely _π_ ; that is, the ranking of team _i_ is _πi_ . If any of _r_ ’s entries are equal, one can easily adjust the rankings to exhibit ties, but this is unlikely to occur in practice. In the following section, we will provide a specific example of the CM rankings. 

We now discuss the data used throughout the paper. We downloaded football data from the website [4] for the 2006–2011 regular seasons. (This website appears to be an archive of Wolfe’s website [3].) In particular, no post-season data is included. For each regular season, the data contains the outcomes of all college football games played in the United States, but we limit our focus to just FBS teams. For example, consider the 2010 college football season, which included 3,960 games played between 730 teams around the country. Of the 730 teams, 120 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

were FBS teams, and of the 3,960 games, 772 involved at least one FBS team. We focus our attention on these 772 games since they contain all data directly related to FBS teams. In the case of 2010, these 772 games yield _n_ = 195 because the FBS teams played 75 outside teams. Throughout this paper, ratings will be done for all _n_ teams in a given season, but only ratings and rankings for FBS teams will be discussed since our interest is in ranking these teams. Specifically, we will rate all _n_ teams using the vector _r_ , but prior to computing the FBS rankings, we will delete the non-FBS teams from _r_ before sorting and ranking. In this way, the FBS rankings are computed using all available FBS data, but we focus our rankings on just the FBS teams. (Colley handles non-FBS teams in a more involved pre-processing step, but he likewise maintains a focus on FBS teams [2].) 

### **3 Sensitivity of the Colley Matrix Method** 

In this section, we empirically investigate the sensitivity of the Colley Matrix (CM) rankings to modest changes in the win-loss outcomes of “inconsequential” games. We specifically focus on the sensitivity of the rankings of the top teams. 

Given the win matrix _W_ , let _π_ be the permutation vector encoding the CM rankings for _W_ . Given an integer _t ∈_ [ _n_ ], define 



to be the index set of the top _t_ teams (ranks between 1 and _t_ ). In contrast, let _ω ∈_ [0 _,_ 1] be given and define 



to be the bottom teams (winning percentages less than _ω_ ). As long as _t_ is relatively small and _ω_ is relatively close to 0, it is highly likely that _T_ and _B_ are disjoint. For example, in all experiments, we take _t_ = 25 and _ω_ = 0 _._ 3 and find that, for the years 2006–2011, _T_ and _B_ never intersect. Note that _B_ does not depend on the rankings _π_ , whereas _T_ does. We call a game _inconsequential_ if it has occurred between two bottom teams _i, j ∈ B_ , and we define 



to be the set of all pairs playing inconsequential games. Note that, to remove redundancy, ( _i, j_ ) _∈I_ implies _i < j_ by definition. 

We wish to examine the sensitivity of the CM rankings of teams in _T_ to modest changes in the win-loss outcomes of games between pairs ( _i, j_ ) _∈I_ . For 

6 

###### Burer: Robust Rankings 

this, we define perturbations _W_<sup>_′_</sup> := _W_ + ∆ of the win matrix _W_ that switch the outcomes of a few inconsequential games. Formally, define 



The condition ∆ _ij_ = ∆ _ji_ = 0 for all ( _i, j_ ) _̸ ∈I_ guarantees that only inconsequential games are switched, and the equations ∆ _ij_ + ∆ _ji_ = 0 for all ( _i, j_ ) _∈I_ ensure that any switch is mathematically consistent between ( _i, j_ ) and ( _j, i_ ). For example, if we wish to switch a game having _Wij_ = 0 and _Wji_ = 1, then we need to perturb _Wij_ by +1 and _Wji_ by _−_ 1. Finally, the inequalities _−Wij ≤_ ∆ _ij ≤ Wji_ limit the number of switched games for ( _i, j_ ) _∈I_ . For example, in case _Wij_ = 1 and _Wji_ = 2, it is clear that we logically need _−Wij_ = _−_ 1 _≤_ ∆ _ij ≤_ 2 = _Wji_ . 

We also define a convenient restriction of _D_ . Given ∆ _∈D_ , the quantity � _i<j_<sup>_|_∆</sup><sup>_ij|_equals the number of games switched by ∆. For any integer limit</sup><sup>_L ≥_0,</sup> 



to be those perturbations that switch no more than _L_ inconsequential games. For example, _D_ (0) = _{_ 0 _}_ , and _D_ (1) consists of all perturbations changing exactly 1 or 0 games. Letting _N_ :=<sup>�</sup> ( _i,j_ ) _∈I_<sup>(</sup><sup>_Wij_+</sup><sup>_Wji_),onecanseethatthenumberof</sup> perturbations in _D_ ( _L_ ) equals<sup>�</sup><sup>_L_</sup> _ℓ_ =0 � _Nℓ_ �. For any ∆ _∈D_ , define _W_<sup>_′_</sup> := _W_ + ∆ and consider the CM rankings _π_<sup>_′_</sup> based on _W_<sup>_′_</sup> . We investigate the differences between the rankings _π_ and _π_<sup>_′_</sup> of the teams in _T_ via the measure 



Alternatively, _δ_ ( _W, W_<sup>_′_</sup> ) is the 1-norm of the sub-vector indexed by _T_ of the difference _π − π_<sup>_′_</sup> . We call _δ_ ( _W, W_<sup>_′_</sup> ) the _switch measure_ . For example, if the top 2 teams switch places but no other ranks change, then _δ_ ( _W, W_<sup>_′_</sup> ) = 2; if the first and third teams switch places but no other ranks change, then the switch measure is 4; and if the top team drops to fourth place but otherwise the orderings remain the same, then _δ_ ( _W, W_<sup>_′_</sup> ) = 6. If all teams in _T_ remain in the top _t_ of _π_<sup>_′_</sup> , then _δ_ ( _W, W_<sup>_′_</sup> ) is an even number, but it can be odd if some team drops out of the top _t_ . 

For each football year _y_ = 2006 _, . . . ,_ 2011 and each _L_ = 1 _,_ 2, we examine the distribution of switch measures 



7 

_Submission to Journal of Quantitative Analysis in Sports_ 

where _t_ = 25 and _ω_ = 0 _._ 3. This involves enumerating all ∆ _∈D_ ( _L_ ) and calculating _δ_ ( _W, W_<sup>_′_</sup> ) for each. Computationally, calculating _δ_ ( _W, W_<sup>_′_</sup> ) is quick, and enumeration of each ∆ _∈D_ ( _L_ ) is reasonable for _L ≤_ 2. 

It turns out that, with _L_ fixed, the distributions _H_ ( _L, y_ ) of the switch measure behave similarly irrespective of the year _y_ , and so to save space, we merge _H_ ( _L,_ 2006),..., _H_ ( _L,_ 2011) into a single histogram for each _L_ = 1 _,_ 2. The resulting two histograms are shown in Figure 1 with basic summary statistics. 



<!-- Start of picture text -->
One Game Switched (L=1)<br>50%<br>40% mean = 5.1<br>median = 4<br>30% min = 0<br>max = 20<br>20% stdev = 4.9<br>10%<br>0%<br>0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30<br>Switch Measure<br>Two Games Switched (L=2)<br>50%<br>40% mean = 6.5<br>median = 4<br>30% min = 0<br>max = 28<br>20% stdev = 6.3<br>10%<br>0%<br>0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30<br>Switch Measure<br>Frequency<br>Frequency<br><!-- End of picture text -->

Figure 1: Histograms for the switch measure _δ_ ( _W, W_<sup>_′_</sup> ) for _L_ = 1 _,_ 2 switched games, each over the years 2006–2011. This illustrates the sensitivity of the Colley Matrix rankings of the top teams to modest changes in the win-loss outcomes of inconsequential games. 

One can see from Figure 1 that the CM rankings of the top _t_ = 25 teams 

8 

###### Burer: Robust Rankings 

are quite sensitive to changes in just a few inconsequential games. For _L_ = 1, the mean of _δ_ ( _W, W_<sup>_′_</sup> ) is 5.1, and the maximum (or worst case) is 20, and both of these statistics increase noticeably for _L_ = 2. The standard deviation is also relatively large and increases between _L_ = 1 and _L_ = 2. In our opinion, such sensitivity is an undesirable property of the CM rankings, especially since rankings are relied upon so heavily in college football. 

In Table 1, we provide an illustrative (albeit worst-case) example of how the CM rankings can change when the outcome of a single inconsequential game is switched. The first column of teams contains the top-25 CM rankings for 2007. These teams comprise _T_ in our experiments. The second column shows the perturbed rankings when the result of the inconsequential game between Marshall and Rice is switched. Note that, in 2007, both Marshall and Rice had winning percentages below 30%, and Marshall beat Rice in real life. In both columns, a bold typeface indicates a ranking that changes. For this example, _δ_ ( _W, W_<sup>_′_</sup> ) = 20, and one can see quite plainly that there is a significant amount of shuffling in the rankings. Some of the shuffling is logical. For example, West Virginia beat Marshall in real-life, and when Marshall loses to Rice hypothetically, West Virginia then becomes a weaker team with a lower ranking. What is unclear, however, is why West Virginia drops four spots, which in our opinion seems excessive. 

|1|**Virginia Tech**|**LSU**|
|---|---|---|
|2|**LSU**|**Virginia Tech**|
|3|Missouri|Missouri|
|4|**Ohio State**|**Georgia**|
|5|**Georgia**|**Ohio State**|
|6|Oklahoma|Oklahoma|
|7|**West Virginia**|**Florida**|
|8|**Florida**|**Hawaii**|
|9|**Hawaii**|**Kansas**|
|10|**Kansas**|**Arizona St**|
|11|**Arizona St**|**West Virginia**|
|12|Boston College|Boston College|
|13|Southern Cal|Southern Cal|
|14|South Florida|South Florida|
|15|Clemson|Clemson|
|16|Brigham Young|Brigham Young|
|17|Illinois|Illinois|
|18|Tennessee|Tennessee|
|19|**Cincinnati**|**Virginia**|
|20|**Virginia**|**Cincinnati**|
|21|**Connecticut**|**Auburn**|
|22|**Auburn**|**Connecticut**|
|23|**Wisconsin**|**Texas**|
|24|**Oregon**|**Wisconsin**|
|25|**Texas**|**Oregon**|



Table 1: Comparison of the 2007 Colley Matrix rankings before (left) and after (right) the result of the inconsequential game between Marshall and Rice is switched. 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **4 The Robust Method** 

The basic idea of our robust method is to calculate a ratings vector _r_ that works well even if the win matrix is modestly perturbed from its real-life value _W_ . Robust rankings will then be determined by sorting _r_ in descending order just as with the regular Colley Matrix (CM) method. We call our method the _Colley Matrix Plus_ (CM+) method. 

Recall the CM system of equations _Cr_ = _b_ for the win matrix _W_ . For a user-specified integer Γ _≥_ 0, we consider perturbations _W_<sup>_′_</sup> := _W_ + ∆ for ∆ _∈ D_ (Γ) as introduced in the preceding section, and we analyze the perturbed system _C_<sup>_′_</sup> _r_ = _b_<sup>_′_</sup> for _W_<sup>_′_</sup> , where _C_<sup>_′_</sup> and _b_<sup>_′_</sup> are given by (1)–(2) except that _W_<sup>_′_</sup> takes the place of _W_ . (Note that Γ plays essentially the same role as _L_ in Section 3, but we will actually use the two parameters Γ and _L_ in slightly different ways for our experiments in Section 5. To facilitate the discussion therein, we introduce and use Γ in this section.) Using properties of ∆, it holds that ∆+ ∆<sup>_T_</sup> = 0, which implies 



i.e., the perturbation ∆ does not alter the matrix _C_ . This makes sense because _C_ depends only on the schedule of games, which is not changed by ∆. On the other hand, it holds that 



and so _b_<sup>_′_</sup> changes linearly with ∆. In total, we are faced with perturbed systems _Cr_ = _b_<sup>_′_</sup> , where ∆ ranges over _D_ (Γ). 

Because _C_ is invertible, there is clearly no single _r_ that solves _Cr_ = _b_<sup>_′_</sup> for all ∆ _∈D_ (Γ) except in the special case when Γ equals 0. A standard idea from robust optimization and the study of robust systems of equations is to search for an _r_ that minimizes the worst-possible violation of _Cr_ = _b_<sup>_′_</sup> over all ∆ _∈D_ (Γ), i.e., to solve the optimization problem 



where _∥· ∥p_ is a user-specified vector _p_ -norm. It is not immediately clear that (4) can be solved in a tractable manner (either practically or theoretically). We focus on the case _p_ = 2<sup>1</sup> and argue next that, even though (4) is a mixed-integer nonlinear 

1 In the first version of this paper, we focused on the case _p_ = _∞_ for which (4) can be solved as a 

10 

###### Burer: Robust Rankings 

program that appears to be NP-hard, we can devise an exact solution procedure that works well in practice (at least for relatively small numbers of inconsequential games and relatively small values of Γ). 

So fix _p_ = 2. We first transform (4) by minimizing the maximum squared norm and separating the objective function via (3): 



By introducing an auxiliary variable _t_ , we can rewrite the inner maximization using a set of explicit linear constraints: 



It is important to note that ∆ is no longer a variable. Rather, there is one linear constraint in ( _r, t_ ) for each specific ∆<sup>¯</sup> _∈D_ (Γ). As such, (6) is a strictly convex quadratic program with a unique optimal solution that can in principle be solved by CPLEX, for example. 

There is still one challenge, however. Since _D_ (Γ) contains<sup>�Γ</sup> _γ_ =0 � _N_ Γ� elements, where _N_ is the total number of inconsequential games, for most combinations of _N_ and Γ we cannot simply list and solve over all linear constraints; the number of such constraints is simply too large. So instead we adopt the following strategy. First, we solve (6) over a limited subset of constraints to generate an approximate solution (¯ _r, t_<sup>¯</sup> ) of (6). Then we solve the following subproblem over the variable ∆: 



Let ∆<sup>¯</sup> be an optimal solution. If the optimal value of the subproblem is positive, then we have determined a violated constraint of (6), and this constraint is added to the approximate model and the process is repeated. On the other hand, if the optimal value is nonnegative, then we have proved that the current (¯ _r, t_<sup>¯</sup> ) is optimal for (6), and hence ¯ _r_ is the robust ratings vector. 

Solving the subproblem for ∆<sup>¯</sup> is actually a difficult problem in theory, but CPLEX is able to solve it quickly as long as _N_ and Γ are not too large. In all instances of this paper, solving (4) via (6) and the procedure just outlined requires 

polynomial-time LP. However, in this case, there were many alternative optima _r_ , which introduced considerable ambiguity in the resultant rankings. We thank the anonymous referees for suggesting and encouraging a switch to a different _p_ -norm. 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

less than a minute using CPLEX 12.2 [16] within Matlab R2010b [19] on an Intel Core 2 Quad CPU running at 2.4 GHz with 4 GB RAM under the Linux operating system. However, larger values of _N_ and Γ may lead to solve times that take a few minutes or even a few hours. 

### **5 Behavior of the Robust Method** 

In this section, we examine the behavior of our Colley Matrix Plus (CM+) method in practice on the football data from 2006–2011. 

##### **5.1 Variation as** Γ **increases** 

Figure 2 presents the top-25 CM+ rankings for the 2008 football season for eleven choices of Γ: Γ = 0 _,_ 1 _, . . . ,_ 10. Note that Γ = 0 yields the regular CM rankings (though keep in mind that these do not necessarily match the rankings on Colley’s website [12] due to our different handling of non-FBS data as mentioned at the end of Section 2). The figure includes both a text table and a graphical chart. Each line in the chart depicts the rank trend of a particular team. For example, Oklahoma is ranked 1 for all Γ, and this corresponds to the top-most, flat line. In contrast, the rank line for Virginia Tech starts at 18 and ends at 16. 

When examining Figure 2 on its own, it is difficult to make and support claims such as: “The rankings for Γ = 8 are _better_ than the rankings for Γ = 3.” Of course, we would say that Γ = 8 is more robust than Γ = 3 by construction (and we investigate this empirically in the next subsection), but in the absence of further analysis, we believe it can be challenging to compare _any_ two rankings objectively. So here we would simply like to point out some observations that we believe are relevant concerning the robust rankings as Γ changes. 

First, as Γ increases, the rankings are sensible compared to Γ = 0. For example, we do not see teams making huge jumps in the rankings. In fact, the ranking of each team moves by at most two positions over all Γ _≤_ 10. 

Second, the changes in the rankings appear to involve several separate groups of closely ranked teams, and each group switches ranks among itself only. For example, Utah and Texas Tech switch places, while Brigham Young, Missouri, and North Carolina adjust to accommodate a decline in the rank of Brigham Young. Two additional groups are Oklahoma St/Florida St/Virginia Tech and Michigan St/Ball St/Boston College. 

Third, the rank trends are not necessarily monotonic, i.e., a team’s rank can increase and then decrease (or decrease and then increase) as Γ increases. However, 

12 

###### Burer: Robust Rankings 

|Rank|Γ = 0<br>Γ = 1|Γ = 2|Γ = 3_,_4_,_5|Γ = 6|Γ = 7_,_8_,_9_,_10|
|---|---|---|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24|Oklahoma<br>Oklahoma<br>Florida<br>Florida<br>Texas<br>Texas<br>Utah<br>Texas Tech<br>Texas Tech<br>Utah<br>Alabama<br>Alabama<br>Penn State<br>Penn State<br>Boise St<br>Boise St<br>Southern Cal<br>Southern Cal<br>Ohio State<br>Ohio State<br>Cincinnati<br>Cincinnati<br>Georgia Tech<br>Georgia Tech<br>Georgia<br>Georgia<br>TCU<br>TCU<br>Pittsburgh<br>Pittsburgh<br>Oklahoma St<br>Oklahoma St<br>Florida St<br>Florida St<br>Virginia Tech<br>Virginia Tech<br>Michigan St<br>Michigan St<br>Ball St<br>Ball St<br>Boston College<br>Boston College<br>Brigham Young<br>Brigham Young<br>Missouri<br>Missouri<br>North Carolina<br>North Carolina|Oklahoma<br>Florida<br>Texas<br>Texas Tech<br>Utah<br>Alabama<br>Penn State<br>Boise St<br>Southern Cal<br>Ohio State<br>Cincinnati<br>Georgia Tech<br>Georgia<br>TCU<br>Pittsburgh<br>Oklahoma St<br>Florida St<br>Virginia Tech<br>Ball St<br>Michigan St<br>Boston College<br>Brigham Young<br>Missouri<br>North Carolina|Oklahoma<br>Florida<br>Texas<br>Texas Tech<br>Utah<br>Alabama<br>Penn State<br>Boise St<br>Southern Cal<br>Ohio State<br>Cincinnati<br>Georgia Tech<br>Georgia<br>TCU<br>Pittsburgh<br>Oklahoma St<br>Florida St<br>Virginia Tech<br>Michigan St<br>Ball St<br>Boston College<br>Missouri<br>Brigham Young<br>North Carolina|Oklahoma<br>Florida<br>Texas<br>Texas Tech<br>Utah<br>Alabama<br>Penn State<br>Boise St<br>Southern Cal<br>Ohio State<br>Cincinnati<br>Georgia Tech<br>Georgia<br>TCU<br>Pittsburgh<br>Oklahoma St<br>Florida St<br>Virginia Tech<br>Ball St<br>Michigan St<br>Boston College<br>Missouri<br>Brigham Young<br>North Carolina|Oklahoma<br>Florida<br>Texas<br>Texas Tech<br>Utah<br>Alabama<br>Penn State<br>Boise St<br>Southern Cal<br>Ohio State<br>Cincinnati<br>Georgia Tech<br>Georgia<br>TCU<br>Pittsburgh<br>Virginia Tech<br>Florida St<br>Oklahoma St<br>Ball St<br>Boston College<br>Michigan St<br>Missouri<br>North Carolina<br>Brigham Young|
|25|Nebraska<br>Nebraska|Nebraska|Nebraska|Nebraska|Nebraska|
||0<br>5<br>10|||||
||15<br>Rank|||||
||20|||||
||25|||||
||1|3<br>5<br>Γ|7|9||



Figure 2: Colley Matrix Plus rankings with 0 _≤_ Γ _≤_ 10 for the 2008 football season. Note that Γ = 0 yields the regular CM rankings (though these do not necessarily match the rankings on Colley’s website [12] due to the different handling of non-FBS data as described at the end of Section 2). 

13 

_Submission to Journal of Quantitative Analysis in Sports_ 

the ranks appear to stabilize for larger Γ. For Figure 2, in particular, all ranks are stable for 7 _≤_ Γ _≤_ 10. 

Finally, the Γ-rankings confirm the robustness of the top-3 teams since they each retain their rank as Γ increases. This could be interpreted as an affirmation of the CM rankings (Γ = 0) for these top teams in 2008. In a similar manner, the top-15 CM rankings are confirmed to be mostly robust (with the exception of Utah and Texas Tech). 

In Figure 3, we show similar charts for the remaining years 2006–07 and 2009–2011. These depict very similar trends as 2008. 

##### **5.2 Sensitivity of the robust rankings** 

In Section 3, we investigated the sensitivity of the CM method when the rankings are recalculated after _L_ games are manually switched. We now conduct the same experiment except this time with our robust rankings. Our goal is to verify that our rankings are indeed less sensitive than the CM rankings, at least for certain values of Γ. 

In this section, it is important to keep in mind the different roles played by _L_ and Γ. The parameter _L_ determines the number of games that switch before recalculating the robust rankings, whereas Γ is the user-supplied parameter that controls the conservatism of the rankings. In particular, the two parameters are set independently. 

We first describe two important properties of the robust rankings that typify extreme cases. First, when Γ = 0, the robust rankings are clearly as sensitive as the CM rankings since they are exactly the CM rankings. Second, we claim that, when Γ is sufficiently large, the robust rankings are completely insensitive to _L_ switches. Said differently, for very large Γ, the Γ-robust rankings cannot change upon recalculation after any number of manual switches. To see this, let the win matrix _W_ be given, and suppose Γ _≥ N_ , where _N_ :=<sup>�</sup> ( _i,j_ ) _∈I_<sup>(</sup><sup>_Wij_+</sup><sup>_Wji_) is the</sup> total number of inconsequential games. Then the Γ-robust rankings _π_ based on _W_ take into account the possibility that _all_ inconsequential games might switch. Next, let _W_<sup>_′_</sup> = _W_ + ∆ be any perturbed win matrix with ∆ _∈D_ ( _L_ ), and calculate the robust Γ-rankings _π_<sup>_′_</sup> based on _W_<sup>_′_</sup> . Because _π_<sup>_′_</sup> is also calculated allowing that all games might switch, it must hold that _π_ = _π_<sup>_′_</sup> . More precisely, the set of scenarios _b_<sup>_′_</sup> optimized over in problem (4) is the same for both _W_ and _W_<sup>_′_</sup> because Γ is so large, and so _π_ = _π_<sup>_′_</sup> . 

Between the two extremes Γ = 0 (as sensitive as CM) and Γ _≥ N_ (completely insensitive), it is reasonable to expect the Γ-rankings will become less sensitive as Γ increases, and we now exhibit this at the intermediate, fixed value of Γ = 5. So let _π_ be the Γ-robust rankings determined by the original _W_ , and let _T_ 

14 

###### Burer: Robust Rankings 



<!-- Start of picture text -->
0 0<br>5 5<br>10 10<br>15 15<br>20 20<br>25 25<br>1 3 5 7 9 1 3 5 7 9<br>(a) 2006 (b) 2007<br>0 0<br>5 5<br>10 10<br>15 15<br>20 20<br>25 25<br>1 3 5 7 9 1 3 5 7 9<br>(c) 2009 (d) 2010<br>0<br>5<br>10<br>15<br>20<br>25<br>1 3 5 7 9<br>(e) 2011<br><!-- End of picture text -->

Figure 3: Colley Matrix Plus rankings versus Γ for all years except 2008. 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

be the index of the top _t_ = 25 teams under _π_ . Also let _π_<sup>_′_</sup> be the Γ-robust rankings determined by _W_<sup>_′_</sup> := _W_ + ∆, where ∆ _∈D_ ( _L_ ) for some _L_ . As in Section 3, we investigate the distributions of the top-team switch measures 



for each football year _y_ = 2006 _, . . . ,_ 2011 and each _L_ = 1 _,_ 2. As in Section 3, we then actually combine _H_ ( _L,_ 2006),..., _H_ ( _L,_ 2011) into a single histogram for each _L_ , the results of which are shown in Figure 4. 

One Game Switched (L=1) for Γ=5 



<!-- Start of picture text -->
50%<br>40% mean = 1.8<br>median= 0<br>30% min = 0<br>max = 10<br>20% stdev = 2.4<br>10%<br>0%<br>0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30<br>Switch Measure<br>Two Games Switched (L=2) for Γ=5<br>50%<br>40% mean = 2.5<br>median= 2<br>30% min = 0<br>max = 14<br>20% stdev = 2.8<br>10%<br>0%<br>0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30<br>Switch Measure<br>Frequency<br>Frequency<br><!-- End of picture text -->

Figure 4: Histograms illustrating the sensitivity of the CM+ rankings of the top teams to modest changes in the win-loss outcomes of inconsequential games. 

We can compare Figure 4 directly with Figure 1 of Section 3. Note in partic- 

16 

###### Burer: Robust Rankings 

ular that all histograms are plotted on the same scale. Looking at both the plots and summary statistics, we see very clearly that the distributions in Figure 4 are considerably lower than those in Figure 1. This demonstrates that, indeed, our CM+ rankings are less sensitive than the CM rankings under the same number of switches ( _L_ = 1 or _L_ = 2), and higher values of Γ will further stabilize the robust rankings. 

We conduct one last set of experiments to compare directly the sensitivity of the CM and CM+ rankings. Again, we fix Γ = 5 and take _L_ = 1 _,_ 2. For each _L_ , the histogram corresponding to _L_ in Figure 4 is based on all possible switches of _L_ games. For each of these same switches, we also calculate the switch measure for the regular CM rankings just as in Section 3. In Figure 5, we then plot the point ( _x, y_ ), where _x_ is the CM switch measure for that instance and _y_ is the CM+ switch measure for the same instance. Then, over all switches, to show the frequency for various ( _x, y_ ) pairs, we use a bubble chart, where the area of a bubble is proportional to the frequency of its ( _x, y_ ) center. Please also note that the line “ _x_ = _y_ ” is plotted for reference. 



<!-- Start of picture text -->
L=1 for Γ=5 L=2 for Γ=5<br>25 25<br>20 20<br>15 15<br>10 10<br>5 5<br>0 0<br>0 10 20 0 10 20<br>Colley Switch Measure Colley Switch Measure<br>Robust Switch Measure Robust Switch Measure<br><!-- End of picture text -->

Figure 5: Bubble plots of CM+ versus CM switch measures. CM+ has Γ = 5 in both plots. Also, _L_ = 1 _,_ 2, and the instances are all switches of _L_ inconsequential games. The line “ _x_ = _y_ ” is plotted for reference. 

Figure 5 shows clearly that the CM+ rankings are much less sensitive than the CM rankings on the same instances. Specifically, the fact that most bubbles are below the _x_ = _y_ line illustrates that, on any given instance, the switch measure for CM+ is less than that of CM. We also note that the CM+ rankings are particularly successful at lessening the sensitivity of the worst-case switch measures for CM 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

(approximately 15–20 for _L_ = 1 and 20–25 for _L_ = 2). 

### **6 Conclusion** 

In recent years, the desire to develop robust analytical models has emerged in many fields, including finance, medicine, and transportation, and we believe that computer sports rankings can also benefit from increased robustness. This paper has introduced a particular concept of robustness for college football rankings via the Colley Matrix method. Through experimentation, we have shown that our concept of robustness is consistent and more robust to modest changes in the data. In addition, the time needed to compute the robust rankings (typically less than a minute) is not an obstacle since rankings would be recalculated about once per week in practice. 

Our approach can be extended in a number of ways. First, just as the Colley Matrix method can be applied to many sports beyond football, so can ours. This opens the way to robust basketball rankings, chess rankings, etc. In addition, our notion of robustness can be modified to the user’s liking. For example, simple changes could be to alter the parameter _ω ∈_ [0 _,_ 1] (the winning percentage defining the bottom teams) or to include FCS games in the inconsequential set _I_ . One could also manually choose a completely different inconsequential set _I_ ; the analysis and the methodology of the paper will go through unchanged. For example, one may wish to protect the rankings against games that were very close, e.g., where the winner was determined by less than 3 points. _I_ could then be constructed to contain just pairs of close games. 

### **References** 

- [1] Bowl Championship Series Official Website. http://www.bcsfootball.org/ . Accessed October 4, 2011. 

- [2] FCS Grouping System. http://colleyrankings.com/iaagroups.html. Accessed October 4, 2011. 

- [3] Peter wolfe’s college football website. http://prwolfe.bol.ucla.edu/cfootball/. Accessed October 4, 2011. 

- [4] Wilson performance ratings. http://homepages.cae.wisc.edu/<sup>_∼_</sup> dwilson/ . Accessed October 4, 2011. 

18 

###### Burer: Robust Rankings 

- [5] Glitch in the (Colley) Matrix puts Boise State at #10, LSU #11 in BCS standings. http://www.sports-ratings.com/college ~~f~~ ootball/2010/12/ glitch-in-the-colley-matrix-puts-boise-state-at-10-lsu-11-in-bcs-standings. html, December 2010. Accessed October 4, 2011. 

- [6] Wes Colley, Alabama-Huntsville researcher, talks about his BCS error. http: //www.al.com/sports/index.ssf/2010/12/wes ~~c~~ olley ~~a~~ labama-huntsville.html, December 2010. Accessed October 4, 2011. 

- [7] A. Ben-Tal, L. El Ghaoui, and A. Nemirovski. _Robust Optimization_ . Princeton Series in Applied Mathematics. Princeton University Press, Princeton, NJ, 2009. 

- [8] D. Bertsimas and M. Sim. The price of robustness. _Operations Research_ , 52(1):35–53, 2004. 

- [9] T. P. Chartier, E. Kreutzer, A. N. Langville, and K. E. Pedings. Sensitivity and stability of ranking vectors. _SIAM J. Sci. Comput._ , 33(3):1077–1102, 2011. 

- [10] B. J. Coleman. Minimizing game score violations in college football rankings. _Interfaces_ , 35(6):483–497, 2005. 

- [11] B. J. Coleman. Ranking sports teams: A customizable quadratic assignment approach. _Interfaces_ , 35(6):497–510, 2005. 

- [12] W. N. Colley. Colley’s bias free college football ranking method: The Colley Matrix explained. Manuscript, 2002. Available at http://www.colleyrankings. com/. 

- [13] L. El Ghaoui and H. Lebret. Robust solutions to least-squares problems with uncertain data. _SIAM J. Matrix Anal. Appl._ , 18(4):1035–1064, 1997. 

- [14] A. Y. Govan, A. N. Langville, and C. D. Meyer. Offense-defense approach to ranking team sports. _J. Quant. Anal. Sports_ , 5(1):Art. 4, 19, 2009. 

- [15] D. S. Hochbaum. Ranking sports teams and the inverse equal paths problem. In _Proceedings of the Second International Workshop on Internet and Network Economics (WINE-2006), Lecture Notes in Computer Sciences_ , volume 4286, pages 307–318, 2006. 

- [16] ILOG, Inc. _ILOG CPLEX 12.2, User Manual_ , 2011. 

- [17] J. P. Keener. The Perron-Frobenius theorem and the ranking of football teams. _SIAM Rev._ , 35(1):80–93, 1993. 

19 

_Submission to Journal of Quantitative Analysis in Sports_ 

- [18] K. Massey. Statistical models applied to the rating of sports teams. Master’s thesis, Bluefield College. 

- [19] MATLAB. _version 7.11.0 (R2010b)_ . The MathWorks Inc., Natick, Massachusetts, 2010. 

20 


