<!-- source: 2026 - Hierarchical Bayesian Modeling of Cross-League Performance Translation in Elite Football - Shaikh.pdf -->
<!-- doi: 10.1177/22150218261481583 · Journal of Sports Analytics 12 (SAGE, Aug 2026) · CC BY-NC 4.0 -->
<!-- text source: author's open SocArXiv preprint (osf.io/59a7s, 2026-06-18, DOI 10.31235/osf.io/59a7s) — the SAGE version of record is behind a Cloudflare datacenter-IP block. Abstract, tables and numbers match the published record; final copy-editing may differ. -->

# Hierarchical Bayesian Modeling of Cross-League Performance Translation in Elite Football

**Mohammad Arshan Shaikh**
Khoury College of Computer Sciences, Northeastern University Miami — Miami, Florida, USA
`shaikh.mohammada@northeastern.edu` · ORCID 0009-0004-6962-3633

*Journal of Sports Analytics*, vol. 12 (2026). DOI [10.1177/22150218261481583](https://doi.org/10.1177/22150218261481583). Open access, CC BY-NC 4.0.

## Abstract

Predicting footballer performance following cross-league transfers is challenging when statistics derive from distinct tactical and competitive environments. We introduce a hierarchical Bayesian framework for quantifying league translation effects separately for attacking/midfield and defensive player roles. Using bridge datasets of 174 attacking and midfield transfers and 106 defensive transfers from the four major European feeder leagues (La Liga, Bundesliga, Serie A, Ligue 1) and within-Premier League transfers as a domestic baseline (2017/18–2022/23), we fit joint multivariate Bayesian models decomposing translation effects into league, team, and age components while capturing metric correlations via LKJ covariance structures. The primary contribution is calibrated uncertainty quantification: 90% highest density intervals enabling principled probabilistic reasoning in recruitment decision-making. Validation on two held-out, strictly cross-league transfer cohorts (attacking and midfield *n* = 45, defensive *n* = 35) demonstrates near-nominal interval coverage on attacking metrics and excellent convergence diagnostics (zero divergences, R̂ ≤ 1.005, where R̂ is the Gelman–Rubin potential scale reduction factor). Results reveal asymmetric league effects: La Liga shows a credibly positive shot-creating actions association (posterior mean +0.306, 90% HDI [+0.015, +0.578]). The framework is currently restricted to Premier League destinations; extending to multi-destination prediction remains an important avenue for future work.

**Keywords:** Bayesian hierarchical modeling, football analytics, performance translation, uncertainty quantification, probabilistic prediction, league effects.

## 1. Introduction

Cross-league player transfers in elite football involve substantial financial investment yet limited quantitative frameworks for predicting performance adaptation. Raw per-90 statistics are context-dependent: they reflect not just individual player skill but also the tactical system, defensive pressure, and space availability in the source league. A player's performance metrics consequently shift systematically when transferring between leagues. This systematic shift, termed the **league tax**, captures the conditional association between source-league context and post-transfer performance, and varies by metric, age, and team context. It is important to note from the outset that these effects are **conditional associations** estimated from historical transfer data, **not causal quantities**; they do not isolate the effect of the league itself from selection processes or unmeasured confounders.

Existing approaches oscillate between subjective scouting (contextually informed but uncalibrated) and naive per-90 comparison (precise but context-blind). Neither systematically quantifies the multidimensional league tax nor provides principled uncertainty quantification necessary for inference and decision-making under uncertainty.

The league tax is not uniform. Shot-creating actions (SCA) may increase or decrease when moving to the Premier League while simpler volumetric metrics remain more stable. Translation patterns differ by age and destination team context. Standard rule-of-thumb adjustments ignore this complexity.

This paper develops a hierarchical Bayesian framework that decomposes translation effects into interpretable random-effect components (league, team, age) while capturing metric correlations through joint multivariate distributions. We construct separate models for attacking and midfield players (174 training transfers) and defenders (106 training transfers) to respect distinct statistical profiles. Third, unlike traditional scouting models that sample cross-border transfers in isolation (thereby conflating macro-environmental league differences with universal team-transition friction), this framework explicitly integrates **within-Premier League transfers as an untreated baseline control**, allowing the model to empirically isolate the universal baseline noise of changing clubs from true competitive and tactical league variances. The framework is restricted to Premier League destinations, which is both a practical constraint of the training data and a genuine limitation of scope; generalisation beyond this destination requires future work. The framework achieves principled uncertainty quantification through 90% highest density intervals (HDI) as the primary deliverable, with point prediction accuracy presented as a secondary diagnostic.

## 2. Literature Review

### 2.1 Pillar A: Performance Translation in Sports

The problem of predicting player performance across competitive contexts extends decades beyond football. In baseball, James (1985) introduced Major League Equivalencies (MLE) to estimate how minor league players would perform in Major League Baseball by controlling for league quality differences. This pioneering work established that systematic translation adjustments can be derived from historical data, forming the conceptual foundation for modern cross-league prediction. Albert and Bennett (2003) extended these concepts in a systematic treatment of baseball statistics, demonstrating how statistical frameworks can quantify the role of chance and context in sports performance, principles directly applicable to cross-league translation.

Application of translation principles to football remained limited until the 2010s. Pavlidis et al. (2014) introduced similar-player matching methods, using Euclidean distance in performance space to identify comparable players across leagues and historical periods. These similarity-based approaches became the industry standard for cross-league valuation, shifting from subjective judgment to data-driven comparison. However, such methods have fundamental limitations: they explain *what* similar players achieved but not *why* translation succeeded or failed; they provide point estimates without uncertainty quantification; and they do not scale naturally to multiple metrics or hierarchical structures.

A significant methodological advance came with McHale and Szczepański (2014), who applied mixed-effects models to football transfer valuation. By modelling league as a random effect, they demonstrated that league quality is a measurable, quantifiable variable that significantly impacts both market value and on-field performance. Their mixed-effects approach represented the first serious application of hierarchical methodology to cross-league prediction in football.

Simultaneously, the expected metrics revolution transformed scouting practice. Pappalardo et al. (2019) established that multi-dimensional statistical profiles are valid for performance evaluation and talent identification. Their PlayeRank framework demonstrated that multi-metric player representations outperform single-metric approaches for ranking and talent scouting, justifying modelling multiple correlated metrics jointly rather than independently.

More recently, machine learning approaches have demonstrated competitive predictive performance for individual performance modelling. Müller et al. (2021) showed that gradient boosting methods can capture nonlinear age-performance interactions and league-quality adjustments from historical transfer data, providing a strong predictive baseline against which uncertainty-focused Bayesian approaches should be benchmarked. Van Roy et al. (2020) applied deep learning architectures to event-level tracking data for player rating, illustrating the breadth of methodology now applied to cross-context performance evaluation. These ML advances motivate an explicit comparison between the Bayesian hierarchical framework and gradient boosting baselines in the present work.

The closest methodological analogue to the present work in the recent literature is Glazer (2026), who estimates G League-to-NBA league translation factors for basketball statistics using a matching and difference-in-differences (DiD) framework. Glazer constructs a comparable player pool from players observed in both leagues across consecutive seasons (**the same bridge structure adopted here**) and applies DiD to produce causal estimates of how a player's statistics would have appeared in the destination league. This causal framing is an important contribution: by explicitly invoking the parallel trends assumption, Glazer moves beyond the correlational MLE tradition toward treatment-effect estimation. The present work is **complementary rather than competing**: rather than targeting a single causal point estimate per statistic, HBFLT produces a full posterior distribution over plausible post-transfer performance ranges, enabling calibrated uncertainty quantification and probabilistic inference. The two approaches represent different priorities (causal identification versus uncertainty representation).

### 2.2 Pillar B: Bayesian Hierarchical Methodology

Gelman et al. (2013) established foundational frameworks for hierarchical Bayesian models and partial pooling, demonstrating how to balance group-level structure with individual-level variation. Partial pooling provides a principled middle ground between complete pooling (treating all groups identically) and no pooling (independent estimation for each group). In cross-league transfer contexts, partial pooling proves particularly valuable when transfer volumes vary substantially across source leagues, allowing information from large-sample leagues to stabilise estimates for small-sample leagues through borrowing of strength.

The hierarchical structure naturally accommodates random effects at multiple levels: league, team, and age. The partial pooling principle ensures that league-specific tax estimates shrink toward the global mean in proportion to the amount of data available, balancing data-driven inference with regularisation.

Multivariate extensions of hierarchical models introduce complexity through covariance structure specification. Lewandowski et al. (2009) introduced the LKJ (Lewandowski–Kurowicka–Joe) distribution, providing a flexible, interpretable prior on correlation matrices that avoids Wishart-related numerical instabilities. LKJ with shape parameter η > 1 is skeptical of extreme correlations while allowing data to override this prior, a balance particularly valuable when sample size is modest relative to the number of metrics.

Joint modelling of correlated metrics offers concrete advantages over separate univariate models. Borrowing of strength across metrics stabilises estimates for sparse metrics by sharing information with more reliably measured ones. Metric correlations themselves become estimable quantities. Joint modelling produces posterior predictive distributions that respect learned metric coupling, enabling scenario analysis that maintains natural metric interdependencies.

Calibration of predictive intervals (the degree to which nominal coverage matches empirical coverage) has been identified as a critical property of Bayesian forecasting models in sports contexts (Gneiting and Raftery 2007). This work adopts **empirical coverage of 90% HDIs as the primary validation criterion**, following the recommendation that calibration be reported alongside point-prediction accuracy for full characterisation of probabilistic forecasts.

### 2.3 Pillar C: Football Metrics and Domain Knowledge

Modern performance metrics build on early work by Reep and Benjamin (1968) and Pollard and Reep (1997), who provided foundational empirical frameworks for systematic performance measurement in football.

- **Shot-creating actions (SCA)** counts the two offensive actions directly preceding a shot, measuring direct involvement in chance creation.
- **Progressive passes (PrgP)** counts passes that move the ball at least 10 yards closer to the opponent's goal.
- **Progressive carries (PrgC)** counts dribbles that move the ball at least 5 yards closer to the opponent's goal.
- **Key passes (KP)** counts passes that directly lead to a shot.

These process metrics are particularly sensitive to league context, depending on average possession levels, team tactical philosophy, and available space. Decroos et al. (2019) introduced VAEP (Valuing Actions by Estimating Probabilities), emphasising that player contribution links tightly to tactical role and game state, supporting position-specific and context-specific modelling.

Spearman (2018) demonstrated that structural league differences in team tactics, possession style, and defensive pressure create systematic differences in how process metrics accumulate across leagues, independent of individual player quality. This motivates explicit league-level modelling for context-sensitive metrics such as KP, PrgP, PrgC, and SCA rather than treating league differences as random noise.

Tackles won (TklW), interceptions (Int), clearances (Clr), and blocks (Blocks) form the defensive metric set. Substantial role heterogeneity exists between centre backs and full backs, with fundamentally different defensive action distributions. This role heterogeneity motivates a separate defensive bridge.

### 2.4 Synthesis and Current Contribution

These three pillars collectively motivate the current framework. We inherit conceptual foundations from baseball translation work and early football analytics, apply modern Bayesian statistical machinery that was unavailable to prior practitioners, and ground metric selection in established football analytics literature. The combination of hierarchical partial pooling, heavy-tailed likelihood, joint multivariate inference with LKJ covariance structures, and separate bridges for attacking and defensive roles distinguishes this framework from prior rule-of-thumb and linear-adjustment approaches. Critically, the primary contribution is **calibrated uncertainty quantification rather than point-prediction superiority** over ML baselines, which is explicitly benchmarked and discussed.

## 3. Data Construction and Bridge Datasets

### 3.1 Transfer Bridge Dataset Architecture

We construct separate bridge datasets from players transferring into the Premier League from the Big Five leagues (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) across consecutive seasons. The training bridge comprises five season-transition pairs (2017/18→2018/19 through 2021/22→2022/23), meaning source-season data spans 2017/18–2021/22 and destination-season data spans 2018/19–2022/23. Two held-out test cohorts (2022/23→2023/24 and 2023/24→2024/25) are excluded from training entirely.

- **Attacking Bridge (ATT+MID):** 174 training transfers of forwards and attacking midfielders; 45 held-out test transfers. Target metrics: KP, PrgP, PrgC, SCA.
- **Defensive Bridge (DEF):** 106 training transfers of outfield defenders; 35 held-out test transfers. Target metrics: TklW, Int, Clr, Blocks.

Importantly, the held-out test cohorts consist **exclusively of cross-border transfers** from La Liga, Bundesliga, Serie A, and Ligue 1 into the Premier League. Intra-Premier League transfers, while utilised during training to establish the baseline variance of transfer shock, are entirely excluded from the out-of-sample validation sets. This strict exclusion ensures that the validation phase provides a rigorous, uncompromised evaluation of the framework's ability to estimate true cross-environmental translation effects rather than relying on stable intra-league baselines.

**Inclusion criteria:** true club change, Premier League destination, minimum 5 full 90-minute equivalents (90s) in both source and destination seasons. This threshold ensures sufficient playing time for reliable per-90 rate estimation; lowering it further would include players with as few as three matches, producing unreliable rate estimates that could distort validation results. Transfer type (permanent vs. loan) is not distinguished, as the FBref dataset does not include this information; this is acknowledged as a limitation in Section 8.

The resulting bridge sizes (174 ATT+MID and 106 DEF training transfers) reflect the **complete population** of qualifying transfers in the dataset window, not a sample. This is a methodological strength for a Bayesian model: partial pooling operates on the full observed transfer history, and the hierarchical prior structure is particularly well-suited to settings where data at some levels are genuinely sparse. Only a small minority of players transferring to the Premier League qualify under these criteria, because the Premier League is widely regarded as the most competitive league in the world; clubs recruit selectively, and most transfers involve players who have established themselves as top performers in their source league. The low bridge count therefore reflects the genuine rarity of qualifying transfers and the selectivity of the Premier League recruitment process, not a deficiency that could be addressed by loosening inclusion thresholds.

Crucially, the bridge dataset includes **domestic intra-Premier League transfers**. While these transfers feature a league transition mapping of Premier League → Premier League (and thus contribute a net-zero addition to the directional league-tax parameters), they provide a critical mathematical function. They supply the joint hierarchical framework with an empirical baseline for standard intra-player variance following a club change under a static competitive environment.

The two-bridge architecture reflects a fundamental modelling decision: attacking and defensive roles have distinct statistical profiles and metric interdependencies. Separate bridges avoid imposing spurious correlations between fundamentally different metric domains.

### 3.2 Source League Distribution

*Figure 1* presents the bridge dataset composition by source league and transfer season pair (ATT+MID training bridge *n* = 174 across five season pairs; DEF training bridge *n* = 106). Within-league Premier League transfers (players who moved between two Premier League clubs across consecutive seasons) are included as the baseline reference group against which foreign league effects are estimated. Because these players experienced the same destination league environment without any cross-league transition, their log-ratios reflect the within-PL year-on-year baseline, providing an anchor for the league association parameters τ<sub>L,s</sub> for all foreign source leagues.

### 3.3 Response Variable Construction

For each metric *s* and player *i*:

$$y_{i,s} = \log\!\left(\frac{\text{destination}_{i,s,\text{per90}} + \epsilon}{\text{source}_{i,s,\text{per90}} + \epsilon}\right), \qquad \epsilon = 0.05$$

Positive values indicate metric increase post-transfer (i.e. the player's rate for that metric is higher in the Premier League than at the source club); negative values indicate a decrease. Per-90 rates are computed as season totals divided by total minutes divided by 90. The ε = 0.05 additive offset prevents extreme log-ratios when source per-90 rates are near zero, improving numerical stability while allowing meaningful ratios for well-measured players.

Each observation associates with: source league *L<sub>i</sub>*, binary foreign indicator (1 if source league ≠ PL), destination team *t(i)*, player identifier *j(i)*, and centered age *ã<sub>i</sub>* = *a<sub>i</sub>* − *ā*.

## 4. Hierarchical Bayesian Modeling

### 4.1 Model Motivation and Structure

Cross-league performance translation involves complex, nested dependencies: players are nested within teams, which are nested within source leagues. Standard approaches either ignore this structure (univariate regression) or impose oversimplified structures (fixed effects). Hierarchical Bayesian modelling accommodates this nesting naturally while enabling partial pooling: information about one league informs estimates for similar leagues through a shared population distribution.

The key insight is that translation effects at each level are random draws from a population distribution. La Liga's SCA translation effect is drawn from the same underlying distribution as Bundesliga's effect, but with league-specific deviation. This partial pooling prevents extreme estimates from small-sample leagues while allowing large-sample leagues to express their own influence.

Separate bridges for attacking and defensive roles avoid imposing unrealistic correlation structures between fundamentally different metric domains.

### 4.2 Model Specification

Joint multivariate Student-*t* distributions for both bridges:

$$y_i \sim \text{MvStudentT}(\nu = 6,\ \mu_i,\ \Sigma)$$

Fixed degrees of freedom (ν = 6) accommodate adaptation outliers robustly. Heavy tails reduce the influence of extreme cases while maintaining flexibility for typical observations. The choice of ν = 6 reflects a balance between robustness to outliers (smaller ν) and efficiency under approximate normality (larger ν). Student-*t* likelihoods have been advocated for hierarchical sports models precisely because transfer outcomes include genuine heavy-tail events (injuries, tactical mismatches) that Gaussian likelihoods handle poorly (Gelman et al. 2013).

Mean structure:

$$\mu_{i,s} = \alpha_s + \text{foreign}_i \cdot \tau_{L_i,s} + \beta^{\text{team}}_{t(i),s} + \beta^{\text{age}}_s \tilde{a}_i + \beta^{\text{age2}}_s \tilde{a}_i^2$$

Component interpretation:

- **α<sub>s</sub>** — global intercept capturing within-league baseline adaptation noise
- **τ<sub>L,s</sub>** — league association for source league *L*, applied only when foreign = 1; domestic transfers receive τ = 0, forming the baseline
- **β<sup>team</sup><sub>t(i),s</sub>** — destination team random effect capturing systematic differences in how teams integrate transferred players
- **β<sup>age</sup><sub>s</sub>, β<sup>age2</sup><sub>s</sub>** — quadratic age curve modelling how translation effects vary across career stages

By assigning the Premier League as the reference baseline (τ = 0), the parameters for the remaining four feeder leagues represent the conditional expected translation effect relative to domestic top-flight standard performance. Because the dataset includes intra-PL transfers, the residual variance components (Σ and team-level random effects) absorb the **universal transfer shock** (e.g. adaptation to new teammates, tactical disruption, change in playing environment). Consequently, the league association parameters τ<sub>L,s</sub> are insulated from general transfer noise and reflect environmental differences in league quality, tempo, and tactical paradigms.

The foreign indicator ensures domestic transfers serve as the reference baseline (τ = 0), while cross-league transfers receive league-specific associations. These associations reflect the conditional relationship between source-league context and post-transfer performance in the training data; they should not be interpreted causally, as they may partly reflect selection effects (i.e. the types of players that clubs recruit from each league).

### 4.3 Prior Specification and Regularisation

All priors are weakly informative, designed to prevent pathological estimates while allowing data dominance:

| Component | Prior |
|---|---|
| Global intercepts | α<sub>s</sub> ~ N(0, 0.2) |
| League association hyper-mean | µ<sub>L,s</sub> ~ N(0, 0.2) |
| League association hyper-scale | σ<sub>L,s</sub> ~ HalfNormal(0.5) |
| League association (non-centred) | τ<sub>L,s</sub> = µ<sub>L,s</sub> + z<sub>L</sub>·σ<sub>L,s</sub>, z<sub>L</sub> ~ N(0, 1) |
| Team-level SD | σ<sup>team</sup><sub>s</sub> ~ HalfNormal(0.2) |
| Age coefficient | β<sup>age</sup><sub>s</sub> ~ N(0, 0.05) |
| Age² coefficient | β<sup>age2</sup><sub>s</sub> ~ N(0, 0.02) |
| Observation-level SD | σ<sub>s</sub> ~ HalfNormal(0.3) |
| Metric correlation matrix | LKJ(η = 3.0) |

League-specific associations shrink toward the global mean in proportion to available transfer data, while still allowing data-driven deviations. Team-level variation is mildly regularised to prevent overfitting on the modest sample.

The LKJ concentration η = 3.0 reflects a deliberate regularising constraint: η = 1.0 would place a uniform prior over all correlation matrices, assigning equal probability to near-perfect correlations that are implausible given the domain context and would likely reflect low-sample noise rather than genuine metric relationships. Setting η = 3.0 penalises extreme correlations (above approximately ±0.9) while remaining permissive of moderate correlations expected among role-specific metrics. This keeps the posterior covariance matrix numerically stable and prevents the model from over-learning transient tactical patterns within the modest transfer windows available.

### 4.4 Covariance Structure and Metric Coupling

Covariance matrix Σ is parameterised via Cholesky decomposition to ensure positive definiteness. The correlation matrix follows corr(Σ) ~ LKJ(η = 3.0), with marginal scales given HalfNormal(0.3) priors.

Joint modelling stabilises estimates for sparse metrics through information borrowing while quantifying metric interdependencies. EDA confirms that ATT+MID metrics exhibit moderate-to-strong inter-correlations (**KP↔SCA: 0.81**), while DEF metrics show notably weaker correlations (**0.10–0.31**), consistent with the distinct positional roles aggregated in the defensive bridge.

### 4.5 Weighting and Inference

Observations are weighted by a minutes-played factor:

$$w_i = \sqrt{\frac{\text{min}_{i,\text{src}}}{\text{min}_{i,\text{src}} + 450}}$$

This soft threshold smoothly reduces weight for players with limited source-season minutes while maintaining full weight for well-used players. The scaling constant of 450 minutes (five full 90s) substantially downweights players at the inclusion threshold. A sensitivity analysis varying this constant across 270–900 minutes confirmed that league association posteriors are robust to this choice, with negligible changes to posterior means or HDI widths.

Both models are fit using PyMC (Abril-Pla et al. 2023) via Hamiltonian Monte Carlo with the No-U-Turn Sampler (NUTS): **1500 draws per chain, 2 chains (3000 total samples), 1500 tuning steps, target acceptance 0.95, random seed 42**. Target acceptance of 0.95 is moderately conservative relative to the default of 0.80, encouraging smaller step sizes and more thorough posterior exploration for hierarchical models with multiple levels of random effects.

### 4.6 Software and Computational Environment

All analyses were conducted in Python 3.10. Hierarchical Bayesian models were specified and fitted using **PyMC 5.28.5** with the **NumPyro 0.21.0** backend for NUTS sampling; **JAX/JAXlib 0.7.2** provided compilation and automatic differentiation. Posterior summaries and highest density intervals were computed with **ArviZ 0.22.0**. Data processing used **pandas 2.2.2** and **NumPy 2.0.2**. Machine learning baselines (Ridge regression, Gradient Boosting Machine) were implemented with **scikit-learn 1.6.1**. Figures were produced with matplotlib 3.10.0 and seaborn 0.13.2. All computations were run on Google Colab with GPU acceleration (NVIDIA T4). The random seed was fixed at 42 throughout. Code: <https://github.com/mohammadarshan/football-league-translation>.

## 5. Validation Framework

### 5.1 Convergence Diagnostics

| Model | Divergences | Max R̂ | N̂<sub>eff</sub> |
|---|---:|---:|---|
| ATT+MID (*n*<sub>train</sub> = 174) | 0 | 1.003 | > 1000 |
| DEF (*n*<sub>train</sub> = 106) | 0 | 1.005 | > 1000 |

*Table 1: Convergence diagnostics.* R̂ values near 1.0 confirm between-chain and within-chain variance are approximately equal; values below 1.05 are conventionally taken as evidence of convergence. Zero divergences indicate no Hamiltonian sampler pathologies. Effective sample sizes exceed 1000 for all key parameters.

### 5.2 Out-of-Sample Validation

Two temporally held-out transfer cohorts serve as the test set: (1) 2022/23→2023/24 and (2) 2023/24→2024/25, combined to yield *n* = 45 ATT+MID and *n* = 35 DEF test observations. Both cohorts are excluded from training via explicit season-pair exclusion to prevent data leakage.

**Baseline comparisons:**

1. **Univariate** — independent per-metric Bayesian models without joint covariance structure.
2. **Ridge regression** — ℓ₂-regularised linear model with cross-validated penalty selection; prediction intervals derived from out-of-fold residuals.
3. **Gradient Boosting Machine (GBM)** — ensemble of decision trees with cross-validated hyperparameters and out-of-fold residual intervals.

ML baselines use identical features (source per-90 rates, league indicator, age, team) as the Bayesian model.

**Evaluation metrics:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and empirical coverage of nominal 90% prediction intervals. **Coverage is the primary criterion**, as calibrated uncertainty quantification is the central contribution; MAE and RMSE are presented for completeness and context.

## 6. Results

All validation metrics are computed exclusively on the strictly cross-league held-out test cohorts. The primary contribution of HBFLT is calibrated uncertainty quantification: the posterior predictive intervals reflect genuine epistemic uncertainty about cross-league adaptation. A recruitment department making a substantial financial commitment does not require a model that asserts a precise point estimate; it requires a model that accurately characterises the full distribution of plausible outcomes, including downside risk. Point prediction accuracy, while reported for comparison against ML baselines, is treated as a secondary diagnostic throughout.

### 6.1 Posterior League Associations

The **La Liga SCA association** (posterior mean **+0.306**, 90% HDI **[+0.015, +0.578]**) is the most notable finding: the 90% HDI excludes zero, providing credible evidence that La Liga attacking players show higher SCA rates in the Premier League than their source-season rates would predict. This may reflect the higher-tempo, more direct style of Premier League play creating more shot-preceding sequences for technically capable La Liga attackers, though alternative explanations including selection effects cannot be ruled out. For Ligue 1 and Serie A, progression and creation metrics show positive associations, consistent with the model detecting systematically lower creation-metric baselines in those leagues relative to the Premier League.

In the DEF model, Ligue 1 and Serie A TklW associations are credibly positive, suggesting defenders from these leagues tend to record higher tackle rates in the Premier League. Posterior uncertainty is wider for Int and Clr, consistent with greater distributional heterogeneity in the test set.

Creative and progression metrics (KP, PrgP, PrgC, SCA) exhibit wider variation across leagues than would be expected under the no-translation assumption. These patterns reflect **conditional associations** in the training data and should not be interpreted as causal league effects.

### 6.2 Attacking Players (ATT+MID)

| Metric | HBFLT MAE | HBFLT Cov.(90%) | Univariate MAE | Univ. Cov. | Ridge MAE | Ridge Cov. | GBM MAE | GBM Cov. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| KP   | 0.349 | **0.933** | 0.349 | 0.956 | 0.341 | 0.978 | 0.304 | 0.956 |
| PrgP | 0.299 | **0.889** | 0.298 | 0.889 | 0.293 | 0.911 | 0.310 | 0.867 |
| PrgC | 0.335 | **0.889** | 0.333 | 0.933 | 0.321 | 0.933 | 0.322 | 0.911 |
| SCA  | 0.249 | **0.889** | 0.249 | 0.978 | 0.244 | 0.978 | 0.261 | 0.956 |

*Table 2: Out-of-sample validation for ATT+MID metrics (n<sub>test</sub> = 45).* MAE on log-ratio scale; Cov.(90%) is empirical coverage of 90% prediction intervals. ML baseline intervals are derived from out-of-fold residuals. HBFLT coverage is near-nominal across all metrics (0.889–0.933). Ridge and GBM achieve lower MAE on some metrics, as expected for point predictors on a small test set; HBFLT's advantage lies in calibrated posterior uncertainty rather than point accuracy.

### 6.3 Defensive Players (DEF)

| Metric | HBFLT MAE | HBFLT Cov.(90%) | Univariate MAE | Univ. Cov. | Ridge MAE | Ridge Cov. | GBM MAE | GBM Cov. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TklW   | 0.247 | **0.943** | 0.246 | 0.943 | 0.244 | 0.943 | 0.245 | 0.971 |
| Int    | 0.390 | **0.657** | 0.388 | 0.829 | 0.392 | 0.829 | 0.388 | 0.829 |
| Clr    | 0.333 | **0.800** | 0.331 | 0.886 | 0.327 | 0.914 | 0.280 | 0.886 |
| Blocks | 0.292 | **0.857** | 0.291 | 0.914 | 0.292 | 0.914 | 0.256 | 0.914 |

*Table 3: Out-of-sample validation for DEF metrics (n<sub>test</sub> = 35).* TklW achieves above-nominal HBFLT coverage (0.943). Int coverage is notably below nominal (0.657) for HBFLT due to distributional mismatch; see Section 6.4. Univariate and ML baselines show higher Int coverage, reflecting their wider out-of-fold residual intervals relative to HBFLT's posterior intervals.

### 6.4 Performance and Calibration

The framework demonstrates useful calibration for attacking metrics, where empirical coverage tracks the nominal 90% target closely. Defensive metrics show greater variability in calibration. TklW is well-calibrated; Int is notably under-covered.

Diagnostic analysis reveals that the **Int under-coverage reflects a genuine distributional mismatch** between training and test sets rather than a modelling flaw: the test-set Int log-ratio standard deviation (0.486) exceeds that of the training bridge (0.380), meaning the model's predictive intervals (estimated from training-set variance) are too narrow for the more variable test distribution. This is an inherent limitation of any model trained on one time window and evaluated on another when distributional shift occurs. Clr coverage (0.800) is similarly affected by within-position role heterogeneity: the DEF bridge aggregates centre backs and full backs whose clearance rates differ systematically, inflating residual variance beyond what the model captures. Future iterations could address this by introducing position-specific hyper-priors within the defensive model, allowing the covariance structure to automatically separate width-based defenders (full backs) from central-area defenders (centre backs) without requiring explicit position labels.

The framework's point-prediction MAE is broadly comparable across HBFLT, Univariate, Ridge, and GBM on this test set. This is not surprising: with *n* = 45 ATT+MID and *n* = 35 DEF test observations, the statistical power to distinguish models on MAE is limited, and heavy regularisation in Ridge is optimal for small, noisy training sets. The primary differentiator of the Bayesian framework is its calibrated uncertainty representation and interpretable posterior decomposition, **not** a claim of superior point accuracy.

### 6.5 Boundaries of Multivariate Joint Architectures and Point-Prediction Trade-offs

Two structural boundaries merit explicit acknowledgment.

**First,** the hierarchical architecture intentionally prioritises uncertainty calibration over point-prediction minimisation. By employing regularising hyper-priors and Student-*t* heavy tails, the model applies shrinkage that pulls extreme individual predictions toward league and team means. This sacrifices marginal point accuracy to guard against overfitting to historical transfer anomalies (an appropriate trade-off given that football transfers are subject to large, unobservable human and environmental shocks such as managerial changes, off-pitch disruption, and soft-tissue injuries that no model can anticipate). The consequence is that a well-regularised ML baseline such as Ridge at α = 100 can match or marginally exceed HBFLT on MAE: both are shrinking toward the mean, but Ridge does so **without producing calibrated intervals**.

**Second,** results confirm that a single omnivorous multivariate structure is ill-suited for the full spectrum of football performance metrics. Highly zero-inflated or low-frequency event metrics violate the linear symmetric assumptions of the joint covariance framework. Furthermore, tactical role-dependency introduces conflicting covariance signals: metrics such as clearances and progressive carries are structurally mutually exclusive in possession-dominant versus low-block defensive teams, meaning any forced correlation between them reflects team style rather than player talent. This explicitly validates the design decision to decouple the framework into role-specific pipelines (ATT+MID and DEF), preserving the behavioural integrity of the underlying covariance matrices.

### 6.6 Theoretical Implications

The asymmetry between attacking creation metrics (wider posterior league associations) and simpler volumetric metrics (narrower associations) aligns with football theory: chance creation and ball progression depend heavily on team system, available space, and opponent pressure, while simpler count metrics are more stable. The model's joint LKJ structure successfully captures the KP↔SCA correlation structure in the ATT+MID bridge, producing posterior predictive distributions with coherent metric co-variation. For the DEF bridge, the weaker inter-metric correlations (0.10–0.31) indicate that defensive metrics are more independently distributed across positions, consistent with distinct positional roles.

## 7. Discussion

### 7.1 Methodological Contributions

The joint multivariate architecture with hierarchical random effects achieves excellent convergence diagnostics (zero divergences, R̂ ≤ 1.005) and near-nominal coverage on ATT+MID metrics. The hierarchical structure effectively decomposes translation associations into interpretable components. The two-bridge architecture respects the fundamental domain distinction between attacking creation and defensive action metrics.

The explicit inclusion of GBM and Ridge baselines alongside the Bayesian model provides a more complete picture than purely Bayesian comparisons. On this test set the models achieve similar MAE, consistent with prior literature showing that ensemble ML methods are strong point predictors when features are rich and training sets are modest (Müller et al. 2021). The advantage of the Bayesian framework lies in the posterior: it provides a full probability distribution over plausible post-transfer performance, enabling **threshold queries** (e.g. probability that a player achieves ≥ *X* SCA per 90) and principled propagation of transfer uncertainty into downstream recruitment decisions.

### 7.2 Causal Interpretation and Ecological Inference

League association parameters estimated from historical transfer data reflect **conditional associations, not causal league effects**. The model observes players who chose (or were chosen) to transfer from specific leagues to the Premier League, a non-random selection process. Players transferring from La Liga to the Premier League are systematically different from those who remain in La Liga, and this selection may partially explain observed league-level associations. The La Liga SCA finding, while credible within the model, should therefore be interpreted cautiously: it reflects the experience of historical La Liga-to-PL transferees rather than a causal property of La Liga as a league environment. Addressing selection bias rigorously would require instrumental variable or structural approaches beyond the scope of the current framework.

### 7.3 Comparison with Previous Literature

The mixed-effects approach of McHale and Szczepański (2014) established the precedent for league as a random effect in transfer modelling. The present work extends this in three directions: joint multivariate modelling of correlated metrics, explicit calibration assessment of predictive intervals, and inclusion of ML baselines as a comparative benchmark. The emphasis on calibrated uncertainty distinguishes this framework from prediction-oriented ML approaches (Müller et al. 2021, Van Roy et al. 2020), where point accuracy is typically the sole criterion. The use of HDI coverage as a primary evaluation metric follows the recommendation of Gneiting and Raftery (2007) that probabilistic forecasts be assessed on both sharpness and calibration.

## 8. Limitations

- **Loan transfers not distinguished** — the bridge does not distinguish permanent transfers from loan spells, as the FBref dataset does not include transfer type information. Loan players may exhibit different adaptation patterns; this unobserved heterogeneity is absorbed into the residual variance.
- **Premier League destination only** — generalising league tax estimates to other destinations would require multi-destination bridge data and a structural model for destination-league quality.
- **Selection bias** — players transferring to the Premier League are not random draws of their source leagues. Systematic differences in player profile, agent relationships, club ambition, and transfer fees all influence who transfers.
- **Defensive role heterogeneity** — the DEF bridge aggregates centre backs and full backs, who have distinct translation mechanisms. Destination position labels are unavailable in the data, inflating residual variance and degrading calibration for Clr and Int.
- **Int distributional mismatch** — interceptions under-coverage (0.657) reflects higher test-set log-ratio variance than seen in training (test SD 0.486 vs. training SD 0.380).
- **Adaptation lag** — the model estimates Year-1 post-transfer performance. Players requiring a longer adaptation period show larger Year-1 log-ratios not attributable to league quality differences.
- **Coarse position buckets** — the ATT+MID grouping obscures distinctions between central forwards, wide forwards, and attacking midfielders.
- **Scope** — restricted to outfield players; goalkeepers have fundamentally different performance metrics and translation dynamics.

## 9. Conclusion

This paper develops hierarchical Bayesian methodology for quantifying cross-league performance translation associations in football. Through separate bridge datasets for attacking (*n*<sub>train</sub> = 174) and defensive players (*n*<sub>train</sub> = 106), joint multivariate Student-*t* models with LKJ covariance structures, and rigorous held-out validation across two transfer cohorts, we provide calibrated probabilistic predictions with excellent convergence diagnostics and interpretable random-effect decomposition.

The primary contribution is calibrated uncertainty quantification: 90% highest density intervals that achieve near-nominal empirical coverage on attacking metrics and remain useful for defensive metrics with the caveats noted. The framework does not claim uniformly superior point prediction over ML baselines, which is by design: the Bayesian framework's value lies in the full posterior distribution it provides, not in minimising MAE on a small test set.

The La Liga SCA association (credibly positive, 90% HDI entirely above zero) and the pattern of wider creative-metric associations across foreign leagues are the most substantive empirical findings, interpreted with appropriate caution regarding ecological inference and selection effects.

Practical applications include posterior-based scenario analysis, league-specific association factors, and age-conditional adaptation curves enabling transparent uncertainty quantification in recruitment decision-making.

## 10. Future Work

- **Position-specific modelling** — granular positional data (centre back vs. full back, central midfielder vs. winger) would enable position-specific covariance structures.
- **Multi-destination generalisation** — extending beyond the Premier League would test generalisability.
- **Selection bias modelling** — propensity-score weighting or instrumental variable approaches.
- **Temporal dynamics** — modelling year-on-year adaptation trajectories rather than only Year-1 translation.
- **Goalkeeper modelling** — distinct performance metrics and profiles.
- **Prospective validation** — tracking whether model predictions correlate with realised player performance over multiple subsequent seasons.

## References

- Abril-Pla O, Andreani V, Carroll C, et al. (2023). PyMC: A modern and comprehensive probabilistic programming framework in Python. *PeerJ Computer Science* 9: e1516. DOI:10.7717/peerj-cs.1516
- Albert J and Bennett J (2003). *Curve Ball: Baseball, Statistics, and the Role of Chance in the Game.* Copernicus/Springer-Verlag.
- Bingham E, Chen JP, Jankowiak M, et al. (2019). Pyro: Deep universal probabilistic programming. *JMLR* 20(28): 1–6.
- Decroos T, Bransen L, Van Haaren J and Davis J (2019). Actions speak louder than goals: Valuing player actions in soccer. *KDD '19*, pp. 1851–1861. DOI:10.1145/3292500.3330758
- Gelman A, Carlin JB, Stern HS, Dunson DB, Vehtari A and Rubin DB (2013). *Bayesian Data Analysis*, 3rd edn. CRC Press.
- Glazer AK (2026). Nuthin' but a G League: Estimating league translation factors. *Journal of Sports Analytics.* DOI:10.1177/22150218261428808
- Gneiting T and Raftery AE (2007). Strictly proper scoring rules, prediction, and estimation. *JASA* 102(477): 359–378. DOI:10.1198/016214506000001437
- James B (1985). *The Bill James Historical Baseball Abstract.* Villard Books/Random House.
- Kumar R, Carroll C, Hartikainen A and Martin O (2019). ArviZ: A unified library for exploratory analysis of Bayesian models in Python. *JOSS* 4(33): 1143. DOI:10.21105/joss.01143
- Lewandowski D, Kurowicka D and Joe H (2009). Generating random correlation matrices based on vines. *Journal of Multivariate Analysis* 100(9): 1989–2001. DOI:10.1016/j.jmva.2009.04.008
- McHale IG and Szczepański L (2014). A mixed-effects model for identifying the determinants of a player's value in the transfer market. *JRSS-C* 63(4): 543–560. DOI:10.1111/rssa.12015
- Müller O, Simons A and Weinmann M (2021). Beyond crowd judgments: Data-driven estimation of market value in association football. *EJOR* 291(2): 611–624. DOI:10.1016/j.ejor.2019.09.033
- Pappalardo L, Cintia P, Ferragina P, et al. (2019). PlayeRank: Data-driven performance evaluation of soccer players. *Scientific Data* 6: 236. DOI:10.1038/s41597-019-0247-7
- Pavlidis H, Thorn J and Palmer P (2014). Evaluating player performance, optimal rosters, and transfer market efficiencies. *MIT Sloan Sports Analytics Conference.*
- Pedregosa F, Varoquaux G, Gramfort A, et al. (2011). Scikit-learn: Machine learning in Python. *JMLR* 12: 2825–2830.
- Pollard R and Reep C (1997). Measuring the effectiveness of playing strategies at soccer. *The Statistician* 46(4): 541–550. DOI:10.1111/1467-9884.00108
- Reep C and Benjamin B (1968). Skill and chance in ball games. *JRSS* 131(4): 581–585. DOI:10.2307/2343726
- Spearman W (2018). Beyond expected goals: Correcting for selection bias in soccer shooting data. *12th MIT Sloan Sports Analytics Conference.*
- Van Roy M, Robberechts P, Yang W, De Raedt L and Davis J (2020). Valuing the art of pressing in soccer. *AAAI Workshop on AI in Team Sports.*

## Appendix A — Data Sources and Availability

Player-season data derive from publicly available Kaggle datasets (FBref-derived) for the Big Five leagues:

- *Football Players Stats 2024–2025* — Kaggle / Hubert Sidorowicz: <https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025>
- *FBRef 2017–2024 (Top Five Leagues)* — Kaggle / Akshan Krithick: <https://www.kaggle.com/datasets/akshankrithick/fbref-2017-2024-for-europes-top-5-leagues>

Code and supplementary materials: <https://github.com/mohammadarshan/football-league-translation>

## Appendix B — Bridge Dataset Composition

| Bridge | Training Transfers | Test Transfers | Mean Age |
|---|---:|---:|---:|
| ATT+MID | 174 | 45 | 24.0 |
| DEF | 106 | 35 | 24.4 |

*Table 4: Bridge dataset composition.* Training bridges span five season-pairs (2017/18–2021/22). Two held-out test cohorts (2022/23→2023/24 and 2023/24→2024/25) are excluded from training entirely. Both bridges target Premier League destination only.

### B.1 Source League Distribution (training bridge)

| Source League | ATT+MID | Pct | DEF | Pct |
|---|---:|---:|---:|---:|
| Serie A | 16 | 9.2% | 15 | 14.2% |
| Bundesliga | 31 | 17.8% | 13 | 12.3% |
| Ligue 1 | 32 | 18.4% | 25 | 23.6% |
| La Liga | 38 | 21.8% | 18 | 17.0% |
| Premier League | 57 | 32.8% | 35 | 33.0% |
| **Total** | **174** | **100%** | **106** | **100%** |

*Table 5:* Within-league Premier League transfers serve as the domestic baseline reference group, against which foreign league association parameters are estimated.

## Appendix C — Convergence Diagnostics Detail

Trace plots and R̂ distributions for both models confirm well-mixing chains and convergence well below the 1.05 threshold. Zero divergences across both models indicate no Hamiltonian sampler pathologies. Effective sample sizes exceed 1000 for all key parameters including league-level association terms, team random effects, and the LKJ correlation parameters.

## Appendix D — Log-Ratio Distributions

*Figure 7* presents the empirical distributions of log-ratio response variables for the DEF bridge metrics (TklW, Int, Clr, Blocks), separated by source league. The Int distribution shows notably higher variance, consistent with the under-coverage observed for this metric in the held-out test set.

## Statements and Declarations

**Conflicting interests:** The author declared no potential conflicts of interest. **Funding:** This research received no specific grant from any public, commercial, or not-for-profit funding agency. **Acknowledgments:** The author thanks Liu Haedy, Part-time Lecturer, Northeastern University, for helpful feedback on the structure and documentation of this manuscript.
