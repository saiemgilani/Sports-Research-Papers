<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2021/2021 - Comparing sequential forecasters is 538 any better than Vegas-Odds - Unknown Authors.pdf -->

# **Comparing Sequential Forecasters** 

**Yo Joong Choe**<sup>*</sup> Data Science Institute University of Chicago yjchoe@uchicago.edu 

**Aaditya Ramdas** Department of Statistics and Data Science Machine Learning Department Carnegie Mellon University aramdas@cmu.edu 

November 10, 2023 

##### **Abstract** 

Consider two forecasters, each making a single prediction for a sequence of events over time. We ask a relatively basic question: how might we compare these forecasters, either online or post-hoc, while avoiding unverifiable assumptions on how the forecasts and outcomes were generated? In this paper, we present a rigorous answer to this question by designing novel sequential inference procedures for estimating the time-varying difference in forecast scores. To do this, we employ confidence sequences (CS), which are sequences of confidence intervals that can be continuously monitored and are valid at arbitrary data-dependent stopping times (“anytime-valid”). The widths of our CSs are adaptive to the underlying variance of the score differences. Underlying their construction is a game-theoretic statistical framework, in which we further identify e-processes and p-processes for sequentially testing a weak null hypothesis — whether one forecaster outperforms another _on average_ (rather than _always_ ). Our methods do not make distributional assumptions on the forecasts or outcomes; our main theorems apply to any bounded scores, and we later provide alternative methods for unbounded scores. We empirically validate our approaches by comparing real-world baseball and weather forecasters. 

## **Contents** 

|**1**|**Introduction**|**3**|
|---|---|---|
|**2**|**Related Work**|**5**|
|**3**|**Preliminaries**|**6**|
||3.1<br>Test Supermartingales, Ville’s Inequality, and Confdence Sequences . . . . . .|. . .<br>6|
||3.2<br>Forecast Evaluation via Scoring Rules . . . . . . . . . . . . . . . . . . . . . .|. . .<br>8|
|**4**|**Anytime-Valid Inference for Average Forecast Score Differentials**|**9**|
||4.1<br>A Game-Theoretic Formulation<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>9|
||4.2<br>The Measure-Theoretic Setup. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>10|
||4.3<br>Time-Uniform Confdence Sequences for Average Score Differentials<br>. . . . .|. . .<br>12|



This manuscript is published in _Operations Research_ ; see https://doi.org/10.1287/opre.2021.0792. 

*Work done while this author was at Carnegie Mellon University. 

1 

|||4.3.1<br>Time-Uniform Boundaries and Exponential Test Supermartingales . . . . . .<br>12|
|---|---|---|
|||4.3.2<br>Warmup: Hoeffding-Style Confdence Sequences . . . . . . . . . . . . . . .<br>13|
|||4.3.3<br>Main Result: Empirical Bernstein Confdence Sequences . . . . . . . . . . .<br>13|
|||4.3.4<br>Choosing the Uniform Boundary via the Method of Mixtures . . . . . . . . .<br>14|
||4.4|Sequential Tests, e-Processes and p-Processes . . . . . . . . . . . . . . . . . . . . .<br>15|
|**5**|**Exp**|**eriments**<br>**18**|
||5.1|Numerical Simulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>18|
||5.2|Comparing Forecasters on Major League Baseball Games . . . . . . . . . . . . . . .<br>23|
||5.3|Comparing Statistical Postprocessing Methods for Weather Forecasts. . . . . . . . .<br>24|
|**6**|**Exte**|**nsions and Discussion**<br>**26**|
|**A **|**Mai**|**n Proofs**<br>**32**|
||A.1|Sub-exponential Test Supermartingales for Time-Varying Means . . . . . . . . . . .<br>32|
||A.2|<br>Proof of Theorem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>33|
||A.3|Proof of Theorem 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>33|
|**B**|**Deta**|**ils on Time-Uniform Boundary Choices**<br>**34**|
||B.1|Computing the Gamma-Exponential Mixture<br>. . . . . . . . . . . . . . . . . . . . .<br>34|
||B.2|The Polynomial Stitching Boundary . . . . . . . . . . . . . . . . . . . . . . . . . .<br>36|
|**C **|**Asy**|**mptotic CSs for Sequential Forecast Comparison**<br>**37**|
|**D **|**Com**|**paring Relative Forecasting Skills Using the Winkler Score**<br>**38**|
|**E**|**Com**|**paring Lagged Forecasts**<br>**41**|
|**F**|**Infe**|**rence for Predictable Subsequences and Bounds**<br>**46**|
||F.1|Inference for Predictable Subsequences<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>46|
||F.2|<br>Inference Under Predictable Bounds . . . . . . . . . . . . . . . . . . . . . . . . . .<br>48|
|**G **|**Gen**|**eralizations To Other Outcome and Forecast Types**<br>**51**|
|**H **|**Com**|**parison with Other Forecast Comparison Methods**<br>**52**|
||H.1|Methodological Comparison with Henzi and Ziegel (2022) . . . . . . . . . . . . . .<br>52|
||H.2|Comparison with DM and GW Tests . . . . . . . . . . . . . . . . . . . . . . . . . .<br>53|
|**I**|**Add**|**itional Experiment Details and Results**<br>**55**|
||I.1|Additional Details & Results from Numerical Simulations<br>. . . . . . . . . . . . . .<br>55|
|||I.1.1<br>Data Generation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>55|
|||I.1.2<br>All Pairwise Comparisons in Numerical Simulations . . . . . . . . . . . . .<br>55|
||I.2|<br>Additional Details & Results from the MLB Experiment<br>. . . . . . . . . . . . . . .<br>57|
|||I.2.1<br>Details on the MLB Forecasters . . . . . . . . . . . . . . . . . . . . . . . .<br>57|
|||I.2.2<br>All Pairwise Comparisons of MLB Forecasters . . . . . . . . . . . . . . . .<br>59|
||I.3|Additional Details & Results from the Weather Experiment . . . . . . . . . . . . . .<br>59|
||I.4|Fine-Tuning the CS Width Using Simulated IID Mean Differentials<br>. . . . . . . . .<br>59|



2 

|**Forecasters**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|FiveThirtyEight<sup>1</sup>|37.9%|41.0%|52.7%|58.7%|37.3%|40.5%|48.5%|
|Vegas-Odds.com<sup>2</sup>|34.9%|37.7%|41.0%|50.7%|33.7%|37.4%|43.1%|
|Adjusted Win Percentage|47.1%|47.4%|47.6%|47.4%|47.2%|47.0%|47.2%|
|K29 Defensive Forecast|50.0%|50.0%|50.9%|51.6%|50.7%|49.9%|49.1%|
|Constant Baseline|50.0%|50.0%|50.0%|50.0%|50.0%|50.0%|50.0%|
|Average Joe|40.0%|50.0%|60.0%|50.0%|30.0%|40.0%|50.0%|
|Nationals Fan|70.0%|70.0%|80.0%|70.0%|60.0%|60.0%|70.0%|
|_Did the Nationals Win?_|Yes|Yes|No|No|No|Yes|Yes|



Table 1: Probability forecasts (%) on whether a baseball team (Washington Nationals) would win each game of the 2019 World Series. The first two forecasters publish their forecasts online in the form of probabilities or betting odds. The next three forecasters are baselines computed using the 10year win/loss records. The last two forecasters are imaginary (but not unrealistic) casual sports fans making their own forecasts using different heuristics. All forecasts are made prior to the beginning of each game. See Section 5.2 for more details. 

## **1 Introduction** 

Forecasts of future outcomes are widely used across domains, including meteorology, economics, epidemiology, elections, and sports. Often, we encounter multiple forecasters making probability forecasts on a regularly occurring event, such as whether it will rain the next day and whether a sports team will win its next game. Yet, despite the ubiquity of forecasts, it is not obvious how we can formally compare different forecasters on their predictive ability, particularly in a sequential setting where they each make a prediction on a sequence of outcomes (once for each outcome). 

As an illustrative example, consider the probability forecasts made on each game of the 2019 World Series by real-world (and fictitious) forecasters in Table 1. It is not clear how we can effectively model the sequence of baseball game outcomes over time, and we also do not have full information on how each forecaster comes up with their predictions. As we observe these forecasts and outcomes game-by-game, we may see one forecaster appearing to be better than the other, according to some scoring rule. But how much of that difference can be attributed to chance or luck? How much evidence do we have that one forecaster has been “genuinely” better than another, even after accounting for chance, and can we quantify this evidence without having to make assumptions about reality or how the forecasts are made? 

In this work, we derive statistically rigorous procedures for _sequentially_ comparing forecasters via the powerful tool of _confidence sequences (CS)_ (Darling and Robbins, 1967; Lai, 1976b; Howard et al., 2021). CSs are sequences of confidence intervals (CIs) that provide time-uniform coverage guarantees, which allow valid sequential inference under continuous monitoring and at data-dependent stopping times. The parameter of interest in this paper is the time-varying mean difference in forecast scores up to time _t_ . Most CSs we develop in our paper are also nonasymptotically valid, meaning that their coverage guarantee holds at every time point _t ≥_ 1. 

In addition, we derive _e-processes_ and _p-processes_ (Ramdas et al., 2022) for testing whether one forecaster outperforms the other on average, which is a composite null that we formally define in Section 4.4. An e-process _Et_ is a nonnegative process such that under the null, its expectation at any 

> 1 Source: https://projects.fivethirtyeight.com/2019-mlb-predictions/games/. 

> 2 Source: https://sports-statistics.com/sports-data/mlb-historical-odds-scores-datasets/. 

3 

t<sup>(fivethirtyeight, vegas); S=BrierScore</sup> 



<!-- Start of picture text -->
95% CS for  t E-Process (log-scale)<br>0.010 10 4<br>EB CS<br>0.005 10 2<br>0.000 10 0<br>0.005 10 2 H 0  : t 0, t<br>H0 : t 0, t<br>0.010 10 4<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>Time Time<br><!-- End of picture text -->

Figure 1: _Left:_ A 95% CS (Theorem 2) for the average Brier score differentials (∆ _t_ )<sup>_T_</sup> _t_ =1<sup>between</sup> _FiveThirtyEight_ and _Vegas_ , two real-world forecasters that made game-by-game probability forecasts on Major League Baseball (MLB) games from 2010 to 2019 ( _T_ = 25 _,_ 165). Positive values of ∆ _t_ indicate that the first forecaster is better than the second on average. Unlike a classical CI, a CS covers the time-varying parameter ∆ _t_ uniformly over all _t_ with high probability. In this case, we find that, with 95% probability, the sequence ∆ _t_ trends negative for _t ≥_ 10 _,_ 000, indicating that _Vegas_ outperformed _FiveThirtyEight_ on average across most of the time horizon. _Right:_ E-processes (Theorem 3) for the null hypotheses, _H_ 0 : ∆ _t ≤_ 0 _, ∀t_ (brown, dashed) and _H_ 0 : ∆ _t ≥_ 0 _, ∀t_ (purple, solid), respectively. An e-process quantifies the accumulated evidence against the null, and it has a direct correspondence to the CS. In this example, larger values in the e-process for _H_ 0 : ∆ _t ≥_ 0 _, ∀t_ indicate evidence of _Vegas_ outperforming _FiveThirtyEight_ on average. The gray dashed line plots the value 2 _/α_ = 40, and the time at which an e-process upcrosses this line is also when the (1 _− α_ )-CS moves entirely below or above zero. See Sections 4 and 5 for details. 

stopping time is at most one. It quantifies the amount of accumulated evidence against the null up to time _t_ : a larger _Et_ is more evidence against the null. Further, p _t_ = 1 _/_ sup _i≤t Ei_ is a p-process — its realization at any stopping time is a valid p-value, a property referred to as _anytime-valid_ or _always-valid_ (Johari et al., 2022; Howard et al., 2021). These are also formally defined in Section 4.4. Throughout the paper, we define _safe, anytime-valid inference (SAVI)_ methods as ones that satisfy either the time-uniform coverage guarantee (CS) or the anytime-valid guarantee (e- or p-processes). 

The setup in which we develop our methods is game-theoretic (Shafer and Vovk, 2019): we posit that two players participate in a forecasting game on a sequence of outcomes with an unknown distribution. This setup naturally leads to “distribution-free” inference procedures — other than requiring bounded scoring rules, we make no assumptions on the time-varying dynamics of the outcomes and forecasts, such as stationarity. We further discuss how to relax even the assumption of bounded scores using asymptotic CSs (Section C) and normalized scores (Section D). 

In Figure 1, we show an example of a CS and its corresponding e-processes applied to a forecasting game between two real-world forecasters, _FiveThirtyEight_ and _Vegas_ , on the outcomes of Major League Baseball (MLB) games. The CS in the left plot continuously tracks the expected average score differential over time and effectively visualizes the time-varying trend along with the uncertainty on its estimation. The two e-processes in the right plot each measure the accumulated evidence favoring each forecaster over time. In this example, both the CS and the e-processes show that _Vegas_ has outperformed _FiveThirtyEight_ on average. We return to this example in Section 5.2. 

The rest of the paper is organized as follows. After discussing related work (Section 2) and prelimi- 

4 

naries (Section 3), we derive CSs for the time-varying average forecast score differentials between two probabilistic forecasters in Sections 4.1-4.3, with the case of binary outcomes as a working example. In Section 4.4, we also derive e-processes and p-processes as duals to our CSs, providing alternative sequential inference procedures for forecast comparison. In Section 5.1, we empirically validate our CSs and compare them against fixed-time and asymptotic confidence intervals (CIs) on simulated data; in Sections 5.2 and 5.3, we apply our methods to real-world forecast comparison tasks, namely comparing game-by-game predictions in Major League Baseball (MLB) and comparing statistical postprocessing methods of ensemble weather forecasts. In addition, Section A contains omitted proofs; Section B contains technical details about the time-uniform boundary choices; Section C contains an alternative forecast comparison approach using an asymptotic CS; Sections D-F contain extensions to normalized scores (Winkler, 1994), lag- _h_ forecasts, and predictable conditions/bounds, respectively; Section G contains extensions from binary outcomes to categorical and continuous outcomes; Section H contains detailed comparisons with the methods of Henzi and Ziegel (2022); Diebold and Mariano (1995); Giacomini and White (2006); and Section I contains additional details about our simulated, MLB, and weather experiments as well as details about experimentally fine-tuning the CS width. 

## **2 Related Work** 

**Evaluation and Comparison of Forecasts.** Forecast evaluation is a well-studied subject in the literature of statistics, economics, finance, and climatology, dating back to the works of Brier (1950); Good (1952); DeGroot and Fienberg (1983); Dawid (1984); Schervish (1989). The primary tool for evaluating forecasts is proper scoring rules, of which the literature is extensive. Many characterization theorems for proper scoring rules exist across different forecasting scenarios, notably including the case of probability forecasts for binary and categorical outcomes, point forecasts (e.g., mean, quantiles, and prediction intervals) for continuous outcomes, and fully probabilistic forecasts (e.g., densities and CDFs) for continuous outcomes. See, e.g., McCarthy (1956); Savage (1971); Schervish (1989); Winkler et al. (1996); Grünwald and Dawid (2004); Gneiting and Raftery (2007); Gneiting (2011); Abernethy and Frongillo (2012); Dawid and Musio (2014); Ehm et al. (2016); Ovcharov (2018); Frongillo and Kash (2021); Waggoner (2021), for both classical and recent developments. 

The problem of comparing forecasts while accounting for sampling uncertainty was first popularized in the case of probability forecasts by Diebold and Mariano (1995) (DM), who proposed tests of equal (historical) forecast accuracy using the differences in forecast errors. The DM test is based on the asymptotic normality of the average forecast score differentials, and it makes stationarity assumptions about the outcomes. Giacomini and White (2006) (GW) developed tests of _conditional_ predictive accuracy given past information, allowing for the comparison of “which forecaster is more accurate given the information available at the time of forecasting.” The GW test thus allows for nonstationarity, although it restricts the forecasters to a fixed window size _m_ and its validity depends on mixing assumptions. Lai et al. (2011) presented a comprehensive overview of the aforementioned methods of forecast comparison and developed a martingale-based theory of scoring rules whose differentials are linear in the outcome, such as proper scoring rules. They proved the asymptotic normality of both forecast scores and score differentials, leading to an asymptotic and fixed-time CI that we use as a point of comparison in our work. More recent work by Ehm and Krüger (2018); Ziegel et al. (2020); Yen and Yen (2021) derive fixed-time tests of forecast dominance under all consistent scoring functions (Gneiting, 2011). In comparison with all of these previous methods that presuppose a fixed sample size, the key difference in our work is that we develop inference methods that are valid at arbitrary data-dependent stopping times, while making virtually no assumption on the time- 

5 

varying dynamics of the data generating process. The resulting graphical representations of CSs and e-processes also convey information about the entire time-varying trend of score differences, as in Figure 1, unlike classical tests and CIs that concern a single comparison at a fixed time point. 

Recently, Henzi and Ziegel (2022) constructed sequential tests of conditional forecast dominance based on e-processes (Howard et al., 2020; Grünwald et al., 2023; Shafer, 2021; Ramdas et al., 2022; Vovk and Wang, 2021). These methods are also anytime-valid and nonasymptotic; yet, they test a “strong<sup>3</sup> null,” which states that one forecaster is better than the other at _every_ point in time, something we rarely believe a priori. Thus, rejecting the strong null only suggests that there exists _some_ time point where the latter forecaster is better than the former, which may not come as much of a surprise. (One case where the strong null is appropriate is if we test two sets of forecasts produced by the same data scientist, with one forecaster using more features or more sophisticated models; but for two unrelated forecasters, we rarely expect the strong null to be true.) In contrast, our e-processes test whether one forecaster dominates the other _on average_ over time (thus requiring consistent outperformance), and the CSs can even test such averaged nulls in a two-sided fashion (equivalently, it tests both one-sided nulls). We examine this distinction further in Sections 4.4 and 5.3; other methodological differences are summarized in Section H.1. 

Table 2 summarizes the aforementioned methods of forecast comparison in terms of whether they have a stopping time (or equivalently, time-uniform; see Section 4.4 for further details) guarantee, a non-asymptotic guarantee, and a distribution-free guarantee. 

**Time-Uniform Confidence Sequences.** Confidence sequences were developed by Robbins and coauthors (Darling and Robbins, 1967; Robbins, 1970; Robbins and Siegmund, 1970; Lai, 1976a). Recent renewed interests on CSs are partly due to best-arm identification in multi-armed bandits (Jamieson et al., 2014; Jamieson and Jain, 2018), where CSs are sometimes referred to as always-valid or anytime confidence intervals. CSs are also duals to sequential hypothesis tests, analogously to CIs being dual to fixed-time hypothesis tests, and one can further derive a sequence of e-processes and p-processes given the CSs (more precisely, its underlying exponential process) (Ramdas et al., 2022). In Section 4.4, we make this connection explicit and discuss how our approach also leads to p-processes, or anytime-valid p-values (Johari et al., 2022), for weak nulls. 

The recent work by Howard et al. (2021) is of particular importance in our paper, as it develops tight CSs that are uniformly valid over time under nonparametric assumptions and has widths that shrink to zero. This work and its underlying technique of developing exponential test (super)martingales (Howard et al., 2020; Darling and Robbins, 1967; Ville, 1939) have led to several interesting results, including state-of-the-art concentration inequalities for IID mean estimation (WaudbySmith and Ramdas, 2023) and sequential quantile estimation (Howard and Ramdas, 2022). Our work makes the connection between the empirical Bernstein (EB) CSs derived in Howard et al. (2021) and the martingale property of forecast score differentials (Lai et al., 2011), leading to a novel sequential inference procedure for forecaster comparison. 

## **3 Preliminaries** 

### **3.1 Test Supermartingales, Ville’s Inequality, and Confidence Sequences** 

The theory of martingales and their interpretation as a gambler’s wealth in a betting game are instrumental in deriving SAVI methods. See Ramdas et al. (2023) for a comprehensive introduction. Let 

> 3This distinction of strong and weak nulls come from the discussion of randomized experiments in causal inference; see, e.g., Lehmann (1975); Rosenbaum (1995). Within the context of forecast comparison, Ehm and Krüger (2018) distinguish between tests of average and step-by-step conditional predictive ability, which mirrors that of weak and strong nulls. 

6 

|**Method & Key Result**|**Null Hypothesis**_H_0|**Weak**|**CI**|**SAVI**|**NA**|**DF**|
|---|---|---|---|---|---|---|
|Diebold and Mariano(1995)<br>_√_<br>_n_( <sup>ˆ</sup>∆_n −δ_)⇝_N_(0_,_2_πfd_(0))|_δ_ = 0<br>|✗|✓|✗|✗|✗|
|Giacomini and White(2006)<br>_Tm_(<sup>ˆ</sup>∆_n_)⇝_χ_<sup>2</sup><br>(_m_: max. forecastingwindow)|E_n−_1[<sup>ˆ</sup>_δm,n_] = 0_, ∀n_|✗|✗|✗|✗|✗|
|Lai et al.(2011)<br>_√_<br>_n_( <sup>ˆ</sup>∆_n −_∆_n_)_/sn_ ⇝_N_(0_,_1),<br>_sn ≤_<br>1<br>4_n_<br>�_n_<br>_i_=1<sup>[</sup><sup>_δi_(1)</sup><sup>_−δi_(0)]2</sup>|1<br>_n_<br>�_t_<br>_i_=1 <sup>E</sup><sup>_i−_1[ˆ</sup><sup>_δi_] = 0</sup><sup>_, ∀n_</sup><br>|✓|✓|✗|✓|✗|
|Henzi and Ziegel(2022)<br>_Et_ = <sup>�</sup><sup>_t_</sup><br>_i_=1<br>�<br>1 +_λ_<br>_δi_(_yi_)<br>_δi_(1(_pi>qi_))<br>�<br>is an e-process,_λ >_0|E_t−_1[<sup>ˆ</sup>_δt_]_≤_0_, ∀t_|✗|✗|✓|✓|✓|
|Ours<br>_t_(<sup>ˆ</sup>∆_t −_∆_t_)is sub-exponential,<br>which yields a CS & an e-process|1<br>_t_<br>�_t_<br>_i_=1 <sup>E</sup><sup>_i−_1[ˆ</sup><sup>_δi_]</sup><sup>_≤_0</sup><sup>_, ∀t_</sup>|✓|✓|✓|✓|✓|



Table 2: Inference methods for comparing probability forecasts for binary outcomes. This table is meant to be a quick summary only; see each referenced paper for the precise definitions, conditions, and guarantees for the method. The last two methods are the only ones that are anytime-valid, nonasymptotic, and distribution-free — both of which develop e-processes. Among the two, only our method tests the weak null and provides a CS for _estimating_ ∆ _t_ . **Notations:** for each _t ∈_ N, _pt_ and _qt_ are two probability forecasts on the outcome _yt_ ; _δt_ ( _y_ ) = _S_ ( _pt, y_ ) _− S_ ( _qt, y_ ); _δ_<sup>ˆ</sup> _t_ = _δt_ ( _yt_ ); ˆ∆ _t_ = _t_<sup>_−_1 �</sup><sup>_t_</sup> _i_ =1<sup>_δ_ˆ</sup><sup>_i_; ∆</sup><sup>_t_=</sup><sup>_t−_1 �</sup><sup>_t_</sup> _i_ =1<sup>E</sup><sup>_i−_1[ˆ</sup><sup>_δi_].We also use</sup><sup>_t_to refer to a time index varying over time,</sup> and _n_ to denote a fixed sample size that must be determined before the experiment. **Weak** : whether the method tests a weak null involving a time-varying average. **CI** : whether the method provides a confidence interval for the score difference (as opposed to only deriving a test). **SAVI** : whether inference is valid at arbitrary data-dependent stopping times (as opposed to only fixed times). **NA** : whether the method has a nonasymptotic guarantee. **DF** : whether the method has a distribution-free guarantee (as opposed to requiring distributional assumptions like stationarity/mixing/IID). 

( _X , G_ ) be a measurable space equipped with a filtration G := ( _Gt_ )<sup>_∞_</sup> _t_ =0<sup>, where each</sup><sup>_Gt_represents the</sup> accumulated information up to time _t_ . Given any probability distribution _P_ on ( _X , G_ ), a sequence of random variables ( _Xt_ )<sup>_∞_</sup> _t_ =0<sup>is called a</sup><sup>_process_if it is</sup><sup>_adapted_to G, meaning that</sup><sup>_Xt_is</sup><sup>_Gt_-measurable</sup> for all _t_ . A process is also _predictable_ w.r.t. G if _Xt_ is _Gt−_ 1-measurable for all _t ≥_ 1. A _stopping time τ_ w.r.t. G is a nonnegative integer random variable that satisfies _{τ ≤ t} ∈Gt_ for all _t ≥_ 1. Let E _t−_ 1[ _·_ ] = E _P_ [ _· | Gt−_ 1] denote the conditional expectation w.r.t. _Gt−_ 1 under _P_ . A process ( _Lt_ )<sup>_∞_</sup> _t_ =0<sup>is a</sup><sup>_supermartingale_if E</sup><sup>_P_[</sup><sup>_|Lt|_]</sup><sup>_< ∞_and E</sup><sup>_t−_1[</sup><sup>_Lt_]</sup><sup>_≤Lt−_1 for each</sup><sup>_t ≥_1, and a</sup><sup>_martingale_</sup> “ ” “ if _≤_ is replaced with =”. A nonnegative supermartingale ( _Lt_ )<sup>_∞_</sup> _t_ =0<sup>thatstartsatone(</sup><sup>_L_0=1)is</sup> called a _test supermartingale_ (for _P_ ) (Shafer et al., 2011). If ( _Lt_ )<sup>_∞_</sup> _t_ =0<sup>is a test supermartingale for</sup><sup>_P_,</sup> then Ville’s inequality (Ville, 1939) states that, for any _α ∈_ (0 _,_ 1), 



Ville’s inequality is the primary tool for constructing confidence sequences, as illustrated in, e.g., Howard et al. (2021); in fact, it is the only admissible way to construct them (Ramdas et al., 2020). Given _α ∈_ (0 _,_ 1), a (1 _−α_ )- _confidence sequence (CS)_ for a time-varying sequence of target parameters 

7 





In particular, the guarantee remains valid at arbitrary stopping times and without a prespecified sample size, so that collecting additional data over time does not invalidate it (Howard et al., 2021, Lemma 3): 



This coverage guarantee at stopping times is sometimes referred to as being _anytime-valid_ . This crucially differentiates a CS from a fixed-time CI, _Cn_ , which only has the following weaker guarantee: 



In short, CSs, as opposed to CIs, are the appropriate tools for sequential inference. 

### **3.2 Forecast Evaluation via Scoring Rules** 

Let _Y_ be the space of all possible outcomes equipped with a _σ_ -field _G_ . Let ∆( _Y_ ) be the set of all probability distributions on ( _Y, G_ ) and _P ⊆_ ∆( _Y_ ). To facilitate our discussion, the primary working example in this paper will be the space of binary outcomes _Y_ = _{_ 0 _,_ 1 _}_ and probability forecasts parametrized by their means in _P_ = [0 _,_ 1]. But our setup can be generalized to any finite sample space _Y_ = _{_ 1 _, . . . , K}_ with _K_ -dimensional probability forecasts _P_ = ∆<sup>_K−_1</sup> , for _K ≥_ 2, and _d_ - dimensional sample space _Y ⊆_ R<sup>_d_</sup> , for _d ≥_ 1, with point (e.g., mean and quantile) or probabilistic (e.g., CDF) forecasts. (We defer our discussion of these general cases to Section G.) 

A _scoring rule_ is any extended real-valued function<sup>4</sup> _S_ : _P × Y →_ R and can be used to evaluate the performance of a (probabilistic) forecast _p ∈P_ given an observation _y ∈Y_ . Following Gneiting and Raftery (2007), we take scoring rules to be _positively oriented_ , meaning that higher scores reflect better forecasts. A prominent example is the Brier score (Brier, 1950), which in the binary case can be expressed as _S_ ( _p, y_ ) = 1 _−_ ( _p − y_ )<sup>2</sup> for _p ∈_ [0 _,_ 1] and _y ∈{_ 0 _,_ 1 _}_ . 

Given a forecast _p ∈P_ and a probability distribution _q ∈_ ∆( _Y_ ), we can naturally extend the definition of a scoring rule _S_ to its _expected score_ w.r.t. _y ∼ q_ (conditional on _p_ ): 



Here, we make the distinction between the scoring rule _S_ on _P × Y_ and its expected score _S_ defined on _P ×_ ∆( _Y_ ) by the notations _S_ ( _p, y_ ) and _S_ ( _p_ ; _q_ ), respectively. We can recover the scoring rule from the expected score definition via _S_ ( _p, y_ ) = _S_ ( _p_ ; _δy_ ), where _δy_ is a point measure on _y_ . 

A scoring rule _S_ is _proper_ if any probability _q ∈_ ∆( _Y_ ) maximizes the expected score _S_ ( _·_ ; _q_ ): 



_S_ is _strictly proper_ if the argmax in (6) is unique. Intuitively, a proper scoring rule encourages forecasters to be honest, because if a forecaster believes that the outcome follows the distribution _q ∈P_ , then they are incentivized to honestly forecast _q_ , instead of any other distribution _p_ = _q_ , as _q_ maximizes the expected score (uniquely, if _S_ is strictly proper) according to their belief. Proper 

> 4More formally, the scoring rule _S_ is required to be _P-quasi-integrable_ in its second argument, meaning that for every _p ∈P_ , _S_ ( _p, ·_ ) is measurable and, for all _q ∈P_ , the integral � _Y_<sup>_S_(</sup><sup>_p, y_)</sup><sup>_dq_(</sup><sup>_y_)existsasapossiblyinfinitebutnot</sup> indeterminate value (Bauer, 2001; Abernethy and Frongillo, 2012). 

8 

scoring rules are often considered as the primary means of evaluating probabilistic forecasts, as they assess both calibration and sharpness (Winkler et al., 1996; Gneiting et al., 2007). 

Classical examples of proper scoring rules for probability forecasts _p ∈P_ = [0 _,_ 1] on binary outcomes _y ∈Y_ = _{_ 0 _,_ 1 _}_ include the following: 

- The Brier score or the quadratic score (Brier, 1950): _S_ ( _p, y_ ) = 1 _−_ ( _p − y_ )<sup>2</sup> . 

- The spherical score (Good, 1971): _S_ ( _p, y_ ) =<sup>_<u>py</u>_</sup><sup><u>+(1</u></sup><sup>_−p_</sup><sup><u>)(1</u></sup><sup>_−y_</sup><sup><u>)</u></sup> 

   - _~~√~~ p_<sup>2</sup> +(1 _−p_ )<sup>2.</sup> 

- The logarithmic score (Good, 1952): _S_ ( _p, y_ ) = _y_ log( _p_ ) + (1 _− y_ ) log(1 _− p_ ). 

- The zero-one score or the success rate: _S_ ( _p, y_ ) = _y_ 1 ( _p ≥_ 0 _._ 5) + (1 _− y_ )1 ( _p <_ 0 _._ 5). 

The Brier, spherical, and logarithmic scores are examples of strictly proper scoring rules, while the zero-one score is an example of a proper but not strictly proper scoring rule. An example of an improper scoring rule for probability forecasts is the absolute score, _S_ ( _p, y_ ) = 1 _−|p − y|_ . Also note that all of the examples except the logarithmic score are bounded for _p ∈_ [0 _,_ 1] and _y ∈{_ 0 _,_ 1 _}_ . 

## **4 Anytime-Valid Inference for Average Forecast Score Differentials** 

In this section, we derive CSs and e-processes, as well as their corresponding sequential tests and p- processes, for the time-varying average difference in the quality of forecasts, as measured by a scoring rule. Our intuition comes from the extensive literature on evaluating and comparing probability forecasts via scoring rules (Winkler et al., 1996; Gneiting and Raftery, 2007; DeGroot and Fienberg, 1983; Schervish, 1989; Gneiting, 2011; Lai et al., 2011), combined with the powerful tool of time-uniform CSs (Darling and Robbins, 1967; Howard et al., 2021). For now, our working example in this section will be the case of comparing probability forecasts on binary outcomes; we further discuss extensions to categorical and certain continuous outcomes in Section G. 

### **4.1 A Game-Theoretic Formulation** 

The intuition behind our SAVI methods for forecast score differentials comes from the game-theoretic statistical framework (Shafer, 2021; Ramdas et al., 2023). Consider a forecasting game where two players make probabilistic forecasts on an event that happens over time (e.g., whether it will rain on each day, whether a sports team will win its game each week, and more) and an unknown player named reality chooses a sequence of distributions that generates the outcomes that the forecasters are trying to predict. Let _t_ = 1 _,_ 2 _, . . ._ denote each round of the game. Though not required, we can also optionally allow having any historical data _y−_ ( _H−_ 1) _, . . . , y−_ 1 _, y_ 0 for some _H ≥_ 0. The forecasting game can be formulated in general as follows — the case of probability forecasts on binary outcomes is obtained by setting _P_ = ∆( _Y_ ) = [0 _,_ 1] ( _yt ∼ rt_ would refer to _yt ∼_ Bernoulli( _rt_ )). 

**Game 1** (Comparing Sequential Forecasters) **.** For rounds _t_ = 1 _,_ 2 _, . . ._ : 

1. Forecasters 1 and 2 make their forecasts, _pt, qt ∈P_ , respectively. _The order in which the forecasters make their forecasts is not specified._ 

2. Reality chooses _rt ∈_ ∆( _Y_ ). _rt is not revealed to the forecasters._ 

3. _yt ∼ rt_ is sampled and revealed to the forecasters. 

We now elaborate on the role of each player in Game 1. 

9 

**Forecasters 1 & 2.** At each round _t_ , the two forecasters can make their forecasts using any information available to them. This includes historical and previous outcomes _y−_ ( _H−_ 1) _, . . . , y_ 0 _, y_ 1 _, . . . , yt−_ 1, any of the previous forecasts made, _p_ 1 _, . . . , pt−_ 1, _q_ 1 _, . . . , qt−_ 1, as well as any other side information available to either forecaster. They cannot, however, make their predictions using any of _r_ 1 _, . . . , rt_ ’s (or information from the future). For example, when predicting the outcome of the next baseball game, the forecasters’ filtration may include not only all of previous games’ results but also any side information that either forecaster may have, such as which players are starting the game and whether there are injuries. The setup also allows for the case where two forecasters have different side information, as our results are completely agnostic to such details. 

This game-theoretic framework for forecast comparison is _prequential_ (Dawid, 1984), in the sense that we put no restrictions on how these forecasts are generated, and we only evaluate forecasters based on the forecasts they did make and the outcomes that did occur, as opposed to forecasts they would have made had the outcomes been different. 

**Reality.** In our game, Reality is the player that determines the unknown distribution _rt_ of the eventual outcome _yt_ conditioned on its past, which notably includes the forecasters’ choices _pt_ and _qt_ . In the binary case, for example, Reality chooses the conditional mean sequence of the outcomes _yt_ given everything it has seen. Reality can essentially choose _rt_ “however they want,” and they can even choose _rt_ after seeing _pt_ or _qt_ . Put differently, the framework is agnostic to what information Reality sees: Reality may only see its past choices _r_ 1 _, . . . , rt−_ 1 and (optionally) the past outcomes _y_ 1 _, . . . , yt−_ 1, or it may act adversarially after seeing _pt_ and _qt_ . In particular, _rt_ could also be a point distribution at _yt_ . 

We note that the distribution-free property of our methods corresponds to the fact that the game places no distributional assumptions on the time-varying dynamics of ( _rt_ )<sup>_∞_</sup> _t_ =1<sup>,suchasstationarity,</sup> Markovian or other conditional independence assumptions. 

**The Statistician.** The statistician, who stands outside of the game, has the goal of comparing the predictive performance of the two forecasters according to a chosen scoring rule and based only on the observed data ( _pt, qt, yt_ )<sup>_∞_</sup> _t_ =1<sup>,withoutmakinganyassumptionsaboutthebehaviorofanyplayer</sup> involved.<sup>5</sup> The statistician may choose to update their inferential conclusions as the game progresses. How the statistician achieves such a goal will be the focus of the subsequent sections. 

### **4.2 The Measure-Theoretic Setup** 

We now formalize Game 1 in the context of comparing the two probabilistic forecasters over time. Let ( _pt_ )<sup>_∞_</sup> _t_ =1<sup>and (</sup><sup>_qt_)</sup><sup>_∞_</sup> _t_ =1<sup>be two sequences of forecasts in</sup><sup>_P_, for a sequence of outcomes (</sup><sup>_yt_)</sup><sup>_∞_</sup> _t_ =1<sup>in</sup><sup>_Y_.In</sup> the binary case, the forecasts will take values in _P_ = [0 _,_ 1] and the outcomes in _Y_ = _{_ 0 _,_ 1 _}_ . We can define Game 1 in a measure-theoretic sense by specifying the associated filtrations, i.e., a sequence of “information sets” with which we perform inference. Our formulation is closely related to the setup of Lai et al. (2011), although we make the game-theoretic intuitions explicit. 

**The “Observable” Forecaster Filtration** F **.** We first define the filtration with which the two forecasters generate their forecasts, denoted as F := ( _Ft_ )<sup>_∞_</sup> _t_ =0<sup>.Foreach</sup><sup>_t≥_1,let</sup><sup>_Ft−_1represent</sup><sup>_any_</sup> information available to the forecasters before making their predictions at time _t_ , as described in the 

> 5Specifically, we do not explicitly consider strategic issues arising from (say) the choice of the scoring rule or the method of comparison. In other words, we consider the comparison problem separately from the elicitation problem (how to elicit honest forecasts). A separate line of work considers these important, but orthogonal, issues. 

10 

previous subsection. Mathematically, this means that ( _pt_ )<sup>_∞_</sup> _t_ =1<sup>, (</sup><sup>_qt_)</sup><sup>_∞_</sup> _t_ =1<sup>, and (</sup><sup>_yt_)</sup><sup>_∞_</sup> _t_ =1<sup>are adapted w.r.t. F.</sup> Note that F also includes the information available to the statistician, making this the “observable” filtration that contrasts with the “oracle” filtration (defined below). 

**The “Oracle” Game Filtration** G **.** The game filtration, denoted as G := ( _Gt_ )<sup>_∞_</sup> _t_ =0<sup>,represents</sup><sup>_all_</sup> sets of information associated with Game 1. The parameter of interest (unknown to the statistician) is defined w.r.t. this “oracle” filtration. More precisely, for each _t ≥_ 1, _Gt−_ 1 includes not only everything in _Ft−_ 1 but also any information available to Reality before the outcome _yt_ is realized, including Reality’s choice _rt_ . Mathematically, this implies that ( _pt_ )<sup>_∞_</sup> _t_ =1<sup>,(</sup><sup>_qt_)</sup><sup>_∞_</sup> _t_ =1<sup>,and(</sup><sup>_rt_)</sup><sup>_∞_</sup> _t_ =1<sup>are</sup><sup>_predictable_</sup> w.r.t. G, while ( _yt_ )<sup>_∞_</sup> _t_ =1<sup>is adapted w.r.t. G. The setup allows for the flexible choices of Reality described</sup> in the previous subsection, as it does not preclude Reality’s actions in any way. 

In the remainder of the paper, we use the notation E _t−_ 1[ _·_ ] = E [ _· | Gt−_ 1] to denote the conditional expectation with respect to the game filtration for each _t_ . In the case of binary (and categorical) outcomes, because the outcome distribution is completely specified by their mean, we simply let _rt_ denote the (unknown) conditional mean of the outcome _yt_ given _Gt−_ 1 for each _t_ , with a slight abuse of notation. In such cases, we have that 



where E _t−_ 1 refers to the conditional expectation over _yt ∼ rt | Gt−_ 1. 

**Comparing Sequential Forecasters via Average Forecast Score Differentials.** With the aforementioned setup, we can now use scoring rules to assess and compare the quality of the two forecasters over time. We define the **_average (forecast) score differential_** ∆ _t_ between the sequences of forecasts ( _pi_ )<sup>_∞_</sup> _i_ =1<sup>and (</sup><sup>_qi_)</sup><sup>_∞_</sup> _i_ =1<sup>, up to time</sup><sup>_t_, as the average difference in</sup><sup>_expected scores_:</sup> 



where E _i−_ 1 denotes the expectation over _yi ∼ ri conditioned on_ the game filtration _Gi−_ 1, which includes both forecasts _pi_ and _qi_ as well as _ri_ . The time-varying parameter ∆ _t_ provides an intuitive way of quantifying the difference in the quality of forecasts made up to time _t_ . We highlight that ∆ _t_ helps us infer whether one forecaster is better than the other _on average_ (over time), as opposed to one strictly dominating the other (Giacomini and White, 2006; Henzi and Ziegel, 2022). This estimand is also used in Lai et al. (2011)’s asymptotic CI. 

The parameter ∆ _t_ is not observable to the statistician or the forecasters, because reality’s moves _r_ 1 _, . . . , rt_ are unknown and never observed. We thus define the **_empirical average (forecast) score differential_** ∆<sup>ˆ</sup> _t_ as the unbiased estimate of each summand in (8), also averaged over time: 



ˆ∆ _t_ is completely observable to the statistician after time _t_ . 

The statistician’s goal then becomes quantifying how far ∆<sup>ˆ</sup> _t_ is from ∆ _t_ , while accounting for the uncertainty associated with sampling _yt_ at each time _t_ . To this end, we define the _pointwise (forecast) score differential δi_ := E _i−_ 1[ _S_ ( _pi, yi_ ) _− S_ ( _qi_ ; _yi_ )] and its empirical counterpart _δ_<sup>ˆ</sup> _i_ := _S_ ( _pi, yi_ ) _− S_ ( _qi, yi_ ). Then, it is immediate that the cumulative sums of deviations, defined by _S_ 0 = 1 and 



11 

forms a martingale, i.e., E _t−_ 1[ _St_ ] = _St−_ 1 _, ∀t ≥_ 1. Previous work including Seillier-Moiseiwitsch and Dawid (1993); Lai et al. (2011) use this property to derive the asymptotic normality of empirical average score differentials. In the following sections, we illustrate how ( _St_ )<sup>_∞_</sup> _t_ =0<sup>canfurtherbe</sup> uniformly and non-asymptotically bounded by constructing _exponential_ test supermartingales. As a result, we will be able to estimate and cover ∆ _t_ using CSs and also test its sign using e-processes. 

### **4.3 Time-Uniform Confidence Sequences for Average Score Differentials** 

#### **4.3.1 Time-Uniform Boundaries and Exponential Test Supermartingales** 

We now show that we can uniformly bound the difference between ∆<sup>ˆ</sup> _t_ and ∆ _t_ over time using uniform boundaries and test supermartingales. To do this, we start with a _cumulative sum_ process _St_ := _t_ � _i_ =1<sup>(ˆ</sup><sup>_δi−δi_)aswellasits</sup><sup>_intrinsictimeV_ˆ</sup><sup>_t_,whichisthevarianceprocessfor</sup><sup>_St_(tobedefined</sup> later). Our goal is then to uniformly bound the sum _St_ over the intrinsic time _V_<sup>ˆ</sup> _t_ , which corresponds to bounding the difference between ∆<sup>ˆ</sup> _t_ and ∆ _t_ over time due to (10). 

Following Howard et al. (2020), for any sum process ( _St_ )<sup>_∞_</sup> _t_ =0<sup>anditsintrinsictimes( ˆ</sup><sup>_Vt_)</sup><sup>_∞_</sup> _t_ =0<sup>,we</sup> define a _(one-sided) uniform boundary u_ = _uα with crossing probability α ∈_ (0 _,_ 1) as any function of the intrinsic time that gives a time-uniform bound on the sums: 



that is, with probability at least 1 _− α_ , the sums _St_ are upper-bounded by _u_ ( _V_<sup>ˆ</sup> _t_ ) _at all times t_ . By similarly computing a uniform boundary to ( _−St, V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>,wecanalsoobtainatime-uniformlower</sup> bound on _St_ . (Alternatively, we can directly define a _two-sided_ sub- _ψ_ uniform boundary, which satisfies _P_ ( _∀t ≥_ 1 : _−uα_ ( _V_<sup>ˆ</sup> _t_ ) _≤ St ≤ uα_ ( _V_<sup>ˆ</sup> _t_ )) _≥_ 1 _− α_ . An example is Robbins (1970)’s two-sided normal mixture that we describe in Section 4.3.4.) The upper and lower bounds then jointly form a time-uniform CS on (∆ _t_ )<sup>_∞_</sup> _t_ =1<sup>by rearranging the terms.</sup> 

How do we show that there exists such a uniform boundary for our definitions of ( _St, V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>?</sup> Howard et al. (2020, 2021) show that there exists such a uniform boundary if, for each _λ ∈_ [0 _, λ_ max), the _exponential process_ defined by _L_ 0( _λ_ ) = 1 and 



is a test supermartingale w.r.t. G. Here, _ψ_ : [0 _, λ_ max) _→_ R is a “CGF-like” function (Howard et al., 2020ˆ ), with a scale parameter _c >_ 0, that controls how fast _St_ can grow relative to the intrinsic time _Vt_ . It is called a “CGF-like” function because it closely resembles (or equals) a cumulant generating function (CGF) of a mean-zero random variable. In this paper, we use two _ψ_ functions: 

- _ψN,c_ ( _λ_ ) = _c_<sup>2</sup> _λ_<sup>2</sup> _/_ 2 _, ∀λ ∈_ [0 _, ∞_ ), which is the CGF of a centered Gaussian with variance _c_<sup>2</sup> ; 

- _ψE,c_ ( _λ_ ) = _c_<sup>_−_2</sup> ( _−_ log(1 _− cλ_ ) _− cλ_ ) _, ∀λ ∈_ [0 _,_ 1 _/c_ ), which is a rescaled CGF of a centered Exponential with scale _c_ . 

If _Lt_ ( _λ_ ) is a test supermartingale for each _λ ∈_ [0 _, λ_ max) for some _ψ_ , then we say that ( _St_ )<sup>_∞_</sup> _t_ =0<sup>is</sup><sup>_sub-ψ_</sup> _with variance process_ ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>.In particular, we say that (</sup><sup>_St_)</sup><sup>_∞_</sup> _t_ =0<sup>is sub-Gaussian or sub-exponential,</sup> with variance process ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>and scale</sup><sup>_c_, if it is sub-</sup><sup>_ψN,c_or sub-</sup><sup>_ψE,c_respectively; these generalize</sup> the definitions of sub-Gaussian and sub-exponential random variables to cumulative sums w.r.t. intrinsic time. The uniform boundary _u_ defined using _ψ_ is then called a _sub-ψ uniform boundary_ . 

Our goal is now to identify the conditions with which ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>is indeed a test supermartingale</sup> and use different _ψ_ functions to obtain different uniform boundaries and hence CSs. 

12 

#### **4.3.2 Warmup: Hoeffding-Style Confidence Sequences** 

We first derive an illustrative example of a CS for ∆ _t_ solely based on the sub-Gaussianity of the empirical pointwise score differentials ( _δ_<sup>ˆ</sup> _i_ )<sup>_∞_</sup> _i_ =1<sup>.WhiletheresultingCSisnotthetightestoneinour</sup> case, its derivation is simple enough to showcase the general pipeline for deriving CSs. 

Recall the problem setup in Section 4.2, and for each _i ≥_ 1, consider two probability forecasts _pi, qi ∈_ [0 _,_ 1] on a binary outcome _yi ∈{_ 0 _,_ 1 _}_ with unknown mean _ri ∈_ [0 _,_ 1]. Since _pi_ , _qi_ , and _yi_ are all bounded, we know that the pointwise score differentials _δ_<sup>ˆ</sup> _i_ for _i ≥_ 1 are also bounded for many of the scoring rules we’ve discussed (e.g., _|δ_<sup>ˆ</sup> _i| ≤_ 1 for the Brier, spherical, and zero-one scores). If _|δ_<sup>ˆ</sup> _i| ≤ c_ for some _c >_ 0, we know that _δ_<sup>ˆ</sup> _i_ is _c_ -sub-Gaussian (Hoeffding, 1963) conditioned on the game filtration _Gi−_ 1, meaning that E _i−_ 1[ _e_<sup>_λ_(ˆ</sup><sup>_δi−δi_)</sup> ] _≤ e_<sup>_λ_2</sup><sup>_c_2</sup><sup>_/_2</sup> = exp _{ψN,c_ ( _λ_ ) _}_ for all _λ ∈_ R. Now, for each _t_ , define the cumulative sum _St_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi−δi_)andtheintrinsictime</sup><sup>_V_ˆ</sup><sup>_t_=</sup> _t_ � _i_ =1<sup>1=</sup><sup>_t_.It then follows that,for each</sup><sup>_λ∈_[0</sup><sup>_, ∞_),the exponential process (</sup><sup>_Lt_(</sup><sup>_λ_))</sup><sup>_∞_</sup> _t_ =0<sup>given by</sup> _Lt_ ( _λ_ ) = exp _{λSt − ψN,c_ ( _λ_ ) _V_<sup>ˆ</sup> _t}_ is a test supermartingale: 



Hence, there exists a sub-Gaussian uniform boundary for ( _St, V_<sup>ˆ</sup> _t_ ) such that the time-uniform guarantee in (11) holds. By rearranging terms and also using the analogous argument for ( _−St, V_<sup>ˆ</sup> _t_ ), we arrive at our first CS. Hereafter, the notation ( _a ± b_ ) denotes the interval ( _a − b, a_ + _b_ ). 

**Theorem 1** (Hoeffding-style confidence sequences for ∆ _t_ ) **.** _Suppose that δ_<sup>ˆ</sup> _i is c-sub-Gaussian conditioned on Gi−_ 1 _for i ≥_ 1 _, for some c ∈_ (0 _, ∞_ ) _. Then, for any α ∈_ (0 _,_ 1) _,_ 



_where u_ = _uα/_ 2 _,c is any (one-sided) sub-Gaussian uniform boundary with crossing probability_<sup>_<u>α</u>_</sup> 2<sup>_and_</sup> _scale c (or alternatively, a two-sided version with crossing probability α and scale c)._ 

The statement (14) is equivalent to saying that, with probability at least 1 _− α_ , ∆ _t_ is contained in _Ct_<sup>H</sup><sup>_for all time t_, or that</sup><sup>_P_(</sup><sup>_∀t≥_1:∆</sup><sup>_t∈C_</sup> _t_<sup>H)</sup><sup>_≥_1</sup><sup>_−α_.This CS is called a Hoeffding-style CS, as</sup> it extends Hoeffding (1963)’s inequality for the sums of independent sub-Gaussian random variables to the sequential case. In the sub-Gaussian case, it is also possible to construct a two-sided boundary without separately constructing a one-sided boundary. This is due to a classical result by Robbins (1970) that we restate later in (17), so the upper and lower confidence bounds need not be constructed separately; in practice, the one-sided and two-sided variants are nearly identical (Howard et al., 2021). We further discuss the possible choices of the uniform boundary in Section 4.3.4. 

The condition for Theorem 1 (and for Theorem 2 that will follow shortly) is satisfied by many scoring rules for probability forecasts on binary or categorical outcomes, including the Brier, spherical, and zero-one scores. For the unbounded logarithmic score, one can use its truncated variant _S_ ( _p, y_ ) = _y_ log( _p ∨ ϵ_ ) + (1 _− y_ ) log((1 _− p_ ) _∨ ϵ_ ) for some small _ϵ >_ 0; although the score is no longer proper, our methods remain valid. The condition is also satisfied for scoring rules on bounded continuous outcomes, such as Brier and quantile scores on [0 _,_ 1]-valued outcomes (See Section G). 

#### **4.3.3 Main Result: Empirical Bernstein Confidence Sequences** 

Now we are ready to present our main result, which is the derivation of a tight CS for ∆ _t_ . The key difference from the Hoeffding-style CS is that we now use an empirical estimate of the variance pro- 

13 

cess for the cumulative sums, leading to a variance-adaptive CS that is often much tighter in practice.<sup>6</sup> Recall the problem setup in Section 4.2 once again. 

**Theorem 2** (Empirical Bernstein confidence sequences for ∆ _t_ ) **.** _Suppose that |δ_<sup>ˆ</sup> _i| ≤_ 2<sup>_<u>c</u>for each i ≥_1</sup><sup>_,_</sup> _for some c ∈_ (0 _, ∞_ ) _. Also, let V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −γi_)2</sup><sup>_, where_(</sup><sup>_γi_)</sup> _i_<sup>_∞_</sup> =1<sup>_is any_</sup> � _−_ 2<sup>_<u>c</u>,_</sup> 2<sup>_<u>c</u>_</sup> � _-valued predictable sequence w.r.t._ G _. Then, for any α ∈_ (0 _,_ 1) _,_ 



_where u_ = _uα/_ 2 _,c is any sub-exponential uniform boundary with crossing probability_<sup>_<u>α</u>_</sup> 2<sup>_and scale c._</sup> 

As before, the statement (15) is equivalent to saying that, with probability at least 1 _− α_ , ∆ _t_ is contained in _Ct_<sup>EB</sup> _for all time t_ , or that _P_ � _∀t ≥_ 1 : ∆ _t ∈ Ct_<sup>EB</sup> � _≥_ 1 _− α_ . The proof is provided in Section A.2. Theorem 2 (and its proof) can be viewed as an extension of Theorem 4 in Howard et al. (2021) to our setup of sequential forecast comparison. 

Like the Hoeffding-style CS in Theorem 1, the EB CS estimates the conditional predictive ability in an anytime-valid and distribution-free manner. The EB CS is further variance-adaptive because its width is a function of the empirical variance process ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>, and we illustrate this empirically in</sup> Section 5. As before, we can use any bounded scoring rules, which in the binary and categorical cases include the Brier, spherical, and zero-one scores (proper), as well as the truncated logarithmic score (improper); scoring rules for bounded continuous outcomes can similarly be used. In addition, for unbounded _proper_ scores for binary forecasts, such as the logarithmic score, we show in Section D that a normalized version of the average score differential, due to Winkler (1994), can be used. 

The choice of the uniform boundary _u_ is discussed in the following subsection. A reasonable choice for the predictable sequence ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>istheaverageofpreviousscoredifferentials,i.e.,</sup><sup>_γi_=</sup> ˆ∆ _i−_ 1, although a smarter choice may lead to tighter CS. For the rest of this paper, our default choice of CS for ∆ _t_ will be that of Theorem 2, using _V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −_ˆ∆</sup><sup>_i−_1)2, unless specified otherwise.</sup> 

#### **4.3.4 Choosing the Uniform Boundary via the Method of Mixtures** 

The specific choice of the uniform boundary _u_ controls the tightness of the CS across time, and an extensive list of choices for _u_ is covered in detail in Howard et al. (2021). While the simplest uniform boundaries are given as linear functions of the intrinsic time (Howard et al., 2020), curved uniform boundaries can produce CSs that are tighter across time. Here, we focus on a type of curved boundaries called the conjugate-mixture boundary; another option, called the polynomial stitching boundary, is also discussed in Section B.2. Either boundary type is applicable to both Theorems 1 and 2. 

The conjugate-mixture (CM) boundary (Howard et al., 2021), denoted as _u_<sup>CM</sup> _α_<sup>, represents a class</sup> of uniform boundaries arising from the method of mixtures, the first instance of which was derived by Darling and Robbins (1967). The key idea is summarized as follows. Since _Lt_ ( _λ_ ) = exp _{λSt − ψ_ ( _λ_ ) _V_<sup>ˆ</sup> _t}_ is a test supermartingale for every _λ ∈_ [0 _, λ_ max), it follows that for any distribution _F_ on [0 _, λ_ max), the mixture _L_<sup>mix</sup> _t_ := � _Lt_ ( _λ_ ) _dF_ ( _λ_ ) is also a test supermartingale. Choosing _F_ to be conjugate (in the Bayesian sense) to _ψ_ then gives a closed-form expression for _L_<sup>mix</sup> _t_ . For example, if ( _St_ )<sup>_∞_</sup> _t_ =0<sup>issub-Gaussianwith( ˆ</sup><sup>_Vt_)</sup><sup>_∞_</sup> _t_ =0<sup>(Theorem1),thenchoosing</sup><sup>_F_tobeaGaussian</sup> results in the _normal mixture_ boundary (Robbins, 1970); if ( _St_ )<sup>_∞_</sup> _t_ =0<sup>issub-exponentialwith( ˆ</sup><sup>_Vt_)</sup><sup>_∞_</sup> _t_ =0 (Theorem 2), then choosing _F_ as a Gamma results in a _gamma-exponential mixture_ boundary. 

> 6The improvement from a Hoeffding-style CS to an empirical Bernstein CS mirrors the improvement from Hoeffding’s inequality to empirical Bernstein’s inequality for bounded random variables in the fixed-sample case. 

14 

|**Type**|**CS**_Ct_|**Intrinsic Time** <sup>ˆ</sup>_Vt_|**Uniform Boundary**_u_|
|---|---|---|---|
|**Hoeffding-Style**|�<br>ˆ∆_± _<sup>_u_( ˆ</sup><sup>_Vt_)</sup><br>�|_t_|Normal Mixture|
|(Theorem1)|_t  _<br>_t_<br>||Polynomial Stitching|
|**Emp. Bernstein**|�<br>ˆ∆_± _<sup>_u_( ˆ</sup><sup>_Vt_)</sup><br>�|�_t_<br>_i_=1<sup>(ˆ</sup><sup>_δi −γi_)2,</sup>|Gamma-Exponential Mixture|
|(Theorem2)|_t  _<br>_t_<br>|(_γi_)<sup>_∞_</sup><br>_i_=1 <sup>predictable</sup>|Polynomial Stitching|



Table 3: Summary of confidence sequences and their uniform boundary choices. 

To elaborate, by Lemma 2 of Howard et al. (2021), if _Lt_ ( _λ_ ) = exp _{λSt − ψ_ ( _λ_ ) _V_<sup>ˆ</sup> _t}_ is a test supermartingale for each _λ ∈_ [0 _, λ_ max) and _F_ is any probability distribution on [0 _, λ_ max), then the following function is a sub- _ψ_ uniform boundary with crossing probability _α ∈_ (0 _,_ 1): 



where _m_ ( _s, v_ ) := � exp _{λs − ψ_ ( _λ_ ) _v} dF_ ( _λ_ ). Because _m_ ( _St, V_<sup>ˆ</sup> _t_ ) = _L_<sup>mix</sup> _t_ is a test supermartingale, Ville’s inequality says that _P_ ( _∀t ≥_ 1 : _m_ ( _St, V_<sup>ˆ</sup> _t_ ) _<_ 1 _/α_ ) _≥_ 1 _− α_ , which in turn implies that _P_ ( _∀t ≥_ 1 : _St ≤ u_<sup>CM</sup> _α_<sup>( ˆ</sup><sup>_Vt_))</sup><sup>_≥_1</sup><sup>_−α_.Similarly,if(</sup><sup>_−St,V_ˆ</sup><sup>_t_)</sup><sup>_∞_</sup> _t_ =0<sup>isalsosub-</sup><sup>_ψ_,thentheabove</sup> procedure also gives the lower bound on _St_ . 

Importantly, the uniform boundary (16) can be used for both Theorems 1 and 2, with the choice of _F_ differing in each case. For the Hoeffding-style CS in Theorem 1, a two-sided normal mixture boundary can be computed directly in closed-form by choosing _F_ to be _N_ (0 _, ρ_<sup>_−_1</sup> ) (Robbins, 1970): 



where _ρ >_ 0 is a free parameter. In practice, _ρ_ can be chosen to optimize the width of the resulting CS at a pre-specified intrinsic time. A one-sided normal mixture boundary can also be derived in closed-form (Howard et al., 2021). 

For the EB CS in Theorem 2, a one-sided gamma-exponential mixture boundary _u_<sup>CM</sup> _α_<sup>(</sup><sup>_v_;</sup><sup>_ψE_), with</sup> _F_ as a Gamma, can be computed efficiently using a numerical root finder ( _m_ ( _s, v_ ) has a closed form, and the boundary _u_<sup>CM</sup> _α_ is obtained numerically; see Section B.1 for details). The one-sided boundary can be used for computing both the upper and lower confidence bounds of the EB CS. If a closed-form boundary is needed, then the polynomial stitching boundary (Section B.2) can be used. Also, while the CM boundary has an asymptotic rate of _O_ (<sup>_√_</sup> _v_ log _v_ ) as illustrated in (17), it is usually tighter than the polynomial stitched boundary in practice. In fact, the CM boundary is unimprovable in the case of sub-Gaussian random variables without additional assumptions (Howard et al., 2021, Proposition 4). 

Table 3 summarizes the choice of uniform boundaries and the CSs we derived for estimating ∆ _t_ . In our experiments, we use the conjugate-mixture uniform boundary by default, although we also perform an empirical comparison between the different choices as well as their hyperparameters in Section I.4. We use the publicly available implementation of the polynomial stitching and CM uniform boundaries by Howard et al. (2021).<sup>7</sup> 

### **4.4 Sequential Tests, e-Processes and p-Processes** 

While our derivation so far has focused on CSs, we can also derive e-processes and p-processes (Shafer and Vovk, 2019; Vovk and Wang, 2021; Grünwald et al., 2023; Ramdas et al., 2020). In particular, 

> 7https://github.com/gostevehoward/confseq 

15 

an e-process can be derived as a lower bound on the exponential test supermartingale (12) that we used to construct the CS in the previous section. This correspondence is general to any exponential process upper-bounded by a test supermartingale, as noted in, e.g., Ramdas et al. (2020); Howard et al. (2021); our work utilizes this fact to introduce alternative sequential inference procedures with the same anytime-valid and distribution-free guarantees. 

**Weak and Strong Null Hypotheses.** Before deriving e- and p-processes, we first make clear the null hypotheses that correspond to the CS derived in Theorem 2. We define the _weak one-sided null H_ 0<sup>w(</sup><sup>_p, q_) as</sup> 



_H_ 0<sup>w(</sup><sup>_p, q_)impliesthat,acrossalltimes</sup><sup>_t_,thefirstforecaster(</sup><sup>_p_)isnobetterthanthesecondfore-</sup> caster ( _q_ ) _on average_ . Note that _H_ 0<sup>w(</sup><sup>_p, q_) is a composite null, in the sense that it consists of all joint</sup> distributions _P_ on G such that ∆ _t ≤_ 0 for all _t ≥_ 1 under _P_ . _H_ 0<sup>w(</sup><sup>_q, p_)isanalogouslydefinedas</sup> _H_ 0<sup>w(</sup><sup>_q, p_) : ∆</sup><sup>_t_=</sup><sup><u>1</u></sup> _t_ � _ti_ =1<sup>_δi≥_0.</sup> 

We now illustrate how the CSs derived in Theorem 1 and Theorem 2 would correspond to sequential tests of the weak one-sided nulls _H_ 0<sup>w(</sup><sup>_p, q_) and</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_q, p_), drawing from the duality between</sup> CSs and sequential tests (Johari et al., 2022; Howard et al., 2021; Ramdas et al., 2020). Specifically, because the upper and lower confidence bounds are often constructed separately, the (1 _− α_ )-level CS for ∆ _t_ denoted as _Ct_ = ( _Lt, Ut_ ) satisfies ∆ _t ≤ Ut_ with probability at least 1 _−_<sup>_<u>α</u>_</sup> 2<sup>_and_that ∆</sup><sup>_t≥Lt_</sup> with probability at least 1 _−_<sup>_<u>α</u>_</sup> 2<sup>.Thus,if for any time</sup><sup>_t_we find that</sup><sup>_Lt>_0 or</sup><sup>_Ut<_0,then we can</sup> reject either _H_ 0<sup>w(</sup><sup>_p, q_)or</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_q, p_)withhighprobability.Moregenerally,theCSsreadilyprovidea</sup> valid stopping rule for rejecting _H_ 0<sup>w, a fact that we summarize in the following corollary.Below, we</sup> follow Robbins’ power-one testing framework which uses one-sided stopping rules that only stop on rejecting the null (and do not stop otherwise). 

**Corollary 1** (A sequential test for _H_ 0<sup>wusing a CS)</sup><sup>**.**</sup><sup>_Given a_(1</sup><sup>_−α_)</sup><sup>_-CS Ct_= (</sup><sup>_Lt, Ut_)</sup><sup>_obtained using_</sup> _either Theorem 1 or 2, the following stopping rule provides a valid level-α sequential test for H_ 0<sup>w(</sup><sup>_p, q_)</sup> _and H_ 0<sup>w(</sup><sup>_q, p_)</sup><sup>_(jointly):_</sup> 



_This means that:_ 



The stopping rule (19) is equivalent to _deciding that p has been better (worse) than q if Ct is entirely above (below) zero._ The anytime-validity of this rule implies that the statistician can, e.g., periodically perform the test as _t_ increases and update their decision accordingly. On one extreme, the statistician can choose to perform the test after every round _t_ , or on the other extreme, they can test just once at a designated time _t_<sup>_∗_</sup> (while leaving open the possibility of revisiting the experiment some time later). Compared to a standard hypothesis test for a stationary mean, the underlying ∆ _t_ can change its course over time, so in general it may not be sufficient to test once at _t_<sup>_∗_</sup> in order to have power against the weak null. See Section 5 for an illustration and Section 6 for a further discussion. 

We note that separately testing for both _H_ 0<sup>w(</sup><sup>_p, q_) and</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_q, p_) is not equivalent to simply testing</sup> for ∆ _t_ = 0 _, ∀t_ , which is equivalent to _δt_ = 0 _, ∀t_ . Rather, the sequential test (19) is the combination of two separate sequential tests in (19) for _H_ 0<sup>w(</sup><sup>_p, q_) and</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_q, p_), each at the significance level</sup><sup>_α/_2. The</sup> 

16 

interpretation of the CS as two simultaneous sequential tests allows the user to continuously monitor the score differential on both sides via the CS-based stopping rule (19). 

For the sake of comparison, we also define the _strong one-sided null H_ 0<sup>s=</sup><sup>_H_</sup> 0<sup>s(</sup><sup>_p, q_) as</sup> 



_H_ 0<sup>s(</sup><sup>_q, p_) is defined analogously as</sup><sup>_H_</sup> 0<sup>s(</sup><sup>_q, p_):</sup><sup>_δt≥_0</sup><sup>_,∀t_=1</sup><sup>_,_2</sup><sup>_, . . ._.The recent work by Henzi and</sup> Ziegel (2022) develops e-processes (defined in the next paragraph) and sequential tests for this null. In contrast to _H_ 0<sup>w,</sup><sup>_H_</sup> 0<sup>scorrespondstosayingthatthefirstforecaster(</sup><sup>_p_)isnobetterthanthesecond</sup> forecaster ( _q_ ) at _every_ time step _t_ = 1 _,_ 2 _, . . ._ . Thus, the strong null _H_ 0<sup>simplies the weak null</sup><sup>_H_</sup> 0<sup>w, but</sup> not vice versa. The critical distinction here is that rejecting _H_ 0<sup>sonly tells us that</sup><sup>_p_outperformed</sup><sup>_q_at</sup> _some_ time step _t_ , but it does not tell us if either was better on average over time. To give a concrete example, fix _k >_ 2 (say, _k_ = 7 indicating Sundays), and define 



In other words, _p_ is generally worse than _q_ but marginally better than _q_ every _k_ th time step (e.g., every Sunday). Because the strong null is false, any (powerful) sequential test for the strong null will reject it, and yet this may be a confusing conclusion as _q_ is generally a better forecaster. 

**Sub-exponential E-processes for the Weak Null.** We now show that the exponential test supermartingale underlying the CS in Theorem 2 can also be transformed to directly measure evidence against the weak one-sided null (rather than make a decision at a level _α_ ). Formally, an _e-process_ (Ramdas et al., 2022) for a (possibly composite) null hypothesis _H_ 0 is defined as a nonnegative process ( _Et_ )<sup>_∞_</sup> _t_ =0<sup>, starting at one (</sup><sup>_E_0= 1), such that:</sup> 



where we define _E∞_ := lim sup _t→∞ Et_ . The larger the value of _Et_ , the more the evidence against the null. In particular, if the null is true, then it is unlikely to observe large values of the process at any stopping times (by Markov’s inequality, _P_ ( _Eτ ≥_ 1 _/α_ ) _≤ α_ ). An e-process is anytime-valid by definition (23) (validity at arbitrary stopping times), analogous to the anytime-validity of a CS in Equation 3, and the term ‘process’ is also used to emphasize this property. An e-process can also be interpreted in a fully game-theoretic statistical sense: an e-process for a composite null measures the _minimum_ wealth among bets against each member of the null (Ramdas et al., 2022), such that it only grows large when there is evidence against all members. At a fixed _t_ , _Et_ is also called an e-variable, and its realization is called an e-value (Vovk and Wang, 2021; Grünwald et al., 2023). 

We can now define and show an e-process that corresponds to Theorem 2. (We can also define an analogous e-process corresponding to Theorem 1, but this is omitted due to space constraints.) The following e-process is for the weak one-sided null _H_ 0<sup>w(</sup><sup>_p, q_)andisrelatedtothelowerconfidence</sup> bound of the CS from Theorem 2; the e-process for _H_ 0<sup>w(</sup><sup>_q, p_)isanalogousandrelatedtotheupper</sup> confidence bound of the CS. Recall once again the problem setup in Section 4.2. 

**Theorem 3** (Sub-exponential E-processes for _H_ 0<sup>w)</sup><sup>**.**</sup><sup>_Assume the same conditions as Theorem 2.Then,_</sup> _for each λ ∈_ [0 _,_ 1 _/c_ ) _,_ 



_Furthermore, given a probability distribution F on_ [0 _,_ 1 _/c_ ) _, the mixture process Et_<sup>_mix_</sup> := � _Et_ ( _λ_ ) _dF_ ( _λ_ ) _is an e-process for H_ 0<sup>w(</sup><sup>_p, q_)</sup><sup>_._</sup> 

17 

The proof, provided in Section A.3, shows that under each _P ∈H_ 0<sup>w,</sup><sup>_Et_(</sup><sup>_λ_)isupper-bounded</sup> by a exponential test supermartingale for _P_ , namely _Lt_ ( _λ_ ) in (12). Because a process is upperbounded by a test supermartingale for _P ∈H_ 0 if and only if it is an e-process for _H_ 0 (Ramdas et al., 2020), this establishes that _Et_ ( _λ_ ) is an e-process in the sense of (23). It then follows that _Et_<sup>mix</sup> _≤_ � _Lt_ ( _λ_ ) _dF_ ( _λ_ ) = _L_<sup>mix</sup> _t ∀t_ , so _Et_<sup>mix</sup> is also an e-process. The e-process of Theorem 3 is an anytime-valid inference procedure that provides a measure of accumulated evidence against the weak one-sided null _H_ 0<sup>w(</sup><sup>_p, q_) at any stopping time.By definition, it</sup> is expected to be small under the weak null, and we only expect to see it grow large when the weak null does not hold. In comparison with Henzi and Ziegel (2022)’s e-process for the _strong_ null, we see that our e-process provides a more useful notion of evidence for saying that one forecaster outperforms another. In the example of (22), an e-process for the strong null can grow large, even though _q_ is generally a better forecaster; in contrast, our e-process (24) for the weak null is expected to remain small. In Section 5.3, we provide an empirical comparison of the two e-processes. 

**Choosing** _λ_ **(or** _F_ **) for E-processes.** Theorem 3 tells us that the expected value of _Et_ ( _λ_ ) and _Et_<sup>mix</sup> are bounded by 1 at all stopping times under the null, for any choice of _λ_ or any mixture distribution _F_ . In practice, we default to using a mixture e-process with the conjugate distribution _F_ , as in Section 4.3.4. For the sub-exponential e-process, the gamma-exponential mixture as before provides a closed form for the function _m_ ( _s, v_ ) in (16), so that _Et_<sup>mix</sup> = _m_ (<sup>�</sup><sup>_t_</sup> _i_ =1<sup>_δ_ˆ</sup><sup>_i,V_ˆ</sup><sup>_t_)canbecomputed</sup> efficiently. The expression for _m_ ( _s, v_ ) is included in Section B.1. 

**P-processes.** Finally, we remark that any e-process for _H_ 0 can also be converted into an _p-process_ for _H_ 0, i.e., the sequence (p _t_ )<sup>_∞_</sup> _t_ =0<sup>that satisfies:for any</sup><sup>_α ∈_(0</sup><sup>_,_1),</sup> 



A p-process evaluated at any stopping time _τ_ , i.e. p _τ_ , is a p-value, but unlike a classical p-value, a p-process is valid at arbitrary stopping times. 

Any e-process ( _Et_ )<sup>_∞_</sup> _t_ =0<sup>can be converted into a p-process via</sup> 



following derivations from, e.g., Ramdas et al. (2020, 2022). We also remark that p _t_ can alternatively be defined from a CS as the smallest _α_ for which the (1 _− α_ )-level CS does not include zero (Howard et al., 2021), so all three notions (CS, e-process, and p-process) are closely related. 

## **5 Experiments** 

In this section, we run both simulated and real-data experiments for sequential forecast comparison using our CSs as well as e-processes. All code and data sources for the experiments are made publicly available online at https://github.com/yjchoe/ComparingForecasters. 

### **5.1 Numerical Simulations** 

As our first experiment, we compare our Hoeffding-style and EB CSs (Theorems 1 and 2, respectively) on simulated data with the asymptotic fixed-time CIs due to Theorem 2 of Lai et al. (2011). The main goal is to confirm that the CSs cover time-varying average score differentials uniformly, unlike the fixed-time CI, and are also nearly as tight as the CI. 

18 



<!-- Start of picture text -->
Forecasters<br>1.0<br>0.8<br>0.6<br>reality (rt)<br>constant_0.5<br>0.4<br>laplace<br>k29<br>0.2<br>mix_01_noiseless<br>mix_10_noiseless<br>0.0<br>0 2000 4000 6000 8000 10000<br>Time<br>Probability Forecast<br><!-- End of picture text -->

Figure 2: Various forecasters on a simulated non-IID data ( _T_ = 10<sup>4</sup> ) with sharp changepoints across time. Note that, instead of plotting the binary outcomes _yt ∈{_ 0 _,_ 1 _}_ , we plot the Reality’s choices ( _rt_ )<sup>_T_</sup> _t_ =1<sup>that generates the outcome sequence.See text for details about the forecasters.</sup> 

In our simulated experiments, we also include an asymptotic CS for time-varying means, recently developed by Waudby-Smith et al. (2021), as an additional tool for anytime-valid inference. Asymptotic CSs can be viewed as alternatives to their non-asymptotic counterparts, including the ones we introduced in Section 4, and they trade off non-asymptotic validity to achieve versatility and also comparatively smaller widths at smaller sample sizes. A formal review of asymptotic CSs in the context of sequential forecast comparison is included in Section C. 

As for our simulated data, we generate a sequence of non-IID binary outcomes and compare different forecasters using our CSs. The overall simulation pipeline closely follows Game 1, with _P_ = ∆( _Y_ ) = [0 _,_ 1], _Y_ = _{_ 0 _,_ 1 _}_ , and _T_ = 10<sup>4</sup> . At each round _t_ = 1 _, . . . , T_ , each forecaster makes a probability forecast _pt, qt ∈P_ , then reality chooses _rt_ , and finally _yt ∼_ Bernoulli( _rt_ ) is sampled. The forecasts _pt_ and _qt_ are made only using the previous outcomes, i.e., _y_ 1 _, . . . , yt−_ 1. The Reality’s choices ( _rt_ )<sup>_T_</sup> _t_ =1<sup>isspecificallychosentobenon-IIDandcontainsharpchangepoints,asshownin</sup> Figure 2. This serves as a challenging test case for the EB CS, as the sharp changepoints make it difficult to quickly adapt to the underlying variance. See Section I.1.1 for further details. 

At the end of each round _t_ = 1 _, . . . , T_ , we compute the 95% Hoeffding-style and EB CS for ∆ _t_ , using Theorems 1 and 2 respectively. We use the Brier score _S_ ( _p, q_ ) = 1 _−_ ( _p − q_ )<sup>2</sup> as our default scoring rule, but we also explore other scoring rules later in the section. As for the hyperparameter choices for sub- _ψ_ uniform boundaries, we are guided by preliminary experiments in Section I.4. 

We consider several forecasters, which are drawn with lines in Figure 2. These include the constant baseline, i.e., _pt_ = 0 _._ 5 (constant_0.5), as well as the Laplace forecasting algorithm (laplace) _pt_ =<sup>_<u>k</u>_</sup> _t_<sup><u>+0</u></sup> +1<sup>_<u>.</u>_</sup><sup><u>5</u>,where</sup><sup>_k_=#</sup><sup>_{i∈_[</sup><sup>_t_]:</sup><sup>_yi_=1</sup><sup>_}_.WefurtheraddpredictionsusingtheK29defensive</sup> forecasting algorithm (k29) (Vovk et al., 2005), which is a game-theoretic forecasting method that yields calibrated forecasts. The method depends on the choice of a kernel function, and here we use the Gaussian RBF _K_ ( _p, q_ ) = exp � _−_<sup><u>(</u></sup><sup>_<u>p</u>_</sup> 2<sup>_−_</sup> _σ_<sup>_<u>q</u>_2)2</sup> � with bandwidth _σ_ = 0 _._ 01. The mix_01_noiseless forecaster is defined as _pt_ = 0 _._ 8 for _t ≤_ 6000 and _pt_ = 0 _._ 2 for _t >_ 6000; the mix_01 forecaster is ˜ a noisy version that adds an independent noise to _pt_ by _pt_ = _pt_ + 0 _._ 5 _· ϵt_ (clipped at 0 and 1), where _ϵt_ is drawn IID from Student’s _t_ -distribution with 1 degree of freedom. The mix_10_noiseless forecaster is defined as _qt_ = 1 _− pt_ and the mix_10 forecaster _q_ ˜ _t_ is analogously defined. 

19 

The choices of forecasters and Reality are made in such a way that the unknown parameter ∆ _t_ , for _t_ = 1 _, . . . , T_ , can not only change its sign but also have different variances over time. For example, the mix_10 forecaster outperforms (∆ _t >_ 0) the mix_01 forecaster on average during _t ∈_ (2000 _,_ 6000), while the sign then reverses (∆ _t <_ 0) for _t ∈_ (6000 _,_ 10000). Among the algorithmic forecasters, the K29 variants consistently perform better than the Laplace algorithm, especially when using sharper kernels, because they are better at modeling the sharp changepoints over time. 

In Figure 3, we plot the 95% Hoeffding-style CS (Theorem 1), EB CS (Theorem 2), and a fixedtime CI for ∆ _t_ (top left), as well as their widths (top right), the corresponding e-process (bottom left), and the cumulative miscoverage rates (bottom right). First, both CSs successfully cover ∆ _t_ at any given time point, and their widths decrease as more outcomes are observed. As expected, the width of the EB CS decays more quickly than the width of the Hoeffding CS due to its use of the empirical variance term ( _V_<sup>ˆ</sup> _t_ ) but more slowly than the fixed-time CI, matching the patterns observed in Howard et al. (2021); Waudby-Smith et al. (2021). As noted before, the fixed-time CI is only valid at a fixed time _t_ and not uniformly over time, despite its tighter width, and this is illustrated by its large cumulative miscoverage rate, i.e., _αt_ = _P_ ( _∃i ≤ t_ : ∆ _i ∈/ Ci_ ) (estimated over the repeated sampling of _y_ 1 _, . . . , yt_ under _P_ ). In contrast, the EB CS<sup>8</sup> keeps its cumulative miscoverage rate well below _α_ (it is in fact zero, as it is constructed using supermartingales and not martingales). In Section H.2, we also include an analogous plot comparing our methods with other classical tests (Diebold and Mariano, 1995; Giacomini and White, 2006). 

The sub-exponential e-processes for _H_ 0( _p, q_ ) (solid green) and _H_ 0( _q, p_ ) (dotted purple) show how they accurately track the accumulated evidence for/against each forecaster over time. For example, the e-process for _H_ 0( _p, q_ ) stays below 1 during _t <_ 2000, when neither forecaster outperforms the other, and grows large during _t ∈_ (2000 _,_ 6000) when data shows more evidence against the null hypothesis that ∆ _t ≤_ 0 _, ∀t_ because the true ∆ _t_ in fact becomes positive. It then decreases back to values below 1 during _t ∈_ (6000 _,_ 10000), when the true ∆ _t_ becomes negative. We note that the gray dotted line indicates the value 2 _/α_ = 40; testing whether an e-process exceeds 2 _/α_ corresponds to a level-( _α/_ 2) sequential test equivalent to the one stated in Corollary 1. In fact, the plots show that the points at which the (1 _− α_ )-level EB CS excludes zero (on either side) are precisely when either e-process exceeds 2 _/α_ , illustrating the duality between the CS and the e-process. 

In Figure 4, we now plot the 95% CSs (left), their widths (middle), and also the corresponding e- processes (right) for comparing the k29_poly3 forecaster against the laplace baseline, using the spherical score (strictly proper), zero-one score (proper), the _ϵ_ -truncated logarithmic score ( _ϵ_ = 10<sup>_−_8</sup> ) (improper). We observe that all variants of CSs always cover the true ∆ _t_ over time, at _α_ = 0 _._ 05, and its width decreases similarly to the case of Brier scores and eventually approaches that of the asymptotic CS. In terms of the width comparison between EB and Hoeffding CSs, we see that the EB CS is generally much tighter than the Hoeffding CS, and it decreases more slowly around time steps when there are sharp changepoints in ∆ _t_ . This can be explained by the variance-adaptive nature of the EB CS, which would use larger values of intrinsic time _V_<sup>ˆ</sup> _t_ at sharp changepoints, whereas the Hoeffding CS simply uses _V_<sup>ˆ</sup> _t_ = _t_ irrespective of the variance process. The sub-exponential e- processes for _H_ 0<sup>w(</sup><sup>_p, q_) and</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_q, p_) illustrate the accumulated evidence for the first forecaster in all</sup> three cases around the same time the CS moves entirely above zero, illustrating the duality between the two methods. 

We include a plot of all pairwise comparisons between four of the forecasters in Section I.1.2. 

> 8The EB CS is computed with the polynomial stitching bound for computational efficiency. 

20 



<!-- Start of picture text -->
t (mix_10, mix_01); S=BrierScore<br>0.20 95% CS/CI for  t 0.6 Width of CS/CI<br>0.15 EB CS EB CS Asymptotic CS<br>Hoeffding CS 0.5 Hoeffding CS Fixed-Time CI<br>0.10<br>Asymptotic CS 0.4<br>0.05 Fixed-Time CI<br>0.00 t 0.3<br>0.05<br>0.2<br>0.10<br>0.1<br>0.15<br>0.20 0.0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>10 4 E-Process (log-scale) 1.0 Cumulative Miscoverage Rate<br>EB CS Asymptotic CS<br>0.8 Hoeffding CS Fixed-Time CI<br>10 2<br>0.6<br>10 0<br>0.4<br>10 2<br>H0 : t 0, t 0.2<br>H0 : t 0, t<br>10 4 0.0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Time Time<br><!-- End of picture text -->

Figure 3: _Top Left:_ 95% EB CS (blue, solid), Hoeffding-style CS (skyblue, dash-dotted), asymptotic CS (green, dashed; Section C), and a fixed-time asymptotic CI (orange, dotted) for simulated timevarying average score differentials (∆ _t_ )<sup>_T_</sup> _t_ =1<sup>between the mix_10 and mix_01 forecasters (</sup><sup>_T_= 104).</sup> The Brier score is used. _All CSs, but not the CI, uniformly cover the true score differential sequence, which changes signs sharply multiple times across the horizon. Top Right:_ Widths of the CSs and the CI across time steps. The variance-adaptive EB CS is tighter than the Hoeffding CS and slightly looser than the asymptotic CS; the fixed-time CI is the tightest, but it does not have the time-uniform guarantee. _Bottom Left:_ Sub-exponential e-processes (Theorem 3) that measure the accumulated evidence against either forecaster (first forecaster: brown, dashed; second: purple, solid). Testing whether the e-process exceeds the dashed gray line at 2 _/_ 0 _._ 05 = 40 corresponds to a sequential test at _α_ = 0 _._ 05 (Corollary 1). _Bottom Right:_ The cumulative miscoverage rate, which estimates _αt_ = _P_ ( _∃i ≤ t_ : ∆ _i ∈/ Ci_ ) over repeated sampling of _y_ 1 _, . . . , yt_ under _P_ , of the CSs/CIs. For a 95% CS, this rate is controlled at 0.05 by definition; it is in fact always zero for the non-asymptotic CSs in our experiments. For the fixed-time CI, this rate exceeds well above _α_ and continues to increase (in log-scale of time). 

21 



<!-- Start of picture text -->
t (k29, laplace); S=SphericalScore<br>95% CS for  t 0.5 Width of CS 10 4 E-Process (log-scale)<br>0.2 EB CS<br>0.4 Hoeffding CS 10 2<br>0.1<br>0.3 Asymptotic CS<br>0.0 EB CS 10 0<br>Hoeffding CS 0.2<br>0.1<br>Asymptotic CS 0.1 10 2 H 0  : t 0, t<br>0.2 t H0 : t 0, t<br>0.0 10 4<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Time Time Time<br>t (k29, laplace); S=ZeroOneScore<br>95% CS for  t 0.5 Width of CS 10 4 E-Process (log-scale)<br>0.2 EB CS<br>0.4 Hoeffding CS 10 2<br>0.1<br>0.3 Asymptotic CS<br>0.0 EB CS 10 0<br>Hoeffding CS 0.2<br>0.1<br>Asymptotic CS 0.1 10 2 H 0  : t 0, t<br>0.2 t H0 : t 0, t<br>0.0 10 4<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Time Time Time<br>t (k29, laplace); S=LogarithmicScore<br>95% CS for  t Width of CS 10 4 E-Process (log-scale)<br>1.0 2.0 EB CS<br>0.5 Hoeffding CS 10 2<br>1.5 Asymptotic CS<br>0.0 EB CS 10 0<br>1.0<br>Hoeffding CS<br>0.5 Asymptotic CS 0.5 10 2 H 0  : t 0, t<br>1.0 t H0 : t 0, t<br>0.0 10 4<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Time Time Time<br><!-- End of picture text -->

Figure 4: 95% EB (blue, solid), Hoeffding-style (skyblue, dash-dotted), and asymptotic (green, dashed) CSs (left), their widths (middle), and the sub-exponential e-processes (right) between the K29 forecaster and the Laplace forecaster. Three different scoring rules are used here: the spherical (top), the zero-one (middle), and the _ϵ_ -truncated logarithmic ( _ϵ_ = 0 _._ 01) (bottom) scores. All scoring rules are positively oriented, such that positive values of ∆ _t_ indicate that the first forecaster is better than the second. Even when the scoring rule is not strictly proper (zero-one) or not proper at all (truncated logarithmic), all CSs still cover ∆ _t_ uniformly, and in general the width of the EB CS shrinks close to the asymptotic CS than the Hoeffding-style CS, which is wider. The e-processes for _H_ 0<sup>w:∆</sup><sup>_t≤_0 (brown, dashed) cross the 2</sup><sup>_/α_line (gray, dotted) as the lower confidence bound of the</sup> EB CS crosses zero. 

22 

### **5.2 Comparing Forecasters on Major League Baseball Games** 

As our first real-world application of the CSs, we consider the problem of predicting wins and losses for baseball games played in the Major League Baseball (MLB). Sports game prediction is particularly suitable for our setting, because there are multiple publicly available probability forecasts on the outcome of each game (e.g., FiveThirtyEight, betting odds, and pundits/experts), that are frequently updated across time. There is also no obvious assumption to be reasonably made about the outcome of the games, such as stationarity or assumptions of parametric models. Recall Table 1 for an illustration of various probability forecasts made on MLB games. 

We specifically focus on predicting the outcome of MLB games over ten years (2010-2019), culminating in the 2019 World Series between the Houston Astros and the Washington Nationals. We use every regular season and postseason MLB game from 2010 to 2019 as our dataset. We convert each game as a single time point in chronological order, leading to a total of _T_ = 25 _,_ 165 games. As for the forecasters, we consider the following: 

- 538: Game-by-game probability forecasts by FiveThirtyEight on every MLB game since 1871, available at https://data.fivethirtyeight.com/#mlb-elo. 

- vegas: Pre-game closing odds made on each game by online sports bettors, converted and scaled to probabilities, as reported by https://Vegas-Odds.com.<sup>9</sup> 

- constant: a constant baseline corresponding to _pt_ = 0 _._ 5 for each _t_ . 

- laplace: A seasonally adjusted Laplace algorithm, representing the season win percentage for each team. The final adjust win percentage from the previous season, reverted to the mean by one-third, is used as the baseline probability for the next season. The final probability forecast for a game between two teams is rescaled to sum to 1. 

- k29: The K29 algorithm applied to each team, using the Gaussian kernel with _σ_ = 0 _._ 1, computed using data from the current season only. The final probability forecast for a game between two teams is rescaled to sum to 1. 

In Section I.2.1, we give further details about the five forecasters and also plot their forecasts on the last 200 games of 2019. 

We perform all pairwise comparisons of the five aforementioned forecasters on the 10-year win/loss predictions. See Sections I.4 for details on tuning the free hyperparameter on the uniform boundary. First, as we showed in Figure 1, we compare the two publicly available forecasters in 538 ( _p_ ) and vegas ( _q_ ), finding that the vegas forecaster has marginally outperformed the 538 forecaster: after _T_ = 25 _,_ 165 games, 95% EB CS for ∆ _T_ is ( _−_ 0 _._ 00265 _, −_ 0 _._ 00062), and the e-value for _H_ 0<sup>w(</sup><sup>_q, p_):∆</sup><sup>_t≥_0</sup><sup>_,∀t_is 2979</sup><sup>_._0.The fact that the vegas forecaster (marginally) outperformed the</sup> 538 forecaster is interesting, especially given that the primary goal of sports bettors is not to maximize predictive accuracy but their overall profit.<sup>10</sup> Yet, given the relatively small score difference and also the inherent uncertainty in sports game outcomes,<sup>11</sup> more fine-grained comparisons between real-world sports forecasters (e.g., regular season vs. playoffs, team-specific comparisons, and comparisons with or without specific side information) remain interesting future work. 

In Table 4, we further compare every other forecaster against the vegas forecaster by estimating the average Brier score differential ∆ _T_ using the 95% EB CS. We also show the corresponding subexponential e-processes (Theorem 3) for the null of _H_ 0<sup>w(</sup><sup>_q, p_):∆</sup><sup>_t≥_0</sup><sup>_,∀t_,whichtranslatesto</sup> 

> 9https://sports-statistics.com/sports-data/mlb-historical-odds-scores-datasets/ 10https://fivethirtyeight.com/features/the-imperfect-pursuit-of-a-perfectbaseball-forecast/ 

> 11https://projects.fivethirtyeight.com/checking-our-work/mlb-games/ 

23 

|**Forecaster**|_C_<sup>EB</sup><br>_T_|_ET_|**Forecaster**|_C_<sup>EB</sup><br>_T_|_ET_|
|---|---|---|---|---|---|
|538|(-0.00265, -0.00061)|2979.0|538|(_−∞_, -0.01012)|_>_10<sup>4</sup>|
|laplace|(-0.00980, -0.00596)|_>_10<sup>4</sup>|laplace|(_−∞_, -0.04723)|_>_10<sup>4</sup>|
|k29|(-0.01392, -0.00905)|_>_10<sup>4</sup>|k29|(_−∞_, -0.14684)|_>_10<sup>4</sup>|
|constant|(-0.01115, -0.00713)|_>_10<sup>4</sup>|constant|(_−∞_, -0.05165)|_>_10<sup>4</sup>|



(a) ∆ _T_ (Brier) against vegas (b) _WT_ (Winkler-logarithmic) against vegas 

Table 4: Comparing forecasters against the vegas forecaster. In (a), we present 95% EB CSs for the average Brier score differential (∆ _t_ )<sup>_∞_</sup> _t_ =0<sup>,evaluatedattime</sup><sup>_T_=25</sup><sup>_,_165(i.e.,</sup><sup>_C_</sup> _T_<sup>EB),aswellas</sup> the e-process for the null of _H_ 0<sup>w(</sup><sup>_q, p_):∆</sup><sup>_t≥_0</sup><sup>_,∀t_,alsoevaluatedattime</sup><sup>_T_(i.e.,</sup><sup>_ET_).In(b),we</sup> present the analogous table for the average Winkler score _WT_ (Section D), which is a normalized difference in a proper score (the logarithmic score, in this case). Note that _CT_<sup>EB</sup> is one-sided due to the one-sided boundedness of _WT_ . Positive (negative) values of ∆ _T_ and _WT_ indicate that the forecaster is better (worse) than the baseline. We find that none of the other forecasters, including 538, have outperformed vegas from 2010 to 2019. 

saying that vegas is not assumed to be better under the null, evaluated at time _T_ . Furthermore, we include comparisons involving the logarithmic score, namely via the average Winkler score _WT_ ( _p, q_ ) (Proposition 4, Section D) that quantifies the relative “skill” of forecasters (Winkler, 1994; Lai et al., 2011) as measured by a scoring rule (the logarithmic score, in this case). The Winkler score approach allows us to utilize unbounded proper scoring rules, such as the logarithmic score, when dealing with binary outcomes. Because the score is normalized and thus always maximized at 1, we can construct a one-sided CS with an upper confidence bound (UCB), and also construct an e-process against the null _H_ 0<sup>ww</sup> : _Wt ≥_ 0 _, ∀t_ . A negative UCB or a high value in the e-process indicates that _p_ is significantly worse than _q_ in relative skill. 

Our results show that none of the other forecasters, including the 538 forecaster, have outperformed vegas, both in terms of the Brier score and the Winkler-logarithmic score. 

We include a plot of all pairwise comparisons between the five forecasters in Section I.2.2. 

### **5.3 Comparing Statistical Postprocessing Methods for Weather Forecasts** 

As our second real-data experiment, we compare a set of statistical postprocessing methods for weather forecasts (Vannitsem et al., 2021), following the recent work by Henzi and Ziegel (2022). Statistical postprocessing here refers to the process of correcting for biases and dispersion errors in ensemble weather forecasts, which are produced by perturbing the initial conditions of numerical weather prediction (NWP) methods. As ensemble forecasts are commonly used in state-of-the-art weather forecasting systems as a means of producing probabilistic forecasts, statistical postprocessing is considered a key component of modern weather forecasting. 

Given 24-hour precipitation data from 2007 to 2017 at four locations (Brussels, Frankfurt, London Heathrow, and Zurich), our goal is to compare three postprocessing methods over time: isotonic distributional regression (IDR; Henzi et al. (2021)), heteroscedastic censored logistic regression (HCLR; Messner et al. (2014)), and a variant of HCLR without its scale parameter (HCLR_). We use the Brier score throughout this section. See Section I.3 for details regarding data as well as a plot of the three forecasting methods. 

Our main goal here is to sequentially compare the three statistical postprocessing methods using the EB CS and the sub-exponential e-process. As noted in Sections 2 and 4.4, the inferential con- 

24 



<!-- Start of picture text -->
90% CS on  t (HCLR, IDR) 90% CS on  t (IDR, HCLR_) 90% CS on  t (HCLR, HCLR_)<br>0.04<br>Airport<br>0.02 Brussels<br>Frankfurt<br>0.00 London<br>Zurich<br>0.02<br>0.04<br>2012 2013 2014 2015 2016 2017 2012 2013 2014 2015 2016 2017 2012 2013 2014 2015 2016 2017<br>Year Year Year<br>10 4 H0 : t (HCLR, IDR) 0, t H0 : t (IDR, HCLR_) 0, t H0 : t (HCLR, HCLR_) 0, t<br>10 3<br>10 2<br>Airport<br>Brussels<br>10 1<br>Frankfurt<br>10 0 London<br>Zurich<br>10 1<br>10 2<br>2012 2013 2014 2015 2016 2017 2012 2013 2014 2015 2016 2017 2012 2013 2014 2015 2016 2017<br>Year Year Year<br>Figure 5: Top: 90% EB CSs for ∆ t between pairs of statistical postprocessing methods (HCLR and<br>IDR; IDR and HCLR_; HCLR and HCLR_) for 1-day ensemble forecasts using Theorem 2, computed<br>and plotted separately for each airport: Brussels ( T = 1 ,  703), Frankfurt ( T = 1 ,  809), London<br>( T = 1 ,  128), and Zurich ( T = 1 ,  621). Positive (negative) scores of ∆ t ( p, q ) indicate that forecaster<br>p  is better (worse) than forecaster  q . Overall, the CSs capture the time-varying score gap on average<br>between the two forecasters across the years. Bottom: E-processes for the null that  H 0 w : ∆ t ≤ 0 , ∀t ,<br>corresponding to (the lower bound of) the 90% CSs above. These e-processes are the  weak  (average-<br>based) counterpart to Henzi and Ziegel (2022)’s e-processes for the strong (step-by-step) null that<br>H 0 s :  δt ≤ 0  ∀t . Note that the e-processes exceed 20 approximately when the lower bound of the 90%<br>CS exceeds 0. Both procedures use the Brier score as the scoring rule.<br>t<br>CS for<br>E-Process (log-scale)<br><!-- End of picture text -->

clusions drawn from the sub-exponential e-process (Theorem 3) are different from Henzi and Ziegel (2022)’s e-process, which provides a test of conditional forecast dominance at all times (i.e., the strong null), instead of average (i.e., the weak null). Given that the weak null is larger than the strong null, we would generally expect the sub-exponential e-process for the weak null to be smaller than Henzi and Ziegel (2022)’s e-process for the strong null. On the other hand, the two methods are similar in that they are both valid at arbitrary (data-dependent) stopping times. 

In Figure 5, we plot both the 90% EB CS on ∆ _t_ (top) as well as the sub-exponential e-processes for the weak one-sided null _H_ 0<sup>w(bottom), between HCLR and IDR, IDR and HCLR_, and HCLR and</sup> HCLR_ on 1-day PoP forecasts at the four airport locations. Note that we compare the same three pairs as Henzi and Ziegel (2022), who compare e-processes for the strong one-sided null _H_ 0<sup>s.The EB</sup> CS is computed using Theorem 2 and the gamma-exponential mixture boundary (16); the analogous mixture e-processes are then computed using Theorem 3. We use the significance level of _α_ = 0 _._ 1 for the EB CS, corresponding the threshold of 2 _/α_ = 20 for each one-sided e-process. 

We first note from Figure 5 that the lower bound of our 90% EB CS on ∆ _t_ ( _p, q_ ) and the e-process for _H_ 0<sup>w: ∆</sup><sup>_t_(</sup><sup>_p, q_)</sup><sup>_≤_0 share a similar trend over time, where the e-process grows large when the lower</sup> bound grows significantly larger than zero, implying that the forecaster _p_ is better than the forecaster _q_ , using the stopping rule (19). Whereas the CS provides a (two-sided) estimate of ∆ _t_ ( _p, q_ ) with 

25 

uncertainty, the e-process explicitly gives the amount of evidence for whether one is better than the other. This illustrates how the two procedures complement each other for anytime-valid inference on ∆ _t_ . We also remark that, although we only plot the e-processes for one-sided null _H_ 0<sup>w(</sup><sup>_p, q_), we can</sup> further compute the e-processes for _H_ 0<sup>w(</sup><sup>_q, p_) : ∆</sup><sup>_t_(</sup><sup>_q, p_)</sup><sup>_≤_0, and they would correspond to the upper</sup> confidence bounds of the EB CSs. 

Based on these results, we find from the 90% EB CSs that IDR forecasts are found to outperform both HCLR and HCLR_ 1-day forecasts for Brussels and that HCLR forecasts outperform HCLR_ forecasts for Frankfurt and Zurich, but we do not find significant differences at other locations between other pairs. The e-processes (thresholded at 20) lead to the same conclusions, and they clearly visualize at which point in time is one forecaster first found to outperform the other and how that pattern changes. For example, when comparing IDR to HCLR_ for Brussels, IDR is found to be better as early as 2012, and it also shows the period between late 2012 and late 2015 where it is no longer found to be better, before eventually regaining evidence favoring IDR starting 2016. 

When we compare the sub-exponential e-processes for the weak null _H_ 0<sup>wwiththee-processes</sup> for the strong null _H_ 0<sup>s,whicharedrawninFigure3ofHenziandZiegel(2022),wefindthate-</sup> processes for the strong null are large whenever e-processes for the weak null are also large, but not vice versa. For example, the comparison of IDR against HCLR_ in Frankfurt is only found to have strong evidence against the strong null, but not the weak null. This is consistent with our previous discussion in Section 4.4 that the strong null implies the weak null and thus is easier to “reject” (or gather evidence against). For example, in Frankfurt, we can infer we only have strong evidence that IDR has outperformed HCLR at some point in time_ between 2012 and 2017, but we do not have sufficient evidence that IDR has outperformed HCLR on average_ in the same time period. 

In Section E, we include e-processes for comparing lag- _h_ forecasts in the same setting. 

## **6 Extensions and Discussion** 

In the following, we discuss some related points that were not highlighted in previous sections. 

**On the use of unbounded scoring rules.** Our main results in Theorems 2 and 3 require the use of bounded scoring rules, which may be restrictive in certain use cases. If the score differentials are unbounded, a general solution would be to use the asymptotic CS (Section C), which assumes that only 2 + _δ_ moments are bounded. When it comes to unbounded proper scores for binary outcomes, such as the logarithmic score, the Winkler score (Section D), which we used in Section 5.2, offers a nonasymptotic and anytime-valid solution. 

**Comparing forecasts of lag** _h >_ 1 **.** In general forecasting scenarios, we may encounter forecasts that are made _h >_ 1 rounds ahead of when the outcome is revealed at time _t_ . In these cases, the expected score differential we seek to estimate should be conditioned on the filtration available at the time of forecasting, rather than the filtration at round _t−_ 1. We formally derive methods for comparing lag- _h_ forecasts in Section E. These include lagged sequential e-values (Arnold et al., 2023), which are not e-processes themselves but can nevertheless quantify the evidence against the weak null (and a “less weak” variant), as well as p-processes and e-processes that are more conservative. The technical details follow the recent discussions by Arnold et al. (2023); Henzi and Ziegel (2022). Constructing a more powerful e-process and also a CS for the lagged weak null remains a challenging problem. 

**On “looking ahead” in distribution-free sequential inference on time-varying means.** Our methods are valid without any assumptions about the time-varying dynamics of the forecast score differ- 

26 

entials ( _δ_<sup>ˆ</sup> _i_ )<sup>_∞_</sup> _i_ =1<sup>, and in particular we avoid conditions involving stationarity or mixing.A large e-value</sup> against _H_ 0 : ∆ _t_ ( _p, q_ ) _≤_ 0 _, ∀t_ at some stopping time _τ_ tells us that _p_ has achieved a better conditional predictive performance than _q_ up to _τ_ on average. The utility of comparing forecasters in such a descriptive sense is often significant in the real world: determining a winner in real-world forecasting competitions can often land significant cash prizes (e.g., financial forecasting<sup>12</sup> ) and/or media attention (e.g., election and sports forecasting). 

This also means that the inferential conclusions drawn from our methods need not extrapolate to _future_ time steps, because hypothetically the forecasters or Reality (from Game 1) can completely change their behaviors going forward. Indeed, there is a distinction between saying that one _has done_ better than the other and that one _is going to be_ better than the other in the future — the former is descriptive, while the latter is predictive. All our methods provide evidence and uncertainty related to the former statement. Because we do not make any assumption that says “the future will resemble the past,” no method can make conclusive statements about the latter without clairvoyance. Our setup highlights that past performance can be compared in a distribution-free manner, while predictions of future performance will require nontrivial distributional assumptions. 

Ultimately, the decision to take the inferential conclusion and extrapolate it toward the future is (and should be) left to the practitioner’s own beliefs. If a practitioner opts to make additional assumptions about Reality, then in principle, the conclusions drawn from our methods can extend to settings that the assumptions allow. If one is willing to assume, say, that the score differentials are constant, then the inferential conclusions will straightforwardly extrapolate to future time steps (in the assumed setting). Furthermore, the variance-adaptive EB CS will remain tight, because the underlying variance remains constant. It should be noted that, even under such assumptions, which are often made by classical methods like the Diebold and Mariano (1995) test, anytime-valid approaches avoid the “p-hacking” problem that the classical methods are susceptible to. 

> 12https://m6competition.com 

27 

### **Acknowledgements** 

YJC and AR thank Alexander Henzi, Johanna F. Ziegel, Rafael M. Frongillo, and the anonymous reviewers for their valuable feedback on this work. AR acknowledges funding from NSF DMS 1916320. Research reported in this paper was sponsored in part by the DEVCOM Army Research Laboratory under Cooperative Agreement W911NF-17-2-0196 (ARL IoBT CRA). The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Army Research Laboratory or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein. 

## **References** 

- Abernethy, J. D. and Frongillo, R. M. (2012). A characterization of scoring rules for linear properties. In Mannor, S., Srebro, N., and Williamson, R. C., editors, _Proceedings of the 25th Annual Conference on Learning Theory_ , volume 23 of _Proceedings of Machine Learning Research_ , pages 27.1–27.13, Edinburgh, Scotland. PMLR. 

- Arnold, S., Henzi, A., and Ziegel, J. F. (2023). Sequentially valid tests for forecast calibration. _The Annals of Applied Statistics_ , 17(3):1909 – 1935. 

- Bauer, H. (2001). _Measure and Integration Theory_ . De Gruyter, Berlin, New York. 

- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. _Monthly Weather Review_ , 78(1):1–3. 

- Darling, D. A. and Robbins, H. (1967). Confidence sequences for mean, variance, and median. _Proceedings of the National Academy of Sciences_ , 58(1):66–68. 

- Dawid, A. P. (1984). Statistical theory: the prequential approach. _Journal of the Royal Statistical Society: Series A (General)_ , 147(2):278–290. 

- Dawid, A. P. and Musio, M. (2014). Theory and applications of proper scoring rules. _Metron_ , 72(2):169–183. 

- DeGroot, M. H. and Fienberg, S. E. (1983). The comparison and evaluation of forecasters. _Journal of the Royal Statistical Society: Series D (The Statistician)_ , 32(1-2):12–22. 

- Diebold, F. X. and Mariano, R. S. (1995). Comparing predictive accuracy. _Journal of Business & Economic Statistics_ , 13(3). 

- Dunsmore, I. (1968). A Bayesian approach to calibration. _Journal of the Royal Statistical Society: Series B (Methodological)_ , 30(2):396–405. 

- Durrett, R. (2019). _Probability: Theory and examples_ , volume 49. Cambridge University Press. 

- Ehm, W., Gneiting, T., Jordan, A., and Krüger, F. (2016). Of quantiles and expectiles: consistent scoring functions, Choquet representations and forecast rankings. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , pages 505–562. 

- Ehm, W. and Krüger, F. (2018). Forecast dominance testing via sign randomization. _Electronic Journal of Statistics_ , 12(2):3758–3793. 

28 

- Fan, X., Grama, I., and Liu, Q. (2015). Exponential inequalities for martingales with applications. _Electronic Journal of Probability_ , 20:1–22. 

- Frongillo, R. M. and Kash, I. A. (2021). General truthfulness characterizations via convex analysis. _Games and Economic Behavior_ , 130:636–662. 

- Giacomini, R. and White, H. (2006). Tests of conditional predictive ability. _Econometrica_ , 74(6):1545–1578. 

- Gneiting, T. (2011). Making and evaluating point forecasts. _Journal of the American Statistical Association_ , 106(494):746–762. 

- Gneiting, T., Balabdaoui, F., and Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 69(2):243–268. 

- Gneiting, T. and Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. _Journal of the American Statistical Association_ , 102(477):359–378. 

- Good, I. (1971). Comment on “Measuring information and uncertainty” by Robert J. Buehler. _Foundations of Statistical Inference_ , pages 337–339. 

- Good, I. J. (1952). Rational decisions. _Journal of the Royal Statistical Society: Series B (Methodological)_ , 14(1):107–114. 

- Grünwald, P., de Heide, R., and Koolen, W. (2023). Safe testing. _Journal of the Royal Statistical Society: Series B (Statistical Methodology) (to appear)_ . 

- Grünwald, P. D. and Dawid, A. P. (2004). Game theory, maximum entropy, minimum discrepancy and robust Bayesian decision theory. _the Annals of Statistics_ , 32(4):1367–1433. 

- Henzi, A. and Ziegel, J. F. (2022). Valid sequential inference on probability forecast performance. _Biometrika_ , 109(3):647–663. 

- Henzi, A., Ziegel, J. F., and Gneiting, T. (2021). Isotonic distributional regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 83(5):963–993. 

- Hoeffding, W. (1963). Probability inequalities for sums of bounded random variables. _Journal of the American Statistical Association_ , 58(301):13–30. 

- Howard, S. R. and Ramdas, A. (2022). Sequential estimation of quantiles with applications to A/B testing and best-arm identification. _Bernoulli_ , 28(3):1704–1728. 

- Howard, S. R., Ramdas, A., McAuliffe, J., and Sekhon, J. (2020). Time-uniform Chernoff bounds via nonnegative supermartingales. _Probability Surveys_ , 17:257–317. 

- Howard, S. R., Ramdas, A., McAuliffe, J., and Sekhon, J. (2021). Time-uniform, nonparametric, nonasymptotic confidence sequences. _The Annals of Statistics_ , 49(2):1055 – 1080. 

- Jamieson, K. and Jain, L. (2018). A bandit approach to multiple testing with false discovery control. In _Proceedings of the 32nd International Conference on Neural Information Processing Systems_ , pages 3664–3674. 

- Jamieson, K., Malloy, M., Nowak, R., and Bubeck, S. (2014). lil’UCB: An optimal exploration algorithm for multi-armed bandits. In _Conference on Learning Theory_ , pages 423–439. PMLR. 

29 

- Johari, R., Koomen, P., Pekelis, L., and Walsh, D. (2022). Always valid inference: Continuous monitoring of A/B tests. _Operations Research_ , 70(3):1806–1821. 

- Lai, T. L. (1976a). Boundary crossing probabilities for sample sums and confidence sequences. _The Annals of Probability_ , 4(2):299–312. 

- Lai, T. L. (1976b). On confidence sequences. _The Annals of Statistics_ , 4(2):265–280. 

- Lai, T. L., Gross, S. T., and Shen, D. B. (2011). Evaluating probability forecasts. _The Annals of Statistics_ , 39(5):2356–2382. 

- Lehmann, E. L. (1975). _Nonparametrics: Statistical methods based on ranks._ Holden-Day. 

- Matheson, J. E. and Winkler, R. L. (1976). Scoring rules for continuous probability distributions. _Management Science_ , 22(10):1087–1096. 

- McCarthy, J. (1956). Measures of the value of information. _Proceedings of the National Academy of Sciences_ , 42(9):654–655. 

- Messner, J. W., Mayr, G. J., Wilks, D. S., and Zeileis, A. (2014). Extending extended logistic regression: Extended versus separate versus ordered versus censored. _Monthly Weather Review_ , 142(8):3003–3014. 

- Molteni, F., Buizza, R., Palmer, T. N., and Petroliagis, T. (1996). The ECMWF ensemble prediction system: Methodology and validation. _Quarterly Journal of the Royal Meteorological Society_ , 122(529):73–119. 

- Murphy, A. H. (1988). Skill scores based on the mean square error and their relationships to the correlation coefficient. _Monthly Weather Review_ , 116(12):2417–2424. 

- Ovcharov, E. Y. (2018). Proper scoring rules and Bregman divergence. _Bernoulli_ , 24(1):53–79. 

- Ramdas, A., Grünwald, P., Vovk, V., and Shafer, G. (2023). Game-theoretic statistics and safe anytimevalid inference. _Statistical Science (to appear)_ . 

- Ramdas, A., Ruf, J., Larsson, M., and Koolen, W. (2020). Admissible anytime-valid sequential inference must rely on nonnegative martingales. _arXiv preprint arXiv:2009.03167_ . 

- Ramdas, A., Ruf, J., Larsson, M., and Koolen, W. M. (2022). Testing exchangeability: Fork-convexity, supermartingales and e-processes. _International Journal of Approximate Reasoning_ , 141:83–109. 

- Robbins, H. (1970). Statistical methods related to the law of the iterated logarithm. _The Annals of Mathematical Statistics_ , 41(5):1397–1409. 

- Robbins, H. and Siegmund, D. (1970). Boundary crossing probabilities for the wiener process and sample sums. _The Annals of Mathematical Statistics_ , 41(5):1410–1429. 

- Rosenbaum, P. R. (1995). _Observational studies_ . Springer. 

- Savage, L. J. (1971). Elicitation of personal probabilities and expectations. _Journal of the American Statistical Association_ , 66(336):783–801. 

- Schervish, M. J. (1989). A general method for comparing probability assessors. _The Annals of Statistics_ , 17(4):1856 – 1879. 

30 

- Seillier-Moiseiwitsch, F. and Dawid, A. (1993). On testing the validity of sequential probability forecasts. _Journal of the American Statistical Association_ , 88(421):355–359. 

- Shafer, G. (2021). Testing by betting: A strategy for statistical and scientific communication. _Journal of the Royal Statistical Society: Series A (Statistics in Society)_ , 184(2):407–431. 

- Shafer, G., Shen, A., Vereshchagin, N., and Vovk, V. (2011). Test martingales, Bayes factors and p-values. _Statistical Science_ , 26(1):84–101. 

- Shafer, G. and Vovk, V. (2019). _Game-theoretic foundations for probability and finance_ , volume 455. Wiley. 

- Vannitsem, S., Bremnes, J. B., Demaeyer, J., Evans, G. R., Flowerdew, J., Hemri, S., Lerch, S., Roberts, N., Theis, S., and Atencia, A. (2021). Statistical postprocessing for weather forecasts: Review, challenges, and avenues in a big data world. _Bulletin of the American Meteorological Society_ , 102(3):E681–E699. 

- Ville, J. (1939). _Étude critique de la notion de collectif_ . Gauthier-Villars. 

- Vovk, V., Takemura, A., and Shafer, G. (2005). Defensive forecasting. In _International Workshop on Artificial Intelligence and Statistics_ , pages 365–372. PMLR. 

- Vovk, V. and Wang, R. (2021). E-values: Calibration, combination and applications. _The Annals of Statistics_ , 49(3):1736–1754. 

- Waggoner, B. (2021). Linear functions to the extended reals. _arXiv preprint arXiv:2102.09552_ . 

- Waudby-Smith, I., Arbour, D., Sinha, R., Kennedy, E. H., and Ramdas, A. (2021). Time-uniform central limit theory and asymptotic confidence sequences. _arXiv preprint arXiv:2103.06476_ . 

- Waudby-Smith, I. and Ramdas, A. (2023). Estimating means of bounded random variables by betting. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ . 

- Waudby-Smith, I., Wu, L., Ramdas, A., Karampatziakis, N., and Mineiro, P. (2023). Anytime-valid off-policy inference for contextual bandits. _ACM/IMS Journal of Data Science (to appear)_ . 

- Winkler, R. L. (1977). Rewarding expertise in probability assessment. In _Decision Making and Change in Human Affairs_ , pages 127–140. Springer. 

- Winkler, R. L. (1994). Evaluating probabilities: Asymmetric scoring rules. _Management Science_ , 40(11):1395–1405. 

- Winkler, R. L., Munoz, J., Cervera, J. L., Bernardo, J. M., Blattenberger, G., Kadane, J. B., Lindley, D. V., Murphy, A. H., Oliver, R. M., and Ríos-Insua, D. (1996). Scoring rules and the evaluation of probabilities. _Test_ , 5(1):1–60. 

- Yen, Y.-M. and Yen, T.-J. (2021). Testing forecast accuracy of expectiles and quantiles with the extremal consistent loss functions. _International Journal of Forecasting_ , 37(2):733–758. 

- Ziegel, J. F., Krüger, F., Jordan, A., and Fasciati, F. (2020). Robust forecast evaluation of expected shortfall. _Journal of Financial Econometrics_ , 18(1):95–120. 

31 

## **A Main Proofs** 

### **A.1 Sub-exponential Test Supermartingales for Time-Varying Means** 

The proofs of Theorems 2 and 3 are both based on a variance-adaptive test supermartingale that uniformly bounds sums of random variables that are bounded from below. We first derive this test supermartingale (which, by definition, is also an e-process itself) and use the result for the proofs of the main theorems in the following subsections. 

We start by revisiting a useful lemma for the sub-exponential processes. Recall from Section 4.3.1 that _ψE,c_ ( _λ_ ) = _c_<sup>_−_2</sup> ( _−_ log(1 _− cλ_ ) _− cλ_ ) _, ∀λ ∈_ [0 _,_ 1 _/c_ ) is the exponential CGF-like function. By the proof of Lemma 4.1 in Fan et al. (2015), for any _λ ∈_ [0 _,_ 1 _/c_ ) and any _ξ ≥−c_ , 



Note that the original proof uses _c_ = 1, but it straightforwardly generalizes to any value of _c >_ 0. To see this, for any _c >_ 0, set _λ_<sup>˜</sup> = _cλ ∈_ [0 _,_ 1) and _ξ_<sup>˜</sup> = _c_<sup>_−_1</sup> _ξ ≥−_ 1. Then, applying the lemma with _c_ = 1 using ( _λ,_<sup>˜</sup> _ξ_<sup>˜</sup> ) gives the desired result. 

Now, we show a time-uniform sub-exponential boundary that is generally applicable to sums of random variables that are bounded from below. This is an extension of Lemma 3(e) from Howard et al. (2020), which also utilizes (27). We note that a similar extension is utilized in the recent work of Waudby-Smith et al. (2023) but without the predictable bounds ( _ci_ )<sup>_∞_</sup> _i_ =1<sup>.</sup> 

In the following, let ( _Xi_ )<sup>_∞_</sup> _i_ =1<sup>be any process whose conditional means</sup><sup>_µi_:=E</sup><sup>_i−_1[</sup><sup>_Xi_] exist.Let</sup> ( _St_ )<sup>_∞_</sup> _t_ =0<sup>be its cumulative deviations from the conditional means, i.e.,</sup><sup>_S_0= 0 and</sup><sup>_St_= �</sup><sup>_t_</sup> _i_ =1<sup>(</sup><sup>_Xi−µi_).</sup> Note that _St_ is a martingale, i.e., E _t−_ 1[ _St_ ] = _St−_ 1. Also, let ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>beanondecreasingvariance</sup> process of the form _V_<sup>ˆ</sup> 0 = 0 and _V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(</sup><sup>_Xi −γi_)2, where (</sup><sup>_γi_)</sup> _i_<sup>_∞_</sup> =1<sup>is a predictable process.Also,</sup> we take 1 _/∞_ = 0 and, with a slight abuse of notation, [0 _,_ 0) = _{_ 0 _}_ . 

**Proposition 1** (Sub-exponential test supermartingales for time-varying means) **.** _Suppose that there exists a predictable positive sequence_ ( _ci_ )<sup>_∞_</sup> _i_ =1<sup>_such that Xi −γi≥−ci a.s.for all i ≥_1</sup><sup>_.Then,_</sup> 



_is a test supermartingale for each λ ∈_ [0 _,_ 1 _/c_ 0) _, where c_ 0 = sup _i≥_ 1 _ci._ 

_Proof._ For each _i ≥_ 1, it suffices to show that 



˜ Let _X_<sup>˜</sup> _i_ = _Xi − µi_ and ˜ _γi_ = _γi − µi_ . Then, _X_<sup>˜</sup> _i − γi_ = _Xi − γi ≥−ci_ a.s. by assumption. By (27), 

Multiplying each side by exp _{λγ_ ˜ _i}_ and rearranging terms, we get 



where in the second inequality we used the fact that 1 _− x ≤ e_<sup>_−x_</sup> for all _x ∈_ R. Finally, we take the conditional expectation E _i−_ 1 on each side. Because E _i−_ 1[ _X_<sup>˜</sup> _i_ ] = E _i−_ 1[ _Xi − µi_ ] = 0, and also because ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>and (</sup><sup>_ci_)</sup><sup>_∞_</sup> _i_ =1<sup>are predictable, we get</sup> 



˜ Substituting back in _X_<sup>˜</sup> _i_ = _Xi − µi_ and _X_<sup>˜</sup> _i − γi_ = _Xi − γi_ , we get the desired result. 

32 

Proposition 1 is stated for a general setting in which bounds on the pointwise score differentials can vary across time, as long as they form a predictable sequence. If there is a constant _c ∈_ (0 _, ∞_ ) such that _|δ_<sup>ˆ</sup> _i| ≤_ 2<sup>_<u>c</u>_, such as in Theorems 2 and 3, then we can simply choose</sup><sup>_ci_=</sup><sup>_c_for all</sup><sup>_i_and further</sup> simplify the expression (28) to 



We return to the case of using non-constant predictable bounds in Section F.2. 

### **A.2 Proof of Theorem 2** 

The proof is a direct consequence of Proposition 1, applied once each to the lower and upper confidence bounds. 



is a test supermartingale for _λ ∈_ [0 _,_ 1 _/c_ ). By definition, this implies that ( _St_ )<sup>_∞_</sup> _t_ =0<sup>is sub-</sup><sup>_ψE,c_(“sub-</sup> exponential with scale _c_ ”) with variance process ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>, and thus we have</sup> 



for any sub-exponential uniform boundary (11) with crossing probability _α/_ 2 and scale _c_ , denoted here as _uα/_ 2. Using the fact that<sup><u>1</u></sup> _t_<sup>_St_=</sup><sup><u>1</u></sup> _t_ � _ti_ =1<sup>_δ_ˆ</sup><sup>_i −_</sup><sup><u>1</u></sup> _t_ � _ti_ =1<sup>_δi_=ˆ∆</sup><sup>_t −_∆</sup><sup>_t_, we can divide each side</sup> of the inequality by _t_ to obtain the lower confidence bound (LCB). 

Similarly, the conditions also imply that _−δ_<sup>ˆ</sup> _i_ + _γi ≥−c_ , so Proposition 1 also implies that the process 



is also a test supermartingale for _λ ∈_ [0 _,_ 1 _/c_ ), or equivalently, ( _−St_ )<sup>_∞_</sup> _t_ =0<sup>issub-</sup><sup>_ψE,c_withthesame</sup> variance process ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>.Applyingthesameargumentto</sup><sup>_L_ucb</sup> _t_ ( _λ_ ) gives the analogous upper confidence bound (UCB) using the _same_ uniform boundary _uα/_ 2. 

Finally, combining the lower and upper confidence bounds with a union bound, we obtain the CS: 



### **A.3 Proof of Theorem 3** 

We state and prove a slightly more general version of Theorem 3 that only assumes the empirical score differentials _δ_<sup>ˆ</sup> _i_ are bounded from _below_ and the predictable estimates _γi_ are bounded (or truncated) from _above_ . Theorem 3 assumes that the score differentials are bounded from below _and_ above, so applying the following proposition twice to ( _δ_<sup>ˆ</sup> _i, γi_ )<sup>_∞_</sup> _i_ =1<sup>and (</sup><sup>_−δ_ˆ</sup><sup>_i, −γi_)</sup><sup>_∞_</sup> _i_ =1<sup>will give us the result.</sup> 

**Proposition 2.** _Suppose that δ_<sup>ˆ</sup> _i ≥−_ 2<sup>_<u>c</u>for each i≥_1</sup><sup>_, for some c∈_(0</sup><sup>_, ∞_)</sup><sup>_.Also, let_(</sup><sup>_γi_)</sup><sup>_∞_</sup> _i_ =1<sup>_be any_</sup> _predictable sequence and V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −_</sup> _<u>γi</u>_ )<sup>2</sup> _, where_ _<u>γi</u>_ = _γi ∧_ 2<sup>_<u>c</u>.Then, for each λ ∈_[0</sup><sup>_,_1</sup><sup>_/c_)</sup><sup>_, the_</sup> _process_ ( _Et_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>_defined as E_0(</sup><sup>_λ_) = 1</sup><sup>_and_</sup> 



33 

Proposition 2 tells us that, if the pointwise empirical score differentials are bounded from below (or above), then we can derive a sub-exponential e-process for _H_ 0( _p, q_ ) (or _H_ 0( _q, p_ )). An important use case for the more general scenario is when using the Winkler score (Winkler, 1994), which is bounded from above by 1 but unbounded from below, as we describe in Section D. 

_Proof of Proposition 2._ First, note that ( _Et_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>is an adapted process w.r.t. G (and also consists of</sup> empirical quantities only). Let _St_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −δi_) =</sup><sup>_t_( ˆ∆</sup><sup>_t −_∆</sup><sup>_t_).Since</sup><sup>_δ_ˆ</sup><sup>_i −_</sup> _<u>γi</u> ≥−c_ for all _i ≥_ 1, Proposition 1 implies that 



is a test supermartingale for each _λ ∈_ [0 _,_ 1 _/c_ ). 



In other words, for each _P ∈H_ 0<sup>w(</sup><sup>_p, q_),theprocess(</sup><sup>_Et_(</sup><sup>_λ_))</sup><sup>_∞_</sup> _t_ =0<sup>isupper-boundedbythetestsuper-</sup> martingale ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>atalltimes</sup><sup>_t_.Thisimpliesthat(</sup><sup>_Et_(</sup><sup>_λ_))</sup><sup>_∞_</sup> _t_ =0<sup>isane-processfor</sup><sup>_H_</sup> 0<sup>w(</sup><sup>_p, q_),by</sup> Corollary 22 of Ramdas et al. (2020). 

## **B Details on Time-Uniform Boundary Choices** 

### **B.1 Computing the Gamma-Exponential Mixture** 

Here, we derive a closed-form expression (up to efficiently computable gamma functions) for the gamma-exponential mixture, which is used in both the mixture boundary for the CS (Equation (16)) and in the mixture e-process for the weak null (Theorem 3). The mixture takes the following form: 



where _fρ_ , for any _ρ >_ 0, is a reparametrized Gamma density _fρ_ ( _λ_ ) = _C_ ( _ρ_ )(1 _− λ_ )<sup>_ρ−_1</sup> _e_<sup>_−ρ_(1</sup><sup>_−λ_)</sup> , _<u>ρ</u>_<sup>_ρ_</sup> _∞ λ ∈_ [0 _,_ 1 _/c_ ), where _C_ ( _ρ_ ) = _<u>γ</u>_ <u>(</u> _ρ,ρ_ )Γ( _ρ_ )<sup>is the normalization constant, Γ(</sup><sup>_a, z_) :=</sup> � _z u_<sup>_a−_1</sup> _e_<sup>_−u_</sup> _du_ is the upper incomplete gamma function, Γ( _a_ ) := Γ( _a,_ 0) is the gamma function, and _<u>γ</u>_ is the regularized lower incomplete gamma function: 



Both Γ and _<u>γ</u>_ can be computed efficiently in standard scientific computing software. (E.g., _<u>γ</u>_ can be computed using boost::math::gamma_p in C++ and scipy.special.gammainc in Python.) 

We note here that all time-uniform boundaries have a “tradeoff of tightness” across different (intrinsic) times (Howard et al., 2021), so that it is natural to have a hyperparameter that controls at what intrinsic time we want the resulting CS width to be optimized. In the above, the single hyperparameter, _ρ >_ 0, can be related to the user-specified optimal intrinsic time _v_ opt (and the significance level _α_ ) via the mapping _ρ_ = _−v_ opt( _W−_ 1( _−α_<sup>2</sup> _/e_ ) + 1), where _W−_ 1 is the lower branch of the Lambert 

34 

_W_ function. As described in Proposition 3 of Howard et al. (2021), this choice of _ρ_ uniquely minimizes the width function _v �→ u_ ( _v_ ) _/_<sup>_√_</sup> _<u>v</u>_ , when _u_ is the two-sided normal mixture boundary, and it is also known to also provide a good approximation for the (one-sided) gamma-exponential mixture boundary in practice. 

The first part of the following proposition is essentially a restatement of Proposition 9 in Howard et al. (2021); the second part additionally provides an upper bound for the mixture when _s ≪_ 0 (e.g., the mixture e-process when data supports the null). 

**Proposition 3** (Gamma-exponential mixture for e-processes) **.** _Fix c >_ 0 _and ρ >_ 0 _. Consider any values of s ∈_ R _and v ≥_ 0 _. If_<sup>_cs_</sup><sup><u>+</u></sup> _c_<sup>_v_2+</sup><sup>_<u>ρ</u>_</sup> _>_ 0 _, then_ 



_otherwise, if_<sup>_cs_</sup><sup><u>+</u></sup> _c_<sup>_v_2+</sup><sup>_<u>ρ</u>_</sup> _<_ 0 _, then_ 



This is precisely the formula for the sub-exponential mixture e-process in Theorem 3: _Et_<sup>mix</sup> = _m_ (<sup>�</sup><sup>_t_</sup> _i_ =1<sup>_δ_ˆ</sup><sup>_i,V_ˆ</sup><sup>_t_) with</sup><sup>_fρ_being the mixture density.It makes sense that</sup><sup>_m_(</sup><sup>_s, v_) is upper-bounded by 1</sup> when<sup>_cs_</sup><sup><u>+</u></sup> _c_<sup>_v_2+</sup><sup>_<u>ρ</u>_</sup> _<_ 0, because _s < −_<sup>_v_</sup><sup><u>+</u></sup> _c_<sup>_<u>ρ</u>_</sup> _<_ 0 would imply that the sum of score differentials is negative, supporting the weak null. In our implementation, we use the first upper bound in (44), which can be computed efficiently and get substantially smaller than 1 when _v ≫_ 0. 

_Proof of Proposition 3._ For simplicity, we assume _c_ = 1. The proof is analogous for any _c >_ 0. Recall that _ψE_ ( _λ_ ) = _−_ log(1 _− λ_ ) _− λ_ for _λ ∈_ [0 _,_ 1). For any _ρ >_ 0, 



where in the last equality we used 

_λ_ ( _s_ + _v_ ) _− ρ_ (1 _− λ_ ) = ( _s_ + _v_ ) _−_ (1 _− λ_ )( _s_ + _v_ ) _−_ (1 _− λ_ ) _ρ_ = _−_ ( _s_ + _v_ + _ρ_ )(1 _− λ_ ) + ( _s_ + _v_ ) _._ Now, let _a_ = _v_ + _ρ_ and _z_ = _s_ + _v_ + _ρ_ , and note that _a >_ 0. 

**Case 1:** _z_ = _s_ + _v_ + _ρ >_ 0 **.** Using the change-of-variable formula _u_ = ( _s_ + _v_ + _ρ_ )(1 _−λ_ ) = _z_ (1 _−λ_ ), we have that 





35 

where we use the fact that the integral in (46) corresponds to the numerator of the lower incomplete gamma function _P_ ( _a, z_ ) in (42). The expression (47) can be computed in closed-form. 

**Case 2:** _z_ = _s_ + _v_ + _ρ <_ 0 **.** Using the change-of-variable formula _u_ = _−_ ( _s_ + _v_ + _ρ_ )(1 _− λ_ ) = _−z_ (1 _− λ_ ), we obtain 



Although the integral in (48) is no longer a regularized lower incomplete gamma function, we can still show that _m_ ( _s, v_ ) is upper-bounded by 1. Since _e_<sup>_u_</sup> _≤ e_<sup>_|z|_</sup> = _e_<sup>_−z_</sup> for _u ≤|z|_ , we have that 



where in (49) we used _−z_ + ( _s_ + _v_ ) = _−_ ( _s_ + _v_ + _ρ_ ) + ( _s_ + _v_ ) = _−ρ_ , and in (50) we substituted in _a_ = _v_ + _ρ_ . We can further bound this value, using the fact that _v >_ 0 and substituting back in _C_ ( _ρ_ ): 



where in (51) we used the fact that _e_<sup>_−ρ_</sup> _≤ e_<sup>_−u_</sup> for _u ∈_ [0 _, ρ_ ]. 

### **B.2 The Polynomial Stitching Boundary** 

The _polynomial stitched boundary_ (Theorem 1, Howard et al. (2021)) provides a fully closed-form (without any gamma functions) alternative to the aforementioned gamma-exponential mixture boundary. It is constructed by finding a smooth analytical upper bound on a sequence of linear uniform 

36 

bounds across different timesteps. The boundary asymptotically grows with _O_ (<sup>_√_</sup> _v_ log log _v_ ) rate, matching the form of the law of the iterated logarithm (LIL). For example, a 95% EB CS for ∆ _t_ (Theorem 2) using the polynomial stitching boundary is given as follows (assuming _|δ_<sup>ˆ</sup> _i| ≤_ 1 _, ∀i_ ): 



where _V_<sup>ˆ</sup> _t_ is the intrinsic time. 

ˆ The polynomial stitched boundary can be applied to both Theorems 1 and 2 by setting _V_<sup>ˆ</sup> _t_ = _t_ and _Vt_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −γi_)2respectively.Previous work showed that the polynomial stitched boundary is a</sup> sub-gamma uniform boundary (Theorem 1, Howard et al. (2021)), which is also a “universal” sub- _ψ_ uniform boundary for any CGF-like function _ψ_ (Proposition 1, Howard et al. (2020)). We omit a full restatement of Howard et al. (2021)’s Theorem 1, which establishes the validity of the polynomial stitching boundary, but rather, we list its three hyperparameters for practical use: 

- _v_ opt _>_ 0 determines the value of the intrinsic time at which the boundary is tightest; 

- _s >_ 1 controls how the crossing probability is distributed over intrinsic time; 

- _η >_ 1 controls the geometric spacing of the intrinsic time. 

Throughout this paper, we fix _s_ = 1 _._ 4 and _η_ = 2, as recommended by the original paper, and only adjust _v_ opt, which serves the analogous role as the hyperparameter of the same name for the gammaexponential boundary in Section B.1. 

Although the stitching boundary is computed in closed form and matches the LIL rate, it is usually not as tight as the CM boundary in practice, and thus we use the CM boundary as our default in all of our main experiments. 

## **C Asymptotic CSs for Sequential Forecast Comparison** 

In their recent work, Waudby-Smith et al. (2021) introduce a new class of time-uniform CSs called asymptotic CSs, which trade the nonasymptotic guarantee of a standard CS (2) for applicability to a wider variety of scenarios, e.g., estimating the average treatment effect in causal inference (for which a nonasymptotic CS is not known). Formally, a sequence of confidence intervals ( _θ_<sup>ˆ</sup> _t ± Rt_<sup>A)</sup><sup>_∞_</sup> _t_ =1<sup>isa</sup> (1 _−α_ ) _-asymptotic CS (AsympCS)_ for ( _θt_ )<sup>_∞_</sup> _t_ =1<sup>if there exists a nonasymptotic (1</sup><sup>_−α_)-CS (ˆ</sup><sup>_θt±R_</sup> _t_<sup>NA</sup> )<sup>_∞_</sup> _t_ =1<sup>,</sup> for ( _θt_ )<sup>_∞_</sup> _t_ =1<sup>, such that</sup> 



Furthermore, the AsympCS has an _approximation rate_ of _r_ ( _t_ ) if _Rt_<sup>NA</sup> _− Rt_<sup>A=</sup><sup>_Oa.s._(</sup><sup>_r_(</sup><sup>_t_)).Def-</sup> inition (54) says that, as _t →∞_ , the AsympCS is an “arbitrarily precise approximation” of the nonasymptotic CS, and it can be viewed as approximately satisfying the time-uniform coverage property when _t_ is large. 

Waudby-Smith et al. (2021) describes an asymptotic CS for time-varying means that can be applied to our setting of estimating (∆ _t_ )<sup>_∞_</sup> _t_ =1<sup>under Lyapunov CLT-type conditions.For the sake of com-</sup> pleteness, we include the (simplified) assumptions and the resulting closed form of the asymptotic CS, adapted to our setting and notations. 

Let _σt_<sup>2=E</sup><sup>_t−_1[(ˆ</sup><sup>_δt−δt_)2]denotetheconditionalvariance,</sup><sup>_Vt_=�</sup><sup>_t_</sup> _i_ =1<sup>_σ_</sup> _i_<sup>2bethecumulative</sup> conditional variance, and _σ_ ˜ _t_<sup>2=</sup><sup>_t−_1</sup><sup>_Vt_betheaverage.Let</sup><sup>_σ_ˆ</sup> _t_<sup>2beanyestimatorof</sup><sup>_σ_</sup> _t_<sup>2,suchas</sup><sup>_σ_ˆ</sup> _t_<sup>2=</sup> _t_<sup>_−_1 �</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi−_ˆ∆</sup><sup>_i−_1)2.(Notice that,in the setting of Theorem 2,</sup><sup>_σ_ˆ</sup> _t_<sup>2=</sup><sup>_t−_1 ˆ</sup><sup>_Vt_with</sup><sup>_γi_set toˆ∆</sup><sup>_i−_1.)</sup> Now, we assume the following: 

37 

˜ _a.s._ (a) _σt_<sup>2</sup> _−→ σ∗_<sup>2for some</sup><sup>_σ_</sup> _∗_<sup>2</sup><sup>_>_0;</sup> 

(b) there exists _q >_ 2 such that the _q_<sup>th</sup> moments of _δ_<sup>ˆ</sup> _t_ is uniformly bounded (a.s.) for all _t ≥_ 1; and (c) _σ_ ˆ _t_<sup>2</sup><sup>_/σ_˜</sup> _t_<sup>2</sup> _−→a.s._ 1. 

As noted in the paper, these conditions can be substantially more general than either sub-Gaussianity or boundedness. Given these assumptions, we know by Theorem 2.3 of Waudby-Smith et al. (2021) that, for any _ρ >_ 0 and any _α ∈_ (0 _,_ 1), 



forms a (1 _− α_ )-AsympCS for (∆ _t_ )<sup>_∞_</sup> _t_ =1<sup>with an approximation rate of</sup><sup>_o_(</sup><sup>_√_</sup> _Vt_ log _Vt/t_ ). _ρ >_ 0 is a hyperparameter that affects the relative tightness of the CS across time, analogous to the hyperparameter _ρ_ in Section B. In our experiments, we follow Waudby-Smith et al. (2021) (Equation 74) and use the choice that approximately optimizes the width at a pre-specified time _t_<sup>_∗_</sup> _≥_ 1: 



Unless specified otherwise, _t_<sup>_∗_</sup> is chosen to be 100 in our experiments. 

As illustrated in Figures 3 and 4, the AsympCS is typically tighter than the EB CS (Theorem 2) for smaller values of _t_ , and as _t_ grows large the widths of the two CSs become close to one another. 

## **D Comparing Relative Forecasting Skills Using the Winkler Score** 

In a typical forecast comparison scenario, we are often interested in comparing a newly developed forecasting algorithm (say, _p_ ) with an existing baseline (say, _q_ ). For example, a company that already deploys a daily forecasting algorithm may want to A/B test if its newly developed method is at least as good as the existing one. In such settings, we may be interested in the _relative_ improvement of a forecaster over a baseline, and early work by Murphy (1988) and Winkler (1994) propose using normalized scoring rules that better reflect the relative “skill” of the new forecaster. 

In this section, we show how our main results can be extended in a unique way to construct timeuniform CSs and e-processes for the _average Winkler score_ (Winkler, 1994), which is a normalized version of the average score differentials between probability forecasts on binary outcomes. Interestingly, these results yield SAVI approaches that are valid _without_ a boundedness or sub-Gaussianity assumption on the underlying scoring rule, and instead, they are valid whenever the scoring rule is proper (Gneiting and Raftery, 2007). The Winkler score is particularly useful when comparing probability forecasters based on the logarithmic score, which is a strictly proper but unbounded score, as we showcased in Section 5.2. We remark that Lai et al. (2011) first showed the asymptotic normality of the average Winkler score. In contrast to their work, the methods we develop here are nonasymptotic and anytime-valid, depending only on the natural upper bound (of 1) on the Winkler score; we also allow the baseline forecaster to be nonconstant. 

Formally, we first define the _(pointwise) Winkler score w_ ( _p, q, y_ ) with a base scoring rule _S_ as follows: 



38 

where we set 0 _/_ 0 := 0. We note that (57) is equivalent to the increment in the e-process of Henzi and Ziegel (2022) (details in Section H.1), and thus we can interpret Henzi and Ziegel (2022)’s e- process for the strong null as betting directly proportionally to the relative forecasting skill between the forecasters. We also define the _expected (pointwise) Winkler score_ as 



for _p, q ∈_ (0 _,_ 1) and _r ∈_ [0 _,_ 1]. As before, _y ∼ r_ denotes _y ∼_ Bernoulli( _r_ ) (conditional on _p_ and _q_ ). Winkler (1994, Section 4) showed that, given any constant forecaster _q ∈_ (0 _,_ 1), the scoring rule _S_<sup>_′_=</sup><sup>_w_(</sup><sup>_p, q, y_) is (strictly) proper for</sup><sup>_p_whenever</sup><sup>_S_itself is (strictly) proper.The score is also</sup> _q_<sup>(</sup><sup>_p, y_)</sup> standardized in the following sense. Suppose that _p_ is a calibrated forecaster and _q_ is the “least skillful” calibrated forecaster, i.e., the constant forecaster that predicts the historical average ( _climatology_ in weather forecasting). Then, the expected Winkler score _w_ ( _p, q_ ; _r_ ) is zero (minimum) when _p_ = _q_ and one (maximum) when _p ∈{_ 0 _,_ 1 _}_ . The _empirical_ Winkler score _w_ ( _p, q, y_ ) can take negative values, which would suggest that _p_ is worse than _q_ on forecasting the outcome _y_ under _S_ . 

In the following lemma, we summarize the characteristics of the Winkler score that are useful for both its interpretation and the proofs that will follow shortly. 

**Lemma 1** (Winkler (1994)) **.** _Let S be a proper scoring rule. Then, for any p, q ∈_ (0 _,_ 1) _and y ∈ {_ 0 _,_ 1 _},_ 



_In the case that y_ = 1 ( _p > q_ ) _, the denominator is non-negative and the numerator is non-positive._ 

See Winkler (1994, 1977) for a proof. Lemma 1 establishes that _p_ gets a positive score of 1 if it is at least as good as _q_ , but otherwise, it does not get a positive score. Two implications are: (i) the Winkler score is bounded from above by 1, and (ii) when we take the average of pointwise Winkler scores over _t_ forecasts and outcomes, we can read off the sign of the average to tell whether _p_ has better or worse forecasting skills than _q_ . 

Returning to the sequential setup in Game 1, we now treat the pointwise Winkler scores between ( _pt_ )<sup>_∞_</sup> _t_ =1<sup>and(</sup><sup>_qt_)</sup><sup>_∞_</sup> _t_ =1<sup>astheanalogsofpointwisescoredifferentialsfromSection4.Because(</sup><sup>_pt_)</sup><sup>_∞_</sup> _t_ =1 and ( _qt_ )<sup>_∞_</sup> _t_ =1<sup>are predictable w.r.t. G, we replace the expectation in (58) with the conditional expectation</sup> w.r.t. _Gt−_ 1. Then, for each _t_ , we can define the _(expected) average Winkler score_ up to _t_ : 



This is the time-varying sequence of parameters that we seek to estimate; we also analogously define the _weak Winkler (WW)_ null 



For this null, the sign is the opposite of (18): we assert that _p_ is at least as good as _q_ as our null, and rejecting _H_ 0<sup>ww</sup><sup>_,≥_</sup> ( _p, q_ ) would mean that _p_ is decidedly worse than _q_ on average up to some time _t_ . Note also that we slightly generalize the average score from Winkler (1994)’s to allow the baseline forecaster to be any predictable (0 _,_ 1)-valued forecaster ( _qt_ )<sup>_∞_</sup> _t_ =1<sup>.</sup> 

We are now ready to present our main result. In the following, we denote the (empirical) pointwise ˆ _t_ Winkler scores as _wi_ = _w_ ( _pi, qi, yi_ ) for each _i_ and their average over time as _W_<sup>ˆ</sup> _t_ :=<sup><u>1</u></sup> _t_ � _i_ =1<sup>_w_(</sup><sup>_pi, qi, yi_).</sup> 

39 

**Proposition 4** (Sequential inference on the average Winkler score) **.** _Suppose that S is a proper scoring rule and that pi, qi ∈_ (0 _,_ 1) _for each i ≥_ 1 _. Let_ <u>(</u> _<u>γi</u>_<sup>)</sup> _i_<sup>_∞_</sup> =1<sup>_be a_[</sup><sup>_−_1</sup><sup>_, ∞_)</sup><sup>_-valued predictable process and_</sup> _let V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>( ˆ</sup><sup>_wi −_</sup><sup>_<u>γ</u>_</sup> _~~i~~_<sup>)2</sup><sup>_._</sup> 



_is a_ (1 _− α_ ) _-CS for_ ( _Wt_ )<sup>_∞_</sup> _t_ =1<sup>_, for any sub-exponential uniform boundary uα with crossing prob-_</sup> _ability α and scale_ 2 _._ 



_is an e-process for H_ 0<sup>ww</sup><sup>_,≥_</sup> : _Wt ≥_ 0 _, ∀t, and so is the mixture process Et_<sup>mix</sup> := � _Et_ ( _λ_ ) _dF_ ( _λ_ ) _for any distribution F on_ [0 _,_ 1 _/c_ ) _._ 

The proof is a direct application of Proposition 1, using the upper bound of 1 on the empirical pointwise Winkler scores. Because the Winkler score is unbounded from below, the standard machinery only readily provides the upper confidence bound for ( _Wt_ )<sup>_∞_</sup> _t_ =1<sup>.Thus,wederiveaone-sidedCS</sup> in (62) that tells us the certainty to which we know _Wt_ is away from 1. The sub-exponential e-process in (63) corresponds to this upper confidence bound and measures the evidence against the null that _p_ is at least as good as _q_ . From the sequential testing point-of-view, either a large value in the e-process or a small value of the upper confidence bound suggests that _p under_ performs _q_ ; conversely, either a small value in the e-process or a value close to 1 for the upper confidence bound (i.e., a vacuous CS) tells us that there is no such evidence. Note that, to satisfy the constraint on the predictable process ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>tobeboundedfrombelowby</sup><sup>_−_1,wecanchooseasdefaulttherunningaverageasin</sup> Theorem 2, but cap it from below at _−_ 1, i.e., _γi_ = _−_ 1 _∨ W_<sup>ˆ</sup> _i−_ 1. 

_Proof of Proposition 4._ We first use Lemma 1 to obtain an upper bound of 1 on the pointwise empirical Winkler scores, _wi_ = _w_ ( _pi, qi, yi_ ). Then, the rest of the proof follows similarly from the proofs of Proposition 1 as well as Theorem 2 and Theorem 3. 

Specifically, define the process ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>as</sup><sup>_L_0(</sup><sup>_λ_) = 1 and</sup> 



which is a test supermartingale an w.r.t. G for each _λ ∈_ [0 _,_ 1 _/_ 2) by Proposition 1 and Lemma 1. By definition, the process ( _t_ ( _Wt − W_<sup>ˆ</sup> _t_ ))<sup>_∞_</sup> _t_ =0<sup>issub-exponentialwithscale2(i.e.,sub-</sup><sup>_ψE,_2)havingthe</sup> variance process ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =0<sup>.The results then follow analogously to Theorems 2 and 3.</sup> 

We close with the note that, if the main goal is rather to tightly estimate ( _Wt_ )<sup>_∞_</sup> _t_ =1<sup>fromboth</sup> sides or to test the null _H_ 0<sup>ww</sup><sup>_,≤_</sup> : _Wt ≤_ 0 _, ∀t_ , then there is a way to use either the sub-Gaussianity or the boundedness assumption on scoring rules (rather than propriety) and apply any of our main Theorems; the proof would be analogous for each application. The caveat with the Winkler score is that it is unbounded from below even when using a bounded base scoring rule, such as the Brier score, because the lower bound depends on how close _q_ can get to 0 or 1. If _qt_ = _q ∈_ (0 _,_ 1) is the climatology forecaster, then this is not an issue, and the two-sided approach can also be useful. We summarize the analogs of Theorem 2 and Theorem 3 for the average Winkler score as a corollary. 

40 

**Corollary 2** (Two-sided sequential inference on the average Winkler score.) **.** _Suppose there exists some c >_ 0 _such that w_ ˆ _i ≥_ 1 _− c for any i ≥_ 1 _. Let_ ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>_be a_[1</sup><sup>_−c,_1]</sup><sup>_-valued predictable process_</sup> _and let V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>( ˆ</sup><sup>_wi −γi_)2</sup><sup>_.Then,_</sup> 



_is a_ (1 _− α_ ) _-CS for_ ( _Wt_ )<sup>_∞_</sup> _t_ =1<sup>_,foranysub-exponentialuniformboundaryu_</sup> _α/_ 2<sup>_withcrossing_</sup> _probability α/_ 2 _and scale c._ 



_is an e-process for H_ 0<sup>ww</sup><sup>_,≤_</sup> : _Wt ≤_ 0 _, ∀t, and so is the mixture process Et_<sup>mix</sup> := � _Et_ ( _λ_ ) _dF_ ( _λ_ ) _for any distribution F on_ [0 _,_ 1 _/c_ ) _._ 

The value of _c_ may depend on both the choice of _S_ and how close _qi_ can get to either 0 or 1. For example, if _S_ is the Brier score and _qi ∈_ [ _q_ 0 _,_ 1 _− q_ 0] for some constant _q_ 0 _∈_ (0 _,_ 1), then _c_ = 2 _/q_ 0. 

## **E Comparing Lagged Forecasts** 

Given an integer lag _h ≥_ 1, if _pi_ and _qi_ were lag- _h_ forecasts made at round _i_ for the eventual outcome _yi_ + _h−_ 1, then we would be interested in the following time-varying parameter: 



For each _t ≥ h_ , we take the average up to the ( _t − h_ + 1)th round, because the forecasts made beyond that round can only be evaluated after the _t_ th round. The conditional expectation is taken in such a way that the forecasters ( _pi_ and _qi_ ) are evaluated based on the information they had at the time of forecasting ( _Gi−_ 1) and not the one right before the outcome is realized ( _Gi_ + _h−_ 1). 

The case of _h_ = 1 corresponds to the setting we considered in Section 4, but extending the construction to the case of _h >_ 1 is not straightforward. For example, the sequence ( _Et_ ( _λ_ ))<sup>_∞_</sup> _t_ =0 defined analogously to the one in Theorem 3 would _not_ be an e-process w.r.t. the game filtration G, let alone a process, because the _t_ th term would include future outcomes that are not realized at time _t_ . Rather, the process ( _Et_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>nowonlysatisfiestheweakerpropertythatE</sup><sup>_t−h_[</sup><sup>_Et_]</sup><sup>_≤_1forall</sup> (non-stopping) times _t ≥ h_ under _H_ 0. In their recent work, Arnold et al. (2023) refer to such processes as _sequential e-values for H_ 0 _at lag h_ and propose to combine _h_ subsequences of the original process that are each test supermartingales w.r.t. different sub-filtrations of G. Although lag- _h_ sequential e-values are not e-processes themselves, the recent preprints of Arnold et al. (2023); Henzi and Ziegel (2022) show that there is a workaround to turn them into an e-process possessing anytime-validity. Here, we adapt their approach and develop e- and p-processes for weaker nulls similar to the weak null in the lag-1 case; developing a tight CS for estimating ∆<sup>(</sup> _t_<sup>_h_)</sup> remains an open problem. 

To proceed, we define two weak nulls related to the sequence of parameters (∆<sup>(</sup> _t_<sup>_h_)</sup> )<sup>_∞_</sup> _t_ = _h_<sup>.The first</sup> is a straightforward generalization of the lag-1 weak null (18) to any _h ≥_ 1: 



41 

This recovers _H_ 0<sup>w(</sup><sup>_p, q_) when</sup><sup>_h_= 1.We refer to (68) as the</sup><sup>_lag-h weak null_between</sup><sup>_p_and</sup><sup>_q_.</sup> 

Because of the aforementioned challenge in the _h >_ 1 case, we also define a null hypothesis for which we can derive a more powerful e-process. The _lag-h period-wise (PW) weak null_ , which we denote as _H_ 0<sup>pw(</sup><sup>_p, q_;</sup><sup>_h_), asserts that the weak null holds at every</sup><sup>_h_th step for all periods</sup><sup>_k∈{_1</sup><sup>_, . . . , h}_,</sup> making it (slightly) stronger than the weak null but weaker than the strong null. Formally, define the index set 



which includes every _h_ th round of the game starting at _k_ +1 up to (at most) _t − h_ +1. (For _t < h_ + _k_ , _It_<sup>[</sup><sup>_k_]</sup> = _∅_ .) Now, for each _k_ = 1 _, . . . , h_ , we define ∆<sup>[</sup> _t_<sup>_k_]</sup> := _t−h_ <u>1+1</u> � _i∈It_<sup>[</sup><sup>_k_]</sup> _δi_ , so that<sup>�</sup><sup>_h_</sup> _k_ =1<sup>∆</sup> _t_<sup>[</sup><sup>_k_]</sup> = ∆<sup>(</sup> _t_<sup>_h_)</sup> . Then, the lag- _h_ PW weak null is defined as 



It is clear from their definitions that the following inclusion relationships hold between the three null hypotheses: 



for any _h ≥_ 1. When _h_ is a small integer (say, 5 or 10) and _t_ grows large, the lag- _h_ PW weak null is still much weaker than the lag- _h_ strong null. 

Having defined the two nulls, we first present an e-process and a p-process for the lag- _h_ PW null (70). Because we cannot straightforwardly derive an e-process for _h >_ 1, we start with a p- process constructed using the lag- _h_ sequential e-values and then use a p-to-e calibrator (Shafer et al., 2011) to obtain an e-process that remains valid at arbitrary stopping times. An analogous proposition for (68) is shown later and relies on similar proof techniques. 

Let _δ_<sup>ˆ</sup> _i_<sup>(</sup><sup>_h_)</sup> = _S_ ( _pi, yi_ + _h−_ 1) _− S_ ( _qi, yi_ + _h−_ 1) be the empirical pointwise score differential for lag- _h_ forecasts. Note that _δi_<sup>(</sup><sup>_h_)</sup> = E _i−_ 1[ _δ_<sup>ˆ</sup> _i_<sup>(</sup><sup>_h_)</sup> ]. In addition, we say that a function _f_ : [0 _,_ 1] _→_ [0 _, ∞_ ) is a 1 _p-to-e calibrator_ if it is non-increasing and satisfies �0<sup>_f_(</sup><sup>_u_)</sup><sup>_du_= 1.</sup> 

**Proposition 5** (Sequential inference for _H_ 0<sup>pw(</sup><sup>_h_))</sup><sup>**.**</sup><sup>_Suppose that |δ_ˆ</sup> _i_<sup>(</sup><sup>_h_)</sup> _| ≤_ 2<sup>_<u>c</u>for all i ≥_1</sup><sup>_, for some c ∈_</sup> (0 _, ∞_ ) _. Let_ ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>_be a_[</sup><sup>_−_</sup> 2<sup>_<u>c</u>,_</sup> 2<sup>_<u>c</u>_]</sup><sup>_-valued predictable process w.r.t._G</sup><sup>_.Also,for each k∈{_1</sup><sup>_, . . . , h}_</sup> _and λ ∈_ [0 _,_ 1 _/c_ ) _, define_ 



_where_<sup>�</sup><sup>_Then, for each λ ∈_[0</sup><sup>_,_1</sup><sup>_/c_)</sup><sup>_, the following statements are true:_</sup> _i∈∅_<sup>(</sup><sup>_·_) = 1</sup><sup>_._</sup> 

_1. (Averaged sequential e-values.) The process_ 



_is adapted w.r.t._ G _and satisfies_ E _P_ [ _E_<sup>¯</sup> _τ_<sup>pw</sup> + _h−_ 1<sup>(</sup><sup>_λ_)]</sup><sup>_≤_1</sup><sup>_for any_G</sup><sup>_-stopping time τand any P∈_</sup> _H_ 0<sup>pw(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_._</sup> 

42 

_2. (P-process.) The process_ (p<sup>pw</sup> _t_<sup>)</sup><sup>_∞_</sup> _t_ =1<sup>_defined by_</sup> 



_is a p-process for H_ 0<sup>pw(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_w.r.t._G</sup><sup>_._</sup> 

_3. (Calibrated e-process.) Let f_ : [0 _,_ 1] _→_ [0 _, ∞_ ) _be any p-to-e calibrator. Then, the process_ ( _Et_<sup>pw)</sup><sup>_∞_</sup> _t_ =0<sup>_defined by E_</sup> 0<sup>pw</sup> = 1 _and_ 



_is an e-process for H_ 0<sup>pw(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_w.r.t._G</sup><sup>_._</sup> 

The structure of the index set ensures that _Et_<sup>[</sup><sup>_k_](</sup><sup>_λ_) for each</sup><sup>_k_is adapted and non-increasing under</sup> the null. For example, with lag-3 forecasts, _Et_<sup>[</sup><sup>_k_](</sup><sup>_λ_) for each</sup><sup>_k_is computed using each of the subse-</sup> quences (1 _,_ 4 _,_ 7 _, . . ._ ), (2 _,_ 5 _,_ 8 _, . . ._ ), and (3 _,_ 6 _,_ 9 _, . . ._ ). As for the choice of a p-to-e calibrator _f_ , we follow Vovk and Wang (2021); Ramdas et al. (2022) and use (as our default) 



In words, sequential e-values are expected to be at most 1 at time _τ_ + _h−_ 1, where _τ_ is any stopping time w.r.t. G. In contrast, the p-process directly yields a valid sequential test without such a condition, and it can also be calibrated to yield an e-process. 

_Proof of Proposition 5._ Our goal is to derive a p-process for _H_ 0<sup>pw(</sup><sup>_h_) based on ideas from the proofs</sup> of Proposition 3.4 in Arnold et al. (2023) and from the validity of their proposed sequential test, and then to calibrate it into an e-process (Shafer et al., 2011; Ramdas et al., 2022). 

**Sub-filtrations** G<sup>[</sup><sup>_k_]</sup> **and processes** _L_<sup>[</sup> _t_<sup>_k_]</sup><sup>**.**</sup> Recall that G = ( _Gt_ )<sup>_∞_</sup> _t_ =0<sup>, and define the G[1]</sup><sup>_, . . . ,_G[</sup><sup>_h_]as</sup> follows: for each _k_ = 1 _, . . . , h_ , 



Because � _<u>t−hk</u>_ � _h_ + _k ≤_ � _<u>t−hk</u>_ � _h_ + _k ≤ t_ , we have _Gt_<sup>[</sup><sup>_k_]</sup> _⊆Gt ∀t_ , i.e., G<sup>[</sup><sup>_k_]</sup> is a sub-filtration of G for each _k_ . (Each _G_<sup>[</sup><sup>_k_]</sup> only updates its filtration every _h_ steps.) In the following, we fix _λ ∈_ [0 _,_ 1 _/c_ ) and omit any dependence on it for notational convenience. For each _k_ = 1 _, . . . , h_ , define the process ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>as follows:</sup><sup>_L_[</sup> 0<sup>_k_]:= 1 and, for each</sup><sup>_t ≥_1,</sup> 



where<sup>�</sup> _i∈∅_<sup>(</sup><sup>_·_) = 1 and</sup> 



(We index (79) by _i −_ 1, because it only consists of _Gi−_ 1-measurable terms aside from _yi_ + _h−_ 1. For example, _δi_<sup>(</sup><sup>_h_)</sup> = E _i−_ 1[ _δ_<sup>ˆ</sup> _i_<sup>(</sup><sup>_h_)</sup> ] is _Gi−_ 1-measurable.) Then, each ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>is an adapted process w.r.t. G,</sup> because the last index of _It_<sup>[</sup><sup>_k_]</sup> is at most _t − h_ + 1, and the outcome corresponding to that index is _yt_ , which is _Gt_ -measurable. 

43 

( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>**isatestsupermartingalew.r.t.**G[</sup><sup>_k_]</sup><sup>**foreach**</sup><sup>_k_</sup><sup>**.**</sup> Recall that E[ _δ_<sup>ˆ</sup> _i_<sup>(</sup><sup>_h_)</sup> _| Gi−_ 1] = _δi_<sup>(</sup><sup>_h_)</sup> by definition. Since the score differentials are bounded by assumption, the proof of Proposition 1 (with _yi_ replaced with _yi_ + _h−_ 1 in the proof) implies that 



Now, if _t < h_ or � _<u>t−hk</u>_ � =<sup>_<u>t−</u>_</sup> _h_<sup>_<u>k</u>_(i.e., not an integer), then</sup><sup>_I_</sup> _t_<sup>[</sup><sup>_k_]</sup> = _It_<sup>[</sup> _−_<sup>_k_]</sup> 1<sup>by construction, so</sup><sup>_L_</sup> _t_<sup>[</sup><sup>_k_]</sup> = _L_<sup>[</sup> _t_<sup>_k_</sup> _−_<sup>]</sup> 1<sup>.</sup> On the other hand, if _t ≥ h_ and � _<u>t−hk</u>_ � =<sup>_<u>t−</u>_</sup> _h_<sup>_<u>k</u>_, then algebra shows that</sup><sup>_L_</sup> _t_<sup>[</sup><sup>_k_]</sup> = _L_<sup>[</sup> _t_<sup>_k_</sup> _−_<sup>]</sup> 1<sup>_·lt−h_(</sup><sup>_yt_), and also</sup> that _Gt_<sup>[</sup><sup>_k_</sup> _−_<sup>]</sup> 1<sup>=</sup><sup>_G_�</sup><sup><u>(</u></sup><sup>_t−_1</sup> _h_<sup><u>)</u></sup><sup>_−k_</sup> � _h_ + _k_<sup>=</sup><sup>_G_</sup> (<sup>_<u>t−</u>_</sup> _h_<sup>_<u>k</u>−_1)</sup><sup>_h_+</sup><sup>_k_=</sup><sup>_Gt−h_.Thus,</sup> 



The above algebra also shows that each multiplicative increment of _L_<sup>[</sup> _t_<sup>_k_]</sup> is either constant (1) or G<sup>[</sup> _t_<sup>_k_]-</sup> measurable. Therefore, ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>is a test supermartingale w.r.t. G[</sup><sup>_k_].</sup> 



We thus have, _P_ -almost surely, 



In other words, under any _P ∈H_ 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_),</sup><sup>_E_</sup> _t_<sup>[</sup><sup>_k_]</sup> is upper-bounded by _L_<sup>[</sup> _t_<sup>_k_]</sup> for each _k_ , where ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0 is a test supermartingale w.r.t. G<sup>[</sup><sup>_k_]</sup> . By the supermartingale optional stopping theorem (e.g., Theorem 4.8.4, Durrett (2019)), we thus have that, for any stopping time _τ_<sup>[</sup><sup>_k_]</sup> w.r.t. G<sup>[</sup><sup>_k_]</sup> , 



under any _P ∈H_ 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_).</sup> Finally, the construction (77) implies that, for any stopping time _τ_ w.r.t. G, the mapping _τ �→ τ_<sup>[</sup><sup>_k_]</sup> defined by 



gives a stopping time w.r.t. G<sup>[</sup><sup>_k_]</sup> (Henzi and Ziegel, 2022), where _τ_<sup>[</sup><sup>_k_]</sup> _∈{τ, τ_ + 1 _, . . . , τ_ + ( _h −_ 1) _}_ . Therefore, for any stopping time _τ_ w.r.t. G, 



for any _P ∈H_ 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_).</sup> 

44 

(p<sup>pw</sup> _t_<sup>)</sup><sup>_∞_</sup> _t_ =0<sup>**is a p-process for**</sup><sup>_H_</sup> 0<sup>pw</sup><sup>**.**</sup> The key idea here is to first use the fact that _L_<sup>[</sup> _t_<sup>_k_]</sup> is a test supermartingale w.r.t. G<sup>[</sup><sup>_k_]</sup> that upper-bounds _Et_<sup>[</sup><sup>_k_], for each</sup><sup>_k∈{_1</sup><sup>_, . . . , h}_, and then use the time-uniform</sup> equivalence lemma for probabilities (Ramdas et al., 2020), along with a p-merging function (Vovk and Wang, 2021), to obtain a combined p-process. 

First, define the following process for each _k_ = 1 _, . . . , h_ : 



The process involves the running supremum of ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>, which is a test supermartingale w.r.t. G[</sup><sup>_k_] as</sup> we showed earlier. In particular, (84) implies that p<sup>[</sup> _t_<sup>_k_]</sup> _≥_ q<sup>[</sup> _t_<sup>_k_]</sup> for all _t_ and _k_ under _P ∈H_ 0<sup>pw.</sup> Applying Ville (1939)’s inequality to ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>, for any</sup><sup>_P_,</sup> 



Then, under any _P ∈H_ 0<sup>pw, the fact that p</sup> _t_<sup>[</sup><sup>_k_]</sup> _≥_ q<sup>[</sup> _t_<sup>_k_]</sup> under _P_ implies 



Now, following an earlier proof in (79) where we showed that ( _L_<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>isanadaptedprocess</sup> w.r.t. the game filtration G, we can analogously show that ( _Et_<sup>[</sup><sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>is also an adapted process w.r.t. G,</sup> and so is (p<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =0<sup>byitsdefinition.Then,byLemma2ofRamdasetal.(2020),(i)</sup><sup>_⇒_(iii),equa-</sup> tion (90) implies that 



for any stopping time _τ_ w.r.t. G and _P ∈H_ 0<sup>pw(</sup><sup>_h_).In other words, (p[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =1<sup>is a p-process for</sup><sup>_H_</sup> 0<sup>pw(</sup><sup>_h_)</sup> w.r.t. G, for each _k ∈{_ 1 _, . . . , h}_ . 

Finally, we can merge the p-processes (p<sup>[</sup> _t_<sup>_k_])</sup><sup>_∞_</sup> _t_ =1<sup>at any G-stopping times.For any G-stopping time</sup> _τ_ , using the harmonic average p-merging function by Vovk and Wang (2021) combined with (91) gives, for any _P ∈H_ 0<sup>pw,</sup> 



( _Et_<sup>pw)</sup><sup>_∞_</sup> _t_ =0<sup>**is an e-process for**</sup><sup>_H_</sup> 0<sup>pw</sup><sup>_._</sup> This follows directly from the validity of a p-to-e calibrator for p-processes (e.g., Proposition 12, Ramdas et al. (2020)). 

The statements and proofs for the weak null _H_ 0<sup>w(</sup><sup>_h_)arecompletelyanalogous,exceptthatin-</sup> stead of taking averages across the _h_ sub-processes we have to take the minimum/maximum for e-/pprocesses, because the weak null only implies that there exists some _k_ for which ∆<sup>[</sup> _t_<sup>_k_]</sup> _≤_ 0. 

**Proposition 6** (Sequential inference for _H_ 0<sup>w(</sup><sup>_h_))</sup><sup>**.**</sup><sup>_Assume the same setup as Proposition 5.Then, for_</sup> _each λ ∈_ [0 _,_ 1 _/c_ ) _, the following statements are true:_ 

_1. (Minimum sequential e-values.) The process_ 



_satisfies_ E _P_ [ _E_<sup>¯</sup> _τ_<sup>pw</sup> + _h−_ 1<sup>(</sup><sup>_λ_)]</sup><sup>_≤_1</sup><sup>_for any_G</sup><sup>_-stopping time τand any P∈H_</sup> 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_._</sup> 

45 

_2. (P-process.) The process_ (p<sup>w</sup> _t_<sup>)</sup><sup>_∞_</sup> _t_ =1<sup>_defined by_</sup> 



_is an p-process for H_ 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_w.r.t._G</sup><sup>_._</sup> 

_3. (Calibrated e-process.) Let f_ : [0 _,_ 1] _→_ [0 _, ∞_ ) _be any p-to-e calibrator. Then, the process_ ( _Et_<sup>w)</sup><sup>_∞_</sup> _t_ =0<sup>_defined by E_</sup> 0<sup>w= 1</sup><sup>_and_</sup> 



_is an e-process for H_ 0<sup>w(</sup><sup>_p, q_;</sup><sup>_h_)</sup><sup>_w.r.t._G</sup><sup>_._</sup> 

The methods described in Propositions 5 and 6 both provide valid options for sequentially comparing lag- _h_ forecasters. While _Et_<sup>pw</sup> may involve a seemingly less intuitive null hypothesis, it upperbounds _Et_<sup>w,anditcangrowmorequicklywheneithernullisfalse.Rejecting</sup><sup>_H_</sup> 0<sup>pw(</sup><sup>_p, q_;</sup><sup>_h_)implies</sup> that there exists some _k ∈{_ 1 _, . . . , h}_ such that ∆<sup>[</sup> _t_<sup>_k_]</sup> _>_ 0 for some _t_ . For example, if _h_ = 2, then it implies _p_ outperforms _q_ on average on either odd or even days. A scenario in which rejecting _H_ 0<sup>pw(</sup><sup>_h_)</sup> would clearly not imply _H_ 0<sup>w(</sup><sup>_h_)iswhen(coincidentally)thereisseasonalityofperiodexactly</sup><sup>_h_in</sup> the game — e.g., when comparing 7-day forecasts for a sequence of outcomes that have a different distribution every weekend, _Et_<sup>wand</sup><sup>_E_</sup> _t_<sup>pw</sup> may differ significantly. A simple way to mitigate this issue is to simply monitor both e-processes (depending on the use case). 

In Table 5, we list the sequential e-values for _H_ 0<sup>w(Proposition6),</sup><sup>_H_</sup> 0<sup>pw</sup> (Proposition 5), and _H_ 0<sup>s</sup> (Henzi and Ziegel (2022); denoted as _E_<sup>¯s</sup> ), for the weather comparison tasks in Section 5.3 with lags _h_ = 1 _, . . . ,_ 5. As in Henzi and Ziegel (2022), no stopping is applied in any of the sequential e-values. As shown, while _E_<sup>¯w</sup> tends to be overly conservative, _E_<sup>¯pw</sup> remains relatively powerful despite testing a substantially weaker null than the strong null (for _E_<sup>¯s</sup> ). Across different locations and lags, _E_<sup>¯s</sup> is generally large ( _≥_ 20) whenever _E_<sup>¯pw</sup> is large, and this is explained by the inclusion relationship between the nulls in (71). The comparison of HCLR against HCLR_ in Zurich is the only case where _E_<sup>¯pw</sup> exceeds _E_<sup>¯s</sup> . In this case, the e-values drawn over time (similar to Figure 5) show that there are multiple time periods (2012-2013 and 2014-2015) during which both _E_<sup>¯s</sup> and _E_<sup>¯pw</sup> decrease substantially, and it is possible that the choice of the hyperparameter or the variance-adaptivity of our e-values affects how quickly they “rebound” after such sharp decreases. 

We close with the note that the choice of how aggressively one can bet, either via the choice of the hyperparameter in the mixture distribution _F_ for _E_<sup>¯w</sup> and _E_<sup>¯pw</sup> (cf. Section 4.4) or the alternative probability _π_ 1 for _E_<sup>s</sup> , directly affects the power of these e-values. Developing powerful strategies for choosing _F_ in the lagged scenario remains a problem deserving of future investigation. 

## **F Inference for Predictable Subsequences and Bounds** 

Martingale theory tells us that we can substitute each variable in the exponential supermartingale (12) with any predictable terms, similar to ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>in Theorem 2.In doing so, we must make sure that the</sup> resulting test supermartingale leads to estimating/testing an appropriate quantity of interest. Here, we illustrate two useful extensions involving this general technique. 

### **F.1 Inference for Predictable Subsequences** 

Suppose that each round of our forecast comparison game (Game 1) happens daily, but we are only interested in comparing the forecasters on weekdays, on every other day, or more interestingly, on 

46 

|**Location**|**La**|**H**|**CLR/ID**|**R**|**ID**|**R/HCL**|**R–**|**HC**|**LR/HC**|**LR–**|
|---|---|---|---|---|---|---|---|---|---|---|
||**g**|¯_E_<sup>w</sup>|¯_E_<sup>pw</sup>|¯_E_<sup>s</sup>|¯_E_<sup>w</sup>|¯_E_<sup>pw</sup>|¯_E_<sup>s</sup>|¯_E_<sup>w</sup>|¯_E_<sup>pw</sup>|¯_E_<sup>s</sup>|
||1|0.012|0.012|0.000|_>_100|_>_100|_>_100|1.083|1.083|_>_100|
||2|0.021|0.033|0.000|0.196|1.659|_>_100|0.510|1.196|_>_100|
|Brussels|3|0.049|0.060|0.006|0.060|0.121|1.786|0.698|2.289|_>_100|
||4|0.053|1.032|22.811|0.018|0.042|0.000|0.114|1.855|_>_100|
||5|0.145|0.714|_>_100|0.021|0.034|0.000|0.254|19.411|_>_100|
||1|0.034|0.034|0.000|1.284|1.284|_>_100|_>_100|_>_100|_>_100|
||2|0.022|0.029|0.000|1.573|7.223|_>_100|1.537|69.508|_>_100|
|Frankfurt|3|0.022|0.041|0.000|0.311|3.814|_>_100|0.836|_>_100|_>_100|
||4|0.047|0.214|0.361|0.033|0.090|0.122|0.163|27.920|_>_100|
||5|0.037|0.334|2.468|0.023|0.104|0.001|0.173|1.781|_>_100|
||1|0.041|0.041|0.029|0.277|0.277|1.351|0.285|0.285|2.845|
||2|0.038|0.038|0.021|0.289|0.321|2.002|0.164|0.200|5.178|
|London|3|0.037|0.061|0.185|0.087|0.367|0.203|0.141|0.241|9.613|
||4|0.077|0.121|1.751|0.051|0.108|0.018|0.077|1.714|8.428|
||5|0.070|0.208|4.949|0.032|0.066|0.002|0.113|0.279|1.427|
||1|0.034|0.034|0.003|6.670|6.670|25.692|_>_100|_>_100|61.747|
||2|0.054|0.061|0.012|0.328|0.415|19.229|2.195|_>_100|74.745|
|Zurich|3|0.066|0.487|1.079|0.037|0.197|0.661|1.877|7.311|94.613|
||4|0.091|1.553|30.478|0.023|0.066|0.004|0.210|54.131|47.069|
||5|0.082|8.436|_>_100|0.026|0.053|0.000|0.192|3.964|40.648|



Table 5: Lag- _h_ sequential e-values between pairs of statistical postprocessing methods for ensemble _E_ weather forecasts across different locations and lags, where¯<sup>w</sup> , _E_ ¯<sup>pw</sup> , and _E_ ¯<sup>s</sup> indicate the lag- _h_ sequential e-values for _T_ theis the last time step (January 01, 2017).lag- _h_ weak, period-wise weak, and strong nulls, respectively. All procedures use the Brier score as the scoring rule. “p/q” indicates the null that “p is no better than q.” Generally speaking, _E_<sup>¯w</sup> is the most conservative, while _E_<sup>¯pw</sup> can be powerful against its relatively weak null (compared to the strong null for _E_<sup>¯s</sup> ). 

days after some specific event happens (e.g., days following market crashes). To formalize this, we introduce a predictable _{_ 0 _,_ 1 _}_ -valued process _ξ_ := ( _ξt_ )<sup>_∞_</sup> _t_ =1<sup>andthenestimate/testtheaveragescore</sup> differential _only_ at times when _ξt_ = 1. The resulting parameter of interest is expressed as follows: 



where _δi_ = E _i−_ 1[ _δ_<sup>ˆ</sup> _i_ ] = E _i−_ 1[ _S_ ( _pi, yi_ ) _− S_ ( _qi, yi_ )] and _ξ_ 1: _t_ = ( _ξ_ 1 _, . . . , ξt_ ). ∆ _t_ ( _ξ_ 1: _t_ ) measures the time-varying average score differential _only_ for times when _ξi_ = 1. Henzi and Ziegel (2022) introduce an analogous extension to testing the strong null (21), where the predictable condition _ξt_ = 1 �max _{pt, qt} ≥_ 2<sup><u>1</u></sup> � is used to compare extreme precipitation forecasts. 

Because the conditions are predictable, we have the property that E _i−_ 1[ _ξiδ_<sup>ˆ</sup> _i_ ] = _ξi_ E _i−_ 1[ _δ_<sup>ˆ</sup> _i_ ] = _ξiδi_ , from which the proofs of Theorem 1 (assuming sub-Gaussianity), as well as Theorem 2 and Theorem 3 

47 

(assuming boundedness), straightforwardly follow. For example, for each _λ ∈_ [0 _,_ 1 _/c_ ), consider 



Then, under the same conditions as Proposition 1, _Lt_ ( _λ_ ; _ξ_ 1: _t_ ) is a test supermartingale w.r.t. G: 



for each _t ≥_ 1. We used the predictability of ( _ξt_ )<sup>_∞_</sup> _t_ =1<sup>in (99) and the boundedness condition (see proof</sup> of Proposition 1) in (100). Applying this to the proof of Theorem 2 shows that we can construct an EB CS for (∆ _t_ ( _ξ_ 1: _t_ ))<sup>_∞_</sup> _t_ =1<sup>.</sup> 

Similarly, we can also derive the corresponding sub-exponential e-process for the null _H_ 0<sup>w(</sup><sup>_ξ_):</sup> ∆ _t_ ( _ξ_ 1: _t_ ) _≤_ 0 _, ∀t_ . This e-process is given by 



for any _λ ∈_ [0 _,_ 1 _/c_ ). This is an e-process because, under _H_ 0<sup>w(</sup><sup>_ξ_), we have that exp(</sup><sup>_−λ_�</sup><sup>_t_</sup> _i_ =1<sup>_ξiδi_)=</sup> � _i_ : _ci_ =1<sup>exp(</sup><sup>_−λδi_)</sup><sup>_≥_1, and thus</sup> 



Since _Et_ ( _λ_ ; _ξ_ 1: _t_ ) is upper-bounded by the test supermartingale _Lt_ ( _λ_ ; _ξ_ 1: _t_ ) for all _t_ under _H_ 0<sup>w(</sup><sup>_ξ_),it</sup> follows that _Et_ ( _λ_ ; _ξ_ 1: _t_ ) is an e-process for _H_ 0<sup>w(</sup><sup>_ξ_) (Ramdas et al., 2020).</sup> 

In summary, both the CS and the e-process remain valid under predictable conditions. 

### **F.2 Inference Under Predictable Bounds** 

For Theorems 2 and 3, we require that the pointwise score differentials are bounded by some fixed constant, i.e., _|δ_<sup>ˆ</sup> _i| ≤_ 2<sup>_<u>c</u>_forall</sup><sup>_i_,forsome</sup><sup>_c∈_(0</sup><sup>_, ∞_).Inpractice,thismayberestrictivewhenthe</sup> value of _c_ is not known a priori or its range shifts drastically over time. One way to mitigate this issue is to have a predictable bound ( _ci_ )<sup>_∞_</sup> _i_ =1<sup>at each round, such that</sup> 



for _i ≥_ 1, instead of having a uniform bound over all rounds. Predictable bounds can also be useful in cases where one can guess how bad/good the forecasts can be before each new round begins. 

Here, we show that we can extend both Theorem 2 and Theorem 3 to work for predictably bounded score differentials. This result depends on the following facts about the exponential CGF-like function, _ψE,c_ ( _λ_ ), _as a function of its scale c_ . Below, we take 1 _/_ 0 = _∞_ . 

**Lemma 2.** _For each λ ≥_ 0 _, the function fλ_ ( _c_ ) := _ψE,c_ ( _λ_ ) = _c_<sup>_−_2</sup> [ _−cλ −_ log(1 _− cλ_ )] _is nondecreasing and convex on c ∈_ (0 _,_ 1 _/λ_ ) _. Furthermore, fλ is strictly increasing and strongly convex on c ∈_ (0 _,_ 1 _/λ_ ) _if and only if λ >_ 0 _._ 

48 



<!-- Start of picture text -->
Fixed  CGF Type<br>15 15<br>= 0.9 E, 1 ( )<br>= 0.95 N, 1 ( )<br>10 = 1.0 10<br>5 5<br>0 0<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>c<br>)<br>)<br>(<br>E c, (<br><!-- End of picture text -->

Figure 6: _Left:_ Plots of the exponential CGF-like function _fλ_ ( _c_ ) = _ψE,c_ ( _λ_ ) against _c ∈_ (0 _,_ 1 _/λ_ ), for fixed _λ_ values of 0 _._ 9, 0 _._ 95, and 1 _._ 0. For each _λ ≥_ 0, _fλ_ ( _c_ ) is strictly increasing and strongly convex on _c ∈_ (0 _,_ 1 _/λ_ ). _Right:_ Comparing _ψE,_ 1( _λ_ ), as a function of _λ ∈_ [0 _,_ 1), with the Gaussian CGF _ψN,_ 1( _λ_ ) = _λ_<sup>2</sup> _/_ 2. 

_Proof._ Since _fλ_ ( _c_ ) is twice differentiable w.r.t. _c_ , it suffices to show that _fλ_<sup>_′_(</sup><sup>_c_)</sup><sup>_≥_0 and</sup><sup>_f_</sup> _λ_<sup>_′′_(</sup><sup>_c_)</sup><sup>_≥_0 for</sup> all _c_ , and also that _fλ_<sup>_′_(</sup><sup>_c_)</sup><sup>_>_0 and</sup><sup>_f_</sup> _λ_<sup>_′′_(</sup><sup>_c_)</sup><sup>_>_0 for all</sup><sup>_c_if and only if</sup><sup>_λ >_0.</sup> Given that 0 _≤ cλ <_ 1, we utilize the Taylor series of _x �→−_ log(1 _− x_ ) at _x_ = 0: 



which converges (absolutely). It then follows that 



Taking first derivatives term-by-term, 



Given that _c >_ 0, we have that _fλ_<sup>_′_(</sup><sup>_c_)</sup><sup>_≥_0 for any</sup><sup>_λ≥_0.Furthermore,we have that</sup><sup>_f_</sup> _λ_<sup>_′_(</sup><sup>_c_)</sup><sup>_>_0 for</sup> _λ >_ 0 and _fλ_<sup>_′_(</sup><sup>_c_) = 0 for</sup><sup>_λ_= 0.</sup> 

Similarly, taking second derivatives term-by-term, 



Given that _c >_ 0, we have that _fλ_<sup>_′′_(</sup><sup>_c_)</sup><sup>_≥_0 for any</sup><sup>_λ≥_0.Furthermore,we have that</sup><sup>_f_</sup> _λ_<sup>_′′_(</sup><sup>_c_)</sup><sup>_>_0 for</sup> _λ >_ 0 and _fλ_<sup>_′′_(</sup><sup>_c_) = 0 for</sup><sup>_λ_= 0.</sup> 

In Figure 6, we plot _ψE,c_ ( _λ_ ) as a function of _c_ , illustrating that it is indeed strictly increasing and strongly convex for different values of _λ >_ 0, and we also show that _ψE,_ 1 as a function of _λ_ approximates _ψN,_ 1( _λ_ ) = _λ_<sup>2</sup> _/_ 2 as _λ →_ 0<sup>+</sup> . 

Now, we derive an e-process that involves predictable bounds and is upper-bounded by a test supermartingale that uses a uniform bound (12). First, let _c_ 0 be a (possibly infinite) constant such that 

49 

_ci ≤ c_ 0 for all _i_ . Also, let ˆ _vi_ = ( _δ_<sup>ˆ</sup> _i − γi_ )<sup>2</sup> where ( _γi_ )<sup>_∞_</sup> _i_ =1<sup>is any predictable sequence as in Theorems 2</sup> and 3. 

Now, for each _λ ∈_ [0 _,_ 1 _/c_ 0) (as before, we set 1 _/∞_ = 0 and [0 _,_ 0) = _{_ 0 _}_ ), define the following processes: _L_ �0<sup>(</sup><sup>_λ_) =</sup><sup>_L_</sup> 0<sup>(</sup><sup>_λ_) = 1, and for</sup><sup>_t ≥_1,</sup> 



(If _c_ 0 = _∞_ , then _ψE,c_ 0 is not well-defined, so set _L_ � _t_<sup>(</sup><sup>_λ_) = 1 for all</sup><sup>_t ≥_1.)</sup> 

**Proposition 7.** _Suppose that |δ_<sup>ˆ</sup> _i| ≤_<sup>_<u>c</u>_</sup> 2<sup>_<u>i</u>, where_(</sup><sup>_ci_)</sup> _i_<sup>_∞_</sup> =1<sup>_is a strictly positive predictable sequence.Also,_</sup> _let V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −γi_)2</sup><sup>_, where_(</sup><sup>_γi_)</sup> _i_<sup>_∞_</sup> =1<sup>_is any_</sup> � _−_<sup>_<u>c</u>_</sup> 2<sup>_<u>i</u>,_</sup><sup>_<u>c</u>_</sup> 2<sup>_<u>i</u>_</sup> � _-valued predictable sequence. Then, for each λ ∈_ [0 _,_ 1 _/c_ 0) _, the following statements are true:_ 

_1. L_ � _t_<sup>(</sup><sup>_λ_)</sup><sup>_≤L_</sup> _t_<sup>(</sup><sup>_λ_)</sup><sup>_for all t ≥_1</sup><sup>_;_</sup> 

_2. The process_ ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>_is a test supermartingale w.r.t._G</sup><sup>_;_</sup> 

_3._ (A predictably-bounded e-process.) _The process_ ( _Et_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>_, defined as E_0(</sup><sup>_λ_) = 1</sup><sup>_and_</sup> 



_is an e-process for H_ 0<sup>w(</sup><sup>_p, q_) : ∆</sup><sup>_t≤_0</sup><sup>_,∀t ≥_1</sup><sup>_._</sup> 

_Proof._ 1. Using the fact that _ci ≤ c_ 0 for each _i_ and that _ψE,c_ ( _λ_ ) is non-decreasing in _c_ by Lemma 2, we obtain 



2. If _c_ 0 = _∞_ , then we must have _λ_ = 0, so ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>alwaystakesthevalue1andisa(triv-</sup> ial) test supermartingale. Otherwise, Proposition 2 directly implies that ( _Lt_ ( _λ_ ))<sup>_∞_</sup> _t_ =0<sup>isatest</sup> supermartingale w.r.t. G. 

3. Because ( _ci_ )<sup>_∞_</sup> _i_ =1<sup>ispredictablew.r.t.G,theprocess(</sup><sup>_Et_(</sup><sup>_λ_))</sup><sup>_∞_</sup> _t_ =0<sup>isadaptedw.r.t.G.</sup> Then, _Et_ ( _λ_ ) _≤ Lt_ ( _λ_ ) ( _P_ -a.s.) for all _t_ under any _P ∈H_ 0<sup>w(</sup><sup>_p, q_),asintheproofofTheorem3,</sup> and thus the result follows by Corollary 22 of Ramdas et al. (2020). 

Note that, if a constant bound _c_ 0 = _c >_ 0 were known _a priori_ , then _L_ � _t_<sup>(</sup><sup>_λ_)coincideswith</sup> the exponential test supermartingale in Equation (12). The e-process (110) can be more powerful than using the analogous ( _E_ � _t_<sup>(</sup><sup>_λ_))</sup><sup>_∞_</sup> _t_ =0<sup>involving</sup><sup>_c_0in some cases, although taking the mixture over</sup><sup>_λ_</sup> (Section 4.3.4) may not yield a closed form. 

50 

## **G Generalizations To Other Outcome and Forecast Types** 

In principle, the game-theoretic approach we describe in Section 4.1 can straightforwardly generalize beyond the case of probability forecasts on dichotomous events. We briefly discuss two such generalizations and to what extent our methods are applicable in each case. 

The first is to the case of _C_ -categorical outcomes, for _C ≥_ 2. We can start with the gametheoretic setup (Game 1) and parameterize the outcome space using _C_ -dimensional length-1 binary vectors, i.e., _Y_ = _{_ **e** _c}_<sup>_C_</sup> _c_ =1<sup>where</sup><sup>**e**</sup><sup>_c_=[1 (</sup><sup>_i_=</sup><sup>_c_)]</sup><sup>_C_</sup> _i_ =1<sup>,and the set of forecasts as the</sup><sup>_C_-dimensional</sup> probability simplex, i.e., _P_ = ∆<sup>_C−_1</sup> = _{_ **p** _∈_ [0 _,_ 1]<sup>_C_</sup> :<sup>�</sup><sup>_C_</sup> _c_ =1<sup>_p_(</sup><sup>_c_)=1</sup><sup>_}_.Realityalsomakesits</sup> choices from ∆<sup>_C−_1</sup> . Note that, if _C_ = 2, we can recover the binary case via the mapping **p** = (1 _− p, p_ ), for _p ∈_ [0 _,_ 1]. Then, by choosing any bounded scoring rule for categorical outcomes, we can straightforwardly apply Theorems 2 and 3 to obtain CSs and e/p-processes (respectively) on the average score differentials. The _C_ -dimensional Brier score, defined as _S_ ( **p** _,_ **y** ) = 1 _−∥_ **p** _−_ **y** _∥_<sup>2</sup> 2<sup>,is</sup> bounded within [0 _,_ 1]; the spherical and zero-one scores can be defined analogously (Gneiting and Raftery, 2007) and are similarly bounded. We note that using the normalized Winkler score to utilize unbounded scores, as in Section D, is not straightforward. 

The next extension is to the case of continuous outcomes. In this case, we can once again start with the game-theoretic setup (Game 1) and parameterize the outcome space as _Y ⊆_ R<sup>_d_</sup> for some _d ≥_ 1. At each round _t_ , Reality now chooses an arbitrary distribution _rt_ on _Y_ , from which _yt_ is sampled. Depending on the specific forecasting task, the forecasters may either predict (i) certain functional(s) of the outcome distribution, denoted as Γ( _P_ ) for each _P ∈P_ , or (ii) the CDF (or density) itself. As an example for (i), each forecaster may predict a level- _α_ (e.g., 95%) prediction interval ( _lt, ut_ ), in which case the statistician can use the _α_ -interval score (Dunsmore, 1968): 



for ( _l, u_ ) _⊆Y_ and _y ∈Y_ . As an example for (ii), each forecaster may predict a (Borel-measurable) CDF _Ft_ for _yt_ , in which case the statistician can use the continuously ranked probability score (CRPS) (Matheson and Winkler, 1976): 



for any CDF _F_ and outcome _y ∈Y_ . In either case, our main results (Theorems 2 and 3) are applicable when the associated score differentials are bounded. Specifically, we can allow the choices of _Y_ , _P_ , and _S_ such that _P ⊆P_<sup>(</sup><sup>_c_)</sup> , where 



for some _c ∈_ (0 _, ∞_ ). For instance, if _Y_ = [0 _,_ 1], then our main theorems can be used to compare mean, quantile, or interval forecasts on _Y_ , using the corresponding scoring rule in each case (Gneiting, 2011). If (114) is restrictive for the use case, then one may consider using predictable bounds (Section F.2) or the asymptotic CS (Section C). Deriving a fully general anytime-valid procedure for unbounded domains and scoring rules remains an open problem. 

In Table 6, we summarize these extensions based on the different choices of the outcome space _Y_ and the forecast type _P_ within Game 1. 

51 

|**Outcome Type**|**Categorical**|**Continuous**||
|---|---|---|---|
|Domain<br>Reality’s Choice|_Y_ =_{_**e**_c}_<sup>_C_</sup><br>_c_=1<br>_rt ∈_∆<sup>_C−_1</sup>|_Y ⊆_R<sup>_d_</sup><br>_rt ∈_∆(_Y_)(arbitrary d|istribution)|
|**Forecast Type**|**Probability**|**Functional**|**Distribution**|
|Domain|_P_ = ∆<sup>_C−_1</sup>|Γ(_P_)|_P ⊆_∆(_Y_)|
|Forecast Examples|any_C_-dim. probability|mean, prediction interval|CDF|
|Score Examples|Brier, spherical, 0-1, log scores|quadratic, interval scores|CRPS|
|Thms.2&3apply|if_P ⊆P_<sup>(</sup><sup>_c_)</sup>|for some_c ∈_(0_, ∞_)||



Table 6: Different specifications of Game 1 based on the outcome space and the forecast type, and the types of scoring rules that can be used in each case. In principle, the game-theoretic setup in our main paper (Section 4.1) can straightforwardly extend to these settings; our main approaches (Theorems 2 and 3) extend to cases where the score differentials are bounded. 

## **H Comparison with Other Forecast Comparison Methods** 

### **H.1 Methodological Comparison with Henzi and Ziegel (2022)** 

The biggest difference between our approach and Henzi and Ziegel (2022)’s (HZ) is in the difference between the strong and weak nulls, as described in the main text. Here, we summarize other methodological differences that are worth noting for practical use cases. HZ focus on sequentially comparing forecasts on dichotomous events using consistent scoring functions (Gneiting, 2011), which straightforwardly induce proper scoring rules, and they develop e-processes of the form 



for a [0 _,_ 1]-valued predictable sequence ( _λt_ )<sup>_∞_</sup> _t_ =1<sup>and a</sup><sup>_negatively oriented_scoring function</sup><sup>_S_. The form</sup> of˜ _δ_<sup>˜</sup> _i_ is exactly that of the Winkler score: by Lemma 1 and reversing the orientation of _S_ , we see that _δi_ = _−w_ ( _pi, qi, yi_ ), and thus HZ’s e-process can be interpreted as betting on the relative forecasting skill as determined by the pointwise empirical Winkler score (57). In this sense, our e-process for the weak Winkler null in Proposition 4 is a weak-null counterpart of HZ’s e-process. 

In terms of the specific form of the e-process, (115) is an example of a _product_ form e-process, contrasting with our _exponential_ form variant. The two forms of e-processes are both found the literature, such as the product form in Waudby-Smith and Ramdas (2023) and the exponential form in Howard et al. (2021) for estimating bounded means. Also, while the e-process we derive in (24) explicitly shows its variance-adaptive property and further utilizes the method of mixtures (Robbins, 1970), HZ’s e-process seeks to optimize its power by optimizing the growth rate of the e-process in the worst case (GROW) (Grünwald et al., 2023) under a chosen alternative (typically set to a convex combination of _pt_ and _qt_ ). 

In terms of use cases, the CSs perform estimation and thus provide information as to exactly _how much_ one forecaster is outperforming the other. The methods in our paper are agnostic to the different types of outcomes (Section G), so they can, e.g., be applied to forecasts on categorical outcomes with _C >_ 2 categories and to forecasts on bounded continuous outcomes. HZ’s approach is applicable to any consistent scoring functions (Gneiting, 2011) on binary outcomes and can also test for forecast dominance w.r.t. all consistent scoring functions. 

52 



<!-- Start of picture text -->
Forecasters 95% CS/CI for  t Cumulative Type I Error<br>1.0<br>1.00 0.06 EB CS EB CS GW Test<br>0.75 0.04 Fixed-Time CIt 0.8 DM Test Fixed-Time CI<br>0.02 0.6<br>0.50 0.00<br>0.25 reality (rt) 0.02 0.4<br>optimist 0.04 0.2<br>0.00 pessimist 0.06<br>0 2500 5000 7500 10000 0.0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Time Time Time<br>Probability Forecast<br><!-- End of picture text -->

Figure 7: _Left:_ Two forecasters, denoted as optimist (blue) and pessimist (orange), on a simulated reality sequence (gray). There is no performance gap between the two in Brier score. _Middle:_ The true average score differentials (∆ _t_ )<sup>_T_</sup> _t_ =1<sup>(dark red) along with the 95% EB CS (blue) and the fixed-</sup> time CI (yellow). _Right:_ Comparing the cumulative type I error rate for the EB CS (blue), the DM test of unconditional predictive ability (green), the GW test of conditional predictive ability (orange), and Lai et al. (2011)’s asymptotic CIs (yellow). All tests are for one-sided nulls of the form “optimist performs no better than the pessimist.” Unlike the EB CS, all classical fixed-time methods, including DM and GW tests, incur a cumulative miscoverage/false decision rate higher than _α_ = 0 _._ 05. 

### **H.2 Comparison with DM and GW Tests** 

As we highlighted in Section 2, the key difference between our work and existing forecast comparison methods, such as Diebold and Mariano (1995); Giacomini and White (2006); Lai et al. (2011); Ehm and Krüger (2018), is whether they have an anytime-valid guarantee. Here, we present additional experiments to illustrate that (i) the DM and GW tests are _not_ valid at arbitrary stopping times, like most other classical tests including Lai et al. (2011), and (ii) anytime-valid methods need not require larger sample sizes than DM and GW tests for high power. 

To recap, the DM test of _unconditional_ predictive ability tests 



where the scoring rule is assumed to depend only on the forecast error, e.g., _S_ ( _pn, yn_ ) = 1 _−_ ( _pn−yn_ )<sup>2</sup> . By the DM assumption, the loss differentials are assumed to be covariance stationary, implying that E[ _δ_<sup>ˆ</sup> _n_ ] = _δ_ for some fixed _δ_ at any _n_ . Given the (stationary) autocovariance function _γ_ ( _k_ ) for score differentials and a consistent estimator _f_<sup>ˆ</sup> (0) of its spectrum at frequency zero, the DM test uses the asymptotic normality under _H_ 0<sup>DM</sup> given by<sup>_√_</sup> _<u>n</u>_ <u>(∆</u><sup>ˆ</sup> _n − µ_ ) _/_ ~~�~~ 2 _πf_<sup>ˆ</sup> (0) ⇝ _N_ (0 _,_ 1). The GW test, on the other hand, is a test of _conditional_ predictive ability that tests 



Here, _m_ is the maximum window size that each forecaster can look back to, meaning that the test now depends on the forecasting model. The GW assumption allows for nonstationarity, although the test statistic involves weights that depend on mixing assumptions (Lai et al., 2011). 

First, we consider a simplistic setting in which ∆ _t_ = 0 for each time _t_ and both the DM and GW assumptions are met. We compare two forecasters, named optimist ( _pt_ ) and pessimist ( _qt_ ), that are equally apart from Reality ( _rt_ ) in their forecasts (Figure 7, left). For all methods, we test their form of the null that “the optimist is no better than the pessimist” under the Brier score. As expected, both the EB CS (Theorem 2) and the fixed-time CI (Lai et al., 2011) to quickly shrink to zero (Figure 7, middle), and also neither the DM nor GW test falsely rejects the null at _T_ = 10 _,_ 000. 

53 



<!-- Start of picture text -->
Forecasters 95% CS for  t H0 : "p is no better than q"<br>1.00 0.2 1.00<br>reality (rt)<br>0.75 k29 0.1 0.75<br>laplace Test<br>0.50 0.0 0.50 CR [SAVI]<br>HZ [SAVI]<br>0.25 0.1 EB CS 0.25 DM<br>t GW<br>0.00 0.00<br>0.2<br>0 2500 5000 7500 10000 0 2500 5000 7500 10000 0 2500 5000 7500 10000<br>Time Time Time<br>CS<br>p-value<br>Probability Forecast<br><!-- End of picture text -->

Figure 8: _Left:_ Two forecasters, k29 (blue) and laplace (orange), on a simulated reality sequence (gray) that induces a changepoint in the loss differentials later in the time horizon. _Middle:_ The 95% EB CS for (∆ _t_ )<sup>_T_</sup> _t_ =1<sup>usingtheBrierscore.∆</sup><sup>_t_stayszeroinitiallybuttrendspositivelater.</sup><sup>_Right:_P-</sup> values for the null “k29 is no better than laplace” at each sample size _t_ . CR (ours; blue) and HZ (yellow) are anytime-valid (SAVI), whereas DM (green) and GW (orange) are not. When ∆ _t_ quickly trends positive ( _t ≈_ 7300), all p-values shrink to zero, and neither CR nor HZ requires substantially many extra samples to get to zero compared to DM and GW. 

Now, we can also compute the cumulative type I error rate, which for p-values (p _t_ ) is given by _αt_ = _P_ ( _∃i ≤ t_ : p _i ≤ α_ ). For CS/CIs ( _Ct_ ), this is equivalent in this case to the cumulative miscoverage rate _αt_ = _P_ ( _∃i ≤ t_ : 0 _∈/ Ci_ ) that we used earlier in Section 5.1, because ∆ _t_ = 0 under any _P ∈H_ 0. The quantity is estimated over a repeated sampling of the data under _P_ . We expect that an anytime-valid procedure satisfies _αt ≤ α_ for any _t_ by definition, whereas classical fixed-time tests such as the DM and GW tests do not. As shown Figure 7 (right), the cumulative type I errors of both the DM and GW tests exceed the significance level of _α_ = 0 _._ 05 after roughly 100 and 1000 steps, respectively, and they continue to trend upward in log-scale. This confirms that the p-values obtained by DM or GW tests, much like the fixed-time CI, are overconfident under continuous monitoring and thus at data-dependent stopping times, even when their assumptions are met. In other words, the DM and GW tests, along with fixed-time CIs, do not have an anytime-valid guarantee. 

Next, we show that the anytime-validity of SAVI methods (CSs, e-processes, and p-processes), do not necessarily require larger sample sizes than the classical tests. We compare two forecasters, k29 with a 3-degree polynomial kernel ( _pt_ ) and laplace ( _qt_ ), whose average and pointwise score differentials stay close to zero for a while ( _t ≤_ 7000) until a sharp changepoint in the data is introduced and ∆ _t_ trends positive afterwards (Figure 8, left). Note that this invalidates the covariance stationarity assumption of the DM test. The EB CS for ∆ _t_ is drawn in the middle plot of Figure 8, which shows that the CS uniformly covers the time-varying average as expected. 

To illustrate that SAVI approaches do not necessarily require larger sample sizes for “detecting” this changepoint, we compare SAVI and non-SAVI p-values for the null that “k29 is no better than laplace” under the Brier score. First, we plot the p-process, p _t_ = 1 _/_ sup _i≤t Ei_ given by (26), where ( _Et_ )<sup>_∞_</sup> _t_ =0<sup>is the sub-exponential e-process (24) that corresponds to the LCB of the CS. This is denoted</sup> in the right plot of Figure 8 (denoted as “CR”). We also plot the p-process constructed from Henzi and Ziegel (2022)’s e-process ( _Et_<sup>HZ</sup> )<sup>_∞_</sup> _t_ =0<sup>via the same mapping, i.e., p</sup> _t_<sup>HZ</sup> = 1 _/_ sup _i≤t Ei_<sup>HZ</sup> . As shown in the plot, when compared against the DM and GW p-values, both our and HZ’s p-processes shrink to zero nearly as quickly, indicating that they require comparable amounts of data to reject the null when ∆ _t_ trends positive. 

54 

## **I Additional Experiment Details and Results** 

### **I.1 Additional Details & Results from Numerical Simulations** 

#### **I.1.1 Data Generation** 

The reality sequence ( _rt_ )<sup>_T_</sup> _t_ =1<sup>is specifically chosen to be non-IID and contain sharp changepoints, as</sup> drawn with gray dots in Figure 2: 



where 



and _ϵt ∼N_ (0 _,_ 0 _._ 1<sup>2</sup> ) is an independent Gaussian noise for each _t_ . 

#### **I.1.2 All Pairwise Comparisons in Numerical Simulations** 

In Figure 9, we plot the 95% EB, Hoeffding-style, and asymptotic CSs for all pairwise comparisons between the constant baseline (constant_0.5), the Laplace forecaster (laplace), and the K29 forecasters with the 3-degree polynomial kernel and the Gaussian RBF kernel with bandwidth 0 _._ 01 (k29_poly3 and k29_rbf0.01, respectively). The Brier score is used. Across all pairwise comparisons, both CSs uniformly cover the true score differentials across all times, regardless of whether the score differentials contain sharp changepoints and contain specific trends. 

55 



<!-- Start of picture text -->
95% Confidence Sequences on  t ; S=BrierScore<br>t (k29_poly3, k29_rbf0.01): (0.010, 0.019) t (k29_poly3, laplace): (0.056, 0.073) t (k29_poly3, constant_0.5): (0.056, 0.073)<br>0.10 0.10 0.10<br>t<br>EB CS 0.05 0.05 0.05<br>Hoeffding CS 0.00 0.00 0.00<br>Asymptotic CS<br>0.05 0.05 0.05<br>0.10 0.10 0.10<br>0 2500 5000 7500 10000 0 2500 5000 7500 10000 0 2500 5000 7500 10000<br>t (k29_rbf0.01, k29_poly3): (-0.019, -0.010) t (k29_rbf0.01, laplace): (0.043, 0.058) t (k29_rbf0.01, constant_0.5): (0.042, 0.058)<br>0.10 0.10 0.10<br>0.05 0.05 0.05<br>0.00 0.00 0.00<br>0.05 0.05 0.05<br>0.10 0.10 0.10<br>0 2500 5000 7500 10000 0 2500 5000 7500 10000 0 2500 5000 7500 10000<br>t (laplace, k29_poly3): (-0.073, -0.056) t (laplace, k29_rbf0.01): (-0.058, -0.043) t (laplace, constant_0.5): (-0.003, 0.003)<br>0.10 0.10 0.10<br>0.05 0.05 0.05<br>0.00 0.00 0.00<br>0.05 0.05 0.05<br>0.10 0.10 0.10<br>0 2500 5000 7500 10000 0 2500 5000 7500 10000 0 2500 5000 7500 10000<br>t (constant_0.5, k29_poly3): (-0.073, -0.056) t (constant_0.5, k29_rbf0.01): (-0.058, -0.042) t (constant_0.5, laplace): (-0.003, 0.003)<br>0.10 0.10 0.10<br>0.05 0.05 0.05<br>0.00 0.00 0.00<br>0.05 0.05 0.05<br>0.10 0.10 0.10<br>0 2500 5000 7500 10000 0 2500 5000 7500 10000 0 2500 5000 7500 10000<br>Time Time Time<br>t<br>CS for<br>t<br>CS for<br>t<br>CS for<br><!-- End of picture text -->

Figure 9: 95% EB (blue), Hoeffding-style (skyblue), and asymptotic (green) CSs on ∆ _t_ between four different forecasters (k29_poly3, k29_rbf0.01, laplace, and constant_0.5) plotted in Figure 2. Scoring rule is the Brier score, and positive values of ∆ _t_ indicate that the first forecaster is better than the second. In all comparisons, both CSs cover ∆ _t_ uniformly, and the width of the EB CS approaches that of the asymptotic CS as time grows large. 

56 



<!-- Start of picture text -->
Home Team Win Probability Forecasts (gray: playoffs)<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2 fivethirtyeight laplace<br>vegas k29<br>constant<br>0.0<br>Games (last 100 of 2019)<br>Probability/Outcome<br><!-- End of picture text -->

Figure 10: Various forecasters on the last 100 MLB games played in 2019 (including regular season and postseason). FiveThirtyEight and Vegas forecasts are publicly available forecasts online; Laplace and K29 forecasts are made using historical outcomes as data without external information. _Note that the forecasts are computed using data from a 10-year window (2010 to 2019), but we only show the last 100 games here for visualization purposes._ The shaded region highlights the playoffs (the last seven being the World Series games). 

### **I.2 Additional Details & Results from the MLB Experiment** 

For all MLB-related experiments, we choose _v_ opt = 100, given the longer time horizon considered (compared to other experiments in this paper). 

#### **I.2.1 Details on the MLB Forecasters** 

Here, we describe in detail the five Major League Baseball (MLB) forecasters that are compared in Section 5.2. Figure 10 illustrate their forecasts on the last 100 games of 2019. 

- 538: Game-by-game probability forecasts on every MLB game since 1871, available at https: //data.fivethirtyeight.com/#mlb-elo. According to the methodology report at https://fivethirtyeight.com/features/how-our-mlb-predictions-work/, the probabilities are calculated using an ELO-based rating system for each team, and gamespecific adjustments are made for the starting pitcher as well as other external factors (travel, rest, home field advantage, etc.). Before each new season, team ratings are reverted to the mean by one-third and combined with preseason projections from other sources (Baseball Prospectus’s PECOTA, FanGraphs’ depth charts, and Clay Davenport’s predictions). 

- vegas: Pre-game closing odds made on each game by online sports bettors, as reported by https://Vegas-Odds.com. (Download source: https://sports-statistics. com/sports-data/mlb-historical-odds-scores-datasets/.) The betting odds are given in the American format, so each odds _o_ is converted to its implied probability _p_ via _p_ = 1 ( _o ≥_ 0) 100+100 _o_<sup>+ 1 (</sup><sup>_o <_0)</sup> 100 _−−o o_<sup>.Then, for each matchup, the pair of implied probabil-</sup> ities for each team is rescaled to sum to 1. For example, given a matchup between team _A_ and ˜ 

- team _B_ with betting odds _oA_ = _−_ 140 and _oB_ = +120, the implied probabilities are _pA_ = 0 _._ 58 ˜ 

- and _pB_ = 0 _._ 45, and the rescaled probabilities are _pA_ = 0 _._ 56 and _pB_ = 0 _._ 44. 

57 



<!-- Start of picture text -->
95% Confidence Sequences on  t ; S=BrierScore<br>0.02 t (fivethirtyeight, vegas): (-0.003, -0.001) 0.02 t (fivethirtyeight, constant): (0.006, 0.009) 0.02 t (fivethirtyeight, laplace): (0.005, 0.008) 0.02 t (fivethirtyeight, k29): (0.008, 0.012)<br>EB CS 0.01 0.01 0.01 0.01<br>Asymptotic CS<br>0.00 0.00 0.00 0.00<br>0.01 0.01 0.01 0.01<br>0.02 0.02 0.02 0.02<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>0.02 t (vegas, fivethirtyeight): (0.001, 0.003) 0.02 t (vegas, constant): (0.007, 0.011) 0.02 t (vegas, laplace): (0.006, 0.010) 0.02 t (vegas, k29): (0.009, 0.014)<br>0.01 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00<br>0.01 0.01 0.01 0.01<br>0.02 0.02 0.02 0.02<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>0.02t (constant, fivethirtyeight): (-0.009, -0.006) 0.02 t (constant, vegas): (-0.011, -0.007) 0.02 t (constant, laplace): (-0.003, 0.000) 0.02 t (constant, k29): (0.000, 0.005)<br>0.01 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00<br>0.01 0.01 0.01 0.01<br>0.02 0.02 0.02 0.02<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>0.02 t (laplace, fivethirtyeight): (-0.008, -0.005) 0.02 t (laplace, vegas): (-0.010, -0.006) 0.02 t (laplace, constant): (-0.000, 0.003) 0.02 t (laplace, k29): (0.002, 0.005)<br>0.01 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00<br>0.01 0.01 0.01 0.01<br>0.02 0.02 0.02 0.02<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>0.02 t (k29, fivethirtyeight): (-0.012, -0.008) 0.02 t (k29, vegas): (-0.014, -0.009) 0.02 t (k29, constant): (-0.005, -0.000) 0.02 t (k29, laplace): (-0.005, -0.002)<br>0.01 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00<br>0.01 0.01 0.01 0.01<br>0.02 0.02 0.02 0.02<br>0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000 0 5000 10000 15000 20000 25000<br>Time Time Time Time<br>t<br>CS for<br>t<br>CS for<br>t<br>CS for<br>t<br>CS for<br><!-- End of picture text -->

Figure 11: Comparing MLB win probability forecasts from 2010 to 2019, using the EB and Hoeffdingstyle CSs at significance level _α_ = 0 _._ 05. _T_ = 25 _,_ 165 corresponds to the final game of the 2019 World Series. The Brier score is used. We find that, over time, the five forecasters are found to achieve significantly different predictive performance from each other (except laplace and constant), with the vegas forecaster achieving the best performance, followed by fivethirtyeight, laplace _≈_ constant, and k29. The title of each subplot includes the 95% EB CS at _T_ = 25 _,_ 165. 

- constant: a constant baseline predicting _pt_ = 0 _._ 5 for each _t_ . 

- laplace: A seasonally adjusted Laplace algorithm, representing the season win percentage for each team. Mathematically, it is given by _pt_ =<sup>_<u>k</u>_</sup> _n_<sup>_<u>t</u>_</sup> _t_<sup><u>+</u></sup> +1<sup>_<u>ct</u>_, where</sup><sup>_kt_is the number of wins so far</sup> in the season, _nt_ is the number of games played in this season, and _ct ∈_ [0 _,_ 1] is a baseline that represents the final probability forecast from the previous season, reverted to the mean by onethird. For example, if the previous season ended after round _t_ 0, then _kt_ =<sup>�</sup><sup>_t_</sup> _i_ =<sup>_−_</sup> _t_<sup>1</sup> 0<sup>1 (</sup><sup>_yi_= 1),</sup> _nt_ = _t − t_ 0, and _ct_ =<sup><u>2</u></sup> 3<sup>_· pt_0+</sup><sup><u>1</u></sup> 3<sup>_·_</sup> 2<sup><u>1</u>(with</sup><sup>_c_0=</sup> 2<sup><u>1</u>).The final probability forecast for a game</sup> between two teams is rescaled to sum to 1. 

- k29: The K29 algorithm applied to each team, using the Gaussian kernel with bandwidth 0 _._ 1, computed using data from the current season only. The final probability forecast for a game between two teams is rescaled to sum to 1. 

58 



<!-- Start of picture text -->
1-Day Precipitation Forecasts: Brussels<br>1.0<br>0.8<br>0.6 Forecast<br>IDR<br>0.4 HCLR<br>HCLR_<br>0.2<br>0.0<br>2016-10-01 2016-10-15 2016-11-01 2016-11-15 2016-12-01 2016-12-15 2017-01-01<br>Date (final 3 months of data)<br>Probability/Outcome<br><!-- End of picture text -->

Figure 12: Comparing three statistical postprocessing methods (IDR, HCLR, HCLR_) for 1-day ensemble weather forecasts on the Probability of Precipitation (PoP). The binary outcome is drawn as gray dots. _For visualization purposes, we plot the data and the forecasts only for the final 3 months (October 01, 2016 to January 01, 2017) and at one airport location (Brussels)._ 

#### **I.2.2 All Pairwise Comparisons of MLB Forecasters** 

Figure 11 includes all pairwise comparisons between the five MLB forecasters considered in our experiment. See main text from Section 5.2 for further details. 

### **I.3 Additional Details & Results from the Weather Experiment** 

The setup closely follows the comparison experiment by Henzi and Ziegel (2022), who compare statistical postprocessing methods for predicting the probability of precipitation (PoP) using the ensemble forecast data from the European Centre for Medium-Range Weather Forecasts (ECMWF; Molteni et al. (1996)). The dataset includes the observed 24-hour precipitation from January 06, 2007 to January 01, 2017 at four airport locations (Brussels, Frankfurt, London Heathrow, and Zurich), and for each location and date it also includes 1- to 5-day ensemble forecasts, consisting of a higher resolution forecast, 50 perturbed ensemble forecasts at a lower resolution, and a control run for the perturbed forecasts. They consider three statistical postprocessing methods in their experiments: isotonic distributional regression (IDR; Henzi et al. (2021)), heteroscedastic censored logistic regression (HCLR; Messner et al. (2014)), and a variant of HCLR without its scale parameter (HCLR_). Each method is applied to the first half of the data, separately for each airport location and lag _h_ = 1 _, . . . ,_ 5, and the second-half data is used to make sequential comparisons of the postprocessing methods. Note that each location has a different number of observations: 3,406 for Brussels, 3,617 for Frankfurt, 2,256 for London, and 3,241 for Frankfurt. See Section 5 in Henzi et al. (2021) and Section 5.1 in Henzi and Ziegel (2022) for further details about the dataset and the postprocessing methods. 

In Figure 12, we plot the three forecasters (1-day) on the PoP for the final year (2016-2017) in Brussels. 

### **I.4 Fine-Tuning the CS Width Using Simulated IID Mean Differentials** 

The uniform boundaries we use in our CSs come with hyperparameter(s) that one can choose to optimize the CS widths at specific intrinsic times (i.e., values that the non-decreasing sequence ( _V_<sup>ˆ</sup> _t_ )<sup>_∞_</sup> _t_ =1 can take). As explained in Section B, this choice can be thought of as an additional fine-tuning step and is secondary to choosing the type of uniform boundary. Nevertheless, since it is a hyperparameter, we seek to find a reasonable default that can be used for typical scenarios of forecast comparison 

59 



<!-- Start of picture text -->
Histogram of  i Cumulative Variance vs. Sample Size<br>0.05<br>80<br>0.04<br>60<br>0.03<br>40<br>0.02<br>20<br>0.01<br>0<br>0.00<br>0.0 0.2 0.4 0.6 0.8 1.0 0 2000 4000 6000 8000 10000<br>i Sample Size (t)<br>)Vt<br>Probability<br>Cumulative Variance (<br><!-- End of picture text -->

IID Figure 13: (Left) Histogram of _δ_<sup>ˆ</sup> _i ∼_ Beta(30 _,_ 10) _−_ Beta(10 _,_ 30) for _i_ = 1 _, . . . ,_ 10 _,_ 000. (Right) Plot of the cumulative variance (intrinsic time) _V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi−_ˆ∆</sup><sup>_i−_1)2,whereˆ∆</sup><sup>_i−_1=�</sup><sup>_i_</sup> _j_<sup>_−_</sup> =1<sup>1</sup><sup>_δ_ˆ</sup><sup>_j_.</sup> Note that the hyperparameter _v_ opt, which we discuss below, determines the intrinsic time _V_<sup>ˆ</sup> _t_ at which the uniform boundary is the tightest. 

without an a priori knowledge of how large the intrinsic time can get. 

To achieve this, we compare the widths of various CSs for the mean differential between two independent and identically distributed (IID) random variables. The main reason for using IID data is so that we can compare the width of our CSs with other CSs developed in previous work (Howard et al., 2021; Waudby-Smith and Ramdas, 2023; Waudby-Smith et al., 2021), including ones that only apply to IID means. 

To begin, we simulate score differences by sampling two IID Beta random variables and taking their differences: 



<u>30 10</u> Note that _−_ 1 _≤ δ_<sup>ˆ</sup> _i ≤_ 1 a.s. and that E[ _δ_<sup>ˆ</sup> _i_ ] = 30+10<sup>_−_</sup> 10+30<sup>=</sup><sup><u>1</u></sup> 2<sup>. Figure 13 illustrates the data sampled</sup> according to (118) (left) as well as the cumulative variance (intrinsic time) _V_<sup>ˆ</sup> _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>(ˆ</sup><sup>_δi −_ˆ∆</sup><sup>_i−_1)2,</sup> where ∆<sup>ˆ</sup> _i−_ 1 =<sup>�</sup><sup>_i_</sup> _j_<sup>_−_</sup> =1<sup>1</sup><sup>_δ_ˆ</sup><sup>_j_, over the sample size</sup><sup>_t_(right).</sup> 

Given the data, we now compare different configurations of the EB CS (Theorem 2) for the mean score differential. Using the EB CS with the conjugate-mixture uniform boundary (Section 4.3.4), we first show how we choose a default value for _v_ opt, the hyperparameter for the uniform boundary that specifies the intrinsic time at which the CS width is optimized (defined in Section B). Recall that, in our previous plot, we showed the values of intrinsic times across sample sizes for this data. In Figure 14 (left), we plot the widths of the 95% EB CS against different choices of _v_ opt. Comparing the values of _v_ opt _∈{_ 0 _._ 1 _,_ 1 _,_ 10 _,_ 100 _,_ 1000 _}_ , we find that the EB CS is generally the tightest across time for _v_ opt = 10 or _v_ opt = 100. Based on the result, we use a default value of _v_ opt = 10 for all our experiments involving the EB CS in the paper, unless specified otherwise. 

We now compare EB CSs constructed using different types of uniform boundaries, including the conjugate-mixture (“ConjMix”) boundary and the polynomial stitching boundary (Section B.2). In this comparison, we additionally include EB CSs constructed using the predictable-mixture (“PredMix”) boundary (Waudby-Smith and Ramdas, 2023), which is an efficient alternative that works specifically for bounded IID means. Finally, we include the asymptotic CSs that we described in 

60 



<!-- Start of picture text -->
CS Width vs. Sample Size, by vopt CS Width vs. Sample Size, by CS Type<br>0.14 v opt 0.14 CS Type<br>0.12 0.1 0.12 ConjMix-EB<br>1.0 Stitching-EB<br>0.10 0.10<br>10.0 PredMix-EB<br>0.08 100.0 0.08 Asymptotic<br>1000.0<br>0.06 0.06<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br>Sample Size (t) Sample Size (t)<br>CS Width CS Width<br><!-- End of picture text -->

Figure 14: _Left:_ Widths of conjugate-mixture EB CSs per sample sizes ( _t_ ), across different values of the hyperparameter _v_ opt (optimal intrinsic time). The choices _v_ opt = 10 and _v_ opt = 100 give the smallest widths overall, with the former being tighter early on and the latter later on. _Right:_ Widths of EB CSs using different uniform boundaries, including the conjugate-mixture (“ConjMix”) and predictable-mixture (“PredMix”) boundaries, and also the asymptotic CS. Overall, the asymptotic CS is the tightest, although the mixture EB CSs achieve similar widths for large sample sizes. The stitching EB CS is considerably wider than the mixture variants. 

#### Section C as a reference. 

In Figure 14 (right), we plot the widths of all CS variants at the coverage level of 95%, optimized for the intrinsic time _v_ opt = 10 when applicable. Generally speaking, we observe that the asymptotic CS achieves the tightest width, although the (non-asymptotic) EB CS variants using mixture boundaries approach that width for large sample sizes. This is consistent with our intuition, as the asymptotic CS is the large-sample “limit” of the EB CS in terms of width (Waudby-Smith et al., 2021). Among the EB CS variants, the conjugate-mixture variant is tighter towards the beginning ( _t <_ 10<sup>3</sup> ) while the predictable-mixture becomes slightly tighter afterwards; the stitching CS is not as tight as the other two. This is also as expected, as both mixture CSs are known to have similar widths (up to differences determined by hyperparameters) (Waudby-Smith and Ramdas, 2023), while the stitching CS tends to be looser in practice (Howard et al., 2021). We close with the note that any of these (EB or asymptotic) CSs are substantially tighter than Hoeffding-style CSs (Theorem 1) in most cases, regardless of the uniform boundary choice. This is evident from our earlier experiments in Section 5.1. 

61 


