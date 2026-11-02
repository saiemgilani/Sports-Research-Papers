<!-- source: 2026 - Deep Learning Based Illegal Bowling Action Detection - Sutradhar et al.pdf -->
<!-- arXiv:2610.07223, 2026-10-05 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# Deep Learning Based Illegal Bowling Action Detection

**Debopom Sutradhar, Niful Islam, Sudipto Mondal, Tasmima Hossain Jamim, Jubaer Muhammad Shufol, Swakkhar Shatabda**

arXiv:[2610.07223](https://arxiv.org/abs/2610.07223), submitted 2026-10-05.

## Abstract

Cricket, often referred to as the "gentleman's game," adheres to a strict rule set for both batsmen and bowlers, where each delivery can significantly impact the match outcome. Detecting illegal bowling actions is crucial for maintaining fair play, yet it remains challenging for umpires to monitor in real time. Existing sensor-based solutions have limitations in live match scenarios, making real-time assessment difficult. This paper proposes a computer vision-based deep learning solution to detect illegal bowling actions in live cricket matches. To develop and evaluate our approach, we compiled a dataset of 62 videos featuring 11 male bowlers, capturing both legal and illegal bowling actions from multiple angles-front, back, and side. However, the dataset predominantly comprises right-handed bowlers with conventional actions. The proposed system identifies two key frames, the shoulder frame and the release frame from video footage of a bowler's delivery and analyzes the change in the bowling arm's angle between these frames. If the angle difference exceeds a predefined threshold (e.g., 15 degrees), the delivery is flagged as potentially illegal. We evaluated the system on a custom dataset and achieved a high true positive rate, suggesting the system's potential effectiveness in real-time match settings. However, further research is required to validate the system across diverse environmental conditions and larger datasets to ensure generalizability and robustness in various live match scenarios. To the best of our knowledge, this is the first AI-based computer vision method for detecting illegal bowling actions in cricket.

## Why it matters

Tiny, mostly right-handed conventional-action dataset; authors themselves call for larger validation.

## Triage score

Sport: Cricket · Novelty 4 · Practicality 4 · Reproducibility 3 · Composite 11/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: proprietary, code: unknown).
