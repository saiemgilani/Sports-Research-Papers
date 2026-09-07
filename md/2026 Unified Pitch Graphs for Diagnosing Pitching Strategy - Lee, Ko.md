<!-- source: 2026 Unified Pitch Graphs for Diagnosing Pitching Strategy - Lee, Ko.pdf -->
<!-- arxiv: https://arxiv.org/abs/2609.03810 -->

Unified Pitch Graphs for Diagnosing Pitching Strategy Kichang Lee

JeongGil Ko

kichang.lee@yonsei.ac.kr Yonsei University

jeonggil.ko@yonsei.ac.kr Yonsei University

arXiv:2609.03810v1 [cs.IR] 3 Sep 2026

Abstract

resolution trade-off. Coarse representations based on pitch types or broad transition categories are compact and well supported, yet they collapse physically distinct executions. Conversely, defining states jointly by trajectory, location, context, and longer pitch histories quickly fragments the representation into sparsely repeated patterns, reflecting the general trade-off between longer sequential contexts and reliable statistical support [3, 15]. Aggregate representations may also obscure the exact games, plate appearances, and physical pitches that support a discovered pattern. The central challenge is therefore not simply to construct a pitch graph, but to preserve physical fidelity and event lineage while maintaining sufficient support for recurring multi-scale patterns. To address these limitations, we propose UPG (Unified Pitch Graph), a hierarchical graph framework for large-scale analysis of sequential spatio-temporal pitching events. First, UPG preserves each pitch as an exact event with its continuous physical execution, rather than replacing it with a coarse pitch-type state. Second, it organizes these events across pitch type, trajectory, location, and temporal scales while retaining links to the original pitches and plate appearances. Third, to avoid the sparsity caused by long or highly detailed sequences, UPG adaptively backs off to shorter or coarser paths when repeated support is insufficient. Together, these components allow recurring pitching patterns to be analyzed at a supported resolution without discarding the physical events from which they were constructed. We evaluate UPG on 3.94 million MLB Statcast pitches from 2021 through a partial 2026 season [1]. Our experiments show that nominally identical discrete sequences can contain distinct physical executions, and that meaningful ordered structure becomes more evident in longer context-conditioned paths. Support-adaptive backoff increases held-out path coverage from 18.9% to 94.9% while improving execution reconstruction from 𝑅 2 = 0.495 to 0.685. We further show that the resulting hierarchy can localize execution changes that pitch-mix and discrete sequence representations cannot detect, while preserving direct lineage from aggregate findings to their supporting games, plate appearances, and individual pitches. We note that these results position UPG as a graph-based diagnostic representation for data-rich sequential event analysis rather than as a causal or future-performance prediction model. Our contributions are as follows: • We formulate pitching-strategy diagnosis as a large-scale sequential graph problem that jointly considers physical execution, observed pitch order, game context, and temporal scope. • We propose UPG, a hierarchical attributed graph that preserves exact pitch events and sequence relations while organizing them through semantic/temporal resolutions with full event lineage. • We develop a support-adaptive variable-order representation that balances fine-grained physical fidelity against the sparsity of long and highly specific strategy paths.

Pitching strategy in baseball is expressed through both physical execution and the ordered context in which pitches are used, yet common representations collapse pitches into discrete types or aggregate statistics. We present Unified Pitch Graphs (UPG), a hierarchical graph representation for retrospective analysis of sequential spatiotemporal events. UPG preserves each pitch as an exact event with reconstructed three-dimensional trajectory and context, connects consecutive pitches through directed sequence edges, and organizes the same events across semantic and temporal resolutions. A support-adaptive mechanism backs off from fine, long sequences when repeated evidence is insufficient, while retaining exact event lineage. We evaluate UPG on 3.94 million MLB Statcast pitches from 2021–2026. Nominally identical pitch sequences exhibit distinct physical executions, and ordered structure becomes increasingly evident in longer context-conditioned paths. Support-adaptive backoff increases held-out path coverage from 18.9% to 94.9% while improving execution reconstruction from 𝑅 2 = 0.495 to 0.685. UPG also reliably localizes controlled execution changes that discrete pitch-mix and sequence representations cannot detect. These results demonstrate that UPG provides a traceable, multi-scale representation for identifying recurring strategy patterns without conflating retrospective associations with causal or future-performance claims.

1

Introduction

Baseball is one of the most data-rich domains in modern sports analytics, with a long tradition of quantitative analysis and increasingly detailed tracking of individual plays [12]. Modern pitch-tracking systems record millions of pitches with release conditions, velocity, movement, three-dimensional flight, plate location, game context, and batter response. Such data provide an opportunity to study not only player outcomes, but also the sequential physical patterns associated with those outcomes Pitching is particularly well suited to this type of analysis since each pitch is both a physical execution and an action within an ordered interaction. The strategic meaning of a pitch depends not only on its nominal type, but also on how it is executed, what preceded it, and the context in which it is thrown. For example, two fastballs with the same pitch-type label may differ substantially in velocity, movement, release path, and trajectory, while the same fastball– breaking-ball sequence may have different effects depending on count, matchup, location, and the physical relationship between the two pitches [10, 14]. Thus, pitching strategy is naturally relational: individual pitch events are connected through observed temporal order and embedded in multiple contextual and temporal scopes. Graph representations provide a natural way to model such sequential structure, and prior work has used directed graphs to capture pitch-order dependencies beyond independent pitch selection [14]. However, graph construction introduces an important 1

Conference’17, July 2017, Washington, DC, USA

Kichang Lee and JeongGil Ko

• Using large-scale MLB tracking data, we demonstrate that UPG reveals execution and ordered structure lost by discrete representations and supports traceable multi-scale diagnosis and retrospective change localization.

or path length can recover specificity, but at the cost of rapidly decreasing statistical support. Trajectory and outcome analysis. PITCHf/x and Statcast enable detailed characterization of release position, velocity, movement, location, and pitch flight [7, 9], while pitch-tunneling analyses examine how consecutive pitches converge and diverge through flight [10]. Pitch-level models additionally estimate effectiveness from pitch type, physical execution, location, and game state [6]. These approaches capture complementary aspects of pitching, but trajectory geometry or outcome prediction alone does not expose the recurring ordered structures and temporal contexts through which an execution acquires strategic meaning.

2 Background and Problem Formulation 2.1 Pitching as Sequential Event Data A plate appearance (PA) is a variable-length interaction in which a pitcher selects and executes an ordered sequence of pitches against a batter. Each pitch is simultaneously a strategic decision, a physical action, and an observed event whose meaning depends on its nominal type, physical execution, preceding pitches, and game context. We represent the 𝑖-th pitch event as 𝑒𝑖 = (𝑠𝑖 , 𝑟𝑖 , 𝑐𝑖 , 𝑜𝑖 ), where 𝑠𝑖 denotes nominal pitch identity, 𝑟𝑖 continuous physical execution, 𝑐𝑖 information available before the pitch, and 𝑜𝑖 post-pitch annotations. Physical execution includes release conditions, velocity, movement, reconstructed three-dimensional trajectory, and plate location; context includes count, handedness matchup, baseout state, inning, and score situation; and post-pitch annotations include batter response, contact quality, and run-value change. Outcomes describe what followed an execution but do not determine pitch identity: nominally identical pitches may follow different trajectories and produce different responses, while similar outcomes may arise from different physical and sequential mechanisms. A plate appearance is an ordered sequence 𝑃 = (𝑒 1, 𝑒 2, . . . , 𝑒𝑇 ), where 𝑇 varies across plate appearances. Consecutive valid events define observed pitch-to-pitch relations, and these local sequences are nested within games and longer temporal windows. Pitchtracking data are therefore naturally hierarchical spatio-temporal event data rather than independent rows. This structure creates a resolution trade-off: coarse states such as pitch type are compact and repeatedly observed but collapse within-type physical variation, whereas adding trajectory, location, context, and longer pitch histories rapidly fragments the state space. A useful representation must therefore preserve the underlying physical events while adapting the resolution at which recurring sequence structure is summarized.

2.2

Positioning of UPG. As summarized in Table 1, existing approaches typically capture only a subset of sequence structure, physical execution, context, outcome pathways, and event-level traceability. Sequence models emphasize order, trajectory analyses physical execution, and outcome models effectiveness. UPG addresses the representation problem that arises when these elements must be analyzed jointly at scale: it preserves exact physical events and observed sequence relations while supporting semantic and temporal aggregation, event-level traceability, and multi-scale diagnosis without forcing every analysis into a single fixed state space. Our focus is therefore on representations that preserve explicit sequence structure and recoverable supporting events. Predictive sequence encoders optimize a different objective, and UPG does not claim superiority as a predictive architecture.

2.3

Problem Formulation

Given pitch-tracking records for pitcher 𝑝 over analysis period 𝜏, let D𝑝,𝜏 = {𝑃 1, 𝑃2, . . . , 𝑃 𝑁 } denote the observed plate-appearance sequences. Our goal is to construct an attributed hierarchical graph 𝐺 𝑝,𝜏 = (𝑉 evt ∪𝑉 sem ∪𝑉 time, 𝐸 seq ∪𝐸 sem ∪𝐸 time ), where 𝑉 evt contains exact pitch events, 𝑉 sem semantic index nodes, and 𝑉 time temporalscope nodes. The corresponding edge sets encode observed pitch order, semantic membership, and temporal containment. The canonical object in 𝐺 𝑝,𝜏 is the exact pitch event. Continuous trajectory and plate location remain attached to each event rather than being replaced by a discrete state; semantic nodes provide alternative resolutions for aggregation and drill-down, while temporal nodes organize the same events across plate appearances, games, rolling windows, and seasons. Post-pitch outcomes remain annotations and are excluded from event identity and semantic state construction. Given 𝐺 𝑝,𝜏 , the primary diagnostic task is to identify recurring ordered patterns and characterize their execution, contextual use, temporal scope, and observed response pathways while retaining support and lineage to the underlying games, plate appearances, transitions, and pitches. Because highly detailed or long paths may occur only a few times, the most specific representation is not always statistically reliable. When repeated evidence is insufficient, the representation therefore backs off to a shorter or coarser description rather than elevating a nearly unique execution into a stable strategy pattern. Accordingly, UPG is designed around three requirements: event fidelity, so that exact physical executions and observed adjacencies

Related Work

Pitch prediction and strategic decision modeling. Pitch-prediction studies estimate the next pitch type or location from pitcher tendencies, batter information, count, and previous pitches [4, 5, 8, 18]. Reinforcement-learning, Markov-decision, and game-theoretic approaches further model pitch selection as a sequential decision problem [11, 16]. These studies establish that pitch choice depends on prior actions and context, but primarily target prediction or strategy optimization rather than retrospective organization of observed execution. Pitch sequences and graph representations. Pitch sequences have been studied through transition structures, recurring motifs, and directed graph representations [2, 13, 14]. Such models capture pitch order efficiently, but states are commonly defined by nominal pitch labels or other discrete categories, which may merge physically different realizations of the same sequence. Increasing state detail 2

Conference’17, July 2017, Washington, DC, USA

Table 1: Comparison of representative pitching analytics. ✓: explicitly modeled, ▲ : partially supported, ✗: not central. Study / line of work

Primary focus

Next-pitch prediction [4, 5, 8, 18]

Pitch-choice prediction

MDP / game-theoretic sequencing [11, 16]

Strategic pitch selection

Pitch tunneling / trajectory similarity [7, 10]

Pairwise pitch execution

Pitch-sequence graph / motif studies [13, 14]

Sequence-structure discovery

Pitch-value / outcome models [6]

Pitch-quality estimation

Counterfactual sequence optimization [17]

Strategy optimization

UPG (ours)

Pitching-strategy diagnosis

Sequence trans.

Trajectory

Context

Outcome pathways

Semantic hierarchy

Event traceability

Multi-scale diagnosis

✓ ✓ ▲ ✓ ✗ ✓ ✓

✗ ✗ ✓ ▲ ▲ ✗ ✓

▲ ✓ ✗ ▲ ▲ ✓ ✓

✗ ▲ ▲ ▲ ✓ ✓ ✓

✗ ✗ ✗ ▲ ✗ ▲ ✓

✗ ✗ ▲ ▲ ▲ ▲ ✓

✗ ✗ ✗ ▲ ✗ ✗ ✓

remain recoverable; support-adaptive resolution, so that sequence length and semantic detail reflect repeated evidence; and multiscale traceability, so that aggregate patterns remain connected to their temporal occurrences and underlying events. The objective is not causal identification or a universally superior predictive model, but a shared graph representation for support-aware, multiscale analysis of observed pitching strategy. Prediction and postexecution modeling are used only as auxiliary evaluations under task-specific information constraints. Section 3 describes how UPG instantiates these principles.

3

The edge preserves observed pitch order together with pairwise execution descriptors such as changes in velocity, release position, trajectory, late-flight separation, and plate location. Thus, nominally identical pitch-type transitions can remain distinguishable through their physical realizations. Invalid intermediate observations break the sequence rather than inducing an artificial adjacency. Exact events and their sequence edges form the canonical backbone of UPG. The semantic and temporal structures introduced below index and aggregate this backbone while retaining links to the original pitches.

3.2

System Design

UPG represents pitching strategy as a hierarchy over exact observed pitch events rather than as a graph with one fixed discrete state space. As illustrated in Figure 1, each pitch remains an individual PitchEvent with its continuous execution and pre-pitch context, while consecutive pitches within a plate appearance (PA) form directed sequence edges. Semantic links provide different levels of physical resolution, and temporal links organize the same events across PAs, games, rolling windows, and seasons. When detailed multi-pitch patterns lack sufficient repeated support, UPG backs off to a shorter or coarser representation without discarding the underlying physical events. The key distinction is between event fidelity and analytical resolution: the former preserves what physically occurred, whereas the latter determines how specifically a recurring pattern can be reported from the available evidence.

3.1

For each pitch, UPG reconstructs its three-dimensional flight from Statcast kinematic measurements: 1 (2) r𝑖 (𝑡) = r0,𝑖 + v0,𝑖 𝑡 + a𝑖 𝑡 2 . 2 The reconstructed curve is sampled at fixed locations along the flight path to obtain a compact trajectory representation. The sampled trajectory, release conditions, and continuous plate coordinates remain attached to the exact event throughout the analysis. Continuous execution is not replaced by a single discrete trajectory state. Instead, UPG provides semantic resolutions ranging from pitch type, through within-type trajectory and location refinements, to the exact event. These levels form an analytical index over the same pitches rather than a causal or generative hierarchy. A coarse view can therefore summarize repeated pitch-type transitions, while a finer view can reveal the physical executions and locations supporting those transitions. Trajectory variation is defined separately within each pitch type. Let e q𝑖 denote the standardized sampled trajectory of pitch 𝑖 under a historical reference distribution. For pitch type 𝑘, let u𝑘 be the first principal direction of the corresponding within-type trajectory distribution. We define q𝑖 . (3) 𝑧𝑖 = u𝑘⊤e

Exact Pitch Events and Sequence Relations

Following Section 2, each valid observed pitch 𝑖 corresponds to one event vertex 𝑣𝑖 with 𝑥𝑖 = [𝑠𝑖 , 𝑟𝑖 , 𝑐𝑖 ], where 𝑠𝑖 is nominal pitch identity, 𝑟𝑖 continuous physical execution, and 𝑐𝑖 pre-pitch context. The physical and contextual variables follow the definitions in Section 2. Post-pitch batter response, contact quality, and run-value variables are stored separately as annotations 𝑜𝑖 and do not determine event identity or semantic membership. The event is exact in the sense that it remains in one-to-one correspondence with an observed pitch rather than being replaced by a pitch-type node, trajectory centroid, or clustered state. For consecutive valid pitches 𝑖 − 1 and 𝑖 within the same PA, we add a directed sequence edge seq

𝑒𝑖

= (𝑣𝑖 −1, 𝑣𝑖 ).

Continuous Execution and Semantic Hierarchy

Frozen reference tertiles of 𝑧𝑖 define three trajectory strata, 𝑇 − , 𝑇 0 , and 𝑇 + . The standardization, projection, and thresholds are estimated before the diagnostic window and then held fixed, giving the strata a consistent meaning across time. They describe relative within-type trajectory variation rather than pitch quality or effectiveness. Plate endpoints are also associated with an interpretable location region, while their original continuous coordinates are retained. Game variables such as count, handedness, base-out state,

(1) 3

Conference’17, July 2017, Washington, DC, USA

1 Records

2 Trajectories

Kichang Lee and JeongGil Ko

PitchEvent Graph

3

4

Within a plate appearance (PA)

E1

E2

E3

𝐄𝐢

Release/velo

Sampled planes

Temporal+ Support -Adaptive

Pitch Type

Temporal Containment

… Trajectory Stratum

T0

T-

PitchEvent

𝐄𝐢

SupportAdaptive Backoff

6

Diagnostic Evidence Outcome-linked

Fine 04

Recurring

Coarse 04

Low-support

T+ PA

Location Region

Nominal identity FF / SL

Pitch type

5

E4 … E5

NEXT_IN_PA

Raw Pitch Records

Semantic Hierarchy

Fine 03

Continuous execution Traj + velo

Trajectory

Pre-pitch context Count / base-out

Plate location

Post-pitch annotation Swing / contact

Player Diagnostic

Game Coarse 03 Rolling Window

02

Count/matchup

Confidence

PitchEvent (exact)

…

outcome

Contact suppression Command & Location Sequencing / Deception Opponent Exploitation

Season

PitchEvent

Sequence Edge

Semantic Link

Temporal Containment

(node)

(NEXT_IN_PA)

(hierarchy)

(PitchEvent -> …-> Season)

Terminal

Strong Moderate Weak

Support-Adaptive Resolution (backoff ladder)

Figure 1: Overview of UPG. Exact pitch events preserve physical execution and within-plate-appearance order. Semantic and temporal hierarchies organize the same events at multiple resolutions, while support-adaptive paths balance sequence specificity with repeated evidence for multi-scale diagnosis.

3.4

inning, and score remain conditioning attributes rather than default semantic-state components. Crossing all physical and contextual variables into a single state would rapidly fragment recurring sequences; UPG instead preserves these variables while allowing the analytical resolution to vary independently.

Support-Adaptive Strategy Paths

Pairwise transitions capture immediate pitch order, but recurring pitching patterns may span longer sequences. UPG therefore considers paths of two to four consecutive pitches within a PA. For a length-𝑚 path ending at pitch 𝑖 under semantic resolution 𝑟 , 𝜋𝑖(𝑚,𝑟 ) = (𝜙𝑟 (𝑣𝑖 −𝑚+1 ), . . . , 𝜙𝑟 (𝑣𝑖 )) .

3.3

Multi-Scale Strategy Graphs

For example, a three-pitch path contains pitches 𝑖 − 2, 𝑖 − 1, and 𝑖 in their observed order, and paths never cross PA boundaries. Longer paths capture more sequential context, while trajectoryrefined states capture more physical specificity. Both reduce recurrence, creating a trade-off between descriptive detail and statistical support. UPG addresses this trade-off with support-adaptive variable-order selection. Each candidate path must satisfy both a minimum number of occurrences and a minimum number of distinct supporting games. At each path length, a trajectory-refined representation is considered before its pitch-type counterpart; if neither is supported, the procedure backs off to the next shorter suffix. If no multi-pitch candidate is supported, the target pitch type serves as the final fallback. Let R denote this ordered set of candidate representations. The selected representation is n     o 𝜌𝑖 = first (𝑚, 𝑟 ) 𝑛 𝜋𝑖(𝑚,𝑟 ) ≥ 𝑛 min, 𝑔 𝜋𝑖(𝑚,𝑟 ) ≥ 𝑔min , (6)

Pitching structure may be local to a PA, recur within a game, emerge over recent games, or characterize a season. UPG therefore links each exact event to its enclosing PA and game and organizes games into rolling windows and seasons. These temporal levels do not create new physical observations; they determine which events are summarized at a particular analytical scope. Let 𝜙𝑟 (𝑣𝑖 ) map exact event 𝑣𝑖 to its semantic state at resolution 𝑟 . For pitcher 𝑝 and temporal scope 𝜏, the weight of aggregate transition (𝑢, 𝑣) is

𝑝,𝜏,𝑟

𝑤𝑢𝑣

=

∑︁

I [𝜙𝑟 (𝑣𝑖 −1 ) = 𝑢, 𝜙𝑟 (𝑣𝑖 ) = 𝑣] ,

(5)

(4)

𝑖 ∈ T𝑝,𝜏

(𝑚,𝑟 ) ∈ R

where T𝑝,𝜏 contains valid within-PA transitions made by pitcher 𝑝 in scope 𝜏. Changing 𝑟 changes the physical resolution of the graph, while changing 𝜏 changes its temporal scope. Aggregate nodes and edges retain references to their constituent events and sequence edges. Their contexts, pairwise execution, and post-pitch annotations can therefore be summarized without losing event lineage. A season-level pattern can be localized to supporting games and PAs and then inspected as individual physical trajectories. Rolling-window analyses use only completed games available within the corresponding window.

where 𝑛(·) is occurrence support and 𝑔(·) is the number of distinct supporting games. Crucially, backoff changes the resolution of the statistical claim rather than the information stored in the graph. A path reported only at pitch-type resolution still retains the trajectories, locations, contexts, temporal occurrences, and exact sequence edges of all supporting pitches. Location and game context can therefore be used for conditioning and drill-down without being crossed into every default path identity. 4

Conference’17, July 2017, Washington, DC, USA

3.5

A

Diagnostic Evidence and Reporting

B Execution A · SL → SL → FF

Height z (ft)

The primary output of UPG is a retrospective diagnosis of recurring pitching structure. We use motif to denote a path that satisfies the recurrence criteria above and is reported as part of a pitcher-level analysis. A physically distinctive but rarely observed sequence remains inspectable, but is not treated as evidence of a stable recurring pattern. For each motif, UPG records its support across games, temporal distribution, contextual usage, physical execution, and exact event lineage. Post-pitch annotations are examined only after the structural motif has been defined, separating the existence of a recurring pattern from its observed effectiveness. Outcome comparisons also respect their relevant populations: whiff evidence is evaluated among swings, while contact-quality evidence is evaluated among balls put in play. When temporal validation is available, the direction of an observed outcome association is additionally checked outside the discovery observations. The resulting reports distinguish three levels of evidence. A recurring motif with a directionally consistent outcome association is reported as outcome-linked diagnostic evidence. A motif that recurs but has weak or unstable outcome differences remains a recurring strategy pattern without a strong effectiveness claim. A detailed execution without sufficient recurrence remains an event-level example rather than being promoted to a stable motif. These reporting levels change the strength of interpretation, not the underlying representation: every reported pattern remains traceable to its supporting games, PAs, sequence edges, and exact pitches. The resulting evidence is observational, and recurrence or held-out consistency does not establish causal effects or guarantee future persistence.

Execution B · SL → SL → FF

6

6

5

5

4

4

3

3 3

3

2

2

2 1

1 −2

−1

0

1

1

2

2 −2

Catcher-view x (ft)

C

−1

0

1 1

2

Catcher-view x (ft)

Order and context recurrence

Pitch attributes Directed edges Ordered 3-pitch paths Ordered 4-pitch paths Paths + context 0

2

4

6

8

10

Observed − order-shuffled similarity (×10⁻³)

Figure 2: Information retained beyond a discrete sequence. (A–B) Two executions assigned the same SGT pitch-type, zone, and count cell; numbers indicate pitch order. (C) Difference between observed cross-window recurrence and recurrence after shuffling pitch order within each PA. Error bars show bootstrap confidence intervals.

Our principal discrete comparator is the Sequence Graph Transform (SGT) [14], which summarizes ordered pitch-type or pitchtype–zone symbols within each plate appearance (PA). Where appropriate, we also compare pitch mix and fixed- versus variableorder path representations. For execution reconstruction, each supported path is represented by the mean continuous execution profile estimated from its training occurrences. We report 𝑅 2 between these path-level reconstructions and the exact execution profiles of heldout pitches; higher values indicate that the representation groups physically similar executions while retaining coverage. The evaluation proceeds from representation validity to support-adaptive aggregation, then to reliability and traceability, and finally to diagnostic case studies.

4 Evaluation 4.1 Evaluation Questions and Protocol We evaluate UPG around four questions that correspond directly to its design goals. RQ1: Representation fidelity. Does UPG preserve physical execution and ordered structure that are lost in discrete sequence representations? RQ2: Adaptive resolution. Can support-adaptive routing retain useful sequence detail without fragmenting the representation into unsupported paths? RQ3: Reliability and traceability. Are discovered motifs supported by repeated evidence across games, and can aggregate findings be traced back to exact supporting pitches? RQ4: Diagnostic utility. Does the resulting representation support meaningful retrospective analyses across changes, players, time, and context? We use 3.94 million MLB Statcast regular-season pitches from 2021 through July 3, 2026; the partial 2026 season is denoted 2026*. The primary evaluation population comprises the 300 pitchers with the largest valid 2025 workloads. Representation dictionaries, trajectory transformations, and support thresholds are estimated on earlier data and frozen before evaluation, and outcome variables never determine graph states. Unless stated otherwise, uncertainty is estimated by pitcher-cluster bootstrap. Player-facing trajectories use unmirrored Statcast coordinates in catcher’s view.

4.2

Representation Fidelity and Ordered Structure

This first experiment asks why a trajectory-aware sequence representation is needed at all. If a discrete pitch-sequence summary already preserves the relevant structure, then a more elaborate event-level graph would be unnecessary. We therefore test two points: whether physically different executions can collapse into the same discrete sequence cell, and whether meaningful sequence signal appears only at longer ordered contexts. Figure 2A–B gives a concrete collision example. The two sequences share the same discrete description (SL–SL–FF with the same zone/count cell), yet their trajectories are visibly different. The point of the example is not that every discrete cell is heterogeneous, but that discrete symbols can merge physically distinct executions that a strategy analysis may wish to separate. This directly motivates the exact-event design of UPG. 5

Conference’17, July 2017, Washington, DC, USA B 94.9%

80% 60% 40% 18.9%

20%

18.9%

0% C-F4

C-Var

A-F4

A-Var

Fine-4 Coarse-4

C

Fine-3 Coarse-3

A

0.686

0.685

Stable repeated

0.496

0.495

0.4 0.2 0.0 C-F4

C-Var

Fine-2 Coarse-2

Type-1

A-F4

A-Var

80%

42.2%

Coarse variable

19%

Adaptive fixed-4

16%

Adaptive variable

16%

0%

48.7%

56.3%

54.8% 80.7%

40% 57.5%

49.0%

50.9%

2022

2023

43.5%

45.2%

2024

2025

19.2%

0% 2026*

81%

40%

36%

81%

34%

20%

40%

9%

60%

27%

80%

100%

Validation routing (%)

Figure 3: Support and execution fidelity under four hierarchy variants. Coarse (C) uses pitch type, adaptive (A) permits qualified trajectory substates, F4 fixes every path at order four, and Var backs off through shorter suffixes. (A) Supported held-out paths. (B) Held-out execution reconstruction (𝑅 2 ). (C) Selected resolution and order for validation paths.

B

Top-10 retention

Outcome-direction retention

95.0%

90.0%

85.0%

80.0%

75.0% 2021

2022

2023

2024

2025

2026*

Figure 4: Cross-game reliability of the ten highest-support motifs for each pitcher and season. (A) Evidence class. (B) Retention of top-ten membership and pitcher-beneficial outcome direction after removing the motif’s highest-support game. The 2026* bar reflects a shorter observation window.

Figure 2C then asks whether pitch order itself carries information beyond the set of pitches thrown. We shuffle pitch order within each PA while preserving the observed events. The result is intuitive and important: shuffling has little effect on isolated event attributes or a single directed transition, but it clearly reduces recurrence for three-pitch, four-pitch, and context-conditioned paths. Thus, the relevant structure is not simply that one pitch followed another, but that longer ordered subsequences recur in non-random ways. Together, these results justify a representation that preserves both exact execution and multi-pitch sequence context.

4.3

50.7%

60%

20%

Leave-one-game-out retention (%)

19%

Episodic

0.6

2021 Coarse fixed-4

Limited evidence

100%

Top motifs (%)

94.9%

100%

Held-out execution R²

Supported paths (%)

A

Kichang Lee and JeongGil Ko

variable-order path as the statistical backbone. Figure 3C makes this operational: most validation paths are reported at coarse orders two to four, while only a smaller fraction are supported at fine trajectory-refined resolutions. The result is a representation that is both physically faithful and statistically usable.

4.4

Reliability, Confidence, and Multi-Scale Traceability

Once a representation can express recurring patterns, the next question is whether those patterns are trustworthy. A useful diagnostic motif should not be driven by a single game, and a season-level claim should remain traceable to the exact PAs and pitches that support it. This subsection therefore evaluates both reliability and traceability. Figure 4 asks whether top motifs remain visible after removing their single highest-support game. They largely do. Across full seasons, a substantial share of high-support motifs are classified as stable repeated patterns, and most retain both top-ten membership and outcome-direction agreement after the most favorable game is removed. In partial 2026*, the stable fraction drops sharply and most motifs are labeled limited evidence. This is the desired behavior. Rather than over-interpreting short observation windows, UPG becomes more conservative when recurrence evidence is limited. If Figure 4 shows that motifs are not merely artifacts of one game, Figure 5 shows what it means for a motif to remain traceable. We use Jacob Misiorowski’s FF–SL–FF motif because it is frequent enough to support aggregation but still simple enough to visualize clearly. The figure resolves the same motif from season-level support to monthly counts, then to specific June games, then to the individual PAs on June 12, and finally to the exact catcher’s-view trajectories of

Support-Adaptive Resolution

The next question is whether a highly detailed sequence representation is actually usable at scale. A graph that preserves fine trajectory detail is only helpful if recurring patterns can still be supported often enough to analyze. This experiment therefore tests the core design trade-off of UPG: how much detail can be retained before the representation becomes too sparse. Figure 3 evaluates four alternatives using a chronological split of each pitcher’s 2025 games. A fixed order-four path captures rich local history, but its support collapses: fewer than one in five held-out paths remain supported. Variable-order backoff resolves this problem, raising coverage to nearly 95% while also improving held-out reconstruction of physical execution. Allowing trajectory-qualified substates adds only a small additional gain in reconstruction, showing that the main benefit comes from adapting path length to available support rather than forcing every path into a fine discrete state. This experiment is central to the paper because it validates the main design decision in Section 3.4. UPG does not insist that the most detailed path is always the best one. Instead, it preserves continuous trajectory at the event level and uses a support-qualified 6

Conference’17, July 2017, Washington, DC, USA B

Other

Season 7

6

5 4

4 2 0

June

4 3

3

3 2

2 1 0

06

07

08

09

Jun 12

Jun 20

Month

Jun 25

Game date

C

AUROC

A 1.0

1.00

False-change rate 1.00 0.97

0.99

0.8 0.6

0.50

0.50

0.4 0.16

0.2

0.04

0.0 Mix

SGT

R-UPG

Changed dimension P@3 Supporting PA P@3

B Localization precision

Beneficial

8

Occurrences

Occurrences

8

Controlled change score

A

1.00

1.0

1.00

0.77

0.8

0.77

0.6 0.4 0.2 0.0

M-UPG

Rolling

Multiscale

D Game PA 2

SL

C3

C1

C3

z2·x2

z3·x3

z2·x1

FF

SL

FF

C3

C1

C1

out-R

z2·x3

z3·x2

FF

SL

FF

R · ahead · empty

PA 23 R · ahead · on

PA 25

C3

C1

C1

out-T

z3·x2

z3·x1

L · even · on

–

+

+

2025

C

PA 23 6

FF

2026*

Future persistence

5

Height z (ft)

FF

Direction P@3

4

3

3

Profile cosine

1

2

2 Outcome forecast

1

−0.10

−0.05

0.00

0.05

0.10

0.15

Selected minus within-pitcher control −2

−1

0

1

2

Catcher-view x (ft)

Figure 6: Change detection and diagnostic guardrails. (A) Detection of a controlled execution-only change and falsechange rate. (B) P@3 for the known changed dimensions and supporting PAs. (C) Gain over within-pitcher control boundaries for natural changes; intervals are pitcher-bootstrap confidence intervals.

Figure 5: Multi-scale drill-down for Jacob Misiorowski’s 2025 FF–SL–FF motif. (A) Monthly support and pitcher-beneficial annotations. (B) Support within June games. (C) Matching PAs on June 12 with context, trajectory substate, and endpoint. (D) Exact catcher’s-view trajectories for one occurrence. Table 2: Confidence-aware diagnostic examples. Δ denotes the outcome-rate difference from the corresponding pitchtype reference.

Player

Motif

Sánchez SI–CH–CH Elder SI–SL–SL Alcantara SI–SI–CH

Support Disc. (occ./games) Δ 63 / 25 55 / 22 17 / 11

important because it shows that UPG does not force every interesting sequence into a strong claim.

Val.

𝑛/Δ

Decision

4.5

−0.8 31 / −3.7 Supported +5.2 7 / −2.5 Uncertain −3.0 8 / −13.7 Abstain

Retrospective Change Localization

A further motivation for the framework is retrospective diagnosis of how a pitcher’s style changes. This requires more than detecting that aggregate statistics moved; it requires localizing what changed and which events support that conclusion. We therefore evaluate change localization in both a controlled setting and a natural retrospective setting. In the controlled study, the pitch type, zone, and count signature are held fixed while the continuous execution distribution is changed at a known game boundary. This design isolates what UPG is meant to detect: execution-level change that is invisible to coarse summaries. Figure 6A shows that pitch mix and SGT remain at chance, whereas multiscale UPG achieves near-perfect discrimination. Figure 6B further shows that the method identifies not only that a change occurred, but also the affected dimensions and supporting PAs. This is the key validity result: the framework can recover localized execution changes when the truth is known. Figure 6C moves to natural retrospective boundaries. Here the message is intentionally more modest. Selected boundaries improve reconstruction and directional localization relative to withinpitcher controls, but they do not imply that the change will persist or that future outcomes will improve. This limitation is important. The contribution of UPG is retrospective diagnosis and evidence localization, not a claim of causal discovery or future-performance forecasting.

one occurrence. This is precisely the intended multi-scale behavior of UPG: an aggregate strategy pattern remains linked to the physical events from which it was constructed. The same example also clarifies the meaning of support-adaptive reporting. The coarse motif is well supported across games, whereas its strict fine realization is not. Accordingly, UPG reports the supported coarse pattern but does not discard the trajectory substates, endpoints, or exact pitches. Backoff therefore weakens the strength of the aggregate claim without deleting the fine-grained evidence. Table 2 complements the population-level results with three concrete diagnostic outcomes. The goal here is not to rank players, but to show how the system reports evidence at different strengths. Cristopher Sánchez provides a clear supported case: the motif repeats broadly and retains its direction in validation. Bryce Elder shows a different situation: the sequence structure repeats, but its outcome association does not remain stable, so the system retains the motif while downgrading the claim. Sandy Alcantara illustrates abstention: the candidate pattern is inspectable but does not have enough repeated support to justify a stable diagnosis. This table is 7

Conference’17, July 2017, Washington, DC, USA A

Kichang Lee and JeongGil Ko

B

Yoshinobu Yamamoto · 2025

A

Jacob Misiorowski · 2025

B

Shohei Ohtani · 2023

Shohei Ohtani · 2026*

FC

FC

FC

<1%

12%

11%

FS

SL

SL 3%

25%

FF

33%

55%

CU

CU

CH

18%

15%

6%

SI

4%

FF

FF

ST

FS

SL

6%

24%

<1%

35%

FS

SL 1%

9%

ST

FF

35%

ST

45%

29%

CU

CU 4%

10%

SI

7%

SI

5%

8%

Representative path

C

Other frequent

D

Height z (ft)

FF → FS → FS · n=24 · 15 games 6

6

5

5

4

Representative path

FF → SL → FF · n=24 · 12 games

1

D

FF

FF→FF→ST

CU

FF→CU→FF

ST→FF→FF

3

4

3

1

3

CU→FF→FF

2 SL

2

2

Other frequent

C

FC→FF→FF

2

FC→FC→FF

3 1

1

FC

ST→ST→ST −10

−2

−1

0

1

Catcher-view x (ft)

2

−2

−1

0

1

2

10

Pitch-share change (pp)

Catcher-view x (ft)

−5.0

−2.5

0.0

2.5

5.0

3-pitch path-share change (pp)

Figure 8: Shohei Ohtani in 2023 and partial 2026*. (A–B) Pitchtype graphs. (C) Pitch-share changes. (D) Largest three-pitch path-share changes.

Figure 7: Graph-to-pitch comparison in 2025. Node area represents pitch share and edge width uses a common transition scale. The lower panels resolve Yoshinobu Yamamoto’s FF–FS–FS and Jacob Misiorowski’s FF–SL–FF motifs to representative PAs and exact catcher’s-view trajectories.

4.6

0

rises, cutter usage largely disappears, and the dominant three-pitch paths shift toward a different set of recurrent combinations. The post-return period also shows higher four-seam velocity and improved contact-quality indicators, although not every performance measure improves. Accordingly, this case is best interpreted as a coordinated reorganization of repertoire, execution, and sequence structure, rather than as a simple claim that his results uniformly improved. Across contexts. We return to Yamamoto to isolate a different capability of the representation: describing how the same pitcher reorganizes his strategy under different matchup contexts. Holding the pitcher fixed makes this case complementary to the cross-player comparison above. Figure 9 shows a clear handedness-conditioned reorganization. Against left-handed batters, Yamamoto emphasizes four-seam fastballs and splitters; against right-handed batters, sinkers and sliders become much more prominent. The difference also appears within trajectory strata, indicating that contextual adaptation involves not only which pitches are chosen, but also how they are executed. This is exactly the kind of structured, contextconditioned diagnosis that a flat pitch-mix summary cannot provide. Beyond individual cases. The preceding figures are intentionally selected to illustrate different analytical questions. Table 3 complements them by applying the same hierarchy-native summary to several pitchers with substantially different repertoire breadth and sequence concentration. Its role is not to declare a best style, but to show that the same representation supports a compact and consistent style description across pitchers. Table 3 makes the diversity of graph-native styles explicit. Misiorowski is highly concentrated around a four-seam backbone and a small set of recurring paths,

Player-Level, Longitudinal, and Contextual Diagnosis

The preceding experiments establish that UPG preserves execution detail, adapts resolution to support, and reports recurring patterns conservatively. We now show what those properties enable in practice. The following cases are chosen to illustrate three complementary analytical uses of the framework: comparing different pitchers, tracing one pitcher’s reorganization over time, and describing how the same pitcher adapts across matchup contexts. Across players. We choose Yoshinobu Yamamoto and Jacob Misiorowski because they provide two clearly contrasting organizations of effective pitching. Yamamoto works from a relatively diverse repertoire with richer mixing among pitch types, whereas Misiorowski builds much of his attack around an unusually concentrated high-velocity fastball–slider backbone. Figure 7 shows that this difference is visible not only in pitch shares and transition structure, but also in the representative executions supporting their motifs. The case illustrates the intended use of UPG in player comparison: it characterizes how pitchers organize their arsenals, not merely how often they throw each pitch. Across time. Ohtani provides a particularly informative longitudinal example because his pitching record contains a clear interruption after 2023 and a later return with a visibly reorganized style. This makes him an appropriate case for asking not only whether aggregate usage changed, but whether the structure of his sequencing and execution changed as well. Figure 8 shows that the difference extends beyond pitch mix: four-seam usage 8

Conference’17, July 2017, Washington, DC, USA A

B

vs LHB · n=770

vs RHB · n=685

FC

FC

16%

10%

FS

FS

SL 1%

30%

SL

22%

13%

FF

FF

32%

22%

CU

CU

15%

12%

SI

SI

5%

21%

Representative path

C

LHB

Other frequent

5

D

RHB

FF

SI · T+

FS

FC · T−

FC

FF · T0

CU

FS · T−

SI

FF · T+

SL 0.0%

Overall, the evaluation supports a qualified but clear conclusion. UPG is not claimed to be universally superior on every compressedsequence or predictive benchmark. Its contribution is that continuous execution, ordered structure, temporal scope, support-aware aggregation, diagnostic confidence, and exact event lineage coexist in a single representation. This makes it possible to move from population-scale summaries to game-level and pitch-level evidence without conflating limited support with strong conclusions.

SI · T0 10.0%

20.0%

30.0%

Pitch share (%)

−20

0

20

40

RHB − LHB within-pitch share (pp)

Figure 9: Yamamoto’s 2026* strategy by batter side. (A– B) Pitch-type graphs against left-handed (LHB) and righthanded batters (RHB). (C) Pitch-mix comparison. (D) Withinpitch trajectory-stratum differences.

Table 3: Hierarchy-native player style signatures. Eff. is effective repertoire; Top-10 is path concentration; Sw. is mean pitch-type switches per three-pitch path.

Player

Eff. Backbone

Yamamoto Misiorowski Ohtani Messick Griffin

5.43 3.02 4.03 5.15 6.09

FF 27% FF 63% FF 45% FF 33% FC 32%

Leading 3-pitch path

Top-10 / Sw.

Execution

FS–FF–FS 3.2% FF–FF–FF 28.8% FF–FF–ST 8.3% FF–FF–FF 5.0% FF–FC–FC 2.4%

24.4 / 1.65 67.2 / 0.96 52.1 / 1.36 28.8 / 1.49 17.7 / 1.65

FF|T+ 49.6% FF|T0 51.7% FF|T+ 47.3% FF|T- 71.6% FC|T+ 70.2%

Discussion

Observational diagnosis rather than causal attribution. UPG is built from retrospective observational data and therefore identifies associations rather than causal effects. Pitch outcomes may also depend on factors that are not fully observed in pitch-tracking data, including batter anticipation, pitcher fatigue and condition, umpire decisions, catcher coordination, and game-specific plans. Accordingly, a trajectory motif associated with whiffs or favorable contact should not be interpreted as proving that the motif caused the outcome. Nevertheless, UPG advances diagnostic resolution by linking trajectory variants, pitch order, game context, and outcome pathways that are collapsed in pitch-mix or aggregate pitch-level summaries. From observed trajectories to pitching mechanics. UPG characterizes how a pitch travels and how it is deployed, but it does not fully explain the biomechanical process that produced that trajectory. Release height, arm slot, deception, spin rate, spin axis, spin efficiency, and pitcher-specific physical constraints may all determine which pitch shapes and sequences are feasible. Future work could integrate biomechanical or pose-tracking measurements with the proposed graph representation. The current analysis should therefore be viewed as generating evidence about observable execution and strategy, rather than directly prescribing mechanical changes. Toward actionable and externally validated diagnosis. The current evaluation measures representation quality and diagnostic specificity, but does not directly establish whether the resulting reports improve coaching or player development decisions. Future studies could evaluate the reports with pitchers, coaches, and analysts, and prospectively examine whether strategy or training changes based on identified motifs produce the expected effects. Broader league-wide, cross-season, and cross-league evaluations would also clarify how well the framework transfers across competition levels and tracking systems.

whereas Messick and Griffin distribute usage across broader repertoires with less concentrated path structure. Yamamoto and Ohtani occupy intermediate positions with different leading motifs and trajectory-refined backbone executions. The value of the table is therefore not in any single number, but in showing that UPG supports a coherent multi-player style vocabulary. Taken together, the player-level analyses demonstrate four complementary uses of the same representation: structural comparison across pitchers, longitudinal reorganization within a pitcher, context-conditioned adaptation, and compact style characterization across multiple players. Across all of these uses, the key property is unchanged: aggregate graph patterns remain connected to the exact physical events that produced them.

6

Conclusion

We presented UPG, a hierarchical graph framework for retrospective analysis of pitching strategy. UPG preserves exact pitch events and continuous execution, organizes them across semantic and temporal scales, and uses support-adaptive paths to balance sequence specificity with repeated evidence. Using 3.94 million MLB Statcast pitches, we showed that discrete sequence representations can miss meaningful execution and ordered structure, while UPG supports reliable multi-scale drill-down, retrospective change localization, and player-level diagnosis with exact event traceability. More broadly, these principles may be useful for other sequential-event domains 9

Conference’17, July 2017, Washington, DC, USA

Kichang Lee and JeongGil Ko

that combine continuous observations with recurring discrete structure. The framework is intended for observational diagnosis rather than causal inference or future-performance prediction.

[9] Kichang Lee, Kyungsik Han, and JeongGil Ko. 2025. Analyzing the impact of the automatic ball strike system in professional baseball through a case study on KBO league data. Scientific reports 15, 1 (2025), 44459. [10] Jeff Long, Jonathan Judge, and Harry Pavlidis. 2017. Prospectus Feature: Introducing Pitch Tunnels. Baseball Prospectus. https://www.baseballprospectus.com/ news/article/31030/prospectus-feature-introducing-pitch-tunnels/ Published January 24, 2017. [11] William Melville, Jesse Melville, Theo Dawson, Delma Nieves-Rivera, Christopher Archibald, and David Grimsman. 2023. A Game Theoretical Approach to Optimal Pitch Sequencing. In Proceedings of the MIT Sloan Sports Analytics Conference. Boston, MA, USA. Research Paper Competition. [12] Joshua Mizels, Brandon J. Erickson, and Peter N. Chalmers. 2022. Current State of Data and Analytics Research in Baseball. Current Reviews in Musculoskeletal Medicine 15, 4 (2022), 283–290. doi:10.1007/s12178-022-09763-6 [13] Youngjai Park, Cheawoon Lim, Seung-Woo Son, and Mi Jin Lee. 2026. Structure of Pitch-Pattern Motifs in Major League Baseball. arXiv:2601.11904 [physics.soc-ph] [14] Arnav Prasad. 2021. Decoding MLB Pitch Sequencing Strategies via Directed Graph Embeddings. In Proceedings of the MIT Sloan Sports Analytics Conference. Boston, MA, USA. Research Paper Competition. [15] Jorma Rissanen. 1983. A universal data compression system. IEEE Transactions on information theory 29, 5 (1983), 656–664. [16] Gagan Sidhu and Brian Caffo. 2014. MONEYBaRL: Exploiting Pitcher DecisionMaking Using Reinforcement Learning. The Annals of Applied Statistics 8, 2 (2014), 926–952. doi:10.1214/13-AOAS712 [17] Ryota Takamido and Hiroki Nakamoto. 2026. Counterfactual Optimization of Baseball Pitch Sequences and Estimation of Its Impact on Season-Level Statistics. arXiv:2606.17345 [cs.LG] [18] Chih-Chang Yu, Chih-Ching Chang, and Hsu-Yung Cheng. 2022. Decide the Next Pitch: A Pitch Prediction Model Using Attention-Based LSTM. In Proceedings of the 2022 IEEE International Conference on Multimedia and Expo Workshops. IEEE. doi:10.1109/ICMEW56448.2022.9859411

References [1] 2026. Baseball Savant: Statcast, Trending MLB Players and Visualizations — baseballsavant.mlb.com. https://baseballsavant.mlb.com/. [2] Joel R. Bock. 2015. Pitch Sequence Complexity and Long-Term Pitcher Performance. Sports 3, 1 (2015), 40–55. doi:10.3390/sports3010040 [3] Fabio Cunial, Jarno Alanko, and Djamal Belazzougui. 2019. A framework for space-efficient variable-order Markov models. Bioinformatics 35, 22 (2019), 4607– 4616. [4] Gartheeban Ganeshapillai and John V. Guttag. 2012. Predicting the Next Pitch. In Proceedings of the MIT Sloan Sports Analytics Conference. Boston, MA, USA. MIT Sloan Sports Analytics Conference. [5] Michael Hamilton, Phuong Hoang, Lori Layne, Joseph Murray, David Padget, Corey Stafford, and Hien Tran. 2014. Applying Machine Learning Techniques to Baseball Pitch Prediction. In Proceedings of the 3rd International Conference on Pattern Recognition Applications and Methods – ICPRAM. INSTICC, SciTePress, 520–527. doi:10.5220/0004763905200527 [6] Glenn Healey. 2019. A Bayesian Method for Computing Intrinsic Pitch Values Using Kernel Density and Nonparametric Regression Estimates. Journal of Quantitative Analysis in Sports 15, 1 (2019), 59–74. doi:10.1515/jqas-2017-0058 [7] David Kagan and Alan M. Nathan. 2017. Statcast and the Baseball Trajectory Calculator. The Physics Teacher 55, 3 (2017), 134–136. doi:10.1119/1.4976652 [8] Jae Sik Lee. 2022. Prediction of Pitch Type and Location in Baseball Using Ensemble Model of Deep Neural Networks. Journal of Sports Analytics 8, 2 (2022), 115–126. doi:10.3233/JSA-200559

10


