<!-- source: [15590410 - Journal of Quantitative Analysis in Sports] Meta-analytics_ tools for understanding the statistical properties of sports metrics.pdf -->

J. Quant. Anal. Sports 2016; 12(4): 151–165 

Alexander M. Franks*, Alexander D’Amour, Daniel Cervone and Luke Bornn 

# **Meta-analytics: tools for understanding the statistical properties of sports metrics** 

DOI 10.1515/jqas-2016-0098 

**Abstract:** In sports, there is a constant effort to improve metrics that assess player ability, but there has been almost no effort to quantify and compare existing metrics. Any individual making a management, coaching, or gambling decision is quickly overwhelmed with hundreds of statistics. We address this problem by proposing a set of “meta-metrics”, which can be used to identify the metrics that provide the most unique and reliable information for decision-makers. Specifically, we develop methods to evaluate metrics based on three criteria: (1) stability: does the metric measure the same thing over time (2) discrimination: does the metric differentiate between players and (3) independence: does the metric provide new information? Our methods are easy to implement and widely applicable so they should be of interest to the broader sports community. We demonstrate our methods in analyses of both NBA and NHL metrics. Our results indicate the most reliable metrics and highlight how they should be used by sports analysts. The meta-metrics also provide useful insights about how to best construct new metrics that provide independent and reliable information about athletes. 

**Keywords:** analysis of variance; basketball; hockey; reliability. 

## **1 Introduction** 

In sports, as in many other industries and research fields, data analysis has become an essential ingredient of management. Sports teams, traditionally run by people with experience playing and/or coaching, now rely on statistical models to measure player ability and inform strategy decisions (Lewis 2004; Oliver 2004). Over the years, the quantity, scope, and sophistication of these models has expanded, reflecting new data sources, methodological 

***Corresponding author: Alexander M. Franks,** University of Washington - Department of Statistics, Seattle, WA, USA, e-mail: amfranks@uw.edu 

**Alexander D’Amour:** University of Berkeley - Department of Statistics, Berkeley, CA, USA **Daniel Cervone:** New York University, New York, NY, USA **Luke Bornn:** Simon Fraser University - Department of Statistics, Burnaby, British Columbia, Canada 

developments, and increasing interest in the field of sports analytics. Despite their inherent promise, new developments in sports analytics have created a clutter of metrics. For example, there are at least three different calculations of the WAR (“Wins Above Replacement”) metric in baseball (Baumer, Jensen and Matthews 2015), all of which have the same hypothetical estimand. In general, any individual making a management, coaching, or gambling decision has potentially dozens of metrics at their disposal, but finding the right metrics to support a given decision can be daunting. We seek to ameliorate this problem by proposing a set of “meta-metrics” that describe which metrics provide the most unique and reliable information for decision-makers. Our methods are simple to implement and applicable to any sport so they should be of broad interest to the sports analytics community. 

The core idea of our work is that quantifying sources of variability – and how these sources are related across metrics, players, and time – is essential for understanding how sports metrics can be used. In this paper, we consider three different sources of variation, which we classify differently depending on the use-case. These are (1) intrinsic player skill, (2) context, e.g. influence of teammates, and (3) chance, i.e. sampling variability. Each of these sources can vary across seasons and between players. We consider each player metric to be composed of a combination of these sources of variation, and in this paper we discuss several diagnostics that can be used to assess how well certain metrics are able to measure, control for, and average across these sources of variation, depending on what is required by the decision-maker. 

The primary purpose of constructing our meta-metrics is to categorize the sources of variation in the data as _signal_ and _noise_ . The signal corresponds to variation that is the key input into a decision process, e.g., a player’s ability to operate in a given system, whereas the _noise_ is variation that we choose not to explain either because of complexity or lack of information (e.g., complex team interactions or minuscule variations in a player’s release between shots). When relevant we condition on observed contextual information (e.g. player position) to create more reliable and interpretable signals. 

For a metric to be useful for a particular decision, its treatment of variation needs to match up with the decision that is being made. For example, consider two distinct 

**152** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 

tasks in which metrics are often deployed – attribution, where we wish to credit a portion of a team’s success to a given player for, e.g., year-end awards, and acquisition, where we wish to assess whether a player should be added to or retained on a team. The classification of signal and noise in these decision tasks is very different. For attribution, we do not care whether a player can repeat their performance in another season (or arguably even how much of their performance was due to chance), whereas repeatability is a central question in player acquisition. That is, chance and team context are still relevant signals when making an attribution decision, but are sources of noise for an acquisition decision. 

While we can isolate some player-wise, season-wise, and team-wise variation by subsetting the data, all measurements that we take are confounded with chance. Further “skills” are abstract concepts that are often collapsed together. With this in mind, we define three meta-metrics that can be used to answer the following questions of player performance metrics: 

- **Discrimination** : Does the metric reliably differentiate between players? 

- **Stability** : Does the metric measure a quantity that is stable over time? 

- **Independence** : Does the metric provide new information? 

Our discrimination meta-metric quantifies how useful a metric is for distinguishing between players within a given season, whereas our stability meta-metric measures how much a metric varies season to season due to changes in context and player skill after removing chance variation. The independence meta-metric quantifies how much information in one metric is already captured by a set of other metrics. Our meta-metrics are based on ideas that have a long history in statistics (e.g., analysis of variance) and psychometrics (e.g., Cronbach’s alpha) (Fisher 1925; Kuder and Richardson 1937; Cronbach 1951) but have not received widespread treatment in sports. The limited work quantifying the reliability of metrics in sports mostly appears in blogs (Blackport 2014; Sprigings 2014; Arthur 2015) and our hope is to formalize and generalize some of the ideas discussed in these articles. We start in Section 2 by motivating and defining three meta-metrics and discuss how to estimate them in Section 3. Section 4 demonstrates the application of these meta-metrics to player performance in the National Basketball Association (NBA) and National Hockey League (NHL). Lastly, in Section 5 we discuss building new metrics and adjusting existing ones in order to improve their meta-analytic properties. 

## **2 Defining meta-metrics** 

Throughout this paper, we write the 3-dimensional array of players, seasons and metrics as _X_ , with _Xspm_ the value of metric _m_ for player _p_ from season _s_ . Our meta-metrics are all R-squared style statistics and can be understood as functions of the (co)variances along the three dimensions of _X_ . As a useful example, consider a model for a metric _m_ that varies over time _s_ and between players _p_ in a linear mixed effects model: 



where 



and [ _µ_ , _σ_<sup>2</sup> ] represents a distribution with mean _µ_ and variance _σ_<sup>2</sup> . The terms _Z*_ can be thought of as random effects, while _ϵspm_ represents the variation induced by the sampling effects of a season – for instance, binomial variation in made shot percentage given a finite sample size; for an infinitely long season, we would observe _τ_<sup>2</sup> M<sup>→0 and</sup> thus _ϵspm_ = 0. _Zspm_ , on the other hand, reflects true value (above average) of the “skill” _m_ of player _p_ in season _s_ . This model encodes four sources of variation, although we only intend to discuss three. The extra parameter, _σ_<sup>2</sup> SM<sup>, captures</sup> variation in league averages over time. For the time scales we will consider in this paper, variation in league averages is small; in practice we will ignore this source of variation, but we will maintain it for completeness in our theoretical development. 

In this representation, we can recognize _σ_<sup>2</sup> PM<sup>+</sup><sup>_σ_2</sup> SPM<sup>+</sup> _τ_<sup>2</sup> M<sup>as the within-season, between-player variance;</sup><sup>_σ_2</sup> SM<sup>+</sup> _σ_<sup>2</sup> SPM<sup>+</sup><sup>_τ_2</sup> M<sup>as the within-player, beween-season variance;</sup> and of course, _σ_<sup>2</sup> SM<sup>+</sup><sup>_σ_2</sup> PM<sup>+</sup><sup>_σ_2</sup> SPM<sup>+</sup><sup>_τ_2</sup> M<sup>asthetotal(be-</sup> tween player-season) variance. Both the discrimination and stability meta-metrics defined in this section can be expressed as ratios involving these quantities, along with the sampling variance _τ_<sup>2</sup> M<sup>.</sup> 

The linear mixed effects model (1) may be a reasonable choice for some metrics and, due to its simplicity, provides a convenient example to illustrate our metametrics. However, an exchangeable, additive model is not appropriate for many of the metrics we consider. A major practical challenge in our analysis is that all of the metrics have unique distributions with distinct support – for example, percentages are constrained to the unit interval, 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **153** 

while many per game or per season statistics are discrete and strictly positive. Other advanced metrics like “plusminus” or “value over replacement” (VORP) in basketball are continuous real-valued metrics that can be negative or positive. 

To define meta-metrics with full generality, consider the random variable _X_ , which is a single entry _Xspm_ chosen randomly from _X_ . Randomness in _X_ thus occurs both from sampling the indexes _S_ , _P_ , and _M_ of _X_ , as well as intrinsic variability in _Xspm_ due to finite season lengths. We will then use the notational shorthand 



and analogously for _Esm_ [ _X_ ], _Vsm_ [ _X_ ], _Em_ [ _X_ ], etc. For example, _Esm_ [ _Vspm_ [ _X_ ]] is the average over all players of the intrinsic variability in _Xspm_ for metric _m_ during season _s_ , or<sup>∑︀</sup> _p_<sup>_Var_[</sup><sup>_X_</sup> _spm_<sup>] /</sup><sup>_N_</sup> _sm_<sup>, where</sup><sup>_N_</sup> _sm_<sup>is the number of entries</sup> of _Xs_ · _m_ . 

### **2.1 Discrimination** 

For a metric measuring player ability to be applicable, it must be a useful tool for discriminating between different players. This implies that most of the variability between players reflects true variation in player ability and not chance variation or noise from small sample sizes. As a useful baseline for discrimination, we compare the average intrinsic variability of a metric to the total between player variation in this metric. Similar approaches which partially inspired our version of this metric have been used in analyzing Major League Baseball data (Tango, Lichtman and Dolphin 2007; Arthur 2015). 

To characterize the discriminative power of a metric, we need to quantify the fraction of total between player variance that is due to chance and the fraction that is due to signal. By the law of total variance, the between player variance can be decomposed as 



Here, _Vsm_ [ _X_ ] corresponds to the total variation in metric _m_ between players in season _s_ , whereas _Esm_ [ _Vspm_ [ _X_ ]] is the average (across players) sampling variability for metric _m_ in season _s_ . With this decomposition in mind, we define the discriminative power of a metric _m_ in season _s_ as 



Intuitively, this describes the fraction (between 0 and 1) of between-player variance in metric _m_ (in season _s_ ) due 

to true differences in player ability. Discrimination metametrics for different seasons can be combined as _𝒟m_ = _Em_ [ _𝒟sm_ ]. 

It is helpful to understand the discrimination estimand for the linear mixed effects model defined in Equation 1. When this model holds, _Esm_ [ _Vspm_ [ _X_ ]] = _τ_<sup>2</sup> M<sup>,and</sup> _Vsm_ [ _X_ ] = _σ_<sup>2</sup> PM<sup>+</sup><sup>_σ_2</sup> SPM<sup>+</sup><sup>_τ_</sup> M<sup>2, the between-player variance</sup> (equal for all seasons _s_ ). Thus, the discrimination metametric under the linear mixed effects model is simply 



### **2.2 Stability** 

In addition to discrimination, which is a meta-metric that describes variation within a single season, it is important to understand how much an individual player’s metric varies from season to season. The notion of stability is particularly important in sports management when making decisions about future acquisitions. For a stable metric, we have more confidence that this year’s performance will be predictive of next year’s performance. A metric can be unstable if it is particularly context dependent (e.g. the player’s performance varies significantly depending on who their teammates are) or if a player’s intrinsic skill set tends to change year to year (e.g. through offseason practice or injury). 

Consequently, we define stability as a metric, which describes how much we expect a single player metric to vary over time after removing chance variability. This metric specifically targets the sensitivity of a metric to change in context or intrinsic player skill over time. Mathematically, we define stability as: 



with 0 _≤𝒮 m ≤_ 1 (see Appendix for proof). Here, _Vpm_ [ _X_ ] is the between-season variability in metric _m_ for player _p_ ; thus, the numerator in (4) averages the between-season variability in metric _m_ , minus sampling variance, over all players. The denominator is the total variation for metric _m_ minus sampling variance. Again, this metric can be easily understood under the assumption of an exchangeable linear model (Equation 1).: 



**154** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 

This estimand reflects the fraction of total variance (with sampling variability removed) that is due to within-player changes over time. If the within player variance is as large as the total variance, then _𝒮 m_ = 0 whereas if a metric is constant over time, then _𝒮 m_ = 1. 

### **2.3 Independence** 

When multiple metrics measure similar aspects of a player’s ability, we should not treat these metrics as independent pieces of information. This is especially important for decision makers in sports management who use these metrics to inform decisions. Accurate assessments of player ability can only be achieved by appropriately synthesizing the available information. As such, we present a method for quantifying the dependencies between metrics that can help decision makers make sense of the growing number of data summaries. 

For some advanced metrics we know their exact formula in terms of basic box score statistics, but this is not always the case. For instance, it is much more challenging to assess the relationships between new and complex model based NBA metrics like adjusted plus minus (Sill 2010), EPV-Added (Cervone et al. 2016) and counterpoints (Franks et al. 2015), which are model-based metrics that incorporate both game-log and player tracking data. Most importantly, even basic box score statistics that are not functionally related will be correlated if they measure similar aspects of intrinsic player skill (e.g., blocks and rebounds in basketball are highly correlated due to their association with height). 

As such, we present a general approach for expressing dependencies among an arbitrary set of metrics measuring multiple players’ styles and abilities across multiple seasons. Specifically, we propose a Gaussian copula model in which the dependencies between metrics are expressed with a latent multivariate normal distribution. Assuming we have _M_ metrics of interest, let _Zsp_ be an _M_ -vector of metrics for player _p_ during season _s_ , and 



where _C_ is a _M × M_ correlation matrix, and _Fm_<sup>_−_1</sup> is the inverse of the CDF for metric _m_ . We define the independence score of a metric _m_ given a condition set of other metrics, _ℳ_ , as 



For the latent variables _Z_ , this corresponds to one minus the R-squared for the regression of _Zm_ on the latent variables _Zq_ with _q_ in _ℳ_ . Metrics for which _ℐmℳ_ is small (e.g. for which the R-squared is large) provide little new information relative to the information in the set of metrics _ℳ_ . In contrast, when _ℐmℳ_ is large, the metric is nearly independent from the information contained in _ℳ_ . Note that _ℐmℳ_ = 1 implies that metric _m_ is independent from all metrics in _ℳ_ . 

We also run a principal component analysis (PCA) on _C_ to evaluate the amount of independent information in a set of metrics. If _UΛ U_<sup>_T_</sup> is the eigendecomposition of _C_ , with _Λ_ = diag( _λ_ 1, _. . . λM_ ) the diagonal matrix of eigenvalues, then we can interpret _ℱk_ = <u>∑∑1</u> _M_ <u>1</u> _k_<sup>_λλii_asthefractionoftotal</sup> variance explained by the first _k_ principal components (Mardia, Kent and Bibby 1980). When _ℱ k_ is large for small _k_ then there is significant redundancy in the set of metrics, and thus dimension reduction is possible. 

## **3 Inference** 

In order to calculate discrimination _𝒟m_ and stability _𝒮 m_ , we need estimates of _Vspm_ [ _X_ ], _Vsm_ [ _X_ ], _Vpm_ [ _X_ ] and _Vm_ [ _X_ ]. Rather than establish a parametric model for each metric (e.g. the linear mixed effects model (1)), we use nonparametric methods to estimate these variances. Specifically, to estimate the sampling distribution of _X_ within each season (e.g., _Var_ [ _Xspm_ ], or equivalently _Vspm_ [ _X_ ], for all _s_ , _p_ , _m_ ), we use the bootstrap (Efron and Tibshirani, 1986). For each team, we resample (with replacement) every game played in a season and reconstruct end-of-season metrics for each player. We use the sample variance of these resampled metrics, BV[ _Xspm_ ], to estimate the intrinsic variation in each player-season metric _Xspm_ . We estimate _Vsm_ [ _X_ ], _Vpm_ [ _X_ ] and _Vm_ [ _X_ ] using sample moments. 

Our implementation of the bootstrap deserves some discussion. Although we run the bootstrap by resampling (with replacement) each game, there are other plausible fine grained units of replication (e.g. we could resample by individual possessions or according to one-minute intervals). However, unlike baseball, hockey and basketball involve complex continuous dynamics and long-term within-game dependences that make it hard to justify the use of higher resolution units of replication. By resampling games, we replicate any within-game correlations that might affect player metrics. For example, there is a tendency for star players to be benched during “garbage time” at the end of games when the score differential is large, but this event depends on the performance of those 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **155** 

players earlier in the game. Because our goal is to estimate variances of functions of season totals, capturing this within-game correlation in the bootstrapping procedure is critical. Finally, we work with games as the unit of replication for practical reasons – it is much simpler to resample at the game level since it does not require access to play-by-play data. In short, there are other resampling methods that replicate within-game correlations, but our approach appears to be the simplest. 

With this approach in mind, assuming _P_ players, our estimator for discrimination is simply 



where _X_<sup>¯</sup> _s_ · _m_ is the average of metric _m_ over the players in season _s_ . Similarly, the stability estimator for a metric _m_ is 



where _X_<sup>¯</sup> · _pm_ is the mean of metric _m_ for player _p_ over all seasons, _X_<sup>¯</sup> ·· _m_ is the total mean over all player-seasons, and _Sp_ is the number of seasons played by player _p_ . 

All independence meta-metrics are defined as a function of the latent correlation matrix _C_ from the copula model presented in Equation 6. To estimate _C_ , we use the semi-parametric rank-likelihood approach developed by Hoff (2007). This method is appealing because we eschew the need to directly estimate the marginal density of the metrics, _Fm_ . We fit the model using the R package _sbgcop_ (Hoff 2012). Using this software, we can model the dependencies for both continuous and discrete valued metrics with missing values. 

In Section 4, we use _ℐmℳ_ to generate “independence curves” for different metrics as a function of the number of statistics in the conditioning set, _ℳ_ . To create these curves, we use a greedy approach: for each metric _m_ we first estimate the independence score _ℐmℳ_ (Equation 8) conditional on the full set of available metrics _ℳ_ , and then iteratively remove metrics that lead to the largest increase in independence score (See Algorithm 1). 

## **4 Results** 

To demonstrate the utility of our meta-metrics, we analyze metrics from both basketball (NBA) and hockey (NHL), including both traditional and “advanced” (modelderived) metrics. We scraped data relevant for over 70 NBA metrics from all players and seasons from the year 2000 

**Algorithm 1** Create independence curves for metric _m_ . 

|1:|IC_m_ ←Vector(_|ℳ|_)|
|---|---|
|2:|_ℳ_<sup>_*_ </sup>←_ℳ_|
|3:|**for**_i_ =_|ℳ|_to 1**do**|
|4:|_ℐmax_ ←0|
|5:|_mmax_ ←NA|
|6:|**for** ˜_m ∈ℳ_<sup>_*_</sup> **do**|
|7:|_𝒢_←_ℳ_<sup>_*_ </sup>\_{_˜_m}_|
|8:|**If**_ℐm𝒢> ℐmax_ **then**|
|9:|_ℐmax_ ←_ℐm𝒢_|
|10:|_mmax_ ←˜_m_|
|11:|**end if**|
|12:|**end for**|
|13:|_ℳ_<sup>_*_ </sup>←_ℳ_<sup>_*_ </sup>\_mmax_|
|14:|IC_m_[_i_] ←_ℐmℳ_<sup>_*_</sup>|
|15:|**end for**|
|16:|**return**IC_m_|



onwards from basketball-reference.com (Sports Reference LLC 2016a). We also scraped data for 40 NHL metrics recorded from the year 2006 onwards (Sports Reference LLC 2016b). For both seasons we use regular season data only. We also use the R package _nhlscrapr_ to gather NHL gamelog data. Where appropriate, we normalized metrics by minutes played or possessions played to ameliorate the impact of anomalous events in our data range, such as injuries and work stoppages; this approach sacrifices no generality, since minutes/possessions can also be treated as metrics. In the Appendix, we provide a glossary of all of the metrics evaluated in this paper. A repository for the replication code is available on GitHub: https://github. com/afranks86/meta-analytics. 

### **4.1 Analysis of NBA metrics** 

In Figure 1 we plot the stability and discrimination meta-metrics for many of the NBA metrics available on basketball-reference.com. When computing the discrimination and stability meta-metrics, we exclude data from players with fewer than 250 minutes played in a season. This leads to 5182 player-seasons of data from the year 2000 onwards. Discrimination scores are estimated from gamelog data for the year 2015 only. There were no minutes or sample size restrictions for the independence analyses: 7507 player-seasons of data from the year 2000 onwards were used for these analyses. 

For basic box score statistics, discrimination and stability scores match intuition. Metrics like rebounds, blocks and assists, which are strong indicators of player position, are highly discriminative and stable because of the relatively large between player variance. As another example, 

**156** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 



<!-- Start of picture text -->
Metric reliabilities<br>1.0<br>FT%<br>STL% BLK%DRB%ORB%TRB%<br>0.9 AST%<br>FG%<br>TOV% 3PAr<br>PF DBPM<br>0.8<br>TS% PER FTAPTSFGA<br>USG%<br>0.7 ORtg WS/48 BPMOBPM<br>3P% EB<br>VORP<br>0.6<br>OWS MPG<br>WS<br>DRtg DWS<br>0.5<br>0.4 MP<br>0.3 3P%<br>0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0<br>Discrimination<br>Stability<br><!-- End of picture text -->

**Figure 1:** Discrimination and stability score estimates for an ensemble of metrics and box score statistics in the NBA. Raw three point percentage is the least discriminative and stable of the metrics we study; empirical Bayes estimates of three point ability (“3P% EB”, Section 5) improve both stability and discrimination. Metrics like rebounds, blocks and assists are strong indicators of player position and for this reason are highly discriminative and stable. Per-minute or per-game statistics are generally more stable but less discriminative. 

free throw percentage is a relatively non-discriminative statistic within-season but very stable over time. This makes sense because free throw shooting requires little athleticism (e.g., does not change with age or health) and is isolated from larger team strategy and personnel (e.g., teammates do not have an effect on a player’s free throw ability). 

Our results also highlight the distinction between pure rate statistics (e.g., per-game or per-minute metrics) and those that incorporate total playing time. Metrics based on total minutes played are highly discriminative but less stable, whereas per-minute or per-game metrics are less discriminative but more stable. One reason for this is that injuries affect total minutes or games played in a season, but generally have less effect on per-game or per-minute metrics. This is an important observation when comparing the most reliable metrics since it is more meaningful to compare metrics of a similar type (rate-based vs total). 

WS/48, ORtg, DRtg and BPM metrics are rate-based metrics whereas WS and VORP based metrics incorporate total minutes played (Sports Reference LLC 2016a). WS and VORP are more discriminative than the rate based statistics primarily because MP increases discrimination, 

not because there is stronger signal about player ability. Rate based metrics are more relevant for estimating player skill whereas total metrics are more relevant for identifying overall end of season contributions (e.g. for deciding the MVP). Since these classes of metrics serve different purposes, in general they should not be compared directly. Our results show moderately improved stability and discriminative power of the BPM-based metrics over other rate-based metrics like WS/48, ORTg and DRtg. Similarly, we can see that for the omnibus metrics which incorporate total minutes played, VORP is more reliable in both dimensions than total WS. 

Perhaps the most striking result is the unreliability of empirical three point percentage. It is both the least stable and least discriminative of the metrics that we evaluate. Amazingly, over 50% of the variation in three point percentage between players who take a non-negligible number of three point shots (at least 10) in a given season is due to chance. This is likely because differences between three point shooters’ true shooting percentage tend to be relatively small, and as such, chance variation tends to be the dominant source of variation. Moreover, contextual variation like a team’s ability to create open shots for a player affect the stability of three point percentage. 

Finally, we use independence meta-metrics to explore the dependencies between available NBA metrics. In Figure 2 we plot the independence curves described in Section 3. Of the metrics that we examine, steals (STL) appear to provide some of the most unique information. This is evidenced by the fact that the _ℐℳ_<sup>_STL_≈0.40 , mean-</sup> ing that only 60% of the variation in steals across playerseasons is explainable by the other 69 metrics. Moreover, the independence score estimate increases quickly as we reduce the size of the conditioning set, which highlights the relative lack of metrics that measure skills that correlate with steals. While the independence curves for defensive metrics are concave, the independence curves for the omnibus metrics measuring overall skill are roughly linear. Because the omnibus metrics are typically functions of many of the other metrics, they are partially correlated with many of the metrics in the conditioning set. 

Not surprisingly, there is a significant amount of redundancy across available metrics. Principal component analysis (PCA) on the full correlation matrix _C_ suggests that we can explain over 75% of the dependencies in the data using only the first 15 out of 65 principal components, i.e., _ℱ_ 15 ≈0.75. Meanwhile, PCA of the sub-matrix _Cℳo_ , _ℳo_ where _ℳo_ = _{_ WS, VORP, PER, BPM, PTS _}_ yields _ℱ_ 1 = 0.75, that is, the first component explains 75% of the variation in these five metrics. This means that much of the information in these 5 metrics can be compressed 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **157** 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>VORP<br>WS<br>0.2<br>PER<br>BPM<br>0.0 PTS<br><!-- End of picture text -->



<!-- Start of picture text -->
DBPM<br>STL<br>BLK<br>DWS<br>DRtg<br><!-- End of picture text -->

**Figure 2:** Independence score estimates as a function of the size of the conditioning set, for overall skill metrics (left) and defensive metrics (right). The curves look more linear for the overall skill metrics, which suggest that they reflect information contained in nearly all existing metrics. The first principal component from the five-by-five sub-correlation matrix consisting of the overall skill metrics, explains 73% of the variation. Defensive metrics have independence curves that are more concave. This highlights the fact that defensive metrics are correlated with a smaller set of metrics. The first principal component from the five-by-five sub-correlation matrix consisting of these defensive metrics, explains only 51% of the variation and the second explains only 73%. 

into a single metric that reflects the same latent attributes of player skill. In contrast, for the defensive metrics presented in Figure 2, _ℳd_ = _{_ DBPM, STL, BLK, DWS, DRtg _}_ , PCA indicated that the first component explains only 51% of the variation. Adding a second principal component increases the total variance explained to 73%. In Figure 9 we plot the cumulative variance explained, _ℱ k_ as a function of the number of components _k_ for all metrics _ℳ_ and the subsets _ℳo_ and _ℳd_ . Figure 8 illustrates a hierarchical clustering of these metrics based on these dependencies. 

### **4.2 Analysis of NHL metrics** 

NHL analytics is a much younger field than NBA analytics, and as a consequence there are fewer available metrics to analyze. In Figure 3A we plot the estimated discrimination and stability scores for many of the hockey metrics available on hockey-reference.com. When computing the discrimination and stability scores, we exclude data from players with fewer than 500 minutes played in a season. This leads to 4291 player-seasons of data from the year 2000 onwards. Discrimination scores are estimated from gamelog data for the year 2015 only. There were no minutes or sample size restrictions for the independence analyses: 7270 player-seasons of data from the year 2000 onwards were used for these analyses. 

Again, we find that metrics like hits (HIT), blocks (BLK) and shots (S) which are strong indicators for player type are the most discriminative and stable because of the large between-player variance. 

Our results can be used to inform several debates in the NHL analytics community. For example, our results highlight the low discrimination of plus-minus (“ _±_ ”) in hockey, which can be explained by the relative paucity of goals scored per game. For this reason, NHL analysts typically focus more on shot attempts (including shots on goal, missed shots and blocked shots). In this context, it is often debated whether it is better to use Corsi- or Fenwickbased statistics (Peterson 2014). Fenwick-based statistics incorporate shots and misses whereas Corsi-based statistics additionally incorporate blocked shots. Our results indicate that with the addition of blocks, Corsi metrics (e.g. “CF% rel” and “CF%”) are both more discriminative and stable than the Fenwick metrics. 

In Figure 3B we plot the estimated independence scores as a function of the number of statistics in the conditional set for five different metrics. Like steals in the NBA, we found that takeaways (TK) provide the most unique information relative to the other 39 metrics. Here, _ℐℳ_<sup>_TK_=</sup> 0.73, meaning that all other metrics together only explain 27% of the total variance in takeaways, which is consistent with the dearth of defensive metrics in the NHL. dZS% is an example of a metric that is highly correlated with only one other metric in the set of metrics we study, but poorly predicted by the others. This metric is almost perfectly predicted by its counterpart oZS% and hence _ℐℳ_<sup>_dZS_≈0</sup> when _oZS_ % _∈ℳ_ and significantly larger otherwise. This is clear from the large uptick in the independence score of dZS% after removing oZS% from _ℳ_ . 

Once again, the analysis of the dependencies among metrics reveals significant redundancy in information 

**158** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 



<!-- Start of picture text -->
A Metric reliabilities (NHL) B Hockey metrics<br>1.0 1.0<br>S% EV PIM BLK<br>GW A G GCPTS TSASHIT<br>0.8 TK 0.8<br>ATOI<br>oiSV% oiSH% GV TGF<br>PDO OPS<br>PPCF%reIDPS<br>0.6 +/- FF% rel PS 0.6<br>TGA C60CF%<br>FF%<br>0.4 0.4<br>TOI<br>PTS<br>0.2 SH 0.2 TK<br>CF% rel<br>OiSH%<br>0.0 FO% 0.0 dZS%<br>0.0 0.2 0.4 0.6 0.8 1.0 0 10 20 30 40<br>Discrimination Number of included metrics<br>Figure 3:  (Left) Discrimination and stability scores for many NHL metrics. Corsi-based statistics are slightly more reliable than Fenwick<br>statistics. Plus/minus is non-discriminative in hockey because of the paucity of goals scored in a typical game. (Right) Fraction of variance<br>explained (R-squared) for each metric by a set of other metrics in our sample. Only 27% of the total variance in takeways (TK) is explained<br>by all other NHL metrics.<br>Stability R-squared<br>FO%<br>SH PGA GV<br>TK<br>oiSH% +/– PIM HIT PGF PS BLK<br>PDO A<br>Dependencies between NHL Metrics  PP GW TGA oiSV% CA FA C60 DPS TOI ATOI TGF OPS PTS GC S% G EV S TSA<br>oZS% dZS% CF FF CF% rel FF% rel CF% FF%<br><!-- End of picture text -->



<!-- Start of picture text -->
PTS<br>TK<br>CF% rel<br>OiSH%<br>dZS%<br><!-- End of picture text -->

**Figure 3:** (Left) Discrimination and stability scores for many NHL metrics. Corsi-based statistics are slightly more reliable than Fenwick statistics. Plus/minus is non-discriminative in hockey because of the paucity of goals scored in a typical game. (Right) Fraction of variance explained (R-squared) for each metric by a set of other metrics in our sample. Only 27% of the total variance in takeways (TK) is explained by all other NHL metrics. 

**Figure 4:** Hierarchical clustering of NHL metrics based on the correlation matrix, _C_ . Clustered metrics have larger absolute correlations but can be positively or negatively associated. The metrics that have large loadings on the two different principal component (Figure 7) are highlighted in red and blue. 

across NHL metrics. We can explain over 90% of the variation in the data using only 15 out of 40 principal components, that is _ℱ_ 15 = 0.90 (Figure 10). Figure 4 illustrates a hierarchical clustering of these metrics based on these dependencies. 

## **5 Constructing novel metrics** 

In addition to providing useful benchmarks on the quality of different metrics, the meta-metrics can motivate the 

design of new and improved metrics or be used to justify the superiority of new metrics over traditional ones. Here we provide two examples in which novel metrics improve upon existing metrics in at least one of the meta-metrics. In the first example, we use a hierarchical model to shrink empirical estimates of three point ability in basketball. We demonstrate that this model-based estimate is both more stable and discriminative than the simple percentage metric. In the second example, we propose a method for creating a set of new metrics that are all mutually independent. 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **159** 

### **5.1 Shrinkage estimators** 

Model-based adjustments of common box score statistics can reduce sampling variability and thus lead to improvements in discrimination and stability. In Section 4.1, we showed how three point percentage was one of the least discriminative and stable metrics in basketball and thus an improved estimator of three point making ability is warranted. We define three point ability using the notation introduced in Section 2 as _Esp_ (3 _P_ %)[ _X_ ] , i.e. the expected three point percentage for player _p_ in season _s_ , and propose a model-based estimate of this quantity that is both more stable and discriminative than the observed percentage. 

For this model, we assume an independent hierarchical Bernoulli model for the three point ability of each player: 



where _X_<sup>3</sup> _sp_<sup>_P_%</sup> is the observed three point percentage of player _p_ in season _s_ , _πsp_ = _Esp_ (3 _P_ %)[ _X_ ] is the estimand of 

interest, _nsp_ is the number of attempts, _π_<sup>0</sup> _p_<sup>=</sup><sup>_E_</sup> _p_ (3 _P_ %)<sup>[</sup><sup>_X_] is</sup> the career average for player _p_ , and _π_<sup>0</sup> _p_<sup>(1</sup><sup>_−π_0</sup> _p_<sup>)/</sup><sup>_r_</sup> _p_<sup>is the</sup> variance in _πsp_ over time. We use the R package _gbp_ for empirical Bayes inference of _πsp_ and _rp_ , which controls the amount of shrinkage (Tak et al. 2016). In Figure 5 we plot the original and shrunken estimates for LeBron James’ three point ability over his career. 

We can compute discrimination and stability estimates for the estimated three point ability derived from this model using the same approach outlined in Section 3. Although the empirical Bayes’ procedure yields probability intervals for all estimates, we can still compute the frequentist variability using the bootstrap (e.g. see Efron (2015)). In Figure 1 we highlight the comparison between observed three point percentage and the empirical Bayes estimate in red. Observed three point percentage is an unbiased estimate of three point ability but is highly unreliable. The Bayes estimate is biased for all players, but theory suggests that the estimates have lower mean squared error due to a reduction in variance (Efron and Morris 1975). The improved stability and discrimination of the empirical Bayes estimate is consistent with this fact. 



<!-- Start of picture text -->
LeBron James three point percentage<br>Shrunken estimate<br>Empiricial percentage<br>Career average<br>Number of attempts<br>Posterior sd<br>0.30 0.35 0.40 0.45<br>95% Interval<br>0.50<br>0.45<br>0.40<br>0.35<br>0.30<br>0.25<br>Season<br>3P%<br>2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014<br><!-- End of picture text -->

**Figure 5:** Three point percentages for LeBron James by season, and shrunken estimates using the empirical Bayes model proposed by Tak et al. (2016). Top: raw three point percentage (top line, ordered from lowest to highest) and the corresponding shrunken estimates (bottom line). The length of the purple lines are proportional to the number of attempts and the length of the green lines is proportional to the posterior standard deviation of the shrunken estimate. Bottom: Original (hollow circle) and shrunken (red circle) three point percentage over time. Shrinking three point percentage to a player’s career average improves stability and discrimination. 

**160** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 

There are, of course, other shrinkage estimators that may be more appropriate depending on the context. For instance, rather than shrink each estimate toward a player’s career average, we could derive estimators based on shrinkage to the league average for each season. This might be especially reasonable for rookie players or players with little career playing time. More sophisticated extensions might involve shrinking estimates to a regression surface based on covariates like how long the player has been in the league. The choice of shrinkage model should reflect the decision-maker’s classification of observed variation into signal and noise and assumptions about the relationships between those sources of variation. The shrinkage scheme used in this section classifies both chance variation and inter-season variation as noise, and treats player-specific variation is independent. 

### **5.2 Principal component metrics** 

The dependency model proposed in Section 2.3 provides a natural way to derive new metrics that describe orthogonal aspects of player ability. In particular, the eigendecomposition of the latent correlation matrix, _C_ , (Equation 6) can be used to develop a (smaller) set of new metrics, which, by construction, are mutually independent and explain much of the variation in the original set. If the latent normal variables _Z_ defined in Equation 6 were known, then we could compute the principal components of this matrix to derive a new set of orthogonal metrics. The principal components are defined as _W_ = _ZU_ where _U_ is the matrix of eigenvectors of _C_ . Then, by definition, _W ∼_ MVN(0, _I_ ) and thus _Wk ⊥⊥ Wj ∀ k_ =/ _j_ . For the independence score defined in Section 2.3, this means that _ℐk_ , _ℳ−W k_<sup>= 1forall</sup><sup>_k_,where</sup><sup>_ℳ_</sup> _−_<sup>_W_</sup> _k_<sup>isthesetofallmet-</sup> rics^ _Wj_ , _j_ =/ _k_ . We estimate _Z_ ^by normalizing _X_ , that is _Zspm_ = Φ<sup>_−_1</sup> (^ _Fm_ ( _Xspm_ )) where _Fm_ is the empirical CDF of _Xm_ . Our estimate of the principal components of the latent matrix _Z_ is then simply _W_<sup>^</sup> _sp_ = _Z_<sup>^</sup> _sp U_ . It should be noted that metrics with high independence scores (Equation 8) will not typically have large loadings on the first few principal components by definition since the first principal components capture variation in the most redundant metrics. In our formulation, a metric with an independence score of one will load on exactly one eigenvector and this vector will have a corresponding eigenvalue of one. 

We present results based on these new PCA-based metrics for both NBA and NHL statistics. In Figure 6 we 

list three PCA-based metrics for the NBA and the corresponding original NBA metrics which load most heavily onto them. We also rank the top ten players across seasons according to _W_<sup>^</sup> _sp_ and visualize the scores for each of these three PCA-based metrics for four different players in the 2014–2015 season. Here, the fact that LeBron James ranks highly in each of these three independent metrics in the 2014-15 season is indicative of his versatility. 

Although the meaning of these metrics can be harder to determine, they can provide a useful aggregation of high-dimensional measurements of player skill that facilitate fairer comparisons of players. 

In Figure 7 we provide two PCA-based metrics for NHL statistics. We again list the metrics that have the highest loadings on two principal component along with the top ten players (in any season) by component. The first principal component largely reflects variation in offensive skill and easily picks up many of the offensive greats, including Ovechkin and Crosby. For comparison, we include another component, which corresponds to valuable defensive players who make little offensive contribution. This component loads positively on defensive point shares (DPS) and blocks (BLK), but negatively on shots and goals (S, G). 

## **6 Discussion** 

Uncertainty quantification, a hallmark of statistical sciences, has so far been under-appreciated in sports analytics. Our work demonstrates the importance of understanding sources of variation and provides a method to quantify how different metrics reflect this variation. Specifically, we explore three different “meta-metrics” for evaluating the reliability of metrics in any sport: discrimination, stability and independence. Our results show that we can use metametrics to characterize the most discriminative and stable summaries amongst a set of omnibus metrics (like win shares, BPM and PER for the NBA), which can in turn help decision-makers identify the metrics that meet necessary requirements to be useful for a given task. First, highly non-discriminative metrics should not be used by decision makers to compare players since differences in these metrics reflect chance variation, not variation in ability. Second, metrics that are highly unstable generally should be considered questionable as criteria for player acquisition since these metrics are likely to change significantly over time either in response to a changing context or fluctuating player ability. 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **161** 

#### PC Scores (2014 2015) 









<!-- Start of picture text -->
Stephen Curry DeAndre Jordan Kirk Hinrich<br><!-- End of picture text -->

LeBron James 

PC ranks (all years) 

|“Effi|cient Shooters” (PC1)||“Shoot|ers, Assisters” (PC|2)|“|High Usage” (PC3)||
|---|---|---|---|---|---|---|---|---|
|FG%,|PER, WS, %FG 2P,||OBPM,|3PA, AST%, %FG|A|USG,|2PA, FGA, LostBall,||
|2P%,|BPM, TS%||3P, Avg|Shot Dist, PGA||FTA, S|fDrawn, PTS, And1||
|Rank|Player|Year|Rank|Player|Year|Rank|Player|Year|
|1|Dwight Howard|2010|1|Stephen Curry|2014|1|Allen Iverson|2006|
|2|Dwight Howard|2009|2|Stephen Curry|2013|2|Cory Higgins|2011|
|3|Dwight Howard|2008|3|Steve Nash|2006|3|Kobe Bryant|2014|
|4|Shaquille O’Neal|2000|4|Chris Paul|2014|4|Allen Iverson|2003|
|5|Shaquille O’Neal|2004|5|Steve Nash|2008|5|Russell Westbrook|2014|
|6|Dwight Howard|2007|6|Chris Paul|2007|6|Tony Wroten|2013|
|7|DeAndre Jordan|2014|7|Damon Jones|2004|7|Tony Wroten|2014|
|8|Amar’e Stoudemire|2007|8|Steve Nash|2009|8|Allen Iverson|2004|
|9|Shaquille O’Neal|2003|9|Stephen Curry|2012|9|Jermaine O’Neal|2004|
|10|Tim Duncan|2006|10|LeBron James|2009|10|Allen Iverson|2005|



**Figure 6:** First three principal components of _C_ . The tables indicate the metrics that predominantly load on the components. Each component generally corresponds to interpretable aspects of player style and ability. The table includes the highest ranking players across all seasons for each component. The top row depicts principal component score for four players in the 2014–2015 season. The radius of the corresponding segment is determined by the quantile of the PC score, with higher ranking players having larger segments. LeBron James ranks highly among all 3 independent components in the 2014–2015 season. 

||“Offensive skill”<br>||“V<br>|aluable defenders <br><br>|”|
|---|---|---|---|---|---|
|PTS,|OPS, GC, PS,||ATOI,|DPS,<br>BLK,||
|TGF,<br>PGF,|G,<br>A,<br>EV,<br> TSA||-S, -T|SA, -G, -FA, -CF||
|Rank|Player|Year|Rank|Player|Year|
|1|Alex Ovechkin|2010|1|Nicklas Lidstrom|2008|
|2|Sidney Crosby|2009|2|Ryan Suter|2014|
|3|Alexander Semin|2008|3|Toby Enstrom|2009|
|4|Daniel Sedin|2010|4|Josh Gorges|2012|
|5|Evgeni Malkin|2011|5|Toni Lydman|2011|
|6|Daniel Sedin|2010|6|Toby Enstrom|2008|
|7|Alex Ovechkin|2007|7|Chris Progner|2010|
|8|Alex Ovechkin|2008|8|Paul Martin|2008|
|9|Sidney Crosby|2012|9|Niclas Havelid|2008|
|10|Marian Hossa|2008|10|Andy Greene|2015|



**Figure 7:** Player rankings based on two principal components. The first PC is associated with offensive ability. The fact that this is the _first_ component implies that a disproportionate fraction of the currently available hockey metrics measure aspects of offensive ability. The other included component reflects valuable defensive players (large positive loadings for defensive point shares and blocks) but players that make few offensive contributions (negative loadings for goals and shots attempted). The metrics that load onto these components are highlighted in the dendrogram of NHL metrics (Figure 4). 

Along these lines, our meta-metrics can elucidate precisely which aspects of player skill are transferable and help analysts partition relevant sources of variability. In Section 4.1 we showed how “minutes played” is 

discriminative and stable and how this can translate to other omnibus metrics which incorporate minutes played. After controlling for minutes played, these metrics may provide little additional stable quantitative value. As 

**162** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 

another example, three point percentage in basketball is likely sensitive to the “openness” of the shooter, which is in turn a function of teammate ability and strategy. 

With this in mind, decision makers should make an effort to use metrics that condition on as much relevant information as possible (like “openness” for the three point example) and then verify that these new metrics are more stable or discriminative and thus more useful for player acquisition decisions. In this sense, meta-metrics can be used as a benchmark for evaluating the improvement of new estimators. In Section 5.1 we provided one example, in which we demonstrate that an estimate based on a simple hierarchical model can improve the stability and discrimination of standard boxscore statistics by reducing chance variability. 

Our methods also demonstrate how decision makers can synthesize information across multiple metrics using the independence criterion. Analysts should work with metrics that are roughly independent to avoid falsely interpreting multiple redundant metrics as additional evidence of player ability. We show how to identify the most independent existing metrics as well as demonstrate how to create new metrics that are all mutually independent (Section 5.2). 

Finally, in this paper, we focused on reliability and dependence of metrics for _all players in the league_ but the meta-metrics can easily be recalculated for relevant subsets of players. This is important because, as shown, in this context the most reliable metrics are often the metrics that distinguish between player types (e.g., blocks and rebounds in basketball). This may be irrelevant when making decisions involving a specific group of players (e.g., which NBA center to acquire). When using metrics to evaluate players of a certain type, we should compute the meta-metrics conditional on this player type. For instance, there is less variation in the number of blocks and rebounds by NBA centers, and as such, these metrics are less discriminative and stable than they are for the league as a whole. Moreover, the dependence between blocks and rebounds is largely driven by height, and thus the conditional dependence between blocks and rebounds given height is much smaller. Further, in our analyses we used sample size restrictions to eliminate players with very few minutes played (or in the case of 3P%, few attempts). Without these restrictions, the meta-metric scores may have largely been driven by differences between high volume and low volume players. 

For this reason, it is important that the meta-metrics are always interpreted in the context of the appropriate group of players. In light of this point, it is notable that the meta-metrics that we present in this paper are stated in terms of expectations and variances, so that estimation of conditional meta-metrics simply requires replacing marginal expectations and variances with their conditional counterparts. 

Another important consideration is that our metametrics only measure the internal quality of a metric. The meta-metrics are not designed to provide any information about how relevant the metrics are for the sport of interest. For instance, although we identified Corsi-based metrics as more discriminative and stable than the related Fenwick-based metrics, it is still possible that Fenwick metrics are more predictive of team performance. As a more extreme example, an athlete’s birthplace zip code would be perfectly discriminative, stable and independent from all other metrics, but is clearly irrelevant for determining a player’s value to the team. This suggests that in practice coaches and analysts should consider a fourth meta-metric: “relevance”. Relevance could simply be a qualitative description of the metric’s meaning and value as determined by domain experts or it could be a quantitative summary of the causal or predictive relationship between the metric and an outcome of interest, like wins or revenue generated. Nevertheless, the methods presented here provide a useful characterization of the reliability of existing metrics. We believe that future iterations of the meta-metrics outlined in this paper can become a standard analytical tool that will improve the decisions made and information gleaned from new and old metrics alike. 

**Acknowledgment:** This work was partially supported by the Washington Research Foundation Fund for Innovation in Data-Intensive Discovery, the Moore/Sloan Data Science Environments Project at the University of Washington and New York University, U.S. National Science Foundation grants 1461435, by DARPA under Grant No. FA8750-14-2-0117, by ARO under Grant No. W911NF-15-10172, by Amazon, and by NSERC. The authors are grateful to Andrew Miller (Department of Computer Science, Harvard University), and Kirk Goldsberry for sharing data and ideas which contributed to the framing of this paper. 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **163** 

## **Appendix** 



<!-- Start of picture text -->
Dependencies between NBA Metrics<br>BLK<br>%FGA Dunks<br>ORB<br>DRB<br>TRB<br>Avg Shot Dist<br>%FGA 0−3<br>%FGA 2P<br>3PA<br>3PAr<br>%FGA 3P<br>FG%<br>2P%<br>%FG 2P<br>%FG 0−3<br>OBPM<br>OWS<br>WS<br>BPM<br>VORP<br>TS%<br>ORtg<br>PER<br>WS/48<br>%3PA − Corner<br>3P%<br>%FG 3P<br>OnCourt<br>On−Off<br>%FGA 10−16<br>%FG 3−10<br>%FG 10−16<br>%FG 16<3<br>TOV%<br>TOV − LostBall<br>Made Dunks<br>%Ast'd 3P<br>PF − Blocking<br>3P% − Corner<br>PF − Take<br>STL<br>DWS<br>Blkd<br>And1<br>FTA<br>SfDrawn<br>2PA<br>PTS<br>FGA<br>USG%<br>FT%<br>%FGA 16<3<br>FTr<br>%FGA 3−10<br>TOV − Other<br>PF − Offensive<br>DBPM<br>DRtg<br>PF<br>PF − Shooting<br>%Ast'd 2P<br>TOV − BadPass<br>AST<br>PGA<br><!-- End of picture text -->

**Figure 8:** Hierarchical clustering of NBA metrics based on the correlation matrix, _C_ . Clustered metrics have larger absolute correlations (e.g. can be positively or negatively related). 



<!-- Start of picture text -->
All NHL metrics<br>0 10 20 30 40<br>Number of included metrics<br>1.0<br>0.8<br>0.6<br>0.4<br>Independence<br>0.2<br>0.0<br><!-- End of picture text -->

**Figure 10:** Total variance explained, _Fk_ by number of principal components for 40 NHL metrics. We can explain over 90% of the total variability using only 15 components. 

### **Proof of 0** **_≤_** _𝒮_ **_m ≤_ 1** 

We calculate stability for metric _m_ (4) as 



To show 0 _≤𝒮 m ≤_ 1, it suffices to show both 

(A) _Em_ [ _Vpm_ [ _X_ ] _− Vspm_ [ _X_ ]] _≥_ 0 

(B) _Vm_ [ _X_ ] _− Em_ [ _Vspm_ [ _X_ ]] _− Em_ [ _Vpm_ [ _X_ ] _− Vspm_ [ _X_ ]] _≥_ 0. 

To verify (A), we can write 











<!-- Start of picture text -->
All NBA Metrics Omnibus NBA Metrics Defensive NBA Metrics<br>1.0 1.0 1.0<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0.0 0.0 0.0<br>0 10 20 30 40 50 60 70 1 2 3 4 5 1 2 3 4 5<br>Number of components Number of components Number of components<br>Variance explained Variance explained Variance explained<br><!-- End of picture text -->

**Figure 9:** Total variance explained, _Fk_ vs number of principal components used. When evaluating the dependencies among all 70 metrics, we can explain over 75% of the total variability using only 15 components. For a subset of five omnibus metrics, the first PC explains 73% of the variation, indicating a high level of redundancy. For a set of five defensive metrics, the first component explains 50% of the variance. 

**164** | A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics 

To check (B), note that 

**Table 2:** NBA Glossary cont. 

_Vm_ [ _X_ ] _− Em_ [ _Vspm_ [ _X_ ]] _− Em_ [ _Vpm_ [ _X_ ] _− Vspm_ [ _X_ ]] 

|_Vm_[_X_]_−Em_[_Vspm_[_X_]]_−Em_[_Vpm_[_X_]_−Vspm_[_X_]]|**Metric**|**Description**|
|---|---|---|
|= _Vm_[_X_]_−Em_[_Vpm_[_X_]]|%FGA 2P|Percentage of feld goal attempts that are 2<br>|
|||pointers|
|= _Vm_[_Epm_[_X_]]|%FGA 0–3|Percentage of feld goal attempts within 0–3 feet|
|_≥_0.|%FGA 3–10<br>|Percentage of feld goal attempts within 3–10<br>feet<br>|
||%FGA 10–16|Percentage of feld goal attempts within 10–16<br>|
|||feet|
|**Glossary of metrics**|%FGA 16_<_3|Percentage of feld goal attempts between 16<br>feet and the 3 point line|
|**Table 1:**Glossary of NBA metrics used. All stats are per 36 minutes|%FGA 3P|Percentage of feld goal attempts that are 3<br>|
|unless otherwise noted. See (Sports Reference LLC, 2016a) for more||pointers|
|<br>detail.|%FG 2P|Percentage of made feld goals that are 2<br>pointers|
|**Metric**<br>**Descrition**|%FG 0–3|Percentage of made feld goals within 0–3 feet|
|**p**|%FG 3–10|Percentage of made feld goals within 3–10 feet|
|MP<br>Minutes played|%FG 10–16|Percentage of made feld goals within 10–16 feet|
|FGA<br>Field goal attempts|%FG 16_<_3|Percentage of made feld goals between 16 feet|
|FG%<br>Field goal percentage||and the 3 point line|
|3PA<br>3 point attempts|%FG 3P|Percentage of made feld goals that are 3|
|3P%<br>3 point percentage||pointers|
|2PA<br>2 point attempts|%Ast’d 2P|Percentage of made 2 point feld goals that are|
|2P%<br>2 point percentage||assisted|
|FTA<br>Free throw attempts|%FGA Dunks|Percentage of feld goal attempts that are dunks|
|FT%<br>Free throw percentage|Made Dunks|Made dunks (per 36 MP)|
|PF<br>Personal fouls|%Ast’d 3P|Percentage of made 3 point feld goals that are|
|PTS<br>Points||assisted|
|PER<br>Personal efciency rating|%3PA - Corner|Percentage of 3 point feld goal attempts taken|
|TS%<br>True shooting percentage||from the corner|
|3PAr<br>Three point attempt rate|3P% - Corner|3 point feld goal percentage from the corner|
|FTr<br>Free throw attempt rate|OnCourt|Plus/minus per 100 possessions|
|ORB<br>Ofensive rebounds|On-Of|Plus/minus net per 100 possession|
|DRB<br>Defensive rebounds|TOV - BadPass|Turnovers from bad passes|
|TRB<br>Total rebounds|TOV - LostBall|Turnovers due to lost ball|
|AST<br>Assists|TOV - Other|All other turnovers (traveling, out of bounds, etc)|
|STL<br>Steals|PF - Shooting|Shooting fouls committed|
|BLK<br>Blocks|PF - Blocking|Blocking fouls committed|
|TOV%<br>Turnover percentage (per possession)|PF - Ofensive|Ofensive fouls committed|
|USG%<br>Usage per|PF - Take|Take fouls committed|
|OWS<br>Ofensive win shares|PGA|Points generated by assists|
|DWS<br>Defensive win shares|SfDrawn|Shooting fouls drawn|
|WS<br>Win shares|And1|shots made on fouls drawn|
|WS/48<br>Win shares per 48 minutes|Blkd|Field goal attempts that are blocked|
|OBPM<br>Ofensive box plus minus|||
|DBPM<br>Defensive box plus minus|||
|<br>BPM<br>Box plus minus|||
|VORP<br>Value over replacement|||
|ORtg<br>Ofensive rating|||
|DRtg<br>Defensive rating|||
|Avg Shot Dist<br>Average shot distance|||



### **Glossary of metrics** 

**Table 1:** Glossary of NBA metrics used. All stats are per 36 minutes unless otherwise noted. See (Sports Reference LLC, 2016a) for more detail. 

A. M. Franks et al.: Meta-analytics: tools for understanding the statistical properties of sports metrics | **165** 

**Table 3:** Glossary of hockey metrics used. 

|**Table 3:**|lossary of hockey metrics used.|Cervone, D., A. D’Amour, L. Bornn, and K. Goldsberry. 2016.|
|---|---|---|
|||“A Multiresolution Stochastic Process Model for Predicting|
|**Metric**|**Description**|Basketball Possession Outcomes.”_Journal of the American_|
|G|Goals|_Statistical Association_111:585–599.<br>|
|A|Assists|Cronbach, L. J. 1951. “Coefcient Alpha and the Internal Structure of<br>|
|PTS|Points|Tests.”_Psychometrika_16:297–334.<br>|
|_±_|Plus / minus|Efron, B. 2015. “Frequentist Accuracy of Bayesian Estimates.”<br>|
|PIM|Penalties in minutes|_Journal of the Royal Statistical Society: Series B (Statistical_<br>|
|EV|Even strength goals|_Methodology)_77:617–646.|
|PP|Power play goals|Efron, B. and C. Morris. 1975. “Data Analysis Using Stein’s Estimator|
|SH|Short handed goals|and Its Generalizations.”_Journal of the American Statistical_|
|GW|Game winning goals|_Association_70:311–319.|
|S|Shots on goal|Efron, B. and R. Tibshirani. 1986. “Bootstrap Methods for Standard|
|S%|Shooting percentage|Errors, Confdence Intervals, and Other Measures of Statistical|
|TSA|Total shots attempted|Accuracy.”_Statistical Science_1:54–75.|
|TOI|Time on ice|Fisher, R. A. 1925._Statistical Methods for Research Workers_.|
|FO%|Face of win percentage|Guildford: Genesis Publishing Pvt Ltd.|
|HIT|Hits at even strength|Franks, A., A. Miller, L. Bornn, and K. Goldsberry. 2015.|
|BLK|Blocks at even strength|“Counterpoints: Advanced Defensive Metrics for NBA|
|TK|Takeways|Basketball,” in_Proceedings of the 2015 MIT Sloan Sports_|
|GV|Giveaways<br>|_Analytics Conference_, MIT Sloan Sports Analytics Conference.|
|GC|Goals created|Boston, MA.|
|TGF|Total goals for (while player was on the ice)<br>|Hof, P. 2012._sbgcop: Semiparametric Bayesian Gaussian Copula_|
|PGF|Power player goals for (while player was on the ice)|_Estimation and Imputation_. URL http://CRAN.R-project.org/|
|TGA<br>|Total goals against (while player was on the ice)<br>|<br>package=sbgcop, r package version 0.975.|
|PGA|Power player goals against (while player was on the ice)|“|
|||Hof, P. D. 2007. Extending the Rank Likelihood for Semiparametric|
|OPS|Ofensive point shares|<br>Copula Estimation.”_The Annals of Applied Statistics_|
|DPS<br>|Defensive point shares<br>|<br>1:265–283.|
|PS|Total point shares<br>|Kuder, G. F. and M. W. Richardson. 1937. “The Theory of the|
|CF<br>|Corsi for (on ice shots + blocks + misses)<br>|<br>Estimation of Test Reliability.”_Psychometrika_2:151–160.|
|CA|Corsi against (on ice shots + blocks + misses)<br>|<br>Lewis M. 2004._Moneyball: The Art of Winning an Unfair Game_. New|
|CF%|Corsi for percentage: CF / (CF + CA)|,  <br>York NY WW Norton & Comn|
|CF% rel|Relative Corsi for (on ice CF% _−_of ice CF%)|, :    pay.<br>|
|||Mardia, K. V., J. T. Kent, and J. M. Bibby. 1980._Multivariate Analysis_.|
|FF|Fenwick for (shots + blocks + misses)|<br>|
|FA|<br>Fenwick against (shots + blocks + misses)|San Diego: Academic Press.<br>|
|FF%|Fenwick for percentage: FF / (FF + FA)|Oliver, D. 2004._Basketball on Paper: Rules and Tools for_<br>|
||<br>|_Performance Analysis_. Lincoln NE: Potomac Books Inc.|
|FF% rel|Relative Fenwick for (on ice FF% _−_of ice FF%)|,   ,|
|oiSH%|<br>Team on ice shooting percentage while player on the ice|Peterson, M. 2014. “Corsi vs. Fenwick: How are They Diferent<br>|
|iSV%|T  i   hil l  h i|and When Do I Use Them?” http://faceofviolation.com/|
|o|eam on ce save percentage we payer on te ce|<br>|
|PDO|Shooting percentage plus save percentage|dekestodangles/2014/11/19/corsi-vs-fenwick-diferent-use/.<br>|
|oZS%|Percentage of ofensive zone starts while on the ice|Accessed on September 6, 2016.|
|dZS%|Percentage of defensive zone starts while on the ice|Sill, J. 2010. “Improved NBA adjusted plus-minus using regulariza-|



- Sill, J. 2010. “Improved NBA adjusted plus-minus using regularization and out-of-sample testing,” in _Proceedings of the 2010 MIT Sloan Sports Analytics Conference_ . 

All metrics are normalized by total time on ice (TOI) unless otherwise noted. 

- Sports Reference LLC. 2016a. “Basketball-Reference.com - Basketball Statistics and History.” http://www.basketballreference.com/. 

## **References** 

   - Sports Reference LLC. 2016b. “Hockey-Reference.com - Hockey Statistics and History.” http://www.hockey-reference.com/. 

   - Sprigings, D. 2014. “donttellmeaboutheart.blogspot.com/ - How Long Does It Take for a Forward’s Shooting to Stabilize?” http://donttellmeaboutheart.blogspot.com/2014/12/howlong-does-it-take-for-forwards.html. Accessed on September 30, 2015. 

- Arthur, R. 2015. “Stats Can’t Tell Us Whether Mike Trout or Josh Donaldson Should Be MVP.” http://fivethirtyeight.com/ features/stats-cant-tell-us-whether-mike-trout-or-joshdonaldson-should-be-mvp/. Accessed on September 30, 2015. 

- Baumer, B. S., S. T. Jensen, and G. J. Matthews. 2015. “openwar: An Open Source System for Evaluating Overall Player Performance in Major League Baseball.” _Journal of Quantitative Analysis in Sports_ 11:69–84. 

   - Tak, H., J. Kelly, and C. N. Morris. 2016. “Rgbp: An R Package for Gaussian, Poisson, and Binomial Random Effects Models with Frequency Coverage Evaluations.” arXiv preprint arXiv:1612.01595. 

- Blackport, D. 2014. “How Long Does It Take for Three Point Shooting to Stabilize?” http://nyloncalculus.com/2014/08/29/longtake-three-point-shooting-stabilize/. Accessed on September 30, 2015. 

- Tango, T. M., M. G. Lichtman, and A. E. Dolphin. 2007. _The Book: Playing the Percentages in Baseball_ . Lincoln, NE: Potomac Books, Inc. 


