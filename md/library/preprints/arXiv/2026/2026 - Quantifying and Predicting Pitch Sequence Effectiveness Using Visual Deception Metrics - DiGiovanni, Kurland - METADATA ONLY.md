<!-- METADATA-ONLY STUB. NO FULL TEXT HELD, BY DESIGN. -->
<!-- arXiv licence for this paper is the arXiv non-exclusive distribution licence, which does not grant redistribution; per the README rule on licensed files only the abstract and bibliographic record are stored. Read the PDF at https://arxiv.org/pdf/2610.35714 -->

# Quantifying and Predicting Pitch Sequence Effectiveness Using Visual Deception Metrics

**Joe DiGiovanni, Justin Kurland**

arXiv:[2610.35714](https://arxiv.org/abs/2610.35714) · 2026-10-27 ingest · licence: nonexclusive

## Abstract (arXiv-supplied)

Pitcher performance is influenced not only by individual pitch characteristics, but also by the relationship and sequencing between consecutive pitches. In this study, we construct a sequence-level framework using MLB Statcast data from 2021-2025 to quantify the value of pitch deception with two geometric features: Decision Angular Separation (DAS) and Average Angular Separation (AAS). These metrics measure visual similarity of back-to-back pitches from the batter's perspective at a hitter's swing "decision point" during the flight of the ball from the pitcher's hand to the plate. We introduce Swinging Strike Lift (SwStr Lift), a residualized outcome isolating sequencing value beyond player identity, pitch type, location, and count. Across more than 740,936 two-pitch sequences, we find that tighter tunnels (low DAS/AAS) produce significant behavioral changes, for well-tunneled FB-to-BR (fastball-to-breaking-ball) sequences in the Shadow/Chase regions. This elevated swing propensity is consistent with swing induction as a primary behavioral pathway underlying the observed gains in swinging strikes. Our predictive modeling confirms the importance of tunneling, as adding DAS/AAS to gradient-boosted models yields substantial relative improvements in out-of-sample R-squared (e.g., +38% for FB-to-BR and +163% for FB-to-OS [fastball-to-off-speed]). These results demonstrate that tunneling generates a measurable and behaviorally coherent sequencing advantage, offering a tractable, perceptually grounded tool for evaluating pitcher deception which informs pitch design and game strategy. Quintile analyses confirm the effect is not confined to extreme tunnels; ICE plots show model-predicted lift declining sharply as DAS increases. Keywords: pitch tunneling; pitch sequencing; baseball analytics; predictive modeling; XGBoost; perceptual geometry; decision point; Statcast

## Analysis (N/P/R = 7/7/8 = 22/30)

Strongest of the batch for a public-data practitioner. Data is the public Statcast CSV via pybaseball (the same surface sportsdataverse-py wraps under `mlb_statcast_*`), so the whole study is rebuildable. The methodological care is the point: SwStr Lift is a *residual* against a Pitcher x Pitch Type x Zone x Count baseline, so sequencing is not confused with pitcher quality; the extreme-group test, quintile check and ICE plots all agree. Caveats: observational, effect on swinging strikes (not run value), no code released, and the +163% R2 gain is relative to a tiny base R2 (the paper itself notes R2 is capped for a continuous target against a discrete outcome).

Summary: Statcast 2021-25 pitch-tunneling framework: angular-separation metrics (DAS/AAS) at the batter decision point plus residualised SwStr Lift; adding DAS/AAS lifts out-of-sample R2 +38% (FB->BR) and +163% (FB->OS).
