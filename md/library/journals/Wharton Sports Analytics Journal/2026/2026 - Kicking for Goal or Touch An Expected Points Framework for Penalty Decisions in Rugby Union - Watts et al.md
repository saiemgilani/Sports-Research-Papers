<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Kicking for Goal or Touch An Expected Points Framework for Penalty Decisions in Rugby Union - Watts et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/kicking-for-goal-or-touch/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Kenny Watts; Jonathan Pipping-Gamón -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Kicking for Goal or Touch? An Expected Points Framework for Penalty Decisions in Rugby Union

Kenny Watts and Jonathan Pipping-Gamón

The Wharton School, University of Pennsylvania

April 10, 2026

## Abstract

Following a penalty in rugby union, teams typically choose between attempting a kick at goal or kicking to touch to pursue a try. We develop an Expected Points (EP) framework that quantifies the value of each option as a function of field location and game context. Using phase-level data and observed penalty kicks, we construct two context-aware surfaces: (i) the expected points of a possession beginning with a lineout and (ii) the expected points of attempting a kick at goal. Comparing these surfaces yields decision maps that identify where kicking for goal or kicking to touch maximizes expected points, and how the boundary shifts with game context and expected meters gained to touch. To our knowledge, this is the first comprehensive EP-based assessment of penalty strategy in rugby union; it also provides a foundation for future refinement with richer event data and extension to win-probability analysis.

## 1 Introduction

Rugby union presents a recurring strategic decision immediately after a penalty. Teams can either attempt an immediate three-point kick at goal or pursue a potential seven-point try via a scrum, a tap-and-go (both from the mark), or a kick to touch followed by a lineout. Except when very close to the opposition try line, teams generally prefer the lineout option to a tap-and-go or scrum because the kick to touch can safely gain territory before the restart. As a result, once a side is within realistic penalty-kick range (roughly 65 m from the opposition try line), the practical decision is usually between kicking at goal or kicking to touch.

While the choice is often straightforward near the opposition corner, for a given scoreline, or late in a match, many game states are ambiguous and governed by convention, perceived kicker ability, and the expected quality of a team’s lineout. In contrast, American football has long relied on Expected Points (EP), Expected Points Added (EPA), and win-probability (WP) frameworks to guide the analogous fourth-down decision, translating field position and context into expected returns and actionable recommendations (Romer, 2006; Burke, 2009; Yurko et al., 2019). In that setting, WP and EP estimators are typically built using statistical machine learning models (e.g., random forests and gradient boosting), as in Lock and Nettleton (2014) and Baldwin (2021).

In rugby union, quantitative decision analysis has progressed more slowly, largely because detailed public data is limited. Martinez-Arastey et al. (2025) present a transparent phase-level Expected Points framework for the English Premiership and show the difficulty of predicting low-frequency outcomes such as penalty kicks. Separately, public analyses of goal-kicking estimate make probability from distance and angle, yielding useful but largely context-free benchmarks (Monpezat, 2023). Building on both strands—and on related decision-modeling work in American football—we evaluate the penalty decision directly.

This paper develops a decision-ready EP framework for the penalty decision. We estimate two context-aware surfaces: (i) expected points for possessions that begin with a lineout and (ii) expected points for penalty kicks at goal. The kick surface combines a continuous angle– distance make model with the continuation value of misses (e.g., 22 m drop-outs and in-play recoveries), rather than assigning misses zero value. Comparing these surfaces yields decision maps (zero-difference contours) that identify where each option maximizes expected return, and sensitivity analyses show how the frontier shifts with team quality, yellow/red cards, and expected meters gained to touch. The framework also makes explicit the translation from penalty location to resulting lineout location, along with the assumptions required when combining Premiership phase data with kicking data from Super Rugby, NPC (New Zealand Provincial Competition), and international matches.

## 2 Data

## 2.1 Phase-Level Data

Our primary dataset consists of phase-level event logs from the 2018/19 Premiership Rugby season compiled by Martinez-Arastey et al. (2025), covering 132 matches and 35,199 phases of play. Each record describes the on-field state at the start of a phase: the initiating event type, a zonal field location and side, the current score differential, and the next score in points for or against the team in possession. We harmonize timestamps to “seconds remaining in match” so that time is strictly decreasing within a game and directly comparable across halves.

The unit of observation in the dataset is a phase, defined as the period between successive rucks. The phase count resets following restarts (e.g., lineouts, scrums, kick-offs) or major infringements that halt play. A possession sequence is an ordered set of phases by the same team without an opposition touch that changes possession. Unless otherwise stated, Expected Points estimates condition on the first phase of a possession sequence (e.g., a lineout), because that is the decision-relevant entry state. Figure 1 summarizes the zonal discretization of the pitch used in the phase-level data.

Figure 1: Field zones used in the phase-level dataset.

## 2.2 Phase-Level Data Processing

For the EP model, the unit of analysis is a possession that begins with a lineout. We therefore restrict the dataset to opening phases of play (i.e., observations with Phase = 1) whose initiating event is a lineout. Each such record represents a distinct possession entry state. We then construct several derived variables that encode field position, time, and game context:

• Field position: The phase data provide location as eight ordered zones (from opposition goal line to own goal line): 5m-Goal (opp), 22m-5m (opp), 10m-22m (opp), Half-10m (opp), 10m-Half (own), 22m-10m (own), 5m-22m (own), Goal-5m (own). We use this zonal location directly as the field-position factor in the lineout model.

• Time remaining: Total seconds remaining in the match are transformed to a halfspecific variable, Sec_Remain_Half, defined as seconds remaining in the current half. We also define Less_Than_2_Min, an indicator equal to 1 when Sec_Remain_Half < 120 and 0 otherwise.

• Score and card context: Points_Difference records the score differential (for the team in possession), while Card_Diff tracks the net player advantage in terms of yellow or red cards.

• Team strength: WinPct_Diff is the running difference in win percentage between each team and its opponent at kickoff, with each team’s running rate shrinkage-smoothed toward 0.5 using m artificial matches: p = (W + 0.5m)/(G + m). We pre-specify m = 2.

To address potential double counting across consecutive possessions, we create a grouping identifier, run_id. Within each match, after ordering by event index, a run is defined as a maximal consecutive block of lineout-start possessions for the same team with unchanged starting point differential and unchanged eventual next-score outcome. Within each run_id we compute n_same, the run length. The role of run_id in estimation is discussed in Section 3.2. The final structure of this reduced dataset is illustrated in Table 1.

Table 1: This table summarizes the processed Rugby Union phase-level dataset used for estimation.

ID Round Home Away Phase Team_In_Poss Points_Difference Sec_Remain_Half Less_Than_2_Min Card_Diff WinPct_Diff Location run_id n_same Points

## 1 Harlequins Sale

Home

## 1 Harlequins Sale

Home

## 1 Harlequins Sale

Away

-3

## 1 Harlequins Sale

Away

-3

## 1 Harlequins Sale

Home

## 1 Harlequins Sale

Away

## 1 Harlequins Sale

Away

-7

2302 2166 2103 2043 1313 1188 926

10m-22m (opp)

Half-10m (opp)

-3

22m-5m (opp)

10m-22m (opp)

10m-Half (own) 4

5m-22m (own)

-7

10m-22m (opp)

## 2.3 Kicking Data

Our kicking dataset was generously provided by Ken Quarrie. It includes international penalty observations from Quarrie and Hopkins (2015), along with kicks from Super Rugby and the NPC competition. The sample spans 2000–2012 and contains 13,338 observations.

Each record contains exact (x, y) penalty locations, which lets us compute both kick distance and angle relative to the posts.

Figure 2 shows the empirical make rate in 5 m × 5 m pitch bins.

Figure 2: Empirical penalty-goal make rates on a 5 m × 5 m pitch grid. 4

## 3 Methods

## 3.1 Expected Points Framework

We evaluate the penalty decision, kicking at goal versus kicking to touch, by comparing the expected points (EP) of the two options at a given field location. Let (x, y) denote the location of a penalty on the field, where x is the distance in meters from the opposition try line and y is the lateral distance from the center of the pitch. For a given assumed gain in territory from a kick to touch, denoted dtouch, we define the decision quantity as the difference in expected points, with positive values favoring a lineout:

∆EP (x, y; dtouch) = EPlineout(xLO) − EPkick(x, y),

(1) where EPkick(x, y) is the expected points from attempting a kick at goal from (x, y), and EPlineout(xLO) is the expected points from a lineout at location xLO on the sideline. Here xLO denotes the resulting lineout x-coordinate after kicking to touch, with the translation rule defined in Section 3.8.

The following subsections describe estimation of EPlineout and EPkick.

## 3.2 Expected Points of a Lineout

To value a lineout, we model the probability of each next scoring outcome using a multinomial logistic regression, based on possession sequences that begin with a lineout in a given field zone. Let C denote the set of observed next-score outcomes in the sample (from the perspective of the team in possession), which in our data is {−7, −5, −3, 0, 3, 5, 7}. For each outcome c ∈ C, the model estimates

P (Y = c | X) log P (Y

= c∗

| X)

= αc + βc,1 · Location + βc,2 · Card_Diff + βc,3 · WinPct_Diff + βc,4 · L2M, where c∗ is the reference outcome category and L2M indicates fewer than two minutes remain in the half. The coefficients {αc, βc,1, βc,2, βc,3, βc,4} are estimated via maximum likelihood. The field position predictor Location enters the model as a factor, allowing a flexible, nonlinear relationship between field zone and scoring probability. Expected points are then recovered as a weighted sum over outcomes,

EPlineout(x) = c · Pˆ(Y = c | X), c∈C where Pˆ(Y = c | X) is the fitted probability from the multinomial model.

A multinomial model is preferable to a single linear regression on points because the response is a discrete state variable and the decision problem depends on the full conditional outcome distribution, not only its mean. Two game states can share similar mean points yet imply different risk profiles if probability mass is distributed differently across no-score, penalty, and try outcomes. Modeling P (Y = c | X) directly preserves that structure, after which

EP is obtained as a linear functional of estimated state probabilities, consistent with prior American-football EP modeling (Yurko et al., 2019).

Grouped five-fold sensitivity checks by match (Appendix A, Table 7) support an additive baseline with Location, Card_Diff, WinPct_Diff, and Less_Than_2_Min. We therefore keep Less_Than_2_Min in the main specification so end-of-half effects enter the core model directly. Alternative covariate specifications (Card_Diff × WinPct_Diff, separate teamstrength terms, and adding continuous Sec_Remain_Half) are reported in Appendix A. The win-percentage shrinkage prior is pre-specified at m = 2 pseudo-games, with robustness checks reported in Appendix B, Table 8.

This specification captures downstream contingencies observed in matches: losing one’s own lineout, turnovers in subsequent phases, or the opponent scoring following a turnover. The resulting quantity represents the expected next-score value of having a lineout at that field position, given competition-level play and the current game context. For interpolation and plotting, we order zones from opposition to own goal line and map them to zone midpoints in meters from the opposition try line (5, 13.5, 31, 45, 55, 69, 86.5, 97.5) using boundaries (0, 5, 22, 40, 50, 60, 78, 95, 100). Unless stated otherwise, decision maps set Less_Than_2_Min to 0.

## 3.2.1 Dealing with Double Counting

Double counting can arise not only at the phase level (which we already handle by restricting to Phase = 1), but also across consecutive possessions that map to the same next-score event. Table 2 shows three successive lineout-start possessions for the same team with the same starting score differential and the same eventual outcome.

Table 2: This table shows an example of consecutive lineout-start possessions mapped to the same next-score outcome.

ID Round Home Away Phase Team_In_Poss Points_Difference Sec_Remain_Half Less_Than_2_Min Card_Diff WinPct_Diff Location run_id n_same Points

## 1 Harlequins Sale

Home

## 1 Harlequins Sale

Home

## 1 Harlequins Sale

Home

22m-10m (own) 11

22m-5m (opp)

22m-5m (opp)

Let run r contain nr consecutive lineouts with a common eventual next-score outcome Yr. If all rows are kept, the likelihood receives nr copies of Yr from that run, so long runs get mechanically up-weighted. In effect, a single scoring event can be counted multiple times simply because play recycled through repeated lineouts before that score occurred. This would bias fitted class probabilities toward outcomes that happen to appear in long sameoutcome runs, rather than toward genuinely more frequent scoring states.

Accordingly, we retain exactly one representative row per run_id. For run r with observations Yr1, . . . , Yrnr , we draw one index uniformly and keep only that row:

Y˜r ∼ Uniform {Yr1, . . . , Yrnr } .

We implement this directly through row selection (one retained row per run) rather than through a weighted-likelihood fit.

This run-level subsampling ensures that each repeated same-outcome sequence contributes once, mitigating pseudo-replication while preserving realistic variation in field position and context across runs. The same idea is used inside each bootstrap replicate (one draw per run in each resampled match), so point estimates and uncertainty intervals are aligned to the same dependence structure. Our approach is conceptually similar to the cluster-level subsampling used by Brill et al. (2025), who randomly retain a subset of plays per simulated game to reduce within-game dependence when estimating win probability. After sampling, we obtain a total of 2,046 lineout observations for estimation. 3.2.2 Multinomial Regression Summary The lineout model treats the next scoring event as a categorical random variable with outcomes {−7, −5, −3, 0, 3, 5, 7} points and converts fitted class probabilities into EP through the probability-weighted sum defined above.

Figure 3: Estimated expected points of the next score by lineout meter line (interpolated from zonal field-position factors). 3.2.3 EP Uncertainty Quantification via Bootstrap To quantify uncertainty in the expected points estimates, we use a percentile bootstrap with B = 2000 replicates. Each replicate follows the same dependence-aware procedure: 1. Sample matches with replacement (match-level cluster bootstrap).

2. Within each resampled match, and for each run_id, draw exactly one row uniformly at random.

3. Refit the multinomial model on that sampled dataset.

4. Recompute lineout EP across meter-line positions from fitted class probabilities.

Confidence intervals are given by the 2.5th and 97.5th percentiles of the bootstrap distribution.

Figure 4: Bootstrap uncertainty bands for lineout expected points (95% confidence intervals).

Uncertainty is largest near a team’s own try line, where lineout-start possessions are sparse and penalty shots at goal wouldn’t even be considered. The decision analysis therefore focuses on penalties within roughly 65 m of the opposition try line.

## 3.3 Expected Points of a Penalty Kick

The expected points of a penalty kick at goal are the weighted sum of the value of a make and the continuation value of a miss. Unlike lineouts, kick outcomes depend primarily on distance and angle to the posts rather than raw field coordinates. Let d denote distance from the penalty spot to the center of the posts and let θ denote the lateral angle. Then

EPkick(d, θ) = Pmake(d, θ) · 3 + 1 − Pmake(d, θ) · EPmiss(d, θ),

(2) where 3 points are awarded for a successful kick, Pmake(d, θ) is the probability of a successful kick from (d, θ), and EPmiss(d, θ) is the expected points of the continuation state following a miss (e.g., change in possession, change in field position).

The field coordinates (x, y) of a penalty uniquely determine (d, θ) through pitch geometry, so EPkick(x, y) is obtained by evaluating EPkick(d, θ) at the corresponding (d, θ). We estimate Pmake(d, θ) from the kicking data and approximate EPmiss(d, θ) from restart sequences in the phase-level dataset.

## 3.4 Estimating Kick Success Probability

Using the exact (x, y) penalty locations, we compute the kick angle to the posts as:

|x − 35| 180 θ = arctan

· y π where x is the distance from the left touchline, y is the distance from the opposition try line, and 35 is the midpoint of the pitch width (in metres), so |x − 35| is the horizontal distance from the centre of the posts.

|x − 35| kick (x, y) y distance θ posts (35, 0) try line

Figure 5: Geometry used to compute the kick angle θ from field coordinates (x, y), where y is the distance from the try line and |x − 35| is the horizontal distance from the centre of the posts.

We then fit a logistic model with distance from the posts and angle as the two predictors: log pi 1 − pi

= β0 + β1 · distancei + β2 · θi where pi is the probability that kick i is successful.

As a sensitivity check (Appendix A, Table 7), a GAM with smooth terms in angle and distance produced nearly identical out-of-sample performance (log loss 0.5165 vs. 0.5183 for logistic) and similar marker-level make probability in the case study (0.563 vs. 0.538). We therefore retain the logistic specification for interpretability.

Estimated kick success probabilities, with dashed contours at probability levels (0.2, 0.4, 0.6, 0.8), are shown in Figure 6.

Figure 6: Estimated probability of kick success by field position. The goal-post center is at lateral position 35 m, and estimated kick probabilities begin at 5 m from the goal line because no observations occur at 0 m.

## 3.5 Continuation Value of a Missed Kick

In rugby, a missed penalty does not immediately end the sequence. After a miss, the defending team may ground the ball in-goal, the ball may travel dead (triggering a 22 m drop-out), or the ball may remain live and be returned from inside the 22. Returned-in-play misses are relatively infrequent, and our phase labels do not reliably separate them from other openplay kicks. We therefore adopt a simplifying assumption: a missed penalty transitions to a 22 m drop-out restart.

Operationally, we identify restarts that (i) do not follow a change in score (excluding postscore kick-offs) and (ii) did not occur at the start of a half, and compute the expected nextscore value of those entries by restart zone, using the same EP framework as for lineouts (Section 3.2). Table 3 reports average expected points following kick restarts by original kick location. Because restart location is only available in broad zones, we map each zone to its midpoint in meters from the opposition try line and fit a weighted smoothing spline (weights = zone counts) to obtain a continuous approximation for EPmiss(y). This avoids artificial step changes at zone boundaries while remaining explicit about the coarse zonal input.

## 3.6 Penalty Kick Expected Points Surface

Combining the kick success surface and the continuation values yields an expected points surface for penalty kicks. For each location on the field, we map (x, y) to (d, θ), evaluate Pmake(d, θ) from the logistic model, and evaluate smoothed EPmiss(y) from the zonal restart

Table 3: This table reports average points following missed-kick restarts by phase-data zone.

Location n Avg. Points

Goal–5m (own) 14

5m–22m (own)

22m–10m (own) 89

10m–Half (own) 45

Half–10m (opp) 22

10m–22m (opp) 7

0.36 -1.00 1.10 -0.44 1.23 4.29

Overall Average 198

0.60 data in Table 3. These quantities are substituted into Equation (2) to obtain the expected points of a kick at goal from that location.

## 3.7 Uncertainty Quantification for Kicks

To align uncertainty reporting with the decision quantities of interest, we estimate uncertainty directly for kick-attempt expected points EPkick rather than reporting continuationonly and make-probability components separately. We use a bootstrap with B = 2000 replicates and summarize kick-attempt EP across dead-center kick locations (x = 35) as distance from the opposition try line varies. In each replicate we resample penalty kicks and refit the kick-success model, resample restart rows and rebuild the continuation smoother, and then recompute EPkick over the dead-center distance grid.

Figure 7: Kick-attempt expected points by dead-center distance (x = 35): bootstrap-mean curve with 95% confidence band.

At the case-study marker (x = 16, y = 40) with dtouch = 20 m, this gives EPkick = 2.22 with 95% CI [1.65, 2.76].

To propagate uncertainty into the decision quantity itself, we run a joint bootstrap with B = 2000 replicates. In each replicate, we:

1. Resample matches with replacement and, within each resampled match, sample one lineout row per run_id.

2. Refit the lineout multinomial model and lineout smoother.

3. Resample penalty kicks and refit the kick-success model.

4. Resample restart rows, refit the continuation smoother, and recompute EPkick and ∆EP .

At the case-study marker (x = 16, y = 40) with dtouch = 20 m, this yields EPlineout = 1.69 (95% CI: [1.25, 2.20]), EPkick = 2.22 (95% CI: [1.65, 2.76]), and ∆EP = −0.53 (95% CI: [−1.26, 0.25]). The corresponding decision uncertainty is shown in Section 4.2.1.

## 3.8 Adjusting for Meters Gained on Kick to Touch

At each penalty location on the field, we compare the value of attempting a kick at goal with the value of kicking to touch and taking the ensuing lineout. The kick-at-goal value is calculated at the penalty spot, using the distance and lateral angle to the posts implied by that location. By contrast, the lineout value is calculated at the location where the lineout would actually occur after the kick to touch.

Let (x, y) denote the penalty location, and let dtouch denote the expected meters gained from a kick to touch along the length of the field. Starting from x (distance from the opposition try line), we approximate the resulting lineout location as xLO = max{5, x − dtouch},

(3) shifting the ball dtouch meters closer to the opposition try line and truncating at the 5 m line if necessary, since the laws prohibit lineouts closer than 5 m from the try line. In reality, the ball is kicked into touch and the restart is on the sideline; however, our lineout EP model depends on longitudinal location (xLO) and context covariates, not on lateral coordinate, so we suppress the lateral dimension for the lineout component.

For a given assumed gain dtouch, the expected points of choosing the lineout option from penalty location (x, y) are then

E Plineout (xLO ), evaluated via the regression in Section 3.2. In our baseline decision maps we consider a grid of plausible translation distances dtouch ∈ {0, 5, 10, 15, 20, 25} m, reflecting different assumptions about territory gained by kicking to touch. Because the data do not record realized meters gained to touch at the penalty level, dtouch is treated as a scenario parameter rather than a latent random variable. The maps are therefore conditional on the chosen dtouch value.

## 3.9 Decision Maps

Given EPlineout and EPkick, the relative value of a lineout versus a kick at goal at the same penalty location is defined by Equation (1). Here (x, y) is the penalty location, dtouch is the assumed meters gained by kicking to touch, and xLO is set by Equation (3). Positive values of ∆EP (x, y; dtouch) favor choosing the lineout, while negative values favor taking the kick at goal, with ∆EP (x, y; dtouch) = 0 tracing out the indifference frontier between the two options.

By mapping out ∆EP (x, y; dtouch) across the field, we obtain decision maps that show how location and assumed meters gained shape the optimal choice. Figure 8 displays these maps for a range of values of dtouch.

(1) dtouch = 0 m.

(2) dtouch = 5 m.

(3) dtouch = 10 m.

(4) dtouch = 15 m.

(5) dtouch = 20 m.

(6) dtouch = 25 m.

Figure 8: These decision maps compare the expected points of a lineout versus a kick at goal for different assumed meters gained to touch dtouch, where blue favors the lineout and red favors the kick.

As expected, increasing dtouch shifts the decision surface toward the lineout option, with a larger share of the pitch turning blue in Figure 8.

## 4 Results

## 4.1 Scenario Analysis

Varying game context covariates in the regression model yields scenario-specific decision surfaces.

4.1.1 Manpower Advantages and Disadvantages In rugby union, manpower differentials occur when a player receives a yellow or red card and is sent off the field (for 10 minutes for a yellow and for the rest of the game for a red card). This directly affects the Card_Diff covariate in the lineout EP model.

(7) Decision map when the at- (8) Decision map when neither (9) Decision map when the detacking team has a yellow card. team has a yellow card. fending team has a yellow card.

Figure 9: These decision maps show manpower-state scenarios while holding other covariates fixed; blue favors the lineout and red favors the kick.

Figure 9 shows substantial shifts in the decision surface by yellow-card state: kicks are preferred more often when the attacking team is down a player, while lineouts are preferred more often when the attacking team has a numerical advantage.

4.1.2 Strong vs. Weak Teams

The same approach can be used to examine how the decision surface changes with positive or negative win-percentage differentials by varying WinPct_Diff.

Figure 10 indicates that stronger teams (positive WinPct_Diff) realize larger expected points from lineouts across more of the pitch, making the aggressive option more attractive. Weaker teams (negative WinPct_Diff) are relatively better off taking points from penalty kicks, though the effect is much less pronounced than the impact of yellow cards. Interestingly, the decision boundary doesn’t appear to shift much when changing relative team strength.

4.2 Case Study: New Zealand vs. South Africa

We apply the model to a real match to illustrate both single-decision analysis and aggregate decision quality. The case-study data were collected by the authors from New Zealand vs.

(10) Decision map at a -25% win-percentage differential.

(11) Decision map at a 0% winpercentage differential.

(12) Decision map at a +25% win differential.

Figure 10: These decision maps compare teams with different win-percentage differentials, using the same color scale as the manpower scenarios.

South Africa, played on September 16, 2025. Throughout this case study, we report the mean-EP-optimal decision (the larger of the two bootstrap-mean EP values) and two regret metrics for each decision j:

Rmean,j = max EPbmeesta,nj − EPamcteuaanl,j , 0 ,

Rboot,j = Eb max EPb(be)st,j − EPa(cbt)ual,j , 0 .

Rmean is deterministic from the reported mean EP values and equals the points left on the table when comparing only the two bootstrap-mean options, while Rboot is uncertainty-aware, averaging points left on the table across bootstrap draws, and can remain positive even when the actual decision matches the mean-EP-optimal decision.

## 4.2.1 A Single Penalty Decision

Consider a penalty awarded to South Africa in the 60th minute, 16 m from the left touchline and 40 m from the opposition try line. We evaluate this decision by varying the expected territory gained from a kick to touch. There were no yellow or red cards at the time. We set win-percentage differential to zero (teams treated as evenly matched), and the under-2minute indicator is 0.

Figure 11 is the primary decision-uncertainty display for this marker: it plots bootstrapmean ∆EP (x, y; dtouch) versus dtouch with bootstrap 95% bands. The bootstrap-mean curve crosses zero around 26 m.

In the game, South Africa gained 20 m when they kicked to touch from this position. The model’s recommendation at the penalty location, with a shift of 20 m is shown in Figure 12.

At this point on the pitch, the bootstrap-mean optimal decision is to kick at goal. Table 4 reports bootstrap means, 95% confidence intervals, and decision-quality metrics at the marker location.

For this decision at dtouch = 20 m, the joint bootstrap gives mean ∆EP = −0.53 with 95% CI [−1.26, 0.25] and Pr(∆EP > 0) = 0.08. This indicates reasonable certainty, with

Figure 11: Expected-points difference between lineout and kick as a function of meters gained to touch (line: bootstrap mean, band: 95% CI).

Figure 12: Penalty decision surface at the observed field position, with the marker denoting the penalty location.

Table 4: Single-decision summary at the case-study marker (dtouch = 20 m), including bootstrap uncertainty and regret metrics for the observed lineout choice.

EP Lineout EP Kick ∆EP

Bootstrap mean

1.69

2.22

-0.53

95% CI

[1.25, 2.20] [1.65, 2.76] [-1.26, 0.25]

Observed decision: lineout Rmean = 0.53, Rboot = 0.55, Pr(∆EP > 0) = 0.08 the bootstrap distribution favoring a kick at goal in this situation. Figure 13 provides a complementary distributional view at this single dtouch value.

Figure 13: Joint-bootstrap distribution of ∆EP at the case-study marker for dtouch = 20 m.

4.2.2 All Penalty Decisions in the Match Decision quality can also be compared across all relevant penalties in the match. Using the definitions above, Table 5 reports bootstrap-mean option values, the mean-EP-optimal decision, and both regret metrics for all penalties within 60 m of the opposition try line. We assume a flat 20 m gain for each kick to touch, treat the teams as equally matched, and use the observed under-2-minute indicator for each decision. If the actual decision matches the mean-EP-optimal decision, then Rmean = 0 by construction; Rboot can still be positive when a non-trivial share of bootstrap draws favors the other option.

Table 5: Bootstrap-mean EP values and two regret definitions for all case-study penalties.

Team NZ NZ SA SA SA SA NZ SA NZ NZ SA SA SA

Actual kick lineout lineout kick kick lineout kick lineout lineout lineout lineout lineout lineout

Mean-EP Optimal kick kick kick lineout kick kick lineout kick lineout lineout lineout kick kick

Lineout EP 1.46 1.91 1.34 2.89 1.54 0.90 3.12 1.69 4.26 4.26 2.69 0.81 1.82

Kick EP 1.96 2.19 1.92 2.57 1.87 1.66 2.71 2.22 2.57 2.68 2.55 1.31 2.89

∆EP -0.50 -0.28 -0.59 0.32 -0.33 -0.76 0.41 -0.53 1.69 1.57 0.14 -0.49 -1.07

Rmean 0.00 0.28 0.59 0.32 0.00 0.76 0.41 0.53 0.00 0.00 0.00 0.49 1.07

Rboot 0.02 0.35 0.59 0.36 0.05 0.77 0.42 0.55 0.00 0.00 0.10 0.51 1.07

Summary metrics of decision quality for this match are reported in Table 6.

Table 6: This table reports summary metrics of penalty-decision quality for the case-study match.

Metric Total Rmean Total Rboot Proportion Mean-EP Optimal

Value 4.46 4.80 0.38

As summarized in Table 6, the mean-EP-optimal decision was made 38% of the time. Total regret is 4.46 points on the mean scale and 4.80 points under the uncertainty-aware bootstrap definition. For context, the game ended 24–17 to New Zealand, so this gap is non-trivial. It is important to note that South Africa was trailing by more than 3 points towards the end of the match so the final ’inefficient’ EP decisions were necessary to attempt to win the game.

## 5 Discussion

## 5.1 Conclusions

This paper develops a decision-ready Expected Points framework for evaluating whether to kick for goal or kick to touch following a penalty in rugby union. By combining a lineoutbased EP model from phase-level Premiership data with an angle–distance model of penalty kick success and a continuation value for missed kicks, we obtain two context-aware EP surfaces and a derived decision surface that identifies where each option maximizes expected return.

The resulting decision maps make the penalty decision explicit as a function of field location, expected meters gained to touch, player advantages, and team-strength differentials. Scenario analyses show how the indifference frontier shifts with yellow cards and team quality, while the case study of New Zealand vs. South Africa demonstrates how the framework can be used to evaluate both individual choices and aggregate decision quality through a regret measure. Under the smoothed continuation specification, the model still identifies inefficiencies, but many decisions sit nearer the indifference frontier than under a purely stepwise continuation mapping.

Because the framework is modular, it can be adapted to different competitions or tailored to specific teams by refitting the underlying EP components with alternative data sources. The lineout and kicking modules can be updated independently as richer data become available, providing a transparent foundation for decision-support tools in both professional and amateur settings.

## 5.2 Limitations and Future Directions

Several assumptions and data limitations should be acknowledged, along with concrete directions for future work.

First, the model combines phase-level data from club competitions with penalty-kicking data from international matches, introducing potential inconsistencies in player quality, decisionmaking, and context. Future work could develop fully competition-specific models by collecting phase-level and kicking data from the same league and year, or by fitting hierarchical models that allow competition-level differences in both lineout and kicking performance to be estimated explicitly.

Second, the analysis restricts team choices to kicking for goal or kicking to touch, even though teams occasionally opt for a scrum or a quick tap—particularly near the try line— albeit infrequently. Extending the framework to additional decision branches is natural: EP models can be trained for scrums and tap-and-go restarts using the same phase-level machinery, enabling multi-armed decision maps that compare all realistic options from a given penalty location.

Third, the analysis is limited to a single season, which constrains the sample size and reduces the generalizability of the findings across competitions or years. Future work could pool multiple seasons and competitions, possibly with random effects for season and league, to increase sample size, stabilize estimates in rare field zones, and quantify between-competition variation in EP surfaces.

Fourth, selection bias may influence the results (Brill et al., 2025). Stronger teams are both more likely to generate attacking lineouts in the opposition half and more likely to earn penalties. As a result, lineouts in advanced field positions are disproportionately taken by stronger sides, potentially inflating expected points estimates for lineouts near the try line. A similar dynamic is present for the kicking data, since stronger sides will have generated more of the observed penalties, and coaches may only elect to kick when they deem the attempt makeable for their kicker. Future research could focus on further de-biasing EP estimates with respect to the underlying decision processes that generated the data.

Fifth, the data do not track realized meters gained when kicking to touch (or individual kicker ability for touch-finding), making it necessary to assume a translation distance between the penalty location and the resulting lineout. As a result, our decision maps are conditional on fixed dtouch scenarios rather than integrated over an empirical dtouch distribution. Future analyses trained on richer tracking or event data could estimate P (dtouch | context) directly and evaluate lineout value via iterated expectation, while also supporting player- and teamspecific models for both goal-kicking accuracy and touch gain.

Sixth, the current datasets lack the granularity of precise (x, y) field coordinates for lineouts, relying instead on zonal encodings and an approximate mapping to continuous coordinates. Improvements in data collection—for example, through optical or GPS tracking—would allow EP surfaces to be estimated directly on a fine spatial grid, supporting smoother decision boundaries, more accurate modeling of angle-dependent effects, and better treatment of corner and touchline situations.

Finally, this modeling framework optimizes expected points. A common critique of expectedpoints-based decision models is that they maximize expected points rather than expected win probability (the quantity that ultimately matters in a game). A natural extension is to develop win-probability models that incorporate field location, score differential, time remaining, and player imbalances resulting from yellow or red cards. Decisions could then be evaluated directly on the scale of win probability, with EP retained as an interpretable intermediate quantity.

## 5.3 Reproducibility

All code used to process the data, fit the models, and generate the figures and tables in this article is available at https://github.com/WhartonSABI/rugby-ep.

## References

Baldwin, B. (2021). Nfl win probability from scratch using xgboost in r. Open Source Football Blog.

Brill, R. S., Yurko, R., and Wyner, A. J. (2025). Analytics, have some humility: A statistical view of fourth-down decision making. The American Statistician, 79(3):393–409.

Burke, B. (2009). The 4th down study – part 3. Advanced Football Analytics (formerly Advanced NFL Stats), published September 16, 2009.

Lock, D. and Nettleton, D. (2014). Using random forests to estimate win probability before each play of an nfl game. Journal of Quantitative Analysis in Sports, 10(2):197–205.

Martinez-Arastey, G., Datson, N., Smith, N., and Robins, M. (2025). Foundations of expected points in rugby union: A methodological approach. Journal of Sports Analytics, 11:1–14. Creative Commons Attribution 4.0 License.

Monpezat, B. (2023). Predicting penalties and conversions success: Rugby world cup 2023 kicks probability insight. Data Ruck Blog.

Quarrie, K. L. and Hopkins, W. G. (2015). Evaluation of goal kicking performance in international rugby union matches. Journal of Science and Medicine in Sport, 18(2):195– 198.

Romer, D. (2006). Do firms maximize? evidence from professional football. Journal of Political Economy, 114(2):340–365.

Yurko, R., Ventura, S., and Horowitz, M. (2019). nflwar: A reproducible method for offensive player evaluation in football. Journal of Quantitative Analysis in Sports, 15(3):163–183.

## Appendix

A Model Specification Sensitivity

Table 7: Out-of-sample sensitivity checks for lineout and kick model specifications (grouped 5-fold CV).

Component

## Model

CV log loss CV Brier ∆ log loss vs baseline

Kick success Kick success Lineout multinomial Lineout multinomial Lineout multinomial Lineout multinomial

Logistic: angle + distance GAM: s(angle) + s(distance) Baseline: meter + Card + WinPct + <2min Baseline + Card x WinPct Baseline with separate team strengths Baseline + continuous time

0.5184 0.5164 1.7513 1.7675 1.7426 1.7079

0.1754 0.1748 0.7852 0.7862 0.7816 0.7707

0.0000 -0.0020 0.0000 0.0162 -0.0088 -0.0434

B Win-Percentage Prior Sensitivity

This section isolates sensitivity to the pre-specified win-percentage shrinkage prior while holding the baseline lineout specification fixed.

Table 8: Sensitivity of baseline lineout performance to the running win-percentage shrinkage prior m (grouped 5-fold CV). m pseudo-games CV log loss CV Brier ∆ log loss vs m = 2

0.5

1.7543

0.7854

0.0186

1.7523

0.7819

0.0165

1.7357

0.7836

0.0000

1.7670

0.7835

0.0313

1.7308

0.7802

-0.0049
