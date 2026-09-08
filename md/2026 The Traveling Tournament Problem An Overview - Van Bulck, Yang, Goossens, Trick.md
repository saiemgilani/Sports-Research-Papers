<!-- source: 2026 The Traveling Tournament Problem An Overview - Van Bulck, Yang, Goossens, Trick.pdf -->
<!-- arXiv:2609.03612, 3 Sep 2026 · text extracted from the arXiv PDF (open access) -->
<!-- weekly research roundup add, 2026-09-08 -->

# The Traveling Tournament Problem: An Overview

**David Van Bulck** (Ghent University / FlandersMake@UGent), **Fan Yang** (Shanghai Normal University), **Dries Goossens** (Ghent University / FlandersMake@UGent), **Michael Trick** (Carnegie Mellon University in Qatar)

arXiv:[2609.03612](https://arxiv.org/abs/2609.03612), 3 September 2026. Dedicated to Dr. Kelly Easton, who co-introduced the TTP and passed away in February 2026.

## Abstract

Over the past 25 years, the Traveling Tournament Problem (TTP) has become one of the most extensively studied optimization problems in sports scheduling. At its core, the TTP seeks to minimize the total travel distance incurred by teams that travel directly between opponents' venues during consecutive away games. The problem originated from the scheduling challenges faced by Major League Baseball, where it was identified as the central computational difficulty. This paper provides a comprehensive overview of the literature on the TTP. We review the principal problem variants and benchmark instances, and summarize the current state of the art in lower bounds, approximation guarantees, and exact and heuristic optimization algorithms. Moreover, we contribute to the continued development of the field by tracking and validating lower and upper bounds, while succeeding the repository originally established by Prof. Michael Trick as part of the RobinX sports timetabling project. Finally, we identify several open questions and outline promising directions for future research.

## Why it matters

The TTP is the operations-research canon problem for sports scheduling — introduced by Easton, Nemhauser & Trick (2001) directly out of MLB's real scheduling difficulties, and it has anchored 25 years of exact/heuristic optimization research since. This survey is written by, among others, Michael Trick himself (who originally established the field's benchmark-instance repository), so it functions simultaneously as a literature review *and* as the continuation/succession of the canonical reference benchmark set (RobinX) that the whole subfield validates results against — making it a load-bearing reference for anyone doing sports-scheduling optimization work, not merely a summary. It's a natural companion to the Colley Matrix and other scheduling/ranking-methodology papers already in this collection.

## What it covers

- **Problem variants and benchmark instances**: the principal formulations of TTP studied in the literature and the standard instance sets used to compare algorithms against each other.
- **State of the art across three solution families**: lower bounds (how good can any solution possibly be), approximation guarantees (heuristics with provable worst-case performance), and exact/heuristic optimization algorithms (what actually solves real or near-real-sized instances in practice).
- **An actively maintained, validated bound repository**: the paper explicitly positions itself as tracking and *validating* current best lower and upper bounds, succeeding Michael Trick's original RobinX-project repository — i.e., this isn't just descriptive, it's the field's living scoreboard.
- **Open problems and future directions**: an explicit research agenda for the next phase of TTP work.

## Assessment

**Novelty (4/10).** As a survey/overview rather than a new algorithm or empirical result, it scores lower on novelty by the collection's rubric (which measures originality of contribution) — but this undersells its field value; a survey by the field's own benchmark-keeper is closer to an infrastructure contribution than a typical review article.

**Practicality (7/10).** Directly useful to anyone building or evaluating a sports-schedule optimizer — league schedulers, researchers benchmarking a new heuristic, or analysts studying travel-distance/competitive-balance tradeoffs — as a single up-to-date entry point to 25 years of scattered literature and current best-known bounds.

**Reproducibility (8/10).** The paper's core secondary contribution *is* a validated, maintained public benchmark repository (the RobinX succession), which is about as reproducible as a reference work can be — the bounds and instances are the artifact, not just a description of them.

**Composite: 19/30.**

**Note on scoring convention.** This collection's rubric was built to score original empirical/methodological contributions; a survey/benchmark paper like this one is a different genre (closer to the Colley Matrix explainer already in the collection, which also scores lower on novelty despite being a foundational reference). Treat the composite here as "value as a reference and benchmark asset," not as a claim about original research contribution.
