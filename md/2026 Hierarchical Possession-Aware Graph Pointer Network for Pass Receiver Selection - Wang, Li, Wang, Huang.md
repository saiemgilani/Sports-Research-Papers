<!-- source: 2026 Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection - Wang, Li, Wang, Huang.pdf -->
<!-- arXiv:2609.04803, 4 Sep 2026 · text extracted from the arXiv PDF (open access) -->
<!-- weekly research roundup add, 2026-09-08 -->

# Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection

**Jingyi Wang, Da Li, Kaixin Wang, Zhangqin Huang** — Beijing Engineering Research Center for IoT Software and Systems / Beijing Key Laboratory of Interdisciplinary Intelligent Technologies in Sports Medicine and Engineering, Beijing University of Technology

arXiv:[2609.04803](https://arxiv.org/abs/2609.04803), 4 September 2026.

## Abstract

Pass receiver selection is a fundamental task in football analytics, aiming to predict the intended receiver under a given game state. This task is challenging with event-centered freeze-frame observations, a broadcast-like setting that provides only partial and variable player visibility without complete trajectories or stable player identities. The model must therefore reason over anonymous visible candidates, opponent pressure, and recent context under partial observation. To address this setting, we propose a Hierarchical Possession-aware Graph Pointer Network (HPGPN), which formulates pass receiver selection as variable-size candidate prediction over visible teammates. HPGPN jointly models current player interactions, local event context, and possession-level temporal dynamics. It represents the current pass situation with a graph, incorporates fixed event context, and uses dynamic possession history to capture how the attacking sequence evolves. Candidate representations are refined hierarchically by integrating spatial, contextual, and historical evidence, and a glimpse pointer head scores the receiver candidates. Experiments on public football event and freeze-frame data show that HPGPN improves pass receiver selection performance. Ablation studies demonstrate the effectiveness of graph-based interaction modeling, fixed event context, and dual-branch dynamic possession-history modeling.

## Why it matters

Optical/tracking-data-based pass models (which see every player's continuous trajectory) are proprietary and expensive; the "freeze-frame" event data this paper targets (visible-only players at the moment of the pass, no stable player IDs, no full trajectories) is the format that public and semi-public soccer event datasets (e.g., StatsBomb open data-style freeze frames) actually ship. A model designed explicitly for that broadcast-like partial-observation setting — rather than assuming full tracking access — is more directly usable by analysts and clubs without an optical tracking contract, which is the paper's most practically relevant framing choice.

## Method, in brief

- **Task framing**: pass receiver selection as *variable-size candidate prediction* over only the teammates visible in a given freeze frame — the candidate set changes size and composition play to play, which rules out a fixed-output-dimension classifier and motivates the pointer-network approach (scoring/selecting over a variable candidate set rather than predicting into a fixed label space).
- **Architecture (HPGPN)**: (1) a graph over the current pass situation capturing player-to-player spatial interactions, (2) fixed event context (the specifics of what "fixed" context means — score state, phase of play, etc. — are detailed in the full paper), (3) a dynamic possession-history branch tracking how the current attacking sequence evolved leading up to this pass, and (4) hierarchical refinement of candidate representations combining spatial, contextual, and historical evidence, scored by a "glimpse" pointer head (an attention-refinement step before final candidate scoring, a technique from the pointer-network literature).
- **Evaluation**: public football event and freeze-frame data; ablations isolate the contribution of graph-based interaction modeling, the fixed event context, and the dual-branch possession-history modeling — each ablation reportedly degrades performance, supporting the architecture's component choices.

## Assessment

**Novelty (6/10).** Pointer networks and graph neural networks have each been applied to soccer pass-related tasks before; the specific contribution here is the *combination* tailored to the anonymous-partial-visibility freeze-frame setting plus the dual-branch possession-history component, which is a solid but incremental architectural advance rather than a new problem formulation.

**Practicality (5/10).** Directly usable by analysts working from public/semi-public event-and-freeze-frame data rather than requiring an optical tracking contract, which is a real practical advantage — but as published this is a research architecture with ablation-study validation, not yet packaged as a metric or tool an analyst could drop into a workflow.

**Reproducibility (5/10).** Trained/evaluated on "public football event and freeze-frame data" (very likely a StatsBomb-style open dataset, consistent with the field's common practice, though the specific dataset name should be confirmed against the full paper), which is a meaningfully more reproducible starting point than proprietary tracking data — but no code release is indicated, and reconstructing this specific hierarchical architecture from the paper description alone would take real engineering effort.

**Composite: 16/30.**

**Caveats.** As with most single-paper architecture results, "HPGPN improves pass receiver selection performance" should be read as *relative to the baselines and dataset tested*, not as an established state of the art across all soccer event datasets — worth checking the full paper's baseline comparisons and dataset details before citing a specific accuracy figure.
