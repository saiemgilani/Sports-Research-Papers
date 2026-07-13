<!-- source: Route Identification in the National Football League.pdf -->

ROUTE IDENTIFICATION IN THE NATIONAL FOOTBALL LEAGUE 

## A PREPRINT 

**Dani Chu**<sup>_∗_</sup> **Matthew Reyers**<sup>_†_</sup> Department of Statistics & Actuarial Sciences Department of Statistics & Actuarial Sciences Simon Fraser University Simon Fraser University Burnaby, BC V5A 1S6 Burnaby, BC V5A 1S6 `dani_chu@sfu.ca matthew_reyers@sfu.ca` 

## **James Thomson** 

Department of Statistics & Actuarial Sciences Simon Fraser University Burnaby, BC V5A 1S6 `james_thomson_2@sfu.ca` 

## **Lucas Wu** 

Department of Statistics & Actuarial Sciences Simon Fraser University Burnaby, BC V5A 1S6 `yifan_wu@sfu.ca` 

August 8, 2019 

# **ABSTRACT** 

Tracking data in the NFL is a sequence of spatial-temporal measurements that vary in length depending on the duration of the play. In this paper, we demonstrate how model-based curve clustering of observed player trajectories can be used to identify the routes run by eligible receivers on offensive passing plays. We use a Bernstein polynomial basis function to represent cluster centers, and the Expectation Maximization algorithm to learn the route labels for each of the 34,698 routes run on the 6,963 passing plays in the data set. We go on to suggest ideas for new potential receiver metrics that account for receiver deployment. The resulting route labels can also be paired with film to enable streamlined queries of game film. 

**_K_ eywords** Model-based curve clustering _·_ Route identification _·_ Functional data _·_ Expectation Maximization algorithm 

# **1 Introduction** 

Curve clustering is the process of finding a latent class structure for observations of functional data and has wide applications across industries such as biology, finance and environmental science [Aghabozorgi et al., 2015]. Many methodologies have been developed to deal with such data [Dong et al., 2018]. These methodologies fall into four main methods; shape-based, compression based dissimilarity, feature based, and model-based clustering [Aghabozorgi et al., 2015]. 

This paper will focus on a model-based route clustering methodology using Gaussian mixture methods. These have been used in previous literature to cluster gene expression [McNicholas and Murphy, 2010], recognize Arabic characters [AlShaher, 2018], and distinguish regions based on temperature data [Bouveyron and Jacques, 2011]. In sport literature, model-based clustering has been used to cluster swimming progression in competition [Leroy et al., 2018], and in basketball to cluster player trajectories in the National Basketball Association (NBA) [Miller and Bornn, 2017]. 

The player trajectory data used by Miller and Bornn has been available to NBA teams since 2013 [Nba, 2013]. Similar data has recently been made available in the NFL by Next-Gen Stats and affiliate organizations [Nfl, 2019]. The player tracking data in the NFL is collected differently than in the NBA, utilizing a chip in the shoulder pads of players for the entirety of collection rather than computer vision tools. Although the data is collected in different ways, the player tracking data is fundamentally the same and allows for analysts in each sport to identify player movement over time. Capturing these insights has proven valuable in the NBA - leading the NFL to pursue the same approach. 

> _∗_ `https://danichusfu.github.io/` 

> _†_ `https://matt-reyers.netlify.com/` 

A PREPRINT - AUGUST 8, 2019 

For this reason, the NFL hosted the inaugural NFL Big Data Bowl, a competition that released player tracking data to the public for the first time, in January of 2019 to help teams gain insights from this data. Previous work in football had relied on play-by-play event data which was popularized and made readily available by the nflscrapr package [Horowitz et al., 2018] for the R Project for Statistical Computing. This led to work such as Expected Points Added, Win Probability Added, and Wins Above Replacement models in football [Yurko et al., 2019] which had already been readily available in sports such as golf [Broadie, 2011], basketball [Stern, 1994] and baseball [Baumer et al., 2013]. 

The data used in the NFL Big Data Bowl was NFL Next-Gen Stats tracking data which was gathered by Zebra Technologies and Wilson Sporting Goods through the use of radio-frequency identification (RFID) chips. These chips measure the field position (x, y) of each player and the ball at ten equally spaced points per second. Key events are listed at the moment they occur, such as a snap, a tackle, or a fumble. Using this information, the shape of each route run by every receiver can be considered a finite function, with a known start and ending point. 

## **1.1 Routes in the NFL** 

A route in football is the path or pattern that an eligible receiver runs on a passing play. Coaches and quarterbacks plan the route for every eligible receiver prior to the start of the play. In some cases receivers may have an option to run one of many predetermined routes where they decide on the specific route to run based on how the defense is set up. These are called option routes. Additionally, the predetermined routes are subject to change. A quarterback can communicate to his receivers new routes before the play begins or a receiver can make an adjustment while running the route. 

Football teams of all levels dedicate staff to tagging videos with the routes run by receivers on passing plays. Doing so is long and tedious work but it allows teams to query plays that meet certain search criteria. For example, to prepare for a playoff game, a coach may want video of all plays where a specific team has receivers run a three route combination including a flat, in, and post route. The same coach may want to evaluate his own team’s success in all plays involving receivers on the same side of the field that run an out route and a go route. Further, a defensive back in preparation for a marquee match-up with a top wide receiver may want to watch film of all the plays where that wide receiver ran a post route. 

With the new player tracking data and the long amount of hours spent tagging film, the automated detection and labeling of routes is of interest to football teams. It is of specific interest to not just detect and label these routes, but to be able to identify the known patterns that exist within the NFL. Although not restricted as a set, a relatively well defined route tree exists in which many realized routes are variations of with the addition of in-play noise. Capturing this structure within the data would lend validity to the utilized method and provide a direct use case for the NFL and its affiliate organizations. Before the availability of this player tracking data, attempts were made to use computer vision and machine learning to identify routes and formations from game film [Ajmeri and Shah, 2012]. Now that the NFL offers tracking data, machine learning techniques have been instead focused on route identification through feature based supervised learning techniques [Hochstedler and Gagnon, 2017]. 

We propose using a model-based unsupervised learning approach to clustering routes using the new player tracking data. We will implement this by using Bézier curves to define cluster means and then learn the cluster parameters and membership probabilities using the Expectation-Maximization algorithm. We will then label the clusters and provide direction for the use of these labels in further analysis. 

Labelling the routes run on a given play provides the information needed for a more nuanced analysis of receiver play in the NFL. Statistics like targets over expectation and air yards over expectation require information about receiver deployment on passing plays. Automating this labelling will help save hundreds of manual labour hours tagging plays and make querying plays of interest easier. 

This sharing of ideas and methodologies across sports and industries leads us to present our route identification methods for routes in the NFL. 

# **2 Bernstein Basis & Bézier Curves** 

In pursuing a model-based approach to clustering routes, we will make specific use of Bézier curves. First established by Pierre Étienne Bézier, these curves are capable of representing complicated "free-form" shapes of infinite points. The fundamentals of this approach originate in Bernstein basis polynomials [N. Bernstein, 1911]. The connection between Bernstein Basis Polynomials and Bézier curves is straightforward. First, we can define the basis polynomials for a degree _P_ on _t ∈_ [0 _,_ 1] by 



2 

A PREPRINT - AUGUST 8, 2019 

Extending these polynomials to the Bézier setting is then done through applying a weight to each term of the polynomial, called control points, by 



with control points **_θ_** 0 _, . . . ,_ **_θ_** _P_ . The output for a given input _t_ , given the control points **_θ_** , are the coordinates of the corresponding point on the Bézier curve. The collection of outputs over the inputs _t_ then forms the Bézier curve. 

Bézier curves are parametric curves and are easy to implement. They generalize well to higher dimensions and make for an excellent general tool. Though their application has been extensively explored in computer graphics, groundwork has been started with player tracking data in the NBA [Miller and Bornn, 2017]. It is worth noting that a desirable property of these Bézier curves is that they naturally handle the comparing of routes that differ in duration. We will rely on this property frequently due to the variability in duration of NFL routes. Our work will look to expand this introductory work into the NFL for receiver routes. 

# **3 Fitting Bézier Curves** 

Adapting the work of [Gaffney, 2004], let **Y** be a set _n_ observed player trajectories, _{_ **y** 1 _, . . . ,_ **y** _n}_ . Each observed curve _yi_ has _mi_ observations along its trajectory. These points describe the location at each observed time in two dimensional space. Therefore, _yi_ is a _mi ×_ 2 matrix. 

Each observed trajectory is measured at times **t** _i_ . We assume that each curve can be described by a Bézier curve with degree _P_ , defined by **_θ_** , which is a ( _P_ + 1) _×_ 2 matrix, and an additive Gaussian error term **_ϵ_** _i_ , a _mi ×_ 2 matrix. The _j_ th term of **_ϵ_** _i_ is _ϵij ∼N_ ( **0** _, σ_<sup>2</sup> **I** ), and _ϵij, σ_<sup>2</sup> which are both 1 _×_ 2 matrices ( _i_ = 1 _,_ 2 _, . . . , n_ , _j_ = 1 _,_ 2 _, . . . , mi_ ). 

Since each trajectory can be described by a Bézier curve we are using a Bernstein polynomial basis expansion where the control points are the coefficients or weights to the basis function. To fit the control points of a Bézier curve, consider the form of Equation (2). The structure of this equation is similar to a regression model. Using this as motivation, we can then naturally summarize the relationship between time points and control points with the following regression equation: 



The regression matrix, **T** _i_ , has dimension _mi ×_ ( _P_ + 1) and is evaluated at _tij_ , where _tij ∈_ [0 _,_ 1]. 

The fitting of Bézier curves can then be seen as equivalently fitting a multivariate linear regression. 



Now that we have the tools to fit a Bézier curve we will discuss how we use these curves to define cluster means and how to calculate how well an observed trajectory fits to a Bézier curve. 

# **4 Model Based Curve Clustering** 

Assuming any route run by a player approximates one of the finite predefined routes, the goal of our work then becomes to try and classify each observed route as a realization of one of the existing predefined routes. This is equivalent to clustering the _n_ routes into _K_ clusters, which we will refer to as labeling the route. Labeling will be done iteratively with labels updated at each step. As such, we let **z** = ( _z_ 1 _, . . . , zn_ ) be the current label of a given route, such that _zi ∈{_ 1 _, . . . , K}_ . Our assumption claims that there exists some correct set of labels **z** _∗_ for our collection of routes. 

The regression matrix defined in (4) can be used to define the conditional Probability Density Function (PDF) of **y** _i_ given **ti** as _f_ ( **yi** _|_ **ti** ) = _N_ ( **y** _i|_ **T** _i_ **_θ_** _, σ_<sup>2</sup> **I** ). Now we can consider a mixture of _K_ of these conditional distributions. Then the probability of observing the _i_<sup>th</sup> curve can be defined as: 



3 

A PREPRINT - AUGUST 8, 2019 

where _αk_ is the mixing weights of the _k_<sup>th</sup> cluster, and<sup>�</sup><sup>_K_</sup> _k_ =1<sup>_αk_= 1.The log-likelihood of observing all</sup><sup>_n_curves is</sup> then defined as the log of the product of the probability of observing each curve. Which in turn is the sum over all the curves of the log of the probability of observing the curve: 



We have that _zi_ is the cluster membership for curve _i_ . Then the joint density of **y** _i_ and _zi_ is 



This leads us to use the Expectation Maximization (EM) Algorithm introduced by Dempster [Dempster et al., 1977] to learn the Maximum Likelihood Estimates (MLE) for a model with a latent variable. The algorithm consists of three steps: Initialization, Expectation, and Maximization. 

We will first discuss here the general process for the Expectation and Maximization steps. We will discuss the specifics of the data pre-processing and initialization procedure in the next section. 

## **4.1 Expectation Step** 

In this step, the current estimates are used to evaluate the conditional expectation. Based on Bayes’ rule, the membership probability _πik_ that the _i_<sup>th</sup> curve was generated from cluster _zi_ is defined as 



It can be calculated by computing the probability that the _i_<sup>th</sup> curve is generated from cluster _k_ 



which is the product of the the probability of generating each _mi_ observed points on the curve from cluster _k_ . 



With regards to implementation, the heaviest computational part of calculating _πik_ is computing _N_ ( **y** _ij|_ **T** _ij_ **_θ_** _k, σk_<sup>2</sup><sup>**I**)</sup> for every observed point. In practice, this calculation is performed in parallel in order to efficiently implement the algorithm. 

## **4.2 Maximization Step** 

The updates rules for the parameters **_θ_** _k, σk_<sup>2</sup><sup>_, αk_are found by maximizing the log-likelihood.</sup><sup>_α_ˆ</sup><sup>_k_is the mean posterior</sup> probability that the _i_<sup>th</sup> curve was generated from cluster _zi_ , and _πik_ is obtained from the E-step: 



**_θ_** ˆ _k,_ ˆ _σk_<sup>2are found through weighted least squares where the weights matrix</sup><sup>**W**</sup><sup>_k_is a diagonal matrix with the diagonal</sup> elements the elements of the vector **w** _k_ , defined as 



This leads to the following weighted least squares solutions (see for example [Gaffney, 2004], [Chamroukhi, 2013], [Faria and Soromenho, 2010]) 



Since we have assumed the variance covariance matrix of the Normal distribution is diagonal we take only the diagonal elements of _σ_ ˆ _k_<sup>2.</sup> 

In practice, the parameters **_θ_**<sup>ˆ</sup> _k_ and _σ_ ˆ _k_<sup>2for different clusters can be computed in parallel and the</sup><sup>**W**</sup><sup>_k_matrices can be</sup> stored as sparse matrices. This gives performance improvements when the number of clusters gets large. 

We repeat the E and M steps until the change in log likelihood reaches a pre-defined tolerance (10<sup>_−_6</sup> in our case). 

4 

A PREPRINT - AUGUST 8, 2019 

# **5** 

## **5.1 NFL Tracking Data** 

The data has a play ID variable that contains all players positional and directional data within each play. There is an event variable indicating the start, end, and key moment within each play. These events can be easily pulled from the data to identify the play ID for each passing play, which contains the corresponding position of each player on the field for the play’s duration. We only looked at those events indicating a pass was attempted (6963 plays). Additionally only trajectories of offensive players who play Wide Receiver, Tight End, Running Back, or Full Back are analyzed (33967 trajectories). While other players can be eligible receivers we have no clear way of identifying them in the data. 

## **5.2 Pre-processing** 

We now perform 3 transformations to the trajectory data. 

1. **Cut Trajectories** : Each player trajectory in its raw form starts before the event “ _ball snap_ ”, and continues until the play is over, indicated by a number of possible events defined in the appendix. We only consider trajectory data beginning from when the ball is snapped, and ending when the play is over; the rest is cut from our analysis. The shift before the snap is outside the scope of this paper. 

2. **Standardize to Line of Scrimmage and Play Direction** : Since offensive plays start at varying distances from the target end zone, and the target end zone shifts for a given team every quarter; trajectories that represent similar routes will appear to be different x y space. Therefore we move all routes to a common line of scrimmage and orient player trajectories so that all routes are moving towards a common end zone. 

3. **Flip Trajectories** : We would expect any route run from one side of the quarterback to be approximately the mirror of the same route run from the other side (see Figure 3). All receiver routes are flipped to start from the same side of the quarterback, and translated to a single point of origin (see Figure 1) 

These pre-processing steps make it easier to identify common patterns and route labels. A shallow "in" route should look approximately the same now regardless of who ran it, and from where on the field they started from at the snap. 

These simplifications make it easier to identify common patterns and route labels. An example of what the pre-processed data looks like is available in Figure 1. After the clustering process we use the features of the non-transformed data for further investigation. 

## **5.3 Initialization** 

Finally, in order to run the EM algorithm we need initial values for the curve centers. We determine these curve centers by assigning each observed curve to an initial cluster and then calculating initial control points, variance parameters, and cluster weights based on the curves in each cluster. 

We use k-means clustering on the last observed point on each observed trajectory to use for the initialization of the cluster centers. This is a sensible idea since each trajectory has already been transformed to start at the same point, so much of the information about what route was run on the play is available in the last observed point. 

This is implemented on _K_ = 30 clusters. After getting our initial weights and parameters, the EM algorithm is run for four steps. Unfortunately the data does not include the true route run by each player, so labelling the curves was done manually. 

## **5.4 Implementation** 

We implemented the curve clustering algorithm on the data for _K_ = 30 clusters. This data consists of 33,967 routes from 6,963 passing plays. In total there are 1,438,133 measurements for an average of 42 measurements per route. 

We used a computer with 8 CPUs and 52 GB of RAM. On average each Expectation step takes 1,910 seconds and each Maximization step takes 19 seconds. We run the algorithm for 4 steps. The log likelihood at each step is -6090879, -6077207, -6069274, -6064259. The total run time was 7,745 seconds. 

## **5.5 Route Labelling** 

We have identified routes with similar structure but it is now our goal to add football context to our work by labelling the clusters. The cluster means obtained from our curve clustering process resemble those of route trees in football see 

5 

A PREPRINT - AUGUST 8, 2019 

Figure 3. We use labels provided by Ben Minaker formerly of the Simon Fraser University Football Team to manually label the mean curve of each cluster. Some clusters end up representing similar routes so we end up condensing the 30 clusters into 12 route groups. These route groups can be plotted back in “football space” and are displayed in Figure 5. This then leads us to perform brief sanity checks that our labelling process worked. In Figure 6 we can compare the route distribution across positions. Despite, the algorithm having limited indicators of a player’s position the routes assigned to each position align with our intuition of player positions. Finally, we can look at very basic trends about route usage. For example we could look at Figure 7 to see which players run which routes most often or Figure 8 to see which 3 WR design play concepts are run most often. These plots provide basic information provided by our labelled routes. However, we believe that there is much more that can be discovered by using route labels in analysis. We have implemented basic versions of them but leave it to future work to develop them fully. 

# **6 Future Work** 

There are 2 main directions for future work in this space. The first is to improve the clustering process. One way in which this can be achieved is by improving the computational efficiency of the clustering process. This would allow for more clusters to be fit. We’ve considered that perhaps clustering based on derivatives and second derivatives of the position vectors may yield improved results. A major drawback is the ability to identify a comeback vs. a go route as the functions look nearly identical to our clustering algorithm. Derivatives of the function will show velocity over time, and second derivatives acceleration. Finally, there are more complex models in [Gaffney, 2004] that may yield better clustering results. 

The second is to augment the analysis of football players. As mentioned in the previous section, we see major opportunities to use these labelled routes to understand and account for player usage across receiver statistics. 

Additionally, the results obtained thus far cannot be proven to work without knowing the true route name for each of the passing plays in our data set. Our only method for checking the results is to compare to our intuition of player tendencies. In the future we hope to work with teams to calibrate our algorithm for accuracy route labelling. 

## **6.1 Potential Uses** 

The automated labelling of routes provides potential avenues for more in depth analysis, e.g. with labelled routes on each play we can build models to understand player deployment, receiver statistics that account for usage [Rossler, 2019], and build better defensive statistics for coverage players. 

We can calculate statistics like type of route run over expectation per 100 plays (see Figure 9) to understand player usage compared to an average player while accounting for position and game situation. These can then be further used to cluster players based on their usages above expectation of an average player. This can then be extended to replicate the work of [Rossler, 2019] to compute targets over expectation for various wide receivers. This can be broken down in a number of different ways. In Figure 10 we break down Targets Over Expectation by 4 different routes to see which receivers are being targeted more often then expected on specific route types. This methodology can be extended to the concept of Air Yards. As provided in [Horowitz et al., 2018], Air Yards can be used to contextualize and quantify receiving opportunities. We plot in Figure 11 the top players for Air Yards Over Expectation per 100 Routes from a preliminary model. As we have demonstrated briefly here there is a large array of applications that can use route labels. One that we did not provide an example for is improving the evaluation of defensive players. The labelling of routes from tracking data is therefore valuable for further analysis as it is for automated film tagging. 

# **7 Conclusion** 

In this work we demonstrate a method for labelling routes for player trajectory data of varying lengths in the National Football League. We do so by using a model based clustering approach and the Expectation Maximization algorithm. The probabilistic model works as a mixture of Gaussian distributions centered at Bézier curves. This provides the potential to understand player usages, efficiencies, and improve defensive evaluation. 

# **8 Acknowledgements** 

We would like to thank Coco Liu, Barinder Thind and Cherlene Lin for their helpful discussions around the EM algoirthm and functional data analysis, Michael Couture and Ben Minaker for their help with football interpretations and Tim Swartz for his guidance and supervision. To the developers of the tidyverse family of packages [Wickham, 2017] without which we would not have been able to perform this research. We would also like to thank the football analytics 

6 

A PREPRINT - AUGUST 8, 2019 

community on twitter for their support and guidance throughout this project. Finally, we wanted to thank Michael Lopez and the NFL for hosting this competition and giving us this opportunity. 

# **References** 

- [Aghabozorgi et al., 2015] Aghabozorgi, S., Shirkhorshidi, A. S., and Wah, T. Y. (2015). Time-series clustering – a decade review. _Information Systems_ , 53:16–38. 

- [Ajmeri and Shah, 2012] Ajmeri, O. and Shah, A. (2012). Using computer vision and machine learning to automatically classify nfl game film and develop a player tracking system. In _Proceedings of the 2012 MIT Sloan Sports Analytics Conference_ . 

- [AlShaher, 2018] AlShaher, A. A. (2018). Arabic character recognition using regression curves with the expectation maximization algorithm. _International Journal of Computer, Electrical, Automation, Control and Information Engineering_ , 12(12):1087–1091. 

- [Baumer et al., 2013] Baumer, B., Jensen, S., and Matthews, G. (2013). Openwar: An open source system for evaluating overall player performance in major league baseball. _Journal of Quantitative Analysis in Sports_ , 11. 

- [Bouveyron and Jacques, 2011] Bouveyron, C. and Jacques, J. (2011). Model-based clustering of time series in group-specific functional subspaces. _Advances in Data Analysis and Classification_ , 5(4):281–300. 

- [Broadie, 2011] Broadie, M. (2011). Assessing golfer performance on the pga tour. _Interfaces_ , 42. 

- [Buccaneers.com, 2015] Buccaneers.com (2015). Red chalk talk: Route tree (3 of 4). [Online; posted 30-August-2015]. 

- [Chamroukhi, 2013] Chamroukhi, F. (2013). Robust em algorithm for model-based curve clustering. _arXiv e-prints_ , page arXiv:1312.7022. 

- [Dempster et al., 1977] Dempster, A. P., Laird, N. M., and Rubin, D. B. (1977). Maximum likelihood from incomplete data via the em algorithm. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 39(1):1–38. 

- [Dong et al., 2018] Dong, J. J., Wang, L., Gill, J., and Cao, J. (2018). Functional principal component analysis of glomerular filtration rate curves after kidney transplant. _Stat Methods Med Res_ , 27(12):3785–3796. 

- [Faria and Soromenho, 2010] Faria, S. and Soromenho, G. (2010). Fitting mixtures of linear regressions. _Journal of Statistical Computation and Simulation_ , 80(2):201–225. 

- [Gaffney, 2004] Gaffney, S. (2004). _Probabilistic Curve-Aligned Clustering and Prediction with Mixture Models_ . PhD thesis, University of California, Irvine. 

- [Hochstedler and Gagnon, 2017] Hochstedler, J. and Gagnon, P. T. (2017). American football route identification using supervised machine learning. In _Proceedings of the 2017 MIT Sloan Sports Analytics Conference_ . 

- [Horowitz et al., 2018] Horowitz, M., Yurko, R., and Ventura, S. (2018). _nflscrapR: Compiling the NFL Play-by-Play API for easy use in R_ . R package version 1.8.1. 

- [Leroy et al., 2018] Leroy, A., MARC, A., DUPAS, O., REY, J. L., and Gey, S. (2018). Functional data analysis in sport science: Example of swimmers’ progression curves clustering. _Applied Sciences_ , 8(10):1766. 

- [McNicholas and Murphy, 2010] McNicholas, P. D. and Murphy, T. B. (2010). Model-based clustering of microarray expression data via latent gaussian mixture models. _Bioinformatics_ , 26(21):2705–2712. 

- [Miller and Bornn, 2017] Miller, A. C. and Bornn, L. (2017). Possession sketches : Mapping nba strategies. In _Proceedings of the 2017 MIT Sloan Sports Analytics Conference_ . 

- [N. Bernstein, 1911] N. Bernstein, S. (1911). Démonstration du théorème de weierstrass fondée sur le calcul des probabilités. _Communications de la Société Mathématique de Kharkov 2_ , 13. 

- [Nba, 2013] Nba (2013). Nba partners with stats llc for tracking technology. [Online; posted Sep 5, 2013]. 

- [Nfl, 2019] Nfl (2019). Nfl next gen stats. https://operations.nfl.com/the-game/technology/nfl-next-gen-stats/. Accessed: 2019-04-23. 

- [Rossler, 2019] Rossler, B. (2019). Introducing targets above expectation. 

- [Stern, 1994] Stern, H. S. (1994). A brownian motion model for the progress of sports scores. _Journal of the American Statistical Association_ , 89(427):1128–1134. 

- [Wickham, 2017] Wickham, H. (2017). _tidyverse: Easily Install and Load the ’Tidyverse’_ . R package version 1.2.1. 

- [Yurko et al., 2019] Yurko, R., Ventura, S., and Horowitz, M. (2019). nflwar: a reproducible method for offensive player evaluation in football. _Journal of Quantitative Analysis in Sports_ . 

7 

A PREPRINT - AUGUST 8, 2019 

# **List of Figures** 

|1|A sample of 500 transformed curves according to our pre-processing steps . . . . . . . .|. . . . . . .<br>9|
|---|---|---|
|2|Cluster Means for 30 Clusters<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>10|
|3|Example of a Route Tree [Buccaneers.com, 2015].<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>11|
|4|Route tree (a) when compared to the results of the clustered means (b) . . . . . . . . . .|. . . . . . .<br>12|
|5|Labelled cluster means plotted with respect to the pre-transformed space . . . . . . . . .|. . . . . . .<br>13|
|6|Routes per Position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>14|
|7|Players who run the most of each route . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>15|
|8|3 WR Designs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>16|
|9|RB Routes Run Over Expectation per 100 Plays . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>17|
|10|Targets Over Expectation per 100 of each Route by Route . . . . . . . . . . . . . . . . .|. . . . . . .<br>18|
|11|Air Yards Over Expectation per 100 Routes . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>19|



8 

A PREPRINT - AUGUST 8, 2019 



Figure 1: A sample of 500 transformed curves according to our pre-processing steps 

9 

A PREPRINT - AUGUST 8, 2019 



Figure 2: Cluster Means for 30 Clusters 

10 

A PREPRINT - AUGUST 8, 2019 



Figure 3: Example of a Route Tree [Buccaneers.com, 2015]. 

11 

A PREPRINT - AUGUST 8, 2019 





Figure 4: Route tree (a) when compared to the results of the clustered means (b) 

12 

A PREPRINT - AUGUST 8, 2019 



Figure 5: Labelled cluster means plotted with respect to the pre-transformed space 

13 

A PREPRINT - AUGUST 8, 2019 



Figure 6: Routes per Position 

14 

A PREPRINT - AUGUST 8, 2019 



Figure 7: Players who run the most of each route 

15 

A PREPRINT - AUGUST 8, 2019 



Figure 8: 3 WR Designs 

16 

A PREPRINT - AUGUST 8, 2019 



Figure 9: RB Routes Run Over Expectation per 100 Plays 

17 

A PREPRINT - AUGUST 8, 2019 



Figure 10: Targets Over Expectation per 100 of each Route by Route 

18 

A PREPRINT - AUGUST 8, 2019 



Figure 11: Air Yards Over Expectation per 100 Routes 

19 


