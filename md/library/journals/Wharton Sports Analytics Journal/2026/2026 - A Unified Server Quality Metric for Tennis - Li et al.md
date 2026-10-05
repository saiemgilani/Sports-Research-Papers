<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - A Unified Server Quality Metric for Tennis - Li et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/a-unified-server-quality-metric-for-tennis/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Aiwen Li; Amrita Balajee; Harry Wieand; Jonathan Pipping-Gamon -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

A Unified Server Quality Metric for Tennis

Aiwen Li1, Amrita Balajee1, Harry Wieand2, and Jonathan Pipping-Gamo´n1

1University of Pennsylvania 2Boston University Academy

## Abstract

Traditional tennis rating systems (e.g., Elo) summarize overall player strength but do not isolate the independent value of serving. Using point-by-point data from Wimbledon and the U.S. Open, we develop serve-specific player metrics that separate serving quality from return ability and other latent factors. For each tournament and gender, we fit logistic mixed-effects models of point outcomes using serve speed, speed variability, and placement features, with crossed server and returner random intercepts to capture unobserved player strengths. From these models we derive Server Quality Scores (SQS): partially pooled, opponent-adjusted estimates of players’ serving impact. In out-of-sample evaluation, SQS aligns more strongly with serve efficiency—the probability of winning points within three shots—than weighted Elo. We further benchmark SQS against task-aligned serve-stat baselines and model ablations, quantifying the incremental value of serve features and partial pooling. Associations with overall serve win percentage are smaller and dataset-dependent, and neither SQS nor weighted Elo consistently dominates that outcome. Overall, SQS is best interpreted as a measure of serve-induced short-point advantage (serve quality plus early-point conversion), complementing holistic ratings with actionable insight for coaching, forecasting, and player evaluation.

## 1 Introduction

Current tennis rating systems, such as Elo, estimate player strength from match-level outcomes. While effective for forecasting, these models compress the complexity of play into a single number and do not isolate the value of specific skills. In particular, the serve—the only shot completely under a player’s control—is treated implicitly rather than modeled directly. In practice, practitioners often summarize serving performance with simple statistics such as ace rate, first-serve-in percentage, and first-serve-win percentage. These summaries are easy to compute, but each reflects only a narrow slice of serve quality and can mask the mechanisms that make a serve effective. Moreover, they conflate distinct dimensions of serving (pace, placement, and variability) and are sensitive to opponent quality and point context. Taken together, these limitations motivate a holistic, point-level measure of serving performance independent of other skills.

Our Contribution: This paper establishes a framework to estimate a serve-specific player metric using generalized linear mixed models (GLMMs). We call this metric a player’s Server Quality Score (SQS). SQS captures both measured skill derived from serve features (average speed, speed variability, and location characteristics) and unmeasured server effects modeled through player-specific random intercepts. To distinguish between aggressive and defensive serving contexts, we fit separate models for first and second serves. We treat SQS as a two-dimensional metric, reporting separate first-serve and second-serve scores.

Using point-by-point data from Wimbledon and the U.S. Open (2018–2019 and 2021–2024), we benchmark these server metrics against weighted Elo (wElo). We also compare against task-aligned baselines (standard serve statistics, random-effects-only GLMM scores, and fixed-effects-only scores) to test whether SQS adds information beyond simpler serve summaries and model ablations.

Organization: Section 2 reviews related work. Section 3 describes our methodology with data preparation, mixed effects models, and construction of SQS. Section 4 discusses out-ofsample testing results and benchmarks SQS against wElo. Additional task-aligned baseline analyses, temporal validation, and point-level robustness checks are reported in the appendix. We conclude with a discussion in Section 5.

## 2 Related Work

## 2.1 Match-Level Ratings and Forecasting

Elo-style ratings, adapted from chess and widely used in tennis, estimate a player’s strength from match results. These ratings have consistently been effective for forecasting match winners using large datasets (Klaassen and Magnus (2003); Kovalchik (2016)). A recent extension, weighted Elo (wElo), incorporates margins of victory and has been shown to outperform standard Elo and other common baselines, including in value-betting applications (Angelini et al. (2022)).

Beyond pre-match ratings, other studies combine in-play information to improve point-bypoint forecasting. For example, Kovalchik and Reid (2019) show that starting from a ratingbased prior and updating dynamically during a match improves win probability estimates.

Alternative approaches model tennis as a hierarchical Markov process, where point-level win probabilities map recursively to game, set, and match win probabilities. Early work studied whether points are independent and identically distributed (IID), finding that this assumption is not always true due to changes in momentum and pressure (Klaassen and Magnus (2001)).

Despite these limitations, models under the IID assumption still provide a useful baseline. O’Malley (2008) derives exact game, set, and match win probabilities under an IID assumption and studies how these probabilities change with serve and return strength. Later studies relax the IID assumption by using state-dependent dynamics that better predict live win probabilities (Klaassen and Magnus (2003); Newton and Aslam (2009)).

While these ratings and match models are valuable for forecasting, they intentionally aggregate performance across all phases of play. This motivates serve-specific modeling that can complement Elo-style summaries when the goal is interpretation and skill isolation rather than match prediction.

## 2.2 Point-Level Models and Serve Win Probabilities

A central part of point-based tennis models is a player’s “serve win probability”, defined as the probability of winning a point as the server. These probabilities are often split between first and second serves, and they can be adjusted based on surface or match context.

Early work by Barnett and Clarke (2005) computes match-specific serve probabilities by combining each player’s historical serve and return performance with opponent strength. Subsequent work refines this approach by adding surface adjustments, shrinkage for small samples, and common-opponent comparisons. More recently, Gollub (2021) improves estimates of serve win probabilities by combining broader Elo-type player ratings.

However, serve win probabilities in point-based models are typically treated as contextdependent inputs for predicting match outcomes rather than as standalone measures of serving quality. Our goal is instead to estimate an interpretable server metric derived from serve characteristics while accounting for unobserved, player-specific effects via partial pooling.

## 2.3 Gap: Isolating Serve Quality

Despite frequent use of serving variables in both match- and point-level models, there is still no widely adopted metric that isolates the serve as an independent component of player quality. In practice, separating the serve’s contribution from other aspects of play improves interpretability and supports decision-making. It clarifies how much advantage comes from the serve itself and informs coaching strategies that are specific to serving and returning.

Motivated by this gap, we introduce a framework for serve-specific player metrics focused solely on serving performance. Section 3 describes the methodology used to construct these metrics.

## 3 Methodology

## 3.1 Data and Feature Construction

We use publicly available point-by-point data for singles matches at the Wimbledon and U.S. Open tournaments from Jeff Sackmann’s public tennis database. We pool six seasons of data (2018–2019 and 2021–2024) into four groups: Wimbledon men’s singles, Wimbledon women’s singles, U.S. Open men’s singles, and U.S. Open women’s singles (excluding 2020 due to COVID-19–related disruptions). All analyses are performed separately for each tournament and gender.

Within each dataset, matches are randomly split into training (80%) and testing (20%) sets within each year. This ensures that all points from a given match are assigned to the same split and that each season contributes to both training and testing, avoiding leakage from within-match dependence while balancing year-to-year variation. Server Quality Scores (SQS) are constructed using the training set, and the testing set is reserved for out-of-sample evaluation. As a complementary check, we also evaluate SQS under a temporal split (train on 2018–2022, test on 2023–2024); these results appear in Appendix C.

We begin by cleaning the raw point-level data, applying the following steps:

• Removing serves with missing location information.

• Restricting the data to valid first and second serves.

• Excluding serves recorded with zero speed (due to faults).

• Defining serve location using two categorical variables, ServeWidth and ServeDepth, and assigning each serve to a discrete width–depth location bin. location bin = (ServeWidth, ServeDepth).

For each server j and serve type s ∈ {1, 2} (first or second), we summarize serve behavior using a set of interpretable features:

• nj(s): number of serves observed of type s. • avg speedj(s): average serve speed (mph), • sd speed(js): standard deviation of serve speed (a proxy for variability/unpredictability), • modal locj(s): the modal location bin (one-hot encoded in the model), • loc entropyj(s): location entropy (a proxy for location unpredictability), defined as loc entropyj(s) = − p(bs,j) log2 p(bs,j), b where pb(s,j) is the proportion of serves by player j (of type s) that land in location bin b. These features were chosen to balance interpretability and signal. Average serve speed summarizes pace, sd speed captures pace unpredictability, modal loc captures directional tendencies, and location entropy captures how dispersed a player’s placement is across coarse bins. To ensure that our estimates are reliable, we only keep servers with more than 20 serves of a given type. Any continuous features are standardized within the dataset (denoted by the superscript z), and serve locations are encoded categorically.

Because these predictors summarize serve behavior at the player level, they compress withinplayer variation across individual points. As a robustness check, we implement alternative models using point-level serve features (serve speed, location bin, and an indicator for whether the serve matches the player’s modal location) and report the results in Appendix D. The alternative results are broadly consistent with the main specification, suggesting that the aggregated server-level model retains most of the predictive signal relevant to serve efficiency while remaining easier to interpret as a stable player-level serve profile.

Finally, we consider two complementary outcomes: overall point win percentage and serve efficiency. We define an efficient serve as one where the server wins the point within the first three shots (serve, return, and the server’s next shot). This restriction is deliberate: by focusing on the earliest phase of the point—when the server’s initial delivery most directly shapes the exchange—serve efficiency acts as a measure of serve-induced short-point advantage rather than overall point wins, which increasingly reflect baseline rally skill and endurance as the point lengthens. In this sense, serve efficiency captures situations in which the serve generates an immediate advantage (e.g., an ace, forced error, weak return, or shortball put-away) that the server converts quickly, rather than points in which the serve merely initiates a neutral rally.

In our analysis, we model the point-level efficient-serve indicator (a 0/1 variable under the three-shot definition above) as the outcome in Section 3.2. These scores are then evaluated using aggregated server-level serve efficiency and win percentage from our testing dataset in Section 3.3.

## 3.2 Mixed-Effects Model and Server Quality Score (SQS)

Our goal is to quantify server quality in a way that reflects both observable serve characteristics and unobservable player effects. To do so, we fit separate logistic mixed-effects models for first and second serves to account for different serving contexts. This separation allows the relationship between serve features and short-point outcomes to differ across serve types.

Each model is fit at the point level, with the outcome being whether the serve was efficient, i.e., whether the server won the point within three total shots (as defined in Section 3.1).

For serve type s ∈ {1, 2}, let Yi(,js) be the binary indicator that server j wins point i within three shots. We model this using a logistic mixed-effects framework: logit Pr(Yi(,js) = 1) = β0(s) + β1(s) avg speedj(s,z) + β2(s) sd speedj(s,z) + (β3(s))⊤ I(modal loc(js)) + β4(s) loc entropy(js,z) + u(js) + vk(s) where u(js) ∼ N (0, σs2) is a server-level random intercept and vk(s) ∼ N (0, τs2) is a returnerlevel random intercept (for returner k). The superscript z on speed and entropy features indicates standardization (z-scoring) within the dataset.

The fixed effects quantify the association between observable serve characteristics (pace, pace variability, and placement tendencies) and short-point success. The returner-specific random intercept vk(s) adjusts for opponent return strength. Without this term, servers who disproportionately face weaker returners (e.g., due to draw effects) can appear artificially strong. By including crossed random intercepts for server and returner, the estimated server effect uj(s) is identified net of the average return quality faced, yielding an opponent-adjusted measure of serving impact.

For each serve type, we summarize the fitted model into a single server quality score by combining each player’s estimated fixed and random effects:

SQSj(s) := βˆ0(s) + βˆ1(s) avg speedj(s,z) + βˆ2(s) sd speed(js,z) + (βˆ3(s))⊤ I(modal loc(js)) + βˆ4(s) loc entropyj(s,z) + uˆ(js).

We report (SQS(j1), SQSj(2)) as a two-dimensional serving profile. The first-serve score SQSj(1) summarizes how much advantage a player’s first delivery tends to create in the three-shot sequence, reflecting the payoff of pace, placement, and disguise in more aggressive serving contexts. The second-serve score SQSj(2) summarizes effectiveness under the more conservative second-serve regime, where the objective shifts toward limiting opponent aggression and securing a playable first-strike opportunity.

Because the fitted model includes both server and returner effects, we define SQS as the server-side linear predictor evaluated at an average returner (i.e., setting vk(s) = 0). Equivalently, SQS summarizes the predicted short-point advantage attributable to the server after adjusting for returner strength. We keep SQS on the log-odds scale of the fitted models, since this is the natural additive scale on which fixed effects and random effects combine. On this scale, differences in SQS correspond to multiplicative changes in the odds of winning the point, so higher values indicate serves that substantially increase the likelihood of winning the rally (e.g., a 0.10 increase in SQS corresponds to an odds ratio of exp(0.10) ≈ 1.11).

## 3.3 Out-of-Sample Evaluation and Baselines

We evaluate Server Quality Scores (SQS) out of sample using the held-out matches in each tournament–gender dataset. Since SQS is defined at the server-by-serve-type level, we aggregate test-set points by server and compute two server-level outcomes: overall point win percentage and serve efficiency (defined in Section 3.1). Serve efficiency captures short-point success within three shots, while win percentage summarizes outcomes over all rally lengths:

#{serve points won with RallyCount ≤ 3}

ServeEffj =

, #{serve points}

#{serve points won} WinPctj = #{serve points}

For each serve type s ∈ {1, 2} and each outcome, we model the number of successes for server j as binomial with denominator equal to the number of test-set serves of type s. We then fit binomial GLMs with grouped outcomes on the corresponding serve-type score, using SQSj(1) for first serves and SQS(j2) for second serves. These regressions quantify how SQS relates to short-point success (serve efficiency) versus overall point success (win percentage) in unseen matches.

As a baseline, we repeat the same evaluation using weighted Elo (wElo) in place of SQS. wElo scores are computed using the R package welo (Angelini et al., 2022), providing a match-level benchmark against which to assess the incremental information in serve-specific scores.

To address task alignment directly, we also evaluate three additional baseline families: (i) standard serve statistics (ace rate, first-serve points won, unreturned-serve proxy rate, and first-serve-in%), (ii) a random-effects-only GLMM with server and returner intercepts but no serve covariates, and (iii) a fixed-effects-only score that uses the measured serve-feature component of SQS without the server random effect.

For comparability, each tournament–gender–serve-type evaluation uses a common completecase server set across all predictors. Full baseline comparisons are reported in Appendix B.

In Section 4, we report regression coefficients and correlations between each predictor and the observed test-set outcomes.

## 4 Results

We report full out-of-sample results for Wimbledon men’s singles in Tables 1 and 2. Analogous tables for Wimbledon women’s singles and the U.S. Open (men and women) appear in Appendix A; we reference them here only to summarize cross-dataset patterns.

Expanded task-aligned baseline comparisons appear in Appendix B. In addition, results from the alternative point-level specification are reported in Appendix D. These results show similar qualitative patterns, indicating that the server-level specification used in the main analysis captures most of the predictive signal while remaining easier to interpret as a stable player-level serve profile.

Table 1: Out-of-sample performance for Wimbledon men’s singles (first serves).

Outcome

Predictor n

Coefficient p-value

Correlation (r)

Serve efficiency

SQS1

Serve efficiency wElo

Win percentage

SQS1

Win percentage wElo

0.240 0.015 0.109 0.030

4.6 × 10−22 0.563

1.5 × 10−5 0.256

0.667 0.148 0.325 0.136

Table 2: Out-of-sample performance for Wimbledon men’s singles (second serves).

Outcome

Predictor n

Coefficient p-value

Correlation (r)

Serve efficiency

SQS2

Serve efficiency wElo

Win percentage

SQS2

Win percentage wElo

0.127 0.017 -0.064 0.014

0.00072 0.663 0.064 0.692

0.232 0.090 -0.251 0.056

4.1 Serve Efficiency vs. Point Win Percentage

Across tournaments and genders, SQS aligns most closely with serve efficiency, our serveproximal target. On first serves, SQS is positively associated with serve efficiency in all four datasets and is especially strong at Wimbledon (e.g., r = 0.667 for Wimbledon men and r = 0.564 for Wimbledon women), with more modest associations at the U.S. Open (r ≈ 0.28 for men and r ≈ 0.24 for women). The larger Wimbledon associations are consistent with surface effects: grass-court match-play features shorter rallies and a more pronounced serve/return advantage, so a three-shot outcome concentrates more of the point’s signal in the opening exchange (Fitzpatrick et al., 2019). On second serves, SQS–serve efficiency associations are smaller and less stable, but remain positive in three of four datasets (including Wimbledon men: r = 0.232), with U.S. Open men as an exception (r ≈ −0.08). In contrast, wElo exhibits weak or negative correlations with serve efficiency across datasets, consistent with a match-level rating that is not designed to isolate serve-driven short-point advantage.

Against the additional task-aligned baselines (Appendix B), SQS remains strongest on average for first-serve efficiency (r¯ = 0.439), ahead of fixed-effects-only (0.423), ace rate (0.406), and random-effects-only (0.388), while wElo is weak on this serve-proximal target (r¯ = −0.067). At the dataset level, SQS is the top first-serve efficiency predictor in three of four splits.

The ablation comparisons support incremental value from both model components. Relative to the random-effects-only model, SQS improves first-serve efficiency correlations in all four datasets, indicating added signal from serve-feature covariates. Relative to fixed-effects-only, SQS is higher in three of four datasets, suggesting that partial pooling via server random effects contributes in most settings.

Associations with overall point win percentage are generally weaker and more variable for both ratings. On first serves, SQS correlations remain positive across datasets, while wElo is small and sometimes negative. On second serves, both predictors show mixed performance, suggesting that overall point outcomes under second-serve conditions depend strongly on broader skills and contextual factors beyond the serve alone. Task-aligned baseline comparisons for win percentage (Appendix B) reinforce this pattern. On first serves, mean correlations are similar across several predictors (SQS: r¯ = 0.259, fixed-effects-only: 0.261, ace rate: 0.240), so no single metric clearly dominates. On second serves, SQS is weaker on average (r¯ = −0.068), while wElo is relatively stronger (r¯ = 0.111), consistent with win percentage reflecting broader point-winning skill beyond serve-proximal effects. This outcome-specific separation is consistent with SQS isolating serve-proximal impact: it aligns most closely with a target designed to concentrate signal in the earliest shots, and less closely with outcomes increasingly driven by longer-rally dynamics. Player ranking tables for first and second serves are provided in Appendix E.

4.2 First vs. Second Serves

Stratifying by serve type clarifies how serving context mediates the relationship between ratings and outcomes. On first serves, servers have the greatest opportunity to create immediate leverage; correspondingly, SQS shows its strongest and most reliable associations with the serve-efficiency target. On second serves, where pace is reduced and the returner typically sees more playable deliveries, efficiency and win-percentage outcomes depend more heavily on the ensuing exchange, making relationships with any serve-only summary less stable across datasets.

## 4.3 Implications

Overall, the out-of-sample results support interpreting SQS as a serve-focused metric. Across datasets, SQS is most informative for explaining variation in serve efficiency—an outcome designed to concentrate signal in the serve–return–first-strike phase—whereas associations with overall point win percentage are weaker and more heterogeneous, especially on second serves where immediate serve leverage is reduced. Although serve efficiency still reflects the return and the server’s next shot, restricting attention to a three-shot window reduces the influence of longer-rally dynamics. This provides empirical evidence that SQS captures a distinct, serve-proximal component of performance.

## 5 Discussion

## 5.1 Comparison with Prior Work

These results are consistent with prior tennis-rating research showing that match-level metrics such as Elo-type ratings are effective summaries of overall performance, while extending that literature by isolating a serve-proximal component. Relative to prior work on serve win probabilities as inputs to match forecasting, SQS is designed as an interpretable player metric rather than a match predictor. The direct comparison with weighted Elo and the additional win-percentage analyses show this distinction empirically: SQS is strongest for short-point serve efficiency, whereas weighted Elo is often more aligned with broader point outcomes, especially on second serves.

## 5.2 Conclusions and Practical Applications

This paper proposes a serve-specific framework for evaluating tennis performance using pointlevel data. We introduce a Server Quality Score (SQS), estimated via logistic mixed-effects models, that summarizes how effectively a player’s serve converts the opening exchange into an early-point advantage.

Across tournaments and genders, out-of-sample evaluation supports the intended interpretation of SQS as a serve-proximal metric. SQS aligns most strongly with serve efficiency, while relationships with overall point win percentage are smaller and more heterogeneous: especially on second serves where immediate serve leverage is reduced. Weighted Elo (wElo), by contrast, reflects broader point-winning ability and in some settings aligns more closely with win percentage; however, neither rating uniformly dominates for win percentage across all datasets. Taken together, these results provide empirical evidence that SQS captures a distinct, serve-driven component of performance that complements holistic match-level ratings.

## 5.3 Limitations and Future Work

Several limitations suggest directions for extending the SQS framework. We adjust for average return strength via a returner random intercept, but we do not model server–returner interaction effects (matchup-specific styles) or contextual shifts in return positioning. First, the model omits contextual factors such as score state, point importance, and fatigue. Because serve selection and execution change under pressure, incorporating context could help distinguish underlying serve quality from strategic adaptation within matches.

Second, our placement features (modal location and location entropy) provide interpretable summaries but compress richer spatial structure. Future work could incorporate continuous serve coordinates, spatial smoothing, or probabilistic location models to better represent placement strategies and their interaction with pace.

Third, data quality limits the characterization of risk. In particular, serves with recorded speed of zero (typically faults or missing tracking) were excluded, potentially omitting information about second-serve safety and risk–reward tradeoffs. More complete tracking of serve attempts and faults would enable models that jointly capture placement, speed, and error propensity.

Finally, our analysis is conducted separately by tournament and gender, which means the resulting SQS values are not directly comparable across tournaments or surfaces. For example, faster courts such as grass typically amplify serve advantage relative to slower hard or clay courts. In this study, we partially address this concern by estimating separate models for each tournament. The top-ranked servers in Appendix E are broadly consistent across the Wimbledon and U.S. Open datasets, suggesting that the metric captures stable aspects of serving ability despite surface differences. An extension to this would be to estimate a hierarchical model that pools information across tournaments and seasons while allowing surface-specific effects. This would enable direct comparisons of serving quality across surfaces and competitions.

Together, these extensions provide a path toward richer serve-specific metrics through contextual modeling and improved spatial representation, while preserving the interpretability and portability of SQS.

## 6 Reproducibility

All code is available on the project’s GitHub repository.

## 7 Acknowledgments

The authors thank Professor Abraham J. Wyner and Tianshu Feng for helpful feedback, Audrey Kuan for her contributions during the summer, and the Wharton Sports Analytics and Business Initiative (WSABI) for supporting this research.

## References

Angelini, G., Candila, V., and De Angelis, L. (2022). Weighted elo rating for tennis match predictions. European Journal of Operational Research, 297(1):120–132.

Barnett, T. and Clarke, S. R. (2005). Combining player statistics to predict outcomes of tennis matches. IMA Journal of Management Mathematics, 16(2):113–120.

Fitzpatrick, A., Stone, J. A., Choppin, S., and Kelley, J. (2019). Important performance characteristics in elite clay and grass court tennis match-play. International Journal of Performance Analysis in Sport, 19(6):942–952.

Gollub, J. (2021). Forecasting serve performance in professional tennis matches. Journal of Sports Analytics, 7(4):223–233.

Klaassen, F. J. and Magnus, J. R. (2001). Are points in tennis independent and identically distributed? evidence from a dynamic binary panel data model. Journal of the American Statistical Association, 96(454):500–509.

Klaassen, F. J. and Magnus, J. R. (2003). Forecasting the winner of a tennis match. European Journal of Operational Research, 148(2):257–267.

Kovalchik, S. and Reid, M. (2019). A calibration method with dynamic updates for withinmatch forecasting of wins in tennis. International Journal of Forecasting, 35(2):756–766.

Kovalchik, S. A. (2016). Searching for the GOAT of tennis win prediction. Journal of Quantitative Analysis in Sports, 12(3).

Newton, P. K. and Aslam, K. (2009). Monte carlo tennis: A stochastic markov chain model. Journal of Quantitative Analysis in Sports, 5(3).

O’Malley, A. J. (2008). Probability formulas and statistical analysis in tennis. Journal of Quantitative Analysis in Sports, 4(2).

## Appendix

A Additional Out-of-Sample Results

Table 3: Out-of-sample performance across datasets (first serves).

Dataset

Outcome

Predictor n Coefficient p-value Correlation (r)

Wimbledon women Serve efficiency

SQS1

0.301

1.1 × 10−22

Wimbledon women Serve efficiency wElo 65 −0.020

0.511

Wimbledon women Win percentage SQS1 65

0.134

8.1 × 10−6

Wimbledon women Win percentage wElo 65 −0.015

0.625

0.564 −0.102 0.447 −0.123

U.S. Open men U.S. Open men U.S. Open men U.S. Open men

Serve efficiency Serve efficiency

SQS1 wElo

0.098

86 −0.074

8.9 × 10−6 3.5 × 10−4

Win percentage

SQS1

0.061

0.0064

Win percentage wElo 86

0.044

0.038

0.283 −0.245 0.164 0.011

U.S. Open women Serve efficiency

SQS1

U.S. Open women Serve efficiency wElo 92

U.S. Open women Win percentage SQS1 92 U.S. Open women Win percentage wElo 92

0.123 0.004 0.046 0.036

2.4 × 10−6 0.866 0.071 0.154

0.243 −0.070 0.099 0.032

Table 4: Out-of-sample performance across datasets (second serves).

Dataset

Outcome

Predictor n Coefficient p-value Correlation (r)

Wimbledon women Serve efficiency

SQS2

Wimbledon women Serve efficiency wElo

Wimbledon women Win percentage

SQS2

Wimbledon women Win percentage wElo

0.129 0.033 0.048 0.100

0.0061 0.531 0.254 0.034

0.331 0.121 0.215 0.287

U.S. Open men U.S. Open men U.S. Open men U.S. Open men

Serve efficiency Serve efficiency

SQS2 wElo

0.009

0.782

−0.154

3.9 × 10−7

Win percentage

SQS2

−0.036

Win percentage wElo

0.070

0.196 0.0091

−0.081 −0.321 −0.139 0.168

U.S. Open women Serve efficiency

SQS2

0.092

U.S. Open women Serve efficiency wElo

63 −0.121

U.S. Open women Win percentage

SQS2

−0.004

U.S. Open women Win percentage wElo

63 −0.022

0.021 0.0050 0.921 0.574

0.181 −0.279 −0.096 −0.067

B Task-Aligned Baseline Comparisons

To supplement the main SQS–wElo comparison, this appendix reports task-aligned baselines requested in review: standard serve statistics, a random-effects-only GLMM score (server/returner intercepts only), and a fixed-effects-only score (measured serve-feature component without server random effects). All values below use the within-year random split and the common complete-case server set per dataset and serve type.

Table 5: Serve-efficiency correlations by predictor, averaged across datasets (random split).

Predictor

SQS FE-only score Ace rate RE-only GLMM Unreturned rate First-serve points won First-serve-in % wElo

First-serve mean r

0.439 0.423 0.406 0.388 0.318 0.245 −0.030 −0.067

Second-serve mean r

0.165 0.129 0.107 0.143 0.047 0.066 −0.012 −0.097

Table 6: First-serve efficiency correlations by dataset for key baseline families (random split).

Dataset

Wimbledon men Wimbledon women U.S. Open men U.S. Open women

SQS

0.667 0.564 0.283 0.243

Best serve stat

0.662 (ace rate) 0.463 (ace rate) 0.262 (ace rate) 0.237 (ace rate)

RE-only GLMM

0.639 0.549 0.261 0.102

FE-only score

0.635 0.502 0.263 0.292 wElo

0.148 −0.102 −0.245 −0.070

Table 7: Win-percentage correlations by predictor, averaged across datasets (random split).

Predictor

FE-only score SQS Ace rate First-serve points won RE-only GLMM Unreturned rate First-serve-in % wElo

First-serve mean r

0.261 0.259 0.240 0.231 0.223 0.103 0.050 0.014

Second-serve mean r

−0.059 −0.068 −0.015 −0.020 −0.088 −0.152 0.061 0.111

The task-aligned baseline results are broadly consistent with the main analysis. For the serve-proximal target (serve efficiency), SQS is strongest on average for first serves and is top in three of four dataset splits, indicating that it captures short-point serve impact better than match-level wElo and most serve-stat baselines. The ablation rows also support incremental value from both components of SQS: compared with random-effects-only, adding serve-feature covariates improves alignment in all first-serve datasets; compared with fixed-effects-only, adding partial pooling improves alignment in most settings. For overall

Table 8: Second-serve win-percentage correlations by dataset for key baseline families (random split).

Dataset

Wimbledon men Wimbledon women U.S. Open men U.S. Open women

SQS

−0.251 0.215 −0.139 −0.096

Best serve stat

0.050 (1st-srv pts won) 0.158 (1st-srv pts won)

−0.011 (ace rate) 0.254 (first-serve-in %)

RE-only GLMM

−0.174 0.000 −0.052 −0.127

FE-only score

−0.262 0.215 −0.203 0.015 wElo

0.056 0.287 0.168 −0.067 win percentage, predictor performance is flatter and more heterogeneous—especially on second serves, where wElo is often relatively stronger—consistent with this outcome reflecting broader point-construction skill beyond serve-proximal effects.

C Temporal Validation

The results in Section 4 and Appendix A use an 80/20 random split within each year. To assess whether SQS generalizes across time, we conduct an additional out-of-time validation: models are trained on 2018–2019 and 2021–2022 data and evaluated on held-out 2023–2024 data, with no temporal overlap between training and testing. This design tests whether serve profiles estimated from earlier seasons remain predictive of future performance.

Table 9: Temporal validation: serve efficiency (train 2018–2022, test 2023–2024).

Dataset

Predictor n

Coefficient p-value

Correlation (r)

First serve

Wimbledon men Wimbledon men Wimbledon women Wimbledon women U.S. Open men U.S. Open men U.S. Open women U.S. Open women

SQS1 wElo SQS1 wElo SQS1 wElo SQS1 wElo

0.184

5.3 × 10−15

0.015

0.512

0.151

7.6 × 10−9

0.063

0.009

0.088

1.1 × 10−5

0.052

2.6 × 10−4

0.224

6.3 × 10−22

0.150

1.9 × 10−19

0.649 0.010 0.365 0.087 0.297 0.247 0.578 0.459

Second serve

Wimbledon men Wimbledon men Wimbledon women Wimbledon women U.S. Open men U.S. Open men U.S. Open women U.S. Open women

SQS2 wElo SQS2 wElo SQS2 wElo SQS2 wElo

0.112

0.023

0.087

0.058

−0.007

−0.016

0.055

0.042

0.005 0.485 0.027 0.160 0.783 0.442 0.076 0.115

0.535 0.024 0.347 0.312 −0.158 −0.073 0.114 0.145

The temporal results are broadly consistent with the within-year random split. On first serves, SQS maintains stronger correlations with serve efficiency than wElo across all four datasets (Wimbledon men: r = 0.649 vs. 0.010; Wimbledon women: r = 0.365 vs. 0.087; U.S. Open men: r = 0.297 vs. 0.247; U.S. Open women: r = 0.578 vs. 0.459). On second serves, SQS–efficiency associations are positive in three of four datasets, mirroring the pattern observed under random splitting. Win percentage associations are weaker and more variable under the temporal split as well, consistent with the main analysis: SQS is most informative for the serve-proximal outcome, while overall point wins depend increasingly on non-serve factors. These findings indicate that the serve profiles captured by SQS are stable across seasons and not merely artifacts of within-year overfitting.

Table 10: Temporal validation: win percentage (train 2018–2022, test 2023–2024).

Dataset

Predictor n

Coefficient p-value

Correlation (r)

First serve

Wimbledon men Wimbledon men Wimbledon women Wimbledon women U.S. Open men U.S. Open men U.S. Open women U.S. Open women

SQS1 wElo SQS1 wElo SQS1 wElo SQS1 wElo

0.120

5.6 × 10−7

0.063

0.006

0.085

0.001

0.075

0.002

0.052

0.011

0.102

5.1 × 10−12

0.133

2.7 × 10−9

0.140

6.0 × 10−17

0.548 0.229 0.218 0.194 0.263 0.534 0.387 0.528

Second serve

Wimbledon men Wimbledon men Wimbledon women Wimbledon women U.S. Open men U.S. Open men U.S. Open women U.S. Open women

SQS2 wElo SQS2 wElo SQS2 wElo SQS2 wElo

0.020

0.586

0.071

0.018

−0.017

0.635

0.107

0.005

−0.095

5.9 × 10−5

0.095

1.2 × 10−7

−0.004

0.873

0.091

1.3 × 10−4

0.257 0.170 0.089 0.525 −0.358 0.384 0.000 0.365

D Point-Level Feature Robustness Check

The main model in Section 3 constructs SQS using server-level summaries of serve behavior, such as average speed, speed variability, modal location, and location entropy. While this choice yields interpretable player-level profiles, it compresses within-player variation across points. To assess whether the main results depend on this aggregation, we estimate an alternative set of GLMMs using point-level serve features directly. For each serve type, the alternative model includes point-level serve speed, point-level serve location bin, and an indicator for whether the observed serve location matches the player’s modal location for that serve type. As in the main model, we include crossed random intercepts for the server and returner. For the point-level mixed-effects model, let Yi,j denote the binary indicator that server j wins point i within three shots. We then model: logit Pr (Yi,j = 1) = β0(p) + β1(p)speedi(,zj) + (β2(p))⊤I(loci,j) + β3(p)I(modal matchi,j) + u(jp) + vk(p).

Here, speed(i,zj) is the standardized serve speed on point i, I(loci,j) is a one-hot encoding of the serve’s location bin, and I(modal matchi,j) indicates whether the observed location matches server j’s modal location for that serve type. The terms u(jp) and vk(p) are serverand returner-specific random intercepts, respectively. We split the data between first and second serves for these mixed-effects models. From the fitted models, we then construct a point-level version of SQS, denoted SQS(sp) for serve type s ∈ {1, 2}. These scores are calculated by combining each player’s estimated fixed and random effects for each serve type. We evaluate SQSs(p) out of sample using the same testing framework as in the main analysis (with an 80/20 random split within each year).

SQSj(p) = βˆ0(p) + βˆ1(p)speed(jz) + (βˆ2(p))⊤I(locj) + βˆ3(p)I(modal matchj) + uˆj(p).

The bars above the covariates indicate that we use the average point-level data across all serves of type s for server j in the training data. Thus, the point-level model is first estimated using individual serve observations, but the resulting SQS is evaluated at the average serve characteristics of each player. This differs from the main specification, where the regressors themselves are constructed directly as server-level summaries (e.g., average speed and location entropy). Tables 11 and 12 report out-of-sample results for serve efficiency and win percentage, respectively, alongside weighted Elo (wElo) as a benchmark. These results allow us to compare the predictive performance of the point-level specification with that of the main server-level model.

Table 11: Point-level feature robustness check: serve efficiency.

Dataset

Predictor n

RMSE p-value

Correlation (r)

First serve

Wimbledon men Wimbledon men

Wimbledon women Wimbledon women

U.S. Open men U.S. Open men

U.S. Open women U.S. Open women

SQS1(p) wElo

SQS(1p) wElo

SQS(1p) wElo

SQS1(p) wElo

0.805

2.39 × 10−9

1.295

0.251

0.865

3.59 × 10−8

1.473

0.418

1.199

1.569

0.011 0.023

1.249

1.455

0.043 0.506

0.671 0.148

0.620 −0.102

0.273 −0.245

0.212 −0.070

Second serve

Wimbledon men Wimbledon men

Wimbledon women Wimbledon women

U.S. Open men U.S. Open men

U.S. Open women U.S. Open women

SQS2(p) wElo

SQS2(p) wElo

SQS(2p) wElo

SQS2(p) wElo

1.216

1.338

1.118

1.311

1.425

1.615

1.274

1.587

0.056 0.495

0.015 0.429

0.803 0.003

0.170 0.027

0.248 0.090

0.360 0.121

−0.028 −0.321

0.175 −0.279

Table 12: Point-level feature robustness check: win percentage.

Dataset

Predictor n

RMSE p-value

Correlation (r)

First serve

Wimbledon men Wimbledon men

Wimbledon women Wimbledon women

U.S. Open men U.S. Open men

U.S. Open women U.S. Open women

SQS1(p) wElo

SQS1(p) wElo

SQS(1p) wElo

SQS1(p) wElo

1.151

1.304

0.010 0.293

1.010

4.70 × 10−5

1.487

0.331

1.302

1.398

0.191 0.918

1.315

1.384

0.232 0.763

0.327 0.136

0.482 −0.123

0.142 0.011

0.126 0.032

Second serve

Wimbledon men Wimbledon men

Wimbledon women Wimbledon women

U.S. Open men U.S. Open men

U.S. Open women U.S. Open women

SQS(2p) wElo

SQS(2p) wElo

SQS2(p) wElo

SQS(2p) wElo

1.573

1.363

1.296

1.180

1.456

1.282

1.453

1.450

0.047 0.673

0.353 0.056

0.516 0.132

0.574 0.599

−0.258 0.056

0.142 0.287

−0.073 0.168

−0.072 −0.067

Relative to the main model, the point-level feature model produces a similar overall pattern: SQS(p) remains more informative for the serve-proximal outcome than for overall win percentage. For first serves, point-level SQS(1p) continues to outperform wElo in predicting serve efficiency across all four datasets with notably stronger correlations. On second serves, the evidence is more mixed but still generally favors SQS(p) for serve efficiency in three of the four datasets, while U.S. Open men remains weak for both metrics. For win percentage, the results are again weaker and less consistent, which matches the main analysis in Section 4 and Appendix C. In particular, the point-level specification does not significantly strengthen the association between SQS(p) and overall point outcomes. Taken together, these results suggest that incorporating point-level serve speed and location does not overturn the main conclusions of the paper. The aggregated server-level model from Section 3.2 seems to retain most of the predictive signal relevant to serve efficiency, while remaining easier to interpret as a stable player-level serve profile.

E Top Server Rankings by Tournament

These tables report top-10 server rankings by SQS within each tournament and serve type. Values are centered by subtracting the tournament–serve-type mean SQS (log-odds). Positive values indicate above-average serving performance within the tournament and serve type, while negative values indicate below-average performance. We also report 95% confidence intervals for player SQS estimates—these intervals are calculated using the covariance matrix of the fixed effects and the conditional variance of the player-specific random intercepts from the mixed-effects models. These intervals also provide a practical ranking-stability diagnostic: when adjacent players’ intervals overlap materially, interpretation should emphasize performance tiers rather than exact ordinal rank positions.

Table 13: Wimbledon men’s singles: top 10 SQS rankings (centered).

First serve

Rank Server

SQS 95% CI

## 1 John Isner

0.522 (0.388, 0.656)

## 2 Milos Raonic

0.485 (0.314, 0.656)

## 3 Nicolas Jarry

0.473 (0.263, 0.683)

4 Tim Van Rijthoven 0.435 (0.249, 0.620)

## 5 Sam Querrey

0.409 (0.222, 0.596)

## 6 Quentin Halys

0.398 (0.211, 0.586)

## 7 Marin Cilic

0.380 (0.207, 0.552)

8 Matteo Berrettini 0.372 (0.236, 0.509)

## 9 Nick Kyrgios

0.372 (0.217, 0.527)

10 Kevin Anderson 0.370 (0.222, 0.518)

Second serve

Rank Server

SQS 95% CI

## 1 Maxime Cressy

0.474 (0.236, 0.712)

## 2 Milos Raonic

0.325 (0.121, 0.531)

## 3 John Isner

0.310 (0.113, 0.509)

4 Tim Van Rijthoven 0.267 (0.051, 0.484)

## 5 Quentin Halys

0.255 (0.037, 0.474)

## 6 Jeremy Chardy

0.237 (0.013, 0.462)

## 7 Nick Kyrgios

0.235 (0.023, 0.449)

8 Kevin Anderson 0.232 (0.036, 0.429)

9 Brandon Nakashima 0.226 (-0.232, 0.686)

## 10 Bradley Klahn

0.218 (-0.016, 0.454)

Table 14: Wimbledon women’s singles: top 10 SQS rankings (centered).

Rank Server

First serve SQS 95% CI

## 1 Elena Rybakina

0.414 (0.247, 0.581)

## 2 Serena Williams

0.358 (0.174, 0.544)

## 3 Jaqueline Cristian

0.342 (0.056, 0.630)

4 Ekaterina Alexandrova 0.323 (0.096, 0.551)

## 5 Qinwen Zheng

0.322 (0.114, 0.531)

## 6 Julia Goerges

0.314 (0.124, 0.505)

## 7 Ashleigh Barty

0.289 (0.127, 0.452)

## 8 Aryna Sabalenka

0.268 (0.086, 0.450)

## 9 Donna Vekic

0.266 (0.089, 0.443)

## 10 Stefanie Voegele

0.265 (0.037, 0.494)

Second serve

Rank Server

SQS 95% CI

## 1 Camila Giorgi

0.278 (0.138, 0.418)

2 Johanna Konta 0.204 (-0.062, 0.470)

## 3 Sofia Kenin

0.162 (-0.103, 0.429)

4 Dayana Yastremska 0.159 (0.069, 0.250)

5 Aryna Sabalenka 0.156 (0.044, 0.268)

## 6 Petra Kvitova

0.153 (0.038, 0.269)

7 Danielle Collins 0.151 (0.054, 0.248)

## 8 Julia Goerges

0.150 (0.047, 0.254)

## 9 Cori Gauff

0.148 (-0.003, 0.300)

## 10 Clara Burel

0.145 (-0.045, 0.335)

Table 15: U.S. Open men’s singles: top 10 SQS rankings (centered).

First serve

Rank Server

SQS 95% CI

1 Bradley Klahn 0.498 (0.263, 0.733)

## 2 Sam Querrey

0.477 (0.253, 0.701)

3 Gianluca Mager 0.456 (0.215, 0.697)

## 4 John Isner

0.456 (0.287, 0.625)

## 5 Milos Raonic

0.424 (0.204, 0.645)

6 Kevin Anderson 0.419 (0.230, 0.607)

## 7 Nick Kyrgios

0.361 (0.183, 0.539)

8 Reilly Opelka 0.351 (0.154, 0.546)

## 9 Jiri Vesely

0.339 (0.130, 0.548)

10 Alexander Bublik 0.312 (0.093, 0.531)

Second serve

Rank Server

SQS 95% CI

1 Carlos Taberner 0.451 (0.077, 0.825)

## 2 Jiri Lehecka

0.361 (-0.062, 0.784)

3 Stefano Travaglia 0.346 (-0.046, 0.738)

4 James Duckworth 0.325 (0.016, 0.633)

5 Vasek Pospisil 0.324 (-0.018, 0.666)

## 6 Jiri Vesely

0.315 (-0.066, 0.695)

## 7 Denis Kudla

0.312 (-0.001, 0.625)

## 8 John Isner

0.308 (-0.026, 0.641)

9 Alexei Popyrin 0.276 (-0.029, 0.581)

10 Cristian Garin 0.268 (-0.051, 0.586)

Table 16: U.S. Open women’s singles: top 10 SQS rankings (centered).

First serve

Rank Server

SQS 95% CI

1 Samantha Stosur 0.620 (0.348, 0.892)

## 2 Serena Williams

0.517 (0.323, 0.712)

## 3 Elena Rybakina

0.414 (0.212, 0.615)

## 4 Jodie Burrage

0.410 (0.178, 0.643)

## 5 Qinwen Zheng

0.410 (0.230, 0.589)

6 Liudmila Samsonova 0.393 (0.196, 0.590)

## 7 Julia Goerges

0.387 (0.184, 0.589)

## 8 Donna Vekic

0.383 (0.201, 0.564)

## 9 Diane Parry

0.343 (0.111, 0.575)

10 Rebeka Masarova 0.342 (0.101, 0.583)

Second serve

Rank Server

SQS 95% CI

1 Liudmila Samsonova 0.482 (0.182, 0.782)

## 2 Ashlyn Krueger

0.441 (0.038, 0.845)

3 Barbora Krejcikova 0.382 (0.115, 0.649)

4 Coco Vandeweghe 0.360 (0.009, 0.712)

5 Rebecca Peterson 0.315 (-0.010, 0.641)

## 6 Caroline Garcia

0.286 (0.005, 0.568)

## 7 Petra Kvitova

0.282 (-0.031, 0.595)

## 8 Danielle Collins

0.250 (-0.023, 0.524)

9 Rebeka Masarova 0.241 (-0.133, 0.615)

## 10 Serena Williams

0.236 (-0.017, 0.490)
