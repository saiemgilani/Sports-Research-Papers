<!-- source: 2014 Factorized Point Process Intensities - Spatial Analysis.pdf -->

# **Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 

### **Andrew Miller** 

ACM@SEAS.HARVARD.EDU 

School of Engineering and Applied Sciences, Harvard University, Cambridge, USA 

### **Luke Bornn** 

BORNN@STAT.HARVARD.EDU 

Department of Statistics, Harvard University, Cambridge, USA 

**Ryan Adams** 

RPA@SEAS.HARVARD.EDU 

School of Engineering and Applied Sciences, Harvard University, Cambridge, USA 

**Kirk Goldsberry** KGOLDSBERRY@FAS.HARVARD.EDU 

Center for Geographic Analysis, Harvard University, Cambridge, USA 

## **Abstract** 

We develop a machine learning approach to represent and analyze the underlying spatial structure that governs shot selection among professional basketball players in the NBA. Typically, NBA players are discussed and compared in an heuristic, imprecise manner that relies on unmeasured intuitions about player behavior. This makes it difficult to draw comparisons between players and make accurate player specific predictions. Modeling shot attempt data as a point process, we create a low dimensional representation of offensive player types in the NBA. Using non-negative matrix factorization (NMF), an unsupervised dimensionality reduction technique, we show that a low-rank spatial decomposition summarizes the shooting habits of NBA players. The spatial representations discovered by the algorithm correspond to intuitive descriptions of NBA player types, and can be used to model other spatial effects, such as shooting accuracy. 

## **1. Introduction** 

The spatial locations of made and missed shot attempts in basketball are naturally modeled as a point process. The Poisson process and its inhomogeneous variant are popular choices to model point data in spatial and temporal settings. Inferring the latent intensity function, _λ_ ( _·_ ), is an 

_Proceedings of the 31_<sup>_st_</sup> _International Conference on Machine Learning_ , Beijing, China, 2014. JMLR: W&CP volume 32. Copyright 2014 by the author(s). 

effective way to characterize a Poisson process, and _λ_ ( _·_ ) itself is typically of interest. Nonparametric methods to fit intensity functions are often desirable due to their flexibility and expressiveness, and have been explored at length (Cox, 1955; Møller et al., 1998; Diggle, 2013). Nonparametric intensity surfaces have been used in many applied settings, including density estimation (Adams et al., 2009), disease mapping (Benes et al., 2002), and models of neural spiking (Cunningham et al., 2008). 

When data are related realizations of a Poisson process on the same space, we often seek the underlying structure that ties them together. In this paper, we present an unsupervised approach to extract features from instances of point processes for which the intensity surfaces vary from realization to realization, but are constructed from a common library. 

The main contribution of this paper is an unsupervised method that finds a low dimensional representation of related point processes. Focusing on the application of modeling basketball shot selection, we show that a matrix decomposition of Poisson process intensity surfaces can provide an interpretable feature space that parsimoniously describes the data. We examine the individual components of the matrix decomposition, as they provide an interesting quantitative summary of players’ offensive tendencies. These summaries better characterize player types than any traditional categorization (e.g. player position). One application of our method is personnel decisions. Our representation can be used to select sets of players with diverse offensive tendencies. This representation is then leveraged in a latent variable model to visualize a player’s field goal percentage as a function of location on the court. 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 

### **1.1. Related Work** 

Previously, Adams et al. (2010) developed a probabilistic matrix factorization method to predict score outcomes in NBA games. Their method incorporates external covariate information, though they do not model spatial effects or individual players. Goldsberry & Weiss (2012) developed a framework for analyzing the defensive effect of NBA centers on shot frequency and shot efficiency. Their analysis is restricted, however, to a subset of players in a small part of the court near the basket. 

Libraries of spatial or temporal functions with a nonparametric prior have also been used to model neural data. Yu et al. (2009) develop the Gaussian process factor analysis model to discover latent ‘neural trajectories’ in high dimensional neural time-series. Though similar in spirit, our model includes a positivity constraint on the latent functions that fundamentally changes their behavior and interpretation. 

## **2. Background** 

This section reviews the techniques used in our point process modeling method, including Gaussian processes (GPs), Poisson processes (PPs), log-Gaussian Cox processes (LGCPs) and non-negative matrix factorization (NMF). 

### **2.1. Gaussian Processes** 

A Gaussian process is a stochastic process whose sample path, _f_ 1 _, f_ 2 _· · · ∈_ R, is normally distributed. GPs are frequently used as a probabilistic model over functions _f_ : _X →_ R, where the realized value _fn ≡ f_ ( _xn_ ) corresponds to a function evaluation at some point _xn ∈X_ . The spatial covariance between two points in _X_ encode prior beliefs about _f_ ; covariances can encode beliefs about a wide range of properties, including differentiability, smoothness, and periodicity. 

As a concrete example, imagine a smooth function _f_ : R<sup>2</sup> _→_ R for which we have observed a set of locations _x_ 1 _, . . . , xN_ and values _f_ 1 _, . . . , fN_ . We can model this ‘smooth’ property by choosing a covariance function that results in smooth processes. For instance, the squared exponential covariance function 



assumes the function _f_ is infinitely differentiable, with marginal variation _σ_<sup>2</sup> and length-scale _φ_ , which controls the expected number of direction changes the function exhibits. Because this covariance is strictly a function of the distance between two points in the space _X_ , the squared exponential covariance function is said to be stationary. 

We use this smoothness property to encode our inductive bias that shooting habits vary smoothly over the court space. For a more thorough treatment of Gaussian processes, see Rasmussen & Williams (2006). 

### **2.2. Poisson Processes** 

A Poisson process is a completely spatially random point process on some space, _X_ , for which the number of points that end up in some set _A ⊆X_ is Poisson distributed. We will use an inhomogeneous Poisson process on a domain _X_ . That is, we will model the set of spatial points, _x_ 1 _, . . . , xN_ with _xn ∈X_ , as a Poisson process with a non-negative intensity function _λ_ ( _x_ ) : _X →_ R+ (throughout this paper, R+ will indicate the union of the positive reals and zero). This implies that for any set _A ⊆X_ , the number of points that fall in _A_ , _NA_ , will be Poisson distributed, 



Furthermore, a Poisson process is ‘memoryless’, meaning that _NA_ is independent of _NB_ for disjoint subsets _A_ and _B_ . We signify that a set of points **x** _≡{x_ 1 _, . . . , xN }_ follows a Poisson process as 



One useful property of the Poisson process is the superposition theorem (Kingman, 1992), which states that given a countable collection of independent Poisson processes **x** 1 _,_ **x** 2 _, . . ._ , each with measure _λ_ 1 _, λ_ 2 _, . . ._ , their superposition is distributed as 



Furthermore, note that each intensity function _λk_ can be scaled by some non-negative factor and remain a valid intensity function. The positive scalability of intensity functions and the superposition property of Poisson processes motivate the non-negative decomposition (Section 2.4) of a global Poisson process into simpler weighted subprocesses that can be shared between players. 

### **2.3. Log-Gaussian Cox Processes** 

A log-Gaussian Cox process (LGCP) is a doubly-stochastic Poisson process with a spatially varying intensity function modeled as an exponentiated GP 



where doubly-stochastic refers to two levels of randomness: the random function _Z_ ( _·_ ) and the random point process with intensity _λ_ ( _·_ ). 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 

### **2.4. Non-Negative Matrix Factorization** 

Non-negative matrix factorization (NMF) is a dimensionality reduction technique that assumes some matrix **Λ** can be approximated by the product of two low-rank matrices 



where the matrix **Λ** _∈_ R<sup>_N_</sup> +<sup>_×V_</sup> is composed of _N_ data points of length _V_ , the basis matrix **B** _∈_ R<sup>_K_</sup> +<sup>_×V_</sup> is composed of _K_ basis vectors, and the weight matrix **W** _∈_ R<sup>_N_</sup> +<sup>_×K_</sup> is composed of the _N_ non-negative weight vectors that scale and linearly combine the basis vectors to reconstruct **Λ** . Each vector can be reconstructed from the weights and the bases 



The optimal matrices **W**<sup>_∗_</sup> and **B**<sup>_∗_</sup> are determined by an optimization procedure that minimizes _ℓ_ ( _·, ·_ ), a measure of reconstruction error or divergence between **WB** and **Λ** with the constraint that all elements remain non-negative: 



Different metrics will result in different procedures. For arbitrary matrices **X** and **Y** , one option is the squared Frobenius norm, 



Another choice is a matrix divergence metric 



which reduces to the Kullback-Leibler (KL) divergence when interpreting matrices **X** and **Y** as discrete distributions, i.e.,<sup>�</sup> _ij_<sup>_Xij_=�</sup> _ij_<sup>_Yij_=1 (Lee & Seung, 2001).</sup> Note that minimizing the divergence _ℓ_ KL( **X** _,_ **Y** ) as a function of **Y** will yield a different result from optimizing over **X** . 

The two loss functions lead to different properties of **W**<sup>_∗_</sup> and **B**<sup>_∗_</sup> . To understand their inherent differences, note that the KL loss function includes a log ratio term. This tends to disallow large _ratios_ between the original and reconstructed matrices, even in regions of low intensity. In fact, regions of low intensity can contribute more to the loss function than regions of high intensity if the ratio between them is large enough. The log ratio term is absent from the Frobenius loss function, which only disallows large _differences_ . This tends to favor the reconstruction of regions of larger intensity, leading to more basis vectors focused on those regions. 

Due to the positivity constraint, the basis **B**<sup>_∗_</sup> tends to be disjoint, exhibiting a more ‘parts-based’ decomposition than other, less constrained matrix factorization methods, such as PCA. This is due to the restrictive property of the NMF decomposition that disallows negative bases to cancel out positive bases. In practice, this restriction eliminates a large swath of ‘optimal’ factorizations with negative basis/weight pairs, leaving a sparser and often more interpretable basis (Lee & Seung, 1999). 

## **3. Data** 

Our data consist of made and missed field goal attempt locations from roughly half of the games in the 2012-2013 NBA regular season. These data were collected by optical sensors as part of a program to introduce spatio-temporal information to basketball analytics. We remove shooters with fewer than 50 field goal attempts, leaving a total of about 78,000 shots distributed among 335 unique NBA players. 

We model a player’s shooting as a point process on the offensive half court, a 35 ft by 50 ft rectangle. We will index players with _n ∈{_ 1 _, . . . , N }_ , and we will refer to the set of each player’s shot attempts as **x** _n_ = _{xn,_ 1 _, . . . , xn,Mn}_ , where _Mn_ is the number of shots taken by player _n_ , and _xn,m ∈_ [0 _,_ 35] _×_ [0 _,_ 50]. 

When discussing shot outcomes, we will use _yn,m ∈{_ 0 _,_ 1 _}_ to indicate that the _n_ th player’s _m_ th shot was made (1) or missed (0). Some raw data is graphically presented in Figure 1(a). Our goal is to find a parsimonious, yet expressive representation of an NBA basketball player’s shooting habits. 

### **3.1. A Note on Non-Stationarity** 

As an exploratory data analysis step, we visualize the empirical spatial correlation of shot counts in a discretized space. We discretize the court into _V_ tiles, and compute **X** such that **X** _n,v_ = _|{xn,i_ : _xn,i ∈ v}|_ , the number of shots by player _n_ in tile _v_ . The empirical correlation, depicted with respect to a few tiles in Figure 2, provides some intuition about the non-stationarity of the underlying intensity surfaces. Long range correlations exist in clearly non-stationary patterns, and this inductive bias is not captured by a stationary LGCP that merely assumes a locally smooth surface. This motivates the use of an additional method, such as NMF, to introduce global spatial patterns that attempt to learn this long range correlation. 

## **4. Proposed Approach** 

Our method ties together the two ideas, LGCPs and NMF, to extract spatial patterns from NBA shooting data. 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 



<!-- Start of picture text -->
Stephen Curry (940 shots) LeBron James (315 shots)<br>GGGGGGGGGGGGG G GGG G GG G GGGGGG GGG GGGGGGGG G GGGGGGG G GGGGGG GG GGGGG GG GG G GGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGG G GGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGG G GGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGG G G G GG G GGGGGGGGGGGGG G GGGGGGGGGGGGGGGGG GGGGGGG G G GG G GGG G GGG G GG G G GG GGGGGG G GGG G GGGGGGGGGGGGGGGGG G GGGGGGG GG GG G GGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G<br>(a) points<br><!-- End of picture text -->



<!-- Start of picture text -->
Emp. cor. at (21, 44) Emp. cor. at ( 7, 28)<br>1.0 1.0<br>G<br>0.8 0.8<br>0.6 0.6<br>G<br>G 0.4 G 0.4<br>0.2 0.2<br>0.0 0.0<br><!-- End of picture text -->

_Figure 2._ Empirical spatial correlation in raw count data at two marked court locations. These data exhibit non-stationary correlation patterns, particularly among three point shooters. This suggests a modeling mechanism to handle the global correlation. 



<!-- Start of picture text -->
Stephen Curry shot grid LeBron James shot grid<br>10<br>10<br>8<br>8<br>6<br>G G 6<br>4 4<br>2 2<br>0 0<br>(b) grid<br>Stephen Curry LGCP LeBron James LGCP<br>5<br>4<br>4<br>3 3<br>G G<br>2 2<br>1 1<br><!-- End of picture text -->

   - _λ_ ¯ _n_ has been normalized s.t.<sup>�</sup> _λ_ ¯ _n_ = 1 

4. Find **B** _,_ **W** for some _K_ such that **WB** _≈_ **Λ** , constraining all matrices to be non-negative (NMF). 

This results in a spatial basis **B** and basis loadings for each individual player, **w** _n_ . Due to the superposition property of Poisson processes and the non-negativity of the basis and loadings, the basis vectors can be interpreted as subintensity functions, or archetypal intensities used to construct each individual player. The linear weights for each player concisely summarize the spatial shooting habits of a player into a vector in R<sup>_K_</sup> +<sup>.</sup> 



<!-- Start of picture text -->
(c) LGCP<br>Stephen Curry LGCP−NMF LeBron James LGCP−NMF<br>4 4<br>3 3<br>G G<br>2 2<br>1 1<br>(d) LGCP-NMF<br><!-- End of picture text -->

Though we have described a continuous model for conceptual simplicity, we discretize the court into _V_ one-squarefoot tiles to gain computational tractability in fitting the LGCP surfaces. We expect this tile size to capture all interesting spatial variation. Furthermore, the discretization maps each player into R<sup>_V_</sup> +<sup>,providingthenecessaryinput</sup> for NMF dimensionality reduction. 

### **4.1. Fitting the LGCPs** 

For each player’s set of points, **x** _n_ , the likelihood of the point process is discretely approximated as 

_Figure 1._ NBA player representations: (a) original point process data from two players, (b) discretized counts, (c) LGCP surfaces, and (d) NMF reconstructed surfaces ( _K_ = 10). Made and missed shots are represented as blue circles and red _×_ ’s, respectively. Some players have more data than others because only half of the stadiums had the tracking system in 2012-2013. 



where, overloading notation, _λn_ ( _·_ ) is the exact intensity function, _λn_ is the discretized intensity function (vector), and ∆ _A_ is the area of each tile (implicitly one from now on). This approximation comes from the completely spatially random property of the Poisson process, allowing us to treat each tile independently. The probability of the count present in each tile is Poisson, with uniform intensity _λn,v_ . 

Given point process realizations for each of _N_ players, **x** 1 _, . . . ,_ **x** _N_ , our procedure is 

1. Construct the count matrix **X** _n,v_ = # shots by player _n_ in tile _v_ on a discretized court. 

2. Fit an intensity surface _λn_ = ( _λn,_ 1 _, . . . , λn,V_ )<sup>_T_</sup> for each player _n_ over the discretized court (LGCP). 

3. Construct the data matrix **Λ** = ( _λ_<sup>¯</sup> 1 _, . . . , λ_<sup>¯</sup> _N_ )<sup>_T_</sup> , where 

Explicitly representing the Gaussian random field **z** _n_ , the 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 



<!-- Start of picture text -->
● ●<br>(a) Corner threes (b) Wing threes<br>● ●<br>(c) Top of key threes (d) Long two-pointers<br><!-- End of picture text -->

_Figure 3._ A sample of basis vectors (surfaces) discovered by LGCP-NMF for _K_ = 10. Each basis surface is the normalized intensity function of a particular shot type, and players’ shooting habits are a weighted combination of these shot types. Conditioned on certain shot type (e.g. corner three), the intensity function acts as a density over shot locations, where red indicates likely locations. 

posterior is 





where the prior over **z** _n_ is a mean zero normal with covariance **K** _v,u_ = _k_ ( _xv, xu_ ), determined by Equation 1, and _z_ 0 is a bias term that parameterizes the mean rate of the Poisson process. Samples of the posterior _p_ ( _λn|_ **x** _n_ ) can be constructed by transforming samples of **z** _n|_ **x** _n_ . To overcome the high correlation induced by the court’s spatial structure, we employ elliptical slice sampling (Murray et al., 2010) to approximate the posterior of _λn_ for each player, and subsequently store the posterior mean. 

### **4.3. Alternative Approaches** 

With the goal of discovering the shared structure among the collection of point processes, we can proceed in a few alternative directions. For instance, one could hand-select a spatial basis and directly fit weights for each individual point process, modeling the intensity as a weighted combination of these bases. However, this leads to multiple restrictions: firstly, choosing the spatial bases to cover the court is a highly subjective task (though, there are situations where it would be desirable to have such control); secondly, these bases are unlikely to match the natural symmetries of the basketball court. In contrast, modeling the intensities with LGCP-NMF uncovers the natural symmetries of the game without user guidance. 

Another approach would be to directly factorize the raw shot count matrix **X** . However, this method ignores spatial information, and essentially models the intensity surface as a set of _V_ independent parameters. Empirically, this method yields a poorer, more degenerate basis, which can be seen in Figure 4(c). Furthermore, this is far less numerically stable, and jitter must be added to entries of **Λ** for convergence. Finally, another reasonable approach would apply PCA directly to the discretized LGCP intensity matrix **Λ** , though as Figure 4(d) demonstrates, the resulting mixed-sign decomposition leads to an unintuitive and visually uninterpretable basis. 

## **5. Results** 

We graphically depict our point process data, LGCP representation, and LGCP-NMF reconstruction in Figure 1 for _K_ = 10. There is wide variation in shot selection among NBA players - some shooters specialize in certain types of shots, whereas others will shoot from many locations on the court. 

Our method discovers basis vectors that correspond to visually interpretable shot types. Similar to the parts-based decomposition of human faces that NMF discovers in Lee & Seung (1999), LGCP-NMF discovers a shots-based decomposition of NBA players. 

Setting _K_ = 10 and using the KL-based loss function, we display the resulting basis vectors in Figure 3. One basis corresponds to corner three-point shots 3(a), while another corresponds to wing three-point shots 3(b), and yet another to top of the key three point shots 3(c). A comparison between KL and Frobenius loss functions can be found in Figure 4. 

### **4.2. NMF Optimization** 

We now solve the optimization problem using techniques from Lee & Seung (2001) and Brunet et al. (2004), comparing the KL and Frobenius loss functions to highlight the difference between the resulting basis vectors. 

Furthermore, the player specific basis weights provide a concise characterization of their offensive habits. The weight _wn,k_ can be interpreted as the amount player _n_ takes shot type _k_ , which quantifies intuitions about player behav- 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 

||G|G|G|G|G|G|G|G|G|G|
|---|---|---|---|---|---|---|---|---|---|---|
|LeBron James|0.21|0.16|0.12|0.09|0.04|0.07|0.00|0.07|0.08|0.17|
|Brook Lopez|0.06|0.27|0.43|0.09|0.01|0.03|0.08|0.03|0.00|0.01|
|Tyson Chandler|0.26|0.65|0.03|0.00|0.01|0.02|0.01|0.01|0.02|0.01|
|Marc Gasol|0.19|0.02|0.17|0.01|0.33|0.25|0.00|0.01|0.00|0.03|
|Tony Parker|0.12|0.22|0.17|0.07|0.21|0.07|0.08|0.06|0.00|0.00|
|Kyrie Irving|0.13|0.10|0.09|0.13|0.16|0.02|0.13|0.00|0.10|0.14|
|Stephen Curry|0.08|0.03|0.07|0.01|0.10|0.08|0.22|0.05|0.10|0.24|
|James Harden|0.34|0.00|0.11|0.00|0.03|0.02|0.13|0.00|0.11|0.26|
|Steve Novak|0.00|0.01|0.00|0.02|0.00|0.00|0.01|0.27|0.35|0.34|



_Table 1._ Normalized player weights for each basis. The first three columns correspond to close-range shots, the next four correspond to mid-range shots, while the last three correspond to three-point shots. Larger values are highlighted, revealing the general ‘type’ of shooter each player is. The weights themselves match intuition about players shooting habits (e.g. three-point specialist or mid-range shooter), while more exactly quantifying them. 



<!-- Start of picture text -->
G G G G G G G G G G<br>(a) LGCP-NMF (KL)<br>G G G G G G G G G G<br>(b) LGCP-NMF (Frobenius)<br>G G G G G G G G G G<br>(c) Direct NMF (KL)<br>G G G G G G G G G G<br>(d) LGCP-PCA<br><!-- End of picture text -->

_Figure 4._ Visual comparison of the basis resulting from various approaches to dimensionality reduction. The top two bases result from LGCP-NMF with the KL (top) and Frobenius (second) loss functions. The third row is the NMF basis applied to raw counts (no spatial continuity). The bottom row is the result of PCA applied to the LGCP intensity functions. LGCP-PCA fundamentally differs due to the negativity of the basis surfaces. Best viewed in color. 

ior. Table 1 compares normalized weights between a selection of players. 

Empirically, the KL-based NMF decomposition results in a more spatially diverse basis, where the Frobenius-based decomposition focuses on the region of high intensity near the basket at the expense of the rest of the court. This can be 

seen by comparing Figure 4(a) (KL) to Figure 4(b) (Frobenius). 

We also compare the two LGCP-NMF decompositions to the NMF decomposition done directly on the matrix of counts, **X** . The results in Figure 4(c) show a set of sparse basis vectors that are spatially unstructured. And lastly, we 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 



<!-- Start of picture text -->
Predictive Likelihood (10−fold cv)<br>K=1 K=3 K=5 K=10 K=15 K=20 LGCP<br>Model<br>−6.10<br>−6.20<br>log likelihood<br>−6.30<br><!-- End of picture text -->

_Figure 5._ Average player test data log likelihoods for LGCPNMF varying _K_ and independent LGCP. For each fold, we held out 10% of each player’s shots, fit independent LGCPs and ran NMF (using the KL-based loss function) for varying _K_ . The predictive performance of our representation improves upon the high dimensional independent LGCPs, showing the importance of pooling information across players. 

depict the PCA decomposition of the LGCP matrix **Λ** in Figure 4(d). This yields the most colorful decomposition because the basis vectors and player weights are unconstrained real numbers. This renders the basis vectors uninterpretable as intensity functions. Upon visual inspection, the corner three-point ‘feature’ that is salient in the LGCPNMF decompositions appears in five separate PCA vectors, some positive, some negative. This is the cancelation phenomenon that NMF avoids. 

We compare the fit of the low rank NMF reconstructions and the original LGCPs on held out test data in Figure 5. The NMF decomposition achieves superior predictive performance over the original independent LGCPs in addition to its compressed representation and interpretable basis. 

## **6. From Shooting Frequency to Efficiency** 

Unadjusted field goal percentage, or the probability a player makes an attempted shot, is a statistic of interest when evaluating player value. This statistic, however, is spatially uninformed, and washes away important variation due to shooting circumstances. 

Leveraging the vocabulary of shot types provided by the basis vectors, we model a player’s field goal percentage for each of the shot types. We decompose a player’s field goal percentage into a weighted combination of _K_ basis field goal percentages, which provides a higher resolution summary of an offensive player’s skills. Our aim is to estimate the probability of a made shot for each point in the offensive half court _for each individual player_ . 

### **6.1. Latent variable model** 

For player _n_ , we model each shot event as 

_kn,i ∼_ Mult( ¯ _wn,_ :) shot type _xn,i|kn,i ∼_ Mult( _B_<sup>¯</sup> _kn,i_ ) location _yn,i|kn,i ∼_ Bern(logit<sup>_−_1</sup> ( _βn,kn,i_ )) outcome 

where _B_<sup>¯</sup> _k ≡ Bk/_<sup>�</sup> _k_<sup>_′ Bk′_is the normalized basis, and the</sup> player weights _w_ ¯ _n,k_ are adjusted to reflect the total mass of each unnormalized basis. NMF does not constrain each basis vector to a certain value, so the volume of each basis vector is a meaningful quantity that corresponds to how common a shot type is. We transfer this information into the weights by setting 



We do not directly observe the shot type, _k_ , only the shot location _xn,i_ . Omitting _n_ and _i_ to simplify notation, we can compute the the predictive distribution 



where the outcome distribution is red and the location distribution is blue for clarity. 

The shot type decomposition given by **B** provides a natural way to share information between shooters to reduce the variance in our estimated surfaces. We hierarchically model player probability parameters _βn,k_ with respect to each shot type. The prior over parameters is 



where the global means, _β_ 0 _,k_ , and variances, _σk_<sup>2, are given</sup> diffuse priors, _σ_ 0<sup>2=100, and</sup><sup>_a_=</sup><sup>_b_=</sup><sup>_._1.The goal of this</sup> hierarchical prior structure is to share information between players about a particular shot type. Furthermore, it will shrink players with low sample sizes to the global mean. Some consequences of these modeling decisions will be discussed in Section 7. 

### **6.2. Inference** 

Gibbs sampling is performed to draw posterior samples of the _β_ and _σ_<sup>2</sup> parameters. To draw posterior samples of _β|σ_<sup>2</sup> _, y_ , we use elliptical slice sampling to exploit the normal prior placed on _β_ . We can draw samples of _σ_<sup>2</sup> _|β, y_ directly due to conjugacy. 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 



<!-- Start of picture text -->
Posterior Mean Court Posterior Mean uncertainty<br>1.0<br>0.035<br>0.8 0.030<br>0.025<br>0.6<br>G G 0.020<br>0.4 0.015<br>0.010<br>0.2<br>0.005<br>0.0 0.000<br>(a) global mean (b) posterior variance<br>LeBron James Posterior Court Steve Novak Posterior Court<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>G G<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>(c) (d)<br>Kyrie Irving Posterior Court Stephen Curry Posterior Court<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>G G<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>(e) (f)<br><!-- End of picture text -->

vides an accurate low dimensional summary of shooting habits and an intuitive basis that corresponds to shot types recognizable by basketball fans and coaches. After visualizing this basis and discussing some of its properties as a quantification of player habits, we then used the decomposition to form interpretable estimates of a spatially shooting efficiency. 

We see a few directions for future work. Due to the relationship between KL-based NMF and some fully generative latent variable models, including the probabilistic latent semantic model (Ding et al., 2008) and latent Dirichlet allocation (Blei et al., 2003), we are interested in jointly modeling the point process and intensity surface decomposition in a fully generative model. This spatially informed LDA would model the non-stationary spatial structure the data exhibit within each non-negative basis surface, opening the door for a richer parameterization of offensive shooting habits that could include defensive effects. 

Furthermore, jointly modeling spatial field goal percentage and intensity can capture the correlation between player skill and shooting habits. Common intuition that players will take more shots from locations where they have more accuracy is missed in our treatment, yet modeling this effect may yield a more accurate characterization of a player’s habits and ability. 

We also see potential spatio-temporal extensions of our model. For instance, the per-game occurrence of shots over the course of a season or the daily occurrence of crimes within a city can be viewed as a spatio-temporal point process. We can extend the LGCP-NMF framework by introducing temporal correlation in the weights of the NMF decomposition. This may decouple spatial patterns from temporal patterns in the data, revealing interesting structure and offering a reduced representation. 

_Figure 6._ (a) Global efficiency surface and (b) posterior uncertainty. (c-f) Spatial efficiency for a selection of players. Red indicates the highest field goal percentage and dark blue represents the lowest. Novak and Curry are known for their 3-point shooting, whereas James and Irving are known for efficiency near the basket. 

### **6.3. Results** 

We visualize the global mean field goal percentage surface, corresponding parameters to _β_ 0 _,k_ in Figure 6(a). Beside it, we show one standard deviation of posterior uncertainty in the mean surface. Below the global mean, we show a few examples of individual player field goal percentage surfaces. These visualizations allow us to compare players’ efficiency with respect to regions of the court. For instance, our fit suggests that both Kyrie Irving and Steve Novak are below average from basis 4, the baseline jump shot, whereas Stephen Curry is an above average corner three point shooter, valuable information for a defending player. More details are available in the supplemental material. 

## **Acknowledgments** 

The authors would like to acknowledge the Harvard XY Hoops group - Alex Franks, Alex D’Amour, Ryan Grossman, and Dan Cervone - as well as the HIPS lab and several referees for helpful suggestions and discussion. We thank STATS LLC for providing the data. To compare various NMF optimization procedures, the authors used the r package NMF (Gaujoux & Seoighe, 2010). 

## **References** 

Adams, Ryan P., Murray, Iain, and MacKay, David J.C. Tractable nonparametric Bayesian inference in Poisson processes with Gaussian process intensities. In _Proceedings of the 26th International Conference on Machine Learning (ICML)_ , Montreal, Canada, 2009. 

## **7. Discussion** 

We have presented a method that models related point processes using a constrained matrix decomposition of independently fit intensity surfaces. Our representation pro- 

**Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball** 

- Adams, Ryan P., Dahl, George E., and Murray, Iain. Incorporating side information into probabilistic matrix factorization using Gaussian processes. In _Proceedings of the 26th Conference on Uncertainty in Artificial Intelligence (UAI)_ , 2010. 

- Benes, Viktor, Bodl´ak, Karel, and Wagepetersens, Jesper Møller Rasmus Plenge. Bayesian analysis of log Gaussian Cox processes for disease mapping. Technical report, Aalborg University, 2002. 

- Blei, David M., Ng, Andrew Y., and Jordan, Michael I. Latent Dirichlet allocation. _The Journal of Machine Learning Research_ , 3:993–1022, 2003. 

- Brunet, Jean-Philippe, Tamayo, Pablo, Golub, Todd R, and Mesirov, Jill P. Metagenes and molecular pattern discovery using matrix factorization. _Proceedings of the National Academy of Sciences of the United States of America_ , 101.12:4164–9, 2004. 

   - Møller, Jesper, Syversveen, Anne Randi, and Waagepetersen, Rasmus Plenge. Log Gaussian Cox processes. _Scandinavian Journal of Statistics_ , 25 (3):451–482, 1998. 

   - Murray, Iain, Adams, Ryan P., and MacKay, David J.C. Elliptical slice sampling. _Journal of Machine Learning Research: Workshop and Conference Proceedings (AISTATS)_ , 9:541–548, 2010. 

   - Rasmussen, Carl Edward and Williams, Christopher K.I. _Gaussian Processes for Machine Learning_ . The MIT Press, Cambridge, Massachusetts, 2006. 

   - Yu, Byron M., John P. Cunningham, Gopal Santhanam, Ryu, Stephen I., and Shenoy, Krishna V. Gaussianprocess factor analysis for low-dimensional single-trial analysis of neural population activity. _Advances in Neural Information Processing Systems (NIPS)_ , 2009. 

- Cox, D. R. Some statistical methods connected with series of events. _Journal of the Royal Statistical Society. Series B_ , 17(2):129–164, 1955. 

- Cunningham, John P, Yu, Byron M, Shenoy, Krishna V, and Sahani, Maneesh. Inferring neural firing rates from spike trains using Gaussian processes. _Advances in Neural Information Processing Systems (NIPS)_ , 2008. 

- Diggle, Peter. _Statistical Analysis of Spatial and SpatioTemporal Point Patterns_ . CRC Press, 2013. 

- Ding, Chris, Li, Tao, and Peng, Wei. On the equivalence between non-negative matrix factorization and probabilistic latent semantic indexing. _Computational Statistics & Data Analysis_ , 52:3913–3927, 2008. 

- Gaujoux, Renaud and Seoighe, Cathal. A flexible r package for nonnegative matrix factorization. _BMC Bioinformatics_ , 11(1):367, 2010. ISSN 1471-2105. doi: 10.1186/1471-2105-11-367. 

- Goldsberry, Kirk and Weiss, Eric. The Dwight effect: A new ensemble of interior defense analytics for the nba. In _Sloan Sports Analytics Conference_ , 2012. 

- Kingman, John Frank Charles. _Poisson Processes_ . Oxford university press, 1992. 

- Lee, Daniel D. and Seung, H. Sebastian. Learning the parts of objects by non-negative matrix factorization. _Nature_ , 401(6755):788–791, 1999. 

- Lee, Daniel D. and Seung, H. Sebastian. Algorithms for non-negative matrix factorization. _Advances in Neural Information Processing Systems (NIPS)_ , 13:556–562, 2001. 


