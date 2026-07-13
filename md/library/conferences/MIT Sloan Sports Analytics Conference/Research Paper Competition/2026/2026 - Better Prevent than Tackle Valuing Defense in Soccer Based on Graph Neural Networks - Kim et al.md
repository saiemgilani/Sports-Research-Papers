<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Better Prevent than Tackle Valuing Defense in Soccer Based on Graph Neural Networks - Kim et al.pdf -->

# **Better Prevent than Tackle: Valuing Defense in Soccer Based on Graph Neural Networks** 

Paper Track: Soccer Paper ID: 117 

## **1. Introduction** 

The accurate player evaluation is critical in professional soccer, where players' market values have reached astronomical levels. However, unlike other sports where key performance indicators are more explicitly measurable, soccer lacks clear, frequent, and directly observable metrics that can fully capture a player's contribution [8]. As a result, player evaluation has traditionally relied on subjective assessment made by domain experts, who must watch numerous matches to form qualitative judgments. Despite these efforts, even high-cost player recruitments offer no guarantee of success, highlighting the need for a more quantitative approach. 

With the increasing availability of event and tracking data, research on data-driven player evaluation in soccer has gained traction in recent years [6] [8] [20] [21] [23] [28] [29] [31]. Most studies have focused on valuing on-ball actions, such as passes and shots, by estimating how much each action increases a team's probability of scoring. These methods provide a more consistent and granular assessment of player contributions compared to traditional statistics. 

Even with these advances, existing studies primarily focus on valuing on-ball actions, leaving a fundamental gap in crediting defensive players. Particularly, effective defending is not just about visible actions like interceptions and tackles but also about preventing dangerous offensive events before they happen<sup>1</sup> [33]. For example, if defending players effectively press the ball possessor and enforce the player to pass the ball backward by reducing the success probability of forward plays, their defensive contribution should be recognized even though they do not record any interception or tackle. Conversely, even if a play does not result in a goal, defenders should be penalized if they allow a dangerous pass or shot. Thus, valuing defensive performance is more challenging than its offensive counterpart, as it requires considering not only what defending players did with the ball, but also what they prevented (or conceded) and who should be credited (or blamed) for each. 

Due to these challenges, valuing individual defensive contributions has been relatively underexplored, despite its importance in soccer analytics [13]. Bransen and Van Haaren [6] proposed Joint Defensive Impact (JDI), which compares opponents’ attacking performance when a defender is on the pitch with their expectation, yet its indirect, match-level resolution cannot capture contributions in specific defensive moments. Merhej et al. [22] quantified individual defensive contributions via the potential expected threat (xT) [32] removed by successful defensive actions, but their valuation is limited to interceptions and tackles. Forcher et al. [14] and Toda et al. [34] considered more general defensive situations by modeling the probability of defensive success in the near future, but their evaluations remain at the team level rather than assigning credits to individual players. Stockl et al. [33] analyzed which passing options defenders prevented and how threatening those options were using Graph Convolutional Networks (GCNs) [18], but their analysis 

1 As Paolo Maldini’s saying goes, “If I have to make a tackle, then I have already made a mistake.” 



1 

is qualitative and do not propose a unified metric to compare defensive ability of multiple players. Most recently, Everett et al. [9] introduced an approach based on a Graph Attention Network (GAT) [35] that measures how removing a defender’s attention weights affects the estimated pass success probability. However, they only consider passes and do not account for shots, which play a decisive role in goal-scoring. In addition, the value of a pass is defined simply as the difference of xT [32] between its start and end locations without considering contextual information. 

To address these limitations, we proposed DEFCON ( **DEF** ensive **CON** tribution evaluator), a comprehensive framework that quantifies the individual contributions of defending players across every in-game situation. Using GATs [35], DEFCON estimates the success probability of each available attacking option, the expected value of that option upon its success, and the degree of responsibility each defender bears for defending it. Based on these component values, the framework computes the Expected Possession Value (EPV) at the moment of each on-ball attacking action and interprets the reduction in the attacking tam’s EPV before and after their action as the defending team’s contribution. DEFCON then distributes this team-level defensive value to individual defenders in a principled manner across various scenarios. When an opponent’s action fails, defenders receive credit for having lowered its success probability, with additional credit assigned to the defender who directly wins the ball. When an action succeeds and increases the opponent’s EPV, defenders are penalized for allowing a threatening attack. Conversely, when an action succeeds but decreases the opponent’s EPV, defenders receive credit for deterring more dangerous alternatives and steering the opponent toward a less threatening choice. Through these mechanisms, DEFCON evaluates how much each defender contributes to increasing or decreasing the opponent’s scoring potential in every situation, and these event-level contributions can be aggregated to quantify defensive performance over an entire match or season. 

To validate our framework, we trained the component models using event and tracking data from the 2023–24 Eredivisie season and evaluated their performance on the 2024–25 season. Because no ground-truth labels exist for defensive performance, we assess DEFCON through two indirect criteria: (1) the predictive accuracy of the component models and (2) the correlation between our defensive credit and players’ market values. We find that individual defenders’ time-normalized credit exhibits a significant positive relationship with market value, indicating that it aligns well with domain experts’ general intuition about defensive ability. Notably, the penalties imposed for allowing threatening attacks show a particularly strong correlation: defenders with smaller absolute penalties tend to have higher market values. In contrast, scores derived solely from explicit defensive actions show no positive correlation with market value, underscoring the limitations of action-based defensive evaluation and the added value of our framework. Lastly, we further showcase several practical applications, including in-game timelines of defensive contributions, spatial aggregation across pitch zones, and pairwise summaries of attacker–defender interactions. These examples demonstrate that DEFCON can effectively support scouting, player profiling, and post-match analysis in real-world professional clubs. 

## **2. Framework for Defensive Valuation** 

The fundamental objective of defense in soccer is to reduce the opponent’s probability of scoring. Accordingly, when the opponent’s scoring probability decreases as a result of defensive positioning, defenders should receive positive credit; conversely, when it increases, defenders should be penalized for allowing the opponent’s attack to progress. In this section, we formalize this principle by first describing how to estimate the scoring potential at each game state (Section 2.1) and how to 



2 

define defensive value as the change in this potential (Section 2.2). Then, we define the defender responsibility that serves as a weighting factor for distribute this defensive value to individual defenders (Section 2.3), and introduce specific credit assignment rules under different action types and situations (Sections 2.4 and 2.5). Finally, we explain how these situation-level credits are aggregated across an entire match or season to evaluate each player’s overall defensive contribution (Section 2.6). Figure 1 provides an illustrative overview of how the proposed framework computes and allocates defensive credit in a specific match situation. 



**Figure 1:** Overview of the defensive credit assignment process when conceding a threatening pass. 

### **2.1. Expected Possession Value** 

To quantify the value of defense, we rely on the concept of _Expected Possession Value_ (EPV) introduced in prior work [10] [12], which represents the scoring potential of the attacking team at a given game state. Let 𝑠 denote the state at the -th on-ball attacking action and 𝑘 𝐺 be the random 𝑘 𝑘 variable representing its return, defined as 1 or −1 if the attacking team shortly scores/concedes a goal, and 0 otherwise. Then, EPV of state 𝑠 is defined as the expected return 𝐸𝑆 = 𝑠 . 𝑘 [ 𝑘 𝑘] 

Rather than directly estimating EPV using goal records as the sole supervision signal, we adopt the decomposition approach of Fernandez et al. [10] [12]. Since the ball possessor can attempt to either pass to a teammate, take on an opponent through dribbling, or shoot, we express the EPV as the combination of the probability of selecting each action  and the conditional EPV if  is executed: 𝑎 𝑎 





3 

+ 𝑠ℎ𝑜𝑡 𝑝𝑎𝑠𝑠 + where 𝐴= {𝑣∈𝑉 }<sup>∪{𝑎</sup> } is the set of attacking options containing pass attempts 𝑎𝑣 to 𝑣∈𝑉 + 𝑠ℎ𝑜𝑡 (where 𝑉 is the set of the ball possessor’s teammates) and a shot 𝑎 . If  is the ball possessor, 𝑣 𝑝𝑎𝑠𝑠 then 𝑎 represents dribbling attempt treated as a pass to oneself. 𝑣 

The _action EPV_ 𝐸𝑆 = 𝑠 , 𝐴 = 𝑎 given that the player selects a specific action  is further 𝑎 [ 𝑘 𝑘 𝑘 ] decomposed by conditioning on whether the action succeeds or fails as follows: 



where the outcome 𝑂 of the action in 𝑠 is defined as 1 if it is successful and 0 if failed. 𝑘 𝑘 

In summary, EPV consists of the following three components: 





|**Target**|**Select**<br>**prob. **|**Success**<br>**prob. **|**Success**<br>**EPV**|
|---|---|---|---|
|**Red 0**|0.019|0.476|0.0087|
|Red 1|0.312|0.548|0.0085|
|Red 2|0.222|0.722|0.0087|
|Red 3|0.047|0.259|0.0120|
|Red 4|0.243|0.322|0.0149|
|Red 5|0.010|0.307|0.0113|
|Red 6|0.023|0.763|0.0059|
|Red 8|0.004|0.344|0.0108|
|Red 10|0.023|0.994|0.0042|
|Red 13|0.044|0.616|0.0075|
|Red 15|0.052|0.914|0.0052|





4 



|**Target**|**Select**<br>**prob. **|**Success**<br>**prob. **|**Success**<br>**EPV**|
|---|---|---|---|
|Blue 1|0.000|0.414|0.0053|
|Blue 2|0.000|0.814|0.0130|
|Blue 3|0.006|0.345|0.0114|
|Blue 5|0.789|0.885|0.0186|
|Blue 7|0.001|0.699|0.0103|
|Blue 8|0.000|0.495|0.0083|
|**Blue 9**|0.131|0.460|0.0269|
|Blue 11|0.000|0.814|0.0034|
|Blue 12|0.001|0.569|0.0071|
|Blue 13|0.058|0.415|0.0333|
|Blue 15|0.010|0.543|0.0199|



**Figure 2:** Visualization and tabulation of component values before and after a pass. The red player 0 intended to pass to teammate 1, but the blue player 9 intercepted the pass. The size of each circle denotes the action selection probability, indicating how likely red 0 was to choose that passing option. Also, the annotation above the circle shows the pass success probability, and the color of the circle represents the EPV conditioned on the success of that pass. 

As instantiated in Figure 2, this decomposed formulation enhances interpretability by revealing which attacking options are likely to succeed and how threatening they are if successful. Moreover, it allows these components to be reused in later stages of our framework. Section 3 explains how individual components are estimated using Graph Neural Networks. 

### **2.2. Team-Level Defensive Value** 

Once the EPV at each game state is obtained, we evaluate the defensive impact for the opponent’s each on-ball action by measuring how it changes their EPV. Following Decroos et al. [8], we define the _offensive value_ of the action in state 𝑠 as the change in EPV before and after the action: 𝑘 



A central principle of our framework is that defensive value should serve as the zero-sum counter part of this offensive value. Thus, the defending team’s contribution for an opponent action in 𝑠 is 𝑘 defined as the negated offensive value: 



For example, the red team’s EPV in the left snapshot of Figure 2 is 0.0032, while the blue team’s EPV in the right snapshot becomes 0.0158 after intercepting the pass. From the red team’s perspective, the EPV decreases from 0.0032 to −0. 0158, yielding an offensive value of −0. 0190 for the pass. Conversely, the blue team receives a defensive value of + 0. 0190 for the interception. 



5 

This team-level defensive value captures how much the defending team decreases or allows to increase the opponent’s scoring potential during the opponent action. The following sections detail how this defensive value is assigned to individual defenders according to the action outcome. 

### **2.3. Defender Responsibility** 

To distribute the team-level defensive value defined in Section 2.2 to defending players, we must first quantify how responsible each of them is for defending each attacking option (i.e., a pass to each teammate or a shot). Conceptually, defenders who bear greater responsibility for defending an option should receive more credit if that option fails or is prevented, and should receive a greater penalty if the team concedes it. Therefore, we need a principled measure of such responsibility that can serve as a weighting factor for allocating the defensive value. 

A pass or shot is defined as successful when the ball reaches its intended target (i.e., either a teammate or the goal). Hence, a low success probability for an action implies a high probability that one of the defenders rather than the intended target will receive the ball. In other words, a defender who is more likely to receive the ball if an action  is attempted is effectively reducing the success 𝑎 probability of  through their positioning. Therefore, if  fails or is prevented, defenders with high 𝑎 𝑎 receiver probabilities should be more credited. Conversely, they should be more penalized if  𝑎 succeeds, as they failed to stop  despite their high defensive expectation. 𝑎 

Based on this intuition, we define the _defender responsibility_ 𝑤 (𝑠 , 𝑎) of a defender  for an action  𝑣 𝑎 𝑣 𝑘 as being proportional to the probability 𝑃(𝑅 = 𝑣|𝑆 = 𝑠 , 𝐴 = 𝑎) that  would receive the ball if  𝑣 𝑎 𝑘 𝑘 𝑘 𝑘 were attempted. Because the responsibility values must sum to 1 across all defenders, normalizing these probabilities yield the _failure-conditioned receiver probability_ as follows: 



where 𝑅 denotes the defender who would receive the ball in 𝑠 and 𝑉− is the set of players in the 𝑘 𝑘 defending team. 

This conditional receiver probability represents how likely each defender would intercept or recover the ball given the failure of an action , and it serves as the basis for defensive credit 𝑎 assignment described in the subsequent sections. Section 3.1 details the GNN model used to estimate this responsibility and Figure 7 illustrates the resulting values assigned to players. 

### **2.4. Credit Assignment for Defending Passes** 

When an opponent attempts a pass 𝑎 in 𝑠 , the way of distributing the defensive value depends on 𝑘 𝑘 its outcome. We consider the following five possible outcomes and elaborate on the assignment procedures case by case: 

- (a) the pass fails due to an on-ball defensive action (e.g., interception or tackle), 

- (b) the pass fails without a defensive action (e.g., the ball goes out of play or a player is offside), 

- (c) the pass succeeds and increases the attacking team’s EPV, 

- (d) the pass succeeds but decreases the EPV, and 

- (e) the pass results in a defender’s foul. 



6 

**Pass failure caused by a defensive action:** When a pass 𝑎 fails because a defender successfully 𝑘 performed an on-ball defensive action, the defending team receives a positive defensive value. This value must be distributed not only to the defender who performed the defensive action but also to surrounding defenders whose positioning effectively reduced the success probability of the pass. 

To be specific, let 𝑝= 𝑃(𝑂 = 1|𝑠 , 𝑎 ) denote the estimated success probability of the pass. 𝑘 𝑘 𝑘 Without the defenders, the pass would almost certainly succeed, so its natural success probability would be close to 1. However, the defenders’ positioning lowered this probability from 1 to . The 𝑝 defender who intercepted the pass then eliminated the remaining success probability from  to 0.𝑝 

This observation motivates a decomposition of the defensive value 𝐷𝑠 into two components: ( 𝑘) 

- a fraction 1 −𝑝 of 𝐷𝑠 attributable to defensive positioning that disturbed the pass, ( 𝑘) 

- ● a fraction  of 𝑝 𝐷𝑠 attributable to the defensive action. ( 𝑘) 

The former is distributed to all defenders based on their responsibilities 𝑤 (𝑠 , 𝑎 ) and the latter is 𝑣 𝑘 𝑘 dedicated to the interceptor. As a result, each defender  takes a defensive credit 𝑣 𝐷 𝑠 as follows: 𝑣( 𝑘) 



Notably, the weighting factor 𝑤 (𝑠 , 𝑎 )(1 −𝑝) for defensive positioning can be reduced back to the 𝑣 𝑘 𝑘 receiver probability of the defender  as follows: 𝑣 







**Figure 3:** Visualization of defender responsibility and player-level defensive credit for two passes intercepted by the blue team. The color of each blue circle denotes the defender’s responsibility for defending the corresponding pass, and the text above the circle indicates the defensive credit assigned to the player for contributing to the successful defense. 

For example, in the left snapshot of Figure 3, the estimated success probability of the pass to red player 1 was 0.548 (see also the left snapshot in Figure 2), but the pass failed and yielded a 



7 

defensive value of 0.190 as described in Section 2.2. This value was then distributed to the defending players according to Equation (6). The three players who received the largest credits are: 

- blue 9 (responsibility 0.210): 0. 548⋅0. 190 + 0. 210⋅1( −0. 548)⋅0. 190 = 0. 012, 

- ● blue 5 (responsibility 0.467): 0. 467⋅1( −0. 548)⋅0. 190 = 0. 004, ● blue 15 (responsibility 0.168): 0. 168⋅1( −0. 548)⋅0. 190 = 0. 001. 

**Pass failure without a defensive action:** A pass may also fail without any explicit defensive action, such as when the ball goes out of play or the intended receiver is in an offside position. In such cases, the primary reason for the failed pass is the defending players’ positioning, which reduced the pass success probability and disturbed the ball possessor from completing the pass. Thus, the entire defensive value 𝐷𝑠 is attributed to defenders proportionally to their responsibilities for ( 𝑘) 

defending the pass: 



**Successful pass leading to an increase in EPV:** When a pass 𝑎 is successful and results in an 𝑘 increase in the attacking team’s EPV, a penalty is imposed to the defending team for allowing the ball to move into a more threatening location. In this case, defenders with higher responsibility values had a relatively high probability of intercepting the ball, but the pass eventually succeeded despite their high defensive expectation. Therefore, they should take a larger share of the penalty. Accordingly, like the previous case, we allocate the defensive penalty 𝐷𝑠 (which is negative in this ( 𝑘) case) to defenders proportionally to their responsibilities, as illustrated in Figure 4: 







**Figure 4:** Visualization of defender responsibility and player-level defensive credit for a successful pass and a successful dribble by the red team. The color of each blue circle denotes the defender’s responsibility for defending the corresponding pass, and the text above the circle indicates the penalty imposed to the player for conceding the action. 

**Successful pass leading to a decrease in EPV:** When a pass 𝑎 is completed but results in a 𝑘 decrease in the attacking team’s EPV, the pass itself is typically not a preferred choice for the 



8 

attacking team. Rather, the selection of 𝑎 reflects the defending team’s effective positioning, which 𝑘 has neutralized more threatening alternatives and forced the attacker to select a less valuable option. In such situations, the defending team deserves the positive defensive value 𝐷𝑠 for ( 𝑘) deterring those higher-value options. Because multiple threatening options may exist, this defensive value should then be allocated to individual defenders according to both the relative importance of deterring each option and the defender responsibilities for the option. 

Specifically, we define the set of threatening options in the given state 𝑠 as those that would 𝑘 increase the EPV if successful: 



Before assigning defender-level credits, we divide the team-level defensive value 𝐷𝑠 across the ( 𝑘) + threatening options 𝑎∈𝐴 according to their relative importance. Intuitively,  receives a higher 𝑎 𝑘 share 𝐷𝑠 , 𝑎 when (i) its successful completion would substantially raise the EPV, and (ii) ( 𝑘 ) defenders have significantly reduced its success probability, resulting in a much lower action EPV + 𝐸𝑠 , 𝑎 . That is, we assign a defensive value 𝐷𝑠 , 𝑎 for deterring each threatening option 𝑎∈𝐴 [ 𝑘 ] ( 𝑘 ) 𝑘 proportionally to the potential increase in the EPV conditioned its success: 



+ and assign 𝐷𝑠 , 𝑎<sup>=0</sup> for non-threatening options 𝑎∉𝐴 . ( 𝑘 ) 𝑘 

Once we obtain the defensive value 𝐷𝑠 , 𝑎 for deterring each option , we distribute it to 𝑎 ( 𝑘 ) individual defenders. As discussed in Section 2.3, we use the defender responsibility 𝑤 (𝑠 , 𝑎) as a 𝑣 𝑘 weighting factor to compute the contribution 𝐷 𝑠 , 𝑎 of defender  to deterring  as follows: 𝑣 𝑎 𝑣( 𝑘 ) 



+ Consequently, aggregating 𝐷 𝑠 , 𝑎 across the threatening options 𝑎∈𝐴 yields the overall defensive 𝑣( 𝑘 ) 𝑘 credit 𝐷 𝑠 assigned to  in the given situation 𝑣 𝑠 : 𝑣( 𝑘) 𝑘 



**Foul committed by a defender:** When the defending team commits a foul, the next on-ball attacking action becomes a free kick or a penalty kick granted to the attacking team. In such cases, the defensive value 𝐷𝑠 is the change in EPV between the current state and the set-piece state that ( 𝑘) immediately follows the foul. Because the foul results from the action of a single defender, the entire defensive penalty is exclusively assigned to the player who committed the foul, i.e., 𝐷 𝑠<sup>=𝐷𝑠</sup> 𝑣( 𝑘) ( 𝑘)<sup>.</sup> 



9 

For example, since we uniformly set the EPV for all penalty kicks to 0.7884, a player who commits a foul resulting in a penalty kick is penalized by 𝐸𝑠<sup>−0. 7884</sup> . [ 𝑘] 

### **2.5. Credit Assignment for Defending Shots** 

As in the case of passes descried in Section 2.4, the allocation of defensive value for shots depends on the outcome of the attempt. Unlike the conventional definition that regards a shot as successful only when it results in a goal, we define the success of a shot as not being blocked by an outfield player. This definition reflects the fundamentally different defensive roles of outfield players and goalkeepers: the former primarily aims to block shots, whereas the latter is responsible for saving unblocked shots in front of the goal. Accordingly, we treat the defensive effort of blocking a shot in parallel with the interception of a pass, and distinguish two possible shooting outcomes: the shot is blocked or not blocked by an outfield player. 

**Blocked shot:** A blocked shot is treated in the same manner as a pass intercepted by a defender, as both situations involve a defender stopping the ball from reaching its intended target through direct intervention in the ball’s trajectory. Therefore, the defensive value 𝐷𝑠 is distributed following the ( 𝑘) same principle as in Equation (6), with the only difference being that 𝑝= 𝑃(𝑂 = 1|𝑠 , 𝑎 ) now 𝑘 𝑘 𝑘 𝑠ℎ𝑜𝑡 denotes the probability that the shot 𝑎 = 𝑎 is not blocked. 𝑘 

**Unblocked shot:** When a shot is not blocked by an outfield player, the attacking team’s EPV diverges significantly depending on whether the shot results in a goal. If the attacking team scores, their EPV rises sharply to 1. Otherwise, it typically decreases, except in situations where the attacking team immediately obtains a rebound shooting opportunity. 

Regardless of this divergence, failing to block the shot already constitutes a defensive fault from the outfield defenders’ perspective. That is, it means that they have allowed the ball to reach the goal area, thereby failing in their primary defensive duty. Thus, they should receive a penalty independent of whether the shot leads to a goal. 

To quantify this penalty, we compare the attacking team’s current EPV 𝐸𝑠 with the _unblocked-shot_ [ 𝑘] _expected goal_ (UxG) defined as 



which represents the scoring probability if a shot would not be blocked. The difference between these two values (which is typically negative) is distributed among the outfield defenders in 𝑠ℎ𝑜𝑡 proportion to their responsibilities 𝑤 𝑠 , 𝑎 : 𝑣( 𝑘 ) 



Because these responsibilities reflect the likelihood that each defender would have been the blocker if the shot had been blocked, the goalkeeper receives zero responsibility weight. 

The goalkeeper’s credit, in contrast, depends on the consequence of the unblocked shot. If the shot is off target and requires no goalkeeper intervention, the goalkeeper 𝑣 receives zero credit. If the 𝐺𝐾 



10 

shot is on target, 𝑣 receives 𝑈𝑠<sup>−𝐸𝑠</sup> , which may be positive or negative depending on the 𝐺𝐾 ( 𝑘) [ 𝑘+1] subsequent event. Specifically, if 𝑣 saves the shot and transitions the game into a state with a 𝐺𝐾 smaller 𝐸𝑠 , they obtain positive credit for the save. Conversely, if the save leads to a more [ 𝑘+1] dangerous rebound opportunity, then 𝐸𝑠 may exceed 𝑈𝑠 , yielding a negative credit (penalty). [ 𝑘+1] ( 𝑘) If the shot results in a goal, then 𝐸𝑠<sup>=1</sup> , imposing the goalkeeper a large penalty of 𝑈𝑠<sup>−1</sup> . [ 𝑘+1] ( 𝑘) In summary, the credit for the goalkeeper is 







**Figure 5:** Visualization of defensive credit assignment in unblocked-shot situations. The left and right snapshots show examples of a shot off target and a saved shot on target, respectively. Circle colors for the defending team represent each defender’s responsibility for defending the shot, and the text above each circle indicates the defensive credit or penalty. 



11 

Figure 5 instantiates how defensive credit is assigned in unblocked-shot situations. In the left snapshot, the attacking team’s EPV before the shot was 0.024, while its UxG was 0.121. This means that the defenders allowed the situation to reach a state in which the scoring probability was 0.121, so they share a penalty of 0. 024 −0. 121 =−0. 097 according to their individual responsibilities. 

In the right snapshot, the EPV before the shot was 0.035 and the UxG was 0.069. As in the previous case, the defenders incur a penalty of 0. 035 −0. 069 =−0. 034 for failing to block the shot. However, in this example the shot was on target and the goalkeeper saved it. Therefore, the goalkeeper receives positive credit of 0.069 for reducing the scoring probability from 0.069 to 0. 

Through this formulation, our framework assigns meaningful penalties to defenders even for non-goal shots, which occur far more frequent than shots resulting in goals. This enables us to better quantify the defender’s ability to prevent dangerous shooting opportunities before they develop. 

### **2.6. Aggregating Defensive Contributions Across Matches** 

The situation-level defensive credits defined in the previous subsections can be aggregated over an entire match or season to evaluate each player’s overall defensive contribution. For interpretability, we group these credits into four categories: 

- (a) Intercept: credit for directly winning the ball through on-ball defensive actions, 

- (b) Disturb: credit for inducing the failure of the opponent’s attack by lowering its success probability through effective positioning, 

- (c) Deter: credit for deterring more threatening attacking options when the opponent completes a less valuable action that reduces their EPV, and 

- (d) Concede: penalty for allowing threatening attacks that increase the opponent’s EPV. 

Figure 6 shows the aggregated credits for defenders in a match where the home team defeated the away team 5–0. Because the home team dominated possession, the away defenders were involved in many on-ball defensive actions such as interceptions and tackles and consequently accumulated large on-ball credits (blue bars). However, they also conceded many threatening attacks, leading to far larger penalties (red bars), which ultimately produced substantially lower net credits (purple bars) compared to the home defenders. 

This example underscores a key limitation of existing evaluating metrics that rely solely on on-ball defensive actions. That is, they can misleadingly suggest that the away defenders performed better simply because they executed more on-ball defensive actions. In contrast, our framework appropriately penalizes defenders for allowing dangerous situations, yielding a more reliable and comprehensive assessment of defensive performance. 



12 



**Figure 6:** Category-wise and net defensive credits aggregated per 90 minutes for each defender in a given match. The numbers at the top indicate the final score, where the home team defeated the away team 5–0. 

## **3. Estimation of Component Values** 

To implement the credit assignment framework introduced in Section 2, we must estimate the following underlying component values: 



Because player movement patterns differ substantially between passes and shots, we estimate the action success probability separately for the two action types, namely, the _pass success probability_ 𝑃𝑠 , 𝑎𝑝𝑎𝑠𝑠 and the _shot success probability_ 𝑃𝑠 , 𝑎𝑠ℎ𝑜𝑡 As we define the success of a shot as not ( 𝑘 𝑣 ) ( 𝑘 )<sup>.</sup> being blocked by an outfield player, we calculate the shot success probability by estimating the _shot_ 𝑠ℎ𝑜𝑡 _blocking probability_ 𝑃𝑠 , 𝑎 and subtracting it from 1. ( 𝑘 ) 

Outcome-conditioned EPV also requires separate modeling for passes and shots. For passes, we follow existing approaches [8] [31] that decomposes the conditional EPV into _goal-scoring_ and _goal-conceding probabilities_ and estimate them independently: 



For shots, we treat the EPV for a blocked shot as zero, while for unblocked shots we adopt the 𝑠ℎ𝑜𝑡 _unblocked-shot expected goal_ 𝑈𝑠<sup>=𝑃𝑠</sup> , 𝑂 = 1 introduced in Section 2.5: ( 𝑘) ( 𝑘<sup>, 𝑎</sup> 𝑘 ) 



13 

**Table 1:** Summary of predictive tasks for estimating the component values, including how each task is formulated within the GNN architecture, which action types and labels are used for training. 

|**Task**|**Output activation**|**Output size**|**Pass**|**Dribble**|**Shot**|**Supervision label**||
|---|---|---|---|---|---|---|---|
|(a1) Action selection|Softmax over<br>teammate nodes|1 per node|✓|✓|✓|Actual action taken||
|(b1) Pass success|Node-wise<br>sigmoid|1 per node|✓|✓||Whether the selected pass<br>succeeded||
|(b2) Shot blocking|Average pooling<br>and sigmoid|1 per graph|||✓|Whether the shot was<br>blocked||
|(c1) Goal-scoring|Node-wise|2  d|✓|✓||Whether the actual action<br>d t ld t htl||
|(c2) Goal-conceding|sigmoid|per noe|✓|✓||an oucome e o sory<br>scoring/concedingagoal||
|(d1) Responsibility|Softmax over<br>opponent nodes|1 per node|✓(|failed acti|ons)|Actual receiver of the action||
||𝐸<br>⎡⎢⎣|𝑠𝑘, 𝑎<br>𝑠ℎ𝑜𝑡, 𝑂𝑘|= 1<br>⎤⎥⎦|= 𝑈𝑠𝑘<br>( )<sup>,</sup>|<sup>𝐸𝑠</sup>𝑘<sup>,</sup><br>⎡⎢⎣|<sup>𝑎</sup><br>𝑠ℎ𝑜𝑡, 𝑂𝑘= 0<br>⎤⎥⎦= 0.|(18)|



In summary, our framework trains separate predictive models for the following component values: 



Except for UxG (c3), we employ Graph Neural Networks (GNNs) as in previous studies [3] [9] [27] [30] [33] [36] [37] to effectively model complex interactions among multiple players. In contrast, UxG is modeled using a logistic regression mainly based on shot location to leverage publicly available event data [24] that contains much more shots than the tracking dataset used in this study. The following subsections describe the training procedures for these tasks in detail. 

### **3.1. Graph Neural Network Models** 

For each on-ball attacking action, we construct a fully connected graph 𝐺= (𝑉, 𝐸) in which all players on the pitch and two goals are represented as nodes 𝑣∈𝑉, with every pair of nodes connected by an edge 𝑒∈𝐸. Inspired by earlier studies [2] [11] [19] [29] [30] [31] on contextual analysis using tracking data in soccer, we represent each node with 25 node features as follows: 

- four binary attributes: indicators for whether the node corresponds to the ball carrier, a teammate of the ball carrier, a goalkeeper, and a goal. 

- six running features: the node’s (𝑥, 𝑦) location, (𝑥, 𝑦) velocity, speed, and acceleration. 

- three relative features to the goal: the distance to the defending team’s goal and the sine and cosine of the angle between the node-goal line and the x-axis (i.e., the lower sideline). 



14 

- six ball-related features: the height of the ball (shared across all nodes), the distance to the ball, the sine and cosine of the angle between the node-ball line and the x-axis, and the sine and cosine of the angle between the node’s velocity and the ball carrier’s velocity. 

- four opponent-context features: the distance to the nearest opponent, the number of opponents within a 3m radius of the node, the number of opponents closer to their goal than the node, and the number of opponents inside the triangular region formed by the node and the opposing team’s two goalposts. 

- two passing-line features: the distance from the potential passing line to its nearest opponent and the number of opponents in a 10m-wide corridor around the passing line, where the passing line is the line segment between the ball possessor and the node. 

We additionally include two edge features: for each pair of nodes: the Euclidean distance between them and a binary indicator for whether they belong to the same team. 

Because each component value requires a distinct prediction target, we train a separate Graph Attention Network (GAT) model [35] for the task. All models take the above graph  represented by 𝐺 |𝑉|×25 |𝐸|×2 the node features 𝑋∈𝑅 and the edge features 𝐸∈𝑅 as input and produce node embeddings 𝐻= ℎ by two layers of GAT convolution: ( 𝑣) 𝑣∈𝑉 



where their output structures and supervision labels differ by task. Table 1 summarizes these differences, and the following paragraphs describe each model in more detail. 

**(a1) Action selection:** This task aims to predict the node to which the ball possessor will attempt to send the ball. Since the ball possessor does not intend to pass to an opponent, we apply 

+ node-wise MLPs  and a softmax only to the node embeddings ϕ 𝐻 = (ℎ𝑣) + of the ball possessor’s 𝑣∈𝑉 

teammates and the target goal: 



^<sup>+</sup> ^ = The output values 𝑦 (𝑦𝑣)𝑣∈𝑉+ represent the probabilities of passing (or shooting) to the 

^ candidate nodes, satisfying ∑𝑦<sup>1</sup> . The model is trained using cross-entropy loss against the 𝑣<sup>=</sup> 𝑣∈𝑉+ one-hot vector of the true attempt. 

To correctly supervise the model, we need to identify the intended receivers of failed passes, since their observed receivers are opponents. Following the approach of previous studies [25] [31], we treat the teammate closest to the endpoint of a failed pass  in terms of distance and angle as its 𝑎 intended receiver. That is, we find the teammate  that maximizes the following score: 𝑣 





15 

where 𝐷𝑖𝑠𝑡𝑎, 𝑣( ) denotes the distance between the endpoint of  and the location of the teammate  𝑎 𝑣 at the moment of reception, and 𝐴𝑛𝑔𝑙𝑒𝑎, 𝑣( ) is the angle between the passing line of  and the line 𝑎 connecting the passer and . 𝑣 

**(b1) Pass success:** We independently apply a node-wise MLP  and a sigmoid activation  to each ϕ σ node embedding to produce the probability that the associated action would succeed if attempted: 



^ During training, we focus only on the probability 𝑦 ∈𝑅 for the observed pass 𝑣 , and the model is 𝑣 𝑘 𝑘 supervised using binary cross-entropy against whether that action succeeded or failed. 

**(b2) Shot blocking:** Unlike the previous tasks, predicting whether a shot attempt in the given state will be blocked is modeled as a graph classification task. Instead of producing node-wise logits, the GAT aggregates node embeddings through average pooling to obtain a single graph embedding ℎ . 𝐺 ^ Then, it estimates a shot blocking probability 𝑦 ∈𝑅 through an MLP  with a sigmoid activation : ψ σ 



The model is trained using binary cross-entropy against whether the shot is actually blocked. 

A key challenge in this task is that players rarely attempt shots when they expect them to be blocked, so training only on observed shots underestimate the true blocking probability. To address this issue and the inherent scarcity of shots in the dataset, we augment the training data by treating certain passes as proxy failed shots. Specifically, we include passes occurring in regions with UxG greater than 0.05 and with a defender positioned between the ball possessor and the goal. 

**(c1 & c2) Outcome-conditioned goal-scoring/conceding:** Estimating the outcome-conditioned goal-scoring probability is formulated as a node classification task in which each node 𝑣∈𝑉 ^+ ^− produces two probabilities (𝑦 , 𝑦 ): one representing the probability that the team will shortly 𝑣 𝑣 scores a goal if the pass to  succeeds, and the other corresponding to the probability if it fails. 𝑣 



During training, we focus only on the node 𝑣 corresponding to the executed action and select one of 𝑘 its two probabilities associated with its observed outcome. The selected probability is then compared using binary cross-entropy against the ground-truth indicator of whether the attacking team scores within the next ten events [8] [31]. A parallel procedure is used to estimate the outcome-conditioned goal-conceding probability, with the ground truth indicating whether the current attacking team concedes a goal within the next ten events. 



16 



**Figure 7:** Illustration of the defender responsibility estimation model. Each left panel shows an input graph conditioned on a hypothetical pass. A binary indicator is added to the node features, where only the highlighted node is assigned a value of 1 and all others are assigned 0. The right panels display the corresponding model outputs, where the blue-team nodes are colored and annotated according to their predicted responsibilities for defending the pass to the highlighted node. 

**(d1) Defender responsibility:** We model the task of predicting which defending player would receive the ball if a given pass or shot were to fail. This corresponds to selecting one receiver node conditioned on the specific action being attempted and its failure, as illustrated in Figure 7. To encode this conditioning, we extend the original 25 node features with an additional binary indicator specifying the action of interest, assigning 1 to the node  corresponding to the intended 𝑢 receiver (or goal) and 0 to all other nodes. The GAT processes the graph with these extended node * |𝑉|×26 features 𝑋 = 𝑋; 𝑒<sup>∈𝑅</sup> and produces node-wise logits. A softmax is then applied over the 𝑢 [ 𝑢] logits of the defending players 𝑣∈𝑉− to yield a probability distribution representing their ^ responsibilities (𝑦𝑢,𝑣)𝑣∈𝑉− for defending the given action : 𝑣 



− where 𝐻𝑢 = (ℎ𝑢,𝑣) − denotes the node embeddings of the defending players. The model is trained 𝑣∈𝑉 using only failed passes and blocked shots. For each instance, we construct the graph with the 



17 

appropriate action-indicator feature, and train the model using cross-entropy against the identity of the defender who actually intercepted or blocked the action. 

### **3.2. Unblocked-Shot Expected Goals Model** 

Because shots and goals occur infrequently during the match, the dataset used in this study does not provide enough samples to reliably train an Expected Goals (xG) [1] [15] model. However, estimating the xG of unblocked shots (c3) does not need to account for the possibility of the shot being blocked, and therefore does not depend on contextual information about surrounding players. This allows us to train the model using external event data with sufficient shot volume. 

To this end, we utilize the Wyscout open event dataset [24], from which we extract shot features and labels from shots recorded in 1,941 matches. The dataset includes 45,945 shot attempts, where 34,987 were unblocked and 5,105 resulted in goals. We train a logistic regression model using six shot features: the (𝑥, 𝑦) location relative to the goal, the distance and angle to the goal, and binary indicators for whether the shot was taken from a set-piece and was a header. 

## **4. Experiments** 

Since there is no ground truth measure of players’ defensive ability, we evaluate the proposed DEFCON through several complementary approaches. First, Section 4.2 compares the predictive accuracy of the component GAT models against other baseline models. Also, Section 0 analyzes the correlation between players’ aggregated defensive scores with their market values. Section 4.4 further provides qualitative validation by inspecting which players rank highest and comparing these rankings with market-value rankings. The datasets used in all experiments are described in Section 4.1. 

### 4.1. **Datasets** 

In this study, we utilize optical tracking data and event data collected from 564 matches of the 2023–24 and 2024–25 seasons of Dutch Eredivisie, provided by AFC Ajax. The tracking data contains player and ball positions sampled at 25Hz, while the event data consists of approximately 1,400 manually annotated on-ball actions per match. Since manually recorded event timestamps contain temporal inaccuracies, we synchronize all events with the tracking data using ELASTIC [17]. 

To examine how well the models generalize across different seasons, we use the 2023–24 season data to train all component models and evaluate them on the 2024–25 season. We consider passes, dribbles, and shots across both open play and set-piece situations for model training, with each model utilizing a different subset of actions. Note that although different subsets are used for training, all models are applied to every pass, dribble, and shot event in the test set, since EPV computation and defensive credit assignment requires component values for every possible attacking option. Table 2 describes the detailed statistics on the dataset. 

**Table 2:** The number of actions used in each predictive task and the number of matches shared across all tasks. The term ‘action’ encompasses pass, dribble, and shot. 

|**Task**|**Action type**|**Training**|**Validation**|**Test**|**% Positive**|
|---|---|---|---|---|---|
|(a1) Action selection|Action|200,255|81,650|286,696|–|
|(b1) Pass success|||||76.80%|
|(c1) Goal-scoring|Pass & dribble|194,680|79,433|279,328|1.59%|
|(c2) Goal-conceding|||||0.63%|





18 

||Real shot|5,575|2,217|7,368|26.20%|
|---|---|---|---|---|---|
|(b2) Shot blocking|Augmented<br>shot|3,773|1,552|0|100%|
|(d1) Responsibility|Failed action|36,782|14,947|50,984|–|
|# Matches|–|200|81|283|–|



### 4.2. **Predictive Performance of Component Models** 

To evaluate the predictive performance of the component models used in DEFCON, we compare our GAT-based models with both GNN (GCN [18] and GIN [38]) and gradient-boosting (XGBoost [7] and CatBoost [26]) baselines. The applicable baselines differ by task due to differences in problem formulation. Pass success prediction (b1), shot-blocking prediction (b2), and outcome-conditioned goal-scoring (c1) and goal-conceding (c2) prediction are binary classification tasks, so they can be implemented using either GNNs or tabular boosting models. In contrast, action selection prediction (a1) and defender responsibility estimation (d1) require selecting one node among many, where boosting models cannot directly support. Therefore, we only compare GNN variants for these tasks. 

For boosting models, we replace the graph input with tabular feature vectors. In pass-related tasks (b1, c1, c2), we construct input vectors by concatenating the the node features of the ball carrier and the intended receiver. For shot-blocking (b2), we use only the ball carrier’s node features. 

Table 3 reports the resulting performance in terms of F1-score, AUC, and Brier score for binary classification tasks (b1, b2, c1, c2), and accuracy, cross entropy (CE), and mean reciprocal rank (MRR) for multi-class classification tasks (a1, d1). Overall, GAT outperforms all GNN variants and is the strongest model for pass success prediction (b1) across all methods. Its superior performance reflects the power of attention-weighted message-passing, which enables the model to modulate the influence of surrounding players. Pass success prediction benefits from abundant training data and minimal class imbalance, allowing GAT to fully leverage relational information and outperform both GNN baselines and boosting models. 

Interestingly, boosting models outperform GNNs on the shot-blocking prediction (b2) and goal prediction (c1, c2) tasks, for different potential reasons. For shot-blocking, GNN models treat the task as a graph classification problem, which requires aggregating node embeddings via average pooling. This inevitably discards some relational information and places GNNs at a structural disadvantage compared to boosting models. Meanwhile, the goal prediction tasks suffer from extreme class imbalance, making it difficult for GNNs to learn stable relational patterns. 

Despite these limitations, GNNs achieve Brier scores comparable to boosting models across all tasks, indicating that they still produce well-calibrated probability estimates. Such calibration quality is important, since our objective is not simply to classify outcomes, but to reliably estimates underlying probabilities for accurate EPV computation and credit assignment. Given these considerations, and to maintain architectural consistency across all component models, we adopt GAT as the unified model architecture in all subsequent experiments and applications. 

**Table 3:** Performance of component model variants. 

|**Task**|**Metric**|**XGBoost**|**CatBoost**|**GCN**|**GIN**|**GAT**|
|---|---|---|---|---|---|---|
|ll|Accuracy|–|–|0.6080|0.6119|**0.6738**|
|(a1, muti-cass)<br>Ati lti|CE|–|–|1.1003|1.0925|**0.9239**|
|con seecon|MRR|–|–|0.7555|0.7581|**0.7996**|





19 

|b1 bi|F1|0.9059|0.9060|0.9104|0.9105|**0.9115**|
|---|---|---|---|---|---|---|
|(, nary)<br>Pass success|AUC|0.9124|0.9115|0.9149|0.9151|**0.9167 **|
||Brier|0.0980|0.0984|0.0942|0.0941|**0.0933**|
|b2 bi|F1|0.4485|**0.4491**|0.4232|0.4117|0.3984|
|(, nary)<br>Shot blockin|AUC|0.6845|**0.6896**|0.6373|0.6402|0.6717|
|g|Brier|0.2070|**0.2014**|0.2313|0.2268|0.2037|
|1 bi|F1|0.0884|**0.0951**|0.0780|0.0721|0.0759|
|(c, nary)<br>Goal-scorin|AUC|0.6873|**0.7056**|0.6823|0.6818|0.6834|
|g|Brier|0.0149|0.0149|**0.0148**|**0.0148**|**0.0148**|
|2 bi|F1|**0.0070**|0.0000|0.0000|0.0000|0.0000|
|(c, nary)<br>Goal-concedin|AUC|0.6030|**0.6478**|0.6168|0.6174|0.6172|
|g|Brier|**0.0031**|**0.0031**|0.0032|0.0032|0.0032|
|d1 lil|Accuracy|–|–|0.2439|0.2361|**0.5021**|
|(, mut-cass)<br>Resonsibilit|CE|–|–|2.3282|2.3399|**1.4036**|
|py|MRR|–|–|0.4868|0.4792|**0.6940**|



### 4.3. **Correlation with Market Values** 

To check how well the proposed defensive credit reflects players’ actual defensive ability, we examine its correlation with players’ market values. Specifically, we consider 261 outfield players from Eredivisie 2024–25 who played at least 900 minutes and compute each player’s average defensive credit per 90 minutes. Market values are collected from Transfermarkt<sup>2</sup> at the end of the season and transformed into log scale to mitigate the heavy-tailed distribution, where a small number of star players exhibit disproportionately higher valuations. 

We analyze correlations for three types of defensive scores: 

- (a) Intercept: positive credits earned through on-ball defensive actions such as intercepting passes (including tackling against dribbles treated as self-passes) or blocking shots, 

- (b) Concede: penalties incurred from conceding threatening attacks or committing fouls, and (c) Net credit: the total credit across all types of defense. 

To better understand positional differences, we report correlations both across all players and within major positional groups: defenders (DF), midfielders (MF), and forwards (FW), with the corresponding scatterplots shown in Figure 8. We further analyze three defensively oriented sub-positions: center-backs (CB), side-backs (SB), and central/defensive midfielders (CM), as visualized in Figure 9. Table 4 summarizes the Pearson correlation coefficients against the log-scale market values against these groups. 

**Table 4:** Pearson correlation coefficients between defensive credits and log-scale market values for regular players in Eredivisie 2024–25. Coefficients greater than 0.5 are highlighted in bold. 

|**Role**|**Plaers**||**Intercept**|||**Con**|**cede**||**Net**|
|---|---|---|---|---|---|---|---|---|---|
||**y**|**Pass**|**Shot**|**Total **|**Pass**|**Shot**|**Foul **|**Total **|**credit**|
|Total|261|–0.159|–0.242|–0.204|0.442|0.217|0.098|0.344|0.383|
|DF|99|–0.220|–0.317|–0.317|**0.665**|0.272|0.133|**0.545**|0.451|
|MF|132|–0.131|–0.175|–0.157|**0.605**|0.169|0.008|0.425|0.346|
|FW|30|–0.329|–0.230|–0.193|0.481|0.074|0.087|0.333|0.229|
|CB|46|–0.497|–0.447|–0.596|**0.752**|**0.643**|0.059|**0.754**|**0.563**|
|SB|53|–0.110|–0.281|–0.235|**0.600**|0.123|0.214|**0.518**|0.360|



> 2 <u>https://www.transfermarkt.com</u> 



20 



<!-- Start of picture text -->
CM  66 –0.311  –0.287  –0.344  0.755 0.274  0.158 0.621  0.337<br><!-- End of picture text -->







**Figure 8:** Relationships between category-wise defensive credits and log-scale market values for all regular players in Eredivisie 2024–25, with points and trend lines color-coded by major positional group. 







**Figure 9:** Relationships between category-wise defensive credits and log-scale market values for defensively orientied positions in Eredivisie 2024–25, with points and trend lines color-coded by positional subgroup. 



21 

Across all players, net defensive credit exhibits a clear positive correlation with market value, and this relationship becomes stronger for more defensively oriented roles. In particular, center-backs show a strong correlation of 0.563, indicating that our metric effectively captures aspects of defensive quality reflected in the real-world market. 

In contrast, credits obtained from on-ball defensive actions display a negative correlation with market value. This counter-intuitive trend reflects a fundamental limitation of existing action-based defensive evaluation: players on weaker teams naturally face more defensive situations and therefore become overestimated by accumulating more on-ball defensive actions. This underscores the value of our approach, which rewards not only direct defensive actions but also the prevention of conceding threatening attacks. 

Notably, penalties for conceding threatening attacks show the strongest alignment with market value among all components. Across every positional group, players with smaller absolute penalties (i.e., those who allow fewer dangerous attacks) tend to have higher market valuations. Correlations for all defensive roles (DF, CB, SB, and CM) exceed 0.5, with center-backs showing a particularly high correlation of 0.754. Interestingly, pass-conceding penalties are highly informative across all positions, whereas shot-conceding penalties show a strong correlation only for center-backs. This aligns with common intuition that center-backs bear primary responsibility for defending shots, while defending passes is a shared duty across positions. Overall, these results demonstrate that preventing opponents’ dangerous actions is far more important than performing many on-ball defensive actions (summarized as “better prevent than tackle”). 

### 4.4. **Qualitative Validation Through Player Rankings** 

Beyond the correlation analysis, we also conduct a qualitative inspection of which players appear at the top of each defensive metric. Tables 5–7 list the top-10 center-backs according to net credit, defensive action (“intercept”) credit, and conceding penalty, respectively. The rightmost column reports each player’s Transfermarkt market value, with the number in parentheses indicating their rank among the 46 center-backs who played at least 900 minutes in the 2024–25 season. 

The results are consistent with our earlier findings. For net credit (Table 5), 7 of the top-10 players are also ranked within the top-10 by market value, suggesting strong alignment between our metric and practitioners’ valuation. A similar pattern appears for conceding penalties (Table 7), where high-value players tend to cluster near the top. In contrast, players ranked highly by defensive action credit (Table 6) generally have low market values. They accumulated many interceptions or tackles because their teams were exposed to more dangerous situations, emphasizing that values obtained from observed actions alone do not reliably represent individual defensive ability. 

While market value is influenced by many confounding factors such as age, nationality, and contract length, it nevertheless correlates with overall perceived ability, making it a useful indirect validation signal. In practical settings, clubs can leverage DEFCON’s metrics to automatically filter players who exceed certain thresholds in desired defense categories, substantially narrowing scouting pools. Instead of manually reviewing large numbers of players, analysts can focus their time on a targeted shortlist identified through our trustworthy defensive valuation. 

**Table 5:** Top-10 center-backs ranked by net defensive credit. 

|**Rank**|**Team**|**Player**|**Intercept**|**Concede**|**Net credit**|**Market value**|
|---|---|---|---|---|---|---|
|1|PSV Eindhoven|O. Boscagli|0.1165|–0.1511|0.0464|€20.0m (3)|





22 

|2|Sparta Rotterdam|M. Young|0.1778|–0.2756|0.0434|€2.5m (14)|
|---|---|---|---|---|---|---|
|3|PSVEindhoven|R. Flamingo|0.1153|–0.2200|–0.0027|€20.0m (3)|
|4|Ajax Amsterdam|Y. Baas<br>|0.0848|–0.1872|–0.0056|€12.0m (5)|
|5|Ajax Amsterdam|J.Šutalo|0.1304|–0.2335|–0.0098|€24.0m (2)|
|6|Feyenoord Rotterdam|T. Beelen|0.1114|–0.2063|–0.0110|€8.0m (8)|
|7|AZ Alkmaar|Alexandre Penetra|0.1507|–0.2774|–0.0110|€9.0m (7)|
|8|FC Twente|A. Van Hoorenbeeck|0.1838|–0.3184|–0.0174|€0.8m (30)|
|9|FC Twente|M. Bruns|0.1399|–0.2818|–0.0278|€2.5m (14)|
|10|FC Twente|M. Hilgers|0.0762|–0.2127|–0.0290|€6.5m (9)|



**Table 6:** Top-10 center-backs ranked by “intercept” credit (i.e., highest credits from defensive actions). 

|**Rank**|**Team**|**Player**|**Intercept**|**Concede**|**Net credit**|**Market value**|
|---|---|---|---|---|---|---|
|1|Almare City FC|J. Jacobs|0.2281|–0.4539|–0.0907|€350k (43)|
|2|RKC Waalijk|R. Van Eijma|0.2165|–0.4652|–0.1090|€450k (40)|
|3|NAC Breda|L. Greiml|0.2155|–0.4469|–0.0970|€2,000k (19)|
|4|RKC Waalijk|D. Van den Buijs|0.2059|–0.4995|–0.1598|€500k (37)|
|5|Heracles Almelo|I. Mesík|0.1932|–0.3921|–0.0770|€1,300k (24)|
|6|GoAheadEagles|G.Nauber|0.1855|–0.4042|–0.0978|€400k (41)|
|7|FC Twente|A. Van Hoorenbeeck|0.1838|–0.3488|–0.0174|€800k (30)|
|8|HeraclesAlmelo|D. Mirani|0.1807|–0.3462|–0.1081|€650k (35)|
|9|SC Heerenveen|S. Kersten|0.1787|–0.2756|–0.0579|€1,000k (26)|
|10|Fortuna Sittard|S. Adewoye|0.1781|–0.4138|–0.0500|€1,300k (24)|



**Table 7:** Top-10 center-backs ranked by “concede” credit (i.e., lowest penalties for allowing attacks). 

|**Rank**|<br>**Team**|**Player**|**Intercept**|**Concede**|**Net credit**|**Market value**|
|---|---|---|---|---|---|---|
|1|PSV Eindhoven|O. Boscagli|0.1165|–0.1511|0.0464|€20.0m (3)|
|2|Ajax Amsterdam|Y. Baas|0.0848|–0.1872|–0.0056|€12.0m (5)|
|3|Feyenoord Rotterdam|T. Beelen|0.1114|–0.2063|–0.0110|€8.0m (8)|
|4|FC Twente|M. Hilgers|0.0762|–0.2127|–0.0290|€6.5m (9)|
|5|PSV Eindhoven|R. Flamingo<br>|0.1153|–0.2200|–0.0027|€20.0m (3)|
|6|Ajax Amsterdam|J.Šutalo|0.1304|–0.2335|–0.0098|€24.0m (2)|
|7|Sparta Rotterdam|M. Young|0.1778|–0.2756|0.0434|€2.5m (14)|
|8|AZ Alkmaar|Alexandre Penetra|0.1507|–0.2774|–0.0110|€9.0m (7)|
|9|FC Twente|M. Bruns|0.1399|–0.2818|–0.0278|€2.5m (14)|
|10|FC Utrecht|M. Van der Hoorn|0.1206|–0.2875|–0.0529|€1.0m (26)|



## **5. Practical Applications** 

To illustrate how DEFCON can support real-world analysis in professional clubs, this section showcases several practical applications that leverage its defensive valuations across temporal (Section 5.1), spatial (Section 5.2), and relational (Section 5.3) dimensions. 

### **5.1. Interactive Timeline** 



23 

To support practical match-analysis workflows, we develop an interactive timeline visualization (Figure 10) that enables analysts to efficiently retrieve key defensive moments in terms of credit gain and loss. The tool is implemented using Plotly<sup>3</sup> , allowing users to zoom into specific time intervals and inspect events by hovering over the timeline, which reveals the action index, action type, involved players, and assigned defensive credit. 

This interface allows users to quickly spot when and how each player performed good defense or allowed dangerous attacks throughout the match, simply by scanning for spikes in credit, rather than manually reviewing the entire match. After finding an important moment, analysts can identify the corresponding timestamp or the action index and then use them to visualize or replay the associated scene. In the future, we plan to integrate this prototype with common visualization tools such as Power BI<sup>4</sup> or video analysis tools like Hudl Sportscode<sup>5</sup> to enable seamless navigation from a colored event in the timeline to the exact video clip. Such integration can significantly streamline and accelerate data-driven post-match analysis in professional clubs. 



**Figure 10:** Retrieval of key defensive moments using an interactive timeline for player-wise credit gain and loss, where blue indicates positive credit and red indicates penalties. 

### **5.2. Spatial Tendency Across Pitch Zones** 

To understand where on the pitch teams gain and lose defensive value, we visualize the spatial distribution of defensive credits in the form of heatmaps overlaid on the pitch, as shown in Figure 

> 3 <u>https://plotly.com</u> 

> 4 <u>https://www.microsoft.com/en-us/power-platform/products/power-bi</u> 

> 5 <u>https://www.hudl.com/en_gb/products/sportscode</u> 



24 

11. These visualizations reveal spatial patterns of each team’s offensive and defensive performance that cannot be captured through action counts alone. 

For the away team in the figure, although they accumulated a large amount of positive credit through on-ball defensive actions and disturbances, these gains were concentrated in front of their own goal. Crucially, they also incurred much larger penalties in these same high-risk zones, indicating repeated exposure to dangerous attacks. This pattern reflects their reactive defensive performance: forced deep into their box, often succeeding in last-moment interventions but still allowing the opponent to reach threatening areas too frequently. 

In contrast, the home team exhibited a very different defensive profile. Because they were rarely pushed deep into their own box, their total positive credit near goal was smaller. However, the credits they did earn were spread across the entire pitch, most notably the central regions inside the opponent’s half, which appear as a prominent blue area in the Home-Disturb heatmap. Their high “disturb” value in this zone suggests effective high pressing that reduced the success probability of the opponent’s build-up before dangerous situations could emerge. 

There is also a notable contrast in both teams’ half-spaces, i.e., the vertical lanes located between the central lane and the flank. In these regions, the home team conceded almost no penalty, while the away team incurred a large amount. Although the away team got relatively low penalties on the flanks, indicating that they allowed fewer wide attacks, they were repeatedly broken down through the more dangerous central and half-space channels around the box. 

Together, these spatial patterns show how DEFCON provides interpretable insights into team defensive behavior, enabling analysts to identify intense battlefields on the pitch, diagnose teams’ structural weaknesses, and evaluate their pressing effectiveness. 



**Figure 11:** Spatial distribution of defensive credits across pitch zones for the match illustrated in Figure 6. The top and bottom rows display the credit heatmaps for the home and the away teams, respectively, with values separated into the four defense categories defined in Section 2.6. 

### **5.3. Pairwise Attacker-Defender Analysis** 

Unlike existing offense-centered evaluation frameworks which do not identify defensive counterparts of each attacking action, our approach explicitly determines the defending responsibilities associated with every on-ball attacking action. Thus, it enables pairwise 



25 

attacker-defender analysis about how much defensive credit each defender gained or lost against each opposing attacker, as visualized in Figure 12. This allows analysts to identify which defenders held superiority or inferiority over specific opponents. 

Moreover, combining these pairwise values with spatial context such as players’ roles or average on-field locations provides further insights into how and where these credits or penalties emerged. For example, the lower left matrix in Figure 12 shows that many away defenders earned large credit against home 4, who appears as a central forward in Figure 13. When interpreted alongside the Away-Intercept and Away-Disturb heatmaps in Figure 11, which highlight intense defensive activity around their own penalty box, this pattern implies away defenders’ frequent last-moment interventions against home 4’s scoring attempts in dangerous situations. 

In contrast, the lower-right matrix indicates that the away team’s penalties were distributed across a wide range of home attackers, rather than concentrated on a single player. For instance, Figure 13 shows that during the first half, the left fullback away 1 conceded significant value to home 8 (right winger), as well as home 0 (right fullback) and several opposing midfielders. Meanwhile, the center back away 2 effectively handled home 4 (center forward), incurring relatively small penalties against him. However, away 2 instead received huge penalties from home 3 (central midfielder), indicating a vulnerability in defending threatening passes made from the opposing midfield. 

Overall, this pairwise attacker-defender analysis provides actionable insights into matchup-specific strengths and weaknesses. Such information can support various real-world decision-making processes, such as selecting lineups that best exploit or mitigate specific matchups and scouting players whose defensive style fits the tactical needs of the team. 



26 



**Figure 12:** Pairwise defensive credit matrices, visualizing how much defensive credit (left) or penalty (right) each defending player accumulated against each opposing attacker in the match. 



27 





**Figure 13:** Visualziation of pairwise penalties imposed on away defenders against home attackers during the first half of the match. Player locations correspond to their average locations in the half, and the thickness of each arrow is proportional to the magnitude of penalty from the attacker to the defender of interest. 

## **6. Conclusions** 

This paper proposes DEFCON, a comprehensive framework for fine-grained quantification of defensive contributions in soccer. While most existing data-driven approaches have largely focused on on-ball actions, DEFCON addresses the longstanding challenge of also evaluating what they prevent or concede and how responsible they are for defending each attacking option. 

For every attacking on-ball action, DEFCON classifies the situation based on pass success or failure, EPV increase or decrease, and whether a shot is blocked, and assigns defensive credit to individual players according to principled, scenario-specific rules. To enable these computations, it employs Graph Attention Networks to estimate key component values such as action success probabilities, success-conditioned EPVs, and defender responsibilities with high contextual fidelity. The resulting defensive credits align well with players’ actual defensive ability, revealing that the penalty for conceding dangerous attacks exhibits a far stronger correlation with market value than the credit for on-ball defensive actions alone. Finally, we present practical applications of DEFCON in temporal, spatial, and relational analyses, providing practitioners with actionable, interpretable insights with multiple levels of resolution. 



28 

Looking ahead, several extensions of DEFCON present promising avenues for future work. One direction is to integrate our defensive valuation with established offensive metrics such as xT [32], VAEP [8], and GIM [20], enabling holistic assessment of players’ offensive and defensive contributions. Since a player’s tactical roles often change across matches and even within a single match, another direction is to incorporate algorithms for detecting time-varying formations and player roles [4] [5] [16] to separate the player’s defensive performance by role and compare multiple players taking the same role. Finally, we aim to extend our applications to tactical analysis, such as identifying which formation best defend defending against specific opponent structures, or diagnosing which role become vulnerable when deploying a particular lineup against them. 



29 

## **References** 

- [1] Gabriel Anzer and Pascal Bauer. A Goal scoring probability model for shots based on synchronized positional and event data in football (Soccer). _Frontiers in Sports and Active Living_ , 3, 2021. 

- [2] Gabriel Anzer and Pascal Bauer. Expected passes: Determining the difficulty of a pass in football (soccer) using spatio-temporal data. _Data Mining and Knowledge Discovery_ , 36(1):295–317, 2022. 

- [3] Gabriel Anzer, Pascal Bauer, Ulf Brefeld, and Dennis Fassmeyer. Detection of tactical patterns using semi-supervised graph neural networks. In _MIT Sloan Sports Analytics Conference_ , 2022. 

- [4] Pascal Bauer, Gabriel Anzer, and Laurie Shaw. Putting team formations in association football into context. _Journal of Sports Analytics_ , 9(1): 39–59. 2023. 

- [5] Ulrik Brandes, Hadi Sotudeh, Doğan Parlak, Paolo Laffranchi, and Mert Erkul. Shape graphs and the instantaneous inference of tactical positions in soccer. _npj Complexity_ , 2(25), 2025. 

- [6] Lotte Bransen and Jan Van Haaren. Player chemistry: Striving for a perfectly balanced soccer team. In _MIT Sloan Sports Analytics Conference_ , 2020. 

- [7] Tianqi Chen and Carlos Guestrin. XGBoost: A scalable tree boosting system. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 2016. 

- [8] Tom Decroos, Lotte Bransen, Jan Van Haaren, and Jesse Davis. Actions speak louder than goals: Valuing player actions in soccer. In _Proceedings of the 25th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , 2019. 

- [9] Gregory Everett, Ryan Beal, Tim Matthews, Timothy Normal, and Sarvapali Ramchurn. Evaluating defensive influence in multi-agent systems using graph attention networks. In _IEEE 12th International Conference on Data Science and Advanced Analytics_ , 2025. 

- [10] Javier Fernandez, Luke Bornn, and Daniel Cervone. Decomposing the immeasurable sport: A deep learning expected possession value framework for soccer. In _MIT Sloan Sports Analytics Conference_ , 2019. 

- [11] Javier Fernandez and Luke Bornn. SoccerMap: A deep learning architecture for visually-interpretable analysis in soccer. In _Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases_ , 2020. 

- [12] Javier Fernandez, Luke Bornn, and Daniel Cervone. A framework for the fine-grained evaluation of the instantaneous expected value of soccer possessions. _Machine Learning_ , 110(6):1389–1427, 2021. 

- [13] Leander Forcher, Stefan Altmann, Leon Forcher, Darko Jekauc, and Matthias Kempe. The use of player tracking data to analyze defensive play in professional soccer - A scoping review. _International Journal of Sports Science and Coaching_ , 17(6):1567–1592, 2022. 

- [14] Leander Forcher, Tobias Beckmann, Oliver Wohak, Christian Romeike, Ferdinand Graf, and Stefan Altmann. Prediction of defensive success in elite soccer using machine learning - Tactical analysis of defensive play using tracking data and explainable AI. _Science and Medicine in Football_ , 8(4):317–332, 2024. 

- [15] Sam Green. Assessing the performance of Premier League goalscorers, 2012. 

- [16] Hyunsung Kim, Bit Kim, Dongwook Chung, Jinsung Yoon, and Sang-Ki Ko. SoccerCPD: Formation and role change-point detection in soccer matches using spatiotemporal tracking data. In _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , 2022. 

- [17] Hyunsung Kim, Hoyoung Choi, Sangwoo Seo, Tom Boomstra, Jinsung Yoon, and Chanyoung Park. ELASTIC: Event-tracking data synchronization in soccer without annotated event 



30 

locations. In _ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics_ , 2025. 

- [18] Thomas N. Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. In _Proceedings of the 5th International Conference on Learning Representations_ , 2017. 

- [19] Minho Lee, Geonhee Jo, Miru Hong, Pascal Bauer, and Sang-Ki Ko. exPress: Contextual valuation of individual players within pressing situations in soccer. In _MIT Sloan Sports Analytics Conference_ , 2025. 

- [20] Guiliang Liu, Yudong Luo, Oliver Schulte, and Tarak Kharrat. Deep soccer analytics: Learning an action-value function for evaluating soccer players. _Data Mining and Knowledge Discovery_ , 34(5):1531–1559, 2020. 

- [21] Yudong Luo, Oliver Schulte, and Pascal Poupart. Inverse reinforcement learning for team 

   - sports: Valuing actions and players. In _Proceedings of the 29th International Joint Conference on Artificial Intelligence_ , 2020. 

- [22] Charbel Merhej, Ryan Beal, Tim Matthews, and Sarvapali Ramchurn. What happened next? using deep learning to value defensive actions in football event-data. In _Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , 2021. 

- [23] Luca Pappalardo, Paolo Cintia, Paolo Ferragina, Emanuele Massucco, Dino Pedreschi, and Fosca Giannotti. PlayeRank: Data-driven performance evaluation and player ranking in soccer via a machine learning approach. _ACM Transactions on Intelligent Systems and Technology_ , 10(5):59:1–27, 2019. 

- [24] Luca Pappalardo, Paolo Cintia, Alessio Rossi, Emanuele Massucco, Paolo Ferragina, Dino Pedreschi, and Fosca Giannotti. A public data set of spatio-temporal match events in soccer competitions. _Scientific Data_ , 6(1):236, 2019. 

- [25] Paul Power, Hector Ruiz, Xinyu Wei, and Patrick Lucey. Not all passes are created equal: Objectively measuring the risk and reward of passes in soccer from tracking data. In _Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 2017. 

- [26] Liudmila Prokhorenkova, Gleb Gusev, Aleksandr Vorobev, Anna Dorogush, and Andrey Gulin. CatBoost: Unbiased boosting with categorical features. In _Advances in Neural Information Processing Systems_ 31, 2018. 

- [27] Dominik Raabe, Reinhard Nabben, and Daniel Memmert. Graph representations for the analysis of multi-agent spatiotemporal sports data. _Applied Intelligence_ , 53(4):3783–3803, 2023. 

- [28] Pegah Rahimian, Jan Van Haaren, Togzhan Abzhanova, and Laszlo Toka. Beyond action valuation: A deep reinforcement learning framework for optimizing player decisions in soccer. In _MIT Sloan Sports Analytics Conference_ , 2022. 

- [29] Pegah Rahimian, Jan Van Haaren, and Laszlo Toka. Towards maximizing expected possession outcome in soccer. _International Journal of Sports Science and Coaching_ , 19(1), 2023. 

- [30] Pegah Rahimian, Hyunsung Kim, Marc Schmid, and Laszlo Toka. Pass receiver and outcome prediction in soccer using temporal graph networks. In _ECML PKDD Workshop on Machine Learning and Data Mining for Sports Analytics_ , 2023. 

- [31] Pieter Robberechts, Maaike Van Roy, and Jesse Davis. un-xPass: Measuring soccer player’s creativity. In _Proceedings of the 29th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 2023. 

- [32] Karun Singh. Introducing Expected Threat (xT): Modelling team behaviour in possession to gain a deeper understanding of buildup play, 2019. https://karun.in/blog/expectedthreat.html. Accessed: 2025-12-01. 



31 

- [33] Michael Stockl, Thomas Seidl, Daniel Marley, and Paul Power. Making offensive play predictable - using a graph convolutional network to understand defensive performance in soccer. In _MIT Sloan Sports Analytics Conference_ , 2021. 

- [34] Kosuke Toda, Masakiyo Teranishi, Keisuke Kushiro, and Keisuke Fujii. Evaluation of soccer team defense based on prediction models of ball recovery and being attacked: A pilot study. _PLOS ONE_ , 17(1), 2022. 

- [35] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph Attention Networks. In _Proceedings of 6th International Conference on Learning Representations_ , 2018. 

- [36] Lintao Wang, Shiwen Xu, Michael Horton, Joachim Gudmundsson, and Zhiyong Wang. Player-team heterogeneous interaction graph transformer for soccer outcome prediction. In _Proceedings of the 31st ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 2025. 

- [37] Zhe Wang, Petar Veličković, Daniel Hennes, Nenad Tomasev, Laurel Prince, Michael Kaisers, Yoram Bachrach, Romuald Elie, Li Kevin Wenliang, Federico Piccinini, William Spearman, Ian Graham, Jerome T. Connor, Yi Yang, Adria Recasens, Mina Khan, Nathalie Beauguerlange, Pablo Sprechmann, Pol Moreno, Nicolas Heess, Michael Bowling, Demis Hassabis, and Karl Tuyls. TacticAI: An AI assistant for football tactics. _Nature Communications_ , 15(1906), 2024. 

- [38] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? In _Proceedings of the 7th International Conference on Learning Representations_ , 2019. 



32 


