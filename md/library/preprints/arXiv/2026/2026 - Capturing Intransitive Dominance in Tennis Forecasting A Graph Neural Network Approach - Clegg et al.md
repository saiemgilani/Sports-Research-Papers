<!-- source: library/preprints/arXiv/2026/2026 - Capturing Intransitive Dominance in Tennis Forecasting A Graph Neural Network Approach - Clegg et al.pdf -->
<!-- item: https://arxiv.org/abs/2510.20454 -->
<!-- authors: Lawrence Clegg, John Cartlidge -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-18; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Capturing Intransitive Dominance in Tennis Forecasting: A Graph Neural Network Approach

                                                 Capturing Intransitive Dominance in Tennis
                                               Forecasting: A Graph Neural Network Approach
                                                                                   ∗
                                                               Lawrence Clegg       , John Cartlidge
                                                School of Engineering Mathematics and Technology, University of Bristol,
                                                     Ada Lovelace Building, Tankard’s Close, Bristol, BS8 1TW, UK
arXiv:2510.20454v3 [cs.LG] 11 Nov 2026




                                         Abstract
                                         Intransitive player dominance, where player A beats B, B beats C, but C
                                         beats A, is common in competitive tennis. Yet, there are few known at-
                                         tempts to incorporate it within forecasting methods. We address this problem
                                         with a graph neural network approach that explicitly models these intran-
                                         sitive relationships through temporal directed graphs, with players as nodes
                                         and their historical match outcomes as directed edges. Our model (65.7%
                                         accuracy, 0.214 Brier score) forecasts competitively with established rating
                                         systems such as Weighted Elo. Although it does not improve on the baseline
                                         in unconditional accuracy, a forecast-encompassing test shows that it carries
                                         complementary information. A combined forecast significantly outperforms
                                         Weighted Elo, and there is some indication that the gain is larger on the
                                         intransitive matchups our model targets. A graph-based representation of
                                         player interactions thus captures a forecasting signal that transitive rating
                                         systems discard, even between players who share no common opponents.
                                         Keywords: Sports forecasting, Graph neural networks, Intransitivity,
                                         Forecast combination, Probability forecasting, Tennis prediction




                                           ∗
                                            Corresponding author
                                            Email addresses: lawrence.clegg@bristol.ac.uk (Lawrence Clegg ),
                                         john.cartlidge@bristol.ac.uk (John Cartlidge )


                                         Accepted author manuscript, International Journal of Forecasting (2027)   Page 1 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Contents

1 Introduction                                                                      3

2 Background                                                                        5

3 Data                                                                              7

4 Graph Model                                                                       8
  4.1 Graph representation . . . . . . . . . . . . . . . . . . . . . . .            8
  4.2 MagNet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           12
  4.3 Walk-forward validation . . . . . . . . . . . . . . . . . . . . .            14
  4.4 Parameter optimisation . . . . . . . . . . . . . . . . . . . . . .           15
  4.5 Ablation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         17

5 General Predictive Performance                                          19
  5.1 Model calibration . . . . . . . . . . . . . . . . . . . . . . . . . 20

6 Intransitivity and Forecast Complementarity                                      20
  6.1 Quantifying intransitivity . . . . . . . . . . . . . . . . . . . .           21
  6.2 Model complementarity and encompassing . . . . . . . . . . .                 23
  6.3 Robustness of the orthogonal-signal finding . . . . . . . . . . .            25
  6.4 Locating the complementary signal . . . . . . . . . . . . . . .              28

7 Conclusion                                                                       29

 Appendix A          Mathematical Details of MagNet                                37

 Appendix B          Extended Initial Model                                        39

 Appendix C          Cardinal Intransitivity Measure                               41

 Appendix D          Robustness of Dominance Scores                                42




                                    Page 2 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



1. Introduction
Tennis is a sport well-suited to predictive modelling, with dense tournament
schedules generating extensive historical data. The official ranking systems
of the Association of Tennis Professionals (ATP) and Women’s Tennis Asso-
ciation (WTA) have been shown to exhibit some predictive power for match
outcomes (Clarke and Dyte, 2000; Klaassen and Magnus, 2003), but there
are notable limitations: for example, ranking points accumulate over a 52-
week period, without decay, which can mask recent changes in player form,
while match-specific factors, such as surface type, tournament progression
difficulty, and margin of victory in individual matches, are overlooked.
    Some well-known methods have been applied to tennis and modified to ac-
commodate these factors, such as a Bradley-Terry model with surface-specific
adjustments (McHale and Morton, 2011) or Elo rating systems that incorpo-
rate margin of victory (Kovalchik, 2020; Angelini et al., 2022). More recently,
analysis has extended to progressively finer scales: from match outcomes to
point-level dynamics such as unforced errors (Peiris et al., 2025), rally-level
player characteristics (Epasinghege Dona et al., 2025), and shot-level tactics
such as intended serve direction (Tea and Swartz, 2023).
    Bookmakers are considered the most accurate predictors of match out-
comes (Kovalchik, 2016), with sophisticated models that adjust odds based
on betting patterns and proprietary methods. Yet, despite the multi-billion
dollar betting industry, one limitation that persists is the poor consideration
of intransitivity (van Ours, 2025). Intransitivity is analogous to rock-paper-
scissors. In tennis, it occurs where player A tends to defeat B, B defeats C, yet
C defeats A, violating the assumption of transitive dominance. One example
is Nadal beats Federer (24/40 career win rate), Federer beats Davydenko
(19/21), yet Davydenko beats Nadal (6/11). Such patterns are known to be
common in tennis, with two papers finding evidence in both the WTA and
ATP tours (Bozóki et al., 2016; Temesi, 2019), and recent work has shown
these patterns create systematic biases in rating systems like Elo (Hamilton
et al., 2025).
    Representing historical tennis matches as a graph (where each player-
matchup can be represented as an edge joining two player-nodes) can pre-
serve intransitive dynamics. Several existing graph-based approaches have
reported strong predictive performance, such as the eigenvector centrality
approach by Arcagni et al. (2023). However, global ranking methods such
as eigenvector centrality cannot capture intransitive matchups, where player-

                                    Page 3 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



specific dynamics matter more than overall strength. To better handle these
scenarios, a graph model must effectively learn from the local neighbourhoods
of players.
    We tackle this fundamental limitation of sports forecasting models with
graph neural networks (GNNs), a predictive approach that has not previously
been applied to pre-match tennis prediction (apart from our own preliminary
study: Clegg and Cartlidge, 2025).1 We first construct gender-specific surface
graphs that summarise match history and preserve player relationships, and
apply a spectral graph convolutional network for directed graphs named Mag-
Net (Zhang et al., 2021). We then establish that our model performs com-
petitively with established rating systems such as the Weighted Elo approach
by Angelini et al. (2022), although it trails the Pinnacle Sports bookmaker
benchmark. Next, we analyse model behaviour on intransitive matchups,
where intransitivity is measured using a model-free count of cyclic head-to-
head triads and an evidence-weighted adaptation of the graph-based measure
of Hamilton et al. (2025): we find that women’s tennis contains 12.1% more
cyclic triads than men’s. Finally, we use a forecast-encompassing test to
show that Weighted Elo does not fully subsume our model, whose marginal
contribution remains significant on intransitive matchups.
    In Section 2, we describe the related background of tennis forecasting,
graph-based predictive methods, and intransitivity. In Section 3, we describe
the necessary data for our research. Section 4 introduces our graph-based
method, while in Section 5, we report the models’ out-of-sample accuracy. In
Section 6, we analyse intransitivity and test whether our model carries fore-
casting information complementary to established rating systems. Finally,
in Section 7, we summarise our findings, acknowledge key limitations, and
outline future research directions.

   1
    A search was conducted on 22/10/2025 using Google Scholar to identify papers ap-
plying GNNs to tennis prediction. The search combined six graph neural network related
terms with eleven tennis prediction related terms, resulting in 66 distinct search queries.
All searches used exact phrase matching with quotation marks (e.g., “graph convolutional
network” “tennis forecasting”). In total, these search queries returned 11 papers. Other
than our own preliminary work (Clegg and Cartlidge, 2025), none of the papers used GNNs
for pre-match tennis outcome forecasting.




                                       Page 4 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



2. Background
Tennis presents an ideal domain for predictive modelling due to several of
its unique characteristics. Its scoring structure is inherently hierarchical,
advancing from points to games to sets, which lends itself to mathematical
modelling. Furthermore, the individual nature of singles tennis eliminates
the complexity of team dynamics found in other sports, where player trans-
fers and injuries can confound prediction models. The worldwide tournament
calendar also ensures that the same players face one another repeatedly on
multiple surfaces and across various event tiers, thereby generating a dense
record of head-to-head encounters that can be analysed for statistical infer-
ence.
    Various predictive modelling approaches have been developed for tennis.
Point-based models determine match win probabilities by first estimating on-
serve and return strengths to obtain point win probabilities and then applying
hierarchical equations that reflect the structure of tennis scoring; examples
include the Bayesian model of Ingram (2019) and the serve-performance fore-
casts of Gollub (2021). In contrast, pairwise comparison models use head-to-
head match outcomes to dynamically update relative player strength scalars,
as in the popular Elo rating system (Elo and Sloan, 1978). Regression models
using player statistics as predictors can also be used; Buhamra et al. (2024)
compared several such specifications for Grand Slam matches. Kovalchik
(2016) compared the performance of various published methods across these
categories, finding that a specialised Elo implementation by Morris and Bia-
lik (2015) achieved 70% accuracy, second only to the Bookmaker Consensus
Model (BCM) of Leitner et al. (2009) at 72%. Wilkens (2021) similarly find
that machine-learning models plateau near 70% accuracy, with most predic-
tive information already embedded in betting-market odds.
    While the original Elo rating model by Elo and Sloan (1978) was intended
for chess, its application to tennis is well-established. Kovalchik (2020) devel-
oped four distinct models that extended Elo by incorporating various margin
of victory measures, including: set scores, games won, break points won, to-
tal points won, and serve percentage won. Angelini et al. (2022) proposed a
similar method, named Weighted Elo, that adjusts rating updates based on
the proportion of games won in each match. Both methods demonstrated
improvements over the standard Elo system, confirming that incorporating
greater match information leads to more accurate predictions.
    One group of models that the survey by Kovalchik (2016) did not consider

                                    Page 5 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



was graph-theoretic methods. Two early studies that applied graph theory to
tennis offered alternative rating systems to the official ATP ratings. Radicchi
(2011) applied PageRank, a node importance algorithm originally developed
by Brin and Page (1998), to identify the most successful men’s tennis players,
using a dataset of matches played from January 1968 to October 2010. They
observed that their ranking method outperformed the ATP and ITF rankings
by anticipating, a year in advance, the player who would top those official
rankings. However, they found active players were penalised compared to
retired ones due to their incomplete career data. Subsequently, Dingle et al.
(2013) extended Radicchi’s PageRank approach by evaluating it as a match-
outcome predictor, finding it slightly outperformed official rankings on ATP
matches (67.0% vs 66.4%). However, the authors did not distinguish between
court surfaces, and lower-ranked players appeared in too few matches to be
reliably ranked.
     Aparício et al. (2016) incorporated court surface considerations with a
coloured directed network. With the use of 4-node subgraphs, the authors
developed an Orbit-score ranking system that captured indirect dominance
relationships between players from different time periods. The model iden-
tified surface specialists, all-round players, and players with an Achilles-heel
on a specific surface. While their model enabled more detailed player differ-
entiation, it was not extended to directly predict individual match outcomes.
More recently, Bayram et al. (2021) used three centrality measures (out-in-
degree-difference, Hubs, and PageRank) to estimate surface-specific player
scores. The score was used as a feature in several machine learning mod-
els to predict individual matches, with a random forest model achieving the
highest classification accuracy of 67% on a dataset of 21,083 matches be-
tween 2012 and 2020. The authors’ approach demonstrated the effectiveness
of graph-based features, but prioritised machine learning sophistication over
the graph methods themselves.
     Arcagni et al. (2023) developed a new model based on the eigenvector cen-
trality, deriving global ratings that were subsequently used as covariates in a
simple logit model for match prediction. The eigenvector centrality approach
attained a Brier score of 0.194 on ATP matches between 2016 and 2020, out-
performing several competing methods, including standard Elo (0.206) and
the margin of victory Elo extension (0.204) by Kovalchik (2020). This impres-
sive performance demonstrated the growing effectiveness of graph-theoretic
methods in tennis prediction while suggesting potential for even more sophis-
ticated approaches.

                                    Page 6 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



    In other domains, recent advances in deep learning applied to graphs, par-
ticularly Graph Neural Networks (GNNs), have shown considerable promise.
There have been successful applications of GNNs in other sports, such as
American football and Counter-Strike: Global Offensive (Xenopoulos and
Silva, 2021), association football (Mirzaei, 2022), and basketball (He et al.,
2022).
    Unlike traditional GNN architectures designed for undirected or symmet-
ric graphs, recent work on spectral methods for directed graphs enables learn-
ing from cyclic structures through complex-valued representations. Zhang
et al. (2021) used the magnetic Laplacian (a complex Hermitian matrix) to
encode directed cycle information in its eigenvalue spectrum, with a tun-
able parameter q that controls sensitivity to cyclical patterns. Such spec-
tral methods can address intransitive relationships between nodes, where
A → B → C → A forms a directed cycle that cannot be resolved into a
strict hierarchical ordering. The capability to learn from directed cycles,
rather than through symmetrisation, makes spectral methods for directed
graphs specifically suited to tennis, where intransitive matchup patterns are
prevalent (Bozóki et al., 2016; Temesi, 2019). Representing tennis players
as nodes and their matchup histories as directed edges, GNN architectures
like MagNet (Zhang et al., 2021) can encode intransitive matchup patterns
as directed-cycle information that scalar ratings cannot represent.

3. Data
We collected historical data on professional tennis matches organised by both
the Association of Tennis Professionals (ATP) and the Women’s Tennis As-
sociation (WTA) from tennis-data.co.uk, spanning 8 January 2012 to 16 Oc-
tober 2025.
    The dataset contains information such as match date, competitors, games
won by each competitor for each set played, tournament, surface, round
of the tournament, and betting odds from several bookmakers, from which
we select Pinnacle Sports due to the consistent availability of their odds
across the dataset timespan. Additionally, Pinnacle Sports is recognised
as a “sharp” bookmaker, one that operates with low margins and adjusts
odds aggressively based on large betting volumes, which leads to accurate
outcome forecasting (Buchdahl, 2016; Hegarty and Whelan, 2025). We also
gathered the following player characteristics from tennisexplorer.com: height,
weight, date of birth, and handedness. For missing characteristic values, the

                                    Page 7 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



median of the population is imputed. These static attributes are evaluated
as candidate node features but do not improve predictive accuracy, and are
excluded from the final model (Section 4.5).
    We filter for matches played in the highest tiers of professional tennis for
both men and women: Grand Slams, the season-ending tour finals, and all
1000 and 500 series events. We treat men’s and women’s tennis as separate
prediction tasks, training and validating each tour independently; only hy-
perparameter tuning is run jointly, so both tours share a single configuration.
    After removing incomplete matches and entries with missing or incorrect
values, the final dataset comprises 20,181 matches played by 670 men and
19,985 matches played by 640 women. We split each tour chronologically
into three consecutive sets. The earliest matches build the dominance graph
and train the model. The next 8,435 matches form a validation set, used
for hyperparameter optimisation (Section 4.4) and the ablation study (Sec-
tion 4.5). The most recent 12,052 matches are held out as the out-of-sample
test set. The men’s validation set runs from 31 July 2018 to 21 February
2022 and the women’s from 28 August 2018 to 12 March 2022, with each test
set beginning the next day and ending in October 2025. The walk-forward
procedure is detailed in Section 4.3.

4. Graph Model
In their overview of temporal graph networks, Longa et al. (2023) describe
two primary approaches to temporal graph representation: snapshot-based
(using a sequence of static graphs capturing network states at different time
points) and event-based (representing edges as a continuous stream of times-
tamped interactions). Here, we adopt a snapshot-based approach by inter-
preting each tournament round (e.g., Wimbledon 2010 Quarter Finals) as a
discrete timestamped snapshot.
    We now describe our graph construction, the use of MagNet for match
prediction, and our walk-forward validation approach. Table 1 summarises
the key mathematical notation used in this section.

4.1. Graph representation
In professional tennis, players compete on three distinct court surfaces: clay,
grass, and hard. Each surface requires different playing styles and favours
different skill sets, with researchers such as Fayomi et al. (2022) finding that
the “surface on which a game is played on contributes significantly towards a

                                    Page 8 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


                    Table 1: Mathematical notation, grouped by role.

         Symbol     Description
         Indices
             s      Target court surface for which the graph is built (clay, grass, or hard)
            sk      Court surface of historical match k
           i, n     Snapshot indices: arbitrary (i), prediction target (n)
            k       Historical match index
           u, v     Player indices
         Observed data and graph structure
          τn , τ k  Timestamps: snapshot n (earliest scheduled match); match k
         gk (u, v)  Proportion of games won by u against v in match k
             V      Node set (players)
            Ei      Edge set at snapshot i (head-to-head matchups)
            Gsi     Surface-specific graph at snapshot i
           XV i     Node feature matrix at snapshot i
         Optimised parameters
            λ       Time decay rate
          αs,sk     Surface similarity (skill transfer from sk to s)
           βk       Tournament prestige (by tier of match k)
            q       Directional weighting in the magnetic Laplacian (phase strength)
         Derived quantities and estimators
             ϕk     Time decay coefficient for match k (from λ)
         Wis , wuv  Edge weights for surface s; weight from u to v
         Dns (u, v) Dominance score of u against v on surface s at snapshot n
            p̂uv    Estimated set-win probability, u against v
          P̂3 , P̂5 Estimated match-win probabilities (best-of-3, best-of-5)



player’s performance”. Players compete separately on the men’s tour (ATP)
and women’s tour (WTA), with no cross-gender competition. We construct
separate graph representations for each gender and each surface, account-
ing for this well-documented variation in player performance across surfaces,
although we incorporate cross-surface information through our dominance
score calculation, which aggregates match results from all surfaces with ap-
propriate weighting.
    A static directed graph can be formally defined as G = (V, E, XV , XE ),
where V represents a set of nodes (or vertices), E represents the set of edges
between nodes, XV represents the associated node features, and XE repre-
sents the associated edge features. The edges are directed, meaning (u, v)
does not necessitate (v, u) and E is asymmetric. Importantly, each edge
(u, v) can possess a weight wuv ∈ XE that quantifies the strength of the
relationship.
    For each tournament round snapshot, we construct three surface-specific
graphs per gender, summarising all the preceding matches. By encoding sur-


                                          Page 9 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



face in the graph, we aim to model surface-dependent performance dynamics
more precisely. Hence, for each snapshot i and court surface s (clay, grass,
or hard), we construct the graph:

                              Gsi = (V, Ei , XVi , Wis ),                         (1)

where Wis denotes the edge-weight vector. Since this is the only edge feature
we consider, we use the simplified notation Wis rather than the more general
edge feature matrix XE,s   i .
    We consider the set of all players of a given gender who competed during
the period covered by the dataset as the fixed node set V . The node features
XVi ∈ R|V |×d are the surface-specific in-degree and out-degree of each player,
summarising the number of incoming and outgoing dominance edges for each
player-node. We also evaluated static player attributes (height, weight, date
of birth, and handedness) as node features, but they did not improve pre-
dictive accuracy and are excluded from the final model (Section 4.5). Each
feature qvector v is ℓ2 -normalised, scaling the vector by its Euclidean norm
           P 2
∥v∥2 =         j vj , resulting in unit-length vectors that preserve directional in-
formation while standardising magnitude. Maintaining the fixed player set V
across surface-specific graphs allows the model to process the surface-specific
degree features consistently across surfaces.
    We use a common edge index set Ei ⊆ V ×V across all surfaces, summaris-
ing historical head-to-head matchups between players, with edge weights Wis
that are surface-specific. Provided there is at least one match played between
player u and player v prior to snapshot i, we add a weighted directed edge
(u, v) to Ei . Each weight wuv ∈ Wis represents the head-to-head dominance
of player u over player v, where direction indicates the dominant player and
magnitude quantifies the degree of dominance. The edge weight wuv is cal-
culated based on the historical proportion of games won by player u against
player v. This base value is then adjusted using factors for time decay, sur-
face weighting, and tournament weighting. Motivated by Kovalchik (2020),
who found granular performance measures more robust than binary match
outcomes, we treat the dominance signal, the proportion of sets, games, or
points won, as a tuned hyperparameter (Table 2). The proportion of games
won gk (u, v) ∈ [0, 1] by player u against v in historical match k achieved
the best validation Brier score on both tours, so we adopt it as the primary
variable in our dominance score calculation.
    An early use of exponential time decay to down-weight older sports match

                                    Page 10 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



results originates from Dixon and Coles (1997) for association football, where
they down-weighted each historical match in the likelihood by an exponential
factor. It was subsequently adapted to tennis by McHale and Morton (2011),
who additionally incorporated surface weights to improve forecasting accu-
racy. We further extend this principle by introducing an explicit tournament
quality factor, so that results from higher-prestige events have greater influ-
ence on the estimated dominance between players. Hence, to each historical
result gk (u, v) we apply the time decay coefficient:

                          ϕk (u, v) = exp(−λ (τn − τk )),                         (2)

where τn denotes the timestamp of the earliest scheduled match in the tour-
nament round being predicted, τk denotes the timestamp of historical match
k, and the decay rate λ > 0 is a learnable parameter governing the rate at
which older matches lose influence. This approach ensures that the influ-
ence of past interactions diminishes over time, with more recent interactions
having a greater impact on the current dominance scores.
    For each target surface s, we calculate surface-specific dominance scores
that incorporate matches from all surfaces with appropriate weighting. To
refine the influence of each historical match, we scale each match by two fur-
ther coefficients: a surface similarity parameter αs,sk and a tournament pres-
tige parameter βk . The surface similarity factor αs,sk down-weights matches
played on surface sk when constructing the graph for target surface s, reflect-
ing the reduced transferability of performance across surfaces, with αs,s = 1
for same-surface matches. The tournament prestige factor βk assigns weights
based on match k’s tournament tier relative to Grand Slams, acknowledging
that results from higher-prestige events may be more indicative of true player
dominance.
    These parameter values are optimised using the Non-dominated Sorting
Genetic Algorithm II (NSGA-II), described in Section 4.4. The surface-
specific dominance score is updated for each new tournament snapshot n
between players u and v on surface s as follows:
                                    P
                          s             αs,s βk ϕk gk (u, v)
                       Dn (u, v) = k P k                     ,              (3)
                                          k αs,sk βk ϕk

where the sum ranges over all matches k between players u and v that oc-
curred before snapshot n, and gk (u, v) ∈ [0, 1] is the proportion of games won
by player u against v in historical match k, and sk is the surface of historical

                                    Page 11 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



match k. αs,sk captures surface similarity, βk captures tournament prestige,
and ϕk captures match recency. This calculation is performed independently
for each of the three surfaces, yielding three separate graph representations.
Since gk (u, v) records the proportion of games won rather than the match
outcome alone, each match is worth much more than one binary observation
(measured in Section 6.3).
    The dominance score calculation produces a value Dns (u, v), from which
we create a single directed edge pointing from the player with the higher
dominance score to the weaker player. Specifically, if Dns (u, v) > 0.5, we
assign a directed edge from player u to player v with weight Dns (u, v). Con-
versely, if Dns (u, v) < 0.5, we assign a directed edge from player v to player
u with weight 1 − Dns (u, v). If Dns (u, v) = 0.5 exactly, no edge is created.
This ensures that each player pair contributes at most one directed edge
to a graph, with the edge always pointing from the dominant player to the
dominated player. Finally, we remove an edge when its corresponding players
have not met for longer than a maximum edge age, set by the hyperparameter
optimisation to 1.55 years (Table 2).
    This directed edge construction with asymmetric weights naturally pre-
serves the intransitive relationships that exist between players. Figure 1
provides an overview of our temporal graph construction process.

4.2. MagNet
To generate match outcome probability estimates, we use the spectral graph
convolutional network (GCN) MagNet by Zhang et al. (2021).2 We frame the
problem as directional edge prediction, where for a scheduled match between
players u and v, MagNet estimates the edge direction (translating to set-
win probability). We select MagNet specifically for its use of the magnetic
Laplacian, a complex Hermitian matrix that enables learning from intransi-
tive relationships rather than imposing transitive hierarchies. The magnetic
Laplacian encodes undirected geometric structure (existence of head-to-head
matches) in the magnitude of its entries and directional information (who
dominated) in their phase.
    MagNet uses a parameter q ∈ [0, 0.25] that controls the extent to which
directional information is incorporated. When q = 0, the model disregards

  2
    MagNet is accessible via the PyTorch Geometric Signed Directed library (He et al.,
2024).



                                    Page 12 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




                Figure 1: Overview of the graph construction process.
Following each snapshot, the Dominance Score (Equation 3) of the observed
matchups is updated, determining the direction and weight of the edge between the
players in the surface graphs Gsi . Considering new graphs that are initialised at the
2024 Wimbledon semi-finals, i = 0, two new edges are created. They point from
the player who won > 50% of games, towards the player with the lower percentage
of games won. At i = n, Djokovic wins 54% of the games in the Paris Olympics
gold medal match, which weakens Alcaraz’s dominance in all three surface graphs,
most in the clay graph. Because of Alcaraz’s stronger performance at Wimbledon,
every Djokovic-Alcaraz edge still points towards Djokovic. Static node features are
evaluated during parameter optimisation but excluded from the final model.


which player has historically dominated the head-to-head matchups, whereas
at q = 0.25, this dominance information is maximally integrated. We opti-
mise q; the search selects q = 0.238, near its maximum, where directional
information is most strongly incorporated.
    The model is trained to predict set outcomes by minimising cross-entropy
loss with the Adam optimiser. The learning rate (1.8 × 10−3 ) is tuned jointly
with the graph and architecture hyperparameters (Section 4.4), while weight
decay (10−5 ) and dropout (0.3) are fixed at standard defaults. Complete
mathematical details are provided in Appendix A.
    In our dataset, there are both best-of-5 matches (played at men’s Grand
Slams) and best-of-3 matches (all women’s matches and non-Grand Slam
men’s matches). In a best-of-3 match, there is a greater chance for the lower-
ranked player to win as there are fewer opportunities for the stronger player


                                    Page 13 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 2: The walk-forward validation process. After each pass, predictions are generated
and the model is retrained; the historical graph grows as matches are added. For illustra-
tion, the schematic is not to scale: in practice, the historical graph and sliding training
window span several hundred snapshots.


to assert their dominance. Therefore, when producing probability estimates
for the out-of-sample test set, we calculate match outcome probabilities for a
best-of-3 sets match P̂3 and a best-of-5 sets match P̂5 under the assumption
of independent and identically distributed sets:


P̂3 (u, v) = p̂2uv +2p̂2uv (1− p̂uv ),
                                P̂5 (u, v) = p̂3uv +3p̂3uv (1− p̂uv )+6p̂3uv (1− p̂uv )2
                                                                                    (4)
where p̂uv is the set-win probability for player u against player v output by
MagNet.

4.3. Walk-forward validation
With the temporal directed graph representation of tennis matches described
in Section 4.1, we adopt a walk-forward validation approach, shown in Fig-
ure 2, to optimise parameters on a validation set and evaluate the model on
an out-of-sample test set.
    At each snapshot, three surface graphs are constructed from the earliest
85% of historical matches. The model is then trained to predict the most
recent 15% of matches, held out as labelled edges, from the graph built on
the earlier matches.
    The MagNet model parameters are optimised by training on this 15%
edge set. The model is initially trained for 100 epochs. To adapt to evolving
player dynamics, it is then retrained for an additional 30 epochs every 38
snapshots, which we approximate to a quarter of a year. Each training
run completes in under 10 seconds on consumer-grade hardware (RTX 2070
Super, Ryzen 3600).
    Following each training run, the model predicts outcomes for the next
chronological snapshot. Once the true outcomes for a given snapshot are

                                         Page 14 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



observed, its matches are integrated into the historical graph. The fixed-size
training window then advances, redefining the 15% training set to include
the most recent matches for the subsequent cycle.

4.4. Parameter optimisation
To identify the optimal parameters for graph construction, model architec-
ture, and training, we conduct 250 trials using walk-forward validation. Each
tour’s match history is split chronologically: an initial window seeds the dom-
inance graph, after which the model trains and hyperparameters are scored
on a validation period ending in early 2022 (8,435 matches across both tours).
All later matches, through October 2025, form the held-out test set of 12,052
matches (Section 5) and are not used in tuning.
    We select the final configuration in three stages: an initial optimisation
over the full hyperparameter set, an ablation that discards the components
which do not improve the validation Brier score (Section 4.5), and a re-
tuning of the reduced set. The configuration reported in this section is that
of the final re-tuning, which optimises the 12 hyperparameters retained after
ablation.
    Table 2 summarises the search space used for each parameter during op-
timisation, along with the optimal values found by applying the NSGA-II
algorithm by Deb et al. (2002).3 We adopt a multi-objective framework,
treating the Brier scores for men’s and women’s tours as separate objec-
tives. We identify Pareto-optimal solutions that have a favourable trade-off
between men’s and women’s performance, selecting a unified parameter set
that balances predictive accuracy across both genders. The final model has
12 graph-construction and architecture hyperparameters, listed in Table 2
and retained after the ablation in Section 4.5, all tuned jointly with the
Adam learning rate.
    Given the model’s complexity relative to traditional sports forecasting
approaches, we select conservative search bounds for the graph construction
parameters, described in Section 4.1. Tournament tiers are weighted uni-
formly, as tier-specific weights did not improve predictive accuracy in our
ablation.
    For the model architecture, we optimise several hyperparameters. The
most important of these are the order of the Chebyshev polynomial approx-

  3
    We use the Python library Optuna (Akiba et al., 2019) to implement the NSGA-II
algorithm.


                                    Page 15 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


Table 2: Search spaces and selected values for the graph-construction and architecture
hyperparameters.

       Parameter                        Search Space        Optimal Value
       Model Architecture
       K, Chebyshev filter order             1, 2, 3                1
       Hidden units                     16, 32, 64, 128            16
       Number of layers                       1, 2                  2
       Use activation function            True, False             False
       Directional weighting q             0.10–0.25              0.24
       Dominance signal
       Granularity                    games, sets, points         games
       Min. dominance percentile           0.0–0.5                 0.10
       Time decay
       λ                                    0.0–2.5                0.34
       Max. edge age                        0.0–8.0                1.55
       Surface transferability (symmetric)
       αh,c                                0.0–0.5                 0.41
       αh,g                                0.0–0.5                 0.22
       αc,g                                0.0–0.5                 0.40
   Notes. Tuned parameters were optimised under uniform distributions over the
   stated ranges; comma-separated values denote discrete choices. Surface transfer
   is symmetric (αs,sk = αsk ,s ), with subscripts denoting surfaces: hard (h), clay
   (c), grass (g). In line with the ablation, tournament tiers are weighted uniformly
   (β = 1).


imation in the spectral graph convolution and the number of complex graph
convolutional layers, collectively determining the size of the local neighbour-
hood from which player information is aggregated. We also optimise the
dimensionality of the hidden channels, which controls the model’s capac-
ity to learn complex features. Furthermore, we evaluate the inclusion of
a complex-valued ReLU activation function, which introduces non-linearity
and allows the model to capture more intricate patterns.
    From the Pareto-optimal solutions shown in Figure 3, we select the trial
with K = 1 and L = 2 layers and therefore an effective receptive field span-
ning 2 hops. This neighbourhood size captures direct opponents and their
immediate neighbours, providing sufficient context for detecting intransitive

                                    Page 16 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 3: Brier scores from 250 parameter optimisation trials, with Pareto-optimal trials
highlighted. Colour indicates receptive field size (K × L hops).


cycles while avoiding overfitting to global network properties that charac-
terise existing graph-theoretic measures like eigenvector centrality.
    The ablation that follows confirms the retained set is not redundant:
removing any of its main components measurably degrades the validation
Brier score.

4.5. Ablation
We assess each component’s contribution with a component ablation on the
validation set, altering the full tuned configuration of the selection stage
(Section 4.4) one component at a time: removing each retained component,
and applying each simplification or addition considered for the final model
(Table 3).
    Two findings stand out. First, the predictive signal is carried overwhelm-
ingly by the graph structure. Removing the dominance graph entirely (leav-
ing self-loops only, with fixed random node features) raises the pooled Brier
score from 0.2142 to 0.2492, and the most consequential individual compo-
nents are graph-structural: edge-age decay (0.0118), the multi-hop receptive
field (0.0095), and the in/out-degree node features (0.0058). By contrast, the

                                     Page 17 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


Table 3: Component ablation of the tuned configuration on the validation set: pooled
Brier-score change for each variant.

                   Variant                                ∆Brier
                   Remove a component
                   Dominance graph (entire)              +0.0350
                   Edge-age decay                        +0.0118
                   Multi-hop receptive field (L=2)       +0.0095
                   In/out-degree node features           +0.0058
                   Cross-surface edges                   +0.0043
                   Dominance edge weights                +0.0013
                   Directional weighting (q)             +0.0007
                   Simplify or add
                   Static player attributes (add)        +0.0005
                   Uniform tournament-tier weights       −0.0001
                   Symmetric surface transfer             0.0000
                   Games-level dominance signal           0.0000
Entries are each variant’s Brier score (pooled across both tours by match count) minus
   the full-model reference of 0.2142. Positive values indicate a degraded forecast.


directional weighting q (0.0007) and the dominance edge weights (0.0013) are
the two smallest effects: the explicit direction and magnitude of each individ-
ual matchup add little to overall accuracy, consistent with the model’s value
being the broad-based complementary signal of Section 6.2 rather than local
intransitivity decoding.
    Second, descriptive node features beyond degree do not help. Adding the
static player attributes (height, weight, date of birth, handedness) raises the
Brier score by 0.0005. The full model therefore retains only the graph-derived
in/out-degree as node features, and these are themselves valuable: removing
them is among the largest single-component effects.
    The remaining choices are simplifications the ablation shows cost nothing.
Symmetric surface transfer (αs,sk = αsk ,s ) and uniform tournament tiers each
move the pooled Brier score by at most 0.0001, so we adopt both, shrinking
the hyperparameter set before the final re-tuning. The games-level domi-
nance signal performs no worse than the set- or point-level alternatives, so it
is the level we retain.



                                    Page 18 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


     Table 4: Model Performance vs Baselines: Men’s and Women’s Results by Surface.

                                  Model             Elo           WElo             BT              PS
Gender      Surface   Count     Acc    Brier    Acc    Brier    Acc    Brier    Acc    Brier    Acc    Brier
Men         Clay       1710 0.667 0.209 0.643 0.219 0.653 0.215 0.637 0.217 0.708 0.190
Men         Grass       741 0.676 0.205 0.680 0.205 0.687 0.202 0.649 0.212 0.714 0.185
Men         Hard       3604 0.656 0.214 0.659 0.215 0.661 0.214 0.659 0.217 0.683 0.199
Women       Clay       1539    0.663 0.210 0.668 0.211 0.669 0.209 0.650 0.215 0.700 0.192
Women       Grass       738    0.654 0.218 0.659 0.221 0.664 0.218 0.649 0.223 0.663 0.207
Women       Hard       3720    0.646 0.219 0.641 0.221 0.647 0.218 0.634 0.223 0.675 0.205
Both        All       12052    0.657 0.214     0.653   0.217   0.658 0.214     0.646   0.219   0.687   0.198
 *
      Notes. Bold indicates best performance and underlined indicates second-best among the evaluated
     models (excluding PS benchmark) for each surface/gender combination, with values tied at three decimal
     places sharing a mark. Count refers to the number of matches in the out-of-sample test set. All metrics
     rounded to three decimal places. Elo represents the standard Elo rating system by Morris and Bialik
     (2015). WElo represents the Elo extension by Angelini et al. (2022). BT is the Bradley-Terry model of
     Bradley and Terry (1952). PS represents Pinnacle Sports odds with Shin (1993) margin adjustment.



5. General Predictive Performance
We evaluate the proposed graph-based model against the Weighted Elo ap-
proach of Angelini et al. (2022), the Elo approach of Morris and Bialik (2015),
a Bradley-Terry model (Bradley and Terry, 1952), and bookmaker odds from
Pinnacle Sports. We initialise the Elo rating systems from 2012, such that
ratings are sufficiently stabilised for the out-of-sample test period.
    For the Bradley-Terry baseline, player strengths are estimated over a
rolling two-year window by regularised maximum likelihood, computed via
iterative Luce spectral ranking (Maystre and Grossglauser, 2015). For the
bookmaker benchmark, we derive margin-adjusted implied probabilities from
Pinnacle Sports odds using the model of Shin (1993), which Štrumbelj (2014)
finds more accurate than basic margin normalisation.
    The out-of-sample test period spans early 2022 to October 2025. We
report two standard metrics. Classification accuracy is the proportion of
matches whose winner is correctly identified (the predicted winner being the
player assigned p̂mP> 0.5). The Brier score (Brier, 1950) is the mean squared
forecast error, N1 N                 2
                     m=1 (p̂m − om ) , with om ∈ {0, 1} the outcome of match
m; it rewards accuracy and calibration jointly. Lower Brier score and higher
accuracy indicate better forecasts.
    Table 4 reports performance overall and by surface. Our model is compet-
itive with the rating-system baselines: it ties Weighted Elo (Angelini et al.,
2022) on Brier score (0.214), with Weighted Elo marginally ahead on accu-

                                               Page 19 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 4: Calibration curves for the men’s and women’s predictions, showing predicted
probabilities versus observed frequencies. Perfect calibration would align with the diagonal
y = x line.


racy (65.8% vs 65.7%); standard Elo (65.3%, 0.217) and the Bradley-Terry
model (64.6%, 0.219) follow.
    The bookmaker odds’ implied probability, denoted as “PS”, remains no-
tably superior overall with 68.7% accuracy and 0.198 Brier score, owing to
its incorporation of expert knowledge, real-time market adjustments based
on betting activity, and state-of-the-art models.

5.1. Model calibration
To assess reliability, we follow Boshnakov et al. (2017) and use recursive bin-
ning to plot calibration curves of the empirical outcome frequency P (y = 1 |
q) against predicted win probability q. Figure 4 shows predicted probabil-
ities closely tracking observed frequencies for both tours, indicating strong
calibration. The bias-corrected Murphy decomposition (Murphy, 1973; Ferro
and Fricker, 2012) of the full test-set Brier score quantifies this: the model’s
reliability term is below 0.0001, against 0.0012 for WElo, while WElo retains
slightly higher resolution (0.036 vs 0.035). These offsetting terms leave the
two near-identical in Brier score, with the model better calibrated and WElo
slightly more discriminating.

6. Intransitivity and Forecast Complementarity
A prior application of MagNet (Clegg and Cartlidge, 2025) used an unop-
timised configuration with substantial methodological limitations, includ-

                                       Page 20 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 5: An intransitive triangle among Federer, Nadal, and Davydenko. Edge weights
are career head-to-head match-win proportions. Each directed edge indicates a consistent
head-to-head advantage.


ing poorly calibrated time decay parameters, lack of cross-surface informa-
tion flow, and reduced tournament coverage (detailed comparisons in Ap-
pendix B). The present work addresses these limitations through systematic
tuning and a complete cross-surface graph construction.
    We investigate whether MagNet’s advantages stem specifically from its
ability to handle intransitive relationships. Traditional rating systems can-
not capture such structures because they rely on scalar player strength rep-
resentations, assigning each athlete a single power rating (or perhaps sepa-
rate serve and return point-win probabilities, as in the point-based model of
O’Malley (2008)).
    This limitation is particularly relevant in tennis, where stylistic matchups
can create intransitive relationships that our graph-based approach is de-
signed to utilise. A well-known example of an intransitive relationship in
tennis is shown in Figure 5 and occurred during Roger Federer’s peak in
the mid-to-late 2000s, involving Federer, Rafael Nadal, and Nikolay Davy-
denko. Although Federer was the dominant world number one, Nadal con-
sistently defeated him by exploiting his one-handed backhand with heavy,
high-topspin forehands. In turn, Nadal was often troubled by Davydenko
(when not playing on clay courts), whose flat, early baseline hitting neu-
tralised Nadal’s spin and pace, resulting in Davydenko’s repeated success on
hard courts. Completing the intransitive loop, Federer, despite his strug-
gles against Nadal, dominated Davydenko, using variety and slice to disrupt
Davydenko’s rhythm.

6.1. Quantifying intransitivity
We quantify intransitivity primarily with a model-free, ordinal count of cyclic
head-to-head triads, in the tradition of circular-triad statistics (Kendall and
Babington Smith, 1940; Shizuka and McDonald, 2012). The raw-triad count


                                     Page 21 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 6: Two intransitive cycles involving Maria Sakkari and Aryna Sabalenka, before
their match in the 2021 Abu Dhabi WTA Women’s Tennis Open. Each directed edge
indicates a head-to-head dominance advantage.


Th (u, v) counts common opponents c for which the directed-majority wins
among the three pairs {(u, c), (v, c), (u, v)} form a 3-cycle, with each pair
supported by at least h prior head-to-head matches (default h = 1). Pairs
that have never met contribute no triad. Being an integer count of raw
results, Th inherits neither the model’s dominance scores nor the instability
of a logit transform near certain outcomes, and it is the binning variable for
every forecast-comparison test in this section (Sections 6.2–6.4).
    By this count, cyclic dominance is common in professional tennis, and
more so in the women’s game: across the test set, women’s matches con-
tain 12.1% more intransitive common-opponent triads than men’s (13.87%
vs 12.37% of triads are intransitive). Figure 6 illustrates two such cycles for
one highly intransitive women’s matchup.
    We complement Th with a cardinal measure that reads intransitivity from
the magnitudes of dominance rather than the direction of wins alone. Adapt-
ing the Hodge-decomposition measure of Hamilton et al. (2025) to each
match’s common-opponent neighbourhood and scaling it by the matchup’s
accumulated evidence yields an evidence-weighted magnitude I ∗ (Auv ) (con-
struction in Appendix C). Because I ∗ derives from the model’s dominance
scores, it serves a descriptive role and enters none of the forecast-comparison
tests. It is stable under shrinkage of those scores (Appendix D) and agrees
directionally with Th without being interchangeable.
    Figure 7 shows distinct surface-specific patterns. Hard and clay courts
exhibit right-skewed distributions, with most matchups at low-to-moderate
I ∗ and a long tail of upset-prone, highly intransitive matchups. The hard
court’s larger magnitudes reflect its greater match volume. Grass shows a
concentration of moderate intransitivity despite low evidence, likely from

                                    Page 22 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting




Figure 7: Distribution of evidence-weighted intransitivity I ∗ (Auv ) across the test set, by
surface and gender, restricted to matches with I ∗ > 0. Mean values: hard (men 2.94,
women 2.99), clay (men 2.58, women 2.52), grass (men 1.95, women 2.09). Sample sizes:
hard (men n = 1,007, women n = 941), clay (men n = 433, women n = 387), grass (men
n = 171, women n = 165).


its faster pace and lower friction. The gender gap in cyclic triads, clear
under Th , is muted under I ∗ (2.77 vs 2.74 on the I ∗ > 0 subset), because
I ∗ conditions on direct head-to-head evidence and 58.2% of test matches fall
between players who have not met.

6.2. Model complementarity and encompassing
The measures of Section 6.1 describe where intransitivity concentrates. Our
model does not unconditionally outperform WElo (Section 5), so we test
whether it nonetheless carries information orthogonal to WElo that improves
a combined forecast. A forecast-encompassing test (Chong and Hendry,
1986) answers this directly. We refit the WElo logistic on the validation
set:
                    logit p̂W (y) = a0 + a1 logit πWElo (y),             (5)
where πWElo is the Weighted Elo win probability for match y. The test
isolates our model’s marginal contribution, and this Platt recalibration, with
â1 < 1, shrinks an overconfident raw WElo and itself lowers the test-set Brier


                                       Page 23 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


        Table 5: Correctness 2×2 between our model and WElo on the test set.

                                  WElo right     WElo wrong        Total
                Model right             7,036              877     7,913
                Model wrong               899            3,240     4,139
                Total                   7,935            4,117    12,052
 A forecast is correct when its favourite (p̂ > 0.5) wins. McNemar’s test does not reject
                       off-diagonal symmetry (χ2 = 0.25, p = 0.62).


score from 0.2142 to 0.2130. The encompassing test incorporates our model’s
forecast πG :
             logit p̂W+G (y) = b0 + b1 logit πWElo (y) + b2 logit πG (y),             (6)
following the combination form of Granger and Ramanathan (1984). Evalu-
ating each logistic model on the test set, WElo encompasses our model if and
only if b2 = 0 in expectation. A one-sided Diebold-Mariano test (Diebold and
Mariano, 2002) assesses whether the combination improves on recalibrated
WElo’s Brier score. Because the combination nests recalibrated WElo at
b2 = 0, with weights estimated once on validation and held fixed, the test
is valid under the fixed-scheme asymptotics of Giacomini and White (2006),
which admit nested forecasts.
    WElo is rejected as an encompassing forecaster on the test set: B(p̂W+G ) =
0.2113 vs recalibrated WElo B(p̂W ) = 0.2130 (DM p < 0.001), with combi-
nation coefficient b̂2 = +0.498. Our model carries information not already
present in WElo, and the signal is not confined to intransitive matches: eval-
uating the single validation-fitted combination on subsets of the test set, the
gain is significant on both T1 =0 (p < 0.001) and T1 >0 (p = 0.028) matches.
    Neither a surface-specific Elo (per-surface ratings) nor the Bradley-Terry
model adds information to recalibrated WElo (p = 0.28 and 0.78), so our
model’s signal is absent from every scalar rating we consider. In particular,
it comes neither from surface specialisation nor from an alternative estimate
of scalar strength. Its contribution also holds within each tour.
    Table 5 quantifies how the two forecasts differ: exactly one is correct on
14.7% of test matches, and these disagreements split almost evenly. McNe-
mar’s test does not reject symmetry, so neither systematically wins when the
two disagree. They nonetheless err in complementary ways (Section 5.1), so
combining them extracts a signal absent from either alone.

                                      Page 24 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


Table 6: Encompassing gain of the combination model across common-opponent subsets
of the test set.

        Subset                                N       ∆B         η   p-value
        No common opponents                 745     0.0044   14.6%    0.002
        Common opponents, no triad        6,275     0.0017   10.5%   <0.001
        Transitive triads                   911     0.0004    8.9%    0.371
        Intransitive triads               4,121     0.0012   10.7%    0.028
  N is the number of test matches in the subset; ∆B is the combination’s Brier-score
 improvement over recalibrated WElo; η (Equation 7) is the share of the gap between
     recalibrated WElo and Pinnacle that it closes; p-values are from a one-sided
              Diebold-Mariano test of B(W+G) < B(W) on each subset.


   To gauge how much of the available improvement this represents, we take
the Pinnacle closing odds as a sharp market forecast and measure comple-
mentarity efficiency as the share of the WElo-to-market headroom that our
model closes:
                               B(W) − B(W+G)
                           η=                    .                     (7)
                                B(W) − B(Pin)
Table 6 partitions the test set by local common-opponent structure. The
gain is significant in three of the four cells, including the 745 matches whose
players share no common opponents at all, where both the headroom and
the share of it closed are largest (η = 14.6%). On intransitive matches the
model closes η = 10.7% of a smaller headroom, with the point estimate rising
to 20.1% (h=2) and 27.2% (h=3) under the stricter triad-evidence thresh-
olds of Section 6.3. The market itself encompasses our model: adding πG
to recalibrated Pinnacle gives no Brier-score improvement on either intran-
sitivity subset (DM p ≥ 0.47), so our model carries no information beyond
the market even on intransitive matches. Its complementarity is relative to
scalar rating systems rather than the market. The gain appears even where
no local triad evidence exists, suggesting it is due to the global propagation
of information through the dominance graph rather than the decoding of
intransitivity.

6.3. Robustness of the orthogonal-signal finding
The dominance score (Equation 3) is built from sparse head-to-head records,
so we assess its robustness to verify that the encompassing finding of Sec-
tion 6.2 does not rely on sampling noise. Table 7 reports the distribution:

                                    Page 25 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


                Table 7: Distribution of head-to-head meeting counts.

                                              Share (%)
                      Prior meetings     Pairs   Test matches
                      0                      –            58.2
                      1                   67.4            20.3
                      2                   17.8             9.7
                      3                    7.4             4.9
                      4                    3.4             2.7
                      5+                   3.9             4.1
Pairs: 24,374 unique pairs by total meetings (median 1, max 28), with no zero row as a
pair appears only once it has met. Test matches: the 12,052 test-set matches, grouped
                       by the pair’s number of prior meetings.


the median pair has met once, and 58.2% of test predictions involve players
with no prior meeting. Each match nonetheless contains many games rather
than one binary outcome. To account for dependence among those games,
we use the one-way analysis-of-variance estimator of the intraclass correla-
tion (Ridout et al., 1999), treating each match between a pair as a cluster
of game outcomes. This gives intra-match correlations of ρ = 0.0075 for
men and 0.0333 for women, comparable with the near-iid behaviour of tennis
points (Klaassen and Magnus, 2001). The larger correlation for women is
potentially due to the weaker serve dominance reported in the same study,
which leaves game outcomes less tied to the service-alternation pattern.
    By the design effect of Kish (1965), 1 + (m̄ − 1)ρ for clusters of mean size
m̄, a match of mean length effectively contains 23.0 design-effect-equivalent
games of the 27.6 played (men) and 12.8 of the 21.7 (women). Even the
shortest possible best-of-three match, a 6–0 6–0 score known as a “double
bagel”, contains 11 and 9 effective games for men and women, respectively.
The estimate may be conservative, as it attributes all variation between a
pair’s matches, including changes in form and surface, to within-match cor-
relation. The resulting effective-game counts should also be interpreted as
approximations because service alternation means that games do not have
identical win probabilities. Importantly, these counts apply only to domi-
nance within one match, as measured by the proportion of games won. They
do not show that this dominance persists across meetings, which a single
meeting cannot establish.


                                    Page 26 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


Table 8: Encompassing gain on intransitive and transitive matches as h (minimum prior
meetings per triad edge) increases.

                 h   Triads             N       ∆B          η   p-value
                 1   Intransitive    4,121   0.0012    10.7%       0.028
                     Transitive        911   0.0004     8.9%       0.371
                 2   Intransitive    1,362   0.0027    20.1%       0.012
                     Transitive      1,174   0.0009    11.6%       0.233
                 3   Intransitive     736    0.0031    27.2%       0.034
                     Transitive       630    0.0026    19.2%       0.055
                 4   Intransitive     243    0.0055    42.7%       0.037
                     Transitive       511    0.0022    19.8%       0.120
 N : matches per cell (transitive: at least one consistently ordered triad and no cycle at
  threshold h). ∆B and η (Equation 7): the combined forecast’s Brier reduction over
recalibrated WElo, and the share of the WElo-to-Pinnacle headroom it closes. p-values:
                one-sided Diebold–Mariano test of B(W+G) < B(W).


    Since a single meeting is weak evidence of a directed dominance relation,
we re-evaluate the encompassing test under stricter triad-evidence thresholds.
Table 8 increases the triad-evidence threshold h: the number of intransitive
matches shrinks, yet the encompassing gain stays significant at every h. The
gain also rises in both ∆B and η, but the same rise appears on transitive
triads, so it tracks head-to-head evidence density rather than cyclicity. The
intransitive gain is consistently larger, though the intransitive-transitive dif-
ference is not significant at any h. We do not consider h beyond four, where
the intransitive set has fallen to 243 matches, as a stricter threshold would
leave too few for a reliable test. The finding is likewise insensitive to whether
triad edges are oriented by match-, set-, or game-win majority, which agree
on the Th >0 label for 93–96% of matches.
    Since edges depend on which matches were played, we test their stability
by leaving each contributing match out in turn. The graphs entering the test
period contain 10,173 active surface-specific edges, giving 17,565 leave-one-
match-out deletions. Of these, 8,826 (50.2%) leave no directed edge, 7,903
(45.0%) retain the original direction, and 836 (4.8%) reverse it. Conditional
on an edge surviving, the direction is retained in 90.4% of cases. The high
removal rate reflects the sparse recent record, as 8,793 edges have only one


                                      Page 27 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



meeting within the 1.55-year activity window. Edges that reverse also have
smaller weights, averaging |Dns (u, v) − 0.5| = 0.036, compared with 0.113
for other multi-meeting edges. A single deletion therefore rarely reverses an
edge but removes it about half the time, so the graph’s topology is sensi-
tive to individual matches. Reversals are concentrated among near-neutral
relationships.
    Additionally, we test the stability of the intransitivity classifications by
perturbing the matches played and their game scores. We bootstrap each
pair’s match history, resampling matches with replacement 1,000 times, then
redraw the game share of each sampled match from a Beta–Binomial distri-
bution centred on the observed share and using the estimated intra-match
correlation ρ. No set structure is imposed, so the replay’s winner is the player
with the redrawn game majority. A 13–11 match has its winner reversed in
35% of redraws for men and 38% for women, while a match with the most
common best-of-three scoreline (6–3 6–4 for men and 6–3 6–2 for women) is
reversed in 13% and 8%, respectively. An intransitive match at h = 1 retains
its label in 91% of bootstrap replicates, falling to 66% at h = 4 as fewer
cyclic triads support each classification.
    For the encompassing gain itself, each replicate instead redraws every
historical match’s winner once and rebuilds every classification, with the
model’s forecasts held fixed so that variation reflects reclassification alone.
The intransitive–transitive gap is positive in 42% of replicates at h = 1
and 85% at h = 4, matching the unconfirmed difference above. The Brier
reduction on intransitive matches, however, stays positive in every one of
1,000 replicates at h = 1 (90% perturbation interval [0.0007, 0.0014], against
0.0012 observed) and in at least 99.7% of replicates at every threshold. Since
the forecasts are held fixed, this tests the stability of the classifications and
subgroup results, not the sensitivity of the model’s forecasts to the graph
itself.

6.4. Locating the complementary signal
Section 6.2 attributed the combination’s gain to global propagation through
the dominance graph rather than to the decoding of individual cycles, but
did not test the latter directly. We test it here. If the model is successfully
decoding local cycles, it should side with the head-to-head record against the
scalar favourite when the two disagree. We define a conflict as a match in
which the WElo favourite differs from the leader of the prior head-to-head
record, excluding matches with no prior meeting or a tied record.

                                    Page 28 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



    Because a scalar rating imposes a single order, it must contradict the
head-to-head record on some intransitive matchups, and conflicts concentrate
there: 98% occur on intransitive matchups, and conflicts are some four times
more common on intransitive than transitive matchups (30.6% vs 7.5%). This
association survives controls for neighbourhood size, head-to-head depth, and
tour (p < 0.001).
    On conflicts, a head-to-head direction indicator added to the WElo recal-
ibration of Equation 5 is insignificant on both the validation and test sets:
the record predicts the winner no better than WElo alone, and our model,
like the market, discounts it. The encompassing gain also disappears on the
conflict subset itself (DM p = 0.40). The complementary signal is there-
fore not local cycle-decoding but global propagation of dominance structure
across the graph: it is present even between players with no common oppo-
nents and grows on the more intransitive matchups our construction targets
(Table 8).

7. Conclusion
In this paper, we addressed the phenomenon of intransitive dominance be-
tween professional tennis players by constructing temporal directed graphs
that preserve their relationships and applying a spectral graph convolutional
network that learns directly from cyclic structure.
    Our optimised model predicts tennis match outcomes with strong out-of-
sample performance (65.7% accuracy, 0.214 Brier score) and is competitive
with existing prediction methods such as Weighted Elo (65.8%, 0.214). Al-
though the model does not improve on this baseline in accuracy, a forecast-
encompassing test shows that a combined forecast significantly improves on
Weighted Elo alone, with a Brier score of 0.211, demonstrating that our
model provides complementary information. Furthermore, the complemen-
tary signal of our model remains significant on intransitive matchups, which
embody the cyclic structure that transitive rating systems cannot represent,
though its absolute magnitude is roughly uniform across match types. This
complementary value survives stricter head-to-head evidence thresholds and
controlled reclassification of match histories.
    However, the observed complementarity has limits. The model’s overall
predictive performance still trails bookmaker odds-implied probabilities sig-
nificantly (0.214 vs 0.198 Brier score), and the approach is less interpretable
than simpler ratings such as WElo. Moreover, even on the matchups where it

                                    Page 29 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



complements rating systems, the model adds nothing to the market: combin-
ing it with Pinnacle’s odds yields no measurable Brier-score improvement, so
its complementary value is realised against transitive rating systems rather
than the market itself. Two further limitations concern the graph itself.
First, most edges rest on a single meeting. The graph is therefore sensitive
to individual matches, and one meeting cannot establish that a head-to-head
relationship persists. Second, the resampling analysis holds the model’s fore-
casts fixed, so their sensitivity to the graph is not assessed.
    Future research could explore several promising directions. Construct-
ing a more accurate measure of player-matchup intransitivity could enable
deeper investigations into how rating systems handle cyclic dominance. Since
player interactions and match histories can be encoded as graph structures, a
natural next step is to test whether graph-based methods carry similar com-
plementary value in other individual sports with strong stylistic components,
such as mixed martial arts. There is also scope for a more detailed graph
representation, given that our approach loses information when summarising
rich matchup histories into simple edge weights. A method that learns from
multiple edge attributes would be useful, and richer node features may also
help. Overall, this study has shown that graph neural networks can capture
forecasting information that transitive rating systems discard, complement-
ing established ratings rather than replacing them.

Acknowledgements
LC’s PhD is supported by a studentship from the Engineering and Physical
Sciences Research Council (EPSRC) Doctoral Training Partnership (DTP),
grant number EP/W524414/1. JC is supported by the UK Research and In-
novation (UKRI) Engineering and Physical Sciences Research Council (EP-
SRC), grant number EP/Y028392/1: AI for Collective Intelligence (AI4CI).
The authors have no conflict of interest to declare.

References
Akiba, T., Sano, S., Yanase, T., Ohta, T., Koyama, M., 2019. Optuna: A
 next-generation hyperparameter optimization framework, in: Proceedings
 of the 25th ACM SIGKDD International Conference on Knowledge Dis-
 covery & Data Mining, pp. 2623–2631. doi:10.1145/3292500.3330701.



                                    Page 30 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Angelini, G., Candila, V., De Angelis, L., 2022. Weighted Elo rating for
 tennis match predictions. European Journal of Operational Research 297,
 120–132. doi:10.1016/j.ejor.2021.04.011.

Aparício, D., Ribeiro, P., Silva, F., 2016. A subgraph-based ranking system
 for professional tennis players, in: Cherifi, H., Gonçalves, B., Menezes, R.,
 Sinatra, R. (Eds.), Complex Networks VII. Springer International Pub-
 lishing, Cham. volume 644 of Studies in Computational Intelligence, p.
 159–171. doi:10.1007/978-3-319-30569-1_12.

Arcagni, A., Candila, V., Grassi, R., 2023. A new model for predicting the
  winner in tennis based on the eigenvector centrality. Annals of Operations
  Research 325, 615–632. doi:10.1007/s10479-022-04594-7.

Bayram, F., Garbarino, D., Barla, A., 2021. Predicting tennis match out-
  comes with network analysis and machine learning, in: Bureš, T., Dondi,
  R., Gamper, J., Guerrini, G., Jurdziński, T., Pahl, C., Sikora, F., Wong,
  P.W. (Eds.), SOFSEM 2021: Theory and Practice of Computer Science,
  Springer International Publishing, Cham. p. 505–518. doi:10.1007/978-
  3-030-67731-2_37.

Boshnakov, G., Kharrat, T., McHale, I.G., 2017. A bivariate Weibull count
  model for forecasting association football scores. International Journal of
  Forecasting 33(2), 458–466. doi:10.1016/j.ijforecast.2016.11.006.

Bozóki, S., Csató, L., Temesi, J., 2016. An application of incomplete pairwise
  comparison matrices for ranking top tennis players. European Journal of
  Operational Research 248, 211–218. doi:10.1016/j.ejor.2015.06.069.

Bradley, R.A., Terry, M.E., 1952. Rank analysis of incomplete block designs:
  I. The method of paired comparisons. Biometrika 39, 324–345. doi:10.
  2307/2334029.

Brier, G.W., 1950. Verification of forecasts expressed in terms of probability.
  Monthly weather review 78, 1–3. URL: https://doi.org/10.1175/1520-
  0493(1950)078<0001:VOFEIT>2.0.CO;2.

Brin, S., Page, L., 1998. The anatomy of a large-scale hypertextual Web
  search engine. Computer Networks and ISDN Systems 30, 107–117. doi:10.
  1016/S0169-7552(98)00110-X.


                                    Page 31 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Buchdahl, J., 2016. Squares & Sharps, Suckers & Sharks: The Science,
  Psychology & Philosophy of Gambling. High Stakes, London.

Buhamra, N., Groll, A., Brunner, S., 2024. Modeling and prediction of tennis
  matches at Grand Slam tournaments. Journal of Sports Analytics 10, 17–
  33. doi:10.3233/JSA-240670.

Chong, Y.Y., Hendry, D.F., 1986. Econometric evaluation of linear macro-
  economic models. The Review of Economic Studies 53, 671–690.

Clarke, S., Dyte, D., 2000. Using official ratings to simulate major ten-
  nis tournaments. International Transactions in Operational Research 7,
  585–594. doi:10.1111/j.1475-3995.2000.tb00218.x.

Clegg, L.W., Cartlidge, J.P., 2025.    Tennis match outcome predic-
  tion using temporal directed graph neural networks, in: 11th In-
  ternational Conference on Mathematics in Sport (MathSport Interna-
  tional), pp. 50–56. URL: https://www.mathsportinternational.com/
  MathSport2025Proceedings.pdf.

Deb, K., Pratap, A., Agarwal, S., Meyarivan, T., 2002. A fast and elitist
  multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolu-
  tionary Computation 6, 182–197. doi:10.1109/4235.996017.

Defferrard, M., Bresson, X., Vandergheynst, P., 2016. Convolutional neural
  networks on graphs with fast localized spectral filtering. Advances in neural
  information processing systems 29.

Diebold, F.X., Mariano, R.S., 2002. Comparing predictive accuracy. Journal
  of Business & economic statistics 20, 134–144.

Dingle, N., Knottenbelt, W., Spanias, D., 2013. On the (page) ranking of
  professional tennis players, in: Tribastone, M., Gilmore, S. (Eds.), Com-
  puter Performance Engineering, Springer, Berlin, Heidelberg. p. 237–247.
  doi:10.1007/978-3-642-36781-6_17.

Dixon, M.J., Coles, S.G., 1997. Modelling association football scores and
  inefficiencies in the football betting market. Journal of the Royal Statistical
  Society: Series C (Applied Statistics) 46, 265–280. doi:10.1111/1467-
  9876.00065.


                                    Page 32 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Elo, A.E., Sloan, S., 1978. The rating of chessplayers: Past and present.
  ARCO Publishing, New York, USA.

Epasinghege Dona, N., Gill, P.S., Swartz, T.B., 2025. What does rally
  length tell us about player characteristics in tennis?   Journal of the
  Royal Statistical Society Series A: Statistics in Society 188, 188–204.
  doi:10.1093/jrsssa/qnae027.

Fayomi, A., Majeed, R., Algarni, A., Akhtar, S., Jamal, F., Nasir, J.A.,
  2022. Forecasting tennis match results using the Bradley-Terry model.
  International Journal of Photoenergy 2022, 1898132. doi:10.1155/2022/
  1898132.

Ferro, C.A.T., Fricker, T.E., 2012. A bias-corrected decomposition of the
  Brier score. Quarterly Journal of the Royal Meteorological Society 138,
  1954–1960. doi:10.1002/qj.1924.

Giacomini, R., White, H., 2006. Tests of conditional predictive ability. Econo-
  metrica 74, 1545–1578.

Gollub, J., 2021. Forecasting serve performance in professional tennis
 matches. Journal of Sports Analytics 7, 223–233. doi:10.3233/JSA-
 200345.

Granger, C.W., Ramanathan, R., 1984. Improved methods of combining
  forecasts. Journal of forecasting 3, 197–204.

Hamilton, A.H., Kalenkova, A., Roughan, M., 2025. The impact of intransi-
  tivity on the Elo rating system. PLOS ONE 20, e0338261. doi:10.1371/
  journal.pone.0338261.

He, Y., Gan, Q., Wipf, D., Reinert, G.D., Yan, J., Cucuringu, M., 2022.
  GNNrank: Learning global rankings from pairwise comparisons via di-
  rected graph neural networks, in: International Conference on Machine
  Learning, PMLR. pp. 8581–8612. URL: https://proceedings.mlr.
  press/v162/he22b/he22b.pdf.

He, Y., Zhang, X., Huang, J., Rozemberczki, B., Cucuringu, M., Rein-
  ert, G., 2024. PyTorch geometric signed directed: A software package
  on graph neural networks for signed and directed graphs, in: Learning


                                    Page 33 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



  on Graphs Conference (LoG), PMLR. URL: https://proceedings.mlr.
  press/v231/he24a/he24a.pdf.

Hegarty, T., Whelan, K., 2025. Forecasting soccer matches with betting
  odds: A tale of two markets. International Journal of Forecasting 41(2),
  803–820. doi:10.1016/j.ijforecast.2024.06.013.

Ingram, M., 2019. A point-based Bayesian hierarchical model to predict the
  outcome of tennis matches. Journal of Quantitative Analysis in Sports 15,
  313–325. doi:10.1515/jqas-2018-0008.

Kendall, M.G., Babington Smith, B., 1940. On the method of paired com-
  parisons. Biometrika 31, 324–345. doi:10.2307/2332613.

Kish, L., 1965. Survey sampling. John Wiley & Sons, New York, USA.

Klaassen, F.J., Magnus, J.R., 2001. Are points in tennis independent and
  identically distributed? evidence from a dynamic binary panel data model.
  Journal of the American Statistical Association 96, 500–509. doi:10.1198/
  016214501753168217.

Klaassen, F.J., Magnus, J.R., 2003. Forecasting the winner of a tennis match.
  European Journal of Operational Research 148(2), 257–267. doi:10.1016/
  S0377-2217(02)00682-3.

Kovalchik, S., 2020. Extension of the Elo rating system to margin of victory.
  International Journal of Forecasting 36(4), 1329–1341. doi:10.1016/j.
  ijforecast.2020.01.006.

Kovalchik, S.A., 2016. Searching for the GOAT of tennis win prediction.
  Journal of Quantitative Analysis in Sports 12, 127–138. doi:10.1515/
  jqas-2015-0059.

Leitner, C., Zeileis, A., Hornik, K., 2009. Is Federer stronger in a tournament
  without Nadal? An evaluation of odds and seedings for Wimbledon 2009.
  Austrian Journal of Statistics 38(4), 277–286. doi:10.17713/ajs.v38i4.
  280.

Longa, A., Lachi, V., Santin, G., Bianchini, M., Lepri, B., Lio, P., Scarselli,
  F., Passerini, A., 2023. Graph neural networks for temporal graphs:
  State of the art, open challenges, and opportunities. Transactions on

                                    Page 34 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



  Machine Learning Research URL: https://openreview.net/forum?id=
  pHCdMat0gI.

Maystre, L., Grossglauser, M., 2015. Fast and accurate inference of plackett–
 luce models. Advances in neural information processing systems 28.

McHale, I., Morton, A., 2011. A Bradley-Terry type model for forecasting
 tennis match results. International Journal of Forecasting 27(2), 619–630.
 doi:10.1016/j.ijforecast.2010.04.004.

Mirzaei, A., 2022. Sports match outcome prediction with graph rep-
 resentation learning. Master’s thesis. School of Computing Science,
 Simon Fraser University, CA, USA. URL: https://summit.sfu.ca/
 _flysystem/fedora/2022-08/input_data/22492/etd21919.pdf.

Morris, B., Bialik, C., 2015. Serena Williams and the difference be-
 tween all-time great and greatest of all time. FiveThirtyEight. URL:
 http://fivethirtyeight.com/features/serena-williams-and-the-
 difference-between-all-time-great-and-greatest-of-all-time.
 accessed: 2025-04-03.

Murphy, A.H., 1973. A new vector partition of the probability score. Jour-
 nal of Applied Meteorology 12, 595–600. doi:10.1175/1520-0450(1973)
 012<0595:ANVPOT>2.0.CO;2.

O’Malley, A.J., 2008. Probability formulas and statistical analysis in tennis.
  Journal of Quantitative Analysis in Sports 4(2). doi:10.2202/1559-0410.
  1100.

van Ours, J.C., 2025. Non-transitive patterns in sports match outcomes: A
  profitable anomaly. Empirical Economics 69(4). doi:https://doi.org/
  10.1007/s00181-025-02838-6.

Peiris, B., Epasinghege Dona, N., Swartz, T.B., 2025. Analysis of the impact
  of unforced errors in tennis. International Journal of Sports Science &
  Coaching doi:10.1177/17479541251333943.

Radicchi, F., 2011. Who is the best player ever? A complex network analysis
  of the history of professional tennis. PLOS ONE 6(2), e17249. doi:10.
  1371/journal.pone.0017249.


                                    Page 35 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Ridout, M.S., Demétrio, C.G.B., Firth, D., 1999. Estimating intraclass cor-
  relation for binary data. Biometrics 55, 137–148. doi:10.1111/j.0006-
  341X.1999.00137.x.

Shin, H.S., 1993. Measuring the incidence of insider trading in a market
  for state-contingent claims. The Economic Journal 103(420), 1141–1153.
  doi:10.2307/2234240.

Shizuka, D., McDonald, D.B., 2012. A social network perspective on mea-
  surements of dominance hierarchies. Animal Behaviour 83, 925–934.
  doi:10.1016/j.anbehav.2012.01.011.

Tea, P., Swartz, T.B., 2023. The analysis of serve decisions in tennis using
  bayesian hierarchical models. Annals of Operations Research 325, 633–648.

Temesi, J., 2019. An interactive approach to determine the elements of
  a pairwise comparison matrix. Central European Journal of Operations
  Research 27, 533–549. doi:10.1007/s10100-018-0539-6.

Wilkens, S., 2021. Sports prediction and betting models in the machine
 learning age: The case of tennis. Journal of Sports Analytics 7, 99–117.
 doi:10.3233/JSA-200463.

Xenopoulos, P., Silva, C., 2021. Graph neural networks to predict sports
  outcomes, in: 2021 IEEE International Conference on Big Data (Big Data),
  IEEE. pp. 1757–1763. doi:10.1109/BigData52589.2021.9671833.

Zhang, X., He, Y., Brugnone, N., Perlmutter, M., Hirn, M., 2021. MagNet:
  A neural network for directed graphs, in: International Conference on
  Neural Information Processing Systems, pp. 27003–27015. URL: https:
  //dl.acm.org/doi/10.5555/3540261.3542329.

Štrumbelj, E., 2014. On determining probability forecasts from betting
  odds. International Journal of Forecasting 30, 934–943. doi:10.1016/
  j.ijforecast.2014.02.008.




                                    Page 36 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



Appendix A. Mathematical Details of MagNet
This appendix provides the complete mathematical formulation of the Mag-
Net architecture used in Section 4.2. For clarity, we omit the court surface
and snapshot notation, but the following applies independently to each tem-
poral surface-graph. We also follow standard notation where bold uppercase
letters (e.g., A) denote matrices and bold lowercase letters (e.g., x) denote
vectors.
    Given a static directed graph G = (V, E, XV , W ), we denote its adjacency
matrix as A ∈ R|V |×|V | , where A(u, v) = wuv if an edge (u, v) ∈ E exists
indicating player u has historically dominated player v, and 0 otherwise.
First, we compute the symmetrised adjacency matrix As and the diagonal
degree matrix D s , defined as

                 1                                          X
      As (u, v) = (A(u, v) + A(v, u)),        Ds (u, u) =       As (u, v).      (A.1)
                 2                                          v

   To preserve the directional information representing head-to-head domi-
nance between players, the phase encoding matrix Θ(q) is calculated as:

                       Θ(q) (u, v) = 2πq(A(u, v) − A(v, u))                     (A.2)
where q ∈ [0, 0.25] is a tunable hyperparameter that controls the extent to
which directional information is incorporated. When q = 0, the model dis-
regards which player has historically dominated the head-to-head matchups,
whereas at q = 0.25, this dominance information is maximally integrated.
   For improved numerical stability during training, we use the normalised
formulation of the magnetic Laplacian, which is defined as:
                      (q)
                    LN = I − D −1/2
                               s    As D −1/2
                                         s    ⊙ exp(iΘ(q) )                     (A.3)
The normalised magnetic Laplacian is a complex Hermitian matrix, which
guarantees real eigenvalues, thus resolving the challenges posed by asymmet-
ric adjacency matrices. This complex-valued representation captures both
the existence of head-to-head history between players in the magnitude of
its entries and the directional dominance pattern in their phase. For player
pairs with no prior matches, the corresponding entries remain zero.
    To address the computationally expensive eigendecomposition of the La-
placian, MagNet implements the spectral filtering approach based on Cheby-
shev polynomial approximation, as introduced by Defferrard et al. (2016). As

                                    Page 37 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



the eigenvalues of the normalised magnetic Laplacian lie in the range [0, 2],
the Laplacian is first rescaled to have eigenvalues in the range [−1, 1] for the
Chebyshev approximation:
                                        2       (q)
                                L̃ =          LN − I                            (A.4)
                                       λmax
                                                (q)
where λmax is the largest eigenvalue of LN . The parameter K in the Cheby-
shev approximation corresponds to the order of the polynomial, defining the
filter’s receptive field as the K-hop neighbourhood of each node. The result-
ing filters aggregate information from nodes within K hops, considering both
incoming and outgoing edges. The phase of the Laplacian’s entries, which
encodes edge direction, allows the filter to process information from these
two neighbourhoods distinctly. The filters act on node features x as follows:
                                       K
                                       X
                               Yx=            θk Tk (L̃)x                       (A.5)
                                       k=0

where θk are the learnable filter parameters and Tk are the Chebyshev poly-
nomials of the first kind.
   These filters operate across multiple layers of the network. When L layers
are stacked, the effective receptive field expands to L × K hops, allowing
the model to aggregate information from increasingly distant players in the
network. The multi-layer operation follows:
                                     Fℓ−1
                                                    !
                            (ℓ)
                                     X (ℓ) (ℓ−1)
                           xj = σ         Y ij xi                       (A.6)
                                        i=1

        (ℓ)
where xj is the j-th feature channel at layer ℓ, σ is a complex ReLU ac-
                                                                            (ℓ)
tivation function, Fℓ−1 is the number of input channels to layer ℓ, and Y ij
represents the convolution matrices implementing the spectral filters between
the i-th input channel and the j-th output channel. After the final convolu-
tional layer, the complex-valued node embeddings for all players are collected
in the matrix X (L) ∈ C|V |×FL . To obtain real-valued node representations
hu , hv ∈ R2FL , the matrix is unwound into real-valued features by separating
real and imaginary parts into a matrix R|V |×2FL . Edge features are extracted
by concatenating the unwound node embeddings for each player pair (u, v),
resulting in edge representation euv = [hu ; hv ] ∈ R4FL .


                                    Page 38 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



    The final prediction layer applies a linear transformation followed by soft-
max activation to produce an order-dependent probability vector for a given
player pair, representing the estimated probability associated with the di-
rected edge from u to v (indicating player u’s dominance over v):

                         ẑuv = softmax(W[hu ; hv ] + b)                        (A.7)
where hu and hv are the node embeddings from the final layer, [hu ; hv ] repre-
sents their concatenation, and W ∈ R2×4FL and b ∈ R2 are learnable weight
and bias terms.
     To mitigate the impact of player ordering (u, v) on probability estimates
and to ensure a balanced prediction, we average the model outputs from both
directed perspectives. The final set-win probability for player u, denoted p̂uv ,
is defined as:
                                   1
                            p̂uv = ((ẑuv )1 + (ẑvu )2 )                   (A.8)
                                   2
where (·)1 refers to the first component of the probability vector (i.e., the
probability of the first player in the input pair winning) and (·)2 refers to the
second. This averaging ensures that the model’s predictions are consistent
regardless of player order and that the resulting probabilities sum to one,
i.e., p̂uv + p̂vu = 1.

Appendix B. Extended Initial Model
In earlier work (Clegg and Cartlidge, 2025) we proposed an unoptimised
temporal graph model with a less sophisticated graph structure for the same
task of tennis forecasting. To evaluate the robustness of this unoptimised
approach, we increased the out-of-sample dataset to cover the period 31
October 2023 to 8 June 2025. By incorporating 844 additional matches, the
total out-of-sample test set increased in size to 1,918 professional matches
across both the original period (31 October 2023 to 8 September 2024) and
the extended period (9 September 2024 to 8 June 2025). The dataset differs
from the one we use here in that it only considers men’s matches and excludes
any 500-point matches other than the Halle Open and the Queen’s Club
Championships.
    The initial implementation of temporal graph neural networks for tennis
forecasting also differs in several key aspects from the model presented in our
current work. Specifically, the graph edge weights are constructed with a time
decay parameter of λ = 0.01, and there is no cross-surface graph updating.

                                    Page 39 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting


      Table B.9: Model Performance Comparison By Surface: Extended Dataset.

                            Count         Accuracy           Brier
              Dataset      MS       E     MS         E     MS        E
              Clay         314    681   0.675   0.649    0.216   0.226
              Grass        169    169   0.710   0.710    0.209   0.209
              Hard         591   1068   0.638   0.624    0.221   0.228
              All         1074   1918   0.660   0.640    0.218   0.226
               * Notes.  MS refers to results presented in Clegg and
                 Cartlidge (2025) E refers to results from using the
                 same methodology but with an extended dataset.
                 While the original results used a dataset spanning
                 31 October 2023 to 8 September 2024, the extended
                 dataset covers 31 October 2023 to 8 June 2025. All
                 metrics rounded to three decimal places.


This extension provides further justification for the proper hyperparameter
tuning and improved graph structure in this work.
    In Table B.9, the results from the original out-of-sample test set are shown
along with results when including the 844 additional matches. The unopti-
mised model achieves an overall classification accuracy of 64.0% and a Brier
score of 0.226, representing a decline from the original model’s performance
of 66.0% accuracy and 0.218 Brier score. This deterioration is consistent
across most performance metrics and surfaces, with the exception of grass
courts, since there were no additional matches on grass. The difference is
most pronounced on clay courts, where accuracy drops from 67.5% to 64.9%,
with hard court performance declining from 63.8% to 62.4%.
    We attribute the performance deterioration to several methodological dif-
ferences. First, the dramatically different time decay parameter (λ = 0.01
vs λ = 0.34) significantly alters how historical match information influences
current predictions, causing the graph to retain excessive influence from out-
dated match results that may no longer reflect current player form.
    Second, the exclusion of 500-point tournaments reduces the graph den-
sity and available training information, particularly affecting predictions of
players who compete primarily at these lower-tier events. Finally, the restric-
tion of cross-surface information flow prevents the model from consistently
learning across the year. This is most pronounced with grass tournaments,

                                    Page 40 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



which necessitated the selective inclusion in the original work of the Halle
Open and the Queen’s Club Championships as a partial remediation.
   The performance of the initial model with the extended dataset highlights
the importance of our improved approach, with systematic hyperparameter
optimisation and complete graph construction.

Appendix C. Cardinal Intransitivity Measure
Section 6.1 pairs the model-free raw-triad count with a cardinal measure, the
evidence-weighted intransitivity I ∗ (Auv ), whose construction we give here. It
adapts the Hodge-decomposition measure of Hamilton et al. (2025) to each
match’s common-opponent neighbourhood. For players u and v, the common
opponents are those who have faced both before snapshot n:

                  Cuv = {c ∈ V : (u, c) ∈ En and (v, c) ∈ En }.                 (C.1)

We extract the (|Cuv | + 2) × (|Cuv | + 2) subgraph Guv on {u, v} ∪ Cuv and form
the advantage matrix Auv by a logit transform,
                                                     
                                                wab
                          Auv [a, b] = log              ,                  (C.2)
                                              1 − wab
where wab is the dominance score of player a over player b within the neigh-
bourhood, clipped 10−6 away from 0 and 1 so the transform cannot di-
verge. This maps bounded dominance scores [0, 1] to unbounded advan-
tages (−∞, +∞). Because wba = 1 − wab , the transform is antisymmetric
(Auv [b, a] = −Auv [a, b]), as the Hodge decomposition requires. The decompo-
sition separates Auv into a transitive component grad ◦ div(Auv ) and a cyclic
remainder. Hamilton et al. (2025) measure intransitivity as the ratio
                               1 + ∥Auv − grad ◦ div(Auv )∥F
                   I(Auv ) =                                 ,                  (C.3)
                                  1 + ∥grad ◦ div(Auv )∥F
which equals one when the cyclic and transitive components have equal mag-
nitude, with values above one marking predominantly cyclic neighbourhoods.
Equation C.3 scores a whole neighbourhood uniformly, whereas we need a
matchup-specific quantity, so we scale it by the accumulated evidence weight
for (u, v):                               sX
                      ∗
                     I (Auv ) = I(Auv ) ·      αs,sk βk ϕk ,           (C.4)
                                                k


                                    Page 41 of 42
Accepted manuscript: Clegg and Cartlidge (2027), International Journal of Forecasting



where the sum ranges over all matches k between u and v before snapshot n,
matching the denominator of Equation 3. The accumulated weight captures
evidence from match recency, tournament prestige, and surface correlations,
with square-root scaling moderating highly-weighted matchups. Because I ∗
is built from the model’s dominance scores, it is descriptive only and enters
none of the forecast-comparison tests, which bin on the model-free Th . Its
stability under shrinkage of those scores is established in Appendix D.

Appendix D. Robustness of Dominance Scores
A potential concern with the dominance score Dns (u, v) (Equation 3) is esti-
mation error arising from sparse head-to-head records. We assess this with
Bayesian shrinkage at two levels.
    Firstly, we shrink each pair’s pooled empirical game share towards 0.5
using its Beta(α, α) posterior mean, with prior strengths α ∈ {1, 3, 5}. Across
the 17,364 pairwise head-to-head records observed before the test period, the
Kendall τ between empirical and shrunken shares is 0.99 at α = 1 and 0.96
at α = 5.
    Secondly, we shrink Dns (u, v) directly towards 0.5 by adding 2α pseudo-
observations of an even game share. At α = 1, the original and shrunken
rankings by dominance strength (distance from 0.5) have Kendall τ = 0.64.
Being symmetric, this shrinkage cannot reverse an edge, so sensitivity of
edge direction to the underlying record is assessed by the leave-one-match-
out analysis of Section 6.3.
    Because I ∗ (Auv ) is derived from the dominance scores, we also recompute
it from the shrunken scores while retaining the observed evidence weights.
Its ranking remains stable across all prior strengths (Spearman ρ ≥ 0.94,
Kendall τ ≥ 0.79), with no match changing its I ∗ > 0 status, indicating that
the descriptive results for I ∗ (Auv ) in Section 6.1 are not artefacts of unstable
estimates.




                                    Page 42 of 42
