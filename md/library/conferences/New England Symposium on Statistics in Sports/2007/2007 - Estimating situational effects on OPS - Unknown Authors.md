<!-- source: library/conferences/New England Symposium on Statistics in Sports/2007/2007 - Estimating situational effects on OPS - Unknown Authors.pdf -->

# **Using Gibbs sampling to estimate the situational effects on OPS** 

## **Philip Yates** 

Department of Mathematics & Statistics, Cal Poly Pomona, Pomona, California  91768 

### **Introduction** 

### **Results** 

How can a baseball fan figure out the significance difference of situational OPS?  One way is to look at a player’s three or five year performance for a given situation.  This three to five year span can account for any real situational effect and control for any single season variability in situational splits that might be due to a player having an injury-plagued or a career season. 

Gibbs sampling was performed on each player that qualified for the batting title in 2006 to find the effect on OBP and SLG on seven different situations: ahead in the count vs. two strikes; opposite side vs. same side; home vs. away; runners in scoring position vs. no one on base; pre-All-Star game vs. post-All-Star game; day vs. night; groundball pitcher vs. flyball pitcher. 

Albert (1994) discussed the inherent problems with interpreting the significance of seasonal batting averages.  These problems can be extended to both on base percentages, slugging percentages, and OPS. The problem is whether or not a particular player’s situational effect on OPS can be accurately estimated from one season. 

A burn-in period of 10,000 iterations was used for each metric and situation to approach its stationary distribution.  Another 10,000 simulated values were generated to estimate the parameters.  This entire simulated sample can be thought of as a sample from the parameter’s posterior distribution. 

When estimating the true situational effects on OPS, improvements in the estimates can be obtained by shrinking the parameters to some common value.  James (1986) refers to this as a “regression to the mean” when he looked at team breakdown statistics. 

In order to get the difference in OBP for a player, one can compute _pi1-pi2_ by _exp(μi+αi)/(1+exp(μi+αi))-exp(μi-αi)/(1+exp(μi-αi))_ .  The difference in SLG is computed by _exp(μi+αi)-exp(μi-αi)_ .  For each player, these transformations are summed to compute the situation effect on OPS. 



### **Methods** 

Data was collected on the 157 players who qualified for the batting title during the 2006 season.  To qualify for the batting title, a player needs at least 502 plate appearances.  The data were found at www.baseball-reference.com. 

**Figure 3.** Boxplots of the posterior means of the differences in OPS for the seven situational variables.  The situations are abbreviated in the following manner: ahead in the count vs. two strikes (A-2S); opposite side vs. same side (O-S); home vs. away (H-A); scoring position vs. no one on (S-N); preAll-Star game vs. post-All-Star game (PR-PS); day vs. night (D-N); groundball pitcher vs. flyball pitcher (GB-FB). 

The metric of interest, OPS, is a player’s on-base percentage (OBP) plus a player’s slugging percentage (SLG). **Figure 1** shows how to compute these two metrics. 

To set up the model for the effects on OBP, a model similar to Albert’s (1994) for batting average can be used.  The observed values are the logit transformation of the ratio of times reaching base over times not reaching base.  To model the effects on SLG, the observed values are the log transformation of the SLG. 



<!-- Start of picture text -->
Situation E(μ α ) OBP E(σ α ) E(μ α ) SLG E(σ α ) Summary statistics of [E(pQ 1 Munit = .001)Q 3 i1 -p i2 )] (oneQ 3 -Q 1<br>GBALL-FBALL 0.009 0.125 -0.022 0.123 -80 -17 48 128<br>DAY-NIGHTPRE/AS-POST/AS 0.0010.003 0.1210.122 -0.0030.002 0.1170.114 -60-48 -32 5463 114111<br>SCORING-NONE ONHOME-AWAYOPP-SAMEAHEAD-2 STRIKES 0.4580.0350.0780.071 0.1390.1290.1240.118 0.0010.0520.3020.024 0.1250.1270.1310.115 404-30-1123 477338136 5811519687 17712612898<br><!-- End of picture text -->

**Figure 2a** and **Figure 2b** show the models and priors used to run WinBUGS 1.4.1 for each component of OPS. 



<!-- Start of picture text -->
OBP = ABH + BB + BB + HBP + HBP + SF Table 1.  summary statistics of the posterior means of the OPS differencesPosterior means of the parameters of the situation effects and pi1-pi2<br>SLG = 1B + ( 2 × 2B ) + ( AB3 × 3B ) + ( 4 × HR ) Figure 1. batter reaches base for any reason other  OBP measures how often a  across all players.<br>(a) ob ij ~ dbin ( p ij , pa ij ), j = 1 , 2 than a fielding error, fielder’s choice, fielder’s obstruction, or catcher’s<br>μ ln i ⎛⎜ ⎜ ⎝ ~ 1 − dnormp ijp ij ⎞⎟ ⎟ ⎠ = ( 0 μ . 0i , + 0 . α 000001ij , α i 1 = ) α i , α i 2 = −α i interference; SLG measures the average number of bases per at bat. Figure 3  mentioned transformations on the simulated values of {and  Table 1  show the results of applying the previously  μi } and { αi }.<br>α i ~ dt ( μα , τ , 4 ) Figure 3  plots the boxplots of the differences in OPS for the eight<br>τμ (b) tb α ij ~ ~~ dgammadnormdpois ( λ (( 0ij0 .),. 05 ,, 0j0 . = . 00000151 ) , 2 ) situations.  median, quartiles, and interquartile range for the situational effect on OPS. σα  that describe the population of the situational effects.  It also gives the  Table 1  gives the posterior means of the parameters of  μα  and<br>αμλ log ijii ~~ =(μ dtdnorm μ ij ij ) ( μ=× α ab μ , τ i ( ij0 + , 4 . α 0 ), ij0 ,. 000001 α i 1 = α i ), α i 2 = −α i WinBUGS 1.4.1 to find the situational effect on OBP for the i Figure 2 .  (a)  th The model and priors used in player.  (b)  The model and  The one situation that stands out the most is a player being ahead in the count versus having two strikes.  The median difference in OPS is 477<br>τμα ~ ~ dgammadnorm (( 00 .. 05 ,, 00 .. 0000015 ) ) priors used in WinBUGS 1.4.1 to find the situational effect on SLG for the i th player. points.  The next most important situation is when a player is facing a pitcher throwing with the opposite arm versus the same arm.  The median<br>difference in OPS in this situation is 81 points.<br><!-- End of picture text -->

Another result to note in **Table 1** concerns the posterior means of scale and for SLG are on the log scale, they still provide some _μα_ and _σα_ .  Even though the results for OBP are on the logit indication about the significance of each situation and the variability for each situation.  Again, pitch counts and opposite versus same arm seem to be the most important comparisons.  All of the situations have about the same spread except for the pitch counts. 

**Figure 4** illustrates the shrinking of the 2006 season effects to the posterior means with the line _y=x_ plotted on top of the graph. This “regressing to the mean” was what James (1986) was referring to when discussing team breakdown statistics.  The goal here was to shrink the season effects of OPS to a common value. 



**Figure 4.** Posterior means of the differences in OPS plotted against the 2006 seasonal differences in OPS for each of the seven situations. 



<!-- Start of picture text -->
Season Estimate<br>Player Situation OPS 1 OPS 2 difference of p 1 -p 2<br>Eric Chavez ahead-2 strikes 1.482 0.463 1.019 0.893<br>Adam Dunn ahead-2 strikes 1.517 0.759 0.758 0.890<br>Jeff Francouer ahead-2 strikes 1.353 0.378 0.975 0.863<br>Manny RamirezTodd Walker ahead-2 strikesahead-2 strikes 0.8281.694 0.8240.759 0.0040.935 0.1120.854<br>Jim Thome opposite-same 1.203 0.715 0.488 0.431<br>Craig BiggioMatt HollidayVernon WellsCraig MonroeCarlos Beltran home-awayhome-awayhome-awayhome-awayhome-away 0.6780.8550.8681.0381.132 0.8971.0890.7620.5410.818 -0.219-0.2340.2760.3270.314 -0.160-0.1780.2390.2580.264<br>Nomar GarciaparraRafael FurcalRichie SexsonRyan Howard pre/AS-post/ASpre/AS-post/ASpre/AS-post/ASpre/AS-post/AS 0.9231.0040.6910.706 1.2600.6940.9631.012 -0.337-0.272-0.3060.310 -0.280-0.227-0.2470.237<br>Jason Giambi day-night 1.294 0.827 0.467 0.376<br><!-- End of picture text -->

found in Table 1. **Table 2.** Outlying situational players based on _Q3+1.5 IQR_ and _Q1-1.5 IQR_ 

**Table 2** lists any player who could be identified as an outlying situational player based on their large or small differences in OPS compared to all other differences in OPS for a given situation.  What stands out the most are the “outliers” for the most significant variables, whether or not a player is ahead in the count or has two strikes.  The players with the largest differences are known for being players prone to striking out a lot over the course of a season.  The smallest difference is a player known for being more of a contact hitter. 

### **Conclusions** 

Looking back at the results, the two situations that stand out are whether or not a player is ahead in the count versus having two strikes (median effect 477 OPS points) and a batter facing a pitcher with opposite throwing arm versus the same throwing arm (median effect 81 OPS points).  Both of these situations can be argued to be more due to “ability effect” rather than a “bias,” a variable that has the same effect on all players.  These two variables were the most significant in Albert’s (1994) paper when dealing with batting average (median effect with pitch count: 123 points; median effect with opposite versus the same: 20 points). 

One reason behind using OPS to measure a player’s offensive value is that it is easier than more complex metrics used by sabermetricians. OPS is simply the OBP plus the SLG.  Unfortunately, just because it is one of the more easily accessible metrics does not mean it is the best one to use in order to measure a player’s offensive value.  Kahrl (2004) among others point out the need for OPS to be adjusted to control for ball park effects and overall league effects, such as the differences between the two leagues. 

### **Literature cited** 

Albert, J. 1994. Exploring Baseball Hitting Data: What About Those Breakdown Statistics? _Journal of the American Statistical Association_ 89:1066-1074. Baseball-Reference.com. <www.baseball-reference.com>. Accessed 2007 July 16 – August 18. James, B. 1986. _The Bill James Baseball Abstract_ . New York: Ballatine. Kahrl, C. 2004. Baseball Prospectus Basics: OPS. <http://www.baseballprospectus.com/article.php?articleid=2640>. Accessed 2007 March 28. 

### **Acknowledgments** 

Thanks to Webster West and his statistical computing course that he taught while still at the University of South Carolina.  That course is where I first came across Jim Albert’s paper that was that inspired me to pursue this project.  Thanks to David Rockoff for helping me think of ways to apply my love of baseball in a more academic manner.  Thanks to John Grego for his advice and guidance with this project. 

### **For further information** 

Please contact _payates@csupomona.edu_ .  More information on this and related projects can be obtained at _www.csupomona.edu/~math._ A link to an online, PDFversion of this poster can be found at _www.csupomona.edu/~payates_ . 




