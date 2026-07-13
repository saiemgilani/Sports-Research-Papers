<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2018/2018 - Wide Open Spaces A statistical technique for measuring space creation in professional soccer - Unknown Authors.pdf -->



# **Wide Open Spaces: A statistical technique for measuring space creation in professional soccer** 

Other Sports Track Paper Id: 5675 

## **1 Introduction** 

Soccer analytics has long focused on the outcomes of discrete, on-ball events; however, much of the sport’s complexity resides in off-ball events. In the words of Johan Cruyff: “it is statistically proven that players actually have the ball 3 minutes on average. So, the most important thing is: what do you do during those 87 minutes when you do not have the ball? That is what determines whether you are a good player or not”. The creation and closure of spaces is a recurrent subject in observation-based tactical analysis, yet it remains highly unexplored from a quantitative perspective. 

We present a method for quantifying spatial value occupation and generation during open play. Here direct space occupation refers to space created for oneself, while space generation refers to opening up space for teammates by attracting opponents out of position. We �irst build a novel parametric pitch control model that incorporates motion information, relative distance to the ball, and player position in order to provide a smooth surface of potential ball control. Through the mixture of all players’ control surfaces we obtain a fuzzy degree of potential ball control at the team level in any given moment. We also construct a model for the relative value of any pitch position, based on the position of the ball and using feed forward neural networks. From all this (a player’s invested pitch zones, a team’s pitch control, and the relative value of each zone), we employ the full spatio-temporal dynamics of each player to construct two novel spatial value creation metrics, accounting for both occupation and generation of spaces. 

Through the analysis of a �irst division Spanish league match, we show a handful of approaches to better understand a missing key factor for performance analysis in soccer: off-ball attacking dynamics. The quanti�ication of space occupation gain and space generation allows us to observe Sergio Busquets’ high relevance during positional attacks through his pivoting skills, the dragging power of Luis Suarez to generate spaces for his teammates, and the capacity of Lionel Messi to occupy spaces of value with smooth movements along the �ield, among many other characteristics. 

The level of detail we can reach with automated quantitative analysis of space dynamics is beyond what it can be reached by observational analysis. Thus, the capacity of evaluating space occupation and generation opens the door for new research on off-ball dynamics that can be applied in speci�ic matches and situations, and directly integrated into coaches analysis. With this insight, this information can be used not only to better evaluate players’ contribution to their teams, but also to improve their positioning and movement through coaching, providing a key competitive advantage in a complex and dynamic sport. 





2018 Research Papers Competition Presented by: 

1 



## **2 Occupation and Generation of Spaces** 

During the last two decades, successful elite soccer teams have been increasingly adapting possessioncentered playing styles, especially within Spanish, English and German leagues. Beyond the basic idea of simply controlling the ball as much as possible, these strategies compromise of a large set of on-ball and off-ball actions to generate better chances to score goals. Some of these are: creating superiorities (numerical, positional or qualitative), creating disorder on the opponents defense through movements and team-collaboration, building up plays from the goalkeeper, and executing passes with offensive intention, among many others. Above all these actions there is a main underlying concept: the generation and occupation of spaces. Pep Guardiola once said: 

We have to pass the ball, yes, but with clear intention. Pass it to drag players to one side and creating space in the opposite side. Then, move the ball there. That’s our game. 

Occupying space on the �ield is fundamentally about a player’s act of continually positioning himself in an area of high value. The value of space can be de�ined in terms of the relative position of the ball, the closeness to the opponent goals, and more speci�ically the level of ownership of space, regarding the distance to close opponents and density of opponents within the given area. Furthermore, we can cluster the types of occupation of space depending on the speed of the player. Speci�ically we identify two types: active occupation, when the player moves at running speed to earn the space, and passive occupation, when the player is below running speed (jogging or walking). For instance, if a player is closely marked and then runs towards a free space faster than the opponent, he will obtain a gain on owned space through active space occupation. As another example, if the player is walking towards a given area and near opponents move away from that area, the player will be gaining space through passive occupation. 

A more complex concept is that of space generation. We de�ine the generation of space as the action of dragging opponents out of certain areas to create new available space in previously covered areas. Specifically, we identify situations where a player drags an opponent away from another teammate whom the opponent was close to originally. The dragging concept is, at its simplest, creating space for a teammate by pulling their defender towards oneself. Notice that unoccupied space could also be generated when dragged players leave a clear area; however, we are not considering this case for this study. Similarly to the Space Occupation Gain (SOG) concept above, later we also explore the concept of Space Generation Gain (SGG). In this way, we separate out space created for oneself from space created for teammates, in both a passive and active manner. 

Figure 1 presents an example for both space occupation and space generation during an of�icial Spanish �irst division match. The three images show a process where Andrés Iniesta moves to clear up space away from the ball and then attacks a high value space inside the box. When he moves to this space he drags three defenders towards himeslf while also receiving a pass. The attraction of the three defenders leaves open space for Lionel Messi, who in this newfound space receives a pass free of a mark, and subsequently sends a lob pass onwards for Suarez, who meanwhile was running towards the goal line in search of space of value to score. A more detailed video example of occupation and generation of spaces can be seen at the following link, where players are highlighted when adding space for themselves or teammates: `http://www.lukebornn.com/sloan/space_occupation_1.mp4` 

Before providing explicit details on how to calculate space occupation and generation, we �irst need a better notion of space ownership and value, as creating space for your own goalkeeper who is 80 meters 





2018 Research Papers Competition Presented by: 

2 





**Figure 1:** A game situation presenting both space occupation and generation. From left to right: in the �irst frame Iniesta moves back to occupy a space of value with higher control. In the second frame, Iniesta observes an open space to attack. He moves towards the space, dragging three defenders. In the third frame, the three dragged defenders leave an open space for Messi that can now receive the ball free of mark, while Suarez runs towards the goal line enabling him to receive a pass. 

behind the location of play is worth much less than creating space in high-threat areas nearer the ball and goal. The next two sections present a novel pitch control model for evaluating space ownership, and a dynamical model for space value according to ball and player position. 

## **3 Modelling Pitch Control: A Parametric Approach** 

Pitch control is a recurrent concept in the analysis of space dominance in team sports. It can be de�ined as the degree or probability of control that a given player (or team) has on any speci�ic point in the available playing area. The emerge of player tracking data has given rise to different pitch control (or dominant region) models. A widely applied model is the Voronoi Tesselation, which takes into account the position of all players on the �ield and calculates the closest player to each given spatial point, �inding dominance cells for each player. This model has been used for quantifying the dominant area of attacking and defending teams in constrained playing areas [1], to evaluate the space dominance based on passing behaviour [2], to improve models for pass probabilities [3], and to evaluate positional value of players on rebounds in basketball [4], among many other applications. From the original model for team sports presented by Taki and Hasegawa [5] there have been several extensions for faster computation, as well as extensions to incorporate motion and weighted valuation of dominant space [3, 6]. Beyond its bene�its, all the different Voronoi Tesselation-based approaches start from the idea of �inding regions that are exclusively dominated by a given player. This concept disregards the concept that ownership of space is continuous, not discrete, with uncertainty in who controls areas between players. Also, the distance between players and the ball its also believed to in�luence the relative positioning and degree of space control, especially for sports with wider playing spaces such as soccer; however, this is not taken into account by the mentioned approaches. 





2018 Research Papers Competition Presented by: 

3 



We propose a novel pitch control model that takes into account the location, velocity and distance to the ball of all the players, providing a smooth surface of control for each team. For any given location, the in�luence that every player has in that place is computed and summarized, resulting in a probability of control. An additional objective of this approach was to provide a model that could be applied in a given data frame, without requiring signi�icant data for learning its parameters. This is particularly important for clubs in competitions such as the Spanish League where tracking data is not available for direct usage. Also, such a model would allow easier reproducibility. 

### **3.1 Player In�luence Area** 

Depending on their location in time, player’s might have different levels of in�luence on nearby zones. When a player is far away from the ball his level of in�luence can be understood as a wider area, based on the reasoning that if the ball moves towards the player he would have a more time to reach the ball within a larger space. On the opposite, when closer to the ball, the player has a less possibilities of reaching the ball if it moves from its current location. Also, the magnitude and direction of speed plays an important role in de�ining the area of in�luence. A player at running speed might have more in�luence in the areas in the direction of speed compared to if they were walking or jogging. Further, the player may have higher levels of in�luence in close spaces within its in�luence area than in farther spaces. 

Based on this reasoning we propose de�ining the player in�luence area through a bivariate normal distribution, whose shape can be adjusted to account for the player’s location, velocity, and relative distance to the ball. At any given location a degree of in�luence or control can be queried through the distribution’s probability density function. 

Speci�ically, the player’s in�luence _I_ at a given location _p_ for a given player _i_ at time _t_ is de�ined by a bivariate normal distribution with mean _µi_ ( _t_ ) and covariance matrix Σ _i_ ( _t_ ), given the players speed vector _s_ and speed rotation angle _θ_ . For a given location in space _p_ at time _t_ , the probability density function of player _i_ in�luence area is de�ined by a standard multivariate normal distribution. The player’s in�luence likelihood is then de�ined as the normalization of _f_ at the given location _p_ by the value of _f_ at player’s current location _pi_ ( _t_ ), as shown in Equation 1. 



This formulation provides an initial model for obtaining a degree of in�luence within a [0 _,_ 1] range for any given location on the �ield. The mean and covariance matrix can be dynamically adjusted to provide a player dominance distribution that accounts for location and velocty. In Appendix A.1 we provide speci�ic details for this equation. 

Figure 2 presents the player in�luence area in two different situations regarding player’s distance to the ball and velocity. Here we can observe how depending on the distance to the ball the range of in�luence of the player varies. Also, the distribution of player in�luence is reshaped to be oriented according the rotation angle of the speed vector and stretched in relation to the magnitude of speed. If the player is in motion, the distribution is translated so the higher level of in�luence is near points where the player can reach faster, according to his speed. 





2018 Research Papers Competition Presented by: 

4 







**(a)** Player in�luence area for player in possession of the **(b)** Player in�luence area for player 15 meters away from ball and no speed (lower than walking speed) the ball, running at 6.36 m/s in a 45 degrees angle 

**Figure 2:** Two situations representing the player in�luence area 

### **3.2 Modelling Team Pitch Control** 

When de�ining a team’s degree of control at any given location on the �ield, it is desirable to take into account the level of in�luence each individual player of both teams is having on that point. Since many players can have in�luence at a given location at a certain time, the model should be able to account for the aggregated in�luence of each player and provide a value of control within a continuous range, instead of strict areas such as the case of Voronoi Tesselation. 

Based on this, we present a pitch control model that summarizes the level of in�luence of every player, and outputs a degree of control for any part of the pitch. Equation 2 presents the pitch control level at a location _p_ at time _t_ , where _i_ and _j_ refers to the index of the player in each opposing team. Here the logistic function transforms the substraction of the accumulated individual in�luence area of each team into a degree of control within then [0 _,_ 1] range. Also, since we are de�ining a team-oriented pitch control model, a single player without any in�luence of any other player at its current location only controls _logistic_ (1) = 0 _._ 73 of the space. This provides the need of higher density of players near a given area to provide higher level of control in that area. For the statistically-inclined, note that this formulation represents the probability of control of a given team, where each team’s latent surface is captured by a kernel-based non-parametric point process. 



where _σ_ is the logistic function. Since the pitch control model follows the de�inition of player in�luence area in Figure 2, the model is taking into account the location of the ball, player’s speed and the location of all the players on the �ield. Figure 7 presents the pitch control surface in a given situation of the match. At 





2018 Research Papers Competition Presented by: 

5 





**Figure 3:** Pitch control surface indicating the degree of control for team in red. Arrows show the magnitude and direction of speed, and contour lines allow to visualize the surface geometry. Numbers in white indicate the pitch control value at their drawing location. Axis dimensions are in meters/ 

location (82 _,_ 8), near the ball, it can be observed clearly how the yellow team’s high density provides lower level of control for the red team near the ball. Also the speed vector of the (red team) player in possession of the ball provides the red team an advantage in the running direction. At location (80 _,_ 25), the red player is creating a positional advantage. Meanwhile, at location (50 _,_ 30) the yellow player has minimal control of space because of the high density provided by the three surrounding opponent players. For a single time frame, this pitch control model provides a synthesis of player locations, player velocities and ballrelative positioning in one variable. Also, by exploiting the dynamics of pitch control time, it becomes a versatile tool for evaluating multiple types of spatio-temporal characteristics of the game such as the creation of positional advantages, the in�luence of density and pressure speed in defending situations, and the creation and generation of spaces. 





2018 Research Papers Competition Presented by: 

6 



## **4 Quantifying Pitch and Space Value** 

Although the control of space is a fundamental element to identify occupation and generation of spaces, we still need an additional part of the equation: the value of space. The sole fact of moving for �inding better passing options is an advantage itself. However, it can be easily argued that not every space has the same value. A trivial method for determinating the value of space is its distance to the opponent goal. Its well known that spaces near the goal have an increased value, given the advantage that would provide to dominate them. But exploring more deeply into the dynamics of soccer, and based on the opinion from F.C. Barcelona expert analysts, it can be also argued that the value of space changes dynamically depending on multiple positional factors, such as the position of the ball and the players. In order to quantify in a detailed way the value of the space generated or occupied we provide a novel model for �inding the relative pitch value on every position of the �ield, depending on the location of the ball. The following link presents a video where the dynamic evaluation of pitch value depending on the ball position, as detailed below, can be observed: `http://www.lukebornn.com/sloan/field_value.mp4` . 

Instead of de�ining a priori a model for space valuation we would like to extract a sense of space value from the spatio-temporal behaviour of players during multiple matches. For this we set the following hypothesis: considering a suf�iciently high number of situations, the defending team distributes itself throughout the �ield in a manner which covers high value spaces. Although it is clear that at any given point defenders will deviate based on overloads, speci�ic offensive player positioning, and other scenarios, in general, most players will remain close to high value areas. An extreme example of this will be the case where the attacking team places all players in the middle of �ield. Its arguable that, although this would impact the position of the defending team, they will most probably still keep players near the box and their own goal. Note that similar ideas are used when identifying defensive matchups based on defender locations in basketball [7]. 

Based on this, we propose learning the sum in�luence that a defensive team would have in a given location on the �ield, given the location of the ball. Let _Vi,j_ ( _t_ ) be the value of location _pi,j_ of the pitch at time _t_ , and let _pb_ ( _t_ ) be the location of the ball at time _t_ , we want to learn a function _fn_ with parameters _θ_ that values space as a function of of the ball, 



At a �irst glance it seems the relation between the position of the ball and the �ield location for predicting location value is complex and non-linear. While we have tested several linear models, we have observed signi�icantly improved performance with non-linear alternatives, so stick to those here. In order to solve the proposed problem, we use a feed forward neural network with one hidden layer, that aims to learn the parameters _θ_ of the mapping de�ined in Equation 3. For the learning process we build a dataset where the target value _Vi,j_ ( _t_ ) is calculated by minimizing the loss 4, which corresponds to the sum of player in�luence for every defending player _d_ in a given situation. 







2018 Research Papers Competition Presented by: 

7 





- **(a)** Pitch value for ball vertically centered at the �irst quarter of the �ield 



- **(c)** Pitch value for ball at the third quarter of the �ield on top of the left lane 



- **(b)** Pitch value for ball at the center of �ield 



- **(d)** Pitch value for ball vertically centered at the fourt quarter of the �ield 

**Figure 4:** Predicted pitch value in a [0,1] range for given ball location (white circle) 

Defensive situations are found by selecting game situations where the opponent has possession of the ball. Then, the sum of player in�luence is found for every location ( _i, j_ ) within a 21 _x_ 15 grid, for every defending player _i_ . Situations are selected so they are separated in time by at least three seconds. Here we employ TRACAB tracking-data of 20 matches of �irst and second Spanish division, consisting of 2.4 million examples. For learning the parameters we use a feed forward neural network with one hidden layer using _adam_ optimization algorihthm [8]. Speci�ically, we aim to �ind the optimal parameters _θ∗_ that minimizes the loss function _L_ as presented in Equation 5. We selected mean square error as loss function _L_ and sigmoid function as the activation function _f_ . 



We found the best model through a 10-fold cross-validation process, obtaining a 0 _._ 085 mean square error value and 0 _._ 001 standard deviation among folds. 

In order to obtain a valuation of a �ield location for a given ball location, we now query the learned model. Figure 4 shows three different ball position scenarios and the obtained �ield valuation. This model has learned that nearby locations to the ball have increasing value for a certain range, while understanding effectively how to translate this value depending on ball position. The model still lacks from the natural intuition that space generated at the higher valued locations of the �irst quarter of the �ield should not have an identical valuation than those of higher valued locations at the last quarter. In other words, the 





2018 Research Papers Competition Presented by: 

8 





- **(a)** Distance to goal pitch value normalization surface 



- **(c)** Normalized pitch value for ball at the center of �ield 



**(b)** Normalized pitch value for ball vertically centered at the �irst quarter of the �ield 



**(d)** Normalized pitch value for ball vertically centered the fourt quarter of the �ield 

**Figure 5:** Predicted pitch value in a [0,1] range for given ball location (white circle) normalized by a distance to goal model 

cumulative value of space is higher when further up the �ield, closer to the opponent’s goal. In order to adapt to this intuitive thinking we normalize the obtained pitch value by the distance to the goal of every location normalized on a [0 _,_ 1] range. Figure 5 presents the normalization surface and three different pitch value situations, where the results still adapt to ball location but show a more consistent valuation of the pitch which adjusts for the threat of the ball location, according to expert analysts. We see that when one’s own goalkeeper has the ball, the overall value of space is limited, but when in the opponent’s box, space is much more valuable alongside the looming threat of a shot on goal. 

## **5 Occupation and Generation of Spaces** 

Previously, we approached the occupation and generation of spaces as actions focused on the improvement of the quality of team positioning, with the purpose of reaching better goal scoring chances. The quality of positioning of a given player is then related with having the best possible control of the space, and doing so for spaces with higher value. We could then express the quality of owned space _Q_ as a function of the level of ownership (control) _PC_ and the value of space _V_ , as presented in Equation 6. 



Based on the de�initions of Sections 3 and 4 we can model _PCi_ ( _t_ ) through our team pitch control model, 





2018 Research Papers Competition Presented by: 

9 



and _Vi_ ( _t_ ) using the ball-relative �ield value model. Figure 6 presents the team pitch control, the pitch value and the obtained quality of owned space, in a given match situation. We can now de�ine with detail our two main proposed concepts: Space Occupation Gain and Space Generation Gain. 

### **5.1 Space Occupation Gain** 

Now that we have the necessary tools to represent the value of space ownership in a given time, we can de�ine a model for identifying gain in space occupation in time. As mentioned in section 2 we propose the Space Occupation Gain (SOG) concept as the relative amount of quality of owned space earnt during a time window. An opposite concept is that of Space Occupation Loss (SOL), which relates to a negative gain during the time window. We �irst de�ine the concept of gain in time _G_ as the mean difference of quality of space occupation _Q_ during a time window [ _t_ + 1 _, t_ + _w_ + 1], for a given player _i_ . This is expressed in Equation 7. 



Given the dynamic nature of football, players are involved in a continuous process of winning and losing space. A small gain of space can happen when the nearby defenders follow the ball when it moves away from the player, leaving the player a better control of space. However the same can happen in a high speed running situation between the attack and the defender, where the attacker is moving slightly faster. In another case, a medium or high gain of space can happen when the player moves towards a free space. Given this, it is necessary to de�ine a level of space gain from which the earned space can be considered an actual occupational advantage and not a consequence of slower-moving contextual factors in a given situation. We set a constant _ϵ_ as a threshold to account for space occupation gain only in the cases the gain is above that threshold. We can do the equivalent for space occupation loss. Both expressions are de�ined in Equations 8 and 9. 









**(a)** Pitch control surface **(b)** Pitch value based on ball position **(c)** Value of the owned space as product of pitch control and �ield value 

**Figure 6:** Pitch control, �ield value and value of owned space for attacking team in red, for attacking direction left to right 





2018 Research Papers Competition Presented by: 

10 



An additional concept for re�ining the idea of gaining space quality is the way that space is gained, speci�ically regarding player’s speed. We present two de�initions: active and passive space occupation gain. A space is occupied actively when the player moves towards that space with a greater speed than speed of jogging (>1.5m/s [9]). Otherwise we consider that space to be occupied passively. 

### **5.2 Space Generation Gain** 

The generation of space for teammates is a concept that involves two or more teammates during certain attacking situation. Two main types of actors are present: one generator and one or more receivers. The generator is a player that moves toward a certain space while dragging opponents during the process. This dragging behaviour causes the freeing up of space previously occupied by the dragged opponent. When that opponent was previously close to one or more other teammates we say those players are receving space generated by the attracting player. In order to express this concept mathematically, we need to de�ine a value for closeness. We will say that a player is close to another if the distance between them in a given time _t_ is below a constant _δ_ . Also, it is desirable to de�ine another constant _α_ for constraining the minimum attracting distance, which refers to the difference in distance between the starting and end position of the generator and the attracted opponent. This allows us to avoid innaccurate attractions when players are very close to each other initially. Given this, and let _di,j_ ( _t_ ) be the distance between players _i_ and _j_ , Equation 10 expresses the concept of space generation _SG_ between any pair of teammates ( _i, i_<sup>_′_</sup> ) and any opponent _j_ , for a time window [ _t, t_ + _w_ ]. 



Oncewecanidentifywhenaspacegenerationbehaviourisoccuring, wewouldliketofocusonthecases in which we actually have a gain in space due to the dragging effect. Analogously to the _SOG_ de�inition, we express the Space Generation Gain _SGG_ as space generation situations where the gain is above a threshold _ϵ_ , as presented in Equation 11. 



Essentially, we are attributing space gain to a player when a defender leaves his mark and moves towards a teammate, subject to the conditions that the defender was close to the player and ended close to the teammate during a time window. It is important to clarify that while _SOG_ and _SGG_ represent two frequent and relevant cases of space gain within soccer, other types of situations and movements might contribute as well to the total space created by a player during a match. An additional possible concept is that of potential space, referring to a space that the player is more likely to reach, within his positioning, but its not in its immediate in�luence area. We will now focus on analyzing _SOG_ and _SGG_ whitin a match context. 

## **6 Match Analysis** 

The ability to create and occupy spaces are two commonly trained concepts in modern soccer. During training, coaches interrupt and reshape individual drills to teach players how to orient and move toward spaces and away from low value local zones on the �ield. When analyzing off-ball performance, coaches appeal to video analysis. Although elite soccer analysis staff typically have a great capacity to understand 





2018 Research Papers Competition Presented by: 

11 



complex concepts through match visualization, the dynamics of space creation are so frequent and happen in so short-time windows, that it becomes impractical for video analysts to grasp them all, even for a single match. However, is important to note that there is no existance of ground truth data regarding the use of spaces in soccer. Hence we have performed an extensive validation of the developed concepts through video and studying individual situations within games, with the help of two expert soccer video analysts from F.C. Barcelona, in order to �ine-tune our quantitative approach. The following videos are examples of the video-based validation tool we have used: `http://www.lukebornn.com/sloan/space_occupation_ 1.mp4` , `http://www.lukebornn.com/sloan/space_occupation_2.mp4` 

Based on this, we provide a complete summary of off-ball movements statistics for a speci�ic Spanish �irst division of�icial match between F.C. Barcelona and Villareal F.C. in January 2017. Speci�ically, we provide an analysis focused on the concepts of space occupation and space generation, using TRACAB optical tracking data. This match ended with a 1-1 result, where the �irst goal was scored by Villareal F.C. at the 49th minute (second half), and the F.C. Barcelona equalizer came at the 90th minute by Lionel Messi. Situationally, this presents a game where F.C. Barcelona was in need of scoring during the �inal minutes, and required to occupy and generate the most spaces possible to reach scoring chances. In order to identify space occupation and generation actions we calculate for the attacking situations of F.C. Barcelona all the instances where a player had controlled possession of the ball with his feet. From each of those situations, and alongside expert football analysts from F.C. Barcelona, we de�ine a window _w_ of three seconds after each of these cases, reaching a total of 845 different situations. The closeness factor _δ_ is set to 5 meters, based on the minimum distance an opponent is on average to a player in possession of the ball. We also set the minimum attraction distance for space generation _α_ to 3 meters. 

Table 1 presents the space occupation statistics for F.C. Barcelona, sorted in descending order by the total amount of Space Occupation Gain (SOG). At �irst glance it can be seen that over 41% of gain of space occupation was performed by Iniesta, Sergio Busquets and Lionel Messi. Notably, these three players occupy different positions and have different roles within the team. Busquets is a pivot and has a speci�ic role of helping to drive the ball with controlled possession during build-ups, and to accompany the game creation during positional attacks. Iniesta is an attacking mid�ielder with great control of the ball, and special skills in moving and �inding spaces between lines. Messi is an attacker but not attached to a speci�ic position, and is allowed to cover wide areas of the pitch to �ind space and request the ball. The three players share, however, a long-time tradition of possession-centered and off-ball movements quality during their career. Suarez and Neymar, two highly mobile players, appear with a lower count of situations where space was gained. This can be associated with the high level of strictly closed marking these players suffered during the match. 

It is interesting to observe that for most players the active occupation of spaces is considerably more frequent than passive occupation. This is particularly noticeable on left and right backs Digne and Sergi Roberto, who need to cover wider spaces and show a high mean distance to ball for SOG, a characteristic shared by central defenders Pique and Mascherano. A remarkable case is that of Lionel Messi, whose passive SOG is considerably higher than the active one. The passive characteristic of SOG does not mean the player is not occupying the space intentionally, but rather that he is not moving at running speed, but slower. Much has been argued in recent years about several moments during matches where Messi walks through zones of the �ield. However, that walking behaviour is not a detachment from the match but a conscious action to move through empty spaces of value and claim the control of valuable space, and ultimately the ball. Messi does this very effectively, placing him near the top of players in terms of space 





2018 Research Papers Competition Presented by: 

12 



||# SOG|~~∑~~SOG|_µ_SOG|Active (%)|Passive (%)|FRT|BEH|MBD|Mins|
|---|---|---|---|---|---|---|---|---|---|
|Name||||||||||
|Iniesta|96 (14.8%)|15.77|0.16|56.25|43.75|49|47|15.19|94.86|
|S. Busquets|90 (13.9%)|14.85|0.16|47.78|52.22|44|46|16.65|94.86|
|Messi|81 (12.5 %)|14.72|0.18|33.33|66.67|58|23|17.50|94.86|
|A. Gomes|74 (11.4%)|12.58|0.17|68.92|31.08|40|34|15.93|68.61|
|Suarez|70 (10.8%)|12.27|0.18|57.14|42.86|57|13|13.46|94.86|
|Neymar|61 (9.4%)|9.46|0.16|59.02|40.98|48|13|18.31|94.86|
|S. Roberto|51 (7.8%)|7.34|0.14|78.43|21.57|25|26|25.10|94.86|
|Pique|29 (4.4%)|4.92|0.17|48.28|51.72|6|23|21.05|94.86|
|Mascherano|29 (4.4 %)|4.54|0.16|41.38|58.62|2|27|22.03|94.86|
|D. Suarez|22 (3.4%)|4.07|0.18|77.27|22.73|13|9|17.47|26.25|
|A. Turan|17 (2.6%)|3.51|0.21|52.94|47.06|12|5|12.71|23.32|
|Digne|26(3.2%)|3.48|0.13|80.77|19.23|13|13|16.23|71.54|



**Table 1:** Statistics of space occupation for F.C. Barcelona in an of�icial Spanish League match against Villareal F.C. Symbols #,<sup>∑</sup> and _µ_ represent the total, sum and mean of their associated variable. SOG refers to Space Occupation Gain, while FRT and BEH indicate the amount of times SOG occurs in front or behind the ball. MBD represents the mean ball distance, and Active (%) and Passive (%) the player percentage of times the space was occupied through active or passive occupation. 

gained during the whole match, despite the lack of active gain. A relevant characteristic of this is that 71% of the time the gain in space is done in front of the ball rather than behind. The in front and behind the ball statistics show a clear tendency for central defenders to gain space behind the ball, while attackers show a higher rate of space gain in front of the ball. Noticeably Busquests, Iniesta and the right and left backs (Digne and S. Roberto) have a balanced ratio of space gain behind and in front of the ball. 

Table 2 presents the statistics for Space Occupation Loss (SOL) and Space Generation Gain (SGG). The SOL statistics show a clear tendency of higher space loss for players that are more often in possession of the ball such as Iniesta, Messi, Neymar and Suarez. The space loss can be directly associated with pressure effect by the opponent, who tends to increase density near to attacking players to reduce their range of action, specially for highly skilled players. Regarding the generation of space, we obtain a different picture from the space occupation skills. Here, Neymar and Suarez appear to be, alongside Messi, the players that more oftenly drag opponents to create space. With a 4-3-3 system and high-quality players, a speci�ic attacking strategy is that of spreading out attacking players to drag defenders out of position and provide wider spaces for attacking action. Busquets, a pivoting specialist, appears also at the top of the table showing his value in supporting space creation. Notably the left and right back, Digne and S. Roberto do not generate much space. Given that they move towards the border lines of the �ield, it is less likely that opponents are dragged by back defenders. 

A more detailed perspective of space generators and receivers is presented in Figure 7. Here we can observe the amount of times generators are producing space for receivers, and discover some collaborative playing behaviour. First to observe is that Busquets receives space from most of the players at least once, possibly showing his ability to stay at the center of play. A renowned skill of F.C. Barcelona team playing is the third-man pass, which consists of the following: if a player A wants to pass to player C, but is marked, he passes to player B, dragging the opponents toward him, enabling C to receive the ball in more space. This 





2018 Research Papers Competition Presented by: 

13 



||# Generated|# Received|~~∑~~SGG|_µ_SGG|# SOL|~~∑~~SOL|_µ_SOL|Mins|
|---|---|---|---|---|---|---|---|---|
|Name|||||||||
|Neymar|28 (18.9%)|6 (4.1%)|5.97|0.21|51|-8.53|-0.17|94.86|
|Suarez|25 (16.9%)|18 (12.3%)|5.60|0.22|52|-9.12|-0.18|94.86|
|Messi|22 (14.9%)|24 (16.4%)|4.32|0.20|68|-11.61|-0.17|94.86|
|S. Busquets|15 (10.1%)|24 (16.4%)|3.83|0.26|38|-6.16|-0.16|94.86|
|Pique|14 (9.5%)|9 (6.2%)|3.66|0.26|19|-2.77|-0.15|94.86|
|Iniesta|13 (8.9%)|21 (14.4%)|2.62|0.20|75|-11.79|-0.16|94.86|
|A. Turan|8 (5.4%)|7 (4.8%)|2.26|0.28|8|-1.29|-0.16|23.32|
|S. Roberto|7 (4.7%)|2 (1.4%)|1.55|0.22|31|-4.62|-0.15|94.86|
|A. Gomes|9 (6%)|18 (1.2%)|1.49|0.17|44|-6.25|-0.14|68.61|
|Mascherano|5 (3.4%)|9 (6.2%)|0.80|0.16|23|-3.39|-0.15|94.86|
|D. Suarez|2(1.4%)|8(5.5%)|0.46|0.23|16|-3.14|-0.20|26.25|



**Table 2:** Statistics of space generation, and space occupation loss for F.C. Barcelona in an of�icial Spanish League Match against Villareal F.C. Symbols #,<sup>∑</sup> and _µ_ represent the total, sum and mean of their associated variable. # Generated and # Received indicate the total times a player generated or received generated space, accompained by the team-relative percentage. SGG refers to Space Generation Gain and SOL refers to Space Occupation Loss. 

plot might show a third-man behaviour through Busquets. Notably, Suarez, Neymar and Messi, generate space commongly for each other, especially Suarez who provides considerable space to both. A special connection Suarez-Messi is also shown for this game, where both were able to generate high amount of spaces for each other. 

A further vision of space gain and generation can be grasped from Figure 9. Here we present the spatial heatmap forSOGand SGG situations. In a �irstglanceis clear toobservethe amount of space gainedthrough occupation is considerably higher than through generation, a more complex process. Iniesta presents an interesting case where he can generate more space next to the left border line of the �ield, while he is better at gaining spaces for himself at the interior of the �ield. Also, he produces a notable amount of space near the box. Busquets shows an incredible collaborative behaviour by generating space almost anywhere around the �ield. He also presents wide areas of SOG, but more intensively near the mid�ield, his natural habitat. Suarez presents a notable ability to generate space within the box, where he concentrates most of his generating contribution. Here he arises as a specialist in dragging defenders either while making spaces for himself or while generating spaces to others. Messi also shows a great ability in generating spaces around the attacking zones of the �ield, while Neymar concentrated on the left wing, focused on high speed diagonal runs towards the box. Defenders, as expected show very little generation of space. 

## **7 Discussion** 

In a sport where the average possession of the ball by a player is 3 minutes in a 90 minute game, the analysis of team-collective dynamics through off-ball movements becomes a critical element for understanding performance. We have shown how through spatio-temporal data it is possible to extract meaningful information relating the occupation of spaces of value and the generation of spaces for teammates. Beyond the bigger picture that overall performance statistics of multiple matches can provide, the understanding of off-ball movements demands the need for a more specialized per-match or even per-situation analysis. Through the understanding of the frequencies, quality, position and effectiveness of space occupation and 





2018 Research Papers Competition Presented by: 

14 





**Figure 7:** A heatmap showing the total times space was genreated by generators (y-axis) for receivers (x-axis) 

generation, a coach can provide speci�ic guidance to players to help the team playing dynamics beyond what he can do with the ball. 

In order to provide a deeper understanding of space, we have presented two novel approaches for pitch control and pitch value modelling. Our pitch control model takes into account critical factors when understanding the dominance of space such as the velocity and position of the player. It also provides a key element that was missing in previous dominance region models: the idea of a soft surface of control where for a given location on the �ield, nearby players have a certain level of in�luence, instead of de�ining strict dominance margins such as in Voronoi-based models. On the other hand, the proposed pitch value model presents a way of quantifying the value of every location on the �ield in a dynamic way, relative to the location of the ball. This way, we can account for both the control of space a team has and the value of that space, to obtain a measure of spatial value controlled. 

For future studies, the proposed pitch control and �ield models can be directly applied for reaching more comprehensive pass probability and reward models, and in general to incorporate a new perspective on dominant-regions based approaches for understanding team sports. But more generally, this study sets a base for new research on off-ball behaviour in soccer. New perspectives are still to be studied, such as the effect of different pressure strategies, the concept of potential space and how it could be exploited, the overall dynamic balance of space control between the two teams and its association to performance, as well as many other research lines that address a critical question when training to succeed in soccer: what should I do when my teammate is in possession of the ball?. 





2018 Research Papers Competition Presented by: 

15 





**Figure 8:** Space Occupation Gain and Space Generation heatmap for every �ield player playing over 60 minutes. The scaling factor is based on the maximum Space Occupation and maximum Space Generation among all the team, respectively. 

## **References** 

- [1] Pedro Silva, Paulo Aguiar, Ricardo Duarte, Keith Davids, Duarte Araújo, and Júlio Garganta. Effects of pitch size and skill level on tactical behaviours of association football players during small-sided and conditioned games. _International Journal of Sports Science & Coaching_ , 9(5):993–1006, 2014. 

- [2] Robert Rein, Dominik Raabe, Jürgen Perl, and Daniel Memmert. Evaluation of changes in space control due to passing behavior in elite soccer using voronoi-cells. In _Proceedings of the 10th International Symposium on Computer Science in Sports (ISCSS)_ , pages 179–183. Springer, 2016. 





2018 Research Papers Competition Presented by: 

16 



- [3] Michael Horton, Joachim Gudmundsson, Sanjay Chawla, and Joël Estephan. Classi�ication of passes in football matches using spatiotemporal data. _arXiv preprint arXiv:1407.5093_ , 2014. 

- [4] R Masheswaran, Y Chang, Jeff Su, Sheldon Kwok, Tal Levy, Adam Wexler, and Noel Hollingsworth. The three dimensions of rebounding. _MIT SSAC_ , 2014. 

- [5] Tsuyoshi Taki, Jun-ichi Hasegawa, and Teruo Fukumura. Development of motion analysis system for quantitative evaluation of teamwork in soccer games. In _Image Processing, 1996. Proceedings., International Conference on_ , volume 3, pages 815–818. IEEE, 1996. 

- [6] Dan Cervone, Luke Bornn, and Kirk Goldsberry. Nba court realty. MIT Sloan Sports Analytics Conference, Boston, MA, USA, 2016. 

- [7] Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Counterpoints: Advanced defensive metrics for nba basketball. In _9th Annual MIT Sloan Sports Analytics Conference, Boston, MA_ , 2015. 

- [8] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

- [9] Angel Ric, Carlota Torrents, Bruno Gonçalves, Lorena Torres-Ronda, Jaime Sampaio, and Robert Hristovski. Dynamics of tactical behaviour in association football when manipulating players’ space of interaction. _PloS one_ , 12(7):e0180773, 2017. 

- [10] A geometric interpretation of the covariance matrix. `http://www.visiondummy.com/2014/04/ geometric-interpretation-covariance-matrix` . Accessed: 2017-11-10. 





2018 Research Papers Competition Presented by: 

17 



## **A Appendix** 

### **A.1 Player In�luence Area Details** 

Section 3.1 presents a player in�luence model that accounts for the position, velocity and distance to ball of a given player. The in�luence degree _Ii_ at Equation 13 is expressed in terms of the probability density function of a bivariate gaussian distribution de�ined by Equation 12. In this section we detail the calculation of each of the elements involved in the equation. 





The covariance matrix can be dynamically adjusted to provide a player dominance distribution that accounts for location and velocity. Using the singular value decomposition algorithm we can express the covariance matrix as a function of its eigenvectors and eigenvalues as expressed in Equation 14, where _V_ is the matrix whose columns are the eigenvectors of Σ, and _L_ is the diagonal matrix whose non-zero elements are the corresponding eigenvalues [10]. Let _R_ = _V_ and _S_ = _√L_ , we can de�ine _R_ as a rotation matrix and _S_ as a scaling matrix, allowing to express the covariance as in Equation 15. Based on this, the rotation matrix and scaling matrix can be de�ined as Equations 16 and 17, where _θ_ is the rotation angle of the speed vector and, _sx_ and _sy_ are the scaling factors in the x and y direction. 









In order to �ind the scaling factors, we take into account both the player’s magnitude of speed _Si_ ( _t_ ) (as meters per second), and the distance to the ball _Di_ ( _t_ ). Based on the opinion of expert soccer analysts we have de�ined the range [4 _,_ 10] as the minimum and maximum distance in meters of player’s pitch control surface radius _Ri_ ( _t_ ), based on the distance to the ball, following the transformation function shown at Figure 9. Setting 13 _m_ / _s_ as the maximum possible speed reachable, we calculate the ratio between player’s and the maximum speed, as shown in Equation 18. Then, the scaling matrix is expanded in x direction and contracted in y direction by this factor, as expressed in Equation 19. Given this, we can express a function _COV_ for obtaining the covariance matrix as shown in Equation 21. Finally, the distribution mean value _µi_ ( _t_ ) is found by translating the players location at time _t_ by half the magnitude of speed vector _⃗s_ , following Equation 21. 









2018 Research Papers Competition Presented by: 









**Figure 9:** Player in�luence radius relation with distance to the ball 





2018 Research Papers Competition Presented by: 

19 


