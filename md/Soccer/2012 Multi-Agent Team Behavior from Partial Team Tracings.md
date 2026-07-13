<!-- source: Soccer/2012 Multi-Agent Team Behavior from Partial Team Tracings.pdf -->

Proceedings of the Twenty-Sixth AAAI Conference on Artificial Intelligence 

# **Characterizing Multi-Agent Team Behavior from Partial Team Tracings: Evidence from the English Premier League** 

## **Patrick Lucey**<sup>1</sup> **, Alina Bialkowski**<sup>1</sup><sup>_,_2</sup> **, Peter Carr**<sup>1</sup> **, Eric Foote**<sup>1</sup> **and Iain Matthews**<sup>1</sup> 

1Disney Research Pittsburgh, Forbes Avenue, Pittsburgh, PA, 15213 

2SAIVT Laboratory, Queensland University of Technology, Brisbane, Australia, QLD, 4001 –patrick.lucey,peter.carr,eric.foote,iainm˝@disneyresearch.com alina.bialkowski@qut.edu.au 

#### **Abstract** 

Real-world AI systems have been recently deployed which can automatically analyze the plan and tactics of tennis players. As the game-state is updated regularly at short intervals (i.e. point-level), a library of successful and unsuccessful plans of a player can be learnt over time. Given the relative strengths and weaknesses of a player’s plans, a set of proven plans or _tactics_ from the library that characterize a player can be identified. For low-scoring, continuous team sports like soccer, such analysis for multi-agent teams does not exist as the game is not segmented into “discretized” plays (i.e. plans), making it difficult to obtain a library that characterizes a team’s behavior. Additionally, as player tracking data is costly and difficult to obtain, we only have partial team tracings in the form of ball actions which makes this problem even more difficult. In this paper, we propose a method to overcome these issues by representing team behavior via _play-segments_ , which are spatio-temporal descriptions of ball movement over fixed windows of time. Using these representations we can characterize team behavior from _entropy maps_ , which give a measure of predictability of team behaviors across the field. We show the efficacy and applicability of our method on the 2010-2011 English Premier League soccer data. 

## **Introduction** 

The use of AI systems in sport has graduated from the virtual to the real-world. This is due in part to the popularity of livesport, the amount of live-sport being broadcasted, the proliferation of mobile devices, the rise of second-screen viewing, the amount of data/statistics being generated for sports, and demand for in-depth reporting and analysis of sport. Systems which use match statistics to automatically generate narratives have already been deployed (Allen et al. 2010; Statsheet 2012). Although impressive, these solutions just give a low-level description of match statistics and notable individual performances without giving any tactical analysis about factors which contributed to the result. In tennis however, IBM has created _Slamtracker_ (IBM SlamTracker 2012) which can provide player analysis by finding patterns and styles of play that characterize a player from an enormous amount of data. 

Copyright _⃝_ c 2012, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

Figure 1: A multi-agent plan recognition (MAPR) framework can be used to analyze team tactics of a sporting match. Given a sequence of team behaviors, we can map these to a plan within a library. A set of these common plans can then describe the underlying tactics employed. For continuous and low-scoring sports, such as soccer, segmenting agent behaviors into a series of plans is difficult. In this paper, we show a method of circumventing this issue. 

Multi-agent plan recognition (MAPR) constitutes a method to provide this type of analysis for team sports in the future. Given a sequence of observed team behaviors or activities, MAPR seeks to map these behaviors to one distinct plan within a library of plans. A set of these recognized plans can then be used to infer the tactics employed by an agent team in adversarial domains (see Figure 1(a)). As the match is segmented into distinct plan segments, this type of approach has started to be applied for team sports such as American Football (Intille and Bobick 1999; Hess, Fern, and Mortensen 2007; Siddiquie, Yacoob, and Davis 2009; Li and Chellappa 2010; Stracuzzi et al. 2011) and basketball (Perse et al. 2008). But due to the difficulty of tracking players and the ball in confined spaces, as well as labeling the complex actions and interactions between players and their teammates and adversaries, the large amount of tracing data which is required to do find characteristic patterns is not available. As such, most of the work has been dedicated to doing team activity detection on small amounts of data. 

For continuous and low-scoring team sports such as soccer, it has the additional headache of the game not being segmented into “discretized” plays (i.e. plans) - therefore making automatic analysis even more difficult. However, due to 

1387 

the explosion in interest in analyzing soccer, there has been a massive demand for real-time statistics and visualizations. Due to the difficulty associated with tracking players and the ball, most of the data collected is via an army of human annotators who label all actions that occur around the ball - which they call _ball actions_ . Although only giving partial team tracing information, the sheer volume of data available makes automatic analysis of team behavior an interesting and possible research endeavor. 

In this paper, we propose a method to characterize team behaviors for soccer using partial team tracings. As we do not have a library of labeled plans, we do this by representing team behavior as _play-segments_ , which are spatiotemporal descriptions of ball movement over fixed windows of time. This differs from current approaches which use labeled plan libraries and full team tracings (see Figure 1). The ball movements were inferred from the hand annotated ball action dataset which is currently used for visualizations in sports production (Opta 2012). Using our play-segment representations we can characterize team behavior from _entropy maps_ , which give a measure of predictability of team behaviors across the field. We show the efficacy and applicability of our method on the 2010-2011 English Premier League soccer data. 

## **Related Work** 

MAPR aims to describe the activity sequence of a set of agents by identifying team structures and behaviors learnt from a library of team plans (Banerjee, Kraemer, and Lyle 2010). Due to the host of military, surveillance and sport applications that it can be utilized in, research into this area has dramatically increased recently. Outside of the sport realm, most of this work has focussed on dynamic teams (i.e. where individual agents can leave and join teams over the period of the observations). An initial approach to MAPR was to use a library of single agent plans to recognize team plans (Avrahami-Zilberbrand et al. 2010). Sukthankar and Sycara used a library of team plans but pruned the size of the library by using temporal ordering constraints and agent resource dependencies (Sukthankar and Sycara 2008; 2012). Banerjee et al.’s work was somewhere in between as they “decompressed” the single agent plan library as they found that it was NP-complete for the multi-agent case (Banerjee, Kraemer, and Lyle 2010). Sadilek and Kautz (Sadilek and Kautz 2008) used GPS locations of multiple agents in a “capture the flag” game to recognize low-level activities such as approaching and being at the same location. All of these works assume that team traces and plans are fully observed, but Zhuo and Li (Laviers et al. 2011) proposed a MAX-SAT solver which can do MAPR with partial team tracings and team plans. 

Sport related MAPR research mostly centers on low-level activity detection and with the majority centered on American Football. In the seminal work by Intille and Bobick (Intille and Bobick 1999), they recognized a single football play _pCurl51_ , using a Bayesian network to model the interactions between the players trajectories. Li et al. (Li, Chellappa, and Zhou 2009), modeled and classified five offensive football plays (e.g. dropback, combo dropback, middle 

run, left run, right run). Siddiquie et al. (Siddiquie, Yacoob, and Davis 2009), performed automated experiments to classify seven offensive football plays using a shape (HoG) and motion (HoF) based spatio-temporal feature. Instead of recognizing football plays, Li and Chellapa (Li and Chellappa 2010) used a spatio-temporal driving force model to segment the two groups/teams using their trajectories. Researchers at Oregon State University have also done substantial research in the football space (Hess, Fern, and Mortensen 2007; Hess and Fern 2009; Stracuzzi et al. 2011) with the goal of automatically detecting offensive plays from a raw video source and transfer this knowledge to a simulator. For soccer, Kim et al. (Kim et al. 2010) used the global motion of all players in a soccer match to predict where the play will evolve in the short-term. Beetz et al. (Beetz et al. 2009) developed the _automated sport game models_ (ASPOGAMO) system which can automatically track player and ball positions via a vision system. Using soccer as an example, the system was used to gain a heat-map of player positions (i.e. which area of the field did a player mostly spend time in) and also has the capability of clustering passes into low-level classes (i.e. long, short etc.), although no thorough analysis was conducted due to a lack of data. In basketball, Perse et al. (Perse et al. 2008) used trajectories of player movement to recognize three types of team offensive patterns. Hervieu et al. (Hervieu and Bouthemy 2010) also used player trajectories to recognize low-level team activities using a hierarchical parallel semi-Markov model. 

Apart from the IBM Slamtracker (IBM SlamTracker 2012), no tactical team behavior analysis systems for realworld sports seem to exist. However, this is not the case with the Robocup domain, especially for the Coach Agent competition (Riley and Veloso 2002). “Rush 2008” is a simulation of American Football and was developed as a platform for evaluating game-playing agents (Molineaux 2008). Using this simulation, researchers have started to study the problem of learning strategies by observation (Li et al. 2009) as well as opponent modeling (Laviers et al. 2009). 

While similar in spirit, our work differs from these works mentioned above as we aim to recognize and characterize team behaviors for real-world sports, while having no plan library, or labels to form a plan library from partial team tracing data. 

## **Problem Formulation** 

We define a team as a set of agents having a shared objective and a shared mental state (Cohen and Levesque 1990). As we are dealing with soccer, each agent is permanently fixed to one team. Unless an agent has been dismissed from the match, each team always has the same number of agents (11). We refer to _team behaviors_ , as short, observable segments of coordinated movement and action executed by a team (e.g. pass from agent A to agent B). These behaviors are observed from partial spatio-temporal tracings, which in this case refers to ball movement inferred from handannotated ball-action data (see next section). 

A _plan_ can be defined as an ordered sequence of team behaviors describing a recipe used by a team to achieve a goal (Sukthankar and Sycara 2012). A team performing a 

1388 





Figure 2: (a) A modified example of the Opta F24 feed between Arsenal and Liverpool. (b) From this we can infer the ball position and possession at every time step (solid lines and dots are annotated, dotted lines are inferred). 

group of these plans to achieve a major goal (e.g. winning a match), can be said to be employing _tactics_ . However, as soccer is low-scoring, continuous and complex due to the various multi-agent interactions, labeling and segmenting the game into a series of plans is extremely difficult. Hence recognizing team tactics using the MAPR framework we described previously is impossible without these labelled plans. To overcome this issue, we quantize a match into equal temporal chunks which we use to describe team behavior. As these segments do not describe a method of achieving a specific goal, we do not call them plans, but _play-segments_ . We use these play-segments to form a library or _playbook_ of play-segments, _P_ = _{p_ 1 _, p_ 2 _, p_ 3 _, . . . , pm}_ , where _m_ is the number of unique play-segments within the playbook. 

The open questions to address with respect to the playsegments are: 

- How to represent these play-segments given partial team tracings? Also, what are the optimal parameters of this representation? 

- What tactical insights can we gain from having a playbook of play-segments? Can we devise a visualization or quantitative analysis to back up the analysis? 

- How discriminative are our representations? That is, do teams have unique styles of play? And if so, can we detect when they deviate from this style? 

Using ball action data as our partial tracing data (see next section), the rest of the paper is dedicated to answering these questions. 

|**Ranking**|**Team Name**|**Ranking**|**Team Name**|
|---|---|---|---|
|1|Man Utd|11|West Brom|
|2|Chelsea|12|Newcastle|
|3|Man City|13|Stoke City|
|4|Arsenal|14|Bolton|
|5|Tottenham|15|Blackburn|
|6|Liverpool|16|Wigan|
|7|Everton|17|Wolves|
|8|Fulham|18|Birmingham|
|9|Aston Villa|19|Blackpool|
|10|Sunderland|20|West Ham|



Table 1: Table showing the team name and ranking for the 2010-2011 English Premier League season. 

## **Partial Team Tracing from Ball Action Data** 

Due to the difficulty associated with tracking players and the ball, data containing this information is still scarce. Most of the data collected is via an army of human annotators who label all actions that occur around the ball - which they call _ball actions_ . The F24 soccer data feed collected for the English Premier League (EPL) by Opta (Opta 2012) is a good example of this. The F24 data is a time coded feed that lists all player action events within the game with a player, team, event type, minute and second for each action. Each event has a series of qualifiers describing it. An example of the data feed is given in Figure 2(a). This type of data is currently used for the real-time online visualizations of events, as well as post-analysis for prominent television and newspaper entities (e.g. ESPN, The Guardian). Even though this data has been widely used, there are no systems which use this data or data like this for automatic tactical analysis. 

For our work we used the 2010-2011 EPL season F24 Opta feed, which consists of 380 games and more than 760,000 events. Each team plays 38 games each, which corresponds with each team playing each other team twice (once home and once away). The team names and ranking for the 2010-2011 EPL data is given in Table 1. In our approach, to analyze the tactics of a team we are required to know the position of the ball and which team has possession of it at every time step (i.e. every second). To do this, we infer the ball location from the data feed. We describe our method via Figure 2. In (a) we can see at _t_ 0 = 114 Arsenal successfully passed the ball from (20 _._ 2 _,_ 64 _._ 0) to (35 _._ 6 _,_ 87 _._ 3). As no time is given for the arrival time of the pass, we assume that the pass took one second, so _t_ 1 = 115. The next action labeled is that an Arsenal player took on a Liverpool player at (51 _._ 2 _,_ 84 _._ 1), while the Liverpool defender unsuccessfully tried to tackle the Arsenal player at (48 _._ 8 _,_ 15 _._ 9) at _t_ 4 = 118. As nothing occurred between the time 115 to 118, we infer that an Arsenal player dribbled the ball from (35 _._ 6 _,_ 87 _._ 3) to (51 _._ 2 _,_ 84 _._ 1). From these two points, we assume that the ball was dribbled in a straight line and at a uniform speed. Based on these assumptions, we can infer the ball location at _t_ 2 = 116 and _t_ 3 = 117 and that Arsenal still had possession as the next annotated ball action involved Arsenal having the ball. It is worth noting here that all data is normalized onto a field of size 100 _×_ 100, with all positions given for teams attacking left to right. So in this 

1389 



Figure 3: Given a possession string, we break it up into _N_ equal chunks and use the quantized ball position values as our play-segment representation, **s** . 

example, even though the take on and tackle occurred at the same position, the position relative to each team differs. Using the same procedure, we can estimate the ball position and team possession for the remaining times. 

## **Characterizing Team Behavior via Entropy Maps** 

### **Play-Segment Representation** 

Given the observed partial spatio-temporal tracings in a game, _O_ = _{A, B}_ , we partition the tracings for each team into possession strings (i.e. continuous movement of the ball for a single team without turnover or stoppage), where _A_ = _{_ **a** 0 _, . . . ,_ **a** _I−_ 1 _}_ and _B_ = _{_ **b** 0 _, . . . ,_ **b** _J−_ 1 _}_ refer to the possession strings associated with each team and _I −_ 1 and _J −_ 1 are the number of possessions. We then quantize the field into a grid of size _l × w_ and vectorize the field via the columns. As the possession strings vary in length, we apply a sliding window of length _T_ to quantize or chunk the possessions into play-segments _S_ = _{_ **s** 0 _, . . . ,_ **s** _N −_ 1 _}_ of equal length, where _N_ is the total number of play-segments for a possession, and _M_ is the total number of play-segments for a team over a match. Given that a team’s possession string is of length _T_ 1, the resulting number of play-segments for each possession is therefore: _N_ = ( _T_ 1 _− T_ )+1. If the possession string is smaller in duration than _T_ , we discard it. To represent each play-segment **p** = _{p_ 0 _, . . . , pT −_ 1 _}_ , the quantized ball position at each time step is then used to populate each entry. 

A description of this process is given in Figure 3. Given the possession string **a** = _{a_ 0 _, . . . , a_ 13 _}_ shown, we first break the field up into a grid of 4 _×_ 5 and then vectorize it to give quantized ball positions. At each time step, the quantized ball position is used to populate **a** . Using _T_ = 10, we 



Figure 4: For a set of play-segments which start at a quantized field position _Si_ , we can form a probability distribution, **p** ( _Si_ ) based on where the ball travels to from this initial position. Using this probability distribution, we can determine the entropy of each area which together forms an entropy map. 

then chunk **a** into _N_ = (14 _−_ 10 + 1) = 5 play-segments resulting in five play-segments _{_ **s** 0 _, . . . ,_ **s** 4 _}_ shown. Using this process, we can get play-segments from all the possession strings to represent a team’s behavior. We used this approach as it allows us to analyze the short-term behavior of a team over a particular region, which maybe lost otherwise. 

### **Entropy Maps** 

The _entropy_ or information content of a random discrete variable, _X_ with a probability distribution **p** ( _X_ ) = ( _p_ 0 _, . . . , pn−_ 1) was defined by Shannon (Shannon 1948) as: 



where 0 log _∞_ = 0 and the base of the logarithm determines the unit, (e.g. if base 2 the measure is in bits). Entropy can be viewed as a measure of uncertainty or how predictable or unpredictable a team’s patterns of play is for different areas on the field. For soccer, this means that for each region on the field we can work out how predictable a team is (e.g. at a particular region, do teams do the same thing or do they vary their behavior?). High entropy refers to uncertainty in the input signal - we need more bits to transfer this information. Low entropy means that the signal is highly predictable - meaning that this information can be transferred by fewer bits. 

Using our play-segment representation, we can determine an entropy map to quantify and visualize the predictability of team behavior. We do this as follows: Given the observations of a team, we determine the set of playsegments _S_ = _{_ **s** 0 _, . . . ,_ **s** _N −_ 1 _}_ . From these representations, we know where the ball started from and where it travelled over the duration of the play-segment. For each quantized area on the field we have a set of play-segments, where **S** = _{S_ 1 _, . . . , Sl×w}_ and the indices refer to the quantized field areas. For each set of play-segments we can then form a probability distribution based on the occupancy for all the play-segments which started in that quantized area. From this probability distribution we can calculate the entropy for that area. An example of this procedure is given in Figure 4. 

1390 











Figure 5: Entropy maps which show the characteristic ball movement for (a) Manchester United, (b) Tottenham, (c) Stoke City, (d) Blackburn and (e) Wigan using the entire 38 games for the EPL 2010-2011 season. Note that these maps have been normalized for teams attacking from left to right. 



<!-- Start of picture text -->
Length of Play-Segment Window,  T (seconds)<br>Mean Entropy<br><!-- End of picture text -->

Figure 6: Plot of the mean team entropies for different playsegment windows, _T_ . The order of the curves relating to team id (see Table 1) are given by the legend on the top of the plot (top 10 teams are on the first row, bottom 10 teams are on the bottom). 

### **Characterizing Teams Using Entropy Maps** 

Using entropy maps, we can gain both a quantitative as well as a visual method of seeing how predictable a team is from an area of the field (e.g. are they more dangerous at one area over another?). For this analysis, we use the entire season of data to build a characteristic map of each team. The first question we wanted to answer was “does entropy relate to team ranking?” and “does this vary depending on _T_ ?”. To do this we quantized the field into 20 _×_ 16 bins and used different time window lengths to find the entropy map for each team. The results are shown in Figure 6. As can be seen from this plot, the top five teams have the highest mean entropies for varying play-segment window lengths. Other than the top five teams, team ranking does not correspond with entropy. It is also worth noting that the maximum entropy occurs around 4 to 5 seconds for all teams, which is important to note as this also means that this window of time maximizes the amount of information available. It might be tempting however to use a longer window as there is greater separation in the curves, but this also relates to a drop off in information which reduces the discriminative power of the signal. 

In Figure 5, we show the characteristic entropy maps of five teams, (a) Manchester United (rank 1), (b) Tottenham (rank 5), Stoke City (rank 13), Blackburn (rank15) and Wigan (rank 16). As _T_ = 5 yields the most information, 

we used this time window for the rest of experiments (i.e. heuristically, we found this to be the case as well). Generally, it can be seen that the the entropy around goal area in the attacking end is low due to the amount of players that are around these areas trying to protect the goal as well as the corners which makes sense as there are relatively little options from these positions. More specifically, in (a) and (b), the heavy redness throughout the maps is evident, especially through the centers which signifies both Manchester United and Tottenham are passing teams who move the ball around quite well. The heavy red for Manchester United is more pronounced on the right-side of the field (relative to each team attacking left-to-right on the page), while for Tottenham it is on the left. These trends make sense as Manchester United have Luis Nani who is a dynamic winger who tends to spend a lot of time in these areas, and Tottenham have Gareth Bale who has similar traits on the left-hand side. In next two maps (c) and (d), it is apparent that both these teams do not play such an expansive passing game, which makes sense as both Stoke City and Blackburn play a predicable direct style (i.e. from the back they kick the ball long to their forwards to minimize the amount of error in their defensive half). In the last map (e), we see that despite finishing in 16th position, Wigan played a similar style to the top teams, although it can be seen that they do not utilize the width as much. 

### **Identifying Team Behavior Variation** 

In terms of tactical analysis at the match level, it is important to be able to determine what type of style a team is playing. Additionally, it is important to see if they are playing as expected or they have employed a new style of play. To do this, we conducted some team identification experiments. Not only do these experiments allow us to determine these things, we also get to see how discriminative our representations are, as well as seeing if individual teams have unique styles of play. The team identification task we posed was, _given we have the play-segment playbooks for a home and away team, could we correctly identify the home team?_ For these experiments, we used the entire 380 games of the season and used a leave-one-match-out cross validation strategy to maximize training and testing data. To show how discriminative our entropy map approach was, we compared it to twenty-three match statistics currently used in analysis (e.g. passes, shots, tackles, fouls, aerials, possession, timein-play etc.), as well as a combination of the entropy map and match statistics. For classification, we used a k-Nearest Neighbor approach. All experiments were conducted using 

1391 







Figure 7: Confusion matrices for the team identification experiments using: (a) match statistics (accuracy = 19%), (b) entropy maps (accuracy = 30%), (c) concatenation of match statistics and entropy map (accuracy = 47%). The actual team identity is given on the vertical axis, while the predicted/recognized identity is given on the horizontal axis. Also, notice that in (c) the team that got ranked (1) got confused as the last placed team for a game (red circle in the top right corner). 

a play-segments size of 10 _×_ 8 over a window of _T_ = 5 as we heuristically we found this to yield optimal results. All feature sets were also scaled and underwent a step of LDA (linear discriminant analysis) to gain a compact, class preserving representation. The confusion matrices for the three different feature sets are given in Figure 7. 

As can be seen from the first confusion matrix (a), very little discriminative information about the team exists with accuracy of about 19% obtained (chance is 5%). The entropy maps reached 30% accuracy, with the diagonal clearly visible. Combining both information sources together greatly improves the classification accuracy again, with 47% achieved, which is very good when you consider we only have the ball movement data. It also shows that teams do have unique styles of play which can be picked up from using our approach. It is also worth noting that the teams that tend to get confused with each other play similar styles. An example of this is teams 13, 14, 15 (Stoke, Bolton and Blackburn). As mentioned previously, these teams tend to play a very similar simple and predicable direct style. This plot shows that they do not vary this style much during the season, which also reinforces why their entropy levels were the lowest out of all the teams (see Figure 6. These also seems to be a trend for the top teams, where they often get confused with each other which means they also play similar styles. But this begs the question, when they play each other do they play the same style or do they play another style? To answer this, we can use this team identification result shown in the top corner of Figure 6(c). 

When looking at the result, the top team Manchester United got confused with the bottom team West Ham United. Their opponent on this occasion was Arsenal who finished fourth and play a very expansive passing game, which is highlighted by the fact that they have the highest entropy value. When we compare the mean entropy map of Manchester United to their entropy map of the game in Figure 8 (a) and (b) we can see the difference. When you compare this to the West Ham mean entropy map, you can see why it got confused. What is interesting to note though, 







Figure 8: Entropy maps for (a) Average Man Utd performance, (b) Man Utd performance vs Arsenal, (c) Average West Ham performance. Our analysis shows that for this game, Man Utd’s style changed to a more counter-attacking West Ham style. 

is that on this occasion Manchester United actually won 2- 0 by playing a counter attacking game (e.g. be defensively compact and break quickly). Due to a relative lack of talent, West Ham played this style too but probably did not have the offensive weapons to pull this off. A tactical analysis of this game is given by zonalmarking.net (Zonalmarking 2011). 

## **Summary and Future Work** 

In this paper, we proposed a method to characterize team behavior for soccer by representing team behavior via _playsegments_ , which are spatio-temporal descriptions of ball movement over fixed windows of time. Using these representations we characterized team behavior from _entropy maps_ , which gives a measure of predictability of team behaviors across the field. As soccer is low-scoring and continuous, analyzing team patterns of play is difficult as there is no library of labeled plan or full team tracings, which differs from current MAPR approaches which use labeled plan libraries and full team tracings. We illustrated the benefit of our approach on the 2010-2011 English Premier League soccer data by characterizing teams via entropy maps, as well as showing how our approach can be used to detect team style variation through team identification experiments. In the future we endeavor to use this type of approach to characterize team behaviors in goal-scoring scenarios. Also, seeing that we can do this type of analysis using partial team tracings we plan to develop this tool on a tablet device, such as an iPad which would make it accessible in amateur and semiprofessional sporting domains. 

1392 

## **References** 

Allen, N.; Templon, J.; McNally, P.; Birnbaum, L.; and Hammond, K. 2010. StatsMonkey: A Data-Driven Sports Narrative Writer. In _AAAI Fall Symposium Series_ . 

Avrahami-Zilberbrand, D.; Banerjee, B.; Kraemer, L.; and Lyle, J. 2010. Multi-Agent Plan Recognition: Formalization and Algorithms. In _AAAI_ . 

Banerjee, B.; Kraemer, L.; and Lyle, J. 2010. Multi-Agent Plan Recognition: Formalization and Algorithms. In _AAAI_ . Beetz, M.; von Hoyningen-Huene, N.; Kirchlechner, B.; Gedikli, S.; Siles, F.; Durus, M.; and Lames, M. 2009. ASPOGAMO: Automated Sports Game Analysis Models. _International Journal of Computer Science in Sport_ 8(1). 

Cohen, P., and Levesque, H. 1990. Intention is Choice with Commitment. _Artificial Intelligence_ 42. 

Hervieu, A., and Bouthemy, P. 2010. Understanding sports video using players trajectories. In Zhang, J.; Shao, L.; Zhang, L.; and Jones, G., eds., _Intelligent Video Event Analysis and Understanding_ . Springer Berlin / Heidelberg. Hess, R., and Fern, A. 2009. Discriminatively Trained Particle Filters for Complex Multi-Object Tracking. In _CVPR_ . Hess, R.; Fern, A.; and Mortensen, E. 2007. Mixture-ofParts Pictorial Structures for Objects with Variable Part Sets. In _ICCV_ . 

Riley, P., and Veloso, M. 2002. Recognizing Probabilistic Opponent Movement Models. In Birk, A.; Coradeschi, S.; and Tadorokoro, S., eds., _RoboCup-2001: Robot Soccer World Cup V_ . Springer Verlag. 

Sadilek, A., and Kautz, H. 2008. Recognizing Multi-Agent Activities from GPS Data. In _AAAI_ . 

Shannon, C. 1948. A Mathematical Theory of Communication. _The Bell System Technical Journal_ 28. 

Siddiquie, B.; Yacoob, Y.; and Davis, L. 2009. Recognizing Plays in American Football Videos. Technical report, University of Maryland. 

Statsheet. 2012. www.statsheet.com. 

Stracuzzi, D.; Fern, A.; Ali, K.; Hess, R.; Pinto, J.; Li, N.; Konik, T.; and Shapiro, D. 2011. An Application of Transfer to American Football: From Observation of Raw Video to Control in a Simulated Environment. _AI Magazine_ 32(2). 

Sukthankar, G., and Sycara, K. 2008. Hypothesis Pruning and Ranking for Large Plan Recognition Problems. In _AAAI_ . Sukthankar, G., and Sycara, K. 2012. Activity Recognition for Dynamic Multi-Agent Teams. _ACM Trans. Intell. Syst. Technol_ . 

Zonalmarking. 2011. www.zonalmarking.net2011/03/12/ man-utd-2-0-arsenal-tactics/. 

IBM SlamTracker. 2012. www.australianopen.com/en˙AU/ ibmrealtime/index.html. 

Intille, S., and Bobick, A. 1999. A Framework for Recognizing Multi-Agent Action from Visual Evidence. In _AAAI_ . 

Kim, K.; Grundmann, M.; Shamir, A.; Matthews, I.; Hodgins, J.; and Essa, I. 2010. Motion Fields to Predict Play Evolution in Dynamic Sports Scenes. In _CVPR_ . 

Laviers, K.; Sukthankar, G.; Molineaux, M.; and Aha, D. 2009. Improving Offensive Performance through Opponent Modeling. In _AAAI Conference on Artificial Intelligence for Interactive Digital Entertainment_ . 

Laviers, K.; Sukthankar, G.; Molineaux, M.; and Aha, D. 2011. Improving Offensive Performance through Opponent Modeling. In _International Joint Conference on Artificial Intelligence Conference_ . 

Li, R., and Chellappa, R. 2010. Group Motion Segmentation Using a Spatio-Temporal Driving Force Model. In _CVPR_ . 

Li, C.; Manya, F.; Mohamedou, N.; and Planes, J. 2009. Exploiting Cycle Structures in MAX-SAT. In _International Conference on Theory and Applications of Satisfiability Testing_ . 

Li, R.; Chellappa, R.; and Zhou, S. 2009. Learning MultiModal Densities on Discriminative Temporal Interaction Manifold for Group Activity Recognition. In _CVPR_ . 

Molineaux, M. 2008. Working Specification for Rush 2008 Interface. Technical report, Knexus Research Corp. 

Opta. 2012. www.optasports.com. 

Perse, M.; Kristan, M.; Kovacic, S.; and Pers, J. 2008. A Trajectory-Based Analysis of Coordinated Team Activity in Basketball Game. _Computer Vision and Image Understanding_ . 

1393 


