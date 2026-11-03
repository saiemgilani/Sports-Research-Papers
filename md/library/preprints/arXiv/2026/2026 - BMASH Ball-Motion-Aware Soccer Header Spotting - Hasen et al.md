<!-- source: 2026 - BMASH Ball-Motion-Aware Soccer Header Spotting - Hasen et al.pdf -->
<!-- arXiv:2609.39300, 2026-09-30 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-03 -->

# BMASH: Ball-Motion-Aware Soccer Header Spotting

**Ahmed Endris Hasen, Muhammad Shahzad Khan, Nikolaos Passalis, Jenni Raitoharju**

arXiv:[2609.39300](https://arxiv.org/abs/2609.39300), submitted 2026-09-30.

## Abstract

Recent advances in computer vision have made broadcast sports videos increasingly useful for event analysis, performance assessment, and player-safety applications. In soccer, however, header spotting remains a challenging problem due to the subtle and short-lived nature of header events. This paper focuses on soccer header spotting: identifying moments in broadcast videos where the ball contacts a player's head. We first adapt and evaluate Video Swin as a strong action-recognition baseline for this task, and then introduce BMASH, a ball-motion-aware fusion framework that integrates detector-derived ball features. BMASH combines Video Swin action representations with ball-presence and motion features from frame-level soccer-ball detection, integrating player-action context with ball dynamics to distinguish headers from visually similar events. We evaluate BMASH using game-level splits with separate test matches and rotating validation folds, considering both centered-window classification and continuous full-video spotting. Results show that Video Swin provides a strong baseline for header spotting, while BMASH improves clip-level AP and ROC-AUC over the corresponding Video Swin baseline. In continuous full-video spotting, BMASH achieves a comparable event-level F1-performance with a different precision--recall trade-off.
