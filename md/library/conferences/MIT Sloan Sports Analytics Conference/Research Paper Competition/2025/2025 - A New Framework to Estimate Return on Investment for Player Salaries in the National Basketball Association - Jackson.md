<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2025/2025 - A New Framework to Estimate Return on Investment for Player Salaries in the National Basketball Association - Jackson.pdf -->

# **A new framework to estimate return on investment for player salaries in the National Basketball Association** 

Basketball 20251470 

## **1. Introduction** 

Methods to assess the ongoing financial performance of invested monies are essential for financial analysts. Examples are ubiquitous: mutual fund fact sheets report historical returns, publiclytraded companies report quarterly earnings to shareholders, and lenders report on defaulted and delinquent loans. In the vast majority of these cases, both the cash inflows and outflows of invested capital may be recorded as market prices. This makes the financial return calculations rudimentary. 

For example, to calculate the realized return on investment (ROI) for a sequence of cash flows, it is possible to utilize the internal rate of return (IRR) methodology of Berk and Demarzo (2007, §4.8). That is, we solve for the rate of return, , such that the discounted present value of future return cash flows equals the time zero investment. Formally, let 𝐶 0 be the initial (i.e., negative) investment, and 𝐶 1, . . . , 𝐶 be the positive future cash flows. For simplicity, we assume all cash 𝑟𝑟 flows occur on equally spaced intervals. Because we are performing a realized, ex post, return 𝐾𝐾 calculation, all 𝐶 , are assumed known. Then, 𝑡𝑡 , 𝑡𝑡 = 1, . . . 𝐾𝐾 𝐶 0 𝐾𝐾 (1) = � 𝑡𝑡 ~~�~~ �𝑟𝑟: 𝐶 𝑡𝑡=1 (1 + 𝑟𝑟)<sup>𝑡𝑡</sup> is the realized ROI. Aside from simple forms of (1), solving for will typically require the use of optimization software (e.g., Varma, 2021). 𝑟𝑟 

Complexities arise when one side of (1) does not have a clear monetary cash value or market price, however. One such case is the player contract in the National Basketball Association (NBA). Specifically, given a financial investment into an NBA player via a con tractual salary, it is of interest to assess the realized return vis-à-vis on court activities (i.e., points, rebounds, etc.). It is not immediately clear how to value such on court performance in financial terms, and it is this curiosity that is the object of our study. In other words, we endeavor to propose a methodology capable of combining a player’s salary and on court performance in such a way as to produce an equivalent formulation of (1). In doing so, we may then solve for , which is the ROI we desire to estimate. Financially quantifying on court performance would benefit numerous NBA stakeholders: e.g., 𝑟𝑟 

informing player evaluations, informing roster building decisions, assessing team roster building competency, and comparing the relative financial efficiency of NBA teams and players. Furthermore, with the recent value of NBA franchises reaching $4 billion (Wojnarowski, 2022), the answers to these questions have become more important than ever. It is natural, then, to suppose there exists a great number of studies that consider both on court performance and salary simultaneously to arrive at methods to measure realized ROI or IRR of a player’s contract in view of said player’s on court performance. A survey of related studies (e.g., Idson and Kahane, 2000; Berri 



1 

et al., 2005; Tunaru et al., 2005; Berri and Krautmann, 2006; Berri et al., 2007a; Simmons and Berri, 2011; Halevy et al., 2012; 61 Kuehn, 2017) indicates that this is not the case, however. 

We thus propose the first known unified framework to consider both on court performance and salary concomitantly to derive a realized contractual ROI for players in the NBA. It is a five-part process. The first step is to select a measurement period, such as a single NBA regular season. Step two is to select a model to assign fractional credit to players within a single game for all completed games in the measurement time period. Step three is to estimate a Single Game Value (SGV) in dollars for all completed games in the measurement time period. Steps two and three may occur simultaneously after step one. The fourth step is to combine the results of steps two and three to derive player cash flows that are based on relative on court performance. The final step is to use a player’s contractual salary as an invested cash flow and the now derived performance-based cash flows to solve for the ROI via (1). The complete ROI process is summarized in Figure 1. 



Figure 1: **NBA Contractual ROI Estimation Framework Summary** . 

We illustrate this proposed framework with a novel player credit estimator, the _Wealth Redistribution Merit Share_ (WRMS). It is a general estimator that translates an on court player performance estimate into a standardized fractional share, akin to a wealth redistribution exercise that starts from perfect uniformity and reallocates credit via relative performance. We show the WRMS estimator is asymptotically unbiased to the natural share, and it is calibrated to a replacement player, often desirable in sports analysis (e.g., Shea and Baker, 2012). As an illustration, we present a novel applied study of player performance using logistic regression for data from the 2022-2023 NBA regular season. The attractiveness of the WRMS is that an analyst is free to choose a player performance estimate, and we present such comparisons. The formal statements of these results may be found in Theorem 2.1. Given we desire to recover (1), our performance measurements are constrained to a single game. This allows us to present a methodology to compare a player with high-performance and frequent missed games against a player with average performance but consistent availability (e.g., Figure 3). To our knowledge, such a perspective remains unexplored in the sports analysis literature. We also propose a model based on ticket sales and television revenue to estimate the SGV. Conditional on the WRMS estimates, Theorem 3.1 ensures our player share dollar estimates are unbiased to total game value. 



2 

The paper proceeds as follows. Section 2 begins by heuristically deriving the WRMS starting from the natural share concept and an assumption of complete naivete. Section 2.1 then offers a novel logistic regression player performance measurement, including a review of per-game on court player performance models. The entirety of Section 2 is dedicated to step II in Figure 1. Section 3 then builds upon the work of Section 2 to complete the ROI calculation. It thus includes steps III, IV, and V in Figure 1. In both Sections 2 and 3, we provide empirical illustrations of all methods using data from the 2022-2023 NBA regular season. The paper concludes in Section 4. The Appendix provides complete proofs, and the Supplemental Material includes a brief review of basic finance, a detailed literature review, a glossary of common basketball abbreviations, details on a theoretical derivation of a Cauchy distribution, an index reference, expanded details on the logistic regression model we employ, a comparison of player performance measurements, and simulation studies. All data and replication code used herein may be found at [git repository BLINDED]. 

## **2. Wealth Redistribution Merit Share** 

The entirety of this section addresses step II of the ROI framework of Figure 1. We first derive the WRMS with a heuristic argument built from the natural share concept. We then expand upon potential on court performance measurement estimators in Section 2.1. Section 2.2 closes with empirical estimates from the 2022-2023 NBA regular season. To begin, assume there are , total games over the investment horizon selected in step I of Figure 1. Let the current game be denoted by , . Per NBA league rules, we assume each team will roster 15 players (National Basketball Association, 2018), and so 30 players 𝑁𝑁 ≥ 1 𝑁𝑁 ∈ ℤ within each game have the potential to contribute. We will index each player by 𝑔𝑔 ∈ ℤ 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 , 30, for each game, , . It is desirable to only award players that appear in each game (i.e., MIN > 0) with credit.<sup>1</sup> This allows us to treat missed games as _defaults_ in the ROI framework. 𝑚𝑚 ∈ ℤ 1 ≤ 𝑚𝑚 ≤ In the sequel, we denote the set of players with positive minutes played in game 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 , , as ℳ , and the set of 30 players with the potential to appear in game , , as ℳ<sup>�</sup> . Per NBA rules (National Basketball Association, 2018), a minimum of 10 players (5 per team) will receive 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝑔𝑔 𝑔𝑔 playing time (i.e., MIN > 0). Formally, then, 10 ≤ #{ℳ } ≤ #{ℳ<sup>�</sup> 𝑔𝑔} = 301 ≤ 𝑔𝑔 ≤ 𝑁𝑁 and ℳ ⊂ ℳ<sup>�</sup> . 𝑔𝑔 𝑔𝑔 𝑔𝑔 𝑔𝑔 

To calibrate the wealth redistribution estimate based upon on court performance, let us first assume there exists some performance measure, ∆𝑔 ∈ℝ, for each player, , , in each game , . Hence, the _natural player credit game share_ , 𝑔 for player , , in 𝑔𝑔 game , , becomes 𝑚𝑚 𝑚𝑚 ∈ ℳ 𝑔𝑔 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝒩𝒩 𝑚𝑚 𝑚𝑚 ∈ ℳ Δ 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝑔 = 𝑔 ∑ Δ𝑔𝑔𝑔∈ℳ𝑔𝑔 ~~,~~ (2) 𝟏𝟏 𝒩𝒩 𝑔𝑔∈ℳ<sup>�</sup> 𝑔𝑔 𝑔𝑔∈ℳ𝑔𝑔 𝟏𝟏 where = 1 if statement is true and 0 otherwise. It is immediate that ∑ 𝑔 = 1 for all 1 ≤ _g_ ≤ _N_ . Intuitively, this implies that players for both teams compete by way of on court performance 𝑞𝑞 𝑔𝑔 for a share of the estimated SGV in dollars. Practically, each player 𝟏𝟏 𝑞𝑞 , 𝒩𝒩, for game , 1 ≤ , would receive the 𝑔 percentage share of the SGV. For any player , \ ℳ }, 𝑔𝑔 𝑚𝑚 𝑚𝑚∈ ℳ<sup>�</sup> 𝑔𝑔 𝑔𝑔 𝑔𝑔 𝑔𝑔 ≤ 𝑁𝑁 𝒩𝒩 𝑚𝑚 𝑚𝑚 ∈ {ℳ<sup>�</sup> 

1 A full glossary of common NBA abbreviations my be found in the Supplemental Material. 



3 

𝑔 = 0 (i.e., players without playing time receive no credit). All subsequent calculations will build from the natural share construct in (2). 𝒩𝒩 As a starting point, we begin with an assumption of complete naivete. Specifically, we assign a degenerative random variable for ∆𝑔 such that , , for all , , and , . In this case, the expected credit share of a player , given the total 𝑔𝑔 number of players in the set ℳ𝑊𝑊 is known, is the uniform share: the inverse of the cardinality of the 𝑃𝑃𝑟𝑟(𝑊𝑊 = 𝑐𝑐) = 1 𝑐𝑐 ∈ ℝ 𝑚𝑚 𝑚𝑚 ∈ ℳ<sup>�</sup> 𝑔𝑔 set ℳ𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁. Symbolically, the uniform credit share is 𝑔 | ℳ , ∆𝑔 𝑚𝑚 ∈ℳ }. Hence, we 𝑔𝑔 approximate the complete naivete credit share as }]; that is, the inverse of the average 𝑔𝑔 𝑔𝑔 𝑔𝑔 𝐸𝐸(𝒩𝒩 ∼ 𝑊𝑊) = 1/#{ℳ = number of players appearing in a game over the measurement time period. If we define 𝑔𝑔 ∑∑ , then an immediate estimator of 1/𝐸𝐸[#{ℳ}] is , where . 𝑚𝑚<sup>∗</sup> 𝑔𝑔 𝑔𝑔 𝑔𝑔∈ℳ𝑔𝑔 𝑔𝑔 To incorporate a version of the replacement player standardization widely preferred in sports 𝟏𝟏 1/𝐸𝐸[#{ℳ 1/𝑚𝑚� 𝑚𝑚�= 𝑚𝑚<sup>∗</sup> /𝑁𝑁 



and 





4 



𝑔 𝑔 �ℳ � →0. (iii) Suppose the i.i.d. random variables ∆𝑔 are parametric random variables parameterized by . Let 𝑀 be a maximum likelihood estimate (MLE) of **.** For any function, ℎ1 of 𝑔 such that  ∈𝒮𝒮ℎ1 𝑔 ) ≡ ℎ2 the maximum 𝑀𝑀 likelihood estimate of 𝚯𝚯 ℎ1𝚯𝚯<sup>�</sup> ≡𝑓𝑓(𝒮𝒮)𝑔 ) is ℎ2 𝑀 ). 𝚯𝚯 𝒲𝒲(𝒮𝒮) (𝒲𝒲(𝒮𝒮) (𝚯𝚯), 𝑀𝑀 . See Appendix A. (𝒲𝒲(𝒮𝒮) (𝚯𝚯<sup>�</sup> 

_Proof_ . See Appendix A. 

◻ In an economic interpretation, the WRMS of (5) may be thought of as a prescriptive allocation of the SGV share of wealth earned by a player , , in reference to the performance measure ∆𝑔 , in comparison to uniformity (i.e., complete naivete) for any game , . Below average 𝑔𝑔 games, (i.e., ∆𝑔 < Δ<sup>�</sup> ) will decrease the share below 𝑚𝑚 𝑚𝑚 ∈ℳ , and above average games (i.e., ∆𝑔 > Δ<sup>�</sup> ) will increase the share above . In effect, then, (5) is a wealth redistribution tool. That is, 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝑔𝑔<sup>∗</sup> starting from the complete naivete assumption that all players appearing in a game have equal 1/𝑚𝑚� 𝑔𝑔<sup>∗</sup> performance and thus a perfect uniformity of wealth share, the WRMS then redistributes the wealth 1/𝑚𝑚� to each player based on each player’s on court performance in comparison to an average (or replacement) player. A notable property of (5) is that players who perform well on the losing team may still receive a large share of the SGV. Finally, observe that by definition 



which ensures an unbiased estimate at the aggregate level (i.e., the total reallocation of games sums to the original total of games, ). **2.1. Performance Measurement** 𝑁𝑁 At present, the i.i.d. on court performance measure random variable, denoted by ∆𝑔 for all , ℳ , and , , has been left unspecified. Part II of the ROI framework of Figure 1 requires 𝑚𝑚 𝑚𝑚 ∈ the basketball performance-based calculations to be contained within a single game unit. This is 𝑔𝑔 because the overall ROI framework of Figure 1 treats a player’s contractual salary as invested 𝑔𝑔 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 capital that is intended to generate per game returns or positive payments. Particularly bad games become negative cash flows (losses), and missed games are treated as defaults or missed payments. Outside of the financial ROI framework of Figure 1, the purely basketball importance of the single game unit is well-known (e.g., Oliver, 2004, Chapter 16, pg. 192), and it is thus a natural delineation of NBA performance units. Furthermore, working on a per-game basis offers some advantages. For example, _per possession_ standardization (e.g., Oliver, 2004, pg. 25) is not necessary because each 



5 

team uses approximately the same number of possessions within one game (Berri et al., 2007b, pg. 101). Finally, our per-game approach to performance measurement implies that running season per game totals (e.g., (16) of Section 2.2) allow analysts to determine the exact inflection point of an excellent player that misses many games versus a solid player that consistently plays (e.g., Figure 3.) 

Does an existing performance estimator adequately meet our per-game requirements? Given what is available at present, we believe the answer is largely negative. Many previous studies have become dated when compared against recent player tracking data (e.g., Berri, 1999; Page et al., 2007; Fearnhead and Taylor, 2011; Martínez, 2012; Casals and Martínez, 2013). In a promising study, Lackritz and Horowitz (2021) create a model to assign fractional credit to scoring statistics for players in the NBA. Unfortunately, Lackritz and Horowitz (2021) consider only offensive statistics. Idson and Kahane (2000) and Tunaru et al. (2005) do not consider basketball. In a comprehensive review, Terner and Franks (2021) further our findings that a per-game approach is largely unstudied. (The Supplemental Material provides a more detailed literature review.) 



where the abbreviations follow National Basketball Association (2023).<sup>2</sup> Despite the per game nature of (7), there are some limitations. First, GmSc does not utilize any of the recent NBA data advancements (National Basketball Association, 2023). Second, it relies on hard-coded coefficients, which are both difficult to interpret without greater context and potentially unstable over time. Finally, GmSc was derived outside of the peer-review process, which has garnered criticism (e.g., Berri and Bradbury, 2010). 

There is a much discussed level of subjectivity to assigning credit to players in a basketball game (e.g., Oliver, 2004; Berri et al., 2007b). Given this, it is our intention to propose the general WRMS in Theorem 2.1, of which the analyst is free to choose the performance estimator for ∆. For example, the Win Score (WSc) of Berri et al. (2007b), defined as 

the Win Score (WSc) of Berri et al. (2007b), defined as (8) 𝑊𝑊𝐺𝐺𝑐𝑐 = 𝑃 𝐺𝐺 + 𝑂 𝑂𝑂 + 𝐷𝐷𝑂 + 𝐺𝐺𝑃𝑃𝑆𝑆 + 0.5𝑂𝑂𝑆𝑆𝐾𝐾 + 0.5𝐹𝐹𝐺𝐺𝑃𝑃 − 𝐶𝐶𝐺𝐺𝐹𝐹 − 0.5𝐶𝐶𝑃𝑃𝐹𝐹 may be instead recoded on a per-game basis. − 𝑃𝑃𝑂𝑂𝑇𝑇 − 0.5𝑃𝑃𝐶𝐶,<sup>3</sup> For the purposes of presenting a timely and robust performance measurement model for ∆, we will employ a logistic regression model as follows (Kutner et al., 2005). Let = 1 (win) or = 0 (loss) with probability , where 𝑖 ) is a row of the design matrix of 𝑖𝑖 𝑖𝑖 team level statistics, **X** . That is, is a Bernoulli random variable with parameter, 𝑦𝑦 , for 𝑦𝑦 . 𝑖𝑖 𝑖𝑖 𝑖𝑖 𝑖𝑖 𝑖𝑖1 Notice here the indexing 𝑃𝑃𝑟𝑟(𝑦𝑦 = 1 |𝒙𝒙 , 𝜷𝜷) ≡𝑝𝑝 is for game outcome. Hence, for each 𝒙𝒙 = (1, 𝑋𝑋 , . . . , 𝑋𝑋 , 𝑖𝑖 𝑖𝑖 𝑦𝑦 𝑝𝑝 𝑖𝑖 = 1, . . . , 𝑛𝑛 𝑖𝑖, 1 ≤ 𝑖𝑖 ≤ 𝑛𝑛 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 = 𝑛𝑛/2 

2 A full glossary of common NBA abbreviations may be found in the Supplemental Material. 3 A full glossary of common NBA abbreviations may be found in the Supplemental Material. 



6 

there are two game outcomes, and . As we will introduce another indexing variable, , for the covariates, we provide an index reference in the Supplemental Material. 𝑖𝑖 = 2𝑔𝑔 𝑖𝑖 = 2𝑔𝑔 − 1 The formulation of the model implies merit performance credit is directly connected to winning 𝑗𝑗 

games, though alternative optimization objectives, such as _championships_ or _revenue_ may instead be used. The binary logit regression model has the form, for , 𝑖𝑖 = 1, . . . , 𝑛𝑛 (9) ) = log � ~~�~~ 𝑖𝑖 𝑇𝑇 𝑝𝑝 𝑖𝑖 𝑖𝑖 logit(𝑝𝑝 𝑖𝑖 = 𝒙𝒙 𝜷𝜷. The form (9) implies 1 −𝑝𝑝 1 = = . 𝑇𝑇 𝑖𝑖 exp (𝒙𝒙 𝜷𝜷) 𝑖𝑖 𝑇𝑇 𝑇𝑇 𝑝𝑝 Hence, the regression coefficients are called log-odds ratios. That is, 1 + exp (𝒙𝒙𝑖𝑖 𝜷𝜷) 1 + exp (−𝒙𝒙𝑖𝑖 𝜷𝜷) is the additive increase in the log-odds success probability from a unit increase in , when all other ’s, are held 𝑗𝑗 fixed, . Thus, at the team level, any field in **X** that returns a positive (and significant) 𝛽𝛽 𝑖𝑖𝑗𝑗 𝑖𝑖𝑗𝑗<sup>∗</sup> coefficient estimate can be interpreted as having a positive contribution to winning and vice versa 𝑥𝑥 𝑥𝑥 𝑗𝑗<sup>∗</sup> ≠𝑗𝑗 for negative coefficients. 𝑗𝑗, 𝑗𝑗<sup>∗</sup> = 1, . . . , 𝑘𝑘 Logistic regression in the context of basketball game data outcome offers some pleasing interpretations. First, if we center each covariate, , i.e., replace with ), where = , then the intercept, 0, becomes the logit at the mean. In other words, an average game by a 𝑖𝑖𝑗𝑗 𝑖𝑖𝑗𝑗 𝑖𝑖𝑗𝑗 𝑗𝑗 𝑗𝑗 team yields a 1 0 𝑋𝑋 0)) probability of winning. Hence, 𝑋𝑋 (𝑋𝑋 −𝑋𝑋<sup>�</sup> 0 = 0𝑋𝑋<sup>�</sup> 𝑖𝑖𝑗𝑗 ∑𝑋𝑋implies /𝑛𝑛 1 ) = 0.5, a quite reasonable assumption. Second, if we both assume 𝛽𝛽 0 = 0 and 𝑖𝑖 that each NBA team has the required roster of 15 players per game (National Basketball 𝑝𝑝(𝑋𝑋<sup>�</sup> , . . . , 𝑋𝑋<sup>�</sup> ) = 𝑒𝑒𝑥𝑥𝑝𝑝(𝛽𝛽 )/(1 + 𝑒𝑒𝑥𝑥𝑝𝑝(𝛽𝛽 𝛽𝛽 𝑖𝑖 Association, 2018), then we may distribute the logit of the team’s win probability linearly to the 𝑝𝑝(𝑋𝑋<sup>�</sup> , . . . , 𝑋𝑋<sup>�</sup> 𝛽𝛽 logit of each player’s individual win probability. This is a direct result of team level statistics equaling the sum of individual player level statistics (with minor exceptions; e.g., a team turnover is not credited to an individual player). We formalize this property in Theorem 2.2. **Theorem 2.2** . Let represent the individual total for player , for statistical category for game outcome . Fix and define the team total 𝑖𝑖𝑗𝑗𝑔𝑔 statistics for game outcome 𝑋𝑋 , as 𝑚𝑚, 𝑚𝑚 = 1, . . . ,15 𝑗𝑗, 𝑗𝑗 = 1, . . . , 𝑘𝑘 𝑖𝑖, 𝑖𝑖 = 1, . . . , 𝑛𝑛 𝑗𝑗 = 1, . . . , 𝑘𝑘 15 𝑖𝑖, 𝑖𝑖 = 1, . . . , 𝑛𝑛 X = . 𝑖𝑖𝑗𝑗• 𝑖𝑖𝑗𝑗𝑔𝑔 �𝑋𝑋 𝑔𝑔=1 

Then 





7 



That is, the team level logit of the win probability may be written as a sum of the logits of the individual player win probabilities. 

_Proof_ . See Appendix A. 

◻ 

The first part of Theorem 2.2 may be reminiscent of finding the treatment effects of balanced experiment designs (e.g., Montgomery, 2020). 

**Remark** . There is an important assumption of independence underlying the logistic regression model of (9) and Theorem 2.2. This independence assumption also plays an important role in Theorem 2.1. For a greater discussion, see Section 4. **Remark** . We acknowledge an abuse of notation in the indices appearing in Theorem 2.2. Specifically, when the vector notation appears, we drop the covariate index and shift the player index, , to the th position, e.g., (11). The player index, , also shifts from game, , to team, . We may equivalently index over ℳ<sup>�</sup> or 𝑗𝑗ℳ by name, , or , for any game 𝑚𝑚 𝑗𝑗 . This is done beginning at the end of Section 2.2, i.e., (15). For an index 𝑚𝑚 1 ≤ 𝑚𝑚 ≤ 30 reference, see the Supplemental Material. 1 ≤ 𝑚𝑚 ≤ 15 𝜋𝜋 𝑚𝑚, 1 ≤ 𝑚𝑚 ≤ 30 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 To translate (11) to the performance measurement, ∆𝑔 , , it is necessary to shift the index from game outcome, , to game, (recall ). Hence, to use (11) 𝑔𝑔 with Theorem 2.1, we obtain the estimator 𝑚𝑚 ∈ℳ 𝑖𝑖, 1 ≤ 𝑖𝑖 ≤ 𝑛𝑛 𝑔𝑔, 𝑔𝑔 = 1, . . . , 𝑛𝑛/2 𝑁𝑁 = 𝑛𝑛/2 1 ����� 𝑔 = ∗ 𝑔 �−WL ∗�<sup>1</sup> +<sup>1</sup> . (12) 𝑔𝑔 where �����WL ∗ = ∑∑𝒲𝒲(𝑿𝑿) 𝑠𝑠(WL)𝑔 𝑔𝑔 and �logit�𝑝𝑝 2 ∗ = ∑∑ 𝑚𝑚� 𝑚𝑚� 𝑔 �−WL����� ∗�2 ∗ − 1). For the sake of performance measurement comparison, we may also use (7) to define the 𝑔𝑔 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 𝑔𝑔 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 𝑔𝑔 estimator for player , logit�𝑝𝑝 in game �/𝑚𝑚<sup>∗</sup> 𝑠𝑠(WL) , �logit�𝑝𝑝 /(𝑚𝑚 𝑔𝑔 1 ���� 𝑚𝑚 𝑚𝑚 ∈ℳ 𝑔𝑔, 𝑔𝑔 = 1, . . . , 𝑛𝑛/2 GmSc<sup>∗</sup> 𝑔 = ∗ �GmSc𝑔 −GS ∗�<sup>1</sup> +<sup>1</sup> . (13) 𝑔𝑔 ���� (𝑿𝑿) 𝑔𝑔 2 ���� 2 ∗ where GS ∗ = ∑∑ GmSc𝑔 𝑠𝑠(GS) and ∗ = ∑∑ 𝑚𝑚��GmSc𝑚𝑚� 𝑔 −GS ∗� −1). Similarly, via (8) we define for player 𝑔𝑔 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 , 𝑔𝑔 in game 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 , 𝑔𝑔 /𝑚𝑚<sup>∗</sup> 𝑠𝑠(GS) /(𝑚𝑚 𝑔𝑔 𝑚𝑚 𝑚𝑚 ∈ℳ 𝑔𝑔, 𝑔𝑔 = 1, . . . , 𝑛𝑛/2 



8 

1 ���� WnSc<sup>∗</sup> 𝑔 = ∗ �WnSc𝑔 −WS ∗�<sup>1</sup> +<sup>1</sup> . (14) 𝑔𝑔 ���� (𝑿𝑿) 𝑔𝑔 2 ���� 2 ∗ where WS ∗ = ∑∑ WnSc𝑔 𝑠𝑠(WS) and ∗ = ∑∑ 𝑚𝑚��WnSc𝑚𝑚� 𝑔 −WS ∗� −1). By property (i) of Theorem 2.1, both (13) and (14) remain equivalently standardized to a sample 𝑔𝑔 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 𝑔𝑔 𝑔𝑔 𝑔𝑔 ∈ℳ𝑔𝑔 𝑔𝑔 /𝑚𝑚<sup>∗</sup> 𝑠𝑠(WS) /(𝑚𝑚 mean and sample standard deviation of . Hence, we can directly compare wealth allocation differences between (12), (13), and (14) (e.g., Figure 2). 1/𝑚𝑚� In closing this section, it may be tempting to ask why (2) cannot be used directly if Δ𝑔 ≡ 𝑔 � for all , and . The trouble is that, under the assumptions of Theorem 2.2, the conditional natural share in this construct, for any given , , 𝑔𝑔 logit�𝑝𝑝, is 𝑚𝑚 ∈ℳ 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝑔𝑔 𝑚𝑚 𝑚𝑚 ∈ℳ 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 logit� <u>𝑔 �</u> gm|ℳ ∑ 𝑔 � ≈ , 𝑝𝑝 𝑈𝑈 𝑔𝑔 𝒩𝒩 , 𝑿𝑿= 𝑔𝑔∈ℳ𝑔𝑔 where ), ), and . This is because, with some abuse of notation and logit�𝑝𝑝 𝑈𝑈+ 𝑇𝑇 allowance for heuristics, 𝑢𝑢<sup>2</sup> 𝑣𝑣<sup>2</sup> 𝑔 𝑔 � 2) (recall 0 = 0 by assumption and the 𝑈𝑈~𝑁𝑁(0, 𝜎𝜎 𝑇𝑇~𝑁𝑁(0, 𝜎𝜎 𝑈𝑈⊥𝑇𝑇 𝑇𝑇 covariates are centered). Hence, it can be shown that follows a Cauchy distribution with<sup>∗</sup> logit�𝑝𝑝 �≡�𝒙𝒙 𝜷𝜷≈𝑁𝑁(0, 𝜎𝜎 𝛽𝛽 <u>𝑢</u> location parameter 0 and scale parameter ~~√~~ , where = #�ℳ � (see 𝑈𝑈/(𝑈𝑈 + 𝑇𝑇) 𝜎𝜎𝑣𝑣<sup>2</sup> +𝜎𝜎<sup>2</sup> the Supplemental Material). Therefore, 𝑥𝑥 = 1/𝑎𝑎 𝑔 |ℳ 𝛾𝛾 = )  does not exist! (The median is the location 𝑎𝑎−1/𝑎𝑎 𝑎𝑎= 𝜎𝜎𝑢𝑢<sup>2</sup> 𝑔𝑔 parameter, 1/#�ℳ �.) Thus, without the stabilization of (5), players would be subject to extreme 𝑔𝑔 𝐸𝐸(𝒩𝒩 wealth shares, rendering almost all estimates practically useless. This is an additional advantage of 𝑔𝑔 the formulation of (5) in that it is robust to the practical use of a logistic regression model for performance measurement, commonly used in the literature (e.g., Teramoto and Cross, 2010; DalyGrafstein and Bornn, 2019; Terner and Franks, 2021). 

### **2.2. Empirical Results** 

We now employ the methods of Section 2.1 to NBA player statistics from the 2022-2023 NBA regular season (National Basketball Association, 2023). To compile an updated set of on court performance statistics, we utilize the python package nba_api (Patel, 2018). Because we require game-by-game statistics, we design a custom game-by-game query wrapper for Patel (2018). The result is a novel data set of 1,226 2022-2023 NBA regular season games (i.e., ) spanning 36 statistical categories (see the Supplemental Material for details). For completeness, we note that four games did not report player tracking data and were excluded: GSW @ SAS on January 13, 2023, 𝑛𝑛 = 2,452 CHI @ DET on January 19, 2023, POR @ SAS on April 6, 2023, and MIN @ SAS on April 8, 2023. To obtain the data and replication code, please navigate to the public github repository at <u>https://github.com/jackson-lautier/nba_roi.</u> 

In constructing the initial logistic regression and selecting the 36 data fields, we employ three modeling principles: aligning merit to winning, valuing as much on court activity as possible, and avoiding double counting. The variable selection process consists of first fitting a logistic regression model at the team level for all 36 statistical on court data fields. For simplicity, we then remove covariates that are not statistically significant at and perform a second logistic regression. In this second model, we estimate 0 = −0.004930 with a p-value of 0.948. Hence, we may comfortably refit the logistic regression without an intercept, as it only results in a negligible 𝛼𝛼 = 0.10 𝛽𝛽̂ 



9 

amount of bias. Because we may use Theorem 2.2 with 0 = 0, we feel allowing such small estimation bias is a negligible trade-off (further, the form of (12) will correct this bias per (6)). The final fitted model may be found in Table 1. For reference, the Supplemental Material contains 𝛽𝛽 additional details of the model fitting process, such as an expanded discussion on the modeling principles, definitions of each of the original 36 data fields, and the original fitted model with all 36 data fields. 



Table 1: **Logistic Regression Model Parameters** . Based on team outcomes for the 2022-2023 NBA regular season. Because player tracking data was not available for four games, . Significant at (∗∗∗), (∗∗), and (∗). The McFadden (McFadden, 1974) is 0.6457. Variable importance computed using Kuhn (2008). 𝑛𝑛 = 2,452 𝛼𝛼 = 0.001 𝛼𝛼 = 0.01 𝛼𝛼 = 0.05 𝑂𝑂<sup>2</sup> 

The model of Table 1 suggests that missing shots (i.e., FG2X, FG3X, FTMX), committing fouls (PF) and turnovers (TOV), contesting three point shots (C3P), allowing baskets on defended shots (DFGO), and defensive distance traveled (DDIS) negatively impact win probability. Of these, the only surprise is C3P, though it may be highly related to opponents making three-point shots. On the winning side, it is beneficial to make baskets (i.e., FG2O, FG3O, FTMO), collect rebounds (AORB, ADRB), steals (STL), blocks (BLK), draw non-charge fouls (PFD), draw charges (CHGD), set screen assists (SAST), contest two-point shots (AC2P), box out on the defensive end (DBOX), have contested shots miss (DFGX), make passes not counted in assists (APM), and collect contested 



10 

rebounds (OCRB, DCRB). The most important statistical categories may be assessed by a standard variable importance analysis (Kuhn, 2008). It finds that making (FG3O) and missing (FG3X) threepoint field goals are the most important determinants of winning. This aligns closely with long-term trend analysis of the NBA (e.g., Goldsberry, 2019). 

The performance measurement model in Table 1 is just one possibility for ∆ in (5). Many choices exist, such as (7) and (8). Different choices for ∆ will impact the resulting wealth redistribution, which allows an analyst to tailor player credit by performance measurement preference. To illustrate this, we compare the resulting distributions of (12), (13), and (14) in Figure 2. We see that despite having the same mean and standard deviation of , the distributions differ. Specifically, the WRMS estimate is more symmetric, whereas both the Game Score and Win Score are skewed right. In a robustness analysis, we find (12) outperforms both (13) and (14) in terms of 1/𝑚𝑚�= 4.75% team win prediction and team rank for data from the 2022-2023 NBA regular season (for details, see the Supplemental Material). As such, the remainder of the manuscript will provide results for (12) only, and the Supplemental Material will provide greater discussion on performance measurement comparisons between (12), (13), and (14). We emphasize that it is the framework of Figure 1 we propose, of which the NBA analyst has flexibility to replace ∆ as they see fit. 



<!-- Start of picture text -->
9<br>Game Score<br>Logistic Regression<br>Win Score<br>6<br>3<br>0<br>-10% 0% 10% 20% 30%<br>Player Game Share<br><!-- End of picture text -->





<!-- Start of picture text -->
Player Game Share<br><!-- End of picture text -->

Figure 2: **Wealth Redistribution Comparison** . Frequency distributions of (12), (13), and (14) for all NBA players from the 2022-2023 NBA regular season. The sample of game outcomes results in = 25,804. 𝑛𝑛 = 2,452 financial perspective. Denote We may also assess the cumulative total performance of a player over the investment period with a 𝑚𝑚<sup>∗</sup> ����� as the set of all players with the potential to contribute over the investment horizon. For a player , , let represent the set of games for which 𝑔𝑔 𝑔𝑔 player ’s team appeared (i.e., 𝒫𝒫= ⋃ℳ} = 82 for a standard NBA regular season). Hence, define for 𝜋𝜋 any , , 𝜋𝜋 𝜋𝜋 ∈ 𝒫𝒫 𝒢𝒢 𝜋𝜋 𝜋𝜋 #{𝒢𝒢 𝜋𝜋 𝑔𝑔 ∈𝒢𝒢 𝜋𝜋 ∈𝒫𝒫 



11 

> ∗ (15) = �<sup>𝒲𝒲(𝒮𝒮)𝑔𝑔𝜋𝜋</sup> 0,<sup>,</sup> 𝑔𝑔 𝜋𝜋∈ℳ 𝑔𝑔𝜋𝜋 Because ∑ ∑ 𝑔𝒲𝒲(𝒮𝒮)= ∑ ∑ 𝑔 𝜋𝜋∉ℳ still holds trivially, the desirable 𝑔𝑔<sup>,</sup> unbiased property of (6) remains. In financial parlance, the form of (15) implies a missed game is a 𝑁𝑁𝑔𝑔=1 𝑔𝑔∈ℳ𝑔𝑔 𝑁𝑁𝑔𝑔=1 𝑔𝑔∈ℳ<sup>�</sup> 𝑔𝑔 𝒲𝒲(𝒮𝒮) 𝒲𝒲(𝒮𝒮)<sup>∗</sup> = 𝑁𝑁 _default_ . The season total of (15) for player , , is then ∗ PVW(⋅) 𝜋𝜋= 𝜋𝜋∈𝒫𝒫 . (16) 𝜋𝜋 𝑔𝑔𝜋𝜋 �𝒲𝒲(𝒮𝒮) 𝑔𝑔∈𝒢𝒢𝑚𝑚 We may consider (16) as a present value of a series of cash flows taking the value of (15) discounted at a zero interest rate. In other words, (16) assumes all single game values are unity. This allows for a pure performance measure that does not include salary. Notably, the game-bygame approach including zeros used in (15) allows for an instant comparison of a high-performing player with frequent missed games against an average-performing player with consistent availability (i.e., Figure 3). This has been a source of perturbation in evaluating players among NBA pundits (e.g., Lowe, 2020), of which (16) may offer new insights. 



Figure 3: **Quantifying Missed Games** . The per-game approach of (16) allows for break-even calculations between high-performing players with frequent missed games (Kevin Durant, 47 games played, top) against average-performing players with consistent availability (Tari Eason, 82 games played, bottom). Data spans the 2022-2023 NBA regular season. 



12 

The placeholder (·) in (16) is generic notation that may be replaced to remind us which performance measurement underlies . For example, we will use PVWL in the sequel to denote (16) that uses (12) for ∆. For reference, a summary of the distributions of PVWL by position may be found in Figure 4. We can see the model of Table 1 tends to prefer the center position. In addition, 𝒲𝒲 we also report the top performing players, of which Nikola Jokic is the top overall PVWL performer. Though outside the scope of our present analysis, we present a comparison of PVW(·) performance measures using (13) and (14) in the Supplemental Material. Because , an average player playing 82 games would obtain a PV total of 3.896 for the 2022-2023 NBA regular season, regardless of the performance measure used. For complete results, navigate to the public github 1/𝑚𝑚�= 4.75% repository at <u>https://github.com/jackson-lautier/nba_roi.</u> 



Figure 4: **Top Performers: PVWL** . A summary of the top performers using (16) with logistic regression as the performance measurement (i.e., Table 1) in the WRMS by position. Data spans the 2022-2023 NBA regular season. 

## **3. Return on Investment** 

The purpose of the present section is to complete steps III, IV, and V of the ROI framework of Figure 1. The section proceeds in two parts. First, Section 3.1 introduces a model for the SGV (step III) and an unbiased technique to create the cash flows (step IV). We ultimately reproduce (1) in the NBA context with (19). Section 3.2 then illustrates the ROI framework with data from the 2022-2023 NBA regular season. Prior to this, we briefly review the related literature (the Supplemental Material provides a more detailed literature review). 

While no NBA studies consider both player salary and on court performance simultaneously, there is related work outside of basketball (e.g., Idson and Kahane, 2000; Tunaru et al., 2005). The field of sports economics within basketball considers competitive imbalances (Berri et al., 2005), shirking 



13 

(Berri and Krautmann, 2006), and salaries (Berri et al., 2007a; Simmons and Berri, 2011; Halevy et al., 2012; Kuehn, 2017). Our forthcoming analysis differs from all of these studies generally in that we do not attempt to explain salary decisions. Instead, we propose the first known framework to measure the realized return of a player’s contract in light of on court performance. 

### **3.1. Methods** 

It remains to estimate the SGV (step III), derive the performance-based cash flows (step IV), and perform the ROI calculations (step V) to complete the ROI framework of Figure 1. Specifically, we first propose a method to model the SGV. Next, we use the SGV model and the results of Section 2.1 to derive an unbiased estimate of a player’s performance-based cash flows. Finally, we produce (19) in the form of (1), which results in a player’s ROI estimate. 

Modeling a SGV is equivalent to answering the question: how does a regular season NBA game generate revenue? Variations of this question have attracted previous attention (e.g., Berri et al., 2007b, Chapter 5). In working from the basic ideas of Berri et al. (2007b), we assume NBA revenue is generated from ticket sales and television rights. We add a third component, which is revenue from advertising. Specifically, for , define the parametric random variable SGV (α) = α1GATE + α𝑔𝑔 = 1, . . . , 𝑁𝑁2 ESPN + α3 TNT + α4 ESPN TNT NBATV), (17) 𝑔𝑔 𝑔𝑔 where the parameter vector 𝟏𝟏1 2 3 𝟏𝟏4)<sup>𝑇𝑇</sup> consists of (𝟏𝟏 1 + 𝟏𝟏, the average ticket price for an NBA  + 𝟏𝟏 regular season game, 2, the average TV contract revenue for a regular season NBA game on ESPN, 3, the average TV contract revenue for a regular season game on TNT, and, 𝛼𝛼 = (𝛼𝛼 , 𝛼𝛼 , 𝛼𝛼 , 𝛼𝛼 𝛼𝛼 4, the average advertising revenue for a televised regular season game. Further, 𝛼𝛼 GATE is a random variable that 𝛼𝛼represents the attendance for game . In proposing (17), we do not assume a game 𝛼𝛼 𝑔𝑔 televised on NBATV generates television rights revenue for the NBA, but we do assume it generates advertising revenue. 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 In words, we propose to model SGV as the sum total of ticket sales, television revenue, and advertising revenue from game . The natural assumption is that games with higher 𝑔𝑔 attendance will be worth more, all else equal, and games that are nationally televised will be worth more, all else equal. This allows us to approximate the relative importance of a game, and it results 𝑔𝑔, 𝑔𝑔 = 1, . . . , 𝑁𝑁 in the intuitive outcome that players with more nationally televised games will generate a better ROI. This latter point connects with previous studies, as part of the value of signing star players is greater attention from fans and advertisers (e.g., Berri et al., 2007b, Chapter 5). 

With an approach to model the SGVs in hand, we may move to deriving the performance-based cash flows (i.e., step IV in Figure 1). In doing so, we will have recovered (1), which is the main objective of our analysis. We first assume the time zero cash flow (i.e., 𝐶 0) is a player’s full salary over the investment time horizon and is paid in a single lump sum. For example, assuming an NBA regular season, 𝐶 0 would represent a full season salary. From the perspective of the NBA team, it is a negative cash flow and represents the initial investment. To find the return cash flows, 𝐶 , for any player, , it is left to multiply (17) with (15) for all . This product is 𝑡𝑡 player ’s, , dollar share of SGV , , based on player ’s, , on court , 𝑡𝑡 = 𝜋𝜋 performance.  1, . . . 𝐾𝐾 𝜋𝜋, 𝜋𝜋∈𝒫𝒫 𝑔𝑔 ∈ 𝒢𝒢 𝑔𝑔 𝜋𝜋 𝜋𝜋∈𝒫𝒫 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 𝜋𝜋 𝜋𝜋∈𝒫𝒫 Formally, for any player, , let 𝐒 = (SGV1, . . . , SGV )<sup>𝑇𝑇</sup> be a vector of SGVs, via (17), and let ∗ ∗ ) be a vector of WRMSs, via (15), for all games in which player 𝑔𝑔∈𝒢𝒢𝜋𝜋 𝐾𝐾 ’s, 𝜋𝜋, 𝜋𝜋∈𝒫𝒫 𝐒𝐒 𝑇𝑇 𝑔𝑔∈𝒢𝒢𝜋𝜋 1𝜋𝜋 𝐾𝐾𝜋𝜋 𝐖𝐖 = (𝒲𝒲 , … , 𝒲𝒲 𝜋𝜋 



14 

, team appeared over the investment time horizon, where . Then the vector of return cash flows over the investment time horizon for player , becomes 𝜋𝜋 𝜋𝜋∈𝒫𝒫 #{𝒢𝒢 } = 𝐾𝐾∈ℕ ∗ ∗ π = �𝐒 � �= (SGV1 , . . . , SGV𝜋𝜋, 𝜋𝜋∈𝒫𝒫 ) , (18) 𝑻𝑻 𝑇𝑇 𝑔𝑔∈𝒢𝒢𝜋𝜋 𝑔𝑔∈𝒢𝒢𝜋𝜋 1𝜋𝜋 𝐾𝐾 𝐾𝐾𝜋𝜋 where 𝐂𝐂𝐅𝐅 � represents a diagonal 𝐒𝐒 diag�𝐖𝐖 matrix with diagonal 𝒲𝒲 𝒲𝒲 . By the definition of (5), it is possible a particularly bad game may result in SGV ∗ < 0  0 for some and 𝑔𝑔∈𝒢𝒢𝜋𝜋 𝑔𝑔∈𝒢𝒢𝜋𝜋 player diag�𝐖𝐖 . 𝐾𝐾× 𝐾𝐾 𝐖𝐖 𝑡𝑡 𝑡𝑡𝜋𝜋 𝒲𝒲 𝑡𝑡, 𝑡𝑡 = 1, . . . , 𝐾𝐾 Before proceeding to complete the ROI methodology, we illustrate that the form (18) has a 𝜋𝜋, 𝜋𝜋∈𝒫𝒫 desirable conditional unbiasedness property. Specifically, recall that (5) may be thought of as a wealth redistribution model that reallocates the SGV based on a player’s on court performance. Hence, it is of interest to ensure the reallocated cash flows in (18), given a performance model in (5), are unbiased to the expected sum total of all SGVs, i.e., ). In other words, we do not wish to inadvertently “create” or “eliminate” wealth due to a faulty estimator. This property holds if 𝑔𝑔 𝑔𝑔 ) = µ ∈ℝ for all . 𝐸𝐸(∑SGV 𝑔𝑔 𝐸𝐸(SGV **Theorem 3.1** Let SGV be a single game value random variable for any game, 𝑔𝑔 = 1, . . . , 𝑁𝑁 such that ) = µ ∈ℝ for all . Then, conditional on ∗ for all , , 𝑔𝑔 𝑔𝑔 = 1, . . . , 𝑁𝑁 𝑔𝑔 𝑔𝑔𝜋𝜋 𝐸𝐸(SGV 𝑔𝑔 = 1, . . . , 𝑁𝑁 𝒲𝒲 𝜋𝜋, 𝜋𝜋∈𝒫𝒫 𝑔𝑔 = 1, . . . , 𝑁𝑁 ∗ ∗ 𝑁𝑁 E ���SGV𝑔𝑔 𝑔𝑔𝜋𝜋 𝑔𝑔𝜋𝜋 𝒲𝒲 �𝒲𝒲 �= 𝜇𝜇𝑁𝑁. 𝑔𝑔=1 𝜋𝜋∈ℳ<sup>�</sup> 𝑔𝑔 That is, the WRMS estimator of (5), when viewed over all players and games in the investment time horizon, is unbiased to the expected total generated revenue. 

_Proof_ . See Appendix A. ◻ Finally, to retrieve the form of (1), let )<sup>−1</sup> )<sup>−𝐾𝐾</sup> )<sup>𝑇𝑇</sup> be a vector of discount factors at the rate, , where . Then the contractual ROI for player , over the 𝜋𝜋 𝜋𝜋 𝜋𝜋 investment time horizon, is the rate, 𝝂𝝂, that equates the discounted present value of player = ((1 + 𝑟𝑟 , . . . , (1 + 𝑟𝑟 ’s, 𝜋𝜋 , cash flows, (18), to player 𝑟𝑟 𝜋𝜋∈𝒫𝒫’s, , salary. That is, 𝜋𝜋, 𝜋𝜋∈𝒫𝒫 𝜋𝜋 𝑟𝑟 𝜋𝜋 𝜋𝜋∈ ∗ 𝒫𝒫 𝜋𝜋 𝜋𝜋∈𝒫𝒫 π:CF0π = �𝐒 � 𝐾𝐾 (19) ≡�<sup>SGV</sup> )<sup>𝑡𝑡</sup> �r 𝑻𝑻 𝑡𝑡<sup>𝒲𝒲</sup> 𝑡𝑡𝜋𝜋 �. 𝑔𝑔∈𝒢𝒢𝜋𝜋 𝑔𝑔∈𝒢𝒢𝜋𝜋 𝜋𝜋 where CF0π is player ’s, , full salary over the investment time horizon. We have thus 𝐒𝐒 diag�𝐖𝐖 �𝝂𝝂 𝑡𝑡=1 (1 + 𝑟𝑟𝜋𝜋 recovered (1), which completes the ROI framework of Figure 1. We remark that (19) relies on a set of reasonable assumptions, which are discussed more fully in Section 4. 𝜋𝜋 𝜋𝜋∈𝒫𝒫 

### **3.2Empirical Results** 

We now employ the methods of Section 3.1 to estimate the ROI for player salaries for the 20222023 NBA regular season. Player salary data for all players from the 2022-2023 NBA regular season are via HoopsHype (2023) (with one supplement for the player Chance Comanche (Spotrac, 2023)). The data to estimate the parameters of the SGV, denoted by (17), may be compiled from various publicly available sources. As we review the parameter estimates of (17), we will detail these 



15 

sources. To obtain the data and replication code, please navigate to the public github repository at <u>https://github.com/jackson-lautier/nba_roi.</u> Let us first estimate the parameters of (17) before proceeding to the ROI calculations. Attendance figures are readily available per game (e.g., National Basketball Association, 2023), which allows for a reliable estimate of . To estimate 1, we may work backwards from total NBA revenue. Specifically, total gates for the 2022-2023 NBA regular season are known to be 21.57% of 𝑔𝑔 total NBA revenue (Statista, 2023a). Further, total NBA revenue for the 2022-2023 NBA regular 𝐺𝐺𝐹𝐹𝑃𝑃E , 𝑔𝑔 = 1, . . . , 𝑁𝑁 𝛼𝛼 season is known to be $10.58B (Statista, 2023c). Hence, we may estimate total gate revenue at $10.58 × 21.57% = $2.28B. With total attendance for the 2022-2023 NBA regular season at 22,234,502 (National Basketball Association, 2023), we arrive at an estimate of the average perticket price, 1 = $102.64. To estimate 𝛼𝛼�2, 3, and 4, we may again work backwards from total NBA revenue. Specifically, it is known that total NBA television revenue for the 2022-2023 NBA regular season is $1.4B for games televised on ESPN (Lewis, 2023) and $1.2B for games televised on TNT (Lewis, 2023). With 101 𝛼𝛼 𝛼𝛼 𝛼𝛼 games televised on ESPN (National Basketball Association, 2023) and 65 games televised on TNT, we estimate 1 = $13,861,386 and 3 = $18,461,538. Finally, total NBA advertising revenue for the 2022-2023 NBA regular season is known to be $1.66B (Statista, 2023b). As an approximation, we assume total ad revenue to be spread equally among the 273 nationally televised 2022-2023 𝛼𝛼� 𝛼𝛼� NBA regular season games (ESPN: 101; TNT: 65; NBATV: 107) (National Basketball Association, 2023). Hence, we estimate 4 = $6,080,586. A summary of coefficient estimates for (17) may be found in Table 2. For reference, the top five teams in terms of total SGV for the 2022-2023 NBA regular season are LAL ($908.3M), GSW ($885.4M), BOS ($831.1M), PHX ($766.3M), and PHI 𝛼𝛼� ($708.5M). Each of these teams play in some of the largest television media markets (Sports Media Watch, 2024), which helps to validate these estimates. Players on these teams will generate higher ROIs because the games are more valuable, all else equal. 



Table 2: **Component Estimates of** 𝐒 . Coefficient estimates of (17) based on available data for the 2022-2023 NBA regular season (National Basketball Association, 2023; Statista, 2023a,c; 𝑔𝑔 Lewis, 2023; Statista, 2023b). 𝐒𝐒 

To estimate contractual ROI, it is necessary to select a performance measurement random variable for ∆. For consistency with Section 2.2, we will use (12) with the missed game adjustment (15). The only restriction is that a player’s salary is at or above the 2022-2023 league minimum, $1,017,781 (RealGM, L.L.C., 2024). Because we treat missed games as defaults, the minimum game restriction is just one game played. Results for all players in the 2022-2023 NBA regular season may be found in Figure 5. Not surprisingly, players with higher salaries generally realize lower ROIs, all else equal. The display of Figure 5 may be used by NBA teams to target players that may represent a better relative value at various salary ranges. Similarly, Figure 5 may be used to evaluate the performance of NBA team player personnel decision-makers when signing players. Finally, Figure 5 may be used 



16 

by the players or player agents in negotiating a new contract that is more closely aligned with comparable players in the aggregate market. To our knowledge, Figure 5 is the first such attempt to evaluate the ROI for all players in the NBA. 



Figure 5: **ROI by Salary: All Players** . A scatter plot of ROI by log of salary for all players with a salary at the league minimum ($1,017,781 (RealGM, L.L.C., 2024)) or higher for the 2022-2023 NBA regular season. The on court performance measurement is (12) with the missed game adjustment (15). Salary data (HoopsHype, 2023; Spotrac, 2023) and SGV parameter estimate data (National Basketball Association, 2023; Statista, 2023a,c; Lewis, 2023; Statista, 2023b; Sports Media Watch, 2024) detailed in Section 3.2. The ROI calculations may be performed using (19). 

As an additional illustration of the utility of the ROI estimates of Figure 5, we will use traditional financial calculations to compare the risk-reward by position. For example, the coefficient of variation (CV) (Klugman et al., 2012, Definition 3.2, pg. 20) takes a ratio of the standard deviation of an asset class to its mean. Hence, if we consider each position as an asset class, we may perform the same calculation. We do so in Table 3. 



17 



Table 3: **Coefficient of Variation for ROI by Position** . A ratio of sample standard deviation to sample mean of 2022-2023 NBA regular season empirical ROI estimates in Figure 5 by position. 

Table 3 suggests that the Center position offers the least risk per unit of return, whereas the Point Guard position is the relative riskiest per unit of return. Such results may be used to help NBA team player personnel decision-makers decide where to invest salary by position, a decision of obvious importance. Furthermore, we may calculate a replacement player ROI. Recall we have normalized (5) to , which is 4.75% for the 2022-2023 NBA regular season. With an average SGV of $5,318,785, the combination yields a replacement player game cash flow of $252,706. Finally, of the 539 players appearing in a 2022-2023 regular season NBA game, we obtain an average salary of 1/𝑚𝑚� $8,274,410. Therefore, a replacement player appearing in all 82 regular season games yields a 2.71% ROI. As an observation, the ROIs for various players will change with an alternative performance measurement model, such as (13) or (14). For details on this, see the Supplemental Material. For complete results, please navigate to the public github repository at <u>https://github.com/jackson-lautier/nba_roi.</u> 

## **4. Discussion** 

A vital component of competently investing in capital markets is assessing the ex post financial performance of invested monies. While such assessments are a standard financial calculation generally, difficulties arise when the returns are non-financial, such as on court basketball activities like rebounding, passing, and scoring. This paper attempts to address these challenges by presenting the first known framework to assess the on court performance of NBA players simultaneously within the relative context of salary. Just as the return on a financial investment is relative to the purchase price, a complete evaluation of player performance is enhanced by considering a player’s salary. Such calculations are nontrivial, and the interdisciplinary framework we propose is a five-part process that combines theory from statistics, finance, and economics. With the value of NBA franchises reaching billions of US dollars (Wojnarowski, 2022), the need for such tools is now at an all-time high. 

Within the five-part ROI framework we propose in Figure 1, the WRMS of Theorem 2.1 is itself a novel, flexible estimator of player credit capable of considering various estimates of on court player performance. The heuristic derivation of the WRMS suggests a wealth redistribution starting from an assumption of complete naivete. Further, the per-game approach required by (19) yields a new dimension to the field of basketball statistics in the form of break-even calculations for missed games (e.g., Figure 3). Such a calculation is itself timely, as the NBA’s governing body has recently implemented strategies to encourage players to avoid missing games (Wimbish, 2023). Pleasingly, the WRMS is asymptotically unbiased to the natural share. To ensure the ROI framework we 



18 

propose in this manuscript and summarize in Figure 1 is reliable and complete, we use a logistic regression model of player performance. The plug and play design of the ROI framework of Figure 1 allows for analysts to swap out player performance measures, estimators of the SGV, or even the WRMS altogether. It is our intention that this flexibility will be viewed as a positive attribute. 

Nonetheless, the infancy of research into methods to combine on court performance with player salaries in the NBA naturally suggests numerous areas ripe for further study. For example, while not necessary to utilize our ROI framework, we elect to constrain our empirical analysis to a single NBA regular season to ease exposition. Player contracts typically span multiple seasons, and so a more complete empirical analysis would increase the observation period. Further, our empirical estimates do not consider play-off games, which some NBA analysts consider to be a significant component of a player’s value (Mahoney, 2019). Hence, the empirical ROI estimates may be updated to include the playoffs. Our illustrative logistic regression model in (12) is calibrated to wins, and it is of interest to explore models calibrated to other performance goals, such as championships or revenue. Similarly, the SGV model we propose treats games with higher attendance and viewership as more important. An alternative approach might instead prefer to weight games with a significant impact on the standings as more important (though the two are likely correlated). As an example, Özmen (2016) analyzes the marginal contribution of game statistics across various levels of competitiveness in the Euroleague to win probability. Similarly, Teramoto and Cross (2010) is an example of how weighting schemes may differ for playoff games versus regular season games in the NBA. Something similar may be used to model a game’s importance. An important assumption not yet fully discussed is the implied independence in the sample, . Though a thorough study is outside the scope of this analysis, discussion is merited. Can players on a basketball court be considered independent? The answer is complex (e.g., Horrace et al., 2022), 𝒮𝒮 and more study is needed. For our purposes, the asymptotic unbiasedness derived in Theorem 2.1 will likely maintain if the dependence among the observations is weak enough to allow the Central Limit Theorem to work (Lautier et al., 2023). Hence, as a point estimate, we feel the WRMS concept is likely robust (though we notably do not present any type of variance analysis for this reason). Other approaches, such as mixed effects models or generalized estimating equations could be explored. 

The estimators would also benefit from higher precision. This may come through in the form of greater data detail. For example, considering Nielson television ratings, specific ticket prices, or a more refined approach to allocate television revenue. Individual players may get additional credit for off court revenue, such as from jersey sales. A difficulty of these potential enhancements is to obtain detailed data. Higher precision may also be obtained through enhanced calibration. For example, methods exist to refine the quality of a field-goal attempt (e.g., Shortridge et al., 2014; Daly-Grafstein and Bornn, 2019) or account for peer (i.e., teammate) and non-peer effects (e.g., Horrace et al., 2022). 

In addition to the statistical aspect, greater precision may be investigated in the financial aspects of the ROI framework of Figure 1 and the derivation of (19). For example, we assume an NBA player’s single season salary is paid in one lump sum at time zero. Generally, a player’s salary will be paid in installments throughout the regular season. Obtaining more detailed salary payment data will have an impact on the ROI calculations, which may be of interest. Further, we assume all games are played on equally spaced time intervals. This assumption may be explored using financial rate conversion techniques and more precise game dates. Further, an implicit assumption in (19) is that 



19 

games in the earlier part of the season are given more weight due to the basic conditions of the time value of money. Research into the implication of this assumption, such as randomizing the order of the games to calculate a distribution of realized ROI calculations may be prudent. Additionally, the NBA imposes a player salary cap (National Basketball Association, 2018), which includes a team salary floor. Hence, there is an implicit minimum invested, which suggests a type of risk-free rate. This may be explored further to offer Sharpe Ratio calculations (e.g., Berk and Demarzo, 2007, 

(11.17)). In addition to the replacement player adjustments employed herein, previous studies such as Niemi (2010) may be helpful for this analysis. 

## **References** 

J. Berk and P. Demarzo (2007). _Corporate Finance, 1st Edition_ . Pearson Education, Inc. D. J. Berri (1999). “Who is ‘most valuable’? Measuring the player’s production of wins in the National Basketball Association.” _Managerial and Decision Economics_ **20** , 411–427. 

D. J. Berri and J. C. Bradbury (2010). “Working in the land of the metricians.” _Journal of Sports Economics_ **11** , 29–47. 

D. J. Berri, S. L. Brook, B. Frick, A. J. Fenn and R. Vicente-Mayoral (2005). “The short supply of tall people: Competitive imbalance and the National Basketball Association.” _Journal of Economic Issues_ **39** , 1029–1041. 

D. J. Berri, S. L. Brook and M. B. Schmidt (2007a). “Does one simply need to score to score?” _International Journal of Sport Finance_ **2** , 190–205. 

D. J. Berri and A. C. Krautmann (2006). “Shirking on the court: Testing for the incentive effects of guaranteed pay.” _Economic Inquiry_ **44** , 536–546. 

D. J. Berri, M. B. Short and S. L. Brook (2007b). _The Wages of Wins: Taking Measure of the Many Myths in Modern Sport_ . Standford Business Books. 

M. Casals and J. A. Martínez (2013). “Modelling player performance in basketball through mixed models.” _International Journal of Performance Analysis in Sport_ **13** , 64–82. 

D. Daly-Grafstein and L. Bornn (2019). “Rao-blackwellizing field goal percentage.” _Journal of Quantitative Analysis in Sports_ **15** , 85–95. 

P. Fearnhead and B. M. Taylor (2011). “On estimating the ability of NBA players.” _Journal of Quantitative Analysis in Sports_ **7** . 

K. Goldsberry (2019). _Sprawlball: A Visual Tour of the New Era of the NBA_ . HarperCollins. 

N. Halevy, E. Y. Chou, A. D. Galinsky and J. K. Murnighan (2012). “When hierarchy wins: Evidence from the National Basketball Association.” _Social Psychological and Personality Science_ **3** , 398–406. HoopsHype (2023). “2022/23 NBA Player Salaries.” hoopshype.com. 

- <u>https://hoopshype.com/salaries/players/2022 2023/.  Online; accessed 12 June 2023.</u> 

W. C. Horrace, H. Jung and S. Sanders (2022). “Network competition and team chemistry in the NBA.” _Journal of Business & Economic Statistics_ **40** , 35–49. 

T. Idson and L. Kahane (2000). “Team effects on compensation: An application to salary determination in the National Hockey League.” _Economic Inquiry_ **38** , 345–357. 

S. A. Klugman, H. H. Panjer and G. E. Willmot (2012). _Loss Models: From Data to Decisions, Fourth Edition_ . Hoboken, New Jersey: John Wiley & Sons, Inc. 

J. Kuehn (2017). “Accounting for complementary skill sets: Evaluating individual marginal value to a team in the National Basketball Association.” _Economic Inquiry_ **55** , 1556–1578. 

M. Kuhn (2008). “Building predictive models in R using the caret package.” _Journal of Statistical Software_ **28** , 1–26. 

M. H. Kutner, C. J. Nachtsheim, J. Neter and W. Li (2005). _Applied Linear Statistical Models_ . McGrawHill Irwin. 



20 

J. Lackritz and I. Horowitz (2021). “The value of statistics contributing to scoring in the NBA: A quantitative approach.” _The American Economist_ 66, 175–189. 

J. P. Lautier, V. Pozdnyakov and J. Yan (2023). “Pricing time-to-event contingent cash flows: A discrete-time survival analysis approach.” _Insurance: Mathematics and Economics_ **110** , 53–71. 

E. Lehmann and G. Casella (1998). _Theory of Point Estimation, 2nd Edition_ . Springer. 

J. Lewis (2023). “NBA announces 9-year extension with ESPN, Turner, through 2025.” https://www.sportsmediawatch.com/ - Sports Media Watch 

<u>https://www.sportsmediawatch.com/2014/10/nba-tv-deal-espn-abc-tnt-nine-year-deal-2025-24billion-lockout/.  Online; accessed 27 December 2023.</u> 

Z. Lowe (2020). “2020 NBA awards ballot: Zach Lowe’s picks for All-NBA, All Defensive and AllRookie.” https://www.ESPN.com - Entertainment and Sports Programming Network. <u>https://www.espn.com/nba/story/_/id/29541185/2020-nba-awards-ballot-zach-lowe-picks-allnba-all-defensive-all-rookie. Online; accessed 24 July 2023.</u> R. Mahoney (2019). “The 16-game player: Why Draymond Green thrives in the NBA playoffs.” Sports Illustrated. <u>https://www.si.com/nba/2019/05/29/draymond-green-warriors-raptors-2019-nbafinals-stephen-curry-kevin-durant.  Online; accessed 20 July 2023.</u> J. A. Martínez (2012). “Factors determining production (FDP) in basketball.” _Economics and Business Letters_ **1** , 21–29. 

D. McFadden (1974). “Conditional logit analysis of qualitative choice behavior.” _Frontiers in Econometrics_ pp. 105–142. 

D. C. Montgomery (2020). _Design and Analysis of Experiments: Tenth Edition_ . Hoboken, 665 New Jersey: John Wiley & Sons, Inc. 

N. Mukhopadhyay (2000). _Probability and Statistical Inference_ . New York, NY: Marcel Dekker. National Basketball Association (2018). “Highlights of the Collective Bargaining Agreement between the National Basketball Association (NBA) and National Basketball Players Association (NBPA).” nba.com. <u>https://cdn.nba.com/manage/2021/03/2018-19-CBA.pdf . Online; accessed 19 July 2023.</u> National Basketball Association (2023). “Statistics.” nba.com. <u>https://www.nba.com/stats. Online;</u> accessed 13 June 2023. 

J. B. Niemi (2010). “Evaluating individual player contributions to team offense and defense: A model based approach.” JSM Proceedings, Section on Statistics in Sports, Vancouver, BC, Canada: American Statistical Association. 

D. Oliver (2004). _Basketball on Paper: Rules and Tools for Performance Analysis_ . Potomac Books, Inc. M. U. Özmen (2016). “Marginal contribution of game statistics to probability of winning at different levels of competition in basketball: Evidence from the Euroleague.” _International Journal of Sports Science & Coaching_ **11** , 98–107. 

G. L. Page, G. W. Fellingham and C. S. Reese (2007). “Using box-scores to determine a position’s contribution to winning basketball games.” _Journal of Quantitative Analysis in Sports_ 3. 

S. Patel (2018). “nba_api: An API client package to access the APIs of NBA.com.” GitHub repository. https://github.com/swar/nba api. Online; accessed 21 July 2023 (v1.2.0). RealGM, L.L.C. (2024). “2017 CBA minimum annual salary scale.” RealGM.com. https://basketball.realgm.com/nba/info/minimum scale. Online; accessed 1 May 2024. S. M. Shea and C. E. Baker (2012). “Calculating Wins over Replacement Player (WORP) for NHL goaltenders.” _Journal of Quantitative Analysis in Sports_ 8. 

A. Shortridge, K. Goldsberry and M. Adams (2014). “Creating space to shoot: Quantifying spatial relative field goal efficiency in basketball.” _Journal of Quantitative Analysis in Sports_ **10** , 303–313. 

R. Simmons and D. J. Berri (2011). “Mixing the princes and the paupers: Pay and performance in the National Basketball Association.” _Labour Economics_ **18** , 381–388. The Economics of Sports Labour Markets. 



21 

Sports Media Watch (2024). “Major pro and college sports teams ranked by market size.” Sports Media Watch. https://www.sportsmediawatch.com/nba-market-size-nfl-mlb-nhl-nielsenratings/. Online; accessed 9 February 2024. 

Sports Reference LLC (2023). “Glossary.” Basketball-Reference.com - Basketball Statistics and History. https://www.basketball-reference.com/about/glossary.html. Online; accessed 26 January 2023. 

Spotrac (2023). “Contract details.” Spotrac.com. https://www.spotrac.com/nba/portland-trailblazers/chance-comanche-82139/. Online; accessed 25 July 2023. 

Statista (2023a). “Gate receipts as percentage of total revenue in the National Basketball Association from 2010/11 to 2022/23.” https://www.statista.com/ Statista https://www.statista.com/statistics/193410/percentage-of-ticketing-revenue-in-the-nba-since2006/. Online; accessed 27 December 2023. 

Statista (2023b). “National Basketball Association sponsorship revenue from 2010 to 2023.” https://www.statista.com/ - Statista https://www.statista.com/statistics/380270/nbasponsorship-revenue/. Online; accessed 27 December 2023. 

Statista (2023c). “National Basketball Association total league revenue from 2001/02 713 to 2022/23.” https://www.statista.com/ - Statista https://www.statista.com/statistics/193467/totalleague-revenue-of-the-nba-since-2005/. Online; accessed 27 December 2023. 

M. Teramoto and C. L. Cross (2010). “Relative importance of performance factors in winning NBA games in regular season versus playoffs.” _Journal of Quantitative Analysis in Sports_ **6** . 

Z. Terner and A. Franks (2021). “Modeling player and team performance in basketball.” _Annual Review of Statistics and Its Application_ **8** , 1–23. 

R. Tunaru, E. Clark and H. Viney (2005). “An option pricing framework for valuation of football players.” _Review of Financial Economics_ **14** , 281–295. Real Options SI. 

J. Varma (2021). jrvFinance: Basic finance; NPV/IRR/annuities/bond-Pricing; Black Scholes. R package version 1.4.3. 

J. Wimbish (2023). “NBA CBA: New details emerge about in-season tournament, 65-game threshold for MVP, other awards.” https://www.cbssports.com/ - CBS Sports. https://www.cbssports.com/nba/news/nba-cba-new-details-emerge-about-in-season{}tournament-65-game-threshold-for-mvp-other-awards/. Online; accessed 28 July 2023. A. Wojnarowski (2022). “Mat Ishbia agrees to Suns purchase for record $4 billion.” https://www.ESPN.com - Entertainment and Sports Programming Network. https://www.espn.com/nba/story/_/id/35292815/sources-mat-ishbia-finalizing-suns-purchase4-billion. Online; accessed 30 June 2023. 



22 

## **Appendix A** 

_Proof of Theorem 2.1_ . For the standardization of (i), recall (3), (4), and (5) to write 



Next, ignore the radical to similarly show 



For (ii), recall Δ𝑔 are i.i.d. for all and observe 𝑔𝑔 𝑚𝑚, 𝑚𝑚 ∈ ℳ , 𝑎𝑎𝑛𝑛𝑎𝑎 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 



Further, given ℳ , 𝑔𝑔 𝑔𝑔 𝑚𝑚 ∈ ℳ , 𝑎𝑎𝑛𝑛𝑎𝑎 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁, But Δ𝑔 are i.i.d. for all , and so the distribution of 𝑔 |ℳ is equivalent for all . Hence, assuming 𝑔 |ℳ ) exists, 𝑔𝑔 𝑔𝑔 𝒮𝒮 𝒩𝒩 𝑚𝑚∈ℳ 𝑔𝑔 𝐸𝐸(𝒩𝒩 



23 



for all . Hence, 𝑔 �ℳ �= 1/#{ℳg}. The number of players appearing in any game, , is a discrete random variable over the integers {10,...,30}, and so the expectation is 𝑔𝑔 𝑔𝑔 finite and nonzero. Hence, by the Weak Law of Large Numbers (Lehmann and Casella, 1998, 𝑚𝑚∈ℳ 𝐸𝐸�𝒩𝒩 Theorem 8.2, pg. 54-55) and the continuous mapping theorem (Lehmann and Casella, 1998, 𝑔𝑔, 1 ≤ 𝑔𝑔 ≤ 𝑁𝑁 Corollary 8.11, pg. 58), consistency follows. 

Finally, property (iii) is an immediate consequence of the invariance property of the MLE (Mukhopadhyay, 2000, Theorem 7.2.1, pg. 250). 



_Proof of Theorem 2.2_ . Observe, 











24 

_Proof of Theorem 3.1_ . Observe, 



The proof is then complete by (6). 

◻ 

## **Appendix B** 

This manuscript has an accompanying online Supplemental Material.  The Supplemental Material contains a brief review of discounting cash flows with interest, a detailed literature review, a glossary of standard statistical abbreviations used in the NBA, a result related to generating a Cauchy distribution, a reference of indexing variables, additional logistic regression model details, and simulation studies (including an extension to Theorem 3.1).  To locate the Supplemental Material, please navigate to <u>nba_roi_0529.pdf</u> (beginning on pg. 36). 



25 


