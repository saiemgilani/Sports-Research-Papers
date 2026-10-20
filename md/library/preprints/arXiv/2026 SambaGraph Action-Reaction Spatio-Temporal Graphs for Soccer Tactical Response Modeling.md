<!-- source: library/preprints/arXiv/2026 SambaGraph Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling.pdf -->
<!-- arXiv:2609.25569v1, text extracted from the arXiv PDF (open access, fetched 2026-10-20) -->

# SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling

https://arxiv.org/abs/2609.25569

```text
                                              SambaGraph: Action–Reaction Spatio-Temporal
                                              Graphs for Soccer Tactical Response Modeling
                                                                  Abel A. Reyes-Angulo1,4 , Henry O. Velesaca2,3,4 , and Steven Araujo3,4
                                               1
                                                   Michigan Technological University, Houghton, MI, USA 2 ESPOL Polytechnic University, Guayaquil, Ecuador
                                                                3
                                                                  University of Granada, Granada, Spain 4 SambaSports AI, Guayaquil, Ecuador
                                                                        areyesan@mtu.edu; hvelesac@espol.edu.ec; saraujo@espol.edu.ec


                                            Abstract—Soccer tactics are interactive: an attacking action        Our contributions are threefold. First, we curate a graph-
                                         changes the opponent’s defensive problem, and the observed          structured action–reaction dataset with 4,070 episodes from
                                         response depends on the multi-agent match state. We introduce       64 World Cup matches. Second, we define response classifi-
arXiv:2609.25569v1 [cs.LG] 22 Sep 2026




                                         SambaGraph, an action–reaction spatio-temporal graph dataset
                                         and benchmark for soccer tactical response modeling. From           cation and attack-to-defense retrieval protocols with match-
                                         tracking and event data for all 64 matches of the 2022 FIFA         level split safety. Third, we report repeated-seed baselines
                                         World Cup, we curate 4,070 action-centered episodes repre-          showing that compact signatures are strong for classification,
                                         sented as temporally aligned 23-node player–ball graph sequences    graph–signature fusion improves retrieval, hard-negative pair
                                         with attack/defense views, response labels, and 26,270 split-safe   discrimination does not necessarily improve retrieval, and local
                                         attack–defense pairs. We study three questions: whether observed
                                         responses can be classified from graph episodes, whether success-   LLMs are best used as explanation/reranking modules rather
                                         ful defenses can be retrieved for a query attack, and whether       than primary predictors. These contributions are organized
                                         graph-derived summaries support grounded LLM reasoning.             around three research questions. RQ1: Can observed tacti-
                                         A compact signature MLP obtains 0.796 ± 0.007 macro-F1              cal responses be classified from action-centered player–ball
                                         for response classification, while a fused graph–signature dual     graph episodes? RQ2: Can successful defensive responses be
                                         encoder reaches 0.471 ± 0.029 Hit@5 and 0.655 ± 0.051 Hit@10
                                         for full-bank defensive retrieval. Hard negatives maximize pair     retrieved for a query attacking context? RQ3: Can graph-
                                         discrimination but not retrieval quality. Local LLMs under-         derived summaries support grounded LLM reasoning without
                                         perform supervised encoders for direct classification and do        replacing supervised graph/signature models?
                                         not improve over a strong original order in eight-candidate
                                         reranking, but they provide grounded tactical rationales. These
                                         results position SambaGraph as a reproducible benchmark for
                                         graph-based soccer strategy-response research. Code and dataset                          II. R ELATED W ORK
                                         are available at: https://github.com/areyesan/SambaGraph.
                                            Index Terms—sports computer vision, spatio-temporal graphs,
                                         tactical response modeling                                             Tracking data has enabled detailed modeling of team behav-
                                                                                                             ior, pass value, spatial control, and tactical decision support
                                                                                                             in soccer [3]–[5]. Large-scale resources such as SoccerNet
                                                                I. I NTRODUCTION
                                                                                                             have further accelerated soccer video understanding [6], [7].
                                            Soccer is a multi-agent visual reasoning problem. A pass,        These works are valuable, but many benchmarks are centered
                                         cross, shot, foul, or set piece immediately changes the oppo-       on recognizing events or estimating value from a possession
                                         nent’s defensive problem: defenders press, cover, clear, recover    state. SambaGraph instead treats the tactical unit as an action–
                                         shape, or concede a chance. Although tracking and event data        reaction episode: an attacking anchor, the surrounding multi-
                                         make these interactions observable, most public benchmarks          agent configuration, the observed defensive response, and
                                         focus on event recognition, localization, or outcome prediction     retrieved examples that may help explain the response.
                                         rather than action–reaction supervision: given an attacking            Graph representations are a natural fit for interacting players
                                         context, what defensive response followed, and which past           and the ball [8]–[10], and spatio-temporal graph models have
                                         defensive examples are tactically relevant?                         been successful for structured visual dynamics such as skele-
                                            This work introduces SambaGraph, a curated dataset and           ton action recognition [11]. Recent sports-specific systems,
                                         benchmark for tactical response modeling from tracking and          including TacticAI for corner-kick analysis [12] and temporal
                                         event data. We use the PFF FC Enhanced 2022 World Cup               graph models for pass receiver/outcome prediction [13], show
                                         data release, which provides match-level tracking, event logs,      the value of graph-based tactical reasoning. Dynamic graph
                                         and metadata for all 64 matches [1], [2]. As Fig. 1 illustrates,    methods such as DyRep, JODIE, TGAT, EvolveGCN, and
                                         we convert raw data into action-centered graph episodes: each       TGN model interactions that evolve over time [14]–[18].
                                         episode starts from an on-ball anchor, aligns nearby tracking       SambaGraph complements this literature by releasing broad
                                         frames, constructs a fixed player–ball graph sequence, assigns      action–response supervision across multiple event types and
                                         a response label, and exports attack/defense views and paired       by evaluating both response prediction and example-based
                                         examples for classification and retrieval.                          retrieval.
Fig. 1. SambaGraph curation pipeline. Event and tracking streams are aligned through tactical anchors, converted into synchronized player–ball graph windows,
labeled by the ensuing possession outcome, and exported as full graphs, team views, metadata, and paired samples.



                  III. DATASET C ONSTRUCTION                                      At each sampled step ℓ, the full view is a graph Gℓ =
A. Source data and event anchors                                                (Vℓ , Eℓ , Xℓ ) with 23 fixed nodes: 11 home players, 11 away
                                                                                players, and the ball. Node features include location, speed
   We derive SambaGraph from the PFF FC Enhanced 2022
                                                                                when available, team identity, and jersey identifiers. Let
World Cup dataset [1]. We flatten event logs into a unified
                                                                                                       (r)
table containing timestamps, teams, players, set-piece types,                    Xℓ ∈ R23×d ,       Aℓ       ∈ {0, 1}23×23 ,
                                                                                                                      r ∈ {team, opp, ball}
possession events, shot outcomes, and foul outcomes. We                                                                                   (3)
select high-signal anchors: shots, goals, corners, free kicks,                  be the node-feature matrix and relation-specific adjacency
penalties, and explicit fouls. Each anchor is represented as                    matrices for intra-team kNN, cross-team nearest-opponent,
  a = (gameId, period, anchorType, gameEventId,                                 and ball-player edges. We use kteam = 3, kopp = 2, and
                                                                                                             W (r)
                                                                                kball = 5, and define Aℓ = r Aℓ . Edge attributes include
                                              t0 , teamId).
                                                           (1)                  relative displacement, Euclidean distance, and relation type.
and anchors are deduplicated by event identifier and type.                      The episode graph sequence is

B. Tracking windows and graph tensors                                                                G(a) = {(Xℓ , Aℓ , Eℓ )}L
                                                                                                                             ℓ=1 ,                       (4)
   For an anchor at time t0 , we extract                                        with synchronized 12-node attack and defense views formed
                                                                                by selecting one team plus the ball.
              W (a) = {ft | t ∈ [t0 − 5s, t0 + 10s]},                    (2)
canonicalize attack direction so the attacking team moves                       C. Response labels and pair mining
toward +x, and uniformly sample each episode to L = 64                             Each episode receives a fine response label from the event
temporal steps for sequence baselines. This converts each 15-                   stream, including GOAL, SHOT_*, FOUL_*, and END_*.
second window into a fixed 64-step tensor, corresponding to an                  We collapse long-tailed fine labels into four coarse tacti-
effective sampled rate of approximately 4.3 Hz in the released                  cal outcomes: SUCCESS for goals and high-value attack-
representation. The task therefore models the observed action–                  ing outcomes, STOPPED_BY_DEFENSE for unsuccessful
reaction episode, not strict pre-anchor forecasting: the input                  shots, clearances, interceptions, and end-of-attack events,
may include early post-anchor defensive motion, while the                       FOUL_STOP for foul-stopped possessions, and UNKNOWN for
label summarizes the subsequent possession outcome. Pre-                        ambiguous or unresolved cases. This mapping preserves the
anchor-only anticipation is a future benchmark variant.                         tactical distinction needed for the benchmark while avoiding
                           TABLE I                                                                 TABLE III
            DATASET SCALE AND VALIDATION SUMMARY.                                  PAIR DISTRIBUTION FOR RESPONSE MATCHING .

                Item                             Value                                 Pair type                          Pairs
                Matches                             64                                 pos_same                          4,070
                Episodes                         4,070                                 pos_retrieved_success             9,990
                Attack–defense pairs            26,270                                 neg_hard_failure                 12,210
                Automated validation checks         20
                Failed validation checks             0
                Full NPZ tensor coverage         100%
                Attack-view NPZ coverage         100%                  System. You are a soccer tactics analyst and graph reasoning
                Defense-view NPZ coverage        100%                  assistant. Compare a query attacking context with candidate
                Media coverage                   100%                  defensive responses and return valid JSON.
                Cross-split pair leakage             0                 User. Rank the candidate defensive responses for the query
                                                                       attack. Prefer candidates that are tactically plausible and likely to
                                                                       correspond to a successful defensive response.
                            TABLE II
              C OARSE RESPONSE LABEL DISTRIBUTION .                    Query attack: Anchor type = corner;
                                                                       ball displacement = (2.8, 6.6); attack
                Coarse label                  Episodes
                                                                       compactness = 12.4; nearest player to ball
                                                                       = 3.1m; players within 10m = 5; ...
                STOPPED_BY_DEFENSE               2,201                 Candidate C1: Anchor type = free kick;
                FOUL_STOP                        1,066                 defense compactness = 7.8; depth = 29.4;
                UNKNOWN                            464                 nearest player to ball = 1.2m; ...
                SUCCESS                            339
                                                                       Candidate C2: Anchor type = corner; defense
                                                                       compactness = 12.8; depth = 72.2; nearest
                                                                       player to ball = 6.5m; ...
unstable fine-label classes. For retrieval, we construct split-safe    Output JSON schema: {"ranking":["C1","C2",...],
pairs                                                                  "best":"C1", "rationale":"brief reason"}
                 (ai , dj , wij , pairType) ∈ P,                (5)   Fig. 2. Example of the label-masked LLM reranking prompt built from graph-
                                                                      derived summaries.
where ai is a query attack and dj is a candidate defensive
response. Pair types include same-episode positives, retrieved
successful defensive positives, and hard failure negatives            B. Attack-to-defense retrieval and pair scoring
mined using a lightweight signature over ball trajectory and
team-shape summaries. Tables I, II, and III summarize scale,             Given a query attack, the model ranks candidate defen-
labels, and pair composition.                                         sive responses. A relevant retrieval is a successful defensive
D. Artifact schema                                                    response under the success-only protocol. We compare ran-
                                                                      dom retrieval, signature cosine retrieval, random/hard/mixed-
   The curated release contains global metadata and per-match         negative dual encoders, and a fused graph–signature dual
artifacts keyed by attack_id: flattened events, anchors,              encoder. We report Hit@1, Hit@5, Hit@10, MRR, and
episode metadata, full 23-node NPZ windows, 12-node team              nDCG@10. Full-bank retrieval ranks all eligible same-split
views, response metadata, training pairs, compact episode             candidate responses, which makes the task harder and more
contexts, and optional GIF/MP4 visualizations. This schema            realistic than reranking a short list. We also evaluate pair clas-
supports tabular, sequence, and graph baselines without repars-       sification with AUC and AP to test whether curated positives
ing the raw source files.                                             and negatives are separable; this diagnostic is intentionally
         IV. B ENCHMARK TASKS AND BASELINES                           distinct from full-bank retrieval because a model can separate
                                                                      pair labels without producing the best global ranking of
A. Response classification
                                                                      successful defenses.
   Given an episode graph sequence, the goal is to classify
the coarse observed response label. We report accuracy, bal-
anced accuracy, macro-F1, and weighted-F1 over three seeds.           C. Auxiliary LLM graph-summary reasoning
Baselines are: (i) a compact MLP over episode-level tactical
signatures, (ii) a dynamic kNN graph-GRU that applies frame-             We evaluate a lightweight language-based protocol in which
level graph message passing before temporal aggregation, and          each graph sequence is converted into a structured text
(iii) a graph–signature fusion model. This setup is response          summary with anchor type, ball displacement, team spread,
modeling over the full action–reaction window, not a claim of         compactness, and local pressure. LLMs either predict the
pre-anchor anticipation. This clarification is important because      coarse label or rerank eight candidate defenses. Candidate
the post-anchor frames may contain part of the reaction being         outcome labels are masked from the prompt and used only
modeled; the benchmark is therefore designed to represent,            for evaluation, as shown in Fig. 2. This protocol tests whether
classify, and retrieve observed tactical responses rather than        graph summaries support tactical reasoning; it is not treated
forecast them from only pre-event context.                            as a replacement for tensor-based graph or signature models.
                                                                             Fig. 4. Full-bank retrieval and eight-candidate reranking. The fused graph–
                                                                             signature encoder is strongest for full-bank retrieval; Llama-3.2-3B best
                                                                             preserves the strong original reranking order.
Fig. 3. Coarse response classification macro-F1. Supervised models outper-
form LLMs that receive only graph-summary text.



                V. E XPERIMENTS AND R ESULTS
A. Dataset validation
   Table I shows that all validation checks pass. In particular,
all full/attack/defense NPZ files exist, sampled tensors load
with expected node counts, pair identifiers join to existing
episodes, media artifacts are present, and all curated pairs                 Fig. 5. Comparison of pair discrimination, full-bank retrieval, and eight-
remain split-safe. These checks are important because leakage                candidate LLM reranking. Hard negatives improve pair AP, but retrieval and
can otherwise occur when a retrieved defense comes from a                    reranking quality follow different trends.
match assigned to a different split than the query attack.
   All experiments use match-level train/validation/test splits to
                                                                             order is already very strong (0.980 ± 0.000 Hit@1); Llama-
prevent leakage across games. We report mean and standard
                                                                             3.2-3B largely preserves this order (0.943 ± 0.005 Hit@1),
deviation over three seeds for learned baselines. Classification
                                                                             while larger local models degrade top-ranked success. Fig. 4
is evaluated with accuracy, balanced accuracy, macro-F1, and
                                                                             shows the protocol-specific results side by side.
weighted-F1, while retrieval is evaluated with Hit@K, MRR,
and nDCG@10. The LLM experiments use the same test                           D. Negative mining and LLM interpretation
episodes but receive only label-masked graph-summary text;                      Table VI reports the pair-discrimination sanity check. Hard-
outcome labels are used only for evaluation.                                 negative training gives the best pair AUC/AP, but Fig. 5
B. Response classification                                                   shows that this does not translate monotonically to full-
                                                                             bank retrieval. The result is methodological: pair classification
   Table IV reports coarse response classification. The sig-                 tests separability of curated positives and negatives, whereas
nature MLP is strongest, reaching 0.842 ± 0.009 accuracy                     retrieval tests whether successful defenses are ranked well
and 0.796 ± 0.007 macro-F1. Graph–signature fusion is close,                 among many candidates.
while the graph-only GRU is lower and higher-variance.                          The LLM results add a complementary perspective. The
Local LLM classifiers are weaker than supervised encoders:                   LLM classifier is not competitive with supervised numerical
Qwen2.5-7B obtains the best LLM macro-F1 (0.451 ± 0.017).                    encoders, and LLM reranking does not beat the original
Fig. 3 visualizes the same trend and supports the interpretation             candidate order. However, Llama-3.2-3B preserves most of
that graph-derived summaries contain useful signal but do                    that ordering and produces natural-language tactical rationales
not replace specialized supervised encoders. The fact that the               from label-masked graph summaries. Thus, we treat LLMs
signature MLP remains strongest also provides a useful bench-                as explanation/reranking modules rather than primary graph
mark constraint: future graph models should be compared                      encoders. Fig. 7 reports the corresponding Hit@1 comparison.
against compact tactical features rather than only against weak
baselines.                                                                   E. Qualitative retrieval
                                                                                Beyond aggregate metrics, retrieval outputs are useful only
C. Attack-to-defense retrieval and reranking                                 if they are spatially interpretable. Fig. 6 illustrates how
   Table V compares full-bank retrieval with the separate                    retrieved examples can be inspected on the pitch. These
eight-candidate LLM reranking protocol. These protocols are                  qualitative views are not used to compute the metrics, but
not equivalent: full-bank models rank the same-split retrieval               they are useful for auditing whether retrieved defenses are not
pool, whereas LLMs rerank eight preselected candidates with                  only label-correct but also spatially and tactically plausible.
outcome labels hidden. In full-bank retrieval, the fused graph–              This is important for sports analytics applications, where
signature dual encoder is best, reaching 0.471 ± 0.029 Hit@5                 a recommendation should be interpretable to analysts and
and 0.655±0.051 Hit@10. In reranking, the original candidate                 coaches.
                                                             TABLE IV
 C OARSE RESPONSE CLASSIFICATION . S UPERVISED MODELS USE TENSORS / SIGNATURES ; LLM S USE GRAPH - SUMMARY TEXT. R ESULTS ARE MEAN ±
                                                STANDARD DEVIATION OVER THREE SEEDS .


 Model                            Input                         Protocol                            Acc.             Bal. Acc.                 Macro-F1
 Signature MLP                    Signature vector              Supervised             0.842 ± 0.009          0.825 ± 0.004          0.796 ± 0.007
 Graph–signature fusion           Graph + signature             Supervised             0.842 ± 0.001          0.788 ± 0.013          0.784 ± 0.007
 Dynamic graph-GRU                Graph tensor                  Supervised             0.543 ± 0.087          0.538 ± 0.098          0.495 ± 0.097
 Qwen2.5-7B                       Graph-summary text            LLM zero-shot          0.504 ± 0.022          0.448 ± 0.017          0.451 ± 0.017
 Llama-3.1-8B                     Graph-summary text            LLM zero-shot          0.527 ± 0.040          0.469 ± 0.031          0.424 ± 0.027
 Llama-3.2-3B                     Graph-summary text            LLM zero-shot          0.460 ± 0.012          0.482 ± 0.012          0.398 ± 0.011

                                                              TABLE V
R ETRIEVAL AND RERANKING RESULTS . F ULL - BANK RETRIEVAL SEARCHES SAME - SPLIT CANDIDATES ; LLM S RERANK EIGHT PRESELECTED DEFENSES
                                                         WITH LABELS HIDDEN .


 Model                    Protocol                             Hit@1               Hit@5              Hit@10                 MRR               nDCG@10
 Fused dual encoder       Full-bank retrieval        0.193 ± 0.014         0.471 ± 0.029      0.655 ± 0.051        0.328 ± 0.020       0.295 ± 0.007
 Dual encoder             Full-bank retrieval        0.164 ± 0.018         0.414 ± 0.021      0.579 ± 0.041        0.293 ± 0.021       0.247 ± 0.023
 Mixed 70% hard           Full-bank retrieval        0.138 ± 0.031         0.411 ± 0.041      0.588 ± 0.004        0.275 ± 0.029       0.235 ± 0.024
 Signature cosine         Full-bank retrieval        0.018 ± 0.000         0.083 ± 0.000      0.122 ± 0.000        0.052 ± 0.000       0.039 ± 0.000
 Random                   Full-bank retrieval        0.006 ± 0.002         0.030 ± 0.002      0.061 ± 0.003        0.033 ± 0.002       0.014 ± 0.001
 Original order           8-candidate reranking      0.980 ± 0.000         0.981 ± 0.002      1.000 ± 0.000        0.983 ± 0.000       0.986 ± 0.000
 Llama-3.2-3B             8-candidate reranking      0.943 ± 0.005         0.977 ± 0.002      1.000 ± 0.000        0.954 ± 0.003       0.959 ± 0.003
 Random order             8-candidate reranking      0.352 ± 0.005         0.959 ± 0.001      1.000 ± 0.000        0.584 ± 0.004       0.677 ± 0.002
 Llama-3.1-8B             8-candidate reranking      0.319 ± 0.010         0.821 ± 0.010      1.000 ± 0.000        0.539 ± 0.007       0.694 ± 0.003
 Qwen2.5-7B               8-candidate reranking      0.128 ± 0.011         0.801 ± 0.008      1.000 ± 0.000        0.388 ± 0.008       0.590 ± 0.005




             Fig. 6. Qualitative retrieval example showing a query attack and retrieved defensive response candidates rendered on the pitch.



                           TABLE VI
     PAIR CLASSIFICATION ON CURATED ATTACK – DEFENSE PAIRS .

 Model                                            AUC                AP
 Dual encoder, hard negatives             0.983 ± 0.014   0.982 ± 0.014
 Dual encoder, mixed 70% hard             0.947 ± 0.008   0.946 ± 0.002
 Dual encoder, mixed 50% hard             0.928 ± 0.005   0.926 ± 0.006
 Dual encoder, mixed 30% hard             0.924 ± 0.006   0.919 ± 0.003
 Fused dual encoder, random negatives     0.900 ± 0.015   0.908 ± 0.013
 Dual encoder, random negatives           0.903 ± 0.006   0.897 ± 0.007



                         VI. D ISCUSSION                                      Fig. 7. Eight-candidate LLM reranking with outcome labels masked. The
                                                                              original order is strongest; Llama-3.2-3B preserves it better than the other
   The experiments answer the motivating questions. First,                    local LLMs.
tracking and event logs can be transformed into validated
action–reaction graph episodes with split-safe labels and re-
trieval supervision. Second, observed response classification                 this weakens any claim that graph encoders alone drive
is feasible, but compact signatures remain difficult to beat;                 classification performance and establishes a strong baseline
for future graph models. This outcome is expected in a              over a strong original reranking order. Together, these results
limited-data setting: hand-crafted signatures directly encode       establish SambaGraph as a practical benchmark for graph
ball displacement, team spread, compactness, and local pres-        reasoning and strategy-response research in soccer.
sure, whereas graph encoders must learn these abstractions
                                                                                                 R EFERENCES
from relatively few episodes. Third, graph information is
useful for the retrieval use case: the fused graph–signature         [1] PFF FC, “Unleash your inner analyst: PFF FC’s 2022 World Cup dataset
                                                                         now available,” PFF FC Blog, 2024.
dual encoder is the strongest full-bank retrieval model. This        [2] PySport/Kloppy contributors, “PFF FC – Kloppy documentation,”
retrieval setting is closest to the intended analytics use case:         Kloppy documentation, 2025.
given a current attacking configuration, an analyst can inspect      [3] P. Power, H. Ruiz, X. Wei, and P. Lucey, “Not all passes are created
                                                                         equal: objectively measuring the risk and reward of passes in soccer
similar historical defensive responses and compare how differ-           from tracking data,” in Proc. KDD, 2017, pp. 1605–1613.
ent teams contained or failed to contain comparable situations.      [4] J. Fernández and L. Bornn, “SoccerMap: A deep learning architecture
Fourth, negative mining changes what the embedding learns,               for visually-interpretable analysis in soccer,” in ECML PKDD, 2021, pp.
                                                                         491–506.
with hard negatives improving pair AP but reducing broad             [5] H. M. Le, Y. Yue, P. Carr, and P. Lucey, “Coordinated multi-agent
success-oriented retrieval. Finally, local LLMs can reason over          imitation learning,” in Proc. ICML, 2017, pp. 1995–2003.
graph-derived summaries, but their practical role is currently       [6] A. Cioppa, A. Deliège, S. Giancola, B. Ghanem, M. Van Droogenbroeck,
                                                                         et al., “Scaling up SoccerNet with multi-view spatial localization and
grounded explanation and short-list reranking, not direct pre-           re-identification,” Scientific Data, vol. 9, no. 355, 2022.
diction.                                                             [7] SoccerNet, “SoccerNet: Open-source tools and utilities,” GitHub repos-
   The benchmark should therefore be read primarily as a                 itory, 2026.
                                                                     [8] P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V.
dataset and protocol contribution rather than as a new architec-         Zambaldi, et al., “Relational inductive biases, deep learning, and graph
ture paper. This is intentional. By providing the graph tensor           networks,” arXiv:1806.01261, 2018.
representation, response-label mapping, pair construction, val-      [9] T. N. Kipf and M. Welling, “Semi-supervised classification with graph
                                                                         convolutional networks,” in Proc. ICLR, 2017.
idation checks, and multiple baseline families, SambaGraph          [10] P. Veličković, G. Cucurull, A. Casanova, A. Romero, P. Liò, and Y.
makes it possible to study when relational structure helps,              Bengio, “Graph attention networks,” in Proc. ICLR, 2018.
when compact tactical descriptors are sufficient, and how           [11] S. Yan, Y. Xiong, and D. Lin, “Spatial temporal graph convolutional
                                                                         networks for skeleton-based action recognition,” in Proc. AAAI, 2018,
retrieval can support interpretable soccer analysis.                     pp. 7444–7452.
                                                                    [12] Z. Wang, P. Veličković, D. Hennes, N. Tomašev, L. Prince, et al.,
               VII. L IMITATIONS AND E THICS                             “TacticAI: An AI assistant for football tactics,” Nature Communications,
                                                                         vol. 15, p. 1906, 2024.
   SambaGraph models observed action–reaction outcomes              [13] P. Rahimian, H. Kim, M. Schmid, and L. Toka, “Pass receiver and out-
rather than optimal tactical decisions. It is also not a pure            come prediction in soccer using temporal graph networks,” in Machine
pre-anchor anticipation benchmark, because the released full-            Learning and Data Mining for Sports Analytics, 2024, pp. 52–63.
                                                                    [14] R. Trivedi, M. Farajtabar, P. Biswal, and H. Zha, “DyRep: Learning
window representation includes early post-anchor motion. A               representations over dynamic graphs,” in Proc. ICLR, 2019.
successful response may depend on factors not fully captured        [15] S. Kumar, X. Zhang, and J. Leskovec, “Predicting dynamic embedding
in the graph, such as attacker error, goalkeeper performance,            trajectory in temporal interaction networks,” in Proc. KDD, 2019, pp.
                                                                         1269–1278.
score state, fatigue, or coaching instructions. Coarse labels       [16] D. Xu, C. Ruan, E. Korpeoglu, S. Kumar, and K. Achan, “Inductive
compress rich tactical behavior, and broadcast tracking may              representation learning on temporal graphs,” in Proc. ICLR, 2020.
include occlusions, identity switches, or positional noise. The     [17] A. Pareja, G. Domeniconi, J. Chen, T. Ma, T. Suzumura, et al.,
                                                                         “EvolveGCN: Evolving graph convolutional networks for dynamic
benchmark is intended for aggregate tactical research, not indi-         graphs,” in Proc. AAAI, 2020, pp. 5363–5370.
vidual player assessment. Any release must respect the source-      [18] E. Rossi, B. Chamberlain, F. Frasca, D. Eynard, F. Monti, and M.
data license; if raw tracking/event data cannot be redistributed,        Bronstein, “Temporal graph networks for deep learning on dynamic
                                                                         graphs,” arXiv:2006.10637, 2020.
the public release should provide curation code, schemas,
manifests, validation notebooks, and benchmark scripts while
requiring users to obtain the original data through the official
source.
                     VIII. C ONCLUSION
   We introduced SambaGraph, a curated action–reaction
graph dataset and benchmark for soccer tactical response
modeling. The dataset contains 4,070 validated episodes from
64 World Cup matches, synchronized attack/defense graph
views, and 26,270 curated pairs. The baselines show that
compact signatures are strong for response classification,
graph–signature fusion improves full-bank defensive retrieval,
and pair discrimination is not equivalent to retrieval quality.
Multi-seed local LLM experiments show that graph summaries
support grounded rationales, but current LLMs remain below
supervised encoders for classification and do not improve

```
