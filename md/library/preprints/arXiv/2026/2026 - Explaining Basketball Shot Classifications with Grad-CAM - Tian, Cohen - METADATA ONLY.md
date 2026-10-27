<!-- METADATA-ONLY STUB. NO FULL TEXT HELD, BY DESIGN. -->
<!-- arXiv licence for this paper is the arXiv non-exclusive distribution licence, which does not grant redistribution; per the README rule on licensed files only the abstract and bibliographic record are stored. Read the PDF at https://arxiv.org/pdf/2610.33263 -->

# Explaining Basketball Shot Classifications with Grad-CAM: An Investigation of Shortcut Reliance with Spatiotemporal Correlations

**Hongyi Tian, Robin Cohen**

arXiv:[2610.33263](https://arxiv.org/abs/2610.33263) · 2026-10-27 ingest · licence: nonexclusive

## Abstract (arXiv-supplied)

Basketball action recognition is used in high-stakes scenarios to inform such tasks as specialized coaching, yet the evidence used by its deep-learning models is poorly understood. This paper investigates whether there is evidence that an R(2+1)D-18 model trained on the Basketball-51 dataset relies on spurious spatiotemporal correlations when classifying basketball shot outcomes. Gradient-weighted Class Activation Mapping (Grad-CAM) was used to generate spatiotemporal saliency maps, whose faithfulness was evaluated by progressively blurring the most salient pixels. Twenty saliency maps were then visually reviewed for recurring salient regions. Grad-CAM highlighted spatially central regions of clips including the shooter, net, and occasionally the courtside crowd. Blurring interventions were conducted to support these patterns. Blurring the central region resulted in an accuracy of 43.7%, compared to the original test accuracy of 69.3% and random-blurred accuracy of 50.9%. The additional 7.2 percentage-point reduction from central blurring compared to random blurring suggests that the model relies on task-relevant visual regions; this highlights the need for continual audits to ensure trustworthy, equitable sports analytics.

## Analysis (N/P/R = 5/4/6 = 15/30)

Small, explicit, and honest about limits (20 maps reviewed by eye, one model, one dataset). Worth keeping as a template for faithfulness testing via progressive blurring. Interpretation caution: the drop from central blurring (43.7%) vs random blur (50.9%) is a 7.2 pt gap on one model; it supports 'relies on the centre' but not 'relies on spurious cues'. Practical value to a public-data analyst is low; no tracking-free pipeline to reuse.

Summary: Grad-CAM on an R(2+1)D-18 shot-outcome classifier (Basketball-51): blurring the central region drops accuracy 69.3% to 43.7% vs 50.9% for random blur, suggestive but not conclusive evidence of shortcut reliance; 20 saliency maps reviewed.
