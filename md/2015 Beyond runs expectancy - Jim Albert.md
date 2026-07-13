<!-- source: 2015 Beyond runs expectancy - Jim Albert.pdf -->

3 

Journal of Sports Analytics 1 (2015) 3–18 DOI 10.3233/JSA-140001 IOS Press 

# Beyond runs expectancy 

## Jim Albert<sup>∗</sup> 

_Department of Mathematics and Statistics, Bowling Green State University, Bowling Green, OH, USA_ 

Received: 7 July 2014; revised 7 July 2014; accepted: 5 December 2014 

**Abstract** . George Lindsey was one of the first to present run scoring distributions of teams of Major League Baseball. One drawback of Lindsey’s approach is that his calculations represented a situation where the team is average. By use of a multinomial/multilevel modeling approach, we look more carefully how run-scoring distributions vary between teams and how run-scoring is affected by different covariates such as ballpark, pitcher quality, and clutch situations. By use of exchangeable models over ordinal regression coefficients, one gets a better understanding which covariates represent meaningful differences between run-scoring of teams. 

Keywords: Multilevel modeling, clutch hitting, multinomial, ordinal regression modeling 

### **1. Introduction** 

- _1.1. George Lindsey and the runs expectancy matrix_ 

One the pioneers in sabermetics was George Lindsey, a defense consultant in Canada who had a great loveforbaseball.Lindseywrotetworemarkablepapers in the 1960’s that had a great influence on the quantitative analysis of baseball. In particular, Lindsey (1963) focused on several questions of baseball strategy such as stealing a base, sacrificing to sacrifice a runner to second base, and issuing an intentional walk. Lindsay observed that these questions could be answered by the collection of appropriate data. 

“By collecting statistics from a large number of baseball games it should be possible to examine the probability distributions of the number of runs resulting from these various situations. Object of all choices is ... to maximize the probability ... of winning the game.” 

> ∗Corresponding author: Jim Albert, Department of Mathematics and Statistics, Bowling Green State University, Bowling Green, OH, USA. Tel.: +1 419 372 7456; Fax: +1 419 372 6092; E-mail: albert@bgsu.edu. 

Lindsay noted that the probability of winning at a point during the game depends on the current score and inning and presented tables of _W_ ( _I, Hi_ ), the probability a team with a lead of _I_ runs at the home half of the _i_ th inning _Hi_ will win the game. 

In this paper, Lindsey also considered the runs scoring distribution of a team during an inning. He focused on the run potential, the number of runs a team will score in the remainder of the inning. He noted that the runpotentialdependsonthecurrentnumberofoutsand the runners on base. Since there are three possible number of outs and eight possible runner configurations, there are 3 × 8 = 24 possible out/runner situations, and Lindsey focused on computing 

### _Prob_ ( _R_ | _T, B_ ) _,_ 

the probability of scoring exactly _R_ runs in the remainder of the inning given _T_ outs and runners on base _B_ . 

To learn about run potential, Lindsey’s father collected run-scoring data for over 6000 half-innings in games during the 1959 and 1960 seasons, and Lindsey was able to find empirical run-scoring distributions for each of the 24 situations. By computing the mean runs for each situation, he produced the runs expectancy matrix as displayed in Table 1. 

ISSN 2215-020X/15/$27.50 © 2015 – IOS Press and the authors. All rights reserved 

This article is published online with Open Access and distributed under the terms of the Creative Commons Attribution Non-Commercial License. 

_J. Albert / Beyond runs expectancy_ 

4 

Table 1 

Lindsey’s runs expectancy matrix from Lindsey (1963) 

|Outs||||Bases o|ccupie|d|||
|---|---|---|---|---|---|---|---|---|
||0|1|2|3|1,2|1,3|2,3|1,2,3|
|0 Outs|0.46|0.81|1.19|1.39|1.47|1.94|1.96|2.22|
|1 Out|0.24|0.50|0.67|0.98|0.94|1.12|1.56|1.64|
|2 Outs|0.10|0.22|0.30|0.36|0.40|0.53|0.69|0.82|



At the beginning of an inning with no outs and bases empty, a team will score, on average, 0.46 runs in the remainder of the inning. In contrast, when the bases are loaded with one out, a team will score 1.64 runs in the rest of the inning. 

The runs expectancy table has been illustrated in a number of sabermetrics books such as Thorn et al. (1984), Albert and Bennett (2003), Keri et al. (2007) and Tango et al. (2007) for deciding on proper baseball strategy, for learning about the value of plays, and for evaluating players. For example, Chapter 7 of Albert and Bennett (2003) shows the use of run expectancies in determining the values of singles, doubles, triples, and home runs that leads to use of linear weights to measure batting performances. Chapter 9 of Albert and Bennett (2003) uses the run expectancy table to assess the value of common baseball strategies such as a sacrifice bunt, intentional walk, and stealing a base. 

Lindsay (1963) cautioned that the run expectancy table represented the situation where all players were “average”. 

“It must be reiterated that these calculations pertain to the mythical situation in which all players are ‘average’. The allowance for the deviation from average performance of the batter at the plate, and those expected to follow him, or of runners on the bases, can be made by a shrewd manager who knows his players.” 

Also Lindsey (1963) mentioned the possibility of extending this analysis to run-scoring of teams with non-average players. 

“If it were desired to provide a manager with a guide to the advisability of attempting various strategies in different situations, it would be possible to complete calculations of the type outlined here for all stages of the game and scores, pertaining to average players. It would also be possible, although onerous, to compute tables for nonaverage statistics, perhaps based on the past records of the individual players on the team.” 

Table 2 

Basic probability model fits to runs scored in MLB. The Actual column gives the observed fractions of scoring 0, 1, 2, ... runs in the 2013 season and the Poisson and NB columns give the estimated fractions from fitting the Poisson and negative binomial distributions 

|Runs|Actual|Poisson|NB|
|---|---|---|---|
|||_λ_=0_._462|_n_=0_._399_,p_=0_._464|
|0|0.738|0.630|0.736|
|1|0.146|0.291|0.158|
|2|0.066|0.067|0.059|
|3|0.029|0.010|0.025|
|4|0.013|0.001|0.012|
|5|0.005|0.000|0.005|
|6|0.002|0.000|0.003|
|7|0.001|0.000|0.001|



### _1.2. Modeling runs scored in an inning_ 

A related line of research is the use of probability models to represent the number of runs scored in an inning or a game. Fits of basic discrete probability models do not accurately represent actual runs scored in an inning. To demonstrate this claim, the Poisson ( _λ_ ) and negative binomial ( _n, p_ ) models were separately fit to all inning runs scored in the 2013 season and the fitted probabilities for these two models and the actual run-scoring distribution are displayed in Table 2. Looking at the table, the Poisson fit underestimates the probability of a scoreless inning. Generally, the Poisson fit understates the actual variability in runs scored. The negative binomial fit is better than the Poisson, but this model overestimates the probability of scoring one run and underestimates the probability of scoring two runs. 

Since basic probability models appear inaccurate, more sophisticated models for run scoring have been proposed in the literature. For example, Rosner et al. (1996) represents the probability of scoring _x_ runs in an inning by the sum 



where _N_ represents the number of batters in the inning. In this paper, the probability function _f_ ( _N_ ) is represented by a modification of a negative binomial distribution, and the conditional distribution of the number of runs given the number of batters, _g_ ( _x_ | _N_ ), is modeled by a truncated binomial distribution. Another approach in Wollner (2000) provides an exponential formula for the probability a team averaging _A_ runs per game scores _R_ runs in a particular inning. 

5 

_J. Albert / Beyond runs expectancy_ 

### _1.3. Multilevel modeling_ 

Another research theme in modeling of sports data is the use of multilevel or hierarchical models to estimateparametersfromseveralgroups.EfronandMorris (1975) illustrate the use of an exchangeable model to estimate true batting averages of 18 players from the 1970 season. Albert (2004, 2006) provide further illustrations of the use of an exchangeable model to estimate a set of true batting rates or pitching rates. These models can be extended to the regression framework. Morris (1983) uses an multilevel regression model to assess if Ty Cobb was ever a true .400 hitter. Albert (2009) uses an exchangeable regression model to simultaneously estimate the true pitching trajectories for a number of pitchers. 

### _1.4. Plan of the paper_ 

This paper provides an multilevel modeling framework for understanding run scoring of teams in Major League Baseball, and understanding how team run scoring is affected by several factors, such as ballpark, pitcher quality, and runners in scoring position. The basic multilevel model, described in Section 2.1, simultaneously estimates means from several populations, say the average number of runs scored for 30 MLB teams, when the means are believed to follow a normal curve model with unknown mean and standard deviation. 

As in Lindsay’s work, we focus on the number of runs scored in a half-inning. A run scoring distribution for a particular team is represented by a multinomial distribution with underlying probabilities over the classes 0 runs, 1 run, 2 runs, 3 runs, and 4 or more runs. Section 2.2 describes a multilevel model for simultaneously estimating a set of multinomial probability vectors. By using this model to estimate the run scoring distributions for the 30 MLB teams, one obtains “improved” estimates at the teams’ abilities to score runs. 

After estimating teams’ scoring distributions, we next explore team situational effects. An ordinal regression model, described in Section 2.3, is a useful method for describing how run-scoring probabilities change as one changes a predictor such the quality of a pitcher. This model can be described in terms of the odds of scoring at least a particular number of runs. It is called a proportional odds model as a change in the predictor will result in the odds of scoring runs being 

increased by a constant factor. Section 3.2 introduces the use of odds in comparing run scoring distributions of the National and American Leagues. Section 3.3 extends this approach to compare run scoring of the 30 teams and illustrates the value of multilevel modeling. 

Section 4 focuses on the effect of the following covariates on team run scoring. 

- ( **Home Effects** ) Teams generally score more runs at home compared to away games. What is the general size of the home/away effect for scoring runs and how does this effect vary among the teams? 

- ( **Pitcher Effects** ) Clearly, the pitcher has a significant impact on run-scoring. A strong starting pitcher can neutralize the runs scored by even the best-scoring team in baseball. Generally, one expects that a team’s run scoring is negatively associated with the quality of the pitcher. How can one quantify this pitcher effect, and how does this effect differ among teams? 

- ( **Runner Advancement** ) Run scoring can be viewed as a two-step process – batters get on base and then other batters advance them to home. Do teams differ in their ability to get runners home? 

We address each of these questions by a multilevel ordinal regression model where the effect of the covariate can vary across teams. Section 5 generalizes this approach to handle several covariates at once, Section 6 gives a brief discussion of the potential covariates relevant to run-scoring, and Section 7 summarizes the general findings. 

### **2. Methods** 

### _2.1. Estimating a group of means_ 

Consider the problem of estimating a collection of means from several populations. One observes sample means _y_ 1 _, ..., yN_ , where the sample mean from the _j_ th population, _yj_ is distributed normal with mean _θj_ and known standard error _σj_ . We describe this situation in a baseball setting, where _N_ = 30, _y_ 1 _, ..., y_ 30 correspond to the sample mean numbers of runs scored in a halfinning for the thirty teams for a season, and _θ_ 1 _, ..., θN_ are the corresponding population means of runs scored. 

One can obtain obtained improved estimates at the population means by means of the following multilevel model.Weassumethatthemeans _θ_ 1 _, ..., θ_ 30 representa 

6 

_J. Albert / Beyond runs expectancy_ 

sample from a normal curve with mean _µ_ and standard deviation _τ_ . The locations of the normal curve parameters _µ_ and _τ_ are unknown, and so (under a Bayesian framework) vague or imprecise prior distributions are assigned to these parameters. 

One can fit this multilevel model from the observed sample means of runs scored for the 30 teams. In particular, we estimate the population mean and standard deviation _µ_ and _τ_ by _µ_ ˆ and _τ_ ˆ, respectively. The estimate _µ_ ˆ represents the overall or combined estimate of a population mean of the runs scored from the 30 teams and the estimate ˆ _τ_ represents the spread of these population means. 

### _Three sets of estimates_ 

There are three types of estimates of the population means. If we estimate each population mean only by using data from the corresponding sample, we obtain _individual_ estimates 



On the other extreme, if we assume that the population means are equal, that is, _θ_ 1 = _..._ = _θN_ , then we’d estimate _θj_ by the _combined_ estimate 



where the sample mean _yj_ is weighted by the inverse of the sampling variance 1 _/σj_<sup>2.</sup> 

By use of the multilevel model, we obtain improved estimates of the population means that compromise between the individual and combined estimates. The multilevel (ML) estimate of the population mean for team _j_ , _θ_<sup>ˆ</sup> _j_<sup>_ML_</sup> , is given by 



theThe estimate of the mean runs scored for the _θ_ ˆ _j_<sup>_ML_</sup> combinedshrinks the _µ_ ˆ individual, where theteamsizeestimateof the _y_ shrinkage _jj_ th team,towards depends on the ratio of the estimated population standard deviation _τ_ ˆ to the standard error _σj_ . If _τ_ ˆ is small relative to the standard error _σj_ , then the multilevel estimate _θ_<sup>ˆ</sup><sup>_ML_</sup> will be close in value to the combined _j_ estimate. In contrast, if the estimate ˆ _τ_ is large (relative to the standard error), the multilevel estimate will be close to the individual estimate. 

### _2.1.1. Example_ 

This multilevel model was fit to the sample means of runs scored for the 30 teams in the 2013 season. ˆ We obtain the estimates _µ_ = 0 _._ 461 _,_ ˆ _τ_ = 0 _._ 045, so the population means of the runs scored are estimated by a normal curve with mean 0.461 and standard deviation 0.045. In the 2013 season, Anaheim averaged 0.500 runs scored per inning with a standard error of 0.027. The individual estimate of Anaheim’s mean runs scored is _yj_ = 0 _._ 500 and the combined estimate ˆ is given by _θ_<sup>ˆ</sup><sup>_C_</sup> = _µ_ = 0 _._ 461 _._ The improved multilevel estimate of Anaheim’s mean is given by 



Here the multilevel estimate of Anaheim mean shrinks theindividualestimate26%towardsthecombinedestimate. Across all teams, the median shrinkage is 23%. Since this shrinkage percentage is a small value, this indicates that the observed differences in run scoring between the 30 teams correspond to meaningful differences in the teams’ run-scoring abilities. 

### _2.2. Estimating collections of multinomial data_ 

A related problem is estimating a multinomial population. Suppose we classify data into _k_ bins and observe the vector of frequencies _W_ = ( _w_ 1 _, ..., wk_ ). The vector _W_ is assumed to have a multinomial distribution with sample size _N_ = _w_ 1 + _..._ + _wk_ and probability vector _p_ = ( _p_ 1 _, ..., pk_ ), where _pj_ represents the probability that an observation falls in the _j_ th bin. In our setting, we classify the number of runs scored in an inning in the five bins 0, 1, 2, 3, and 4 or more runs, and the frequencies _w_ 1 _, ..., w_ 5 represent the number of innings where a particular team scores the different number of runs. 

This type of multinomial data on runs scored is collected for each of the 30 baseball teams. Let _W_<sup>1</sup> _, ..., W_<sup>30</sup> denote the vectors of frequencies of runs scored for the 30 teams. We assume the vector for the _j_ th team _W_<sup>_j_</sup> is multinomial with probability vector _p_<sup>_j_</sup> . We are interested in estimating the probability vectors _p_<sup>1</sup> _, ..., p_<sup>30</sup> . As in the population means case, we can consider individual, combined, and multilevel estimates for the probability vectors. 

_J. Albert / Beyond runs expectancy_ 

7 

### _Individual estimates_ 

Suppose we use the data from only the _j_ th team to learn about its run scoring tendencies. Then the probabilities of falling in the different run groups are estimated by the individual estimates: 



where _w_<sup>_j_</sup> 1<sup>_, ..., wj_</sup> _k_<sup>arethebincountsforthe</sup><sup>_j_thteam</sup> and _N_<sup>_j_</sup> is the number of innings for the _j_ th team. 

### _Combined estimates_ 

Instead, suppose we assume that the probabilities of falling in the different runs group are the same for all teams; that is, _p_<sup>1</sup> = _..._ = _p_<sup>30</sup> . Then we can estimate each team’s probability vector by the combined estimate 



Here we are pooling the bin counts for all teams to get the probability estimate for a particular bin. 

### _Multilevel estimates_ 

Wewishtogetimprovedestimatesattheteamprobability vectors _p_<sup>1</sup> _, ..., p_<sup>30</sup> that compromise between the individual estimates and the combined estimates. This is accomplished by means of the following multilevel model. We assume that the unknown probability vectors _p_<sup>1</sup> _, ..., p_<sup>30</sup> are a random sample from a Dirichlet distribution with mean vector _η_ and precision _K_ with density proportional to 



where _η_ = ( _η_ 1 _, ..., η_ 5). The parameters _η_ and _K_ are assigned vague prior distributions. 

One fits this multilevel model to the observed count data and one obtains estimates at _K_ and _η_ from the posterior distribution – call these estimates _K_<sup>ˆ</sup> and _η_ ˆ . (Details of this computation are provided in the appendix.) The estimate _η_ ˆ is approximately the combined estimate _p_ ˆ<sup>_C_</sup> . Then the multilevel estimate at the probability vector of team _j_ is given by 



As anticipated, the multilevel model estimate for the probability vector of team _j_ is approximately a weighted average of the individual estimate _p_ ˆ<sup>_j_</sup> and the combined estimate _p_ ˆ<sup>_C_</sup> . The weights depend on the ratio of the precision parameter estimate _K_<sup>ˆ</sup> and the multinomial sample size _Nj_ . We will illustrate the application of this model in simultaneously estimating the run-scoring distributions of the 30 teams in Section 3.3. (An early use of this Dirchlet distribution in modeling is given in Good (1967) and a good survey of smoothing estimates for multinomial data is provided in Simonoff (1995)). 

- _2.3. Groups of ordinal multinomial data with regression_ 

### _Ordinal logistic regression_ 

Suppose one observes the vector of run frequencies _w_ = ( _w_ 1 _, ..., wk_ ) which is multinomial with probability vector _p_ = ( _p_ 1 _, ..., pk_ ). The categories 1, ..., _k_ are ordinal – in our setting, these categories will be “0 runs”, “1 run”, “2 runs”, etc. Define the probability 



which represents the probability of scoring at least _c_ runs. The odds of scoring at least _c_ runs is given by 



Suppose one observes a variable _x_ that influences the run-scoring probabilities _p_ . The ordinal logistic model (see McCullagh (1980) and Johnson and Albert (1999)) says that the log of the odds of scoring at least _c_ runs is a linear function of _x_ . This model is written as 



where _γc_ and _β_ are unknown parameters. A unit increase in the covariate _x_ results in the log odds of scoring _c_ or more runs to be increased by _β_ . By taking the exponential of both sides, this model can be written in the “proportional odds” form: 



_J. Albert / Beyond runs expectancy_ 

8 

Foreachunitincreaseinthevariable _x_ ,theoddsofscoring at least _c_ runs will increase by a factor of exp( _β_ ). This proportional odds model has the special property that the odds of scoring _c_ or more runs will increase (with a unit increase of _x_ ) by a factor of exp( _β_ ) for all values of _c_ . We illustrate this basic ordinal regression model in comparing the run-scoring distributions of the NL and AL in Section 3.2. 

### **3. League and team differences in scoring** 

### _3.1. Run scoring of all teams in 2013 season_ 

We begin by collecting in Table 3 the runs scored for all complete innings (three outs) in the 2013 season. Since scoring five or more runs in an inning is relatively rare, Table 4 collapses the data from Table 3 by combining the counts of runs four or greater into the class “4+”. 

### _Ordinal logistic regression over groups_ 

As a more general set-up, suppose we observe run-scoring frequencies for _N_ = 30 teams, where the frequencies for the _j_ th team _w_<sup>_j_</sup> is multinomial with probability vector _p_<sup>_j_</sup> = ( _p_<sup>_j_</sup> 1<sup>_, ..., pj_</sup> _k_<sup>).Withthesame</sup> covariate _x_ , we fit the ordinal logistic model to _w_<sup>_j_</sup> of the form 



where _θc_<sup>_j_=</sup><sup>_pj_</sup> _c_<sup>+</sup><sup>_..., pj_</sup> _k_<sup>. In our setting, the regression</sup> coefficient _βj_ represents the additive increase in the logit of scoring at least _c_ runs for the _j_ team for each unit increase in _x_ , and exp( _βj_ ) represents the multiplicative increase in the odds of scoring _c_ or more runs. After performing separate fits of the ordinal model to the run-scoring data for each of the _N_ teams, we obtain theestimates _β_<sup>ˆ</sup> 1 _, ..., β_<sup>ˆ</sup> _N_ withassociatedstandarderrors _σ_ 1 _, ..., σN_ . 

One can now use the estimation of separate means methodology of Section 2.1 to get improved (multilevel) estimates at the regression effects. The true regression effects _β_ 1 _, ..., βN_ are given a normal distribution with mean _µ_ and standard deviation _τ_ , we place vague priors on _µ_ and _τ_ . Improved estimates are provided by fitting this multilevel model – the estimates have the general form 



Thesemultilevelestimates _{β_<sup>ˆ</sup> _j_<sup>_ML_</sup> _}_ adjusttheindividual estimates _{β_<sup>ˆ</sup> _j}_ towards a combined estimate _µ_ ˆ . As will be seen in a later section, the degree of adjustment depends on the sizes of the estimate of the standard deviation of the true effects ˆ _τ_ relative to the size of the standard error estimates _{σj}_ . 

### _3.2. Logits and comparing scoring of the NL and AL_ 

To motivate our general approach, a useful reexpression of a proportion _p_ is the logit _L_ = log � 1− _<u>pp</u>_ �. For example, using data from Table 4, the logit of the proportion of innings where at least one run is scored is 



This particular logit is computed by dividing the data bythebreakpoint“0/1runs”andcomparingtheproportions of the categories “1 or more runs” and “0 runs”. In a similar way, one can divide the data by each of the breakpoints “1/2 runs”, “2/3 runs”, and 3/4+ runs” and compute the logits of the resulting proportions. If we do this for all breakpoints, Table 5 is obtained. 

Logitsareusefulincomparinggroupsofordinaldata such as runs scored. To illustrate, suppose we want to compare the runs scored per inning of National and 

Table 3 

Frequency table of runs scored for all complete innings in 2013 season 

|Runs|Count|Runs|Count|
|---|---|---|---|
|0|32315|6|81|
|1|6400|7|38|
|2|2899|8|14|
|3|1254|9|4|
|4|584|10|1|
|5|207|11|1|



Table 4 

|Counts and percentages of i|nning runs<br>“4+”|scored wit|h the new c|ategory|
|---|---|---|---|---|
|Runs<br>0|1|2|3|4+|
|Count<br>32315|6400|2899|1254|930|
|Percentage<br>73.80|14.60|6.60|2.90|2.10|



_J. Albert / Beyond runs expectancy_ 

9 

Table 5 

Logits of runs scored for all breakpoints 

|Breakpoint|0/1 runs|1/2 runs|2/3 runs|3/4+ runs|
|---|---|---|---|---|
|Proportion scoring<br>“large” runs|0.262|0.116|0.050|0.021|
|Proportion scoring|0.738|0.884|0.950|0.979|
|“small” runs|||||
|Logit = log <sup>_Proportion large_</sup><br>_Proportion small_|<sup>−1.036</sup>|−2.031|−2.944|−3.842|



Table 6 

Runs scored per inning by the American and National Leagues in the 2013 season 

|Runs|0|1|2|3|4+|
|---|---|---|---|---|---|
|American League|15963|3246|1497|654|500|
|National League|16352|3154|1402|600|430|



Table 7 

Logits of runs scored for all breakpoints for the two leagues 

|Breakpoint|0/1 runs|1/2 runs|2/3 runs|3/4+ runs|Median|
|---|---|---|---|---|---|
|American League|−0.996|−1.980|−2.887|−3.755||
|National League|−1.074|−2.082|−3.011|−3.912||
|Difference|0.078|0.102|0.124|0.157|0.113|



American League teams in the 2013 season. First we obtain the counts of runs scored by the two leagues as displayed in Table 6. Each row of counts of the table is converted to proportions, and then logits are computed using each of the four breakpoints. The logits for each league are displayed in Table 7 and the “Difference” row gives the difference in the logits for the two leagues. 

An ordinal regression model is a useful way to summarize the relationship seen in Table 7. If _θc_ is the probability of scoring at least _c_ runs, then the model is 



where the _{γc}_ are parameters defining the cutpoints of the probabilities of scoring on the logit scale, _x_ indicates the league ( _x_ = 1 if AL and _x_ = 0 if NL), and _β_ is the increase in the log odds of scoring _c_ runs or more for the AL league. If we fit this model to the 2013 run scoring data, we obtain the estimates 



Note that the estimates of _γc_ are approximately equal to the logit values given in Table 7. Due to the designated 



<!-- Start of picture text -->
0.10<br>0.05<br>2000 2005 2010<br>Season<br>AL.Advantage<br><!-- End of picture text -->

Fig. 1. American League run-scoring advantage over the National League for the seasons 1998 to 2013, the advantage is the estimate of the parameter _β_ in the fit of the ordinal regression model. A smoothing curve indicates that the American League advantage in scoring runs has remained pretty constant over this time interval. 

hitter, more runs are scored by American League teams and the size of this effect is measured by the coefficient estimate _β_<sup>ˆ</sup> . On the logit scale, the the probability an American League team scores a large number of runs is 0.0822 greater than the probability a National League team scores a large number of runs. There is a nice approximation for differences in logits – for small values of _x_ , an increase of _x_ on the logit scale is approximately a 100 × _x_ percentage increase on the probability scale. Using this interpretation, we can say that the probability an American League team scores a large number of runs is 100 × 0 _._ 0822 = 8 _._ 22% greater than the probability a National League team scores a large number of runs. 

To gain some historical perspective on the runscoringadvantageoftheAmericanLeague,thisordinal regression model was fit for each of the 16 seasons 1998 through 2013. Figure 1 displays a graph of the AL advantage (on the logit scale) against season. It is interesting to note that there is substantial variability in the AL advantage – for example the advantage was 0.121 in 1998 and decreased sharply to 0.019 in 2007. But there is no clear pattern in the changes in AL advantage over this time period. Generally, the probability an AL team scores a large number of runs is about 6% larger than the probability a NL team scores a large number of runs. 

### _3.3. Comparing scoring of teams_ 

How does run scoring vary across teams? If we break down this runs table by the batting team in Table 8, we see some interesting variation in runs scored. 

_J. Albert / Beyond runs expectancy_ 

10 

Table 8 



Percentages of different inning runs scored for all teams in the 2013 

season 

||BAT<br>TEAM|R0|R1|R2|R3|R4|
|---|---|---|---|---|---|---|
|1|ANA|72.4|15.5|6.5|2.8|2.8|
|2|ARI|74.6|13.1|7.1|3.3|1.9|
|3|ATL|74.2|13.5|6.9|2.9|2.5|
|4|BAL|71.1|16.0|7.2|3.4|2.3|
|5|BOS|68.9|15.9|7.9|4.1|3.2|
|6|CHA|75.7|14.2|6.4|2.0|1.6|
|7|CHN|76.3|12.9|6.3|2.7|1.7|
|8|CIN|72.7|16.2|6.2|2.7|2.2|
|9|CLE|71.4|15.4|7.4|3.5|2.4|
|10|COL|72.4|15.1|7.0|3.4|2.1|
|11|DET|72.0|13.6|7.4|3.4|3.5|
|12|HOU|76.7|13.0|5.3|3.2|1.8|
|13|KCA|74.4|14.0|5.6|3.4|1.9|
|14|LAN|73.2|15.3|7.5|2.3|1.7|
|15|MIA|79.1|12.5|4.9|2.2|1.4|
|16|MIL|74.6|14.4|6.6|2.5|1.9|
|17|MIN|74.6|15.2|6.0|2.7|1.5|
|18|NYA|74.6|14.2|6.1|2.9|2.2|
|s 19|NYN|75.8|13.6|6.3|2.5|1.7|
|20|OAK|72.0|14.4|7.9|2.6|3.1|
|21|PHI|75.6|13.8|6.5|2.1|1.9|
|22|PIT|74.4|15.4|5.8|2.6|1.8|
|23|SDN|74.8|15.1|5.7|2.5|1.8|
|24|SEA|74.6|14.7|6.9|2.2|1.6|
|25|SFN|74.6|14.9|5.6|3.4|1.6|
|26|SLN|71.6|15.5|6.8|3.0|3.2|
|27|TBA|71.9|16.1|7.2|2.9|1.8|
|28|TEX|72.5|14.8|7.6|2.6|2.5|
|29|TOR|72.4|14.8|7.4|3.2|2.2|
|30|WAS|74.1|14.4|6.7|3.0|1.9|



Fig. 2. Logit run scoring estimates for all teams. A team’s residual logits were obtained by subtracting the overall logits. 



If one looks at the percentage of big innings (four runs or more), Boston’s percentage of big innings is 3.2, contrasted with Miami’s percentage of 1.4. Boston’s percentage of scoreless innings is 68.9, while the New York Mets were scoreless in 75.8 percent of their innings. 

Fig. 3. Logit run scoring estimates for all teams using a multilevel model. The residual logits were obtained by subtracting the overall logits. 

teams fall within 0.1 (on the logit scale) of the average. Note that some of the team lines are not monotone which indicate the presence of some chance variability in these run scoring estimates. Also, note there is more variability in the logit of 3 or more runs scored – that is a reflection of the small number of occurrences of big innings for the teams. 

The logit approach described in Section 3 is used to facilitate comparisons in team scoring. Logits were computed for each team using the four breakpoints. For example, for Philadelphia, we computed the four logits 





To help in interpretation, the collection of logits for each team was converted to a residual by subtracting the MLB logits found in Table 5, and the team logit residuals are displayed in Fig. 2. Teams with lines above the horizontal line at zero represent aboveaverage scoring teams. The run scoring for most of the 

### _3.4. Multilevel modeling of team run distributions_ 

Since there appears to be chance variability in the estimates of run scoring for the individual teams, there 

_J. Albert / Beyond runs expectancy_ 

11 

may be some advantage to estimating the run scoring distributions simultaneously using a multilevel model. The exchangeable model of Section 2.2 is fit to the run distributions for the 30 teams. The estimate of the smoothing parameter _K_ is 1973. Most teams play close to the median number of innings 1457. So the size of the shrinkage of the individual estimates towards the combined estimate is 



The multilevel estimates shrink the observed percentages approximately 57% towards the combined estimate. Figure 3 displays the logit reexpression of these multilevel estimates. We see these multilevel estimates adjust the individual estimates towards the combined estimate represented by the horizontal line at zero. One attractive feature of these estimates is that they remove some of the nonmonotone behavior of the individual estimates and reduces the variability in the logits of runs scored that we saw in Fig. 2. From similar experience with the use of multilevel models in estimating a collection of batting averages, we would expect these multilevel model estimates to provide better predictions than individual estimates of team run-scoring for future games. 

### **4. Covariate effects** 

### _4.1. General method_ 

Section 3 introduced the use of logits in the comparison of run-scoring distributions. To explore the effect of specific covariates like home/away, pitcher quality, and clutch hitting on scoring, we fit the general ordinal logistic model of the form 



where _θc_ is the probability of scoring at least _c_ runs, and _x_ is the covariate of interest (either of the categorical or measurement type). To understand how the covariate influences run scoring for all MLB teams, we use the following two-step modeling approach. 

1. The ordinal logistic model is first fit separately to run-scoring data for each of the 30 teams. One obtains the regression effects _β_<sup>ˆ</sup> 1 _, ...β_<sup>ˆ</sup> 30 

   - with associated estimated standard errors _σ_ ˆ 1 _, ... σ_ ˆ 30. 

2. The multilevel exchangeable model in Section 2.1 is used to simultaneously estimate the regression effects. We assume the estimated covariate effect _β_<sup>ˆ</sup> _j_ is normal with mean _βj_ and standard error _σ_ ˆ _j_ . Once the estimates _β_<sup>ˆ</sup> 1 _, ...β_<sup>ˆ</sup> 30 are computed, we are interested in simultaneously estimating the set of true effects _β_ 1 _, ..., β_ 30. The improved estimate of the covariate effect for the _j_ th team 



is a compromise between the individual estimate _β_ ˆ _j_ and a combined estimate _β_ ˆ<sup>_C_</sup> . The size of the shrinkage of the individual estimates towards the combined estimate depends on the size of _τ_ ˆ, the spread of the true effects _{βj}_ . 

### _4.2. Home versus away effects_ 

To consider a team’s scoring advantage of playing at home, write the logit of the probability of scoring at least _c_ runs by 



where the variable _HOME_ is equal to 1 if the team is playing at home, and _HOME_ = 0 otherwise. If one computes the difference in the logits of the probability of scoring at least _c_ runs at home _θc_<sup>_H_, and away</sup><sup>_θ_</sup> _c_<sup>_A_, one</sup> obtains 



or 



This ordinal regression model is initially fit to runscoring data for all teams in the 2013 season and one obtains the covariate estimate _β_<sup>ˆ</sup> = 0 _._ 032. The interpretation is that the ratio of the odds of scoring at least _c_ runs at home and away is equal to exp(0 _._ 032) = 1 _._ 032. Specifically, the probability that a team scores at least one run in an inning is increased by 3% at home, the probability a team scores at least two runs in an inning is increased by 3%, and so on. 

_J. Albert / Beyond runs expectancy_ 

12 



<!-- Start of picture text -->
Home Effects<br>WAS<br>TOR<br>TEX<br>TBA<br>SLN<br>SFN<br>SEA<br>SDN<br>PIT<br>PHI<br>OAK<br>NYN<br>NYA<br>MIN<br>MIL<br>MIA<br>LAN<br>KCA<br>HOU<br>DET<br>COL<br>CLE<br>CIN<br>CHN<br>CHA<br>BOS<br>BAL<br>ATL<br>ARI<br>ANA<br>−0.25             0.00         0.25       0.50<br>Estimate<br>Team<br><!-- End of picture text -->

Fig. 4. Individual and multilevel home field run effects for all teams. The black line represents the individual estimate plus and minus the standard error and the red line represents the multilevel estimate plus and minus the standard error. 

Since ballparks are known to have a significant impact on scoring, it is natural to fit this home/away model for each of the 30 teams. Figure 4 displays the individual estimates of the parameters _β_ 1 _, ..., β_ 30 as black dots where the endpoints of the bars correspond to the estimates plus and minus the standard errors. As expected, the individual home/away estimates show = substantial variability from the New York Mets ( _β_<sup>ˆ</sup> _j_ −0 _._ 31) to the Colorado Rockies ( _β_<sup>ˆ</sup> _j_ = 0 _._ 52). 

Next we apply the multilevel model of Section 2.1 to simultaneously estimate the 30 home effects ˆ _β_ 1 _, ..., β_ 30. One obtains the multilevel estimates _µ_ = ˆ ˆ 0 _._ 071 and _τ_ = 0 _._ 114. The estimate _µ_ represents an averageballparkeffectand ˆ _τ_ isanestimateatthespread of the true ballpark effects. Here the multilevel model estimates of { _βj_ } shrink the individual estimates 52% of the way towards the combined estimate _µ_ ˆ . The red bars in Fig. 4 show the posterior means plus and minus the posterior standard deviations. Since the size of the shrinkage is relatively small, this indicates that there is sizeable variation between the true home park effects. 

### _4.3. Pitcher effects_ 

The same ordinal regression approach can to be used to learn about the pitcher effect on team run-scoring. The logit of the probability of scoring at least _c_ runs in a half-inning is given by 



where the variable _PITCHER_ is a measure of the quality of the pitcher who starts to pitch the half-inning. 

The challenge in this approach is to find a good measure of pitcher quality. Many pitchers are of the relief type with a small number of plate appearances, and the measurements of pitcher quality typically show high variability. We use a multilevel model approach to obtain improved estimates of pitcher quality and these improved estimates are used as covariates in the ordinal model for run scoring. 

To begin, we use a run value approach illustrated in Albert and Bennett (2003), Keri et al. (2007) and Tango 

_J. Albert / Beyond runs expectancy_ 

13 



<!-- Start of picture text -->
−0.04 −0.02 0.00 0.02 0.04<br>Pitcher Ability<br>35<br>30<br>25<br>20<br>15<br>10<br>5<br>0<br><!-- End of picture text -->

Fig. 5. Histogram of abilities of all pitchers in 2013 season. 

et al. (2007) to measure the quality of all pitchers who played in the 2013 season. For each plate appearance (PA), we measure the run value as 

### RUNS = Run Potential after PA 

### −Run Potential before PA + Runs Scored _,_ 

where the run potential values come from the runs expectancy matrix (see Table 1) using 2013 season data.Forthe _j_ thpitcherinthe2013season,wecompute the mean run value _y_ ¯ _j_ and the number of PA’s _nj_ . We assume that _y_ ¯ _j_ is approximately normally distributed with mean _µj_ and standard error _σ/_<sup>~~√~~</sup> _<u>nj</u>_ , where _σ_ is estimated using all of the run values for the season. If we have _N_ pitchers, then we estimate the population means _µ_ 1 _, ..., µN_ by use of an exchangeable multilevel model (see Section 2) and the corresponding multilevel estimates _µ_ ˆ 1 _, ..., µ_ ˆ _N_ are used as surrogates for the qualities of the _N_ pitchers in the ordinal regression model. 

Figure 5 displays a histogram of the run value measures of the 679 pitchers in the 2013 season. These multilevel estimates shrink the individual mean run value estimates towards the overall value, the degree of shrinkage depending on the number of batters faced. For pitchers who faced fewer than 100 batters, the shrinkage exceeds 80%; for a starter facing 900 batters, the shrinkage was only 35%. In this particular season, Clayton Kershaw stands out with a run value measure of −0 _._ 036 – since he faced 934 batters, he saved 934 × −0 _._ 036 = −33 _._ 6 runs during the 2013 season. 

If the ordinal regression model with pitcher quality covariate is fit to data for all teams, one obtains 

the estimate _β_<sup>ˆ</sup> = 19 _._ 51. The standard deviation of all pitcher abilities is 0.012. So if the pitcher’s ability measure is increased by one standard deviation, one predicts a team’s log odds of scoring runs to increase by 19 _._ 51 × 0 _._ 012 = 0 _._ 23. 

By fitting the multilevel ordinal regression model, we learn about the pitcher effects for all 30 teams. Figure 6 displays individual (team) effects by black bars and the multilevel model estimates are displayed by red bars. The individual estimates show substantial variation. For example, Seattle’s regression coefficient is _β_<sup>ˆ</sup> _j_ = 9 _._ 84 and Philadelphia’s coefficient is _β_<sup>ˆ</sup> _j_ = 28 _._ 24, indicating that the Phillies were much more able to take advantage of poor pitching than Seattle in the 2013 season. The multilevel estimates in this case shrink the individual estimates about 76% towards the average value. Seattle and Philadelphia’s pitcher effects, under the multilevel model, are corrected to 16.85 and 21.05, respectively. These multilevel estimates are better reflections of the true team pitcher effects than the individual team estimates, and would lead to better predictions of run-scoring against pitchers of different abilities. 

### _4.4. Advancing baserunners home (clutch effects)_ 

Run scoring generally is viewed as a two-step process. A team places runners on bases and then these runners are advanced to home. There is a special focus in the media on advancing runners who are in scoring position (on second and third base). One commonly hears about the number of runners left on base and the proportionofrunnersinscoringpositionwhoscore.Do teams really differ in their abilities to advance runners from scoring position? 

To address this clutch hitting question, an ordinal regression model is constructed. For each half-inning, one records the total number of (unique) runners _SP_ who are in scoring position (either on second or third base) and the number of these runners _R_ who eventually score. (Note that _R_ can be smaller than the number of runs that score in the half-inning since runners who score don’t need to be in scoring position.) As before, we classify _R_ into the categories 0, 1, 2, 3, and “4 or more”, and consider the ordinal regression model 



where _θc_ is the probability that _R_ is at least _c_ . This model is to data for all teams. One obtains 

_J. Albert / Beyond runs expectancy_ 

14 

## Pitcher Effects 



<!-- Start of picture text -->
WAS<br>TOR<br>TEX<br>TBA<br>SLN<br>SFN<br>SEA<br>SDN<br>PIT<br>PHI<br>OAK<br>NYN<br>NYA<br>MIN<br>MIL<br>MIA<br>LAN<br>KCA<br>HOU<br>DET<br>COL<br>CLE<br>CIN<br>CHN<br>CHA<br>BOS<br>BAL<br>ATL<br>ARI<br>ANA<br>10 20 30<br>Estimate<br>Team<br><!-- End of picture text -->

Fig. 6. Individual and multilevel pitcher effects for all teams. The black line represents the individual estimate plus and minus the standard error and the red line represents the multilevel estimate plus and minus the standard error. 

the estimate _β_<sup>ˆ</sup> = 2 _._ 395 which indicates that for each additional runner in scoring position, the log odds of scoring runs is increased by 2.395. 

To see how this clutch hitting statistic varies between teams, this ordinal regression model was fit separately for all teams. Anaheim and the New York Mets had the smallest and largest regression estimates of _β_<sup>ˆ</sup> _j_ = 2 _._ 19 and _β_<sup>ˆ</sup> _j_ = 2 _._ 60, respectively. This indicates that the Mets were the best team in baseball in 2013 from a clutch-hitting perspective and Anaheim was the worst. However, when we use the multilevel model to simultaneously estimate the true clutch regression coefficients for all teams, we learn that this observed variability in clutch measures is primarily due to chance. Figure 7 displays the individual and multilevel clutch estimates for all teams. Here the shrinkage is about 93% and we see that the individual clutch estimates are shrunk almost entirely towards the common value in the multilevel model fit. The interpretation is that although teams obviously have different abilities to score runs, 

teams appear to have similar abilities to advance runners in scoring position. 

### **5. Multiple regression approach** 

### _5.1. Introduction_ 

In our exploration of the effects of covariates on run-scoring, we focused on the application of an ordinal regression model with a single covariate. This was done since it is simpler to describe the covariate effects and the shrinkage behavior of the multilevel model. A natural extension of this approach is to model runscoring of all teams by a large ordinal regression model where one includes all covariates that one believes have an impact on run scoring. Using our general notation, one can write the ordinal logistic model as 



15 

_J. Albert / Beyond runs expectancy_ 



<!-- Start of picture text -->
Clutch Effects<br>WAS<br>TOR<br>TEX<br>TBA<br>SLN<br>SFN<br>SEA<br>SDN<br>PIT<br>PHI<br>OAK<br>NYN<br>NYA<br>MIN<br>MIL<br>MIA<br>LAN<br>KCA<br>HOU<br>DET<br>COL<br>CLE<br>CIN<br>CHN<br>CHA<br>BOS<br>BAL<br>ATL<br>ARI<br>ANA<br>2.2 2.4 2.6<br>Estimate<br>Team<br><!-- End of picture text -->

Fig. 7. Individual and multilevel clutch effects for all teams. The black line represents the individual estimate plus and minus the standard error and the red line represents the multilevel estimate plus and minus the standard error. 

where _θc_<sup>_j_represents the probability of scoring at least</sup> _c_ runs for the _j_ th team, _x_ 1 _, .., xk_ represent _k_ possible covariates (such as league, ballpark, and pitcher quality), and _βj_ 1 _, ..., βjk_ represent the regression effects for the _j_ th team. In the multilevel modeling framework, one could assign _γc_<sup>1</sup><sup>_, ..., γ_</sup> _c_<sup>_N_</sup> a common multivariate normal distribution, and likewise assume each of the sets of team covariate effects _{βjk, j_ = 1 _, ..., N}_ come from a common normal distribution. This model is more complicated to fit due to the large number of unknownparameters,butitwouldaccomplishthesame smoothing effect as demonstrated in this paper. Team scoring distributions would be shrunk towards an overall scoring distribution – this is accomplished by the commonmultivariatenormaldistributionplayedonthe bin cutpoint parameters _γc_<sup>_j_. In a similar fashion, team</sup> effects for a particular covariate such as pitcher quality would be shrunk or moved towards a common covariate effect. This particular approach is promising and can help us better understand relevant covariates that affect run scoring. 

### _5.2. Example_ 

To illustrate this multiple regression approach, suppose we are interested in learning about the home and inning effects on team run scoring. For the _j_ th team, we write the ordinal regression model as 



This model was fit on the 2013 season data. One can represent an estimate of the pair ( _βj_ 1 _, βj_ 2) by an ellipse that contains the unknown pair of parameters with95%probability.Figure8displaystheestimatesof the home and inning effects where one uses individual 

16 

_J. Albert / Beyond runs expectancy_ 



Fig. 8. Individual team estimates of home/away and early/late inning effects from ordinal multivariate regression model for 2013 season. Each ellipse represents the location of a 95% confidence region and the region corresponding to Colorado is labelled. 



Fig.9. Multilevelordinalregresssionmodelestimatesofhome/away and early/late inning effects for 2013 season. Each ellipse represents thelocationofa95% confidence region and the region corresponding to Colorado is labelled. 

regression models for the 30 teams, and Fig. 9 displays estimates of the same effects using the multilevel regression model. Note that there are general tendencies for teams to score more at home and in early innings (the ellipses tend to be located in the upperright section of the graph), but the locations of the ellipses for the multilevel model estimates tend to be shrunk towards a common estimate. 

### **6. What covariates are relevant to run-scoring?** 

The ordinal regression approach seems advantageous to the expected runs approach for understanding team run-scoring, and we have illustrated the use of several covariates such as home/away, pitcher quality, and ability to advance runners in scoring position. But there needs to be a more careful look at all of the team attributes that affect run-scoring. One believes that this modeling approach can be extended to handle many other covariates. 

**Home/away affect.** The home-away run-scoring effects documented actually have several dimensions. A team scores more in their ball park partly due to physical and weather attributes of their ballpark, but there is evidence to suggest that umpires may favor the home team in the calling of balls and strikes. How much of the home/away effect is due to each factor? 

**Individual batter effects.** This paper has focused on run-scoring of teams. But a team’s batting lineup consists of players who aid run-scoring by their ability to get on-base and other players contribute by advancing runners home by extra-base hits. One typically evaluates the contribution of individual hitters by run value, but these run value calculations are based on league averages. One would speculate that one could get better evaluations of hitter runs contributed by using run distributions individualized for the player’s team. 

**Base-running effects.** As documented in the recent World Series between the Royals and the Giants, runs are often scored by good runner advancement. Several of the runs were set up by a runner on second base who advanced to third on a sacrifice fly. Teams clearly differ with respect to their ability to steal and take the extra base, and one would be interested in measuring the effect of base-running on run scoring for all teams. 

**Situational effects.** Runs are scored within a context of the opposing pitcher and defense, and the inning. The measurement of pitcher quality used here is actually a measurement of picher quality and team defense. How can one isolate the effect of these two effects in run scoring? There is a recent movement to shifting the infielders for specific hitters – what is the value of this shift from the viewpoint of runs? During different innings, teams may have different goals towards runscoring. In close games, the objective might be to score a single run. In other situations, the goal might be to 

_J. Albert / Beyond runs expectancy_ 

17 

score multiple runs. Do teams differ with their ability to score a single run? 

### **7. Summary and concluding comments** 

Efron, B., Morris, C., 1975. Data analysis using Stein’s estimator and its generalizations. Journal of the American Statistical Association. 70(350), 311–319. 

Good, I.J., 1967. A Bayesian significance test for multinomial distributions. Journal of the Royal Statistical Society. Series B, pp. 399–431. 

Johnson, V., Albert, J., 1999. Ordinal Data Modeling, Springer. 

The primary objective of this work is to provide a better understanding of the run-scoring patterns in Major League Baseball. Instead of focusing on the mean number of runs scored in a half-inning, we focus on the probability distribution of runs scored. We are interested in how this run-scoring distribution varies among teams and the effect of various covariates such as the ballpark, pitcher/defense, and “runners in scoring position” situations. 

The primary method is ordinal regression of the multinomial run-scoring outcome and the use of multilevel modeling to estimate run-scoring over different groups. One finding is that there are some covariates such as ballpark where there are clear team-specific run-scoring advantages. This is not surprising since it is well-known that Coors Field (home of Colorado Rockies) is very advantagous for run-scoring and other parks such as Citi Field (home of the New York Mets) are more restrictive for scoring runs. But there are other covariates such as advancing runners in scoring position where there are little differences between teams in scoring runs. It should be clarified that we do observe differences in teams’ advancing runners in scoring position, but there is little evidence to suggest that teams have different clutch-hitting abilities. If the media understands this conclusion, then there would be less discussion about teams’ batting performances when runners are in scoring position. The goal of future work to find suitable covariates such as the ones suggested in Section 5.2 that have a significanat impact on run-scoring, and the knowledge of these covariates would be helpful for teams building an offense. 

### **References** 

> Albert, J., 2004. A batting average: Does it represent ability or luck? Technical Report. 

- Albert, J., 2006. Pitching statistics, talent and luck, and the best strikeout seasons of all-time. Journal of Quantitative Analysis in Sports. 2(1), 2. 

Albert, J., 2009. Is Roger Clemens’ WHIP trajectory unusual? Chance. 22(2), 8–20. 

Albert, J., Bennett, J., 2003. Curve Ball, Springer. 

Keri, J., Baseball Baseball Prospectus, 2007. Baseball Between the Numbers: Why Everything You Know About the Game is Wrong,’ Basic Books. 

Lindsey, G., 1963. An investigation of strategies in baseball. Operations Research. 11(4), 477–501. 

McCullagh, P., 1980. Regression models for ordinal data. Journal of the Royal Statistical Society, Series B. 42(2), 109–142. 

Morris, C., 1983. Parametric empirical Bayes inference: Theory and applications. Journal of the American Statistical Association. 78(381), 47–55. 

Rosner, B., Mosteller, F., Youtz, C., 1996. Modeling pitcher performance and the distribution of runs per inning in major league baseball. The American Statistician. 50(4), 352–360. 

Simonoff, J., 1995. Smoothing categorical data. Journal of Statistical Planning and Inference. 47(1), 41–69. 

Tango, T., Lichtman, M., Dolphin, A., 2007. The Book: Playing the Percent-ages in Baseball, Potomac Books, Inc. 

Thorn, J., Palmer, P., Reuther, D., 1984. The Hidden Game of Baseball: A Revolutionary Approach to Baseball and Its Statistics,’ Doubleday Garden City, New York. 

Wollner, K., 2000, An analytic model for per-inning scoring distributions, Baseball Prospectus. 

### **Appendix: Estimating collections of multinomial data using an exchangeable model** 

In Section 2.2, one observes _W_<sup>1</sup> _, ..., W_<sup>30</sup> , vectors of runs scored for the 30 teams and one assumes that _W_<sup>_j_</sup> = ( _W_ 1<sup>_j, ..., W_</sup> 5<sup>_j_), the number of runs scored in the</sup> bins 0, 1, 2, 3, and 4 or more is multinomial with probability vector _p_<sup>_j_</sup> = ( _p_<sup>_j_</sup> 1<sup>_, ..., pj_</sup> 5<sup>).Underthemultilevel</sup> exchangeable model, we assume that _p_<sup>1</sup> _, ..., p_<sup>30</sup> represent a random sample from a Dirichlet distribution of the form 



where 



is the Dirichlet function and _�_ () is the gamma function. The model is completed by assigning the mean vector 

_J. Albert / Beyond runs expectancy_ 

18 

_η_ = ( _η_ 1 _, ..., η_ 5) and the “precision” parameter _K_ priors – we assume that one has little information about these parameters and that leads to the prior density of the form 



One estimates the precision parameter _K_ from its marginal posterior distribution. One can show that the posterior density of ( _K, η_ ) has the form 



One estimates ( _K, η_ ) by the posterior mode, that is, the value ( _K,_<sup>ˆ</sup> ˆ _η_ ) that maximizes the marginal posterior density _g_ ( _K, η_ |data). These estimates are used in computing the multilevel estimate at the probability vector of team _j_ given in Section 2.2 as 



The multilevel estimate _p_ ˆ<sup>_j_</sup> _ML_<sup>is a compromise between</sup> ˆ the individual team estimate _p_<sup>_j_</sup> = _W_<sup>_j_</sup> _/N_<sup>_j_</sup> and the combined estimate _η_ ˆ ≈<sup>�</sup> _W_<sup>_j_</sup> _/_<sup>�</sup> _N_<sup>_j_</sup> . 


