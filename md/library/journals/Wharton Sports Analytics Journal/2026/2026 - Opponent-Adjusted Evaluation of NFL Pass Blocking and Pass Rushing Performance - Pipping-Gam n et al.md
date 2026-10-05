<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Opponent-Adjusted Evaluation of NFL Pass Blocking and Pass Rushing Performance - Pipping-Gam n et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/opponent-adjusted-evaluation-of-nfl-pass-blocking-and-pass-rushing-performance/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Jonathan Pipping-Gamón; Maximilian Gebauer; Victoria Lee; Kenny Watts; Abraham J. Wyner -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Opponent-Adjusted Evaluation of NFL Pass Blocking and Pass Rushing Performance

Jonathan Pipping-Gamón, Maximilian Gebauer, Victoria Lee, Kenny Watts, Abraham J. Wyner

University of Pennsylvania

## Abstract

Evaluating offensive linemen and pass rushers at the player level is difficult because observable outcomes are sparse, opponent dependent, and strongly shaped by surrounding context. Using 2021 regular-season Hudl tracking data, we construct a blocker–rusher interaction dataset and estimate two ridge-regularized Bradley–Terry paired-comparison models: a binary win/loss model aligned with the 2.5-second pass block win-rate definition and a four-class severity model over loss/win/hit/sack, with both models incorporating a double-team indicator. The final dataset contains 153,138 interactions across 33,283 pass plays in 266 games. On an ordered 80/20 holdout split (ntest = 30,628), both models improve on global baselines and modestly outperform stronger matchup baselines under log-loss evaluation, corresponding to relative log-loss reductions of about 0.24% to 1.21%. Game-level bootstrap resampling indicates that these gains are most stable for the win model and for the severity model relative to the global baseline, while the severity-versus-matchup comparison remains directionally positive but less certain. External comparison to 2021 AP All-Pro selections provides additional face validation on the learned rankings, with the severity model showing the strongest alignment to expert recognition. Overall, ridge-regularized Bradley–Terry models provide an interpretable opponent-adjusted framework for evaluating NFL pass protection and pass rush at the interaction level.

## 1 Introduction

Pass protection and pass rushing are central to modern NFL efficiency and roster construction, yet player-level evaluation in the trenches remains difficult. For rushers, box-score outcomes such as sacks and hits are rare and strongly mediated by context, including quarterback time-to-throw, coverage, and game situation. For blockers, the inverse problem holds: a lineman can execute consistently without generating a direct box-score statistic. Aggregate summaries therefore fail to distinguish individual ability from opponent quality, help structure, and team environment.

Recent work has improved how line play can be operationalized. For example, ESPN’s pass block win rate (PBWR) is a label-based metric defined by whether a blocker sustains a pass block for 2.5 seconds (Burke, 2018). By contrast, STRAIN is a tracking-based measure that summarizes how quickly defenders close space to the quarterback over time (Nguyen et al., 2023). Both approaches capture more signal than sacks alone, but they do not by themselves separate a blocker’s performance from the quality of the opposing pass rush, nor do they produce opponent-adjusted joint ratings for blockers and rushers.

We study offensive and defensive line play within a paired-comparison framework. Each blocker–rusher engagement is treated as a head-to-head contest, and we fit ridge-regularized Bradley–Terry (BT) models (Bradley and Terry, 1952; Friedman et al., 2010; Glickman and Jones, 2025) to estimate relative blocker and rusher ability from those paired outcomes. Operationally, a rusher win is defined when the rusher becomes closer to the quarterback than the blocker within 2.5 seconds, and a double-team indicator records overlapping help when multiple blockers are assigned to the same rusher. This setup is natural for trench play because every interaction has an offensive and defensive participant, while ridge shrinkage stabilizes estimates when exposure is uneven and the matchup graph is incomplete. We estimate separate BT models for the binary 2.5-second win/loss outcome and for a four-class severity outcome, allowing each model to be tailored to its own objective, evaluation, and interpretation.

Contributions. Our main contributions are:

1. An opponent-adjusted paired-comparison framework that evaluates blockers and rushers jointly while preserving role-specific interpretation.

2. Separate ridge-regularized BT models for binary win/loss and four-class outcome severity, with scalar severity summaries derived from the multiclass model.

3. Ordered out-of-sample validation against task-specific baselines, supplemented by gamelevel bootstrap uncertainty for predictive performance.

4. External validation against AP All-Pro selections using AUC and enrichment@K, benchmarked against task-matched raw baselines.

5. End-of-season leaderboards and cumulative path uncertainty summaries for longitudinal interpretation.

The remainder of the paper describes data and outcome construction, presents the modeling framework and validation design, and then reports internal validation, external validation, end-of-season leaderboards, longitudinal uncertainty summaries, and future directions for the framework.

## 2 Data and Outcome Construction

## 2.1 Tracking Data and Interaction Table

We use NFL player-tracking data from the 2021 regular season provided by Hudl. Tracking coordinates are recorded at 10 Hz and are accompanied by event annotations marking blocking engagements, pass attempts, and sacks.

We restrict attention to dropbacks by retaining plays containing either a forward pass event or a quarterback sack event. Within each retained play, we keep offensive linemen, identified pass rushers, and the quarterback. For each frame t, we compute the Euclidean distance between the quarterback and any non-quarterback player: dp,t = (xp,t − xQB,t)2 + (yp,t − yQB,t)2.

Our unit of analysis is a blocker–rusher interaction, defined from the engagement labels in the tracking data. A single play can contribute multiple interactions when several pass-rush engagements occur simultaneously. We generate a binary double-team indicator and set it to 1 when multiple blockers are assigned to the same rusher within overlapping time windows. This indicator enters both BT models as an observed matchup covariate rather than being absorbed into player effects.

After filtering and labeling, the modeling table contains 153,138 blocker–rusher interactions across 33,283 pass plays in 266 games, with 620 rushers and 348 blockers. The double-team rate is 42.7%. This interaction table is the analysis sample for both BT models.

## 2.2 Outcome Definitions

All outcomes are coded from the rusher’s perspective. A rusher win is recorded when, within the labeled engagement window and before 2.5 seconds after the snap, the rusher becomes closer to the quarterback than the blocker. The four outcome labels form a severity hierarchy from the rusher’s perspective: sack is the most severe realized outcome, hit is a less severe contact outcome, win is a pressure win without contact, and loss is the absence of those events. Because the more severe outcomes are downstream realizations of the less severe ones, we assign only the most severe realized label to each interaction rather than doublecounting multiple outcomes on the same rep. We then assign one outcome per interaction using severity priority sack > hit > win > loss, where sack comes directly from event annotations and hit denotes a non-sack quarterback-contact event in the play annotations. If none of these events occurs, the interaction is labeled loss.

We model two targets:

1. Win/Loss target (win_target): indicator of whether the rusher wins within the 2.5second definition.

2. Severity target (severity_outcome): multinomial outcome in {loss, win, hit, sack}.

For scalar summaries of the severity model, we map the four outcome classes to a onedimensional severity scale. This mapping is used only after fitting the multinomial model, for example when computing expected severity scores or weighted coefficient summaries.

The weights are anchored to EPA benchmarks for pass-rush outcomes reported in Eager

(2018). Using the reported EPA benchmarks (no pressure = 0.233, hurry-only = 0.019, hitonly = −0.161, sack = −1.856), we rescale outcomes to the unit interval from the defender perspective using w(o) = EPAno pressure − EPAo . EPAno pressure − EPAsack

This mapping yields w(win) ≈ 0.10 and w(hit) ≈ 0.19, which we round to a one-decimal scale for interpretability: w(loss) = 0, w(win) = 0.10, w(hit) = 0.20, w(sack) = 1.00, so that severity scoring preserves ordering and is directly tied to observed EPA differentials. Observed sample frequencies in the full table are: pˆ(loss) = 0.730, pˆ(win) = 0.253, pˆ(hit) = 0.0109, pˆ(sack) = 0.0063.

## 3 Modeling Framework

We fit separate models because the binary and multiclass targets correspond to different estimands and are evaluated with different loss functions.

## 3.1 Win/Loss Ridge BT

For interaction t, let Dt = 1 if the rusher is double teamed. With rusher i(t) and blocker j(t), the binary BT model is logit P(Yt = 1) = α + ri(t) − bj(t) + δDt, where Yt = 1 indicates a rusher win under the operational 2.5-second definition above. Positive rusher effects therefore indicate stronger pass-rush performance, while positive blocker effects indicate stronger pass protection because blocker coefficients enter with a negative sign.

We estimate parameters via ridge-penalized logistic regression: arg min θ

−ℓ(θ) + λ∥θ∥22

, with λ selected by cross-validation on a log-spaced grid. Ridge regularization shrinks player effects toward zero, which helps stabilize estimates under sparse exposure and incomplete matchup overlap.

## 3.2 Severity Ridge BT

For severity classes c ∈ {loss, win, hit, sack}, we fit a ridge-regularized multinomial BT model:

P(Ct = c) = exp(ηt,c) , c′ exp(ηt,c′ ) ηt,c = αc + ri(t),c − bj(t),c + δcDt.

The fitted likelihood is purely multiclass. After estimation, we convert predicted class probabilities to an expected severity score for scalar summaries using the mapping loss = 0, win = 0.10, hit = 0.20, and sack = 1.00.

## 3.3 Ordered Split and Baselines

We sort interactions by game_id, play_id, and event_game_index, then apply a deterministic 80/20 ordered split (train = 122,510, test = 30,628).

The paper reports two baselines per task: a global baseline that ignores player identity and a matchup baseline that uses player-specific training-set frequencies without fitting a shared latent rating model.

Win baselines. Let Ttrain denote the training interactions and let Yt ∈ {0, 1} be the win outcome for interaction t. The global win baseline is the train-set rusher win rate, pˆglobal

=

|Ttrain|

Yt, t∈Ttrain which is used for every test interaction. For the matchup baseline, let ni(R) be the number of training interactions for rusher i, let nj(B) be the number for blocker j, and define

Y¯i(R)

=

1 n(iR)

Yt, t∈Ttrain:i(t)=i

Y¯j(B)

=

1 n(jB)

Yt, t∈Ttrain:j(t)=j where Y¯i(R) denotes the empirical rusher win rate for rusher i, and Y¯j(B) denotes the empirical rusher win rate allowed by blocker j. Both components are smoothed toward the global rate with prior strength m = 25: p˜(iR)

= ni(R)Y¯i(R) + mpˆglobal n(iR) + m

, p˜j(B)

= nj(B)Y¯j(B) + mpˆglobal n(jB) + m

.

For a test interaction between rusher i and blocker j, the matchup prediction is obtained by averaging on the logit scale:

 logit pˆimjatch = logit−1 p˜(iR)

+ logit p˜j(B) 2

 .

If either player is unseen in training, that component defaults to pˆglobal.

Severity baselines. t, and let

Let Ct ∈ {loss, win, hit, sack} be the severity class for interaction πˆcglobal

=

1 |Ttrain|

1{Ct t∈Ttrain

= c} denote the train-set marginal class probability for class c. This is the global multiclass baseline.

For the matchup baseline, let πˆi(,Rc ) be rusher i’s empirical class frequency in training and let πˆj(,Bc) be blocker j’s empirical allowed class frequency. With prior strength m = 50, we smooth each class profile toward the global class probabilities. We use stronger smoothing for severity than for win (m = 50 versus m = 25) because player-level multiclass frequencies are sparser and noisier than binary win rates: π˜i(,Rc )

= ni(R)πˆi(,Rc ) + mπˆcglobal , n(iR) + m π˜j(,Bc )

= n(jB)πˆj(,Bc ) + mπˆcglobal . nj(B) + m

As a robustness check, we repeat matchup-baseline validation over m ∈ {10, 25, 50, 100} for both tasks. We then combine the two smoothed profiles on the multinomial-logit scale using loss as the reference class. For c ̸= loss, ηi(,Rc )

= log π˜i(,Rc ) , π˜i(,Rlo)ss and the matchup logits are ηj(,Bc )

= log π˜j(,Bc ) , π˜j(,Blo)ss mij,c

= ηi(,Rc )

+ 2 ηj(,Bc ) ,

The resulting baseline class probabilities are mij,loss = 0. πˆimj,actch = exp(mij,c) . c′ exp(mij,c′ )

If either player is unseen in training, that class profile defaults to the global class probabilities.

Importantly, none of these baselines conditions on the double-team indicator. They are intentionally competitive because they use player-specific historical frequencies, but they do not model shared latent ability or explicit help structure.

## 3.4 Uncertainty

We report two complementary uncertainty procedures (Efron and Tibshirani, 1994):

1. End-to-end bootstrap (B = 1000): resample games, refit with fixed λ selected from full-data CV, and recompute validation metrics and player ratings.

2. Weekly path bootstrap (B = 100): for each cumulative week checkpoint, resample past games and refit to obtain path-level uncertainty bands.

## 4 Results

We present internal predictive validation first, then external rank validation, followed by descriptive summaries of end-of-season ratings and weekly uncertainty.

## 4.1 Model Fit and Validation

On the ordered training split used for holdout validation, cross-validated ridge selected λmin = 1.31 × 10−4 for the win model and λmin = 1.17 × 10−4 for the severity model.

Table 1 reports holdout log loss relative to both global and matchup baselines; for the severity task, this is multiclass cross-entropy over the four outcome probabilities. Because the matchup baselines already use player-specific training histories, the absolute gains are necessarily modest. Even so, both BT models improve on the corresponding baselines on the ordered holdout split. These conclusions are stable under baseline prior-strength sensitivity (m ∈ {10, 25, 50, 100}): matchup-baseline improvements remain positive for all tested m in both win (0.0014–0.0019) and severity (0.0015–0.0020) log-loss units (Appendix Table 5). The bootstrap intervals from end-to-end game resampling are entirely positive for both win-model comparisons and for severity versus global class frequencies; for severity versus the stronger matchup baseline, the interval overlaps zero, so that comparison should be interpreted as directional rather than decisive.

Table 1: Ordered holdout log-loss validation.

Task Baseline Model log loss Baseline log loss Improvement 95% CI

Win Global Win Matchup Severity Global Severity Matchup

0.5568 0.5568 0.6319 0.6319

0.5636 0.5582 0.6395 0.6333

0.0068 [0.0047, 0.0093] 0.0014 [0.0005, 0.0024] 0.0077 [0.0049, 0.0106] 0.0015 [-0.0000, 0.0031]

## 4.2 External Validation Against All-Pro Selections

Having established holdout performance, we next ask whether the fitted rankings align with external expert evaluations. We compare BT rankings against 2021 AP All-Pro labels (first team and first+second team) and benchmark each task against its raw baseline. For win/loss, the baseline is empirical win rate (rusher: E[win_target], blocker: E[1 − win_target]). For severity, the baseline is empirical severity EV (rusher: E[severity_target], blocker: E[1 − severity_target]). Because the number of positives is small within each role/accolade slice, we treat this exercise as an external face validation rather than a gold-standard outcome. We report:

1. Rank AUC: probability that a randomly chosen All-Pro player is ranked above a randomly chosen non-All-Pro player. With labels yi ∈ {0, 1}, scores si, n+ = i 1{yi = 1}, and n− = i 1{yi = 0}, we use the Mann–Whitney form

## 1 AUC =

n+n− i:yi=1 j:yj =0

1{si

> sj }

+

1 2

1{si

= sj }

.

2. Enrichment@K: precision@K divided by base rate, where K is the number of All-Pro positives in that role/accolade slice (equivalently, the AP selection-slot count for that slice): precision@K

Enrichment@K =

, n+/n hits@K precision@K =

.

K

Here n is the number of players in the role/accolade slice.

Tables 2 and 3 separate first-team and first+second-team results and place each BT model beside its task-matched raw baseline. The severity model leads AUC in three of four role/accolade slices, while the win/loss model leads rusher AUC for first+second team. Enrichment@K improvements are non-negative in every slice and are largest for the severity model.

Table 2: All-Pro alignment for AP first team.

Task

Role K AUC Base AUC ∆AUC Enrich@K Base Enrich@K ∆Enrich

Win/Loss Blocker 5 0.735 Win/Loss Rusher 7 0.749 Severity Blocker 5 0.854 Severity Rusher 7 0.781

0.712 0.702 0.783 0.751

0.023 0.047 0.071 0.030

0.00 0.00 0.00 25.31

0.00

0.00

0.00

0.00

0.00

0.00

0.00 25.31

Table 3: All-Pro alignment for AP first+second team.

Task

Role K AUC Base AUC ∆AUC Enrich@K Base Enrich@K ∆Enrich

Win/Loss Blocker 10 Win/Loss Rusher 14 Severity Blocker 10 Severity Rusher 14

0.654 0.768 0.877 0.732

0.653 0.718 0.727 0.752

0.002 0.050 0.150 -0.020

3.48 6.33 10.44 12.65

0.00

3.48

0.00

6.33

0.00 10.44

9.49

3.16

## 4.3 Ratings and Leaderboards

After internal and external validation, we refit each model on the full interaction table and summarize the resulting end-of-season ratings. Figure 1 shows BT score distributions by role for both tasks. Figure 2 reports top players by model and role (minimum 200 interactions to reduce small-sample volatility). Scores are interpreted within each model (win versus severity) rather than across models, because the two targets induce different scales. They should also be interpreted as interaction-level efficiency conditional on observed pass-rush engagements, not as an all-snap measure of overall player value. The win/loss and severity leaderboards are directionally similar for elite rushers but differ more noticeably for blockers, which is consistent with the severity model’s heavier emphasis on high-impact outcomes.

## 4.4 Weekly Path Uncertainty

The weekly path bootstrap adds a longitudinal view to the end-of-season summaries. The regular-season dataset yields 18 cumulative weekly checkpoints for each player-model-role series. Figure 3 shows weekly trajectories for the top three players in each model-role panel,

Figure 1: Distribution of BT scores by model and role. Higher scores indicate stronger performance within role.

Figure 2: Top 10 players by BT score in each model-role panel (minimum 200 interactions). Higher scores indicate stronger performance within role. Points are estimates and horizontal bands are central 50% bootstrap intervals (25th–75th percentiles).

Table 4: Top five players by model and role (minimum 200 interactions).

## Model Role Player

Rating

Win/Loss Win/Loss Win/Loss Win/Loss Win/Loss

Rusher Rusher Rusher Rusher Rusher

Adam Gotsis Josh Allen Patrick Queen Taven Bryan Aaron Donald

0.510 0.509 0.477 0.475 0.469

Win/Loss Win/Loss Win/Loss Win/Loss Win/Loss

Blocker Blocker Blocker Blocker Blocker

Erik McCoy Calvin Throckmorton Trey Hopkins Chase Roullier Ben Cleveland

0.683 0.635 0.598 0.527 0.440

Severity Severity Severity Severity Severity

Rusher Rusher Rusher Rusher Rusher

Robert Quinn T.J. Watt Myles Garrett Nick Bosa Jaelan Phillips

0.543 0.531 0.493 0.430 0.429

Severity Severity Severity Severity Severity

Blocker Blocker Blocker Blocker Blocker

Joe Thuney Corey Linsley Tytus Howard Dion Dawkins Halapoulivaati Vaitai

0.258 0.255 0.250 0.215 0.207 using the same minimum interaction threshold (n ≥ 200) applied in the leaderboard visualizations. These paths are descriptive rather than predictive, and early-week intervals are widest when cumulative exposure is still limited.

Figure 3: Weekly cumulative BT score paths with bootstrap uncertainty ribbons (mean ± 1.96 SD) for the top three players in each model-role panel (minimum 200 interactions).

## 5 Discussion

## 5.1 Interpretation

The main empirical signal is not a dramatic predictive jump, but a consistent one. In a noisy interaction-level problem, modest log-loss improvements over already competitive baselines are still meaningful, especially when accompanied by interpretable opponent-adjusted ratings. External validation is especially encouraging for the severity model, whose rankings place 2021 All-Pro selections closer to the top than the simpler win-rate benchmark. Taken together, these results suggest that modeling richer pass-rush outcomes can improve separation among elite players while preserving a transparent blocker–rusher comparison structure. In turn, opponent-adjusted ratings of this kind can inform team-facing scouting and personnel evaluation, especially when interpreted alongside richer contextual information.

## 5.2 Limitations and Future Work

Several limitations suggest natural extensions. First, the win label is based on a distanceto-quarterback rule and may not fully capture functional pressure quality. More realistic labels could incorporate pocket geometry, rush lane, and quarterback decision constraints. Second, the scalar severity mapping is only one plausible calibration of football value. The multinomial fit itself does not depend on that mapping, but scalar summaries and weighted leaderboards do. Third, help mechanisms (chip blocks, tight-end/running-back assistance, and protection-slide structure) are only partially captured by a coarse double-team indicator. Fourth, sacks and pressure proxies are influenced by quarterback time-to-throw and play design, which are only indirectly represented. Finally, although BT adjusts for opponent strength, it does not explicitly model teammate effects, role specialization, or position-family hierarchy; hierarchical shrinkage and multi-season pooling are natural next steps.

## 5.3 Conclusion

Ridge-regularized BT models provide a stable and interpretable framework for NFL pass-rush and pass-protection evaluation. In this 2021 regular-season study, the models outperform naïve baselines on both binary win/loss and outcome-severity tasks, while the severity formulation shows the strongest external alignment with All-Pro selections. The approach does not remove the need for richer football context, but it does provide a transparent statistical foundation for future tracking-based work on offensive and defensive line evaluation.

Reproducibility

Code used for data processing, model fitting, validation, and figure/table generation is available at https://github.com/WhartonSABI/nfl-elo.

## Acknowledgements

We gratefully acknowledge the support of the Wharton Sports Analytics and Business Initiative. We also thank Hudl for providing access to the 2021 NFL tracking dataset used in this study and Dr. Paul Sabin for early conversations that helped spark and shape the project.

## References

Bradley, R. A. and Terry, M. E. (1952). Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika, 39(3/4):324–345.

Burke, B. (2018). We created better pass-rusher and pass-blocker stats: How they work. ESPN Analytics. Explainer article on pass-rush and pass-block win rate metrics.

Eager, E. (2018). Just how important are sacks for a defense? Pro Football Focus. Published February 22, 2018.

Efron, B. and Tibshirani, R. J. (1994). An Introduction to the Bootstrap. Chapman & Hall/CRC, New York.

Friedman, J., Hastie, T., and Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. Journal of Statistical Software, 33(1):1–22.

Glickman, M. E. and Jones, A. C. (2025). Models and rating systems for head-to-head competition. Annual Review of Statistics and Its Application, 12:1–31.

Nguyen, Q., Yurko, R., and Matthews, G. J. (2023). Here comes the STRAIN: Analyzing defensive pass rush in american football with player tracking data. The American Statistician, 77(4):353–370.

## Appendix

A Baseline Prior-Strength Sensitivity

Table 5: Matchup-baseline prior-strength sensitivity on the ordered holdout split.

Task m Model log loss Baseline log loss Improvement

Win

Win

Win

Win 100

Severity 10

Severity 25

Severity 50

Severity 100

0.5568 0.5568 0.5568 0.5568 0.6319 0.6319 0.6319 0.6319

0.5582 0.5582 0.5584 0.5587 0.6339 0.6334 0.6333 0.6336

0.0014 0.0014 0.0016 0.0019 0.0020 0.0016 0.0015 0.0017
