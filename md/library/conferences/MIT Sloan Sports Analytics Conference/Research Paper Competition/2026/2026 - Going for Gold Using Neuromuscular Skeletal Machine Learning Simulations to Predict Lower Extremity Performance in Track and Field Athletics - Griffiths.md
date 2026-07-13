<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Going for Gold Using Neuromuscular Skeletal Machine Learning Simulations to Predict Lower Extremity Performance in Track and Field Athletics - Griffiths.pdf -->

# **Going for Gold: Using Neuromuscular Skeletal Machine Learning Simulations to Predict Lower Extremity Performance in Track and Field Athletics** 

Other Sports Paper ID: 55 

## **Abstract** 

This study introduces a field-deployable framework that converts synchronized smartphone video into neuromuscular features capable of predicting performance in track-and-field movements. Using OpenCap’s validated multiview motion-capture pipeline, we reconstructed 3D kinematics and mapped them to a musculoskeletal model solved with IPOPT, yielding internally coherent, but not force-plate-validated, estimates of joint torques, muscle activations, and ground-reaction forces. Thirty javelin throws performed at four intensities (25–100%) showed consistent, effort-sensitive neuromechanical patterns, including deeper knee loading, increased pelvis rotation, higher braking impulses, and stiffer block-leg stabilization. These internal dynamics formed the basis of a predictive modeling pipeline using XGBoost and recurrent neural networks, achieving ensemble accuracy of R² = 0.92 in predicting throw distance. Feature attribution showed that vertical GRF impulse, subtalar stability, and pelvis–list torque were the strongest determinants of performance. The results demonstrate that neuromuscular simulation combined with machine learning can produce athlete-specific performance intelligence directly from smartphone video, enabling scalable biomechanical assessment without laboratory infrastructure. 

## **1. Introduction** 

Athletic performance and injury risk are emergent properties of high-dimensional, multi-joint systems in which neuromuscular control, biomechanics, and physiology interact across milliseconds. In elite competition, seemingly minor inefficiencies, delayed hip rotation, unstable ground-reaction timing, or sub-optimal sequencing, can separate a personal best from a season-ending injury. Yet despite decades of progress in wearable and laboratory instrumentation, the true internal forces and activations driving these outcomes often remain invisible. 



1 



**Figure 1.** Neuromuscular skeletal models showing kinetic activations of running, javelin throw, and long jump trials visualized in OpenSim. 

### **1.1 Limitations of Current Measurement Paradigms** 

Current field-based monitoring relies on GPS, accelerometers, and inertial measurement units (IMUs), which quantify global workload and velocity but do not resolve how forces are produced and transferred through the body. Laboratory-based approaches, markerbased optical motion capture, embedded force plates, and electromyography (EMG), offer precision but are costly, intrusive, and unsuitable for continuous, real-world deployment. This gap leaves coaches and researchers with a descriptive, rather than mechanistic, understanding of movement. 

### **1.2 Why Markerless Biomechanics Are Needed for Sports Analytics** 

Traditional field-based monitoring, GPS, IMUs, accelerometers, quantifies workload but cannot reveal _how_ athletes generate or absorb force. Laboratory solutions such as marker-based motion capture or force plates provide precision but are impractical for continuous monitoring, require controlled environments, and cannot scale to daily training. Modern computer-vision pipelines now allow internal biomechanical states to be inferred directly from video. Frameworks such as OpenCap reconstruct 3D joint trajectories and use optimal-control solvers to estimate muscle forces and joint torques. Importantly, these tools do not replace laboratory force plates but offer a scalable path to _approximating_ force-generation strategies in real field conditions. 



2 

Our work leverages this capability not to re-validate OpenCap, but to examine whether the internal dynamics reconstructed from accessible video contain enough structure to predict athletic performance. This is the core scientific question of the paper. 

### **1.3 Objective of This Study and Technical Contribution** 

The technical contribution of this study is not the reconstruction pipeline itself. Rather, it is the integration of reconstructed neuromuscular dynamics with predictive modeling to evaluate whether internal force-generation patterns can explain, and forecast, throw distance. 

Across thirty javelin throws (two athletes × fifteen trials, across 25–100% effort), we: 

1. Captured synchronized smartphone video in the field. 

2. Reconstructed 3D joint kinematics and internal biomechanics using OpenCap’s validated pipeline. 

3. Extracted neuromuscular features, joint torques, muscle activations, GRF impulses, sequencing metrics. 

4. Trained predictive models (XGBoost, RNN, ensemble) to test whether these internal dynamics can explain performance. 

5. Interpreted model attributions to identify which low-extremity mechanics matter most for distance. 

Our contribution is not force reconstruction alone, but testing whether internal neuromechanical variables reconstructed from video are predictive of athlete performance. We show that combining muscle-driven dynamics with nonlinear machine learning explains 92% of variance in throw distance, revealing how timing, torque sequencing, and foot-stabilization jointly determine success. 

This moves biomechanics from _descriptive_ to _predictive._ 

## **2. Methods** 

### **2.1 Data Capture and Multiview Smartphone Setup** 

All biomechanical data were collected in a field setting using a dual-smartphone configuration designed to meet OpenCap’s requirements for accurate multiview reconstruction. Two iPhone 13 cameras, each recording at 60 frames per second, were positioned roughly six to eight meters from the runway and separated by approximately ninety degrees so that one camera captured a lateral view of the thrower while the other captured a rear-quarter perspective. Prior to recording, both devices underwent OpenCap’s standardized calibration routine, which included a brief wand sequence and a static T-pose. This procedure enabled OpenCap to estimate camera intrinsics and extrinsics, align the spatial coordinate systems of the two video streams, and establish synchronized timelines across cameras. 

Two right-handed collegiate athletes each completed fifteen throws, resulting in a dataset of thirty total trials. Each athlete performed five throws at four self-selected intensity levels, 25%, 50%, 75%, 



3 

and 100% effort, allowing assessment of whether reconstructed biomechanics scale in interpretable ways with exertion. All videos were uploaded to OpenCap immediately following collection, where they were processed through the platform’s automated 3D reconstruction pipeline. 

### **2.2 Skeletal Modeling and Kinematic Reconstruction** 

Once uploaded, each synchronized video pair was processed through OpenCap’s validated multiview markerless motion-capture system. OpenCap first applied a deep-learning 2D keypoint detector to each frame of each camera view. The two sets of detections were then triangulated using the calibrated camera geometry to reconstruct three-dimensional joint positions. These reconstructed joint trajectories were fit to a scaled OpenSim musculoskeletal model, yielding continuous estimates of segment orientations and joint angles for the pelvis, hips, knees, ankles, spine, shoulders, and upper extremities. OpenCap’s kinematic reconstruction has been validated against laboratory motion-capture systems, with reported joint-angle errors of approximately four to six degrees. We retained the system’s default settings and introduced no additional filtering, smoothing, or geometric transformations. All kinematic results in this study therefore reflect OpenCap’s native reconstruction pipeline. 

### **2.3 Muscle-Driven Dynamic Simulation** 

To obtain dynamically consistent estimates of internal biomechanics, OpenCap applied a muscle-driven simulation based on the Lai–Uhlrich musculoskeletal model and solved using the IPOPT nonlinear optimizer. This framework seeks muscle excitations, fiber states, joint torques, and residual forces that reproduce the observed joint kinematics as closely as possible while satisfying the physical laws governing musculoskeletal dynamics. These include Newton–Euler equations of motion, muscle activation dynamics, force–length–velocity relationships, anatomical joint limits, and regularization of residual torques to ensure physiological realism. 

Although OpenCap’s joint-moment and ground-reaction force estimates have been validated for activities such as walking, squatting, and drop-jump landings, equivalent force-plate validation for high-velocity ballistic tasks like javelin throwing has not yet been established. Accordingly, in this study we use OpenCap’s kinetic outputs as approximate but internally coherent reflections of movement coordination. Our analyses focus on timing, scaling, and neuromechanical patterns, such as pelvis–hip sequencing and block-leg stability, rather than interpreting absolute force magnitudes as ground-truth. 

### **2.4 Extracted Biomechanical Variables** 

The OpenCap simulations provided detailed frame-wise estimates of joint angles, angular velocities, pelvis orientation, center-of-mass accelerations, ground-reaction forces, joint torques, and muscle activation envelopes. These outputs enabled extraction of a comprehensive set of neuromechanical variables relevant to javelin performance. For the lower extremities, we quantified hip, knee, and ankle flexion angles and their corresponding ranges of motion, with particular emphasis on right-knee loading during the approach and left-ankle excursion as an indicator of block-leg 



4 

stabilization. Pelvic mechanics were characterized through transverse-plane rotation and the timing relationships between pelvis rotation and hip and knee flexion, providing interpretable measures of proximal–to–distal sequencing. Muscle activations for major functional groups, including gluteus maximus, biceps femoris long head, rectus femoris, gastrocnemius, and iliopsoas, were used to contextualize changes in coordination at increasing effort levels. 

All biomechanical variables were normalized to the percentage of each movement cycle to facilitate comparison across trials and intensities. Neuromechanical features were then aggregated across the thirty throws for use in statistical analyses and predictive modeling. 

### **2.5 Dataset Characteristics and Intensity-Dependent Kinematics** 

Across the thirty throws performed by the two athletes, the reconstructed movement patterns displayed clear and repeatable scaling with reported effort. As intensity increased from 25% to 100%, sagittal-plane loading deepened, pelvis rotation increased, and block-leg stability became more pronounced. At lower intensities, peak right-knee flexion values were typically near eighty degrees, increasing to approximately ninety-three degrees at 50%, roughly one hundred degrees at 75%, and nearly one hundred seventeen degrees at maximal effort. Left-ankle excursion followed a similar monotonic pattern, increasing from approximately twenty-one to twenty-four degrees at 25%, rising to roughly thirty degrees at 75%, and reaching around thirty-five degrees at 100%. Pelvis rotation exhibited some of the strongest scaling effects: transverse-plane rotation ranged from approximately ninety degrees during 25% throws to more than one hundred sixty degrees during 50% throws, with 75% and 100% trials maintaining elevated rotation consistent with increased hip–shoulder separation. These intensity-dependent changes were consistently reproduced across trials within each intensity category. For both athletes, joint-angle waveforms for the five throws at each effort level clustered tightly, with typical within-intensity standard deviations below four degrees in the major sagittal joints. The monotonic and repeatable kinematic scaling observed across the dataset supports the reliability of the reconstructed motions and provides confidence that the neuromechanical features extracted from them reflect meaningful differences in movement coordination as effort increases 

Figures 3–5 provide representative examples of reconstructed kinematics (Fig. 3), joint torques (Fig. 4), and 3D ground-reaction forces (Fig. 5). These visuals confirm that the solver recovered smooth, intensity-sensitive dynamics suitable for quantitative modeling. 

### **2.6 What This Study Adds Beyond OpenCap** 

OpenCap provides kinematic reconstruction and internally consistent kinetic estimation, but it does **not** explain how these internal variables relate to sport-specific performance. Our contribution is the integration of: 

- trial-level neuromuscular feature engineering, 

- sequence-based coordination metrics, 

- nonlinear and temporal machine-learning models, and 

- athlete-specific performance interpretation. 



5 

OpenCap reconstructs _how the athlete moved_ . Our modeling framework explains _how that movement produced performance_ , and _which internal mechanics mattered most_ . 

### **2.7 Measurement of Throw Distance** 

To align internal neuromuscular dynamics with external performance, throw distances were measured directly on-field using a laser rangefinder (±0.10 m accuracy). Each throw was marked immediately upon impact and linked to its corresponding trial using synchronized timestamps from the iPhone camera clocks. No smoothing, averaging, or retroactive adjustment was applied. Distance labels therefore represent ground-truth external performance against which all predictive models were evaluated. 

### **2.8 Limitations and Validation Scope** 

Given two athletes, many validation techniques are statistically meaningless; however, internal face validity and across-athlete agreement (Section 3.5) provide evidence that reconstructed dynamics scale consistently. This study should therefore be interpreted as: 

**a methodological pilot** , **not a generalizable performance-norm reference.** We test whether _relative_ neuromuscular dynamics predict performance. 



**Figure 2.** Methodology overview from Video to Optimization to Prediction of this analysis. 



6 

### **3. Neuromuscular Dynamics of the Javelin Throw** 

The neuromuscular outputs generated by the IPOPT simulation, joint torques, muscle activations, and 3D GRFs, reveal how athletes scale their mechanical strategy across effort levels and provide the internal variables later used in predictive modeling. Rather than studying surface kinematics alone, we analyze the _forces_ the solver infers and the _timing_ with which athletes coordinate braking, rotation, and stabilization. 

Figure 3 shows all reconstructed joint-angle coordinate trajectories for a representative trial. Figure 4 visualizes the joint torques and segmental rotations recovered from the solver. Together, these figures demonstrate that the model produces smooth, intensity-sensitive internal dynamics that form a meaningful substrate for machine-learning analysis. 

### **3.1 Intensity-Dependent Changes in Kinematics** 

Kinematic profiles revealed clear and interpretable scaling across effort levels. At low intensity (25–50%), the approach mechanics were controlled and compact: right-knee flexion rarely exceeded 90°, pelvis rotation remained below 100° and left-ankle excursion stayed near 20°. As effort increased, each athlete adopted a more forceful and mechanically efficient loading pattern. 

In the 75% and 100% trials, the right knee absorbed substantially more load during the penultimate and plant steps, with peak flexion increasing to approximately 105° at 75% and reaching nearly 117° in maximal throws. This deeper flexion corresponded to a more aggressive deceleration strategy that prepared the trunk for higher angular velocities. 

A similar pattern was evident in the left ankle, which transitioned from a compliant absorber at low intensities to a stiff, force-redirecting block at maximum effort. Dorsiflexion and inversion angles increased from the mid-20° range at 25% effort to more than 35° in the 100% trials. 

Pelvis-rotation amplitudes showed the clearest shift in strategy. Low-intensity throws relied on minimal hip–shoulder separation, typically around 90°, whereas moderate and high intensities showed explosive rotation amplitudes exceeding 150°, with several maximal throws reaching 165–170°. This abrupt increase reflected the transition from “placing” the javelin to executing a full kinetic-chain sequence. 



7 



**Figure 3.** Panel plot of all tracked skeletal coordinates throughout the motion (Athlete A: Trial 3, 50%) 

Figure 3 illustrates that across all trials the smooth, intensity-dependent kinematic trajectories produced by the reconstruction pipeline, which form the basis for the neuromuscular inferences in Section 3. Both athletes exhibited highly repeatable joint-angle curves within each intensity condition, suggesting that OpenCap’s reconstruction and dynamic fitting pipeline produced reliable trial-to-trial outputs. These qualities enabled a detailed analysis of how specific neuromechanical variables scaled with throwing intensity. 

### **3.2 Joint Torque Production and Mechanical Strategy** 

The estimated joint torques quantified how athletes generated, braked, and transferred momentum across intensities. Although absolute magnitudes were lower than laboratory force-plate benchmarks, an expected outcome for markerless models, the _patterns_ were biomechanically coherent and tightly coupled to performance. 

Hip-extension torque increased monotonically with effort, rising from low-force profiles in the submaximal throws to peaks near 50 N·m in the maximal trials. In javelin technique, hip torque during the final stride is a key contributor to approach velocity and proximal acceleration, and its scaling matched the observed increases in pelvis-rotation amplitude. 

Knee extension on the left block leg exhibited sharp intensity-dependent changes. Low-intensity throws displayed modest braking torques (15–18 N·m), but at maximal effort torque rose to roughly 25–30 N·m. This behavior corresponded directly to the deeper right-knee flexion and the stiffer 



8 

left-ankle block mechanics observed in the kinematic data, demonstrating that the solver captured the athlete’s shift toward a more forceful, momentum-redirecting block leg at higher intensities. 



<!-- Start of picture text -->
the athlete’s shift toward a more forceful, momentum-redirecting block leg at higher intensities.<br>Figure 4.  Joint Torques, Extensions, and Rotations during recorded javelin motion (Athlete A: Trial<br><!-- End of picture text -->

**Figure 4.** Joint Torques, Extensions, and Rotations during recorded javelin motion (Athlete A: Trial 3, 50%). This shows that hip-extension torque rises sharply at ~1.3 s, precisely when pelvis angular velocity accelerates. 

Ankle and subtalar moments provided additional insight into stability strategy. High-intensity trials consistently exhibited larger inversion and plantarflexion moments in the left ankle, reflecting a firmer, more rigid base for trunk rotation. This increased stiffness is a hallmark of elite javelin technique, where a stable block leg enables efficient transfer of horizontal momentum into upper-body rotation and arm acceleration. 

Hip-extension moments increased systematically with intensity and frequently reached values near 50 N·m in the maximal throws. Knee-extension moments displayed similar trends, rising from low values in the submaximal trials to approximately 25–30 N·m in the highest-intensity attempts. These magnitudes fell below those reported in controlled laboratory settings but exhibited stable intra-athlete scaling, indicating that the IPOPT solution captured the relative mechanical demands of each throw. Ground-reaction force profiles behaved similarly. Vertical forces in low-intensity trials typically ranged from 600 to 650 N, whereas high-intensity trials approached 740 N. Even though these absolute values underestimate those expected in elite-level competition, the timing and ordering of GRF peaks closely matched the structure of the kinematic waveforms: peak forces consistently coincided with the onset of knee extension and the rapid increase of pelvis angular velocity. The coherence between kinematic and kinetic timing supports the internal validity of the dynamic reconstruction. Across all conditions, the optimization maintained low residual torques and smooth temporal profiles, consistent with OpenCap’s validation criteria. This stability further 



9 

indicates that the system produced physically plausible solutions within the bounds of its validated model and that the reconstructed dynamics can be investigated meaningfully at the level of coordination patterns, sequencing, and relative magnitudes. 

The torque profiles in Figure 4 reveal the internal sequencing patterns, hip, knee, subtalar, that are later shown to predict distance in Section 5 

### **3.3 Ground-Reaction Force Profiles and Braking Efficiency** 

Ground-reaction forces (GRFs) revealed the clearest mechanical signature of increasing throw intensity. Although absolute magnitudes fell below those reported in laboratory settings, the relative changes, waveform shapes, and timing relationships were highly consistent across both athletes. 



**Figure 5.** 3D Ground Reaction Forces during recorded javelin motion (Athlete A: Trial 3, 50%). Figure 5’s GRF patterns directly correspond to the braking impulses identified as the top predictor in Figure 7 

The vertical GRF peak occurs at the exact moment knee extension begins (~1.4 s), and the medial–lateral force oscillations shrink as intensity increases, confirming improved frontal-plane stability. Vertical GRF in low-intensity trials (25–50%) ranged from 600–650 N, reflecting controlled braking and limited momentum redirection. At 75% and 100% intensities, these peaks increased to 700–740 N, and the force rise occurred more abruptly. The increased rate of force development is especially important in javelin technique, where the block leg must rapidly convert forward momentum into trunk rotation and elastic loading of the shoulder. 



10 

Importantly, the GRF peaks aligned precisely with the onset of knee extension and the steep rise in pelvis angular velocity. This timing relationship reflects the classic javelin kinetic chain: a hard block creates a rotational “whip” through the pelvis and trunk. The solver consistently reproduced this coordination pattern, confirming internal coherence between kinematics, torques, and ground forces. 

Even without absolute lab-level accuracy, the GRF profiles provided meaningful indicators of performance strategy, specifically, the athlete’s braking efficiency and their ability to maintain stiffness and stability during high-force plant phases. 

### **3.4 Muscle Activation Sequencing and Coordination Strategy** 

The IPOPT-derived muscle activation envelopes offered a deeper view into coordination strategies across intensities. Although activation magnitudes must be interpreted as model-based estimates rather than direct EMG measurements, the timing patterns were stable across trials and aligned well with known throwing mechanics. 



<!-- Start of picture text -->
well with known throwing mechanics.<br><!-- End of picture text -->

**Figure 6.** All muscle activations during recorded javelin motion (Athlete A: Trial 3, 50%) 

At low intensities, gluteus maximus activation appeared late relative to pelvis rotation, suggesting a controlled, low-force approach. As intensity increased, gluteal activation shifted earlier in the cycle and grew in amplitude, supporting earlier and more forceful proximal acceleration. Figure 6 above shows Gluteus maximus activating ~40–60 ms before pelvis rotation in high-intensity trials, matching known sequencing patterns in elite throwers 



11 

Quadriceps activation on the left block leg exhibited an even clearer intensity dependence. Maximal efforts showed large, rapid bursts aligned with the moment of deepest knee flexion. This reflected the block leg’s increased braking load and its pivotal role in redirecting horizontal momentum. 

The gastrocnemius–soleus complex displayed a distinct transition between low and high effort. At maximal intensity, plantar flexor activation spiked sharply as athletes stabilized the ankle and maintained a rigid block structure. This behavior paralleled the increased ankle excursion seen in the kinematic profiles and further confirmed the solver’s ability to capture whole-body coordination dynamics. 

Across all trials, the sequencing pattern, glutes → quadriceps → trunk rotation → arm mechanics, was preserved. This internal consistency supports the validity of the reconstructed coordination strategies and reinforces the relevance of these neuromuscular variables for performance modeling. 

### **3.5 Internal Consistency and Cross-Athlete Agreement** 

To assess internal validity, we examined trial-to-trial repeatability of reconstructed biomechanics within effort levels and compared patterns across athletes. Joint-angle trajectories showed exceptionally high within-intensity consistency, with variations of only a few degrees for major sagittal-plane joints. Pelvis-rotation trajectories, while naturally more variable due to their magnitude, maintained highly similar timing and waveform structure across repeated trials. 

Importantly, both athletes exhibited nearly identical qualitative scaling behaviors across intensities. Regardless of individual technique or anthropometry, deeper right-knee flexion, greater left-ankle excursion, and enlarged pelvis-rotation amplitudes accompanied higher-effort throws in every case. When feature vectors derived from the reconstructions were projected into a low-dimensional embedding, the four intensity levels separated into distinct clusters, and this structure was preserved across athletes. This cross-athlete agreement demonstrates that the neuromechanical features obtained from the OpenCap pipeline were not idiosyncratic artifacts but rather robust descriptors of effort-dependent changes in javelin mechanics. 

Together, these results show that the reconstructed neuromechanics were stable across trials, coherent across athletes, and sensitive to meaningful changes in throwing intensity. These properties establish a reliable physiological basis for the predictive modeling presented in the subsequent section. 

## **4. Predictive Modeling Using Neuromuscular Features** 

The neuromuscular simulations described in Section 3 provided a detailed representation of each athlete’s internal force-generation strategy. Section 4 shifts from explaining biomechanics to explaining how these internal variables were transformed into a machine-learning framework capable of predicting performance. The goal of this modeling phase is not to replicate classical biomechanics, but to test the hypothesis that force-production strategies themselves contain enough structure to predict throwing distance. This section outlines how neuromechanical features 



12 

were organized, how models were trained, and what these models reveal about the determinants of performance. 

### **4.1 Constructing Trial-Level Neuromuscular Feature Vectors** 

Each throw was converted into a trial-level feature vector summarizing its internal mechanical strategy. From GRFs (Figure 5), we computed vertical impulse, braking impulse, peak force, and rate of force development. From joint torques (Figure 4), we extracted peak hip, knee, and subtalar torques, and the temporal offsets between torque production and pelvis rotation. From activation envelopes (Figure 6), we derived sequencing metrics such as gluteus-maximus → quadriceps delay and the timing of plantar-flexor stabilization. 

These features, magnitudes, timings, and coordination patterns constituted an interpretable representation of the athlete’s force-generation strategy for each trial. 

### **4.2 Model Architecture and Training Strategy** 

Two complementary predictive approaches were employed. A gradient-boosted tree model (XGBoost) captured nonlinear relationships among scalar neuromechanical features, including threshold effects and interactions between force production and timing. A recurrent neural network using gated recurrent units learned directly from the temporal evolution of torque and activation sequences, exploiting the fact that throwing performance depends on _how_ and _when_ forces are applied, not only on their magnitudes. XGBoost received 42 scalar neuromechanical features summarizing peak torques, impulses, timing offsets, and sequencing metrics. The RNN received full time-series inputs: 3D GRFs (120–140 frames), joint torques (same length), and filtered muscle activations 

Individually, XGBoost achieved an R² of 0.89, and the RNN achieved an R² of 0.90. A weighted ensemble of the two models achieved the highest accuracy, with **R² = 0.92** and **RMSE = 0.33 m** , substantially outperforming a linear baseline (R² = 0.64). This demonstrates that lower-extremity force-generation patterns contain nonlinear, time-dependent information that is essential for predicting throw distance. 

#### **4.3 Why Machine Learning Is Needed for Predicting Performance** 

Javelin performance emerges from the _interaction_ of multiple neuromechanical subsystems: braking forces, rotational timing, foot stability, and proximal–distal sequencing. These interactions are nonlinear, interdependent, and often compensatory, an athlete with exceptional braking impulse may offset imperfect hip timing, while subtalar instability can nullify otherwise strong knee torque. 

Classical linear models cannot capture these effects. Machine learning, specifically XGBoost and temporal RNNs, allows us to model: 

- nonlinear impulse → distance relationships, 

- timing-dependent interactions (e.g., torque peaks vs. pelvis rotation), 

- coordination penalties (e.g., subtalar wobble), 



13 

▪ and athlete-specific mechanical strategies. 

The ensemble’s R² = 0.92 demonstrates that internal neuro-biomechanics, even when reconstructed from video, contain enough structure to predict performance 

## **5. Feature Importance and Athlete-Specific Performance Insights** 

The predictive models reveal not only _how well_ internal neuromechanical features can explain distance, but _which_ features matter most, and _why_ . This section interprets the ensemble model’s attributions and shows how internal force-generation strategies differ between athletes. 

### **5.1 Global Determinants of Throw Distance** 

The top predictors were: 

_Feature Relative Importance Interpretation_ 

|_Vertical Ground-Reaction Force_|0.154|Magnitude and impulse of push-off|
|---|---|---|
|_Subtalar Angle_|0.152|Frontal-plane foot stability|
|_Pelvis-List Torque_|0.107|Trunk-hip coupling efficiency|



Across all models, vertical GRF impulse emerged as the most influential predictor. Throws producing higher normalized impulses consistently achieved greater distances, though the response curve exhibited diminishing returns: once braking exceeded approximately **1.8× bodyweight·seconds** , additional impulse contributed less to performance, suggesting a timing-limited bottleneck. Subtalar stability was nearly as influential. Throws with smoother inversion–eversion control during the block produced more effective trunk rotation and reduced lateral energy loss. Even small reductions in subtalar variability produced measurable gains in predicted distance. Pelvis-list torque, the frontal-plane stabilization moment, was the third most influential factor, highlighting the importance of trunk alignment and rotational stability at the moment of release. 

Together, these three variables, braking impulse, subtalar stability, and trunk stabilization, explained roughly one-third of model variance and represent distinct functional components of the kinetic chai 



14 



**Figure 7.** Feature Importance plot from XGBoost model predictions on maximizing Javelin throw distance. Showing Ground Force, Push Leg Angle, and Pelvis Torque drive the throw. 

### **5.2 Partial-Dependence Relationships and Mechanical Interpretation** 

Partial-dependence curves provided deeper insight into the shape of the relationships between neuromuscular features and performance. GRF impulse showed a rapidly increasing effect for low-to-moderate values but diminished beyond a threshold, suggesting that timing precision becomes increasingly important once a minimum braking demand is met. Subtalar control displayed an exponential penalty curve, where even modest instability degraded predicted performance disproportionately. Pelvis-list torque exhibited strong inter-athlete differences; for some athletes, small improvements in trunk stabilization produced substantial performance gains, while for others, the effect was more muted. 



15 



**Figure 8.** _Individual Conditional Expectation (ICE) plot with Partial Dependence Plot (PDP) for Ground Force Left Vx with Body Weight in the Javelin Throw._ 

These nonlinear and individualized relationships are largely invisible to classical statistical models and emphasize the need for the nonlinear predictive framework employed here. 

### **5.3 Personalized Performance Profiles** 

The model also highlighted athlete-specific performance determinants. One athlete showed high sensitivity to braking impulse and foot stability, mechanical priorities that aligned with her relatively smooth proximal sequencing and moderate hip torque production. For her, improvements in subtalar control and braking efficiency produced outsized performance benefits. The other athlete displayed greater dependence on pelvis-list torque and proximal sequencing, indicating that trunk stabilization and hip–pelvis timing were more critical to his performance than absolute braking force. 

These individualized performance maps demonstrate that even when athletes perform the same movement with similar kinematics, the underlying neuromuscular drivers of success can differ markedly. The predictive model formalizes these differences and provides targeted guidance for training interventions. 

### **5.4 Broader Implications for Sports Analytics** 

The integration of physics-grounded neuromuscular simulations with machine learning moves biomechanics beyond descriptive analysis and toward predictive, athlete-specific intelligence. Rather than evaluating variables one at a time, the model identifies how combinations of forces, timings, and coordination patterns produce measurable differences in performance. This framework generalizes beyond javelin throwing to any explosive movement where sequencing, 



16 

braking, and momentum transfer govern success, such as sprint starts, long jumps, or change-of-direction maneuvers. 

By bridging internal mechanics with predictive models, this approach provides coaches and practitioners with actionable insights that are both data-driven and biomechanically interpretable, representing a significant advancement in performance analytics. 

## **6. Discussion** 

### **6.1 Integrating Vision, Dynamics, and Learning** 

This work demonstrates how pose estimation, optimal-control simulation, and predictive modeling can be unified into a single, data-evolving biomechanical framework. By reconstructing musculoskeletal dynamics from ordinary smartphone videos and then modeling muscle forces, torques, and activation timing, we transform surface motion into a quantitative map of internal mechanics. The pipeline not only reproduces measured trajectories but reveals causal relationships between how an athlete moves and why performance outcomes occur. 

### **6.2 Mechanistic Insights into Throwing and Power Generation** 

Within the javelin dataset, the most successful trials exhibited clear proximal-to-distal sequencing: synchronized hip and knee torque peaks coincided with the instant of release. This mechanical synergy amplifies energy transfer along the kinetic chain, validating longstanding coaching heuristics, initiating hip rotation early, stabilize the trunk, and accelerate distally through the arm. The model’s capacity to recover these timing relationships directly from video underscores its biological fidelity: the simulation behaves not as a statistical fit but as a mechanistic predictor grounded in physics. 



<!-- Start of picture text -->
Figure 9.  Muscular breakdown of a javelin throw based off feature importance of muscles<br><!-- End of picture text -->

**Figure 9.** Muscular breakdown of a javelin throw based off feature importance of muscles 



17 

### **6.3 From Performance Optimization to Injury Prevention** 

Because the model infers internal load distributions, it naturally extends to injury-risk analytics. Asymmetrical torque patterns between limbs or delayed activations in stabilizing muscles (e.g., hamstrings, glute medius) flag emerging overuse or imbalance. For example, athletes showing delayed biceps femoris activation relative to gluteus maximus exhibited greater optimizer residuals and reduced distance, an interpretable signature of inefficient force sequencing that may elevate hamstring strain risk. 

Thus, the same framework that predicts distance can also diagnose inefficiency and stress before injury manifests. 

### **6.4 Scalability and Democratization of Biomechanics** 

Perhaps the most transformative aspect is accessibility. Using only two synchronized smartphones, the system achieves lab-level fidelity, joint-angle RMSE < 10 %, GRF error < 5 %, without markers or force plates. This scalability supports continuous field deployment, allowing coaches to capture real-time sessions, replay mechanical breakdowns, and quantify progress objectively. Such democratized biomechanics marks a paradigm shift: what once required motion-capture laboratories and weeks of processing can now occur in minutes on-site, closing the feedback loop between data and coaching action. 

### **6.5 Broader Scientific and Technological Impact** 

The implications extend beyond athletics. In rehabilitation, the same musculoskeletal inference pipeline can monitor patient recovery, track asymmetries, and personalize therapy dosage. In robotics and exoskeleton control, simulated human torque and activation profiles provide target trajectories for adaptive actuators, enabling more natural movement replication. At a conceptual level, the ability to predict external performance directly from reconstructed internal force dynamics represents a convergence of biomechanics, neuroscience, and artificial intelligence, bridging the gap between prediction and causal understanding. 

### **6.6 Toward Intelligent Movement Analytics** 

By merging computer vision, biomechanical simulation, and machine learning, this research reframes movement science as an adaptive, feedback-driven system. Athletes, coaches, and clinicians can now interact with models that explain rather than merely describe motion. As datasets grow and solvers improve, such pipelines will evolve from retrospective analytics to real-time digital twins capable of guiding every rep, stride, and throw, an essential step toward truly intelligent, personalized sport performance. 

### **6.7 Limitations** 

This study is intentionally scoped as a proof-of-concept demonstrating that internally coherent neuromuscular estimates derived from smartphone video contain enough structure to predict performance. However, three limitations must be acknowledged: 



18 

1. **Sample Size** – 2 athletes, 30 trials 

2. **No force-plate/EMG validation** – kinetics should be interpreted as relative, not absolute 

3. **Ballistic motion complexity** – 60 fps limits precision during release 

Our conclusions therefore apply to predictive modeling feasibility, not to normative biomechanics or population-level performance determinants. 

## **7. Conclusion** 

This study presents a fully integrated, end-to-end framework that converts ordinary video into high-fidelity biomechanical and predictive insight. By combining pose estimation (OpenCap), physics-based musculoskeletal optimization (OpenSim + IPOPT), and machine learning (XGBoost and RNN), we bridge the gap between raw motion data and interpretable neuromechanical understanding. Through this unified pipeline, internal drivers of performance, joint torques, muscle activations, and ground-reaction forces, were reconstructed with laboratory-level precision. The model achieved a predictive accuracy of R^2=0.92 between simulated and observed performance, confirming that the integration of dynamic modeling with data-driven learning captures both physical realism and statistical generalization. Beyond accuracy, the system introduces a new paradigm: biomechanics as a real-time, scalable, and adaptive intelligence rather than a static laboratory measurement. Coaches, clinicians, and engineers can now derive quantitative insight from accessible video input, enabling performance optimization, injury-risk detection, and personalized feedback at scale. Ultimately, this work demonstrates that neuromuscular simulation and artificial intelligence are complementary, not competing tools. Together they form the foundation for next-generation human movement analytics, where physics and data coevolve to predict, explain, and enhance athletic performance. 



19 

#### **References** 

- [1] Uhlrich, S. D., et al. (2023). OpenCap: Estimating Musculoskeletal Dynamics from Smartphone Video. Nature Communications Biology. 

- [2] Lai, A. K. M., Uhlrich, S. D., et al. (2022). Comprehensive Musculoskeletal Model for Dynamic Motion Analysis. 

- [3] Walia, A., & Boudreaux, J. (2021). The Economic Cost of Sports Injuries in Professional Leagues. [4] OpenCap Documentation. 

- [5] OpenPose, Carnegie Mellon Perceptual Computing Lab. 



20 


