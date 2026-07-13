<!-- source: 2017 Hockey Passing Defensive Ability.pdf -->



# **Evaluating Defensive Ability in Hockey Using Passing Data** 

Ryan Stimson & Matt Cane 

Other Sports (Hockey) 

1614 

## **Abstract** 

Measuring defensive success in hockey is difficult due to a historical reliance on shotbased metrics. In other sports, passing data has led to major insights on defensive play. In 2015, 20 fans began tracking each pass leading to a shot to help understand the factors that lead to goals. For each shot, trackers recorded the sequence of passes which preceded it. Data collected included shot time, passer(s) and shooter, pass locations (center/left/right and offensive/defensive/neutral zone), and other known predictors of shot success (one-timers, odd-man rushes). Using this data, new metrics were developed to better evaluate the defensive impacts of both players and coaching systems. Defensive passing metrics are significant improvements upon existing defensive measures, and are both more repeatable and more predictive of future defensive results. Passing metrics have a broad range of applications at both the ingame and managerial level, and can inform tactical decisions, measure system success, and assist with player evaluation. 

## **1. Introduction** 

Evaluating defensive play in hockey traditionally been difficult, as isolating an individual player’s defensive contributions from those of the defensive system he or she plays within is not a simple task with the data currently recorded by the NHL. Defense is largely about measuring the absence of your opponent’s offense, and this can be interrupted in a number of ways that go undetected. While shot attempt and expected goals metrics<sup>1</sup> offer information on who may be excelling or struggling defensively, current models still lack critical contextual information about the movement of the puck via passing prior to the shot, a key area in which the defensive team can have a direct impact via positioning and player marking. 

The importance of passing is already well established in other sports. Preliminary work on tracking the impact of passing in hockey<sup>2</sup> has shown many similar themes to those uncovered using passing 

1 DTMAboutHeart, mean_63. “Expected Goals are a better predictor of future scoring than Corsi, Goals.” _Hockey-Graphs._ 1 Oct. 2015. Web. 3 Dec. 2016. 

> 2 Stimson. “Redefining Shot Quality: One Pass at a Time.” _Hockey-Graphs_ . 27 Jan. 2016. Web. 3 Dec. 2016. 





2017 Research Papers Competition 

1 



data in soccer<sup>3</sup> . Passing data has also shed light on the factors that drive success in basketball: “shots that immediately follow passes are much more likely to go through the hoop than their unassisted counterparts. The best kinds of shots result from teamwork.”<sup>4</sup> Knowing that better passers can facilitate the “best kinds of shots” as Kirk Goldsberry has said, and acquiring these types of players can have a significant impact on your team.<sup>5</sup> Similarly, finding players who are able to disrupt your opponent’s passing plays can have a strong positive impact defensively. 

Passing information is clearly critical to understanding the factors that drive success in hockey and to understanding which players and teams are best at influencing these factors. Unfortunately, passing data in hockey is not recorded by the NHL, and needs to be tracked by volunteers, which has been shown to provide new ways of evaluating player and team performance.<sup>6</sup> Recording this data allows us to gain insight on which areas of the game players and teams can consistently influence, and sheds light on how critical the ability to prevent dangerous passing sequences is to defensive results. 

## **2. Data Collection and Methods** 

Data for the project was collected by a team of volunteer trackers. Each tracker was required to complete 2 - 3 training games for validation by the project leader to ensure consistency in classification of passes and recording of data. Occasional spot-checking of games was also conducted.  565 total games were tracked from the 2015-2016 season. 

For each shot, trackers recorded the sequence of passes which preceded it. Data attributes collected were determined following review of exploratory data collected in the 2014-2015 season. Attributes collected included shot time, passer(s) and shooter, pass locations (center/left/right and offensive/defensive/neutral zone), and other known predictors of shot success (one-timers, oddman rushes, lateral puck movement). Landmarks on the ice were used to minimize tracker bias in interpreting events (passes were recorded when they originated behind the goal line, back to the point at the blue line, or from the center lane, which we defined as being between the faceoff dots). Data from NHL.com was used to determine which defenders were on the ice. 

> 3 Alex Olshansky. “Shots and Key Passes are Better than Goals and Assists.” _Statsbomb._ 26 Sept. 2013. Web. 3 Dec. 2016. 

4 Kirk Goldsberry. “The NBA’s Next Shooting Revolution Has Already Been Televised.” _Grantland._ 13 Oct 2015. Web. 3 Dec. 2016. 

5 Seth Partnow. “Clippers now have two of the NBA’s best playmakers in Josh Smith and Chris Paul.” _Fancy Stats_ . 27 Jul. 2015. Web. 3 Dec. 2016. 

6 Eric Tulsky, Geoffrey Detweiler, Robert Spencer, Corey Sznajder. “Using Zone Entry Data to Separate Offensive, Neutral, And Defensive Zone Performance.” _HockeyAnalytics._ 1 Mar. 2013. Web. 3 Dec. 2016. 





2017 Research Papers Competition 

2 



Metrics were developed based on the expected scoring rate of passing plays and known defensive strategies. The pass types tracked and metrics developed are listed in Table 1 below. 

_Table 1: Passing Metrics Developed_ 

|**Pass Type**|**Definition**|**Shot Attempt**<br>**Shooting**<br>**Percentage**|
|---|---|---|
|Rebound Shots<br>(RBD)|Shots taken from inside the home plate area<br>following anothershotfroma pass.|13.5%|
|Odd-Man Shots<br>(OM)|Shots taken off of passes where the attacking team<br>outnumbered the defending team upon entry into<br>the offensive zone.|16.9%|
|Point Shots (PNT)|Shots from passes within the offensive zone back to<br>a teammate at the blue line.|1.6%|
|Royal Road Shots<sup>7</sup><br>(RR)|Shots from passes crossing a line from the center of<br>one net to the other that did not meet one of the<br>above criteria.|14.6%|
|Behind-The-Net<br>Shots (BTN)|Shots from passes originating from behind the icing<br>line that did not meet one of the above criteria.|6.1%|
|Center Lane Shots<br>(CL)|Shots from passes originating from between the<br>faceoff dots that did not meet one of the above<br>criteria.|3.8%|
|Left/Right Lane<br>Shots (LRL)|Shots from passes originating from outside the<br>faceoff dots that did not meet one of the above<br>criteria.|2.9%|



Teams with more than 32 games played (N=16) and players with more than 500 minutes played (N=67 defensemen, 69 forwards) were included in the analysis. 

Metrics were tested for their repeatability (how much of a skill does the metric represent) and predictive value (how much does this skill relate to winning). Repeatability was tested using splithalf correlations. Predictive value was tested by calculating the correlation between passing metrics and out-of-sample goals against. Correlations between passing metrics were tested at the individual level to test the independence of defensive skills. 

## **3. The Importance of Pre-Shot Movement** 

Passing before a shot was found to have a significant impact on the likelihood of a shot resulting in a goal. Shots preceded by multiple passes had a shooting percentage 1.9% higher than shots preceded by no passes whatsoever. 

> 7 Kevin Woodley. “Unmasked: Analytics provide new evaluation tools.” _NHL.com._ 18 Dec. 2014. Web. 3 Dec. 2016. 





2017 Research Papers Competition 

3 



_Table 2: Shooting Percentage by # of Passes Preceding Shot_ 

|**# of Passes Before Shot**|**Shot Attempt Shooting Percentage**|
|---|---|
|0|3.2%|
|1|3.4%|
|2+|5.1%|



Shot attempts with passes also showed a high level of repeatability, and a strong ability to predict out of sample goal scoring. Shots without passes show significantly less ability to predict future goals than shots with passes. 

_Table 3: Split Half Reliability and Predictive Power of Passing and Shot Metrics_ 

|**# of Passes Before Shot**|**Split Half Repeatability**<br>**(R)**|**Split Half Predictive Value (R)**|
|---|---|---|
|ShotAttempts with Passes/60|0.68*|0.57*|
|Shot Attempts/60|0.77*|0.50*|
|Non-Passing Shots/60|0.73*|0.10|



_*P <= 0.05_ 

## **4. The Impact of Passing on the Quality of Shots** 

While current expected goals models account for the location of a shot and other contextual factors such as the time since the last shot, they do not take into account any pre-shot puck movement that occurs. This movement tends to increase the odds of a shot resulting in a goal by causing both the defenders and goaltender to move. The ability to pass and force the defenders to turn and reassess the situation allows for teams to take advantage of this moment and attack space that is now unaccounted for by a defense mid-decision. The goalie must move and may be blind to where the shot is coming from if there is significant lateral movement or the pass came from behind the net. 

We can use the passing data collected to close this gap by creating a new expected goals model based on the passes that preceded a shot. We define the total passing expected goals, or 𝑥𝐺𝑝, for or against, as: 



Where 𝑃𝑎𝑠𝑠𝑖𝑛𝑔 𝑀𝑒𝑡𝑟𝑖𝑐𝑖 is the 𝑖th passing metric from Table 1, and 𝑆ℎ%𝑃𝑎𝑠𝑠𝑖𝑛𝑔 𝑀𝑒𝑡𝑟𝑖𝑐𝑖 is the league average shooting percentage for that passing metric. We also include all shots not preceded by a pass to ensure that our average expected goal rates match the league average actual goal rates. 

## **5. Team Level Metrics** 

At the team level, passing metrics show significantly more repeatability and predictive value than existing shot based and expected goals metrics. 





2017 Research Papers Competition 

4 



_Table 4: Team Level Passing Metric Repeatability and Predictive Value (>= 32 Games per team)_ 

|**Team Metric**|**Split Half**<br>**Repeatability (R)**|**Split Half Predictive**<br>**Value (R)**|
|---|---|---|
|Shot Attempts Against/60|0.51|0.27*|
|GoalsAgainst/60|0.03|0.03|
|𝑥𝐺𝐴𝐶𝑜𝑟𝑠𝑖𝑐𝑎/60|0.52|0.43*|
|𝑥𝐺𝐴𝑝/60|0.68|0.58*|



_*P <= 0.05_ 

### **5. 1. Player Level Metrics** 

Most pass defense metrics showed reasonable repeatability for both forwards and defensemen, particularly considering the limited samples involved. For defensemen, split half correlations were slightly below the repeatability of Shot Attempts Against, although all but one metric had a significant repeatability in a smaller sample of events within each metric. For forwards, most metrics showed repeatability roughly in line with Shot Attempts Against once again in smaller samples. 

_Table 5: Player Level Passing Metric Repeatability (>= 250 Minutes per Half)_ 

|**Metric**|**Defensemen Split-Half**<br>**Repeatability (R)**|**Forward Split-Half**<br>**Repeatability (R)**|
|---|---|---|
|ShotAttemptsAgainst/60|0.53*|0.39*|
|Rebounds Against/60|0.40*|0.21*|
|OddMan Against/60|0.37*|0.42*|
|PointAgainst/60|0.27*|0.47*|
|RR Against/60|0.00|0.24*|
|BTN Against/60|0.26*|0.36*|
|CL Against/60|0.37*|0.35*|
|LRL Against/60|0.41*|0.33*|



_*P <= 0.05_ 

In addition, passing expected goals against per 60 is also a much better predictor of out-of-sample goals-against per 60 than traditional shot attempt metrics. Passing expected goals is a significant predictor of out-of-sample goals against per 60 for forwards, although it is not as predictive as current expected goals models. 

_Table 6: Predictive Value of Player Level Passing Metrics_ 

|**Metric**|**Defensemen Predictive Value**<br>**(R)**|**Forward Predictive Value**<br>**(R)**|
|---|---|---|
|Shot Attempts Against/60|0.04|0.02|
|𝑥𝐺𝐴𝐶𝑜𝑟𝑠𝑖𝑐𝑎/60|0.17|0.24*|
|𝑥𝐺𝐴𝑝/60|0.22*|0.17*|



_*P <= 0.05_ 

2017 Research Papers Competition 





5 



Player level metrics show low to moderate levels of correlation within themselves. Many of the metrics appear to be independent from one another, indicating that the passing metrics may be measuring distinct skillsets that skaters may possess. 

_Table 7: Correlations between Passing Defense Metrics (Shaded Cells are P <= 0.05)_ 

|**Defen**|**semen**|||||||**Forw**|**ards**|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**R**|**RBD**|**OM **|**PNT**|**RR**|**BTN**|**CL **|**LRL**|**R**|**RBD**|**OM **|**PNT**|**RR**|**BTN**|**CL **|**LRL**|
|**RBD**|1|0.2|0.2|0|0.3|0.4|0.1|**RBD**|1|0.2|0.1|-0.1|0.5|0.1|-0.1|
|**OM **|0.2|1|0.2|0.2|0.5|0.2|0.2|**OM **|0.2|1|0|0.3|0.5|0.3|0|
|**PNT**|0.2|0.2|1|0.3|0.2|-0.1|0.1|**PNT**|0.1|0|1|0.2|0|-0.4|-0.2|
|**RR**|0|0.2|0.3|1|0.2|0|0.3|**RR**|-0.1|0.3|0.2|1|0|0|0.1|
|**BTN**|0.3|0.5|0.2|0.2|1|0.3|0.2|**BTN**|0.5|0.5|0|0|1|0.3|0.1|
|**CL**|0.4|0.2|-0.1|0|0.3|1|0.5|**CL**|0.1|0.3|-0.4|0|0.3|1|0.3|
|**LRL**|0.1|0.2|0.1|0.3|0.2|0.5|1|**LRL**|-0.1|0|-0.2|0.1|0.1|0.3|1|



## **6. Strategic Considerations at the Team Level** 

Passing data can be used to evaluate tactical approaches which teams employ to suppress their opponents’ offensive opportunities. After conducting extensive video review of the teams that excelled or struggled at defending against passing opportunities, certain systems emerged as being better suited to preventing passes against. 

For example, the 2015-2016 Florida Panthers employed an aggressive, half-ice overload system which exerted a significant amount of pressure on their opponents in all three zones of the ice. This system allowed fewer opportunities for their opponents to generate extended passing sequences, and their rate of pass-assisted shots against per 60 minutes of 5-on-5 play was the lowest of all teams in games tracked to date. 

In contrast, the 2015-2016 Colorado Avalanche were much more passive and did not allow players to fill in for each other, instead relying on a strict man-to-man coverage system. This system was frequently exposed by their opponents, resulting in the Avalanche allowing the second most Royal Road Shots Against per 60, and the fourth most Behind-The-Net shots against per 60. The Avs player-to-player marking frequently allowed their opponents’ stars to lose their defenders and create opportunities to make dangerous passes and create high quality scoring chances. 

<mark>By evaluating team performance via passing data, new tactical approaches can also be innovative formations (eschewing the standard 3F-2D model) and shifting tactics to maximize these higher quality passing sequences (prioritizing pattern plays that have stronger predictive impact on goalscoring/suppression) should be at the forefront of a team’s research and analytics efforts.</mark> 

### **6.1. Strategic Considerations at the Player Level** 

At the player level, the independence of the various passing metrics has strategic implications for both team building and player deployment. Passing metrics can help identify what types of attacks teams are vulnerable to with their current rosters and which potential acquisitions could fill a defensive gap for a particular club. 





2017 Research Papers Competition 

6 



In addition, passing metrics can help coaches determine which players are best suited to certain matchups or zone deployments. Players who are strong at defending against odd-man rushes and royal road passes may offer defensive advantages from starting their shifts in the offensive zone, while skaters who are particularly good at preventing behind-the-net or center-lane passes may be more useful when starting in the defensive zone. 

Lastly, passing data can help coaches set matchups to either exploit or defend against their opponent’s strengths at defending certain pass types. Defensive units that struggle to control against behind the net passes could be exploited by forward groups strong at puck recovery after a dump-and-chase entry, or who excel at cycling the puck below the faceoff dots. 

## **7. Conclusions** 

Being able to properly account for pre-shot puck movement is a significant step forward for measuring the defensive abilities of a player, team, or system. Not only does passing data provide a descriptive picture of the types of chances that a team generates and suppresses, a simple expected goals model created using passing data can provide more predictive insights than existing public metrics. Quantifying specific passing patterns can expedite video review and allow a coach to zero in on how a team attacks via a certain passing sequence and how to better defend against it. The repeatability and predictability at the player level also can help identify potential free-agent or trade targets to address existing weaknesses or strengthen a team’s ability to defend against a certain opponent’s attacking style. 

Furthermore, in addition to exceeding the predictive powers of existing public defensive metrics, our 𝑥𝐺𝑝/60 is superior to existing public _offensive_ metrics as well. Identifying which passing plays offer a greater chance of a goal being scored can provide data-driven modifications to a team’s system, offering a more efficient route to goal-scoring. 





2017 Research Papers Competition 

7 


