<!-- source: 2017 Body Shots - Analyzing Shooting Styles in the NBA using Body-Pose Attributes.pdf -->



# **“Body Shots”: Analyzing Shooting Styles in the NBA using Body-Pose Attributes** 

Paper Track: Basketball Paper ID 1690 

## **1. Introduction** 

Much as no two people sound, look, walk, or write exactly alike, each NBA player has his own unique shooting style. A player’s individual form can undergo signi󰅭icant scrutiny. Forums are dedicated to analyzing which players have the most or least beautiful jump shot. Although interesting, such comparisons are subjective. Objective measures, requisite for meaningful comparisons, demand trajectories of players’ 3D body pose. The value of such player pose information is expansive, from predicting movements to quantifying the ideal pose for a movement. 

Over the past 󰅭ive years, the STATS SportVU [1] system has fueled a basketball _analytics revolution_ by providing player _x, y_ and ball _x, y, z_ coordinate trajectories in every NBA game. This has enabled analysis beyond traditionally-recorded statistics [2–12]. While extremely useful, there is a limitation; no body-pose data to inform how a player executes a speci󰅭ic skill, such shooting. 

Consider the player con󰅭iguration in the upper half of Figure 1. From SportVU data alone, this appears to be a very high-percentage opportunity. The shooter is spotted-up and wide-open. Why does he not score? And why does he wait until his defender has closed-out before shooting? To address such questions, we must look beyond the existing SportVU data. 





<!-- Start of picture text -->
How-<br><!-- End of picture text -->





Figure 1: In the (top) overhead view, this looks to be a very high-percentage shot opportunity. However, the (bottom) broadcast view shows the pose of the player and reveals an off-balance shooter as he tries to recover from a poorly placed pass. 



1 



The shooter’s appearance, shown in the lower half of Figure 1, reveals that during the defender’s closeout, the shooter is completely off-balance while he attempts to receive a poorly placed pass. Using the top-down view, the dot which represent the center-of-mass of the player, is just stationary which gives no information whether or not the player is balanced or not. Only via body-pose data can we infer such information. 

Capturing body-pose information (i.e., skeleton of a player) within a game situation, has for a long period of time been a lofty but unachievable goal. This is due to the inability of current technology to enable such capture in real-world settings. If someone wanted that information, they would have to 󰅭irst make the player wear a motion-capture suit with re󰅭lective markers and capture their movement and behavior in a controlled lab-setting with an array of cameras such as the one used by Vicon [13], which is the motion capture method used in making movies. 

However, very recent advances in computer vision and machine learning, with the help of GPU (Graphical Processing Units) and “deep learning” architectures have now made it possible to estimate the 3D body-pose information from a monocular camera view (i.e., broadcast camera-view) [14, 15]. This is exciting as it is now possible to capture body-pose information about each player at every frame, which can lead to 󰅭iner-grain analysis compared to analysis which just uses raw _x, y_ of a player’s center of mass. 

Given that we have such information, it begs the question _what types of analysis can we conduct with such information?_ In this paper, we focus on answering the following two questions: 

1. Do various types of body motion correlate with a made vs missed shot? **(Section 3)** , and 

2. How unique is Steph Curry’s shooting style in terms of body motion? Can we quantify how his body motion is different when he shoots compared to other shooters? **(Section 4)** 

To enable these types of questions, we 󰅭irst need to obtain a reasonable representation of the bodypose information. Inspired by the recent work in 󰅭ine-grain analysis using visual attributes [16], we 󰅭irst map the skeleton to 17 attributes **(see Section 2)** . From these attributes, we then run analysis on which attributes correlate with making a shot or not. 

As the shot-context, or the dif󰅭iculty of the shot taken can bias the analysis, we 󰅭irst segmented the shot into easy or tough shots. To partition these examples into those two categories, we used an expected point value (EPV) model to estimate the dif󰅭iculty of the shot based on the events, location and motion of the surrounding players. The intuition behind this approach is that if a player is being guarded closely, he may be unbalanced to actually take the tough shot. This is vastly different to the situation when a player has an open shot, and is unbalanced due to his poor technique of ball handling. As such, it was of the utmost importance to normalize for shot-context. 

For our analysis, we solely focus on three-point shots. In total, we have the positions of the shooter’s 2D body joints in 181-frame broadcast video clips of approximately1500 three-pointshots in the 2015/16 NBA season. 



2 







Figure 2: The (a) broadcast views and (b) corresponding player poses for six snapshots of four shots. Wedividedthetime-lineofashotinto󰅭ivebins: (blue)beforetheplayerpossessestheball, (pink)when the player possesses the ball before the shot, (black) immediately before the shot, (green) during the jump and release, and (red) after the player lands. The border colors of the snapshots correspond to their respective time-line bin. 

## **2. The Anatomy of a Three Point Shot** 

Before we start doing 󰅭ine-grain analysis of three-point shots, let’s 󰅭irst consider at a high-level what happens when a player takes a three-point shot in basketball. They set their feet, grasp the ball with their hands, jump and/or extend into the air, release the ball toward the basket, and land back on the 󰅭loor. At some point before setting their feet, they may have received a pass, dribbled the ball, and moved their body with or without the ball in any number of ways. 

These descriptions of the shooter’s body movements before, during, and after his shot form the basis of their high-level shot anatomy. To make concrete this shot anatomy, we divide the time-line of the shot into the following 󰅭ive bins, from the perspective of the shooter: (1) prior to possession of the ball, (2) after possession of the ball but prior to the moment just before the shot, (3) the moment immediately before the shot, (4) the jump and release, and (5) the landing and after. For each bin, we record attributes designed to capture the variety of movements the shooter may take, at different levels of granularity, from the direction of their full body movements to the foot they step with immediately before their shot. Outside of these designated bins, we include one additional attribute for overall balance during the full time-line of the shot. 

Figure 6 visualizes examples of this binning applied to four shots. On the left, we show the broadcast view of the shot (Figure 6(a)), and on the right we show the extracted body-pose which appears like a skeleton (Figure 6(b)). These illustrate the types of movement variation that may occur during each 



3 



|**Attribute**|**Description**|||**Values**|||
|---|---|---|---|---|---|---|
|**Balance**|“Overall”|balanced|off-balance||||
|**Move**<br>**Direction**|“Before<br>Pass”|no, set<br>left|yes, run<br>right|yes, walk<br>forward|yes, hop<br>backward||
|**Pass Quality**<br>**Pump Fake**<br>**Dribble**|“Before<br>Shot”|good<br>yes<br>yes|too high<br>no<br>no|too low|too left|too right|
|**Move**<br>**Direction**<br>**Turn**<br>**Footwork**|“Just<br>Before<br>Shot”|none<br>left<br>none<br>l. foot step|yes, step<br>right<br>yes, left<br>r. foot step|yes, run<br>forward<br>yes, right<br>hop|yes, walk<br>backward||
|**Set Foot Stance**|“vs. Shoulders”|aligned|wide|narrow|||
|**Jump Foot**||left foot|right foot|both feet|||
|**Legs During Jump**<br>**Legs During Fall**|“During<br>Shot”|straight up<br>together|swing fwd<br>wide|separate<br>split|||
|**Landing Foot**||left|right|both|||
|**Land Foot Stance**|“vs. Torso”|aligned|behind|right|left|front|
|**Move**|“After Shot”|none|left|right|forward|backward|



Table 1: Summarization of the attributes associated with three-point shots. In the 󰅭irst column, we de󰅭ine the 17 labelled attributes. The second column refers to when the attribute occurs during the shot. The last column corresponds to the values that each attribute can take. 

time bin. In particular, Brandon Rush, Klay Thompson, and Damian Lillard are seen moving in different ways (running, hopping, and turning) before and after receiving a pass. In contrast, Draymond Green is completely set for his shot as he waits for the pass. The landing of each player also noticeably differs, with Rush’s feet just in front of his torso, Thompson’s wide stance, Green’s completely-in-line body, and Lillard’s one-legged-landing. 

From these viewpoints, we then wanted to label each shot as a set of attributes which describes both the temporal and spatial characteristics of the shot. Table 1 summarizes our 17 anatomy attributes and their possible values. We labeled approximately 1500 three point shots in 29 Golden State Warriors games from the 2015/16 NBA regular season. Attributes were marked by viewing the broadcast footage in a three second window around the recorded time of the shot in the SportVU data. All direction attributes are egocentric for the shooter. Attributes that were not visible in that time window were left unmarked. Otherwise, the values of an attribute were mutually exclusive– for each visible attribute, only one value was marked. The set of attributes were de󰅭ined by a basketball experts who helped us generate this attribute dictionary. 

## **3. Discovering the Attributes of a Good and Bad Shot** 

### **3.1. Identifying Open vs. Tough Shots** 

As the shot-context, or the dif󰅭iculty of the shot taken can bias analysis, we 󰅭irst segmented the shot into easy or tough shots. To partition these examples into those two categories, we used an expected point value (EPV) model to estimate the dif󰅭iculty of the shot based on the events, location and motion of the surrounding players. To do this, we trained a classi󰅭ier based on spatial and temporal game con- 



4 



|**Method**|**Made**|**Missed**|**mAP**|
|---|---|---|---|
|Random Chance|61.8|37.7|50.0|
|Random Forest|67.4|42.0|54.7|
|Support Vector Machine|63.2|39.7|51.5|
|Logistic Regression|**69.8**|**44.3**|**57.1**|



Table 2: Average Precision (AP). 

text features computed from the SportVU trajectory and event data - similar to [8]. In the 󰅭ive second time window immediately prior to shot, we calculate the time since last event: free throw, 󰅭ield goal, rebound, dribble, pass, player possession, block, and drive. These times, along with player velocities comprised the temporal features. The spatial features, selected to capture the player con󰅭iguration at the moment of the shot, included the raw player and ball positions, and the angle and distance between each player and the ball. For consistency, spatial features were ordered by offense and defense, and distance to the ball. 

The training data for the classi󰅭ier was comprised of all three point shots in the remaining 53 regular season Warriors games in 2015/16. This data is complementary to the data used for the attributes. Table 2 reports the classi󰅭iers’ Average Precision for the two classes, made and missed shots, evaluated on the three point shots in the 29 games where we collected attribute labels. With mean Average Precision 57 _._ 1%, the Logistic Regression classi󰅭ier outperforms Random Forest (54 _._ 7%) and Support Vector Machine (51 _._ 5%) classi󰅭iers. All classi󰅭iers outperform random chance (50 _._ 0%). 

For an input shot, the Logistic Regression classi󰅭ier returns the likelihood the shot is successful. We classify shots as _open (or easy)_ or _tough_ by applying thresholds to this probability. In particular, shots with probability of success greater than 0 _._ 53 were considered open shots, and those with probability of success lower than 0 _._ 47 were considered tough shots. 

Now that we have partitioned the examples into open and tough shots, we can start the analysis. The rationale behind doing this is to normalize the examples as much as possible to minimize variance of other factors. The intuition is that if a player is being guarded closely, he may be unbalanced to actually take the tough shot. This is vastly different to the situation when a player has an open shot, and is unbalanced due to his poor technique of ball handling. As such, it was of the utmost importance to normalize for shot-context. Naturally, open shots can be either made or missed. Similarly, tough shots can sometimes fall and sometimes not - but knowing this context can help us discover which attributes make it more likely to make a shot or not. We explore this in the next subsection. 

### **3.2. Attribute Differences across Shot Opportunities** 

To address how a player’s shot attributes may affect his success in a shot, we consider whether there is a statistically signi󰅭icant difference between: 

1. the shooter’s attributes in tough, made shots ( _Tma_ ) versus in tough, missed shots ( _Tmi_ ) 

2. the shooter’s attributes in easy, made shots ( _Ema_ ) versus in easy, missed shots ( _Emi_ ) 

To address whether a player’s shot attributes may indicate if he has just taken a dif󰅭icult or easy shot, we consider whether there is a statistically signi󰅭icant difference between: 



5 



|**Attribute**|**Descrition**|**dof**||**p-v**|**alue**||
|---|---|---|---|---|---|---|
||**p**|**...**|_Tmi_v_Tma_|_Emi_v_Ema_|_Tmi_v_Emi_|_Tma_v_Ema_|
|**Balance**|“Overall”|1|0.222|0.114|0.939|0.644|
|**Move**|“Before|4|0.202|**0.004**|0.195|0.328|
|**Direction**|Pass”|4|0.483|0.454|**0.034**|0.201|
|**Pass Quality**|“|2<sup>_∗_</sup>|0.117|0.697|**0.049**|0.178|
|**Pump Fake**|Before<br>”|1|0.325|**0.020**|0.423|**0.048**|
|**Dribble**|Shot|1|0.161|0.329|0.315|0.153|
|**Move**|“|3|**0.070**|0.297|0.253|0.721|
|**Direction**|Just<br>|4|0.101|0.212|**0.064**|**0.013**|
|**Turn**|Before<br>Shot”|2|0.884|0.288|0.550|0.453|
|**Footwork**||2|**0.016**|0.420|0.265|**3e-9**|
|**Set Foot Stance**|“vs. Shoulders”|2|0.718|**0.096**|0.266|0.121|
|**Jump Foot**||1<sup>_∗_</sup>|0.318|0.268|0.422|0.338|
|**Legs During Jump**|“During|2|0.213|0.741|0.698|0.637|
|**Legs During Fall**|Shot”|2|0.559|**0.024**|0.803|**0.008**|
|**Landing Foot**||2|0.297|0.769|0.906|**0.006**|
|**Land Foot Stance**|“vs. Torso”|4|0.731|0.353|0.103|**0.003**|
|**Move**|“After Shot”|4|**0.002**|0.247|0.456|**1e-6**|



Table 3: The p-values for per-attribute Pearson’s Chi-squared tests for four shot comparisons: (1) tough, missed ( _Tmi_ ) vs. tough, made ( _Tma_ ); (2) easy, missed ( _Emi_ ) vs. easy, made ( _Ema_ ); (3) tough, missed vs easy, missed; and (4) bad, made vs good, made. For many attributes, the difference in distributions between shot classes is statistically signi󰅭icant at an _α_ = 0 _._ 1 signi󰅭icance level for at least one set of shot comparisons. 

3. the shooter’s attributes in easy, made shots ( _Ema_ ) versus in tough, made shots ( _Tma_ ) 

4. the shooter’s attributes in easy, missed shots ( _Emi_ ) versus in tough, missed shots ( _Tmi_ ) 

Figures 3, 4 illustrates comparisons of the attribute histograms for each of these. A visual inspection indicates clear differences between the attribute distributions, especially with movement before and after a shot. 

To quantify these differences, for each of these four cases, we perform a Pearson’s Chi-squared test on the histograms for each attribute. Individual tests for each attribute enables us to see exactly which attributes exhibit statistically signi󰅭icant differences between the shot classes. For pass quality, we combined all the bad pass attribute values, too low/high/left/right, into one bad pass value. Similarly, for jump foot, we combined left and right jump feet into one single leg jump value. For both of these attributes, there were not enough data points of the original attribute values for comparison. 

At a 90% con󰅭idence level, we observe many attributes with different distributions between the two compared shot classes. Table 3 reports the p-values. Each of the four comparisons display signi󰅭icant differences in at least three attributes. This suggests that indeed, various types of body motion do correlate with made versus missed shots, regardless of the game context. In comparing good, made shots versus bad, made shots, nearly half the attributes have statistically signi󰅭icant distributions between the two shot classes. This suggests the possibility of distinguishing between good and bad shots when 



6 





Figure 3: Pairwise attribute distributions for comparisons of made and missed shots in tough (left) and easy (right) game contexts. 







<!-- Start of picture text -->
(a) easy, missed (top) vs tough, missed (b) easy, made (top) vs tough, made<br><!-- End of picture text -->

Figure 4: Pairwise attribute distributions for comparisons of made and missed shots in easy and tough game contexts. The attributes are ordered from top to bottom identically to Table 1. 

observing the attributes of a made shot. 



7 





Figure 5: Stephen Curry’s shooting style vs everyone else in attribute space. The top bar corresponds with Curry’s attributes and the bottom is everyone else’s. Curry noticeably takes a higher proportion of off-balance shots compared to everyone else (attribute number one). 

## **4. Stephen Curry Shot Analysis via Attributes** 

It is widely acknowledged that Stephen Curry and the Golden State Warriors began a three-point shooting revolution in the NBA, with Curry being widely considered the best shooter in the league’s history. In this section, we analyze Curry’s shot via body-pose attributes. 

In Figure 6 we show some examples of Curry shooting from: (a) the broadcast view and (b) via his skeleton. From these examples, what we are attempting to show is that he tends to be the player with the most movement in all aspects of his shots compared to other shooters. In terms of his labelled attributes, we show a visualization of his attributes (top) compared to other shooters in the NBA (bottom) in Figure 5. The key take-away here is that Curry noticeably takes a higher proportion of off-balance shots compared to everyone else (attribute number one). 

Figure 7 visualizes Curry’s shooting style in made vs missed shots and in easy vs tough shots. Similar trends are observed for both comparisons. The 󰅭irst thing to notice about Curry’s shot is that he moves a lot! Whether it is before a pass, before his shot, during his shot, or after his shots, Curry is usually on the move. All this movement may contribute to the higher proportion of off-balance shots he takes compared to average. His higher proportion of off-balance shots correlates with a higher proportion of shots where he lands on a single foot. Whether he’s landing on a single foot or not, Curry often separates his legs as he’s landing on the 󰅭loor after releasing the ball. 



8 





(a) Broadcast View 



(b) Extracted Pose 

Figure 6: The (a) broadcast views and (b) corresponding player poses for 󰅭ive snapshots of 󰅭ive of Stephen Curry’s shots. We divided the time-line of a shot into 󰅭ive bins: (blue) before the player possesses the ball, (pink) when the player possesses the ball before the shot, (black) immediately before the shot, (green) during the jump and release, and (red) after the player lands. The border colors of the snapshots correspond to their respective time-line bin. 

## **5. Summary** 

In this work, we have introduced a novel, attribute-based representation for a shooter’s body pose. We demonstrated the value of this pose representation by showing how a shooter’s attributes differ for made and missed shots in different game contexts. And, we performed one case study using our attribute representation on Stephen Curry’s shooting style. 

## **References** 

- [1] STATS SportVU, www.sportvu.com. 

- [2] K. Goldsberry, “CourtVision: New visual and spatial analytics for the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2012. 

- [3] R. Maheswaran, Y. Chang, A. Henehan, and S. Danesis, “Destructing the rebound with optical tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2012. 



9 







- (a) made shots (top) vs missed shots 

Figure 7: Stephen Curry’s shooting style according to the attribute distributions. 

- [4] J. Wiens, G. Balakrishnan, J. Brooks, and J. Guttag, “To Crash or Not to Crash: A quantitative look at the relationship between the offensive rebounding and transition defense in the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2013. 

- [5] R. Masheswaran, Y. Chang, J. Su, S. Kwok, T. Levy, A. Wexler, and N. Hollingsworth, “The three dimensions of rebounding,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [6] P. Lucey, A. Bialkowski, P. Carr, Y. Yue, and I. Matthews, “How to get an open shot: Analyzing team movement in basketball using tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [7] A. Miller, L. Bornn, R. Adams, and K. Goldsberry, “Factorized point process intensities: A spatial analysis of professional basketball,” in _ICML_ , 2014. 

- [8] D. Cervone, A. D’Amour, L. Bornn, and K. Goldsberry, “POINTWISE: Predicting points and valuing decisions in real time with NBA optical tracking data,” in _MIT Sloan Sports Analytics Conference_ , 2014. 

- [9] Y. Yue, P. Lucey, P. Carr, A. Bialkowski, and S. Sridharan, “Learning Fine-Grained Spatial Models for Dynamic Sports Play Prediction,” in _ICDM_ , 2014. 

- [10] K. Wang, “Classifying NBA Offensive Plays Using Neural Networks,” in _MIT Sloan Sports Analytics Conference_ , 2016. 

- [11] J. G. A. McIntyre, J. Brooks and J. Wiens, “Recognizing and Analyzing Ball Screen Defense in the NBA,” in _MIT Sloan Sports Analytics Conference_ , 2016. 



10 



- [12] S. Zheng, Y. Yue, and P. Lucey, “Generating Long-term Trajectories Using Deep Hierarchical Networks,” in _Neural Information Processing Systems (NIPS)_ , 2016. 

- [13] V. M. C. Systems, www.vicon.com. 

- [14] D. B. M. H. V. Ramakrishna, D. Munoz and Y. Sheikh, “Pose Machines: Articulated Pose Estimation via Inference Machines,” in _European Conference on Computer Vision (ECCV)_ , 2014. 

- [15] V. R. S. Wei and Y. Sheikh, “Convolutional Pose Machines,” in _IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2016. 

- [16] A. Yu and K. Grauman, “Fine-Grained Comparisons with Attributes,” in _Visual Attributes_ , C. L. R. Feris and D. Parikh, Eds. Springer, 2004. 



11 


