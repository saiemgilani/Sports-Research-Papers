<!-- source: Measuring Spatial Allocative Efficiency in Basketball.pdf -->

# Measuring Spatial Allocative Efficiency in Basketball 

### Nathan Sandholtz, Jacob Mortensen, and Luke Bornn 

Simon Fraser University 

August 4, 2020 

##### **Abstract** 

Every shot in basketball has an opportunity cost; one player’s shot eliminates all potential opportunities from their teammates for that play. For this reason, player-shot efficiency should ultimately be considered relative to the lineup. This aspect of efficiency—the optimal way to allocate shots within a lineup—is the focus of our paper. Allocative efficiency should be considered in a spatial context since the distribution of shot attempts within a lineup is highly dependent on court location. We propose a new metric for spatial allocative efficiency by comparing a player’s field goal percentage (FG%) to their field goal attempt (FGA) rate in context of both their four teammates on the court and the spatial distribution of their shots. Leveraging publicly available data provided by the National Basketball Association (NBA), we estimate player FG% at every location in the offensive half court using a Bayesian hierarchical model. Then, by ordering a lineup’s estimated FG%s and pairing these rankings with the lineup’s empirical FGA rate rankings, we detect areas where the lineup exhibits inefficient shot allocation. Lastly, we analyze the impact that sub-optimal shot allocation has on a team’s overall offensive potential, demonstrating that inefficient shot allocation correlates with reduced scoring. 

**Keywords:** Bayesian hierarchical model, spatial data, ranking, ordering, basketball 

_*The first and second authors contributed equally to this work._ 

## **1 Introduction** 

From 2017 to 2019, the Oklahoma City Thunder faced four elimination games across three playoff series. In each of these games, Russell Westbrook attempted over 30 shots and had an average usage rate of 45.5%.<sup>1</sup> The game in which Westbrook took the most shots came in the first round of the 2017-18 National Basketball Association (NBA) playoffs, where he scored 46 points on 43 shot attempts in a 96-91 loss to the Utah Jazz. At the time, many popular media figures conjectured that having one player dominate field goal attempts in this way would limit the Thunder’s success. While scoring 46 points in a playoff basketball game is an impressive feat for any one player, its impact on the overall game score is moderated by the fact that it required 43 attempts. Perhaps 

> 1Usage percentage is an estimate of the percentage of team plays used by a player while they were on the floor. For a detailed formula see `www.basketball-reference.com/about/glossary.html` 

1 

not coincidentally, the Thunder lost three of these four close-out games and never managed to make it out of the first round of the playoffs. 

At its core, this critique is about shot efficiency. The term ‘shot efficiency’ is used in various contexts within the basketball analytics community, but in most cases it has some reference to the average number of points a team or player scores per shot attempt. Modern discussion around shot efficiency in the NBA typically focuses on either shot selection or individual player efficiency. The concept of shot selection efficiency is simple: 3-pointers and shots near the rim have the highest expected points per shot, so teams should prioritize these high-value shots. The idea underlying individual player efficiency is also straightforward; scoring more points on the same number of shot attempts increases a team’s overall offensive potential. 

However, when discussing a player’s individual efficiency it is critical to do so in context of the lineup. Basketball is not a 1-v-1 game, but a 5-v-5 game. Therefore, when a player takes a shot, the opportunity cost not only includes all other shots this player could have taken later in the possession, but also the potential shots of their four teammates. So regardless of a player’s shooting statistics relative to the league at large, a certain dimension of shot efficiency can only be defined relative to the abilities of a player’s teammates. Applying this to the Oklahoma City Thunder example above, if Westbrook were surrounded by dismal shooters, 43 shot attempts might not only be defensible but also desirable. On the other hand, if his inordinate number of attempts prevented highly efficient shot opportunities from his teammates, then he caused shots to be inefficiently distributed and decreased his team’s scoring potential. This aspect of efficiency—the optimal way to allocate shots within a lineup—is the primary focus of our paper. 

Allocative efficiency is spatially dependent. As illustrated in Figure 1, the distribution of shots within a lineup is highly dependent on court location. The left plot in Figure 1 shows the overall relationship between shooting frequency (x-axis) and shooting skill (y-axis), while the four plots on the right show the same relationship conditioned on various court regions. Each dot represents a player, and the size of the dot is proportional to the number of shots the player took over the 201617 NBA regular season. To emphasize how shot allocation within lineups is spatially dependent, we have highlighted the Cleveland Cavaliers starting lineup, consisting of LeBron James, Kevin Love, Kyrie Irving, JR Smith, and Tristan Thompson. 

2 



<!-- Start of picture text -->
Overall Field Goal Attempt (FGA) Rate by Points Per Shot (PPS) Restricted Area: FGA Rate by PPS 3−pointers: FGA Rate by PPS<br>1.41.21.00.8 GGGG Thompson GGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GG GGGGGGGG G GGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G G Smith GGGGGGGGGGGGGGGGGG G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGG G G G GGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGG Love GGGGGGGGGGGGGG G GGG G GGGGGGGG G GGGGGGG James GGGGGGGGGGGGGGGGGGGGG Irving G G G G 1.51.00.51.51.00.5 Paint: FGA Rate by PPS0.0Field Goal Attempt Rate (per 36 minutes)SmithSmith GGGGGGGGGGGGG G GGG G GGGGG G GGGGGGGG G GGGGGG G GGGGGGGG G GGGGGGG G GGGG G GGGGGGG G GGGGGGGGG G GGGGGGGGGG G GGGG G GGGGGGG G G GGGGG G GGG G GGGGGGGGG G GG G GGGGG G GGGGG G GGGGGGGGGGGGGGGGGGG G G G GG G GGGGGGG G GGGGGGGGGGGG G G GGGGGGGG G GGG G GGGGGGGGGGGG G GGG G GGGGG G GGGG G GGGGGGGGGG G GG G GGGGGGGGGGGGGGGG G GGG G GGGGGG Thompson G G G G G GGG G GGG G GGG G GGGGG G GGGGG G G G GGG G G G GGGGG G GG G GGGGGGGGG Love G G G GG G G Love G Thompson G G G G GG G GGGGG G GGGGGGG G G G GGG G 2.5 GGGGGGGGGGGGGGGG G G G GGGG G GGG G GGGGGGGGGGGGGGG G GG G GGG G GGGGGGG G GGGGGG G GGGGGGG G GGGGGGG G G GG G G GGGG G GG G GGGGGG G GGGGGGGGGGG G G G G G G GG G GGGG G G G G G GGGGGGGG G GGGGGGGGGG G GGG GG GGGGG GG G G GGGGGGGGGGGGG G G G G GGGGG G GGGGG G GGGGGGGGGGGGGGGGGGG G GG G GGGGGGGGGGG G Irving G G G Irving GGGG G GG G GGGGGG G GGGGGGG G G GG G GGGGGGGGGGG G GGG 5.0 GGGGGGGG G GGG G GGGGG G G G G GGGGGGGGGGGGGG JamesJames GGGGGGG G G G GGGG G GGGGGGG 7.5 GG 10.0 1.51.00.51.51.00.5 Mid−range: FGA Rate by PPS0.0Field Goal Attempt Rate (per 36 minutes)Thompson GGGG G GGGGGGGGGG Smith GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GG G GGG G GGGGGGGGGGGGGGGG G GGGG G GGG G G G GGGGGGGGGGGGGGGGGGGGGGGGGGG G GG G GGGGG G GGGGGG G G G GG G 2.5 G G GGGGGGGGGGGGGGGGGG G GGGGGGG GG GG G G G GGGGGGGGGGGGGG James GGGGGGGGG G G Love GGG GG GGGGGGG G GGGGGGGGGGGGGGGG G GGGG GG GGG G G G GG GG GGG G GGGGGGGGG G GGGGGG G GG G GGGGG G GGGGGGGG G G G GG G GGGG G G G GGGGGG G GGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGG G GGGGG G G G GGGGGGGGGGGG G GGGGGGGGGGG G GG G GGGGGGGGG G G G GGGGGGGGGGG G GGGGGGGGGGGGGGGGGGG G G G G G GGGGGGG James G GG G GGG G GGGGGGG G 5.0 GG G G GGGGGGGG Irving GGGGGGGGGGGGGGGGGG G G G G G GGGGGGGGGGGGGGGG G GGGG G GGGGGGGGGGGGG G GGGGG G GGGGGGGGGGGGGGGG G GGGGGGGG G GGGGGGGGGGGGGG GG GGGGGGGGGGGGGGGGGGGGGGG GG G Irving G G Love GGGG G G GGG 7.5 GGGGGGGGGGGG G GGGGGGGG G GGGGG Smith GGGGGG 10.0 G<br>5 10 15 20 25 0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0<br>Field Goal Attempt Rate (per 36 minutes) Field Goal Attempt Rate (per 36 minutes) Field Goal Attempt Rate (per 36 minutes)<br>Figure 1: Left: overall relationship between field goal attempt rate (x-axis) and points per shot (y-axis).<br>Right: same relationship conditioned on various court regions. The Cleveland Cavaliers 2016-17 starting<br>lineup is highlighted in each plot. The weighted least squares fit of each scatter plot is overlaid in each plot<br>by a dotted line.<br>When viewing field goal attempts without respect to court location (left plot), Kyrie Irving<br>appears to shoot more frequently than both Tristan Thompson and LeBron James, despite scoring<br>fewer points per shot than either of them. However, after conditioning on court region (right plots),<br>we see that Irving only has the highest FGA rate in the mid-range region, which is the region for<br>which he has the highest PPS for this lineup. James takes the most shots in the restricted area and<br>paint regions—regions in which he is the most efficient scorer. Furthermore, we see that Thompson’s<br>high overall PPS is driven primarily by his scoring efficiency from the restricted area and that he<br>has few shot attempts outside this area. Clearly, understanding how to efficiently distribute shots<br>within a lineup must be contextualized by spatial information.<br>Notice that in the left panel of Figure 1, the relationship between field goal attempt (FGA)<br>rate and points per shot (PPS) appears to be slightly negative, if there exists a relationship at all.<br>Once the relationship between FGA rate and PPS is spatially disaggregated (see right hand plots<br>of Figure 1), the previously negative relationship between these variables becomes positive in every<br>region. This instance of Simpson’s paradox has non-trivial implications in the context of allocative<br>efficiency which we will discuss in the following section.<br>The goal of our project is to create a framework to assess the strength of the relationship between<br>shooting frequency and shooting skill spatially within lineups and to quantify the consequential<br>impact on offensive production. Using novel metrics we develop, we quantify how many points are<br>being lost through inefficient spatial lineup shot allocation, visualize where they are being lost, and<br>identify which players are responsible.<br>Points per Shot Points per Shot<br>Points per Shot<br>Points per Shot Points per Shot<br><!-- End of picture text -->

3 

### **1.1 Related Work** 

In recent years, a number of metrics have been developed which aim to measure shot efficiency, such as true shooting percentage (Kubatko et al. 2007), qSQ, and qSI (Chang et al. 2014). Additionally, metrics have been developed to quantify individual player efficiency, such as Hollinger’s player efficiency rating (Sports Reference LLC n.d.). While these metrics intrinsically account for team context, there have been relatively few studies which have looked at shooting decisions explicitly in context of lineup, and none spatially. 

Goldman & Rao (2011) coined the term ‘allocative efficiency’, modeling the decision to shoot as a dynamic mixed-strategy equilibrium weighing both the continuation value of a possession and the value of a teammate’s potential shot. They propose that a team achieves optimal allocative efficiency when, at any given time, the lineup cannot reallocate the ball to increase productivity on the margin. Essentially, they argue that lineups optimize over all dimensions of an offensive strategy to achieve equal marginal efficiency for every shot. The left plot of Figure 1 is harmonious with this theory—there appears to be no relationship between player shooting frequency and player shooting skill when viewed on the aggregate. However, one of the most important dimensions the players optimize over is court location. Once we disaggregate the data by court location, (as shown in the right plots of Figure 1), we see a clear relationship between shooting frequency and shooting skill. A unique contribution of our work is a framework to assess this spatial component of allocative efficiency. 

Shot satisfaction (Cervone et al. 2016) is another rare example of a shot efficiency metric that considers lineups. Shot satisfaction is defined as the expected value of a possession conditional on a shot attempt (accounting for various contextual features such as the shot location, shooter, and defensive pressure at the time of the shot) minus the unconditional expected value of the play. However, since shot satisfaction is marginalized over the allocative and spatial components, these factors cannot be analyzed using this metric alone. Additionally, shot satisfaction is dependent on proprietary data which limits its availability to a broad audience. 

### **1.2 Data and Code** 

The data used for this project is publicly available from the NBA stats API (stats.nba.com). Shooter information and shot ( _x, y_ ) locations are available through the shotchartdetail’ API endpoint, while lineup information can be constructed from the playbyplayv2’ endpoint. Code for constructing lineup information from play-by-play data is available at: `https://github.com/jwmortensen/ pbp2lineup` . Using this code, we gathered a set of 224,567 shots taken by 433 players during the 2016-17 NBA regular season, which is the data used in this analysis. Code used to perform an empirical version of the analysis presented in this paper is also available online: `https://github. com/nsandholtz/lpl` . 

4 

## **2 Models** 

The foundation of our proposed allocative efficiency metrics rest on spatial estimates of both player FG% and field goal attempt (FGA) rates. With some minor adjustments, we implement the FG% model proposed in Cervone et al. (2016). As this model is the backbone of the metrics we propose in Section 3, we thoroughly detail the components of their model in Section 2.1. In Section 2.2, we present our model for estimating spatial FGA rates. 

### **2.1 Estimating FG% Surfaces** 

Player FG% is a highly irregular latent quantity over the court space. In general, players make more shots the closer they are to the hoop, but some players are more skilled from a certain side of the court and others specialize from very specific areas, such as the corner 3-pointer. In order to capture these kinds of non-linear relationships, Cervone et al. (2016) summarizes the spatial variation in player shooting skill by a Gaussian process represented by a low-dimensional set of deterministic basis functions. Player-specific weights are estimated for the basis functions using a Bayesian hierarchical model (Gelman et al. 2013). This allows the model to capture nuanced spatial features that player FG% surfaces tend to exhibit, while maintaining a feasible dimensionality for computation. 

We model the logit of _πj_ ( **s** ), the probability that player _j_ makes a shot at location **s** , as a linear model: 



Here **_β_** is a 4 _×_ 1 vector of covariate effects and **x** is a 4 _×_ 1 vector of observed covariates for the shot containing an intercept, player position, shot distance, and the interaction of player position and shot distance. _Zj_ ( **s** ) is a Gaussian process which accounts for the impact of location on the probability of player _j_ making a shot and is modeled using a functional basis representation, 



where **w** _j_ = (w _j_ 1 _, . . . ,_ w _jD_ )<sup>_′_</sup> denotes the latent basis function weights for player _j_ and **ΛΨ** ( **s** ) denotes the basis functions. Specifically, **Λ** = ( **_λ_**<sup>_′_</sup> 1<sup>_, . . . ,_</sup><sup>**_λ_**</sup><sup>_′_</sup> _D_<sup>)</sup><sup>_′_isa</sup><sup>_D × K_matrix,whereeachrowvector</sup><sup>**_λ_**</sup><sup>_d_</sup> represents the projection of the _d_ th basis function onto a triangular mesh with _K_ vertices over the offensive half court (more details on the construction of **Λ** follow below). We use the mesh proposed in Cervone et al. (2016), which was selected specifically for modeling offensive spatial behaviour in basketball. **Ψ** ( **s** ) = ( _ψ_ 1( **s** ) _, . . . , ψK_ ( **s** ))<sup>_′_</sup> is itself a vector of basis functions where each _ψk_ ( **s** ) is 1 at mesh vertex _k_ , 0 at all other vertices, and values at the interior points of each triangle are determined by linear interpolation between vertices (see Lindgren et al. (2011) for details). Finally, we assume **w** _j ∼N_ ( **_ω_** _j,_ **Σ** _j_ ), which makes (2) a Gaussian process with mean **_ω_**<sup>_′_</sup> _j_<sup>**ΛΨ**(</sup><sup>**s**)and</sup> covariance function Cov( **s** 1 _,_ **s** 2) = **Ψ** ( **s** 1)<sup>_′_</sup> **Λ**<sup>_′_</sup> **Σ** _j_ **ΛΨ** ( **s** 2). 

5 

Following Miller et al. (2014), the bases of shot taking behavior, **Λ** , are computed through a combination of smoothing and non-negative matrix factorization (NMF) (Lee & Seung 1999). Using integrated nested Laplace approximation (INLA) as the engine for our inference, we first fit a log Gaussian Cox Process (LGCP) (Banerjee et al. 2015) independently to each player’s point process defined by the ( _x, y_ ) locations of their made shots using the aforementioned mesh.<sup>2</sup> Each player’s estimated intensity function is evaluated at each vertex, producing a _K_ -dimensional vector for each of the _L_ = 433 players in our data. These vectors are exponentiated and gathered (by rows) into the _L × K_ matrix **P** , which we then factorize via NMF: 



This yields **Λ** , the deterministic bases we use in (2). While the bases from (3) are constructed solely with respect to the spatial variation in the FGA data (i.e. no basketball-specific structures are induced a priori), the constraint on the number of bases significantly impacts the basis shapes. In general, the NMF tends to first generate bases according to shot distance. After accounting for this primary source of variation, other systematic features of variation begin to appear in the bases, notably asymmetry. We use D = 16 basis functions, aligning with Miller et al. (2014) which suggests the optimal number of basis functions falls between 15 and 20. Collectively, these bases comprise a comprehensive set of shooting tendencies, as shown in Figure 2. We have added labels post hoc to provide contextual intuition. 



<!-- Start of picture text -->
Under Hoop<br><!-- End of picture text -->

















<!-- Start of picture text -->
Hoop Front<br><!-- End of picture text -->















Figure 2: _Deterministic bases resulting from the non-negative matrix factorization of_ **P** _. The plots are arranged such that the bases closest to the hoop are on the left (e.g. Under Hoop) and the bases furthest from the hoop are on the right (e.g. Center Arc 3). The residual basis, comprising court locations where shots are infrequently attempted from, is shown in the bottom-right plot._ 

Conceptually, the _Zj_ ( **s** ) term in (1) represents a player-specific spatial ‘correction’ to the global regression model **_β_**<sup>_′_</sup> **x** . These player-specific surfaces are linear combinations of the bases shown in 

> 2Players who took less than five shots in the regular season are treated as “replacement players.” 

6 

Figure 2. The weights of these combinations, **w** _j_ , are latent parameters which are jointly estimated with **_β_** . Since these player weights can be highly sensitive for players with very little data, it is imperative to introduce a regularization mechanism on them, which is accomplished using a conditionally autoregressive (CAR) prior. Conveniently, the NMF in (3) provides player-specific loadings onto these bases, **B** , which we use in constructing this CAR prior on the basis weights, **w** _j_ (Besag 1974). The purpose of using a CAR prior on the basis weights is to shrink the FG% estimates of players with similar shooting characteristics toward each other. This is integral for obtaining realistic FG% estimates in areas where a player took a low volume of shots. With only a handful of shots from an area, a player’s empirical FG% can often be extreme (e.g. near 0% or 100%). The CAR prior helps to regularize these extremes by borrowing strength from the player’s neighbors in the estimation. 

In order to get some notion of shooting similarity between players, we calculate the Euclidean distance between the player loadings contained in **B** and, for a given player, define the five players with the closest player loadings as their neighbors. This is intentionally chosen to be fewer than the number of neighbors selected by Cervone, recognizing that more neighbors defines a stronger prior and limits player-to-player variation in the FG% surfaces. We enforce symmetry in the nearestneighbors relationship by assuming that if player _j_ is a neighbor of player _ℓ_ , then player _ℓ_ is also a neighbor of player _j_ , which results in some players having more than five neighbors. These relationships are encoded in a player adjacency matrix **H** where entry ( _j, ℓ_ ) is 1 if player _ℓ_ is a neighbor of player _j_ and 0 otherwise. The CAR prior on **w** _j_ can be specified as 



where _nj_ is the total number of neighbors for player _j_ . 

Lastly, we set a _N_ ( **0** _,_ 0 _._ 001 _×_ **I** ) prior on **_β_** , and fit the model using INLA. This yields a model that varies spatially and allows us to predict player-specific FG% at any location in the offensive half court. In order to get high resolution FG% estimates, we partition the court into 1 ft. by 1 ft. grid cells (yielding a total of _M_ = 2350 cells) and denote player _j_ ’s FG% at the centroid of grid cell _i_ as _ξij_ . The projection of the FG% posterior mean ( **_ξ_**<sup>�</sup> _j_ ) for LeBron James is depicted in Figure 3. 

In order to have sufficient data to reliably estimate these surfaces, we assume that player FG%s are lineup independent. We recognize this assumption may be violated in some cases, as players who draw significant defensive attention can improve the FG%s of their teammates by providing them with more unguarded shot opportunities. Additionally, without defensive information about the shot opportunities, the FG% estimates are subject to systematic bias. Selection bias is introduced by unequal amounts of defensive pressure applied to shooters of different skill levels. 

The Bayesian modeling framework can amplify selection bias as well. Since the FG% estimates are regularized in our model via a CAR prior, players FG% estimates shrink toward their neighbors (which we’ve defined in terms of FGA rate). While this feature stabilizes estimates for players with 

7 

low sample sizes, it can be problematic when entire neighborhoods have low sample sizes from specific regions. For example, there are many centers who rarely or never shoot from long range. Consequently, the entire neighborhood shrinks toward the global mean 3-point FG%, inaccurately inflating these players’ FG%s beyond the 3-point line. These are intriguing challenges and represent promising directions for future work. 





<!-- Start of picture text -->
FG%<br>80<br>70<br>60<br>50<br>40<br>30<br><!-- End of picture text -->





<!-- Start of picture text -->
Std. Dev.<br>7<br>6<br>5<br>4<br><!-- End of picture text -->

Figure 3: _LeBron James 2016-17 FG% posterior mean (left) and posterior standard deviation (right) projected onto the offensive half court. The prediction surfaces shown here and throughout the figures in this paper utilize projections onto a spatial grid of 1 ft. by 1 ft. cells._ 

### **2.2 Determining FGA Rate Surfaces** 

We determine a player’s FGA rate surface by smoothing their shot attempts via a LGCP. This model has the form 

#### log _λ_ ( **s** ) = _β_ 0 + _Z_ ( **s** ) _,_ 

where _λ_ ( **s** ) is the Poisson intensity indicating the number of expected shots at location **s** , _β_ 0 is an intercept, and _Z_ ( **s** ) is a Gaussian process. We fit this model separately for each player using INLA, following the approach in Simpson et al. (2015). In brief, they demonstrate that the likelihood for the LGCP can be approximated using a finite-dimensional Gaussian random field, allowing _Z_ ( **s** ) to be represented by the basis function expansion _Z_ ( **s** ) =<sup>�</sup><sup>_B_</sup> _b_ =1<sup>_zbφb_(</sup><sup>**s**).Thebasisfunction</sup><sup>_φb_(</sup><sup>**s**)</sup> projects shot location onto a triangular mesh akin to the one detailed for (2). The expected value of _λ_ ( **s** ) integrated over the court is equal to the number of shots a player has taken, however there can be small discrepancies between the fitted intensity function and the observed number of shots. In order to ensure consistency, we scale the resulting intensity function to exactly yield the player’s observed number of shot attempts in that lineup. 

We normalize the surfaces to FGA per 36 minutes by dividing by the total number of minutes played by the associated lineup and multiplying by 36, allowing us to make meaningful comparisons between lineups who differ in the amount of minutes played. As with the FG% surfaces ( **_ξ_** ), we partition the court into 1 ft. by 1 ft. grid cells and denote player _j_ ’s FGA rate at the centroid of grid cell _i_ as _Aij_ . 

Note that we approach the FGA rate estimation from a fundamentally different perspective than 

8 

the FG% estimation. We view a player’s decision to shoot the ball as being completely within their control and hence non-random. As such, we incorporate no uncertainty in the estimated surfaces. We use the LGCP as a smoother for observed shots rather than as an estimate of a player’s true latent FGA rate. Other smoothing methods (e.g. kernel based methods (Diggle 1985)) could be used instead. 

Depending on the player and lineup, a player’s shot attempt profile can vary drastically from lineup to lineup. Figure 4 shows Kyrie Irving’s estimated FGA rate surfaces in the starting lineup (left) and the lineup in which he played the most minutes without LeBron James (middle). Based on these two lineups, Irving took 9.2 more shots per 36 minutes when he didn’t share the court with James. He also favored the left side of the court far more, which James tends to dominate when on the court. 





<!-- Start of picture text -->
FGA<br>0.10<br>0.05<br><!-- End of picture text -->





<!-- Start of picture text -->
FGA<br>0.06<br>0.04<br>0.02<br><!-- End of picture text -->





<!-- Start of picture text -->
Diff<br>0.050<br>0.025<br>0.000<br>−0.025<br><!-- End of picture text -->

Figure 4: _Left: Kyrie Irving’s FGA rate per 36 minutes in the starting lineup (in which he shared the most minutes with LeBron James). Center: Kyrie Irving’s FGA rate per 36 minutes in the lineup for which he played the most minutes without LeBron James. Right: The difference of the center surface from the left surface._ 

Clearly player shot attempt rates are not invariant to their teammates on the court. We therefore restrict player FGA rate estimation to lineup-specific data. Fortunately, the additional sparsity introduced by conditioning on lineup is a non-issue. If a player has no observed shot attempts from a certain region (e.g, Tristan Thompson from 3-point range), this simply means they chose not to shoot from that region—we don’t need to borrow strength from neighboring players to shed light on this area of “incomplete data”. 

## **3 Allocative Efficiency Metrics** 

The models for FG% and FGA rate described in Section 2 are the backbone of the allocative efficiency metrics we introduce in this section: lineup points lost (LPL) and player LPL contribution (PLC). Before getting into the details, we emphasize that these metrics are agnostic to the underlying FG% and FGA models; they can be implemented using even crude estimates of FG% and FGA rate, for example, by dividing the court into discrete regions and using the empirical FG% and FGA rate within each region.<sup>3</sup> Also note that the biases affecting FG% and FGA rate described 

> 3Section 6.1 in the appendix shows how LPL can be calculated using empirical estimates of FG% and FGA rate. We use the Cavaliers starting lineup to compare these empirical LPL surfaces to the more sophisticated versions presented in the main text. 

9 

in Section 2 may affect the allocative efficiency metrics as well. Section 4 includes a discussion of the causal limitations of the approach. 

LPL is the output of a two-step process. First, we redistribute a lineup’s observed distribution of shot attempts according to a proposed optimum. This optimum is based on ranking the five players in the lineup with respect to their FG% and FGA rate and then redistributing the shot attempts such that the FG% ranks and FGA rate ranks match. Second, we estimate how many points could have been gained had a lineup’s collection of shot attempts been allocated according to this alternate distribution. In this section, we go over each of these steps in detail and conclude by describing PLC, which measures how individual players contribute to LPL. 

### **3.1 Spatial Rankings Within a Lineup** 

With models for player FG% and player-lineup FGA rate, we can rank the players in a given lineup (from 1 to 5) on these metrics at any spot on the court. For a given lineup, let **_R_**<sup>_ξ_</sup> _i_<sup>beadiscrete</sup> transformation of **_ξ_** _i_ —the lineup’s FG% vector in court cell _i_ —yielding each player’s FG% rank relative to their four teammates. Formally, 



where _nξi_ is the length of **_ξ_** _i_ , the vector being ranked (this length will always be 5 in our case), and _ξi_<sup>(</sup><sup>_k_)</sup> is the _k_ th order statistic of **_ξ_** _i_ . Since _ξij_ is a stochastic quantity governed by a posterior distribution, _Rij_<sup>_ξ_isalsodistributional,howeveritsdistributionisdiscrete,thesupportbeingthe</sup> integers _{_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _}_ . The distribution of _Rij_<sup>_ξ_canbeapproximatedbytakingposteriorsamplesof</sup> **_ξ_** _i_ and ranking them via (5). Figure 16 in the appendix shows the 20% quantiles, medians, and 80% quantiles of the resulting transformed variates for the Cavaliers starting lineup. 

We obtain ranks for FGA rates in the same manner as for FG%, except these will instead be deterministic quantities since the FGA rate surfaces, **_A_** , are fixed. We define _Rij_<sup>_A_as</sup> 



where _nAi_ is the length of **_A_** _i_ and _A_<sup>(</sup> _i_<sup>_k_)</sup> is the _k_ th order statistic of **_A_** _i_ . Figure 5 shows the estimated maximum a posteriori<sup>4</sup> (MAP) FG% rank surfaces, **_R_**<sup>�</sup> _ξ_ , and the deterministic FGA rate rank surfaces, **_R_**<sup>_A_</sup> , for the Cleveland Cavaliers starting lineup. 

> 4For the FG% rank surfaces we use the MAP estimate in order to ensure the estimates are always in the support of the transformation (i.e. to ensure _R_<sup>�</sup> _ij_<sup>_ξ∈{_1</sup><sup>_, . . . ,_5</sup><sup>_}_).Forparameterswithcontinuoussupport,suchas</sup><sup>**_ξ_**�,thehat</sup> symbol denotes the posterior mean. 

10 



<!-- Start of picture text -->
LeBron James<br><!-- End of picture text -->



<!-- Start of picture text -->
JR Smith<br><!-- End of picture text -->



<!-- Start of picture text -->
Kevin Love<br><!-- End of picture text -->



<!-- Start of picture text -->
Kyrie Irving<br><!-- End of picture text -->



<!-- Start of picture text -->
Tristan Thompson<br><!-- End of picture text -->



<!-- Start of picture text -->
FG% MAP Rank<br>1<br>2<br>3<br>4<br>5<br><!-- End of picture text -->













<!-- Start of picture text -->
FGA rate Rank<br>1<br>2<br>3<br>4<br>5<br><!-- End of picture text -->

Figure 5: _Top: Estimated FG% ranks for the Cleveland Cavaliers’ starting lineup. Bottom: Deterministic FGA rate ranks._ 

The strong correspondence between **_R_**<sup>�</sup> _ξ_ and **_R_** _A_ shown in Figure 5 is not surprising; all other factors being equal, teams would naturally want their most skilled shooters taking the most shots and the worst shooters taking the fewest shots in any given location. By taking the difference of _ξ_ a lineup’s FG% rank surface from its FGA rate rank surface, **_R_**<sup>_A_</sup> _−_ **_R_**<sup>�</sup> , we obtain a surface which measures how closely the lineup’s FG% ranks match their FGA rate ranks. Figure 6 shows these surfaces for the Cavaliers’ starting lineup. 













<!-- Start of picture text -->
Rank<br>Correspondence<br>4<br>3<br>2<br>1<br>0<br>−1<br>−2<br>−3<br>−4<br><!-- End of picture text -->

Figure 6: _Rank correspondence surfaces for the Cleveland Cavaliers’ starting lineup._ 

Note that rank correspondence ranges from -4 to 4. A value of -4 means that the worst shooter in the lineup took the most shots from that location, while a positive 4 means the best shooter took the fewest shots from that location. In general, positive values of rank correspondence mark areas of potential under-usage and negative values show potential over-usage. For the Cavaliers, the positive values around the 3-point line for Kyrie Irving suggest that he may be under-utilized as a 

11 

3-point shooter. On the other hand, the negative values for LeBron James in the mid-range region suggest that he may be over-used in this area. We emphasize, however, that conclusions should be made carefully. Though inequality between the FG% and FGA ranks may be indicative of suboptimal shot allocation, this interpretation may not hold in every situation due to bias introduced by confounding variables (e.g. defensive pressure, shot clock, etc.). 

### **3.2 Lineup Points Lost** 

By reducing the FG% and FGA estimates to ranks, we compromise the magnitude of player-toplayer differences within lineups. Here we introduce lineup points lost (LPL), which measures deviation from perfect rank correspondence while retaining the magnitudes of player-to-player differences in FG% and FGA. 

LPL is defined as the difference in expected points between a lineup’s actual distribution of FG attempts, **_A_** , and a proposed redistribution, **_A_**<sup>_∗_</sup> , constructed to yield perfect rank correspondence (i.e. **_R_**<sup>_A∗_</sup> _−_ **_R_**<sup>_ξ_</sup> = **0** ). Formally, we calculate LPL in the _i_ th cell as 



where v _i_ is the point value (2 or 3) of a made shot, _ξij_ is the FG% for player _j_ in cell _i_ , _Aij_ is player _j_ ’s FG attempts (per 36 minutes) in cell _i_ , and _g_ ( _Rij_<sup>_ξ_) =</sup><sup>_{k_:</sup><sup>_R_</sup> _ij_<sup>_ξ≡R_</sup> _ik_<sup>_A}_.Thefunction</sup><sup>_g_(</sup><sup>_·_)</sup> reallocates the observed shot attempt vector **_A_** _i_ such that the best shooter always takes the most shots, the second best shooter takes the second most shots, and so forth. 

Figure 7 shows a toy example of how LPL is computed for an arbitrary 3-point region, contextualized via the Cleveland Cavaliers starting lineup. In this hypothetical scenario, James takes the most shots despite both Love and Irving being better shooters from this court region. When calculating LPL for this region, Irving is allocated James’ nine shots since he is the best shooter in this area. Love, as the second best shooter, is allocated Irving’s four shots (which was the second most shots taken across the lineup). James, as the third best shooter, is allocated the third most shot attempts (which is Love’s three shots). Smith and Thompson’s shot allocations are unchanged since their actual number of shots harmonizes with the distribution imposed by _g_ ( _·_ ). Each player’s actual expected points and optimal expected points are calculated by multiplying their FG% by the corresponding number of shots and the point-value of the shot (3 points in this case). LPL is the difference (in expectation) between the optimal points and the actual points, which comes out to 0.84. 

12 



<!-- Start of picture text -->
Kyrie Irving Kevin Love LeBron James JR Smith Tristan Thompson<br>FG%: 40% 38% 35% 32% 25%<br>Actual shots taken: 4 43 109 12 21<br>Optimal redistribution: 9 4 3 2 1<br>Actual points: ((.40 × 4)+ (.38 × 3) + (.35 × 9) + (.32 × 2) + (.25 × 1)) × 3 = 20.34<br>Optimal points: ((.40 × 9)+ (.38 × 4) + (.35 × 3) + (.32 × 2) + (.25 × 1)) × 3 = 21.18<br>Lineup points lost (LPL): Optimal points      − Actual points                             = 0.84<br><!-- End of picture text -->

Figure 7: _A toy LPL computation in an arbitrary 3-point court region for the Cleveland Cavalier’s starting lineup. The players are ordered from left to right according to FG% (best to worst). Below each player’s picture is the number of actual shots the player took from this location. The black arrows show how the function g_ ( _·_ ) _reallocates these shots according to the players’ FG% ranks. The filled gray dots show the number of shots the player would be allocated according to the proposed optimum. Below the horizontal black line, each player’s actual expected points and optimal expected points are calculated by multiplying their FG% by the corresponding number of shots and the point value of the shot. LPL is the difference (in expectation) between the optimal points and the actual points._ 

The left plot of Figure 8 shows LPL (per 36 minutes) over the offensive half court for Cleveland’s<sup>�</sup> starting lineup, computed using the posterior mean of **_ξ_** .<sup>5</sup> Notice that the LPL values are highest around the rim and along the 3-point line. These regions tend to dominate LPL values because the density of shot attempts is highest in these areas. 





<!-- Start of picture text -->
LPL per 36<br>0.006<br>0.004<br>0.002<br>0.000<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per Shot<br>0.06<br>0.04<br>0.02<br>0.00<br><!-- End of picture text -->

Figure 8: _LPL_<sup>�</sup> _and LPL_<sup>�</sup> _Shot surfaces for the Cleveland Cavaliers starting lineup._ 

If we re-normalize LPL with respect to the number of shots taken in each court cell we can 

> 5Since LPL _i_ is a function of **_ξ_** _i_ , which is latent, the uncertainty in LPL _i_ is proportional to the posterior distribution of<sup>�5</sup> _j_ =1<sup>_ξij_.Figures17-18intheappendixillustratethedistributionalnatureofLPL.</sup> 

13 

identify areas of inefficiency that do not stand out due to low densities of shot attempts: 



This formulation yields the average lineup points lost per shot from region _i_ , as shown in the right plot of Figure 8. 

LPL incorporates an intentional constraint—for any court cell _i_ , **_A_**<sup>_∗_</sup> _i_<sup>isconstrainedtobea</sup> _permutation_ of **_A_** _i_ . This ensures that no single player can be reallocated every shot that was taken by the lineup (unless a single player took all of the shots from that region to begin with). It also ensures that the total number of shots in the redistribution will always equal the observed number of shots from that location �i.e.<sup>�5</sup> _j_ =1<sup>_Aij_= �5</sup> _j_ =1<sup>_A∗_</sup> _ij_<sup>,forall</sup><sup>_i_</sup> �. 

Ultimately, LPL aims to quantify the points that could have been gained had a lineup adhered to the shot allocation strategy defined by **_A_**<sup>_∗_</sup> . However, as will be detailed in Section 4, there is not a 1-to-1 relationship between ‘lineup points’ as defined here, and actual points. In other words, reducing the total LPL of a team’s lineup by 1 doesn’t necessarily correspond to a 1-point gain in their actual score. In fact, we find that a 1-point reduction in LPL corresponds to a 0.6-point gain (on average) in a team’s actual score. One reason for this discrepancy could be because LPL is influenced by contextual variables that we are unable to account for in our FG% model, such as the shot clock and defensive pressure. Another may be due to a tacit assumption in our definition of LPL. By holding each player’s FG% constant despite changing their volume of shots when redistributing the vector of FG attempts, we implicitly assume that a player’s FG% is independent of their FGA rate. The basketball analytics community generally agrees that this assumption does not hold—that the more shots a player is allocated, the less efficient their shots become. This concept, referred to as the ‘usage-curve’ or ‘skill-curve’, was introduced in Oliver (2004) and has been further examined in Goldman & Rao (2011). Incorporating usage curves into LPL could be a promising area of future work. 

### **3.3 Player LPL Contribution** 

LPL summarizes information from all players in a lineup into a single surface, compromising our ability to identify how each individual player contributes to LPL. Fortunately, we can parse out each player’s contribution to LPL and distinguish between points lost due to undershooting and points lost due to overshooting. We define player _j_ ’s LPL contribution (PLC) in court location _i_ as 



where all terms are as defined in the previous section. The parenthetical term in (10) apportions LPL _i_ among the 5 players in the lineup proportional to the size of their individual contributions to LPL _i_ . Players who are reallocated more shots under **_A_**<sup>_∗_</sup> _i_<sup>compared to their observed number of shot</sup> 

14 

attempts will have PLC _ij >_ 0. Therefore, positive PLC values indicate potential undershooting and negative values indicate potential overshooting. As in the case of LPL, if we divide PLC by the sum of shot attempts in cell _i_ , we obtain average PLC per shot from location _i_ : 



The PLC<sup>_Shot_</sup> _i_ surfaces for the Cleveland Cavaliers’ 2016-17 starting lineup are shown in Figure 9. We see that Kyrie Irving is potentially being under-utilized from beyond the arc and that LeBron James is potentially over-shooting from the top of the key, which is harmonious with our observations from Figure 6. However, it is worth noting that the LPL per 36 plot (left plot in Figure 8) shows very low LPL values from the mid-range region since the Cavaliers have a very low density of shots from this area. So while it may be true that LeBron tends to overshoot from the top of the key relative to his teammates, the lineup shoots so infrequently from this area that the inefficiency is negligible. 













<!-- Start of picture text -->
PLC per shot<br>0.02<br>0.00<br>−0.02<br><!-- End of picture text -->

Figure 9: _PLC_<sup>�</sup> _Shot surfaces for the Cleveland Cavaliers starting lineup._ 

For every red region in Figure 9 (undershooting) there are corresponding blue regions (overshooting) among the other players. This highlights the fact that LPL is made up of balancing player contributions from undershooting and overshooting; for every player who overshoots, another player (or combination of players) undershoots. By nature of how LPL is constructed, there cannot be any areas where the entire lineup overshoots or undershoots. For this reason, our method does not shed light on shot selection. LPL and PLC say nothing about whether shots from a given region are efficient or not, instead they measure how efficiently a lineup adheres to optimal allocative efficiency given the shot attempts from that region. 

## **4 Optimality - Discussion and Implications** 

We have now defined LPL and given the theoretical interpretation (i.e. overuse and underuse), but we have not yet established that this interpretation is valid in practice. The utility of LPL as a diagnostic tool hinges on the answers to four questions, which we explore in detail in this section: 

15 

1. Do lineups minimize LPL? 

2. Does LPL relate to offensive production? 

3. How can LPL inform strategy? 

4. Is minimizing LPL always optimal? 

### **4.1 Do lineups minimize LPL?** 

In Figure 8, cell values range from 0 to 0.008, and the sum over all locations in the half court is 0.68. While this suggests that the Cavaliers’ starters were minimizing LPL, we need a frame of reference to make this claim with certainty. The frame of reference we will use for comparison is the distribution of LPL under completely random shot allocation. This is not to suggest offenses select shooting strategies randomly. Rather, a primary reason why lineups fail to effectively minimize LPL is because the defense has the opposite goal; defenses want to get the opposing lineup to take shots from places they are bad at shooting from. In other words, while the offense is trying to minimize LPL, the defense is trying to maximize LPL. By comparing LPL against random allocation, this provides a general test for whether offenses are able to pull closer to the minimum than defenses are able to pull toward the maximum, or the absolute worst allocation possible. 

In statistical terms, this comparison can be stated as a hypothesis test. We are interested in testing the null hypothesis that offenses minimize and defenses maximize LPL with equal magnitudes. We consider a one-sided alternative—that the offensive minimization outweighs the defensive response (as measured on by LPL). A permutation test allows us to test these hypotheses by comparing a lineup’s observed total LPL (summing over all court locations,<sup>�</sup><sup>_M_</sup> _i_<sup>LPL</sup><sup>_i_,where</sup><sup>_M_isthe</sup> total number of 1 ft. by 1 ft. cells in the half court) against the total LPL we would expect under completely random shot allocation. To ensure the uncertainty in **_ξ_** is accounted for, we simulate variates of the test statistic _T_ as 



where _ξ_<sup>�</sup> _ij_ is a sample from player _j_ ’s posterior distribution of FG% in cell _i_ , _A_<sup>_†_</sup> _ij_<sup>is the</sup><sup>_j_th element of</sup> a random permutation of the observed FGA rate vector **_A_** _i_ , and all other symbols are defined as in (7)-(8). Note that a _different_ random permutation is drawn for each court cell _i_ . After simulating 500 variates from the null distribution, we approximate the one-sided p-value of the test as the proportion of variates that are less than 0. 

Figure 10 illustrates this test for the Cleveland Cavaliers’ starting lineup. The gray bars show a histogram of the variates from (12). Bars to the left of the dashed line at 0 represent variates 

16 

for which random allocation outperforms the observed allocation. The approximate p-value of the test in this case is 1/500, or 0.002. We can therefore say with high certainty that the Cleveland starters minimize LPL beyond the defense’s ability to prevent them from doing so. 

Permutation test of H0 vs HA 



<!-- Start of picture text -->
120<br>100<br>80<br>60<br>40<br>1<br>20 p ^  =<br>500<br>0<br>−1 0 1 2 3 4 5 6<br>T =  ∑M LPLHi 0 − ∑M LPLi<br>i = 1 i = 1<br>Frequency<br><!-- End of picture text -->

Figure 10: _Permutation test for the Cleveland Cavaliers’ 2016-17 starting lineup. The gray bars show a histogram of the variates from (12). The approximate p-value for the Cavaliers starting lineup (i.e. the proportion of variates that are less than 0) is 1/500 or 0.002._ 

The computational burden of performing the test precludes performing it for every lineup, but we did perform the test for each team’s 2016-17 starting lineup. The results are shown in Table 4.1. Across the NBA’s starting lineups, only two teams had no variates less than 0—the Golden State Warriors and the Portland Trailblazers. The Sacramento Kings showed the worst allocative efficiency with an approximate p-value of 0.44 for their starting lineup. Based on these results we are confident that most lineups employ shot allocation strategies that minimize LPL to some degree, though it appears that some teams do so better than others. 

**Approximate** **<u>p-values</u> for** H<sup>0</sup> **vs.** H<sup>A</sup> 

||1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Team|GSW|POR|CLE|LAC|ATL|HOU|TOR|IND|LAL|DET|DEN|NOP|CHA|UTA|OKC|
|ˆ_p_|0.000|0.000|0.002|0.002|0.014|0.014|0.016|0.020|0.022|0.024|0.028|0.030|0.030|0.038|0.042|
||16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|
|Team|DAL|MIA|MIN|BOS|NYK|ORL|SAS|BKN|PHI|MIL|WAS|PHX|MEM|CHI|SAC|
|ˆ_p_|0.044|0.046|0.054|0.056|0.058|0.064|0.104|0.106|0.130|0.134|0.144|0.148|0.170|0.210|0.442|



Table 1: Approximate p-values for H<sup>0</sup> vs. H<sup>A</sup> for each team’s starting lineup in the 2016-17 NBA regular season. 

### **4.2 Does LPL relate to offensive production?** 

We next want to determine whether teams with lower LPL values tend to be more proficient on offense. In order to achieve greater discriminatory power, we’ve chosen to make this assessment at 

17 

the game level. Specifically, we regress a team’s total game score against their total LPL generated in that game, accounting for other relevant covariates including the team’s offensive strength, the opponents’ defensive strength, and home-court advantage. This framework is analogous to the model proposed in Dixon & Coles (1997). 

We calculate game LPL (GLPL) by first dividing the court into three broad court regions (restricted area, mid-range, and 3-pointers). Then, for a given game and lineup, we calculate GLPL in each of these court regions (indexed by _c_ ) by redistributing the lineup’s observed vector of shot attempts using on a weighted average of each player’s **_ξ_**<sup>�</sup> _j_ : 



In (15), _wij_ is a weight proportional to player _j_ ’s total observed shot attempts in court cell _i_ over the regular season. The notation<sup>�</sup> _i∈c_<sup>meanswearesummingoverallthe1ft.by1ft.grid</sup> cells that are contained in court region _c_ . Finally, for a given game _g_ and team _a_ , we calculate the team’s total game LPL (TGLPL) by summing GLPL _c_ over all court regions _c_ and all lineups _ℓ_ : 



where _C_ = _{_ restricted area, mid-range, 3-pointers _}_ and _La_ is the total number of team _a_ ’s lineups. This process is carried out separately for the home and away teams, yielding two TGLPL observations per game. 

Equipped with a game-level covariate measuring aggregate LPL, we model team _a_ ’s game score against opponent _b_ in game _g_ as 





where _µ_ represents the global average game score, _αa_ is team _a_ ’s offensive strength parameter, _βb_ is team _b_ ’s defensive strength parameter, _γ_ governs home court advantage, _θ_ is the effect of TGLPL, and _ϵabg_ is a normally distributed error term. _θ_ is the parameter that we are primarily concerned with. We fit this model in a Bayesian framework using Hamiltonian Monte Carlo methods implemented in Stan (Carpenter et al. 2017). Our prior distributions are as follows: _µ ∼ N_ (100 _,_ 10<sup>2</sup> ); _αa, βb, γ, θ ∼ N_ (0 _,_ 10<sup>2</sup> ); _σ ∼ Gamma_ (shape = 2 _,_ rate = 0 _._ 2). 

The 95% highest posterior density interval for _θ_ is (-1.08, -0.17) and the posterior mean is -0.62.<sup>6</sup> Therefore, we estimate that for each additional lineup point lost, a team loses 0.62 actual points. Put differently, by shaving roughly 3 points off of their TGLPL, a team could gain an estimated 2 points in a game. Given that 10% of games were decided by 2 points or less in the 

> 6Figure 19 in the appendix shows the posterior distribution of _θ_ . 

18 

2016-17 season, this could have a significant impact on a team’s win-loss record and could even have playoff implications for teams on the bubble. Figure 11 shows the estimated density of actual points lost per game for every team’s 82 games in the 2016-17 NBA regular season (i.e. density of � _θ ×_ TGLPL _ag, g ∈{_ 1 _, . . . ,_ 82 _}_ for each team _a_ ). Houston was the most efficient team, only losing about 1 point per game on average due to inefficient shot allocation. Washington, on the other hand, lost over 3 points per game on average from inefficient shot allocation. 

### Distribution of Actual Points Lost per Game from LPL 



<!-- Start of picture text -->
Washington<br>Brooklynn<br>New Orleans<br>Memphis<br>Oklahoma City<br>Denver<br>Boston<br>Atlanta<br>Cleveland<br>Sacramento<br>Dallas<br>Golden State<br>Points Lost<br>Portland<br>6<br>Miluakee<br>Miami 4<br>Detroit<br>2<br>San Antonio<br>Phoenix<br>0<br>New York<br>Philidelphia<br>Minnesota<br>Chicago<br>Charlotte<br>Utah<br>Indiana<br>L.A. Clippers<br>Toronto<br>L.A. Lakers<br>Orlando<br>Houston<br>0 2 4 6<br>Actual Points Lost<br>Team<br><!-- End of picture text -->

Figure 11: _Estimated density of actual points lost per game for every team’s 82 games in the 2016-17 NBA regular season._ 

19 

### **4.3 How can LPL inform strategy?** 

At this point, we offer some ideas for how coaches might use these methods to improve their teams’ offense. First, for lineups with high LPL, coaches could explore the corresponding PLC plots to ascertain which players are primarily responsible. If the coach determines that the LPL values do indeed represent areas of inefficiency, they could consider interventions targeting the player’s shooting habits in these areas. This short-term intervention could be coupled with long-term changes to their practice routines; coaches could work with players on improving their FG% in the areas shown by the PLC plots. Also, by exploring lineup PLC charts, coaches could identify systematic inefficiency in their offensive schemes, which could prompt changes either in whom to draw plays for or whether to change certain play designs altogether. 

Coaches are not the only parties who could gain value from these metrics; players and front office personnel could utilize them as well. Players could use PLC plots to evaluate their shooting habits and assess whether they exhibit over-confident or under-confident shot-taking behavior from certain areas of the court. Front office personnel may find trends in the metrics that indicate a need to sign players that better fit their coach’s strategy. LPL and PLC could help them identify which players on their roster to shop and which players to pursue in free agency or the trade market. 

Consider these ideas in context of the Utah Jazz LPL/PLC charts for the 2016-17 regular season shown in Figure 12. 





<!-- Start of picture text -->
LPL per 36<br>0.03<br>0.02<br>0.01<br>0.00<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per Shot<br>0.125<br>0.100<br>0.075<br>0.050<br>0.025<br>0.000<br><!-- End of picture text -->













<!-- Start of picture text -->
PLC per shot<br>0.050<br>0.025<br>0.000<br>−0.025<br>−0.050<br><!-- End of picture text -->

On reviewing the LPL per shot plot for the starting lineup, the coach might flag the left baseline 

20 

and top of the key as areas of potential inefficiency to investigate. On exploring the corresponding PLC plots, they would see Derrick Favors as the driving force behind the high LPL numbers from these regions. Interestingly, from the 2013-14 season through 2016-17, the Derrick Favors baseline and elbow jump shots were go-to plays for the Jazz. Across these four seasons, Favors took over 1500 mid-range shots for an average of 0.76 points per shot (PPS). 

In the 2017-18 and 2018-19 seasons, the Jazz drastically altered Favors’ shot policy from the mid-range. Beginning in 2017, the Jazz started focusing on running plays for 3-pointers and shots at the rim, a trend that was becoming popular throughout the league. As part of this change in play-style, they tried turning Favors into a stretch four<sup>7</sup> ; he went from taking a total of 21 3-point shots over the previous four seasons, to 141 3-point shots in these two seasons alone. Unfortunately, their intervention for Favors appears to have been misguided; his average PPS for these 141 shots was 0.66. The front office eventually determined that Favors wasn’t the best fit for their coach’s offensive strategy; they opted not to re-sign Favors at the end of the 2019 season. 

This process took place over six yearsperhaps it could have been expedited had LPL and PLC been available to the coaches and front 

### **4.4 Is minimizing LPL always optimal?** 

While we have demonstrated that lower LPL is associated with increased offensive production, we stress that LPL is a diagnostic tool that should be used to inform basketball experts rather than as a prescriptive measure that should be strictly adhered to in all circumstances. As mentioned previously, the LPL and PLC values presented in this paper are influenced by contextual variables that we are unable to account for because they are not available in public data sources, such as the shot clock and defensive pressure. Additionally, there are certain game situations where minimizing LPL may be sub-optimal. 

One such situation is illustrated in Figure 13, which shows the PLC<sup>_Shot_</sup> surfaces for the Oklahoma City 2016-17 starting lineup. 













<!-- Start of picture text -->
PLC per shot<br>0.10<br>0.05<br>0.00<br>−0.05<br><!-- End of picture text -->

The first panel from the left in this figure shows positive PLC values for Russell Westbrook in 

> 7A stretch four is a player at the power forward position that can generate offense farther from the basket than a traditional power forward. 

21 

the corner 3-point regions, suggesting that Westbrook should be taking more shots from these areas. However, anyone who watched the Thunder play that season will know that many of these corner 3-point opportunities were created by Westbrook driving to the basket, drawing extra defenders toward him, then kicking the ball out to an open teammate in the corner. Obviously, Westbrook cannot both drive to the rim and simultaneously pass to himself in another area of the court. In this case, strictly minimizing LPL would reduce the number of these drive-and-kick plays, potentially attenuating their offensive firepower. Shot-creation is not accounted for by LPL and should be carefully considered when exploring LPL and PLC. 

There are game theoretic factors to be considered as well. Beyond the defensive elements discussed in Section 4.1, rigid adherence to minimizing LPL could lead to a more predictable offense and thus make it easier to defend (D’Amour et al. 2015). Needless to say, offensive game-planning should be informed by more than LPL metrics alone. 

## **5 Conclusion** 

Our research introduces novel methods to evaluate allocative efficiency spatially and shows that this efficiency has a real impact on game outcomes. We use publicly available data and have made an empirical demonstration of our methods available online, allowing our methods to be immediately accessible. Also, since LPL and PLC do not depend on specific models for FG% and FGA rate, LPL and PLC could readily be calculated at G-league, NCAA, and international levels using a simplified model of FG% and FGA rate. 

As most professional basketball teams have access to proprietary data, many of the contextual variables that we do not account for could be included in the FG% and FGA rate models, which could make the proposed shot distribution proposed by LPL a more reliable optimum to seek. Additionally, by pairing LPL with play call data coaches could gain insight into the efficiency of specific plays. Even without access to these data, it may be possible to recreate some contextual features that aren’t explicitly provided by the NBA’s public-facing API. For instance, shot clock times could be reverse engineered using game clock times given in the play-by-play data. 

There are interesting academic questions that stem from this paper as well. Future studies could investigate the sensitivity of our metrics to model parameters that we fixed, such as the number of basis functions in the NMF and the number of neighbors in the CAR prior. We could also investigate the robustness of LPL to alternate FG% models. As mentioned previously, we do not account for usage curves in our analysis. Doing so would turn LPL into a constrained optimization problem, which would be a fascinating challenge to tackle. Also, using LPL to inform player-specific shot policy changes, entire seasons could be simulated using the method in Sandholtz & Bornn (2020) to quantify the impact of specific shot allocation changes on point production. We hope that the methods introduced in this paper will be built upon and improved. 

22 

## **6 Appendix** 

### **6.1 Empirical Implementation** 

To illustrate some important considerations associated with this approach, we present a brief example of LPL and PLC using empirical FG% and FGA rates. This example demonstrates that these quantities are agnostic to the underlying FG% model. 

We examine the same lineup for the Cavaliers that is discussed in the main text. In order to obtain FG% and FGA rate estimates, we divide the court into twelve discrete regions and calculate the empirical values for each player within these regions. We defined these regions based on our understanding of the court, but it is worth noting that defining these regions requires many of the same considerations as with any histogram style estimator; namely, that increasing the number of regions will decrease bias at the expense of increasing variance. In some cases, a player may have only one or two shots within an area, resulting in either unrealistically high or low field goal percentage estimates. As an _ad hoc_ solution to this, we give all players one made field goal and five field goal attempts within each region, which means that players with just a handful of shots in a region will have their associated field goal percentage anchored near 20 percent. Rather than perform smoothing for the field goal attempt estimates, we simply count up the number of attempts for each player within each section, and normalize them to get the attempts per 36 minutes, as before. With these FG% and FGA estimates, we can replicate the analysis detailed in Section 3. 

Figure 14 shows the empirical ranks for this lineup, as well as the rank correspondence. Generally, it shows the same patterns as the model-based analysis in Figures 5 and 6. However, there are some key differences, including Tristan Thompson having a higher field goal percentage rank from the right midrange and a corresponding reduction in rank for Kevin Love in the same area. This pattern is also manifest in Figure 15, which shows the empirical LPL. We observe that most lineup points appear to be lost in the right midrange and in above the break three point shots. Finally, considering the empirical PLC in Figure 15, we notice that in addition to the Love-Thompson tradeoff in the midrange, JR Smith appears to be overshooting from the perimeter, while Kyrie Irving and LeBron James both exhibit undershooting. 

The persistence of the Love-Thompson connection in the midrange in this empirical analysis, and its divergence from what we saw in the model based analysis, merits a brief discussion. Kevin Love and Tristan Thompson both had a low number of shots from the far-right midrange region, with Love shooting 8 for 26 and Thompson shooting 4 for 6. Because they both shot such a low amount of shots, even with the penalty of one make and four misses added to each region, Thompson appears far better. This highlights the fact that although LPL and PLC are model agnostic, the underlying estimates for field goal percentage do matter and raw empirical estimates alone may be too noisy to be useful in calculating LPL. One simple solution may be to use a threshold and only consider players in a region if the number of their field goal attempts passes that threshold. 

23 



<!-- Start of picture text -->
JR Smith Kevin Love Kyrie Irving LeBron James Tristan Thompson<br>FG% Rank<br>1<br>2<br>3<br>4<br>5<br>JR Smith Kevin Love Kyrie Irving LeBron James Tristan Thompson<br>FGA Rank<br>1<br>2<br>3<br>4<br>5<br>JR Smith Kevin Love Kyrie Irving LeBron James Tristan Thompson<br>Rank Diff<br>4<br>3<br>2<br>1<br>0<br>−1<br>−2<br>−3<br>−4<br><!-- End of picture text -->

Figure 14: _Top: Empirical FG% ranks for the Cleveland Cavaliers starting lineup. Middle: Empirical FGA ranks. Bottom: Rank correspondence._ 



<!-- Start of picture text -->
Cleveland 2016−17 Starting Lineup Cleveland 2016−17 Starting Lineup<br>L. James J. Smith K. Love K. Irving T. Thompson L. James J. Smith K. Love K. Irving T. Thompson<br>LPL per 36 LPL per shot<br>0.6 0.100<br>0.4 0.075<br>0.050<br>0.2 0.025<br>0.0 0.000<br>JR Smith Kevin Love Kyrie Irving LeBron James Tristan Thompson<br>PLC per 36<br>0.050<br>0.025<br>0.000<br>−0.025<br>−0.050<br><!-- End of picture text -->

Figure 15: _Top: Empirical LPL and LPL_<sup>_Shot_</sup> _for the Cleveland Cavaliers starting lineup. Bottom: Empirical PLC for the Cleveland Cavaliers starting lineup._ 

24 

### **6.2 Additional Figures** 



<!-- Start of picture text -->
LeBron James<br><!-- End of picture text -->







<!-- Start of picture text -->
JR Smith<br><!-- End of picture text -->







<!-- Start of picture text -->
Kevin Love<br><!-- End of picture text -->







<!-- Start of picture text -->
Kyrie Irving<br><!-- End of picture text -->







<!-- Start of picture text -->
Tristan Thompson<br><!-- End of picture text -->







<!-- Start of picture text -->
FG% Rank<br>20% Quantile<br>1<br>2<br>3<br>4<br>5<br>FG% Rank<br>Median<br>1<br>2<br>3<br>4<br>5<br>FG% Rank<br>80% Quantile<br>1<br>2<br>3<br>4<br>5<br><!-- End of picture text -->

Figure 16: _Top: 20% quantiles of the Cleveland Cavaliers starting lineup posterior distributions of FG% ranks. Middle: medians of these distributions. Bottom: 80% quantiles._ 



Figure 17: _Histogram of_<sup>�</sup><sup>_M_</sup> _i_ =1<sup>_LPLifortheClevelandCavaliersstartinglineup.500posteriordrawsfrom_</sup> _each ξij, where i ∈{_ 1 _. . . , M } and j ∈{_ 1 _, . . . ,_ 5 _}, were used to compute the 500 variates of_<sup>�</sup><sup>_M_</sup> _i_ =1<sup>_LPLi_</sup> _comprising this histogram._ 

25 





<!-- Start of picture text -->
LPL per 36<br>0.06<br>0.04<br>0.02<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per 36<br>0.06<br>0.04<br>0.02<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per 36<br>0.06<br>0.04<br>0.02<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per Shot<br>0.25<br>0.20<br>0.15<br>0.10<br>0.05<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per Shot<br>0.25<br>0.20<br>0.15<br>0.10<br>0.05<br><!-- End of picture text -->





<!-- Start of picture text -->
LPL per Shot<br>0.25<br>0.20<br>0.15<br>0.10<br>0.05<br><!-- End of picture text -->

Figure 18: _Left: 20% quantile LPL surfaces for the Cleveland Cavaliers starting lineup. Middle: median LPL surfaces. Bottom: 80% quantile LPL surfaces. The top rows show LPL_<sup>36</sup> _while the bottom rows show LPL_<sup>_Shot_</sup> _._ 

#### θ Posterior Distribution 



<!-- Start of picture text -->
1.5<br>1.0<br>0.5<br>0.0<br>−1.5 −1.0 −0.5 0.0<br>θ<br>Density<br><!-- End of picture text -->

Figure 19: _Posterior distribution of the effect for TGLPL in model (17)-(18) described in Section 4.2._ 

26 

## **References** 

- Banerjee, S., Carlin, B. P. & Gelfand, A. E. (2015), _Hierarchical Modeling and Analysis for Spatial Data_ , 2nd edn, CRC Press, Boca Raton, FL. 

- Besag, J. (1974), ‘Spatial interaction and the statistical analysis of lattice systems’, _Journal of the Royal Statistical Society. Series B._ **36** (2), 192–236. 

- Carpenter, B., Gelman, A., Hoffman, M. D., Lee, D., Goodrich, B., Betancourt, M., Brubaker, M., Guo, J., Li, P. & Riddell, A. (2017), ‘Stan: A probabilistic programming language’, _Journal of statistical software_ **76** (1). 

- Cervone, D., DAmour, A., Bornn, L. & Goldsberry, K. (2016), ‘A multiresolution stochastic process model for predicting basketball possession outcomes’, _Journal of the American Statistical Association_ **111** (514), 585–599. 

- Chang, Y.-H., Maheswaran, R., Su, J., Kwok, S., Levy, T., Wexler, A. & Squire, K. (2014), Quantifying shot quality in the NBA, _in_ ‘The 8th Annual MIT Sloan Sports Analytics Conference, Boston, MA’. 

- D’Amour, A., Cervone, D., Bornn, L. & Goldsberry, K. (2015), ‘Move or die: How ball movement creates open shots in the nba’, _Sloan Sports Analytics Conference_ . 

- Diggle, P. (1985), ‘A Kernel Method for Smoothing Point Process Data’, _Journal of the Royal Statistical Society. Series C (Applied Statistics)_ **34** (2), 138–147. 

- Dixon, M. J. & Coles, S. G. (1997), ‘Modelling association football scores and inefficiencies in the football betting market’, _Journal of the Royal Statistical Society: Series C (Applied Statistics)_ **46** (2), 265–280. 

- Gelman, A., Carlin, J., Stern, H., Dunson, D., Vehtari, A. & Rubin, D. (2013), _Bayesian Data Analysis, Third Edition_ , Chapman & Hall/CRC Texts in Statistical Science, Taylor & Francis. **URL:** _https://books.google.ca/books?id=ZXL6AQAAQBAJ_ 

- Goldman, M. & Rao, J. M. (2011), Allocative and dynamic efficiency in nba decision making, _in_ ‘The 5th Annual MIT Sloan Sports Analytics Conference, Boston, MA’. 

- Kubatko, J., Oliver, D., Pelton, K. & Rosenbaum, D. T. (2007), ‘A starting point for analyzing basketball statistics’, _Journal of Quantitative Analysis in Sports_ **3** (3). 

- Lee, D. D. & Seung, H. S. (1999), ‘Learning the parts of objects by non-negative matrix factorization’, _Nature_ **401** , 788. 

   - **URL:** _https://doi.org/10.1038/44565 http://10.0.4.14/44565_ 

27 

- Lindgren, F., Rue, H. & Lindstr¨om, J. (2011), ‘An explicit link between Gaussian fields and Gaussian Markov random fields: the stochastic partial differential equation approach’, _Journal of the Royal Statistical Society, Series B_ **73** (4), 423–498. **URL:** _http://dx.doi.org/10.1111/j.1467-9868.2011.00777.x_ 

- Miller, A., Bomn, L., Adams, R. & Goldsberry, K. (2014), ‘Factorized point process intensities: A spatial analysis of professional basketball’, _31st International Conference on Machine Learning, ICML 2014_ **1** , 398–414. 

- Oliver, D. (2004), _Basketball on Paper: Rules and Tools for Performance Analysis_ , Brassey’s, Incorporated. 

**URL:** _https://books.google.com/books?id=hDUK-rAVwbQC_ 

- Sandholtz, N. & Bornn, L. (2020), ‘Markov decision processes with dynamic transition probabilities: An analysis of shooting strategies in basketball’, _arXiv preprint arXiv:1812.05170_ . 

- Simpson, D., Illian, J. B., Lindgren, F., Sørbye, S. H. & Rue, H. (2015), ‘Going off grid: Computationally efficient inference for log-Gaussian Cox processes’, _Biometrika_ **103** (1), 49–70. 

- Sports Reference LLC (n.d.), ‘Calculating PER’. 

   - **URL:** _https://www.basketball-reference.com/about/per.html_ 

28 


