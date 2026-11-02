<!-- source: 2026 - Perceiving and Predicting Dynamic Sports Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video - Braicu et al.pdf -->
<!-- arXiv:2610.37619, 2026-10-27 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video

**Tudor Braicu, Joseph DelPreto, Jared Boyer, Mónika Farsang, Maximilian Stölzle, Tim Niklas Seyde, Daniela Rus**

arXiv:[2610.37619](https://arxiv.org/abs/2610.37619), submitted 2026-10-27.

## Abstract

Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these capabilities, particularly from a moving egocentric camera, which is a natural view for robots. To investigate this, we collect an annotated tennis dataset and train a suite of vision models on spatiotemporal tasks. Our dataset contains egocentric video synchronized with five allocentric videos, estimated global positions, labeled contact times, and annotated stroke types. We then evaluate seven prediction tasks from egocentric images: 2D ego player and 3D ball localization, future player and ball trajectories, forehand or backhand stroke anticipation, time to the next ego player ball contact, and 3D ball position at that contact. We compare image encoders, video encoders, and vision-language models with jointly trained prediction heads. The best performing models achieve mean current-frame localization errors of 0.14 m for the ego player and 0.54 m for the ball, future forecasting errors of 0.34 m for the ego player and 0.91 m for the ball over 1.1 s, and a mean contact-time prediction error of 0.14 s. Auxiliary depth information substantially improves 3D ball localization, suggesting that inferring metric depth remains a challenge. Longer image histories do not improve ball forecasting, indicating that representations exploit scene context rather than rely solely on inter-frame motion. Finally, we propose a conditional diffusion model to generate whole-body kinematic tennis motion from vision encoder predictions on egocentric video at real-time rates, adapting movements as predictions are refined. These results move towards a deeper understanding of how foundation vision models can support real-time dynamic robots using egocentric video.

## Why it matters

Robotics-oriented; value to analysts is the benchmark of foundation vision models on a moving camera, not a stats method.

## Triage score

Sport: Tennis · Novelty 6 · Practicality 3 · Reproducibility 5 · Composite 14/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: public, code: unknown).
