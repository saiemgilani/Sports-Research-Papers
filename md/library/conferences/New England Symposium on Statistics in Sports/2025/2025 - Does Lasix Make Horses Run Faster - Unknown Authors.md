<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - Does Lasix Make Horses Run Faster - Unknown Authors.pdf -->





**DOES LASIX MAKE HORSES RUN FASTER? Michele Sezgin**<sup>**1**</sup> **Advised by Ron Yurko**<sup>**1**</sup> **, Joel Greenhouse**<sup>**1**</sup> **, Joseph Appelbaum**<sup>**2**</sup> 1. Carnegie Mellon University Department of Statistics & Data Science, 2. Waigr **METHODS** ● **Conditional logistic regression** treats each horse as a **strata** with their own intercept: ● **Mixed effects logistic regression** treats horse intercepts as random: horses to run faster? **RESULTS Both models suggest a negative effect GLMM improves calibration by explicitly for race-level fraction of Lasix. modeling between-horse variation.** Figure 1: Each horse has raced roughly two times with and without Lasix on **Both models suggest a positive effect for Lasix on finishing in the money. DISCUSSION** ● Among two-year-old American thoroughbred race horses, using Lasix corresponds to a marginal effect of a **1.44-fold increase in odds of finishing in the money (GLMM)** (95% CI [1.40, 1.49]), controlling for relevant confounders. Figure 2: Relationship between ● Among two-year-old American thoroughbred race horses, each percentage increase in the race-level fraction of horses finishing in the money and odds is using Lasix corresponds to a marginal effect of a **0.12-factor change in odds of finishing in the money (GLMM)** linear and negative. (95% CI [0.08, 0.20]), controlling for relevant confounders. ● Model diagnostics suggest misspecification in the conditional logistic model, but correct specification of the GLMM, indicating estimation of between-horse variability is important when estimating probability of finishing in the money. **FUTURE WORK** ● Fit more flexible hierarchical models, use doubly robust estimators to extend to non-matched settings, and model other performance measures like finishing times and finishing order. ● Analyze GLMM with random slopes for Lasix use and directly model distributional shape/skew parameters as functions of Lasix use to understand its impact on horse performance variability. 

**BACKGROUND** ● Lasix (furosemide) is a loop diuretic ○ Intended to treat exercise-induced pulmonary hemorrhage ○ Speculation about performance-enhancing effects ● Horseracing Integrity and Safety Authority (HISA) restricts Lasix ○ _No race day Lasix for two-year-old and stakes races_ ○ Question: Does Lasix actually _cause_ horses to run faster? **● We aim to quantify the population-level effect of Lasix on race-day performance. DATA** ● **Response** : Finishing “in the money” (first, second, or third) ● **Treatment** : Lasix indicator Figure 1: Each horse has raced roughly two times with and without Lasix on ● **Curated sub-dataset** : average. ○ ~100,000 race results ○ ~28,000 horses ○ 1991 - 2024 ○ Two-year-old horses that have raced both with and without Lasix at least once . **(perfect matching)** Figure 2: Relationship between finishing in the money and odds is linear and negative. Figure 3: More horses finishing in the money (ITM) than expected when using Lasix. 





<!-- Start of picture text -->
●<br>Response : Finishing “in the money” (first, second, or third)<br>●<br>Treatment : Lasix indicator<br>Figure 1: Each horse has raced roughly<br>two times with and without Lasix on<br>● Curated sub-dataset :<br>average.<br>○<br>~100,000 race results<br>○<br>~28,000 horses<br>○<br>1991 - 2024<br>○<br>Two-year-old horses that<br>have raced both with and<br>without Lasix at least once<br>.<br>(perfect matching)<br>Figure 2: Relationship between<br>finishing in the money and odds is<br>linear and negative.<br><!-- End of picture text -->



<!-- Start of picture text -->
Figure 3: More horses finishing in the<br>money (ITM) than expected when<br><!-- End of picture text -->



<!-- Start of picture text -->
Figure 2: Relationship between<br>finishing in the money and odds is<br>linear and negative.<br><!-- End of picture text -->


