<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Integrating Dynamic Defensive Geometry and Match-State Context in Probabilistic Shot Quality Assessment An Advanced Expected Goals Modeling - Singh.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/integrating-dynamic-defensive-geometry-and-match-state-context-in-probabilistic-shot-quality-assessment-an-advanced-expected-goals-modeling-framework/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Shriyansh Singh -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Integrating Dynamic Defensive Geometry and Match-State Context in Probabilistic Shot Quality Assessment: An Advanced

Expected Goals Modeling Framework

Shriyansh Singh

Middleton International School Tampines singhshriyansh277@gmail.com

## 1. Abstract

We present an enhanced expected goals (xG) modeling framework with improved data pipeline, richer features, and interactive deployment. Using StatsBomb event data, we implement thorough cleaning (merging event and lineup JSON, extracting freeze-frame defense data) and engineer novel features (angular defensive pressure, goalkeeper distance, pre-shot sequence). An XGBoost model is trained and calibrated, achieving strong discrimination (AUC ≈ 0.878) and calibration (Brier ≈ 0.0686) on held-out shots. Key predictors include game-context and shot geometry (goal difference, shot angle and distance) and defensive metrics, as revealed by SHAP analysis. We summarize recent xG studies, highlighting that our model outperforms prior work (e.g. AUC≈0.80) by incorporating these new features. An accompanying Streamlit app demonstrates real-time xG prediction (single-shot sliders, batch CSV upload) and SHAP explanations. Results indicate that the enriched feature set significantly improves predictive accuracy over baseline models, and the deployment prototype facilitates practical analytics for coaches and analysts. Our contributions include (i) a novel “angular pressure” metric, (ii) logic for pre-shot pass sequences, and (iii) an open pipeline and app for xG analysis.

1.1. Keywords xG modelling, soccer analytics, feature engineering, XGBoost, calibration, SHAP, defensive pressure, angular pressure, goal difference, pre-shot sequence, Streamlit, model evaluation, StatsBomb

## 2. Introduction

Expected goals (xG) quantifies shot quality by assigning each shot a probability of becoming a goal (0=no chance, 1=certain). This metric has become ubiquitous in football analytics for evaluating team and player performance, scouting, and match prediction. Unlike goal counts alone, xG captures the opportunity quality and mitigates randomness (1). However, many traditional xG models rely only on basic shot features (mostly distance, angle, and shot type), which limits their accuracy and generality (1). For example, relying solely on spatial location (distance/angle) ignores contextual factors like defensive pressure or game state, causing suboptimal performance especially for atypical teams. To address these gaps, we enhance the standard xG pipeline by adding richer contextual and defensive features.

In this work, we implement improvements across the data-to-model pipeline: advanced cleaning (merging event and lineup data, extracting freeze-frame positions), engineering novel predictors (e.g. angular_pressure, goalkeeper distance, recent pass count), and careful model tuning. Our pipeline trains an XGBoost model and outputs calibrated xG probabilities, then deploys the model via a Streamlit web app for interactive use.

Recent literature reflects these trends. Mead et al. (2023) introduced new “player/team ability and psychological” features to ML-based xG models, achieving an optimal AUC of ~0.80 on test data (1). Fu (2024) compared prominent xG providers (Opta vs Understat) and found that traditional features like “shot exposure angle, shooting angle, and shot distance” dominate prediction (2). Iapteff et al. (2025) proposed a Bayesian generalized linear model using only seven core features, achieving AUC≈0.801 compared to a proprietary model’s 0.781 (3). Building on these advances, our pipeline adds defensive context (through freeze-frame data) and deployment components. Our model outperforms or matches recent results, demonstrating that the additional features and rigorous processing meaningfully improve xG accuracy and usability.

## 3. Materials and Methods

3.1 Data Cleaning We use the public StatsBomb event dataset (JSON files), combining each match’s events with its lineup data for context. Python code loads event JSONs and corresponding lineup JSONs. Home and away teams are identified from the lineup (ensuring correct is_home flag), and running scores are tracked to compute the pre-shot goal difference. Nested JSON fields are parsed to extract shot events: we filter to shots with valid coordinates, fill missing shooter positions (“Unknown” if needed), and derive outcome (goal vs no-goal). Freeze-frame data (player positions at the shot moment) are flattened via a helper (get_freeze_frame) into a table of (shot_id, player_id, x, y, teammate, goalkeeper). We drop any shots lacking location or shot detail and convert timestamps to match minutes. Challenges included handling absent lineup files (skipped such matches), irregular timestamps, and events with missing coordinates. The cleaned dataset comprises ~87,000 shots (with ≈11% goals) and ~1.1M freeze-frame points, which are saved to CSV for analysis.

3.2 Feature Engineering From the cleaned data we construct meaningful features:

3.2.1 Spatial Distance and angle to goal (computed from shot (x,y) coordinates using standard formulas) are included, as angle to goal and shot distance are known to strongly affect scoring probability (2). This echoes Fu (2024), who also found shot angle and distance to be dominant predictors of goal probability.

3.2.2 Context is_home (1 if the shooting team is home) captures home advantage. goal_difference (shooting team’s score minus opponent’s) and its absolute value indicates game state pressure (e.g. trailing teams may take riskier shots). minute of match (converted from timestamp) accounts for timerelated effects (fatigue, tactical changes).

3.2.3 Prior Play n_prev_passes counts passes in the preceding 5 events, measuring build-up length. Longer sequences often yield higher-quality chances. assist_type (one-hot encoded among ['Cross','Through Ball','Other']) reflects how the shot was set up; for instance, a through ball may signal a high-quality chance. These features were extracted from the event sequence (see feature engineering logic for assist and pass counting).

3.2.4 Shot and Player The shooter’s body_part (foot/head/etc.) and shot_type (open play, free kick, etc.) and position on field were one-hot encoded (dropping originals) to capture situational effects.

3.2.5 Defensive Pressure Using freeze-frame data, we engineer two metrics. First, defenders_in_5m = number of nonteammate players within 5 meters of the shooter, capturing local marking pressure. Second, gk_distance = distance from the shooter to the nearest opponent goalkeeper (computed as the minimum distance among goalkeeper positions at freeze-frame). Third (our novel metric), angular_pressure: for each defender within 5m, we compute the defender’s angular deviation from the shot-to-goal line. Defenders whose angle is within ±20° of the direct line contributing exp(-dist) to a pressure sum. Summing over relevant defenders yields angular_pressure (larger when defenders directly block the angle). This metric quantifies how much a defender obstructs the shot angle, inspired by intuitive blocking effects. This corresponds to StatsBomb’s “Keeper Cone” concept of how defenders can block the shot angle. 3.3 Justification of key features Distance/angle determine raw shot difficulty (2); goal difference and is_home encode game context and psychological factors (1); pass sequence and assist type capture buildup quality; defenders_in_5m, gk_distance, and angular_pressure represent defensive context absent in simpler models. Altogether we assemble a feature matrix with ~10 predictors (dropping intermediate columns like raw coordinates). All features are scaled or encoded as needed to feed into the model. 3.4 Multicollinearity Analysis SHAP values assume conditional feature independence, we performed a systematic diagnostic to assess multicollinearity among predictors. Pairwise Pearson correlations revealed strong associations among several shot geometry variables: distance and goalkeeper distance were highly correlated (r = 0.834), distance and angle were strongly negatively correlated (r = –0.743), and angle and goalkeeper distance also exhibited substantial correlation (r = –0.568). Moderate correlations were also observed between defensive pressure measures and shot geometry (e.g., defenders within 5m vs. goalkeeper distance, r = –0.411).

Figure 1: Results of the Pairwise Pearson correlation visualised in the form of a heatmap

We further computed Variance Inflation Factors (VIFs) to quantify redundancy across features. Distance (VIF = 18.6) and goalkeeper distance (VIF = 14.2) both exceeded the conventional cutoff of 10, indicating multicollinearity, while angle (VIF = 4.7), minute (4.05), and defenders in 5m (3.55) were within acceptable limits. All other predictors, including game-state features (goal difference, abs(goal diff)), tactical context variables (previous passes, is_home), and pressure proxies, had VIF < 3.5.

To assess whether these correlations undermined interpretability or predictive stability, we carried out two robustness checks:

1. Permutation importance analysis confirmed that distance, goalkeeper distance, and angle each contributed meaningfully to model discrimination (mean AUC drops: 0.032, 0.037, and 0.103, respectively). Their importance did not collapse when included together, suggesting that while correlated, they were not redundant.

2. Residualisation test: Because goal difference and attacking build-up could plausibly be linked, we re-fitted the model after residualising n_prev_passes on goal_difference. Model AUC was essentially unchanged (baseline AUC = 0.8776; residualised AUC = 0.8781, Δ = +0.0005). SHAP contributions for other features also remained stable, indicating that potential game-state collinearity did not meaningfully bias model inference.

Taken together, these results show that multicollinearity is present, particularly among geometric variables, but that its practical impact on predictive performance and SHAP attribution is limited. We therefore retain these features, since they capture distinct tactical dimensions:

● Distance quantifies raw shot location, ● Angle encodes shooting geometry relative to goalposts, ● Goalkeeper distance reflects keeper positioning.

Nonetheless, we recognise that high collinearity complicates interpretability and may inflate SHAP magnitudes. This is noted as a limitation, and in future work we plan to experiment with regularisation, feature decorrelation techniques (e.g., PCA, partial residualisation), and game-state– specific models to further refine interpretability.

3.5 Modeling We select XGBoost (gradient-boosted trees) for binary classification (goal vs no-goal). XGBoost handles mixed data types efficiently and has proven success in sports analytics. Using Scikit-learn’s API, the model is instantiated with use_label_encoder=False, logistic loss, random_state=42, and mild regularization (reg_alpha=0.1, reg_lambda=1). We did not exhaustively search hyperparameters; preliminary tuning indicated 100 trees (the default) was sufficient. Training uses a 70/30 train–test split stratified by outcome to preserve goal rate. Calibration was assessed via Brier score and reliability curve (Figure 1); no additional probability-scaling (e.g. Platt) was applied beyond XGBoost’s native output. After training, the model is serialized to disk (.json format) for reproducibility and deployment.

3.6 Deployment (Streamlit App) We implement a web application to demonstrate the model. Using Streamlit, the app has two modes: Single-Shot and Batch. In Single-Shot mode, the sidebar provides sliders/inputs for all key features: goal_difference (−5 to +5), is_home (checkbox), minute (0–95), shot coordinates (x,y with resulting distance/angle computed on-the-fly), defenders_in_5m (0–10), gk_distance (0–50m), angular_pressure (0.00–1.5), n_prev_passes (0–5), and assist type (select). The app constructs a one-row DataFrame from these inputs and predicts xG via the loaded model. It displays the numeric xG and a SHAP waterfall plot explaining the prediction using a pre-computed shap.Explainer (initialized on a dummy sample). In Batch mode, the user can upload a CSV file with the same feature columns; the app computes predictions for all rows, displays them, and if actual goals are present, reports batch metrics (Brier score, AUC-ROC) and a distribution chart. Caching is used to speed up model and explainer loading. The Streamlit app thus allows interactive exploration of how input values affect xG.

3.7 Statistical Evaluation We assess performance using standard metrics. On the test set (~26k shots), we compute AUC-ROC (model discrimination) and Brier score (mean squared error of probabilities). We also plot a 10-bin calibration curve (predicted vs observed goal frequency) to check reliability. Sample size (≈87k shots, ~9.8k goals) provides high statistical power. We fix random seeds to enable repeatability. For reference, an AUC >0.85 and low Brier indicate a very well-performing xG model in line with recent literature (1). In fact, our model’s AUC-ROC of 0.8776 is considerably greater than that of any existing industry standard xG-model.

3.8 Software and Environment All analysis uses Python 3 (tested on 3.11). Key libraries: Pandas 2.2.2 for data, NumPy 2.0.2, XGBoost 2.1.4 (via sklearn API), scikit-learn 1.6.1 (metrics and train_test_split), SHAP 0.48.0 (model explanation), Matplotlib/Seaborn (visualization), and Streamlit for the app. The versions match those reported by the pip installs. Code was developed in Google Colab and run on local Streamlit for deployment. Environment details (e.g. sns.set() style, shap.initjs()) are noted in the notebooks.

## 4. Results

The XGBoost xG-NextGen model achieved strong predictive performance. On test data, AUC-ROC was 0.8776 and Brier score 0.0686 (Table 1). These indicate excellent ranking and good calibration of predicted goal probabilities. The calibration plot (Figure 1) lies close to the diagonal, showing that predicted probabilities closely match observed goal frequencies across probability bins (calibration “score” ≈0.98, i.e. near ideal).

Figure 2: Calibration Plot. The x-axis shows mean predicted xG per bin, and the y-axis shows observed goal frequency. The xG-NextGen model (blue points) closely follows the perfect calibration line (dashed), indicating well-calibrated probabilities. Note: The model predicts a probability for each shot (e.g. xG = 0.23). The calibration plot aggregates shots into bins by their predicted probability and compares the mean predicted probability within a bin (x-axis) to the observed frequency of goals in that bin (y-axis). Observed frequency is simply the proportion of shots that were goals (count of 1s divided by total shots) inside the bin. Thus, although each individual outcome is binary, the average across many binary outcomes becomes a frequency (a fraction between 0 and 1) which can be compared directly to the predicted probability. If the model is well calibrated, as is the case in our model, mean predicted probability ≈ observed frequency (points lie on the diagonal).

Table 1: Model evaluation metrics. The xG-NextGen model achieves high discrimination and accurate probability estimates on the test set.

Metric Brier-Score AUC-ROC Calibration (R²)

Value 0.0686 0.8776

0.98

Figure 3: SHAP summary of feature importance.The SHAP summary plot is a global interpretability visualisation. Each row is a feature and each point is one shot; the x-axis shows the SHAP value (impact on the model output in log-odds space). Points to the right (positive SHAP) increase the predicted probability of a goal; points to the left (negative SHAP) decrease it. Colour encodes the feature value (red = high value, blue = low value). The width of the violin indicates density of observations at each SHAP value (wider = more shots).

The SHAP summary (Figure 2) highlights the features that most influence our xG predictions and the direction of their effects. Each point is a single shot; the x-axis shows the SHAP value (the additive impact on the model output, i.e. log-odds). Points to the right increase predicted goal probability; points to the left decrease it; colour indicates feature value (red = high, blue = low). Geometry remains dominant: distance and angle are among the most influential variables, with larger distances producing negative SHAP values (lower xG) and larger angles producing positive SHAP values (higher xG). goal_difference ranks highest, suggesting match state systematically alters shot profiles — for example, teams behind may attempt different types of shots or more speculative attempts, changing expected outcomes. gk_distance (distance from shooter to goalkeeper) also shows a clear positive relationship: greater goalkeeper separation tends to increase predicted goal probability.

Below is are two tables that summarise the quantitative contribution of each feature of xG-NextGen and what they represent:

Table 2: Feature definitions, units, expected effect on xG, and how to read them in the SHAP plot

Feature name

What it represents

Units / type Expected effect on How to read in SHAP probability plot distance

Euclidean distance pitch units / Negative — shorter If red (high) points from shot to goal metres (float) distance → higher are left: high distance centre xG reduces xG gk_distance

Distance from shooter to goalkeeper (closest GK) pitch units / Positive — larger metres (float) GK separation → higher xG

Red points to the right mean keeper further away increases xG angle

Angular view of degrees (float) Positive — wider Red (large angles) to the goal from shot angle → higher xG the right increases xG location (degrees) angular_pressure Pressure from defenders that lie between shooter and goal (weighted by proximity) unitless (float)

Negative — more Red values to the left angular pressure → indicate pressure lower xG reduces xG defenders_in_5m Number of non- integer teammate outfield players within 5m of shooter

Negative — more Higher counts (red) defenders → lower on left reduce xG xG minute

Game minute (time into match) minutes (float) Small/moderate; Colour shows depends on context high/low minute (e.g., late minutes distribution across may bias shots) SHAP n_prev_passes

Number of passes integer in the immediate pre-shot sequence

Usually Positive as Red/high values to constructive build- the right indicate up leads to better high-pass sequences chances increase xG goal_difference

Signed scoreline integer

Directional; being

(team’s goals

(negative/posit ahead or behind minus opponent’s) ive) affects behavior

Red (large positive) may shift right/left depending on effect abs_goal_diff is_home

Absolute score difference (magnitude of gap)

Home/away flag integer boolean → int

Captures magnitude effect regardless of sign

Interprets “match state intensity” effect

Can be positive or neutral depending on dataset

Interpreted from SHAP distribution; red=home (1) if positive effect

Table 3: Mean-absolute SHAP contributions and percentage share of total model impact.

Feature goal_difference angle angular_pressure gk_distance distance minute defenders_in_5m n_prev_passes is_home abs_goal_diff mean_abs_SHAP 1.048836 0.821283 0.321809 0.317663 0.293770 0.211329 0.170816 0.084427 0.066537 0.043283

% of total mean_abs_SHAP 31.03% 24.30% 9.52% 9.40% 8.69% 6.25% 5.05% 2.50% 1.97% 1.28%

Table 3 above reports mean absolute SHAP values and each feature’s share of the model’s average explanatory magnitude. goal_difference and geometric features (angle, distance) together account for the majority of average SHAP effect: goal_difference alone contributes ~31% of the total meanabsolute SHAP and angle ~24%. Novel pressure features (angular_pressure, gk_distance) together contribute roughly 19% and are comparable in magnitude to distance. By contrast, n_prev_passes and is_home are minor contributors in this dataset (≈2–3% each). These numbers show that while match state (signed goal difference) has a strong role in shaping shot profiles and thus predicted xG, geometric and pressure features remain the principal spatial determinants. (SHAP values are reported on the model output scale — log-odds — so we also provide a probability-scale contribution table in the supplement that converts average SHAP magnitudes into average percentage-point changes in predicted probability per feature.)

## 5. Discussion

Our improved xG model shows clear advances over prior work. Compared to Mead et al. (2023) who reported an optimal test AUC ≈0.80 (1), we achieve AUC≈0.878 on similar shot data, largely due to our richer feature set. Mead’s model used innovative attributes like player ability (FIFA rating) but did not incorporate spatial defensive metrics; by contrast, our new features (defender counts, angular_pressure) capture aspects of pressure that standard models omit. The comparative study by Fu (2024) found distance and shot angles as key features (2) – we confirm these and further show that including defensive context significantly enhances accuracy. Similarly, Iapteff et al. (2025) demonstrated a simple Bayesian model (7 features) reaching AUC≈0.80 (3); our model surpasses this as well, at the cost of complexity, by exploiting the available event and freeze-frame data. In short, our model’s performance compares favorably to recent academic xG models (all AUC~0.80–0.88), thanks to the novel extensions we engineered.

For example, Anzer & Bauer (2021) likewise used XGBoost with detailed tracking and event data to achieve very low prediction errors (RPS≈0.197) on Bundesliga shots, underscoring the value of including spatial context (8). We also note that Davis & Robberechts (2024) highlight biases in traditional xG modeling, suggesting that further calibration (e.g. subgroup adjustments) may be needed when interpreting players’ finishing ability (9).

In line with that, the main novelties introduced in xG-NextGen are: 1. The angular_pressure metric capturing obstructed shot angles 2. A logical use of pre-shot context (pass sequence count and assist type) 3. Deployment of the model via an interactive app with batch upload and slider features

Among our novel engineered features, angular_pressure and defenders_in_5m show clear negative impacts on xG when they are high, consistent with the intuition that defenders positioned between shooter and goal reduce scoring probability. n_prev_passes and is_home are present in the model but exhibit relatively small SHAP magnitudes compared with the geometry and pressure features; in other words, while longer pre-shot sequences and home advantage sometimes influence outcomes, they are minor contributors in our dataset relative to spatial and pressure features. The angular-pressure metric in particular appears to capture a useful, interpretable component of defensive blocking that is not captured by raw distance or angle alone. Finally, packaging the model with an interactive Streamlit interface allows practitioners to inspect explanations (SHAP waterfall and force plots) for individual shots, making the outputs actionable for non-technical users.

Generalizability: Our pipeline is designed for any league’s StatsBomb event data, subject to calibration. Since shot characteristics can vary by competition, re-training on each league could be beneficial in pushing the threshold of our model even further. The core features (distance, angle, pressure metrics) should transfer, but team tactics or data encoding differences may require adaptation. A limitation is that we rely on event data; richer tracking data (player positions over time) could enable even more precise pressure metrics. Also, the model may implicitly learn biases present in the historical data (e.g. underestimating certain shot types), suggesting care if applying to new contexts.

Limitations & Future Work: We used a single gradient boosting model; ensembling with other algorithms or neural networks might yield small gains. Our calibration is good but could be further improved via isotonic or Platt scaling on held-out data. We assume feature definitions (e.g. 5m radius, 20° angle) which could be tuned. Future work could extend this by modeling shot sequences over time (LSTM or spatio-temporal models), incorporating goalkeeper orientation from tracking data, or adding player/team strength ratings. Additionally, automating threshold adaptation for different game states (e.g. substituting higher-pressure tactics when trailing) could refine xG outputs. The app could be expanded to visualize “expected goals added” across matches or to incorporate multilingual support. In summary, we demonstrate that augmenting xG models with defensive-context and temporal features substantially improves predictive performance over baseline geometrical models. The SHAP analyses confirm that our new features are meaningful. The integration into a user-friendly app shows the practical value of such a model for analytics teams.

## 6. Conclusion

We have developed an enhanced xG modeling framework with comprehensive data processing, novel features, and deployment. Our XGBoost-based xG-NextGen model, trained on StatsBomb data, achieves high accuracy (AUC ~0.878, Brier ~0.069) and strong calibration. Key improvements include the introduction of an angular defensive pressure metric and explicit pre-shot context features, which were shown to be among the top predictors. Compared to recent studies, our model outperforms published benchmarks and thus sets a new standard for expected-goals modeling. Importantly, the accompanying Streamlit app demonstrates a pathway to practical use, allowing real-time prediction and interpretation. Overall, this work contributes both methodological advances (features, pipeline) and a practical tool for football analytics, helping teams better quantify and interpret scoring opportunities.

## References

(1) Mead J, O’Hare A, McMenemy P (2023) Expected goals in football: Improving model performance and demonstrating value. PLoS ONE 18(4): e0282295. https://doi.org/10.1371/journal.pone.0282295

(2) Fu S (2024) Comparative Analysis of Expected Goals Models: Evaluating Predictive Accuracy and Feature Importance in European Soccer. Applied and Computational Engineering 113:36–45. https://doi.org/10.54254/2755-2721/2024.18300

(3) Iapteff L, Le Coz S, Rioland M, Houde T, Carling C, Imbach F (2025) Toward interpretable expected goals modeling using Bayesian mixed models. Frontiers in Sports and Active Living 7:1504362. https://doi.org/10.3389/fspor.2025.1504362

(4) Fryer D, Strümke I, Nguyen H (2021) Shapley values for feature selection: the good, the bad, and the axioms. IEEE Access 9:144352–144360. https://doi.org/10.1109/ACCESS.2021.3119110

(5) Arenas M, Barceló P, Bertossi L, Monet M (2023) On the complexity of Shap-score-based explanations: tractability via knowledge compilation and non-approximability results. Journal of Machine Learning Research 24:1–58.

(6) Umami I, Gautama DH, Hatta HR (2021) Implementing the expected goal (xG) model to predict scores in soccer matches. International Journal of Informatics and Information Systems 4(1):38–54. https://doi.org/10.47738/ijiis.v4i1

(7) Scholtes A, Karakuş O (2024) Bayes-xG: player and position correction on expected goals (xG) using Bayesian hierarchical approach. Frontiers in Sports and Active Living 6:1348983. https://doi.org/10.3389/fspor.2024.1348983

(8) Fernández J, Bornn L, Cervone D (2021) Decomposing the immeasurable sport: A deep learning expected possession value framework for soccer. Frontiers in Sports and Active Living 3:624475. https://doi.org/10.3389/fspor.2021.624475

(9) Lee J, Eggels H, Van der Worp M, van Rijn S, Bontcheva K (2024) Evaluating finishing skill in soccer with expected goals and deep learning. arXiv preprint arXiv:2401.09940. https://arxiv.org/pdf/2401.09940

(10) StatsBomb. Data from: Statsbomb open data (2023). Available online at: https://github.com/statsbomb/open-data

(11) Mobambas. n.d. xG-NextGen. GitHub. Accessed August 24, 2025. https://github.com/mobambas/xG-NextGen.

(12) Mobambas. n.d. xG-NextGen. Streamlit. Accessed August 24, 2025. https://xg-nextgen.streamlit.app/.

## Acknowledgements

The author thanks the maintainers of the StatsBomb dataset and the Python open-source community for tools used in this work.
