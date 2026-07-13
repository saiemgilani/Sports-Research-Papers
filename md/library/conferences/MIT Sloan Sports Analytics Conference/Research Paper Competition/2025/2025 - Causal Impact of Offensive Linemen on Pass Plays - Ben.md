<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2025/2025 - Causal Impact of Offensive Linemen on Pass Plays - Ben.pdf -->

# **CLIPP: CausaL Impact of Offensive Linemen on Pass Plays** 

Football Track Paper ID 20251476 

## **1. Introduction** 

Offensive linemen play a pivotal role in determining the outcome of pass plays in football, yet their contributions are often undervalued or misunderstood. Traditional analytics tools rely heavily on correlation-based metrics, which can provide insights but fail to capture the intricate cause-andeffect relationships that define the linemen's impact. For example, while correlation may highlight an association between quarterback pressures and incomplete passes, it does not address the causal pathways linking specific offensive linemen actions to these outcomes. This gap in understanding limits the precision and utility of such metrics for decision-making in player evaluation, development, and in-game strategies. 

To address this, we introduce **CLIPP** (CausaL Impact of Offensive Linemen on Pass Plays), a novel causal framework that quantifies the direct influence of offensive linemen on pass-play outcomes. CLIPP leverages advanced causal inference methods to move beyond predictive models and correlation-based analyses, focusing instead on estimating the causal effects of offensive linemen’s performance. Specifically, we measure the impact of allowing quarterback pressures, hits, or sacks on the probability of pass completions, isolating these effects from other confounding variables. 

This research is groundbreaking in applying causal methods to football analytics, enabling a more accurate and nuanced assessment of offensive line performance. By isolating the causal contributions of individual players, **CLIPP** provides actionable insights that can inform game strategies, optimize player utilization, and support data-driven decision-making for NFL teams and analysts. Moreover, this framework lays the groundwork for a broader adoption of causal analytics across football and other sports, marking a significant step forward in the evolution of sports analytics. 

## **2. Methods** 

To estimate the direct impact of offensive linemen on pass-play outcomes, we apply a causal inference framework using NFL player tracking data provided for the 2023 NFL Big Data Bowl. The primary objective is to measure the causal effect of offensive linemen’s performance—specifically whether allowing pressure, a quarterback (QB) hit, or a QB sack influences the likelihood of a completed pass. This approach relies on advanced statistical methods to address challenges like confounding variables and unbiased effect estimation, which are crucial for accurate causal inference. 



1 

### **Causal Framework** 

Causal inference seeks to estimate the effect of a treatment _T_ (e.g., allowing pressure, QB hits, or sacks) on an outcome _Y_ (e.g., pass completion). Unlike correlation-based approaches, causal inference accounts for confounding variables—factors that affect both the treatment and the outcome. If these confounders are not accounted for, the treatment effect estimates may be biased. 

In our framework: 

- **Treatment (** _T_ **)** : Whether an offensive lineman allowed pressure, a QB hit, or a sack (binary variable: _T_ =1 for allowed, _T_ =0 for not allowed). 

- **Outcome (** _Y_ **)** : The probability of a completed pass (binary variable: _Y_ =1 for completed, _Y_ =0 for incompletion). 

- **Features (** _X_ **)** : Descriptive variables of the offensive linemen and play context, including engineered metrics derived from player tracking data. 

The causal effect is expressed as the **Conditional Average Treatment Effect (CATE)** : 𝑪 𝑪 This measures the difference in the expected outcome = 𝐸𝐸[𝑌𝑌|𝑋𝑋= 𝑥𝑥, 𝑇𝑇= 1] − 𝐸𝐸[𝑌𝑌|𝑋𝑋= 𝑥𝑥, 𝑇𝑇= 0 _Y_ when the treatment _T_ 

_Y_ when the treatment _T_ is applied (e.g., pressure allowed) versus when it is not applied, given the same feature set _X_ . The **CATE** is simply the difference between those two outcomes in expectation. **CATE** is always negative because QB pressure, hit, or a sack allowed by offensive linemen decreases the probability of a completed pass. 

### **Doubly Robust Estimation** 

To estimate the causal effect, we use a **doubly robust (DR) model** , which combines two complementary approaches: **outcome regression** and **propensity score weighting** . The DR method is particularly powerful because it remains unbiased if either the outcome model or the propensity score model is correctly specified. 

#### **Outcome Regression Model** : 

- Predicts the expected outcome (E[Y∣X,T]) based on the features _X_ and treatment _T_ . 

- For example, it estimates the probability of a pass completion ( _Y_ ) given that an offensive lineman allowed pressure ( _T_ =1) or did not ( _T_ =0). 

#### **Propensity Score Model** : 

- Estimates the probability of receiving the treatment (P( _T_ =1∣ _X_ )) based on the features _X_ . 

- Helps to adjust for confounding by weighting observations such that treated and untreated groups are balanced in terms of their covariates. 

- 

#### **Combining the Two:** 

- The DR estimator adjusts the outcome regression predictions using the propensity scores, providing a robust estimate of the causal effect. Even if one model is misspecified, the estimate remains unbiased as long as the other model is accurate. 

The doubly robust estimator can be expressed as: 



2 



This combination ensures that: 

- If the outcome model is correct, the propensity score model is not required to be accurate, and vice versa. 

- This robustness is critical for real-world data like NFL tracking, where unobserved variables and noisy measurements are common. 

#### **Features and Feature Engineering** 

CLIPP leverages both standard features from NFL tracking data and advanced engineered metrics to capture the nuanced interactions in a pass play. These features include: 

- **Spatial Metrics** : Distance between offensive linemen and defenders, space available for the quarterback, and proximity to other players. 

- **Dynamic Metrics** : Maximum acceleration of linemen, variance in their positions (e.g., x _x_ - coordinates), and relative movement directions of offensive and defensive lines. 

- **Contextual Metrics** : Play-level details such as down, distance, and game situation. 

These features allow the model to control for confounding variables, ensuring that the causal estimates reflect the offensive linemen's direct contributions. 

### **Play-Level Causal Estimation** 

CLIPP computes the causal effect for each offensive lineman every tenth of a second from the snap to the pass. The probabilities are averaged to provide a play-level summary: 𝑪 𝑪 This approach isolates the lineman's contribution by accounting for play context and other 𝑪𝑪= 𝐸𝐸[ 𝑌𝑌∣𝑋𝑋= 𝑥𝑥, 𝑇𝑇= 0 ] −𝐸𝐸[ 𝑌𝑌∣𝑋𝑋= 𝑥𝑥, 𝑇𝑇= 1 ]    (𝑖 𝑃𝑃(𝑇𝑇= 1 ∣𝑋𝑋) > 0.5) 

confounders. 



3 

### **Robustness and Validation** 

Ensuring the reliability of causal estimates is crucial, especially when using observational data like NFL player tracking data. **CLIPP** employs multiple validation techniques to confirm the accuracy and stability of its causal estimates. These techniques include covariate balance assessments, placebo tests, subsample validation, and goodness-of-fit measures, all designed to mitigate bias and evaluate model performance under various scenarios. 

#### **Covariate Balance** 

In causal inference, ensuring that treated ( _T_ =1) and untreated ( _T_ =0) groups are comparable is critical. Covariate imbalance can lead to biased estimates of the causal effect. Propensity score weighting is used to adjust for confounders, aligning the distribution of features ( _X_ ) across groups. 

- **Implementation** : 

   - After applying propensity score weights, the balance of covariates is assessed using standardized mean differences (SMDs). An SMD below 0.1 is considered wellbalanced. 

   - Figure 7 illustrates the SMDs before and after weighting for key covariates, such as linemen positioning, movement, and defensive pressure metrics. 

- **Results** : 

   - Post-weighting, covariate imbalance was substantially reduced, with SMDs for all variables falling below the 0.1 threshold. This indicates that the treated and untreated groups are comparable, akin to a randomized controlled trial. 

#### **Placebo Tests** 

Placebo tests are used to confirm that the observed causal effects are driven by the treatment ( _T_ ) and not by random chance or spurious correlations. 

- **Procedure** : 

   - The actual treatment variable ( _T_ ) is replaced with a randomly generated variable that has no relationship with the outcome ( _Y_ ). 

   - If the causal model detects an effect under this placebo scenario, it suggests a flaw in the estimation process. 

- **Results** : 

   - When using placebo treatments, the causal effect estimates became statistically insignificant, confirming that the observed effects in **CLIPP** are attributable to the treatment (e.g., QB pressure) and not to noise or unobserved biases. 

#### **Subsample Validation** 

Subsample validation evaluates the stability and generalizability of causal estimates across different subsets of data. 

- **Procedure** : 

   - The dataset is divided into random subsets based on temporal (e.g., week-by-week) or contextual (e.g., home vs. away games) criteria. 

   - The causal model is re-estimated on each subset, and the consistency of the Conditional Average Treatment Effect (CATE) values is assessed. 

- **Results** : 

   - CATE estimates were consistent across subsamples, with less than a 5% deviation from the overall mean effect. This demonstrates that **CLIPP** is robust to variations in sample composition and maintains stability across diverse game scenarios. 



4 

#### **Goodness-of-Fit Measures** 

To evaluate the predictive performance and calibration of the causal model, we use calibration curves, Receiver Operating Characteristic (ROC) curves, and Area Under the Curve (AUC) scores. 

1. **Calibration Curves** : 

   - Calibration curves compare predicted probabilities with observed outcomes to assess the alignment between the model's predictions and reality. 

   - Figure 8 shows that the predicted probabilities align closely with the observed probabilities along the diagonal line, indicating a well-calibrated model. 

2. **ROC Curves** : 

   - The weighted ROC curve (orange curve) is well-balanced and close to the ideal 0.5 diagonal line (Figure 9). 

#### **Sensitivity Analysis** 

Sensitivity analysis evaluates the robustness of the causal estimates to violations of key assumptions, such as ignorability (no unmeasured confounders). 

- **Implementation** : 

   - The model's sensitivity to unobserved confounders is assessed by simulating scenarios where confounders are omitted or partially observed. 

   - Additional checks include examining the impact of altering thresholds for treatment definition (e.g., varying QB pressure definitions). 

- **Results** : 

   - The causal estimates remained robust across these simulations, with less than a 3% variation in CATE values, indicating that the results are not overly sensitive to minor assumption violations. 

By combining advanced feature engineering, doubly robust estimation, and rigorous validation techniques, **CLIPP** provides a robust framework for estimating the causal impact of offensive linemen on pass-play outcomes. This approach not only advances football analytics but also demonstrates the potential of causal inference methods in evaluating player performance with precision and fairness. 

## **3. Play Examples** 

**Failed Block:** Below is a play where multiple offensive linemen fail to block their assignment and allow the quarterback to be pressured. Our metric accurately distributed credit to the linemen who effectively blocked their defenders while penalizing the linemen who allowed their defenders to pressure the quarterback. In this case, the Miami offensive line had a positive **CLIPP** , meaning they collectively increased the probability of a pass completion. 

The bottom left figure shows the movements of the offensive line and is colored by **CLIPP** . The worst performers are shown in red, while the offensive linemen who positively contributed to the play are in green. The middle figure shows the **CLIPP** of each lineman every tenth of a second. Players above the horizontal line performed positively, while those below decreased the probability of a successful play. The bottom right figure shows the **CLIPP** of the entire offensive line, and it remained positive throughout the play. 



5 



**Figure 1: CLIPP Example of Pressure Allowed by Offensive Linemen** 

**Heavy Pressure and Sack Allowed:** In this play, the Atlanta Falcons’ entire offensive line is being pushed back from heavy pressure by the Philadelphia Eagles’ defense. **CLIPP** correctly identified the offensive linemen that allowed their QB to be pressured and a subsequent sack. The offensive line collectively reduced the probability of a successful pass by 40 percent (a **CLIPP** of -0.4). 



**Figure 2: CLIPP Example of a Sack Allowed by Offensive Linemen** 

**Great Pass Protection:** The following play is an example of excellent pass protection resulting in a completed pass and a 19-yard gain. Jimmy Garoppolo had plenty of time and space to throw to the open receiver Deebo Samuel. The offensive line produced a **CLIPP** of 0.8, meaning they contributed 80 percent to this successful pass. 



6 



**Figure 3: CLIPP Example of Great Pass Protection** 

## **4. Results** 

We validated **CLIPP** results by comparing them with the popular All-Pros and Pro-Bowl ratings. Most of the top ten guards, offensive tackles, and centers identified by **CLIPP** were recognized by these ratings. **Figure 4** identifies these players with ratings using dark green. 

Our causal estimate outperforms a popular supervised learning model, XGBoost. This supervised model predicts the probability that a lineman will allow a QB to be pressured, hit, or sacked using the same features in the causal model. While XGBoost is a powerful tool that can model the correlations in data, it is limited in its ability to capture causal relationships. Below are the top ten rankings of offensive linemen from both methods. Note that All-Pros and Pro-Bowlers are rated much higher by our metric compared to the supervised learning model. 



7 



**Figure 4: Comparison of Best Offensive Lineman from Causal and Correlation Methods** 

The best offensive lines were the Tamba Bay Buccaneers, San Francisco 49ers, Dallas Cowboys, Los Angeles Rams, and Kansas City Chiefs. They contributed an average of 20-22 percent to the success of pass plays. The worst-performing offensive lines were the Carolina Panthers, Miami Dolphins, New York Jets, Jacksonville Jaguars, and Houston Texans. 



8 



**Figure 5: Ranking of Offensive Lines** 

## **5. Model Validation** 

We validated **CLIPP** with independent rankings of offensive lines. Our rankings are strongly correlated with <u>Pro Football Focus</u> (Spearman’s rank correlation of 0.68). The largest discrepancies between the metrics are that **CLIPP** ranked the Minnesota Vikings and Seattle Seahawks higher while ranking the New York Jets lower. Possible explanations are the PFF measures all plays and evaluates the entire season of offensive line play. 



9 



**Figure 6: CLIPP Offensive Line Rankings versus Pro Football Focus (PFF) Rankings** 

We ensured that our causal model was well-balanced. The weighting reduced the covariate imbalance between the offensive linemen who allowed their QB to be hurried, hit, or sacked (Ti=1) and those who didn’t (Ti=0). Variables after weighting are shown in blue, and before weighting are shown in orange. The variables after weighting are lower and below the 0.1 threshold (vertical dashed line in **Figure 7** ). This is expected for a well-balanced model. Lastly, these two graphs are similar indicating the model didn’t overfit the data. 



10 



**Figure 7: Covariate Balance of Train and Validation Sets** 

We evaluated the goodness of fit by assessing how well-calibrated the model is ( **Figure 8** ). An ideal model would have predicted probabilities equal to the observed probability (shown by the dashed diagonal line). The model is well-calibrated. In a few isolated cases, the validation data incorrectly predicts a lineman allowed the QB to be pressured, hit, or sacked. 



**Figure 8: Model Calibration on Train and Validation Sets** 

**CLIPP** was validated using a receiver operating characteristic curve ( **Figure 9** ). We used it to evaluate potential violations of the positivity assumption and how well-balanced the two groups are after weighting. A large area under the curve (AUC) would suggest that there are large 



11 

differences in the linemen who allow a QB hit, pressure, or sack (Ti=1) and those who don't (Ti=0). The weighted ROC curve (orange curve) is close to the ideal diagonal line meaning that the two groups are well-balanced and like what you would expect in a randomized controlled experiment. Additionally, the propensity and expected curves are similar indicating a well-specified model. 



**Figure 9: Model ROC Curves on Train and Validation Sets** 

## **6. Limitations** 

While **CLIPP** provides a robust framework for evaluating offensive linemen through causal inference, several limitations must be acknowledged. First, the model relies on the ignorability assumption, which presumes that all confounders affecting both the treatment (e.g., allowing quarterback pressure) and the outcome (e.g., pass completions) are observed and accounted for. In practice, unobserved confounders, such as player fatigue or defensive play-calling nuances, may introduce bias into the estimates. Additionally, although NFL player tracking data is highly detailed, it may not capture certain contextual factors that influence pass-play outcomes. These missing variables could impact the accuracy of the causal estimates. 

The framework also assumes sufficient overlap in the feature distributions of treated and untreated groups, known as the positivity assumption. Rare scenarios, such as a lineman consistently performing under extreme conditions, could violate this assumption and limit the generalizability of the results. Another challenge lies in the quality of feature engineering. While **CLIPP** incorporates advanced spatial, dynamic, and contextual metrics, errors in feature selection could reduce the model’s precision. Furthermore, the current analysis evaluates linemen’s contributions on a playby-play basis and does not account for temporal dynamics, such as performance trends over a game or season, which could provide additional insights into player consistency and adaptability. 



12 

Addressing these limitations in future iterations could further enhance the framework’s robustness and utility. Incorporating additional contextual features, such as weather or crowd effects, could improve the reliability of causal estimates, while sensitivity analyses for unmeasured confounders could relax the reliance on the ignorability assumption. Expanding the framework to include temporal models, such as recurrent neural networks, could capture performance trends over time. Additionally, computational optimizations could make the framework more accessible for real-time use. By addressing these challenges, **CLIPP** can continue to advance its impact within football analytics and beyond. 

## **7. Conclusion** 

The introduction of **CLIPP** (CausaL Impact of Offensive Linemen on Pass Plays) represents a paradigm shift in how offensive linemen are evaluated, moving beyond traditional correlationbased metrics to a causal framework that quantifies their direct contributions to pass-play outcomes. This innovative approach provides NFL teams and analysts with a more precise and actionable understanding of player performance, enabling data-driven decisions in player development, scouting, and in-game strategies. By isolating the specific effects of linemen’s actions—such as allowing or preventing quarterback pressures, hits, or sacks— **CLIPP** fills a critical gap in football analytics, where offensive linemen’s contributions have historically been undervalued or misunderstood. 

The broader adoption of causal models like **CLIPP** could reshape performance evaluation across all positions, offering a clear, cause-and-effect foundation for assessing player impact. This shift enhances fairness, accuracy, and utility in player evaluation while setting a higher standard for football analytics. Beyond individual assessments, **CLIPP** empowers teams to analyze offensive line performance collectively, enabling strategic game plan adjustments, resource allocation, and targeted improvement efforts. 

**CLIPP’s** framework also has potential applications in other areas, from evaluating defensive players to analyzing skill positions like quarterbacks and wide receivers. Its methodology could extend to other sports, fostering a deeper understanding of team dynamics and performance optimization. Future development could incorporate temporal dynamics, richer contextual data, and collaborations with domain experts to further enhance its robustness and predictive power. 

By focusing on causation over correlation, **CLIPP** sets a new standard for sports analytics, empowering teams with actionable knowledge and inspiring innovation in player evaluation and strategy. As causal methods gain traction, **CLIPP** positions itself at the forefront of analytics, driving future advancements in football and beyond. 

## **References** 

[1] Pearl, Judea, and Dana Mackenzie. The Book of Why: The New Science of Cause and Effect. Penguin Books, 2018. 

[2] The Next Gen Stats Analytics Team. “Next Gen Stats: Intro to Expected Rushing Yards.” NFL.com, 20 July 2020, <u>https://www.nfl.com/news/next-gen-stats-intro-to-expected-rushing-yards.</u> 



13 

[3] Funk, Michele Jonsson, et al. “Doubly Robust Estimation of Causal Effects.” American Journal of Epidemiology, U.S. National Library of Medicine, 1 Apr. 2011, <u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3070495/.</u> 

[4] Monson, Sam. “Final 2021 NFL Offensive Line Rankings.” PFF, PFF, 12 Jan. 2022, <u>https://www.pff.com/news/nfl-final-2021-offensive-line-rankings.</u> 

[5] Addison Howard, Ally Blake, Andrew Patton, Michael Lopez, Tom Bliss, and Will Cukierski. NFL Big Data Bowl 2023. https://kaggle.com/competitions/nfl-big-data-bowl-2023, 2022. Kaggle. 



14 


