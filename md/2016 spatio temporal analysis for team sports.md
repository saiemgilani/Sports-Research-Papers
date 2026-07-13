<!-- source: 2016 spatio temporal analysis for team sports.pdf -->

# **– Spatio-Temporal Analysis of Team Sports A Survey** 

Joachim Gudmundsson<sup>_⋆_</sup> and Michael Horton 

The University of Sydney, Australia 

**Abstract.** Team-based _invasion sports_ such as football, basketball and hockey are similar in the sense that the players are able to move freely around the playing area; and that player and team performance cannot be fully analysed without considering the movements and interactions of all players as a group. State of the art object tracking systems now produce _spatio-temporal_ traces of player trajectories with high definition and high frequency, and this, in turn, has facilitated a variety of research efforts, across many disciplines, to extract insight from the trajectories. We survey recent research efforts that use spatio-temporal data from team sports as input, and involve non-trivial computation. This article categorises the research efforts in a coherent framework and identifies a number of open research questions. 

## **1 Introduction** 

Team sports are a significant recreational activity in many societies, and attract participants to compete in, watch, and also to capitalise from the sport. There are several sporting codes that can be classed together as _invasion sports_ in that they share a common structure: two teams are competing for possession of a ball (or puck) in a constrained playing area, for a given period of time, and each team has simultaneous objectives of scoring by putting the ball into the opposition’s goal, and also defending their goal against attacks by the opposition. The team that has scored the greatest number of goals at the end of the allotted time is the winner. Football (soccer), basketball, ice hockey, field hockey, rugby, Australian Rules football, American football, handball, and Lacrosse are all examples of invasion sports. 

Teams looking to improve their chances of winning will naturally seek to understand their performance, and also that of their opposition. Systematic analysis of sports play has been occurring since the 1950s using manual notation methods [70]. However human observation can be unreliable – experimental results in Franks and Miller [32] showed that the expert observers’ recollection of significant match events is as low as 42 % – and in recent years, automated systems to capture and analyse sports play have proliferated. 

> _⋆_ Joachim Gudmundsson was supported under the Australian Research Council’s _Discovery Projects_ funding scheme (DP150101134). 

Today, there are a number of systems in use that capture spatio-temporal data from team sports during matches. The adoption of this technology and the availability to researchers of the resulting data varies amongst the different sporting codes and is driven by various factors, particularly commercial and technical. There is a cost associated with installing and maintaining such systems, and while some leagues mandate that all stadium have systems fitted, in others the individual teams will bear the cost, and thus view the data as commercially sensitive. Furthermore, the nature of some sports present technical challenges to automated systems, for example, sports such as rugby and American football have frequent collisions that can confound optical systems that rely on edge-detection. 

To date, the majority of datasets available for research are sourced from football and basketball, and the research we surveyed reflects this, see Fig. 1. The National Hockey League intends to install a player tracking system for the 2015/6 season, and this may precipitate research in ice hockey in coming years [76]. 



<!-- Start of picture text -->
20<br>18<br>16<br>14 Sporting Code<br>basketball<br>12<br>10 football<br>8 american football<br>6 other<br>4<br>2<br>0<br>1995 2000 2005 2010 2015<br>Year<br>Number of Papers<br><!-- End of picture text -->

**Fig. 1:** _Spatial sports research papers cited in this survey, by year,_ 1995 _-_ 2015 _(to date), divided by sporting code. There has been a significant increase in papers published in this area as data has become available for researchers, particularly in football and basketball._ 

Sports performance is actively researched in a variety of disciplines. To be explicit, the research that we consider in this survey fulfils three key criteria: 

1. We consider **team-based invasion sports** . 

2 

2. The model used in the research has **spatio-temporal data** as its primary input. 

3. The model performs some **non-trivial computation** on the spatio-temporal data. 

The research covered has come from many research communities, including machine learning, network science, GIS, computational geometry, computer vision, complex systems science, statistics and sports science. There has been a consequent diversity of methods and models used in the research, and our intention in writing this survey was to provide an overview and framework on the research to date. 

Furthermore, the spatio-temporal data extracted from sports has several useful properties that make it convenient for fundamental research. For instance, player trajectories exhibit small spatial and temporal range, dense sampling rates, a small number of agents (i.e. players), highly cooperative and adversarial interaction between agents, and a latent structure. As such, we believe that this survey is a timely contribution to this emerging area of research. 

This survey contains the following sections. In Section 2 we describe the primary types of spatio-temporal data captured from team sports. We describe the properties of these data and outline the sports from which it is currently available. 

Section 3 describes approaches that have been used to subdivide the playing area into regions that have a particular property. The playing area may be discretized into a fixed subdivision and the occurrences of some phenomena counted, for instance a player occupying a particular region or a shot at goal occurring from that region, producing an _intensity map_ of the playing area. On the other hand, a subdivision of the playing area based on areas that are dominated by particular players has also been used in several papers. 

In Section 4, we survey approaches that represent temporal sequences of events as _networks_ and apply network-theoretic measure to them. For example, sequences of passes between players can be represented as a network with players as the vertices and weighted edges for the frequency of passes between pairs of players, and network measures be computed to quantify the passing performance. 

Section 5 provides a task-oriented survey of the approaches to uncover information inherent in the spatio-temporal data using _data mining_ techniques. Furthermore, several papers define metrics to measure the performance of players and teams, and these are discussed in Section 6. 

Finally, in Section 7, we detail the research into _visualisation_ techniques to succinctly present metrics of sports performance. 

## **2 Representing Sports Play using Spatio-Temporal Data** 

The research surveyed in this paper is based on _spatio-temporal data_ , the defining characteristic of which is that it is a sequence of samples containing the timestamp and location of some phenomena. In the team sports domain, two types 

3 

of spatio-temporal data are commonly captured: _object trajectories_ that capture the movement of players or the ball; and _event logs_ that record the location and time of match events, such as passes, shots at goal or fouls. These datasets, described in detail below, individually facilitate the spatiotemporal analysis of play, however they are complementary in that they describe different aspects of play, and can provide a richer explanation of the game when used in combination. For example, the spatial formation in which a team arranges itself in will be apparent in the set of player trajectories. However, the particular formation used may depend on whether the team is in possession of the ball, which can be determined from the event log. On the other hand, a _shot at goal_ event contains the location from where the shot was made, but this may not be sufficient to make a qualitative rating of the shot. Such a rating ought to consider whether the shooter was closely marked by the defence, and the proximity of defenders – properties that can be interpolated from the player trajectories. 

### **2.1 Object Trajectories** 

The movement of players or the ball around the playing area are sampled as a timestamped sequence of location points in the plane, see Fig. 2. The trajectories are captured using optical- or device-tracking and processing systems. _Optical tracking systems_ use fixed cameras to capture the player movement, and the images are then processed to compute the trajectories [12]. There are several commercial vendors who supply tracking services to professional sports teams and leagues [19, 44, 69, 77]. On the other hand, _device tracking systems_ rely on devices that infer their location, and are attached to the players’ clothing or embedded in the ball or puck. These systems can be based on GPS [16] or RFID [76] technology. 

The trajectories produced by these systems are dense, in the sense that the location points samples are uniform and frequent – in the range of 10 to 30 Hz. 

The availability of spatio-temporal data for research varies. Some leagues capture data from all matches, such as the NBA [61] and the German Football Leagues [44], in other cases, teams capture data at their stadia only. League-wide datasets are not simply larger, but also allow for experiments that control for external factors such as weather, injuries to players, and playing at home and on the road. 

### **2.2 Event Logs** 

Event logs are a sequence of significant events that occur during a match. Events can be broadly categorised as _player events_ such as passes and shots; and _technical events_ , for example fouls, time-outs, and start/end of period, see Fig. 2. Event logs may be derived in part from the trajectories of the players involved, however they may also be captured directly from video analysis, for example Opta Sports Ltd [63] uses this approach. This is often the case in sports where there are practical difficulties in capturing player trajectories, such as rugby and American football. 

4 



<!-- Start of picture text -->
p si x 1 x 2 Trajectory: tpj<br>. . .<br>pj 10.1 3940 -2362<br>pj 10.2 3948 -2346 Speed: ϵ ( tpj , si )<br>pj 10.3 3956 -2331<br>pj 10.4 3923 -2392<br>pj 10.5 3977 -2309 Direction: γ ( tpj , si )<br>. . .<br>pj<br>Location: ξ ( tpj , si )<br>si v P Distance<br>10.1. . . Touch {pj } Duration<br>10.2 Pass {pj }<br>10.6 Touch {pk }<br>11.0 Tackle {pl , pk }<br>. . . Event: ek pj<br>pk<br>Direction<br><!-- End of picture text -->

**Fig. 2:** _Example of the trajectory and event input data and an illustration of their geometric representations. Each trajectory is a sequence of location points, and these can be used to extrapolate the basic geometry of a player at a given time-step. Similarly, the geometry of events such as the_ pass _shown, can be computed from the trajectories of the involved players._ 

Event logs are qualitatively different from the player trajectories in that they are not dense – samples are only captured when an event occurs – however they can be semantically richer as they include details like the type of event and the players involved. 

The models and techniques described in the following sections all use object trajectories and/or event logs as their primary input. 

## **3 Playing Area Subdivision** 

Player trajectories and event logs are both low-level representations, and can be challenging to work with. One way to deal with this issue is to discretize the playing area into regions and assign the location points contained in the trajectory or event log to a discretized region. The frequency – or intensity – of events occurring in each region is a spatial summary of the underlying process, alternatively, the playing area may be subdivided into regions such that each region is dominated in some sense by a single player, for example by the player being able to reach all points in the region before any other player. There are a variety of techniques for producing playing area subdivisions that have been used in the research surveyed here, and are summarised in this section. 

5 

### **3.1 Intensity Matrices and Maps** 

Spatial data from team sports have the useful property that they are constrained to a relatively small and symmetric playing area – the pitch, field or court. The playing area may be subdivided into regions and events occurring in each region can be counted to produce an intensity matrix, and can be visualised with an intensity map, see Fig. 3. This is a common preprocessing step for many of the techniques described in subsequent sections. 





<!-- Start of picture text -->
(a) Left-back (b) Striker<br><!-- End of picture text -->

**Fig. 3:** _Example intensity maps showing areas of the football pitch that the player’s occupy. The player trajectories have been oriented such that the play is from left to right. (a) The left-back is positioned on the left of the field, but is responsible for taking attacking corner-kicks from the right. (b) The striker predominantly stays forward of the half-way line, however will retreat to help defend corner-kicks._ 

When designing a spatial discretization, the number and shape of the induced regions can vary. A common approach is to subdivide the playing area into rectangles of equal size [5, 9, 17, 31, 52, 60, 74], for example see Fig. 4c. However, the behaviour of players may not vary smoothly in some areas. For example: around the three-point line on the basketball court, a player’s propensity to shoot varies abruptly; or the willingness of a football defender to attempt a tackle will change depending on whether they are inside the penalty box. The playing area may be subdivided to respect such predefined assumptions of the player’s behaviour. Camerino et al. [15] subdivides the football pitch into areas that are aligned with the penalty box, see Fig. 4a, and interactions occurring in each region where counted. Similarly, Maheswaran et al. [57] and Goldsberry and Weiss [38] define subdivisions of the basketball half-court that conforms with the three-point line and is informed by intuition of shooting behaviour, see Fig. 4b. 

Transforming the playing area into polar space and inducing the subdivision in that space is an approach used in several papers. This approach reflects the fact that player behaviour may be similar for locations that are equidistant from the goal or basket. Using the basket as the origin, polar-space subdivisions were 

6 

used by Reich et al. [71] and by Maheswaran et al. [56]. Yue et al. [89] used a polar-space subdivision to discretize the position of the players marking an attacking player. Under this scheme, the location of the attacking player was used as the origin, and the polar space aligned such that the direction of the basket is at 0<sup>_◦_</sup> , see Fig. 4d. 



<!-- Start of picture text -->
(a) Hand-designed<br>(b) Hand-designed (c) Cartesian grid (d) Polar grid<br><!-- End of picture text -->

**Fig. 4:** _Examples of subdivisions used to discretize locations: (a), (b) hand-designed subdivision reflecting expert knowledge of game-play in basketball [57] and football [15]; (c) subdivision of court into unit-squares [17]; (d) polar subdivision where origin is centred on ball-carrier and grid is aligned with the basket [89]._ 

Given a subdivision of the playing area, counting the number of events by each player in each region induces a discrete spatial distribution of players’ locations during the match. This can be represented as an R<sup>_N_</sup> +<sup>_×K_</sup> intensity matrix containing the counts _X_ for _N_ players in each of the _R_ regions of the subdivision. The event _X_ may be the number of visits by a player to the region, e.g. Maheswaran et al. [57] used the location points from player trajectories to determine whether a cell was visited. Bialkowski et al. [4] used event data such as passes and touches made by football players to determine the regions a player had visited. 

7 

The number of passes or shots at goal that occur in each region may also be counted. For example, many papers counted shots made in each region of a subdivision of a basketball court [31, 38, 56, 71, 74]. Similarly, Borrie et al. [9], Camerino et al. [15], Narizuka et al. [60], and Cervone et al. [17] counted the number of passes made in each region of a subdivision of the playing area. 

### **3.2 Low-rank Factor Matrices** 

Matrix factorization can be applied to intensity matrices described in Section 3.1, to produce a compact, low-rank representation. This approach has been used in several papers to model shooting behaviour in basketball [17, 31, 89]. The insight that motivates this technique is that similar types of players tend to shoot from similar locations, and so each player’s shooting style can be modelled as a combination of a few distinct _types_ , where each _type_ maps to a coherent area of the court that the players are likely to shoot from. 

The input is an intensity matrix _X ∈_ R<sup>_N×V_</sup> . Two new matrices _W ∈_ R<sup>_N_</sup> +<sup>_×K_</sup> and _B ∈_ R<sup>_K_</sup> +<sup>_×V_</sup> are computed such that _WB ≈ X_ and _K ≪ N, V_ . The _K_ spatial bases in _B_ represent areas of similar shooting intensity, and the _N_ players’ shooting habits are modelled as a linear combination of the spatial bases. The factorization is computed from _X_ by minimizing some distance measure between _X_ and _WB_ , under the constraint that _W_ and _B_ are non-negative. The non-negativity constraint, along with the choice of distance function encourages sparsity in the learned matrices. This leads to intuitive results: each spatial basis corresponds to a small number of regions of the halfcourt; and the shooting style of each player is modelled as the mixture of a small number of bases, see Fig. 5 for examples of learned spatial bases. 





<!-- Start of picture text -->
(a) Corner three-point (b) Top-of-key three-point (c) Right low-post<br><!-- End of picture text -->

**Fig. 5:** _Examples of spatial bases induced by using non-negative matrix factorization. Each basis represents an intensity map of where a subset of players tend to shoot from. Shown are three spatial basis intensity maps that represent defined shooting locations._ 

8 

Miller et al. [58] used non-negative matrix factorization to represent shooting locations in basketball. They observe that the shooting intensity should vary smoothly over the court space, and thus fit a Log-Gaussian Cox Process to infer a smooth intensity surface over the intensity matrix, which is then factorized. 

Yue et al. [89] used non-negative matrix factorization to model several event types: shooting; passing and receiving. They include a spatial regularization term in the distance function used when computing the matrix factorization, and claim that spatial regularization can be seen as a frequentist analog of the Bayesian Log-Gaussian Cox process used by Miller et al. [58]. 

Cervone et al. [17] also used non-negative matrix factorization to find a basis representing player roles, based on their occupancy in areas of the court. Players who are similar to a given player were identified as those who are closest in this basis, and this was used to compute a similarity matrix between players. 

### **3.3 Movement Models and Dominant Regions** 

A team’s ability to control space is considered a key factor in the team’s performance, and was one of the first research areas in which computational tools were developed. Intuitively a player dominates an area if he can reach every point in that area before anyone else (see Definition 1). An early algorithmic attempt to develop a computational tool for this type of analysis was presented by Taki et al. [79], which defined the _Minimum Moving Time Pattern_ – subsequently renamed the _Motion Model_ – and the _Dominant Region_ . 

**Motion Model** The motion model presented by Taki et al. [79] is simple and intuitive: it is a linear interpolation of the acceleration model. It assumes that potential acceleration is the same in all directions when the player is standing still or moving very slowly. As speed increases it becomes more difficult to accelerate in the direction of the movement. However, their model did not account for deceleration and hence is only accurate over short distances. 

Fujimura and Sugihara [36] presented a more realistic motion model, in particular they incorporated a resistive force that decrease the acceleration. The maximum speed of a player is bounded, and based on this assumption, Fujimura and Sugihara [36] formulated the following equation of motion: 



where _m_ is the mass, _F_ is the maximum driving force, _k_ is the resistive coefficient, and _v_ is the velocity. The solution of the equation is: 



where _v_ 0 is the velocity at time _t_ = 0. If the maximum speed _v_ max = _F/k_ and the magnitude of the resistance _α_ = _k/m_ are known, then the motion model is fixed. To obtain _α_ and _v_ max, Fujimura and Sugihara [36] studied players’ movement 

9 

on video and empirically estimated _α_ to be 1 _._ 3 and _v_ max as 7 _._ 8m/s. This is then generalised to two dimensions as follows: 



Solving the equation we get that all the points reachable by a player, starting at position _x_ 0 with velocity **v0** , can reach point _x_ within time _t_ form the circular region centred at 



They compared this model empirically and observed that the model yields a good approximation of actual human movement, but they stated that a detailed analysis is a topic for future research. 

A different model was used in a recent paper by Cervone et al. [17] with the aim to predict player movement in basketball. They present what they call a micro-transition model. The micro-transition model describes the player movement during a single possession of the ball. Separate models are then used for defense and attack. Let the location of an attacking player _ℓ_ at time _t_ be ( _x_<sup>_ℓ_</sup> ( _t_ ) _, y_<sup>_ℓ_</sup> ( _t_ )). Next they model the movement in the _x_ and _y_ coordinates at time ( _t_ + _ε_ ) using 



and analogously for _y_<sup>_ℓ_</sup> ( _t_ + _ε_ ). This expression derives from a Taylor series expansion of the function for determining the ball-carrier’s position such that _αx_<sup>_ℓ_[</sup><sup>_xℓ_(</sup><sup>_t_)</sup><sup>_−xℓ_(</sup><sup>_t −ε_)]</sup><sup>_≈εxℓ_(</sup><sup>_t_),and</sup><sup>_η_</sup> _x_<sup>_ℓ_(</sup><sup>_t_)representsthecontributionofhigher</sup> order derivatives modelling accelerations and jerks. When a player receives the ball outside the three-point line, the most common movement is to accelerate towards the basket. On the other hand, a player will decelerate when closer to the basket. Players will also accelerate away from the boundary of the court as they approach it. To capture this behaviour the authors suggest mapping a player’s location to the additive term _ηx_<sup>_ℓ_(</sup><sup>_t_)in(2).Thepositionofthefivedefenders</sup> are easier to model, conditioned on the evolution of the attack’s positions, see Cervone et al. [17] for details. 

Next we consider how the motion models have been used to develop other tools. 

**Dominant Regions** The original paper by Taki et al. [79] defined the dominant region as: 

**Definition 1.** _The_ dominant region _of a player p is the region of the playing area where p can arrive before any other player._ 

Consequently the subdivision induced by the dominant regions for all players will partition the playing area into cells. In a very simple model where acceleration 

10 

is not considered, the dominant region is equivalent to the Voronoi region and the subdivision can be efficiently computed [30]. However, for more elaborate motion models, such as the ones described in Section 3.3, the distance function is more complex. For some motion models the dominant region may not be a connected area [78], an example is shown in Fig. 6a. A standard approach used to compute the subdivision for a complex distance function is to compute the intersection of surfaces in three dimensions, as shown in Fig. 6b. However, this is a complex task and time-consuming for non-trivial motion models. Instead approximation algorithms have been considered in the literature. 







<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

**Fig. 6:** _(a) Showing the dominant region for two players. The left player is moving to the right with high speed and the right player is standing still. Using the motion models discussed in Section 3.3 the resulting dominant region for a single player might not be connected. (b) A standard approach used in computational geometry to subdivide the plane is to compute the projection of the intersection of surfaces in three dimensions onto the plane._ 

Taki and Hasegawa implemented algorithms to compute dominant regions, albeit using a simple motion model. Instead of computing the exact subdivision they considered the 640 _×_ 480 pixels that at that time formed a computer screen and for each pixel they computed the player that could reach that pixel first, hence, visualizing the dominant regions. The same algorithm for computing the dominant region was used by Fujimura and Sugihara [36], although they used a more realistic motion model, see Section 3.3. 

However, the above algorithms were shown to be slow in practice, for example preliminary experiments by Nakanishi et al. [59] stated that the computation requires 10 s to 40 s for a 610 _×_ 420 grid. To achieve the real-time computation required for application in the RoboCup robot football tournament [47], the authors proposed an alternative approach. Instead of computing the time required for every player to get to every point, Nakanishi et al. [59] used a so-called _reachable polygonal region_ (RPR). The RPR of a player _p_ given time _t_ is the region that _p_ can reach within time _t_ . An advantage with using the RPR for computing dominant regions is that more complex motion models can be used by simply drawing the RPR for different values of _t_ . They presented the following high-level algorithm. Given a sequence of time-steps _ti_ , 1 _≤ i ≤ k_ compute the RPRs for each player and each time-step. The algorithm then iterates through 

11 

the sequence of time-steps and for each pair of players, the _partial dominant regions_ are constructed from the RPRs. The partial dominant regions are then combined with the dominant regions computed in the previous time-step to form new dominant regions. Assuming that the RPR is a convex area for any _p_ and any _t_ , Nakanishi _et al._ claim a factor of 1000 improvement in computation time at the cost of roughly a 10% drop in accuracy. 

Gudmundsson and Wolle [41] used RPRs induced from real trajectory data. They also presented an algorithm for constructing an approximate dominant region subdivision, which is superficially similar to the algorithm by [59]. However, instead of computing partial dominant regions for each pair of players at each time-step, an approximate bisector is constructed for every pair of players. An example of an approximate bisector between two players is shown in Fig. 7a, and in Fig. 7b the final subdivision generated by the algorithm in Gudmundsson and Wolle [41] is depicted. 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

**Fig. 7:** _(a) An approximate bisector between two players using the intersection points of the RPRs. (b) An example of the approximate dominant region subdivision by Gudmundsson and Wolle [41]._ 

A closer study of a player’s dominant region was performed by Fonseca et al. [29] in an attempt to describe the spatial interaction between players. They considered two variables denoting the smallest distance between two teammates and the size of the dominant region. They observed that the individual dominant regions seem to be larger for the attacking team. They also found that for the defending team the two measures were more irregular which indicates that their movement was more unpredictable that the movement of the attacking team. 

According to the authors, the player and team dominant regions detect certain match events such as “when the ball is received by an attacker inside the defensive structure, revealing behavioural patterns that may be used to explain the performance outcome.” 

12 

Ueda et al. [80] compared the team-area and the dominant region (within the team-area) during offensive and defensive phases. The _team area_ is defined as the smallest enclosing orthogonal box containing all the field players of the defending team. The results seem to show that there exists a correlation between the ratio of the dominant region to team area, and the performance of the team’s offence and defence. Dominant regions of successful attacks were thinner than those for unsuccessful attacks that broke down with a turnover event located near the centre of the playing area. The conclusion was that the dominant region is closely connected to the offensive performance, hence, perhaps it is possible to evaluate the performance of a group of players using the dominant region. 

**Open 1** _The function modelling player motion used in dominant region computations has often been simple for reasons of tractability or convenience. Factors such as the physiological constraints of the players and_ a priori _momentum have been ignored. A motion function that faithfully models player movement and is tractable for computation is an open problem._ 

**Further Applications** The dominant region is a fundamental structure that has been shown to support several other interesting measures, and are discussed next. 

1. **(Weighted) Area of team dominant region.** Taki et al. [79] defined a _team dominant region_ as the union of dominant regions of all the players in the team. Variations in the size of the team dominant region was initially regarded by [79] as a strong indication on the performance of the team. However, Fujimura and Sugihara [36] argued that the size of a dominant region does not capture the contribution of a player. Instead they proposed using a _weighted_ dominant region, by either weighting with respect to the distance to the goal, or with respect to the distance to the ball. They argued that both these approaches better model the contribution of a player compared to simply using the size of the dominant region. However, no further analysis was performed. 

   - Fujimura and Sugihara [36] also suggested that the weighted area of dominant regions can be used to evaluate attacking teamwork: tracking the weighted dominant region (“defensive power”) over time for the defender marking each attacker will indicate the attacker’s contribution to the team. 

2. **Passing evaluation.** A player’s _passable area_ is the region of the playing area where the player can potentially receive a pass. The size and the shape of the passable area depends on the motion model, and the positions of the ball and the other players. Clearly this is also closely related to the notion of dominant region. 

**Definition 2.** _[41] A player p is open for a pass if there is some direction and (reasonable) speed that the ball can be passed, such that p can intercept the ball before all other players._ 

13 

Taki and Hasegawa [78] further classified a pass as “successful” if the first player that can receive the pass is a player from the same team. This model was extended and implemented by Fujimura and Sugihara [36], as follows. They empirically developed a motion model for the ball, following formula (1) in Section 3.3. They then defined the _receivable pass variation_ (RPV) for each player to be the number of passes the player can receive among a set of sampled passes. They experimentally sampled 54 000 passes by discretizing [0 _,_ 2 _π_ ) into 360 unit directions and speeds between 1 and 150 km h<sup>_−_1</sup> into 150 units. 

Gudmundsson and Wolle [41] also used a discretization approach, but viewed the problem slightly differently. Given the positions, speeds and direction of motion of the players, they approximated who is open for a pass for each discretized ball speed. For each fixed passing speed they built RPRs for each player and the ball over a set of discrete time-steps. Then an approximate bisector is computed between the ball and the player. Combining the approximate bisectors for all the players, a piecewise linear function _f_ is generated over the domain [0 _,_ 2 _π_ ). The segments of the bisectors that lie on the lower envelope of _f_ map to intervals on the domain where the player associated with the bisector is open for a pass. An example of the output is shown in Fig. 8 for a fixed ball speed. 



**Fig. 8:** _Available receivers of a pass by player Red_ 2 _where velocity of the ball is_ 20 m s<sup>_−_1</sup> _. Each sector represents an interval on_ [0 _,_ 2 _π_ ) _that indicates which player may receive the pass. Players may receive a pass made at more than one interval, for example Blue_ 7 _._ 

**Open 2** _The existing tools for determining whether a player is open to receive a pass only consider passes made along the shortest path between passer_ 

14 

_and receiver and where the ball is moving at constant velocity. The development of more realistic model that allows for aerial passes, effects of ball-spin, and variable velocities is an interesting research question._ 

3. **Spatial Pressure.** An important tactical measure is the amount of spatial pressure the team exerts on the opposition. Typically when a team believes that the opponent is weak at retaining possession of the ball, then a high pressure tactic is used. Taki et al. [79] defined spatial pressure for a player _p_ as: 



where, for a fixed radius _r_ , _P_ denotes the fraction of the disk of radius _r_ with center at _p_ that lies within the dominant region of opposing players, _d_ is the distance between _p_ and the ball, _D_ is the maximal distance between _p_ and any point on the playing area, and _m_ is a preset weight. This definition was also used by Horton et al. [43]. See Fig. 9 for two examples of spatial pressure. 

**Open 3** _The definition of spatial pressure in Taki et al. [79] is simple and does not model effects such as the direction the player is facing or the direction of pressuring opponents, both of which would intuitively be factors that ought to be considered. Can a model that incorporates these factors be devised and experimentally tested?_ 

4. **Rebounding.** Traditionally a player’s rebounding performance has been measured as the average number of rebounds per game. Maheswaran et al. [57] presented a model to quantify the potential to rebound unsuccessful shots in basketball in more detail. Simplified the model considers three phases. The first phase is the _position_ of the players when the shot is made. From the time that the ball is released until it hits the rim, the players will try to move into a better position – the _crash_ phase. After the crash phase the players have the chance to make the rebound. The proficiency of a player in rebounding is the measured by the _conversion_ – the third phase. Both the positioning phase and the crash phase make use of the dominant region (Voronoi diagram) to value the position of the player, i.e., they compute a “real estate” value of the dominant region of each player both when the shot is made, and when the shot hits the rim. These values, together with the conversion, are combined into a _rebounding_ value. 

## **4 Network tools for team performance analysis** 

Understanding the interaction between players is one of the more important and complex problems in sports science. Player interaction can give insight into a team’s playing style, or be used to assess the importance of individual players to the team. Capturing the interactions between individuals is a central goal 

15 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

**Fig. 9:** _Comparing the pressure that the encircled player is under in the two pictures shows that the encircled player in the right figure is under much more pressure._ 

of social network analysis [84] and techniques developed in this discipline have been applied to the problem of modelling player interactions. 

An early attempt to use networks for sports analysis was in an entertaining study by Gould and Gatrell [39] where they explore all passes made in the 1977 FA Cup Final between Liverpool and Manchester United. They studied the simplicial complexes of the passing network and made several interesting observations, including that the Liverpool team had two “quite disconnected” subsystems and that Kevin Keegan was “the linchpin of Liverpool”. However, their analysis, while innovative, did not attract much attention. 

In the last decade numerous papers have appeared that apply social network analysis to team sports. Two types of networks have dominated the research literature to date: _passing networks_ and _transition networks_ . 

Passing networks have been most frequently studied type in the research field. To the best of our knowledge, they were first introduced by Passos et al. [64]. A passing network is a graph _G_ = ( _V, E_ ) where each player is modelled as a vertex and two vertices _v_ 1 and _v_ 2 in _V_ have a directed edge _e_ = ( _v_ 1 _, v_ 2) from _v_ 1 to _v_ 2 with integer weight _w_ ( _e_ ) such that the player represented by vertex _v_ 1 has made _w_ ( _e_ ) successful passes to the player represented by vertex _v_ 2. A small example of a passing graph is shown in Fig. 10a. Passing networks can be constructed directly from _event logs_ , defined in Section 2. A temporal sequence of passes made in a match is encoded as a path within the passing network. A passing network that is extended with outcomes, as illustrated in Fig. 10b, is then referred to as a _transition network_ . 

Many properties of passing networks have been studied, among them _density_ , _heterogeneity_ , _entropy_ , and _Nash equilibria_ . However, the most studied measurement is _centrality_ . We begin by considering centrality and its variants, and then we briefly consider some of the other measures discussed in the literature. 

### **4.1 Centrality** 

Centrality measures were introduced in an attempt to determine the key nodes in a network, for example, to identify the most popular persons in a social network 

16 



<!-- Start of picture text -->
8 8 2 shot on goal<br>A C A C<br>2 2<br>1 shot of goal<br>4 2 4 5 4 2 4 5 3<br>lost possession<br>2<br>B D B D<br>1 1 free kick<br>1<br>(a) (b)<br><!-- End of picture text -->

**Fig. 10:** _(a) A passing network modelling four players {A, B, C, D} and the passes between the players. (b) A transition network is a passing network extended with outcomes. For example, twice player C made a shot on goal and once the player lost possession._ 

or super-spreaders of a disease [62]. In team sports the aim of using centrality measurements is generally to identify key players, or to estimate the interactivity between team members. For an excellent survey on network centrality see Borgatti [8]. 

**Degree centrality** The simplest centrality measure is the _degree centrality_ , which is the number of edges incident to a vertex. For directed networks one usually distinguish between the in-degree and the out-degree centrality. In sports analysis the out-degree centrality is simply referred to as _centrality_ while the in-degree centrality is usually called the _prestige_ of a player. Some papers do consider both centrality and prestige, see for example Clemente et al. [24], but most of the literature has focused on centrality. 

Fewell et al. [28] considered a transition graph on basketball games where the vertices represented the five traditional player positions (point guard, shooting guard, small forward, power forward, and center), possession origins and possession outcomes. The centrality was computed on the transition graph, split into two outcomes: “shots” and “others”. The measure was computed on 32 basketball games and prior knowledge about the importance of players to the teams involved was compared to the centrality values of the players. They used degree centrality to compare teams that heavily rely on key players with teams with a more even distribution between their team members. Unfortunately, the data was not definitive since the overall centrality rankings did not show a strong relation to the teams performance. 

Grund [40] used degree centrality together with Freeman centralization [34]. The idea by Freeman was to consider the relative centrality of the most important node in the network. That is, how central is the most central node compared to the centrality of the other nodes in the network. The Freeman centrality is measured as the sum of the differences between the node with the highest degree centrality and all other nodes; divided by a value depending only on the size of the network [34]. They used an extensive set of 283 259 passes from 760 English 

17 

Premier League games for their experiments. From a team performance perspective Grund [40] set out to answer two hypotheses: (i) increased interaction between players leads to increased team performance; and (ii) increased interaction centralization leads to decreased team performance. The latter is strongly connected to centrality and Grund [40] went on to show that a high level of centralization decreases team performance. 

In a series of recent papers, Clemente _et al._ argue that centrality may recognise how players collaborate, and also the nature and strength of their collaboration. For example, central midfielders and central defenders usually show higher degree centrality then other players. Some exceptions were shown in Clemente et al. [22] where the left and right defenders also obtained very high degree centrality. In general goal-keepers and forwards have the lowest centrality measure. 

**Betweenness Centrality** The betweeness centrality of a node is the number of times it lies on the shortest path between two other nodes in the network. Originally it was introduced by Freeman [33] in an attempt to estimate “a human’s potential control of communication in a social network”. 

Pe˜na and Touchette [65] claimed that the betweenness centrality measures how the ball-flow between players depends on a particular player and as such provides a measure of the impact of the “removal” of that player from the game, either by being sent off or by being isolated by the opponents. They also argued that, from a tactical point of view, a team should aim to have a balanced betweenness score for all players. 

A centrality measure closely related to the betweenness centrality is flow centrality. The flow centrality is measured by the proportion of the entire flow between two vertices that occur on paths of which a given vertex is a part. 

Duch et al. [27] considered flow centrality for transition networks where the weight of an edge from a player _v_ 1 to a player _v_ 2 is equal to the fraction of passes initiated by _v_ 1 to reach _v_ 2. Similarly, the shooting accuracy for a player (the weight of the edge from the player to the vertex “shots on goal”) is the fraction of shots made by the player that end up on goal. They then studied the flow centrality over all paths that results in a shot. They also take the defensive performance into account by having each player initiate a number of flow paths which is comparable to the number of times the player wins possession of the ball. The _match performance_ of the player is then the normalised value of the logarithm of this combined value. They argue that this gives an estimate of the contribution of a single player and also of the whole team. The team’s match performance value is the mean of the individual player values. Using these values, both for teams and individual players, Duch et al. [27] analysed 20 games from the football 2008 UEFA European Cup. They claim that their measurements provide “sensible results that are in agreement with the subjective views of analysts and spectators”, in other words, the better paid players tend to contribute more to the team’s performance. 

18 

**Closeness Centrality** The standard distance metric used in a network is the length (weight or cost) of the shortest path between pairs of nodes. The _closeness centrality_ of a node is defined as the inverse of the _farness_ of the node, which is the sum of its distance to all other nodes in the network Bavelas [2]. Pe˜na and Touchette [65] argued that the closeness score is an estimate of how easy it is to get the ball to a specific player, i.e., a high closeness score indicates a wellconnected player within the team. They made a detailed study using the 2010 FIFA World Cup passing data. The overall conclusion they reached was that there is a high correlation between high scores in closeness centrality, _PageRank_ and clustering (see below), which supports the general perception of the players performance reported in the media at the time of the tournament. 

**Eigenvector Centrality and** **_PageRank_** The general idea of Eigenvector centrality and PageRank is that the importance of a node depends, not only on its degree, but also on the importance of its neighbours. Cotta et al. [25] used the eigenvector centrality calculated with the power iteration model by von Mises and Pollaczek-Geiringer [82]. The measure aims to identify which player has the highest probability to be in possession of the ball after a sequence of passes. They also motivated their measure by a thorough analysis of three games from the 2010 FIFA World Cup, where they argued the correlation between the eigenvector centrality score and the team’s performance. 

A variant of the eigenvector centrality measure is _PageRank_ , which was one of the algorithms used by Google Search to rank web-pages [14]. The passing graph is represented as an adjacency matrix _A_ where each entry _Aji_ is the number of passes from player _j_ to player _i_ . In football terms, the _PageRank_ centrality index for player _i_ is defined as: 



where _L_<sup>_out_</sup> _j_ =<sup>�</sup> _k_<sup>_Ajk_isthetotalnumberofpassesmadebyplayer</sup><sup>_j_,</sup><sup>_p_isthe</sup> parameter representing the probability that a player will decide to give the ball away rather than keep it and shoot, and _q_ is a ‘free’ popularity assigned to each player. Note that the _PageRank_ score of a player is dependant on the scores of the player’s team mates. Pe˜na and Touchette [65] argue that the _PageRank_ measure gives each player a value that is approximately the likelihood that the player will be in possession of the ball after a fixed number of passes. Using data from the 2010 FIFA World Cup, they computed the _PageRank_ for the players in the top 16 teams, but focused their discussion on the players in the top four teams: Spain, Germany, Uruguay and the Netherlands. They showed that the _PageRank_ of players in the Dutch and Uruguay teams were more evenly distributed than players from Spain and Germany. This indicates that no player in those teams has a predominant role in the passing scheme while Xavi Hernandez (Spain) and Bastian Schweinsteiger (Germany) were particularly central to their teams. 

19 

### **4.2 Clustering Coefficients** 

A clustering coefficient is a measure of the degree of which nodes in a network are inclined to cluster together. In the sport science literature both the _global_ and the _local_ clustering coefficients have been applied. The idea of studying the global cluster coefficient of the players in a team is that it reflects the cooperation between players, that is, the higher coefficient for a player the higher is his cooperation with the other members of the team [21, 28, 65]. Fewell et al. [28] also argued that a high global clustering coefficient indicates that attacking decisions are taken by several players, and thus increases the number of possible attacking paths that have to be assessed by the defence. Pe˜na and Touchette [65] showed, using the 2010 FIFA World Cup passing data, that Spain, Germany and the Netherlands consistently had very high clustering scores when compared to Uruguay, suggesting that they were extremely well connected teams, in the sense that almost all players contribute. 

Cotta et al. [25] considered three games involving Spain from the 2010 FIFA World Cup and used the local clustering coefficient as a player coefficient. They studied how the coefficient changed during the games, and argued for a correlation between the number of passes made by Spain and the local clustering coefficient. They claimed that Spain’s clustering coefficient remains high over time, “indicating the elaborate style of the Spanish team”. 

It should be noted that it is not completely clear that there is a strong connection between the clustering coefficient and the team performance. For example, Pe˜na and Touchette [65] stated that in their study they did not get any reasonable results and “will postpone the study of this problem for future work.” 

**Open 4** _Various centrality and clustering measures have been proposed to accurately represent some aspect of player or team performance. A systematic study reviewing all such measures against predefined criteria, and on a large dataset would be a useful contribution to the field._ 

### **4.3 Density and Heterogeneity** 

In general it is believed that stronger collaboration (i.e. more passes) will make the team stronger. This is known as the _density-performance hypothesis_ [1]. Therefore a widely-assessed measure of networks is density, which is traditionally calculated as the number of edges divided by the total number of possible edges. This is the density measure used by Clemente et al. in a series of recent papers . For weighted graphs the measurement becomes slightly more complex. Grund [40] defined the _intensity_ of a team as the sum of the weighted degrees over all players divided by the total time the team have possession of the ball, i.e., possession-weighted passes per minute. 

Related to the density is _passing heterogeneity_ , which Cintia et al. [20] defined as the standard deviation of the vertex degree for each player in the network. High heterogeneity of a passing network means that the team tends to coalesce 

20 

into sub-communities, and that there is a low level of cooperation between players [23]. One interesting observation made by Clemente et al. [23] was that the density usually went down in the 2nd half while the heterogeneity went up. 

**Open 5** _The density-performance hypothesis suggests an interesting metric of team performance. Can this hypothesis be tested scientifically?_ 

### **4.4 Entropy, Topological Depth, Price-of-Anarchy and Power Law Distributions** 

As described above, Fewell et al. [28] considered an extended transition graph for basketball games, where they also calculated _player entropy_ . Shannon entropy [73] was used to estimate the uncertainty of a ball transition. The _team entropy_ is the aggregated player entropies, which can be computed in many different ways. Fewell et al. [28] argue that from the perspective of the opposing team the real uncertainty is the number of options, and computed the team entropy from the transition matrix describing ball movement probabilities across the five standard player positions and the two outcomes. 

Skinner [75] showed that passing networks have two interesting properties. They identified a correspondence between a basketball transition network and a traffic network, and used insights from the latter to make suppositions about the former. They posited that there may be a difference between the Nash equilibrium of a transition network and the community optimum – the _Price of Anarchy_ . In other words, for the best outcome one should not always select the highest-percentage shot. A similar observation was made in Fewell et al. [28] who noted that the low flow centrality of the most utilised position (point guard) seems to indicate that the contribution of key players can be negatively affected by controlling the ball more often than other players. Related to the same concept, Skinner [75] suggested that removing a key player from a match – and hence the transition network – may actually _improve_ the team performance, a phenomena known as the _Braess’ paradox_ in network analysis [13]. 

## **5 Data Mining** 

The representations and structures described in Sections 2–4 are informative in isolation, but may also be the input for more complex algorithmic and probabilistic analysis of team sports. In this section, we present a task-oriented survey of the techniques that have been applied, and outline the motivations for these tasks. 

### **5.1 Applying Labels to Events** 

Sports analysts are able to make judgments about events and situations that occur in a match, and apply qualitative or quantitative attributes to that event, for example, to rate the riskiness of an attempted shot on goal, or the quality 

21 

of a pass. Event labels such as these can be used to measure player and team performance, and are currently obtained manually by video analysis. Algorithmic approaches to automatically produce such labels may improve the efficiency of the process. 

Horton et al. [43] presented a classifier that determines the quality of passes made in football matches by applying a label of _good_ , _OK_ or _bad_ to each pass made, and were able to obtain an accuracy rate of 85 _._ 8 %. The classifier uses features that are derived from the spatial state of the match when the pass occurs, including features derived from the dominant region described in Section 3.3, which were found to be important features to the classifier. 

In research by Beetz et al. [3], the approach was to cluster passes, and to then induce a decision tree on each cluster where the passes were labelled as belonging to the cluster or not. The feature predicates, learned as splitting rules, in the tree could then be combined to provide a description of the important attributes of a given pass. 

Bialkowski et al. [5] used the formation descriptors computed with the algorithm presented in [6] (see Section 5.3) to examine whether formations could accurately predict the identity of a team. In the model, a linear discriminant analysis classifier was trained on features describing the team formation, and the learned model was able to obtain an accuracy of 67 _._ 23 % when predicting a team from a league of 20 teams. 

In Maheswaran et al. [56] the authors perform an analysis of various aspects of the rebound in basketball to produce a rebound model. The rebound is decomposed into three components: the location of the shot attempt; the location where the rebound is taken; and the height of the ball when the rebound is taken. Using features derived from this model, a binary classifier was trained to predict whether a missed shot would be successfully rebounded by the offensive team. The model was evaluated and obtained an accuracy rate of 75 % in experiments on held-out test data. 

### **5.2 Predicting Future Event Types and Locations** 

The ability to predict how play will unfold given the current game-state has been researched extensively, particularly in the computer vision community. This has an application in automated camera control, where the camera filming a match must automatically control its pitch, tilt and zoom. The framing of the scene should ideally contain not just the current action, but the movement of players who can be expected to be involved in future action, and the location of where such future action is likely to occur. 

Kim et al. [46] considered the problem of modelling the evolution of football play from the trajectories of the players, such that the location of the ball at a point in the near future could be predicted. Player trajectories were used to compute a dense motion field over the entire playing area, and points of convergence within the motion field identified. The authors suggest that these points of convergence indicate areas where the ball can be expected to move to 

22 

with high probability, and the experiments described in the paper demonstrate this with several examples. 

Yue et al. [89] construct a model to predict whether a basketball player will shoot, pass to one of four teammates, or retain possession. The action a player takes is modelled using a multi-class conditional random field. The input features to the classifier include latent factors representing player locations which are computed using non-negative matrix factorization, and the experimental results show that these features improve the predictive performance of the classifier. 

Wei et al. [86] constructed a model to make short-term predictions of which football player will be in possession of the ball after a given interval. They propose a model – augmented-Hidden Conditional Random Fields (aHCRF) – that combines local observation features with the hidden layer states to make the final prediction of the player who possess the ball. The experimental results show that they are able to design a model that can predict which player will be in possession of the ball after 2 s with 99 _._ 25 % accuracy. 

### **5.3 Identifying Formations** 

Sports teams use pre-devised spatial formations as a tactic to achieve a particular objective. The ability to automatically detect such formations is of interest to sports analysts and coaches. For example, a coach would be interested in understanding the proportion of time that a team maintains an agreed formation, and also when the team is compelled by the circumstances of the match to alter its formation. Moreover, when preparing for a future opponent, an understanding of the formation used, and periods where the formation changes would be of interest. 

A formation is a positioning of players, relative to the location of other objects, such as the pitch boundaries or goal/basket, the players’ team-mates, or the opposition players. Formations may be spatially anchored, for example a zone defence in basketball where players position themselves in a particular location on the playing area, see Fig. 11a. On the other hand, a formation may vary spatially, but maintain a stable relative orientation between the players in the formation. For example, the defensive players in a football team will position themselves in a straight line across the pitch, and this line will move as a group around the pitch, depending on the phase of play, Fig. 11c. Finally, a different type of formation is a _man marking_ defence, where defending players will align themselves relative to the attacking players that they are marking, Fig. 11b. In this scenario, the locations of defenders may vary considerably, relative to their teammates or to the boundaries of the playing area. 

Moreover, the players that fulfil particular roles within a formation may switch, either explicitly through substitutions or dynamically where players may swap roles for tactical reasons. The following approaches have been used to determine formations from the low-level trajectory signal. 

Lucey et al. [53] investigated the assignment of players to roles in field hockey, where teams use a formation of three lines of players arrayed across the field. At 

23 





<!-- Start of picture text -->
(a) Zone Defence (b) Man-marking Defence (c) Back-four Defence<br><!-- End of picture text -->

**Fig. 11:** _Examples of typical formations used in basketball and football. (a) The zone defence is spatially anchored to the dimensions of the court and the players positioning is invariant to the phase of play. (b) Defenders who are man-marking will align themselves relative to their opposing player, typically between the attacker and the basket. (c) The back-four formation in football maintains the alignment of players in the formation, but will move forward and laterally, depending on the phase of play._ 

any time _t_ there is a one-to-one assignment of players to roles, however this assignment may vary from time-step to time-step. This problem is mathematically equivalent to permuting the player ordering **p**<sup>_τ_</sup> _t_<sup>usingapermutationmatrix</sup><sup>**x**</sup><sup>_τ_</sup> _t_ which assigns the players to roles _rt_<sup>_τ_=</sup><sup>**x**</sup><sup>_τ_</sup> _t_<sup>**p**</sup><sup>_τ_</sup> _t_<sup>.Theoptimalpermutationmatrix</sup> **x**<sup>_τ_</sup> _t_<sup>shouldminimisethetotalEuclideandistancebetweenthereferencelocation</sup> of each role and the location of the player assigned to the role, and can be computed in closed form using the Hungarian algorithm [49]. 

Wei et al. [85] used this approach as a preprocessing step on trajectory data from football matches, and the computed role locations were subsequently used to temporally segment the matches into game phases. Lucey et al. [54] applied role assignment to basketball players in sequences leading up to three-point shots. They analysed close to 20 000 such shots and found that role-swaps involving particular pairs of players in the moments preceding a three-point shot have a significant impact on the probability of the shooter being _open_ – at least 6 feet away from the nearest marker – when the shot is made. 

Furthermore, Bialkowski et al. [6] observed that the role assignment algorithm presented by Lucey et al. [53] required a predefined prototype formation to which the players are assigned. They consider the problem of simultaneously detecting the reference location of each role in the formation, and assigning players to the formation, using an expectation maximization approach [26]. The initial role reference locations are determined as the mean position of each player. The algorithm then uses the Hungarian algorithm to update the role assignment for each player at each time-step, and then the role reference locations are re- 

24 

computed according to the role assignment. The new locations are used as input for the next iteration, and process is repeated until convergence. 

The learned formations for each team and match were then clustered into six formations, and the authors claim that the clustered formations were consistent with expert knowledge of formations used by football teams. This was validated experimentally by comparing the computed formation with a formation label assigned by an expert, and an accuracy of 75 _._ 33 % was obtained. 

In a subsequent paper, Bialkowski et al. [4] investigated differences in team strategies when playing home or away, by using formations learned with the role assignment algorithm. By computing the mean position when teams are playing at home from when they are playing away, they observed that teams defend more deeply when away from home, in other words they set their formation closer to the goal they are defending. 

A qualitatively different formation is for players to align themselves with the positions of the opposition players, such as _man-marking_ defense used in basketball, see Fig. 11b. Franks et al. [31] defined a model to determine which defender is marking each attacker. For a given offensive player at a given time, the mean location of the defender is modelled as a convex combination of three locations: the position of the attacker, the location of the ball and the location of the hoop. The location of a defender, given the observed location of the marked attacker, is modelled as a Gaussian distribution about a mean location. The matching between defenders and the attacker that they are marking over a sequence of time-steps is modelled using a Hidden Markov Model, ensuring that the marking assignments are temporally smoothed. 

### **5.4 Identifying Plays and Tactical Group Movement** 

Predefined _plays_ are used in many team sports to achieve some specific objective. American football uses highly structured plays where the entire team has a role and their movement is highly choreographed. On the other hand, plays may also be employed in less structured sports such as football and basketball when the opportunity arises, such as the _pick and roll_ in basketball or the _onetwo_ or _wall pass_ in football. Furthermore, teammates who are familiar with each other’s playing style may develop ad-hoc productive interactions that are used repeatedly, a simple example of which is a sequence of passes between a small group of players. Identification of plays is a time-consuming task that is typically carried out by a video analyst, and thus a system to perform the task automatically would be useful. 

An early attempt in this direction attempted to recognise predefined plays in American football [45]. They model a play as a choreographed sequence of movements by attacking players, each trying to achieve a local goal, and in combination achieve a group goal for the play. The approach taken was to encode predefined tactical plays using a temporal structure description language that described a local goal in terms of a sequence of actions carried out by an individual player. These local goals were identified in the input trajectories using a Bayesian belief network. A second belief network then identified whether a 

25 

global goal had been achieved based on the detected local goals – signifying that the play has occurred. 

Two papers by Li _et al._ investigated the problem of identifying group motion, in particular the type of offensive plays in American football. Li et al. [51] presented the Discriminative Temporal Interaction Network (DTIM) framework to characterise group motion patterns. The DTM is a temporal interaction matrix that quantifies the interaction between objects at two given points in time. For each predefined group motion pattern – a play – a multi-modal density was learned using a properly defined Riemannian metric, and a MAP classifier was then used to identify the most likely play for a given input set of trajectories. The experiments demonstrated that the model was able to accurately classify sets of trajectories into five predefined plays, and outperformed several other common classifiers for the task. This model has the advantage of not requiring an _a priori_ definition of each player’s movement in the play, as required in Intille and Bobick [45]. 

Li and Chellappa [50] considered group motion segmentation, where a set of unlabelled input trajectories are segmented into the subset that participated in the group motion, and those that did not. The problem was motivated by the example of segmenting a set of trajectories into the set belonging to the offensive team (who participated in the play) and the defensive team (who did not). The group motion is modelled as a dynamic process driven by a _spatiotemporal driving force_ – a densely distributed motion field over the playing area. The driving force is modelled as a 3 _×_ 3 matrix _F_ ( _t_ 0 _, tf , x, y_ ) such that _X_ ( _tf_ ) = _F_ ( _t_ 0 _, tf , x, y_ ) _X_ ( _t_ 0). Thus, an object located at _X_ ( _t_ 0) at time _t_ 0 will be driven to _X_ ( _tf_ ) at time _tf_ . Using Lie group theory [72], a Lie algebraic representation _f_ of _F_ is determined with the property that the space of all _f_ s is linear, and thus tractable statistical tools can be developed upon _f_ . A Gaussian mixture model was used to learn a fixed number of driving forces at each time-step, which was then used to segment the trajectories. 

There has been number of diverse efforts to identify commonly occurring sequences of passes in football matches. In Borrie et al. [9], the pitch is subdivided into zones and sequences of passes are identified by the zones that they start and terminate in. A possession can thus be represented by a string of codes representing each pass by source and target zone, and with an elapsed time between them. They introduce _T-pattern_ analysis which is used to compute possessions where the same sequence of passes are made with consistent time intervals between each pass, and frequently occurring patterns could thus be identified. Camerino et al. [15] also used T-pattern analysis on pass strings, however the location of passes was computed relative to the formation of the team in possession, e.g. between the defense and midfield, or in front of the attacking line. 

An algorithm to detect frequently occurring sequences of passes was presented in Gudmundsson and Wolle [41]. A suffix tree [87] was used as a data structure _D_ to store sequences of passes between individual players. A query ( _τ, o_ ) can then be made against _D_ that returns all permutations of _τ_ players 

26 

such that the ball is passed from a player _p_ 1 to _pτ_ , via players _p_ 2 _, . . . , pτ −_ 1 at least _o_ times, and thus determine commonly used passing combinations between players. 

Van Haaren et al. [81] considered the problem of finding patterns in offensive football strategies. The approach taken was to use inductive logic programming to learn a series of clauses describing the pass interactions between players during a possession sequence that concludes with a shot on goal. The passes were characterised by their location on the pitch, and a hierarchical model was defined to aggregate zones of the pitch into larger regions. The result is a set of rules, expressed in first-order predicate logic, describing the frequently-occurring interaction sequences. 

Research by Wang et al. [83] also aimed to detect frequent sequences of passing. They claim that the task of identifying tactics from pass sequences is analogous to identifying topics from a document corpus, and present the Team Tactic Topic Model (T<sup>3</sup> M) based on Latent Dirichlet Allocation [7]. Passes are represented as a tuple containing an order-pair of the passer and receiver, and a pair of coordinates representing the location where the pass was received. The T<sup>3</sup> M is an unsupervised approach for learning common tactics, and the learned tactics are coherent with respect to the location where they occur, and the players involved. 

### **5.5 Temporally Segmenting the Game** 

Segmenting a match into phases based on a particular set of criteria is a common task in sports analysis, as it facilitates the retrieval of important phases for further analysis. The following paragraphs describe approaches that have been applied this problem for various types of criteria. 

Hervieu _et al._ present a framework for labelling phases within a handball match from a set of predefined labels representing common attacking and defensive tactics. The model is based on a hierarchical parallel semi-Markov model (HPaSMM) and is intended to model the temporal causalities implicit in player trajectories. In other words, modelling the fact that one player’s movement may cause another player to subsequently alter their movement. The upper level of the hierarchical model is a semi-Markov model with a state for each of the defined phase labels, and within each state the lower level is a parallel hidden Markov model for each trajectory. The duration of time spent in each upper level state is modelled using a Gaussian mixture model. In the experiments, the model was applied to a small dataset of handball match trajectories from the 2006 Olympics Games final, and resulted in accuracy of 92 % accuracy on each time-step, compared to the ground truth provided by an expert analyst. The model exactly predicted the sequence of states, and the misclassifications were all the result of time-lags when transitioning from one state to the subsequent state. 

Perˇse et al. [67] investigated segmentation of basketball matches. A framework with two components was used, the first segmented the match duration into sequences of offensive, defensive or time-out phases. The second component 

27 

identified basic activities in the sequence by matching to a library of predefined activities, and the sequences of activities were then matched with predefined templates that encoded known basketball plays. 

Wei et al. [85] considered the problem of automatically segmenting football matches into distinct game phases that were classified according to a two-level hierarchy, using a decision forest classifier. At the top level, phases were classed as being _in-play_ or a _stoppage_ . _In-play_ phases were separated into highlights or nonhighlights; and _stoppages_ were classified by the reason for the stoppage: _out for corner_ , _out for throw-in_ , _foul_ or _goal_ . The classified sequences were subsequently clustered to find a team’s most probable method of scoring and of conceding goals. 

In a pair of papers by Bourbousson _et al._ , the spatial dynamics in basketball was examined using relative-phase analysis. In Bourbousson et al. [10], the spatial relation between dyads of an attacking player and their marker were analysed. In Bourbousson et al. [11], the pairwise relation between the centroid of each team was used, along with a _stretch index_ that measured the aggregate distance betweens players and their team’s centroid. A Hilbert transformation was used to compute the relative phase in the _x_ and _y_ direction of the pairs of metrics. Experimental results showed a strong in-phase relation between the various pairs of metrics in the matches analysed, suggesting individual players and also teams move synchronously. The authors suggest that the spatial relations between the pairs are consistent with their prior knowledge of basketball tactics. 

Frencken et al. [35] performed a similar analysis of four-a-side football matches. They used the centroid and the convex hull induced by the positions of the players in a team to compute metrics, for example the distance in the _x_ and _y_ direction of the centroid, and the surface area of the convex hull. The synchronized measurements for the two teams were modelled as coupled oscillators, using the HKB-model [42]. Their hypothesis was that the measurements would exhibit in-phase and anti-phase coupling sequences, and that the anti-phase sequences would denote game-phases of interest. In particular, the authors claim that there is a strong linear relationship between the _x_ -direction of the centroid of the two teams, and that phases where the centroid’s _x_ -directions cross are indicative of unstable situations that are conducive to scoring opportunities. They note that such a crossing occurs in the build up to goals in about half the examples. 

**Open 6** _Coaches and analysts are often interested in how the_ intensity _of a match varies over time, as periods of high intensity tend to be present more opportunities and threats. It is an interesting open problem to determine if it is possible to compute a measure of intensity from spatio-temporal data, and thus be able to determine high-intensity periods._ 

## **6 Performance Metrics** 

Determining the contribution of the offensive and defensive components of team play has been extensively researched, particularly in the case of basketball which 

28 

has several useful properties in this regard. For example, a basketball match can be easily segmented into a sequence of _possessions_ – teams average around 92 possessions per game [48] – most of which end in a shot at goal, which may or may not be successful. This segmentation naturally supports a variety of offensive and defensive metrics [48], however the metrics are not spatially informed, and intuitively, spatial factors are significant when quantifying both offensive and defensive performance. In this section we survey a number of research papers that use spatio-temporal data from basketball matches to produce enhanced performance metrics. 

### **6.1 Performance** 

Shooting effectiveness is the likelihood that a shot made will be successful, and _effective field goal percentage_ (EFG) is a de-facto metric for offensive play in basketball [48]. However, as Chang et al. [18] observe, this metric confounds the efficiency of the shooter with the difficulty of the shot. Intuitively, spatial factors such as the location where a shot was attempted from, and the proximity of defenders to the shooter would have an impact of the difficulty of the shot. This insight has been the basis of several efforts to produce metrics that provide a more nuanced picture of a player or team’s shooting efficiency. 

Early work in this area by Reich et al. [71] used shot chart data (a list of shots attempted, detailing the location, time, shooter and outcome of each shot). The paper contained an in-depth analysis of the shooting performance of a single player – Sam Cassell of the Minnesota Timberwolves – over the entire 2003/2004 season. A vector of boolean-valued predictor variables was computed for each shot, and linear models fitted for shot frequency, shot location and shot efficiency. By fitting models on subsets of the predictor variables, the authors analysed the factors that were important in predicting shot frequency, location and efficiency. 

Miller et al. [58] investigated shooting efficiency by using vectors computed with non-negative matrix factorization to represent spatially distinct shot-types, see Section 3.2. The shooting factors were used to estimate spatial shooting efficiency surfaces for individual players. The efficiency surfaces could then be used to compute the probability of a player making a shot conditioned on the location of the shot attempt, resulting in a spatially-varying shooting efficiency model for each individual player. 

Cervone et al. [17] present _expected possession value_ (EPV), a continuous measure of the expected points that will result from the current possession. EPV is thus analogous to a “stock ticker” that provides a valuation of the possession at any point in time during the possession. The overall framework consists of a macro-transition model that deals with game-state events such as passes, shots and turnovers, and micro-transition model that describes player movement within a phase when a single player is in possession of the ball. Probability distributions, conditioned on the spatial layout of all players and the ball, are learned for the micro- and macro-transition models. The spatial effects are 

29 

modelled using non-negative matrix factorization to provide a compact representation that the authors claim has the attributes of being computationally tractable with good predictive performance. The micro- and macro-transition models are combined in a Markov chain, and from this the expected value of the end-state – scoring 0, 2 or 3 points – can be determined at any time during the possession. Experimental results in the paper show how the EPV metric can support a number of analyses, such as _EPV-Added_ which compares an individual player’s offensive value with that of a league-average player receiving the ball in the same situation; or _Shot Satisfaction_ which quantifies the satisfaction (or regret) of a player’s decision to shoot, rather than taking an alternative option such as passing to a teammate. 

Chang et al. [18] introduces another spatially-informed measure of shooting quality in basketball: _Effective Shot Quality_ (ESQ). This metric measures the value of a shot, were it to be taken by the league-average player. ESQ is computed using a learned least-squares regression function whose input includes spatial factors such as the location of the shot attempt, and the proximity of defenders to the shooter. Furthermore, the authors introduce EFG+, which is calculated by subtracting ESQ from EFG. EFG+ is thus an estimate of how well a player shoots relative to expectation, given the spatial conditions under which the shot was taken. 

A further metric, _Spatial Shooting Effectiveness_ , was presented by Shortridge et al. [74]. Using a subdivision of the court, an empirical Bayesian scoring rate estimator was fitted using the neighbourhood of regions to the shot location. The spatial shooting effectiveness was computed for each player in each region of the subdivision, and is the difference between the points-per-shot achieved by the player in the region and the expected points-per-shot from the estimator. In other words, it is the difference between a player’s expected and actual shooting efficiency, and thus measures how effective a player is at shooting, relative to the league-average player. 

Lucey et al. [55] considered shooting efficiency in football. They make a similar observation that the location where a shot is taken significantly impacts the likelihood of successfully scoring a goal. The proposed model uses logistic regression to estimate the probability of a shot succeeding – the _Expected Goal Value_ (EGV). The input features are based on the proximity of defenders to the shooter and to the path the ball would take to reach the goal; the location of the shooter relative to the lines of players in the defending team’s formation; and the location where the shot was taken from. The model is empirically analysed in several ways. The number of attempted and successful shots for an entire season is computed for each team in a professional league, and compared to the expected number of goals that the model predicts, given the chances. The results are generally consistent, and the authors are able to explain away the main outliers. Furthermore, matches where the winning team has fewer shots at goal are considered individually, and the expected goals under the model are computed. This is shown to be a better predictor of the actual outcome, 

30 

suggesting that the winning team was able to produce fewer – but better – quality chances. 

### **6.2 Defensive Performance** 

Measures of defensive performance have traditionally been based on summary statistics of _interventions_ such as blocks and rebounds in basketball [48] and tackles and clearances in football. However, Goldsberry and Weiss [38] observed that, in basketball the defensive effectiveness ought to consider factors such as the spatial dominance by the defence of areas with high rates of shooting success; the ability of the defence to prevent a shot from even being attempted; and secondary effects in the case of an unsuccessful shot, such as being able to win possession or being well-positioned to defend the subsequent phase. 

In order to provide a finer-grained insight into defensive performance, Goldsberry and Weiss [38] presented _spatial splits_ that decompose shooting frequency and efficiency into a triple consisting of close-range, mid-range and 3-point-range values. The offensive half-court was subdivided into three regions, and the shot frequency and efficiency were computed separately for shots originating in each region. These offensive metrics were then used to produce defensive metrics for the opposing team by comparing the relative changes in the splits for shots that an individual player was defending to the splits for the league-average defender. 

An alternate approach to assessing the impact of defenders on shooting frequency and efficiency was taken by Franks _et al._ . They proposed a model that quantifies the effectiveness of man-to-man defense in different regions of the court. The proposed framework includes a model that determines who’s marking whom by assigning each defender to an attacker. For each attacker, the canonical position for the defender is computed, based on the relative spatial location of the attacker, the ball and the basket. A hidden Markov model is used to compute the likelihood of an assignment of defenders to attackers over the course of a possession, trained using the expectation maximization algorithm [26]. A second component of the model learned spatially coherent shooting type bases using non-negative matrix factorization on a shooting intensity surface fitted using a log-Gaussian Cox process. By combining the assignment of markers and the shot type bases, the authors were able to investigate the extent to which defenders inhibit (or encourage) shot attempts in different regions of the court, and the degree to which the efficiency of the shooter is affected by the identity of the marker. 

Another aspect of defensive performance concerns the actions when a shot is unsuccessful, and both the defence and attack will attempt to _rebound_ the shot to gain possession. This was investigated by Maheswaran et al. [57] where they deconstructed the rebound into three components: _positioning_ ; _hustle_ and _conversion_ , described in Section 3.3. Linear regression was used to compute metrics for player’s _hustle_ and _conversion_ , and experimental results showed that the top-ranked players on these metrics were consistent with expert consensus of top-performing players. 

31 

On the other hand, Wiens et al. [88] performs a statistical evaluation of the options that players in the offensive team have when a shot is made in basketball. Players near the basket can either _crash the boards_ – move closer to the basket in anticipation of making a rebound – or retreat in order to maximise the time to position themselves defensively for the opposition’s subsequent attack. The model used as factors the players’ distance to the basket, and proximity of defenders to each attacking player. The experimental results suggested that teams tended to retreat more than they should, and thus a more aggressive strategy could improve a team’s chances of success. 

The analysis of defense in football would appear to be a qualitatively different proposition, in particular because scoring chances are much less frequent. To our knowledge, similar types of analysis to those presented above in relation to basketball have not been attempted for football. 

**Open 7** _There has been significant research into producing spatially-informed metrics for player and team performance in basketball, however there has been little research in other sports, particularly football. It is an open research question whether similar spatially-informed sports metrics could be developed for football._ 

## **7 Visualisation** 

To communicate the information extracted from the spatio-temporal data, visualization tools are required. For real-time data the most common approach is so-called _live covers_ . This is usually a website that comprise of a text panel that lists high-level updates of the key events in the game in almost real time, and several graphics showing basic information about the teams and the game. Live covers are provided by leagues (e.g. NHL, NBA and Bundesliga), media (e.g. ESPN) and even football clubs (e.g. Liverpool and Paris Saint-Germain). For visualizing aggregated information the most common approach is to use heat maps. Heat maps are simple to generate, are intuitive, and can be used to visualize various types of data. Typical examples in the literature are, visualizing the spread and range of a shooter (basketball) in an attempt to discover the best shooters in the NHL [37] and visualizing the shot distance (ice hockey) using radial heat maps [68]. Two recent attempts to provide more extensive visual analytics systems have been made by Perin et al. [66] and Janetzko _et al._ . 

Perin et al. [66] developed a system for visual exploration of phases in football. The main interface is a timeline and _small multiples_ providing an overview of the game. A _small multiple_ is a group of similar graphs or charts designed to simplify comparisons between them. The interface also allows the user to select and further examine the _phases_ of the game. A phase is a sequence of actions by one team bounded by the actions in which they first win, and then finally lose possession. A selected phase can be displayed and the information regarding a phase is aggregated into a sequence of views, where each view only focus on a specific action (e.g. a long ball or a corner). The views are then connected to show a whole phase, using various visualization tools such as a passing network, a time line and sidebars for various detailed information. 

32 

In two papers Janetzko _et al._ present a visual analysis system for interactive recoginition of football patterns and situations. Their system tightly couple the visualization system with data mining techniques. The system includes a range of visualization tools (e.g., parallel coordinates and scalable bar charts) to show the ranking of features over time and plots the change of game play situations, attempting to support the analyst to interpret complex game situations. Using classifiers they automatically detected the most common situations and introduced semantically-meaningful features for these. The exploration system also allows the user to specify features for a specific situations and then perform a similarity search for similar situations. 

**Open 8** _The area of visual interfaces to support team sports analytics is a developing area of research. Two crucial gaps are large user studies with the aim to (1) explore the analytical questions that experts need support for, and (2) which types of visual analytical tools can be understood by experts?_ 

## **8 Conclusion** 

The proliferation of optical and device tracking systems in the stadia of teams in professional leagues in recent years have produced a large volume of player and ball trajectory data, and this has subsequently enabled a proliferation of research efforts across a variety of research communities. To date, a diversity of techniques have been brought to bear on a number of problems, however there is little consensus on the key research questions or the techniques to use to address them. Thus, we believe that this survey of the current research questions and techniques is a timely contribution to the field. 

This paper surveys the recent research into team sports analysis that is primarily based on spatio-temporal data, and describes a framework in which the various research problems can be categorised. We believe that the structured approach used in this survey reflects a useful classification for the research questions in this area. Moreover, the survey should be useful as a concise introduction for researchers who are new to the 

33 

# **Bibliography** 

- [1] Prasad Balkundi and David A. Harrison. Ties, Leaders, And Time In Teams: Strong Inference About Network Structures Effects On Team Viability And Performance. _Academy of Management Journal_ , 49(1):49– 68, feb 2006. ISSN 0001-4273. doi: 10.5465/AMJ.2006.20785500. URL `http://amj.aom.org/cgi/doi/10.5465/AMJ.2006.20785500` . 

- [2] Alex Bavelas. Communication Patterns in Task-Oriented Groups. _The Journal of the Acoustical Society of America_ , 22(6):725–730, 1950. 

- [3] Michael Beetz, Nicolai von Hoyningen-Huene, Bernhard Kirchlechner, Suat Gedikli, Francisco Siles, Murat Durus, and Martin Lames. ASPOGAMO: Automated Sports Games Analysis Models. _International Journal of Computer Science in Sport_ , 8(1):1–21, 2009. 

- [4] Alina Bialkowski, Patrick Lucey, G. Peter K. Carr, Yisong Yue, and Iain Matthews. Win at home and draw away: automatic formation analysis highlighting the differences in home and away team behaviors. In _Proc. 8th Annual MIT Sloan Sports Analytics Conference_ , pages 1–7, Boston, MA, feb 2014. MIT. URL `http://www.sloansportsconference.com/?p=13005` . 

- [5] Alina Bialkowski, Patrick Lucey, G. Peter K. Carr, Yisong Yue, Sridha Sridharan, and Iain Matthews. Identifying Team Style in Soccer Using Formations Learned from Spatiotemporal Tracking Data. In _2014 IEEE International Conference on Data Mining Workshops, ICDM Workshops_ , pages 9–14, Shenzen, dec 2014. IEEE. doi: 10.1109/ICDMW.2014.167. 

- [6] Alina Bialkowski, Patrick Lucey, Peter Carr, Yisong Yue, Sridha Sridharan, and Iain Matthews. Large-Scale Analysis of Soccer Matches using Spatiotemporal Tracking Data. In _2014 IEEE International Conference on Data Mining_ , ICDM ’14, pages 725–730, Shenzen, dec 2014. IEEE. ISBN 978-1-4799-4302-9. doi: 10.1109/ICDM. 2014.133. URL `http://www.disneyresearch.com/publication/ large-scale-analysis-of-soccer-matches-using-spatiotemporal-tracking-data/ http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber= 7023391` . 

- [7] David M. Blei, Andrew Y. Ng, and Michael I. Jordan. Latent dirichlet allocation. _The Journal of Machine Learning Research_ , 3:993–1022, mar 2003. ISSN 1532-4435. URL `http://dl.acm.org/citation.cfm?id= 944919.944937` . 

- [8] Stephen P. Borgatti. Centrality and network flow. _Social Networks_ , 27(1):55–71, jan 2005. ISSN 03788733. doi: 10.1016/j.socnet.2004. 11.008. URL `http://www.sciencedirect.com/science/article/pii/ S0378873304000693` . 

- [9] Andrew Borrie, Gudberg K Jonsson, and Magnus S Magnusson. Temporal pattern analysis and its applicability in sport: an explanation and exemplar data. _Journal of Sports Sciences_ , 20(10):845–52, 2002. ISSN 0264-0414. 

doi: 10.1080/026404102320675675. URL `http://www.ncbi.nlm.nih.gov/ pubmed/12363299` . 

- [10] J´erˆome Bourbousson, Carole S`eve, and Tim McGarry. Space-time coordination dynamics in basketball: Part 2. The interaction between the two teams. _Journal of Sports Sciences_ , 28(3):349–58, feb 2010. ISSN 1466-447X. doi: 10.1080/02640410903503640. 

- [11] J´erˆome Bourbousson, Carole S`eve, and Tim McGarry. Spacetime coordination dynamics in basketball: Part 1. Intra- and inter-couplings among player dyads. _Journal of Sports Sciences_ , 28(3):339–347, feb 2010. ISSN 02640414. doi: 10.1080/02640410903503632. URL `http://www.tandfonline. com/doi/abs/10.1080/02640410903503632` . 

- [12] Paul Bradley, Peter O’Donoghue, Blake Wooster, and Phil Tordoff. The reliability of ProZone MatchViewer: a video-based technical performance analysis system. _International Journal of Performance Analysis in Sport_ , 7 (3):117–129, 2007. 

- [13] Dietrich Braess, Anna Nagurney, and Tina Wakolbinger. On a Paradox of Traffic Planning. _Transportation Science_ , 39(4):446–450, nov 2005. ISSN 0041-1655. doi: 10.1287/trsc.1050.0127. URL `http://pubsonline. informs.org/doi/abs/10.1287/trsc.1050.0127` . 

- [14] Sergey Brin and Lawrence Page. The anatomy of a large-scale hypertextual Web search engine. _Computer Networks and ISDN Systems_ , 30(1-7):107– 117, apr 1998. ISSN 01697552. doi: 10.1016/S0169-7552(98)00110-X. URL `http://linkinghub.elsevier.com/retrieve/pii/S016975529800110X` . 

- [15] Oleguer Foguet Camerino, Javier Chaverri, M. Teresa Anguera, and Gudberg K. Jonsson. Dynamics of the game in soccer: Detection of T-patterns. _European Journal of Sport Science_ , 12(3):216–224, may 2012. ISSN 17461391. doi: 10.1080/17461391.2011.566362. 

- [16] Catapult Sports Ltd. Catapult USA - Wearable Technology for Elite Sports, 2015. URL `http://www.catapultsports.com/` . 

- [17] Daniel Cervone, Alex D’Amour, Luke Bornn, and Kirk Goldsberry. A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes. _CoRR_ , 1(1):1–30, aug 2014. 

- [18] Yu-Han Chang, Rajiv Maheswaran, Jeff Su, Sheldon Kwok, Tal Levy, Adam Wexler, and Kevin Squire. Quantifying Shot Quality in the NBA. In _Proc. 8th Annual MIT Sloan Sports Analytics Conference_ , pages 1–8, Boston, MA, feb 2014. MIT. URL `http://www.sloansportsconference.com/?p= 13588` . 

- [19] ChyronHego Corporation. Tracab Player Tracking System, 2015. URL `http://chyronhego.com/sports-data/player-tracking` . 

- [20] Paolo Cintia, Fosca Giannotti, Luca Pappalardo, Dino Pedreschi, and Marco Malvaldi. The harsh rule of the goals : data-driven performance indicators for football teams. In _2015 IEEE International Conference on Data Science and Advanced Analytics (DSAA)_ , pages 1–10, Paris, oct 2015. IEEE. ISBN 9781467382731. doi: 10.1109/DSAA.2015. 7344823. URL `http://ieeexplore.ieee.org/lpdocs/epic03/wrapper. htm?arnumber=7344823` . 

35 

- [21] Filipe Manuel Clemente, Micael Santos Couceiro, Fernando Manuel Louren¸co Martins, and Rui Sousa Mendes. Using network metrics to investigate football team players’ connections: A pilot study. _Motriz: Revista de Educa¸c˜ao F´ısica_ , 20(3):262–271, sep 2014. ISSN 1980-6574. doi: 10.1590/S1980-65742014000300004. 

- [22] Filipe Manuel Clemente, Fernando Manuel Louren¸co Martins, Micael Santos Couceiro, Rui Sousa Mendes, and Ant´onio Jos´e Figueiredo. Inspecting teammates coverage during attacking plays in a football game : A case study. _International Journal of Performance Analysis in Sport_ , 14(2):384– 400, 2014. ISSN 14748185. 

- [23] Filipe Manuel Clemente, Micael Santos Couceiro, Fernando Manuel Louren¸co Martins, and Rui Sousa Mendes. Using Network Metrics in Soccer: A Macro-Analysis. _Journal of Human Kinetics_ , 45 (March):123–134, 2015. ISSN 1640-5544. doi: 10.1515/hukin-2015-0013. 

- [24] Filipe Manuel Clemente, Frutuoso Silva, Fernando Manuel Louren¸co Martins, Dimitris Kalamaras, and Rui Sousa Mendes. Performance Analysis Tool for network analysis on team sports: A case study of FIFA Soccer World Cup 2014. _Proceedings of the Institution of Mechanical Engineers, Part P: Journal of Sports Engineering and Technology_ , 229(3): 1–13, jul 2015. ISSN 1754-3371. doi: 10.1177/1754337115597335. URL `http://pip.sagepub.com/lookup/doi/10.1177/1754337115597335` . 

- [25] Carlos Cotta, Antonio M. Mora, Juan Juli´an Merelo, and Cecilia MereloMolina. A network analysis of the 2010 FIFA World Cup champion team play. _Journal of Systems Science and Complexity_ , 26:21–42, 2013. ISSN 10096124. doi: 10.1007/s11424-013-2291-2. 

- [26] Arthur P. Dempster, Nan M. Laird, and Donald B. Rubin. Maximum Likelihood from Incomplete Data via the EM Algorithm. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 39(1):1–38, 1977. ISSN 00359246. URL `http://www.jstor.org/stable/2984875` . 

- [27] Jordi Duch, Joshua S. Waitzman, and Lu´ıs A. Nunes Amaral. Quantifying the Performance of Individual Players in a Team Activity. _PLoS ONE_ , 5 (6):e10937, jun 2010. ISSN 1932-6203. doi: 10.1371/journal.pone.0010937. URL `http://dx.plos.org/10.1371/journal.pone.0010937` . 

- [28] Jennifer H Fewell, Dieter Armbruster, John Ingraham, Alexander Petersen, and James S Waters. Basketball Teams as Strategic Networks. _PLoS ONE_ , 7 (11):e47445, nov 2012. ISSN 1932-6203. doi: 10.1371/journal.pone.0047445. URL `http://dx.plos.org/10.1371/journal.pone.0047445` . 

- [29] Sofia Fonseca, Jo˜ao Milho, Bruno Travassos, and Duarte Ara´ujo. Spatial dynamics of team sports exposed by Voronoi diagrams. _Human Movement Science_ , 31(6):1652–1659, 2012. ISSN 01679457. doi: 10.1016/j.humov.2012. 04.006. URL `http://dx.doi.org/10.1016/j.humov.2012.04.006` . 

- [30] Steven Fortune. A Sweepline Algorithm for Voronoi Diagrams. _Algorithmica_ , 2:153–174, 1987. doi: 10.1007/BF01840357. URL `http://dx.doi. org/10.1007/BF01840357` . 

- [31] Alexander Franks, Andrew Miller, Luke Bornn, and Kirk Goldsberry. Characterizing the spatial structure of defensive skill in professional basket- 

36 

ball. _The Annals of Applied Statistics_ , 9(1):94–121, mar 2015. ISSN 1932-6157. doi: 10.1214/14-AOAS799. URL `http://projecteuclid.org/ euclid.aoas/1430226086` . 

- [32] Ian M. Franks and Gary Miller. Eyewitness testimony in sport. _Journal of sport behavior_ , 9(1):38–45, 1986. ISSN 0162-7341. 

- [33] Linton C. Freeman. A Set of Measures of Centrality Based on Betweenness. _Sociometry_ , 40(1):35–41, mar 1977. ISSN 00380431. doi: 10.2307/3033543. URL `http://www.jstor.org/stable/3033543?origin=crossref` . 

- [34] Linton C. Freeman. Centrality in social networks conceptual clarification. _Social Networks_ , 1(3):215–239, jan 1978. ISSN 03788733. doi: 10.1016/ 0378-8733(78)90021-7. 

- [35] Wouter Frencken, Koen Lemmink, Nico Delleman, and Chris Visscher. Oscillations of centroid position and surface area of soccer teams in small-sided games. _European Journal of Sport Science_ , 11(4):215–223, jul 2011. ISSN 1746-1391. doi: 10.1080/17461391.2010.499967. 

- [36] Akira Fujimura and Kokichi Sugihara. Geometric analysis and quantitative evaluation of sport teamwork. _Systems and Computers in Japan_ , 36(6): 49–58, 2005. ISSN 0882-1666. doi: 10.1002/scj.20254. URL `http://doi. wiley.com/10.1002/scj.20254` . 

- [37] Kirk Goldsberry. Courtvision: New visual and spatial analytics for the NBA. In _Proc. 6th Annual MIT Sloan Sports Analytics Conference_ , pages 1–7, Boston, MA, mar 2012. MIT. URL `http://www.sloansportsconference.com/wp-content/uploads/2012/ 02/Goldsberry_Sloan_Submission.pdf` . 

- [38] Kirk Goldsberry and Eric Weiss. The Dwight Effect : A New Ensemble of Interior Defense Analytics for the NBA. In _Proc. 7th Annual MIT Sloan Sports Analytics Conference_ , pages 1–11, Boston, MA, feb 2013. MIT. 

- [39] Peter Gould and Anthony Gatrell. A structural Analysis of a Game: The Liverpool v Manchester United Cup Final of 1977. _Social Networks_ , 2(3):253–273, jan 1979. ISSN 03788733. doi: 10. 1016/0378-8733(79)90017-0. URL `http://linkinghub.elsevier.com/ retrieve/pii/0378873379900170` . 

- [40] Thomas U. Grund. Network structure and team performance: The case of English Premier League soccer teams. _Social Networks_ , 34(4):682–690, 2012. ISSN 03788733. doi: 10.1016/j.socnet.2012.08.004. URL `http://dx. doi.org/10.1016/j.socnet.2012.08.004` . 

- [41] Joachim Gudmundsson and Thomas Wolle. Football analysis using spatiotemporal tools. _Computers, Environment and Urban Systems_ , 47:16–27, 2014. ISSN 01989715. doi: 10.1016/j.compenvurbsys.2013.09.004. URL `http://dx.doi.org/10.1016/j.compenvurbsys.2013.09.004` . 

- [42] Hermann Haken, J. A. Scott Kelso, and H. Bunz. A theoretical model of phase transitions in human hand movements. _Biological Cybernetics_ , 51 (5):347–356, feb 1985. ISSN 0340-1200. doi: 10.1007/BF00336922. URL `http://link.springer.com/10.1007/BF00336922` . 

- [43] Michael Horton, Joachim Gudmundsson, Sanjay Chawla, and Jo¨el Estephan. Automated Classification of Passing in Football. In _Proc. Ad-_ 

37 

_vances in Knowledge Discovery and Data Mining - 19th Pacific-Asia Conference, PAKDD 2015, Part II_ , volume 9078 of _Lecture Notes in Computer Science_ , pages 319–330, Ho Chi Minh City, may 2015. Springer. doi: 10.1007/978-3-319-18032-8 ~~2~~ 5. URL `http://dx.doi.org/10.1007/ 978-3-319-18032-8_25` . 

- [44] Impire AG. Impire AG, 2015. URL `http://www.bundesliga-datenbank. de/en/products/` . 

- [45] Stephen S Intille and Aaron F Bobick. A Framework for Recognizing Multi-agent Action from Visual Evidence. In _Proceedings of the Sixteenth National Conference on Artificial Intelligence and the Eleventh Innovative Applications of Artificial Intelligence Conference Innovative Applications of Artificial Intelligence_ , number 489, pages 518–525, Orlando, FL, jul 1999. American Association for Artificial Intelligence. ISBN 0-262-51106-1. URL `http://dl.acm.org/citation.cfm?id=315149.315381` . 

- [46] Kihwan Kim, Matthias Grundmann, Ariel Shamir, Iain Matthews, Jessica Hodgins, and Irfan Essa. Motion fields to predict play evolution in dynamic sport scenes. In _2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition_ , pages 840–847, San Francisco, CA, jun 2010. IEEE. ISBN 978-1-4244-6984-0. doi: 10.1109/CVPR.2010. 5540128. URL `http://ieeexplore.ieee.org/lpdocs/epic03/wrapper. htm?arnumber=5540128` . 

- [47] Hiroaki Kitano, Minoru Asada, Yasuo Kuniyoshi, Itsuki Noda, and Eiichi Osawa. RoboCup. In _Proceedings of the first international conference on Autonomous agents - AGENTS ’97_ , pages 340–347, New York, NY, feb 1997. ACM Press. ISBN 0897918770. doi: 10.1145/267658.267738. URL `http://portal.acm.org/citation.cfm?doid=267658.267738` . 

- [48] Justin Kubatko, Dean Oliver, Kevin Pelton, and Dan T. Rosenbaum. A Starting Point for Analyzing Basketball Statistics. _Journal of Quantitative Analysis in Sports_ , 3(3):1–22, jan 2007. ISSN 1559-0410. doi: 10.2202/ 1559-0410.1070. URL `http://www.degruyter.com/view/j/jqas.2007.3. 3/jqas.2007.3.3.1070/jqas.2007.3.3.1070.xml` . 

- [49] Harold W. Kuhn. The Hungarian method for the assignment problem. _Naval Research Logistics Quarterly_ , 2(1-2):83–97, mar 1955. ISSN 00281441. doi: 10.1002/nav.3800020109. URL `http://doi.wiley.com/10.1002/nav. 3800020109` . 

- [50] Ruonan Li and Rama Chellappa. Group motion segmentation using a Spatio-Temporal Driving Force Model. In _2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition_ , pages 2038– 2045, San Francisco, CA, jun 2010. IEEE. ISBN 978-1-4244-6984-0. doi: 10.1109/CVPR.2010.5539880. URL `http://ieeexplore.ieee.org/ lpdocs/epic03/wrapper.htm?arnumber=5539880` . 

- [51] Ruonan Li, Rama Chellappa, and Shaohua Kevin Zhou. Learning multimodal densities on Discriminative Temporal Interaction Manifold for group activity recognition. In _2009 IEEE Conference on Computer Vision and Pattern Recognition_ , pages 2450–2457, Miami, FL, jun 2009. IEEE. doi: 10. 

38 

1109/CVPR.2009.5206676. URL `http://ieeexplore.ieee.org/lpdocs/ epic03/wrapper.htm?arnumber=5206676` . 

- [52] Patrick Lucey, Alina Bialkowski, G. Peter K. Carr, Eric Foote, and Iain Matthews. Characterizing Multi-Agent Team Behavior from Partial Team Tracings: Evidence from the English Premier League. In _Proceedings of the Twenty-Sixth AAAI Conference on Artificial Intelligence_ , pages 1–7, Toronto, jul 2012. AAAI Press. URL `http://www.aaai.org/ocs/index. php/AAAI/AAAI12/paper/view/5004` . 

- [53] Patrick Lucey, Alina Bialkowski, G. Peter K. Carr, Stuart Morgan, Iain Matthews, and Yaser Sheikh. Representing and Discovering Adversarial Team Behaviors Using Player Roles. In _Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR’13)_ , pages 2706–2713, Portland, OR, jun 2013. IEEE. doi: 10.1109/CVPR.2013.349. URL `http: //dx.doi.org/10.1109/CVPR.2013.349` . 

- [54] Patrick Lucey, Alina Bialkowski, G. Peter K. Carr, Yisong Yue, and Iain Matthews. How to Get an Open Shot: Analyzing Team Movement in Basketball using Tracking Data. In _Proc. 8th Annual MIT Sloan Sports Analytics Conference Conference_ , pages 1–10, Boston, MA, feb 2014. MIT. 

- [55] Patrick Lucey, Alina Bialkowski, Mathew Monfort, Peter Carr, and Iain Matthews. ”Quality vs Quantity”: Improved Shot Prediction in Soccer using Strategic Features from Spatiotemporal Data. In _Proc. 8th Annual MIT Sloan Sports Analytics Conference_ , pages 1–9, Boston, MA, feb 2014. MIT. URL `http://www.sloansportsconference.com/?p=15790` . 

- [56] Rajiv Maheswaran, Yu-Han Chang, Aaron Henehan, and Samantha Danesis. Deconstructing the rebound with optical tracking data. In _Proc. 6th Annual MIT Sloan Sports Analytics Conference_ , pages 1–7, Boston, MA, USA, feb 2012. MIT. URL `http://www.sloansportsconference.com/?p=6143` . 

- [57] Rajiv Maheswaran, Yu-Han Chang, Jeff Su, Sheldon Kwok, Tal Levy, Adam Wexler, and Noel Hollingsworth. The three dimensions of rebounding. In _Proc. 8th Annual MIT Sloan Sports Analytics Conference_ , pages 1–7, Boston, MA, USA, feb 2014. MIT. URL `http://www. sloansportsconference.com/?p=13011` . 

- [58] Andrew Miller, Luke Bornn, Ryan P Adams, and Kirk Goldsberry. Factorized Point Process Intensities: A Spatial Analysis of Professional Basketball. In _Proc. 31th International Conference on Machine Learning, (ICML’2014)_ , pages 235–243, Beijing, jun 2014. JMLR.org. URL `http: //jmlr.org/proceedings/papers/v32/miller14.html` . 

- [59] Ryota Nakanishi, Junya Maeno, Kazuhito Murakami, and Tadashi Naruse. An Approximate Computation of the Dominant Region Diagram for the Real-Time Analysis of Group Behaviors. In _Proc. 13th Annual RoboCup International Symposium_ , pages 228–239, Graz, Austria, jun 2009. Springer. doi: 10.1007/978-3-642-11876-0 ~~2~~ 0. URL `http://dx.doi.org/10.1007/ 978-3-642-11876-0_20` . 

- [60] Takuma Narizuka, Ken Yamamoto, and Yoshihiro Yamazaki. Statistical properties of position-dependent ball-passing networks in football games. _Physica A: Statistical Mechanics and its Applications_ , 412:157–168, oct 

39 

   2014. ISSN 03784371. doi: 10.1016/j.physa.2014.06.037. URL `http: //linkinghub.elsevier.com/retrieve/pii/S0378437114005123` . 

- [61] NBA Media Ventures LLC. NBA Stats, 2014. URL `http://stats.nba. com/featured/whole_new_view_2013_10_29.html` . 

- [62] Mark E. J. Newman. _Networks: An introduction_ . Oxford University Press, New York, NY, mar 2010. ISBN 9780199206650. 

- [63] Opta Sports Ltd. Opta Live Performance Data, 2015. URL `http://www. optasports.com/about/what-we-do/live-performance-data.aspx` . 

- [64] Pedro Passos, Keith Davids, Duarte Ara´ujo, N Paz, J. Mingu´ens, and J. Mendes. Networks as a novel tool for studying team ball sports as complex social systems. _Journal of Science and Medicine in Sport_ , 14(2): 170–176, mar 2011. ISSN 14402440. doi: 10.1016/j.jsams.2010.10.459. URL `http://linkinghub.elsevier.com/retrieve/pii/S1440244010006602` . 

- [65] Javier Lopez Pe˜na and Hugo Touchette. A network theory analysis of football strategies. In _Proc. 2012 Euromech Physics of Sports Conference_ , pages 517–528, Paris, apr 2012. LEditions<sup>´</sup> de l’Ecole<sup>´</sup> Polytechnique. URL `http://arxiv.org/abs/1206.6904` . 

- [66] Charles Perin, Romain Vuillemot, and Jean-Daniel Fekete. SoccerStories: A Kick-off for Visual Soccer Analysis. _IEEE Transactions on Visualization and Computer Graphics_ , 19(12):2506–2515, 2013. doi: 10.1109/TVCG.2013. 192. URL `http://dx.doi.org/10.1109/TVCG.2013.192` . 

- [67] Matej Perˇse, Matej Kristan, Stanislav Kovaˇciˇc, Goran Vuˇckoviˇc, and Janez Perˇs. A trajectory-based analysis of coordinated team activity in a basketball game. _Computer Vision and Image Understanding_ , 113(5):612– 621, may 2009. ISSN 10773142. doi: 10.1016/j.cviu.2008.03.001. URL `http://linkinghub.elsevier.com/retrieve/pii/S1077314208000465` . 

- [68] Hannah Pileggi, Charles D. Stolper, J. Michael Boyle, and John T. Stasko. SnapShot: Visualization to Propel Ice Hockey Analytics. _IEEE Transactions on Visualization and Computer Graphics_ , 18(12):2819–2828, dec 2012. ISSN 1077-2626. doi: 10.1109/TVCG.2012.263. URL `http://ieeexplore.ieee. org/lpdocs/epic03/wrapper.htm?arnumber=6327288` . 

- [69] Prozone Sports Ltd. Prozone Sports - Our technology, 2015. URL `http: //prozonesports.stats.com/about/technology/` . 

- [70] Charles Reep and Bernard Benjamin. Skill and Chance in Association Football. _Journal of the Royal Statistical Society. Series A (General)_ , 131 (4):581–585, 1968. ISSN 00359238. doi: 10.2307/2343726. URL `http: //www.jstor.org/stable/2343726?origin=crossref` . 

- [71] Brian J. Reich, James S. Hodges, Bradley P. Carlin, and Adam M. Reich. A Spatial Analysis of Basketball Shot Chart Data. _The American Statistician_ , 60(1):3–12, feb 2006. ISSN 0003-1305. doi: 10.1198/000313006X90305. URL `http://www.tandfonline.com/doi/abs/10.1198/000313006X90305` . 

- [72] Wulf Rossmann. _Lie Groups: An Introduction Through Linear Groups_ . Oxford University Press, Oxford, 2002. ISBN 0199202516. URL `https: //books.google.com/books?hl=en&lr=&id=EjDazZvcquwC&pgis=1` . 

- [73] Claude E Shannon. A mathematical theory of communication. _ACM SIGMOBILE Mobile Computing and Communications Review_ , 5(1):3–55, 

40 

jan 2001. ISSN 15591662. doi: 10.1145/584091.584093. URL `http: //portal.acm.org/citation.cfm?doid=584091.584093` . 

- [74] Ashton Shortridge, Kirk Goldsberry, and Matthew Adams. Creating space to shoot: quantifying spatial relative field goal efficiency in basketball. _Journal of Quantitative Analysis in Sports_ , 10(3):303–313, jan 2014. ISSN 15590410. doi: 10.1515/jqas-2013-0094. URL `http://www.degruyter.com/ view/j/jqas.2014.10.issue-3/jqas-2013-0094/jqas-2013-0094.xml` . 

- [75] Brian Skinner. The Price of Anarchy in Basketball. _Journal of Quantitative Analysis in Sports_ , 6(1):1–16, jan 2010. ISSN 1559-0410. doi: 10.2202/ 1559-0410.1217. URL `http://www.degruyter.com/view/j/jqas.2010.6. 1/jqas.2010.6.1.1217/jqas.2010.6.1.1217.xml` . 

- [76] SportVision Inc. NHL, Sportvision test program to track players, puck, 2015. URL `http://www.sportvision.com/news/ nhl-sportvision-test-program-track-players-puck` . 

- [77] STATS LLC. SportVU Player Tracking, 2015. URL `http://www.stats. com/leagues-teams/` . 

- [78] Tsuyoshi Taki and Jun-ichi Hasegawa. Visualization of dominant region in team games and its application to teamwork analysis. In _Proceedings Computer Graphics International 2000_ , pages 227–235, Geneva, Switzerland, jun 2000. IEEE Comput. Soc. ISBN 0-7695-0643-7. doi: 10.1109/CGI.2000.852338. URL `http://ieeexplore.ieee.org/lpdocs/ epic03/wrapper.htm?arnumber=852338` . 

- [79] Tsuyoshi Taki, Jun-ichi Hasegawa, and Teruo Fukumura. Development of motion analysis system for quantitative evaluation of teamwork in soccer games. In _Proceedings of 3rd IEEE International Conference on Image Processing_ , volume 3, pages 815–818, Lausanne, sep 1996. IEEE. ISBN 0- 7803-3259-8. doi: 10.1109/ICIP.1996.560865. URL `http://ieeexplore. ieee.org/lpdocs/epic03/wrapper.htm?arnumber=560865` . 

- [80] Fumiya Ueda, Honda Masaaki, and Horino Hiroyuki. The Causal Relationship between Dominant Region and Offense- Defense Performance - Focusing on the Time of Ball Acquisition. _Football Science_ , 11:1–17, 2014. 

- [81] Jan Van Haaren, Vladimir Dzyuba, Siebe Hannosset, and Jesse Davis. Automatically Discovering Offensive Patterns in Soccer Match Data. In _Advances in Intelligent Data Analysis XIV - 14th International Symposium, IDA 2015_ , volume 9385 of _Lecture Notes in Computer Science_ , pages 286– 297, Saint Etienne, oct 2015. Springer. doi: 10.1007/978-3-319-24465-5 ~~2~~ 5. URL `http://link.springer.com/10.1007/978-3-319-24465-5_25` . 

- [82] Richard von Mises and Hilda Pollaczek-Geiringer. Praktische Verfahren der Gleichungsaufl¨osung . _ZAMM - Journal of Applied Mathematics and Mechanics / Zeitschrift f¨ur Angewandte Mathematik und Mechanik_ , 9(2): 152–164, 1929. ISSN 1521-4001. doi: 10.1002/zamm.19290090206. URL `http://dx.doi.org/10.1002/zamm.19290090206` . 

- [83] Qing Wang, Hengshu Zhu, Wei Hu, Zhiyong Shen, and Yuan Yao. Discerning Tactical Patterns for Professional Soccer Teams. In _Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining - KDD ’15_ , pages 2197–2206, Sydney, aug 2015. ACM Press. ISBN 

41 

9781450336642. doi: 10.1145/2783258.2788577. URL `http://dl.acm.org/ citation.cfm?doid=2783258.2788577` . 

- [84] Stanley Wasserman and Katherine Faust. _Social network analysis: Methods and applications. Structural analysis in the social sciences._ Cambridge University Press, Cambridge, 1997. ISBN 0521382696. 

- [85] Xinyu Wei, Long Sha, Patrick Lucey, Stuart Morgan, and Sridha Sridharan. Large-Scale Analysis of Formations in Soccer. In _2013 International Conference on Digital Image Computing: Techniques and Applications (DICTA)_ , pages 1–8, Hobart, nov 2013. IEEE. ISBN 978-1-4799-21263. doi: 10.1109/DICTA.2013.6691503. URL `http://ieeexplore.ieee. org/lpdocs/epic03/wrapper.htm?arnumber=6691503` . 

- [86] Xinyu Wei, Patrick Lucey, Stephen Vidas, Stuart Morgan, and Sridha Sridharan. Forecasting Events Using an Augmented Hidden Conditional Random Field. In _Proc. 12th Asian Conference on Computer Vision_ , volume 9006 of _Lecture Notes in Computer Science_ , pages 569–582. Springer International Publishing, Cham, nov 2015. ISBN 978-3-319-16816-6. doi: 10. 1007/978-3-319-16817-3 ~~3~~ 7. URL `http://link.springer.com/10.1007/ 978-3-319-16817-3_37` . 

- [87] Peter Weiner. Linear pattern matching algorithms. In _14th Annual Symposium on Switching and Automata Theory (SWAT 1973)_ , pages 1–11, Iowa City, IA, oct 1973. IEEE. doi: 10.1109/SWAT.1973. 13. URL `http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm? arnumber=4569722` . 

- [88] Jenna Wiens, Guha Balakrishnan, Joel Brooks, and John Guttag. To Crash or Not To Crash: A Quantitative Look at the Relationship Between Offensive Rebounding and Transition Defense in the NBA. In _Proc. 6th Annual MIT Sloan Sports Analytics Conference_ , pages 1–7, Boston, mar 2013. MIT. 

- [89] Yisong Yue, Patrick Lucey, Peter Carr, Alina Bialkowski, and Iain Matthews. Learning Fine-Grained Spatial Models for Dynamic Sports Play Prediction. In _2014 IEEE International Conference on Data Mining_ , pages 670–679, Shenzen, dec 2014. IEEE. ISBN 978-1-4799-43029. doi: 10.1109/ICDM.2014.106. URL `http://ieeexplore.ieee.org/ lpdocs/epic03/wrapper.htm?arnumber=7023384` . 

42 


