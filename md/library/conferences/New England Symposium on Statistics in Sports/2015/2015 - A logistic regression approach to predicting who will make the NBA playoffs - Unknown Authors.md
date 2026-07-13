<!-- source: library/conferences/New England Symposium on Statistics in Sports/2015/2015 - A logistic regression approach to predicting who will make the NBA playoffs - Unknown Authors.pdf -->

A Logistic Regression Approach to Predicting Who Will Make the NBA Playoffs Ryan Elmore, Department of Business Information and Analytics, Daniels School of Business In 2015, Research Starts with a Tweet… Modelling and Simulation Overview Conclusions Let’s be honest, we knew that the Nuggets were not _<u>p</u>_ = Question : _X · · · X_ going to make the playoffs without this analysis! : What is the probability Regression Model log _β_ 0 + + _β_ 1 1 + + + _β_ 5 5 1 _−_ ✓ _p_ ◆ that the Denver Nuggets will of _p_ = probability making playo↵s From Section 4.10 of Severini (2015): make the playoffs given their _X_ = indicator of 1 prior year playo↵s ✔ record at 35 games? … concepts such as the margin of error are still useful for - _X_ = wins losses 2 ✔ understanding the role of randomness in sports statistics. However, such concepts should be viewed as guidelines _X_ 3 = average point di↵erential ✔ rather than as strict results. Why is this important? From nba.com (last year)… _X_ = number of ❌ 4 away games _X_ = number of back-to-back ❌ 5 games The methodology is generalizable to any number of games. But, is this better than just looking at the standings? Yes and no. No, the records at various dates tell a similar story. Yes, because we incorporate some notion of Data uncertainty into the predictions. 



<!-- Start of picture text -->
=<br>:  X  · · · X<br>log  β 0 + +  β 1 1 + +  +  β 5 5<br>1  −<br>p<br>of<br>p  = probability making playo↵s<br>X = indicator of<br>1 prior year playo↵s<br>-<br>X = wins losses<br>2<br>X di↵erential<br>3 = average point<br>X = number of<br>4 away games<br>X = number of back-to-back<br>5 games<br><!-- End of picture text -->





Data Dependent variable: playoffs or not Independent variables: record, cumulative point differential, strength of schedule (away games, back to back games), organizational stability (prior-year success) Collaboration Opportunities? If you’re interested in working on this type of project, contact me at Ryan.Elmore@du.edu or @rtelmore, and check out the code repository at https://github.com/rtelmore/Nuggets. 

Future Work 

GAM: Fit a general additive model to the logit, _i.e._ _<u>p</u>_ = log _s_ 1( _X_ 1) + _· · ·_ + _s_ 5( _X_ 5) 1 _−_ ✓ _p_ ◆ 



where _s i_ are nonparametric, smooth functions. Free Agency: Incorporate off-season movement into the prediction equations, _e.g._ use team salary information as a proxy. Acknowledgements The author would like to thank Tommy Balcetis, Manager of Basketball Analytics for the Denver Nuggets, for his contributions to this work. 




