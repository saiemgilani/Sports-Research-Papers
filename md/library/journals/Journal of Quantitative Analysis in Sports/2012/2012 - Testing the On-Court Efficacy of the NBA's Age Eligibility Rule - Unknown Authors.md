<!-- source: library/journals/Journal of Quantitative Analysis in Sports/2012/2012 - Testing the On-Court Efficacy of the NBA's Age Eligibility Rule - Unknown Authors.pdf -->

# _Journal of Quantitative Analysis in Sports_ 

Manuscript 1426 

## Testing the On-Court Efficacy of the NBA's Age Eligibility Rule 

**Ryan Rodenberg,** _Florida State University_ **Jun Woo Kim,** _Florida State University_ 

©2012 American Statistical Association. All rights reserved. 

## Testing the On-Court Efficacy of the NBA's Age Eligibility Rule 

Ryan Rodenberg and Jun Woo Kim 

#### **Abstract** 

The NBA’s age eligibility rule is controversial. To examine the on-court efficacy of the NBA’s age eligibility rule, we test the effect of age of entry on NBA career performance. Our data set comprises the 332 players selected in the first round of the NBA draft from 1989 to 2000. Using censored normal regression models, we found that players drafted at a relatively younger age have more successful NBA careers across three different metrics. To explore a beneficial effect of one year in college, group selection bias tests were conducted by comparing differences in career success between “one and done” players and players who entered the NBA straight out of high school. The results were consistent with our main analyses – players who moved into the NBA directly from high school generally perform better than players with a single year of college experience. We find no systematic evidence in support of the on-court efficacy of the NBA’s age eligibility rule. 

**KEYWORDS:** NBA, age eligibility rules, censored normal regression 

**Author Notes:** The authors would like to thank the editor, two anonymous referees, and conference participants at the 2011 New England Symposium on Statistics in Sports for helpful comments. 

Rodenberg and Kim: NBA Age Rule 

### **Introduction** 

In 1999, National Basketball Association (NBA) commissioner David Stern posited: “We feel we have the right to set an age limit” (Popper, 1999).  Six years later, as part of negotiations in furtherance of a new collective bargaining agreement (CBA) between the NBA and its players, a collective group represented by the National Basketball Players Association (NBPA), the league and union bilaterally agreed on a minimum age rule requiring American players to be one year removed from high school and at least 19 years of age by December 31 of the draft year in order to be eligible for that year’s draft.<sup>1</sup> One month before agreeing to the minimum age rule, NBPA executive director Billy Hunter opined: “I’m still strongly philosophically opposed to [a minimum age rule] and I can’t understand why people think one is needed” (Sheridan, 2005). 

Since being adopted in 2005, the NBA’s age eligibility rule has proven to be contentious.  U.S. Secretary of Education Arne Duncan called the NBA age rule and its impact on “one and done” players in college basketball a “farce” and “intellectually dishonest” (Jackson, 2010).  Steve Cohen, a U.S. Representative from Tennessee described the rule as “a vestige of slavery” (Thamel, 2009). Jones (2005), Rossen (2008), Shaffer (2008), and Litman (2010) have all criticized the NBA minimum age rule from a legal perspective.  With ample ethical and legal controversy swirling, this article aims to analyze the on-court efficacy of the NBA’s age eligibility rule.<sup>2</sup> Our use of the phrase “on-court” is deliberate and specific, as the aim here is to focus solely on the metrics pertaining to basketball performance during competition, not (important) off-court issues such as the value of higher education, purported socially irresponsible behavior or criminal activity, and the pecuniary aspects of being a professional athlete. 

In addition to being controversial, analyzing the efficacy of the NBA’s age-based eligibility rule is an empirical challenge.  The ideal experiment would be one where randomization resulted in a treatment group required to comply with the rule and a control group that had no such mandate.  Subsequent player performance could then be compared across the two random samples and the impact of the rule could be evaluated.  For a number of overriding legal, ethical, and logistical reasons, such an experimental ideal is impossible.  Nevertheless, the nature of rule-making in sports leagues has given rise to a number of “interesting natural experiments that offer opportunities for analysis” (Kahn, 2000, p. 75). Consistent with the general observations of Rosen and Sanderson (2001) regarding sports labor market research, the availability of objective on-court 

> 1 Non-American players are not required to be at least one year removed from high school. 

> 2 The more generalized topic of the interplay between precocity and labor market outcomes in professional basketball was addressed by Rodenberg and Kim (2011). 

1 

_Submission to Journal of Quantitative Analysis in Sports_ 

performance measures at the individual player level further lends itself to the quantitative evaluation of the NBA’s age eligibility rule. 

Emerging research has pointedly considered the interaction between precocity and performance in sports.  Sowell and Mounts (2005) concluded that such interaction is “one of the most basic in all of economics…[i]t is at the foundation of all acts of production or utility creation.”  Several studies have looked at aging and peak performance in sports (Schulz and Curnow, 1988; Bradbury, 2009; Fried and Tauer, 2011).  Specific to the NBA, playing careers have been analyzed vis-à-vis opportunity costs (McCann, 2004), draft order (Staw and Hoang, 1995), college performance (Coates and Oguntimein, 2010; Berri, Brook, and Fenn, 2011), possible exit discrimination (Groothuis and Hill, 2004), internationalization (Eschker, Perez, and Siegler, 2004), and the confluence of unraveling, human capital, and option value (Groothuis, Hill, and Perri, 2007). 

The effect of minimum age rules has been investigated outside of sports on a number of occasions.  Most recently, Miron and Tetelbaum (2009) evaluated the interaction between traffic fatalities involving underage drivers and an increase in the minimum age required to drink alcohol legally.  Rodenberg and Stone (2011) is the most closely related sport-specific paper, which analyzed female professional tennis player career outcomes before and after a minimum age rule was adopted by the governing body of women’s professional tennis in 1995 and found such rule to have a largely null effect.  This paper adds to the literature by measuring the impact of age of entry on career-level performance and, in turn, tests the on-court efficacy of the NBA’s age eligibility rule. 

### **Methodology** 

#### **Data** 

As specifically listed in Appendix A, the sample includes all players selected in the first round of the NBA draft from 1989 to 2000.  The NBA’s reverse-order draft is held annually and currently includes two rounds.<sup>3</sup> Barring draft pick trades or other transactions involving draft picks, teams have one pick in each round.  There are presently 30 NBA teams, meaning there are 60 draft slots total. We restricted our sample to the first round of NBA draft during the twelve year period from 1989 to 2000 for three reasons.  First, detailed career performance statistics and comprehensive biographical information is unavailable for (often obscure) players selected in the second round.  Second, previous NBA-NBPA CBAs were structured in such a way that the contracts for second round draft 

> 3 See Zola (2012) for a detailed analysis of the NBA draft and the movement of players from college basketball to professional basketball in the NBA. 

2 

Rodenberg and Kim: NBA Age Rule 

selections, if the player and team even agreed upon terms, were not guaranteed for their duration in the same way that all contracts for first round draft picks were.<sup>4</sup> Accordingly, a non- _de minimus_ number of second round draft picks never played in the NBA, opting to instead play overseas where the underlying team contracts had more certainty.  Third, as described in detail below, the twelve year period with 1995 as a mid-point was important to our research design given that 1995 was the year that players began entering the draft straight out of high school after a 20 year gap that saw no American players attempt to move directly to the NBA without at least one year of college playing experience.<sup>5</sup> 

Data were collected from publicly available resources.  NBA.com and Basketball-Reference.com are two examples.  Both websites include detailed performance statistics for every player in our data set from the time such player was drafted until 2011.  Our regression equation was estimated with the following player-specific independent variables – age of NBA entry ( _AGE_ ),<sup>6</sup> height ( _HT_ ),<sup>7</sup> and draft pick slot ( _DRFT_ ).<sup>8</sup> The following time-constant dummy variables were also included in our estimation – college experience ( _CLLGE_ ),<sup>9</sup> playing position ( _PSTN_ ),<sup>10</sup> nationality ( _NATL_ ),<sup>11</sup> and race ( _RACE_ ).<sup>12</sup> Our variable of interest was _AGE_ .  The other explanatory variables have been frequently used in the relevant NBA-related literature highlighted above.  To test our null hypothesis that age of entry has no effect on NBA careers, we selected three dependent variables given that there is no single definitive measure of basketball career success:<sup>13</sup> 

4 For example, from 1995 to 2000, the CBA mandated that all initial contracts for first round draft picks be guaranteed for three years. 

5 Shawn Kemp was drafted in the first round of the NBA draft by the Seattle Supersonics in 1989. Following graduation from high school in 1988, Kemp enrolled at the University of Kentucky before transferring to a junior college.  However, Kemp never played in a college basketball game during the one year period between high school and the 1989 NBA draft.  As such, it is factually incorrect to label Kemp as a player who moved straight from high school to the NBA. 

> 6 _AGE_ during the draft year for every player is set forth in Appendix A. 

> 7 _HT_ is denoted in meters. 

> 8 _DRFT_ is an ordinal ranking and a reasonable proxy for important, yet unobservable, variables such as ability and talent. 

9 1 = some college, 0 = no college. 

10 1 = primarily a guard, 0 = primarily a forward or center. 

11 1 = American, 0 = non-American. 

12 1= black, 0 = non-black. 

13 We did not include salary as dependent variable for two reasons.  First, Groothuis, Hill, and Perri (2007) and Rosenbaum (2003) showed that the CBA severely distorts salary levels at the outset of a player’s career and has residual effects throughout.  Second, McCann (2006) described a number of nonmonetary reasons why players may enter into a contract with a certain team during free agency. 

3 

_Submission to Journal of Quantitative Analysis in Sports_ 

- (i) Average minutes played per game ( _MNT_ ).  Given that players can only (directly) help their team win when actually participating in the game, _MNT_ is a reasonable gauge of how valuable the player is to his team. 

- (ii) Player efficiency rating ( _PER_ ).  As a composite metric, _PER_ considers a variety of micro-level player statistics commonly found in a basketball box score.  Points, rebounds, assists, turnovers, and fouls are all examples.<sup>14</sup> 

- (iii) All-star game appearances ( _A-S_ ).  All-star game appearances are a subjective measure of macro-level career outcomes that result from league, coach, media, peer, and fan input. 

Summary statistics for our full sample (all players 1989 to 2000 inclusive) are set forth in Table 1. 

#### **Empirical Strategy** 

Each of our dependent variables was modeled using a censored normal regression estimator.  Using ordinary least squares regression with partially censored dependent variables would have been problematic.  When an observed dependent variable is censored, “variation in the observed dependent variable will understate the effect of the regressors on the true dependent variable” (Chay & Powell, 2001, p. 29). Accordingly, standard ordinary least squares regression using censored data will typically result in a violation of assumptions related to homoskedasticity and normality.  Through the use of a censored normal regression model, the empirical analysis can forecast the dependent variables even though the full range of values is not observed.  Here, 55 players in our full sample ( _N_ =332) were still active as of the end of the 2011 season.  Applying the censored normal regression model addresses such data censoring (Wooldridge, 2009, p. 600).  Kennedy (2008, p. 270) makes clear that the “estimated coefficients from censored and truncated models must be interpreted with care.”  Even though only 16.57% (55 of 332) of the subjects in our data set are censored, coefficient estimates would differ, by moving towards zero, if we were to (incorrectly) apply ordinary least squares regression and treat all data points as being uncensored. 

> 14 A detailed discussion regarding the calculation of _PER_ is set forth in Hollinger (2011). 

4 

Rodenberg and Kim: NBA Age Rule 

**Table 1.  Summary Statistics** 

|||Full Sa<br>|mple(1<br>|989-2000<br>|)<br>||Sub Sam<br>|ple 1(<br>|1989-199<br>|4)<br>||Sub Sa<br>|mple 2<br>|(1995-20<br>|00)<br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Variable|N|Mean|SD|Min|Max|N|Mean|SD|Min|Max|N|Mean|SD|Min|Max|
|AGE|332|22.03|1.27|18|26|161|22.36|0.96|20|26|171|21.71|1.43|18|26|
|DRFT|332|14.40|8.07|1|29|161|13.93|7.79|1|27|171|14.83|8.33|1|29|
|CLLGE|332|0.94|0.24|0|1|161|0.99|0.08|0|1|171|0.88|0.32|0|1|
|PSTN|332|0.40|0.49|0|1|161|0.45|0.50|0|1|171|0.35|0.48|0|1|
|HT|332|2.02|0.09|1.78|2.28|161|2.01|0.09|1.78|2.28|171|2.02|0.09|1.78|2.24|
|NATL|332|0.89|0.32|0|1|161|0.94|0.24|0|1|171|0.84|0.37|0|1|
|RACE|332|0.79|0.41|0|1|161|0.84|0.36|0|1|171|0.73|0.44|0|1|
|MNT|332|21.95|8.81|3.10|41.10|161|21.60|8.63|3.10|38.60|171|22.28|8.99|4.10|41.10|
|PER|332|13.54|3.61|-0.90|26.40|161|13.32|3.30|-0.40|26.40|171|13.74|3.88|-0.90|24.80|
|A-S|332|0.82|2.33|0|15|161|0.72|2.05|0|15|171|0.91|2.57|0|14|



_Legend_ . AGE - age of NBA entry; DRFT - draft pick slot; CLLGE - college experience; PSTN - playing position; HT - height; NATL - nationality; RACE - race; MNT - average minutes played per game; PER – career player efficiency rating; and A-S - all-star game appearances. 

**Figure 1.  Fitted Values of Dependent Variables as a Function of AGE** 



<!-- Start of picture text -->
(1) MNT - AGE                                                   (2) PER - AGE                                                     (3) A-S - AGE<br>18 20 22 24 26 18 20 22 24 26 18 20 22 24 26<br>Age Age Age<br>Full Sample Sub Sample 1 Full Sample Sub Sample 1 Full Sample Sub Sample 1<br>Sub Sample 2 Sub Sample 2 Sub Sample 2<br>35 18 3<br>30 16 2<br>MNT 25 PER 14 A-S 1<br>20 12 0<br>15 10 -1<br>10 8 -2<br><!-- End of picture text -->

_Note_ . The fitted values of MNT, PER, and A-S are plotted against AGE, our variable of interest, across each of our samples after fixing all remaining variables at their means. AGE has a negative relationship with each dependent variable, implying that players drafted at a younger age play more minutes, earn higher player efficiency ratings, and appear in more all-star games. 

5 

_Submission to Journal of Quantitative Analysis in Sports_ 

Further, we bifurcated our full sample to more closely capture important year effects as would be done using a regression discontinuity model.  In 1995, for the first time in 20 years,<sup>15</sup> a player was drafted straight from high school into the NBA.<sup>16</sup> Over the course of the next ten years (1996 to 2005), dozens of other players with no college-level playing experience were selected by teams in the NBA draft.  The bilateral enactment of the minimum age rule in 2005 ended the practice, as the 2006 draft did not include any high school players.  In order to replicate the natural experiment approach highlighted by Kahn (2000) and Kennedy (2008), we halved our full sample – 1989-1994 (sub-sample #1) and 1995-2000 (sub-sample #2).  This allowed us to further tease out the impact age of entry has on career success.  As such, the analytical framework here is most accurately described as an indirect test of the NBA’s age rule, with 1995’s seminal event serving as a mid-point.<sup>17</sup> Similarly, given the _de facto_ age rule that was in place from 1976 to 1994, using 1995 as an equalizing fulcrum for our twelve year sample is intuitive and practical.  Summary statistics for sub-sample #1 (1989-1994) and sub-sample #2 (1995-2000) are set forth in Table 1. 

To address any issues pertaining to selection bias and contemporaneously account for “one and done” players who leave college for the NBA after one year and are the focus of the aforementioned controversy surrounding the practical effects of the NBA’s current age rule, we individually coded players and ran a series of selection bias tests to tease out any beneficial effect of one year in college and the actual age when teenagers are drafted (18 or 19).  Our group selection bias tests examined whether players who entered the NBA directly from high school have better on-court performance than players entering the league following one year of college (the aforementioned “one and done” players).  To conduct the bias tests, a dummy coded variable for the two groups<sup>18</sup> and the same 

15 Moses Malone was drafted straight out of high school in 1974.  Darryl Dawkins and Dave Willoughby both followed suit in 1975.  Several years earlier, Spencer Haywood had challenged the NBA’s then-restrictive age rule requiring all draft eligible players to be four years removed from high school graduation.  Haywood’s antitrust challenge to the NBA’s rule succeeded after the case reached the U.S. Supreme Court, an event that enabled high school players to bypass college and be eligible for the NBA draft. 

16 Kevin Garnett was drafted fifth overall by the Minnesota Timberwolves. 

17 A direct test of the NBA’s current age rule would consider player outcomes among those who entered the league just before and just after the imposition of the age rule following the 2005 draft. In 2012, such a direct test is impractical.  Given the relatively short amount of time that has passed since the imposition of the rule and the fact that virtually all of the players remain active in the infancy of their NBA careers, the data would be severely censored.  The high degree of statistical noise would cause all standard errors to explode, resulting in an imprecise estimation of our variable of interest ( _AGE_ ) as well as all the other control variables.  Given these problems, any inferences from such a direct test would be tenuous and superficial. 

18 0 = players drafted directly out of high school, 1 = quasi-“one and done” players.  For the avoidance of doubt, the three non-American players meeting the aforementioned criteria were 

6 

Rodenberg and Kim: NBA Age Rule 

player-specific independent variables used in the main analyses<sup>19</sup> were regressed on our three dependent variables.<sup>20</sup> The inclusion of the additional dummy variable allowed us to investigate the beneficial effect of one year in college while controlling for age of entry.  A censored normal regression model is used because some of the players in both groups ( _N_ =31) are still active players so their NBA careers have yet to end.  The null hypothesis for the group selection bias models is that there will be no difference in career success between “one and done” players and those who entered the NBA straight out of high school.  The results for the group selection bias tests are set forth in Table 3. 

### **Results** 

Regression results for the full sample, sub-sample #1, and sub-sample #2 are set forth in Table 2, with graphs illustrating the fitted values of our three dependent variables ( _MNT, PER,_ and _A-S_ ) as a function of our variable of interest ( _AGE_ ) set forth in Figure 1.  Players who are drafted at a younger age relative to other draftees have, on average, more successful NBA careers.  The importance of such precocity is consistent across all three dependent variables ( _MNT_ , _PER_ , and _A-S_ ) considered here.  Players who enter the NBA at a younger age play more minutes per game, earn a higher player efficiency rating, and appear in more all-star games.  These general results are further explained when comparing the agerelated coefficients in sub-sample #1 and sub-sample #2.  Revealingly, the playerlevel outcomes in sub-sample #2 (1995-2000) are driving the results for the full sample, evidencing the pronounced impact high school players with no college experience have had.  Coefficients for our variable of interest – _AGE_ – are statistically significant predictors for each dependent variable at the 1% level for both our full sample and sub-sample #2.  In addition to being statistically significant, an interpretation of the regression coefficients reveals that our results are practically significant. 

dropped from this analysis.  Further, given that our variable of interest is age, we dropped the three American players who were drafted at the age of 19 following one year of college, as such players’ ages were indistinguishable from the ages of American players who entered the NBA directly from high school.  These players were Stephon Marbury, Larry Hughes, and Ricky Davis. 19 The _NATL_ variable was dropped in this analysis because all players included were an American. 20 Such players are listed in Appendix B, with year drafted and age when drafted included. 

7 

_Submission to Journal of Quantitative Analysis in Sports_ 

**Table 2.  Censored Normal Regression Results** 

||Full S|ample(1989-|2000)|Sub Sa|mple 1(1989|-1994)|Sub Sa|mple 2(199|5-2000)|
|---|---|---|---|---|---|---|---|---|---|
|Variable|MNT|PER|A-S|MNT|PER|A-S|MNT|PER|A-S|
|AGE|-1.825***|-0.778***|-0.482***|-0.950|-0.340|-0.234|-2.023***|-0.907***|-0.559***|
||(0.056)|(0.185)|(0.122)|(0.593)|(0.274)|(0.176)|(0.571)|(0.279)|(0.185)|
|DRFT|-0.612***|-0.181***|-0.093***|-0.627***|-0.164***|-0.085***|-0.659***|-0.219***|-0.111***|
||(0.056)|(0.026)|(0.017)|(0.073)|(0.034)|(0.022)|(0.087)|(0.043)|(0.028)|
|EDUC|-5.320**|-3.406***|-2.467***|-22.04***|-6.751**|-0.886|-3.357|-3.074**|-2.467***|
||(2.193)|(1.027)|(0.676)|(7.101)|(3.276)|(2.113)|(2.648)|(1.288)|(0.845)|
|PSTN|2.414*|-0.371|0.333|1.336|-0.356|0.069|5.231**|-0.004|0.905|
||(1.342)|(0.629)|(0.414)|(1.598)|(0.737)|(0.475)|(2.290)|(1.117)|(0.741)|
|HT|-7.980|-6.668*|-0.017|-8.057|-4.931|1.038|-0.368|-6.380|0.267|
||(7.459)|(3.496)|(2.304)|(9.045)|(4.173)|(2.691)|(12.467)|(6.077)|(4.037)|
|NATL|-0.029|-0.283|-0.399|1.867|-0.073|-0.084|0.148|-0.241|-0.628|
||(1.549)|(0.721)|(0.472)|(2.343)|(1.081)|(0.697)|(2.170)|(1.046)|(0.685)|
|RACE|2.473**|0.482|0.354|4.928***|0.568|0.106|1.268|0.582|0.581|
||(1.132)|(0.531)|(0.348)|(1.490)|(0.689)|(0.442)|(1.753)|(0.853)|(0.562)|
|Constant|90.043|50.377|15.408|83.214|39.616|5.898|78.841|53.089|16.90|
||(18.368)|(8.616)|(5.705)|(24.143)|(11.144)|(7.181)|(30.266)|(14.793)|(9.883)|
|Total<br>Observations|332|332|332|161|161|161|171|171|171|
|Censored<br>Observations|55|55|55|3|3|3|52|52|52|
|Pseudo R<sup>2</sup>|0.09|0.07|0.07|0.08|0.04|0.04|0.10|0.08|0.09|



_Note_ . Robust standard errors in parentheses.  *, **, and *** denote significance at 10, 5 and 1% levels, respectively.  Our regression results evidence that players who enter the NBA at a younger age are expected to play more minutes per game, earn a higher player efficiency rating, and appear in more all-star games.  These general results from our full sample are supported by the results derived from sub-sample #2. 

8 

Rodenberg and Kim: NBA Age Rule 

Among all players in our full sample (1989-2000), for every year older a player is when he enters the league, we expect that he will play close to two minutes less per game, earn a _PER_ that is roughly 0.75 lower, and have about 0.5 less all-star game appearances over the course of his NBA career.<sup>21</sup> The practical effects of being a year older relative to others is even more pronounced among players in sub-sample #2 (1995-2000).  Like age, our estimates similarly reveal that increased education at the university level does not result in better on-court outcomes.  Players in our full sample with at least some college experience are expected to play over five minutes less per game, earn a _PER_ that is 3.4 lower, and participate in almost 2.5 fewer all-star games.  A player’s draft position proxies talent and ability, as _DRFT_ was significant at the 1% level across every specification.<sup>22</sup> The remaining control variables did not hold any systematic predictive power vis-à-vis each dependent variable and the different sample restrictions. 

Using a completely censored sample of 13 players drafted from 2007 to 2010, Haberstroh (2011) concluded that players who would have likely entered the NBA straight out of high school but were barred by the 2005 age rule do not seem to have better on-court performance than players who entered the NBA directly from high school before the eligibility rule was imposed.  Regression results from our group selection bias tests are in line with Haberstroh.  Players who entered the NBA straight out of high school played more minutes per game and appeared in more all-star games than players who entered the NBA after one year of college basketball playing experience.  In sum, the results of our group selection bias tests are consistent with the results of the main analyses – players who are drafted at a younger age relative to other draftees have better on-court performance.  Likewise, the group selection bias tests reject our narrower null hypothesis and imply that players who entered the NBA directly from high school have more successful NBA careers than “one and done” players.  As such, we are on safe ground in concluding that there was no selection bias in our main analyses.  Regression results for group selection bias tests are set forth in Table 3. 

> 21 As a player-level composite metric that is relative in nature and only intuitively meaningful when compared to other players, we acknowledge that a discussion of the practical significance of age on _PER_ is somewhat extenuated. 

> 22 Sunk costs may also play a role in how draft pick slotting impacts on-court performance, a topic explored in-depth by Staw and Hoang (1995). 

9 

_Submission to Journal of Quantitative Analysis in Sports_ 

**Table 3.  Censored Normal Regression Results (Group Selection Bias Tests)** 

|Variable|MNT|PER|A-S|
|---|---|---|---|
|GROUP|-5.528***|0.126|-3.460***|
||(1.395)|(0.693)|(0.579)|
|AGE|-0.329***|-2.095***|-0.230***|
||(0.081)|(0.039)|(0.032)|
|DRFT|-0.517***|-0.256***|-0.113***|
||(0.080)|(0.039)|(0.032)|
|PSTN|1.947|2.415***|7.335***|
||(1.268)|(0.579)|(0.432)|
|HT|-33.015***|5.430***|32.438***|
||(0.762)|(0.371)|(0.300)|
|RACE|-64.899***|-30.218***|-25.143***|
||(1.572)|(0.764)|(0.619)|
|Constant|179.401|80.646|-29.392|
||(1.572)|(0.764)|(0.619)|
|Total Observations|31|31|31|
|Censored Observations<br>|15|15|15|
|Pseudo R<sup>2</sup>|0.04|0.04|0.08|



_Note_ . Robust standard errors in parentheses.  *** denotes significance at 1% level. Group selection bias tests were conducted to compare the on-court performance between players who entered the NBA straight out of high school and players who entered the NBA after one year of college. The results of such test indicate that players who enter the NBA directly from high school played more minutes per game and appeared in more all-star games than so-called one-and-done players. 

### **Discussion and Conclusion** 

Our tests pertaining to the NBA age eligibility rule’s efficacy tell a number of interrelated stories, all of which question the justifications for the rule and challenge the necessity of the “one size fits all” policy.  First, despite the inability to evaluate young players extensively during college-level competition, NBA teams have repeatedly demonstrated their draft day expertise when selecting young players, especially those moving straight from high school to the NBA.<sup>23</sup> Second, there is no systematic evidence of success among late-blooming NBA players.  This indicates that NBA-level professional basketball talent is probably manifested and observable no later than the age of 18.  Third, there is no evidence that players who played one year of college basketball, while controlling for other factors, perform better than individuals who moved into the NBA straight from high school. 

23 Groothuis, Hill, and Perri (2009) discussed the difficulty of choosing talent in the NBA draft generally. 

10 

Rodenberg and Kim: NBA Age Rule 

Our results and policy-related conclusions are neither surprising nor novel. Even a casual observer of professional basketball would likely posit that some of the best players in the NBA over the course of the past decade entered the league straight out of high school.  Examples include Kevin Garnett, Kobe Bryant, LeBron James, and Dwight Howard.<sup>24</sup> Nevertheless, there are sample-related limitations to our study,<sup>25</sup> the most prominent tied to possible non-random sample selection and self-selection among players who partake in the NBA draft.<sup>26</sup> Accordingly, we are cautious in not overstating the inferences from our results and careful not to over-generalize our analysis, as it only pertains to the on-court efficacy of the minimum age policy in basketball.<sup>27</sup> 

The NBA doesn’t try to defend its rule on ethical, moral, or educational grounds (Lowe, 2011).  Beck (2009) quoted NBA Commissioner David Stern: “This is a business decision by the NBA, which is: We like to see our players in competition after high school.”  The league has also effectively rebutted criticism by pointing out non-sports examples of age rules being imposed, with the most prominent example being the U.S. Constitution’s minimum ages set for representatives, senators, and the presidency.  Likewise, other prominent sports governing bodies such as the National Football League (NFL) impose age eligibility rules.<sup>28</sup> As explained by Abbott (2010), the NBPA also faces potentially problematic issues related to the age rule.  Namely, marginal veteran NBA players (and union members) looking to preserve their lucrative spot at the end of a team’s bench have a strong incentive to see better/younger players excluded from the league for as long as possible.  NPBA voting membership is limited to current NBA players, not prospective undrafted players. 

> 24 Haberstroh (2011) summarized: “The league was able to convince the masses that high schoolers aren’t fit for the big show despite overwhelming evidence to the contrary.  Here’s the hidden truth about David Stern’s NBA: Most of its stars never went to college.” 25 Heckman (1979) and its progeny address sample selection issues in detail. 

> 26 As discussed above, our sample: (i) is partially censored; (ii) does not include second round draft picks; (iii) does not include players who were draft-eligible but were not drafted; and (iv) lends itself only to an indirect test of the NBA’s age eligibility rule at the present time. 

> 27 Haberstroh (2011) addressed such sample-related issues by using an effective rhetorical argument: “The skeptic will argue, ‘Obviously, the high school prospects did better than the guys who weren’t good enough to come out early,’ _but that’s exactly the point. Why are we forbidding the most valuable prospects from the [NBA]_ ?” (emphasis added) 

28 The NFL’s minimum age rule was upheld in litigation involving former Ohio State University running back Maurice Clarett. 

11 

_Submission to Journal of Quantitative Analysis in Sports_ 

Weiss (2005) highlighted some of the inherent difficulties in any sportrelated age rule policy: 

Chronological age is not equivalent to social, emotional, cognitive, and anatomical age. We need age eligibility rules, but we also know that chronological age, while we use it as a main index for classifying athletes, is not reliably associated with these other age or maturity levels. Two adolescents of the same age can be widely different in terms of social and emotional types of maturity (p. 2). 

Handling draft eligibility issues on a case-by-case basis in the NBA has been advocated by Vitale (2005) and is employed by other governing bodies such as the Ladies Professional Golf Association (LPGA) Tour.  The LPGA Tour requires all full-time playing members to be at least 18, but has a mechanism in place whereby underage players can apply for tour membership earlier (Rodenberg, Gregg, and Fielding, 2009).  For example, in 2011 the LPGA Tour allowed 16 year old Lexi Thompson to join the tour following a full vetting of her comprehensive application.  In an ironic (and revealing) twist, such a case-bycase evaluation is what resulted following the _Haywood v. NBA_ Supreme Court decision, with the NBA required to consider “hardship” waivers for draft eligibility.  Absent abolishment of the rule, perhaps a more nuanced and individualized consideration of a prospective player’s draft eligibility would be prudent given the dearth of evidence pointing to any on-court efficacy of the NBA’s age eligibility rule. 

12 

Rodenberg and Kim: NBA Age Rule 

### **Appendix A.  Players Included in Data Set** 

|1989||1990||1991||
|---|---|---|---|---|---|
|Name|Age|Name|Age|Name|Age|
|Pervis Ellison|22|Derrick Coleman|23|Larry Johnson|22|
|Danny Ferry|23|Gary Payton|22|Kenny Anderson|21|
|Sean Elliott|23|Mahmoud Abdul-Rauf|21|Billy Owens|22|
|Glen Rice|22|Dennis Scott|22|Dikembe Mutombo|25|
|J.R. Reid|21|Kendall Gill|22|Steve Smith|22|
|Stacey King|22|Felton Spencer|22|Doug Smith|22|
|George McCloud|22|Lionel Simmons|22|Luc Longley|22|
|Randy White|22|Bo Kimble|24|Mark Macon|22|
|Tom Hammonds|22|Willie Burton|22|Stacey Augmon|23|
|Pooh Richardson|23|Rumeal Robinson|24|Bison Dele|22|
|Nick Anderson|23|Tyrone Hill|22|Terrell Brandon|21|
|Mookie Blaylock|22|Alec Kessler|23|Greg Anthony|24|
|Michael Smith|24|Loy Vaught|22|Dale Davis|22|
|Tim Hardaway|23|Travis Mays|22|Rich King|22|
|Todd Lichti|22|Dave Jamerson|23|Anthony Avent|23|
|Dana Barros|22|Terry Mills|23|Chris Gatling|24|
|Shawn Kemp|20|Jerrod Mustaf|21|Victor Alexander|22|
|B.J. Armstrong|22|Duane Causwell|22|Kevin Brooks|22|
|Kenny Payne|23|Dee Brown|22|LaBradford Smith|22|
|Jeff Sanders|23|Gerald Glass|23|John Turner|24|
|Blue Edwards|24|Jayson Williams|22|Eric Murdock|23|
|Byron Irvin|23|Tate George|22|LeRon Ellis|22|
|Roy Marble|23|Anthony Bonner|22|Stanley Roberts|21|
|Anthony Cook|23|Dwayne Schintzius|22|Rick Fox|22|
|John Morton|22|Alaa Abdelnaby|22|Mark Randall|24|
|Vlade Divac|21|Lance Blanks|24|Pete Chilcutt|23|
|KennyBattle|25|Elden Campbell|22|||



13 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **Appendix A.  Players Included in Data Set (Continued)** 

|1992||1993||1994||
|---|---|---|---|---|---|
|Name|Age|Name|Age|Name|Age|
|Shaquille O'Neal|20|Chris Webber|22|Glenn Robinson|21|
|Alonzo Mourning|22|Shawn Bradley|23|Jason Kidd*|21|
|Christian Laettner|23|Anfernee Hardaway|23|Grant Hill*|22|
|Jim Jackson|22|Jamal Mashburn|22|Donyell Marshall|21|
|LaPhonso Ellis|22|Isaiah Rider|21|Juwan Howard*|21|
|Tom Gugliotta|23|Calbert Cheaney|22|Sharone Wright|21|
|Walt Williams|22|Bobby Hurley|22|Lamond Murray|21|
|Todd Day|22|Vin Baker|22|Brian Grant|22|
|Clarence Weatherspoon|22|Rodney Rogers|22|Eric Montross|23|
|Adam Keefe|22|Lindsey Hunter|23|Eddie Jones|23|
|Robert Horry|22|Allan Houston|23|Carlos Rogers|23|
|Harold Miner|21|George Lynch|22|Khalid Reeves|22|
|Bryant Stith|22|Terry Dehere|24|Jalen Rose|21|
|Malik Sealy|22|Scott Haskin|23|Yinka Dare|22|
|Anthony Peeler|23|Doug Edwards|22|Eric Piatkowski|24|
|Randy Woods|22|Rex Walters|22|Clifford Rozier|22|
|Doug Christie|22|Greg Graham|20|Aaron McKie|22|
|Tracy Murray|21|Luther Wright|22|Eric Mobley|24|
|Don MacLean|22|Acie Earl|23|Tony Dumas|22|
|Hubert Davis|22|Scott Burrell|23|B.J. Tyler|23|
|Jon Barry|23|James Robinson|24|Dickey Simpkins|22|
|Oliver Miller|22|Chris Mills|23|Bill Curley|22|
|Lee Mayberry|22|Ervin Johnson|23|Wesley Person|23|
|Latrell Sprewell|22|Sam Cassell|23|Monty Williams|23|
|Elmore Spencer|23|Corie Blount|22|Greg Minor|23|
|Dave Johnson|22|Geert Hammink|21|Charlie Ward|24|
|Byron Houston|23|Malcolm Mackey|25|Brooks Thompson|24|



_Note_ : * denotes players still active. 

14 

Rodenberg and Kim: NBA Age Rule 

### **Appendix A.  Players Included in Data Set (Continued)** 

|1995||1996||1997||
|---|---|---|---|---|---|
|Name|Age|Name|Age|Name|Age|
|Joe Smith|20|Allen Iverson|21|Tim Duncan*|21|
|Antonio McDyess*|21|Marcus Camby*|22|Keith Van Horn|22|
|Jerry Stackhouse*|21|Shareef Abdur-Rahim|20|Chauncey Billups*|21|
|Rasheed Wallace|21|Stephon Marbury|19|Antonio Daniels|22|
|Kevin Garnett*|19|Ray Allen*|21|Tony Battie*|21|
|Bryant Reeves|22|Antoine Walker|20|Ron Mercer|21|
|Damon Stoudamire|22|Lorenzen Wright|21|Tim Thomas|20|
|Shawn Respert|23|Kerry Kittles|22|Adonal Foyle|22|
|Ed O'Bannon|23|Samaki Walker|20|Tracy McGrady*|18|
|Kurt Thomas*|23|Erick Dampier*|21|Danny Fortson|21|
|Gary Trent|21|Todd Fuller|22|Tariq Abdul-Wahad|23|
|Cherokee Parks|23|Vitaly Potapenko|21|Austin Croshere|22|
|Corliss Williamson|22|Kobe Bryant*|18|Derek Anderson|23|
|Eric Williams|23|Peja Stojakovic*|21|Maurice Taylor|21|
|Brent Barry|24|Steve Nash*|22|Kelvin Cato|23|
|Alan Henderson|23|Tony Delk|22|Brevin Knight|22|
|Bob Sura|22|Jermaine ONeal*|18|Johnny Taylor|23|
|Theo Ratliff*|22|John Wallace|22|Chris Anstey|22|
|Randolph Childress|23|Walter McCarty|22|Scot Pollard|22|
|Jason Caffey|22|Zydrunas Ilgauskas*|22|Paul Grant|24|
|Michael Finley|22|Dontae Jones|22|Anthony Parker*|22|
|George Zidek|22|Roy Rogers|23|Ed Gray|22|
|Travis Best|23|Efthimis Rentzias|26|Bobby Jackson|24|
|Loren Meyer|23|Derek Fisher*|22|Rodrick Rhodes|24|
|David Vaughn|22|Martin Muursepp|22|John Thomas|22|
|Sherell Ford|23|Jerome Williams|23|Charles Smith|22|
|Mario Bennett|22|Brian Evans|23|Jacque Vaughn|22|
|||Priest Lauderdale|23|Keith Booth|23|
|||Travis Knight|22|||



_Note_ : * denotes players still active. 

15 

_Submission to Journal of Quantitative Analysis in Sports_ 

### **Appendix A.  Players Included in Data Set (Continued)** 

|1998||1999||2000||
|---|---|---|---|---|---|
|Name|Age|Name|Age|Name|Age|
|Michael Olowokandi|23|Elton Brand*|20|Kenyon Martin*|23|
|Mike Bibby*|20|Steve Francis|22|Stromile Swift|21|
|Raef LaFrentz|22|Baron Davis*|20|Darius Miles|19|
|Antawn Jamison*|22|Lamar Odom*|20|Marcus Fizer|22|
|Vince Carter*|21|Jonathan Bender|18|Mike Miller*|20|
|Robert Traylor|21|Wally Szczerbiak|22|DerMarr Johnson|20|
|Jason Williams*|23|Richard Hamilton*|21|Chris Mihm|21|
|Larry Hughes|19|Andre Miller*|23|Jamal Crawford*|20|
|Dirk Nowitzki*|20|Shawn Marion*|21|Joel Przybilla*|21|
|Paul Pierce*|21|Jason Terry*|22|Keyon Dooling*|20|
|Bonzi Wells|22|Trajan Langdon|23|Jerome Moiso|22|
|Michael Doleac|21|Aleksandar Radojevic|23|Etan Thomas*|23|
|Keon Clark|23|Corey Maggette*|20|Courtney Alexander|23|
|Michael Dickerson|23|William Avery|20|Mateen Cleaves|23|
|Matt Harpring|25|Ron Artest*|20|Jason Collier|23|
|Bryce Drew|24|Cal Bowdler|22|Hedo Turkoglu*|21|
|Rasho Nesterovic|22|James Posey*|22|Desmond Mason|23|
|Mirsad Turkcan|23|Quincy Lewis|22|Quentin Richardson*|20|
|Pat Garrity|22|Dion Glover|21|Jamaal Magloire*|22|
|Roshown McLeod|23|Jeff Foster*|22|Speedy Claxton|23|
|Ricky Davis|19|Kenny Thomas|22|Morris Peterson*|23|
|Brian Skinner*|22|Devean George|22|Donnell Harvey|20|
|Tyronn Lue|21|Andrei Kirilenko*|20|DeShawn Stevenson*|19|
|Felipe Lopez|24|Tim James|23|Dalibor Bagaric|20|
|Al Harrington*|18|Vonteego Cummings|23|Jake Tsakalidis|21|
|Samuel Jacobson|23|Jumaine Jones|20|Mamadou N'Diaye|25|
|Vladimir Stepania|22|Scott Padgett|23|Primoz Brezec|22|
|Corey Benjamin|20|Leon Smith|21|Erick Barkley|24|
|Nazr Mohammed*|21|||Mark Madsen|24|



_Note_ : * denotes players still active. 

16 

Rodenberg and Kim: NBA Age Rule 

### **Appendix B.** 

### **Players Used in the Group Selection Bias Test (** **_N_ = 31)** 

|Players enteringthe NBA out of high s<br> <br>|chool<br>|Quasi-one and done<br>|players based on<br>|age<br>|
|---|---|---|---|---|
|Name<br>Year Drafted|Age|Name|Year Drafted|Age|
|Kevin Garnett<br>1995|19|Shawn Kemp|1989|20|
|Kobe Bryant<br>1996|18|Shaquille O’Neal|1992|20|
|Jermaine O’Neal<br>1996|18|Chris Webber|1993|20|
|Tracy McGrady<br>1997|18|Joe Smith|1995|20|
|Al Harrington<br>1998|18|Shareef Abdur-Rahim|1996|20|
|Jonathan Bender<br>1999|18|Antoine Walker|1996|20|
|Darius Miles<br>2000|19|Samaki Walker|1996|20|
|DeShawn Stevenson<br>2000|19|Tim Thomas|1997|20|
|||Mike Bibby|1998|20|
|||Corey Benjamin|1998|20|
|||Elton Brand|1999|20|
|||Baron Davis|1999|20|
|||Lamar Odom|1999|20|
|||Corey Maggette|1999|20|
|||William Avery|1999|20|
|||Ron Artest|1999|20|
|||Jumaine Jones|1999|20|
|||Mike Miller|2000|20|
|||DerMarr Johnson|2000|20|
|||Jamal Crawford|2000|20|
|||Keyon Dooling|2000|20|
|||Quentin Richardson|2000|20|
|||Donnell Harvey|2000|20|



### **References** 

- Abbott, H. (2010). Larry Coon on the age restriction. _ESPN.com_ , November 23. Retrieved November 18, 2011 from 

http://espn.go.com/blog/truehoop/post/_/id/22011/larry-coon-on-agerestriction. 

- Beck, H. (2009). NBA commissioner Stern wants to preserve age limit for players, _NYTimes.com_ , June 5. Retrieved November 13, 2011 from http://www.nytimes.com/2009/06/05/sports/basketball/05stern.html. 

- Berri, D. J., Brook, S. L., & Fenn, A. J. (2011). From college to the pros: Predicting the NBA amateur player draft. _Journal of Productivity Analysis_ , _35_ (1), 25-35. 

17 

_Submission to Journal of Quantitative Analysis in Sports_ 

- Bradbury, J. C. (2009). Peak athletic performance and ageing: Evidence from baseball. _Journal of Sports Sciences, 27_ (6), 599-610. 

- Chay, K. Y., & Powell, J. L. (2001). Semiparametric censored regression models. _Journal of Economic Perspectives_ , _15_ (4), 29-42. 

_Clarett v. National Football League_ , 369 F.3d 124 (2004). 

Coates, D., & Oguntimein, B. (2010). The length and success of NBA careers: Does college production predict professional outcomes? _International Journal of Sport Finance_ , _5_ (1), 4-26. 

- Eschker, E., Perez, S. J., & Siegler, M. V. (2004). The NBA and the influx of international basketball players. _Applied Economics, 36_ (10), 1009-1020. 

- Fried, H. O., & Tauer, L. W. (2011). The impact of age on the ability to perform under pressure: Golfers on the PGA Tour. _Journal of Productivity Analysis, 35_ (1), 75-84. 

- Gregory, S. (2008). 10 questions for David Stern, _Time.com_ , March 12. Retrieved November 12, 2011 from 

http://www.time.com/time/magazine/article/0,9171,1722284,00.html. 

- Groothuis, P. A., & Hill, J. R. (2004). Exit discrimination in the NBA: A duration analysis of career length. _Economic Inquiry, 42_ (2), 341-349. 

- Groothuis, P. A., Hill, J. R., & Perri, T. (2007). Early entry in the NBA draft: The influence of unraveling, human capital, and option value. _Journal of Sports Economics, 8_ (3), 223-243. 

- Groothuis, P. A., Hill, J. R., & Perri, T. (2009). The dilemma of choosing talent: Michael Jordans are hard to find. _Applied Economics, 41_ (25), 3193-3198. 

- Haberstroh, T. (2011). Impact of one-and-done rule. _ESPN.com_ , October 27. Retrieved November 18, 2011 from 

   - http://insider.espn.go.com/ncb/preview2011/story?id=7156333&_slug_=st ate-game-impact-one-done-rule-nba-college-basketball&action=login& appRedirect=http%3a%2f%2finsider.espn.go.com%2fncb%2fpreview201 1%2fstory%3fid%3d7156333%26_slug_%3dstate-game-impact-onedone-rule-nba-college-basketball. 

_Haywood v. National Basketball Association_ , 401 U.S. 1204 (1971). 

- Heckman, J. J. (1979). Sample selection bias as a specification error. Econometrica, _47_ (1), 153-161. 

- Hollinger, J. (2011). What is PER? _ESPN.com_ , August 8. Retrieved November 13, 2011 from http://sports.espn.go.com/nba/columns/story?columnist= hollinger_john&id=2850240. 

18 

##### Rodenberg and Kim: NBA Age Rule 

Jackson, S. (2010). NBA’s age restriction won’t change. _ESPN.com_ , January 18. Retrieved November 13, 2011 from 

http://sports.espn.go.com/espn/commentary/news/story?id=4836818 . 

- Jones, A. M. (2005). Hold the mayo: An analysis of the validity of the NBA’s stern no preps to pros rule and the application of the nonstatutory labor exemption. _Loyola of Los Angeles Entertainment Law Review, 26_ , 475522. 

- Kahn, L. M. (2000). The sports business as a labor market laboratory. _Journal of Economic Perspectives, 14_ (3), 75-94. 

- Kennedy, P. (2008). _A guide to econometrics_ . Maldon, MA: Blackwell Publishing. 

- Litman, J. A. (2010). Tremendous upside potential: How a high-school basketball player might challenge the National Basketball Association’s eligibility requirements. _Washington University Law Review, 88_ , 261-288. 

- Lowe, Z. (2011). Tressel scandal revives age limit debate. _SI.com,_ May 31, 2011. Retrieved November 17, 2011 from http://nba-point-forward.si.com/ 2011/05/31/tressel-scandal-revives-age-limit-debate/. 

McCann, M. A. (2006). It's not about the money: the role of preferences, 

- Cognitive biases and heuristics among professional athletes. _Brooklyn Law Review, 71_ , 1451-1570. 

- McCann, M. A. (2004). Illegal defense: the irrational economics of banning high school players from the NBA draft. _Virginia Sports and Entertainment Law Journal, 3_ , 115-198. 

- Miron, J. A., & Tetelbaum, E. (2009). Does the minimum legal drinking age save lives? _Economic Inquiry, 47_ (2), 317-336. 

- Popper, S. (1999). NBA: Roundup; Stern wants to set minimum age, _NYTimes.com_ , June 15. Retrieved November 14, 2011 from http://www.nytimes.com/1999/06/15/sports/nba-roundup-stern-wants-toset-minimum-age.html?scp=1&sq=steve%20popper%20stern%20age& st=cse. 

- Rodenberg, R. M., & Kim, J. W. (2011). Precocity and labor market outcomes: Evidence from professional basketball. _Economics Bulletin, 31_ (3), 21852190. 

- Rodenberg, R. M., & Stone, D. F. (2011). Short and long run labor market effects of age eligibility rules: Evidence from women’s professional tennis. _Journal of Labor Research, 32_ (2), 181-198. 

19 

_Submission to Journal of Quantitative Analysis in Sports_ 

- Rodenberg, R. M., Gregg, E. A., & Fielding, L. W. (2009). Age eligibility rules in women’s professional golf: A legal eagle or an antitrust bogey? _Journal of Legal Aspects of Sport, 19_ (2), 103-120. 

- Rosen, S., & Sanderson, A. (2001). Labor markets in professional sports. _The Economic Journal, 111_ (469), 47-68. 

- Rosenbaum, D. T. (2003). How the NBA turned a trickle of underclassmen leaving school early into a flood. Unpublished working paper. 

- Rossen, J. M. (2008). The NBA’s age minimum and its effect on high school phenoms. _Virginia Sports and Entertainment Law Journal, 8_ , 173-190. 

- Schulz, R., & Curnow, C. (1988). Peak performance and age among superathletes: Track and field, swimming, baseball, tennis, and golf. _Journal of Gerontology, 43_ (5), 113-120. 

- Shaffer, B. (2008). The NBA’s age requirement shoots and misses: How the nonstatutory exemption produces inequitable results for high school basketball stars. _Santa Clara Law Review, 48_ , 681-707. 

- Sheridan, C. (2005). Hunter still opposed to raising NBA age limit, _USAToday.com_ , May 12. Retrieved November 14, 2011 from http://www.usatoday.com/sports/basketball/nba/2005-05-12-hunter-agelimit_x.htm. 

- Sowell, C. B., & Mounts, W. S. (2005). Ability, age, and performance: Conclusions from the Ironman Triathlon World Championships. _Journal of Sports Economics, 6_ (1), 78-97. 

- Staw, B. M., & Hoang, H. (1995). Sunk costs in the NBA: Why draft order affects playing time and survival in professional basketball. _Administrative Science Quarterly, 40_ (3), 474-494. 

- Thamel, P. (2009). Congressman asks NBA and union to rescind age minimum for players, _NYTimes.com_ , June 4. Retrieved November 13, 2011 from http://query.nytimes.com/gst/fullpage.html?res=9506E6D61031F937A357 55C0A96F9C8B63. 

- Vitale, D. (2005). Don’t keep the best high schoolers out of the NBA. _ESPN.com_ , April 26. Retrieved on November 19, 2011 from http://espn.go.com/ dickvitale/vcolumn050425_ageplan.html. 

- Weiss, M. (2005, December). _Successful transitions: Strategies and programs_ . Oral presentation at “Phenoms to Professionals: Successful Transitions” forum hosted by the Ladies Professional Golf Association, Daytona Beach, FL. 

20 

Rodenberg and Kim: NBA Age Rule 

- Wooldridge, J. W. (2009). _Introductory econometrics: A modern approach_ . Mason, Ohio: South-Western Cengage Learning. 

- Zola, W. K. (2012). Transitioning to the NBA: Advocating on behalf of studentathletes for NBA & NCAA rule changes. _Harvard Journal of Sports & Entertainment Law, 3_ (1), 159-200. 

21 


