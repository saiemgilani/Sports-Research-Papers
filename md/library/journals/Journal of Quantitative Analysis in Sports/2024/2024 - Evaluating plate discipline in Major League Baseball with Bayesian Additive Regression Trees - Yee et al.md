<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2024/2024 - Evaluating plate discipline in Major League Baseball with Bayesian Additive Regression Trees - Yee et al.pdf -->

J. Quant. Anal. Sports 2024; 20(1): 5–20 

### **Research Article** 

Ryan Yee and Sameer K. Deshpande* 

# **Evaluating plate discipline in Major League Baseball with Bayesian Additive Regression Trees** 

https://doi.org/10.1515/jqas-2023-0048 Received May 9, 2023; accepted August 23, 2023; published online September 20, 2023 

**Abstract:** We introduce a three-step framework to determine at which pitches Major League batters should swing. Unlike traditional plate discipline metrics, which implicitly assume that all batters should always swing at (resp. take) pitches inside (resp. outside) the strike zone, our approach explicitly accounts not only for the players and umpires involved in the pitch but also in-game contextual information like the number of outs, the count, baserunners, and score. We first fit flexible Bayesian nonparametric models to estimate (i) the probability that the pitch is called a strike if the batter takes the pitch; (ii) the probability that the batter makes contact if he swings; and (iii) the number of runs the batting team is expected to score following each pitch outcome (e.g. swing and miss, take a called strike, etc.). We then combine these intermediate estimates to determine whether swinging increases the batting team’s run expectancy. Our approach enables natural uncertainty propagation so that we can not only determine the optimal swing/take decision but also quantify our confidence in that decision. We illustrate our framework using a case study of pitches faced by Mike Trout in 2019. 

**Keywords:** decision theory; uncertainty quantification; Bayesian nonparametrics 

## **1 Introduction** 

### **1.1 Motivating example** 

At the top of the seventh inning of the September 5, 2019 game between the Oakland Athletics and the Los Angeles Angels, Angels batter Kevan Smith faced Athletics pitcher 

***Corresponding author: Sameer K. Deshpande** , Department of Statistics, University of Wisconsin–Madison, Madison, USA, E-mail: sameer .deshpande@wisc.edu. https://orcid.org/0000-0003-4116-5533 **Ryan Yee** , Department of Statistics, University of Wisconsin–Madison, Madison, USA, E-mail: ryan.yee@wisc.edu 

A.J. Puk with the Angels leading 5 runs to 1. On an 0–2 pitch with no outs and no runners on-base, Puk threw a fastball that just missed the lower right-hand corner of the strike zone (see Figure 1). Smith decided to swing at the pitch. Did Smith make the correct decision? 

By swinging, Smith risked missing the pitch, picking up a strike, and losing an out, thereby putting his team at a disadvantage. And even if he had made contact, he risked flying or grounding out, which would also disadvantage his team. At the same time, however, by swinging, Smith had a chance of getting on base or even scoring a home run. On the other hand, had Smith not swung and had instead taken the pitch, the umpire may have correctly called the pitch a ball (which would advantage Smith’s team) or mistakenly called a strike (which would disadvantage Smith’s team). 

As it turns out, Smith hit a home run on this pitch. So at least retrospectively, it would seem like the decision to swing was good. But was Smith simply lucky? Or should we expect him to hit home runs consistently off of similar pitches in similar game situations? And how sure should we be about these expectations? 

We provide quantitative answers to these questions using a Bayesian modeling framework to assess a batter’s decision making — or plate discipline — _before_ observing the outcome of each pitch. In the case of Smith, we find that there was a 12.3 % chance (90 % credible interval [5.8 %, 16.7 %]) that the umpire would call the pitch a strike. Although taking the pitch would likely have benefitted Smith’s team, Smith had about an equal chance of making contact if he swung (83.1 %, 90 % credible interval [80.6 % _,_ 85.3 %]). In fact, we find that by swinging on similar pitches, Smith increases the number of runs the Angels are expected to score in the remainder of the half-inning only 61.4 % of the time and only by about 0.01 runs on average (90 % credible interval [−0.04 _,_ 0.08]). Ultimately, our analysis concludes that while Smith’s decision to swing on the pitch was not especially risky, it was unlikely to substantially benefit his team, in terms of the number of expected runs the team would score in the rest of the inning. 

Traditional plate discipline metrics compare the proportion of pitches batters swing at that are outside and inside the strike zone (Slowinski 2010). In this way, these 

> **6 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 



**Figure 1:** Kevan Smith swings at a fastball thrown just outside the lower right-hand corner of the strike zone. 

metrics reward batters for avoiding taken strikes based on the implicit assumption that pitches thrown outside (resp. inside) the strike zone are always called balls (resp. strikes). Of course, umpires do not adhere strictly to the official strike zone when making ball/strike decisions. Though they often rely on adaptive heuristics and prior experience to make calls (Green and Daniels 2022), umpires can also be influenced by the framing ability of individual catchers (Deshpande and Wyner 2017; Lindbergh 2013; Marchi 2011); player age or ability (Kim and King 2014; Mills 2014); their previous calls (Chen, Moskowitz, and Shue 2016); and the fact that their calls are reviewed by the league (Mills 2017). As a result, traditional plate discipline metrics may systematically penalize batters who swing at “frameable” pitches that just barely miss the strike zone but are likely to be called strikes. These metrics additionally fail to account for the fact that some pitches are easier to hit than others. At least intuitively, we might regard a batter who only takes hard-to-hit pitches as more disciplined than a batter who consistently takes easy-to-hit pitches. Further, traditional plate discipline metrics entirely ignore the many contextual and situational factors that can influence a batter’s decision to swing. For instance, batters may be more aggressive on pitches thrown with two strikes to avoid striking out while looking. Finally, existing plate discipline metrics do not quantify the uncertainty in their findings. 

### **1.2 Our contributions** 

We introduce a three-step approach to determine optimal swing decisions, assess batter decision-making on a perpitch basis, and quantify our uncertainty about both. In the first step, we fit flexible Bayesian nonparametric models that enable us to estimate, for any single pitch, (i) the 

probability that a batter makes contact; (ii) the probability that the umpire calls a strike; and (iii) the average number of runs that the batting team is expected to score in the remaining half-inning as functions of the pitch location, players and umpires involved, and game-state information like the count, inning, and baserunners. Then, in the second step, we combine these estimates using the law of total expectation to compute the expected number of runs the batting team is expected to score if the batter swings or takes the pitch. Finally, we use these quantities to determine the optimal swing/take decision. By fitting Bayesian models in the first step, we can propagate uncertainty about the actual outcomes of a particular pitch through to our assessment of the batter’s decision making in an intuitive and computationally efficient manner. 

Our framework involves fitting three component models, each of which may be of independent interest. First, elaborating on work begun in Deshpande and Wyner (2017), we develop a Bayesian model of called strike probability that “borrows statistical strength” across umpires and players through flexible partial pooling of data. We demonstrate that this model, which is based on Bayesian additive regression trees [BART; (Chipman, George, and McCulloch 2010)] and accounts not only for pitch location but also player and umpire identities and game-state information, outperforms parametric and nonparametric competitors that only account for location. We develop a similar model for the probability that a batter makes contact on a pitch. Finally, we developed a BART-based run expectancy model, which we call BARTxR, to predict the number of runs a team is expected to score following each pitch outcome as a function of in-game contextual variables like the count, number of outs, score differential, and baserunners. At a high-level BARTxR generalizes existing run expectancy measures like 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 7** 

RE24 (Tango, Lichtman, and Dolphin 2007), which computes the average number of runs scored within bins defined by the number of outs and configuration of baserunners. Using a comprehensive cross-validation study, we demonstrate that BARTxR’s predictions are more accurate than those of RE24 and several variants thereof. 

The remainder of this paper is organized as follows. We introduce the data and notation used in Section 2.1 before describing our three-step framework for assessing batter decision-making in Section 2.2. Then, we detail our modeling approach in Section 3. In Section 4.2, we perform a case study of a single batter, Mike Trout, highlighting the types of plate discipline assessments that can be done using our framework. We conclude in Section 5 with a discussion of several extensions of our modeling framework. 

## **2 Data and background** 

### **2.1 Data and notation** 

Our analysis uses pitch-by-pitch tracking data from Major League Baseball’s Statcast database. For each pitch, we observe game-state information (e.g. count, outs, score, baserunners), pitch personnel (e.g. pitcher, batter, fielders, umpire), pitch outcome (e.g. hit, ball, strike), and other game actions (e.g. steal, substitution). Additionally, we observe the horizontal and vertical coordinates of each pitch’s trajectory as it crosses the front edge of home plate. We scraped these data using the **baseballr** package [version 1.2.0; (Petti and Gilani 2022)]. We limited our analysis to pitches thrown during regular season games. We fit our strike probability model using all 380,654 pitches that were taken during the 2019 season and we fit our contact probability model using all 341,725 pitches at which batters swung in the 2019 season. We fit our expected runs model (BARTxR) using all 2,853,912 pitches thrown between 2015 and 2018, inclusive. Observe that these three datasets are disjoint. 

We use  to denote information about the state of the game when the pitch was thrown including the count, outs, baserunners, score differential, inning, and whether it is the top or bottom of the inning. We similarly use  to record the personnel involved in a pitch including the identities of the batter, catcher, pitcher, and home plate umpire. We additionally include indicators of the batter and pitcher handedness in  as well as quantitive measures of the batter and pitcher quality, which we describe below. Finally, we denote the location of the pitch (i.e. the plate_x and plate_z coordinates in Statcast) as its crosses the front edge of home plate with . 

> Let swing = 1 if the batter swings and swing = 0 if the batter takes the pitch. If the batter decides to swing, 

> let contact = 1 if the batter makes contact with the pitch and contact = 0 if the batter misses. If the batter does not swing, let strike = 1 if the umpire calls a strike and strike = 0 if the umpire calls a ball. Let outcome = (contact, strike) be a vector denoting the outcome of the pitch where contact = NA if swing = 0 and strike = NA if swing = 1. Let gstate denote the game-state category the game moves to after the outcome of the pitch is observed. gstate encodes similar information as outcome but treats a called strike and a miss as the same game-state. 

We quantify batter and pitcher quality using a running estimate of their weighted on-base average [wOBA; (Tango, Lichtman, and Dolphin 2007)]. For each game, we set these quality measures to be their mean wOBA, averaged over all of their previous games in the season. For batters, higher wOBA represents higher quality while for pitchers, lower wOBA represents higher quality. Note that for the first game, we set each player’s quality measure to be the league average wOBA from the previous season. Our choice to track player quality using a running wOBA estimates follows the example of Brill, Deshpande, and Wyner (2022). 

### **2.2 Determining the optimal decision** 

To motivate our three-step framework, consider a pitch at the moment just before the batter decides to swing. Suppose that we knew the number of runs the batter’s team would score in the remainder of the half-inning if (a) the batter swings or (b) the batter does not swing. Based on that knowledge, the optimal decision is intuitively the one that leads to scoring more runs. Of course, we are uncertain about these run values at the moment just before the batter swings or takes the pitch. This is because there is uncertainty in the ultimate outcome: if he swings, the batter might make contact or miss and if he takes the pitch, the umpire may call it a ball or a strike. Because of this uncertainty, we determine the optimal swinging decision using the _expected_ number of runs the batter’s team will subsequently score. That is, we will average over our uncertainty about these outcomes. 

Figure 2 illustrates the four possible outcomes following the batter’s decision. Computing the expected number of runs scored after a swing requires knowledge of (i) the probability the batter will make contact; (ii) the expected number of runs the batting team will score in the current half-inning after making contact; and (iii) the expected number of runs the batting team will score in the current half-inning after swinging but missing. Similarly, computing the expected number of runs scored after a take requires knowledge of (i) the probability the umpire will call a strike; (ii) the expected number of runs the batting team will score in the current half-inning after a called strike; and (iii) the 

> **8 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 



**Figure 2:** Framework for modeling the outcomes of a pitch. 

expected number of runs the batting team will score in the current half-inning after a called ball. 

Formally, let _R_ be the number of runs the batting team scores following the pitch. Given the game-state information , personnel , and location  of a pitch, we need to compute 𝔼[ _R_ | _,_  _,_  _,_ swing] for both values of swing in order to determine the optimal decision for that pitch. Observe that we can decompose the expected runs following a swing or take as 



To determine the optimal decision, we introduce EVdiff as the difference in expected runs following a swing and following a take. Formally, we define 



The sign of EVdiff determines the optimal decision xR_optimal, which is given by 



Determining the optimal decision for a pitch and subsequently assessing a batter’s decision-making requires knowledge of 𝔼[ _R_ | _,_  _,_  _,_ swing _,_ outcome] and ℙ(outcome| _,_  _,_  _,_ swing). Although we do not know these quantities exactly, we can estimate them using our collected data. We will discuss each estimation problem in Section 3. 

### **2.3 Related work and background on BART** 

**Existing plate discipline metrics** . Traditional plate discipline metrics [e.g., (Slowinski 2010)] characterize how often batters swing at pitches thrown outside (O-Swing%) and inside (Z-Swing%) the strike zone as well as how often batters made contact with these pitches (O-Contact% and Z-Contact%, respectively). Intuitively, disciplined batters have high Z-Swing% and low O-Swing%. Unfortunately, such metrics implicitly assume that all pitches thrown inside (resp. outside) the strike zone are equally desirable to hit (resp. not hit) which can give a false impression of a batter’s plate discipline. For example, Kevan Smith’s decision in Figure 1 would negatively affect his O-Swing% even though he had a high probability of making contact. By treating every pitch equally, traditional metrics fail to account for important contextual factors that impact a batter’s decision to swing such as strike probability [see, e.g., (Arthur 2014b; Green and Daniels 2014; Mills 2014)]. As a result, they may systematically over-penalize batters who see many pitches near the edges of the strike zone. 

To overcome these limitations, recent studies have focused on directly modeling the batter’s actual decisionmaking process. For instance, Arthur (2014a) first estimates the probability that each pitch is called a strike and then uses those estimates to predict whether a batter will swing at a pitch. The authors characterize disciplined batters as those whose swing probabilities increase most in response to small increases in strike probability. Unfortunately, this characterization does not consider the downstream impact swing decisions have on metrics like run expectancy or win probability. Towards this end, Vock and 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 9** 

Vock (2018) used a causal inference framework to predict how a batter’s batting average, on-base percentage, and slugging percentage would change under different counterfactual decision-making strategies. At a high-level, their framework answers the question “What would happen if batter A made swing/take decisions like batter B?” While interesting and informative, the models in Arthur (2014a) and Vock and Vock (2018) make no attempt to determine the decision a batter _ought_ to make. In the context of Figure 2, these models try to predict which path a batter will follow. Our approach, in contrast, attempts to determine which path would most benefit the batter’s team. 

Independently of but concurrently to this work, Mould and Anderson (2022a, 2022b) introduced the Expected Additional runs Gained by Looking/swinging Estimate (EAGLE) model to quantify plate discipline. Like us, they also used a tree-structured framework to determine the optimal swing/take decision and fit intermediate strike probability and contact probability models using flexible, nonparametric procedures. Superficially, our approach differs from theirs in terms of the predictor variables included in these intermediate probability models as well as the specific model fitting procedure used (BART in our case versus gradient-boosted trees in theirs). Like us, EAGLE combines predictions from intermediate probability models with a run expectancy model to compute the expected number of runs a team will score following a swing or take. EAGLE uses a variant of RE24 that accounts for baserunners, count, and outs<sup>1</sup> followed by an _ad hoc_ correction for batter quality. Our approach, on the other hand, uses predictions from a much higher-resolution regression-based run expectancy model. 

The most substantive difference between our proposal and EAGLE’s lies in uncertainty quantification. Simply put, EAGLE makes no attempt to propagate uncertainties about the intermediately-estimated strike probability, contact probability, and run expectancies to their evaluation of batter decision making. In sharp contrast, our Bayesian approach makes such uncertainty propagation easy (see Section 3.1). We argue that such uncertainty quantification is of paramount importance for evaluating decision-making. Basically, we do not wish to penalize batters for making suboptimal decisions when there is considerable uncertainty about what the optimal decision even is! 

**BART** . Initially introduced in the context of nonparametric regression, BART has emerged as a popular “off-theshelf” modeling tool because it often delivers accurate predictions with reasonably well-calibrated uncertainty estimates without requiring users to (a) pre-specify the parametric form of the regression function and (b) tune any hyperparameters. At a high-level, BART works by approximating unknown functions with sums of binary regression trees and excels at capturing complicated nonlinearities and complex, high-order interaction effects. We believe _a priori_ that both strike and contact probabilities are highly non-linear and may depend on complicated interactions between players, umpires, pitch location, and in-game contextual variables like the count or baserunner configuration. Insofar as such nonlinearities and interactions are difficult to specify correctly in a parametric fashion, BART is an especially attractive modeling choice as it does not require us to pre-specify such a parametric form. We fit our three BART models using the **flexBART** package, which permits more flexible modeling with categorical predictors such as batter identity that can take on many values. See Despande (2023) for more details. 

## **3 Modeling and uncertainty propagation** 

### **3.1 Uncertainty propagation** 

Recall that computing EVdiff requires first estimating each term in the summand in Equation (1). By taking a Bayesian approach, we can quantify how uncertainties about these estimates propagate to uncertainty about EVdiff and xR_optimal in a relatively straightforward fashion. Specifically, because they involve non-overlapping subsets of pitches, we can fit independent Bayesian models to obtain posterior samples of 𝔼[ _R_ | _,_  _,_  _,_ swing _,_ outcome] and ℙ(outcome| _,_  _,_  _,_ swing) for each outcome. By suitably multiplying and summing these samples according to Equation (1), we obtain posterior samples of 𝔼[ _R_ | _,_  _,_  _,_ swing], from which we can immediately compute posterior samples of EVdiff and xR_optimal. Given posterior samples of EVdiff, we use the proportion of samples with positive EVdiff as an estimated probability that swinging is the optimal decision. We further quantify how much better (or worse) swinging at the pitch is than taking the pitch using the posterior mean and 90 % credible interval (formed using the 5 % and 95 % sample quantiles) of EVdiff. 

**1** We include this model in our cross-validation study in Section 4.1 as RE288. 

> **10 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 

### **3.2 Modeling assumptions and fitting** 

**Expected Runs.** We need to compute run expectancy following the four pitch outcomes shown in Figure 2. That is, we need to compute 𝔼[ _R_ | _,_  _,_  _,_ swing _,_ outcome]. A natural approach begins by first partitioning our dataset of 2,853,912 pitches into bins, one for every combination of variables in , , , swing, and outcome, and then computing the average number of runs scored subsequently in each bin. Despite its intuitive appeal, such a binning and averaging procedure is impractical without further simplifying assumptions due to the vast number of combinations. To wit, in 2019 there were a total of 988 batters, 93 umpires, and 113 catchers. Accounting for all combinations of just these three aspects of  requires over 10 million bins, far exceeding the number of pitches in our dataset. 

To simplify this estimation, we assume that given the game context, swing decision, and outcome, personnel and pitch location have no predictive effect on expected runs. Formally, we assume that 𝔼[ _R_ | _,_  _,_  _,_ swing _,_ outcome] = 𝔼[ _R_ | _,_ swing _,_ outcome]. While this may seem like a rather strong assumption, we note that it is actually _weaker_ than the assumptions underpinning other popular run expectancy models. For example, RE24 assumes that, given the number of outs and the configuration of baserunners, _R_ is conditionally independent of all other contextual factors, personnel, and pitch location. That is, RE24 assumes that 𝔼[ _R_ | _,_  _,_  _,_ swing _,_ outcome] = 𝔼[ _R_ |outs _,_ baserunners]. 

Under our assumption, we must now compute 𝔼[ _R_ | _,_ swing _,_ outcome]. We fit a single BART model to estimate the expected runs following a strike, ball, contact, and miss. Fitting a single model allows us to “borrow strength” from related observations with different outcomes. Such partial pooling may be preferable to separately modeling each outcome since different outcomes can lead to the same game-state (e.g. swinging strike vs. called strike). We fit our run expectancy model BARTxR using combined pitch data from the 2015 to 2018 MLB seasons, inclusive. 

**Event Probabilities.** We fit BART models with probit links to estimate the strike probability and contact probabilities as functions of , , and . We fit these models to data from the 2019 MLB season. 

## **4 Results** 

Code to download and pre-process our data, fit the constituent models, and compute the posterior distributions of EVdiff and xR_optimal is available at https://github.com/ ryanyee3/plate_discipline_code. All our experiments and 

analyses were run on a high throughput computing cluster [for details, see (Center for High Throughput Computing 2006)]. 

### **4.1 Model validation** 

We performed several cross-validation studies to understand the predictive accuracy of our BART models for strike probability, contact probability, and run expectancy. 

**Strike and contact probabilities.** We compared the out-of-sample performance of our BART models fit with , , and  as predictors for strike and contact probabilities to several competitors including (i) BART models fit with every combination of , , and ; a generalized additive model (GAMs) fit with ; and the empirical probabilities of each event using 10-fold cross-validation. We used the **mgcv** package [version 1.8–41; Wood 2017] to fit GAMs with logit links to predict strike and contact probabilities as a smooth function of location. We evaluated each model in terms of mean squared error (i.e. the Brier score). Figure 3 shows the performance of each model relative to BART(, , ) (i.e. the BART model fit with , , and  as predictors). 

Unsurprisingly, models using  as a predictor substantially outperformed models that did not adjust for pitch location. Interestingly, we found that BART(, ) performed better than BART(, ), but BART() outperformed BART(). The fact that these models achieved similar predictive performance, despite using fewer predictors than the full BART model, suggests that location is, by far, the main driver of strike and contact probabilities. Figures illustrating the relative performance of all other models tested can be found in Appendix A.1. 

**Expected runs.** We conducted a comprehensive comparison of BARTxR to 14 variants of RE24. We considered every combination of count (12 possibilities), outs (3 possibilities), and baserunners (8 possibilities) as predictors in candidate models for a total of seven unique sets of predictors. For each set of predictors we fit two types of models: REx and BayesREx where x denotes the number of predictors. REx models are fit in the same way as RE24. BayesREx models are hierarchical Bayesian models of the following form 



> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 11** 



**Figure 3:** Out-of-sample mean-squared error relative to a BART model fit with , , and  for strike (a) and contact (b) probabilities. 

where _i_ indexes the pitch, _g_ ( _i_ ) indexes the bin (i.e., combination of count, out, and/or baserunners), half − _t_ 7 denotes a _t_ -distribution with 7 degrees of freedom truncated to the positive axis, and _R_ is _R_ standardized to have mean zero and variance one. We set _𝜈_ and _𝜆_ so that the prior probability on the event _𝜎<_ 1 is about 90 %. Our decision to specify the model in Equation (3) on the standardized scale and our choices of _𝜈_ and _𝜆_ mirror the choices made in default implementations of BART. We completed our prior specification with the weakly informative choice _𝜏_<sup>2</sup> _𝛽_<sup>= 100.</sup> Compared to REx, which estimates run expectancy in each bin independently, BayesREx“borrows strength” across bins. 

Figure 4 shows the mean-squared error results of each candidate model relative to BARTxR in 10-fold crossvalidation. We find REx and BayesREx models perform similarly for each combination of predictors. This is perhaps unsurprising given the large number of pitches; basically, the conditional posterior distribution of each _𝛽 g_ ( _i_ ) given _𝛽, 𝜎_<sup>2</sup> , and _𝜏 𝛽_ is sharply concentrated around the average values of the _Ri_ ’s in the bin. We find that the models which account for outs and baserunners perform best. On average, BARTxR was more accurate than RE24 by 0.009 runs per pitch and RE288 by 0.007 runs per pitch, which respectively correspond to improvements of 1.8 % and 1.4 % in mean square error. 

### **4.2 Batter evaluation case study** 

We now illustrate the type of plate discipline analysis facilitated by our modeling efforts with a case study about Mike Trout in the 2019 MLB season. For each pitch Trout faced in 2019, we generated samples of EVdiff and determined the xR_optimal decision based on the posterior mean of EVdiff. We quantified our uncertainty by computing the xR_optimal decision for each individual sample; that is, we computed the proportion of samples in which the xR_optimal decision is to swing. Figure 5 shows the results of these calculations for every pitch faced by Trout in the 2019 regular season broken down by the actual decision and the xR_optimal decision. In Figure 5a, the darker the shading, the greater the difference in the posterior means of expected runs from swinging and the expected runs from taking. In Figure 5b, the darker the shading, the more posterior certainty we have in the xR_optimal decision. 

In Figure 5a and b, the large number of pitches in panels (a) and (d) reveal that Trout’s actual decision very often matched our model’s xR_optimal decision. Moreover, these decisions tended to agree with the conventional wisdom that batters should swing at pitches inside the strike zone and take pitches outside the strike zone. In panels (a) and (d) of the figures, we find, for instance, that Trout tended not to swing at pitches thrown outside the strike zone and rarely took pitches inside the zone. The dark shading of pitches outside the strike zone in panel (a) illustrate our model’s 

> **12 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 



**Figure 4:** Out-of-sample mean-squared error relative to BARTxR for seven REx models and seven BayesREx models. 



**Figure 5:** Pitches faced by Mike Trout in the 2019 MLB season where he took (left) and swung (right) and the xR_optimal decision is to take (top) and swing (bottom). Pitches in (a) are shaded based on EVdiff and pitches in (b) are shaded based on ℙ(xR_optimal = swing). The darker the shading, the larger the EVdiff (a) and our certainty that the xR_optimal decision is to swing (b). All plots are from the perspective of the home plate umpire. 

high degree of certainty that the xR_optimal decision is to take the pitch. Similarly, the dark shading of pitches inside the strike zone in panel (d) illustrate our model’s certainty that the xR_optimal decision is to swing. 

Perhaps more interesting are those pitches where our model’s xR_optimal decision deviated from the conventional wisdom and Trout’s actual decision-making (panels (b) and (c) in Figure 5a and b). In panel (b), for instance, 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 13** 

we see that Trout swung at many pitches inside the strike zone for which our model determined the xR_optimal decision was to take. As suggested by the relatively light shading of these pitches, we found on further inspection that our model was very uncertain about the xR_optimal decision. In fact, the posterior distributions of EVdiff for these pitches tended to be nearly symmetric and tightly concentrated around zero. Because of the uncertainty in the xR_optimal decision and relatively small magnitude of EVdiff for these pitches, we would not classify Trout’s decision to swing at these pitches as bad decisions per se. 

In panel (c), however, we find that Trout took several pitches that passed inside the strike zone for which our model determined, with relatively high certainty (as evidenced by the dark shading), that the xR_optimal decision was to swing. For these pitches, the posterior distributions of EVdiff were largely concentrated on positive values. 

By taking these pitches, our model suggests that Trout cost his team in terms of expected runs. Similarly, in panel (b), we find that Trout swung at many low and away pitches that passed outside the strike zone for which our model determined the xR_optimal decision was to take with relatively high certainty. By swinging at these pitches, our model suggests that Trout cost his team in terms of expected runs. 

Of additional interest are the low-and-away pitches in panel (c) of Figure 5b where our model is very confident that the xR_optimal decision is to swing. We found that the posterior mean EVdiff for these pitches is close to zero, suggesting that the cost of making a sub-optimal decision on these pitches is very small. Nevertheless, it is interesting that our model is so confident that the xR_optimal decision is to swing on these pitches thrown well outside the strike zone, when it is similarly confident that the xR_optimal decision is to take pitches thrown in similar locations in panels (a) 



**Figure 6:** Pitches faced by Mike Trout in the 2019 MLB season where his swing decision conflicts with the xR_optimal decision. Pitches are shaded based on the proportion of samples where the expected runs from swinging is greater than the expected runs from taking. 

> **14 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 

and (b) of Figure 5b. We speculate that the difference is due, at least in part, to differences in the game contexts in which these pitches were thrown. 

To probe this possibility, we visualized all pitches faced by Trout broken down by the number of outs and the number of baserunners in Figure 6. Pitches are colored in Figure 6 based on the posterior probability that the xR_optimal decision is to swing. We see that the low-andaway pitches where the xR_optimal decision is to swing (pitches of interest) occur when there are two outs and few baserunners while the low-and-away pitches where the xR_optimal decision is to take occur when there are no outs. Such a finding is, we argue, intuitive, because the expected runs from a positive outcome will be similar to the expected runs from a negative outcome when there are two outs and few baserunners. 

Finally, although we have focused on Trout in this paper, we can conduct such analyses for any batter using our model results. We have created an interactive Shiny app [version 1.7.2; Chang et al. 2022] that performs such visual analysis for all batters who faced at least 1000 pitches in the 2019 MLB season. The app is available at https://ryanyee3 .shinyapps.io/batter_evaluation_app/. 

### **4.3 Summary metrics** 

We can complement our visual analysis using several aggregate metrics to summarize the performance of batters over an entire season. Importantly, although it is tempting to compare players with these metrics, such comparisons are 

confounded by differences in pitch situations across players. Similar to how a batter’s RBI depends on how often his teammates get on base, a batter’s plate-discipline metrics are dependent on the pitches he sees. In Section 5.1 we elaborate on potential methods for making these metrics more comparable and the computational challenges in doing so. 

Our first aggregate metric is the proportion of pitches where the batter actually makes the xR_optimal decision. To account for our uncertainty in the xR_optimal decision, we calculated this proportion for every posterior sample of xR_optimal, and compute a credible interval for this metric. We found that, on average, batters made the xR_optimal decision 69.4 % of the time in the 2019 MLB season. For reference, based on the traditional heuristic that a disciplined batter swings at pitches inside the strike zone and takes pitches outside the strike zone, batters made the disciplined decision 68.4 % of the time in the 2019 MLB season. In our dataset, Jonathan Luplow appeared to be the most disciplined batter, making the xR_optimal decision on 76.8 % of pitches (90 % credible interval: [46.1 %, 88.7 %]). The least disciplined batter in our dataset, Jorge Alfaro, made the xR_optimal decision on 61.4 % of pitches (90 % credible interval: [37.7 %, 83.2 %]). These numbers closely align with traditional plate discipline metrics that credit Luplow and Alfaro with making the disciplined decision 76.4 % and 60.7 % of the time, respectively. 

Figure 7 compares the proportion of xR_optimal decisions to the proportion of traditionally “correct” decisions. 



**Figure 7:** Proportion of pitches where the batter made the xR_optimal decision versus proportion of pitches where the batter swung (resp. took) pitches inside (resp. Outside) the strike zone. Includes all batters who faced at least 1000 pitches in the MLB 2019 regular season. The blue line is the least-squares regression line and the dashed red line is the line the data would follow if both metrics were identical. 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 15** 

**Table 1:** Year-to-year correlation of metrics. 

||**Prop**|**ortion xR_o**|**ptimal**|**Trad**|**itional me**|**trics**|
|---|---|---|---|---|---|---|
||**2017**|**2018**|**2019**|**2017**|**2018**|**2019**|
|2017|1.000|0.714|0.722|1.000|0.772|0.740|
|2018|0.714|1.000|0.735|0.772|1.000|0.790|
|2019|0.722|0.735|1.000|0.740|0.790|1.000|



We find a moderate correlation (0.750) between the two metrics indicating that batters who follow the traditional plate discipline heuristics tend to make the xR_optimal decision more often. We observe a shrinkage-like effect where the distribution of batters based on our metric are more tightly clustered around the sample average compared to traditional metrics. This finding is unsurprising, given the partial pooling performed by our BART models. We also found that our metric has similar year-to-year consistency as traditional metrics (see Table 1 in Appendix A.2). 

Our second aggregate metric measures the total impact a batter’s decisions have on expected runs over an entire season by taking the difference in expected runs between the decision the batter made and the alternative decision and summing over every pitch a batter faces. In terms of the plots in Figure 5, let<sup>∑</sup> _p_<sup>EVdiffbethesumof EVdiff</sup> of all the pitches shown in panel _p_ . Then the expected runs added over an entire season is 



Figure 8 shows a histogram of the posterior mean of expected runs added for all batters who faced at least 1000 pitches in the 2019 season. We find the difference between the best and worst batters according to this metric is not 

— large only about 0.1 expected runs. We further find that there is considerable overlap in the 90 % credible intervals of the expected runs added (see Figure 11). For instance, we estimate the top batter, Jordan Luplow, on average adds 0.08 expected runs per pitch due to his decision-making with a − 90 % credible interval of [ 0.06, 0.21] while the worst batter, Javier Baez, adds 0.03 expected runs per pitch on average − with a 90 % credible interval of [ 0.13, 0.18]. 

While informative, the expected runs added metric has limitations. We argue that if a batter faces many lowleverage pitches (i.e. pitches where |EVdiff| is close to zero) he will have fewer opportunities to pick up added runs than batter’s facing many high-leverage pitches (i.e. pitches where |EVdiff| is large). To account for this situation, we calculated runs lost as the minimum of 0 and the runs added from a pitch. To motivate this metric, we argue that when a batter faces a low-leverage pitch, his decision does not matter since it may be unclear what the best decision is. For example, in Figure 5 panel (b) there are many pitches inside the strike zone that Trout swings at that, while the xR_optimal decision is to take, there is still considerable uncertainty in the xR_optimal decision. Since the most a batter can be punished on a given pitch is the expected runs lost by not making the xR_optimal decision, on lowleverage pitches the batter will either not be penalized or be penalized by a small amount. When a batter faces a highleverage pitch, the xR_optimal decision should be obvious, so a batter that does not make the xR_optimal decision on these pitches will be severely punished. In terms of the plots in Figure 5, runs lost is 



Results of expected runs lost are similar to the results of expected runs added: the absolute differences between the best and worst batters are small (see Figure 8) with considerable overlap in credible intervals (see Figure 12). We 



**Figure 8:** Distributions of posterior means of batters who faced at least 1000 pitches in the 2019 MLB season for each summary metric. 

> **16 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 

estimate the top batter, Andrew McCutchen, has an average loss of 0.03 expected runs per pitch with a 90 % credible interval of [0.01, 0.09] while the worst batter, Jorge Alfaro, lost 0.07 expected runs per pitch on average with a 90 % credible interval of [0.01, 0.20]. 

For all three of these metrics, we find that there are a few batters who do much better than everyone else and a few who are much worse. Figure 8 shows the distribution of these metrics for batters that faced at least 1000 pitches in the 2019 MLB season. 

## **5 Discussion** 

We developed a three-step framework for estimating the optimal swing/take decision of batters in Major League Baseball. In the first step of our framework, we estimate, for a given pitch, (i) the probability the umpire will call a strike; (ii) the probability a batter will make contact; and (iii) the expected number of runs the batting team will score in the remainder of the inning after a ball, strike, contact, and miss. Then, we combine these estimates to calculate the expected runs following a swing and a take decision. Finally, we determine the xR_optimal decision to be the one that leads to more expected runs. We adopt a Bayesian approach which allows us to propagate uncertainty from each intermediate estimate to our evaluation of the xR_optimal decision. 

Our findings have several implications for Major League Baseball teams. First, we can determine those batters who consistently make xR_optimal swing decisions, which can aid in player evaluation. We can also identify pitch locations where a batter consistently makes suboptimal swing decisions. Batters can use this information to make adjustments to their decision-making, while pitchers can use this information to target locations where a batter is likely to make a decision that costs his team runs. Finally, we can identify locations where pitches are likely to lead to a significant increase in expected runs (i.e. locations with high EVdiff). Pitchers can use this information to avoid these locations to minimize the opportunities for the batting team to score. 

We found that across the league, batters made the xR_optimal decision 69.4 % of the time according to our model, which aligns with the findings of other plate discipline studies. Critically, we should ask ourselves why are our results so similar to the simpler traditional plate discipline metrics. One explanation is that, despite their somewhat heavy-handed assumptions (e.g. one should swing at every pitch in the strike zone and take every pitch outside 

the zone), traditional metrics offer a reasonably accurate approximation of our more fine-grained model. 

Like umpires, batters are not robots: just as umpires do not strictly adhere to the rulebook definition of the strike zone, batters almost certainly consider more than just expected runs when making swing decisions. The fact that batters deviated from the xR_optimal decision about 30 % of the time suggests that batters do not always consider expected runs when making swing decisions. For example, a player chasing a home run record (e.g., Aaron Judge at the end of the 2022 season) may make swing decisions to maximize expected home runs. While these decisions are not xR_optimal, they might be optimal when viewed through the lens of expected home runs. 

### **5.1 Limitations and future work** 

We presented an analysis of plate discipline that asserts the “disciplined” swing decision is the one that leads to a greater number of expected runs. While we believe our assertion is reasonable, an honest argument could be made that this is an incorrect characterization of a “disciplined” swing decision. In such cases, our modular framework gives us the flexibility to use any other objective to evaluate batters. For example, we could replace _R_ in each branch of Figure 2 with another team outcome (e.g., win probability) or individual outcome (e.g., home runs, wOBA, OPS) and follow the same strategy: estimate intermediate probabilities and conditional expectations; compute the expected outcome following a swing and following a take; and determine the optimal decision. 

While we used BART to fit the three models in the first step of our framework, other choices are possible. Indeed, we selected BART for its ease-of-use: we did not have to manually pre-specify the functional forms of the called strike and contact probabilities and run expectancy, which we suspected depended on complicated non-linearities and interactions. Although our BART-based models slightly outperformed parametric alternatives, these differences in outof-sample predictive power were not especially large. For instance, we found that our BART model of called strike and contact probabilities, which accounted for location, game state, and pitch personnel, achieved very similar predictive performance as a generalized additive model that only accounted for location. Such a finding, to us, suggests that pitch location is, by far, the main driver of strike and contact probabilities, with other predictors like outs or count or player identifies contributing little additional predictive power. We also found that the difference in outof-sample RMSE between our BART-based run expectancy 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 17** 

model, BARTxR, and the best-performing alternative based on binning and averaging was about 0.01 runs. While this is a small difference on a per-pitch basis, these differences can magnify over the course of an entire season. 

More substantively, we only considered two possible outcomes following a swing decision, a miss or contact. We could extend our framework to account for more postswing outcomes like miss, foul, out, single, double, triple, and home run in one of two ways. First, we could replace our binary contact probability model with Murray (2021) multinomial logistic BART model. In the context of Figure 2, this would involve replacing the contact branch with several branches. Alternatively, we could augment our existing framework with a further model of these outcomes _conditional_ on making contact. That is, we could add additional child branches to the contact branch of Figure 2, one for each potential outcome following contact. We note that the developers of EAGLE pursued the first strategy. We suspect, however, that the second approach would lead to less uncertainty about the xR_optimal decision as the overall accuracy of our contact/miss model is better than the reported accuracy of EAGLE’s multi-outcome model. 

Beyond a pitch-by-pitch visual assessment, we introduced three aggregate metrics that tracked the proportion of times batters made the xR_optimal decision and the expected number of runs added or lost due to plate discipline across an entire season. Although it is tempting to compare these metrics across players, these metrics are confounded by pitch location and the context in which players see different pitches. Simply put, because the distribution of pitches one batter sees may differ from the distribution seen by another batter, it is difficult to directly compare their aggregated plate discipline metrics. To overcome such confounding, we could first marginalize EVdiff over  and  before computing in a manner similar to Jensen, Shirley, and Wyner (2009) spatially aggregate fielding evaluation. While such spatially and contextually aggregated plate discipline metrics are intuitively appealing, computing them introduces considerable computational challenges. Basically, to marginalize over  and , we must make predictions for every combination of batter and pitch in our dataset. We leave efficient computation of the approximately seven hundred million combinations required for such marginal combinations to future work. 

Although we did not control for pitch-related factors like type, velocity, or spin, including them in our models is relatively straightforward. Accounting for pitch sequencing is somewhat harder. One approach would be to include information about the previous _k_ pitches as additional covariates. However, determining the appropriate lag _k_ is 

highly non-trivial, since it may vary batter-to-batter (in the case of contact probability) or umpire-to-umpire (in the case of called strike probability). Relatedly, our strike and contact probability models both condition on the location of the pitch as it crosses the front edge of home plate. Insofar as batters decide to swing or take the pitch before it reaches home plate, one could reasonably argue that such precise location information is unavailable to the batter. Rather than omit pitch location from our strike and contact probability models, a more realistic model would incorporate the trajectory (or portions thereof) of the pitch as it travels from the pitcher’s hand to home plate. Incorporating _functional_ predictors into BART and other tree-based models is an interesting and important methodological challenge. 

#### **Research ethics:** Not applicable. 

**Author contributions:** The authors have accepted responsibility for the entire content of this manuscript and approved its submission. 

**Competing interests:** The authors state no conflict of interest. 

**Research funding:** Support for this work was provided by the University of Wisconsin–Madison, Office of the Vice Chancellor for Research and Graduate Education with funding from the Wisconsin Alumni Research Foundation (DOI: 10.13039/100001395). 

**Data availability:** Code to download and pre-process the data used in this paper is available at https://github.com/ ryanyee3/plate_discipline_code. 

## **A Appendix** 

### **A.1 Cross-validation results** 

Figure 9 reports the relative mean-square error (i.e. Brier score) for strike and contact probability BART models fit with every combination of  and  relative to the full BART model fit with ,  and . Because these models do not adjust for pitch location , the relative MSEs are much larger than those shown in Figure 3. 

### **A.2 Stability of summary metrics** 

Table 1 shows the year-to-year correlation of (i) the proportion of pitches where a batters makes the xR_optimal decision and (ii) the proportion of pitches where a batter swung if the pitch was inside the strike zone and took if the pitch was outside the strike zone. Batters who faced at least 1000 pitches in all three MLB regular seasons from 2017 to 2019 were included. 

> **18 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 



**Figure 9:** Out-of-sample mean-squared error relative to a BART model fit with , , and  for strike (a) and contact (b) probabilities. 



**Figure 10:** Boxplots of posterior samples of the proportion of pitches where the batter made the xR_optimal decision for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. 

### **A.3 Additional figures** 

Figure 10 shows boxplots of the proportion of pitches where batter’s made the xR_optimal decision for each posterior 

sample for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. There is considerable uncertainty in the proportion of pitches where batter’s made the xR_optimal decision, and the overlap 

> R. Yee and S. K. Deshpande: Bayesian plate discipline **— 19** 



**Figure 11:** Boxplots of posterior samples of the runs added metric for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. 



**Figure 12:** Boxplots of posterior samples of the runs lost metric for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. 

> **20 —** R. Yee and S. K. Deshpande: Bayesian plate discipline 

between batters demonstrates the difficulty in differentiating batters. 

Figure 11 shows boxplots of the runs added metric for each posterior sample for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. The boxplots show considerable uncertainty in these estimates, and overlap in distributions between batters demonstrates the difficulty in differentiating batters based on this metric. 

Figure 12 shows boxplots of the runs lost metric for each posterior sample for the top 10 and bottom 10 batters who faced at least 1000 pitches in the 2019 MLB regular season. There is considerable uncertainty in these estimates, and overlap in distributions between batters demonstrates the difficulty in differentiating batters based on this metric. 

## **References** 

- Arthur, R. 2014a. _Moonshot: The New Best Way to Measure Plate Discipline_ . Also available at: https://www.baseballprospectus.com/news/ article/25008/moonshot-the-new-best-way-to-measure-platediscipline/. 

- Arthur, R. 2014b. _Moonshot: The Victims of a Bad Strike Zone_ . Also available at: https://www.baseballprospectus.com/news/ article/24862/moonshot-the-victims-of-a-bad-strike-zone/. 

- Brill, R. S., S. K. Deshpande, and A. J. Wyner. 2022. “A Bayesian Analysis of the Time through the Order Penalty in Baseball.” _arXiv preprint arXiv:2210.06724_ . 

- Center for High Throughput Computing. 2006. _Center for High Throughput Computing_ . 

- Chang, W., J. Cheng, J. Allaire, C. Sievert, B. Schloerke, Y. Xie, J. Allen, J. McPherson, A. Dipert, and B. Borges. 2022. _Shiny: Web Application Framework for R_ . 

- Chen, D. L., T. J. Moskowitz, and K. Shue. 2016. “Decision Mkaing under the Gambler’s Fallacy: Evidence from Asylum Judges, Loan Officers, and Baseball Umpires.” _Quarterly Journal of Economics_ 131 (3): 1181−242 **.** 

- Chipman, H. A., E. I. George, and R. E. McCulloch. 2010. “BART: Bayesian Additive Regression Trees.” _Annals of Applied Statistics_ 4 (1): 266−98 **.** 

- Deshpande, S. K. (2023). “flexBART: Flexible Bayesian regression trees with categorical predictors.” _arXiv preprint_ arXiv:2211.04459. 

- Deshpande, S. K., and A. J. Wyner. 2017. “A Hierarchical Bayesian Model of Pitch Framing.” _Journal of Quantitative Analysis in Sports_ 13 (3): 95−112 **.** 

- Green, E., and D. P. Daniels. 2014. “What Does it Take to Call a Strike? Three Biases in Umpire Decision Making.” In _MIT Sloan Sports Analytics Conference_ . 

- Green, E., and D. Daniels. 2022. “Bayesian Instinct.” _SSRN preprint 2916929_ . 

- Jensen, S. T., K. E. Shirley, and A. J. Wyner. 2009. “Bayesball: A Bayesian Hierarchical Model for Evaluating Fielding in Major League Baseball.” _Annals of Applied Statistics_ 3 (2): 491−520 **.** 

- Kim, J. W., and B. G. King. 2014. “Seeing Stars: Matthew Effects and Status Bias in Major League Baseball Umpiring.” _Management Science_ 60 (11): 2619−44 **.** 

- Lindbergh, B. 2013. _The Art of Pitch Framing_ . Also available at: http:// grantland.com/features/studying-art-pitch-framing-catchers-suchfrancisco-cervelli-chris-stewart-jose-molina-others/. 

- Marchi, M. 2011. _Evaluating Catchers: Quantifying the Framing Pitches Skill_ . Also available at: https://tht.fangraphs.com/evaluating-catchersquantifying-the-framing-pitches-skill/. 

- Mills, B. M.. 2014. “Social Pressure at the Plate: Inequality Aversion, Status, and Mere Exposure.” _Managerial and Decision Economics_ 35 (6): 387−403 **.** 

- Mills, B. M.. 2017. “Technological Innovations in Monitoring and Evaluation: Evidence of Performance Impacts Among Major League Baseball Umpires.” _Labour Economics_ 46: 189−99 **.** 

- Mould, J., and D. Anderson. 2022a. _Quantifying Hitter Plate Discipline with Eagle: Part 1_ . Also available at: https://www.baseballprospectus .com/news/article/74173/quantifying-hitter-plate-discipline-witheagle-part-1/. 

- Mould, J., and D. Anderson. 2022b. _Quantifying Hitter Plate Discipline with Eagle: Part 2_ . Also available at: https://www.baseballprospectus .com/news/article/74214/quantifying-hitter-plate-discipline-witheagle-part-2/. 

- Murray, J. S. 2021. “Log-linear Bayesian Additive Regression Trees for Multinomial Logistic and Count Regression.” _Journal of the American Statistical Association_ 116 (534): 756−69 **.** 

- Petti, B., and S. Gilani. 2022. _Baseballr: Acquiring And Analyzing Baseball Data_ . 

- Slowinski, P. 2010. _Plate Discipline_ . Also available at: https://library .fangraphs.com/offense/plate-discipline/. 

- Tango, T., M. Lichtman, and A. Dolphin. 2007. _The Book: Playing the Percentages In Baseball_ . Sterling, Virginia: Potomac Books. 

- Vock, D. M., and L. F. B. Vock. 2018. “Estimating the Effect of Plate Discipine Using a Causal Inference Framework: An Application of the G-Computation Algorithm.” _Journal of Quantitative Analysis in Sports_ 14 (2): 37−66 **.** 

- Wood, S. 2017. _Generalized Additive Models: An Introduction with R_ , 2nd ed. Boca Raton: Chapman and Hall/CRC. 


