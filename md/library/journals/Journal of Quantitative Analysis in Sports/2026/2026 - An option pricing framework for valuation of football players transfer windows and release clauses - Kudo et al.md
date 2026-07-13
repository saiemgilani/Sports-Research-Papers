<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2026/2026 - An option pricing framework for valuation of football players transfer windows and release clauses - Kudo et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

### **Research Article** 

Yuta Kudo, Makoto Goto*, Martyn Williams, Naoto Noguchi, Shohei Sasaki, Akihiro Takai, Manabu Kosako, Shun Takemoto and Kazuki Nagai 

# **An option pricing framework for valuation of football players: transfer windows and release clauses** 

https://doi.org/10.1515/jqas-2026-0043 Received March 10, 2026; accepted May 11, 2026; published online June 1, 2026 

**Abstract:** This study develops a dynamic framework for evaluating professional football player contracts under institutional trading constraints. We incorporate transfer windows and release clauses, which restrict when transfers can occur and under what terms. Player performance is represented by a stochastic process based on a revenueadjusted Opta metric, and the club’s decision problem is formulated with time-dependent constraints. Numerical analysis reveals two main mechanisms. First, under realistic market conditions, voluntary sellouts are not optimal (“rational retention”). As contract expiration approaches, the declining remaining duration expands the set of situations in which accepting a transfer becomes optimal, generating a pronounced deadline effect. Second, release clauses reduce the club’s discretion by making high-performing players harder to retain when interest from other clubs arrives. Sensitivity analysis shows that the resulting cost is particularly 

Yuta Kudo and Makoto Goto share first and senior authorship, respectively. 

Martyn Williams, Naoto Noguchi, Shohei Sasaki, Akihiro Takai, Manabu Kosako, Shun Takemoto, and Kazuki Nagai contributed equally to this work. 

***Corresponding author: Makoto Goto** , Department of Information Science and Technology, Tokyo University of Science, 2641 Yamazaki, Noda 278-8510, Japan; and Research Institute for Science and Technology, Tokyo University of Science, 2641 Yamazaki, Noda 278-8510, Japan, E-mail: goto@rs.tus.ac.jp. https://orcid.org/0009-0008-9756-6196 **Yuta Kudo** , Department of Industrial and Systems Engineering, Tokyo University of Science, Noda 278-8510, Japan 

**Martyn Williams and Naoto Noguchi** , Cerezo Osaka Co., Ltd., Osaka 5460034, Japan 

**Shohei Sasaki, Manabu Kosako, Shun Takemoto and Kazuki Nagai** , Yanmar Holdings Co., Ltd., Osaka 530-0013, Japan 

**Akihiro Takai** , Yanmar Holdings Co., Ltd., Osaka 530-0013, Japan; and Research Institutefor Science and Technology, Tokyo University of Science, Noda 278-8510, Japan 

large for high-growth scenarios and in high-liquidity markets with frequent transfer offers, while it is less affected by downside risks such as injuries. An empirical application using proprietary data from a J.League (Japan Professional Football League) club shows that incorporating these institutional features changes contract evaluations materially, yields a lower bound tied to the release fee relative to a static DCF benchmark, and shows through counterfactual experiments that the deadline effect is driven by horizon contraction rather than short-term performance fluctuations. 

**Keywords:** contract design; deadline effect; decision thresholds; institutional constraints; optimal stopping 

## **1 Introduction** 

In recent decades, the global football market has expanded rapidly, driven by broadcasting revenues, sponsorships, and matchday income. The international transfer market has grown substantially (FIFA 2024; IMARC Group 2024), with fees increasingly concentrated on young elite players (Metelski 2024). As transfer fees and wages rise, clubs face growing financial exposure under performance uncertainty. This environment requires valuation frameworks that treat player contracts not merely as sporting assets, but as dynamic financial commitments under risk. 

To address this valuation challenge, a growing body of literature has applied quantitative methods. Marketbased and crowd-sourced approaches provide empirical benchmarks (Herm et al. 2014; Müller et al. 2017), and related work estimates transfer fees using advanced performance metrics and machine-learning methods (McHale and Holmes 2023). Theoretical research has increasingly adopted real-options theory. Tunaru et al. (2005) pioneered this approach by modeling player transfers as real options under performance uncertainty and injury risk. Wang et al. (2010) enhanced tractability by introducing protection periods. More recently, Kudo et al. (2024) 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

developed a dynamic framework incorporating both market-driven transfer offers and club-initiated sellouts, highlighting the role of managerial flexibility. Cohen and Risk (2025) further extended stochastic valuation by integrating network theory to assess salary structures and player contributions. While these studies advance the literature, they generally abstract from institutional trading constraints that shape real-world transfer decisions. 

Parallel empirical and optimization studies link performance metrics to financial and managerial decisionmaking. Empirical valuation models combine financial techniques with granular performance data (Coluccia et al. 2018; Sæbø and Hvattum 2019; Tunaru and Viney 2010). Optimization frameworks examine roster construction and transfer decisions under institutional constraints such as transfer windows or salary caps (Pantuso and Hvattum 2021; Smith and Bickel 2023). Related empirical evidence also documents forward-looking strategic behavior in professional soccer under known future conditions (Deutscher et al. 2022). However, this literature typically abstracts from the dynamic interaction between transfer timing and contractual buyout provisions that we model explicitly. 

Despite these advances, existing real-options models possess notable limitations regarding the institutional structure of the football market. Most models, including Kudo et al. (2024), treat player contracts as continuously tradable assets or focus exclusively on market-driven offers. 

This abstraction ignores transfer windows, which create alternating periods of liquidity and illiquidity (Frick 2007; Peeters and Szymanski 2014). As a result, standard models fail to capture the “deadline effect,” whereby clubs face increasing pressure to transact before market closure. Moreover, prior work often overlooks release clauses, which cap the club’s upside by mandating transfer at a predetermined fee. Ignoring these institutional constraints risks systematic misvaluation, particularly across what we term “safety” and “danger” zones of market demand. 

To overcome these limitations, we develop a dynamic valuation framework that integrates transfer windows and release clauses into an optimal stopping problem. The player’s revenue-adjusted performance metric follows a geometric Brownian motion, and the associated Hamilton–Jacobi–Bellman equations characterize the club’s timedependent decision thresholds. We solve the model numerically using the Crank–Nicolson method to capture the boundaries imposed by alternating transfer windows. Relative to standard real-options models with continuous trading, the qualitative novelty of our framework lies in the time-dependent decision structure generated by alternating transfer windows and release clauses. These institutional 

constraints create mechanisms that do not arise under continuous market access, including intra-window deadline effects, non-linear deadline acceleration across windows, and timing-dependent losses of contractual flexibility. 

This study makes three contributions. First, we identify the structural mechanism underlying the deadline effect in a finite-horizon setting with alternating liquidity regimes. Under realistic parameters, voluntary sellouts are suboptimal (“rational retention”), yet as expiration approaches, the continuation value collapses and the transfer-acceptance region expands sharply. We quantify this acceleration, with the inter-window jump reaching 159.18 % in the final window. Second, we demonstrate that release clauses impose an opportunity cost by truncating upside potential, particularly for high-growth scenarios or those facing high market liquidity. We also highlight the strong sensitivity of finitehorizon valuations to the drift parameter. Third, we provide an empirical case study using proprietary club data, complemented by counterfactual analyses and robustness checks across multiple player profiles. In this case-study setting, we document a release-fee floor relative to DCF, closer alignment of the constrained specification with Transfermarkt, and counterfactual evidence that the deadline effect is driven by horizon contraction. From a managerial perspective, the framework provides a structured basis for scenario analysis, helping clubs assess how institutional constraints may affect contract value dynamics and transfertiming incentives. 

The remainder of this paper is organized as follows. Section 2 introduces the institutional setting and develops the baseline model. Section 3 derives the valuation framework and solves the associated HJB equations. Section 4 presents numerical analyses of the model’s structural properties. Section 5 provides the empirical application. Section 6 concludes with limitations and directions for future research. 

## **2 The model** 

### **2.1 Setup** 

Our model builds on the stochastic real-options framework of Tunaru et al. (2005) and Kudo et al. (2024), extending it to incorporate transfer windows and release clauses, which introduce time-dependent trading constraints. 

Let _Rt_ denote a club’s weekly sales, _Nt_ the Opta Index of an individual player, and _St_ the aggregate Opta Index of all players within the club. While the index is an industry standard, the high inter-operator consistency of the underlying event data has been confirmed by Liu et al. (2013). It 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 3** 

quantifies a player’s performance by assigning points for various on-field actions – such as shots, passes, tackles, and fouls – based on their frequency and context within a match. These points are aggregated to yield a cumulative score for each game, providing a robust quantitative measure of a player’s skills, form, and match impact. Consequently, a higher value of _Nt_ denotes superior performance. The player’s state variable is constructed from these three elements. Let _Y t_ be the sales per player’s Opta Index, defined as the Opta value, and _Y t_ satisfies 



Assuming that _Y t_ follows a geometric Brownian motion, the stochastic dynamics of _Y t_ are given by 



where _𝜇_ ∈ ℝ denotes the drift parameter representing the expected growth rate of the revenue-adjusted performance metric, _𝜎 >_ 0 is the volatility parameter capturing performance uncertainty, and { _Wt_ } _t_ ≥0 is a standard Brownian motion defined on a filtered probability space (Ω _,_  _,_ { _t_ } _t_ ≥0 _,_ ℙ). The parameters _𝜇_ and _𝜎_ are assumed to be constant over the contract horizon. 

Since _Y t_ represents the player’s state variable, the contract value is assumed to depend on _Y t_ . We develop a model for a player’s contract value under the following assumptions: 

##### **Assumption 1.** 

- (A1) _Contract and timing:_ The contract expires at time _T_ without renewal. Transfers and sellouts are institutionally restricted to _n_ designated transfer windows,<sup>_t_</sup> 

- where the _i_ -th window is defined as <u>[</u> _<u>t</u> i_<sup>_,i_].</sup> 

- (A2) _Transfer offers and release clauses:_ Transfer offers with a release fee _K_ arrive according to a stochastic process, where the _j_ -th arrival time _𝜂 j_ follows an Erlang distribution with parameter ( _j, 𝜈_ ), independent of _Y t_ . The outcome of an offer depends on the contract type: 

   - (a) if a release clause is included, the transfer is mandatory upon the offer’s arrival; 

   - (b) otherwise, the club retains the discretion to accept or reject the offer. 

- (A3) _Club-initiated sellouts:_ The club holds the option to sell the player for a minimum transfer fee _L_ ( _< K_ ) at any chosen stopping time _𝜏_ within the transfer windows. 

- (A4) _Injury risk:_ Player injuries occur at stochastic times _𝜃k_ following an Erlang distribution with parameter 

( _k, 𝜆_ ), independent of _Y t_ , resulting in a temporary loss of value equivalent to _m_ matches ( _mY_ ). 

- (A5) _Discounting:_ Future cash flows are discounted at a constant discount rate _𝜌_ . 

> <sup>_t_</sup> Each transfer window [ _<u>t</u> i_<sup>_,i_]isfollowedbythenon-</sup> transfer window ( _ti,_ _<u>t</u> i_ +1<sup>),where0≤</sup><sup>_<u>t</u>_</sup> 1<sup>_<_</sup> _t_ 1 _<_ _<u>t</u>_ 2<sup>_<_···</sup><sup>_<_</sup> _<u>t</u> n_<sup>_<_</sup> _tn < T_ . Typically, there are two transfer windows in a season. To assess a player’s value, it is essential to distinguish whether a release clause is included, as stated in Assumption (A2). If a release clause is included, the transfer timing is determined as _𝜂_ = _𝜂_ 1, otherwise the club chooses the transfer timing _𝜂_ ∈ { _𝜂 j_ } so as to maximize the contract value. We assume Erlang distributions for offer arrivals and injuries for analytical tractability. Both processes are taken to be independent of the performance process _Y_ , allowing us to isolate institutional trading constraints from endogenous market responses. 

To facilitate the mathematical formulation, we distinguish the value functions based on the market regime and contractual terms. We denote the contract value during<sup>_tV_</sup> a transfer window [ _<u>t</u> i_<sup>_,i_](liquidperiod)by</sup><sup>_i_(</sup><sup>_Y,t_)and</sup> during a non-transfer window ( _ti,_ _<u>t</u> i_ +1<sup>)(illiquidperiod)</sup> by _V i_ ( _Y, t_ ). Furthermore, we use the superscript † (e.g., _V_<sup>†</sup> _i_<sup>(</sup><sup>_Y,t_),</sup><sup>_V_</sup> _i_<sup>†(</sup><sup>_Y,t_))torepresentcontractswithoutarelease</sup> clause (Assumption A2-b), whereas the notation without the superscript corresponds to contracts with a release clause (Assumption A2-a). 

### **2.2 Boundary conditions and recursive structure** 

The model is solved by backward induction from contract expiration _T_ . The boundary conditions and the backwardrecursive structure are identical with or without a release clause. For expositional convenience, we present the recursion using _V_ ; the corresponding expressions without a release clause follow by the same recursion with the appropriate notation. We begin with the final non-transfer window _t_ ∈ ( _tn, T_ ), where no transfer or sellout options remain and the player generates cash flows subject only to injury risk. The contract value _V n_ ( _Y, t_ ) is given by the expected discounted cash 



where 𝔼[⋅] denotes the expectation conditioned on  _t_ with _Y t_ = _Y_ (assuming standard filtration). Calculating the expected value (see, e.g., Kitamura et al. 2026), we obtain 

> **4 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 



This analytical solution serves as the terminal boundary condition for the entire framework. Values for earlier periods are determined recursively, with each window’s terminal value serving as the boundary condition for the preceding regime. 

Then, the connection between the transfer window and the non-transfer window is governed by the following continuity and optimality conditions for any _i_ ∈ {1 _,_ … _, n_ }. At the end of a transfer window ( _t_ = _ti_ ), the club chooses the optimal strategy between selling at _L_ or retaining the contract for the subsequent non-transfer window: 



At the end of a non-transfer window ( _t_ = _<u>t</u> i_ +1<sup>),thecontract</sup> value continuously transitions into the value of the next transfer window: 



For _i_ = _n_ , the boundary is the contract expiration _T_ , where _V n_ ( _Y T, T_ ) = 0. 

## **3 Valuation methodology** 

The club is assumed to choose transfer and retention decisions so as to maximize the economic value generated by the player’s contract under institutional constraints. This does not imply that clubs prioritize transfer profits over sporting success; rather, the model isolates the contractvaluation component of a broader decision problem, while on-field contribution is reflected in the performance-based state variable. For players with a release clause, the club determines the optimal timing of release. In contrast, for players without a release clause, the club determines the optimal timing of both transfer and release. Therefore, the formulation of the player’s contract must be distinguished according to the presence or absence of a release clause. 

### **3.1 Valuation with a release clause** 

We first analyze contracts with a release clause (Assumption A2-a), where transfer offers trigger mandatory sales. We derive the value function inside transfer windows and then consider the non-transfer regime. 

#### **3.1.1 Inside the transfer window** 

Inside the transfer window _t_ ∈<sup><u>[</u></sup> _<u>t</u> i_<sup>_,̄ ti_</sup> ], considering the possibilities of transfer offers and sellouts, the player is enrolled until 



and the club receives _K_ at the timing of the transfer offer, or _L_ at the timing of the sellout. Furthermore, remaining with the team until the end of the transfer window _ti_ allows the club to secure the contract value for the subsequent period outside the transfer window. Consequently, the contract value _V i_ ( _Y, t_ ) at time _t_ ∈ [ _<u>t</u> i_<sup>_,ti_]iscontingentuponits</sup> valuation during the subsequent interval _t_ ∈ [ _ti,_ _<u>t</u> i_ +1<sup>].Thus,</sup> letting _i_ = _n_ , with the current time _t_ ∈<sup><u>[</u></sup> _<u>t</u> n_<sup>_,̄ tn_</sup> ], the player’s Opta value _Y_ , the sellout timing _𝜏_ , and the subsequent contract value _Vn_ ( _Ytn_<sup>_,̄ t_</sup> _n_<sup>)outsidethetransferwindow,thevalue</sup> function _V n_ ( _Y, t_ ) inside the _n_ -th (final) transfer window is defined by 





where  denotes the set of admissible stopping times, for any _E_ ∈  _t_ , **1** _E_ is the indicator function. 

It is essential to clarify the relationship between stochastic times, such as the offer timing _𝜂_ , and other times, like the current time _t_ . The time points _t_ , _T_ , and _𝜏_ are related by _t_ ≤ _𝜏_ ≤ _T_ . Moreover, _𝜂_ and _𝜃k_ must satisfy _t_ ≤ _𝜂_ and _t_ ≤ _𝜃k_ , and they are assumed to be independent of the stochastic process { _Y t_ }. 

Applying dynamic programming and Itô’s formula yields 





where  is the following infinitesimal generator: 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 5** 

The same HJB structure applies to any transfer window _i < n_ , with boundary conditions determined recursively by the subsequent non-transfer period. The finite-horizon HJB system does not admit a closed-form analytical solution. We therefore compute the value function numerically using the Crank–Nicolson scheme. 

Solving Eq. (9) requires appropriate boundary conditions at _t_ = _tn_ , _Y_ = 0, and _Y_ → ∞. The boundary condition at the end of the transfer window _t_ = _tn_ follows directly from the optimality condition (5) defined in Section 2.2 (with _i_ = _n_ ). 

As _Y_ → ∞, the sellout constraint becomes non-binding since _V n_ ( _Y, t_ ) is increasing in _Y_ . Thus, the value function converges to the no-sellout value: 

#### **3.1.2 Outside the transfer windows** 



During the non-transfer window ( _ti,_ _<u>t</u> i_ +1<sup>),transferandsell-</sup> out options are unavailable, and the contract is valued as an illiquid asset. In this period, value derives from on-field contributions and the continuation value at the reopening of the next transfer window. For _i < n_ and _t_ ∈ ( _ti,_ _<u>t</u> i_ +1<sup>),</sup> 

where _gn_ ( _Y, t_ ) is the total expected present value of the contract without the possibility of sellout: 





The difference between Eqs. (16) and (3) lies in the third term of Eq. (16). In the case of _i_ = _n_ , the non-transfer window period ends at the contract termination _T_ , and at _t_ = _T_ , _V n_ ( _Y T, T_ ) = 0. On the other hand, when _i < n_ , the nontransfer window period ends at _<u>t</u> i_ +1<sup>,atwhichpointthe</sup> ( _i_ + 1)-th transfer window begins. At this point, the club is assumed to receive _V i_ +1( _Yt i_ +1<sup>_,_</sup><sup>_<u>t</u>_</sup> _i_ +1<sup>)at</sup><sup>_t_=</sup><sup>_<u>t</u>_</sup> _i_ +1<sup>.</sup> 

which is derived in Appendix A. 

Subsequently, we derive the boundary condition for _Y_ = 0. Substituting _Y_ = 0 into Eq. (9) yields 

By applying the same procedure as in the previous section, we obtain the following partial differential equation: 





By solving the differential equations given in Eq. (13), we obtain 

where  is the following infinitesimal generator: 





Solving Eq. (17) requires appropriate boundary conditions at _t_ = _<u>t</u>_<sup>_Y_=0,and</sup><sup>_Y_→∞.Theboundarycondition</sup> _i_ +1<sup>,</sup> at the end of the non-transfer window _t_ = _<u>t</u>_<sup>givenbythe</sup> _i_ +1<sup>is</sup> continuity condition (6) defined in Section 2.2. Since _V i_ ( _Y, t_ ) is an increasing function with respect to _Y_ from Eq. (16), we obtain the following boundary condition: 

Eq. (14) represents the decision at _Y_ = 0 between selling the player immediately or waiting for a potential transfer opportunity. Thus, the following proposition on sellout feasibility holds: 

**Proposition 1.** _A sufficient condition for feasible sellouts is given by:_ 





where _gi_ ( _Y, t_ ) is the solution to Eq. (16) obtained through expected value calculation. By following the procedure outlined in the previous section, we have the following result: 

_This condition implies that the club is incentivized to sell assets with limited upside or low liquidity._ 

> **6 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 



In particular, when _i_ = _n_ , it is natural to consider _gn_ +1( _Y, t_ ) = 0, and in this case, _gn_ ( _Y, t_ ) coincides with _V n_ ( _Y, t_ ). 

Unlike the case with a release clause, the HJB equation (25) implies two endogenous thresholds that partition the state space into three regions: a sellout region where _V_<sup>†</sup> _i_<sup>≤</sup><sup>_L_,a</sup> transfer-acceptance region where _L < V_<sup>†</sup> _i_<sup>_<K_,andareten-</sup> tion region where _V_<sup>†</sup> _i_<sup>≥</sup><sup>_K_.Inthefirstregiontheclubsells</sup> at _L_ , in the second it accepts transfer offers at _K_ , and in the third it rejects offers and retains the player. 





By solving the differential equation (21), we obtain 



The boundary conditions are identical to those in Section 3.1.1, except for the limit _Y_ → ∞. Since the club can retain high-value players indefinitely, the value approaches: 



especially _Vi_ (0 _, t_ ) = _e_<sup>−</sup><sup>_𝜌_(</sup><sup>_<u>t</u>_</sup> _i_ +1<sup>−</sup><sup>_t_)</sup> _L_ when _L_ satisfies Eq. (15). The system is solved numerically using the Crank–Nicolson method. 



### **3.2 Valuation without a release clause** 

We now consider contracts without a release clause (Assumption A2-b), where the club may accept or reject transfer offers, introducing an additional strategic control. 

#### **3.2.1 Inside the transfer windows** 

When a player does not have a release clause, the club maximizes the player’s contract value by strategically choosing not only the timing of sellout ( _𝜏_ ) but also whether to accept incoming transfer offers ( _𝜂_ ). Consequently, the value function _V_<sup>†</sup> _i_<sup>(</sup><sup>_Y,t_)isdefinedas:</sup> 



where the optimal transfer timing is the form of 



Following the same dynamic programming principle as in Section 3.1.1, but replacing the fixed transfer payoff with the maximization operator regarding the transfer decision, we obtain the following HJB equation: 

where _g_<sup>†</sup> _i_<sup>(</sup><sup>_Y,t_)isthetotalexpectedpresentvalueofthe</sup> contract without the possibility of sellout and transfer: 



The value function is computed numerically using the Crank–Nicolson method. 

#### **3.2.2 Outside the transfer windows** 

During the non-transfer window, the institutional constraints prohibit any transaction regardless of the contractual terms. Therefore, the governing partial differential equation (PDE) for the value function _Vi_<sup>†(</sup><sup>_Y,t_)isidentical</sup> to Eq. (17) derived in Section 3.1.2. The presence or absence of a release clause does not alter the instantaneous cash flow or risk dynamics when the market is closed. However, the distinction arises in the boundary condition at the end of the non-transfer window ( _t_ = _<u>t</u> i_ +1<sup>).Whilethegovern-</sup> ing equation is shared, the terminal value _Vi_<sup>†</sup> +1<sup>(</sup><sup>_Yt_</sup> _i_ +1<sup>_,_</sup><sup>_<u>t</u>_</sup> _i_ +1<sup>)</sup> incorporates the club’s enhanced flexibility to reject offers in the subsequent window. Thus, the value without a release clause follows the same PDE as in Section 3.1.2, with 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 7** 

the boundary condition determined by the optimization problem in Section 3.2.1. 

## **4 Numerical analysis of model properties** 

This section illustrates the dynamic implications of our theoretical framework through numerical analysis. We begin with a realistic benchmark parameterization that reflects observed transfer-market conditions, then introduce a counterfactual configuration to activate latent decision boundaries, and finally examine the structural sensitivity of the optimal thresholds. 

### **4.1 Baseline dynamics: rational retention** 

We analyze valuation dynamics over a three-year contract ( _T_ = 102 weeks), corresponding to three seasons of 34 league matches per season in the J.League calendar, with alternating transfer and non-transfer windows. In each season, we define two transfer windows: weeks 1–6 and weeks 18–22. Across the three-season horizon, this yields six transfer windows in total. The model uses benchmark weekly parameters ( _𝜇_ = 0, _𝜎_ = 0.2, _𝜌_ = 0.1∕34, _𝜈_ = 1∕10, _𝜆_ = 1∕34, _m_ = 3) with a release fee _K_ = 1 and minimum transfer fee _L_ = 0.5. Under these benchmark parameters, the condition of Proposition 1 is not satisfied, implying that voluntary sellout is not optimal and that no sellout threshold exists. 

We implement the Crank–Nicolson scheme with grid steps Δ _Y_ = 0.0005 and Δ _t_ = 0.1. Since the state variable is normalized by the release fee ( _K_ = 1), this spatial 

resolution corresponds to 0.05 % of the fee level. Gridrefinement checks confirm convergence: value-function differences are below 0.5 %, and transfer-threshold differences remain small in absolute terms (see Appendix D). 

Figure 1 illustrates the evolution of the contract value for different performance levels. The thin lines represent contracts with a release clause, while the thick lines represent those without. The blue solid, orange dashed, green dotted, and red dash-dotted lines correspond to performance levels _Y_ = 0, 0.02, 0.04, and 0.06, respectively. The yellow regions represent the alternating transfer windows. 

For _Y_ = 0 (blue solid lines), the player generates no performance-based value but may still create value through a potential transfer fee _K_ . As time elapses, the probability of receiving a transfer offer declines, causing the contract value to decrease monotonically. To avoid a zero payoff at expiration, it becomes optimal for the club to sell the player during the final transfer window. Because accepting any transfer offer is strictly optimal when _Y_ = 0, the presence of a release clause does not affect the optimal strategy. Consequently, the values with and without a release clause coincide, and the thin and thick lines overlap. 

A distinct dynamic emerges for higher performance levels ( _Y_ = 0.02 _,_ 0.04 _,_ 0.06), where the performance-based value of retaining the player exceeds the release fee _K_ . Under a release clause (thin lines), the arrival of a transfer offer is undesirable, as it forces the club to transfer the player at the predetermined fee _K_ . Within a transfer window, as time passes, the probability of such a forced transfer declines, leading to a gradual increase in contract value. Outside transfer windows, this transfer risk disappears, and the value decreases with the shortening of the remaining contract duration. 



**Figure 1:** Contract value dynamics over a 3-year horizon with alternating transfer and non-transfer windows. The thin lines represent the contract value with a release clause, while the thick lines represent the value without a release clause. Colors and line styles correspond to different levels of the player’s performance state ( _Y_ ): blue solid ( _Y_ = 0), orange dashed ( _Y_ = 0.02), green dotted ( _Y_ = 0.04), and red dash-dotted ( _Y_ = 0.06). The horizontal lines denote the release fee ( _K_ ) and the minimum transfer fee ( _L_ ). Shaded yellow regions indicate transfer windows. 

> **8 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

In contrast, without a release clause (thick lines), the club can reject undesirable offers. As a result, the contract value is not exposed to forced-transfer risk and therefore does not exhibit the same intra-window 

However, as contract expiration approaches, the remaining benefit from retaining the player declines, making realization of the transfer fee increasingly attractive. Consequently, the value difference between contracts with and without a release clause narrows and eventually disappears. Regarding the final sellout decision, for moderate performance levels ( _Y_ = 0.02 _,_ 0.04), it is optimal to sell the player at the end of the final transfer window to secure the minimum transfer fee _L_ . In contrast, for a high-performing player ( _Y_ = 0.06), the expected value of retaining the player until expiration exceeds _L_ , making retention optimal even in the final window. 

Figure 2 depicts the optimal transfer thresholds over time under realistic market conditions. The yellow regions represent the alternating transfer windows. For contracts without a release clause, the club optimally manages the transfer-acceptance threshold (red solid line), which partitions the state space into a retention region<sup>(</sup> _Y > Yt_<sup>∗∗</sup> ) and a transfer-acceptance region<sup>(</sup> _Y_ ≤ _Yt_<sup>∗∗</sup> ). To isolate the impact of market frictions, we compare this baseline threshold with a hypothetical “always-open window” scenario in which the market remains continuously open (blue dashed line). 

Two insights emerge. First, the baseline threshold (red solid line) is consistently higher than the continuous-trading 



**Figure 2:** Optimal transfer thresholds and the deadline effect approaching contract expiration under realistic baseline parameters. The red solid curve illustrates the time-varying transfer-acceptance threshold ( _Yt_ ∗∗) for contracts without a release clause. The blue dashed curve represents the transfer-acceptance threshold under the hypothetical assumption that the transfer window is always open. The sharp upward divergence of the threshold in the final year demonstrates the deadline effect. Shaded yellow regions indicate transfer windows. 

**Table 1:** Quantification of deadline acceleration in transfer thresholds. 

|**Transfer** **window**|**1**|**2**|**3**|**4**|**5**|**6**|
|---|---|---|---|---|---|---|
|Average intra-window|2.22|1.25|3.09|4.65|7.74|11.36|
|increase (%)|||||||
|Inter-window jump to next<br>window (%)|–|17.65|28.57|34.38|64.71|159.35|



threshold (blue dashed line). This upward shift reflects the periodic loss of liquidity: when future trading opportunities are restricted, the continuation value of retention declines, and transfer acceptance becomes optimal over a wider range of states. Second, while the blue dashed line rises smoothly over time, the red solid line exhibits localized increases near the end of each transfer window. This pattern indicates an intra-window deadline effect, in which the impending market closure temporarily raises the transferacceptance threshold and increases the incentive to conclude transactions before the window closes. 

Finally, as contract expiration approaches, a pronounced long-term deadline effect emerges in both scenarios. The shortening of the remaining duration reduces the continuation value of retention, expanding the acceptance region. Consequently, the transfer threshold increases sharply near _T_ , indicating that the club becomes willing to accept offers at _K_ for players it would have retained earlier in the contract. 

Table 1 quantifies this structural shift by measuring the percentage increase in the transfer-acceptance threshold across the six transfer windows. Both the intra-window increase and the inter-window jump accelerate non-linearly as expiration approaches. By the final transfer window, the inter-window jump reaches 159.35 %, while intra-window pressure peaks at 11.36 %. This pattern provides clear quantitative evidence that as the remaining time vanishes ( _T_ − _t_ → 0), time decay dominates performance considerations, shifting the optimal strategy from retention toward transfer acceptance. 

### **4.2 Structural mechanism of the deadline effect** 

To elucidate the latent mechanisms governing transfer and sellout decisions, we conduct a theoretical “stress test.” By imposing a counterfactually high discount rate ( _𝜌_ = 0.05) and adjusting the offer intensity ( _𝜈_ = 0.4∕10), we mechanically suppress the continuation value of retention. This exaggerated parameterization forces the hidden decision boundaries to materialize within the observable state space. Figure 3 illustrates the contract value dynamics under this 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 9** 





**Figure 3:** Contract value dynamics under the counterfactual stress-test parameterization. To activate the sellout option, a high discount rate and high offer intensity are imposed. The thin lines represent the contract value with a release clause, and the thick lines represent the value without a release clause. Colors and line styles indicate different performance levels ( _Y_ = 0 _,_ 0.02 _,_ 0.04 _,_ 0.06). Shaded yellow regions indicate transfer windows. 

counterfactual regime in which voluntary sellout is feasible. We adopt the same graphical conventions as in Figure 1 and focus on the contrast with the baseline dynamics. 

For _Y_ = 0, the minimum transfer fee _L_ dominates the expected payoff of waiting for a transfer. It is therefore optimal to sell the player at the beginning of each transfer window. Once the window closes, this sellout opportunity disappears, and the contract value declines during the nontransfer period. As the next transfer window approaches, the value gradually rises toward _L_ , reflecting the reinstated option to sell. 

For _Y_ = 0.02, the player lies at the margin between transfer acceptance and sellout. The optimal strategy is to wait for a transfer offer during the window and sell the player at the window’s end if no offer arrives. Unlike the baseline case in Figure 1, the transfer fee _K_ now exceeds the discounted performance value. Since the arrival of an offer is desirable, the valuation dynamics reverse: within a transfer window, the contract value declines as time passes and the probability of receiving an offer decreases. Outside the window, the value increases as the next trading period approaches. 

For _Y_ = 0.04, voluntary sellout is no longer optimal, but transfer arrival remains desirable. The contract therefore continues to exhibit intra-window depreciation and interwindow appreciation. Finally, for _Y_ = 0.06, performance value is sufficiently high that transfer arrival is undesirable during the first two seasons. The dynamics revert to those observed in Figure 1: value increases within transfer windows as the likelihood of an unwanted transfer declines. 

Although the parameter configuration in this section is intentionally counterfactual, activating the sellout option clarifies the range of strategic regimes embedded in the model. It highlights how alternating transfer and 

non-transfer windows generate distinct patterns of value decline and recovery, depending on whether a potential market transaction is or detrimental to the club. 

Figure 4 presents the optimal decision thresholds under the counterfactual parameterization introduced in this section. The primary contrast with the baseline scenario in Figure 2 is the emergence of the sellout threshold ( _Yt_<sup>∗,</sup> blue dashed line). This reveals that the absence of voluntary sellout in the baseline case is not a structural restriction of the model, but a consequence of realistic parameter values that sustain a sufficiently high continuation value. When this value is exogenously reduced, the full decision structure becomes visible, explicitly dividing the state space into 



**Figure 4:** Optimal decision thresholds under the counterfactual stress-test parameterization. The figure displays both the optimal sellout threshold ( _Yt_<sup>∗, blue dashed curve) and the transfer-acceptance threshold</sup> ( _Yt_<sup>∗∗, red solid curve) for contracts without a release clause. Shaded</sup> yellow regions indicate transfer windows. 

> **10 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

three economic regions: retention (upper region), transfer acceptance (middle region), and sellout (lower region). 

Both thresholds display periodic variation driven by the alternating transfer windows. Within each window, the thresholds generally rise as the remaining time in that window decreases, reflecting the declining continuation value as the club approaches the temporary closure of the transfer window. 

Furthermore, this stress test clarifies the mechanism underlying the deadline effect. In the baseline case, the sellout threshold does not emerge, whereas the transferacceptance threshold rises sharply near expiration. Under the counterfactual parameterization, both the transfer and sellout thresholds increase markedly as _T_ − _t_ → 0. As the remaining contract duration shortens, the continuation value of retention diminishes, expanding the regions in which transfer or sellout becomes optimal. 

### **4.3 Impact of release clauses and strategic contract design** 

In this section, we quantify the “opportunity cost” of a release clause, defined as the value gap between the unconstrained contract ( _V_<sup>†</sup> ) and the constrained contract ( _V_ ). This gap represents the economic loss incurred when a club surrenders its strategic flexibility to reject transfer offers. To systematically evaluate this cost, we conduct sensitivity analyses across performance dynamics and transfer conditions. 

First, Figure 5 presents a four-panel comparison of contract values with and without a release clause under different combinations of the player’s expected growth rate ( _𝜇_ ) and performance volatility ( _𝜎_ ). The results clearly demonstrate that the drift parameter _𝜇_ exerts an overwhelmingly dominant influence on the contract 



**Figure 5:** Sensitivity of contract value and opportunity cost to expected growth rate ( _𝜇_ ) and performance volatility ( _𝜎_ ). In each panel, the red solid curve ( _V_<sup>†</sup> ) represents the contract value without a release clause, and the blue dashed curve ( _V_ ) represents the value with a release clause. The vertical gap between the curves visualizes the opportunity cost of the release clause. The horizontal axes denote the player’s performance state ( _Y_ ), and horizontal lines indicate the release fee ( _K_ ) and minimum transfer fee ( _L_ ). 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 11** 

value compared to the volatility _𝜎_ . Comparing the upper panels ( _𝜇_ = 0.1, high growth) with the lower panels ( _𝜇_ = −0.1, decline) reveals that a large positive drift drastically inflates the unconstrained value ( _V_<sup>†</sup> , red solid line). This extreme sensitivity of the finite-horizon valuation to expected growth rate highlights a critical modeling challenge: calibrating the model with noisy, short-term point estimates of _𝜇_ can mechanically explode the valuation. 

Furthermore, this dominant effect of _𝜇_ refines the practical implications of the opportunity cost. The widening of the value gap occurs in high-growth scenarios (large _𝜇_ , Panels a and b), illustrating how expected growth can amplify the opportunity cost of a release clause. These scenarios are intended to characterize the model’s structural sensitivity to expected growth rather than to estimate individual 

players’ future trajectories. For these developing prospects, the unbounded upside is strictly truncated by the release fee _K_ . Consequently, when the player-value process is assumed to follow a high-growth path, a release clause can transfer substantial upside potential from the club to the acquiring club, generating a large opportunity cost. Conversely, for players in a declining phase (Panels c and d), the opportunity cost remains negligible regardless of the volatility level. 

Second, Figure 6 illustrates the sensitivity of the contract value to offer arrival intensity _𝜈_ and release fee _K_ . Panel (b) represents the “danger zone” (high _𝜈_ , low _K_ ), where frequent external offers combined with a low buyout cap systematically strip the club of its most valuable assets, maximizing the opportunity cost. Conversely, Panel (d) represents the “safety zone” ( _𝜈_ = 0.6∕10, _K_ = 10), where 



**Figure 6:** Sensitivity of contract value and opportunity cost to offer frequency ( _𝜈_ ) and release fee ( _K_ ). The red solid curve ( _V_<sup>†</sup> ) represents the contract value without a release clause, and the blue dashed curve ( _V_ ) represents the value with a release clause. Panel (b) illustrates the “danger zone” combining high market demand with a low release fee, while panel (d) represents the “safety zone” where the release fee is sufficiently high to be non-binding. 

> **12 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

market interest is moderate and the release fee is set sufficiently high. In this regime, the release clause is effectively non-binding, and the opportunity cost becomes negligible. 

Injury risk is incorporated to capture the realistic downside uncertainty inherent in player performance. However, it does not generate the structural regime shifts analyzed in this paper. Varying the injury parameters shifts the overall value level but leaves the qualitative properties of the optimal thresholds and the deadline effect unchanged. The core mechanisms therefore arise from contractual timing and institutional constraints rather than injury shocks. 

These results yield a clear practical prescription for contract design: for high- _𝜇_ and high- _𝜈_ profiles, clubs must either secure a prohibitively high _K_ (moving to the safety zone) or refuse the clause entirely to protect their financial interests. 

## **5 Empirical case study** 

We apply the proposed framework as an empirical case study using a unique proprietary dataset provided by Cerezo Osaka, an established Japanese professional football club competing in the J1 League, the top division of the Japan Professional Football League (J.League). This dataset includes internal managerial information not publicly available, specifically club sales data and detailed contractual provisions. These data are used not to calibrate the model mechanically to an external market benchmark, but to examine whether the framework provides institutionally and operationally plausible guidance under realistic club-specific conditions. We estimate the model parameters using the Opta Index and weekly sales estimates derived from these proprietary records. The Opta Index data used in this study are provided by Stats Perform. Additionally, we discussed the model-implied patterns with practitioners at the partner club. Their feedback supported the face validity of the model and indicated that the predicted timing incentives are qualitatively consistent with decision-making under transfer-window constraints. 

### **5.1 Data construction and benchmark specification** 

Table 2 summarizes the weekly parameterization used in the empirical case study. We distinguish between two types of analyses. First, Panel (a) presents the estimates for Player A, a longitudinal case study over three seasons, used to compare the model-implied valuations with an external market benchmark. Second, Panel (b) introduces Players B and C, representing distinct risk profiles – high volatility and high liquidity, respectively. These profiles allow us to examine the robustness of the opportunity cost mechanism under different market conditions in Section 5.3. 

The drift ( _𝜇_ ) and volatility ( _𝜎_ ) are estimated via maximum likelihood using a one-season rolling window (34 matches) to reflect the practical emphasis on recent performance in transfer decision-making, with standard errors reported in parentheses. As reported in Table 2, _𝜇_ is estimated with considerable uncertainty and is not statistically distinguishable from zero at conventional levels, whereas _𝜎_ is estimated more precisely, with comparatively small standard errors. Given the well-known difficulty of precisely identifying drift from short-horizon player-level data, and the strong sensitivity of finite-horizon optimal stopping problems to expected growth as shown in Section 4.3, we set _𝜇_ = 0 in the empirical case study. This neutral and conservative specification avoids mechanically amplifying noisy short-sample drift estimates and isolates the institutional effects of transfer windows and release clauses from spurious growth assumptions. 

The transfer intensity ( _𝜈_ ) is calibrated using historical club data. The release fee is standardized to _K_ = 1, with the minimum transfer fee set to _L_ = 0.41, 0.77 and 0.67 for each player. Detailed descriptions of the data processing and estimation methodology are provided in Appendix B. Additionally, we select a discount rate _𝜌_ = 0.0029, corresponding to an annual rate of 10 %. In practice, such discount rates are typically determined internally by firms or clubs as hurdle rates and are not publicly observable. Because this information is unavailable due to confidentiality, we adopt 10 % per year as a benchmark value and convert it to the 

**Table 2:** Estimated weekly model parameters for empirical analysis. 

|**(a)** **Lo**|**ngitudinal** **case** **study (pla**|**yer A)**|**(b)** **Risk** **profiles fo**|**r robustness check**|
|---|---|---|---|---|
|**1st season**|**2nd season**|**3rd season**|**Player B**|**Player C**|
|_𝜇_<br>0.0326 (0.0413)|0.0106 (0.0358)|0.0342 (0.0200)|0.1255 (0.0992)|0.0450 (0.0532)|
|_𝜎_<br>0.2201 (0.0284)|0.1911 (0.0247)|0.1072 (0.0138)|0.4715 (0.0653)|0.2812 (0.0363)|
|_𝜈_<br>0.1250|0.1250|0.1250|0.0625|0.1875|
|_L_<br>0.41|0.41|0.41|0.77|0.67|
|_T_<br>170|136|102|102|102|



Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 13** 

weekly frequency used in the model. We also set _𝜆_ = 1∕34 (one injury per season) and _m_ = 3 (missed three games due to one injury). 

### **5.2 Player A case study: valuation dynamics and deadline effect** 

Using the observed series _Y t_ , we evaluate the model-implied value function at each week – _V i_ ( _Yt, t_ ) during transfer windows and _V i_ ( _Y t, t_ ) otherwise – to obtain the valuation trajectories based on the actual remaining contract duration in Figure 7. The blue line with circle markers represents the value with a release clause ( _V_ ), and the red line with triangle markers represents the value without a release clause ( _V_<sup>†</sup> ). To quantify the intrinsic value of on-field contributions, we plot the static discounted cash flow (DCF) value defined by Eq. (4) (green line with square markers), which represents the baseline value of retaining the player until expiration without any transfer options. The orange line with x markers indicates the normalized market value provided by Transfermarkt, which has been widely used as a proxy for actual transfer fees within the sports economics literature (Herm et al. 2014; Müller et al. 2017). We use Transfermarkt as an external market benchmark rather than as a calibration target. While it provides a useful public comparison point, it does not contain the internal sales-based cash-flow information or operational decision 



**Figure 7:** Evolution of player A’s contract value based on the actual remaining contract duration. The blue line with circle markers represents the model-implied value with a release clause ( _V_ ), and the red line with triangle markers represents the value without a release clause ( _V_<sup>†</sup> ). The green line with square markers shows the static discounted cash flow (DCF) valuation, and the orange line with x markers represents the normalized market value from Transfermarkt. Shaded yellow regions indicate transfer windows in the J.League. 

context required to evaluate the institutional mechanisms modeled here. All values are dimensionless, normalized by the release fee _K_ . The yellow regions indicate transfer windows. In our empirical analysis, _Y t_ is computed as a 4-week moving average of the revenue-adjusted Opta Index, so the valuation trajectories commence at week 4. 

Two forces jointly shape the valuation path. First, shortrun performance fluctuations generate moderate value variation across seasons. Second, the gradual reduction in the remaining contract horizon lowers continuation value, compressing the gap between constrained and unconstrained contracts over time. The positive gap reflects the economic value of contractual flexibility embedded in the unconstrained contract. Under a static DCF approach, contract value moves one-for-one with performance: when performance declines, the valuation mechanically falls. In contrast, the option-based valuation incorporates strategic timing. The presence of a transfer fee _K_ creates a floor effect, as sufficiently strong external offers allow the club to realize _K_ even if recent performance weakens. Without a release clause, the club can defer acceptance and preserve upside potential, whereas a release clause truncates this flexibility. The observed gap therefore captures the value of discretionary timing relative to passive cash-flow valuation. 

The model-based valuation with a release clause (blue line with circle markers) broadly tracks the Transfermarkt benchmark (orange line with x markers) during most of the sample period. In contrast, the unconstrained valuation (red line with triangle markers) remains persistently above the observed benchmark. This pattern suggests that the constrained specification is more consistent with market-based assessments. 

To isolate the role of contractual timing, Figure 8 presents a counterfactual experiment in which the contract is assumed to expire at _T_ = 102, holding all other parameters fixed. As _t_ → _T_ , both contract valuations collapse toward the minimum transfer fee _L_ , illustrating the pure deadline effect: the loss of remaining contract duration compresses continuation value, independent of shortterm performance realizations. Static DCF valuation cannot reproduce this convergence because it ignores transfer timing, while market benchmarks such as Transfermarkt report valuation levels but do not isolate contractual timing effects near expiration. Our framework captures this horizon-driven convergence directly. The narrowing of this gap as expiration approaches provides a model-implied measure of the deadline effect. 

To assess the robustness of the empirical case-study results to fixed auxiliary parameters, we also conduct a oneat-a-time sensitivity analysis with respect to the discount 

> **14 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 



**Figure 8:** Counterfactual analysis of player A’s contract value assuming imminent expiration ( _T_ = 102). This scenario isolates the deadline effect. The blue line with circle markers represents the value with a release clause ( _V_ ), the red line with triangle markers represents the value without a release clause ( _V_<sup>†</sup> ), the green line with square markers is the static DCF valuation, and the orange line with x markers is the Transfermarkt benchmark. As expiration approaches, both model valuations converge sharply toward the minimum transfer fee ( _L_ ). 

rate, injury intensity, and missed-game loss parameter. The details are reported in Appendix C. In addition to recomputing the Player A valuation paths, we repeat the counterfactual expiration experiment with _T_ = 102 used in Figure 8 to assess the deadline effect. The results show that these parameters affect valuation levels in the expected direction, but the main qualitative patterns remain unchanged. In particular, the release-clause opportunity cost, defined as _V_<sup>†</sup> − _V_ , remains positive on average across all specifications and 



declines to zero near expiration. Thus, the opportunity-cost mechanism and the deadline effect are not driven by a particular choice of these auxiliary parameters. 

### **5.3 Cross-player robustness: volatility, liquidity and opportunity cost** 

To examine whether the main patterns extend beyond the specific case of Player A, we examine the valuation dynamics for the distinct risk profiles defined in Panel (b) of Table 2. Figure 9 illustrates the contract values over a oneyear horizon. To ensure strict comparability and isolate the impact of risk characteristics, we adopt the standardized no-trend benchmark ( _𝜇_ = 0) across all profiles. Transferwindow definitions follow the J.League calendar and are reported in Appendix B. 

Player B (high volatility) exhibits significantly higher performance volatility ( _𝜎_ ≈ 0.47) compared to Player A. Based on the observed high-volatility series _Y t_ , the left panel shows that larger performance fluctuations are associated with a wider divergence between contracts with and without release clauses. Since a release clause caps the upside potential, the club cannot fully capitalize on the high variance, resulting in a larger opportunity cost. Player C (high liquidity) is characterized by a high offer arrival rate ( _𝜈_ ≈ 0.19). The right panel demonstrates that frequent offers increase the probability of the release clause being triggered. This “liquidity pressure” systematically widens the gap between the constrained and unconstrained values. These results suggest that the opportunity-cost mechanism is not specific to the Player A case study, but also appears 



**Figure 9:** Robustness check across different risk profiles. The left panel shows player B, characterized by high performance volatility. The right panel shows player C, characterized by high market liquidity (offer arrival rate). The red line with triangle markers represents the contract value without a release clause ( _V_<sup>†</sup> ), and the blue line with circle markers represents the value with a release clause ( _V_ ). Both profiles illustrate that the opportunity-cost mechanism appears under different risk factors. 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 15** 

under distinct risk profiles driven by internal risk (volatility) and external demand (liquidity). 

## **6 Discussion and conclusion** 

### **6.1 Limitations** 

This section critically examines the modeling assumptions and their implications for the applicability of the proposed framework. While our model explicitly incorporates the institutional constraints of transfer windows and release clauses, several simplifications were necessary to maintain analytical tractability. 

First, the model abstracts from the strategic structure of real-world transfer negotiations. In practice, transfer outcomes may depend on bargaining between clubs, competition among multiple buyers, player and agent preferences, wage renegotiation, and contract extensions. These mechanisms may affect both the timing and the final terms of a transaction. Incorporating them would require a richer strategic or game-theoretic model with endogenous bargaining outcomes, which lies beyond the scope of the present paper. Our objective is instead to isolate the institutional timing effects generated by transfer windows and release clauses. 

Second, we acknowledge that treating the offer arrival rate _𝜈_ as exogenous is a simplification. In reality, _𝜈_ likely correlates positively with performance _Y_ (higher demand for better players) and negatively with the release fee _K_ (lower demand for expensive contracts). However, estimating these sensitivities requires market-wide demand data, which is beyond the scope of our single-club dataset. Furthermore, our constant _𝜈_ assumption likely yields conservative estimates: 

1. If _𝜈_ increases with _Y_ , the actual opportunity cost of release clauses for high-performing players would be even higher than our model predicts (as they would receive offers more frequently than modeled). 

2. If _𝜈_ decreases with _K_ , the effectiveness of setting a high release fee to create a “safety zone” would be even more pronounced. Thus, the constant _𝜈_ framework serves as a robust baseline for isolating the structural impacts of transfer windows. 

Third, the model treats a release clause as a fixed-fee, binding buyout provision that substantially limits the club’s discretion once an offer arrives. In practice, release clauses may involve heterogeneous payment terms, activation conditions, renegotiation possibilities, and playeragent involvement. Such flexibility may soften the effective 

constraint imposed by the release fee _K_ : the opportunity cost of the clause would likely be smaller in magnitude, and the gap between constrained and unconstrained contract values would narrow. However, as long as the clause limits the club’s ability to retain a high-value player when external interest arrives, the qualitative mechanism remains unchanged: release clauses truncate the club’s upside by restricting retention flexibility. The present specification should therefore be interpreted as a baseline case in which _K_ acts as a hard cap, allowing us to isolate this mechanism. 

Fourth, we modeled the Opta value using Geometric Brownian Motion (GBM). As theoretically demonstrated in Section 4.3, finite-horizon valuations are highly sensitive to the drift parameter ( _𝜇_ ), which justified our adoption of a conservative no-trend benchmark ( _𝜇_ = 0) in the empirical analysis to prevent mechanical valuation explosions. Although geometric Brownian motion is standard in asset pricing, player performance may exhibit mean reversion or age effects. For typical contract horizons, however, GBM provides a tractable approximation. Extensions could incorporate alternative stochastic processes to capture lifecycle dynamics. 

Fifth, the model assumes that sellouts can occur within transfer windows at the minimum transfer fee _L_ . In reality, matching frictions and wage negotiations may affect transactions. These frictions are abstracted from to establish a baseline valuation framework. 

Finally, for practical implementation, the framework should be viewed as a scenario-analysis and decisionsupport structure rather than a plug-and-play operational tool. Applying it to live club decisions would require richer market data, club-specific calibration, and integration with broader sporting objectives. 

Despite these limitations, the proposed framework serves as a critical baseline model. By isolating the impact of transfer windows and release clauses from other confounding factors, we provide the first rigorous quantification of how these specific institutional structures alter the risk-return profile of football players compared to the continuous-time assumptions in existing literature. 

### **6.2 Conclusions** 

This study develops an option-pricing framework for valuing football player contracts under transfer windows and release clauses. By modeling performance as a stochastic asset and solving the associated HJB equations, we quantify how contractual constraints shape valuation and optimal strategy. The main contribution is therefore the identification of institutional timing mechanisms that are absent from continuous-trading formulations: intra-window deadline 

> **16 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

effects, non-linear deadline acceleration, and the timingdependent loss of contractual flexibility created by release clauses. 

Our numerical analysis reveals two critical dynamics that standard models fail to capture. First, we establish “rational retention” under realistic parameters, where voluntary sellouts are strictly suboptimal. Yet, by conducting a theoretical stress test, we expose the structural mechanism of the deadline effect: acceptance thresholds diverge sharply as expiration approaches. Consistent with this mechanism, Table 1 shows that deadline pressure intensifies non-linearly across windows, with the inter-window jump reaching 159.18 % in the final window. Second, we quantify the opportunity cost of release clauses across performance dynamics, transfer conditions, and injury risks, showing that it is driven primarily by foregone upside for high-growth or frequently offered scenarios. We also note that finite-horizon valuations are highly sensitive to the drift parameter, underscoring the need for cautious calibration. 

The empirical case study, complemented by counterfactual experiments and robustness checks, illustrates how ignoring institutional constraints can lead to materially different valuations, especially near expiration. In particular, the release fee induces a valuation floor relative to DCF, the constrained specification aligns more closely with Transfermarkt, and counterfactual expiration experiments isolate horizon contraction as the source of the deadline effect. Future research could extend this framework to include a wider range of mechanisms, such as player trades, loan agreements with options to buy, and contract renewals. Additionally, incorporating “offfield value,” such as merchandise sales and popularity, into the stochastic process could provide a more holistic valuation for superstar players. Despite these avenues for extension, the proposed framework provides a structured baseline for analyzing football player contracts under realistic institutional constraints, linking theoretical valuation methods with practical questions in sports management. 

**Acknowledgments:** The authors thank the partner club in the Japan Professional Football League (J.League) for providing access to proprietary data and for helpful discussions. The authors also thank Stats Perform for providing Opta Index data used in this study. 

**Research ethics:** Not applicable. **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and 

approved the final version of the manuscript. YK: Methodology, Software, Validation, Formal analysis, Investigation, Writing – original draft, Visualization. MG: Conceptualization, Methodology, Validation, Formal analysis, Writing – review & editing, Visualization, Supervision, Project administration. MW: Validation. NN: Validation. SS: Validation, Resources, Data curation. AT: Resources, Data curation, Project administration. MK: Resources, Data curation. ST: Resources, Data curation. KN: Resources, Data curation. 

**Use of Large Language Models, AI and Machine Learning Tools:** During the preparation of this work, the authors used generative AI solely for language editing and to improve the readability of the English text. After using this tool, the authors carefully reviewed and edited the content as needed and take full responsibility for the content of this publication. 

**Conflict of interest:** Authors MW and NN are employees of the partner club that provided proprietary data for this study. Authors SS, AT, MK, ST and KN are employees of the partner club’s parent company. The partner club and its parent company provided data and reviewed the empirical patterns for operational plausibility and helped contextualize the results from a practitioner perspective, but had no role in the study design, analysis choices, interpretation of results, or the decision to submit the manuscript. All remaining authors declare no competing interests. 

**Research funding:** None declared. 

**Data availability:** The proprietary data are not publicly available due to confidentiality restrictions. The Opta Index data are provided by Stats Perform and are subject to licensing restrictions. 

## **A Derivation of Eq. (12)** 

Let _𝜂_ denote the offer-arrival time, independent of the performance process { _Ys_ } _s_ ≥ _t_ . For any measurable function _h_ , 



Using 𝔼[ _Ys_ ∣ _Yt_ = _Y_ ] = _Ye_<sup>_𝜇_(</sup><sup>_s_−</sup><sup>_t_)</sup> and _P_ ( _𝜂 > s_ ∣ _𝜂 > t_ ) = _e_<sup>−</sup><sup>_𝜈_(</sup><sup>_s_−</sup><sup>_t_)</sup> , we obtain 



Replacing _Y s_ by (1 − _𝜆m_ ) _Y s_ yields the net flow term in Eq. (13). Moreover, 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 17** 



and the no-offer continuation term is 



Combining these terms yields Eq. (12). 

## **B Data processing and parameter estimation details** 

This appendix details the construction of the state variable _Y t_ and the estimation procedure for the model parameters presented in Section 5. First, the state variable _Y t_ (revenueadjusted performance) was constructed from the raw match data and financial records using the following three-step procedure: 

1. Aggregation (time indexing): To capture the actual flow of opportunities, the time series was constructed based on match events rather than calendar weeks. Each match defines a time step _t_ . Weeks without matches are excluded to maintain continuity in player activity. 

2. Scaling (revenue allocation): Club revenue data exhibits strong monthly seasonality. To address this, we first calculated a 12-month moving average of the monthly revenue to extract the baseline financial trend. This smoothed revenue was then allocated to each match period _t_ by dividing the monthly value by the number of matches played in that respective month. Finally, all financial values were standardized such that the release fee _K_ equals unity ( _K_ = 1), rendering the contract value dimensionless. 

3. Smoothing (GBM consistency): The individual performance metric _Nt_ was smoothed using a 4-match moving average. Smoothing ensures strictly positive values required under geometric Brownian motion and mitigates short-term volatility. A four-match moving average balances stability and sample size. 

Finally, the parameters _𝜇_ and _𝜎_ were estimated using the maximum likelihood estimation (MLE) method for a geometric Brownian motion (see, e.g., Gourieroux and Jasiak 2022). Let _xt_ = ln( _Y t_ ) denote the log-transformed state variable. The discrete log-returns Δ _xt_ = _xt_ +1 − _xt_ are assumed to follow a normal distribution: 



We maximized the log-likelihood function for the observed series of Δ _xt_ to obtain the point estimates and standard errors reported in Table 2. 

In the J.League, transfer windows create alternating periods of liquidity and illiquidity. To align the numerical implementation with the observation period used in this study, we define the transfer windows as follows. In Season 1, transfer windows are weeks 1–4 and 17–26; in Season 2, weeks 1–4 and 20–26; and in Season 3, week 1 and weeks 9–21. These week ranges are used consistently throughout the empirical valuation in Section 5.2. For the robustness analysis in Section 5.3, we use player-specific transferwindow calendars to match the observed schedules: weeks 1–6 and 21–27 for Player B, and weeks 1–4 and 17–26 for Player C. 

## **C Sensitivity analysis for fixed auxiliary parameters** 

We examine whether the empirical case-study results depend on the fixed auxiliary parameters introduced in Section 5.1. Specifically, we conduct a one-at-a-time sensitivity analysis around the benchmark specification by varying the annual discount rate _𝜌_ , the injury intensity _𝜆_ , and the missed-game loss parameter _m_ , while holding the remaining parameters fixed. The benchmark specification uses an annual discount rate of 10 %, _𝜆_ = 1∕34, and _m_ = 3. 

For each specification, we recompute the Player A valuations with and without a release clause. To evaluate the deadline effect, we also repeat the counterfactual expiration experiment in Figure 8, in which the contract is assumed to expire at _T_ = 102 while the observed performance path is held fixed. Table 3 reports the resulting valuation levels and the release-clause opportunity cost (OC), defined as _V_<sup>†</sup> − _V_ . Mean values are computed over the observed weeks in the Player A case study. Early and late opportunity costs are computed from the counterfactual expiration experiment with _T_ = 102, where “early” denotes the beginning of the first season and “late” denotes the end of the final transfer window. 

The results show that the auxiliary parameters affect valuation levels in intuitive directions: lower discounting, lower injury intensity, or smaller missed-game losses increase valuations, while the opposite changes reduce them. Importantly, the main qualitative conclusions are unchanged. The mean release-clause opportunity cost remains positive in every case, ranging from 0.20 to 0.31, and the late opportunity cost is zero after rounding across all 

> **18 —** Y. Kudo et al.: Valuation of football players: transfer windows and release clauses 

**Table 3:** Sensitivity of player A case-study valuations and release-clause opportunity cost to fixed auxiliary parameters. All values are rounded to two decimal places. 

|**Parameter** **setting**|**Mean** **_V_**|**Mean** **_V_** <sup>**†**</sup>|**Mean** **OC**|**Early** **OC**|**Late** **OC**|
|---|---|---|---|---|---|
|Benchmark (_𝜌_=10 %,_𝜆_=1/34,_m_=3)|1.15|1.42|0.27|0.78|0.00|
|_𝜌_=5 %|1.19|1.49|0.30|0.90|0.00|
|_𝜌_=15 %|1.12|1.35|0.24|0.68|0.00|
|_𝜆_=0|1.19|1.49|0.31|0.88|0.00|
|_𝜆_=3/34|1.07|1.27|0.20|0.59|0.00|
|_m_=1|1.18|1.47|0.29|0.85|0.00|
|_m_=5|1.12|1.37|0.24|0.72|0.00|



**Table 4:** Convergence of contract values with _Y_ = 0.02 and transfer thresholds. 

|**Week**|**Baseline****_V_** <sup>**†**</sup>|**Refined****_V_** <sup>**†**</sup>|**Abs.** **Diff.**|**%** **Diff.**|**Baseline** **_Y_** <sup>**∗∗**</sup><br>**_t_**|**Refined** **_Y_** <sup>**∗∗**</sup><br>**_t_**|**Abs. Diff.**|**%** **Diff.**|
|---|---|---|---|---|---|---|---|---|
|6|2.0649|2.0655|0.0005|0.03 %|0.0035|0.0034|−0.0001|−2.86 %|
|53|1.3255|1.3248|−0.0007|−0.05 %|0.0090|0.0090|0.0000|0.00 %|
|88|0.6261|0.6234|−0.0027|−0.43 %|0.0775|0.0776|0.0001|0.13 %|



specifications. This pattern indicates that the release-clause opportunity-cost mechanism and the deadline effect are not artifacts of the benchmark auxiliary parameter values. 

## **D Grid convergence check** 

To verify numerical stability of the Crank–Nicolson implementation, we compare the baseline discretization Δ _Y_ = 0.0005, Δ _t_ = 0.1 with a refined grid Δ _Y_ = 0.0002, Δ _t_ = 0.05. Since the state variable is normalized by the release fee ( _K_ = 1), the spatial resolution corresponds to 0.02–0.05 % of the fee level. 

In Table 4, we report representative weeks covering (i) an early transfer window, (ii) a mid-contract period, and (iii) the final transfer window (deadline region). Both transfer thresholds and value functions are examined. 

Across all reported cases, deviations remain below 0.5 % for contract values. For transfer thresholds, the only larger percentage deviation occurs at Week 6, because _Yt_<sup>∗∗</sup> is close to zero early in the horizon (the absolute deviation is 1 × 10<sup>−4</sup> ). The timing and magnitude of the deadline acceleration pattern are unchanged under refinement. These results confirm numerical convergence of the solution and indicate that the reported institutional effects are not driven by discretization error. 

## **References** 

- Cohen, A. and Risk, J. (2025). European football player valuation: integrating financial models and network theory. _J. Quant. Anal. Sports_ 21: 3−22,. 

- Coluccia, D., Fontana, S., and Solimene, S. (2018). An application of the option-pricing model to the valuation of a football player in the Serie A league. _Int. J. Sport Manage. Mark._ 18: 155−168,. 

- Deutscher, C., Sahm, M., Schneemann, S., and Sonnabend, H. (2022). Strategic investment decisions in multi-stage contests with heterogeneous players. _Theory Decis._ 93: 281−317,. 

- FIFA. (2024). Global transfer report 2023, https://inside.fifa.com/mediareleases/club-spending-on-international-transfer-fees-reaches-alltime-record-in-2023. 

- Frick, B. (2007). The football players’ labor market: empirical evidence from the major European leagues. _Scott. J. Political Econ._ 54: 422−446,. 

- Gourieroux, C. and Jasiak, J. (2022). _Financial econometrics: problems, models, and methods_ , vol. 2. Princeton University Press, Princeton, NJ. 

- Herm, S., Callsen-Bracker, H.-M., and Kreis, H. (2014). When the crowd evaluates soccer players’ market values: accuracy and evaluation attributes of an online community. _Sport Manage. Rev._ 17: 484−492,. 

- IMARC Group. (2024). Football market report 2024: trends and forecast by 2033, https://www.imarcgroup.com/football-market. 

- Kitamura, Y., Kudo, Y., Shimoshimizu, M., and Goto, M. (2026). Closed-form valuation of discounted cash flows with finite Poisson arrivals in a finite horizon. _Risks_ 14: 90,. 

Y. Kudo et al.: Valuation of football players: transfer windows and release clauses **— 19** 

- Kudo, Y., Shimoshimizu, M., Goto, M., Williams, M., Noguchi, N., Sasaki, S., and Takai, A. (2024). An option pricing framework for valuation of football players: transfer offers and sellouts. In: _Proceedings of ACMSA 2023_ . The Asian Association of Management Science and Applications, Okinawa, Japan, pp. 412−426. 

- Liu, H., Hopkins, W., Gómez, M.A., and Molinuevo, J.S. (2013). Inter-operator reliability of live football match statistics from OPTA Sportsdata. _Int. J. Perform. Anal. Sport_ 13: 803−821,. 

- McHale, I.G. and Holmes, B. (2023). Estimating transfer fees of professional footballers using advanced performance metrics and machine learning. _Eur. J. Oper. Res._ 306: 389−399,. 

Metelski, A. (2024). Transfer market in football: analyzing the 

- top 100 most expensive players. _Humanit. Soc. Sci._ 31: 109−120,. 

Müller, O., Simons, A., and Weinmann, M. (2017). Beyond crowd 

- judgments: data-driven estimation of market value in association football. _Eur. J. Oper. Res._ 263: 611−624,. 

- Pantuso, G. and Hvattum, L.M. (2021). Maximizing performance with an eye on the finances: a chance-constrained model for football transfer market decisions. _TOP_ 29: 493−522,. 

- Peeters, T. and Szymanski, S. (2014). Financial fair play in European football. _Econ. Policy_ 29: 343−390,. 

- Sæbø, O.D. and Hvattum, L.M. (2019). Modelling the financial 

- contribution of soccer players to their clubs. _J. Sports Anal._ 5: 23−34,. 

- Smith, Z.J. and Bickel, J.E. (2023). A roster construction decision tool for MLS expansion teams. _J. Quant. Anal. Sports_ 19: 1−14,. 

- Tunaru, R. and Viney, H. (2010). Valuations of soccer players from 

- statistical performance data. _J. Quant. Anal. Sports_ 6: 1−23,. 

- Tunaru, R., Clark, E., and Viney, H. (2005). An option pricing framework for valuation of football players. _Rev. Financ. Econ._ 14: 281−295,. 

- Wang, Q., Xu, Z., and Wu, Z. (2010). An analysis of football player transfer problems based on real options. In: _Proceedings of the 2010_ 

   - _international conference on management and service science_ . Wuhan, China, IEEE, pp. 1−3. 


