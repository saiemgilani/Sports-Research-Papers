<!-- source: randoms/An_Improved_Adjusted_Plus_Minus_Statisti (1).pdf -->

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



# **An Improved Adjusted Plus-Minus Statistic for NHL Players** 

Brian Macdonald Department of Mathematical Sciences United States Military Academy West Point, NY, USA, 10928 Email: bmac@jhu.edu 

## **Abstract** 

The plus-minus statistic for NHL players is meant to be a measure of a player's offensive and defensive abilities.  However, a player's plus-minus is highly dependent on the team he plays for, the opponents he faces, and other variables out of his control, so it is not always a good measure of that player's individual contribution to his team.  In this paper we develop an adjusted plus-minus statistic that attempts to isolate a player's individual contribution.  Using data from the detailed shift reports on NHL.com, we develop two weighted least squares regression models to estimate an NHL player's effect on his team's success in scoring and preventing goals, independent of that player's teammates and opponents.  Our initial work focused on even strength situations, excluding situations in which one team had pulled their goalie.  In our current work, we have modeled power play and shorthanded situations, and we are able to estimate a player's offensive and defensive contributions during those situations.  Also, for those shifts that begin with a faceoff, we have accounted for the zone on the ice in which a shift begins. 

## **1   Introduction** 

In basketball, the adjusted plus-minus (APM) statistic is used by NBA analysts, front offices, and fans for estimating the offensive and defensive contributions of players.  Several different adjusted plusminus models have been developed.  See, for example, [1], [2], [3], and [4].  One main benefit of these APM statistics is that each player's APM is independent of the strength of that player's teammates and opponents.  The APM statistic is considered an improvement of the traditional plus-minus statistic, which is highly dependent on the strength of a player's team, and also the strength of the opponents he faces.  Playing with very good players will tend to raise a player's plus-minus, while playing against very good players will tend to lower a player's plus-minus.  Since traditional plus-minus is so teamand opponent-dependent, it is not always a good measure of a player's individual contribution. 

In [5], the author develops an APM statistic for NHL players that uses models similar to those in [2] and [3] to estimate the individual contributions of players during even strength situations.  Hockey games are mostly played at even strength, so these statistics give a good indication of a player's contribution to his team.  However, unlike basketball, hockey is not always played at even strength. During a power play in hockey, the game can be played 5-on-4, 5-on-3, or 4-on-3, and we would like to estimate a player's contribution during these special teams situations as well.  A different model is 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



needed for these situations.  If we were to include special teams situations in the model in [5], players who spend a lot of time on the power play would have unfairly high ratings, while players who play during shorthanded situations would have unfairly low ratings. 

In this paper, we develop a new model for special teams situations.  Also, for those shifts which start with a faceoff, we use information about the zone in which the shift begins.  We include this information in the special teams model, and we modify the model in [5] by using this information in a new even strength model.  For each player, the models will give an offensive and defensive component of APM per 60 minutes for even strength, power play, and shorthanded situations separately.   Using playing time, we can also express these components of APM in terms of goals per season.  These converted results for even strength, power play, and shorthanded situations can be added to give the offensive (OPM), defensive (DPM), and total (APM) contributions of a player in all situations in terms of goals per season.  The notation we use for the different components of APM during different situations is summarized in Table 1.  The components of APM per 60 minutes are denoted similarly but with “/60” at the end. 

Table 1: Notation for the components of APM 

||Even Strength|Power Play|Shorthanded|Total(EV+PP+SH)|
|---|---|---|---|---|
|Offensive Component|EVOPM|PPOPM|SHOPM|OPM|
|Defensive Component|EVDPM|PPDPM|SHDPM|DPM|
|Total(Off. + Def.)|EVAPM|PPAPM|SHAPM|APM|



The rest of the paper is organized as follows.  The modified model for even strength situations and the model for special teams situations are described in Sections 2 and 3.  In Section 4, we give a sample of the results and discuss the best overall players according to APM, the best offensive players on the power play according to PPOPM/60, and the best defensive players in shorthanded situations according to SHDPM/60.  We finish with some concluding remarks in Section 5. 

## **2   Modified Model for Even Strength Situations** 

In the model in Section 2.1 of [5] each skater has both an offensive and defensive variable, and each goalie has only a defensive variable.  The model is 



which can be written more succinctly in summation notation as 



The variables in the model are defined as follows: 

- � = �0,    skater  �  is  not  playing,  not  on  offense,  or  not  at  even  strength;<sup>1,    skater  �  is  on  offense  and  at  even  strength  during  the  observation</sup> 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



- � = �0,    skater  �  is  not  playing,  not  on  defense,  or  not  at  even  strength;<sup>1,    skater  �  is  on  defense  and  at  even  strength  during  the  observation</sup> 

- �� = �0,    goalie  �  is  not  playing,  not  on  defense,  or  not  at  even  strength;<sup>1,    goalie  �  is  on  defense  and  at  even  strength  during  the  observation</sup> 

A shift is considered to be a period of time on the ice when no substitutions are made.  For each shift, we get two observations in this model, one corresponding to the offensive output of the home team, and one corresponding offensive output of the away team.  Each observation is weighted by the duration of the shift.  The data comes from the detailed shift reports on NHL.com for games played during the 2007-08, 2008-09, and 2009-10 seasons. 

The coefficients in the model have the following interpretation: 

- �� = goals  per  60  minutes  contributed  by  skater  �  on  offense  at  even  strength, �� = goals  per  60  minutes  contributed  by  skater  �  on  defense  at  even  strength, �� = goals  per  60  minutes  contributed  by  goalie  �  on  defense  at  even  strength. 

The least squares regression coefficients �<sup>�</sup> �, �<sup>�</sup> �,  and ���, are the components of our EVAPM/60 estimates: 

- <sup>�</sup> �  is  an  estimate  of  EVOPM/60  for  skater  �, 

- �<sup>�</sup> �  is  an  estimate  of  EVDPM/60  for  skater  �, 



Now that we wish to take into account initial zones, this model for even strength situations becomes 



where �  ����� = 1 for those observations in which a shift begins with a faceoff in the offensive zone, and �  ����� = 0  otherwise.  The values of ������ are determined likewise.  The variables ����, ����,  and ���� are defined the same as ��,  ��,  and ��.  Likewise, the least squares regression coefficients �<sup>�</sup> ���, �����, and ����� have the same interpretations as ���, ���,  and ���,.  We have added the superscripts �� to our variables and coefficients for clarity since we will have similar variables and coefficients for the power play model below. 

## **3   Model for Special Teams Situations** 

In our new model for special teams situations, we are estimating the offensive and defensive contribution of players during both power play and shorthanded situations.  Instead of having two variables in the model for each skater, like we did in the even strength model, each skater will have four variables.  Skaters will have two variables for offense and defense during power play situations, and two variables for offense and defense during shorthanded situations.  Each goalie will have two variables, one for defense during power plays, and one for defense during shorthanded situations.  As we did in [5], we assume that a goalie's impact on offense is negligible.  We use the linear model 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 





The variables ����, ����,  and ���� are defined similarly to ��,  ��,  and ��, except for power play situations.  Likewise, the variables ����, ����,  and ���� are defined similarly, except for shorthanded situations.  The least squares regression coefficients �<sup>�</sup> ���, �����, and ����� have the same interpretations as �<sup>�</sup> �, �<sup>�</sup> �,  and ���, except that they are for power play situations and estimate PPOPM/60 or PPDPM/60 instead of EVOPM/60 or EVDPM/60.  The coefficients �<sup>�</sup> ���, �����, and ����� have analogous interpretations but for shorthanded situations. 

We can combine or manipulate these statistics in various ways.  For example, to get a player's total contribution per 60 minutes on the power play, PPAPM/60, we can add his PPOPM/60 and PPDPM/60.  To get a player's PPOPM, we can divide his PPOPM/60 by 60 and multiply by his minutes played per season on the power play. Likewise, we can use playing time to find PPDPM and PPAPM for power play contributions per season, SHOPM, SHDPM, and SHAPM for shorthanded contributions per season, and EVOPM, EVDPM, and EVAPM for even strength contributions per season.  If we wish to determine a player's offensive, defensive, and total contribution per season in all situations, we can calculate OPM, DPM, and APM as follows: 



## **4   Results** 

We now give a sample of the results of the model.  In Table [2], we give the top 10 skaters in APM. Recall that APM is a measure of the total contribution of a player during both even strength and special teams situations in terms of goals per season.  Note that Rk is the rank of that player in terms of APM, Pos is the player's position, AErr is the standard error in the APM estimates, and Mins is the number of minutes that the player played on average during the 2007-08, 2008-09, and 2009-10 seasons. 

Pavel Datsyuk is considered by many to be the best two-way forward in the league, and his APM rating certainly supports that belief.  There are some notable omissions to this list of top skaters, including Sidney Crosby, Alex Ovechkin, and Evgeni Malkin, three of the league’s most recognizable superstars.  If we list the top 10 offensive players according to OPM, as we do in Table 3, Crosby, Ovechkin, and Malkin make the list, along with Henrik Sedin. 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



Table 2: Top 10 Skaters in APM 

|Rk|Player|Pos|OPM|DPM|APM|AErr|EVAPM|STAPM|Mins|
|---|---|---|---|---|---|---|---|---|---|
|1|Pavel Datsyuk|C|37.8|14.5|52.2|20.9|42.2|10.1|1602|
|2|Ryan Getzlaf|C|37.1|8.7|45.8|19.6|25.1|20.7|1426|
|3|Jeff Carter|C|36.1|9.2|45.3|15.7|25.7|19.6|1511|
|4|Mike Richards|C|31.5|11.6|43.0|17.2|26.5|16.5|1588|
|5|Joe Thornton|C|34.2|8.3|42.6|17.6|29.7|12.8|1547|
|6|Marc Savard|C|35.1|7.0|42.1|15.5|24.9|17.1|1176|
|7|Alex Burrows|LW|18.9|21.3|40.2|13.3|25.2|15.0|1252|
|8|Jonathan Toews|C|35.4|4.6|40.0|15.5|18.4|21.6|1377|
|9|Nicklas Lidstrom|D|23.4|16.5|39.8|25.9|21.1|18.7|1966|
|10|Nicklas Backstrom|C|30.6|7.7|38.3|18.4|9.1|29.2|1531|



Henrik tops the list in Table 3, while his twin brother Daniel is left out, but his ratings are the least reliable in the list.  The standard errors are a measure of the uncertainty in the APM estimates, and Henrik and Daniel have the highest standard errors in the league among forwards. The high errors are due to the fact that the twin brothers spend almost all of their time on the ice playing together, and the model has difficulty separating the contribution of the two players.  Daniel spent 92% of his time at even strength and 98% of his time on the power play playing with Henrik. 

Table 3: Top 10 Skaters in OPM 

|Rk|Player|Pos|OPM|DPM|APM|AErr|EVOPM|PPOPM|Mins|
|---|---|---|---|---|---|---|---|---|---|
|1|Henrik Sedin|C|47.8|-13.9|33.8|27.0|29.9|17.8|1487|
|2|Alex Ovechkin|LW|38.7|-1.5|37.2|22.3|29.7|9.0|1686|
|3|Pavel Datsyuk|C|37.8|14.5|52.2|20.9|30.6|7.9|1602|
|4|Ryan Getzlaf|C|37.1|8.7|45.8|19.6|19.7|17.4|1426|
|5|Sidney Crosby|C|36.4|-2.8|33.6|16.5|27.8|8.6|1423|
|6|Jeff Carter|C|36.1|9.2|45.3|15.7|20.9|14.2|1511|
|7|Jonathan Toews|C|35.4|4.6|40.0|15.5|20.0|13.9|1377|
|8|Marc Savard|C|35.1|7.0|42.1|15.5|14.5|20.6|1176|
|9|Evgeni Malkin|C|34.2|-5.0|29.2|17.9|24.6|9.6|1564|
|10|Joe Thornton|C|34.2|8.3|42.6|17.6|23.2|11.0|1547|



Our remaining tables are in the appendix.  We give the top 10 skaters in PPOPM/60 in Table 4. Recall that PPOPM/60 is a measure of the offensive contribution of a player during power play situations in terms of goals per 60 minutes.  The first thing to note is that since a typical NHL game is played mostly at even strength, there is much less data for the special teams model, and the resulting 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



ratings have much higher standard errors than the even strength ratings.  Excluding the Sedin twins, the standard errors in EVAPM/60 for a typical player are between 0.50 and 0.78, while for PPAPM/60 the errors are between 1.13 and 2.23.  The increased uncertainty in the PPAPM/60 ratings make the ratings less useful, and a priority in future research is to take measures to reduce errors for all estimates.  Nevertheless, the results are reasonable, as the players in Table 4 are all considered valuable contributors on the power play.  Nicklas Backstrom, for example, is an integral part of one of the most dangerous power play units in the league in Washington. 

Interestingly, most of these players seemingly fall into one of two categories:  (1) play-makers/power play quarterbacks, or (2) players who typically play in front of the net.  The only player who might be considered an elite shooter or goal scorer is Jeff Carter.  This trend is even more apparent in the list for PPOPM, and it would be interesting to study this trend further in an attempt to determine whether it is legitimate or just happened by chance. 

Next, we give the top 10 players in SHDPM/60 in Table 5.  Recall that SHDPM/60 is a measure of the defensive contribution of a player during shorthanded situations in terms of goals per 60 minutes of playing time.  Alex Burrows leads this list by a wide margin.  At even strength Burrows does not rate quite as highly, but he still ranks in the top 30 in EVDPM/60 among players with at least 700 minutes played at even strength.  His most common linemate during both even strength and shorthanded situations is Ryan Kesler.  For the past two years, Kesler has been a finalist for the Frank J. Selke Trophy, an award given to the best defensive forward in the NHL.  Interestingly, Burrows actually ranks higher than Kesler in our advanced defensive statistics EVDPM/60 and SHDPM/60, and also ranks higher in EVGA/60 and SHGA/60, which measure (unadjusted) goals allowed per 60 minutes in even strength and shorthanded situations, respectively. 

## **5   Concluding Remarks** 

The development of a special teams model and the inclusion of initial zones data were important improvements to our existing APM model.  As expected, the results from the special teams model were reasonable but were noisier than the results from the even strength model since there is much less data for special teams situations.  One could borrow ideas from APM models in basketball to help reduce the errors.  For example, the author is currently working a model similar to that in [4]. 

We finish with one hockey-specific idea.  One could attempt to use “weighted shots” as the dependent variable.  A particular shot can be weighted based on how often that kind of shot results in a goal.  The weights could be taken from [6], [7], or [8], where Ken Krzywicki develops a shot quality model which estimates the probability that a shot will be a goal based on shot type (slap, snap, wrist, etc.), shot distance, and other factors.  The number of shots in a typical NHL game is about 10 times the number of goals scored, and the extra data could help reduce noise in the estimates.  In [9], the authors use even more data by including (unweighted) shots and several other on-ice events in their model, and weight each event based on the probability that a goal scores within 10 seconds of that event. 

## **6   Acknowledgements** 

I would like to thank William Pulleyblank and Robert Wooster for reading a draft of this paper and for their comments and suggestions. 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



## **7   References** 

[1] Wayne L. Winston. Mathletics: how gamblers, managers, and sports enthusiasts use mathematics in baseball, basketball, and football. Princeton University Press, 2009. 

[2] Dan Rosenbaum. Measuring How NBA Players Help Their Teams Win, April 2004. <u>http://www.82games.com/comm30.htm.</u> 

[3] S. Ilardi and A. Barzilai. Adjusted Plus-Minus Ratings: New and Improved for 2007-2008, 2008. <u>http://www.82games.com/ilardi2.htm.</u> 

[4] Joe Sill. Improved NBA adjusted +/- using regularization and out-of-sample testing, March 2010. <u>http://www.sloansportsconference.com/research-papers/2010-2/past-years/improvednba-adjusted-using-regularization-and-out-of-sample-testing/.</u> 

[5] Brian Macdonald. A Regression-Based Adjusted Plus-Minus Statistic for NHL Players. Submitted, 2010. 39 pages. ArXiv preprint: http://arxiv.org/abs/1006.4310. 

[6] Ken Krzywicki. Shot quality model: A logistic regression approach to assessing nhl shots on goal, January 2005. http://www.hockeyanalytics.com/Research_files/Shot_Quality_Krzywicki.pdf. 

[7] Ken Krzywicki. Removing observer bias from shot distance - shot quality model - NHL - regular season 2008-09, September 2009. <u>http://www.hockeyanalytics.com/Research_files/SQ DistAdj-RS0809-Krzywicki.pdf.</u> 

[8] Ken Krzywicki. Nhl shot quality 2009-10: A look at shot angles and rebounds, October 2010. <u>http://hockeyanalytics.com/2010/10/nhl-shot-quality-2010/.</u> 

[9] Michael Schuckers et al. National hockey league skater ratings based upon all on-ice events: An ad~ justed minus/plus probability (ampp) approach, 2009. <u>http://myslu.stlawu.edu/ msch/sports/ LockSchuckersProbPlusMinus113010.pdf.</u> 

MIT Sloan Sports Analytics Conference 2011 March 4-5, 2011, Boston, MA, USA 



## **8   Appendix** 

Table 4: Top 10 Skaters in PPOPM/60 

|Rk|Player|Pos|PPOPM|PPDPM|PPAPM|PPAErr|EVOPM|PPMins|
|---|---|---|---|---|---|---|---|---|
|1|Nicklas Backstrom|C|5.09|0.52|5.61|1.48|0.20|312|
|2|Marc Savard|C|5.05|-0.84|4.21|1.78|0.94|244|
|3|Brenden Morrow|LW|4.49|0.19|4.68|1.65|0.24|228|
|4|Jeff Carter|C|4.01|-0.11|3.90|1.69|1.13|213|
|5|Ray Whitney|LW|3.67|0.16|3.83|1.41|0.24|311|
|6|Ryan Getzlaf|C|3.64|0.69|4.33|1.66|1.04|288|
|7|Andrei Markov|D|3.55|0.02|3.57|1.59|0.68|318|
|8|Todd White|C|3.49|0.09|3.58|1.46|0.33|233|
|9|Saku Koivu|C|3.46|0.22|3.68|1.52|0.37|223|
|10|Henrik Sedin|C|3.46|-0.29|3.17|2.73|1.53|309|



Table 5: Top 10 Skaters in SHDPM/60 

|Rk|Player|Pos|SHOPM|SHDPM|SHAPM|SHAErr|EVDPM|SHMins|
|---|---|---|---|---|---|---|---|---|
|1|Alex Burrows|LW|0.83|3.27|4.10|1.63|0.54|219|
|2|Chris Kelly|C|-0.61|2.74|2.14|1.55|-0.06|256|
|3|Vernon Fiddler|LW|-0.12|2.16|2.04|1.54|-0.27|211|
|4|Nick Schultz|D|0.06|2.08|2.14|1.85|0.35|237|
|5|Dan Girardi|D|-0.26|1.95|1.70|1.81|-0.34|227|
|6|Blair Betts|C|-0.15|1.89|1.74|1.66|0.65|209|
|7|Jeff Schultz|D|-0.27|1.88|1.61|1.46|0.21|208|
|8|Kim Johnsson|D|-0.60|1.84|1.24|1.82|0.04|212|
|9|Zdeno Chara|D|-0.65|1.80|1.16|1.47|0.05|249|
|10|Marty Reasoner|C|-0.19|1.67|1.47|1.33|0.33|262|




