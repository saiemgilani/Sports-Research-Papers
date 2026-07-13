<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2025/2025 - Identifying playing styles in football using topic modeling - Misuric-Ramljak et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

### **Research Article** 

Vanja Misuric-Ramljak and Michel van de Velden* 

# **Identifying playing styles in football using topic modeling** 

https://doi.org/10.1515/jqas-2025-0154 Received September 30, 2025; accepted April 30, 2026; published online June 1, 2026 

**Abstract:** Football clubs analyze large amounts of data in an attempt to improve their performance and gain a competitive advantage over rivals. Several attempts have been made in formulating, detecting, and measuring team-based indicators. One team-based indicator popular with football analysts and managers, is a so-called playing style. Analysts at all levels of the game regularly use the term playing style to better understand the complexity of football matches and team tactics. A formal definition, let alone a proper quantification, of a playing style is typically not provided. In this paper, we introduce a method for quantifying a team’s playing style based on match event data. In particular, we define playing styles based on the location and patterns of a team’s consecutive actions with the ball. Specifically, we apply Latent Dirichlet allocation to ball movement patterns to obtain distributions over such ball movement patterns with similar structure; that is, the playing styles. Using our method, a team’s playing style is represented by a “style” vector, that summarizes the playing style in an interpretable way. We apply our methodology to a publicly available data set, and illustrate how the resulting playing styles can be used in practice. 

**Keywords:** soccer; cluster analysis; topic models; playing style 

## **1 Introduction** 

In the competitive and constantly evolving world of modern football, data analytics has become increasingly popular over recent years (Davis et al. 2024; Herberger and Litke 2021). Football clubs analyze large amounts of data in an 

***Corresponding author: Michel van de Velden** , Econometric Institute, Erasmus School of Economics, Erasmus University Rotterdam, Rotterdam, the Netherlands, E-mail: vandevelden@ese.eur.nl **Vanja Misuric-Ramljak** , Econometric Institute, Erasmus School of Economics, Erasmus University Rotterdam, Rotterdam, the Netherlands 

attempt to improve their performance and gain a competitive advantage over rivals. As a result, many models have been developed to evaluate the quality of actions and players (Bransen et al. 2019; Pulis and Bajada 2022; Van Roy et al. 2021). Less emphasis, however, has been placed on formulating, detecting, and measuring _team-based_ indicators. That is, indicators that do not focus on actions by individual players, but that relate to patterns of a team. One team-based indicator that is often mentioned by football analysts and managers, is a _playing style_ . Analysts at all levels of the game regularly use the term playing style to better understand the complexity of football matches and team tactics. However, a formal definition, let alone a proper quantification, of a playing style is typically not provided. 

From a club’s perspective, understanding playing styles may be essential for several practical cases. For example, having a better understanding of your opponents’ playing style may allow for better match preparations and can thus improve match performance. Furthermore, insights in playing style allows for improved player and manager acquisition by realizing a better fit. In addition, the evolution of a team’s playing style over time, could provide valuable information concerning individual as well as team developments over time. 

Popular sports media often provide narratives on playing style based on basic historical and cultural experiences (e.g., English kick-and-rush, Italian catenaccio, Spanish tiki-taka, etc.) or by considering simple aggregated metrics (e.g., percentages of possession, number of passes etc.). The coaching staff at high-level football teams, however, may obtain deeper insights by performing video analyses. The former approach can provide narratives that are easy to understand but that are usually inadequate at capturing actual playing styles (Decroos et al. 2021). The latter approach, allows for a more detailed analysis but is a time-consuming process, considering the large amount of matches from teams across several leagues and seasons. Moreover, such analyses may lean quite heavily on subjective evaluations of a small number of experts. It would be beneficial to have a method that characterizes playing style in a more objective and verifiable manner. 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football 

In existing work on playing style quantification, playing styles are modelled using various observable factors such as team formations, attacking patterns, passing tendencies or network statistics (Bialkowski et al. 2014; Decroos et al. 2018; Palazzo et al. 2023). However, since playing style is a subjective concept with no verifiable ground truth attached to it, no single modeling approach has been widely accepted. There remains a need to characterize playing style in a way that is better applicable for football teams (Plakias et al. 2023). 

In this paper, we introduce a method for quantifying a team’s playing style based on match event data. In particular, we define playing styles based on the location and patterns of a team’s consecutive actions with the ball. Using our method, a team’s playing style is represented by a “style” vector, that summarizes the playing style in a way that is both interpretable and suitable for further data analysis. 

Characterizing playing style from match event data is challenging as such data are complex and high-dimensional. Match event data involve player locations, their movements, and the actions they perform. We deal with these challenges by first constructing ball movement patterns, which are sequences of coordinated actions involving the ball. Using these ball movement patterns, we identify playing styles by adapting methodology from the field of text analytics. Specifically, we apply latent Dirichlet allocation (Blei et al. 2003) to ball movement patterns to obtain distributions over such ball movement patterns with similar structure; that is, the playing styles. We apply our methodology to a publicly available data set, and show how the resulting playing styles can be used in practice. 

## **2 Related work** 

Developing objective insights into a team’s playing style is no easy task, since it is an inherently subjective concept. As a result, no single modeling approach has been widely accepted. Previous papers have suggested that playing style is connected to where on the pitch a team tends to carry out certain types of actions (Decroos et al. 2021; Fernandez-Navarro et al. 2016). During matches, players perform certain sequences of actions with the ball, and these can be considered to reflect a team’s playing style. Consequently, playing style can be identified by utilizing part of the information present in match event data. One approach, for example, is to divide the pitch into zones and consider count data related to actions in these zones (Brooks et al. 2016; Clijmans et al. 2022). The selection of the number of zones and their sizes directly impacts the retrieved playing styles 

in such analysis. In addition, the strict boundaries between zones can make spatially similar actions appear dissimilar. 

Since passes are the most performed actions in football matches, sports analytics researchers have explored different ways of using passes to characterize playing style. For example, Gyarmati et al. (2014) and Bekkers and Dabadghao (2019) focus on the underlying structure of passing sequences to find similarities and differences between teams’ playing style. They characterize the different passing structures by flow motifs; an ordered list of players connected by three consecutive passes, where players are represented by labels. The analysis of a team’s usage of different motifs allows them to compare and differentiate the passing styles of different teams. In Malqui et al. (2019), the concept of flow motifs was extended by incorporating the spatial component of passes when categorizing motifs. 

In contrast to modeling passing sequences as flow motifs, Cintia et al. (2015) apply a network based approach on passing sequences incorporating both the involved players and the spatial component of passes. Modeling the passes between players and zones on the pitch as a network helps in understanding where a team prefers to play and whether they utilize long or short passes. 

For our approach, we use passing sequences together with their spatial components, that is, where the sequences occur on the field, to identify playing styles. In particular, we consider all possession sequences (i.e., passes and actions with the ball where a team remains in possession) and cluster them into a large set of “movement patterns”. Then, by observing, for all matches, distributions over these patterns, we obtain passing profiles. We define a playing style as a consistent, stable, distribution over the movement patterns. 

## **3 Methodology** 

In this section, we present a framework to extract playing styles from match event data. That is, data for all actions involving the ball, that occurred on the pitch during matches. More specifically, our method requires data on the player who performed the action, the type of action (passes, shots, and interceptions), the start and end locations of the action (i.e., the ( _x_ , _y_ )-coordinates), and the timestamp of the action in the match. Note that this type of data is collected for virtually all professional football matches in the major leagues. The data are shared among professional teams and/or can be purchased (Stats Perform 2020). Using this type of match event data, we propose a sequential 

V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football **— 3** 

procedure to identify a team’s playing style, consisting of the following three steps: 

- (1) **Create ball movement chains** : Extract uninterrupted sequences of events where one team remains in possession of the ball. Then cut these possession sequences into sequences that describe four consecutive player involvements. The resulting sequences are referred to as ball movement chains. 

- (2) **Identify ball movement patterns** : Cluster spatially similar ball movement chains and assign each ball movement chain to the appropriate (nearest) cluster. The resulting clusters are referred to as ball movement patterns. 

- (3) **Characterize playing styles** : For each match and team, derive the distributions over the ball movement patterns. Apply Latent Dirichlet allocation to these distributions to extract playing styles, where playing styles correspond to similar distributions over ball movement patterns. 

In the following subsections, we go over these three steps in more detail. 

### **3.1 Creating ball movement chains** 

Each match can be represented as a sequence of consecutive actions performed by both teams. A match _M_ can therefore be denoted by _M_ = [ _a_ 1 _,_ … _, an_ ], where each _ai_ is an action and _n_ is the total number of actions in that match. The manner in which a team plays is manifested through consecutive sequences of coordinated actions on the pitch. For example, a team may tend to attack through the centre of the pitch, or move the ball quickly from one flank to the other flank. Therefore, we represent a match by considering the _possession sequences_ of both teams, where we define a possession sequence _Si_ as an uninterrupted sequence of actions where one team is in possession of the ball. A match _M_ can then be represented as _M_ = [ _S_ 1 _,_ … _, Sm_ ], where _m_ denotes the total number of possession sequences. Each possession sequence _Si_ = _ai_ 1 _,_ … _, ais_ is a sub-sequence of consecutive actions performed by a team in a match. 

A new possession sequence starts when there is a pause of at least 10 s between actions, there is a stoppage in play (e.g., the ball goes out of play or the referee stops the game) or when possession switches from one team to the other. We exclude sequences that started due to set pieces. Set pieces tend to be performed by set piece specialists and often involve custom tactics that are beyond the scope of this work. 

Possession sequences may vary in length and complexity. The shortest possession sequence consists of just two actions, while the longest sequence may exceed 60 actions. Possession sequences that are too short or too long are usually not very informative of the playing style of a team. To account for the differences in length and complexity, we define ball movement chains as sequences of four consecutive player involvements. This choice follows the _movement-chains_ convention used by Stats Perform (Opta), where defining chains as four consecutive player involvements is motivated as a practical restriction that reduces complexity for downstream analysis (Whitmore 2020). Beyond this convention, we found that a chain length of four provides a reasonable trade-off between the amount of information contained per ball movement chain and the number of ball movement chains per match. Ball movement chains that are too short (e.g., 2 to 3 player involvements) tend to capture simple exchanges that are less diagnostic of team style, while chains that are too long become mixtures of several patterns, increasing sparsity and making comparisons between styles less interpretable. Furthermore, we exclude ball movement chains that begin and end in a team’s own penalty area, begin in the opponent’s penalty area and end outside of it, or contain a clearance action. Ball movement chains that belong to one of these three situations are likely to be executed out of necessity rather than as a reflection of playing style. Figure 1 shows a possession sequence that is split into two ball movement chains. Note that the same player can appear more than once within a sequence. (For example, in Figure 1, Player 1 and Player 3 could be the same player). Furthermore, as illustrated in Figure 1 individual players can perform more than one action with the ball, and possession sequences may contain multiple overlapping ball movement chains. 

### **3.2 Identifying ball movement patterns** 

The ball movement chains defined in the previous subsection, provide a standardized way of looking at a team’s possession sequences. However, although each ball movement chain is probably unique (as locations are used, it is unlikely that the exact same chain is observed twice), we can expect several chains to be similar. To further reduce the granularity of the data, we group similar chains into _ball movement patterns_ . The ball movement patterns should be constructed in such a way that they adequately describe all observed ball movement chains. To achieve this, we first cluster spatially similar ball movement chains so that the resulting clusters of sequences sufficiently capture overall 

> **4 —** V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football 



**Figure 1:** Creating ball movement chains from possession sequences. 

variation in the sequences. Next, we define _ball movement patterns_ as the representative ball movement chains of each cluster. 

For the clustering of ball movement chains, we use _k_ -medoids clustering (Rousseeuw and Kaufman 1987) as implemented in the kmedoids Python package (Schubert and Lenssen 2022). _K_ -medoids is a variant of _k_ -means (Hartigan and Wong 1979) cluster analysis, where each cluster is identified through a representative (i.e., the medoid) point. Hence, observations are clustered in such a way that the overall distance of points to their respective cluster medoid is as small as possible. The resulting medoids correspond to actual observations and can be seen as points best representing the clusters (Park and Jun 2009). We refer to these medoids as the ball movement patterns. _K_ -medoids clustering can be used with any distance measure. For our purposes, the distance measure must meet two requirements. First, it must be able to identify similar ball movement chains on the basis of spatial characteristics. Second, it must be able to deal with ball movement chains of varying lengths. A distance function that satisfies both requirements is dynamic time warping (DTW) (Müller 2007). In our implementation, each ball movement chain is represented as an _ordered_ sequence of event locations, i.e., {( _xi, yi_ )}<sup>_n_</sup> _i_ =1<sup>,where</sup> the index _i_ follows the sequential order of actions within the chain. DTW is applied directly to these discrete event locations. DTW computes an optimal one-to-many alignment between two sequences, which allows for small mismatches in the placement of intermediate actions while preserving similarity in the overall spatial path. To calculate the DTW distances, we use a custom Python implementation based on code described in Tavenard (2021). 

To decide on an appropriate number of clusters (i.e., a number of ball movement patterns), it is important to note that this number should be large enough to capture variation in the observed patterns whilst at the same time being small enough to distinguish and interpret general patterns (playing styles). For our setting, we propose a cluster validity measure, inspired by the approach in Meza (2017), based on team stability. The general idea of this method is that when, for a certain team, one considers the observed ball movement patterns over matches, the distribution over the _k_ ball movement patterns is similar. Hence, if the number of ball movement patterns is too small (or too large) the clusters are too general (or too specific) and the distributions over matches differ. 

We propose an algorithm that evaluates the stability of a given number of medoids _k_ by measuring whether team’s cluster assignments are consistent across random partitions of their matches. First, for each candidate _k_ , we perform _k_ −medoids cluster analyses on _R_ random samples of the data. For each sample, we consider _S_ random splits of each team’s match set into two halves ( _A_ and _B_ ), we compute the normalized distribution over the _k_ clusters for each set, and compare each team’s _A_ -distribution to its own _B_ -distribution using the total variation distance (Gibbs and Su 2002). Averaging results over all _R_ trials yields a final similarity score. A high (i.e., close to 1) similarity score indicates that _k_ ball movement patterns effectively distinguish teams based on the ball movement chains they used. By plotting the similarity scores for different values of _k_ , a choice can be made leveraging complexity versus stability. We summarized this approach in Algorithm 1. 

V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football **— 5** 

**Algorithm ** Stability evaluation of _k_ -medoids clustering 

|1. Set complete set of ball movement chains , maximum cluster<br>size _K_ max , number of random samples _R_, sample size _N_, and number|
|---|
|of splits _S_.|
|2. **For** cluster size _k_ ∈  = {10_,_ 20_,_ … _,_ _K_ max }:<br>(a) **For** _r_ = 1, ...,<br>_R_<br>i. _Sample:_ Draw  _r_ _⊂_  without replacement with | _r_ | = _N_.<br>ii. _Cluster:_ Compute DTW on  _r_ and run _k_-medoids (PAM) to<br>obtain medoids  _r_ .<br>iii. _Assign_ _all_ _chains:_ Using  _r_ , assign each chain in  to its<br>nearest medoid, yielding a one-hot assignment matrix|
|_X_ ∈ {0_,_ 1} <sup>||×</sup><sup>_k_ </sup>. Let _X_ _tm_ ∈ {0_,_ 1} <sup>_n_ </sup><sup>_tm_ ×</sup><sup>_k_ </sup>denote the _n_ _tm_ × _k_ submatrix<br>of _X_ corresponding to the matches of team _t_, where _n_ _tm_ denotes the<br>number of chains for team _t_ in match _m_.<br>iv. _Per-match_ _distributions:_ For each team _t_ and match _m_,|
|calculate match pattern distributions by averaging over a team’s<br>chains in a match:<br>_p_ _tm_ = <sup>1</sup><br>_n_ _tm_<br>**** <sup>_⊤_ </sup>_X_ _tm_ .|
|For each team, collect these in _m_ _t_ × _k_ pattern distribution matrices<br>_P_ _t_ .<br>v. _Stability_ _scoring:_ For _s_ = 1, ...,_S_:<br>A. For each team _t_, randomly split the _P_ _t_ pattern distribution<br>matrices into two equal-sized parts: _P_ _t_ : _A_ _s_ and _P_ _t_ : _B_ _s_ and calculate<br>team and partition specific means: <br>_pt_ : _A_ _s_ and <br>_pt_ : _B_ _s_ . These are the<br>mean distributions for each team, for two different (random)<br>subsets of the data.<br>B. Compute distances between the mean distributions of<br>|
|teams in the two random subsets: _d_ <sup>( </sup><br>_pt_ : _A_ _s_ _,_ <br>_pt_ ′ : _B_ _s_<br>) . Count the<br>number of times that the distance between the mean team<br>distributions for the same team in the two subsets, is among the _q_<br>closest in the two random subsets:|







### **3.3 Characterizing playing styles** 

We define playing styles as clusters of similar distributions over ball movement patterns that occur in different football matches. To find such clusters, we apply latent Dirichlet allocation (LDA), which is a topic model popular for text analysis (see, e.g., Thorsrud 2020). We implement the model in Python using the gensim package (Řehůřek and Sojka 



**Figure 2:** Format of the matches by patterns LDA input data. 

2010). In topic modeling, LDA describes documents, in a large set of documents, as mixtures of topics, where each topic is a distribution over words. By viewing a team’s match data as a document and the ball movement patterns as words, the playing styles correspond to the LDA topics. That is, we consider playing styles as probability distributions over ball movement patterns that occur in different football matches. 

Hence, after identifying the ball movement patterns, we construct, for each match that a team plays, a distribution over these patterns by assigning the observed ball movement chains to the nearest (using the DTW distance) ball movement pattern. This results in a frequency matrix as shown in Figure 2. 

Applying LDA to the frequency matrix yields the playing styles. In our setting, matches of teams are modeled through probability distributions over playing styles, whereas the playing styles are modeled as probability distributions over ball movement patterns. 

In LDA, it is assumed that the underlying distributions are Dirichlet distributions with parameters _𝛼_ and _𝜂_ , where, in our football setting, _𝛼_ controls the distribution of playing styles in each match, and _𝜂_ controls the distribution of ball movement patterns in each playing style. We propose to use fixed symmetric Dirichlet priors, setting _𝛼_ = _𝜂_ = 1∕ _K_ , where _K_ denotes the number of playing-styles. Fixed symmetric parameters assume that all matches exhibit similar playing-style diversity, and that all playing-styles cover ball movement patterns equally. This may be a simplification, as some clubs consistently favor a dominant playing style, while others exhibit more balanced mixtures. Similarly, certain playing styles are more tightly associated with a few ball movement patterns, whereas others are broader and more diffuse. However, using fixed symmetric priors, improves computational efficiency and enhances reproducibility across experiments. Note that, for our empirical application (Section 4), we did perform experiments involving asymmetric priors. However, we found only marginal, and inconsistent, performance gains from such adaptations. 

> **6 —** V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football 



#### **3.3.1 Number of playing styles** 

In addition to selecting the LDA priors _𝛼_ and _𝜂_ , the number of playing-styles _K_ needs to be determined. Similar to our criterion for the number of ball movement patterns, we define a stability-based criterion, using multiple LDA runs and a similarity metric. In particular, estimation of LDA involves a random initialization that can produce different results (Agrawal et al. 2018). If the number of playing styles is incorrectly specified, it is likely that the obtained styles differ for different initializations. For example, if estimation is attempted with too few styles, some playing styles need to be “incorporated” into others. It is unlikely that this occurs in the same fashion for different runs. Hence, different runs are expected to result in different playing styles. Similarly, if too many styles are indicated, non-existing styles are generated by the algorithm. These additional playing styles are expected to differ between runs, leading to increased variability of the results. 

denote the “within” and “between” similarity for team _t_ . 

Note that the composite measure _St_ is largest when a team’s style is both consistent (i.e., similar over its own matches) and differentiates well when compared to other team’s playing styles (i.e., differs from other team’s playing styles). 

An overall measure for stability can be obtained by averaging over teams. Moreover, repeating this procedure for _R_ independent runs (using different random train/test splits) yields a distribution of stability scores. The mean of this distribution represents the average playing style stability and the variance indicates run-to-run consistency. We have summarized our procedure for selecting the number of playing styles in Algorithm 2. 

To quantify the stability of the algorithm, we perform, for each candidate _K_ , _R_ independent LDA runs, where we equally split each team’s matches into training and test sets. We then extract team’s playing styles for both splits by considering the corresponding means. However, as style vectors are compositional (i.e., their components are nonnegative and constrained to sum to one) their elements are dependent. This can create spurious trade-offs and bias simple arithmetic averages.computesTotheavoidaveragethis, Totheavoidaveragethis, avoidaveragethis, this, welog-ratiouse use the Aitchi-space son mean, which computesTotheavoidaveragethis, theavoidaveragethis, averagethis, inwelog-ratiouse log-ratiouse space (where relative information is treated appropriately) and then maps the result back to the space of valid compositions. This approach respects the compositional nature of the data and yields more meaningful averages across teams and splits (Aitchison 1982;; Pawlowsky-Glahna et al. 2015).).over 

###### **Algorithm ** Playing style stability 

1. Let _F_ denote the 2 _m_ × _k_ frequency matrix obtained after allocating team’s playing styles for both splits all ball movement chains to _k_ ball movement patterns and counting corresponding means. However, as style team and match specific occurrences. Set the maximum number of (i.e., their components are nonplaying styles as _K_ max and the number of random splits to _R_ . to sum to one) their elements 2. For each _K_ ∈  = {2 _,_ 3 _,_ … _, K_ max}: can create spurious trade-offs and bias (a) For each split _r_ = 1, ..., _R_ : i. _Data splitting:_ For each team _t_ , randomly partition its _m_ averages.computesTotheavoidaveragethis, inwelog-ratiouse the Aitchi-space matchesii. C _onstruct_ into two _train-test_ equal-sized _sets:_ setsConstruct _Ft_ : _Ar_ and _F_<sup>train</sup> _Ft_ ,: _B_ by _r_ . collecting the information is treated appropriately) and matrices of all teams in the _A_ sets ( _Ft_ : _Ar_ ) and, similarly, _F_<sup>test</sup> , by back to the space of valid composicollecting the matrices corresponding to the _B_ sets ( _Ft_ : _Br_ ). respects the compositional nature of iii. _Model fitting:_ A. Use _F_<sup>train</sup> to fit LDA using _K_ playing styles and symmetric more meaningful averages across teams priors _𝛼_ = _𝜂_ = 1/ _K_ and. Use the fitted LDA model to obtain the<sup>_K_</sup> denote1982;; Pawlowsky-Glahna matrix of _m_ distributionset al. 2015).).over per–matchiv. _Stability_ playing _assessment:_ styles _𝜃tm_<sup>train</sup> For eachand _𝜃_ team _tm_<sup>testusing</sup> _t_ :<sup>_F_trainand</sup><sup>_F_test.</sup> each row contains proportions that sum A. Compute team–level playing–style distributions by mean is defined as the normalized geoaveraging over matches: the _m_ rows of Θ.. We can collect these _𝜃_<sup>train</sup> _t_ = Aitchison mean over _Ft_ : _Ar_ vector _̄ 𝜃_ with as its _k_ -th element: _𝜃_<sup>test</sup> _t_ = Aitchison mean over _Ft_ : _Br m_ 1∕ _m 𝜃k_ = _K_ <u>(∏</u> _<u>i</u>_ =1<sup>_𝜃_</sup> _m_<sup>_ik_</sup> <u>)</u> 1∕ _m_<sup>_,_</sup> B. Use equation (1) to calculate team specific stability ~~∑~~ _j_ =1 ~~(∏~~ _i_ =1<sup>_𝜃ij_</sup> ~~)~~ scoresv. _S_ Calculate _t_ . the average stability over teams: _Sr_ = _T_<sup>1</sup> ∑ _Tt_ =1<sup>_St_.</sup> _𝜃ij_ denotes the _ij_ -th element of Θ.. Let (b) Compute summary stability statistics over splits. 

Let Θ ∈ ℝ<sup>_m_×</sup><sup>_K_</sup> a matrix of _m_ over _K_ columns. Hence, each row contains proportions that sum to 1. The Aitchison mean is defined as the normalized geometric mean over the _m_ rows of Θ.. We can collect these means in a _K_ -dimensional vector _̄ 𝜃_ with as its _k_ -th element: 

where, generically, _𝜃ij_ denotes the _ij_ -th element of Θ.. Let _𝜃_<sup>train</sup> _t_ and _𝜃_<sup>test</sup> _t_ denote the resulting playing styles (i.e., the Aitchison means over the appropriate set of matches) for team _t_ in the train and test sets respectively. We define the overall stability for team _t_ , as 

## **4 Empirical application** 

To illustrate our methodology, we consider an application to publicly available match event data. In particular, we use match event data provided by Wyscout for 1826 matches 



where, 

V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football **— 7** 

(corresponding to more than three million actions) played in the 2017/2018 season of the five major domestic European football leagues: the English Premier League, the Spanish Primera Division, the Italian Serie A, the French Ligue 1 and the German Bundesliga (Pappalardo and Massucco 2019). We organize the data by considering locations of the actions from the perspective of the team in possession of the ball. Since pitch dimensions vary from one venue to another, the locations are standardized to a pitch of 105 m long and 68 m wide, which is either the required or recommended pitch dimension in most international and domestic competitions. 

Creating ball movement chains as described in Section 3.1, results in more than 320,000 ball movement chains. To extract the ball movement patterns we apply Algorithm 1, where we use _K_ max = 120 _, R_ = 20 _, N_ = 20 _,_ 000 and _S_ = 100. Based on these results, presented in Figure 3a, we select _k_ = 70, as increasing the number of clusters does not appear to lead to further improvements. 

The 70 identified ball movement patterns can be considered as the equivalent of a vocabulary in a topic analysis model. For each team, we can find a distribution over these ball movement patterns during each match. These distributions describe structured interactions that characterize a team’s playing style. Applying LDA to the resulting data, results in playing styles that are characterized by different distributions over ball movement patterns. 

To select the optimal number of playing styles, we apply the stability-based procedure described in Algorithm 2, where we set _K_ max = 10, and _R_ = 10. The results can be found in Figure 3b. Note that, as _K_ increases, the score initially climbs steeply but levels off when _K_ exceeds 6. Hence, 

> _K_ = 6 strikes a desirable balance between statistical robustness and interpretability. In addition, this choice produces six distinct and interpretable playing styles. In Figure 4, we depicted these playing styles using Bézier curves (Shao and Zhou 1996) corresponding to the 10 most representative ball movement patterns. These patterns reveal wellseparated and tactically coherent styles that align with football domain knowledge, validating both the modeling approach and the chosen number of topics. 

### **4.1 Interpretation and validation** 

Recall that our goal is to quantify playing styles in a way that is both interpretable and suitable for further data analysis. The distributions, for each team and match, over the playing styles, allow us to analyze team and/or match specific patterns. To illustrate this, we provide two examples of applications, using only basic visualizations and descriptive statistics. 

#### **4.1.1 Differences in team playing styles** 

For a comparison of playing styles within and between leagues, we compare the playing styles of the teams winning their leagues and those finishing in last place. The results are depicted in Figure 5a and b. We see that although there are similarities between the champions in the different leagues, there are also some noticeable differences. In particular, the French champions, Paris Saint Germain, have a clearly different playing style that more frequently employs midfield play and plays less high up the field compared to the other champions. Furthermore, we see that Italian winners 



**Figure 3:** Stability plots for the number of ball movement patterns and playing styles. (a) Ball movement pattern stability. (b) Mean stability score. 

> **8 —** V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football 



**Figure 4:** A visualisation of the top 10 ball movement patterns for each of the six playing styles. Labels are added to the playing styles based on these visualizations. (a) Play low on the field. (b) Midfield play. (c) Attack from the right flank. (d) Play high up the field. (e) Switch flanks. (f) Attack from the left flank. 



**Figure 5:** Parallel coordinate plots of the average distributions over the six playing styles for league champions and losers during the 2017/2018 season. (a) National champions. (b) Teams ending last. 

V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football **— 9** 



**Figure 6:** Parallel coordinate plot of the average playing style distributions of Borussia Dortmund under Bosz and Stöger. 

Juventus rely more on playing low on the field than the other champions. 

The playing styles of the last teams in the different leagues appear to vary more over the different leagues. Moreover, comparing Figure 5a and b clearly shows that there are considerable differences between champions and the teams finishing last. To quantify uncertainty, we report nonparametric bootstrap (match-resampling) 95 % confidence bands around each team’s compositional mean. In particular, there appears to be significant difference in the utilization of the play high up the field style. As our playing styles are based on the observed possession sequences, a team’s intentions or tactical plans can only be inferred for as much as teams were able to execute these. Consequently, for stronger teams we expect to observe the play high style more than for weaker teams, and, similarly, weaker teams are expected to make more use of the play low style. Moreover, team tactics or actions concerning non-possession periods are not observed, and hence they are not directly accounted for. 

#### **4.1.2 Within seasonal changes in team playing styles: coach effects** 

As we have data for all matches during a season, we can use the playing styles to see if over time, changes in styles can be observed. For example, we can consider the average playing style of a team at the beginning of the season and compare this with the style towards the end of the season. Alternatively, we can consider the effect of changing a coach by considering average playing styles before and after the termination. To illustrate this, we consider the playing style of Dortmund during the 2017/2018 season. 

Borussia Dortmund began the 2017/18 season under Peter Bosz in a high-press 4-3-3 with a very high 

defensive line, midfielders pushed up to sustain possession and territory in the final third, and expansive width in attack. This allowed Dortmund to create wide overloads and quick entries into the final third, particularly via the flanks, mirroring Bosz’s general philosophy of playing a high-tempo attacking game in the opponent’s half (Eaton 2017; Honigstein 2017). Despite persisting with his possession-first approach, Bosz oversaw an eight-match winless league run and after a 2–1 home defeat to Werder Bremen on 9 December 2017, he was dismissed the next day and replaced by Peter Stöger. 

Stöger retained a base 4-3-3 formation but quickly overhauled Dortmund’s tactics. He instilled a much more compact, deeper defensive block in place of Bosz’s relentless high press (Honigstein 2017). In possession, their attacking buildup became more measured (Buczko 2017). 

The tactical changes of Dortmund can be observed in Figure 6. The transition from Bosz to Stöger appears as a sharp drop in the play high style proportion, a modest rise in midfield play, and clear increases in left-flank, right-flank, and switch-flank proportions. By contrast, the play low style proportion is roughly unchanged across coaches, implying the key difference is in post-recovery buildup: Stöger’s Dortmund were likelier to circulate wide and switch flanks rather than hold the ball high for long periods. 

## **5 Conclusions** 

We presented a method for quantifying football team’s playing styles based on match event data. Our method combines machine learning methods to extract playing styles from match event data. In particular, cluster analysis was used to extract ball movement patterns. That is, clusters of representative ball possession sequences. Next, Latent Dirichlet allocation, a model developed to find topics in textual 

> **10 —** V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football 

data based on distributions of words in documents, was applied to a matches-by-ball-movement-patterns matrix, to obtain the playing styles. 

To determine appropriate parameters (e.g., the number of ball movement patterns and the number of playing styles), we proposed several stability measures. As our methodology is unsupervised, assessment and validation in terms of model fit is not possible. However, our stabilitybased parameter selection methods ensure that interpretations are stable. That is, small changes in the data are unlikely to affect the results. 

We applied our methodology to a publicly available data set and showed how results can be used to provide a data driven analysis of team- or league-specific playing styles. Moreover, by comparing our interpretations to qualitative, media reports, we were able to provide an empirical validation of our playing styles for the analysed data. 

The type of match-event data needed to apply our methodology is collected for many, if not all, professional football matches. However, these data are not typically open-source and require commercial licenses. Here we only used the publicly available match event data provided by Wyscout for our illustration (Pappalardo and Massucco 2019). As the match event data only involve locations and actions with the ball, the obtained playing styles may not always adequately reflect team tactics and plans. Moreover, this type of match event data completely ignores nonpossession actions. That is, positioning of players not in possession of the ball. It would be interesting to see if our methodology can be extended to incorporate such data, and whether this would make it possible to identify more detailed playing styles. However, although, such data are gathered by professional teams, they are not available to us. 

In this paper we focused on the development of methodology for deriving playing styles. Our empirical application primarily served as an example to illustrate and empirically validate the proposed methodology. Consequently, we only considered basic applications concerning team playing styles. However, we believe that our methodology can be applied more widely by defining appropriate research questions and/or combining different data sources. For example, playing styles may be linked to match outcomes; individual players may contribute differently to different playing styles; performance of individual players may depend on playing styles; cultural elements could play a role in playing style adaptation; evolution (or stability) of playing styles over seasons may be indicators for success. It would be interesting to repeat our analysis to different seasons, and perhaps different leagues, to further assess these and other questions. 

##### **Research ethics:** Not applicable. 

**Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** None declared. 

**Conflict of interest:** The authors state no conflict of interest. **Research funding:** None declared. 

**Data availability:** Not applicable. 

## **References** 

- Agrawal, A., Fu, W., and Menzies, T. (2018). What is wrong with topic modeling? And how to fix it using search-based software engineering. _Inf. Software Technol._ 98: 74−88,. 

- Aitchison, J. (1982). The statistical analysis of compositional data. _J. R. Stat. Soc. Ser. B_ 44: 139−177,. 

- Bekkers, J. and Dabadghao, S. (2019). Flow motifs in soccer: what can passing behavior tell us? _J. Sports Anal._ 5: 299−311,. 

- Bialkowski, A., Lucey, P., Carr, P., Yue, Y., Sridharan, S., and Matthews, I. (2014). Identifying team style in soccer using formations learned from spatiotemporal tracking data. In: _2014 IEEE international conference on data mining workshop_ . IEEE, Shenzhen, China, pp. 9−14. 

- Blei, D.M., Ng, A.Y., and Jordan, M.I. (2003). Latent Dirichlet allocation. _J. Mach. Learn. Res._ 3: 993−1022. 

- Bransen, L., Haaren, J.V., and van de Velden, M. (2019). Measuring soccer players’ contributions to chance creation by valuing their passes. _J. Quant. Anal. Sports_ 15: 97−116,. 

- Brooks, J., Kerr, M., and Guttag, J. (2016). Using machine learning to draw inferences from pass location data in soccer. _Stat. Anal. Data Mining_ 9: 338−349,. 

- Buczko, S. (2017). Stöger’s pragmatic approach could be the tonic Dortmund need to recover. ESPN, https://www.espn.com/soccer/ story/_/id/37488328/stoger-pragmatic-approach-tonic-dortmundneed-recover (Accessed 19 September 2025). 

- Cintia, P., Rinzivillo, S., and Pappalardo, L. (2015). A network-based approach to evaluate the performance of football teams. In: _Machine learning and data mining for sports analytics workshop_ . CEUR Workshop Proceedings, Porto, Portugal. 

- Clijmans, J., Van Roy, M., and Davis, J. (2022). Looking beyond the past: analyzing the intrinsic playing style of soccer teams. In: _Joint European conference on machine learning and knowledge discovery in databases_ . Springer, Grenoble, France, pp. 370−385. 

- Davis, J., Bransen, L., Devos, L., Jaspers, A., Meert, W., Robberechts, P., Haaren, J.V., and Roy, M.V. (2024). Methodology and evaluation in sports analytics: challenges, approaches, and lessons learned. _Mach. Learn._ 113: 6977−7010,. 

- Decroos, T., Van Haaren, J., and Davis, J. (2018). Automatic discovery of tactics in spatio-temporal soccer match data. In: _Proceedings of the 24th ACM Sigkdd international conference on knowledge discovery & data mining_ . ACM, London, United Kingdom, pp. 223−232. 

- Decroos, T., Van Roy, M., and Davis, J. (2021). Soccermix: representing soccer actions with mixture models. In: _Machine learning and_ 

V. Misuric-Ramljak and M. van de Velden: Identifying playing styles in football **— 11** 

_knowledge discovery in databases. Applied data science and demo_ 

   - _track: European conference_ . Springer, Ghent, Belgium, pp. 459−474. 

- Eaton, R. (2017). Borussia Dortmund 2−1 Hoffenheim: tactical analysis. Breaking the lines, https://breakingthelines.com/opinion/borussiadortmund-2-1-hoffenheim-tactical-analysis/ (Accessed 17 September 2025). 

- Fernandez-Navarro, J., Fradua, L., Zubillaga, A., Ford, P.R., and McRobert, A.P. (2016). Attacking and defensive styles of play in soccer: analysis of Spanish and English elite teams. _J. Sports Sci._ 34: 2195−2204,. 

- Gibbs, A.L. and Su, F.E. (2002). On choosing and bounding probability metrics. _Int. Stat. Rev._ 70: 419−435,. 

- Gyarmati, L., Kwak, H., and Rodriguez, P. (2014). Searching for a unique style in soccer. arXiv preprint arXiv:1409.0308. 

- Hartigan, J.A. and Wong, M.A. (1979). A k-means clustering algorithm. _Appl. Stat._ 28: 100−108,. 

- Herberger, T.A. and Litke, C. (2021). The impact of big data and sports analytics on professional football: a systematic literature review. In: _Digitalization, digital transformation and sustainability in the global economy: risks and opportunities_ . Springer, Cham, Switzerland, pp. 147−171. 

- Honigstein, R. (2017). Pragmatist Peter Stöger steadies Borussia Dortmund after Bosz failure. ESPN, https://www.espn.com/soccer/ story/_/id/37488200/pragmatist-peter-stoger-steadies-borussiadortmund-bosz-failure (Accessed 17 September 2025). 

- Malqui, J.L.S., Romero, N.M.L., Garcia, R., Alemdar, H., and Comba, J.L. (2019). How do soccer teams coordinate consecutive passes? A visual analytics system for analysing the complexity of passing sequences using soccer flow motifs. _Comput. Graph._ 84: 122−133,. 

- Meza, D.P. (2017). Passing network autographs and overshooting style, https://statsbomb.com/articles/soccer/passing-networkautographs-and-overshooting-style/. 

- Müller, M. (2007). Dynamic time warping. In: _Information retrieval for music and motion_ . Springer, Berlin, Heidelberg, pp. 69−84. 

- Palazzo, L., Ievoli, R., and Ragozini, G. (2023). Testing styles of play using triad census distribution: an application to men’s football. _J. Quant. Anal. Sports_ 19: 125−151,. 

Pappalardo, L. and Massucco, E. (2019). Soccer match event dataset. Park, H.-S. and Jun, C.-H. (2009). A simple and fast algorithm for 

   - k-medoids clustering. _Expert Syst. Appl._ 36: 3336−3341,. 

- Pawlowsky-Glahn, V., Egozcue, J.J., and Tolosana-Delgado, R. (2015). _Modeling and analysis of compositional data. Statistics in practice_ . Wiley, Chichester, UK. 

- Plakias, S., Moustakidis, S., Kokkotis, C., Tsatalas, T., Papalexi, M., Plakias, D., Giakas, G., and Tsaopoulos, D. (2023). Identifying soccer teams’ styles of play: a scoping and critical review. _J. Funct. Morphol. Kinesiol._ 8: 39,. 

- Pulis, M. and Bajada, J. (2022). Reinforcement learning for football player decision making analysis. In: _StatsBomb Conference_ . Hudl StatsBomb, London, United Kingdom. 

- Řehůřek, R. and Sojka, P. (2010). Software framework for topic modelling with large corpora. In: _Proceedings of the LREC 2010 workshop on new challenges for NLP frameworks_ . ELRA, Valletta, Malta, pp. 45−50. 

- Rousseeuw, P. and Kaufman, L. (1987). Clustering by means of medoids. In: _Proceedings of the statistical data analysis based on the L1 norm conference_ , 31. Elsevier, Neuchatel, Switzerland. 

- Schubert, E. and Lenssen, L. (2022). Fast k-medoids clustering in rust and python. _J. Open Source Software_ 7: 4183,. 

- Shao, L. and Zhou, H. (1996). Curve fitting with Bézier cubics. _Graph. Models Image Process._ 58: 223−232,. 

- Stats Perform. (2020). New official premier league insights feed − powered by stats perform & second spectrum. Stats Perform, https://www.statsperform.com/press/new-official-premier-leagueinsights-feed-powered-by-stats-perform-second-spectrum/ (Accessed 26 August 2025). 

- Tavenard, R. (2021). An introduction to dynamic time warping, https:// rtavenar.github.io/blog/dtw.html. 

- Thorsrud, L.A. (2020). Words are the new numbers: a newsy coincident index of the business cycle. _J. Bus. Econ. Stat._ 38: 393−409,. 

- Van Roy, M., Robberechts, P., Yang, W.-C., De Raedt, L., and Davis, J. (2021). Leaving goals on the pitch: evaluating decision making in soccer. arXiv preprint arXiv:2104.03252. 

- Whitmore, J. (2020). Introducing movement chains. Stats Perform. 


