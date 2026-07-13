<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2025/2025 - CoachAI+ Badminton Environment Realistic Badminton Game Simulator for Enhancing Player Performance - Wen-Chih et al.pdf -->

# **CoachAI+ Badminton Environment: A Realistic Badminton Game Simulator for Enhancing Player Performance** 

Other Sports Track Paper 20251430 

## **1. Introduction** 

In recent years, advancements in artificial intelligence (AI) and data collection technologies have revolutionized sports analytics, enabling deeper insights into athletic performance that were previously unattainable. Badminton, a fast-paced and strategy-intensive sport, involves rapid decision-making and complex rally dynamics, making it a challenging yet ideal candidate for exploring the integration of AI in sports analysis. Badminton analysis typically focuses on shuttlecock landing trajectories, player movement patterns, shot type selection, and strategic planning. Accurate analysis is crucial for understanding player decision-making and providing actionable insights, both for in-game tactics and pre-match training. Effective sports analytics can help athletes address weaknesses, exploit strengths, and optimize on-court performance through targeted preparation. 

However, applying deep learning to enhance individual badminton performance in real-time scenarios remains underexplored. This gap is largely due to the lack of **realistic badminton agents** and **simulation environments** capable of capturing the sport’s unique complexities. Unlike sports such as basketball [1] and football [2], where player movements are self-determined, badminton is a turnbased sport where a player’s state, such as receiving position, is dictated by their opponent’s actions. This interdependency makes it particularly challenging to model realistic strategies. 

To address these challenges, [2] proposed a closed-loop AI framework for badminton, introducing RallyNet [3], a state-of-the-art imitation learning model that simulates player behavior. Alongside RallyNet, they developed the CoachAI Badminton Environment [4] [5], a realistic simulation platform designed to test strategies, validate hypotheses, and optimize decision-making algorithms. These tools not only assist players in improving performance, but also enable personalized training plans and tactical preparation, bridging the gap between AI-driven insights and practical applications in badminton. 

Despite its advancements, the current environment faces two significant challenges. First, unlike game environments that rely on simple randomness and rules [6], creating a realistic badminton simulation requires accounting for player limitations and strategic plausibility. This ensures that agents can act freely without producing unrealistic behaviors—an aspect overlooked in existing environments. Second, previous environments primarily offer simulation functions, API integrations, and basic action statistics. However, for coaches and players, the analysis should provide actionable insights related to winning and losing strategies, limiting the practical adoption of these tools by the broader community. 



1 



**Figure 1.** Overview of the CoachAI+ Badminton Environment's Objectives. 

This study aimed to enhance player performance by using AI to simulate player styles, match scenarios, and provide actionable insights for training and strategic decision-making. Specifically, it focused on developing a realistic badminton environment and addressed two key research questions: 

#### **1. Can CoachAI+ simulate diverse player behavior across different game scenarios?** 

**2. How to extract insights on winning and losing from CoachAI+ ?** 

To achieve this, we propose three key contributions, as outlined in Figure 1: 

- **Improving RallyNet with RallyNetv2:** We enhanced the imitation learning model, RallyNet, to better capture player behavior. In rally reconstruction experiments, RallyNetv2 achieved significant improvements in key metrics: a 53% reduction in Landing Location Error (DTW Distance: 0.2983), a 68% reduction in Shot Type Error (CTC Loss: 8.3533), and a 43% reduction in Moving Position Error (DTW Distance: 0.1934) compared to the original RallyNet. 

- **Introducing Realism Constraints:** We incorporated a set of rule-based constraints derived from historical data into the simulation environment. These constraints improve realism by preventing unrealistic actions, such as implausible shot types or movement patterns, creating simulations closer to real match scenarios. 

- **Optimizing Evaluation for Strategic Insights:** We expanded the evaluation system to deliver more actionable and strategic insights, including shot-level statistics for each rally, integrating a badminton-specific win probability model [7], and analyzing player tempo and active/passive states. To enhance interpretability, we collaborated with domain experts to define tactical patterns and conduct tactical analysis. A user-friendly web interface was also developed, allowing coaches to directly import matches for analysis, offering intuitive and comprehensive evaluation results. 

These contributions collectively advance the applicability of CoachAI+ as a tool for improving player performance through realistic simulation and insightful analysis. 



2 

## **2. Preliminaries** 

This section provides an overview of background knowledge and prior research on badminton analysis, covering key topics such as stroke-level badminton datasets, techniques for analyzing badminton players’ behaviors, and recent advancements in badminton environments. 

### **2.1. A Human-Annotated Badminton Dataset** 

Existing studies on badminton analytics face challenges in capturing structured, stroke-level data. To address this, [8] developed the Badminton Language for Sequence Representation (BLSR), a framework for transforming match data into structured tabular formats. BLSR records every stroke with precision, detailing aspects such as stroke timing, shot type, and spatial positions. This structured representation significantly enhances analytical efficiency and precision, laying a solid foundation for professional sports analysis. 

Building on BLSR, [9] introduced ShuttleSet, the largest public badminton singles dataset, featuring 36,492 strokes with detailed player and shuttlecock positions. ShuttleSet evolves with new data as exemplified by ShuttleSet22 [10], which incorporates high-level match data from 2022, capturing modern tactical trends. Its emphasis on data diversity and rally continuity provides comprehensive tactical insights, recording every rally from serve to final shot. 

ShuttleSet prioritizes data diversity and contextual continuity, capturing every rally from serve to final shot, and providing comprehensive tactical insights. In this study, ShuttleSet served as the foundation for constructing a realistic badminton simulation environment. Leveraging its extensive data, we trained models to simulate player behavior and decision-making across diverse match scenarios, enabling in-depth exploration of tactical strategies and their impact on match outcomes. 

### **2.2. Badminton Tactical Analysis** 

Artificial intelligence has become integral to badminton analytics, addressing various challenges and enabling significant advancements. The availability of stroke-level badminton match data has inspired numerous studies. [11] introduced the ShuttleNet model for stroke forecasting, predicting landing points and shot types by incorporating stroke dependencies and player styles. [12] proposed the DyMF model for the first movement forecasting task, using dynamic graphs to predict player movements after returns. Building on these efforts, [3] reframed these forecasting tasks as an imitation learning problem, presenting a specialized model for badminton. 

### **2.3. Badminton Environment** 

Creating a realistic and functional badminton simulation environment is essential for tactical analysis and strategy optimization. Unlike standard game simulations, sports analysis requires adherence to game rules and realistic agents to generate meaningful and actionable insights. 

The existing CoachAI Badminton Environment [4] [5] partially replicates match dynamics, but cannot model realistic player behavior or provide practical tactical insights. Effective simulations require realistic constraints, such as movement limits and valid shot placements—factors that are challenging for models to learn independently. Additionally, providing actionable insights demands domain knowledge, which is missing in current environments that rely on basic statistical summaries, limiting their relevance for players and coaches. 



3 

To overcome these limitations, we developed an enhanced simulation system built on the ShuttleSet dataset [9] and trained on real match data. This system simulates player behavior and decision-making while integrating realistic constraints, such as movement limits and plausible shuttlecock landing position, ensuring that simulations closely reflect actual gameplay. The simulation outputs can be analyzed with advanced tools to assess shot type selection and performance, active vs. passive play, tempo control, and tactical performance. 

By combining data-driven strategy simulations with well-designed constraints, the system captures complex match dynamics and overcomes the limitations of traditional simulations. This improved environment provides coaches and players with actionable insights, enabling targeted training and better performance in competitions. 

## **3. Methodology** 



**Figure 2.** An overview of the CoachAI+ Badminton Environment. 

### **3.1. A Human-Annotated Badminton Dataset** 

Our environment is built upon and improves the current state-of-the-art deep imitation learning model for badminton simulation CoachAI. It models the badminton game as a Markov Decision Process (MDP). The complete architecture is shown in Figure 2. To create realistic virtual players, we introduce RallyNetv2, an enhanced version of RallyNet [4] **,** which is used in CoachAI. Additionally, we apply behavioral constraints by analyzing the correlation between states and actions in real-game data from ShuttleSet. These constraints include limiting shot types based on the received shot type and y-axis movement, limiting landing locations based on shot type, and applying movement limitations. Furthermore, we introduce three evaluation modules that analyze and visualize the outputs of the simulation and real games. These modules provide coaches and players with valuable insights into how a player interacts with the opponent, helping them make more informed decisions. 



4 

### **3.1.1. The Markov Decision Process (MDP) in Badminton Games** 

We model badminton games as a turn-based game between two agents in a singles match. The game is framed using the Markov Decision Process (MDP) [14], which consists of several key components: S, A, T(y∣x, a), R(x), and γ. The set S represents the possible states, which include the type of shot to receive, the shuttlecock’s position, the agent’s position, and the opponent’s position. Set A denotes the actions that the agents can take, which include choosing the type of shot to use, determining the landing position of the shuttlecock, and deciding the movement the agent will make after returning the shuttlecock. The transition probability, T(y∣x, a), defines the likelihood of moving from the previous state x to the current state y, which is determined by the actions of the opposing agent. The reward function, R(x), is governed by the rules of badminton, such as when a shot goes out of bounds, when the shuttlecock is unreachable, or when the agent violates a constraint, such as attempting a smash when receiving a smash. Finally, γ ∈ [0, 1) is the discount factor. 

According to the rules of a real badminton game, the agent who first scores 21 points wins the set. However, if the score reaches 20-20, a deuce occurs, and the agents must lead two points to win the set. At each step t of the set, the agent receives a state st∈S at the t-th step. Based on the state, the agent chooses an action at∈A according to its policy π(at∣st). The environment then returns a reward R(x) and transitions to the next state based on the transition probability T(y∣x, a) which is determined by the actions of the opposing agent. 

### **3.1.2. Opponent as Transition Dynamics** 

As shown in Figure 2, the opponent in badminton serves as a transition dynamic, determining the player's next state and shaping the rally's progression. Accurately reflecting real player behavior is a key goal of the simulation environment. In this paper, we propose RallyNetv2 to effectively capture player strategies, providing realistic transition dynamics for simulations. 



**Figure 3.** The framework of RallyNetv2. 

Figure 3 illustrates the RallyNetv2 framework, which models player interactions as dynamic exchanges mediated by the shuttlecock, akin to particle interactions through collisions. Rally dynamics are captured using Latent Geometric Brownian Motion (LGBM), projecting rally states into latent space and modeling their dynamics with geometric Brownian motion. This approach integrates useful inductive biases from GBM into player decision-making, enhancing the agent's ability to account for opponent behavior and to produce more realistic, responsive gameplay simulations. Inspired by GBM's success in modeling uncertainty and interaction patterns in fields such as financial markets 



5 

[15] and population dynamics [16], LGBM effectively captures the inherent uncertainty and complexity of badminton gameplay. 

In Figure 3, the model is conceptualized as a variational autoencoder. The encoder maps the rally's state sequence into a rally context while projecting the current state into latent space to derive the Current Latent State and intermediate states. To simulate geometric Brownian motion in latent space, we adopted a stochastic differential equation (SDE) approach, as described in [17]. Variational infer- 

ence in SDEs allows us to parameterize both the prior and approximate posterior: 



Here,  hθ and hϕ are the target drift function and the player drift function, respectively. Both processes share the same function σ. 

The target drift function in the encoder leverages rally context, embedding future information. This enables the latent trajectory produced by the encoder to serve as a target for the decoder, encouraging the player's latent trajectory to align closely with the target's latent trajectory. To achieve this, we minimize the KL divergence between the two trajectories [17], ensuring that the model learns how to represent rally state dynamics as geometric Brownian motion in latent space. During inferencing, the decoder uses the current state to predict future latent states, which guide gameplay decisions. Since displacement in latent space corresponds to agent decisions, the geometric Brownian motion (LGBM) incorporates the opponent’s actions into the agent’s decision-making. 

Unlike RallyNet, which simulates only the next shot, RallyNetv2 learns by simulating entire rallies. This longer horizon enables agents to base decisions on extended future outcomes, achieving performance that more closely mirrors real players. The action projection layer translates latent positions zt into actionable outputs for interaction with the opponent. Specifically: 

- **For shot type selection** : A linear layer maps the latent position zt to predict the shot type. 

- **For landing and moving position** : Landing and movement are modeled as weighted bivariate normal distributions, reflecting the multiple viable options in badminton. Two linear layers parameterize these distributions, from which landing and movement positions are sampled. 

Finally, the concatenated shot type, landing position, and movement position define the agent’s action, which interacts with the environment and determines the opponent's next state. This structure ensures realistic gameplay simulation, capturing both agent decision-making and opponent interactions. 

### **3.1.3. Realism Action Constraint** 

In the existing simulation environment, a set of **Constraint mechanisms** based on historical data statistics have been added to study the correlation between player actions and other factors. This is used to judge and limit the actions of the simulated player (agent), aiming to enhance the realism and 



6 

complexity of the match simulation. When the model generates unreasonable actions, this function will immediately correct them, adjusting the actions to results that are more aligned with actual match scenarios. 

####  **Shot Type Constraint** 



**Figure 4.** By using Cramer's V, we found that hit location, Y-axis movement, and opponent’s shot type moderately correlated with shot selection. 

To ensure that the agent's actions reflect real-world scenarios, we implemented restrictions to prevent arbitrary shot selection. Using historical data, we analyzed the relationships between an agent's shot type and key factors, including movement along the x and y axes, the agent’s location during the shot, the opponent's location, and the opponent's shot type. The analysis, shown in Figure 4, highlighted moderate correlations between hit location, opponent shot types, and agent movement along the y-axis. 

Figure 5's statistical analysis shows that if the probability of a specific shot type in a given context is below 2%, the agent is restricted from selecting it, with its probability redistributed among more realistic options. The 2% threshold accounts for potential labeling errors in the dataset, providing a practical constraint. For instance, when responding to an opponent's smash, the agent is limited to defensive lobs or net drops. Similarly, if the agent moves more than 0.25 units along the y-axis before returning the shuttlecock, it is restricted from selecting a smash. These constraints ensure the agent’s actions closely align with real-world behavior patterns observed in matches. 



**Figure 5.** Statistical distribution of the agent's shot types (percentages) based on opponent shot types (left) and y-axis movement (right). Shot types with a frequency below 2% (highlighted in red) are restricted for agent selection. 

####  **Landing Position Constraint** 



**Figure 6.** Cramer's V values identified the agent's shot type as the variable that most strongly correlated with the landing location of the agent’s shot. 



7 

We further investigated whether the landing position of the shuttlecock when the agent hits it is correlated with the opponent’s location or the shot type used by the agent. As shown in Figure 6, the landing location is closely related to both of these factors, with the shot type having the highest correlation with the landing location. As an example of this constraint, high clears tend to land mostly in the backcourt, while smashes and net drops are more likely to land in the frontcourt or midcourt areas. For certain shot types, there are clear restrictions on the landing locations; for instance, net shots cannot land in the backcourt. 





**Figure 7.** Statistics were gathered on the landing area of the player when hitting specific shot types (presented as percentages), with landing areas below 2% marked in red. This ensures that the agent cannot hit the landing location with a probability of less than 2 when facing specific shot types from the opponent. 

####  **Moving Location Constraint** 



**Figure 8.** Calculating the density distribution of the player's total movement distance, where a higher y- value indicates that the player moves that particular distance more frequently. 



8 

When the agent's movement exceeds the maximum value, the system will dynamically adjust its behavior, restricting the movement range within the maximum allowable distance in the same direction. This prevents the simulated agent from exhibiting unreasonable locationing behaviors that deviate from the logic of the game, and ensures that the simulation results are consistent with the statistical characteristics of real-life matches. 

### **3.2. Evaluation Modules** 

We provide three evaluation modules for the user to get better insight into the game, which are Shot Evaluation, Tactic Evaluation, and Visualization & Winning/Losing Reason Statistics. 

### **3.2.1. Shot Evaluation** 

For **Shot Evaluation** , we introduce **Shot Influence** [8], a specialized deep-learning model designed to assess the impact of individual shots on rally outcomes. The model evaluates shots by analyzing their immediate and cumulative effects on the trajectory of a rally, capturing both **short-term dynamics** and **long-term patterns** in player performance. 

The model’s output is visualized as a line graph, which tracks win probability changes throughout the rally. Each shot is evaluated for its contribution to the player’s win probability, providing a dynamic, shot-by-shot view of how the rally evolves. 



**Figure 9.** Illustration of how to interpret the Rally Shot-by-Shot Momentum and Pace Plot. (a) A sharp drop in Kento Momota’s win probability occurs after the third round, (b) A fast-paced smash from the opponent in the fourth round reduces Momota's momentum, and (c) Rapid fluctuations in win probability occur toward the end of the rally. 

While the Shot Influence model offers powerful predictions, its deep-learning nature inherently limits interpretability. To address this, we enhance the analysis with complementary visualizations such as the **Rally Shot-by-Shot Momentum and Pace Plot** and **Rally Length vs. Energy Expenditure Diagram** . 

In the Rally Shot-by-Shot Momentum and Pace Plot, pace (P) is defined as the player’s shot speed, calculated as: 





9 

where Δt is the frame difference between the shuttle leaving the player's racket and reaching the opponent's side. Next, momentum is represented by the sign of the pace. Positive momentum (+P) indicates that the player is hitting above the net, while negative momentum (−P) indicates hitting below the net. This distinction highlights whether the player is maintaining or losing control of the rally. 



In the Rally Length vs. Energy Expenditure Diagram, energy expenditure (E) is calculated as: 

where: 

- The opponent's Shot Pace measures how fast the opponent's shuttle travels. 

- The player's Recovery Speed is the speed of the player returning to an optimal position after hitting a shot. 

A higher opponent shot pace increases the energy cost, while a slower recovery speed indicates greater fatigue for the player. 

In addition to rally-level analysis, Figure 19 provides match-level differences based on shot types for comparison. The average win probability grouped by shot type across each match is calculated to evaluate the effectiveness of various shots in securing points. For pace with momentum, average delta values (representing changes in rally pace after each shot) are used to highlight how specific shot types influence momentum shifts. By incorporating these two metrics—win probability and delta pace—the grouped bar chart format enables easy visual comparison across matches, helping to identify trends or deviations in shot performance. 

In Figure 20(b) , the densities are calculated using Kernel Density Estimation (KDE). KDE evaluates the density of shuttlecock landing positions or player moving positions by smoothing the data points into a continuous surface. The contours represent equal densities, while the higher exaggeration lines represent higher density values. 

Figure 21 visualizes the differences in the distribution of shots of two specified matches for a given player, separately for winning and losing rallies. The KDE for the landing and movement positions are computed using Gaussian kernels, and the differences are obtained by subtracting one distribution from the other. Since the higher density difference corresponding to losing shots would be blue, which is counterintuitive to losing more, the color scheme is reversed to create a negative impression. 

### **3.2.2. Tactic Evaluation** 

Our goal for tactical evaluation is to visualize these tactics through data and definitions, providing an intuitive display of their actual usage and success rates. This not only helps clearly understand the application frequency and distribution characteristics of various behaviors in the match, but also assists players and coaches in identifying which factors significantly influence the success rate, helping them optimize match strategies and improve performance in actual competitions. 



10 

We referenced [18] and worked with badminton coaches to define three main tactical categories: Four-Corner, Full-Court Pressure, and Defensive Counterattack: 

**1. Full-Court Pressure** 

   - The player accumulates high points in a short time through aggressive offensive techniques (such as net shots, drop shots, and smashes) to apply Full-Court Pressure and quickly end the rally. 

**2. Defensive Counterattack** 

   - After the opponent launches an attack (such as a smash), the player transitions from a defensive state to a counterattack, achieving an effective Defensive Counterattack through precise drop shots, net shots, or smashes 

**3. Four-Corner** 

The player achieves strategic pressure by locking the landing points of shots to specific areas of the court (such as the left and right corners of the front or back court) or by utilizing a variety of landing point variations for Four-Corner. 

Within the **Four-Corner** tactic, there are five subtactics: **Forehand-Lock, Backhand-Lock, FrontCourt-Lock, BackCourt-Lock,** and **Four-Corners-Clear-Drop** : 

**1. Forehand Lock** 

The player stabilizes the landing point of the shot in a specific area on the forehand side of the court to maintain control of the court and accumulate points. 

**2. Backhand Lock** 

   - The player stabilizes the landing point of the shot in a specific area on the backhand side of the court, using precise control to weaken the opponent's counterattack ability. 

**3. FrontCourt Lock** The player concentrates the shots in a specific area of the front court to suppress the opponent and enhance the offensive advantage. 

**4. BackCourt Lock** 

   - The player stabilizes the landing point of the shot in a specific area of the backcourt (excluding smashes) to maintain defensive stability and wait for an opportunity to counterattack. 

**5. Four-Corner Clear Drop** The player continuously pulls and pushes by changing the landing points to specific areas in the four corners of the court, creating offensive opportunities and accumulating points. 

In the tactical classification process, we refined the tactical categories into four hierarchical levels, each representing varying levels of tactical detail. The first three levels were independently evaluated to ensure their definitions accurately captured match dynamics and strategic decisions. The levels are illustrated in Figure 10, with detailed definitions and corresponding abbreviations provided in the appendix. 

Using match data from two players, we analyzed and classified their tactics, followed by statistical comparisons. Specifically, we recorded the win rates and usage frequencies of different tactics for each player, and visualized their effectiveness by projecting them onto a 2D plane. Furthermore, we compared the players' tactical choices using bar charts to highlight similarities and differences, particularly their strategic preferences in critical match scenarios. This analysis provides insights into each player’s tactical strengths and characteristics while revealing differences in strategic styles. The process is depicted in Figure 10. 



11 



**Figure 10.** The tactical classification flow diagram illustrates the process of collecting rally data from the matches of two players. Each rally is individually assessed through tactical layer classification, analyzing the tactics used by the players. Finally, the tactics and win rates are statistically analyzed and visualized in charts, providing an intuitive presentation of the tactical usage results. 

### **3.2.3. Visualization & Winning/Losing Reason Statics** 

We calculate win/lose probabilities across different states, emphasizing the top winning and losing states along with their corresponding actions. The platform offers dynamic, interactive visualizations of match data, enabling coaches and players to analyze and prepare effectively. Through intuitive animations, users can seamlessly explore match dynamics, as illustrated in Figure 11. Moreover, we have developed an interactive web page that can run our three evaluation modules on it. 



**Figure 11.** Visualization & Winning/Losing Reason Statistics highlights top winning and losing states and the corresponding actions. 



12 

## **4. Experimental Results** 

This section addresses two key research questions: **(1) Can CoachAI+ simulate diverse player behavior across different game scenarios? (2) How to extract insights on winning and losing from CoachAI+ ?** We first evaluate the imitation accuracy of RallyNetv2, followed by demonstrations of the effectiveness of the evaluation modules and simulation capabilities using three selected matchups. 

### **4.1. Can CoachAI+ Simulate Diverse Player Behavior across Different Game Scenarios?** 

To assess the accuracy of the CoachAI+ Badminton Environment, we conducted experiments based on three key criteria, adapted from the goals proposed in RallyNetv2 for offline imitation learning in badminton: 

1. **Behavioral Sequence Similarity** : The agent's behavior should closely replicate real-world rallies, capturing shot sequences, shuttle trajectories, and player movements. 

2. **Rally Duration Realism** : The simulated rallies should reflect the length of actual gameplay, efficiently modeling player interactions. 

3. **Outcome Consistency** : Simulated rallies should produce results that align with real-world competitive dynamics. 

To evaluate RallyNetv2's performance in badminton analysis, we conducted rally reconstruction experiments using the ShuttleSet dataset, following the setup from RallyNet. The ShuttleSet dataset was split into 80% for training and 20% for testing. As shown in Figure 12, the task involves initializing the serving agent with a given state and simulating complete rallies through interaction, allowing for a detailed comparison of accuracy and suitability for badminton scenarios. 



**Figure 12.** An illustration of the agent in a badminton rally. In our experiments, the agent is provided with an initial state and is tasked with predicting the full rally sequence. 

### **4.1.1. Behavioral Sequence Similarity** 

We evaluated RallyNet and RallyNetv2 on the ShuttleSet dataset. Traditional alignment-based metrics such as MSE and Cross-Entropy are unsuitable due to the varying lengths of simulated and real rallies. Minor timing differences in executing tactics, such as the Four-Corner Tactic, which forces opponents to move extensively, should not overly influence decision sequence evaluations. To address this, we employed Dynamic Time Warping (DTW) to measure landing and movement position predictions and Connectionist Temporal Classification (CTC) loss to evaluate shot type predictions. These metrics effectively assess sequence similarity, even when sequences differ in length, ensuring accurate evaluation of generated versus real rallies. 



13 

**Table 1.** Quantitative results. 

|**Model**|**Landing Position (↓)**|**Shot Type (↓)**|**Moving Position (↓)**|
|---|---|---|---|
|**RallyNet**|**0.6449**|**26.5384**|**0.3424**|
|**RallyNetv2**|**0.2983**|**8.3533**|**0.1934**|



Table 1 compares the performance of RallyNet and RallyNetv2, showing that RallyNetv2 significantly outperforms RallyNet. By extending the LGBM interaction length for direct mapping to accurate mixed-action sequences, RallyNetv2 achieves notable improvements, aligning more closely with true action sequences. 

### **4.1.2. Rally Duration Realism** 

To evaluate whether the model accurately captures rally interactions, the ability to simulate errors at the correct moments is a key metric. This reflects whether the agent understands player limits, such as failing to return a shot or hitting out of bounds. Learning error patterns is particularly challenging due to their rarity—errors occur only once per rally, compared to more frequent in-bound interactions. 



**Figure 13.** The length distribution comparison is shown, with RallyNet results on the left and RallyNetv2 on the right. The orange distribution represents the ground truth rally lengths, while the blue distribution shows the generated rally lengths. 

Rally length also serves as an indicator of how well the model replicates realistic gameplay scenarios. Figure 13 presents a histogram of rally lengths, with Jensen–Shannon divergence (JSD) used to quantify the difference between the real and generated distributions. As shown, RallyNetv2 models more intricate strategies, producing rally length distributions that closely align with real-world data, outperforming RallyNet. 



14 

### **4.1.3. Outcome Consistency** 

To assess the outcome consistency of the learned models in replicating real player behavior, we simulated rallies and evaluated the average win rates for each player across all matchups. Simulations used the initial states from actual rallies to ensure accurate comparisons. RallyNet achieved a mean absolute error (MAE) of 9.5% for win rate, while RallyNetv2 reduced this to 7.4%. 

Additionally, we analyzed Carolina Marin, the player with the most rally data in the ShuttleSet test dataset, focusing on her top four matchups by rally count. As shown in Table 2, RallyNetv2 achieved an average difference of just 5.25% from actual win rates, outperforming RallyNet in replicating real match outcomes. These findings highlight RallyNetv2's superior ability to model realistic gameplay results. 

**Table 2. Simulated rally-level win rates comparing ground truth with learned agents for Carolina MARIN's top four matchups by rally count.** 

|**Matchup**|**An Se Young**|**Carolina**<br>**Neslihan Yigit**|**MARIN**<br>**Supanida**<br>**Katethong**|**Pornpawee**<br>**Chochuwong**|**Mean Differ-**<br>**ence**|
|---|---|---|---|---|---|
|**Ground Truth Win**<br>**Rate**|0.5517|0.6296|0.5918|0.6190|-|
|**RallyNet**|0.4942|0.3703|**0.5714**|0.5238|0.1081|
|**RallyNetv2**|**0.5172**|**0.5185**|0.5510|**0.5952**|**0.0525**|



In conclusion, the experimental results demonstrate that RallyNetv2 outperforms the state-of-theart RallyNet in capturing players' decision patterns with greater precision. By refining LGBM’s learning objectives, it achieves direct mapping to accurate mixed-action sequences. We believe RallyNetv2 can serve as a more effective agent in the environment, enabling more realistic interactions in badminton simulation environments. 

### **4.2. How to Extract Insights on Winning and Losing from CoachAI+** 

In this subsection, we demonstrate the benefits of the CoachAI+ Badminton Environment's evaluation module and its simulation capabilities. The primary goal of the system is to provide actionable insights for coaches and players, enabling targeted training and tactical preparation. 

The system offers two key applications. When sufficient historical match data are available, the evaluation modules analyze the data directly to extract insights. In scenarios with limited or unavailable match data for specific player matchups, the simulation function generates matches, which can then be analyzed to provide insights. This allows players and coaches to gain a competitive edge by accessing valuable information even in data-scarce situations. 

It is important to note that the evaluation modules aim to help identify strengths and weaknesses between players, but do not directly offer "winning strategies." Instead, they serve as a tool for deeper tactical understanding and preparation. 



15 

### **4.2.1. Evaluating Historical Matches** 

We present two scenarios to demonstrate the application of the CoachAI+ Badminton Environment for analyzing historical matches: **single-match analysis** and **cross-match comparisons** . To illustrate, we selected two matchups and applied various evaluation modules to extract diverse insights, highlighting the environment's analytical capabilities. 

### **4.2.1.1. Single-Match Analysis** 

#### **Kento Momota vs. Viktor Axelsen Malaysia Masters 2020 Finals match** 

In this match, Momota emerged victorious. By using our system, we highlight Momota's strengths and potential weaknesses, demonstrating the effectiveness of the Evaluation Modules. We summarize the observations as follows: 

####  **Kento Momota favors longer rallies** 



**Figure 14.** In Set 2, Kento Momota wins the first several long rallies. Viktor Axelsen wins some shorter rallies near the end of the set, but his energy cost is significantly higher compared to Momota. 

Figure 14 presents the "Rally Length vs. Energy Expenditure Diagram," where the line depicts energy expenditure and the bar chart illustrates the length of each rally. The analysis reveals that Momota tends to win longer rallies. Even in shorter rallies, his playing style forces Axelsen to expend more energy, showcasing Momota’s tactical advantage in maintaining control and dictating pace. 

####  **Kento Momota's frequent use in the "Four-Corner" tactic.** 

Figure 15 shows that Kento Momota uses the Four-corner play most frequently, despite its low win rate. However, Figure 14 reveals that he has an advantage during long rallies. This suggests that Kento Momota's frequent use of the Four-corner play is likely a strategy to extend rallies and gain an advantage. 



16 



**Figure 15.** The scatter chart illustrates the win rate and frequency of tactics used by both players. Momota has a high win rate in DC rallies and over 50% using Four-Corner. 

####  **Kento Momota's ability to shift momentum, especially under pressure** 



**Figure 16.** The Shot Influence prediction (left) and Pace Plot (right) provide complementary insights into how Kento Momota’s performance influences rally outcomes, highlighting his strategic resilience and ability to shift momentum, especially under pressure. 

Figure 16 illustrates the 15th rally of Set 2, where Kento Momota served. Momota, known for his Defensive Counterattack style, demonstrates a higher win probability when receiving net shots. This is due to his ability to respond effectively to risky net plays without compromising his position. In this rally, his opponent’s net shot increases the likelihood of an immediate loss, which ultimately occurs and results in Momota's win. Additionally, Figure 16 highlights Momota's resilience under pressure from Viktor Axelsen. Despite receiving a fast-paced smash from his opponent, Momota's smash defense enables him to not only withstand the attack but also turn the rally in his favor. This aligns with his playing style, and the ability to shift momentum during high-pressure moments. 



17 

####  **Momota excels with left-side landing position** 



**Figure 17.** Visualize the area analyzed in this section.(left). Shows Kento Momota's top 1 win reason: the opponent missing the shot(middle).  Shows Kento Momota's top 1 lose reason: out of bound (right). 

In Figure 17, we visualize the match progress by dividing the court into 10 areas (9 within the court and 1 out-of-bounds area) to analyze the distribution of winning and losing actions. Since importing data from only one set may not provide reliable statistical results, we imported all of Momota's past match data for analysis in this module. The findings show that Momota's winning shots often land on the left side of the court, while his most common mistake is hitting the shuttle out of bounds, particularly when both players are positioned near the center. This pattern aligns with his Four-Corner tactical style, which emphasizes boundary-line placements and actively maneuvering the opponent. 

By analyzing match data from multiple sets and leveraging the insights from the various evaluation modules, we gain a comprehensive understanding of Momota's strengths. Future opponents should focus on building stamina and preparing specific defensive strategies, particularly against his forehand smashes and tactical court movements. These insights not only enhance our understanding of Momota's style, but also provide a framework for improving player strategies when facing him in competition. 

### **4.2.1.2. Cross-Match Comparisons** 

#### **Viktor Axelsen vs. Anthony Sinisuka Ginting Indonesia Masters 2020 Semi-finals, and the YONEX THAILAND OPEN 2021 Semi-finals.** 

In this case, we analyze both player’s strengths and weaknesses in the Indonesia Masters 2020 Semifinals, and the YONEX THAILAND OPEN 2021 Semi-finals. In their two meetings, Viktor Axelsen lost the first one, but won the second. We demonstrate, from Viktor Axelsen's perspective, how to utilize the match comparison feature to uncover the key factors contributing to his victories. The findings are summarized as follows: 



18 

####  **Inconsistent win rates of  Viktor Axelsen for DC and FCP, while FC and FhL were more effective.** 





**Figure 18.** Illustrates the win rate and frequency of tactics used by both players in the Indonesia Masters 2020 Semi-finals (left) and YONEX THAILAND OPEN 2021 Semi-finals (right). 

In Figure 18, we observe that the tactics Defensive Counterattack (DC) and Full-Court Pressure (FCP) had inconsistent win rates. Additionally, the two tactics were more demanding to execute. The usage rates of both tactics were generally below 0.1, limiting their effectiveness to match outcomes. In contrast, Four-Corner (FC) has a higher usage rate throughout the matches. When Axelsen wins, Four-Corner (FC) is used more frequently, indicating that it plays a key role in determining match outcomes. Under the tactic category Four-Corner (FC), we compare the overall performance of the 5 subtactics. The subtactic Forehand Lock (FhL) has the highest win rate in both matches. In Match II, where Axelsen won, FhL's significantly higher usage and exceptional win rate demonstrate its effectiveness in both quantity and quality. 

Based on the results of the above analysis, our recommendation is that Viktor Axelsen could execute more Forehand Lock (FhL) tactics to capitalize on Anthony Sinisuka Ginting’s weaknesses, or undergo specialized training to strengthen this tactic prior to matches against Anthony Sinisuka Ginting, enabling its frequent usage in matches. 

####  **Viktor Axelsen’s Push Shots significantly improve win probability, yet the pace decreases.** 





19 

**Figure 19.** Compares Viktor Axelsen’s average win probability (left) and average delta pace (right) by shot type across the Indonesia Masters 2020 Semi-finals and the YONEX THAILAND OPEN 2021 Semifinals. 

In Figure 19, we observed that the shot type Push Shot has one of the greatest average win probability increases between the two matches. However, counter intuitively, the delta pace is much lower in the second match. 

This suggests that when Viktor Axelsen performs Push Shots, he could slightly reduce the pace of the shot. A similar pattern can be observed in the increased win rates for Smashes and Drops, where the pace of play also decreases. For Viktor Axelsen, it might be more effective to slow down the overall rally tempo, and to deliver Push Shots, Smashes, and Drops with greater precision. 

####  **Comparing landing position and movement of Viktor Axelsen’s  smash** 



**Figure 20.** (a) Comparing the distribution of Smash landing positions by category . (b) Showing the player's movement after shots. Both (a) and (b) display data from the Indonesia Masters 2020 Semifinals (left) and the YONEX Thailand Open 2021 Semi-finals (right). 

Figure 20 highlights Viktor Axelsen's weakness on the backhand side during the Indonesia Masters 2020 Semi-finals and the amplified disadvantage in the YONEX THAILAND OPEN 2021 Semi-finals. 

Incorporating the shot type evaluation feature, it is shown that in the second match where Viktor Axelsen executed Smashes with overall slower pace, the net errors were reduced, and more winners were successfully delivered towards the opponent's backhand side. In order to further evaluate Axelsen’s smash, we then utilized the feature for comparing shuttlecock landing position and player moving position distributions across different matches. 



20 

####  **KDE difference shows Viktor Axelsen’s weakness of his backhand area being targeted** 





**Figure 21.** Illustration of the density difference obtained by subtracting the KDE of the Indonesia Masters 2020 Semi-finals from the KDE of the YONEX THAILAND OPEN 2021 Semi-finals for Viktor Axelsen. 

In Figure 21, higher values (blue) in the winning rallies graph (left) indicate more winning rallies in the YONEX THAILAND OPEN 2021 Semi-finals, while lower values (red) correspond to fewer winning rallies. In the losing rallies graph (right), higher values (red) indicate more losing rallies in the YONEX THAILAND OPEN 2021 Semi-finals, while lower values (blue) correspond to fewer losing rallies. 

We observe that on the forehand side, Viktor Axelsen seizes more opportunities to attack down the line with fewer point losses. Throughout both matches, he struggles to win when delivering Smashes on the backhand side. On the backhand side, Axelsen was forced to back up more to execute Smashes, and was unable to recover to an appropriate returning position after Smash shots were performed. This weakness was amplified in the YONEX THAILAND OPEN 2021 Semifinals. Backhand side Smashes allowed Ginting to execute high quality Net Shot returns, resulting in a lower win rate in the corresponding area. 

Notice the similarities of the shuttlecock landing positions in the two matches. Axelsen’s Smashes towards Ginting’s forehand often result in point losses. Smashes were more effective targeting the backhand side, achieving a higher win rate and generating more winners. 

To reduce the weakness of the backhand area being targeted, specific training focused on this scenario can be incorporated. Adjusting the pace during smashes may help ensure the player is in an optimal position when the opponent returns the shot. In terms of shot selection, he should 



21 

avoid returning smashes or drops when dealing with deep backhand shots. Instead, he should opt for clears, which result in fewer points lost in the same area. When choosing to smash, he should aim for cross-court shots to target Ginting's backhand side weakness. 

####  **FhL remains Axelsen's most effective tactic; backhand Smashes cost points.** 





**Figure 22.** Provides a comparison with another match up, the DAIHATSU INDONESIA MASTERS 2022 Semi-finals, highlighting the significance of the Forehand Lock (FhL) tactic (left) along with his stroke placement and movement distribution patterns (right). 

To validate our analysis, we evaluate a future match up between Viktor Axelsen and Anthony Sinisuka Ginting, the DAIHATSU INDONESIA MASTERS 2022 Semi-finals, where Axelsen won the match in straight sets. It’s shown in  Figure 22. that Forehand Lock (FhL) persists to be the most productive tactic, achieving both a high usage rate and a high win rate. Furthermore, examining Viktor Axelsen's Smash landing position distribution in this match reveals a similar pattern to previous matches, where Axelsen loses more points when executing backhand-side Smashes. The lost rallies were primarily those targeting the opponent's forehand. 

### **4.2.2. Simulating Future Matches** 

In cases where game data between two players is insufficient, we can leverage the simulated functionality of the CoachAI+ environment to generate synthetic game data. To validate the accuracy of the simulations, we selected players who have faced each other and have recorded matches in ShuttleSet22, but are not included in the ShuttleSet dataset. We simulated an entire set starting from a 0- 0 score and used evaluation modules to assess the simulation’s accuracy. Figure 23 shows that the shot distribution and tactical patterns of Victor Axelsen in the simulation closely match those observed in real matches. 

Analysis of the tactical usage reveals that both the real and simulated games mostly feature the FourCorner (FC) tactic, with the Defensive-Counterattack (DC) and Full-Court Pressure (FCP) tactics being used less frequently. Observing landing distribution, both simulation and the real match show that his lob shots scored more points in the top-right corner and lost more points in the left area. 



22 



**Figure 23.** The tactics distribution and landing position distribution of ‘lob’ by Victor Axelsen  when playing against LEE Zii Jia in the Semi-final of the INDONESIA OPEN 2022 and by simulation in CoachAI+ environment. 

## **5. Conclusion and Future Works** 

The CoachAI+ Badminton Environment presents a robust platform for realistic match simulations and in-depth performance evaluations. By combining advanced imitation learning models with datadriven and constraint-based approaches, it delivers actionable insights that can aid coaches and players in refining strategies and optimizing performance. This system bridges the gap between data analysis and practical application, making it a valuable tool for enhancing player training and influencing the methodologies used in competitive preparation. 

In our future work, we envision integrating large language models (LLMs) into the CoachAI+ Badminton Environment to provide tailored insights and recommendations in natural language, making strategic guidance more accessible and actionable for coaches and players. Additionally, the system could allow for customizable constraints, enabling the simulation of specific scenarios, such as a player managing a recent injury or other context-specific conditions, to better prepare for real-world challenges. Furthermore, incorporating reinforcement learning could enhance the system's capability to explore optimal strategies for winning under various circumstances or against specific opponents, offering a more dynamic and adaptive approach to tactical planning. These advancements would further solidify the platform's role as a comprehensive tool for training, strategy refinement, and performance enhancement. 



23 

## **Reference** 

- [1] K.-S. Chang, W.-Y. Wang and W.-C. Peng, "Where Will Players Move Next? Dynamic Graphs and Hierarchical Fusion for Movement Forecasting in Badminton," in _Thirty-Seventh AAAI Conference on Artificial Intelligence, AAAI 2023, Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence, IAAI 2023, Thirteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2023, Washington, DC, USA, February 7-14, 2023_ , 2023. 

- [2] X. Chen, W.-Y. Wang, Z. Hu, D. Reynoso, K. Jin, M. Liu, P. J. Brantingham and W. Wang, "PlayBest: Professional Basketball Player Behavior Synthesis via Planning with Diffusion," in _Proceedings of the 33rd ACM International Conference on Information and Knowledge Management, CIKM 2024, Boise, ID, USA, October 21-25, 2024_ , 2024. 

- [3] S. Engen, "Stochastic growth and extinction in a spatial geometric Brownian population model with migration and correlated noise," _Mathematical Biosciences,_ vol. 209, p. 240–255, 2007. 

- [4] A. Feinberg, "Markov Decision Processes: Discrete Stochastic Dynamic Programming (Martin L. Puterman)," _SIAM Rev.,_ vol. 38, p. 689, 1996. 

- [5] S. Greydanus, A. Koul, J. Dodge and A. Fern, "Visualizing and Understanding Atari Agents," in _Proceedings of the 35th International Conference on Machine Learning, ICML 2018, Stockholmsmässan, Stockholm, Sweden, July 10-15, 2018_ , 2018. 

- [6] L.-C. Huang, N.-Z. Hseuh, Y.-C. Chien, W.-Y. Wang, K.-D. Wang and W.-C. Peng, "A Reinforcement Learning Badminton Environment for Simulating Player Tactics (Student Abstract)," in _Thirty-Seventh AAAI Conference on Artificial Intelligence, AAAI 2023, Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence, IAAI 2023, Thirteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2023, Washington, DC, USA, February 7-14, 2023_ , 2023. 

- [7] H. M. Le, P. Carr, Y. Yue and P. Lucey, "Data-driven ghosting using deep imitation learning," 2017. 

- [8] X. Li, T.-K. L. Wong, R. T. Q. Chen and D. Duvenaud, "Scalable Gradients for Stochastic Differential Equations," in _The 23rd International Conference on Artificial Intelligence and Statistics, AISTATS 2020, 26-28 August 2020, Online [Palermo, Sicily, Italy]_ , 2020. 

- [9] C. Perin, R. Vuillemot, C. D. Stolper, J. T. Stasko, J. Wood and S. Carpendale, "State of the Art of Sports Data Visualization," _Comput. Graph. Forum,_ vol. 37, p. 663–686, 2018. 

- [10] K. Suganthi and G. Jayalalitha, "Geometric brownian motion in stock prices," in _Journal of Physics: Conference Series_ , 2019. 

- [11] K.-D. Wang, "Enhancing Badminton Player Performance via a Closed-Loop AI Approach: Imitation, Simulation, Optimization, and Execution," in _Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, CIKM 2023, Birmingham, United Kingdom, October 21-25, 2023_ , 2023. 

- [12] K.-D. Wang, W.-Y. Wang, P.-C. Hsieh and W.-C. Peng, "Offline Imitation of Badminton Player Behavior via Experiential Contexts and Brownian Motion," in _Machine Learning and Knowledge Discovery in Databases. Applied Data Science Track - European Conference, ECML PKDD 2024, Vilnius, Lithuania, September 9-13, 2024, Proceedings, Part X_ , 2024. 



24 

- [13] K.-D. Wang, W.-Y. Wang, Y.-T. Chen, Y.-H. Lin and W.-C. Peng, "The CoachAI Badminton Environment: A Novel Reinforcement Learning Environment with Realistic Opponents (Student Abstract)," in _Thirty-Eighth AAAI Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence, IAAI 2024, Fourteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2014, February 20-27, 2024, Vancouver, Canada_ , 2024. 

- [14] K.-D. Wang, Y.-T. Chen, Y.-H. Lin, W.-Y. Wang and W.-C. Peng, "The CoachAI Badminton Environment: Bridging the Gap between a Reinforcement Learning Environment and RealWorld Badminton Games," in _Thirty-Eighth AAAI Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence, IAAI 2024, Fourteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2014, February 20-27, 2024, Vancouver, Canada_ , 2024. 

- [15] W.-Y. Wang, W.-W. Du, W.-C. Peng and T.-U. Ik, "Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset," in _Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, IJCAI 2024, Jeju, South Korea, August 3-9, 2024_ , 2024. 

- [16] W.-Y. Wang, T.-F. Chan, H.-K. Yang, C.-C. Wang, Y.-C. Fan and W.-C. Peng, "Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches," in _IEEE International Conference on Data Mining, ICDM 2021, Auckland, New Zealand, December 7-10, 2021_ , 2021. 

- [17] W.-Y. Wang, T.-F. Chan, W.-C. Peng, H.-K. Yang, C.-C. Wang and Y.-C. Fan, "How Is the Stroke? Inferring Shot Influence in Badminton Matches via Long Short-term Dependencies," _ACM Trans. Intell. Syst. Technol.,_ vol. 14, p. 7:1–7:22, 2023. 

- [18] W.-Y. Wang, H.-H. Shuai, K.-S. Chang and W.-C. Peng, "ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles for Stroke Forecasting in Badminton," in _Thirty-Sixth AAAI Conference on Artificial Intelligence, AAAI 2022, Thirty-Fourth Conference on Innovative Applications of Artificial Intelligence, IAAI 2022, The Twelveth Symposium on Educational Advances in Artificial Intelligence, EAAI 2022 Virtual Event, February 22 - March 1, 2022_ , 2022. 

- [19] W.-Y. Wang, Y.-C. Huang, T.-U. Ik and W.-C. Peng, "ShuttleSet: A Human-Annotated StrokeLevel Singles Dataset for Badminton Tactical Analysis," in _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD 2023, Long Beach, CA, USA, August 6-10, 2023_ , 2023. 

- [20] 王志全 and 張家昌, "以 SWOT 分析探討羽球單打戰術," 中華體育季刊 _,_ vol. 22, p. 128–135, 2008. 



25 

## **Appendix** 

### **Tactic Detailed Definition:** 

#### **1. Full-Court-Pressure:** 

The player scores 1 point for a net shot or slice and 2 points for a smash; other shot types score 0 points. If the player accumulates 3 points in 2 shots, the interval is defined as FullCourt Pressure. If the player scores 4 points in 3 shots or 5 points in 4 shots, it also counts as Full-Court Pressure (excluding shots with 0 points at the beginning or end of the interval). 

#### **2. Defensive Counterattack** 

After the opponent performs a smash, the player receiving enters a defensive state. If the player performs a smash, slice, or net shot from a defensive state, it is considered executing Defensive-Counterattack, starting from the beginning of the defensive state until the smash is completed. 

#### **3. Four-Corner** 

The tactic is based on five subtactics: Forehand Lock, Backhand Lock, Front-Court Lock, Back-Court Lock, and Four-Corner Clear Drop. If one of the subtactics is executed, it's defined as a Four-Corner. 

### **SubTactic Detailed Definition:** 

#### **1. Four-Corner Clear Drop** 

The player’s shot placement differs from the previous one and lands in zones 1, 2, 5, or 6 (refer to Figure 25), scoring 1 point per occurrence. If the player accumulates 3 points in 4 shots and the last shot contributes a positive score, the interval is defined as Four-Corner Movement. 

#### **2. Forehand Lock** 

The player’s shot lands in zones 3 or 5 in Figure 25, scoring 1 point per occurrence. If the player accumulates 2 points in 4 shots and both the first and last shots contribute positive scores, the interval is defined as Forehand Lock. 

#### **3. Backhand Lock** 

The player’s shot lands in zones 4 or 6 in Figure 25, scoring 1 point per occurrence. If the player accumulates 2 points in 4 shots and both the first and last shots contribute positive scores, the interval is defined as Backhand Lock. 



26 

#### **4. FrontCourt Lock** 

The player’s shot lands in zones 1 or 2 in Figure 25, scoring 1 point per occurrence. If the player accumulates 2 points in 3 shots and both the first and last shots contribute positive scores, the interval is defined as FrontCourt Lock. 

#### **5. BackCourt Lock** 

The player’s shot lands in zones 5 or 6 in Figure 25 and is not a smash, scoring 1 point per occurrence. If the player accumulates 2 points in 4 shots and both the first and last shots contribute positive scores, the interval is defined as BackCourt Lock. 



**Figure 24.** Tactics and corresponding Abbreviation. 



**Figure 25.** Assigned number of Court area for define tactics. 



27 


