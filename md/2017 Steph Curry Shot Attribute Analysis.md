<!-- source: 2017 Steph Curry Shot Attribute Analysis.pdf -->



# **“Body Shots”: Analyzing Shooting Styles in the NBA using Body Pose** 

Panna Felsen Patrick Lucey UC Berkeley and STATS STATS `panna@eecs.berkeley.edu plucey@stats.com` 

### **Abstract** 

In this work we develop a novel attribute-based representation of a basketball player’s body pose during his three point shot. The attributes are designed to capture the highlevel body movements of a player during the different phases of his shot, e.g., the jump and release. Analysis is performed on 1500 labeled three point shots. Normalized for game context, we use Pearson’s Chi-squaredtest toquantify differencesin attributedistributions for made and missed shots, where we observe statistically signi󰅭icant differences in distributions of attributes describing the style of movement, e.g., walk, run, or hop, in various phases of the shot. Similarly, with 󰅭ixed shot outcomes, across game contexts, we observe statistically signi󰅭icant differences in distributions of attributes describing the pass quality, direction of movement, and footwork. We also present a case study for Stephen Curry, where we observe that Curry moves much more than the average player in all phases of his shot and he takes a higher proportion of off-balance shots compared to the average player. 

## **1. Introduction** 

No two people sound, look, walk, or write exactly alike. Similarly, each NBA player has a unique shooting style. A player’s individual form can undergo signi󰅭icant scrutiny, as forums are dedicated to analyzing who has the most (or least) beautiful jump shot. Although interesting, such comparisons are subjective. Objective measures require trajectories of players’ body pose. 

Over the past 󰅭ive years, the STATS SportVU [1] system has fueled a basketball _analytics revolution_ by providing player _x, y_ and ball _x, y, z_ coordinate trajectories in every NBA game. This has enabled analysis beyond traditionally-recorded statistics, including quantifying players’ shooting range and offensive tendencies [2,3], introducing new rebounding metrics [4–6], and recognizing, understanding, and predicting team movements [7–12]. While the SportVU trajectory data has proven extremely useful, there is a limitation; it does not contain body pose data necessary to inform how a player executes a speci󰅭ic skill, such as shooting the basketball. 

Consider the player con󰅭iguration in the upper half of Figure 1. From the SportVU trajectory data alone, this appears to be a very high-percentage opportunity. The shooter is spotted-up and wide-open. Why does he not score? And why does he wait until his defender has closed-out before shooting? To address such questions, we must look beyond the existing SportVU trajectory data to the player’s body pose. The shooter’s appearance, in the lower half of Figure 1, reveals that during the defender’s close-out, the shooter is completely off-balance while he attempts to receive a poorly placed pass. These details can only be inferred from viewing the player’s body pose. 





1 







<!-- Start of picture text -->
How-<br>shows the pose of the player and reveals an off-balance shooter<br><!-- End of picture text -->





Figure 1: From SportVU data (top), this appears to be a very high-percentage shot opportunity. However, the broadcast view (bottom) shows the pose of the player and reveals an off-balance shooter recovering from a poorly placed pass. 

Capturing body pose information within an NBA game has long been a lofty but unachievable goal. Body pose data could previously only be collected for an individual wearing a motion-capture suit with re󰅭lective markers in a controlled lab-setting with an array of cameras, such as the one used by Vicon [13], the motion capture method used in 󰅭ilm production. However, recent advances in computer vision have signi󰅭icantly improved automated detection of a person’s 2D body pose from a monocular camera view, without the need for any dedicated motion capture setup [14,15]. These advances can potentially enable the capture of each player’s body pose throughout the broadcast video. 

Imagine that we have such pose information, it begs the question _what types of analysis can we conduct with player pose data?_ In this paper, we address the following two questions: 

1. Do various types of body movements correlate with a made vs missed shot? **(Section 3)** 

2. How unique is Steph Curry’s shooting style in terms of his body movements? **(Section 4)** 

To answer these types of questions, we 󰅭irst need to obtain a meaningful representation of the body pose. Inspired by work in 󰅭ine-grain analysis using visual attributes [16], we map the skeleton to 17 attributes **(see Section 2)** that describe the movements of a player during his shot, such as his overall balance throughout the shot. Analysis is performed in this attribute space. 

In our analysis, we focus solely on three point shot attempts. Since the advent of the three point shot, it has gone from “gimmick” to “vital”, a transition headlined by Stephen Curry’s record-breaking three point shooting in the 2012/13 NBA season. The three point shot is currently relevant for NBA teams’ offensive strategies. Isolating analysis to the three point shots poses two key advantages: 1) it provides a consistent game context across which to compare, and 2) the range of the shot necessitates a jump shot form, reducing the variability in body movements during the shot. 





2 







Figure 2: The (a) broadcast views and (b) corresponding player poses for six temporal snapshots of four three point shots. We divided the timeline of a shot into 󰅭ive bins: (blue) before the player possesses the ball, (pink) when the player possesses the ball before the shot, (black) immediately before the shot, (green) during the jump and release, and (red) after the player lands. The border colors of the snapshots correspond to their respective timeline bin. 

## **2. The Anatomy of a Three Point Shot** 

Consider at a high level what happens when a player takes a three point shot in basketball. They set their feet, grasp the ball with their hands, extend into the air, release the ball toward the basket, and land back on the 󰅭loor. At some point before setting their feet, they may have received a pass, dribbled the ball, and moved their body with or without the ball in a number of different ways. 

These descriptions of the shooter’s body movements before, during, and after his shot form the basis of his high-level shot anatomy. To make concrete this shot anatomy, we divide the timeline of the shot into the following 󰅭ive bins, from the perspective of the shooter: (1) prior to possession of the ball, (2) after possession of the ball but prior to the moment just before the shot, (3) the moment immediately before the shot, (4) the jump and release of the ball toward the basket, and (5) after the landing. 

Figure 2 visualizes examples of this binning applied to four shots. On the left, we show the broadcast view of the shot (Figure 2a), and on the right we show the extracted body pose skeleton (Figure 2b). These illustrate the types of movement variation that may occur during each time bin. For example, Rush, Thompson, and Lillard are seen moving in different ways (running, hopping, and turning) before and after receiving a pass. In contrast, Green is completely set for his shot as he waits for the pass. The landing of each player also noticeably differs, with Rush’s feet just in front of his torso, Thompson’s wide stance, Green’s completely-in-line body, and Lillard’s one-legged-landing. 





3 



|**Attribute**|**Bin**|||**Values**|||
|---|---|---|---|---|---|---|
|**Balance**|Overall|balanced|off-balance||||
|**Move**|1|no, set|yes, run|yes, walk|yes, hop||
|**Direction**|()|left|right|forward|backward||
|**Pass Quality**||good|too high|too low|too left|too right|
|**Pump Fake**|(2)|yes|no||||
|**Dribble**||yes|no||||
|**Move**||none|yes, step|yes, run|yes, walk||
|**Direction**|3|left|right|forward|backward||
|**Turn**|()|none|yes, left|yes, right|||
|**Footwork**||l. foot step|r. foot step|hop|||
|**Set Foot Stance**|vs. Shoulders|aligned|wide|narrow|||
|**Jump Foot**||left foot|right foot|both feet|||
|**Legs During Jump**<br>**Legs During Fall**|(4)|straight up<br>together|swing fwd<br>wide|separate<br>split|||
|**Landing Foot**||left|right|both|||
|**Land Foot Stance**|vs. Torso|aligned|behind|right|left|front|
|**Move**|(5)|none|left|right|forward|backward|



Table 1: The attributes associated with three point shots. The 󰅭irst column provides the name for each attribute, the second column lists the associated timeline bin, and the last column corresponds to the values that each attribute can take. 

From these viewpoints, we labeled each shot as a set of attributes which describes both the temporal and spatial characteristics of the shot. In particular, for each bin, we record attributes designed to capture the various movements the shooter may perform, from the direction of movement to type of movement to which limb performed the movement. We also include one additional attribute for overall balance during the full timeline of the shot. Basketball experts helped us generate the attribute dictionary. Table 1 summarizes our 17 anatomy attributes and their possible values. 

In total, we labeled approximately 1500 three point shots in 29 Golden State Warriors games from the 2015/16 NBA regular season. Attributes were marked by viewing the broadcast footage in a three second window around the recorded time of the shot in the SportVU data. All direction attributes are egocentric for the shooter. Attributes that were not visible in that time window were left unmarked. Otherwise, the values of an attribute were mutually exclusive; for each visible attribute, only one value was marked. 

## **3. Shot Attribute Analysis** 

#### **3.1. Identifying Open vs. Tough Shots** 

As the shot-context, or shot dif󰅭iculty, can bias analysis, we 󰅭irst separated the shots into _open_ or _tough_ shots. We used an expected point value model to estimate the dif󰅭iculty of the shot based on the events prior to the shot (e.g., dribble, pass, etc.) and the location and motion of the players on the court. To do this, we trained a classi󰅭ier based on spatial and temporal game context features computed from the SportVU trajectory and event data - similar to [8]. In the 󰅭ive second time window immediately 





4 



|**Method**|**Made**|**Missed**|**mAP**|
|---|---|---|---|
|Random Chance|61.8|37.7|50.0|
|Random Forest|67.4|42.0|54.7|
|Support Vector Machine|63.2|39.7|51.5|
|Logistic Regression|**69.8**|**44.3**|**57.1**|



Table 2: Using spatial and temporal features captured from the SportVU trajectories, we trained linear and non-linear classi󰅭iers to identify made and missed shots. On unseen (test) data, the probability of a made shot (output from the classi󰅭ier) provides the expected point value for the shot. This table lists the Average Precision (AP) and mean AP for made and missed shots for different classi󰅭iers. 

prior to shot, we calculate the time since last event: free throw, 󰅭ield goal, rebound, dribble, pass, player possession, block, and drive. These times, along with player velocities comprised the temporal features. The spatial features, selected to capture the player con󰅭iguration at the moment of the shot, included the player and ball _x, y_ positions, and the angle and distance between each player and the ball. For consistency, spatial features were ordered by offense and defense, and distance to the ball. 

The training data for the classi󰅭ier was comprised of all three point shots in the remaining 53 regular season Warriors games in 2015/16. This data is complementary to the data with attribute labels. Table 2 reports the classi󰅭iers’ Average Precision for the two classes, made and missed shots, evaluated on the three point shots in the remaining 29 games (the games with the attribute labels). With mean Average Precision 57 _._ 1%, the Logistic Regression classi󰅭ier outperforms Random Forest (54 _._ 7%) and Support Vector Machine (51 _._ 5%) classi󰅭iers. All classi󰅭iers outperform random chance (50 _._ 0%). 

For an input shot, the Logistic Regression classi󰅭ier returns the likelihood the shot is successful. We classify shots as open or tough by applying thresholds to this probability. In particular, shots with probability of success greater than 0 _._ 53 were considered _open_ shots, and those with probability of success lower than 0 _._ 47 were considered _tough_ shots. 

Now that we have partitioned the examples into open and tough shots, we can start the analysis. Separating the shots by dif󰅭iculty normalizes the examples as much as possible to minimize variance of other factors. The intuition is that if a player is being guarded closely, he may be off-balance in order to actually take the tough shot. This is vastly different from the situation where a player has an open shot, and is off-balance due to poor ball handling. As such, it was of the utmost importance to normalize for shot context. Naturally, open shots can be either made or missed. Similarly, tough shots can sometimes fall and sometimes not - but knowing this context can help us discover which attributes make it more likely to make a shot or not. We explore this in the next subsection. 

#### **3.2. Attribute Correlation with Game Context and Shot Outcome** 

In this section we explore the correlation between body movements and shot success in the two different game contexts, open and tough shots. We consider two settings: 1) the game contexts are 󰅭ixed and we compare attributes for made versus missed shots in each game context, and 2) the shot outcome is 󰅭ixed and we compare attributes for open versus tough shots for each shot outcome. 

In the 󰅭irst setting, we address how a player’s attributes may in󰅭luence his shot success. For a 󰅭ixed game context, differences in attribute distributions between made and missed shots indicate corre- 





5 



|**Attribute**|**Bin**|**dof**||**p-v**|**alue**||
|---|---|---|---|---|---|---|
|||**...**|_Tmi_v_Tma_|_Omi_v_Oma_|_Tmi_v_Omi_|_Tma_v_Oma_|
|**Balance**|Overall|1|0.222|0.114|0.939|0.644|
|**Move**|1|4|0.202|**0.004**|0.195|0.328|
|**Direction**|()|4|0.483|0.454|**0.034**|0.201|
|**Pass Quality**||2<sup>_∗_</sup>|0.117|0.697|**0.049**|0.178|
|**Pump Fake**|(2)|1|0.325|**0.020**|0.423|**0.048**|
|**Dribble**||1|0.161|0.329|0.315|0.153|
|**Move**||3|**0.070**|0.297|0.253|0.721|
|**Direction**||4|0.101|0.212|**0.064**|**0.013**|
|**Turn**|(3)|2|0.884|0.288|0.550|0.453|
|**Footwork**||2|**0.016**|0.420|0.265|**3e-9**|
|**Set Foot Stance**|vs. Shoulders|2|0.718|**0.096**|0.266|0.121|
|**Jump Foot**||1<sup>_∗_</sup>|0.318|0.268|0.422|0.338|
|**Legs During Jump**||2|0.213|0.741|0.698|0.637|
|**Legs During Fall**|(4)|2|0.559|**0.024**|0.803|**0.008**|
|**Landing Foot**||2|0.297|0.769|0.906|**0.006**|
|**Land Foot Stance**|vs. Torso|4|0.731|0.353|0.103|**0.003**|
|**Move**|(5)|4|**0.002**|0.247|0.456|**1e-6**|



Table 3: The p-values for per-attribute Pearson’s Chi-squared tests for four shot comparisons: (1) tough, missed ( _Tmi_ ) vs. tough, made ( _Tma_ ); (2) open, missed ( _Omi_ ) vs. open, made ( _Oma_ ); (3) tough, missed vs open, missed; and (4) tough, made vs open, made. For many attributes, the difference in distributions between shot classes is statistically signi󰅭icant at an _α_ = 0 _._ 1 signi󰅭icance level for at least one set of shot comparisons. *We combined: all the bad pass attribute values, too low/high/left/right, into one bad pass value; and left and right jump feet into one single leg jump value. For both of these attributes, there was insuf󰅭icient data of each attribute value for quantitative comparison. 

lation between those attributes and shot success. For each attribute, we evaluate whether there is a statistically signi󰅭icant difference between the distribution of: 

1. the shooter’s attributes in tough, made shots ( _Tma_ ) versus in tough, missed shots ( _Tmi_ ) 

2. the shooter’s attributes in open, made shots ( _Oma_ ) versus in open, missed shots ( _Omi_ ) 

In the second setting, we address how a player’s attributes may indicate whether he has just taken a tough or open shot. For a 󰅭ixed shot outcome, differences in attribute distributions between open and tough shots indicate correlation between those attributes and game context. For each attribute, we evaluate whether there is a statistically signi󰅭icant difference between the distribution of: 

3. the shooter’s attributes in open, made shots ( _Oma_ ) versus in tough, made shots ( _Tma_ ) 

4. the shooter’s attributes in open, missed shots ( _Omi_ ) versus in tough, missed shots ( _Tmi_ ) 

Figures 3, 4 illustrate comparisons of the attribute histograms for each of these settings. Qualitatively, we observe clear differences between the attribute distributions, especially with movement before 





6 





Figure 3: Pairwise comparison of all players’ attribute distributions for made (top bar) and missed (bottom bar) shots in tough (left) and easy (right) game contexts. 



Figure 4: Pairwise comparison of all players’ attribute distributions for open (top bar) and tough (bottom bar) shots in missed (left) and made (right) shot outcomes. 





7 







Figure 5: The (a) broadcast views and (b) corresponding player poses for snapshots of 󰅭ive of Stephen Curry’s shots. We use the same timeline bins described in Section 2 to partition the shot into phases. 

and after a shot. To quantify these differences, for each of the four cases, we perform a Pearson’s Chisquared test on the histograms for each attribute. Individual tests for each attribute enable us to isolate which attributes exhibit statistically signi󰅭icant differences between the shot classes. 

Table 3 reports the p-values for these hypothesis tests. At a 90% con󰅭idence level, we observe many attributes with statistically signi󰅭icant differences in distributions. Each of the four comparisons display signi󰅭icant differences in at least three attributes. 

For 󰅭ixed game context (Figure 3), this suggests that indeed, various types of body motion do correlate with made versus missed shots, regardless of the game context. In particular, for tough shots: right foot step just prior to the shot and walking instead of running just prior to the shot have a higher proportion in the distribution for made shots versus missed shots. We also observe the phenomenon that players are more likely to freeze and watch a tough missed shot, i.e., not move after landing, than after a tough made shot. And for open shots: no movement prior to receiving a pass, no pump fake, narrow set foot stance, and legs split during fall all have a higher proportion in the distribution for made shots than for missed shots. 

For 󰅭ixed shot outcome (Figure 4), the p-values indicate that various types of body movements corre- 





8 





Figure 6: In tough shots, (left) Stephen Curry’s (top bar) shooting style vs everyone else (bottom bar) in attribute space. Curry noticeably takes a higher proportion of off-balance and off a dribble shots. For comparison, (right) Klay Thompson’s (top bar) style is also compared with everyone else (bottom bar); he noticeably takes a higher proportion of balanced catch and shoot threes. 

late with a tough or open shot. Speci󰅭ically, for made shots: a pump fake, moving backward just prior to the shot, left foot step just prior to the shot, legs split during fall, land on right foot, land with feet and torso aligned all have a higher proportion in the distribution for easy shots than for tough shots. Again we observe the freezing phenomenon after tough made shots, but not after open made shots. And for missed shots: a good pass prior to the shot, and left/forward movement just prior to the shot have a higher proportion in the distribution for open shots than for tough shots. 

## **4. Stephen Curry Shot Attribute Analysis** 

The recent three point shooting revolution in the NBA has frequently been headlined by the Golden State Warriors and Stephen Curry, who is widely regarded as the best shooter in the league’s history. In this section, we analyze Curry’s three point shot in the context of the pose attributes, and compare his style with all of the other players in our dataset. 

Figure 5 illustrates examples of Curry’s shots in the broadcast view and skeleton pose view with the same shot timeline bins as described in Section 2. Qualitatively, we observe that Curry tends to strike more extreme poses than the average player, and a higher percentage of his shots are off a dribble, not a pass. Figure 6 provides the side-by-side comparison of Curry’s shot attributes (top bar) and other NBA player shot attributes (lower bar) for tough shots. Most striking is that Curry noticeably takes a higher proportion of off-balance shots compared to everyone else. The attributes also con󰅭irm that he shoots more frequently off a dribble as compared to other players, and he moves more than other 





9 





Figure 7: On the left, Curry’s shooting style for made (top) and missed (bottom). On the right, Curry’s shooting style for open (top) and tough (bottom) shots. 

players in every phase of his shot. 

Figure 7 visualizes Curry’s shooting style in made vs missed shots and in open vs tough shots. Similar trends are observed for both comparisons. The 󰅭irst thing to notice about Curry’s shot is that he moves a lot! Whether it is before a pass, before his shot, during his shot, or after his shots, Curry is usually in motion. All this movement may contribute to the higher proportion of off-balance shots he takes compared to average. His higher proportion of off-balance shots correlates with a higher proportion of shots where he lands on a single foot. Whether he’s landing on a single foot or not, Curry often separates his legs as he’s landing on the 󰅭loor after releasing the ball. 

## **5. Summary** 

In this work, we have introduced a novel, attribute-based representation for a player’s body pose during a three point shot attempt. We demonstrated the value of this pose representation by quantifying attribute differences for made and missed shots in 󰅭ixed game contexts, addressing which attributes may be important for (or predictive of) successful shot outcomes. We also quanti󰅭ied attribute differences for open and tough shots with 󰅭ixed shot outcome, addressing which attributes may inform the shot dif󰅭iculty. And, we performed one case study using our attribute representation on Stephen Curry’s shooting style. 





10 



## **References** 

[1] STATS SportVU, www.sportvu.com. 

- [2] K. Goldsberry, “CourtVision: New visual and spatial analytics for the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2012. 

- [3] A. Miller, L. Bornn, R. Adams, and K. Goldsberry, “Factorized point process intensities: A spatial analysis of professional basketball,” in _ICML_ , 2014. 

- [4] R. Maheswaran, Y. Chang, A. Henehan, and S. Danesis, “Deconstructing the rebound with optical tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2012. 

- [5] J. Wiens, G. Balakrishnan, J. Brooks, and J. Guttag, “To Crash or Not to Crash: A quantitative look at the relationship between the offensive rebounding and transition defense in the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2013. 

- [6] R. Masheswaran, Y. Chang, J. Su, S. Kwok, T. Levy, A. Wexler, and N. Hollingsworth, “The three dimensions of rebounding,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [7] P. Lucey, A. Bialkowski, P. Carr, Y. Yue, and I. Matthews, “How to get an open shot: Analyzing team movement in basketball using tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [8] D. Cervone, A. D’Amour, L. Bornn, and K. Goldsberry, “POINTWISE: Predicting points and valuing decisions in real time with NBA optical tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [9] Y. Yue, P. Lucey, P. Carr, A. Bialkowski, and S. Sridharan, “Learning Fine-Grained Spatial Models for Dynamic Sports Play Prediction,” in _ICDM_ , 2014. 

- [10] K. Wang, “Classifying NBA Offensive Plays Using Neural Networks,” in _MIT Sloan Sports Analytics Conference_ , 2016. 

- [11] J. G. A. McIntyre, J. Brooks and J. Wiens, “Recognizing and Analyzing Ball Screen Defense in the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2016. 

- [12] S. Zheng, Y. Yue, and P. Lucey, “Generating Long-term Trajectories Using Deep Hierarchical Networks,” in _Neural Information Processing Systems (NIPS)_ , 2016. 

- [13] V. M. C. Systems, www.vicon.com. 

- [14] D. B. M. H. V. Ramakrishna, D. Munoz and Y. Sheikh, “Pose Machines: Articulated Pose Estimation via Inference Machines,” in _European Conference on Computer Vision (ECCV)_ , 2014. 

- [15] V. R. S. Wei and Y. Sheikh, “Convolutional Pose Machines,” in _IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2016. 

- [16] A. Yu and K. Grauman, “Fine-Grained Comparisons with Attributes,” in _Visual Attributes_ , C. L. R. Feris and D. Parikh, Eds. Springer, 2004. 





11 


