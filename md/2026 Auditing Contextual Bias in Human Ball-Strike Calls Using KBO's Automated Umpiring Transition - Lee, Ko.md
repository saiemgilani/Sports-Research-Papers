<!-- source: 2026 Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition - Lee, Ko.pdf -->
<!-- arXiv:2609.03786, 3 Sep 2026 · text extracted from the arXiv PDF (open access) -->
<!-- weekly research roundup add, 2026-09-08 -->

# Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition

**Kichang Lee, JeongGil Ko** — Yonsei University, School of Integrated Technology, Seoul, Republic of Korea

arXiv:[2609.03786](https://arxiv.org/abs/2609.03786), 3 September 2026.

## Abstract

This paper uses the Korean Baseball Organization's adoption of the Automated Ball-Strike (ABS) system to audit long-standing claims about contextual bias in human ball-strike calls. Using pitch-level KBO data from 2021 through the available portion of the 2026 season, we model called-strike probability for taken pitches near the strike-zone boundary, with 2022–2023 as the primary human-umpire baseline and ABS seasons (2024 and onward) as a diagnostic benchmark. The strongest evidence concerns count pressure. Relative to 0–0 counts, human umpires called substantially fewer strikes in two-strike counts and more strikes in hitter-ahead three-ball counts. Specifically, in the main 0.25-ft boundary band, 0–2 was associated with a -17.17 percentage-point effect and 3–0 with a +6.61 percentage-point effect. Under ABS, the corresponding effects were close to zero and did not survive false-discovery-rate correction. Game progression shows a smaller but coherent pattern as human calls were less strike-prone in early innings and more strike-prone in innings 7–9+, especially in late-close situations, while complete ABS seasons were essentially flat. Other suspected biases are weaker or more localized. Salary-based reputation proxies provide suggestive but proxy-sensitive evidence, and catcher identity shows human-period residual heterogeneity that disappears under ABS. Home-context evidence is mostly null at the umpire level, with one FDR-significant human-period exception and an exploratory umpire-team gap best treated as an audit lead. Overall, the results do not show that human umpires were biased everywhere. Instead, they map where the human strike zone was most context-sensitive, where evidence was weaker, and where common suspicions received little support.

## Why it matters

Umpire strike-zone bias is one of the most litigated questions in public baseball analytics (PITCHf/x- and Statcast-era studies have argued for count-based, catcher-framing, and reputation effects for over a decade), but almost all of that work has had to infer bias indirectly, since there was no ground-truth "correct call" to compare against. The KBO's league-wide switch to an Automated Ball-Strike system in 2024 hands this literature something rare: a real, non-simulated natural experiment where the same population of hitters/pitchers/games is observed under human calling and then under a robotic ground truth. That design is directly relevant to MLB's own ABS/Challenge System rollout debate (MLB tested and is expanding a challenge system in spring training and some minor leagues over the same period), making this a timely applied-policy paper, not just a historical bias study.

## Method, in brief

- **Data**: pitch-level KBO data, 2021 through partial 2026 season; focuses on *taken* pitches near the strike-zone boundary (the only pitches where a "would robot vs. human disagree" question is meaningful).
- **Design**: 2022–2023 = human-umpire baseline; 2024-onward ABS seasons = diagnostic benchmark for what the *same* boundary pitches "should" have been called, given the same distributions of count, inning, and game context.
- **Model**: called-strike probability as a function of distance from the strike-zone boundary, count, inning, score situation (late-close), and additional covariates (salary-based reputation proxy, catcher identity, home/away, umpire-team pairing); false-discovery-rate correction applied across the many contextual comparisons tested (correct practice given the number of subgroup effects examined).
- **Headline finding**: strong, count-conditional bias in the human era (-17.17 pp at 0–2, +6.61 pp at 3–0 in the main 0.25-ft band) that is close to zero and non-significant after FDR correction under ABS — i.e., the bias tracks the *rule-enforcement mechanism*, not some fixed property of those game states.
- **Secondary findings, explicitly hedged by the authors**: weaker/more localized effects for game progression (innings 7–9+, late-close), reputation proxies ("suggestive but proxy-sensitive"), catcher framing (human-period heterogeneity that vanishes under ABS), and home-context (mostly null, one exception, one flagged as an "audit lead" rather than a confirmed effect).

## Assessment

**Novelty (8/10).** The natural-experiment design — using a real automated-system rollout as the counterfactual rather than a statistical adjustment — is a genuinely creative identification strategy relative to the existing indirect-inference literature on umpire bias, and KBO's earlier ABS adoption than MLB's makes this data available years before an equivalent U.S. audit could be run.

**Practicality (7/10).** Directly relevant to the live MLB policy question of whether/how to roll out automated or challenge-based ball-strike systems, and it's a template methodology transferable to MLB the moment enough ABS-era Statcast/challenge data accumulates domestically.

**Reproducibility (5/10).** KBO pitch-level tracking data is not as openly/uniformly distributed as MLB Statcast, and the paper does not state a code/data release; a public replication would likely require negotiating KBO data access rather than downloading an open dataset, which is the main drag on this score.

**Composite: 20/30.**

**Caveats.** The authors are careful to frame this as "not biased everywhere" rather than a blanket indictment of human umpiring, and several secondary effects (reputation, home-umpire-team pairing) are explicitly flagged as weaker or exploratory — worth preserving that nuance rather than over-quoting the headline count-pressure numbers as if they generalized to every bias claim tested.
