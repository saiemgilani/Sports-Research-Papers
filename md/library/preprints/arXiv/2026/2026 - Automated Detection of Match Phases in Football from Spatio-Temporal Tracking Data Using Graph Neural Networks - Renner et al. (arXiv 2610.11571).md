<!-- source: library/preprints/arXiv/2026/2026 - Automated Detection of Match Phases in Football from Spatio-Temporal Tracking Data Using Graph Neural Networks - Renner et al. (arXiv 2610.11571).pdf -->
<!-- item: https://arxiv.org/abs/2610.11571 -->
<!-- arXiv: 2610.11571, submitted 2026-10-08 -->
<!-- authors: Vincent Renner; Nils Koster; Pascal Bauer; Melanie Schienle -->
<!-- machine conversion from the stored PDF via pdftotext -layout, 2026-10-28; equations, tables and figures are NOT preserved - consult the PDF for those -->

                                              AUTOMATED D ETECTION OF M ATCH P HASES IN F OOTBALL
                                              FROM S PATIO -T EMPORAL T RACKING DATA U SING G RAPH
                                                                N EURAL N ETWORKS

                                                              Vincent Renner1,2        Nils Koster1,3    Pascal Bauer4,5    Melanie Schienle1
                                                              1
arXiv:2610.11571v1 [stat.AP] 8 Oct 2026

                                                                  Institute of Statistics, Karlsruhe Institute of Technology, Karlsruhe, Germany
                                                                                   2
                                                                                     Karlsruher Sport-Club, Karlsruhe, Germany
                                                                           3
                                                                             Broad Institute of MIT & Harvard, Cambridge, MA, USA
                                                                            4
                                                                              German Football Association (DFB), Frankfurt, Germany
                                                                    5
                                                                      Chair for Sports Analytics, Saarland University, Saarbrücken, Germany
                                                                      {vincent.renner,nils.koster,melanie.schienle}@kit.edu
                                                                                              pascal.bauer@dfb.de

                                                                                                October 9, 2026

                                                                                                 A BSTRACT
                                                   Spatio-temporal tracking data has opened new possibilities for detecting complex tactical patterns in
                                                   football, yet modeling the interactive movements of multiple players remains challenging. This paper
                                                   proposes a framework combining graph neural networks (GNNs) with a sequential model to classify
                                                   match phases on a second-by-second basis across a seven-class taxonomy. Match phase classification
                                                   is tactically meaningful, and the availability of rule-based labels across 203 matches makes it a
                                                   suitable testbed for a systematic comparison of adjacency constructions and message-passing layers,
                                                   a question that has received limited attention in existing research. Our selected GNN-LSTM model
                                                   outperforms all aggregated-feature baselines, including XGBoost and a Long Short-Term Memory
                                                   (LSTM) network, as the strongest baseline scores 4.6% lower in macro F1. Graph representations
                                                   using a domain-informed Delaunay triangulation that approximates passing lanes, paired with a
                                                   custom Spatial Edge-Augmented Convolution (SEAConv) layer that injects edge attributes directly
                                                   into messages, achieve the best performance by capturing spatial dependencies while limiting
                                                   uninformative messages from redundant edges. Integrated Gradients attributions indicate the model
                                                   uses spatial player configurations, particularly horizontal positioning, in combination with possession
                                                   and ball-status indicators. This work offers an automated solution for fine-grained tactical analysis,
                                                   reducing the need for manual tagging and providing deeper insight into dynamic team behavior.

                                          Keywords sports analytics; soccer; tactical pattern recognition; message passing; model interpretability; positional data

                                          1   Introduction

                                          Data analytics has become central to association football, spanning player recruitment, athletic performance, and
                                          tactical analysis (Rein and Memmert, 2016). This scope has been further expanded through the introduction of tracking
                                          systems, recording the positions of all players and the ball at high frequency (10–25 Hz). Unlike traditional event-based
                                          data, tracking data captures all movements on- and off-ball, permitting a more comprehensive reconstruction of game
                                          situations and making tactical analysis an active area of research (Goes et al., 2021). Modeling this data while preserving
                                          the complete spatial arrangement of all players over time is a complex task. While several modeling approaches exist,
                                          no systematic comparison has identified a method that consistently outperforms all others across this complex setting
                                          in space and time. In particular, previous works have used graph neural networks (GNNs; see Hamilton, 2020) that
                                          can handle the relational structure of football through permutation-invariant operations over player nodes (see e.g.,
                                                                                         A PREPRINT - O CTOBER 9, 2026

Anzer et al., 2022; Lee et al., 2026; Ochin et al., 2025; Raabe et al., 2023). How GNNs compare to established tabular
baselines such as gradient-boosted trees on tabular-based features, and how architectural choices such as graph topology
and message-passing mechanism affect performance in a tactical setting, remain open questions which we address in
this work. We study match phase identification as the evaluation task: it is tactically meaningful, as players’ behavior,
instructions, and positioning all depend on the current phase (see e.g., Ric et al., 2021; Shaw and Glickman, 2019), and
tracking-synced labels are available at scale.
In this paper, we propose a GNN approach to capture spatial and temporal dependencies among football players, aiming
to identify the current match phase for both teams at one-second resolution. Our contributions are as follows:
First, our GNN uses player-level features directly, preserving the full spatial structure of all players instead of aggregating
into team-wide features. We define a seven-class phase taxonomy that includes three defensive sub-phases (‘High
Block’, ‘Mid Block’, ‘Low Block’), distinguishable only by spatial player arrangements. Labels are generated by a
rule-based model across 203 matches, enabling large-scale training and evaluation.
Second, we construct adjacencies using Delaunay triangulation, motivated by the triangular passing structures players
form to keep passing options open. To capture the spatial and directional structure of these interactions, we adapt the
edge-augmented graph transformer layer of Shi et al. (2021) into a Spatial Edge-Augmented Convolution (SEAConv).
Relational edge attributes (pairwise distance, relative angle, and team membership) enter both the attention weights and
the messages themselves, and player coordinates are encoded with random Fourier features (Tancik et al., 2020) to
resolve fine-grained positional differences. We systematically evaluate both of these domain-driven design choices
against common alternatives, as these properties have a direct influence on learning behavior in GNNs (Alon and Yahav,
2021; Dwivedi et al., 2023; Topping et al., 2022; Xu et al., 2019).
Third, we make the model’s predictions interpretable through the application of Integrated Gradients (IG; Sundararajan
et al., 2017), analyzing the importance of the graph’s features, as well as the overall contribution of individual spatial
features compared to graph-wide possession-based information.
Our work builds on two lines of research: tactical analysis from tracking data, and graph-based modeling in football.
On the tactical side, tracking data has enabled applications such as team formation detection (Bauer et al., 2023),
pressing analysis (Bauer and Anzer, 2021; Lee et al., 2025), and play-style characterization (Shaw and Glickman,
2019). Methodologically, GNNs have gained traction for modeling spatial tracking data. Stöckl et al. (2021) show
empirically that GNNs can make hand-crafted features unnecessary in certain football analytics tasks. Raabe et al. (2023)
propose ‘tactical graph networks’ that transform tactical situations into graph representations to predict possession
gain probability. Ochin et al. (2025) implement a graph-based architecture for event detection from tracking data.
Graph-based representations of tracking data are not specific to football and have been applied across a range of invasion
sports (e.g., Raabe et al., 2023; Sun et al., 2019; Xenopoulos and Silva, 2021; Yeh et al., 2019). Automated match
phase detection has recently been approached from several directions. Biermann et al. (2025) train a recurrent model on
handcrafted team-level features for hierarchical binary classification of match phases with manually annotated labels.
Rothe et al. (2026) define an expert state system that pairs in-possession and out-of-possession phases, including low,
mid and high blocks, and detect these states by clustering the number of players per pitch zone within each ball zone,
validated against human annotation of twelve Bundesliga matches. Our work differs from these approaches in three
respects. First, instead of zone-count representations, which discard inter-player distances and team compactness,
we operate on player-level graphs that retain continuous positions and pairwise relations. Our taxonomy spans in-
possession, out-of-possession, and transition phases, and the model itself must separate active phases from stoppages
and unclassifiable play rather than relying on a pre-processing step. Second, we systematically compare adjacency
constructions and message-passing layers across 80 runs, isolating how graph topology and message design affect
tactical classification, a question that has received limited attention in football. Third, rule-based labels allow training
and evaluation on 203 matches, substantially more than related work, at the cost of agreement with human annotation.
The rest of the paper is structured as follows: Section 2 introduces the data and graph representations. Section 3
describes the message-passing layers and model architecture. Section 4 presents the empirical evaluation. In Section 5,
we interpret the model through graph embeddings and feature attributions. Section 6 discusses the results. All code is
available at: https://gitlab.kit.edu/vincent.renner/match_phase_detection.

2     Data and Graph Representations

2.1   Data Set

The data set, provided by the Deutscher Fußball-Bund (DFB), comprises 203 matches from the DFB-Pokal, senior
national team, and under-21 national team competitions. The data set covers men’s competitions exclusively. Table 5 in
the Appendix lists the number of matches per competition and season.

                                                              2
                                                                                      A PREPRINT - O CTOBER 9, 2026

The data set comprises positional data at 25 Hz for all 22 players and the ball, described by spatial and kinematic
features such as speed and acceleration. These data were collected by TRACAB1 , which has been used in various
studies (see e.g., Anzer and Bauer, 2022; Bauer and Anzer, 2021; Bauer et al., 2023) and validated by Linke et al. (2018,
2020). Event data were collected by Sportec Solutions. Both data sets were provided in the Common Data Format
(Anzer et al., 2025). The matches include the 2019/20–2024/25 seasons, and were selected based on data quality and
the availability of match phase labels: for a total of six (sub)phases of play (‘Build Up’, ‘Low Block’, ‘Mid Block’,
‘High Block’, ‘Counter Attack’, ‘Defensive Transition’; see also Table 1), we use rule-based labels (see Appendix A).
We construct a set of ten tailored spatial features outlined in Table 6 in the Appendix.

Table 1: Descriptive Statistics. Share of phases in the data set and mean duration in seconds. Both are computed over
the full data set of 203 matches. The numbers on the validation split differ slightly.
                                  In Possession     Out of Possession           Transitions        No Phase
                                                  High     Mid    Low      Counter    Defensive
                                    Build Up                                                       No Phase
                                                  Block   Block   Block    Attack     Transition
                 Share               15.6%        0.9%    15.9%    2.1%     3.0%        5.3%        57.2%
                 Mean Duration       16.6s        5.6s    13.9s    7.0s     6.3s        7.5s        22.7s

Every part of the match without an active phase for the observed team is labeled as ‘No Phase’. Keeping ‘No Phase’ in
our taxonomy is essential, as no prior information regarding start and end points of actual phases can be passed into the
model in a real-world application. This results in seven (sub)classes within four larger categories as outlined in Table 1.
The empirical distribution of the match phases and the mean duration of each is reported as well. ‘No Phase’ occupies
the largest share of match time (57.2%) as it consists of the union of stoppages and unclassifiable play, while ‘Build Up’
and ‘Mid Block’ are the most frequent labeled phases. Transition periods occupy less time, and ‘High Block’, ‘Low
Block’, and ‘Counter Attack’ are relatively rare (6.0% in total). Since both teams are labeled at each second, both
teams’ data can be used, effectively doubling the number of observations. Further, we treat a full match as a single
sequence from start to end.

2.2       Graph Representations

We model each timestamp of the tracking data as a directed graph Gt = (V, E). V consists of all players and the ball, so
k = |V| = 23. Situations in which a player has been sent off are treated identically, with the corresponding reduction in
the number of nodes. Each node vi carries an m-dimensional attribute vector xi ∈ Rm comprising spatial coordinates
(see Table 6), movement descriptors, and indicators for the node type (attacking player, defending player, or ball)
relative to the focal team, yielding a node feature matrix X ∈ Rk×m . All variables are listed in Table 6 in the Appendix.
Connectivity is encoded by an adjacency matrix A ∈ {0, 1}k×k with ai,j = 1 if edge (vi , vj ) ∈ E. Each edge carries
an l-dimensional attribute vector ei,j ∈ Rl containing the distance and angle between connected nodes as well as
indicators of the relationship type (teammates, opponents, player-to-ball), collected in a feature tensor E ∈ Rk×k×l .
We set ei,j = 0 if ai,j = 0, where 0 denotes the zero-vector. We include graph-level features u ∈ {0, 1}2 indicating
whether the focal team is in possession and whether the ball is in play. To reduce noise, one graph per second is created
by averaging features across the 25 frames.
In other graph-based applications such as molecular systems (Rittig et al., 2023; Wang et al., 2023), edges are unique
and observable, whereas edges in tracking data are not. Hence, the edge construction strategy poses a modeling
decision, trading off computational cost against the quantity and type of information exchanged between nodes. Prior
work typically uses complete graphs (see e.g., Lee et al., 2026; Wang et al., 2024) without systematic comparison
of alternatives, leaving this design choice largely unexplored for football applications. Raabe et al. (2023) reduce
the complete graph based on different distance-based thresholds, showing that a sparse adjacency matrix can lead to
improved results.
We propose to construct the adjacency matrix through Delaunay triangulation (Delaunay, 1934), motivated by the
spatial structure of football. Players typically arrange in triangles to create and maintain passing options; the Delaunay
triangulation encodes this property by connecting nodes into triangles such that no other node lies inside the circumcircle
of any triangle. Formally, given the set of spatial node coordinates
                                                P = xpos      ∈ R2 | i ∈ V ,
                                                      
                                                         i

      1
    TRACAB provides an optical tracking system that originated within ChyronHego. TRACAB Technologies has operated as a
standalone company since 2021 and was acquired by EA Sports in 2025.

                                                            3
                                                                                       A PREPRINT - O CTOBER 9, 2026

                                 Delaunay                                          k-NN (3)

                                  Radius                                           Complete

Figure 1: Adjacency Construction Options. Comparison of edge construction strategies for a single observation in
the data set. Node colors indicate team associations, with the black node being the ball. Mexico vs. Germany, 02:26,
International Friendly, October 17, 2023.

                                                                                              (Del)
let EDel denote the edge set of the Delaunay triangulation TDel (P). The adjacency entry ai,j is set to 1 if (i, j) ∈ EDel
and 0 otherwise. The Delaunay triangulation is dual to the Voronoi tessellation commonly used for pitch control analysis
(see e.g., Rein et al., 2016; Taki and Hasegawa, 2000).
To evaluate this domain-informed construction, we compare against three general-purpose strategies. The k-nearest
neighbors (k-NN) graph connects each node to its kNN spatially closest nodes, using kNN ∈ {3, 6} in our evaluation
setting. The radius graph connects all node pairs whose Euclidean distance falls below a threshold r, equivalent to the
threshold-based sparsification used by Raabe et al. (2023). The complete graph connects every node to every other
node, making no structural assumptions but incurring the highest computational cost, while being a common choice in
prior work (see e.g., Lee et al., 2026; Wang et al., 2024). In all constructions, self-loops are added to ensure each node’s
own attributes are processed during message passing. All adjacency matrices are symmetric except for the k-NN graph.
Figure 1 illustrates the four strategies applied to the same frame.

3     Model Design
3.1   GNN Layers

Following Gilmer et al. (2017), a generic message-passing layer updates each node’s feature vector as
                                                                              
                                                     M
                                      x′i = γΘ xi ,       ϕΘ (xi , xj , ej,i ) ,
                                                        j∈N (i)
                                                    L
where γΘ and ϕΘ are differentiable functions and     is a differentiable, permutation-invariant aggregation (e.g., sum,
mean, or max), as generalized by Fey and Lenssen (2019), and N (i) denotes the neighbors of node i. The message
function ϕΘ processes adjacent node features together with the connecting edge, and the update function γΘ combines
the aggregated messages with the current node features.
Typically in GNNs, multiple message-passing layers are stacked, each receiving embeddings from its predecessor. In
graph-level tasks, the final layer’s representations are pooled through a readout layer
                                                      zG = R({x′i }),

                                                             4
                                                                                      A PREPRINT - O CTOBER 9, 2026

which outputs a single vector for the entire graph. For the overall network to be invariant to graph isomorphism, the
readout must depend only on the set of representations {x′i } and not on the node indexing (Gilmer et al., 2017). This is
realized through the same class of permutation-invariant operations used in neighborhood aggregation, ranging from
sum, mean, or max pooling to learnable attention-based pooling (Li et al., 2016).
In addition to standard layer choices, we propose a layer design adapted to match phase detection, addressing two
limitations of existing operators. First, attention-based layers such as GATConv (Brody et al., 2022; Veličković et al.,
2018) incorporate edge attributes into the attention mechanism but not into the messages themselves. In our setting,
edges encode distances, angles, and team membership — information that should directly shape the messages exchanged
between nodes. Second, raw low-dimensional spatial coordinates are subject to the spectral bias of neural networks
toward low-frequency functions (Tancik et al., 2020), limiting the model’s ability to distinguish nearby but tactically
distinct positions.
To address the first limitation, we adapt the edge-augmented graph transformer layer of Shi et al. (2021) into a Spatial
Edge-Augmented Convolution (SEAConv), a message-passing layer in which edge embeddings augment both the
attention coefficients and the messages. Compared with Shi et al. (2021), SEAConv shares the key and value projection,
treats the node’s own state as a self-loop within the attention softmax instead of a separate skip connection, and operates
on Fourier-encoded coordinates. The updated node features are computed as
                                                  K
                                              1 X        X         (k)
                                                                       
                                                                         (k)    (k)
                                                                                    
                                        x′i =                    αi,j ht,j + ẽi,j ,
                                              K
                                               k=1 j∈N (i)∪{i}
       (k)    (k)                                                                                   (k)    (k)
where hs,i = Θs xi is the projection of the receiving node, which acts as the attention query, and ht,j = Θt xj is
the projection of the sending neighbor. Augmented by the edge embedding, the latter serves as both key and value. The
                    (k)      ′                                                                         ′
edge embeddings ẽi,j ∈ Rm are the k-th head component of a learnable edge encoder γe : Rl → RKm applied to the
raw edge features ei,j .
The attention coefficients follow scaled dot-product attention (Vaswani et al., 2017):
                                                             (k)    (k)     (k)
                                                                                !
                                        (k)                 hs,i , ht,j + ẽi,j
                                      αi,j = softmaxj              √              ,
                                                                     m′
where softmaxj normalizes over N    √(i) ∪ {i}. The node’s own state enters as a self-loop (j = i) whose raw edge
features are set to ei,i = 0. The 1/ m′ scaling prevents softmax saturation as the head dimension grows. Attention
weights are regularized via dropout (Veličković et al., 2018) with probability pattn .
                                                                                                                         ′
To address the second limitation, we encode the spatial coordinates xpos
                                                                     i   ∈ R2 via random Fourier features ψ(·) ∈ R2m ,
which map positions into a high-dimensional sinusoidal basis, enabling the network to resolve fine-grained spatial
differences (Rahimi and Recht, 2007; Tancik et al., 2020):
                                      ψ(xpos              ⊤ pos          ⊤ pos
                                                                              
                                          i ) = sin(B xi ), cos(B xi ) ,
                   ′
where B ∈ R2×m is a fixed matrix with entries drawn from N (0, σ 2 ), and σ controls the frequency band. The
                                                                          ′                                    ′
remaining non-spatial node attributes xrest
                                         i   ∈ Rm−2 are projected to Rm via a separate linear layer Θr ∈ Rm ×(m−2)
                                                 pos          ′
before concatenation, yielding [Θr xrest
                                       i   ∥ ψ(xi )] ∈ R3m . As these modifications are directly targeted to enhance
the handling of spatial attributes, subsequent stacked layers use standard graph attention layers (GATConv, introduced
below), which in our implementation continue to consume the raw edge attributes but without the Fourier-based
encodings.
We compare SEAConv against three established message-passing operators: Graph Convolutions (GCNConv; Kipf
and Welling, 2017), which propagate features via the symmetrically normalized adjacency matrix; Graph Isomorphism
Networks (GINConv; Xu et al., 2019), which apply a learnable MLP after neighborhood aggregation; and Graph
Attention Networks (GATConv; Brody et al., 2022; Veličković et al., 2018), which weight neighbor contributions
through multi-head attention. Formal definitions are provided in Appendix B.

3.2   Model Architecture

Each graph is processed by a GNN block consisting of stacked message-passing layers followed by graph-level attention
pooling (Li et al., 2016). This transforms each graph into a single dg -dimensional embedding Zt = ϕg (Gt ) ∈ Rdg . We
concatenate Zt with embedded global features ϕu (ut ), where ϕu is an MLP mapping the binary global features into a
higher-dimensional representation. The resulting sequence is
                                  Hseq = (Z1 ∥ϕu (u1 ), Z2 ∥ϕu (u2 ), . . . , ZT ∥ϕu (uT )).                        (1)

                                                            5
                                                                                           A PREPRINT - O CTOBER 9, 2026

The concatenated representations are subsequently normalized using layer normalization and transformed by a learned
projection before being passed to the recurrent model. A unidirectional LSTM (Hochreiter and Schmidhuber, 1997;
see Appendix C for a short introduction) processes this sequence, producing an output state at each timestep. A final
classification layer yields predicted probabilities
                                                    P (yt = c | G≤t ),
for each timestep t and class c. The model architecture is visualized in Figure 2.

                                                                              Classification
                                                                    LSTM         Layer

                                                                              Classification
                                                                    LSTM         Layer

                                                                      ...
                            ...

                                                                              Classification
                                                                    LSTM         Layer

Figure 2: Model Architecture. Schematic structure of the model, receiving a sequence of graph representations as
input and producing class probabilities for each timestep.

3.3   Baseline Models

To isolate the contribution of graph representations, we compare against baselines operating on aggregated features.
We train four tabular baselines: multinomial logistic regression (see e.g., Hosmer et al., 2013) and XGBoost (Chen
and Guestrin, 2016) on features consisting of the per-team mean and variance of the players’ positions and velocities,
as well as the global features; a separate XGBoost model using only the global features (possession and ball status);
and an XGBoost model using pre-computed topological features derived from the point cloud of player positions. The
construction of the topological features is explained in detail in Appendix D. Since logistic regression and XGBoost
cannot model temporal dependencies, each observation is augmented with lag features from the preceding ten seconds.
The LSTM baseline shares the full model’s sequence module and classification head, training protocol (data split,
optimizer, learning-rate schedule, epochs) and seeds, and receives per-team aggregate features (centroid, positional
variance and mean speed of both teams) in place of the pooled graph embedding Zt , alongside the same global features.
All models are trained and evaluated on the same match split.

4     Empirical Results
Our goal is to correctly classify match phases per second, where correctness is judged according to the given rule-based
labels. The GNN models are implemented in Python using PyTorch (Paszke et al., 2019) and PyTorch Geometric (Fey
and Lenssen, 2019). All models minimize multiclass cross-entropy (CE) loss (see Appendix E).
Hyperparameters (Table 7) were fixed before the comparative experiments and shared across all adjacency–layer
combinations and seeds. Where established values exist, we adopted them from the literature (optimizer settings, weight
decay, GNN and attention dropout, hidden dimension, number of message-passing layers; sources in Table 7). The
remaining settings (the Fourier scale σ, the radius threshold r, the number of attention heads, the learning-rate floor, the
LSTM dropout, and the number of LSTM layers) were set manually in preliminary runs with the sole aim of stable
convergence. No systematic hyperparameter search was performed. This is deliberate, as the purpose of this study is
not to maximize predictive performance, but to compare graph constructions and message-passing operators under
identical training conditions. Additionally, its aim is to assess whether a graph-based architecture can learn tactical
phase structure from player-level tracking data. Because all configurations share the same hyperparameters and training
protocol, performance differences between them can be attributed to the design choice under study rather than to

                                                             6
                                                                                       A PREPRINT - O CTOBER 9, 2026

differential tuning effort. Tuning each configuration separately would likely raise absolute performance, but would
confound this comparison.
The data set is split 70/30 into training and validation sets by full matches to avoid data leakage. We do not hold out a
separate test set. The validation set is used only for reporting, and configuration-level results are means over all runs of
that configuration. Absolute performance figures may therefore be slightly optimistic as estimates of performance on
unseen matches. The same protocol applies to every model, so this does not systematically favor any configuration in
the relative comparisons, which are the focus of this work. All GNN results in Tables 2 and 3 are reported as means
over four seeds.
To accommodate over 5,000 observations per team and match, truncated backpropagation through time (BPTT) is
applied, with each sequence split into four equal parts. Before the actual training, the graph encoder (GNN layers,
attention pooling, and global-feature embedding) is pre-trained for 10 epochs through an auxiliary frame-wise linear
classification head, bypassing the LSTM. The main training loop then starts after this pre-training stage.
                                                                                   PC
We evaluate validation performance using accuracy, balanced accuracy BAcc = C1 c=1 TPcTP     +FNc , and macro F1 score
                                                                                               c

             1
               PC          2 TPc
F1macro = C c=1 2 TPc +FPc +FNc with C the number of classes. Note that ‘raw’ accuracy can be misleading given
the class imbalance present in our data set: ‘No Phase’ accounts for 56.3% of observations. Therefore a trivial classifier
predicting the majority class would already achieve 56.3% accuracy. Balanced accuracy and macro F1 are therefore our
primary evaluation metrics. Metrics are reported using the mean of the last 10 epochs.

4.1   Graph Representations and Message-Passing Layers

Table 2: Design Choice Results. Mean performance metrics for adjacency-construction strategies (Panel A) and
message-passing layers (Panel B), averaged over all seeds and combinations of other parameters. The best metric per
panel is in bold; relative differences are shown in parentheses. Higher values indicate better performance for all metrics
except CE loss, where lower is better.
                                  CE Loss          Accuracy       Bal. Accuracy Weighted F1            Macro F1
      Panel A: Adjacency Construction
      Delaunay                   0.249              0.901             0.773             0.898             0.788
      k-NN (kN N = 3)        0.254 (+2.0%)      0.899 (-0.2%)     0.767 (-0.8%)     0.897 (-0.2%)     0.783 (-0.6%)
      Radius                 0.258 (+3.8%)      0.899 (-0.3%)     0.767 (-0.8%)     0.896 (-0.3%)     0.783 (-0.7%)
      k-NN (kN N = 6)        0.258 (+3.7%)      0.898 (-0.3%)     0.761 (-1.5%)     0.895 (-0.3%)     0.780 (-1.0%)
      Complete              0.276 (+11.2%)      0.894 (-0.8%)     0.749 (-3.1%)     0.891 (-0.9%)     0.767 (-2.6%)
      Panel B: Message-Passing Layer
      SEAConv               0.248 (+0.0%)           0.902             0.781             0.899             0.793
      GATConv                    0.247          0.902 (-0.0%)     0.775 (-0.8%)     0.899 (-0.0%)     0.788 (-0.6%)
      GCNConv               0.258 (+4.1%)       0.897 (-0.5%)     0.762 (-2.5%)     0.894 (-0.6%)     0.778 (-2.0%)
      GINConv               0.283 (+14.4%)      0.893 (-1.0%)     0.737 (-5.7%)     0.889 (-1.1%)     0.761 (-4.1%)

We evaluate our two proposed modeling choices, Delaunay triangulation for adjacency construction and SEAConv for
message passing, against the alternatives introduced in Sections 2.2 and 3.1. We fit models for each combination of
adjacency strategy and message-passing layer with four different seeds, yielding 80 runs. To isolate the effect of each
design choice, we aggregate metrics across all combinations of the remaining parameters.
Table 2 shows the results for both design choices. Regarding the adjacency construction (Panel A), the differences
among sparse strategies are modest, but the ranking is mostly consistent across metrics. Delaunay triangulation
performs best, followed by the k-NN (kNN = 3) graph. The complete graph ranks last. To verify these rankings
statistically, we conduct pairwise Wilcoxon signed-rank tests on the Macro F1, pairing runs by the complementary
factor (message-passing layer) and seed. Full results are reported in Table 8 in the Appendix. The block-normalized
residuals in Figure 7 provide a descriptive view of robustness that is quantified by the Wilcoxon analysis. Delaunay
scores significantly higher than every alternative (Holm-adjusted p ≤ 0.0003 in all four comparisons; higher Macro F1
in at least 15/16 matched pairs in each case), with bootstrap 95% CIs on the mean paired difference excluding zero. The
only non-significant pairwise contrast is kNN = 3 vs. Radius (p = 0.50), consistent with their near-identical aggregate
metrics. The superiority of the Delaunay graph is an interesting result, as the complete graph is a common choice in
prior work (see e.g., Lee et al., 2026; Wang et al., 2024). A likely explanation for the difference in performance is
that sparser adjacency matrices prune edges between distant players that carry little information, while relationships

                                                             7
                                                                                     A PREPRINT - O CTOBER 9, 2026

between non-adjacent players can still be captured through multi-hop message passing. Delaunay graphs may exceed
other sparse adjacency matrices by apparently keeping more meaningful edges and maintaining the spatial structure
of the graph. The complete graph also incurs substantially higher computational cost: it contains roughly 4.5× more
edges than a Delaunay graph, leading to a 67% increase in training time on average in our experiments.
Having established the advantage of Delaunay adjacency, we turn our attention toward the message-passing layers (see
Panel B of Table 2). SEAConv achieves the best performance on every metric except the CE loss, where the difference
to the GATConv is marginal. The improvements are modest but consistent across all runs and adjacency strategies,
suggesting that adapting the message-passing function to the problem structure yields reliable, if incremental, gains
over standard layers. The same pairwise Wilcoxon analysis (Panel B of Table 8) confirms that SEAConv significantly
outperforms every alternative on Macro F1, including the close competitor GATConv (mean paired difference +0.0050,
95% CI [+0.0042, +0.0060], p < 10−4 Holm-adjusted, higher in 20/20 matched pairs). The margin over GATConv is
small in absolute terms, but it is statistically reliable across the full crossing of adjacency strategies and seeds.
As the Delaunay adjacency combined with SEAConv led to the best performance, we use this configuration for all
subsequent analyses and refer to it as ‘our’ model. Full results for all 80 runs are reported in Table 11 in the Appendix.

4.2   Comparison with Baselines

We now compare our GNN configuration against the baseline models to assess whether a graph-based approach justifies
its added complexity. All models are trained on the same matches and evaluated on the same validation matches.
Table 3 reports the results. The GNN outperforms every baseline on every metric. The strongest baseline is XGBoost
on the lagged standard features, which trails the GNN by only 2.4% in accuracy but by 3.7% in balanced accuracy,
4.6% in macro F1 and 28.8% in CE. The gap is thus small in accuracy but substantial in cross-entropy and on the less
frequent phases, where the class-balanced metrics diverge. The LSTM, which shares the GNN’s training protocol and
classification head, follows closely in CE (+29.7%) but falls further behind on macro F1 (-8.4%). Each of the four GNN
seeds individually outperforms both the XGBoost and the LSTM baseline on every metric. Hand-crafted interaction
features (convex-hull areas, persistence entropies) do not close it, and perform well below the standard features. This
indicates that a learned representation of player interactions captures information that neither aggregate positional
features nor hand-crafted spatial descriptors provide.

Table 3: Baseline Results. Comparison of the GNN with the baseline models across evaluated metrics on the validation
set. Percentages are relative to the GNN. The GNN metrics refer to the mean across seeds of the model using Delaunay
adjacency and SEAConv layers (see Table 11). XGBoost is abbreviated as ‘XGB’. Percentages are computed from
unrounded values.
   Model                         CE Loss        Accuracy       Bal. Accuracy      Weighted F1         Macro F1
  GNN (ours)                     0.241             0.904              0.785              0.901              0.797
  XGB – Standard            0.310 (+28.8%)     0.882 (-2.4%)      0.756 (-3.7%)      0.878 (-2.6%)      0.761 (-4.6%)
  LSTM                      0.313 (+29.7%)     0.876 (-3.0%)      0.749 (-4.6%)      0.875 (-2.9%)      0.731 (-8.4%)
  XGB – Topological         0.366 (+51.9%)     0.856 (-5.3%)     0.614 (-21.8%)      0.847 (-6.0%)     0.625 (-21.6%)
  Multinomial Logit        0.447 (+85.3%)      0.856 (-5.3%)     0.660 (-16.0%)      0.849 (-5.7%)     0.687 (-13.9%)
  XGB – Globals            0.519 (+115.3%)     0.822 (-9.0%)     0.469 (-40.2%)     0.799 (-11.3%)     0.446 (-44.0%)

4.3   Calibration

In the preceding section, we evaluated the model’s ability to discriminate between classes. We now assess the quality of
the model’s probabilistic predictions. Formal definitions are provided in Appendix F.
Figure 3 visualizes the per-class reliability diagram. For most classes, the calibration curves lie close to the diagonal,
indicating good calibration across both majority and minority classes. The ‘Low Block’ and ‘Counter Attack’ classes
are systematically overconfident in the 0.3-0.8 range.
To quantify calibration error, we use the expected calibration error (ECE), which measures the weighted average
absolute difference between observed positive fractions and mean predicted probabilities across bins (Pakdaman Naeini
et al., 2015). Table 9 reports the ECE alongside per-class CE and F1 score. Given the true class, CE is highest for the
transition phases and ‘High Block’. Consequently, the F1 score also drops for these classes. In settings with high class
imbalance, this can be expected. The overall CE hides this because frequent classes dominate it. The model achieves
low ECE across all classes.

                                                            8
                                                                                                                            A PREPRINT - O CTOBER 9, 2026

                                                              None
                                                     100%     Build Up
                                                              Low Block
                                                              Mid Block
                                                              High Block
                                                              Def. Transition
                                                     80%      Counter Attack
                                                              Overall

                               Observed Proportion
                                                     60%

                                                     40%

                                                     20%

                                                      0%
                                                        0%        20%            40%         60%           80%   100%
                                                                                Mean Predicted Probability

Figure 3: Reliability Diagram. Per-class calibration of predicted probabilities from the GNN model (all four Delaunay
/ SEAConv runs on the last epoch), with mean predicted probability plotted against empirical class frequency per
confidence bin.

5     Model Interpretability
Beyond predictive performance, we investigate whether the graph-based model captures the football-specific structure
in the tracking data. We use Integrated Gradients (IG; Sundararajan et al., 2017) to attribute predictions to inputs. For a
model F : Rn → [0, 1], input z ∈ Rn , and baseline z ′ ∈ Rn , IG computes the path integral of gradients from z ′ to z:
                                                         Z 1
                                                    ′         ∂F (z ′ + α · (z − z ′ ))
                                 IGi (z) := (zi − zi ) ·                                dα
                                                          α=0           ∂zi
                                                                                  S
                                                                                  X ∂F (z ′ + s · (z − z ′ ))               1
                                                             ≈ (zi − zi′ ) ·                            S
                                                                                                                        ·     .                       (2)
                                                                                  s=1
                                                                                                       ∂zi                  S

For our multiclass model, we apply IG separately to each class probability Fc : Rn → [0, 1], yielding per-class
                 (c)
attributions IGi (z) for c = 1, . . . , C. Attributions for class c are aggregated over all observations annotated with label
c, so that the reported values indicate the model’s use of each input while phase c is active. We apply IG in two analyses:
first to assess the contribution of graph embeddings versus global features (Section 5.1), second to identify the most
influential node features (Section 5.2).

5.1   Importance of Graph Embeddings

As the baseline LSTM already achieves reasonable performance using only information about possession, ball-in-play
indicators, and aggregated positional data (refer to Table 3), we examine whether the pooled graph embeddings ϕg (Gt )
provide additional predictive information beyond the embedded global features ϕu (ut ). We compute IG on the full
embedded sequence with z = Hseq (Equation 1) using the validation set mean embedding as baseline z ′ . All analyses
were carried out on the validation set exclusively.
Figure 4 shows that the model relies on both input types across all classes, with the graph embeddings receiving at least
36.1% of the overall attribution, while reaching higher attributions than global features in the ‘Low Block’, ‘Counter
Attack’, ‘Def. Transition’, and ‘No Phase’ phases. The global features take the larger share in ‘Build Up’, ‘Mid
Block’, and ‘High Block’. Every phase except ‘No Phase’ occurs under one dominant combination of possession and
ball-in-play state (Panel B of Table 10). Hence, ϕu (ut ) alone already separates attacking from defending phases. The
one exception is the ‘No Phase’ class: as the only phase spread across all four global states, it is also the phase for
which the graph embeddings receive their largest share (68.8%). Within a global state, by contrast, the individual phases

                                                                                          9
                                                                                                       A PREPRINT - O CTOBER 9, 2026

                              No Phase                                                                       68.8%

                             Low Block                                              52.9%

                         Counter Attack                                                54.7%

                             Mid Block              36.1%

                            High Block                       42.1%

                         Def. Transition                                             53.3%

                               Build Up                              45.6%

                                                                              50%
                                           Share of Integrated Gradients attribution to the pooled graph embeddings
                                               Pooled Graph Embeddings dominate    Global Feature Embeddings dominate

Figure 4: Importance of Embeddings. Per-class share of total Integrated Gradients importance ϕg (Gt ) + ϕu (ut )
attributed to the pooled graph embeddings ϕg (Gt ) (computed via Equation 2).

 cannot be resolved. ‘Low Block’, ‘Mid Block’, and ‘High Block’ share the same dominant state in 95.3%, 97.4% and
 98.1% of their frames, respectively. Conditioning on that state leaves the phase undetermined among them (Panel A:
‘Mid Block’ 53.1%, ‘Def. Transition’ 14.2%, ‘Low Block’ 6.6%, ‘High Block’ 3.2%). Separating these phases requires
 information about the spatial configuration. This result is consistent with Section 4.2, where the LSTM with access to
 the same global features but aggregated spatial information is surpassed by the full model. This comparison comes with
 one caveat. As IG attributions scale with the displacement z − z ′ from the baseline (Equation 2), for which we use the
validation set mean embedding, aggregating over the frames of a given phase favors whichever stream is most strongly
 displaced from its marginal mean during that phase. Therefore, Figure 4 reports relative reliance under this baseline
 rather than the unique information each stream carries.

                                                                                                                 No Phase
                                                                                                                 Build Up
                                                                                                                 Low Block
                                                                                                                 Mid Block
                                                                                                                 High Block
                                                                                                                 Def. Transition
                                                                                                                 Counter Attack

                t-SNE Dimension 2

                                       t-SNE Dimension 1
Figure 5: t-SNE Embeddings. Learned graph embeddings per class reduced to two dimensions using t-SNE. A random
25% subsample of the validation set is shown for readability.

To assess the learned representations visually, we project the 64-dimensional embeddings ϕg (Gt ) into two dimensions
using t-SNE (van der Maaten and Hinton, 2008) and visualize them in Figure 5. Classes appear well separated in this
projection, indicating that the embeddings capture phase-specific structure.

                                                                        10
                                                                                       A PREPRINT - O CTOBER 9, 2026

5.2   Relevance of Node Features

We further apply IG to quantify the importance of individual node features. To isolate their contribution, we compute IG
with z = vec(X), the flattened node-feature matrix, holding adjacency, edges, and globals fixed at their original values.
The baseline z ′ is set to the unconditional feature means across all nodes in the validation set. Per-class attributions are
computed for every validation set observation, reduced to absolute values, mean-pooled across all nodes of each graph,
and then averaged over all observations annotated with phase c to obtain a single attribution per combination of input
feature and class. For concepts represented by multiple features (e.g., team association), we use the sum as aggregation.

Table 4: Feature Importance. Relative node feature importance by class per Integrated Gradients (Equation 2).
Variables are x (X) and y (Y) coordinates, speed (S), acceleration (A), distance to opponent goal (DG), distance to ball
(DB), team association (TA; sum of three variable contributions), movement direction (MD; sin + cos), angle to goal
(GA; sin + cos), and angle to ball (BA; sin + cos).
                             X        Y        S        A       DG       DB       TA     MD       GA       BA
        No Phase           26.1%     7.7%     12.9%     3.4%     0.7%    7.0%     19.3%     8.6%     2.2%     12.2%
        Build Up           18.0%     6.7%     10.0%     6.4%     0.5%    8.0%     23.9%     7.3%     1.9%     17.4%
        Low Block          36.3%     5.1%      7.8%     5.4%     0.8%    6.5%     20.2%     6.0%     1.0%     10.8%
        Mid Block          16.9%     8.1%     11.3%     6.6%     0.6%    7.3%     24.6%     9.9%     1.2%     13.5%
        High Block         40.1%     5.4%      7.0%     4.4%     0.7%    5.0%     17.5%     8.5%     1.7%     9.6%
        Def. Transition    22.3%     6.3%     10.5%     6.5%     0.7%    7.1%     22.1%     9.6%     1.5%     13.6%
        Counter Attack     18.4%     6.3%     10.2%     6.4%     0.7%    6.8%     25.5%     9.6%     1.5%     14.5%

Table 4 reports the relative importance of each node feature by output class. Values are normalized within each class to
sum to 100%. The x-coordinate is the most important feature in four classes, with its highest attributions for ‘High
Block’ (40.1%) and ‘Low Block’ (36.3%). This aligns with the fact that horizontal position directly distinguishes
defensive phases at different pitch depths. The x-coordinate outweighs the y-coordinate in all classes, reflecting the
stronger role of horizontal positioning in phase differentiation. Team association is most important in the other three
classes (23.9–25.5%), indicating that the one-hot encoding of team membership is effectively learned. However, it
must be stated that this feature aggregates three one-hot columns, with the per-column contribution of roughly 6–9%
remaining below the x-coordinate’s in every class. Among dynamic features, angle to ball is the largest contribution
in all classes but ‘No Phase’ (9.6–17.4%), with speed (7.0–12.9%) and movement direction (6.0–9.9%) showing a
moderate contribution. Distance to goal shows a very low contribution, which can be explained through the feature not
containing much additional information beyond the x-coordinate.
Together, these analyses indicate that the model not only performs well (see Section 4) but also bases its predictions on
tactically plausible features, consistent with domain knowledge of defensive phases.

6     Discussion

The central finding of this paper is that spatial relationships between players carry predictive information for match
phase classification that tabular feature representations do not capture. Our GNN-LSTM architecture outperformed
all tabular baselines, whilst the strongest, XGBoost on the standard features, scores 4.6% lower in macro F1 and
incurs 28.8% higher cross-entropy. This suggests that the processing of the full spatial configuration of the players is
advantageous for detecting tactical patterns compared to aggregated features present in the baselines. Additionally,
the interpretability analysis reinforces this, assigning comparable importance to the graph embeddings and the global
possession state features.
Two design choices contributed to this result. Delaunay triangulation outperformed all alternative adjacency strategies,
while complete graphs ranked last with 11.2% higher cross-entropy. Removing edges between distant players appears
to reduce uninformative messages during aggregation, while multi-hop passing still allows information flow across
the pitch. The computational savings are a positive side effect: complete graphs required 67% longer training time.
Our custom SEAConv layer, which incorporates edge attributes directly into messages rather than only into attention
weights, ranked first among the message-passing operators tested. The margins over GCNConv and GINConv are
substantial (2.0% and 4.1% lower macro F1), whereas the margin over the closest competitor, GATConv, is small
in absolute terms (tied in cross-entropy, +0.005 macro F1) though statistically reliable across all runs and adjacency
strategies. Identifying which specific design elements within SEAConv drive this advantage, and whether its edge over
attention-based message passing holds on other data sets, remains an open question for future work.

                                                            11
                                                                                      A PREPRINT - O CTOBER 9, 2026

The IG analysis provides further support for the graph-based approach. Graph embeddings received at least 36.1% of
the total attribution across all classes, and held the majority share in four of seven. The global features alone cannot
separate the three block phases, which occur almost exclusively under the same global state (ball in play, opponent in
possession), so the model must draw on spatial player configurations rather than game-state indicators alone. At the
node-feature level, the x-coordinate was the most important input feature next to the team association, which makes
tactical sense: classifying defensive phases depends on where defensive lines sit along the length of the pitch. The
reliability diagram (see Figure 3) indicates that predicted class probabilities are well calibrated for all classes except
‘Low Block’.
The proposed framework offers practical relevance, as it automates phase labeling, a task currently performed manually.
As the architecture is applicable beyond the specific phase taxonomy used in this work, it can be retrained on the custom
phase definitions commonly used by professional teams, widening its applicability.
The practical value of the graph-based representation extends beyond this specific task. Because a match is encoded as
relations between individual nodes, the same representation supports the detection of tactical patterns at the individual,
group, and team level within a single framework. Previous approaches are typically tied to one of these levels or to one
specific pattern: image-based representations capture team-level structures such as the basic phases of play considered
in this study (Bauer et al., 2023), whereas the detection of dedicated patterns — for instance counter-pressing (Bauer
and Anzer, 2021) or counter attacks (Faßmeyer et al., 2021) — has so far relied on pattern-specific, hand-crafted feature
representations. Combinations of image-based and LSTM representations have been used to classify the defensive
roles of individual players at corner kicks (Bauer et al., 2022). Graph representations, providing a task-agnostic,
permutation-invariant representation of the spatio-temporal multi-agent data, have already been successfully used in
sports, e.g., to classify group-level patterns like overlapping runs (Anzer et al., 2022).
Beyond pattern detection, an efficient graph representation of match situations can serve as a shared backbone for
more sophisticated downstream models. While movement prediction with graph neural networks has already been
demonstrated (Omidshafiei et al., 2022), expected possession value (EPV) models represent a further, not yet fully
exploited potential of graph-based representations.
Our proposed approach comes with several limitations. First, performance dropped for transition classes ‘Counter
Attack’ (F1 = 0.54) and ‘Defensive Transition’ (F1 = 0.66). These phases are typically very short, so their boundaries
fall within a few seconds and a minor delay in detection costs a large share of the class (see Table 1). Using the full
25 Hz frame rate rather than aggregating to one-second graphs could enhance the model for these classes, but would
increase computational cost. Second, our labels are generated by a rule-based system rather than manual annotation,
meaning label quality depends on the fidelity of that system. Third, the data set covers only men’s football and a limited
number of competitions, and generalization to women’s football data or to a larger, more diverse set of competitions
remains untested. Fourth, no independent test set was used, and hyperparameters were not tuned per configuration. Our
results should therefore be read as a controlled comparison of design choices under a fixed training protocol rather than
as optimized performance estimates. Confirming the absolute performance on an independent set of matches, ideally
from further competitions, is left to future work.
Beyond these limitations, our findings suggest that domain-informed graph construction and edge-aware message
passing may benefit other tactical tasks operating on tracking data, motivating future work on graph-based modeling
across a wider range of spatio-temporal sports analytics.

                                                           12
                                                                                     A PREPRINT - O CTOBER 9, 2026

References
Alon, U. and Yahav, E. (2021). On the bottleneck of graph neural networks and its practical implications. In International
  Conference on Learning Representations (ICLR).
Anzer, G., Arnsmeyer, K., Bauer, P., Bekkers, J., Brefeld, U., Davis, J., Evans, N., Kempe, M., Robertson, S. J., Smith,
  J. W., and Van Haaren, J. (2025). Common data format (CDF): a standardized format for match-data in football
  (soccer). arXiv:2505.15820.
Anzer, G. and Bauer, P. (2022). Expected passes: determining the difficulty of a pass in football (soccer) using
  spatio-temporal data. Data Mining and Knowledge Discovery, 36(1):295–317.
Anzer, G., Bauer, P., Brefeld, U., and Faßmeyer, D. (2022). Detection of tactical patterns using semi-supervised graph
  neural networks. In MIT Sloan Sports Analytics Conference, pages 1–3.
Bauer, P. and Anzer, G. (2021). Data-driven detection of counterpressing in professional football: a supervised machine
  learning task based on synchronized positional and event data with expert-based feature extraction. Data Mining and
  Knowledge Discovery, 35(5):2009–2049.
Bauer, P., Anzer, G., and Shaw, L. (2023). Putting team formations in association football into context. Journal of
  Sports Analytics, 9(1):39–59.
Bauer, P., Anzer, G., and Smith, J. W. (2022). Individual role classification for players defending corners in football
  (soccer): categorisation of the defensive role for each player in a corner kick using positional data. Journal of
  Quantitative Analysis in Sports, 18(2):147–160.
Biermann, H., Memmert, D., Petersen, N., and Raabe, D. (2025). Contextualization of soccer analysis with tactical
  periodization and machine learning. Data Mining and Knowledge Discovery, 39(3):23.
Brody, S., Alon, U., and Yahav, E. (2022). How attentive are graph attention networks? In International Conference on
  Learning Representations (ICLR).
Chen, T. and Guestrin, C. (2016). XGBoost: a scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD
  International Conference on Knowledge Discovery and Data Mining, pages 785–794. ACM.
Chintakunta, H., Gentimis, T., Gonzalez-Diaz, R., Jimenez, M.-J., and Krim, H. (2015). An entropy-based persistence
  barcode. Pattern Recognition, 48(2):391–401.
Delaunay, B. (1934). Sur la sphère vide. Bulletin de l’Académie des Sciences de l’URSS. VII. Série, (6):793–800.
Dwivedi, V. P., Joshi, C. K., Luu, A. T., Laurent, T., Bengio, Y., and Bresson, X. (2023). Benchmarking graph neural
  networks. Journal of Machine Learning Research, 24(43):1–48.
Edelsbrunner, H. and Harer, J. (2010). Computational topology: an introduction. American Mathematical Society,
  Providence, RI.
Faßmeyer, D., Anzer, G., Bauer, P., and Brefeld, U. (2021). Toward automatically labeling situations in soccer. Frontiers
  in Sports and Active Living, 3:725431.
Fey, M. and Lenssen, J. E. (2019). Fast graph representation learning with PyTorch Geometric. In ICLR Workshop on
  Representation Learning on Graphs and Manifolds.
Gilmer, J., Schoenholz, S. S., Riley, P. F., Vinyals, O., and Dahl, G. E. (2017). Neural message passing for quantum
  chemistry. In Proceedings of the 34th International Conference on Machine Learning (ICML), volume 70 of
  Proceedings of Machine Learning Research, pages 1263–1272. PMLR.
Goes, F. R., Meerhoff, L. A., Bueno, M. J. O., Rodrigues, D. M., Moura, F. A., Brink, M. S., Elferink-Gemser, M. T.,
  Knobbe, A. J., Cunha, S. A., Torres, R. S., and Lemmink, K. A. P. M. (2021). Unlocking the potential of big data to
  support tactical performance analysis in professional soccer: a systematic review. European Journal of Sport Science,
  21(4):481–496.
Hamilton, W. L. (2020). Graph representation learning. Number 46 in Synthesis Lectures on Artificial Intelligence and
  Machine Learning. Morgan & Claypool, San Rafael, CA.
Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8):1735–1780.
Hosmer, D. W., Lemeshow, S., and Sturdivant, R. X. (2013). Applied logistic regression. Wiley Series in Probability
  and Statistics. Wiley, Hoboken, NJ, 3rd edition.
Kingma, D. P. and Ba, J. (2015). Adam: a method for stochastic optimization. In International Conference on Learning
  Representations (ICLR).
Kipf, T. N. and Welling, M. (2017). Semi-supervised classification with graph convolutional networks. In International
  Conference on Learning Representations (ICLR).

                                                           13
                                                                                     A PREPRINT - O CTOBER 9, 2026

Lee, M., Jo, G., Hong, M., Bauer, P., and Ko, S.-K. (2025). exPress: contextual valuation of individual players within
   pressing situations in soccer. In MIT Sloan Sports Analytics Conference, pages 1–16.
Lee, M., Jo, G., Hong, M., Bauer, P., and Ko, S.-K. (2026). Contextual evaluation of individual contributions from
   pressing situations in football. In Machine Learning and Data Mining for Sports Analytics: 12th International
  Workshop, MLSA 2025, volume 2833 of Communications in Computer and Information Science, pages 35–47.
   Springer.
Li, Q., Han, Z., and Wu, X.-M. (2018). Deeper insights into graph convolutional networks for semi-supervised learning.
   In Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence, volume 32, pages 3538–3545. AAAI
   Press.
Li, Y., Tarlow, D., Brockschmidt, M., and Zemel, R. (2016). Gated graph sequence neural networks. In International
  Conference on Learning Representations (ICLR).
Linke, D., Link, D., and Lames, M. (2018). Validation of electronic performance and tracking systems EPTS under
   field conditions. PLOS ONE, 13(7):e0199519.
Linke, D., Link, D., and Lames, M. (2020). Football-specific validity of TRACAB’s optical video tracking systems.
  PLOS ONE, 15(3):e0230179.
Loshchilov, I. and Hutter, F. (2017). SGDR: stochastic gradient descent with warm restarts. In International Conference
   on Learning Representations (ICLR).
Loshchilov, I. and Hutter, F. (2019). Decoupled weight decay regularization. In International Conference on Learning
  Representations (ICLR).
Moura, F. A., Martins, L. E. B., Anido, R. O., Ruffino, P. R. C., Barros, R. M. L., and Cunha, S. A. (2013). A spectral
   analysis of team dynamics and tactics in Brazilian football. Journal of Sports Sciences, 31(14):1568–1577.
Ochin, J., Devineau, G., Stanciulescu, B., and Manitsaris, S. (2025). Game state and spatio-temporal action detection
   in soccer using graph neural networks and 3D convolutional networks. In Proceedings of the 14th International
  Conference on Pattern Recognition Applications and Methods (ICPRAM), volume 1, pages 636–646. SciTePress.
Omidshafiei, S., Hennes, D., Garnelo, M., Wang, Z., Recasens, A., Tarassov, E., Yang, Y., Elie, R., Connor, J. T., Muller,
   P., Mackraz, N., Cao, K., Moreno, P., Sprechmann, P., Hassabis, D., Graham, I., Spearman, W., Heess, N., and Tuyls,
   K. (2022). Multiagent off-screen behavior prediction in football. Scientific Reports, 12(1):8638.
Pakdaman Naeini, M., Cooper, G., and Hauskrecht, M. (2015). Obtaining well calibrated probabilities using Bayesian
   binning. In Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence, volume 29, pages 2901–2907.
  AAAI Press.
Pascanu, R., Mikolov, T., and Bengio, Y. (2013). On the difficulty of training recurrent neural networks. In Proceedings
   of the 30th International Conference on Machine Learning (ICML), volume 28 of Proceedings of Machine Learning
  Research, pages 1310–1318. PMLR.
Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L.,
   Desmaison, A., Köpf, A., Yang, E., DeVito, Z., Raison, M., Tejani, A., Chilamkurthy, S., Steiner, B., Fang, L., Bai,
  J., and Chintala, S. (2019). PyTorch: an imperative style, high-performance deep learning library. In Advances in
  Neural Information Processing Systems (NeurIPS), volume 32, pages 8024–8035. Curran Associates, Inc.
Preparata, F. P. and Shamos, M. I. (1985). Computational geometry: an introduction. Texts and Monographs in
   Computer Science. Springer, New York.
Raabe, D., Nabben, R., and Memmert, D. (2023). Graph representations for the analysis of multi-agent spatiotemporal
   sports data. Applied Intelligence, 53(4):3783–3803.
Rahimi, A. and Recht, B. (2007). Random features for large-scale kernel machines. In Advances in Neural Information
  Processing Systems (NeurIPS), volume 20, pages 1177–1184. Curran Associates, Inc.
Rein, R. and Memmert, D. (2016). Big data and tactical analysis in elite soccer: future challenges and opportunities for
   sports science. SpringerPlus, 5(1):1410.
Rein, R., Raabe, D., Perl, J., and Memmert, D. (2016). Evaluation of changes in space control due to passing behavior
   in elite soccer using Voronoi-cells. In Proceedings of the 10th International Symposium on Computer Science in
  Sports (ISCSS), volume 392 of Advances in Intelligent Systems and Computing, pages 179–183. Springer.
Ric, A., Bradley, P., Shaw, L., Thies, H., Sumpter, D., Lopez-Felip, M. A., and Bauer, P. (2021). Football analytics
  2021: the role of context in transferring analytics to the pitch. Barça Innovation Hub, Barcelona.
Rittig, J. G., Gao, Q., Dahmen, M., Mitsos, A., and Schweidtmann, A. M. (2023). Graph neural networks for the
   prediction of molecular structure–property relationships. In Zhang, D. and Del Río Chanona, E. A., editors, Machine
  Learning and Hybrid Modelling for Reaction Engineering, pages 159–181. Royal Society of Chemistry, Cambridge.

                                                           14
                                                                                      A PREPRINT - O CTOBER 9, 2026

Rothe, F., Van Roy, M., Pinheiro, G., Davis, J., and Lames, M. (2026). Automatic detection of tactical states in football
  based on player and ball position. Journal of Sports Analytics. Advance online publication.
Shaw, L. and Glickman, M. (2019). Dynamic analysis of team strategy in professional football. In Barça Sports
  Analytics Summit, pages 1–13.
Shi, Y., Huang, Z., Feng, S., Zhong, H., Wang, W., and Sun, Y. (2021). Masked label prediction: unified message passing
  model for semi-supervised classification. In Proceedings of the Thirtieth International Joint Conference on Artificial
  Intelligence (IJCAI), pages 1548–1554. International Joint Conferences on Artificial Intelligence Organization.
Stöckl, M., Seidl, T., Marley, D., and Power, P. (2021). Making offensive play predictable – using a graph convolutional
  network to understand defensive performance in soccer. In MIT Sloan Sports Analytics Conference, pages 1–19.
Sun, C., Karlsson, P., Wu, J., Tenenbaum, J. B., and Murphy, K. (2019). Stochastic prediction of multi-agent interactions
  from partial observations. In International Conference on Learning Representations (ICLR).
Sundararajan, M., Taly, A., and Yan, Q. (2017). Axiomatic attribution for deep networks. In Proceedings of the 34th
  International Conference on Machine Learning (ICML), volume 70 of Proceedings of Machine Learning Research,
  pages 3319–3328. PMLR.
Sutskever, I., Martens, J., Dahl, G., and Hinton, G. (2013). On the importance of initialization and momentum in
  deep learning. In Proceedings of the 30th International Conference on Machine Learning (ICML), volume 28 of
  Proceedings of Machine Learning Research, pages 1139–1147. PMLR.
Taki, T. and Hasegawa, J. (2000). Visualization of dominant region in team games and its application to teamwork
  analysis. In Proceedings of Computer Graphics International 2000, pages 227–235. IEEE.
Tancik, M., Srinivasan, P. P., Mildenhall, B., Fridovich-Keil, S., Raghavan, N., Singhal, U., Ramamoorthi, R., Barron,
  J. T., and Ng, R. (2020). Fourier features let networks learn high frequency functions in low dimensional domains. In
  Advances in Neural Information Processing Systems (NeurIPS), volume 33, pages 7537–7547. Curran Associates,
  Inc.
Tauzin, G., Lupo, U., Tunstall, L., Burella Pérez, J., Caorsi, M., Medina-Mardones, A. M., Dassatti, A., and Hess, K.
  (2021). giotto-tda: a topological data analysis toolkit for machine learning and data exploration. Journal of Machine
  Learning Research, 22(39):1–6.
Topping, J., Di Giovanni, F., Chamberlain, B. P., Dong, X., and Bronstein, M. M. (2022). Understanding over-squashing
  and bottlenecks on graphs via curvature. In International Conference on Learning Representations (ICLR).
van der Maaten, L. and Hinton, G. (2008). Visualizing data using t-SNE. Journal of Machine Learning Research,
  9(86):2579–2605.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017).
  Attention is all you need. In Advances in Neural Information Processing Systems (NeurIPS), volume 30, pages
  5998–6008. Curran Associates, Inc.
Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., and Bengio, Y. (2018). Graph attention networks. In
  International Conference on Learning Representations (ICLR).
Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P.,
  Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N., Nelson, A. R. J.,
  Jones, E., Kern, R., Larson, E., Carey, C. J., Polat, İ., Feng, Y., Moore, E. W., VanderPlas, J., Laxalde, D., Perktold,
  J., Cimrman, R., Henriksen, I., Quintero, E. A., Harris, C. R., Archibald, A. M., Ribeiro, A. H., Pedregosa, F., van
  Mulbregt, P., and SciPy 1.0 Contributors (2020). SciPy 1.0: fundamental algorithms for scientific computing in
  Python. Nature Methods, 17(3):261–272.
Wang, Y., Li, Z., and Barati Farimani, A. (2023). Graph neural networks for molecules. In Qu, C. and Liu, H., editors,
  Machine Learning in Molecular Sciences, volume 36 of Challenges and Advances in Computational Chemistry and
  Physics, pages 21–66. Springer, Cham.
Wang, Z., Veličković, P., Hennes, D., Tomašev, N., Prince, L., Kaisers, M., Bachrach, Y., Elie, R., Wenliang,
  L. K., Piccinini, F., Spearman, W., Graham, I., Connor, J., Yang, Y., Recasens, A., Khan, M., Beauguerlange,
  N., Sprechmann, P., Moreno, P., Heess, N., Bowling, M., Hassabis, D., and Tuyls, K. (2024). TacticAI: an AI assistant
  for football tactics. Nature Communications, 15(1):1906.
Xenopoulos, P. and Silva, C. (2021). Graph neural networks to predict sports outcomes. In 2021 IEEE International
  Conference on Big Data (Big Data), pages 1757–1763. IEEE.
Xu, K., Hu, W., Leskovec, J., and Jegelka, S. (2019). How powerful are graph neural networks? In International
  Conference on Learning Representations (ICLR).
Yeh, R. A., Schwing, A. G., Huang, J., and Murphy, K. (2019). Diverse generation for multi-agent sports games. In
  2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 4605–4614. IEEE.

                                                           15
                                                                                        A PREPRINT - O CTOBER 9, 2026

Appendix

A     Definition of Play Phases
This appendix formalizes the rule-based labels of the six phases of play reported in this work — ‘Build Up’, ‘Low
Block’, ‘Mid Block’, ‘High Block’, ‘Counter Attack’, ‘Defensive Transition’ — and extends the five-phase scheme
of Bauer et al. (2023). A phase is kept alive until the ball goes dead. Distances are given in meters, speeds in km/h,
and durations in seconds or milliseconds. The pitch is partitioned into an own third, a middle third, and a final third,
referenced from the perspective of the team the phase describes, with the final third adjacent to the opponent’s goal.

A.1   General Concepts

Stationary A player is considered stationary if it is not moving forward or backward at more than 10 km/h, where
forward and backward movement are defined by two opposing 60◦ cones aligned with the goal-to-goal axis.

Organized A team is considered organized if its units approximately form horizontal lines. Excluding the most
advanced player, the remaining defenders are grouped into three units; letting a, b, and c denote the vertical band width
of these units from rear to front, the organization score is (4a + 4b + c)/9, and the team is organized if this score is
below 250.

A.2   Build Up

‘Build Up’ is an in-possession phase that requires at least 8 defenders behind the ball, independent of the third in which
 the ball is located. A build up is classified as opposed if the defending team is pressing and the closest defender is
within 12 m of the ball, or at least two defenders are within 6 m of the ball, or at least one player is within 4 m of the
 ball. The phase is kept alive until its criteria are not fulfilled for 500 ms within a 2.5 s window.

A.3   Low Block

‘Low Block’ is an out-of-possession phase that requires the defending team to be stationary and organized. The team
has been stationary for at least 1.6 s during the previous 2 s; at least 4 defenders are behind the ball and organized, or at
least 4 defenders are in the own box; at least 5 defenders are in the own third; and at least 8 defenders are in the middle
or own third. The phase is kept alive until its criteria are not fulfilled for 400 ms within a 2 s window.

A.4   Mid Block

The team has been stationary for at least 1.6 s during the previous 2 s; at least 4 defenders are behind the ball and
organized, or at least 4 defenders are in the own box; no low block applies; and at least 8 defenders are in the middle or
own third. The phase is kept alive until its criteria are not fulfilled for 400 ms within a 2 s window.

A.5   High Block

The team has been stationary for at least 1.6 s during the previous 2 s; at least 4 defenders are behind the ball and
organized; no mid or low block applies; at least 3 defenders are in the final third; at least 8 defenders are in the middle
or final third; and possession changed more than 500 ms ago. The phase is kept alive until its criteria are not fulfilled for
400 ms within a 2 s window.

A.6   Counter Attack

‘Counter Attack’ is an in-possession transition phase. The ball is moved forward; possession changed within the
previous 3.5 s (this timer is not increased while the phase is a counter attack); at least 5 defenders recover; the ball
speed exceeds 20 km/h; and no defender is closer to the ball than an attacker. The phase is kept alive until its criteria are
not fulfilled for 400 ms within a 1.5 s window.

A.7   Defensive Transition

A transition follows a change of possession and is assigned to both teams: it is labeled an attacking transition for
the team gaining possession and a defensive transition for the team losing it. The defensive transition requires that

                                                             16
                                                                                           A PREPRINT - O CTOBER 9, 2026

possession changed within the previous 5 s, that the ball is not yet under control, and that no other in-possession phase
applies. The ball is considered under control if the distance to the closest attacker is less than 2.5 m, the distance to the
closest defender is more than 4 m, and these conditions hold for 15 consecutive frames. The phase is kept alive until its
criteria are not fulfilled within 5 s; a defensive transition is additionally kept alive during a simultaneous counter-press
until the end of that counter-press.

B    Baseline GNN Layers
Graph Convolutions (GCNConv) The graph convolutional operator (Kipf and Welling, 2017) is based on the
symmetrically normalized adjacency matrix with self-loops. Let Â = A + I denote the adjacency matrix with added
self-loops, and let dˆi = j Âi,j denote the degree of node i including the self-loop. The GCN update rule can then be
                         P
written as
                                                                   Â
                                                                  q j,i xj ,
                                                         X
                                            x′i = Θ⊤
                                                      j∈N (i)∪{i}   dˆj dˆi
where Θ is a trainable weight matrix.
GCNConv operates on a scalar-weighted adjacency matrix and, unlike SEAConv and GATConv, cannot incorporate the
edge attribute vector ei,j . In our experiments we therefore use the unweighted adjacency, i.e., Âi,j = 1 for (i, j) ∈ E
and Âi,i = 1 for the added self-loops; the edge attributes are not used by this layer. The same holds for GINConv (see
below), which aggregates neighbor features without edge information.

Graph Isomorphism Network (GINConv) Introduced by Xu et al. (2019), message-passing within the graph
isomorphism operator is written as
                                                                                    
                                                                          X
                                          x′i = hΘ (1 + ϵ) · xi +                xj  ,
                                                                        j∈N (i)

where hΘ is a learnable multilayer perceptron (MLP) and ϵ a learnable parameter or a fixed scalar.

Graph Attention (GATConv) Veličković et al. (2018) brought the concept of multi-head attention to GNNs (see
Vaswani et al., 2017, for an introduction to the attention mechanism). We employ the GATv2 variant of Brody et al.
(2022), which reorders the attention computation such that the attention vector is applied after the non-linearity, making
the attention dynamic, i.e., conditional on the receiving node. The updated node features x′i are calculated as
                                                     K
                                                   1 X      X            (k)   (k)
                                           x′i =                        αi,j Θt xj ,
                                                   K
                                                    k=1 j∈N (i)∪{i}

        (k)
where Θt is a learnable weight matrix transforming the message-sending node, unique per attention head k; the node’s
own contribution enters the sum as a self-loop (j = i). The attention coefficients α are computed as
                                                                                        
                                                              (k)       (k)        (k)
                                  exp a(k)⊤ LeakyReLU Θs xi + Θt xj + Θe ei,j
                    (k)
                  αi,j = P                                                                      ,
                                          exp   a(k)⊤ LeakyReLU Θ(k) x + Θ(k) x + Θ(k) e
                              l∈N (i)∪{i}                            s   i     t    l     e  i,l

                                                                  (k)
where a(k) is a learnable weight vector unique per head, Θs projects the receiving node, ei,j are edge attributes
                               (k)
between nodes i and j, and Θe is a learnable weight matrix that projects the edge attributes into the attention space.
Note that the edge attributes modulate the attention weights but do not alter the messages themselves.

C    Long Short-Term Memory Networks
A long short-term memory (LSTM) is a special type of Recurrent Neural Network (RNN), first introduced by Hochreiter
and Schmidhuber (1997). RNNs are a subclass of neural networks designed to handle sequential data like text or time
series. In contrast to feed-forward neural networks, they connect a neuron’s output to the next input to account for the
structural dependence of the data. As the unfolding of these networks leads to very deep structures, they typically suffer

                                                             17
                                                                                           A PREPRINT - O CTOBER 9, 2026

from the ‘vanishing gradient problem’, which limits the learning ability of deep networks due to the vanishing of the
weights’ gradients through an increasing number of layers. LSTMs were designed to mitigate this issue, as gradients
can flow through the network without being reduced too much.
For this purpose, LSTM cells possess a state as well as three gates — an input, output, and forget gate. Figure 6
visualizes such an LSTM cell. The cell state ct is updated in each cell based on the output of each of the three gates. As
these gates are a single sigmoid layer, they essentially output how much information is added to the cell state, based on
the previous state as well as this cell’s input. The forget gate ft has the previous output ht−1 and the current input xt as
input and decides how much information is kept or otherwise forgotten. Additionally, the input gate it determines how
much of the input xt is used based on ht−1 , and multiplies this with the new candidate c̃t that is based on a tanh layer.
The new cell state is then calculated as ct = ft · ct−1 + it · c̃t . Finally, the output gate ot is responsible for how much
of this cell state is kept as the cell’s output ht .

                                                x                   +

                                                                    x         tanh

                                                                  tanh

                                                                                x

Figure 6: LSTM cell. Schematic visualization of an LSTM cell with input gate it , forget gate ft , and output gate ot
that use the previous cell state ct−1 and output ht−1 to update the cell state ct and output a new value ht .

D    Topological Features for the Baseline Model
In order to describe the spatial arrangement of players, topological features are derived from the player positions data
for each second of observed match time. First, the convex hull of the observed team is computed as

                                                    1    X
                                        Ateam =                   (xi yi+1 − xi+1 yi ) ,
                                                    2
                                                        i∈Vteam

where Vteam denotes the ordered vertices of the convex hull of the observed team’s positions, with Aopp equivalently
computed for the opponent. xi and yi are the x and y-coordinate of node i (Preparata and Shamos, 1985). The area ratio
Aratio = Ateam /Aopp is used as a measure of relative spatial dominance. Moura et al. (2013) used similar features to
describe team dynamics and tactics in football.
Additional topological features are computed via persistent homology. Concretely, we apply a Vietoris-Rips filtration
(Edelsbrunner and Harer, 2010) to the combined 22-player spatial features xpos ∈ R22×2 , obtaining persistence diagrams
dgmk for k ∈ {0, 1}. From these, the persistence entropy is derived (Chintakunta et al., 2015) as
                                                         X ℓi       
                                                                    ℓi
                                                Ek = −         log       ,
                                                          i
                                                             L      L
                                                               P
where ℓi = di − bi is the lifetime of the i-th feature and L = i ℓi . E0 captures the entropy of connected-component
merging (clustering structure), while E1 captures the entropy of loops (encirclement/spatial holes between formations).
The convex hulls are computed using the SciPy package (Virtanen et al., 2020), and the persistence diagrams and
entropy are obtained using the Giotto-TDA package (Tauzin et al., 2021).

E    Cross-Entropy Loss
The cross-entropy loss quantifies the divergence between a predicted probability distribution and the true class label,
increasing as predictions diverge from the observed outcome. For binary classification with true label y ∈ {0, 1} and

                                                              18
                                                                                                                        A PREPRINT - O CTOBER 9, 2026

predicted probability ŷ ∈ [0, 1], the per-observation loss is defined as
                                                                                                                      
                                                                      L(y, ŷ) = − y · log(ŷ) + (1 − y) · log(1 − ŷ) .
For multiclass classification with C > 2 classes, let yc ∈ {0, 1} denote the one-hot indicator that the observation belongs
                                                                                       PC
to class c, and let ŷc ∈ [0, 1] denote the corresponding predicted probability, with c=1 ŷc = 1. The per-observation
loss generalizes to
                                                             C
                                                             X
                                                L(y, ŷ) = −    yc · log(ŷc ).
                                                                                               c=1
The negative sign ensures non-negativity, since log(ŷc ) ≤ 0 for ŷc ∈ (0, 1]. The reported CE values in Section 4
correspond to the mean of L over all observations in the validation set.

F                                    Calibration Definitions
A perfectly calibrated model predicts correct event probabilities. In the binary case, let Y ∈ {0, 1} denote the outcome
and let P̂ ∈ [0, 1] be the model’s predicted probability for Y = 1; perfect calibration requires P(Y = 1 | P̂ = p) = p
for all p ∈ [0, 1]. As match phase prediction is a multiclass setting, this definition does not apply to the joint probability
vector. Instead, marginal calibration is assessed by considering each class in a one-vs-rest view. Since P(Y = 1 | P̂ = p)
is unknown, we estimate it by binning class predictions into M bins and, in each bin, comparing the observed fraction
of positives to the mean predicted probability. This visualization is known as a reliability diagram.
The expected calibration error (ECE) is defined as
                                                                                         M
                                                                                         X |Bm |
                                                                                ECE =                |om − bm |,                                           (3)
                                                                                         m=1
                                                                                                n

with Bm denoting bin m, n the total number of observations in the validation set. Each sample enters every class’s
one-vs-rest problem. om is the observed fraction of positives in bin m, and bm the mean predicted probability in bin m.
The ECE is weighted by all observations, so for rare classes it is dominated by the many near-zero predictions and can’t
be compared across classes.

G                                    Figures

                                                                  Adjacency                                                    Layer
                                            Layer                                                      Adjacency
                                    0.02     GCNConv                                                      Complete
                                             GINConv                                                      k-NN (6)
                                             GATConv                                                      Radius
                                             SEAConv                                                      k-NN (3)
Macro F1 mean(Macro F1 | control)

                                    0.01                                                                  Delaunay

                                    0.00

                                    0.01

                                    0.02

                                    0.03

                                    0.04
                                           Complete    k-NN (6)    Radius     k-NN (3)   Delaunay        GCNConv     GINConv           GATConv   SEAConv

Figure 7: Block-normalized residual validation macro F1. Left: effect of adjacency after removing mean layer
effects. Right: effect of layer after removing mean adjacency effects. Boxplots show residual distributions; colored
points denote the control setting. Higher values indicate better performance.

                                                                                               19
                                                                                         A PREPRINT - O CTOBER 9, 2026

H   Tables

         Table 5: Competitions and Seasons. Number of matches in the data set by competition and season.
                                                             Season
              Competition              19/20 20/21 21/22 22/23 23/24 24/25                    Total
                DFB-Pokal                  3        0         35      53          59         29          179
                Senior national team       0        0          0       3          11          4           18
                Under-21 national team     0        1          0       3           2          0            6
                Total                      3        1         35      59          72         33          203

Table 6: Variables. List of all variables contained in the data set with detailed explanations and processing methods.
 Variable                Abbreviation Explanation                                  Details
 X-coordinate             X               Spatial horizontal coordinate of             Standardized to 0–1 based on pitch
                                          player / ball                                dimensions
 Y-coordinate             Y               Spatial vertical coordinate of player        Standardized to 0.176–0.824 to
                                          / ball                                       match the x-coordinate in aspect ra-
                                                                                       tio for a 105 m × 68 m pitch
 Speed                    S               Movement speed of player / ball in           Standardized based on a maximum
                                          m/s                                          value of 10 m s−1
 Acceleration             A               Change in player speed in m s−2              Standardized based on a maximum
                                                                                       value of 7 m s−2
 Distance to Goal         DG              Distance to opponent goal                    Computed from standardized coor-
                                                                                       dinates
 Distance to Ball         DB              Distance to the ball position                Computed from standardized coor-
                                                                                       dinates
 Team Association         TA              One-hot encoding of team associa-            Three columns indicating if the
                                          tion                                         node is part of the observed team,
                                                                                       opponent team, or the ball
 Movement Direction       MD              X and Y deviation of player coordi-          Modeled using sine and cosine com-
                                          nates                                        ponents
 Angle to Goal            GA              Angle to opponent goal                       Modeled using sine and cosine
 Angle to Ball            BA              Angle to the ball position                   Modeled using sine and cosine

                                                         20
                                                                                 A PREPRINT - O CTOBER 9, 2026

Table 7: Hyperparameters. Detailed collection of all hyperparameters used for model training. The column ‘Selection’
contains the selection process and reasoning for the parameter value with references if the parameter is standard or
common.
 Hyperparameter                   Value                               Selection
 Train/validation split           70/30 (by matches)                  -
 Loss function                    Cross-entropy                       -
 Epochs                           100 (+ 10 GNN pre-training)         Computational constraints
 Truncated BPTT                   4 chunks per match                  Computational constraints
 Gradient clipping                max-norm 1.0                        Common for RNNs (Pascanu et al., 2013)
 r for radius graph               0.2 (≈ 20 m in physical units)      Manual
 Optimizer (graph encoder)        SGD (momentum 0.9)                  Standard (Sutskever et al., 2013)
 Learning rate (graph encoder)    0.01                                Common
 Optimizer (LSTM & head)          AdamW                               Standard (Kingma and Ba, 2015; Loshchilov
                                                                      and Hutter, 2019)
 Learning rate (LSTM & head)      0.001                               Standard (Kingma and Ba, 2015; Loshchilov
                                                                      and Hutter, 2017)
 Weight decay (both)              5 × 10−4                            Standard in GNN literature (Kipf and
                                                                      Welling, 2017; Veličković et al., 2018)
 LR schedule (both)               Cosine annealing to 3 × 10−6        Standard technique (Loshchilov and Hutter,
                                                                      2017), final value manually chosen
 Message-passing layers           3                                   Common, deeper GNNs oversmooth (Li
                                                                      et al., 2018)
 Normalization (GNN)              PairNorm + SiLU after each layer    Design choice
 Dropout (GNN layers)             0.1                                 Standard (Vaswani et al., 2017)
 Dropout (LSTM)                   0.3                                 Manual
 Attention heads                  4                                   Manual
 Attention dropout                0.1                                 Standard (Vaswani et al., 2017)
 Fourier σ                        2π                                  Manual
 Hidden dimension (GNN)           64                                  Common (e.g. Dwivedi et al., 2023)
 LSTM layers                      1                                   Manual
 Hidden dimension (LSTM)          64                                  Set in accordance with GNN

                                                        21
                                                                                    A PREPRINT - O CTOBER 9, 2026

Table 8: Pairwise Wilcoxon Signed-Rank Tests. All pairwise comparisons of adjacency construction strategies
(Panel A) and message-passing layers (Panel B) by Macro F1. Observations are paired by the complementary factor and
seed (n = 16 and n = 20 matched pairs, respectively). ∆ = Macro F1(Method A) − Macro F1(Method B); positive
values favor Method A. 95% CI is a percentile bootstrap confidence interval on the mean paired difference. p-values are
two-sided and Holm–Bonferroni corrected within each panel. Consistent denotes the fraction of matched pairs where
the sign of ∆ of the individual pair is consistent with that of the mean.
                                                                            Macro F1
            Method A             Method B                 ∆             95% CI         p (Holm)       Cons.
           Panel A: Adjacency Construction (n = 16)
           Delaunay             Complete            +0.0206     [+0.0137, +0.0281]       0.0003      16/16
           k-NN (kN N = 3)      Complete            +0.0158     [+0.0096, +0.0227]       0.0003      16/16
           Radius               Complete            +0.0154     [+0.0091, +0.0222]       0.0003      16/16
           k-NN (kN N = 6)      Complete            +0.0125     [+0.0077, +0.0180]       0.0003      16/16
           Delaunay             k-NN (kN N = 6)     +0.0081     [+0.0058, +0.0104]       0.0003      16/16
           Delaunay             Radius              +0.0052     [+0.0040, +0.0062]       0.0003      15/16
           Delaunay             k-NN (kN N = 3)     +0.0048     [+0.0036, +0.0059]       0.0003      16/16
           k-NN (kN N = 3)      k-NN (kN N = 6)     +0.0033     [+0.0015, +0.0052]       0.0125      13/16
           Radius               k-NN (kN N = 6)     +0.0029     [+0.0009, +0.0049]       0.0365      12/16
           k-NN (kN N = 3)      Radius              +0.0004     [-0.0007, +0.0015]       0.4954       9/16
           Panel B: Message-Passing Layer (n = 20)
           SEAConv              GINConv             +0.0325     [+0.0271, +0.0386]     1.1 × 10−5    20/20
           GATConv              GINConv             +0.0275     [+0.0222, +0.0338]     1.1 × 10−5    20/20
           GCNConv              GINConv             +0.0167     [+0.0130, +0.0211]     1.1 × 10−5    20/20
           SEAConv              GCNConv             +0.0158     [+0.0137, +0.0180]     1.1 × 10−5    20/20
           GATConv              GCNConv             +0.0108     [+0.0088, +0.0129]     1.1 × 10−5    20/20
           SEAConv              GATConv             +0.0050     [+0.0042, +0.0060]     1.1 × 10−5    20/20

Table 9: Class-wise Evaluation Metrics. Per-class metrics of the GNN’s predictions on the validation set, averaged
over the four seeds of the model using Delaunay adjacency and SEAConv layers, each
                                                                                P evaluated at its final checkpoint
(epoch 100). CE is the cross-entropy conditional on the true class, CEc = − n1c i: yi =c log ŷi,c . ECE (Equation 3,
10 equal-width bins) and F1 are computed one-vs-rest, taking the class with the highest predicted probability as the
prediction for F1.
                         Class                  Class Size      CE Loss      ECE       F1
                        No Phase                 56.3%              0.153     0.0061    0.936
                        Build Up                 16.2%              0.204     0.0051    0.912
                        Low Block                2.1%               0.422     0.0018    0.811
                        Mid Block                16.4%              0.147     0.0015    0.932
                        High Block               1.0%               0.591     0.0006    0.795
                        Defensive Transition     5.2%               0.846     0.0012    0.659
                        Counter Attack           2.9%               1.371     0.0041    0.535

                                                          22
                                                                                     A PREPRINT - O CTOBER 9, 2026

Table 10: Global State and Match Phase. Empirical conditional distributions of global state ut (ball in play, own team
in possession) and the annotated phase, over the 689,570 validation observations used in the attribution analysis. Phases
are No Phase, Build Up (BU), Low Block (LB), Mid Block (MB), High Block (HB), Defensive Transition (DT) and
Counter Attack (CA).
                                  Panel A: phase distribution given the global state
          Global state            No Phase         BU      LB       MB       HB       DT        CA           n
          In play, own poss.           36.1%    52.8%     0.0%     0.0%     0.0%     2.3%     8.8%       204,378
          In play, opp. poss.          21.9%     0.3%     6.6%    53.1%     3.2%    14.2%     0.6%       206,939
          Dead ball, own poss.         99.1%     0.7%     0.0%     0.0%     0.0%     0.0%     0.2%       133,602
          Dead ball, opp. poss.        94.4%     1.4%     0.5%     2.1%     0.1%     1.1%     0.5%       144,651

                                    Panel B: global-state distribution given the phase
                                             Ball in play                 Dead ball
                  Phase               Own poss.     Opp. poss.    Own poss.    Opp. poss.            n
                  No Phase                19.0%         11.7%         34.1%         35.2%    388,192
                  Build Up                96.9%          0.5%          0.8%          1.8%    111,453
                  Low Block                0.0%         95.3%          0.0%          4.7%     14,391
                  Mid Block                0.0%         97.4%          0.0%          2.6%    112,936
                  High Block               0.0%         98.1%          0.0%          1.9%      6,745
                  Def. Transition         13.2%         82.2%          0.1%          4.5%     35,783
                  Counter Attack          89.2%          6.2%          1.1%          3.5%     20,070

                                                           23
                                                                                  A PREPRINT - O CTOBER 9, 2026

Table 11: Full Results. Detailed results and validation metrics for all combinations run. The table is sorted by Macro
F1.

 Adjacency Construction     Layer         Seed    Accuracy    Bal. Accuracy     CE Loss    Macro F1     Weighted F1
 Delaunay                   SEAConv       123       0.9039            0.7871     0.2397       0.7988          0.9017
 Delaunay                   SEAConv       789       0.9034            0.7872     0.2408       0.7976          0.9010
 Delaunay                   SEAConv       456       0.9038            0.7837     0.2406       0.7969          0.9011
 k-NN (kN N = 3)            SEAConv       123       0.9034            0.7838     0.2422       0.7959          0.9006
 k-NN (kN N = 3)            SEAConv       456       0.9034            0.7818     0.2410       0.7956          0.9007
 Delaunay                   SEAConv       42        0.9032            0.7830     0.2430       0.7953          0.9008
 Delaunay                   GATConv       789       0.9036            0.7870     0.2401       0.7951          0.9016
 k-NN (kN N = 6)            SEAConv       456       0.9029            0.7828     0.2445       0.7951          0.9003
 k-NN (kN N = 6)            SEAConv       123       0.9028            0.7802     0.2437       0.7950          0.9002
 k-NN (kN N = 6)            SEAConv       789       0.9031            0.7818     0.2435       0.7949          0.9004
 k-NN (kN N = 3)            SEAConv       789       0.9029            0.7808     0.2413       0.7946          0.9002
 Radius                     SEAConv       42        0.9016            0.7813     0.2477       0.7939          0.8991
 k-NN (kN N = 3)            SEAConv       42        0.9021            0.7805     0.2438       0.7938          0.8995
 Delaunay                   GATConv       456       0.9037            0.7802     0.2406       0.7937          0.9013
 Delaunay                   GATConv       123       0.9030            0.7826     0.2418       0.7925          0.9007
 Radius                     SEAConv       456       0.9016            0.7788     0.2479       0.7923          0.8988
 Radius                     SEAConv       789       0.9005            0.7784     0.2482       0.7922          0.8978
 Radius                     SEAConv       123       0.9011            0.7778     0.2499       0.7918          0.8983
 k-NN (kN N = 6)            SEAConv       42        0.9013            0.7758     0.2463       0.7909          0.8985
 Radius                     GATConv       42        0.9023            0.7795     0.2465       0.7904          0.9000
 Delaunay                   GATConv       42        0.9030            0.7764     0.2416       0.7904          0.9005
 Complete                   SEAConv       123       0.8997            0.7794     0.2616       0.7900          0.8972
 Radius                     GATConv       123       0.9021            0.7801     0.2486       0.7899          0.8998
 k-NN (kN N = 6)            GATConv       456       0.9019            0.7738     0.2475       0.7897          0.8993
 k-NN (kN N = 6)            GATConv       123       0.9017            0.7766     0.2473       0.7893          0.8995
 Radius                     GATConv       789       0.9022            0.7743     0.2461       0.7892          0.8998
 Complete                   SEAConv       456       0.8998            0.7780     0.2605       0.7889          0.8970
 k-NN (kN N = 3)            GATConv       42        0.9017            0.7765     0.2458       0.7888          0.8992
 k-NN (kN N = 6)            GATConv       42        0.9021            0.7723     0.2470       0.7884          0.8993
 Complete                   SEAConv       42        0.8991            0.7788     0.2628       0.7880          0.8965
 k-NN (kN N = 3)            GATConv       456       0.9018            0.7721     0.2463       0.7880          0.8992
 Complete                   SEAConv       789       0.8997            0.7763     0.2614       0.7879          0.8969
 k-NN (kN N = 3)            GATConv       789       0.9019            0.7740     0.2439       0.7878          0.8991
 Radius                     GATConv       456       0.9017            0.7724     0.2476       0.7872          0.8991
 k-NN (kN N = 6)            GATConv       789       0.9019            0.7703     0.2474       0.7871          0.8992
 Delaunay                   GCNConv       789       0.9005            0.7735     0.2460       0.7870          0.8974
 k-NN (kN N = 3)            GATConv       123       0.9008            0.7729     0.2487       0.7867          0.8983
 Complete                   GATConv       456       0.9011            0.7716     0.2523       0.7867          0.8985
 Delaunay                   GCNConv       42        0.8999            0.7744     0.2476       0.7866          0.8969
 Delaunay                   GCNConv       123       0.8997            0.7724     0.2487       0.7863          0.8969
 Delaunay                   GCNConv       456       0.9003            0.7698     0.2480       0.7858          0.8971
 Complete                   GATConv       789       0.8998            0.7683     0.2558       0.7831          0.8974
 k-NN (kN N = 3)            GCNConv       789       0.8989            0.7712     0.2518       0.7829          0.8961
 Complete                   GATConv       123       0.9001            0.7650     0.2555       0.7827          0.8974
 Complete                   GATConv       42        0.8997            0.7687     0.2577       0.7823          0.8972
 Radius                     GCNConv       42        0.8978            0.7685     0.2560       0.7820          0.8951
 Radius                     GCNConv       456       0.8983            0.7661     0.2546       0.7814          0.8952
 k-NN (kN N = 3)            GCNConv       42        0.8979            0.7680     0.2539       0.7805          0.8949
 Radius                     GCNConv       789       0.8985            0.7636     0.2549       0.7804          0.8952
 Radius                     GCNConv       123       0.8982            0.7608     0.2546       0.7800          0.8948
 k-NN (kN N = 3)            GCNConv       123       0.8975            0.7656     0.2558       0.7796          0.8944
 k-NN (kN N = 3)            GCNConv       456       0.8976            0.7580     0.2537       0.7774          0.8941
 Delaunay                   GINConv       123       0.8979            0.7575     0.2609       0.7768          0.8951
                                                                                             Continued on next page

                                                         24
                                                                     A PREPRINT - O CTOBER 9, 2026

Continued from previous page
Adjacency Construction Layer     Seed   Accuracy   Bal. Accuracy   CE Loss   Macro F1   Weighted F1
Delaunay               GINConv   789      0.8976         0.7526     0.2642     0.7762        0.8946
k-NN (kN N = 6)        GCNConv   42       0.8964         0.7581     0.2584     0.7758        0.8932
k-NN (kN N = 6)        GCNConv   789      0.8970         0.7577     0.2578     0.7757        0.8936
Delaunay               GINConv   42       0.8974         0.7558     0.2659     0.7755        0.8946
k-NN (kN N = 6)        GCNConv   456      0.8961         0.7557     0.2599     0.7749        0.8930
k-NN (kN N = 6)        GCNConv   123      0.8962         0.7576     0.2609     0.7749        0.8929
Delaunay               GINConv   456      0.8969         0.7483     0.2679     0.7710        0.8939
k-NN (kN N = 3)        GINConv   789      0.8949         0.7499     0.2706     0.7707        0.8920
Radius                 GINConv   789      0.8941         0.7538     0.2787     0.7707        0.8912
k-NN (kN N = 3)        GINConv   123      0.8955         0.7490     0.2699     0.7702        0.8927
k-NN (kN N = 3)        GINConv   456      0.8954         0.7440     0.2753     0.7685        0.8922
k-NN (kN N = 3)        GINConv   42       0.8951         0.7398     0.2722     0.7682        0.8916
Radius                 GINConv   42       0.8938         0.7431     0.2830     0.7678        0.8903
Complete               GCNConv   123      0.8927         0.7495     0.2726     0.7672        0.8896
Radius                 GINConv   123      0.8941         0.7452     0.2802     0.7672        0.8907
Radius                 GINConv   456      0.8934         0.7457     0.2849     0.7667        0.8899
Complete               GCNConv   42       0.8922         0.7495     0.2719     0.7654        0.8889
Complete               GCNConv   456      0.8924         0.7461     0.2720     0.7647        0.8892
Complete               GCNConv   789      0.8924         0.7481     0.2728     0.7645        0.8889
k-NN (kN N = 6)        GINConv   123      0.8932         0.7391     0.2781     0.7640        0.8902
k-NN (kN N = 6)        GINConv   42       0.8938         0.7355     0.2776     0.7619        0.8904
k-NN (kN N = 6)        GINConv   789      0.8922         0.7327     0.2809     0.7603        0.8888
k-NN (kN N = 6)        GINConv   456      0.8924         0.7313     0.2829     0.7580        0.8892
Complete               GINConv   456      0.8831         0.7089     0.3146     0.7353        0.8797
Complete               GINConv   42       0.8837         0.7014     0.3146     0.7324        0.8801
Complete               GINConv   789      0.8827         0.7032     0.3192     0.7308        0.8789
Complete               GINConv   123      0.8827         0.6956     0.3187     0.7266        0.8788

                                              25
