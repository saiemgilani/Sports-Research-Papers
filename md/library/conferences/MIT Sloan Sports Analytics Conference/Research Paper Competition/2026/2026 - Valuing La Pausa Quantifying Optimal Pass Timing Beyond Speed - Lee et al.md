<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Valuing La Pausa Quantifying Optimal Pass Timing Beyond Speed - Lee et al.pdf -->

# **Valuing La Pausa: Quantifying Optimal Pass Timing Beyond Speed** 

### Soccer 

Paper ID: 160 Submitted to 2026 MIT Sloan Sports Analytics Conference Research Papers Competition 

## **1. Introduction** 

In the rapidly evolving landscape of football analytics, the quantification of decision-making has emerged as a central frontier. While the evaluation of spatial decisions—identifying optimal target locations—has advanced significantly through frameworks such as Expected Threat (xT)<sup>1</sup> and possession value models (e.g., VAEP [1]), the temporal dimension of these decisions remains underexplored. In elite football, the outcome of a play is governed not only by where the ball is delivered but precisely when it is released. 

Despite the critical importance of timing, prevailing metrics have largely reduced the evaluation of temporal quality to a proxy of execution speed. Recently, metrics such as Pace of Play (PoP) [2] have been proposed to quantify the tempo of possession, operating on the hypothesis that elite performance is characterized by the minimization of time on the ball. Empirical evidence supports this to an extent; higher-quality leagues and competitions indeed exhibit faster average ball circulation, necessitating rapid cognitive processing and technical execution. Consequently, analytical models often implicitly reward players who release the ball quickly and penalize those who dwell on possession, equating velocity with efficiency. 

However, this "faster-is-better" heuristic presents a measurement challenge: since such metrics are designed to reward a faster tempo as an indicator of quality, they are inherently limited in their ability to assess the appropriate timing of an action in complex tactical scenarios. This strategic delay, known as "La Pausa"<sup>2</sup> , is not a sign of indecision but a high-level cognitive and tactical skill used to manipulate defenders and create space. Because speed-based models often penalize such delays, they fail to capture the nuance of this temporal optimization. 

To accurately capture this phenomenon, it is necessary to move beyond discrete event evaluation and adopt a continuous framework that views time as a strategic resource. This requires not only a 

> 1 https://karun.in/blog/expected-threat.html 

> 2 https://totalfootballanalysis.com/article/la-pausa-why-this-spanish-passing-style-is-so-effectivetactical-analysis-tactics 



1 



Figure 1. Overall framework of our proposed method. The pipeline synchronizes event and tracking data to calculate the potential Off-Ball Scoring Opportunity (OBSO) across a defined temporal window. This enables the decomposition of the pass decision into distinct Temporal Judgment and Spatial Selection components. 

conceptual shift but also a methodological advancement in handling high-fidelity data to distinguish between inefficient hesitation and value-generating patience. To address these challenges, this paper presents the framework illustrated in Figure 1, with the following main contributions: 

**1. Precise Temporal Segmentation of Pass Execution:** We leverage the ELASTIC [3] framework to accurately align discrete event data with continuous tracking trajectories. This enables the rigorous determination of exact timestamps for “Pass Receipt” and “Pass Release” at the frame level, overcoming the granularity limitations of traditional event-based metrics and ensuring the precision required for derivative-based value analysis. 

**2. Decomposition of Decision Components** : Utilizing the Off-Ball Scoring Opportunity (OBSO) model [4] as a continuous value function, we mathematically decompose the passing action into two distinct axes: Temporal Judgment (When) and Spatial Selection (Where). This framework enables the evaluation of decision quality by quantifying the divergence between the maximum potential value achievable at the moment of execution and the actual value realized by the player. 

3. **Validation through Team Strength and Stylistic Profiling** : Through extensive experiments, we demonstrate that our proposed metric exhibits a stronger correlation with Team Strength than traditional methods. Furthermore, we illustrate the metric's capacity to categorize player styles quantitatively, successfully distinguishing between players who generate value through rapid circulation and those who maximize value through strategic delay. 



2 

We validate our metric using event and tracking data from 55 matches in the German Bundesliga 1. The remainder of this paper is organized as follows: Section 2 reviews related work, and Section 3 details the methodology behind our proposed framework. Section 4 presents the experimental results and validation against team performance, followed by a discussion of player archetypes and future directions in Section 5. 

## **2. Related Work** 

The pursuit of optimal timing remains a paramount objective in sports analytics, as the outcome of high-stakes competition often hinges on split-second judgments. In elite sports, temporal windows as brief as 300 milliseconds can differentiate a successful play from a failed one, shaping the pivotal moments that ultimately dictate results [5, 6, 7, 8]. While existing research in discrete domains—such as batter swing timing in baseball or serve returns in tennis—has successfully characterized these windows in interceptive tasks [9, 10], the fluid nature of soccer presents a fundamentally distinct challenge. Unlike reactive environments, a pass in soccer involves a complex coupling of execution time and spatial direction, where the value of a target fluctuates dynamically with player movement. Consequently, metrics designed for isolated cognitive tasks in closed environments are insufficient for capturing the open-ended complexity of football. 

Despite this, prevailing studies in soccer have largely utilized execution speed as a proxy for temporal quality. Metrics like Pace of Play (PoP) [2] operate on the premise that elite players are characterized by their ability to minimize time on the ball. However, this heuristic fails to capture the nuances of high-level tactical intelligence. The tactical concept of “La Pausa” illustrates that a delayed action is not necessarily an indicator of inefficiency but a deliberate strategic mechanism to manipulate defensive structures. Theoretical frameworks suggest that by strategically delaying a pass, a player can provoke defenders into breaking their shape, effectively allowing the ball to be directed into the space vacated by the opponent rather than merely to a static teammate<sup>3</sup> . Without this temporal optimization, rapid ball progression risks becoming mere chaotic movement rather than effective tactical advancement. Therefore, relying solely on speed metrics risks penalizing players who possess the cognitive maturity to wait for the optimal window, highlighting the need for a framework that evaluates timing based on value maximization rather than mere swiftness. 

While spatiotemporal frameworks in soccer have advanced beyond intuitive speed metrics. They have predominantly focused on the selection problem, identifying the optimal target coordinates or action type [11-15]. Established models utilizing Expected Possession Value (EPV) [11] or Off-Ball Scoring Opportunities (OBSO) [4] effectively quantify the value of a spatial configuration but typically treat the action’s timestamp as a fixed parameter. This approach overlooks a critical dimension: a pass that is suboptimal at the exact moment of reception may evolve into the value-maximizing option after a strategic delay, as passing lanes materialize or teammates complete their runs. Thus, current literature lacks a unified framework that treats execution timing as a dynamic decision variable, leaving a critical gap in quantifying the player's ability to synchronize action execution with the evolving tactical context. 

## **3. Methods** 

3 www.nytimes.com/athletic/1890161/2020/06/27/a-hidden-quality-explains-why-pep-lovesgundogan-foden-wont-play-silva-role/ 



3 

In this section, we formally define our proposed metric, PAUSA (Passing Ability Under Spatiotemporal Awareness). To ensure the high temporal fidelity required for this analysis, we utilize the ELASTIC framework [3] to synchronize discrete event data with continuous tracking trajectories, enabling the rigorous determination of exact timestamps for Pass Receipt (𝑡 )  and 𝑟𝑒𝑐𝑒𝑖𝑝𝑡 Pass Release (𝑡 ) at the frame level. Based on this synchronized data, we detail the value function 𝑎𝑐𝑡 and decompose the decision-making process into Temporal Judgment and Spatial Selection. 

#### **3.1 Value Function: Off-Ball Scoring Opportunity (OBSO)** 

Building upon the Off-Ball Scoring Opportunity (OBSO) framework proposed by Spearman [4], we adopt this model as our primary value function. Unlike traditional metrics that focus solely on the ball carrier, OBSO is designed to evaluate the quality of off-ball positioning by assessing how the spatial configuration of all players contributes to creating scoring chances. 

Fundamentally, given the instantaneous game state  (comprising positions and velocities of all 𝐷 players and the ball), the OBSO model estimates the probability of scoring assuming the next on-ball 2 event occurs at a specific target location 𝑟 ∈ 𝑅 . This value is derived by aggregating the joint probabilities of three distinct components: Scoring (𝑆), Control (𝐶), and Transition (Ⲧ). Formally, the total probability of scoring, P(G|D), is defined as the sum of these conditional probabilities across all possible locations on the pitch: 



Here, 𝑃(𝑆𝑟) represents the probability of scoring given that the attacking team possesses the ball at location , 𝑟𝑃(𝐶𝑟) represents the probability that the attacking team controls the ball at location , 𝑟 and 𝑃(Ⲧ𝑟) represents the probability that the next event occurs at location . Finally, the value of a 𝑟 pass directed to a location  at a specific time , denoted as OBSO(t, r), is defined as: 𝑟 𝑡 𝑂𝐵𝑆𝑂(𝑡, 𝑟) = 𝑃(𝑆𝑟|𝐷𝑡) 𝑃(𝐶𝑟|𝐷𝑡) 𝑃(Ⲧ𝑟|𝐷𝑡) (2) 

The mathematical derivation and the specific modeling of each component of the OBSO framework are detailed in Appendix A. 

#### **3.2 Temporal Judgement (When)** . 

The primary objective of this study is to evaluate the optimality of pass timing, explicitly capturing the value generated through "La Pausa"—the strategic delay of play. While existing pass evaluation metrics treat the execution time as a fixed constraint, we broaden the scope to verify whether the timing chosen by the player was theoretically optimal. 

To formulate this, let 𝑡 denote the actual time the pass was executed. We introduce a temporal 𝑎𝑐𝑡 search window 𝑊 to explore alternative timings around this event. The range of this window is determined by two distinct temporal margins: a backward margin δ (e.g., 3.0s) and a forward 𝑝𝑟𝑒 margin δ (e.g., 1.0s). Crucially, since a player cannot execute a pass before gaining possession, 𝑝𝑜𝑠𝑡 



4 

the lower bound of the search window is constrained by the time the player received the ball, denoted as 𝑡 . Accordingly, the feasible temporal window 𝑊 is defined as: 𝑟𝑒𝑐𝑒𝑖𝑝𝑡 



Within this window, we compare the potential value at the specific moment of action against the maximum potential value achievable across the entire duration. We define Temporal Judgment as the ratio between these two values: 



The numerator represents the maximum potential value achievable at the actual pass time 𝑡 . The 𝑎𝑐𝑡 denominator represents the global maximum potential value achievable if the player had perfectly regulated the tempo within the feasible window 𝑊. Crucially, this metric evaluates the pure potential of the chosen timing by assuming the player selects the best spatial option available at that moment. However, even with perfect timing, the realized outcome depends on the target selection. To assess the quality of the actual target chosen by the player, we introduce Spatial Selection in the subsequent section. 

#### **3.3 Spatial Selection (Where)** 

While Temporal Judgment evaluates the timing of the action, it relies on the assumption of optimal target selection. However, in reality, a player might execute an action at the optimal moment but fail to identify the best option. To address this, we introduce Spatial Selection, which evaluates the quality of the target chosen by the player at time 𝑡 . We define Spatial Selection as the ratio 𝑎𝑐𝑡 between the OBSO value of the actual pass and the maximum potential value achievable at time 𝑡 : 𝑎𝑐𝑡 



Here, 𝑟 denotes the coordinate where the pass was successfully received (i.e., the pass end 𝑎𝑐𝑡 location). The numerator represents the realized value corresponding to this specific target location evaluated at time 𝑡 . The denominator represents the maximum potential value achievable at time 𝑎𝑐𝑡 𝑡 , which is identical to the numerator in Eq. 4. 𝑎𝑐𝑡 

#### **3.4 PAUSA (Passing Ability Under Spatiotemporal Awareness)** 

Finally, we integrate the spatial and temporal components defined in the previous sections into a unified metric: PAUSA (Passing Ability Under Spatiotemporal Awareness). This metric quantifies the overall efficiency of a pass decision by simultaneously considering when the action was executed and where it was directed. We define PAUSA as the product of Spatial Selection and Temporal Judgment: 





5 

Mathematically, the intermediate term (the maximum potential value at 𝑡 ) cancels out, 𝑎𝑐𝑡 simplifying the metric to the ratio between the realized value of the actual pass and the global maximum potential achievable within the temporal window. However, the theoretical value of this framework lies in its decomposition of the decision-making process, which enables us to identify specific sources of inefficiency. 

For instance, it distinguishes between scenarios where a player finds the optimal window but misses the target, and conversely, where a player selects the best local option but acts prematurely. Thus, PAUSA comprehensively evaluates “La Pausa” by rewarding the specific synergy of strategic patience (Temporal Intelligence) and value-maximizing selection (Spatial Intelligence). 

## **4. Experimental Results** 

#### **4.1 Dataset** 

To validate the proposed framework, we utilized a high-fidelity spatiotemporal dataset comprising 55 matches from the German Bundesliga (2023-2024 season), including the open-source dataset released by Bassek et al. [16]. The dataset integrates optical tracking data, capturing the 𝑥, 𝑦 coordinates of all 22 players and the ball at a sampling frequency of 25Hz, with event data that provides semantic annotations for distinct game actions. As noted in Section 3, these sources were synchronized using the ELASTIC framework to ensure frame-level temporal alignment. 

To ensure the validity of our simulation and value extraction, we applied specific filtering criteria to the event data. First, we selected only successful passes and crosses (based on SPADL<sup>4</sup> types) to focus on completed offensive actions. Second, set-pieces were excluded, as the absence of a preceding dynamic receiver trajectory makes the temporal simulation of the "waiting phase" infeasible. Finally, we restricted the analysis to instances where the receiver belonged to the same team as the passer. This condition is crucial because determining the realized OBSO value requires a specific target location secured by the attacking team; extracting the intended value for intercepted passes where the receiver is an opponent is methodologically ambiguous in this framework. 

#### **4.2 Implementation Details** 

To ensure the reproducibility of our results, we configured the temporal parameters and preprocessing pipeline as follows. The temporal search window 𝑊 was defined with an asymmetric structure, setting the backward margin δ to 3.0 seconds and the forward margin δ 𝑝𝑟𝑒 𝑝𝑜𝑠𝑡 

to 1.0 seconds. The backward margin was empirically determined to capture the majority of the holding phase, covering over 80% of open-play passes in our dataset. Conversely, the forward margin was restricted to 1.0 seconds to mitigate the uncertainty inherent in projecting player trajectories and pitch control dynamics over longer horizons; a detailed justification regarding simulation precision is provided in Appendix B. 

Regarding data preprocessing, we adopted the pipeline established in the ELASTIC framework. All tracking coordinates were transformed into a standardized 105𝑚×68𝑚 system with the direction of play aligned left-to-right. To address measurement noise in optical tracking, we applied a Savitzky-Golay filter to smooth positional data before deriving velocity and acceleration vectors, and 

> 4 https://socceraction.readthedocs.io/en/latest/documentation/spadl/spadl.html 



6 

frames corresponding to dead-ball phases were subsequently removed to restrict the analysis to active gameplay. 

#### **4.3 Results** 

To validate the analytical utility of PAUSA, we conducted a two-fold correlation analysis as illustrated in Figure 2: first, assessing the relationships between PAUSA and existing baseline metrics at the player level, and second, evaluating the metric's predictive power regarding team performance. 

#### **4.3.1. Player-Level Evaluation: Correlation with Baseline Metrics** 

We examined the Pearson correlation matrix between PAUSA and established metrics—Pass Completion Rate, Pace of Play (PoP), and Expected Threat (xT)—based on player-level aggregated values (Figure 2, Left). The analysis yields several critical insights into the interplay between spatial and temporal decision-making. 





Figure 2. Pearson correlation analysis at player and team levels. (Left) Pairwise correlations between PAUSA components and baseline metrics for players with at least 150 completed passes. (Right) Correlations between team-aggregated metrics and performance (Points Per Game), demonstrating the superior predictive validity of PAUSA over speed-based metrics. 

First, Pass Completion Rate exhibits a positive correlation with Temporal Judgment (𝑟= 0.307). This relationship is largely driven by positional characteristics, particularly those of Center Backs. In the build-up phase, defenders often operate under relatively low pressure, allowing them to secure optimal timing and execute stable passes. However, since these passes rarely target high-value areas, they result in low overall Spatial Selection scores, limiting the final PAUSA value. 

Second, the Pace of Play (PoP) shows a weak positive correlation with Temporal Judgment ( = 𝑟 0.200), suggesting that longer possession time can facilitate finding the appropriate moment. However, PoP displays a negative correlation with PAUSA ( = -0.286). This indicates that while 𝑟 caution may improve timing precision to a degree, excessive delay without spatial gain incurs opportunity costs, reinforcing that minimizing time is not always optimal, but neither is indefinite holding. 

Third, Expected Threat (xT) demonstrates a moderate positive correlation with Spatial Selection ( 𝑟 = 0.404)  but a distinct negative correlation with Temporal Judgment. ( = -0.484) This divergence 𝑟 highlights a limitation of xT: while it effectively evaluates the _spatial_ quality of a pass, it fails to 



7 

capture the temporal efficiency of the execution. 

Crucially, the analysis reveals a strong negative correlation ( = -0.499) between Spatial Selection 𝑟 and Temporal Judgment. This reflects the inherent trade-off in football: targeting high-value spaces (High Spatial) inevitably invites strong defensive pressure, making it difficult to secure optimal timing (High Temporal). Conversely, pressure-free situations allow for perfect timing but typically offer lower spatial value. PAUSA is designed to identify the elite players who can defy this trade-off. 

#### **4.3.2. Team-Level Evaluation: Correlation with Match Outcomes** 

To verify whether the individual capacity for optimal pass timing translates to collective success, we analyzed the relationship between team-aggregated PAUSA scores and Points Per Game (PPG). Given that our dataset comprises a subset of the season rather than the entire schedule, we utilized the PPG calculated specifically from the analyzed matches. This ensures a direct and valid comparison between our metric and the team's actual performance within the scope of this study (Figure 2, Right). 

The results demonstrate that PAUSA exhibits the strongest positive correlation ( = 0.733) with PPG 𝑟 compared to other baseline metrics, including Completion Rate ( = 0.469). In contrast, PoP shows 𝑟 no significant correlation with PPG ( = -0.033). This near-zero coefficient implies that the mere 𝑟 speed of ball circulation—whether fast or slow—is not a decisive factor in match outcomes. Instead, it suggests that slowing down the tempo benefits the team only when it is a product of tactically valid regulation (i.e., high PAUSA), rather than simple hesitation. This finding empirically supports our hypothesis that the _optimality_ of timing is a superior predictor of performance than the _speed_ of execution. 

## **5. Application** 

Having validated the correlation between PAUSA and team performance, we now demonstrate the metric's practical utility in characterizing player styles. By dissecting the PAUSA score into its constituent components—Spatial Selection and Temporal Judgment—we identify distinct tactical archetypes and evaluate how elite players optimize decision-making under varying constraints. 

#### **5.1 Elite Player Profiling and Team Performance Analysis** 

We analyzed the distribution of Spatial Selection (x-axis) and Temporal Judgment (y-axis) scores across different positions and teams, as illustrated in Figure 3. The most defining characteristic of high-level performance is observed in the upper-right quadrant, where effective playmakers such as Exequiel Palacios and Granit Xhaka reside. Unlike typical players who trade off time for space, these elite midfielders demonstrate a unique ability to bridge the gap between stability and creativity, combining the "Strategic Vision" to identify high-value targets with the "La Pausa" required to synchronize the release at the optimal moment. 

Crucially, this individual capacity for optimal timing serves as a foundational driver of collective dominance. As shown in the team-level aggregation (Figure 3, Right), Bayer 04 Leverkusen clusters most prominently in this high-spatial, high-temporal region. Given that our dataset corresponds to 



8 





Figure 3. Comparison of Spatial Selection (x-axis), Temporal Judgement (y-axis), and PAUSA (size) per pass for players (Left) and teams (Right). Colors represent player positions. 

their historic undefeated Bundesliga campaign, this alignment provides powerful empirical validation of our metric. It suggests that their unprecedented success was fueled by a systemic superiority in identifying and exploiting optimal spatiotemporal windows—a qualitative advantage that traditional speed-based metrics fail to capture. 

Contextualizing this elite performance reveals a clear stratification of tactical roles for the broader player population. Outside the elite cluster, players are largely constrained by their positional demands. Defenders, particularly Center Backs (CB), typically cluster in the upper-left quadrant; operating under lower pressure in the build-up phase, they enjoy high temporal freedom but prioritize safer, lower-value targets to maintain possession. Conversely, midfielders and forwards operating in high-density zones are found in the lower-right or lower-left quadrants. Constrained by intense defensive pressure, they are often forced to operate with tighter temporal margins, limiting their ability to wait for the theoretically optimal window compared to the players who defy these constraints. 

#### **5.2 Temporal Judgement Style** 







9 

Figure 4. Comparison of PAUSA values according to Time Difference (Left) and Control Probability Difference (Right). 

Beyond aggregate performance, we characterize player styles by analyzing the bias in their temporal decision-making. Figure 4 (Left) visualizes the relationship between timing execution and overall efficiency. The x-axis represents the Time Difference, calculated as the deviation of the actual pass time from the optimal timing, while the y-axis represents the PAUSA score. 

Superior performance generally corresponds to player positions closer to zero on the x-axis with high PAUSA scores. However, the distribution reveals distinct temporal profiles among elite players. A positive Time Difference (> 0) indicates a tendency to execute the pass later than the calculated optimal moment. High PAUSA values in this region reflect the effective application of "La Pausa," where players like Exequiel Palacios and Alejandro Grimaldo deliberately delay the release to stabilize play or manipulate defensive structures. Conversely, a negative Time Difference (< 0) indicates a tendency to execute the pass faster than the baseline. High PAUSA values in this domain correspond to players like Florian Wirtz and Atakan Karazor, who generate high value through rapid anticipation, exploiting fleeting windows before they close. 

#### **5.3 Spatial Selection Style** 

We analyze the relationship between the spatial selection (Pitch Control Difference) and PAUSA. The x-axis represents the Pitch Control Difference between control probability of the actual pass end location and the optimal location, while the y-axis represents the PAUSA score. 

Superior performance corresponds to player positions that are closer to zero on the x-axis and higher on the y-axis. Values approaching zero indicate directing passes to areas where the team maintains high control probability; high PAUSA values in this region reflect "Spatial Stability," where players like Palacios, Grimaldo, and Florian Wirtz generate high value by identifying open spaces that ensure possession. Conversely, a large negative difference indicates directing passes to areas with lower control probability; players in this region, such as Waldemar Anton. 

## **6. Case Study** 

#### **6.1 Slower vs Faster** 

We analyze two distinct optimization scenarios visualized in Figure 5 to validate the practical utility of the metric. 

Figure 5 (a) and (b) illustrates a counter-attacking sequence initiated by the Red team following a ball recovery in the middle third. Red 6 Player (Passer) executes a pass to Red 27 Player (Receiver) at the moment 𝑡 . As shown in the Figure 5 (a), OBSO heatmap at this timestamp indicates a 𝑎𝑐𝑡 concentration of value primarily in the wide areas, corresponding to PAUSA value of 0.523. However, a counterfactual analysis at 𝑡 + 1 reveals a significant tactical shift. As visualized in 𝑎𝑐𝑡 Figure 5 (b), delaying the decision would have allowed Red 2 Player to exploit the space created in the central channel. This spatiotemporal optimization is captured by PAUSA, which surges to 0.690 in the delayed scenario. In the actual play, Red 6 Player's decision to release the ball immediately to Red 27 Player locked in a suboptimal state, bypassing the higher-value opportunity that was emerging centrally. The comparison exemplifies the necessity of "La Pausa," where a deliberate 



10 









Figure 5: Spatiotemporal value comparison between actual execution (𝑡 ) and optimal timing. The 𝑎𝑐𝑡 "La Pausa" scenario: (a) actual pass at 𝑡 , and (b) counterfactual simulation at 𝑡 + 1, showing 𝑎𝑐𝑡 𝑎𝑐𝑡 higher value when execution is delayed. The "Acceleration" scenario: (c) actual pass at 𝑡 , and (d) 𝑎𝑐𝑡 counterfactual simulation at 𝑡 - 2.12, showing higher value achieved when execution is advanced. 𝑎𝑐𝑡 

delay would have synchronized execution with the probability peak, maximizing the PAUSA value from 0.523 to 0.690. 

Conversely, Figure 5 (c) and 5 (d) illustrates a context necessitating rapid execution. Here, Blue 10 Player (Passer) holds possession while Blue 5 Player makes a run into open space. The actual pass executed at  𝑡 resulted in a relatively low PAUSA value of 0.008, as visualized in Figure 5 (c), 𝑎𝑐𝑡 

indicating that the optimal window had already passed due to defensive consolidation. However, the counterfactual analysis illustrates that the highest value existed prior to the actual execution. As shown in Figure 5 (d), releasing the ball earlier would have allowed Blue 5 Player to receive the pass in a more advantageous position before the space closed. This "Acceleration" would have increased the PAUSA value to 0.011. The comparison highlights that in specific high-pressure contexts, maximizing value requires exploiting fleeting windows through rapid decision-making rather than hesitation. 



11 

## **7. Conclusion** 

This study presents a paradigm shift in football analytics, moving beyond the prevailing heuristic that faster play is inherently superior. We introduced the PAUSA (Passing Ability Under Spatiotemporal Awareness) metric, a novel framework designed to quantify the optimality of pass timing rather than its speed. By leveraging high-fidelity tracking data and the continuous Off-Ball Scoring Opportunity (OBSO) model, we mathematically decomposed the passing decision into two distinct axes: Temporal Judgment (the ability to synchronize action with the optimal window) and Spatial Selection (the ability to identify value-maximizing targets). 

Our empirical results validate that the capacity for optimal timing is a more significant driver of collective success than execution speed alone. The PAUSA metric demonstrated a strong positive correlation with team performance (Points Per Game), significantly outperforming traditional metrics like Pace of Play (PoP). Furthermore, the framework successfully identified the unique spatiotemporal signatures of elite playmakers, distinguishing those who create value through rapid anticipation from those who utilize strategic delay to manipulate defensive structures. Ultimately, this work reframes the analytical evaluation of decision-making from "how fast" a player acts to "how well-timed" their actions are, providing a rigorous tool for talent identification and tactical analysis in elite football. 

## **References** 

[1] Decroos, Tom, et al. "VAEP: An objective approach to valuing on-the-ball actions in soccer." Proceedings of the twenty-ninth international joint conference on artificial intelligence, IJCAI-20. International Joint Conferences on Artificial Intelligence Organization, 2020. 

[2] Bransen, Lotte, and Jesse Davis. "Measuring player pace of play in elite female association football." _International Journal of Sports Science & Coaching_ (2025): 17479541251334022. 

[3] Kim, Hyunsung, et al. "ELASTIC: Event-Tracking Data Synchronization in Soccer Without Annotated Event Locations." arXiv preprint arXiv:2508.09238 (2025). 

[4] William Spearman. "Beyond expected goals." In Proceedings of the 12th MIT Sloan Sports Analytics Conference. 2018. 

[5] Savelsbergh, Geert JP, et al. "Visual search, anticipation and expertise in soccer goalkeepers." _Journal of sports sciences_ 20.3 (2002): 279-287. 

[6] Land, Michael F., and Peter McLeod. "From eye movements to actions: how batsmen hit the ball." Nature neuroscience 3.12 (2000): 1340-1345. 

[7] Yarrow, Kielan, Peter Brown, and John W. Krakauer. "Inside the brain of an elite athlete: the neural processes that support high achievement in sports." _Nature Reviews Neuroscience_ 10.8 (2009): 585-596. 

[8] Mann, Derek TY, et al. "Perceptual-cognitive expertise in sport: A meta-analysis." _Journal of sport and exercise psychology_ 29.4 (2007): 457-478. 

[9] Muraskin, Jordan, Jason Sherwin, and Paul Sajda. "Knowing when not to swing: EEG evidence that enhanced perception–action coupling underlies baseball batter expertise." NeuroImage 123 (2015): 1-10. 

[10] Shim, Jaeho, et al. "The use of anticipatory visual cues by highly skilled tennis players." _Journal of motor behavior_ 37.2 (2005): 164-175. 

[11] Fernández, Javier, and Luke Bornn. "Soccermap: A deep learning architecture for visually-interpretable analysis in soccer." _Joint European Conference on Machine Learning and Knowledge Discovery in Databases_ . Cham: Springer International Publishing, 2020. 



12 

[12] Mendes-Neves, Tiago, Luís Meireles, and João Mendes-Moreira. "Forecasting events in soccer matches through language." _arXiv preprint arXiv:2402.06820_ (2024). 

[13] Mendes-Neves, Tiago, Luís Meireles, and João Mendes-Moreira. "Towards a foundation large events model for soccer." _Machine Learning_ 113.11 (2024): 8687-8709. 

[14] Honda, Yutaro, et al. "Pass receiver prediction in soccer using video and players' trajectories." _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ . 2022. 

[15] Hubáček, Ondřej, Gustav Šourek, and Filip Železný. "Deep learning from spatial relations for soccer pass prediction." _International workshop on machine learning and data mining for sports analytics_ . Cham: Springer International Publishing, 2018. 

[16] Bassek, Manuel, et al. "An integrated dataset of spatiotemporal and event data in elite soccer." Scientific Data 12.1 (2025): 195. 

## **Appendix A** 









Figure A.1. Example of immediate vs. delayed pass timing. When Red No. 12 played the pass immediately, the resulting OBSO was lower than when he briefly held the ball and released the pass under pressure. This illustrates how OBSO can be used to quantify the value of optimal pass timing. 



13 

#### **A.1. Off-Ball Scoring Opportunity (OBSO)** 

The total probability of scoring, 𝑃(𝐺|𝐷), is formally defined as the sum of the joint probabilities of Scoring (𝑆), Control (𝐶), and Transition (Ⲧ) across all possible locations  on the pitch: 𝑟 



The joint probability in Equation (A.1) can be decomposed into a series of conditional probabilities: 



The terms in Equation (A.2) represent the conditional dependencies between scoring, control, and transition. To simplify the model, we assume conditional independence between the three components. Specifically, we assume that the probability of scoring is independent of the control dynamics, and the transition probability is independent of the control probability in our framework. Consequently, Equation (A.2) is approximated by the product of three independent probabilities: 



The resulting OBSO surface is shown in Figure 2 (a), highlighting the spatial value of the pitch. 

#### **A.2. Scoring Probability** 

The scoring probability, 𝑃(𝑆𝑟), represents the likelihood that the attacking team would score if it successfully gains possession at location . In this study, we adopt the scoring probability surface 𝑟 defined in the original OBSO framework [4]. The scoring probability at each pitch location is modeled as a function of the distance and angle to the goal. The resulting probability field assigns higher values to central areas closer to the penalty box and decreases smoothly with greater distance or tighter shooting angles. The resulting scoring probability surface is shown in Figure A.1. (b), highlighting the high-value zones near the penalty area. 

#### **A.3. Transition Probability** 

The transition probability, 𝑃(Ⲧ𝑟 ), represents the likelihood of the ball moving to location . In the 𝑟 original OBSO framework [4], this probability is coupled with the control probability via a parameter  (see Equation 6 in [4]), reflecting the tendency of players to pass to locations where α teammates are likely to gain control. 

However, to isolate the spatial mechanics of the ball carrier from the teammate's positioning, we set the parameter α = 0. By doing so, we constrain the transition probability to follow a Bivariate Normal Distribution centered on the ball carrier’s location. The resulting transition probability surface is shown in Figure A.1. (c), highlighting the spatial distribution of pass likelihood centered on the ball carrier. 



14 

(A.4) 



#### **A.4. Control Probability** 

The control probability, 𝑃(𝐶𝑟|𝐷, referred to as Pitch Control, represents the likelihood that the attacking team will be the first to intercept and control the ball at location r. Following the Potential Pitch Control Field (PPCF) formulation described in the OBSO framework [4], we model a player's ability to gain control as a Poisson point process. The evolution of control probability for a player  𝑗 at a location  over time  is governed by the following differential equation: 𝑟 𝑇 



In this equation, ∑𝑃𝑃𝐶𝐹 (𝑡, 𝑟, 𝑇) denotes the sum of control probabilities of all other players (𝑘) 𝑘 up to time , representing the probability that the ball has not yet been controlled. 𝑇 𝑓 (𝑡, 𝑟, 𝑇) is the 𝑗 probability that the player  can physically reach the location  within time , calculated using a 𝑗 𝑟 𝑇 logistic function of the expected arrival time. Finally, λ is the control rate parameter, representing 𝑗 the inverse of the mean time required to make a controlled touch once the player arrives. The resulting control probability surface is shown in Figure A.1. (d), highlighting the regions controlled by the home team and the away team. 



15 


