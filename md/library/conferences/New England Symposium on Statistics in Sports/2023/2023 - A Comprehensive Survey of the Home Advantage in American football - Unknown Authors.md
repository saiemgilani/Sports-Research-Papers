<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - A Comprehensive Survey of the Home Advantage in American football - Unknown Authors.pdf -->

**A Comprehensive Survey of the Home Advantage in American Football** Bliss<sup>1</sup> Luke Benz<sup>2</sup> and Michael<sup>1</sup> , , Thompson Lopez 1 National Football League 2 Harvard T.H. Chan School of Public Health, Department of Biostatistics 







# **Conclusions** 

**Introduction** The existence and justification to the home advantage (HA)—the benefit a sports team receives when at home—has been studied across playing sport. Most research on this topic is restricted to individual leagues in short time frames, which limits a thorough understanding of the drivers of home advantage and prevents extrapolation. Using nearly two decades of data from the National Football League (NFL), the National Collegiate Athletic Association (NCAA), and high schools from across the United States, we provide a framework for estimating home advantage. **In particular, we are interested in the question of whether/how much home advantage has changed over time** . **Statistical Framework** Our statistical framework leverages STAN to fit a suite of Bayesian linear regression based pairedcomparison models, with various plausible temporal trends for home advantage: a constant home advanover a linear home trend over tage time, advantage time, and a trend in which home advantage is allowed to over time. vary freely **Priors:** _θ_ Team _i ∼_ Normal(0 _, σθ_<sup>2)</sup> Strength _∼ σ_ Team Variance _θ_ InverseGamma(1 _,_ 1) Strength _α ∼_ Normal(0 _, σα_<sup>2)</sup> Home Advantage _σ_ Home Variance _α ∼_ InverseGamma(1 _,_ 1) Advantage _σ ∼_ Score Variance InverseGamma(1 _,_ 1) Differential **Models** : Let _Y_ denote the score differential of a game where _ijt_ team _i_ plays at team _j_ in year _t Y N θ θ_ **Constant HA** _ijt ∼_ ( _i − j_ + _α, σ_<sup>2</sup> ) (1) _Yijt ∼ N_ ( _θi − θj_ + _α_ 0 + _α_ 1 _t, , σ_<sup>2</sup> ) **Linear HA** (2) _Yijt ∼ N_ ( _θi − θj_ + _αt, σ_<sup>2</sup> ) **Time-Varying HA** (3) 

# **Results** 











Across 50 high school states, 4 NCAA divisions, and the NFL, a constant home advantage trend was preferred in the majority of states. 95% posterior credible intervals for _α_ 1, the linear home advantage trend in Model (2), do not contain 0 in only 7/55. Similar results are obtained when formally comparing models on the basis of expected log pointwise predictive density (ELPD) estimated via the leave-oneout cross-validation (LOO) approach of Gelman and colleagues [1]. Interestingly, FBS exhibits the largest estimated decline in HA, with a drop of roughly 0.11 points/year between 2004-2022. If anything, HA has declined more in NCAA/NFL over the past 2 decades than in where in HA are far more high school, changes heterogeneous. An intuitive but perhaps underappreciated point is the importance of properly adjusting for team when home In strength estimating advantage. professional leagues such as the NFL, better teams host playoff games, and so even with more balanced schedules, one would expect model based estimates of HA to be attenuated compared to empirical observations. In lower levels of football, including college and high school, better teams are both more likely to host more home games (perhaps due to better facilities and larger athletic budgets) and win by larger amounts. As evidenced in Figure 2, failure to properly account for confounding by team strength would lead one to not only produce estimates of HA that are severely biased, but also overstate the extent to which strong temporal HA trends exist (e.g. Tennessee). **References** [1] Aki Vehtari, Andrew Gelman, and Jonah Gabry. Practical bayesian model evaluation using leave-one-out cross-validation and waic. _Statistical_ 2017. _Computing_ , 27(6):1413–1432, 



1: Posterior distributions for _α_ the of the linear Figure 1, slope trend for HA in Model (2), which denotes the change in home _α_ advantage in points/year. Negative values of 1 denote a decline in HA while values of _α_ denote an increase in HA. positive 1 

2: of HA mean estimates for se- Figure Comparison posterior lect state/league between 2004-2022 from each of the 3 mod- els. Also included on the is the mean plot (HOME AWAY) score for each In the vast differential league-season. majority of leagues, this "observed" home advantage is much larger than than any model based estimate, suggesting failure to account for team lead to incorrect conclusions. strength may 




