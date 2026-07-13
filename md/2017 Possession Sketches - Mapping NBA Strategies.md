<!-- source: 2017 Possession Sketches - Mapping NBA Strategies.pdf -->



# **Possession Sketches: Mapping NBA Strategies** 

Paper Track 1624 

#### **Abstract** 

We present _Possession Sketches_ , a new machine learning method for organizing and exploring a database of basketball player-tracks. Our method organizes basketball possessions by offensive structure. We �irst develop a model for populating a dictionary of short, repeated, and spatially registered ”actions”. Each action corresponds to an interpretable type of player movement. We examine statistical patterns in these actions, and show how they can be used to describe individual player behavior. Leveraging this “vocabulary” of actions, we develop a hierarchical model to characterize interactions between players. Our approach draws on the topic-modeling literature, extending Latent Dirichlet Allocation (LDA) through a novel representation of player movement data which uses techniques common inanimation and videogamedesign. Weshowthatthis modelis abletogrouptogetherpossessions with similar offensive structure, allowing ef�icient search and exploration of the entire database of playertracking data. We show that our model �inds repeated offensive structure in teams (e.g. strategy), providing a much more sophisticated, yet interpretable lens into basketball player-tracking data. 

## **1 Introduction** 

Player-tracking data present a unique challenge for basketball analytics. Some believe that there is a windfall of quantitative insight available in these data, hidden in spatiotemporal patterns that coaches and analysts typically process with human intuition. While there has been work toward quantifying player ability [6], possession value [4, 3], and play classi�ication based on small set of labeled plays [13], methods for _automatically_ organizing, summarizing, and interpreting basketball possessions have not delivered. 

As an example, consider the following use case for defensive scouting: an analyst is tasked with �inding all possessions in which James Harden drives to the basket and passes the ball to a teammate for a right corner three-point attempt. Ad hoc engineering solutions for this scenario are easy to imagine: �irst sub-select Rockets possessions with a right corner three-point attempt and then look for passes from Harden that originate in the paint. However, adding search criteria quickly renders this ad hoc solution intractable: �ind sequences where Harden uses a high screen before driving to the basket and then passes to the corner for a three-point attempt; �ind sequences where Harden uses a high screen, drives to the basket, passes to the corner and that teammate drives to the basket; �ind sequences where _any rocket_ uses a high screen, drives to the basket, etc. The landscape of relevant basketball scenarios is far too vast for ad hoc search solutions. 

Furthermore, this type of sequential query is only one approach to gaining insight from playertracking data. We can imagine starting a research project by simply asking — what leads to a corner three? What sort of patterns are employed by different offenses in order to get an open three-point attempt? What sorts of actions do speci�ic players tend to do in order to generate an open three-point attempt? Existing methodology falls short of extracting this information from player-tracking data. 

In this work, we bridge this gap by formulating a novel machine learning method to describe an entire database of player-tracks. Our method uncovers characteristic patterns of offense in a way that is searchable and interpretable. We �irst describe individual player’s actions by building a data-driven 



2017 Research Papers Competition Presented by: 

1 



dictionary of _action templates_ derived from a novel statistical model. We then construct a model of possessions that describes patterns in these _action templates_ — common co-occurrences that create a signature of offensive strategy. For each play, this yields a _possession sketch_ , a concise summary of the offense’s actions in a basketball possession. We show that this model structure at multiple levels — in dynamic actions taken by individual players, as well as collective actions present in each possession. 

Importantly, we construct our model out of interpretable pieces — each _action template_ can be interpreted as a type of on- or off-ball cut. Further, pairs of actions are also interpretable — some clearly correspond to on- and off-ball screens, others correspond drives and passes to various wings. Our use of probabilistic graphical models on an interpretable representation of the data allows for easier-tounderstand model output and inferences than recent deep learning approaches [13]. 

In the following section we describe the components of our method that generate _action templates_ and _possession sketches_ . After describing our method, we explore the structure it reveals by looking at three of the different organizational tools it makes possible: 

- _team possession maps_ : low-dimensional visualization of all of the offensive possessions of a team — exploring this map reveals different set calls used by a team. 

- _shot possession maps_ : low-dimensional visualization of possessions that led to a particular type of shot — we examine the different types of actions that lead to corner threes. 

- _possession basis_ : common and repeated actions discovered by the model — this establishes the types of player interaction that make up the “vocabulary” of a basketball possession. 

By integrating machine learning methods, statistics, and visualization, this work shows that we can organize and systematically explore NBA possessions, allowing us to drive useful basketball intelligence from the NBA’s vast and growing store of player-tracking data. 

## **2 Methods** 

This section details the machine learning model we construct to recognize patterns at two resolutions: spatiotemporal patterns in individual player trajectories ( _action templates_ ), and co-occurrence of actions in each possession ( _possession sketches_ ). 

Before we go into further detail, the overall procedure behind our method can be broadly decomposed into the following steps 

- _Segmentation_ : We cut possession-length (e.g. 5-24 second) player trajectories into shorter, more manageable segments (e.g. .6-8 second) based on moments of sustained low-velocity. 

- _Learning action templates_ : We formulate a novel statistical clustering algorithm to learn which action is represented by each short segment. 

- _Possession modeling_ : We represent each possession as a “bag” of pair-actions, and �it a possessionlevel hierarchical model inspired by the document modeling and natural language processing literature. 

The following subsections describe the process of applying the above steps to a large data set of basketball player-tracks. 

### **2.1 Data and preprocessing** 

We analyze a database of player-tracks from the 2014-2015 season of the NBA. The data are organized into over _N_ = 190 _,_ 000 possessions (and possessions into quarters and games). For each possession (indexed by _n_ ), we model the trajectories of players on offense. For each player (indexed by _j_ ) in possession _n_ , we cut their trajectory (denoted **_x_**<sup>(</sup> _j_<sup>_n_)</sup> ) into short segments at locations of sustained low-velocity. To do this, we �irst detect moments of low velocity by inspecting the smoothed �irst difference of the 



2017 Research Papers Competition Presented by: 

2 





<!-- Start of picture text -->
Harrison Barnes Stephen Curry<br>start Harrison Barnes start Stephen Curry<br>0 1 3 2 1.41.2 cut pts 0.80.7 cut pts<br>1.0 0.6<br>0.8 0.5<br>4 0.6 0.4<br>0.4 0 0.30.2<br>7 0.2 0.1<br>65 0.0 0.0<br>0 2 4 6 8 10 12 14 16 0 1 2 3 4 5<br>time time<br>(a) (b)<br>Manu Ginobili Danny Green<br>1<br>start Manu Ginobili start Danny Green<br>0.70.6 cut pts 0 0.80.7 cut pts<br>0 0.5 0.6<br>1 0.4 0.50.4<br>0.3<br>0.3<br>0.2 0.2<br>0.1 0.1<br>0.0 0.0<br>0 1 2 3 4 5 6 0 1 2 3 4<br>time time<br>(c) (d)<br>velocity velocity<br>velocity velocity<br><!-- End of picture text -->

**Figure 1:** Examples of trajectory segments resulting from the “sustained-low-velocity-moment” �inding algorithm. In each example, the left plot depicts the spatial trajectory with cut points denoted by the red dots (with the order of the cuts labeled). The right plot depicts the approximate magnitude of the velocity at each moment during the possession, with the corresponding cut points. 

trajectory. At sustained moments of low velocity ( _> ._ 25 seconds below a threshold of _._ 1 feet per second), we cut the possession, resulting in a collection of shorter segments. Figure 1 depicts four example trajectories, cut into various number of segments. 

We refer to these shorter segments as **_x_**<sup>(</sup> _j_<sup>_n_</sup> 1<sup>)</sup><sup>_, . . . ,_</sup><sup>**_x_**(</sup> _j_<sup>_n_</sup> _S_<sup>), where it is understood that</sup><sup>_S_varies from pos-</sup> session trajectory to trajectory. The resulting short segments are on average 2.25 seconds (the interior 95 percentiles ranges from 0.6 to 7.96 seconds). Applying this preprocessing step to the full 2014-2015 regular season creates a data set of roughly 4.5 million segment observations. 

### **2.2 Action Templates: Segment Clustering** 

Our method assumes that each short trajectory segment represents some discrete _action_ , and each player performs a series of actions throughout the course of a possession. For instance, a player might (i) make a cut along the baseline and then (ii) camp out in the corner. Alternatively, a player can (i) make a cut along the 3-point line, (ii) stand at the break, and then (iii) cut toward the basket. In order to decompose a player’s trajectory into a set of actions, we must �irst infer a meaningful set of actions that all players share. We use a data-driven approach to infer this set of actions, each action’s structure, and the action label for each trajectory segment. 

To accomplish this, we construct a probabilistic clustering algorithm tailored for functional data (i.e. continuous trajectories). Our model posits that each trajectory segment represents one of _V_ discrete actions, where each action is characterized by a _template_ . Each template can be thought of as a cluster center in a clustering model — each trajectory segment is centered around a cluster with some deviation. We specify each template as a _Bezier curve_ – a tool commonly used to model movement in the computer graphics community – which speci�ies a function _B_ ( _t_ ) that maps time to a two-dimensional point, _B_ : [0 _,_ 1] _�→_ R<sup>2</sup> . This maps out a dynamic curve through space, which describes the movement of each action. See the appendix for technical details. 

Figure 2 depicts a sampling of learned templates resulting from �itting a mixture of _V_ = 250 Bezier curves to the processed trajectory segments. The result of the model �it allows us to succinctly represent 



2017 Research Papers Competition Presented by: 

3 





<!-- Start of picture text -->
start start start start<br>0.40 Duration, action 126 (9194 examples, has ball freq =0.03) 0.30 Duration, action 217 (11708 examples, has ball freq =0.23) 0.45 Duration, action 220 (12543 examples, has ball freq =0.06) 0.45 Duration, action 222 (9657 examples, has ball freq =0.05)<br>0.35 0.25 0.40 0.40<br>0.30 0.35 0.35<br>0.25 0.20 0.30 0.30<br>0.25 0.25<br>0.20 0.15<br>0.20 0.20<br>0.15 0.10 0.15 0.15<br>0.10 0.10 0.10<br>0.05 0.05 0.05 0.05<br>0.00 0 2 4 seconds6 8 10 12 0.00 0 5 seconds10 15 20 0.00 0 2 4 6 seconds 8 10 12 14 0.00 0 2 4 seconds6 8 10 12<br>(a)  Action 126 (b)  Action 217 (c)  Action 220 (d)  Action 222<br><!-- End of picture text -->

**Figure 2:** A sampling of _action templates_ . Our method automatically builds a taxonomy of commonly repeatedmovements sharedamong allplayers(i.e. _actions_ ). Ineachcolumn, thetopplotdepictsthe spatial trajectory for a single action template. The light blue lines are real segment trajectories that fall in that cluster. Below each action plot is a histogram of segment lengths (in seconds) for all segments that fall into that cluster — some actions are shorter or longer (on average) than others. For a more dynamic picture of an action template, please view this animated �igure: `https://youtu.be/-a6_Ot6etmk` 

each trajectory segment as a single discrete integer, _v_ = 1 _, . . . ,_ 250. We view these actions as a kind of _vocabulary_ — each possession combines words in the vocabulary to describe structured interactions that characterize the possession. Following this thread, weturn tostatistical methods originallydevised for modeling documents, and adapt them to basketball sequences. 

### **2.3 Possession Model** 

Offensive possessions are highly structured. When James Harden drives toward the basket, drawing defender attention, his teammates are not distributed randomly on the �loor — it is likely at that least one teammate is in the corner waiting for a pass; it is likely that other teammates vacate the paint, and begin jockeying for a rebounding position. The structure of an offensive possession can be viewed as structure in the actions that each player performs throughout the possession. Which actions tend to simultaneously co-occur? Which actions tend to precede or follow other actions? Our possession model seeks to answer these questions by �irst observing that these actions are a lot like words. Words are interwoven sequentially to express a coherent idea; player actions are interwoven sequentially to implement a coherent strategy. We run with this analogy by adapting _topic models_ [1] to describe sequences of actions in basketball possessions. 

We use Latent Dirichlet Allocation (LDA) [2], a topic model for unsupervised structure discovery in a corpus of text documents. LDA is a latent factor model, similar to factor analysis or principal components analysis. In document modeling, LDA describes each document as a mixture _topics_ , where each topic is a distribution over the entire vocabulary of words. As a concrete example, LDA applied to a corpus of _Science_ articles �inds topics corresponding to _cancer_ (e.g. probable words are “tumor”, ”cell”, ”cancer”, etc.), _neuroscience_ (“synaptic”, “neurons”, “hippocampal”, etc.), among many others (see [8, 1]). 

We use LDA to describe each possession as a mixture of _strategies_ , where each strategy is a distribution over co-occurring actions that are frequently observed in the data. LDA requires that we represent 



2017 Research Papers Competition Presented by: 

4 





**Figure 3:** The “bag of words” construction of each possession. Each “word” represents two actions that occur simultaneously throughout the course of the possession. In the toy example depicted, we have three players, each performing a sequence of actions (corresponding to the four colors). At each moment in time, we enumerate all unique pairs of actions. We represent the entire possession as a bag of these pair-action counts. 

each possession as a vector of “word counts”. To do this, we need to �irst establish a vocabulary.¹ Our �irst approach was to simply count the number of _v_ = 1 _, . . . , V_ actions that occur in each possession. This approach is appealing in its simplicity, and does reveal interesting structure. However, this representation completely ignores temporal structure in the possession. 

In this work, we use a vocabulary of _pair-actions_ , where each “word” in the vocabulary is a unique pair of of the _V_ actions, ( _vi, vj_ ) for _vi, vj ∈{_ 1 _, . . . , V }_ and _vi_ = _vj_ . We then represent each possession as a “bag of simultaneous pair-actions”, mapping the “bag of words” concept from topic models to basketball actions. For each possession, we simply count the number of times each unique pair of actions ( _v_ = 1 _, . . . , V_ ) occurred simultaneously. We string these counts into a single vector, which represent possession _n_ 



Figure 3 illustrates the construction of our pair-action vocabulary that we use to succinctly represent each possession. This representation allows us to easily apply LDA to basketball possessions. To scale this model to the over 190 _,_ 000 possessions in the season, we use a newly developed scalable Bayesian inference technique [9]. See the appendix for technical details. 

This model yields a low-dimensional embedding of every NBA play that allows us to quickly assess similarities between possessions and explore the space of team offensive strategies. We can create interactive graphics (a dynamic version of Figure 5a), where each point in space represents an NBA possession and nearby points indicate “similar” possessions — possessions that share the same pattern of actions. The following section dives deeper into this exploration tool, and what it can afford an analyst. The _topics_ themselves encode strategic co-occurrences of actions, and using these topics we can shed light on the fundamental building blocks of collective action on the basketball court. Inspecting these topics can help us quantify what exactly makes a unique offense unique. 

## **3 Analysis** 

In this section, we explore the output of the possession level model to see which patterns are represented. We focus on the following aspects of model output 

¹In document modeling, the vocabulary is typically the vocabulary of the language itself, with minimal preprocessing. Bigrams and tri-grams are sometimes included as vocabulary words to improve the model. 



2017 Research Papers Competition Presented by: 

5 



















**Figure 4:** The result of �itting a _K_ = 100 topic possession model. A “topic” in our framework corresponds to a distribution over _pairs_ of actions. Above, we show common _pairs_ of actions from 8 of the 100 topics. We observe that topics tend to pick up on combinations of actions that include common actions. For instance, the top two pair-actions in topic 0 includes a cut along the 3-point line while a teammate cuts nearby (perhaps setting an off-ball screen). 

- _basketball topics_ : we see which _pair-actions_ are represented by each of the _K_ = 100 topics. This tells us not only which pair-actions occur frequently, but which pair-actions co-occur in possessions — this will reveal structure 

- _possession sketch_ : each possession can be described as a distribution over topics, and “similarity” can be measured using this topic-loading vector. We explore what “similarity” means for basketball possessions according to our model, and we empirically test this notion of similarity by measuring distances between set plays we know are similar. 

In the following sections we explore the above concepts by visualizing and exploring possessions in ways newly afforded by our framework. 

### **3.1 Basketball Topics** 

Figure 4 graphically depicts a small sampling of “topics” discovered by the possession model. The topics reveal which pair-actions are most common in our data set, and we do see patterns emerge. As a concrete example, if a particular possession “loads” onto topic 3² then that possession is more likely to include the pair-actions depicted in Figure 4d — a cut to the basket while a teammate is standing in either of the two corners. Topic 5 prominently includes possessions with a baseline cut from the right block to the left break. Note that there are _many more_ pair-actions with signi�icant probability than the ones depicted, and there are many more topics than we depict. 

> ²i.e. the possession sketch vector is large along the dimension corresponding to topic 3 



2017 Research Papers Competition Presented by: 

6 





<!-- Start of picture text -->
0.18<br>weave-to-other dists<br>0.16 weave-to-weave dists<br>0.14<br>0.12<br>0.10<br>0.08<br>0.06<br>0.04<br>0.02<br>0.00<br>0 20 40 60 80 100<br>KL-div<br>(b) Weave-to-weave and weave-to-other dis-<br>(a)  Warriors Possessions (t-SNE map) tances<br><!-- End of picture text -->

**Figure 5:** Left: map of 2014-2015 Warriors Possessions, with a small set of known “weave” plays highlighted in red. The weave plays tend to cluster together in this visualization. We verify this by computing the average distance between two weave possessions and between a weave and a random warriors possession of a similar length. This indicates that our topic-model-based representation is picking up on patterns that are able to (mostly) distinguish between semantically different plays. 

**Sparsity** We also notice that each possession topic vector is quite sparse — on average only 8 of the 100 entries are non-zero (on average). This makes intuitive sense — each possession can only include a small number of offensive patterns from the wide array of available tactics. 

### **3.2 Possession Map Exploration** 

Each possession has an associated _possession sketch_ — a per-topic vector that describes how much of each of the _basketball topics_ (a subset illustrated in Figure 4) are featured in that possession. We can use these _possession sketches_ to reason about large sets of basketball possessions. In this section we select the offensive possessions of the 2014-2015 Golden State Warriors (over 6 _,_ 000 possessions). With each possession succinctly described by a (sparse) 100-dimensional topic vector, we use the dimensionality reduction technique t-SNE [10] to visualize these vectors in 2-dimensions. This method �inds a 2-dimensional representation of each 100-dimensional vector such that the distance in 2-d is similar to the distance in 100-d (emphasizing the preservation of local distances).³ Figure 5 visualize all warriors possessions in 2014-2015. 

We test the notion of “similarity” in topic space by examining a group of hand-labeled _set plays_ , a “weave play”. We animate two examples of the weave play in this animated �igure: `https://youtu. be/KRDsTLMm7FY` . We hand-label 40 weave plays in the 2014-2015 season, and visualize them in the t-SNE Warriors map (Figure 5a, in red). We can visually verify in Figure 5 that the possession sketch preserves this notion of similarity — weave plays tend to cluster around other weave plays. 

We can further measure this clustering by comparing two distributions of possession sketch distances: (i) the distribution of distances between two weave plays, and (ii) the distribution of distances between one weave, and one non-weave play. Figure 5b illustrates these two distributions. The average distance between the known weave plays is much smaller than the average distance between weave and non-weave plays. In fact, the nearest neighbor of each weave play is most often itself a weave play, 

³For intuition, t-SNE tends to yield a visualization where locally clustered points are close in distance in the full, 100dimensional topic space; points that are farther away from each other tend to be far, but could also be close. 



2017 Research Papers Competition Presented by: 

7 







**(a)** frame 1: (left) Aaron Brooks brings the ball along the left; (right) Deron Williams brings the ball along the left 



**(b)** frame 2: (left) Taj Gibson sets a high screen in the left frame; (right) Deron Williams waits for a screen in the right frame. 



**(c)** frame 3: (left) Aaron Brooks curls around the screen and drives; (right) Brook Lopez sets a high screen for Deron Williams 

**(d)** frame 4: (left) Aaron Brooks attacks the basket; (right) Deron Williams curls around the screen and drives 

**Figure 6:** An example of two very similar possessions: each sub-�igure displays key frames from two possessions — one where Chicago has the ball and one where Brooklyn has the ball. These frames highlight similar features between the two possessions. For a clearer picture of “possession similarity”, please navigate to `https://youtu.be/0Jlj6xekxeI` to see these plays animated. 

highlighting the potential of our technique to quickly �ind a collection of plays similar to a chosen play. 

### **3.3 Between Team Nearest Neighbors** 

Our method also identi�ies similar possession structure between different teams. To highlight this, we select a play at random, and search through the entire database of 190,000 possession sketches to �ind the most similar play. The resulting two possessions are compared in Figure 6. Chicago is on offense in our �irst possession, and Brooklyn is on offense in the nearest-neighbor possession. 

We examine what exactly is similar between these two possessions — which basketball patterns are being modeled by our method. There are a handful of salient similarities: (i) the point guard brings the ball up the left side of the �loor in each possession; (ii) a player sets a high screen on the left side, and the point guard curls around the screen toward the middle with the ball; (iii) through both possessions a player camps out in the weak-side corner three; (iv) the point guard attacks through the middle of the paint. The possession sketch contains this information — and we can further inspect the particular basketball topics for this possession to see how this information is summarized in our model. 

### **3.4 Corner Threes** 

In this section we explore possession sketch similarity in the context of a particular type of shot — a corner three. We �irst sub-select the 2014-2015 data to possessions that include corner three-point 



2017 Research Papers Competition Presented by: 

8 





<!-- Start of picture text -->
GS<br>Hou<br>SA<br><!-- End of picture text -->













**Figure 7:** Corner Three. The left pane cluster examples are similar in that they include a drive to the basket, and a pass to a teammate camping out in the corner. The right pane cluster esamples are similar in that they include a baseline cut toward the corner in which the shot is taken. Please see the animated �igures at `https://youtu.be/hUuPkE06rX4` (left), and `https://youtu.be/mMcWuqgrj1w` (right). 

shots for three teams: the Warriors, the Rockets, and the Spurs. We then apply t-SNE to visualize the resulting shots in Figure 7a. We can immediately notice that the possession sketches that lead to corner threes overlap signi�icantly between teams, however there are some regions of the space in which the Rockets are more likely to inhabit than the Spurs. 

We examine the structure of the possession-map clusters by zooming in on two groups on the op- 



2017 Research Papers Competition Presented by: 

9 



posite side of the map. Figure 7 compares two possessions in the cluster in the left-pane to two possessions in the cluster in the right pane. An immediate difference between the two clusters is that the right pane includes a baseline cut toward the corner in which the shot is taken, whereas the left pane includes a drive into the middle, and a pass out to a player camping out in the corner.⁴ Indeed, these are two very different ways of ending up with a corner three point attempt, and our method identi�ies this and allows us to ef�iciently explore this different structure. 

## **4 Discussion** 

**Relatedwork** Thispaperdevelopsaframeworkforexploringinterpretablepatternsinplayer-tracking data—applicationsofthisframeworkcanenhanceplayerevaluationandmediaconsumption. Asimilar system for measuring play similarity was developed in [12], based on point-wise similarities in trajectories. We take a more data-driven and global approach — we use scalable machine learning techniques to �it a probabilistic model to an entire season’s worth of player tracking data, directly modeling player interactions. The result is a more interpretable, succinct, and scalable decomposition of possessions. 

In [4, 3], the authors propose a stochastic process model to measure the moment-by-moment expected possession value (EPV) of a basketball sequence. They handcraft a set of basketball states that are used in the model. Our approach is more of a data-driven decomposition of basketball states that we use for exploration (but could be used within an EPV model). Other examples that develop data-driven representations from player-tracking data can be found in [11, 7, 6]. 

**Future work and conclusion** There are multiple avenues for future work. Firstly, we can improve the action-template method by inferring the number of actions using more sophisticated methods, such as Bayesian nonparametrics. The action templates should also have more temporal structure — autocorrelation and dynamic variance. Further, our possession sketch ignores much of the temporal information in each possession (a trade-off for statistical and computational ef�iciency). A future project could further describe the time-varying nature of possession strategies, which, for example, would allow us to identify which possessions may have started out in a “weave” set, but broke down into a different sequence. 

Insight derived from player-tracking data has been promised more than delivered. We reduce this gap by devising a method that will have a profound impact on the use of player-tracking data for analysis — from summarizing situational statistics (e.g. how often did the “weave” play succeed?), to searching for similar plays (e.g. for post-game analysis), to discovering and quantifying previously unknown habits of interaction between players (e.g. for team-speci�ic scouting). 

## **References** 

- [1] David M Blei. Probabilistic topic models. _Communications of the ACM_ , 55(4):77–84, 2012. 

- [2] David M Blei, Andrew Y Ng, and Michael I Jordan. Latent dirichlet allocation. _Journal of machine Learning research_ , 3(Jan):993–1022, 2003. 

- [3] Dan Cervone, Alexander D’Amour, Luke Bornn, and Kirk Goldsberry. Pointwise: predicting points and valuing decisions in real time with NBA optical tracking data. 2014. 

- [4] Daniel Cervone, Alexander D’Amour, Luke Bornn, and Kirk Goldsberry. A multiresolution stochastic process model for predicting basketball possession outcomes. _arXiv preprint arXiv:1408.0777_ , 2014. 

⁴Please refer to animated �igures `https://youtu.be/hUuPkE06rX4` (left pane) and `https://youtu.be/mMcWuqgrj1w` (right pane). 



2017 Research Papers Competition Presented by: 

10 



- [5] Arthur P Dempster, Nan M Laird, and Donald B Rubin. Maximum likelihood from incomplete data via the em algorithm. _Journal of the royal statistical society. Series B (methodological)_ , pages 1–38, 1977. 

- [6] Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Counterpoints: Advanced defensive metrics for nba basketball. In _2015 MIT Sloan Sports Analytics Conference_ , 2015. 

- [7] Alexander Franks, Andrew Miller, Luke Bornn, Kirk Goldsberry, et al. Characterizing the spatial structure of defensive skill in professional basketball. _The Annals of Applied Statistics_ , 9(1):94– 121, 2015. 

- [8] Thomas L Grif�iths and Mark Steyvers. Finding scienti�ic topics. _Proceedings of the National academy of Sciences_ , 101(suppl 1):5228–5235, 2004. 

- [9] Matthew D Hoffman, David M Blei, Chong Wang, and John William Paisley. Stochastic variational inference. _Journal of Machine Learning Research_ , 14(1):1303–1347, 2013. 

- [10] Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. _Journal of Machine Learning Research_ , 9(Nov):2579–2605, 2008. 

- [11] Andrew Miller, Luke Bornn, Ryan Adams, and Kirk Goldsberry. Factorized point process intensities: A spatial analysis of professional basketball. In _Proceedings of the 31th International Conference on Machine Learning (ICML-14)_ , 2014. 

- [12] Long Sha, Patrick Lucey, Yisong Yue, Peter Carr, Charlie Rohlf, and Iain Matthews. Chalkboarding: A new spatiotemporal query paradigm for sports play retrieval. In _Proceedings of the 21st International Conference on Intelligent User Interfaces_ , pages 336–347. ACM, 2016. 

- [13] Kuan-ChiehWangandRichardZemel. Classifyingnbaoffensiveplaysusingneuralnetworks. 2016. 



2017 Research Papers Competition Presented by: 

11 



## **A Appendix** 

### **A.1 Segment Clustering Model Details** 

Our clustering model speci�ies _V_ Bezier curve components, _Bv_ : [0 _,_ 1] _�→_ R<sup>2</sup> , each parameterized by _θv ∈_ R<sup>_P ×_2</sup> , where _P_ is the number of _control points_ used to characterize the curve.⁵ 



Importantly, each curve can be speci�ied as a linear function with respect to parameters _θv_ , with a nonlinear (but �ixed) basis in time, _DP_ ( _t_ ). Bezier curves are a natural choice for these data — they are �lexible, concisely parameterized, and easy to �it. The non-linear basis in time allows for a wide variety of template shapes. 

The complete functional clustering model is speci�ied as 



We use maximum likelihood to learn parameters _θv, π,_ and Σ _v_ (and therefore each action) directly from the data set of 4.5 million trajectory segments. To do so ef�iciently, we devise expectation maximization [5]updatesthatexploitthelinearstructureofBeziercurves—eachmaximizationstepcanbecomputed using weighted least squares. Further, each expectation step can operate on each segment in parallel, allowing us to scale our method up to the 4.5 million trajectory segments. We omit the technical details of the inference procedure in this writeup for brevity. 

### **A.2 Topic Model Details** 

Conceptually, LDA de�ines _K topics_ , _ϕk_ , each a distribution over _actions_ . Each observed possession is characterized by some latent distribution over _topics_ , _π_<sup>(</sup><sup>_n_)</sup> , which describes the probability that a particular topic is expressed in possession _n_ . These two distributions — possession-speci�ic proportions and global topics — determine the probability of observing any particular action in possession _n_ . LDA posits the following data generating process to give rise to the matrix of counts 



where _Mn_ is the total number of actions present in possession _n_ (a �ixed constant). We use statistical inference techniques to infer both the global topics, Φ, and the possession-speci�ic proportions, _π_<sup>(</sup><sup>_n_)</sup> for all possessions. Due to the size of the dataset, we use stochastic variational inference [9], a scalable method for Bayesian inference in hierarchical models. 

⁵More control points allow for more �lexibility in �itting shapes — we use 10 control points in our experiments 



2017 Research Papers Competition Presented by: 

12 


