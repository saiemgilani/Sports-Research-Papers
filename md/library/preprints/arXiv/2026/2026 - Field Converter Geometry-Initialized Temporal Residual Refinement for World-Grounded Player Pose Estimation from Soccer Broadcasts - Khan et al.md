<!-- source: 2026 - Field Converter Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts - Khan et al.pdf -->
<!-- arXiv:2609.10498, 2026-09-09 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-03 -->

# Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts

**Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte**

arXiv:[2609.10498](https://arxiv.org/abs/2609.10498), submitted 2026-09-09.

## Abstract

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.
