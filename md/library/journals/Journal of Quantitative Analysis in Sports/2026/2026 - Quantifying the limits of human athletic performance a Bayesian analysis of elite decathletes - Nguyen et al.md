<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2026/2026 - Quantifying the limits of human athletic performance a Bayesian analysis of elite decathletes - Nguyen et al.pdf -->

J. Quant. Anal. Sports 2026; aop 

#### **Research Article** 

Paul-Hieu V. Nguyen*, James M. Smoliga, Benton Lindaman and Sameer K. Deshpande 

# **Quantifying the limits of human athletic performance: a Bayesian analysis of elite decathletes** 

https://doi.org/10.1515/jqas-2026-0026 Received February 18, 2026; accepted May 12, 2026; published online June 1, 2026 

**Abstract:** Because the decathlon tests many facets of athleticism, including sprinting, throwing, jumping, and endurance, many consider it to be the ultimate test of athletic ability. On this view, estimating the maximal decathlon score and understanding what it would take to achieve that score provides insight into the upper limits of human athletic potential. To this end, we develop a Bayesian composition model for forecasting how individual decathletes perform in each of the 10 decathlon events of time. Besides capturing potential non-linear temporal trends in performance, our model carefully captures the dependence between performance in an event and all preceding events. Using our model, we can simulate and evaluate the distribution of the maximal possible scores and identify profiles of decathletes who could realistically attain scores approaching this limit. 

**Keywords:** age-curves; simulation; uncertainty quantification 

***Corresponding author: Paul-Hieu V. Nguyen** , Department of Statistics, University of Wisconsin–Madison, 1205 University Avenue, Madison, WI 53706, USA, E-mail: pvnguyen5@wisc.edu. https://orcid.org/0009-0006-6578-9163 **James M. Smoliga and Benton Lindaman** , Department of Rehabilitation Sciences, Tufts University, Seattle, WA, USA, E-mail: james.smoliga@tufts.edu (J. M. Smoliga), benton.lindaman@tufts.edu (B. Lindaman) **Sameer K. Deshpande** , Department of Statistics, University of Wisconsin–Madison, 1205 University Avenue, Madison, WI 53706, USA, E-mail: sameer.deshpande@wisc.edu. https://orcid.org/0000-0003-4116-5533 

## **1 Introduction** 

#### **1.1 Motivation: realistic max decathlon score** 

The decathlon is a combined track-and-field event consisting of ten disciplines spread over two days. These events test multiple facets of athletic ability, including sprinting, jumping, throwing, technique, and endurance. The decathlon is widely regarded as the ultimate test of athletic ability due to its diversity of events and demand on both the body and mind (Edouard et al. 2010). The order of events is consistent for each decathlon. Though technique is valuable for each discipline, we note that generally, day one emphasizes explosiveness – decathletes compete in the 100 m, long jump (LJ), shot put (SP), high jump (HJ), and 400 m – while day two focuses on technique and endurance, featuring the 110 m hurdles, discus throw (DT), pole vault (PV), javelin throw (JT), and 1,500 m. Decathletes earn points based on their performance in each discipline based on a scoring table developed by the World Athletics. Their overall decathlon score is the sum of each event’s points. The scoring system is designed to balance high-level performances with overall competence. Excelling in only a single discipline will produce exponentially increasing rewards for that event, while underperformance in other events diminishes the overall score. 

More specifically, let _Y e_ measure a decathlete’s performance in event _e_ . For track events (i.e., the 100 m, 400 m, 110 m hurdles, or 1,500 m), _Y e_ is a time and smaller values of _Y e_ correspond to better performance. For all others (i.e., LJ, SP, HG, DT, PV, and JT), _Y e_ is distance and larger values correspond to better performance. Decathletes earn _ae_ − ( _be_ − _Ye_ )<sup>_ce_</sup> points for track events and _ae_ − ( _Ye_ − _be_ )<sup>_ce_</sup> points for all other events, where _ae, be_ , and _ce_ are event-specific coefficients (see Table A3). 

Figure 1 shows the best decathlon scores from 2001 to 2022, with world records by Roman Šerble (2001), Ashton Eaton (2012 and 2015), and Kevin Mayer (2019). These 

Open Access. © 2026 the author(s), published by De Gruyter. 

This work is licensed under the Creative Commons Attribution 4.0 International License. 

> **2 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 



**Figure 1:** Top decathlon scores from 2001 to 2022. We highlight the previous world record holders and scores. All decathlon performances greater than 8,500 are included in this graph ( _n_ = 126). 

decathletes differ in their event-specific strengths, with Šerble excelling in jumping events and javelin throw, Eaton excelling in sprinting, and Mayer doing well across all disciplines. Mayer broke the previous world record by roughly 80 points. Given these trends, we ask whether a new performance threshold, say another 80 point increase for a 9,200 point total, is realistically attainable, and what combination of event abilities would be required to achieve 9,200 points. 

Based on World Athletics scoring table, if a decathlete managed to attain world-record performance in each individual event, their score would be 12,676. Of course, it is unrealistic to expect a decathlete to perform at a worldrecord level in all ten disciplines. If, on the other hand, a decathlete managed to attain the highest score in each event _that has ever been observed specifically in a decathlon_ , their score would be 10,669. Even this hypothetical is unrealistic as it requires a decathlete to attain peak performance in all disciplines at exactly the same time. Intuitively, we would expect individual event performance to vary with age (Villaroel et al. 2011), with performance peaking in different events at different times. 

Motivated by this, we build age curves for individual decathlete’s performances in each discipline. By applying World Athletics’ scoring table to forecasted individual event performances, we can predict an individual decathlete’s overall score over the course of their career. To capture the inter-event dependencies, we specifically fit _compositional_ 

age curves in which performance in one discipline depends not only on a non-linear function of age but also on performance in the immediately preceding disciplines. That is, our model for LJ performance depends on the observed 100 m. We take a Bayesian approach, which allows us to quantify and propagate uncertainty about forecasted discipline performance through to final decathlon score in a coherent fashion. 

#### **1.2 Related literature** 

The majority of prior research on the decathlon has been descriptive in nature, focusing on clustering different disciplines (Cox and Dunn 2002; Schomaker and Heumann 2011; Walker and Caddigan 2015; Woolf et al. 2007) and creating archetypes of decathletes who perform similarly across different discipline clusters (Dziadek et al. 2022; Kenny et al. 2005; Van Damme et al. 2002). Cox and Dunn (2002), for instance, applied multiple clustering and dimension scaling methods to group decathlon events, broadly separating the track disciplines and JT from the field disciplines. They noted that the HJ, PV, JT, and 1,500 m were not as consistent with cluster membership compared to other events. Woolf et al. (2007) used cluster analysis based on personal best performances of elite decathletes and suggest track athletes may have a scoring advantage. Schomaker and Heumann (2011) analyzed data from the 2004 Olympics using factor analysis and identified three 

P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 3** 

main groups, one each for speed, strength, and endurance events. Other authors have analyzed decathlon performance using principal component analysis (PCA). Park and Zatsiorsky (2011) identified latent structures across events while Dziadek et al. (2022) tracked how the structure of the decathlon shifts over a decathlete’s career and found that decathletes broadly shifted from generalists to specializing in particular events. This finding may be a result of data availability across different stages of different decathletes’ careers. 

Several authors have attempted to identify trade-offs between specializing in different disciplines. Van Damme et al. (2002) found some evidence of antagonistic traits, as well as tradeoffs between specialist and generalist phenotypes. Aoki et al. (2015) found physiological differences between athletes specializing in sprinting and jumping, though their analysis is not directly focused on the decathlon. Kenny et al. (2005), Walker and Caddigan (2015) argue that there is no evidence of event trade-offs when looking at the subpopulation of elite decathlon performers: top athletes perform uniformly well across all events, and they found positive correlation between all decathlon events. Park and Zatsiorsky (2011) comment that the outcomes of these experiments differ between methods and sample, and their analysis agrees with Kenny et al. (2005). 

Fewer studies have explored the decathlon from a predictive standpoint. Battles et al. (2025) use gamma regression to model a decathlete’s career best using early-career decathlon performances. They found that the results from PV, JT, LJ, and SP were especially predictive of future performance. To the best of our knowledge, Wimmer et al. (2011) is the only other Bayesian analysis of decathlon data. They fit semi-parametric latent variable models to cluster disciplines and model the effects of age, season, and year on decathlon results. 

Age-performance relationships have also been explored outside of the decathlon. Researchers have sought to identify ages for peak performance in hockey (Brander et al. 2014; Schuckers et al. 2023), baseball (Fair 2008), golf (Baker and McHale 2023), and the triathlon (Villaroel et al. 2011). Griffin et al. (2022) use a Bayesian analysis to model individual sprinting and weightlifting events. 

#### **1.3 Our contributions** 

We introduce a compositional Bayesian model to account for the multi-event, dependent nature of the decathlon. We model a decathlete’s scores in an event as a function of the decathlete’s age, their preceding-event scores within the same decathlon, and decathlete-specific random intercepts. We compare multiple models, with varying 

levels of flexibility and granularity, in an extensive set of experiments. We show that compositional models accurately predict decathlon scores and allow for greater interpretability, enabling researchers to study relationships between events, than simpler models. Using our probabilistic models, we obtain personalized decathlon and eventspecific age curves to develop training programs, set goals for competitions, and model potential for future success. We further develop several real and synthetic decathlete profiles, based on latent abilities in each individual decathlon event, and we simulate decathlon performances to investigate the distribution of decathlon scores from these decathlete profiles. Through these simulations, we show that breaking the 9,200 point threshold is unlikely, but still possible. 

## **2 Data and model** 

#### **2.1 Data** 

Our dataset contains the overall score and the results from each individual discipline from all completed decathlons between 2001 and 2022. These data were initially provided by World Athletics and were later analyzed and distributed by Battles et al. (2025).<sup>1</sup> The data contains observations from all decathlon performances with overall scores greater than 7,000 for 2001–2008, greater than 6,600 for 2009, and above 6,400 for the years 2010–2022. We further truncated the data to include performances from only those decathletes who scored 6,400 points or more at least four times. This threshold is somewhat lower than Battles et al. (2025), who kept only those decathletes who completed a decathlon in at least four seasons, and allows us to model a wider range of development trajectories. We note that previous decathlon analyses’ results have differed depending on the method and sample (Kenny et al. 2005; Park and Zatsiorsky 2011; Van Damme et al. 2002). We standardized each individual discipline’s performance to have a mean of zero and standard deviation of one. Our final dataset includes 8,668 decathlon performances from 1,007 unique decathletes. 

#### **2.2 Modeling decathlon performance over time** 

To predict how a decathlete’s overall scores evolve over the course of their career and to account for the fact 

> **1** The data is available at https://github.com/Battles186/DecathlonCareerBest.git. 

> **4 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 

that we have multiple observations per decathlete, we can fit a simple age curve with decathlete-specific random intercepts. Letting _Pi, j_ be the total score earned by decathlete _i_ in decathlon _j_ , a simple starting model asserts 



> where _𝛼i_ is a decathlete-specific random intercept, { _𝜙_ 1(⋅) _,_ … _, 𝜙D_ (⋅)} is some pre-specified basis of non-linear functions of age, and age _i, j_ is the age of decathlete _i_ when they completed decathlon _j_ . To fit this model, we take a Bayesian approach based on the following relatively weakly informative priors, which we specify _after_ standardizing the observed _Pi, j_ values to have mean zero and variance one: 





While it is relatively straightforward to fit the age curves in Equation (1) and to use them to identify when a given decathlete’s performance will peak, simply modeling the overall points provides no insight into _how_ a given decathlete can obtain that peak. That is, with such a simple model, it is impossible to determine whether a decathlete’s forecasted performance is due to improved performance in any particular discipline. So, we instead model the outcomes of the individual events. Specifically, let _Y i, j,e_ record the performance of decathlete _i_ in discipline (hereafter “event”) _e_ in decathlon _j_ . Then a natural model for individual event performances asserts for each _i, j_ and _e_ that 



where the _𝛼i,e_ ’s are random intercepts specific to each combination of decathlete and event. Because the model in Equation (2) features event-specific basis coefficients _𝛽 e,d_ , it is flexible enough to allow the temporal evolution of individual event performances to vary across events. In other words, the model in Equation (2) allows for decathletes to obtain peak performance in different disciplines at different times. 

To fit the model in Equation (2), we specify the priors 



Despite its intuitive appeal, the model in Equation (2) implicitly assumes that performance in each event is independent of performance in all other events. Given the sequential nature of the decathlon – namely, the events are run in the same, fixed order – it is natural to suspect that individual event performances are not independent due to factors like fatigue and event similarity. For instance, a decathlete’s performance in the 100 m may impact their performance in the 400 m, which takes place on the same day. Beaulieu et al. (1995) found that decathletes’ blood lactate levels differed before each event and were particularly high before the 400 m. To better capture inter-event dependencies, we propose a _compositional_ elaboration of the model in Equation (2) in which performance in each event depends on performance in all preceding events: 



To illustrate the difference between the models in Equation (2) and Equation (3), consider modeling shot put (SP) performance. Whereas the simple model in Equation (2) only uses decathlete age and identity to model SP performance, the composition model in Equation (3) additionally accounts for performance in the long jump (LJ) and 100 m, which take place immediately before SP. In this context, the coefficient _𝛾_ 100m _,SP_ captures, up to scaling, the conditional correlation between 100 m performance and SP performance holding age and LJ performance fixed. If there is a positive (resp. negative) conditional correlation – that is, if running a faster 100 m is associated with achieving longer (resp. shorter) shot put distances – we would expect _𝛾_ 100m _,SP_ to be negative (resp. positive). On the other hand, if there is essentially no conditional dependence between sprinting and shot putting 

P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 5** 

abilities, we would expect _𝛾 SP,_ 100m to be close to zero. This is an alternate representation of the grouped structure previously explored within the decathlon literature by Cox and Dunn (2002), Schomaker and Heumann (2011), Woolf et al. (2007). Our approach reflects how the decathlon is physically performed, whereas other types of analyses do not account for the sequential nature of the competition. 

We specify analogous priors for the parameters in Equation (3) as we did for Equation (2): 



## **3 Posterior inference and simulated performance** 

#### **3.1 Model comparison and validation** 

**Model comparison** . We fit each model using the **rstan** (Stan Development Team 2025) interface to Stan. We used the package defaults, simulating four Markov chains for 2,000 iterations each and discarding the first 1,000 iterates as “burn-in.” We performed a 10-fold cross-validation study to compare the predictive performance of two versions of each model, one that set { _𝜙d_ } to be a cubic polynomial basis and one that set { _𝜙d_ } to be a cubic splines basis with interior knots at age deciles. 

We compared the out-of-sample predictive accuracy on real decathlon data for each version of each model in two ways. First, which we call the “general” case, we created ten 90–10 % training/testing splits where individual decathlete observations were randomly held out in the test set. In the second framework, which we call the “tail” case, we held out just the last observed decathlon for a random 10 % of the decathletes. Generally speaking, all models achieved very similar out-of-sample mean square errors in both cases; see Tables A4 and A5 for full tabulations. In the general case, the average out-of-sample standardized mean square error (SMSE<sup>2</sup> ) for the baseline points model in Equation (1) 

> **2** Standardized mean square error is the mean square error divided by the variance of the training set responses. A model with worse predictive performanance than another model will have a larger SMSE. A model with perfect out-of-sample accuracy will have an SMSE of 

was 0.234 and 0.235 using the cubic polynomial and cubic splines basis. Both versions of the simple (Equation (2)) and compositional (Equation (3)) models achieved mean out-ofsample SMSEs of 0.235. In the “tail” case, we found that the baseline points model with cubic polynomial basis had everso-slightly smaller SMSE than the compositional model with the same non-linearities (0.358 vs 0.362). In this setting, we found that modeling the age-event relationship with a cubic polynomial tends to perform slightly better than modeling with a spline. 

Although our compositional model with a cubic polynomial basis had slightly worse predictive performance than the baseline model for overall points, it provides much more insight into the underlying inter-event dynamics. To support this choice further, we conducted two additional simulation studies that verify the ability of the compositional model to detect inter-event dependencies when present. 

**Ability to recover model parameters.** First, we demonstrate that the compositional model was powered to recover the model parameters. At a high-level, we fixed values of all parameters in Equation (3), generated 200 synthetic datasets of the same size as our decathlon dataset, fit our model to those synthetic datasets, and assessed how well we estimated the data-generating parameter values. We specifically assessed the extent to which the 95 % posterior credible intervals for each parameter covered the true data-generating parameter values. Generally speaking, with the single exception of the coefficient for JT when modeling PV (90.5 %), the vast majority of the intervals displayed nearnominal 95 % coverage; see Table A6 for a full tabulation. Overall, the high coverage across virtually all predictors suggests that the model is well-calibrated for recovering inter-event relationships. 

**Posterior predictive checks.** Once we fit our simple and compositional model with cubic polynomial basis, we generated 2,000 decathlon datasets from the posterior predictive distribution using the same decathletes and ages as in the observed data. Using these simulated datasets, we computed the posterior predictive correlation between every pair of individual events. The colored boxplots in Figure 2 show the posterior predictive distribution of these correlations for selected pairs of events for both models, with the true observed correlation represented with a red line. We see that the true observed inter-event correlations from the original data lie squarely in the middle of the posterior predictive distributions corresponding to the compositional model. In sharp contrast, the simple model, 

> 0, whereas a baseline naive model that simply predicts the average response will have an SMSE of 1. 

> **6 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 



**Figure 2:** Boxplots depicting the posterior predictive correlations for the simple and compositional models over 2,000 simulated datasets between the 100 m and long jump (top) and javelin and long jump (bottom). For each model, the 25th, 50th, and 75th percentile is marked in the boxplot. The empirical correlation from the observed data is marked with a red line. 

which does not explicitly model inter-event dependencies, induces posterior predictive distributions over correlations that are concentrated away from and weaker than the actually observed correlations. 

#### **3.2 Studying inter-event relationships** 

To better understand the relationship between any two events, we can examine the posterior distributions of their modeled coefficient. Figure 3 displays the distributions of the effect of the 100 m sprint on 1,500 m performance. Our model estimates this relationship to be antagonistic. That is, an improvement of 0.1 s in the 100 m, after accounting for age and the sequential effects of preceding events, is associated with an expected increase of 0.45 min in the 1,500 m. 

Before proceeding, we pause to stress that these associations are not necessarily causal. A positive coefficient between the 100 m and long jump may arise from shared underlying attributes or an emphasis on, say, anaerobic training, rather than a direct transfer of skill from one event to another. This is particularly relevant given that our dataset consists only of top decathlon performances, where 

decathletes are typically competitive across all events. Stemmler and Baumler (2005) found that while all-rounders generally achieve higher scores than specialists, atheletes who excel in only one or two types of events (e.g., sprinting) can still achieve high scores. Consequently, these coefficients may be better interpreted as indicators of general performance patterns at the elite level rather than isolated event-on-event effects. 

Table 1 contains the posterior mean regression event coefficients for each decathlon discipline. For instance, the posterior mean coefficient corresponding to 100 m, when modeling LJ, is −0.48. Positive coefficients whose 95 % credible interval do not contain 0 are bolded. Our results are comparable to previous grouping analyses of the decathlon. Similar to Cox and Dunn (2002), Schomaker and Heumann (2011), Woolf et al. (2007), we find evidence of a grouping of ‘speed’ events, namely 100 m, LJ, SP, 400 m, 110 mH. We also find a grouping for ‘throwing’ events - note that the coefficients highlighted in JT column include SP and DT, that the highlighted coefficient for the DT is SP, and that these coefficients are all positive. In contrast to the previous approaches, our model depicts 1,500 m with stronger relationships with 400 m and JT. 

P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 7** 



**Figure 3:** Histogram of posterior draws of _𝛽_ associated with 100 m for prediction of 1,500 m. 

**Table 1:** Posterior mean regression coefficients by event. The _i, j_ ’th entry represents the coefficient corresponding to event _i_ when modeling event _j_ . Positive coefficients whose 95 % credible interval do not contain 0 have been bolded. 

|**Event**|**LJ**|**SP**|**HJ**|**400 m**|**110 mH**|**DT**|**PV**|**JT**|**1,500 m**|
|---|---|---|---|---|---|---|---|---|---|
|100 m|−0.48|−0.14|−0.09|**.**|**.**|−0.03|−0.07|0.00|−0.09|
|LJ|–|**.**|**.**|−0.11|−0.09|0.00|**.**|**.**|−0.03|
|SP|–|–|**.**|−0.08|−0.09|**.**|**.**|**.**|**.**|
|HJ|–|–|–|−0.05|−0.07|**.**|**.**|**.**|−0.06|
|400 m|–|–|–|–|**.**|0.00|−0.09|−0.04|**.**|
|110 mH|–|–|–|–|–|−0.08|−0.12|−0.03|**.**|
|DT|–|–|–|–|–|–|**.**|**.**|0.00|
|PV|–|–|–|–|–|–|–|**.**|−0.07|
|JT|–|–|–|–|–|–|–|–|−0.12|



#### **3.3 Simulating decathlon performance over time** 

We can forecast the entire arc of an individual decathlete’s career with a posterior predictive simulation. Specifically, for a given decathlete, _i_ , posterior sample, _s_ , and age, we simulate a single decathlon performance as follows. First, we simulate their 100 m performance at that age by drawing 



Then, having simulated their 100 m performance time at that age, we can simulate their long jump performance by drawing 





At the end, we obtain a single sample from the posterior predictive distribution of performance in each event of a single decathlon, which we can then convert into a single 

> **8 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 



**Figure 4:** Posterior predictive shotput (left) and 400 m (right) intervals for selected decathletes. The shaded areas represent the 95 % posterior predictive interval for each respective model, and the solid line depicts the posterior mean. Each dot represents an observation for a given decathlete. Greater distances for shot put and faster times for the 400 m correspond to more points. 

overall score using Table A3. Repeating this for every age in a fixed grid, and with every sample from the posterior distribution of the model parameters, yields a posterior distribution over each decathlete’s age curve. Importantly, our posterior predictive simulation strategy propagates and combines not only uncertainty about model parameters but the inherent variability in actual event performance. 

Figure 4 shows the point-wise posterior predictive mean and 95 % uncertainty intervals for several decathletes’ age curves. Ashton Eaton, Romain Barras and Brendt Newdick are highlighted in Figure 4 to compare progressions of decathletes with performances consistently across our age range. Reassuringly, the observed performances tend to lie within the point-wise 95 % predictive intervals. We also see benefits of modeling each event individually. The shapes of each age curve differ for different events. SP distances improve steadily over time while 400 m times improve and then degrade over time. Further, while decathletes display their peak SP distances in the later stages of their careers, their 400 m times are predicted to peak in their early-20’s. 

#### **3.4 Measuring latent skill** 

Recall that our models assume that for each event, random decathlete intercepts are drawn from a latent normal population with event-specific means and variances. This 

population, in some sense, captures the range of latent ability in each event, and the decathletes in our analysis can be viewed as a sample from the underlying population. 

To evaluate decathlete-specific latent skill in an event, we use the posterior distribution of decathlete-level random intercepts from our hierarchical model. Since slopes for age and other covariates are shared across decathletes, these intercepts capture persistent decathlete-level differences in event performance. For any given decathlete in our sample, we assess their latent skill in each event by computing the z-score and percentile associated with their event-intercept within the overall posterior distribution of decathlete random intercepts. Figure 5 visualizes the posterior distribution of the Ashton Eaton’s and Kevin Mayer’s percentile within the latent population of skill in each discipline. We find that Eaton is among the elite at the 100 m, LJ, and 400 m, while Mayer is generally better than Eaton on the Day 2 events (hurdles, DT, PV, JT, and 1,500 m). 

Figure 6 plots the posterior mean quantile for each decathlete’s latent skill in the 400 m and 1,500 m. We find that Eaton ranks above the 90th-percentile in terms of his latent 400 m skill but is in the middle-of-the-pack for the 1,500 m. Mayer, by contrast, is above average in both events but not to a large degree. Their examples suggest that achieving high decathlon scores does not require elite performance in all events. 

P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 9** 



**Figure 5:** Boxplots of quantiles for event intercepts for Ashton Eaton and Kevin Mayer across 4,000 MCMC samples. 



**Figure 6:** Mean posterior intercept percentiles in the 400 m and 1,500 m for all decathletes, with selected decathletes highlighted. The 50th percentile for each event is marked with a red line. 

#### **3.5 Decathlete profiles – breaking 9,200** 

In Section 3.4, we calculated the mean posterior eventintercept percentiles in each event for selected decathletes 

in our sample. We refer to this collection of posterior mean percentiles as a decathlete’s _profile_ . Table 2 shows the profiles for the five decathletes with the highest scores in our dataset. Given any profile (i.e., any combination of 10 

> **10 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 

**Table 2:** Profiles of last world record holders and synthetic decathletes. Entries consist of each event’s intercept percentile. We calculate the proportion of simulated careers in which a decathlete with the given profile breaks 9,200 points. 

|**Name**|**100** **m**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|**9,200?**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|K. Mayer|0.88|0.94|0.91|0.85|0.66|0.85|0.88|0.92|0.93|0.62|7.7|
|A. Eaton|1.00|0.94|0.40|0.60|0.95|0.78|0.65|0.74|0.44|0.49|5.65|
|R. Šebrle|0.91|1.00|0.92|0.94|0.77|0.55|0.79|0.57|0.95|0.35|10.325|
|D. Warner|1.00|0.71|0.52|0.67|0.57|0.90|0.82|0.26|0.77|0.44|1.825|
|R. Dvořák|0.92|0.95|0.97|0.55|0.69|0.74|0.44|0.34|0.96|0.67|0.6|
|Day 1|0.95|0.95|0.95|0.95|0.95|0.50|0.50|0.50|0.50|0.50|2.4|
|Day 2|0.50|0.50|0.50|0.50|0.50|0.95|0.95|0.95|0.95|0.95|0|
|Excellent|0.95|0.95|0.95|0.95|0.95|0.95|0.95|0.95|0.95|0.95|99.95|
|Good|0.80|0.80|0.80|0.80|0.80|0.80|0.80|0.80|0.80|0.80|0.075|



quantiles), we can simulate a career’s worth of decathlons for a hypothetical decathlete with that profile using a procedure very similar to the one described in Section 3.3. Specifically, for each posterior sample _s_ , we set the random intercept _𝛼e_<sup>_s_tothecorrespondingquantileofthe</sup> ( _𝜇e_<sup>(</sup><sup>_s_)</sup><sup>_, 𝜎_</sup> _𝛼,_<sup>2(</sup> _e_<sup>_s_)</sup> ) distribution. Then, we simulate 2 decathlons for every year between the ages 19 and 30, and compute the proportion of simulations where this decathlete breaks 9,200 points. 

For instance, to simulate the career of a decathlete with Asthon Eaton’s profile – that is, someone who is elite in the 100 m, long jump, and 400 m but slightly below average in the shot put and javelin toss – we would sample the 99.9 %-quantile for the 100 m intercept, the 94%-quantile for the LJ, and so on. We find that a decathlete, over the course of their entire career, with Eaton’s profile broke 9,200 points in just 6 % of our posterior samples while decathletes with Kevin Mayer’s and Roman Šebrle’s profiles 

respectively break 9,200 with posterior probabilities of 7 % and 10 %, assuming decathletes compete consistently for this period of time. We note that these simulations likely overestimate these probabilities, as they do not account for injury, mental fatigue, recovery time, or pressure. Additionally, our model and results are based on historical data, and do not account for unexpected breakthroughs that will systematically change human performance (e.g., new track surfaces, novel performance enhancement supplements, etc.). 

We repeat this procedure for the various synthetic decathlete profiles. We consider a decathlete that specializes in the Day 1 events, with 95th percentile intercepts in the first five events and 50th percentile intercepts in the last five events. This decathlete breaks 9,200 points in only 2 % of our simulations. The analogous Day 2 specialist never broke 9,200 in our simulations. 



**Figure 7:** Histogram of greatest decathlon performances for synthetic decathletes, excellent (green) and good (purple), across 4,000 simulated careers. The vertical line depicts the average highest score for each synthetic decathlete. 

P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 11** 

Perhaps unsurprisingly, an unrealistic “unicorn” decathlete, who is consistently 95th percentile across all ten events, does break the 9,200 mark in virtually all of our simulations. But the somewhat more realistic “good” decathlete, who consistently performs at the 80th percentile across all events, almost never breaks 9,200. Figure 7 shows histograms for the highest scores in each simulated career for these synthetic decathletes. There is minimal overlap for their max scores at their respective skill levels, with the “unicorn” decathlete’s average high score being 9,561 points and the “good” decathlete’s average high score at 8,671. So, returning to our original question, we conclude that breaking 9,200, while technically feasible, is highly unlikely and would be an extremely impressive feat. 

## **4 Discussion** 

In this paper, we developed a new compositional Bayesian model that can predict overall decathlon scores and individual discipline performance over the course of a decathlete’s career. We showed that our compositional model better captured inter-event dependencies than simpler alternatives. Using our model, we introduced a profile for each decathlete, which summarizes their latent skill in an easilyinterpretable way. Examining these profiles revealed that elite decathlon performance tend not to arise from elite performance across all ten disciplines. Rather, the top decathletes tend to be elite at only a few events (e.g., Ashton Eaton) or good but not elite in many (e.g., Kevin Mayer). Based on posterior predictive simulations of several synthetic decathlete profiles, we concluded that breaking the 9,200 point limit is possible, but unlikely. 

There are several potential extensions to our overall modeling. First, we were unable to account for important variables that affect decathlon performance like temperature, wind speeds, and shoe and surface technology. That said, it is conceptually straightforward to elaborate the model in Equation (3) to include additional covariates. More substantively, we fit each event-specific model separately, which renders the event-specific intercepts for a given decathlete independent _a posteriori_ . A better way to capture _latent_ inter-event dependence would be to fit a single model for all event performances in which the vector of decathlete-specific random intercepts was drawn from a normal population with non-diagonal covariance matrix. Additionally, as noted by Schuckers et al. (2023), our analysis may be subject to a certain amount of selection bias, as only the most successful decathletes are observed at the extremes of the age range considered. While this is certainly of concern, we believe that the selection bias is less severe 

in track and field than in professional sports like baseball or hockey. Finally, our compositional model only allowed for linear dependence between events. We leave development and investigation of a non-linear compositional model to future work. 

**Acknowledgments:** The authors thank Tristan Faure for his early contributions to the original conception of this project and for assistance with initial data collection during its preliminary phase. 

**Research ethics:** Not applicable. 

##### **Informed consent:** Not applicable. 

**Author contributions:** All authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Use of Large Language Models, AI and Machine Learning Tools:** None declared. 

**Conflict of interest:** The authors state no conflict of interest. **Research funding:** Support was also provided by the University of Wisconsin–Madison, Office of the Vice Chancellor for Research and Graduate Education with funding from the Wisconsin Alumni Research Foundation. 

**Data availability:** The data that support the findings of this study are openly available in [DecathlonCareerBest] at [https://github.com/Battles186/DecathlonCareerBest]. 

## **A Additional results** 

#### **A.1 Point calculation details** 

The formula for calculating points for each individual event is given below: 



where _a_ , _b_ , and _c_ are given by Table A3, and _y_ is the decathlete’s time, distance, or height. Faster times in track events (100 m, 400 m, hurdles, and 1,500 m) and greater distances and heights in field events produce higher scores. 

#### **A.2 Model comparisons with real data** 

We compared the out of sample accuracy on real decathlon data for each model under two frameworks. The first framework is a ‘general’ case, where we created ten 90–10 % training/testing splits, with observations placed in the test split at random. In ‘tail’ framework, we create ten training/testing splits by selecting 10 % of the decathletes and using their last decathlon observation as the test set, and 

> **12 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 

**Table A3:** Parameter values by event for point calculation. 

|**Event**|**a**|**b**|**c**|
|---|---|---|---|
|100 m|25.435|18.0|1.81|
|Long jump|0.144|220.0|1.40|
|Shot put|51.390|1.5|1.05|
|High jump|0.847|75.0|1.42|
|400 m|1.538|82.0|1.81|
|110 m hurdles|5.744|28.5|1.92|
|Discus throw|12.910|4.0|1.10|
|Pole vault|0.280|100.0|1.35|
|Javelin throw|10.140|7.0|1.08|
|1,500 m|0.038|480.0|1.85|



inter-event relationship over 200 simulated datasets, as described in Section 3. We specified a known structure of linear dependence between events and estimated coefficients for the age polynomials and preceding events using the original decathlon data. We then simulated 200 datasets with 8,668 observations. After fitting the cubic, compositional model to the 200 simulated datasets, we studied the posterior distributions over the _𝛽_ coefficients corresponding to age and preceding events. For each coefficient, we computed the proportion of 95 % posterior intervals containing the true value used in simulation. 

all other observations in the training dataset. Tables A4 and A5 contain the results (SMSE) from the real decathlon data bakeoff experiments with randomly removed observations and tail observations. 

### **A.3 Parameter recovery with known** **_𝜷_** 

Table A6 displays the proportion of 95 % credible intervals containing the true parameter associated with the 

#### **A.4 Empirical and posterior predictive correlations between decathlon events** 

Table A7 contains the empirical correlations between the decathlon events from the observed data. Tables A8 and A9 contain the 2.5 % and 97.5 % quantiles from the posterior predictive correlations from the simulated datasets generated by the simple and compositional models respectively, as described in Section 3. 

**Table A4:** Mean standardized MSE across 10 cross validations in predicting decathlon performance with randomly removed observations. 

|**Model**|**Basis**|**100 m**|**LJ**|**SP**|**HJ**|**400 m**|**110 mH**|**DT**|**PV**|**JT**|**1,500 m**|**Points**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Baseline|Cubic|–|–|–|–|–|–|–|–|–|–|0.234|
|Simple|Cubic|0.309|0.414|0.188|0.343|0.329|0.311|0.262|0.294|0.295|0.413|0.235|
|Compositional|Cubic|0.309|0.414|0.188|0.344|0.329|0.312|0.262|0.294|0.294|0.414|0.235|
|Baseline|Spline|–|–|–|–|–|–|–|–|–|–|0.235|
|Simple|Spline|0.309|0.414|0.188|0.344|0.329|0.311|0.263|0.294|0.295|0.414|0.235|
|Compositional|Spline|0.309|0.414|0.188|0.344|0.329|0.312|0.262|0.294|0.294|0.414|0.235|



**Table A5:** Mean standardized MSE across 10 cross validations tail-removed observations for decathletes. 

|**Model** **and** **prior**|**Basis**|**100** **m**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|**Points**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Baseline none|Cubic|–|–|–|–|–|–|–|–|–|–|0.358|
|Simple none|Cubic|0.337|0.471|0.238|0.414|0.406|0.447|0.301|0.372|0.315|0.482|0.362|
|Compositional none|Cubic|0.337|0.469|0.239|0.415|0.407|0.445|0.300|0.371|0.315|0.482|0.362|
|Baseline|Spline|–|–|–|–|–|–|–|–|–|–|0.359|
|Simple|Spline|0.338|0.470|0.238|0.415|0.409|0.448|0.301|0.371|0.317|0.484|0.363|
|Compositional|Spline|0.337|0.469|0.239|0.415|0.408|0.445|0.300|0.369|0.315|0.482|0.363|



P.-H. V. Nguyen et al.: Bayesian decathlon simulation **— 13** 

**Table A6:** Proportion of 95 % credible intervals containing the true parameter associated with corresponding predictor over 200 simulations. Entries are rounded to the second digit. 

|**Predictor**|**100** **m**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|
|---|---|---|---|---|---|---|---|---|---|---|
|Age|0.95|0.96|0.96|0.96|0.94|0.95|0.96|0.96|0.92|0.95|
|Age <sup>2</sup>|0.94|0.94|0.96|0.92|0.96|0.96|0.95|0.96|0.96|0.98|
|Age <sup>3</sup>|0.92|0.96|0.94|0.94|0.96|0.94|0.95|0.96|0.93|0.97|
|100 m|–|0.97|0.94|0.98|0.97|0.93|0.96|0.98|0.95|0.96|
|LJ|–|–|0.97|0.94|0.96|0.93|0.94|0.95|0.94|0.96|
|SP|–|–|–|0.98|0.96|0.94|0.98|0.96|0.96|0.94|
|HJ|–|–|–|–|0.97|0.94|0.96|0.96|0.96|0.98|
|400 m|–|–|–|–|–|0.93|0.95|0.96|0.96|0.96|
|110 mH|–|–|–|–|–|–|0.95|0.93|0.92|0.96|
|DT|–|–|–|–|–|–|–|0.96|0.95|0.96|
|PV|–|–|–|–|–|–|–|–|0.90|0.94|
|JT|–|–|–|–|–|–|–|–|–|0.94|



**Table A7:** Empirical correlations between decathlon events in observed data, rounded to 2 digits. 

|**Event**|**100** **m**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|
|---|---|---|---|---|---|---|---|---|---|---|
|100 m|1.00|−0.54|−0.20|−0.20|0.66|0.52|−0.18|−0.25|−0.13|0.10|
|LJ|–|1.00|0.33|0.43|−0.45|−0.47|0.29|0.34|0.24|−0.14|
|SP|–|–|1.00|0.31|−0.15|−0.36|0.73|0.38|0.51|−0.01|
|HJ|–|–|–|1.00|−0.21|−0.34|0.28|0.29|0.22|−0.10|
|400 m|–|–|–|–|1.00|0.46|−0.13|−0.25|−0.11|0.46|
|110 mH|–|–|–|–|–|1.00|−0.32|−0.37|−0.24|0.12|
|DT|–|–|–|–|–|–|1.00|0.40|0.48|−0.02|
|PV|–|–|–|–|–|–|–|1.00|0.31|−0.20|
|JT|–|–|–|–|–|–|–|–|1.00|−0.09|
|1,500 m|–|–|–|–|–|–|–|–|–|1.00|



**Table A8:** 2.5 % and 97.5 % quantiles for posterior predictive correlation between decathlon events from 2,000 simulated datasets from the simple model, rounded to 2 digits. 

|**Event**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|
|---|---|---|---|---|---|---|---|---|---|
|100 m|−0.41,−0.37|−0.16, −0.13|−0.16, −0.12|0.49, 0.52|0.37, 0.41|−0.15, −0.12|−0.19, −0.16|−0.11, −0.07|0.03, 0.07|
|LJ|1, 1|0.24, 0.28|0.29, 0.33|−0.35,−0.31|−0.37,−0.33|0.23, 0.26|0.24, 0.28|0.16, 0.2|−0.1, −0.06|
|SP|–|1, 1|0.25, 0.28|−0.12,−0.08|−0.33,−0.29|0.64, 0.67|0.32, 0.35|0.44, 0.47|−0.01, 0.03|
|HJ|–|–|1, 1|−0.17,−0.13|−0.29, −0.25|0.23, 0.26|0.22, 0.26|0.17, 0.2|−0.07, −0.03|
|400 m|–|–|–|1, 1|0.31, 0.35|−0.11,−0.07|−0.2,−0.16|−0.09, −0.05|0.28, 0.32|
|110 mH|–|–|–|–|1, 1|−0.29,−0.25|−0.31,−0.27|−0.21, −0.18|0.03, 0.07|
|DT|–|–|–|–|–|1, 1|0.32, 0.36|0.41, 0.44|−0.02, 0.02|
|PV|–|–|–|–|–|–|1, 1|0.24, 0.28|−0.16, −0.12|
|JT|–|–|–|–|–|–|–|1, 1|−0.06, −0.02|
|1,500 m|–|–|–|–|–|–|–|–|1, 1|



> **14 —** P.-H. V. Nguyen et al.: Bayesian decathlon simulation 

**Table A9:** 2.5 % and 97.5 % quantiles for posterior predictive correlation between decathlon events from 2,000 simulated datasets from the compositional model, rounded to 2 digits. 

|**Event**|**LJ**|**SP**|**HJ**|**400** **m**|**110** **mH**|**DT**|**PV**|**JT**|**1,500** **m**|
|---|---|---|---|---|---|---|---|---|---|
|100 m|−0.55, −0.52|−0.22, −0.18|−0.22, −0.18|0.64, 0.67|0.5, 0.54|−0.19, −0.16|−0.27, −0.23|−0.15, −0.11|0.09, 0.13|
|LJ|1, 1|0.3, 0.34|0.39, 0.43|−0.47, −0.43|−0.48, −0.45|0.26, 0.3|0.31, 0.35|0.21, 0.25|−0.17, −0.12|
|SP|–|1, 1|0.29, 0.32|−0.17, −0.13|−0.37, −0.34|0.71, 0.73|0.36, 0.39|0.49, 0.52|−0.03, 0.01|
|HJ|–|–|1, 1|−0.23, −0.19|−0.35, −0.31|0.25, 0.29|0.26, 0.3|0.2, 0.24|−0.13, −0.08|
|400 m|–|–|–|1, 1|0.44, 0.48|−0.15, −0.11|−0.27, −0.24|−0.14, −0.1|0.43, 0.47|
|110 mH|–|–|–|–|1, 1|−0.33, −0.3|−0.38, −0.35|−0.26, −0.22|0.1, 0.15|
|DT|–|–|–|–|–|1, 1|0.37, 0.41|0.46, 0.49|−0.04, 0|
|PV|–|–|–|–|–|–|1, 1|0.28, 0.32|−0.22, −0.17|
|JT|–|–|–|–|–|–|–|1, 1|−0.12, −0.08|
|1,500 m|–|–|–|–|–|–|–|–|1, 1|



## **References** 

Aoki, K., Kohmura, Y., Sakuma, K., Koshikawa, K., and Naito, H. (2015). Relationships between field tests of power and athletic performance in track and field athletes specializing in power events. _Int. J. Sports Sci. Coach._ 10: 133−144,. 

Baker, R.D. and McHale, I.G. (2023). A flexible mixed model for age-dependent performance: application to golf. _J. Roy. Stat. Soc. C: Appl. Stat._ 72: 1260−1275,. 

Battles, P., Noble, T.J., and Chapman, R.F. (2025). Predicting high-performance decathlon career best. _Exp. Physiol._ 110: 1672−1681,. 

- Beaulieu, P., Ottoz, H., Grange, C., Thomas, J., and Bensch, C. (1995). Blood lactate levels of decathletes during competition. _Br. J. Sports Med._ 29: 80−84,. 

Brander, J.A., Egan, E.J., and Yeung, L. (2014). Estimating the effects of age on NHL player performance. _J. Quant. Anal. Sports_ 10: 241−259,. Cox, T.F. and Dunn, R.T. (2002). An analysis of decathlon data. _J. R. Stat. Soc. Ser. D: Statistician_ 51: 179−187. 

Dziadek, B., Iskra, J., Mendyka, W., and Przednowek, K. (2022). Principal component analysis in the study of the structure of decathlon at different stages of sports career. _Polish J. Sport Tourism_ 29: 21−28,. Edouard, P., Pruvost, J., Edouard, J.-L., and Morin, J.-B. (2010). Causes of 

dropouts in decathlon. A pilot study. _Phys. Ther. Sport_ 11: 133−135,. Fair, R.C. (2008). Estimated age effects in baseball. _J. Quant. Anal. Sports_ 4, https://doi.org/10.2202/1559-0410.1074. 

Griffin, J.E., Hinoveanu, L.C., and Hopker, J.G. (2022). Bayesian modelling of elite sporting performance with large databases. _J. Quant. Anal. Sports_ 18: 253−268,. 

- Kenny, I.C., Sprevak, D., Sharp, C., and Boreham, C. (2005). Determinants of success in the Olympic decathlon: some statistical evidence. _J. Quant. Anal. Sports_ 1, https://doi.org/10.2202/1559-0410.1002. 

- Park, J. and Zatsiorsky, V.M. (2011). Multivariate statistical analysis of decathlon performance results in olympic athletes (1988−2008). _World Acad. Sci., Eng. Technol._ 5: 985−988. 

- Schomaker, M. and Heumann, C. (2011). Model averaging in factor 

   - analysis: an analysis of Olympic decathlon data. _J. Quant. Anal. Sports_ 7: 1−15,. 

- Schuckers, M., Lopez, M., and Macdonald, B. (2023). Estimation of player aging curves using regression and imputation. _Ann. Oper. Res._ 325: 681−699,. 

- Stan Development Team (2025). RStan: the R interface to Stan. R package version 2.32.7. 

- Stemmler, M. and Baumler, G. (2005). The detection of types among decathletes using configural frequency analysis (CFA). _Psychol. Sci._ 47: 447. 

- Van Damme, R., Wilson, R.S., Vanhooydonck, B., and Aerts, P. (2002). Performance constraints in decathletes. _Nature_ 415: 755−756,. 

- Villaroel, C., Mora, R., and Gonzalez-Parra, G.C. (2011). Elite triathlete performance related to age. _J. Human Sport Exerc._ 6: 363−373,. 

- Walker, J.A. and Caddigan, S.P. (2015). Performance trade-offs and individual quality in decathletes. _J. Exp. Biol._ 218: 3647−3657,. 

- Wimmer, V., Fenske, N., Pyrka, P., and Fahrmeir, L. (2011). Exploring competition performance in decathlon using semi-parametric latent factor models. _J. Quant. Anal. Sports_ 7 (4): 1−19. 

- Woolf, A., Ansley, L., and Bidgood, P. (2007). Grouping of decathlon disciplines. _J. Quant. Anal. Sports_ 3. 


