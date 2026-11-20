<!-- source: library/preprints/arXiv/2026/2026 - MyoChallenge 2025 A New Benchmark for Human Athletic Intelligence - Wang et al.pdf -->
<!-- item: https://arxiv.org/abs/2605.15650 -->
<!-- authors: Cheryl Wang, Chun Kwang Tan, Balint K. Hodossy, Eric Lyu, Jun Guo, Wentao Zhao, Huaping Liu, Chengkun Li, Merkourios Simos, Bianca Ziliotto, Alexander Mathis, Siyuan Liu, Jiahao Chen, Shanlin Zhong, Bo Jiang, Ci Song, Yaoye Zhu, Chenhui Zuo, Yanan Sui, Mohamed Irfan Refai, Massimo Sartori, Guillaume Durandau, Vikash Kumar, Vittorio Caggiano -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-20; equations, tables and figures are NOT preserved - consult the PDF for those -->

# MyoChallenge 2025: A New Benchmark for Human Athletic Intelligence

                                         MyoChallenge 2025: Benchmark Design, Competition
                                         Results, and Lessons for Human Athletic Intelligence


                                           Cheryl Wang1∗ Chun Kwang Tan2∗ Balint K. Hodossy 3∗ Eric Lyu4 Jun Guo5†
                                          Wentao Zhao5† Huaping Liu5† Chengkun Li6‡ Merkourios Simos6‡ Bianca Ziliotto6‡
                                           Alexander Mathis6‡ Siyuan Liu7§ Jiahao Chen7§ Shanlin Zhong7§ Bo Jiang 7§
                                           Ci Song7§ Yaoye Zhu5¶ Chenhui Zuo5¶ Yanan Sui5¶ Mohamed Irfan Refai 8
arXiv:2605.15650v2 [cs.RO] 18 Nov 2026




                                            Massimo Sartori8 Guillaume Durandau1 Vikash Kumar9 Vittorio Caggiano4
                                                         1
                                                             McGill University, Canada 2 Nanyang Technological University, Singapore
                                                                  3
                                                                    Imperial College London, UK 4 King’s College London, UK
                                                                5
                                                                   Tsinghua University, China 6 EPFL, Switzerland 7 CASIA, China
                                                                       8
                                                                         University of Twente, Netherlands 9 MyoLab, USA

                                                         †                   ‡                            §                  ¶
                                                             Team ActingAI       Team Servette MyoClub        Team BioSyn        Team LNSGroup



                                                                                              Abstract

                                                     Athletic performance represents the pinnacle of human motor intelligence, de-
                                                     manding rapid choices, precise control, agility, and coordinated physical execution.
                                                     Although recent advances in robotics have demonstrated remarkable capabilities
                                                     in replicating complex human movements, these achievements provide limited
                                                     insight into the underlying neuromuscular coordination that enables such behaviors.
                                                     Understanding how the nervous system recruits and coordinates muscles during
                                                     athletic movements remains challenging, as complex muscle activation patterns are
                                                     difficult to measure directly in vivo, particularly during dynamic, high-intensity
                                                     activities. To bridge this fundamental gap in understanding, MyoChallenge at
                                                     NeurIPS 2025 established a pioneering benchmark for motor control intelligence in
                                                     sports, leveraging high-fidelity musculoskeletal models within physics simulation
                                                     combined with machine learning-driven algorithms. The competition introduced
                                                     two distinct tracks emphasizing either upper or lower limbs control: a table tennis
                                                     rally task utilizing a biomechanic upper limb model composed of an arm with
                                                     a hand (MyoArm) and a trunk (MyoTorso); and a soccer penalty kick using a
                                                     biomechanic model of legs (MyoLeg) and a trunk (MyoTorso). Marking the fourth
                                                     iteration of the MyoChallenge series, this event attracted almost 70 teams and over
                                                     560 submissions globally, uniting a diverse community ranging from physicians
                                                     and neuroscientists to machine learning experts. The competition facilitated the
                                                     development of several state-of-the-art control algorithms for the musculoskele-
                                                     tal system capable of sports agility, leveraging techniques such as physics-based
                                                     motion planners, on-policy behaviour cloning, hierarchical planning, and muscle
                                                     synergies. By integrating standardized tasks and physiologically realistic mod-
                                                     els into the open-source framework of MyoSuite, MyoChallenge’25 serves as a
                                                     reproducible and reusable testbed to accelerate interdisciplinary research across
                                                     machine learning, biomechanics, sports science, and neuroscience. Project page:
                                                     https://www.myosuite.org/myochallenge/myochallenge-2025

                                            ∗ co-first




                                         40th Conference on Neural Information Processing Systems (NeurIPS 2026). Track on Evaluations and Datasets.
1   Introduction




                       A                                                   B
Figure 1: Two tracks of MyoChallenge 2025. A. The Table Tennis track in which an agent is required
to hold a paddle and return an incoming table tennis ball B. The Soccer track where the agent needs
to score a penalty goal with or without a goalie.
Human athletic performance represents one of the most complex manifestations of sensorimotor
intelligence, involving continuous control over high-dimensional musculoskeletal (MSk) systems
in dynamically changing environments. Understanding human athletic intelligence is a critical
pursuit for advancing artificial intelligence systems [1]. Recent advances in humanoid robotics
have demonstrated remarkable capabilities in human-like coordination, agile locomotion, and highly
dynamic athletic behaviors, including acrobatics and martial arts [2, 3, 4, 5], navigating uncertain
terrain [6], and collaborating with humans in real time [7]. However, reproducing human-like
motion and understanding how such behaviors emerge under physiological constraints remain distinct
research objectives. Most humanoid robotic systems rely on simplified actuation models that do
not capture the nonlinear muscle–tendon dynamics, delayed force generation, and redundancy
characteristic of human MSk systems. Studying athletic behaviors under these constraints is essential
for understanding human muscle coordination and adaptive motor control.
Understanding muscle recruitment patterns during athletic movement is also crucial for investigating
human motor coordination, recovery, and performance training. Studying athletic behavior under
fast, dynamic, and uncertain conditions offers a unique opportunity to understand how the body
integrates perception, prediction, and control with applications in prosthetics, rehabilitation, and
assistive technologies [8, 9, 10, 11, 12]. In addition, these studies can enhance biomechanically
grounded animation, virtual athletics, and embodied AI agents in simulation environments [13].
Previous MSk research in sports science has largely focused on isolated kinetic performance [14]
or estimating muscle forces during specific athletic tasks [15, 16, 17]. Furthermore, these forward
simulations are generally restricted to partial body segments and rely heavily on tracking captured
MoCap data, limiting their ability to simulate generalized, whole-body sports movements.
In recent years, the community has seen substantial progress across computational biomechanics
and ML[18, 19, 20, 21, 22, 23], assistive technologies [24, 25, 26], and physics-based simulation
[27, 28, 29, 30]. Within computational biomechanics, several benchmarks have emerged over the
past decade to evaluate assistive devices [31, 32] and general human motor control [33, 34, 35, 36,
37]. However, no public benchmark currently integrates high-fidelity, full-body MSk models with
interactive, physically simulated sports environments. Developing such a benchmark is essential to
systematically evaluate the capabilities and limitations of current learning-based approaches under
physiologically grounded muscle actuation.
To address this gap, we introduce MyoChallenge 2025: Towards Human Athletic Intelligence, a
competition designed to benchmark sports agility using MSk simulations. This work aims to advance
the development of realistic biomechanical digital twins of humans, seeking to answer a central
question: Can physiological digital twins achieve human-level coordination during complex sports
activities? The competition features two independent tracks focused explicitly on upper and lower
limb coordination. Crucially, these challenges go far beyond static or repetitive motions and demand
generalization through reactive, adaptive embodied behaviors, requiring real-time perception-action
loops for agile motor control. By providing a reproducible benchmark for complex sports tasks,


                                                 2
Table 1: Comparison of musculoskeletal models across MyoChallenge years. The highlighted rows
denote the MyoChallenge 2025 environments introduced in this work.
Model                      Challenge Year Embodiment                      Jointsa DoFs Muscles Core task
                                                                                                      Die reorientation and Baoding-ball
MyoHand                           2022         Biological hand              23       23       39
                                                                                                      manipulation
                                                                                                      Reaching, grasping, and object
MyoArm                            2023         Unilateral upper limb        38       27       63
                                                                                                      relocation
                                                                                                      Goal-directed chase-tag
MyoLeg                            2023         Biological lower body        15       28       80
                                                                                                      locomotion
                                               Biological arm with                                    Biological–prosthetic coordination
MyoMPL                            2024                                      55       44    63 + 17b
                                               MPL prosthesis                                         and object handover
                                               Transfemoral limb                                      Prosthetic locomotion over varied
MyoOSL                            2024                                      17       22       54
                                               with OSL prosthesis                                    terrain
MyoArm +                                       Upper limb with                                        Moving-ball interception, timed
                                  2025                                      56       45    273 + 2c
MyoTorso                                       articulated torso                                      contact, and repeated rallying
MyoLeg +                                       Lower body with                                        Locomotion, stabilization, ball
                                  2025                                      33       46      290
MyoTorso                                       articulated torso                                      approach, and timed kicking
a
    Joint counts follow MuJoCo’s definition and therefore need not equal the number of anatomical joints. b Includes 17 prosthetic actuators.
c
    Includes two pelvis-position actuators.

MyoChallenge aims to advance the development and evaluation of neuromuscular control strategies,
with broader implications for biomechanical simulation, rehabilitation, and embodied intelligence.


2        The MyoChallenge’25 Competition

For three consecutive years, the MyoSuite team – a multi-university open-source and open-science
initiative to advance human musculoskeletal motor control – has hosted the MyoChallenge as an
official NeurIPS competition to advance the benchmark for controlling human digital twins using
frontier machine learning algorithms. Marking its fourth edition, MyoChallenge ’25 introduces two
athletic-intelligence tracks that substantially increase musculoskeletal and task complexity while
retaining separate focus on upper-limb control and locomotion (Table 1). Whereas previous editions
used models with at most 80 actuators, the 2025 Table Tennis and Soccer tasks require control of 275
and 290 actuators, respectively. The Table Tennis track extends previous upper-limb manipulation
tasks from object reorientation and relocation to grasping and orienting a paddle, intercepting a
moving ball, and directing its return, which requires precise contact timing and fluent upper-body
control. The Soccer track similarly extends previous lower-limb locomotion tasks by requiring
coordinated approach, balance, and a precisely timed kick against a moving goalkeeper. To keep these
added demands focused on the intended control challenges, pelvis translation was position-actuated
in Table Tennis, while the arms were omitted in Soccer.
The competition was divided into an opening phase and a playoff phase. In the initial phase, submis-
sions were evaluated using static environments with no task variations, encouraging participants of
all skill levels to test early solutions. Teams scoring above 10% advanced to the playoff phase, which
introduced significant environmental variations to test model robustness. The following sections
outline the simulation environment and musculoskeletal models (Sec. 2.1), the proposed tasks and
evaluation criteria (Sec. 2.2), and the results of the competition (Sec. 3).

2.1       Simulation Environment, Models, and Data

Simulation Framework The competition and the complete set of musculoskeletal models are
embedded within MyoSuite, an open-source collection of environments and tasks powered by the
MuJoCo physics engine [38]. MyoSuite provides physiologically realistic musculoskeletal models
[39] within a simulation framework that significantly surpasses the speed of state-of-the-art simulators
[40, 41] used in prior competitions, such as OpenSim. Furthermore, MyoSuite natively supports
comprehensive contact dynamics, enabling the simulation of complex, contact-rich environment
interactions. Within MuJoCo, the muscles are specifically modelled as actuators attached to tendons,
which are assumed to be infinitely stiff and without elasticity.

Musculoskeletal Models                   Each model segment used in the two tasks is presented in detail below:


                                                                      3
• MyoArm The right arm of the MyoArm model, comprising 27 degrees of freedom (DOFs) and 63
  muscle-tendon units, is adapted from the OpenSim MoBL arm model [42, 43]. This model has
  been utilized in prior MyoChallenges for manipulation tasks [35, 36, 32].
• MyoTorso The MyoTorso is created based on [44] in [26] with 210 actuators and 18 DoFs, and has
  been used in previous balancing research [45].
• MyoLeg MyoLeg model comprises 80 muscle-tendon and 28 DoFs units derived from the OpenSim
  lower limb model [46] and was previously featured in the MyoChallenges [36, 32].

Data Participation in the competition did not require pre-collected training datasets. The primary
challenge was to develop policies that learn directly through interaction and exploration within the
MyoSuite environments. However, to support alternative approaches like imitation learning and
behavior cloning, we provide a custom MyoChallenge bot (Appendix I) that allows participants to
generate and record their own training data. We also encouraged the use of public motion capture
datasets, such as AMASS [47]. Following the conclusion of the competition, further relevant datasets
have become available, e.g., the BONES-SEED dataset [48]. While optional, these datasets can serve
as strong motion priors for imitation learning or behavior cloning.

2.2     Tasks and Evaluations

2.2.1    Table Tennis Track
Task The table tennis track (Fig.1-A) features a single-arm and trunk task where the agent must hold
on to a table tennis paddle and return an incoming ball trajectory, while controlling the torso posture.
To simplify the task, the pelvis is given two position actuators in the horizontal x and y directions to
allow positioning around the table. The left arm is left unactuated and is fixed in a static position to
help with balance. The paddle is initiated close to the right palm in an ungrasped position. A key
source of complexity in this task is that a generalist policy that must swiftly handle the control across
incoming table tennis ball trajectories with various speeds. The environmental variations across
different phases and evaluations are detailed in Appendix C - Table 4 and the variations in Table 5.
Observation The controller receives a 416-dimensional observation vector, including MSk joint
positions and velocities, muscle stimulation levels, and the 6-DoF positions and velocities of the table
tennis ball and paddle. Additionally, contact status is indicated by six binary labels specifying which
object is the ball in contact with, if any (see Appendix C.1 - Table 6 for details).
Action The action space includes a 275-dimensional continuous vector ranging from [-1, 1]. This
includes the MyoArm, consisting of 63 muscles, the MyoTorso, consisting of 210 muscles and two
position actuators for pelvis translation in the x,y plane. The actions targeting muscles are then
renormalized to a [0, 1] range within the environment, to be interpreted as muscle excitation levels.
Termination A trial is successful if the paddle strikes the ball exactly once, sending it directly to
the opponent’s side without touching the agent’s half of the table, or missing the table entirely. The
termination condition can be found in full in Appendix C.1.
Evaluation Metric The participants were first ranked based on the number of successful returns of
table tennis. During phase 2, teams that scored within 10% of each other in the ’success rate’ metrics
were then re-ranked based on the second criterion, which is the muscle activation effort, with less
effort leading to a better ranking.
Baseline Controller We provided a benchmarking baseline policy that used a heuristic muscle
grouping dimensional reduction strategy presented in [45] and further trained with a deep neural
network with reinforcement learning. The baseline demonstrated a success rate of approximately 2%
under Phase 1 variation. Detailed hyperparameters can be found in Appendix C.1.

2.2.2    Soccer Track
Task The objective is to develop a controller for the fullbody MSk model that allows for coordinated
locomotion and kicking of a ball to score goals in a net with and without a goalkeeper, as shown in
Fig.1-B. To reduce the number of muscles, the model has no arms. A key source of complexity in
this task is coordinating 290 muscles to produce a single movement sequence that requires the legs
to generate locomotion, maintain postural stability, and deliver a precisely targeted ballistic strike.


                                                   4
Table 2: Phase 1 evaluation results over 100 trials for the Table Tennis and Soccer tracks. All methods
were trained for 10M steps using Stable-Baselines3 with default hyperparameters. The shaded row
denotes the provided Table Tennis baseline; no baseline was provided for the Soccer track.
(a) Table Tennis Track
Algorithm/Method            Holding paddle Maintain upright R-Arm Upright            Success rate Effort
PPO + muscle grouping +
                                  ✓                ✓                   ✓                 2%        0.79
CL (Baseline)
PPO + muscle grouping             ✓                ✓                   ×                 0%        0.20
PPO                               ✓                ✓                   ×                 0%        0.51
SAC + muscle grouping             ✓                ✓                   ×                 0%        0.67
SAC                               ×                ×                   ×                 0%        0.63
(b) Soccer Track (no baseline)
Algorithm/Method             Torso upright   Walking forward Kicking Soccer          Success rate Effort
PPO + muscle grouping             ×                ×                   ×                 0%        0.09
PPO                               ×                ×                   ×                 0%        0.17
SAC + muscle grouping             ×                ×                   ×                 0%        0.33
SAC                               ×                ×                   ×                 0%        0.32
These functions place competing demands on the same effectors. The environmental variations and
goalkeeper behaviour are detailed in Appendix C.2 - Table 7 and the variations in Table 8.
Observation The controller/policy has access to a 418-dimension proprioceptive vector that includes
information such as joint angles, velocities, muscle states, and goal conditions, including soccer,
keeper and net, updated at each time step (Appendix C.2 - Table 9).
Action The action space consists of 290 continuous muscle excitation controls ranging from [-1, 1].
Termination A simulation trial is deemed complete when the player (or agent) scores the ball such
that it is fully within the confines of the net within the maximum time constraints stated in Table 8.
Evaluation Metrics. The performance was first measured by the success rate of scoring goals.
During phase 2, teams that scored within 10% of each other in the ’success rate’ metrics were then
ranked based on the muscle activation effort, with less effort leading to a better ranking.
Baseline Controller We did not provide a baseline controller for the soccer task. However, baseline
controllers for the intact myoLeg model that produce walking are available in MyoSuite [30], such as
DEP-RL controller [20] and a reflex-based controller [49].


3     Benchmark and Competition Results

3.1   Performance of Standard RL Baselines

To assess whether existing off-the-shelf reinforcement learning methods are sufficient for the pro-
posed tasks, we evaluate PPO and SAC together with muscle-grouping and curriculum-learning
variants. All methods are trained for 10 million environment steps using the default Stable-Baselines3
hyperparameters and evaluated over 100 unseen Phase 1 trials. In addition to task success and effort,
we report intermediate behavioral competencies to identify where each method fails.
Table 2 shows that standard, off-the-shelf, model-free RL fails to solve either task within the evaluated
training budget. In Table Tennis, the PPO variants and SAC with muscle grouping learn basic paddle
retention and postural stability, but only the curriculum-learning baseline achieves correct arm
positioning and any successful returns, with a success rate of just 2%. In Soccer, none of the
tested methods acquires even the prerequisite behaviors of standing upright. These results expose the
exploration and coordination limitations of off-the-shelf methods in high-dimensional musculoskeletal
systems and motivate the development of new structured solutions through the competition.

3.2   Competition Results

This year’s MyoChallenge saw a total of 69 participating teams from over 10 countries. Over the four-
month submission period, we received a total of 562 submissions across two phases and recorded over


                                                   5
Table 3: Ranking results for the two tracks of MyoChallenge 2025. Effort is recomputed as mean
squared activation with a reward weight of 1; see Appendix C.
                       Table Tennis Track                          Soccer Track
Rank         Team                    Score (%) Effort Team                         Score (%) Effort
                                               Phase 1
1st Place ActingAI                          100 0.3277 Servette MyoClub                   100 0.9265
2nd Place CIAO Group                         96 0.7428 Ligament Legends                     0 0.2393
3rd Place Servette MyoClub                   94 0.8229 N/A                                N/A    N/A
                                               Phase 2
1st Place ActingAI                           64 0.1306 Servette MyoClub                    32 1.3174
2nd Place BioSyn                             60 0.1297 N/A                                N/A    N/A
3rd Place LNSGroup                           61 0.8473 N/A                                N/A    N/A

16k total downloads of MyoSuite. Among the teams that completed the post-competition survey, 63%
were composed entirely of students, including four teams of bachelor’s students. The DEI (Diversity,
Equity, and Inclusion) award was presented to Team KAIST_RISE from KAIST, Korea, which
featured women researchers in physiology and became the first team without a machine learning
background to achieve a score of 41% in Phase 1. The Student Award was given to MusclePower,
a team consisting of a single master’s student from Imperial College London, UK, which achieved
a score of up to 18% in Phase 2. However, no participants came from South America, Oceania, or
Africa, suggesting that further extension is needed within these underrepresented communities.
This year’s table tennis track attracted the highest number of competing teams since MyoChallenge
2022. In phase 1, more than 12 teams scored beyond baseline, with 7 of them scoring more than 90%;
in phase 2, 9 teams competed for the final winner. The winning team in the table tennis achieved
100% in phase 1 and a 64% success rate in phase 2 with an effort of 0.1306 (average muscle activation
units). The top three teams underwent a fierce competition of only a 5% difference in success rate in
the final scoring. Due to the complexity of the soccer task, only one team was able to surpass the
provided baselines during the period of competition (Table 3). To further advance development in
sports biomechanics, the competition suite will be retained within the MyoSuite repository.

3.3     Table Tennis Winning Solutions

3.3.1    First Place - Team ActingAI
Architecture Overview ActingAI propose Diff-Muscle, a hierarchical reinforcement learning
framework designed based on differential flatness to enable dimensionality reduction and efficient
control for complex musculoskeletal systems in the highly dynamic table tennis task. As illustrated
in Figure 2(a), the framework consists of a high-level Physics-based Planner, a low-level RL Policy,
and a Kinematics-based Muscle Actuation Controller (K-MAC). As illustrated in Figure 2(c), the
planner predicts the incoming ball’s trajectory and computes target racket states (position, velocity,
and orientation) as commands. The RL policy, optimized via Proximal Policy Optimization (PPO),
generates target joint positions based on these commands. These joint targets are then translated into
physiologic muscle activation signals through the K-MAC module.

Key Solution Insight ActingAI’s key insight is that musculoskeletal systems, despite their complex-
ity, exhibit conditional differential flatness [50, 51] with respect to joint configurations. Through
rigorous mathematical proof, the group demonstrates that all system states and control inputs can
be algebraically determined by a set of flat outputs (the joint angles z) and their finite derivatives.
As illustrated in Figure 2(b), this theoretical foundation allows ActingAI to transform the policy
exploration space from the high-dimensional muscle activation space (R273 for our MyoSuite model)
to a significantly lower-dimensional joint space (R32 ), effectively compressing the action space
by nearly an order of magnitude without loss of dynamical information. Their proposed K-MAC
establishes a principled bridge between joint-level planning and muscle-level execution through
kinematics priors, analytically mapping target joint configurations to physiological muscle activations.
This ensures that the learned policy explores a structurally valid manifold, bypassing the inefficient


                                                   6
search in the null space of redundant muscle forces. By utilizing kinematic priors, Diff-Muscle
achieves higher exploration efficiency and lower energy consumption compared to end-to-end RL or
learned synergy baselines.

         (a)                                                      Framework Overview
                                                                                RL Policy
                                                       Command
                                  Physics-based                                                                    Target Joint Position 𝑧 ∗
                                                                                          Actor
                                    Planner
                                                                                                           Value
                                                     Obs                                  Critic                           PPO
                              Ball
                             State
                                                                          Privilege obs
                                                                                                                 Kinematics-based Muscle
                                               Environment                                                         Actuation Controller
                                                                            Activations 𝑎𝑐𝑡


         (b) Kinematics-based Muscle Actuation Controller                                     (c)            Physics-based Planner
                                                                                                                             Desired Racket
                                                                                                   Initial Vel
                                                                                                                                               Predefined
                                                                                                                                                Hit Plane


                                   Forward                      PD
                                  Kinematics                 Controller

           Joint Position ∈ ℝ"#     Muscle Length ∈ ℝ#$"     Muscle Activations ∈ ℝ#$"



Figure 2: (a) Framework overview. The policy takes as input current observation and high-
level commands from the planner, and generates the target joint positions, which are subsequently
translated into muscle signals through the Kinematics-based Muscle Actuation Controller. (b)
Kinematics-based Muscle Actuation Controller. Through proving the differential flatness, Diff-
Muscle integrates forward kinematics and a PD controller to translate target joint positions into
muscle activations. (c) Physics-based Planner. Given the ball state, the planner predicts the desired
racket position, orientation, and velocity at the predefined plane as high-level commands.
3.3.2   Second Place - Team BioSyn
Architecture Overview Team BioSyn used a hybrid framework combining hierarchical planning
and structured reinforcement learning. In the table tennis task, trajectory generation and stroke
execution were guided by simplified models of ball flight and paddle-ball interaction [52]. The
structured reinforcement learning module explicitly modelled muscle synergies by assigning spe-
cialized subnetworks to different body regions, and leveraged synergetic exploration to improve
search efficiency in the redundant muscle space [53]. Furthermore, a weakness-aware curriculum
learning strategy was introduced to emphasize underperforming stroke patterns during the later phase
of training, leading to an overall performance gain.




Figure 3: BioSyn neural controller. The controller is structured according to the musculoskeletal
system, with synergy subnetworks dedicated to the hand, arm, torso, and pelvis.


Key Solution Insight - Structured Reinforcement Learning BioSyn was initially inspired by
evidence that different effectors are associated with distinct control regions in the human motor cortex.
Based on this insight, muscle control was decomposed across different body parts rather than learned
through a single monolithic controller. As illustrated in Fig. 3, the neural network was designed to


                                                                                7
reflect the structure of the musculoskeletal system, with synergistic subnetworks dedicated to the
hand, arm, torso, and pelvis. Furthermore, to improve learning efficiency in the high-dimensional
muscle action space, the weights of these synergy networks were incorporated into the exploration
process via multivariate Gaussian noise (see Appendix E for full equation). Further analysis in [53]
showed that BioSyn induces more correlated control patterns among functionally similar muscles,
thereby reducing antagonistic co-activation and improving muscular energy efficiency.

3.3.3     Third Place - Team LNSGroup
Architecture Overview To address the challenges of the complex table tennis task, the LNSGroup
team proposed a framework integrating physical priors, CrossQ [54], and a Gaussian Process Classifier
(GPC) [55] hybrid strategy. A data-calibrated physical model predicts the incoming ball’s trajectory
in real time, yielding explicit spatiotemporal targets that reshape dense reward signals. For low-level
actuation, the CrossQ algorithm ensures stable high-dimensional control. At the high level, a GPC
      (a)between specialized forehand and backhand policies based on incoming-ball features and
selects
estimated policy success probabilities.
      (a)




  (a)


        (b)
        (b)



  (b)




      Figure 4: Visualization of the agent executing (a) a forehand strike and (b) a backhand strike.
Key Solution Insights LNSGroup’s key insight was to reduce open-ended muscle control into
confidence-weighted stroke execution around physics-derived targets. A lightweight ball-flight model,
calibrated by trajectory sampling [52], predicted the hitting position, paddle orientation, velocity,
and strike time, turning sparse returns into dense geometric tracking rewards; rule-based pelvis
control stabilized the torso so RL could focus on upper-limb striking. The low-level controller used
CrossQ [54], an off-policy actor-critic method that removes target networks and instead evaluates
current and next state-action pairs in a shared batch. This design uses batch normalization effectively
under end to end training, improving sample efficiency and training robustness for high-dimensional
actions. To cover the broadened Phase-2 trajectory distribution, LNSGroup trained specialized
forehand and backhand policies and used a GPC [55] to estimate each policy’s success probability
from incoming-ball features, selecting the stroke with the highest confidence at runtime.

3.4     Soccer Penalty Winning Solution

3.4.1     First Place - Servette MyoClub
Architecture Overview Rather than training a controller from scratch, which would require jointly
solving locomotion, balance, and kicking, Servette MyoClub took a more principled approach by
building on an existing policy, KINESIS [56], that already produces human-like gait via imitation
learning, and that had been extended to support goal-directed movement. KINESIS was trained via
motion imitation on 1.8 hours of human locomotion data (KIT-Locomotion dataset [57]), outputting
muscle activations for a full-body model with up to 290 muscles. The architecture comprises
a Mixture of Experts (MoE) with 3 expert policies (deep MLPs with 6 hidden layers of sizes


                                                    8
[2048, 1536, 1024, 1024, 512, 512], SiLU activations) and a gating network for expert selection. Each
expert maps proprioceptive and target observations (pelvis state, joint kinematics, foot contacts, target
reference pose) to high-dimensional muscle activation signals. For the challenge solution, Expert 1,
the most extensively trained expert (10,000 epochs) which is specialized in forward locomotion [56],
was used as the foundation for the soccer adaptation pipeline described below.

    Motion imitation                Target reaching
                       Soccer ball kicking
       Offline trajectory collection

                       fine-tune                               fine-tune                                                               Student Policy          Final policy
       learning                         policy                                  policy                 (with success filtering)



                                     Teacher Policy: Kinesis                                              Base Policy Rollout
          Pre-training    On-policy behavior cloning

                                                                                                      with domain randomization                               + fine-tuning



                                   Figure 5: Overview of Servette MyoClub training pipeline.

Key Solution Insight The winning solution
decomposed the penalty kick task into two
stages (see Figure 5 for the full pipeline):

1. Teacher policy development. Starting from
   the KINESIS motion imitation policy (Ex-
   pert 1), a soccer ball-kicking policy was
   derived through two successive fine-tuning
   steps: first into a target-reaching policy, then
   into a kicking policy. For convenience, this
   stage operated entirely within the KINESIS
   observation space.
2. Retargeting to the MyoChallenge environ- Figure 6: Task visualization. Top: Ball-reaching
   ment. Because the KINESIS and MyoChal- performance at from-scratch initialization. Middle:
   lenge environments define different obser- Zero-shot ball-reaching performance by KINESIS.
   vation spaces, the ball-kicking policy from Bottom: Final ball kicking performance after on-
   stage 1 was transferred into a student policy policy behavior cloning.
   that operated on MyoChallenge observations
   through offline trajectory collection, student pre-training, on-policy behavior cloning [23], and
   reinforcement learning fine-tuning.

4    Discussion
Generalizable Design Principles Across both MyoChallenge 2025 tracks, no single RL algorithm,
action representation, or reward formulation provided a plug-and-play solution to high-dimensional
MSk control. Instead, three generalizable design principles emerged from the successful solutions.
First, task-specific structure was important for reducing exploration and credit-assignment difficulties.
To handle the highly dynamic nature of incoming table tennis balls, all winning solutions moved
beyond purely end-to-end learning and incorporated explicit physics-based modelling and task-
specific priors. Second, hierarchical decomposition helped make complex motor tasks more tractable.
ActingAI, BioSyn, and LNSGroup separated trajectory planning from muscle-level execution, while
LNSGroup further demonstrated the advantages of specialized forehand and backhand controllers
over a single universal policy. Similarly, Servette MyoClub progressively built upon foundational
locomotion skills [56] before acquiring task-specific kicking behaviors. These approaches share
structural similarities with biological motor learning, where foundational motor capabilities and high-
level movement strategies support the execution of complex motor skills. More broadly, the results
suggest that separating task-level planning from motor execution, or reusing previously acquired
skills, can reduce the difficulty of learning complex muscle-driven behaviors. Lastly, observation
and action representations influenced both learning efficiency and control expressiveness. ActingAI
demonstrated the importance of including muscle activation states in policy observations, while
BioSyn showed that removing planned striking targets substantially increased exploration difficulty.
To manage the high-dimensional muscle action space, ActingAI utilized state-space compression,
while BioSyn employed biologically inspired muscle-synergy subnetworks [58, 59, 60]. In contrast,
LNSGroup employed CrossQ-based reinforcement learning for muscle-level stroke control without
introducing an explicit learned low-dimensional muscle-synergy representation [54, 61], preserving


                                                                                                  9
control expressiveness but resulting in higher Effort scores (Table 3). In the Soccer track, Servette
MyoClub leveraged imitation learning [56] to start with a controller that already encodes a plausible
motion prior, and thus did not require any explicit constraining of the action space. A post-hoc
analysis of the functional dimensionality further showed that even synergies that explain only a
small amount of variance are important for successful control (Appendix G.5), which extends recent
modeling results from dexterous hand control [21, 23]. Overall, these insights suggest that informative
observations are essential, whereas action-space reduction introduces a trade-off between learning
efficiency and the expressiveness of muscle control, in part because it may discard low-variance
components that still matter for control.

Unsuccessful Strategies The winning teams also reported several unsuccessful approaches. For
example, LNSGroup found that successful approaches in previous challenges such as DynSyn [22],
as well as CrossQ [62] without sufficient task-specific guidance, could not directly solve the Table
Tennis task. Sparse rewards provided insufficient credit assignment, while dense tracking objectives
could produce contact without valid returns. Their attempts to train a universal forehand–backhand
controller also remained unreliable despite additional training and curriculum learning, emphasizing
the advantages of policy specialization. Similarly, Servette MyoClub found that direct PPO training
from scratch failed to establish stable locomotion, achieving a 0% scoring rate. Those unsuccessful
attempts showed that established principles such as muscle synergies, imitation learning, and reward
shaping remained useful, but required adaptation to the more dynamic tasks introduced in 2025.

Competition-Wide Analysis and Limitations Beyond the winning teams, the broader competition
results reveal the limitations of current musculoskeletal control methods. In Table Tennis Phase 1, the
11 teams scoring above baseline averaged 76.3±24.9 (median: 90), whereas the nine teams achieving
non-zero scores in Phase 2 averaged only 30.6 ± 26.6, with four scoring above 50. Several strong
Phase 1 teams deteriorated substantially under randomized incoming-ball conditions; for example,
CIAO’s score dropped from 96% to 1%. These results demonstrate that strong performance in
simplified task settings often fails to generalize to more complex and dynamic conditions. The Soccer
track was even more challenging, with only Servette MyoClub achieving a non-zero scoring rate.
Nevertheless, its resulting behavior shows a slow approach towards the ball and produces a small kick,
rather than demonstrating diverse athletic movements. This performance gap reflects the distinction
between optimizing a competition objective and reproducing the biomechanical characteristics of
human performance, including coordinated kinetic-chain sequencing and muscle–tendon stretch-
shortening dynamics [63, 64]. While the winning solutions establish the feasibility of muscle-driven
sports control, robust generalization and diverse, human-like motor behavior remain open challenges.

Computational Scalability and Future Directions Computational cost represents an additional
barrier to scalable musculoskeletal learning. Despite both achieving a 100% success rate in Phase
1, Servette MyoClub required approximately 14 days to train its Phase 1 Soccer policy, while the
Acting AI’s Table Tennis policy required 51 hours, both using the CPU-based MyoSuite environment.
As the community scales toward high-dimensional, full-body musculoskeletal control, this CPU
bottleneck becomes prohibitive. Recent GPU-accelerated frameworks [65, 66] offer opportunities to
increase simulation throughput and enable more extensive experimentation with algorithms, reward
formulations, and training curricula. Although these developments were not part of the official 2025
challenge, this paradigm shift paves the way for a fully GPU-accelerated and data-driven era in
biomechanical simulation and future editions of MyoChallenge.

5   Conclusion and Future Challenges
Digital twins of humans are essential tools for understanding neuromotor control, muscle recruitment
patterns, athletic performance, and rehabilitation strategies. In this paper, we present MyoChallenge
2025, a competition benchmarking the gap between human athletic abilities and current MSk simula-
tion capabilities. The winning solutions demonstrated diverse approaches, including physics-based
priors, muscle synergies, expert distillation, and behavior cloning. Despite these advances, scalable
full-body control remains limited by both computational and algorithmic challenges in this edition.
Future challenges will move toward GPU-based simulation to reduce computational bottlenecks,
while continuing to lower barriers to participation, especially for underrepresented groups, and
encourage the global community to advance neuromotor control and human–machine interaction.


                                                  10
Acknowledgments and Disclosure of Funding
We would like to acknowledge support for this competition from the University of Twente Techmed
and DSI, Google Cloud Computing, MyoLab, Delsys, Ocon - Orthopesische Kliniek, Ocon –
Sportmedische Kliniek, and EU ERC StG Interact. Special thanks goes to Dhruv Batra, Ram
Racmrakhya, Deshraj Yadav, and Rishabh Jain for help with the EvalAI platform. A.M.: Swiss
SNF grant (310030_212516) and Simons foundation (SFI-AN-NC-SCN-00007276-14). G.D. and
C.W.: NSERC Discovery Grant and NFRF: Exploration. B. K. H.: Imperial-Meta Wearable Neural
Interfaces Research Centre.
The authors declare no competing financial interests or relationships that could be perceived as
influencing the work presented in this paper.

References
 [1] Siqi Liu, Guy Lever, Zhe Wang, Josh Merel, S. M. Ali Eslami, Daniel Hennes, Wojciech M. Czarnecki,
     Yuval Tassa, Shayegan Omidshafiei, Abbas Abdolmaleki, Noah Y. Siegel, Leonard Hasenclever, Luke
     Marris, Saran Tunyasuvunakool, H. Francis Song, Markus Wulfmeier, Paul Muller, Tuomas Haarnoja,
     Brendan Tracey, Karl Tuyls, Thore Graepel, and Nicolas Heess. From motor control to team play in
     simulated humanoid football. Science Robotics, 7(69):eabo0235, 2022.

 [2] Yumeng Liu, Yaxun Yang, Youzhuo Wang, Xiaofei Wu, Jiamin Wang, Yichen Yao, Sören Schwertfeger,
     Sibei Yang, Wenping Wang, Jingyi Yu, et al. Realdex: Towards human-like grasping for robotic dexterous
     hand. arXiv preprint arXiv:2402.13853, 2024.

 [3] Boston Dynamics. Atlas. https://bostondynamics.com/atlas, 2023.

 [4] Tairan He, Jiawei Gao, Wenli Xiao, Yuanhang Zhang, Zi Wang, Jiashun Wang, Zhengyi Luo, Guanqi He,
     Nikhil Sobanbabu, Chaoyi Pan, Zeji Yi, Guannan Qu, Kris Kitani, Jessica Hodgins, Linxi "Jim" Fan, Yuke
     Zhu, Changliu Liu, and Guanya Shi. Asap: Aligning simulation and real-world physics for learning agile
     humanoid whole-body skills. arXiv preprint arXiv:2502.01143, 2025.

 [5] Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu,
     and Guanya Shi. Omnih2o: Universal and dexterous human-to-humanoid whole-body teleoperation and
     learning, 2024.

 [6] Ziwen Zhuang, Zipeng Fu, Jianren Wang, Christopher Atkeson, Soeren Schwertfeger, Chelsea Finn, and
     Hang Zhao. Robot parkour learning, 2023.

 [7] Hanxin Zhang, Abdulqader Dhafer, Zhou Daniel Hao, and Hongbiao Dong. A generative system for
     robot-to-human handovers: from intent inference to spatial configuration imagery, 2025.

 [8] Francisco J. Valero-Cuevas. Fundamentals of Neuromechanics. 2024.

 [9] Massimo Sartori, David G. Llyod, and Dario Farina. Neural data-driven musculoskeletal modeling for
     personalized neurorehabilitation technologies. IEEE transactions on bio-medical engineering, 63(5):879–
     893, 2016.

[10] Pavan Ramdya and Auke Jan Ijspeert. The neuromechanics of animal locomotion: From biology to robotics
     and back. Science Robotics, 8(78):eadg0279, 2023.

[11] Massimo Sartori. Advancing wearable robotics for shaping the human musculoskeletal system [young
     professionals]. IEEE Robotics & Automation Magazine, 30(3):164–165, 2023.

[12] Seungmoon Song, Łukasz Kidziński, Xue Bin Peng, Carmichael Ong, Jennifer Hicks, Sergey Levine,
     Christopher G Atkeson, and Scott L Delp. Deep reinforcement learning for modeling human locomotion
     control in neuromechanical simulation. Journal of neuroengineering and rehabilitation, 18(1):1–17, 2021.

[13] Takara Everest Truong, Michael Piseno, Zhaoming Xie, and Karen Liu. Pdp: Physics-based character
     animation via diffusion policy. In SIGGRAPH Asia 2024 Conference Papers, SA ’24, page 1–10. ACM,
     December 2024.

[14] C. Martin, B. Bideau, M. Ropars, P. Delamarche, and R. Kulpa. Upper limb joint kinetic analysis during
     tennis serve: Assessment of competitive level on efficiency and injury risks. Scandinavian Journal of
     Medicine & Science in Sports, 24(4):700–707, January 2013.


                                                    11
[15] James H. Buffi, Katie Werner, Tom Kepple, and Wendy M. Murray. Computing muscle, ligament,
     and osseous contributions to the elbow varus moment during baseball pitching. Annals of Biomedical
     Engineering, 43(2):404–415, October 2014.

[16] Caitlin E. Clancy, Anthony A. Gatti, Carmichael F. Ong, Monica R. Maly, and Scott L. Delp. Muscle-driven
     simulations and experimental data of cycling. Scientific Reports, 13(1), December 2023.

[17] Cedric E. Attias, Thomas K. Uchida, Keaton Inkol, and John McPhee. Musculoskeletal modelling and
     predictive simulation of baseball pitching to improve performance and mitigate injury using forward
     dynamics and optimal control. Multibody System Dynamics, January 2026.

[18] Aleksi Ikkala, Florian Fischer, Markus Klar, Miroslav Bachinski, Arthur Fleig, Andrew Howes, Perttu
     Hämäläinen, Jörg Müller, Roderick Murray-Smith, and Antti Oulasvirta. Breathing life into biomechanical
     user models. In Proceedings of the 35th Annual ACM Symposium on User Interface Software and
     Technology, pages 1–14, 2022.

[19] Jungnam Park, Sehee Min, Phil Sik Chang, Jaedong Lee, Moon Seok Park, and Jehee Lee. Generative
     gaitnet. In ACM SIGGRAPH 2022 Conference Proceedings, pages 1–9, 2022.

[20] Pierre Schumacher, Daniel F.B. Haeufle, Dieter Büchler, Syn Schmitt, and Georg Martius. Dep-rl: Embod-
     ied exploration for reinforcement learning in overactuated and musculoskeletal systems. In Proceedings of
     the Eleventh International Conference on Learning Representations (ICLR), May 2023.

[21] Alberto Silvio Chiappa, Pablo Tano, Nisheet Patel, Abigail Ingster, Alexandre Pouget, and Alexander
     Mathis. Acquiring musculoskeletal skills with curriculum-based reinforcement learning. bioRxiv, pages
     2024–01, 2024.

[22] Kaibo He, Chenhui Zuo, Chengtian Ma, and Yanan Sui. Dynsyn: dynamical synergistic representation for
     efficient learning and control in overactuated embodied systems. In Proceedings of the 41st International
     Conference on Machine Learning, ICML’24. JMLR.org, 2024.

[23] Alberto Silvio Chiappa, Boshi An, Merkourios Simos, Chengkun Li, and Alexander Mathis. Arnold: a
     generalist muscle transformer policy. arXiv preprint arXiv: 2508.18066, 2025.

[24] Alejandro F. Azocar, Luke M. Mooney, Jean-François Duval, Ann M. Simon, Levi J. Hargrove, and
     Elliott J. Rouse. Design and clinical implementation of an open-source bionic leg. Nature Biomedical
     Engineering, 4(10):941–953, October 2020.

[25] Kristin E. Yu, Briana N. Perry, Courtney W. Moran, Robert S. Armiger, Matthew S. Johannes, Abigail
     Hawkins, Lauren Stentz, Jamie Vandersea, Jack W. Tsao, and Paul F. Pasquina. Clinical evaluation of
     the revolutionizing prosthetics modular prosthetic limb system for upper extremity amputees. Scientific
     Reports, 11(1), January 2021.

[26] Rohan Walia, Morgane Billot, Kevin Garzon-Aguirre, Swathika Subramanian, Huiyi Wang, Mohamed Irfan
     Refai, and Guillaume Durandau. Myoback: A musculoskeletal model of the human back with integrated
     exoskeleton. In 2025 International Conference On Rehabilitation Robotics (ICORR), page 128–135. IEEE,
     May 2025.

[27] Scott L. Delp, Frank C. Anderson, Allison S. Arnold, Peter Loan, Ayman Habib, Chand T. John, Eran
     Guendelman, and Darryl G. Thelen. Opensim: Open-source software to create and analyze dynamic
     simulations of movement. IEEE Trans. Biomed. Eng., 54(11):1940–1950, 2007.

[28] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David
     Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel State. Isaac gym: High performance
     GPU based physics simulation for robot learning. In Thirty-fifth Conference on Neural Information
     Processing Systems Datasets and Benchmarks Track (Round 2), 2021.

[29] Thomas Geijtenbeek. The Hyfydy simulation software, 11 2021. https://hyfydy.com.

[30] Vittorio Caggiano, Huawei Wang, Guillaume Durandau, Massimo Sartori, and Vikash Kumar. Myosuite –
     a contact-rich simulation suite for musculoskeletal motor control, 2022.

[31] Łukasz Kidziński, Carmichael Ong, Sharada Prasanna Mohanty, Jennifer Hicks, Sean F. Carroll, Bo Zhou,
     Hongsheng Zeng, Fan Wang, Rongzhong Lian, Hao Tian, Wojciech Jaśkowski, Garrett Andersen, Odd Rune
     Lykkebø, Nihat Engin Toklu, Pranav Shyam, Rupesh Kumar Srivastava, Sergey Kolesnikov, Oleksii
     Hrinchuk, Anton Pechenko, Mattias Ljungström, Zhen Wang, Xu Hu, Zehong Hu, Minghui Qiu, Jun
     Huang, Aleksei Shpilman, Ivan Sosin, Oleg Svidchenko, Aleksandra Malysheva, Daniel Kudenko, Lance
     Rane, Aditya Bhatt, Zhengfei Wang, Penghui Qi, Zeyang Yu, Peng Peng, Quan Yuan, Wenxin Li, Yunsheng


                                                     12
     Tian, Ruihan Yang, Pingchuan Ma, Shauharda Khadka, Somdeb Majumdar, Zach Dwiel, Yinyin Liu,
     Evren Tumer, Jeremy Watson, Marcel Salathé, Sergey Levine, and Scott Delp. Artificial intelligence for
     prosthetics - challenge solutions, 2019.

[32] Cheryl Wang, Chun Kwang Tan, Balint K Hodossy, Shirui Lyu, Pierre Schumacher, James Heald, Kai
     Biegun, Samo Hromadka, Maneesh Sahani, Gunwoo Park, Beomsoo Shin, JongHyun Park, SEUNGBUM
     KOO, Chenhui Zuo, Chengtian Ma, Yanan Sui, Nicklas Hansen, Stone Tao, Yuan Gao, Hao Su, Seungmoon
     Song, Letizia Gionfrida, Massimo Sartori, Guillaume Durandau, Vikash Kumar, and Vittorio Caggiano.
     Myochallenge 2024: A new benchmark for physiological dexterity and agility in bionic humans. In The
     Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks
     Track, 2025.

[33] Łukasz Kidziński, Sharada P Mohanty, Carmichael F Ong, Jennifer L Hicks, Sean F Carroll, Sergey Levine,
     Marcel Salathé, and Scott L Delp. Learning to run challenge: Synthesizing physiologically accurate motion
     using deep reinforcement learning. In The NIPS’17 Competition: Building Intelligent Systems, pages
     101–120. Springer, 2018.

[34] Seungmoon Song, Łukasz Kidziński, Xue Bin Peng, Carmichael Ong, Jennifer Hicks, Sergey Levine,
     Christopher G. Atkeson, and Scott L. Delp. Deep reinforcement learning for modeling human locomotion
     control in neuromechanical simulation. Journal of neuroengineering and rehabilitation, August 2020.

[35] Vittorio Caggiano, Huawei Wang, Guillaume Durandau, Seungmoon Song, Yuval Tassa, Massimo Sartori,
     and Vikash Kumar. Myochallenge: Learning contact-rich manipulation using a musculoskeletal hand.
     https://sites.google.com/view/myochallenge, 2022.

[36] Vittorio Caggiano, Huawei Wang, Guillaume Durandau, Seungmoon Song, Tan Chun Kwang, Berg
     Cameron, Schumacher Pierre, Massimo Sartori, and Vikash Kumar. Myochallenge 2023: Towards
     human-level dexterity and agility. https://sites.google.com/view/myosuite/myochallenge/
     myochallenge-2023, 2023.

[37] Vittorio Caggiano, Guillaume Durandau, Huiyi Wang, Chun Kwang Tan, Pierre Schumacher, Huawei
     Wang, Alberto Silvio Chiappa, Alessandro Marin Vargas, Alexander Mathis, Jungdam Won, Jungnam Park,
     Gunwoo Park, Beomsoo Shin, Minseung Kim, Seungbum Koo, Zhuo Yang, Wei Dang, Heng Cai, Jianfei
     Song, and Seungmoon Song. Myochallenge 2023: Towards human-level dexterity and agility. In NeurIPS
     2024 Track Datasets and Benchmarks, 2024.

[38] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In
     2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 5026–5033. IEEE,
     2012.

[39] Huawei Wang, Vittorio Caggiano, Guillaume Durandau, Massimo Sartori, and Vikash Kumar. Myosim:
     Fast and physiologically realistic mujoco models for musculoskeletal and exoskeletal studies. In 2022
     International Conference on Robotics and Automation (ICRA), pages 8104–8111. IEEE, 2022.

[40] Aleksi Ikkala and Perttu Hämäläinen. Converting biomechanical models from opensim to mujoco.
     In Converging Clinical and Engineering Research on Neurorehabilitation IV: Proceedings of the 5th
     International Conference on Neurorehabilitation (ICNR2020), October 13–16, 2020, pages 277–281.
     Springer, 2022.

[41] Tom Erez, Yuval Tassa, and Emanuel Todorov. Simulation tools for model-based robotics: Comparison of
     bullet, havok, mujoco, ODE and physx. In IEEE International Conference on Robotics and Automation,
     ICRA 2015, pages 4397–4404. IEEE, 2015.

[42] Katherine R Saul, Xiao Hu, Craig M Goehler, Meghan E Vidt, Melissa Daly, Anca Velisar, and Wendy M
     Murray. Benchmarking of dynamic simulation predictions in two software platforms using an upper limb
     musculoskeletal model. Computer methods in biomechanics and biomedical engineering, 18(13):1445–
     1458, 2015.

[43] SimTK. Upper extremity dynamic model. https://simtk.org/projects/upexdyn.

[44] Miguel Christophy, Nur Adila Faruk Senan, Jeffrey C. Lotz, and Oliver M. O’Reilly. A musculoskeletal
     model for the lumbar spine. Biomechanics and Modeling in Mechanobiology, 11(1–2):19–34, February
     2011.

[45] Huiyi Wang, Jozsef Kovecses, and Guillaume Durandau. Reinforcement learning identifies age-related bal-
     ance strategy shifts. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 33:4078–4088,
     2025.


                                                     13
[46] Apoorva Rajagopal, Christopher L. Dembia, Matthew S. DeMers, Denny D. Delp, Jennifer L. Hicks,
     and Scott L. Delp. Full-body musculoskeletal model for muscle-driven simulation of human gait. IEEE
     Transactions on Biomedical Engineering, 63(10):2068–2079, 2016.
[47] Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard Pons-Moll, and Michael J. Black. AMASS:
     Archive of motion capture as surface shapes. In International Conference on Computer Vision, pages
     5442–5451, October 2019.
[48] Bones Studio. Bones-seed: Skeletal everyday embodiment dataset. https://huggingface.co/
     datasets/bones-studio/seed, 2026.
[49] Seungmoon Song and Hartmut Geyer. A neural circuitry that emphasizes spinal feedback generates diverse
     behaviours of human locomotion. The Journal of physiology, 593(16):3493–3511, 2015.
[50] Hebertt Sira-Ramirez and Sunil K Agrawal. Differentially flat systems. Crc Press, 2018.
[51] Wentao Zhao, Jun Guo, Kangyao Huang, Xin Liu, and Huaping Liu. Diff-muscle: Efficient learning for
     musculoskeletal robotic table tennis. arXiv preprint arXiv:2603.08617, 2026.
[52] Zhi Su, Bike Zhang, Nima Rahmanian, Yuman Gao, Qiayuan Liao, Caitlin Regan, Koushil Sreenath, and
     S Shankar Sastry. Hitter: A humanoid table tennis robot via hierarchical planning and learning. arXiv
     preprint arXiv:2508.21043, 2025.
[53] Siyuan Liu, Bo Jiang, Lijun Han, Shanlin Zhong, Ci Song, Huaping Liu, and Jiahao Chen. Biosyngrasp:
     Bio-inspired structured reinforcement learning with synergetic exploration and human demonstration for
     dexterous grasping of musculoskeletal robot. IEEE Transactions on Automation Science and Engineering,
     23:6102–6116, 2026.
[54] Aditya Bhatt, Daniel Palenicek, Boris Belousov, Max Argus, Artemij Amiranashvili, Thomas Brox, and
     Jan Peters. Crossq: Batch normalization in deep reinforcement learning for greater sample efficiency and
     simplicity. In The Twelfth International Conference on Learning Representations, 2024.
[55] Christopher KI Williams and Carl Edward Rasmussen. Gaussian processes for machine learning, volume 2.
     MIT press Cambridge, MA, 2006.
[56] Merkourios Simos, Alberto Silvio Chiappa, and Alexander Mathis. Kinesis: Motion imitation for human
     musculoskeletal locomotion. In 2026 IEEE international conference on robotics and automation (ICRA).
     IEEE, 2026.
[57] Christian Mandery, Ömer Terlemez, Martin Do, Nikolaus Vahrenkamp, and Tamim Asfour. The kit
     whole-body human motion database. In 2015 International Conference on Advanced Robotics (ICAR),
     pages 329–336. IEEE, 2015.
[58] Emilio Bizzi and Vincent C. K. Cheung. The neural origin of muscle synergies. Frontiers in Computational
     Neuroscience, 7, 2013.
[59] Anderson Nascimento Guimarães, Herbert Ugrinowitsch, Juliana Bayeux Dascal, Alessandra Beggiato
     Porto, and Victor Hugo Alves Okazaki. Freezing degrees of freedom during motor learning: A systematic
     review. Motor Control, 24(3):457–471, July 2020.
[60] Alberto Silvio Chiappa, Alessandro Marin Vargas, Ann Zixiang Huang, and Alexander Mathis. Latent
     exploration for reinforcement learning. Advances in Neural Information Processing Systems, 2023.
[61] Yunyue Wei, Chenhui Zuo, and Yanan Sui. Scalable exploration for high-dimensional continuous control
     via value-guided flow. In The Fourteenth International Conference on Learning Representations, 2026.
[62] Aditya Bhatt, Daniel Palenicek, Boris Belousov, Max Argus, Artemij Amiranashvili, Thomas Brox, and
     Jan Peters. Crossq: Batch normalization in deep reinforcement learning for greater sample efficiency and
     simplicity, 2019.
[63] V. Jelusic, Slobodan Jaric, and M. Kukolj. Effects of the stretch-shortening strength training on kicking
     performance in soccer players. J Hum Mov Stud, 22:231–238, 01 1992.
[64] A. Lees, T. Asai, T. B. Andersen, H. Nunome, and T. Sterzing. The biomechanics of kicking in soccer: A
     review. Journal of Sports Sciences, 28(8):805–817, June 2010.
[65] Chengkun Li, Cheryl Wang, Bianca Ziliotto, Merkourios Simos, Jozsef Kovecses, Guillaume Durandau,
     and Alexander Mathis. Towards embodied ai with musclemimic: Unlocking full-body musculoskeletal
     motor learning at scale. arXiv preprint arXiv:2603.25544, 2026.


                                                     14
[66] Yunyue Wei, Chenhui Zuo, Shanning Zhuang, Haixin Gong, Yaming Liu, and Yanan Sui. Scaling
     whole-body human musculoskeletal behavior emulation for specificity and diversity. arXiv preprint
     arXiv:2603.29332, 2026.

[67] Deshraj Yadav, Rishabh Jain, Harsh Agrawal, Prithvijit Chattopadhyay, Taranjeet Singh, Akash Jain,
     Shiv Baran Singh, Stefan Lee, and Dhruv Batra. Evalai: Towards better evaluation systems for ai agents.
     arXiv, arXiv:1902.03570, 2019.

[68] Jungdam Won, Deepak Gopinath, and Jessica Hodgins. Physics-based character controllers using condi-
     tional vaes. ACM Trans. Graph., 41(4), July 2022.

[69] Stéphane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured
     prediction to no-regret online learning. In Proceedings of the fourteenth international conference on
     artificial intelligence and statistics, pages 627–635. JMLR Workshop and Conference Proceedings, 2011.

[70] Nikolai A. Bernstein. The co-ordination and regulation of movements, volume 1. Oxford, New York,
     Pergamon Press, 1967.

[71] Gerald E Loeb. Learning to use muscles. Journal of human kinetics, 76:9, 2021.
[72] Matthew C Tresch and Anthony Jarc. The case for and against muscle synergies. Current opinion in
     neurobiology, 19(6):601–607, 2009.

[73] Vittorio Caggiano, Vittorio La Barbera, Andrea Prestia, Ouassim Aouattah, Pierre Schumacher, Varun
     Joshi, and Vikash Kumar. Myoskeleton: A universal human skeletal model. White paper, MyoLab Inc.,
     2024. Available at: https://github.com/myolab/myo_model.




                                                    15
NeurIPS Paper Checklist
    1. Claims
      Question: Do the main claims made in the abstract and introduction accurately reflect the
      paper’s contributions and scope?
      Answer: [Yes]
      Justification: The abstract and introduction rigorously align with the paper’s contributions:
      (1) a novel competition framework for benchmarking sports intelligence in MSk model, (2)
      detailed methodological analysis of competition results, and (3) quantitative improvements
      over prior iterations (e.g., task complexity, participant performance). (4) New state-of-the-art
      methods developed by the winning teams.
      Guidelines:
         • The answer [N/A] means that the abstract and introduction do not include the claims
           made in the paper.
         • The abstract and/or introduction should clearly state the claims made, including the
           contributions made in the paper and important assumptions and limitations. A [No] or
           [N/A] answer to this question will not be perceived well by the reviewers.
         • The claims made should match theoretical and experimental results, and reflect how
           much the results can be expected to generalize to other settings.
         • It is fine to include aspirational goals as motivation as long as it is clear that these goals
           are not attained by the paper.
    2. Limitations
      Question: Does the paper discuss the limitations of the work performed by the authors?
      Answer: [Yes]
      Justification: In Section 4, we analyze (1) the methodological limitations of each team’s
      approach and (2) the relationship between each team’s methodological approach and their
      difference from true sports intelligence (3) the gaps between the current CPU-enabled
      environment and potential transition to GPU. We identify key challenges and propose
      actionable steps to bridge these gaps in future work.
      Guidelines:
         • The answer [N/A] means that the paper has no limitation while the answer [No] means
           that the paper has limitations, but those are not discussed in the paper.
         • The authors are encouraged to create a separate “Limitations” section in their paper.
         • The paper should point out any strong assumptions and how robust the results are to
           violations of these assumptions (e.g., independence assumptions, noiseless settings,
           model well-specification, asymptotic approximations only holding locally). The authors
           should reflect on how these assumptions might be violated in practice and what the
           implications would be.
         • The authors should reflect on the scope of the claims made, e.g., if the approach was
           only tested on a few datasets or with a few runs. In general, empirical results often
           depend on implicit assumptions, which should be articulated.
         • The authors should reflect on the factors that influence the performance of the approach.
           For example, a facial recognition algorithm may perform poorly when image resolution
           is low or images are taken in low lighting. Or a speech-to-text system might not be
           used reliably to provide closed captions for online lectures because it fails to handle
           technical jargon.
         • The authors should discuss the computational efficiency of the proposed algorithms
           and how they scale with dataset size.
         • If applicable, the authors should discuss possible limitations of their approach to
           address problems of privacy and fairness.
         • While the authors might fear that complete honesty about limitations might be used by
           reviewers as grounds for rejection, a worse outcome might be that reviewers discover
           limitations that aren’t acknowledged in the paper. The authors should use their best


                                                 16
       judgment and recognize that individual actions in favor of transparency play an impor-
       tant role in developing norms that preserve the integrity of the community. Reviewers
       will be specifically instructed to not penalize honesty concerning limitations.
3. Theory assumptions and proofs
  Question: For each theoretical result, does the paper provide the full set of assumptions and
  a complete (and correct) proof?
  Answer: [N/A].
  Justification: This paper does not include theoretical results.
  Guidelines:
     • The answer [N/A] means that the paper does not include theoretical results.
     • All the theorems, formulas, and proofs in the paper should be numbered and cross-
       referenced.
     • All assumptions should be clearly stated or referenced in the statement of any theorems.
     • The proofs can either appear in the main paper or the supplemental material, but if
       they appear in the supplemental material, the authors are encouraged to provide a short
       proof sketch to provide intuition.
     • Inversely, any informal proof provided in the core of the paper should be complemented
       by formal proofs provided in appendix or supplemental material.
     • Theorems and Lemmas that the proof relies upon should be properly referenced.
4. Experimental result reproducibility
  Question: Does the paper fully disclose all the information needed to reproduce the main ex-
  perimental results of the paper to the extent that it affects the main claims and/or conclusions
  of the paper (regardless of whether the code and data are provided or not)?
  Answer: [Yes]
  Justification: Yes, we have included the methodology, performance, and setup of the baseline
  and each team’s solutions in section 3, Appendix C.1, D, E, F and G.
  Guidelines:
     • The answer [N/A] means that the paper does not include experiments.
     • If the paper includes experiments, a [No] answer to this question will not be perceived
       well by the reviewers: Making the paper reproducible is important, regardless of
       whether the code and data are provided or not.
     • If the contribution is a dataset and/or model, the authors should describe the steps taken
       to make their results reproducible or verifiable.
     • Depending on the contribution, reproducibility can be accomplished in various ways.
       For example, if the contribution is a novel architecture, describing the architecture fully
       might suffice, or if the contribution is a specific model and empirical evaluation, it may
       be necessary to either make it possible for others to replicate the model with the same
       dataset, or provide access to the model. In general. releasing code and data is often
       one good way to accomplish this, but reproducibility can also be provided via detailed
       instructions for how to replicate the results, access to a hosted model (e.g., in the case
       of a large language model), releasing of a model checkpoint, or other means that are
       appropriate to the research performed.
     • While NeurIPS does not require releasing code, the conference does require all submis-
       sions to provide some reasonable avenue for reproducibility, which may depend on the
       nature of the contribution. For example
       (a) If the contribution is primarily a new algorithm, the paper should make it clear how
            to reproduce that algorithm.
       (b) If the contribution is primarily a new model architecture, the paper should describe
            the architecture clearly and fully.
       (c) If the contribution is a new model (e.g., a large language model), then there should
            either be a way to access this model for reproducing the results or a way to reproduce
            the model (e.g., with an open-source dataset or instructions for how to construct
            the dataset).


                                           17
        (d) We recognize that reproducibility may be tricky in some cases, in which case
             authors are welcome to describe the particular way they provide for reproducibility.
             In the case of closed-source models, it may be that access to the model is limited in
             some way (e.g., to registered users), but it should be possible for other researchers
             to have some path to reproducing or verifying the results.
5. Open access to data and code
   Question: Does the paper provide open access to the data and code, with sufficient instruc-
   tions to faithfully reproduce the main experimental results, as described in supplemental
   material?
   Answer: [Yes]
   Justification: Yes, we have included the URL for code, instructions, baseline in the abstract,
   section C.1 and Appendix H. The solutions of the participants are provided base in their
   own section’s Appendix D, E, F and G.
   Guidelines:
      • The answer [N/A] means that paper does not include experiments requiring code.
      • Please see the NeurIPS code and data submission guidelines (https://neurips.cc/
         public/guides/CodeSubmissionPolicy) for more details.
      • While we encourage the release of code and data, we understand that this might not
         be possible, so [No] is an acceptable answer. Papers cannot be rejected simply for not
         including code, unless this is central to the contribution (e.g., for a new open-source
         benchmark).
      • The instructions should contain the exact command and environment needed to run to
         reproduce the results. See the NeurIPS code and data submission guidelines (https:
         //neurips.cc/public/guides/CodeSubmissionPolicy) for more details.
      • The authors should provide instructions on data access and preparation, including how
         to access the raw data, preprocessed data, intermediate data, and generated data, etc.
      • The authors should provide scripts to reproduce all experimental results for the new
         proposed method and baselines. If only a subset of experiments are reproducible, they
         should state which ones are omitted from the script and why.
      • At submission time, to preserve anonymity, the authors should release anonymized
         versions (if applicable).
      • Providing as much information as possible in supplemental material (appended to the
         paper) is recommended, but including URLs to data and code is permitted.
6. Experimental setting/details
   Question: Does the paper specify all the training and test details (e.g., data splits, hyperpa-
   rameters, how they were chosen, type of optimizer) necessary to understand the results?
   Answer: [Yes]
   Justification: We provide the necessary training setup and details in Appendix C and Section
   2, as well as the individual’s team set up in Appendix D, E, F and G.
   Guidelines:
      • The answer [N/A] means that the paper does not include experiments.
      • The experimental setting should be presented in the core of the paper to a level of detail
         that is necessary to appreciate the results and make sense of them.
      • The full details can be provided either with the code, in appendix, or as supplemental
         material.
7. Experiment statistical significance
   Question: Does the paper report error bars suitably and correctly defined or other appropriate
   information about the statistical significance of the experiments?
   Answer: [Yes]
   Justification: While this challenge doesn’t report the statistical significance due to limited
   sample size, we use success rate and effort as the metric as detailed in Section 3.
   Guidelines:


                                            18
       • The answer [N/A] means that the paper does not include experiments.
       • The authors should answer [Yes] if the results are accompanied by error bars, confidence
          intervals, or statistical significance tests, at least for the experiments that support the
          main claims of the paper.
       • The factors of variability that the error bars are capturing should be clearly stated (for
          example, train/test split, initialization, random drawing of some parameter, or overall
          run with given experimental conditions).
       • The method for calculating the error bars should be explained (closed form formula,
          call to a library function, bootstrap, etc.)
       • The assumptions made should be given (e.g., Normally distributed errors).
       • It should be clear whether the error bar is the standard deviation or the standard error
          of the mean.
       • It is OK to report 1-sigma error bars, but one should state it. The authors should
          preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis
          of Normality of errors is not verified.
       • For asymmetric distributions, the authors should be careful not to show in tables or
          figures symmetric error bars that would yield results that are out of range (e.g., negative
          error rates).
       • If error bars are reported in tables or plots, the authors should explain in the text how
          they were calculated and reference the corresponding figures or tables in the text.
 8. Experiments compute resources
    Question: For each experiment, does the paper provide sufficient information on the com-
    puter resources (type of compute workers, memory, time of execution) needed to reproduce
    the experiments?
    Answer: [Yes]
    Justification: The compute resources of the baseline and solutions are outlined within
    Appendix C.1, D, E, F and G.
    Guidelines:
       • The answer [N/A] means that the paper does not include experiments.
       • The paper should indicate the type of compute workers CPU or GPU, internal cluster,
          or cloud provider, including relevant memory and storage.
       • The paper should provide the amount of compute required for each of the individual
          experimental runs as well as estimate the total compute.
       • The paper should disclose whether the full research project required more compute
          than the experiments reported in the paper (e.g., preliminary or failed experiments that
          didn’t make it into the paper).
 9. Code of ethics
    Question: Does the research conducted in the paper conform, in every respect, with the
    NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?
    Answer: [Yes]
    Justification: The author confirmed that the paper follows the NeurIPS Code of Ethics.
    Guidelines:
       • The answer [N/A] means that the authors have not reviewed the NeurIPS Code of
          Ethics.
       • If the authors answer [No], they should explain the special circumstances that require a
          deviation from the Code of Ethics.
       • The authors should make sure to preserve anonymity (e.g., if there is a special consid-
          eration due to laws or regulations in their jurisdiction).
10. Broader impacts
    Question: Does the paper discuss both potential positive societal impacts and negative
    societal impacts of the work performed?
    Answer: [Yes]


                                              19
    Justification: Yes, our paper discusses how the benchmarking environment that we have
    provided can positively impact the community with neuroscience, biomechanics, and sports
    rehabilitation within the introduction and conclusion. We also discuss the gap between our
    current framework and solutions with true sports athletes.
    Guidelines:
       • The answer [N/A] means that there is no societal impact of the work performed.
       • If the authors answer [N/A] or [No], they should explain why their work has no societal
         impact or why the paper does not address societal impact.
       • Examples of negative societal impacts include potential malicious or unintended uses
         (e.g., disinformation, generating fake profiles, surveillance), fairness considerations
         (e.g., deployment of technologies that could make decisions that unfairly impact specific
         groups), privacy considerations, and security considerations.
       • The conference expects that many papers will be foundational research and not tied
         to particular applications, let alone deployments. However, if there is a direct path to
         any negative applications, the authors should point it out. For example, it is legitimate
         to point out that an improvement in the quality of generative models could be used to
         generate Deepfakes for disinformation. On the other hand, it is not needed to point out
         that a generic algorithm for optimizing neural networks could enable people to train
         models that generate Deepfakes faster.
       • The authors should consider possible harms that could arise when the technology is
         being used as intended and functioning correctly, harms that could arise when the
         technology is being used as intended but gives incorrect results, and harms following
         from (intentional or unintentional) misuse of the technology.
       • If there are negative societal impacts, the authors could also discuss possible mitigation
         strategies (e.g., gated release of models, providing defenses in addition to attacks,
         mechanisms for monitoring misuse, mechanisms to monitor how a system learns from
         feedback over time, improving the efficiency and accessibility of ML).
11. Safeguards
    Question: Does the paper describe safeguards that have been put in place for responsible
    release of data or models that have a high risk for misuse (e.g., pre-trained language models,
    image generators, or scraped datasets)?
    Answer: [N/A]
    Justification: The paper poses no risk of data misuse.
    Guidelines:
       • The answer [N/A] means that the paper poses no such risks.
       • Released models that have a high risk for misuse or dual-use should be released with
         necessary safeguards to allow for controlled use of the model, for example by requiring
         that users adhere to usage guidelines or restrictions to access the model or implementing
         safety filters.
       • Datasets that have been scraped from the Internet could pose safety risks. The authors
         should describe how they avoided releasing unsafe images.
       • We recognize that providing effective safeguards is challenging, and many papers do
         not require this, but we encourage authors to take this into account and make a best
         faith effort.
12. Licenses for existing assets
    Question: Are the creators or original owners of assets (e.g., code, data, models), used in
    the paper, properly credited and are the license and terms of use explicitly mentioned and
    properly respected?
    Answer: [Yes]
    Justification: The MyoSuite is cited as the simulator embedded within MuJoCo with a URL.
    The participants’ solutions are cited and referenced accordingly. The license is available on
    the MyoSuite GitHub repository. Only publicly available data are used.
    Guidelines:


                                             20
       • The answer [N/A] means that the paper does not use existing assets.
       • The authors should cite the original paper that produced the code package or dataset.
       • The authors should state which version of the asset is used and, if possible, include a
          URL.
       • The name of the license (e.g., CC-BY 4.0) should be included for each asset.
       • For scraped data from a particular source (e.g., website), the copyright and terms of
          service of that source should be provided.
       • If assets are released, the license, copyright information, and terms of use in the
          package should be provided. For popular datasets, paperswithcode.com/datasets
          has curated licenses for some datasets. Their licensing guide can help determine the
          license of a dataset.
       • For existing datasets that are re-packaged, both the original license and the license of
          the derived asset (if it has changed) should be provided.
       • If this information is not available online, the authors are encouraged to reach out to
          the asset’s creators.
13. New assets
    Question: Are new assets introduced in the paper well documented and is the documentation
    provided alongside the assets?
    Answer: [Yes]
    Justification: All assets are available from the MyoSuite GitHub repository including license,
    model and code.
    Guidelines:
       • The answer [N/A] means that the paper does not release new assets.
       • Researchers should communicate the details of the dataset/code/model as part of their
          submissions via structured templates. This includes details about training, license,
          limitations, etc.
       • The paper should discuss whether and how consent was obtained from people whose
          asset is used.
       • At submission time, remember to anonymize your assets (if applicable). You can either
          create an anonymized URL or include an anonymized zip file.
14. Crowdsourcing and research with human subjects
    Question: For crowdsourcing experiments and research with human subjects, does the paper
    include the full text of instructions given to participants and screenshots, if applicable, as
    well as details about compensation (if any)?
    Answer: [N/A]
    Justification: No human subjects were involved.
    Guidelines:
       • The answer [N/A] means that the paper does not involve crowdsourcing nor research
          with human subjects.
       • Including this information in the supplemental material is fine, but if the main contribu-
          tion of the paper involves human subjects, then as much detail as possible should be
          included in the main paper.
       • According to the NeurIPS Code of Ethics, workers involved in data collection, curation,
          or other labor should be paid at least the minimum wage in the country of the data
          collector.
15. Institutional review board (IRB) approvals or equivalent for research with human
    subjects
    Question: Does the paper describe potential risks incurred by study participants, whether
    such risks were disclosed to the subjects, and whether Institutional Review Board (IRB)
    approvals (or an equivalent approval/review based on the requirements of your country or
    institution) were obtained?
    Answer: [N/A]


                                             21
    Justification: No human subjects were involved.
    Guidelines:
       • The answer [N/A] means that the paper does not involve crowdsourcing nor research
          with human subjects.
       • Depending on the country in which research is conducted, IRB approval (or equivalent)
          may be required for any human subjects research. If you obtained IRB approval, you
          should clearly state this in the paper.
       • We recognize that the procedures for this may vary significantly between institutions
          and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the
          guidelines for their institution.
       • For initial submissions, do not include any information that would break anonymity (if
          applicable), such as the institution conducting the review.
16. Declaration of LLM usage
    Question: Does the paper describe the usage of LLMs if it is an important, original, or
    non-standard component of the core methods in this research? Note that if the LLM is used
    only for writing, editing, or formatting purposes and does not impact the core methodology,
    scientific rigor, or originality of the research, declaration is not required.
    Answer: [N/A]
    Justification: The core method development in this research does not involve LLMs as any
    important, original, or non-standard components.
    Guidelines:
       • The answer [N/A] means that the core method development in this research does not
          involve LLMs as any important, original, or non-standard components.
       • Please refer to our LLM policy in the NeurIPS handbook for what should or should not
          be described.




                                           22
A     Competition Details

The competition ran from July 21st to November 8th on EvalAI https://eval.ai/web/
challenges/challenge-page/2628/overview, with a final workshop in the NeurIPS 2025
conference competition: MyoSymposium (https://sites.google.com/view/myosuite/
myochallenge/myochallenge-2025). The workshop allowed winners from both tracks to present
their solutions and bring together researchers and scholars in the field of biomechanics, ML, neuro-
science, and sports science.
All environments and task configurations can be cloned from the MyoChallenge25 GitHub tem-
plate (https://github.com/MyoHub/myochallenge_2025eval). The challenge was hosted on
EvalAI (https://eval.ai), where the policies uploaded by participants underwent automated
evaluation for a public scoreboard. Final scores reflect the average performance across 100 unseen
trials to ensure robustness against multiple seeds and unseen environmental variations.


B     EvalAI Computation Resources

The MyoChallenge utilizes EvalAI ([67]) for its evaluation platform and deployment support. Its
computational infrastructure is powered by Amazon Web Services (AWS), as detailed in the following
list:

       • AWS EC2 - c5.4xlarge (16 CPU, 32 GB RAM)
       • AWS EBS - gp2 (17 GB)
       • AWS ECS for Kubernetes
       • AWS ECR


C     Environment Details

In the evaluation on EvalAI, a hidden set of parameters is used to ensure fairness across submissions.
All efforts from the EvalAI platform are recomputed using the following formula:

                                                      n a
                                                   1 X
                                        Effort =          a2
                                                   na i=1 i

C.1   Table Tennis Track

Table Tennis Baseline The table tennis baseline uses a 12 CPU with one 5090 RTX GeForce. The
baseline model implements PPO using the stable_baselines3 library. The policy network follows an
ActorCriticPolicy architecture with an MLP comprising three hidden layers of sizes [1024, 512, 512],
respectively, employing the SiLU activation function. The agent was trained for a total of 10 million
timesteps, collecting 2,048 steps per rollout across six parallel environments, followed by ten update
epochs with a batch size of 64. Key algorithmic parameters include a discount factor (γ) of 0.99,
a GAE lambda of 0.95, an entropy coefficient of 0.001 to encourage exploration, a value function
coefficient of 0.5, and a maximum gradient norm of 0.5 for gradient clipping. Both the learning rate
and the PPO clipping range follow a linear decay schedule, annealing from initial values of 1.0 and
0.2, respectively, to zero over the course of training.

Termination Condition An episode terminates when any of the following conditions are met: (1)
the maximum episode duration is exceeded; (2) the ball’s vertical position drops below a critical
height threshold (z < 0.3,m); (3) the task is successfully solved; or (4) the ball exhibits an invalid
contact trajectory. An invalid trajectory is strictly defined as a Double Touch (contacting the paddle
multiple times), an Invalid Bounce (bouncing twice or rolling on the agent’s table side), a Missed
Strike (landing on the opponent’s side without paddle contact), or an Incomplete Play (failing to land
on the opponent’s side after a valid strike).


                                                 23
                      Table 4: Unvaried Object properties for the Table Tennis.
                     Object                           Properties
                     Table Tennis Task
                       Table Top (Total)              2.74 × 1.52 × 1.59 m3
                       Table Top (Each Side)          1.37 × 1.52 × 1.59 m3
                       Net                            0.01 × 1.825 × 0.305 m3
                       Paddle Handle                  Radius: 1.6 cm, Height: 5.1 cm
                       Paddle Face                    Radius: 9.3 cm, Height: 2 cm
                       Ball Radius                    2 cm
                       Ball Mass                      2.7 g
                       Ball Inertia                   7.2 × 10−7 kg·m2


Table 5: Changing Object properties across phases for table tennis tasks. During the first phase, all
initial starting criteria are kept constant except for a slight change in ball starting position. During the
second phase, we feed in variations in terms of mass, friction for the ball and the paddle. In addition,
now the incoming trajectory could span towards the entire side of the model’s table at various speeds.
It is not guaranteed that the model can always return the table tennis successfully.
              Property               Phase 1               Phase 2               Evaluation
           Paddle Mass               150 g                 100–150 g                  90–200 g
           Ball Friction
             Sliding                  1.0                  [0.9, 1.1]                 [0.9, 1.1]
             Torsional               0.005              [0.004, 0.006]             [0.004, 0.006]
             Rolling                0.0001           [0.00001, 0.00003]         [0.00001, 0.00003]
           Ball Start Pos.
             x                 [−1.25, −1.20]          [−1.25, −0.50]               [−1.25, −0.40]
             y                 [−0.50, −0.45]           [−0.50, 0.50]                [−0.50, 0.50]
             z                   [1.40, 1.50]            [1.40, 1.50]                 [1.30, 1.55]
           Ball Velocity
             vx                       5.6
             vy                       1.6                                 Varies*
             vz                       0.1
                                    * Guaranteed to land on the agent’s side.




C.2   Soccer Track

Goal Keeper Behavior A simple goal keeper, created with Mujoco native shapes, acts as a goal
keeper to increase the challenge of the task for trained policies. There are 3 different goal keeper
behaviors, where the environment randomly selects during evaluation. They are:

      1. Random static location along the goal line: Goal keeper appears at a random location
         along the goal line at the start of each episode, and remains stationary for the entire episode
      2. Random movement along the goal line: Goal keeper moves randomly along the goal line
         throughout the episode, at a randomized velocity
      3. Ball tracking behavior along the goal line: Goal keeper tracks the position of the ball, but
         does not leave the goal line

Goal keeper behaviors are parameterized by the velocity they are moving along the goal line. Goal
keeper velocity is randomized between 1m/s to 5m/s at the start of each episode.




                                                      24
                                 Table 6: Observation Space for Table Tennis Task
                 Description                                      Component                         Count
                 Pelvis Position                                  pelvis_pos                           3
                 Joint Positions                                  body_qpos                           58
                 Joint Velocities                                 body_vel                             58
                 Ball Position                                    ball_pos                              3
                 Ball Velocity                                    ball_vel                              3
                 Paddle Position*                                 paddle_pos                           3
                 Paddle Velocity                                  paddle_vel                           3
                 Paddle Orientation                               paddle_ori                           3
                 Paddle Reaching Error (see below)                reach_err                            3
                 Muscle Activations                               muscle_activations                  273
                 Touching Information **                          touching_info                         6
                     * This measures the spatial distance between the paddle and the table tennis object.
    ** This consists of six boolean indicators representing the ping-pong ball’s contact status with various objects in the

environment: Paddle (contact with the paddle), Own (the agent’s table side), Opponent (the opponent table side), Ground,
                                    Net, and Env (any other part of the environment).




                          Table 7: Unvaried Object properties for the Soccer tasks.
                                 Object               Properties
                                 Soccer Task
                                   Soccer Net         Width: 7.32 m, Height: 2.50 m
                                   Ball Radius        0.117 m
                                   Ball Mass          450 g




         Table 8: Comparison of starting criteria across challenge phases for the soccer task.
         Property             Phase 1              Phase 2                 Evaluation
          Ball Start Pos.                                                Fixed
          Agent Start Pos.
            x                            39.0               [38.0, 39.0]                      [36.5, 39.0]
            y                             0.0                 [±1.0]                            [±2.5]
          Agent Orientation                             Facing goal, in front of the ball
                             *
          Position Noise                  0.0                     1.0                              2.5
          Joint Noise**                   0.0                     0.02                            0.03
                                                     60% S, 30% R, 10% T                10% S, 45% R, 45% T
          Goalkeeper†                  100% S
                                                          v ∈ [1, 5]                       v ∈ [3.5, 5.5]
          Max Time                        20 s                    10 s                             10 s
                                         * Shifts base x by [−v, 0] and y by [−v, v].
                                   ** Adds uniform noise ∈ [−µ, µ] to initial joint angles.
                                     † S: Stationary, R: Random, T: Tracking soccer ball.




                                                             25
                    Table 9: Observation space components for the soccer task.
                Description                           Component              Count
                Ball Position                                           ball_pos                       3
                4 Position Coords (bounding goal area)                  goal_bounds                    12
                Muscle Activations                                      act                           290
                Joint Angles                                            internal_qpos                 46
                Joint Velocities                                        internal_qvel                 46
                Foot Position (Right)                                   r_toe_pos                       3
                Foot Position (Left)                                    l_toe_pos                       3
                Body COM in world frame*                                model_root_pos                 7
                Body COM vel in world frame*                            model_root_vel                 6
                Goal Keeper Position                                    goalkeeper_pos                 2
* The body COM position is represented with a free joint, hence the 7 dimensions: [x, y, z, q
                                                                                             x , qy , qz , qw ]. Similarly, the
                       body COM velocity is represented with 6 dimensions: [vx , vy , vz , α, β, γ].




                                                             26
D     Table Tennis First Place - Acting AI Full Solution
D.1   Reward Design

Our total reward function Rtotal integrates terms for dense grasping reward, dense tracking reward
and sparse task finishing reward:
                            Rtotal = wg Rgrasp + wc Rtracking + ws Rtask                                  (1)

The dense grasping reward encourages the agent to maintain a stable grip on the paddle throughout
the episode. It consists of three terms: the relative position error between the paddle and the grasp
site, the relative orientation error, and a penalty for finger opening:
                                                                   
        • relative position: rrel_p = exp −8 prel − pinit   rel  2
                                                                      
        • relative rotation: rrel_r = exp −4 arccos qrel · qinit  rel
                                            P                          
                                                   4
        • finger open: rf in_open = exp −5 i=0 ∥pfini − ppalm ∥2

where prel = R⊤    grasp (ppaddle − pgrasp ) is the paddle position expressed in the grasp frame. qrel =
  −1
qgrasp ⊗ qpaddle is the relative orientation quaternion between the paddle and the grasp site. pinit rel and
qinit
  rel  are their values   at the beginning    of each episode. And  pfini , ppalm denote the positions  of the
i-th fingertip and the palm center, respectively.
The dense tracking reward guides the agent to move the paddle towards the planned hit position
with the correct orientation before contact, and to match the target paddle velocity at the moment of
contact:
                                                             
       • reach distance: rreach = exp −4 ∥ppaddle − phit ∥2 , t < thit
                                                                
       • paddle orientation: rori = exp −2 ∥qpaddle − qhit ∥2 , t < thit
                                                           
       • paddle velocity: rvel = exp − ∥vpaddle − vhit ∥2 , t = thit

where phit , qhit and vhit are the planned hitting position, orientation and velocity computed by the
physics-based planner. thit is the planned hit time. The reach and orientation terms are active only
before thit and before any ball–paddle contact occurs, while the velocity term is a sparse signal
triggered only at t = thit .
The sparse task finishing reward provides goal-oriented feedback upon successful task completion. It
consists of three terms:

       • hit success: rhit = 1 if paddle successfully contacts the ball else 0
       • land success: rland = 1 if the predicted land position is within the valid range else 0
                                                                     
       • landing accuracy: racc = exp −0.5 ∥p̂land − popp_center ∥2

where p̂land is the analytically predicted landing position of the ball computed from its current position
and velocity after the hit, and popp_center is the center of the opponent half table. The landing accuracy
term racc is only activated when the ball is predicted to land within opponent range.

D.2   Computer Resources:

All experiments were performed on a local workstation featuring an AMD Ryzen 9 7950X 16-core
processor and a single NVIDIA GeForce RTX 4090 GPU with 24 GB of VRAM. A policy trained
from scratch over 300 million timesteps cost 51 hours of training time.

D.3   Training Details:

The policy was trained using the Proximal Policy Optimization (PPO) algorithm. The hyperparameters
are shown in Table 10.


                                                     27
                          Table 10: Hyperparameters for PPO Training.
      Category           Hyperparameter             Value
                         Learning rate               3 × 10−4 (linear decay)
                         Steps per update            200
      PPO
                         Batch size                  12800
                         Total timesteps             108
                         Architecture                MLP [1024, 1024, 512, 512, 256, 256]
      Network            Activation function         SiLU
                         Parallel environments       64
      Environment
                         Observation normalization   enabled
                         wrel_p                      1
                         wrel_r                      1
                         wfin_open                   1
      Reward weights     wreach                      5
                         wpaddle_ori                 5
                         wvel                        50
                         whit_success                100
                         wland_success               100
                         wland_acc                   100


D.4   Code Availablity

The code of Diff-Muscle is available at https://github.com/TaoshuaiZ/Diff-Muscle.
The submission repository is publicly available at https://github.com/TaoshuaiZ/Team_
ActingAI_Submit.




                                               28
E     Table Tennis Second Place - BioSyn Full Solution

E.1   Multivariate Gaussian Noise Definition

To improve the exploration efficiency within the redundant muscle action space, the exploration noise
in BioSyn is defined as a multivariate normal distribution associated with specific muscle synergy
weights:
                                                                            
              π(a|s) ∼ N Wa xa ⊕ Wh xh ⊕ Wt xt ⊕ Wp xp , Σsyn + Σo
                                                                                                  (2)
                Σsyn = diag Wa Σa Wa ⊤ , Wh Σh Wh ⊤ , Wt Σt Wt ⊤ , Wp Σp Wp ⊤
                                                                                     

where Wh , Wa , Wt , and Wp denote the synergy weights for the hand, arm, torso, and pelvis,
respectively. xh , xa , xt , and xp denote the corresponding synergy modulations. Σo denotes the
original exploration noise used in reinforcement learning. Σh , Σa , Σt , and Σp denote the synergy-
specific exploration noise for the hand, arm, torso, and pelvis, respectively.

E.2   Reward Design

The reward function was designed to guide the BioSyn agent to execute the striking commands issued
by the high-level planner. The key terms in the reward design are described as follows:

       • Hand–handle distance: rh_h = exp(−5 ∥phand − phandle ∥2 )
                                                                 
       • Paddle position: rpaddle = exp −5 ∥ppaddle − ptarget ∥2
                                                                        
       • Paddle orientation: rrot = exp − 10 vec qtarget ⊗ q−1   paddle   2

       • Paddle drop: rdrop = −1 if the paddle is dropped from the hand else 0
       • Hit success: rhit = 1 if paddle successfully contacts the ball else 0
                                                         
       • paddle velocity: rvel = exp − ∥vpaddle − vhit ∥2 , thit − 0.03s < t < thit + 0.03s

where phand , phandle , ppaddle , ptarget are the positions of the hand, the paddle handle, the paddle, and
the desired striking target, respectively. qpaddle , qtarget are the orientations of the current paddle and
the desired striking target, represented as unit quaternions. vec(q) denotes the vector part (last three
components) of quaternion q. ⊗ represents quaternion multiplication. vpaddle , vhit are the current
paddle velocity and the desired hitting velocity. thit denotes the desired hitting time. The indicator
functions in rdrop and rhit take values of 1 or 0 depending on whether the paddle is dropped or
successfully contacts the ball, respectively. The detailed curriculum reward weights are provided in
Sec. E.6.

E.3   Weakness-Aware Curriculum

Inspired by table tennis training principles, team BioSyn proposes a Weakness-Aware Table Tennis
Curriculum. During the early stage of training, the curriculum primarily emphasizes learning in the
default hitting environment. In the later stages, the hitting performance of the policy is systematically
evaluated to identify weak regions in the striking space. Based on this evaluation, the environment
sampling strategy at subsequent curriculum stage is adapted to increase the probability of sampling
balls from these weak regions, enabling the policy to progressively improve its deficient hitting skills.

E.4   Computer Resources

Team BioSyn trained their solution on a single Ubuntu server featuring two AMD EPYC 9654 CPUs
(96 cores each), an NVIDIA GeForce RTX 4090 GPU with 24GB of memory, and 256GB of DDR5
RAM. Training required nearly 15 days to complete 1 billion steps.

E.5   Training Details

The key hyperparameters for reinforcement learning in BioSyn are summarized in Table 11.


                                                    29
               Table 11: Hyperparameters for the BioSyn training framework.
             Hyperparameter                    Value
             Number of Parallel Environments        180
             Network Archiecture                    LSTM[256]+MLP[256, 256, 150]
             Number of Hand Synergies               20
             Number of Arm Synergies                20
             Number of Torso Synergies              100
             Actication Function                    Relu
             Learning Rate                          1 × 10−5
             Updates per Iteration                  5
             Entropy Coefficient                    1 × 10−5
             Batch Size                             2048
             Steps per Update                       512


E.6   Code availability

The BioSyn detail training code is available at https://github.com/Siyuan-Liu99/BioSynTT.
The submission repository is publicly available at https://github.com/Siyuan-Liu99/
myochallenge2025eval_BioSyn.




                                               30
F     Table Tennis Third Place - LNSGroup Full Solution
F.1   Reward Design

Our reward (Rtotal ) decomposes the task into dense geometric tracking, biomechanical kinematics,
sparse task completion, and rule penalties:
               Rtotal = wtrack Rtrack + wquat Rquat + wtorso Rtorso +
                        wpalm Rpalm + whit Rhit + wsuccess Rsuccess + wown Rown

1. Dense Geometric Tracking: Guides the paddle towards the predicted physical targets.
                            Tracking : Rtrack = exp (−5∥ppaddle − phit ∥2 )
                                                                      
                                                1    dpaddle · dhit
                          Orientation : Rquat =                     +1
                                                2 ∥dpaddle ∥∥dhit ∥
where ppaddle and dpaddle denote the position and normal direction vector of the paddle surface,
while phit and dhit represent the optimal striking position and desired striking direction predicted by
the physical prior model, respectively.
2. Biomechanical Kinematics: Introduces an upright torso reward (Rtorso ) and a palm-to-handle
proximity reward (Rpalm ) to prevent spine collapse and paddle decoupling independently, ensuring a
stable and continuous mechanical base.
3. Sparse Task Completion: Functions as the core task incentive.

       • Hit Sparse: 1.0 when the paddle successfully strikes the ball.
       • Success: 1.5 if the ball lands inside an optimal rectangular target zone on the opponent’s
         side, 1.0 for any valid opponent table hit, and 0.0 otherwise.

4. Rule-based Penalty: Penalizes the agent if the ball bounces on its own side after the expected
hitting time thit (Rown = −1.0).

F.2   Computational Resources

Training experiments were conducted on a workstation equipped with a single NVIDIA 80GB A100
GPU and two Intel(R) Xeon(R) Gold 6348 CPUs. Each RL training run was initialized from scratch
for 100 million steps, taking approximately 12 hours.

F.3   Training and Evaluation Details

The key hyperparameters for the reinforcement learning framework are summarized in Table 12.

                 Table 12: Hyperparameters for the CrossQ training framework.
              Hyperparameter                       Value
              Number of Vectorized Environments        64
              Hidden Dimension                         1024
              Hidden Layers                            2
              Base Learning Rate                       5 × 10−4 (Linear decay to 20%)
              Entropy Learning Rate (α)                7 × 10−3
              Buffer Size                              1 000 000
              Updates per Iteration                    1



F.4   Code availability

The training and submission code is available at https://github.com/LNSGroup/
MyoChallenge2025-LNSGroup.


                                                  31
G     Soccer First Place - Servette MyoClub Full Solution

G.1   From Motion Imitation to Soccer Kicking (Teacher Policy)

KINESIS’ motion imitation policy tracks reference motions via target keypoint observations. To
obtain a target-reaching policy, a simple observation modification was applied: the root (pelvis)
position in the target observation was set to the desired target location, while all other target keypoints
were set to the current positions of their respective body parts, following prior work [56, 23]. Motion
tracking reward components were also replaced with target-reaching rewards inspired by Won
et al. [68]. This reward formulation directs the policy to walk toward the specified target while
maintaining a natural gait for the rest of the body.
The target position was uniformly sampled across a 2 × 2 m2 area around the agent, until the policy
successfully reached the entire sampled region. Subsequently, the agent was transferred to the
penalty-kick environment, where the target position was set to the ball’s location, and the agent was
initialized at a default upright position. The target-reaching policy was fine-tuned with a reward
based on ball velocity along the goal direction. The kicking policy was trained and evaluated in an
environment without joint-level noise and with only minor position randomization. This produced a
teacher policy that could reliably walk towards the ball and kick it, achieving a goal conversion rate
of approximately 25% in the MyoChallenge evaluation setting. For comparison, training a kicking
policy from scratch with the same reward fails entirely, as the agent cannot learn to balance, walk,
and kick simultaneously in the 290-dimensional muscle action space.

G.2   Retargeting to the MyoChallenge environment

The soccer kicking policy from the previous stage operates on KINESIS observations (453 di-
mensions), whereas the MyoChallenge environment provides a different observation space com-
prising: internal_qpos, internal_qvel, grf, torso_angle, ball_pos, model_root_pos,
model_root_vel, muscle_length, muscle_velocity, and muscle_force. To bridge this gap,
a four-step adaptation pipeline was employed.

Offline trajectory collection with success filtering. The KINESIS soccer kicking policy (teacher)
was deployed in the MyoChallenge environment with domain randomization (random joint-level noise
and random initial positions) and trajectory rollouts were collected. Trajectories were filtered based
on success rate, retaining only episodes with successful kicking behavior. At each timestep, both
the KINESIS-format and MyoChallenge-format observations we recorded, along with the teacher’s
muscle controls.

Student policy pre-training. A student policy, which takes MyoChallenge observations as input,
was pre-trained on the filtered offline trajectories via supervised learning (behavioral cloning on the
collected dataset). This provided a stable warm-start initialization for the subsequent on-policy stage.

On-policy behavior cloning (Online DAgger, OBC [23]). The pre-trained student was further
refined through on-policy behavior cloning (Figure 7). The environment was modified to simul-
taneously generate both KINESIS and MyoChallenge observations from the same simulator state.
The KINESIS observation was routed to the teacher policy to produce target muscle controls; the
MyoChallenge observation was provided to the student policy. The student was trained to minimize
the mean squared error (MSE) between its predicted activations and the teacher’s activations. This was
performed on-policy: the student generated its own rollouts and the teacher provided target activations
at each visited state, avoiding the covariate shift inherent in offline-only behavioral cloning, similar
to DAgger [69]. Domain randomization (random joint-level noise and random initial positions) was
applied throughout this stage. After OBC, the student policy achieved a goal conversion rate of 34%,
exceeding the teacher policy’s 25%, with a MSE of approximately 0.019.

Reinforcement learning fine-tuning. The behavior-cloned student policy was fine-tuned with PPO
using conservative updates to preserve the learned locomotion prior. Specifically, three techniques
were considered: (1) reduced PPO clipping parameter ε to constrain policy updates; (2) reduced actor
learning rate; and (3) an additional behavior cloning regularization term, yielding the combined loss:


                                                    32
                      Figure 7: Schematic diagram of online behavior cloning.



                                        L = LPPO + λBC LBC ,                                         (3)
where λBC controls the strength of the behavior cloning regularizer. Early termination conditions
were applied when the agent lost balance or when the ball was clearly out of scoring range.

G.3   Reward Design

KINESIS motion imitation reward. The base reward combined four weighted terms: position
tracking (weight 0.6, k = 200), velocity tracking (weight 0.2, k = 5), energy regularization (weight
0.1, ℓ1 + ℓ2 on muscle activations), and upright reward (weight 0.1, k = 3).

KINESIS target reaching reward. Position and velocity tracking components were replaced with
                           rtrack = δt−1 − δt ,     rsuccess = 1[δt < 0.1] ,                         (4)
where δ denotes the distance between the root and the target position.

Soccer kicking reward. The kicking policy was fine-tuned with a reward based on the forward ball
velocity vx (along the goal direction) and the lateral ball velocity vy :
                                                                vx
                                   
                                   vx if vx ≥ ϵv and                   ≥ 1,
                           rkick =                           |v |
                                                               y + ϵr                        (5)
                                   0 otherwise,

where ϵv = 10−2 m/s is a minimum forward-speed threshold, and ϵr = 10−6 is a small regularizer
that prevents division by zero. The two gate conditions enforce that (i) the ball is moving forward
with non-negligible speed, and (ii) the forward-to-lateral velocity ratio satisfies vx /|vy | ≥ 1, which
restricts rewarded kicks to a cone of ±45◦ around the goal direction. When both conditions are
met, the reward equals the forward ball velocity, encouraging maximum kick power. Angular kicks
toward the goal corners emerged as a natural consequence of goalkeeper movement randomness, the
randomly off-center initialization of the agent, and the goal-scoring reward, without explicit reward
shaping for kick angle.

G.4   Results

The pre-trained KINESIS policy managed to move towards the ball and initiate contact with it in
a zero-shot manner, thus already solving the hard problem of balance and locomotion (Figure 6).
After implementing the full training pipeline, the policy consistently converted penalty kicks against
random, static, and adversarial goalkeepers.

G.5   Analysis of motor dimensionality

The challenge of controlling over-actuated, high-dimensional musculoskeletal systems is well-
documented in neuroscience [70, 71]. An influential hypothesis claims that brain solves this challenge
through simplification by grouping functionally or anatomically related muscles together and exe-
cuting control at that group level [72]. In animals and humans, many previous studies have used
principal component analysis to show that both kinematic trajectories and electromyography signals
evolve along trajectories that are low-dimensional relative to their degrees of freedom. However, an


                                                  33
alternative explanation for these findings is that low dimensionality is a consequence of and not a
requirement for good motor control [71]. To distinguish these two accounts, it is necessary to quantify
control dimensionality via its effect on task performance instead of through signal reconstruction.
While such causal experiments are difficult in real animals, they are particularly well-suited for
in-silico models of motor control, where the control signal can be analysed and manipulated at will in
real time.
We recorded muscle activity patterns generated by the musculoskeletal policy during the penalty-kick
task. We then extracted all principal components from the 292-dimensional signal acquired by
concatenating 1000 episodes. We found that 50 components were sufficient to explain 95.03% of the
control variance, significantly lower than the full control dimensionality. We subsequently performed
a control subspace inactivation (CSI) experiment, where, at each time step, we projected the control
signal produced by the policy onto a subspace spanned by a subset of PCs prior to applying it to the
muscles (see Chiappa et al. [21] for method details). Interestingly, we found that 95% of relative
task performance was only reached with 120 PCs or more, despite these components only providing
marginal explained variance.
These findings were consistent with previous studies done on dexterous hand movement, general
locomotion, as well as across motor tasks performed by a single control policy [21, 56, 23], suggesting
that signal reconstruction methods may underestimate the functional dimensionality of control signals.
They furthermore suggest that the low-dimensionality of the control signal is a consequence of and
not a requirement for good motor control [71].

G.6   Ablation: Pipeline Stage Contributions

The teacher policy achieved a goal rate of 25% when evaluated in the MyoChallenge environment.
After on-policy behavior cloning, the student policy achieved a goal rate of 34%, yielding a 9
percentage-point improvement over the teacher, with a final muscle activation MSE of approximately
0.019 between student and teacher. This improvement indicates that the student not only successfully
replicated the teacher’s behavior but may have benefited from operating in the MyoChallenge
observation space and with random noise.
After performing RL fine-tuning for 100K steps, the goal conversion rate remained at approximately
34%, but energy consumption was substantially reduced. This result indicates that fine-tuning primar-
ily serves to improve energy efficiency rather than increase the goal conversion rate. In hindsight, the
reason performance did not improve further may be attributed to the provided observations, which
did not include potentially relevant information, such as the goalkeeper’s state. A flexible aiming
mechanism might also further improve performance.

G.7   Compute Resources

All models were trained on a single NVIDIA A100 GPU and 128 CPU threads, with 128 parallel
environment instances. Stage 1 training, from imitation learning to the ball-kicking policy, took
approximately 14 days.

G.8   Training and Test Details

KINESIS is described in Simos et al. [56].

G.9   Code availability

KINESIS: (including motion imitation, target reaching, and ball kicks) code is publicly available at
https://github.com/amathislab/Kinesis.
Our submission repository is publicly available at https://github.com/amathislab/
mc25-soccer-servette-myoclub.




                                                  34
H    Advocacy, Tutorials, and Baseline
To broaden the reach of the competition, we recruited a global and diverse team of volunteers working
with the MyoSuite toolbox to improve accessibility and participation. The current advocacy team is
listed here: https://sites.google.com/view/myosuite/myochallenge/advocacy-2025/
current-advocates
Outreach was conducted through multiple channels, including direct invitations to prior MyoSuite
users, targeted emails to relevant research groups, announcements on community forums, and
promotion via social and professional networks. This approach helped engage contributors across
different time zones, expertise levels, and application domains.
Advocates contributed both technically and pedagogically: they co-developed tutorials, tested baseline
solutions, identified usability bottlenecks, and iteratively refined documentation based on user
feedback. Through coordination meetings and asynchronous collaboration, the team ensured that
materials remained consistent, up-to-date, and aligned with participant needs.
Together, we developed a range of support resources, including Google Colab tutorials, step-by-step
video guides, baseline implementations, and interactive workshops, as summarized below.
Colab Tutorials:

       • MyoChallenge Tutorial1 - Getting Started with MyoSuite: https://colab.research.
         google.com/drive/1AqC1Y7NkRnb2R1MgjT3n4u02EmSPem88?usp=sharing
       • MyoChallenge Tutorial2 - Getting Started with Table Tennis Baselines: https:
         //colab.research.google.com/drive/15w_dzEYI9SVFLFW_OmaDOwtWJ9tu4os6?
         usp=sharing
       • MyoChallenge Tutorial3 - Submission Instructions: https://colab.research.google.
         com/drive/11vRvWMWykNrd_5ViJVGdLXz2pnbc5QEs?usp=sharing

Manipulation Baselines Huggingface URL: hf://cheryl-tootty/mc25-tt-baseline
MyoChallenge 25’ Video Tutorials and Webinars:

       • MyoChallenge 25’ Kick Off Webinar: https://youtu.be/5u-BEDnHa0k?si=
         Y6BJtLdrQZFQDe1y
       • Reinforcement Learning for human motion control: https://youtu.be/fcYkDYVRPho?
         si=oB6qXLyC6z5k9Wyn
       • Tutorial: An introduction to using MyoChallenge Bot : https://youtu.be/
         v8PZYj0wNGw?si=Fi4ZnRICxFZZEGYu
       • MyoChallenge’25 Video Walkthrough by Siyuan Liu: https://www.youtube.com/
         watch?v=4v33Nv_kMzk
       • MyoChallenge’25      2nd     Webinar:       https://youtu.be/mOrr4Sf5EGc?si=
         vYQgkzYVpUP4MOZa

Documentation:

       • Official MyoChallenge ’25 Documentation: https://myosuite.readthedocs.io/en/
         latest/challenge-doc2025.html
       • MyoChallenge ’25 GitHub Discussion Board: https://github.com/MyoHub/
         myosuite/discussions/categories/myochallenge-2025




                                                 35
I   MyoChallenge Bot
In this edition of MyoChallenge, we also provide the participants with a Discord bot that allows the
generation of kinematics data of the MyoSkeleton [73] from any uploaded video in the form of an
h5 file and a skeleton video, as shown in Figure 8. Participants are able to convert the kinematics
references from myoskeleton to h5 files and use imitation learning on self-recorded or internet data if
necessary.




           A: example soccer video                               B: example table tennis video
Figure 8: Example video conversion ability of MyoChallenge Bot. A: left column as soccer penalty
kick example. B: right as table tennis rally example.




                                                  36
