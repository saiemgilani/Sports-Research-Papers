<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2021/2021 - MAYFIELD Machine Learning Algorithm for Yearly Forecasting Indicators and Estimation of Long-Run Player Development - Unknown Authors.pdf -->



# **MAYFIELD: Machine Learning Algorithm for Yearly Forecasting Indicators and Estimation of Long-Run Player Development** 

Alexander H. Williams<sup>1</sup> Department of Economics 

The Ohio State University 

Sethward R. Brugler Benjamin A. Clarke Inventory Systems Department of Computer Science & Engineering General Motors The Ohio State University 

Accurate statistical prediction of American football player development and performance is an important issue in the sports industry. We propose and implement a novel, fast, approximate k-nearest neighbor regression model utilizing localitysensitive hashing in highly dimensional spaces for prediction of yearly National Football League player statistics. MAYFIELD accepts quantitative and qualitative input data and can be calibrated according to a variety of parameters. Concurrently, we propose several new computational metrics for empirical player comparison and evaluation in American football, including a weighted inverse-distance similarity score, stadium and league factors, and NCAA-NFL statistical translations. We utilize a training set of comprehensive NFL statistics from 1970-2009, across all player positions and conduct cross-validation on the model with the subset of 2010-18 NFL statistics. Preliminary results indicate the model to significantly improve on current, publicly available predictive methods. Future training with advanced statistical datasets and integration with scouting-based methods could improve MAYFIELD's accuracy even further. 

_Keywords_ : k-nearest neighbors, regression, locality-sensitive hashing, time-series forecasting, nonparametric models, American football 

## **1. Introduction** 

Accurate forecasting of on-field performance in professional sports is a major component of player evaluation by fans, coaches, and sports executives. Due to a variety of factors, including a lack of highly detailed, publicly available data, emphasis on traditional video scouting methods by coaches and executives, and the relative complexity of the sport, American football is considerably less analytically developed than other professional sports, most notably baseball and basketball. Silver (2003, 2015) presents advanced comprehensive forecasting models for the MLB and NBA, although 

> 1 Corresponding author; can be reached via email at williams.5889@osu.edu. 



1 



these algorithms are proprietary and are thus irreproducible. Schatz (2008) presents a similar noncomprehensive<sup>2</sup> model for the NFL, although it is likewise not publicly available. 

We present a reproducible, comprehensive, learning-based methodology for year-by-year statistical forecasting of NFL players’ careers and implement it on the entire set of post-merger (i.e., after 1970) NFL players. A wide survey of the relevant literature reveals that, to date, no algorithm exists which comprehensively projects NFL player statistics across all positions and utilizes a dataset of MAYFIELD’s size and scope. We also propose several important contributions to football analytics for future implementation into MAYFIELD: an Approximate Value metric for collegiate football players, NCAA-NFL statistical translations which adjust for park and league factors, and a Jameseanstyle Similarity Scores framework for empirical player comparison. 

Our paper proceeds in the following manner. Section 2 describes MAYFIELD's dataset, the operation of the MAYFIELD algorithm, and reviews the relevant previous work which MAYFIELD builds upon. Section 3 gives our initial evaluation of MAYFIELD's accuracy. Section 4 concludes the paper. 

## **2. Methodology** 

### **2.1 Data** 



_Figure 1- Position Mapping_ 

MAYFIELD utilizes a dataset derived from the Pro Football Reference (PFR) historical database consisting of on-field performance statistics and biographical information for every player, team, and season since 1970, when the NFL and the AFL merged. For purpose of analysis, we 

> 2 Offensive linemen and punters are not included in Schatz’s (2008) forecasts. 



2 



segregate the player data into several position groups according to their PFR-listed positions as shown in Figure 1<sup>3</sup> . 

Our on-field statistics comprise a set of standard NFL box-score statistics such as yards, touchdowns, tackles, field goal attempts, etc. As depicted in Figure 2, we limit the set of variables considered for players at a given position to only those relevant to the on-field role of a typical player at that position. Importantly, we include PFR's “Approximate Value" metric (Drinen 2008b), which places a numerical value on the all-inclusive contributions of a player to his team's success in a given season. 

Our biographical data can be split into two categories: static, and dynamic. Static biographical variables are variables for a player whose initial value never changes from year to year, whereas dynamic biographical variables may fluctuate from year to year. We list which biographical variables are used for offensive (i.e., QB, RB, TE, WR, OL) and defensive (i.e., DL, EDGE, LB, CB, S) players in Figure 3<sup>4</sup> . In addition to data collected from PFR, some of the dynamic variables are not taken explicitly from PFR, but instead calculated from the data, including the variables for changes coaching, team, and scheme, consecutive years with a players' current coaches, team, and scheme, and the total AV per game of a team's players at each position during the previous season. One dynamic biographical statistic of note is team ratings from the Simple Rating System (SRS), which is described by Drinen (2006). SRS estimates the strength of a team's offense and defense relative to the league average in terms of points per game- for instance, a team with an offensive SRS of +6.0 would be expected to score 6 more points per game than an average team, all else equal. 



_Figure 2- Biographical Variable Assignment_ 

> 3 Note that some PFR-listed positions are mapped to MAYFIELD's according to the defensive schemes which the player performed under (i.e., 4-3 or 3-4). This is denoted by the name of the scheme marked on the corresponding arrow. 

> 4 Special teams players (K, P) only use the statistics listed in the intersection of Figure 3. Note that static biographical statistics are italicized. 



3 



When predicting a future performance, MAYFIELD combines players' historical performance over many years into overlapping periods of the respective player's career, which we refer to as segments. Each segment consists of a player's static biographical data and _Y_ consecutive seasons of that player's dynamic biographical and performance data. We find the set _S_ of all of the consecutive _Y-_ year segments and use this _S_ as the basis for our training set. 



_Figure 3- Performance Variable Assignment_ 

### **2.2 Statistical Translations** 

### **2.2.1 NFL Equivalencies** 

A major hurdle when comparing raw statistics of professional football players is variance in scoring environments. Kickers, for instance, often experience high performance variance due to weather conditions (Pasteur & Cunningham-Rhoads 2014). Similarly, due to differences in rules across leagues, or the quality and styles of play, players of otherwise equal ability may experience nonrandom variance in their observed statistics. Despite that some of the earliest sabermetrics work addresses this issue in professional baseball (e.g., Davenport 1996; James 1985; Thorn & Palmer 1984), no method yet exists for American football. 

We adopt a method similar to that of Szymborski (1997) to translate players' collegiate and professional statistics to one NFL-average baseline. First, we calculate stadium factors of each statistic for each team and post-merger season using a modified variant of Thorn & Palmer (1984)’s calculations, which we give below. Our base factor Φ<sup>𝑖,𝑡</sup> for team _i_ in year t on a statistic λ , where λ<sup>𝑖,𝑡</sup> is the per-game average of 𝜆 which team _i_ recorded in year _t, and_ λ<sup>′𝑖,𝑡</sup> is the per-game average of 𝜆 which team _i_ allowed in year _t_ , is: 



4 





However, Φ is not entirely satisfactory since it accounts for neither the caliber of the team in question nor its opponents. To resolve the issue, we introduce Thorn & Palmer’s (1984) offensive and defensive team ratings with respect to λ which we call τ. The formulae for 𝜏 are as follows, letting 𝑛<sup>𝑡</sup> be the number of NFL teams playing during the current year: 



Since 𝜏 are codependent, we initialize each 𝜏= 1, and then recompute their values until convergence, typically after 3 iterations. The adjusted stadium factors Ω are then respectively: 



We maintain Thorn & Palmer’s (1984) s segregation of offensive and defensive factors in our calculations; that is, offensive players' statistics are adjusted using Ω𝑜𝑓𝑓 and defensive players' statistics are adjusted using Ω𝑑𝑒𝑓. However, instead of the typical 1-year park factors used in sabermetrics, we utilize an unweighted 5-year moving average of Ω due to the comparably smaller sample size of games in a given NFL season. Without adjustment to the time horizon of stadium factor calculations, random variance in the data may influence stadium factors more than is optimal. 

So far, our stadium factors only differ from those of Thorn & Palmer (1984) in our calculation of Φ. From here, we utilize Szymborski’s (1997) method for our translations. The two remaining components of interest are year and league factors. To adjust for these effects, we compute a leagueyear factor, Θ for λ as follows: 



Θ is just the average team's λ during some base year and league over the average team's λ in a given league and year, times a deflator δ which measures the relative talent level of a player's league as a compared to the base league. We define our base as the NFL 2018-19 season, although any season or league could theoretically be used. The calculation of 𝛿 is not detailed by Szymborski, so where 𝜒<sup>𝑖,𝑡</sup> is the cumulative yearly statistics which player _i_ recorded, we define 𝛿 as the ratio in NFL-average 𝜒<sup>𝑖,𝑡</sup> and the average 𝜒<sup>𝑖,𝑡</sup> for a given league, among players which played in both the NFL and that league over the course of their careers (note that we adjust 𝜒<sup>𝑖,𝑡</sup> with Ω and Θ first before computing averages). 



5 



We conduct translations of both players' collegiate and professional statistics. Importantly, δ is measured separately for each NCAA D-IA conference and an “Other" category for all non-D-IA players. The final translated value of a player's χ<sup>𝑖,𝑡</sup> is then: 



Note that these translations are not a prediction of how a player would have performed during that year if they had been in the NFL, rather, they are an estimation of the player's observed performance in the context of the baseline NFL environment. Changes in playing time due to higher levels of team talent, differences in play style, coaching, and strategy of NFL teams as opposed to collegiate teams, and other factors which influence observed player statistics in more nuanced manners are not captured by these translations. 

### **2.2.2 Collegiate Approximate Value** 

All-inclusive measures of total player contributions to team success are an important component of advanced statistical analysis of sporting performance. The development and spread of such metrics (e.g., Wins Above Replacement in the MLB, Player Efficiency Rating in the NBA, and Real Plus-Minus in the NHL and NBA) have greatly affected both the style of play on the field and the evaluation of player talent off of it. Although less analytically advanced relative to its analogs in other professional sports, Approximate Value (Drinen 2008a) has proven a useful tool for empirically evaluating the performance of NFL athletes. However, Approximate Value is only defined for the NFL, and does not currently support evaluation of collegiate football players. Therefore, we extend Drinen’s (2008a) methodology to NCAA football, and give our formulation of collegiate Approximate Value below. 

Approximate Value evaluates player contributions to team success according to the players' primary positional responsibilities with respect to cumulative team success at that position group. Consider the following partition of offensive team performance, where ζ𝑎 is the fraction of total team offensive output by a positional responsibility _a_ , among skill position players (defined as QB, RB, WR, TE): 





6 



Where 𝑔<sup>𝑖,𝑡</sup> is the number of games which player _i_ 's team played in year _t_ , 𝑇𝑒𝑎𝑚𝑖,𝑡 is the set of <u>χ𝑅𝑢𝑠ℎ𝑌𝑎𝑟𝑑𝑠</u> players on player _i_ 's team in year _t_ , χ𝑌𝑃𝐶 = ~~,~~ χ𝐴𝑌𝐴 = (χ𝑃𝑎𝑠𝑠𝑌𝑎𝑟𝑑𝑠 + 20χ𝑃𝑎𝑠𝑠𝑇𝐷 −45χ𝑃𝑎𝑠𝑠𝐼𝑁𝑇)/ χ𝑅𝑢𝑠ℎ𝐴𝑡𝑡 χ𝑃𝑎𝑠𝑠𝐴𝑡𝑡, and χ𝑇𝑜𝑢𝑐ℎ𝑒𝑠 = χ𝑅𝑢𝑠ℎ𝐴𝑡𝑡 + χ𝑅𝑒𝑐𝑒𝑝𝑡𝑖𝑜𝑛𝑠. Note that here (and thereafter) the leading coefficients on each term are due to Drinen (2008a), and as in Section 2.2.1, averages are calculated within-conference. Furthermore, ζ𝐵𝑙𝑜𝑐𝑘 is used exclusively for the TE position and takes a value of 0 otherwise. So, letting λ𝑃𝑃𝐷 = λ𝑃𝑜𝑖𝑛𝑡𝑠/λ𝐷𝑟𝑖𝑣𝑒𝑠, skill position Approximate Value is thus: 



So far, we use Drinen’s (2008a) method without modification. However, we necessarily deviate for calculation of Approximate Value at the offensive line positions (OT, OG, C) due to Drinen’s (2008a) use of starting lineup and Pro Bowl / All-Pro<sup>5</sup> data, which is unavailable and/or nonexistent at the collegiate level. Therefore, we adopt the following procedure, which substitutes All-America and All-Conference awards for the Pro Bowl and All-Pro dummy variables respectively, and does not utilize starting lineup data: 



We now define defensive Approximate Value: 



Where 𝜓<sup>𝑖</sup> = 0.6 when player _i_ is a DL or EGDE, 0.3 when an LB, and 0.1 when a CB or S. This formulation of defensive AV is identical to that of Drinen (2008a), except for its modification on account of All-Americans and a lack of starting lineups, and that unlike Drinen, we utilize proportions of team-total defensive statistics (i.e., <u>χ</u> ~~)~~ rather than pooling by position group. Special teams 𝑔λ Approximate Value is given as follows: 



> 5 For the unfamiliar reader, these are designations given to the top players at each position in the NFL. 



7 



<u>χ𝑃𝑢𝑛𝑡𝑌𝑎𝑟𝑑𝑠 χ𝑋𝑃 χ𝐹𝐺</u> Where χ𝑌𝑃𝑃 = , χ𝑋𝑃𝑃 = , and χ𝐹𝐺𝑃 = ~~.~~ Finally, the cumulative Approximate Value χ𝑃𝑢𝑛𝑡𝑠 χ𝑋𝑃𝐴𝑡𝑡 χ𝐹𝐺𝐴𝑡𝑡 for a player is thus: 



This formulation of collegiate Approximate Value borrows heavily from Drinen’s (2008a) methodology and is designed to be as similar as feasibly possible, as to make player comparisons of the variety described in Section 2.3 more meaningful, as comparing these “Approximate Values" for one player across his collegiate and professional career yields less useful information the more dissimilar the two metrics are. We now proceed to describe MAYFIELD's algorithmic structure and operation. 

### **2.3 The kNN Algorithm** 

K-nearest neighbor (kNN) algorithms are among the oldest and most widely utilized methods in machine learning. Since Cover (1968) originally put forth kNN<sup>6</sup> , nearest-neighbor algorithms have proliferated in usage for prediction problems in both classification and regression. The nearestneighbor principle from which kNN derives is essentially just that objects which are highly similar in their observable characteristics (i.e., are “nearest neighbors") are likely to be similar in their unknown characteristics as well. Due to the simplicity of this premise and of nearest-neighbor algorithms in general, kNN has been shown as a versatile, but surprisingly effective method for prediction in problems as disparate as credit scoring (Mukid et al. 2018), cardiovascular medicine (Shouman, Turner, & Stocker 2012), and encryption (Wong et al. 2009). Importantly, several advanced player projection techniques similar to MAYFIELD (Silver 2003, 2015; Schatz 2008) utilize nearest-neighbor comparisons, although their proprietary nature prevents analysis of their algorithmic structure (kNN or otherwise). MAYFIELD follows in the tradition of these algorithms, albeit with more formalized and reproducible methods. 

MAYFIELD can be characterized as an approximate kNN regression method for predicting the on-field statistics of National Football League players. In this respect, MAYFIELD is distinct from both kNN classification techniques, which predict categorical variables rather than continuous ones, and exact kNN methods, which search the entire training set for neighbors, as opposed to MAYFIELD's only partial search as controlled by locality-sensitive hashing (see Section 2.3.2). We provide the specification of MAYFIELD's exact structure and operation in the following subsections. 

### **2.3.1 Model Training Procedure** 

Supervised learning methods such as kNN principally depend on parameters whose values are learned via training the specified model on the dataset. This process is achieved by generation of parameter combinations, measurement of the model's accuracy under the given parameter values, and repetition until errors are minimized. Hence, supervised learning is effectively equivalent to the optimization problem posed by finding the parameters values which minimize the model's error. 

MAYFIELD learns the optimal values for 6 + Y distinct weighting parameters, whose respective roles in the MAYFIELD algorithm are detailed in Sections 2.3.2-2.3.6. These weighting 

> 6 For more recent surveys of modern kNN methods, see Bhatia & Vandana (2010) and Altman (1992). 



8 



parameters should be distinguished from hyperparameters, whose values are not learned via optimization, but instead heuristically selected based upon results of cross-validation. More specifically, we specify 5 hyperparameters: K, the number of “nearest neighbors" used to predict players' future performance vectors; Y, the length in years of player career segments; u, the number of years into the future which MAYFIELD predicts performance; T, the number of randomly generated hash functions used during locality-sensitive hashing (see Section 2.3.2); and B, the proportion of the data which is used for calculating each local regression in our LOESS correction (see Section 2.3.5). However, we only select values for K and Y during cross-validation; B and T have little direct relationship to MAYFIELD's accuracy, and we set these ex-ante. u is effectively a hyperparameter in name only, as we train MAYFIELD for all values of 𝑢 ∈{1,2,3}, since different u represent different sets of performance vectors we seek to predict. 

We select the Covariance Matrix Adaptation-Evolution Strategy (CMA-ES) solver for optimizing MAYFIELD's parameters. For an excellent summary of CMA-ES, see Hansen (2016); we describe its basic method and desirable properties here. CMA-ES is a stochastic, evolutionary strategy solver which is especially useful for optimization on ill-conditioned problems (i.e., when fitness functions lack continuity, convexity, linearity, existence of derivatives, separability, low dimensionality, or other simplifying properties), and has been shown to be a highly efficient and reliable method for global optimization (Hansen 2009; Hansen & Kern 2004). As opposed to methods which attempt to directly estimate gradients (e.g., quasi-Newton), CMA-ES estimates a fitness function in several generations, selecting the most optimal parameter value combinations to serve as “parents" for the following generation of parameter estimates, repeating until the fitness function value converges. Since the landscape of player performance vectors is highly rugged, noisy, and highly dimensional, CMA-ES is an ideal optimization algorithm for use in MAYFIELD compared to other existing methods (e.g., BOBYQA, BFGS, Nelder-Mead, Powell, etc.). 

We train MAYFIELD using the CMA-ES algorithm in the following manner. Given the entire training set of _Y_ -length segments _S_ and values for each hyperparameter, we specify a subset 𝑅= {𝑟<sup>𝑖,𝑡</sup> ∈𝑆: ∃𝑟<sup>𝑖,𝑡+𝑢</sup> ∈𝑆} of segments which have corresponding future performance vectors in the training data. After applying the statistical translations of Section 2.2 and converting the quantitative data to percentile ranks, we then apply locality-sensitive hashing on _R_ which generates a reduced set 𝐻𝑟𝑖,𝑡 of nonequivalent and arbitrarily similar segments for each member of _R_ . Given an initial CMAES generation of parameter value combinations, the _K_ most similar segments in 𝐻𝑟𝑖,𝑡 to each 𝑟<sup>𝑖,𝑡</sup> are then used to predict the future performance vectors {𝑣<sup>𝑖,𝑡+𝑢</sup> } which correspond to _R_ and whose value is a function of the parameters. The root-mean squared error across each dimension of the performance vector space _V_ on these predictions is then calculated for each parameter combination. CMA-ES then re-estimates a generation of new parameter combinations based upon the most accurate members of the current generation and continues to repeat the parameters-predictions cycle until errors have converged. Once the solver terminates and returns the trained parameter values, we move on to a cross-validation step where we select the most optimal model across each different combination of hyperparameters, which we describe in Section 2.5. 

### **2.3.2 Locality Sensitive Hashing** 

Locality-sensitive hashing (LSH) is a dimensionality reduction technique commonly employed in nearest neighbor search problems when distance measurements are computationally 



9 



costly. LSH was first proposed by Gionis, Indyk & Motwani (1999) and has acquired a considerable history of usage in statistical similarity measurement and related applications (e.g., Datar et al. 2004; Andoni & Indyk 2008; Andoni et al. 2015; Das et al. 2007; Koga, Ishibashi, & Watanabe 2007; Cochez & Mou 2015; Brizna et al. 2010). 

For any given player segment, MAYFIELD's initial _N_ -order set of comparables may be in excess of 10,000 segments comprising up to _q_ = 49* _Y_ +17 variable dimensions, so some form of dimensionality reduction is necessary to make training MAYFIELD's parameters practically feasible. As a consequence of employing LSH, MAYFIELD is not an exact nearest neighbor search algorithm since some potential neighbors are excluded from distance measurement. However, the manner in which LSH operates ensures with high probability that these excluded segments are unlikely to be of practical interest when _K_ is small relative to _N_ (Leskovec 2001). We describe our LSH procedure below. 

When predicting future performance vectors 𝑣<sup>𝑡+𝑢</sup> ∈𝑉= [0,1]<sup>𝑝</sup> of a segment 𝑟<sup>0</sup> , we begin with a set 𝑅= 𝑟<sup>𝑖,𝑡</sup> of segments which might be compared to 𝑟<sup>0</sup> . Each segment 𝑟<sup>𝑖,𝑡</sup> can thus be viewed as corresponding to a vector in the _q_ -dimensional feature space, _F_ . Due to our choice of distance function (see Section 2.3.3 below for discussion), we apply a linear transformation to _F_ , which yields a modified feature space _F'_ : 



Σ<sup>−</sup> 2<sup>1</sup> is the principal root of the inverse of the auto-covariance matrix Σ of _F_ , and _C_ is a 𝑞 × 𝑞 diagonal matrix of nonnegative weighting coefficients (Section 2.3.3 explains further). Letting 𝑟<sup>′</sup> be the vector in 𝐹<sup>′</sup> corresponding to 𝑟 ∈𝐹, we first construct ⌈𝑙𝑜𝑔_2(𝑁)⌉ hyperplanes. For each hyperplane, we first generate _q_ random vectors, which are distributed under the following multivariate uniform distribution: 



Multiple linear regression on the set {𝑤} of these random vectors yields some affine function 𝑞−1 ′ 𝑓<sup>𝑘∈{1,2…𝑞}</sup> : Π𝑗=1 𝐹𝑗 →𝐹𝑞′ which describes a _q-1_ -dimensional hyperplane that intersects every point in {𝑤}. If we consider 𝑟<sup>′</sup> as just σ, 𝑟𝑞<sup>′</sup> , the resulting hash function _h_ will be: 



Notice that the _j_ th bit of the hash code is just the value of the indicator function for that 𝑟<sup>′𝑖𝑡</sup> 's residual on 𝑓<sup>𝑘</sup> is nonnegative. These hash functions naturally imply a set of segments arbitrarily similar to 𝑟<sup>0</sup> , namely: 



Statistical noise during the hyperplane construction process may result in the exclusion of low-distance comparables due to hyperplanes which cut closer to 𝑟<sup>0</sup> than optimal. Therefore, we 𝑇 𝑘 repeat the LSH process _T_ times and take the union 𝐻𝑟0 =∪𝑘=1 𝐻𝑟0 across the _H_ -sets or repeat until |𝐻𝑟0| ≥𝐾, whichever occurs last. We set the hyperparameter _T_ = 20, although any positive integer 



10 



value could potentially be used instead; however, one should keep in mind that too low of a _T_ will result in a narrow 𝐻𝑟0, while too high of _T_ may not give the desired reduction in runtime. 

### **2.3.3 A Novel Weighted Mahalanobis Distance Metric** 

The canonical nearest neighbor problem for some object of interest _a_ , is to find the most similar object _b_ to a within a search set _A_ , where 𝑎 ∈𝐴 and 𝑎 ≠𝑏, and to then make inferences about _a_ based upon the observable characteristics of _b_ . kNN is a generalization of nearest neighbor search which instead of mapping _a_ to the most similar element _b_ , returns the set 𝐵 ⊆𝐴 of the _K_ elements most similar to _a_ (i.e., |𝐵| = 𝐾 where 𝑎 ∉𝐵). For MAYFIELD, our object of interest is 𝑟<sup>0</sup> , and the search set is the LSH output 𝐻𝑟<sup>0</sup> , which is a set of segments arbitrarily similar to 𝑟<sup>0</sup> . 

The principal question when designing a nearest-neighbor search algorithm is that of similarity measurement. The standard approach (which we adopt) is to specify some distance metric on the search set, and to identify the objects with lower distances to the object of interest as monotonically more similar. While many distance metrics exist which could potentially be utilized, the Mahalanobis distance (MD) is especially useful in similarity learning algorithms such as kNN (Mahalanobis 1936; De Maesschalck, Jouan-Rimbaud, & Massart 2000; Xing et al. 2003; Schultz & Joachims 2004; Woefel & Ekenel 2005). We give the classical formulation of MD below, where _a_ and _b_ are vectors in the feature space _A_ , and Σ is the auto-covariance matrix of the features identified in _A_ : 



MD offers several advantages over more common metrics, such as Euclidean distance. Chiefly, the insertion of the inverse auto-covariance matrix Σ<sup>−1</sup> simultaneously standardizes the scale of each axis (as measured by the feature variance) and adjusts for the presence of correlation between dimensions of the data, which may result in a non-orthonormal basis of _A_ if the issue is left uncorrected (as in Euclidean distance). Moreover, if we set Σ to be just 𝐼𝑞, then 𝑑𝐴 is the Euclidean norm on _A_ . Similarly, any diagonal Σ (for instance, when each feature is pairwise independent) will yield a standardized Euclidean distance. Note that throughout, the distance component for a categorical variable between two segments would be the Jaccard distance (Jaccard 1901), rather than the numerical distance between the pair of vectors. 

However, some authors identify issues with using this formulation of the MD metric. Σ is highly sensitive to the presence of outliers, which may bias estimates of MD (Woefel & Ekenel 2005). Additionally, Σ may perform suboptimally if MD is used for inference on the object of interest, as it does not adjust for the relation between the measured features and those which are being predicted (Schultz & Joachims 2004; Xing et al. 2003). As MAYFIELD is foremost a predictive algorithm, these issues are of serious concern. 

To address the salient problems with classical MD, we make two modifications which should result in a more useful distance metric. Firstly, instead of estimating Σ as the classical auto-covariance matrix, we compute Rousseuw’s (1984) Minimum Covariance Determinant (MCD) estimator Σ. MCD has been shown to be highly robust to outliers (Rousseuw & Van Drissen 1992; Hubert & Debruyne 2010), and previous authors' results demonstrate MCD to be a quite clearly superior estimator of covariance when used in MD calculations. Secondly, we introduce a diagonal matrix 𝐶<sup>2</sup> of weighting 



11 



coefficients into the MD equation in the reparameterization described by Schultz & Joachims (2004). Their “weighted" MD metric replaces Σ with a matrix 𝐴 𝑊 𝐴<sup>⊤</sup> , where _W_ is some 𝑞 × 𝑞 diagonal real matrix with nonnegative entries, and _A_ is any 𝑞 × 𝑞 real matrix such that 𝐴 𝑊 𝐴<sup>⊤</sup> is positive semidefinite. Since Σ is positive semidefinite and symmetric, assuming Σ is nonsingular<sup>7</sup> , it necessarily has a unique positive semidefinite inverse square root (i.e., some _A_ such that 𝐴<sup>2</sup> = Σ<sup>−1</sup> ) ⊤ which is also symmetric (hence Σ<sup>−</sup> 2<sup>1</sup> = Σ<sup>−</sup> 2<sup>1</sup> ). Therefore, we set Schultz & Joachims’ (2004) _A_ equal to the square root of the inverse of Σ as estimated by the MCD (denoted by Σ<sup>−</sup> 2<sup>1</sup> ), and _W_ to a matrix |𝐶|<sup>−</sup> 𝑞<sup>2</sup> 𝐶<sup>2</sup> , which we discuss below. This weighted MD is now: 



Conveniently, 𝑑𝐹 can be interpreted as simply the Euclidean distance between 𝑟<sup>′𝑖,𝑡</sup> and 𝑟<sup>′0</sup> in the linearly transformed space _F'_ . Note that since Σ<sup>−</sup> 2<sup>1</sup> is positive semidefinite, and 𝐶<sup>2</sup> has strictly nonnegative entries independent of the specification of a diagonal _C_ and is thus also positive semidefinite, the product matrix will satisfy Schultz & Joachims (2004) criteria of the positive semidefiniteness of 𝐴 𝑊 𝐴<sup>⊤</sup> . Additionally, since we utilize Σ<sup>−</sup> 2<sup>1</sup> and _C_ in our implementation of LSH, our estimations of Σ and _C_ are performed on the entire population of segments, rather than 𝑟<sup>0</sup> - dependent subsets thereof such as _R_ or 𝐻𝑟0. 

This generalized parameterization of MD is considerably more flexible than the classical variant. Considering each entry 𝐶𝑗,𝑗2 as simply the relative weight placed on the _j_ th feature of 𝐹𝑗∈{1,2,…𝑞}, we are able to link each feature's influence on 𝑑𝐹 to its predictive power. For instance, supposing each feature to have equivalent predictive power, we set 𝐶= 𝐼𝑞, which yields the classical MD, since Σ<sup>−</sup> 2<sup>1</sup> 𝐶<sup>2</sup> Σ<sup>~~−~~</sup> 2<sup>1</sup> = Σ<sup>−1</sup> by definition. 

The optimal measure of a feature's predictive power, especially when predicting future components of a vector as opposed to a singular scalar value, is less clear. While Schultz & Joachims (2004) suggest supervised learning of each coefficient in _C_ , this is impractical for our values of _q_ due to a lack of computing power. We therefore adopt the following approach to estimating _C_ , which yields a computationally more efficient solution. 

The principal goal of setting _C_ is to maximize similarity between the arbitrary segments 𝑟<sup>𝑖1,𝑡</sup> and 𝑟<sup>𝑖2,𝑡</sup> contingent upon the similarity of future performance vectors 𝑣<sup>𝑖1,𝑡+𝑢</sup> and 𝑣<sup>𝑖2,𝑡+𝑢</sup> , respectively. Therefore, we seek to identify the features that correlate most strongly with highly similar future performance of two segments. Consider the random variables η𝑗 and κ, which are respectively the standardized Euclidean (i.e., the classical 1-dimensional Mahalanobis) pairwise distance between 𝑟𝑗𝑖1,𝑡  and 𝑟𝑗𝑖2,𝑡, and the classical MD 𝑑𝐴(𝑣𝑖1,𝑡+𝑢, 𝑣𝑖2,𝑡+𝑢), for any given segments 𝑟𝑖1,𝑡 and 𝑟𝑖2,𝑡: 

> 7 In practice, it is statistically unlikely to observe singular estimates of Σ. In such cases, we utilize the MoorePenrose pseudoinverse of Σ, which exists for any real matrix Σ (Moore 1920; Penrose 1955; Bjerhammar 1951). Additionally, since the pseudoinverse of nonsingular Σ are just Σ<sup>−1</sup> , we may be regarded as simply computing the pseudoinverse of Σ in all cases. 



12 





To calculate _C_ , we first identify the (<sup>𝑁</sup> 2<sup>) nonidentical segments in the population of the data</sup> and compute the values of η𝑗 and κ for each pair under their respective MCD auto-covariance matrices. Letting ρ𝑗 = 𝑐𝑜𝑟𝑟(η𝑗, κ) we appear to have found a suitable candidate for each coefficient on the diagonal of _C_ . However, simply setting each 𝐶𝑗,𝑗 = ρ𝑗 is not quite satisfactory for two reasons. Firstly, if any ρ𝑗 = 0, then _C_ will be singular and result in indeterminate values of 𝑑𝐹, making any estimation of _v_ impossible. Secondly, features which have negative correlations with κ make estimations of _v_ based on 𝑑𝐹 less accurate. These “malignant" features are such that the more similar any two segments are in that dimension of the data, the less similar their corresponding future performance vectors are. Consequently, weighting a malignant feature such that it comprises a higher proportion of 𝑑𝐹 will result in higher selection rates of “near" neighbors which are similar in terms of 𝑟𝑗, but imply predicted _v_ dissimilar to the actual “true" _v_ , resulting in highly imprecise estimates. While the easiest course of action might be to simply remove such features from the calculation of 𝑑𝐹 by setting 𝐶𝑗,𝑗 = 0 ∀ρ𝑗 ≤0, this runs into the former issue of a singular _C_ . Therefore, to ensure strictly positive 𝐶𝑗,𝑗 which appropriately upweight features with large, positive ρ, we adopt the following exponential weighting scheme based on a hyperparameter α ∈[1, `∞` ): 



This 𝐶 in some sense still makes 𝑑𝐹 a “learned" metric on 𝐹 in the same manner which Schultz & Joachims’s (2004) original specification of their “learned" MD; however, our approach is feasible when 𝑞 is large without any loss of resolution in the data via principal components analysis or similar methods. 

### **2.3.4 Inverse Distance-Weighted Similarity Scores** 

It is often useful to compute indices of similarity as an inverse distance function. Whereas a distance metric measures the dissimilarity of two objects on the interval [0, `∞` ), where the larger the distance, the more dissimilar the two objects are, a similarity measure indexes the similarity of two objects on the interval (0,1], with a larger similarity index indicating, as the name suggests, highly similar objects. The key property of any similarity measure is a strictly decreasing image with respect to its corresponding distance metric. Often, similarity measures can be expressed in closed form as kernel functions that map directly from the feature space, which are commonly used in learningbased algorithms (Schoelkopf, Tsuda, & Vert, 2004). 

Similarity measures appear in some sabermetrics and other sports analytics work, albeit in a more informal manner. Bill James (1994) first introduced the concept of “similarity scores" for empirical comparison of Baseball Hall of Fame candidates to its already inducted members, which spawned a variety of methods for sports performance comparison (e.g.  Silver, 2015; Kubatko 2004; Hollinger 2003; Pelton 2003; Drinen 2008b). Some forecasting models (Silver 2003, 2015; Schatz 2008) incorporate similarity scores into their respective methodologies as well. Similarity scores are one of the few areas of advanced empirical analysis of sports in which American football is well- 



13 



represented. Schatz (2010) and Drinen’s (2008b) methodologies are well-known, and more importantly, reproducible. However, almost all work on sports performance similarity scores have used strictly first or second order polynomial models<sup>8</sup> with no consideration for interactions between features. Moreover, the weighting coefficients utilized in such models appear to be completely arbitrary, as their respective authors give no treatment to the procedure used to estimate weights<sup>9</sup> . We seek to rectify these shortcomings by returning to more formally established methods in the non-sporting literature. 

MD has the property that, if features are normally distributed, 𝑑𝐴2 ∼χ2(𝑞). While our data is certainly nonnormal (and moreover, are highly nonindependent), making this property less useful, we percentilize the data, which conforms features to a strictly uniform distribution on (0,1). Linear transformation of the feature space from _F_ into 𝐹<sup>′</sup> modifies the range of the underlying feature distributions, but not their uniformity. Our distance function 𝑑𝐹 is therefore principally a summation of uniformly distributed random variables, which for large _q_ , converges to a normal distribution. Since our _q_ certainly qualify as large (𝑞> 60 in all cases), we may expect the distribution of 𝑑𝐹 to be sufficiently approximated by χ<sup>2</sup> (𝑞). 

We define our similarity score as the probability, given 𝑟<sup>0</sup> , of observing a segment at least as distant from 𝑟<sup>0</sup> as a given segment 𝑟<sup>𝑖,𝑡</sup> , which under the assumed 𝑑𝐹 ∼χ<sup>2</sup> (𝑞): 



Γ and γ are the complete and lower incomplete gamma functions, respectively. Notice that 𝑆𝑆 is just the complement of the χ<sup>2</sup> (𝑞) cumulative distribution function over 𝑑𝐹. For every segment 𝑟<sup>𝑖,𝑡</sup> ∈ 𝐻𝑟0, we compute 𝑆𝑆(𝑟<sup>𝑖,𝑡</sup> , 𝑟<sup>0</sup> ) and identify the following set of 𝑟<sup>0</sup> 's “nearest neighbors": 



Less formally, 𝑀𝑟0 is just the set of the _K_ most similar segments to 𝑟<sup>0</sup> which reside in 𝐻𝑟0, or equivalently, the set of the _K_ segments in 𝐻𝑟0 which are least distant from 𝑟<sup>0</sup> . We now proceed to the following steps in the MAYFIELD algorithm, where we describe MAYFIELD's further utilization of 𝑀𝑟0 in its predictions of 𝑣<sup>0,𝑡+𝑢</sup> . 

### **2.3.5 The Regression Equation** 

Given the set 𝑀𝑟0, our remaining task is to form an estimate of 𝑣<sup>0,𝑡+𝑢</sup> . Consider the set 𝐿𝑟0, the set of future performance vectors which correspond to the members of 𝑀𝑟0: 



> 8 The methods we review exclusively use affine equations over either absolute or squared differences in observed feature values to compute their similarity scores. 

> 9 We speculate that the weighting coefficients of these similarity scores were set a priori by their respective authors, rather than via analytical methods. 



14 



Classical kNN regression techniques (e.g., Benedetti 1977; Altman 1992) typically compute a weighted average of vectors in 𝐿𝑟0 as the predicted value of 𝑣<sup>0,𝑡+𝑢</sup> . However, more recent authors (e.g., Mehdizadeh 2020; Al-Qhatani & Crone 2013; Wen, Song, & Wang 2016) find that incorporating traditional time-series techniques such as autoregressive moving-average (ARMA) terms into the kNN regression equation greatly improves model accuracy and fit in some applications. We therefore take an approach which builds autoregressive terms and a directional component of 𝐿𝑟0 into the classical kNN regression equation: 



The predicted value for 𝑣<sup>0,𝑡+𝑢</sup> is a linear combination of an inverse-distance weighted interpolation of 𝐿𝑟0, a similar interpolation on the net change in 𝑣<sup>𝑖,𝑡10</sup> , and lagged values of 𝑣<sup>0,𝑡</sup> , plus a constant. The first pair of terms is the classical kNN regression value, which is a first-order polynomial on the interpolated 𝑣<sup>𝑖,𝑡+𝑢</sup> weighted by similarity and a parameter β1. The third term is the interpolated change in 𝑣<sup>𝑖,𝑡</sup> weighted by similarity and a parameter β2. The final term is a _Y_ -order autoregressive series on 𝑣<sup>0,𝑡</sup> , which are the single-year components of the performance vector within 𝑟<sup>0</sup> . Note that the φ and β are weighting parameters whose values are learned through the training process. 

We favor this hybrid approach to regression, much like other parts of MAYFIELD, due to its flexibility and computational efficiency. Beyond the aforementioned improvement in accuracy resulting from integrating AR into the kNN model, there are a few other advantageous attributes to the above formulation of the regression equation. One common pitfall of algorithms similar in aim to MAYFIELD is their failure to consistently predict statistics with accuracy better than even a naive model. Simply letting φ3 = 1 and the remaining φ𝑤≠3 = 0 , the above just becomes a naive prediction of 𝑣<sup>0,𝑡+𝑢</sup> . MAYFIELD is thus guaranteed accuracy no worse than either a naive or the classical kNN predicted value, since both methods are subsumed by our model. 

However, we are not quite done. Two potential issues may arise in the above regression, dependent on the local structure of the data in the training set. Firstly, our formulation of the kNN 0,𝑡+𝑢 regression may predict values of  𝑣<sup>0,𝑡+𝑢</sup> which has components 𝑣𝑗 ∉[0,1]. Since percentile ranks not contained on this interval are impossible, we need a method for dealing with such instances in the data. Standard methods in least-squares regression for prediction of bounded dependent variables include transforming the data using an asymptotically bounded function (e.g., probit and logit models), or censoring fitted values which fall outside the interval (e.g., Tobit models). We take a slightly different route due to the second potential issue we identify: systematic bias in 𝑣<sup>0,𝑡+𝑢</sup> , which may arise among any or all of the components of 𝑣<sup>0,𝑡+𝑢</sup> . Since CMA-ES optimization attempts to minimize a scalar error (see Sections 2.3.1 and 2.3.6), each individual dimension of _V_ may be 0,𝑡+𝑢 suboptimally predicted by 𝑣<sup>0,𝑡+𝑢</sup> . We may regard predictions of 𝑣𝑗 ∉[0,1] as a special case of 0,𝑡+𝑢 0,𝑡+𝑢 such systemic bias, since any 𝑣𝑗 > 1 are inherently biased upwards, and any 𝑣𝑗 < 0 are 0,𝑡+𝑢 similarly biased downwards. Additionally, there may be cases where for of some range of 𝑣𝑗 ∈ 

> 10 This term can be unambiguously interpreted as the expected residual of a naive prediction of 𝑣𝑖,𝑡+𝑢. 



15 



0,𝑡+𝑢 0,𝑡+𝑢 0,𝑡+𝑢 [𝑎, 𝑏] ⊆[0,1] the expected residuals 𝐸(𝑣𝑗 −𝑣𝑗 ̂) ∉[𝑎, 𝑏] . For instance, 𝑣𝑗 may be 0,𝑡+𝑢 nonmonotonic with respect to 𝑣𝑗 , or may increase at a rate different from unity. kNN regressions such as MAYFIELD are particularly suspect in this respect, since interpolations on the data as performed in nearest-neighbor algorithms may over-predict regression to the mean. Although we expect such cases to be limited, robustness to such issues is a desirable feature for regression models. 

Given the possible estimation bias that may enter into our regression, we take the additional step of fitting a LOESS model for each feature in _V_ , i.e., regressing 𝑣𝑗0,𝑡+𝑢 on 𝑣𝑗0,𝑡+𝑢. LOESS, or locally estimated scatterplot smoothing, was independently discovered by Savitzky & Golay (1964) and Cleveland (1979), and has since become widely utilized in several fields of application, including learning-based algorithms (e.g., Cleveland & Devlin 1988; Cleveland, Grosse, & Shyu, 1992; Jacoby 2000; Trexler & Travis 1993; Berger et al., 2004; Howarth & McArthur 1997; McArthur & Howarth 2001). LOESS is a nonparametric method which estimates weighted low-order polynomial regressions on overlapping subsets of the independent variable and constructs a smoothed function on the local polynomials. The size of these subsets depends on the bandwidth hyperparameter _B_ , which is the ratio of the order of the subsets to _N_ , the number of total players in _R_ . Larger values of _B_ result in smoother results and make the locally estimated polynomials more robust to outliers. We set 𝐵= 𝑙𝑜𝑔2(𝑁) ~~,~~ which results in a relatively large bandwidth, as our data is both highly noisy and 𝑁 highly dense. So, where 𝑔𝑗 is the LOESS-constructed function for the _j_ th feature of _V_ , our final predicted value of the performance vector 𝑣<sup>0,𝑡+𝑢</sup> is: 



Our utilization of this LOESS correction to 𝑣<sup>0,𝑡+𝑢</sup> yields several advantages. Firstly, the aforementioned issues of ill-defined and biased values of 𝑣<sup>0,𝑡+𝑢</sup> ̂are resolved. Secondly, the nonparametric nature of LOESS admits a far more flexible bias correction than the standard parametric models; cases of non-monotonically increasing 𝑣<sup>0,𝑡+𝑢</sup> with respect to 𝑣<sup>0,𝑡+𝑢</sup> are likely to benefit. Thirdly, LOESS's confidence intervals are calculated based on the local structure of the data, as opposed to aggregate measures of variance (as in most least-squares regressions) and give a meaningful and ready-made confidence bounds on the expected range of 𝑣<sup>0,𝑡+𝑢</sup> . These may be especially useful when more than just point-estimates of 𝑣<sup>0,𝑡+𝑢</sup> are required. Finally, investigation on the shape of the LOESS-generated functions 𝑔𝑗 may reveal various characteristics of 𝑣<sup>0,𝑡+𝑢</sup> such as over or under-prediction of regression to the mean, artificially induced clustering, or lack of predictive power by the training data. 

Note that while it is possible to absorb the linear regression in the above formula into the LOESS correction by simply computing a multiple LOESS regression of 𝑣<sup>0,𝑡+𝑢</sup> on the respective terms in the former regression stage, there are good reasons against doing so. Since we are interested in the values of 𝜑, which offer a measure of the relative importance of the respective components in the above formula, LOESS' lack of a functional form with directly interpretable coefficients would mean that combining the two regression stages would result in a loss of this information. Additionally, we intend LOESS as a minor correction to the prediction of 𝑣<sup>0,𝑡+𝑢</sup> , not the prediction itself; due to LOESS' 



16 



flexibility, overfitting, especially in a multiple regression setting, is a concern for the out-of-sample robustness of 𝑣<sup>0,𝑡+𝑢</sup> . Moreover, LOESS is computationally expensive, especially when performed on multivariate data, so letting LOESS estimate 𝑣<sup>0,𝑡+𝑢</sup> from 𝑆𝑆(𝑟<sup>0</sup> , 𝑟<sup>𝑖,𝑡</sup> ), 𝑣<sup>0,𝑡−𝑤−1</sup> , 𝑣<sup>𝑖,𝑡+𝑢</sup> , and 𝑣<sup>𝑖,𝑡</sup> would result in far greater runtimes than with our linear first stage and a univariate LOESS correction. 

#### **2.3.6 RMSE Fitness Function** 

After predicting 𝑣<sup>𝑖,𝑡+𝑢</sup> for all 𝑟<sup>𝑖,𝑡</sup> ∈𝑅, we need a mechanism for computing the cumulative error of 𝑣<sup>0,𝑡+𝑢</sup> across all dimensions of _V_ . Standard methods, such as computing root-mean squared error (RMSE) or mean absolute scaled error (MASE), may work for predicting univariate data, but for estimating _V_ , do not have readily available formulations for comparing accuracy across the entire 

performance vector space _V_ . Hence, we require an extra step to convert 𝑣<sup>0,𝑡+𝑢</sup> − 𝑣<sup>0,𝑡+𝑢</sup> from a _p_ - dimensional vector to a scalar value. 

Fortunately, we have already specified a metric which has this capacity: the classical Mahalanobis distance. In fact, classical MD is especially useful since it adjusts for covariance between the dimensions of _V_ , and thus constitutes a measure of the general lack of information on 𝑣<sup>0,𝑡+𝑢</sup> with 

respect to 𝑣<sup>0,𝑡+𝑢</sup> , rather than simply the cumulative observed errors across each dimension. After computing the classical MD between the predicted and realized values of 𝑣<sup>0,𝑡+𝑢</sup> , errors can be interpreted as univariate, and methods such as RMSE and MASE may then be applied to measure the cumulative error across the set of all 𝑣<sup>0,𝑡+𝑢</sup> . Therefore, we specify our fitness function, whose value the CMA-ES optimizer attempts to minimize, as follows: 



ε is thus the RMSE of the classical MD between 𝑣<sup>𝑖,𝑡+𝑢</sup> and 𝑣<sup>𝑖,𝑡+𝑢</sup> for all segments in _R_ . While ε will depend on the local structure of the data in _R_ , it is principally a function of the weighting parameters ε, β1, and β2, and the set of φ, which MAYFIELD learns via CMA-ES minimization of ε. 

|**Position **|**_U = 1_**|**_U = 2_**|**_U =3_**|
|---|---|---|---|
|**QB**|15|15|15|
|**RB**|20|40|35|
|**WR**|15|45|50|
|**TE**|45|50|45|
|**OL**|50|40|50|
|**DL**|30|30|25|
|**EDGE**|15|15|25|
|**LB**|20|20|40|
|**CB**|25|40|45|
|**S**|20|45|50|
|**K**|10|10|45|
|**P**|45|50|50|



Table 1: Optimal _K_ 



17 



### **2.4 Cross-Validation Procedure** 

To select the optimal hyperparameters for MAYFIELD, we first train (via the CMA-ES optimizer) MAYFIELD's parameters on a 1970-2009 subset of the data, and then evaluate MAYFIELD's out-of-sample accuracy on a 2010-2018 subset of the data in a cross-validation step. We test values of _K_ ∈ {5,10,15,20,25,30,35,40,45,50} and _u_ ∈ {1,2,3} with _Y_ = 3 . We present the results of our cross-validation above in Table 1. Note that for player-seasons for which the player in question has played less than _Y_ years, we use his predicted stats for _Y_ = _y_ , where _y_ is the length in years of the player's career so far, and the same value of _K_ as is _Y_ were unchanged. RMSE are stable between the training set and the out-of-sample results, indicating that MAYFIELD is not accuracy due to spurious variation in the data, but rather genuine predictive power (see Table 2 for example) 

Table 2: MAYFIELD Tight End RMSEs (u=2) In-sample vs. out-of-sample 

||Games|Games<br>Started|AV|All<br>pro|Pro<br>bowl|2pt<br>conversions|Fumbles|Receptions|Targets|Rec<br>yards|Rec<br>td|
|---|---|---|---|---|---|---|---|---|---|---|---|
|In-||||||||||||
|sample|2.63|3.37|1.33|0.13|0.20|0.15|0.62|11.34|15.08|137.32|1.46|
|Out-of-||||||||||||
|sample|2.67|3.38|1.46|0.16|0.25|0.23|0.44|11.88|18.95|137.43|1.51|



## **3. Results** 

To evaluate the effectiveness of MAYFIELD, we compared the predicted season results of our model to the 2010-2017 predictions of KUBIAK (Schatz, 2008), the foremost football statistics prediction model. Similar to MAYFIELD, KUBIAK considers historical performance of each player over multiple seasons, biographical statistics, and comparisons to similar players. We compare the standardized RMSEs (i.e., where 1.0 represents an RMSE of 1 standard deviation, lower is better) for all positions below: 





_Figure 4- MAYFIELD vs. KUBIAK Standardized RMSEs_ 



18 















_Figure 5 (contd.)- MAYFIELD vs. KUBIAK Standardized RMSEs_ 



19 







_Figure 6 (contd.)- MAYFIELD vs. KUBIAK Standardized RMSEs_ 

Overall, MAYFIELD offers a substantial improvement in accuracy over KUBIAK's methods in every position as shown by the graphs above. Furthermore, MAYFIELD's standardized RMSEs are more balanced across each statistic as compared to KUBIAK. MAYFIELD's main weaknesses appear to be the prediction of defensive/special teams touchdowns and wide receiver rushing statistics. For almost every position that includes the defensive/special teams TD statistic, MAYFIELD's standardized RMSE’s for these variables were among the largest among all statistics at the respective positions and were also usually larger than the KUBIAK values. In addition to these categories, the only other case where KUBIAK significantly (at 90% confidence) outperformed MAYFIELD was for wide receiver rushing statistics (rushing attempts, yards, touchdowns). While these previously mentioned variables, are better estimated by KUBIAK, they are not truly indicative of player performance for that respective position, as defensive touchdowns, special teams touchdowns, and wide receiver rushes are currently rare occurrences in the NFL and not stable. MAYFIELD is significantly better than KUBIAK for all other statistics. This includes all quarterback, tight end, and kicker statistics. This also includes all statistics that are very relevant to their respective positions, including running back rushing attempts, yards, touchdowns and fumbles, wide receiver targets, receptions, receiving yards and touchdowns, and defensive solo tackles, assisted tackles, tackles for loss, sacks, forced fumbles, fumble recoveries, pass deflections, and interceptions. These statistics are better indicative of player talent level and of a team’s performance as a whole. 



20 



Table 3: MAYFIELD RMSEs (u=1) 2010-2017 out-of-sample 

||**QB **|**RB**|**WR**|**TE**|**OL **|**DL**|**EDGE **|**LB**|**CB **|**S**|**K**|**P**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Games**|2.78|2.98|3.31|2.73|4.30|2.44|3.06|2.68|2.54|2.45|2.35|2.32|
|**Games Started**|2.01|3.07|3.28|3.09|5.14|2.97|3.04|3.39|2.81|3.38|1.62|1.16|
|**AV**|2.36|1.91|1.67|1.34|3.05|1.58|1.67|1.54|1.36|1.32|1.47|2.80|
|**All pro**<br>|0.15<br>|0.17|0.16|0.14|0.20|0.15|0.18<br>|0.15|0.18|0.18|0.18|0.19|
|**Pro bowl**|0.25|0.23|0.23|0.22|0.28|0.21|0.25|0.20|0.23|0.24|0.24|0.22|
|**2pt conversions**|0.17|0.29|0.30|0.22|||||||||
|**Pass comp**<br>|44.77<br>||||||||||||
|**Pass att**|70.07||||||||||||
|**Pass yards**|508.44||||||||||||
|**Pass td**|5.13<br>||||||||||||
|**Pass int**|3.56||||||||||||
|**Pass sack**|6.89||||||||||||
|**Pass sack yards**|48.28||||||||||||
|**Rush att**|8.73|34.64|16.31||||||||||
|**Rush yard**|51.69|161.23|77.93||||||||||
|<br>**Rush td**|1.08|1.60|0.66||||||||||
|**Fumbles**|2.28|1.09|0.94|0.45|||||0.35|0.34|||
|**Receptions**||8.85|12.02|10.55|||||||||
|<br>**Targets**||17.04|22.80|16.82|||||||||
|**Rec yards**||92.92|157.14|123.76|||||||||
|**Rec td**||1.14|1.94|1.45|||||||||
|**Punt ret**||3.35|5.21||||||2.48|2.39|||
|**Punt ret yards**||35.90|53.86||||||25.61|25.35|||
|<br>**Punt ret TD**||0.11|0.18||||||0.08|0.08|||
|**Kick ret**||3.53|4.10||||||1.86|1.89|||
|**Kick ret yards**||93.12|108.70||||||48.66|49.44|||
|**Kick ret TD**||0.11|0.12||||||0.02|0.02|||
|**Forced fumb**||||||0.86|1.06|0.89|0.77|0.77|||
|**Fumb rec**<br>||||||0.61<br>|0.68<br>|0.65<br>|0.60<br>|0.62<br>|||
|**Fumb rec yards**||||||5.14|9.04|7.94|9.30|9.29|||
|**Fumb rec TD**||||||0.15|0.20|0.18|0.18|0.18|||
|**Sacks**<br>||||||2.12<br>|2.34<br>|1.81<br>|0.83<br>|0.82<br>|||
|**Tfl**||||||2.82|3.09|2.72|1.56|1.61|||
|**Solo tackle**||||||7.94|11.56|14.45|13.17|13.59|||
|**Ast tackle**||||||5.14|6.21|8.45|6.18|6.26|||
|**QB hits**||||||5.02|5.32|3.83|1.80|1.85|||
|**Safeties**||||||0.13|0.15|0.13|0.06|0.07|||
|**Pass deflection**||||||1.58|1.93|2.21|3.33|3.34|||
|**Int**|||||||0.47|0.70|1.07|1.10|||
|**Int yards**|||||||8.68|13.62|22.65|22.85|||
|**Int TD**<br>|||||||0.18|0.22|0.32|0.32|||
|**FGA 0-19**|||||||||||0.38||
|**FGM 0-19**|||||||||||0.38||
|**FGA 20-29**<br>|||||||||||2.35<br>||
|**FGM 20-29**|||||||||||2.23||
|**FGA 30-39**|||||||||||2.35||
|**FGM 30-39**<br>|||||||||||2.25<br>||
|**FGA 40-49**|||||||||||2.59||
|**FGM 40-49**|||||||||||2.41||
|**FGA 50+**|||||||||||192||
|<br>**FGM 50+**|||||||||||.<br>1.56||
|**FGM Long**|||||||||||5.24||
|**XPA**|||||||||||8.06||
|**XPM**|||||||||||8.06||
|**Punt att**||||||||||||8.62|
|**Punt yards**||||||||||||403.88|
|**Punt block**||||||||||||0.53|
|**Punt Long**||||||||||||5.81|





21 



## **4. Conclusion** 

MAYFIELD displays excellent predictive accuracy across all positions and appears to be very balanced across the performance variables, rather than targeting a few specific variables. This is likely due to the endogenous nature of MAYFIELD’s parameter weighting scheme (as discussed in Section 2.3), its large sample size of player comparisons to draw upon, and its algorithmic architecture that builds in state-of-the-art computational tools from the computer science, statistics, and sports analytics literature. Given the results shown here, MAYFIELD could be successfully applied for numerous sports forecasting problems, such as in player scouting, sports gambling, and prediction of team-level performance and results. 

The MAYFIELD algorithm we propose is designed in a manner which supports integration with possible future advances in football analytics.  For instance, while our dataset consists of only standard box-score performance variables, newer metrics reliant<sup>11</sup> upon player-tracking or other advanced techniques are easily absorbed into MAYFIELD's feature space, since our distance function is robust to missing data (a major concern for any newer metrics which are unable to be calculated for historical data). Similarly, integration with other contextual data, such as player positions on depth chart, scouting report grades, and medical or salary information, would likewise increase MAYFIELD's accuracy by their addition to the feature space without any modification needed to make full use of the inserted variables. 

Most American sports, such as baseball and basketball, have experienced a boom in analytics while football has fallen behind. Factors such as the complexity of the sport, emphasis on traditional scouting methods, and lack of high-quality public data have led to this gap. Our MAYFIELD algorithm is an effort to close that gap. Similar methods exist in other sports such as those proposed by Silver (2003, 2015), but the algorithm details are not as transparent as MAYFIELD. Attempts to produce a similar model for football (Schatz 2008) focus only on fantasyrelevant players and have methods which are likewise largely not publicly available. We present a reproducible, comprehensive, learning-based methodology for year-by-year statistical forecasting of NFL players' careers and implement it on the entire set of post-merger NFL players. The initial results we present here indicate MAYFIELD to be an improvement over currently existing methods. Based on a wide survey of the relevant literature, MAYFIELD is unprecedented in size and scope of application. We also propose several important contributions to football analytics for future implementation into MAYFIELD: an Approximate Value metric for collegiate football players, NCAANFL statistical translations which adjust for park and league factors, and a Jamesean-style Similarity Scores framework for empirical player comparison. These advancements represent substantial progress in updating football analytics methods to the state-of-the-art as compared to other professional sports and demonstrate MAYFIELD's potential for utilization by football decision-makers, statisticians, and fans alike. 

> 11 E.g., pass blocking and pass rushing win rate (Burke 2018), air yards, completion percentage allowed, nflWAR (Yurko, Ventura, & Horowitz 2019), etc. 



22 



## **Acknowledgements** 

We thank Dr. John Draper and Dr. Ryan Ruddy for their guidance on the project. Their advice, assistance, and encouragement proved invaluable. Additionally, we thank Dr. Chris Knoester and the Ohio State University Sports and Society Initiative for their support, Jesse Chick, Nick Sarkauskas and Dr. Dhabaleswar Panda for their technical assistance, and Josh Krassenstein for his contributions to the project’s initial stages. Finally, we thank Aaron Schatz and Football Outsiders for generously sharing KUBIAK’s historical data with us. 

## **References** 

- Al-Qhatani, F., Crone, S. 2013. Multivariate k-nearest neighbour regression for time series data — a novel algorithm for forecasting UK electricity demand. Proceedings of the 2013 International Joint Conference on Neural Networks, 228-235. 

- Altman, N.S. 1992. An introduction to kernel and nearest neighbor nonparametric regression. The American Statistician, 4(3): 175-185. 

- Andoni, A., Indyk, P. 2008. Near-optimal hashing algorithms for approximate nearest neighbor in high dimensions. Communications of the ACM, 51(1): 117-122. 

- Andoni, A., Indyk, P., Laarhoven, T., Razenshteyn, I., Schmidt, L. 2015. Practical and optimal LSH for angular distance. Proceedings of the 28th International Conference on Neural Information Processing Systems, 1225–1233. 

- Benedetti, J. K. 1977. On the Nonparametric Estimation of Regression Functions. Journal of the Royal Statistical Society Series B, 39(2): 248-253. 

- Berger, J., Hautaniemi, S, Jaervinen, A.K., Edgren, H. Mitra S.K., Astola, J. 2004. Optimized LOWESS normalization parameter selection for DNA microarray data. BMC Bioinformatics, 5(194): 1- 13. 

- Bhatia, N., Vandana. 2010. Survey of nearest neighbor techniques. International Journal of Computer Science and Information Security, 8(2): 302-305. 

- Bjerhammar, A. 1951. Application of calculus of matrices to method of least squares; with special references to geodetic calculations. Transactions of the Royal Institute of Technology, 49. 

- Brizna, D., Schultz, M., Tesler, G., Bafna, V. 2010. RAPID detection of gene-gene interactions in genome-wide association studies. Bioinformatics, 26(22): 2856-2862. 

- Burke, B. 2018. We created better pass-rusher and pass-blocker stats: How they work. ESPN. Accessed at https://www.espn.com/nfl/story/\_/id/24892208/creating-better-nfl-passblocking-pass-rushing-stats-analytics-explainer-faq-how-work. 

- Cleveland, W.S. 1979. Robust locally weighted regression and smoothing scatterplots. Journal of the American Statistical Association, 74(368): 829-836. 



23 



Cleveland, W.S., Devlin, S. 1988. Locally weighted regression: an approach to regression analysis by local fitting. Journal of the American Statistical Association, 83(403): 596-610. 

- Cleveland, W.S., Grosse, E., Shyu, W.M. Local regression models; 309-376 in Chambers, J.M., Hastie, T. 1992. Statistical models in S. Chapman & Hall / CRC Press. Print. 

- Cochez, M., Mou, H. 2015. Twister tries: approximate hierarchical agglomerative clustering for average distance in linear time. Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data, 505-517. 

- Cover, T. 1968. Estimation by the nearest neighbor rule. IEEE Transactions on Information Theory, 14(1): 50-55. 

- Das, A., Datar, M., Garg, A., Rajaram, S.S. 2007. Google news personalization: scalable online collaborative filtering. Proceedings of the 16th International Conference on World Wide Web, 271-280. 

- Datar, M., Immorlica, N., Indyk, P., Mirrokni., V. 2004. Locality-sensitive hashing scheme based on p- stable distributions. Proceedings of the twentieth annual symposium on Computational geometry,  253-262. 

- Davenport, C. Davenport Translations; in Huckaby, G., Davenport, C., Jazayerli, R., Kahrl, C., Sheehan, J. 1996. Baseball Prospectus 1996. Baseball Prospectus LLC. Accessed at https://legacy.baseballprospectus.com/other/bp1996/dtessay.html. 

- De Maesschalck, R. Jouan-Rimbaud, D. Massart, D.L. 2000. The Mahalanobis distance. Chemometrics and Intelligent Laboratory Systems, 50(1): 1-18. 

- Drinen, D. 2006. A very simple ranking system. Pro Football Reference. Accessed at https://www.pro-football-reference.com/blog/index4837.html?p=37. 

- Drinen, D. 2008. Approximate value in the NFL. Pro Football Reference. Accessed at https://www.pro-football-reference.com/blog/index6b92.html?p=465. 

- Drinen, D. 2008. Who is the current Dave Duerson?. Pro Football Reference. Accessed at https://www.pro-football-reference.com/blog/indexa215.html?p=556. 

- Gionis, A., Indyk, P., Motwani, R. 1999. Similarity search in high dimensions via hashing. Proceedings of the 25th VLDB Conference, 518-529. 

- Hansen, N. 2009. Benchmarking a bi-population CMA-ES on the BBOB-2009 function testbed. Workshop Proceedings of the GECCO Genetic and Evolutionary Computation Conference, 2389-2395. 

- Hansen, N. 2016. The CMA Evolution Strategy: a tutorial. ArXiv Preprint: 1604.0077. Accessed at https://arxiv.org/abs/1604.00772. 

- Hansen, N., Kern, S. 2004. Evaluating the CMA Evolution Strategy on multimodal test functions. Proceedings of the Eighth International Conference on Parallel Problem Solving from Nature PPSN VIII, 282-291. 



24 



Hollinger, J. 2003. Pro Basketball Prospectus: 2003 Edition. University of Nebraska Press. Print. 

- Howarth, R.J., McArthur, J.M. 1997. Statistics For strontium isotope stratigraphy: a robust Lowess fit to the marine sr‐isotope curve for 0 to 206 Ma, with look‐up table for derivation of numeric age. The Journal of Geology, 105(4): 441-456. 

- Hubert, M., Debruyne, M. 2010. Minimum covariance determinant. Computational Statistics, 2(1): 3643. 

- Jaccard, P. 1901. Etude comparative de la distribution florale dans une portion des Alpes et du Jura., Bulletin de la Soci'et'e Vaudoise des Sciences Naturelles, 37(1): 547–579. 

- Jacoby, W. 2000. Loess: a nonparametric, graphical tool for depicting relationships between variables. Electoral Studies, 19(4): 577-613. 

James, B. 1985. The Bill James baseball abstract, 1985. Ballantine Books. Print. 

James, B. 1994. The politics of glory. Macmillan Publishers. Print. 

- Kerhet, A. Small, C. Quon, H. Riauka, T. Schrader, L. Greiner, R. Yee, D. McEwan, A. Roa, W. 2010. Application of machine learning methodology for PET-based definition of lung cancer. Current Oncology, 17(1): 41–47. 

- Koga, H., Ishibashi, T., Watanabe, T. 2007. Fast agglomerative hierarchical clustering algorithm using locality-sensitive hashing. Knowledge and Information Systems, 12(1): 25-53. 

- Kubatko, J. 2004. Similarity scores. Basketball Reference. Accessed at https://www.basketballreference.com/about/similar.html. 

- Leskovec, J., Rajaraman, A., Ullman, J. 2011. Mining of massive datasets. Cambridge University Press. Print. 

- Mahalanobis, P.C. 1936. On the generalized distance in statistics. Proceedings of National Institute of Sciences, 2(1): 49-55. 

- McArthur, J.M., Howarth, R.J., Bailey, T.R. 2001. Strontium isotope stratigraphy: LOWESS version 3: best fit to the marine sr‐isotope curve for 0–509 Ma and accompanying look‐up table for deriving numerical age. The Journal of Geology, 109(2): 155-170. 

- Mehdizadeh, S. 2020. Using AR, MA, and ARMA time series models to improve the performance of MARS and KNN approaches in monthly precipitation modeling under limited climatic data. Water Resources Management, 34(1): 263–282. 

- Moore, E. H. 1920. On the reciprocal of the general algebraic matrix. Bulletin of the American Mathematical Society, 26(9): 394–95. 

- Mukid, M.A., Widiharih, T., Rusgiyono, A., Prahutama, A. 2018. Credit scoring analysis using weighted k nearest neighbor. Journal of Physics: Conference Series, 1025(1): 012114. 

- Pasteur, R., Cunningham-Rhoads, K. 2014. An expectation-based metric for NFL field goal kickers. Journal of Quantitative Analysis in Sports, 10(1): 49-66. 



25 



- Pelton, K. 2003. Review: Pro Basketball Prospectus: 2003-04 Edition. Hoopsworld. Accessed at http://www.hoopsworld.com/article\_5978.shtml. 

- Penrose, R. 1955. A generalized inverse for matrices. Proceedings of the Cambridge Philosophical Society, 51(3): 406–13. 

- Rezvani, M., Hashemi, S.M. 2012. Enhancing accuracy of topic sensitive PageRank using Jaccard Index and cosine similarity. Proceedings of the 2012 IEEE/WIC/ACM International Conferences on Web Intelligence and Intelligent Agent Technology, 620-624. 

- Rousseeuw, P. 1984. Least median of squares regression. Journal of the American Statistical Association, 79(338): 871-880. 

- Rousseeuw, P., Van Driessen, K. 1999. A fast algorithm for the minimum covariance determinant estimator. Technometrics, 41(3): 212-223. 

- Savitzky, A., Golay, M.J.E. 1964. Smoothing and differentiation of data by simplified least squares procedures. Analytical Chemistry, 36(8): 1627–1639. 

Schatz, A. 2008. Pro Football Prospectus 2008. Plume. Print. 

- Schatz, A. 2010. Football Outsiders similarity scores. Football Outsiders. Accessed at https://www.footballoutsiders.com/stats/similarity. 

- Schoelkopf, B., Tsuda, K., Vert, J.P. 2004. Primer on kernel methods in computational biology. MIT Press. Print. 

- Schultz, M., Joachims, T. 2004. Learning a distance metric from relative comparisons. Proceedings of the 16th International Conference on Neural Information Processing Systems, 41-48. 

- Shouman, M., Turner, T., Stocker, R. 2012. Applying k-Nearest Neighbour in diagnosing heart disease patients. International Journal of Information and Education Technology, 2(3): 220-223. 

- Silver, N. Introducing PECOTA; 507-514 in Huckaby, G., Kahrl, C., Pease, D. 2003. Baseball Prospectus: 2003 Edition. Potomac Books. Print. 

- Silver, N. 2015. We're predicting the career of every NBA player. Here's how. FiveThirtyEight. Accessed at https://fivethirtyeight.com/features/how-were-predicting-nba-player-career/. 

- Szymborski, D. 1997. How to calculate MLEs. Baseball Think Factory. Accessed at https://www.baseballthinkfactory.org/btf/scholars/czerny/articles/calculatingMLEs.htm. 

- Thorn, J., Palmer, P. 1984. The hidden game of baseball. Knopf Doubleday Publishing Group. Print. 

Trexler, J., Travis, J. 1993. Nontraditional regression analyses. Ecology, 74(6): 1629-1637. 

- Wen Y., Song M., Wang, J. 2016. A combined AR-kNN model for short-term wind speed forecasting. Proceedings of the 2016 IEEE 55th Conference on Decision and Control, online. 

- Woelfel, M., Ekenel, H.K. 2005. Feature weighted mahalanobis distance: improved robustness for Gaussian classifiers. Proceedings of the 2005 13th European Signal Processing Conference, online. 



26 



- Wong, W.K., Cheung, D.W., Kao, B., Mamoulis, N. 2009. Secure kNN computation on encrypted databases. Proceedings of the 2009 ACM SIGMOD International Conference on Management of data, 139–152. 

- Xing, E., Ng, A., Jordan, M., Russell, S. 2003. Distance metric learning with application to clustering with side-information. Proceedings of the 15th International Conference on Neural Information Processing Systems, 521-528. 

- Yurko, R., Ventura, S., Horowitz, M. nflWAR: a reproducible method for offensive player evaluation in football. Journal of Quantitative Analysis in Sports, 15(3): 163-183. 



27 


