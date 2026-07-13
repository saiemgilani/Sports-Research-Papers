<!-- source: 2013 To Crash or Not To Crash A quantitative look at the relationship between offensive rebounding and transition defense in the NBA.pdf -->



# **To Crash or Not To Crash:** 

**A quantitative look at the relationship between offensive rebounding and transition defense in the NBA** 

Jenna Wiens, Guha Balakrishnan, Joel Brooks, John Guttag Massachusetts Institute of Technology, Cambridge, MA, USA, 02139 Email: jwiens@mit.edu 

## **Abstract** 

Immediately following a missed shot an offensive player can choose to crash the boards for an offensive rebound, get back on defense, or hold their current position. In this paper, we use optical tracking data to develop novel metrics to summarize a team’s strategy immediately following a shot. We evaluate each metric using data from the 2011-2012 NBA season. Our results confirm that getting back on defense and neutralizing threats early in the possession contribute to a defensive success. However, tendencies to get back early on defense after a missed shot can reduce a team’s probability of getting an offensive rebound by more than half. 

## **1   Introduction** 

The American General George S. Patton had a simple philosophy of war, "When in doubt, attack."  The 1st Duke of Wellington had a more nuanced view.  A great general, he said, should "know when to retreat, and to dare to do it." When it comes to offensive rebounding in the NBA, some coaches take a Patton-like approach--they want their players to attack the offensive boards at every opportunity.  Other coaches emphasize the importance of retreating to a strong defensive position. When the offense sends more players toward the basket when a shot is taken, that team has a better chance of securing an offensive rebound [1].  But sending too many players in to rebound might impede the ability of a team to get back quickly on defense. This paper provides steps toward understanding and quantifying the tradeoff between offensive rebounding and transition defense. 

Figure 1 highlights a possession in a game between Boston and New Jersey.  As soon as the ball is released the three offensive players closest to the basket decide to crash. In this instance Boston gets the offensive rebound. This clip is somewhat unusual since more often than not Boston retreats after a shot goes up, readying their defense for the next possession. The tradeoff between these two opposing strategies is complex. Current popular metrics often quoted by analysts, such as offensive rebound rate and transition points allowed offer no insight into what strategic choices influence a team’s performance. 





**Figure 1: These frames are extracted from a game between the New Jersey Nets and the Boston Celtics form March 2**<sup>**nd**</sup> **2012 [2]. In the frame on the left we see a field goal attempt from the Celtics. The frame on the right is taken 1 second after Paul Pierce releases the shot. From the time the shot was released three players have moved closer to the basket.  Players don’t have much time to decide what they will do after a shot is released, but what they do decide can have a significant impact on the outcome of the game.** 



2013 Research Paper Competition Presented by: 





In this paper, we attempt to quantify this trade-off using data from the STATS SportVU system [3], which contains data from 233 games from the 2011-2012 season (including playoffs). This dataset contains all the {x,y} positions of every player on the court and the {x,y,z} coordinates of the ball at 25 frames per second. We develop several new metrics based on the positioning of teams after a missed shot. These metrics are shown to relate to outcome (though in different ways), and may be used by teams to evaluate defensive (and offensive) strategies. 

## **2   What Teams Gain by Crashing** 

Player movement immediately following the release of a shot (as in Figure 1) can have an impact on not only who gets the rebound if the shot is missed, but also the result of the next possession (if the other team gets the defensive rebound). To test this hypothesis we consider all missed field goals taken at least 15ft from the basket.  Our final dataset consists of 6,521 instances of missed jump shots. For each instance we consider the {x,y} positions of every offensive player on the court in relation to the basket at the time the shot is released (the blue markers in Figure 2) and at the time the rebound is secured (the red markers in Figure 2). We define _reaction time_ as the total time from when the shot is released to when the ball is rebounded. The mean reaction time in our dataset was approximately 2.22s (standard deviation of 0.65 seconds). 

To determine a player’s intention to get the offensive rebound it is not enough to simply consider the movement of players in relation to the basket. Some players who are close to the basket may actually move slightly _away_ from the basket in order to gain a better position. Players far away from the basket may not even consider crashing since the probability of getting the rebound is so low. We characterize the positioning and movement of players during the reaction time using the following four metrics: 



<!-- Start of picture text -->
4 1<br>33ft<br>8ft<br>2<br>5<br>3<br><!-- End of picture text -->



<!-- Start of picture text -->
Figure 2: We consider the movement<br>of offensive players immediately<br>following a missed jump shot. The<br>red markers indicate the position of<br>players at the time the ball is released.<br>The blue markers indicate their<br>position at the time of the rebound.<br><!-- End of picture text -->

**Figure 2: We consider the movement of offensive players immediately following a missed jump shot. The red markers indicate the position of players at the time the ball is released. The blue markers indicate their position at the time of the rebound.** 

- _Number of Players Inside_ (PI) – the number of players positioned 8 feet from the basket when the shot is released 

- _Numbers of Players Outside_ (PO) – the number of players positioned more than 33 feet from the basket when the shot is released 

- _Number of Neutral Players who Crash_ (NPC) –the number of players initially positioned between 8 and 33 feet from the basket who move at least 5 feet t **oward** the basket 

- _Number of Neutral Players who Retreat_ (NPR) – the number of players initially positioned between 8 and 33 feet from the basket who move at least 5 feet **away from** the basket 

In addition we define two summary statistics: 

- _Crash Index_ (CI) = PI+NPC 

- _Retreat Index_ (RI) = PO+NPR 

Figure 2 is an example of Golden State’s offensive positioning and movement during the reaction time after a jump shot. In this instance Golden State has PI=1, NPC=1, NPR=3 and PO=0, and was successful in securing the offensive rebound. 

We begin by considering how these metrics relate to the probability of getting the offensive rebound. Considering all 6,521 possessions, we vary the NPC from 0 to 3 and the PI from 0 to 2. There were a few cases where CI=4, but these were removed since the number of instances was so low. All other combinations had at least 100 examples. Figure 3 (a) shows that the probability of getting the offensive rebound is greatest when PI=2 and NPC=1. Unsurprisingly the offensive rebounding rate increases as PI and NPC increase. Figure 3(b) shows the probability of getting the offensive rebound is greatest when no one retreats and 3 players crash.  It is important to note that this figure shows an _association_ between the number of players who crash and the probability of getting an offensive rebound.  It does not show that crashing the boards _causes_ offensive rebounds.  It is possible that more players crash when it appears that getting an offensive rebound is there for the taking. 





2013 Research Paper Competition Presented by: 





<!-- Start of picture text -->
0.4<br>0.35<br>0.3<br>0.25<br>0.2<br>0.15<br><!-- End of picture text -->



<!-- Start of picture text -->
(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
0.4<br>0.35<br>0.3<br>0.25<br>0.2<br>0.15<br>0.1<br>0.05<br><!-- End of picture text -->





<!-- Start of picture text -->
(b)<br><!-- End of picture text -->

**Figure 3: The probability of getting an offensive rebound as a function of (a) NPC & PI and (b) CI & RI. As you increase PI and NPC the probability increases, however increasing RI always results in a lower probability.** 

For each team we consider all possessions where a missed jump shot occurs, and calculate the fraction of time CI>RI (more players crash than retreat), and the offensive rebounding rate. We believe that the fraction of time CI>RI is indicative of the relative importance a team places on offensive rebounding or transition defense. We plot the results of this analysis in Figure 4. Note that the SportVU system is not installed in all arenas. Therefore, there are some teams for which we have little data. To avoid confusing the signal with the noise we do not plot results for teams for which we have fewer than 150 examples of a missed jump shot. Figure 4 indicates a strong association between CI>RI and offensive rebounding. 



<!-- Start of picture text -->
0.3<br>0.28 HOU<br>0.26<br>WAS<br>TOR<br>0.24 NYK MIA<br>MIL<br>0.22 GSW SAS IND MIN<br>0.2 OKCPOR<br>0.18<br>0.25 0.3 0.35 0.4 0.45<br>CI>RI Rate<br>Offensive Reb. Rate<br><!-- End of picture text -->

**Figure 4: Considering possessions grouped by teams, we again note a relationship between CI & RI and the offensive rebounding rate (for missed jump shots in our data). The number of possessions we have for each team varies from 151 to 622, here the size of the markers indicates the number of possessions.** 

Moving toward the basket immediately following a missed shot seems to increase a team’s probability of getting the offensive rebound, but still even the best offensive rebounding percentage is much less than 50%. I.e., following a missed jump shot, a defensive rebound by the other team is always more likely. The data shows that most of the time a team’s RI is greater than its CI (42% of the time RI>CI, 32% of time CI>RI). Does sending players back early affect the result of the next defensive possession? 

To address this question we consider all missed shots that result in a defensive rebound by the other team and the outcome of the next possession. We assign a 0 to possessions that result in either a made shot or an attempted free throw, and +1 to the other possessions. Here, a positive outcome is good for the team that just missed a field goal. 



<!-- Start of picture text -->
7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>0−2 2−4 4−6 6−8 8−10 10−12 >12<br>Possession Length<br>Odds Ratio<br><!-- End of picture text -->

**Figure 5: The positive effect of retreating immediately following the release of a shot (assuming the other team gets the defensive rebound) is transient.** 2013 Research Paper Competition 

2013 Research Paper Competition Presented by: 







For each possession we calculated the RI of the offensive team, and grouped possessions into high and low RI (upper quartile and lower quartile). We measure the probability of a positive event occurring in both groups. Figure 5 shows the impact of a team’s movement immediately following the release of a shot makes in terms of outcome (assuming a missed offensive rebound). For each bin we calculate the odds ratio (Eq. 1). 

Odds Ratio = Pupper(+1)*Plower(0)/(Plower(+1)*Pupper(0) **Eq. 1** 

As the length of the possession increases, the odds ratio decreases. Figure 5 implies that movement away from the basket immediately following the release of the shot has the greatest impact on short possessions. I.e., the effect is transient. But what is the team giving up in return for limiting transition baskets? 

Again we consider the movement of offensive players immediately following a missed shot, but in addition we consider the outcome of what happens next. If an offensive rebound occurs, any points scored during this possession count as a gain. If a defensive rebound occurs, any points scored on the next possession count as a loss. By averaging over all possessions we can compute the net gain of all missed shots (Eq. 2) 

Net Gain = P(Offensive Rebound)*Avg. Pts. For – P(Defensive Rebound)*Avg. Pts. Against **Eq. 2** 

Table 1 shows the average net gain (points/possession) as a function of CI and RI. In all cases, the net gain is negative, i.e., missed shots are bad. On average a missed shot results in -0.549 points per possession. 

**Table 1: Net gain of missed shot broken down by CI and RI. Offensive rebounding rates are given in parentheses. We consider only scenarios for which we have at least 100 possessions. The shaded area represents the most probable scenarios (over 500 instances each).** 

||0<br>|Crash In<br>1<br>|dex<br>2<br>|3<br>|
|---|---|---|---|---|
|0|%0.83(0.21)|%0.49(0.27)|%0.22(0.34)|%0.12(0.40)|
|at<br>x<br>1|%0.69(0.15)|%0.53(0.21)|%0.45(0.29)|%0.09(0.36)|
|etre<br>nde<br>2|%0.76(0.11)|%0.62(0.19)|%0.46(0.27)|%0.36(0.31)|
|R<br>I<br>3|%0.97(0.08)|%0.85(0.15)|%0.40(0.28)||
|4|%1.08(0.04)|%0.50(0.12)|||



Notice that it appears that a team can mitigate the effect of missed jump shots by sending more players to crash. Considering only the most probable scenarios (the shaded region in Table 1) we can increase the net gain from -0.62 (CI=1 & RI=2) to -0.45 (CI=2 & RI=1) just by swapping the role of a single player. This change results in a net gain of 0.17 pts/possession. If a team misses on average 25 jump shots per game this could translate to a possible gain of 4 points per game. 

We investigated which teams were doing this already, by considering the ratio of the number of times teams found themselves in each scenario. We plot this ratio vs. the average net gain per team in Figure 6. Here we consider only teams for which we had at least 100 possessions (that meet our inclusion criteria) worth of data. 

Admittedly this analysis does not account for the personnel on a team. For example, some teams may not have two good rebounders. In such a case sending two players to crash and one player to retreat might not have the same expected gain as it does when we consider aggregate data from all teams.  This is an opportunity for further analysis. 

Still our results suggest that in general focusing on the offensive rebound immediately after the shot goes up seems to trump the gain a team gets with a head start on getting back. In the next sections we investigate how a team’s movement _after_ the ball is rebounded impacts the outcome of a possession immediately following a missed offensive rebound. 





2013 Research Paper Competition Presented by: 





<!-- Start of picture text -->
−0.3 WAS<br>NYK<br>−0.4<br>HOU<br>SAS<br>−0.5 MIL<br>MIN<br>−0.6<br>TOR<br>−0.7 GSW<br>0.8 1 1.2 1.4 1.6 1.8 2<br>(CI=2 & RI=1)/(CI=1 & RI=2)<br>Average Net Gain (pts./possession)<br><!-- End of picture text -->

**Figure 6: Washington and Houston already appear to be doing the optimal thing after a missed jump shot (at least in the games for which we had data), while Toronto and Golden State could improve their strategy.** 

## **3   Early Threat Neutralization** 





<!-- Start of picture text -->
7 10 5<br>2<br>1 8 3<br>6<br>4 9<br><!-- End of picture text -->



<!-- Start of picture text -->
7 5 10<br>2<br>1 8 3<br>6<br>4 9<br><!-- End of picture text -->

**(a).  Good threat neutralization (b). Bad threat neutralization** 

**Figure 7:  Illustration of threat neutralization, where offense is marked with ‘o’ and defense is marked with ‘x’.  Player 10 of the offensive team has just come within his threatening distance (red arc).  (a) shows an example of good neutralization, where the distance between Player 10 and the closest defender (Player 5) is small.  (b) shows an example of bad neutralization.** 

The previous measures do not quantify how well a team prevents its opponents from entering a threatening offensive position after a defensive rebound.  Simply retreating to the defensive end of the court is not sufficient. We developed the maximum distance to early threats (MDET) score to measure this element of defense.  Figure 7 illustrates the intuition of the MDET score.  The first time an offensive player is within a threatening distance to the basket in the first five seconds of his team’s possession, we measure his distance (in feet) to the closest defending player.  We compute a distance for each offensive player that becomes a threat during the possession and use the maximum of these distances as the MDET score.  The maximum distance represents the most “open” player during the early portion of the possession.  Note that a lower MDET score indicates better neutralization. 



<!-- Start of picture text -->
140<br>120<br>100<br>80<br>60<br>40<br>20<br>0<br>0 10 20 30<br>Offensive Threat Range (ft)<br># of players<br><!-- End of picture text -->

Offensive threat range varies by player.  A center like Dwight Howard should be considered an offensive threat at a much closer distance to the basket than a 3-point shooter like Ray Allen.  Therefore we set an offensive player’s threat range based on the distribution of his shot distances in the data.  We found that using the 75<sup>th</sup> percentile of a player’s shot distance distribution works well.  Figure 8 plots the offensive threat ranges for all the players in the data. As expected, this distribution is somewhat bimodal, with high density around 15 and 23 ft. 

We compare MDET with defensive outcome by considering all continuous **Figure 8: Distribution of** possessions (i.e. possessions without a stoppage in the middle) following a **offensive threat range across all** defensive rebound. During our analysis we found that the MDET did not **players. A significant number of** have a significant effect on the outcome of possessions greater than 15 **players are not considered a threat outside of 16 ft.** seconds in length. This is similar to the trend we saw with RI and outcome; the effect appears to be transient. Thus in following analysis we consider only 

possessions less than 15 seconds. This includes possessions that end in free throws since a poor defensive effort can lead to defensive fouls.  In total, we had 10,915 possessions.  We computed the MDET score for each defensive possession and recorded a binary outcome (1 = opponent did not score, 0 = opponent scored or got to the free throw line).  Figure 9 plots the MDET distribution for each outcome.  Using the Kolmogorov-Smirnov test, we 





2013 Research Paper Competition Presented by: 



found that the two distributions were significantly different (p < 0.01).  Looking at the distributions, we see that outcome 1’s distribution is shifted toward lower MDET values than outcome 0.  The mean MDET score for outcome 1 was 9.05 ft and the mean score for outcome 0 was 9.63 ft. 



<!-- Start of picture text -->
0.25 Outcome 0 1.4<br>Outcome 1<br>0.2 1.3<br>0.15 1.2<br>0.1 1.1<br>0.05 1<br>0 0.9<br>0 2 4 6 8 10 12 14 16 18 20 2 4 6 8 10 12 14 16 18<br>MDET MDET<br>Figure 9: MDET distributions for outcomes  Figure 10: Points allowed per possession vs.<br>0 and 1.   MDET<br>Fraction of possessions<br>Points Allowed Per Possession<br><!-- End of picture text -->



<!-- Start of picture text -->
Figure 9: MDET distributions for outcomes<br>0 and 1.<br><!-- End of picture text -->

**Figure 10: Points allowed per possession vs. MDET** 

These results are consistent with the intuition that better threat neutralization can prevent transition baskets on defense.  Figure 10 displays the number of points allowed per possession versus MDET.  An increase of MDET from 6 to 12, for example, leads to roughly 0.06 more points allowed per possession after a defensive rebound. Based on the dataset, there are about 25 possessions for a team per game that are continuous and follow a defensive rebound.  It follows that a difference of 0.06 points per possession could change an opponent’s score by 1.5 points 

## **4   Early Threat Neutralization vs. Crashing/Retreating** 

Finally, we investigate how early threat neutralization relates to offensive rebound crashing.  We hypothesized that having more players crash the boards will worsen threat neutralization performance since a player that crashes must run a longer distance to get back on defense.  To test this hypothesis we considered all possessions in which a team missed a shot and did not get the offensive rebound and for which the following possession lasted at most 15 seconds.  We then compare how the number of players crashing and retreating relates to MDET. Figure 11 shows that MDET tends to increase with an increase in RI and decrease with an increase in CI.  These results are in agreement with our hypothesis that there is a tradeoff between offensive rebounding and getting back on defense. 



<!-- Start of picture text -->
9.9 CI<br>RI<br>9.8<br>9.7<br>9.6<br>9.5<br>9.4<br>9.3<br>1 2 3 4<br># of players who crash<br>MDET<br><!-- End of picture text -->

**Figure 11: Comparison of CI and RI to MDET** 

## **5   Conclusion** 

In this paper we study optical tracking data in an attempt to quantify the tradeoff of going for the offensive rebound vs. getting ready for the transition to defense. 

We analyzed the relationship between the movements of players when a shot is in the air and a team’s ability to garner offensive rebounds.  We defined two new metrics the Crash Index (CI) and Retreat Index (RI) that quantify the extent to which teams pursue an offensive rebound or ready themselves for transition defense. We also looked at what the offense does after the other team secures the defensive rebound. In doing so we introduced another metric, the maximum distance to early threats (MDET), designed to measure the effectiveness with which players defend during the transition period. We showed that there is a strong association between each of these three metrics and points/possession. 

In conclusion, our results suggest that focusing on the offensive rebound immediately after the shot goes up seems to trump the gain a team gets with a head start on getting back. In the case of a defensive rebound by the other team early threat neutralization (as opposed to merely getting back early) can help limit the negative impact of transition baskets. The generalizability of these conclusions is limited by the data. For some teams we lacked data. Moreover, there are many factors we have yet to consider, e.g. the positioning of the defensive players, the game situation and especially the personnel on the floor. 

**Acknowledgements.** We would like to thank STATS LLC for sharing their data, and Mike Zarren for all his help. 





2013 Research Paper Competition Presented by: 



## **6   References** 

[1] Maheswaran, Rajiv, et al. “Deconstructing the Rebound with Optical Tracking Data”. _MIT Sloan Sports Analytics Conference 2012._ March 2012. 

[2] http://www.youtube.com/watch?v=PfhGqe3IoMU 

[3] STATS SportsVu, http://www.sportvu.com/ 





2013 Research Paper Competition Presented by: 


