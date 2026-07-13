<!-- source: SEAM methodology for context-rich player matchup evaluations.pdf -->

# SEAM methodology for context-rich player matchup evaluations 

### Charles Young, David Dalpiaz, Daniel J. Eck 

### May 19, 2020 

#### **Abstract** 

We develop the SEAM (synthetic estimated average matchup) method for describing batter versus pitcher matchups in baseball, both numerically and visually. We first estimate the distribution of balls put into play by a batter facing a pitcher, called the spray chart distribution. This distribution is conditional on batter and pitcher characteristics. These characteristics are a better expression of talent than any conventional statistics. Many individual matchups have a sample size that is too small to be reliable. Synthetic versions of the batter and pitcher under consideration are constructed in order to alleviate these concerns. Weights governing how much influence these synthetic players have on the overall spray chart distribution are constructed to minimize expected mean square error. We then provide novel performance metrics that are calculated as expectations taken with respect to the spray chart distribution. These performance metrics provide a context rich approach to player evaluation. Our main contribution is a Shiny app that allows users to evaluate any batter-pitcher matchup that has occurred or could have occurred in the last five years. One can access this app at `https://seam.stat.illinois.edu/app/` . This interactive tool has utility for anyone interested in baseball as well as team executives and players. 

## **1 Introduction** 

Baseball has a rich statistical history dating back to the first box score created by Henry Chadwick in 1859. Fans, journalists, and teams have obsessed over baseball statistics and performance metrics ever since. This passion with baseball statistics is best summarized by the existence of Schwarz [2004], a best selling book devoted entirely to the statistical history of baseball. Baseball data is analyzed in the classroom as well. Max Marchi, Jim Albert, and Benjamin S. Baumer have written a book that teaches R through baseball analysis [Marchi et al., 2019], and Jim Albert maintains an actively updated website Exploring Baseball Data with R that supplements this book. Quantification of players’ skill has appeared in the Statistics literature, with articles devoted to hitting [Berry et al., 1999, Albert, 2008, Brown, 2008, Jensen et al., 2009a], pitching [Albert, 2006, Shinya et al., 2017], fielding [Jensen et al., 2009b, Piette and Jensen, 2012], and total value [Baumer et al., 2015]. 

Most baseball statistics used for player evaluations are obtained from raw box score totals. While box score totals are an enjoyable statistical summary for baseball fans and analysts, the information contained in them is not very substantive. They ignore rich contextual information. Most commonly used player evaluation metrics are functions of context-free box score totals. These include, and are far from limited to, adjusted earned run average (ERA+), adjusted on base plus slugging percentage (OPS+), weighted runs created plus (wRC+), and wins above replacement (WAR) [Baseball-Reference, 2020, Fangraphs, 2020]. More sophisticated techniques in Berry et al. [1999], Brown [2008], Jensen et al. [2009a], and Baumer et al. [2015] also constructed methodology grounded in raw box score totals. While many of these tools account for some contextual information such 

1 

as ball parks, position of a player, and a player’s age, they ignore opponent strength. Eck [2020] showed that context-free metrics and the class of metrics that compares a player’s accomplishments directly with that player’s peers are ill-equipped for player comparisons across eras of baseball, although they may perform well over the course of a single season or a few consecutive seasons. That being said, these context-free metrics do not offer any guidance for how any particular batter will perform against a particular pitcher, the most important and relevant outcome in baseball. Furthermore, baseball outcomes have been assumed to be independent and identically distributed (iid) realizations in the literature [Brown, 2008, Jensen et al., 2009a]. The iid assumption of outcomes may be reasonable in the prediction contexts of Brown [2008] and Jensen et al. [2009a] that involve long time frames, but this assumption is not appropriate for small time frames when the variability in quality of batter and pitcher characteristics can be very large. 

In this article we develop spray chart distributions as a methodology for understanding batterpitcher matchups visually and numerically. Informally, spray chart distributions are 2-dimensional contours that overlay spray charts [Petti, 2009, Marchi et al., 2019]. We construct spray chart distributions for batter-pitcher matchups where separate batter spray chart distributions are constructed for each of the pitches that the pitcher throws. Rich pitch characteristic information is used to supplement labelled pitch type data since the velocity, trajectory, movement characteristics, and release points of a pitch exhibit large variation across pitchers. The reported spray chart distribution for the batter pitcher matchup is the aggregation of the spray chart distributions for each pitch that the pitcher throws. The aggregation is with respect to the percentage that the pitcher throws each pitch. The density functions corresponding to these spray chart distributions are estimated nonparametrically using the `kde2d` function in the `MASS` R package [Ripley et al., 2019]. 

One concern with this approach is the potential sparsity of batter-pitcher matchup data. We alleviate this concern with the development of synthetic batters and pitchers with similar characteristics as the batter and pitcher under study. Our synthetic player creation methodology is inspired by the notion of similarity scores [James, 1994, Silver, 2003]. However, unlike the similarity scores presented in James [1994] and Silver [2003], we construct similarity scores using a nearest neighbor approach that is based on the underlying batter and pitcher characteristics of the players under study instead of observed statistics. The pitcher characteristics are averages of the velocity, trajectory, movement, and release point of pitches thrown. The batter characteristics are averages of launch angle, exit velocity, spray angle, and binned batted ball location information. These player characteristics are obtained from Statcast [Baseball, 2014] scraped using functionality in the `baseballr` R package [Petti et al., 2020], and reflect the underlying talent and tendencies of players. For each batter-pitcher matchup we estimate three spray chart densities, the first is the natural spray chart density corresponding to the players under study, the second is the spray chart of the synthetic pitcher versus the original batter, and the third is the spray chart of the original pitcher versus the synthetic batter. We report a synthetic spray chart density which is a weighted average of these spray chart densities. The weights are chosen with the aim of minimizing mean squared error. 

The main contribution of this work is a Shiny app which gives users the ability to display the synthetic spray chart distribution for any batter pitcher matchup that has occurred or could have occurred in the last five years, the years that Statcast data exists. These synthetic spray charts are visualized over an image of a representative baseball field so that the batted ball distribution is displayed to give proper context. We also report performance metrics that are computed as expectations with respect to the synthetic spray chart distribution. The expected number of singles, doubles, triples, home runs are reported. The expected batting average on balls in play (xBABIP) and the expected bases on contact (xBsCON) are also reported. These matchup dependent metrics 

2 



Figure 1: The layout of the application upon submission. 

allow for any user to assess the expected performance of batters and pitchers when they face each other. 

## **2 Motivating Example** 

In this section we present a snapshot of what our Shiny app offers users. The Shiny app is available at `https://seam.stat.illinois.edu/app/` . The default matchup in the application pairs the reigning American League Cy Young winner Justin Verlander against the reigning American League MVP Mike Trout. The layout includes a sidebar with four filters: two dropdowns for batter/pitcher selection and two sliders for metric adjustment. A snapshot of the appearance of our visualization is depicted in Figures 1 and 2. 

The pitcher slider allows users to determine the relative importance of “stuff”, a colloquial term for pitch quality, versus release information. Stuff includes velocity, spin rate, and movement. Release includes release angles and release point. The batter slider allows users to determine the relative importance of launch conditions versus batted ball locations. Launch conditions includes exit velocity and launch angle. Location includes pull%, middle%, oppo% (the percentage of batted balls place into the corresponding thirds of a baseball field). The default setting of the pitcher slider favors stuff over release information. The logic for this is quality of pitches being more representative of ability than release point. The default setting of the batter slider favors quality of contact over batted ball tendencies which appears to bias the synthetic batter’s spray chart away from that of the batter under consideration. That being said, the batted ball tendencies are recorded as percentages of balls hit to six large grids on the baseball field, ignoring the quality, trajectory, and exact location of the batted ball. Thus, the quality of contact forms a more complete representation of a batter’s skill than tendency. 

As previously mentioned, these visualizations can help coaches position their fielders effectively. While a traditional spray chart may be useful in aggregate, building a custom spray chart to reflect a specific batter-pitcher matchup will yield more accurate results on a plate appearance by plate appearance level. This synthetically created spray chart will give the user an expected 

3 



Figure 2: Spray chart distributions constructed by our app. This example corresponds to the spray chart distribution when batter Mike Trout faces pitcher Justin Verlander. The top-left panel is the complete synthetic spray chart for the batter-pitcher matchup. The top-right panel is the traditional batter-pitcher spray chart distribution, with no consideration of similar players. The bottom-left panel is the synthetic batter’s spray chart distribution versus the real pitcher. The bottom-right panel is the real batter’s spray chart distribution versus the synthetic batter. 

distribution of batted balls for the batter-pitcher matchup based on a combination the distribution of similar batters against the pitcher, the distribution of similar pitchers against the batter, and any observations of pitcher vs batter since 2015. The app also displays two additional synthetic charts and a leaderboard displaying the most similar pitchers/batters. These include their overall similarity score and a variety of performance metrics. See Figure 3 for an example of the top 10 most similar pitchers to Justin Verlander. 

This matchup presents a good example of how to interpret the resulting spray charts. Trout seems to be a pull-heavy hitter in general according to his traditional chart. When facing pitchers similar to Verlander, he seems to push the ball the opposite way. This may be explained by Verlander’s high velocity fastball. In general, batters have a hard time “getting around” (pulling) an upper-90’s fastball, so they end up hitting the ball to the opposite field. Given this spray chart distribution, a coach may position the shortstop more towards third base, the second baseman more up the middle, and the first baseman more towards second base. This will protect against Trout’s usual habit of pulling the ball, and also put the first baseman in a position to cover the opposite field soft ground ball. If this decision were made just by Trout’s traditional chart, the first baseman might not have been moved to cover ground balls through the right side. 

## **3 Pitcher and batter characteristics** 

The data for our app was acquired via the `baseballr` R package [Petti et al., 2020]. This dataset contains every pitch thrown since 2015 that has been captured by Statcast. A few preprocessing steps are involved: 

- Pitches classified as Eephus, Knuckleball, and Screwball are removed since these pitch types 

4 



Figure 3: The most similar pitchers to Justin Verlander with an 85% stuff-to-release ratio 

are rare. 

- Pitches classified as Knuckle-Curve are renamed to Curveball. 

- Pitches classified as Forkball are renamed to Splitter. 

- Pitch launch angles are calculated using rudimentary kinematics: 



where _vxr_ , _vyr_ , _vzr_ are, respectively, the _x_ , _y_ , _z_ components of release velocity. 

- Batted ball locations are adjusted to reflect accurate baseball field coordinates [Petti, 2017]. 

- Spray angle is calculated from the x and y coordinates of the batted ball, and adjusted where a negative angle implies the ball was pulled. 

- Player characteristic data are standardized to have mean zero and standard deviation 1. The player characteristic data are physically dimensionless after standardization. 

For pitcher comparisons, pitchers are aggregated on a season and pitch type basis. The variables considered are: velocity, spin rate, horizontal break, horizontal release angle, horizontal release point, vertical break, vertical release angle, vertical release point, and extension. Averages of these variables are taken across each pitcher-pitch type combination. To be eligible for comparison, a pitcher must share at least _⌈_<sup>_n_</sup><sup><u>pitch</u></sup> 2 ~~t~~ <u>ypes</u> _⌉_ pitches with the pitcher under study. 

For batter comparisons, batters are aggregated on a season, handedness, and pitch type basis. The variables considered are: exit velocity, launch angle, pull%, middle%, and oppo%. Averages of these variables are taken across each batter-pitch type combination. 

5 

## **4 Spray chart distributions and densities** 

A spray chart distribution for a batter is a distribution _F_ over a bounded subset _Y ∈_ R<sup>2</sup> . The set _Y_ contains plausible locations of batted balls from home plate. Let (0 _,_ 0) _∈Y_ denote the location of home plate. With this specification we can take _Y_ = _{_ **y** _∈_ R<sup>2</sup> : _∥_ **y** _∥≤_ 1000 _}_ where values in _Y_ are locations in feet and _∥· ∥_ is the Euclidean norm. This specification of _Y_ guarantees that _F_ ( _Y_ ) = 1 for all batters in history. No human in history has ever come close to hitting a ball 1000 feet. 

Our main inferential goal will be to consider spray chart distributions that are conditional on several characteristics for pitchers **x** _p_ and batters **x** _b_ , where **x** = ( **x**<sup>_′_</sup> _p_<sup>_,_</sup><sup>**x**</sup> _b_<sup>_′_)</sup><sup>_′∈X_, and</sup><sup>_X_is assumed to</sup> be bounded. The conditional spray chart density function will be denoted as _f_ ( _·|_ **x** ) for all **x** _∈X_ . We will estimate _f_ ( _·|_ **x** ) with a multivariate kernel estimator 



where _K_ is a multivariate kernel function, **H** is a matrix of bandwidth parameters, and **y** 1 _, . . . ,_ **y** _n_ **x** are the _n_ **x** batted ball locations from home plate observed when the batter-pitcher matchup is encoded as **x** . The estimated spray chart density function (1) is a smoothed surface overlaying a spray chart. Our visualization of the spray chart distribution will be along _ng_ common grid points _g_ 1 _, . . . , gng_ for all batters and all conditional characteristics **x** _∈X_ under study. Commonality of grid of points across the batters and **x** allows for straightforward comparisons of spray chart distributions. 

Our implementation will estimate _f_ ( _·|_ **x** ) using the `kde2d` and `kde2d.weighted` functions in R [Ripley et al., 2019, Hamilton, 2018]. These functions are chosen because of their presence in the `ggplot2` R package [Wickham, 2016] which will be employed for visualization. Therefore, we estimate _f_ ( _·|_ **x** ) using a bivariate nonparametric Gaussian kernel density estimator 



where _φ_ is a standard Gaussian density, **h** _∈_ R<sup>2</sup> is a bandwidth parameter so that the matrix **H** in (1) is **H** = diag( **h** ), and ( _y_ 1 _i, y_ 2 _i_ ), _i_ = 1 _, . . . , n_ are the observed batted ball locations. In our application, **H** is chosen according to the default bandwidth selection procedures within the `kde2d` and `kde2d.weighted` functions. 

### **4.1 Synthetic player construction** 

We develop a method for synthetically recreating baseball players in order to alleviate the small sample size concerns of individual batter-pitcher matchups. Matchup data involving these synthetic players will then be included in our analysis to estimate the spray chart density function for individual batter-pitcher matchups. Our synthetic player is similar in spirit to similarity scores [James, 1994, Silver, 2003]. 

Our similarity score of pitcher _j_ to pitcher _k_ is _s_ ( **x** _p,j,_ **x** _p,k_ ) = exp( _−∥_ **x** _p,j −_ **x** _p,k∥_ **V** _p_ ) where **x** _p,j_ and **x** _p,k_ are, respectively, the underlying pitch characteristics for pitcher _j_ and _k_ , _∥_ **x** _p,j −_ **x** _p,k∥_ **V** _p_ = ~~�~~ ( **x** _p,j −_ **x** _p,k_ )<sup>_′_</sup> **V** _p_ ( **x** _p,j −_ **x** _p,k_ ) _,_ and **V** _p_ is a diagonal weight matrix that is chosen to scale the pitch characteristics and give preference to pitch characteristics that are chosen to have higher influence on the spray chart distribution under study. Similarity scores with exponential weighting have desirable theoretical properties that are explained in the appendix and in practice guards against downplaying the effect of the players under study. The user of our Shiny app has some control 

6 

of the entries of **V** _p_ by adjusting the pitcher slider. Similarity scores for batters are defined in a similar way. Implicit in this construction is the assumption that the underlying pitcher and batter characteristics that we collect are an exhaustive set of inputs to properly estimate the spray chart distribution. 

Our method for estimating spray chart densities for batter-pitcher matchups with synthetic players is as follows: first, without loss of generality, let **x** _p_ and **x** _b_ be the characteristics for the batter and pitcher under study so that **x** = ( **x**<sup>_′_</sup> _p_<sup>_,_</sup><sup>**x**</sup> _b_<sup>_′_)</sup><sup>_′_.Therewillbe</sup><sup>_J_pitchersand</sup><sup>_K_batters</sup> available to form the pool of players that we compare to the pitcher and batter under study. Then line up the batter and pitcher characteristics for all of the available players outside of those under study, **x** _b,j_ , _j_ = 1 _, ..., J_ and **x** _p,k_ , _k_ = 1 _, ..., K_ . Now obtain the similarity scores _sp,j_ = _s_ ( **x** _p,_ **x** _p,j_ ), _j_ = 1 _, ..., J_ and _sb,k_ = _s_ ( **x** _b,_ **x** _b,k_ ), _k_ = 1 _, ..., K_ . Now convert the similarity scores to weights _wp,j_ = _sp,j/_<sup>�</sup><sup>_J_</sup> _l_ =1<sup>_sp,l_and</sup><sup>_wb,k_=</sup><sup>_sb,k/_�</sup><sup>_K_</sup> _l_ =1<sup>_sb,l_.Thespraychartdensityforabatterfacingthe</sup> synthetic pitcher is 



The spray chart density for a pitcher facing the synthetic batter is 



It is clear that the above synthetic densities are biased in the population. We then estimate (3) and (4) with 



where we let _np,j_ denote the matchup sample size of pitcher _j_ versus the batter under study, _nb,k_ denote the matchup sample size of the pitcher under study versus batter _k_ , and **h** _p,j_ and **h** _b,k_ are bandwidth parameters. 

Our implementation estimates the densities in (5) with the `kde2d.weighted` function. The estimators (5) are obviously biased estimators for _f_ ( **y** _|_ **x** ). However, they have the potential to reduce MSE. One obvious case is when there exists weights _wp,j ≈_ 1, _wb,k ≈_ 1 and _np,j > n_ , _nb,k > n_ . In these settings, the players under study are almost perfectly replicated by another player in the available pool and this player has a larger number of matchups with the batter or pitcher under study. Another obvious case is when the batter has never faced the pitcher so that no data is available to estimate _f_ ( **y** _|_ **x** ) directly, although that does not guarantee that the estimators (5) are good estimators for _f_ ( **y** _|_ **x** ). Our implementation will estimate _f_ ( **y** _|_ **x** ) with 



where _λ, λp_ , _λb_ form a convex combination. Note that these calculations are conditional on the pitch characteristics which implies that they are also conditional on _wp,j_ and _wb,k_ since the weights are a deterministic function of the pitch characteristics. Our implementation will estimate the elements of **_λ_** as 



7 

where _np_ =<sup>�</sup><sup>_J_</sup> _j_ =1<sup>_s_2</sup> _p,j_<sup>_np,j_and</sup><sup>_nb_=�</sup><sup>_K_</sup> _k_ =1<sup>_s_2</sup> _b,k_<sup>_nb,k_.Informally,thesechoicesariseasabalance</sup> between the natural bias that exists in our synthetic player construction and the inherent estimation variation. In our application it is reasonable to take _np,j_ = _O_ ( _n_ ) and _nb,k_ = _O_ ( _n_ ) for all _j_ = 1 _, . . . , J_ and _k_ = 1 _, . . . , K_ . It is also reasonable to assume that _n_ will be too small to be of much use, hence the reason why _np_ and _nb_ are aggregated with respect to similarity scores instead of weights that form a convex combination. However, in the event that _n_ is large enough to provide reliable estimation of _f_ ( **y** _|_ **x** ) with _f_<sup>ˆ</sup> _h_ ( **y** _|_ **x** ), then _n_ dominates _np_ and _nb_ . Formal technical justification for selecting **_λ_** is given in the Appendix. In the Appendix we argue that our choices of **_λ_** lead to the estimator (6) having a lower MSE than the estimator (2). 

### **4.2 Performance metrics** 

We develop novel performance metrics that are theoretically computed as expectations with respect to the synthetic spray chart distribution estimated in the previous subsection. We estimate the expected number of singles, doubles, triples, and home runs that the batter hits versus the pitcher in a particular matchup. We also estimate the xBABIP and xBsCON as additional summary measures. The metric xBsCON is best interpreted as slugging percentage conditional on balls put into play. Our implementation will not estimate these expectations exactly as there is not enough historical batted ball data. 

To theoretically estimate these quantities we first obtain five years of batted ball data. We then estimate the proportion of batted balls that were either an out (O), single (1B), double (2B), triple (3B), or home run (HR) at locations **y** on the baseball field. Denote this vector of estimated� proportions at **y** as **P**<sup>�</sup> ( **y** ) = ( _p_ O( **y** ) _, p_ 1B( **y** ) _, p_ 2B( **y** ) _, p_ 3B( **y** ) _, p_ HR( **y** ))<sup>_′_</sup> _._ Next, we obtain _E_ ( **x** ) = � **P** ( **y** )ˆ _g_ **_λ_** ( **y** _|_ **x** ) _d_ **y** , where _E_<sup>�</sup> ( **x** ) = (ˆ _e_ O( **x** ) _,_ ˆ _e_ 1B( **x** ) _,_ ˆ _e_ 2B( **x** ) _,_ ˆ _e_ 3B( **x** ) _,_ ˆ _e_ HR( **x** ))<sup>_′_</sup> _._ Thus _E_<sup>�</sup> ( **x** ) is the estimated expected vector of outcomes where the expectation is taken with respect to the estimated spray chart distribution. Expected BABIP is then calculated as xBABIP = _e_ ˆ1B( **x** )+ˆ _e_ 2B( **x** )+ˆ _e_ 3B( **x** ) ˆ and xBsCON is calculated as xBsCON = _e_ 1B( **x** ) + 2ˆ _e_ 2B( **x** ) + 3ˆ _e_ 3B( **x** ) + 4ˆ _e_ HR( **x** ) _._ Our Shiny app also displays the floor of 100ˆ _e_ 1B( **x** ), 100ˆ _e_ 2B( **x** ), 100ˆ _e_ 3B( **x** ), and 100ˆ _e_ HR( **x** ). The 100 multiplier is a normalization that is intended for ease of interpretation. The previous paragraph outlines how we would calculate our performance metrics if we could obtain **P**<sup>�</sup> ( **y** ) for every **y** _∈Y_ . In reality, we do not have enough data available to achieve this task. Therefore, we calculate discretized versions of these performance metrics over 10 feet by 10 feet bins. 

## **5 Discussion** 

The primary contribution of this work is the development of synthetic spray chart distributions that are calculated under the hood of a Shiny app which provides users with visual and numeric summary measures of batter-pitcher matchups. This app will be of interest to baseball fans, analysts, players, and team executives alike. Our application shows users batter tendencies versus pitchers while providing summaries of their overall success or lack thereof. Our application greatly improves upon the inferential power of spray charts [Petti, 2009, Marchi et al., 2019] as a visualization of a batter’s hitting tendencies. Spray charts may be uninformative for individual matchups due to a lack of data. Our synthetic player construction alleviates this problem. 

We are not the first to incorporate additional players into an analysis via similarity scores with the understanding that doing so improves estimation performance. The PECOTA prediction methodology [Silver, 2003] tries to forecast the ability of players using aggregate estimates obtained from other similar players. To the best of our knowledge, we are the first to base similarity scores 

8 

exclusively on Statcast data which we believe provides a truer notion of similarity in the context of individual batter-pitcher matchups. 

There needs to be a clear distinction made that clarifies the goal of this study. The goal of this synthetic spray chart approach is to provide a system to estimate the position of a batted ball given a certain batter-pitcher matchup - it is **not** to gauge true talent. On average, players who hit the ball harder with a more optimized launch angle will receive better projected stats, since these balls tend to produce more home runs (and thus take fielders out of the equation.) Tools like speed and eye at the plate, therefore, will will not be reflected in this application. 

## **Acknowledgements** 

We would like to thank ATLAS Infrastructure and Illini Analytics for computational resources that made our Shiny app possible. We would also like to thank Alan Nathan, Jim Albert, James Balamuta, Dootika Vats, John Marden, and Dave Zhao for helpful comments that improved our article and our Shiny app. 

## **Appendix: Justification for our choice of** **_λ_** 

We now motivate **_λ_** theoretically. We first assume some additional structure on the space of functions that _f_ ( _·|·_ ) belongs to in order to facilitate our motivation. The best batters in baseball are good at hitting the ball with general intent but batted ball locations will still exhibit variation. Therefore we expect spray chart densities to be smooth and lacking sharp peaks. It is reasonable to assume that _f_ ( _·|·_ ) belongs to a multivariate H¨older class of densities which we will denote by _H_ ( _β, L_ ). The space _H_ ( _β, L_ ) is the set of functions _f_ ( **y** _|_ **x** ) such that 



for all **y** _,_ **y**<sup>_′_</sup> _∈Y_ , all **x** _,_ **x**<sup>_′_</sup> _∈X_ , and all **s** such that _|_ **s** _|_ = _β −_ 1 where _D_ **y**<sup>**s**=</sup><sup>_∂s_1+</sup><sup>_s_2</sup><sup>_/∂y_</sup> 1<sup>_s_1</sup><sup>_∂y_</sup> 2<sup>_s_2,</sup> _D_ **x**<sup>**t**=</sup><sup>_∂t_1+</sup><sup>_···_+</sup><sup>_tp/∂xt_</sup> 1<sup>1</sup><sup>_· · · ∂x_</sup> _p_<sup>_tp_and</sup><sup>_L_</sup> **x**<sup>_≤L_forall</sup><sup>**x**</sup><sup>_∈X_and</sup><sup>_L_</sup> **y**<sup>_≤L_forall</sup><sup>**y**</sup><sup>_∈Y_.Wewillassume</sup> the following regularity conditions for our spray chart distributions and kernel functions: 

- A1. The density _f_ is square integrable, twice continuously differentiable, and all the second order partial derivatives are square integrable. We will suppose that _β_ = 2 in _H_ ( _β, L_ ). 

- A2. The kernel _K_ is a spherically symmetric and bounded pdf with finite second moment and square integrable. 

- A3. **H** = **H** _n_ is a deterministic sequence of positive definite symmetric matrices such that, _n_ det( **H** ) _→∞_ when _n →∞_ and **H** _→_ 0 elementwise. 

Condition A2 holds for the multivariate Gaussian kernel function that we use in our implementation. We will let **H** be a matrix of bandwidth parameters that has diagonal elements **h** , in our implementation **H** = diag( **h** ). We will use the following notation: _R_ **x** ( _f_ ) = � _f_ ( **y** _|_ **x** )<sup>2</sup> _d_ **y** , _µ_ 2( _K_ ) = � _u_<sup>2</sup> _K_ ( _u_ ) _du_ , and _Hf_ ( **y** _|_ **x** ) is the Hessian matrix respect to _f_ ( **y** _|_ **x** ) where derivatives are taken with respect to **y** . Assume that pitch outcomes are independent across at bats and that _np,j_ = _O_ ( _n_ ), _nb,k_ = _O_ ( _n_ ) and **h** _p,j_ = _O_ ( **h** ), **h** _b,k_ = _O_ ( **h** ) for all _j_ = 1 _, . . . , J_ , _k_ = 1 _, . . . , K_ . 

9 

With the specification that _β_ = 2 in Condition A1 we have that _f_ ( **y** _|_ **x** ) _−L∥_ **x** _−_ **x**<sup>_′_</sup> _∥_<sup>2</sup> _≤ f_ ( **y** _|_ **x**<sup>_′_</sup> ) _≤ f_ ( **y** _|_ **x** ) + _L∥_ **x** _−_ **x**<sup>_′_</sup> _∥_<sup>2</sup> _._ This result implies that 



and _R_ **x** ( _f_ ) _−_ 2 _L∥_ **x** _−_ **x**<sup>_′_</sup> _∥_<sup>2</sup> _≤ R_ **x** _′_ ( _f_ ) _≤ R_ **x** ( _f_ ) + 2 _L∥_ **x** _−_ **x**<sup>_′_</sup> _∥_<sup>2</sup> _._ 

˜ We will define **x** _b,k_ = ( **x**<sup>_′_</sup> _p_<sup>_,_</sup><sup>**x**</sup><sup>_′_</sup> _b,k_<sup>)</sup><sup>_′_and</sup><sup>**x**˜</sup><sup>_p,j_=(</sup><sup>**x**</sup><sup>_′_</sup> _p,j_<sup>_,_</sup><sup>**x**</sup> _b_<sup>_′_)</sup><sup>_′_fornotationalconvenience,andwill</sup> additionally assume the following regularity approximations: 





Approximation A4 is reasonable in our baseball application where there are many players sim- **x** ilar˜ _p,j∥_ enough<sup>_m_</sup> _, sb,k∥_ **x** to _−_ the **x** ˜ _b,k_ players _∥_<sup>_m_</sup> _→_ 0underas _∥_ **x** study _−_ **x** ˜ _p,j_ so _∥, ∥_ that **x** _−_<sup>�</sup> **x** ˜ _b,k_<sup>_J_</sup> _j_ =1 _∥→∞_<sup>_sp,j>_1</sup> for<sup>and</sup> all<sup>�</sup> integers<sup>_K_</sup> _k_ =1<sup>_sb,k_</sup> _m_<sup>_>_</sup> .<sup>1</sup> Approximation<sup>and</sup><sup>_sp,j∥_</sup><sup>**x**</sup><sup>_−_</sup> A5 is reasonable by similar logic. Specification of _β_ = 2 implies that _<u>∥</u>_ diag( _Hf_ ( **y** _|_ **x** _p,_ **x** _b,k_ )) _−_ diag( _Hf_ ( **y** _|_ **x** )) _∥≤_ ~~�~~ _dpL_ and _∥_ diag( _Hf_ ( **y** _|_ **x** _p,j,_ **x** _b_ )) _−_ diag( _Hf_ ( **y** _|_ **x** )) _∥≤_<sup>_√_</sup> _dbL_ where _dp_ and _db_ are, respectively, the dimension of **x** _p_ and **x** _b_ . 

We now have enough structure to estimate the MSE of (2) and (6). Standard results from nonparametric estimation theory give 



and 



Our multivariate H¨older class specifications yield, 





10 

and 



Let _θp,j_ = _n_ det( **H** ) _/np,j_ det( **H** _p,j_ ) and _θb,k_ = _n_ det( **H** ) _/nb,k_ det( **H** _b,k_ ). With these specifications, we have that 



Our assumption on the _wb,k_<sup>2</sup><sup>_∥_</sup><sup>**x**</sup><sup>_−_</sup><sup>**x**˜</sup><sup>_,k∥m_and</sup><sup>_w_</sup> _p,j_<sup>2</sup><sup>_∥_</sup><sup>**x**</sup><sup>_−_</sup><sup>**x**˜</sup><sup>_p,j∥m_,for</sup><sup>_m_=2</sup><sup>_,_4,andanidenticallower</sup> bound argument implies that 



We also have 

and regularity approximations A4 and A5 yield 



11 



where _t ∈{_ 0 _,_ 1 _}_ is chosen to satisfy the above inequality. Putting these variance and bias results together without the lower order terms yields 

_MSE_ (ˆ _g_ **_λ_** ( **y** _|_ **x** ) _, f_ ( **y** _|_ **x** )) _− MSE_ ( _f_<sup>ˆ</sup> **h** ( **y** _|_ **x** ) _, f_ ( **y** _|_ **x** )) 



This motivates the following choice of **_λ_** , 



whereFirst, notice _np_ =<sup>�</sup> that<sup>_J_</sup> _j_ =1 _λ_<sup>_s_2</sup> _p,jp, λ_<sup>_n_</sup> _b_<sup>_p,j_</sup> _→_<sup>and</sup> 0 as<sup>_nb_</sup> min<sup>= �</sup> _j_ ( _∥_<sup>_K_</sup> _k_ **x** =1 _−_<sup>_s_2</sup> _b,k_ **x** ˜ _p,j_<sup>_nb,k_</sup> _∥_ ) _,_<sup>.</sup> min<sup>We</sup> _k_<sup>will</sup> ( _∥_ **x** _−_<sup>now</sup> **x** ˜ _b,k_<sup>develop</sup> _∥_ ) _→∞_<sup>intuition</sup> . These cases<sup>forthese</sup> correspond,<sup>choices.</sup> to there being no similar pitchers or batters to the players under study. We turn attention to the bias terms, notice that 



˜ ˜ when there exists some _j_<sup>_′_</sup> such that _∥_ **x** _−_ **x** _p,j∥→_ 0 or min _j_ ( _∥_ **x** _−_ **x** _p,j∥_ ) _→∞_ . These cases correspond, respectively, to there being a few highly similar pitchers or there being no similar pitchers to the pitcher under study. Thus, the discrepancy in bias vanishes in the extreme cases. The same argument holds for batters. Now notice that 



12 

The same argument holds for batters. Therefore, when there is a pitcher _j_<sup>_′_</sup> and batter _k_<sup>_′_</sup> so that _wp,j′, wb,k′ →_ 1, we have that 



The above is not always less than 0 for all configurations. However, it will be less than 0 when _n_ is comparable to _np,j′_ and _nb,k′_ , a setting that we will guard against in our implementation by specifying a minimal sample size to enter into available player pool. 

## **References** 

- J. Albert. Pitching statistics, talent and luck, and the best strikeout seasons of all-time. _Journal of Quantitative Analysis in Sports_ , 2(1), 2006. 

- J. Albert. Streaky hitting in baseball. _Journal of Quantitative Analysis in Sports_ , 4(1), 2008. 

- Major League Baseball. Statcast. `https://baseballsavant.mlb.com/` , 2014. Accessed: 2020-0429. 

Baseball-Reference. `https://www.baseball-reference.com` , 2020. Accessed: 2020-04-29. 

- B. S. Baumer, S. T. Jensen, and G. J. Matthews. openwar: An open source system for evaluating overall player performance in major league baseball. _Journal of Quantitative Analysis in Sports_ , 11(2):69–84, 2015. 

- S. M. Berry, C. S. Reese, and P. D. Larkey. Bridging different eras in sports. _Journal of the American Statistical Association_ , 94(447):661–676, 1999. 

- L. D. Brown. In-season prediction of batting averages: A field test of empirical bayes and bayes methodologies. _The Annals of Applied Statistics_ , pages 113–152, 2008. 

- D. J. Eck. Challenging nostalgia and performance metrics in baseball. _Chance_ , 33(1):16–25, 2020. 

- Fangraphs. `https://www.fangraphs.com` , 2020. Accessed: 2020-04-29. 

- N. Hamilton. _ggtern: An Extension to ’ggplot2’, for the Creation of Ternary Diagrams_ , 2018. 

- B. James. _The politics of glory: how baseball’s Hall of Fame really works_ . Macmillan, 1994. 

- S. T. Jensen, B. B. McShane, and A. J. Wyner. Hierarchical bayesian modeling of hitting performance in baseball. _Bayesian Analysis_ , 4(4):631–652, 2009a. 

- S. T. Jensen, K. E. Shirley, and A. J. Wyner. Bayesball: A bayesian hierarchical model for evaluating fielding in major league baseball. _The Annals of Applied Statistics_ , 3(2):491–520, 2009b. 

- M. Marchi, J. Albert, and B. S. Baumer. _Analyzing baseball data with R 2nd Edition_ . CRC Press, 2019. 

- B. Petti. The interactive spray chart tool. `https://billpetti.shinyapps.io/shiny_ spraychart/` , 2009. Accessed: 2020-04-29. 

13 

- B. Petti. Research notebook: New format for statcast data export at baseball savant. _The Hardball Times_ , 2017. 

- B. Petti, B. Baumer, and B. Dilday. _baseballr: Functions for acquiring and analyzing baseball data_ , 2020. 

- J. Piette and S. T. Jensen. Estimating fielding ability in baseball players over time. _Journal of Quantitative Analysis in Sports_ , 8(3), 2012. 

- B. Ripley, B. Venables, D. Bates, K. Hornik, A. Gebhardt, and D. Firth. _MASS: R package_ , 2019. 

- A. Schwarz. _The numbers game: Baseball’s lifelong fascination with statistics_ . Macmillan, 2004. 

- Masahiro Shinya, Shinji Tsuchiya, Yousuke Yamada, Kimitaka Nakazawa, Kazutoshi Kudo, and Shingo Oda. Pitching form determines probabilistic structure of errors in pitch location. _Journal of sports sciences_ , 35(21):2142–2147, 2017. 

- N. Silver. Introducing pecota. _Baseball Prospectus_ , pages 507–514, 2003. 

- H. Wickham. _ggplot2: Elegant Graphics for Data Analysis_ . Springer-Verlag New York, 2016. URL `https://ggplot2.tidyverse.org` . 

14 


