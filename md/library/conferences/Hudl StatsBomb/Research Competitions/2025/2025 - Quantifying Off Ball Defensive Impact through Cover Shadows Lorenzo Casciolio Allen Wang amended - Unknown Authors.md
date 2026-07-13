<!-- source: library/conferences/Hudl StatsBomb/Research Competitions/2025/2025 - Quantifying Off Ball Defensive Impact through Cover Shadows Lorenzo Casciolio Allen Wang amended - Unknown Authors.pdf -->



# **Quantifying Off-Ball Defensive Impact through Cover Shadows** 

Lorenzo Cascioli<sup>1,</sup> ∗ _,_ Allen Wang<sup>1,</sup> ∗, Luca Stradiotti<sup>1</sup> , Maaike Van Roy<sup>1</sup> , Pieter Robberechts<sup>1</sup> , Maxim Wouters<sup>2</sup> , Arne Jaspers<sup>1,2</sup> and Jesse Davis<sup>1</sup> 

_1  KU Leuven, Dept. of Computer Science; Leuven.AI, B-3000 Leuven, Belgium 2  Royal Belgian Football Association, RBFA Knowledge Centre, B-1480 Tubize, Belgium_ 

- ∗ _These authors contributed equally._ 

## **Introduction** 

Defensive contributions in soccer often occur without the ball and are poorly captured by traditional metrics. In fact, Wu and Swartz [1] observe that players typically have possession for less than three minutes per match. Yet, almost all of the widely reported metrics are based on actions involving the ball. In practice, a defender might merely block an opponent’s passing lane: such a move might prevent a valuable pass that is never realized and hence, never recorded. These off-ball actions, often referred to as “cover shadows”, are crucial to a team’s defense but have received little analytical attention. 

Existing defensive metrics fail to capture this positional aspect of defending. Conventional stats (tackles, interceptions, clearances) only record events where the ball is won or play is interrupted, ignoring instances where defenders merely steer attackers into less dangerous options. More sophisticated frameworks (i.e., expected disruption models)  [2],  [3] , aim to value off-ball defensive actions by attributing changes in a team’s typical playing style or offensive efficiency to the defensive behavior of opponents. However, these approaches mainly consider man-marking actions and primarily attribute their impact at the team level. In short, no existing approach explicitly quantifies the impact of a defender obstructing an opponent’s passing lane. 

Recent data advances make new analyses possible. StatsBomb 360 data (launched in 2021) provides the locations of all players surrounding each event, effectively combining traditional event logs with tracking-like spatial context. This “contextual” event dataset provides the kind of context needed to evaluate defensive positioning. By leveraging these positional snapshots, one can identify when a defender’s placement cuts off a passing lane and model how much the opponent’s attack is thereby disrupted. 

In this paper, we propose a novel data-driven approach to quantify the effect of blocking passing lanes in soccer. First, we determine whether a player blocks a passing lane. Naively, this means checking if the player is on an imaginary line between the ball and a potential receiver. In practice, however, the ability to intercept also depends on factors beyond positioning such as reaction time, ball speed, and trajectory. To capture this, we propose a physics-based model that estimates the 

**1** 



probability of a player blocking a pass at any location by incorporating time to intercept (cf. pitch control) and an approximation of the ball's travel time given the target location of a potential pass. 

Second, we measure how effectively a defending team is blocking passing lanes.  We start by quantifying the threat of the attacking team in a game snapshot. To do so, we sum the threat of all potential passes, weighting each pass by its likelihood of completion. We then create a counterfactual scenario by removing (one or more) defenders that are casting a cover shadow, and re-take the threat of this alternative game state. The difference in threat serves as a measure of cover shadows effectiveness. We show how this metric can be used in practice to analyze defensive contributions at both the player and team levels,  thereby identifying those who excel or underperform in the use of cover shadows. 

Finally, we assess if and how a team can improve their ability to block passing lanes. To do so, we cast defensive positioning as an optimization problem. The objective is to identify the optimal allocation of defenders to passing lanes so that the most dangerous attackers are blocked. 

In short, this work makes three key contributions: 

- **RQ1** : We provide a more accurate analytical method for identifying when defenders obstruct a passing lane. 

- **RQ2** : We provide a novel metric for measuring the cover-shadow effectiveness of players and teams. Our metric rates how defenders’ positioning influences the likelihood of opponents playing valuable passes. 

- **RQ3** : We introduce a novel approach for optimizing defensive positioning that enables quantifying how small positional adjustments in a team’s collective shape can reduce the attacking threat by blocking access to progressive passing lanes. 

## **Data and Definitions** 

### **Dataset Overview** 

Our work builds on StatsBomb 360 event stream data, which augments the conventional human-annotated event logs with spatiotemporal snapshots extracted from broadcast video. Each event record includes the standard event metadata (i.e., event type, timestamp, player, team, bodypart, outcome, and pitch coordinates)  along with a “freeze frame” capturing the positions of the players (where visible in the broadcast video) at the moment of the event, along with their relationship to the ball carrier (i.e., teammate or opponent).  Because freeze frames occur at the moment of the ball-related action, they do not represent continuous player movement. 

Our main dataset comprises 1,752 matches from the Big 5 European leagues during the 2024/25 season. We use the data from the Bundesliga, Premier League, LaLiga and Ligue 1 to train models and select hyperparameters. Serie A data is reserved to evaluate the models and develop the use cases. Since the StatsBomb 360 freeze frame data does not provide the identity of players, we complement this evaluation dataset with one match of the 2020 European Championship (Belgium 

**2** 



vs Portugal). For this match, we enriched the 360 snapshots with player IDs gathered from tracking data provided by the RBFA. The tracking data and StatsBomb 360 event stream data were first synchronized using ETSY [4] . Afterward, the player identities in each freeze frame were determined using a shortest-distance approach. This combined dataset will allow us to study defensive behavior at both the player and team level. 

To standardize and facilitate analysis, we employ the SPADL<sup>1</sup> representation of the events and transform the player coordinates in the freeze frames into the 105 x 68 meters standardized pitch coordinate system. We exclude passes where the origin or the destination falls outside of the visible area, as we might be missing essential context. 

### **Defining a (Blocked) Passing Lane** 

To analyze pass blocking, we select all snapshots associated with a pass in the attacking half where the ball carrier had at least one viable progressive passing option. We exclude set pieces, high or aerial passes, and passes made with body parts other than the foot. Passes that occur inside the penalty area are also removed. This process results in 67,426 snapshots from the Serie A season and 224 snapshots from the Belgium–Portugal match. Each snapshot provides the positions of players visible in the frame (not all 22 players) including: 

- The ball carrier 𝑝 𝑎 

- All visible potential receivers 𝑅 = {𝑟1, 𝑟2, ..., 𝑟𝑛}, and 

- All visible defenders  𝐷 = {𝑑1, 𝑑2, ..., 𝑑𝑛} 

For each potential pass {𝑝𝑎, 𝑟𝑖} in the frame, we compute whether the passing lane is open or blocked given the positions of . Therefore, we define a passing lane as the direct, straight-line 𝐷 corridor between the ball carrier and a potential receiver. Formally, the lane 𝐿(𝑝 , 𝑟 ) is represented 𝑎 𝑖 by the segment connecting their positions. A lane is considered blocked if any defender 𝑑 ∈𝐷 is 𝑗 positioned such that they could realistically intercept the ball if the pass was attempted. We operationalize this definition in RQ1. 

### **Identifying Lane-Blocking Players** 

Not all defenders contribute equally to blocking passing lanes. We distinguish between two primary defensive roles: man-marking defenders and lane-blocking defenders. 

- **Man-marking defenders** closely follow an attacker and are not really concerned with blocking passing lanes. 

> 1 SPADL unifies existing event stream formats into a common language. It provides a tabular representation in which each on-the-ball action is described by the same set of twelve attributes. For more info, see <u>https://github.com/ML-KULeuven/socceraction.</u> 

**3** 



- **Lane-blocking defenders** , in contrast, occupy the empty space between the ball carrier and one or more potential receivers to discourage dangerous passes. 

Operationally, we classify as man-markers all defenders that are positioned within a 3m radius centered 1m behind an attacking player, to account for the typical marking position where the defender stays close to the attacker between the latter and the goal. Defenders outside this marking zone are treated as potential lane-blocking defenders. In this work, we focus specifically on the contribution of these lane-blocking defenders. 

## **RQ1: Is a player blocking a passing lane?** 

In previous work, quantifying whether a defender blocks a pass has been approached with several geometric approaches [5], [6], [7]. For example, the most common approach involves drawing a fictional cone extending from the passer to the receiver. A pass is then considered to be blocked if a defender is positioned within the cone. These geometric approaches provide a useful starting point for assessing blocked passes, but they overlook that players are already in motion before the pass is played and that several uncertain or unobserved factors (such as reaction time) render passing-lane obstruction a probabilistic event. Therefore, we introduce _Lane Control_ , a novel physics-based pass block model. 

### **Baseline Pass Block Models** 

We first define three geometric baseline models for evaluating if a pass is blocked. Figure 1 provides a graphical illustration of each approach. 

First, the **Line Corridor** baseline assumes the passing lane to be a rectangle 𝑅 (𝑝 , 𝑟 ) of fixed 𝑤 𝑎 𝑖 width 𝑤, centered on the segment connecting the ball carrier 𝑝 and receiver : 𝑟 𝑎 𝑖 

2 𝑅𝑤(𝑝𝑎, 𝑟𝑖) = { 𝑥∈ℜ | 𝑝𝑒𝑟𝑝_𝑑𝑖𝑠𝑡(𝑥, 𝐿(𝑝𝑎, 𝑟𝑖)) < 𝑤/2} , 

where 𝑝𝑒𝑟𝑝_𝑑𝑖𝑠𝑡(𝑥, 𝐿(𝑝 , 𝑟 )) represent the perpendicular distance from a point  to the line 𝑥 𝑎 𝑖 segment 𝐿(𝑝 , 𝑟 ) . A pass is considered blocked if any defender’s position falls within this corridor: 𝑎 𝑖 ∃𝑑 ∈ 𝐷 : 𝑑 ∈𝑅 (𝑝 , 𝑟 ). 𝑗 𝑗 𝑤 𝑎 𝑖 We empirically obtained the best results for 𝑤= 2 meters. 

Second, the **Cone Corridor** baseline expands the passing corridor to a cone with vertex at the ball carrier and base at the receiver. The cone width at the receiver scales proportionally with the pass length: 𝑤 = 𝑘 * || 𝑟 − 𝑝 || where  is a scaling constant and 𝑘 || 𝑟 − 𝑝 || is the Euclidean 𝑖 𝑎 𝑖 𝑎 distance between  and 𝑟 𝑝 .  Let 𝑇 (𝑝 , 𝑟 ) represent the cone triangle with vertex at 𝑝 , base at  𝑟 , 𝑖 𝑎 𝑘 𝑎 𝑖 𝑎 𝑖 and width scaling constant .  A pass is blocked if any defender lies within the cone: 𝑘 ∃𝑑 ∈ 𝐷 : 𝑑 ∈ 𝑇 (𝑝 , 𝑟 ). 𝑗 𝑗 𝑘 𝑎 𝑖 

In our experiments, we set  = 0.2 so the cone width is 2 meters for a 10 meter pass. 𝑘 

**4** 



Finally, the **Gaussian Cone** baseline incorporates positional uncertainty about the defenders. Each defender is represented as an isotropic 2D Gaussian [8] 𝑁(µ , Σ ) centered on their recorded 𝑗 𝑗 

2 position µ = (𝑥 , 𝑦 ) with covariance  Σ = σ 𝐼. For a pass from 𝑝 to  , each defender is projected 𝑟 𝑗 𝑗 𝑗 𝑗 𝑎 𝑖 onto the pass center line; at that location, we take the cone’s perpendicular cross section and compute the normalized Gaussian mass of the defender within the cross-section  (the blocking fraction 𝐹 ). A pass is considered blocked if any defender’s blocking fraction 𝐹 exceeds a σ σ threshold : τ 

∃𝑑 ∈𝐷 : 𝐹 (𝑝 , 𝑟 , 𝑑 ) ≥τ 𝑗 σ 𝑎 𝑖 𝑗 

All mathematical details and derivations of 𝐹 are provided in Appendix A. We use σ = 1 for 1m<sup>2</sup> σ variance, τ = 0. 5 for the threshold, and the same  = 0.2 so the cone width is 2 meters for a 10 𝑘 meter pass. 



**Figure 1:** Sample illustration of blocked/open pass options in a game state with Line Corridor, Cone Corridor, and Gaussian Cone baselines. Green passes are marked as open, red passes are marked as blocked. Note that when considering the attacker closest to the attacking penalty box, the two closest defenders are both slightly outside of the line and the cone, as shown for the first two baselines. In this case, the Gaussian Cone still marks the passing lane as blocked due to the influence of the defender positioned earlier on the passing lane. The second defender is still ignored, as he is positioned right below the attacker, therefore he does not generate any valid cross section. 

Because of their static assumptions, these baselines ignore how the movement of players and the ball shapes passing outcomes . They can identify whether a defender is geometrically positioned to block a pass, but not how players’ initial speeds, their timing, or the ball’s velocity influence the likelihood of interception. 

**5** 



### **Our solution: Lane Control** 

To address the limitations of the geometric baseline approaches, we introduce Lane Control, a physics-based model inspired by pitch control [9], [10], and pressing intensity [11]. In short, Lane Control evaluates the probability that a pass will be intercepted by computing the 

time-to-intercept (TTI) for the ball, attacking players, and defenders at a set of discrete locations describing the passing lane. Specifically, it consists of three subsequent steps: corridor parameterization, TTI estimation, and probability conversion. 

### _Corridor Parameterization_ 

First, Lane Control parameterizes the passing corridor into three lines, analogous to the previously defined passing cones: a center line corresponding to the shortest straight-line distance from the passer to the receiver; and a left and right line along the edges of the passing cone, ending at the two sides of the receiver. Concretely, each line is sampled at 30 target points from the passer to the receiver. 

### _TTI Estimation_ 

Having computed a discrete set of locations along the passing lane, we compute the TTI for the ball, all defenders 𝐷, and all attackers 𝑅 to each of these locations. This is simply the estimated time that it takes the ball/player to get to that point, given the current velocity and constants describing the motion. 

- **Ball Time:** To model the ball’s time, we follow Spearman’s approach [9] for ball motion under quadratic drag, ignoring gravity and Magnus force while assuming a constant drag coefficient and a straight-line path. We use the same constants as the original model: air density ( =1.22 kg/mσ<sup>3</sup> ), drag coefficient (𝐶 = 0.25), cross sectional area of the ball ( = 𝐴 𝐷 

- 0.038 m<sup>2</sup> ), and mass of the ball (𝑚 = 0.42 kg). We combine these into a single drag parameter 𝑘= (σ𝐶 𝐴) / (2𝑚) . Then, the time for the ball to reach a target point at distance  given 𝑑 𝑑 

- initial speed 𝑣 is defined as: 0 



In practice, the initial speed 𝑣 is often unknown or difficult to estimate. To address this, we 0 set  𝑣 to an average ball speed of 12.0 m/s as a proxy. For numerical stability when 𝑘𝑑 is 0 𝑘𝑑 small, we use the numpy function _exmp1_ to compute 𝑒 - 1. 

- **Players TTI:** For each sampled target point 𝑞 on any of the three lines and for each player 𝑘 

- 𝑝∈𝐷∪𝑅, we model the TTI with a capped accelerate-then-cruise model with reaction time. Let 𝑟 and 𝑣 be the initial position and velocity of the player. After a reaction delay of 𝑝 𝑝 

**6** 



𝑡 = 0.7 s, the player is at 𝑟 = 𝑟 + 𝑣 𝑡 .  Let 𝑑= ||𝑞 −𝑟 || be the distance 𝑟𝑒𝑎𝑐𝑡 𝑟𝑒𝑎𝑐𝑡 𝑝 𝑝 𝑟𝑒𝑎𝑐𝑡 𝑘 𝑟𝑒𝑎𝑐𝑡 from the player to the target after the reaction and _ê_ = (𝑞 −𝑟 ) / ||𝑞 −𝑟 || be the 𝑘 𝑟𝑒𝑎𝑐𝑡 𝑘 𝑟𝑒𝑎𝑐𝑡 unit vector from the player to the target. We only consider the  initial velocity component towards the target: 𝑣0 = 𝑚𝑎𝑥(0, 𝑣𝑝 · ê).  The maximum acceleration (  =7.0 m/s𝑎<sup>2</sup> ) and the maximum speed (𝑣 =12.0 m/s) are fixed for all players. Defenders only need to get within 𝑚𝑎𝑥 a block radius (𝑟 =0.7 m) of the target to block/deflect the pass, while receivers must 𝑏𝑙𝑜𝑐𝑘 reach the point exactly to properly control the ball. The effective distance is thus 𝑑 = 𝑚𝑎𝑥(𝑑−𝑟 , 0) for defenders and 𝑑 = 𝑑 for attackers.  Each player’s time to 𝑒𝑓𝑓 𝑏𝑙𝑜𝑐𝑘 𝑒𝑓𝑓 reach maximum speed during the acceleration phase is 𝑡 = (𝑣 −𝑣 ) / 𝑎  while the 𝑎𝑐𝑐𝑒𝑙 𝑚𝑎𝑥 0 distance covered during acceleration is 𝑑𝑎𝑐𝑐𝑒𝑙 = 𝑣0𝑡𝑎𝑐𝑐𝑒𝑙 +<sup>1</sup> 2 𝑎𝑡2𝑎𝑐𝑐𝑒𝑙. Adding the reaction delay, the TTI for a player is then given by the piecewise formula below: 



In other words, a player can reach the target point in one of three cases: 

- Cruising case: the player is already moving at maximum speed and simply has to react before covering the effective distance. 

- Acceleration case: the player is not already running at max speed, hence he starts accelerating and reaches the target before hitting max speed. 

- Accelerate-then-cruise case: the player accelerates, reaches max speed, and continues running at max speed before arriving at the target. 

If a player is already running at max speed, then the TTI does not consider any acceleration. If instead the player gets to the ball before reaching the max speed, then max speed cruising is not considered. Some popular physics-based implementations  do not consider the acceleration phase and simply assume that players run at max speed [12]. We found this to clearly worsen the method performance, hence we chose to explicitly model acceleration. 

**7** 



The presented formulation assumes we know the speed of each player in the snapshot. However, StatsBomb 360 data do not provide any velocity information. We therefore infer velocities at the time of the snapshot  [13]. For each event, we look at the next event and calculate the positional displacement for all players in the event freeze frame and divide it by the difference in event timestamps to estimate velocities for each snapshot. 

### _Probability Conversion_ 

In the previous steps, we parametrized the passing line with a finite set of points, and calculated the TTI of all players and the ball to each of these points. As the final step, we now compute the probability that each of the three passing lines (right, center, left) is blocked by aggregating TTIs. 

Similarly to [9], we express the probability that each player gains possession of the ball at a particular target point (𝑘) as the combination of two components. First, a player needs to be in a position to intercept the ball at that location. We call the time it takes the ball to get there 𝑇 . Then, 𝑘 we model the **interception probability** as the CDF of a sigmoid centered on Δ𝑡 = 𝑇 − 𝑇𝑇𝐼 : 𝑘 𝑗 𝑖𝑛𝑡 𝑃 ,  with 𝑠= √3 σ / π . This accounts for variability that is not 𝑗<sup>= 1 / (1 + 𝑒𝑥𝑝 (−Δ𝑡/𝑠 ) )</sup> explicitly modeled in TTI calculation such as differing speeds, reaction time, or fatigue. So, for 𝑖𝑛𝑡 example, if the player would arrive way before the ball, Δ𝑡 << 0  hence  𝑃 We found σ = 0. 20 𝑗<sup>≈ 1 .</sup> to give us the best results. Second, even if the player is ready, controlling the ball takes time. This 𝑐𝑡𝑟𝑙 **control probability** is modeled  as an exponential process  𝑃 = 1 −𝑒𝑥𝑝(−λΔ𝑇) ≈λΔ𝑇 with 𝑗 𝑘 rate λ ≈ 4.3 s ⁻ ¹ and △𝑇 = 𝑇 −𝑇 (with 𝑇 the start) being the time interval between consecutive 𝑘 𝑘 𝑘−1 0 target points. 

Combined, this gives the probability that player j gains possession in the interval [𝑇 , 𝑇 + ∆𝑇 ]: 𝑘 𝑘 𝑘 



This holds if only one player exists. In practise, we need to subtract the probability that any player has already intercepted the ball by time . So the formulation becomes: 𝑇 



For each passing lane, we compute this discretized numerical integration simultaneously for each player, across each [𝑇 , 𝑇 +△𝑇 ] interval along the parameterized line. This gives us the total 𝑘 𝑘 𝑘 probability 𝑃 that each player intercepts/receives the ball before the end of the cone: 𝑗 



We aggregate the probabilities of players on the defending team into a block probability 𝑃 and 𝑏𝑙𝑜𝑐𝑘𝑒𝑑 those of the attacking team into a receive probability 𝑃 . Note that as we don’t run the 𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑑 

**8** 



numerical integration to   𝑡 → ∞, we are left with a non-zero probability that no one controls the ball before the end of the cone. 

We define any one of the three lines as blocked if 𝑃 > 𝑃 . Finally, the passing lane can 𝑏𝑙𝑜𝑐𝑘𝑒𝑑 𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑑 be defined as blocked if **Any** (one), **Majority** (two), or **All** (three) of these lines are blocked. This provides more granularity and flexibility to our analysis. We give a visual example of the discretized passing lanes, an intuition about TTIs and final blocking/receiving probabilities in Figure 2. 



**Figure 2:** Evaluating block probability for potential passes using Lane Control. The dots along the passing cone represent the target points, and are colored according to the object that has the shortest time to arrive: the ball (green), an attacker (red), and a defender (blue). For each of the center, left, and right lines of the passing corridor we show the probability that a pass along that line is blocked 𝑃 and that it is 𝑏𝑙𝑜𝑐𝑘𝑒𝑑 

successfully received 𝑃 . 𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑑 

### **Evaluating Pass Block Models** 

Evaluating the accuracy of our Lane Control approach presents a fundamental challenge: by definition, a blocked pass is an unobserved event. When a defender successfully obstructs a passing lane, the corresponding pass is typically never attempted, meaning there is no explicit ground truth record against which to validate the prediction of 𝑃 and 𝑃 . Consequently, 𝑏𝑙𝑜𝑐𝑘𝑒𝑑 𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑑 assessing the quality of a pass lane-blocking model requires an indirect approach. 

To overcome this issue, we evaluate our pass block models on observed passes. The key intuition behind our approach is that if a passing lane is genuinely blocked, it should not be possible for a successful pass to be played through it. Therefore, we assess the accuracy of our proposed Lane Control approach and the three geometric baselines by testing whether their predictions of blocked or open lanes are consistent with the results of passes that were actually executed during matches. 

**9** 



Formally, for each completed pass (𝑝 , 𝑟 ), we compute whether the lane 𝐿(𝑝 , 𝑟 ) was predicted to 𝑎 𝑖 𝑎 𝑖 be blocked or open by each model. If a model predicts the lane as blocked but the pass was nevertheless successfully completed, this constitutes a false positive, indicating an overestimation of defensive influence. Conversely, if a model predicts the lane as open but the pass was unsuccessful or intercepted, this is treated as a false negative, representing an underestimation of defensive influence. 

We restrict our evaluation to progressive passes (excluding high passes) which occurred between the halfway line and the attacking penalty box, as our original intuition was to evaluate the impact of defensive midfielders screening the backline. Although this evaluation could be extended to the entire pitch and consider the defensive impact of attackers pressing, we found expanding the area of interest made the already imbalanced dataset even more skewed. For progressive passes between the halfway line and attacking penalty box, the pass completion ratio was 98% across the Big 5 European leagues (Appendix B). This is mostly because we exclude high passes, which bypass the effect of blocking defenders while also accounting for a large percentage of incomplete passes. For example, ~73% (141/193) of incomplete passes  in the match between Hellas Verona and Napoli on August 18th, 2024 were high passes. 

Table 1 reports standard classification metrics across the Big 5 European leagues. Both Lane Control Majority and All outperform the three baselines in terms of balanced accuracy (+ 11-15%) and macro F1 score (+ 0.17-0.20). While all of the models had similarly low rates of false negatives (underestimating defenders influence on a pass that was actually unsuccessful), the baselines had significantly higher rates of false positives (overestimating defenders influence on a pass which was actually completed). The raw accuracies are high due to the class imbalance.  Lane Control Majority has slightly better recall (hence the higher balanced accuracy), while Lane Control All has lower overestimation (FP) and higher precision (hence the best F1/macro F1 score). 

**Table 1:** Performance of baseline pass block models and Lane Control on progressive passes between midfield and attacking penalty box for Big 5 European leagues from 2024/25 season (Ground truth: 69,500 passes analyzed, 98.74% successful passes, 1.17% unsuccessful passes) 

||||**Metr**<br>|**ic**<br>|||
|---|---|---|---|---|---|---|
||**FP**<br>(overestimation)|**FN**<br>(underestimation)|**Balanced**<br>**Accuracy**|**Accuracy**|**Macro F1**<br>**Score**|**F1 Score**|
|**Line Corridor**|10.89%<br>(7,572)|0.90%<br>(628)|55.82%|88.20%|0.3006|0.0430|
|**Cone Corridor**|2.17%<br>(1,508)|1.07%<br>(745)|53.03%|96.76%|0.2932|0.0561|
|**Gaussian**<br>**Cone**|14.09%<br>(9,791)|0.84%<br>(586)|56.79%|85.07%|0.3048|0.0417|



**10** 



|**Lane Control**<br>**(Majority)**|1.52%<br>(1,053)|0.73%<br>(507)|68.01%|97.76%|0.4806|0.2811|
|---|---|---|---|---|---|---|
|**Lane Control**<br>**(All)**|0.98%<br>(680)|0.76%<br>(529)|66.93%|98.26%|0.4941|0.3189|



## **RQ2. How effective are the cover shadows?** 

Having established how to detect when a defender blocks a potential pass, we now extend our focus to the collective level. Our aim is to quantify how effectively the defending team’s positioning constrains the opponent’s most dangerous, chance-creating passes. This entails adding an additional layer to the analysis: the threat brought by each potential pass. 

Ideally, a set of well-executed cover shadows reduces the threat that the ball carrier can generate by passing to teammates. Therefore, to quantify how effective the defending team’s cover shadows are, we: 

1. **Quantify the current offensive threat of the attacking team** as the sum of each available passing option’s threat value, weighted by the probability that the ball gets to that player (i.e., the ball carrier chooses that option for the next pass, and the pass succeeds). 

2. **Quantify the threat of a counterfactual unblocked scenario** by modeling how pass selection and success probabilities would change if fewer or no cover shadows were applied by the defending team. 

3. **Define the** **_blocking score_** as the difference between the two threat values, where a positive value indicates that the applied cover shadows are actively reducing the opponents’ potential to create goal-scoring chances. 

### **Quantifying the Current Threat** 

The threat posed by the attacking team in the current snapshot  is composed of the individual 𝑆 threat of each of its players: 



Intuitively the threat posed by each of the attacking team’s players depends on two factors: how dangerous each attacking player’s position is, and how likely that player is to successfully receive the ball next. An attacker may occupy a dangerous area (e.g., inside the box) but is unlikely to receive the ball if surrounded by several defenders. In this case, the ball carrier might choose a safer pass to an open teammate, or the attempted pass may fail as it is missed or intercepted by a defender. Consequently, the most dangerous attackers are those who combine a high positional threat (i.e., proximity to goal) with a high probability of receiving the ball (i.e., being relatively open). 

**11** 



It follows that computing the attacking team’s threat requires estimating (1) the positional threat of each potential receiver, and (2) the probability that the given receiver will successfully receive the next pass. 

Passes often target the open space near a player rather than their exact location. Therefore, both aspects should not only consider the receiver’s exact location, but also his surroundings. To do so, we discretize the pitch into a 104x68 cell grid, where each cell is described by its (𝑥, 𝑦) coordinates, and we consider that the ball carrier can attempt a pass towards each of these cells. We then partition the space computing Voronoi regions so that each grid cell is associated with the closest attacker. We express the attacker controlling position (𝑥, 𝑦) as:<sup>2</sup> 



Defining the set of cells assigned to receiver  as 𝑟 𝑁 , the threat associated with receiver  in 𝑟 𝑟 snapshot  can be computed by taking the weighted sum over all 𝑆 (𝑥, 𝑦) ∈ 𝑁𝑟: 



where 𝑡ℎ𝑟𝑒𝑎𝑡(𝑥, 𝑦) represents the positional threat at location (𝑥, 𝑦), and 𝑝𝑟(𝑥, 𝑦) represents the probability that the given receiver  successfully receives the ball at location 𝑟 (𝑥, 𝑦). 

We estimate the probability that receiver  successfully receives the ball at location 𝑟 (𝑥, 𝑦) as 𝑝𝑟(𝑥, 𝑦) = 𝑃(𝐷= (𝑥, 𝑦) | 𝑆) · 𝑃(𝑜= 𝑠𝑢𝑐𝑐𝑒𝑠𝑠 | 𝐷= (𝑥, 𝑦), 𝑆) , 

where: 

- 𝑃(𝐷= (𝑥, 𝑦) | 𝑆) is the probability that the next pass targets cell (𝑥, 𝑦) 

- 𝑃(𝑜= 𝑠𝑢𝑐𝑐𝑒𝑠𝑠 | 𝐷= (𝑥, 𝑦), 𝑆) is the probability that if attempted, a pass to cell (𝑥, 𝑦) succeeds. 

Therefore the formula for 𝑝𝑟(𝑥, 𝑦) quantifies the probability that the given receiver will successfully receive the next pass by encompassing (1) pass selection probability, i.e., how likely it is that the receiver is chosen for the next pass and (2) pass success probability, i.e., how likely it is that a pass to that receiver succeeds (and hence is not missed or intercepted by a defender). We now explain how we estimate the positional threat, the pass selection likelihood and the pass success likelihood. 

### _Positional Threat Model_ 

> 2 This simplification assigns each cell to one, and only one, attacker. However, it would also be possible to apply a probabilistic assignment. 

**12** 



To estimate the positional threat for every cell (𝑥, 𝑦) ∈ 𝑁𝑟, we employ Expected Threat (𝑥𝑇) [14].<sup>3</sup> This approach overlays a grid on the field (Figure 3) and assigns a value to each grid cell based on how often a possession from that area leads to a goal. 



**Figure 3** : The positional threat as a result of upscaling the original Expected Threat (𝑥𝑇) grid. Darker red means a higher positional threat (i.e., probability of scoring a goal later on in the possession). 

_Pass Selection Model_ 

To estimate the pass selection probabilities, we take inspiration from previous work [6] and implement a pass selection model using the SoccerMap [15] architecture. This popular CNN architecture has been used (among other things) to generate a probability surface over the full pitch, estimating the probability that the ball carrier will play the ball at each location. To do so, it takes into account the positional information of all players on the pitch, as these will all influence the probability a pass is played to a particular location. 

We train our pass selection model by gathering all passes from the 2024/25 season of the Big Five European leagues, filtering as described in “Data and Definitions".  We use four leagues for training, extracting a total of 1,116,738 passes. A random sample of 20% of these passes is used as a validation set for model selection, and the rest is used as the training set. We keep aside the 317,061 passes from Serie A, as we use them for evaluating the model. Figure 4 (left) shows the predicted pass selection surface for one example pass. 

### _Pass Success Model_ 

> 3 We use Karun Singh’s league-wide xT values from the 2017-18 Premier League season (available from <u>https://karun.in/blog/data/open_xt_12x8_v1.json), upscaled to a 104x68 grid with bilinear interpolation.</u> 

**13** 



Similarly, we use SoccerMap to generate a probability surface over the full pitch, estimating the probability that the pass will be successfully played to each location. We again reproduce the model from [6], and use the same set of passes as for the pass selection model. The difference is in the input (we only use the first 7 channels for pass success) and in the label, which reflects whether an executed pass succeeded or not. 

The pass success surface for the example snapshot is shown in Figure 4 (right).  We precisely evaluate our pass selection and pass success models and discuss their performances in Appendix C. 



<!-- Start of picture text -->
evaluate our pass selection and pass success models and discuss their performances in Appendix<br>C.<br>Figure 4 : Pass selection surface (left) and pass success surface (right) for an example snapshot. The pass<br><!-- End of picture text -->

**Figure 4** : Pass selection surface (left) and pass success surface (right) for an example snapshot. The pass selection surface shows how likely it is that the ball carrier plays a pass to each location. Red shading represents more likely pass destinations. The pass success surface shows the probability that a pass to any location successfully reaches the receiver. Red shading represents easier passes. 

Ultimately, the product of the 𝑥𝑇 surface (Figure 3), the pass selection surface (Figure 4, left) and the pass success surface (Figure 4, right)  yields the weighted threat surface shown in Figure 5. Each cell in the resulting surface amounts to 𝑡ℎ𝑟𝑒𝑎𝑡(𝑥, 𝑦) · 𝑝𝑟(𝑥, 𝑦). We can finally aggregate * threat values per each potential receiver  by taking the sum over all 𝑟 (𝑥, 𝑦): 𝑟 (𝑥, 𝑦) = 𝑟. Aggregated values are also reported in Figure 5. 

**14** 



<!-- Start of picture text -->
: Weighted threat surface for the example snapshot, obtained as the product of xT surface (Figure 3),<br>pass selection surface (Figure 4, left) and pass success surface (Figure 4, right). Red shading represents<br><!-- End of picture text -->

**Figure 5** : Weighted threat surface for the example snapshot, obtained as the product of xT surface (Figure 3), pass selection surface (Figure 4, left) and pass success surface (Figure 4, right). Red shading represents more threatening pass options.The threat of each player is the sum of the values of all cells in the Voronoi region of that player. The total offensive threat is the sum of the threat of each potential receiver, and is equal to 0.031. 

### **Quantifying the Unblocked Threat** 

The task of lane-blocking defenders is to occupy dangerous passing lanes and thereby discourage passes to attacking players who are positioned in a threatening area. While the positional threat of a potential receiver is exclusively related to his location, the choice between the receivers and the difficulty of each potential pass are influenced by the defenders’ positioning. Hence, the threat of the attacking team in a counterfactual _unblocked_ scenario (S’) can be estimated by modifying the defenders’ positioning. 

Specifically, we alter the input to the SoccerMap models by removing (a subset of) the defenders that are not man-marking. Depending on the use case, one can focus on removing one defender (e.g., to value individual covering abilities), or a coherent subset / all lane-blocking defenders (e.g., to quantify the covering abilities on a group level). Afterward, we estimate new pass selection and pass probability surfaces and recompute the total threat with updated weights 𝑝𝑟(𝑥, 𝑦) for every location. This ultimately yields a different threat value for the _unblocked_ counterfactual scenario. We show the comparison between threat surfaces of the original and counterfactual scenario in Figure 6, together with aggregated threat per player. 

**15** 



<!-- Start of picture text -->
Figure 6<br><!-- End of picture text -->



**Figure 6** : Weighted threat surface for our example snapshot in the original (left) and counterfactual scenario where cover shadows are removed (right). Only defenders that are man-marking are kept in the counterfactual. Red shading represents more threatening pass options. The total threat of the original scenario is 0.031, and increases to 0.041 in the counterfactual, yielding a blocking score of 0.01. A positive blocking score indicates that cover shadows are preventing some threat. 

As a second example, we show that we can also study the effect of a single cover shadow by only removing one player in the counterfactual. Figure 7 focuses on the midfielder of the defending team (in purple) , who is shielding a dangerous pass. If we ignore him in the figure on the right, the attacking team's striker is by far the most threatening receiver, as he is well-positioned and has some free space to occupy in proximity of the box. On the left, we see that the cover shadow applied by the defender is a well-executed block forcing the ball carrier to play a safer pass (e.g., on the left wing). 



<!-- Start of picture text -->
team (in purple) , who is shielding a dangerous pass. If we ignore him in the figure on the right, the<br>attacking team's striker is by far the most threatening receiver, as he is well-positioned and has<br>some free space to occupy in proximity of the box. On the left, we see that the cover shadow<br>applied by the defender is a well-executed block forcing the ball carrier to play a safer pass (e.g., on<br>the left wing).<br>Figure 7 : Threat surfaces for a game snapshot where we study the effect of a single cover shadow. We focus<br>on the purple defender. On the right, we see that removing him clearly increases the threat coming from the<br><!-- End of picture text -->

**Figure 7** : Threat surfaces for a game snapshot where we study the effect of a single cover shadow. We focus on the purple defender. On the right, we see that removing him clearly increases the threat coming from the attacker he is blocking. 

**16** 



### **Defining the Blocking Score** 

To quantify the overall offensive threat the defending team’s cover shadows are preventing, we define the blocking score as: 

### blocking_score = threatS’ - threatS 

In our running example from Figures 6, the defensive team’s cover shadows clearly impact the aggregated threat values of the two alternatives. Indeed,  𝑡ℎ𝑟𝑒𝑎𝑡 0. 041 and 𝑡ℎ𝑟𝑒𝑎𝑡 = 0. 031, 𝑆' = 𝑆 

hence the blocking score is equal to 0. 01. The positive value indicates that the well-executed cover shadows have reduced the offensive team's danger by 25%. In the second scenario (Figure 7)  the players are further away from the goal, hence the offensive team is less threatening, with 𝑡ℎ𝑟𝑒𝑎𝑡 0. 027 and 𝑡ℎ𝑟𝑒𝑎𝑡 = 0. 029. The blocking score is still positive, albeit much lower ( 𝑆' = 𝑆 0. 002). 

## **RQ3: Can the cover shadows be improved?** 

Finally, we study if and how the effectiveness of the employed cover shadows can be improved. To this end, we compute the optimal defensive positioning of the defending team with respect to the most dangerous attackers. We formulate this task as a linear optimization problem. 

Intuitively, we attempt to find the minimal distance each defender has to travel such that the passing lanes to the most dangerous attackers are blocked. This requires defining (1) which attackers are considered the most dangerous, and (2) in which areas of pitch the defenders should be positioned in order to guarantee optimal blockage of the aforementioned attackers. Then, it becomes possible to optimize the defenders’ positions by assigning each individual defender to a location within the considered areas minimizing displacement from their current positions. Searching for the minimal distance to travel allows us to find _realistic_ adjustments to the defenders’ positioning in order to optimize the effectiveness of their cover shadows. 

### **Defining the set of dangerous attackers** 

We define the set of dangerous attackers to consider in the optimization problem, 𝑅' ⊂ 𝑅, as those attackers that are positioned between the ball carrier and the goal. We quantify how dangerous each attacker 𝑟 is by exclusively considering the 𝑥𝑇 value at his location. We ignore the 𝑖 likelihood term from RQ2 to make the problem formulation more tractable when repositioning defenders. 

### **Defining the set of areas that defenders should occupy** 

Ideally, defenders should block all passing lanes to dangerous attackers. We define an attacker to be blocked if at least one defender is positioned within the passing cone 𝑇(𝑝 , 𝑟 ) going from the 𝑎 𝑗 

**17** 



ball carrier 𝑝 to the attacker  (i.e., we use the cone baseline from RQ1 to define positional 𝑟 𝑎 𝑗 adjustments using straightforward geometric regions). 

In a naive scenario where each defender can block at most one attacker, the set of areas to occupy simply corresponds to the cones related to the 𝑛 attackers with the highest 𝑥𝑇, where 𝑛 𝑑𝑒𝑓 𝑑𝑒𝑓 equals the number of defenders in the snapshot. However, when passing cones overlap, a single defender could block multiple passing lanes at once  when positioned at the intersection of these cones (see Figure 8). Therefore we consider additional areas of interest for defending positioning beyond the set of cones. For any combination of dangerous attackers 𝑈⊆𝑅', we define the intersection of their cone triangles as ∩{𝑟𝑗 ∈𝑈} 𝑇(𝑝𝑎, 𝑟𝑗). If this intersection is non-empty, we consider it as a potential area for a defender to occupy. To encompass all passing cone triangles and non-empty intersections that defenders could occupy, we refer to each of the considered areas as a polygon. The set of all considered polygons  is formally defined as: 



<!-- Start of picture text -->
𝑃= {∩{𝑟𝑗𝑗 ∈𝑈} 𝑇(𝑝𝑎, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑎, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑗 ∈𝑈} 𝑇(𝑝𝑎, 𝑟𝑗)) > 0}<br><!-- End of picture text -->

𝑃= {∩{𝑟𝑗𝑗 ∈𝑈} 𝑇(𝑝𝑎, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑎, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗, 𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗): 𝑈⊆𝑅', 𝑎𝑟𝑒𝑎(∩{𝑟𝑗𝑗 ∈𝑈} 𝑇(𝑝𝑎, 𝑟𝑗)) > 0} 

**Figure 8** : A snapshot with 5 dangerous attackers and their passing cones. Suppose 𝑛 = 4. Whenever two 𝑑𝑒𝑓 cones intersect, it is enough for a defender to be positioned in the intersection of the two cones to simultaneously block two attackers. The dark red polygons show the areas in which 4 defenders could be positioned to block all 5 dangerous attackers. If we did not consider intersections of cones, we would have 5 cones and 4 defenders, hence the attacker with the lowest 𝑥𝑇 would remain free even under optimal defensive positioning. 

**18** 



We then need to identify the optimal subset of polygons, i.e., the smallest set of polygons that, when all occupied by defenders, guarantees the best possible coverage of dangerous attackers. To do so, we enumerate all possible combinations of polygons. For each subset of polygons , we 𝑄 check which attackers are covered, and we call this set 𝑐𝑜𝑣𝑒𝑟𝑒𝑑(𝑄). We compute the total 𝑥𝑇 

blocked by   as 𝑄 ∑ 𝑥𝑇 . Having enumerated all possible subsets, we formally define the 𝑗 𝑟 ∈ 𝑐𝑜𝑣𝑒𝑟𝑒𝑑(𝑄) 𝑗 

minimal-size set of polygons maximizing threat coverage as: 



Therefore, the best-case scenario for the defenders is to occupy each polygon in . Figure 8 𝐺 illustrates this in an example with 5 attackers for which the optimal set of polygons has size 4. 

### **Defining the optimization problem** 

Once we know where defenders should be placed to optimally prevent passes to dangerous attackers, we can frame an optimization problem to suggest repositioning. Formally, the optimization problem then becomes: 



where  is the set of defenders and  the optimal set of polygons to occupy. Here, 𝐷 𝐺 𝑐 ∈𝐶  (i.e., the 𝑑,𝑔 cost matrix) represents the shortest distance that defender  needs to travel with respect to his 𝑑 current position in order to occupy polygon   (i.e., be inside polygon  ). 𝑔 𝑔𝑥 is a binary variable set 𝑑,𝑔 to 1 if defender  is assigned to polygon . We solve this linear optimization problem using the 𝑑 𝑔 Hungarian algorithm [16], [17]. The solution to this problem yields updated coordinates for defenders that were not optimally positioned. Figure 9 shows an example situation in which the approach suggests slightly repositioning three defenders to better shield the attackers. 

**19** 



**Figure 9:** A snapshot illustrating the optimal defensive positioning as result of the linear optimization problem. The positions of three defenders (red dots) are slightly altered (red triangles) to optimally cover the most dangerous attackers (blue dots). The passing cones to the attackers which were already covered in the original scenario  (yellow) / are newly covered in the optimal scenario (red)  are also shown. 

### **Evaluating Optimization Problem Solutions** 

We first conduct a basic evaluation of our method by extracting game snapshots preceding the top 1000 most dangerous successful passes from the 2024/25 Serie A season, where the danger consists of the 𝑥𝑇 value at the receiver’s location. We identify the receiver of the pass, and check if any defender is actively blocking him from receiving the pass (i.e., is located within the cone going from the ball to the pass receiver) in two scenarios: the actual game state, and the alternative game state where defenders are repositioned according to our assignment problem solution. We then count how often this is the case, and report results in Table 4. 

**Table 4** : Comparison of actual vs. suggested defenders positions for the top 1000 most dangerous successful passes of the 2024/25 Serie A season. A pass is blocked if at least one defender is in the cone going from the ball to the actual receiver. 

|**Actual / Suggested**|Blocked|Free|
|---|---|---|
|Blocked|178|0|



**20** 

Free 

789 

33 



In 822 out of 1000 passes, no defender was occupying the passing cone of the receiver. Our method suggests a repositioning where the cone is occupied in 789 of these cases. In 33 passes, the receiver comes from behind and is therefore not accounted for in our formulation, which focuses on dangerous attackers between the ball and the goal. In the remaining 178 cases, the receiver was already blocked. Note that it never happens that our formulation “frees up” a dangerous attacker. 

### **Evaluating  Cover Shadows Improvements** 

Finally, we evaluate whether our suggested repositionings reduce the attacking team’s threat, calculated using the full weighted threat formulation from RQ2. Note that differently from RQ2, the optimization problem uses as target defender locations a set of polygons defined by just looking at the 𝑥𝑇 of each attacker. Hence it does not consider the probability that each attacker receives the ball. However, while we do not explicitly account for pass likelihood or success, our underlying assumption is that the generated solution will inherently discourage passes to high-𝑥𝑇 attackers, given that it forces defenders to block them. We now specifically check whether this claim holds as part of our evaluation. 

We first analyze the effect of suggested positional adjustments on the threat surface of one specific example, which we show in Figure 10. On the left, we see that in the original game state, the ball carrier has an open corridor towards a teammate closer to the opponents’ goal, who is also the most dangerous attacker according to the threat surface generated by our analysis. As we reposition defenders (on the right), the purple defender is slightly moved to exactly occupy that passing lane. In this alternative scenario, the ball carrier is forced to play a conservative backward pass, which becomes the most likely option. This is reflected in a lower aggregated threat, though in this case the numerical difference is minimal as all players are positioned far from the goal (specifically, it decreases from 0.025 to 0.022) . 





**21** 



**Figure 10** : Aggregated threat surfaces for a snapshot before and after applying suggested defender repositionings from the optimization problem solution. Repositioned defenders are purple. Red shading means more threatening pass options. The threat associated with each attacker is the sum of the values of all cells in the Voronoi region of that player. 

We broadly evaluate if threat consistently decreases thanks to our repositionings by applying our method on all passes from a full season. We take all moments of interest in the 2024/25 Serie A season (i.e., the interesting snapshots described in our “Data and Definitions” section), and filter out game states where defenders position cannot be improved according to our method, which leaves us with 63,037 snapshots. We then extract updated defenders positions and generate pass selection/success surfaces with SoccerMap, to then compute the aggregated threat for all snapshots where defenders have been repositioned  (we compute the threat as explained in RQ2). Finally, we compare the threat after our suggested repositioning with the threat of the original scenario in each of the considered snapshots. 

Interestingly, the overall threat is reduced in 75% of the cases, indicating that our repositioning is effective in discouraging dangerous passes. For the remaining cases, we believe modeling our repositioning on basic geometric obstruction of passing cones might be an oversimplification (as players right outside of a cone can still block  or influence the pass).  Future work should explore how to better model optimal repositioning without relying on simple geometric constraints. A possible line of work involves extending our physics-based approach to define a broader influence zone around the passing lane, capturing all spatial regions where a defender’s presence could realistically deter or intercept a pass, without being constrained to passing cones. 

## **Use Cases** 

We now use our contributions from RQ1 and RQ2 to study how effective teams and players are at applying cover shadows. Specifically, we present a few insights on a team level by applying our methods on data of the 2024/25 Serie A season. Additionally, we analyze  the Belgium-Portugal match from the 2020 European Championship to study performances at a player level. 

### **1 .  Which teams are better at cover shadowing?** 

We study teams’ effectiveness at preventing dangerous passes by aggregating their blocking score over all defensive situations from the 2024/25 Serie A season. We consider all game states where the team’s opponents are playing a foot pass between midfield and the defending team box, excluding set pieces and scenarios where no attacker is positioned in front of the ball (as no cover shadow happens there). We then average the total blocking score per match, and show the resulting ranking in Figure 11. 

**22** 





**Figure 11** : Average blocking score per match for each team of the 2024/25 Serie A season. For each match, we take the sum of the blocking score of all (selected) defensive situations where the team is applying at least a cover shadow. 

Notably, teams topping the list finished on the lower end of the table, and were often more focused on limiting their opponents rather than building up valuable plays. Hence one would expect that they pay a lot of attention to cover shadows. On the other end of the spectrum instead are Bologna and Como, two of the best surprises of the year. These were mostly known for an offensive style of play with lots of possession and many players going beyond the ball when attacking. It naturally follows that cover shadows were less of a factor for them. 

### **2 .  Which players are better at cover shadowing?** 

We can use our contributions from RQ1 and RQ2 to also quantify a player’s ability to apply effective cover shadows. Together, these metrics capture both how often a player blocks a lane and how much value those blocks contribute defensively. Players who combine a high blocking rate with high threat prevention can be interpreted as especially effective in applying cover shadows. 

To do so, we analyze the Belgium vs. Portugal match from the UEFA Euro 2020. We consider freeze frames between midfield and the attacking penalty box in which at least one forward passing option exists. After filtering out frames with incomplete player velocity values, 186 of the 224 snapshots of interest are kept (76 for Belgium and 110 for Portugal in possession), corresponding to 288 potential passes for Belgium and 462 for Portugal. 

For each defender, we compute a **blocking rate** as the proportion of frames with a passing lane that is classified as blocked by the defender according to Lane Control: 



This simple metric captures how frequently a player obstructs available passing options, independently of whether the opponent actually attempts the pass. 

**23** 



Next, we  measure the _impact_ of each defender — that is, how much attacking threat is neutralized by each defender’s cover shadow. For each selected snapshot, we estimate the reduction in threat due to the cover shadow applied by each defender  (as defined in RQ2) and aggregate these values per player over all snapshots. 

Plotting players by their blocking rate (x-axis) and total threat prevented (y-axis) highlights distinct defensive profiles (Figure 12). Players on the lower-right quadrant exhibit the highest block rates, reflecting their frequent role in screening passing lanes. Here we find central midfielders such as Witsel, Tielemans, Palhinha and Moutinho. Players in the higher-left quadrant, instead, block less frequently but prevent a lot of threat. This is the case for fullbacks such as Meunier and T. Hazard, who occasionally find themselves covering crucial defensive areas.  Players in the upper-right quadrant both block frequently and prevent high-threat passes, representing the most effective cover-shadowing performers. Here, Sanches represents a mix of the two profiles. Finally, offensive players and central defenders tend to cluster toward the lower-left, indicating limited involvement in preventing dangerous passes. 



**Figure 12** : Defensive cover shadowing performances of all players in the Belgium vs. Portugal UEFA Euro 2020 match. Each point represents a player, plotted by their blocking rate (x-axis: proportion of passing lanes blocked) and total threat prevented (y-axis: cumulative 𝑥𝑇 reduction due to cover shadows). 

## **Related Work** 

Research in soccer analytics has predominantly focused on offensive actions (i.e., passes, shots, carries). The majority of player valuation models and event-based metrics are designed to assess 

**24** 



how these actions increase the likelihood of scoring [14], [18], [19]. In contrast, defensive contributions have received far less attention. Studies of on-ball actions show a clear bias toward offensive play, leaving defensive involvement underrepresented [20]. This gap is largely due to the nature of defending, which is more about positioning and movement rather than discrete, ball-related events. Defenders exert influence by occupying space, cutting passing lanes, and constraining opponents. Yet, these behaviors were historically difficult to quantify without high-frequency tracking data or freeze-frame snapshots of player positioning. 

Therefore, prior work on defensive play analysis using solely event data has mainly focused on notational match statistics of defensive on-ball actions [21], [22] and the valuation of defensive on-ball actions (e.g., interceptions and tackles) by predicting the offensive threat they prevented [32]. However, by solely focusing on the on-ball actions, these approaches only consider a small part of a defender’s responsibilities and cannot provide a complete view of their skills. 

Using tracking or snapshot data, it becomes possible to evaluate a wider range of positional aspects. To this end, research has mainly looked into general behavioral analysis of players and teams, such as the calculation of centroids and dispersion [23], [24], density [25], and the positioning of defensive lines [26]. In addition, some work has looked into the quantification of _specific_ defensive aspects, such as pressure [27], [28], [29], [30] and defensive anticipation [1]. In contrast, the _overall_ off-ball defensive influence has been modeled in some frameworks (i.e., expected disruption models)  [2],  [3] by attributing changes in a team’s typical playing style or offensive efficiency to the defensive behavior of opponents. However, these approaches mainly consider man-marking actions and primarily attribute their impact at the team level. 

Among works quantifying defensive pressure, J. Bekkers recently proposed a physics-based framework for measuring pressing intensity via time-to-intercept estimation, and outlined a potential extension for passing lanes where pressure is assessed at a point along the line rather than for a moving attacker [11]. Building on this concept, our Lane Control approach parameterizes passing corridors and computes TTI-based blocking probabilities for each point along the corridor. 

Most closely related are the recent works of Everett et al. [3], [31]. On the one hand, they provide an approach for calculating optimized defender positions with respect to the threat using a multi-agent Markov Decision Process. However, this uses a coarse-grained grid to represent possible positions, and does not explicitly consider lane-covering defenders nor blockable areas. On the other hand, they analyze a defender’s covering abilities by applying graph neural networks (GNNs) and attention mechanisms to measure their influence on the reception probabilities of attackers. 

In this work, we build on this line of research and combine both the evaluation and optimization of defensive positioning. Rather than relying solely on latent influence scores, we take a ‑ first principles approach and quantify how defensive positioning, and in particular positional adjustments, change the threat associated with the opponent’s possession. 

**25** 



## **Conclusion** 

This paper introduced a framework for analyzing cover shadows in soccer. First, we demonstrated the limitations of basic geometric models in detecting blocked passing lanes, and introduced a physics-based model to give a more accurate estimation of _pass blocking probability_ . Second, we formulated a novel metric to quantify the threat of the attacking team’s passing options, defining _cover shadow effectiveness_ as the reduction in this threat. Third, we proposed an algorithm to _optimize defenders’ positioning_ so that the most dangerous passing lanes are blocked. Therefore, this work provides tools to detect, quantify and optimize the use of cover shadows to prevent dangerous passes. 

While the StatsBomb 360 data used in this work provides valuable off-ball information, the provided contextual information is still limited. Future work could extend this framework to full tracking data, which would help in better distinguishing whether a player is a cover shadow defender or a man-marking defender. Full knowledge of players and ball kinematics would also allow for a more accurate physics-based model and more accurate assessments of each passing option’s threat. Additionally, having access to player identities would enable a more detailed player-level analysis, such as examining performance across specific regions of the pitch or in different phases of the match. For example, we hypothesize that as fatigue sets in, players become less adept at sustaining optimal positioning. Thus, by tracking a player's effectiveness at maintaining cover shadows, one might be able to identify the onset of fatigue. 

## **Acknowledgements** 

This research is supported by the Flemish Government under the “Onderzoeksprogramma Artificiële Intelligentie (AI) Vlaanderen” program [AW, LS, MVR, JD], the Research Foundation Flanders (FWO, LC: 11I8125N, MVR: 12A4326N), and KU Leuven Research Fund (iBOF/21/075, C14/24/091 to JD). 

## **References** 

- [1] Y. Wu and T. Swartz, “Evaluation of off-the-ball actions in soccer,” _Stat. Appl. - Ital. J. Appl. Stat._ , no. 2, May 2023, doi: 10.26398/IJAS.0035-008. 

- [2] M. Stöckl, T. Seidl, D. Marley, and P. Power, “Making Offensive Play Predictable - Using a Graph Convolutional Network to Understand Defensive Performance in Soccer,” _Proc 15th MIT Sloan Sports Anal. Conf._ , 2021, [Online]. Available: 

   - https://www.statsperform.com/wp-content/uploads/2021/04/Making-Offensive-Play-Predict able.pdf 

- [3] G. Everett, R. J. Beal, T. Matthews, T. J. Norman, and S. D. Ramchurn, “Evaluating Defensive Influence in Multi-Agent Systems Using Graph Attention Networks,” presented at the 2025 IEEE 12th International Conference on Data Science and Advanced Analytics, 2025. 

- [4] M. Van Roy, L. Cascioli, and J. Davis, “ETSY: A Rule-Based Approach to Event and Tracking Data SYnchronization,” in _Machine Learning and Data Mining for Sports Analytics_ , U. Brefeld, J. Davis, 

**26** 



J. Van Haaren, and A. Zimmermann, Eds., Cham: Springer Nature Switzerland, 2024, pp. 11–23. doi: 10.1007/978-3-031-53833-9_2. 

- [5] G. Anzer and P. Bauer, “Expected passes,” _Data Min. Knowl. Discov._ , vol. 36, no. 1, pp. 295–317, Jan. 2022, doi: 10.1007/s10618-021-00810-3. 

- [6] P. Robberechts, M. Van Roy, and J. Davis, “un-xPass: Measuring Soccer Player’s Creativity,” in _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , in KDD ’23. New York, NY, USA: Association for Computing Machinery, Agosto 2023, pp. 4768–4777. doi: 10.1145/3580305.3599924. 

- [7] F. Goes, E. Schwarz, M. Elferink-Gemser, K. Lemmink, and M. Brink, “A risk-reward assessment of passing decisions: comparison between positional roles using tracking data from professional men’s soccer,” _Sci. Med. Footb._ , vol. 6, no. 3, pp. 372–380, July 2022, doi: 10.1080/24733938.2021.1944660. 

- [8] D. Vatvani, “Upgrading Expected Goals,” Upgrading Expected Goals. Accessed: Oct. 15, 2025. [Online]. Available: https://www.hudl.com/blog/upgrading-expected-goals 

- [9] W. Spearman, A. Basye, G. Dick, R. Hotovy, and P. Pop, “Physics-Based Modeling of Pass Probabilities in Soccer,” presented at the MIT Sloan Sports Analytics Conference, Mar. 2017. [Online]. Available: https://www.researchgate.net/publication/315166647_Physics-Based_Modeling_of_Pass_Prob abilities_in_Soccer 

- [10] W. Spearman, “Beyond Expected Goals,” presented at the MIT Sloan Sports Analytics Conference, Boston, MA, Mar. 2018. [Online]. Available: https://www.researchgate.net/publication/327139841_Beyond_Expected_Goals 

- [11] J. Bekkers, “Pressing Intensity: An Intuitive Measure for Pressing in Soccer,” Dec. 30, 2024, _arXiv_ : 2501.04712. [Online]. Available: https://arxiv.org/abs/2501.04712 

- [12] L. Shaw, _Metrica_PitchControl.py_ . Github, Friends-of-Tracking-Data-FoTD. Accessed: Oct. 15, 2025. [Online]. Available: https://github.com/Friends-of-Tracking-Data-FoTD/LaurieOnTracking/blob/master/Metrica_P itchControl.py 

- [13] F. Hadddad, “Building a Pitch Control Model for StatsBomb Event Data,” Medium. Accessed: Oct. 12, 2025. [Online]. Available: https://medium.com/@fadih3940/building-a-pitch-control-model-for-statsbomb-event-datae0fbe50cac97 

- [14] K. Singh, “Introducing Expected Threat (xT).” Accessed: Nov. 06, 2025. [Online]. Available: https://karun.in/blog/expected-threat.html 

- [15] J. Fernández and L. Bornn, “SoccerMap: A Deep Learning Architecture for Visually-Interpretable Analysis in Soccer,” in _Machine Learning and Knowledge Discovery in Databases. Applied Data Science and Demo Track_ , Y. Dong, G. Ifrim, D. Mladenić, C. Saunders, and S. Van Hoecke, Eds., Cham: Springer International Publishing, 2021, pp. 491–506. doi: 10.1007/978-3-030-67670-4_30. 

- [16] H. W. Kuhn, “The Hungarian method for the assignment problem,” _Nav. Res. Logist. Q._ , vol. 2, no. 1–2, pp. 83–97, 1955, doi: 10.1002/nav.3800020109. 

- [17] SciPy Developers, _linear_sum_assignment (Hungarian algorithm)_ . (2025). [Online]. Available: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment .html 

- [18] “Introducing On-Ball Value (OBV) • Statsbomb Blog Archive.” Accessed: Nov. 06, 2025. [Online]. Available: https://blogarchive.statsbomb.com/news/introducing-on-ball-value-obv/ 

**27** 



- [19] T. Decroos, L. Bransen, J. V. Haaren, and J. Davis, “Actions Speak Louder Than Goals: Valuing Player Actions in Soccer,” in _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , July 2019, pp. 1851–1861. doi: 10.1145/3292500.3330758. 

- [20] L. Forcher, S. Altmann, L. Forcher, D. Jekauc, and M. Kempe, “The use of player tracking data to analyze defensive play in professional soccer - A scoping review,” _Int. J. Sports Sci. Coach._ , vol. 17, no. 6, pp. 1567–1592, Dec. 2022, doi: 10.1177/17479541221075734. 

- [21] J. Fernandez-Navarro, C. Ruiz-Ruiz, A. Zubillaga, and L. Fradua, “Tactical Variables Related to Gaining the Ball in Advanced Zones of the Soccer Pitch: Analysis of Differences Among Elite Teams and the Effect of Contextual Variables,” _Front. Psychol._ , vol. 10, Jan. 2020, doi: 10.3389/fpsyg.2019.03040. 

- [22] H. Lepschy, H. Wäsche, and A. Woll, “Success factors in football: an analysis of the German Bundesliga,” _Int. J. Perform. Anal. Sport_ , vol. 20, no. 2, pp. 150–164, Mar. 2020, doi: 10.1080/24748668.2020.1726157. 

- [23] R. Bartlett, C. Button, M. Robins, A. Dutt-Mazumder, and G. Kennedy, “Analysing Team Coordination Patterns from Player Movement Trajectories in Soccer: Methodological Considerations,” _Int. J. Perform. Anal. Sport_ , vol. 12, no. 2, pp. 398–424, Aug. 2012, doi: 10.1080/24748668.2012.11868607. 

- [24] L. Forcher, L. Forcher, S. Altmann, D. Jekauc, and M. Kempe, “Is a compact organization important for defensive success in elite soccer? – Analysis based on player tracking data,” _Int. J. Sports Sci. Coach._ , vol. 19, no. 2, pp. 757–768, Apr. 2024, doi: 10.1177/17479541231172695. 

- [25] L. Vilar, D. Araújo, K. Davids, and Y. Bar-Yam, “Science of winning soccer: Emergent pattern-forming dynamics in association football,” _J. Syst. Sci. Complex._ , vol. 26, no. 1, pp. 73–84, Feb. 2013, doi: 10.1007/s11424-013-2286-z. 

- [26] J. Castellano and D. Casamichana, “What are the differences between first and second divisions of Spanish football teams?,” _Int. J. Perform. Anal. Sport_ , vol. 15, no. 1, pp. 135–146, Mar. 2015, doi: 10.1080/24748668.2015.11868782. 

- [27] S. Merckx, P. Robberechts, Y. Euvrard, and J. Davis, “Measuring the Effectiveness of Pressing in Soccer,” _Proc. 8th Workshop Mach. Learn. Data Min. Sports Anal. P 1-15_ , 2021. 

- [28] I. Bojinov and L. Bornn, “The Pressing Game: Optimal Defensive Disruption in Soccer,” _Proc 10th MIT Sloan Sports Anal. Conf._ , 2016. 

- [29] G. Andrienko _et al._ , “Visual analysis of pressure in football,” _Data Min. Knowl. Discov._ , vol. 31, no. 6, pp. 1793–1839, Nov. 2017, doi: 10.1007/s10618-017-0513-2. 

- [30] L. Forcher, L. Forcher, S. Altmann, D. Jekauc, and M. Kempe, “The keys of pressing to gain the ball – Characteristics of defensive pressure in elite soccer using tracking data,” _Sci. Med. Footb._ , vol. 8, no. 2, pp. 161–169, Apr. 2024, doi: 10.1080/24733938.2022.2158213. 

- [31] G. Everett, R. J. Beal, T. Matthews, T. J. Norman, and S. D. Ramchurn, “Optimising Spatial Teamwork Under Uncertainty,” _Proc. AAAI Conf. Artif. Intell._ , vol. 39, no. 22, pp. 23168–23176, Apr. 2025, doi: 10.1609/aaai.v39i22.34482. 

- [32] C. Merhej, R. J. Beal, T. Matthews, and S. Ramchurn, “What Happened Next? Using Deep Learning to Value Defensive Actions in Football Event-Data,” in _Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining_ , Virtual Event Singapore: ACM, Aug. 2021, pp. 3394–3403. doi: 10.1145/3447548.3467090. 

**28** 



## **Appendix** 

**A.  Implementation Details for the Gaussian Cone Baseline** We represent each defender 𝑑 by an isotropic <u>2D Gaussian distribution 𝑁(µ</u> , σ ) with mean 𝑗 𝑗 𝑗 

2 position  µ = (𝑥 , 𝑦 ) and covariance  Σ = σ 𝐼 , where  is the variance multiplier (we use σ σ = 1 𝑗 𝑗 𝑗 𝑗 for 1m<sup>2</sup> variance) and  is the identity matrix. We compute how much the defender’s Gaussian 𝐼 distribution covers the cross section of the cone at the defender’s projected position on the passing line. For a pass from 𝑝 to  𝑟 of length  meters and unit direction , the parameterized 𝐿 û 𝑎 𝑖 center line is: 



For defender 𝑑 , we orthogonally project the defender’s mean position  onto the center line to µ 𝑗 𝑗 obtain the distance along the pass: 

_s*_ = 𝑐𝑙𝑖𝑝((µ −𝑝 ) · û; 0, 𝐿). 𝑗 𝑎 At _s*_ , the cone has a width 𝑊 _(s*)_ . The cross section  is a line segment of length  𝑆 𝑊 _(s*)_ 𝑗 perpendicular to the pass unit vector  and passing through the center line at û 𝐶 _(s*)_ . 

Denoting û as the unit vector normal to the pass unit vector   at û _s*_ where  (û ·û=0), the end points ⊥ ⊥ of the cross section are: 



The defender’s lateral coordinate relative to the segment is 



**29** 



With 𝑒𝑟𝑓 denoting the Gaussian error function, the line integral of the defender’s Gaussian over   𝑆 𝑗 reduces to a 1D normal integral: 



To ensure comparability across different cross section widths and defender positions, this integral is normalized by its maximum possible value, attained when the defender is standing right in the center of the pass line and  𝑢𝑗 =<sup>𝑊(</sup> 2<sup>𝑠*)</sup> ~~,~~ giving a denominator of 𝑒𝑟𝑓(𝑊(𝑠*) / 2σ). The normalized blocking fraction for defender 𝑑 is then: 𝑗 



A pass is considered blocked if any defender’s normalized Gaussian blocking fraction exceeds a threshold τ = 0. 5: 



### **B.  Overview of Passing Dataset** 

We use  passes from the Big 5 European leagues in the 2024-2025 season to evaluate our pass block models in RQ1. Specifically, we only retain passes that satisfy the following filters: 

- The pass is not a high pass 

- 

   - The pass originates between midfield and the attacking penalty box 

- The pass is progressive (i.e., the x coordinate of the pass end location is ahead of the x coordinate of the pass start location) 

- The end location of the pass and the pass receiver are visible in the 360 frame. 

The Bundesliga had the highest rate of unsuccessful passes while the EPL had the lowest rate of unsuccessful passes. Note that there are 18 teams and 306 games in both Ligue 1 and the Bundesliga, compared to 20 teams and 380 games in the other three leagues. 

**Table B1** : Distribution of ground truth data from Big 5 European leagues in the 2024-2025 season (total 69,500 passes) 

||**EPL**|**Ligue 1**|**Bundesliga**|**La Liga**|**Serie A**|
|---|---|---|---|---|---|
|Total Passes|16,245|12,815|11,935|14,902|13,603|
|Successful<br>Passes|16,102|12,665|11,779|14,719|13,431|
|Unsuccessful<br>Passes|143|150|156|183|172|
|Actual Pass<br>Block Rate|0.88%|1.17%|1.31%|1.23%|1.26%|



**30** 



### **C.  Evaluating the Pass Selection and Pass Success Models** 

Evaluating the performance of a pass selection model is not trivial. We follow the procedure from Robberechts et al. [6], extracting the most likely receiver according to the model and comparing it with the actual receiver. We compare with a naive baseline which always predicts the closest teammate as the receiver, an XGB ranking classifier trained on the same handcrafted features from [6], and our SoccerMap model. Table 2 shows that performances are similar between XGBoost and SoccerMap, and coherent with those reported in [6] where SoccerMap is only slightly less accurate than the feature-based model. 

**Table C1** : Average logloss and accuracy of our SoccerMap pass selection model, an XGBoost ranking classifier and a naive baseline for predicting the pass selection probabilities. 

||**LogLoss**|**Accuracy**|
|---|---|---|
|Closest Teammate|-|0.366|
|XGBoost|-|0.547|
|SoccerMap|6.521|0.536|



We also evaluate our pass success model and report results in Table 3. We again compare with a feature-based XGBoost model trained on the set of handcrafted features from Robberechts et al. Performances are very similar between the two models, and are consistent with the evaluation from [6]. 

**Table C2** : Average performance of our SoccerMap model and an XGBoost classifier for predicting the pass success  probabilities. 

||**Precision**|**Recall**|**F1**|**AUC**|**Brier**|
|---|---|---|---|---|---|
|XGBoost|0.933|0.938|0.935|0.942|0.073|
|SoccerMap|0.923|0.942|0.933|0.937|0.076|



**31** 


