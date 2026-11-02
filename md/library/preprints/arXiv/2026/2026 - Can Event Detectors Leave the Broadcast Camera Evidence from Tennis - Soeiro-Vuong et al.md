<!-- source: 2026 - Can Event Detectors Leave the Broadcast Camera Evidence from Tennis - Soeiro-Vuong et al.pdf -->
<!-- arXiv:2610.38042, 2026-10-27 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-02 -->

# Can Event Detectors Leave the Broadcast Camera? Evidence from Tennis

**David Soeiro-Vuong, Andre-Louis Rochet**

arXiv:[2610.38042](https://arxiv.org/abs/2610.38042), submitted 2026-10-27.

## Abstract

Ball bounces and racket hits are the events from which tennis statistics are derived, and on monocular video the two are easy to confuse. We release a benchmark of 345 bounce and hit annotations at frame level on eight clips that mix broadcast, fixed elevated, phone and court-level viewpoints, with a frozen development and test split, a confusion-aware matcher, clip-level bootstrap intervals and a blind second annotation of three clips. On it we score supervised precise spotters with published broadcast weights, two zero-shot vision-language models, and RallyArb, an arbitration layer over a ball track and player poses that fits no parameter on event labels. The supervised spotters score near-perfectly on broadcast footage and almost nothing on phone and court-level footage, where the pooled bounce F1 of E2E-Spot is 0.130. RallyArb keeps a bounce F1 above 0.8 on the three phone and court-level clips, two of which were used to tune it, and finds 8 of 11 bounces on the held-out one, but it places hits too far from the contact frame to match human timing. The vision-language models detect events on every viewpoint and miss the contact frame by about 0.1 s. Fine-tuned leave-one-clip-out from its broadcast weights, the spotter reaches about 0.8 bounce F1 on two phone and court-level clips and stays at 0.2 on a grazing phone angle. The annotations, the evaluator and the frozen predictions of every scored row are released.

## Why it matters

Shows event detectors trained on broadcast footage do not transfer to phone or court-level video, and releases annotations, evaluator and frozen predictions so the claim can be rerun.

## Triage score

Sport: Tennis · Novelty 6 · Practicality 6 · Reproducibility 8 · Composite 20/30 (abstract-level triage with the rubric in `paper-ranking-report.md`; data: public, code: yes).
