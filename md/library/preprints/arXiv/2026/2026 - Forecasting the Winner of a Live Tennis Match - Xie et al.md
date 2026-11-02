<!-- source: 2026 - Forecasting the Winner of a Live Tennis Match - Xie et al.pdf -->
<!-- arXiv:2609.07617, 2026-09-07 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# Forecasting the Winner of a Live Tennis Match

**Charles Xie, Aneesh Muppidi**

arXiv:[2609.07617](https://arxiv.org/abs/2609.07617), submitted 2026-09-07.

## Abstract

With the rise of live sports betting in recent years, tennis forecasting has expanded from pre-match prediction to models that update win probabilities as a match unfolds. A central challenge in creating such a model is the constant need for models to adapt to score and performance changes. This study examines how pre-match and live information can be most effectively integrated into a model to produce accurate win-probability estimates. The analysis uses 8,222 Grand Slam matches containing a total of 1,505,355 points. Five models were evaluated using a chronological split, with matches from 2011-2021 used for training, 2022 for validation, and 2023-2024 for testing. Trace, a hybrid model, achieved accuracies of 76.06%, 82.15%, and 88.34% at 25%, 50%, and 75% match progress, suggesting that hybrid modeling is a practical approach to live tennis forecasting.

## Why it matters

Chronological split and point-level Grand Slam data make it a usable live-WP baseline for tennis, the analogue of the football/basketball WP models in sdv-py.

## Triage score

Sport: Tennis · Novelty 5 · Practicality 7 · Reproducibility 6 · Composite 18/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: public, code: unknown).
