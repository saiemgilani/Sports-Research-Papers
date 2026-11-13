<!-- source: library/preprints/arXiv/2026/2026 - One Hierarchy, Many Sports Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction - Cai et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.15529 -->
<!-- authors: Chao-Wei Cai, Min-Te Sun, Sheng Kuang Wu, Hung-Hsuan Chen -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-13; equations, tables and figures are NOT preserved - consult the PDF for those -->

# One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction

                                                  O NE H IERARCHY, M ANY S PORTS : H IERARCHY-A LIGNED
                                                   M ULTI -TASK L EARNING FOR N EXT-S HOT P REDICTION


                                                               Chao-Wei Cai† , Min-Te Sun† , Sheng Kuang Wu‡ , Hung-Hsuan Chen†
                                                      †
                                                      Computer Science and Information Engineering, National Central University, Taoyuan, Taiwan
                                                            ‡
                                                              Department of Kinesiology, National Tsing Hua University, Hsinchu, Taiwan
                                                 a96521852@gmail.com, msun@csie.ncu.edu.tw, skwu@mx.nthu.edu.tw, hhchen1105@acm.org
arXiv:2611.15529v1 [cs.LG] 11 Nov 2026




                                                                                                A BSTRACT
                                                    Next-shot prediction in racket sports requires learning from event data with different match structures,
                                                    recorded attributes, and label vocabularies. Table tennis, badminton, and tennis nevertheless share
                                                    a hierarchy in which shots form rallies and rallies form higher scoring units. We present MT-HTA,
                                                    a hierarchy-aligned multi-task Transformer that uses this structure to jointly predict the attributes
                                                    of the next shot. A temporal Transformer captures event progression, a feature-token path models
                                                    interactions among semantic fields rather than along the time axis, and task-specific attention retrieves
                                                    information from hierarchical summaries and player context. The architecture supports three- and
                                                    four-level hierarchies and sport-dependent task sets. Across four datasets from three sports, the final
                                                    MT-HTA achieves the highest mean task-averaged F1 among the compared main models. Ablations
                                                    on table tennis support the combination of hierarchical encoding, task attention, and feature-token
                                                    interaction. Additional modules alter the balance between classification scores and spatial error
                                                    rather than improving every metric. These results support a reusable architecture for heterogeneous
                                                    racket-sport event data. We release the code for reproducibility.1

                                         Keywords next-shot prediction · racket sports · hierarchical Transformer · multi-task learning · sports analytics ·
                                         heterogeneous event data

                                         1       Introduction
                                         Racket sports such as table tennis, badminton, and tennis are fast, continuous decision-making games with explicit rally
                                         boundaries, and predicting a player’s next shot—its type, placement, hand, strength, and spin—is valuable for tactical
                                         analysis, opponent modeling, and training support. They also share a common rule-induced hierarchy: a shot is part of a
                                         rally, rallies form games or sets, and the next decision depends on both the short-term exchange within the current rally
                                         and the longer-term match state. Event-based deep models have made this prediction tractable, from rally-and-style
                                         fusion in badminton (Wang et al., 2022) to movement forecasting (Chang et al., 2023). What has changed underneath
                                         these models is the data. Professional annotation systems, crowdsourced charting projects, and automated vision
                                         pipelines now log every shot of every rally, turning what used to be a handful of hand-coded matches into a continuously
                                         growing, spatio-temporal event stream: the four corpora we use already hold more than 240, 000 annotated shots, and
                                         each of the three sports contributes records under a different schema, label vocabulary, and structural depth. Next-shot
                                         prediction is therefore no longer only a modeling question; it is a question of how to learn over heterogeneous big data
                                         without rebuilding the stack for every source.
                                         Three gaps remain. First, existing stroke-forecasting models are built one sport at a time and typically optimize one or
                                         two attributes, leaving the open question of whether a single architecture can serve sports with different rules, hierarchy
                                         depths, and label spaces. This is the classic variety bottleneck of big data analytics: covering a new sport, or the
                                         same sport under a different annotation provider, means designing, preprocessing, tuning, and maintaining another
                                         model from scratch. Second, the dominant practice of flattening a match into one long sequence—whether recurrent or
                                             1
                                            https://github.com/gndd1221/For-Sports-event-modeling-with-rally-and-score-hierarchical-A-Mul
                                         ti-Task-Hierarchical-Transformer
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction



                                Table Tennis / Badminton                           Tennis
                                D = 3: shot→rally→set                   D = 4: shot→rally→game→set




                                                            MT-HTA
                                                            one model




                                           Type      Loc.      BH         Str.   Spin


Figure 1: MT-HTA applies one formulation and training recipe to sports with different hierarchy depths, jointly
predicting each shot’s attributes. It matches or exceeds generic sequence baselines across all four datasets (Table 3),
with gains driven by a shared core rather than by sport-specific components.


Transformer-based (Hochreiter and Schmidhuber, 1997; Vaswani et al., 2017)—erases the rally and set boundaries the
rules impose, forcing attention across tactically discontinuous shots and blending short-term exchanges with long-term
match structure. Third, and most fundamentally, the literature rarely asks what actually generalizes across racket sports:
which parts of a hierarchical model carry over unchanged from sport to sport, and which are sport-specific adaptations.
We believe that next-shot prediction is best posed as a single, structurally grounded, multi-task problem shared across
racket sports. Concretely, we make the following claim.

Central claim A hierarchy-aligned multi-task architecture can be instantiated with a single formulation and training
recipe across racket sports whose rules, hierarchy depth, and label spaces differ, while remaining competitive with
generic sequence baselines on each sport.

Why this is a machine-learning-on-big-data problem Three properties of the data, not of the sport, drive the design.
Variety dominates. Three sports, four corpora, and three independent annotation protocols disagree on at least three
things: how deep the match structure is (D = 3 for table tennis and badminton, D = 4 for tennis); which shot attributes
are annotated, since badminton records neither strength nor spin and tennis omits strength; and how many classes each
attribute has, the shot-type vocabulary alone ranging from 10 to 19. Thus, we lack a representation general enough to
ingest all of them. Volume sets the operating point: the corpora span 45, 714 to 108, 289 shots, and our largest split
enlarges every axis—matches, players, and events—by roughly 2.3×, which we use as a second, larger operating point.
Velocity shapes the interface. The model reads the shots already played in the current rally, together with the rallies and
the games or sets that have already finished, and emits every attribute in one forward pass. That is the shape an in-match
system needs, and a single prediction costs only milliseconds on a laptop CPU. Multi-task learning (one shared encoder
amortized over every attribute of every sport) is what makes this affordable.
Figure 1 summarizes the resulting arrangement: sports of different hierarchy depth enter one model that predicts every
attribute of the next shot jointly.

Contributions

      1. A unified hierarchy-aligned multi-task formulation that admits a variable hierarchy depth D ∈ {3, 4} and
         a variable task set without per-sport customization, so supporting a new source is a matter of mapping its
         schema, not of redesigning the model.
      2. Cross-sport evidence: under one training recipe, the highest mean Macro F1 on all four datasets, with margins
         over the strongest baselines quantified across three seeds.
      3. A component analysis that, through controlled ablations, isolates the shared core (hierarchy, task attention,
         and feature-token interaction) from sport-specific spatial-fidelity refinements, and characterizes a classifica-
         tion/spatial trade-off.


2   Related Work
Stroke forecasting in racket sports Early tactical analysis used statistics and pattern mining over event sequences (Ter-
roba et al., 2010). In badminton, CoachAI (Hsu et al., 2019), ShuttleSet (Wang et al., 2023), and a stroke-forecasting
benchmark (Wang et al., 2024) provide annotated data and evaluation settings. ShuttleNet (Wang et al., 2022) combines


                                                                 2
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


rally progress with player styles to predict shot type and location; related work studies shot influence (Wang et al., 2021),
movement (Chang et al., 2023), and multimodal next-move prediction (Ibh et al., 2024). Table tennis studies include
video-based hit anticipation (Etaat et al., 2025) and racket-kinematics analysis (Chou et al., 2025; Cheng et al., 2025).
Seq2Event (Simpson et al., 2022) extends event-sequence prediction to soccer. Our focus is developing a multi-attribute
prediction model across different racket sports by an explicit match hierarchy.

Transformers and feature-token modeling The Transformer (Vaswani et al., 2017) replaced recurrence with self-
attention whose standard implementation has quadratic cost in sequence length. Long-sequence forecasters, e.g.,
Informer (Zhou et al., 2021), Autoformer (Wu et al., 2021), and TimesNet (Wu et al., 2023), improve efficiency or
temporal structure. The iTransformer model (Liu et al., 2024) attends across variables; we adopt this view, treating each
semantic shot field as a token to capture interactions among shot attributes. In badminton, MuLMINet (Seong et al.,
2023) couples a multi-input Transformer with a weighted loss. MT-HTA combines field-level interaction with explicit
shot, rally, and higher-level context.

Hierarchical sequence models Hierarchical attention networks (Yang et al., 2016) aggregate words and sentences,
HLogformer (Hou et al., 2024) represents nested log data, and hierarchical recurrent models analyze sentence purpose in
academic abstracts (Hsu et al., 2021). MT-HTA applies this principle to competition units. Its shot–rally–set hierarchy,
extended with games for tennis, differs from DyMF’s hierarchical fusion of movement cues (Chang et al., 2023) and
ShuttleNet’s within-rally modeling (Wang et al., 2022).

Multi-task learning and loss balancing Multi-task learning shares representations to exploit inductive transfer
across related tasks (Caruana, 1997), which is well-suited to next-shot prediction, since several interrelated attributes
jointly define a shot. Balancing competing tasks has been addressed by uncertainty weighting (Kendall et al., 2018)
and gradient normalization (Chen et al., 2018), while architectural approaches route task-specific information through
attention (Liu et al., 2019) or mixtures of experts (Ma et al., 2018). MT-HTA uses a task-specific query over shared
hierarchical context and evaluates random loss weighting (Lin et al., 2022) as an alternative to fixed weights.

3   Problem Formulation
We represent a match as an ordered event sequence nested over a hierarchy of depth D. For the three-level case, a match
M contains NS top-level scoring units, each containing rallies and shots. We use set for this unit following the table
tennis and badminton annotations:
                                               M = {S1 , . . . , SNS },                                                    (1)
                                                       (i)          (i)
                                                Si = {R1 , . . . , R (i) },                                                (2)
                                                                    N    R
                                                (i)
                                              Rj = {xi,j,1 , . . . , xi,j,N (i,j) }.                                       (3)
                                                                             T

For table tennis and badminton, the hierarchy is three levels (shot–rally–set); for tennis, it is four (shot–rally–game–set).
Tennis inserts a game index between the set and rally indices in Eqs. (2)–(3). Using table tennis as an example, each
shot xi,j,t is a vector of semantic fields,
                              xi,j,t = type, loc, bh, spin, str, scA , scB , pid, oid, set i,j,t ,
                                                                                          
                                                                                                                         (4)
comprising the predictable shot attributes (type, location, forehand/backhand, spin, strength), the score state of the two
players (scA , scB ), their identities (pid, oid), and the set index (set). The input-field set is dataset-specific: badminton
additionally records player positions, while tennis includes game scores and serve-state fields.
We now consider a single target rally; with that rally fixed, the i, j subscripts are constant, so we suppress them. For a
prediction target within this rally, the model receives two inputs. The first is the current-rally prefix—the shots already
played in the ongoing rally, up to but excluding the target,
                                               X1:t−1 = [x1 , x2 , . . . , xt−1 ].                                         (5)
The second is the completed hierarchical context Ht . For table tennis and badminton, L2 contains completed rallies
in the current set and L3 contains completed sets. For tennis, L2 contains completed rallies in the current game,
L3 contains completed games in the current set, and L4 contains completed sets. Thus L1 always contains only the
current-rally prefix, and higher levels contain only units completed before the target shot.
Next-shot prediction is then the joint mapping
                                    (k)                                          (k)
                                                                                        ∈ RCk ,
                                                             
                                     ŷt k∈T = fθ X1:t−1 ; Ht ,                  ŷt                                       (6)


                                                                3
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


                                                             Input: X1:t−1 , Ht


                                                          Feature Embedding (Eq. 7)



                                                 HTT (Eq. 8)             FT-iTransformer (Eqs. 9–10)



                                                       Gated Fusion (Eqs. 11–12) ×D


                                                     Bottom-up pooling: L1 → · · · → LD


                                                      Task-Attention Fusion (Eqs. 13–14)


                                              Type        Loc.         BH         Str.     Spin


Figure 2: Final MT-HTA overview. The hierarchical temporal Transformer (HTT) and FT-iTransformer encode each
hierarchy level, with gated path fusion in the Final configuration. Task-specific queries attend to the resulting summaries
and player context. The additional refinements are described in Section 4.5.

                                                                 Completed                                 (2)
                                 Completed set S1                                         Current rally R2
                                                                          (2)
                                   all its rallies               rally R1                  observed shots
                                     and shots                   all its shots               x1 , x 2 , x 3

                                  L3 : set history           L2 : rally history            L1 : current prefix

                                           Excluded: target x4 and all later shots, rallies, and sets


Figure 3: Example of prefix-only input construction for a three-level match. Solid boxes contain observed events; the
                                              (i)
dashed target and future region is excluded. Rj is rally j in set i. The current rally contributes only its observed prefix.


        (k)
where ŷt denotes task logits, T is the dataset-specific task set, and Ck is the corresponding output dimension, including
any reserved padding class. The three sports have five, three, and four prediction tasks, respectively. Hierarchy depth,
input fields, task vocabularies, and sequence-length limits are configured per dataset. Source-specific preprocessing
maps records into this representation, after which the same model implementation is used with independently learned
parameters θ.

4     Method: MT-HTA
Figure 2 summarizes the architecture. Each configured hierarchy level is encoded by a temporal path (hierarchical
temporal Transformer, HTT) and a feature-token path (FT-iTransformer); the two paths are combined, levels are pooled
bottom up, and per-task queries read the resulting summaries together with player context. The remainder of this section
defines these components in order.

4.1   Constructing the Prediction Context

Figure 3 makes the prediction boundary explicit. Consider the fourth shot of the second rally in the second set of a
table tennis match. The current input L1 contains exactly the first three shots of that rally. The completed first rally of
the current set supplies L2 , while the completed first set supplies L3 . The target shot and the remaining events are not
included in any level. Histories are grouped by their competition boundaries before they are encoded; a completed set is
therefore not appended to the current-rally sequence.
At the start of the first rally, both higher-level histories are empty. After that rally ends, its observed events become
eligible for the next rally’s L2 input. When a new set starts, L2 is empty again, whereas the completed set becomes
available to L3 . Missing history is represented by a learned empty-summary token, not by invented events. This absence
is distinct from batch padding, whose positions are excluded by masks. Thus, the same prediction interface covers the
opening, middle, set-boundary, and late-context groups evaluated in Section 5.5.


                                                                         4
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


4.2   Adapting the Event Schema

The shared interface specifies field roles and nesting, while label dictionaries remain source-specific. Table tennis
supplies Type, Backhand, Location, Strength, and Spin targets; badminton supplies Type, Backhand, and Landing Area;
tennis supplies Type, Backhand, Location, and Spin. Badminton player-position fields are inputs rather than additional
targets, and tennis adds game-score and serve-state inputs. Each source retains its own categorical vocabularies and
output dimensions, e.g., a location category in one sport is not assumed to denote the same region in another. Only the
configured tasks receive prediction heads and losses.
Tennis also changes the nesting: completed rallies belong to the current game (L2 ), completed games to the current
set (L3 ), and completed sets to L4 . The temporal and feature-token operations below are reused at each configured
level. This is architectural reuse with dataset-specific embeddings, task queries, and learned parameters, rather than
joint training or parameter transfer between sports.

Adding a source Once records are converted into the shot–rally–higher-unit sample format, supporting a new dataset
is a matter of declaration rather than of model code. A source specifies its hierarchy depth and level names, its
categorical and numerical input fields with per-field embedding widths, the subset of fields that receive prediction heads,
the per-task loss weights, and a sequence-length cap for each level. The encoder, path fusion, and task attention are
untouched. The four corpora used here differ in these declarations and in the preprocessing that produces their samples,
not in the model implementation.

4.3   Hierarchy-Aligned Dual-Path Encoder

Feature embedding Each recorded categorical field is mapped through its own embedding, and player and opponent
identities pass through a shared player-style encoder to give style embeddings ep , eo . Numerical fields are kept as raw
values. For the table tennis field set, the concatenation is projected to the model width dmodel as follows:
                                    ct = [ ep ; eo ; etype ; eloc ; ebh ; espin ; estr ; scA ; scB ; set ],
                                   (0)
                                                                                                                                 (7)
                                  ht     = LayerNorm(Wproj ct + bproj ).

Temporal path The hierarchical temporal Transformer (HTT) adds sinusoidal positional encodings and applies
Nlayers Transformer encoder layers along the time axis:
                               H (n) = TransformerEncoderLayer H (n−1) , mask ,
                                                                             
                                                                                                       (8)
                                                                                (0)
where n = 1, . . . , Nlayers , H (0) stacks the embedded vectors ht of one sequence, and the mask excludes padding
positions. Causality is enforced by constructing inputs exclusively from the observed prefix and completed history; the
encoder uses full self-attention within each observed sequence. Lower-level units are encoded separately before their
summaries enter the next level.

Feature-interaction path (FT-iTransformer) In parallel, each categorical or numerical field forms a feature token;
player identities are handled separately by the style encoder. With C and N denoting the categorical and numerical
input fields, V = C ∪ N is indexed by m. For each m ∈ V, the field’s projected representations U  eτ(m) ∈ Rdmodel at
positions τ are right-aligned to the level-specific maximum length and padding is masked. They are projected along
time with learnable, feature-specific coefficients α(m) ,
                                                                     (ℓ)
                                                                    Tmax
                                                                    X
                                                          (m)
                                                      z         =          ατ(m) U
                                                                                 e (m) ,
                                                                                  τ                                              (9)
                                                                    τ =1
         (ℓ)
where Tmax is the maximum sequence length at hierarchy level ℓ, yielding one token per field. Stacking the F = |V|
tokens into Zfeat = [ z (1) ; . . . ; z (F ) ] ∈ RF ×dmodel , self-attention runs across fields, and a mean over feature tokens gives
the path summary (computed at each hierarchy level):
                                                                                                   
                                               Ze = TransformerEncoder LayerNorm(Zfeat ) ,
                                                                       PF                                                        (10)
                                         hiTrans = LayerNorm 1
                                                                                    
                                                                    F       m=1Zem,: .
At higher levels, field summaries retain their semantics: categorical embeddings are averaged over valid lower-level
units, while numerical state fields retain the last valid value. HTT models temporal progression, and the feature-token
path models interactions among these fields.


                                                                        5
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


Path fusion MT-HTA Core concatenates the two path summaries at each level, projects them to dmodel , and applies
                                                                                                (ℓ)
layer normalization. Final MT-HTA replaces this projection with sigmoid-gated fusion. With hHTT pooled from the
                   (ℓ)
temporal path and hiTrans from the feature-token path, and ⊙ denoting the elementwise product, Final uses
                                                    (ℓ)    (ℓ)
                                g (ℓ) = σ Wgfuse [ hHTT ; hiTrans ] + bfuse
                                                                            
                                                                       g      ,                             (11)
                                (ℓ)                              (ℓ)            (ℓ)
                              hfused = LayerNorm g (ℓ) ⊙ hHTT + (1 − g (ℓ) ) ⊙ hiTrans .
                                                                                      
                                                                                                            (12)
Bottom-up flow Temporal encoding proceeds shot → rally → set, or shot → rally → game → set for tennis. Last-
valid-token pooling produces lower-level summaries for the next level’s sequence. The feature-token path aggregates
fields separately as described above. A level with no completed history uses a learned empty-summary token.

4.4   Task-Attention Fusion

For the three-level case, hierarchical summaries and player embeddings form Sctx = [ hshot ; hrally ; hset ; e′p ; e′o ]; tennis
inserts hgame before hset . Here e′p , e′o are style embeddings projected to the model width. Each task k has a learnable
query qk that attends over this context and is refined by a task-specific feed-forward block:
                                  (k)                                                    
                                ut = MultiHeadAttn Q = qk , K = Sctx , V = Sctx ,                                           (13)
                                  (k)                     (k)           (k) 
                                 zt = LayerNorm ut + FFNk (ut ) .                                                           (14)
                                                     (k)         (k)   (k)      (k)
The per-task vector is decoded by a linear head, ŷt = Wout zt               + bout . Independent queries allow tasks to weight the
shared context differently. The encoder is optimized jointly.

4.5   Domain-Informed Refinements

In addition to gated path fusion, Final MT-HTA enables four refinements. Shot-aware positional encoding adds a serve
flag and a self/opponent flag to the shot input to represent rally starts and player identity within the exchange:
                                  (SA)      (0)
                               ht    = ht + Embserve (is_servet ) + Embself (is_selft ).                            (15)
Top-down refinement lets the highest available summary hhigh query the full shot sequence Hshot , the L1 output of Eq. 8
before pooling, and feeds the result back with a learnable residual scale:
                                                                                         
                            hTD = MultiHeadAttn Q = hhigh , K = Hshot , V = Hshot ,                                 (16)
                            h̃shot = hshot + γTD hTD .                                                             (17)
Gated skip window re-injects the most recent shot (w = 1), projected to sproj , into each task representation through a
sigmoid gate, preserving the local cue that deep aggregation can wash out:
                                                            (k)
                                        g (k) = σ Wgskip [ zt ; sproj ] + bskip
                                                                                
                                                                           g      ,                                (18)
                                            (k)            (k)
                                       z̃t = g (k) ⊙ zt + (1 − g (k) ) ⊙ sproj .                                (19)
Finally, turn-based gating hard-swaps the player and opponent style embeddings at each step according to who strikes,
keeping the context representation hitter-centric across alternating turns. All five optional components are enabled
during training of Final MT-HTA. Their effects are evaluated by retraining ablated configurations.

4.6   Training Objective

All tasks use label-smoothed cross-entropy (ϵ = 0.1). For table tennis location, we additionally penalize spatial error on
the nine valid grid cells, which form a 3 × 3 layout; the remaining location class is a non-grid category. Let BG denote
batch examples whose target lies in the grid, and let p̂(n,G) be the softmax restricted to the nine grid logits. Then
                                                               9
                                                    1 X X (n,G)
                                          Ldist =                 p̂i    Disti, y(n) ,                                (20)
                                                  |BG |       i=1
                                                           n∈BG
                                                      (loc)
                                         Llocation = LCE + λdist Ldist .                                           (21)
Here Dist is Euclidean distance in grid-cell units, λdist = 1.0, and the distance term is zero when BG is empty. Cross-
entropy retains the non-grid category and ignores padding. TheP badminton and tennis configurations use cross-entropy
without this grid-distance term. The total loss is Ltotal = k∈T wk Lk , with fixed weights: 0.2 per task for table
tennis, 0.25 for tennis, and 0.34/0.33/0.33 for badminton Type/Backhand/Location. Random loss weighting was also
evaluated, but did not improve Final MT-HTA’s mean Macro F1 on original table tennis and is excluded from the
reported Final configuration.


                                                                 6
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction



Table 1: Dataset overview. D is hierarchy depth. Class counts are in task order: Type / Backhand / Location for every
dataset, plus Strength / Spin for table tennis and Spin for tennis. These are semantic annotation classes; counts exclude
the model’s index-0 padding class, so each output dimension Ck is one larger. Table tennis location includes nine grid
cells and a non-grid category; location definitions differ across sports.
  Dataset                     D Matches Rallies            Shots     Players Tasks Classes per task Annotation source
    Table Tennis (orig.)     3      116       9,303       45,714      82          5      19 / 3 / 10 / 4 / 6   technical–tactical system
    Table Tennis (exp.)      3      271       20,273     108,289      189         5      19 / 3 / 10 / 4 / 6   technical–tactical system
    Badminton (ShuttleSet)   3       94        5,953      64,378       43         3         10 / 2 / 10        expert-annotated, public
    Tennis (MCP)             4      100       15,778     75,937       78          4        11 / 2 / 7 / 3      crowdsourced, public

Table 2: Input scope and representation on original table tennis. “Full” includes L1 , L2 , and L3 when available, within
the configured input limits. All inputs precede the target.

                                 Model                 History   Representation
                                 Current BiLSTM       L1         Shot recurrence
                                 ShuttleNet (adapted) L1         Encoder–decoder
                                 Rally-context LSTM L1 + L2      LSTM + history mean
                                 Hierarchical LSTM    Full       Hierarchical recurrence
                                 Flat Transformer     Full       Flat shot tokens
                                 PatchTST (adapted) Full         Per-field temporal patches
                                 FT-iTransformer      Full       Flat feature tokens
                                 MT-HTA Core / Final Full        Hierarchical dual paths



5     Experiments

Datasets and setup We evaluate on four datasets spanning three racket sports (Table 1). Table tennis records come
from a technical–tactical annotation system previously used for stroke-type prediction (Cai and Chen, 2025); the
expanded version adds matches and a broader player population. The badminton dataset combines ShuttleSet and
ShuttleSet22 (Wang et al., 2023, 2024), and tennis uses converted Match Charting Project records (Sackmann, 2013).
Dataset-specific preprocessing preserves competition boundaries and maps categorical fields to the model’s vocabularies.
We use a fixed 70/10/20 train/validation/test split by match, preventing a match from appearing in multiple partitions
but does not require disjoint players or pairings. Learned-model results are means and sample standard deviations
over three training trials. For each task, F1 is weighted by class support; “Macro F1” denotes the arithmetic mean of
these task-level weighted F1 scores. For table tennis, Location Average Distance is the mean Euclidean distance in
grid-cell units over examples where both the target and the argmax prediction lie in the valid 3 × 3 grid, so it must be
read alongside Location F1. Throughout, bold marks the best mean in a comparison but may not indicate a statistically
significant difference.

Implementation The compared models use dmodel = 256, which standardizes hidden width but does not equalize
parameter counts. Training uses AdamW (learning rate 10−4 , weight decay 0.01) for 40 epochs, a cosine schedule
with 10% warm-up, and gradient clipping at 1.0. We evaluate the checkpoint with the lowest validation loss. The
accompanying configurations specify batch size 128 for table tennis and badminton and 64 for tennis; the task weights
and distance-loss settings are given in Section 4.6. Training and the reported evaluations use a single NVIDIA V100
GPU (32 GB), 4 vCPUs, and 60 GB RAM, with Python 3.9 and PyTorch 2.3.0 on Linux. Inference is a single forward
pass and does not use this GPU; the millisecond-scale latency noted in Section 1 was measured separately on a laptop
CPU (Apple M2, four threads).

Comparison models and input scope Table 2 distinguishes access to history from the way that history is encoded.
Current BiLSTM and adapted ShuttleNet use only the current-rally prefix. Rally-context LSTM adds a mean-pooled
representation of completed rallies, while Hierarchical LSTM explicitly models shot, rally, and set sequences. Flat
Transformer receives completed history as well as the current prefix, but concatenates them into one shot sequence.
Thus, comparison with the flat model is not a comparison against a current-rally-only input.
We also report an adapted PatchTST (Nie et al., 2023) baseline in the same original table tennis comparison (Table 5).
Each categorical field is embedded and each numerical field is projected before overlapping temporal patches are formed
within each semantic channel. A shared Transformer encodes channels independently; pooled channel summaries are


                                                            7
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction



Table 3: Cross-sport main results (Macro F1); all learned models are mean±std. Structural columns: number of
hierarchy levels and average shots per rally.
 Dataset                    #Lvl     Sh/Rally     Majority    Rally-ctx LSTM       Flat Transformer     MT-HTA Core           Final MT-HTA
 Table Tennis (orig.)        3        4.91         0.2532     0.5177 ± 0.0030      0.5191 ± 0.0059      0.5302 ± 0.0065      0.5315 ± 0.0047
 Table Tennis (exp.)         3        5.34         0.2379     0.5405 ± 0.0057      0.5500 ± 0.0011      0.5474 ± 0.0013      0.5525 ± 0.0007
 Badminton (ShuttleSet)      3        10.81        0.2175     0.5308 ± 0.0028      0.5238 ± 0.0041      0.5289 ± 0.0070      0.5309 ± 0.0028
 Tennis (MCP)                4         4.81        0.5349     0.7038 ± 0.0049      0.6969 ± 0.0012      0.7074 ± 0.0014      0.7095 ± 0.0064


Table 4: Task-level cross-sport results (mean±std). Each F1 is support-weighted. Bold marks the highest mean F1 or
lowest mean distance among the four models within a dataset. A dash denotes a task or metric not used for that dataset.
Location means Landing Area for badminton; only table tennis uses grid-cell distance.
 Model                     Type F1              Backhand F1        Location F1          Strength F1           Spin F1            Loc. Dist. ↓
 (a) Expanded table tennis
 Rally-context LSTM      0.4773 ± 0.0076    0.7756 ± 0.0011      0.3096 ± 0.0079      0.5381 ± 0.0151      0.6018 ± 0.0023     0.8562 ± 0.0115
 Flat Transformer        0.4914 ± 0.0054    0.7731 ± 0.0024     0.3172 ± 0.0047       0.5577 ± 0.0037      0.6105 ± 0.0038    0.8315 ± 0.0040
 MT-HTA Core             0.4884 ± 0.0053    0.7778 ± 0.0009      0.3064 ± 0.0045     0.5593 ± 0.0118       0.6051 ± 0.0007     0.8572 ± 0.0060
 Final MT-HTA           0.5009 ± 0.0015    0.7792 ± 0.0043       0.3104 ± 0.0007      0.5565 ± 0.0039     0.6156 ± 0.0025      0.8567 ± 0.0043
 (b) Badminton
 Rally-context LSTM    0.5002 ± 0.0088     0.8333 ± 0.0030       0.2590 ± 0.0030            –                    –                    –
 Flat Transformer      0.4890 ± 0.0114      0.8245 ± 0.0021      0.2578 ± 0.0030            –                    –                    –
 MT-HTA Core           0.5020 ± 0.0093      0.8301 ± 0.0065      0.2545 ± 0.0067            –                    –                    –
 Final MT-HTA         0.5072 ± 0.0039       0.8236 ± 0.0044     0.2620 ± 0.0037             –                    –                    –
 (c) Tennis
 Rally-context LSTM    0.7856 ± 0.0065      0.7484 ± 0.0063      0.4559 ± 0.0038            –              0.8252 ± 0.0036            –
 Flat Transformer      0.7753 ± 0.0027      0.7469 ± 0.0041      0.4568 ± 0.0014            –              0.8085 ± 0.0017            –
 MT-HTA Core           0.7889 ± 0.0014      0.7541 ± 0.0115     0.4607 ± 0.0039             –              0.8259 ± 0.0036            –
 Final MT-HTA         0.7897 ± 0.0010      0.7640 ± 0.0188       0.4584 ± 0.0036            –             0.8260 ± 0.0024             –



subsequently fused for multi-task classification. This differs from FT-iTransformer, which attends across field tokens,
and from MT-HTA, which additionally retains the competition hierarchy.

5.1   Cross-Sport Main Results

Final MT-HTA attains the highest mean Macro F1 on every dataset in Table 3. Which generic baseline comes closest,
however, changes from sport to sport: the hierarchical LSTM is the strongest on original table tennis (Table 5), whereas
the rally-context LSTM is the strongest on badminton and tennis. Ranking first on all four therefore does not reduce to
outperforming a single fixed competitor.
MT-HTA Core is close to Final. However, Core trails the flat Transformer on expanded table tennis and the rally-context
LSTM on badminton. These results support reuse of the architecture across the evaluated datasets, without establishing
uniform superiority or cross-sport transfer.
The Majority column in Table 3 calibrates these scores across sports: tennis starts from a far higher constant-prediction
baseline, so its higher absolute Macro F1 partly reflects a more concentrated label distribution rather than stronger
prediction. Macro F1 remains support-weighted throughout, so none of these comparisons speaks to performance on
rare labels.

5.2   Task-Level Differences across Sports

Table 4 expands the aggregate comparison into the tasks available for each dataset. Scores are compared within each
panel: Type and Location use different vocabularies across sports, and an absent task is not assigned a zero score. The
table exposes differences that can be hidden by averaging over tasks.
On expanded table tennis, Final has the highest mean Type, Backhand, and Spin F1, while Core has the highest Strength
F1. Flat Transformer remains best on Location F1 (0.3172 vs. Final’s 0.3104) and Location Distance (0.8315 vs.
0.8567). Its spatial advantage is therefore not visible in Macro F1 alone. The distance comparison also retains the
valid-prediction restriction described above; it is not an unconditional error over every test example.
On badminton, Final’s Type and Landing Area means exceed those of Rally-context LSTM (0.5072 vs. 0.5002, and
0.2620 vs. 0.2590), while its Backhand mean is lower (0.8236 vs. 0.8333). These opposing differences explain why
their Macro F1 scores are nearly equal.


                                                                      8
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction



Table 5: Baseline comparison on original table tennis (three-seed mean±std, dmodel = 256). Bold = column-wise best.
ShuttleNet and PatchTST are adapted for single-step multi-task classification; Table 2 specifies their input scope.
 Setting                    Macro F1           Type F1          Backhand F1           Location F1         Strength F1           Spin F1          Loc. Dist. ↓
 ShuttleNet (Seq2Seq)    0.3958 ± 0.0260   0.2672 ± 0.0439    0.5690 ± 0.0411       0.2046 ± 0.0062    0.4376 ± 0.0015      0.5009 ± 0.0423     0.9607 ± 0.0061
 Current BiLSTM          0.5154 ± 0.0034   0.4578 ± 0.0054    0.7417 ± 0.0028       0.2550 ± 0.0123    0.5101 ± 0.0018      0.6124 ± 0.0021     0.8919 ± 0.0080
 Rally-context LSTM      0.5177 ± 0.0030   0.4644 ± 0.0140    0.7439 ± 0.0012       0.2666 ± 0.0057    0.5036 ± 0.0040      0.6101 ± 0.0109     0.9041 ± 0.0144
 Hierarchical LSTM       0.5206 ± 0.0009   0.4715 ± 0.0045    0.7443 ± 0.0023       0.2627 ± 0.0098    0.5063 ± 0.0045      0.6180 ± 0.0081     0.9001 ± 0.0145
 Flat Transformer        0.5191 ± 0.0059   0.4598 ± 0.0090    0.7355 ± 0.0024       0.2667 ± 0.0122    0.5148 ± 0.0041      0.6185 ± 0.0060    0.8791 ± 0.0012
 PatchTST (adapted)      0.4635 ± 0.0091   0.3648 ± 0.0121    0.6598 ± 0.0265       0.2373 ± 0.0148    0.4855 ± 0.0045      0.5700 ± 0.0056     0.9157 ± 0.0174
 MT-HTA Core             0.5302 ± 0.0065    0.4848 ± 0.0036   0.7457 ± 0.0004       0.2693 ± 0.0043     0.5273 ± 0.0094      0.6238 ± 0.0176   0.9046 ± 0.0055
 Full Final MT-HTA      0.5315 ± 0.0047    0.4891 ± 0.0069     0.7429 ± 0.0061       0.2686 ± 0.0060   0.5310 ± 0.0049      0.6259 ± 0.0041    0.8874 ± 0.0101



Table 6: Hierarchy depth and task-fusion variants relative to MT-HTA Core on original table tennis (three-seed
mean±std, dmodel = 256). All rows disable the optional components. L1, L1+L2, and Core use Task Attention (TA);
the other variants use all three levels with different task-fusion operators. Bold = column-wise best within this table.

                        Setting                          Macro F1                      Location F1                      Loc. Dist. ↓
                        L1 only (TA)                0.5204 ± 0.0054                  0.2677 ± 0.0078            0.8902 ± 0.0059
                        L1+L2 (TA)                  0.5250 ± 0.0042                  0.2677 ± 0.0009             0.8944 ± 0.0187
                        Task Projection             0.5271 ± 0.0048                  0.2643 ± 0.0019             0.9086 ± 0.0190
                        CLS-token Fusion            0.5278 ± 0.0025                  0.2634 ± 0.0078             0.9104 ± 0.0142
                        MT-HTA Core                0.5302 ± 0.0065                  0.2693 ± 0.0043              0.9046 ± 0.0055



On tennis, Final leads in mean Type, Backhand, and Spin F1, but Core has the highest Location F1 (0.4607 vs. Final’s
0.4584). The largest Final–Core task-level gap is in Backhand, whose Final score also has substantial seed variation
(0.7640 ± 0.0188). Across the three panels, an overall improvement need not benefit every output, and the optional
refinements do not have a uniform effect across sports.


5.3    Component Analysis

On original table tennis, both Core and Final have higher mean Macro F1 than the recurrent and flat Transformer
baselines (Table 5). The flat Transformer has the lowest Location Distance, indicating that aggregate classification and
spatial error can favor different models.
Adapted PatchTST reaches 0.4635 ± 0.0091 Macro F1, below Flat Transformer’s 0.5191 ± 0.0059. Both use flattened
available history, but organize it into different tokens and encoders. This comparison shows that access to longer history
through temporal patches does not by itself match the other encoders in this setup. It does not isolate patching, channel
independence, or the categorical-task adaptation as the cause of the gap.
Table 6 examines hierarchy depth and the fusion of hierarchical summaries into task representations.
With Task Attention, mean Macro F1 increases from 0.5204 for L1 to 0.5250 for L1+L2 and 0.5302 for all three levels
(Table 6). At that depth, Task Attention also has a higher mean than CLS-token fusion (0.5278) and Task Projection
(0.5271). These differences are modest relative to seed variability. Location Distance follows the opposite mean
trend across the depth variants. Thus, the observed classification gains are accompanied by higher spatial error in this
comparison.
Final reduces Location Distance from Core’s 0.9046 to 0.8874 (Table 7), while the flat Transformer remains lower
at 0.8791 (Table 5). Removing the skip window, top-down attention, or shot-aware positional encoding from Final
increases mean distance by 0.0268, 0.0217, and 0.0201, respectively. Removing turn-based gating or gated path
fusion increases it by smaller amounts, 0.0066 and 0.0017. Conversely, the configurations without the skip window or
turn-based gating have higher mean Macro F1 than Final (0.5345 and 0.5330 vs. 0.5315).
The ablations therefore describe a classification–spatial trade-off on original table tennis. Each ablation reflects a
component’s effect within the full configuration.
The standalone FT-iTransformer reaches 0.5098 Macro F1 (Table 8). Removing the feature-token path from Final
lowers mean Macro F1 by 0.0035 and raises Location Distance from 0.8874 to 0.9153. Type and Strength F1 also
decrease, while Backhand and Location F1 increase slightly. This ablation supports the path’s complementary role
within the full model, with task-dependent effects.


                                                                                9
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction



Table 7: Module sensitivity on original table tennis (three-seed mean±std). Each optional component is disabled in turn
relative to Full Final MT-HTA, and each ablated model is retrained; “w/o Gated Path Fusion” restores concatenation
and projection. MT-HTA Core disables all five components and is repeated from Table 6. Bold = column-wise best
within this table.
 Setting                      Macro F1            Type F1          Backhand F1        Location F1         Strength F1         Spin F1          Loc. Dist. ↓
 Full Final MT-HTA         0.5315 ± 0.0047    0.4891 ± 0.0069    0.7429 ± 0.0061    0.2686 ± 0.0060     0.5310 ± 0.0049   0.6259 ± 0.0041    0.8874 ± 0.0101
 MT-HTA Core               0.5302 ± 0.0065    0.4848 ± 0.0036    0.7457 ± 0.0004    0.2693 ± 0.0043     0.5273 ± 0.0094   0.6238 ± 0.0176     0.9046 ± 0.0055
  w/o Shot-Aware PE         0.5296 ± 0.0017    0.4800 ± 0.0122    0.7432 ± 0.0032    0.2719 ± 0.0049    0.5245 ± 0.0048    0.6282 ± 0.0037   0.9075 ± 0.0067
  w/o Gated Path Fusion     0.5301 ± 0.0041    0.4850 ± 0.0062    0.7461 ± 0.0060    0.2700 ± 0.0006    0.5273 ± 0.0064    0.6221 ± 0.0048   0.8891 ± 0.0090
  w/o Top-Down Attention    0.5272 ± 0.0039    0.4804 ± 0.0029    0.7431 ± 0.0038    0.2622 ± 0.0035    0.5274 ± 0.0049    0.6231 ± 0.0085   0.9091 ± 0.0216
  w/o Turn-Based Gating     0.5330 ± 0.0018    0.4846 ± 0.0051    0.7455 ± 0.0035    0.2722 ± 0.0030   0.5342 ± 0.0033     0.6286 ± 0.0034   0.8940 ± 0.0178
  w/o Skip Window          0.5345 ± 0.0016    0.4897 ± 0.0025    0.7482 ± 0.0024    0.2744 ± 0.0132     0.5307 ± 0.0044   0.6298 ± 0.0057    0.9142 ± 0.0115


Table 8: Dual-path analysis on original table tennis (three-seed mean±std). The standalone FT-iTransformer baseline
and Final without the feature-token path are compared with Final.

                               Setting                                        Macro F1                    Loc. Dist. ↓
                               FT-iTransformer only                      0.5098 ± 0.0037                0.8995 ± 0.0077
                               Final w/o FT-iTransformer                 0.5280 ± 0.0051                0.9153 ± 0.0124
                               Final MT-HTA                             0.5315 ± 0.0047                0.8874 ± 0.0101


5.4        Expanded Data and Multi-Step Prediction

The expanded table tennis dataset increases the number of matches from 116 to 271, players from 82 to 189, and shots
from 45,714 to 108,289 (Table 1). Final achieves 0.5525 Macro F1, compared with 0.5500 for the flat Transformer and
0.5474 for Core (Table 3). Final’s margin over the flat Transformer is smaller than on original table tennis (0.0025 vs.
0.0124), and Core no longer leads that baseline.

Autoregressive evaluation protocol To examine feedback from earlier predictions, we evaluate autoregressive Type
prediction on original table tennis using the three trained Final checkpoints. The model observes n = 1, . . . , 5 initial
shots and predicts up to five further steps, provided the targets exist. Each appended event uses the argmax labels for all
five tasks, although this diagnostic scores only Type. Completed-rally and completed-set histories remain observed
context.
Player identities, score state, and other non-target fields retain their recorded values. Rollout stops at the recorded rally
boundary, so this is conditional label prediction, not autonomous match simulation. Top-3 measures membership in a
ranked candidate set; only argmax labels are fed back, without branching into alternative trajectories.

Aggregation and horizon-specific results For prefix length n and future step K, let Nn,K count eligible pairs and
cn,K count hits. Horizon accuracy is
                                                     P
                                                         cn,K
                                             AK = P n          .                                             (22)
                                                       n Nn,K
Top-1 and Top-3 use this same expression and differ only in what counts as a hit. Table 9 reports the mean and sample
standard deviation of AK over the three training trials. Overall also weights by pair count, rather than equally weighting
horizons. A rally can contribute several prefixes and horizons; pairs are not independent rallies. These Type accuracies
differ from the main task-averaged weighted F1.
First-step Top-1 accuracy (0.5146 ± 0.0061) is close to the single-step result (0.5143 ± 0.0064), but falls to 0.3142 at
+2 and approximately 0.26–0.27 thereafter. Top-3 also falls, from 0.8501 to 0.5456–0.5728 at +3 to +5. Candidate-set
membership does not establish calibrated probabilities or tactically coherent generated sequences.
Pairs decrease from 6,602 at +1 to 1,697 at +5, as distant targets require longer rallies. The small Top-1 rise after
+3 is therefore not evidence of recovery on a fixed sample set. This diagnostic combines prediction feedback with
changing target coverage and does not isolate their separate effects.

5.5        Context Availability during Match Progression

We group original table tennis test examples by available history, fixing each example to the first three observed shots
and the fourth-shot target. The groups contain only L1 (opening), L1+L2 (middle), L1+L3 (set boundary), or all three


                                                                             10
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


Table 9: Autoregressive Type accuracy on original table tennis (three-seed mean±std). Pair counts are averages per
seed. Each horizon pools evaluated prefix lengths by sample count; Overall pools all prefix–horizon pairs.

                                  Step      Pairs/seed   Top-1 accuracy     Top-3 accuracy
                                  +1            6,602    0.5146 ± 0.0061    0.8501 ± 0.0049
                                  +2            5,070    0.3142 ± 0.0075    0.6151 ± 0.0024
                                  +3            3,638    0.2623 ± 0.0126    0.5456 ± 0.0122
                                  +4            2,479    0.2641 ± 0.0096    0.5676 ± 0.0185
                                  +5            1,697    0.2709 ± 0.0076    0.5728 ± 0.0176
                                  Overall     19,486 0.3623 ± 0.0075 0.6720 ± 0.0077


Table 10: Final MT-HTA by context availability on original table tennis (three-seed mean±std). All examples predict
the fourth shot from the first three. Groups contain different examples, classified by available completed history.

            Stage                        Samples         Macro F1            Location F1        Loc. Dist. ↓
            Opening: L1 only                 20     0.5187 ± 0.0536        0.3225 ± 0.0700    0.8566 ± 0.0838
            Middle: L1+L2                   279     0.5143 ± 0.0066        0.2887 ± 0.0169    0.8744 ± 0.0081
            Set boundary: L1+L3              64     0.5096 ± 0.0127        0.2909 ± 0.0843    0.7416 ± 0.1503
            Late: L1+L2+L3                  989     0.5398 ± 0.0074        0.2639 ± 0.0129    0.8839 ± 0.0174



levels (late). Empty higher levels use learned fallback tokens. This is an offline stratified evaluation; examples in
different groups also differ in match phase and label distribution.
Final has its highest mean Macro F1 in the late group (0.5398; Table 10), which contains 989 of 1,352 examples. The
opening group contains only 20 examples and has much greater seed variability (0.5187 ± 0.0536). These results do
not establish equal reliability across match phases. The overall majority score is not a matched baseline for individual
groups, and differences between groups cannot be attributed solely to context availability.
Within the same late-group examples, mean Macro F1 is 0.5247 for L1, 0.5318 for L1+L2, 0.5349 for Core, and 0.5398
for Final (Table 11); the same ordering holds in the middle group. This pattern is consistent with benefits from available
history, but the variants also differ in parameters and optional components. It is descriptive evidence, not an isolated
causal estimate of higher-level context.


5.6   Fixed-Rule Attention Case Study

To inspect how the context summaries are used within one match, we examine a fixed-rule case from the original table
tennis test set. Among matches that contain a fourth-shot target at all three context stages, we select the one whose rally
count is closest to the candidate median, breaking ties by match identifier; prediction correctness plays no part in the
selection. The chosen match has 79 rallies across five sets, and the middle and late checkpoints are the first eligible
rallies in search order.
All three checkpoints observe the first three shots and predict the fourth. The opening checkpoint is set 1, rally 1, with
no completed rally or set. The middle checkpoint is set 1, rally 5, with four completed rallies and no completed set. The
late checkpoint is set 2, rally 2, with one completed rally in the current set and one completed set. “Late” therefore
denotes availability of all hierarchy levels, not the final portion of the match.
Figure 4 shows per-task attention over the hierarchy summaries and hitter/receiver context. Averaging the unrounded
three-seed means across tasks, the opening checkpoint places 0.5321 on L1 , compared with 0.0664 and 0.0602 on the
empty L2 and L3 summaries. The nonzero empty-token weights are attention to learned fallback representations, not
access to future rallies or sets. At the middle checkpoint, the mean L2 weight is 0.1758. At the late checkpoint, the
weights are distributed across L1 (0.2901), L2 (0.1708), L3 (0.1958), and hitter context (0.1970).
Prediction correctness does not increase monotonically along these checkpoints. Using three-seed mean task probabili-
ties, Final is correct on 3 of 5 tasks at opening, 4 of 5 at middle, and 2 of 5 at late, with the true label in its top three
everywhere; Core reaches 3 of 5 at the late checkpoint. These are single predictions, so the example illustrates changing
context allocation without establishing a model ranking or a causal reading of attention. Tables 10 and 11 carry the
population-level comparison.


                                                              11
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


Table 11: Macro F1 of hierarchy-depth variants by context availability (three-seed mean±std). The full models lead
once rally- and set-level history exist; the Opening column rests on 20 samples and is not read as a ranking.

                Model                     Opening              Middle             Set boundary                      Late
                L1 only (TA)           0.5217 ± 0.0354     0.5016 ± 0.0030      0.5160 ± 0.0111           0.5247 ± 0.0082
                L1+L2 (TA)             0.5373 ± 0.0225     0.5077 ± 0.0040      0.4996 ± 0.0060           0.5318 ± 0.0072
                MT-HTA Core            0.5451 ± 0.0462     0.5134 ± 0.0073      0.5019 ± 0.0226           0.5349 ± 0.0112
                Final MT-HTA           0.5187 ± 0.0536     0.5143 ± 0.0066      0.5096 ± 0.0127          0.5398 ± 0.0074


                              Opening                                    Middle                                                       Late
         Type 0.66 0.03 0.03 0.10 0.18                   Type 0.63 0.14 0.02 0.08 0.14                  Type 0.37 0.16 0.15 0.19 0.13
Backhand 0.61 0.05 0.04 0.12 0.18                  Backhand 0.59 0.14 0.03 0.09 0.14              Backhand 0.35 0.16 0.16 0.19 0.15
 Location 0.45 0.09 0.08 0.17 0.21                  Location 0.42 0.19 0.07 0.14 0.18             Location 0.25 0.19 0.20 0.21 0.16
    Strength 0.41 0.10 0.10 0.18 0.21               Strength 0.40 0.21 0.08 0.14 0.17              Strength 0.23 0.18 0.24 0.20 0.16
         Spin 0.52 0.06 0.06 0.15 0.21                   Spin 0.50 0.20 0.04 0.11 0.15                  Spin 0.26 0.17 0.24 0.20 0.14
                 L1     L∗2      L∗3   Hit. Rec.               L1   L2    L∗3     Hit. Rec.                    L1          L2         L3      Hit. Rec.
     ∗
         Learned empty summary                                            Mean attention:   0.0   0.1   0.2   0.3    0.4        0.5     0.6    0.7



Figure 4: Final MT-HTA task-attention weights at the three fixed-rule checkpoints. Each cell is a three-seed mean,
displayed to two decimals; darker shading denotes a larger weight. Rows are tasks and columns are context tokens;
Hit. and Rec. denote hitter and receiver. An asterisk marks a learned empty-summary token, not observed history. All
panels use the same shading scale.



6        Discussion and Limitations

MT-HTA provides a common architectural design for event datasets with different hierarchies, fields, and prediction
tasks. The shared encoder serves the tasks within a dataset; preprocessing, configuration, and learned parameters remain
dataset-specific. The evidence therefore concerns architectural applicability across racket sports. It does not measure
joint training across sports, transfer to an unseen sport, or reductions in pipeline maintenance cost.
Three patterns recur across the results. Aligning the encoder to the competition hierarchy helps on every dataset, but by
small amounts: Final exceeds the flat sequence baseline on all four corpora without ever pulling far ahead. The gain
comes from the shared core rather than from the sport-specific refinements, since Core stays close to Final everywhere
and, on original table tennis, two refinements can be removed without lowering mean Macro F1. Classification and
spatial accuracy respond differently to the same components, so an aggregate score hides which outputs a change helps.
The hierarchy is therefore the part that ports across sports, while the refinements are what a new source should expect to
re-tune.
The accuracy margins are modest and estimated from three training seeds on one fixed split per dataset. Match-level
splitting does not test generalization to entirely unseen players. Differences in task sets, label distributions, hierarchy
depth, and dataset composition also prevent attributing cross-sport score differences to structural richness. The detailed
component analysis is limited to original table tennis.
Location remains difficult, and classification and distance metrics can favor different configurations. The distance
metric excludes non-grid predictions and may therefore average over different subsets for different models. Lower
distance alone does not establish better location prediction. Grid discretization and imbalanced placement labels are
additional limitations; continuous-coordinate modeling could reduce discretization error, but would require suitable
annotations and separate evaluation.
The original ShuttleNet cannot be applied directly here: it assumes a fixed prefix length and targets stroke-sequence
generation, whereas our setting has dynamic history length and single-step multi-task prediction. The Adapted
ShuttleNet, despite keeping most components identical to the original design, still differs from its original stroke-
generation setting in output representation and decoding, and uses only the current-rally prefix. Its scores may reflect
adaptation and context differences.


                                                                    12
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


7   Conclusion
We presented MT-HTA, a hierarchy-aligned multi-task Transformer for next-shot prediction over heterogeneous racket-
sport event data. The same architectural design supports three- and four-level match structures and different task sets,
with separate training on each dataset. Across four datasets, Final MT-HTA achieves competitive task-averaged F1 and
the highest means among the compared main models, with modest margins and an effective tie on badminton. Ablations
on original table tennis support hierarchical encoding with task attention and complementary feature-token interaction,
while exposing trade-offs between classification and spatial error.
Future work includes continuous-coordinate location prediction, objective physical measurements for attributes such as
strength, multimodal pre-shot cues, and measured transfer between sports. Evaluating incremental processing and live
annotation latency would further establish the framework’s suitability for in-match analysis.

Acknowledgments and GenAI Usage Disclosure
This work was supported by the National Science and Technology Council of Taiwan under Grant 113-2221-E-008-100-
MY3. Computational and storage resources were provided by the National Center for High-performance Computing of
National Applied Research Laboratories, Taiwan. The authors largely used LLMs to improve language and readability.
The authors reviewed and edited the content as needed. The authors take full responsibility for the content.

References
Cai, C.-W. and Chen, H.-H. (2025). Predicting stroke types in table tennis using sequence to sequence models. In 15th
  International Symposium on Computer Science in Sport (IACSS).
Caruana, R. (1997). Multitask learning. Machine Learning, 28(1):41–75.
Chang, K.-S., Wang, W.-Y., and Peng, W.-C. (2023). Where will players move next? dynamic graphs and hierarchical
  fusion for movement forecasting in badminton. In Proc. AAAI Conf. on Artificial Intelligence, volume 37, pages
  6998–7005.
Chen, Z., Badrinarayanan, V., Lee, C.-Y., and Rabinovich, A. (2018). GradNorm: Gradient normalization for adaptive
  loss balancing in deep multitask networks. In Proc. 35th Int. Conf. on Machine Learning (ICML), pages 794–803.
Cheng, P.-C., Chen, H.-H., Lai, C.-Y., Chen, D.-Y., Sun, M.-T., Sheu, Y.-H., Song, T.-F., and Wu, S. K. (2025). From
  swing to insight: An IoT-based system for kinematic analysis and player assessment in table tennis. In IEEE Annual
  Congress on Artificial Intelligence of Things.
Chou, C.-Y., Chen, Z.-H., Sheu, Y.-H., Chen, H.-H., Sun, M.-T., and Wu, S. K. (2025). TTSwing: A dataset for table
  tennis swing and racket kinematics analysis. Scientific Data, 12(1):339.
Etaat, D., Kalaria, D., Rahmanian, N., and Sastry, S. S. (2025). LATTE-MV: Learning to anticipate table tennis hits
  from monocular videos. In IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), pages 7115–7124.
Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8):1735–1780.
Hou, Z., Ghashami, M., Kuznetsov, M., and Torkamani, M. (2024). HLogformer: A hierarchical transformer for
  representing log data. arXiv:2408.16803.
Hsu, L., Kao, C., Jheng, I., and Chen, H. (2021). Toward building an academic search engine understanding the
  purposes of the matched sentences in an abstract. IEEE Access, 9:109344–109354.
Hsu, T.-H., Chen, C.-H., Jut, N. P., Ik, T.-U., Peng, W.-C., Wang, Y.-S., Tseng, Y.-C., Huang, J.-L., Ching, Y.-T., Wang,
  C.-C., and Lin, Y.-H. (2019). CoachAI: A project for microscopic badminton match data collection and tactical
  analysis. In 20th Asia-Pacific Network Operations and Management Symposium (APNOMS), pages 1–4.
Ibh, M., Graßhof, S., and Hansen, D. W. (2024). A stroke of genius: Predicting the next move in badminton. In
  IEEE/CVF Conf. on Computer Vision and Pattern Recognition Workshops (CVPRW), pages 3376–3385.
Kendall, A., Gal, Y., and Cipolla, R. (2018). Multi-task learning using uncertainty to weigh losses for scene geometry
  and semantics. In IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), pages 7482–7491.


                                                          13
One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction


Lin, B., Ye, F., Zhang, Y., and Tsang, I. W. (2022). Reasonable effectiveness of random weighting: A litmus test for
  multi-task learning. Transactions on Machine Learning Research.
Liu, S., Johns, E., and Davison, A. J. (2019). End-to-end multi-task learning with attention. In IEEE/CVF Conf. on
  Computer Vision and Pattern Recognition (CVPR), pages 1871–1880.
Liu, Y., Hu, T., Zhang, H., Wu, H., Wang, S., Ma, L., and Long, M. (2024). iTransformer: Inverted transformers are
  effective for time series forecasting. In Int. Conf. on Learning Representations (ICLR).
Ma, J., Zhao, Z., Yi, X., Chen, J., Hong, L., and Chi, E. H. (2018). Modeling task relationships in multi-task learning
 with multi-gate mixture-of-experts. In Proc. 24th ACM SIGKDD Int. Conf. on Knowledge Discovery and Data
 Mining (KDD), pages 1930–1939.
Nie, Y., Nguyen, N. H., Sinthong, P., and Kalagnanam, J. (2023). A time series is worth 64 words: Long-term
  forecasting with transformers. In Int. Conf. on Learning Representations (ICLR).
Sackmann, J. (2013). Tennis match charting project. https://github.com/JeffSackmann/tennis_MatchChar
  tingProject. Accessed: 2026-06-12.
Seong, M., Oh, J., and Kim, S. (2023). MuLMINet: Multi-layer multi-input transformer network with weighted loss.
  IJCAI-2023 CoachAI Badminton Challenge, Track 2.
Simpson, I., Beal, R. J., Locke, D., and Norman, T. J. (2022). Seq2Event: Learning the language of soccer using
  transformer-based match event prediction. In Proc. 28th ACM SIGKDD Conf. on Knowledge Discovery and Data
  Mining (KDD), pages 3898–3908.
Terroba, A., Kosters, W. A., and Vis, J. K. (2010). Tactical analysis modeling through data mining. In Proceedings of
  the International Conference on Knowledge Discovery and Information Retrieval.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017).
  Attention is all you need. In Advances in Neural Information Processing Systems (NeurIPS), pages 5998–6008.
Wang, W.-Y., Chan, T.-F., Yang, H.-K., Wang, C.-C., Fan, Y.-C., and Peng, W.-C. (2021). Exploring the long short-term
 dependencies to infer shot influence in badminton matches. In IEEE Int. Conf. on Data Mining (ICDM), pages
 1397–1402.
Wang, W.-Y., Du, W.-W., Peng, W.-C., and Ik, T.-U. (2024). Benchmarking stroke forecasting with stroke-level
 badminton dataset. In Proc. 33rd Int. Joint Conf. on Artificial Intelligence (IJCAI), pages 8829–8832.
Wang, W.-Y., Huang, Y.-C., Ik, T.-U., and Peng, W.-C. (2023). ShuttleSet: A human-annotated stroke-level singles
 dataset for badminton tactical analysis. In Proc. 29th ACM SIGKDD Conf. on Knowledge Discovery and Data
 Mining (KDD), pages 5126–5136.
Wang, W.-Y., Shuai, H.-H., Chang, K.-S., and Peng, W.-C. (2022). ShuttleNet: Position-aware fusion of rally progress
 and player styles for stroke forecasting in badminton. In Proc. AAAI Conf. on Artificial Intelligence, volume 36,
 pages 4219–4227.
Wu, H., Hu, T., Liu, Y., Zhou, H., Wang, J., and Long, M. (2023). TimesNet: Temporal 2d-variation modeling for
 general time series analysis. In Int. Conf. on Learning Representations (ICLR).
Wu, H., Xu, J., Wang, J., and Long, M. (2021). Autoformer: Decomposition transformers with auto-correlation for
 long-term series forecasting. In Advances in Neural Information Processing Systems (NeurIPS), pages 22419–22430.
Yang, Z., Yang, D., Dyer, C., He, X., Smola, A., and Hovy, E. (2016). Hierarchical attention networks for document
  classification. In Proc. NAACL-HLT, pages 1480–1489.
Zhou, H., Zhang, S., Peng, J., Zhang, S., Li, J., Xiong, H., and Zhang, W. (2021). Informer: Beyond efficient transformer
  for long sequence time-series forecasting. In Proc. AAAI Conf. on Artificial Intelligence, pages 11106–11115.




                                                           14
