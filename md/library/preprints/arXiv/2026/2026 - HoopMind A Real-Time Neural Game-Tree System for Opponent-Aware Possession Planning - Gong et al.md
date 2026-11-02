<!-- source: 2026 - HoopMind A Real-Time Neural Game-Tree System for Opponent-Aware Possession Planning - Gong et al.pdf -->
<!-- arXiv:2608.29563, 2026-08-30 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# HoopMind: A Real-Time Neural Game-Tree System for Opponent-Aware Possession Planning

**Yibo Gong, Cong Guo, Jiacheng Ding**

arXiv:[2608.29563](https://arxiv.org/abs/2608.29563), submitted 2026-08-30.

## Abstract

School coaches prepare for opponents with game film and intuition. The analytics tools of professional teams stay out of reach. We ask how far public data can close this gap. Professional basketball is our case study, chosen for its data rather than the league. We fuse five public sources into one per-shot dataset of 4.23M shots over 21 seasons. The sources are shot locations, two play-by-play feeds, official matchup tracking, and player biometrics. Alignment across them is 99.5% to 100%. We also report two data pitfalls that are easy to miss. We then model a half-court possession as a sequential game. Shot values come from ShotNet, an embedding multilayer perceptron (MLP). On a held-out season it beats a zone-rate baseline and a logistic baseline, and its probabilities are well calibrated. A depth-limited expectimax search then solves the offensive decision tree, with branch-and-bound pruning to keep it real time. All training runs offline, so the online system stays light. A scouting planner and a playable simulator both run in a single browser page.

## Why it matters

Public-data shot-value model with a game-tree planner; the data-fusion pitfalls are the transferable part for anyone joining NBA shot and play-by-play feeds.

## Triage score

Sport: NBA · Novelty 6 · Practicality 6 · Reproducibility 6 · Composite 18/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: public, code: unknown).
