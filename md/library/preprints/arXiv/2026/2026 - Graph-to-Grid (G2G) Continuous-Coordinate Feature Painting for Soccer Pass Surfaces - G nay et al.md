<!-- source: library/preprints/arXiv/2026/2026 - Graph-to-Grid (G2G) Continuous-Coordinate Feature Painting for Soccer Pass Surfaces - G nay et al.pdf -->
<!-- item: https://arxiv.org/abs/2609.24040 -->
<!-- authors: Kaan Günay, Orhun Gun -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-05; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Graph-to-Grid (G2G): Continuous-Coordinate Feature Painting for Soccer Pass Surfaces

                                             Graph-to-Grid (G2G): Continuous-Coordinate Feature Painting
                                                              for Soccer Pass Surfaces
                                                               Kaan Günay                                                  Orhun Gun∗
                                                   Sabancı University, Istanbul, Turkey                 Carnegie Mellon University, Pittsburgh, PA, USA
                                                   kaan@pittsburghdynamics.net                                        orhun@cmu.edu
                                              https://orcid.org/0009-0008-5517-1321                     https://orcid.org/0009-0003-1578-7117
arXiv:2609.24040v1 [cs.LG] 21 Sep 2026




                                                                                                Abstract
                                                    Dense pass surfaces give, for every pitch cell, whether a pass played there would arrive, whether
                                                the carrier would choose it, and what the possession would then be worth. The networks that draw
                                                them read the state as a raster of per-cell counts, losing where inside a cell each player stands. LiDAR
                                                detectors, bird’s-eye-view perception and graph weather models move entity features onto a grid,
                                                binning each entity to a cell or learning the transfer. We evaluate the interpolated form: each player’s
                                                features are scattered bilinearly onto the grid at the player’s measured coordinates, so the surface loss
                                                trains the per-player encoder end to end. Those systems adopt an interface; this paper measures one.
                                                On 53,628 passes from the 2022 World Cup, painting improves selection likelihood over the same
                                                core fed rasters alone by about a quarter of a nat: in every match of an eight-fold cross-validation, with
                                                every arm tuned over five seeds, and after retraining on seven Bundesliga and 2. Bundesliga matches
                                                from another provider. Thirteen pre-specified studies locate the gain: painting the nine raw player
                                                features with no encoder carries three quarters of it, and the learned encoder and message passing add
                                                a smaller, resolved increment. Painting also helps the original SoccerMap and a canonical U-Net,
                                                whereas offset channels, a finer raster, an attention painter and a raster-free decoder do not. Frozen
                                                across the provider boundary the likelihood advantage is lost; injected tracking error compresses it.
                                                These results concern observed-endpoint prediction, not calibrated evaluation of hypothetical passes.

                                         Keywords: differentiable rasterisation; dense prediction from sets; entity-to-grid interfaces; sports
                                         analytics; tracking data; pre-specified replication


                                         1     Introduction
                                         An analyst who pauses a match wants, for every spot on the pitch, three numbers: if the ball were played
                                         there, would it arrive; would this carrier choose it; and what would the possession be worth afterwards.
                                         Answering them for every cell produces a surface over the pitch, and surfaces are what practitioners
                                         read: they show the options a player had, not just the one taken. Learning such surfaces from historical
                                         passes is hard because each example supplies one observed endpoint, and an unsuccessful pass may end
                                         at an interception rather than at its intended destination. In this paper, “selection” denotes prediction of
                                         the observed endpoint. Completion and value are supervised at that endpoint; their values at unchosen
                                         locations are model extrapolations, not validated counterfactuals.
                                             SoccerMap-style networks represent the match state as a raster and predict a dense pitch surface (Fer-
                                         nández and Bornn, 2021; Fernández et al., 2021). Occupancy and aggregated velocity channels lose
                                         within-cell position and the association between a player and that player’s own features. Graph models
                                         retain players and their relations, but the soccer systems reviewed here predict over players or events (Stöckl
                                         et al., 2021; Wang et al., 2024; Rahimian et al., 2026), not over pitch cells. A standard entity-to-grid in-
                                         terface connects the two: scatter each entity’s features bilinearly onto the grid at its measured continuous
                                         coordinates, then process the grid with a convolutional network. Interfaces of this kind carry LiDAR
                                             ∗ Corresponding author. orhun@cmu.edu




                                                                                                    1
object detectors (Lang et al., 2019), bird’s-eye-view perception from cameras (Philion and Fidler, 2020)
and graph weather models (Lam et al., 2023). They differ in where an entity’s features land: those three
bin each entity to one cell or learn the transfer, whereas the interface studied here writes at the measured
continuous position, and Sec. 6.4.2 prices that difference.
     We study this interface through the Graph-to-Grid (G2G) family, our name for a nested set of models
whose arms differ only in what is painted onto a shared raster-only core (Sec. 4, Fig. 2; on the name,
Sec. 2). Bilinear scatter-add is established machinery, and its differentiability is inherited. What has not
been established is what the interface buys and which part of it pays, and soccer pass surfaces are an
unusually clean place to find out: one observed endpoint supervises every example, and the same core,
corpus, recipe and evaluation code can be held fixed while only the front end changes. The contribution
is that measurement.

1.1   Claims, evidence and importance
The main empirical claim is that continuous-coordinate feature painting improves observed-endpoint
prediction over the tested raster-only systems. The full front end improves selection negative log-
likelihood (NLL) over the same core by 0.251 nats in eight-fold cross-validation over all 64 World Cup
matches, 0.292 nats under per-arm learning-rate selection over five seeds, and 0.239 nats after retraining
on seven external German league matches, ahead in every match of each comparison (Table 1). These
are complementary checks, not three independent replications: cross-validation and tuning retain design
choices made on the original World Cup split, while the external corpus is from a different provider,
league and season.
     The attribution is more specific than an improvement from graph learning. Painting the nine raw node
features with no learned encoder retains approximately three quarters of the selection gain, on the World
Cup and on the external corpus alike; the learned encoder and message passing together add a further
0.065–0.067 nats in the cross-validation and tuned comparisons. That increment is resolved there, over
64 match clusters and five seeds, whereas the three-seed holdout studies alone could not characterise it.
Painting also improves the original SoccerMap and a canonical U-Net, so the effect is not tied to one
core. Sub-cell offset channels, a raster four times finer, a learned attention painter and a raster-free set
decoder do not close the gap, within the scope stated in Sec. 7.
     For a new deployment we would start from raw painting: it has no front-end parameters, keeps most
of the gain, and is the cheaper of the two painted variants (Sec. 6.10). We would add the learned front
end where in-distribution selection likelihood is the objective and the tracking provider is fixed. Frozen
across a provider boundary, the raster-only core has the best selection likelihood of the three; raw painting
is numerically ahead of G2G there, but the contrast does not cross the study’s adjusted max-𝑇 threshold.
Entity-to-grid interfaces are already load-bearing in the detection, perception and forecasting systems
cited above, which bin to a cell or learn the transfer rather than writing at continuous coordinates. The
attribution reported here, that placement and the write carry most of the gain and the learned content the
rest, is the kind of question those systems leave open. The present experiments establish evidence only
for soccer endpoint prediction.

Related work by the authors. A companion manuscript, An Open, Auditable Pass-Surface Benchmark
from Public Bundesliga Tracking Data (Günay and Gun, in preparation), studies the construction and
automated target corroboration of the public IDSSE benchmark used here. The papers share the upstream
data, extraction implementation and benchmark version. The companion uses a separately trained
reproduction of published SoccerMap, but no G2G-family checkpoint, contrast or result from this paper,
and its validation and sensitivity results are not reported here. The supplement specifies the external
corpus construction independently of the companion, and the cover letter includes a contribution-overlap
disclosure.




                                                     2
Table 1: The interface effect at a glance. Δ is the selection NLL of the first arm minus the second in nats, so
a negative value favours the first arm; 95% intervals from each study’s match-cluster or hierarchical bootstrap.
Arm C is the raster-only core SoccerMap-v2; D adds the painted front end with a per-node encoder; Draw paints
the nine raw node features with no encoder; G2G replaces the per-node encoder with the relational one; original is
the published SoccerMap; Uraster and Uraw read the same two inputs with a canonical U-Net core. Study numbers
follow Table 3; every full family is in the supplement

 Contrast                                       Study, Sec.             Δ selection NLL Reading
 Value of the painted write
 G2G − C, eight-fold CV over 64 matches         5, §6.1        −0.251 [ −0.263, −0.239]   ahead in 64 of 64 matches
 G2G − C, every arm tuned, converged, 5 seeds   4, §6.3        −0.292 [ −0.338, −0.245]   margin survives per-arm tuning
 G2G − C, other provider, retrained             7, §6.2        −0.239 [ −0.285, −0.197]   ahead in 7 of 7 matches
 originalsplat − original                       8, §6.5        −0.295 [ −0.416, −0.214]   same write on the published core
 Uraw − Uraster (canonical U-Net core)          13, §6.5       −0.242 [ −0.264, −0.213]   same write on a third core
 Uraster − C (U-Net core, raster only)          13, §6.5       +0.366 [+0.333, +0.397]    our core reads better (shared recipe)
 Attribution within the front end
 Draw − C, eight-fold CV over 64 matches        12, §6.1       −0.186 [ −0.199, −0.172]   raw painter carries three quarters
 G2G − Draw , eight-fold CV over 64 matches     12, §6.1       −0.065 [ −0.078, −0.052]   learned content: the remaining quarter
 Draw − C, tuned, converged, 5 seeds            12, §6.3       −0.225 [ −0.256, −0.195]   same share under tuning
 Draw − C, other provider, retrained            10, §6.2       −0.178 [ −0.207, −0.139]   three quarters of the margin, no encoder
 Draw − D (raw features for the embedding)      3, §6.4.2      +0.005 [ −0.049, +0.064]   no separation over 8 matches
 G2G − D (message passing on top of painting)   1, §6.4.1     −0.0515 [ −0.095, −0.005]   clears max-𝑇; seed sd as large
 Dnearest − D (nearest cell for bilinear)       3, §6.4.2      +0.084 [+0.033, +0.125]    placement and interpolation: half the package
 Raster and learned-interface substitutes
 Coffsets − C (sub-cell offset channels)        8, §6.5        −0.044 [ −0.075, −0.011]   a quarter of the gap to D
 Chalf − C (raster four times finer)            9, §6.5        −0.047 [ −0.106, +0.001]   no resolved gain, localisation worsens
 Dattn − C (learned attention painter, tuned)   11, §6.6       +0.235 [+0.170, +0.308]    worse than no painting at all
 SetOnly − C (raster-free set decoder, tuned)   11, §6.6       +0.219 [+0.183, +0.261]    worse than the raster core alone
 Limits of zero-shot transfer
 G2G − C, frozen across the provider boundary 7, §6.2          +0.079 [+0.036, +0.121] likelihood lost, localisation kept
 G2G − Draw , frozen                          10, §6.2         +0.048 [+0.023, +0.070] raw painter ahead; adjusted 𝑝 = 0.062



1.2     Research questions and design
RQ1: Does painting improve endpoint selection and completion prediction over the same raster-only
core across matches and after a change of provider? RQ2: Which front-end components account for the
gain, and does it persist under per-arm learning-rate selection and the stated early-stopping rule?
    The primary corpus contains 53,628 quality-gated passes from all 64 matches of the 2022 World Cup.
The family comprises the raster-only core C, the raw-feature painter Draw , the per-node encoder D and the
relational encoder G2G; controls include the original SoccerMap and a widened version matched to G2G’s
parameter count. Cross-validation and external retraining address RQ1; component ablations, alternative
interfaces and tuned comparisons address RQ2. Thirteen studies recorded their training designs before
their own runs, with the statistical specification and prior data exposure distinguished in Sec. 5.5. The
original three-arm comparison is development history, not independent confirmation.

1.3     Contributions
   1. Evidence, under cross-validation over all 64 matches, per-arm learning-rate selection over five
      seeds, external retraining and three surface cores, that continuous-coordinate feature painting
      improves endpoint-supervised soccer surfaces over the same raster-only core.

   2. A quantified representation trade-off: raw-feature painting carries three quarters of the gain and
      learned content the remaining quarter, with the tested interface alternatives priced against the same
      core and the limits of frozen transfer reported.

   3. A retained evaluation record: signed study commitments, locked predictions, match- and seed-level
      uncertainty, full hypothesis families, and explicit disclosure of holdout reuse and post-hoc analyses.

      Section 2 describes prior work; Secs. 3, 4 and 5 specify the data, models and evaluation. Section 6

                                                                   3
presents the primary comparisons before the mechanism studies. Section 7 states the limits and Sec. 8
concludes. The online supplement (Online Resource 1) contains the full hypothesis families, construction
details and development records.


2    Related work
Three axes locate the contribution: output support (per-player probabilities vs. dense pitch cells), state
representation (hand-crafted, raster, coordinate sequence, graph) and temporal context. Models with
dense spatial outputs read the match state as binned rasters (Fernández and Bornn, 2021; Fernández et al.,
2021; Overmeer et al., 2025; Robberechts et al., 2023), as sequences of tracking coordinates (Pei et al.,
2024), or through hand-specified physics on continuous positions and velocities (Spearman et al., 2017).
Relational and graph models keep players as entities but emit per-player or per-event outputs (Stöckl et al.,
2021; Rahimian et al., 2026; Wang et al., 2024). None of the soccer systems we reviewed writes learned
per-player features onto a pitch grid at continuous coordinates and trains that encoder end to end through
a dense pitch-cell loss, which is the cell this work occupies.

Dense surfaces. SoccerMap (Fernández and Bornn, 2021) established the three-scale fully convolu-
tional surface trained by single-pixel supervision and is our architectural ancestor and control; the EPV
framework of Fernández et al. (2021) supplies the completion/selection/value decomposition our three
heads instantiate. Later work varies that design: Overmeer et al. (2025) introduce a U-Net-inspired
architecture (Ronneberger et al., 2015) with a three-level encoder and attention-gated skips, and add a
risk/reward split and an expert-paired benchmark; our modernised core shares the three-level encoder and
the lateral skips into a top-down path, and adds squeeze-and-excitation and a dilated bottleneck that theirs
does not have, and Sec. 6.5 reproduces the interface effect on a canonical U-Net core rather than on their
system. The un-xPass system (Robberechts et al., 2023) reuses SoccerMap-style components to score
creativity. Pei et al. (2024) feed two seconds of player and ball tracking coordinates to a transformer and
predict the pass-end zone, with separate cross-entropy losses along each pitch axis. Physics-based pitch
control (Spearman et al., 2017; Spearman, 2018) is the complementary non-neural family, computed
from continuous positions and velocities. These systems differ in what they read. SoccerMap and its
descendants bin players into raster cells, the sequence model reads coordinates and decodes zones through
attention, and pitch control is specified by hand. None of them paints learned per-player features onto the
grid at each player’s continuous position for a convolutional network to read, which is the interface this
paper evaluates.

Relational models. Graph learning for soccer is not new: graph convolution for expected receiver, pass
and threat (Stöckl et al., 2021), possession memory for reception against defensive structure (Rahimian
et al., 2026), and earlier pairwise spatial relations (Hubáček et al., 2019). These emit distributions over
players or events rather than training a per-cell loss. TacticAI (Wang et al., 2024) applies geometric
deep learning to corner kicks with graph-level and per-player predictions, but trains no per-cell surface
either. Head-to-head numbers with the closest systems are unavailable because they share no evaluation
universe: Rahimian et al. (2026) score per-receiver predictions on middle-third forward passes from one
league, and Overmeer et al. (2025) use 63 of the same 64 matches as one of two corpora, alongside 624
Eredivisie matches, under different sourcing and gating (TRACAB tracking supplied through the Dutch
federation, 58,569 World Cup passes split for training and evaluation, against our 53,628 admitted), so
cross-quoting compares pipelines, not architectures. The comparison this paper can make fairly is the
one it makes: against SoccerMap reproductions trained under an identical protocol.

Entity-to-grid representations and differentiable rasterisation. Writing learned per-entity features
onto a grid so that a convolutional network can read them is an established pattern outside sport.
VoxelNet (Zhou and Tuzel, 2018) and PointPillars (Lang et al., 2019) encode the points of a LiDAR


                                                     4
sweep with a small per-point network and scatter the result into voxels or pillars for a 2D CNN; the per-
point network is a PointNet (Qi et al., 2017) in both, the pooled-set construction that Deep Sets (Zaheer
et al., 2017) formalises, and attention-based set encoders (Lee et al., 2019) extend it with relations
between points. SPLATNet (Su et al., 2018) splats point features onto a permutohedral lattice, and
Lift-Splat-Shoot (Philion and Fidler, 2020) splats image features into a bird’s-eye grid. On the rendering
side, spatial transformer networks (Jaderberg et al., 2015) made bilinear sampling differentiable, and
soft rasterisers (Kato et al., 2018; Liu et al., 2019) do the same for the transpose direction, geometry to
pixels. Outside computer vision, the encoder and decoder of GraphCast (Lam et al., 2023) pass messages
between a latitude–longitude grid and a mesh graph, a learned transfer between the two representations
where ours is a fixed write at measured coordinates. These systems differ in where an entity’s features
land. VoxelNet, PointPillars and Lift-Splat-Shoot bin each entity to one cell, the last assigning every
point to its nearest pillar before sum pooling, so sub-cell position is discarded at the write; SPLATNet
instead distributes each point over the surrounding lattice vertices with barycentric weights. Splatting
with fractional weights is itself established machinery, in the bilateral grid (Chen et al., 2007), in the
bilinear scatter-add of softmax splatting for forward warping (Niklaus and Liu, 2020) and in differentiable
surface splatting (Yifan et al., 2019); the nearest-versus-interpolated question has been raised inside the
pillar literature in the opposite, gather direction (Wang et al., 2020). Our operator is the bilinear case of
that family written onto a Cartesian grid, with a per-entity encoder that is Deep-Sets-like in arm D and
relational in G2G. What is new is not the operator but its use: entities are players whose sub-cell position
and own features carry the signal, the grid is a pitch surface supervised at one observed endpoint per
pass, and the paper prices each element of the front end under a pre-specified multi-seed protocol.
    Graph-to-Grid is our name for the family of models studied here, not an established term, and the
words are already in use elsewhere. Lyu et al. (2023) lay general graphs out on a 2-D grid so that a CNN
can read them, and Jin and Li (2023) use G2G for a graph-to-grid module that recodes graph-structured
physiological features as a 2-D array, also for a CNN. The abbreviation is in use for graph-to-graph models
as well. In all of those the grid is a layout to be learned or optimised; here it is the pitch, every entity is
written at its measured physical position, and no graph is emitted.

Value, evaluation and data validity. VAEP (Decroos et al., 2019), pass risk/reward decomposi-
tion (Power et al., 2017) and line-breaking analyses of the same tournament (Karakuş and Arkadaş, 2026)
are reminders that expected possession value is one of several defensible semantics. Davis et al. (2024)
separate model accuracy from indicator validity, and van Arem et al. (2026) quantify such indicators’
estimation error against a ground truth football cannot observe. Broadcast tracking carries provider-
dependent position error (Crang et al., 2026; Mills et al., 2026), quantified in Sec. 7. Dwork et al.
(2015) formalise how sequential holdout reuse erodes a holdout’s guarantees, which is the reason the
attribution ladder was repeated under a pre-specified protocol. Temperature scaling follows Guo et al.
(2017). Multiplicity control follows Holm (1979) and, for the joint sign-flip test, the max-𝑇 construction
of Westfall and Young (1993). Reporting is guided by the checklist of Pineau et al. (2021).


3     Data, targets and quality control
Every pass in the primary corpus is a real pass from the World Cup, with its destination read off the
tracking data where the ball flight resolves to a tracked next-possession event (98.9% of admitted passes)
and taken from a geometry-derived boundary exit or a receiver-capture rule for the remainder (Sec. 3.2).

3.1   Corpus, loader and split
We use the PFF FC release (PFF FC, 2024) covering all 64 matches of the 2022 FIFA World Cup: event
JSON, metadata and broadcast tracking; our copy stores smoothed tracking at 29.97 Hz, about 50 GB and
on the order of 107 frames. It gives full-tournament coverage without instrumented stadiums, at the cost
of players leaving frame, intermittent ball visibility and smoothing artifacts, so the pipeline treats data


                                                      5
      64 matches, 2022 FIFA World Cup, partitioned by match
      label-blind deterministic split: the final is pre-declared as test; the other 63 are ranked by SHA-256(version | seed | gid)


                                                     train                                                   validation              test

                                                  48 matches                                                  8 matches        8 matches
                                                 40,047 passes                                               7,385 passes     6,196 passes



       Train                              Validate                           Commit and lock                   Test
       48 matches                         8 matches                          commitment hashed                 8 matches
       four heads: PP, PS,                early stopping                     before any test pass;             6,196 shared passes
       PE-succ and PE-miss                temperature scaling                lock binds predictions            opened once by the rule




Fig. 1 The shared 48/8/8 match-grouped protocol: a label-blind deterministic split, validation-only early stopping
and temperature scaling, and a hash-committed test evaluation of 6,196 shared passes, which the protocol opens
once per arm. In the realised runs the G2G arm opened them twice, the first cycle aborted by an automated integrity
failure and each control opening once; the records are in Sec. 5.3 and Sec. 7


quality as a modeling problem. The corpus contains 53,628 admitted passes at 83.8% completion, split
48/8/8 by match into 40,047 training, 7,385 validation and 6,196 test rows (Fig. 1).
    All raw access flows through one self-verifying loader whose audited source modules are embedded
as SHA-256-checked payloads; any modification fails the import. A ball-in-play state machine closes play
at out-of-play, period end and awarded fouls and reopens at set-piece releases or first open-play control.
We additionally mask the 5 s after free kicks, corners, throw-ins and penalties, removing set-piece routines
from an open-play pass model. Quality intervals flag illegal roster sizes, observational blackouts, provider
dead time, frozen scenes, inter-frame gaps and impossible speeds, and a pass snapshot is admitted only
under joint constraints on event–frame latency, roster completeness at the snapshot and at the 1 s-earlier
frame used for finite-difference velocities, actor–ball distance and tracking-run continuity. Coordinates
are rotated per possession so the acting team always attacks toward 𝑥 = 105.
    Matches are split 48/8/8 by a label-blind deterministic rule: the final is pre-declared as a test anchor
and the remaining 63 are ranked by SHA256(version | seed | gid) with seed 1907, so no outcome or model
output can influence membership. A 192-file SHA-256 manifest binds the raw data to the split signature
16cf1b7a..., identical across arms.

3.2   Tracking-grounded endpoints
Where a pass ended is the label the selection model is scored against, so we take it from the tracking
rather than from annotation. Each eligible pass opens a 6 s ball-flight window resolved to the tracked
ball position at the next possession event (53,041 passes, 98.9%), a geometry-derived pitch-boundary
intersection (476, 0.89%), or the first frame where the ball comes within 1 m of the annotated receiver
after ≥2 m of travel (111, 0.21%); unresolved flights are quarantined. Where we stratify by provenance
the reported strata are next-event (6,135 rows) and boundary geometry (52); the 9 receiver-capture rows
are too few to bootstrap and are omitted there, though present in every pooled number. Admission is not
outcome-blind in effect even though it is outcome-blind by rule: completion rates are 83.8%, 85.3% and
81.9% in the training, validation and test splits, and 6.6%, 5.9% and 7.4% of passes carry a nonzero value
label. The loader logs every gate; the per-gate exclusion count on this corpus (68,566 candidate pass
events, 11,003 removed by the ball-in-play contract, 3,935 by the snapshot and endpoint gates, 53,628
admitted) and the admission rates by pass type are given in Supplement Sec. S3, Tables S2 and S3. A
validation of the endpoint rule against manual annotation is not part of this paper (Sec. 7). The public
seven-match corpus that Sec. 6.2 uses as a second provider is built by the same rules; its construction is
specified in full in Supplement Sec. S2.



                                                                        6
3.3   Targets
Let 𝑘 ∗ be the grid cell of the observed endpoint on the 104 × 68 grid (≈1 m cells, 7,072 cells). PP (pass
probability) is trained with binary cross-entropy between the completion label 𝑦 ∈ {0, 1} and 𝜎(𝑧 𝑘 ∗ ), the
sigmoid of the logit at the observed endpoint cell; PS (pass selection) as a 7,072-way softmax with 𝑘 ∗ as
the target class. PE (pass value) regresses a signed 15-second expected-goal balance,
                                h    Ö            i h    Ö             i
                           𝑟 = 1−       (1 − 𝑥 𝑠 ) − 1 −     (1 − 𝑥 𝑠 ) ∈ [−1, 1],                       (1)
                                   𝑠∈𝑆own                 𝑠∈𝑆opp

over shots by each team within 15 s of the pass, 𝑥 𝑠 being an expected-goal value clipped at 0.999. The xG
estimator is external to the tournament: an XGBoost classifier (Chen and Guestrin, 2016) fitted on the
80,304-shot training partition of a 4,171-match, 106,787-shot StatsBomb open-data corpus (StatsBomb,
2018) from which the 2022 World Cup was removed before cache construction (match-grouped 75% split;
26,483-shot diagnostic holdout, log-loss 0.285). Two heads condition on outcome, PEsucc on completed
and PEmiss on missed passes, each regressing 𝑟˜ = (𝑟 + 1)/2 of Eq. (1) under MSE at 𝑘 ∗ ; predictions map
back by 𝑣ˆ = 2𝜎(𝑧) − 1 onto the signed [−1, 1] scale. The combined surface is
                                                                    
                               b(𝑘) = 𝑝(𝑘)
                               𝑉        ˆ    𝑣ˆ succ (𝑘) + 1 − 𝑝(𝑘)
                                                               ˆ      𝑣ˆ miss (𝑘).                      (2)

Because every head is supervised at a single observed cell 𝑘 ∗ per pass, the surfaces away from 𝑘 ∗ are
extrapolations of the network, a point Sec. 7 returns to under calibration.


4     Method
G2G describes each player, paints that description onto the pitch where the player stands, and reads the
painted pitch with a convolutional network. It is built as three layers around the original SoccerMap
(Fig. 2), and each layer is one arm of the experiments.

4.1   What is new, and what is inherited
The interface is established; the contribution is its evaluation. A differentiable splat writes entity features
into a grid, and endpoint supervision reaches any encoder that produced them. The study compares bilinear
and nearest-cell placement, raw and learned features, and raster and attention alternatives. Fractional-
weight splatting, the SoccerMap architecture, and the completion/selection/value decomposition are
inherited (Sec. 2). Raw painting is the simpler recommended baseline; the learned G2G front end has
the better in-distribution selection likelihood in the primary comparisons.
    The system nests. SoccerMap is the base: raster channels in, a three-scale fully convolutional
network, a logit surface out. SoccerMap-v2, our name for the modernised core and not a release by the
SoccerMap authors, keeps that layout and input but modernises every block (Sec. 4.2); alone, it is arm C.
The painted front end adds a per-node network and the splat (Sec. 4.3), 36 learned channels alongside
the raster stack; with it, arm D. G2G replaces the per-node network with the relational encoder (Sec. 4.4).
The chain SoccerMap → v2 → D → 𝐺2𝐺 is also the attribution ladder of Sec. 6.4.1; the arms are
specified, with parameter counts, in Sec. 5.1.

4.2   SoccerMap-v2: the surface core
The core reads the raster stack of Fernández and Bornn (2021); Fernández et al. (2021): 13 channels
for PP/PS and 15 for PE, plus a 16th carrying the model’s own raw PP surface (Sec. 5.2). In the arms
that paint, the 36 painted channels are concatenated to it, giving input widths 49 and 52. The core
keeps SoccerMap’s three scales, processing at 1×, 21 ×, 14 ×, and differs in the blocks. Widths become
(32, 48, 64). Each scale’s pair of plain 5 × 5 convolutions becomes a residual (He et al., 2016) block
with GroupNorm (Wu and He, 2018) and GELU (Hendrycks and Gimpel, 2016), followed by squeeze-
and-excitation (Hu et al., 2018); the coarsest scale adds dilated convolutions. SoccerMap’s per-scale

                                                      7
 Attribution ladder: each layer adds one arm around the one inside it

   G2G: relational encoder                                                                                                        G2G
   Replaces the per-node network with two edge-aware message-passing
   blocks (width 32), so every 12-d embedding depends on all players.

      Painted front end                                                                                                        arm D
      Per-node MLP → 12-d embedding per player and ball, splatted at each
      continuous position as 36 channels; with the nine raw features instead, Draw.

         SoccerMap-v2                                                                                                    arm C
         Same three scales (1×, ½×, ¼×), widths 32/48/64; residual GroupNorm/GELU
         blocks, squeeze-and-excitation, dilations, pyramid path, 1×1 head.

            SoccerMap                                                                               original / wide controls
            Raster stack (13 or 15 channels, plus raw PP for PE) read
            by a three-scale surface CNN, widths 32/64 (wide 52/102).




 Data path, one forward pass

  Snapshot graph                Encoder                           Splat                   v2 core                    Four surfaces
  22 players and ball           G2G: message passing              36 painted channels     3 scales, pyramid          PP, PS,
  9 node, 8 edge feat.          arm D: per-node MLP               + raster stack          1×1 head → logits          PE-succ, PE-miss
                                Draw: no encoder




Fig. 2 G2G as three layers around the original SoccerMap, each layer one arm of the attribution ladder. Innermost,
SoccerMap: raster channels read by a three-scale surface CNN (the original and wide controls). SoccerMap-v2
(arm C) keeps that layout with residual GroupNorm/GELU blocks, squeeze-and-excitation, dilations and a pyramid
path. The painted front end (arm D) describes every player and the ball in 12 numbers and splats them onto the grid
at each one’s continuous position as 36 extra channels. G2G replaces that per-node network with two edge-aware
message-passing blocks; Sec. 6.4.1 prices that replacement; with the nine raw node features painted in place of the
embedding, the front end is Draw . Below, the data path


predictions with nonlinear upsampling and concatenation fusion become a top-down pyramid path (Lin
et al., 2017) that restores full resolution before a single 1 × 1 head emits the logit surface. PP, PS, PE-succ
and PE-miss are independently trained instances of the whole network; no weights are shared across
heads or arms.

4.3    The painted front end: splatting
Each player and the ball is a node with nine features — normalised position, velocity, team and ball-role
identity — on fixed physical scales, nothing fitted to the corpus. A per-node network maps those features
to a 12-dimensional embedding 𝑒 𝑖 ∈ R12 , and the splat writes that embedding into the surface domain
at the node’s continuous grid coordinates. The features can also be painted directly, with no network,
and Sec. 6.4.2 compares them with learned per-node embeddings. Let (𝑢 𝑖 , 𝑣 𝑖 ) be node 𝑖’s position in
cell units, let ( 𝑢¯ 𝑖 , 𝑣¯ 𝑖 ) = ( ⌊𝑢 𝑖 ⌋, ⌊𝑣 𝑖 ⌋) and (𝛿𝑖 , 𝜖𝑖 ) = (𝑢 𝑖 − 𝑢¯ 𝑖 , 𝑣 𝑖 − 𝑣¯ 𝑖 ). For each of the three groups
𝑔 ∈ {attackers, defenders, ball} the painted channel block 𝑆 𝑔 ∈ R12×68×104 is
                                      ∑︁ ∑︁
                 𝑆 𝑔 [𝑐, 𝑦, 𝑥] =                       𝑤 𝑎𝑏 (𝛿𝑖 , 𝜖𝑖 ) ⊮[𝑥 = 𝑢¯ 𝑖 + 𝑎] ⊮[𝑦 = 𝑣¯ 𝑖 + 𝑏] 𝑒 𝑖 [𝑐],           (3)
                                        𝑖 ∈𝑔 𝑎,𝑏∈ {0,1}

                      𝑤 𝑎𝑏 (𝛿, 𝜖) = 𝛿 𝑎 (1 − 𝛿) 1−𝑎 𝜖 𝑏 (1 − 𝜖) 1−𝑏 ,

The implementation uses cell-centre coordinates

                  𝑢 𝑖 = clip(𝑊𝑥𝑖 /105 − 1/2, 0, 𝑊 − 1),                      𝑣 𝑖 = clip(𝐻𝑦 𝑖 /68 − 1/2, 0, 𝐻 − 1)


                                                                        8
for physical positions (𝑥𝑖 , 𝑦 𝑖 ), with 𝑊 = 104 and 𝐻 = 68. The upper neighbours are clipped to the
last valid indices. Coincident boundary contributions accumulate, so the weights still sum to one;
clipping sacrifices positional resolution in the outer half-cell strips. Masked nodes contribute zero. An
implementation audit checks signed-feature conservation, permutation invariance, boundary cases, and
embedding and interior-coordinate gradients (Supplement Sec. S7). Equation (3) is therefore bilinear
weights over the four surrounding cell centres accumulated by scatter-add, 3 × 12 = 36 channels in all.
This is the painting step. It is linear in the embeddings and its Jacobian with respect to 𝑒 𝑖 is the weight
pattern itself, so the surface loss backpropagates through the grid into whatever network produced the
embedding. Positions are inputs here, and the map is differentiable in them almost everywhere, with kinks
at cell boundaries. Three properties matter for what follows. First, a node sitting a fraction 𝛿 inside a cell
contributes 1 − 𝛿 of its embedding to that cell and 𝛿 to the next, so the painted channels carry sub-cell
position up to bilinear interpolation, whereas an occupancy raster carries only the cell. When two nodes
of one group fall in the same cell their contributions add. Second, the operator is permutation-invariant
within a group and defined for any number of nodes (its output scales with that number, fixed here at 22
players plus the ball up to players out of frame). Third, nothing in the operator is fitted: every parameter
of the front end lives in the embedding network. With a per-node MLP as that network, the front end
is arm D: nodes are described independently and never exchange information. With the nine raw node
features in place of the embedding, it is Draw , which fits no front-end parameter at all (Sec. 6.4.2).

4.4   The relational encoder
G2G replaces the per-node MLP with an encoder in which players see each other. The snapshot becomes
a fully connected graph over up to 23 nodes (up to 11 per side plus the ball) with eight directed
edge features of pairwise geometry. Two residual message-passing blocks of hidden width 32 follow
the graph-network formalism (Battaglia et al., 2018). The attention logits combine scaled dot-product
content similarity (Vaswani et al., 2017) with an edge-geometry bias, following attention over graph
neighbourhoods (Veličković et al., 2018; Brody et al., 2022):
                                                                  
                                                    ⟨𝑞 ,𝑘 ⟩
                                    𝛼𝑖 𝑗 = softmax √𝑖 𝑗 + 𝑏(𝑒 𝑖 𝑗 ) ,                             (4)
                                              𝑗 ∈ N (𝑖)       32

                                                                                                   Í
with 𝑏 a two-layer MLP on edge features. Messages 𝑚 𝑖 𝑗 = MLP𝑚 ( [ℎ 𝑗 ; 𝑒 𝑖 𝑗 ]) aggregate as 𝑎 𝑖 = 𝑗 𝛼𝑖 𝑗 𝑚 𝑖 𝑗
under a residual layer-normed update, and a linear layer emits the 12-dimensional embedding per node
that the splat paints. The encoder is permutation-equivariant and anonymous: no player identity is used.
Because the splat of Eq. (3) is linear in 𝑒 𝑖 and the attention of Eq. (4) is smooth in its inputs, the whole
chain from node features through message passing to the logit surface is differentiable. The endpoint
supervision of Sec. 3.3 is the only supervision the encoder ever receives.

4.5   Estimands, supervision and what the surfaces mean
Every head produces a dense output surface but is supervised sparsely, at the one observed endpoint
per pass, and the three heads estimate different things. PP estimates the probability that a pass played
to a cell is completed, conditional on that cell being the observed endpoint. It is trained with binary
cross-entropy at 𝑘 ∗ only, so its values at cells the passer did not choose are extrapolations by the network
from historically chosen endpoints, and no label ever tests them. PS estimates the distribution of the
observed next endpoint over the 7,072 cells: its softmax gradient touches every logit, so PS is the one
head whose whole surface is shaped directly by the loss. PE estimates the expected value of the signed
15-second expected-goal balance, conditional on outcome and endpoint, again supervised at 𝑘 ∗ only. The
endpoint is where the ball was next observed, not where the passer intended it to go (Sec. 7). Away from
observed endpoints the convolutional core supplies only its locality and weight-sharing biases, not an
explicit smoothness constraint. This is the standard SoccerMap arrangement, and it is the reason we report
both target-pixel metrics and, for selection, the full distribution’s mass and rank statistics. Wherever this
paper says a surface is calibrated, it means temperature-scaled at observed endpoints; calibration away

                                                          9
Table 2: The three shipped arms (top) and the three attribution arms (bottom); Draw trains PP and PS heads only.
All share data, targets, loader, split, optimiser, losses, calibration, metrics and evaluation code. The convergence
reruns of Supplement Sec. S5.4 retrain only the two controls’ PS heads with the epoch cap raised to 200 and
are otherwise identical to their shipped counterparts. Parameter counts refer to our instantiations; the published
SoccerMap leaves some widths unspecified

    Arm                                            PP/PS parameters      PE parameters    Input / system
    G2G                                                      700,353           702,753    graph + splat + raster
    Original SoccerMap                                       274,251           276,651    raster only
    Wide SoccerMap                                           698,573           702,473    raster only
    Arm D (splat, no message passing)                        684,479           686,879    splat + raster
    Arm Draw (raw features painted, no encoder)              676,499                —     splat + raster
    Arm C (SoccerMap-v2 alone)                               654,899           657,299    raster only


from them is not established (Sec. 7). Optimisation, early stopping, calibration and the leak-free stacking
of the PP surface into the PE heads are shared by every arm and are specified in Sec. 5.2.

4.6    Implementation
The models are implemented in PyTorch. The shipped arms trained from the original notebooks, and
the multi-seed studies from a standalone training engine that reproduces the shipped predictions to a
maximum absolute probability difference of 1.63 × 10−4 . AI assistance with code and text is described
in the Statements and Declarations.


5     Experimental protocol
Every arm sees the same matches, the same passes, the same training allowance and the same scoring
code, and each evaluation opens the held-out test matches (the holdout) only after the models are frozen.
This section specifies the arms, the shared training recipe, the evaluation records, the inference machinery
and the thirteen pre-specified studies; the supplement gives each study’s design in full.

5.1    Arms
Original SoccerMap is a topology-faithful reproduction of Fernández and Bornn (2021): three scales,
two 5 × 5 convolution+ReLU blocks per scale at widths 32/64, 1 × 1 prediction at every scale, nonlinear
upsampling and concatenation fusion, consuming the same deterministic channels and no graph channels.
It totals 274,251 parameters; the published architecture leaves some widths unspecified, so all control
counts here refer to our instantiations. Wide SoccerMap is the identical topology at widths 52/102,
chosen so its parameter count matches G2G: 698,573 vs. 700,353 for PP/PS, a difference of 1,780
parameters (0.25%), and 702,473 vs. 702,753 for PE (0.04%). No advantage of G2G can be attributed to
parameter count alone.
     Two further arms split the front end. Arm C is SoccerMap-v2 alone, fed only the deterministic
channels, with the painting step and node encoder deleted together (654,899 PP/PS parameters). Arm D
restores the painting step and a per-node MLP but removes both message-passing blocks, so nodes are
described independently and never exchange information (684,479; its projector holds 780 of G2G’s
16,654 projector parameters). The chain wide → C → D → 𝐺2𝐺 isolates, in order, SoccerMap-v2,
the painting interface and message passing. The graph branch’s full marginal cost over arm C is 45,454
parameters: 16,654 in the projector plus 28,800 that the 36 painted channels add to the core’s first
convolution. That is a 6.9% increase over SoccerMap-v2 and 6.5% of the final model. Table 2 lists every
arm with both head groups’ counts.




                                                        10
5.2   Training, calibration and stacking
Here “tuned” means learning-rate selection on the stated grid, not exhaustive hyperparameter optimisation.
“Converged” is shorthand for satisfying the stated validation early-stopping rule before the epoch cap; it
is not a claim of numerical or global optimisation convergence.
     All shipped arms trained with Adam under bf16 autocast on a single RTX 5090 (mean logged epoch
42.6 s for G2G against 19.8 s and 20.5 s for the controls; training windows 0.917, 1.379 and 0.912 h). The
pre-specified studies trained on an NVIDIA RTX PRO 6000 Blackwell workstation GPU, the attribution
ladder among them in under four GPU hours. Every arm shares per-head learning rates (PP 10−4 , PS
10−5 , PE 10−6 ), batch sizes, recorded seeds (which in the shipped runs governed data order only; Sec. 7),
and early stopping on the validation objective (patience 5, cap 50 epochs, an epoch being one full sweep
through the training data). We call this shared setting the recipe; Supplement Sec. S13 tabulates every
input feature, hyperparameter and selected epoch and temperature. After weights freeze, one scalar
temperature per probabilistic head is fitted on validation only: a single number improving agreement
between predicted percentages and observed frequencies, binary for PP, spatial for PS (Guo et al., 2017).
PE is left uncalibrated. Because PP is trained and scored at the historically chosen destination cell, this
is target-pixel calibration.
     The PE heads consume the arm’s own raw PP surface as an input channel. To prevent a producer
from scoring a match it trained on, the training matches are partitioned into four interleaved folds and
a dedicated PP producer predicts only its held-out fold. Validation and test rows receive surfaces from
the main PP model, which never trained on them; a 53,628-row provenance table records the producer of
every row.

5.3   Evaluation records
Before any test forward pass, each evaluation cycle writes a hash-verified commitment freezing the test
match list, checkpoint hashes, both temperatures, a metric menu and the hash of eight pre-declared scenes.
A later lock binds it to the prediction-file hashes. The shipped arms were evaluated on 14, 16 and 17
August 2026 on the same eight matches. The G2G arm’s log records two commitment/evaluation cycles,
the first aborted by an automated integrity failure; Sec. 7 discusses the consequence and Supplement
Sec. S8 prints the discarded cycle in full.

5.4   Paired inference
Estimands. The eight test matches are the resampling units: passes within a match are not independent,
teams recur across matches, and the final was anchored by rule rather than drawn. The pass-weighted
estimand is the difference in a metric between two arms over the population of passes from which the
6,196 test passes are a sample; it is estimated by the pooled difference over all test rows. The equal-match
estimand is the expected per-match difference over the population of matches; it is estimated by the mean
of the eight per-match differences, which weights the final and a group-stage match equally. Both are
reported for every contrast (Supplement Table S31), together with a leave-final-out pooled estimate for
the primary metrics.

Interval estimation. Because all arms are scored on identical rows, the comparative question is an-
swered by resampling the eight test matches with replacement (𝐵 = 10,000, seed 1907) and recomputing
Δ = 𝐺2𝐺 − control on the same resampled rows in each replicate. We report percentile match-cluster
bootstrap intervals (Efron and Tibshirani, 1994) obtained from those 10,000 resamples; bias-corrected
and accelerated intervals agree on the exclusion of zero in every case. The 13-metric family, the set of
hypotheses over which multiplicity is controlled, spans PP log-loss, Brier, AUC and ECE, and five PS
metrics: NLL, mean argmax distance, probability mass within 3 m and 5 m of the observed endpoint, and
the rank fraction of the observed cell. It also spans both PE-branch MSEs and combined EPV MSE and
MAE.


                                                    11
Sign-flip inference and its scope. With eight clusters, bootstrap tail proportions are floored at 1/𝐵 and
are not valid confirmatory 𝑝-values: few-cluster cluster bootstraps over-reject (Cameron et al., 2008),
and an uncentred tail proportion is not a test of a null. We therefore prioritise the joint sign-flip max-
𝑇 analysis over those√bootstrap tail probabilities. We studentise the eight match-level paired deltas,
𝑡 = mean(𝑑)/(sd(𝑑)/ 8), and recompute 𝑡 under all 28 = 256 cluster sign-flip patterns; the single-step
max-𝑇 adjusted 𝑝 (Westfall and Young, 1993) for comparison 𝑗 is the fraction of patterns whose family-
wide maximum |𝑡| reaches the observed |𝑡 𝑗 |. Its error control assumes that the paired match-level deltas
are exchangeable in sign under the joint null, an assumption that match grouping motivates but does not
guarantee (Sec. 7); a global flip leaves |𝑡| unchanged, so the 128 mirror pairs make 2/256 = 0.0078
the smallest attainable adjusted 𝑝, still below 𝛼. The statistic tests the equal-match estimand, so it is
the natural companion of the equal-match column in every table. For the multi-seed studies the same
test is applied to the seed-averaged per-match differences, which conditions on the seeds drawn; the
hierarchical bootstrap of Sec. 5.5 supplies the intervals that carry seed variability. For comparability
with the earlier analysis, Holm adjustment (Holm, 1979) of the bootstrap 𝑝-values is also reported in
every full-family table of the supplement. It is applied post hoc across the 26 reported contrasts of this
retrospective comparison (the shipped commitment fixed a broader metric menu, and this 13 × 2 family
and its correction were settled after the locked predictions existed) and within the pre-declared family of
each later study. Where the two procedures, max-𝑇 and Holm, disagree, the max-𝑇 verdict is the one
the paper reports. Two unadjusted per-comparison checks of the shipped family, the exact sign-flip and
Wilcoxon tests, are given in Supplement Sec. S9.

5.5   Pre-specified multi-seed studies
Every study after the shipped comparison was run under a stricter discipline than that comparison, and
all share an auditable workflow, with study-specific families and seed counts. Each writes a self-hashed
commitment record before any of its runs begins training. The record fixes the run matrix (arm × seed,
with every fit seed derived from a recorded seed base by a fixed formula), the study-specific metric family
(14 metrics for full four-head studies, and 10 PP/PS metrics where value is not evaluated), two primary
endpoints (calibrated PP log-loss and calibrated PS NLL), the comparison pairs, the Holm family and
𝛼 = 0.05, and the bootstrap design. It also fixes a test-set policy: no test label is read before a lock
record has hashed every checkpoint of every run. Training touches train and validation rows only; the
one array written during training that spans test rows is the PE raw-PP input channel, which is forward
inference of the run’s own PP model and consumes no label. Evaluation refuses to train and fails if any
checkpoint is missing or no longer matches its locked digest. The commitment also records the SHA-256
of every code file involved, and the later phases refuse to proceed under code drift. One study needed
an override: in Study 3 an analysis-arm naming rule was repaired after the lock and after the single test
opening, before any analysis output existed, and the analysis was re-run with the drift recorded in the run
status; the training runs, the locked predictions, the metric family, the pairs and the bootstrap design are
as committed.
     A pre-submission audit found two further defects, both in the analysis code of the two cross-validation
studies. In Studies 5 and 12 Part A the sign-flip max-𝑇 divided every sign-flipped cluster mean by the
standard error of the observed deltas instead of recomputing it under each pattern, as this section specifies
and as the other eleven studies implement; and the AUC and calibration-error intervals resampled a row-
weighted mean of per-match values while the printed estimate is the metric on the pooled predictions.
Both families were recomputed from the same locked predictions, under the committed bootstrap draws
and sign patterns, with the studentised statistic described above and the exact pooled resampling used
elsewhere in the paper. The point estimates are unchanged, no rejection is lost, nine further hypotheses
across the two families newly clear max-𝑇, and no interval changes whether it excludes zero. The
correction can only lower these 𝑝-values: dividing each hypothesis by a constant leaves a valid but
under-powered variant of the same single-step test, so no rejection reported here depends on the change
having gone in our favour. One reading is strengthened by it, the learned-content increment of Sec. 6.1,
which now clears both procedures on every metric of its family except calibration error. The uncorrected

                                                     12
families are retained beside the corrected ones.
     The analysis is a hierarchical bootstrap, described here for the three-seed holdout studies; the tuned
studies draw five seeds, the cross-validation resamples 64 match clusters with one seed per fold, and the
external studies resample seven. Each of 𝐵 = 10,000 replicates draws the 8 test matches with replacement
and the 3 seeds with replacement, independently; each arm’s metric is the mean over the drawn seeds
evaluated on the drawn rows, and the pair delta is 𝐴 − 𝐵 under that same draw. Its intervals therefore
carry match and initialisation variability together. Two-sided 𝑝-values are 2 min{𝑃(Δ ≤ 0), 𝑃(Δ ≥ 0)},
floored at 1/𝐵, and Holm-adjusted over the pooled family. Every bootstrap statistic is computed from
per-match sufficient statistics, so a resample is an exact contraction rather than a re-scan of the 6,196 rows.
The fixed-bin ECE and the Mann–Whitney AUC decompose exactly, and the analysis script re-derives a
sample of replicates the naive way and asserts equality.
     One engine amendment applies to every one of the pre-specified studies and matters for the repro-
ducibility note in Sec. 7: seeding now runs before model construction, so a recorded seed fixes weight
initialisation as well as data order. Replicate 𝑟 ∈ {1, 2, 3} uses seed base 1907 + 100,000 𝑟; seed base
1907 reproduces the shipped runs’ data order.
     Table 3 lists the thirteen studies in the order in which they are introduced here, with the archive
folder that holds each one’s commitment record, lock record, runs and analysis. Supplement Sec. S1
gives every study’s design as it was committed: arms, seeds, comparison pairs, family, bootstrap, and
the time and signature of the commitment; each results subsection restates the design of its own study.
Studies that reuse reference predictions pin their digests in the commitment; the cross-validation, tuned,
and external-retraining protocols instead fit the arms specified for those protocols. Study 4 and Study 11
are adaptive by design and pre-specified as such. A validation-only sweep on seed 1 trains each head at
every rate of a committed grid to a cap of 200 epochs. A committed rule selects the rate with the lowest
best-validation loss and signs the selection. Seeds 2–5 train at the chosen rates, and the test set is opened
once after every checkpoint is locked.
     Study 12 takes the raw-feature painted arm Draw of Study 3 (676,499 parameters: the 13 raster
channels plus the 27 painted raw node features, no learned encoder) through both primary protocols,
in two parts with separate commitment records, each signed before any run of its part began training.
Part A trains it in the eight folds of Study 5 at the shipped recipe, one seed per fold with the Study 5 seed
bases and fold table, and compares its pooled out-of-fold predictions with the locked Study 5 out-of-fold
rows of C and G2G: two pairs (Draw −C, G2G−Draw ), a family of 20, the 64-cluster bootstrap and the
Monte-Carlo max-𝑇 test of Study 5. Part B takes it through the Study 4 protocol, a validation-only sweep
on seed 1 over the Study 4 grid, the committed selection rule, seeds 2–5 at the chosen rates, cap 200,
against the locked Study 4 tuned runs of C and G2G: two pairs, a family of 20, a hierarchical bootstrap
over 8 matches and 5 seeds and the exact 256-pattern max-𝑇 test. Neither reference arm is retrained in
either part.
     Study 13 asks whether the interface effect is a property of the painting step rather than of the
SoccerMap-v2 core. Two arms are built on a canonical three-level 2-D U-Net at widths 32, 72 and 160,
the triple closest to the doubling pattern among the 31 of the 7,564 enumerated width triples that land
within 1% of arm C’s parameter count: Uraster reads the 13 raster channels (652,833 parameters) and Uraw
the same channels plus the 27 painted raw node features of Draw (660,609; the 7,776 extra parameters
all in its first convolution). Each trains PP and PS heads at the shipped recipe under the three Study 1
seeds and is compared with the locked runs of C and G2G (Study 1) and Draw (Study 3), never retrained:
four pairs (Uraw −Uraster , Uraster −C, Uraw −Draw , Uraw −G2G), a family of 40, a hierarchical bootstrap over
8 matches and 3 seeds, the exact 256-pattern max-𝑇 test; its commitment was signed before training.

Reporting priorities. Each study’s commitment fixed its metric family, comparison pairs, and Holm
over the family and the bootstrap design, and none of that is changed here. Every family is reported
in full, with both estimands and both procedures, in the supplement tables that the summary tables of
Sec. 6 cite. In the text, each study is reported through its two primary endpoints, calibrated selection
NLL and calibrated completion log-loss, with the two localisation metrics, probability mass within 5 m


                                                      13
Table 3: The thirteen pre-specified studies. Study is the name used in this paper; archive is the study’s original name,
under which the study archive holds its commitment record, lock record, runs and analysis (folder overnightN,
lower case, no hyphen; the archive keeps its original names); commitment is the first eight hex digits of the SHA-
256 signature of the self-hashed commitment record written before any run of the study began training. LOMO:
leave-one-match-out. The shared design, the per-study families and every deviation are given in Supplement Sec. S1

      Study Archive        Sec.   Commitment Arms × seeds                             Tests
       1    Overnight-2    6.4.1 1f549421     G2G, C, D × 3 seeds; cap-200 PS         attribution ladder: front end, painted pack-
                                              reruns of both controls                 age, message passing
       2    Overnight-3    6.8    7522b56a    original, wide × 3 seeds vs. locked     shipped comparison with seed variance on
                                              G2G                                     both sides
       3    Overnight-5    6.4.2 0bf9037a     Dnearest , Dgauss , Draw , Cmatched ,   painting geometry, anti-aliasing, learned
                                              G2Gnearest × 3                          vs. raw features, parameter count
       4    Overnight-4    6.3    07be9096    G2G, C, original, wide × 5 seeds,       per-arm learning rate and convergence
                                              tuned
       5    Overnight-6    6.1    3789298f    4 arms × 8 folds, all 64 matches the effect over the whole tournament
       6    Overnight-7    6.6    5c107078    Dattn , SetOnly × 3              attention painter; raster-free set decoder
       7    Overnight-8    6.2    4ff4c7ab    4 arms: zero-shot (3 seeds) and 7transfer and replication on a second
                                              LOMO folds on IDSSE              provider
       8    Overnight-9a   6.5    5cef6d46    Coffsets , originalsplat × 3     sub-cell offsets on the raster; the splat on
                                                                               the original core
        9   Overnight-9b 6.5      6629aeb1    Chalf , originalhalf × 3         a raster four times finer
       10   Overnight-10a 6.2     341c1f84    Draw : zero-shot (3 seeds) and 7 the raw-feature painter across the provider
                                              LOMO folds on IDSSE              boundary
       11   Overnight-10b 6.6     faafcd51    Dattn , SetOnly × 5 seeds, tuned the interface alternatives at their own learn-
                                                                               ing rates
       12   Overnight-11   6.1    261af843    Draw : 8 CV folds (A); tuned × 5 the recommended variant under the pri-
                                              seeds (B)                        mary protocols
       13   Overnight-12   6.5    3327ef11    Uraster , Uraw × 3               the interface effect on a canonical U-Net
                                                                               core



and argmax distance, alongside. Effect sizes and intervals come first and the max-𝑇 adjusted 𝑝 is the
prioritised inferential summary, subject to the assumptions above. Where a study has seeds, the per-seed
standard deviation of the pooled difference is printed beside the interval so that an effect can be read
against its own initialisation spread. This reporting choice was made after the studies had run; it relabels
no family and no procedure as pre-specified, and the Holm verdicts remain in the supplement tables and
their captions.
    Studies 1, 2, 3, 4, 6, 8, 9, 11 and 13 and Part B of Study 12 run on the previously used eight-match
holdout and are not evaluations on new data. Studies 7 and 10 are the two studies on data from outside
the tournament. Study 5 first scores 56 of the 64 matches as test cases (Sec. 7); Part A of Study 12 scores
the same 56 matches out of fold, against Study 5’s locked out-of-fold rows.


6    Results
Secs. 6.1 and 6.2 answer RQ1 of Sec. 1, whether the painted front end improves on the same core across
the tournament and across a change of provider; Secs. 6.3–6.6 answer RQ2, which part of the front
end carries the gain and whether it persists under per-arm tuning. Estimands and metrics are defined
in Secs. 4.5 and 5.4; where the pooled and equal-match estimands differ, both are shown. The primary
comparisons report effect sizes and intervals; frozen-model probes are descriptive sensitivity analyses.
The max-𝑇 sign-flip test is the prioritised inferential summary, exact over all sign patterns in the seven-
and eight-match studies and Monte Carlo in the 64-match comparisons, and where a study has seeds
the per-seed spread of the effect is printed beside its interval (Sec. 5.5). Throughout, a contrast clears
a test, or survives it, when its adjusted 𝑝 is below 0.05, and both procedures means max-𝑇 and Holm.
The subsections are ordered by evidential weight. The cross-validation over all 64 matches, the external
replication and the tuned, converged comparison (Secs. 6.1, 6.2, 6.3) carry the paper’s claim. The
attribution ladder, the front-end ablations, the raster controls and the interface alternatives (Secs. 6.4–6.6)
locate the mechanism on the reused holdout. The probes and the tracking-noise curves (Sec. 6.7) test what
the surfaces rely on. The three-arm comparison from which the design came is reported as development

                                                             14
                               World Cup
                            cross-validation             Learning-rate tuned            External retraining
                        64 matches; 1 seed/fold      8 reused matches; 5 seeds        7 matches; 1 seed/fold

                           -0.251                      -0.292                             -0.239
       Full front end
             G2G − C
       Raw painting             -0.186                       -0.225                            -0.178
          Draw − C

 Learned increment                        -0.065                        -0.067                          -0.061
       G2G − Draw
                         −0.3 −0.2 −0.1 0.0             −0.3 −0.2 −0.1 0.0             −0.3 −0.2 −0.1 0.0
                                         Selection NLL difference (nats)
Fig. 3 Primary selection evidence. Points show pooled NLL differences and bars show the reported pointwise 95%
bootstrap intervals; negative values favour the first arm. The full front end is G2G minus C, raw painting is Draw
minus C, and the learned increment is G2G minus Draw . These panels reuse the results of Studies 5, 4, 7, 10, and
12, not new experiments. Cross-validation intervals condition on one seed per fold; the tuned panel resamples
matches and seeds; external retraining has seven match clusters. Intervals are pointwise; the family-adjusted tests
are in the study tables


history (Sec. 6.8), and value, compute and the surfaces themselves (Secs. 6.9–6.11) close the section.
The pooled and equal-match estimands agree closely on every primary metric. Figure 3 summarises the
main selection contrasts; Sec. 6.10 examines their computational trade-off.

Reading the summary tables. Each main-text summary table gives the four headline metrics for each
pair shown of one study, in a common format; the full study tables, with every pre-declared pair and
metric, are in the supplement. Each pair spans two lines. The first gives the pooled difference Δ, the first
arm minus the second, so a negative value favours the first arm in the columns marked ↓ and a positive
value favours it in the column marked ↑, with its 95% interval. The second gives the per-seed standard
deviation of that Δ where the study has seeds, the number of test matches in which the first arm is ahead,
and the max-𝑇 adjusted 𝑝, with ◦ for a max-𝑇 rejection and ∗ for a Holm rejection over the study’s family
at 𝛼 = 0.05. Each caption then gives only what is particular to its own study: the design, the bootstrap,
the size of the family, and the supplement table that prints the family in full.

6.1   Cross-validation over the whole tournament
The interface effect holds over the whole tournament: against the same core fed rasters alone, G2G
improves selection NLL by −0.251 nats and leads in every one of the 64 matches. Selection NLL is the
mean negative log probability the calibrated surface places on the cell the pass actually reached, so a
reduction of 𝑑 nats is a factor of 𝑒 𝑑 in that probability on a geometric average. The headline 0.251 nats is
therefore a factor of about 1.29: by that average G2G places some 29% more probability on the observed
destination than arm C does. That is a relative statement about one cell of a 7,072-cell surface, not a
claim about any downstream decision. Every other World Cup study except Study 12 scores the same
eight matches (Sec. 6.8); Study 5 (Sec. 5.5) scores all 64 in eight match-grouped folds, the shipped test
set as fold 1 and the other 56 matches assigned by the same label-blind hash rule, each fold’s four arms
trained at the shipped recipe with one seed and tested on the fold they never saw. Arm C and G2G differ
only in the painted front end, so their contrast is the interface effect. Table 6 summarises the family;
Supplement Tables S4 and S5 give all 50 hypotheses and the two primary metrics fold by fold.



                                                        15
The effect holds on the 56 matches never before scored as test data. Pooled over the tournament,
G2G reaches a selection NLL of 5.024 against 5.275 for arm C, and its margin over the two SoccerMap
controls is between half a nat and seven tenths; completion log-loss improves by one to three hundredths
against every raster arm. G2G wins all 64 matches on selection NLL against every raster arm and on
every headline metric against both SoccerMap controls. With 64 clusters the smallest adjusted 𝑝 this test
can return is 10−5 rather than the 2/256 = 0.0078 of the eight-match studies, and every headline contrast
of the three G2G pairs clears both procedures at that floor; only the five calibration-error contrasts do not.
Tables 4 and 5 give these levels a scale, one for each supervised head, by scoring two models that need no
network on the same rows and folds. On selection, against a uniform surface and against a displacement
prior fitted on each fold’s training matches, every learned arm is ahead by more than two nats in all 64
matches, so the interface effect is about a tenth of the distance between the raster core and the stronger
null. On completion the same construction puts the interface effect at about a fourteenth of the distance
to its own null: the length prior reaches 0.397 of log-loss where arm C reaches 0.189 and G2G 0.174,
so the −0.015 the front end adds sits against a −0.207 gap between the prior and the core. Both nulls
are deliberately simple, and a richer network-free baseline would narrow these ratios. The controls order
differently on the two heads: on selection the wide control is ahead of the original, while on completion
the two are level, and both trail arm C.

Table 4: Selection null models under the Study 5 protocol: pooled out-of-fold metrics over all 53,628 passes and
64 matches. Uniform spreads its mass over the 7,072 cells. The displacement prior is a smoothed two-dimensional
histogram of the endpoint’s displacement from the ball’s cell at release, estimated on each fold’s 48 training matches
with the smoothing width chosen on its 8 validation matches, so it uses no test row and no network. Arm rows are
the locked Study 5 runs of Table 6. Every learned arm is ahead of both nulls in all 64 matches; the gap of arm C
over the displacement prior is −2.601 nats [−2.659, −2.542] (64-cluster match bootstrap, 𝐵 = 10,000) and of G2G
−2.852 [−2.913, −2.791]

                   Model                       Selection NLL     Mass <5 m       Argmax dist. (m)
                   Uniform over the grid                 8.864            —                      —
                   Displacement prior                    7.876         0.038                   18.1
                   Original SoccerMap                    5.727         0.214                   14.0
                   Wide SoccerMap                        5.544         0.233                   13.4
                   Arm C (SoccerMap-v2)                  5.275         0.276                   12.1
                   G2G                                   5.024         0.304                   11.3


Table 5: Completion null models under the Study 5 protocol: pooled out-of-fold metrics over the same 53,628
passes and 64 matches as Table 4, which gives the selection counterpart. The base rate is one constant, the
completion rate of each fold’s 48 training matches. The length prior is completion probability as a function of the
straight release-to-endpoint distance, an empirical curve over 1 m bins estimated on those same training matches
with the smoothing width chosen on the fold’s 8 validation matches, so it uses no test row and no network. Arm
rows are the locked Study 5 runs of Table 6, temperature-scaled on validation. The base rate is one constant within
each fold, so its AUC carries no ranking information and is omitted. Every learned arm is ahead of both nulls
in all 64 matches; the gap of arm C over the length prior is −0.207 [−0.216, −0.199] nats and of G2G −0.223
[−0.231, −0.215] (64-cluster match bootstrap, 𝐵 = 10,000)

                         Model                       Completion log-loss       Brier   AUC
                         Base rate (one constant)                   0.444      0.136      —
                         Length prior                               0.397      0.119   0.685
                         Original SoccerMap                         0.206      0.061   0.945
                         Wide SoccerMap                             0.208      0.061   0.944
                         Arm C (SoccerMap-v2)                       0.189      0.056   0.955
                         G2G                                        0.174      0.051   0.962




                                                         16
Table 6: Study 5 summary: the eight-fold match-grouped cross-validation over all 64 matches at the shipped
recipe, pooled out-of-fold predictions of 53,628 passes in 64 match clusters, one seed per fold. Intervals from the
64-cluster match bootstrap over 64 matches (𝐵 = 10,000); family of 50 hypotheses. Reading conventions: Sec. 6.
Full family: Supplement Table S4

    Pair                      Selection NLL ↓     Completion log-loss ↓           Mass <5 m ↑     Argmax dist. (m) ↓
    G2G−C             −0.251 [−0.263, −0.239] −0.015 [−0.018, −0.013] +0.028 [+0.026, +0.031] −0.77 [−0.85, −0.68]
    matches, adj. 𝑝          64/64, 𝑝 < 0.01 ∗◦       58/64, 𝑝 < 0.01 ∗◦     64/64, 𝑝 < 0.01 ∗◦    62/64, 𝑝 < 0.01 ∗◦
    G2G−original −0.704 [−0.736, −0.670] −0.032 [−0.035, −0.029] +0.090 [+0.084, +0.097] −2.74 [−2.90, −2.58]
    matches, adj. 𝑝          64/64, 𝑝 < 0.01 ∗◦       64/64, 𝑝 < 0.01 ∗◦     64/64, 𝑝 < 0.01 ∗◦    64/64, 𝑝 < 0.01 ∗◦
    G2G−wide          −0.520 [−0.553, −0.487] −0.034 [−0.037, −0.031] +0.071 [+0.065, +0.078] −2.15 [−2.30, −2.00]
    matches, adj. 𝑝          64/64, 𝑝 < 0.01 ∗◦       64/64, 𝑝 < 0.01 ∗◦     64/64, 𝑝 < 0.01 ∗◦    64/64, 𝑝 < 0.01 ∗◦
    C−original        −0.452 [−0.480, −0.425] −0.017 [−0.019, −0.014] +0.062 [+0.057, +0.067] −1.97 [−2.11, −1.84]
    matches, adj. 𝑝          64/64, 𝑝 < 0.01 ∗◦       61/64, 𝑝 < 0.01 ∗◦     64/64, 𝑝 < 0.01 ∗◦    64/64, 𝑝 < 0.01 ∗◦
    C−wide            −0.269 [−0.296, −0.241] −0.019 [−0.022, −0.016] +0.043 [+0.038, +0.048] −1.38 [−1.51, −1.24]
    matches, adj. 𝑝          63/64, 𝑝 < 0.01 ∗◦       62/64, 𝑝 < 0.01 ∗◦     63/64, 𝑝 < 0.01 ∗◦    64/64, 𝑝 < 0.01 ∗◦


Table 7: Study 12 (A) summary: the raw-feature arm Draw in the Study 5 eight-fold match-grouped cross-validation
at the shipped recipe, one seed per fold, against the locked Study 5 out-of-fold rows of C and G2G. Intervals from
the 64-cluster match bootstrap over 64 matches (𝐵 = 10,000); family of 20 hypotheses. Reading conventions:
Sec. 6. Full family: Supplement Table S6

    Pair                      Selection NLL ↓     Completion log-loss ↓          Mass <5 m ↑      Argmax dist. (m) ↓
    Draw −C           −0.186 [−0.199, −0.172] −0.010 [−0.012, −0.007] +0.017 [+0.015, +0.020] −0.46 [−0.55, −0.37]
    matches, adj. 𝑝          64/64, 𝑝 < 0.01 ∗◦       53/64, 𝑝 < 0.01 ∗◦     63/64, 𝑝 < 0.01 ∗◦    57/64, 𝑝 < 0.01 ∗◦
    G2G−Draw          −0.065 [−0.078, −0.052] −0.006 [−0.008, −0.003] +0.011 [+0.008, +0.014] −0.31 [−0.41, −0.21]
    matches, adj. 𝑝          55/64, 𝑝 < 0.01 ∗◦       43/64, 𝑝 < 0.01 ∗◦     56/64, 𝑝 < 0.01 ∗◦    53/64, 𝑝 < 0.01 ∗◦



Fold 1 is the hardest fold for the painted arms. Fold 1, the eight matches the holdout studies reuse,
is the hardest fold on selection for G2G and arm C and among the harder ones for the two SoccerMap
controls, whose worst folds are 2 and 7, and G2G’s margin over the original control there is below the
tournament-wide one (Supplement Table S5). Two qualifications follow. The learning rates, budget and
architecture were chosen on the original split, so folds 2–8 are unseen as test data but not as data the
design was tuned against. A fold’s validation matches serve as the next fold’s test matches, the standard
rotation, which leaks no label but means the eight models are not independent.

The core and the front end again. Across the tournament the modernised core alone improves on both
controls on selection and on completion under both procedures, and the front end adds its quarter of a
nat on top; the two steps are the same size here as in the single-split studies, as one expects if they are
properties of the architectures rather than of the eight matches.

The recommended variant under the same protocol. Study 12, Part A (Sec. 5.5) puts the raw-feature
painter Draw through the same eight folds at the same recipe and scores it against the locked out-of-fold
rows of C and G2G (Table 7; Supplement Tables S6 and S7). With no learned front-end parameter at all,
painting the nine raw node features is worth −0.186 nats of selection NLL [−0.199, −0.172] over arm C,
ahead in all 64 matches and under both procedures at the same 10−5 floor, three quarters of the −0.251
the full front end earns, the same share it carries on the external corpus (Sec. 6.2). The remaining quarter,
−0.065 [−0.078, −0.052], is what the learned encoder and message passing add together; over 64 match
clusters that increment clears both procedures on every metric of the family except calibration error, and
it is resolved again under per-arm tuning with five seeds (Sec. 6.3), whereas in the three-seed holdout
studies it sits within seed noise (Secs. 6.4.1, 6.4.2). The tournament-wide reading is therefore sharper
than the holdout’s: the write carries three quarters of the gain, the learned content one quarter.



                                                             17
6.2   External replication on public German league tracking data
Retrained on seven public Bundesliga and 2. Bundesliga matches from another provider, league and
season, G2G leads the same core by −0.239 nats of selection NLL in every match; frozen, it keeps its
localisation advantage but not its selection likelihood. Every study but this one and Study 10 draws
on one tournament from one provider. Study 7 (Sec. 5.5) takes the frozen pipeline to a public corpus
from another league, tracking provider and season and asks whether the locked World Cup models keep
their ordering when scored, unchanged, on passes they were never trained for, and whether the ordering
reappears when every arm is trained from scratch on the external matches alone.

The external benchmark. The IDSSE release (Bassek et al., 2025) holds seven complete Bundesliga
and 2. Bundesliga matches of season 2022/23 with raw event data and raw optical tracking at 25 Hz, under
CC BY 4.0; no model of this paper had seen a frame of it before Study 7. We imported the World Cup
feature chain verbatim and re-implemented the admission gates on the IDSSE schema, with an estimated
per-match event–frame alignment and a receiver-capture-first endpoint rule; the port admits 4,241 passes,
and PE is not evaluated, no value target having been ported. Supplement Sec. S2 gives the port in full,
with its gate audit and every deviation from the World Cup pipeline; the corpus is also described, as a
benchmark, in a companion manuscript by the authors (Sec. 1), none of whose results this paper uses. Its
endpoints are reconstructed from tracking under an estimated alignment rather than annotated, so what
follows is a change-of-provider replication on a reconstructed corpus, not a measurement against clean
labels.

Design. Part A is zero-shot: the locked World Cup checkpoints of G2G, arm C and both SoccerMap
controls, three seeds each, are scored with their locked temperatures on every external pass, nothing
refitted. Part B retrains all four arms from scratch at the shipped recipe in seven leave-one-match-out
folds, one seed per fold plus a three-seed repeat of fold 1 that enters no family, every run hashed before
any test match is opened. Each part is a family of 30 hypotheses, G2G against original, wide and C on
the ten PP and PS metrics, with a hierarchical bootstrap over the 7 matches (and, in Part A, the 3 seeds)
and the prioritised sign-flip test over all 27 = 128 match-level sign patterns, whose smallest attainable
adjusted 𝑝 is 2/128 = 0.0156. Table 8 summarises both parts; Supplement Tables S8–S11 give the
families, the primary metrics fold by fold and the fold-1 repeat.

Zero-shot transfer. Frozen, the World Cup models find the external corpus harder by more than a nat of
selection NLL each, and the shift does not treat the arms alike (Table 8, Part A). On selection NLL G2G
is level with both SoccerMap controls and behind arm C in every one of the seven matches, a contrast that
clears the max-𝑇 test in C’s favour; completion is a wash for all three pairs. What does transfer is where
the mass goes: G2G puts more probability within 5 m of the observed endpoint than either SoccerMap
control, ahead in all seven matches and clearing the max-𝑇 test, and its argmax lands closer. The frozen
models thus keep the sharper surfaces the splat produces but not the better selection likelihood, on the raw
score as well as the calibrated one (Supplement Table S8); the raster-only core degrades most gracefully.

Retrained on five matches. Fitted to the new distribution, the full ordering returns (Table 8, Part B).
Out of fold, G2G scores 6.377 nats of selection NLL against 6.616 for arm C, and it leads all three raster
arms in all seven matches on selection NLL and local mass under both procedures, by more than half a
nat against the SoccerMap controls. Completion follows by a few hundredths of log-loss against every
arm, but at the 0.0156 floor of the seven-cluster test only the contrast against C clears the adjusted max-𝑇
threshold; the calibration-error contrasts clear neither procedure. G2G is ahead of arm C on both primary
metrics in every fold (Supplement Table S10), and the fold-1 repeat (Supplement Table S11) puts the seed
noise of the G2G−C contrasts well inside their margins, all three seeds in favour; the contrast against the
wide control is the variable one, the wide control’s own convergence on about three thousand training
passes being the variable part.


                                                    18
Table 8: Study 7 summary: the external replication on the seven IDSSE matches (4,241 passes, 7 match clusters).
Part A scores the locked World Cup checkpoints (three seeds per arm) with their locked temperatures, nothing
refitted; Part B retrains every arm from scratch in seven leave-one-match-out folds, one seed per fold. Intervals from
the hierarchical bootstrap over 7 matches and 3 seeds (Part A) or 7-cluster match bootstrap (Part B) (𝐵 = 10,000);
family of 30 hypotheses per part; †: SD from the three-seed fold-1 repeat. Reading conventions: Sec. 6. Full
family: Supplement Tables S8 and S9

  Pair                       Selection NLL ↓         Completion log-loss ↓                   Mass <5 m ↑           Argmax dist. (m) ↓
  zero-shot (Part A)
  G2G−C           +0.079 [+0.036, +0.121] +0.011 [−0.003, +0.028] +0.007 [+0.001, +0.014]                      −0.01 [−0.21, +0.18]
  matches, adj. 𝑝   sd 0.042, 0/7, 𝑝 = 0.016 ∗◦      sd 0.013, 1/7, 𝑝 = 0.469     sd 0.006, 6/7, 𝑝 = 0.203           sd 0.06, 4/7, 𝑝 = 1
  G2G−original −0.045 [−0.144, +0.039] −0.003 [−0.014, +0.010] +0.044 [+0.035, +0.052]                         −0.68 [−1.20, −0.28]
  matches, adj. 𝑝      sd 0.085, 4/7, 𝑝 = 0.797          sd 0.005, 4/7, 𝑝 = 1 sd 0.006, 7/7, 𝑝 = 0.016 ∗◦     sd 0.27, 7/7, 𝑝 = 0.219 ∗
  G2G−wide          +0.033 [−0.018, +0.084] +0.010 [−0.005, +0.025] +0.031 [+0.024, +0.037]                    −0.64 [−1.06, −0.28]
  matches, adj. 𝑝      sd 0.037, 2/7, 𝑝 = 0.969      sd 0.006, 1/7, 𝑝 = 0.922 sd 0.003, 7/7, 𝑝 = 0.016 ∗◦     sd 0.21, 6/7, 𝑝 = 0.203 ∗

  retrained (Part B)
  G2G−C           −0.239 [−0.285, −0.197] −0.026 [−0.030, −0.022] +0.044 [+0.035, +0.055]                      −0.83 [−1.15, −0.51]
  matches, adj. 𝑝 sd 0.032† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.002† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.002† , 7/7, 𝑝 = 0.031 ∗◦ sd 0.28† , 7/7, 𝑝 = 0.047 ∗◦
  G2G−original −0.887 [−1.024, −0.742] −0.041 [−0.064, −0.018] +0.136 [+0.116, +0.153]                         −2.59 [−2.88, −2.27]
  matches, adj. 𝑝 sd 0.050† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.038† , 7/7, 𝑝 = 0.094 ∗ sd 0.009† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.08† , 7/7, 𝑝 = 0.016 ∗◦
  G2G−wide          −0.591 [−0.678, −0.508] −0.027 [−0.041, −0.015] +0.100 [+0.083, +0.117]                    −2.83 [−3.57, −2.11]
  matches, adj. 𝑝 sd 0.315† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.004† , 6/7, 𝑝 = 0.062 ∗ sd 0.034† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.92† , 7/7, 𝑝 = 0.031 ∗◦



What transfers. The front-end margin over the same core, G2G−C, is −0.239 nats on the external
corpus and −0.251 on the 64-match cross-validation of Sec. 6.1: trained on about three thousand passes
from another provider, league and season, with an estimated event–frame alignment and raw optical
positions, the entity-to-grid interface is worth what it was worth on the World Cup. The margin over the
SoccerMap controls, core and front end together, is larger externally; the controls are the arms that suffer
most from five training matches.

The raw-feature arm on the external corpus. Study 7 carries the shipped model and three controls
across the provider boundary but not the front-end ablation that matters most for the interface claim:
Draw , the nine raw node features painted with no learned encoder (Sec. 6.4.2), which on the World Cup
sits within a hundredth of a nat of the learned embeddings. Study 10 (Sec. 5.5) adds that arm to both
parts under the Study 7 protocol with nothing else changed, its three locked Study 3 checkpoints scored
zero-shot against the locked Study 7 rows of C and G2G (a family of 20) and its seven retrained folds
scored against the locked rows of C, G2G and original (a family of 30), with the intervals, test and floor of
Study 7. Table 9 summarises both parts; Supplement Tables S12–S15 give the families, the fold-by-fold
metrics and the fold-1 repeat.

Zero-shot transfer of the raw-feature arm. Frozen, the raw-feature arm has better likelihood point
estimates than G2G (Table 9, Part A). Its selection NLL sits between arm C’s and G2G’s: against C it
is a null contrast, whereas G2G is behind it in all seven matches, without an adjusted max-𝑇 rejection
(𝑝 = 0.062). On completion the frozen raw-feature arm is ahead of C in all seven matches and clears
the max-𝑇 test, while its margin over G2G does not, and local mass is level with G2G’s. The frozen
raw-feature painter thus keeps the splat’s sharper surfaces across the provider boundary as G2G does,
but its calibrated likelihood degrades as arm C’s does rather than as G2G’s, a pattern consistent with a
learned encoder fitted to the source distribution.

Retrained on five matches without a learned encoder. Retrained on five matches, the raw-feature
arm reproduces the World Cup attribution (Table 9, Part B). Out of fold it scores 6.438 nats of selection
NLL against 6.616 for arm C and 6.377 for G2G: it leads C and the original control in all seven matches
on selection NLL, local mass and argmax distance under both procedures, and G2G keeps a small margin

                                                                   19
Table 9: Study 10 summary: the raw-feature arm Draw on the seven IDSSE matches under the Study 7 protocol,
against the locked Study 7 rows of C, G2G and original: Part A zero-shot with the three locked Study 3 checkpoints,
Part B retrained in the seven leave-one-match-out folds. Intervals from the hierarchical bootstrap over 7 matches
and 3 seeds (Part A) or 7-cluster match bootstrap (Part B) (𝐵 = 10,000); family of 20 (Part A) and 30 (Part
B) hypotheses per part; †: SD from the three-seed fold-1 repeat. Reading conventions: Sec. 6. Full family:
Supplement Tables S12 and S13

  Pair                       Selection NLL ↓         Completion log-loss ↓                   Mass <5 m ↑           Argmax dist. (m) ↓
  zero-shot (Part A)
  Draw −C        +0.030 [−0.021, +0.084] −0.007 [−0.017, +0.003] +0.006 [+0.000, +0.010]                       −0.14 [−0.32, +0.03]
  matches, adj. 𝑝      sd 0.050, 1/7, 𝑝 = 0.281    sd 0.009, 7/7, 𝑝 = 0.016 ◦     sd 0.003, 6/7, 𝑝 = 0.328      sd 0.03, 5/7, 𝑝 = 0.453
  G2G−Draw          +0.048 [+0.023, +0.070] +0.018 [+0.006, +0.030] +0.002 [−0.006, +0.009]                    +0.14 [−0.03, +0.35]
  matches, adj. 𝑝    sd 0.012, 0/7, 𝑝 = 0.062 ∗     sd 0.009, 0/7, 𝑝 = 0.141      sd 0.008, 5/7, 𝑝 = 0.969      sd 0.05, 1/7, 𝑝 = 0.641

  retrained (Part B)
  Draw −C         −0.178 [−0.207, −0.139] −0.018 [−0.023, −0.013] +0.030 [+0.021, +0.038]                      −0.62 [−0.80, −0.41]
  matches, adj. 𝑝 sd 0.077† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.002† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.013† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.45† , 7/7, 𝑝 = 0.016 ∗◦
  G2G−Draw          −0.061 [−0.099, −0.025] −0.008 [−0.013, −0.004] +0.014 [+0.006, +0.023]                    −0.20 [−0.57, +0.12]
  matches, adj. 𝑝   sd 0.081† , 6/7, 𝑝 = 0.109 ∗ sd 0.003† , 6/7, 𝑝 = 0.172 ∗ sd 0.011† , 6/7, 𝑝 = 0.156 ∗     sd 0.28† , 4/7, 𝑝 = 0.859
  Draw −original −0.826 [−0.970, −0.673] −0.033 [−0.059, −0.006] +0.122 [+0.100, +0.144]                       −2.39 [−2.53, −2.26]
  matches, adj. 𝑝 sd 0.042† , 7/7, 𝑝 = 0.016 ∗◦    sd 0.038† , 5/7, 𝑝 = 0.453 sd 0.008† , 7/7, 𝑝 = 0.016 ∗◦ sd 0.29† , 7/7, 𝑝 = 0.016 ∗◦



above it on selection, completion and local mass, six of seven matches each, short of the adjusted max-𝑇
threshold on all three. Draw sits between C and G2G on selection in six of the seven folds (Supplement
Table S14), and in the fold-1 repeat (Supplement Table S15) all three seeds favour Draw over C and G2G
over Draw , the second increment being of the order of its own seed noise. Of the 0.239 nats that separate
G2G from arm C on the external corpus, the raw-feature painter with no learned parameters accounts for
about three quarters, the share the painted package holds on the World Cup (Sec. 6.4.1). On both corpora
raw painting accounts for most of the measured gain; the additional learned-content increment is resolved
in the World Cup cross-validation and tuned studies, but not in this small external comparison.

The external effect and the endpoint rule. The two corpora resolve their endpoints differently: on
the World Cup 98.9% of admitted passes end at the next tracked possession event and 0.21% at a
receiver capture, whereas on the external corpus the mix is inverted, 91.2% capture and 6.6% next event
(Supplement Table S1). Because the capture rule returns the first frame at which the ball is within 1 m
of the annotated receiver, an external endpoint lies within about one grid cell of a tracked player by
construction, which is a label a front end that writes player features at continuous coordinates might
exploit. We therefore re-scored the locked Part B out-of-fold rows inside each stratum, a post-hoc
analysis that no commitment record covers. The effect is carried by the capture stratum: there G2G
leads arm C by −0.266 nats [−0.323, −0.216] in all seven matches, while on the 282 next-event rows
the point estimate turns round to +0.102, with an interval [−0.013, +0.247] that spans zero and two of
seven matches favouring G2G, and on the 91 boundary rows it is −0.128 [−0.452, +0.278]. These are
pointwise intervals over the same seven match clusters, with no sign-flip test and no adjustment across
the strata. The strata are also not a clean contrast: the next-event rows are the harder ones, arm C scoring
7.60 nats on them against 6.50 in the capture stratum, they are few, and they differ from the capture rows
in completion rate and in pass length, so endpoint provenance is confounded with what kind of pass it is.
Two readings survive: the external margin may be partly a property of the capture rule, and the World
Cup result, whose labels are almost entirely next-event, shows that the interface effect does not require
that rule. What the external study cannot do is separate the two.

6.3      Tuned, converged, five-seed comparison
With every arm tuned to its own learning rate and trained to convergence, G2G stays −0.292 nats of
selection NLL ahead of the same core, and the margin against both tuned SoccerMap controls is about 0.3


                                                                   20
Table 10: Study 4 summary: the tuned, converged comparison: every arm’s PP and PS heads at its own validation-
selected learning rate, cap 200 epochs, five seeds. Intervals from the hierarchical bootstrap over 8 matches and 5
seeds (𝐵 = 10,000); family of 50 hypotheses. Reading conventions: Sec. 6. Full family: Supplement Table S16

   Pair                       Selection NLL ↓        Completion log-loss ↓                  Mass <5 m ↑        Argmax dist. (m) ↓
   G2G−C             −0.292 [−0.338, −0.245] −0.013 [−0.022, −0.007] +0.038 [+0.031, +0.045] −0.87 [−1.17, −0.60]
   matches, adj. 𝑝    sd 0.024, 8/8, 𝑝 < 0.01 ∗◦   sd 0.009, 8/8, 𝑝 < 0.01 ∗◦   sd 0.005, 8/8, 𝑝 < 0.01 ∗◦ sd 0.29, 8/8, 𝑝 < 0.01 ∗◦
   G2G−original −0.319 [−0.364, −0.275] −0.035 [−0.042, −0.029] +0.033 [+0.026, +0.042] −1.36 [−1.64, −1.09]
   matches, adj. 𝑝    sd 0.015, 8/8, 𝑝 < 0.01 ∗◦   sd 0.004, 8/8, 𝑝 < 0.01 ∗◦   sd 0.008, 8/8, 𝑝 < 0.01 ∗◦ sd 0.28, 8/8, 𝑝 < 0.01 ∗◦
   G2G−wide          −0.328 [−0.368, −0.291] −0.031 [−0.039, −0.023] +0.035 [+0.027, +0.046] −1.39 [−1.72, −1.06]
   matches, adj. 𝑝    sd 0.026, 8/8, 𝑝 < 0.01 ∗◦   sd 0.008, 8/8, 𝑝 < 0.01 ∗◦   sd 0.010, 8/8, 𝑝 < 0.01 ∗◦ sd 0.36, 8/8, 𝑝 < 0.01 ∗◦
   C−original        −0.027 [−0.063, +0.006] −0.022 [−0.031, −0.012] −0.005 [−0.010, +0.000] −0.49 [−0.74, −0.18]
   matches, adj. 𝑝      sd 0.035, 7/8, 𝑝 = 0.297   sd 0.007, 8/8, 𝑝 < 0.01 ∗◦    sd 0.005, 2/8, 𝑝 = 0.320 sd 0.29, 8/8, 𝑝 < 0.01 ∗◦
   C−wide            −0.036 [−0.069, +0.007] −0.018 [−0.027, −0.009] −0.002 [−0.011, +0.005] −0.52 [−0.72, −0.28]
   matches, adj. 𝑝      sd 0.043, 8/8, 𝑝 = 0.094   sd 0.009, 8/8, 𝑝 < 0.01 ∗◦    sd 0.009, 3/8, 𝑝 = 0.656 sd 0.20, 8/8, 𝑝 < 0.01 ∗◦



nats. The shipped comparison trains every arm at one shared learning rate under one epoch cap, which
Supplement Sec. S5.5 shows favours G2G on validation. Study 4 (Sec. 5.5) removes both conditions at
once: we trained each arm’s PP and PS heads at their own validation-selected learning rate to a cap of
200 epochs under five seeds, and opened the test set once after every checkpoint was locked. Table 10
summarises the family; Supplement Table S16 gives all 50 hypotheses under both estimands and both
procedures.

Selected rates and convergence. The committed rule chose 2×10−4 for G2G’s selection head, 10−4 for
arm C’s and the wide control’s and 5 × 10−5 for the original control’s, and completion-head rates between
10−4 and 5 × 10−4 ; the shipped completion rate was the bottom of its grid and the shipped selection rate
lies below it. Every evaluated head run stopped early inside the cap. Thus the cap is not binding under
the selected rates and stopping rule; this does not establish an optimiser-independent optimum.

The gap narrows and stays. Seed-averaged over five seeds, G2G reaches a selection NLL of 4.965
against 5.257 for tuned arm C, with both tuned SoccerMap controls within a few hundredths of arm C
(Table 10); every selection and completion contrast of the three G2G pairs clears both procedures, the
calibration-error contrasts excepted. Per-arm tuning therefore takes the matched-budget selection margin
against the capacity-matched control from about half a nat (Supplement Table S31) to a third, where the
cap-200 reruns of Supplement Sec. S5.4 put it, and leaves the completion margin at three-quarters of its
shipped size: what tuning removes is the part of the margin the shared recipe had given G2G for free,
and what it leaves is the part the paper claims.

Arm C under tuning. Tuned, the modernised core beats both tuned controls on completion log-loss
and argmax distance under both procedures, but not on selection NLL, where both of its contrasts span
zero. Under tuning the core alone is therefore a better completion model than SoccerMap but not a better
selection model; it is the painted front end that separates G2G from all three raster arms on selection by
about 0.3 nats.

The recommended variant, tuned. Study 12, Part B (Sec. 5.5) runs Draw through the same sweep,
selection rule and five seeds against the locked tuned runs of C and G2G (Table 11; Supplement Table S17).
The committed rule chose 10−4 for its completion head and 2 × 10−4 for its selection head. Tuned and
converged, the raw-feature painter is −0.225 nats [−0.256, −0.195] ahead of the tuned core on selection
NLL, in all eight matches under both procedures, three quarters of the tuned front-end margin; G2G keeps
−0.067 [−0.088, −0.045] over it, again in all eight matches under both procedures, with completion level
between the two. Under tuning, then, the split is the one the cross-validation gives: the write carries three
quarters of the gain and the learned content a quarter.


                                                                 21
Table 11: Study 12 (B) summary: the raw-feature arm Draw under the Study 4 protocol, its own validation-selected
learning rate, cap 200 epochs, five seeds, against the locked Study 4 runs of G2G and C. Intervals from the
hierarchical bootstrap over 8 matches and 5 seeds (𝐵 = 10,000); family of 20 hypotheses. Reading conventions:
Sec. 6. Full family: Supplement Table S17

      Pair                       Selection NLL ↓      Completion log-loss ↓                  Mass <5 m ↑        Argmax dist. (m) ↓
      Draw − C          −0.225 [−0.256, −0.195] −0.009 [−0.016, −0.002] +0.027 [+0.021, +0.033] −0.64 [−0.82, −0.50]
      matches, adj. 𝑝    sd 0.019, 8/8, 𝑝 < 0.01 ∗◦   sd 0.005, 7/8, 𝑝 = 0.125   sd 0.006, 8/8, 𝑝 < 0.01 ∗◦ sd 0.14, 8/8, 𝑝 < 0.01 ∗◦
      G2G − Draw        −0.067 [−0.088, −0.045] −0.005 [−0.010, +0.001] +0.011 [+0.008, +0.015] −0.23 [−0.50, +0.00]
      matches, adj. 𝑝    sd 0.010, 8/8, 𝑝 < 0.01 ∗◦   sd 0.005, 6/8, 𝑝 = 0.352   sd 0.004, 8/8, 𝑝 < 0.01 ∗◦ sd 0.27, 7/8, 𝑝 = 0.047 ◦



6.4      What the painted front end supplies
The three studies above measure what the painted front end is worth; the two here, both on the reused
eight-match holdout, take it apart. The attribution ladder prices the front end as a package and separates
the painted channels from message passing; the ablations then vary one element at a time.

6.4.1        Attribution under the pre-specified replication
The painted front end earns the improvement. Adding relational reasoning on top of it moves the selection
score by −0.0515 nats, an estimate whose nominal interval excludes zero but whose per-seed spread is
as large as the effect. Fig. 4 shows every headline effect of the three multi-seed studies it covers, with its
interval.
     The replication is Study 1 of Sec. 5.5: we trained three fresh seeds each of G2G, arm C and arm D,
plus cap-200 selection-head reruns of both controls, on the same eight matches and split signature. Arm C
and arm D differ only in the painted front end; arm D and G2G differ only in the per-node encoder, which
G2G replaces with the relational one. Table 12 prices the three design steps on the four headline metrics;
Supplement Tables S40 and S41 print all 54 hypotheses under both procedures. The exact sign-flip test
applies here in a restricted sense: the pre-specified recipe averages each within-match delta over the seeds
before the sign flip, so the test says nothing about seed variability, and the hierarchical bootstrap, which
resamples seeds as well, is the stricter procedure on that axis (Sec. 5.5).
     Adding the painted front end to SoccerMap-v2 (arm C → D), the painted package of 29,580 param-
eters, is worth −0.1705 nats of selection NLL; the whole front end including message passing (arm C →
G2G) is worth −0.2220 (Table 12), so the point estimates put the painted package at roughly three-quarters
of the front-end selection improvement. Because the painted front end bundles the per-node network, the
entity features, the bilinear projection, the 36 extra channels and the wider input stem, this step is evidence
for the composite package, not for splatting or sub-cell geometry in isolation; Secs. 6.4.2 and 6.5 separate
them. On selection NLL, local mass and argmax distance both the whole front end and the painted
package clear the max-𝑇 test, ahead in all eight matches; on completion log-loss neither does, although
both intervals exclude zero. Message passing on top of the package clears max-𝑇 on selection NLL and
local mass and on nothing else, so on this holdout the relational increment is small and seed-sensitive
rather than absent: across the three seeds (Supplement Table S18) the G2G−D selection-NLL difference
ranges from nearly a tenth of a nat to nearly nothing, a spread as large as the effect. The combined learned
increment, encoder and message passing together, is resolved over 64 matches and under five-seed tuning
(Secs. 6.1, 6.3).

6.4.2        Front-end ablations
How the write is placed carries about half the painted package’s selection gain; for what is written, how
it is anti-aliased and how many parameters the core has, no difference is detected under this protocol.
Study 3 (Sec. 5.5) takes apart the package that the attribution ladder priced, with trained ablations, three
seeds each, against the locked Study 1 runs of D, G2G and C, each ablation changing one element of the
design and holding the rest fixed. Table 13 summarises the family and Supplement Table S19 gives all

                                                                   22
Table 12: Study 1 summary: which design step earns the improvement: front end is the whole graph front end
added to SoccerMap-v2 (G2G−C); painted package is that front end without relational message passing, i.e. the
per-node MLP, splat operator, 36 painted channels and wider input stem together (D−C); message passing is the
increment message passing adds on top of the package (G2G−D). Three fresh seeds per arm on the eight-match
holdout. Intervals from the hierarchical bootstrap over 8 matches and 3 seeds (𝐵 = 10,000); family of 54 hypotheses.
Reading conventions: Sec. 6. Full family: Supplement Tables S40 and S41

   Pair                       Selection NLL ↓         Completion log-loss ↓                   Mass <5 m ↑         Argmax dist. (m) ↓
   G2G−C             −0.222 [−0.259, −0.181] −0.014 [−0.024, −0.006] +0.029 [+0.023, +0.034] −0.77 [−1.04, −0.41]
   matches, adj. 𝑝    sd 0.020, 8/8, 𝑝 < 0.01 ∗◦     sd 0.007, 8/8, 𝑝 = 0.070 ∗   sd 0.005, 8/8, 𝑝 < 0.01 ∗◦ sd 0.32, 8/8, 𝑝 < 0.01 ∗◦
   D−C               −0.171 [−0.227, −0.112] −0.010 [−0.021, −0.001] +0.023 [+0.016, +0.031] −0.59 [−0.90, −0.31]
   matches, adj. 𝑝    sd 0.046, 8/8, 𝑝 < 0.01 ∗◦      sd 0.010, 8/8, 𝑝 = 0.055    sd 0.007, 8/8, 𝑝 < 0.01 ∗◦ sd 0.29, 8/8, 𝑝 < 0.01 ∗◦
   G2G−D             −0.051 [−0.095, −0.005] −0.004 [−0.010, +0.003] +0.006 [−0.001, +0.015] −0.18 [−0.55, +0.15]
   matches, adj. 𝑝    sd 0.046, 8/8, 𝑝 = 0.016 ◦      sd 0.005, 6/8, 𝑝 = 0.516     sd 0.009, 8/8, 𝑝 < 0.01 ◦    sd 0.35, 8/8, 𝑝 = 0.086


                                                   selection NLL     completion log-loss mass within 5 m              argmax distance
                Study 1: attribution ladder
                       front end (G2G − C)
                   painted package (D − C)
                 message passing (G2G − D)
                     G2G − original, cap 200
                       G2G − wide, cap 200
 Study 2: controls at the shipped budget
                                G2G − original
                                  G2G − wide
              Study 3: front-end ablations
                      nearest − bilinear (D)
                   nearest − bilinear (G2G)
                    Gaussian − bilinear (D)
                 raw features − learned (D)
              parameter-matched raster − C
           message passing, nearest decoder

                                              −0.8 −0.4 0.0               −0.025 0.000          0.00 0.04 0.08       −3.0 −1.5 0.0
          pooled difference in nats (selection NLL), log-loss, probability mass or metres, with its 95% interval over 8 matches and 3 seeds
                        clears max-T over its study's family          does not clear it        metric not pre-declared for that pair

Fig. 4 Multi-seed effects with 95% hierarchical-bootstrap intervals over 8 matches and 3 seeds, for the four headline
metrics, with one colour and one band per study: the Study 1 attribution ladder (front end, painted package, message
passing) with its cap-200 convergence pairs, the Study 2 multi-seed controls at the shipped budget, and the Study
3 front-end ablations (Sec. 6.4.2). A filled marker means the contrast clears the exact sign-flip max-𝑇 test over
its study’s pre-declared family at 𝛼 = 0.05, the test this paper prioritises; a hollow marker means it does not. A
vertical tick at zero marks a metric that was not pre-declared for that pair, the cap-200 reruns having trained the
selection head only


60 hypotheses.

Bilinear placement carries about half the package. Replacing bilinear painting by nearest-cell paint-
ing discards the fractional position at which each write is placed, and changes the interpolation with it;
the node features themselves are unchanged. It costs the per-node arm and G2G each close to a tenth of
a nat of selection NLL, both contrasts clearing the max-𝑇 test, and costs G2G a little local mass. Against
the painted package’s −0.1705 nats (Table 12), roughly half the selection gain is therefore attributable
to bilinear placement at continuous coordinates, a point estimate for a change that alters placement and
interpolation together. Completion is untouched, which matches the inference-time quantisation probe


                                                                    23
Table 13: Study 3 summary: front-end ablations, three seeds each, against the locked Study 1 runs of D, G2G and
C: nearest-cell and Gaussian painting against bilinear, the nine raw node features against the learned embedding, a
parameter-matched raster core, and message passing under the nearest-cell decoder. Intervals from the hierarchical
bootstrap over 8 matches and 3 seeds (𝐵 = 10,000); family of 60 hypotheses. Reading conventions: Sec. 6. Full
family: Supplement Table S19

   Pair                              Selection NLL ↓       Completion log-loss ↓              Mass <5 m ↑       Argmax dist. (m) ↓
   nearest − bilinear (D)   +0.084 [+0.033, +0.125] +0.005 [ −0.001, +0.011] −0.001 [ −0.006, +0.004] +0.03 [ −0.20, +0.31]
   matches, adj. 𝑝           sd 0.046, 0/8, 𝑝 < 0.01 ◦ sd 0.005, 1/8, 𝑝 = 0.211 sd 0.004, 2/8, 𝑝 = 0.984        sd 0.22, 4/8, 𝑝 = 1
   Gaussian − bilinear (D) −0.012 [ −0.024, +0.001] +0.001 [ −0.004, +0.007] +0.001 [ −0.001, +0.004] +0.06 [ −0.05, +0.19]
   matches, adj. 𝑝            sd 0.012, 7/8, 𝑝 = 0.078       sd 0.006, 3/8, 𝑝 = 1 sd 0.002, 6/8, 𝑝 = 0.852      sd 0.06, 2/8, 𝑝 = 1
   raw feat. − learned (D) +0.005 [ −0.049, +0.064] −0.002 [ −0.010, +0.006] −0.005 [ −0.014, +0.002] +0.05 [ −0.27, +0.36]
   matches, adj. 𝑝                 sd 0.058, 3/8, 𝑝 = 1      sd 0.007, 5/8, 𝑝 = 1 sd 0.008, 2/8, 𝑝 = 0.438      sd 0.28, 4/8, 𝑝 = 1
   Cmatched − C             −0.013 [ −0.042, +0.012] −0.003 [ −0.008, +0.002] +0.000 [ −0.005, +0.006] +0.07 [ −0.09, +0.24]
   matches, adj. 𝑝                 sd 0.016, 4/8, 𝑝 = 1 sd 0.001, 6/8, 𝑝 = 0.945       sd 0.005, 4/8, 𝑝 = 1     sd 0.06, 3/8, 𝑝 = 1
   nearest − bilinear (G2G) +0.093 [+0.072, +0.117] +0.001 [ −0.004, +0.005] −0.005 [ −0.011, −0.000] +0.09 [ −0.08, +0.33]
   matches, adj. 𝑝          sd 0.015, 0/8, 𝑝 < 0.01 ∗◦       sd 0.003, 3/8, 𝑝 = 1 sd 0.005, 0/8, 𝑝 = 0.094 sd 0.19, 3/8, 𝑝 = 0.969
   msg. pass. (nearest)     −0.042 [ −0.080, −0.011] −0.009 [ −0.013, −0.005] +0.003 [ −0.002, +0.008] −0.12 [ −0.31, +0.08]
   matches, adj. 𝑝           sd 0.035, 8/8, 𝑝 < 0.01 ◦ sd 0.001, 8/8, 𝑝 < 0.01 ∗◦ sd 0.004, 7/8, 𝑝 = 0.734 sd 0.17, 6/8, 𝑝 = 0.852



of Sec. 6.7.1: sub-cell placement acts on selection.

No effect of anti-aliasing is detected. A normalised 3 × 3 Gaussian painting of half-cell width does
not separate from bilinear painting on any headline metric under this protocol. Its selection interval is
narrow, so any difference between the two kernels is at most a few hundredths of a nat, well below the
effect of bilinear placement itself.

Raw features and the learned embedding are not separated on the holdout. Painting the nine raw
node features bilinearly with no learned encoder (Draw , 27 channels instead of 36) does not separate from
the per-node MLP arm on any headline metric, and the two arms’ seed-averaged selection NLLs lie within
a hundredth of a nat of each other. This is not evidence of equivalence: the selection interval reaches five
to six hundredths of a nat in either direction, as wide as the learned increment that the cross-validation
resolves (Sec. 6.1). On this holdout, most of what the painted package supplies is available from painting
the players’ own features at continuous positions, and the learned embedding adds no detectable further
gain.

Parameters do not explain it. Widening the raster core to within 0.6% of G2G’s parameter count
moves arm C by about a hundredth of a nat on selection NLL, a null contrast, against the fifth of a nat the
whole front end adds to the same core. The front-end gain is not a parameter-count effect.

Message passing under the nearest decoder. With sub-cell placement removed from both arms,
adding the two message-passing blocks is worth a few hundredths of a nat of selection NLL and under
a hundredth of completion log-loss, both clearing the max-𝑇 test and both of the order of what message
passing adds on top of bilinear painting (Table 12). The relational encoder recovers a little of what
nearest-cell painting loses, but only a little: G2Gnearest remains behind the non-relational bilinear arm D.
Taken together with Sec. 6.4.1, these holdout studies locate most of the gain the front end adds to
SoccerMap-v2 in writing per-player information onto the grid at continuous coordinates. No separate
contribution of the learned embedding, the anti-aliasing kernel or the parameter count is detected here,
and relational message passing adds a small increment of the order of its own seed variation under either
decoder. The larger cross-validation and tuned comparisons resolve the combined contribution of the
learned encoder and message passing, but not either one alone.




                                                                 24
6.5   Raster controls with sub-cell information
Neither sub-cell offset channels nor a raster four times finer closes the gap to the painted front end, and
the same splat on the original SoccerMap core is worth −0.295 nats. The ablations of Sec. 6.4.2 and the
interface alternatives of Sec. 6.6 vary the painted front end and hold the raster fixed; two objections run
the other way. The first is that a raster core loses to a painted front end only because hard binning discards
where inside a cell a player stands, so that a raster carrying that information would close the gap without
any graph; the second is that the original SoccerMap core was never given the painted channels, so that
the margin over it conflates core and front end. Studies 8 and 9 (Sec. 5.5) test specific versions of these
alternatives.

Design: sub-cell information on the raster. Study 8 registers two arms on the untouched engine.
Coffsets is arm C’s SoccerMap-v2 core on the 13 raster channels plus six deterministic sub-cell mean-
offset channels, two per node type, each cell carrying the mean offset from its centre of the nodes of
that type inside it; the channels hold no learned parameter and are the arm’s only difference from arm C.
Originalsplat is the original three-scale SoccerMap core on the 13 raster channels plus the 27 bilinearly
painted raw node features of Draw (Sec. 6.4.2); the painted channels are its only difference from the
original control, and it has fewer parameters than the wide control. Each arm trains PP and PS heads at
the shipped recipe under the three Study 1 seeds and is compared with the locked runs of C, D, original,
wide and Draw , none retrained: five pre-declared pairs, 50 hypotheses, with the hierarchical bootstrap
over 8 matches and 3 seeds and the exact 256-pattern max-𝑇 test; Table 14 summarises the family and
Supplement Table S20 gives every hypothesis.

Sub-cell offsets on the raster core. Giving the raster core the sub-cell position of every player and the
ball helps it, but not much (Table 14). Coffsets improves on arm C by a few hundredths of a nat of selection
NLL and by less than a hundredth of completion log-loss; the completion contrast clears the max-𝑇 test,
the selection contrast does not, and local mass and argmax distance are null. With seed-averaged selection
NLLs of 5.446 for Coffsets against 5.490 for C and 5.319 for D, the offset channels close about a quarter
of the gap between the raster core and the painted front end, and none of the gap in local mass: sub-cell
position written as an explicit raster feature is worth a fraction of what the same position is worth as the
place the embedding is written.

Learned and raw painting against the offset raster. Against the raster that carries the same sub-cell
position, both painted arms stay ahead by the same margin: D and Draw each lead Coffsets by about an
eighth of a nat of selection NLL, with more local mass and a closer argmax, all under both procedures,
while completion is level; every Coffsets head early-stopped, so the budget was not binding. What the
splat adds over an offset raster is therefore not the position itself, which both arms have, but writing the
player’s own features at that position, and the raw-feature painter with no learned parameters recovers
essentially all of it, as it did against arm C in Sec. 6.4.2.

The painted front end on the original core. The painted front end is worth more on the original
core than on ours. Originalsplat improves on the original control by −0.295 nats of selection NLL, with
completion, local mass and argmax distance improving as well, every contrast under both procedures,
where the same raw-feature write adds −0.165 nats to the SoccerMap-v2 core (Draw against C on the
locked runs, as below); against the wide control, which has more than twice its parameters, it is level on
selection and local mass and ahead on completion under both procedures, at equal budget. The margin the
paper reports over the original SoccerMap therefore does not conflate core and front end in the direction a
reader might fear, the front end alone on the original core being worth close to half of the matched-budget
gap, and the entity-to-grid interface is not tied to the SoccerMap-v2 core.




                                                     25
Table 14: Study 8 summary: the raster controls with sub-cell information: the raster core of arm C plus six
deterministic sub-cell mean-offset channels (Coffsets ) and the original SoccerMap core plus the 27 painted raw node
features (originalsplat ), three seeds each, against the locked runs of C, D, original, wide and Draw . Intervals from the
hierarchical bootstrap over 8 matches and 3 seeds (𝐵 = 10,000); family of 50 hypotheses. Reading conventions:
Sec. 6. Full family: Supplement Table S20

   Pair                             Selection NLL ↓       Completion log-loss ↓               Mass <5 m ↑          Argmax dist. (m) ↓
   Coffsets − C             −0.044 [ −0.075, −0.011] −0.006 [ −0.010, −0.003] −0.002 [ −0.005, +0.001]          +0.28 [ −0.06, +0.59]
   matches, adj. 𝑝            sd 0.001, 6/8, 𝑝 = 0.406 sd 0.000, 8/8, 𝑝 = 0.016 ◦ sd 0.002, 2/8, 𝑝 = 0.844 sd 0.30, 1/8, 𝑝 = 0.125
   Draw − Coffsets          −0.122 [ −0.152, −0.090] −0.006 [ −0.011, −0.002] +0.019 [+0.014, +0.026]          −0.81 [ −1.09, −0.55]
   matches, adj. 𝑝          sd 0.027, 8/8, 𝑝 < 0.01 ∗◦ sd 0.003, 7/8, 𝑝 = 0.102 sd 0.005, 8/8, 𝑝 < 0.01 ∗◦ sd 0.22, 8/8, 𝑝 < 0.01 ∗◦
   D − Coffsets             −0.127 [ −0.172, −0.078] −0.004 [ −0.015, +0.006] +0.025 [+0.016, +0.033]          −0.86 [ −1.32, −0.36]
   matches, adj. 𝑝          sd 0.046, 8/8, 𝑝 < 0.01 ∗◦ sd 0.010, 7/8, 𝑝 = 0.430 sd 0.008, 8/8, 𝑝 < 0.01 ∗◦ sd 0.49, 8/8, 𝑝 < 0.01 ∗◦
   originalsplat − original −0.295 [ −0.416, −0.214] −0.017 [ −0.024, −0.008] +0.026 [+0.020, +0.032]          −0.64 [ −0.81, −0.43]
   matches, adj. 𝑝          sd 0.108, 8/8, 𝑝 < 0.01 ∗◦ sd 0.008, 8/8, 𝑝 < 0.01 ∗◦ sd 0.005, 8/8, 𝑝 < 0.01 ∗◦ sd 0.15, 8/8, 𝑝 < 0.01 ∗◦
   originalsplat − wide     −0.009 [ −0.071, +0.044] −0.022 [ −0.030, −0.015] −0.002 [ −0.010, +0.008]          −0.03 [ −0.35, +0.31]
   matches, adj. 𝑝                 sd 0.057, 5/8, 𝑝 = 1 sd 0.006, 8/8, 𝑝 < 0.01 ∗◦ sd 0.009, 2/8, 𝑝 = 0.805        sd 0.31, 4/8, 𝑝 = 1



Design: the half-metre raster. Study 9 trains the same two cores on a raster four times finer: Chalf and
originalhalf apply the SoccerMap-v2 core of arm C and the original SoccerMap core to the 13 deterministic
channels rasterised at 0.5 m, 136 × 208 = 28,288 cells instead of 68 × 104 = 7,072; the convolutions are
resolution-free, so the grid is the only difference from those arms. We built the 0.5 m cache from the same
locked record cache by the unchanged extractor, pinned its digest in the commitment and self-checked it
against the locked 1 m cache. Every 0.5 m arm is scored on the 1 m grid by a rule fixed before training
and quoted verbatim in Supplement Sec. S4.6.1: tempered 0.5 m selection probabilities are sum-pooled
2 × 2 to the 1 m cells, and the completion probability of a pass is the tempered sigmoid at the 0.5 m
cell containing the observed endpoint. Each arm trains under the three Study 1 seeds and is compared
with the locked runs of C, D, G2G and original: four pre-declared pairs, 40 hypotheses, with the same
bootstrap and test; Table 15 summarises the family and Supplement Table S21 gives every hypothesis.

A finer raster. A raster four times finer does not close the gap; on two of three selection metrics it
widens it (Table 15). Chalf moves the SoccerMap-v2 core’s selection NLL by a few hundredths of a
nat, an interval that touches zero and a contrast far from the adjusted max-𝑇 threshold, while its argmax
lands nearly a metre farther from the observed endpoint and its mass within 5 m falls, both under both
procedures; completion is unchanged. The original core is simply worse at half a metre, a fifth of a nat
behind on selection NLL and behind on local mass. Given four times as many cells to put its mass in,
a raster core spreads it: the likelihood at the observed cell changes little, and the surface’s peak and its
local concentration get worse.

The painted front end against the finer raster. Against the half-metre raster the painted arms keep
the margin they hold against the metre raster: D and G2G lead Chalf on every headline metric in all
eight matches under both procedures. Read together with Study 8, the two objections are answered in
the same way, within the reach of the controls run: give the raster the sub-cell position as a feature and
it recovers a quarter of the painted front end’s gain; give it cells four times smaller and its selection
likelihood shows no statistically resolved improvement while its localisation worsens. The finer raster
keeps the convolutional architecture, so its physical receptive field halves with the cell; the study rules out
resolution as a substitute for the write under that architecture, not resolution in general. What the splat
adds, on this evidence, is neither resolution nor position alone: it is each player’s own features written at
that player’s position, in a form the convolution reads directly.

The interface on a canonical U-Net core. The gain is not a property of SoccerMap-v2 either. Study
13 (Sec. 5.5) trains a canonical three-level 2-D U-Net (Ronneberger et al., 2015), parameter-matched to
arm C within one percent, on the raster channels alone (Uraster ) and with the 27 painted raw node features
of Draw added (Uraw ), three seeds each at the shipped recipe, against the locked runs of C, G2G and Draw ;

                                                                  26
Table 15: Study 9 summary: the half-metre raster: the raster core of arm C (Chalf ) and the original SoccerMap core
(originalhalf ) on the 13 channels rasterised at 0.5 m, scored for comparability with the 1 m arms, three seeds each,
against the locked runs of C, D, G2G and original. Intervals from the hierarchical bootstrap over 8 matches and 3
seeds (𝐵 = 10,000); family of 40 hypotheses. Reading conventions: Sec. 6. Full family: Supplement Table S21

   Pair                               Selection NLL ↓       Completion log-loss ↓                Mass <5 m ↑          Argmax dist. (m) ↓
   Chalf − C               −0.047 [ −0.106, +0.001] +0.007 [ −0.003, +0.015] −0.011 [ −0.016, −0.005]          +0.93 [+0.70, +1.26]
   matches, adj. 𝑝           sd 0.034, 5/8, 𝑝 = 0.609 sd 0.007, 1/8, 𝑝 = 0.461 sd 0.005, 0/8, 𝑝 = 0.016 ∗◦ sd 0.18, 0/8, 𝑝 < 0.01 ∗◦
   originalhalf − original +0.199 [+0.082, +0.274] −0.000 [ −0.009, +0.010] −0.019 [ −0.022, −0.015]           +0.28 [+0.09, +0.47]
   matches, adj. 𝑝         sd 0.104, 0/8, 𝑝 < 0.01 ∗◦       sd 0.004, 3/8, 𝑝 = 1 sd 0.003, 0/8, 𝑝 < 0.01 ∗◦ sd 0.15, 0/8, 𝑝 = 0.023 ◦
   D − Chalf               −0.123 [ −0.167, −0.087] −0.018 [ −0.026, −0.009] +0.034 [+0.028, +0.040]          −1.52 [ −1.91, −1.20]
   matches, adj. 𝑝         sd 0.033, 8/8, 𝑝 < 0.01 ∗◦ sd 0.004, 8/8, 𝑝 < 0.01 ∗◦ sd 0.005, 8/8, 𝑝 < 0.01 ∗◦ sd 0.30, 8/8, 𝑝 < 0.01 ∗◦
   G2G − Chalf             −0.175 [ −0.224, −0.121] −0.022 [ −0.031, −0.015] +0.041 [+0.035, +0.046]          −1.70 [ −1.96, −1.43]
   matches, adj. 𝑝         sd 0.048, 8/8, 𝑝 < 0.01 ∗◦ sd 0.006, 8/8, 𝑝 < 0.01 ∗◦ sd 0.004, 8/8, 𝑝 < 0.01 ∗◦ sd 0.14, 8/8, 𝑝 < 0.01 ∗◦


Table 16: Study 13 summary: the interface on a canonical U-Net core: Uraster (a three-level 2-D U-Net on the 13
raster channels, parameter-matched to arm C within 1%) and Uraw (the same U-Net plus the 27 painted raw node
features of Draw ), three seeds each, against the locked runs of C and G2G (Study 1) and Draw (Study 3). Intervals
from the hierarchical bootstrap over 8 matches and 3 seeds (𝐵 = 10,000); family of 40 hypotheses. Reading
conventions: Sec. 6. Full family: Supplement Table S22

      Pair                       Selection NLL ↓        Completion log-loss ↓                   Mass <5 m ↑        Argmax dist. (m) ↓
      Uraw − Uraster −0.242 [−0.264, −0.213] −0.020 [−0.028, −0.009] +0.015 [+0.011, +0.020] −0.49 [−0.71, −0.19]
      matches, adj. 𝑝    sd 0.012, 8/8, 𝑝 < 0.01 ∗◦   sd 0.008, 8/8, 𝑝 < 0.01 ∗◦    sd 0.004, 8/8, 𝑝 < 0.01 ∗◦ sd 0.17, 7/8, 𝑝 = 0.016 ◦
      Uraster − C       +0.366 [+0.333, +0.397] +0.018 [+0.005, +0.033] −0.041 [−0.046, −0.034] +1.76 [+1.58, +1.99]
      matches, adj. 𝑝    sd 0.014, 0/8, 𝑝 < 0.01 ∗◦     sd 0.009, 1/8, 𝑝 = 0.102    sd 0.006, 0/8, 𝑝 < 0.01 ∗◦ sd 0.17, 0/8, 𝑝 < 0.01 ∗◦
      Uraw − Draw       +0.290 [+0.258, +0.325] +0.011 [+0.001, +0.023] −0.043 [−0.050, −0.037] +1.81 [+1.59, +2.06]
      matches, adj. 𝑝    sd 0.026, 0/8, 𝑝 < 0.01 ∗◦     sd 0.004, 2/8, 𝑝 = 0.484    sd 0.006, 0/8, 𝑝 < 0.01 ∗◦ sd 0.09, 0/8, 𝑝 < 0.01 ∗◦
      Uraw − G2G        +0.346 [+0.319, +0.379] +0.013 [+0.002, +0.023] −0.054 [−0.060, −0.049] +2.04 [+1.71, +2.42]
      matches, adj. 𝑝    sd 0.022, 0/8, 𝑝 < 0.01 ∗◦     sd 0.008, 0/8, 𝑝 = 0.164    sd 0.004, 0/8, 𝑝 < 0.01 ∗◦ sd 0.27, 0/8, 𝑝 < 0.01 ∗◦



Table 16 summarises the family and Supplement Table S22 gives all 40 hypotheses. Adding the write
to the U-Net core is worth −0.242 nats of selection NLL [−0.264, −0.213], ahead in all eight matches
under both procedures, and completion, local mass and the argmax move with it; on SoccerMap-v2 the
same write, Draw against C from the locked runs, is worth −0.165. The write therefore pays on three
cores: the published SoccerMap, SoccerMap-v2 and a canonical U-Net. The U-Net is the weaker core:
raster-only it trails arm C by +0.366 nats of selection NLL and painted it trails Draw by +0.290, behind
in every match under both procedures, so the modernised core is the stronger reader at this shared recipe.
This core comparison was not repeated under per-arm learning-rate tuning.

6.6       Interface alternatives
A learned attention painter is worse than the fixed splat, and a raster-free set decoder is worse than a
raster core with no set encoder, at the shipped recipe and at their own learning rates. The ablations of
Sec. 6.4.2 price removals from one design and leave two questions open that removal cannot answer:
whether the bilinear splat is the right way to write the embeddings onto the grid, and whether a grid and
a convolutional core are needed at all once the players are encoded as a set. Study 6 (Sec. 5.5) answers
both with two trained arms, three seeds each at the shipped recipe, against the locked Study 1 runs of D,
G2G and C: four pre-declared pairs on the ten PP and PS metrics, 40 hypotheses, with the hierarchical
bootstrap over 8 matches and 3 seeds and the exact 256-pattern max-𝑇 test. Table 17 summarises the
family and Supplement Table S23 gives every hypothesis; the pattern in the point estimates is the result.

The two arms. Dattn is arm D with one operator exchanged: only the bilinear splat is replaced by a cell-
query cross-attention painter in which each of the 7,072 cells queries, through fixed Fourier features of
its centre, keys built from each node’s embedding and position, with the embeddings as values, yielding


                                                                     27
the same 36 channels. The painter sees exactly what the splat sees; the two differ in normalisation.
The splat normalises per node, so a node’s contribution is conserved and most cells receive nothing
(sparse, node-conserving); the painter normalises per cell, so no cell is empty and no node’s contribution
is conserved (dense, cell-normalised). SetOnly has no raster channels and no convolutional core: the
relational encoder of G2G encodes the 23 nodes, the 7,072 cell queries attend to them through two
cross-attention blocks, and a per-cell MLP gives one logit per cell, so that the 68 × 104 logit surface feeds
the same heads, losses, calibration and evaluation as every other arm. Its widths were chosen for the
parameter count closest to G2G’s and frozen in the commitment, 700,303 parameters, 50 below G2G.
The arm is the set-attention family of Sec. 2 (Lee et al., 2019) with the same graph inputs and relational
encoder as G2G, so that the comparison evaluates a different decoding system, including removal of the
deterministic raster channels; it does not isolate the decoder alone. Both arms are specified in full in
Supplement Sec. S1.

A learned kernel is worse than the splat. Exchanging the bilinear splat for the attention painter, with
encoder, core, recipe and seeds held fixed, costs a fifth of a nat of selection NLL and a few hundredths
of local mass under both procedures; it moves the argmax farther out and barely moves completion
(Supplement Table S23). The seed-averaged selection NLL of Dattn is 5.528 against 5.319 for D and
5.490 for the raster-only arm C: the attention-painted arm is behind the core it feeds, and the swap costs
more than discarding sub-cell position altogether (Sec. 6.4.2) and more than the whole painted package
is worth (Table 12), with every Dattn head early-stopped. The painter has to learn the locality that the
splat has by construction, and at this recipe it does not: a dense, non-conserving write of every node into
every cell is worse for selection than writing nothing.

The shipped model against the painter. G2G keeps its margin over the painter on selection NLL,
completion log-loss and local mass under both procedures. Set against the small increment that message
passing adds on top of bilinear painting (Sec. 6.4.1), about four fifths of this margin is the painter’s cost,
not the relational encoder’s contribution.

The raster-free decoder is behind the raster core. The raster-free arm is behind everything. Against
G2G at matched parameter count SetOnly gives up more than half a nat of selection NLL and some eight
hundredths of completion log-loss; against the raster-only core C, which has no set encoder at all, it gives
up a third of a nat and nearly as much completion log-loss, all under both procedures, its seed-averaged
levels being 5.836 nats and 0.275 log-loss against 5.490 and 0.209 for C. One qualification is owed:
SetOnly’s selection head reached the 50-epoch cap in all three seeds, so its selection level is what the set
decoder reaches at the shipped budget, not its ceiling, whereas its completion deficit is one at convergence.
    Two things follow for the entity-to-grid framing of Sec. 1. The interface is the right abstraction but the
operator is not interchangeable: the tested splat, a sparse write at continuous coordinates that conserves
each node’s contribution, beats a learned attention kernel over the same embeddings and positions by
more than any ablation of the splat itself, though the painter changes locality, sparsity and conservation
at once, so which of the three is decisive is not settled. And on this corpus the tested raster-free system
is behind the grid plus convolutional core, given the same node features and the same parameter budget.

Tuned and converged. The qualification above is a budget, not a verdict: SetOnly’s selection head
reached the cap, and both arms were trained at the shipped rates that Supplement Sec. S5.5 shows favour
G2G. Study 11 (Sec. 5.5) removes both conditions for the two arms exactly as Study 4 removed them for
the controls, with the same sweep and selection rule, seeds 2–5 at the chosen rates and the test set opened
once, against the locked Study 4 units of G2G and C at their own selected rates: four pre-declared pairs, 40
hypotheses, with the hierarchical bootstrap over 8 matches and 5 seeds and the exact 256-pattern max-𝑇
test. Table 18 summarises the family; Supplement Table S24 gives every hypothesis. The rule chose
rates at or above the shipped ones for every head, ten times the shipped selection rate for the raster-free



                                                     28
Table 17: Study 6 summary: the interface alternatives at the shipped recipe: the attention-painted arm Dattn and
the raster-free SetOnly arm, three seeds each, against the locked Study 1 runs of D, G2G and C. Intervals from the
hierarchical bootstrap over 8 matches and 3 seeds (𝐵 = 10,000); family of 40 hypotheses. Reading conventions:
Sec. 6. Full family: Supplement Table S23

      Pair                      Selection NLL ↓       Completion log-loss ↓               Mass <5 m ↑          Argmax dist. (m) ↓
      Dattn − D       +0.208 [+0.146, +0.271] +0.011 [+0.000, +0.022] −0.023 [ −0.033, −0.013]             +0.52 [+0.18, +0.84]
      matches, adj. 𝑝 sd 0.056, 0/8, 𝑝 < 0.01 ∗◦ sd 0.011, 0/8, 𝑝 < 0.01 ◦ sd 0.009, 0/8, 𝑝 < 0.01 ∗◦ sd 0.27, 0/8, 𝑝 < 0.01 ◦
      G2G − Dattn     −0.260 [ −0.317, −0.220] −0.015 [ −0.023, −0.006] +0.029 [+0.025, +0.035]           −0.70 [ −0.93, −0.47]
      matches, adj. 𝑝 sd 0.043, 8/8, 𝑝 < 0.01 ∗◦ sd 0.007, 8/8, 𝑝 < 0.01 ∗◦ sd 0.002, 8/8, 𝑝 < 0.01 ∗◦ sd 0.15, 8/8, 𝑝 < 0.01 ∗◦
      SetOnly − G2G +0.568 [+0.460, +0.681] +0.081 [+0.056, +0.112] −0.044 [ −0.056, −0.035]               +0.71 [+0.37, +1.03]
      matches, adj. 𝑝 sd 0.111, 0/8, 𝑝 < 0.01 ∗◦ sd 0.027, 0/8, 𝑝 < 0.01 ∗◦ sd 0.005, 0/8, 𝑝 < 0.01 ∗◦ sd 0.19, 1/8, 𝑝 = 0.016 ∗◦
      SetOnly − C     +0.346 [+0.254, +0.435] +0.066 [+0.040, +0.096] −0.015 [ −0.027, −0.005]             −0.06 [ −0.39, +0.30]
      matches, adj. 𝑝 sd 0.093, 0/8, 𝑝 < 0.01 ∗◦ sd 0.027, 0/8, 𝑝 < 0.01 ∗◦ sd 0.009, 1/8, 𝑝 = 0.031 ∗◦        sd 0.14, 5/8, 𝑝 = 1


Table 18: Study 11 summary: the two set-attention arms of Study 6 under the Study 4 protocol, every arm at
its own validation-selected learning rate, cap 200 epochs, five seeds, against the locked Study 4 runs of G2G and
C. Intervals from the hierarchical bootstrap over 8 matches and 5 seeds (𝐵 = 10,000); family of 40 hypotheses.
Reading conventions: Sec. 6. Full family: Supplement Table S24

  Pair                         Selection NLL ↓        Completion log-loss ↓                  Mass <5 m ↑        Argmax dist. (m) ↓
  Dattn − G2G        +0.527 [+0.449, +0.610] +0.015 [+0.007, +0.024] −0.069 [−0.080, −0.059] +1.62 [+1.25, +1.97]
  matches, adj. 𝑝      sd 0.068, 0/8, 𝑝 < 0.01 ∗◦   sd 0.008, 0/8, 𝑝 < 0.01 ∗◦   sd 0.006, 0/8, 𝑝 < 0.01 ∗◦ sd 0.30, 0/8, 𝑝 < 0.01 ∗◦
  Dattn − C          +0.235 [+0.170, +0.308] +0.002 [−0.008, +0.013] −0.032 [−0.040, −0.025] +0.75 [+0.54, +0.94]
  matches, adj. 𝑝      sd 0.079, 0/8, 𝑝 < 0.01 ∗◦         sd 0.007, 4/8, 𝑝 = 1   sd 0.008, 0/8, 𝑝 < 0.01 ∗◦ sd 0.10, 0/8, 𝑝 < 0.01 ∗◦
  SetOnly − G2G +0.511 [+0.459, +0.566] +0.085 [+0.065, +0.110] −0.059 [−0.070, −0.049] +1.18 [+0.91, +1.42]
  matches, adj. 𝑝      sd 0.034, 0/8, 𝑝 < 0.01 ∗◦   sd 0.022, 0/8, 𝑝 < 0.01 ∗◦   sd 0.008, 0/8, 𝑝 < 0.01 ∗◦ sd 0.20, 0/8, 𝑝 < 0.01 ∗◦
  SetOnly − C        +0.219 [+0.183, +0.261] +0.071 [+0.048, +0.099] −0.021 [−0.030, −0.014] +0.31 [+0.08, +0.54]
  matches, adj. 𝑝      sd 0.032, 0/8, 𝑝 < 0.01 ∗◦   sd 0.025, 0/8, 𝑝 < 0.01 ∗◦   sd 0.006, 0/8, 𝑝 < 0.01 ∗◦   sd 0.16, 1/8, 𝑝 = 0.102



arm, and no head reached the cap: what bound the raster-free arm at the shipped recipe was the learning
rate, not the epoch cap.

The painter at its validation-selected learning rate. Tuning does not rescue the painter (Table 18).
At its selected rate Dattn scores 5.492 nats of selection NLL against 4.965 for tuned G2G and 5.257 for
tuned arm C, about half a nat behind the shipped model and a quarter behind the raster-only core under
both procedures, with less local mass and a farther argmax; completion is level with C and slightly behind
G2G. Per-arm tuning removed roughly a third of the controls’ shipped deficit (Sec. 6.3); it improves the
painter’s own selection NLL by 0.036 nats and widens its deficit to G2G from 0.260 to 0.527 nats, so the
attention-painted arm falls from level with arm C to a quarter of a nat behind it.

The raster-free arm at its validation-selected learning rate. Part of the raster-free arm’s shipped
deficit was the budget, and the rest is not. Tuned and converged, SetOnly scores 5.476 nats of selection
NLL, more than a third of a nat better than at the shipped recipe, yet still about half a nat behind tuned
G2G and a fifth of a nat behind tuned arm C under both procedures, with completion log-loss several
hundredths worse and less local mass against both; of the third of a nat that it trailed the raster-only core
by at the shipped budget, about a third was the budget and the rest remains at convergence. With the same
node features, the same parameter count and its own learning rate, the raster-free system is still worse
than a raster and a convolutional core with no set encoder at all, and the deficit is largest exactly where
there is no raster to fall back on, on completion.

6.7      What the surfaces rely on: probes and tracking noise
The surfaces rely on team identity, velocity and sub-cell position; under injected tracking noise the G2G
family degrades faster than the raster controls but keeps its selection lead. The studies above retrain

                                                                  29
arms; the two probes here edit only the inputs of the frozen shipped checkpoints, and carry no bootstrap
interval.

6.7.1   Inference-time probes
Each probe edits the input graph or the tracking state at inference only, reusing the shipped validation
temperatures unchanged, so it measures what the trained surfaces depend on under distribution shift.

Knockouts. Supplement Table S25 gives the full knockout probe table. Permuting the explicit pairwise
edge features produces only a +0.0006-nat change in selection NLL. Dropping the ball node costs +0.101
nats. Zeroing velocities costs +1.29 nats. Swapping team labels drives completion AUC to 0.18, below
chance. Team identity and velocity dominate. Permuting the edge features moves every metric by very
little, so the shipped model draws almost nothing from the explicit pairwise edge channel at test time;
this is consistent with the small message-passing increment above.

Quantisation: a sensitivity consistent with sub-cell position. The sharpest probe is quantisation:
every player and the ball is snapped to the centre of its ≈1 m grid cell, a 105/104 = 1.0096 m by 1.0 m
lattice, and the snapped positions feed both the rebuilt raster and the graph nodes, with no Gaussian
noise added. It costs G2G +0.127 nats (5.2446 → 5.3713) and arm D +0.071, and removes 0.0247
and 0.0186 of probability mass within 5 m. Every raster-only arm moves by at most 0.0012 nats (arm C
+0.0011, original −0.0007, wide −0.0005) and gains about 0.001 of local mass. This is an inference-time
sensitivity of the trained models, not a trained causal ablation. Only the splatting arms are materially
sensitive to the lattice, as one would expect if sub-cell precision is what the painted front end supplies;
arm D losing less than G2G indicates that message passing amplifies the sensitivity rather than creating
it. The quantise row is also the only selection row of the noise table (Supplement Table S26) in which
G2G is not the leading arm, and it loses that lead to arm D, the other splatting arm, rather than to any
raster control.

6.7.2   Tracking noise
Supplement Table S26 gives the noise curves, each level the mean and standard deviation over 𝑁 = 10
common-random-number draws; Sec. 7 draws their consequences. The noise model is i.i.d. per-frame
Gaussian
  √       tracking error, 𝑁 (0, 𝜎 2 ) per position component, with an independent velocity error of amplitude
𝜎 2, the amplitude a one-second finite difference of two independently perturbed frames carries. The
noise is independent across frames as well as players; a temporally correlated variant, in which the two
frames the pipeline uses carry a stationary AR(1) error pair with lag-one correlation 0.9 or 0.5, is reported
in Supplement Table S27. The same draws feed the regenerated 13-channel raster and the graph node
array, so comparisons across arms are paired within a draw. Baseline is each arm’s shipped unperturbed
test metrics and rebuild the regeneration path at 𝜎 = 0, where the rebuilt rasters and node arrays are
bit-identical to the shipped caches.
     Three readings matter. First, the G2G family is more noise-sensitive than the raster controls: by
𝜎 = 1 m G2G has lost 1.61 nats of selection NLL against the original’s 1.09. The sharper positional
response that the quantisation probe credits to the splat is also a sharper noise response. Second, the
selection advantage survives the whole range, compressed. Under independent noise G2G’s lead over
the nearest control is positive in every draw at every level; it compresses from +0.52 nats at 𝜎 = 0 to
+0.090 ± 0.025 at 1 m (worst draw +0.050) before re-widening to +0.53 at 4 m. Correlated noise does
not compress it monotonically: with near-persistent error (𝜌 = 0.9) the lead is +0.200 ± 0.013 at 1 m but
+0.032 ± 0.020 at 2 m, where one of ten draws is negative against the wide control. Against arm C G2G
stays ahead on selection in every draw at every level and correlation, and against arm D in all but two of
the hundred correlated draws. Supplement Table S27 gives the curves against arm C and arm D. Third,
on completion the picture is less favourable: from 𝜎 = 2 m the ordering against the controls is within
draw-to-draw noise (−0.007 ± 0.008), and arm D beats G2G in 10 of 10 draws (−0.0112 ± 0.0029).

                                                     30
6.8    Development history: the retrospective three-arm comparison
The original comparison used one run per arm at a shared recipe on the eight-match holdout. Its selection-
NLL advantage over the wide control was 0.5156 nats; later per-arm learning-rate selection reduced that
margin to about a third of a nat. These records are retained as development history, not as independent
confirmation, and the evaluation events behind them are in Sec. 5.3 and Sec. 7. Supplement Sec. S5 gives
the full results, multi-seed control extension, learning curves, and historical figures; Sec. 7 explains the
implications. The primary evidence is the cross-validation, external retraining, and tuned comparisons
above.

6.9    Value surfaces
Value is where the paper’s null models bite: G2G beats the constant-zero predictor on squared error, and
no arm beats it on absolute error. In this corpus PE is empirically the hardest of the three tasks: 92.6%
of test rewards are exactly zero, so value is a downstream integration result rather than a headline. It rests
on only 459 test passes with nonzero reward, 62 of them negative. Supplement Table S33 gives the EPV
comparison (Eq. (2)) over all 6,196 test rows against two null models. The constant-zero predictor, the
null model for a target that is zero on most rows, attains MSE 0.003482 and MAE 0.010666 for every
arm. The frozen baseline predicts the two outcome-conditioned training-branch means, gated by each
arm’s own calibrated PP surface; skill scores are relative to it. The graph-gate column re-gates every arm
with G2G’s calibrated PP surface, holding the gate common and letting only the value branches differ;
the oracle-gate column substitutes the realised pass outcome for the predicted probability.
    Value performance is metric-dependent. Among the learned systems G2G leads both controls on EPV
error, and against frozen per-branch means four of five arms carry positive MSE skill, up to +0.102; G2G
also beats the constant-zero predictor on MSE. But no arm beats constant zero on MAE (0.01067 against
the best model’s 0.01605), every arm being 1.5–2.0× worse. The original control’s value heads show no
detectable skill over the frozen constants (MSE difference +1.44 × 10−5 , [−7.10 × 10−5 , +7.71 × 10−5 ],
bootstrap 𝑝 = 0.659). The gate is nearly irrelevant. Re-gating with G2G’s PP closes only 6.2% of the
G2G-versus-original MSE gap and 9.7% of the G2G-versus-wide gap, while an oracle gate buys G2G
just 2.6% of its own MSE; the value branches rather than the completion gate do what work there is.
On the 459 nonzero-reward rows every arm carries positive skill over the frozen baseline on both MSE
and MAE. The positive tail is resolved (G2G’s precision@25 of 0.64 is a 10× lift over base rate); the
negative tail is resolved by no arm, the best precision@25 being 0.08 against only 62 negative rows. The
wide control’s advantages on imbalance-aware sign metrics carry intervals excluding zero (Supplement
Table S34, Sec. 7). Sign accuracy is not evidence for a G2G advantage.

6.10    Compute cost
Compute cost depends on the representation and on the batching regime. Supplement Table S35 retains
the original measurements, and a post-hoc audit measures all six principal arms, Draw included, under one
implementation, GPU, precision and timing protocol (Supplement Table S36), separating single-example
latency from batch-32 amortised cost and excluding preprocessing and data transfer. At batch size one,
arm C takes 2.800 ms per forward pass, Draw 4.127 ms and G2G 6.559 ms; amortised over a batch of 32
the three cost 0.087, 0.128 and 0.201 ms per pass. Raw painting is therefore cheaper than G2G but not
free relative to the raster-only core. G2G’s smaller counted FLOP total than the wide control does not
translate into lower measured latency, because FLOP counting omits some scatter and indexing work.
These measurements price a cost–accuracy trade-off; the recommendation of Sec. 1 follows from them
together with the accuracy results.

6.11    The surfaces themselves
Fig. 5 shows what the model draws for two real scenes of the World Cup final, pairing a failure with
a success. The completion score collapses inside the opponent’s block and behind pressing lines; the

                                                     31
Fig. 5 Two scenes of the 2022 World Cup final, one row per scene. Row 1 is outcome-selected: of the final’s
missed passes of at least 10 m, the one with the lowest completion score at its endpoint — a 27.7 m extra-time
attempt whose endpoint is the global minimum of the completion map (0.006). Row 2 is pre-declared in the
sealed evaluation record: a completed second-half pass (0.992). Left, the model’s completion score over candidate
destinations, temperature-scaled at observed endpoints and an extrapolation elsewhere. Right, the temperature-
scaled distribution over the ball’s next destination, on a log scale clipped at 𝑒 −20 ; it sums to one over the 7,072
cells. Yellow: attackers; blue: defenders; cyan ring: the player on the ball; X: where the ball ended up


selection surface concentrates on nearby, unpressured destinations. Both panels are temperature-scaled
model outputs: the selection surface is a distribution the loss shapes everywhere, whereas the completion
surface is calibrated only at observed endpoints and is an extrapolation elsewhere (Sec. 4.5). The eight
pre-declared scenes of the shipped evaluation were chosen by a purely chronological rule (equal index
strata of the final’s eligible-pass sequence, midpoint of each stratum). They were hashed into the test
commitment record before any test forward pass and rendered only after the metric lock; the second
displayed scene comes from that pre-declared set, and the first, as the caption states, was chosen after the
scores were known. Neither scene is quantitative validation.




                                                         32
7    Limitations and Threats to Validity
Each threat is stated here once; the record-level detail behind each statement is given in Supplement
Sec. S5.6.
     The shipped three-arm comparison is retrospective. The arms were evaluated sequentially and the
controls were not externally timestamped before the first G2G evaluation, so the records cannot establish
that their design choices were independent of that earlier result. We call it retrospective and controlled,
not pre-specified: the label is ours, the adaptive-reuse danger Dwork et al. (2015)’s. It also rests on one
training run per arm, which Study 2 (Supplement Sec. S5.2) addresses. The cross-validation, the tuned
comparison and the external replication now carry the paper’s claim, and only the external replication
scores data that took no part in development; what depends on the original split throughout is the choice
of architectures, recipe and grid, which no study here evaluates design-blind.
     The G2G arm opened the test set twice. Its log (Sec. 5.3) records two commitment/evaluation
cycles; the first was followed by an automated integrity failure that quarantined the transaction and
triggered retraining, and the shipped evaluation is the second. The log cannot establish whether any
first-cycle output was inspected; each control shows one commitment and zero recovery events. The
complete first-cycle block is printed in full (Supplement Sec. S8): the discarded opening was the better
draw on completion and on combined EPV, and the shipped cycle leads only on calibrated selection NLL,
by a few thousandths of a nat against control gaps of half a nat or more, and marginally on PE-succ MSE,
so selection toward a favourable draw is not a plausible reading of these records.
     The attribution ladder was first run post hoc. Its original single-seed form ran after the test set
had been opened and was therefore exploratory. Sec. 6.4.1 reports the pre-specified replacement; two of
the single-seed findings did not replicate and have been withdrawn (Supplement Sec. S11).
     The replications reuse the holdout, and therefore do not cure adaptivity. The pre-specified multi-
seed studies of Secs. 6.4.1–6.6 and 6.3, and Study 2, run on the previously used eight-match split. What
they cure is real: analysis, metric family, comparison pairs and multiplicity correction were fixed in a
signed commitment before training and the checkpoints sealed before a single opening. What they cannot
cure is that those matches had already been opened and that the hypotheses they test were derived from
that earlier look; no reusable-holdout mechanism of the kind Dwork et al. (2015) develop was used. Read
them as evidence that the attribution is stable across initialisations and was not selected after the fact, not
as independent confirmation on unseen data. The cross-validation and the external replication reproduce
the headline on matches never before scored as test data, but the recipe and the architectures of both were
chosen on the original split, and the external corpus is seven matches from a single second provider. The
ladder prices removals from one trained design at one budget rather than mapping an architecture space:
arm D shows what happens when message passing is deleted here, not that no relational encoder could
do better.
     What the intervals and tests cover. Intervals condition on the fitted models, the dataset construction
and the retained design choices. Match resampling accounts for within-match clustering but does not
model dependence from recurring teams or from overlapping cross-validation training sets, and one seed
per cross-validation fold does not estimate training-seed uncertainty, so the reported uncertainty does not
cover every source of variation under deployment or a new tournament. The sign-flip test’s error control
rests on sign-exchangeability of the paired match-level deltas under the joint null, which match grouping
motivates but does not guarantee, and strong familywise control needs the corresponding subset-null
conditions as well. Multiplicity is controlled within each study’s family, not across the adaptive sequence
of thirteen studies; prior holdout exposure and later reporting choices preclude reading the sequence as
prospective confirmation. The full families are retained to make that sequence inspectable.
     Roughly a third of the matched-budget selection margin disappears under per-arm learning-
rate tuning. With every arm tuned and converged over five seeds, the selection margin against the
capacity-matched control falls from about half a nat to a third (Sec. 6.3); the direction is unchanged. The
tuning grid is coarse, and which control is the stronger selector is itself learning-rate dependent.
     Calibration is unresolved. No calibration-error comparison in any study survives correction. The
metric is badly conditioned here, about two thirds of every arm’s calibrated completion predictions

                                                      33
falling in the single top bin (Supplement Sec. S10), and calibration is in any case established only where
the labels are: outcomes at unchosen cells are never observed, so neither whole-grid calibration nor
the counterfactual validity of the surface away from the selected destination has been established. The
external study adds a second failure mode: frozen across a provider boundary, G2G’s calibrated selection
likelihood falls behind the raster-only core in all seven matches and behind the raw-feature painter, on
the untempered score as well, while its localisation advantage survives. The raw-feature painter’s better
transfer is consistent with a learned encoder fitted to the source distribution without proving it, and the
G2G−Draw contrast changes the per-node encoder and message passing together, so it isolates neither.
     Value performance depends on the metric. No arm beats a constant-zero predictor on EPV MAE,
the original control’s value heads show no detectable skill over two frozen constants, no arm resolves the
negative reward tail, and the wide control exceeds G2G on imbalance-aware sign metrics (Sec. 6.9).
     Measurement error sets a floor, and G2G is more sensitive to it. Broadcast-derived positions
carry provider-dependent error reaching several metres (Crang et al., 2026; Mills et al., 2026). Under
the i.i.d. Gaussian perturbation of Sec. 6.7.2 the G2G family degrades faster than the raster controls: its
selection lead stays positive in every draw at every level of independent noise, and in all but one draw
under correlated noise, but has compressed to a small fraction of its noise-free size by one metre of
per-coordinate error, and on completion the ordering against the controls is within draw-to-draw noise
from two metres, with arm D ahead of G2G in every draw. Here 𝜎 is additional error per coordinate,
whereas provider validations often report two-dimensional error against ground truth. The perturbations
are added to measurements that already contain unknown error, and the targets are held fixed. They cannot
be converted directly into an expected advantage for a provider at a reported RMSE. The experiments
measure sensitivity to the specified extra noise, not recovery of true player positions.
     What the secondary comparisons do not settle. Each ablation and raster control of Secs. 6.4.2
and 6.5 is one change to one design at one budget, three seeds, on the reused holdout, and each confounds
something: nearest-cell painting changes the interpolation as well as the placement, the offset raster
carries a per-type within-cell mean rather than each node’s own position, and the finer raster halves every
convolution’s receptive field. They establish deficits for the raster constructions tested, not for every
raster model. Failure to reject the raw-versus-MLP contrast in the three-seed study does not establish
equivalence; the combined learned-content increment is resolved in the larger primary comparisons,
where message passing alone was not isolated. The attention painter and the raster-free decoder are
specific implementations rather than exhaustive representatives of their families, and each changes several
properties at once, so neither comparison isolates a single inductive bias; a kernel constrained to be local
and mass-conserving was not tried. The external raw-feature study reuses the external matches of Study
7 and strengthens attribution on that corpus rather than adding an independent replication.
     What the present design leaves open. The canonical U-Net of Study 13 is a second core-invariance
check at the shared recipe, and the published surface core of Overmeer et al. (2025), with its risk/reward
split, was not reproduced. A second tournament from the same provider, which would separate provider
shift from league shift, is not in this paper; nor are a threshold-sensitivity analysis and a blinded manual
audit of the endpoint pipeline.
     Target semantics and validation. The selection target is an observed next-event endpoint, not
the passer’s intent; for incomplete passes the intended target is unobserved (Robberechts et al., 2023;
Anzer and Bauer, 2022). The value target is model-generated, an XGBoost (Chen and Guestrin, 2016)
expected-goals estimator fitted on StatsBomb open data (StatsBomb, 2018), so the labels carry estimation
error of the kind van Arem et al. (2026) quantify. No blinded human audit establishes endpoint accuracy
for either corpus: the per-gate audit verifies the extraction accounting, not the semantic correctness of
each target, and the automated corroboration of the separate benchmark project is neither new human
ground truth nor a validation result of this paper. Indicator-level validation, expert-paired benchmarks
such as Overmeer et al. (2025), is absent. Provider-smoothed input positions have no established causal
filtering guarantee here, so the study is retrospective prediction from supplied snapshots, not a validated
live system. The external replication is seven matches from one other provider, with the value heads
unscored and an estimated event–frame alignment; it establishes that the ordering and the size of the


                                                    34
interface effect transfer when the arms are retrained, and that frozen likelihood ordering does not. Its
endpoints are 91.2% receiver captures against 0.21% on the World Cup, and the post-hoc stratification
of Sec. 6.2 shows the external margin concentrated in that stratum, so on this corpus the interface effect
is not separated from a label rule that places endpoints at tracked player positions; the World Cup
corpus, whose labels are almost entirely next-event, is what shows the effect does not require that rule.
Independent release-time and endpoint annotation, construction-threshold sensitivity, and downstream
decision evaluation remain necessary for stronger practical claims.


8    Conclusion
Writing each player’s features onto the pitch at the player’s continuous position improves endpoint-
supervised surfaces on every core and corpus we trained it on. Relative to the same raster-only core,
the full front end reduces selection NLL by 0.251 nats across the World Cup folds, 0.292 nats under
per-arm learning-rate selection, and 0.239 nats after external retraining, ahead in every match of each
comparison. The same write pays on the original SoccerMap and on a canonical U-Net. The operator is
standard bilinear scatter-add; the finding is that the interface, not what is written through it, carries most
of the gain.
    Painting the nine raw node features with no learned encoder retains approximately three quarters of
that gain. The learned encoder and message passing add a further 0.065–0.067 nats in the cross-validation
and tuned comparisons, an increment that is real but small. For a new deployment we would therefore
start from raw painting, which has no front-end parameters and costs 4.127 ms per example against G2G’s
6.559 ms at batch size one (Supplement Table S36), and add the learned front end where in-distribution
selection likelihood is the objective and the provider is fixed. Frozen across a provider boundary, the
ordering reverses: the raster-only core has the best selection likelihood of the three, raw painting is
numerically ahead of G2G without an adjusted max-𝑇 rejection, and only retraining restores the interface
effect.
    The evidence concerns reconstructed observed endpoints. Reused holdouts, overlapping folds,
provider-dependent tracking error, and unobserved outcomes at alternative destinations bound what
the intervals cover. The value task remains secondary and metric-dependent. Independent endpoint
validation and evaluation of downstream decisions are needed before these surfaces can be treated as
calibrated assessments of hypothetical passes.


Statements and Declarations
Funding.    No funding was received for conducting this study. Computing resources were the authors’
own.

Competing interests. The authors have no competing interests to declare that are relevant to the content
of this article. The World Cup data were obtained under the provider’s research licence; neither author
has a financial relationship with PFF FC, StatsBomb or the IDSSE authors.

Data availability. The raw PFF FC World Cup tracking and event data (PFF FC, 2024) are obtained
from the provider on request under its terms of use and are not redistributed by us; reconstructing that
corpus requires a copy obtained directly from the provider. The public IDSSE source data (Bassek et al.,
2025) are available under CC BY 4.0 from their authors, and the expected-goals estimator uses public
StatsBomb data (StatsBomb, 2018); data provided by StatsBomb. The per-row locked predictions, study
commitment and lock records, and analysis tables that underlie every reported number are retained by the
authors and are available from the corresponding author on reasonable request.




                                                     35
Code availability. The source code is not publicly available. The supplement specifies every arm,
study design, admission gate and scoring rule in enough detail to re-implement them.

Author contributions. Conceptualization: K.G. and O.G. Methodology and model development: K.G.
Software, experimental design, formal analysis, investigation and visualization: O.G. Original draft:
O.G. Review, editing and final manuscript preparation: K.G. Both authors reviewed and approved the
manuscript.

Use of AI tools. Claude (Anthropic) assisted with drafting and refactoring analysis and figure scripts,
deriving multi-seed orchestration code from the training engine, and restructuring and editing manuscript
text. Codex (OpenAI) assisted with consistency checks, figure generation, source-to-result checks, and a
post-hoc implementation and compute audit that left all locked predictive results unchanged. These uses
extend beyond copy-editing, and the authors reviewed and verified the output of both tools. The tools are
not authors; the human authors are responsible for the study design, the verification and interpretation of
results, and approval of the final manuscript.

Prior dissemination. No part of this manuscript has been published, presented, posted or submitted
elsewhere. A companion manuscript by the same authors describing the public pass-surface corpus of
Sec. 6.2 as a benchmark is in preparation; it shares data and extraction code with this paper but no claim,
result or text (Sec. 1).

Ethics approval and consent. Not applicable: the study uses licensed and public sports data on
professional matches and involves no recruitment, intervention, or collection of new participant data.

References
Anzer, G. and Bauer, P. (2022). Expected passes: Determining the difficulty of a pass in football (soccer) using spatio-temporal
  data. Data Mining and Knowledge Discovery, 36:295–317. https://doi.org/10.1007/s10618-021-00810-3.

Bassek, M., Rein, R., Weber, H., and Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite
  soccer. Scientific Data, 12. Article 195. https://doi.org/10.1038/s41597-025-04505-y.

Battaglia, P. W., Hamrick, J. B., Bapst, V., Sanchez-Gonzalez, A., Zambaldi, V., Malinowski, M., Tacchetti, A., Raposo, D.,
  Santoro, A., Faulkner, R., Gulcehre, C., Song, F., Ballard, A., Gilmer, J., Dahl, G., Vaswani, A., Allen, K., Nash, C.,
  Langston, V., et al. (2018). Relational inductive biases, deep learning, and graph networks. arXiv:1806.01261. https:
  //arxiv.org/abs/1806.01261.

Brody, S., Alon, U., and Yahav, E. (2022). How attentive are graph attention networks? In International Conference on Learning
  Representations.

Cameron, A. C., Gelbach, J. B., and Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors.
  The Review of Economics and Statistics, 90(3):414–427. https://doi.org/10.1162/rest.90.3.414.

Chen, J., Paris, S., and Durand, F. (2007). Real-time edge-aware image processing with the bilateral grid. ACM Transactions
  on Graphics, 26(3):103. https://doi.org/10.1145/1276377.1276506.

Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD
  International Conference on Knowledge Discovery and Data Mining, pages 785–794. https://doi.org/10.1145/
  2939672.2939785.

Crang, Z. L., Johnston, R. D., Mills, K. L., Billingham, J., Robertson, S., Cole, M. H., Weakley, J., Hewitt, A., and Duthie,
  G. M. (2026). Concurrent validity of computer-vision artificial intelligence player tracking software using broadcast footage.
  Journal of Sports Analytics, 12:1–13. https://doi.org/10.1177/22150218261445834.

Davis, J., Bransen, L., Devos, L., Jaspers, A., Meert, W., Robberechts, P., Van Haaren, J., and Van Roy, M. (2024). Methodology
  and evaluation in sports analytics: Challenges, approaches, and lessons learned. Machine Learning, 113:6977–7010.
  https://doi.org/10.1007/s10994-024-06585-0.




                                                              36
Decroos, T., Bransen, L., Van Haaren, J., and Davis, J. (2019). Actions speak louder than goals: Valuing player actions in
  soccer. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
  pages 1851–1861. https://doi.org/10.1145/3292500.3330758.

Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., and Roth, A. (2015). Generalization in adaptive data analysis and
  holdout reuse. In Advances in Neural Information Processing Systems, volume 28.

Efron, B. and Tibshirani, R. J. (1994). An Introduction to the Bootstrap. Chapman & Hall/CRC.

Fernández, J. and Bornn, L. (2021). SoccerMap: A deep learning architecture for visually-interpretable analysis in soccer. In
   Machine Learning and Knowledge Discovery in Databases: Applied Data Science and Demo Track (ECML PKDD 2020),
   volume 12461 of LNCS, pages 491–506. Springer. https://doi.org/10.1007/978-3-030-67670-4_30.

Fernández, J., Bornn, L., and Cervone, D. (2021). A framework for the fine-grained evaluation of the instantaneous expected
   value of soccer possessions. Machine Learning, 110:1389–1427. https://doi.org/10.1007/s10994-021-05989-6.

Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). On calibration of modern neural networks. In Proceedings of the
  34th International Conference on Machine Learning, pages 1321–1330.

He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. In IEEE Conference on Computer
  Vision and Pattern Recognition (CVPR), pages 770–778. https://doi.org/10.1109/CVPR.2016.90.

Hendrycks, D. and Gimpel, K. (2016). Gaussian error linear units (GELUs). arXiv:1606.08415. https://arxiv.org/abs/
  1606.08415.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2):65–70.

Hu, J., Shen, L., and Sun, G. (2018). Squeeze-and-excitation networks. In IEEE Conference on Computer Vision and Pattern
  Recognition (CVPR), pages 7132–7141. https://doi.org/10.1109/CVPR.2018.00745.

Hubáček, O., Šourek, G., and Železný, F. (2019). Deep learning from spatial relations for soccer pass prediction. In
  Machine Learning and Data Mining for Sports Analytics (MLSA 2018), volume 11330 of LNCS, pages 159–166. Springer.
  https://doi.org/10.1007/978-3-030-17274-9_14.

Jaderberg, M., Simonyan, K., Zisserman, A., and Kavukcuoglu, K. (2015). Spatial transformer networks. In Advances in Neural
   Information Processing Systems, volume 28. https://arxiv.org/abs/1506.02025.

Jin, M. and Li, J. (2023). Graph to grid: Learning deep representations for multimodal emotion recognition. In Proceedings of the
   31st ACM International Conference on Multimedia, pages 5985–5993. https://doi.org/10.1145/3581783.3612074.

Karakuş, O. and Arkadaş, H. (2026). Through the gaps: Uncovering tactical line-breaking passes with clustering. In Machine
  Learning and Data Mining for Sports Analytics (MLSA 2025), volume 2833 of CCIS, pages 86–96. Springer. https:
  //doi.org/10.1007/978-3-032-15165-0_7.

Kato, H., Ushiku, Y., and Harada, T. (2018). Neural 3D mesh renderer. In IEEE/CVF Conference on Computer Vision and
  Pattern Recognition (CVPR), pages 3907–3916. https://doi.org/10.1109/CVPR.2018.00411.

Lam, R., Sanchez-Gonzalez, A., Willson, M., Wirnsberger, P., Fortunato, M., Alet, F., Ravuri, S., Ewalds, T., Eaton-Rosen,
  Z., Hu, W., Merose, A., Hoyer, S., Holland, G., Vinyals, O., Stott, J., Pritzel, A., Mohamed, S., and Battaglia, P. (2023).
  Learning skillful medium-range global weather forecasting. Science, 382(6677):1416–1421. https://doi.org/10.1126/
  science.adi2336.

Lang, A. H., Vora, S., Caesar, H., Zhou, L., Yang, J., and Beijbom, O. (2019). PointPillars: Fast encoders for object detection
  from point clouds. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 12689–12697.
  https://doi.org/10.1109/CVPR.2019.01298.

Lee, J., Lee, Y., Kim, J., Kosiorek, A. R., Choi, S., and Teh, Y. W. (2019). Set transformer: A framework for attention-
  based permutation-invariant neural networks. In Proceedings of the 36th International Conference on Machine Learning,
  volume 97 of Proceedings of Machine Learning Research, pages 3744–3753. https://proceedings.mlr.press/v97/
  lee19d.html.

Lin, T.-Y., Dollár, P., Girshick, R., He, K., Hariharan, B., and Belongie, S. (2017). Feature pyramid networks for object detection.
   In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 936–944. https://doi.org/10.1109/
   CVPR.2017.106.

Liu, S., Chen, W., Li, T., and Li, H. (2019). Soft rasterizer: A differentiable renderer for image-based 3D reasoning. In
   IEEE/CVF International Conference on Computer Vision (ICCV), pages 7707–7716. https://doi.org/10.1109/ICCV.
   2019.00780.


                                                                37
Lyu, Y., Huang, X., and Zhang, Z. (2023). Revisiting 2D convolutional neural networks for graph-based applications. IEEE
  Transactions on Pattern Analysis and Machine Intelligence, 45(6):6909–6922. https://doi.org/10.1109/TPAMI.2021.
  3083614.

Mills, K., Wang, H., Crang, Z., Billingham, J., Duthie, G., Johnson, R., and Robertson, S. (2026). Automatic event detection
  in association football using broadcast-derived tracking data. Sports Engineering, 29. Article 15. https://doi.org/10.
  1007/s12283-026-00549-4.

Niklaus, S. and Liu, F. (2020). Softmax splatting for video frame interpolation. In IEEE/CVF Conference on Computer Vision
  and Pattern Recognition (CVPR), pages 5437–5446. https://doi.org/10.1109/CVPR42600.2020.00548.

Overmeer, T., Janssen, T., and Nuijten, W. P. M. (2025). Revisiting expected possession value in football: Introducing a U-Net
  architecture, reward and risk for passes, and a benchmark. In Proceedings of the 13th International Conference on Sport
  Sciences Research and Technology Support, pages 100–109. https://doi.org/10.5220/0013784300003988.

Pei, Y., De Silva, V., and Caine, M. (2024). Passing heatmap prediction based on transformer model using tracking data
   for football analytics. In Intelligent Systems and Pattern Recognition (ISPR 2023), volume 1940 of CCIS, pages 162–173.
   Springer. https://doi.org/10.1007/978-3-031-46335-8_13.

PFF FC (2024). Unleash your inner analyst: PFF FC’s 2022 World Cup dataset now available. PFF FC Blog. https:
  //www.blog.fc.pff.com/blog/pff-fc-release-2022-world-cup-data.

Philion, J. and Fidler, S. (2020). Lift, splat, shoot: Encoding images from arbitrary camera rigs by implicitly unprojecting to
   3D. In Computer Vision – ECCV 2020, Lecture Notes in Computer Science, pages 194–210. Springer. https://doi.org/
   10.1007/978-3-030-58568-6_12.

Pineau, J., Vincent-Lamarre, P., Sinha, K., Larivière, V., Beygelzimer, A., d’Alché Buc, F., Fox, E., and Larochelle, H. (2021).
   Improving reproducibility in machine learning research (a report from the NeurIPS 2019 reproducibility program). Journal
   of Machine Learning Research, 22(164):1–20.

Power, P., Ruiz, H., Wei, X., and Lucey, P. (2017). Not all passes are created equal: Objectively measuring the risk and reward
  of passes in soccer from tracking data. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge
  Discovery and Data Mining, pages 1605–1613. https://doi.org/10.1145/3097983.3098051.

Qi, C. R., Su, H., Mo, K., and Guibas, L. J. (2017). PointNet: Deep learning on point sets for 3D classification and segmentation.
   In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 77–85. https://doi.org/10.1109/
   CVPR.2017.16.

Rahimian, P., Davis, J., and Toka, L. (2026). Temporal graph network framework for quantifying pass reception probabilities
  against defensive structures. Machine Learning, 115. Article 6. https://doi.org/10.1007/s10994-025-06935-6.

Robberechts, P., Van Roy, M., and Davis, J. (2023). un-xPass: Measuring soccer player’s creativity. In Proceedings of the 29th
  ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pages 4768–4777. https://doi.org/10.1145/
  3580305.3599924.

Ronneberger, O., Fischer, P., and Brox, T. (2015). U-Net: Convolutional networks for biomedical image segmentation. In
  Medical Image Computing and Computer-Assisted Intervention (MICCAI 2015), pages 234–241. https://doi.org/10.
  1007/978-3-319-24574-4_28.

Spearman, W. (2018). Beyond expected goals. In 12th MIT Sloan Sports Analytics Conference.

Spearman, W., Basye, A., Dick, G., Hotovy, R., and Pop, P. (2017). Physics-based modeling of pass probabilities in soccer. In
  11th MIT Sloan Sports Analytics Conference.

StatsBomb (2018). StatsBomb open data. GitHub repository. https://github.com/hudl/open-data, accessed 2026-08-14.

Stöckl, M., Seidl, T., Marley, D., and Power, P. (2021). Making offensive play predictable: Using a graph convolutional network
   to understand defensive performance in soccer. In 15th MIT Sloan Sports Analytics Conference.

Su, H., Jampani, V., Sun, D., Maji, S., Kalogerakis, E., Yang, M.-H., and Kautz, J. (2018). SPLATNet: Sparse lattice
   networks for point cloud processing. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages
   2530–2539. https://doi.org/10.1109/CVPR.2018.00268.

van Arem, K., Söhl, J., Bruinsma, M., and Jongbloed, G. (2026). Model quality in football: Quantifying the quality of an
   expected threat model. arXiv:2604.21087. https://arxiv.org/abs/2604.21087.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. (2017). Attention is
  all you need. In Advances in Neural Information Processing Systems, volume 30, pages 5998–6008.


                                                               38
Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., and Bengio, Y. (2018). Graph attention networks. In International
  Conference on Learning Representations.

Wang, Y., Fathi, A., Kundu, A., Ross, D. A., Pantofaru, C., Funkhouser, T., and Solomon, J. (2020). Pillar-based object detection
  for autonomous driving. In Computer Vision – ECCV 2020, Lecture Notes in Computer Science, pages 18–34. Springer.
  https://doi.org/10.1007/978-3-030-58542-6_2.

Wang, Z., Veličković, P., Hennes, D., Tomašev, N., Prince, L., Kaisers, M., Bachrach, Y., Elie, R., Wenliang, L. K., Piccinini,
  F., Spearman, W., Graham, I., Connor, J., Yang, Y., Recasens, A., Khan, M., Beauguerlange, N., Sprechmann, P., Moreno,
  P., et al. (2024). TacticAI: An AI assistant for football tactics. Nature Communications, 15. Article 1906. https:
  //doi.org/10.1038/s41467-024-45965-x.

Westfall, P. H. and Young, S. S. (1993). Resampling-Based Multiple Testing: Examples and Methods for p-Value Adjustment.
  Wiley.

Wu, Y. and He, K. (2018). Group normalization. In European Conference on Computer Vision (ECCV), pages 3–19.
  https://doi.org/10.1007/978-3-030-01261-8_1.

Yifan, W., Serena, F., Wu, S., Öztireli, C., and Sorkine-Hornung, O. (2019). Differentiable surface splatting for point-based
   geometry processing. ACM Transactions on Graphics, 38(6):230:1–230:14. https://doi.org/10.1145/3355089.
   3356513.

Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R., and Smola, A. (2017). Deep sets. In Advances in Neural
  Information Processing Systems, volume 30. https://arxiv.org/abs/1703.06114.

Zhou, Y. and Tuzel, O. (2018). VoxelNet: End-to-end learning for point cloud based 3D object detection. In IEEE/CVF
  Conference on Computer Vision and Pattern Recognition (CVPR), pages 4490–4499. https://doi.org/10.1109/CVPR.
  2018.00472.




                                                               39
