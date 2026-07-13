<!-- source: 2016 Meta-Analytics.pdf -->

# Meta-Analytics: Tools for Understanding the Statistical Properties of Sports Metrics<sup>_∗_</sup> 

Alexander Franks, Alexander D’Amour, Daniel Cervone and Luke Bornn 

### October 3, 2016 

##### **Abstract** 

In sports, there is a constant effort to improve metrics which assess player ability, but there has been almost no effort to quantify and compare existing metrics. Any individual making a management, coaching, or gambling decision is quickly overwhelmed with hundreds of statistics. We address this problem by proposing a set of “meta-metrics” which can be used to identify the metrics that provide the most unique, reliable, and useful information for decision-makers. Specifically, we develop methods to evalute metrics based on three criteria: 1) stability: does the metric measure the same thing over time 2) discrimination: does the metric differentiate between players and 3) independence: does the metric provide new information? Our methods are easy to implement and widely applicable so they should be of interest to the broader sports community. We demonstrate our methods in analyses of both NBA and NHL metrics. Our results indicate the most reliable metrics and highlight how they should be used by sports analysts. The meta-metrics also provide useful insights about how to best construct new metrics which provide independent and reliable information about athletes. 

> _∗_ Alexander M. Franks is a Moore/Sloan Data Science and WRF Innovation in Data Science Postdoctoral Fellow (amfranks@uw.edu). Alexander D’Amour is a Neyman Visiting Assistant Professor in the Department of Statistics at UC Berkeley (alexdamour@berkeley.edu). Daniel Cervone is a Moore-Sloan Data Science Fellow at New York University (dcervone@nyu.edu). Luke Bornn is an Assistant Professor of Statistics at Simon Frasier University. This work was partially supported by the Washington Research Foundation Fund for Innovation in Data-Intensive Discovery, the Moore/Sloan Data Science Environments Project at the University of Washington and New York University, U.S. National Science Foundation grants 1461435, by DARPA under Grant No. FA8750-14-2-0117, by ARO under Grant No. W911NF- 15-1-0172, by Amazon, and by NSERC. The authors are grateful to Andrew Miller (Department of Computer Science, Harvard University), and Kirk Goldsberry for sharing data and ideas which contributed to framing of this paper. 

1 

## **1 Introduction** 

In sports, as in many other industries and research fields, data analysis has become an essential ingredient of management. Sports teams, traditionally run by people with experience playing and/or coaching, now rely heavily on statistical models to measure player ability and inform strategy decisions (Lewis, 2004; Oliver, 2004). Over the years, the quantity, scope, and sophistication of these models has expanded, reflecting new data sources, methodological developments, and increasing interest in the field of sports analytics. Despite their inherent promise, new developments in sports analytics have created a clutter of metrics. For example, there are at least three different calculations of the WAR (“Wins Above Replacement”) metric in baseball (Baumer et al., 2015), all of which have the same hypothetical estimand. In general, any individual making a management, coaching, or gambling decision has potentially dozens of metrics at his/her disposal, but finding the right metrics to support a given decision can be daunting. We seek to ameliorate this problem by proposing a set of “metametrics” that describe which metrics provide the most unique and reliable information for decision-makers. Our methods are simple to implement and applicable to any sport so they should be of broad interest to the sports analytics community. 

The core idea of our work is that quantifying sources of variability—and how these sources are related across metrics, players, and time—is essential for understanding how sports metrics can be used. In this paper, we consider three different sources of variation, which we classify differently depending on the use-case. These are 1) intrinsic player skill, 2) context, e.g. influence of teammates, and 3) chance, i.e. sampling variability. Each of these sources can vary across seasons and between players. We consider each player metric to be composed of a combination of these sources of variation (Figure 1), and in this paper we discuss several diagnostics that can be used to assess how well certain metrics are able to measure, control for, and average across these sources of variation, depending on what is required by the decision-maker. 

The primary purpose of constructing our meta-metrics is to categorize the sources of variation in the data as _signal_ and _noise_ . The signal corresponds to variation that is the key 

2 

input into a decision process, e.g., a player’s ability to operate in a given system, whereas the _noise_ is variation that we choose not to explain either because of complexity or lack of information (e.g., complex team interactions or minuscule variations in a player’s release between shots). When relevant we condition on observed contextual information (e.g. player position) to create more reliable and interpretable signals. 

For a metric to be useful for a particular decision, its treatment of variation needs to match up with the decision that is being made. For example, consider two distinct tasks – in which metrics are often deployed attribution, where we wish to credit a portion of a team’s success to a given player for, e.g., year-end awards, and acquisition, where we wish to assess whether a player should be added to or retained on a team. The classification of signal and noise in these decision tasks is very different. For attribution, we do not care whether a player can repeat their performance in another season (or arguably even how much of their performance was due to chance), whereas repeatability is a central question in player acquisition. That is, chance and team context are still relevant signals when making an attribution decision, but are sources of noise for an acquisition decision. 

While we can isolate some player-wise, season-wise, and team-wise variation by subsetting the data, all measurements that we take are confounded with chance. Further “skills” are abstract concepts that are often collapsed together. With this in mind, we define three metametrics that can be used to answer the following questions of player performance metrics: 

- **Discrimination** : Does the metric reliably differentiate between players? 

- **Stability** : Does the metric measure a quantity which is stable over time? 

- **Independence** : Does the metric provide new information? 

Our discrimination meta-metric quantifies how useful a metric is for distinguishing between players within a given season, whereas our stability meta-metric measures how much a metric varies season to season due to changes in context and player skill after removing chance variation. The independence meta-metric quantifies how much information in one metric is already captured by a set of other metrics. Our meta-metrics are based on ideas 

3 

which have a long history in statistics (e.g., analysis of variance) and psychometrics (e.g., Cronbach’s alpha) (Fisher, 1925; Cronbach, 1951; Kuder and Richardson, 1937) but have not received widespread treatment in sports. The limited work quantifying the reliability of metrics in sports mostly appears in blogs (Sprigings, 2014; Blackport, 2014; Arthur, 2015) and our hope is to formalize and generalize some of the ideas discussed in these these articles. We start, in Section 2 by motivating and defining three meta-metrics and discuss how to estimate them in Section 3. Section 4 demonstrates the application of these meta-metrics to player performance in National Basketball Association (NBA) and National Hockey League (NHL). Lastly, in Section 5 we discuss building new metrics and adjusting existing ones in order to improve their meta-analytic properties. 



Figure 1: Sources of variation in end-of-season metrics. Player metrics confound different aspects of intrinsic player style or ability, team effects and chance (e.g. sampling variability). We visualize metrics amongst multiple players across seasons in a 3-dimensional array (right). Here, we illustrate two hypothetical metrics, one in red and another purple. Variation in the color’s tone on the front face corresponds to observed between-player variability in a single season and variation on the right face corresponds to variability in the metric for one player over time. Team-wise and chance variation also play a role in determining the variation in color tone. 

4 

## **2 Defining Meta-metrics** 

Throughout this paper, we write the 3-dimensional array of players, seasons and metrics as _X_ , with _Xspm_ the value of metric _m_ for player _p_ from season _s_ (see Figure 1). Our meta-metrics are all R-squared style statistics and can be understood as functions of the (co)variances along the three dimensions of _X_ . As a useful example, consider a model for a metric _m_ that varies over time _s_ and between players _p_ is a linear mixed effects model: 



where 



and [ _µ, σ_<sup>2</sup> ] represents a distribution with mean _µ_ and variance _σ_<sup>2</sup> . The terms _Z∗_ can be thought of as random effects, while _ϵspm_ represents individual player-season variation in a metric—for instance, binomial variation in made shot percentage given a finite sample size. _Zspm_ and _ϵspm_ are distinguished by assuming that for an infinitely long season, a player’s metric would have no such variability, thus _ϵspm_ = 0. Note that we can recognize _σ_ PM<sup>2+</sup><sup>_σ_</sup> SPM<sup>2+</sup><sup>_τ_2</sup> M<sup>asthewithin-season,between-playervariance;</sup><sup>_σ_</sup> SM<sup>2+</sup><sup>_σ_</sup> SPM<sup>2+</sup><sup>_τ_2</sup> M<sup>asthe</sup> within-player, beween-season variance; and of course, _σ_ SM<sup>2+</sup><sup>_σ_</sup> PM<sup>2+</sup><sup>_σ_</sup> SPM<sup>2+</sup><sup>_τ_2</sup> M<sup>asthetotal</sup> (between player-season) variance. Both the discrimination and stability meta-metrics defined in this section can be expressed as ratios involving these quantities, along with the sampling variance _τ_ M<sup>2.</sup> 

The linear mixed effects model (1) may be a reasonable choice for some metrics and, due to its simplicity, provides a convenient example to illustrate our meta-metrics. However, an exchangeable, additive model is not appropriate for many of the metrics we consider. A major practical challenge in our analysis is that all of the metrics have unique distributions 

5 

with distinct support—percentages are constrained to the unit interval, while many per game or per season statistics are discrete and strictly positive. Other advanced metrics like “plus-minus” or “value over replacement” (VORP) in basketball are continuous real-valued metrics which can be negative or positive. 

To define meta-metrics with full generality, consider the random variable _X_ , which is a single entry _Xspm_ chosen randomly from _X_ . Randomness in _X_ thus occurs both from sampling the indexes _S, P_ , and _M_ of _X_ , as well as intrinsic variability in _Xspm_ due to finite season lengths. We will then use the notational shorthand 



and analogously for _Esm_ [ _X_ ] _, Vsm_ [ _X_ ] _, Em_ [ _X_ ], etc. For example, _Esm_ [ _Vspm_ [ _X_ ]] is the average over all players of the intrinsic variability in _Xspm_ for metric _m_ during season _s_ , or � _p_<sup>_V ar_[</sup><sup>_Xspm_]</sup><sup>_/Nsm_,where</sup><sup>_Nsm_isthenumberofentriesof</sup><sup>_Xs·m_.</sup> 

### **2.1 Discrimination** 

For a metric measuring player ability to be applicable, it must be a useful tool for discriminating between different players. Implicit in this is that most of the variability between players reflects true variation in player ability and not chance variation or noise from small sample sizes. As a useful baseline for discrimination, we compare the average intrinsic variability of a metric to the total between player variation in this metric. A similar approach which partially inspired this metric was used to compare how reliably one could differentiate MVP candidates in Major League Baseball (Arthur, 2015). 

To characterize the discriminative power of a metric, we need to quantify the fraction of total between player variance that is due to chance and the fraction that is due to signal. By the law of total variance, this can be decomposed as 



6 

Here, _Vsm_ [ _X_ ] corresponds to the total variation in metric _m_ between players in season _s_ , whereas _Esm_ [ _Vspm_ [ _X_ ]] is the average (across players) sampling variability for metric _m_ in season _s_ . With this decomposition in mind, we define the discriminative power of a metric _m_ in season _s_ as 



Intuitively, this describes the fraction (between 0 and 1) of between-player variance in _m_ (in season _s_ ) due to true differences in player ability. Discrimination meta-metrics for different seasons can be combined as _Dm_ = _Em_ [ _Dsm_ ]. 

It is helpful to understand the discrimination estimand for the linear mixed effects model defined in Equation 1. When this model holds, _Esm_ [ _Vspm_ [ _X_ ]] = _τ_ M<sup>2,and</sup><sup>_Vsm_[</sup><sup>_X_]=</sup><sup>_σ_</sup> PM<sup>2+</sup> _σ_ SPM<sup>2+</sup><sup>_τ_2</sup> M<sup>,thebetween-playervariance(equalforallseasons</sup><sup>_s_).Thus,thediscrimination</sup> meta-metric under the linear mixed effects model is simply 



### **2.2 Stability** 

In addition to discrimination, which is a meta-metric that describes variation within a single season, it is important to understand how much an individual player’s metric varies from season to season. The notion of stability is particularly important in sports management when making decisions about about future acquisitions. For a stable metric, we have more confidence that this year’s performance will be predictive of next year’s performance. A metric can be unstable if it is particularly context dependent (e.g. the player’s performance varies significantly depending on who their teammates are) or if a players’ intrinsic skill set tends to change year to year (e.g. through offseason practice or injury). 

Consequently, we define stability as a metric, which describes how much we expect a single player metric to vary over time after removing chance variability. This metric specifically targets the sensitivity of a metric to change in context or intrinsic player skill over time. 

7 

Mathematically, we define _stability_ as: 



with 0 _≤Sm ≤_ 1 (see Appendix for proof). Here, _Vpm_ [ _X_ ] is the between-season variability in metric _m_ for player _p_ ; thus, the numerator in (4) averages the between-season variability in metric _m_ , minus sampling variance, over all players. The denominator is the total variation for metric _m_ minus sampling variance. Again, this metric can be easily understood under the assumption of an exchangeable linear model (Equation 1).: 



This estimand reflects the fraction of total variance (with sampling variability removed) that is due to within-player changes over time. If the within player variance is as large as the total variance, then _Sm_ = 0 whereas if a metric is constant over time, then _Sm_ = 1. 

### **2.3 Independence** 

When multiple metrics measure similar aspects of a player’s ability, we should not treat these metrics as independent pieces of information. This is especially important for decision makers in sports management who use these metrics to inform decisions. Accurate assessments of player ability can only be achieved by appropriately synthesizing the available information. As such, we present a method for quantifying the dependencies between metrics that can help decision makers make sense of the growing number of data summaries. 

For some advanced metrics we know their exact formula in terms of basic box score statistics, but this is not always the case. For instance, it is much more challenging to assess the relationships between new and complex model based NBA metrics like adjusted plus minus (Sill, 2010), EPV-Added (Cervone et al., 2014) and counterpoints (Franks et al., 2015), which are model-based metrics that incorporate both game-log and player tracking data. Most importantly, as illustrated in Figure 1, even basic box score statistics that are 

8 

not functionally related will be correlated if they measure similar aspects of intrinsic player skill (e.g., blocks and rebounds in basketball are highly correlated due to their association with height). 

As such, we present a general approach for expressing dependencies among an arbitrary set of metrics measuring multiple players’ styles and abilities across multiple seasons. Specifically, we propose a Gaussian copula model in which the dependencies between metrics are expressed with a latent multivariate normal distribution. Assuming we have _M_ metrics of interest, let _Zsp_ be an _M_ -vector of metrics for player _p_ during season _s_ , and 





where _C_ is a _M × M_ correlation matrix, and _Fm_<sup>_−_1</sup> is the inverse of the CDF for metric _m_ . We define independence score of a metric _m_ given a condition set of other metrics, _M_ , as 



For the latent variables _Z_ , this corresponds to one minus the R-squared for the regression of _Zm_ on the latent variables _Zq_ with _q_ in _M_ . Metrics for which _ImM_ is small (e.g. for which the R-squared is large) provide little new information relative to the information in the set of metrics _M_ . In contrast, when _ImM_ is large, the metric is nearly independent from the information contained in _M_ . Note that _ImM_ = 1 implies that metric _m_ is independent from all metrics in _M_ . 

We also run a principal component analysis (PCA) on _C_ to evaluate the amount of independent information in a set of metrics. If _U_ Λ _U_<sup>_T_</sup> is the eigendecomposition of _C_ , with Λ = diag( _λ_ 1 _, ...λM_ ) the diagonal matrix of eigenvalues, then we can interpret _Fk_ = <u>�</u> _Mk_ <u>1</u><sup>_λi_</sup> <u>�1</u><sup>_λi_as</sup> the fraction of total variance explained by the first _k_ principal components (Mardia et al., 1980). When _Fk_ is large for small _k_ then there is significant redundancy in the set of metrics, and thus dimension reduction is possible. 

9 

## **3 Inference** 

In order to calculate discrimination _Dm_ and stability _Sm_ , we need estimates of _Vspm_ [ _X_ ]], _Vsm_ [ _X_ ], _Vpm_ [ _X_ ] and _Vm_ [ _X_ ]. Rather than establish a parametric model for each metric (e.g. the linear mixed effects model (1)), we use nonparametric methods to estimate reliability. Specifically, to estimate the sampling distribution of _X_ within each season (e.g., _V ar_ [ _Xspm_ ], or equivalently _Vspm_ [ _X_ ], for all _s_ , _p_ , _m_ ), we use the bootstrap (Efron and Tibshirani, 1986). For each team, we resample (with replacement) every game played in a season and reconstruct end-of-season metrics for each player. We use the sample variance of these resampled metrics, BV[ _Xspm_ ], to estimate the intrinsic variation in each player-season metric _Xspm_ . We estimate _Vsm_ [ _X_ ], _Vpm_ [ _X_ ] and _Vm_ [ _X_ ] using sample moments. 

Thus, assuming _P_ players, our estimator for discrimination is simply 



where _X_<sup>¯</sup> _s·m_ is the average of metric _m_ over the players in season _s_ . Similarly, the stability estimator for a metric _m_ is 



where _X_<sup>¯</sup> _·pm_ is the mean of metric _m_ for player _p_ over all seasons, _X_<sup>¯</sup> _··m_ is the total mean over all player-seasons, and _Sp_ is the number of seasons played by player _p_ . 

All independence meta-metrics are defined as a function of the latent correlation matrix _C_ from the copula model presented in Equation 6. To estimate _C_ , we use the semi-parametric rank-likelihood approach developed by Hoff (2007). This method is appealing because we eschew the need to directly estimate the marginal density of the metrics, _Fm_ . We fit the model using the R package _sbgcop_ (Hoff, 2012). Using this software, we can model the dependencies for both continous and discrete valued metrics with missing values. 

In Section 4, we use _ImM_ to generate “independence curves” for different metrics as a function of the number of statistics in the conditioning set, _M_ . To create these curves, we use a greedy approach: for each metric _m_ we first estimate the independence score _ImM_ 

10 

(Equation 8) conditional on the full set of available metrics _M_ , and then iteratively remove metrics that lead to the largest increase in independence score (See Algorithm 1). 

**Algorithm 1** Create independence curves for metric _m_ 1: IC _m ←_ Vector( _|M|_ ) 2: _M_<sup>_∗_</sup> _←M_ 3: **for** _i_ = _|M|_ to 1 **do** 4: _Imax ←_ 0 5: _mmax ←_ NA 6: **for** _m_ ˜ _∈M_<sup>_∗_</sup> **do** 7: _G ←M_<sup>_∗_</sup> _\ {_ ˜ _m}_ 8: **if** _ImG > Imax_ **then** 10:9: _Immaxmax←I← m_ ˜ _mG_ 11: **end if** 12: **end for** 13: _M_<sup>_∗_</sup> _←M_<sup>_∗_</sup> _\ mmax_ 14: IC _m_ [ _i_ ] _←ImM∗_ 15: **end for** 

16: **return** IC _m_ 

## **4 Results** 

To demonstrate the utility of our meta-metrics, we analyze metrics from both basketball (NBA) and hockey (NHL), including both traditional and “advanced” (model-derived) metrics. We gathered data on 70 NBA metrics from all players and seasons from the year 2000 onwards (Sports Reference LLC, 2016a). We also gather 40 NHL metrics recorded from the year 2000 onwards (Sports Reference LLC, 2016b). Where appropriate, we normalized metrics by minutes played or possessions played to ameliorate the impact of anomalous events in our data range, such as injuries and work stoppages; this approach sacrifices no generality, since minutes/possessions can also be treated as metrics. In the appendix we provide a glossary of all of the metrics evaluated in this paper. 

11 

### **4.1 Analysis of NBA Metrics** 

In Figure 2 we plot the stability and discrimination meta-metrics for many of the NBA metrics available on `basketball-reference.com` . For basic box score statistics, discrimination and stability scores match intuition. Metrics like rebounds, blocks and assists, which are strong indicators of player position, are highly discriminative and stable because of the relatively large between player variance. As another example, free throw percentage is a relatively non-discriminative statistic within-season but very stable over time. This makes sense because free throw shooting requires little athleticism (e.g., does not change with age or health) and is isolated from larger team strategy and personnel (e.g., teammates do not have an effect on a player’s free throw ability). 

Our results also highlight the distinction between pure rate statistics (e.g., per-game or per-minute metrics) and those that incorporate total playing time. Metrics based on total minutes played are highly discriminative but less stable, whereas per-minute or per-game metrics are less discriminative but more stable. One reason for this is that injuries affect total minutes or games played in a season, but generally have less effect on per-game or perminute metrics. This is an important observation when comparing the most reliable metrics since it is more meaningful to compare metrics of a similar type (rate-based vs total). 

WS/48, ORtg, DRtg and BPM metrics are rate-based metrics whereas WS and VORP based metrics incorporate total minutes played (Sports Reference LLC, 2016a). WS and VORP are more reliable than the rate based statistics primarily because MP significantly increases their reliability, _not_ because there is stronger signal about player ability. Rate based metrics are more relevant for estimating player skill whereas total metrics are more relevant for identifying overall end of season contributions (e.g. for deciding the MVP). Since these classes of metrics serve different purposes, in general they should not be compared directly. Our results show moderately improved stability and discriminative power of the BPM-based metrics over other rate-based metrics like WS/48, ORTg and DRtg. Similarly, we can see that for the omnibus metrics which incorporate total minutes played, VORP is more reliable in both dimensions than total WS. 

12 

Perhaps the most striking result is the unreliability of empirical three point percentage. It is both the least stable and least discriminative of the metrics that we evaluate. Amazingly, over 50% of the variation in three point percentage between players in a given season is due to chance. This is likely because differences between shooters’ true three point shooting percentage tend to be very small, and as such, chance variation tends to be the dominant source of variation. Moreover, contextual variation like a team’s ability to create open shots for a player affect the stability of three point percentage. 

Finally, we use independence meta-metrics to explore the dependencies between available NBA metrics. In Figure 3 we plot the independence curves described in Section 3. Of the metrics that we examine, steals (STL) appear to provide some of the most unique information. This is evidenced by the fact that the _IM_<sup>_STL_</sup> _≈_ 0 _._ 40 , meaning that only 60% of the variation in steals across player-seasons is explainable by the other 69 metrics. Moreover, the independence score estimate increases quickly as we reduce the size of the conditioning set, which highlights the relative lack of metrics that measure skills that correlate with steals. While the independence curves for defensive metrics are concave, the independence curves for the omnibus metrics measuring overall skill are roughly linear. Because the omnibus metrics are typically functions of many of the other metrics, they are partially correlated with many of the metrics in the conditioning set. 

Not surprisingly, there is a significant amount of redundancy across available metrics. Principal component analysis (PCA) on the full correlation matrix _C_ suggests that we can explain over 75% of the dependencies in the data using only the first 15 out of 65 principal components, i.e., _F_ 15 _≈_ 0 _._ 75. Meanwhile, PCA of the sub-matrix _CMo,Mo_ where _Mo_ = _{_ WS, VORP, PER, BPM, PTS _}_ yields _F_ 1 = 0 _._ 75, that is, the first component explains 75% of the variation in these five metrics. This means that much of the information in these 5 metrics can be compressed into a single metric that reflects the same latent attributes of player skill. In contrast, for the defensive metrics presented in Figure 3, _Md_ = _{_ DBPM, STL, BLK, DWS, DRtg _}_ , PCA indicated that the first component explains only 51% of the variation. Adding a second principal component increases the total variance 

13 

#### **Metric Reliabilities** 



<!-- Start of picture text -->
FT%<br>STL% BLK%TRB%<br>DRB%ORB%<br>AST%<br>FG%<br>TOV% 3PAr<br>PF DBPM<br>PTS<br>TS% PER FTA FGA<br>USG%<br>WS/48 BPM<br>ORtg OBPM<br>3P% EB<br>VORP<br>MPG<br>OWS<br>WS<br>DRtg DWS<br>MP<br>3P%<br>0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0<br>Discrimination<br>1.0<br>0.9<br>0.8<br>0.7<br>Stability<br>0.6<br>0.5<br>0.4<br>0.3<br><!-- End of picture text -->

Figure 2: Discrimination and stability score estimates for an ensemble of metrics and box score statistics in the NBA. Raw three point percentage is the least discriminative and stable of the metrics we study; empirical Bayes estimates of three point ability (“3P% EB”, Section 5) improve both stability and discrimination . Metrics like rebounds, blocks and assists are strong indicators of player position and for this reason are highly discriminative and stable. Per-minute or per-game statistics are generally more stable but less discriminative. 

explained to 73%. In Figure 10 we plot the cumulative variance explained, _Fk_ as a function of the number of components _k_ for all metrics _M_ and the subsets _Mo_ and _Md_ . 

14 





Figure 3: Independence score estimates as a function of the size of the conditioning set, for overall skill metrics (left) and defensive metrics (right). The curves look more linear for the overall skill metrics, which suggest that they reflect information contained in nearly all existing metrics. The first principal component from the five-by-five sub-correlation matrix consisting of the overall skill metrics, explains 73% of the variation. Defensive metrics have independence curves that are more concave. This highlights the fact that defensive metrics are correlated with a smaller set of metrics. The first principal component from the five-byfive sub-correlation matrix consisting of these defensive metrics, explains only 51% of the variation and the second explains only 73%. 

15 

### **4.2 Analysis of NHL Metrics** 

NHL analytics is a much younger field than NBA analytics, and as a consequence there are fewer available metrics to analyze. In Figure 4a we plot the estimated discrimination and stability scores for many of the hockey metrics available on `hockey-reference.com` . Again, we find that metrics like hits (HIT), blocks (BLK) and shots (S) which are strong indicators for player type are the most discriminative and stable because of the large between-player variance. 

Our results can be used to inform several debates in the NHL analytics community. For example, our results highlight the low discrimination of plus-minus (“+/-”) in hockey, which can be explained by the relative paucity of goals scored per game. For this reason, NHL analysts typically focus more on shot attempts (including shots on goal, missed shots and blocked shots). In this context, it is often debated whether it is better to use Corsi- or Fenwick-based statistics (Peterson, 2014). Fenwick-based statistics incorporate shots and misses whereas Corsi-based statistics additionally incorporate blocked shots. Our results indicate that with the addition of blocks, Corsi metrics (e.g. “CF% rel” and “CF%”) are both more reliable and stable than the Fenwick metrics. 

In Figure 4b we plot the estimated independence scores as a function of the number of statistics in the conditional set for five different metrics. Like steals in the NBA, we found that takeaways (TK) provide the most unique information relative to the other 39 metrics. Here, _IM_<sup>_TK_</sup> = 0 _._ 73, meaning that all other metrics together only explain 27% of the total variance in takeaways, which is consistent with the dearth of defensive metrics in the NHL. dZS% is an example of a metric that is highly correlated with only one other metric in the set of metrics we study, but poorly predicted by the others. This metric is almost perfectly predicted by its counterpart oZS% and hence _IM_<sup>_dZS_</sup> _≈_ 0 when _oZS_ % _∈M_ and significantly larger otherwise. This is clear from the large uptick in the independence score of dZS% after removing oZS% from _M_ . 

Once again, the analysis of the dependencies among metrics reveals significant redundancy in information across NHL metrics. We can explain over 90% of the variation in the 

16 

data using only 15 out of 40 principal components, that is _F_ 15 = 0 _._ 90 (Figure 11). Figure 5 illustrates a hierarchical clustering of these metrics based on these dependencies. 



<!-- Start of picture text -->
Metric Reliabilities (NHL)<br>EV<br>GW S% A GPIMPTSGC BLKTSAS HIT<br>TK<br>ATOI<br>PDOoiSV% oiSH% GVTGFOPS<br>PP<br>CF% relDPS<br>+/− FF% rel PS<br>TGA C60CF%<br>FF%<br>TOI<br>SH<br>FO%<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Discrimination<br>(a) (b)<br>1.0<br>0.8<br>0.6<br>Stability<br>0.4<br>0.2<br>0.0<br><!-- End of picture text -->

Figure 4: Left) Discrimination and stability scores for many NHL metrics. Corsi-based statistics are slightly more reliable than Fenwick statistics. Plus/minus is non-discriminative in hockey because of the paucity of goals scored in a typical game. Right). Fraction of variance explained (R-squared) for each metric by a set of other metrics in our sample. Only 27% of the total variance in takeways (TK) is explained by all other NHL metrics. 

## **5 Constructing Novel Metrics** 

In addition to providing useful benchmarks on the quality of different metrics, the metametrics can motivate the design of new and improved metrics or be used to justify the superiority of new metrics over traditional ones. Here we provide two examples in which novel metrics improve upon existing metrics in at least one of the meta-metrics. In the first example, we use a hierarchical model to shrink empirical estimates of three point ability in basketball. We demonstrate that this model-based estimate is both more stable and discriminative than the simple percentage metric. In the second example, we propose a 

17 



Figure 5: Hierarchical clustering of NHL metrics based on the correlation matrix, _C_ . Clustered metrics have larger absolute correlations but can be positively or negatively associated. The metrics that have large loadings on the two different principal component (Figure 8) are highlighted in red and blue. 

18 

method for creating a set of new metrics that are all mutually independent. 

### **5.1 Shrinkage Estimators** 

Model-based adjustments of common box score statistics can reduce sampling variability and thus lead to improvements in discrimination and stability. In Section 4.1, we showed how three point percentage was one of the least discriminative and stable metrics in basketball and thus an improved estimator of three point making ability is warranted. We define three point ability using the notation introduced in Section 2 as _Esp_ (3 _P_ %)[ _X_ ] , i.e. the expected three point percentage for player _p_ in season _s_ , and propose a model-based estimate of this quantity that is both more stable and discriminative than the observed percentage. 

For this model, we assume an independent hierarchical Bernoulli model for the three point ability of each player: 



where _Xsp_<sup>3</sup><sup>_P_%</sup> is the observed three point percentage of player _p_ in season _s_ , _πsp_ = _Esp_ (3 _P_ %)[ _X_ ] is the estimand of interest, _nsp_ is the number of attempts, _πp_<sup>0=</sup><sup>_Ep_(3</sup><sup>_P_%)[</sup><sup>_X_]isthecareer</sup> average for player _p_ , and _πp_<sup>0(1</sup><sup>_−π_</sup> _p_<sup>0)</sup><sup>_/rp_is the variance in</sup><sup>_πsp_over time.We use the R package</sup> _gbp_ for empirical Bayes inference of _πsp_ and _rp_ , which controls the amount of shrinkage (Kelly and Morris, 2014). In Figure 2 we plot the original and shrunken estimates for LeBron James’ three point ability over his career. 

We can compute discrimination and stability estimates for the estimated three point ability derived from this model using the same approach outlined in Section 3. Although the empirical Bayes’ procedure yields probability intervals for all estimates, we can still compute the frequentist variability using the bootstrap (e.g. see Efron (2015)). In Figure 2 we highlight the comparison between observed three point percentage and the empirical Bayes estimate in red. Observed three point percentage is an unbiased estimate of three point 

19 

ability but is highly unreliable. The Bayes estimate is biased for all players, but theory suggests that the estimates have lower mean squared error due to a reduction in variance (Efron and Morris, 1975). The improved stability and discrimination of the empirical Bayes estimate is consistent with this fact. 

### **5.2 Principal Component Metrics** 

The dependency model proposed in Section 2.3 provides a natural way to derive new metrics that describe orthogonal aspects of player ability. In particular, the eigendecomposition of the latent correlation matrix, _C_ , (Equation 6) can be used to develop a (smaller) set of new metrics, which, by construction, are mutually independent and explain much of the variation in the original set. If the latent normal variables _Z_ defined in Equation 6 were known, then we could compute the principle components of this matrix to derive a new set of orthogonal metrics. The principle components are defined as _W_ = _ZU_ where _U_ is the matrix of eigenvectors of _C_ . Then, by definition, _W ∼_ MVN(0 _, I_ ) and thus _Wk ⊥⊥ Wj ∀ k_ = _j_ . For the independence score defined in Section 2.3, this means that _Ik,MW−k_<sup>=1forall</sup><sup>_k_,</sup> where _M_<sup>_W_</sup> _−k_<sup>isthesetofallmetrics</sup><sup>_Wj_,</sup><sup>_j_=</sup><sup>_k_.Weestimate</sup><sup>_Z_bynormalizing</sup><sup>_X_,thatis</sup> ˆ ˆ _Zspm_ = Φ<sup>_−_1</sup> ( ˆ _Fm_ ( _Xspm_ )) where _Fm_ is the empirical CDF of _Xm_ . Our estimate of the principle components of the latent matrix _Z_ is then simply _W_<sup>ˆ</sup> _sp_ = _Z_<sup>ˆ</sup> _spU_ . We present results based on these new PCA-based metrics for both NBA and NHL statistics. In Figure 7 we list three PCA-based metrics for the NBA and the corresponding original NBA metrics which load most heavily onto them. We also rank the top ten players across seasons according to _W_<sup>ˆ</sup> _sp_ and visualize the scores for each of these three PCA-based metrics for four different players in the 2014-2015 season. Here, the fact that LeBron James ranks highly in each of these three independent metrics is indicative of his versatility. Although the meaning of these metrics can be harder to determine, they can provide a useful aggregation of high-dimensional measurements of player skill that facilitate fairer comparisons of players. 

In Figure 8 we provide two PCA-based metrics for NHL statistics. We again list the metrics that have the highest loadings on two principal component along with the top ten 

20 



<!-- Start of picture text -->
LeBron James three point percentage<br>G Shrunken estimate<br>G Empiricial percentage G G G GGG G GG G G G<br>Career average<br>Number of attempts<br>Posterior sd<br>G GG G G GG G G G<br>0.30 0.35 0.40 0.45<br>95 % Interval<br>0.50<br>0.45<br>0.400.350.30 − G G −− G G −− G G −− G G −− G G −− G −− G G −− G G −− G G −− G G −− G G −− G G<br>−<br>0.25<br>Season<br>3P%<br>2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014<br><!-- End of picture text -->

Figure 6: Three point percentages for LeBron James by season, and shrunken estimates using the empirical Bayes model proposed by Kelly and Morris (2014). Shrinking three point percentage to a player’s career average improves stability and discrimination. 

21 



Stephen Curry 

LeBron James 



DeAndre Jordan 



Kirk Hinrich 

||||**“Shoo**|**tersAssisters”**|**(PC2)**||||
|---|---|---|---|---|---|---|---|---|
|**“Ef**|**cient Shooters” (P**|**C1)**||**,  **|||**High Usage” (PC3**|**)**|
|FG%, <br>2P, 2P<br>|PER, WS, %FG<br>%, BPM, TS%<br>||OBPM<br>%FGA<br>Dist, P|,<br>3PA,<br>AST%,<br>3P,<br>Avg<br>Shot<br>GA||USG, <br>Ball,<br>PTS,|2PA, FGA, Lost-<br>FTA,<br>SfDrawn,<br>And1||
|Rank|Plaer|Year|||||||
||y<br>||Rank|Player|Year|Rank|Player|Year|
||||||||||
|2<br>|wgt owar<br>Dwight Howard<br>|2009<br>|1<br>2|Stephen Curry<br>StephenCurry|2014<br>2013|1<br>2|Allen Iverson<br>Cory Higgins|2006<br>2011|
|3|Dwight Howard<br>|2008|3|<br>SteveNash|2006|3|Kobe Bryant|2014|
|4<br>|Shaquille O’Neal<br>|2000<br>|4|<br>ChrisPaul|2014|4|Allen Iverson|2003|
|5|Shaquille O’Neal<br>|2004<br>|5|<br>SteveNash|2008|5|Russell Westbrook|2014|
|6<br>|Dwight Howard<br>|2007<br>|6|<br>ChrisPaul|2007|6|Tony Wroten|2013|
|7<br>|DeAndre Jordan<br>|2014<br>|7|<br>DamonJones|2004|7|Tony Wroten|2014|
|8<br>9<br>|Amar’e Stoudemire<br>Shaquille O’Neal<br>|2007<br>2003<br>|8<br>9|<br>Steve Nash<br>StephenCurry|2009<br>2012|8<br>9|Allen Iverson<br>Jermaine O’Neal|2004<br>2004|
|10|Tim Duncan|2006|10|<br>LeBron James|2009|10|Allen Iverson|2005|



Figure 7: First three principal components of _C_ . The tables indicate the metrics that predominantly load on the components. Each component generally corresponds to interpretable aspects of player style and ability. The table includes the highest ranking players across all seasons for each component. The top row depicts principal component score for four players players in the 2014-2015 season. LeBron James ranks highly among all 3 independent components. 

22 

players (in any season) by component. The first principal component largely reflects variation in offensive skill and easily picks up many of the offensive greats, including Ovechkin and Crosby. For comparison, we include another component, which corresponds to valuable defensive players who make little offensive contribution. This component loads positively on defensive point shares (DPS) and blocks (BLK), but negatively on shots and goals (S, G). 

||“Ofensive skill”||“|Valuable defenders|”|
|---|---|---|---|---|---|
|PTS,|OPS, GC, PS,||ATOI,|DPS,<br>BLK,||
|TGF,|G,<br>A,<br>EV,||-S, -TS|A, -G, -FA, -||
|PGF,|TSA||CF|||
|Rank|Player|Year|Rank|Player|Year|
|1|Alex Ovechkin|2010|1|Nicklas Lidstrom|2008|
|2|Sidney Crosby|2009|2|Ryan Suter|2014|
|3|Alexander Semin|2008|3|Toby Enstrom|2009|
|4|Daniel Sedin|2000|4|Josh Gorges|2012|
|5|Evgeni Malkin|2011|5|Toni Lydman|2011|
|6|Daniel Sedin|2010|6|Toby Enstrom|2008|
|7|Alex Ovechkin|2007|7|Chris Progner|2010|
|8|Alex Ovechkin|2008|8|Paul Martin|2008|
|9|Sidney Crosby|2012|9|Niclas Havelid|2008|
|10|Marian Hossa|2008|10|Andy Greene|2015|



Figure 8: Player rankings based on two principal components. The first PC is associated with offensive ability. The fact that this is the _first_ component implies that a disproportionate fraction of the currently available hockey metrics measure aspects of offensive ability. The other included component reflects valuable defensive players (large positive loadings for defensive point shares and blocks) but players that make few offensive contributions (negative loadings for goals and shots attempted). The metrics that load onto these components are highlighted in the dendrogram of NHL metrics (Figure 5). 

## **6 Discussion** 

Uncertainty quantification, a hallmark of statistical sciences, has so far been under-appreciated in sports analytics. Our work demonstrates the importance of understanding sources of vari- 

23 

ation and provides a method to quantify how different metrics reflect this variation. Specifically, we explore three different “meta-metrics” for evaluating the reliability of metrics in any sport: discrimination, stability and independence. Our results show that we can use meta-metrics to characterize the most discriminative and stable summaries amongst a set of omnibus metrics (like win shares, BPM and PER for the NBA), which can in turn help decision-makers identify the metrics that are most relevant for a given task. Meta-metrics can also be used as a benchmark for evaluating the improvement of new estimators. For instance, in the case of three point percentage, we demonstrate that an estimate based on a simple hierarchical model can improve the stability _and_ discrimination of standard boxscore statistics. 

In this paper, we focused on reliability and dependence of metrics for _all players in the league_ but the meta-metrics can easily be recalculated for relevant subsets of players. This is important because, as shown, in this context the most reliable metrics are often the metrics which distinguish between player types (e.g., blocks and rebounds in basketball). This may be irrelevant when making decisions involving a specific group of players (e.g., which NBA center to acquire). When using metrics to evaluate players of a certain type, we should compute the meta-metrics conditional on this player type. For instance, there is less variation in the number of blocks and rebounds by NBA centers, and as such, these metrics are less discriminative and stable than they are for the league as a whole. Moreover, the dependence between blocks and rebounds is largely driven by height, and thus the conditional dependence between blocks and rebounds given height is much smaller. Thus, it is important that the meta-metrics are always interpreted in the context of the appropriate group of players. In light of this point, it is notable that the meta-metrics that we present in this paper are stated in terms of expectations and variances, so that estimation of conditional meta-metrics simply requires replacing marginal expectations and variances with their conditional counterparts. 

Another important consideration is that our meta-metrics only measure the internal quality of a metric. The meta-metrics are not designed to provide any information about how relevant the metrics are for the sport of interest. For instance, although we identified Corsi- 

24 

based metrics as more discriminative and stable than the related Fenwick-based metrics, it is still possible that Fenwick metrics are more predictive of team performance. As a more extreme example, an athlete’s birthplace zip code would be perfectly discriminative, stable and independent from all other metrics, but is clearly irrelevant for determining a player’s value to the team. This suggests that in practice coaches and analysts should consider a fourth meta-metric: “relevance”. Relevance could simply be a qualitative description of the metric’s meaning or it could a quantitative summary of the causal or predictive relationship between the metric and an outcome of interest, like wins or revenue generated. Nevertheless, the methods presented here provide a useful characterization of the reliability of existing metrics. We believe that future iterations of the meta-metrics outlined in this paper can become a standard analytical tool that will improve the decisions made and information gleaned from new and old metrics alike. 

25 

## **References** 

- Rob Arthur. Stats cant tell us whether mike trout or josh donaldson should be MVP. `http://fivethirtyeight.com/features/ stats-cant-tell-us-whether-mike-trout-or-josh-donaldson-should-be-mvp/` , 2015. Accessed: 2015-09-30. 

- Benjamin S Baumer, Shane T Jensen, and Gregory J Matthews. openwar: An open source system for evaluating overall player performance in major league baseball. _Journal of Quantitative Analysis in Sports_ , 11(2):69–84, 2015. 

- Darryl Blackport. How long does it take for three point shooting to stabilize? `http: //nyloncalculus.com/2014/08/29/long-take-three-point-shooting-stabilize/` , 2014. Accessed: 2015-09-30. 

- Daniel Cervone, Alex D’Amour, Luke Bornn, and Kirk Goldsberry. A multiresolution stochastic process model for predicting basketball possession outcomes. _arXiv preprint arXiv:1408.0777_ , 2014. 

- Lee J Cronbach. Coefficient alpha and the internal structure of tests. _psychometrika_ , 16(3): 297–334, 1951. 

- Bradley Efron. Frequentist accuracy of bayesian estimates. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 77(3):617–646, 2015. 

- Bradley Efron and Carl Morris. Data analysis using stein’s estimator and its generalizations. _Journal of the American Statistical Association_ , 70(350):311–319, 1975. 

- Bradley Efron and Robert Tibshirani. Bootstrap methods for standard errors, confidence intervals, and other measures of statistical accuracy. _Statistical science_ , pages 54–75, 1986. 

- Ronald Aylmer Fisher. _Statistical methods for research workers_ . Genesis Publishing Pvt Ltd, 1925. 

26 

- Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Counterpoints: Advanced defensive metrics for NBA basketball. In _Proceedings of the 2015 MIT Sloan Sports Analytics Conference_ . MIT Sloan Sports Analytics Conference. Boston, MA, 2015. 

- Peter Hoff. _sbgcop: Semiparametric Bayesian Gaussian copula estimation and imputation_ , 2012. URL `http://CRAN.R-project.org/package=sbgcop` . R package version 0.975. 

- Peter D Hoff. Extending the rank likelihood for semiparametric copula estimation. _The Annals of Applied Statistics_ , pages 265–283, 2007. 

- Joseph Kelly and Carl Morris. Rgbp: An r package for gaussian, poisson, and binomial hierarchical modeling. _Journal of Statistical Software_ , VV(Ii), 2014. 

- G Frederic Kuder and Marion W Richardson. The theory of the estimation of test reliability. _Psychometrika_ , 2(3):151–160, 1937. 

- Michael Lewis. _Moneyball: The art of winning an unfair game_ . WW Norton & Company, 2004. 

- Kantilal Varichand Mardia, John T Kent, and John M Bibby. _Multivariate analysis_ . Academic press, 1980. 

- Dean Oliver. _Basketball on paper: rules and tools for performance analysis_ . Potomac Books, Inc., 2004. 

- Melissa Peterson. Corsi vs. Fenwick: How are they different and when do i use them? `http://faceoffviolation.com/dekestodangles/2014/11/19/ corsi-vs-fenwick-different-use/` , 2014. Accessed: 2016-09-06. 

- Joseph Sill. Improved NBA adjusted plus-minus using regularization and out-of-sample testing. In _Proceedings of the 2010 MIT Sloan Sports Analytics Conference_ , 2010. 

- Sports Reference LLC. Basketball-Reference.com - basketball statistics and history. `http: //www.basketball-reference.com/` , 2016a. 

27 

- Sports Reference LLC. Hockey-Reference.com - hockey statistics and history. `http://www. hockey-reference.com/` , 2016b. 

- Dawson Sprigings. donttellmeaboutheart.blogspot.com/ - How Long Does It Take For A Forward’s Shooting To Stabilize? `http://donttellmeaboutheart.blogspot.com/2014/ 12/how-long-does-it-take-for-forwards.html` , 2014. Accessed: 2015-09-30. 

28 

## **Appendix** 

Figure 9: Hierarchical clustering of NBA metrics based on the correlation matrix, _C_ . Clustered metrics have larger absolute correlations (e.g. can be positively or negatively related) 

Dependencies between NBA Metrics 



<!-- Start of picture text -->
BLK<br>%FGA Dunks<br>ORB<br>DRB<br>TRB<br>Avg Shot Dist<br>%FGA 0−3<br>%FGA 2P<br>3PA<br>3PAr<br>%FGA 3P<br>FG%<br>2P%<br>%FG 2P<br>%FG 0−3<br>OBPM<br>OWS<br>WS<br>BPM<br>VORP<br>TS%<br>ORtg<br>PER<br>WS/48<br>%3PA − Corner<br>3P%<br>%FG 3P<br>OnCourt<br>On−Off<br>%FGA 10−16<br>%FG 3−10<br>%FG 10−16<br>%FG 16<3<br>TOV%<br>TOV − LostBall<br>Made Dunks<br>%Ast'd 3P<br>PF − Blocking<br>3P% − Corner<br>PF − Take<br>STL<br>DWS<br>Blkd<br>And1<br>FTA<br>SfDrawn<br>2PA<br>PTS<br>FGA<br>USG%<br>FT%<br>%FGA 16<3<br>FTr<br>%FGA 3−10<br>TOV − Other<br>PF − Offensive<br>DBPM<br>DRtg<br>PF<br>PF − Shooting<br>%Ast'd 2P<br>TOV − BadPass<br>AST<br>PGA<br><!-- End of picture text -->

29 



<!-- Start of picture text -->
All NBA Metrics Omnibus NBA Metrics Defensive NBA Metrics<br>0 10 20 30 40 50 60 70 1 2 3 4 5 1 2 3 4 5<br>Number of Components Number of Components Number of Components<br>1.0 1.0 1.0<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>Variance Explained Variance Explained Variance Explained<br>0.0 0.0 0.0<br><!-- End of picture text -->

Figure 10: Total variance explained, _Fk_ vs number of principal components used. When evaluating the dependencies among all 70 metrics, we can explain over 75% of the total variability using only 15 components. For a subset of five omnibus metrics, the first PC explains 73% of the variation, indicating a high level of redundancy. For a set of five defensive metrics, the first component explains 50% of the variance. 

**All NHL Metrics** 



<!-- Start of picture text -->
0 10 20 30 40<br>Number of Included Metrics<br>1.0<br>0.8<br>0.6<br>0.4<br>Independence<br>0.2<br>0.0<br><!-- End of picture text -->

Figure 11: Total variance explained, _Fk_ by number of principal components for 40 NHL metrics. We can explain over 90% of the total variability using only 15 components. 

30 

## **Proof of** 0 _≤Sm ≤_ 1 

We calculate stability for metric _m_ (4) as 



To show 0 _≤Sm ≤_ 1, it suffices to show both 





To verify (A), we can write 



To check (B), note that 



31 

## **Glossary of Metrics** 

Table 1: Glossary of NBA metrics used. All stats are per 36 minutes unless otherwise noted. See (Sports Reference LLC, 2016a) for more detail. 

|Metric|Description|
|---|---|
|MP|Minutes played|
|FGA|Field goal attempts|
|FG%<br>|Field goal percentage<br>|
|3PA<br>|3 point attempts|
|3P%|3 point percentage|
|2PA|2 point attempts|
|2P%|2 point percentage|
|FTA|Free throw attempts|
|FT%|Free throw percentage|
|PF|Personal fouls|
|PTS|Points|
|PER|Personal efciency rating|
|TS%|True shooting percentage|
|3PAr|Three point attempt rate|
|FTr|Free throw attempt rate|
|ORB|Ofensive rebounds|
|DRB|Defensive rebounds|
|TRB|Total rebounds|
|AST|Assists|
|STL|Steals|
|BLK|Blocks|
|TOV%<br>|Turnover percentage (per possession)|
|USG%|Usage per|
|OWS|Ofensive win shares|
|DWS|Defensive win shares|
|WS|Win shares|
|WS/48|Win shares per 48 minutes|
|OBPM|Ofensive box plus minus|
|DBPM|Defensive box plus minus|
|BPM|Box plus minus|
|VORP|Value over replacement|
|ORtg|Ofensive rating|
|DRtg|Defensive rating|
|Avg Shot Dist|Average shot distance|



32 

Table 2: NBA Glossary cont. 

|Metric|Description|
|---|---|
|%FGA 2P<br>%FGA 0-3|percentage of feld goal attempts that are 2 pointers<br>percentage of feld goal attempts within 0-3 feet|
|%FGA 3-10|percentage of feld goal attempts within 3-10 feet|
|%FGA 10-16<br>%FGA 16_<_3|percentage of feld goal attempts within 10-16 feet<br>percentage of feld goal attempts between 16 feet and the 3 point line|
|%FGA 3P<br>%FG 2P|percentage of feld goal attempts that are 3 pointers<br>percentage of made feld goals that are 2 pointers|
|%FG 0-3<br>%FG 3-10|percentage of made feld goals within 0-3 feet<br>percentage of made feld goals within 3-10 feet|
|%FG 10-16<br>%FG 16_<_3|percentage of made feld goals within 10-16 feet<br>percentage of made feld goals between 16 feet and the 3 point line|
|%FG 3P|percentage of made feld goals that are 3 pointers|
|%Ast’d 2P<br>%FGA Dunks<br>Made Dunks<br>%Ast’d 3P|percentage of made 2 point feld goals that are assisted<br>percentage of feld goal attempts that are dunks<br>made dunks (per 36 MP)<br>percentage of made 3 point feld goals that are assisted|
|%3PA - Corner<br>3P% - Corner|percentage of 3 point feld goal attempts taken from the corner<br>3 point feld goal percentage from the corner|
|OnCourt|plus/minus per 100 possessions|
|On-Of|plus/minus net per 100 possession|
|TOV - BadPass|turnovers from bad passes|
|TOV - LostBall|turnovers due to lost ball|
|TOV - Other|all other turnovers (traveling, out of bounds, etc)|
|PF - Shooting|shooting fouls committed|
|PF - Blocking|blocking fouls committed|
|PF - Ofensive<br>PF - Take|ofensive fouls committed<br>take fouls committed|
|PGA|points generated by assists|
|SfDrawn|shooting fouls drawn|
|And1|shots made on fouls drawn|
|Blkd|feld goal attempts that are blocked|



33 

Table 3: Glossary of hockey metrics used. All metrics are normalized by total time on ice (TOI) unless otherwise noted. 

|metric|description|
|---|---|
|G|goals|
|A|assists|
|PTS|points|
|_±_|plus / minus<br>|
|PIM|penalties in minutes|
|EV|even strength goals|
|PP|power play goals|
|SH|short handed goals|
|GW|game winning goals|
|S|shots on goal|
|S%|shooting percentage|
|TSA|total shots attempted|
|TOI|time on ice|
|FO%|face of win percentage|
|HIT|hits at even strength|
|BLK|blocks at even strength|
|TK|takeways|
|GV|giveaways|
|GC|goals created|
|TGF|total goals for (while player was on the ice)|
|PGF|power player goals for (while player was on the ice)|
|TGA|total goals against (while player was on the ice)|
|PGA|power player goals against (while player was on the ice)|
|OPS|ofensive point shares|
|DPS|defensive point shares|
|PS|total point shares|
|CF|Corsi for (on ice shots+blocks+misses)<br>|
|CA|Corsi against (on ice shots+blocks+misses)|
|CF%|Corsi for percentage: CF / (CF + CA)|
|CF% rel|Relative Corsi for (on ice CF% - of ice CF%)|
|FF|Fenwick for (shots+blocks+misses)|
|FA|Fenwick against (shots+blocks+misses)|
|FF%|Fenwick for percentage: FF / (FF + FA)|
|FF% rel|Relative Fenwick for (on ice FF% - of ice FF%)|
|oiSH%|Team on ice shooting percentage while player on the ice|
|oiSV%|Team on ice save percentage while player on the ice|
|PDO<br>|Shooting percentage plus save percentage|
|oZS%|percentage of ofensive zone starts while on the ice|
|dZS%|percentage of defensive zone starts while on the ice|



34 


