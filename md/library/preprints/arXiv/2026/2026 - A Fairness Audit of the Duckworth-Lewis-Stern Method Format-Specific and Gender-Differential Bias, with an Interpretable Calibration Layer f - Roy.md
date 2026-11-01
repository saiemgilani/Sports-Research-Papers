<!-- source: 2026 A Fairness Audit of the Duckworth-Lewis-Stern Method - Roy.pdf -->
<!-- arXiv:2609.04754, 4 Sep 2026 · text extracted from the arXiv PDF (open access) -->
<!-- weekly research roundup add, 2026-09-08 -->

# A Fairness Audit of the Duckworth–Lewis–Stern Method: Format-Specific and Gender-Differential Bias, with an Interpretable Calibration Layer for Cricket Target Revision

**Soumyadeep Roy** — St. Xavier's College (Autonomous), Kolkata, India · `soumyadeeproy142@gmail.com`

arXiv:[2609.04754](https://arxiv.org/abs/2609.04754), 4 September 2026.

## Abstract

The Duckworth–Lewis–Stern (DLS) method has set revised targets in rain-interrupted limited-overs cricket since 1999, yet no large-scale empirical audit of its prediction bias has been published. Using ball-by-ball data for 8,150 international matches from Cricsheet, we audit DLS by sampling synthetic interruption points and comparing its resource-based projection against the runs actually scored. We find that DLS bias is far from uniform: it varies systematically with match state, over-predicting the death overs of Twenty20 and under-predicting collapse scenarios in one-day cricket, a format-specific pattern we quantify across the full space of overs remaining and wickets lost (a 137-run span of per-bucket mean bias). Our second finding concerns fairness: because a single resource table governs both men's and women's cricket, DLS miscalibrates women's one-day matches relative to men's at comparable match states, producing a gender-differential bias of several runs (a +6.13-run gap on the training split) that, to our knowledge, has not previously been documented. The gap survives match-level clustered inference, holds among matches between top (Full Member) teams, and is stable across temporal windows. We benchmark DLS against five modern learning methods and introduce DLS-Cal, a lightweight interpretable calibration layer that adds a state-conditioned correction to the published DLS prediction, reducing absolute bias by 31% on ODI and 19% on T20I; a gender-aware variant reduces women's ODI residual bias from +6.19 to +0.65 runs without altering the DLS framework. We also introduce the Win-Flip Rate, a threshold-based fairness metric for target revision, and release code, trained models, and the audit dataset for reproducible research.

## Why it matters

DLS is the ICC's official, non-negotiable resolution method for every rain-affected men's and women's international — an outcome-determining formula with essentially no public empirical audit trail in 25+ years of use. This is the first large-sample (8,150 matches) empirical test of whether its projections track actual scoring, and the first to document that the *same* resource table produces materially different bias by gender. A +6.13-run systematic gap in a method that directly sets a match-winning target is a governance-relevant finding, not just an academic one.

## Method, in brief

- **Data**: Cricsheet ball-by-ball logs, 8,150 international men's and women's ODI/T20I matches.
- **Audit design**: sample synthetic interruption points within completed (uninterrupted) matches, compute what DLS *would have* projected as the revised target from that point, and compare against runs actually scored the rest of the innings. This sidesteps the confound of only being able to observe DLS on matches that were genuinely interrupted.
- **Bias mapping**: tabulate mean bias across the full (overs remaining × wickets lost) state space — finds DLS over-predicts scoring in T20 death overs and under-predicts collapse scenarios in ODIs, a 137-run span between the best- and worst-calibrated buckets.
- **Fairness test**: same state-space comparison split by gender, with match-level clustered standard errors (correct unit of inference — observations within a match aren't independent) and a Full-Member-only robustness subsample to rule out team-quality confounding.
- **DLS-Cal**: a state-conditioned additive correction layer on top of the *existing* DLS output (doesn't replace it, doesn't require ICC to adopt a new model) — 31%/19% absolute bias reduction on ODI/T20I; a gender-aware variant nearly eliminates the women's ODI gap (+6.19 → +0.65 runs).
- **Win-Flip Rate**: a new fairness metric — how often would the calibration correction actually flip who wins, at a given target threshold — proposed as a decision-relevant complement to raw bias metrics.
- Benchmarks against five modern learning methods (details in the paper's methods section); code, trained models, and the audit dataset are released.

## Assessment

**Novelty (8/10).** First published large-scale empirical audit of DLS bias and the first documentation of a DLS gender-differential effect. The Win-Flip Rate is a genuinely new, decision-relevant fairness metric for this class of problem (target-revision methods), not just an accuracy statistic.

**Practicality (8/10).** Directly actionable by a cricket board or the ICC's own methods committee: DLS-Cal is a drop-in correction layer, not a replacement system, which lowers the adoption barrier considerably. The Win-Flip Rate gives officials a metric expressed in the currency they actually care about (does the correction change who wins), rather than an abstract error number.

**Reproducibility (9/10).** Public Cricsheet data named explicitly; synthetic-interruption audit design is fully specified; code, trained models, and the audit dataset are released per the abstract. Docked one point pending independent verification of the released artifacts.

**Composite: 25/30.**

**Caveats.** The 137-run bias span is a *range* across state-space buckets, not a single average bias figure — worth reading the full per-bucket table before quoting a single number. The synthetic-interruption design assumes completed matches are a valid proxy for how the same teams would have played out a genuine rain-shortened chase, which is a reasonable but not bulletproof identification assumption (rain interruptions may correlate with match state in ways synthetic sampling doesn't capture). As with any bias-audit paper, "improves calibration on this historical sample" does not guarantee performance on the next genuinely rain-affected match — but this is by a wide margin the most rigorous public treatment of DLS calibration/fairness available.
