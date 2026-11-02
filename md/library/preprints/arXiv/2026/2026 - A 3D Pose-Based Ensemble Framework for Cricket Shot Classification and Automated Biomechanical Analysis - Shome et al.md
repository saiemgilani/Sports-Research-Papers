<!-- source: 2026 - A 3D Pose-Based Ensemble Framework for Cricket Shot Classification and Automated Biomechanical Analysis - Shome et al.pdf -->
<!-- arXiv:2609.26923, 2026-09-22 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# A 3D Pose-Based Ensemble Framework for Cricket Shot Classification and Automated Biomechanical Analysis

**Sourav Shome, M. D. Ashiquzzaman Rahad, Rameswar Debnath**

arXiv:[2609.26923](https://arxiv.org/abs/2609.26923), submitted 2026-09-22.

## Abstract

Cricket is one of the most celebrated sports world-wide, and technological advancement has become deeply embedded in how the modern game is analyzed and coached. Cricket shot classification and automated performance analysis add a further dimension to this trend. Traditional approaches rely on RGB video features or static images, which are sensitive to environmental variations such as camera angle, lighting, and background clutter, and often fail to capture the underlying biomechanics of batting actions. In this paper, we propose a system to improve cricket coaching that takes raw video data, extracts batsmen from video frames using YOLO, and extracts 3D pose data from video frames using MeTRAbs. The system produces sequential skeletal pose data of 30 body points and captures the biomechanical features of a batsman. As part of the system, we also propose a deep learning ensemble for shot classification of four shots: flick, pull, defense, and drive. The ensemble performed well, compared to existing classification works, achieving 97.68% accuracy. In addition, we analyzed the misclassification rates to identify cases where shots were incorrectly classified and examined their possible causes. Our proposed system allows novice players to obtain useful feedback, such as important joint angles relative to expert batsmen, which can also be useful for injury prevention. The shot classifier also helps track class-wise shots over time for further analysis. In addition to novice players, coaches can use the system for player evaluation.

## Why it matters

Coaching-oriented pose pipeline; accuracy is on a self-collected dataset, so generalization is unproven.

## Triage score

Sport: Cricket · Novelty 5 · Practicality 5 · Reproducibility 5 · Composite 15/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: proprietary, code: unknown).
