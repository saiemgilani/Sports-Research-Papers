<!-- source: 2013 Using Zone Entry Data To Separate Offensive, Neutral, And Defensive Zone Performance.pdf -->



# **Using Zone Entry Data To Separate Offensive, Neutral, And Defensive Zone Performance** 

Eric Tulsky, Geoffrey Detweiler, Robert Spencer, Corey Sznajder Berkeley, CA, USA, 94707 Email: bsh.erict@gmail.com 

## **Abstract** 

Separating a hockey player’s offensive and defensive contributions is quite difficult. Offensive skill can lead to increased puck possession and therefore improve statistics aimed at measuring defensive performance such as goals or shots allowed. This challenge can be overcome by measuring goals or shots per possession rather than per game, provided a reasonable estimate of possessions is available. Recording when the puck is brought across the blue line makes this transformation possible, enabling a true assessment of performance in the offensive or defensive zone. Surprisingly, a season of data shows no clear separation between players in shot production or suppression; if offensive stars generate more shots per offensive zone possession than fourth line grinders, the difference is small enough to not show up in a single season’s data. Instead, the team’s shot differential – which has been shown to be a strong predictor of wins – is determined almost entirely in the much less-heralded neutral zone. Neutral zone success involves more than getting extra zone entries; since carrying the puck across the blue line generates more than twice as many shots, scoring chances, and goals as dumping the puck in, gaining the zone with possession is a major driver of success. 

## **1   Introduction** 

Hockey outcomes are often divided into components of shot differential and shot quality; the latter can be easily and meaningfully divided into offensive and defensive components, but it is widely thought to be the lesser driver of outcomes in the long run.[1-3] Shot differential is the primary driver of outcomes in today’s NHL, but separating out offensive and defensive contributions to shot differential is difficult since an offensively gifted player might prolong his team’s possessions and thereby suppress the opposing team’s shot total. 

The result is that while most analysts agree that shot differential plays a critical role in determining outcomes of games, statistically breaking things down further to assess how a player drives shot differential relies on inferences and assumptions. For example, defensive skill is often inferred from the assumption that a player whose coach puts him on the ice against good opponents for defensive zone faceoffs is good at defense. 

To really understand whether a player who allows few shots or goals is achieving this result through good defense or by playing a puck possession game that gives the opponent fewer opportunities, we need to shift from shots or goals per game to shots or goals per possession. Achieving this transformation requires some data that is not tracked by the NHL, but can easily be recorded in real time by a dedicated observer. Recording zone entries allows us to separate out performance in each zone and with over 300 games from the 2011-12 NHL season tracked, it is possible to identify both skills and strategy that lead directly to a team’s success. 

## **2   Data Collection and Assessment** 

Each time a team advanced the puck into the offensive zone, the observers recorded a few key parameters: 

- The time on the clock 

- The player who sent the puck into the zone 

- The method of entry (e.g. carrying the puck in with possession, dumping it into the zone and trying to recover it, or miscellaneous other entries such as shots on goal from the neutral zone) 

This data was then merged with the official play-by-play, breaking the game into a series of segments from one zone entry or offensive zone faceoff to the next. The number of shots (including those that miss the net) and goals produced in each offensive zone possession were extracted from the play-by-play. This permitted assessments of 





2013 Research Paper Competition Presented by: 



each player’s contributions with the puck; to additionally identify defensive and off-puck offensive contributions, the list of players on the ice at the time of each zone entry was obtained from the official shift charts. 

In this manner, 330 games were tracked, covering a full season for the Flyers and Wild, a half-season for the Capitals and Sabres, and approximately 7-10 games for most other teams. 

For any manually-tracked data, it is important to assess the potential impact of scorer variability. Subjective assessments such as scoring chance counts can show major differences across scorers.[4] Since the puck crossing the blue line is a discrete, objective event, zone entry counts might be expected to be less problematic, but the scorers do still have a few decisions to make. The difference between carrying the puck in and dumping it in is usually clear, but the line between a pass with possession and a dump-in is occasionally tricky, as are some miscellaneous entries (e.g. when a player carries the puck back into his own zone and then turns it over). Additionally, since the goal is to assess offensive and defensive performance, plays where the offense dumps the puck in and goes for a line change without making any attempt to recover the puck were excluded, which introduces a bit more subjectivity. 

Several games were tracked by multiple observers. Comparing zone entry data from those games permits assessment of the integrity of the data and the viability of comparisons across data sets. Correlation matrices are given in Figure 1, indicating how often observers agreed on a given entry (more than 85% of the time) and what the most common discrepancies were (nearly two-thirds were when one observer omitted an entry that another recorded). 

|||Recorded|by GD|||||Recorded|by CS|||||Recorded|by CS||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||Carry|Dump|Misc|Omit|||Carry|Dump|Misc|Omit|||Carry|Dump|Misc|Omit|
|Carry<br>RS|74|5|2|0|RS|Carry|160|11|2|15|GD|Carry|289|32|1|25|
|Dump<br>ded by|7|47|4|4|ded by|Dump|12|153|12|60|ded by|Dump|11|161|19|41|
|Misc<br>Recor|0|3|2|0|Recor|Misc|4|1|2|4|Recor|Misc|0|1|3|6|
|Omit|3|7|3|–||Omit|10|16|1|–||Omit|18|28|3|–|



**Figure 1.** Correlation matrices for comparing observer recording tendencies. 

The only significant scorer bias appears to be in the number of entries omitted; the distribution of entry types was consistent across observers and there was no apparent tendency for an observer to record his favorite team differently from what a fan of the opponent would record. Dump-and-change plays were explicitly tracked for Capitals games and were typically accompanied by having four offensive players leave the ice within five seconds. Therefore, subjectivity around omissions could be removed by recording every dump-in and algorithmically removing the dump-and-change plays from the NHL shift chart. 

## **3   Importance of Entering the Offensive Zone with Possession** 

It would be a mistake to simply use shots per entry as the measure of offensive zone success, because there is an aspect of neutral zone performance that can impact the offensive zone results. A team that moves the puck through the neutral zone most effectively will be able to enter the offensive zone with possession, carrying the puck across the blue line. This might be expected to result in more shots and goals than a play where the team dumps the puck into the corner hoping to retrieve it, so we must first assess the impact of this neutral zone outcome before judging the offensive zone performance. 

|**Table 1.**Shots and<br>Each table e|goals generat<br>ntry is based<br>Sh<br>|ed by carrying<br>on at least 300<br>ots<br>|or dumping t<br>0 5-on-5 entr<br>G<br>|he puck in.<br>ies.<br>oals<br>|
|---|---|---|---|---|
||Puck<br>carried in|Puck<br>dumped in|Puck<br>carried in|Puck<br>dumped in|
|PHI entries for|0.55|0.24|0.039|0.017|
|PHI entries against|0.58|0.25|0.037|0.012|
|MIN entries for|0.58|0.26|0.031|0.010|
|MIN entries against|0.60|0.28|0.027|0.015|
|WSH entries for|0.56|0.25|0.035|0.014|
|WSH entries against|0.54|0.22|0.037|0.013|
|BUF entries for|0.53|0.24|0.032|0.018|
|BUF entries against|0.59|0.26|0.038|0.010|
|Rest of league|0.62|<br>0.28|<br>0.035|<br>0.015|



Indeed, the difference between a zone entry with possession and a dump-in is quite substantial. As Table 1 shows, every data set collected showed entries with possession being more than twice as effective as dump-ins at 5-on5. The neutral zone play that sets a team up to enter the offensive zone with possession is a critical driver of success. 

It is clear that any assessment of offensive zone performance must 

2013 Research Paper Competition Presented by: 







account for the influence of the neutral zone play that initiates the offensive zone possession. 

## **4   Zone Performance Scores** 

A zone performance score can be produced by establishing how far above or below average a team’s share of the shots would be given their actual performance in that zone and league-average performance in the other zones: 

|<br>  ( )<br>|
|---|
|<br>  ( )     ( )<br>|
|( )<br>|
|( ) ( )<br>|



Here, Sh_EWP = shots per entry with possession, Sh_EWoP = shots per entry without possession, EWP = entries with possession, EWoP = entries without possession, EWP% = percent of the team’s entries that are with possession, an O at the start of a term means it is the result allowed to the team’s opponents, and an asterisk superscript means the league average for that metric. Despite the dense abbreviations, the approach is relatively simple in concept. The offensive zone score is just a function of shots per entry with possession and shots per entry without possession, the defensive zone score is a function of the opponents’ shots per entry of each type, and the neutral zone score is a function of how many of each type of entry the team gets and allows. 

The neutral zone scores for the teams with at least 40 tracked games were: Flyers 51.1%, Sabres 50.6%, Capitals 49.3%, and Wild 45.7%. The spread was smaller for offensive and defensive zone performances, with all eight numbers falling between 48.8% and 51.0%. This grouping is narrow enough that differences could be impacted by a scorer’s tendency to omit more entries, as fewer recorded entries would raise the number of shots per entry and thereby increase offensive zone score and decrease defensive zone score. This study was performed with a single observer recording the bulk of the games for a given team, so without enough games in common to prepare accurate correction factors, comparing the offensive and defensive zone scores across teams will be difficult. 

However, comparison of players on a team can come from calculating the team’s performance score with a given player on the ice; in such intra-team comparisons, any scorer bias would be neutralized. Figure 2 illustrates the relationship between some reasonable measures of a Flyers forward’s skill and his offensive zone performance score. As shown in the top-right panel, the correlation between average ice time per game (which should relate to overall skill) and point scoring rate (a measure of offensive skill) is very strong. However, very little correlation is observed between either of those measures and the player’s offensive zone score. Similar results were observed for the Wild forwards, and the defensive zone score of the defensemen showed no clear correlation with the measures commonly used to rank defensemen. These unexpected results call for further analysis of statistical significance. 



A split half reliability test can help assess the extent to which our offensive and defensive zone scores represent a true talent, whether the surprising rankings in the zone performance scores are highlighting undervalued players or warning us that these data are dominated by noise. Table 2 shows that for the Flyers and Wild games, only the neutral zone score is consistently meaningful at the half-season level. 

**Figure 2.** Scatterplots comparing offensive zone score, scoring rate, and ice time. Only the scoring rate/ice time (top-right) correlation is strong. 





2013 Research Paper Competition Presented by: 



**Table 2.** Correlations between odd and even games for many metrics that come out of zone entry data. Shaded cells indicate a correlation that exceeds a 95% significance threshold for the number of data points in question. 

||Flye<br>|rs correla<br>|tion<br>|Wil<br>|d correla<br>|tion<br>|
|---|---|---|---|---|---|---|
|Metric|F|D|All|F|D|All|
|Fraction of aplayer’s entries that are withpossession|**0.8**|**0.9**|**0.9**|**0.8**|0.4|**0.9**|
|Team’s shotsper timeplayer carriespuck into zone|<0|0.2|0|<0|0.3|0|
|Team’s shotsper timeplayer dumpspuck into zone|<0|0|<0|0|0.2|0.1|
|Team’s entrydifferential withgivenplayer on ice|0.4|**0.9**|**0.5**|**0.6**|**0.8**|**0.6**|
|% of team’s entries that are withpossession w/player on ice|**0.9**|0.3|**0.9**|**0.8**|0.2|**0.7**|
|Team’s shotsper entryw/possession w/givenplayer on ice|0|0|<0|<0|<0|<0|
|Team’s shotsper dump-in withgivenplayer on ice|<0|0.5|0.1|0.3|<0|0.1|
|% of opponent’s entries that are withposs. w/player on ice|0|**0.7**|0.2|0.4|0|0.3|
|Opp’s shotsper entryw/possession w/givenplayer on ice|0.2|0.4|<0|0.3|0.4|0.4|
|Opp’s shotsper dump-in withgivenplayer on ice|0.4|<0|<0|**0.6**|**0.7**|**0.5**|
|Overall offensive zoneperformance score|<0|0.2|<0|<0|0|<0|
|Overall defensive zoneperformance score|0.4|<0|0.2|0.4|**0.6**|0.4|
|Overall neutral zoneperformance score|**0.5**|**0.7**|**0.5**|**0.6**|0.5|**0.6**|



Offensive zone scores appear to be essentially completely random. Defensive zone scores show a very weak persistence which does pass a 95% significance test for the Wild defensemen. However, caution is needed here, as enough correlations are being calculated that one might expect a couple of false positives. The relationship between ice time and defensive zone score is shown in Figure 3; the strong inverse relationship again suggests that either the Wild were giving the most playing time to the defensemen who play the worst in the defensive zone (which seems unlikely) or the differences over this sample size are dominated by noise and this is a false positive. The most likely conclusion is that the shots-per- 



<!-- Start of picture text -->
23:00<br>22:00<br>21:00<br>20:00<br>19:00<br>18:00<br>17:00<br>43% 44% 45% 46% 47% 48% 49% 50% 51% 52%<br>Defensive zone performance score<br>Average TOI per game<br><!-- End of picture text -->

**Figure 3.** Scatterplot comparing defensive zone score to average ice time for Wild defensemen. 

possession component of shot differential is heavily driven by luck at the single-season level. This is consistent with the reliability test outcomes of all other measures and helps explain why the differences between teams were small. 

However, it is well-established that shot differential does represent a true talent and an important distinguisher of superior players and teams. Surprisingly, the talent component of shot differential seems to come almost entirely from the neutral zone play, as metrics like entry differential and fraction of entries with possession clearly show reproducible differences from player to player and that collection of talent presumably drives the large differences between teams in neutral zone score. 

Metrics which are based on a team’s shot differential are often referred to as “possession metrics” because they correlate strongly with puck possession and zone time, but it has never previously been established how players achieve that goal. It now seems clear that the strong correlation is more than incidental, that the teams that achieve good shot differential do so precisely by controlling puck possession, winning the neutral zone more than their share to get extra offensive zone possessions, and winning it decisively enough to maintain puck possession as they enter the offensive zone. 

## **5   Puck Handling** 

Almost everything discussed to this point has revolved around team performance; even the individual performance scores were based on what the team did with that player on the ice. In addition, since the observers recorded which player sent the puck into the offensive zone, it is possible to extract some data about player puck handling. 





2013 Research Paper Competition Presented by: 



Two metrics were developed for this purpose. A player’s responsibility for advancing the puck through the neutral zone can be calculated by dividing the number of times he personally pushes the puck into the offensive zone by the number of zone entries his team has when he is on the ice. His success in those entries can be assessed by looking at what fraction of his individual zone entries are with possession rather than by dumping the puck into the zone. 



<!-- Start of picture text -->
75% 68<br>70% Flyers<br>Wild 28<br>65% 48 93<br>7<br>60% 2421 96<br>15<br>55% 10 19 9<br>50% 10<br>36 17<br>21 22<br>45% 14<br>40% 27 25<br>43 18<br>35% 48 16<br>14<br>30%<br>14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36%<br>Player involvement<br>Of the team's entries with him on the ice, how often was he the one sending the puck in?<br>Player results<br>How often did he retain possession on his zone entries?<br><!-- End of picture text -->

<mark>14</mark> Figure 4 shows the relationship 30% between these metrics for the 14% 16% 18% 20% 22% 24% 26% 28% 30% forwards on the Flyers and Wild. **Player involvement** _Of the team's entries with him on the ice, how often was he the one sending the puck in?_ Several things stand out in this plot. It is clear from the overall average **Figure 4.** Indication of Wild and Flyers forwards’ involvement in position of the orange and green advancing the puck and their success in gaining the zone with possession. markers that the Flyers forwards were much better than the Wild at keeping possession of the puck as they entered the offensive zone. 

**Figure 4.** Indication of Wild and Flyers forwards’ involvement in advancing the puck and their success in gaining the zone with possession. 

In addition, the Flyers neutral zone plays were much more efficiently constructed; the correlation between a player’s involvement and usage was relatively strong, meaning the Flyers generally kept the puck on the stick of the most skilled forward. The lone exception to this was with Wayne Simmonds (#17) and Daniel Briere (#48). The two of them played together for the majority of the year, yet despite Briere being much more effective with the puck, Simmonds was responsible for more of the zone entries. This is a problem a coach could seek to analyze on video, finding specific plays where Briere too readily deferred to Simmonds and/or where Simmonds dumped the puck in when he could have carried it in or passed to Briere. Examples like this were present on each common line the Wild used last year (15-9-10, 25-21-14, 96-7-22), as the Wild exacerbated their deficit of talent with an inefficient system. 

## **6   Strategic Considerations** 

Given the extreme differences in offensive success for entries with possession and dumping the puck in, it is worth questioning whether teams are pressing hard enough to carry the puck in. Dumping the puck in is often thought to be a safe, responsible play, as a turnover at the blue line might lead to a rapid chance against, whereas the worst case on a dump-in is that the other team recovers the puck and has to advance the full length of the ice against an established forecheck. However, that traditional sports strategies are often too conservative as a result of misaligned incentives – an aggressive strategy might earn the team more wins in the long run, but the occasional spectacular failure of an aggressive scheme can cost a coach his job. So it is worth re-evaluating the conventional thinking in light of the zone entry data described here. 

It is clear that much more offense results from plays where the puck is carried in. One question to address is the extent to which this difference arises from odd-man rushes, plays where the offense has a sizable advantage and nearly always carries the puck into the offensive zone. As part of the zone entry tracking, observers recorded which entries were odd-man rushes so that their impact could be evaluated. It was found that their impact was negligible, both because they are relatively infrequent in today’s NHL (representing less than 3% of all 5-on-5 zone entries) and because the difference between an odd-man rush and a standard carry-in is significant but not overwhelming (0.78 shots versus 0.57). 

It is also important to evaluate the defensive aspect of the entry decision. It is clear that successfully carrying the puck in leads to substantially more offense, but how many unsuccessful attempts are there and how costly are they? To address this, unsuccessful entry attempts were also recorded in the Capitals games. That permits calculation of the expected outcome of each decision, as shown in Table 3. Contrary to popular understanding about the importance of making a team go the full length of the ice, failed attempts to carry the puck into the zone actually lead to fewer shots against than dump-and-chase plays and have a better average outcome than dumping the puck and going for a line change. 





2013 Research Paper Competition Presented by: 



**Table 3.** Accounting for the possibility of a turnover at the blue line and the expected outcome on the subsequent play actually increases the value of carrying the puck in relative to dumping it in, as measured in Capitals games. 

|Entry type|Shots for on<br>entry N|Opp gets<br>entry N+1|Shots for on<br>own entry<br>N+1|Shots against<br>on opp entry<br>N+1|Net expected<br>shots on<br>entryN+1|Net overall<br>value for<br>entry|
|---|---|---|---|---|---|---|
|Successful carry|0.55|52.7%|0.29|0.37|-0.06|0.50|
|Failed carry|0.00|55.6%|0.31|0.40|-0.08|-0.08|
|Carryattempt|0.48|53.1%|0.29|0.37|-0.06|0.42|
|Dump-chase|0.24|60.9%|0.31|0.39|-0.11|0.12|
|Dump-change|0.02|69.8%|0.36|0.32|-0.12|-0.10|



While the carry attempts on average are much more successful than trying to set up the offense by dumping the puck in, this is still not sufficient data to say conclusively that teams should be trying harder to carry the puck in at every opportunity. Clear proof for a change in strategy requires an analysis of the marginal situations rather than the average outcomes; only 14% of all carry-in attempts resulted in a turnover, but surely the turnover frequency would be higher in the marginal plays in question. Let us try to evaluate what the decision matrix looks like for those relatively well-defended situations. 



<!-- Start of picture text -->
1<br>0.9<br>0.8<br>0.7 Carry<br>0.6<br>0.5<br>0.4<br>0.3<br>Dump<br>0.2<br>0.1<br>0<br>0 0.2 0.4 0.6 0.8 1<br>Probability of successful carry<br>Shots per successful entry<br><!-- End of picture text -->

The failed carry-in attempts recorded here generally occurred 0 0.2 0.4 0.6 0.8 1 when a team was attempting to gain the zone with possession Probability of successful carry despite a reasonable challenge by the defense, so it is reasonable to assume that the outcomes of failed attempts in **Figure 5.** Decision chart for carry-in attempts. our marginal situations would have that same net outcome of - Solid line represents decisions for equal teams; 0.08 shots on average. The unknown parameters are how dashed line for a team that expects to shoot 9% likely a team is to succeed if they attempt to carry the puck in and hold the opponents to 7%. Dotted line on a reasonably well-defended play, and whether those shows average shots per carry-in. successes would result in fewer shots for than the average successful carry-in. The expected net shots for that attempt and the subsequent entry can be calculated as follows: 

**Figure 5.** Decision chart for carry-in attempts. Solid line represents decisions for equal teams; dashed line for a team that expects to shoot 9% and hold the opponents to 7%. Dotted line shows average shots per carry-in. 

### ( ) (     ) 

When this number exceeds the net +0.12 shots obtained on a dump-and-chase play, attempting to carry the puck in would be advantageous. Figure 5 shows the decision curve for attempting to carry the puck in. On a play where the typical 0.57 shots would be expected from a successful carry-in, one needs to be only 34% confident of success to make an attempted carry-in preferable to a dump-in given equal shooting percentages. This drops even further when the players on the ice have more skill than their opponents; if they expect to score on 9% of their shots and hold the opponents to 7% then the carry/dump threshold drops to 26%. It is likely that players give up the puck far too easily at the blue line, as in practice players seem not to take on defenses set up that well. There is some support for coaches’ tendency to encourage less-skilled players to make the safer play (the threshold for the 7% team would be 44%), but in general NHL teams probably could benefit from being more aggressive at the blue line. 

## **7   Conclusions** 

Breaking the game into discrete offensive, neutral, and defensive zone possessions has permitted a detailed understanding of what drives success. It is found that talent for driving shot differential derives almost entirely from neutral zone play and that attack zone talent is largely confined to shot quality effects. Some strategic inefficiencies have been identified, both in lineup construction and in aggressiveness on zone entry attempts. 

[1] JLikens. “Even Strength Shooting Percentage.” _Objective NHL_ . Blogspot, 1 Feb. 2009. Web. 13 Jan. 2013. 

[2] Vic Ferrari. “Real Effects and Team Shooting Percentage at Even Strength.” _Irreverent Oiler Fans_ . Blogspot, 8 Jun. 2009. Web. 13 Jan. 2013. 

[3] JLikens. “Even Strength Outshooting and Team Quality.” _Objective NHL_ . Blogspot, 26 Jan. 2011. Web. 13 Jan. 2013. 

[4] Rob Parker. “On Tracking Scoring Chances, Part I.” _Japers’ Rink_ . SB Nation, 27 Aug. 2012. Web. 13 Jan 2013. 



2013 Research Paper Competition Presented by: 




