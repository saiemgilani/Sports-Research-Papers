<!-- source: 2026 Unified Pitch Graphs for Diagnosing Pitching Strategy - Lee, Ko.pdf -->
<!-- arXiv:2609.03810, 3 Sep 2026 · text extracted from the arXiv PDF (open access) -->
<!-- weekly research roundup add, 2026-09-08 -->

# Unified Pitch Graphs for Diagnosing Pitching Strategy

**Kichang Lee, JeongGil Ko** — Yonsei University

arXiv:[2609.03810](https://arxiv.org/abs/2609.03810), 3 September 2026.

## Abstract

Pitching strategy in baseball is expressed through both physical execution and the ordered context in which pitches are used, yet common representations collapse pitches into discrete types or aggregate statistics. We present Unified Pitch Graphs (UPG), a hierarchical graph representation for retrospective analysis of sequential spatiotemporal events. UPG preserves each pitch as an exact event with reconstructed three-dimensional trajectory and context, connects consecutive pitches through directed sequence edges, and organizes the same events across semantic and temporal resolutions. A support-adaptive mechanism backs off from fine, long sequences when repeated evidence is insufficient, while retaining exact event lineage. We evaluate UPG on 3.94 million MLB Statcast pitches from 2021–2026. Nominally identical pitch sequences exhibit distinct physical executions, and ordered structure becomes increasingly evident in longer context-conditioned paths. Support-adaptive backoff increases held-out path coverage from 18.9% to 94.9% while improving execution reconstruction from R² = 0.495 to 0.685. UPG also reliably localizes controlled execution changes that discrete pitch-mix and sequence representations cannot detect. These results demonstrate that UPG provides a traceable, multi-scale representation for identifying recurring strategy patterns without conflating retrospective associations with causal or future-performance claims.

## Why it matters

Most public pitch-sequencing analysis (pitch-mix tables, Markov-chain type-to-type transition matrices) discards exactly the information this paper argues matters: two "fastball → slider" sequences are not interchangeable if the fastball's actual release point, velocity, and location differed. UPG keeps the full continuous trajectory attached to every node in the sequence graph instead of quantizing to a pitch-type label first, which is a genuinely different representational choice from prior pitch-sequencing work — and the paper is explicit that it is a *descriptive/diagnostic* tool, not a forecasting or causal-inference model, which is the right level of claim for what a graph representation alone can support.

## Method, in brief

- **Representation**: each pitch is a node carrying its reconstructed 3D trajectory and game context; directed edges connect consecutive pitches within an at-bat/sequence; the same underlying events are simultaneously indexed at multiple semantic (pitch-type granularity) and temporal (sequence-length) resolutions — a genuine hierarchy, not a single flat graph.
- **Support-adaptive backoff**: the core engineering contribution. Long, fine-grained sequence paths are frequently unique (no other instance in the data shares that exact multi-pitch history), which would normally force either discarding rare paths or coarsening everything uniformly. Instead, UPG backs off *locally* — only for paths without enough repeated evidence — while keeping the exact event lineage intact for paths that do have support. This lifted held-out path coverage from 18.9% to 94.9%, a large practical gain, and R² for reconstructing execution characteristics from 0.495 to 0.685.
- **Data**: 3.94 million MLB Statcast pitches, 2021–2026 — a genuinely large, multi-season sample.
- **Validation approach**: shows nominally identical pitch-type sequences have measurably distinct physical executions (motivating the trajectory-preserving design), and that UPG localizes known/controlled execution changes that discrete pitch-mix and sequence representations miss — a targeted-intervention style validation rather than a single aggregate accuracy number.

## Assessment

**Novelty (7/10).** The specific combination — exact trajectory preservation at the node level, directed sequence structure, multi-resolution indexing, and a locally adaptive (rather than globally uniform) backoff mechanism for the sparse-long-sequence problem — is a genuinely new representation design for this data type, even though graph-based sports representations and Markov pitch-sequencing models both have prior art individually.

**Practicality (6/10).** Useful for a pitching coach or analyst doing retrospective diagnosis ("did this pitcher's slider shape change after inning 5," "is this sequence pattern actually new or a relabeling artifact") — the localization-of-execution-changes result is the most directly actionable piece. Less immediately useful as a plug-and-play metric or leaderboard stat; it's an analysis framework more than a single number a team could adopt tomorrow.

**Reproducibility (5/10).** Statcast pitch-tracking data (release point, movement, location) is publicly queryable via Baseball Savant, so the underlying data is accessible in principle, though assembling 3.94M pitches at this granularity requires nontrivial scraping/ETL work, and the paper does not indicate a code release for the graph-construction pipeline itself.

**Composite: 18/30.**

**Caveats.** The paper is careful to frame its findings as retrospective/associational and explicitly disclaims causal or future-performance claims — worth preserving that framing rather than treating "UPG localizes execution changes" as evidence the method could forecast pitcher decline or predict future strategy shifts, which is not what was tested.
