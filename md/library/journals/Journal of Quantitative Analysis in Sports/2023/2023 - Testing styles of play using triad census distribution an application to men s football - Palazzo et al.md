<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2023/2023 - Testing styles of play using triad census distribution an application to men s football - Palazzo et al.pdf -->

J. Quant. Anal. Sports 2023; 19(2): 125–151 

### **Research Article** 

Lucio Palazzo*, Riccardo Ievoli and Giancarlo Ragozini 

# **Testing styles of play using triad census distribution: an application to men’s football** 

https://doi.org/10.1515/jqas-2022-0010 Received February 14, 2022; accepted May 8, 2023; published online May 23, 2023 

**Abstract:** Summary statistics of football matches such as final score, possession and percentage of completed passes are not satisfyingly informative about style of play seen on the pitch. In this sense, networks and graphs are able to quantify how teams play differently from each others. We study the distribution of triad census, i.e., the distribution of local structures in networks and we show how it is possible to characterize passing networks of football teams. We describe the triadic structure and analyse its distribution under some specific probabilistic assumptions, introducing, in this context, some tests to verify the presence of specific triadic patterns in football data. We firstly run an _omnibus_ test against random structure to asses whether observed triadic distribution deviates from randomness. Then, we redesign the Dirichlet-Multinomial test to recognize different triadic behaviours after choosing some reference patterns. The proposed tests are applied to a real dataset regarding 288 matches in the Group Stage of UEFA Champions League among three consecutive seasons. 

**Keywords:** count data; multivariate testing; passing network; sport performance; triad census. 

## **1 Introduction** 

In past decades, decision-makers in sports used to be subjective, trusting mainly in intuition and personal experience rather than evidences from the data. Nowadays, sport analytics and availability of data facilitate the usage of 

***Corresponding author: Lucio Palazzo** , Department of Political Sciences, University of Naples Federico II, Napoli, Italy, 

E-mail: lucio.palazzo@unina.it. https://orcid.org/0000-0001-7529-4689 **Riccardo Ievoli** , Department of Chemical, Pharmaceutical and Agricultural Sciences, University of Ferrara, Ferrara, Italy. https://orcid.org/00000001-9489-3564 

**Giancarlo Ragozini** , Department of Political Sciences, University of Naples Federico II, Napoli, Italy 

statistical methodologies in a broad range of sports (such as basket, cricket, hockey and golf) recently spreading even in football (for a wide review of the literature see Kimber and Hansford 1993; Cox and Trevor 2002; Albert, Bennett, and Cochran 2005; Lewis 2005; McIntyre and McKitrick 2005; Sampaio et al. 2006; Ibáñez et al. 2008; Tibshirani, Price, and Taylor 2011; Moura, Martins, and Cunha 2014, and references therein). 

A relevant part of the literature has been focused on player-level analysis, see, e.g., Kahn (1993); Baumer, Jensen, and Matthews (2015) (baseball), Fewell et al. (2012) (basketball), Hadley et al. (2000) and Yurko, Ventura, and Horowitz (2019) (American football), Gomez (2002), (hockey) and Gallagher, Frisoli, and Luby (2021) (tennis). For what concerns football, increasingly sophisticated statistical models are used to predict football outcomes (Groll, Schauberger, and Tutz 2015), even considering players abilities (Carpita, Ciavolino, and Pasca 2019), or teams’ final rankings (Groll et al. 2019). At a team-level perspective, tactics and strategies are key elements for success in football. Statistical methodologies that are used in this context are still under debate: conventional approaches are based on the analysis of ball possession (Bate 1988; Lago-Peñas and Dellal 2010), while others rely on summary statistics (Clemente et al. 2016) or on the prediction of the probability of scoring goals (Keller 1994; Stern 1991). 

In recent years network analysis has been applied on football passing distributions. A seminal contribution can be found in Grund (2012), helping to establish a relationship between network structure (measured by “intensity”, i.e., passes over minutes, and centralization-based indices) and team performance (measured in terms of scored goals). More recently, a set of network summary measures from the passing distribution has been used to model the probability of win the game (Ievoli, Gardini, and Palazzo 2021a), while passing network indicators have been involved in Bayesian Hierarchical models (using regularization methods) to model the scored goals or the difference in goals (Ievoli, Gardini, and Palazzo 2021b). Other interesting applications of network analysis in football can be found in Pina, Paulo, and Araújo (2017), Clemente, Sarmento, and 

Open Access. © 2023 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **126 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

Aquino (2020), Mclean et al. (2018), and Gonçalves et al. (2017). 

Starting from the aforementioned literature, we propose a network analysis approach based on triad census to extract the properties of passing behaviour in football that should be informative to identify and characterize team strategies. 

We focus on passes since they are undoubtedly the most representative events in football, especially compared to goals, shots and other in-field variables (Cintia, Rinzivillo, and Pappalardo 2015). Although the literature has been mainly focused on scored (and expected) goals, recent studies highlight the importance of passing effectiveness (Rein, Raabe, and Memmert 2017) and passing behaviours in evaluating overall players’ performance (Bransen, Van Haaren, and van de Velden 2019). Bransen, Van Haaren, and van de Velden (2019) also evidence that passing distribution among players is able to characterize players’ profiles, also allowing to make comparisons between them. Indeed, starting from the (undirected) passing networks of the Italian teams in first division (“Serie A”), Diquigiovanni and Scarpa (2019) identify 15 different tactics using a two phase clustering technique. 

Passes are not only related to individual technical aspects or “vision” throughout the pitch, but also express social attitudes of players which may include “ _sympathies and antipathies, good versus bad cooperation partners, kindness versus resentment_ ” (Hyballa and Te Poel 2015, p. 55). In this sense, each social phenomenon expressing a particular structure relies on properties such as density, transitivity and presence of clusters (Faust 2006). Then triad census, widely surveyed by Faust (2010), appears a suitable method to take into account all of these features. 

Our aim is twofold: we want to study the triadic distribution in football passing networks using the resulting information to test if it significantly deviates from a random scenario. We also formally test for the presence of one or different styles of play in football according to a set of reference “strategies” determined by specific triadic configurations. 

To pursue the research aim, at first we adopt the _omnibus_ test for the observed triadic distribution against a random structure. The test is based on inferential and probabilistic properties of triads, discussed in Holland and Leinhardt (1978) and Faust (2010), and can be useful to find how observed triads deviate from randomness. However, testing only the non-randomness of triads does not allow to identify different styles of play that could be developed in a game, expressed through the distribution of passes. Thus, the omnibus test is not able to provide comparisons at team level. 

To overcome this issue, we redesign a multivariate test based on Dirichlet-Multinomial (DM) distribution. This family of tests have been developed and applied within several research contexts (cf. Ennis and Bi 1999; La Rosa et al. 2012; Ricard and Davison 2007; Wu et al. 2017, among others), and it is suitable in case of non-independent counts. However, to the best of our knowledge, the DM-based tests have never been applied to triad census, especially for football data. 

The main contribution of this work is to exploit a more flexible testing approach to triad census with the purpose to unveil the potential of triadic distribution in football passing network analysis, especially to retrieve possible styles of play. 

The paper is organized as follows: Section 2 introduces the main concepts and theory of team passing networks and triad census, while in Section 3 the theory behind the _omnibus_ test and the DM-based test is introduced. Section 4 includes an application regarding three European Champions League Seasons from 2016 to 2017 to 2018–2019. Finally, in Section 5 we highlight the possible main implications of this approach in football along with some conclusions and possible advances. 

## **2 Methodology** 

Football matches are characterized by complex and multidimensional features: scored points (goals) have very low frequencies with respect to other relevant and detectable events, such as shots, cards, fouls and free kicks among others (Cintia, Rinzivillo, and Pappalardo 2015). Nowadays, new technologies such as image analysis, wearable devices, multiple-camera player trackers and drone-based analysis of training sessions, are changing the way to retrieve data and provide new opportunities in football tactics (cf. Boyle and Haynes 2004; Buchheit and Simpson 2017; Buchheit et al. 2014; Edgecomb and Norton 2006). Among them, ball passes between players of the same team are complex events to analyse and their study can be crucial to retrieve useful information regarding underlying mechanics determining style of play and the overall team performance. A first descriptive approach is given by the analysis of type and frequency of passes between players in a team, during each match. 

Resulting data share a “relational” structure, defined as a set of “measurements” between pairs of units, also called “agents” and may involve contacts, connections, group attachments, meetings or relations between agents and these links, expressed by ties binding individuals together. The overall structure coming from football matches, defined as team passing network, can be described as the relationship between player (agents) in terms of passes (measurements) in a valued square matrix. Within this framework, comparisons at individual (micro) level involving players are generally straightforward and some global information can be also extracted in a more general context, in order to evaluate performance of teams in a macro level perspective. A systematic literature review on the relationship between passing network and tactic analysis in football can be found in Caicedo-Parada, Lago-Peñas, and Ortega-Toro (2020). 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 127** 

#### **2.1 Passing networks in football** 

A passing network _G_ is defined as the ordered triple ( _,_  _,_ ) consisting of a set of 11 first team players _𝑣_ ∈ , a set of arcs _a_ ∈  _⊆_  × , consisting of all the passing relationships between them and a set of weights _𝜔_ ∈ , i.e., the number of passes occurred during the match, denoting the strength of the connection. We assume that both vertices  and arcs  are finite as well as || = _n_ . Passing network can be expressed in the form of an adjacency matrix _P_ =<sup>(</sup> _pi, j_ ), with _pi, j_ = _𝜔_ ( _ai, j_ ) if ∃ _ai, j_ ∈  and _pi, j_ = 0 otherwise. 

In Table 1 we present the team passing network of a match involving Arsenal against PSG in September 13th 2016 (first match of the Group Stage, group A). For example, during the match, goalkeeper Ospina passed successfully the ball to Monreal four times ( _p_ 7) and 11 to Mustafi ( _p_ 9), while he received once the ball from Bellerin ( _p_ 10). Figure 1 represents the directed and weighted graph representation obtained through the adjacency matrix of Table 1; eleven agents (representing the players) are connected between arrows and the strength of relationship, i.e., the number of passes, is expressed through the size of them. 

We need to remark that values on the main diagonal in Table 1 are constrained to be null since we assume that a player cannot pass the ball to himself. Thus the so-called “loops” are not allowed in this framework. 

To summarize, passing networks in football share some peculiarities: they are not high dimensional, involving a small and generally fixed number of vertices, but may also present a certain degree of sparseness. In fact, the number of interactions may depend on (i) position on the pitch (ii) individual skills and team cooperation attitudes and, finally, (iii) team strategies and/or style of play. 

In order to formally uncover the qualitative attributes of these links, the analysis of triads represents a possible way to detect patterns in the passing distribution and, under some mild assumptions, make a proper inference. Thus, observed triadic distribution can be used to compare connectivity of a team during competitions, in order to analyse changes in strategies and styles of play. In addition, the comparison could be also made through teams in the same tournament, helping to understand if different passing behaviours can have an impact on the football outcomes. 



<!-- Start of picture text -->
6 7<br>4<br>2<br>3<br>1<br>8<br>11<br>9<br>10<br>5<br><!-- End of picture text -->

**Figure 1:** Graph of adjacency matrix of the team passing network of Arsenal illustrated in Table 1. 

#### **2.2 Triad census** 

Although the minimal structural element in a network is a dyad, defined as the interaction occurring between two agents, the minimal group is represented by a triad, involving a subset composed by three agents. In general, given a set of _n_ nodes (agents), a _k_ -subgraph is defined as the set containing all the possible subsets of dimension equal to _k_ of a network. The number of possible distinct _k_ -subgraph that can be examined are ( _kn_ ), with _k_ ≤ _n_ , and the number of possible unweighted and directed arcs occurring between _k_ individuals is _k_ ( _k_ − 1), spanning from the totally disconnected ( _null_ ) to the full connected 

**Table 1:** An example of adjacency matrix in football representing the team passing network of Arsenal, first Group Stage match of 2016–2017 Champions League. 

|||**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|**_p_**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Ospina|_p_1||1|1|1|1|1|4|1|11|2|1|
|Koscielny|_p_2|1||3|2|0|1|13|11|12|1|1|
|Alexis Sanchez|_p_3|0|3||9|4|4|0|4|0|2|4|
|Ozil|_p_4|0|2|8||2|8|3|6|2|3|5|
|Oxlade-Chamberlain|_p_5|0|2|2|2||0|0|4|0|2|1|
|Iwobi|_p_6|0|4|6|8|0||7|3|4|4|2|
|Monreal|_p_7|3|3|8|2|3|7||5|1|0|6|
|Santi Cazorla|_p_8|0|10|11|13|5|7|5||8|7|6|
|Mustafi|_p_9|6|13|1|1|2|2|0|15||13|1|
|Bellerin|_p_10|1|0|2|1|4|5|0|2|11||3|
|Coquelin|_p_11|0|3|5|3|1|4|3|9|2|3||



> **128 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

( _clique_ ) case. Each tie can be either present or absent; for each subgraph there are 2<sup>_k_(</sup><sup>_k_−1)</sup> possible states considering the exact identity of the individuals in the whole set. 

Focusing on the structure elapsing between individuals, there are some recurrent states where the relational structure (i.e., in which way agents are linked between each other) is invariant under permutations of labels attached to the agents. Such categories are called _isomorphism classes_ . The number of possible isomorphism classes of a _k_ -subgraph depends on the number of elements belonging in each subgroup, in general this value can be exceedingly high even with modest subgroup dimensions, (Holland and Leinhardt 1976). For instance, when _k_ = 2 _,_ 3 the number of isomorphism classes is 3 and 16, respectively, rapidly increasing even with _k_ = 4 (218 classes). 

In a purely theoretical point of view, both dyads and triads are two special cases of _k_ -subgraphs. Figure 2 presents all the possible isomorphism classes derived from triad census, from the so called “003”, which involves no relationship between vertices, to the full connected triad “300”, presenting six edges. A summary of triads’ labels can be found in Figure 2. 

Main differences between dyads and triads have been surveyed in Krackhardt (1999) and he stated that the individuality of agents is preserved when the analysis is focused on dyads, helping to highlight the direction of interactions between couples of agents. The census of all possible triads has been introduced by Davis and Leinhardt (1967), while Wasserman and Faust (1994) and Faust (2010) help to develop the method in order to retrieve information about network structural properties regarding the level (or quality) of transitivity nodes between individuals (see also Lorrain and White 1971; Luczkovich et al. 2003; Cugmas, Ferligoj, and Žiberna 2017, for further details). 

In order to analyse the probabilistic properties of triad census, we use the notation introduced in Wasserman and Faust (1994) starting from the general _k_ -subgraph theory. Then we apply authors’ results shown in Theorem 14.1 and 14.2 to the triadic case ( _k_ = 3), in order to obtain moments of triad census. We remark that these quantities are based on the theoretical distribution related to the random structure. 

Given a network having _n_ agents, let us suppose to label each node with a number equal to 1 _,_ 2 _,_ … _, n_ . We denote two distinct isomorphism classes for the _k_ -subgraph _𝜂_ and _𝜈_ , defined as two _k_ - subgraphs having at least one vertex or edge that they do not share (while all other vertices and edges can overlap). We refer to generic 

elements of the two isomorphism classes as _K_ = _Ki_ 1 _,_ … _,ik_ ∈ _𝜂_ and _L_ = _Li_ ′1<sup>_,_…</sup><sup>_,i_′</sup> _k_<sup>∈</sup><sup>_𝜈_,wherethesubscriptsarerelatedtothelabelsattached</sup> to each vertex of the subgraph. Therefore, we define the following probabilities: 



representing the probability that any single subgraph _K_ or any two subgraphs _K, L_ belong to classes _𝜂_ and _𝜈_ , respectively. Since the above probabilities may vary for each configuration, it would be necessary to average the probability of each isomorphism class over all possible _K_ and _L_ structures available in the _k_ -subgraph, as follows: 



where 0 ≤ _h_ ≤ _k_ − 1. 

The subgraph census’ random variable _H𝜂_ is then defined as the number of _k_ -subgraphs belonging to the isomorphism class _𝜂_ . Using the theorem introduced Holland and Leinhardt (1976), it is possible to define the moments of _k_ -subgraph census random variables _H𝜂_ for each admissible isomorphism classes that can be retrieved in the _k_ -subgraph. Hence, such moments rely on a given probability structure. 

## **3 Testing triadic patterns** 

### **3.1 Testing against random structure** 

Several possible random distributions can be used to compute moments for each isomorphism (see Holland and Leinhardt 1976; Faust 2007, for further details). Among others, the so called U|MAN (Uniform given Mutual Asymmetric and Null arcs) is one of the most relevant structures in the literature, and will be used as reference throughout the 



**Figure 2:** List of isomorphism classes belonging to the triadic subgraph. Each label consists in three digits representing the number of mutual (↔), asymmetric (→), and null links connecting two units. Some classes with the same MAN distribution have a letter representing the additional structural differentiation: _C_ = cycle, _T_ = transitive, _U_ = up and _D_ = down. Plot adapted from Faust (2008). 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 129** 

rest of the paper. U|MAN random digraph is the probability distribution on the set of all digraphs with _n_ agents considering fixed and discrete values of mutual, asymmetric and null arcs present in the network. The motivation to use the U|MAN distribution can be found in the possibility to construct, imposing a set of assumptions, an asymptotic statistical test for each of the 16 isomorphism classes and, more importantly, a comprehensive asymptotic test involving all types of triads. 

Thus, it is possible to define a random network structure starting from the number of mutual, asymmetric and null arcs in the network comparing the observed triads against those which are uniformly distributed among the agents. In order to make this comparison, our purpose is to formally test if the probabilistic structure of a team passing network is closer or not to the one defined in the conditionally uniform random case. 

Since it holds a direct connection between averaged and single probabilities shown in Equations (1) and (2), the use of U|MAN distribution allows to simplify results of Equations (3) and (4) in the following way: 





where 





and 0 ≤ _h_ ≤ _k_ − 1. The first equality is a consequence of the invariance under permutations property of U|MAN distribution; to summarize, changing the node’ labels of a triad does not change the probability of belonging to an isomorphism class. On the same basis, the second equation indicates that the probabilities _pK,L_ ( _𝜂, 𝜈_ ) depend only on _𝜂_ and _𝜈_ and also on the number of nodes they share, i.e., _h_ = | _K_ ∩ _L_ |. 

Moreover, it is possible to derive a correspondence between the joint probabilities of two triads having either zero or one vertex in common, such as: 



Basing on the above statements, it is possible to apply the results shown in Holland and Leinhardt (1976) under the condition that data generating process of links in a network is characterized by a U|MAN distribution. As mentioned, the total number of isomorphism classes of a triad census is 16 (as in Figure 2) and it is possible to define the triad census vector **T** = ( _T_ 1 _,_ … _, T_ 16) from a random directed graph based on the U|MAN distribution. Expectation, variance, and covariance for each isomorphism class are directly 

retrieved combining the results in Holland and Leinhardt (1976) and are depicted in the Appendix A. Regarding the asymptotic distribution of vector **T** , it is worth to notice that it has an approximate multivariate normal distribution with an increasing number of vertices included in the graph (Wasserman and Faust 1994). Starting from results presented in the Appendix A, Equations (9)–(11), it is possible to compute the _𝜏𝜂_ statistics for each isomorphism class 



For each class _𝜂_ , _𝜏 𝜂_ represents the standardized departures of observed triads from the theoretical random distribution, allowing to formally test the presence of patterns that deviate from what is expected in the randomly distributed case. Thus, a test statistic denoted as _𝜏_ max<sup>2can be used to build an</sup> omnibus test of randomness: 



where **_𝝁_** is the vector of expectations and Σ the variance–covariance matrix computed using the U|MAN distribution. Σ<sup>−1</sup> is the pseudo-inverse of the variance–covariance matrix and can be obtained as terms of eigenvalue decomposition Σ<sup>−1</sup> = Γ _D_<sup>−1</sup> Γ<sup>′</sup> , where Γ is the matrix of eigenvectors of Σ and the values _𝜆i_ of the inverse diagonal matrix _D_<sup>−1</sup> = diag<sup>(</sup> 1∕ _𝜆_ 1 _,_ … _,_ 1∕ _𝜆 p,_ 0 _,_ … _,_ 0<sup>)</sup> correspond to the non-null eigenvalues of Σ, for _i_ = 1 _,_ … _, p_ and _p_ = rank(Σ) ≤ 16. The above statistic can be used as test for detecting the possible deviation against a random network structure in the data. 

Holland and Leinhardt (1978) prove that, given a random reference distribution and if the vector **T** is approximately Normal, _𝜏_ max<sup>2asymptoticallyfollowsa</sup><sup>_𝜒_2distri-</sup> bution with degrees of freedom equal to the rank of Σ. Therefore, we can test if data exhibit a random structure compared to the alternative hypothesis of strong deviations against randomness. 

### **3.2 Testing specific team strategies** 

The approach introduced in Holland and Leinhardt (1978) lacks of flexibility: it is not straightforward to manipulate the null hypothesis in order to test for deviation from different random structures or, more importantly, to test for significant changes in a subset of triad counts. Moreover, the _𝜏_ max<sup>2teststatisticmaybemoreconservativeinfinite</sup> samples. 

A possible workaround could be the use of univariate tests for each isomorphism class, but this alternative generally implies the fulfilment of strict assumptions (such 

> **130 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

as independence between the triadic configurations) that are not satisfied in this context. Then, given the multivariate nature of triadic configurations, we are interested in defining a set of multivariate hypotheses allowing to formally test a set of factors composed by non-independent counts. 

Testing procedures of count data have been applied in other fields, such as the analysis of contingency tables or ratings data obtained from ordered categorical responses showing the presence of variability between samples (Ennis and Bi 1999), but mainly related with biology and genetics, i.e., olfactometer data (Ricard and Davison 2007) or DNA sequencing data (Wu et al. 2017). A comprehensive analysis of discrete multivariate distributions can be found in Johnson, Kotz, and Balakrishnan (1997) for a. 

Despite the presence of interest in literature regarding this topic, to the best of our knowledge there are no applications to triad census analysis. In this context, due to the structure induced by isomorphism classes, the Dirichlet-Multinomial (hereafter DM) distribution (introduced in Mosimann 1962) suits properly the features belonging to triad census data. Throughout the rest of the paper we will refer to Equation (13) (see Appendix B) and then we will denote that an _m_ -variate random variable follows a DM distribution as **X** ∼ DM _m_ ( **_𝝅_** _, 𝜃_ ). The main information regarding DM distribution useful for the purpose of the present work is depicted in the Appendix B. 

Beta-Binomial distribution is a special case of the DM distribution when the number of modalities reduces to _m_ = 2. It can also be shown that it approaches the Multinomial distribution as _𝜃_ approaches to zero. Parameter estimation can be carried out through Maximum Likelihood or Method of Moments as described in Minka (2000) and Brier (1980). 

Our proposal is to adopt DM family of distributions to the problem of formally testing for the presence of “structural equivalence” in a set of triad census data. The aim of the test is to determine if a sample belongs to a previously specified distribution, given that the data generating process is from a DM family. 

Initially, Brier (1980) focused their effort on the study of fitting and testing of general log-linear models in contingency tables following DM distribution, then the problem of testing vector of proportions generated from different families of processes has been surveyed (Koehler and Wilson 1986), deriving general goodness-of-fit statistics based on generalized Wald statistic, also computing asymptotic results. 

More recently, a goodness-of-fit statistic for testing the fit of a model based on DM family is also obtained in Johnson, Kotz, and Balakrishnan (1997): given that data have 

been generated by a DM distribution, a possible approach could be to compare the estimated frequencies with a reference distribution defined in null hypothesis by imposing theoretical frequencies **_𝝅_** 0. Nowadays, with the One-Sample DM test (OSDM) for grouped count data, La Rosa et al. (2012) extended this testing procedure to formally test for a set of _g_ samples belonging to the same population measured on different subjects. 

Consider a set { **x** _i_ } _j_ =1 _,_ … _,g_ of _g_ samples, each one consisting of _m_ counts of distinct modalities where the count of modality _i_ corresponding to the _j_ th sample is denoted as _xi, j_ . Denote _x_ 0 _,_ ∙ =<sup>∑</sup><sup>_m_</sup> _i_ =1∑ _gj_ =1<sup>_xi, j_as the sum of all frequencies</sup> over all samples, while _x_ 0 _, j_ =<sup>∑</sup><sup>_g_</sup> _j_ =1<sup>_xi, j_standsforthetotal</sup> of the _j_ th sample. Then, to formally tests the hypothesis _H_ 0: **_𝝅_** = **_𝝅_** 0 versus the alternative _H_ 1: **_𝝅_** ≠ **_𝝅_** 0 the following test statistic is presented 



where the operator (⋅)<sup>+</sup> is the Moore–Penrose generalized inverse and the matrix Σ corresponds to 



> with ( **_𝝅_** _,̂ 𝜃_ ) unbiased estimators of distribution parameters. The test statistic _X_ obs asymptotically converges to a _𝜒_<sup>2</sup> distribution with degrees of freedom equal to the rank of the matrix<sup>(</sup> diag( **_𝝅0_** ) − **_𝝅0𝝅0_**<sup>_⊤_)+</sup> . 

In addition, due to the aggregation property (see, e.g., Johnson, Kotz, and Balakrishnan 1997, and references therein), the DM family allows for a flexible re-parametrization of the probability vectors: the joint distribution over sums of disjoint subsets of modality counts is also DM, i.e., if ( _x_ 1 _,_ … _, xm_ ) ∼ DM _m_ ( _𝜋_ 1 _,_ … _, 𝜋m, 𝜃_ ) then, ( _x_ 1 _,_ … _, xs, x_ 0 − ∑ _mi_ = _s_ +1<sup>_xi_</sup> ) ∼ DM _s_ +1( _𝜋_ 1 _,_ … _, 𝜋s,_ 1 − ∑ _mi_ = _s_ +1<sup>_𝜋i, 𝜃_).Hence,itispossible</sup> to “collapse” a subset of isomorphism classes into one containing the sum of their counts, e.g., the ones having low frequencies or structural zeroes. 

We redesign the testing procedure in Equation (7) to triad census analysis to unveil if a triadic pattern, computed from a group of networks sharing similar features, has been generated from a reference DM distribution. To this end, we propose two sets of null hypotheses. Firstly, reference team strategies (based on the triadic configuration) are set to identify if and how teams follow a given strategy. Secondly, a more direct comparison between couple of teams can be performed to detect possible similarities. 

Although a small-scale simulation of size has been performed considering either few _m_ modalities and small total 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 131** 

counts _x_ 0 _,_ ∙ (see La Rosa et al. 2012), there is no empirical evidence in literature of test statistic validity when the number of _g_ samples is small, as it happens in our empirical application. For this reason, in order to give a further support to our testing strategy, we carried out a small scale Monte Carlo exercise computing the empirical size of the DM test with small sample sizes. All the details are given in Appendix. 

## **4 Empirical application** 

In this Section we summarize the main results of data analysis pertaining to Football Data. Our data consist of a set of team passing distributions coming from the Group stage of 32 UEFA Champions League (UCL) for three consecutive Seasons: 2016–2017, 2017–2018 and 2018–2019. Data were collected through the official UEFA website (www.uefa.com) and subsequentially processed to include 96 matches and 192 passing networks for each season, for a total of 288 matches and 576 passing networks. Fifty-six teams were involved; among them, 26 teams (46.4 %) played in nearly two editions of the tournament, while 14 teams (25 %) were qualified in the competition in all editions. England, Spain, Germany and Italy were the most represented federations, followed by France and Portugal. Table 2 depicts the overall descriptive statistics of passes in the three considered UCL Seasons for the teams. The mean of passes for each team in a match was about 386 passes (median equal to 370). The variability around the mean does not indicate substantial changes among the three UCL Seasons, even if the range can be very large. 

The total number of passes contributes to the perceived competitiveness of a team. In Figure 3 we include only the best and worst five teams in the first phase of the three considered UCL editions, highlighting the best and worst performances of their first lineups. In terms of passes, all of 

the top-five-ranked teams advanced to the knockout phase, with the exception of Naples in 2018–2019, although that team did achieve the same number of points as the secondbest team in the group (Liverpool). Barcelona (Spain) was the only team that was always in the top five, while Borussia Dortmund, Real Madrid, Bayern München and Manchester City placed in higher positions of the ranking twice over three times. 

Furthermore, four-fifths of the “worst” five teams in terms of completed passes failed to pass the Group Stage in each edition. Only Leicester City (2016–2017), Basel (2017–2018) and Schalke 04 (2018–2019) managed to advance despite their poor performance. Among them, only Leicester City passed through the round of 16 to get to the round of 8. 

In the following, triad census methods are applied to our networks, including the formal tests of Section 3. The main results were developed through R software using igraph (Csardi and Nepusz 2006) and HMP (La Rosa et al. 2019). 

### **4.1 Descriptive analysis** 

Network structure can be relevant in this kind of analysis, showing evidence of having relationship with the number of passes. For example, considering all networks, a positive and statistically significant large correlation can be found between the number of passes and the mutual dyads (0.77, _p_ -value _<_ 0 _._ 001). In addition, the asymmetric and null dyads were negatively correlated with the passes (−0.67 and −0.45 respectively), again with statistical significance ( _p_ -value _<_ 0 _._ 001 for both variables). 

Regarding the dyadic distribution, the football teams expressed a median of 37 mutual relationships per match, while unilateral links varied between 10 and 15 in 50 % of the teams. There was an average of 6 unconnected dyads 

**Table 2:** Descriptive statistics of total number of passes in football UCL data. 

||**Statistic**|**2016–2017**|**2017–2018**|**2018–2019**|**Overall**|
|---|---|---|---|---|---|
|**Total passes**|Mean|386.25|388.34|382.19|385.60|
||SD|136.93|134.31|131.30|133.99|
||min|121.00|126.00|114.00|114.00|
||Q1|285.75|278.50|278.75|281.00|
||Median|373.00|377.00|362.00|370.50|
||Q3|462.25|475.50|471.00|467.75|
||Max|876.00|743.00|921.00|921.00|



> **132 —** L. Palazzo et al.: Testing styles of play using triad census distribution 



<!-- Start of picture text -->
2016−2017<br>4000<br>3000 Match<br>I<br>II<br>2000 III<br>IV<br>V<br>VI<br>1000<br>0<br>2017−2018<br>4000<br>3000<br>Match<br>I<br>II<br>2000 III<br>IV<br>V<br>VI<br>1000<br>0<br>2018−2019<br>4000<br>3000<br>Match<br>I<br>II<br>2000 III<br>IV<br>V<br>VI<br>1000<br>0<br>Bayern Munchen Barcelona Borussia DortmundPSG Juventus MedianLegia WarsavCSKA Moskov LeicesterDynamo Zagreb Rostov<br>Manchester CityBarcelonaReal Madrid SevillaBayern Munchen MedianOlympiacos Monaco Maribor Basel APOEL<br>Borussia Dortmund BarcelonaReal MadridManchester City Napoli Median SchalkeAEK AthensViktoria Plzen Red Star BelgradePSV<br><!-- End of picture text -->

**Figure 3:** List of best and worst five teams (along with median values) ranked by the number of completed passes in each season. 

for each team per match, varying between a minimum of 0 and a maximum of 19, as well as presenting higher variability (47 %) among the MAN. Differences between the three seasons seemed to be negligible for the three counts. We 

must remark that the sum of MAN for football teams ( _n_ = 11 players) is constrained to 55, i.e., ( _n_ ( _n_ − 1)∕2). 

Furthermore, generalizing to the triad census, we recognized specific triadic patterns in football passes. Table 4 shows the distribution of triads for passing networks of all teams involved in the group stage of the UCL 2016–2017 to 2018–2019 seasons ( _n_ = 576). 

We highlighted noticeable differences in terms of mean and variability between 16 isomorphism classes. In particular, the most frequent triads were as follows: “300” (fully connected), which also presented the highest variability; “210”; “201” and “111D”. Additionally, classes with lower ties, involving sparse connections, seemed to be recurrent structures in these types of networks. For example, if we consider classes with “0” as first number (corresponding to all the isomorphism classes having zero mutual edges), we can also observe median values greater than zero and a certain amount of variability, expressed in terms of standard deviation. Moreover, several isomorphism classes appeared less frequently in football games, such as the types “030C” and “030T”, involving three directed links. 

These findings revealed uncommon types of triadic relations in passing networks: type “030C” refers to cyclic ties, i.e., _A_ → _B_ → _C_ → _A_ , while “030T” represents transitive triads of the form _A_ → _B_ → _C, A_ → _C_ . To summarize, such classes mainly concern transitivity structure and share the presence of three directed links (arrows). The reasons behind these low counts remain somewhat unclear, but could be linked to the direction of the ball (clearly related to the main aim of the game) and positions on the pitch (initial formation). Another issue can be represented by the possibility of “structural” zero issue (Block 2015). Some triad counts can be constrained to zero in particular conditions (i.e., the “003” case if all players nearly make a pass to each individual other player). In general, we remark that, similarly to the dyad census case, the total number of triads for each team ( _n_ = 11 players) in each match was constrained _n_ to 165, i.e., . ( 3 ) 

Figure 4 shows the distribution of triad counts for the three UCL Seasons, confirming some considerations mentioned above. 

In Figure 5, the first 10 teams are plotted according to their average value for all 16 isomorphism classes. We immediately noticed that skilful teams such as Real Madrid, Barcelona and Manchester City presented an average of “300” counts, which is always greater than 70. On the other hand, teams such as Anderlecht, Dinamo Zagreb and Leicester were more likely to present counts of disconnected or partially non-connected triads (such as “003” and “012”). 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 133** 

**Table 3:** Descriptive statistics of MAN in football UCL data. 

|**Edge type**||**2016–2017**|**2017–2018**|**2018–2019**|**Overall**|
|---|---|---|---|---|---|
|Mutual|Mean|36.61|36.16|36.48|36.42|
||SD|5.32|5.41|5.10|5.27.00|
||Min|17.00|19.00|21.00|17.00|
||Q1|33.00|33.00|34.00|33.00|
||Median|37.00|37.00|36|37.00|
||Q3|40|40.00|40.00|40.00|
||Max|46|49.00|47.00|49.00|
|Asymmetric|Mean|12.21|12.51|12.57|12.43|
||SD|4.13|3.91|4.10|4.04|
||Min|3.00|4.00|3.00|3.00|
||Q1|9.00|10.00|9.00|10.00|
||Median|12.00|12.00|12.00|12.00|
||Q3|15.00|15.00|15.00|15.00|
||Max|26.00|23.00|25.00|26.00|
|Null|Mean|6.17|6.33|5.94|6.15|
||SD|2.94|3.04|2.75|2.91|
||Min|0.00|1.00|0.00|0.00|
||Q1|4.00|4.00|4.00|4.00|
||Median|6.00|6.00|6.00|6.00|
||Q3|8.00|8.00|8.00|8.00|
||Max|17.00|19.00|15.00|19.00|



**Table 4:** Summary statistics of triad census. 

|**Triad**|**Mean**|**SD**|**Min**|**Q1**|**Median**|**Q3**|**Max**|
|---|---|---|---|---|---|---|---|
|003|0.33|0.93|0|0|0|0|10|
|012|1.87|2.60|0|0|1|3|23|
|021C|1.70|2.03|0|0|1|2|13|
|021D|0.84|1.22|0|0|0|1|9|
|021U|0.89|1.22|0|0|1|1|7|
|030C|0.48|0.85|0|0|0|1|5|
|030T|1.90|2.46|0|0|1|3|20|
|102|5.43|4.82|0|2|4|7|29|
|111D|9.70|4.42|0|7|10|12|25|
|111U|8.55|4.71|0|5|8|11|24|
|120C|7.36|4.63|0|4|7|10|22|
|120D|5.60|3.99|0|3|5|8|27|
|120U|4.82|3.43|0|2|4|7|21|
|201|18.11|7.49|0|13|18|23|43|
|210|42.17|9.44|16|36|43|48|70|
|300|55.24|20.28|6|41|54|69|118|



In keeping with this, triadic information could be summarized by factor analysis. We followed the approach of Faust (2006) to investigate the “resemblance” of triad census in empirical networks, although several approaches may be conducted to make dimensionality reduction (see Greenacre 1984, for a comprehensive overview). In practice, 

we applied the Correspondence Analysis (CA) to the original data, where the 16 isomorphism classes can be viewed as the modalities of a single variable by looking at data as a crosstabulation between two categorical variables. Each row of the input matrix represents a team in a match that occurred during the Group Stage of the UCL, while the counts of all the isomorphism classes are arranged in columns. 

Considering all networks, the first two dimensions of the CA explain the more than 60 % “triadic” variability, with 38.4 % for the first dimension and 22.9 % for the second. The third dimension also explains the 6.3 % “triadic” variability. 

The scree plot of Figure 6 suggests the presence of at least three factors (67.6 % of the overall variability) according to the conventional Kaiser criterion (Kaiser 1960). According to the above results, we focused on these three dimensions. Furthermore, Figure 7 shows both individuals (passing networks of teams) and isomorphism classes on the factor map in first two dimensions. The first dimension is mainly characterized by the presence or absence for connections, with opposing classes such “012C”, “021D” and “021U” against the fully connected type, i.e., “300”. Hence, the second dimension is mainly driven by differences between “210”, i.e., including two transitive connections and two disconnected vertices, and “210”, presenting 

> **134 —** L. Palazzo et al.: Testing styles of play using triad census distribution 



<!-- Start of picture text -->
120<br>90<br>60<br>30<br>0<br>003 012 021C 021D 021U 030C 030T 102 111D 111U 120C 120D 120U 201 210 300<br><!-- End of picture text -->

**Figure 4:** Distribution of isomorphism classes in Group Stage of Uefa Champions League ( _n_ = 576). 

Then, in Figure 8, we can observe the contribution of all 16 isomorphism classes for the first three CA dimensions in terms of squared cosines (or squared correlations). These quantities directly express the acceptability of the triad projections along the three dimensions; that is, these quantities can be used to measure the quality of the representation of each isomorphism class on the factor map. For the first dimension, the “300” class is the best represented in terms of squared cosine, reaching a high value of 91 %, followed by “012C”, “012” and “111U” with values higher than 45 %. In general, only “201” and “210” appear to be almost orthogonal with respect to the first factor. Regarding the second dimension, satisfyingly represented classes in terms of squared cosine were “102” (including only a single mutual link between three agents), as well as “120” and “210”, presenting two transitive links. Interestingly, the three classes “012D”, “012U” and “012C” are not correlated with the second factor. Only classes “003” and “201” appeared to be correlated with the third dimension. 

We also graphically identify the isomorphism classes that presents the higher contribution to the first three CA dimensions (Figure 9). Classes “300”, “120”, “012” and “210” are greater than the empirical threshold of 1∕( _m_ − 1), while “030T” and “003” are almost equal to this value. Other triads appear redundant to explain the variability of the football passing network. 

Finally, starting from these results, we applied _k_ -means clustering in order to establish a set of motivated profiles, defining a proper null hypothesis for the OSDM test. This allowed us to identify a set of triadic profiles that are related to different triadic behaviours in football. We chose _𝜅_ = 4 clusters based on the total within-cluster sum of squares. 

The four resulting centroids are plotted on the factor map as supplementary points in Figure 7, and their reconstructed triads are found in Table 5 and compared with the general median of the overall teams. 

Table 5, shows that the first centroid _T_ 1 presents a number of “102” and “201” greater than the general medians, while the second one ( _T_ 2) presents lower “201” and greater 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 135** 

|300<br>120D<br>102<br>021D<br>0<br>20<br>40<br>60<br>80<br>0<br>5<br>10<br>0<br>3<br>6<br>9<br>0<br>1<br>2|
|---|
|Anderlecht<br>Sporting Lisbon<br>Inter<br>Maribor<br>Spartak Moskov<br>Qarabag<br>Rostov<br>Dynamo Zagreb<br>Schalke 04<br>Red Star Belgrade<br>Inter<br>Olympiacos<br>Atletico Madrid<br>Schalke 04<br>Ajax<br>APOEL<br>Celtic<br>Dinamo Kiev<br>Monaco<br>Anderlecht<br>Spartak Moskov<br>Legia Warsav<br>CSKA Moskov<br>Copenaghen<br>Dynamo Zagreb<br>Valencia<br>Young Boys<br>Bayer Leverkusen<br>Lokomotiv Moskov<br>Rostov<br>PSG<br>Roma<br>Sevilla<br>Borussia Dortmund<br>Arsenal<br>Bayern Munchen<br>Juventus<br>Barcelona<br>Manchester City<br>Real Madrid|
|210<br>120C<br>030T<br>021C<br>10<br>20<br>30<br>40<br>50<br>5<br>10<br>2<br>4<br>6<br>2<br>4<br>6|
|5<br>0<br>0<br>0<br>0<br>PSV<br>Hoffenheim<br>Rostov<br>Maribor<br>Olympiacos<br>Schalke 04<br>Red Star Belgrade<br>Leicester<br>APOEL<br>Dynamo Zagreb<br>Celtic<br>Bayer Leverkusen<br>Leicester<br>Viktoria Plzen<br>Galatasaray<br>Lokomotiv Moskov<br>APOEL<br>AEK Athens<br>Dynamo Zagreb<br>Rostov<br>Bayer Leverkusen<br>Besiktas<br>Feyenord<br>AEK Athens<br>Lokomotiv Moskov<br>Maribor<br>Qarabag<br>Red Star Belgrade<br>Copenaghen<br>Galatasaray<br>Brugge<br>PSG<br>Besiktas<br>Legia Warsav<br>Tottenham<br>Bayer Leverkusen<br>Galatasaray<br>Shakhtar Donetsk<br>Copenaghen<br>Lokomotiv Moskov|
|201<br>111U<br>030C<br>012<br>0<br>5<br>10<br>15<br>20<br>2<br>0<br>5<br>10<br>15<br>0.0<br>0.5<br>1.0<br>1.5<br>0<br>2<br>4<br>6|
|Monaco<br>Leicester<br>Leipzig<br>Celtic<br>Maribor<br>Schalke 04<br>Olympiacos<br>Dynamo Zagreb<br>APOEL<br>Anderlecht<br>Spartak Moskov<br>Celtic<br>Lokomotiv Moskov<br>Schalke 04<br>AEK Athens<br>Red Star Belgrade<br>PSV<br>Besiktas<br>Copenaghen<br>Dynamo Zagreb<br>Feyenord<br>Inter<br>Celtic<br>PSV<br>Leicester<br>Olympiacos<br>Hoffenheim<br>APOEL<br>Maribor<br>Schalke 04<br>Leicester<br>Maribor<br>Celtic<br>Monaco<br>Napoli<br>Schalke 04<br>Viktoria Plzen<br>Lyon<br>Benfica<br>Sporting Lisbon|
|120U<br>111D<br>021U<br>003<br>0<br>2<br>4<br>6<br>8<br>0<br>5<br>10<br>15<br>0<br>1<br>2<br>3<br>0.0<br>0.5<br>1.0<br>1.5<br>2.0<br>2.5<br>Leicester<br>Maribor<br>Celtic<br>APOEL<br>Dinamo Kiev<br>Olympiacos<br>Schalke 04<br>Monaco<br>Dynamo Zagreb<br>Anderlecht<br>Maribor<br>Olympiacos<br>PSV<br>Spartak Moskov<br>Viktoria Plzen<br>Red Star Belgrade<br>Leicester<br>Rostov<br>Dynamo Zagreb<br>APOEL<br>Anderlecht<br>Dinamo Kiev<br>Legia Warsav<br>CSKA Moskov<br>Spartak Moskov<br>Dynamo Zagreb<br>PSV<br>APOEL<br>Valencia<br>Rostov<br>Celtic<br>Feyenord<br>Hoffenheim<br>Qarabag<br>Lokomotiv Moskov<br>Leicester<br>Red Star Belgrade<br>AEK Athens<br>Bayer Leverkusen<br>Copenaghen|



**Figure 5:** First 10 European Teams for all isomorphism classes (average values). 

> **136 —** L. Palazzo et al.: Testing styles of play using triad census distribution 



<!-- Start of picture text -->
40<br>30<br>20<br>10<br>0<br>1 2 3 4 5 6 7 8 9 10<br><!-- End of picture text -->

**Figure 6:** Scree plot of the CA on triad census. Red dashed line indicates the reference value 1∕( _m_ − 1), where _m_ is the number of modalities. 

“210” and “120” (D, U, C) types. The centroid denoted as _T_ 3 shows the highest counts of fully connected triads, i.e., “300” (exceeding the general median of 22 units), while on the contrary, centroid _T_ 4 exhibits the lower value of this class 

and the higher counts of triads with a low number of links, i.e., “012” and “102”. 

### **4.2 Testing the presence of a strategy** 

After performing a statistical comparison of triad census, we empirically evaluated differences between the observed triads of the football teams against their conditional random reference, i.e., the U|MAN, following the methodology presented in Section 3.1. 

Figure 10 graphically shows the distribution over three UCL Seasons of _𝜏 u_ statistics as defined in Section 3.1. As expected, such statistics did not seem to show substantial changes among seasons both in terms of location (mean or median) and scale (variability expressed through interquartile range), although there were some exceptions (see, for example, type “030C”). Moreover, most connected classes, i.e., “201”, “210” and “300” as well as “102” and “111D”, present evidence against the theoretical values of the random graph scenario, i.e., the null hypothesis discussed in Section 3.1 (here represented by a dashed red line) more often than others. 



<!-- Start of picture text -->
1.5 003<br>1.0<br>102<br>012<br>0.5<br>T4<br>201<br>T1 111U<br>300 111D 021U<br>0.0<br>T3 021C 021D<br>210 T2<br>120C<br>120D 120U<br>−0.5<br>030T<br>030C<br>−0.5 0.0 0.5 1.0<br>Dim1 (38.4%)<br>Dim2 (22.9%)<br><!-- End of picture text -->

**Figure 7:** Biplot of first two CA factors. Red arrows are isomorphism classes and grey points are the networks (matches). Blue supplementary points represent coordinates of four _k_ -means centroids explained in the text. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 137** 



**Figure 8:** Heatmap of squared cosines related with triads in the CA dimensions. 

In order to carry out the formal test introduced in Section 3.1, we computed _𝜏_ max<sup>2statisticsforallavailable</sup> UCL matches. Table 6 contains the percentage of _p_ -values associated with _𝜏_<sup>2whicharelowerthanconventional</sup> max<sup>,</sup> nominal levels, i.e., 0.1, 0.05 and 0.01, even divided by the three Seasons (576 matches). Since we are considering multiple testing, we also included the rejection frequencies adjusted using the Bonferroni correction (i.e., _p_ = _𝛼_ ∕ _G_ ). The proportion of _p_ -values lower than nominal levels can vary from 24 % (when the nominal level is 0.01) to 53 % with a greater I error type, and it is noticeable that first Season (2016–2017) presents the highest number of rejections. Using the Bonferroni correction for multiple testing, we observed lower rejection frequencies, and the null hypothesis of U|MAN structure can be rejected for one-tenth of the networks. 

Despite these unexciting results, we should remark that (a) a test based on _𝜏_ max<sup>2statistic may be more conservative</sup> in finite samples, mainly due to the well-known asymptotic approximation issue, and (b) the (conditional) distribution of _𝜏_ max<sup>2underthenullhypothesisoftriadicrandomness</sup> strictly depends on the linear dependence occurring in the 

triad census matrix (i.e., its rank). For example, in our football data, we found a mode of 13 for the ranking of the triad census matrix among all networks. As discussed in Section 3.1, this number corresponds to the degrees of freedom in the _𝜏_ max<sup>2statistic under the null hypothesis of a</sup> random graph. 

Ultimately, we can conclude that more than 40 % of the football teams involved in a match showed strong empirical evidence in terms of triadic behaviour against their random graph counterparts based on U|MAN. 

Table 7 contains the rejection frequencies, at a 5 % nominal level, for European teams during the three Seasons. PSG rejected all the times in Season 2017–2018, followed by Real Madrid, Porto and Rostov also rejecting the randomness five times out of six in the previous Season. Considering all Seasons, Atletico Madrid rejected the null hypothesis two times out of three (12 matches), followed by PSG (9 matches over 18). Surprisingly, team such as Borussia Dortmund rejects the null for only one match over 18. 

**Table 5:** Reconstructed Triad census of _k_ -means based centroids. 



<!-- Start of picture text -->
20<br>15<br>10<br>5<br>0<br>300 102 012 201030T 003120C111U021C120U120D 210111D021D021U030C<br>Contributions (%)<br><!-- End of picture text -->

**Figure 9:** Contributions of isomorphism classes to the CA dimensions. Red dashed line is the reference value 1∕15. 

|**Class**|**_T_**|**_T_**|**_T_**|**_T_**|**Median**|
|---|---|---|---|---|---|
|003|0|0|0|2|0|
|012|2|2|1|9|1|
|102|8|3|3|16|4|
|021D|1|1|0|2|0|
|021U|1|1|0|3|1|
|021C|2|2|1|5|1|
|111D|11|11|7|14|10|
|111U|11|10|5|14|8|
|030T|1|4|1|3|1|
|030C|0|1|0|1|0|
|201|24|13|16|22|18|
|120D|4|9|4|5|5|
|120U|4|8|3|5|4|
|120C|6|12|5|8|7|
|210|39|48|43|30|43|
|300|51|40|76|26|54|



> **138 —** L. Palazzo et al.: Testing styles of play using triad census distribution 



<!-- Start of picture text -->
8<br>4<br>0<br>−4<br>8<br>4<br>0<br>−4<br>8<br>4<br>0<br>−4<br>003 012 021C 021D 021U 030C 030T 102 111D 111U 120C 120D 120U 201 210 300<br>16−17<br>17−18<br>18−19<br><!-- End of picture text -->

**Figure 10:** Boxplot of _𝜏 u_ statistics, showing discrepancies between triad frequencies and expected frequencies under U|MAN distribution per Season. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 139** 

**Table 6:** Percentages of rejection at a fixed nominal levels (Conventional – Conv) and using Bonferroni’s (Bonf) correction for the _𝜏_ max<sup>2statistics.</sup> 

|**Season**|**_p <_ **|**0.1**|**_p <_ **|**0.05**|**_p <_ **|**0.01**|
|---|---|---|---|---|---|---|
||**Conv**|**Bonf**|**Conv**|**Bonf**|**Conv**|**Bonf**|
|2016–2017|53 %|11 %|44 %|10 %|31 %|9 %|
|2017–2018|43 %|11 %|35 %|8 %|24 %|7 %|
|2018–2019|43 %|8 %|35 %|7 %|24 %|6 %|
|2016–2019|46 %|10 %|38 %|8 %|27 %|7 %|



The reasons of those rejections can be significantly vary. In some cases, they are driven by high levels of isomorphism classes with low connection (i.e., “012” or “120”); in other cases, the teams are able to exhibit a large number of connected triads (i.e., types “300” or “210”), as well as 

providing the expected values of their MAN distribution. If we consider the adjusted error rate to be equal to 0.05∕192, we can observe that the test was rejected two times out of six (in each Season) for the following teams: Manchester City and Benfica (2016–2017), Real Madrid and Anderlecht (2017–2018), and Valencia (2018–2019). 

### **4.3 Triad census and style of play** 

We further tested for the presence of a “structural equivalence” in terms of triadic relationships applying the OSDM test outlined in Section 2.2. First, the OSDM test was applied considering the six matches of each team in the three Seasons. Thus, we formalized four null hypotheses based upon the four cluster centroids reconstructed in Table 5 of Section 4.1. 

**Table 7:** Number of matches in which each team rejects the _𝜏_ max<sup>2in each Season at 5 % significance level. Results based on Bonferroni’s correction are</sup> depicted in brackets. 

|**Season 2016–2017**|**_p <_ 0.05**|**Season 2017–2018**|**_p <_ 0.05**|**Season 2018–2019**|**_p <_ 0.05**|
|---|---|---|---|---|---|
|Porto|5 (1)|PSG|6 (1)|Atletico Madrid|4 (1)|
|Rostov|5 (1)|Real Madrid|5 (2)|Valencia|4 (2)|
|Arsenal|4 (1)|Atletico Madrid|4 (1)|Ajax|3 (1)|
|Atletico Madrid|4 (0)|Chelsea|4 (1)|Barcelona|3 (0)|
|Basel|4 (1)|Liverpool|4 (1)|Brugge|3 (0)|
|Bayer Leverkusen|4 (1)|Qarabag|4 (0)|CSKA Moskov|3 (1)|
|Bayern Munchen|4 (0)|Anderlecht|3 (2)|Hoffenheim|3 (0)|
|<br>Celtic|4 (0)|Juventus|3 (0)|Inter|3 (0)|
|Manchester City|4 (2)|Napoli|3 (0)|Juventus|3 (0)|
|Brugge|3 (1)|Olympiacos|3 (0)|Lokomotiv Moskov|3 (1)|
|CSKA Moskov|3 (0)|Tottenham|3 (1)|Manchester United|3 (0)|
|Juventus|3 (1)|Barcelona|2 (0)|Monaco|3 (0)|
|Lyon|3 (0)|Besiktas|2 (1)|Red Star Belgrade|3 (1)|
|Monaco|3 (0)|Manchester City|2 (1)|Roma|3 (1)|
|Napoli|3 (0)|Porto|2 (1)|Bayern Munchen|2 (1)|
|PSV|3 (0)|Roma|2 (1)|Manchester City|2 (0)|
|Sevilla|3 (1)|Sevilla|2 (1)|Napoli|2 (0)|
|Tottenham|3 (1)|Spartak Moskov|2 (1)|PSV|2 (0)|
|Barcelona|2 (1)|Bayern Munchen|1 (0)|Real Madrid|2 (0)|
|Benfica|2 (2)|Benfica|1 (0)|Tottenham|2 (1)|
|Besiktas|2 (0)|Borussia Dortmund|1 (0)|Viktoria Plzen|2 (0)|
|Legia Warsav|2 (1)|Celtic|1 (0)|Young Boys|2 (1)|
|Leicester|2 (0)|CSKA Moskov|1 (0)|AEK Athens|1 (0)|
|Ludogorets|2 (1)|Leipzig|1 (1)|Benfica|1 (0)|
|PSG|2 (1)|Manchester United|1 (0)|Liverpool|1 (0)|
|Sporting Lisbon|2 (0)|Maribor|1 (0)|Lyon|1 (0)|
|Borussia Gladbach|1 (0)|Monaco|1 (0)|Porto|1 (0)|
|Copenaghen|1 (0)|Shakhtar Donetsk|1 (0)|PSG|1 (0)|
|Dynamo Kiev|1 (1)|Sporting Lisbon|1 (0)|Schalke|1 (1)|
|Real Madrid|1 (1)|APOEL|0 (0)|Shakhtar Donetsk|1 (1)|
|Borussia Dortmund|0 (0)|Basel|0 (0)|Borussia Dortmund|0 (0)|
|Dynamo Zagreb|0 (0)|Feyenord|0 (0)|Galatasaray|0 (0)|



> **140 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

In Tables 9–12 (depicted in Appendix D) we rank the teams according to their OSDM estimated statistics and their associated _p_ -value in the three UCL Seasons. Regarding the first system, denoted as _T_ 1, it can be seen that the null hypothesis cannot be rejected for almost all Dutch and French teams (excluding the first Season of PSG) and the Spanish teams of Atletico Madrid and Seville. Similar to this strategy are most of the Italian teams, such as Naples, Rome (2017–2018) and Inter. 

If we consider the null hypothesis constructed upon _T_ 2, few teams were ultimately reflected in this strategy. Notably, however, all Russian teams (CSKA Moscow, Spartak and Lokomotiv Moscow) were unable to reject the hypothesis at a 5 % nominal level throughout the three UCL seasons. These teams are followed by other “Eastern” Teams such as Qarabag, Galatasaray, AEK Athens and Warsaw. 

As mentioned, the third cluster ( _T_ 3) contains teams that generally produce more closed triads between players. For all three years, we found that the OSDM could not be rejected for Manchester City, Juventus, Real Madrid, Bayern Munchen, Borussia Dortmund and Barcelona (except the preceding Season). Finally, almost all teams rejected the null hypothesis _T_ 4 based on the four centroids. 

Another possibility is given by the use of “reference” teams as null hypothesis. This kind of test consists of imposing under the null hypothesis a specific parameter scheme derived from a set of chosen teams, e.g., by using the triadic median. In Tables 13–15 (Appendix D), we perform the OSDM test for each of the proposed reference teams, ranking the teams according to their OSDM estimated statistic and its associated _p_ -value in the three UCL Seasons. 

Considering only the first examples for the sake of brevity, European teams that were closer to Real Madrid in a triadic point of view were Barcelona (2017–18 and 2018–19), Juventus (2017–18 and 2018–19) Bayern Munchen (2016–17 and 2018–19), PSG (first two Seasons), but also Naples and Borussia Dortmund (last Season) and Arsenal (first Season). Conversely, in terms of triadic distribution it can be found in Dynamo Zagreb, Rostov, Spartak Moscow, APOEL and PSV. 

We would like to note that the results of the OSDM test discussed here are highly similar considering the adjusted type I error rate obtained through the Bonferroni correction. Indeed, observing the Tables in Appendix D, the null hypothesis can be rejected for all the teams such that _p < 𝛼_ ∕192, approximately equal to 0.0003 when _𝛼_ = 0.05. 

To conclude, network structure and triadic analysis can provide information for trainers, coaches and policymakers in football. Triad census can highlight tactical and technical aspects, and may be able to separate out the cohesion of a team in terms of passing behaviour, clarifying types and the strength of relationships among players, as well as express the collectivity of sub-groups. Therefore, from a tactical perspective, knowledge of opposite triadic distribution may provide a specific improvement both at individual level and for the overall team, also becoming relevant to the outcome of a game, e.g., the probability of winning. 

## **5 Conclusions and future works** 

Passing networks may provide useful information on the style of play and performance of football teams (Diquigiovanni and Scarpa 2019). In addition, descriptive analysis of dyads and triads is common in the social network analysis field. In particular, triad census is capable of characterizing the network structure, including from a comparative perspective. The present paper exploits the potential of the triad census to analyse networks, interpreting the presence or absence of specific triads as characteristics of different playing styles and/or coaching strategies. 

Given some levels of probabilistic assumptions, we showed that it is possible to retrieve a particular triadic configuration in football matches. On such bases, we adopted two types of formal tests. The former was an omnibus test used to determine whether the triadic distribution of teams deviated from randomness. The latter was a DM-based test redesigned to assume a null hypothesis of adherence to a given strategy (in terms of triadic configuration) or to detect similarity between teams. 

In our case study, the omnibus test evidenced that there were teams particularly able to create as many links as possible, while other teams showed their strategy to be built on making few connections between players. Moreover, since football teams are always oriented by real-time coach strategies, often the triad census of such teams may be similar to those obtained via random graphs based on the U|MAN assumptions. This means that sometimes the football teams were unable to pursue a given strategy. The reasons for this might lie in several causes, e.g., when the opponent is able to break the playing schemes, when players are not particularly skilful with respect to the opponents, or in the absence of influential players having a key role in sorting passes. 

From a slightly different point of view, the OSDM tests help to identify almost three different strategies according to the triadic distribution. One in particular ( _T_ 3) was related 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 141** 

to the highly tactical and technical teams, able to reach around 70 % of two types of more connected triads (“300” and “210”). Another strategy (denoted as _T_ 1) seemed to be prerogative of Dutch and French teams, presenting greater balance between types “210” and “201”. A third group ( _T_ 2) was mainly composed of teams from Eastern Europe, sharing the types of triad “120” characterized by asymmetric links. As mentioned, this approach can be also used to rank teams according to a specific null hypothesis. We have also tried to use reference teams to see how teams can be close to or far from the triadic behaviour arising from the null hypothesis. 

Despite the usefulness of this analysis, the next step would be the development of a weighted triad approach to take into account the different degrees of connections between players involved in a match. In this regard, a further methodology to combine the isomorphism classes of directed networks with the degree of links connecting nodes (e.g., the number of passes between players) should be developed. Moreover, a potential approach to extend the analysis to the weighted cases has been suggested by Onnela et al. (2005), even if applied in a different framework. To the best of our knowledge, a similar approach has not been fully explored in the current literature. 

Indeed, passes may have different features according to their length, their position on the pitch (Rein, Raabe, and Memmert 2017), the role of players involved and last but not least, their effectiveness in creating chances (Bransen, Van Haaren, and van de Velden 2019). 

**Author contributions:** All the authors have accepted responsibility for the entire content of this submitted manuscript and approved submission. 

**Research funding:** None declared. 

**Conflict of interest statement:** The authors declare no conflicts of interest regarding this article. 

## **Appendix A: Moments of the U** | **MAN distribution** 

In this Section we depict the expected value, the variance and the covariance of the U|MAN distribution: 





where the set of probabilities _p_ ( _𝜂_ ), _p_ 0( _𝜂, 𝜈_ ), _p_ 2( _𝜂, 𝜈_ ) are computed in Holland and Leinhardt (1976) (Tables 2–4) (2) and the symbol ( _n_ 3 ) represents the descending factorial ( _n_ 3 )[( _n_ 3 ) − 1]. 

## **Appendix B: The Dirichlet-Multinomial distribution** 

The DM distribution (also known as Dirichlet-Compound Multinomial, multivariate Binomial-Beta distribution or multivariate Pòlya, as defined in Ishii and Hayakawa 1960; Johnson, Kotz, and Balakrishnan 1997), is a family of discrete multivariate probability distributions on a finite support of non-negative integers. Consider a random vector of _m_ distinct modality counts **x** = ( _x_ 1 _,_ … _, xm_ ), the density function of a DM distribution with parameters **_𝜶_** = ( _𝛼_ 1 _,_ … _, 𝛼m_ ) is 



where _xi_ ∈ ℕ ∪{0}, min _i_ ( _xi_ ) _>_ 0 and<sup>∑</sup><sup>_m_</sup> _i_ =1<sup>_xi_=</sup><sup>_x_0 is the sum</sup> of all modalities’ counts. Distribution parameters are positive, i.e., _𝛼i >_ 0, and<sup>∑</sup><sup>_m_</sup> _i_ =1<sup>_𝛼i_=</sup><sup>_𝛼_0.</sup> 

Alternatively, a different parametrization is given setting _𝛼_ 0 = (1 − _𝜃_ )∕ _𝜃_ and _𝛼i_ = _𝜋i_ (1 − _𝜃_ )∕ _𝜃_ , with _i_ = 1 _,_ … _, m_ . In this case parameters _𝜋i_ represent the (theoretical) relative frequencies of each modality, while _𝜃_ is an overdispersion parameter. The density function in Equation (12) then becomes 





Obviously, the same constraints already defined on the support hold, while the new parameter constraints equal to 0 ≤ _𝜋i_ ≤ 1, _𝜃_ ≥ 0 and<sup>∑</sup><sup>_m_</sup> _i_ =1<sup>_𝜋i_= 1. DM distribution has been</sup> formally defined as a compound distribution where a probability vector **_𝝅_** is assumed to follow a Dirichlet distribution and an observation **x** is drawn from a Multinomial distribution with given probability vector **_𝝅_** and _x_ 0 number of trials. 

> **142 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

Using the second parametrization and following Tvedebrink (2010), it is possible to derive mean and variance of the random variable 





**Table 8:** Size of OSDM test at nominal level _𝛼_ = 0.05. 

|**_n_**|**_m_ = 16**|
|---|---|
|6|0.0766|
|13|0.0598|
|38|0.0544|
|50|0.0524|



It is worth to note that distribution parameters do not directly depend on total counts _x_ 0 of all the occurrences present in the sample, but only on the relative frequencies of each modality. 

## **Appendix C: Performance of OSDM test in small samples** 

Here we perform a small-scale Monte Carlo experiment to obtain the empirical size and power of the OSDM test. We generate 100,000 Monte Carlo samples from a DirichletMultinomial distribution **X** ∼ DM _m_ ( **_𝝅_** _, 𝜃_ ). 

We set a fixed _𝜃_ = 0.01 generating 6 observations having _m_ = 16 modalities and a total number of triads for each team equal to 165, mimicking the structure of football data. The parameter scheme under the null hypothesis equals to _𝜋i_ = 1∕16, for _i_ = 1 _,_ … _,_ 16. To compute the power we let variate the set of probabilities by unbalancing one of the frequencies proportionally to the remaining others, i.e., _𝜋_ 1 = 

1∕16 ± _k_ , with _k_ ∈{0 _,_ 0.01 _,_ 0.02 _,_ …}, and _𝜋h_ = (1 − _𝜋_ 1)∕15, ∀ _h_ = 2 _,_ … _, m_ . 

In Table 8 the size of the test is computed as function of increasing sample size while the empirical power of the OSDM test is depicted in Figure 11, according to different values of _k_ . The null hypothesis is in correspondence of _k_ = 0. 

We have to remark that power analysis of OSDM test can be exploited in many ways and here we present only a possible scenario related to changes in a single count. More power analysis will be carried out in further research to take into account the multidimensional nature of the test. 

## **Appendix D: Results of OSDM tests** 

In what follows we present the results of the OSDM test considering firstly the centroids of _k_ -means after CA, and then using reference teams (i.e., three different styles of play). 



<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>−0.04 0.00 0.04<br>k<br><!-- End of picture text -->

**Figure 11:** Empirical power of the OSDM test as function of _k_ with _n_ = 6 samples. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 143** 

**Table 9:** Results of one-sample DM test under _H_ 0: _T_ 1. 

|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|---|---|---|---|---|---|
|PSV|2.90 (0.9997)|Leipzig|6.78 (0.9634)|Monaco|6.77 (0.9636)|
|Dinamo Kiev|3.24 (0.9994)|Napoli|8.69 (0.8932)|Inter|7.29 (0.9492)|
|Borussia Gladbach|4.40 (0.9961)|Benfica|10.97 (0.7548)|Benfica|8.90 (0.8826)|
|Monaco|4.55 (0.9953)|Olympiacos|11.28 (0.7322)|Atletico Madrid|9.69 (0.8385)|
|Lyon|9.05 (0.8750)|Liverpool|12.31 (0.6551)|Lyon|11.40 (0.7236)|
|Atletico Madrid|9.36 (0.8580)|Celtic|13.97 (0.5282)|Ajax|13.06 (0.5973)|
|Napoli|10.62 (0.7792)|Feyenord|14.65 (0.4766)|PSG|18.08 (0.2584)|
|Benfica|11.49 (0.7170)|Anderlecht|15.81 (0.3951)|Liverpool|18.75 (0.2255)|
|Barcelona|11.66 (0.7046)|Borussia Dortmund|16.12 (0.3741)|Porto|19.09 (0.2096)|
|Sporting Lisbon|14.13 (0.5159)|Monaco|16.47 (0.3514)|Napoli|19.74 (0.1821)|
|Sevilla|15.29 (0.4310)|Sevilla|17.55 (0.2872)|Roma|20.92 (0.1394)|
|Legia Warsav|17.54 (0.2874)|Atletico Madrid|17.79 (0.2738)|Shakhtar Donetsk|21.19 (0.1308)|
|Manchester City|18.61 (0.2319)|Chelsea|17.82 (0.2723)|Valencia|21.81 (0.1128)|
|Tottenham|18.79 (0.2233)|CSKA Moskov|19.04 (0.2118)|Viktoria Plzen|23.23 (0.0794)|
|Ludogorets|21.99 (0.1081)|Porto|20.52 (0.1530)|Manchester United|23.30 (0.0779)|
|Arsenal|24.44 (0.0580)|Basel|22.81 (0.0883)|Hoffenheim|24.07 (0.0639)|
|Basel|27.24 (0.0269)|PSG|23.48 (0.0745)|Tottenham|26.40 (0.0340)|
|Besiktas|30.10 (0.0116)|Sporting Lisbon|25.16 (0.0478)|Schalke 04|26.71 (0.0312)|
|Brugge|30.97 (0.0089)|Roma|26.71 (0.0312)|Brugge|26.96 (0.0291)|
|Leicester|31.04 (0.0087)|Manchester City|28.93 (0.0164)|Juventus|30.16 (0.0114)|
|Juventus|32.60 (0.0053)|Maribor|29.30 (0.0147)|Manchester City|38.01 (0.0009)|
|CSKA Moskov|38.41 (0.0008)|Manchester United|29.48 (0.0140)|Bayern Munchen|40.64 (0.0004)|
|Porto|42.90 (0.0002)|Juventus|32.41 (0.0057)|CSKA Moskov|40.97 (0.0003)|
|PSG|46.35 (0.0000)|Qarabag|36.82 (0.0013)|Barcelona|41.34 (0.0003)|
|Celtic|54.48 (0.0000)|Besiktas|41.15 (0.0003)|Galatasaray|43.55 (0.0001)|
|Bayer Leverkusen|70.43 (0.0000)|Barcelona|52.97 (0.0000)|Real Madrid|44.62 (0.0001)|
|Borussia Dortmund|71.42 (0.0000)|Shakhtar Donetsk|70.90 (0.0000)|AEK Athens|48.64 (0.0000)|
|Bayern Munchen|74.65 (0.0000)|Tottenham|71.27 (0.0000)|Young Boys|50.40 (0.0000)|
|Real Madrid|79.34 (0.0000)|APOEL|93.73 (0.0000)|Red Star Belgrade|51.80 (0.0000)|
|Rostov|110.25 (0.0000)|Real Madrid|97.06 (0.0000)|Borussia Dortmund|55.22 (0.0000)|
|Copenaghen|114.24 (0.0000)|Spartak Moskov|102.30 (0.0000)|PSV|102.70 (0.0000)|
|Dynamo Zagreb|117.70 (0.0000)|Bayern Munchen|114.20 (0.0000)|Lokomotiv Moskov|130.26 (0.0000)|



_p_ -Values are denoted in brackets. 

> **144 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

**Table 10:** Results of one-sample DM test under _H_ 0: _T_ 2. 

|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|---|---|---|---|---|---|
|Copenaghen|7.20 (0.9517)|Besiktas|7.38 (0.9463)|AEK Athens|4.45 (0.9959)|
|Legia Warsav|10.09 (0.8138)|Feyenord|8.12 (0.9191)|Galatasaray|8.98 (0.8783)|
|Bayer Leverkusen|12.72 (0.6239)|Qarabag|10.41 (0.7929)|Hoffenheim|11.33 (0.7286)|
|Brugge|15.16 (0.4396)|Basel|17.90 (0.2680)|Inter|13.32 (0.5774)|
|CSKA Moskov|15.25 (0.4338)|Tottenham|22.33 (0.0993)|CSKA Moskov|14.77 (0.4684)|
|Atletico Madrid|19.65 (0.1858)|Porto|22.35 (0.0989)|Lokomotiv Moskov|14.91 (0.4579)|
|Leicester|24.19 (0.0619)|Spartak Moskov|22.80 (0.0884)|Porto|18.34 (0.2454)|
|Borussia Gladbach|30.60 (0.0099)|<br>CSKA Moskov|23.71 (0.0701)|PSG|18.42 (0.2410)|
|Sevilla|30.94 (0.0089)|Benfica|25.85 (0.0396)|Young Boys|19.11 (0.2086)|
|Rostov|37.63 (0.0010)|Olympiacos|27.94 (0.0219)|Red Star Belgrade|19.75 (0.1816)|
|Arsenal|37.86 (0.0009)|Anderlecht|29.89 (0.0123)|<br>PSV|29.71 (0.0130)|
|Porto|40.11 (0.0004)|Liverpool|33.86 (0.0036)|Shakhtar Donetsk|31.93 (0.0066)|
|PSV|40.22 (0.0004)|Monaco|37.62 (0.0010)|Brugge|34.79 (0.0026)|
|Tottenham|42.66 (0.0002)|Roma|41.28 (0.0003)|Tottenham|35.71 (0.0019)|
|Monaco|44.32 (0.0001)|Leipzig|41.43 (0.0003)|Lyon|40.92 (0.0003)|
|Ludogorets|47.26 (0.0000)|Maribor|41.73 (0.0002)|Valencia|41.15 (0.0003)|
|Dinamo Kiev|48.14 (0.0000)|Celtic|44.30 (0.0001)|Monaco|44.43 (0.0001)|
|Lyon|50.38 (0.0000)|Chelsea|46.66 (0.0000)|Schalke 04|45.51 (0.0001)|
|Juventus|55.25 (0.0000)|PSG|55.12 (0.0000)|Viktoria Plzen|46.21 (0.0000)|
|Barcelona|56.30 (0.0000)|Manchester City|58.88 (0.0000)|Napoli|46.85 (0.0000)|
|Manchester City|56.76 (0.0000)|Juventus|67.04 (0.0000)|Juventus|48.27 (0.0000)|
|Dynamo Zagreb|58.36 (0.0000)|Borussia Dortmund|67.15 (0.0000)|Liverpool|48.59 (0.0000)|
|Celtic|60.57 (0.0000)|Sporting Lisbon|68.92 (0.0000)|Bayern Munchen|53.77 (0.0000)|
|Besiktas|65.48 (0.0000)|Sevilla|69.73 (0.0000)|Barcelona|66.90 (0.0000)|
|Basel|72.84 (0.0000)|APOEL|72.76 (0.0000)|Atletico Madrid|67.50 (0.0000)|
|Sporting Lisbon|73.57 (0.0000)|Manchester United|75.49 (0.0000)|Real Madrid|87.80 (0.0000)|
|PSG|86.32 (0.0000)|Napoli|82.39 (0.0000)|Benfica|91.45 (0.0000)|
|Benfica|89.62 (0.0000)|Shakhtar Donetsk|82.73 (0.0000)|Roma|93.40 (0.0000)|
|Napoli|105.42 (0.0000)|Atletico Madrid|86.50 (0.0000)|Manchester United|94.01 (0.0000)|
|Borussia Dortmund|146.99 (0.0000)|Barcelona|137.66 (0.0000)|Manchester City|95.29 (0.0000)|
|Real Madrid|153.74 (0.0000)|Real Madrid|190.99 (0.0000)|Borussia Dortmund|109.76 (0.0000)|
|Bayern Munchen|162.06 (0.0000)|Bayern Munchen|258.83 (0.0000)|Ajax|134.18 (0.0000)|



_p_ -Values are denoted in brackets. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 145** 

**Table 11:** Results of one-sample DM test under _H_ 0: _T_ 3. 

|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|---|---|---|---|---|---|
|PSG|2.68 (0.9998)|Juventus|2.06 (1.0000)|Napoli|2.14 (1.0000)|
|Borussia Dortmund|3.70 (0.9986)|Manchester City|3.06 (0.9995)|Barcelona|3.43 (0.9991)|
|Juventus|5.11 (0.9911)|Roma|6.28 (0.9747)|Juventus|3.69 (0.9986)|
|Tottenham|5.27 (0.9896)|Bayern Munchen|8.50 (0.9020)|Real Madrid|4.67 (0.9946)|
|Bayern Munchen|5.29 (0.9894)|Barcelona|10.81 (0.7658)|Borussia Dortmund|4.80 (0.9937)|
|Arsenal|5.50 (0.9870)|Real Madrid|14.93 (0.4564)|Manchester City|7.71 (0.9349)|
|Real Madrid|8.28 (0.9120)|Sevilla|17.45 (0.2929)|<br>Liverpool|9.98 (0.8212)|
|Manchester City|8.32 (0.9103)|Benfica|18.55 (0.2350)|Shakhtar Donetsk|11.13 (0.7436)|
|<br>Sevilla|10.08 (0.8148)|PSG|24.03 (0.0646)|Bayern Munchen|16.61 (0.3425)|
|Ludogorets|20.66 (0.1481)|Liverpool|24.37 (0.0591)|Tottenham|18.46 (0.2391)|
|Borussia Gladbach|21.91 (0.1102)|Borussia Dortmund|25.95 (0.0385)|Porto|22.84 (0.0876)|
|Atletico Madrid|24.22 (0.0614)|Shakhtar Donetsk|41.41 (0.0003)|Roma|26.84 (0.0301)|
|Lyon|25.92 (0.0388)|Manchester United|43.61 (0.0001)|Inter|33.14 (0.0045)|
|Barcelona|29.31 (0.0147)|Feyenord|43.76 (0.0001)|PSG|33.90 (0.0035)|
|Brugge|37.15 (0.0012)|Chelsea|47.27 (0.0000)|Atletico Madrid|40.36 (0.0004)|
|Besiktas|37.70 (0.0010)|Besiktas|56.04 (0.0000)|Lyon|59.08 (0.0000)|
|Monaco|45.24 (0.0001)|Leipzig|62.26 (0.0000)|Manchester United|62.69 (0.0000)|
|PSV|46.38 (0.0000)|Anderlecht|65.46 (0.0000)|Valencia|64.86 (0.0000)|
|Legia Warsav|50.04 (0.0000)|Napoli|65.58 (0.0000)|Galatasaray|68.41 (0.0000)|
|Porto|55.70 (0.0000)|Olympiacos|68.16 (0.0000)|Monaco|71.19 (0.0000)|
|Sporting Lisbon|55.90 (0.0000)|Tottenham|69.82 (0.0000)|Ajax|75.38 (0.0000)|
|Dinamo Kiev|59.18 (0.0000)|Atletico Madrid|83.00 (0.0000)|Hoffenheim|81.63 (0.0000)|
|Bayer Leverkusen|82.10 (0.0000)|Basel|85.56 (0.0000)|Young Boys|88.17 (0.0000)|
|CSKA Moskov|90.91 (0.0000)|Porto|88.41 (0.0000)|AEK Athens|93.05 (0.0000)|
|Benfica|100.59 (0.0000)|Qarabag|91.22 (0.0000)|CSKA Moskov|99.54 (0.0000)|
|Leicester|105.51 (0.0000)|CSKA Moskov|91.60 (0.0000)|Viktoria Plzen|106.74 (0.0000)|
|Napoli|107.73 (0.0000)|Celtic|102.58 (0.0000)|Brugge|110.05 (0.0000)|
|Basel|151.29 (0.0000)|Monaco|116.41 (0.0000)|Benfica|124.34 (0.0000)|
|Celtic|184.54 (0.0000)|Maribor|146.27 (0.0000)|Red Star Belgrade|128.87 (0.0000)|
|Rostov|186.58 (0.0000)|Sporting Lisbon|179.63 (0.0000)|Schalke 04|133.93 (0.0000)|
|Copenaghen|202.83 (0.0000)|APOEL|258.55 (0.0000)|Lokomotiv Moskov|150.41 (0.0000)|
|Dynamo Zagreb|263.87 (0.0000)|Spartak Moskov|271.92 (0.0000)|PSV|230.21 (0.0000)|



_p_ -Values are denoted in brackets. 

> **146 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

**Table 12:** Results of one-sample DM test under _H_ 0: _T_ 4. 

|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|---|---|---|---|---|---|
|Leicester|26.28 (0.0352)|APOEL|17.35 (0.2985)|Schalke 04|18.32 (0.2463)|
|Dynamo Zagreb|31.01 (0.0088)|Anderlecht|19.97 (0.1731)|Inter|31.55 (0.0074)|
|Monaco|31.49 (0.0076)|Olympiacos|22.32 (0.0998)|AEK Athens|46.75 (0.0000)|
|Celtic|43.84 (0.0001)|Celtic|27.66 (0.0238)|Red Star Belgrade|47.71 (0.0000)|
|Rostov|52.03 (0.0000)|Maribor|30.90 (0.0090)|Monaco|54.74 (0.0000)|
|Atletico Madrid|53.27 (0.0000)|Monaco|38.29 (0.0008)|Hoffenheim|62.18 (0.0000)|
|Dinamo Kiev|57.89 (0.0000)|CSKA Moskov|39.39 (0.0006)|Brugge|62.55 (0.0000)|
|PSV|58.54 (0.0000)|Feyenord|53.03 (0.0000)|PSV|65.40 (0.0000)|
|Legia Warsav|63.56 (0.0000)|Porto|56.74 (0.0000)|CSKA Moskov|76.38 (0.0000)|
|Benfica|70.84 (0.0000)|Sporting Lisbon|68.47 (0.0000)|Valencia|80.34 (0.0000)|
|Borussia Gladbach|75.36 (0.0000)|<br>Besiktas|71.98 (0.0000)|Viktoria Plzen|86.01 (0.0000)|
|CSKA Moskov|93.72 (0.0000)|Qarabag|76.53 (0.0000)|Galatasaray|89.42 (0.0000)|
|Sevilla|95.16 (0.0000)|Leipzig|81.97 (0.0000)|Porto|91.48 (0.0000)|
|Brugge|96.13 (0.0000)|Basel|86.47 (0.0000)|PSG|98.24 (0.0000)|
|Lyon|101.87 (0.0000)|Benfica|93.99 (0.0000)|Lyon|109.25 (0.0000)|
|Manchester City|111.22 (0.0000)|Liverpool|98.82 (0.0000)|Atletico Madrid|120.76 (0.0000)|
|Arsenal|114.47 (0.0000)|Roma|140.50 (0.0000)|Napoli|126.37 (0.0000)|
|Tottenham|120.53 (0.0000)|Manchester City|146.49 (0.0000)|Shakhtar Donetsk|126.71 (0.0000)|
|Barcelona|122.53 (0.0000)|Napoli|157.84 (0.0000)|Young Boys|133.78 (0.0000)|
|Sporting Lisbon|132.04 (0.0000)|Sevilla|163.36 (0.0000)|Tottenham|142.23 (0.0000)|
|Napoli|135.86 (0.0000)|PSG|164.03 (0.0000)|Liverpool|145.27 (0.0000)|
|Bayer Leverkusen|136.11 (0.0000)|Chelsea|171.72 (0.0000)|Juventus|148.86 (0.0000)|
|Ludogorets|163.35 (0.0000)|Tottenham|171.81 (0.0000)|Benfica|151.94 (0.0000)|
|Basel|170.56 (0.0000)|Atletico Madrid|173.45 (0.0000)|Barcelona|177.27 (0.0000)|
|Copenaghen|171.08 (0.0000)|Juventus|175.01 (0.0000)|Lokomotiv Moskov|198.41 (0.0000)|
|Juventus|176.31 (0.0000)|Spartak Moskov|176.03 (0.0000)|Bayern Munchen|201.63 (0.0000)|
|Porto|178.25 (0.0000)|Borussia Dortmund|179.32 (0.0000)|Manchester City|205.81 (0.0000)|
|PSG|247.50 (0.0000)|Manchester United|245.07 (0.0000)|Roma|215.06 (0.0000)|
|Besiktas|251.22 (0.0000)|Barcelona|289.00 (0.0000)|Ajax|224.92 (0.0000)|
|Real Madrid|349.35 (0.0000)|Shakhtar Donetsk|355.26 (0.0000)|Real Madrid|230.40 (0.0000)|
|Bayern Munchen|389.47 (0.0000)|Real Madrid|428.29 (0.0000)|Manchester United|250.30 (0.0000)|
|Borussia Dortmund|406.26 (0.0000)|Bayern Munchen|666.18 (0.0000)|Borussia Dortmund|259.83 (0.0000)|



_p_ -Values are denoted in brackets. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 147** 

**Table 13:** One-sample test statistics of teams in each season, whose null hypothesis is “structural similarity” Tier A versus reference teams. 

|**Reference:****_Re_**|**_al Madrid_**|**Reference:****_Re_**|**_al Madrid_**|**Reference:****_R_**|**_eal Madrid_**|
|---|---|---|---|---|---|
|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|PSG|11.76 (0.6974)|Manchester City|16.24 (0.3663)|Barcelona|6.94 (0.9594)|
|Manchester City|12.84 (0.6147)|Juventus|17.66 (0.2809)|Napoli|7.05 (0.9562)|
|Tottenham|17.72 (0.2778)|Barcelona|18.59 (0.2331)|Borussia Dortmund|8.13 (0.9185)|
|Bayern Munchen|18.94 (0.2165)|PSG|52.70 (0.0000)|Manchester City|9.32 (0.8603)|
|Arsenal|20.73 (0.1457)|Sevilla|52.97 (0.0000)|Juventus|16.29 (0.3628)|
|Juventus|27.60 (0.0242)|Roma|59.67 (0.0000)|Bayern Munchen|26.83 (0.0301)|
|Borussia Dortmund|32.37 (0.0057)|Liverpool|62.89 (0.0000)|Liverpool|28.22 (0.0202)|
|Sevilla|38.32 (0.0000)|Bayern Munchen|65.16 (0.0000)|Shakhtar Donetsk|34.10 (0.0033)|
|Lyon|51.50 (0.0000)|Borussia Dortmund|85.44 (0.0000)|Tottenham|42.01 (0.0000)|
|Borussia Gladbach|58.03 (0.0000)|Benfica|98.06 (0.0000)|Porto|43.89 (0.0001)|
|Barcelona|76.13 (0.0000)|Feyenord|161.81 (0.0000)|Inter|59.44 (0.0000)|
|Monaco|88.22 (0.0000)|Leipzig|163.98 (0.0000)|Roma|62.00 (0.0000)|
|PSV|97.54 (0.0000)|Napoli|164.59 (0.0000)|PSG|67.36 (0.0000)|
|Atletico Madrid|103.76 (0.0000)|Shakhtar Donetsk|170.90 (0.0000)|Atletico Madrid|68.07 (0.0000)|
|Brugge|103.79 (0.0000)|Anderlecht|201.17 (0.0000)|Lyon|101.22 (0.0000)|
|Ludogorets|108.18 (0.0000)|Chelsea|204.27 (0.0000)|Valencia|121.67 (0.0000)|
|Besiktas|122.51 (0.0000)|Manchester United|205.85 (0.0000)|Ajax|127.00 (0.0000)|
|Dinamo Kiev|127.17 (0.0000)|Besiktas|206.67 (0.0000)|Monaco|131.60 (0.0000)|
|Porto|127.81 (0.0000)|Tottenham|207.34 (0.0000)|Benfica|151.22 (0.0000)|
|Legia Warsav|132.25 (0.0000)|Atletico Madrid|214.07 (0.0000)|Galatasaray|159.68 (0.0000)|
|Sporting Lisbon|151.47 (0.0000)|Olympiacos|220.13 (0.0000)|Manchester United|164.68 (0.0000)|
|Benfica|213.55 (0.0000)|Basel|239.46 (0.0000)|CSKA Moskov|176.33 (0.0000)|
|Bayer Leverkusen|227.12 (0.0000)|Celtic|265.64 (0.0000)|Brugge|183.50 (0.0000)|
|CSKA Moskov|229.24 (0.0000)|Porto|286.50 (0.0000)|Viktoria Plzen|195.40 (0.0000)|
|Napoli|270.75 (0.0000)|Monaco|313.33 (0.0000)|AEK Athens|195.65 (0.0000)|
|Leicester|276.03 (0.0000)|Qarabag|315.74 (0.0000)|Hoffenheim|201.17 (0.0000)|
|Basel|400.26 (0.0000)|CSKA Moskov|333.67 (0.0000)|Young Boys|217.99 (0.0000)|
|Copenaghen|534.15 (0.0000)|Maribor|407.93 (0.0000)|Schalke 04|289.88 (0.0000)|
|Celtic|537.47 (0.0000)|Sporting Lisbon|590.96 (0.0000)|Lokomotiv Moskov|303.20 (0.0000)|
|Rostov|645.08 (0.0000)|APOEL|836.93 (0.0000)|Red Star Belgrade|354.21 (0.0000)|
|Dynamo Zagreb|794.94 (0.0000)|Spartak Moskov|843.63 (0.0000)|PSV|511.75 (0.0000)|



_p_ -Values are denoted in brackets. 

> **148 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

**Table 14:** One-sample test statistics of teams in each season, whose null hypothesis is “structural similarity” of Tier B versus reference teams. 

|**Reference:****_Spor_**|**_ting Lisbon_**|**Reference:****_Spor_**|**_ting Lisbon_**|**Reference:**|**_Benfica_**|
|---|---|---|---|---|---|
|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|Lyon|8.32 (0.9105)|Monaco|3.82 (0.9983)|Inter|8.14 (0.9180)|
|Borussia Gladbach|15.03 (0.4494)|Olympiacos|4.03 (0.9976)|Atletico Madrid|14.83 (0.4637)|
|Tottenham|15.90 (0.3890)|Celtic|4.40 (0.9961)|PSG|15.47 (0.4181)|
|Manchester City|17.84 (0.2714)|CSKA Moskov|5.98 (0.9800)|Porto|17.54 (0.2876)|
|Sevilla|17.88 (0.2692)|Porto|6.72 (0.9649)|Lyon|17.55 (0.2870)|
|Arsenal|21.74 (0.1148)|Anderlecht|6.91 (0.9601)|Liverpool|20.82 (0.1428)|
|Atletico Madrid|24.99 (0.0500)|Feyenord|9.22 (0.8658)|Shakhtar Donetsk|21.63 (0.1180)|
|Ludogorets|25.79 (0.0403)|Maribor|11.04 (0.7498)|Napoli|22.72 (0.0903)|
|Barcelona|33.40 (0.0041)|Leipzig|13.36 (0.5747)|Monaco|24.48 (0.0574)|
|Monaco|33.92 (0.0035)|Qarabag|16.76 (0.3334)|Roma|25.67 (0.0416)|
|Juventus|37.13 (0.0012)|Basel|17.33 (0.2995)|Brugge|26.24 (0.0356)|
|Dinamo Kiev|39.86 (0.0005)|Benfica|21.71 (0.1155)|Tottenham|26.79 (0.0305)|
|PSG|41.89 (0.0002)|Liverpool|25.91 (0.0390)|Viktoria Plzen|29.64 (0.0133)|
|PSV|43.26 (0.0001)|Besiktas|28.54 (0.0184)|Ajax|30.82 (0.0093)|
|Besiktas|45.84 (0.0001)|Napoli|33.56 (0.0039)|Valencia|30.86 (0.0092)|
|Benfica|46.71 (0.0000)|Chelsea|35.76 (0.0019)|Juventus|33.04 (0.0046)|
|Legia Warsav|52.61 (0.0000)|Atletico Madrid|40.96 (0.0003)|Hoffenheim|33.41 (0.0041)|
|Porto|55.79 (0.0000)|Borussia Dortmund|42.65 (0.0002)|Bayern Munchen|37.07 (0.0012)|
|Borussia Dortmund|57.86 (0.0000)|Roma|45.00 (0.0001)|Manchester United|41.28 (0.0003)|
|Bayer Leverkusen|60.17 (0.0000)|PSG|46.18 (0.0000)|Galatasaray|42.06 (0.0002)|
|Bayern Munchen|62.45 (0.0000)|Sevilla|48.68 (0.0000)|Schalke 04|44.02 (0.0001)|
|Real Madrid|65.15 (0.0000)|APOEL|51.15 (0.0000)|Manchester City|45.34 (0.0001)|
|Napoli|69.69 (0.0000)|Spartak Moskov|52.46 (0.0000)|Barcelona|45.43 (0.0001)|
|CSKA Moskov|85.48 (0.0000)|Manchester City|54.52 (0.0000)|Real Madrid|47.13 (0.0000)|
|Brugge|99.05 (0.0000)|Manchester United|59.39 (0.0000)|AEK Athens|47.30 (0.0000)|
|Celtic|154.96 (0.0000)|Tottenham|61.62 (0.0000)|CSKA Moskov|50.95 (0.0000)|
|Rostov|165.26 (0.0000)|Juventus|61.78 (0.0000)|Young Boys|58.85 (0.0000)|
|Leicester|176.68 (0.0000)|Shakhtar Donetsk|102.31 (0.0000)|Borussia Dortmund|62.78 (0.0000)|
|Basel|234.35 (0.0000)|Barcelona|107.65 (0.0000)|Red Star Belgrade|69.09 (0.0000)|
|Copenaghen|268.88 (0.0000)|Real Madrid|175.79 (0.0000)|PSV|119.95 (0.0000)|
|Dynamo Zagreb|563.09 (0.0000)|Bayern Munchen|227.70 (0.0000)|Lokomotiv Moskov|125.42 (0.0000)|



_p_ -Values are denoted in brackets. 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 149** 

**Table 15:** One-sample test statistics of teams in each season, whose null hypothesis is “structural similarity” of Tier C versus reference teams. 

|**Reference:****_Dyna_**|**_mo Zagreb_**|**Reference:****_An_**|**_derlecht_**|**Reference:**|**_Monaco_**|
|---|---|---|---|---|---|
|**2016–2017**|**_X_obs**|**2017–2018**|**_X_obs**|**2018–2019**|**_X_obs**|
|Rostov|15.99 (0.3828)|Olympiacos|6.84 (0.9620)|Inter|6.84 (0.9618)|
|Leicester|16.30 (0.3621)|Monaco|15.08 (0.4460)|Viktoria Plzen|9.55 (0.8469)|
|Celtic|36.03 (0.0017)|CSKA Moskov|17.45 (0.2928)|Brugge|13.38 (0.5730)|
|Legia Warsav|38.70 (0.0007)|Celtic|17.89 (0.2686)|Benfica|15.33 (0.4282)|
|Monaco|42.34 (0.0002)|Porto|18.85 (0.2208)|Lyon|15.92 (0.3875)|
|Atletico Madrid|46.61 (0.0000)|Feyenord|21.02 (0.1361)|PSG|16.43 (0.3539)|
|CSKA Moskov|57.08 (0.0000)|Liverpool|21.37 (0.1255)|Hoffenheim|16.69 (0.3376)|
|Dinamo Kiev|61.37 (0.0000)|Leipzig|23.47 (0.0747)|Atletico Madrid|17.09 (0.3133)|
|PSV|63.31 (0.0000)|Maribor|24.05 (0.0643)|Porto|18.14 (0.2553)|
|Brugge|66.44 (0.0000)|Benfica|24.78 (0.0530)|Schalke 04|21.83 (0.1125)|
|Borussia Gladbach|69.95 (0.0000)|Qarabag|29.38 (0.0144)|Valencia|22.94 (0.0853)|
|Copenaghen|73.85 (0.0000)|Basel|34.24 (0.0032)|CSKA Moskov|23.76 (0.0693)|
|Bayer Leverkusen|82.11 (0.0000)|Sporting Lisbon|34.44 (0.0030)|Liverpool|24.90 (0.0513)|
|Sevilla|87.83 (0.0000)|Atletico Madrid|37.11 (0.0012)|Shakhtar Donetsk|25.57 (0.0428)|
|Benfica|96.79 (0.0000)|Chelsea|38.71 (0.0007)|AEK Athens|28.56 (0.0183)|
|Lyon|100.31 (0.0000)|Sevilla|41.04 (0.0003)|Tottenham|28.69 (0.0176)|
|Arsenal|102.89 (0.0000)|Roma|42.79 (0.0002)|Napoli|29.39 (0.0143)|
|Tottenham|110.55 (0.0000)|PSG|43.07 (0.0002)|Galatasaray|30.48 (0.0103)|
|Manchester City|112.70 (0.0000)|APOEL|43.11 (0.0002)|Ajax|31.90 (0.0066)|
|Barcelona|113.59 (0.0000)|Napoli|44.41 (0.0001)|Roma|34.77 (0.0027)|
|Sporting Lisbon|135.15 (0.0000)|Besiktas|45.52 (0.0001)|Juventus|38.30 (0.0008)|
|Porto|136.46 (0.0000)|Manchester City|46.83 (0.0000)|Red Star Belgrade|38.44 (0.0008)|
|Ludogorets|140.47 (0.0000)|Borussia Dortmund|51.75 (0.0000)|Young Boys|39.86 (0.0005)|
|Basel|145.57 (0.0000)|Juventus|56.60 (0.0000)|Manchester United|42.33 (0.0002)|
|Juventus|153.92 (0.0000)|Tottenham|71.39 (0.0000)|Bayern Munchen|44.89 (0.0001)|
|Napoli|155.98 (0.0000)|Spartak Moskov|76.23 (0.0000)|Barcelona|53.06 (0.0000)|
|Besiktas|208.52 (0.0000)|Manchester United|79.70 (0.0000)|Manchester City|55.06 (0.0000)|
|PSG|224.55 (0.0000)|Barcelona|94.60 (0.0000)|Real Madrid|60.23 (0.0000)|
|Real Madrid|339.19 (0.0000)|Shakhtar Donetsk|114.47 (0.0000)|Borussia Dortmund|74.86 (0.0000)|
|Borussia Dortmund|372.93 (0.0000)|Real Madrid|137.29 (0.0000)|PSV|93.66 (0.0000)|
|Bayern Munchen|375.26 (0.0000)|Bayern Munchen|208.59 (0.0000)|Lokomotiv Moskov|99.75 (0.0000)|



_p_ -Values are denoted in brackets. 

> **150 —** L. Palazzo et al.: Testing styles of play using triad census distribution 

## **References** 

- Albert, J., Y. Bennett, and J. J. Cochran. 2005. _Anthology of Statistics in Sports_ . United States: SIAM. 

- Bate, R. 1988. “Football Chance: Tactics and Strategy.” In _Science and Football: Proceedings of the First World Congress of Science and Football_ , edited by T. Reilly, A. Lees, and K. Davids. United States: Routledge. 

- Baumer, B. S., S. T. Jensen, and G. J. Matthews. 2015. “Openwar: An Open Source System for Evaluating Overall Player Performance in Major League Baseball.” _Journal of Quantitative Analysis in Sports_ 11 (2): 69−84 **.** 

- Block, P. 2015. “Reciprocity, Transitivity, and the Mysterious Three-Cycle.” _Social Networks_ 40: 163−73 **.** 

- Boyle, R., and R. Haynes. 2004. _Football in the New Media Age_ . Routledge. 

- Bransen, L., J. Van Haaren, and M. van de Velden. 2019. “Measuring Soccer Players’ Contributions to Chance Creation by Valuing Their Passes.” _Journal of Quantitative Analysis in Sports_ 15 (2): 97−116 **.** 

- Brier, S. S. 1980. “Analysis of Contingency Tables under Cluster Sampling.” _Biometrika_ 67 (3): 591−6 **.** 

- Buchheit, M., A. Allen, T. K. Poon, M. Modonutti, W. Gregson, and V. Di Salvo. 2014. “Integrating Different Tracking Systems in 

   - Football: Multiple Camera Semi-Automatic System, Local Position Measurement and Gps Technologies.” _Journal of Sports Sciences_ 32 (20): 1844−57 **.** 

- Buchheit, M., and B. M. Simpson. 2017. “Player-Tracking Technology: Half-Full or Half-Empty Glass?” _International Journal of Sports Physiology and Performance_ 12 (s2): S2−35 **.** 

- Caicedo-Parada, S., C. Lago-Peñas, and E. Ortega-Toro. 2020. “Passing Networks and Tactical Action in Football: A Systematic Review.” _International Journal of Environmental Research and Public Health_ 17 (18): 6649 **.** 

- Carpita, M., E. Ciavolino, and P. Pasca. 2019. “Exploring and Modelling Team Performances of the Kaggle European Soccer Database.” _Statistical Modelling_ 19 (1): 74−101 **.** 

- Cintia, P., S. Rinzivillo, and L. Pappalardo. 2015. “A Network-Based 

   - Approach to Evaluate the Performance of Football Teams.” 

   - In _Machine Learning and Data Mining for Sports Analytics Workshop_ . 

- Clemente, F. M., F. M. L. Martins, and R. S. Mendes. 2016. _Social Network_ 

_Analysis Applied to Team Sports Analysis_ . United States: Springer. 

Clemente, F. M., H. Sarmento, and R. Aquino. 2020. “Player Position 

   - Relationships with Centrality in the Passing Network of World Cup Soccer Teams: Win/Loss Match Comparisons.” _Chaos, Solitons & Fractals_ 133: 109625 **.** 

- Cox, D., and F. R. T. Trevor. 2002. “An Analysis of Decathlon Data.” _Journal of the Royal Statistical Society: Series D (The Statistician)_ 51 (2): 179−87 **.** 

Csardi, G., and T. Nepusz. 2006. _The igraph Software Package for Complex Network Research_ , 1695. United States: InterJournal Complex Systems. 

- Cugmas, M., A. Ferligoj, and A. Žiberna. 2017. “Generating Global Network Structures by Triad Types.” arXiv preprint arXiv:1710.10042. 

- Davis, J. A., and S. Leinhardt. 1967. “The Structure of Positive Interpersonal Relations in Small Groups.” In _Schlüsselwerke der Netzwerkforschung_ . Germany: Springer. 

- Diquigiovanni, J., and B. Scarpa. 2019. “Analysis of Association Football Playing Styles: An Innovative Method to Cluster Networks.” _Statistical Modelling_ 19 (1): 28−54 **.** 

- Edgecomb, S., and K. Norton. 2006. “Comparison of Global Positioning and Computer-Based Tracking Systems for Measuring Player Movement Distance During Australian Football.” _Journal of Science and Medicine in Sport_ 9 (1−2): 25−32 **.** 

- Ennis, D. M., and J. Bi. 1999. “The Dirichlet-Multinomial Model: 

   - Accounting for Inter-Trial Variation in Replicated Ratings.” _Journal of Sensory Studies_ 14 (3): 321−45 **.** 

- Faust, K. 2006. “Comparing Social Networks: Size, Density, and Local Structure.” _Metodoloski zvezki_ 3 (2): 185 **.** 

- Faust, K. 2007. “7. Very Local Structure in Social Networks.” _Sociological Methodology_ 37 (1): 209−56 **.** 

- Faust, K. 2008. “Triadic Configurations in Limited Choice Sociometric Networks: Empirical and Theoretical Results.” _Social Networks_ 30 (4): 273−82 **.** 

- Faust, K. 2010. “A Puzzle Concerning Triads in Social Networks: Graph Constraints and the Triad Census.” _Social Networks_ 32 (3): 221−33 **.** 

- Fewell, J. H., D. Armbruster, J. Ingraham, A. Petersen, and J. S. Waters. 2012. “Basketball Teams as Strategic Networks.” _PLoS One_ 7 (11): e47445 **.** 

- Gallagher, S. K., K. Frisoli, and A. Luby. 2021. “Opening up the Court: Analyzing Player Performance across Tennis Grand Slams.” _Journal of Quantitative Analysis in Sports_ 17 (4): 255−71 **.** 

- Gomez, R. 2002. “Salary Compression and Team Performance: Evidence from the National Hockey League.” In _Sportökonomie_ , 203−20. Germany: Springer. 

- Gonçalves, B., D. Coutinho, S. Santos, C. Lago-Penas, S. Jiménez, and J. Sampaio. 2017. “Exploring Team Passing Networks and Player Movement Dynamics in Youth Association Football.” _PLoS One_ 12 (1): e0171156 **.** 

- Greenacre, M. J. 1984. _Correspondence Analysis_ . London: Academic Press. 

- Groll, A., C. Ley, G. Schauberger, and H. Van Eetvelde. 2019. “A Hybrid Random Forest to Predict Soccer Matches in International Tournaments.” _Journal of Quantitative Analysis in Sports_ 15 (4): 271−87 **.** 

- Groll, A., G. Schauberger, and G. Tutz. 2015. “Prediction of Major International Soccer Tournaments Based on Team-specific Regularized Poisson Regression: An Application to the Fifa World Cup 2014.” _Journal of Quantitative Analysis in Sports_ 11 (2): 97−115 **.** 

- Grund, T. U. 2012. “Network Structure and Team Performance: The Case of English Premier League Soccer Teams.” _Social Networks_ 34 (4): 682−90 **.** 

- Hadley, L., M. Poitras, J. Ruggiero, and S. Knowles. 2000. “Performance Evaluation of National Football League Teams.” _Managerial and Decision Economics_ 21 (2): 63−70 **.** 

- Holland, P. W., and S. Leinhardt. 1976. “Local Structure in Social Networks.” _Sociological Methodology_ 7: 1−45 **.** 

- Holland, P. W., and S. Leinhardt. 1978. “An Omnibus Test for Social Structure Using Triads.” _Sociological Methods & Research_ 7 (2): 227−56 **.** 

- Hyballa, P., and H.-D. Te Poel. 2015. _German Soccer Passing Drills: More than 100 Drills from the Pros_ . Germany: Meyer & Meyer Verlag. 

- Ibáñez, S. J., J. Sampaio, S. Feu, A. Lorenzo, M. A. Gómez, and E. Ortega. 2008. “Basketball Game-Related Statistics that Discriminate Between Teams’ Season-Long Success.” _European Journal of Sport Science_ 8 (6): 369−72 **.** 

- Ievoli, R., A. Gardini, and L. Palazzo. 2021a. “The Role of Passing Network Indicators in Modeling Football Outcomes: An Application Using Bayesian Hierarchical Models.” _AStA Advances in Statistical Analysis_ , 107: 1−23 **.** 

> L. Palazzo et al.: Testing styles of play using triad census distribution **— 151** 

- Ievoli, R., L. Palazzo, and G. Ragozini. 2021b. “On the Use of Passing Network Indicators to Predict Football Outcomes.” _Knowledge-Based Systems_ 222: 106997 **.** 

- Ishii, G., and R. Hayakawa. 1960. “On the Compound Binomial Distribution.” _Annals of the Institute of Statistical Mathematics_ 12 (1): 69−80 **.** 

- Johnson, N. L., S. Kotz, and N. Balakrishnan. 1997. _Discrete Multivariate Distributions_ , Vol. 165. New York: Wiley. 

- Kahn, L. M. 1993. “Managerial Quality, Team Success, and Individual Player Performance in Major League Baseball.” _ILR Review_ 46 (3): 531−47 **.** 

- Kaiser, H. F. 1960. “The Application of Electronic Computers to Factor Analysis.” _Educational and Psychological Measurement_ 20 (1): 141−51 **.** 

- Keller, J. B. 1994. “A Characterization of the Poisson Distribution and the Probability of Winning a Game.” _The American Statistician_ 48 (4): 294−8 **.** 

- Kimber, A. C., and A. R. Hansford. 1993. “A Statistical Analysis of Batting in Cricket.” _Journal of the Royal Statistical Society: Series A_ 156 (3): 443−55 **.** 

- 

- Koehler, K. J., and J. R. Wilson. 1986. “Chi Square Tests for Comparing Vectors of Proportions for Several Cluster Samples.” 

   - _Communications in Statistics - Theory and Methods_ 15 (10): 2977−90 **.** 

- Krackhardt, D. 1999. “The Ties that Torture: Simmelian Tie Analysis in Organizations.” _Research in the Sociology of Organizations_ 16 (1): 183−210. 

- La Rosa, P. S., J. P. Brooks, E. Deych, E. L. Boone, D. J. Edwards, Q. Wang, E. Sodergren, G. Weinstock, and W. D. Shannon. 2012. “Hypothesis Testing and Power Calculations for Taxonomic-Based Human Microbiome Data.” _PLoS One_ 7 (12): e52078 **.** 

- La Rosa, P. S., E. Deych, S. Carter, B. Shands, D. Yang, and W. D. Shannon. 2019. _HMP: Hypothesis Testing And Power Calculations for Comparing Metagenomic Samples from HMP_ . R package version 2.0.1. 

- Lago-Peñas, C., and A. Dellal. 2010. “Ball Possession Strategies in Elite Soccer According to the Evolution of the Match-Score: The Influence of Situational Variables.” _Journal of Human Kinetics_ 25: 93−100 **.** 

- Lewis, A. 2005. “Towards Fairer Measures of Player Performance in One-Day Cricket.” _Journal of the Operational Research Society_ 56 (7): 804−15 **.** 

- Lorrain, F., and H. C. White. 1971. “Structural Equivalence of Individuals in Social Networks.” _Journal of Mathematical Sociology_ 1 (1): 49−80 **.** 

- Luczkovich, J. J., S. P. Borgatti, J. C. Johnson, and M. G. Everett. 2003. “Defining and Measuring Trophic Role Similarity in Food Webs Using Regular Equivalence.” _Journal of Theoretical Biology_ 220 (3): 303−21 **.** 

- McIntyre, S., and R. McKitrick. 2005. “Hockey Sticks, Principal Components, and Spurious Significance.” _Geophysical Research Letters_ 32 (3): 1−6,. 

- Mclean, S., P. M. Salmon, A. D. Gorman, N. J. Stevens, and C. Solomon. 2018. “A Social Network Analysis of the Goal Scoring Passing Networks of the 2016 European Football Championships.” _Human Movement Science_ 57: 400−8 **.** 

- Mosimann, J. E. 1962. “On the Compound Multinomial Distribution, the Multivariate _𝛽_ -Distribution, and Correlations Among Proportions.” _Biometrika_ 49 (1/2): 65−82 **.** 

- Minka, T. 2000. _Estimating a Dirichlet Distribution_ . https://tminka.github .io/papers/dirichlet/. 

- Moura, F. A., L. E. B. Martins, and S. A. Cunha. 2014. “Analysis of Football Game-Related Statistics Using Multivariate Techniques.” _Journal of Sports Sciences_ 32 (20): 1881−7 **.** 

- Onnela, J.-P., J. Saramäki, J. Kertész, and K. Kaski. 2005. “Intensity and Coherence of Motifs in Weighted Complex Networks.” _Physical Review E_ 71 (6): 065103 **.** 

- Pina, T. J., A. Paulo, and D. Araújo. 2017. “Network Characteristics of Successful Performance in Association Football. A Study on the Uefa Champions League.” _Frontiers in Psychology_ 8: 1173 **.** 

- Rein, R., D. Raabe, and D. Memmert. 2017. “‘Which Pass Is Better?’ Novel Approaches to Assess Passing Effectiveness in Elite Soccer.” _Human Movement Science_ 55: 172−81 **.** 

- Ricard, I., and A. Davison. 2007. “Statistical Inference for Olfactometer Data.” _Journal of the Royal Statistical Society: Series C (Applied Statistics)_ 56 (4): 479−92 **.** 

- Sampaio, J., M. Janeira, S. Ibáñez, and A. Lorenzo. 2006. “Discriminant Analysis of Game-Related Statistics between Basketball Guards, Forwards and Centres in Three Professional Leagues.” _European Journal of Sport Science_ 6 (3): 173−8 **.** 

- Stern, H. 1991. “On the Probability of Winning a Football Game.” _The American Statistician_ 45 (3): 179−83 **.** 

- Tibshirani, R. J., A. Price, and J. Taylor. 2011. “A Statistician Plays Darts.” _Journal of the Royal Statistical Society: Series A_ 174 (1): 213−26 **.** 

- Tvedebrink, T. 2010. “Overdispersion in Allelic Counts and _𝜃_ -Correction in Forensic Genetics.” _Theoretical Population Biology_ 78 (3): 200−10 **.** 

- Wasserman, S., and K. Faust. 1994. _Social Network Analysis: Methods and Applications_ , 8. United Kingdom: Cambridge University Press. 

- Wu, S. H., R. S. Schwartz, D. J. Winter, D. F. Conrad, and R. A. Cartwright. 2017. “Estimating Error Models for Whole Genome Sequencing Using Mixtures of Dirichlet-Multinomial Distributions.” _Bioinformatics_ 33 (15): 2322−9 **.** 

- Yurko, R., S. Ventura, and M. Horowitz. 2019. “Nflwar: A Reproducible Method for Offensive Player Evaluation in Football.” _Journal of Quantitative Analysis in Sports_ 15 (3): 163−83 **.** 


